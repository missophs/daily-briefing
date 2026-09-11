<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa Weiss — Friday, September 11, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrapper { max-width: 1200px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: white; border-radius: 16px; padding: 36px 40px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; }
  .header-left h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header-left .subtitle { font-size: 15px; opacity: 0.8; margin-top: 4px; }
  .header-right { text-align: right; }
  .header-right .stat { font-size: 13px; opacity: 0.75; margin-bottom: 4px; }
  .header-right .stat span { font-weight: 700; color: #e2b96f; font-size: 15px; }
  .header-badge { background: rgba(255,255,255,0.12); border-radius: 8px; padding: 8px 16px; margin-top: 8px; font-size: 12px; letter-spacing: 1px; text-transform: uppercase; opacity: 0.9; }

  /* SECTION HEADERS */
  .section-title { font-size: 17px; font-weight: 700; letter-spacing: 0.3px; margin-bottom: 14px; padding-bottom: 8px; border-bottom: 2px solid; display: flex; align-items: center; gap: 8px; }
  .section { margin-bottom: 28px; background: white; border-radius: 12px; padding: 22px 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }

  /* COLOR THEMES */
  .red { border-left: 5px solid #dc2626; }
  .red .section-title { color: #dc2626; border-color: #fca5a5; }
  .yellow { border-left: 5px solid #d97706; }
  .yellow .section-title { color: #b45309; border-color: #fcd34d; }
  .blue { border-left: 5px solid #2563eb; }
  .blue .section-title { color: #1d4ed8; border-color: #93c5fd; }
  .green { border-left: 5px solid #16a34a; }
  .green .section-title { color: #15803d; border-color: #86efac; }
  .purple { border-left: 5px solid #7c3aed; }
  .purple .section-title { color: #6d28d9; border-color: #c4b5fd; }
  .gray { border-left: 5px solid #9ca3af; }
  .gray .section-title { color: #4b5563; border-color: #d1d5db; }
  .teal { border-left: 5px solid #0d9488; }
  .teal .section-title { color: #0f766e; border-color: #5eead4; }
  .pink { border-left: 5px solid #db2777; }
  .pink .section-title { color: #be185d; border-color: #f9a8d4; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 13px; }
  th { background: #f8fafc; color: #374151; font-weight: 700; padding: 10px 12px; text-align: left; border-bottom: 2px solid #e5e7eb; }
  td { padding: 9px 12px; border-bottom: 1px solid #f1f3f5; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #fafbfc; }

  /* STATUS BADGES */
  .badge { display: inline-block; padding: 2px 9px; border-radius: 20px; font-size: 11px; font-weight: 700; letter-spacing: 0.3px; white-space: nowrap; }
  .badge-red { background: #fee2e2; color: #b91c1c; }
  .badge-yellow { background: #fef3c7; color: #92400e; }
  .badge-green { background: #dcfce7; color: #166534; }
  .badge-blue { background: #dbeafe; color: #1e40af; }
  .badge-purple { background: #ede9fe; color: #5b21b6; }
  .badge-gray { background: #f3f4f6; color: #374151; }
  .badge-orange { background: #ffedd5; color: #9a3412; }
  .badge-teal { background: #ccfbf1; color: #0f766e; }
  .badge-pink { background: #fce7f3; color: #9d174d; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 18px; margin-bottom: 12px; border: 1px solid; }
  .card-red { background: #fff5f5; border-color: #fecaca; }
  .card-yellow { background: #fffbeb; border-color: #fde68a; }
  .card-green { background: #f0fdf4; border-color: #bbf7d0; }
  .card-blue { background: #eff6ff; border-color: #bfdbfe; }
  .card-purple { background: #faf5ff; border-color: #ddd6fe; }
  .card-gray { background: #f9fafb; border-color: #e5e7eb; }
  .card-teal { background: #f0fdfa; border-color: #99f6e4; }
  .card-pink { background: #fdf2f8; border-color: #f9a8d4; }
  .card-title { font-weight: 700; font-size: 14px; margin-bottom: 4px; }
  .card-meta { font-size: 12px; color: #6b7280; margin-bottom: 6px; }
  .card-body { font-size: 13px; margin-bottom: 6px; }
  .card-action { font-size: 12px; font-weight: 600; }
  .card-action.red { color: #b91c1c; }
  .card-action.green { color: #15803d; }
  .card-action.blue { color: #1d4ed8; }
  .card-action.yellow { color: #92400e; }

  /* EXECUTIVE SUMMARY BULLETS */
  .exec-bullet { display: flex; gap: 12px; align-items: flex-start; margin-bottom: 10px; padding: 12px 14px; border-radius: 8px; }
  .exec-bullet-icon { font-size: 20px; min-width: 28px; }
  .exec-bullet-text strong { display: block; font-size: 14px; margin-bottom: 2px; }
  .exec-bullet-text span { font-size: 13px; color: #4b5563; }
  .exec-bullet-red { background: #fff5f5; border: 1px solid #fecaca; }
  .exec-bullet-green { background: #f0fdf4; border: 1px solid #bbf7d0; }
  .exec-bullet-blue { background: #eff6ff; border: 1px solid #bfdbfe; }

  /* PRIORITY TABLE */
  .priority-high { color: #b91c1c; font-weight: 700; }
  .priority-medium { color: #b45309; font-weight: 600; }
  .priority-low { color: #374151; font-weight: 500; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { font-size: 14px; font-weight: 700; color: #1d4ed8; background: #eff6ff; border-radius: 6px; padding: 6px 12px; margin-bottom: 8px; display: inline-block; }
  .cal-day-header.today { background: #dbeafe; color: #1e40af; border: 1.5px solid #93c5fd; }
  .cal-event { background: #f8fafc; border-left: 4px solid #2563eb; border-radius: 6px; padding: 10px 14px; margin-bottom: 8px; }
  .cal-event.declined { border-left-color: #9ca3af; opacity: 0.7; }
  .cal-event.needs-action { border-left-color: #d97706; }
  .cal-event.confirmed { border-left-color: #16a34a; }
  .cal-event.accepted { border-left-color: #2563eb; }
  .cal-event-time { font-size: 12px; font-weight: 700; color: #2563eb; margin-bottom: 2px; }
  .cal-event-title { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
  .cal-event-detail { font-size: 12px; color: #4b5563; margin-bottom: 2px; }
  .cal-conflict { font-size: 11px; font-weight: 700; color: #b91c1c; background: #fee2e2; border-radius: 4px; padding: 2px 7px; display: inline-block; margin-top: 4px; }
  .cal-prep { font-size: 12px; color: #166534; background: #dcfce7; border-radius: 4px; padding: 2px 7px; margin-top: 4px; display: inline-block; }

  /* TRIAGE TABLE */
  .triage-table td { font-size: 12.5px; }
  .rescued-row td { background: #f0fdf4 !important; }
  .inbox-row td { background: #fafbff !important; }
  .summary-row td { background: #f9fafb !important; font-style: italic; }

  /* DASHBOARD */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin-top: 4px; }
  .dash-card { border-radius: 10px; padding: 14px 16px; border: 1px solid; }
  .dash-card-label { font-size: 11px; font-weight: 700; letter-spacing: 0.8px; text-transform: uppercase; margin-bottom: 6px; }
  .dash-card-value { font-size: 22px; font-weight: 800; margin-bottom: 4px; }
  .dash-card-note { font-size: 12px; color: #6b7280; }
  .dash-red { background: #fff5f5; border-color: #fecaca; }
  .dash-red .dash-card-label { color: #b91c1c; }
  .dash-red .dash-card-value { color: #dc2626; }
  .dash-green { background: #f0fdf4; border-color: #bbf7d0; }
  .dash-green .dash-card-label { color: #15803d; }
  .dash-green .dash-card-value { color: #16a34a; }
  .dash-blue { background: #eff6ff; border-color: #bfdbfe; }
  .dash-blue .dash-card-label { color: #1e40af; }
  .dash-blue .dash-card-value { color: #2563eb; }
  .dash-yellow { background: #fffbeb; border-color: #fde68a; }
  .dash-yellow .dash-card-label { color: #92400e; }
  .dash-yellow .dash-card-value { color: #d97706; }
  .dash-purple { background: #faf5ff; border-color: #ddd6fe; }
  .dash-purple .dash-card-label { color: #5b21b6; }
  .dash-purple .dash-card-value { color: #7c3aed; }
  .dash-gray { background: #f9fafb; border-color: #e5e7eb; }
  .dash-gray .dash-card-label { color: #4b5563; }
  .dash-gray .dash-card-value { color: #374151; }

  /* TOP 3 */
  .top3 { counter-reset: top3; }
  .top3-item { display: flex; gap: 14px; align-items: flex-start; padding: 14px 16px; border-radius: 10px; margin-bottom: 10px; border: 1px solid; }
  .top3-num { font-size: 28px; font-weight: 900; min-width: 36px; opacity: 0.25; }
  .top3-content strong { display: block; font-size: 15px; font-weight: 700; margin-bottom: 4px; }
  .top3-content p { font-size: 13px; color: #4b5563; }
  .top3-1 { background: #fff5f5; border-color: #fecaca; }
  .top3-1 .top3-num { color: #dc2626; }
  .top3-2 { background: #f0fdf4; border-color: #bbf7d0; }
  .top3-2 .top3-num { color: #16a34a; }
  .top3-3 { background: #eff6ff; border-color: #bfdbfe; }
  .top3-3 .top3-num { color: #2563eb; }

  /* NOTE BOX */
  .note-box { background: #fffbeb; border: 1px solid #fde68a; border-radius: 8px; padding: 10px 14px; font-size: 12.5px; color: #78350f; margin-bottom: 10px; }
  .rescued-note { background: #f0fdf4; border: 1px solid #86efac; border-radius: 8px; padding: 10px 14px; font-size: 12.5px; color: #14532d; margin-bottom: 10px; }
  .phishing-note { background: #fff5f5; border: 1px solid #fecaca; border-radius: 8px; padding: 10px 14px; font-size: 12.5px; color: #7f1d1d; margin-bottom: 10px; }

  /* UTILITY */
  .mt8 { margin-top: 8px; }
  .mt12 { margin-top: 12px; }
  .flex-row { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; }
  .divider { border: none; border-top: 1px solid #e5e7eb; margin: 14px 0; }
  .small-gray { font-size: 12px; color: #6b7280; }
  .tag { display: inline-block; background: #e0e7ff; color: #3730a3; font-size: 11px; font-weight: 600; border-radius: 4px; padding: 1px 6px; margin: 2px 2px 2px 0; }
  .tag-red { background: #fee2e2; color: #991b1b; }
  .tag-green { background: #dcfce7; color: #166534; }
  .tag-yellow { background: #fef3c7; color: #92400e; }
  .tag-gray { background: #f3f4f6; color: #4b5563; }
  .section-intro { font-size: 13px; color: #6b7280; margin-bottom: 14px; }

  @media (max-width: 700px) {
    .header { flex-direction: column; gap: 16px; }
    .header-right { text-align: left; }
    .dashboard-grid { grid-template-columns: 1fr 1fr; }
  }
</style>
</head>
<body>
<div class="page-wrapper">

<!-- ═══════════════════════════════════════════════════ -->
<!-- SECTION 0: EMAIL TRIAGE QUICK LIST -->
<!-- ═══════════════════════════════════════════════════ -->
<div class="section teal" style="margin-bottom: 24px;">
  <div class="section-title">⚡ Email Triage Quick List</div>
  <p class="section-intro">One row per email. Inbox and rescued emails shown individually. Trashed emails collapsed into summary rows at the bottom.</p>
  <table class="triage-table">
    <thead>
      <tr>
        <th style="width:120px;">Status</th>
        <th style="width:200px;">From</th>
        <th style="width:260px;">Subject</th>
        <th>Summary</th>
      </tr>
    </thead>
    <tbody>
      <!-- RESCUED ROWS -->
      <tr class="rescued-row">
        <td><span class="badge badge-green">✅ RESCUED</span></td>
        <td>My Best Buy® Visa® Card (Citi)</td>
        <td>Time's running out on 24 month financing</td>
        <td>Financing deadline reminder. Rescued from Trash — protected sender. Review before offer expires.</td>
      </tr>
      <tr class="rescued-row">
        <td><span class="badge badge-green">✅ RESCUED</span></td>
        <td>Claude's Notebook (Substack)</td>
        <td>Ipse</td>
        <td>Philosophical newsletter essay. Rescued from Trash — protected sender. Read when time permits.</td>
      </tr>

      <!-- INBOX ROWS -->
      <tr class="inbox-row">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>303 East 83rd (Equity Apartments)</td>
        <td>You have a delivery!</td>
        <td>Package arrived at Apt 03H — Amazon tracking #4471. Pick up from building.</td>
      </tr>
      <tr class="inbox-row">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Amazon.com</td>
        <td>Delivered: 1 Cosmetics item</td>
        <td>Cosmetics order delivered. Confirmed delivery.</td>
      </tr>
      <tr class="inbox-row">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Slack</td>
        <td>Your trial of Slack's Pro plan has ended</td>
        <td>Pro trial expired — premium features no longer accessible. Decide: upgrade or stay free.</td>
      </tr>
      <tr class="inbox-row">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>VP, People at Backblaze and 10 more</td>
        <td>10+ VP/People roles. Includes Backblaze VP People reporting to CHRO.</td>
      </tr>
      <tr class="inbox-row">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>LinkedIn</td>
        <td>Melissa A, add Sonya Tkacs</td>
        <td>Connection suggestion — Founder, Recruitlynk. Relevant recruiter for job search.</td>
      </tr>
      <tr class="inbox-row">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Match</td>
        <td>You've had a profile view from Michael</td>
        <td>Michael, 62, Holyoke MA viewed your profile. Personal / dating app notification.</td>
      </tr>
      <tr class="inbox-row">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Synchrony Bank</td>
        <td>Your CareCredit Rewards Mastercard Payment Has Posted</td>
        <td>$265.00 payment posted to account ending 5572. Confirmed — no action needed.</td>
      </tr>
      <tr class="inbox-row">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>Vice President – People & Culture at Greenbox Capital and 2 more</td>
        <td>VP People & Culture (US Remote) at Greenbox Capital. Strong match — review.</td>
      </tr>
      <tr class="inbox-row">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>Vice President Human Resources at PeopleOps Jobs and 39 more</td>
        <td>39+ VP HR roles. High volume — worth scanning for best matches.</td>
      </tr>
      <tr class="inbox-row">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>VP, People at Backblaze and 39 more</td>
        <td>Duplicate/updated alert for Backblaze VP role + 39 more. Cross-reference with earlier alert.</td>
      </tr>
      <tr class="inbox-row">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Zoom</td>
        <td>1 Hour to Go for Day -1 of the Claude 101 Workshop!</td>
        <td>Claude 101 Webinar starting in 1 hour from send time. No recordings — attendance required.</td>
      </tr>
      <tr class="inbox-row">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>TikTok Shop</td>
        <td>Your order is confirmed!</td>
        <td>TikTok Shop order confirmed for Melissa Weiss. Tracking to follow.</td>
      </tr>
      <tr class="inbox-row">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>TikTok Shop</td>
        <td>Your order 577561376577196060 was canceled</td>
        <td>TikTok Shop order canceled due to unexpected circumstances. Check if refund applies.</td>
      </tr>
      <tr class="inbox-row">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Notifications (Zoho Sites)</td>
        <td>Your inactive Zoho Sites website will be deleted soon</td>
        <td>Addressed to "Dennis" — likely a misdirected email. Zoho site will be deleted in 15 days.</td>
      </tr>
      <tr class="inbox-row">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Robinhood</td>
        <td>Your trade confirmations are available</td>
        <td>Recent Robinhood trades confirmed. Review trade confirmations in app.</td>
      </tr>
      <tr class="inbox-row">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Match</td>
        <td>Melissa, you've still got an unread message</td>
        <td>Unread Match message waiting. Personal / dating app follow-up.</td>
      </tr>
      <tr class="inbox-row">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>10-Prompts-You-Need-For-GPT-6-Astra.pdf — Google Drive</td>
        <td>Self-sent Google Drive link to AI prompts PDF. Review/save as needed.</td>
      </tr>
      <!-- TRASH SUMMARY ROWS -->
      <tr class="summary-row">
        <td><span class="badge badge-red">🗑 TRASHED (auto)</span></td>
        <td colspan="2">19 emails auto-trashed (newsletters &amp; phishing) — see Trash Review</td>
        <td>Includes auto-trashed phishing (3 flagged), newsletter digests (4 flagged), and other spam/adult content trashed by system.</td>
      </tr>
      <tr class="summary-row">
        <td><span class="badge badge-gray">🗂 TRASH (manual)</span></td>
        <td colspan="2">11 additional emails in Trash — see Trash Review</td>
        <td>Manually trashed items including casino spam, adult spam, newsletters. Details in Trash Review section.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════ -->
<!-- SECTION 1: HEADER -->
<!-- ═══════════════════════════════════════════════════ -->
<div class="header">
  <div class="header-left">
    <h1>Good morning, Melissa ☀️</h1>
    <div class="subtitle">Executive Briefing prepared by your Chief of Staff</div>
    <div class="subtitle" style="margin-top: 8px;">Friday, September 11, 2026 &nbsp;|&nbsp; <em>Remembrance Day — 25th Anniversary</em></div>
  </div>
  <div class="header-right">
    <div class="stat">Total Emails Reviewed: <span>50</span></div>
    <div class="stat">Calendar Events Reviewed: <span>10</span></div>
    <div class="stat">Unread Emails: <span>44</span></div>
    <div class="stat">Security Threats Blocked: <span>7</span></div>
    <div class="header-badge">🔒 Confidential — Executive Eyes Only</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════ -->
<!-- SECTION 2: EXECUTIVE SUMMARY -->
<!-- ═══════════════════════════════════════════════════ -->
<div class="section yellow">
  <div class="section-title">📋 Executive Summary</div>
  <div class="exec-bullet exec-bullet-red">
    <div class="exec-bullet-icon">🚨</div>
    <div class="exec-bullet-text">
      <strong>Biggest Risk: Heavy phishing &amp; spam campaign targeting your email</strong>
      <span>7 malicious emails detected this cycle — including 3 auto-trashed credential-harvesting phishing attempts (fake cloud storage lockouts), multiple casino scams, and adult spam. Your Slack Pro trial has also expired, cutting off premium workspace features.</span>
    </div>
  </div>
  <div class="exec-bullet exec-bullet-green">
    <div class="exec-bullet-icon">💼</div>
    <div class="exec-bullet-text">
      <strong>Biggest Opportunity: CUNY Vice Chancellor of HR Interview — TODAY at 3:00 PM</strong>
      <span>You have a confirmed in-person interview at CUNY Central Office today (3–4 PM) with Elisa Russo and Sujata Malhotra, followed by a second interview block (4–5 PM). This is your highest-priority career event. Multiple LinkedIn job alerts also arrived overnight with 50+ VP/CHRO-level openings.</span>
    </div>
  </div>
  <div class="exec-bullet exec-bullet-blue">
    <div class="exec-bullet-icon">📅</div>
    <div class="exec-bullet-text">
      <strong>Biggest Calendar Item: Back-to-back CUNY interviews today + PT this morning (already passed)</strong>
      <span>PT was 9:30–10:30 AM. CUNY interviews run 3–5 PM today. Next week: New Patient medical visit Monday (8:45 AM), M&amp;M meeting Tuesday, HR Networking Group Wednesday, Open Office Hours Thursday. The HR Networking Group (Wed) has an unanswered RSVP — action needed.</span>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════ -->
<!-- SECTION 3: ACTION REQUIRED -->
<!-- ═══════════════════════════════════════════════════ -->
<div class="section red">
  <div class="section-title">🔴 Action Required</div>

  <div class="card card-red">
    <div class="flex-row"><span class="badge badge-red">URGENT — TODAY</span><span class="badge badge-green">CAREER</span></div>
    <div class="card-title mt8">🏛️ CUNY Vice Chancellor of HR Interview — In-Person</div>
    <div class="card-meta">Source: Google Calendar | Location: CUNY Central Office | 3:00 PM – 5:00 PM ET</div>
    <div class="card-body">Two back-to-back confirmed interview blocks today with Elisa Russo and Sujata Malhotra. This is a top-tier public university executive HR role. First block (3–4 PM) confirmed; second block (4–5 PM) accepted. Prepare materials, arrive early.</div>
    <div class="card-action red">→ Prep talking points, bring copies of resume/portfolio, confirm building entry. Leave with ample travel time.</div>
    <div class="card-meta mt8">Due: Today by 2:45 PM</div>
  </div>

  <div class="card card-yellow">
    <div class="flex-row"><span class="badge badge-yellow">ACTION — RSVP</span><span class="badge badge-blue">CALENDAR</span></div>
    <div class="card-title mt8">📅 RSVP Needed: HR Networking &amp; Job Search Group — Wednesday, Sep 16</div>
    <div class="card-meta">Source: Google Calendar | Zoom | 12:00–1:30 PM ET | Status: needsAction</div>
    <div class="card-body">Large HR networking Zoom (150+ attendees) on Wednesday — your RSVP is still pending. A separate "Network" block is also confirmed for the same time. Confirm attendance and prepare a 30-second intro.</div>
    <div class="card-action yellow">→ Accept or decline the HR Networking Group invite. Prepare your job search status update.</div>
    <div class="card-meta mt8">Due: Before Wednesday, Sep 16</div>
  </div>

  <div class="card card-yellow">
    <div class="flex-row"><span class="badge badge-yellow">ACTION — RSVP</span><span class="badge badge-blue">CALENDAR</span></div>
    <div class="card-title mt8">📅 RSVP Needed: HR Networking Open Office Hours — Thursday, Sep 17</div>
    <div class="card-meta">Source: Google Calendar | Zoom | 12:00–1:00 PM ET | Status: needsAction</div>
    <div class="card-body">Open office hours session — same large HR networking group. Unanswered RSVP. Note: AI notetaking tools are discouraged in this meeting.</div>
    <div class="card-action yellow">→ Accept or decline the invite before Thursday.</div>
    <div class="card-meta mt8">Due: Before Thursday, Sep 17</div>
  </div>

  <div class="card card-yellow">
    <div class="flex-row"><span class="badge badge-yellow">ACTION — BILLING</span></div>
    <div class="card-title mt8">💳 Slack Pro Trial Ended — Decide: Upgrade or Stay Free</div>
    <div class="card-meta">Source: Slack &lt;no-reply@slack.com&gt; | Received: 10:06 AM</div>
    <div class="card-body">Your Slack Pro trial has ended. Premium features (message history, integrations, video calls) are no longer accessible. Evaluate whether your current use justifies the $7.25+/mo cost.</div>
    <div class="card-action yellow">→ Log in to Slack and decide to upgrade or revert to free tier. Act today to avoid workflow disruption.</div>
    <div class="card-meta mt8">Due: Today</div>
  </div>

  <div class="card card-blue">
    <div class="flex-row"><span class="badge badge-blue">ACTION — PACKAGE</span></div>
    <div class="card-title mt8">📦 Package Waiting at Building — Apt 03H</div>
    <div class="card-meta">Source: 303 East 83rd / Equity Apartments | Received: 10:52 AM | Tracking: #4471</div>
    <div class="card-body">Amazon package delivered to building. Must pick up from lobby/package room. Also: Amazon confirms delivery of 1 cosmetics item (separate email).</div>
    <div class="card-action blue">→ Pick up package from building before heading to CUNY interview or upon return.</div>
    <div class="card-meta mt8">Due: Today</div>
  </div>

  <div class="card card-yellow">
    <div class="flex-row"><span class="badge badge-yellow">ACTION — FINANCES</span></div>
    <div class="card-title mt8">💳 Citi Best Buy Visa — Financing Deadline Warning (Rescued from Trash)</div>
    <div class="card-meta">Source: My Best Buy® Visa® Card / Citi | Rescued from Trash — Protected Sender</div>
    <div class="card-body">24-month financing window is expiring. Act before deadline to use financing benefit (save up to 45% during Labor Day Appliances Sale). This email was rescued from Trash because the sender is on your protected list.</div>
    <div class="card-action yellow">→ Log in to Citi account, review your financing terms, and confirm no remaining balance requires attention before the promotional period ends.</div>
    <div class="card-meta mt8">Due: Imminent — check offer expiry date in email</div>
  </div>

  <div class="card card-yellow">
    <div class="flex-row"><span class="badge badge-yellow">ACTION — ORDERS</span></div>
    <div class="card-title mt8">🛍️ TikTok Shop Order Canceled — Check Refund</div>
    <div class="card-meta">Source: TikTok Shop | Order #577561376577196060 | Received: 2:03 AM</div>
    <div class="card-body">Your TikTok Shop order was canceled due to "unexpected circumstances." Per TikTok policy, you are typically only charged when an order ships — but verify no charge was applied.</div>
    <div class="card-action yellow">→ Check your bank/payment method to confirm no charge was processed. Contact TikTok Shop if needed.</div>
    <div class="card-meta mt8">Due: This week</div>
  </div>

  <div class="card card-gray">
    <div class="flex-row"><span class="badge badge-gray">LOW PRIORITY — REVIEW</span></div>
    <div class="card-title mt8">🌐 Zoho Sites Deletion Warning (Addressed to "Dennis")</div>
    <div class="card-meta">Source: notifications@mailers.zohosites.com | Received: Thu 10:10 PM</div>
    <div class="card-body">Email appears misdirected — addressed to "Dennis," not Melissa. A Zoho Sites website (Site ID: 81841...) will be deleted in 15 days for inactivity. Likely not relevant, but worth a quick check if you have any Zoho account.</div>
    <div class="card-action yellow">→ Verify whether you have a Zoho Sites account. If not, ignore. If yes, log in within 15 days to prevent deletion.</div>
    <div class="card-meta mt8">Due: Within 15 days (by ~Sep 25)</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════ -->
<!-- SECTION 4: FULL 7-DAY CALENDAR -->
<!-- ═══════════════════════════════════════════════════ -->
<div class="section blue">
  <div class="section-title">📅 Full 7-Day Calendar</div>
  <p class="section-intro">All 10 calendar events from September 11–17, 2026. Today is highlighted. Events shown with RSVP status, location, and prep notes.</p>

  <!-- FRIDAY SEPT 11 -->
  <div class="cal-day">
    <div class="cal-day-header today">📌 Friday, September 11, 2026 — TODAY</div>

    <div class="cal-event confirmed">
      <div class="cal-event-time">9:30 AM – 10:30 AM</div>
      <div class="cal-event-title">Pt (Physical Therapy)</div>
      <div class="cal-event-detail">📍 Location: Not specified &nbsp;|&nbsp; ✅ Status: Confirmed</div>
      <div class="cal-event-detail">No attendees listed. Recurring personal health appointment.</div>
      <span class="badge badge-gray">⏰ Already passed</span>
    </div>

    <div class="cal-event confirmed">
      <div class="cal-event-time">3:00 PM – 4:00 PM</div>
      <div class="cal-event-title">🏛️ Vice Chancellor of Human Resources Interview — with Elisa Russo &amp; Sujata Malhotra</div>
      <div class="cal-event-detail">📍 CUNY Central Office &nbsp;|&nbsp; ✅ Status: Confirmed</div>
      <div class="cal-event-detail">Visitor: Melissa Weiss | Provider: CUNY Central Office</div>
      <span class="cal-prep">📝 Prep: Bring resume, research CUNY HR structure, prepare questions for Elisa Russo &amp; Sujata Malhotra</span>
      <span class="badge badge-red" style="margin-left:6px;">⚠️ Key Interview — Do Not Miss</span>
    </div>

    <div class="cal-event accepted">
      <div class="cal-event-time">4:00 PM – 5:00 PM</div>
      <div class="cal-event-title">🏛️ Vice Chancellor of Human Resources Interview (Block 2)</div>
      <div class="cal-event-detail">📍 CUNY Central Office (Teams Meeting link available) &nbsp;|&nbsp; ✅ Status: Accepted</div>
      <div class="cal-event-detail">Second consecutive interview block. May be with different panelists or continuation of first.</div>
      <span class="cal-prep">📝 Prep: Prepare closing remarks, questions about role scope, reporting structure, and timeline for decision</span>
      <span class="cal-conflict">⚠️ Consecutive with Block 1 — no break between</span>
    </div>
  </div>

  <!-- MONDAY SEPT 14 -->
  <div class="cal-day">
    <div class="cal-day-header">Monday, September 14, 2026</div>

    <div class="cal-event accepted">
      <div class="cal-event-time">8:45 AM – 9:40 AM</div>
      <div class="cal-event-title">🏥 New Patient Visit with Andrea D. Card</div>
      <div class="cal-event-detail">📍 53 W 23rd St, 6th Floor, New York NY 10010 &nbsp;|&nbsp; ✅ Status: Accepted</div>
      <div class="cal-event-detail">Appointment Time: 9:00 AM EDT | Phone: 212-746-2900</div>
      <div class="cal-event-detail">Note: Office may contact you if insurance verification is needed before appointment.</div>
      <span class="cal-prep">📝 Prep: Bring insurance card, ID, completed new patient forms if any. Allow extra time for travel to 23rd St. Confirm insurance coverage is verified in advance.</span>
    </div>
  </div>

  <!-- TUESDAY SEPT 15 -->
  <div class="cal-day">
    <div class="cal-day-header">Tuesday, September 15, 2026</div>

    <div class="cal-event accepted">
      <div class="cal-event-time">3:00 PM – 4:00 PM</div>
      <div class="cal-event-title">🤝 M&amp;M (Meeting with Monte Montoya)</div>
      <div class="cal-event-detail">📍 Location: Not specified &nbsp;|&nbsp; ✅ Status: Accepted</div>
      <div class="cal-event-detail">Attendee: monte.montoya@gmail.com</div>
      <span class="cal-prep">📝 Prep: Confirm agenda with Monte. Likely networking or collaboration discussion. Set Zoom/call link if virtual.</span>
    </div>
  </div>

  <!-- WEDNESDAY SEPT 16 -->
  <div class="cal-day">
    <div class="cal-day-header">Wednesday, September 16, 2026</div>

    <div class="cal-event needs-action">
      <div class="cal-event-time">12:00 PM – 1:30 PM</div>
      <div class="cal-event-title">👥 HR Networking &amp; Job Search Group — Zoom 2</div>
      <div class="cal-event-detail">📍 <a href="https://us06web.zoom.us/j/81954171722" style="color:#1d4ed8;">Zoom Link</a> &nbsp;|&nbsp; ⚠️ Status: RSVP Pending (needsAction)</div>
      <div class="cal-event-detail">~180 attendees. Large HR professional networking group with job search focus.</div>
      <span class="cal-prep">📝 Prep: Accept/decline invite ASAP. Prepare 30-second job search status update. Review guidelines doc shared by organizer.</span>
      <span class="cal-conflict">⚠️ RSVP REQUIRED — Still Pending</span>
    </div>

    <div class="cal-event confirmed">
      <div class="cal-event-time">12:00 PM – 1:30 PM</div>
      <div class="cal-event-title">🌐 Network (Personal Block)</div>
      <div class="cal-event-detail">📍 Location: Not specified &nbsp;|&nbsp; ✅ Status: Confirmed</div>
      <div class="cal-event-detail">Personal networking block — appears to overlap with HR Group Zoom above.</div>
      <span class="cal-conflict">⚠️ Overlaps with HR Networking Group — same time slot</span>
    </div>
  </div>

  <!-- THURSDAY SEPT 17 -->
  <div class="cal-day">
    <div class="cal-day-header">Thursday, September 17, 2026</div>

    <div class="cal-event declined">
      <div class="cal-event-time">9:00 AM – 10:30 AM</div>
      <div class="cal-event-title">🔲 Executive Roundtable (John Madigan)</div>
      <div class="cal-event-detail">📍 <a href="https://us02web.zoom.us/j/207786667" style="color:#9ca3af;">Zoom Link</a> &nbsp;|&nbsp; ❌ Status: Declined</div>
      <div class="cal-event-detail">Meeting ID: 207 786 667 | Dial-in: +1-646-876-9923 (NY)</div>
      <span class="badge badge-gray">You declined this event — no action needed unless you wish to reconsider.</span>
    </div>

    <div class="cal-event needs-action">
      <div class="cal-event-time">12:00 PM – 1:00 PM</div>
      <div class="cal-event-title">👥 HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
      <div class="cal-event-detail">📍 <a href="https://us06web.zoom.us/j/85945371140" style="color:#1d4ed8;">Zoom Link</a> &nbsp;|&nbsp; ⚠️ Status: RSVP Pending (needsAction)</div>
      <div class="cal-event-detail">Open discussion format. AI notetaking tools discouraged. Same large HR group.</div>
      <span class="cal-prep">📝 Prep: Accept invite. Come with 1–2 specific job search questions or updates to share.</span>
      <span class="cal-conflict">⚠️ RSVP REQUIRED — Still Pending</span>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════ -->
<!-- SECTION 5: JOB SEARCH & INTERVIEW PIPELINE -->
<!-- ═══════════════════════════════════════════════════ -->
<div class="section green">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>

  <div class="card card-green">
    <div class="flex-row"><span class="badge badge-green">HIGH FIT</span><span class="badge badge-red">TODAY</span></div>
    <div class="card-title mt8">🏛️ CUNY — Vice Chancellor of Human Resources</div>
    <div class="card-meta">Interview: Today, 3:00–5:00 PM | CUNY Central Office | With: Elisa Russo, Sujata Malhotra</div>
    <div class="card-body">Back-to-back interview blocks. Public university CHRO-adjacent executive role. High prestige, stable employer, strong mission alignment. This is the most significant opportunity in your current pipeline.</div>
    <div class="card-action green">→ Prep now. Arrive at CUNY Central Office before 3 PM. Send thank-you emails to both interviewers by tonight.</div>
  </div>

  <div class="card card-green">
    <div class="flex-row"><span class="badge badge-green">HIGH FIT</span><span class="badge badge-blue">REMOTE</span></div>
    <div class="card-title mt8">🏢 Greenbox Capital — VP, People &amp; Culture (US Remote)</div>
    <div class="card-meta">Source: LinkedIn Job Alert | Received: 7:05 AM</div>
    <div class="card-body">VP People & Culture role, remote-eligible. Greenbox Capital is a fintech/lending company. Strong strategic HR scope.</div>
    <div class="card-action green">→ Review full JD on LinkedIn. Apply if strong fit. Deadline unknown — act this week.</div>
  </div>

  <div class="card card-green">
    <div class="flex-row"><span class="badge badge-green">HIGH FIT</span></div>
    <div class="card-title mt8">📋 Backblaze — VP, People (Nasdaq: BLZE | Reports to CHRO)</div>
    <div class="card-meta">Source: LinkedIn Job Alerts (2 separate alerts) | Received: 9:05 AM &amp; 3:05 AM</div>
    <div class="card-body">VP People at a public tech company (Nasdaq-listed), reporting directly to CHRO. Appeared in two separate job alert emails — high priority signal. Tech sector, likely hybrid or remote.</div>
    <div class="card-action green">→ Apply immediately. Appearing in two separate alerts suggests strong algorithmic match.</div>
  </div>

  <div class="card card-green">
    <div class="flex-row"><span class="badge badge-green">MEDIUM-HIGH FIT</span></div>
    <div class="card-title mt8">📋 PeopleOps Jobs — VP Human Resources + 39 More Roles</div>
    <div class="card-meta">Source: LinkedIn Job Alert | Received: 5:05 AM</div>
    <div class="card-body">Broad alert with 39+ VP HR listings. PeopleOps Jobs is an HR-specialized job board — roles tend to be relevant. Worth a systematic scan.</div>
    <div class="card-action green">→ Set aside 30 minutes this weekend to scan all 39 listings. Flag top 3–5 for applications.</div>
  </div>

  <div class="card card-teal">
    <div class="flex-row"><span class="badge badge-teal">RECRUITER</span><span class="badge badge-green">CONNECT</span></div>
    <div class="card-title mt8">🤝 Sonya Tkacs — Founder, Recruitlynk (LinkedIn Connection Suggestion)</div>
    <div class="card-meta">Source: LinkedIn | Received: 8:41 AM</div>
    <div class="card-body">Sonya Tkacs — Founder of Recruitlynk, specializing in Sales, Ops &amp; Leadership Search. Relevant recruiter for C-suite/VP HR placement.</div>
    <div class="card-action green">→ Accept connection. Send a brief personalized note referencing your CHRO/VP HR background.</div>
  </div>

  <div class="card card-teal">
    <div class="flex-row"><span class="badge badge-teal">NETWORKING</span></div>
    <div class="card-title mt8">👥 HR Networking &amp; Job Search Group — Zoom (Wed Sep 16 + Thu Sep 17)</div>
    <div class="card-meta">Source: Google Calendar | 150+ HR professionals | RSVP: Pending</div>
    <div class="card-body">Active large-scale HR networking group with regular Zoom sessions. Both upcoming sessions have unanswered RSVPs. Strong networking opportunity given job search status.</div>
    <div class="card-action green">→ RSVP to both sessions. Prepare your pitch. Especially valuable post-CUNY interview to share update.</div>
  </div>

  <div class="card card-teal">
    <div class="flex-row"><span class="badge badge-teal">NETWORKING</span></div>
    <div class="card-title mt8">🤝 Pashmira Martins — TroopHR LinkedIn Invitation</div>
    <div class="card-meta">Source: LinkedIn | Received: 1:05 AM | Status: Read</div>
    <div class="card-body">LinkedIn connection invitation from Pashmira Martins, TroopHR member. TroopHR is a well-regarded peer community for HR leaders.</div>
    <div class="card-action green">→ Accept this connection — TroopHR community is valuable for CHRO/VP HR networking.</div>
  </div>

  <div class="card card-gray">
    <div class="flex-row"><span class="badge badge-gray">LOW PRIORITY</span></div>
    <div class="card-title mt8">📋 Glassdoor — HR Business Partner at MoneyGram + 10 More</div>
    <div class="card-meta">Source: Glassdoor Jobs | Received: 1:30 AM | Auto-trashed as newsletter</div>
    <div class="card-body">Glassdoor job alert auto-trashed as newsletter digest. HRBP roles may be below target level (VP/CHRO). DoorDash featured prominently in alert.</div>
    <div class="card-action yellow">→ Low priority. Review only if other applications slow down.</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════ -->
<!-- SECTION 6: FULL EMAIL REVIEW BY CATEGORY -->
<!-- ═══════════════════════════════════════════════════ -->
<div class="section red">
  <div class="section-title">🔒 Category: Security / Risk</div>
  <p class="section-intro">10 emails flagged as malicious, phishing, spam, or high-risk. Do not click any links in these emails.</p>
  <div class="phishing-note">🚨 <strong>3 emails were Auto-Trashed as phishing before this briefing was compiled.</strong> These were automatically removed and require no further action beyond awareness. They are noted below.</div>

  <table>
    <thead><tr><th>Type</th><th>From</th><th>Subject</th><th>Status / Notes</th></tr></thead>
    <tbody>
      <tr><td><span class="badge badge-red">Auto-Trashed</span></td><td>Payment-Declined (random domain)</td><td>[melissaw212] Your Cloud Account has been locked on [Fri,11 Sep-2026]</td><td>Auto-Trashed — Phishing. Spoofed cloud storage lockout, credential-harvesting lure, fake deadline threatening photo/video deletion.</td></tr>
      <tr><td><span class="badge badge-red">Auto-Trashed</span></td><td>Cloud_Storage (random domain)</td><td>ACTION REQUIRED: Data protection disabled</td><td>Auto-Trashed — Phishing. Fake expired payment warning, spoofed from random domain, billing credential harvest attempt.</td></tr>
      <tr><td><span class="badge badge-red">Auto-Trashed</span></td><td>Payment-Declined (random domain)</td><td>melissaw212 Your Account Has been Blocked! Photos and Videos will be Removed</td><td>Auto-Trashed — Phishing. Same spoofed cloud storage threat pattern, fake deadline, data deletion threat.</td></tr>
      <tr><td><span class="badge badge-red">Phishing</span></td><td>melissaw212 (spoofed)</td><td>Sorry [melissaw212@gmail.com] We Have To Suspend Your Account Today! Thu,10 Sep-2026</td><td>In Trash. Fake cloud storage suspension threat from spoofed address. Do not click.</td></tr>
      <tr><td><span class="badge badge-red">Phishing</span></td><td>melissaw212 (spoofed)</td><td>Sorry [melissaw212@gmail.com] We Have To Suspend Your Account Today! Fri,11 Sep-2026</td><td>In Trash. Repeat of above — same campaign, next day. Do not click.</td></tr>
      <tr><td><span class="badge badge-orange">Spam — Adult</span></td><td>Sex Trick (random domain)</td><td>PORNT5tar 5ecret</td><td>Not in Trash, not in inbox. Adult spam. Mark spam and delete immediately.</td></tr>
      <tr><td><span class="badge badge-orange">Spam — Adult</span></td><td>Sex_Trick (random domain)</td><td>Watch this Alone</td><td>Not in Trash, not in inbox. Adult spam. Mark spam and delete.</td></tr>
      <tr><td><span class="badge badge-orange">Spam — Adult</span></td><td>FUCK💧ME💧 (random domain)</td><td>USE THE RAW SECRET TO FUCK HER FOR 4 HOURS STRAIGHT</td><td>Not in Trash, not in inbox. Adult spam. Mark spam and delete.</td></tr>
      <tr><td><span class="badge badge-orange">Spam — Adult</span></td><td>FuckMyPussy (random domain)</td><td>[Explicit subject]</td><td>In Trash. Adult spam. Safe to permanently delete.</td></tr>
      <tr><td><span class="badge badge-orange">Spam — Adult</span></td><td>Hard (random domain)</td><td>Thousands of men are using this trick to increase their size</td><td>In Trash. Adult/health spam. Safe to permanently delete.</td></tr>
    </tbody>
  </table>
  <div class="note-box mt8">⚠️ <strong>Recommendation:</strong> Report all non-trashed spam/phishing emails using Gmail's "Report Phishing" function. Consider enabling Google's advanced spam filters. The volume of phishing targeting your username is elevated this cycle.</div>
</div>

<div class="section green">
  <div class="section-title">💼 Category: Job Search</div>
  <p class="section-intro">4 LinkedIn job alert emails reviewed. Multiple high-fit VP/CHRO-level openings.</p>
  <table>
    <thead><tr><th>From</th><th>Subject</th><th>Fit</th><th>Action</th></tr></thead>
    <tbody>
      <tr><td>LinkedIn Job Alerts</td><td>VP, People at Backblaze and 10 more</td><td><span class="badge badge-green">HIGH</span></td><td>Review & apply — Backblaze is public (Nasdaq), reports to CHRO</td></tr>
      <tr><td>LinkedIn Job Alerts</td><td>Vice President – People &amp; Culture at Greenbox Capital and 2 more</td><td><span class="badge badge-green">HIGH</span></td><td>Review & apply — remote eligible</td></tr>
      <tr><td>LinkedIn Job Alerts</td><td>Vice President Human Resources at PeopleOps Jobs and 39 more</td><td><span class="badge badge-green">HIGH</span></td><td>Scan all 39 listings this weekend</td></tr>
      <tr><td>LinkedIn Job Alerts</td><td>VP, People at Backblaze and 39 more</td><td><span class="badge badge-green">HIGH</span></td><td>Duplicate/updated alert — cross-reference. Apply to Backblaze.</td></tr>
    </tbody>
  </table>
  <div class="note-box mt8">📌 <strong>Count: 4 emails.</strong> All from LinkedIn Job Alerts. Strong batch — Backblaze (Nasdaq) is particularly notable. Glassdoor HR HRBP alert (auto-trashed as newsletter) is separately noted in Newsletters section.</div>
</div>

<div class="section teal">
  <div class="section-title">🤝 Category: Recruiters / Networking</div>
  <p class="section-intro">2 LinkedIn networking emails.</p>
  <table>
    <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
    <tbody>
      <tr><td>LinkedIn</td><td>Melissa A, add Sonya Tkacs (Founder, Recruitlynk)</td><td>Accept connection — strong recruiter contact for VP HR search</td></tr>
      <tr><td>Pashmira Martins (LinkedIn)</td><td>You have an invitation — TroopHR Member</td><td>Accept — TroopHR is a top HR leadership community</td></tr>
    </tbody>
  </table>
  <div class="note-box mt8">📌 <strong>Count: 2 emails.</strong> Both are valuable professional connections. Accept both promptly.</div>
</div>

<div class="section blue">
  <div class="section-title">📅 Category: Calendar / Events</div>
  <p class="section-intro">2 emails related to scheduled events and reminders.</p>
  <table>
    <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
    <tbody>
      <tr><td>Zoom</td><td>1 Hour to Go for Day -1 of the Claude 101 Workshop!</td><td>Workshop reminder — no recording provided. Attend live. (Already passed if sent early AM)</td></tr>
      <tr><td>Notifications (Zoho Sites)</td><td>Your inactive Zoho Sites website will be deleted soon</td><td>Check if you have a Zoho account. Addressed to "Dennis" — may be misdirected. 15-day window.</td></tr>
    </tbody>
  </table>
  <div class="note-box mt8">📌 <strong>Count: 2 emails.</strong> Claude 101 Workshop was a timed event (1 hour from send at 2:52 AM UTC). Zoho notification is low priority but actionable within 15 days.</div>
</div>

<div class="section pink">
  <div class="section-title">🏥 Category: Medical / Health</div>
  <p class="section-intro">1 email related to health/medical scheduling.</p>
  <table>
    <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
    <tbody>
      <tr><td>Google Calendar (New Patient Visit)</td><td>New Patient Visit with Andrea D. Card — Sep 14, 8:45 AM</td><td>Confirmed appointment. Arrive at 53 W 23rd St, 6th Floor by 8:45 AM. Bring insurance card.</td></tr>
    </tbody>
  </table>
  <div class="note-box mt8">📌 <strong>Count: 1 email (
