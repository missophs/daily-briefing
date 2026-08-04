<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa Weiss — August 4, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; line-height: 1.5; }
  .page-wrap { max-width: 1200px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a237e 0%, #283593 60%, #3949ab 100%); color: #fff; border-radius: 14px; padding: 32px 36px 24px; margin-bottom: 24px; box-shadow: 0 4px 18px rgba(26,35,126,0.18); }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 15px; opacity: 0.85; margin-top: 4px; }
  .header .meta-row { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.13); border-radius: 8px; padding: 8px 18px; font-size: 13px; }
  .header .meta-item span { font-weight: 700; font-size: 20px; display: block; }

  /* SECTION TITLES */
  .section-title { font-size: 17px; font-weight: 700; letter-spacing: 0.3px; margin: 28px 0 12px; padding: 8px 14px; border-radius: 8px; display: flex; align-items: center; gap: 8px; }
  .section-title.red { background: #fdecea; color: #b71c1c; border-left: 5px solid #e53935; }
  .section-title.yellow { background: #fffde7; color: #856404; border-left: 5px solid #fbc02d; }
  .section-title.blue { background: #e3f2fd; color: #0d47a1; border-left: 5px solid #1976d2; }
  .section-title.green { background: #e8f5e9; color: #1b5e20; border-left: 5px solid #388e3c; }
  .section-title.purple { background: #f3e5f5; color: #4a148c; border-left: 5px solid #7b1fa2; }
  .section-title.gray { background: #f5f5f5; color: #424242; border-left: 5px solid #9e9e9e; }
  .section-title.navy { background: #e8eaf6; color: #1a237e; border-left: 5px solid #3949ab; }
  .section-title.teal { background: #e0f2f1; color: #004d40; border-left: 5px solid #00897b; }

  /* CARDS */
  .card { background: #fff; border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); border-left: 5px solid #ccc; }
  .card.red { border-left-color: #e53935; }
  .card.yellow { border-left-color: #fbc02d; }
  .card.blue { border-left-color: #1976d2; }
  .card.green { border-left-color: #388e3c; }
  .card.purple { border-left-color: #7b1fa2; }
  .card.gray { border-left-color: #9e9e9e; }
  .card.teal { border-left-color: #00897b; }
  .card h3 { font-size: 15px; font-weight: 700; margin-bottom: 6px; }
  .card .label { display: inline-block; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 12px; margin-bottom: 6px; letter-spacing: 0.5px; text-transform: uppercase; }
  .label-red { background: #fdecea; color: #c62828; }
  .label-yellow { background: #fff9c4; color: #856404; }
  .label-blue { background: #e3f2fd; color: #0d47a1; }
  .label-green { background: #e8f5e9; color: #1b5e20; }
  .label-purple { background: #f3e5f5; color: #6a1b9a; }
  .label-gray { background: #f5f5f5; color: #424242; }
  .label-teal { background: #e0f2f1; color: #00695c; }
  .card .meta { font-size: 12px; color: #666; margin-bottom: 4px; }
  .card .meta strong { color: #333; }
  .card .action-step { background: #f8f9fa; border-radius: 6px; padding: 8px 12px; margin-top: 8px; font-size: 13px; }
  .card .action-step strong { color: #1a237e; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.07); margin-bottom: 18px; }
  th { background: #1a237e; color: #fff; padding: 10px 13px; text-align: left; font-size: 12px; font-weight: 700; letter-spacing: 0.4px; text-transform: uppercase; }
  td { padding: 9px 13px; border-bottom: 1px solid #eeeeee; font-size: 13px; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f9f9fb; }
  .triage-status { font-weight: 700; white-space: nowrap; }
  .status-inbox { color: #1565c0; }
  .status-rescued { color: #2e7d32; }
  .status-trashed { color: #757575; }
  .status-auto { color: #b71c1c; }

  /* BADGE */
  .badge { display: inline-block; padding: 2px 9px; border-radius: 10px; font-size: 11px; font-weight: 700; }
  .badge-red { background: #fdecea; color: #c62828; }
  .badge-yellow { background: #fff9c4; color: #856404; }
  .badge-green { background: #e8f5e9; color: #1b5e20; }
  .badge-blue { background: #e3f2fd; color: #0d47a1; }
  .badge-gray { background: #f5f5f5; color: #616161; }
  .badge-purple { background: #f3e5f5; color: #6a1b9a; }

  /* CALENDAR */
  .cal-day { background: #fff; border-radius: 10px; margin-bottom: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); overflow: hidden; }
  .cal-day-header { background: #1a237e; color: #fff; padding: 10px 18px; font-weight: 700; font-size: 14px; }
  .cal-day-header.today { background: linear-gradient(90deg, #1565c0, #1976d2); }
  .cal-event { padding: 12px 18px; border-bottom: 1px solid #eee; display: flex; gap: 16px; align-items: flex-start; }
  .cal-event:last-child { border-bottom: none; }
  .cal-time { font-weight: 700; color: #1a237e; min-width: 120px; font-size: 13px; }
  .cal-info { flex: 1; }
  .cal-info h4 { font-size: 14px; font-weight: 700; margin-bottom: 3px; }
  .cal-info .cal-meta { font-size: 12px; color: #666; }
  .cal-status { font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 10px; white-space: nowrap; }
  .cal-confirmed { background: #e8f5e9; color: #1b5e20; }
  .cal-needs { background: #fff9c4; color: #856404; }
  .cal-declined { background: #fdecea; color: #c62828; }
  .cal-conflict { background: #fff3e0; border-left: 4px solid #f57c00; padding: 6px 12px; border-radius: 4px; margin-top: 6px; font-size: 12px; color: #e65100; font-weight: 600; }

  /* EXEC SUMMARY */
  .exec-summary { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-bottom: 18px; }
  .exec-card { border-radius: 10px; padding: 16px 18px; font-size: 13px; }
  .exec-card h4 { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px; }
  .exec-card.risk { background: #fdecea; border-left: 5px solid #e53935; color: #b71c1c; }
  .exec-card.opp { background: #e8f5e9; border-left: 5px solid #388e3c; color: #1b5e20; }
  .exec-card.cal { background: #e3f2fd; border-left: 5px solid #1976d2; color: #0d47a1; }

  /* DASHBOARD */
  .dashboard-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-bottom: 18px; }
  .dash-tile { background: #fff; border-radius: 10px; padding: 14px 16px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .dash-tile .big-num { font-size: 32px; font-weight: 800; }
  .dash-tile .tile-label { font-size: 12px; color: #666; margin-top: 2px; }
  .dash-tile.red .big-num { color: #e53935; }
  .dash-tile.yellow .big-num { color: #fbc02d; }
  .dash-tile.green .big-num { color: #388e3c; }
  .dash-tile.blue .big-num { color: #1976d2; }
  .dash-tile.purple .big-num { color: #7b1fa2; }
  .dash-tile.gray .big-num { color: #9e9e9e; }

  /* PRIORITY */
  .priority-card { background: #fff; border-radius: 10px; padding: 18px 22px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); display: flex; gap: 16px; align-items: flex-start; }
  .priority-num { font-size: 32px; font-weight: 800; color: #1a237e; min-width: 40px; }
  .priority-content h4 { font-size: 15px; font-weight: 700; }
  .priority-content p { font-size: 13px; color: #555; margin-top: 4px; }

  /* ACCOUNTING */
  .accounting-total { background: #1a237e; color: #fff; font-weight: 700; }
  .accounting-total td { border-bottom: none; }

  /* MISC */
  .pill { display: inline-block; padding: 1px 8px; border-radius: 10px; font-size: 11px; font-weight: 600; }
  .pill-high { background: #fdecea; color: #c62828; }
  .pill-med { background: #fff9c4; color: #856404; }
  .pill-low { background: #f5f5f5; color: #616161; }
  .divider { border: none; border-top: 2px solid #e0e0e0; margin: 24px 0; }
  .note-box { background: #fff3e0; border-left: 4px solid #f57c00; border-radius: 6px; padding: 10px 14px; font-size: 13px; color: #e65100; margin-bottom: 14px; }
  .phish-box { background: #fdecea; border-left: 4px solid #e53935; border-radius: 6px; padding: 10px 14px; font-size: 13px; color: #b71c1c; margin-bottom: 8px; }
  .trash-box { background: #f5f5f5; border-left: 4px solid #9e9e9e; border-radius: 6px; padding: 10px 14px; font-size: 13px; color: #424242; margin-bottom: 8px; }
  .restore-box { background: #e8f5e9; border-left: 4px solid #388e3c; border-radius: 6px; padding: 10px 14px; font-size: 13px; color: #1b5e20; margin-bottom: 8px; }
  a { color: #1976d2; text-decoration: none; }
  @media (max-width: 800px) {
    .exec-summary, .dashboard-grid { grid-template-columns: 1fr 1fr; }
  }
  @media (max-width: 500px) {
    .exec-summary, .dashboard-grid { grid-template-columns: 1fr; }
    .header .meta-row { gap: 10px; }
  }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ═══════════════════════════════════════════════════════════
     HEADER
════════════════════════════════════════════════════════════ -->
<div class="header">
  <div class="subtitle">EXECUTIVE BRIEFING — PREPARED BY CHIEF OF STAFF</div>
  <h1>Good Morning, Melissa ☀️</h1>
  <div class="subtitle">Tuesday, August 4, 2026 &nbsp;|&nbsp; Your day at a glance</div>
  <div class="meta-row">
    <div class="meta-item"><span>50</span>Total Emails Reviewed</div>
    <div class="meta-item"><span>7</span>Calendar Events (7-Day)</div>
    <div class="meta-item"><span>4</span>Auto-Trashed (Phishing)</div>
    <div class="meta-item"><span>3</span>Action Items — High Priority</div>
    <div class="meta-item"><span>1</span>Event Today</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 0 — EMAIL TRIAGE QUICK LIST
════════════════════════════════════════════════════════════ -->
<div class="section-title navy">📋 Email Triage Quick List</div>
<p style="font-size:12px;color:#666;margin-bottom:10px;">Rescued emails appear first, then inbox emails, then summary rows for trash.</p>
<table>
  <thead>
    <tr>
      <th style="width:140px;">Status</th>
      <th style="width:200px;">From</th>
      <th>Subject</th>
      <th>Summary</th>
    </tr>
  </thead>
  <tbody>
    <!-- INBOX EMAILS (individual rows) -->
    <tr>
      <td class="triage-status status-inbox">📥 INBOX</td>
      <td><strong>Bank of America</strong></td>
      <td>Delivery status of credit card - 5690 - Created</td>
      <td>New credit card created — Step 1 of 3; shipping details pending. <span class="badge badge-yellow">Action</span></td>
    </tr>
    <tr>
      <td class="triage-status status-inbox">📥 INBOX</td>
      <td><strong>Inclusively</strong></td>
      <td>melissa weiss - Check out these recommended jobs for you!</td>
      <td>Job recommendations from Inclusively based on your profile. <span class="badge badge-green">Job Search</span></td>
    </tr>
    <tr>
      <td class="triage-status status-inbox">📥 INBOX</td>
      <td><strong>Bank of America</strong></td>
      <td>A direct deposit was credited to your account</td>
      <td>$760.38 NYS DOL UI direct deposit to Personal Checking/Savings – 7471. <span class="badge badge-yellow">Financial</span></td>
    </tr>
    <tr>
      <td class="triage-status status-inbox">📥 INBOX</td>
      <td><strong>Old Navy</strong></td>
      <td>Forget to check out? It happens</td>
      <td>Abandoned cart reminder. <span class="badge badge-gray">Promo</span></td>
    </tr>
    <tr>
      <td class="triage-status status-inbox">📥 INBOX</td>
      <td><strong>Match</strong></td>
      <td>Jay likes you. See if it's mutual.</td>
      <td>Jay (47, Tenafly NJ) liked your profile on Match. <span class="badge badge-gray">Personal</span></td>
    </tr>
    <tr>
      <td class="triage-status status-inbox">📥 INBOX</td>
      <td><strong>Match</strong></td>
      <td>You've had a profile view from Jay</td>
      <td>Jay viewed your Match profile. <span class="badge badge-gray">Personal</span></td>
    </tr>
    <tr>
      <td class="triage-status status-inbox">📥 INBOX</td>
      <td><strong>LinkedIn (Ashish Mishra)</strong></td>
      <td>I'd like to connect 👤</td>
      <td>Ashish Mishra, Founder at Talscan, awaiting connection response. <span class="badge badge-green">Networking</span></td>
    </tr>
    <tr>
      <td class="triage-status status-inbox">📥 INBOX</td>
      <td><strong>OkCupid</strong></td>
      <td>Someone likes you</td>
      <td>Match notification from OkCupid. <span class="badge badge-gray">Personal</span></td>
    </tr>
    <tr>
      <td class="triage-status status-inbox">📥 INBOX</td>
      <td><strong>Bank of America</strong></td>
      <td>Billing Dispute for account - 2994 - Merchant credit has been issued</td>
      <td>Dispute Step 2 of 3 — merchant credit issued on account 2994. <span class="badge badge-yellow">Financial</span></td>
    </tr>
    <tr>
      <td class="triage-status status-inbox">📥 INBOX</td>
      <td><strong>SHEIN</strong></td>
      <td>Start from $4.99 | Your weekly wardrobe update.</td>
      <td>Weekly promotional email. <span class="badge badge-gray">Promo</span></td>
    </tr>
    <tr>
      <td class="triage-status status-inbox">📥 INBOX</td>
      <td><strong>JobLeads</strong></td>
      <td>Why successful candidates upload their resume</td>
      <td>Resume-upload prompt from JobLeads for better matches. <span class="badge badge-green">Job Search</span></td>
    </tr>
    <tr>
      <td class="triage-status status-inbox">📥 INBOX</td>
      <td><strong>Nordstrom Rack</strong></td>
      <td>Your Nordstrom Rack order #1054718582</td>
      <td>Order confirmation — more updates coming. <span class="badge badge-yellow">Order</span></td>
    </tr>
    <tr>
      <td class="triage-status status-inbox">📥 INBOX</td>
      <td><strong>TikTok Shop</strong></td>
      <td>Your order is confirmed!</td>
      <td>Order confirmed, preparing for shipment. <span class="badge badge-yellow">Order</span></td>
    </tr>
    <tr>
      <td class="triage-status status-inbox">📥 INBOX</td>
      <td><strong>OpenArt</strong></td>
      <td>⚠️ Your OpenArt data will be deleted within 7 days</td>
      <td>Images/videos deleted in 7 days unless you subscribe. <span class="badge badge-yellow">Deadline</span></td>
    </tr>
    <tr>
      <td class="triage-status status-inbox">📥 INBOX</td>
      <td><strong>OpenArt AI / Stripe</strong></td>
      <td>Your refund from OpenArt AI #3162-7712</td>
      <td>Refund issued from OpenArt AI via Stripe. <span class="badge badge-yellow">Financial</span></td>
    </tr>
    <tr>
      <td class="triage-status status-inbox">📥 INBOX</td>
      <td><strong>Bank of America</strong></td>
      <td>Fraud Claim for account - 2994 - Claim request received</td>
      <td>Fraud claim Step 1 of 3 received for account 2994. <span class="badge badge-red">Urgent</span></td>
    </tr>
    <tr>
      <td class="triage-status status-inbox">📥 INBOX</td>
      <td><strong>LinkedIn Job Alerts</strong></td>
      <td>Chief People & Workplace Officer at Confidential: up to $600K/year</td>
      <td>High-value CPO/CPWO alert — actively recruiting, confidential employer. <span class="badge badge-green">High Fit</span></td>
    </tr>
    <tr>
      <td class="triage-status status-inbox">📥 INBOX</td>
      <td><strong>Reuters Support</strong></td>
      <td>RCOM | Case#00318393 | Feedback</td>
      <td>Thomson Reuters support acknowledged your feedback about the fraudulent recruiter domain. <span class="badge badge-red">Security</span></td>
    </tr>
    <tr>
      <td class="triage-status status-inbox">📥 INBOX</td>
      <td><strong>Catholic Health MyChart</strong></td>
      <td>You have a new billing statement in Catholic Health MyChart</td>
      <td>New medical billing statement available for review/payment. <span class="badge badge-yellow">Medical</span></td>
    </tr>
    <tr>
      <td class="triage-status status-inbox">📥 INBOX</td>
      <td><strong>melissa (self)</strong></td>
      <td>your linkedin post</td>
      <td>Self-note: "The cheapest media you'll ever buy" — LinkedIn post draft/note. <span class="badge badge-gray">Personal</span></td>
    </tr>
    <!-- Sent/non-inbox individual notable emails -->
    <tr>
      <td class="triage-status" style="color:#555;">📤 SENT/OTHER</td>
      <td><strong>melissa (self)</strong></td>
      <td>Re: Head of People / VP of Human Resources</td>
      <td>Melissa's replies in the fraudulent "David Hersch" thread. <span class="badge badge-red">Security</span></td>
    </tr>
    <tr>
      <td class="triage-status" style="color:#555;">📤 SENT/OTHER</td>
      <td><strong>melissa (self)</strong></td>
      <td>I've built the function you're describing</td>
      <td>Outbound application to Travis — strong proactive outreach. <span class="badge badge-green">Job Search</span></td>
    </tr>
    <tr>
      <td class="triage-status" style="color:#555;">📤 SENT/OTHER</td>
      <td><strong>melissa (self)</strong></td>
      <td>website</td>
      <td>Self-note about Claude/Fable website edits. <span class="badge badge-gray">Personal</span></td>
    </tr>
    <tr>
      <td class="triage-status" style="color:#555;">📤 SENT/OTHER</td>
      <td><strong>melissa (self)</strong></td>
      <td>Re: [EXTERNAL] 15 years, one specific fit for your Corporate Affairs role</td>
      <td>Follow-up sent to Susan Medina; applied online. <span class="badge badge-green">Job Search</span></td>
    </tr>
    <tr>
      <td class="triage-status" style="color:#555;">📤 SENT/OTHER</td>
      <td><strong>Bank of America</strong></td>
      <td>Your credit card has been deleted from Apple Pay</td>
      <td>Card 2994 removed from Apple Pay — likely tied to fraud claim. <span class="badge badge-red">Security</span></td>
    </tr>
    <tr>
      <td class="triage-status" style="color:#555;">📤 SENT/OTHER</td>
      <td><strong>LinkedIn Job Alerts</strong></td>
      <td>Senior Human Resources Business Partner at Orca Security</td>
      <td>HRBP alert from LinkedIn — worth reviewing. <span class="badge badge-green">Job Search</span></td>
    </tr>
    <tr>
      <td class="triage-status" style="color:#555;">📤 SENT/OTHER</td>
      <td><strong>Glassdoor</strong></td>
      <td>HR Manager at Meow Wolf + 8 more (Remote, US)</td>
      <td>Glassdoor digest — remote HR roles. <span class="badge badge-green">Job Search</span></td>
    </tr>
    <tr>
      <td class="triage-status" style="color:#555;">📤 SENT/OTHER</td>
      <td><strong>Glassdoor</strong></td>
      <td>Relations Coordinator at Heard.Help + 5 more (New York, NY)</td>
      <td>Glassdoor digest — NY-area roles. <span class="badge badge-green">Job Search</span></td>
    </tr>
    <tr>
      <td class="triage-status" style="color:#555;">📤 SENT/OTHER</td>
      <td><strong>Glassdoor</strong></td>
      <td>Assoc. HR BP at 1-800-FLOWERS + 10 more (New York, NY)</td>
      <td>Glassdoor digest — NY-area HR roles. <span class="badge badge-green">Job Search</span></td>
    </tr>
    <tr>
      <td class="triage-status" style="color:#555;">📤 SENT/OTHER</td>
      <td><strong>Glassdoor</strong></td>
      <td>HR Manager at Novolex + 10 more (United States)</td>
      <td>Glassdoor digest — national HR roles. <span class="badge badge-green">Job Search</span></td>
    </tr>
    <tr>
      <td class="triage-status" style="color:#555;">📤 SENT/OTHER</td>
      <td><strong>Ladders</strong></td>
      <td>Hey Melissa, here's your Resume Report</td>
      <td>Resume flagged as stale (last updated 12/26/16). <span class="badge badge-yellow">Action</span></td>
    </tr>
    <tr>
      <td class="triage-status" style="color:#555;">📤 SENT/OTHER</td>
      <td><strong>Facebook</strong></td>
      <td>About Ana and others: 32 other new notifications</td>
      <td>32 unread Facebook notifications (Noor Hussein, Charo Garcia). <span class="badge badge-gray">Personal</span></td>
    </tr>
    <tr>
      <td class="triage-status" style="color:#555;">📤 SENT/OTHER</td>
      <td><strong>Chewy.com</strong></td>
      <td>For the walkers, fetchers, and snack-seekers</td>
      <td>Chewy promotional email for pet supplies. <span class="badge badge-gray">Promo</span></td>
    </tr>
    <!-- TRASH — SUMMARY ROWS ONLY -->
    <tr style="background:#fff8f8;">
      <td class="triage-status status-auto">🚫 AUTO-TRASHED (4)</td>
      <td colspan="2"><em>David Hersch / thomsonreute.com (×4 messages in thread) — Phishing/Fraud</em></td>
      <td>4 emails auto-trashed as phishing — see <strong>Trash Review</strong> &amp; <strong>Security / Risk</strong> sections below.</td>
    </tr>
    <tr style="background:#fff8f8;">
      <td class="triage-status status-auto">🚫 AUTO-TRASHED (2)</td>
      <td colspan="2"><em>Blood Sugar Alert, ED-Trick, Casino scam, Cloud Admin phishing — spam/scam</em></td>
      <td>Additional spam/scam/phishing not auto-flagged but never reached inbox — see <strong>Trash Review</strong>.</td>
    </tr>
    <tr style="background:#fafafa;">
      <td class="triage-status status-trashed">🗂 TRASH (3 manual)</td>
      <td colspan="2"><em>Gemma Bonham-Carter, Kohl's, YesStyle.com</em></td>
      <td>3 emails manually trashed — see <strong>Trash Review</strong> section below.</td>
    </tr>
  </tbody>
</table>

<hr class="divider">

<!-- ═══════════════════════════════════════════════════════════
     SECTION 2 — EXECUTIVE SUMMARY
════════════════════════════════════════════════════════════ -->
<div class="section-title navy">⚡ Executive Summary</div>
<div class="exec-summary">
  <div class="exec-card risk">
    <h4>🔴 Biggest Risk / Urgent</h4>
    An active fraud claim is open on Bank of America account 2994 (card also removed from Apple Pay). Separately, a sophisticated employment scam using the typosquat domain <strong>thomsonreute.com</strong> (not thomsonreuters.com) has been targeting you — 4 emails auto-trashed. Thomson Reuters support (legitimate) has acknowledged your report.
  </div>
  <div class="exec-card opp">
    <h4>🟢 Biggest Job Search Opportunity</h4>
    LinkedIn alert for <strong>Chief People &amp; Workplace Officer</strong> at a confidential employer — up to <strong>$600K/year</strong>, actively recruiting. This is your highest-value lead right now. Also: proactive outreach email to Travis already sent today. Act fast on the CPO role.
  </div>
  <div class="exec-card cal">
    <h4>🔵 Biggest Calendar / Deadline</h4>
    You have <strong>PT (physical therapy or personal training) at 10–11 AM today</strong>. Tomorrow (Aug 5) is the HR Networking &amp; Job Search Group Zoom — RSVP still pending. OpenArt data deletion in 7 days requires a decision on subscription.
  </div>
</div>

<hr class="divider">

<!-- ═══════════════════════════════════════════════════════════
     SECTION 3 — ACTION REQUIRED
════════════════════════════════════════════════════════════ -->
<div class="section-title red">🚨 Action Required</div>

<div class="card red">
  <span class="label label-red">URGENT — FRAUD</span>
  <h3>Bank of America Fraud Claim — Account 2994 (Step 1 of 3)</h3>
  <div class="meta"><strong>Source:</strong> Bank of America &lt;onlinebanking@ealerts.bankofamerica.com&gt; &nbsp;|&nbsp; <strong>Received:</strong> Mon Aug 3, 2026</div>
  <p>A fraud claim has been filed for account 2994. The card has also been removed from Apple Pay. A billing dispute on the same account (2994) shows a merchant credit has been issued (Step 2 of 3). Ensure claim is progressing and confirm no unauthorized charges remain.</p>
  <div class="action-step"><strong>Next Step:</strong> Log into Bank of America online banking to track claim progress, verify no additional unauthorized transactions, and confirm new card (ending 5690) is on its way.</div>
  <div class="action-step"><strong>Due:</strong> Today — do not delay.</div>
</div>

<div class="card red">
  <span class="label label-red">SECURITY ALERT</span>
  <h3>Fraudulent Recruiter Thread — "David Hersch" / thomsonreute.com</h3>
  <div class="meta"><strong>Source:</strong> david.hersch@thomsonreute.com (typosquat — NOT thomsonreuters.com) &nbsp;|&nbsp; 4 messages auto-trashed</div>
  <p>You correctly identified and flagged this domain. Three separate people warned you they were being scammed by this same contact. You filed a report with Reuters Support (legitimate response received: Case #00318393). All "David Hersch" emails have been auto-trashed. Do NOT engage further, share personal info, or click any links.</p>
  <div class="action-step"><strong>Next Step:</strong> No further engagement. Your report to Thomson Reuters is logged (Case #00318393). Consider warning your HR network group about this scam.</div>
  <div class="action-step"><strong>Due:</strong> Awareness only — already handled.</div>
</div>

<div class="card yellow">
  <span class="label label-yellow">DEADLINE — 7 DAYS</span>
  <h3>OpenArt Data Deletion Warning</h3>
  <div class="meta"><strong>Source:</strong> OpenArt &lt;marketing@openart.ai&gt; &nbsp;|&nbsp; Received: Tue Aug 4, 2026</div>
  <p>Your OpenArt images and videos will be permanently deleted within 7 days unless you subscribe. A refund from OpenArt AI was also just issued (Stripe receipt #3162-7712). Decide whether to subscribe, export, or let data lapse.</p>
  <div class="action-step"><strong>Next Step:</strong> Log into OpenArt, export/download any images you want to keep, then decide on subscription.</div>
  <div class="action-step"><strong>Due:</strong> By August 11, 2026.</div>
</div>

<div class="card yellow">
  <span class="label label-yellow">RSVP NEEDED</span>
  <h3>HR Networking &amp; Job Search Group — Zoom (Aug 5)</h3>
  <div class="meta"><strong>Source:</strong> Google Calendar &nbsp;|&nbsp; <strong>Status:</strong> Needs Action</div>
  <p>Tomorrow's HR Networking &amp; Job Search Group Zoom session (12:00–1:30 PM) has not yet been confirmed. This is a large group (190+ attendees) and a key job search network.</p>
  <div class="action-step"><strong>Next Step:</strong> Accept the calendar invite. Prepare your 30-second intro and any updates on your search.</div>
  <div class="action-step"><strong>Due:</strong> Today (RSVP) / Tomorrow 12:00 PM (attend).</div>
</div>

<div class="card green">
  <span class="label label-green">HIGH PRIORITY — JOB LEAD</span>
  <h3>Chief People &amp; Workplace Officer — Up to $600K/Year (Confidential)</h3>
  <div class="meta"><strong>Source:</strong> LinkedIn Job Alerts &lt;jobalerts-noreply@linkedin.com&gt; &nbsp;|&nbsp; Received: Mon Aug 3, 2026</div>
  <p>Confidential employer actively recruiting for a Chief People &amp; Workplace Officer role at up to $600K/year. This is a direct match for your experience level and search target. Actively recruiting means urgency.</p>
  <div class="action-step"><strong>Next Step:</strong> Open LinkedIn alert immediately, review the full posting, and apply today if qualified.</div>
  <div class="action-step"><strong>Due:</strong> Today — active recruitment moves fast.</div>
</div>

<div class="card yellow">
  <span class="label label-yellow">MEDICAL BILLING</span>
  <h3>New Billing Statement — Catholic Health MyChart</h3>
  <div class="meta"><strong>Source:</strong> mychartteam@chsli.org &nbsp;|&nbsp; Received: Mon Aug 3, 2026</div>
  <p>A new billing statement is available in Catholic Health MyChart. Log in to review the amount and pay or set up a payment plan.</p>
  <div class="action-step"><strong>Next Step:</strong> Log into MyChart at chsli.org to review and pay the statement.</div>
  <div class="action-step"><strong>Due:</strong> This week.</div>
</div>

<div class="card yellow">
  <span class="label label-yellow">RSVP NEEDED</span>
  <h3>HR Networking Open Office Hours — Zoom (Aug 6)</h3>
  <div class="meta"><strong>Source:</strong> Google Calendar &nbsp;|&nbsp; <strong>Status:</strong> Needs Action</div>
  <p>Thursday Aug 6, 12:00–1:00 PM Open Office Hours Zoom. Status: Needs Action. Note: conflicts with your "disability" appointment (9–11 AM) but should not overlap.</p>
  <div class="action-step"><strong>Next Step:</strong> Accept or decline the calendar invite.</div>
  <div class="action-step"><strong>Due:</strong> Today.</div>
</div>

<div class="card yellow">
  <span class="label label-yellow">INSURANCE / BILLING</span>
  <h3>State Farm Bill — Due Aug 7</h3>
  <div class="meta"><strong>Source:</strong> Google Calendar &nbsp;|&nbsp; <strong>Date:</strong> August 7, 2026 (all-day reminder)</div>
  <p>State Farm insurance bill reminder on calendar for August 7. Ensure payment is scheduled or submitted before the due date.</p>
  <div class="action-step"><strong>Next Step:</strong> Verify payment is scheduled or pay online before Aug 7.</div>
  <div class="action-step"><strong>Due:</strong> August 7, 2026.</div>
</div>

<hr class="divider">

<!-- ═══════════════════════════════════════════════════════════
     SECTION 4 — FULL 7-DAY CALENDAR
════════════════════════════════════════════════════════════ -->
<div class="section-title blue">📅 Full 7-Day Calendar</div>

<!-- TUESDAY AUG 4 -->
<div class="cal-day">
  <div class="cal-day-header today">📍 TODAY — Tuesday, August 4, 2026</div>
  <div class="cal-event">
    <div class="cal-time">10:00 AM – 11:00 AM</div>
    <div class="cal-info">
      <h4>Pt <span class="cal-status cal-confirmed">✅ Confirmed</span></h4>
      <div class="cal-meta">📍 No location specified &nbsp;|&nbsp; No attendees listed &nbsp;|&nbsp; No description</div>
      <div class="cal-meta" style="margin-top:4px;"><strong>Prep:</strong> Likely PT (physical therapy) or personal training. Confirm location/details in advance. Allow travel time if needed.</div>
    </div>
  </div>
</div>

<!-- WEDNESDAY AUG 5 -->
<div class="cal-day">
  <div class="cal-day-header">Wednesday, August 5, 2026</div>
  <div class="cal-event">
    <div class="cal-time">12:00 PM – 1:30 PM</div>
    <div class="cal-info">
      <h4>HR Networking &amp; Job Search Group — Zoom 2 <span class="cal-status cal-needs">⚠️ RSVP Needed</span></h4>
      <div class="cal-meta">🔗 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Join Zoom Meeting</a> &nbsp;|&nbsp; 190+ attendees</div>
      <div class="cal-meta" style="margin-top:4px;"><strong>Prep:</strong> Prepare 30-second professional update. Review team guidelines document linked in description. RSVP today.</div>
      <div class="cal-conflict">⚠️ RSVP PENDING — Accept or decline today.</div>
    </div>
  </div>
  <div class="cal-event">
    <div class="cal-time">12:00 PM – 1:30 PM</div>
    <div class="cal-info">
      <h4>Network <span class="cal-status cal-confirmed">✅ Confirmed</span></h4>
      <div class="cal-meta">📍 No location specified &nbsp;|&nbsp; Likely same as HR Networking Zoom above (same time block)</div>
      <div class="cal-meta" style="margin-top:4px;"><strong>Prep:</strong> This appears to be your personal reminder or a parallel networking block. Confirm whether this is a duplicate of the HR Networking Zoom or a separate commitment.</div>
      <div class="cal-conflict">⚠️ POTENTIAL DUPLICATE — Overlaps with HR Networking &amp; Job Search Group (same time). Confirm.</div>
    </div>
  </div>
</div>

<!-- THURSDAY AUG 6 -->
<div class="cal-day">
  <div class="cal-day-header">Thursday, August 6, 2026</div>
  <div class="cal-event">
    <div class="cal-time">9:00 AM – 11:00 AM</div>
    <div class="cal-info">
      <h4>disability <span class="cal-status cal-confirmed">✅ Confirmed</span></h4>
      <div class="cal-meta">📍 No location specified &nbsp;|&nbsp; No attendees &nbsp;|&nbsp; No description</div>
      <div class="cal-meta" style="margin-top:4px;"><strong>Prep:</strong> Likely a disability-related appointment (benefits, legal, medical). Confirm location/call-in details. Allow full 2 hours.</div>
    </div>
  </div>
  <div class="cal-event">
    <div class="cal-time">9:00 AM – 10:30 AM</div>
    <div class="cal-info">
      <h4>Executive Roundtable <span class="cal-status cal-declined">❌ Declined</span></h4>
      <div class="cal-meta">🔗 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Meeting</a> (John Madigan) &nbsp;|&nbsp; Meeting ID: 207 786 667 &nbsp;|&nbsp; Password: 205454</div>
      <div class="cal-meta" style="margin-top:4px;"><strong>Note:</strong> You declined this event. It conflicts with your disability appointment (9–11 AM). If you reconsider, contact organizer.</div>
      <div class="cal-conflict">⚠️ CONFLICT — Overlaps with "disability" appointment (9–11 AM). Correctly declined.</div>
    </div>
  </div>
  <div class="cal-event">
    <div class="cal-time">12:00 PM – 1:00 PM</div>
    <div class="cal-info">
      <h4>HR Networking &amp; Job Search: Open Office Hours — Zoom 2 <span class="cal-status cal-needs">⚠️ RSVP Needed</span></h4>
      <div class="cal-meta">🔗 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Join Zoom Meeting</a> &nbsp;|&nbsp; 190+ attendees</div>
      <div class="cal-meta" style="margin-top:4px;"><strong>Prep:</strong> Open discussion (no recording). No AI notetaking tools per host request. Good opportunity for casual networking after disability appt.</div>
      <div class="cal-conflict">⚠️ RSVP PENDING — Accept or decline today.</div>
    </div>
  </div>
</div>

<!-- FRIDAY AUG 7 -->
<div class="cal-day">
  <div class="cal-day-header">Friday, August 7, 2026</div>
  <div class="cal-event">
    <div class="cal-time">All Day</div>
    <div class="cal-info">
      <h4>State Farm Bill <span class="cal-status cal-confirmed">✅ Reminder Set</span></h4>
      <div class="cal-meta">📍 No location &nbsp;|&nbsp; All-day billing reminder</div>
      <div class="cal-meta" style="margin-top:4px;"><strong>Prep:</strong> Insurance bill due. Log into State Farm or your bank to confirm payment is scheduled. Do not miss.</div>
    </div>
  </div>
</div>

<!-- SAT–TUE: No events -->
<div class="cal-day">
  <div class="cal-day-header">Saturday, August 8 – Tuesday, August 11, 2026</div>
  <div class="cal-event">
    <div class="cal-time">—</div>
    <div class="cal-info">
      <h4 style="color:#888;">No calendar events scheduled.</h4>
      <div class="cal-meta">Note: OpenArt data deletion deadline falls ~Aug 11. Plan to export data before then.</div>
    </div>
  </div>
</div>

<hr class="divider">

<!-- ═══════════════════════════════════════════════════════════
     SECTION 5 — JOB SEARCH & INTERVIEW PIPELINE
════════════════════════════════════════════════════════════ -->
<div class="section-title green">💼 Job Search &amp; Interview Pipeline</div>

<table>
  <thead>
    <tr>
      <th>Fit</th>
      <th>Role / Opportunity</th>
      <th>Source</th>
      <th>Status</th>
      <th>Next Step</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="pill pill-high">HIGH</span></td>
      <td><strong>Chief People &amp; Workplace Officer</strong><br><em>Confidential Employer — up to $600K/yr</em></td>
      <td>LinkedIn Job Alerts</td>
      <td><span class="badge badge-red">Not Yet Applied</span></td>
      <td>Apply TODAY — actively recruiting</td>
    </tr>
    <tr>
      <td><span class="pill pill-high">HIGH</span></td>
      <td><strong>Head of People / VP Human Resources</strong><br><em>Proactive outreach to Travis</em></td>
      <td>Melissa (self-sent)</td>
      <td><span class="badge badge-yellow">Application Sent</span></td>
      <td>Await response; follow up in 3–5 days if none</td>
    </tr>
    <tr>
      <td><span class="pill pill-high">HIGH</span></td>
      <td><strong>Senior HRBP — Orca Security</strong></td>
      <td>LinkedIn Job Alerts</td>
      <td><span class="badge badge-yellow">Alert Received</span></td>
      <td>Review posting and apply if aligned</td>
    </tr>
    <tr>
      <td><span class="pill pill-med">MED</span></td>
      <td><strong>Corporate Affairs Role</strong><br><em>Susan Medina (Exec recruiter)</em></td>
      <td>Outbound email (self)</td>
      <td><span class="badge badge-green">Applied Online ✓</span></td>
      <td>Awaiting recruiter response; no further action</td>
    </tr>
    <tr>
      <td><span class="pill pill-med">MED</span></td>
      <td><strong>HR Manager at Meow Wolf + 8 Remote Roles</strong></td>
      <td>Glassdoor Digest</td>
      <td><span class="badge badge-gray">Unreviewed</span></td>
      <td>Scan digest; filter by fit and apply selectively</td>
    </tr>
    <tr>
      <td><span class="pill pill-med">MED</span></td>
      <td><strong>Relations Coordinator, Heard.Help + 5 NY Roles</strong></td>
      <td>Glassdoor Digest</td>
      <td><span class="badge badge-gray">Unreviewed</span></td>
      <td>Review — Heard.Help is a mental health startup; possible fit</td>
    </tr>
    <tr>
      <td><span class="pill pill-med">MED</span></td>
      <td><strong>Assoc. HR BP at 1-800-FLOWERS + 10 NY Roles</strong></td>
      <td>Glassdoor Digest</td>
      <td><span class="badge badge-gray">Unreviewed</span></td>
      <td>Review; 1-800-Flowers is a sizeable employer in NY</td>
    </tr>
    <tr>
      <td><span class="pill pill-med">MED</span></td>
      <td><strong>HR Manager at Novolex + 10 US Roles</strong></td>
      <td>Glassdoor Digest</td>
      <td><span class="badge badge-gray">Unreviewed</span></td>
      <td>Review for any senior-level fits</td>
    </tr>
    <tr>
      <td><span class="pill pill-med">MED</span></td>
      <td><strong>Recommended jobs — profile match</strong></td>
      <td>Inclusively</td>
      <td><span class="badge badge-gray">Unreviewed</span></td>
      <td>Review recommendations; Inclusively focuses on disability-inclusive employers</td>
    </tr>
    <tr>
      <td><span class="pill pill-low">LOW</span></td>
      <td><strong>Resume upload suggestion for better matches</strong></td>
      <td>JobLeads</td>
      <td><span class="badge badge-gray">Action Optional</span></td>
      <td>Upload updated resume to JobLeads for improved matching</td>
    </tr>
    <tr>
      <td><span class="pill pill-low">LOW</span></td>
      <td><strong>LinkedIn Connection — Ashish Mishra, Founder, Talscan</strong></td>
      <td>LinkedIn</td>
      <td><span class="badge badge-yellow">Pending Response</span></td>
      <td>Review Talscan; accept if relevant to HR/People space</td>
    </tr>
    <tr>
      <td><span class="pill pill-low">LOW</span></td>
      <td><strong>HR Networking &amp; Job Search Group Zoom</strong></td>
      <td>Google Calendar (Aug 5)</td>
      <td><span class="badge badge-red">RSVP Pending</span></td>
      <td>RSVP and attend tomorrow 12–1:30 PM</td>
    </tr>
    <tr>
      <td>—</td>
      <td><strong>⚠️ FRAUD — "David Hersch" / Head of People / VP HR</strong></td>
      <td>thomsonreute.com (typosquat)</td>
      <td><span class="badge badge-red">AUTO-TRASHED</span></td>
      <td>Do NOT engage. Already reported to Thomson Reuters (Case #00318393).</td>
    </tr>
    <tr>
      <td><span class="pill pill-low">LOW</span></td>
      <td><strong>Ladders Resume Report — Stale Resume Flag</strong></td>
      <td>Ladders</td>
      <td><span class="badge badge-yellow">Action Needed</span></td>
      <td>Update Ladders resume (last updated 12/26/16)</td>
    </tr>
  </tbody>
</table>

<hr class="divider">

<!-- ═══════════════════════════════════════════════════════════
     SECTION 6 — FULL EMAIL REVIEW BY CATEGORY
════════════════════════════════════════════════════════════ -->
<div class="section-title navy">📂 Full Email Review by Category</div>
<p style="font-size:12px;color:#666;margin-bottom:12px;">Every email accounted for exactly once. Total: 50.</p>

<!-- SECURITY / RISK -->
<div class="section-title red" style="font-size:14px;">🔴 Security / Risk &nbsp;<span style="font-weight:400;font-size:12px;">(8 emails)</span></div>
<div class="card red">
  <h3>Fraudulent Recruiter — "David Hersch" / thomsonreute.com (4 emails AUTO-TRASHED)</h3>
  <div class="meta"><strong>Senders:</strong> david.hersch@thomsonreute.com &nbsp;|&nbsp; <strong>Auto-Trashed:</strong> Yes (4 messages)</div>
  <p style="margin-top:6px;">Ongoing thread spanning Aug 3–4. Domain <strong>thomsonreute.com</strong> is a typosquat of thomsonreuters.com. You flagged it yourself after three contacts warned you of the scam. All 4 inbound messages from this address have been auto-trashed. Your outbound replies (4 sent emails) remain in your sent folder for reference. Thomson Reuters support confirmed receipt of your report (Case #00318393).</p>
  <div class="phish-box">🚫 Auto-Trashed — Phishing: <em>thomsonreute.com typosquat domain impersonating Thomson Reuters in employment fraud scheme.</em></div>
  <div class="action-step"><strong>Action:</strong> No further engagement. Do not click any links in the trashed messages. You may want to warn your HR networking group.</div>
</div>
<div class="card red">
  <h3>Fake Cloud Admin — Subscription Renewal Phishing (1 email AUTO-TRASHED)</h3>
  <div class="meta"><strong>Sender:</strong> "Cloud Admin" &lt;jmfpmtdohpqlrh...@25ybm1.ub3okd.4pay2n.us&gt;</div>
  <div class="phish-box">🚫 Auto-Trashed — Phishing: <em>Spoofed "Cloud Admin" from gibberish domain, fake payment failure urgency — classic credential/billing phishing.</em></div>
  <div class="action-step"><strong>Action:</strong> Already handled. Do not open or click.</div>
</div>
<div class="card red">
  <h3>Bank of America — Fraud Claim (Account 2994) + Card Removed from Apple Pay</h3>
  <div class="meta"><strong>Sender:</strong> onlinebanking@ealerts.bankofamerica.com &nbsp;|&nbsp; <strong>2 emails</strong></div>
  <p style="margin-top:6px;">(1) Fraud claim received for account 2994 — Step 1 of 3. (2) Credit card 2994 deleted from Apple Pay. These are legitimate BofA alerts from the correct ealerts.bankofamerica.com domain.</p>
  <div class="action-step"><strong>Action:</strong> Log into BofA immediately. Track claim. Confirm no additional unauthorized charges. Verify new card 5690 is being shipped.</div>
</div>
<div class="card red">
  <h3>Reuters Support Response — Case #00318393</h3>
  <div class="meta"><strong>Sender:</strong> reuters.support@thomsonreuters.com (LEGITIMATE domain)</div>
  <p style="margin-top:6px;">Official Thomson Reuters support acknowledged your fraud report about the thomsonreute.com typosquat. Your complaint has been forwarded to their team.</p>
  <div class="action-step"><strong>Action:</strong> Keep for your records. No further action needed unless they respond with follow-up questions.</div>
</div>

<!-- JOB SEARCH -->
<div class="section-title green" style="font-size:14px;">🟢 Job Search &nbsp;<span style="font-weight:400;font-size:12px;">(11 emails)</span></div>
<div class="card green">
  <h3>LinkedIn Job Alerts (2 emails)</h3>
  <div class="meta"><strong>Senders:</strong> jobalerts-noreply@linkedin.com</div>
  <ul style="margin-top:6px;padding-left:18px;">
    <li><strong>Chief People &amp; Workplace Officer</strong> — Confidential, up to $600K/yr, actively recruiting ⭐ HIGH PRIORITY</li>
    <li><strong>Senior Human Resources Business Partner</strong> — Orca Security (cybersecurity firm)</li>
  </ul>
  <div class="action-step"><strong>Action:</strong> Apply to CPO role TODAY. Review Orca Security HRBP and apply if aligned.</div>
</div>
<div class="card green">
  <h3>Glassdoor Job Digests (4 emails)</h3>
  <div class="meta"><strong>Sender:</strong> noreply@glassdoor.com</div>
  <ul style="margin-top:6px;padding-left:18px;">
    <li>HR Manager at Meow Wolf + 8 Remote US jobs</li>
    <li>Relations Coordinator at Heard.Help + 5 NYC jobs</li>
    <li>Assoc. HR BP at 1-800-FLOWERS + 10 NYC jobs</li>
    <li>HR Manager at Novolex + 10 US jobs</li>
  </ul>
  <div class="action-step"><strong>Action:</strong> Scan all four digests; apply selectively based on level and compensation requirements.</div>
</div>
<div class="card green">
  <h3>Proactive Applications / Outreach (3 sent emails)</h3>
  <div class="meta"><strong>Sender:</strong> melissa (melissaw212@gmail.com — self)</div>
  <ul style="margin-top:6px;padding-left:18px;">
    <li><strong>"I've built the function you're describing"</strong> — Sent to Travis with resume attached (strong proactive outreach)</li>
    <li><strong>Re: [EXTERNAL] 15 years, one specific fit for your Corporate Affairs role</strong> — Follow-up to Susan Medina (Exec recruiter); applied online</li>
    <li><strong>Re: Head of People / VP of Human Resources</strong> — Multiple sent replies in the (fraudulent) thread; documented in Security section</li>
  </ul>
  <div class="action-step"><strong>Action:</strong> Follow up on Travis outreach in 3–5 business days if no response.</div>
</div>
<div class="card green">
  <h3>Inclusively — Job Recommendations (1 email)</h3>
  <div class="meta"><strong>Sender:</strong> contactus@inclusively.com</div>
  <p style="
