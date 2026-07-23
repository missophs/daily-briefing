#!/usr/bin/env python3
"""
Fetch Gmail + Google Calendar data and generate BRIEFING.md via Claude.
Called by .github/workflows/daily-briefing.yml.
"""

from __future__ import annotations

import json
import os
import re
import sys
import socket
import smtplib
import time
import datetime
import zoneinfo
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import anthropic


SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/calendar.readonly",
]

# Global socket timeout — applies to all Google API HTTP calls.
socket.setdefaulttimeout(60)


def _retry(fn, *, attempts=3, delay=2):
    """Call fn up to `attempts` times with exponential backoff on any exception."""
    for attempt in range(1, attempts + 1):
        try:
            return fn()
        except Exception as exc:
            if attempt == attempts:
                raise
            wait = delay * (2 ** (attempt - 1))
            print(f"  Attempt {attempt}/{attempts} failed ({exc}). Retrying in {wait}s…", flush=True)
            time.sleep(wait)


# ── Google credentials ──────────────────────────────────────────────────────────

def build_google_credentials() -> Credentials:
    creds = Credentials(
        token=None,
        refresh_token=os.environ["GMAIL_REFRESH_TOKEN"],
        token_uri="https://oauth2.googleapis.com/token",
        client_id=os.environ["GOOGLE_CLIENT_ID"],
        client_secret=os.environ["GOOGLE_CLIENT_SECRET"],
        scopes=SCOPES,
    )
    creds.refresh(Request())
    return creds


# ── Gmail ───────────────────────────────────────────────────────────────────────

def _header(headers: list, name: str) -> str:
    for h in headers:
        if h["name"].lower() == name.lower():
            return h["value"]
    return ""


def fetch_emails(service, days: int = 7) -> list[dict]:
    after = (datetime.date.today() - datetime.timedelta(days=days)).strftime("%Y/%m/%d")

    ids, page_token = [], None
    while len(ids) < 50:
        resp = _retry(lambda pt=page_token: service.users().messages().list(
            userId="me",
            q=f"after:{after}",
            maxResults=50,
            pageToken=pt,
            includeSpamTrash=True,
        ).execute())
        ids.extend(resp.get("messages", []))
        page_token = resp.get("nextPageToken")
        if not page_token:
            break

    emails = []
    for ref in ids[:50]:
        msg = _retry(lambda r=ref: service.users().messages().get(
            userId="me",
            id=r["id"],
            format="metadata",
            metadataHeaders=["From", "Subject", "Date"],
        ).execute())
        labels = msg.get("labelIds", [])
        hdrs   = msg.get("payload", {}).get("headers", [])
        emails.append({
            "id":       ref["id"],
            "from":     _header(hdrs, "From"),
            "subject":  _header(hdrs, "Subject"),
            "date":     _header(hdrs, "Date"),
            "snippet":  msg.get("snippet", "")[:150],
            "unread":   "UNREAD"  in labels,
            "in_inbox": "INBOX"   in labels,
            "in_trash": "TRASH"   in labels,
        })
    return emails


# ── Phishing auto-trash ──────────────────────────────────────────────────────────

PHISHING_PROMPT = """\
You are a security triage assistant. Review these emails and identify ONLY the ones \
that are high-confidence phishing or malicious — credential-harvesting attempts, \
spoofed senders impersonating a known service/bank/employer with urgent account-\
threat language, fake invoice/wire-fraud attempts, or similar clear attacks.

Do NOT flag: newsletters, marketing, legitimate bills, recruiter/networking messages, \
or anything merely low-value or ambiguous. When unsure, do not flag it — false \
positives here get an email auto-deleted, so only flag what you are highly confident \
is malicious.

EMAILS:
{emails}

Return ONLY a JSON object, no markdown, no explanation:
{{"phishing": [{{"id": "<message id>", "reason": "<short reason>"}}]}}
If none qualify, return {{"phishing": []}}.
"""


