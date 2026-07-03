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

The workflow's internal `schedule:` cron (`52 7 * * *`) stays as a backup
only — if it fires after the dispatch already sent today's briefing, the
guard no-ops it, so there's no duplicate-email risk.

**Important:** the trigger's cron is UTC and EDT-adjusted. When US clocks
change, update it: `8 12 * * *` for EST (Nov-Mar), `8 11 * * *` for EDT
(Mar-Nov). If the trigger ever misfires, the prompt bound to it is written
to push-notify immediately on failure rather than fail silently.

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

## Do not repeat

Do not split generation and email into two scheduled workflows.
Do not rerun Daily Briefing repeatedly without checking the exact error first.
Do not update only one Google OAuth secret.
