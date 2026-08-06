---
type: project
title: Automated Morning Briefing
status: active
created: 2026-07-24
updated: 2026-07-25
repo: missophs/daily-briefing
branch: webhooks
tags: [gmail, automation, github-actions, email-triage, claude]
---

# Automated Morning Briefing

## Overview
A GitHub Actions workflow that runs every morning, triages Gmail, and generates a polished HTML executive briefing via Claude. Saves to BRIEFING.md and README.md on the `webhooks` branch of `missophs/daily-briefing`. A second, hourly workflow (`trash-newsletters.yml`) runs the same deterministic trash step alone, so matching senders don't sit in the inbox for up to 24h waiting on the daily run.

## Key Files
- `scripts/generate_briefing.py` — all logic lives here (shared by both workflows)
- `scripts/trash_newsletters.py` — hourly companion, calls the same trash function, no Claude API call
- `.github/workflows/daily-briefing.yml` — dual-cron daily workflow
- `.github/workflows/trash-newsletters.yml` — hourly trash-only workflow

## Workflow Schedule
- Daily briefing — primary cron: `30 9 * * *` (9:30 AM UTC = 5:30 AM EDT); backup cron: `15 10 * * *` (10:15 AM UTC)
- Guard step does `git pull origin webhooks` before checking `.last_briefing_date` to prevent double-sends
- Trash job — real reliability now comes from an **external cron-job.org job** ("Trash newsletters trigger", every 5 min) that POSTs directly to `https://api.github.com/repos/missophs/daily-briefing/actions/workflows/trash-newsletters.yml/dispatches` with an `Authorization: Bearer <PAT>` header and `Accept: application/vnd.github+json`, body `{"ref":"webhooks"}`. Set up and confirmed working 2026-07-26 (verified via a real `workflow_dispatch` run completing successfully). The GitHub PAT (classic, `repo` scope) lives only in cron-job.org's stored headers — expires ~1yr from creation, will need regenerating and re-pasting into cron-job.org when it does.
  - GitHub's own `schedule:` cron (`*/5 * * * *`, tightened from `*/15` on 2026-08-03) stays as a backup — GitHub's scheduled cron is best-effort and drifts (observed 1.5–4hr gaps at hourly, still drifted noticeably even at 15-min), so don't rely on it alone.
  - A `push` trigger on `trigger/heartbeat.txt` still exists as a third manual fallback (push to that path to force an immediate run).
  - Do NOT recreate the local `hourly-trash-heartbeat` scheduled-task pattern — tried 2026-07-25, proved unreliable (depends on a background daemon that wasn't running, silently never fired). Deleted.

## Email Triage Pipeline (in order)
1. **delete_spam()** — permanently deletes all SPAM-labeled messages
2. **trash_newsletter_emails()** — deterministic pattern match, no Claude API call
3. **classify_phishing()** — Claude API, skips protected senders
4. **rescue_protected_trash()** — deterministic rescue of protected senders from trash
5. **classify_legitimate_trash()** — Claude API rescue of remaining legitimate trash
6. **generate_briefing()** — Claude generates full HTML executive briefing

## Auto-Trash List (NEWSLETTER_TRASH_PATTERNS)
Case-insensitive substring match on From header. Single source of truth is `generate_briefing.py`; this list is kept in sync with it manually — check the code if in doubt:
- cooldeep, medium daily digest, @medium.com
- the average joe, averagejoecrypto
- 1% better, 1percentbetter, the ai report, theaireport
- optery, christopher rainey, giulia guerrieri, tradealgo
- j.t. o'donnell, jt o'donnell, jtodonnell, sophia davis
- fred from fireflies, fireflies.ai
- experteer, eharmony, pranit naik, quillbot, phil strazzulla
- limitless creator, 16handles, techpresso, stephanie adams
- ifttt, tldr newsletter, tldrnewsletter
- yesstyle, kohls, kohl's, melissa westgate, gap factory, gapfactory, gemma bonham
- info@skincareessentials.com, hello@digistore24newsletter.com, community@transform.us
- talentrealist@substack.com, talent realist
- email.nextdoor.com (consolidated 2026-07-26, catches all prefix/subdomain combos — reply@/no-reply@ × rs./is.)
- emailreplies@messages.classmates.com, team@craft.do, insider monkey
- lisa rangel, chameleonresumes.com, fractional in a box, fractionalpowerhouse.com
- car shield, carshield, tractorsupply
- uncovering ai, uncoverai@mail.beehiiv.com
- ai with mariah, dreamtuesday.com
- alison.com (Alison Courses — broadened 2026-07-27 to catch all subdomains: us-courses/us-skills/us-news/us-education), mail.lemon8-app.com (Lemon8)
- no-reply@otter.ai, students.udemy.com (Udemy), email.shoestation.com (Shoe Station)
- thepeoplepeoplegroup.com (Martin)
- send.zapier.com (Deb at Zapier), redroosterharlem (Red Rooster Harlem)
- sarmail.cuddly.com (Remo's Rescue via Cuddly), anyaandniki.com, mindstream.news, cultivatedculture.com (Austin Belcak), m.themuse.com (The Muse newsletter, not job alerts)
- 3percentconf.com (Katherine Gordon)
- leapsome.com (Trevor Murray)
- jackcocchiarella@substack.com
- jointhecolab@substack.com (the Co-Lab) — note: "The Average Joe <joe@readthejoe.com>" already covered by existing "the average joe" pattern, no new entry needed
- ridethroo.ai, mail.promptmates.ai (PromptMates)
- microsoftstore.microsoft.com (Microsoft Store), tealhq.com (David Fano)
- careerevolved=oliviagamber.com@f.kajabimail.net (Olivia Gamber)
- endeavorexecutive.com (Cord Harper)
- patient-voices.com
- kickresume.com (Tomas at Kickresume)
- peoplestrategycollective.org (People Strategy Collective membership)
- linktr.ee (Linktree)
- mycitizenshr.com (Citizens Careers)
- theskimm.com (theSkimm)
- workweek.com (Hebba Youssef)
- mail.apollo.io (Apollo)
- allevents.in (AllEvents)
- emails.zappos.com (Zappos)
- marketing.landsend.com (Lands' End)
- mail.shein.com (Shein), mgs.opentable.com (OpenTable recs), openart.ai (OpenArt marketing), noreply@glassdoor.com (Glassdoor job digest), donaldjtrump.com (Trump campaign) — added 2026-08-05
- e.targetoptical.com (Target Optical marketing — added 2026-08-05; does NOT match targetoptical.com receipt emails, which stay untouched)
- 360learning.com (Freddie at 360Learning) — added 2026-08-05
- m.send.coursera.org (Edureka, sent via Coursera) — added 2026-08-06

## Protected Senders (PROTECTED_SENDER_PATTERNS)
Never trashed; rescued from trash if found there:
- match.com
- **linkedin** — job alerts, always keep
- chatgpt, openai.com, claude, anthropic.com
- All major airlines
- Merrill Lynch (merrilllynch, merrill lynch, ml.com, merrilledge)
- All major banks (chase, bankofamerica, wellsfargo, citibank, usbank, tdbank, pnc, capitalone, schwab, fidelity, vanguard, synchrony, ally, discover, barclays, regions, suntrust, truist, navyfederal, usaa)

## Briefing Format
- **Triage Quick List**: inbox/rescued emails shown individually; trashed items as summary rows only (not line-by-line)
- Sections: Header → Executive Summary → Action Required → 7-Day Calendar → Job Search Pipeline → Full Email Review → Trash Review → Promotional Summary → Newsletters → Email Accounting → Dashboard → Action Items → Top 3 Priorities

## Key Decisions
- Deterministic trash runs before Claude API — faster, cheaper, reliable
- LinkedIn is protected — job alerts must never be trashed
- Trash triage table uses summary rows, not individual lines per trashed email
- Unsubscribing from newsletters doesn't work — auto-trash list is the fix

## Lessons Learned
- **CRITICAL**: Always verify code before pushing. A stray `tml` typo on a `max_tokens` line caused a Python SyntaxError that broke the entire daily briefing (2026-07-24).
- The hourly trash job's `fetch_emails()` originally capped at 50 messages across the whole mailbox (all labels, 2-day window) — on a busy mailbox, older inbox newsletters got pushed out of the fetch window and never evaluated. Fixed 2026-07-25 by adding `max_results`/`inbox_only` params so the hourly job searches only the inbox with a 200 cap; daily briefing's call is unaffected (defaults preserve prior behavior).
- Pattern strings must exactly match the real sender name — `"techspresso"` sat in the list for a while matching nothing because the actual sender is `"Techpresso"` (no middle "s"). A misspelled pattern fails silently; if a sender says it's "still not being trashed," check the exact spelling against a live email first, don't assume it's a timing/caching issue.
- A local scheduled-task heartbeat (meant to fix GH cron drift by pushing a file hourly) silently never fired after setup — it depends on a background daemon that wasn't running, and there's no easy way to see why it failed from the outside. Don't rely on this pattern for anything time-sensitive without confirming the daemon is alive first; increasing the GitHub Actions cron frequency directly (e.g. every 15 min instead of hourly) is a simpler, more verifiable fix for drift.