def classify_phishing(client: "anthropic.Anthropic", emails: list) -> dict:
    candidates = [e for e in emails if not e["in_trash"]]
    if not candidates:
        return {}
    slim = [{"id": e["id"], "from": e["from"], "subject": e["subject"], "snippet": e["snippet"]} for e in candidates]
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        messages=[{"role": "user", "content": PHISHING_PROMPT.format(emails=json.dumps(slim, indent=2))}],
    )
    text = message.content[0].text.strip()
    text = re.sub(r"^```(?:json)?\n?", "", text)
    text = re.sub(r"\n?```$", "", text.rstrip())
    data = json.loads(text)
    return {item["id"]: item.get("reason", "") for item in data.get("phishing", [])}


def trash_phishing_emails(service, phishing: dict) -> None:
    for msg_id, reason in phishing.items():
        try:
            _retry(lambda m=msg_id: service.users().messages().trash(userId="me", id=m).execute())
            print(f"  Trashed {msg_id}: {reason}")
        except Exception as exc:
            print(f"  Failed to trash {msg_id}: {exc}")


# ── Rescue legitimate emails from Trash ─────────────────────────────────────────

RESCUE_PROMPT = """\
You are a helpful email assistant. Review these emails that are currently in the Trash.
Identify any that appear to be legitimate and important — emails Melissa would likely
want rescued back to her inbox. These include:
- Purchase or payment receipts from real companies
- Government or emergency alerts
- Job application responses (from Greenhouse, Lever, Workday, hiring portals, etc.)
- Bank or financial alerts from real institution domains (chase.com, bankofamerica.com, wellsfargo.com, etc.)
- Subscription or account confirmations from known services (OpenAI, Perplexity, Apple, Google, etc.)
- Vet, medical, or appointment-related emails
- Direct personal or professional correspondence from real people

Do NOT rescue: marketing emails, newsletters, retail promotions, sale announcements,
spam, social network digests, or anything clearly unwanted even if from a real company.

EMAILS IN TRASH:
{emails}

Return ONLY a JSON object, no markdown, no explanation:
{{"rescue": [{{"id": "<message id>", "reason": "<short reason why legitimate>"}}]}}
If none qualify, return {{"rescue": []}}.
"""


def classify_legitimate_trash(client: "anthropic.Anthropic", emails: list) -> dict:
    trash_emails = [e for e in emails if e["in_trash"] and not e.get("auto_trashed")]
    if not trash_emails:
        return {}
    slim = [{"id": e["id"], "from": e["from"], "subject": e["subject"], "snippet": e["snippet"]} for e in trash_emails]
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        messages=[{"role": "user", "content": RESCUE_PROMPT.format(emails=json.dumps(slim, indent=2))}],
    )
    text = message.content[0].text.strip()
    text = re.sub(r"^```(?:json)?\n?", "", text)
    text = re.sub(r"\n?```$", "", text.rstrip())
    data = json.loads(text)
    return {item["id"]: item.get("reason", "") for item in data.get("rescue", [])}


def rescue_emails(service, to_rescue: dict) -> None:
    for msg_id, reason in to_rescue.items():
        try:
            _retry(lambda m=msg_id: service.users().messages().untrash(userId="me", id=m).execute())
            print(f"  Rescued to inbox {msg_id}: {reason}")
        except Exception as exc:
            print(f"  Failed to rescue {msg_id}: {exc}")


# ── Individual email triage summary ─────────────────────────────────────────────

SUMMARY_PROMPT = """\
You are Melissa's email assistant. Write a short daily email digest.

For EVERY email below, write exactly one line in this format:
• [CATEGORY] From: [sender name] — [subject] — [one sentence summary of what it is]

Categories to use: INBOX | RESCUED | TRASHED | TRASH

- INBOX = currently in inbox, normal email
- RESCUED = was in trash, moved back to inbox automatically (flagged rescued_from_trash: true)
- TRASHED = auto-trashed as phishing (flagged auto_trashed: true)
- TRASH = already in trash, not rescued, not phishing

Sort by: RESCUED first, then INBOX, then TRASHED, then TRASH.
Be concise. One line per email, no exceptions.

EMAILS:
{emails}

Return plain text only. No markdown. No headers. Just the bullet list.
"""


