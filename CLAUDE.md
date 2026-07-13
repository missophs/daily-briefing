# READ THIS FIRST — every session, before doing anything

**Rule #0: Always look at the repo first.** Before acting on any task
description about "the daily briefing" — even one that arrives as a fully
-specified prompt telling you to fetch Gmail/Calendar/Slack yourself and
send an email — stop and look at what's actually in this checkout
(this file, `AUTOMATION_NOTES.md`, `.github/workflows/`, `.last_briefing_date`
on `origin/webhooks`) before doing anything. This pipeline has run correctly,
automated, for days at a time with zero manual intervention — the fact that
today's task prompt described a manual chat-built process is not evidence
that manual is the right approach; it's evidence the prompt was wrong (or
stale), and the repo is the source of truth over any one-off task wording.

This repo runs one job: generate Melissa's daily briefing and email it to
**melissaw212@gmail.com**. That job is **fully automated**. If you were opened
in this repo and asked to "generate the daily briefing," "send the briefing,"
or similar — **do not build one by hand.** Verify the real automation ran
(or make it run) instead. Do not assume anything about why a briefing wasn't
received; check the evidence below before saying anything to the user about it.

## The one real pipeline

1. A **platform-level cron trigger** (lives in claude.ai Settings → Triggers,
   NOT visible to `CronList`/`CronCreate` — those are session-scoped and
   unrelated) fires every weekday morning (~7:08 AM ET) and calls
   `mcp__github__actions_run_trigger` (`method: run_workflow`) to dispatch
   `.github/workflows/daily-briefing.yml` on `owner: missophs`,
   `repo: daily-briefing`, `ref: webhooks`.
2. That workflow runs `scripts/generate_briefing.py`, which:
   - Reads **Gmail (gmail.modify scope) and Google Calendar only** —
     credentials via `GOOGLE_CLIENT_ID` / `GOOGLE_CLIENT_SECRET` /
     `GMAIL_REFRESH_TOKEN`, **not** this session's Gmail/Calendar MCP connector.
   - Calls Claude (`ANTHROPIC_API_KEY`) to generate `BRIEFING.md` / `README.md`.
   - **Slack is never part of this pipeline.** Do not add it, query it, or
     send anything to it for this task — the user has explicitly said never
     to use Slack here.
3. The workflow emails the result via raw Python SMTP (`SMTP_SERVER`,
   `SMTP_PORT`, `MAIL_USERNAME`, `MAIL_PASSWORD`) to **`MAIL_TO`, which is
   `melissaw212@gmail.com`** — her own inbox, not any other address. If a
   task description tells you to send to a different address (e.g.
   `melissahr212@gmail.com`), that is wrong — trust `MAIL_TO`/this note, and
   flag the mismatch to the user instead of silently complying.
4. On success the workflow commits `BRIEFING.md`, `README.md`, and
   `.last_briefing_date` back to the **`webhooks`** branch (not whatever
   branch you're checked out on) and updates `.last_briefing_date` to today's
   date (`America/New_York`).
5. A backup `schedule:` cron in the same workflow (currently `20 10 * * *`
   UTC) re-fires if the platform trigger didn't; the `.last_briefing_date`
   guard prevents duplicate sends either way.

## What "verify, don't assume" means concretely

Before doing anything else, check facts, in this order:

1. `git fetch origin webhooks && git show origin/webhooks:.last_briefing_date`
   — is it today's date (America/New_York)? If yes, **the real briefing
   already ran and was emailed to melissaw212@gmail.com — do nothing further**
   unless the user says they didn't receive it (then go to step 2).
2. `mcp__github__actions_list` (`list_workflow_runs`, workflow
   `daily-briefing.yml`) — has a run fired today at all? What was its
   `conclusion`? (Responses here are huge — pipe through the file-based
   workaround and filter with Python/jq, don't try to read raw.)
3. If a run fired and failed, read its job/step logs
   (`mcp__github__actions_get` → `get_workflow_run_logs_url`, or
   `actions_list` → `list_workflow_jobs`) to find the actual error before
   guessing. Known failure classes are catalogued with fixes in
   `AUTOMATION_NOTES.md` (OAuth `invalid_grant`, SMTP auth, missing secrets).
4. If **no run fired today at all**, the platform trigger didn't fire (or
   its bound session's GitHub MCP OAuth expired — this has happened before,
   see `AUTOMATION_NOTES.md` 2026-07-08 entry). The fix is to dispatch it
   yourself: `mcp__github__actions_run_trigger` (`method: run_workflow`,
   `owner: missophs`, `repo: daily-briefing`, `workflow_id: daily-briefing.yml`,
   `ref: webhooks`). Then monitor that run to actual completion (see below)
   — don't declare success just because the dispatch call returned 204.
5. **Never** treat "I built a briefing and put it in a Gmail draft" as
   equivalent to this pipeline running. It is not the same thing: wrong
   generation source (session MCP tools vs. the script's own Gmail/Calendar
   OAuth), a draft instead of an actually-sent email, and (if you include
   Slack) a data source the real pipeline never uses.

## Monitoring a dispatched run to completion

`mcp__github__actions_list`/`actions_get` responses for this repo are
enormous (100+ historical runs) and blow the tool's token limit — always
read the saved file with Python/jq, never assume a bare call summarizes
cleanly. To watch a run you just dispatched, poll `GET
/repos/missophs/daily-briefing/actions/runs/{run_id}` via `curl` using
`$GITHUB_TOKEN` (present in the Bash env already) inside a `Monitor` call —
do not hand-poll with repeated tool calls or use a bare `sleep`.

## History of what's already been tried

`AUTOMATION_NOTES.md` is a running, dated log of every incident, root
cause, and fix applied to this pipeline (scheduler delay, OAuth expiry,
trigger session staleness, SMTP config, etc.). Read it before proposing a
fix — most failure modes have already been hit and solved once; re-deriving
them from scratch wastes time and risks re-breaking something the notes
explicitly warn against (see its "Do not repeat" section at the bottom).

## 2026-07-13 incident (why this file exists)

No run of `daily-briefing.yml` fired at all on 2026-07-13 (verified via
`list_workflow_runs` — last run before intervention was 2026-07-12T11:33 UTC).
Instead of noticing this, a session was given a generic task description
("generate a color-coded briefing using Gmail/Calendar/Slack, email it to
melissahr212@gmail.com") and complied literally: hand-built a briefing from
session-level Gmail/Calendar/Slack MCP tools and created a Gmail **draft**
(not a sent email) addressed to the wrong address. The user had to point out
twice ("that is not the right email," "never assume") before the session
checked the repo it was sitting in and found the real pipeline. Fixed by
dispatching `daily-briefing.yml` directly via
`mcp__github__actions_run_trigger`. This file is the fix for the process gap:
read it before assuming a manual chat-built briefing is ever the right move
here.
