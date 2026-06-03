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
- Full Email Review by Category
- Trash Review
- Promotional / Retail Summary
- Email Accounting
- Dashboard

If any are missing, revise the output before returning it.
Return only the final complete HTML.
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

    import html as _html
    from collections import Counter

    def _val(email, *keys):
        for key in keys:
            value = email.get(key)
            if value:
                return str(value)
        return ""

    def _labels(email):
        labels = email.get("labels") or email.get("labelIds") or []
        if isinstance(labels, list):
            return " ".join(str(x) for x in labels)
        return str(labels)

    def _category(email):
        blob = " ".join([
            _val(email, "from", "sender"),
            _val(email, "subject"),
            _val(email, "snippet", "body"),
            _labels(email),
        ]).lower()

        if "trash" in blob:
            return "Trash Review"
        if any(x in blob for x in ["password", "security", "locked", "pin", "phish", "scam", "casino", "account access"]):
            return "Security / Risk"
        if any(x in blob for x in ["linkedin", "job", "recruiter", "interview", "application", "people business partner", "chief people", "hr business"]):
            return "Job Search / Recruiters"
        if any(x in blob for x in ["doctor", "dr.", "medical", "appointment", "lens", "health", "skin"]):
            return "Medical / Health"
        if any(x in blob for x in ["bill", "payment", "invoice", "state farm", "netlify", "credits", "billing"]):
            return "Financial / Billing"
        if any(x in blob for x in ["webinar", "event", "training", "newsletter", "research", "hr.com", "substack"]):
            return "Professional Development / Newsletters"
        if any(x in blob for x in ["sale", "% off", "promo", "deal", "discount", "cart", "shop", "offer"]):
            return "Promotional / Retail"
        return "Other / Review"

    rows = []
    counts = Counter()

    for i, email in enumerate(emails, start=1):
        category = _category(email)
        counts[category] += 1

        sender = _html.escape(_val(email, "from", "sender") or "Unknown sender")
        subject = _html.escape(_val(email, "subject") or "(No subject)")
        date = _html.escape(_val(email, "date", "internalDate") or "")
        labels = _html.escape(_labels(email))
        snippet = _html.escape((_val(email, "snippet", "body") or "")[:180])

        recommendation = "Review"
        if category in ["Security / Risk"]:
            recommendation = "Act / Delete if scam"
        elif category in ["Promotional / Retail", "Other / Review"]:
            recommendation = "Delete or ignore unless useful"
        elif category == "Trash Review":
            recommendation = "Review before permanent delete"
        elif category == "Job Search / Recruiters":
            recommendation = "Review for opportunity or follow-up"

        rows.append(f"""
<tr>
  <td>{i}</td>
  <td>{category}</td>
  <td>{sender}</td>
  <td>{subject}</td>
  <td>{date}</td>
  <td>{labels}</td>
  <td>{snippet}</td>
  <td>{recommendation}</td>
</tr>""")

    accounting_rows = "\n".join(
        f"<tr><td>{_html.escape(cat)}</td><td>{count}</td></tr>"
        for cat, count in sorted(counts.items())
    )

    email_rows = "\n".join(rows)

    forced_sections = f"""
<hr>
<h2>Trash Review</h2>
<p><strong>Purpose:</strong> Review deleted emails for anything important before permanent deletion. Anything from job search, billing, medical, calendar, security, legal, GitHub, Netlify, LinkedIn, recruiters, or professional contacts should be reviewed before deleting.</p>

<h2>Promotional / Retail Summary</h2>
<p><strong>Purpose:</strong> Promotional emails are included in the full email inventory below. Delete or ignore retail/promotional items unless there is a deal you actually plan to use or a sender looks suspicious.</p>

<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> {len(emails)}</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
{accounting_rows}
</table>

<h2>Full Email Inventory</h2>
<p><strong>Every fetched email is listed below.</strong> Use this section to see what to act on, review, delete, or ignore.</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr>
  <th>#</th>
  <th>Category</th>
  <th>From</th>
  <th>Subject</th>
  <th>Date</th>
  <th>Labels</th>
  <th>Snippet</th>
  <th>Recommendation</th>
</tr>
{email_rows}
</table>
"""

    if "</body>" in text:
        text = text.replace("</body>", forced_sections + "\n</body>")
    else:
        text += forced_sections

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
