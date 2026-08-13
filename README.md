<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa W. — August 13, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px 60px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 16px; padding: 36px 40px 28px; margin-bottom: 24px; box-shadow: 0 6px 24px rgba(0,0,0,0.18); }
  .header h1 { font-size: 2rem; font-weight: 700; letter-spacing: -0.5px; }
  .header .subtitle { font-size: 1.05rem; color: #a8c0e0; margin-top: 4px; }
  .header-meta { display: flex; gap: 32px; margin-top: 20px; flex-wrap: wrap; }
  .header-meta-item { background: rgba(255,255,255,0.08); border-radius: 10px; padding: 10px 18px; }
  .header-meta-item .label { font-size: 11px; color: #a8c0e0; text-transform: uppercase; letter-spacing: 0.08em; }
  .header-meta-item .value { font-size: 1.2rem; font-weight: 700; color: #fff; }

  /* SECTION HEADERS */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 1.05rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; padding: 10px 16px; border-radius: 8px 8px 0 0; display: flex; align-items: center; gap: 8px; }
  .section-body { background: #fff; border-radius: 0 0 12px 12px; padding: 18px 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.07); }
  .section-body.rounded { border-radius: 12px; }

  /* COLOR THEMES */
  .red .section-title { background: #c0392b; color: #fff; }
  .red { border: 1.5px solid #c0392b; border-radius: 12px; }
  .yellow .section-title { background: #f39c12; color: #fff; }
  .yellow { border: 1.5px solid #f39c12; border-radius: 12px; }
  .blue .section-title { background: #2471a3; color: #fff; }
  .blue { border: 1.5px solid #2471a3; border-radius: 12px; }
  .green .section-title { background: #1e8449; color: #fff; }
  .green { border: 1.5px solid #1e8449; border-radius: 12px; }
  .purple .section-title { background: #7d3c98; color: #fff; }
  .purple { border: 1.5px solid #7d3c98; border-radius: 12px; }
  .gray .section-title { background: #717d7e; color: #fff; }
  .gray { border: 1.5px solid #717d7e; border-radius: 12px; }
  .navy .section-title { background: #1a1a2e; color: #fff; }
  .navy { border: 1.5px solid #1a1a2e; border-radius: 12px; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #f4f6f8; text-align: left; padding: 9px 12px; font-weight: 700; color: #444; border-bottom: 2px solid #e0e4ea; font-size: 12px; text-transform: uppercase; letter-spacing: 0.05em; }
  td { padding: 9px 12px; border-bottom: 1px solid #f0f2f5; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f9fafb; }

  /* CARDS */
  .card { background: #fff; border-radius: 10px; padding: 16px 18px; margin-bottom: 12px; border-left: 4px solid #ccc; box-shadow: 0 1px 6px rgba(0,0,0,0.06); }
  .card.red-card { border-left-color: #c0392b; }
  .card.yellow-card { border-left-color: #f39c12; }
  .card.blue-card { border-left-color: #2471a3; }
  .card.green-card { border-left-color: #1e8449; }
  .card.purple-card { border-left-color: #7d3c98; }
  .card.gray-card { border-left-color: #717d7e; }
  .card-title { font-weight: 700; font-size: 14px; margin-bottom: 4px; }
  .card-meta { font-size: 12px; color: #777; margin-bottom: 6px; }
  .card-body { font-size: 13px; }
  .card-row { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 6px; }
  .card-label { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; padding: 2px 8px; border-radius: 20px; }
  .label-red { background: #fdecea; color: #c0392b; }
  .label-yellow { background: #fef9e7; color: #d4ac0d; }
  .label-green { background: #eafaf1; color: #1e8449; }
  .label-blue { background: #eaf3fb; color: #2471a3; }
  .label-purple { background: #f5eef8; color: #7d3c98; }
  .label-gray { background: #f2f3f4; color: #717d7e; }
  .label-orange { background: #fef0e7; color: #ca6f1e; }

  /* EXEC SUMMARY */
  .exec-bullets { list-style: none; padding: 0; }
  .exec-bullets li { padding: 10px 14px; margin-bottom: 8px; border-radius: 8px; font-size: 14px; display: flex; align-items: flex-start; gap: 10px; }
  .exec-bullets li.risk { background: #fdecea; border-left: 4px solid #c0392b; }
  .exec-bullets li.opportunity { background: #eafaf1; border-left: 4px solid #1e8449; }
  .exec-bullets li.calendar-item { background: #eaf3fb; border-left: 4px solid #2471a3; }
  .exec-bullets li .icon { font-size: 1.1rem; flex-shrink: 0; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { background: #1a1a2e; color: #fff; padding: 8px 14px; border-radius: 8px 8px 0 0; font-weight: 700; font-size: 13px; }
  .cal-event { background: #fff; border-left: 4px solid #2471a3; padding: 12px 16px; margin-bottom: 6px; border-radius: 0 8px 8px 0; box-shadow: 0 1px 4px rgba(0,0,0,0.06); }
  .cal-event.declined { border-left-color: #c0392b; opacity: 0.75; }
  .cal-event.needs-action { border-left-color: #f39c12; }
  .cal-event.accepted { border-left-color: #1e8449; }
  .cal-event.confirmed { border-left-color: #2471a3; }
  .cal-time { font-weight: 700; font-size: 13px; color: #2471a3; }
  .cal-name { font-weight: 700; font-size: 14px; }
  .cal-detail { font-size: 12px; color: #666; margin-top: 3px; }
  .cal-badge { display: inline-block; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 20px; margin-left: 6px; vertical-align: middle; }
  .badge-declined { background: #fdecea; color: #c0392b; }
  .badge-accepted { background: #eafaf1; color: #1e8449; }
  .badge-pending { background: #fef9e7; color: #d4ac0d; }
  .badge-confirmed { background: #eaf3fb; color: #2471a3; }

  /* TRIAGE TABLE */
  .triage-status { font-weight: 700; white-space: nowrap; }
  .triage-rescued { color: #1e8449; }
  .triage-inbox { color: #2471a3; }
  .triage-trash { color: #717d7e; }
  .triage-auto { color: #c0392b; }

  /* DASHBOARD */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 14px; }
  .dash-tile { background: #fff; border-radius: 12px; padding: 18px 16px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.08); border-top: 4px solid #ccc; }
  .dash-tile.red-t { border-top-color: #c0392b; }
  .dash-tile.yellow-t { border-top-color: #f39c12; }
  .dash-tile.blue-t { border-top-color: #2471a3; }
  .dash-tile.green-t { border-top-color: #1e8449; }
  .dash-tile.purple-t { border-top-color: #7d3c98; }
  .dash-tile.gray-t { border-top-color: #717d7e; }
  .dash-tile .tile-num { font-size: 2.2rem; font-weight: 800; color: #1a1a2e; }
  .dash-tile .tile-label { font-size: 11px; text-transform: uppercase; letter-spacing: 0.07em; color: #888; margin-top: 4px; }
  .dash-tile .tile-detail { font-size: 12px; color: #555; margin-top: 6px; }

  /* PRIORITY */
  .priority-high { color: #c0392b; font-weight: 700; }
  .priority-med { color: #d4ac0d; font-weight: 700; }
  .priority-low { color: #1e8449; font-weight: 700; }

  /* TOP 3 */
  .top3 { counter-reset: top3; }
  .top3-item { display: flex; align-items: flex-start; gap: 16px; padding: 16px 18px; background: #fff; border-radius: 10px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); border-left: 5px solid #1a1a2e; }
  .top3-num { font-size: 2rem; font-weight: 900; color: #1a1a2e; line-height: 1; flex-shrink: 0; width: 32px; text-align: center; }
  .top3-content .top3-title { font-weight: 700; font-size: 15px; }
  .top3-content .top3-desc { font-size: 13px; color: #555; margin-top: 4px; }

  /* MISC */
  .rescued-badge { background: #eafaf1; color: #1e8449; font-size: 11px; font-weight: 700; padding: 2px 7px; border-radius: 20px; margin-left: 6px; }
  .phishing-badge { background: #fdecea; color: #c0392b; font-size: 11px; font-weight: 700; padding: 2px 7px; border-radius: 20px; margin-left: 6px; }
  .warning-box { background: #fdecea; border: 1.5px solid #c0392b; border-radius: 8px; padding: 12px 16px; margin-bottom: 12px; font-size: 13px; }
  .info-box { background: #eaf3fb; border: 1.5px solid #2471a3; border-radius: 8px; padding: 12px 16px; margin-bottom: 12px; font-size: 13px; }
  .success-box { background: #eafaf1; border: 1.5px solid #1e8449; border-radius: 8px; padding: 12px 16px; margin-bottom: 12px; font-size: 13px; }
  .note { font-size: 12px; color: #888; font-style: italic; margin-top: 6px; }
  .divider { border: none; border-top: 1.5px solid #e8eaed; margin: 18px 0; }
  a { color: #2471a3; text-decoration: none; }
  a:hover { text-decoration: underline; }
  .bold { font-weight: 700; }
  ul.plain { list-style: none; padding: 0; }
  ul.plain li { padding: 3px 0; }
  .inline-flex { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
  @media (max-width: 700px) {
    .header { padding: 22px 18px; }
    .header h1 { font-size: 1.4rem; }
    .header-meta { gap: 12px; }
    .page-wrap { padding: 12px 8px 40px; }
  }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ═══════════════════════════════════════════════════════════
     SECTION 0 — EMAIL TRIAGE QUICK LIST
═══════════════════════════════════════════════════════════ -->
<div class="section navy">
  <div class="section-title">📋 Email Triage Quick List</div>
  <div class="section-body">
    <p class="note" style="margin-bottom:12px;">Rescued emails first → Inbox emails → Trash summary rows. One row per inbox/rescued email; trash collapsed.</p>
    <table>
      <thead><tr><th>Status</th><th>From</th><th>Subject</th><th>Summary / Note</th></tr></thead>
      <tbody>
        <!-- RESCUED emails first -->
        <tr>
          <td class="triage-status triage-rescued">✅ RESCUED</td>
          <td>Google</td>
          <td>You shared some Google Account data with Slack</td>
          <td>Security notice — Google data shared with Slack (Wed 22:12). Rescued: security notification.</td>
        </tr>
        <tr>
          <td class="triage-status triage-rescued">✅ RESCUED</td>
          <td>Google</td>
          <td>You shared some Google Account data with Claude</td>
          <td>Security notice — Google data shared with Claude (Wed 22:02). Rescued: security notification.</td>
        </tr>
        <tr>
          <td class="triage-status triage-rescued">✅ RESCUED</td>
          <td>Google</td>
          <td>You shared some Google Account data with Slack</td>
          <td>Security notice — Google data shared with Slack (Wed 22:01). Rescued: security notification.</td>
        </tr>
        <tr>
          <td class="triage-status triage-rescued">✅ RESCUED</td>
          <td>GitHub</td>
          <td>[GitHub] A third-party OAuth application has been added to your account</td>
          <td>OAuth app "MCP Market" added to GitHub account. Rescued: security alert — verify authorization.</td>
        </tr>
        <tr>
          <td class="triage-status triage-rescued">✅ RESCUED</td>
          <td>Google</td>
          <td>You shared some Google Account data with Blink.new</td>
          <td>Security notice — Google data shared with Blink.new (Wed 21:06). Rescued: security notification.</td>
        </tr>
        <tr>
          <td class="triage-status triage-rescued">✅ RESCUED</td>
          <td>Google</td>
          <td>You shared some Google Account data with Slack</td>
          <td>Security notice — Google data shared with Slack (Wed 19:12). Rescued: security notification.</td>
        </tr>
        <tr>
          <td class="triage-status triage-rescued">✅ RESCUED</td>
          <td>Google</td>
          <td>You shared some Google Account data with Slack</td>
          <td>Security notice — Google data shared with Slack (Wed 19:00). Rescued: security notification.</td>
        </tr>
        <tr>
          <td class="triage-status triage-rescued">✅ RESCUED</td>
          <td>Google</td>
          <td>You shared some Google Account data with Claude</td>
          <td>Security notice — Google data shared with Claude (Wed 18:54). Rescued: security notification.</td>
        </tr>
        <tr>
          <td class="triage-status triage-rescued">✅ RESCUED</td>
          <td>Google</td>
          <td>You shared some Google Account data with Slack</td>
          <td>Security notice — Google data shared with Slack (Wed 18:32). Rescued: security notification.</td>
        </tr>
        <tr>
          <td class="triage-status triage-rescued">✅ RESCUED</td>
          <td>JetBlue Plus Card (Barclays)</td>
          <td>Reminder: Activate your 8.99% promo rate now</td>
          <td>Promo APR activation offer — protected sender, rescued from trash. Review before deadline.</td>
        </tr>
        <tr>
          <td class="triage-status triage-rescued">✅ RESCUED</td>
          <td>Workday (Booking Holdings)</td>
          <td>Thank you for your interest in a career with Booking Holdings!</td>
          <td>Application acknowledged — Head of HR at Booking Holdings. Rescued: job application response.</td>
        </tr>
        <!-- INBOX emails -->
        <tr>
          <td class="triage-status triage-inbox">📥 INBOX</td>
          <td>Bank of America</td>
          <td>Billing Dispute for account -2994 — Merchant credit has been issued</td>
          <td>Dispute resolved — merchant credit issued. Step 2 of 3. Monitor for Step 3.</td>
        </tr>
        <tr>
          <td class="triage-status triage-inbox">📥 INBOX</td>
          <td>LinkedIn Job Alerts</td>
          <td>People Partner, GTM at Profound</td>
          <td>Job alert — People Partner, GTM role at Profound. Review fit.</td>
        </tr>
        <tr>
          <td class="triage-status triage-inbox">📥 INBOX</td>
          <td>LinkedIn Job Alerts</td>
          <td>Vice President of Human Resources, The Americas at Soho House &amp; Co</td>
          <td>Actively recruiting — VP HR, The Americas. High-fit senior role.</td>
        </tr>
        <tr>
          <td class="triage-status triage-inbox">📥 INBOX</td>
          <td>Match</td>
          <td>Alexander likes you. See if it's mutual.</td>
          <td>Match notification — Alexander liked your profile.</td>
        </tr>
        <tr>
          <td class="triage-status triage-inbox">📥 INBOX</td>
          <td>Match</td>
          <td>You've had a profile view from Mike</td>
          <td>Profile view from Mike, 56, Providence RI.</td>
        </tr>
        <tr>
          <td class="triage-status triage-inbox">📥 INBOX</td>
          <td>Amazon.com</td>
          <td>Shipped: 1 Storage item</td>
          <td>Storage item shipped — track delivery.</td>
        </tr>
        <tr>
          <td class="triage-status triage-inbox">📥 INBOX</td>
          <td>TikTok Shop</td>
          <td>Your order 577508639223287836 was canceled</td>
          <td>Order canceled — lost/damaged. Refund in progress.</td>
        </tr>
        <tr>
          <td class="triage-status triage-inbox">📥 INBOX</td>
          <td>Amazon.com</td>
          <td>Shipped: 1 Apparel item</td>
          <td>Apparel item shipped (06:02) — track delivery.</td>
        </tr>
        <tr>
          <td class="triage-status triage-inbox">📥 INBOX</td>
          <td>Amazon.com</td>
          <td>Shipped: 1 Apparel item</td>
          <td>Apparel item shipped (06:00) — track delivery.</td>
        </tr>
        <tr>
          <td class="triage-status triage-inbox">📥 INBOX</td>
          <td>LinkedIn</td>
          <td>View Games Jobs Direct's post and your next steps</td>
          <td>LinkedIn recommended actions — Games Jobs Direct post.</td>
        </tr>
        <tr>
          <td class="triage-status triage-inbox">📥 INBOX</td>
          <td>LinkedIn Job Alerts</td>
          <td>Vice President of Human Resources, The Americas at Soho House &amp; Co (earlier alert)</td>
          <td>Duplicate job alert — Soho House VP HR, The Americas (earlier send).</td>
        </tr>
        <tr>
          <td class="triage-status triage-inbox">📥 INBOX</td>
          <td>LinkedIn Job Alerts</td>
          <td>People Partner, GTM at Profound (earlier alert)</td>
          <td>Duplicate job alert — People Partner, GTM at Profound (earlier send, read).</td>
        </tr>
        <!-- TRASH SUMMARY ROWS -->
        <tr style="background:#fff8f8;">
          <td class="triage-status triage-auto">🚫 AUTO-TRASHED (1)</td>
          <td colspan="3"><strong>1 email auto-trashed as phishing</strong> — iCloud/Apple credential harvesting spoof. See Trash Review &amp; Security sections below.</td>
        </tr>
        <tr style="background:#f8f8f8;">
          <td class="triage-status triage-trash">🗂 TRASH (manual, ~26)</td>
          <td colspan="3"><strong>~26 emails in Trash</strong> (newsletters, retail, spam, Slack setup, job digests, etc.) — see Trash Review section below.</td>
        </tr>
        <!-- Non-inbox, non-trashed, non-rescued spam still in inbox area -->
        <tr style="background:#fff8f8;">
          <td class="triage-status triage-auto">⚠️ SPAM (not trashed)</td>
          <td colspan="3"><strong>4 spam/phishing emails</strong> still in non-inbox limbo (GLP-1 spam ×3, adult spam ×1) — see Security &amp; Safe to Delete sections below.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 1 — HEADER
═══════════════════════════════════════════════════════════ -->
<div class="header">
  <div class="subtitle">Executive Briefing · Prepared by Your Chief of Staff</div>
  <h1>Good morning, Melissa ☀️</h1>
  <div class="header-meta">
    <div class="header-meta-item"><div class="label">Date</div><div class="value">Thursday, August 13, 2026</div></div>
    <div class="header-meta-item"><div class="label">Emails Reviewed</div><div class="value">50</div></div>
    <div class="header-meta-item"><div class="label">Calendar Events</div><div class="value">7</div></div>
    <div class="header-meta-item"><div class="label">Action Items</div><div class="value">8</div></div>
    <div class="header-meta-item"><div class="label">Security Alerts</div><div class="value">⚠️ 11</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 2 — EXECUTIVE SUMMARY
═══════════════════════════════════════════════════════════ -->
<div class="section navy">
  <div class="section-title">⚡ Executive Summary</div>
  <div class="section-body rounded">
    <ul class="exec-bullets">
      <li class="risk"><span class="icon">🔴</span><span><strong>SECURITY RISK:</strong> A GitHub OAuth app ("MCP Market") was added to your account last night, and 8 Google account data-sharing events with Slack, Claude, and Blink.new occurred across the evening — all rescued from Trash. Verify each authorization is intentional. Additionally, one phishing email (iCloud spoof) was auto-trashed, and 4 spam/adult-content emails remain untrashed and should be deleted immediately.</span></li>
      <li class="opportunity"><span class="icon">🟢</span><span><strong>JOB SEARCH OPPORTUNITY:</strong> Two strong senior-level alerts are in your inbox — <strong>VP of Human Resources, The Americas at Soho House &amp; Co</strong> (actively recruiting) and <strong>People Partner, GTM at Profound</strong> — plus a confirmed application acknowledgment from <strong>Booking Holdings</strong> (Head of HR). Your networking session today at noon and your m&amp;M meeting at 3:30 PM are live opportunities.</span></li>
      <li class="calendar-item"><span class="icon">🔵</span><span><strong>CALENDAR / DEADLINES:</strong> You have three events today — an Executive Roundtable (declined, 9–10:30 AM), HR Networking Open Office Hours at noon (RSVP pending — decide now), and m&amp;M at 3:30 PM (accepted). Next week: Stella's vet appointment Tuesday Aug 18, and another HR Networking session Tuesday Aug 19 (RSVP still pending). JetBlue Plus Card 8.99% promo APR activation has an unknown expiration — act soon.</span></li>
    </ul>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 3 — ACTION REQUIRED
═══════════════════════════════════════════════════════════ -->
<div class="section red">
  <div class="section-title">🚨 Action Required</div>
  <div class="section-body">

    <div class="card red-card">
      <div class="inline-flex"><span class="card-label label-red">🔴 URGENT — SECURITY</span></div>
      <div class="card-title" style="margin-top:6px;">Verify GitHub OAuth App — "MCP Market" Added to Your Account</div>
      <div class="card-meta">Source: GitHub &lt;noreply@github.com&gt; · Wed Aug 12, 9:52 PM · Rescued from Trash</div>
      <div class="card-body">A third-party OAuth app called <strong>MCP Market</strong> with <code>user:email</code> scope was authorized on your GitHub account (username: <strong>missophs</strong>). If you did not authorize this, revoke immediately at <a href="https://github.com/settings/applications">github.com/settings/applications</a>.</div>
      <div class="card-row"><span class="card-label label-red">Next Step</span> <span>Visit GitHub → Settings → Applications → Authorized OAuth Apps → Revoke "MCP Market" if unrecognized.</span></div>
      <div class="card-row"><span class="card-label label-red">Due</span> <span>Today — immediately</span></div>
    </div>

    <div class="card red-card">
      <div class="inline-flex"><span class="card-label label-red">🔴 URGENT — SECURITY</span></div>
      <div class="card-title" style="margin-top:6px;">Review 9 Google Account Data-Sharing Events (Slack, Claude, Blink.new)</div>
      <div class="card-meta">Source: Google &lt;noreply-accounts@google.com&gt; · Multiple events Wed Aug 12, 6:30–10:12 PM · All rescued from Trash</div>
      <div class="card-body">Between ~6:30 PM and 10:12 PM yesterday, your Google account triggered <strong>9 data-sharing notifications</strong>: Slack (×6), Claude (×2), Blink.new (×1). This volume in a short window may indicate repeated sign-in attempts or automated connections. Verify each app is authorized at <a href="https://myaccount.google.com/permissions">myaccount.google.com/permissions</a>.</div>
      <div class="card-row"><span class="card-label label-red">Next Step</span> <span>Audit connected apps at Google Account → Security → Third-party apps. Revoke any unrecognized. Consider enabling login alerts.</span></div>
      <div class="card-row"><span class="card-label label-red">Due</span> <span>Today</span></div>
    </div>

    <div class="card red-card">
      <div class="inline-flex"><span class="card-label label-red">🔴 SECURITY — DELETE</span></div>
      <div class="card-title" style="margin-top:6px;">Delete 4 Spam / Adult / Phishing Emails Still in Your Account</div>
      <div class="card-meta">Sources: GLP-1 spam ×3 (DirectMeds, Direct_Meds_Care_Team, 'Direct Meds Care Team'), Adult spam ×1 ('F**ckMeHard'), Adult spam ×1 ('Sex Trick?!*') · Not trashed</div>
      <div class="card-body">Five unsolicited spam emails remain untrashed: three are GLP-1 weight-loss spam (suspicious domains), one is an adult solicitation with explicit content, and one is an adult/viral video lure. Do not click any links. Delete all immediately.</div>
      <div class="card-row"><span class="card-label label-red">Next Step</span> <span>Select all five → Delete + Mark as Spam to help Gmail filter future messages.</span></div>
      <div class="card-row"><span class="card-label label-red">Due</span> <span>Now</span></div>
    </div>

    <div class="card yellow-card">
      <div class="inline-flex"><span class="card-label label-yellow">🟡 FINANCIAL — ACTION</span></div>
      <div class="card-title" style="margin-top:6px;">JetBlue Plus Card — Activate 8.99% Promo APR Before It Expires</div>
      <div class="card-meta">Source: JetBlue Plus Card (Barclays) &lt;info@emails.barclaysus.com&gt; · Wed Aug 12 · Rescued from Trash</div>
      <div class="card-body">You are one click away from activating a promotional 8.99% APR on purchases for your JetBlue Plus Card. Expiration date of the offer is not specified — act promptly to secure the rate.</div>
      <div class="card-row"><span class="card-label label-yellow">Next Step</span> <span>Open the Barclays email and click the activation link, or log into your Barclays account to activate the promo rate.</span></div>
      <div class="card-row"><span class="card-label label-yellow">Due</span> <span>ASAP — offer may expire soon</span></div>
    </div>

    <div class="card yellow-card">
      <div class="inline-flex"><span class="card-label label-yellow">🟡 FINANCIAL — MONITOR</span></div>
      <div class="card-title" style="margin-top:6px;">Bank of America — Billing Dispute Step 2 of 3 Complete (Merchant Credit Issued)</div>
      <div class="card-meta">Source: Bank of America &lt;onlinebanking@ealerts.bankofamerica.com&gt; · Thu Aug 13, 3:11 AM · Inbox</div>
      <div class="card-body">Your billing dispute for account ending <strong>-2994</strong> is progressing. Step 2 complete: merchant credit has been issued as of August 13. One more step (Step 3) remains. Monitor your account for final resolution.</div>
      <div class="card-row"><span class="card-label label-yellow">Next Step</span> <span>Log into Bank of America to confirm the credit posted and await Step 3 notification.</span></div>
      <div class="card-row"><span class="card-label label-yellow">Due</span> <span>Monitor this week</span></div>
    </div>

    <div class="card yellow-card">
      <div class="inline-flex"><span class="card-label label-yellow">🟡 SHOPPING — ACTION</span></div>
      <div class="card-title" style="margin-top:6px;">TikTok Shop — Order Canceled (Lost/Damaged) — Confirm Refund</div>
      <div class="card-meta">Source: TikTok Shop &lt;no-reply@shop-us.tiktok.com&gt; · Thu Aug 13, 6:17 AM · Inbox</div>
      <div class="card-body">Order <strong>#577508639223287836</strong> was canceled because the package was lost or damaged. A refund is reportedly on its way. Verify the refund posts to your account and consider reordering if the item is still needed.</div>
      <div class="card-row"><span class="card-label label-yellow">Next Step</span> <span>Check TikTok Shop account or payment method for refund confirmation within 3–5 business days.</span></div>
      <div class="card-row"><span class="card-label label-yellow">Due</span> <span>Monitor this week</span></div>
    </div>

    <div class="card blue-card">
      <div class="inline-flex"><span class="card-label label-blue">🔵 CALENDAR — RSVP NEEDED</span></div>
      <div class="card-title" style="margin-top:6px;">RSVP Now: HR Networking &amp; Job Search Open Office Hours — TODAY Noon</div>
      <div class="card-meta">Source: Google Calendar · Today 12:00–1:00 PM ET · Status: Needs Action</div>
      <div class="card-body">Your HR Networking Open Office Hours Zoom session starts in a few hours. Your RSVP is still pending ("needsAction"). This is a direct networking opportunity aligned with your job search. Decide: attend or decline now so organizers can plan.</div>
      <div class="card-row"><span class="card-label label-blue">Next Step</span> <span>Accept or decline on Google Calendar. If attending: <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1">Zoom link here</a>. Note: AI notetaking tools are not allowed per organizer.</span></div>
      <div class="card-row"><span class="card-label label-blue">Due</span> <span>Today — before noon</span></div>
    </div>

    <div class="card green-card">
      <div class="inline-flex"><span class="card-label label-green">🟢 JOB SEARCH — HIGH PRIORITY</span></div>
      <div class="card-title" style="margin-top:6px;">Apply / Respond: VP of Human Resources, The Americas — Soho House &amp; Co (Actively Recruiting)</div>
      <div class="card-meta">Source: LinkedIn Job Alerts · Thu Aug 13 · Inbox (2 alerts)</div>
      <div class="card-body">Soho House &amp; Co is <strong>actively recruiting</strong> for VP of Human Resources, The Americas — a senior leadership role directly aligned with your profile. Two separate job alerts were received, indicating high match. This is a top-tier opportunity.</div>
      <div class="card-row"><span class="card-label label-green">Next Step</span> <span>Open LinkedIn, review full JD, and apply today or send a connection request to the hiring team. Tailor your resume to hospitality/lifestyle brand leadership.</span></div>
      <div class="card-row"><span class="card-label label-green">Due</span> <span>Today — actively recruiting, roles fill fast</span></div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 4 — FULL 7-DAY CALENDAR
═══════════════════════════════════════════════════════════ -->
<div class="section blue">
  <div class="section-title">📅 Full 7-Day Calendar</div>
  <div class="section-body">

    <!-- TODAY -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Thursday, August 13, 2026 — TODAY</div>

      <div class="cal-event declined">
        <div class="inline-flex">
          <span class="cal-time">9:00 AM – 10:30 AM</span>
          <span class="cal-name">Executive Roundtable</span>
          <span class="cal-badge badge-declined">DECLINED</span>
        </div>
        <div class="cal-detail">📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09">Zoom — Meeting ID: 207 786 667 · PW: 205454</a></div>
        <div class="cal-detail">Host: John Madigan · You have declined this invitation.</div>
        <div class="cal-detail">⚠️ <strong>Conflict Note:</strong> Declined — no action needed unless you wish to reverse. No prep required.</div>
      </div>

      <div class="cal-event needs-action">
        <div class="inline-flex">
          <span class="cal-time">12:00 PM – 1:00 PM</span>
          <span class="cal-name">HR Networking &amp; Job Search: Open Office Hours (Zoom 2)</span>
          <span class="cal-badge badge-pending">⚠️ RSVP PENDING</span>
        </div>
        <div class="cal-detail">📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1">Zoom Link</a></div>
        <div class="cal-detail">~190+ attendees · Open discussion · AI notetaking tools NOT permitted per organizer.</div>
        <div class="cal-detail">🎯 <strong>Prep:</strong> Prepare a 30-second professional intro, 1–2 specific asks (introductions, referrals, role intel). Have LinkedIn open.</div>
        <div class="cal-detail">⚡ <strong>Action:</strong> RSVP now — accept or decline on Google Calendar.</div>
      </div>

      <div class="cal-event accepted">
        <div class="inline-flex">
          <span class="cal-time">3:30 PM – 4:30 PM</span>
          <span class="cal-name">m&amp;M</span>
          <span class="cal-badge badge-accepted">ACCEPTED</span>
        </div>
        <div class="cal-detail">📍 No location specified · With: monte.montoya@gmail.com</div>
        <div class="cal-detail">🎯 <strong>Prep:</strong> No description — confirm agenda with Monte in advance. Likely a 1:1 check-in or collaboration meeting.</div>
        <div class="cal-detail">✅ You are confirmed. No conflict.</div>
      </div>
    </div>

    <!-- Fri Aug 14 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Friday, August 14, 2026</div>
      <div class="cal-event confirmed" style="border-left-color:#ccc; opacity:0.7;">
        <div class="cal-name" style="color:#888;">No events scheduled.</div>
      </div>
    </div>

    <!-- Sat Aug 15 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Saturday, August 15, 2026</div>
      <div class="cal-event confirmed" style="border-left-color:#ccc; opacity:0.7;">
        <div class="cal-name" style="color:#888;">No events scheduled.</div>
      </div>
    </div>

    <!-- Sun Aug 16 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Sunday, August 16, 2026</div>
      <div class="cal-event confirmed" style="border-left-color:#ccc; opacity:0.7;">
        <div class="cal-name" style="color:#888;">No events scheduled.</div>
      </div>
    </div>

    <!-- Mon Aug 17 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Monday, August 17, 2026</div>
      <div class="cal-event confirmed" style="border-left-color:#ccc; opacity:0.7;">
        <div class="cal-name" style="color:#888;">No events scheduled.</div>
      </div>
    </div>

    <!-- Tue Aug 18 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Tuesday, August 18, 2026</div>

      <div class="cal-event confirmed">
        <div class="inline-flex">
          <span class="cal-time">10:00 AM – 11:00 AM</span>
          <span class="cal-name">Vet</span>
          <span class="cal-badge badge-confirmed">CONFIRMED</span>
        </div>
        <div class="cal-detail">📍 No location specified · No attendees listed</div>
        <div class="cal-detail">🐾 Note: "Stella vet" is a duplicate event at the exact same time — same appointment confirmed twice.</div>
      </div>

      <div class="cal-event confirmed">
        <div class="inline-flex">
          <span class="cal-time">10:00 AM – 11:00 AM</span>
          <span class="cal-name">Stella Vet</span>
          <span class="cal-badge badge-confirmed">CONFIRMED (duplicate)</span>
        </div>
        <div class="cal-detail">📍 No location specified · Duplicate of "Vet" above.</div>
        <div class="cal-detail">⚠️ <strong>Conflict Note:</strong> Two calendar entries for the same appointment. Consider deleting one to avoid confusion.</div>
        <div class="cal-detail">🎯 <strong>Prep:</strong> Confirm vet appointment address, bring Stella's records/vaccination history. Arrive 10 min early.</div>
      </div>
    </div>

    <!-- Wed Aug 19 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Wednesday, August 19, 2026</div>

      <div class="cal-event needs-action">
        <div class="inline-flex">
          <span class="cal-time">12:00 PM – 1:30 PM</span>
          <span class="cal-name">HR Networking &amp; Job Search Group — 2 Zoom</span>
          <span class="cal-badge badge-pending">⚠️ RSVP PENDING</span>
        </div>
        <div class="cal-detail">📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1">Zoom Link</a></div>
        <div class="cal-detail">~190+ attendees · Full networking group session (1.5 hrs) · Includes team resources + agenda prep.</div>
        <div class="cal-detail">⚡ <strong>Action:</strong> RSVP on Google Calendar. Review HR Networking Team Guidelines before joining.</div>
      </div>

      <div class="cal-event confirmed">
        <div class="inline-flex">
          <span class="cal-time">12:00 PM – 1:30 PM</span>
          <span class="cal-name">Network</span>
          <span class="cal-badge badge-confirmed">CONFIRMED (duplicate)</span>
        </div>
        <div class="cal-detail">📍 No location specified · Duplicate/personal reminder for the same Aug 19 networking event above.</div>
        <div class="cal-detail">⚠️ <strong>Conflict Note:</strong> Two calendar entries for this session — one confirmed personal block, one RSVP still pending on the group invite. Resolve the RSVP on the group event.</div>
      </div>
    </div>

    <div class="info-box" style="margin-top:12px;">
      📌 <strong>Calendar Housekeeping:</strong> You have two duplicate calendar entries — "Vet" + "Stella Vet" on Aug 18, and "Network" + "HR Networking Group" on Aug 19. Recommend deleting one of each. Also RSVP on both Aug 13 and Aug 19 HR Networking group events.
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 5 — JOB SEARCH & INTERVIEW PIPELINE
═══════════════════════════════════════════════════════════ -->
<div class="section green">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">

    <table>
      <thead>
        <tr><th>Fit</th><th>Role / Opportunity</th><th>Company</th><th>Source</th><th>Status</th><th>Next Step</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="card-label label-green">HIGH</span></td>
          <td>VP of Human Resources, The Americas</td>
          <td>Soho House &amp; Co</td>
          <td>LinkedIn Job Alerts (×2 alerts)</td>
          <td><span class="card-label label-red">Actively Recruiting</span></td>
          <td>Apply today on LinkedIn — role is live and filling fast.</td>
        </tr>
        <tr>
          <td><span class="card-label label-green">HIGH</span></td>
          <td>Head of HR (Application Acknowledged)</td>
          <td>Booking Holdings (Priceline)</td>
          <td>Workday email — rescued from Trash</td>
          <td><span class="card-label label-blue">Under Review</span></td>
          <td>Application received and under review. Monitor for next steps. Send a follow-up connection request to the HR team on LinkedIn if 1–2 weeks pass with no update.</td>
        </tr>
        <tr>
          <td><span class="card-label label-orange">MEDIUM</span></td>
          <td>People Partner, GTM</td>
          <td>Profound</td>
          <td>LinkedIn Job Alerts (×2 alerts)</td>
          <td><span class="card-label label-yellow">New Alert</span></td>
          <td>Review JD on LinkedIn. If aligned with your GTM/HRBP expertise, apply. Medium fit due to likely smaller company stage vs. senior experience.</td>
        </tr>
        <tr>
          <td><span class="card-label label-orange">MEDIUM</span></td>
          <td>Chief People Officer / Lead Talent / Culture / Change (5 new matches)</td>
          <td>Various</td>
          <td>JobLeads digest — in Trash</td>
          <td><span class="card-label label-gray">In Trash (digest)</span></td>
          <td>Restore email from Trash or visit JobLeads.com to review the 5 new matches for your saved CPO/Talent/Culture search.</td>
        </tr>
        <tr>
          <td><span class="card-label label-gray">LOW</span></td>
          <td>Games Jobs Direct — LinkedIn Post</td>
          <td>Various</td>
          <td>LinkedIn recommendations — Inbox</td>
          <td><span class="card-label label-gray">Informational</span></td>
          <td>Review only if gaming/entertainment industry is of interest. Otherwise, dismiss.</td>
        </tr>
      </tbody>
    </table>

    <hr class="divider">
    <div class="bold" style="margin-bottom:8px;">Networking Events — Active</div>
    <table>
      <thead><tr><th>Date</th><th>Event</th><th>RSVP Status</th><th>Notes</th></tr></thead>
      <tbody>
        <tr>
          <td>Today, Aug 13 · 12–1 PM</td>
          <td>HR Networking &amp; Job Search Open Office Hours (Zoom 2)</td>
          <td><span class="card-label label-yellow">Needs Action</span></td>
          <td>190+ HR professionals, job seekers. Strong networking opportunity. AI tools not permitted.</td>
        </tr>
        <tr>
          <td>Today, Aug 13 · 3:30–4:30 PM</td>
          <td>m&amp;M (Monte Montoya)</td>
          <td><span class="card-label label-green">Accepted</span></td>
          <td>1:1 with Monte — confirm agenda. Potential networking/collaboration touchpoint.</td>
        </tr>
        <tr>
          <td>Tue, Aug 19 · 12–1:30 PM</td>
          <td>HR Networking &amp; Job Search Group (Zoom 2)</td>
          <td><span class="card-label label-yellow">Needs Action</span></td>
          <td>Full group session, 1.5 hrs. Review team resources before attending.</td>
        </tr>
      </tbody>
    </table>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 6 — FULL EMAIL REVIEW BY CATEGORY
═══════════════════════════════════════════════════════════ -->
<div class="section navy">
  <div class="section-title">📂 Full Email Review by Category</div>
  <div class="section-body rounded">

    <!-- SECURITY / RISK -->
    <div class="card red-card">
      <div class="card-title">🔴 Security / Risk — 11 emails</div>
      <div class="card-meta">Most urgent category. Review immediately.</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>GitHub</td><td>[GitHub] Third-party OAuth app "MCP Market" added</td><td><span class="rescued-badge">✅ RESCUED</span></td><td>Verify/revoke at github.com/settings/applications</td></tr>
          <tr><td>Google (×9 events)</td><td>Google Account data shared with Slack (×6), Claude (×2), Blink.new (×1)</td><td><span class="rescued-badge">✅ RESCUED</span></td><td>Audit at myaccount.google.com/permissions — revoke unknowns</td></tr>
          <tr><td>'melissaw212' (spoof)</td><td>iCloud account block / payment expiry threat</td><td><span class="phishing-badge">🚫 AUTO-TRASHED — Phishing</span></td><td>Auto-removed. No action needed. Spoofed iCloud credential harvesting.</td></tr>
        </tbody>
      </table>
      <div class="note">Note: The 9 Google security notifications are counted as individual emails. Auto-trashed phishing = 1. Total in this category: 11.</div>
    </div>

    <!-- JOB SEARCH -->
    <div class="card green-card">
      <div class="card-title">🟢 Job Search — 6 emails</div>
      <div class="card-meta">Active opportunities — review and act today.</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>LinkedIn Job Alerts</td><td>VP of Human Resources, The Americas @ Soho House &amp; Co</td><td><span class="card-label label-blue">Inbox</span></td><td>Apply today — actively recruiting</td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>VP of Human Resources, The Americas @ Soho House &amp; Co (earlier)</td><td><span class="card-label label-blue">Inbox (read)</span></td><td>Duplicate — archive after acting on above</td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>People Partner, GTM at Profound</td><td><span class="card-label label-blue">Inbox</span></td><td>Review JD — medium fit</td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>People Partner, GTM at Profound (earlier)</td><td><span class="card-label label-blue">Inbox (read)</span></td><td>Duplicate — archive</td></tr>
          <tr><td>Workday / Booking Holdings</td><td>Thank you for your interest — Head of HR application</td><td><span class="rescued-badge">✅ RESCUED</span></td><td>Application under review — monitor</td></tr>
          <tr><td>JobLeads</td><td>5 new jobs: CPO / Lead Talent / Culture / Change</td><td><span class="card-label label-gray">Trash</span></td><td>Restore or visit JobLeads.com to review matches</td></tr>
        </tbody>
      </table>
    </div>

    <!-- RECRUITERS / NETWORKING -->
    <div class="card green-card">
      <div class="card-title">🟢 Recruiters / Networking — 2 emails</div>
      <div class="card-meta">LinkedIn professional updates and recommendations.</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>LinkedIn</td><td>View Games Jobs Direct's post and your next steps</td><td><span class="card-label label-blue">Inbox</span></td><td>Review if gaming industry is of interest; otherwise dismiss</td></tr>
          <tr><td>LinkedIn</td><td>Tamia Powell posted (L'Oréal HQ Paris)</td><td><span class="card-label label-gray">Trash</span></td><td>Informational — Like/comment to nurture relationship if relevant, then archive</td></tr>
        </tbody>
      </table>
    </div>

    <!-- CALENDAR / EVENTS -->
    <div class="card blue-card">
      <div class="card-title">🔵 Calendar / Events — 0 emails (events in Calendar section)</div>
      <div class="card-meta">All calendar-related items are managed under Section 4. No standalone calendar emails in this dataset.</div>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="card yellow-card">
      <div class="card-title">🟡 Financial / Billing — 2 emails</div>
      <div class="card-meta">Two actionable financial items.</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Bank of America</td><td>Billing Dispute -2994 — Merchant credit issued (Step 2 of 3)</td><td><span class="card-label label-blue">Inbox</span></td><td>Confirm credit posted; await Step 3</td></tr>
          <tr><td>JetBlue Plus Card (Barclays)</td><td>Activate 8.99% promo APR now</td><td><span class="rescued-badge">✅ RESCUED</span></td><td>Activate promo rate ASAP before offer expires</td></tr>
        </tbody>
      </table>
    </div>

    <!-- SHOPPING / ORDERS -->
    <div class="card yellow-card">
      <div class="card-title">🟡 Shopping / Orders — 4 emails</div>
      <div class="card-meta">Active orders and cancellation to monitor.</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Amazon.com</td><td>Shipped: 1 Storage item</td><td><span class="card-label label-blue">Inbox</span></td><td>Track delivery</td></tr>
          <tr><td>Amazon.com</td><td>Shipped: 1 Apparel item (06:02)</td><td><span class="card-label label-blue">Inbox</span></td><td>Track delivery</td></tr>
          <tr><td>Amazon.com</td><td>Shipped: 1 Apparel item (06:00)</td><td><span class="card-label label-blue">Inbox</span></td><td>Track delivery</td></tr>
          <tr><td>TikTok Shop</td><td>Order canceled — lost/damaged, refund coming</td><td><span class="card-label label-blue">Inbox</span></td><td>Confirm refund received; reorder if needed</td></tr>
        </tbody>
      </table>
    </div>

    <!-- PERSONAL -->
    <div class="card gray-card">
      <div class="card-title">👤 Personal — 2 emails</div>
      <div class="card-meta">Match.com dating app notifications.</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Match</td><td>Alexander likes you. See if it's mutual.</td><td><span class="card-label label-blue">Inbox</span></td><td>View at your leisure on Match.com</td></tr>
          <tr><td>Match</td><td>Profile view from Mike (56, Providence RI)</td><td><span class="card-label label-blue">Inbox</span></td><td>View at your leisure on Match.com</td></tr>
        </tbody>
      </table>
    </div>

    <!-- SLACK ACCOUNT ACTIVITY -->
    <div class="card purple-card">
      <div class="card-title">🟣 Slack Account Activity — 7 emails (in Trash)</div>
      <div class="card-meta">Series of Slack workspace creation and invitation emails — all in Trash. These relate to workspaces named "performance" and "perfomance chat" (note typo in latter).</div>
