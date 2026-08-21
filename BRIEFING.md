<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa — Friday, August 21, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* Header */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px; }
  .header-left h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.3px; }
  .header-left .subtitle { font-size: 14px; color: #a8b8d8; margin-top: 4px; }
  .header-stats { display: flex; gap: 20px; flex-wrap: wrap; }
  .stat-pill { background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.18); border-radius: 30px; padding: 8px 18px; text-align: center; }
  .stat-pill .num { font-size: 22px; font-weight: 700; color: #e0e8ff; }
  .stat-pill .lbl { font-size: 11px; color: #a8b8d8; text-transform: uppercase; letter-spacing: 0.8px; }

  /* Section headers */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 14px; display: flex; align-items: center; gap: 8px; padding-bottom: 8px; border-bottom: 2px solid currentColor; }

  /* Color themes */
  .red    { color: #c0392b; border-color: #c0392b; }
  .yellow { color: #b7860b; border-color: #b7860b; }
  .blue   { color: #1565c0; border-color: #1565c0; }
  .green  { color: #1a7a3b; border-color: #1a7a3b; }
  .purple { color: #6a1b9a; border-color: #6a1b9a; }
  .gray   { color: #5a5a5a; border-color: #5a5a5a; }
  .orange { color: #e65100; border-color: #e65100; }

  /* Cards */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; border-left: 5px solid; }
  .card-red    { background: #fff5f5; border-color: #e53935; }
  .card-yellow { background: #fffde7; border-color: #f9a825; }
  .card-blue   { background: #e8f0fe; border-color: #1565c0; }
  .card-green  { background: #f0fdf4; border-color: #2e7d32; }
  .card-purple { background: #f3e5f5; border-color: #7b1fa2; }
  .card-gray   { background: #f5f5f5; border-color: #9e9e9e; }
  .card-orange { background: #fff3e0; border-color: #e65100; }
  .card h3 { font-size: 14px; font-weight: 700; margin-bottom: 6px; }
  .card .meta { font-size: 12px; color: #555; margin-bottom: 6px; }
  .card p { font-size: 13px; }
  .card .label { display: inline-block; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; padding: 2px 8px; border-radius: 12px; margin-bottom: 8px; }
  .label-red    { background: #fde8e8; color: #b71c1c; }
  .label-yellow { background: #fff9c4; color: #7a5800; }
  .label-blue   { background: #dce8ff; color: #0d47a1; }
  .label-green  { background: #d4edda; color: #145a23; }
  .label-purple { background: #ede7f6; color: #4a148c; }
  .label-gray   { background: #ececec; color: #444; }
  .label-orange { background: #ffe0b2; color: #bf360c; }

  /* Tables */
  table { width: 100%; border-collapse: collapse; font-size: 13px; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }
  th { background: #1a1a2e; color: #e0e8ff; padding: 10px 12px; text-align: left; font-size: 11px; text-transform: uppercase; letter-spacing: 0.7px; font-weight: 600; }
  td { padding: 9px 12px; border-bottom: 1px solid #eee; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #fafafa; }
  tr:hover td { background: #f0f4ff; }

  /* Triage table status badges */
  .status-badge { display: inline-block; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 10px; white-space: nowrap; }
  .badge-inbox    { background: #dce8ff; color: #0d47a1; }
  .badge-rescued  { background: #d4edda; color: #145a23; }
  .badge-trash    { background: #ececec; color: #444; }
  .badge-autotrash{ background: #fde8e8; color: #b71c1c; }

  /* Summary bullets */
  .exec-summary { background: #1a1a2e; color: #e8efff; border-radius: 12px; padding: 24px 28px; margin-bottom: 24px; }
  .exec-summary h2 { font-size: 15px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #a8b8d8; margin-bottom: 14px; }
  .exec-summary ul { list-style: none; }
  .exec-summary ul li { padding: 8px 0; border-bottom: 1px solid rgba(255,255,255,0.08); display: flex; gap: 10px; align-items: flex-start; }
  .exec-summary ul li:last-child { border-bottom: none; }
  .exec-summary .bullet-icon { font-size: 18px; flex-shrink: 0; }

  /* Calendar day blocks */
  .cal-day { background: #fff; border-radius: 10px; margin-bottom: 14px; box-shadow: 0 1px 4px rgba(0,0,0,0.06); overflow: hidden; }
  .cal-day-header { background: #1565c0; color: #fff; padding: 8px 16px; font-weight: 700; font-size: 13px; letter-spacing: 0.5px; }
  .cal-day-header.today { background: #0d47a1; }
  .cal-event { padding: 12px 16px; border-bottom: 1px solid #eef0f4; display: grid; grid-template-columns: 120px 1fr; gap: 12px; align-items: start; }
  .cal-event:last-child { border-bottom: none; }
  .cal-event .time { font-weight: 700; font-size: 12px; color: #1565c0; }
  .cal-event .event-name { font-weight: 600; font-size: 13px; }
  .cal-event .event-detail { font-size: 12px; color: #555; margin-top: 3px; }
  .cal-event .rsvp { display: inline-block; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 8px; margin-left: 6px; }
  .rsvp-accepted  { background: #d4edda; color: #145a23; }
  .rsvp-confirmed { background: #dce8ff; color: #0d47a1; }
  .rsvp-declined  { background: #fde8e8; color: #b71c1c; }
  .rsvp-pending   { background: #fff9c4; color: #7a5800; }
  .cal-all-day { padding: 10px 16px; border-bottom: 1px solid #eef0f4; background: #f8fbff; }
  .cal-all-day .event-name { font-weight: 600; font-size: 13px; color: #444; }
  .cal-all-day .event-detail { font-size: 12px; color: #777; }

  /* Priority pills */
  .priority-high   { background: #fde8e8; color: #b71c1c; padding: 2px 8px; border-radius: 10px; font-size: 10px; font-weight: 700; }
  .priority-medium { background: #fff9c4; color: #7a5800; padding: 2px 8px; border-radius: 10px; font-size: 10px; font-weight: 700; }
  .priority-low    { background: #ececec; color: #444; padding: 2px 8px; border-radius: 10px; font-size: 10px; font-weight: 700; }

  /* Fit tags */
  .fit-high   { background: #d4edda; color: #145a23; padding: 2px 8px; border-radius: 10px; font-size: 10px; font-weight: 700; }
  .fit-medium { background: #dce8ff; color: #0d47a1; padding: 2px 8px; border-radius: 10px; font-size: 10px; font-weight: 700; }
  .fit-low    { background: #ececec; color: #444; padding: 2px 8px; border-radius: 10px; font-size: 10px; font-weight: 700; }

  /* Dashboard grid */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; margin-bottom: 24px; }
  .dash-tile { background: #fff; border-radius: 10px; padding: 16px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); border-top: 4px solid; }
  .dash-tile h4 { font-size: 11px; text-transform: uppercase; letter-spacing: 0.8px; color: #777; margin-bottom: 8px; }
  .dash-tile .dash-val { font-size: 26px; font-weight: 800; }
  .dash-tile .dash-sub { font-size: 12px; color: #555; margin-top: 4px; }
  .dt-red    { border-color: #e53935; } .dt-red .dash-val    { color: #c0392b; }
  .dt-yellow { border-color: #f9a825; } .dt-yellow .dash-val { color: #b7860b; }
  .dt-blue   { border-color: #1565c0; } .dt-blue .dash-val   { color: #1565c0; }
  .dt-green  { border-color: #2e7d32; } .dt-green .dash-val  { color: #1a7a3b; }
  .dt-purple { border-color: #7b1fa2; } .dt-purple .dash-val { color: #6a1b9a; }
  .dt-gray   { border-color: #9e9e9e; } .dt-gray .dash-val   { color: #5a5a5a; }

  /* Top priorities */
  .top3 { counter-reset: priorities; }
  .top3-item { background: #fff; border-radius: 10px; padding: 18px 20px 18px 60px; margin-bottom: 12px; box-shadow: 0 1px 5px rgba(0,0,0,0.08); position: relative; border-left: 5px solid; }
  .top3-item:nth-child(1) { border-color: #e53935; }
  .top3-item:nth-child(2) { border-color: #f9a825; }
  .top3-item:nth-child(3) { border-color: #2e7d32; }
  .top3-num { position: absolute; left: 16px; top: 50%; transform: translateY(-50%); font-size: 28px; font-weight: 900; color: #ddd; }
  .top3-item h3 { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
  .top3-item p { font-size: 13px; color: #444; }

  /* Misc */
  .note { font-size: 12px; color: #888; font-style: italic; margin-top: 8px; }
  .group-header { background: #eef0f4; padding: 7px 14px; font-weight: 700; font-size: 12px; color: #333; border-radius: 6px; margin: 10px 0 6px 0; }
  .tag { display: inline-block; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 8px; margin: 2px 2px 2px 0; }
  .tag-delete  { background: #fde8e8; color: #b71c1c; }
  .tag-review  { background: #fff9c4; color: #7a5800; }
  .tag-keep    { background: #d4edda; color: #145a23; }
  .tag-restore { background: #dce8ff; color: #0d47a1; }
  .tag-unsub   { background: #f3e5f5; color: #4a148c; }
  .tag-ignore  { background: #ececec; color: #444; }
  .phish-badge { background: #fde8e8; color: #b71c1c; border: 1px solid #e53935; padding: 2px 8px; border-radius: 8px; font-size: 10px; font-weight: 700; }
  .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
  @media(max-width:680px){ .two-col { grid-template-columns: 1fr; } .header { flex-direction:column; } .cal-event { grid-template-columns: 1fr; } }
  .divider { height: 1px; background: #e2e6ea; margin: 20px 0; }
  .total-row td { font-weight: 700; background: #1a1a2e !important; color: #e0e8ff; }
  .conflict-warn { color: #e65100; font-size: 11px; font-weight: 700; }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════
     HEADER
═══════════════════════════════════════════════ -->
<div class="header">
  <div class="header-left">
    <div style="font-size:13px;color:#a8b8d8;text-transform:uppercase;letter-spacing:1px;margin-bottom:4px;">Executive Briefing</div>
    <h1>Good morning, Melissa ☀️</h1>
    <div class="subtitle">Friday, August 21, 2026 &nbsp;·&nbsp; Prepared by your Executive Chief of Staff</div>
  </div>
  <div class="header-stats">
    <div class="stat-pill"><div class="num">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="stat-pill"><div class="num">15</div><div class="lbl">Calendar Events</div></div>
    <div class="stat-pill"><div class="num">2</div><div class="lbl">Meetings Today</div></div>
    <div class="stat-pill"><div class="num">7</div><div class="lbl">Action Items</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 0 — EMAIL TRIAGE QUICK LIST
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title blue">📋 Email Triage Quick List</div>
  <table>
    <thead>
      <tr>
        <th style="width:130px;">Status</th>
        <th style="width:200px;">From</th>
        <th>Subject</th>
        <th>Summary</th>
      </tr>
    </thead>
    <tbody>
      <!-- INBOX EMAILS (individual rows) -->
      <tr>
        <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
        <td>Match</td>
        <td>You've had a profile view from Jp</td>
        <td>Dating app — Jp, 67, Yonkers viewed your profile.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
        <td>LinkedIn</td>
        <td>Glenn accepted your invitation</td>
        <td>New connection accepted — Glenn Lesko. Explore network.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>Head of Human Resources — Global Energy Alliance</td>
        <td>New job alert — strong potential fit. Review.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
        <td>LinkedIn</td>
        <td>HR Executive roles — HireTalent</td>
        <td>Top company hiring HR Executives. Review listing.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
        <td>Match</td>
        <td>Unread message — see what they said</td>
        <td>Dating app — unread message waiting. Check app.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
        <td>OkCupid</td>
        <td>Someone likes you</td>
        <td>Dating app — someone liked your profile.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
        <td>LinkedIn (Shoan Shinde)</td>
        <td>Melissa A, I'd like to connect</td>
        <td>CMO from TurboHire wants to connect. Pending response.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>VP of People (HR) — K Health</td>
        <td>Job alert — VP-level HR role at K Health. Strong fit.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>LinkedIn headline</td>
        <td>Self-note: formula for LinkedIn headline optimization.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>VP Human Resources | Lerryn House | LinkedIn</td>
        <td>Self-saved LinkedIn job link — VP HR at Lerryn House.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>HR Director | Iceberg | LinkedIn</td>
        <td>Self-saved LinkedIn job link — HR Director at Iceberg.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>Seth Rogers | LinkedIn</td>
        <td>Self-saved LinkedIn profile link — contact to reach.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>Mario Linale | LinkedIn</td>
        <td>Self-saved LinkedIn profile link — contact to reach.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>Senior HR Business Partner | Maven Clinic | LinkedIn</td>
        <td>Self-saved LinkedIn job link — Sr. HRBP at Maven Clinic.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>HR Director (Remote) — Maximus</td>
        <td>Job alert — remote HR Director role at Maximus. In inbox.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
        <td>Archer / HackaJob</td>
        <td>Your dream job is a few clicks away</td>
        <td>Profile started on HackaJob — complete to activate search.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>Hackajob</td>
        <td>Self-note about Hackajob platform — likely reminder.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
        <td>Match</td>
        <td>Johnny likes you</td>
        <td>Dating app — Johnny liked your profile.</td>
      </tr>
      <!-- NOT IN INBOX, NOT IN TRASH, NOT AUTO-TRASHED (individual rows for high-value) -->
      <tr>
        <td><span class="status-badge badge-inbox">📨 NOT IN INBOX</span></td>
        <td>Zoom (Outskill)</td>
        <td>Your seat is reserved — Claude 101 Workshop</td>
        <td>Zoom confirmation for Claude 101 Workshop. Check date/time.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📨 NOT IN INBOX</span></td>
        <td>Outskill</td>
        <td>You're in. Here's what we built for you.</td>
        <td>Workshop registration confirmed. Rebuilt around Claude's new capabilities.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📨 NOT IN INBOX</span></td>
        <td>Slack</td>
        <td>Set up Slack across your devices</td>
        <td>New Slack workspace — download apps for desktop/mobile.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📨 NOT IN INBOX</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>Head of HR — Global Energy Alliance (duplicate)</td>
        <td>Earlier alert for same role — already seen in inbox version.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📨 NOT IN INBOX</span></td>
        <td>LinkedIn</td>
        <td>Jules S. Ehrenberg shares thoughts on LinkedIn</td>
        <td>Payroll Manager posting in LinkedIn network feed. Low priority.</td>
      </tr>
      <tr>
        <td><span class="status-badge badge-inbox">📨 NOT IN INBOX</span></td>
        <td>Old Navy</td>
        <td>Need a denim update? Get yours from $22</td>
        <td>Retail promotional email. Not in inbox or trash.</td>
      </tr>
      <!-- TRASH SUMMARY ROWS -->
      <tr style="background:#fde8e8;">
        <td><span class="status-badge badge-autotrash">🛡 AUTO-TRASHED</span></td>
        <td colspan="3"><strong>8 emails auto-trashed (phishing/spam)</strong> — Cloud storage scams, spoofed CashApp, spoofed SiriusXM, spoofed Gmail, adult spam, and gibberish-domain emails. See Security / Risk &amp; Trash Review sections below.</td>
      </tr>
      <tr style="background:#f5f5f5;">
        <td><span class="status-badge badge-trash">🗑 TRASH (manual)</span></td>
        <td colspan="3"><strong>19 emails in Trash</strong> — Newsletters, retail promos, job digests, gambling, political. See Trash Review section below.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 2 — EXECUTIVE SUMMARY
═══════════════════════════════════════════════ -->
<div class="exec-summary">
  <h2>⚡ Executive Summary</h2>
  <ul>
    <li>
      <span class="bullet-icon">🔴</span>
      <div><strong>Security Risk:</strong> 8 phishing/spam emails were auto-trashed before reaching your inbox — including spoofed Gmail, CashApp, iCloud, SiriusXM, and two cloud-storage account-deletion threats. No action needed on these, but your inbox is an active phishing target. Do not respond to any account-locked messages. All legitimate threats have been neutralized.</div>
    </li>
    <li>
      <span class="bullet-icon">🟢</span>
      <div><strong>Job Search:</strong> Multiple strong leads require attention today — including a VP of People role at K Health, Head of HR at Global Energy Alliance, and VP HR at Lerryn House. You also have self-saved profiles (Seth Rogers, Mario Linale) that suggest active outreach in progress. Complete your HackaJob profile and finalize your LinkedIn headline to maximize visibility.</div>
    </li>
    <li>
      <span class="bullet-icon">🔵</span>
      <div><strong>Calendar / Deadlines:</strong> Two meetings today — Tina/Melissa connect (10:30 AM via Teams) and Zoom with Dee Dee (12:00 PM). Looking ahead: Verizon Fios bill due Sunday Aug 23, hair appointment Monday Aug 24 at UMI Salon, and a recruiter call Tuesday Aug 25. RSVP still needed for HR Networking Group on Aug 26 and Open Office Hours on Aug 27.</div>
    </li>
  </ul>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 3 — ACTION REQUIRED
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title red">🚨 Action Required</div>

  <div class="card card-red">
    <span class="label label-red">🔴 URGENT — SECURITY</span>
    <h3>Do NOT engage with any "account locked" or "storage deleted" emails</h3>
    <div class="meta">Source: 8 auto-trashed phishing emails (multiple senders)</div>
    <p><strong>Why it matters:</strong> Multiple credential-harvesting attempts spoofing Gmail, iCloud, CashApp, and SiriusXM are actively targeting your address. None are legitimate.</p>
    <p><strong>Next step:</strong> No action needed — all were auto-trashed. Continue ignoring any similar messages. Consider enabling Gmail Advanced Protection if not already active.</p>
    <div class="meta" style="margin-top:6px;">Due: Ongoing</div>
  </div>

  <div class="card card-yellow">
    <span class="label label-yellow">🟡 DEADLINE — BILLING</span>
    <h3>Verizon Fios Bill Due — Sunday, August 23</h3>
    <div class="meta">Source: Google Calendar</div>
    <p><strong>Why it matters:</strong> Bill reminder is two days away. Risk of service interruption if missed.</p>
    <p><strong>Next step:</strong> Log in to Verizon and pay or confirm auto-pay is active.</p>
    <div class="meta" style="margin-top:6px;">Due: Sunday, August 23</div>
  </div>

  <div class="card card-blue">
    <span class="label label-blue">🔵 TODAY — MEETING PREP</span>
    <h3>Tina/Melissa Connect — 10:30 AM (Microsoft Teams)</h3>
    <div class="meta">Source: Google Calendar | tina@msearchadvisory.com</div>
    <p><strong>Why it matters:</strong> Meeting with Tina at M Search Advisory — likely a recruiter or search firm contact. High-value connection for your job search.</p>
    <p><strong>Next step:</strong> Prepare your current positioning, target roles, and availability. Have your updated resume and LinkedIn URL ready. Join via Teams link.</p>
    <div class="meta" style="margin-top:6px;">Due: Today, 10:30 AM</div>
  </div>

  <div class="card card-blue">
    <span class="label label-blue">🔵 TODAY — MEETING</span>
    <h3>Zoom with Dee Dee — 12:00 PM</h3>
    <div class="meta">Source: Google Calendar</div>
    <p><strong>Why it matters:</strong> Confirmed Zoom call. No Zoom link or agenda listed — verify before the call.</p>
    <p><strong>Next step:</strong> Locate the Zoom link and confirm agenda with Dee Dee. Be ready at noon.</p>
    <div class="meta" style="margin-top:6px;">Due: Today, 12:00 PM</div>
  </div>

  <div class="card card-green">
    <span class="label label-green">🟢 JOB SEARCH — PRIORITY</span>
    <h3>Review & Apply: VP of People (HR) at K Health</h3>
    <div class="meta">Source: LinkedIn Job Alerts — jobalerts-noreply@linkedin.com</div>
    <p><strong>Why it matters:</strong> VP-level HR role at a digital health company. Strong match with your HR executive background.</p>
    <p><strong>Next step:</strong> Open the LinkedIn alert, review the full JD, and apply if it aligns with targets.</p>
    <div class="meta" style="margin-top:6px;">Due: Today or this weekend</div>
  </div>

  <div class="card card-green">
    <span class="label label-green">🟢 JOB SEARCH — PRIORITY</span>
    <h3>Finalize LinkedIn Headline & Optimize Profile</h3>
    <div class="meta">Source: Self-email — melissaw212@gmail.com ("LinkedIn headline")</div>
    <p><strong>Why it matters:</strong> You emailed yourself the headline formula (Job Title + Expertise + Differentiation + Tagline + SEO). Profile optimization directly impacts recruiter visibility.</p>
    <p><strong>Next step:</strong> Write 3 headline variations using your formula and update your LinkedIn profile today.</p>
    <div class="meta" style="margin-top:6px;">Due: Today</div>
  </div>

  <div class="card card-yellow">
    <span class="label label-yellow">🟡 RSVP NEEDED</span>
    <h3>RSVP to HR Networking & Job Search Group Zoom — Aug 26</h3>
    <div class="meta">Source: Google Calendar | Status: needsAction</div>
    <p><strong>Why it matters:</strong> Large HR networking group meeting. RSVP is still pending. Strong networking opportunity.</p>
    <p><strong>Next step:</strong> Accept or decline the calendar invite. Review the team's guidelines doc linked in the event description.</p>
    <div class="meta" style="margin-top:6px;">Due: Before Aug 26, 12:00 PM</div>
  </div>

  <div class="card card-purple">
    <span class="label label-purple">🟣 PROFESSIONAL DEV</span>
    <h3>Confirm Claude 101 Workshop Details (Outskill / Zoom)</h3>
    <div class="meta">Source: Zoom — no-reply@zoom.us | Outskill — hi@mail.outskill.com</div>
    <p><strong>Why it matters:</strong> Your seat is reserved for the Claude 101 Workshop — a 3-hour session on Claude's current capabilities. Highly relevant for AI literacy in HR leadership roles.</p>
    <p><strong>Next step:</strong> Add the workshop date/time to your calendar. Locate and save the Zoom link from the confirmation email.</p>
    <div class="meta" style="margin-top:6px;">Due: Check confirmation for date</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 4 — FULL 7-DAY CALENDAR
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title blue">📅 Full 7-Day Calendar</div>

  <!-- FRIDAY AUG 21 -->
  <div class="cal-day">
    <div class="cal-day-header today">⭐ TODAY — Friday, August 21, 2026</div>
    <div class="cal-event">
      <div class="time">10:30 – 11:00 AM</div>
      <div>
        <div class="event-name">Tina/Melissa Connect <span class="rsvp rsvp-accepted">✅ Accepted</span></div>
        <div class="event-detail">📍 Microsoft Teams Meeting | Contact: tina@msearchadvisory.com</div>
        <div class="event-detail">🗒 <strong>Prep:</strong> Bring updated resume, target role list, and LinkedIn URL. Tina appears to be from M Search Advisory — likely an executive search firm. Be ready to discuss compensation expectations and timeline.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="time">12:00 – 12:30 PM</div>
      <div>
        <div class="event-name">Zoom with Dee Dee <span class="rsvp rsvp-confirmed">✅ Confirmed</span></div>
        <div class="event-detail">📍 No location/link listed — verify before call</div>
        <div class="event-detail">🗒 <strong>Prep:</strong> Locate Zoom link. Confirm agenda with Dee Dee. <span class="conflict-warn">⚠️ No link found — follow up now.</span></div>
      </div>
    </div>
  </div>

  <!-- SAT AUG 22 -->
  <div class="cal-day">
    <div class="cal-day-header">Saturday, August 22, 2026</div>
    <div class="cal-all-day">
      <div class="event-name" style="color:#777;">No events scheduled</div>
      <div class="event-detail">Free day — good time for job applications and LinkedIn headline update.</div>
    </div>
  </div>

  <!-- SUN AUG 23 -->
  <div class="cal-day">
    <div class="cal-day-header">Sunday, August 23, 2026</div>
    <div class="cal-all-day">
      <div class="event-name">📋 Verizon Fios Bill Due <span class="rsvp rsvp-confirmed">Confirmed</span></div>
      <div class="event-detail">All-day reminder — pay or verify auto-pay before end of day. <span class="conflict-warn">⚠️ Action required by today.</span></div>
    </div>
  </div>

  <!-- MON AUG 24 -->
  <div class="cal-day">
    <div class="cal-day-header">Monday, August 24, 2026</div>
    <div class="cal-all-day">
      <div class="event-name">🎂 Michael Rich's Birthday</div>
      <div class="event-detail">All-day — send a message or card if close.</div>
    </div>
    <div class="cal-event">
      <div class="time">9:15 – 10:15 AM</div>
      <div>
        <div class="event-name">Elle (calendar block) <span class="rsvp rsvp-confirmed">Confirmed</span></div>
        <div class="event-detail">⚠️ Overlaps with salon appointment below — this appears to be an early calendar block for the same appointment.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="time">9:15 – 10:45 AM</div>
      <div>
        <div class="event-name">💇 Hair Appointment — Elle at UMI Salon <span class="rsvp rsvp-confirmed">Confirmed</span></div>
        <div class="event-detail">📍 37 West 20th Suite 1107, New York, NY 10011</div>
        <div class="event-detail">Service: Single Process with Blowout | Stylist: Elle M</div>
        <div class="event-detail">🗒 <strong>Prep:</strong> Manage appointment at glossgenius link if changes needed. Allow travel time. <span class="conflict-warn">⚠️ Dual calendar entries — confirm which is the actual block.</span></div>
      </div>
    </div>
  </div>

  <!-- TUE AUG 25 -->
  <div class="cal-day">
    <div class="cal-day-header">Tuesday, August 25, 2026</div>
    <div class="cal-event">
      <div class="time">9:30 – 10:30 AM</div>
      <div>
        <div class="event-name">📞 Recruiter Call <span class="rsvp rsvp-confirmed">Confirmed</span></div>
        <div class="event-detail">📍 No location/link listed — confirm call-in details</div>
        <div class="event-detail">🗒 <strong>Prep:</strong> Have your pitch ready — target roles, salary range, availability, and top 3 accomplishments. Research the recruiter/firm beforehand if details surface.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="time">4:30 – 5:30 PM</div>
      <div>
        <div class="event-name">💅 Nails <span class="rsvp rsvp-confirmed">Confirmed</span></div>
        <div class="event-detail">📍 Location not listed</div>
        <div class="event-detail">🗒 Personal appointment — note conflict risk if recruiter call runs long.</div>
      </div>
    </div>
  </div>

  <!-- WED AUG 26 -->
  <div class="cal-day">
    <div class="cal-day-header">Wednesday, August 26, 2026</div>
    <div class="cal-all-day">
      <div class="event-name">💍 Amy's Anniversary</div>
      <div class="event-detail">All-day — send a message or card if appropriate.</div>
    </div>
    <div class="cal-event">
      <div class="time">12:00 – 1:30 PM</div>
      <div>
        <div class="event-name">🌐 HR Networking &amp; Job Search Group — Zoom 2 <span class="rsvp rsvp-pending">⏳ RSVP Needed</span></div>
        <div class="event-detail">📍 <a href="https://us06web.zoom.us/j/81954171722" style="color:#1565c0;">Zoom Link</a> | 150+ HR professionals</div>
        <div class="event-detail">🗒 <strong>Prep:</strong> Review HR Networking Team Guidelines (linked in calendar description). Prepare your 30-second intro and 2–3 networking asks. <span class="conflict-warn">⚠️ RSVP not yet submitted.</span></div>
      </div>
    </div>
    <div class="cal-event">
      <div class="time">12:00 – 1:30 PM</div>
      <div>
        <div class="event-name">🌐 Network (duplicate block) <span class="rsvp rsvp-confirmed">Confirmed</span></div>
        <div class="event-detail">Appears to be a personal block for the same HR Networking Zoom above.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="time">3:00 – 4:00 PM</div>
      <div>
        <div class="event-name">💅 Nails <span class="rsvp rsvp-confirmed">Confirmed</span></div>
        <div class="event-detail">📍 Location not listed — personal appointment.</div>
      </div>
    </div>
  </div>

  <!-- THU AUG 27 -->
  <div class="cal-day">
    <div class="cal-day-header">Thursday, August 27, 2026</div>
    <div class="cal-all-day">
      <div class="event-name">🎂 Christian H's Birthday</div>
      <div class="event-detail">All-day — send a message if appropriate.</div>
    </div>
    <div class="cal-event">
      <div class="time">9:00 – 10:30 AM</div>
      <div>
        <div class="event-name">🏛 Executive Roundtable (John Madigan) <span class="rsvp rsvp-declined">❌ Declined</span></div>
        <div class="event-detail">📍 Zoom | Meeting ID: 207 786 667 | Password: 205454</div>
        <div class="event-detail">🗒 You have declined this event. No action needed unless you wish to reconsider.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="time">12:00 – 1:00 PM</div>
      <div>
        <div class="event-name">🌐 HR Networking &amp; Job Search: Open Office Hours — Zoom 2 <span class="rsvp rsvp-pending">⏳ RSVP Needed</span></div>
        <div class="event-detail">📍 <a href="https://us06web.zoom.us/j/85945371140" style="color:#1565c0;">Zoom Link</a> | Note: AI notetaking tools NOT permitted</div>
        <div class="event-detail">🗒 <strong>Prep:</strong> Open discussion format — good for informal networking. <span class="conflict-warn">⚠️ RSVP not yet submitted. Do NOT use AI notetaking per host instructions.</span></div>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 5 — JOB SEARCH & INTERVIEW PIPELINE
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title green">💼 Job Search & Interview Pipeline</div>

  <div class="group-header">🎯 Active Job Leads / Alerts</div>
  <table>
    <thead>
      <tr>
        <th>Role</th>
        <th>Company</th>
        <th>Source</th>
        <th>Fit</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>VP of People (HR)</td>
        <td>K Health</td>
        <td>LinkedIn Job Alert</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>Open alert, review JD, apply today</td>
      </tr>
      <tr>
        <td>Head of Human Resources</td>
        <td>Global Energy Alliance for People and Planet</td>
        <td>LinkedIn Job Alert (x2)</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>Review role — mission-driven org, strong fit</td>
      </tr>
      <tr>
        <td>VP Human Resources</td>
        <td>Lerryn House</td>
        <td>Self-saved LinkedIn link</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>Open saved link, review, apply if aligned</td>
      </tr>
      <tr>
        <td>HR Director</td>
        <td>Iceberg</td>
        <td>Self-saved LinkedIn link</td>
        <td><span class="fit-medium">MEDIUM</span></td>
        <td>Review JD — apply if strong match</td>
      </tr>
      <tr>
        <td>Human Resources Director (Remote)</td>
        <td>Maximus</td>
        <td>LinkedIn Job Alert</td>
        <td><span class="fit-medium">MEDIUM</span></td>
        <td>Already in inbox — review and apply</td>
      </tr>
      <tr>
        <td>Senior HR Business Partner</td>
        <td>Maven Clinic</td>
        <td>Self-saved LinkedIn link</td>
        <td><span class="fit-medium">MEDIUM</span></td>
        <td>Review JD — good digital health exposure</td>
      </tr>
      <tr>
        <td>Chief People Officer / Lead Talent Culture Change</td>
        <td>Multiple (JobLeads)</td>
        <td>JobLeads digest (trashed)</td>
        <td><span class="fit-medium">MEDIUM</span></td>
        <td>Log in to JobLeads to review Aug 20 results</td>
      </tr>
      <tr>
        <td>HR Executive roles</td>
        <td>HireTalent — Staffing &amp; Recruiting Firm</td>
        <td>LinkedIn</td>
        <td><span class="fit-medium">MEDIUM</span></td>
        <td>Click through to HireTalent listing for details</td>
      </tr>
    </tbody>
  </table>

  <div class="group-header" style="margin-top:16px;">🤝 Recruiters & Networking Contacts</div>
  <table>
    <thead>
      <tr>
        <th>Contact</th>
        <th>Org / Platform</th>
        <th>Status</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Tina (last name unknown)</td>
        <td>M Search Advisory</td>
        <td>Meeting TODAY 10:30 AM</td>
        <td>Prep and join Teams call — high priority</td>
      </tr>
      <tr>
        <td>Recruiter (name unknown)</td>
        <td>Unknown firm</td>
        <td>Call scheduled Aug 25, 9:30 AM</td>
        <td>Confirm dial-in details; prepare pitch</td>
      </tr>
      <tr>
        <td>Glenn Lesko</td>
        <td>LinkedIn</td>
        <td>Connection accepted</td>
        <td>Send a warm introductory message</td>
      </tr>
      <tr>
        <td>Shoan Shinde (CMO, TurboHire)</td>
        <td>LinkedIn</td>
        <td>Pending — connection request received</td>
        <td>Review profile; accept or decline</td>
      </tr>
      <tr>
        <td>Seth Rogers</td>
        <td>LinkedIn (self-saved profile)</td>
        <td>Not yet reached out</td>
        <td>Review profile and send connection request</td>
      </tr>
      <tr>
        <td>Mario Linale</td>
        <td>LinkedIn (self-saved profile)</td>
        <td>Not yet reached out</td>
        <td>Review profile and send connection request</td>
      </tr>
      <tr>
        <td>HR Networking Group (150+ members)</td>
        <td>Zoom — Aug 26 &amp; Aug 27</td>
        <td>RSVP pending</td>
        <td>Confirm RSVP to both sessions</td>
      </tr>
    </tbody>
  </table>

  <div class="group-header" style="margin-top:16px;">🛠 Job Search Tools & Platforms</div>
  <table>
    <thead>
      <tr>
        <th>Platform</th>
        <th>Status</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>HackaJob / Archer</td>
        <td>Profile started but incomplete</td>
        <td>Complete profile to activate AI-powered job hunting</td>
      </tr>
      <tr>
        <td>LinkedIn</td>
        <td>Active — headline needs update</td>
        <td>Apply self-note formula: Title + Expertise + Differentiation + SEO</td>
      </tr>
      <tr>
        <td>Outskill / Claude 101 Workshop</td>
        <td>Registered — seat confirmed</td>
        <td>Add to calendar; prepare questions about Claude for HR use</td>
      </tr>
      <tr>
        <td>JobLeads</td>
        <td>Active digest (trashed)</td>
        <td>Log in directly for Aug 20 CPO/Talent results</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 6 — FULL EMAIL REVIEW BY CATEGORY
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title red">📂 Full Email Review by Category</div>

  <!-- SECURITY / RISK -->
  <div class="card card-red">
    <span class="label label-red">🔴 Security / Risk — 8 Emails</span>
    <h3>Phishing & Credential-Harvesting Attempts</h3>
    <p>All 8 emails below were <strong>auto-trashed</strong> before reaching your inbox. No action required beyond awareness.</p>
    <br>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Reason Auto-Trashed</th></tr></thead>
      <tbody>
        <tr><td><span class="phish-badge">PHISH</span> melissaw212 (gibberish domain)</td><td>We've blocked your account! Photos deleted Fri Aug 21</td><td>Spoofed cloud storage scam; gibberish sender domain; credential harvesting</td></tr>
        <tr><td><span class="phish-badge">PHISH</span> 'Payment-Declined' (gibberish)</td><td>🚨 Your Account Sirius XM Will Be Removed Today</td><td>Spoofed SiriusXM; urgent account removal threat; gibberish domain</td></tr>
        <tr><td><span class="phish-badge">PHISH</span> 💲CashApp💲 (gibberish)</td><td>You have received $15.99 — Raging Bull Casino</td><td>Spoofed CashApp; unrendered template variables; gibberish domain; mass phishing</td></tr>
        <tr><td><span class="phish-badge">PHISH</span> 'Paym̲ent_lssue' (gibberish)</td><td>🚨 We've blocked your account! Photos deleted Fri Aug 21 #324694</td><td>Spoofed cloud/payment service; Unicode lookalike characters; gibberish domain</td></tr>
        <tr><td><span class="phish-badge">PHISH</span> 'GmailSupportTeam' (gibberish)</td><td>melissaw212, Your Account locked Thu Aug 20</td><td>Explicitly spoofed Gmail Support; victim email on gibberish domain; credential harvesting</td></tr>
        <tr><td><span class="phish-badge">PHISH</span> melissaw212 (vexogroup.biz)</td><td>We have blocked your account — photos deleted Thu Aug 20</td><td>Spoofed iCloud; victim's own email address on gibberish domain</td></tr>
        <tr><td><span class="phish-badge">SPAM</span> 'Rock Hard' (gibberish)</td><td>Your wife will thank you</td><td>Adult spam; gibberish sender domain</td></tr>
        <tr><td><span class="phish-badge">SPAM</span> 'Sex Trick' (gibberish)</td><td>🔞 Naughty porn star reveals secret...</td><td>Adult spam; gibberish sender domain</td></tr>
      </tbody>
    </table>
    <p class="note">Additionally: "Penis_Growth_Doctor" and "FUCK-BUDDY SECRET" emails from gibberish domains were not marked auto_trashed in the data but are identical in pattern — treat as spam/auto-delete.</p>
  </div>

  <!-- JOB SEARCH -->
  <div class="card card-green">
    <span class="label label-green">🟢 Job Search — 13 Emails</span>
    <h3>Active Job Leads, Applications & Search Tools</h3>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Status / Action</th></tr></thead>
      <tbody>
        <tr><td>LinkedIn Job Alerts</td><td>VP of People (HR) — K Health</td><td>📥 Inbox — Apply today</td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>Head of HR — Global Energy Alliance (x2 alerts)</td><td>📥 Inbox + Not in inbox — Review &amp; apply</td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>HR Director (Remote) — Maximus</td><td>📥 Inbox — Review</td></tr>
        <tr><td>LinkedIn</td><td>HR Executive — HireTalent Staffing</td><td>📥 Inbox — Click through for details</td></tr>
        <tr><td>Melissa W (self)</td><td>VP HR | Lerryn House</td><td>📥 Self-saved — Review &amp; apply</td></tr>
        <tr><td>Melissa W (self)</td><td>HR Director | Iceberg</td><td>📥 Self-saved — Review &amp; apply</td></tr>
        <tr><td>Melissa W (self)</td><td>Sr. HRBP | Maven Clinic</td><td>📥 Self-saved — Review &amp; apply</td></tr>
        <tr><td>Melissa W (self)</td><td>LinkedIn headline formula</td><td>📥 Self-note — Execute today</td></tr>
        <tr><td>Melissa W (self)</td><td>Hackajob note</td><td>📥 Self-note — Complete profile</td></tr>
        <tr><td>Archer / HackaJob</td><td>Your dream job is a few clicks away</td><td>📥 Inbox — Complete profile setup</td></tr>
        <tr><td>JobLeads</td><td>5 new CPO/Talent jobs — Aug 20</td><td>🗑 Trashed — Log in to JobLeads directly</td></tr>
        <tr><td>Glassdoor Jobs</td><td>Senior HR Generalist + 8 more remote jobs</td><td>🗑 Trashed — Check Glassdoor if interested</td></tr>
        <tr><td>Glassdoor Jobs</td><td>Director, Community Cat Program + 6 NYC jobs</td><td>🗑 Trashed — Low fit for exec search</td></tr>
      </tbody>
    </table>
  </div>

  <!-- RECRUITERS / NETWORKING -->
  <div class="card card-green">
    <span class="label label-green">🟢 Recruiters / Networking — 5 Emails</span>
    <h3>Connection Requests & Professional Networking</h3>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>LinkedIn (Glenn Lesko)</td><td>Glenn accepted your invitation</td><td>📥 Inbox — Send warm intro message</td></tr>
        <tr><td>LinkedIn (Shoan Shinde / TurboHire CMO)</td><td>Melissa A, I'd like to connect</td><td>📥 Inbox — Review profile; accept or decline</td></tr>
        <tr><td>Melissa W (self)</td><td>Seth Rogers | LinkedIn</td><td>📥 Self-saved profile — Reach out</td></tr>
        <tr><td>Melissa W (self)</td><td>Mario Linale | LinkedIn</td><td>📥 Self-saved profile — Reach out</td></tr>
        <tr><td>LinkedIn</td><td>Jules S. Ehrenberg shares thoughts</td><td>Not in inbox — Low priority, read if time permits</td></tr>
      </tbody>
    </table>
  </div>

  <!-- CALENDAR / EVENTS -->
  <div class="card card-blue">
    <span class="label label-blue">🔵 Calendar / Events — 3 Emails</span>
    <h3>Meeting Confirmations & Workshop Registration</h3>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>Zoom / Outskill</td><td>Your seat is reserved — Claude 101 Workshop (3 hrs)</td><td>Add to calendar; locate date/time in full email</td></tr>
        <tr><td>Outskill</td><td>You're in. Here's what we built for you.</td><td>Read for workshop details — rebuilt around Claude's new capabilities</td></tr>
        <tr><td>Slack</td><td>Set up Slack across your devices</td><td>Download desktop + mobile apps for new workspace</td></tr>
      </tbody>
    </table>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="card card-yellow">
    <span class="label label-yellow">🟡 Financial / Billing — 1 Email</span>
    <h3>Equifax Credit Report Offer</h3>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>Equifax</td><td>Get your credit report by dinner time 🍽</td><td>🗑 Trashed — Visit Equifax.com directly if needed; do not click email links for credit services</td></tr>
      </tbody>
    </table>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="card card-purple">
    <span class="label label-purple">🟣 Professional Development — 2 Emails</span>
    <h3>AI Workshop & Online Learning</h3>
    <table
