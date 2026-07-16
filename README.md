<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa — July 16, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrapper { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* Header */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: .5px; }
  .header .subtitle { font-size: 15px; color: #a8c0e8; margin-top: 6px; }
  .header-meta { display: flex; gap: 28px; margin-top: 18px; flex-wrap: wrap; }
  .header-meta-item { background: rgba(255,255,255,0.09); border-radius: 8px; padding: 10px 18px; text-align: center; }
  .header-meta-item .val { font-size: 22px; font-weight: 700; color: #7eb8f7; }
  .header-meta-item .lbl { font-size: 11px; color: #a8c0e8; text-transform: uppercase; letter-spacing: .8px; margin-top: 2px; }

  /* Section headings */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; letter-spacing: .4px; margin-bottom: 14px; padding-bottom: 7px; border-bottom: 2px solid #e2e6ea; display: flex; align-items: center; gap: 8px; }
  .section-title .icon { font-size: 18px; }

  /* Color bands */
  .band-red    { border-left: 5px solid #e53935; background: #fff5f5; }
  .band-yellow { border-left: 5px solid #f9a825; background: #fffde7; }
  .band-blue   { border-left: 5px solid #1565c0; background: #e8f1ff; }
  .band-green  { border-left: 5px solid #2e7d32; background: #f1f8f2; }
  .band-purple { border-left: 5px solid #6a1b9a; background: #f8f0ff; }
  .band-gray   { border-left: 5px solid #90a4ae; background: #f5f7f8; }

  /* Cards */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; }
  .card h3 { font-size: 14px; font-weight: 700; margin-bottom: 6px; }
  .card .meta { font-size: 12px; color: #5a6a7a; margin-bottom: 6px; }
  .card p { font-size: 13px; }
  .card .tag { display: inline-block; font-size: 11px; font-weight: 700; border-radius: 4px; padding: 2px 8px; margin-right: 5px; margin-top: 6px; text-transform: uppercase; letter-spacing: .6px; }
  .tag-red    { background:#fde8e8; color:#c62828; }
  .tag-yellow { background:#fff8e1; color:#f57f17; }
  .tag-blue   { background:#e3f0ff; color:#1565c0; }
  .tag-green  { background:#e8f5e9; color:#1b5e20; }
  .tag-purple { background:#f3e5f5; color:#4a148c; }
  .tag-gray   { background:#eceff1; color:#455a64; }
  .tag-orange { background:#fff3e0; color:#e65100; }

  /* Executive Summary bullets */
  .exec-summary { list-style: none; padding: 0; }
  .exec-summary li { padding: 12px 16px; border-radius: 8px; margin-bottom: 10px; display: flex; gap: 12px; align-items: flex-start; font-size: 13.5px; }
  .exec-summary li .bullet-icon { font-size: 20px; flex-shrink: 0; margin-top: 1px; }

  /* Tables */
  table { width: 100%; border-collapse: collapse; font-size: 13px; margin-top: 4px; }
  th { background: #1a1a2e; color: #fff; padding: 9px 12px; text-align: left; font-size: 12px; letter-spacing: .5px; }
  td { padding: 8px 12px; vertical-align: top; border-bottom: 1px solid #e6eaf0; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #f8fafc; }
  .tbl-wrap { border-radius: 10px; overflow: hidden; border: 1px solid #dde3ec; margin-bottom: 12px; }

  /* Calendar day blocks */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { font-size: 13px; font-weight: 700; background: #1a1a2e; color: #7eb8f7; padding: 7px 14px; border-radius: 7px 7px 0 0; }
  .cal-event { padding: 10px 14px; border-bottom: 1px solid #e6eaf0; background: #fff; display: flex; gap: 14px; align-items: flex-start; }
  .cal-event:last-child { border-bottom: none; border-radius: 0 0 7px 7px; }
  .cal-time { font-weight: 700; font-size: 12px; color: #1565c0; min-width: 90px; }
  .cal-details .title { font-weight: 700; font-size: 13px; }
  .cal-details .sub { font-size: 12px; color: #5a6a7a; margin-top: 2px; }
  .cal-details .prep { font-size: 12px; color: #6a1b9a; margin-top: 3px; }
  .status-pill { display: inline-block; font-size: 10px; font-weight: 700; border-radius: 10px; padding: 2px 8px; text-transform: uppercase; letter-spacing: .5px; }
  .pill-accepted  { background:#e8f5e9; color:#2e7d32; }
  .pill-declined  { background:#fde8e8; color:#c62828; }
  .pill-pending   { background:#fff8e1; color:#f57f17; }
  .pill-confirmed { background:#e3f0ff; color:#1565c0; }

  /* Dashboard grid */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; }
  .dash-widget { border-radius: 10px; padding: 16px; text-align: center; }
  .dash-widget .dw-num { font-size: 30px; font-weight: 800; }
  .dash-widget .dw-lbl { font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: .7px; margin-top: 4px; }

  /* Priority action table */
  .pri-high   { color: #c62828; font-weight: 700; }
  .pri-medium { color: #f57f17; font-weight: 700; }
  .pri-low    { color: #2e7d32; font-weight: 700; }

  /* Top 3 */
  .top3 { counter-reset: top3counter; }
  .top3-item { background: #fff; border-radius: 10px; padding: 16px 20px 16px 56px; margin-bottom: 12px; position: relative; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-left: 5px solid #1565c0; }
  .top3-item::before { counter-increment: top3counter; content: counter(top3counter); position: absolute; left: 14px; top: 50%; transform: translateY(-50%); font-size: 26px; font-weight: 900; color: #1565c0; opacity: .2; }
  .top3-item h3 { font-size: 14px; font-weight: 700; }
  .top3-item p { font-size: 13px; color: #4a5568; margin-top: 4px; }

  /* Misc */
  .note-box { background:#fff3cd; border-left:4px solid #f9a825; border-radius:6px; padding:10px 14px; font-size:12.5px; margin-top:10px; }
  .phishing-row td { background: #fff0f0 !important; }
  .separator { height: 2px; background: linear-gradient(to right, #1a1a2e, #0f3460, #1a1a2e); border-radius: 2px; margin: 10px 0 22px 0; opacity: .15; }

  @media(max-width:600px){
    .header { padding:20px; }
    .header h1 { font-size:20px; }
    .header-meta { gap:10px; }
  }
</style>
</head>
<body>
<div class="page-wrapper">

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 1. HEADER -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="header">
  <div class="subtitle">EXECUTIVE BRIEFING · PREPARED BY YOUR CHIEF OF STAFF</div>
  <h1>Good Morning, Melissa ☀️</h1>
  <div class="subtitle">Thursday, July 16, 2026 &nbsp;|&nbsp; New York, NY</div>
  <div class="header-meta">
    <div class="header-meta-item"><div class="val">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="header-meta-item"><div class="val">11</div><div class="lbl">Calendar Events</div></div>
    <div class="header-meta-item"><div class="val">10</div><div class="lbl">Phishing / Scams Auto-Trashed</div></div>
    <div class="header-meta-item"><div class="val">3</div><div class="lbl">Action Required Today</div></div>
    <div class="header-meta-item"><div class="val">2</div><div class="lbl">Events Today</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 2. EXECUTIVE SUMMARY -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">⚡</span> Executive Summary</div>
  <ul class="exec-summary">
    <li class="card band-red">
      <span class="bullet-icon">🚨</span>
      <div><strong>BIGGEST RISK:</strong> Ten phishing/scam emails targeted you today using spoofed cloud storage, fake payment declines, casino lures, and fake prize offers — all auto-trashed. Additionally, two suspicious "Dr. Arthur Green" and "Lucky Creek Casino" emails are sitting in your inbox/spam area and require manual deletion. Stay vigilant; the volume suggests your email address is on a harvested list.</div>
    </li>
    <li class="card band-green">
      <span class="bullet-icon">💼</span>
      <div><strong>BIGGEST OPPORTUNITY:</strong> Horizon Media confirmed receipt of your application for <strong>Director, HR Business Partner</strong> (Workday notification received today). Amber Krusza from Formative SP has messaged you on LinkedIn and sent a calendar invite for <strong>tomorrow, Fri Jul 17 at 3:30 PM</strong> — this is a live recruiter lead requiring immediate response. Also, Glassdoor alerts show active openings at Stanford University and Landmark Properties.</div>
    </li>
    <li class="card band-blue">
      <span class="bullet-icon">📅</span>
      <div><strong>BIGGEST CALENDAR ITEM:</strong> You have two events <strong>today</strong>: HR Networking Open Office Hours at noon (RSVP still pending — action needed) and Tea with LeiLani at 1 PM at T Shop, 247 Elizabeth St (accepted). Tomorrow brings a Quest Diagnostics appointment at 10:10 AM and a Dr. Yuen appointment at 3 PM — plus the Amber Krusza recruiter call at 3:30 PM pending your acceptance.</div>
    </li>
  </ul>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 3. ACTION REQUIRED -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">🔴</span> Action Required</div>

  <div class="card band-green">
    <span class="tag tag-green">HIGH PRIORITY</span><span class="tag tag-yellow">RESPOND TODAY</span>
    <h3>🔗 LinkedIn Message from Amber Krusza (Formative SP) + Calendar Invite</h3>
    <div class="meta">From: Amber Krusza via LinkedIn &amp; amber.krusza@formativesp.com · Thu Jul 16, 2026</div>
    <p>Amber messaged you on LinkedIn (unread) and separately sent a calendar invitation for <strong>Fri Jul 17, 3:30–4:00 PM EDT</strong>. The calendar invite is currently showing as "unknown sender" (you haven't interacted with her before). This is a live recruiter outreach that requires a prompt, professional reply.</p>
    <p style="margin-top:8px;"><strong>📌 Next Step:</strong> Read Amber's LinkedIn message today. Accept or decline the calendar invite. Confirm the meeting context (role, company, scope) before the call.</p>
    <p style="margin-top:6px;"><strong>⏰ Due:</strong> Today — meeting is tomorrow at 3:30 PM</p>
  </div>

  <div class="card band-yellow">
    <span class="tag tag-yellow">RSVP NEEDED</span>
    <h3>📋 HR Networking &amp; Job Search: Open Office Hours — Today at Noon</h3>
    <div class="meta">Calendar · Thu Jul 16, 12:00–1:00 PM EDT · Zoom</div>
    <p>Your RSVP status is <strong>"Needs Action"</strong> for today's HR Networking Open Office Hours Zoom session. The meeting begins in a few hours. This is a large group call (170+ attendees) focused on job search networking — highly relevant given your active search.</p>
    <p style="margin-top:8px;"><strong>📌 Next Step:</strong> RSVP now. Note: the invite requests you disable automated AI notetaking tools. Join link: <a href="https://us06web.zoom.us/j/85945371140">Zoom Link</a></p>
    <p style="margin-top:6px;"><strong>⏰ Due:</strong> Today — 12:00 PM EDT</p>
  </div>

  <div class="card band-yellow">
    <span class="tag tag-yellow">BILLING / RECEIPT</span>
    <h3>🧾 Anthropic Receipt #2791-7051-8194 — Review &amp; File</h3>
    <div class="meta">From: Anthropic, PBC · invoice+statements@mail.anthropic.com · Thu Jul 16, 2:21 AM</div>
    <p>A new receipt has arrived from Anthropic (Claude/AI subscription). This appears to be a legitimate billing notification. Review the amount, confirm it matches your expected subscription, and file for expense tracking.</p>
    <p style="margin-top:8px;"><strong>📌 Next Step:</strong> Open email, verify charge amount, file receipt. If the amount is unexpected, contact Anthropic support.</p>
    <p style="margin-top:6px;"><strong>⏰ Due:</strong> Today or tomorrow</p>
  </div>

  <div class="card band-yellow">
    <span class="tag tag-yellow">RSVP NEEDED</span>
    <h3>📋 Amber Krusza Calendar Invite — Fri Jul 17, 3:30 PM</h3>
    <div class="meta">From: amber.krusza@formativesp.com · Thu Jul 16, 2026</div>
    <p>Calendar invite sitting in your inbox from an "unknown sender" (Amber Krusza, Formative SP) for a 30-minute meeting tomorrow. The invite is unaccepted. Cross-reference with her LinkedIn message before accepting.</p>
    <p style="margin-top:8px;"><strong>📌 Next Step:</strong> Read LinkedIn DM first, then accept the calendar invite to confirm the meeting.</p>
    <p style="margin-top:6px;"><strong>⏰ Due:</strong> Today</p>
  </div>

  <div class="card band-red">
    <span class="tag tag-red">SECURITY</span>
    <h3>🗑️ Delete Remaining Non-Auto-Trashed Scam Emails Manually</h3>
    <div class="meta">Senders: "Dr. Arthur Green" · "Lucky Creek Casino" (melissaw212@) · "Vapofil Men Over 40" · OkCupid (2 emails, not in inbox)</div>
    <p>Several scam/spam emails were NOT auto-trashed and are sitting in your account. These include a male-enhancement scam, a casino promo from a spoofed "self" address, and adult supplement spam. They should be manually deleted and the senders blocked.</p>
    <p style="margin-top:8px;"><strong>📌 Next Step:</strong> Delete and block: "Dr. Arthur Green" (brfqwalgkxwuvg...), "melissaw212" casino sender (uqdxsupportrg@...), "Vapofil Men Over 40" (bscsupportfy@...), OkCupid duplicates if unwanted, and Old Navy / Chumba casino non-auto-trashed items.</p>
    <p style="margin-top:6px;"><strong>⏰ Due:</strong> Today</p>
  </div>

  <div class="card band-blue">
    <span class="tag tag-blue">API / TECH</span>
    <h3>🔔 Nokia API Hub — New Announcement for JSearch API</h3>
    <div class="meta">From: Nokia API Hub · support@rapidapi.com · Thu Jul 16, 5:31 AM</div>
    <p>There is a new announcement from the JSearch API on RapidAPI. If you are actively using this API (likely for job search tooling), this may affect your integration or pricing tier.</p>
    <p style="margin-top:8px;"><strong>📌 Next Step:</strong> Log into your RapidAPI Developer Dashboard and review the announcement. Assess any impact on active projects.</p>
    <p style="margin-top:6px;"><strong>⏰ Due:</strong> This week</p>
  </div>

  <div class="card band-blue">
    <span class="tag tag-blue">LEGAL / COMPLIANCE</span>
    <h3>📄 Resend — Subprocessor List Update Notice</h3>
    <div class="meta">From: Resend · legal@notifications.resend.com · Thu Jul 16, 8:43 AM</div>
    <p>Resend (email infrastructure service) has updated its list of subprocessors — a standard legal/compliance notification. If you use Resend for any business or side project, review the changes for data compliance.</p>
    <p style="margin-top:8px;"><strong>📌 Next Step:</strong> Read and file. If relevant to any active project, log for compliance review.</p>
    <p style="margin-top:6px;"><strong>⏰ Due:</strong> This week</p>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 4. FULL 7-DAY CALENDAR -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">📅</span> Full 7-Day Calendar</div>

  <!-- THURSDAY JULY 16 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 THURSDAY, JULY 16, 2026 — TODAY</div>

    <div class="cal-event band-red" style="background:#fff5f5;">
      <div class="cal-time">9:00 – 10:30 AM</div>
      <div class="cal-details">
        <div class="title">Executive Roundtable <span class="status-pill pill-declined">Declined</span></div>
        <div class="sub">Hosted by: John Madigan · Zoom · Meeting ID: 207 786 667 · PW: 205454</div>
        <div class="sub"><a href="https://us02web.zoom.us/j/207786667">Zoom Link</a></div>
        <div class="prep">⚠️ You have declined this event. No action needed unless you wish to reconsider.</div>
      </div>
    </div>

    <div class="cal-event band-yellow" style="background:#fffde7;">
      <div class="cal-time">12:00 – 1:00 PM</div>
      <div class="cal-details">
        <div class="title">HR Networking &amp; Job Search: Open Office Hours — Zoom 2 <span class="status-pill pill-pending">RSVP Needed</span></div>
        <div class="sub">170+ attendees · Large group networking session · No AI notetaking allowed</div>
        <div class="sub"><a href="https://us06web.zoom.us/j/85945371140">Zoom Link</a></div>
        <div class="prep">🔔 ACTION: RSVP now. Disable AI notetaking tools before joining. Prepare a brief 30-second intro for networking.</div>
      </div>
    </div>

    <div class="cal-event band-green" style="background:#f1f8f2;">
      <div class="cal-time">1:00 – 2:00 PM</div>
      <div class="cal-details">
        <div class="title">Tea with LeiLani | Brew At the Table <span class="status-pill pill-accepted">Accepted</span></div>
        <div class="sub">📍 T Shop, 247 Elizabeth St, New York, NY 10012</div>
        <div class="sub">Attendees: leilani@bethechangehr.com, tlow@teresalowconsulting.com, leylasnovini@gmail.com, jessi@alvisolutions.com</div>
        <div class="prep">✅ Confirmed. Allow travel time from wherever you are at 12 PM. Professional networking opportunity — bring business cards or LinkedIn QR. Follows immediately after Zoom session.</div>
        <div class="prep">⚠️ CONFLICT: Zoom ends at 1 PM; T Shop is in-person. Plan to leave Zoom on time.</div>
      </div>
    </div>
  </div>

  <!-- FRIDAY JULY 17 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 FRIDAY, JULY 17, 2026 — TOMORROW</div>

    <div class="cal-event band-blue" style="background:#e8f1ff;">
      <div class="cal-time">10:10 – 10:25 AM</div>
      <div class="cal-details">
        <div class="title">Quest Diagnostics Appointment <span class="status-pill pill-confirmed">Confirmed</span></div>
        <div class="sub">📍 Quest Diagnostics – 65 E 76th St, Professional Apt GR-G, New York, NY 10021</div>
        <div class="sub">Confirmation #: FOUGZX · Activity: All Other Tests</div>
        <div class="prep">🩺 Bring photo ID and insurance card. Check Quest's fasting requirements for your test type. Appointment is only 15 min — arrive a few minutes early.</div>
      </div>
    </div>

    <div class="cal-event band-yellow" style="background:#fffde7;">
      <div class="cal-time">3:00 – 4:00 PM</div>
      <div class="cal-details">
        <div class="title">Dr. Yuen <span class="status-pill pill-confirmed">Confirmed</span></div>
        <div class="sub">📍 Location not specified</div>
        <div class="prep">🩺 Confirm location/address and any prep instructions for Dr. Yuen's office. Add travel time buffer.</div>
      </div>
    </div>

    <div class="cal-event band-green" style="background:#f1f8f2;">
      <div class="cal-time">3:30 – 4:00 PM</div>
      <div class="cal-details">
        <div class="title">melissa weiss and Amber Krusza (Recruiter Call) <span class="status-pill pill-pending">Needs RSVP</span></div>
        <div class="sub">From: amber.krusza@formativesp.com (Formative SP) · Invite received via email</div>
        <div class="prep">⚠️ CONFLICT: Overlaps with Dr. Yuen (3:00–4:00 PM). Verify whether Dr. Yuen ends before 3:30 PM or if you need to reschedule one of these. Read Amber's LinkedIn DM first; then RSVP.</div>
        <div class="prep">📌 ACTION REQUIRED: Accept or decline today.</div>
      </div>
    </div>
  </div>

  <!-- SATURDAY JULY 18 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 SATURDAY, JULY 18, 2026</div>
    <div class="cal-event" style="background:#f8fafc; padding:12px 14px; border-radius:0 0 7px 7px;">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="title" style="color:#90a4ae;">No Events Scheduled</div>
        <div class="sub">Rest &amp; Recovery Day — use for job search prep or self-care.</div>
      </div>
    </div>
  </div>

  <!-- SUNDAY JULY 19 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 SUNDAY, JULY 19, 2026</div>
    <div class="cal-event" style="background:#f8fafc; padding:12px 14px; border-radius:0 0 7px 7px;">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="title" style="color:#90a4ae;">No Events Scheduled</div>
        <div class="sub">Prepare for Monday's PT session and review any outstanding job applications.</div>
      </div>
    </div>
  </div>

  <!-- MONDAY JULY 20 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 MONDAY, JULY 20, 2026</div>

    <div class="cal-event band-blue" style="background:#e8f1ff;">
      <div class="cal-time">1:45 – 2:45 PM</div>
      <div class="cal-details">
        <div class="title">PT (Physical Therapy) <span class="status-pill pill-confirmed">Confirmed</span> <span style="font-size:11px; color:#e65100; font-weight:700; margin-left:6px;">⚠️ DUPLICATE</span></div>
        <div class="sub">📍 Location not specified · Note: This event appears twice in calendar data (duplicate entry)</div>
        <div class="prep">🏃 Confirm PT location and bring any relevant health documentation. Consider removing the duplicate calendar entry.</div>
      </div>
    </div>
  </div>

  <!-- TUESDAY JULY 21 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 TUESDAY, JULY 21, 2026</div>

    <div class="cal-event band-purple" style="background:#f8f0ff;">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="title">🎂 Eric Dordick's Birthday <span class="status-pill pill-confirmed">Noted</span></div>
        <div class="sub">All-day calendar reminder</div>
        <div class="prep">🎉 Send Eric a birthday message or card today. Don't let this slip past.</div>
      </div>
    </div>

    <div class="cal-event band-green" style="background:#f1f8f2;">
      <div class="cal-time">10:00 – 11:00 AM</div>
      <div class="cal-details">
        <div class="title">Umi <span class="status-pill pill-confirmed">Confirmed</span></div>
        <div class="sub">📍 Location not specified · Attendees not listed</div>
        <div class="prep">📌 No description provided. Confirm the purpose of this meeting (networking, personal, professional?) and add location/dial-in if needed.</div>
      </div>
    </div>
  </div>

  <!-- WEDNESDAY JULY 22 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 WEDNESDAY, JULY 22, 2026</div>

    <div class="cal-event band-yellow" style="background:#fffde7;">
      <div class="cal-time">12:00 – 1:30 PM</div>
      <div class="cal-details">
        <div class="title">HR Networking &amp; Job Search Group — Zoom 2 <span class="status-pill pill-pending">RSVP Needed</span></div>
        <div class="sub">170+ attendees · <a href="https://us06web.zoom.us/j/81954171722">Zoom Link</a></div>
        <div class="sub">Resources: HR Networking Team Guidelines, Job search prep materials</div>
        <div class="prep">📌 RSVP needed. This is the longer weekly group session (90 min). Block your calendar accordingly and prepare questions or updates to share with the group.</div>
      </div>
    </div>

    <div class="cal-event band-gray" style="background:#f5f7f8;">
      <div class="cal-time">12:00 – 1:30 PM</div>
      <div class="cal-details">
        <div class="title">Network <span class="status-pill pill-confirmed">Confirmed</span> <span style="font-size:11px; color:#e65100; font-weight:700; margin-left:6px;">⚠️ POSSIBLE DUPLICATE</span></div>
        <div class="sub">No location, no attendees, no description — may be a personal placeholder overlapping the group Zoom above</div>
        <div class="prep">📌 Verify if this is a separate commitment or a duplicate. Remove if redundant.</div>
      </div>
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 5. JOB SEARCH & INTERVIEW PIPELINE -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">💼</span> Job Search &amp; Interview Pipeline</div>

  <div class="tbl-wrap">
    <table>
      <thead><tr><th>Fit</th><th>Type</th><th>Source / Sender</th><th>Detail</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td><span class="tag tag-green">HIGH</span></td>
          <td>Recruiter Outreach</td>
          <td>Amber Krusza · Formative SP<br><small>amber.krusza@formativesp.com</small></td>
          <td>LinkedIn DM + calendar invite for Fri Jul 17, 3:30–4:00 PM. Live recruiter contact — most urgent lead.</td>
          <td class="pri-high">READ DM + RSVP TODAY</td>
        </tr>
        <tr>
          <td><span class="tag tag-green">HIGH</span></td>
          <td>Application Confirmation</td>
          <td>Workday · Horizon Media<br><small>horizonmedia@myworkday.com</small></td>
          <td>Application received for <strong>Director, HR Business Partner</strong>. Standard acknowledgment. No interview scheduled yet.</td>
          <td class="pri-medium">Monitor for next steps · Follow up in 1 week if no contact</td>
        </tr>
        <tr>
          <td><span class="tag tag-yellow">MEDIUM</span></td>
          <td>Job Alert — New York</td>
          <td>Glassdoor Jobs<br><small>noreply@glassdoor.com</small></td>
          <td>Community Manager – Wellness at Jetzy + 6 more NY roles. Landmark Properties mentioned. (Email trashed — review before deleting)</td>
          <td class="pri-medium">Restore from trash · Review roles · Apply if relevant</td>
        </tr>
        <tr>
          <td><span class="tag tag-yellow">MEDIUM</span></td>
          <td>Job Alert — Remote</td>
          <td>Glassdoor Jobs<br><small>noreply@glassdoor.com</small></td>
          <td>Remote positions — Stanford University mentioned as hiring. (Email trashed — review before deleting)</td>
          <td class="pri-medium">Restore from trash · Review roles · Apply if relevant</td>
        </tr>
        <tr>
          <td><span class="tag tag-yellow">MEDIUM</span></td>
          <td>Networking Group</td>
          <td>HR Networking &amp; Job Search<br><small>Calendar event — today noon</small></td>
          <td>Large HR professional networking group with 170+ members. Open office hours today. Great for peer support, referrals, and leads.</td>
          <td class="pri-high">RSVP &amp; JOIN TODAY at noon</td>
        </tr>
        <tr>
          <td><span class="tag tag-yellow">MEDIUM</span></td>
          <td>Networking Group</td>
          <td>HR Networking &amp; Job Search<br><small>Calendar — Wed Jul 22</small></td>
          <td>Weekly group Zoom — 90 min, same community. RSVP pending.</td>
          <td class="pri-medium">RSVP this week</td>
        </tr>
        <tr>
          <td><span class="tag tag-yellow">MEDIUM</span></td>
          <td>Networking Tea</td>
          <td>Tea with LeiLani · leilani@bethechangehr.com<br><small>T Shop — Today 1 PM</small></td>
          <td>In-person networking with HR professionals. LeiLani (Be The Change HR), Teresa Low Consulting, and others. Already accepted. High-value relationship-building opportunity.</td>
          <td class="pri-high">ATTEND TODAY — 1 PM · 247 Elizabeth St</td>
        </tr>
        <tr>
          <td><span class="tag tag-yellow">MEDIUM</span></td>
          <td>Networking Call — Tue</td>
          <td>Umi · Calendar<br><small>Tue Jul 21, 10–11 AM</small></td>
          <td>Meeting with "Umi" — context unknown. Could be a professional contact or personal. Confirm purpose.</td>
          <td class="pri-medium">Add location/dial-in · Confirm purpose</td>
        </tr>
        <tr>
          <td><span class="tag tag-green">HIGH</span></td>
          <td>Industry Intelligence</td>
          <td>Stanton Chase via LinkedIn<br><small>newsletters-noreply@linkedin.com</small></td>
          <td>"How AI Is Removing the Junior Roles That Build Game Industry Leaders" — strategic insight relevant to HR leadership in tech/media. Know the landscape you're stepping into.</td>
          <td class="pri-low">Read when time permits</td>
        </tr>
        <tr>
          <td><span class="tag tag-gray">LOW</span></td>
          <td>Workshop — Last Call</td>
          <td>Gemma Bonham-Carter<br><small>hello@gemmabonhamcarter.com</small></td>
          <td>"Last call: Kate's workshop — starting in a few hours." Likely a business/creator workshop. Assess relevance to your career pivot goals.</td>
          <td class="pri-low">Decide quickly — time-sensitive today</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 6. FULL EMAIL REVIEW BY CATEGORY -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">📧</span> Full Email Review by Category</div>

  <!-- SECURITY / RISK -->
  <div class="card band-red">
    <span class="tag tag-red">Security / Risk</span>
    <h3>🚨 Security &amp; Phishing — 13 Emails</h3>
    <div class="meta">Auto-Trashed: 8 · Manually flagged: 5 · All unread</div>
    <p><strong>Auto-Trashed (Phishing — No Action Needed Beyond Review):</strong></p>
    <div class="tbl-wrap" style="margin-top:8px;">
      <table>
        <thead><tr><th>Sender</th><th>Subject</th><th>Reason</th></tr></thead>
        <tbody>
          <tr class="phishing-row"><td>Cloud_Storage &lt;ujeuff9k1n@8t2cnym4ls.us&gt;</td><td>⚠️ Action Required: Your Storage Plan Has Expired</td><td>Spoofed storage alert from random domain — credential/payment harvest</td></tr>
          <tr class="phishing-row"><td>Cloud_Storage &lt;ms1b46ehgk@4dca25vz24.us&gt;</td><td>⚠️ Action Required: Your Storage Plan Has Expired (duplicate)</td><td>Identical spoofed cloud storage credential-harvest attempt</td></tr>
          <tr class="phishing-row"><td>𝗣aym𝗲nt_lssu𝗲 &lt;flidargxyjvosr...itcprosolutions.com&gt;</td><td>Act now: Your account will be closed within 48 hours</td><td>Fake payment issue, unicode-obfuscated sender, account closure threat</td></tr>
          <tr class="phishing-row"><td>𝗣aym𝗲nt_Declin𝗲d &lt;lazsupportur@yhhquqjzyjqzrunsjfqeygho.com&gt;</td><td>melissaw212 — Account Blocked, Photos/Videos Removed</td><td>Spoofed payment decline, fake cloud block targeting named user</td></tr>
          <tr class="phishing-row"><td>'🎉Congratulations!' &lt;qzghsupporttsdn@...com&gt;</td><td>Get Your 130 FREE Spins Now On Chumba</td><td>Fake casino promo, obfuscated sender, credential harvest lure</td></tr>
          <tr class="phishing-row"><td>OnlineCasino &lt;gbfhvkcggjz@mwqj...us&gt;</td><td>130 Free Spins Pending in your Account</td><td>Fake casino promo from random domain, payment harvest lure</td></tr>
          <tr class="phishing-row"><td>Cloud.Storage &lt;kiwbwwobzlj@hojn...us&gt;</td><td>[melissaw212] Cloud Account Locked — Wed 15 Jul 2026</td><td>Spoofed cloud lock, named user targeted, billing harvest</td></tr>
          <tr class="phishing-row"><td>United_Healthcare_Promo &lt;contact@afwukza6afwukza6.com&gt;</td><td>melissaw212 Claim Your Free Oral-B Dental Kit</td><td>Spoofed UHC, fake prize survey, personal data harvest</td></tr>
          <tr class="phishing-row"><td>𝗣aym𝗲nt_Declin𝗲d &lt;6fd8ta7r3b@9pun76xyow...us&gt;</td><td>melissaw212 — Account Blocked, Photos/Videos Removed — Wed 15 Jul</td><td>Spoofed payment decline repeat, fake cloud block</td></tr>
          <tr class="phishing-row"><td>'Tractor Supply Co.' &lt;ejxuxskqudjhrm...us&gt;</td><td>Pending Action: Tractor Supply Shopper Verification</td><td>Spoofed Tractor Supply, fake loyalty prize, personal info harvest</td></tr>
        </tbody>
      </table>
    </div>
    <p style="margin-top:8px;"><strong>NOT Auto-Trashed — Manual Action Required:</strong></p>
    <ul style="margin-top:6px; padding-left:20px; font-size:13px;">
      <li><strong>'Dr. Arthur Green'</strong> &lt;brfqwalgkxwuvg...us&gt; — "Add 3.8 inches naturally with this $3 method" — Male enhancement scam. <em>Delete &amp; block immediately.</em></li>
      <li><strong>melissaw212</strong> &lt;lssivqevooz@hxrd...us&gt; — "Use Code: 200GETLUCKY for welcome bonus 30 free spins" — Casino spam spoofing your own address. <em>Delete immediately.</em></li>
      <li><strong>'Vapofil Men Over 40'</strong> &lt;bscsupportfy@cednuuasywqznlwjydmneczu.com&gt; — Men's supplement scam. <em>Delete &amp; block.</em></li>
      <li><strong>melissaw212</strong> &lt;uqdxsupportrg@hkvarsdtdclycssclukkgnld.com&gt; — Cloud account blocked threat (non-auto-trashed duplicate). <em>Delete immediately.</em></li>
    </ul>
    <p style="margin-top:8px;"><strong>Recommended Action:</strong> Your email address (melissaw212) is clearly on a harvested spam list. Consider enabling stricter spam filters and reviewing your Google account security settings.</p>
  </div>

  <!-- JOB SEARCH -->
  <div class="card band-green">
    <span class="tag tag-green">Job Search</span>
    <h3>💼 Job Search &amp; Applications — 3 Emails</h3>
    <div class="meta">Senders: Workday/Horizon Media · Glassdoor (x2, in trash)</div>
    <p><strong>Horizon Media (Workday):</strong> Application confirmed for Director, HR Business Partner. Monitor Workday portal for status updates.<br>
    <strong>Glassdoor (x2 — in Trash):</strong> NY jobs (Landmark, Jetzy) and Remote jobs (Stanford University). Both trashed — restore to review before deletion.<br>
    <strong>Recommended Action:</strong> Restore Glassdoor alerts from trash. Set up saved searches directly on Glassdoor for better control.</p>
  </div>

  <!-- RECRUITERS / NETWORKING -->
  <div class="card band-green">
    <span class="tag tag-green">Recruiters / Networking</span>
    <h3>🤝 Recruiters &amp; Professional Networking — 3 Emails</h3>
    <div class="meta">Senders: Amber Krusza (LinkedIn + calendar) · LinkedIn (NBCUniversal notification)</div>
    <p><strong>Amber Krusza (LinkedIn DM):</strong> Unread message from Formative SP recruiter — highest priority today. <br>
    <strong>Amber Krusza (Calendar Invite):</strong> Fri Jul 17, 3:30 PM — accept after reading her DM. <br>
    <strong>LinkedIn — NBCUniversal Campaign Manager:</strong> A connection posted about a career milestone. Low urgency but worth a quick congratulatory comment for relationship maintenance.<br>
    <strong>Recommended Action:</strong> Respond to Amber today. Engage with NBCUniversal post when convenient.</p>
  </div>

  <!-- CALENDAR / EVENTS -->
  <div class="card band-blue">
    <span class="tag tag-blue">Calendar / Events</span>
    <h3>📅 Calendar &amp; Event Emails — 1 Email</h3>
    <div class="meta">Sender: Gemma Bonham-Carter &lt;hello@gemmabonhamcarter.com&gt;</div>
    <p><strong>Kate's Workshop — Last Call:</strong> "Starting in a few hours" — time-sensitive workshop invite from Gemma Bonham-Carter, a well-known online business coach. Assess if the workshop topic (likely digital business/income) aligns with your current goals. Decide quickly as it starts today.<br>
    <strong>Recommended Action:</strong> Read and decide whether to join today.</p>
  </div>

  <!-- MEDICAL / HEALTH -->
  <div class="card band-blue">
    <span class="tag tag-blue">Medical / Health</span>
    <h3>🩺 Medical &amp; Health — 1 Email (via Calendar)</h3>
    <div class="meta">Reflected in Calendar: Quest Diagnostics · Dr. Yuen</div>
    <p>No standalone medical emails arrived today, but two medical appointments are confirmed on the calendar for tomorrow (Jul 17): Quest Diagnostics at 10:10 AM (Conf# FOUGZX) and Dr. Yuen at 3:00 PM. Also, HomeAgain PetRescuers sent a lost dog alert (Chino, Brooklyn) — see Personal section.<br>
    <strong>Recommended Action:</strong> Review Quest Diagnostics fasting/prep requirements tonight.</p>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="card band-yellow">
    <span class="tag tag-yellow">Financial / Billing</span>
    <h3>💳 Financial &amp; Billing — 2 Emails</h3>
    <div class="meta">Senders: Anthropic PBC · Resend (legal/subprocessors)</div>
    <p><strong>Anthropic Receipt #2791-7051-8194:</strong> Legitimate billing receipt for Claude/AI subscription. Review amount and file for records.<br>
    <strong>Resend Subprocessor Update:</strong> Legal compliance notice — review if using Resend for any business project.<br>
    <strong>Recommended Action:</strong> Open Anthropic email, verify charge, file. Read Resend notice.</p>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="card band-purple">
    <span class="tag tag-purple">Professional Development</span>
    <h3>📚 Professional Development — 3 Emails</h3>
    <div class="meta">Senders: Stanton Chase via LinkedIn · BambooHR (HR Hub) · The People People Group Digest</div>
    <p><strong>Stanton Chase (LinkedIn):</strong> "How AI Is Removing the Junior Roles That Build Game Industry Leaders" — strategic HR insight on AI's workforce impact. Read when convenient.<br>
    <strong>BambooHR [HR Hub]:</strong> "The Future of Work Is Still Human" — monthly HR trends newsletter (in Trash — was it intentionally trashed?). Restore if valuable.<br>
    <strong>The People People Group Digest:</strong> Topics include AI-generated candidate responses and recruiter visibility of resumes (in Trash). Highly relevant to HR work — restore and read.<br>
    <strong>Recommended Action:</strong> Restore TPPG Digest and BambooHR from trash. Read Stanton Chase article.</p>
  </div>

  <!-- PERSONAL -->
  <div class="card band-gray">
    <span class="tag tag-gray">Personal</span>
    <h3>🏠 Personal — 6 Emails</h3>
    <div class="meta">Senders: HomeAgain PetRescuers · Match.com (x3) · OkCupid (x2) · Medium — Dr. Gazala Shaikh</div>
    <p><strong>HomeAgain PetRescuers:</strong> Chino (lost dog) near Van Voorhees Playground, Brooklyn, NY. Ref ID: HAP-1898539. If you're in the area or know someone nearby, consider sharing.<br>
    <strong>Match.com (x3):</strong> Steve likes you (x2 — profile view + mutual like notification) · John likes you. Personal dating app activity — manage on your own time.<br>
    <strong>OkCupid (x2):</strong> "Someone likes you" (Thu + Wed) — personal dating app notifications.<br>
    <strong>Medium — Dr. Gazala Shaikh:</strong> "Not all men" — personal/social commentary article.<br>
    <strong>Recommended Action:</strong> No urgent action. Manage dating apps at your leisure. Note the HomeAgain alert if relevant to your community.</p>
  </div>

  <!-- NEWSLETTERS / SUBSCRIPTIONS -->
  <div class="card band-purple">
    <span class="tag tag-purple">Newsletters / Subscriptions</span>
    <h3>📰 Newsletters &amp; Subscriptions — 10 Emails</h3>
    <div class="meta">See full breakdown in Section 9 below</div>
    <p>AI Report · Average Joe · Medium Daily Digest · TLDR · The Hustle · 1% Better · CoolDeep AI · AI For Leaders · Lisa Rangel · Sue Mysko / Fractional Pipeline · The Daily Skimm<br>
    <strong>Recommended Action:</strong> See Newsletter &amp; Subscriptions section below for individual recommendations.</p>
  </div>

  <!-- PROMOTIONAL / RETAIL -->
  <div class="card band-gray">
    <span class="tag tag-gray">Promotional / Retail</span>
    <h3>🛍️ Promotional &amp; Retail — 6 Emails</h3>
    <div class="meta">Senders: Boomerang · VIVAIA · Kohl's · SHEIN · Old Navy · Boomerang 30% off</div>
    <p>See full breakdown in Promotional/Retail Summary section below.<br>
    <strong>Recommended Action:</strong> Delete or archive unless actively shopping.</p>
  </div>

  <!-- TECH / DEVELOPER -->
  <div class="card band-blue">
    <span class="tag tag-blue">Tech / Developer</span>
    <h3>🔧 Tech / Developer — 2 Emails</h3>
    <div class="meta">Senders: Nokia API Hub (RapidAPI) · Resend (also in Billing)</div>
    <p><strong>Nokia API Hub / JSearch API:</strong> New announcement in RapidAPI Developer Dashboard. If you're actively using JSearch API for job search tooling or projects, review this promptly.<br>
    <strong>Resend Subprocessor Update:</strong> Also categorized under Financial/Billing. Legal compliance notice.<br>
    <strong>Recommended Action:</strong> Log into RapidAPI dashboard and review JSearch announcement.</p>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 7. TRASH REVIEW -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">🗑️</span> Trash Review</div>

  <div class="card band-green" style="margin-bottom:12px;">
    <span class="tag tag-green">RESTORE</span>
    <h3>✅ Restore Immediately — 3 Emails</h3>
    <div class="tbl-wrap" style="margin-top:8px;">
      <table>
        <thead><tr><th>Sender</th><th>Subject</th><th>Why Restore</th></tr></thead>
        <tbody>
          <tr><td>Glassdoor Jobs</td><td>Community Manager – Wellness at Jetzy + 6 more NY jobs</td><td>Active job leads relevant to your search — review before applying</td></tr>
          <tr><td>Glassdoor Jobs</td><td>New jobs in Remote, US (Stanford University hiring)</td><td>Remote HR roles — high relevance to your search</td></tr>
          <tr><td>The People People Group</td><td>TPPG Digest — AI Candidate Responses, Resume Visibility (8 topics)</td><td>Directly relevant HR professional community content — valuable for your work</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card band-yellow" style="margin-bottom:12px;">
    <span class="tag tag-yellow">REVIEW BEFORE DELETING</span>
    <h3>🔍 Review Before Deleting — 4 Emails</h3>
    <div class="tbl-wrap" style="margin-top:8px;">
      <table>
        <thead><tr><th>Sender</th><th>Subject</th><th>Reason to Review</th></tr></thead>
        <tbody>
          <tr><td>BambooHR (Sadie)</td><td>[HR Hub] The Future of Work Is Still Human</td><td>Monthly HR trends newsletter — may have useful content for your field. Check if intentionally trashed.</td></tr>
          <tr><td>AI For Leaders</td><td>Same AI Rejects Job Applications at Different Companies</td><td>Directly relevant to your job search experience — worth reading for advocacy/awareness</td></tr>
          <tr><td>Lisa Rangel (Chameleon Resumes)</td><td>Excellent and unfindable</td><td>Career/resume advice newsletter — possibly trashed by mistake; review if you value resume coaching content</td></tr>
          <tr><td>The Daily Skimm</td><td>If the Montagues and Capulets were burgers</td><td>General news digest — low priority but check if you enjoy this newsletter before permanent deletion</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card band-gray">
    <span class="tag tag-gray">SAFE TO DELETE</span>
    <h3>🗑️ Safe to Delete — 3 Emails</h3>
    <div class="tbl-wrap" style="margin-top:8px;">
      <table>
        <thead><tr><th>Sender</th><th>Subject</th><th>Reason</th></tr></thead>
        <tbody>
          <tr><td>TLDR Newsletter</td><td>Stripe's PayPal bid, Uber vs Waymo, against SDKs</td><td>General tech news digest — time-sensitive content now stale; safe to delete</td></tr>
          <tr><td>Sue Mysko (Substack)</td><td>The $1M–$15M Rule Is Wrong (Fractional Pipeline)</td><td>Fractional executive newsletter — delete if not pursuing fractional work at this time</td></tr>
          <tr><td>Sadie at BambooHR</td><td>[HR Hub] The Future of Work Is Still Human</td><td>(Same as above — delete after review if not relevant)</td></tr>
        </tbody>
      </table>
    </div>
    <div class="note-box" style="margin-top:8px;">📌 Note: 10 additional emails were auto-trashed as confirmed phishing before this briefing was prepared. They are listed in the Security/Risk section. No further action is required on those beyond confirming they remain in trash.</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 8. PROMOTIONAL / RETAIL SUMMARY -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">🛍️</span> Promotional / Retail Summary</div>
  <div class="tbl-wrap">
    <table>
      <thead><tr><th>Brand / Sender</th><th>Count</th><th>Subject / Theme</th><th>Recommendation</th></tr></thead>
      <tbody>
        <tr><td>Boomerang for Gmail<br><small>boomerang@baydin.com</small></td><td>1</td><td>24-Hour Sale — 30% off with code GOAL30</td><td><span class="tag tag-yellow">REVIEW</span> If you use Boomerang, consider the discount. Expires today. Otherwise delete.</td></tr>
        <tr><td>VIVAIA<br><small>hello@edm.vivaia.com</small></td><td>1</td><td>Summer's Strongest Neutral — new shoes/flats</td><td><span class="tag tag-gray">IGNORE / DELETE</span> Retail fashion promo — delete unless actively shopping.</td></tr>
        <tr><td>Kohl's<br><small>Kohls@s.kohls.com</small></td><td>1</td><td>20% off + Kohl's Cash + 70% off clearance</td><td><span class="tag tag-gray">IGNORE / DELETE</span> Standard retail promo. Delete if not shopping.</td></tr>
        <tr><td>SHEIN<br><small>shein@market-us.shein.com</small></td><td>1</td><td>New accessories in stock — bags, shoes, jewelry</td><td><span class="tag tag-gray">IGNORE / DELETE</span> Fast-fashion promo. Delete unless actively browsing.</td></tr>
        <tr><td>Old Navy Clearance<br><small>oldnavy@email.oldnavy.com</small></td><td>1</td><td>Shop clearance by size · Free shipping for Encore Members</td><td><span class="tag tag-gray">IGNORE / DELETE</span> Clearance promo. Low urgency. Delete.</td></tr>
        <tr><td>OkCupid<br><small>bounces@alerts.oknotify3.com</small></td><td>2</td><td>"Someone likes you" (Thu + Wed notifications)</td><td><span class="tag tag-gray">PERSONAL / LOW PRIORITY</span> Manage within the app. Not in inbox. No action needed in email.</td></tr>
      </tbody>
    </table>
  </div>
  <div class="note-box">💡 Consider unsubscribing from retail brands you don't actively shop with to reduce inbox noise during your job search.</div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 9. NEWSLETTERS & SUBSCRIPTIONS -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">📰</span> Newsletters &amp; Subscriptions</div>
  <div class="tbl-wrap">
    <table>
      <thead><tr><th>Sender</th><th>Topic</th><th>In Inbox?</th><th>Recommendation</th></tr></thead>
      <tbody>
        <tr><td>The AI Report<br><small>theaireport@mail.beehiiv.com</small></td><td>OpenAI physical keypad; 71% of enterprise "agents" are still chatbots</td><td>Yes</td><td><span class="tag tag-purple">KEEP</span> Relevant to AI-in-workplace knowledge for HR leadership. Read today.</td></tr>
        <tr><td>The Average Joe<br><small>joe@readthejoe.com</small></td><td>Industrial gold rush — when smartphones aren't smart enough</td><td>Yes</td><td><span class="tag tag-purple">KEEP / REVIEW</span> Business/investing insights. Read when convenient.</td></tr>