def generate_email_summary(client: "anthropic.Anthropic", emails: list) -> str:
    slim = [{
        "from": e["from"],
        "subject": e["subject"],
        "snippet": e["snippet"],
        "auto_trashed": e.get("auto_trashed", False),
        "auto_trash_reason": e.get("auto_trash_reason", ""),
        "rescued_from_trash": e.get("rescued_from_trash", False),
        "rescue_reason": e.get("rescue_reason", ""),
        "in_trash": e["in_trash"],
        "in_inbox": e["in_inbox"],
    } for e in emails]
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4000,
        messages=[{"role": "user", "content": SUMMARY_PROMPT.format(emails=json.dumps(slim, indent=2))}],
    )
    return message.content[0].text.strip()


def send_triage_summary(summary_text: str, phishing: dict, rescued: dict) -> None:
    sender    = os.environ["MAIL_USERNAME"]
    recipient = os.environ["MAIL_TO"]
    today_str = datetime.date.today().strftime("%A, %B %-d, %Y")
    subject   = f"📬 Email Triage Summary – {today_str}"

    trashed_count = len(phishing)
    rescued_count = len(rescued)

    header_lines = [f"📬 Email Triage – {today_str}", ""]
    if trashed_count:
        header_lines.append(f"🗑 {trashed_count} phishing email(s) auto-trashed")
    if rescued_count:
        header_lines.append(f"✅ {rescued_count} email(s) rescued from trash to inbox")
    if not trashed_count and not rescued_count:
        header_lines.append("Inbox looks clean — nothing trashed or rescued today.")
    header_lines += ["", "— Individual Email Summary —", ""]

    body = "\n".join(header_lines) + "\n" + summary_text

    msg = MIMEMultipart("alternative")
    msg["From"]    = f"Melissa Daily Briefing <{sender}>"
    msg["To"]      = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain", "utf-8"))

    smtp_server = os.environ["SMTP_SERVER"]
    smtp_port   = int(os.environ["SMTP_PORT"])
    if smtp_port == 465:
        with smtplib.SMTP_SSL(smtp_server, smtp_port, timeout=30) as server:
            server.login(sender, os.environ["MAIL_PASSWORD"])
            server.sendmail(sender, [recipient], msg.as_string())
    else:
        with smtplib.SMTP(smtp_server, smtp_port, timeout=30) as server:
            server.ehlo(); server.starttls(); server.ehlo()
            server.login(sender, os.environ["MAIL_PASSWORD"])
            server.sendmail(sender, [recipient], msg.as_string())
    print(f"Triage summary sent to {recipient}")


# ── Google Calendar ─────────────────────────────────────────────────────────────

def fetch_events(service, days: int = 7) -> list[dict]:
    et_tz = zoneinfo.ZoneInfo("America/New_York")
    day_start = datetime.datetime.now(et_tz).replace(hour=0, minute=0, second=0, microsecond=0)
    day_end   = day_start + datetime.timedelta(days=days)

    result = _retry(lambda: service.events().list(
        calendarId="primary",
        timeMin=day_start.isoformat(),
        timeMax=day_end.isoformat(),
        singleEvents=True,
        orderBy="startTime",
        maxResults=30,
    ).execute())

    events = []
    for e in result.get("items", []):
        my_response = ""
        for a in e.get("attendees", []):
            if a.get("self"):
                my_response = a.get("responseStatus", "")
        events.append({
            "summary":     e.get("summary", "(No title)"),
            "start":       e["start"].get("dateTime", e["start"].get("date", "")),
            "end":         e["end"].get("dateTime",   e["end"].get("date", "")),
            "location":    e.get("location", ""),
            "my_status":   my_response or e.get("status", ""),
            "attendees":   [a.get("email", "") for a in e.get("attendees", []) if not a.get("self")],
            "description": (e.get("description") or "")[:300],
        })
    return events


# ── Claude briefing prompt ───────────────────────────────────────────────────────

