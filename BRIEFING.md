<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa W — August 17, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrapper { max-width: 1100px; margin: 0 auto; padding: 24px 16px 48px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px 28px; margin-bottom: 24px; }
  .header h1 { font-size: 26px; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 14px; color: #a0aec0; margin-top: 4px; }
  .header-meta { display: flex; gap: 28px; margin-top: 18px; flex-wrap: wrap; }
  .header-meta-item { background: rgba(255,255,255,0.08); border-radius: 8px; padding: 8px 16px; }
  .header-meta-item .label { font-size: 11px; color: #90cdf4; text-transform: uppercase; letter-spacing: 0.8px; }
  .header-meta-item .value { font-size: 18px; font-weight: 700; color: #fff; }

  /* SECTION TITLES */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 15px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #2d3748; border-left: 4px solid #4a90e2; padding-left: 10px; margin-bottom: 14px; }

  /* EXECUTIVE SUMMARY */
  .exec-summary { background: #fff; border-radius: 12px; padding: 20px 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .exec-bullet { display: flex; align-items: flex-start; gap: 10px; padding: 8px 0; border-bottom: 1px solid #edf2f7; }
  .exec-bullet:last-child { border-bottom: none; }
  .exec-icon { font-size: 18px; flex-shrink: 0; }
  .exec-text strong { display: block; font-size: 13px; color: #2d3748; }
  .exec-text span { font-size: 13px; color: #4a5568; }

  /* COLOR CARDS */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; border-left: 5px solid; }
  .card-red { background: #fff5f5; border-color: #e53e3e; }
  .card-yellow { background: #fffff0; border-color: #d69e2e; }
  .card-blue { background: #ebf8ff; border-color: #3182ce; }
  .card-green { background: #f0fff4; border-color: #38a169; }
  .card-purple { background: #faf5ff; border-color: #805ad5; }
  .card-gray { background: #f7fafc; border-color: #a0aec0; }
  .card-orange { background: #fffaf0; border-color: #dd6b20; }

  .card .card-title { font-weight: 700; font-size: 14px; margin-bottom: 4px; }
  .card .card-meta { font-size: 12px; color: #718096; margin-bottom: 6px; }
  .card .card-body { font-size: 13px; color: #2d3748; }
  .card .card-action { margin-top: 8px; font-size: 12px; font-weight: 600; }
  .card-red .card-action { color: #c53030; }
  .card-yellow .card-action { color: #b7791f; }
  .card-blue .card-action { color: #2b6cb0; }
  .card-green .card-action { color: #276749; }
  .card-purple .card-action { color: #553c9a; }

  /* BADGE */
  .badge { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
  .badge-red { background: #fed7d7; color: #c53030; }
  .badge-yellow { background: #fefcbf; color: #b7791f; }
  .badge-green { background: #c6f6d5; color: #276749; }
  .badge-blue { background: #bee3f8; color: #2b6cb0; }
  .badge-gray { background: #edf2f7; color: #4a5568; }
  .badge-purple { background: #e9d8fd; color: #553c9a; }
  .badge-orange { background: #feebc8; color: #c05621; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  th { background: #2d3748; color: #fff; padding: 10px 14px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.8px; }
  td { padding: 9px 14px; border-bottom: 1px solid #edf2f7; font-size: 13px; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f7fafc; }
  .triage-rescued td { background: #f0fff4; }
  .triage-inbox td { background: #ebf8ff; }
  .triage-auto td { background: #fff5f5; }
  .triage-manual td { background: #fffff0; }

  /* CALENDAR */
  .cal-day { background: #fff; border-radius: 10px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.06); overflow: hidden; }
  .cal-day-header { background: #2d3748; color: #fff; padding: 10px 18px; font-weight: 700; font-size: 13px; display: flex; justify-content: space-between; align-items: center; }
  .cal-day-header .day-label { font-size: 12px; color: #90cdf4; }
  .cal-today-header { background: linear-gradient(90deg, #3182ce, #2b6cb0); }
  .cal-event { padding: 12px 18px; border-bottom: 1px solid #edf2f7; }
  .cal-event:last-child { border-bottom: none; }
  .cal-event-time { font-weight: 700; font-size: 12px; color: #3182ce; margin-bottom: 3px; }
  .cal-event-name { font-weight: 700; font-size: 14px; }
  .cal-event-detail { font-size: 12px; color: #4a5568; margin-top: 3px; }
  .cal-event-link { font-size: 12px; color: #3182ce; word-break: break-all; }
  .cal-event-prep { font-size: 12px; color: #744210; background: #fefcbf; border-radius: 4px; padding: 3px 8px; display: inline-block; margin-top: 4px; }
  .cal-conflict { font-size: 12px; color: #c53030; background: #fed7d7; border-radius: 4px; padding: 3px 8px; display: inline-block; margin-top: 4px; }
  .cal-empty { padding: 12px 18px; color: #a0aec0; font-style: italic; font-size: 13px; }

  /* JOB PIPELINE */
  .job-card { background: #fff; border-radius: 10px; padding: 14px 18px; margin-bottom: 10px; box-shadow: 0 2px 6px rgba(0,0,0,0.06); border-left: 4px solid #38a169; display: flex; flex-direction: column; gap: 5px; }
  .job-card-title { font-weight: 700; font-size: 14px; }
  .job-card-org { font-size: 13px; color: #2b6cb0; }
  .job-card-detail { font-size: 12px; color: #4a5568; }
  .job-card-action { font-size: 12px; font-weight: 600; color: #276749; }

  /* DASHBOARD GRID */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-tile { background: #fff; border-radius: 10px; padding: 16px 18px; box-shadow: 0 2px 6px rgba(0,0,0,0.07); }
  .dash-tile .tile-label { font-size: 11px; text-transform: uppercase; letter-spacing: 0.8px; color: #718096; margin-bottom: 6px; }
  .dash-tile .tile-value { font-size: 24px; font-weight: 800; }
  .dash-tile .tile-sub { font-size: 12px; color: #4a5568; margin-top: 4px; }
  .tile-red .tile-value { color: #e53e3e; }
  .tile-yellow .tile-value { color: #d69e2e; }
  .tile-green .tile-value { color: #38a169; }
  .tile-blue .tile-value { color: #3182ce; }
  .tile-purple .tile-value { color: #805ad5; }

  /* PRIORITIES */
  .priority-list { counter-reset: plist; }
  .priority-item { background: #fff; border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.07); display: flex; gap: 16px; align-items: flex-start; counter-increment: plist; }
  .priority-num { background: #2d3748; color: #fff; font-size: 18px; font-weight: 800; width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
  .priority-num-1 { background: #e53e3e; }
  .priority-num-2 { background: #d69e2e; }
  .priority-num-3 { background: #38a169; }
  .priority-content strong { display: block; font-size: 15px; margin-bottom: 4px; }
  .priority-content span { font-size: 13px; color: #4a5568; }

  /* MISC */
  .tag { display: inline-block; background: #edf2f7; color: #4a5568; border-radius: 4px; padding: 1px 7px; font-size: 11px; margin-right: 4px; }
  .divider { height: 1px; background: #e2e8f0; margin: 20px 0; }
  .note { background: #ebf8ff; border-radius: 6px; padding: 8px 14px; font-size: 12px; color: #2b6cb0; margin-top: 8px; }
  .warn { background: #fff5f5; border-radius: 6px; padding: 8px 14px; font-size: 12px; color: #c53030; margin-top: 8px; }
  .sub-section { margin-bottom: 16px; }
  .sub-section-title { font-size: 13px; font-weight: 700; color: #4a5568; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px; }
  .inline-list { list-style: none; padding: 0; }
  .inline-list li { padding: 5px 0; border-bottom: 1px solid #edf2f7; font-size: 13px; }
  .inline-list li:last-child { border-bottom: none; }
  a { color: #3182ce; text-decoration: none; }
  a:hover { text-decoration: underline; }

  @media (max-width: 600px) {
    .header { padding: 20px; }
    .header-meta { gap: 12px; }
    th, td { padding: 7px 10px; }
  }
</style>
</head>
<body>
<div class="page-wrapper">

<!-- ══════════════════════════════════════════ -->
<!-- SECTION 0: EMAIL TRIAGE QUICK LIST        -->
<!-- ══════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📋 Email Triage Quick List</div>
  <table>
    <thead>
      <tr>
        <th style="width:130px">Status</th>
        <th style="width:220px">From</th>
        <th>Subject</th>
        <th style="width:260px">Summary</th>
      </tr>
    </thead>
    <tbody>
      <!-- INBOX ROWS -->
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Center for Veterinary Care</td>
        <td>Action Required: Payment failed for your Autoship order</td>
        <td>Pet Autoship payment failed — fix payment method to avoid disruption</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>VP, HR Business Partner - Technology at JPMorgan (up to $180K)</td>
        <td>High-fit VP HRBP role at JPMorgan — review and apply</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>Chief People Officer at Kinora Group</td>
        <td>CPO-level role alert — review fit and apply if interested</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>Head of People and Culture at NAACP Legal Defense and Education Fund</td>
        <td>Mission-driven senior HR leadership role — actively recruiting</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Amazon.com</td>
        <td>Shipped: 1 Skincare item</td>
        <td>Skincare order shipped — track delivery</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Amazon.com</td>
        <td>Shipped: 2 Jewelry and Health Care items</td>
        <td>Two additional items shipped — track delivery</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Match</td>
        <td>You've had a profile view from Stephen (54, New York)</td>
        <td>Profile view on Match — review Stephen's profile</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Bank of America</td>
        <td>Your statement is available — Money Market Savings 7549</td>
        <td>Monthly statement ready — review account</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>Sabrina Ramonov 🍄 on TikTok</td>
        <td>Self-forwarded TikTok link — AI/productivity creator</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>GitHub — anthropics/knowledge-work-plugins</td>
        <td>Self-forwarded GitHub link (Anthropic plugins repo) — sent twice</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>GitHub — anthropics/knowledge-work-plugins (duplicate)</td>
        <td>Duplicate self-forward of same GitHub repo</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>(No subject) — Substack note link</td>
        <td>Self-forwarded Substack note from Sabrina Ramonov</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>Blotato | Social Media APIs for AI Agents</td>
        <td>Self-forwarded tool link — AI social media API</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>How to Use Claude to Land Your Next Job | Maverick AI</td>
        <td>Job-search AI guide — relevant to current search</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>claude_code_guide_v4.pdf — Google Drive</td>
        <td>Self-forwarded Claude code guide PDF</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>Free AI Guides for ChatGPT, Claude &amp; Gemini | God of Prompt</td>
        <td>Self-forwarded AI prompt guide resource</td>
      </tr>
      <!-- TRASH SUMMARY ROWS -->
      <tr class="triage-auto">
        <td><span class="badge badge-red">🗑 AUTO-TRASHED</span></td>
        <td colspan="2">6 emails auto-trashed (newsletters/phishing) — see Trash Review</td>
        <td>Includes 1 phishing scam + 5 newsletter digests auto-removed</td>
      </tr>
      <tr class="triage-manual">
        <td><span class="badge badge-yellow">🗂 TRASHED</span></td>
        <td colspan="2">28 emails in Trash (manual/other) — see Trash Review</td>
        <td>Spam, job alerts, promotions, digests moved to trash</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ══════════════════════════════════════════ -->
<!-- SECTION 1: HEADER                         -->
<!-- ══════════════════════════════════════════ -->
<div class="header">
  <h1>☀️ Good Morning, Melissa</h1>
  <div class="subtitle">Executive Briefing — Prepared by Your Chief of Staff</div>
  <div class="header-meta">
    <div class="header-meta-item">
      <div class="label">Date</div>
      <div class="value">Monday, Aug 17, 2026</div>
    </div>
    <div class="header-meta-item">
      <div class="label">Emails Reviewed</div>
      <div class="value">50</div>
    </div>
    <div class="header-meta-item">
      <div class="label">Calendar Events</div>
      <div class="value">9</div>
    </div>
    <div class="header-meta-item">
      <div class="label">Action Required</div>
      <div class="value">5</div>
    </div>
    <div class="header-meta-item">
      <div class="label">Open Job Leads</div>
      <div class="value">7</div>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════ -->
<!-- SECTION 2: EXECUTIVE SUMMARY              -->
<!-- ══════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">⚡ Executive Summary</div>
  <div class="exec-summary">
    <div class="exec-bullet">
      <div class="exec-icon">🔴</div>
      <div class="exec-text">
        <strong>Biggest Risk / Urgent:</strong>
        <span>Your pet's Autoship payment failed at Center for Veterinary Care — action required immediately to avoid an order disruption. Additionally, a phishing scam (fake casino deposit) was auto-trashed and multiple unsolicited spam emails remain in your mailbox requiring cleanup.</span>
      </div>
    </div>
    <div class="exec-bullet">
      <div class="exec-icon">🟢</div>
      <div class="exec-text">
        <strong>Biggest Job Search / Opportunity:</strong>
        <span>Seven high-caliber HR/People leadership roles are actively being surfaced today — including VP HRBP at JPMorgan (~$180K), Senior Director People Partners at Honor ($230–255K), CPO at Kinora Group, Head of People &amp; Culture at NAACP LDF, and VP People at Clio. Your HR Networking Group meets Tuesday (RSVP pending) and you have a 1:1 with Monte Montoya Tuesday at 2 PM.</span>
      </div>
    </div>
    <div class="exec-bullet">
      <div class="exec-icon">🔵</div>
      <div class="exec-text">
        <strong>Biggest Calendar / Deadline:</strong>
        <span>This week includes Stella's vet appointment Tuesday 8/18 at 10 AM, the HR Networking &amp; Job Search Group Zoom on Wednesday 8/19 (RSVP still needed), a 1:1 with Monte Montoya Wednesday at 2 PM, and your Verizon Fios bill due Sunday 8/23. You also declined the Executive Roundtable on 8/20 — confirm that was intentional. Wegovy reminder window closes Tuesday 8/18.</span>
      </div>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════ -->
<!-- SECTION 3: ACTION REQUIRED                -->
<!-- ══════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">🚨 Action Required</div>

  <div class="card card-red">
    <div class="card-title">🔴 Fix Failed Payment — Pet Autoship</div>
    <div class="card-meta">From: Center for Veterinary Care &lt;centerforveterinarycare@outbound.ourvet.com&gt; | Aug 17, 2026</div>
    <div class="card-body">Your Autoship order payment failed. This may cause your pet's recurring supply order to be cancelled or delayed. Update your payment method immediately in your account portal.</div>
    <div class="card-action">➜ Action: Log into Center for Veterinary Care account and update payment method. | Due: Today</div>
  </div>

  <div class="card card-yellow">
    <div class="card-title">🟡 RSVP Needed — HR Networking &amp; Job Search Group Zoom</div>
    <div class="card-meta">From: Google Calendar | Event: Wed Aug 19, 2026 · 12:00–1:30 PM ET</div>
    <div class="card-body">You have not yet responded (status: needsAction) to the HR Networking &amp; Job Search Group Zoom on Wednesday. This is a key professional networking session with 180+ attendees. RSVP and add the Zoom link to your calendar.</div>
    <div class="card-action">➜ Action: Accept or decline the calendar invite. Zoom: https://us06web.zoom.us/j/81954171722 | Due: Today</div>
  </div>

  <div class="card card-yellow">
    <div class="card-title">🟡 RSVP Needed — HR Open Office Hours Zoom</div>
    <div class="card-meta">From: Google Calendar | Event: Thu Aug 20, 2026 · 12:00–1:00 PM ET</div>
    <div class="card-body">Thursday's HR Networking Open Office Hours Zoom also has no RSVP (status: needsAction). Note the event description requests no automated AI notetaking tools.</div>
    <div class="card-action">➜ Action: Accept or decline calendar invite. Zoom: https://us06web.zoom.us/j/85945371140 | Due: Today</div>
  </div>

  <div class="card card-yellow">
    <div class="card-title">🟡 Review Bank of America Statement — Money Market Savings 7549</div>
    <div class="card-meta">From: Bank of America &lt;onlinebanking@ealerts.bankofamerica.com&gt; | Aug 16, 2026</div>
    <div class="card-body">Your monthly statement is now available for your Money Market Savings account ending in 7549. Review for any unexpected charges or discrepancies.</div>
    <div class="card-action">➜ Action: Log into Bank of America and review statement. | Due: This week</div>
  </div>

  <div class="card card-yellow">
    <div class="card-title">🟡 Verizon Fios Bill Due</div>
    <div class="card-meta">From: Google Calendar | Event: Sun Aug 23, 2026 (all day)</div>
    <div class="card-body">Verizon Fios bill is due or arrives around August 23. Confirm payment is set up to avoid a late fee.</div>
    <div class="card-action">➜ Action: Confirm auto-pay or schedule manual payment. | Due: Aug 23</div>
  </div>
</div>

<!-- ══════════════════════════════════════════ -->
<!-- SECTION 4: FULL 7-DAY CALENDAR            -->
<!-- ══════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📅 Full 7-Day Calendar (Aug 17–23, 2026)</div>

  <!-- MONDAY AUG 17 -->
  <div class="cal-day">
    <div class="cal-day-header cal-today-header">
      <span>Monday, August 17, 2026</span>
      <span class="day-label">TODAY</span>
    </div>
    <div class="cal-event">
      <div class="cal-event-time">All Day (Aug 16–18)</div>
      <div class="cal-event-name">💊 Wegovy</div>
      <div class="cal-event-detail"><span class="badge badge-blue">Confirmed</span> · Reminder window</div>
      <div class="cal-event-prep">⚠ Reminder: Wegovy window closes tomorrow (Aug 18). Take dose if not yet done today.</div>
    </div>
  </div>

  <!-- TUESDAY AUG 18 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span>Tuesday, August 18, 2026</span>
      <span class="day-label">TOMORROW</span>
    </div>
    <div class="cal-event">
      <div class="cal-event-time">All Day (ends)</div>
      <div class="cal-event-name">💊 Wegovy (window ends)</div>
      <div class="cal-event-detail"><span class="badge badge-blue">Confirmed</span> · Last day of reminder window</div>
      <div class="cal-event-prep">⚠ Final day — ensure Wegovy dose is taken.</div>
    </div>
    <div class="cal-event">
      <div class="cal-event-time">10:00 AM – 11:00 AM ET</div>
      <div class="cal-event-name">🐾 Vet / Stella Vet Appointment</div>
      <div class="cal-event-detail"><span class="badge badge-blue">Confirmed</span> · Two calendar entries for same event (Vet + Stella Vet)</div>
      <div class="cal-event-prep">📋 Prep: Confirm appointment. Note: Pet Autoship payment failed — resolve today so Stella's supplies are not disrupted. Bring any health records or medication refill requests.</div>
      <div class="cal-conflict">⚠ Duplicate calendar entries ("Vet" and "Stella Vet") — same time slot. Consider deleting one.</div>
    </div>
  </div>

  <!-- WEDNESDAY AUG 19 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span>Wednesday, August 19, 2026</span>
      <span class="day-label">IN 2 DAYS</span>
    </div>
    <div class="cal-event">
      <div class="cal-event-time">12:00 PM – 1:30 PM ET</div>
      <div class="cal-event-name">👥 HR Networking &amp; Job Search Group — Zoom 2</div>
      <div class="cal-event-detail"><span class="badge badge-yellow">RSVP NEEDED (needsAction)</span> · 180+ attendees · Large group session</div>
      <div class="cal-event-link">🔗 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a></div>
      <div class="cal-event-prep">📋 Prep: RSVP today. Review HR Networking Team Guidelines (linked in invite). Prepare brief job search update to share. Also a duplicate "Network" event confirmed for same slot — consolidate.</div>
      <div class="cal-conflict">⚠ Duplicate event: "Network" (confirmed) overlaps exactly with HR Networking Zoom. Merge or delete the duplicate.</div>
    </div>
    <div class="cal-event">
      <div class="cal-event-time">12:00 PM – 1:30 PM ET</div>
      <div class="cal-event-name">🗂 Network (duplicate)</div>
      <div class="cal-event-detail"><span class="badge badge-blue">Confirmed</span> · Appears to be a personal placeholder for the same HR Networking Zoom above</div>
      <div class="cal-conflict">⚠ Overlaps with HR Networking Zoom — consider deleting this duplicate entry.</div>
    </div>
    <div class="cal-event">
      <div class="cal-event-time">2:00 PM – 3:00 PM ET</div>
      <div class="cal-event-name">☕ M&amp;M — 1:1 with Monte Montoya</div>
      <div class="cal-event-detail"><span class="badge badge-green">Accepted</span> · Attendee: monte.montoya@gmail.com</div>
      <div class="cal-event-prep">📋 Prep: Prepare agenda for discussion with Monte. Likely job search / networking conversation based on context. Follows immediately after the HR Networking session — allow 30 min buffer.</div>
    </div>
  </div>

  <!-- THURSDAY AUG 20 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span>Thursday, August 20, 2026</span>
      <span class="day-label">IN 3 DAYS</span>
    </div>
    <div class="cal-event">
      <div class="cal-event-time">9:00 AM – 10:30 AM ET</div>
      <div class="cal-event-name">🏛 Executive Roundtable (Declined)</div>
      <div class="cal-event-detail"><span class="badge badge-gray">DECLINED</span> · Host: John Madigan · Zoom</div>
      <div class="cal-event-link">🔗 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> · Meeting ID: 207 786 667 · Password: 205454</div>
      <div class="cal-event-prep">📋 Note: You declined this event. Confirm this was intentional — John Madigan may be an important executive contact. Consider a brief note to John if the decline was due to a conflict.</div>
    </div>
    <div class="cal-event">
      <div class="cal-event-time">12:00 PM – 1:00 PM ET</div>
      <div class="cal-event-name">👥 HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
      <div class="cal-event-detail"><span class="badge badge-yellow">RSVP NEEDED (needsAction)</span> · Note: No AI notetaking tools permitted</div>
      <div class="cal-event-link">🔗 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a></div>
      <div class="cal-event-prep">📋 Prep: RSVP today. Disable Otter.ai or any AI meeting assistant for this session per organizer request.</div>
    </div>
  </div>

  <!-- FRIDAY AUG 21 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span>Friday, August 21, 2026</span>
      <span class="day-label">IN 4 DAYS</span>
    </div>
    <div class="cal-empty">No events scheduled.</div>
  </div>

  <!-- SATURDAY AUG 22 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span>Saturday, August 22, 2026</span>
      <span class="day-label">IN 5 DAYS</span>
    </div>
    <div class="cal-empty">No events scheduled.</div>
  </div>

  <!-- SUNDAY AUG 23 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span>Sunday, August 23, 2026</span>
      <span class="day-label">IN 6 DAYS</span>
    </div>
    <div class="cal-event">
      <div class="cal-event-time">All Day</div>
      <div class="cal-event-name">💳 Verizon Fios Bill</div>
      <div class="cal-event-detail"><span class="badge badge-blue">Confirmed</span> · Bill reminder</div>
      <div class="cal-event-prep">📋 Confirm auto-pay is enabled or schedule manual payment before this date.</div>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════ -->
<!-- SECTION 5: JOB SEARCH & PIPELINE          -->
<!-- ══════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>

  <div class="job-card">
    <div style="display:flex;justify-content:space-between;align-items:flex-start;">
      <div class="job-card-title">Senior Director, People Partners (Remote)</div>
      <span class="badge badge-green">HIGH FIT</span>
    </div>
    <div class="job-card-org">🏢 Honor · Source: Indeed + LinkedIn</div>
    <div class="job-card-detail">💰 $230,000–$255,000/year · Remote · 1 school alum connection on LinkedIn</div>
    <div class="job-card-action">➜ Review job description and apply. Strong compensation match. Dual sourcing (Indeed + LinkedIn) confirms active role.</div>
  </div>

  <div class="job-card">
    <div style="display:flex;justify-content:space-between;align-items:flex-start;">
      <div class="job-card-title">Vice President, HR Business Partner — Technology</div>
      <span class="badge badge-green">HIGH FIT</span>
    </div>
    <div class="job-card-org">🏢 JPMorgan Chase · Source: LinkedIn Job Alert</div>
    <div class="job-card-detail">💰 Up to $180,000/year · 1 LinkedIn connection · Tech-focused HRBP role</div>
    <div class="job-card-action">➜ Leverage LinkedIn connection for a warm introduction before applying.</div>
  </div>

  <div class="job-card">
    <div style="display:flex;justify-content:space-between;align-items:flex-start;">
      <div class="job-card-title">Chief People Officer</div>
      <span class="badge badge-green">HIGH FIT</span>
    </div>
    <div class="job-card-org">🏢 Kinora Group · Source: LinkedIn Job Alert</div>
    <div class="job-card-detail">CPO-level opportunity — compensation not listed. Research company and role scope.</div>
    <div class="job-card-action">➜ Research Kinora Group. Apply if mission and size align.</div>
  </div>

  <div class="job-card">
    <div style="display:flex;justify-content:space-between;align-items:flex-start;">
      <div class="job-card-title">Head of People and Culture</div>
      <span class="badge badge-green">HIGH FIT</span>
    </div>
    <div class="job-card-org">🏢 NAACP Legal Defense and Education Fund · Source: LinkedIn</div>
    <div class="job-card-detail">Actively recruiting · Mission-driven organization · Impactful culture leadership role</div>
    <div class="job-card-action">➜ Review role. If mission-aligned, apply promptly — actively recruiting signals urgency.</div>
  </div>

  <div class="job-card">
    <div style="display:flex;justify-content:space-between;align-items:flex-start;">
      <div class="job-card-title">VP, People Business Partners &amp; Talent Development</div>
      <span class="badge badge-blue">MEDIUM FIT</span>
    </div>
    <div class="job-card-org">🏢 Clio · Source: LinkedIn Job Alert</div>
    <div class="job-card-detail">Actively recruiting · Tech-adjacent legal software company</div>
    <div class="job-card-action">➜ Review company size and culture. Strong title alignment. Apply if tech sector is desirable.</div>
  </div>

  <div class="job-card">
    <div style="display:flex;justify-content:space-between;align-items:flex-start;">
      <div class="job-card-title">5 New Jobs — CPO / Lead Talent / Culture / Change</div>
      <span class="badge badge-blue">MEDIUM FIT</span>
    </div>
    <div class="job-card-org">📧 JobLeads · Source: Saved Search Alert</div>
    <div class="job-card-detail">JobLeads saved search results based on Chief People Officer / Lead Talent / Culture / Change criteria</div>
    <div class="job-card-action">➜ Review JobLeads results — email is in Trash. Retrieve and scan the 5 listings before deleting.</div>
  </div>

  <!-- NETWORKING -->
  <div style="margin-top:14px">
    <div class="sub-section-title">🤝 Networking &amp; Group Events</div>
    <div class="card card-green">
      <div class="card-title">HR Networking &amp; Job Search Group — Zoom (Wed Aug 19, 12–1:30 PM)</div>
      <div class="card-body">Large peer HR networking session with 180+ members. RSVP pending. Great opportunity to share updates, learn from peers, and expand your network.</div>
      <div class="card-action">➜ RSVP today. Prepare a 60-second job search update.</div>
    </div>
    <div class="card card-green">
      <div class="card-title">1:1 with Monte Montoya — "M&amp;M" (Wed Aug 19, 2–3 PM)</div>
      <div class="card-body">Private networking/mentoring meeting confirmed with Monte Montoya. Likely a job search support conversation. Follows the group session — allow a bio break between calls.</div>
      <div class="card-action">➜ Prepare agenda and key talking points for Monte.</div>
    </div>
    <div class="card card-blue">
      <div class="card-title">HR Open Office Hours — Zoom (Thu Aug 20, 12–1 PM)</div>
      <div class="card-body">Open discussion format — no AI notetaking permitted. RSVP pending. Good informal networking session.</div>
      <div class="card-action">➜ RSVP and disable Otter.ai / AI assistants for this session.</div>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════ -->
<!-- SECTION 6: FULL EMAIL REVIEW BY CATEGORY  -->
<!-- ══════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📬 Full Email Review by Category</div>

  <!-- SECURITY / RISK -->
  <div class="card card-red">
    <div class="card-title">🔴 Security / Risk — 5 Emails</div>
    <div class="card-meta">Senders: zbsupportqfpe (fake casino), sebcvpyfhdqscq (ED spam), idxsgkm4wq (explicit spam), zwdeoklwkbglwb (ED spam), mwgzwejskzfulm (GLP-1 spam)</div>
    <div class="card-body">
      <ul class="inline-list">
        <li><strong>AUTO-TRASHED — PHISHING:</strong> "You received a direct deposit of $13,963.99" (zbsupportqfpe@msspuftimqdgdimrlsboiuwh.com) · Fake casino deposit scam with broken template placeholder in subject. <em>Reason: Advance-fee/scam lure — auto-removed.</em></li>
        <li><strong>SPAM (Not trashed):</strong> "biggest performance insecurity" — ED supplement spam from random domain. In Trash manually.</li>
        <li><strong>SPAM (Not trashed):</strong> "F*ckMeHard" — explicit spam from random domain. Still in inbox/not trashed — delete immediately.</li>
        <li><strong>SPAM (Not trashed):</strong> "Rock Hard / ½ Teaspoon Brown Powder kills ED?" — spam from random domain. Still in mailbox — delete.</li>
        <li><strong>SPAM (Not trashed):</strong> "Direct_Meds_Care_Team" — GLP-1 medication spam from random domain. Still in mailbox — delete.</li>
      </ul>
    </div>
    <div class="card-action">➜ Action: Delete all 4 remaining spam emails immediately. The phishing email was auto-trashed — no further action needed.</div>
  </div>

  <!-- JOB SEARCH -->
  <div class="card card-green">
    <div class="card-title">🟢 Job Search — 7 Emails</div>
    <div class="card-meta">Senders: LinkedIn Job Alerts (4), Indeed (1), JobLeads (1), Melissa W / Maverick AI (1)</div>
    <div class="card-body">
      <ul class="inline-list">
        <li><strong>LinkedIn:</strong> VP HR Business Partner - Technology @ JPMorgan (~$180K) — <span class="badge badge-green">HIGH</span> — In Inbox</li>
        <li><strong>LinkedIn:</strong> Chief People Officer @ Kinora Group — <span class="badge badge-green">HIGH</span> — In Inbox</li>
        <li><strong>LinkedIn:</strong> Head of People and Culture @ NAACP LDF — <span class="badge badge-green">HIGH</span> — Actively recruiting — In Inbox</li>
        <li><strong>LinkedIn:</strong> Senior Director, People Partners @ Honor — <span class="badge badge-blue">MED</span> — In Trash (previously seen via LinkedIn)</li>
        <li><strong>LinkedIn:</strong> VP, People Business Partners &amp; Talent Development @ Clio — <span class="badge badge-blue">MED</span> — Seen/read</li>
        <li><strong>Indeed:</strong> Senior Director, People Partners @ Honor ($230–255K) — <span class="badge badge-green">HIGH</span> — In Trash</li>
        <li><strong>JobLeads:</strong> 5 new jobs matching CPO/Lead Talent/Culture/Change search — In Trash</li>
      </ul>
    </div>
    <div class="card-action">➜ Action: Review all 7, retrieve JobLeads and Indeed emails from Trash, apply to top 3 roles this week.</div>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="card card-purple">
    <div class="card-title">🟣 Professional Development — 7 Emails</div>
    <div class="card-meta">Senders: Melissa W (self-forwards of AI tools/guides), LinkedIn (HRPN notification), HomeAgain (community), Substack verification</div>
    <div class="card-body">
      <ul class="inline-list">
        <li><strong>Self-forward:</strong> GitHub anthropics/knowledge-work-plugins (sent twice — 2 emails)</li>
        <li><strong>Self-forward:</strong> Sabrina Ramonov 🍄 TikTok link</li>
        <li><strong>Self-forward:</strong> Substack note from Sabrina Ramonov (no subject)</li>
        <li><strong>Self-forward:</strong> Blotato — Social Media APIs for AI Agents</li>
        <li><strong>Self-forward:</strong> How to Use Claude to Land Your Next Job (Maverick AI)</li>
        <li><strong>Self-forward:</strong> claude_code_guide_v4.pdf (Google Drive)</li>
        <li><strong>Self-forward:</strong> Free AI Guides — God of Prompt</li>
        <li><strong>LinkedIn:</strong> HR Professionals Network (HRPN) — 2 new page updates</li>
        <li><strong>Substack:</strong> Verification code 544481 (already used/expired)</li>
        <li><strong>Veeraj's Substack:</strong> Welcome email (in Trash)</li>
      </ul>
    </div>
    <div class="card-action">➜ Action: Organize AI guides and self-forwards into a resource folder. Review HRPN LinkedIn updates. Delete duplicate GitHub email. Substack code is expired — ignore.</div>
  </div>

  <!-- MEDICAL / HEALTH -->
  <div class="card card-orange">
    <div class="card-title">🟠 Medical / Health — 2 Emails</div>
    <div class="card-meta">Senders: Center for Veterinary Care, Calendar (Wegovy)</div>
    <div class="card-body">
      <ul class="inline-list">
        <li><strong>Center for Veterinary Care:</strong> Payment failed for Autoship order — <span class="badge badge-red">URGENT</span> — In Inbox</li>
        <li><strong>Calendar:</strong> Wegovy reminder (Aug 16–18 window) — take dose if not yet done</li>
      </ul>
    </div>
    <div class="card-action">➜ Action: Fix vet Autoship payment immediately. Confirm Wegovy dose taken today.</div>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="card card-yellow">
    <div class="card-title">🟡 Financial / Billing — 2 Emails</div>
    <div class="card-meta">Senders: Bank of America, Amazon.com</div>
    <div class="card-body">
      <ul class="inline-list">
        <li><strong>Bank of America:</strong> Statement available — Money Market Savings 7549 — In Inbox</li>
        <li><strong>Amazon:</strong> Order confirmation — 1 Luggage item (read, not in inbox) — Ordered at 1:09 AM</li>
      </ul>
    </div>
    <div class="card-action">➜ Action: Review BofA statement this week. Confirm luggage order is expected.</div>
  </div>

  <!-- PERSONAL -->
  <div class="card card-blue">
    <div class="card-title">🔵 Personal — 4 Emails</div>
    <div class="card-meta">Senders: Match.com (2), Netflix (1), HomeAgain PetRescuers (1)</div>
    <div class="card-body">
      <ul class="inline-list">
        <li><strong>Match:</strong> Profile view from Stephen (54, New York) — In Inbox</li>
        <li><strong>Match:</strong> Jay likes you — (read, not in inbox)</li>
        <li><strong>Netflix:</strong> New movie recommendation — thriller about online romance + serial killer — Not in inbox</li>
        <li><strong>HomeAgain:</strong> Lost cat "Tang" — last seen 120th St &amp; Hillside Ave, Richmond Hill, NY 11418 — keep an eye out</li>
      </ul>
    </div>
    <div class="card-action">➜ Action: Check Match profile if interested. Note lost cat in your neighborhood.</div>
  </div>

  <!-- AMAZON ORDERS/SHIPMENTS -->
  <div class="card card-blue">
    <div class="card-title">🔵 Amazon Orders &amp; Shipments — 4 Emails</div>
    <div class="card-meta">Sender: Amazon.com (auto-confirm and shipment-tracking)</div>
    <div class="card-body">
      <ul class="inline-list">
        <li><strong>Ordered:</strong> 1 Skincare item (confirmed 2:40 AM)</li>
        <li><strong>Shipped:</strong> 1 Skincare item (shipped 6:06 AM) — In Inbox</li>
        <li><strong>Shipped:</strong> 2 Jewelry and Health Care items (shipped 5:13 AM) — In Inbox</li>
        <li><strong>Ordered:</strong> 1 Luggage item (confirmed 1:09 AM, read)</li>
      </ul>
    </div>
    <div class="card-action">➜ Action: Track all 3 shipments. Confirm luggage order is expected — ordered at 1 AM.</div>
  </div>

  <!-- NEWSLETTERS / SUBSCRIPTIONS -->
  <div class="card card-purple">
    <div class="card-title">🟣 Newsletters &amp; Subscriptions — 8 Emails</div>
    <div class="card-meta">Senders: Medium, 1% Better, Dylan's Diary, The Daily Skimm, Talent Edge Weekly, Otter.ai, Nextdoor, Alison Courses, Veeraj's Substack</div>
    <div class="card-body">
      <ul class="inline-list">
        <li><strong>AUTO-TRASHED:</strong> Medium Daily Digest (newsletter_trashed: true) — "Open source models are good enough"</li>
        <li><strong>AUTO-TRASHED:</strong> Kohl's cart abandonment (newsletter_trashed: true)</li>
        <li><strong>AUTO-TRASHED:</strong> Gap Factory Friends &amp; Family (newsletter_trashed: true) — "Tees/jeans 50% off"</li>
        <li><strong>In Trash:</strong> 1% Better newsletter — "Hayden Panettiere Dies, Pacific Uncovered…"</li>
        <li><strong>In Trash:</strong> Dylan's Diary — "The Slowest-Moving Train Wreck in History"</li>
        <li><strong>In Trash:</strong> The Daily Skimm — "A soup-er summer tip"</li>
        <li><strong>In Trash:</strong> Talent Edge Weekly Issue 360 — HR professional development</li>
        <li><strong>In Trash:</strong> Otter.ai — Upcoming meetings digest</li>
        <li><strong>In Trash:</strong> Nextdoor — Yorkville neighborhood rat problem post</li>
        <li><strong>In Trash:</strong> Alison Courses — Free course discovery</li>
        <li><strong>In Trash:</strong> Veeraj's Substack — Welcome email</li>
      </ul>
    </div>
    <div class="card-action">➜ Action: Rescue Talent Edge Weekly (HR professional value). Unsubscribe from low-value digests. Delete the rest.</div>
  </div>

  <!-- PROMOTIONAL / RETAIL -->
  <div class="card card-gray">
    <div class="card-title">⚪ Promotional / Retail — 4 Emails</div>
    <div class="card-meta">Senders: Kohl's (2), Gap Factory (2)</div>
    <div class="card-body">
      <ul class="inline-list">
        <li><strong>Kohl's:</strong> "Get your home ready for fall" — In Trash</li>
        <li><strong>Kohl's:</strong> "Your cart's feeling empty" — AUTO-TRASHED (newsletter_trashed)</li>
        <li><strong>Gap Factory:</strong> "50% off clearance + free shipping + extra 15% off" — In Trash</li>
        <li><strong>Gap Factory:</strong> "Tees/jeans/logo: 50% off" — AUTO-TRASHED (newsletter_trashed)</li>
      </ul>
    </div>
    <div class="card-action">➜ Action: Delete all. Unsubscribe from Kohl's and Gap Factory if no longer relevant.</div>
  </div>

  <!-- SAFE TO DELETE / IGNORE -->
  <div class="card card-gray">
    <div class="card-title">⚪ Safe to Delete / Ignore — 6 Emails</div>
    <div class="card-meta">Senders: Various spam/random domains, Verizon, Men's_Health spam</div>
    <div class="card-body">
      <ul class="inline-list">
        <li><strong>Men's Health (fake):</strong> "Bill Gates discovers why 40 million men over 50 are going soft" — nspwpbyjguv@fshx.eilogxdnexzdd.us — Spam</li>
        <li><strong>ForceX:</strong> "He fixed age-related bedroom issues" — spam from random domain — In Trash</li>
        <li><strong>Verizon:</strong> "Your entertainment could cost way less" — In Trash — promotional upsell</li>
        <li><strong>Melissa W (self-forward, trashed):</strong> AI Harness Architect Skill | Learn AI With Mariah — In Trash</li>
        <li><strong>Melissa W (self-forward, trashed):</strong> From-Scratch /route Setup Guide — Fable 5 + GPT-5.6 Sol — In Trash</li>
        <li><strong>Substack:</strong> Verification code 544481 — already expired — safe to delete</li>
      </ul>
    </div>
    <div class="card-action">➜ Action: Delete all. No follow-up needed.</div>
  </div>

</div>

<!-- ══════════════════════════════════════════ -->
<!-- SECTION 7: TRASH REVIEW                   -->
<!-- ══════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">🗑 Trash Review</div>

  <div class="sub-section">
    <div class="sub-section-title" style="color:#276749">✅ Restore Immediately</div>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Reason to Restore</th></tr></thead>
      <tbody>
        <tr>
          <td>Indeed</td>
          <td>Senior Director, People Partners @ Honor ($230–255K)</td>
          <td>High-value job lead — $230–255K salary, remote. Active opportunity matching your search criteria.</td>
        </tr>
        <tr>
          <td>JobLeads</td>
          <td>5 New Jobs — CPO / Lead Talent / Culture / Change</td>
          <td>Saved search results with 5 new listings. Should be reviewed before deleting.</td>
        </tr>
        <tr>
          <td>Brian Heger / Talent Edge Weekly</td>
          <td>Talent Edge Weekly — Issue 360</td>
          <td>High-value HR professional development newsletter — directly relevant to your field and job search.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="sub-section" style="margin-top:16px">
    <div class="sub-section-title" style="color:#b7791f">🔍 Review Before Deleting</div>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Notes</th></tr></thead>
      <tbody>
        <tr>
          <td>LinkedIn Job Alerts</td>
          <td>Senior Director, People Partners (Remote) at Honor</td>
          <td>Duplicate of Indeed alert for Honor role — already surfaced above. Can delete if you've noted the role.</td>
        </tr>
        <tr>
          <td>Otter.ai</td>
          <td>Your upcoming meetings</td>
          <td>May contain useful weekly meeting schedule. Review quickly then delete.</td>
        </tr>
        <tr>
          <td>Nextdoor (Yorkville)</td>
          <td>RAT problem in neighbor's yard</td>
          <td>Community alert — relevant if rats may affect your area. Quick read then delete.</td>
        </tr>
        <tr>
          <td>Melissa W (self-forward)</td>
          <td>AI Harness Architect Skill | Learn AI With Mariah</td>
          <td>Self-forwarded resource — review if you haven't already visited the link.</td>
        </tr>
        <tr>
          <td>Melissa W (self-forward)</td>
          <td>From-Scratch /route Setup Guide — Fable 5 + GPT-5.6 Sol</td>
          <td>Self-forwarded AI workflow guide — review before deleting if relevant to your AI learning path.</td>
        </tr>
        <tr>
          <td>1% Better Newsletter</td>
          <td>Hayden Panettiere Dies, Pacific Uncovered, Beckham Workout</td>
          <td>Lifestyle/wellness newsletter — determine if you want to keep subscription or unsubscribe.</td>
        </tr>
        <tr>
          <td>Dylan's Diary</td>
          <td>The Slowest-Moving Train Wreck in History</td>
          <td>Finance/markets
