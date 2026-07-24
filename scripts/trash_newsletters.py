#!/usr/bin/env python3
"""
Move newsletter/promo emails matching NEWSLETTER_TRASH_PATTERNS to Gmail Trash.
Skips anything matching PROTECTED_SENDER_PATTERNS. Deterministic substring match
on the From header — no Claude API call. Runs hourly via
.github/workflows/trash-newsletters.yml.
"""

from __future__ import annotations

import socket
import sys

from googleapiclient.discovery import build

from generate_briefing import build_google_credentials, _header, _retry

socket.setdefaulttimeout(60)

NEWSLETTER_TRASH_PATTERNS = [
    "cooldeep", "medium daily digest", "@medium.com",
    "the average joe", "averagejoecrypto",
    "1% better", "1percentbetter", "the ai report", "theaireport",
    "optery", "christopher rainey", "giulia guerrieri", "tradealgo",
    "j.t. o'donnell", "jt o'donnell", "jtodonnell", "sophia davis",
    "fred from fireflies", "fireflies.ai",
    "experteer", "eharmony", "pranit naik", "quillbot", "phil strazzulla",
    "limitless creator", "16handles", "techspresso", "stephanie adams",
    "ifttt", "tldr newsletter", "tldrnewsletter",
    "yesstyle", "kohls", "kohl's", "melissa westgate", "gap factory", "gapfactory",
    "gemma bonham",
    "info@skincareessentials.com",
    "hello@digistore24newsletter.com",
    "community@transform.us",
]

PROTECTED_SENDER_PATTERNS = [
    "match.com",
    "linkedin",
    "chatgpt", "openai.com", "claude", "anthropic.com",
    "delta.com", "united.com", "aa.com", "southwest.com", "jetblue.com", "alaskaair.com",
    "merrilllynch", "merrill lynch", "ml.com", "merrilledge",
    "chase", "bankofamerica", "wellsfargo", "citibank", "usbank", "tdbank", "pnc",
    "capitalone", "schwab", "fidelity", "vanguard", "synchrony", "ally", "discover",
    "barclays", "regions", "suntrust", "truist", "navyfederal", "usaa",
]


def is_protected(sender: str) -> bool:
    s = sender.lower()
    return any(p in s for p in PROTECTED_SENDER_PATTERNS)


def matches_trash(sender: str) -> str | None:
    s = sender.lower()
    for pattern in NEWSLETTER_TRASH_PATTERNS:
        if pattern.lower() in s:
            return pattern
    return None


def fetch_inbox_senders(service) -> list[dict]:
    ids, page_token = [], None
    while True:
        resp = _retry(lambda pt=page_token: service.users().messages().list(
            userId="me",
            q="in:inbox",
            maxResults=100,
            pageToken=pt,
        ).execute())
        ids.extend(resp.get("messages", []))
        page_token = resp.get("nextPageToken")
        if not page_token or len(ids) >= 300:
            break

    emails = []
    for ref in ids:
        msg = _retry(lambda r=ref: service.users().messages().get(
            userId="me",
            id=r["id"],
            format="metadata",
            metadataHeaders=["From"],
        ).execute())
        hdrs = msg.get("payload", {}).get("headers", [])
        emails.append({"id": ref["id"], "from": _header(hdrs, "From")})
    return emails


def main() -> None:
    print("Building Google credentials…")
    creds = _retry(build_google_credentials)
    gmail = build("gmail", "v1", credentials=creds)

    print("Fetching inbox senders…")
    emails = fetch_inbox_senders(gmail)
    print(f"  {len(emails)} inbox messages fetched")

    trashed = 0
    for e in emails:
        sender = e["from"]
        if is_protected(sender):
            continue
        matched = matches_trash(sender)
        if not matched:
            continue
        try:
            _retry(lambda m=e["id"]: gmail.users().messages().trash(userId="me", id=m).execute())
            print(f"  Trashed {e['id']} ({sender}) — matched '{matched}'")
            trashed += 1
        except Exception as exc:
            print(f"  Failed to trash {e['id']} ({sender}): {exc}")

    print(f"Done. {trashed} email(s) trashed.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"\nERROR: {exc}", file=sys.stderr)
        sys.exit(1)
