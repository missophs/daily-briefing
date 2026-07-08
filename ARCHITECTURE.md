# Daily Briefing — Complete Architecture Specification

## 1. Repository

**Repo:** `missophs/daily-briefing`, branch `webhooks` (production branch — all automated work reads from and commits to this branch).

**All files:**

| File | Role |
|------|------|
| `.github/workflows/daily-briefing.yml` | Primary automated workflow |
| `.github/workflows/email-briefing.yml` | Legacy manual-only re-send workflow |
| `scripts/generate_briefing.py` | Core Python script: fetch data, generate HTML, write output |
| `scripts/get_google_token.py` | One-time local tool to generate GMAIL_REFRESH_TOKEN |
| `scripts/requirements.txt` | Python package dependencies |
| `.last_briefing_date` | State file: ET date string of last successful send |
| `BRIEFING.md` | Output: generated HTML briefing (name is misleading — content is HTML, not Markdown) |
| `README.md` | Identical to BRIEFING.md — same content written by same loop |
| `index.html` | Static web viewer SPA — fetches BRIEFING.md via JS fetch() |
| `netlify.toml` | Netlify configuration — build always ignored, sets HTTP security headers |
| `.nojekyll` | Empty file — suppresses GitHub Pages Jekyll processing |
| `SETUP.md` | Operational runbook (partially stale) |
| `AUTOMATION_NOTES.md` | Architecture history and incident log |
| `SUMMARY.md` | Stale status document |

---

## 2. Execution Flow — Happy Path

```
[7:08 AM ET]
Platform Trigger (trig_011NHYQpjSNTUK5kG85shGvM)
  │  cron: 8 11 * * *  (UTC, EDT = UTC-4)
  │  mode: create_new_session_on_fire=true
  │  DST: change to 8 12 * * * in November (EST = UTC-5)
  ↓
Fresh Claude Session
  │  calls: mcp__github__actions_run_trigger
  │    method: run_workflow
  │    owner: missophs / repo: daily-briefing
  │    workflow_id: daily-briefing.yml
  │    ref: webhooks
  ↓
GitHub Actions: daily-briefing.yml (ubuntu-latest)
  │  permissions: contents: write
  │
  ├─ Step 1: actions/checkout@v4
  │    clones webhooks branch
  │
  ├─ Step 2: Guard check (bash)
  │    TODAY=$(TZ=America/New_York date +'%Y-%m-%d')
  │    HOUR=$(TZ=America/New_York date +'%H')
  │    reads .last_briefing_date
  │    skip=true if: file exists AND content == TODAY
  │    skip=true if: event==schedule AND HOUR < 7
  │    otherwise: skip=false → proceed
  │    [outputs: today=YYYY-MM-DD, skip=true|false]
  │
  ├─ Step 3: actions/setup-python@v5
  │    python-version: '3.11'
  │    cache: pip
  │
  ├─ Step 4: pip install -r scripts/requirements.txt
  │    anthropic>=0.40.0
  │    google-auth>=2.22.0
  │    google-auth-oauthlib>=1.2.0
  │    google-api-python-client>=2.100.0
  │
  ├─ Step 5: python scripts/generate_briefing.py
  │    [env: ANTHROPIC_API_KEY, GOOGLE_CLIENT_ID,
  │           GOOGLE_CLIENT_SECRET, GMAIL_REFRESH_TOKEN]
  │    ↓
  │    build_google_credentials()
  │      Credentials(token=None, refresh_token=env[GMAIL_REFRESH_TOKEN],
  │        token_uri="https://oauth2.googleapis.com/token",
  │        client_id=env[GOOGLE_CLIENT_ID],
  │        client_secret=env[GOOGLE_CLIENT_SECRET],
  │        scopes=[gmail.readonly, calendar.readonly])
  │      creds.refresh(Request())  ← HTTPS POST to token endpoint
  │      → returns: access_token (short-lived)
  │    ↓
  │    fetch_emails(gmail_service, days=7)
  │      users().messages().list(userId="me",
  │        q="after:YYYY/MM/DD", maxResults=50,
  │        includeSpamTrash=True)
  │      → paginated, capped at 50 message IDs
  │      users().messages().get(id=..., format="metadata",
  │        metadataHeaders=["From","Subject","Date"])
  │      → 50 individual GET requests
  │      returns: list of dicts {from, subject, date, snippet,
  │                               unread, in_inbox, in_trash}
  │    ↓
  │    fetch_events(calendar_service, days=7)
  │      events().list(calendarId="primary",
  │        timeMin=now, timeMax=now+7days,
  │        singleEvents=True, orderBy="startTime",
  │        maxResults=30)
  │      returns: list of dicts {summary, start, end, location,
  │                               my_status, attendees, description}
  │    ↓
  │    generate_briefing(emails, events)
  │      client.messages.create(
  │        model="claude-sonnet-4-6",
  │        max_tokens=16000,
  │        messages=[{role:"user", content: PROMPT.format(...)}])
  │      strips code fences if present
  │      builds Python fallback: forced_sections (DEAD CODE — never used)
  │      builds accounting_section
  │      if "Email Accounting" not in Claude output: appends accounting_section
  │      returns: HTML string
  │    ↓
  │    writes BRIEFING.md  (HTML content, .md extension)
  │    writes README.md    (identical HTML content)
  │
  ├─ Step 6: capture date
  │    today=$(TZ=America/New_York date +'%Y-%m-%d %H:%M ET')
  │    [output: today=YYYY-MM-DD HH:MM ET]
  │
  ├─ Step 7: Email completed briefing (inline Python heredoc)
  │    reads BRIEFING.md → html string
  │    MIMEMultipart("alternative")
  │      From: "Melissa Daily Briefing <{MAIL_USERNAME}>"
  │      To: {MAIL_TO}
  │      Subject: "Melissa Daily Briefing - {today}"
  │      body: MIMEText(html, "html", "utf-8")
  │    if SMTP_PORT==465: SMTP_SSL(server, port).login().sendmail()
  │    if SMTP_PORT!=465: SMTP(server, port).ehlo().starttls()
  │                       .ehlo().login().sendmail()
  │    prints: "SMTP sendmail returned successfully"
  │    prints: "Email sent to {recipient}"
  │
  └─ Step 8: Commit changes
       echo "YYYY-MM-DD" > .last_briefing_date
       git config user.name "github-actions"
       git config user.email "github-actions@github.com"
       git add BRIEFING.md README.md .last_briefing_date
       git commit -m "Daily briefing update" || echo "No changes"
       git pull --rebase origin webhooks
       git push origin HEAD:webhooks
```

