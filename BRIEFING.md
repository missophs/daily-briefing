<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Daily Briefing – Wednesday, June 3, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 15px; line-height: 1.6; }
  .wrapper { max-width: 860px; margin: 0 auto; padding: 0 0 40px 0; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #0d1b3e 0%, #1a3a6e 100%); color: #fff; padding: 36px 40px 28px 40px; border-radius: 0 0 18px 18px; margin-bottom: 28px; }
  .header .greeting { font-size: 2.1em; font-weight: 800; letter-spacing: -0.5px; }
  .header .subline { font-size: 1.05em; opacity: 0.75; margin-top: 6px; }
  .header .badge { display: inline-block; background: rgba(255,255,255,0.15); border-radius: 20px; padding: 4px 16px; font-size: 0.82em; margin-top: 12px; letter-spacing: 0.5px; }

  /* SECTION TITLES */
  .section-title { font-size: 1.18em; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; margin: 30px 0 12px 0; padding-left: 4px; color: #0d1b3e; border-left: 5px solid #1a3a6e; padding-left: 12px; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; border-left: 5px solid transparent; }
  .card-red    { background: #fff5f5; border-color: #e53e3e; }
  .card-yellow { background: #fffbea; border-color: #d69e2e; }
  .card-blue   { background: #ebf8ff; border-color: #3182ce; }
  .card-green  { background: #f0fff4; border-color: #38a169; }
  .card-purple { background: #faf5ff; border-color: #805ad5; }
  .card-gray   { background: #f7f8fa; border-color: #a0aec0; }
  .card-orange { background: #fffaf0; border-color: #dd6b20; }

  .card .card-label { font-size: 0.72em; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 4px; }
  .label-red    { color: #c53030; }
  .label-yellow { color: #b7791f; }
  .label-blue   { color: #2b6cb0; }
  .label-green  { color: #276749; }
  .label-purple { color: #553c9a; }
  .label-gray   { color: #718096; }
  .label-orange { color: #c05621; }

  .card .card-title { font-size: 1.03em; font-weight: 700; margin-bottom: 3px; }
  .card .card-meta  { font-size: 0.83em; color: #555; margin-bottom: 6px; }
  .card .card-body  { font-size: 0.92em; color: #333; margin-bottom: 8px; }
  .card .card-action { font-size: 0.85em; font-weight: 700; }
  .action-red    { color: #c53030; }
  .action-yellow { color: #b7791f; }
  .action-blue   { color: #2b6cb0; }
  .action-green  { color: #276749; }
  .action-purple { color: #553c9a; }
  .action-gray   { color: #718096; }
  .action-orange { color: #c05621; }

  /* EXEC SUMMARY */
  .exec-summary { background: linear-gradient(135deg, #1a3a6e 0%, #2a5298 100%); color: #fff; border-radius: 12px; padding: 22px 28px; margin-bottom: 28px; }
  .exec-summary h2 { font-size: 1.1em; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 14px; opacity: 0.85; }
  .exec-summary ul { list-style: none; padding: 0; }
  .exec-summary ul li { padding: 6px 0; padding-left: 24px; position: relative; font-size: 0.97em; }
  .exec-summary ul li::before { content: "▶"; position: absolute; left: 0; font-size: 0.7em; top: 9px; opacity: 0.7; }

  /* CALENDAR TABLE */
  .cal-table { width: 100%; border-collapse: collapse; margin-bottom: 8px; }
  .cal-table th { background: #1a3a6e; color: #fff; padding: 9px 12px; text-align: left; font-size: 0.82em; text-transform: uppercase; letter-spacing: 0.8px; }
  .cal-table td { padding: 10px 12px; border-bottom: 1px solid #e2e8f0; font-size: 0.88em; vertical-align: top; }
  .cal-table tr:nth-child(even) td { background: #f7f9fc; }
  .cal-table tr:last-child td { border-bottom: none; }
  .status-confirmed { color: #276749; font-weight: 700; }
  .status-declined  { color: #c53030; font-weight: 700; }
  .status-pending   { color: #b7791f; font-weight: 700; }
  .status-accepted  { color: #2b6cb0; font-weight: 700; }
  .conflict-flag    { background: #fff5f5; color: #c53030; font-weight: 700; padding: 2px 8px; border-radius: 6px; font-size: 0.8em; }

  /* ACTION TABLE */
  .action-table { width: 100%; border-collapse: collapse; margin-bottom: 8px; }
  .action-table th { background: #0d1b3e; color: #fff; padding: 9px 12px; text-align: left; font-size: 0.82em; text-transform: uppercase; letter-spacing: 0.8px; }
  .action-table td { padding: 10px 12px; border-bottom: 1px solid #e2e8f0; font-size: 0.88em; vertical-align: top; }
  .action-table tr:nth-child(even) td { background: #f7f9fc; }
  .action-table tr:last-child td { border-bottom: none; }
  .pri-high   { color: #c53030; font-weight: 700; }
  .pri-medium { color: #b7791f; font-weight: 700; }
  .pri-low    { color: #718096; font-weight: 700; }

  /* TOP 3 */
  .top3 { background: linear-gradient(135deg, #0d1b3e 0%, #1a3a6e 100%); color: #fff; border-radius: 12px; padding: 24px 28px; margin-top: 30px; }
  .top3 h2 { font-size: 1.1em; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 16px; }
  .top3-item { display: flex; align-items: flex-start; margin-bottom: 14px; }
  .top3-num { font-size: 1.8em; font-weight: 900; color: rgba(255,255,255,0.25); margin-right: 14px; line-height: 1; min-width: 30px; }
  .top3-text { font-size: 0.97em; }
  .top3-text strong { display: block; font-size: 1.05em; margin-bottom: 2px; }

  /* PROMO GROUP */
  .promo-group { background: #f7f8fa; border-radius: 10px; padding: 14px 18px; margin-bottom: 12px; border: 1px solid #e2e8f0; }
  .promo-group .promo-title { font-weight: 700; font-size: 0.92em; color: #0d1b3e; margin-bottom: 8px; }
  .promo-row { display: flex; justify-content: space-between; align-items: center; padding: 5px 0; border-bottom: 1px solid #edf2f7; font-size: 0.86em; }
  .promo-row:last-child { border-bottom: none; }
  .promo-sender { color: #555; min-width: 120px; }
  .promo-subject { color: #1a1a2e; flex: 1; padding: 0 10px; }
  .tag { font-size: 0.76em; font-weight: 700; padding: 2px 8px; border-radius: 6px; white-space: nowrap; }
  .tag-delete  { background: #fed7d7; color: #c53030; }
  .tag-keep    { background: #c6f6d5; color: #276749; }
  .tag-useful  { background: #bee3f8; color: #2b6cb0; }
  .tag-expiring { background: #fefcbf; color: #b7791f; }
  .tag-suspicious { background: #fbd38d; color: #7b341e; }
  .tag-restore { background: #e9d8fd; color: #553c9a; }
  .tag-review  { background: #bee3f8; color: #2b6cb0; }

  /* SECTION END SUMMARY */
  .section-end { background: #edf2f7; border-radius: 8px; padding: 10px 16px; margin-top: 4px; margin-bottom: 20px; font-size: 0.86em; color: #4a5568; }
  .section-end strong { color: #0d1b3e; }

  /* DIVIDER */
  .divider { border: none; border-top: 2px solid #e2e8f0; margin: 24px 0; }

  /* LINK */
  a { color: #2b6cb0; text-decoration: none; }
  a:hover { text-decoration: underline; }

  @media (max-width: 600px) {
    .header { padding: 22px 16px 18px 16px; }
    .header .greeting { font-size: 1.5em; }
    .wrapper { padding: 0 0 24px 0; }
    .promo-row { flex-direction: column; align-items: flex-start; gap: 3px; }
    .cal-table, .action-table { font-size: 0.8em; }
  }
</style>
</head>
<body>
<div class="wrapper">

  <!-- ==================== HEADER ==================== -->
  <div class="header">
    <div class="greeting">Good morning, Melissa ☀️</div>
    <div class="subline">Wednesday, June 3, 2026 &nbsp;·&nbsp; Your Executive Chief of Staff Briefing</div>
    <div class="badge">📋 Daily Intelligence Report</div>
  </div>

  <!-- ==================== EXECUTIVE SUMMARY ==================== -->
  <div style="padding: 0 20px;">
  <div class="exec-summary">
    <h2>⚡ Executive Summary</h2>
    <ul>
      <li><strong>Security Alert:</strong> Your LinkedIn password was reset today — verify this was you and check for any unauthorized account activity immediately.</li>
      <li><strong>Job Search:</strong> Two strong LinkedIn job leads landed today (Chief People Officer at Conexus up to $350K; Sr. Director HRBP AI-Native at RemoteHunter) — review and apply if aligned. You also have a confirmed 15-min consultation with Netta Jenkins on June 9.</li>
      <li><strong>This Week:</strong> Dr. Husk appointment tomorrow (June 4, 10:30 AM), Jackie's birthday June 6, State Farm bill due June 7, eye appointment June 8 — plus two HR networking sessions need your RSVP.</li>
    </ul>
  </div>

  <!-- ==================== SECTION 1: ACTION REQUIRED ==================== -->
  <div class="section-title">🔴 Section 1 — Action Required</div>

  <div class="card card-red">
    <div class="card-label label-red">🔐 Security — Act Now</div>
    <div class="card-title">LinkedIn Password Reset Confirmation</div>
    <div class="card-meta">From: LinkedIn Security &lt;security-noreply@linkedin.com&gt; · Jun 3, 9:17 PM UTC</div>
    <div class="card-body">Your LinkedIn password was successfully reset today. A PIN (606210) was also sent moments earlier for verification. If you did not initiate this, your account may be compromised.</div>
    <div class="card-action action-red">✅ Next Step: Log in to LinkedIn immediately, confirm password change was yours, review recent sign-in activity, and enable two-factor authentication if not already active.</div>
  </div>

  <div class="card card-yellow">
    <div class="card-label label-yellow">📅 RSVP Needed — Tomorrow</div>
    <div class="card-title">HR Networking &amp; Job Search: Open Office Hours (Zoom)</div>
    <div class="card-meta">Calendar Event · Thu Jun 4, 12:00–1:00 PM · Status: Needs Action</div>
    <div class="card-body">You have not yet responded to this networking session tomorrow. Large group call — 170+ attendees. Note: AI notetaking tools are asked to be turned off. Zoom link available.</div>
    <div class="card-action action-yellow">✅ Next Step: Decide if attending — RSVP Yes or No. <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1">Join Zoom</a></div>
  </div>

  <div class="card card-yellow">
    <div class="card-label label-yellow">📅 RSVP Needed — Next Week</div>
    <div class="card-title">HR Networking &amp; Job Search Group (Zoom 2)</div>
    <div class="card-meta">Calendar Event · Wed Jun 10, 12:00–1:30 PM · Status: Needs Action</div>
    <div class="card-body">Another large HR networking group session on June 10 — also no response yet. Conflicts with your "Network" personal block and Melissa x Meg drinks (1–2 PM) that same day.</div>
    <div class="card-action action-yellow">✅ Next Step: RSVP and check schedule conflict with
