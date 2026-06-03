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
You are Melissa's executive chief of staff. Create a polished, easy-to-read HTML daily briefing from the Gmail and Calendar data below.

Today: {today}

GMAIL DATA:
{emails}

CALENDAR DATA:
{events}

Write the briefing as clean HTML only. No markdown. No code fences.

Style rules:
- Use a dark navy header with "Good morning, Melissa" and today's date.
- Use color-coded cards:
  - Red cards for urgent/action required/security/risk
  - Yellow cards for follow-up items
  - Blue cards for calendar/prep
  - Green cards for job leads/opportunities
  - Purple cards for professional development
  - Gray cards for low-priority/noise
- Use big bold section headers.
- Use short summaries, not long raw email dumps.
- Each important item should include: label, title, source/sender, why it matters, and recommended next step.
- Prioritize interviews, job search, recruiter follow-ups, billing, medical, security, deadlines, and calendar conflicts.
- Do not skip any emails from the Gmail data. Every email should be accounted for.
- Group emails into clear categories: Action Required, Security/Risk, Job Search, Interviews/Recruiters, Calendar/Events, Medical/Health, Financial/Billing, Professional Development, Personal, Promotional/Retail, Newsletters/Subscriptions, Trash Review, and Delete/Ignore.
- Include Gmail Trash. Trash must have its own section called Trash Review.
- For Trash Review, summarize what is in trash and clearly label: Restore / Review / Safe to Delete.
- Promotional emails should be grouped together with sender, subject, and whether anything is useful, expiring, suspicious, or safe to delete.
- Newsletters and subscriptions should be grouped together with a short summary and delete/keep recommendation.
- Do not let promotional emails crowd out urgent items, but do not omit them.
- Include the full week’s calendar, not just today.
- For the calendar, show each day for the next 7 days with time, event, status, location/link, conflicts, and prep needed.
- End every section with a short summary of what Melissa should do: Act / Review / Delete / Ignore.
- Include an Executive Summary at the top with 3 bullets.
- Include all important information from Gmail inbox, Gmail Trash, and Google Calendar.
- End with Top 3 Priorities Today.
- Skip empty sections.

Important email coverage rules:
- Every email fetched from Gmail must be represented somewhere in the briefing.
- Do not skip emails.
- Group emails into categories instead of dumping them one by one.
- Include these categories when present: Action Required, Security/Risk, Job Search, Interviews/Recruiters, Calendar/Events, Medical/Health, Financial/Billing, Professional Development, Personal, Promotional/Retail, Newsletters/Subscriptions, Trash Review, Delete/Ignore.
- Promotional emails must be grouped together with sender/brand, subject/theme, and recommendation: Keep, Review, Delete, or Ignore.
- Trash must be included in a Trash Review section with Restore / Review / Safe to Delete recommendations.
- Include a full 7-day calendar section with each day, time, event, RSVP/status, location/link, conflicts, and prep needed.
- Add an Email Accounting section at the end showing total emails reviewed and category counts. The counts should add up to the total emails fetched.

Use this structure:
1. Header
2. Executive Summary
3. Action Required
4. Today's Schedule + Prep
5. Job Search + Interview Pipeline
6. Important Emails
7. Calendar Risks This Week
8. Full Email Review by Category
9. Trash Review
10. Promotional / Retail Summary
11. Email Accounting
12. Action Items Table
13. Top 3 Priorities Today


Required completeness rules:
- You received {email_count} Gmail messages. The final briefing must account for all {email_count}.
- Add a section called "Email Accounting" near the end.
- In Email Accounting, show a table with category, count, summary, and recommendation.
- Categories must include: Action Required, Security/Risk, Job Search, Interviews/Recruiters, Calendar/Events, Medical/Health, Financial/Billing, Professional Development, Personal, Promotional/Retail, Newsletters/Subscriptions, Trash Review, Delete/Ignore.
- The category counts must add up to {email_count}.
- If an email is not important, still count it and summarize it inside Promotional/Retail, Newsletters/Subscriptions, Trash Review, or Delete/Ignore.
- Do not say there were no emails if {email_count} is greater than 0.

Return only complete HTML that can be sent as an email body.
"""

def generate_briefing(emails: list, events: list) -> str:
    today      = datetime.date.today()
    today_str  = today.strftime("%A, %B %-d, %Y")
    end_str    = (today + datetime.timedelta(days=7)).strftime("%b %-d, %Y")
    date_range = f"{today.strftime('%b %-d')}–{end_str}"

    client  = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8192,
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

Transcription by CastingWords
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
