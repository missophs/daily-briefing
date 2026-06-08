<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing – Melissa | Monday, June 8, 2026</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px 24px; margin-bottom: 24px; }
  .header h1 { font-size: 2rem; font-weight: 700; letter-spacing: -0.5px; }
  .header .sub { font-size: 1rem; color: #a8b8d8; margin-top: 4px; }
  .header .meta-row { display: flex; gap: 28px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-box { background: rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 20px; text-align: center; }
  .header .meta-box .num { font-size: 1.5rem; font-weight: 700; color: #e0f0ff; }
  .header .meta-box .lbl { font-size: 0.75rem; color: #a8b8d8; text-transform: uppercase; letter-spacing: 0.5px; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 1.05rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; padding: 10px 16px; border-radius: 8px 8px 0 0; margin-bottom: 0; }
  .section-body { background: #fff; border-radius: 0 0 10px 10px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .section-wrap { border-radius: 10px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.07); margin-bottom: 28px; }

  /* COLOR THEMES */
  .red .section-title    { background: #c0392b; color: #fff; }
  .yellow .section-title { background: #e67e22; color: #fff; }
  .blue .section-title   { background: #2980b9; color: #fff; }
  .green .section-title  { background: #27ae60; color: #fff; }
  .purple .section-title { background: #8e44ad; color: #fff; }
  .gray .section-title   { background: #7f8c8d; color: #fff; }
  .navy .section-title   { background: #1a1a2e; color: #fff; }
  .teal .section-title   { background: #16a085; color: #fff; }

  /* EXEC SUMMARY */
  .exec-bullets { list-style: none; padding: 0; }
  .exec-bullets li { display: flex; align-items: flex-start; gap: 12px; padding: 10px 0; border-bottom: 1px solid #f0f2f5; }
  .exec-bullets li:last-child { border-bottom: none; }
  .exec-bullet-icon { font-size: 1.3rem; min-width: 28px; text-align: center; }
  .exec-bullet-text strong { display: block; font-size: 0.95rem; }
  .exec-bullet-text span { color: #555; font-size: 0.88rem; }

  /* ACTION CARDS */
  .action-cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; }
  .action-card { border-radius: 10px; padding: 16px; border-left: 5px solid #ccc; background: #fafafa; box-shadow: 0 1px 6px rgba(0,0,0,0.06); }
  .action-card.red-card    { border-left-color: #c0392b; background: #fff5f5; }
  .action-card.yellow-card { border-left-color: #e67e22; background: #fffbf0; }
  .action-card.green-card  { border-left-color: #27ae60; background: #f0fff4; }
  .action-card.blue-card   { border-left-color: #2980b9; background: #f0f8ff; }
  .action-card.purple-card { border-left-color: #8e44ad; background: #faf0ff; }
  .action-card .card-label { font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 6px; }
  .action-card .card-title { font-size: 0.97rem; font-weight: 700; margin-bottom: 8px; }
  .action-card .card-row { display: flex; gap: 6px; font-size: 0.82rem; margin-bottom: 3px; color: #444; }
  .action-card .card-row strong { min-width: 90px; color: #222; }
  .red-card .card-label    { color: #c0392b; }
  .yellow-card .card-label { color: #e67e22; }
  .green-card .card-label  { color: #27ae60; }
  .blue-card .card-label   { color: #2980b9; }
  .purple-card .card-label { color: #8e44ad; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { background: #16213e; color: #fff; padding: 7px 14px; border-radius: 6px; font-weight: 700; font-size: 0.88rem; margin-bottom: 8px; display: flex; justify-content: space-between; }
  .cal-event { background: #f7f9fc; border-radius: 8px; padding: 12px 14px; margin-bottom: 8px; border-left: 4px solid #2980b9; }
  .cal-event.declined { border-left-color: #e74c3c; background: #fff5f5; }
  .cal-event.needs-action { border-left-color: #e67e22; background: #fffbf0; }
  .cal-event.confirmed { border-left-color: #27ae60; background: #f0fff4; }
  .cal-event.accepted  { border-left-color: #2980b9; background: #f0f8ff; }
  .cal-event-title { font-weight: 700; font-size: 0.95rem; margin-bottom: 4px; }
  .cal-meta { display: flex; flex-wrap: wrap; gap: 14px; font-size: 0.82rem; color: #555; margin-bottom: 4px; }
  .cal-meta span strong { color: #1a1a2e; }
  .cal-note { font-size: 0.8rem; color: #777; font-style: italic; margin-top: 4px; }
  .badge { display: inline-block; padding: 2px 8px; border-radius: 20px; font-size: 0.72rem; font-weight: 700; text-transform: uppercase; }
  .badge-green   { background: #d4edda; color: #155724; }
  .badge-yellow  { background: #fff3cd; color: #856404; }
  .badge-red     { background: #f8d7da; color: #721c24; }
  .badge-blue    { background: #d0e8ff; color: #0c5460; }
  .badge-gray    { background: #e2e3e5; color: #383d41; }
  .conflict-warn { background: #fff3cd; border: 1px solid #ffc107; border-radius: 5px; padding: 5px 10px; font-size: 0.8rem; color: #856404; margin-top: 6px; }

  /* JOB TABLE */
  table { width: 100%; border-collapse: collapse; font-size: 0.86rem; }
  th { background: #f0f2f5; padding: 9px 12px; text-align: left; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.5px; color: #555; border-bottom: 2px solid #dde; }
  td { padding: 9px 12px; border-bottom: 1px solid #f0f2f5; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f8f9fb; }
  .fit-high   { color: #27ae60; font-weight: 700; }
  .fit-med    { color: #e67e22; font-weight: 700; }
  .fit-low    { color: #7f8c8d; font-weight: 600; }

  /* EMAIL REVIEW */
  .email-cat { background: #f7f9fc; border-radius: 8px; padding: 14px 16px; margin-bottom: 12px; border-left: 4px solid #ccc; }
  .email-cat.cat-red    { border-left-color: #c0392b; }
  .email-cat.cat-green  { border-left-color: #27ae60; }
  .email-cat.cat-yellow { border-left-color: #e67e22; }
  .email-cat.cat-blue   { border-left-color: #2980b9; }
  .email-cat.cat-purple { border-left-color: #8e44ad; }
  .email-cat.cat-gray   { border-left-color: #95a5a6; }
  .email-cat.cat-teal   { border-left-color: #16a085; }
  .email-cat-title { font-weight: 700; font-size: 0.95rem; margin-bottom: 6px; display: flex; align-items: center; gap: 10px; }
  .email-cat-count { background: #1a1a2e; color: #fff; border-radius: 20px; padding: 1px 9px; font-size: 0.75rem; }
  .email-cat p { font-size: 0.84rem; color: #444; margin-bottom: 4px; }
  .email-cat .senders { font-size: 0.8rem; color: #666; font-style: italic; }
  .email-cat .action-rec { font-size: 0.82rem; font-weight: 600; margin-top: 6px; padding: 4px 10px; border-radius: 4px; display: inline-block; }
  .rec-delete  { background: #f8d7da; color: #721c24; }
  .rec-review  { background: #fff3cd; color: #856404; }
  .rec-keep    { background: #d4edda; color: #155724; }
  .rec-unsubscribe { background: #e2e3e5; color: #383d41; }
  .rec-action  { background: #d0e8ff; color: #0c5460; }

  /* DASHBOARD */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-tile { background: #fff; border-radius: 10px; padding: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); text-align: center; }
  .dash-tile .dash-num { font-size: 2.2rem; font-weight: 800; }
  .dash-tile .dash-label { font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.6px; color: #666; margin-top: 2px; }
  .dash-tile .dash-sub { font-size: 0.78rem; color: #888; margin-top: 4px; }
  .dash-tile.red-tile .dash-num    { color: #c0392b; }
  .dash-tile.yellow-tile .dash-num { color: #e67e22; }
  .dash-tile.green-tile .dash-num  { color: #27ae60; }
  .dash-tile.blue-tile .dash-num   { color: #2980b9; }
  .dash-tile.purple-tile .dash-num { color: #8e44ad; }

  /* TRASH / PROMO */
  .trash-group { margin-bottom: 14px; }
  .trash-group-title { font-weight: 700; font-size: 0.9rem; padding: 6px 12px; border-radius: 5px; margin-bottom: 6px; }
  .trash-restore { background: #d0e8ff; color: #0c5460; }
  .trash-review  { background: #fff3cd; color: #856404; }
  .trash-delete  { background: #e2e3e5; color: #383d41; }
  .trash-item { font-size: 0.82rem; padding: 5px 10px; border-bottom: 1px solid #f0f2f5; display: flex; gap: 8px; }
  .trash-item:last-child { border-bottom: none; }
  .trash-item .ti-sender { font-weight: 600; min-width: 160px; }
  .trash-item .ti-reason { color: #666; font-style: italic; }

  /* NEWSLETTER TABLE */
  .nl-table th { background: #8e44ad; color: #fff; }
  .promo-table th { background: #7f8c8d; color: #fff; }

  /* ACCOUNTING */
  .acct-table th { background: #1a1a2e; color: #fff; }
  .acct-total td { font-weight: 700; background: #f0f2f5; }

  /* PRIORITIES */
  .priority-list { list-style: none; counter-reset: pri; }
  .priority-list li { counter-increment: pri; display: flex; align-items: flex-start; gap: 14px; padding: 14px 0; border-bottom: 1px solid #f0f2f5; }
  .priority-list li:last-child { border-bottom: none; }
  .priority-list li::before { content: counter(pri); background: #1a1a2e; color: #fff; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 1rem; flex-shrink: 0; }
  .priority-list .p-title { font-weight: 700; font-size: 0.97rem; }
  .priority-list .p-detail { font-size: 0.85rem; color: #555; }

  /* ACTION TABLE */
  .at-high   { color: #c0392b; font-weight: 700; }
  .at-medium { color: #e67e22; font-weight: 700; }
  .at-low    { color: #7f8c8d; font-weight: 600; }

  /* MISC */
  .warn-box { background: #fff3cd; border: 1px solid #ffc107; border-radius: 7px; padding: 10px 14px; font-size: 0.85rem; color: #856404; margin-bottom: 14px; }
  .info-box  { background: #d0e8ff; border: 1px solid #90caf9; border-radius: 7px; padding: 10px 14px; font-size: 0.85rem; color: #0c5460; margin-bottom: 14px; }
  a { color: #2980b9; text-decoration: none; }
  a:hover { text-decoration: underline; }
  hr { border: none; border-top: 1px solid #e8eaf0; margin: 18px 0; }
  .no-events { font-style: italic; color: #aaa; font-size: 0.86rem; padding: 8px 0; }

  @media (max-width: 640px) {
    .header h1 { font-size: 1.4rem; }
    .action-cards { grid-template-columns: 1fr; }
    .dash-grid { grid-template-columns: repeat(2, 1fr); }
  }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ═══════════════════════════════════════════════════════
     1. HEADER
════════════════════════════════════════════════════════ -->
<div class="header">
  <div class="sub">EXECUTIVE BRIEFING &nbsp;·&nbsp; PREPARED BY CHIEF OF STAFF</div>
  <h1>Good morning, Melissa ☀️</h1>
  <div class="sub">Monday, June 8, 2026 &nbsp;|&nbsp; Daily Intelligence Briefing</div>
  <div class="meta-row">
    <div class="meta-box"><div class="num">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="meta-box"><div class="num">7</div><div class="lbl">Calendar Events</div></div>
    <div class="meta-box"><div class="num">6</div><div class="lbl">Action Required</div></div>
    <div class="meta-box"><div class="num">3</div><div class="lbl">Security Alerts</div></div>
    <div class="meta-box"><div class="num">4</div><div class="lbl">Job Leads</div></div>
    <div class="meta-box"><div class="num">1</div><div class="lbl">Today's Events</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     2. EXECUTIVE SUMMARY
════════════════════════════════════════════════════════ -->
<div class="section-wrap red">
  <div class="section-title">🔴 Executive Summary — 3 Critical Items</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li>
        <span class="exec-bullet-icon">🚨</span>
        <div class="exec-bullet-text">
          <strong>SECURITY RISK: Multiple phishing &amp; spam campaigns targeting you today</strong>
          <span>You received 3+ fake "Lowe's winner" phishing emails from suspicious domains, a fake Cloud ID lock scam spoofing your own username, two fake Ozempic prescription emails from malicious domains, casino spam, and an explicit/adult spam message. Do not click any links. Mark all as phishing immediately.</span>
        </div>
      </li>
      <li>
        <span class="exec-bullet-icon">💼</span>
        <div class="exec-bullet-text">
          <strong>JOB OPPORTUNITY: LinkedIn shows 149 profile searches + two strong director-level alerts</strong>
          <span>Your LinkedIn profile appeared in 149 searches today. Two active alerts landed — Director, HR Business Partnership at Instacart and VP, Human Resources Business Partner at Moderna. Your profile is attracting attention. Review both postings and consider applying today.</span>
        </div>
      </li>
      <li>
        <span class="exec-bullet-icon">📅</span>
        <div class="exec-bullet-text">
          <strong>CALENDAR: Eye appointment this morning (9–10 AM ET) + RSVP pending for two networking events this week</strong>
          <span>You have an Eye appointment at 9 AM today. Two HR Networking Group events on June 10 &amp; June 11 still show "Needs Action" — RSVP required. Note: a scheduling conflict exists on June 10 (Network and Melissa x Meg drinks overlap). Also: you declined the Executive Roundtable on June 11 — confirm that decision is intentional.</span>
        </div>
      </li>
    </ul>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     3. ACTION REQUIRED
════════════════════════════════════════════════════════ -->
<div class="section-wrap yellow">
  <div class="section-title">⚡ Action Required</div>
  <div class="section-body">
    <div class="action-cards">

      <div class="action-card red-card">
        <div class="card-label">🚨 Security — Phishing</div>
        <div class="card-title">Fake "Lowe's Winner" Phishing Emails (4 copies)</div>
        <div class="card-row"><strong>Source:</strong> Multiple spoofed Lowe's domains</div>
        <div class="card-row"><strong>Why it matters:</strong> 4 nearly-identical phishing emails from suspicious random domains impersonating Lowe's. Designed to steal credentials or install malware.</div>
        <div class="card-row"><strong>Next Step:</strong> Do NOT click any links. Report as phishing in Gmail. Block senders. Consider enabling Gmail advanced phishing protection.</div>
        <div class="card-row"><strong>Due:</strong> Immediately</div>
      </div>

      <div class="action-card red-card">
        <div class="card-label">🚨 Security — Identity Scam</div>
        <div class="card-title">"Your Cloud ID has been locked" — Account Takeover Attempt</div>
        <div class="card-row"><strong>Source:</strong> melissaw212 &lt;rvrrtxlzonl@jstr…&gt; (spoofing your own email)</div>
        <div class="card-row"><strong>Why it matters:</strong> Spoofs your own username to create urgency around a fake Cloud Storage payment issue. Classic credential-harvesting scam.</div>
        <div class="card-row"><strong>Next Step:</strong> Delete immediately. Do not click. Verify your actual cloud accounts (Google, iCloud) directly in a browser — not from any email link.</div>
        <div class="card-row"><strong>Due:</strong> Immediately</div>
      </div>

      <div class="action-card yellow-card">
        <div class="card-label">📅 RSVP Needed</div>
        <div class="card-title">HR Networking &amp; Job Search Group — June 10 &amp; June 11</div>
        <div class="card-row"><strong>Source:</strong> Google Calendar (2 events)</div>
        <div class="card-row"><strong>Why it matters:</strong> Both events still show "Needs Action." These are key networking sessions during an active job search.</div>
        <div class="card-row"><strong>Next Step:</strong> Accept or decline both events. June 10 at noon has a conflict with "Network" (same time) — review and consolidate.</div>
        <div class="card-row"><strong>Due:</strong> Today</div>
      </div>

      <div class="action-card green-card">
        <div class="card-label">💼 Job Opportunity</div>
        <div class="card-title">LinkedIn: 149 Searches + Director/VP Role Alerts</div>
        <div class="card-row"><strong>Source:</strong> LinkedIn notifications + job alerts</div>
        <div class="card-row"><strong>Why it matters:</strong> Profile visibility is high. Two senior HR roles — Instacart (Director, HRBP) and Moderna (VP, HRBP) — are strong matches.</div>
        <div class="card-row"><strong>Next Step:</strong> Log into LinkedIn. Review both roles. Apply to Moderna VP role today (senior, likely competitive). Also check who searched your profile.</div>
        <div class="card-row"><strong>Due:</strong> Today / This week</div>
      </div>

      <div class="action-card blue-card">
        <div class="card-label">📦 Delivery Today</div>
        <div class="card-title">Target Order Arriving Today — Order #912003459399629</div>
        <div class="card-row"><strong>Source:</strong> Target orders@oe.target.com</div>
        <div class="card-row"><strong>Why it matters:</strong> Package arriving today. Note: your Nextdoor neighborhood alert reports package theft at 82 Berry Street last night.</div>
        <div class="card-row"><strong>Next Step:</strong> Monitor delivery notification. Retrieve package promptly. Consider requiring signature or redirecting to a secure location.</div>
        <div class="card-row"><strong>Due:</strong> Today</div>
      </div>

      <div class="action-card yellow-card">
        <div class="card-label">📅 Calendar Decision</div>
        <div class="card-title">Executive Roundtable — June 11 (Currently DECLINED)</div>
        <div class="card-row"><strong>Source:</strong> Calendar — John Madigan, Zoom</div>
        <div class="card-row"><strong>Why it matters:</strong> This is a professional roundtable. You have declined — confirm this is intentional, especially given active job search.</div>
        <div class="card-row"><strong>Next Step:</strong> Confirm your decline is intentional. If not, accept via calendar invite. Zoom link available.</div>
        <div class="card-row"><strong>Due:</strong> Before June 11</div>
      </div>

    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     4. FULL 7-DAY CALENDAR
════════════════════════════════════════════════════════ -->
<div class="section-wrap blue">
  <div class="section-title">📅 Full 7-Day Calendar (June 8–14, 2026)</div>
  <div class="section-body">

    <!-- Monday June 8 -->
    <div class="cal-day">
      <div class="cal-day-header"><span>📆 Monday, June 8, 2026</span><span>TODAY</span></div>

      <div class="cal-event confirmed">
        <div class="cal-event-title">👁️ Eye Appointment <span class="badge badge-green">CONFIRMED</span></div>
        <div class="cal-meta">
          <span><strong>Time:</strong> 9:00 AM – 10:00 AM ET</span>
          <span><strong>Location:</strong> Not specified</span>
          <span><strong>Attendees:</strong> Melissa only</span>
        </div>
        <div class="cal-note">⚠️ This appointment is happening RIGHT NOW (or very soon). Ensure you have departed / are prepared. No location listed — confirm office address if needed.</div>
      </div>
    </div>

    <!-- Tuesday June 9 -->
    <div class="cal-day">
      <div class="cal-day-header"><span>📆 Tuesday, June 9, 2026</span><span>Tomorrow</span></div>

      <div class="cal-event accepted">
        <div class="cal-event-title">🤝 Melissa Weiss &amp; Netta Jenkins — 15-Minute Consultation <span class="badge badge-blue">ACCEPTED</span></div>
        <div class="cal-meta">
          <span><strong>Time:</strong> 12:00 PM – 12:15 PM ET</span>
          <span><strong>Location:</strong> <a href="https://us06web.zoom.us/j/5224221004?pwd=UU5YNmlFckpjQnlzc2FDMHFlNUhhUT09" target="_blank">Zoom Link</a></span>
          <span><strong>Attendees:</strong> netta@hicconsult.com</span>
          <span><strong>Password:</strong> 424726</span>
        </div>
        <div class="cal-note">💡 Prep: This is a consulting call with Netta Jenkins (HIC Consult). 15 minutes only — have your talking points ready. Confirm your goals for this call in advance.</div>
      </div>
    </div>

    <!-- Wednesday June 10 -->
    <div class="cal-day">
      <div class="cal-day-header"><span>📆 Wednesday, June 10, 2026</span><span>3 Events — Conflict!</span></div>

      <div class="cal-event needs-action">
        <div class="cal-event-title">👥 HR Networking &amp; Job Search Group — Zoom Session 2 <span class="badge badge-yellow">NEEDS ACTION</span></div>
        <div class="cal-meta">
          <span><strong>Time:</strong> 12:00 PM – 1:30 PM ET</span>
          <span><strong>Location:</strong> <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a></span>
          <span><strong>Attendees:</strong> 190+ HR professionals</span>
        </div>
        <div class="cal-note">⚠️ RSVP PENDING. Large HR networking group with 190+ members. Highly valuable for job search. Please accept or decline.</div>
        <div class="conflict-warn">⚡ CONFLICT: Overlaps with "Network" event (12:00–1:30 PM same day) — may be the same event with two calendar entries. And overlaps with Melissa x Meg Drinks (1:00–2:00 PM).</div>
      </div>

      <div class="cal-event confirmed">
        <div class="cal-event-title">📋 Network <span class="badge badge-green">CONFIRMED</span></div>
        <div class="cal-meta">
          <span><strong>Time:</strong> 12:00 PM – 1:30 PM ET</span>
          <span><strong>Location:</strong> Not specified</span>
          <span><strong>Attendees:</strong> Melissa only (no attendees listed)</span>
        </div>
        <div class="cal-note">💡 This appears to be a duplicate or companion entry for the HR Networking Group above. Confirm whether this is a separate event.</div>
        <div class="conflict-warn">⚡ CONFLICT: Same time as HR Networking Group Zoom and overlaps with Melissa x Meg Drinks.</div>
      </div>

      <div class="cal-event accepted">
        <div class="cal-event-title">🍹 Melissa x Meg — Drinks <span class="badge badge-blue">ACCEPTED</span></div>
        <div class="cal-meta">
          <span><strong>Time:</strong> 1:00 PM – 2:00 PM ET</span>
          <span><strong>Location:</strong> TBC</span>
          <span><strong>Attendees:</strong> megpark@oakleafpartnership.com</span>
        </div>
        <div class="cal-note">💡 Location is TBC — confirm with Meg before Wednesday. This overlaps with the end of the networking Zoom sessions above. Plan accordingly.</div>
        <div class="conflict-warn">⚡ CONFLICT: Overlaps with HR Networking Zoom (12:00–1:30 PM). You'll need to leave the Zoom early to make this 1:00 PM drinks.</div>
      </div>
    </div>

    <!-- Thursday June 11 -->
    <div class="cal-day">
      <div class="cal-day-header"><span>📆 Thursday, June 11, 2026</span><span>2 Events</span></div>

      <div class="cal-event declined">
        <div class="cal-event-title">🏛️ Executive Roundtable <span class="badge badge-red">DECLINED</span></div>
        <div class="cal-meta">
          <span><strong>Time:</strong> 9:00 AM – 10:30 AM ET</span>
          <span><strong>Location:</strong> <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a></span>
          <span><strong>Organizer:</strong> John Madigan</span>
          <span><strong>Meeting ID:</strong> 207 786 667 | PW: 205454</span>
        </div>
        <div class="cal-note">⚠️ You have DECLINED this event. Given your active job search, reconsider attending an Executive Roundtable — this type of visibility may be valuable.</div>
      </div>

      <div class="cal-event needs-action">
        <div class="cal-event-title">👥 HR Networking &amp; Job Search: Open Office Hours — Zoom 2 <span class="badge badge-yellow">NEEDS ACTION</span></div>
        <div class="cal-meta">
          <span><strong>Time:</strong> 12:00 PM – 1:00 PM ET</span>
          <span><strong>Location:</strong> <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a></span>
          <span><strong>Attendees:</strong> 190+ HR professionals</span>
        </div>
        <div class="cal-note">⚠️ RSVP PENDING. Open office hours format — good for targeted questions and 1:1 connections. Note: AI notetaking tools should be turned off per organizer instructions.</div>
      </div>
    </div>

    <!-- Friday June 12 -->
    <div class="cal-day">
      <div class="cal-day-header"><span>📆 Friday, June 12, 2026</span><span></span></div>
      <div class="cal-note no-events">No calendar events scheduled.</div>
    </div>

    <!-- Saturday June 13 -->
    <div class="cal-day">
      <div class="cal-day-header"><span>📆 Saturday, June 13, 2026</span><span></span></div>
      <div class="cal-note no-events">No calendar events scheduled.</div>
    </div>

    <!-- Sunday June 14 -->
    <div class="cal-day">
      <div class="cal-day-header"><span>📆 Sunday, June 14, 2026</span><span></span></div>
      <div class="cal-note no-events">No calendar events scheduled.</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     5. JOB SEARCH & INTERVIEW PIPELINE
════════════════════════════════════════════════════════ -->
<div class="section-wrap green">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">
    <div class="info-box">📊 LinkedIn shows Melissa's profile appeared in <strong>149 searches</strong> today — strong visibility signal. Two separate LinkedIn notifications confirm profile attention is high.</div>
    <table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Role / Company</th>
          <th>Source</th>
          <th>Fit</th>
          <th>Status</th>
          <th>Next Step</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>🔔 Job Alert</td>
          <td><strong>VP, Human Resources Business Partner</strong><br>Moderna</td>
          <td>LinkedIn Job Alerts</td>
          <td class="fit-high">HIGH</td>
          <td><span class="badge badge-yellow">Not Applied</span></td>
          <td>Review JD and apply today — VP level, major pharma company, strong match for HRBP background.</td>
        </tr>
        <tr>
          <td>🔔 Job Alert</td>
          <td><strong>Director, HR Business Partnership</strong><br>Instacart</td>
          <td>LinkedIn Job Alerts (2 copies)</td>
          <td class="fit-high">HIGH</td>
          <td><span class="badge badge-yellow">Not Applied</span></td>
          <td>Duplicate alert received — review role. Instacart is transforming grocery industry. Strong HRBP fit.</td>
        </tr>
        <tr>
          <td>📣 Profile</td>
          <td><strong>149 Profile Searches Today</strong><br>LinkedIn</td>
          <td>LinkedIn notifications (2 emails)</td>
          <td class="fit-high">HIGH</td>
          <td><span class="badge badge-blue">Unread</span></td>
          <td>Log into LinkedIn Premium to see who searched. Reach out to relevant searchers. Update headline/summary if needed.</td>
        </tr>
        <tr>
          <td>🤝 Networking</td>
          <td><strong>15-Min Consult — Netta Jenkins</strong><br>HIC Consult</td>
          <td>Google Calendar — June 9</td>
          <td class="fit-med">MEDIUM</td>
          <td><span class="badge badge-green">Accepted</span></td>
          <td>Prepare 2–3 talking points. Confirm purpose of call (coaching? referral? consulting?).</td>
        </tr>
        <tr>
          <td>🤝 Networking</td>
          <td><strong>HR Networking &amp; Job Search Group</strong><br>190+ HR Professionals</td>
          <td>Calendar — June 10, 12–1:30 PM</td>
          <td class="fit-high">HIGH</td>
          <td><span class="badge badge-yellow">RSVP Pending</span></td>
          <td>Accept event. Review team guidelines. Prepare introduction and target role talking points.</td>
        </tr>
        <tr>
          <td>🤝 Networking</td>
          <td><strong>HR Networking Open Office Hours</strong><br>190+ HR Professionals</td>
          <td>Calendar — June 11, 12–1 PM</td>
          <td class="fit-high">HIGH</td>
          <td><span class="badge badge-yellow">RSVP Pending</span></td>
          <td>Accept. Prepare specific questions. No AI notetaking tools per organizer instructions.</td>
        </tr>
        <tr>
          <td>☕ Relationship</td>
          <td><strong>Drinks — Meg Park</strong><br>Oakleaf Partnership</td>
          <td>Calendar — June 10, 1–2 PM</td>
          <td class="fit-med">MEDIUM</td>
          <td><span class="badge badge-green">Accepted</span></td>
          <td>Confirm location with Meg (TBC). Prepare casual networking talking points. Potential referral source.</td>
        </tr>
        <tr>
          <td>📰 Career Dev</td>
          <td><strong>LinkedIn Into a Recruiter Magnet</strong><br>KKARENISM Newsletter</td>
          <td>Gmail Inbox</td>
          <td class="fit-med">MEDIUM</td>
          <td><span class="badge badge-blue">Unread — Inbox</span></td>
          <td>Review article — timely given 149 profile searches. Contains LinkedIn Live + interview scripts.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     6. FULL EMAIL REVIEW BY CATEGORY
════════════════════════════════════════════════════════ -->
<div class="section-wrap navy">
  <div class="section-title">📧 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="email-cat cat-red">
      <div class="email-cat-title">🚨 Security / Risk <span class="email-cat-count">6</span></div>
      <p><strong>Emails:</strong></p>
      <p>1. <strong>Fake "Lowe's Winner" #1</strong> — "'Lowe's®'" &lt;gflqsupport…@rlyqh…com&gt; — phishing, suspicious domain</p>
      <p>2. <strong>Fake "Lowe's Winner" #2</strong> — "'Lowe's®'" &lt;fqqsupport…@erdz…com&gt; — identical phishing, different domain</p>
      <p>3. <strong>Fake "Lowe's Winner" #3</strong> — "Lowe's®" &lt;kvzyaq…@b6dple…us&gt; — identical phishing, third domain</p>
      <p>4. <strong>Fake "Lowe's Winner" #4</strong> — "'Lowe's®'" &lt;melissaw212@oqevnv…dumps.in&gt; — spoofs YOUR OWN EMAIL</p>
      <p>5. <strong>Cloud ID Lock Scam</strong> — melissaw212 &lt;rvrrtxl…@jstr…us&gt; — fake Cloud Storage payment issue, credential theft attempt</p>
      <p>6. <strong>Explicit Spam / Malware Risk</strong> — "🔶FUCK-BUDDY SECRET🔶" &lt;zrsupport…&gt; — explicit adult spam, possible malware link</p>
      <div class="senders">Senders: Multiple spoofed/malicious domains, spoofed username</div>
      <span class="action-rec rec-delete">🗑️ Action: Report ALL as phishing. Block senders. Do NOT click any links.</span>
    </div>

    <!-- JOB SEARCH -->
    <div class="email-cat cat-green">
      <div class="email-cat-title">💼 Job Search &amp; Opportunities <span class="email-cat-count">4</span></div>
      <p>1. <strong>LinkedIn: 149 Profile Searches</strong> — LinkedIn &lt;notifications-noreply@linkedin.com&gt; — Inbox, Unread</p>
      <p>2. <strong>LinkedIn: Profile Getting Attention</strong> — LinkedIn &lt;messages-noreply@linkedin.com&gt; — Inbox, Unread</p>
      <p>3. <strong>Director, HR Business Partnership — Instacart</strong> — LinkedIn Job Alerts (×2, sent at different times)</p>
      <p>4. <strong>VP, Human Resources Business Partner — Moderna</strong> — LinkedIn Job Alerts</p>
      <div class="senders">Senders: LinkedIn (notifications, messages, job alerts)</div>
      <span class="action-rec rec-action">✅ Action: Review all. Apply to Moderna VP role today. Check LinkedIn for profile searchers.</span>
    </div>

    <!-- RECRUITERS / NETWORKING -->
    <div class="email-cat cat-green">
      <div class="email-cat-title">🤝 Recruiters / Networking <span class="email-cat-count">1</span></div>
      <p>1. <strong>How to Turn Your LinkedIn Into a Recruiter Magnet</strong> — KKARENISM &lt;kkarenism@substack.com&gt; — Inbox, Unread</p>
      <div class="senders">Sender: KKARENISM Substack — career &amp; LinkedIn tips newsletter, Inbox</div>
      <span class="action-rec rec-keep">📖 Action: Read — contains LinkedIn Live + interview scripts, timely given current search.</span>
    </div>

    <!-- CALENDAR / EVENTS -->
    <div class="email-cat cat-blue">
      <div class="email-cat-title">📅 Calendar / Events <span class="email-cat-count">1</span></div>
      <p>1. <strong>Your Upcoming Meetings</strong> — Otter.ai Insights &lt;no-reply@otter.ai&gt; — not in inbox, read</p>
      <div class="senders">Sender: Otter.ai — weekly meeting prep summary</div>
      <span class="action-rec rec-review">👀 Action: Review Otter.ai summary for this week's meetings if you use it for notes.</span>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="email-cat cat-yellow">
      <div class="email-cat-title">💳 Financial / Billing <span class="email-cat-count">3</span></div>
      <p>1. <strong>Direct Deposit Credited — $23.00 (Venmo Cashout)</strong> — Bank of America — Inbox, Unread ⭐</p>
      <p>2. <strong>JetBlue Plus Card — Earn Your Bonus</strong> — Barclays alerts — bonus progress reminder, account ending 2885</p>
      <p>3. <strong>SmartMoney Minute: Roth Conversions &amp; Social Security Taxes</strong> — SmartAsset — <em>in Trash</em></p>
      <div class="senders">Senders: Bank of America, Barclays/JetBlue, SmartAsset</div>
      <span class="action-rec rec-review">💰 Action: Note $23 Venmo deposit. Review JetBlue bonus progress. SmartMoney article in trash — review before deleting if retirement planning is relevant.</span>
    </div>

    <!-- DELIVERIES / PERSONAL ORDERS -->
    <div class="email-cat cat-teal">
      <div class="email-cat-title">📦 Personal / Deliveries <span class="email-cat-count">4</span></div>
      <p>1. <strong>Target: Order Arrives Today</strong> — orders@oe.target.com — Order #912003459399629 — Inbox ⭐</p>
      <p>2. <strong>Amazon Shipped: "Tempt Me Women One Piece" + 1 More Item</strong> — shipment-tracking@amazon.com — Unread</p>
      <p>3. <strong>Amazon Shipped: "Onyx Professional Hard as…"</strong> — shipment-tracking@amazon.com — Unread</p>
      <p>4. <strong>USPS Informed Delivery: 4 Mailpieces Today</strong> — USPS — read, not in inbox</p>
      <div class="senders">Senders: Target, Amazon (×2), USPS</div>
      <span class="action-rec rec-keep">📬 Action: Monitor Target delivery today (theft alert in neighborhood). Track Amazon shipments. 4 mail items arriving.</span>
    </div>

    <!-- PERSONAL / SOCIAL -->
    <div class="email-cat cat-teal">
      <div class="email-cat-title">💛 Personal / Social <span class="email-cat-count">3</span></div>
      <p>1. <strong>Match: Laurence likes you</strong> — Match.com — Inbox, Unread</p>
      <p>2. <strong>Match: Carl likes you</strong> — Match.com — not in inbox, Unread</p>
      <p>3. <strong>Nextdoor Yorkville: WEDDING SUIT STOLEN</strong> — Nextdoor — Inbox, Unread ⚠️ (package theft alert at 82 Berry Street)</p>
      <div class="senders">Senders: Match.com (×2), Nextdoor</div>
      <span class="action-rec rec-review">👀 Action: Review Nextdoor alert — relevant to your own Target delivery today. Check Match when convenient.</span>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="email-cat cat-purple">
      <div class="email-cat-title">🎓 Professional Development <span class="email-cat-count">2</span></div>
      <p>1. <strong>How to Leave Corporate</strong> — Martin &lt;martin@thepeoplepeoplegroup.com&gt; — <em>in Trash</em>, Unread</p>
      <p>2. <strong>Market Yourself Now…</strong> — Lisa Rangel &lt;lr@chameleonresumes.com&gt; — <em>in Trash</em>, Unread</p>
      <div class="senders">Senders: The People People Group (Martin), Chameleon Resumes (Lisa Rangel)</div>
      <span class="action-rec rec-review">📖 Action: Both are in Trash but unread. Given active job search, consider restoring and reading — resume &amp; career coach content may be useful.</span>
    </div>

    <!-- NEWSLETTERS / SUBSCRIPTIONS -->
    <div class="email-cat cat-purple">
      <div class="email-cat-title">📰 Newsletters / Subscriptions <span class="email-cat-count">7</span></div>
      <p>1. <strong>Medium Daily Digest</strong> — Anthropic/Opus 4.8 article — <em>in Trash</em>, Unread</p>
      <p>2. <strong>1% Better</strong> — Bypassing Hormuz, GLP-1, Health Metric — <em>in Trash</em>, Unread</p>
      <p>3. <strong>The Daily Skimm</strong> — Sleep scientist's summer bedtime rules — <em>in Trash</em>, Unread</p>
      <p>4. <strong>The Average Joe</strong> — 👑 King Coal — not in inbox, read</p>
      <p>5. <strong>The Hustle</strong> — Acupuncture for animals? — not in inbox, read</p>
      <p>6. <strong>CoolDeep AI</strong> — Cowork setup — Inbox, Unread</p>
      <p>7. <strong>CoinOut</strong> — 1,000 Bonus Coins Day 2 — Food &amp; Beverage Journal participation</p>
      <div class="senders">Senders: Medium, 1% Better, The Daily Skimm, The Average Joe, The Hustle, CoolDeep AI, CoinOut</div>
      <span class="action-rec rec-review">📋 Action: Review newsletters in Trash before permanently deleting. Consider unsubscribing from ones you consistently trash.</span>
    </div>

    <!-- PROMOTIONAL / RETAIL -->
    <div class="email-cat cat-gray">
      <div class="email-cat-title">🛍️ Promotional / Retail <span class="email-cat-count">12</span></div>
      <p>1. SHEIN — Home Picks Up to 80% OFF — Inbox</p>
      <p>2. SHEIN Men — Looking Sharp — Inbox</p>
      <p>3. SHEIN — Bestseller Sale $4.99 (×2 duplicate sends) — Inbox</p>
      <p>4. Kohl's — Father's Day Gifts, Budget-Friendly — Inbox</p>
      <p>5. Gap Factory — Linen-Blend Apron Top Restocked — Inbox</p>
      <p>6. Macy's — Up to 50% Off Summer Favorites Sale — not in inbox</p>
      <p>7. Amazon Alexa — Prime Day June 23–26 — <em>in Trash</em></p>
      <p>8. Manychat — Creator marketing email — read, not in inbox</p>
      <div class="senders">Senders: SHEIN (×4), Kohl's, Gap Factory, Macy's, Amazon, Manychat</div>
      <span class="action-rec rec-delete">🗑️ Action: Delete/archive most. Gap Factory restock may be of interest (you wishlisted it). Prime Day June 23–26 is worth noting.</span>
    </div>

    <!-- SPAM / MEDICAL SPAM -->
    <div class="email-cat cat-red">
      <div class="email-cat-title">⚠️ Spam / Suspicious Medical Offers <span class="email-cat-count">5</span></div>
      <p>1. TrimRx.Reminder — "Last call on your $120" — GLP-1 weight loss spam, suspicious domain</p>
      <p>2. "Care Pharmacy" — Erection Packs — spam, obfuscated text in sender name</p>
      <p>3. "Ozempic by DirectMeds" #1 — "Lose Weight Effortlessly" — suspicious domain</p>
      <p>4. "Ozempic by DirectMeds" #2 — identical subject, spoofs YOUR OWN EMAIL in sender</p>
      <p>5. GLP-1-by-DirectMeds — "Lose up to 40 lbs by End of Year" — suspicious domain</p>
      <div class="senders">Senders: TrimRx (spam), Care Pharmacy (spam), DirectMeds ×3 (phishing/spam)</div>
      <span class="action-rec rec-delete">🚨 Action: Report as spam/phishing. Do NOT click. These are not legitimate medical providers.</span>
    </div>

    <!-- GAMBLING SPAM -->
    <div class="email-cat cat-red">
      <div class="email-cat-title">🎰 Gambling Spam <span class="email-cat-count">3</span></div>
      <p>1. Limitless VIP — "Get 130 Free Spins — GETFREE130" #1</p>
      <p>2. Limitless VIP — "Get 130 Free Spins — GETFREE130" #2 (duplicate, different domain)</p>
      <p>3. "Congratulations🎉" — "130 Free Spins Pending in your Account" — suspicious domain</p>
      <div class="senders">Senders: Limitless VIP (×2), fake "Congratulations" sender — all suspicious domains</div>
      <span class="action-rec rec-delete">🗑️ Action: Mark as spam and delete all. Do not engage.</span>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     7. TRASH REVIEW
════════════════════════════════════════════════════════ -->
<div class="section-wrap yellow">
  <div class="section-title">🗑️ Trash Review</div>
  <div class="section-body">

    <div class="trash-group">
      <div class="trash-group-title trash-restore">✅ RESTORE — Consider Bringing Back to Inbox</div>
      <div class="trash-item">
        <span class="ti-sender">Martin / The People People Group</span>
        <span>Subject: "How to Leave Corporate" — Career newsletter, unread, potentially valuable during active job search. Restore and read.</span>
      </div>
      <div class="trash-item">
        <span class="ti-sender">Lisa Rangel / Chameleon Resumes</span>
        <span>Subject: "Market Yourself Now…" — Resume coach content on self-marketing. Unread. Highly relevant to current job search. Restore.</span>
      </div>
    </div>

    <div class="trash-group">
      <div class="trash-group-title trash-review">👀 REVIEW BEFORE DELETING</div>
      <div class="trash-item">
        <span class="ti-sender">Medium Daily Digest</span>
        <span>Subject: "What Anthropic Didn't Say About Opus 4.8" — AI/tech content. Unread. Review if AI topics are professionally relevant; otherwise delete.</span>
      </div>
      <div class="trash-item">
        <span class="ti-sender">1% Better Newsletter</span>
        <span>Subject: "Bypassing Hormuz, GLP-1 Returns, and Your Most Important Health Metric" — Health &amp; geopolitical content. Unread. Skim if interested; otherwise delete.</span>
      </div>
      <div class="trash-item">
        <span class="ti-sender">The Daily Skimm</span>
        <span>Subject: "A Sleep Scientist's Summer Bedtime Rules" — Lifestyle/wellness. Unread. Quick skim or delete.</span>
      </div>
      <div class="trash-item">
        <span class="ti-sender">SmartMoney Minute (SmartAsset)</span>
        <span>Subject: "How Roth Conversions Can Potentially Impact Your Social Security Taxes" — Financial planning content. Unread. Review if retirement planning is a current priority.</span>
      </div>
    </div>

    <div class="trash-group">
      <div class="trash-group-title trash-delete">🗑️ SAFE TO DELETE PERMANENTLY</div>
      <div class="trash-item">
        <span class="ti-sender">Amazon Alexa / Amazon</span>
        <span>Subject: "Prime Day is June 23–26. Shop with Alexa+" — Promotional. Prime Day noted (June 23–26). Safe to delete email.</span>
      </div>
    </div>

    <p style="font-size:0.83rem; color:#777; margin-top: 10px;"><em>Total emails in Trash: 7 — (Medium, 1% Better, Daily Skimm, Lisa Rangel, Martin/People Group, SmartMoney, Amazon Alexa)</em></p>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     8. PROMOTIONAL / RETAIL SUMMARY
════════════════════════════════════════════════════════ -->
<div class="section-wrap gray">
  <div class="section-title">🛍️ Promotional / Retail Summary</div>
  <div class="section-body">
    <table class="promo-table">
      <thead>
        <tr>
          <th>Sender / Brand</th>
          <th>Count</th>
          <th>Subject / Theme</th>
          <th>Recommendation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>SHEIN</strong></td>
          <td>4</td>
          <td>Home picks 80% off; Men's fashion; Bestseller sale $4.99 (2 duplicate sends)</td>
          <td><span class="badge badge-gray">Delete / Ignore</span> — Duplicate sends. Unsubscribe if not actively shopping.</td>
        </tr>
        <tr>
          <td><strong>Kohl's</strong></td>
          <td>1</td>
          <td>Father's Day gifts, budget-friendly. 15% off home for Rewards members</td>
          <td><span class="badge badge-gray">Review</span> — Father's Day is June 21. Check if relevant.</td>
        </tr>
        <tr>
          <td><strong>Gap Factory</strong></td>
          <td>1</td>
          <td>Linen-Blend Apron Top restocked (you wishlisted this item)</td>
          <td><span class="badge badge-blue">Keep / Review</span> — You previously expressed interest. Check if still wanted.</td>
        </tr>
        <tr>
          <td><strong>Macy's</strong></td>
          <td>1</td>
          <td>Summer Favorites Sale — up to 50% off. Father's Day shirts &amp; shorts</td>
          <td><span class="badge badge-gray">Review</span> — Time-sensitive sale. Hours left per subject line.</td>
        </tr>
        <tr>
          <td><strong>Amazon / Amazon Alexa</strong></td>
          <td>1</td>
          <td>Prime Day June 23–26 — shop with Alexa+ (in Trash)</td>
          <td><span class="badge badge-gray">Delete</span> — Note Prime Day date. Email itself not needed.</td>
        </tr>
        <tr>
          <td><strong>Manychat</strong></td>
          <td>1</td>
          <td>"One channel away from your holy crap this works moment" — creator marketing</td>
          <td><span class="badge badge-gray">Ignore / Unsubscribe</span> — Low relevance. Unsubscribe if not using platform.</td>
        </tr>
        <tr>
          <td><strong>JetBlue Plus Card (Barclays)</strong></td>
          <td>1</td>
          <td>Earn your bonus — track rewards progress, account #2885</td>
          <td><span class="badge badge-blue">Review</span> — Check your actual rewards progress. Don't let a bonus expire.</td>
        </tr>
        <tr>
          <td><strong>CoinOut</strong></td>
          <td>1</td>
          <td>Earn 1,000 Bonus Coins for Day 2 — Food &amp; Beverage Journal participation</td>
          <td><span class="badge badge-gray">Ignore</span> — Low
<hr>
<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Job Search / Recruiters</td><td>7</td></tr>
<tr><td>Medical / Health</td><td>3</td></tr>
<tr><td>Other / Review</td><td>28</td></tr>
<tr><td>Promotional / Retail</td><td>5</td></tr>
<tr><td>Security / Risk</td><td>7</td></tr>
</table>
<p><strong>Audit Note:</strong> Every fetched email was reviewed and assigned to one category. Trash emails were included in review. Promotional and low-value emails were accounted for but deprioritized.</p>