PROMPT = """\
You are Melissa's Executive Chief of Staff.

You are reviewing Gmail, Gmail Trash, and Google Calendar.

You must create a polished, color-coded, easy-to-read HTML executive briefing.

Today: {today}

GMAIL DATA:
{emails}

CALENDAR DATA:
{events}

TOTAL EMAILS PROVIDED: {email_count}
TOTAL CALENDAR EVENTS PROVIDED: {event_count}

CRITICAL RULE:
Every email provided in GMAIL DATA must be represented somewhere in the briefing.
Do not skip any emails.
Important emails should be shown individually.
Low-value emails should be grouped by category.
Trash must be reviewed separately.
Promotional emails must be grouped.
Newsletters must be grouped.
The Email Accounting table must add up to {email_count}.

OUTPUT FORMAT:
Return complete HTML only.
Do not return markdown.
Do not return explanations.
Do not return code fences.
Do not return the prompt.

STYLE:
Use a polished executive briefing design.
Use color-coded blocks:
- Red = security, urgent, risk
- Yellow = follow-up, RSVP, billing, deadline
- Blue = calendar, schedule, prep
- Green = job search, interviews, opportunities
- Purple = professional development, newsletters, events
- Gray = promotional, low priority, delete/ignore
Use clear cards, tables, section headers, and short summaries.

Some emails were already auto-trashed as high-confidence phishing before you received this \
data (flagged "auto_trashed": true, with "auto_trash_reason"). List these under Security / Risk \
and in Trash Review as "Auto-Trashed — Phishing" with the reason. Do not recommend further \
action on them beyond noting they were removed.

Some emails were rescued from Trash back to the inbox before you received this data \
(flagged "rescued_from_trash": true, with "rescue_reason"). List these under their \
appropriate category and note they were rescued from Trash with the reason.

REQUIRED SECTIONS:

1. Header
Include:
- Good morning, Melissa
- Date
- Total emails reviewed
- Total calendar events reviewed

2. Executive Summary
Include exactly 3 bullets:
- Biggest risk or urgent item
- Biggest job search / opportunity item
- Biggest calendar / deadline item

3. Action Required
Include only items Melissa must act on.
Each card must include:
- Label
- Title
- Source
- Why it matters
- Recommended next step
- Due date if known

4. Full 7-Day Calendar
Include every calendar event from CALENDAR DATA.
Group by day.
For each event include:
- Time
- Event
- RSVP/status
- Location/link
- Prep needed
- Conflict warning if applicable
Do not only show today or tomorrow.

5. Job Search & Interview Pipeline
Include:
- Job alerts
- Recruiter messages
- Networking meetings
- Interviews
- Applications
- Follow-ups
Rank each opportunity High / Medium / Low fit when possible.

6. Full Email Review by Category
Every email must be accounted for in exactly one category.
Categories:
- Security / Risk
- Job Search
- Recruiters / Networking
- Calendar / Events
- Medical / Health
- Financial / Billing
- Professional Development
- Personal
- Newsletters / Subscriptions
- Promotional / Retail
- Trash Review
- Safe to Delete / Ignore

For each category include:
- Count
- Summary
- Important senders
- Recommended action

7. Trash Review
Review emails marked as Trash.
Create three groups:
- Restore
- Review
- Safe to Delete
For each group, summarize senders and why.

8. Promotional / Retail Summary
Do not skip promotional emails.
Group them by sender or theme.
For each group include:
- Sender or brand
- Count
- Subject/theme
- Recommendation: Keep, Review, Delete, Ignore

9. Newsletters & Subscriptions
Group newsletters by topic.
Include:
- Sender
- Topic
- Recommendation: Keep, Review, Unsubscribe, Delete

10. Email Accounting
This section is mandatory.
Create a table:
Category | Count | Summary | Recommendation
The counts must add up to {email_count}.
Show:
Total Emails Reviewed: {email_count}

11. Dashboard
Include:
- Important unread emails
- Security alerts
- Action items
- Upcoming meetings
- Open job leads
- Interviews scheduled
- Bills/deadlines this week
- Trash items requiring review

12. Action Items
Create a table:
Priority | Action | Source | Due
Use HIGH / MEDIUM / LOW.

13. Top 3 Priorities Today
End with exactly 3 numbered priorities.

FINAL CHECK BEFORE OUTPUT:
Before returning the HTML, verify that the output includes these exact section names:
- Full 7-Day Calendar
- Job Search & Interview Pipeline
- Full Email Review by Category
- Trash Review
- Promotional / Retail Summary
- Email Accounting
- Dashboard

MANDATORY END SECTIONS:
You must include Trash Review, Promotional / Retail Summary, and Email Accounting near the end of the briefing.
Do not skip these sections.
If space is limited, summarize them briefly, but still include the section headings and counts.

Email Accounting must include:
- Total Emails Reviewed
- Category counts
- Trash count
- Promotional / Retail count
- Safe to Delete / Ignore count
- A short note confirming that every fetched email was reviewed or categorized

Trash Review must include:
- Restore Immediately
- Review Before Deleting
- Safe To Delete
Include sender, subject, and reason when available.

If any required section is missing, revise the output before returning it.
Return only the final complete HTML.
"""