---

## 3. Scheduler — Two Layers

| Layer | Mechanism | Time | Reliability |
|-------|-----------|------|-------------|
| **Primary** | Platform trigger `trig_011NHYQpjSNTUK5kG85shGvM` | 7:08 AM ET (EDT), `8 11 * * *` | High — fresh session each fire, but depends on GitHub MCP connector OAuth being valid |
| **Backup** | `schedule: cron: '0 12 * * *'` in workflow | 8:00 AM UTC = 8:00 AM ET nominal, but subject to 0–4h GitHub scheduler delay | Low reliability on timing, but works as last resort |

**Backup fires only if primary failed:** `.last_briefing_date` guard catches duplicates. If primary already sent, guard sees today's date and sets `skip=true`.

**DST handling:** Manual. The platform trigger cron is UTC. Must be updated when US clocks change:
- EDT (Mar–Nov): `8 11 * * *`
- EST (Nov–Mar): `8 12 * * *`
- SETUP.md contains stale examples; AUTOMATION_NOTES.md has the current DST note.

---

## 4. Secrets — All 9 Required

All stored in GitHub repository secrets (`Settings → Secrets → Actions`).

| Secret | Used By | Purpose |
|--------|---------|---------|
| `ANTHROPIC_API_KEY` | `generate_briefing.py` | Anthropic Messages API authentication |
| `GOOGLE_CLIENT_ID` | `generate_briefing.py` | Google OAuth 2.0 client identity |
| `GOOGLE_CLIENT_SECRET` | `generate_briefing.py` | Google OAuth 2.0 client secret |
| `GMAIL_REFRESH_TOKEN` | `generate_briefing.py` | Long-lived token to get Gmail + Calendar access |
| `SMTP_SERVER` | Inline email step | Mail server hostname |
| `SMTP_PORT` | Inline email step | 465 (SMTP_SSL) or 587 (STARTTLS) |
| `MAIL_USERNAME` | Inline email step | Sender email address |
| `MAIL_PASSWORD` | Inline email step | Sender password or app password |
| `MAIL_TO` | Inline email step | Recipient (`melissaw212@gmail.com`) |

