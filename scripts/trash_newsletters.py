#!/usr/bin/env python3
"""
Hourly companion to generate_briefing.py: runs only the deterministic
newsletter-trash step (no Claude call) so matching senders don't sit in the
inbox for up to 24h waiting on the daily briefing run. Uses the same
NEWSLETTER_TRASH_PATTERNS / PROTECTED_SENDER_PATTERNS defined in
generate_briefing.py — no separate list to keep in sync.
Called by .github/workflows/trash-newsletters.yml.
"""

from __future__ import annotations

import socket
import sys

from googleapiclient.discovery import build

from generate_briefing import build_google_credentials, fetch_emails, trash_newsletter_emails, _retry

socket.setdefaulttimeout(60)


def main() -> None:
    print("Building Google credentials…")
    creds = _retry(build_google_credentials)
    gmail = build("gmail", "v1", credentials=creds)

    print("Fetching recent Gmail messages…")
    emails = fetch_emails(gmail, days=2)
    print(f"  {len(emails)} messages fetched")

    print("Auto-trashing newsletters…")
    trashed_ids = trash_newsletter_emails(gmail, emails)
    print(f"Done. {len(trashed_ids)} email(s) trashed.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"\nERROR: {exc}", file=sys.stderr)
        sys.exit(1)
