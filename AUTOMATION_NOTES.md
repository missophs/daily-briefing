# Daily Briefing Automation Notes

## Current setup

Daily Briefing now runs as one GitHub Actions workflow.

It does all of this in one run:

1. Reads Gmail and Calendar
2. Generates BRIEFING.md and README.md
3. Emails the completed briefing using Python SMTP
4. Commits the updated files back to GitHub

## Schedule

Runs once daily at about 6:50 AM Eastern.

Cron:

50 10 * * *

GitHub Actions may run a few minutes late.

## Important fixes

The old setup used two workflows:

- Daily Briefing
- Email Daily Briefing

That was fragile because email could run before the briefing was generated.

The separate Email Daily Briefing workflow is now manual only.

## Google OAuth fix

The old Google OAuth client stopped working.

Final fix:

- Created a new Google OAuth Desktop App client
- Updated GOOGLE_CLIENT_ID
- Updated GOOGLE_CLIENT_SECRET
- Generated and updated GMAIL_REFRESH_TOKEN

These three must always match:

GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET
GMAIL_REFRESH_TOKEN

## Email fix

Email is now sent inside Daily Briefing using Python SMTP.

The workflow supports:

- SMTP_SSL for port 465
- STARTTLS for port 587

Successful logs should include:

SMTP sendmail returned successfully
Email sent →

## Do not repeat

Do not split generation and email into two scheduled workflows.
Do not rerun Daily Briefing repeatedly without checking the exact error first.
Do not update only one Google OAuth secret.