**Critical constraint:** `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, and `GMAIL_REFRESH_TOKEN` must always match. They must all come from the same Google OAuth Desktop App client (`daily-briefing-2026`, project `tough-talent-493313-u9`). Updating one without the others causes `invalid_client` or `unauthorized_client` errors.

---

## 5. Authentication

### Google OAuth 2.0 (Desktop App flow)
- **Client type:** Installed/Desktop App (not Web App) — required because redirect URI is `http://localhost` with no port
- **Token exchange:** `generate_briefing.py` calls `creds.refresh(Request())` which POSTs to `https://oauth2.googleapis.com/token` with the refresh token
- **No local state:** all credentials pass through environment variables; no token file on disk
- **Token expiry:** refresh token no longer expires every 7 days because the Google Cloud project is set to "In production" as of 2026-06-28. Refresh token only expires if user revokes access or changes their Google password.
- **One-time setup tool:** `scripts/get_google_token.py` — run locally on a Mac, not in CI. Uses manual URL-copy flow (no `run_local_server()`). Prints refresh token which is then added to GitHub secrets.

### Anthropic API
- Simple API key (`ANTHROPIC_API_KEY`), passed as header by the `anthropic` SDK
- No OAuth, no expiry mechanism in the workflow

### SMTP
- Username + password authentication, passed via secrets
- No OAuth

### GitHub Actions (workflow dispatch)
- Platform trigger authenticates via GitHub MCP connector (OAuth)
- Fresh sessions (`create_new_session_on_fire: true`) pick up current OAuth state
- No PAT currently in use

---

## 6. External APIs

| API | Call site | Method | Data fetched | Cap |
|-----|-----------|--------|--------------|-----|
| `https://oauth2.googleapis.com/token` | `build_google_credentials()` | POST | Access token | 1 call per run |
| Gmail API v1 `users.messages.list` | `fetch_emails()` | GET | Message IDs (last 7 days, including spam/trash) | 50 IDs, paginated |
| Gmail API v1 `users.messages.get` | `fetch_emails()` | GET (×N) | Message metadata (From, Subject, Date, snippet, labels) | Up to 50 individual calls |
| Google Calendar API v3 `events.list` | `fetch_events()` | GET | Next 7 days of primary calendar events | 30 events |
| Anthropic Messages API | `generate_briefing()` | POST | HTML briefing generation | 1 call, `max_tokens=16000` |
| SMTP server | Inline email step | SMTP | Email delivery | 1 send per run |

---

## 7. Environment Variables in Workflow

The workflow passes secrets as env vars to specific steps only (not globally):

```yaml
# Step: Generate real briefing
env:
  ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
  GOOGLE_CLIENT_ID: ${{ secrets.GOOGLE_CLIENT_ID }}
  GOOGLE_CLIENT_SECRET: ${{ secrets.GOOGLE_CLIENT_SECRET }}
  GMAIL_REFRESH_TOKEN: ${{ secrets.GMAIL_REFRESH_TOKEN }}

# Step: Email completed briefing
env:
  SMTP_SERVER: ${{ secrets.SMTP_SERVER }}
  SMTP_PORT: ${{ secrets.SMTP_PORT }}
  MAIL_USERNAME: ${{ secrets.MAIL_USERNAME }}
  MAIL_PASSWORD: ${{ secrets.MAIL_PASSWORD }}
  MAIL_TO: ${{ secrets.MAIL_TO }}
  EMAIL_SUBJECT: "Melissa Daily Briefing - ${{ steps.date.outputs.today }}"
```

No secrets are available globally. Each step sees only what it needs.

---

## 8. Output Files

| File | Content | Who writes it | Format |
|------|---------|---------------|--------|
| `BRIEFING.md` | Complete HTML briefing | `generate_briefing.py` | HTML (extension is misleading) |
| `README.md` | Identical to BRIEFING.md | `generate_briefing.py` | HTML |
| `.last_briefing_date` | ET date of last send (`YYYY-MM-DD\n`) | Commit step in workflow | Plain text |

`BRIEFING.md` and `README.md` are written in a `for filename in ("BRIEFING.md", "README.md")` loop — they are always byte-for-byte identical.

---

## 9. Timezone Handling

All timezone handling is explicit; the runner is UTC by default.

| Location | Mechanism |
|----------|-----------|
| Guard: today's date | `TZ=America/New_York date +'%Y-%m-%d'` |
| Guard: current hour | `TZ=America/New_York date +'%H'` |
| Email subject date | `TZ=America/New_York date +'%Y-%m-%d %H:%M ET'` |
| Calendar fetch window | `datetime.datetime.utcnow()` — UTC, not ET |
| Email fetch window | `datetime.date.today()` — runner's local time (UTC) |
| Platform trigger cron | UTC, manually adjusted per DST |