def generate_briefing(client: "anthropic.Anthropic", emails: list, events: list) -> str:
    today_str = datetime.date.today().strftime("%A, %B %-d, %Y")
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=16000,
        messages=[{
            "role": "user",
            "content": PROMPT.format(
                today=today_str,
                email_count=len(emails),
                event_count=len(events),
                emails=json.dumps(emails,  indent=2, default=str),
                events=json.dumps(events,  indent=2, default=str),
            ),
        }],
    )
    text = message.content[0].text.strip()
    text = re.sub(r"^```(?:markdown)?\n?", "", text)
    text = re.sub(r"\n?```$", "", text.rstrip())
    return text


# ── Main ────────────────────────────────────────────────────────────────────────

def main() -> None:
    print("Building Google credentials…")
    creds    = _retry(build_google_credentials)
    gmail    = build("gmail",    "v1", credentials=creds)
    calendar = build("calendar", "v3", credentials=creds)

    print("Fetching Gmail messages…")
    emails = fetch_emails(gmail, days=7)
    print(f"  {len(emails)} messages fetched")

    print("Fetching Calendar events…")
    events = fetch_events(calendar, days=7)
    print(f"  {len(events)} events fetched")

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"], timeout=300.0)

    print("Checking for phishing…")
    try:
        phishing = _retry(lambda: classify_phishing(client, emails), attempts=2, delay=5)
    except Exception as exc:
        print(f"  Phishing check failed, skipping ({exc})")
        phishing = {}
    if phishing:
        print(f"  {len(phishing)} phishing email(s) flagged, trashing…")
        trash_phishing_emails(gmail, phishing)
    for e in emails:
        if e["id"] in phishing:
            e["auto_trashed"] = True
            e["auto_trash_reason"] = phishing[e["id"]]

    print("Checking trash for legitimate emails to rescue…")
    try:
        to_rescue = _retry(lambda: classify_legitimate_trash(client, emails), attempts=2, delay=5)
    except Exception as exc:
        print(f"  Rescue check failed, skipping ({exc})")
        to_rescue = {}
    if to_rescue:
        print(f"  {len(to_rescue)} email(s) being rescued from trash to inbox…")
        rescue_emails(gmail, to_rescue)
    for e in emails:
        if e["id"] in to_rescue:
            e["rescued_from_trash"] = True
            e["rescue_reason"] = to_rescue[e["id"]]

    print("Generating individual email triage summary…")
    try:
        summary_text = _retry(lambda: generate_email_summary(client, emails), attempts=2, delay=5)
        send_triage_summary(summary_text, phishing, to_rescue)
    except Exception as exc:
        print(f"  Triage summary failed, skipping ({exc})")

    print("Generating full briefing with Claude…")
    briefing = _retry(lambda: generate_briefing(client, emails, events), attempts=2, delay=5)

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for filename in ("BRIEFING.md", "README.md"):
        path = os.path.join(root, filename)
        with open(path, "w") as f:
            f.write(briefing + "\n")

    print(f"Saved BRIEFING.md + README.md ({len(briefing):,} chars)")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"\nERROR: {exc}", file=sys.stderr)
        sys.exit(1)
