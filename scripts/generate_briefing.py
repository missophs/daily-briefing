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
import datetime

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import anthropic


SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/calendar.readonly",
]


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

    # Collect message IDs (capped at 50 to keep the Claude prompt reasonable)
    ids, page_token = [], None
    while len(ids) < 50:
        resp = service.users().messages().list(
            userId="me",
            q=f"after:{after}",
            maxResults=50,
            pageToken=page_token,
            includeSpamTrash=True,
        ).execute()
        ids.extend(resp.get("messages", []))
        page_token = resp.get("nextPageToken")
        if not page_token:
            break

    emails = []
    for ref in ids[:50]:
        msg = service.users().messages().get(
            userId="me",
            id=ref["id"],
            format="metadata",
            metadataHeaders=["From", "Subject", "Date"],
        ).execute()
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
    now = datetime.datetime.utcnow().isoformat() + "Z"
    end = (datetime.datetime.utcnow() + datetime.timedelta(days=days)).isoformat() + "Z"

    result = service.events().list(
        calendarId="primary",
        timeMin=now,
        timeMax=end,
        singleEvents=True,
        orderBy="startTime",
        maxResults=30,
    ).execute()

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
You are Melissa's personal executive assistant. Generate her daily briefing.

Today: {today}

--- GMAIL ({email_count} messages, last 7 days) ---
{emails}

--- CALENDAR ({event_count} events, next 7 days) ---
{events}

Output ONLY the Markdown document below. No explanation, no code fences.

# MELISSA'S WEEKLY BRIEFING
**Generated:** {today}

---

## 🔴 SECTION 1 — ACTION REQUIRED

Surface only items needing action: security alerts, unread billing, time-sensitive \
job search items (canceled interviews, stale applications), anything happening TODAY. \
Use ### subheadings — SECURITY, BILLING, JOB SEARCH — FOLLOW UP, TODAY — HAPPENING NOW — \
only for subheadings that have content.

---

## 🟡 SECTION 2 — THIS WEEK'S CALENDAR

One ### heading per day (e.g. ### WEDNESDAY, JUNE 4 — TODAY). \
Table per day: | Time | Event | Status |
Include Zoom links verbatim from event descriptions. \
Status values: Confirmed / Declined / No RSVP / Accepted.

---

## 🟢 SECTION 3 — EMAILS BY CATEGORY

Tables with | Date | From | Subject | Status | columns. \
Use only categories that have content:
- ### MEDICAL / HEALTH
- ### JOB SEARCH — ACTIVE LEADS  (batch-summarize job alert digests — e.g. "6 new LinkedIn alerts — CHRO, VP HR, Head of People roles")
- ### PROFESSIONAL DEVELOPMENT
- ### FINANCIAL / BILLING
- ### NOISE / PROMOTIONAL (TRASH — nothing to action)  (bulleted list only, no table)

---

## 🔵 SECTION 4 — ACTION ITEMS

| Priority | Item | Source |
Priorities: HIGH / MEDIUM / LOW only. HIGH items first. Be specific and actionable.

---

*Briefing pulls live data from Gmail inbox and Trash (last 7 days) and \
Google Calendar ({date_range}).*
"""


def generate_briefing(emails: list, events: list) -> str:
    today      = datetime.date.today()
    today_str  = today.strftime("%A, %B %-d, %Y")
    end_str    = (today + datetime.timedelta(days=7)).strftime("%b %-d, %Y")
    date_range = f"{today.strftime('%b %-d')}–{end_str}"

    client  = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        messages=[{
            "role": "user",
            "content": PROMPT.format(
                today=today_str,
                date_range=date_range,
                email_count=len(emails),
                event_count=len(events),
                emails=json.dumps(emails,  indent=2, default=str),
                events=json.dumps(events,  indent=2, default=str),
            ),
        }],
    )

    text = message.content[0].text.strip()
    # Strip code fences if Claude wraps the output anyway
    text = re.sub(r"^```(?:markdown)?\n?", "", text)
    text = re.sub(r"\n?```$", "", text.rstrip())
    return text


# ── Main ────────────────────────────────────────────────────────────────────────

def main() -> None:
    print("Building Google credentials…")
    creds    = build_google_credentials()
    gmail    = build("gmail",    "v1", credentials=creds)
    calendar = build("calendar", "v3", credentials=creds)

    print("Fetching Gmail messages…")
    emails = fetch_emails(gmail, days=7)
    print(f"  {len(emails)} messages fetched")

    print("Fetching Calendar events…")
    events = fetch_events(calendar, days=7)
    print(f"  {len(events)} events fetched")

    print("Generating briefing with Claude…")
    briefing = generate_briefing(emails, events)

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
