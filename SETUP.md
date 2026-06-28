# Daily Briefing — Setup & Maintenance

## Changing the delivery time

1. Edit the `cron:` line in `.github/workflows/daily-briefing.yml`
2. Convert Eastern time to UTC: add 4h (EDT, summer) or 5h (EST, winter)
   - 7:15 AM ET (summer) = `15 11 * * *`
   - 7:15 AM ET (winter) = `15 12 * * *`
3. Commit and push to the `webhooks` branch
4. Do not touch any secrets — the cron line is the only change needed

## Fixing auth errors (invalid_grant / unauthorized_client)

These errors mean the Gmail refresh token expired or was revoked. Fix:

1. On your Mac, run:

       cd /Users/Owner/Documents/Claude/05_RESOURCES/Scheduled/morning-email-digest
       python get_new_token.py

2. Open the printed URL in your browser, sign in, click Allow
3. Your browser shows an error page — that is expected
4. Copy the full URL from the address bar and paste it into the terminal
5. Terminal prints your new refresh token — copy it
6. In Terminal, run:

       gh secret set GMAIL_REFRESH_TOKEN --repo missophs/daily-briefing

   Paste the token when prompted, press Enter, then Ctrl+D

Important: GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET must match the gmail_credentials.json file used to generate the token.
- Client ID: 522559244108-qq2gh2o0t58oe2jhvej0lad75740rh81.apps.googleusercontent.com
- Credentials file: /Users/Owner/Documents/Claude/05_RESOURCES/Scheduled/morning-email-digest/gmail_credentials.json

Note on token expiry: As of 2026-06-28, the Google Cloud project (tough-talent-493313-u9) is set to In production. Refresh tokens no longer expire every 7 days. The only reasons a token would become invalid now are: manually revoking access in your Google account, or changing your Google account password.

## GitHub Secrets required

| Secret | Purpose |
|--------|---------|
| GMAIL_REFRESH_TOKEN | Gmail/Calendar API access |
| GOOGLE_CLIENT_ID | OAuth client identity |
| GOOGLE_CLIENT_SECRET | OAuth client secret |
| ANTHROPIC_API_KEY | Claude AI for briefing generation |
| SMTP_SERVER | Email sending server |
| SMTP_PORT | Email port (465 or 587) |
| MAIL_USERNAME | Sender email address |
| MAIL_PASSWORD | Sender email password |
| MAIL_TO | Recipient (melissaw212@gmail.com) |

## Manually triggering a run

Go to: https://github.com/missophs/daily-briefing/actions/workflows/daily-briefing.yml
Click Run workflow, select branch webhooks, click the green Run workflow button.
