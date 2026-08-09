<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa — Sunday, August 9, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 16px; padding: 36px 40px; margin-bottom: 28px; box-shadow: 0 4px 24px rgba(0,0,0,0.18); }
  .header h1 { font-size: 2rem; font-weight: 700; letter-spacing: -0.5px; }
  .header .sub { font-size: 1rem; color: #a8b8d8; margin-top: 6px; }
  .header .meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.08); border-radius: 10px; padding: 10px 18px; }
  .header .meta-item .label { font-size: 11px; color: #a8b8d8; text-transform: uppercase; letter-spacing: 1px; }
  .header .meta-item .value { font-size: 1.3rem; font-weight: 700; color: #e0eaff; }

  /* EXECUTIVE SUMMARY */
  .exec-summary { background: #fff; border-radius: 14px; padding: 24px 28px; margin-bottom: 24px; box-shadow: 0 2px 10px rgba(0,0,0,0.07); border-left: 5px solid #0f3460; }
  .exec-summary h2 { font-size: 1.1rem; font-weight: 700; color: #0f3460; margin-bottom: 14px; text-transform: uppercase; letter-spacing: 1px; }
  .exec-summary ul { list-style: none; }
  .exec-summary ul li { padding: 8px 0 8px 18px; border-bottom: 1px solid #f0f2f5; position: relative; font-size: 0.97rem; }
  .exec-summary ul li:last-child { border-bottom: none; }
  .exec-summary ul li::before { content: '▶'; position: absolute; left: 0; color: #0f3460; font-size: 10px; top: 11px; }

  /* SECTION HEADERS */
  .section-header { font-size: 1rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; padding: 10px 18px; border-radius: 8px 8px 0 0; margin-bottom: 0; }
  .section-wrap { margin-bottom: 28px; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.07); }

  /* COLOR THEMES */
  .red .section-header    { background: #c0392b; color: #fff; }
  .red .section-body      { background: #fff9f9; border: 1.5px solid #e8b4b4; border-top: none; border-radius: 0 0 12px 12px; padding: 18px 20px; }
  .yellow .section-header { background: #e67e22; color: #fff; }
  .yellow .section-body   { background: #fffdf5; border: 1.5px solid #f0d080; border-top: none; border-radius: 0 0 12px 12px; padding: 18px 20px; }
  .blue .section-header   { background: #1565c0; color: #fff; }
  .blue .section-body     { background: #f5f8ff; border: 1.5px solid #b3c8f0; border-top: none; border-radius: 0 0 12px 12px; padding: 18px 20px; }
  .green .section-header  { background: #1a7a4a; color: #fff; }
  .green .section-body    { background: #f4fff8; border: 1.5px solid #a8d8b8; border-top: none; border-radius: 0 0 12px 12px; padding: 18px 20px; }
  .purple .section-header { background: #6c3483; color: #fff; }
  .purple .section-body   { background: #fdf5ff; border: 1.5px solid #d5b0e8; border-top: none; border-radius: 0 0 12px 12px; padding: 18px 20px; }
  .gray .section-header   { background: #607d8b; color: #fff; }
  .gray .section-body     { background: #f8f9fa; border: 1.5px solid #cfd8dc; border-top: none; border-radius: 0 0 12px 12px; padding: 18px 20px; }
  .dark .section-header   { background: #37474f; color: #fff; }
  .dark .section-body     { background: #f5f5f5; border: 1.5px solid #b0bec5; border-top: none; border-radius: 0 0 12px 12px; padding: 18px 20px; }

  /* CARDS */
  .card { background: #fff; border-radius: 10px; padding: 16px 18px; margin-bottom: 12px; border-left: 4px solid #ccc; box-shadow: 0 1px 4px rgba(0,0,0,0.06); }
  .card.red-card    { border-left-color: #c0392b; }
  .card.yellow-card { border-left-color: #e67e22; }
  .card.blue-card   { border-left-color: #1565c0; }
  .card.green-card  { border-left-color: #1a7a4a; }
  .card.purple-card { border-left-color: #6c3483; }
  .card.gray-card   { border-left-color: #90a4ae; }
  .card h3 { font-size: 0.97rem; font-weight: 700; margin-bottom: 6px; }
  .card .meta-row { display: flex; flex-wrap: wrap; gap: 12px; font-size: 0.82rem; color: #555; margin-bottom: 6px; }
  .card .meta-row span { background: #f0f2f5; padding: 2px 8px; border-radius: 20px; }
  .card p { font-size: 0.88rem; color: #333; margin-bottom: 4px; }
  .card .next-step { background: #e8f4fd; border-left: 3px solid #1565c0; padding: 7px 10px; border-radius: 5px; font-size: 0.85rem; margin-top: 8px; color: #0d47a1; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 0.86rem; }
  th { background: #e8ecf4; color: #1a1a2e; font-weight: 700; padding: 9px 12px; text-align: left; border-bottom: 2px solid #c5cde0; }
  td { padding: 8px 12px; border-bottom: 1px solid #eef0f4; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f7f9ff; }
  .triage-table td:first-child { white-space: nowrap; }

  /* BADGES */
  .badge { display: inline-block; padding: 2px 9px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.3px; }
  .badge-red    { background: #fde8e8; color: #c0392b; }
  .badge-yellow { background: #fef3cd; color: #856404; }
  .badge-blue   { background: #dbeafe; color: #1565c0; }
  .badge-green  { background: #dcf5e4; color: #1a7a4a; }
  .badge-purple { background: #f3e8ff; color: #6c3483; }
  .badge-gray   { background: #eceff1; color: #546e7a; }
  .badge-high   { background: #fde8e8; color: #c0392b; }
  .badge-medium { background: #fef3cd; color: #856404; }
  .badge-low    { background: #eceff1; color: #546e7a; }

  /* TRIAGE TABLE */
  .triage-status-rescued  { color: #1a7a4a; font-weight: 700; }
  .triage-status-inbox    { color: #1565c0; font-weight: 700; }
  .triage-status-autotrash{ color: #c0392b; font-style: italic; }
  .triage-status-trash    { color: #607d8b; font-style: italic; }

  /* CALENDAR EVENTS */
  .cal-day { margin-bottom: 16px; }
  .cal-day-header { font-weight: 700; font-size: 0.95rem; color: #1565c0; background: #e8f0fe; padding: 6px 12px; border-radius: 6px; margin-bottom: 8px; }
  .cal-event { background: #fff; border: 1.5px solid #c5d8f8; border-radius: 8px; padding: 12px 14px; margin-bottom: 8px; display: flex; flex-direction: column; gap: 4px; }
  .cal-event .ev-title { font-weight: 700; font-size: 0.95rem; color: #1a1a2e; }
  .cal-event .ev-time  { font-size: 0.82rem; color: #1565c0; }
  .cal-event .ev-loc   { font-size: 0.82rem; color: #555; }
  .cal-event .ev-rsvp  { font-size: 0.8rem; }
  .cal-event .ev-prep  { font-size: 0.82rem; background: #fff8e1; border-left: 3px solid #f9a825; padding: 4px 8px; border-radius: 4px; color: #6d4c00; margin-top: 4px; }
  .cal-event .ev-conflict { font-size: 0.82rem; background: #fde8e8; border-left: 3px solid #c0392b; padding: 4px 8px; border-radius: 4px; color: #7b1c1c; margin-top: 4px; }
  .rsvp-confirmed   { color: #1a7a4a; font-weight: 700; }
  .rsvp-declined    { color: #c0392b; font-weight: 700; }
  .rsvp-needs       { color: #e67e22; font-weight: 700; }

  /* DASHBOARD GRID */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }
  .dash-card { background: #fff; border-radius: 10px; padding: 16px 18px; box-shadow: 0 1px 6px rgba(0,0,0,0.08); }
  .dash-card .dash-label { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; color: #888; margin-bottom: 6px; }
  .dash-card .dash-value { font-size: 1.5rem; font-weight: 800; }
  .dash-card .dash-detail { font-size: 0.82rem; color: #555; margin-top: 4px; }
  .dash-red    .dash-value { color: #c0392b; }
  .dash-yellow .dash-value { color: #e67e22; }
  .dash-blue   .dash-value { color: #1565c0; }
  .dash-green  .dash-value { color: #1a7a4a; }
  .dash-purple .dash-value { color: #6c3483; }
  .dash-gray   .dash-value { color: #607d8b; }

  /* PRIORITIES */
  .priority-list { counter-reset: pri; }
  .priority-item { display: flex; align-items: flex-start; gap: 14px; background: #fff; border-radius: 10px; padding: 16px 18px; margin-bottom: 12px; box-shadow: 0 1px 6px rgba(0,0,0,0.07); border-left: 5px solid #0f3460; }
  .priority-num { background: #0f3460; color: #fff; border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 1rem; flex-shrink: 0; }
  .priority-content h3 { font-size: 0.97rem; font-weight: 700; margin-bottom: 4px; }
  .priority-content p  { font-size: 0.87rem; color: #444; }

  /* MISC */
  .group-header { font-weight: 700; color: #1a1a2e; margin: 14px 0 6px; font-size: 0.93rem; border-bottom: 1.5px solid #e0e0e0; padding-bottom: 4px; }
  .snip { color: #666; font-size: 0.82rem; font-style: italic; }
  .auto-trash-note { background: #fde8e8; border: 1px solid #f5c6c6; border-radius: 6px; padding: 8px 12px; font-size: 0.82rem; color: #7b1c1c; margin-top: 6px; }
  .info-row { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 4px; }
  ul.simple { padding-left: 18px; }
  ul.simple li { margin-bottom: 4px; font-size: 0.88rem; }
  .count-chip { display: inline-block; background: #e8ecf4; border-radius: 20px; padding: 1px 10px; font-size: 0.8rem; font-weight: 700; color: #1a1a2e; margin-left: 6px; }
  .total-row td { font-weight: 800; background: #e8ecf4; }
  @media (max-width: 700px) {
    .header { padding: 20px 14px; }
    .header h1 { font-size: 1.3rem; }
    .header .meta { gap: 10px; }
    table { font-size: 0.78rem; }
  }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ═══════════════════════════════════════════════
     SECTION 0 — EMAIL TRIAGE QUICK LIST
═══════════════════════════════════════════════ -->
<div class="section-wrap blue">
  <div class="section-header">📋 Email Triage Quick List — All 50 Emails</div>
  <div class="section-body" style="padding:0;">
    <table class="triage-table">
      <thead>
        <tr>
          <th>Status</th>
          <th>From</th>
          <th>Subject</th>
          <th>One-Line Summary</th>
        </tr>
      </thead>
      <tbody>
        <!-- INBOX EMAILS (individual rows) -->
        <tr>
          <td class="triage-status-inbox">📥 INBOX</td>
          <td>Dylan's Diary (newsletter)</td>
          <td>Anthropic is building its own chips</td>
          <td>Tech/AI newsletter — Anthropic chip shortage response; in inbox, unread</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📥 INBOX</td>
          <td>Match</td>
          <td>Scott likes you. See if it's mutual.</td>
          <td>Match.com notification — Scott liked your profile</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📥 INBOX</td>
          <td>Google Business Profile</td>
          <td>DHW, your performance report for July 2026</td>
          <td>0 views for DHW on Google Business last month — needs attention</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📥 INBOX</td>
          <td>Notify NYC</td>
          <td>Missing Vulnerable Adult Alert — Anthony Fulgieri</td>
          <td>NYC emergency alert — 83-year-old missing from New Hyde Park area</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📥 INBOX</td>
          <td>Google Business Profile</td>
          <td>DHW Consulting, your performance report for July 2026</td>
          <td>0 views for DHW Consulting on Google Business — needs attention</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📥 INBOX</td>
          <td>Amazon.com</td>
          <td>Shipped: 1 Office item</td>
          <td>Amazon shipment confirmation — office item en route</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📥 INBOX</td>
          <td>Amazon.com</td>
          <td>Shipped: 1 Beverages item</td>
          <td>Amazon shipment confirmation — beverages item en route</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📥 INBOX</td>
          <td>Match</td>
          <td>Kennedy Andrew likes you. See if it's mutual.</td>
          <td>Match.com notification — Kennedy Andrew liked your profile</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📥 INBOX</td>
          <td>Match</td>
          <td>You've had a profile view from Peter</td>
          <td>Match.com — Peter (57, New Rochelle NY) viewed your profile</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📥 INBOX</td>
          <td>LinkedIn Job Alerts</td>
          <td>Senior People Partner at Superhuman: up to $255K/year</td>
          <td>LinkedIn job alert — Senior People Partner, Superhuman, 1 school alum</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📥 INBOX</td>
          <td>Amazon.com</td>
          <td>Shipped: 2 Office and Essentials items</td>
          <td>Amazon shipment confirmation — 2 office/essentials items en route</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📥 INBOX</td>
          <td>LinkedIn Job Alerts</td>
          <td>VP of People (HR) at K Health</td>
          <td>LinkedIn job alert — VP of People at K Health, 2 school alumni</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📥 INBOX</td>
          <td>Melissa W (self)</td>
          <td>(No subject — LinkedIn link)</td>
          <td>Self-sent note — link to LinkedIn post about Claude AI skills</td>
        </tr>
        <!-- SENT EMAILS (not in inbox, not trashed) -->
        <tr>
          <td class="triage-status-inbox">📤 SENT</td>
          <td>Melissa (self → Tracey)</td>
          <td>6 production sites, one retention problem</td>
          <td>Outreach email to Tracey re: automated facilities & client retention</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📤 SENT</td>
          <td>Melissa (self → Kelly)</td>
          <td>What happens to acquired talent once the deal closes</td>
          <td>Outreach email to Kelly re: Howden/Atlantic Group acquisition talent</td>
        </tr>
        <!-- OTHER NON-INBOX, NON-TRASH, NON-AUTO-TRASHED -->
        <tr>
          <td class="triage-status-inbox">📧 OTHER</td>
          <td>Serafina & Brasserie Cognac</td>
          <td>Two new restaurants, Hemingway & tennis pasta</td>
          <td>Restaurant newsletter — new locations in Tenafly and JFK; not in inbox</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📧 OTHER</td>
          <td>Amazon.com</td>
          <td>Ordered: 2 Nutrition & Wellness and Beverages items</td>
          <td>Amazon order confirmation — nutrition/beverages (read, not in inbox)</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📧 OTHER</td>
          <td>LinkedIn Job Alerts</td>
          <td>Head of People, US at Empathy</td>
          <td>LinkedIn job alert — Head of People at Empathy (actively recruiting)</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📧 OTHER</td>
          <td>LinkedIn</td>
          <td>You appeared in 2 searches this week</td>
          <td>LinkedIn profile visibility — appeared in 2 searches this week</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📧 OTHER</td>
          <td>LinkedIn Job Alerts</td>
          <td>Senior People Partner at Superhuman (duplicate)</td>
          <td>Duplicate LinkedIn job alert — Senior People Partner at Superhuman</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📧 OTHER</td>
          <td>Match</td>
          <td>Mitchell just sent you a new message 💌</td>
          <td>Match.com — Mitchell sent a message (read)</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📧 OTHER</td>
          <td>Match</td>
          <td>Kevin likes you. See if it's mutual.</td>
          <td>Match.com — Kevin liked your profile (read)</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📧 OTHER</td>
          <td>Match</td>
          <td>Salt likes you. See if it's mutual.</td>
          <td>Match.com — Salt liked your profile (unread, not in inbox)</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📧 OTHER</td>
          <td>Match</td>
          <td>You've had a profile view from Patrick</td>
          <td>Match.com — Patrick (57, New York NY) viewed your profile</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📧 OTHER</td>
          <td>Match</td>
          <td>Mitchell likes you. See if it's mutual.</td>
          <td>Match.com — Mitchell liked your profile (unread, not in inbox)</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📧 OTHER</td>
          <td>SHEIN</td>
          <td>Dreaming of a home transformation?</td>
          <td>SHEIN promotional — home décor; not in inbox, not trashed</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📧 OTHER</td>
          <td>Men's Sexual Clinic (spam)</td>
          <td>Harvard Scientists: Something Silent…</td>
          <td>Explicit spam — not auto-trashed, not in inbox; safe to delete</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📧 OTHER</td>
          <td>GLP-1 by-DirectMeds (spam)</td>
          <td>GLP-1 Medications Explained (copy 1)</td>
          <td>Unsolicited pharma spam — suspicious sender domain; safe to delete</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📧 OTHER</td>
          <td>GLP-1 by-DirectMeds (spam)</td>
          <td>GLP-1 Medications Explained (copy 2)</td>
          <td>Unsolicited pharma spam — duplicate; safe to delete</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📧 OTHER</td>
          <td>Sex Without Censorship (spam)</td>
          <td>Sydney Sweeney's secret…</td>
          <td>Explicit spam — random domain; safe to delete</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📧 OTHER</td>
          <td>Mens Health (spam)</td>
          <td>Porn star method for bigger erections</td>
          <td>Explicit spam — random domain; safe to delete</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📧 OTHER</td>
          <td>🔥🍆 Sex.Trick (spam)</td>
          <td>1 simple trick is turning men into… (obfuscated)</td>
          <td>Explicit spam — obfuscated sender; safe to delete</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📧 OTHER</td>
          <td>Sex.Trick (spam)</td>
          <td>The safest "before sex" trick…</td>
          <td>Explicit spam — Epstein-lure variation; safe to delete</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📧 OTHER</td>
          <td>F*ckMeHard (spam)</td>
          <td>I want you f*ck me right now… (obfuscated)</td>
          <td>Explicit spam — obfuscated subject; safe to delete</td>
        </tr>
        <tr>
          <td class="triage-status-inbox">📧 OTHER</td>
          <td>Sex Trick (spam)</td>
          <td>Make her squirt 3x tonight…</td>
          <td>Explicit spam — random domain; safe to delete</td>
        </tr>
        <!-- AUTO-TRASHED SUMMARY ROW -->
        <tr style="background:#fde8e8;">
          <td class="triage-status-autotrash">🗑 AUTO-TRASHED (Phishing)</td>
          <td colspan="3"><strong>4 emails auto-trashed as high-confidence phishing</strong> — Casino payment spoofed as "melissaw212," Casino deposit spoofed as "melissaw212," Cloud ID lock spoofed as "melissaw212," Fake cloud storage full from random domain. See Trash Review for full details.</td>
        </tr>
        <!-- MANUAL TRASH SUMMARY ROW -->
        <tr style="background:#eceff1;">
          <td class="triage-status-trash">🗂 TRASH (manual)</td>
          <td colspan="3"><strong>9 emails in Trash</strong> — CVS sale, Kohl's sale, YesStyle promo, VIVAIA promo, SHEIN promo, Temu promo, Old Navy cart, Glassdoor jobs (newsletter-trashed), Alison Courses (newsletter-trashed), JobLeads (newsletter-trashed). See Trash Review for full details.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 1 — HEADER
═══════════════════════════════════════════════ -->
<div class="header">
  <h1>Good Morning, Melissa ☀️</h1>
  <div class="sub">Executive Briefing prepared by your Chief of Staff</div>
  <div class="meta">
    <div class="meta-item">
      <div class="label">Date</div>
      <div class="value">Sunday, August 9, 2026</div>
    </div>
    <div class="meta-item">
      <div class="label">Total Emails Reviewed</div>
      <div class="value">50</div>
    </div>
    <div class="meta-item">
      <div class="label">Calendar Events</div>
      <div class="value">7</div>
    </div>
    <div class="meta-item">
      <div class="label">Action Required</div>
      <div class="value">6 Items</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 2 — EXECUTIVE SUMMARY
═══════════════════════════════════════════════ -->
<div class="exec-summary">
  <h2>⚡ Executive Summary</h2>
  <ul>
    <li><strong>🔴 Biggest Risk:</strong> Four confirmed phishing emails were auto-trashed — all spoofing your own Gmail address (melissaw212) — including two fake casino payment confirmations and two fake cloud storage alerts. No action needed on those, but your email address may be circulating in spam networks. Additionally, a cascade of explicit sexual spam suggests your address has been sold to low-quality lists; consider a spam filter review.</li>
    <li><strong>🟢 Biggest Opportunity:</strong> Three strong LinkedIn job leads arrived overnight — VP of People at K Health, Senior People Partner at Superhuman (up to $255K, 1 school alum), and Head of People, US at Empathy — plus your Tuesday HR Networking & Job Search Group Zoom requires an RSVP. Two outbound cold outreach emails (to Tracey and Kelly) went out today, which is excellent momentum.</li>
    <li><strong>🔵 Biggest Calendar Item:</strong> Back-to-back medical commitments this week — Stephanie's infusion Monday 8 AM, your Brain MRI (W&WO IVC) at 159 E 53rd St Tuesday at 9:20 AM (arrive 8:50), and PT Wednesday 9:30 AM — confirm all logistics and prepare MRI checklist (remove body piercings, no valuables). Also, two networking Zooms on Wednesday and Thursday need RSVPs.</li>
  </ul>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 3 — ACTION REQUIRED
═══════════════════════════════════════════════ -->
<div class="section-wrap yellow">
  <div class="section-header">⚠️ Action Required</div>
  <div class="section-body">

    <div class="card yellow-card">
      <h3>🗓️ RSVP Required — HR Networking & Job Search Group Zoom</h3>
      <div class="meta-row">
        <span>Source: Google Calendar</span><span>Status: Needs Action</span><span>Due: Wednesday Aug 12, 12:00–1:30 PM</span>
      </div>
      <p><strong>Why it matters:</strong> You have not responded to this calendar invite. The group has 170+ attendees and is a core part of your job search network. Your attendance status is unconfirmed.</p>
      <div class="next-step">➡ Accept or decline the Zoom invite. Link: https://us06web.zoom.us/j/81954171722 — Confirm by Tuesday.</div>
    </div>

    <div class="card yellow-card">
      <h3>🗓️ RSVP Required — HR Networking Open Office Hours Zoom</h3>
      <div class="meta-row">
        <span>Source: Google Calendar</span><span>Status: Needs Action</span><span>Due: Thursday Aug 13, 12:00–1:00 PM</span>
      </div>
      <p><strong>Why it matters:</strong> Second networking session this week, same large HR group. No RSVP submitted. Per the invite, turn off AI notetaking tools — open discussion format.</p>
      <div class="next-step">➡ Accept or decline. Link: https://us06web.zoom.us/j/85945371140 — Confirm by Wednesday.</div>
    </div>

    <div class="card blue-card">
      <h3>🏥 MRI Appointment Prep — Brain MRI W&WO IVC</h3>
      <div class="meta-row">
        <span>Source: Google Calendar</span><span>Tuesday Aug 11, Arrive 8:50 AM / Appt 9:20 AM</span><span>159 E 53rd St, 6th Floor, NY 10022</span>
      </div>
      <p><strong>Why it matters:</strong> This is a medical procedure with specific instructions — remove all body piercings, leave valuables at home, arrive early for a private dressing room with locker. Phone: 646-754-2800.</p>
      <div class="next-step">➡ Prepare tonight: remove jewelry, arrange transport, confirm nothing to reschedule. Arrive no later than 8:45 AM.</div>
    </div>

    <div class="card green-card">
      <h3>💼 Review & Apply — VP of People at K Health</h3>
      <div class="meta-row">
        <span>Source: LinkedIn Job Alerts</span><span>2 school alumni at K Health</span><span>Today — Aug 9</span>
      </div>
      <p><strong>Why it matters:</strong> VP-level People role at a growing health-tech company. Two school alumni are there — warm introduction potential. Strong fit signal.</p>
      <div class="next-step">➡ Review the full posting on LinkedIn, check your alumni connections at K Health, and apply or reach out to an alum for a referral this week.</div>
    </div>

    <div class="card green-card">
      <h3>💼 Review & Apply — Senior People Partner at Superhuman ($255K)</h3>
      <div class="meta-row">
        <span>Source: LinkedIn Job Alerts</span><span>1 school alum at Superhuman</span><span>Today — Aug 9</span>
      </div>
      <p><strong>Why it matters:</strong> High-compensation role (up to $255K) at a fast-growing productivity startup. 1 school alumni connection available. Appeared in two separate alert emails — strong signal of relevance.</p>
      <div class="next-step">➡ Review the posting, message your school alum at Superhuman, and apply today while the listing is fresh.</div>
    </div>

    <div class="card yellow-card">
      <h3>📊 Google Business Profile — 0 Views (DHW & DHW Consulting)</h3>
      <div class="meta-row">
        <span>Source: Google Business Profile (2 emails)</span><span>July 2026 Performance Reports</span>
      </div>
      <p><strong>Why it matters:</strong> Both DHW and DHW Consulting had zero Google Business Profile views in July. This is a visibility gap that directly impacts inbound lead generation for consulting work.</p>
      <div class="next-step">➡ Log into Google Business Profile, update posts, add photos or offers, and verify contact information is current. Consider a short-term keyword optimization effort.</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 4 — FULL 7-DAY CALENDAR
═══════════════════════════════════════════════ -->
<div class="section-wrap blue">
  <div class="section-header">📅 Full 7-Day Calendar — Aug 9–15, 2026</div>
  <div class="section-body">

    <div class="cal-day">
      <div class="cal-day-header">Sunday, August 9 (Today)</div>
      <div style="font-size:0.88rem;color:#607d8b;padding:8px 4px;">No calendar events scheduled today. Use this time to review job leads, RSVPs, and MRI prep.</div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">Monday, August 10</div>
      <div class="cal-event">
        <div class="ev-title">💉 Stephanie Infusion</div>
        <div class="ev-time">⏰ 8:00 AM – 9:00 AM</div>
        <div class="ev-loc">📍 Location not specified</div>
        <div class="ev-rsvp"><span class="rsvp-confirmed">✅ Confirmed</span> — No other attendees listed</div>
        <div class="ev-prep">🗒 Prep: Confirm location/facility if not embedded elsewhere. Allow travel time. This may be related to an ongoing treatment regimen for Stephanie.</div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">Tuesday, August 11</div>
      <div class="cal-event">
        <div class="ev-title">🧠 MRI Brain W&WO IVC</div>
        <div class="ev-time">⏰ Arrive 8:50 AM | Appointment: 9:20 AM – 9:40 AM block</div>
        <div class="ev-loc">📍 159 E 53rd Street, 6th Floor, New York NY 10022 | ☎ 646-754-2800</div>
        <div class="ev-rsvp"><span class="rsvp-confirmed">✅ Confirmed</span></div>
        <div class="ev-prep">🗒 Prep: Remove ALL body piercings before arrival. Leave valuables at home. Gown provided. Private dressing room/locker available. Arrive no later than 8:45 AM to allow check-in time. Confirm no metal implants, pacemakers, or contraindications with ordering physician.</div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">Wednesday, August 12</div>
      <div class="cal-event">
        <div class="ev-title">🏃 PT (Physical Therapy)</div>
        <div class="ev-time">⏰ 9:30 AM – 10:30 AM</div>
        <div class="ev-loc">📍 Location not specified</div>
        <div class="ev-rsvp"><span class="rsvp-confirmed">✅ Confirmed</span></div>
        <div class="ev-prep">🗒 Prep: Wear comfortable workout clothing. Ends at 10:30 — 1.5 hours before networking Zoom at noon. Comfortable buffer.</div>
      </div>
      <div class="cal-event">
        <div class="ev-title">🤝 HR Networking & Job Search Group — Zoom 2</div>
        <div class="ev-time">⏰ 12:00 PM – 1:30 PM</div>
        <div class="ev-loc">🔗 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" style="color:#1565c0;">Zoom Link</a></div>
        <div class="ev-rsvp"><span class="rsvp-needs">⚠️ RSVP NEEDED — Needs Action</span> | ~170+ attendees</div>
        <div class="ev-prep">🗒 Prep: Review HR Networking Team Guidelines linked in calendar description. Prepare a concise professional update/elevator pitch. Have resume and LinkedIn ready for follow-up connections.</div>
        <div class="ev-conflict">⚠️ Note: A separate "Network" calendar block is also set for 12:00 PM – 1:30 PM on this day with no details — this appears to be a duplicate or placeholder for the same event. No conflict.</div>
      </div>
      <div class="cal-event">
        <div class="ev-title">📌 Network (placeholder)</div>
        <div class="ev-time">⏰ 12:00 PM – 1:30 PM</div>
        <div class="ev-loc">📍 No location</div>
        <div class="ev-rsvp"><span class="rsvp-confirmed">✅ Confirmed</span> — Appears to be a personal placeholder/duplicate for the HR Networking Zoom above</div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">Thursday, August 13</div>
      <div class="cal-event">
        <div class="ev-title">🏛 Executive Roundtable (John Madigan — Zoom)</div>
        <div class="ev-time">⏰ 9:00 AM – 10:30 AM</div>
        <div class="ev-loc">🔗 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" style="color:#1565c0;">Zoom Link</a> | ID: 207 786 667 | PW: 205454</div>
        <div class="ev-rsvp"><span class="rsvp-declined">❌ DECLINED</span> — You have declined this invite</div>
        <div class="ev-prep">🗒 Note: You have declined. If circumstances have changed and you wish to attend, contact John Madigan to re-accept. Otherwise, no action needed.</div>
      </div>
      <div class="cal-event">
        <div class="ev-title">🤝 HR Networking & Job Search: Open Office Hours — Zoom 2</div>
        <div class="ev-time">⏰ 12:00 PM – 1:00 PM</div>
        <div class="ev-loc">🔗 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" style="color:#1565c0;">Zoom Link</a></div>
        <div class="ev-rsvp"><span class="rsvp-needs">⚠️ RSVP NEEDED — Needs Action</span> | ~170+ attendees</div>
        <div class="ev-prep">🗒 Prep: Per invite — turn OFF automated AI notetaking tools. Open discussion format. No recording. Good opportunity for candid networking and peer support.</div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">Friday, August 14 — Sunday, August 15</div>
      <div style="font-size:0.88rem;color:#607d8b;padding:8px 4px;">No calendar events scheduled. Use for job application follow-ups, rest, or planning the week ahead.</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 5 — JOB SEARCH & INTERVIEW PIPELINE
═══════════════════════════════════════════════ -->
<div class="section-wrap green">
  <div class="section-header">💼 Job Search & Interview Pipeline</div>
  <div class="section-body">

    <div class="group-header">🔔 LinkedIn Job Alerts (New Today)</div>
    <table>
      <thead>
        <tr><th>Role</th><th>Company</th><th>Signal</th><th>Fit</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>VP of People (HR)</strong></td>
          <td>K Health</td>
          <td>2 school alumni</td>
          <td><span class="badge badge-high">HIGH</span></td>
          <td>Apply + reach out to alumni this week</td>
        </tr>
        <tr>
          <td><strong>Senior People Partner</strong></td>
          <td>Superhuman</td>
          <td>Up to $255K · 1 school alum · appeared twice</td>
          <td><span class="badge badge-high">HIGH</span></td>
          <td>Apply today + message school alum</td>
        </tr>
        <tr>
          <td><strong>Head of People, US</strong></td>
          <td>Empathy</td>
          <td>Actively recruiting</td>
          <td><span class="badge badge-medium">MEDIUM</span></td>
          <td>Review posting and apply if strong fit</td>
        </tr>
      </tbody>
    </table>

    <div class="group-header" style="margin-top:18px;">📋 Glassdoor Job Alerts</div>
    <table>
      <thead>
        <tr><th>Role / Batch</th><th>Source</th><th>Status</th><th>Fit</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>HR Director (Remote) at Maximus + 8 more (Remote, US)</td>
          <td>Glassdoor (auto-trashed as newsletter)</td>
          <td>In Trash</td>
          <td><span class="badge badge-medium">MEDIUM</span></td>
          <td>Retrieve from trash to review Maximus listing; others low priority</td>
        </tr>
        <tr>
          <td>Asst. Community Manager at Twin Pines + 8 more (NYC)</td>
          <td>Glassdoor (newsletter-trashed)</td>
          <td>In Trash</td>
          <td><span class="badge badge-low">LOW</span></td>
          <td>Community Manager likely below level — skip; review others if time permits</td>
        </tr>
      </tbody>
    </table>

    <div class="group-header" style="margin-top:18px;">📋 JobLeads Alert (Auto-Trashed as Newsletter)</div>
    <table>
      <thead>
        <tr><th>Search</th><th>Count</th><th>Status</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Chief People Officer / Lead Talent / Culture Change</td>
          <td>5 new jobs for Aug 8</td>
          <td>In Trash (newsletter-trashed)</td>
          <td>Restore and review — CPO-level roles are directly relevant</td>
        </tr>
      </tbody>
    </table>

    <div class="group-header" style="margin-top:18px;">🤝 Networking Events This Week</div>
    <table>
      <thead>
        <tr><th>Event</th><th>Date/Time</th><th>RSVP Status</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>HR Networking & Job Search Group — Zoom 2</td>
          <td>Wed Aug 12, 12–1:30 PM</td>
          <td><span class="badge badge-yellow">NEEDS ACTION</span></td>
          <td>RSVP immediately</td>
        </tr>
        <tr>
          <td>HR Networking Open Office Hours — Zoom 2</td>
          <td>Thu Aug 13, 12–1:00 PM</td>
          <td><span class="badge badge-yellow">NEEDS ACTION</span></td>
          <td>RSVP; remember to disable AI notetaking</td>
        </tr>
      </tbody>
    </table>

    <div class="group-header" style="margin-top:18px;">📤 Outbound Outreach Sent Today</div>
    <table>
      <thead>
        <tr><th>To</th><th>Subject</th><th>Key Points</th><th>Next Step</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Tracey</td>
          <td>6 production sites, one retention problem</td>
          <td>6 highly automated production facilities; business moving clients toward retention solutions</td>
          <td>Follow up in 3–5 business days if no response</td>
        </tr>
        <tr>
          <td>Kelly</td>
          <td>What happens to acquired talent once the deal closes</td>
          <td>Howden/Atlantic Group acquisition (Jan); $703M raised Feb; talent integration angle</td>
          <td>Follow up in 3–5 business days if no response</td>
        </tr>
      </tbody>
    </table>

    <div class="group-header" style="margin-top:18px;">📊 LinkedIn Visibility</div>
    <div class="card green-card">
      <h3>You appeared in 2 searches this week</h3>
      <p>Source: LinkedIn notifications. Your profile is being found — consistent with active recruiter activity. Continue optimizing headline and open-to-work settings.</p>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 6 — FULL EMAIL REVIEW BY CATEGORY
═══════════════════════════════════════════════ -->
<div class="section-wrap red">
  <div class="section-header">🔐 Security / Risk</div>
  <div class="section-body">
    <p><strong>Count: 9 emails</strong> (4 auto-trashed phishing + 5 explicit/suspicious spam)</p>
    <div class="group-header">🛑 Auto-Trashed Phishing (4 emails — no action needed)</div>
    <div class="card red-card">
      <h3>Casino Payment Spoofed as "melissaw212" — $3,000</h3>
      <div class="meta-row"><span>From: rumiwlthxwbnns…@pktgwk.osntah.biqr75.us</span><span>Auto-Trashed ✅</span></div>
      <div class="auto-trash-note">Auto-Trash Reason: Spoofed sender display name impersonating melissaw212 from a random domain; fake casino payment confirmation ($3,000) designed to harvest account/financial info.</div>
    </div>
    <div class="card red-card">
      <h3>Casino Direct Deposit Spoofed as "💲melissaw212💲" — $13,963.99</h3>
      <div class="meta-row"><span>From: casbz@dripozyiqpubpipdissfwboxhv.net</span><span>Auto-Trashed ✅</span></div>
      <div class="auto-trash-note">Auto-Trash Reason: Spoofed display name impersonating melissaw212; fake large direct deposit ($13,963.99) casino confirmation with unrendered template variables — advance-fee/credential-harvesting lure.</div>
    </div>
    <div class="card red-card">
      <h3>Fake Cloud ID Locked — "melissaw212, Your Cloud ID has been locked"</h3>
      <div class="meta-row"><span>From: lgvgksjpviwwnf…@5lghii.r1312l.rigigi.us</span><span>Auto-Trashed ✅</span></div>
      <div class="auto-trash-note">Auto-Trash Reason: Spoofed sender impersonating melissaw212 from random domain; fake cloud storage locked/payment failure urgency threat — credential/payment harvesting.</div>
    </div>
    <div class="card red-card">
      <h3>Fake Google Storage Full — "Action Required: Storage 100% Full"</h3>
      <div class="meta-row"><span>From: hjrsupportzxw@exzzfmckrkbcpcomcpkoujwy.com</span><span>Auto-Trashed ✅</span></div>
      <div class="auto-trash-note">Auto-Trash Reason: Spoofed 'Cloud_Storage' sender from random domain; fake Google-style storage-full alert — classic credential-harvesting phishing lure.</div>
    </div>

    <div class="group-header" style="margin-top:14px;">⚠️ Explicit Spam / Suspicious (5 emails — Safe to Delete)</div>
    <table>
      <thead><tr><th>Sender</th><th>Subject (Summary)</th><th>Recommendation</th></tr></thead>
      <tbody>
        <tr><td>Men's Sexual Clinic (random domain)</td><td>"Harvard Scientists: Something Silent Has Been Destroying Your Penis's Blood Flow"</td><td><span class="badge badge-red">Delete</span></td></tr>
        <tr><td>GLP-1 by-DirectMeds (random domain) × 2</td><td>"GLP-1 Medications Explained: How They Help You Lose Weight" (2 copies)</td><td><span class="badge badge-red">Delete Both</span></td></tr>
        <tr><td>Sex Without Censorship (random domain)</td><td>"Sydney Sweeney's secret that keeps men hard for hours"</td><td><span class="badge badge-red">Delete</span></td></tr>
        <tr><td>Mens Health (random domain)</td><td>"Porn star method for bigger, hours long erections?"</td><td><span class="badge badge-red">Delete</span></td></tr>
        <tr><td>🔥🍆 Get_Hard (obfuscated, random domain)</td><td>"1 simple trick is turning men into unstoppable sex machines" (obfuscated)</td><td><span class="badge badge-red">Delete</span></td></tr>
        <tr><td>Sex.Trick (random domain)</td><td>"The safest 'before sex' trick you've never tried"</td><td><span class="badge badge-red">Delete</span></td></tr>
        <tr><td>F*ckMeHard (random domain)</td><td>Obfuscated explicit solicitation</td><td><span class="badge badge-red">Delete</span></td></tr>
        <tr><td>'Sex Trick' (random domain)</td><td>"Make her squirt 3x tonight with this porn star secret"</td><td><span class="badge badge-red">Delete</span></td></tr>
      </tbody>
    </table>
    <p style="margin-top:10px;font-size:0.85rem;color:#7b1c1c;"><strong>Note:</strong> The high volume of explicit spam and address-spoofing phishing suggests your email address may be circulating in low-quality and malicious mailing lists. Consider enabling stronger spam filters or using a secondary email address for public-facing accounts.</p>
  </div>
</div>

<div class="section-wrap green">
  <div class="section-header">💼 Job Search</div>
  <div class="section-body">
    <p><strong>Count: 8 emails</strong> — LinkedIn alerts (4), Glassdoor alerts (2, trashed), JobLeads (1, trashed), LinkedIn search appearance (1)</p>
    <table>
      <thead><tr><th>Source</th><th>Role</th><th>Status</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>LinkedIn Job Alerts</td><td>Senior People Partner — Superhuman ($255K, 1 alum) [×2 alerts]</td><td><span class="badge badge-green">Inbox</span></td><td>Apply today</td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>VP of People (HR) — K Health (2 alumni)</td><td><span class="badge badge-green">Inbox</span></td><td>Apply + alumni outreach</td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>Head of People, US — Empathy (actively recruiting)</td><td><span class="badge badge-gray">Other</span></td><td>Review and apply</td></tr>
        <tr><td>LinkedIn</td><td>You appeared in 2 searches this week</td><td><span class="badge badge-gray">Other</span></td><td>Monitor; optimize profile</td></tr>
        <tr><td>Glassdoor</td><td>HR Director (Remote) at Maximus + 8 more</td><td><span class="badge badge-gray">Trashed</span></td><td>Restore; review Maximus</td></tr>
        <tr><td>Glassdoor</td><td>Asst. Community Manager at Twin Pines + 8 more (NYC)</td><td><span class="badge badge-gray">Trashed</span></td><td>Low fit; skip</td></tr>
        <tr><td>JobLeads</td><td>5 new CPO / Talent / Culture Change jobs (Aug 8)</td><td><span class="badge badge-gray">Trashed</span></td><td>Restore; review CPO listings</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="section-wrap green">
  <div class="section-header">🤝 Recruiters / Networking / Outreach</div>
  <div class="section-body">
    <p><strong>Count: 2 emails sent by Melissa (outbound cold outreach)</strong></p>
    <div class="card green-card">
      <h3>Outbound to Tracey — "6 production sites, one retention problem"</h3>
      <p>Melissa initiated outreach to Tracey about a business with 6 automated production facilities facing a client retention challenge. Sent Aug 9 at 7:30 PM.</p>
      <div class="next-step">➡ Log in CRM/tracker. Follow up in 3–5 business days if no reply.</div>
    </div>
    <div class="card green-card">
      <h3>Outbound to Kelly — "What happens to acquired talent once the deal closes"</h3>
      <p>Melissa initiated outreach to Kelly framing the Howden/Atlantic Group acquisition context (closed Jan, $703M raised Feb) around acquired talent integration — a strategic HR consulting angle.</p>
      <div class="next-step">➡ Log in CRM/tracker. Follow up in 3–5 business days if no reply.</div>
    </div>
  </div>
</div>

<div class="section-wrap blue">
  <div class="section-header">📅 Calendar / Events</div>
  <div class="section-body">
    <p><strong>Count: 2 emails</strong> — Notify NYC alert; Executive Roundtable (declined)</p>
    <div class="card blue-card">
      <h3>🚨 Notify NYC — Missing Vulnerable Adult Alert: Anthony Fulgieri</h3>
      <div class="meta-row"><span>Issued: Aug 9, 2026 at 2:57 AM</span><span>83-year-old white male, New Hyde Park area</span></div>
      <p>Standard NYC emergency notification — informational only. No action required unless you have relevant information to report.</p>
      <div class="next-step">➡ No action needed. File away or delete after reading.</div>
    </div>
    <div class="card blue-card">
      <h3>Executive Roundtable — John Madigan (Zoom)</h3>
      <p>Calendar invite — you have declined. Thu Aug 13, 9:00–10:30 AM. If you wish to reconsider, contact John Madigan before the date.</p>
    </div>
  </div>
</div>

<div class="section-wrap red">
  <div class="section-header">🏥 Medical / Health</div>
  <div class="section-body">
    <p><strong>Count: 3 calendar events (Stephanie Infusion, MRI, PT) — no medical emails in inbox.</strong></p>
    <p style="font-size:0.88rem;">All medical items are captured in the calendar section. See Full 7-Day Calendar for complete details and prep notes. Key item: Brain MRI Tuesday Aug 11 at 159 E 53rd St — prepare tonight.</p>
  </div>
</div>

<div class="
