<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa Weiss — Friday, July 10, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 16px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header .subtitle { font-size: 15px; color: #a8b2c8; margin-top: 4px; }
  .header .meta-row { display: flex; gap: 32px; margin-top: 20px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.08); border-radius: 10px; padding: 10px 18px; text-align: center; }
  .header .meta-item .val { font-size: 22px; font-weight: 700; color: #e2e8f0; }
  .header .meta-item .lbl { font-size: 11px; color: #a8b2c8; text-transform: uppercase; letter-spacing: 0.8px; }

  /* SECTION TITLES */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; padding: 10px 16px; border-radius: 8px 8px 0 0; display: flex; align-items: center; gap: 8px; }
  .section-body { border-radius: 0 0 12px 12px; padding: 16px; }

  /* COLOR THEMES */
  .red .section-title    { background: #c0392b; color: #fff; }
  .red .section-body     { background: #fff5f5; border: 1px solid #f5c6c6; border-top: none; }
  .yellow .section-title { background: #e67e22; color: #fff; }
  .yellow .section-body  { background: #fffbf0; border: 1px solid #fce5b0; border-top: none; }
  .blue .section-title   { background: #2980b9; color: #fff; }
  .blue .section-body    { background: #f0f7ff; border: 1px solid #b8d9f5; border-top: none; }
  .green .section-title  { background: #27ae60; color: #fff; }
  .green .section-body   { background: #f0fff6; border: 1px solid #b2dfc6; border-top: none; }
  .purple .section-title { background: #8e44ad; color: #fff; }
  .purple .section-body  { background: #faf0ff; border: 1px solid #d9b8f5; border-top: none; }
  .gray .section-title   { background: #7f8c8d; color: #fff; }
  .gray .section-body    { background: #f8f9fa; border: 1px solid #dee2e6; border-top: none; }
  .dark .section-title   { background: #2c3e50; color: #fff; }
  .dark .section-body    { background: #f5f6f8; border: 1px solid #ccd0d6; border-top: none; }

  /* CARDS */
  .card { background: #fff; border-radius: 10px; padding: 14px 18px; margin-bottom: 12px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
  .card .card-label { display: inline-block; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; padding: 2px 8px; border-radius: 20px; margin-bottom: 6px; }
  .label-red    { background: #fde8e8; color: #c0392b; }
  .label-yellow { background: #fef3cd; color: #b7770d; }
  .label-blue   { background: #d6ecff; color: #1a6fad; }
  .label-green  { background: #d4f4e2; color: #1e7e4a; }
  .label-purple { background: #ead6f7; color: #7b1fa2; }
  .label-gray   { background: #e9ecef; color: #495057; }
  .card h4 { font-size: 14px; font-weight: 700; color: #1a1a2e; margin-bottom: 4px; }
  .card .card-meta { font-size: 12px; color: #6c757d; margin-bottom: 6px; }
  .card .card-row { display: flex; gap: 8px; align-items: baseline; flex-wrap: wrap; }
  .card .card-field { font-size: 12px; }
  .card .card-field strong { color: #2c3e50; }

  /* BULLETS */
  ul.brief-list { list-style: none; padding: 0; }
  ul.brief-list li { padding: 7px 0; border-bottom: 1px solid #eee; font-size: 13px; }
  ul.brief-list li:last-child { border-bottom: none; }
  ul.brief-list li::before { content: "▸ "; color: #888; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #2c3e50; color: #fff; padding: 9px 12px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.6px; }
  td { padding: 8px 12px; border-bottom: 1px solid #e9ecef; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #f8f9fa; }
  .badge { display: inline-block; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 700; }
  .badge-high   { background: #fde8e8; color: #c0392b; }
  .badge-medium { background: #fef3cd; color: #b7770d; }
  .badge-low    { background: #e9ecef; color: #495057; }
  .badge-green  { background: #d4f4e2; color: #1e7e4a; }
  .badge-blue   { background: #d6ecff; color: #1a6fad; }
  .badge-red    { background: #fde8e8; color: #c0392b; }
  .badge-yellow { background: #fef3cd; color: #b7770d; }
  .badge-purple { background: #ead6f7; color: #7b1fa2; }
  .badge-gray   { background: #e9ecef; color: #495057; }

  /* EXEC SUMMARY BULLETS */
  .exec-bullet { display: flex; align-items: flex-start; gap: 12px; padding: 12px 16px; border-radius: 10px; margin-bottom: 10px; }
  .exec-bullet .icon { font-size: 22px; flex-shrink: 0; }
  .exec-bullet .text strong { display: block; font-size: 14px; }
  .exec-bullet .text span { font-size: 13px; color: #555; }
  .exec-bullet-red    { background: #fff5f5; border-left: 4px solid #c0392b; }
  .exec-bullet-green  { background: #f0fff6; border-left: 4px solid #27ae60; }
  .exec-bullet-yellow { background: #fffbf0; border-left: 4px solid #e67e22; }

  /* CALENDAR DAY */
  .cal-day { background: #fff; border-radius: 10px; margin-bottom: 12px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); overflow: hidden; }
  .cal-day-header { background: #2980b9; color: #fff; padding: 8px 16px; font-weight: 700; font-size: 13px; display: flex; justify-content: space-between; align-items: center; }
  .cal-event { padding: 10px 16px; border-bottom: 1px solid #eef2f7; }
  .cal-event:last-child { border-bottom: none; }
  .cal-event .evt-time { font-size: 12px; font-weight: 700; color: #2980b9; min-width: 120px; display: inline-block; }
  .cal-event .evt-title { font-size: 13px; font-weight: 700; color: #1a1a2e; }
  .cal-event .evt-detail { font-size: 12px; color: #6c757d; margin-top: 3px; }
  .cal-event .evt-badges { margin-top: 4px; display: flex; gap: 6px; flex-wrap: wrap; }
  .rsvp-yes    { background: #d4f4e2; color: #1e7e4a; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 700; }
  .rsvp-no     { background: #fde8e8; color: #c0392b; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 700; }
  .rsvp-pending { background: #fef3cd; color: #b7770d; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 700; }
  .rsvp-allday  { background: #ead6f7; color: #7b1fa2; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 700; }
  .conflict-warn { background: #c0392b; color: #fff; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 700; }

  /* DASHBOARD GRID */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 14px; }
  .dash-tile { background: #fff; border-radius: 12px; padding: 16px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); text-align: center; }
  .dash-tile .tile-val { font-size: 32px; font-weight: 800; }
  .dash-tile .tile-lbl { font-size: 12px; color: #6c757d; text-transform: uppercase; letter-spacing: 0.6px; margin-top: 4px; }
  .dash-tile.red-tile   { border-top: 4px solid #c0392b; }
  .dash-tile.yellow-tile { border-top: 4px solid #e67e22; }
  .dash-tile.green-tile { border-top: 4px solid #27ae60; }
  .dash-tile.blue-tile  { border-top: 4px solid #2980b9; }
  .dash-tile.purple-tile { border-top: 4px solid #8e44ad; }
  .dash-tile.gray-tile  { border-top: 4px solid #7f8c8d; }

  /* MISC */
  .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  @media (max-width: 680px) { .two-col { grid-template-columns: 1fr; } .header .meta-row { gap: 12px; } }
  .note { font-size: 12px; color: #888; font-style: italic; margin-top: 8px; }
  .divider { border: none; border-top: 2px solid #e9ecef; margin: 28px 0; }
  .highlight { color: #c0392b; font-weight: 700; }
  .chip { display: inline-block; background: #e9ecef; border-radius: 20px; padding: 2px 10px; font-size: 11px; color: #555; margin: 2px; }
  .warning-box { background: #fff3cd; border: 1px solid #ffc107; border-radius: 8px; padding: 10px 14px; font-size: 13px; margin-bottom: 10px; }
  .info-box { background: #d6ecff; border: 1px solid #2980b9; border-radius: 8px; padding: 10px 14px; font-size: 13px; margin-bottom: 10px; }
  .success-box { background: #d4f4e2; border: 1px solid #27ae60; border-radius: 8px; padding: 10px 14px; font-size: 13px; margin-bottom: 10px; }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 1 · HEADER
════════════════════════════════════════════════════════════════ -->
<div class="header">
  <div class="subtitle">EXECUTIVE MORNING BRIEFING</div>
  <h1>Good Morning, Melissa ☀️</h1>
  <div class="subtitle">Friday, July 10, 2026 &nbsp;|&nbsp; Prepared by your Executive Chief of Staff</div>
  <div class="meta-row">
    <div class="meta-item"><div class="val">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="meta-item"><div class="val">10</div><div class="lbl">Calendar Events</div></div>
    <div class="meta-item"><div class="val">2</div><div class="lbl">Meetings Today</div></div>
    <div class="meta-item"><div class="val">3</div><div class="lbl">Urgent Actions</div></div>
    <div class="meta-item"><div class="val">5</div><div class="lbl">RSVPs Pending</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 2 · EXECUTIVE SUMMARY
════════════════════════════════════════════════════════════════ -->
<div class="section dark">
  <div class="section-title">📋 Executive Summary</div>
  <div class="section-body">
    <div class="exec-bullet exec-bullet-red">
      <div class="icon">🚨</div>
      <div class="text">
        <strong>Biggest Risk / Urgent Item</strong>
        <span>Chase Slate Visa payment is due <strong>July 15</strong> — only 5 days away. Also: your automated Daily Briefing workflow <strong>FAILED</strong> today at 7:08 AM ET and needs a manual re-run. Two spam/phishing emails flagged in inbox area.</span>
      </div>
    </div>
    <div class="exec-bullet exec-bullet-green">
      <div class="icon">💼</div>
      <div class="text">
        <strong>Biggest Job Search / Opportunity Item</strong>
        <span>You have an <strong>Oscar Health phone screen TODAY at 2:00 PM</strong> for "People Strategy Lead." LinkedIn also surfaced a Senior Director HRBP role at Beacon Hill (up to $250K/year) — high-value lead requiring prompt application review. Two LinkedIn connection requests pending response.</span>
      </div>
    </div>
    <div class="exec-bullet exec-bullet-yellow">
      <div class="icon">📅</div>
      <div class="text">
        <strong>Biggest Calendar / Deadline Item</strong>
        <span>Today is packed: Oscar phone screen at 2:00 PM, then a doctor appointment at 3:30 PM. Next week includes Stephanie's infusion (Mon), Stella meeting (Tue), bone density scan (Wed), HR networking Zoom (Wed), and Tea with LeiLani networking event in NYC (Thu). Two upcoming events still need RSVPs.</span>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 3 · ACTION REQUIRED
════════════════════════════════════════════════════════════════ -->
<div class="section yellow">
  <div class="section-title">⚡ Action Required</div>
  <div class="section-body">

    <div class="card">
      <span class="card-label label-red">🔴 URGENT</span>
      <h4>Chase Slate Visa Payment Due</h4>
      <div class="card-meta">From: Chase &lt;no.reply.alerts@chase.com&gt; · Received: Today 8:49 AM</div>
      <div class="card-row">
        <div class="card-field"><strong>Why it matters:</strong> Credit card payment due July 15 — only 5 days away. Missing payment impacts credit and incurs fees.</div>
      </div>
      <div class="card-field" style="margin-top:6px"><strong>Recommended Action:</strong> Log into Chase and schedule or confirm payment today.</div>
      <div class="card-field"><strong>Due:</strong> <span class="highlight">July 15, 2026</span></div>
    </div>

    <div class="card">
      <span class="card-label label-red">🔴 URGENT</span>
      <h4>Daily Briefing Workflow FAILED — Manual Re-Run Needed</h4>
      <div class="card-meta">From: no-reply-claude@mail.anthropic.com · Received: Today 11:10 AM</div>
      <div class="card-row">
        <div class="card-field"><strong>Why it matters:</strong> The automated daily-briefing-dispatch failed at 7:08 AM ET. Your briefing automation is broken and will not run again unless manually triggered.</div>
      </div>
      <div class="card-field" style="margin-top:6px"><strong>Recommended Action:</strong> Go to github.com/missophs/daily-briefing → Actions → Daily Briefing → Run workflow → branch: webhooks</div>
      <div class="card-field"><strong>Due:</strong> <span class="highlight">Today</span></div>
    </div>

    <div class="card">
      <span class="card-label label-green">🟢 INTERVIEW</span>
      <h4>Oscar Health Phone Screen — TODAY 2:00 PM</h4>
      <div class="card-meta">Calendar: Melissa A Weiss and Joelle Molina (Berbano) · joelle@hioscar.com</div>
      <div class="card-row">
        <div class="card-field"><strong>Why it matters:</strong> Phone screen for "People Strategy Lead" at Oscar Health. They will call you at 516-313-8888. You accepted this invite.</div>
      </div>
      <div class="card-field" style="margin-top:6px"><strong>Recommended Action:</strong> Prepare talking points for People Strategy Lead role. Ensure your phone is charged and available at 2:00 PM. Note: Dr. appointment follows at 3:30 PM — no conflict, but tight.</div>
      <div class="card-field"><strong>Due:</strong> <span class="highlight">Today 2:00–2:25 PM</span></div>
    </div>

    <div class="card">
      <span class="card-label label-yellow">🟡 RSVP NEEDED</span>
      <h4>RSVP Pending: HR Networking & Job Search Group Zoom (Wed Jul 15)</h4>
      <div class="card-meta">Calendar Event · Status: needsAction</div>
      <div class="card-field"><strong>Why it matters:</strong> Large HR networking Zoom on July 15, 12:00–1:30 PM. You have NOT responded. This is a core job-search networking event.</div>
      <div class="card-field" style="margin-top:6px"><strong>Recommended Action:</strong> Accept or decline the calendar invite today.</div>
      <div class="card-field"><strong>Due:</strong> <span class="highlight">Before July 15</span></div>
    </div>

    <div class="card">
      <span class="card-label label-yellow">🟡 RSVP NEEDED</span>
      <h4>RSVP Pending: HR Networking Open Office Hours (Thu Jul 16)</h4>
      <div class="card-meta">Calendar Event · Status: needsAction</div>
      <div class="card-field"><strong>Why it matters:</strong> Open Office Hours Zoom on July 16, 12:00–1:00 PM. You have NOT responded. Note conflict with Tea with LeiLani at 1:00 PM same day.</div>
      <div class="card-field" style="margin-top:6px"><strong>Recommended Action:</strong> Accept (these end at 1:00 PM, just as Tea with LeiLani begins — back-to-back but manageable). Confirm logistics.</div>
      <div class="card-field"><strong>Due:</strong> <span class="highlight">Before July 16</span></div>
    </div>

    <div class="card">
      <span class="card-label label-yellow">🟡 OPPORTUNITY</span>
      <h4>LinkedIn Job Alert: Senior Director HRBP — Beacon Hill (Up to $250K)</h4>
      <div class="card-meta">From: LinkedIn Job Alerts · Received: Today 7:05 AM</div>
      <div class="card-field"><strong>Why it matters:</strong> High-paying HRBP leadership role — aligns closely with your HR background. Role was posted 7/8/2026.</div>
      <div class="card-field" style="margin-top:6px"><strong>Recommended Action:</strong> Review posting on LinkedIn and apply before it closes. Strong fit based on your profile.</div>
      <div class="card-field"><strong>Due:</strong> <span class="highlight">Apply ASAP — posted 7/8</span></div>
    </div>

    <div class="card">
      <span class="card-label label-yellow">🟡 HEALTH</span>
      <h4>Northwell Video Visit Reminder — Dr. Stephanie Yuen (Jul 17)</h4>
      <div class="card-meta">From: MyNorthwell · Received: Today 11:21 AM · UNREAD</div>
      <div class="card-field"><strong>Why it matters:</strong> Upcoming video visit with Dr. Stephanie Yuen on July 17 at 3:00 PM EDT. Email asks you to "get ready" — may require pre-visit steps.</div>
      <div class="card-field" style="margin-top:6px"><strong>Recommended Action:</strong> Open the email, complete any pre-visit requirements, confirm telehealth link.</div>
      <div class="card-field"><strong>Due:</strong> <span class="highlight">July 17 at 3:00 PM EDT</span></div>
    </div>

    <div class="card">
      <span class="card-label label-yellow">🟡 FOLLOW-UP</span>
      <h4>USPS Service Request Follow-Up</h4>
      <div class="card-meta">From: USPS Customer Support &lt;uspscustomersupport@usps.gov&gt; · Received: Today 12:21 PM · UNREAD</div>
      <div class="card-field"><strong>Why it matters:</strong> Official USPS response to a service request you filed. Reference #89637899. Melissa Weiss named directly — appears legitimate (.gov domain).</div>
      <div class="card-field" style="margin-top:6px"><strong>Recommended Action:</strong> Read the full email to confirm resolution or next steps for your USPS issue.</div>
      <div class="card-field"><strong>Due:</strong> <span class="highlight">Today</span></div>
    </div>

    <div class="card">
      <span class="card-label label-blue">🔵 TECH</span>
      <h4>LinkedIn Connection Requests — Todd Kosik (VP) &amp; Adam Davison (COO)</h4>
      <div class="card-meta">From: LinkedIn · Received: Today</div>
      <div class="card-field"><strong>Why it matters:</strong> Two pending LinkedIn connections — Todd Kosik (Vice President) has been waiting; Adam Davison (COO/Director, The Rewards Factory) also reached out. May be networking or business development value.</div>
      <div class="card-field" style="margin-top:6px"><strong>Recommended Action:</strong> Review both profiles and respond on LinkedIn today.</div>
      <div class="card-field"><strong>Due:</strong> <span class="highlight">Today / This Week</span></div>
    </div>

    <div class="card">
      <span class="card-label label-gray">⚙️ TECH NOTE</span>
      <h4>Evicore Phone Number Noted (Self-Sent)</h4>
      <div class="card-meta">From: Melissa W &lt;melissaw212@gmail.com&gt; · Received: Today 8:19 AM</div>
      <div class="card-field"><strong>Why it matters:</strong> You emailed yourself the Evicore phone number: <strong>1-800-918-8924</strong>. This likely relates to a prior authorization or healthcare task.</div>
      <div class="card-field" style="margin-top:6px"><strong>Recommended Action:</strong> Call Evicore if you haven't yet. May relate to the upcoming infusion or Dr. Yuen appointment.</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 4 · FULL 7-DAY CALENDAR
════════════════════════════════════════════════════════════════ -->
<div class="section blue">
  <div class="section-title">📅 Full 7-Day Calendar (July 10–16, 2026)</div>
  <div class="section-body">

    <!-- FRIDAY JULY 10 -->
    <div class="cal-day">
      <div class="cal-day-header"><span>📅 Friday, July 10, 2026</span><span style="font-size:11px; opacity:0.85">TODAY · 2 Events</span></div>
      <div class="cal-event">
        <div><span class="evt-time">2:00 PM – 2:25 PM</span> <span class="evt-title">Oscar Health Phone Screen — People Strategy Lead</span></div>
        <div class="evt-detail">With Joelle Molina (Berbano) · joelle@hioscar.com · They will call 516-313-8888</div>
        <div class="evt-badges">
          <span class="rsvp-yes">✅ ACCEPTED</span>
          <span class="badge badge-green">INTERVIEW</span>
          <span class="badge badge-blue">Phone / Google Meet</span>
        </div>
        <div class="evt-detail" style="margin-top:5px">⚡ <strong>Prep needed:</strong> Review Oscar Health's People Strategy priorities. Have resume and notes ready. Ensure phone charged. 25-minute screen — be concise and strategic.</div>
      </div>
      <div class="cal-event">
        <div><span class="evt-time">3:30 PM – 4:30 PM</span> <span class="evt-title">Dr. (Doctor's Appointment)</span></div>
        <div class="evt-detail">No additional details provided · Location not specified</div>
        <div class="evt-badges">
          <span class="rsvp-yes">✅ CONFIRMED</span>
        </div>
        <div class="evt-detail" style="margin-top:5px">⚡ <strong>Prep needed:</strong> Oscar screen ends at 2:25 PM — you have ~65 min buffer before this appointment. Confirm location/address. Note Evicore number you saved (may be relevant).</div>
      </div>
    </div>

    <!-- SATURDAY / SUNDAY — NO EVENTS -->
    <div class="cal-day">
      <div class="cal-day-header" style="background:#7f8c8d;"><span>📅 Saturday, July 11 &amp; Sunday, July 12, 2026</span><span style="font-size:11px; opacity:0.85">No Events Scheduled</span></div>
      <div class="cal-event"><div class="evt-detail" style="color:#888;">No calendar events. Good opportunity to prep for next week's appointments and networking sessions.</div></div>
    </div>

    <!-- MONDAY JULY 13 -->
    <div class="cal-day">
      <div class="cal-day-header" style="background:#8e44ad;"><span>📅 Monday, July 13, 2026</span><span style="font-size:11px; opacity:0.85">1 Event</span></div>
      <div class="cal-event">
        <div><span class="evt-time">All Day</span> <span class="evt-title">Stephanie — Infusion</span></div>
        <div class="evt-detail">All-day event · No location specified</div>
        <div class="evt-badges">
          <span class="rsvp-yes">✅ CONFIRMED</span>
          <span class="rsvp-allday">ALL DAY</span>
        </div>
        <div class="evt-detail" style="margin-top:5px">⚡ <strong>Prep needed:</strong> Confirm logistics and location for Stephanie's infusion. Plan for extended time commitment — may impact availability for the day.</div>
      </div>
    </div>

    <!-- TUESDAY JULY 14 -->
    <div class="cal-day">
      <div class="cal-day-header" style="background:#16a085;"><span>📅 Tuesday, July 14, 2026</span><span style="font-size:11px; opacity:0.85">1 Event</span></div>
      <div class="cal-event">
        <div><span class="evt-time">10:00 AM – 11:00 AM</span> <span class="evt-title">Stella</span></div>
        <div class="evt-detail">No location specified · No additional details</div>
        <div class="evt-badges">
          <span class="rsvp-yes">✅ CONFIRMED</span>
        </div>
        <div class="evt-detail" style="margin-top:5px">⚡ <strong>Prep needed:</strong> Confirm purpose and location of Stella meeting.</div>
      </div>
    </div>

    <!-- WEDNESDAY JULY 15 -->
    <div class="cal-day">
      <div class="cal-day-header" style="background:#e67e22;"><span>📅 Wednesday, July 15, 2026</span><span style="font-size:11px; opacity:0.85">3 Events · Chase payment DUE</span></div>
      <div class="cal-event">
        <div><span class="evt-time">8:30 AM – 9:30 AM</span> <span class="evt-title">Bone Density Scan</span></div>
        <div class="evt-detail">Medical appointment · No location specified</div>
        <div class="evt-badges">
          <span class="rsvp-yes">✅ CONFIRMED</span>
          <span class="badge badge-red">MEDICAL</span>
        </div>
        <div class="evt-detail" style="margin-top:5px">⚡ <strong>Prep needed:</strong> Confirm facility address and any prep instructions (fasting, clothing restrictions, etc.).</div>
      </div>
      <div class="cal-event">
        <div><span class="evt-time">12:00 PM – 1:30 PM</span> <span class="evt-title">HR Networking &amp; Job Search Group — Zoom 2</span></div>
        <div class="evt-detail">Zoom: us06web.zoom.us/j/81954171722 · Large group networking session · 190+ attendees</div>
        <div class="evt-badges">
          <span class="rsvp-pending">⚠️ NO RSVP YET</span>
          <span class="badge badge-green">NETWORKING</span>
        </div>
        <div class="evt-detail" style="margin-top:5px">⚡ <strong>Action required:</strong> RSVP to this event. Prepare your elevator pitch and any questions. Excellent opportunity for HR peer networking during job search.</div>
      </div>
      <div class="cal-event">
        <div><span class="evt-time">12:00 PM – 1:30 PM</span> <span class="evt-title">Network (duplicate/personal reminder block)</span></div>
        <div class="evt-detail">Appears to be a personal reminder concurrent with the HR Networking Zoom above</div>
        <div class="evt-badges">
          <span class="rsvp-yes">✅ CONFIRMED</span>
          <span class="badge badge-gray">PERSONAL BLOCK</span>
        </div>
        <div class="evt-detail" style="margin-top:5px">ℹ️ This event overlaps with the HR Networking Zoom — likely the same block. No conflict.</div>
      </div>
    </div>

    <!-- THURSDAY JULY 16 -->
    <div class="cal-day">
      <div class="cal-day-header" style="background:#c0392b;"><span>📅 Thursday, July 16, 2026</span><span style="font-size:11px; opacity:0.85">3 Events · Back-to-back afternoon ⚠️</span></div>
      <div class="cal-event">
        <div><span class="evt-time">9:00 AM – 10:30 AM</span> <span class="evt-title">Executive Roundtable (John Madigan)</span></div>
        <div class="evt-detail">Zoom: us02web.zoom.us/j/207786667 · Meeting ID: 207 786 667 · Password: 205454</div>
        <div class="evt-badges">
          <span class="rsvp-no">❌ DECLINED</span>
          <span class="badge badge-gray">DECLINED</span>
        </div>
        <div class="evt-detail" style="margin-top:5px">ℹ️ You have already declined this event. No action needed unless you wish to reconsider.</div>
      </div>
      <div class="cal-event">
        <div><span class="evt-time">12:00 PM – 1:00 PM</span> <span class="evt-title">HR Networking Open Office Hours — Zoom 2</span></div>
        <div class="evt-detail">Zoom: us06web.zoom.us/j/85945371140 · Open discussion format · No recording per instructions</div>
        <div class="evt-badges">
          <span class="rsvp-pending">⚠️ NO RSVP YET</span>
          <span class="badge badge-green">NETWORKING</span>
          <span class="conflict-warn">⚠️ BACK-TO-BACK</span>
        </div>
        <div class="evt-detail" style="margin-top:5px">⚡ <strong>Action required:</strong> RSVP. Ends at 1:00 PM — immediately before Tea with LeiLani begins. Plan to leave Zoom promptly and transit to T Shop (NYC).</div>
      </div>
      <div class="cal-event">
        <div><span class="evt-time">1:00 PM – 2:00 PM</span> <span class="evt-title">Tea with LeiLani | Brew At the Table</span></div>
        <div class="evt-detail">📍 T Shop · 247 Elizabeth St, New York, NY 10012 · With: leilani@bethechangehr.com, tlow@teresalowconsulting.com, leylasnovini@gmail.com, jessi@alvisolutions.com</div>
        <div class="evt-badges">
          <span class="rsvp-yes">✅ ACCEPTED</span>
          <span class="badge badge-green">NETWORKING · IN PERSON · NYC</span>
          <span class="conflict-warn">⚠️ BACK-TO-BACK W/ ZOOM</span>
        </div>
        <div class="evt-detail" style="margin-top:5px">⚡ <strong>Prep needed:</strong> Research LeiLani and other attendees. Plan transit to 247 Elizabeth St, NYC — account for travel time from wherever Zoom takes place. This is an in-person HR networking opportunity; come prepared with your current job search status and goals.</div>
      </div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 5 · JOB SEARCH & INTERVIEW PIPELINE
════════════════════════════════════════════════════════════════ -->
<div class="section green">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">

    <div class="info-box">🎯 Active pipeline: 1 interview today, 1 high-value job lead, 2 networking events next week, 2 LinkedIn connection requests pending.</div>

    <table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Role / Event</th>
          <th>Organization</th>
          <th>Status / Date</th>
          <th>Fit</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="badge badge-red">INTERVIEW</span></td>
          <td>People Strategy Lead</td>
          <td>Oscar Health</td>
          <td>Phone Screen TODAY<br>2:00–2:25 PM<br>Call 516-313-8888</td>
          <td><span class="badge badge-red">HIGH</span></td>
          <td>Prepare now. Be ready at 2:00 PM.</td>
        </tr>
        <tr>
          <td><span class="badge badge-yellow">JOB LEAD</span></td>
          <td>Senior Director, HRBP</td>
          <td>Beacon Hill</td>
          <td>Posted 7/8/2026<br>Up to $250K/year</td>
          <td><span class="badge badge-red">HIGH</span></td>
          <td>Apply on LinkedIn ASAP — recent posting.</td>
        </tr>
        <tr>
          <td><span class="badge badge-green">NETWORKING</span></td>
          <td>HR Networking &amp; Job Search Group — Zoom 2</td>
          <td>Peer HR Group</td>
          <td>Wed Jul 15<br>12:00–1:30 PM</td>
          <td><span class="badge badge-red">HIGH</span></td>
          <td>RSVP and prepare elevator pitch.</td>
        </tr>
        <tr>
          <td><span class="badge badge-green">NETWORKING</span></td>
          <td>HR Networking Open Office Hours</td>
          <td>Peer HR Group</td>
          <td>Thu Jul 16<br>12:00–1:00 PM</td>
          <td><span class="badge badge-yellow">MEDIUM</span></td>
          <td>RSVP. Ends just before Tea with LeiLani.</td>
        </tr>
        <tr>
          <td><span class="badge badge-green">NETWORKING</span></td>
          <td>Tea with LeiLani — Brew At the Table</td>
          <td>BeTheChangeHR + consultants</td>
          <td>Thu Jul 16<br>1:00–2:00 PM · NYC</td>
          <td><span class="badge badge-red">HIGH</span></td>
          <td>Accepted. Plan NYC transit. Research attendees.</td>
        </tr>
        <tr>
          <td><span class="badge badge-blue">LINKEDIN</span></td>
          <td>Connection Request</td>
          <td>Todd Kosik, Vice President</td>
          <td>Pending response</td>
          <td><span class="badge badge-yellow">MEDIUM</span></td>
          <td>Review profile, respond on LinkedIn.</td>
        </tr>
        <tr>
          <td><span class="badge badge-blue">LINKEDIN</span></td>
          <td>Connection Request</td>
          <td>Adam Davison, COO — The Rewards Factory</td>
          <td>Pending response</td>
          <td><span class="badge badge-yellow">MEDIUM</span></td>
          <td>Review profile, respond on LinkedIn.</td>
        </tr>
        <tr>
          <td><span class="badge badge-gray">DECLINED</span></td>
          <td>Executive Roundtable</td>
          <td>John Madigan (Zoom)</td>
          <td>Thu Jul 16 9:00 AM<br>Already declined</td>
          <td><span class="badge badge-gray">N/A</span></td>
          <td>No action needed unless reconsidering.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 6 · FULL EMAIL REVIEW BY CATEGORY
════════════════════════════════════════════════════════════════ -->
<div class="section dark">
  <div class="section-title">📧 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="card">
      <span class="card-label label-red">🔴 Security / Risk</span>
      <h4>Count: 3 emails</h4>
      <div class="card-meta">Phishing, spam, and suspicious senders</div>
      <ul class="brief-list">
        <li><strong>"Payment_Processing" &lt;yjriasw4b7@1isgh07mx2.us&gt;</strong> — "Action Required: Your payment was declined" — PHISHING. Suspicious domain, fake antivirus billing. Not in inbox. <span class="badge badge-red">DELETE</span></li>
        <li><strong>"After?40 Change" &lt;4ajf4ap5t4@jbcricn78a.je4tgi4nz7.us&gt;</strong> — Men's health spam. Suspicious domain. Not in inbox. <span class="badge badge-red">DELETE</span></li>
        <li><strong>"Rock-Hard" &lt;qcnbbexby@ampgsfqsssfeootfzmtreoedae.net&gt;</strong> — Male performance spam (in Trash). Random domain. <span class="badge badge-red">ALREADY TRASHED</span></li>
      </ul>
      <div class="card-field" style="margin-top:8px"><strong>Recommended Action:</strong> Do not click any links. Mark as spam and delete. These are phishing/spam campaigns.</div>
    </div>

    <!-- JOB SEARCH -->
    <div class="card">
      <span class="card-label label-green">🟢 Job Search</span>
      <h4>Count: 1 email</h4>
      <ul class="brief-list">
        <li><strong>LinkedIn Job Alerts</strong> — "Senior Director - HRBP at Beacon Hill: up to $250K/year" — Posted 7/8/2026. <span class="badge badge-red">HIGH PRIORITY — Apply ASAP</span></li>
      </ul>
      <div class="card-field" style="margin-top:8px"><strong>Recommended Action:</strong> Review and apply on LinkedIn today.</div>
    </div>

    <!-- RECRUITERS / NETWORKING -->
    <div class="card">
      <span class="card-label label-green">🟢 Recruiters / Networking</span>
      <h4>Count: 2 emails</h4>
      <ul class="brief-list">
        <li><strong>LinkedIn (Todd Kosik, VP)</strong> — "I still want to connect" — Pending connection request. <span class="badge badge-yellow">RESPOND</span></li>
        <li><strong>LinkedIn (Adam Davison, COO — The Rewards Factory)</strong> — "I'd like to connect" — Pending connection request. <span class="badge badge-yellow">RESPOND</span></li>
      </ul>
      <div class="card-field" style="margin-top:8px"><strong>Recommended Action:</strong> Review both profiles and respond on LinkedIn.</div>
    </div>

    <!-- CALENDAR / EVENTS -->
    <div class="card">
      <span class="card-label label-blue">🔵 Calendar / Events</span>
      <h4>Count: 1 email</h4>
      <ul class="brief-list">
        <li><strong>AllEvents</strong> — "Melissa, popular events this weekend in York" — Weekend event recommendations in York area. Low priority. <span class="badge badge-gray">REVIEW IF INTERESTED</span></li>
      </ul>
    </div>

    <!-- MEDICAL / HEALTH -->
    <div class="card">
      <span class="card-label label-red">🔴 Medical / Health</span>
      <h4>Count: 3 emails</h4>
      <ul class="brief-list">
        <li><strong>MyNorthwell</strong> — "Get ready for your visit on 7/17" — Video visit with Dr. Stephanie Yuen, July 17 at 3:00 PM EDT. UNREAD. <span class="badge badge-red">READ &amp; PREP</span></li>
        <li><strong>USPS Informed Delivery</strong> — "Your Daily Digest for Fri, 7/10" — 1 mailpiece, 1 inbound package arriving. Could include medical mail. <span class="badge badge-blue">REVIEW</span></li>
        <li><strong>Melissa W (self-sent)</strong> — Evicore phone number 18009188924. Health-related self-note. <span class="badge badge-yellow">CALL IF NEEDED</span></li>
      </ul>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="card">
      <span class="card-label label-yellow">🟡 Financial / Billing</span>
      <h4>Count: 2 emails</h4>
      <ul class="brief-list">
        <li><strong>Chase</strong> — "Your Chase Slate Visa payment is due on Jul 15, 2026" — URGENT. Payment due in 5 days. <span class="badge badge-red">PAY NOW</span></li>
        <li><strong>Marcus by Goldman Sachs Savings</strong> — "We raised our 14-month CD rate — currently 4.10% APY!" (in Trash) — CD rate announcement. <span class="badge badge-gray">REVIEW IF INTERESTED / TRASHED</span></li>
      </ul>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="card">
      <span class="card-label label-purple">🟣 Professional Development</span>
      <h4>Count: 5 emails</h4>
      <ul class="brief-list">
        <li><strong>TLDR InfoSec</strong> — "npm 12 Reduces Supply Chain Risk, 130 Exploits Published, Linux Distro Sabotage" — InfoSec news. Relevant if tech-adjacent role. <span class="badge badge-purple">REVIEW</span></li>
        <li><strong>AI For Leaders</strong> — "ChatGPT Dreams to Remember You" — AI leadership content. <span class="badge badge-purple">REVIEW</span></li>
        <li><strong>TLDR (main)</strong> — "ChatGPT Work, Meta AI API, code review bottlenecks" — AI/tech news. <span class="badge badge-purple">REVIEW</span></li>
        <li><strong>The AI Report</strong> — "ChatGPT Work goes live" — AI news, Google AI ad disclosures. UNREAD. <span class="badge badge-purple">REVIEW</span></li>
        <li><strong>CoolDeep AI</strong> — "An easy AI roadmap nobody gave me" — (in Trash) AI learning content. <span class="badge badge-gray">TRASHED — REVIEW OR DELETE</span></li>
      </ul>
    </div>

    <!-- PERSONAL -->
    <div class="card">
      <span class="card-label label-gray">Personal</span>
      <h4>Count: 1 email</h4>
      <ul class="brief-list">
        <li><strong>Waze</strong> — "Updates to our Terms and Privacy Policy" — Effective August 1, 2026. Terms update. <span class="badge badge-gray">LOW PRIORITY / NOTE</span></li>
      </ul>
    </div>

    <!-- NEWSLETTERS / SUBSCRIPTIONS -->
    <div class="card">
      <span class="card-label label-purple">🟣 Newsletters / Subscriptions</span>
      <h4>Count: 11 emails</h4>
      <ul class="brief-list">
        <li><strong>The HR Takeaways (×3)</strong> — "AI Jobs Barometer, Rethinking Interviews, Compliance Check" — Triplicate delivery. Read one, delete two duplicates.</li>
        <li><strong>Success In HR</strong> — Issue #65, "Take Off Your Mask!" (in Trash) — Leadership tips for HR leaders.</li>
        <li><strong>Stephanie Wigner</strong> — "Judgment and curiosity cannot coexist" (in Trash) — Mindset/coaching content.</li>
        <li><strong>1% Better</strong> — "Rare Book Heist, Erling Haaland Fandom, 100 Tiny Marriage Upgrades" (in Trash) — Self-improvement newsletter.</li>
        <li><strong>The Daily Skimm</strong> — "Don't worry, your finsta is safe" — Daily news digest. UNREAD.</li>
        <li><strong>The Hustle</strong> — "Rich kid bootcamp" (in Trash) — Business/culture newsletter.</li>
        <li><strong>The Average Joe</strong> — "Halo effect — Should Hershey be more valuable than Nvidia?" — Finance/investing newsletter. UNREAD.</li>
        <li><strong>Medium Daily Digest (×2)</strong> — AI Operating System guide; UX Collective "Wait, who made this?" — Tech/design content.</li>
        <li><strong>Claude's Notebook (Substack)</strong> — "The Installed Self" — AI/philosophy content. UNREAD.</li>
        <li><strong>Meidas+</strong> — "MeidasTouch Full Podcast — 7/9/26 [AD-FREE]" — Politics podcast. UNREAD.</li>
      </ul>
      <div class="card-field" style="margin-top:8px"><strong>Recommended Action:</strong> Consolidate HR Takeaways (delete 2 duplicates). Review trashed newsletters before permanently deleting. Assess subscription value weekly.</div>
    </div>

    <!-- PROMOTIONAL / RETAIL -->
    <div class="card">
      <span class="card-label label-gray">🛍️ Promotional / Retail</span>
      <h4>Count: 13 emails</h4>
      <ul class="brief-list">
        <li><strong>ONE/SIZE Beauty</strong> — "Touch-ups are OOO" (in Trash) — Beauty promo</li>
        <li><strong>Laura Geller (×2)</strong> — "$30 Store Credit Today Only" &amp; "$20 Store Credit Today Only" — Beauty deals, expired today</li>
        <li><strong>Halara</strong> — "All Under $19.95 Is Waiting" — Clothing promo. UNREAD.</li>
        <li><strong>Lands' End</strong> — "55% off swim!" — Swimwear sale. UNREAD, in inbox.</li>
        <li><strong>SHEIN</strong> — "12% OFF: Your Cart Awaits" — Fast fashion promo.</li>
        <li><strong>Target Optical</strong> — "Something Big is Coming..." — Contacts offer teaser.</li>
        <li><strong>Zappos</strong> — "Temps: sweltering, your shoe game: sizzling" — Shoe promo.</li>
        <li><strong>Kohl's</strong> — "Save an extra 30%" — Dept store promo. UNREAD, in inbox.</li>
        <li><strong>Temu</strong> — "Your order out-for-delivery" (#PO-211-13384044800631025) — REAL order notification. UNREAD, in inbox. <span class="badge badge-yellow">TRACK DELIVERY</span></li>
        <li><strong>Venmo</strong> — "$100 bonus offer" — Credit card offer (not spam, but promotional)</li>
        <li><strong>Robinhood Credit Card</strong> — "Your invite expires in 5 days" — Gold Card 3% cash back offer. UNREAD.</li>
        <li><strong>Match.com</strong> — "You've had a profile view from Surprising, 68" — Dating app notification. UNREAD.</li>
        <li><strong>Stocktwits</strong> — "Updated Privacy Policy and Terms of Use" (in Trash) — Terms update, effective today.</li>
      </ul>
      <div class="card-field" style="margin-top:8px"><strong>Action:</strong> Track Temu delivery. Review Robinhood card before invite expires (5 days). Laura Geller store credits expired today. Delete rest.</div>
    </div>

    <!-- TRASH REVIEW (in category table) -->
    <div class="card">
      <span class="card-label label-red">🗑️ Trash Review (from Gmail Trash)</span>
      <h4>Count: 9 emails in Trash</h4>
      <ul class="brief-list">
        <li><strong>ONE/SIZE Beauty</strong> — "Touch-ups are OOO" — Promotional. Safe to delete.</li>
        <li><strong>Success In HR</strong> — Issue #65, "Take Off Your Mask!" — HR newsletter in trash.</li>
        <li><strong>Stephanie Wigner</strong> — "Judgment and curiosity cannot coexist" — Coaching email in trash.</li>
        <li><strong>1% Better</strong> — "Rare Book Heist, Erling Haaland Fandom, 100 Tiny Marriage Upgrades" — Newsletter in trash.</li>
        <li><strong>The Hustle</strong> — "Rich kid bootcamp" — Newsletter in trash.</li>
        <li><strong>Rock-Hard (spam)</strong> — Male performance spam — Safe to permanently delete.</li>
        <li><strong>Marcus by Goldman Sachs</strong> — "14-month CD rate 4.10% APY" — Financial info, trashed.</li>
        <li><strong>Stocktwits</strong> — "Updated Privacy Policy" — Terms update, trashed.</li>
        <li><strong>CoolDeep AI</strong> — "An easy AI roadmap" — AI newsletter in trash.</li>
      </ul>
    </div>

    <!-- SAFE TO DELETE / IGNORE -->
    <div class="card">
      <span class="card-label label-gray">🗑️ Safe to Delete / Ignore</span>
      <h4>Count: 2 emails (spam/gambling)</h4>
      <ul class="brief-list">
        <li><strong>"FreeSpins" &lt;rfjtm@xzwdzxosnuwcqmmbvkomtcoomm.net&gt;</strong> — "Claim your 250 Welcome Free Spins" — Gambling spam. UNREAD. <span class="badge badge-red">DELETE / MARK SPAM</span></li>
        <li><strong>"Congratulations" &lt;tocwqreupix@nazs.heegjckdqrmwr.us&gt;</strong> — "130 Free Spins Pending" — Casino spam. UNREAD. <span class="badge badge-red">DELETE / MARK SPAM</span></li>
      </ul>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 7 · TRASH REVIEW
════════════════════════════════════════════════════════════════ -->
<div class="section red">
  <div class="section-title">🗑️ Trash Review</div>
  <div class="section-body">

    <div class="warning-box">⚠️ 9 emails were found in Gmail Trash. Review before permanently deleting.</div>

    <div class="card">
      <span class="card-label label-yellow">🟡 Restore Immediately</span>
      <h4>Items worth restoring from Trash</h4>
      <table>
        <thead><tr><th>Sender</th><th>Subject</th><th>Reason</th></tr></thead>
        <tbody>
          <tr>
            <td>Marcus by Goldman Sachs Savings</td>
            <td>We raised our 14-month CD rate — 4.10% APY!</td>
            <td>Financial institution update — may be relevant to savings decisions. Restore and review if interested in rate offers.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="card">
      <span class="card-label label-blue">🔵 Review Before Deleting</span>
      <h4>Items with some potential value — review before permanent deletion</h4>
      <table>
        <thead><tr><th>Sender</th><th>Subject</th><th>Reason</th></tr></thead>
        <tbody>
          <tr>
            <td>Success In HR (Substack)</td>
            <td>Issue #65 — Take Off Your Mask! How To Really Impress Others As An HR Leader</td>
            <td>HR leadership content — relevant to your field. Trashed, but may be worth a quick read given job search.</td>
          </tr>
          <tr>
            <td>Stephanie Wigner</td>
            <td>Judgment and curiosity cannot coexist</td>
            <td>Coaching/mindset content. If you subscribed intentionally, review before deleting permanently.</td>
          </tr>
          <tr>
            <td>1% Better Newsletter</td>
            <td>Rare Book Heist, Erling Haaland Fandom, and 100 Tiny Marriage Upgrades</td>
            <td>Self-improvement newsletter. Quick scan if time permits, otherwise delete.</td>
          </tr>
          <tr>
            <td>The Hustle</td>
            <td>Rich kid bootcamp</td>
            <td>Business culture newsletter. May have useful content. Low priority.</td>
          </tr>
          <tr>
            <td>CoolDeep AI</td>
            <td>An easy AI roadmap nobody gave me</td>
            <td>AI learning content — potentially useful for HR-tech awareness. Quick scan recommended.</td>
          </tr>
          <tr>
            <td>Stocktwits</td>
            <td>We've updated our Privacy Policy and Terms of Use</td>
            <td>Terms update effective July 10, 2026. Minimal action needed but note the change if you use Stocktwits.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="card">
      <span class="card-label label-gray">✅ Safe to Delete Permanently</span>
      <h4>Items confirmed safe to permanently delete from Trash</h4>
      <table>
        <thead><tr><th>Sender</th><th>Subject</th><th>Reason</th></tr></thead>
        <tbody>
          <tr>
            <td>ONE/SIZE Beauty</td>
            <td>Touch-ups are OOO 🌴</td>
            <td>Beauty brand promotional email. No value. Safe to delete.</td>
          </tr>
          <tr>
            <td>Rock-Hard &lt;qcnbbexby@ampgsfqsssfeootfzmtreoedae.net&gt;</td>
            <td>A Simple Habit That Many Guys Say Improves Their Performance</td>
            <td>Spam / adult product marketing from
