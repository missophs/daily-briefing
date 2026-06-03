#!/usr/bin/env python3
"""
Run this script ONCE on your local machine to get your GMAIL_REFRESH_TOKEN.
It opens a browser window for you to log in, then prints the token to paste
into GitHub Secrets.

Prerequisites (run in your terminal first):
  pip install google-auth-oauthlib

Usage:
  python scripts/get_google_token.py
"""

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/calendar.readonly",
]

print()
print("=" * 60)
print("  Google OAuth Token Helper")
print("=" * 60)
print()
print("Find these values in Google Cloud Console:")
print("  APIs & Services → Credentials → your OAuth 2.0 Client ID")
print()

client_id     = input("Paste GOOGLE_CLIENT_ID:     ").strip()
client_secret = input("Paste GOOGLE_CLIENT_SECRET: ").strip()
print()

client_config = {
    "installed": {
        "client_id":     client_id,
        "client_secret": client_secret,
        "auth_uri":      "https://accounts.google.com/o/oauth2/auth",
        "token_uri":     "https://oauth2.googleapis.com/token",
        "redirect_uris": ["http://localhost"],
    }
}

flow  = InstalledAppFlow.from_client_config(client_config, SCOPES)
creds = flow.run_local_server(port=0, prompt="consent", access_type="offline")

print()
print("=" * 60)
print("  SUCCESS")
print("=" * 60)
print()
print("Add this as the GMAIL_REFRESH_TOKEN secret in GitHub:")
print()
print(creds.refresh_token)
print()
