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
import time
import datetime
import zoneinfo

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import anthropic


SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
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

    # Collect message IDs (capped at 50 to keep the Claude prompt reasonable).
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
            "from":     _header(hdrs, "From"),
            "subject":  _header(hdrs, "Subject"),
            "date":     _header(hdrs, "Date"),
            "snippet":  msg.get("snippet", "")[:150],
            "unread":   "UNREAD"  in labels,
            "in_inbox": "INBOX"   in labels,
            "in_trash": "TRASH"   in labels,
        })
    return emails


# ── Google Calendar ─────────────────────────────────────────────────────────────

def fetch_events(service, days: int = 7) -> list[dict]:
    # Use start of the ET calendar day so events from earlier this morning
    # are included regardless of what time the briefing actually runs.
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


# ── Claude prompt ───────────────────────────────────────────────────────────────

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

def generate_briefing(emails: list, events: list) -> str:
    today_str = datetime.date.today().strftime("%A, %B %-d, %Y")

    # 5-minute timeout: long enough for a 16k-token response, short enough to
    # fail cleanly rather than block the 6-hour GitHub Actions job limit.
    client  = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"], timeout=300.0)
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
    # Strip code fences if Claude wraps the output anyway.
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

    print("Generating briefing with Claude…")
    briefing = _retry(lambda: generate_briefing(emails, events), attempts=2, delay=5)

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
