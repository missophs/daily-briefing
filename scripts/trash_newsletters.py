#!/usr/bin/env python3
"""
5-min companion to generate_briefing.py: runs the newsletter-trash step so
matching senders don't sit in the inbox waiting on the daily briefing run.
Two passes: (1) deterministic NEWSLETTER_TRASH_PATTERNS / PROTECTED_SENDER_PATTERNS
match, same lists generate_briefing.py uses, no separate list to keep in sync;
(2) a Claude classification pass over whatever the fixed list didn't catch, so
new senders (not yet added to the pattern list) still get trashed. Both passes
skip anything mentioning Claude/Anthropic (CLAUDE_MENTION_PATTERNS).
Called by .github/workflows/trash-newsletters.yml.
"""

from __future__ import annotations

import os
import socket
import sys

import anthropic
from googleapiclient.discovery import build

from generate_briefing import (
    build_google_credentials,
    classify_newsletters,
    fetch_emails,
    trash_ai_newsletters,
    trash_newsletter_emails,
    _retry,
)

socket.setdefaulttimeout(60)


def main() -> None:
    print("Building Google credentials…")
    creds = _retry(build_google_credentials)
    gmail = build("gmail", "v1", credentials=creds)

    print("Fetching recent Gmail messages…")
    emails = fetch_emails(gmail, days=2, max_results=200, inbox_only=True)
    print(f"  {len(emails)} messages fetched")

    print("Auto-trashing newsletters (pattern match)…")
    trashed_ids = trash_newsletter_emails(gmail, emails)
    print(f"  {len(trashed_ids)} email(s) trashed by pattern match")

    print("Classifying remaining inbox mail for newsletters (Claude)…")
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    remaining = [e for e in emails if e["id"] not in trashed_ids]
    classified = _retry(lambda: classify_newsletters(client, remaining))
    ai_trashed_ids = trash_ai_newsletters(gmail, classified)
    trashed_ids |= ai_trashed_ids

    print(f"Done. {len(trashed_ids)} email(s) trashed total.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"\nERROR: {exc}", file=sys.stderr)
        sys.exit(1)
