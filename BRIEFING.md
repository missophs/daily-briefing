<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Melissa's Executive Briefing — Monday, July 13, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px 28px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 15px; color: #a8c0e0; margin-top: 4px; }
  .header .meta { display: flex; gap: 28px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.1); border-radius: 8px; padding: 10px 18px; }
  .header .meta-item .label { font-size: 11px; color: #8ab4d8; text-transform: uppercase; letter-spacing: 1px; }
  .header .meta-item .value { font-size: 20px; font-weight: 700; color: #fff; margin-top: 2px; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; padding: 10px 16px; border-radius: 8px 8px 0 0; margin-bottom: 0; }
  .section-body { background: #fff; border-radius: 0 0 10px 10px; padding: 18px 20px; border: 1px solid #e2e6ea; border-top: none; }

  /* COLOR THEMES */
  .red .section-title    { background: #c0392b; color: #fff; }
  .red .section-body     { border-color: #e57373; }
  .yellow .section-title { background: #f39c12; color: #fff; }
  .yellow .section-body  { border-color: #f9ca74; }
  .blue .section-title   { background: #2563eb; color: #fff; }
  .blue .section-body    { border-color: #90b8f8; }
  .green .section-title  { background: #1a7a4a; color: #fff; }
  .green .section-body   { border-color: #6fcf97; }
  .purple .section-title { background: #6d28d9; color: #fff; }
  .purple .section-body  { border-color: #c4b5fd; }
  .gray .section-title   { background: #6b7280; color: #fff; }
  .gray .section-body    { border-color: #d1d5db; }
  .navy .section-title   { background: #1e3a5f; color: #fff; }
  .navy .section-body    { border-color: #90aac8; }
  .teal .section-title   { background: #0e7490; color: #fff; }
  .teal .section-body    { border-color: #67e8f9; }

  /* CARDS */
  .card { border-radius: 8px; padding: 14px 16px; margin-bottom: 12px; }
  .card-red    { background: #fff5f5; border-left: 4px solid #e53e3e; }
  .card-yellow { background: #fffbeb; border-left: 4px solid #f59e0b; }
  .card-blue   { background: #eff6ff; border-left: 4px solid #3b82f6; }
  .card-green  { background: #f0fdf4; border-left: 4px solid #16a34a; }
  .card-purple { background: #faf5ff; border-left: 4px solid #7c3aed; }
  .card-gray   { background: #f9fafb; border-left: 4px solid #9ca3af; }
  .card-teal   { background: #f0fdfa; border-left: 4px solid #0e7490; }

  .card-title { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
  .card-meta  { font-size: 12px; color: #666; margin-bottom: 6px; }
  .card-body  { font-size: 13px; }
  .card-body p { margin-bottom: 4px; }
  .card-body strong { font-weight: 600; }

  /* BADGES */
  .badge { display: inline-block; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 20px; margin-right: 4px; text-transform: uppercase; letter-spacing: 0.5px; }
  .badge-red    { background: #fee2e2; color: #b91c1c; }
  .badge-yellow { background: #fef3c7; color: #92400e; }
  .badge-green  { background: #dcfce7; color: #166534; }
  .badge-blue   { background: #dbeafe; color: #1e40af; }
  .badge-purple { background: #ede9fe; color: #5b21b6; }
  .badge-gray   { background: #f3f4f6; color: #374151; }
  .badge-orange { background: #ffedd5; color: #9a3412; }
  .badge-teal   { background: #ccfbf1; color: #0f766e; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; margin-top: 8px; font-size: 13px; }
  th { background: #f1f5f9; color: #374151; text-align: left; padding: 9px 12px; font-weight: 700; border-bottom: 2px solid #e2e6ea; }
  td { padding: 8px 12px; border-bottom: 1px solid #f0f0f0; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #fafbfc; }

  /* PRIORITY CHIPS */
  .p-high   { color: #b91c1c; font-weight: 700; }
  .p-medium { color: #92400e; font-weight: 600; }
  .p-low    { color: #166534; font-weight: 500; }

  /* SUMMARY BULLETS */
  .exec-summary { list-style: none; }
  .exec-summary li { padding: 10px 14px; margin-bottom: 8px; border-radius: 8px; font-size: 14px; display: flex; align-items: flex-start; gap: 10px; }
  .exec-summary li .icon { font-size: 20px; flex-shrink: 0; margin-top: 1px; }
  .es-red    { background: #fff5f5; border-left: 4px solid #e53e3e; }
  .es-green  { background: #f0fdf4; border-left: 4px solid #16a34a; }
  .es-blue   { background: #eff6ff; border-left: 4px solid #3b82f6; }

  /* DAY GROUPS */
  .day-header { background: #1e3a5f; color: #fff; padding: 7px 14px; border-radius: 6px; font-weight: 700; font-size: 13px; margin-bottom: 6px; margin-top: 14px; }
  .day-header:first-child { margin-top: 0; }

  /* EVENT ROW */
  .event-row { display: grid; grid-template-columns: 110px 1fr; gap: 10px; padding: 8px 4px; border-bottom: 1px solid #f0f0f0; }
  .event-row:last-child { border-bottom: none; }
  .event-time { font-size: 12px; font-weight: 700; color: #2563eb; padding-top: 2px; }
  .event-detail .etitle { font-size: 13px; font-weight: 700; }
  .event-detail .emeta  { font-size: 12px; color: #666; margin-top: 2px; }

  /* CONFLICT */
  .conflict-warn { background: #fff3cd; border: 1px solid #f59e0b; border-radius: 6px; padding: 6px 12px; font-size: 12px; margin-top: 6px; color: #92400e; }

  /* DIVIDER */
  .divider { height: 1px; background: #e2e6ea; margin: 14px 0; }

  /* DASHBOARD GRID */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 12px; }
  .dash-tile { border-radius: 10px; padding: 16px; text-align: center; }
  .dash-tile .dt-label { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; font-weight: 700; margin-bottom: 6px; }
  .dash-tile .dt-value { font-size: 28px; font-weight: 800; }
  .dash-tile .dt-sub   { font-size: 11px; margin-top: 4px; opacity: 0.75; }
  .dt-red    { background: #fee2e2; color: #b91c1c; }
  .dt-yellow { background: #fef3c7; color: #92400e; }
  .dt-green  { background: #dcfce7; color: #166534; }
  .dt-blue   { background: #dbeafe; color: #1e40af; }
  .dt-purple { background: #ede9fe; color: #5b21b6; }
  .dt-gray   { background: #f3f4f6; color: #374151; }
  .dt-teal   { background: #ccfbf1; color: #0f766e; }

  /* TOP 3 */
  .top3 { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 14px; }
  .top3-card { border-radius: 10px; padding: 18px 20px; }
  .top3-num  { font-size: 36px; font-weight: 900; opacity: 0.2; line-height: 1; }
  .top3-title { font-size: 15px; font-weight: 700; margin-top: -8px; }
  .top3-body  { font-size: 13px; margin-top: 6px; }

  /* SMALL NOTE */
  .note { font-size: 12px; color: #666; font-style: italic; margin-top: 8px; }

  /* ACCOUNTING TABLE */
  .acct th { background: #1e3a5f; color: #fff; }

  /* SPAM TAG */
  .spam-tag { background: #fee2e2; color: #991b1b; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 4px; margin-left: 4px; }
  .auto-tag { background: #fde68a; color: #92400e; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 4px; margin-left: 4px; }
  .phish-tag { background: #fee2e2; color: #7f1d1d; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 4px; margin-left: 4px; }

  ul.checklist { list-style: none; padding-left: 0; }
  ul.checklist li { padding: 4px 0; padding-left: 20px; position: relative; }
  ul.checklist li::before { content: '✓'; position: absolute; left: 0; color: #16a34a; font-weight: 700; }

  @media (max-width: 640px) {
    .header .meta { gap: 10px; }
    .dash-grid { grid-template-columns: repeat(2, 1fr); }
    .top3 { grid-template-columns: 1fr; }
    .event-row { grid-template-columns: 1fr; }
  }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════════════ HEADER -->
<div class="header">
  <h1>Good Morning, Melissa 👋</h1>
  <div class="subtitle">Executive Briefing — Prepared by your Chief of Staff</div>
  <div class="meta">
    <div class="meta-item"><div class="label">Date</div><div class="value">Mon, July 13, 2026</div></div>
    <div class="meta-item"><div class="label">Emails Reviewed</div><div class="value">50</div></div>
    <div class="meta-item"><div class="label">Calendar Events</div><div class="value">11</div></div>
    <div class="meta-item"><div class="label">Action Items</div><div class="value">7</div></div>
    <div class="meta-item"><div class="label">Security Flags</div><div class="value" style="color:#f87171;">8</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════ EXEC SUMMARY -->
<div class="section red">
  <div class="section-title">📋 Executive Summary</div>
  <div class="section-body">
    <ul class="exec-summary">
      <li class="es-red">
        <span class="icon">🔴</span>
        <div><strong>Security Risk:</strong> 8 phishing/scam emails detected today — 6 were auto-trashed before reaching your inbox. Fake casino offers, spoofed Atlassian/Jira deactivation notice, fake prize wins (Tractor Supply, Lowe's), explicit spam, and a Cloud ID payment lock threat were all neutralized. No action needed on auto-trashed items; review manually trashed spam to confirm deletion.</div>
      </li>
      <li class="es-green">
        <span class="icon">🟢</span>
        <div><strong>Job Search Opportunity:</strong> LinkedIn has flagged a CHRO role at the City of New York (posted 7/11) and a VP People &amp; Talent role at Armada — both high-fit. 214 people viewed your LinkedIn profile this week. Ahmad Raheed's LinkedIn message is 3 days old and needs a reply today. Ladders also surfaced roles not on LinkedIn/Indeed.</div>
      </li>
      <li class="es-blue">
        <span class="icon">🔵</span>
        <div><strong>Calendar Priority:</strong> You have a conflict on Wednesday July 15 — Bone Density scan and Imaging Appointment at LH Radiology are both at 8:30 AM at 400 East 66th St (they appear to be the same appointment — confirm). HR Networking Zoom at noon Wed needs your RSVP. Tea with LeiLani on Thursday is accepted. Quest Diagnostics lab on Friday at 10:10 AM — confirmation # FOUGZX.</div>
      </li>
    </ul>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════ ACTION REQUIRED -->
<div class="section yellow">
  <div class="section-title">⚡ Action Required — Items Melissa Must Act On</div>
  <div class="section-body">

    <div class="card card-red">
      <div class="card-title">🔴 Reply to Ahmad Raheed on LinkedIn <span class="badge badge-red">OVERDUE</span></div>
      <div class="card-meta">Source: LinkedIn (messages-noreply@linkedin.com) · Received: Mon Jul 13, 9:05 AM</div>
      <div class="card-body">
        <p><strong>Why it matters:</strong> Ahmad sent you a message 3 days ago — no response risks appearing disengaged during an active job search. Could be a recruiter, peer, or collaborator.</p>
        <p><strong>Next step:</strong> Open LinkedIn inbox now and reply to Ahmad Raheed. Even a brief acknowledgment keeps the door open.</p>
        <p><strong>Due:</strong> Today, Monday July 13</p>
      </div>
    </div>

    <div class="card card-yellow">
      <div class="card-title">🟡 RSVP — HR Networking &amp; Job Search Group Zoom (Wed July 15, 12–1:30 PM) <span class="badge badge-yellow">RSVP NEEDED</span></div>
      <div class="card-meta">Source: Google Calendar · Status: needsAction</div>
      <div class="card-body">
        <p><strong>Why it matters:</strong> Large networking group (180+ attendees). Your status is still "needsAction" — organizer may follow up if not confirmed. Conflicts with "Network" block on same day (same time — likely the same event).</p>
        <p><strong>Next step:</strong> Accept or decline on Google Calendar. Link: https://us06web.zoom.us/j/81954171722</p>
        <p><strong>Due:</strong> Before Wednesday July 15</p>
      </div>
    </div>

    <div class="card card-yellow">
      <div class="card-title">🟡 RSVP — HR Networking Open Office Hours Zoom (Thu July 16, 12–1 PM) <span class="badge badge-yellow">RSVP NEEDED</span></div>
      <div class="card-meta">Source: Google Calendar · Status: needsAction</div>
      <div class="card-body">
        <p><strong>Why it matters:</strong> Separate from the Wed session — this is open office hours, explicitly requesting no automated AI notetaking tools. You are listed as an attendee.</p>
        <p><strong>Next step:</strong> Accept or decline. Link: https://us06web.zoom.us/j/85945371140</p>
        <p><strong>Due:</strong> Before Thursday July 16</p>
      </div>
    </div>

    <div class="card card-blue">
      <div class="card-title">🔵 Confirm Calendar Conflict — Bone Density + Imaging Appointment (Wed July 15, 8:30 AM) <span class="badge badge-blue">VERIFY</span></div>
      <div class="card-meta">Source: Google Calendar — two overlapping entries at same time/location</div>
      <div class="card-body">
        <p><strong>Why it matters:</strong> "Bone Density" (8:30–9:30 AM) and "IMAGING APPOINTMENT: LH Radiology at 400 East 66th St" (8:30–9:05 AM) appear to be the same appointment entered twice. Confirm they are the same so you're not double-booked or confused about check-in time.</p>
        <p><strong>Next step:</strong> Review both calendar entries. Delete the duplicate. Arrive at 400 East 66th St by 8:30 AM with pre-registration forms completed.</p>
        <p><strong>Due:</strong> Before Wednesday July 15</p>
      </div>
    </div>

    <div class="card card-green">
      <div class="card-title">🟢 Review &amp; Apply — CHRO at City of New York (LinkedIn Alert) <span class="badge badge-green">HIGH FIT</span></div>
      <div class="card-meta">Source: LinkedIn Job Alerts (jobalerts-noreply@linkedin.com) · Posted: 7/11/2026</div>
      <div class="card-body">
        <p><strong>Why it matters:</strong> CHRO for NYC is a flagship executive HR role. Posted Friday — act fast before the week fills with applicants. Appeared in two separate LinkedIn alerts.</p>
        <p><strong>Next step:</strong> Review the full job description, tailor your résumé/cover letter, and apply or reach out to a connection at NYC government today.</p>
        <p><strong>Due:</strong> Today or tomorrow, July 13–14</p>
      </div>
    </div>

    <div class="card card-blue">
      <div class="card-title">🔵 Prepare for Quest Diagnostics Lab (Fri July 17, 10:10 AM) <span class="badge badge-blue">UPCOMING</span></div>
      <div class="card-meta">Source: Google Calendar · Confirmation # FOUGZX</div>
      <div class="card-body">
        <p><strong>Why it matters:</strong> Lab appointment at 65 E 76th St — only a 15-minute window. Confirm any fasting requirements in advance.</p>
        <p><strong>Next step:</strong> Check whether Dr. Yuen's 3 PM appointment on the same day (Friday) requires any specific lab prep. Bring confirmation # FOUGZX.</p>
        <p><strong>Due:</strong> Friday July 17</p>
      </div>
    </div>

    <div class="card card-yellow">
      <div class="card-title">🟡 Stephanie's Infusion — Today (All Day) <span class="badge badge-yellow">TODAY</span></div>
      <div class="card-meta">Source: Google Calendar · Mon July 13, All Day</div>
      <div class="card-body">
        <p><strong>Why it matters:</strong> Stephanie has an infusion today. You may be needed for support, transportation, or coordination. No location listed in calendar.</p>
        <p><strong>Next step:</strong> Confirm logistics — do you need to be present or on call? Add location if known.</p>
        <p><strong>Due:</strong> Today, July 13</p>
      </div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════ FULL 7-DAY CALENDAR -->
<div class="section blue">
  <div class="section-title">📅 Full 7-Day Calendar — July 13–19, 2026</div>
  <div class="section-body">

    <!-- MONDAY -->
    <div class="day-header">📅 Monday, July 13, 2026 — TODAY</div>
    <div class="event-row">
      <div class="event-time">ALL DAY</div>
      <div class="event-detail">
        <div class="etitle">💉 Stephanie Infusion</div>
        <div class="emeta">
          <span class="badge badge-blue">CONFIRMED</span>
          No location listed · No attendees listed<br>
          <strong>Prep:</strong> Confirm location, transportation needs, and whether you need to be present.<br>
          <strong>Note:</strong> Block time around this if you're providing support.
        </div>
      </div>
    </div>

    <!-- TUESDAY -->
    <div class="day-header">📅 Tuesday, July 14, 2026</div>
    <div class="event-row">
      <div class="event-time">10:00–11:00 AM</div>
      <div class="event-detail">
        <div class="etitle">🐾 Stella</div>
        <div class="emeta">
          <span class="badge badge-blue">CONFIRMED</span>
          No location · No attendees<br>
          <strong>Prep:</strong> No details provided — likely a vet or grooming appointment for Stella. Confirm address and any prep needed (fasting, paperwork).
        </div>
      </div>
    </div>

    <!-- WEDNESDAY -->
    <div class="day-header">📅 Wednesday, July 15, 2026 — ⚠️ CONFLICT + RSVP NEEDED</div>
    <div class="event-row">
      <div class="event-time">8:30–9:05 AM</div>
      <div class="event-detail">
        <div class="etitle">🏥 IMAGING APPOINTMENT — LH Radiology</div>
        <div class="emeta">
          <span class="badge badge-blue">CONFIRMED</span>
          📍 400 East 66th Street, New York<br>
          <strong>Prep:</strong> Complete pre-registration forms before arrival. Check-in at 8:30 AM sharp. Bring ID and insurance.<br>
          <strong>Exam:</strong> Details omitted from calendar description — confirm exam type with provider.
        </div>
        <div class="conflict-warn">⚠️ CONFLICT: "Bone Density" appointment also at 8:30 AM — likely the same event entered twice. Verify and remove duplicate before Wednesday.</div>
      </div>
    </div>
    <div class="event-row">
      <div class="event-time">8:30–9:30 AM</div>
      <div class="event-detail">
        <div class="etitle">🦴 Bone Density Scan</div>
        <div class="emeta">
          <span class="badge badge-blue">CONFIRMED</span>
          No separate location listed<br>
          <strong>Likely same as Imaging Appointment above — confirm and consolidate.</strong>
        </div>
      </div>
    </div>
    <div class="event-row">
      <div class="event-time">12:00–1:30 PM</div>
      <div class="event-detail">
        <div class="etitle">🤝 HR Networking &amp; Job Search Group — Zoom</div>
        <div class="emeta">
          <span class="badge badge-yellow">RSVP NEEDED</span>
          🔗 <a href="https://us06web.zoom.us/j/81954171722" target="_blank">Zoom Link</a> · 180+ attendees<br>
          <strong>Prep:</strong> Review HR Networking Team Guidelines (link in calendar invite). Prepare brief intro / elevator pitch. Have résumé/LinkedIn profile current.<br>
          <strong>Note:</strong> "Network" calendar block at same time is likely the same event — confirm.
        </div>
      </div>
    </div>
    <div class="event-row">
      <div class="event-time">12:00–1:30 PM</div>
      <div class="event-detail">
        <div class="etitle">🤝 Network (Calendar Block)</div>
        <div class="emeta">
          <span class="badge badge-blue">CONFIRMED</span>
          No details — likely duplicate of HR Networking Zoom above. Verify and remove if redundant.
        </div>
      </div>
    </div>

    <!-- THURSDAY -->
    <div class="day-header">📅 Thursday, July 16, 2026</div>
    <div class="event-row">
      <div class="event-time">9:00–10:30 AM</div>
      <div class="event-detail">
        <div class="etitle">🏢 Executive Roundtable — Zoom (John Madigan)</div>
        <div class="emeta">
          <span class="badge badge-red">DECLINED</span>
          🔗 <a href="https://us02web.zoom.us/j/207786667" target="_blank">Zoom Link</a> · Meeting ID: 207 786 667 · Password: 205454<br>
          <strong>Status:</strong> You have declined this event.<br>
          <strong>Note:</strong> If your situation has changed, you can still rejoin — contact John Madigan to confirm.
        </div>
      </div>
    </div>
    <div class="event-row">
      <div class="event-time">12:00–1:00 PM</div>
      <div class="event-detail">
        <div class="etitle">🤝 HR Networking &amp; Job Search: Open Office Hours — Zoom</div>
        <div class="emeta">
          <span class="badge badge-yellow">RSVP NEEDED</span>
          🔗 <a href="https://us06web.zoom.us/j/85945371140" target="_blank">Zoom Link</a> · 180+ attendees<br>
          <strong>Important:</strong> Organizer explicitly requests no automated AI notetaking tools.<br>
          <strong>Prep:</strong> Prepare 1–2 specific questions or challenges to raise in open discussion.
        </div>
      </div>
    </div>
    <div class="event-row">
      <div class="event-time">1:00–2:00 PM</div>
      <div class="event-detail">
        <div class="etitle">☕ Tea with LeiLani | Brew At the Table</div>
        <div class="emeta">
          <span class="badge badge-green">ACCEPTED</span>
          📍 T Shop, 247 Elizabeth St, New York, NY 10012<br>
          <strong>Attendees:</strong> LeiLani (leilani@bethechangehr.com), Teresa Low, Leyla Snovini, Jessi (Alvi Solutions)<br>
          <strong>Prep:</strong> This is an in-person professional networking event — bring business cards or QR code for LinkedIn. Allow travel time from midtown if needed.
        </div>
      </div>
    </div>

    <!-- FRIDAY -->
    <div class="day-header">📅 Friday, July 17, 2026 — Medical Day</div>
    <div class="event-row">
      <div class="event-time">10:10–10:25 AM</div>
      <div class="event-detail">
        <div class="etitle">🧪 Quest Diagnostics Lab Appointment</div>
        <div class="emeta">
          <span class="badge badge-blue">CONFIRMED</span>
          📍 65 E 76th St, Professional Apt GR-G, New York, NY 10021<br>
          <strong>Confirmation #:</strong> FOUGZX · Activity: All Other Tests<br>
          <strong>Prep:</strong> Check fasting requirements. Arrive on time — 15-minute appointment window. Bring photo ID and insurance card.
        </div>
      </div>
    </div>
    <div class="event-row">
      <div class="event-time">3:00–4:00 PM</div>
      <div class="event-detail">
        <div class="etitle">👩‍⚕️ Dr. Yuen</div>
        <div class="emeta">
          <span class="badge badge-blue">CONFIRMED</span>
          No location listed · No attendees<br>
          <strong>Prep:</strong> Confirm office address. Bring Quest Diagnostics results if same-day turnaround. Allow travel time after lab at 10:10 AM.
        </div>
      </div>
    </div>

    <!-- SAT / SUN -->
    <div class="day-header">📅 Saturday, July 18 &amp; Sunday, July 19, 2026</div>
    <div class="event-row">
      <div class="event-time">No Events</div>
      <div class="event-detail">
        <div class="etitle">🗓 Clear Weekend</div>
        <div class="emeta">No calendar events scheduled. Use for rest, job application follow-ups, or prep for next week's networking.</div>
      </div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════ JOB SEARCH & PIPELINE -->
<div class="section green">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">

    <div class="card card-green">
      <div class="card-title">🟢 CHRO — City of New York <span class="badge badge-green">HIGH FIT</span></div>
      <div class="card-meta">LinkedIn Job Alert · Posted 7/11/2026 · Appeared in TWO separate alerts</div>
      <div class="card-body">
        <p>Senior executive HR leadership role for New York City government. Dual LinkedIn alerts suggest high algorithm relevance to your profile. Act quickly — government roles fill fast.</p>
        <p><strong>Action:</strong> Review full JD, tailor application materials, apply ASAP or reach out to NYC HR contacts.</p>
      </div>
    </div>

    <div class="card card-green">
      <div class="card-title">🟢 VP, People &amp; Talent — Armada <span class="badge badge-green">HIGH FIT</span></div>
      <div class="card-meta">LinkedIn Job Alert (jobs-noreply@linkedin.com) · Mon Jul 13, 7:05 AM</div>
      <div class="card-body">
        <p>LinkedIn identified this as similar to roles you've searched. VP-level People &amp; Talent position at Armada — strong match for your executive HR background.</p>
        <p><strong>Action:</strong> Review full JD on LinkedIn. Apply or connect with hiring manager/recruiter.</p>
      </div>
    </div>

    <div class="card card-green">
      <div class="card-title">🟢 Head of People Operations — Runpod <span class="badge badge-yellow">MEDIUM FIT</span></div>
      <div class="card-meta">LinkedIn Job Alert · Posted 7/10/2026</div>
      <div class="card-body">
        <p>AI/tech company (Runpod) seeking Head of People Operations. Tech sector HR leadership role — relevant given your interest in AI for Leaders content.</p>
        <p><strong>Action:</strong> Review and assess fit. Tech startup culture may differ from prior roles.</p>
      </div>
    </div>

    <div class="card card-yellow">
      <div class="card-title">🟡 Ahmad Raheed LinkedIn Message — OVERDUE REPLY <span class="badge badge-red">3 DAYS OLD</span></div>
      <div class="card-meta">LinkedIn (messages-noreply@linkedin.com) · Sent 3 days ago</div>
      <div class="card-body">
        <p>Someone named Ahmad Raheed sent you a direct LinkedIn message that has gone unanswered for 3 days. This could be a recruiter, peer, or connection with an opportunity.</p>
        <p><strong>Action:</strong> Open LinkedIn inbox immediately and reply today. Do not let this slip further.</p>
      </div>
    </div>

    <div class="card card-blue">
      <div class="card-title">👁 214 LinkedIn Profile Views This Week <span class="badge badge-teal">VISIBILITY HIGH</span></div>
      <div class="card-meta">LinkedIn (messages-noreply@linkedin.com) · Mon Jul 13, 11:05 AM</div>
      <div class="card-body">
        <p>Strong signal that your profile is being seen. This is a good moment to update your headline, ensure your availability status is set, and post or engage on LinkedIn to capitalize on the momentum.</p>
        <p><strong>Action:</strong> Check who viewed your profile (if Premium). Engage with recent viewers.</p>
      </div>
    </div>

    <div class="card card-gray">
      <div class="card-title">📋 Ladders Job Digest — Roles Not on LinkedIn/Indeed <span class="badge badge-gray">REVIEW</span></div>
      <div class="card-meta">Ladders (jobs@my.theladders.com) · 2 emails, Sun Jul 12</div>
      <div class="card-body">
        <p>Includes "Lead Fraud Data Scientist" at Gemini and other roles not surfaced by LinkedIn. Duplicate email received — likely a send error.</p>
        <p><strong>Action:</strong> Scan for relevant executive HR roles. Unsubscribe from duplicates.</p>
      </div>
    </div>

    <div class="card card-blue">
      <div class="card-title">🤝 HR Networking &amp; Job Search Group — Wed July 15 + Thu July 16 <span class="badge badge-blue">NETWORKING</span></div>
      <div class="card-meta">Google Calendar — Two Zoom sessions this week</div>
      <div class="card-body">
        <p>Large peer HR job search network. 180+ members including coaches, HR leaders, and recruiters. High-value touchpoint for leads, referrals, and moral support during search.</p>
        <p><strong>Action:</strong> RSVP both sessions. Prepare your 30-second update and 1–2 asks.</p>
      </div>
    </div>

    <div class="card card-teal">
      <div class="card-title">☕ Tea with LeiLani — Thu July 16, 1 PM <span class="badge badge-teal">IN-PERSON</span></div>
      <div class="card-meta">T Shop, 247 Elizabeth St, New York · Accepted</div>
      <div class="card-body">
        <p>In-person gathering with LeiLani (Be the Change HR), Teresa Low (consulting), Leyla Snovini, and Jessi (Alvi Solutions). Strong executive HR network — treat this as a strategic relationship-building opportunity.</p>
        <p><strong>Action:</strong> Research attendees before Thursday. Bring talking points about your search.</p>
      </div>
    </div>

    <div class="card card-gray">
      <div class="card-title">📋 Otter.ai — Upcoming Meetings Summary <span class="badge badge-gray">FYI</span></div>
      <div class="card-meta">Otter.ai (no-reply@otter.ai) · Mon Jul 13, 7:13 AM</div>
      <div class="card-body">
        <p>Weekly prep email from Otter.ai summarizing upcoming meetings. Review before your Wed/Thu Zoom sessions to set up transcription (but note: Thursday's Open Office Hours explicitly prohibits AI notetaking tools).</p>
      </div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════ FULL EMAIL REVIEW BY CATEGORY -->
<div class="section navy">
  <div class="section-title">📬 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="card card-red">
      <div class="card-title">🔴 Security / Risk — 8 Emails <span class="badge badge-red">HIGH RISK</span></div>
      <div class="card-body">
        <p><strong>Auto-Trashed (6) — Phishing / Scam (no action needed):</strong></p>
        <table>
          <tr><th>Sender</th><th>Subject</th><th>Auto-Trash Reason</th></tr>
          <tr><td>"Congratulations🎉" &lt;random domain&gt;</td><td>Check your account — 250 Welcome Free Spins <span class="phish-tag">AUTO-TRASHED</span></td><td>Fake casino payout verification / info harvesting from random domain</td></tr>
          <tr><td>"Congratulations🎰" &lt;random domain&gt;</td><td>130 Free Spins Pending in your Account <span class="phish-tag">AUTO-TRASHED</span></td><td>Fake casino no-deposit offer / info harvesting lure</td></tr>
          <tr><td>TractorSupply &lt;random domain&gt;</td><td>Confirmed: You won a Predator 3500W Generator <span class="phish-tag">AUTO-TRASHED</span></td><td>Fake Tractor Supply prize scam / credential harvesting</td></tr>
          <tr><td>"𝗣aym𝗲nt_Declin𝗲d©" &lt;obfuscated domain&gt;</td><td>Your Cloud ID locked — photos/videos will be removed <span class="phish-tag">AUTO-TRASHED</span></td><td>Spoofed payment/Cloud lock threat with Unicode evasion; random domain</td></tr>
          <tr><td>Atlassian &lt;po.atlassian.net&gt;</td><td>[Important] Jira subscription deactivation due to inactivity <span class="phish-tag">AUTO-TRASHED</span></td><td>Spoofed Atlassian from suspicious subdomain; urgency lure</td></tr>
          <tr><td>"'Lowe's®'" &lt;obfuscated domain&gt;</td><td>Claim Your Free $1000 Gift Set Today — 2nd attempt <span class="phish-tag">AUTO-TRASHED</span></td><td>Fake Lowe's prize/reward / info harvesting targeting username</td></tr>
        </table>
        <div class="divider"></div>
        <p><strong>Remaining Spam — In Non-Trash Folders (recommend manual trash/block):</strong></p>
        <table>
          <tr><th>Sender</th><th>Subject</th><th>Action</th></tr>
          <tr><td>Hot-Sex &lt;random domain&gt;</td><td>Make her squirt 3x tonight... <span class="spam-tag">EXPLICIT SPAM</span></td><td>Mark as spam &amp; block sender</td></tr>
          <tr><td>"🔶FUCK-BUDDY SECRET🔶" &lt;random domain&gt;</td><td>Force her into a meltdown... <span class="spam-tag">EXPLICIT SPAM</span></td><td>Mark as spam &amp; block sender</td></tr>
        </table>
        <p class="note">✅ All 6 auto-trashed phishing emails were caught before inbox delivery. No credentials were requested from you. No action beyond verification needed.</p>
      </div>
    </div>

    <!-- JOB SEARCH -->
    <div class="card card-green">
      <div class="card-title">🟢 Job Search — 6 Emails</div>
      <div class="card-body">
        <table>
          <tr><th>Sender</th><th>Subject</th><th>Priority</th><th>Action</th></tr>
          <tr><td>LinkedIn Job Alerts</td><td>CHRO at City of New York (×2 alerts)</td><td class="p-high">HIGH FIT</td><td>Apply immediately</td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>VP People &amp; Talent at Armada</td><td class="p-high">HIGH FIT</td><td>Review &amp; apply</td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>Head of People Operations at Runpod</td><td class="p-medium">MEDIUM FIT</td><td>Review</td></tr>
          <tr><td>Ladders (×2)</td><td>Jobs not on LinkedIn/Indeed (Lead Fraud Data Scientist, etc.)</td><td class="p-low">LOW–MEDIUM</td><td>Scan for HR roles; unsubscribe from duplicate</td></tr>
        </table>
      </div>
    </div>

    <!-- RECRUITERS / NETWORKING -->
    <div class="card card-green">
      <div class="card-title">🟢 Recruiters / Networking — 3 Emails</div>
      <div class="card-body">
        <table>
          <tr><th>Sender</th><th>Subject</th><th>Action</th></tr>
          <tr><td>LinkedIn</td><td>Ahmad Raheed sent you a message 3 days ago</td><td><strong>Reply today — overdue</strong></td></tr>
          <tr><td>LinkedIn</td><td>214 people visited your profile</td><td>Review viewers; post/engage on profile</td></tr>
          <tr><td>Otter.ai</td><td>Your upcoming meetings</td><td>Review for meeting prep; disable for Thu open office hours</td></tr>
        </table>
      </div>
    </div>

    <!-- CALENDAR / EVENTS -->
    <div class="card card-blue">
      <div class="card-title">🔵 Calendar / Events — 1 Email</div>
      <div class="card-body">
        <table>
          <tr><th>Sender</th><th>Subject</th><th>Action</th></tr>
          <tr><td>Allie Taylor (VFAR)</td><td>Exciting News: A New Chapter at Voters For Animal Rights</td><td>Read when available — leadership transition announcement from nonprofit. No action required immediately.</td></tr>
        </table>
      </div>
    </div>

    <!-- MEDICAL / HEALTH -->
    <div class="card card-teal">
      <div class="card-title">🩺 Medical / Health — 1 Email</div>
      <div class="card-body">
        <table>
          <tr><th>Sender</th><th>Subject</th><th>Action</th></tr>
          <tr><td>USPS Informed Delivery</td><td>Daily Digest — 2 mailpieces + 2 inbound packages</td><td>Check mail today. One or more packages may be medical-related given this week's appointments. (Note: USPS digest categorized here as it ties to incoming health correspondence.)</td></tr>
        </table>
      </div>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="card card-yellow">
      <div class="card-title">🟡 Financial / Billing — 0 Emails</div>
      <div class="card-body">
        <p>No billing or financial emails in today's data. Note: The auto-trashed "Payment Declined / Cloud ID locked" email was a phishing attempt — <strong>not</strong> a real billing notice. No action needed.</p>
      </div>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="card card-purple">
      <div class="card-title">🟣 Professional Development — 4 Emails</div>
      <div class="card-body">
        <table>
          <tr><th>Sender</th><th>Subject</th><th>Action</th></tr>
          <tr><td>AI For Leaders</td><td>The Jobs Crisis the Data Still Hasn't Found (Dario Amodei / white-collar job displacement)</td><td>Read — highly relevant to your HR executive practice</td></tr>
          <tr><td>Medium Daily Digest</td><td>I'll Instantly Know A Writer Used ChatGPT (Matt Lillywhite)</td><td>Optional read — AI writing detection</td></tr>
          <tr><td>Medium Daily Digest</td><td>UX didn't die. It just stopped being about screens (Nurkhon)</td><td>Optional read — future of UX</td></tr>
          <tr><td>Alison Courses</td><td>Melissa A, find a new course to explore</td><td>Scan for relevant HR/leadership certifications</td></tr>
        </table>
      </div>
    </div>

    <!-- PERSONAL -->
    <div class="card card-teal">
      <div class="card-title">🔵 Personal — 4 Emails</div>
      <div class="card-body">
        <table>
          <tr><th>Sender</th><th>Subject</th><th>Action</th></tr>
          <tr><td>melissa (self)</td><td>Melissa's Daily Briefing — July 13, 2026</td><td>Prior self-briefing — superseded by this document</td></tr>
          <tr><td>Match</td><td>You've had a profile view from Sal (66, Hartford, CT)</td><td>Review when available — personal</td></tr>
          <tr><td>OkCupid</td><td>Someone likes you</td><td>Review when available — personal</td></tr>
          <tr><td>Chick-fil-A</td><td>A little something to say thank you 🎁 (free reward)</td><td>Redeem reward when convenient</td></tr>
        </table>
      </div>
    </div>

    <!-- NEWSLETTERS / SUBSCRIPTIONS -->
    <div class="card card-purple">
      <div class="card-title">🟣 Newsletters &amp; Subscriptions — 7 Emails</div>
      <div class="card-body">
        <table>
          <tr><th>Sender</th><th>Subject</th><th>Action</th></tr>
          <tr><td>The AI Report</td><td>⚡ Apple sues OpenAI for theft; Meta kills Instagram AI feature</td><td>Read — relevant AI industry news</td></tr>
          <tr><td>1% Better</td><td>Apple Sues OpenAI, Lindsey Graham, 100 AI Side Hustles</td><td>Scan — in Trash (see Trash Review)</td></tr>
          <tr><td>The Hustle</td><td>🏊 Swim in your neighbor's pool; phone-free events, AI art</td><td>Optional read — light business/culture</td></tr>
          <tr><td>The Daily Skimm</td><td>Sticking to stir fry (July 13 digest)</td><td>Optional read — general news</td></tr>
          <tr><td>The Average Joe</td><td>📉 Musical Chairs — Movin' in with Mom</td><td>In Trash — see Trash Review</td></tr>
          <tr><td>Martin / The People People Group</td><td>⏰ Too Little Too Late; Compensating Candidates</td><td>In Trash — HR newsletter (see Trash Review)</td></tr>
          <tr><td>Gemma Bonham-Carter</td><td>The smartest decision you've made all week</td><td>Scan — online business/entrepreneur content</td></tr>
        </table>
      </div>
    </div>

    <!-- PROMOTIONAL / RETAIL -->
    <div class="card card-gray">
      <div class="card-title">⬜ Promotional / Retail — 11 Emails</div>
      <div class="card-body">
        <p>See <strong>Promotional / Retail Summary</strong> section below for full breakdown. Brands include: SHEIN (×5), Kohl's, Gap Factory, CoolDeep AI (Trash), Lisa Rangel (Trash), "Ozempic by DirectMeds" (spam), Facebook Friend Suggestion.</p>
        <p><strong>Recommended action:</strong> Bulk-delete SHEIN duplicates. Review Kohl's/Gap Factory deals if relevant. Unsubscribe from irrelevant senders.</p>
      </div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════ TRASH REVIEW -->
<div class="section red">
  <div class="section-title">🗑️ Trash Review — Emails in Gmail Trash</div>
  <div class="section-body">

    <h3 style="margin-bottom:10px; color:#1a7a4a;">✅ Restore Immediately — 1 Item</h3>
    <table>
      <tr><th>Sender</th><th>Subject</th><th>Why Restore</th></tr>
      <tr>
        <td>Martin / The People People Group<br><small>martin@thepeoplepeoplegroup.com</small></td>
        <td>⏰ Too Little Too Late; Compensating Candidates &amp; Recognition on a Budget</td>
        <td>Legitimate HR professional newsletter — relevant to your career as an HR executive. Appears to have been trashed in error. Recommend restoring and moving to a "Newsletters" label.</td>
      </tr>
    </table>

    <div class="divider"></div>

    <h3 style="margin-bottom:10px; color:#f39c12;">🟡 Review Before Deleting — 2 Items</h3>
    <table>
      <tr><th>Sender</th><th>Subject</th><th>Notes</th></tr>
      <tr>
        <td>Lisa Rangel<br><small>lr@chameleonresumes.com</small></td>
        <td>Why your job search is exhausting you (there's an easier way)</td>
        <td>Chameleon Resumes is a legitimate executive résumé service. While the subject line is marketing-heavy, the content on executive job search fatigue may be relevant given your active search. Review once — then unsubscribe if not useful.</td>
      </tr>
      <tr>
        <td>1% Better<br><small>hello@onepercentimprovements.convertkit.com</small></td>
        <td>Apple Sues OpenAI, Lindsey Graham, and 100 AI Side Hustles</td>
        <td>Appears to be a legitimate growth/productivity newsletter. The "AI Side Hustles" content may be useful. Review and decide whether to subscribe or unsubscribe.</td>
      </tr>
    </table>

    <div class="divider"></div>

    <h3 style="margin-bottom:10px; color:#c0392b;">🔴 Safe to Delete (Confirm Permanent Deletion) — 7 Items</h3>
    <table>
      <tr><th>Sender</th><th>Subject</th><th>Reason</th></tr>
      <tr><td>"Casino Exclusive" &lt;random domain&gt;</td><td>Pending 150 FREE spins — melissaw212</td><td>Phishing / fake casino scam — permanently delete</td></tr>
      <tr><td>"Congratulations🎰" &lt;random domain&gt;</td><td>Check account — 250 Welcome Free Spins (Sun Jul 12)</td><td>Phishing duplicate — permanently delete</td></tr>
      <tr><td>"𝗖ongratulations🎉" &lt;random domain&gt;</td><td>Get 200 free spins with code LOVERFS</td><td>Fake casino info harvesting — permanently delete</td></tr>
      <tr><td>"Jellyfil.Secret.Trick" &lt;random domain&gt; (×2)</td><td>CNN Exposed Banned Kentucky Horses Trick... (Mon + Sun)</td><td>Explicit male enhancement spam — permanently delete both</td></tr>
      <tr><td>The Average Joe</td><td>📉 Musical Chairs — Movin' in with Mom</td><td>Low-value financial newsletter; trashed appropriately — delete</td></tr>
      <tr><td>CoolDeep AI</td><td>Wow. 50% off for next 48 hours (Nano Banana Use Cases)</td><td>Low-value promotional flash sale — delete</td></tr>
    </table>

  </div>
</div>

<!-- ═══════════════════════════════════════════ PROMOTIONAL / RETAIL SUMMARY -->
<div class="section gray">
  <div class="section-title">🛍️ Promotional / Retail Summary — 11 Emails</div>
  <div class="section-body">
    <table>
      <tr><th>Brand / Sender</th><th>Count</th><th>Subject / Theme</th><th>Recommendation</th></tr>
      <tr>
        <td>SHEIN<br><small>Multiple domains</small></td>
        <td>5</td>
        <td>Move-in Day Must-Haves (×2), All under $14.99 (×2), 🚨 NEW IN: Just Added 3 Days Ago (×1)</td>
        <td><span class="badge badge-red">DELETE DUPLICATES</span> Multiple duplicate sends. If you shop SHEIN, keep 1; unsubscribe from duplicate domains. Consider unsubscribing from all.</td>
      </tr>
      <tr>
        <td>Kohl's</td>
        <td>1</td>
        <td>30% off + Kohl's Cash — summer styles</td>
        <td><span class="badge badge-gray">OPTIONAL</span> Review if planning summer shopping. Otherwise delete.</td>
      </tr>
      <tr>
        <td>Gap Factory</td>
        <td>1</td>
        <td>Extra 55% off clearance + up to 75% off 1000s of styles</td>
        <td><span class="badge badge-gray">OPTIONAL</span> Strong sale — review if you shop Gap. Otherwise delete.</td>
      </tr>
      <tr>
        <td>CoolDeep AI <em>(Trash)</em></td>
        <td>1</td>
        <td>50% off flash sale — Nano Banana Use Cases (48 hrs)</td>
        <td><span class="badge badge-red">DELETE</span> Already in trash. Low-value AI tools flash sale. Permanently delete.</td>
      </tr>
      <tr>
        <td>"Ozempic by DirectMeds" <br><small>Obfuscated random domain</small></td>
        <td>1</td>
        <td>What If You Could Lose Weight Effortlessly? (GLP-1 meds)</td>
        <td><span class="badge badge-red">SPAM — DELETE</span> Unsolicited pharmaceutical marketing from suspicious domain. Mark as spam and delete.</td>
      </tr>
      <tr>
        <td>Facebook Friend Suggestions</td>
        <td>1</td>
        <td>You may know Vali Valicutza from Draganesti-Olt</td>
        <td><span class="badge badge-gray">IGNORE</span> Automated friend suggestion — low relevance. Delete or ignore.</td>
      </tr>
      <tr>
        <td>Chick-fil-A</td>
        <td>1</td>
        <td>A little something to say thank you 🎁 — free reward (402 pts)</td>
        <td><span class="badge badge-green">KEEP / REDEEM</span> Legitimate loyalty reward. Redeem when convenient.</td>
      </tr>
    </table>
    <p class="note">Total promotional emails: 11 (includes 1 in Trash). SHEIN represents 5 of these — consider unsubscribing from duplicate sender domains.</p>
  </div>
</div>

<!-- ═══════════════════════════════════════════ NEWSLETTERS & SUBSCRIPTIONS -->
<div class="section purple">
  <div class="section-title">📰 Newsletters &amp; Subscriptions</div>
  <div class="section-body">
    <table>
      <tr><th>Sender</th><th>Topic</th><th>Relevance</th><th>Recommendation</th></tr>
      <tr><td>AI For Leaders</td><td>AI impact on white-collar jobs / Dario Amodei warning</td><td>⭐⭐⭐ High — executive HR strategy</td><td><span class="badge badge-green">KEEP &amp; READ</span></td></tr>
      <tr><td>The AI Report</td><td>Apple vs. OpenAI; Meta AI feature rollback</td><td>⭐⭐⭐ High — AI industry news</td><td><span class="badge badge-green">KEEP &amp; READ</span></td></tr>
      <tr><td>1% Better (Trash)</td><td>Apple/OpenAI, AI side hustles</td><td>⭐⭐ Medium — broad AI/productivity</td><td><span class="badge badge-yellow">REVIEW — RESTORE FROM TRASH, THEN DECIDE</span></td></tr>
      <tr><td>Medium Daily Digest (×2)</td><td>AI writing detection; UX evolution</td><td>⭐⭐ Medium — professional/tech trends</td><td><span class="badge badge-yellow">KEEP — SKIM WEEKLY</span></td></tr>
      <tr><td>The People People Group (Trash)</td><td>HR compensation; candidate experience</td><td>⭐⭐⭐ High — direct HR relevance</td><td><span class="badge badge-green">RESTORE &amp; KEEP</span></td></tr>
      <tr><td>Gemma Bonham-Carter</td><td>Online business / entrepreneurship</td><td>⭐ Low–Medium — general business</td><td><span class="badge badge-gray">OPTIONAL — REVIEW OR UNSUBSCRIBE</span></td></tr>
      <tr><td>The Hustle</td><td>Business culture, trends, humor</td><td>⭐⭐ Medium — general business</td><td><span class="badge badge-yellow">KEEP — SKIM</span></td></tr>
      <tr><td>The Daily Skimm</td><td>General news digest</td><td>⭐ Low — general awareness</td><td><span class="badge badge-gray">KEEP IF ENJOYED — OTHERWISE UNSUBSCRIBE</span></td></tr>
      <tr><td>The Average Joe (Trash)</td><td>Personal finance / housing economics</td><td>⭐ Low — not career-specific</td><td><span class="badge badge-red">DELETE — ALREADY IN TRASH</span></td></tr>
      <tr><td>Lisa Rangel / Chameleon Résumés