**Note:** Gmail email fetch uses `datetime.date.today()` which is UTC in the GitHub runner. Calendar fetch uses `datetime.datetime.utcnow()`. These are UTC-based, not ET-based, which means the "last 7 days" window is computed from UTC midnight, not ET midnight.

---

## 10. Error Handling

### Workflow level
- Each step uses `if: steps.guard.outputs.skip != 'true'` to skip all substantive steps when guard fires
- Git commit uses `|| echo "No changes"` to suppress error if nothing to commit
- **No `continue-on-error` anywhere** — a failure in any step fails the whole workflow

### Python script level
- `main()` wrapped in `try/except Exception as exc: print(f"\nERROR: {exc}", file=sys.stderr); sys.exit(1)`
- `sys.exit(1)` causes the GitHub Actions step to fail, which fails the workflow
- No retries anywhere in the Python script
- No timeouts set explicitly — default GitHub Actions step timeout is 6 hours; `max_tokens=16000` Anthropic call may take 30–90 seconds

### Email step
- No try/except — inline Python has no error handling
- SMTP failures surface as uncaught exceptions → step fails → workflow fails

---

## 11. Retry Logic

**There is no retry logic anywhere in the system.**

- GitHub Actions: no `retry` on any step
- Python script: no retry on Google API calls, no retry on Anthropic API call, no retry on Gmail list/get
- Email: no retry on SMTP
- Platform trigger: no retry — if MCP call fails, sends push notification; workflow never started
- Schedule backup: acts as a coarse-grained "retry" for the case where the platform trigger produced no workflow run at all

---

## 12. Timeout Handling

**No explicit timeouts are set anywhere.**

- GitHub Actions default: 6 hours per job
- Anthropic API call (`max_tokens=16000`): no timeout parameter in the SDK call; depends on Anthropic network latency
- Gmail API: up to 51 HTTP calls (1 list + 50 get) with no explicit timeout; `google-api-python-client` uses its own default HTTP timeout
- Calendar API: 1 HTTP call, no explicit timeout
- SMTP: no timeout on `smtplib` calls

---

## 13. Logging

All logging is to stdout/stderr, captured by GitHub Actions:

| What | Output |
|------|--------|
| Credential build | `"Building Google credentials…"` |
| Email count | `f"  {len(emails)} messages fetched"` |
| Event count | `f"  {len(events)} events fetched"` |
| Briefing generation | `"Generating briefing with Claude…"` |
| File save | `f"Saved BRIEFING.md + README.md ({len(briefing):,} chars)"` |
| Email sender | `f"Email from:    {sender}"` |
| Email recipient | `f"Email to:      {recipient}"` |
| Email subject | `f"Email subject: {subject}"` |
| SMTP success | `"SMTP sendmail returned successfully"` |
| SMTP result dict | `f"SMTP result: {result}"` |
| Delivery confirmation | `f"Email sent to {recipient}"` |
| Python errors | `f"\nERROR: {exc}"` (stderr) |

No structured logging, no log levels, no log aggregation.

---

## 14. Duplicate Prevention

The `.last_briefing_date` file is the only mechanism:

```
read at: Step 2 (Guard)
written at: Step 8 (Commit)
```

**Race condition:** Both reads happen before either writes. If two workflow runs start simultaneously (before either commits), both will pass the guard. This is unlikely in practice since `workflow_dispatch` events are serialized by GitHub, but the backup schedule run could theoretically overlap a dispatch run that is slow.

**State after email but before commit:** If the email step succeeds but the git commit/push fails, `.last_briefing_date` on the remote is NOT updated. A manual re-run same day would send a duplicate email.

---

## 15. Build and Deployment

**There is no build process.** The repo is pure Python + YAML. No compilation, no bundling, no transpilation.

**Deployment is the commit.** The workflow writes its outputs (BRIEFING.md, README.md, .last_briefing_date) and pushes them back to the `webhooks` branch. That push IS the deployment.

**Netlify:** `netlify.toml` sets `ignore = "exit 0"`, meaning every Netlify build hook call immediately exits 0 (success) without doing anything. Netlify never processes or deploys anything. The `netlify.toml` security headers are never applied because there is no Netlify deployment.

**GitHub Pages:** `.nojekyll` suppresses Jekyll. `index.html` is a static SPA. However, GitHub Pages requires either a public repo or a paid plan — this is a private repo and Pages is not enabled. The `index.html` is not served anywhere automatically.

