<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Daily Briefing – June 3, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 15px; line-height: 1.6; }
  .wrapper { max-width: 780px; margin: 0 auto; padding: 24px 16px; }

  /* Header */
  .header { background: linear-gradient(135deg, #0d1b3e 0%, #1a3a6e 100%); border-radius: 14px; padding: 36px 32px; margin-bottom: 24px; color: white; }
  .header h1 { font-size: 30px; font-weight: 700; letter-spacing: -0.5px; }
  .header .date { font-size: 15px; color: #a8c4f0; margin-top: 4px; }
  .header .tagline { font-size: 13px; color: #7aa8e0; margin-top: 8px; text-transform: uppercase; letter-spacing: 1px; }

  /* Section */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 18px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 14px; padding-bottom: 6px; border-bottom: 3px solid #dde3ef; color: #0d1b3e; }

  /* Cards */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; border-left: 5px solid; }
  .card-red    { background: #fff5f5; border-color: #e53e3e; }
  .card-yellow { background: #fffdf0; border-color: #d69e2e; }
  .card-blue   { background: #f0f6ff; border-color: #3182ce; }
  .card-green  { background: #f0fff4; border-color: #38a169; }
  .card-purple { background: #faf5ff; border-color: #805ad5; }
  .card-gray   { background: #f7f8fa; border-color: #a0aec0; }

  .card-label { display: inline-block; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; padding: 2px 8px; border-radius: 20px; margin-bottom: 6px; }
  .label-red    { background: #fed7d7; color: #c53030; }
  .label-yellow { background: #fef3c7; color: #92400e; }
  .label-blue   { background: #bee3f8; color: #2b6cb0; }
  .label-green  { background: #c6f6d5; color: #276749; }
  .label-purple { background: #e9d8fd; color: #553c9a; }
  .label-gray   { background: #e2e8f0; color: #4a5568; }

  .card-title { font-size: 15px; font-weight: 700; margin-bottom: 3px; color: #1a1a2e; }
  .card-meta  { font-size: 12px; color: #718096; margin-bottom: 6px; }
  .card-body  { font-size: 14px; color: #2d3748; margin-bottom: 8px; }
  .card-action { font-size: 13px; font-weight: 600; color: #2b6cb0; background: #ebf8ff; padding: 5px 10px; border-radius: 6px; display: inline-block; }
  .card-action-red    { color: #c53030; background: #fff5f5; }
  .card-action-green  { color: #276749; background: #f0fff4; }
  .card-action-purple { color: #553c9a; background: #faf5ff; }
  .card-action-yellow { color: #92400e; background: #fffdf0; }

  /* Executive Summary */
  .exec-box { background: linear-gradient(135deg, #1a3a6e 0%, #2a5298 100%); border-radius: 12px; padding: 22px 26px; margin-bottom: 28px; color: white; }
  .exec-box h2 { font-size: 16px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 14px; color: #a8c4f0; }
  .exec-box ul { list-style: none; padding: 0; }
  .exec-box ul li { padding: 6px 0; padding-left: 22px; position: relative; font-size: 14px; color: #e8f0fe; border-bottom: 1px solid rgba(255,255,255,0.1); }
  .exec-box ul li:last-child { border-bottom: none; }
  .exec-box ul li::before { content: "▶"; position: absolute; left: 0; font-size: 10px; top: 9px; color: #63b3ed; }

  /* Schedule */
  .schedule-row { display: flex; gap: 12px; align-items: flex-start; padding: 12px 16px; background: white; border-radius: 8px; margin-bottom: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.07); }
  .schedule-time { font-size: 13px; font-weight: 700; color: #3182ce; min-width: 90px; padding-top: 2px; }
  .schedule-content { flex: 1; }
  .schedule-title { font-size: 14px; font-weight: 700; color: #1a1a2e; }
  .schedule-detail { font-size: 12px; color: #718096; margin-top: 2px; }
  .schedule-badge { font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 20px; display: inline-block; margin-top: 4px; }
  .badge-declined  { background: #fed7d7; color: #c53030; }
  .badge-confirmed { background: #c6f6d5; color: #276749; }
  .badge-pending   { background: #fef3c7; color: #92400e; }
  .badge-accepted  { background: #c6f6d5; color: #276749; }

  /* Table */
  table { width: 100%; border-collapse: collapse; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
  thead { background: #0d1b3e; color: white; }
  thead th { padding: 12px 14px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
  tbody tr { border-bottom: 1px solid #edf2f7; }
  tbody tr:last-child { border-bottom: none; }
  tbody tr:hover { background: #f7f9fc; }
  tbody td { padding: 11px 14px; font-size: 13px; vertical-align: top; }
  .priority-high   { color: #c53030; font-weight: 700; }
  .priority-medium { color: #d69e2e; font-weight: 700; }
  .priority-low    { color: #718096; font-weight: 600; }

  /* Top 3 */
  .top3 { background: linear-gradient(135deg, #0d1b3e 0%, #1a3a6e 100%); border-radius: 12px; padding: 24px 28px; color: white; }
  .top3 h2 { font-size: 16px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 16px; color: #a8c4f0; }
  .top3-item { display: flex; align-items: flex-start; gap: 14px; padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.1); }
  .top3-item:last-child { border-bottom: none; }
  .top3-num { background: #3182ce; color: white; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 15px; flex-shrink: 0; }
  .top3-text strong { display: block; font-size: 15px; color: #e8f0fe; }
  .top3-text span { font-size: 13px; color: #a8c4f0; }

  /* Conflict badge */
  .conflict-note { font-size: 12px; background: #fed7d7; color: #c53030; padding: 3px 8px; border-radius: 6px; display: inline-block; margin-top: 4px; font-weight: 600; }

  /* Divider */
  .divider { height: 1px; background: #dde3ef; margin: 6px 0 14px 0; }

  a { color: #3182ce; text-decoration: none; }
  a:hover { text-decoration: underline; }
</style>
</head>
<body>
<div class="wrapper">

  <!-- ═══════════════════════════════════════════ HEADER -->
  <div class="header">
    <div class="tagline">Executive Daily Briefing</div>
    <h1>Good morning, Melissa ☀️</h1>
    <div class="date">Wednesday, June 3, 2026 &nbsp;·&nbsp; Prepared by your Chief of Staff</div>
  </div>

  <!-- ═══════════════════════════════════════════ EXECUTIVE SUMMARY -->
  <div class="exec-box">
    <h2>📋 Executive Summary</h2>
    <ul>
      <li><strong>Security alert:</strong> Your LinkedIn password was reset tonight — confirm this was you and check for unauthorized access. Two scam/phishing emails also arrived today and should be deleted.</li>
      <li><strong>Job search is active:</strong> Two notable LinkedIn leads landed in your inbox today — a Chief People Officer role (up to $350K) and a Senior Director HRBP (AI-Native). A 15-minute call with Netta Jenkins is confirmed for June 9th, and an open HR networking session is tomorrow (June 4) at noon — RSVP pending.</li>
      <li><strong>Calendar heads-up:</strong> Tomorrow is packed — you have a declined Executive Roundtable at 9 AM, a Dr. Husk appointment at 10:30 AM, and the HR Networking open office hours at noon that still needs your RSVP. Jackie's birthday is Saturday and your State Farm bill is due Sunday.</li>
    </ul>
  </div>

  <!-- ═══════════════════════════════════════════ SECTION 1: ACTION REQUIRED -->
  <div class="section">
    <div class="section-title">🔴 Section 1 — Action Required</div>

    <div class="card card-red">
      <span class="card-label label-red">🔒 Security Alert</span>
      <div class="card-title">LinkedIn Password Was Reset — Confirm It Was You</div>
      <div class="card-meta">From: LinkedIn Security &lt;security-noreply@linkedin.com&gt; · 9:17 PM today</div>
      <div class="card-body">LinkedIn sent both a PIN (606210) and a password-reset confirmation email within 2 minutes of each other this evening. If you did not initiate this, your account may be compromised.</div>
      <span class="card-action card-action-red">→ Log into LinkedIn now, review recent activity, and enable 2-factor authentication if not already active.</span>
    </div>

    <div class="card card-red">
      <span class="card-label label-red">⚠️ Phishing / Scam</span>
      <div class="card-title">Fake "Cloud Account Locked" Email — Do Not Click</div>
      <div class="card-meta">From: "Payment_Declined" &lt;xbtcsupportmd@wcknlkzajfzzlhmducymgdwi.com&gt; · 4:30 PM today</div>
      <div class="card-body">This email claims your cloud subscription expired and your photos/videos will be deleted. The sender domain is clearly fraudulent. This is a phishing attempt designed to steal payment credentials.</div>
      <span class="card-action card-action-red">→ Delete immediately. Do not click any links. Mark as spam.</span>
    </div>

    <div class="card card-red">
      <span class="card-label label-red">⚠️ Scam / Spam</span>
      <div class="card-title">Fake Casino Payment Email — Do Not Engage</div>
      <div class="card-meta">From: Casino_Yabby &lt;tfvrniyohli@fknm.iwebcsruiikul.us&gt; · 5:11 PM today</div>
      <div class="card-body">Claims a payment of $13,963.99 is "ready for your confirmation." Classic advance-fee / prize scam. Sender domain is fake. Not in inbox but still present in your account.</div>
      <span class="card-action card-action-red">→ Delete and block sender. No action needed beyond that.</span>
    </div>

    <div class="card card-yellow">
      <span class="card-label label-yellow">📅 RSVP Needed</span>
      <div class="card-title">HR Networking &amp; Job Search — Open Office Hours (Tomorrow)</div>
      <div class="card-meta">Calendar Event · Thursday, June 4 · 12:00–1:00 PM · Zoom</div>
      <div class="card-body">You have not yet responded to this event. It's tomorrow at noon and includes a large group of HR peers. Note: organizer requests no AI notetaking tools.</div>
      <span class="card-action card-action-yellow">→ Decide and RSVP today. <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1">Zoom link here.</a></span>
    </div>

    <div class="card card-yellow">
      <span class="card-label label-yellow">💰 Bill Reminder</span>
      <div class="card-title">State Farm Bill Due — Sunday, June 7</div>
      <div class="card-meta">Calendar Reminder · All Day · June 7, 2026</div>
      <div class="card-body">You have a State Farm payment flagged on your calendar for Sunday. Make sure the payment is scheduled or set up before the weekend.</div>
      <span class="card-action card-action-yellow">→ Confirm payment is scheduled or pay online before Sunday.</span>
    </div>

    <div class="card card-yellow">
      <span class="card-label label-yellow">🎂 Personal Reminder</span>
      <div class="card-title">Jackie's Birthday — Saturday, June 6</div>
      <div class="card-meta">Calendar Event · All Day · June
