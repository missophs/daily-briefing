<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa — July 19, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .container { max-width: 1100px; margin: 0 auto; padding: 20px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); color: white; padding: 32px 36px; border-radius: 14px; margin-bottom: 24px; box-shadow: 0 8px 32px rgba(0,0,0,0.18); }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header .subtitle { font-size: 14px; color: #a0b4cc; margin-top: 4px; }
  .header .meta { display: flex; gap: 28px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.09); border-radius: 8px; padding: 10px 18px; text-align: center; }
  .header .meta-item .num { font-size: 26px; font-weight: 700; color: #63b3ed; }
  .header .meta-item .lbl { font-size: 11px; color: #a0b4cc; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 2px; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; color: #1a1a2e; margin-bottom: 14px; padding-bottom: 8px; border-bottom: 3px solid #e2e8f0; display: flex; align-items: center; gap: 8px; }
  .section-title .icon { font-size: 19px; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; border-left: 5px solid; box-shadow: 0 2px 8px rgba(0,0,0,0.06); background: #fff; }
  .card.red    { border-left-color: #e53e3e; background: #fff5f5; }
  .card.yellow { border-left-color: #d69e2e; background: #fffff0; }
  .card.blue   { border-left-color: #3182ce; background: #ebf8ff; }
  .card.green  { border-left-color: #38a169; background: #f0fff4; }
  .card.purple { border-left-color: #805ad5; background: #faf5ff; }
  .card.gray   { border-left-color: #718096; background: #f7fafc; }
  .card.orange { border-left-color: #dd6b20; background: #fffaf0; }

  .card-title { font-weight: 700; font-size: 14px; margin-bottom: 4px; }
  .card-source { font-size: 11px; color: #718096; margin-bottom: 6px; }
  .card-body  { font-size: 13px; }
  .card-row   { display: flex; gap: 8px; align-items: flex-start; margin-top: 5px; }
  .card-label { font-size: 11px; font-weight: 700; text-transform: uppercase; color: #555; min-width: 110px; }
  .card-val   { font-size: 13px; color: #2d3748; }

  /* TAGS */
  .tag { display: inline-block; border-radius: 4px; padding: 2px 8px; font-size: 11px; font-weight: 700; margin-right: 4px; text-transform: uppercase; letter-spacing: 0.3px; }
  .tag-red    { background: #fed7d7; color: #c53030; }
  .tag-yellow { background: #fefcbf; color: #975a16; }
  .tag-blue   { background: #bee3f8; color: #2b6cb0; }
  .tag-green  { background: #c6f6d5; color: #276749; }
  .tag-purple { background: #e9d8fd; color: #553c9a; }
  .tag-gray   { background: #e2e8f0; color: #4a5568; }
  .tag-orange { background: #fbd38d; color: #7b341e; }

  /* EXEC SUMMARY */
  .exec-summary { background: #fff; border-radius: 12px; padding: 22px 26px; box-shadow: 0 2px 12px rgba(0,0,0,0.07); margin-bottom: 28px; }
  .exec-summary h2 { font-size: 16px; font-weight: 700; margin-bottom: 14px; color: #1a1a2e; }
  .exec-bullet { display: flex; gap: 12px; align-items: flex-start; padding: 10px 0; border-bottom: 1px solid #edf2f7; }
  .exec-bullet:last-child { border-bottom: none; }
  .exec-bullet .bicon { font-size: 22px; min-width: 32px; }
  .exec-bullet .btxt strong { display: block; font-size: 13px; font-weight: 700; color: #1a1a2e; margin-bottom: 2px; }
  .exec-bullet .btxt span  { font-size: 13px; color: #4a5568; }

  /* TABLE */
  table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); margin-bottom: 16px; }
  th { background: #2d3748; color: #fff; padding: 11px 14px; font-size: 12px; text-align: left; text-transform: uppercase; letter-spacing: 0.4px; }
  td { padding: 10px 14px; font-size: 13px; border-bottom: 1px solid #edf2f7; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #f7fafc; }

  /* CALENDAR */
  .cal-day { background: #fff; border-radius: 10px; margin-bottom: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); overflow: hidden; }
  .cal-day-header { background: #2d3748; color: #fff; padding: 10px 18px; font-weight: 700; font-size: 14px; }
  .cal-day-header.today { background: linear-gradient(90deg, #2b6cb0, #3182ce); }
  .cal-event { padding: 12px 18px; border-bottom: 1px solid #edf2f7; display: grid; grid-template-columns: 140px 1fr; gap: 12px; }
  .cal-event:last-child { border-bottom: none; }
  .cal-time { font-weight: 700; color: #3182ce; font-size: 13px; }
  .cal-details .title { font-weight: 700; font-size: 14px; margin-bottom: 3px; }
  .cal-details .meta-row { font-size: 12px; color: #718096; margin-top: 2px; }
  .cal-details .meta-row a { color: #3182ce; text-decoration: none; }
  .cal-details .meta-row a:hover { text-decoration: underline; }

  /* STATUS BADGES */
  .status { display: inline-block; border-radius: 4px; padding: 2px 8px; font-size: 11px; font-weight: 700; text-transform: uppercase; }
  .status-confirmed  { background: #c6f6d5; color: #276749; }
  .status-needs      { background: #fefcbf; color: #975a16; }
  .status-declined   { background: #fed7d7; color: #c53030; }
  .status-trash      { background: #e2e8f0; color: #4a5568; }

  /* JOB PIPELINE */
  .job-card { background: #fff; border-radius: 10px; padding: 14px 18px; margin-bottom: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-left: 5px solid #38a169; }
  .job-card.medium { border-left-color: #d69e2e; }
  .job-card.low    { border-left-color: #718096; }
  .job-header { display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 8px; }
  .job-title  { font-weight: 700; font-size: 14px; }
  .job-company { font-size: 12px; color: #718096; margin-top: 2px; }
  .job-meta   { font-size: 12px; color: #4a5568; margin-top: 6px; }

  /* DASH GRID */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; margin-bottom: 28px; }
  .dash-tile { background: #fff; border-radius: 10px; padding: 18px 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); text-align: center; }
  .dash-tile .tile-num { font-size: 34px; font-weight: 800; margin-bottom: 4px; }
  .dash-tile .tile-lbl { font-size: 12px; color: #718096; text-transform: uppercase; letter-spacing: 0.4px; }
  .dash-tile.red-t    .tile-num { color: #e53e3e; }
  .dash-tile.yellow-t .tile-num { color: #d69e2e; }
  .dash-tile.blue-t   .tile-num { color: #3182ce; }
  .dash-tile.green-t  .tile-num { color: #38a169; }
  .dash-tile.purple-t .tile-num { color: #805ad5; }
  .dash-tile.gray-t   .tile-num { color: #718096; }

  /* PRIORITY BOX */
  .priority-box { background: linear-gradient(135deg, #1a1a2e, #16213e); color: #fff; border-radius: 12px; padding: 24px 28px; margin-bottom: 28px; }
  .priority-box h2 { font-size: 16px; color: #63b3ed; margin-bottom: 16px; text-transform: uppercase; letter-spacing: 0.5px; }
  .priority-item { display: flex; gap: 14px; align-items: flex-start; margin-bottom: 16px; }
  .priority-item:last-child { margin-bottom: 0; }
  .priority-num { background: #3182ce; color: #fff; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 15px; flex-shrink: 0; }
  .priority-txt strong { display: block; font-size: 14px; font-weight: 700; color: #e2e8f0; }
  .priority-txt span   { font-size: 13px; color: #a0b4cc; }

  /* MISC */
  .group-header { font-size: 13px; font-weight: 700; color: #4a5568; margin-bottom: 8px; margin-top: 14px; text-transform: uppercase; letter-spacing: 0.4px; }
  .pill { display: inline-block; background: #edf2f7; border-radius: 20px; padding: 3px 10px; font-size: 12px; color: #4a5568; margin: 2px; }
  .pill.green { background: #c6f6d5; color: #276749; }
  .pill.red   { background: #fed7d7; color: #c53030; }
  .pill.yellow { background: #fefcbf; color: #975a16; }
  .alert-banner { background: #fff5f5; border: 2px solid #e53e3e; border-radius: 10px; padding: 14px 18px; margin-bottom: 16px; display: flex; gap: 12px; align-items: flex-start; }
  .alert-banner .alert-icon { font-size: 22px; }
  .alert-banner .alert-txt strong { color: #c53030; font-size: 14px; }
  .alert-banner .alert-txt p { font-size: 13px; color: #4a5568; margin-top: 3px; }
  .info-banner { background: #ebf8ff; border: 2px solid #3182ce; border-radius: 10px; padding: 14px 18px; margin-bottom: 16px; display: flex; gap: 12px; align-items: flex-start; }
  .info-banner .alert-icon { font-size: 22px; }
  .info-banner .alert-txt strong { color: #2b6cb0; font-size: 14px; }
  .info-banner .alert-txt p { font-size: 13px; color: #4a5568; margin-top: 3px; }
  .count-badge { display: inline-block; background: #e2e8f0; border-radius: 12px; padding: 1px 9px; font-size: 12px; font-weight: 700; color: #4a5568; margin-left: 6px; }
  .count-badge.red { background: #fed7d7; color: #c53030; }
  .count-badge.green { background: #c6f6d5; color: #276749; }

  .section-desc { font-size: 13px; color: #718096; margin-bottom: 14px; }

  .acct-total { background: #2d3748; color: #fff; font-weight: 700; }
  .acct-total td { color: #fff; border-bottom: none; }

  @media(max-width:680px){
    .cal-event { grid-template-columns: 1fr; }
    .header .meta { gap: 14px; }
    .dash-grid { grid-template-columns: 1fr 1fr; }
  }
</style>
</head>
<body>
<div class="container">

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 1. HEADER -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="header">
  <h1>☀️ Good Morning, Melissa</h1>
  <div class="subtitle">Executive Briefing — Sunday, July 19, 2026 &nbsp;|&nbsp; Prepared by Your Chief of Staff</div>
  <div class="meta">
    <div class="meta-item"><div class="num">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="meta-item"><div class="num">10</div><div class="lbl">Calendar Events</div></div>
    <div class="meta-item"><div class="num">3</div><div class="lbl">Action Required</div></div>
    <div class="meta-item"><div class="num">9</div><div class="lbl">Job Leads</div></div>
    <div class="meta-item"><div class="num">5</div><div class="lbl">Meetings This Week</div></div>
    <div class="meta-item"><div class="num">2</div><div class="lbl">RSVPs Pending</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 2. EXECUTIVE SUMMARY -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="exec-summary">
  <h2>📋 Executive Summary</h2>
  <div class="exec-bullet">
    <div class="bicon">🔴</div>
    <div class="btxt">
      <strong>Biggest Risk: Multiple Phishing &amp; Spam Attacks Targeting You</strong>
      <span>At least 6 phishing/spam emails arrived (2 auto-trashed as confirmed scams). Your email address "melissaw212" is being harvested and actively targeted by fake Lowe's prize scams, explicit spam, and fake gambling sites. Additionally, a NYC Flash Flood Warning for Manhattan/Bronx was issued overnight — check current conditions before going out today.</span>
    </div>
  </div>
  <div class="exec-bullet">
    <div class="bicon">🟢</div>
    <div class="btxt">
      <strong>Biggest Opportunity: Strong Executive HR Job Pipeline + Confidential Recruiter Outreach</strong>
      <span>9 active job leads include VP-level roles at Nanit, K Health, and Deepgram, plus a confidential leadership opportunity from someone claiming to be Egon Zehnder (verify authenticity — sent from a Gmail address). Two HR Networking Zoom sessions this week need RSVP responses.</span>
    </div>
  </div>
  <div class="exec-bullet">
    <div class="bicon">🔵</div>
    <div class="btxt">
      <strong>Biggest Calendar Item: 4 Events This Week Require Attention — 2 RSVPs Still Pending</strong>
      <span>PT session tomorrow (Mon, July 20, 1:45 PM) is confirmed. HR Networking Zoom (Wed, July 22) and Open Office Hours (Thu, July 23) both show "needsAction" — respond today. Bank of America statement is available; review before Verizon FiOS bill due Thursday.</span>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 3. ACTION REQUIRED -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">⚡</span> Action Required</div>

  <div class="alert-banner">
    <div class="alert-icon">⚠️</div>
    <div class="alert-txt">
      <strong>Flash Flood Warning — Manhattan &amp; The Bronx</strong>
      <p>Notify NYC issued a Flash Flood Warning (MN/BX) at 8:32 PM on July 18. Check current NWS conditions before leaving home today. Allow extra travel time if commuting.</p>
    </div>
  </div>

  <div class="card yellow">
    <div class="card-title">⚠️ RSVP Required — HR Networking &amp; Job Search Group Zoom</div>
    <div class="card-source">Source: Google Calendar · Status: needsAction</div>
    <div class="card-row"><span class="card-label">Why It Matters:</span><span class="card-val">This is a structured HR professional networking session with 170+ attendees. You are in the group and need to confirm or decline. Missing it without a response is unprofessional in this community.</span></div>
    <div class="card-row"><span class="card-label">Next Step:</span><span class="card-val">RSVP Accept or Decline in Google Calendar today. Zoom link: us06web.zoom.us/j/81954171722</span></div>
    <div class="card-row"><span class="card-label">Due:</span><span class="card-val">Wednesday, July 22, 12:00 PM – 1:30 PM EDT</span></div>
  </div>

  <div class="card yellow">
    <div class="card-title">⚠️ RSVP Required — HR Networking Open Office Hours Zoom</div>
    <div class="card-source">Source: Google Calendar · Status: needsAction</div>
    <div class="card-row"><span class="card-label">Why It Matters:</span><span class="card-val">Same HR networking group, open office hours session. Also awaiting your RSVP. Note: AI notetaking tools are not permitted in this session.</span></div>
    <div class="card-row"><span class="card-label">Next Step:</span><span class="card-val">RSVP Accept or Decline. Zoom link: us06web.zoom.us/j/85945371140</span></div>
    <div class="card-row"><span class="card-label">Due:</span><span class="card-val">Thursday, July 23, 12:00 PM – 1:00 PM EDT</span></div>
  </div>

  <div class="card yellow">
    <div class="card-title">🏦 Bank of America: Statement Ready — Money Market Savings #7549</div>
    <div class="card-source">From: Bank of America &lt;onlinebanking@ealerts.bankofamerica.com&gt; · Sat, July 18</div>
    <div class="card-row"><span class="card-label">Why It Matters:</span><span class="card-val">Your monthly Money Market Savings statement is available. With Verizon FiOS bill due Thursday (July 23), it's a good time to review your balance and cash flow.</span></div>
    <div class="card-row"><span class="card-label">Next Step:</span><span class="card-val">Log in to ealerts.bankofamerica.com to view your statement. Ask Erica: "View my statement."</span></div>
    <div class="card-row"><span class="card-label">Due:</span><span class="card-val">Review before Thursday, July 23 (Verizon FiOS bill due)</span></div>
  </div>

  <div class="card red">
    <div class="card-title">🔍 Verify Recruiter Legitimacy — Egon Zehnder Outreach (Gmail Address)</div>
    <div class="card-source">From: Alivia Simon &lt;egon.zehnder.hr.recruitingboards@gmail.com&gt; · Sun, July 19</div>
    <div class="card-row"><span class="card-label">Why It Matters:</span><span class="card-val">This email claims to be from a Senior Associate at Egon Zehnder regarding a confidential People Strategy &amp; Transformation leadership role. However, Egon Zehnder is a legitimate executive search firm and would NOT use a Gmail address for outreach. This may be a spoofed recruiter pitch or phishing attempt.</span></div>
    <div class="card-row"><span class="card-label">Next Step:</span><span class="card-val">Do NOT click any links. Independently verify: go directly to egonzehnder.com, search for "Alivia Simon," and call their main office to confirm. If legitimate, respond through verified contact only.</span></div>
    <div class="card-row"><span class="card-label">Due:</span><span class="card-val">Verify before responding — within 48 hours if legitimate</span></div>
  </div>

  <div class="card yellow">
    <div class="card-title">📦 USPS Package: Delivery Tomorrow, July 20 by 9:00 PM</div>
    <div class="card-source">From: USPS Tracking &lt;auto-reply@tracking.usps.com&gt; · Sun, July 19 (in Trash)</div>
    <div class="card-row"><span class="card-label">Why It Matters:</span><span class="card-val">Tracking #9400150106151312010127. Package expected Monday, July 20 by 9:00 PM. Given the Flash Flood Warning, be aware of potential delivery delays. Restore this email from Trash.</span></div>
    <div class="card-row"><span class="card-label">Next Step:</span><span class="card-val">Restore from Trash. Track at usps.com. Be available or arrange for package security Monday.</span></div>
    <div class="card-row"><span class="card-label">Due:</span><span class="card-val">Monday, July 20 by 9:00 PM</span></div>
  </div>

  <div class="card yellow">
    <div class="card-title">💳 Verizon FiOS Bill Due — Thursday, July 23</div>
    <div class="card-source">Source: Google Calendar</div>
    <div class="card-row"><span class="card-label">Why It Matters:</span><span class="card-val">Verizon FiOS bill is due this Thursday. Confirm auto-pay is set up or make manual payment to avoid service interruption.</span></div>
    <div class="card-row"><span class="card-label">Next Step:</span><span class="card-val">Log in to verizon.com or check auto-pay status before Thursday.</span></div>
    <div class="card-row"><span class="card-label">Due:</span><span class="card-val">Thursday, July 23, 2026</span></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 4. FULL 7-DAY CALENDAR -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">📅</span> Full 7-Day Calendar (July 19–25, 2026)</div>

  <!-- SUNDAY July 19 -->
  <div class="cal-day">
    <div class="cal-day-header today">Sunday, July 19, 2026 — TODAY</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="title">No calendar events scheduled</div>
        <div class="meta-row">⚠️ <strong>Flash Flood Warning active</strong> for Manhattan &amp; The Bronx — check NWS before leaving home. RSVP to both Zoom sessions this week.</div>
      </div>
    </div>
  </div>

  <!-- MONDAY July 20 -->
  <div class="cal-day">
    <div class="cal-day-header">Monday, July 20, 2026</div>
    <div class="cal-event">
      <div class="cal-time">1:45 PM – 2:45 PM</div>
      <div class="cal-details">
        <div class="title">🏋️ PT (Physical Therapy / Personal Training)</div>
        <div class="meta-row"><span class="status status-confirmed">✔ Confirmed</span></div>
        <div class="meta-row">📍 Location: Not specified</div>
        <div class="meta-row">📝 Prep: Wear workout attire. Note: This event appears twice in calendar data (duplicate entry) — only one session is scheduled.</div>
        <div class="meta-row">📦 Also: USPS package delivery expected by 9:00 PM tonight — Tracking #9400150106151312010127</div>
      </div>
    </div>
  </div>

  <!-- TUESDAY July 21 -->
  <div class="cal-day">
    <div class="cal-day-header">Tuesday, July 21, 2026</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="title">🎂 Eric Dordick's Birthday</div>
        <div class="meta-row"><span class="status status-confirmed">✔ Confirmed</span></div>
        <div class="meta-row">📝 Send a message or card if appropriate.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-time">10:00 AM – 11:00 AM</div>
      <div class="cal-details">
        <div class="title">📋 Umi</div>
        <div class="meta-row"><span class="status status-confirmed">✔ Confirmed</span></div>
        <div class="meta-row">📍 Location: Not specified</div>
        <div class="meta-row">📝 Prep: Unknown context — verify what "Umi" refers to (appointment, call, meeting?). Confirm details if needed.</div>
      </div>
    </div>
  </div>

  <!-- WEDNESDAY July 22 -->
  <div class="cal-day">
    <div class="cal-day-header">Wednesday, July 22, 2026</div>
    <div class="cal-event">
      <div class="cal-time">12:00 PM – 1:30 PM</div>
      <div class="cal-details">
        <div class="title">🤝 HR Networking &amp; Job Search Group — Zoom Session 2</div>
        <div class="meta-row"><span class="status status-needs">⚠️ RSVP Needed</span> &nbsp; Also appears as "Network" (confirmed duplicate on same day/time)</div>
        <div class="meta-row">📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Join Zoom Meeting</a></div>
        <div class="meta-row">👥 170+ attendees — large HR professional networking group</div>
        <div class="meta-row">📝 Prep: Review team guidelines (link in description). Prepare a brief intro/update on your job search status. RSVP today.</div>
        <div class="meta-row">⚠️ Conflict: Duplicate "Network" event on same time — these appear to be the same meeting. Confirm and remove duplicate.</div>
      </div>
    </div>
  </div>

  <!-- THURSDAY July 23 -->
  <div class="cal-day">
    <div class="cal-day-header">Thursday, July 23, 2026</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="title">🎂 Amy Fink's Birthday</div>
        <div class="meta-row"><span class="status status-confirmed">✔ Confirmed</span></div>
        <div class="meta-row">📝 Send a birthday message if appropriate.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="title">💳 Verizon FiOS Bill Due</div>
        <div class="meta-row"><span class="status status-confirmed">✔ On Calendar</span></div>
        <div class="meta-row">📝 Confirm auto-pay or pay manually at verizon.com.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-time">9:00 AM – 10:30 AM</div>
      <div class="cal-details">
        <div class="title">🏛️ Executive Roundtable (John Madigan / Zoom)</div>
        <div class="meta-row"><span class="status status-declined">✖ Declined</span></div>
        <div class="meta-row">📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> · Meeting ID: 207 786 667 · Password: 205454</div>
        <div class="meta-row">📝 You have declined this event. No action needed unless you wish to reconsider.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-time">12:00 PM – 1:00 PM</div>
      <div class="cal-details">
        <div class="title">🤝 HR Networking &amp; Job Search: Open Office Hours — Zoom Session 2</div>
        <div class="meta-row"><span class="status status-needs">⚠️ RSVP Needed</span></div>
        <div class="meta-row">📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Join Zoom Meeting</a></div>
        <div class="meta-row">👥 170+ attendees · ⚠️ AI notetaking tools NOT permitted</div>
        <div class="meta-row">📝 Open discussion — casual networking. Great for job search momentum. RSVP today. Do not use Otter.ai or similar tools during this session.</div>
      </div>
    </div>
  </div>

  <!-- FRIDAY July 24 -->
  <div class="cal-day">
    <div class="cal-day-header">Friday, July 24, 2026</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="title">No events scheduled</div>
        <div class="meta-row">Clear day — good opportunity for job applications, follow-ups, or deep work.</div>
      </div>
    </div>
  </div>

  <!-- SATURDAY July 25 -->
  <div class="cal-day">
    <div class="cal-day-header">Saturday, July 25, 2026</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="title">No events scheduled</div>
        <div class="meta-row">Clear weekend day.</div>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 5. JOB SEARCH & INTERVIEW PIPELINE -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">💼</span> Job Search &amp; Interview Pipeline</div>
  <div class="section-desc">9 active leads identified from LinkedIn, Glassdoor, and recruiter outreach. No interviews confirmed. Two networking sessions this week. Recruiter outreach requires verification.</div>

  <div class="group-header">🟢 High Fit — VP / Senior Leadership Roles</div>

  <div class="job-card">
    <div class="job-header">
      <div>
        <div class="job-title">VP, People — Nanit</div>
        <div class="job-company">Source: LinkedIn Job Alerts (2 alerts — July 16 posting) · Received twice, 5:05 AM &amp; 7:05 AM</div>
      </div>
      <span class="tag tag-green">HIGH FIT</span>
    </div>
    <div class="job-meta">📅 Posted: 7/16/2026 &nbsp;|&nbsp; 📧 Alerted twice — strong signal this is active &nbsp;|&nbsp; 🍼 Nanit is a leading baby monitor/parenting tech brand</div>
    <div class="job-meta">➡️ <strong>Action:</strong> Apply immediately if not already done. This role aligns with your VP People background.</div>
  </div>

  <div class="job-card">
    <div class="job-header">
      <div>
        <div class="job-title">VP of People (HR) — K Health</div>
        <div class="job-company">Source: LinkedIn Job Alerts · Posted 7/17/2026 (in Trash — restore)</div>
      </div>
      <span class="tag tag-green">HIGH FIT</span>
    </div>
    <div class="job-meta">📅 Posted: 7/17/2026 &nbsp;|&nbsp; 🏥 K Health is a digital health/AI primary care company &nbsp;|&nbsp; Fast-growing, VC-backed</div>
    <div class="job-meta">➡️ <strong>Action:</strong> Restore email from Trash. Apply immediately — recent posting, strong fit.</div>
  </div>

  <div class="job-card">
    <div class="job-header">
      <div>
        <div class="job-title">Vice President, Human Resources — Intelex Technologies ULC</div>
        <div class="job-company">Source: LinkedIn Jobs ("similar jobs") · Received Sunday, July 19</div>
      </div>
      <span class="tag tag-green">HIGH FIT</span>
    </div>
    <div class="job-meta">📅 Today's alert &nbsp;|&nbsp; 🏭 Intelex: EHS &amp; quality management software</div>
    <div class="job-meta">➡️ <strong>Action:</strong> Review similar jobs listed in this alert. Apply to any VP HR-level roles that match.</div>
  </div>

  <div class="group-header">🟡 Medium Fit — Senior/Mid-Level HR Roles</div>

  <div class="job-card medium">
    <div class="job-header">
      <div>
        <div class="job-title">Senior People Partner — Deepgram</div>
        <div class="job-company">Source: LinkedIn Job Alerts · Posted 7/16/2026</div>
      </div>
      <span class="tag tag-yellow">MEDIUM FIT</span>
    </div>
    <div class="job-meta">📅 Posted: 7/16/2026 &nbsp;|&nbsp; 🎙️ Deepgram: AI voice/speech recognition startup &nbsp;|&nbsp; Likely below VP level but strong tech company exposure</div>
    <div class="job-meta">➡️ <strong>Action:</strong> Review job description — may be worth applying if the scope is senior enough.</div>
  </div>

  <div class="job-card medium">
    <div class="job-header">
      <div>
        <div class="job-title">People Partner at Fluidstack — Up to $262K/year</div>
        <div class="job-company">Source: LinkedIn Job Alerts · Posted 7/17/2026 (in Trash)</div>
      </div>
      <span class="tag tag-yellow">MEDIUM FIT</span>
    </div>
    <div class="job-meta">📅 Posted: 7/17/2026 &nbsp;|&nbsp; 💰 Comp: up to $262K — potentially worth reviewing &nbsp;|&nbsp; ☁️ Fluidstack: GPU cloud computing</div>
    <div class="job-meta">➡️ <strong>Action:</strong> Restore from Trash. Review scope — high comp may indicate senior-level even if title is "Partner."</div>
  </div>

  <div class="job-card medium">
    <div class="job-header">
      <div>
        <div class="job-title">Senior Manager, Global Human Resources — Omada Search</div>
        <div class="job-company">Source: LinkedIn Job Alerts · Posted 7/17/2026</div>
      </div>
      <span class="tag tag-yellow">MEDIUM FIT</span>
    </div>
    <div class="job-meta">📅 Posted: 7/17/2026 &nbsp;|&nbsp; 🔍 Omada Search is a recruiting firm — this could be a client placement role</div>
    <div class="job-meta">➡️ <strong>Action:</strong> Review whether this is a direct placement or internal role. Apply if scope is appropriate.</div>
  </div>

  <div class="job-card medium">
    <div class="job-header">
      <div>
        <div class="job-title">People Partner — Same Page HR</div>
        <div class="job-company">Source: LinkedIn Job Alerts · Posted 7/16/2026 (in Trash)</div>
      </div>
      <span class="tag tag-yellow">MEDIUM FIT</span>
    </div>
    <div class="job-meta">📅 Posted: 7/16/2026 &nbsp;|&nbsp; 🏢 HR consultancy role — may be fractional or contract</div>
    <div class="job-meta">➡️ <strong>Action:</strong> Restore from Trash. Review if contract/fractional work aligns with your goals.</div>
  </div>

  <div class="group-header">⚪ Low Fit / Needs Review</div>

  <div class="job-card low">
    <div class="job-header">
      <div>
        <div class="job-title">HR &amp; Payroll Manager — SeatScope · Community Manager — Fairstead · HR Manager — Materion (+10 more)</div>
        <div class="job-company">Source: Glassdoor Jobs · Multiple alerts (2 read, 1 unread)</div>
      </div>
      <span class="tag tag-gray">LOW FIT</span>
    </div>
    <div class="job-meta">🗂️ Mix of Manager-level and non-HR roles (Community Manager) — likely below target level</div>
    <div class="job-meta">➡️ <strong>Action:</strong> Scan titles quickly. Adjust Glassdoor job alert settings to filter for VP/Senior Director level only.</div>
  </div>

  <div class="group-header">🔍 Recruiter Outreach — Requires Verification</div>

  <div class="card red" style="margin-bottom:10px;">
    <div class="card-title">⚠️ Confidential Leadership Opportunity — Alivia Simon (Claims: Egon Zehnder)</div>
    <div class="card-source">From: egon.zehnder.hr.recruitingboards@gmail.com · Sun, July 19, 3:22 AM BST</div>
    <div class="card-body">Claims to be a Senior Associate at Egon Zehnder reaching out about a People Strategy &amp; Transformation role. <strong>Red flag: Egon Zehnder does not recruit from Gmail accounts.</strong> Do not respond until you independently verify via egonzehnder.com. Could be legitimate (a contractor using personal email) or a data harvesting scam.</div>
  </div>

  <div class="group-header">🤝 Networking This Week</div>
  <div class="card blue" style="margin-bottom:10px;">
    <div class="card-body">
      <strong>Wed July 22, 12:00–1:30 PM</strong> — HR Networking &amp; Job Search Group Zoom (170+ attendees) — <span class="tag tag-yellow">RSVP NEEDED</span><br>
      <strong>Thu July 23, 12:00–1:00 PM</strong> — HR Open Office Hours Zoom (170+ attendees) — <span class="tag tag-yellow">RSVP NEEDED</span><br>
      Both sessions: Prepare a concise job search status update. Bring 2–3 targeted questions or asks.
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 6. FULL EMAIL REVIEW BY CATEGORY -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">📬</span> Full Email Review by Category</div>

  <!-- SECURITY / RISK -->
  <div class="card red">
    <div class="card-title">🔴 Security / Risk <span class="count-badge red">8 emails</span></div>
    <div class="card-source">Phishing, spam, scams, suspicious senders</div>
    <table style="margin-top:10px;">
      <tr><th>Sender</th><th>Subject</th><th>Status</th><th>Risk Level</th></tr>
      <tr><td>"Lowe's" (fake domain: rmkf6j...)</td><td>We have been trying to reach you – melissaw212</td><td><span class="tag tag-red">Auto-Trashed</span></td><td>Phishing — Fake prize scam</td></tr>
      <tr><td>"Lowe's" (fake domain: spanisation.com)</td><td>We have been trying to reach you – melissaw212</td><td><span class="tag tag-red">Auto-Trashed</span></td><td>Phishing — Identical scam, spoofed domain</td></tr>
      <tr><td>"The Pleasure Leak 🔞" (random .us domain)</td><td>melissaw212 💥 You're Destroying Your Erection Every Night</td><td><span class="tag tag-red">Spam/Explicit</span></td><td>Explicit spam — harvested your username</td></tr>
      <tr><td>"FUCK-BUDDY SECRET" (random .us domain)</td><td>🍌The Special EXERCISE that Gives Porn Stars their Stamina</td><td><span class="tag tag-red">Spam/Explicit</span></td><td>Explicit spam — dangerous sender</td></tr>
      <tr><td>"Congratulations🎉" (random .us domain)</td><td>200 Free Spins 💰 Pending in your Account</td><td><span class="tag tag-red">Scam</span></td><td>Gambling scam</td></tr>
      <tr><td>"Vapofil.Male.Enhancement" (random .us domain)</td><td>Most men are lying about their size are you one of them</td><td><span class="tag tag-red">Spam</span></td><td>Predatory spam</td></tr>
      <tr><td>HorseWood Alert (random .us domain)</td><td>Boost performance with this simple 12-day trick</td><td><span class="tag tag-red">Spam</span></td><td>Predatory spam</td></tr>
      <tr><td>Alivia Simon (egon.zehnder...@gmail.com)</td><td>Confidential Leadership Opportunity | People Strategy</td><td><span class="tag tag-yellow">Verify First</span></td><td>Suspicious — Gmail used for executive firm name</td></tr>
    </table>
    <div class="card-body" style="margin-top:10px;">⚠️ <strong>Your username "melissaw212" is being actively harvested</strong> by spam networks. Consider strengthening spam filters. All 2 auto-trashed emails have been removed by your system. The remaining 5 pure spam emails should be deleted and the senders blocked immediately. The Egon Zehnder email requires independent verification before any response.</div>
  </div>

  <!-- JOB SEARCH -->
  <div class="card green">
    <div class="card-title">🟢 Job Search <span class="count-badge green">9 emails</span></div>
    <div class="card-source">LinkedIn Job Alerts, Glassdoor — active leads</div>
    <table style="margin-top:10px;">
      <tr><th>Sender</th><th>Role / Subject</th><th>Location</th><th>Status</th></tr>
      <tr><td>LinkedIn Job Alerts</td><td>VP, People at Nanit (×2 alerts)</td><td>—</td><td><span class="tag tag-green">Apply Now</span></td></tr>
      <tr><td>LinkedIn Job Alerts</td><td>VP of People (HR) at K Health</td><td>—</td><td><span class="tag tag-green">Apply Now</span> (Restore from Trash)</td></tr>
      <tr><td>LinkedIn (jobs-noreply)</td><td>New jobs similar to VP HR at Intelex Technologies ULC</td><td>—</td><td><span class="tag tag-green">Review</span></td></tr>
      <tr><td>LinkedIn Job Alerts</td><td>Senior People Partner at Deepgram</td><td>—</td><td><span class="tag tag-yellow">Review</span></td></tr>
      <tr><td>LinkedIn Job Alerts</td><td>People Partner at Fluidstack: up to $262K/year</td><td>—</td><td><span class="tag tag-yellow">Review</span> (Restore from Trash)</td></tr>
      <tr><td>LinkedIn Job Alerts</td><td>Senior Manager, Global Human Resources at Omada Search</td><td>—</td><td><span class="tag tag-yellow">Review</span></td></tr>
      <tr><td>LinkedIn Job Alerts</td><td>People Partner at Same Page HR</td><td>—</td><td><span class="tag tag-yellow">Review</span> (Restore from Trash)</td></tr>
      <tr><td>Glassdoor Jobs</td><td>HR &amp; Payroll Manager at SeatScope + 2 more (Remote)</td><td>Remote, US</td><td><span class="tag tag-gray">Scan &amp; Filter</span></td></tr>
      <tr><td>Glassdoor Jobs</td><td>Community Manager at Fairstead + 5 more (NY)</td><td>New York, NY</td><td><span class="tag tag-gray">Scan &amp; Filter</span></td></tr>
    </table>
    <div class="card-body" style="margin-top:8px;">Note: Glassdoor also sent HR Manager at Materion + 9 more jobs (counted separately in Glassdoor grouping above).</div>
  </div>

  <!-- RECRUITERS / NETWORKING -->
  <div class="card green" style="border-left-color:#2f855a;">
    <div class="card-title">🤝 Recruiters / Networking <span class="count-badge green">1 email</span></div>
    <div class="card-source">Executive search / recruiter outreach</div>
    <div class="card-body">
      <strong>Alivia Simon</strong> (egon.zehnder.hr.recruitingboards@gmail.com) — Confidential Leadership Opportunity | People Strategy &amp; Transformation.<br>
      ⚠️ Treat as suspicious until independently verified. Do not click links. Verify via egonzehnder.com directly.
    </div>
  </div>

  <!-- CALENDAR / EVENTS -->
  <div class="card blue">
    <div class="card-title">📅 Calendar / Events <span class="count-badge" style="background:#bee3f8;color:#2b6cb0;">0 emails</span></div>
    <div class="card-body">No dedicated calendar-related emails in inbox. All scheduling data sourced from Google Calendar events directly.</div>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="card yellow">
    <div class="card-title">💳 Financial / Billing <span class="count-badge yellow">2 emails</span></div>
    <div class="card-source">Bank of America, Equifax</div>
    <table style="margin-top:10px;">
      <tr><th>Sender</th><th>Subject</th><th>Action</th></tr>
      <tr><td>Bank of America</td><td>Your statement is available — Money Market Savings #7549</td><td><span class="tag tag-yellow">Review statement</span></td></tr>
      <tr><td>Equifax</td><td>Where will your credit report take you? (in Trash)</td><td><span class="tag tag-gray">Delete — marketing</span></td></tr>
    </table>
  </div>

  <!-- WEATHER / LOCAL ALERTS -->
  <div class="card red" style="border-left-color:#c05621;">
    <div class="card-title">🌩️ Local / Government Alerts <span class="count-badge red">3 emails</span></div>
    <div class="card-source">Notify NYC, Nextdoor (Yorkville)</div>
    <table style="margin-top:10px;">
      <tr><th>Sender</th><th>Subject</th><th>Status</th></tr>
      <tr><td>Notify NYC</td><td>Flash Flood Warning (Manhattan/Bronx) — issued 8:32 PM July 18</td><td><span class="tag tag-red">Urgent — Check now</span> (in Trash)</td></tr>
      <tr><td>Yorkville (E83st-2ndAve) Trending Posts</td><td>What's a New York memory you'll never forget?</td><td><span class="tag tag-gray">Low priority</span></td></tr>
      <tr><td>Trending on Nextdoor</td><td>Our Mayor, City Council, DOT, Parks Dept. should all be...</td><td><span class="tag tag-gray">Low priority</span> (in Trash)</td></tr>
    </table>
    <div class="card-body" style="margin-top:8px;">⚠️ The Flash Flood Warning email was auto-moved to Trash but is <strong>important</strong> — restore and check current NWS status before going outside today.</div>
  </div>

  <!-- PERSONAL -->
  <div class="card purple" style="border-left-color:#d53f8c;">
    <div class="card-title">👤 Personal <span class="count-badge" style="background:#fed7e2;color:#97266d;">3 emails</span></div>
    <div class="card-source">Match.com, self-sent draft</div>
    <table style="margin-top:10px;">
      <tr><th>Sender</th><th>Subject</th><th>Recommendation</th></tr>
      <tr><td>Match</td><td>You've had a profile view from Chris (62, Old Mystic CT)</td><td>Review if interested</td></tr>
      <tr><td>Match</td><td>John likes you. See if it's mutual.</td><td>Review if interested</td></tr>
      <tr><td>melissa (self)</td><td>(blank subject/body — self-sent draft?)</td><td>Likely a draft or note to self — check sent folder</td></tr>
    </table>
    <div class="card-body" style="margin-top:8px;">Note: Match notifications for Steve (Trash) and Tom (Trash) are covered in Trash Review.</div>
  </div>

  <!-- MEDICAL / HEALTH -->
  <div class="card orange">
    <div class="card-title">🏥 Medical / Health <span class="count-badge" style="background:#fbd38d;color:#7b341e;">1 email</span></div>
    <div class="card-source">Ozempic by DirectMeds (suspicious sender)</div>
    <div class="card-body">
      <strong>"Ozempic by DirectMeds"</strong> (xfylufnezvpfno...@rhvzz6.vtkef6.s6y2sz.us) — "What If You Could Lose Weight Effortlessly?" — GLP-1 medication advertisement from a random .us domain. <strong>This is likely a spam/scam pharma offer.</strong> Do not purchase from this sender. Delete and block.
    </div>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="card purple">
    <div class="card-title">📚 Professional Development <span class="count-badge" style="background:#e9d8fd;color:#553c9a;">2 emails</span></div>
    <div class="card-source">Medium, CoolDeep AI</div>
    <table style="margin-top:10px;">
      <tr><th>Sender</th><th>Subject</th><th>Recommendation</th></tr>
      <tr><td>Medium Daily Digest</td><td>Beyond RAG: How Google's Open Knowledge Format (OKF) is Replacing the Vector Database</td><td>Read if AI/tech strategy relevant</td></tr>
      <tr><td>CoolDeep AI (Beehiiv newsletter)</td><td>I really wasted a year learning AI wrong — The 3 levels (in Trash)</td><td>Worth reading — restore if interested in AI literacy</td></tr>
    </table>
  </div>

  <!-- NEWSLETTERS -->
  <div class="card purple" style="border-left-color:#6b46c1;">
    <div class="card-title">📰 Newsletters / Subscriptions <span class="count-badge" style="background:#e9d8fd;color:#553c9a;">5 emails</span></div>
    <div class="card-source">Medium, Insider Monkey, NBC, SPCA International, Vaishali Lambe/Medium</div>
    <table style="margin-top:10px;">
      <tr><th>Sender</th><th>Subject</th><th>Recommendation</th></tr>
      <tr><td>Medium Daily Digest</td><td>Beyond RAG: Google's Open Knowledge Format (OKF)</td><td>Keep — relevant AI content</td></tr>
      <tr><td>Vaishali Lambe / Medium</td><td>AI Chatbots as Social Actors: Builder's Guide to Interaction Design</td><td>Keep — professional development</td></tr>
      <tr><td>Insider Monkey</td><td>Daily Newsletter July 18 — Undervalued AI Stocks (in Trash)</td><td>Review — finance/investing content</td></tr>
      <tr><td>NBC</td><td>New This Month on NBC — The Odyssey, AGT and more</td><td>Low priority — skim or delete</td></tr>
      <tr><td>SPCA International</td><td>New Clinic, Special Rescue in Spain, Event in NYC (in Trash)</td><td>Keep if interested in animal causes</td></tr>
    </table>
  </div>

  <!-- PROMOTIONAL / RETAIL -->
  <div class="card gray">
    <div class="card-title">🛍️ Promotional / Retail <span class="count-badge">15 emails</span></div>
    <div class="card-source">VIVAIA, Quince, Shopify, Old Navy, Kohl's, SHEIN (×2), Macy's (Trash), Laura Geller (×2), Temu</div>
    <div class="card-body">See dedicated Promotional / Retail Summary section below for full breakdown.</div>
  </div>

  <!-- TRASH REVIEW -->
  <div class="card gray" style="border-left-color:#4a5568;">
    <div class="card-title">🗑️ Trash Review <span class="count-badge">14 emails in Trash</span></div>
    <div class="card-body">See dedicated Trash Review section below for full breakdown.</div>
  </div>

  <!-- SAFE TO DELETE / IGNORE -->
  <div class="card gray">
    <div class="card-title">❌ Safe to Delete / Ignore <span class="count-badge">Included in categories above</span></div>
    <div class="card-body">All spam, explicit content, fake prize scams (Lowe's ×2 auto-trashed), fake gambling, predatory ads (Ozempic, HorseWood, male enhancement) — block senders and delete. See Security section above for full list.</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 7. TRASH REVIEW -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">🗑️</span> Trash Review — 14 Emails in Trash</div>
  <div class="section-desc">The following emails were found in Gmail Trash. Review before permanent deletion.</div>

  <div class="group-header" style="color:#c53030;">🔴 Restore Immediately</div>
  <table>
    <tr><th>Sender</th><th>Subject</th><th>Reason to Restore</th></tr>
    <tr>
      <td>USPS Tracking</td>
      <td>USPS® Expected Delivery Monday, July 20, 2026 by 9:00pm · #9400150106151312010127</td>
      <td>Package arriving TOMORROW — critical delivery info. Restore and track.</td>
    </tr>
    <tr>
      <td>Notify NYC</td>
      <td>Flash Flood Warning (Manhattan/Bronx) — issued 8:32 PM July 18</td>
      <td>Active government weather alert — affects your safety today. Check current status.</td>
    </tr>
  </table>

  <div class="group-header" style="color:#d69e2e; margin-top:16px