---

## 16. Dead Code

| Location | Dead code | Impact |
|----------|-----------|--------|
| `generate_briefing.py` lines 394–452 | `_category()`, `groups`, `counts`, `color_map`, `email_rows` | All computed, never used — `forced_sections` variable built from `email_rows` is defined on line 454 but never appended to output |
| `generate_briefing.py` lines 454–472 | `forced_sections` variable | Defined, never referenced after definition |
| `accounting_section` (lines 474–483) | Only appended if Claude's output lacks "Email Accounting" | Claude reliably includes it, so this is rarely if ever used |
| `email-briefing.yml` | `dawidd6/action-send-mail@v4` dependency | Workflow is manual-only, used for manual re-send; not part of automated flow |

---

## 17. Every Failure Path

| Failure | Point | Consequence | Recovery |
|---------|-------|-------------|----------|
| Platform trigger MCP auth expired | Trigger fires, MCP call fails | No workflow dispatched, push notification sent | Schedule backup fires; user gets notification, manually triggers |
| Schedule backup not dispatched | GitHub scheduler delay | Late delivery (0–4h delay) | None — last resort |
| Guard skips (already sent) | Step 2 | Workflow exits early, no duplicate | Correct behavior |
| Guard skips (schedule before 7 AM ET) | Step 2 | Workflow exits early | Platform trigger should have already run |
| `invalid_grant` / `unauthorized_client` | `build_google_credentials()` | Workflow fails at Step 5; no email sent; `.last_briefing_date` not updated | Regenerate all 3 Google secrets using `get_google_token.py` |
| Gmail API quota / 429 | `fetch_emails()` | Workflow fails at Step 5 | Retry manually |
| Anthropic API error | `generate_briefing()` | Workflow fails at Step 5; no email sent | Retry manually |
| SMTP authentication failure | Email step | Workflow fails at Step 7; briefing was generated but not sent | Check SMTP credentials; `.last_briefing_date` not updated so re-run is safe |
| SMTP connection failure | Email step | Same as above | Same |
| Git push conflict | Commit step | Workflow may fail; `.last_briefing_date` not updated on remote | Email was already sent; re-run would send duplicate |
| Missing GitHub secret | Any step that uses it | Workflow fails with empty env var | Add missing secret in GitHub settings |

---

## 18. Legacy / Stale Elements

| Element | Status | Risk |
|---------|--------|------|
| `email-briefing.yml` | Manual-only, not automated | None — safe to leave |
| `SETUP.md` | References old OAuth client ID (`...rh81...`) and local Mac file paths | Confusion if followed literally — would cause `unauthorized_client` errors |
| `SUMMARY.md` | Describes two-workflow architecture that no longer exists | Misleading documentation |
| `index.html` + `.nojekyll` | Static SPA for web viewing; Pages not enabled | Unused infrastructure |
| `netlify.toml` | Configured but always ignored | No risk; prevents Netlify credit consumption |

---

## 19. Dependency Graph

```
trig_011NHYQpjSNTUK5kG85shGvM (Claude Code Remote platform)
  └─ GitHub MCP connector (OAuth, must be valid)
      └─ daily-briefing.yml (GitHub Actions, webhooks branch)
          ├─ .last_briefing_date (state, read)
          ├─ actions/checkout@v4 (GitHub marketplace)
          ├─ actions/setup-python@v5 (GitHub marketplace)
          ├─ scripts/requirements.txt
          │   ├─ anthropic>=0.40.0 (PyPI)
          │   │   └─ Anthropic Messages API (HTTPS, api.anthropic.com)
          │   ├─ google-auth>=2.22.0 (PyPI)
          │   │   └─ Google Token API (HTTPS, oauth2.googleapis.com)
          │   ├─ google-auth-oauthlib>=1.2.0 (PyPI)
          │   └─ google-api-python-client>=2.100.0 (PyPI)
          │       ├─ Gmail API v1 (HTTPS, googleapis.com)
          │       └─ Calendar API v3 (HTTPS, googleapis.com)
          ├─ scripts/generate_briefing.py
          │   ├─ reads: env vars (9 secrets)
          │   └─ writes: BRIEFING.md, README.md
          ├─ BRIEFING.md (read by email step)
          ├─ SMTP server (external, credentials in secrets)
          ├─ .last_briefing_date (write)
          ├─ BRIEFING.md (staged)
          ├─ README.md (staged)
          └─ webhooks branch (git push target)
```
