# Daily Briefing Automation Notes

## Current setup

Daily Briefing now runs as one GitHub Actions workflow.

It does all of this in one run:

1. Reads Gmail and Calendar
2. Generates BRIEFING.md and README.md
3. Emails the completed briefing using Python SMTP
4. Commits the updated files back to GitHub

## Schedule

**2026-07-03: switched the primary delivery mechanism away from GitHub's
`schedule:` trigger entirely.** Four consecutive days of data showed the
scheduler delay is random within a wide range (2.5h-4h), not a fixed offset:

- 2026-06-30: scheduled ~9:15 UTC, started 13:15 UTC (4h)
- 2026-07-01: scheduled ~9:15 UTC, started 12:17 UTC (~3h02m)
- 2026-07-02: scheduled 7:07 UTC, started 10:13 UTC (~3h06m), landed 6:15 AM ET
- 2026-07-03: scheduled 7:52 UTC, started 10:20 UTC (~2h29m), landed 6:24 AM ET

No cron time can compensate for a delay that swings by 1.5+ hours day to day.
Nudging the cron repeatedly (8+ times across this repo's history) was
chasing the symptom.

**Fix:** a platform-level scheduled trigger (`daily-briefing-dispatch`, cron
`8 11 * * *` = 7:08 AM ET, bound to resume the Claude session at
`session_019hb3CbfvEtCvSSU2hL7rtn`) fires `workflow_dispatch` on
`daily-briefing.yml` directly every morning via `mcp__github__actions_run_trigger`
(method `run_workflow`, ref `webhooks`). `workflow_dispatch` runs start
almost immediately — no scheduler queue. Tested end-to-end on 2026-07-03:
dispatch succeeded, workflow ran in 5s (correctly skipped via the
`.last_briefing_date` guard since that day's briefing was already sent).

The trigger prompt also checks its own fire time against the 7:08 AM ET
target and push-notifies if it fired more than ~20 min early/late, since a
successful-but-late dispatch wouldn't otherwise be distinguishable from a
normal on-time one.

The workflow's internal `schedule:` cron stays as a backup
only — if it fires after the dispatch already sent today's briefing, the
guard no-ops it, so there's no duplicate-email risk.

**2026-07-03, later: shifted backup cron 45min later again (7:52 → 8:37
UTC).** The 7/3 data point above (scheduled 7:52 UTC, landed 6:24 AM ET) was
55 min earlier than needed — plenty of unused buffer against the 7:15 AM ET
target. Moved the cron another 45 min later, to `37 8 * * *` (8:37 UTC),
to tighten the buffer further. If the ~2.5h delay observed on 7/2 and 7/3
holds, this should land close to 7:05-7:10 AM ET.

Caveat: 8:37 UTC scheduled + a shorter-than-usual delay could put the
`schedule:` run close in time to the 7:08 AM ET dispatch trigger. The
`.last_briefing_date` guard is only checked at job start, not held for the
job's duration, so if both runs start within the same generate+send window
(before either commits the guard file) there's a real duplicate-email risk.
Watch for this if both a schedule-triggered and dispatch-triggered run show
up close together in the Actions history.

**Important:** the trigger's cron is UTC and EDT-adjusted. When US clocks
change, update it: `8 12 * * *` for EST (Nov-Mar), `8 11 * * *` for EDT
(Mar-Nov). If the trigger ever misfires, the prompt bound to it is written
to push-notify immediately on failure rather than fail silently.

**2026-07-04: MCP connector auth failure + two additional fixes.**

What went wrong on 7/4:
- The platform trigger fired at exactly 7:08 AM ET ✓
- BUT the GitHub MCP connector OAuth had expired overnight → dispatch call
  failed silently with "requires authentication"
- A push notification was sent but was NOT received by the user
- Briefing arrived at 7:28 AM ET only after manual intervention

Fix 1 — PAT-based dispatch (eliminates auth expiry entirely):
Trigger prompt updated to use `curl` directly against the GitHub REST API
with a Personal Access Token (classic, `workflow` scope, no expiry) instead
of `mcp__github__actions_run_trigger`. There is no OAuth token to expire.
The PAT is embedded in the trigger config (private to the user's account).
Trigger ID: `trig_01UZzMZK9Vur8wLFnfmWvE4a`.

Fix 2 — Backup schedule cron race condition (eliminates duplicate emails):
Added `concurrency: group: daily-briefing` to the workflow so simultaneous
runs queue rather than overlap. Added a time guard: schedule-triggered runs
skip if it is before 7 AM ET, preventing early delivery when GitHub's
scheduler is unusually fast. Schedule cron remains `0 8 * * *` UTC as a
last-resort backup only.

Push notification gap: the 7/4 failure notification was sent but not received.
Cause unknown — may be a device notification settings issue. Investigate if
it happens again.

### Real cause of late/missed deliveries (2026-07-01)

This is NOT a case of "a few minutes late." GitHub's `schedule:` trigger is
best-effort: under load, GitHub queues cron-triggered runs and can delay them
by hours, not minutes. Evidence from run history:

- 2026-06-30: scheduled ~9:15 UTC, actually started 13:15 UTC (4h late)
- 2026-07-01: scheduled ~9:15 UTC, actually started 12:17 UTC (3h late), landed in
  the inbox at 8:21 AM ET instead of 7:15 AM ET

Every prior fix in this repo's history just nudged the cron time earlier
(10:50 → 8:30 → 7:55 → 6:30 → 8:30 → 11:15 → 9:15 UTC). That's chasing the
symptom — the delay is inconsistent and has been growing, so an earlier cron
time buys margin but is not a guarantee.

Two things applied now:
1. Moved off the top-of-hour/quarter-hour mark (`:15`) to an off-peak minute
   (`:07`) — GitHub explicitly recommends this because round minutes are the
   most congested slots on their shared scheduler.
2. Widened the buffer to ~3 hours before the 7:15 AM ET target, based on the
   worst observed delay above.

If this still lands late: the durable fix is to stop relying on GitHub's
`schedule:` trigger entirely and instead have an external cron service
(e.g. cron-job.org) call the GitHub REST API to fire a `workflow_dispatch`
event at exactly 7:15 AM ET. `workflow_dispatch` runs start almost
immediately since they aren't subject to the same scheduler queue as
`schedule:` events.

## Important fixes

The old setup used two workflows:

- Daily Briefing
- Email Daily Briefing

That was fragile because email could run before the briefing was generated.

The separate Email Daily Briefing workflow is now manual only.

## Google OAuth fix

The old Google OAuth client stopped working.

Final fix:

- Created a new Google OAuth Desktop App client
- Updated GOOGLE_CLIENT_ID
- Updated GOOGLE_CLIENT_SECRET
- Generated and updated GMAIL_REFRESH_TOKEN

These three must always match:

GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET
GMAIL_REFRESH_TOKEN

## Email fix

Email is now sent inside Daily Briefing using Python SMTP.

The workflow supports:

- SMTP_SSL for port 465
- STARTTLS for port 587

Successful logs should include:

SMTP sendmail returned successfully
Email sent →

## 2026-07-05: Google OAuth refresh + trigger fix

### What broke
- GMAIL_REFRESH_TOKEN expired → `invalid_grant` errors in workflow
- GitHub PAT used for dispatch returned HTTP 403 (now replaced with GitHub MCP)
- All GitHub secrets were missing and had to be re-added manually

### What was fixed

**Trigger (no more PAT):** The `daily-briefing-dispatch` trigger (ID: `trig_014Ekax1er6ujqdCNwKjsCmZ`,
cron `8 11 * * *` = 7:08 AM ET) now calls `mcp__github__actions_run_trigger` directly
via GitHub MCP — no PAT required, no OAuth expiry to worry about.
Bound to session `session_019hb3CbfvEtCvSSU2hL7rtn`.

**OAuth token regenerated:** New GMAIL_REFRESH_TOKEN generated on 2026-07-05 using
`scripts/get_google_token.py` (manual URL-copy flow — avoids localhost redirect issue).
All three secrets updated in GitHub to match (values in GitHub repository secrets —
do NOT commit them here):
- GOOGLE_CLIENT_ID — Google Cloud Console → OAuth 2.0 Client → `daily-briefing-2026`
- GOOGLE_CLIENT_SECRET — same client
- GMAIL_REFRESH_TOKEN — regenerated 2026-07-05

**Netlify build credits:** Added `ignore = "exit 0"` to `netlify.toml` so pushes to
`webhooks` branch no longer trigger Netlify builds. The email delivery is entirely
GitHub Actions → SMTP and does not involve Netlify.

**`scripts/get_google_token.py` rewritten:** Old version used `run_local_server()` which
failed because localhost redirect never completed. New version uses manual URL-copy:
displays auth URL, user visits browser, copies the full `http://localhost/?code=...` URL
from address bar after "can't connect" error, pastes into terminal.

### If refresh token expires again
1. Run `python3 scripts/get_google_token.py` on your Mac from `~/daily-briefing/` (webhooks branch)
2. Paste GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET when prompted
3. Visit the URL, click Advanced → Go to app (unsafe), copy the localhost callback URL
4. Paste it in terminal — get the refresh token
5. Update ALL THREE secrets in GitHub to match (client ID, secret, refresh token must match)

### Computer does not need to be on
Everything runs in the cloud. The trigger lives on Anthropic's servers, fires into
the Claude session, which calls GitHub Actions (also cloud). No Mac required.

### DST reminder
- EDT (Mar–Nov): cron `8 11 * * *` = 7:08 AM ET ✓ (current)
- EST (Nov–Mar): update trigger to `8 12 * * *` = 7:08 AM ET

## 2026-07-08: Stale session auth failure + schedule backup restored

### What broke (July 7–8)
- Platform trigger (`trig_014Ekax1er6ujqdCNwKjsCmZ`) fired at 7:08 AM ET both days
- But it was bound to session `session_019hb3CbfvEtCvSSU2hL7rtn` (months old) whose GitHub MCP OAuth had expired
- Result: trigger fired → MCP call failed silently → NO workflow dispatched → NO briefing for 2 days

### Root cause
GitHub MCP uses OAuth. The OAuth token in the long-running bound session expires over time.
When the trigger resumes that old session, the MCP call requires re-auth, which can't happen non-interactively.

### Fixes applied (2026-07-08)

**Fix 1 — Trigger now uses fresh sessions:**
Deleted `trig_014Ekax1er6ujqdCNwKjsCmZ` and recreated as new trigger with `create_new_session_on_fire: true`.
Each morning creates a brand-new session (no stale OAuth). Fresh sessions pick up the user's current
connector auth state, which is valid as long as the GitHub MCP connector is authorized in claude.ai settings.

New trigger ID: see below.
Cron unchanged: `8 11 * * *` = 7:08 AM ET (EDT). Update to `8 12 * * *` for EST (Nov–Mar).

**Fix 2 — Schedule backup restored:**
Added `schedule: cron: '0 12 * * *'` (8 AM ET) back to `daily-briefing.yml` as last-resort backup.
The `.last_briefing_date` guard prevents duplicate sends — if the platform trigger already ran,
the schedule run sees today's date and skips. Only fires the full briefing if the platform trigger failed.
GitHub schedule may be delayed 2-4h, but even a 10 AM delivery beats no delivery.

**July 8 manual recovery:**
Dispatched today's briefing manually at 4:29 PM ET. Delivered successfully.

### If GitHub MCP connector loses auth again
Sign in at claude.ai → Settings → Connectors → GitHub → reconnect.
Fresh-session triggers pick up the renewed auth automatically on the next fire.

### Trigger state after 2026-07-08 fix
- Primary: platform trigger with `create_new_session_on_fire: true`, cron `8 11 * * *` (EDT)
- Backup: workflow `schedule: '0 12 * * *'` (8 AM ET) — last resort, may be delayed

## Do not repeat

Do not split generation and email into two scheduled workflows.
Do not rerun Daily Briefing repeatedly without checking the exact error first.
Do not update only one Google OAuth secret — GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, and GMAIL_REFRESH_TOKEN must always match.
Do not bind the dispatch trigger to a persistent session — use create_new_session_on_fire: true so each firing gets fresh OAuth state.
