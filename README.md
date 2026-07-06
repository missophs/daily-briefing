<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa | Monday, July 6, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px 28px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 15px; color: #a8b8d8; margin-top: 6px; }
  .header-meta { display: flex; gap: 28px; margin-top: 18px; flex-wrap: wrap; }
  .header-meta .meta-pill { background: rgba(255,255,255,0.1); border-radius: 20px; padding: 6px 16px; font-size: 13px; color: #e0e8f5; }

  /* SECTION TITLES */
  .section-title { font-size: 17px; font-weight: 700; margin: 28px 0 12px; padding-left: 12px; border-left: 4px solid #0f3460; color: #1a1a2e; letter-spacing: 0.3px; }

  /* EXECUTIVE SUMMARY */
  .exec-summary { background: #fff; border-radius: 12px; padding: 20px 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); margin-bottom: 20px; }
  .exec-summary ul { list-style: none; padding: 0; }
  .exec-summary ul li { padding: 9px 0 9px 20px; border-bottom: 1px solid #f0f2f5; font-size: 14px; line-height: 1.5; position: relative; }
  .exec-summary ul li:last-child { border-bottom: none; }
  .exec-summary ul li::before { content: '▶'; position: absolute; left: 0; font-size: 10px; top: 12px; color: #0f3460; }
  .badge-risk::before { color: #c0392b !important; }
  .badge-opp::before { color: #27ae60 !important; }
  .badge-cal::before { color: #2980b9 !important; }

  /* CARDS */
  .card-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 14px; margin-bottom: 20px; }
  .card { border-radius: 11px; padding: 16px 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .card-red { background: #fff5f5; border-left: 5px solid #c0392b; }
  .card-yellow { background: #fffdf0; border-left: 5px solid #f39c12; }
  .card-blue { background: #f0f7ff; border-left: 5px solid #2980b9; }
  .card-green { background: #f0fff4; border-left: 5px solid #27ae60; }
  .card-purple { background: #f8f0ff; border-left: 5px solid #8e44ad; }
  .card-gray { background: #f8f8f8; border-left: 5px solid #95a5a6; }
  .card-label { font-size: 10px; font-weight: 700; letter-spacing: 1.2px; text-transform: uppercase; margin-bottom: 6px; }
  .label-red { color: #c0392b; }
  .label-yellow { color: #d68910; }
  .label-blue { color: #2980b9; }
  .label-green { color: #27ae60; }
  .label-purple { color: #8e44ad; }
  .label-gray { color: #7f8c8d; }
  .card h3 { font-size: 14px; font-weight: 700; margin-bottom: 6px; }
  .card .card-meta { font-size: 12px; color: #555; margin-bottom: 4px; }
  .card .card-body { font-size: 13px; color: #333; margin-bottom: 8px; line-height: 1.5; }
  .card .card-action { font-size: 12px; font-weight: 600; }
  .card .card-due { font-size: 11px; color: #888; margin-top: 4px; }

  /* CALENDAR */
  .cal-day { background: #fff; border-radius: 11px; padding: 14px 18px; margin-bottom: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
  .cal-day-header { font-size: 13px; font-weight: 700; color: #0f3460; background: #eef4ff; border-radius: 6px; padding: 5px 10px; margin-bottom: 10px; display: inline-block; }
  .cal-day-today .cal-day-header { background: #0f3460; color: #fff; }
  .cal-event { border-left: 4px solid #2980b9; padding: 8px 12px; margin-bottom: 8px; background: #f7faff; border-radius: 0 6px 6px 0; }
  .cal-event:last-child { margin-bottom: 0; }
  .cal-event-title { font-size: 13px; font-weight: 700; }
  .cal-event-meta { font-size: 12px; color: #555; margin-top: 3px; }
  .cal-event-prep { font-size: 12px; color: #2980b9; margin-top: 3px; }
  .cal-event-warn { font-size: 12px; color: #c0392b; font-weight: 600; margin-top: 3px; }
  .status-accepted { color: #27ae60; font-weight: 700; }
  .status-declined { color: #c0392b; font-weight: 700; }
  .status-needs { color: #f39c12; font-weight: 700; }
  .status-confirmed { color: #2980b9; font-weight: 700; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 6px rgba(0,0,0,0.06); margin-bottom: 20px; }
  th { background: #1a1a2e; color: #fff; padding: 10px 13px; font-size: 12px; text-align: left; font-weight: 600; letter-spacing: 0.4px; }
  td { padding: 9px 13px; font-size: 13px; border-bottom: 1px solid #f0f2f5; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #fafafa; }
  .prio-high { color: #c0392b; font-weight: 700; }
  .prio-med { color: #d68910; font-weight: 700; }
  .prio-low { color: #27ae60; font-weight: 700; }
  .fit-high { background: #eafaf1; color: #27ae60; font-weight: 700; padding: 2px 8px; border-radius: 10px; font-size: 11px; }
  .fit-med { background: #fef9e7; color: #d68910; font-weight: 700; padding: 2px 8px; border-radius: 10px; font-size: 11px; }
  .fit-low { background: #fdf0f0; color: #c0392b; padding: 2px 8px; border-radius: 10px; font-size: 11px; }

  /* EMAIL CATEGORY BLOCKS */
  .email-cat { background: #fff; border-radius: 11px; padding: 14px 18px; margin-bottom: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
  .email-cat-header { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }
  .email-cat-title { font-size: 14px; font-weight: 700; }
  .email-count-badge { font-size: 11px; font-weight: 700; padding: 2px 9px; border-radius: 12px; color: #fff; }
  .badge-red { background: #c0392b; }
  .badge-yellow { background: #d68910; }
  .badge-blue { background: #2980b9; }
  .badge-green { background: #27ae60; }
  .badge-purple { background: #8e44ad; }
  .badge-gray2 { background: #7f8c8d; }
  .email-cat-body { font-size: 13px; color: #333; line-height: 1.6; }
  .email-cat-action { font-size: 12px; font-weight: 600; margin-top: 6px; }

  /* DASHBOARD */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 12px; margin-bottom: 20px; }
  .dash-tile { background: #fff; border-radius: 10px; padding: 14px 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.07); text-align: center; }
  .dash-tile .tile-num { font-size: 30px; font-weight: 800; }
  .dash-tile .tile-label { font-size: 12px; color: #666; margin-top: 4px; }
  .tile-red .tile-num { color: #c0392b; }
  .tile-yellow .tile-num { color: #d68910; }
  .tile-blue .tile-num { color: #2980b9; }
  .tile-green .tile-num { color: #27ae60; }
  .tile-purple .tile-num { color: #8e44ad; }
  .tile-gray .tile-num { color: #7f8c8d; }

  /* PRIORITIES */
  .priority-box { background: linear-gradient(135deg, #1a1a2e, #0f3460); color: #fff; border-radius: 12px; padding: 22px 28px; margin-top: 8px; }
  .priority-box h2 { font-size: 17px; margin-bottom: 14px; letter-spacing: 0.3px; }
  .priority-item { display: flex; gap: 14px; align-items: flex-start; margin-bottom: 12px; }
  .priority-num { background: #fff; color: #1a1a2e; font-weight: 800; font-size: 16px; min-width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
  .priority-text { font-size: 14px; line-height: 1.5; color: #d0ddf5; }

  /* TRASH */
  .trash-group { margin-bottom: 14px; }
  .trash-group-title { font-size: 13px; font-weight: 700; margin-bottom: 6px; padding: 4px 10px; border-radius: 6px; display: inline-block; }
  .trash-restore { background: #eafaf1; color: #27ae60; }
  .trash-review { background: #fef9e7; color: #d68910; }
  .trash-delete { background: #fdf0f0; color: #c0392b; }
  .trash-item { background: #fff; border-radius: 8px; padding: 8px 12px; margin-bottom: 6px; font-size: 13px; box-shadow: 0 1px 4px rgba(0,0,0,0.05); }
  .trash-sender { font-weight: 600; }
  .trash-reason { color: #666; font-size: 12px; }

  /* SPAM WARNING */
  .spam-banner { background: #fff0f0; border: 2px solid #c0392b; border-radius: 10px; padding: 12px 16px; margin-bottom: 14px; }
  .spam-banner strong { color: #c0392b; }

  /* ACCOUNTING TABLE */
  .accounting-total { background: #1a1a2e; color: #fff; font-weight: 700; }

  /* MISC */
  .divider { height: 1px; background: #e0e6ef; margin: 24px 0; }
  a { color: #2980b9; text-decoration: none; }
  a:hover { text-decoration: underline; }
  .footnote { font-size: 11px; color: #999; margin-top: 6px; }
  .unread-dot { display: inline-block; width: 8px; height: 8px; background: #2980b9; border-radius: 50%; margin-right: 6px; }

  @media (max-width: 600px) {
    .card-grid { grid-template-columns: 1fr; }
    .dashboard-grid { grid-template-columns: repeat(2, 1fr); }
    .header { padding: 20px 18px; }
  }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════ HEADER ═══ -->
<div class="header">
  <h1>Good Morning, Melissa ☀️</h1>
  <div class="subtitle">Executive Briefing — Prepared by Your Chief of Staff</div>
  <div class="header-meta">
    <div class="meta-pill">📅 Monday, July 6, 2026</div>
    <div class="meta-pill">📧 50 Emails Reviewed</div>
    <div class="meta-pill">📆 10 Calendar Events Reviewed</div>
    <div class="meta-pill">🚨 3 Security / Spam Alerts</div>
    <div class="meta-pill">✅ 7 Action Items</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════ EXEC SUMMARY ═══ -->
<div class="section-title">📌 Executive Summary</div>
<div class="exec-summary">
  <ul>
    <li class="badge-risk"><strong>🔴 BIGGEST RISK:</strong> Multiple sophisticated phishing / scam emails sitting in your inbox (unread) — fake cloud storage threats, casino deposit fraud, and a fake Lowe's prize — require immediate marking as spam and deletion. Your Atlassian Jira subscription also shows a real action-required deactivation notice that needs attention.</li>
    <li class="badge-opp"><strong>🟢 BIGGEST OPPORTUNITY:</strong> Indeed surfaced a <strong>VP of People @ RADAR</strong> role ($225K–$280K), and Scovai flagged a <strong>Chief People &amp; Culture Officer @ Omnisage LLC</strong> opening. Your HR Networking &amp; Job Search Group meets Wednesday, July 8 — prime time to activate both leads. Jim May accepted your LinkedIn invitation today — follow up while it's warm.</li>
    <li class="badge-cal"><strong>🔵 BIGGEST CALENDAR ITEM:</strong> You have a <strong>New Patient Video Visit with Dr. Keerthana Haridas, MD TODAY at 11:20 AM</strong> (in ~minutes — check your Connect account now). This week also includes a new patient appointment with <strong>Dr. Beth Leeman-Markowski (Epilepsy Center) on Thursday, July 9 at 3:30 PM</strong> — bring insurance card, photo ID, and medical records. State Farm bill is due tomorrow, July 7.</li>
  </ul>
</div>

<!-- ════════════════════════════════════════════ ACTION REQUIRED ═══ -->
<div class="section-title">⚡ Action Required</div>
<div class="card-grid">

  <div class="card card-red">
    <div class="card-label label-red">🔴 SECURITY — IMMEDIATE</div>
    <h3>Phishing Emails in Inbox (Unread)</h3>
    <div class="card-meta">Source: Multiple spoofed senders</div>
    <div class="card-body">Three dangerous phishing emails are sitting <strong>unread in your inbox or unread outside trash</strong>: (1) Fake "Cloud Storage Limit Reached" from <em>qkveckfsvkuces…</em>, (2) "Account Blocked / Photos Deleted" from <em>Payment-Declined</em>, (3) Fake casino deposit of $13,963.99 from spoofed sender. Do NOT click any links.</div>
    <div class="card-action label-red">→ Mark as spam &amp; delete all three immediately.</div>
    <div class="card-due">⏰ Due: NOW</div>
  </div>

  <div class="card card-red">
    <div class="card-label label-red">🔴 SECURITY — FAKE PRIZE SCAM</div>
    <h3>"Congratulations — Lowe's Winner" Scam</h3>
    <div class="card-meta">Source: Fake "Lowe's®" &lt;ehkopwsahxiwvr…gts353…&gt;</div>
    <div class="card-body">Spoofed Lowe's email claiming you won a Kobalt Tool Set. Fraudulent domain in sender address. Unread, not in trash. Classic phishing / data harvesting scam.</div>
    <div class="card-action label-red">→ Do not click. Mark as phishing. Delete.</div>
    <div class="card-due">⏰ Due: NOW</div>
  </div>

  <div class="card card-blue">
    <div class="card-label label-blue">🔵 CALENDAR — TODAY</div>
    <h3>Video Visit: Dr. Keerthana Haridas, MD</h3>
    <div class="card-meta">Source: Google Calendar | Today 11:20 AM – 12:00 PM ET</div>
    <div class="card-body">New patient video visit. You must be logged into the Connect portal before the appointment starts. Ensure your device camera and microphone are working.</div>
    <div class="card-action label-blue">→ Log into Connect NOW. Test audio/video.</div>
    <div class="card-due">⏰ Due: 11:20 AM TODAY</div>
  </div>

  <div class="card card-yellow">
    <div class="card-label label-yellow">🟡 BILLING — TOMORROW</div>
    <h3>State Farm Bill Due</h3>
    <div class="card-meta">Source: Google Calendar | July 7, 2026 (all day)</div>
    <div class="card-body">State Farm insurance bill is calendared as due tomorrow. Verify amount and confirm payment has been scheduled or process manually.</div>
    <div class="card-action label-yellow">→ Confirm auto-pay or pay manually before EOD today.</div>
    <div class="card-due">⏰ Due: July 7, 2026</div>
  </div>

  <div class="card card-yellow">
    <div class="card-label label-yellow">🟡 ACTION REQUIRED — SUBSCRIPTION</div>
    <h3>Jira Subscription Deactivation Warning</h3>
    <div class="card-meta">Source: Atlassian &lt;noreply@po.atlassian.net&gt;</div>
    <div class="card-body">Atlassian sent a legitimate notice that your Jira subscription will be deactivated due to inactivity. If you still use or need Jira, log in to prevent deactivation. If not, allow it to lapse or cancel to avoid future charges.</div>
    <div class="card-action label-yellow">→ Decide: Keep (log in) or Cancel. Act before deactivation.</div>
    <div class="card-due">⏰ Due: Within 48 hours</div>
  </div>

  <div class="card card-yellow">
    <div class="card-label label-yellow">🟡 RSVP NEEDED</div>
    <h3>HR Networking &amp; Job Search Group — Zoom</h3>
    <div class="card-meta">Source: Google Calendar | Wed July 8, 12:00–1:30 PM ET</div>
    <div class="card-body">Status is "needsAction" — you have NOT confirmed attendance. Large group networking call highly relevant to your job search. Zoom link available.</div>
    <div class="card-action label-yellow">→ RSVP Yes in Google Calendar. Add Zoom link to calendar.</div>
    <div class="card-due">⏰ Due: Before July 8</div>
  </div>

  <div class="card card-blue">
    <div class="card-label label-blue">🔵 PREP NEEDED — THURSDAY</div>
    <h3>New Patient Appt: Dr. Beth Leeman-Markowski, MD</h3>
    <div class="card-meta">Source: Google Calendar | Thu July 9, 3:30–4:30 PM ET | 223 E 34th St, NYC</div>
    <div class="card-body">Comprehensive Epilepsy Center. Must arrive 15 min early. Bring: insurance card, photo ID, medical records, recent labs/imaging. Phone: 646-558-0800.</div>
    <div class="card-action label-blue">→ Prepare your documents packet today. Plan travel for 3:00 PM arrival.</div>
    <div class="card-due">⏰ Due: July 9, 3:15 PM arrival</div>
  </div>

  <div class="card card-green">
    <div class="card-label label-green">🟢 JOB SEARCH — HIGH PRIORITY</div>
    <h3>VP of People @ RADAR — $225K–$280K</h3>
    <div class="card-meta">Source: Indeed &lt;donotreply@match.indeed.com&gt;</div>
    <div class="card-body">Indeed flagged this as a strong match for your HR leadership background. Salary range $225K–$280K/year at RADAR. Role aligns with your MPA and executive HR experience.</div>
    <div class="card-action label-green">→ Research RADAR, tailor resume, and apply or save. Bring to Wed networking call.</div>
    <div class="card-due">⏰ Due: This week</div>
  </div>

</div>

<!-- ══════════════════════════════════════════ FULL 7-DAY CALENDAR ═══ -->
<div class="section-title">📆 Full 7-Day Calendar (July 6–13, 2026)</div>

<!-- Monday July 6 -->
<div class="cal-day cal-day-today">
  <div class="cal-day-header">📅 Monday, July 6, 2026 — TODAY</div>
  <div class="cal-event" style="border-color:#c0392b;">
    <div class="cal-event-title">🩺 New Patient Video Visit — Dr. Keerthana Haridas, MD</div>
    <div class="cal-event-meta">⏰ 11:20 AM – 12:00 PM ET &nbsp;|&nbsp; Status: <span class="status-accepted">ACCEPTED ✓</span> &nbsp;|&nbsp; Location: Video (Connect Portal)</div>
    <div class="cal-event-prep">🔧 Prep: Log into Connect portal NOW. Test camera + microphone. Have your medical history ready.</div>
    <div class="cal-event-warn">⚠️ STARTING VERY SOON — Ensure you are logged in before 11:20 AM.</div>
  </div>
</div>

<!-- Tuesday July 7 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Tuesday, July 7, 2026</div>
  <div class="cal-event" style="border-color:#f39c12;">
    <div class="cal-event-title">💰 State Farm Bill Due (All Day Reminder)</div>
    <div class="cal-event-meta">⏰ All Day &nbsp;|&nbsp; Status: <span class="status-confirmed">CONFIRMED</span></div>
    <div class="cal-event-prep">🔧 Prep: Verify payment is scheduled or pay today to avoid missing deadline.</div>
  </div>
  <div class="cal-event" style="border-color:#2980b9;">
    <div class="cal-event-title">🏥 PT (Physical Therapy / Personal Training)</div>
    <div class="cal-event-meta">⏰ 12:00 PM – 1:00 PM ET &nbsp;|&nbsp; Status: <span class="status-confirmed">CONFIRMED</span> &nbsp;|&nbsp; Location: TBD</div>
    <div class="cal-event-prep">🔧 Prep: Confirm location/address. Wear appropriate attire. Allow travel time.</div>
  </div>
</div>

<!-- Wednesday July 8 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Wednesday, July 8, 2026</div>
  <div class="cal-event" style="border-color:#f39c12;">
    <div class="cal-event-title">🤝 HR Networking &amp; Job Search Group — Zoom 2</div>
    <div class="cal-event-meta">⏰ 12:00 PM – 1:30 PM ET &nbsp;|&nbsp; Status: <span class="status-needs">NEEDS ACTION ⚠️</span> &nbsp;|&nbsp; <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a></div>
    <div class="cal-event-prep">🔧 Prep: RSVP in calendar. Review team guidelines doc. Prepare your 30-second intro / elevator pitch. Research RADAR VP of People role &amp; Omnisage CPO role to discuss with the group. 190+ attendees.</div>
    <div class="cal-event-warn">⚠️ RSVP REQUIRED — Status still "needsAction." Confirm attendance today.</div>
  </div>
  <div class="cal-event" style="border-color:#27ae60;">
    <div class="cal-event-title">🌐 Network (Personal Networking Block)</div>
    <div class="cal-event-meta">⏰ 12:00 PM – 1:30 PM ET &nbsp;|&nbsp; Status: <span class="status-confirmed">CONFIRMED</span></div>
    <div class="cal-event-warn">⚠️ CONFLICT: Overlaps exactly with HR Networking Zoom above. These may be the same event or one may need to be resolved.</div>
    <div class="cal-event-prep">🔧 Note: Confirm if "Network" entry is a duplicate reminder or a separate commitment. If duplicate, consider removing to avoid confusion.</div>
  </div>
</div>

<!-- Thursday July 9 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Thursday, July 9, 2026</div>
  <div class="cal-event" style="border-color:#c0392b;">
    <div class="cal-event-title">🏢 Executive Roundtable (John Madigan / Zoom)</div>
    <div class="cal-event-meta">⏰ 9:00 AM – 10:30 AM ET &nbsp;|&nbsp; Status: <span class="status-declined">DECLINED ✗</span> &nbsp;|&nbsp; <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> | PW: 205454</div>
    <div class="cal-event-prep">🔧 Note: You have declined this event. If circumstances changed, reach out to John Madigan to request reinstatement or reconsider RSVP.</div>
  </div>
  <div class="cal-event" style="border-color:#f39c12;">
    <div class="cal-event-title">🤝 HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
    <div class="cal-event-meta">⏰ 12:00 PM – 1:00 PM ET &nbsp;|&nbsp; Status: <span class="status-needs">NEEDS ACTION ⚠️</span> &nbsp;|&nbsp; <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a></div>
    <div class="cal-event-prep">🔧 Prep: RSVP in calendar. Open office hours format — come with specific questions. Note: organizer requests NO automated AI notetaking tools.</div>
    <div class="cal-event-warn">⚠️ RSVP REQUIRED.</div>
  </div>
  <div class="cal-event" style="border-color:#c0392b;">
    <div class="cal-event-title">🏥 New Patient Appt — Dr. Beth A. Leeman-Markowski, MD (Comprehensive Epilepsy Center)</div>
    <div class="cal-event-meta">⏰ 3:30 PM – 4:30 PM ET &nbsp;|&nbsp; Status: <span class="status-accepted">ACCEPTED ✓</span> / <span class="status-confirmed">CONFIRMED</span> &nbsp;|&nbsp; 223 East 34th Street, New York, NY 10016</div>
    <div class="cal-event-prep">🔧 Prep: Arrive by 3:15 PM. Bring: insurance card, photo ID, medical records, recent labs/imaging. Phone: 646-558-0800. Plan NYC travel accordingly.</div>
    <div class="cal-event-warn">⚠️ NOTE: Two calendar entries exist for this appointment (duplicate). Both confirmed. No action needed other than ensuring you only attend once.</div>
  </div>
</div>

<!-- Friday July 10 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Friday, July 10, 2026</div>
  <div class="cal-event" style="border-color:#95a5a6;">
    <div class="cal-event-title">📭 No Events Scheduled</div>
    <div class="cal-event-meta">Free day — consider using for follow-ups from Thursday networking and appointments.</div>
  </div>
</div>

<!-- Saturday July 11 + Sunday July 12 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Saturday–Sunday, July 11–12, 2026</div>
  <div class="cal-event" style="border-color:#95a5a6;">
    <div class="cal-event-title">📭 No Events Scheduled</div>
    <div class="cal-event-meta">Weekend — no calendar commitments found.</div>
  </div>
</div>

<!-- Monday July 13 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Monday, July 13, 2026</div>
  <div class="cal-event" style="border-color:#8e44ad;">
    <div class="cal-event-title">💉 Stephanie Infusion (All Day Reminder)</div>
    <div class="cal-event-meta">⏰ All Day &nbsp;|&nbsp; Status: <span class="status-confirmed">CONFIRMED</span></div>
    <div class="cal-event-prep">🔧 Prep: Confirm logistics for Stephanie's infusion appointment — location, transportation, timing, and any pre-appointment instructions.</div>
  </div>
</div>

<!-- ══════════════════════════════════════ JOB SEARCH & PIPELINE ═══ -->
<div class="section-title">🟢 Job Search &amp; Interview Pipeline</div>
<table>
  <thead>
    <tr>
      <th>Type</th>
      <th>Role / Event</th>
      <th>Source</th>
      <th>Details</th>
      <th>Fit</th>
      <th>Next Step</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>🎯 Job Alert</td>
      <td><strong>VP of People @ RADAR</strong></td>
      <td>Indeed</td>
      <td>$225,000–$280,000/yr. Strong match per Indeed's algorithm for Melissa's HR leadership background.</td>
      <td><span class="fit-high">HIGH</span></td>
      <td>Research RADAR; tailor resume; apply this week</td>
    </tr>
    <tr>
      <td>🎯 Job Alert</td>
      <td><strong>Chief People &amp; Culture Officer @ Omnisage LLC</strong></td>
      <td>Scovai</td>
      <td>Open item on Scovai profile. CPO-level role. Salary not listed.</td>
      <td><span class="fit-high">HIGH</span></td>
      <td>Log into Scovai; review full JD; apply or dismiss</td>
    </tr>
    <tr>
      <td>🤝 Networking</td>
      <td><strong>HR Networking &amp; Job Search Group</strong></td>
      <td>Google Calendar</td>
      <td>Wed July 8, 12–1:30 PM Zoom. 190+ HR professionals. Active job search group.</td>
      <td><span class="fit-high">HIGH</span></td>
      <td>RSVP today; prepare pitch &amp; bring leads to discuss</td>
    </tr>
    <tr>
      <td>🤝 Networking</td>
      <td><strong>HR Networking: Open Office Hours</strong></td>
      <td>Google Calendar</td>
      <td>Thu July 9, 12–1 PM Zoom. Open discussion, no recording.</td>
      <td><span class="fit-high">HIGH</span></td>
      <td>RSVP today; prepare 2–3 specific questions</td>
    </tr>
    <tr>
      <td>🔗 LinkedIn</td>
      <td><strong>Jim May — Connection Accepted</strong></td>
      <td>LinkedIn (via Gmail)</td>
      <td>Jim accepted Melissa's invitation today. New connection — warm contact window is open.</td>
      <td><span class="fit-med">MEDIUM</span></td>
      <td>Send a warm follow-up message to Jim May today</td>
    </tr>
    <tr>
      <td>📋 Executive Roundtable</td>
      <td><strong>Executive Roundtable — John Madigan</strong></td>
      <td>Google Calendar</td>
      <td>Thu July 9, 9–10:30 AM. Currently DECLINED by Melissa.</td>
      <td><span class="fit-med">MEDIUM</span></td>
      <td>Consider whether to reconsider declining — may be a valuable executive peer connection</td>
    </tr>
  </tbody>
</table>

<!-- ════════════════════════════════ FULL EMAIL REVIEW BY CATEGORY ═══ -->
<div class="section-title">📧 Full Email Review by Category</div>

<!-- Security / Risk -->
<div class="email-cat">
  <div class="email-cat-header">
    <span class="email-count-badge badge-red">6</span>
    <span class="email-cat-title" style="color:#c0392b;">🔴 Security / Risk / Spam / Phishing</span>
  </div>
  <div class="email-cat-body">
    <strong>Emails:</strong><br>
    1. <span class="unread-dot"></span><strong>"Cloud Storage" (qkveckfsvkuces…)</strong> — "Storage Limit Reached (100%)" — Phishing. Spoofed domain. Unread, not in trash.<br>
    2. <span class="unread-dot"></span><strong>Payment-Declined (ypsykccmtzl@xxjd…)</strong> — "Account Blocked / Photos Removed Sun 05 Jul" — Phishing. Fake cloud threat. Unread.<br>
    3. <span class="unread-dot"></span><strong>"💲melissaw212💲" (belxnzzyealkio…)</strong> — "$13,963.99 direct deposit" — Casino scam with failed template variable ({{No_Deposit_Required}}). Unread.<br>
    4. <span class="unread-dot"></span><strong>"Lowe's®" (ehkopwsahxiwvr…gts353…)</strong> — "We have been trying to reach you — Kobalt Tool Set Winner" — Fake prize scam. Unread.<br>
    5. <span class="unread-dot"></span><strong>Atlassian (noreply@po.atlassian.net)</strong> — "Jira subscription will be deactivated due to inactivity" — Likely LEGITIMATE. Unread. Requires action.<br>
    6. <strong>Notify NYC (noreply@everbridge.net)</strong> — "Safe Overnight Locations: Flooding (NYC)" — Legitimate NYC emergency alert. Heavy rainfall 7/6–7/7. Safe overnight locations listed.
  </div>
  <div class="email-cat-action" style="color:#c0392b;">→ IMMEDIATELY: Mark items 1–4 as phishing and delete. Item 5: Decide on Jira (keep/cancel). Item 6: Read flooding alert — plan outdoor activities accordingly.</div>
</div>

<!-- Job Search -->
<div class="email-cat">
  <div class="email-cat-header">
    <span class="email-count-badge badge-green">2</span>
    <span class="email-cat-title" style="color:#27ae60;">🟢 Job Search / Opportunities</span>
  </div>
  <div class="email-cat-body">
    1. <strong>Indeed</strong> — "VP of People @ RADAR" — $225K–$280K. Strong match. Read.<br>
    2. <strong>Scovai</strong> — "1 thing waits for you today · Omnisage LLC" — Chief People &amp; Culture Officer opening. Read.
  </div>
  <div class="email-cat-action" style="color:#27ae60;">→ Act on both this week. High-value leads.</div>
</div>

<!-- Recruiters / Networking -->
<div class="email-cat">
  <div class="email-cat-header">
    <span class="email-count-badge badge-green">1</span>
    <span class="email-cat-title" style="color:#27ae60;">🟢 Recruiters / Professional Networking</span>
  </div>
  <div class="email-cat-body">
    1. <strong>LinkedIn (Jim May)</strong> — "Jim accepted your invitation, explore their network" — New connection. Warm outreach window open. Read.
  </div>
  <div class="email-cat-action" style="color:#27ae60;">→ Send a personalized message to Jim May today.</div>
</div>

<!-- Calendar / Events -->
<div class="email-cat">
  <div class="email-cat-header">
    <span class="email-count-badge badge-blue">1</span>
    <span class="email-cat-title" style="color:#2980b9;">🔵 Calendar / Scheduling / Events</span>
  </div>
  <div class="email-cat-body">
    1. <strong>Otter.ai Insights</strong> — "Your upcoming meetings" — Weekly meeting prep email from Otter.ai. Read.
  </div>
  <div class="email-cat-action" style="color:#2980b9;">→ Review upcoming meetings in Otter. Note: HR Office Hours organizer requests NO AI notetaking tools on July 9.</div>
</div>

<!-- Medical / Health -->
<div class="email-cat">
  <div class="email-cat-header">
    <span class="email-count-badge badge-red">2</span>
    <span class="email-cat-title" style="color:#8e44ad;">🟣 Medical / Health / Pickup Orders</span>
  </div>
  <div class="email-cat-body">
    1. <span class="unread-dot"></span><strong>Ulta Beauty Orders</strong> — "We're getting your order ready! 🛍️" — Pickup order being prepared. Unread. In inbox.<br>
    2. <span class="unread-dot"></span><strong>Sephora</strong> — "Processing: your pickup order" — Order processing, will notify when ready. Unread. In inbox.
  </div>
  <div class="email-cat-action" style="color:#8e44ad;">→ Monitor Ulta &amp; Sephora for pickup-ready notifications. Check pickup deadlines.</div>
</div>

<!-- Financial / Billing -->
<div class="email-cat">
  <div class="email-cat-header">
    <span class="email-count-badge badge-yellow">1</span>
    <span class="email-cat-title" style="color:#d68910;">🟡 Financial / Billing / Delivery</span>
  </div>
  <div class="email-cat-body">
    1. <strong>USPS Informed Delivery</strong> — "Your Daily Digest for Mon, 7/6 is ready" — 1 mailpiece + 1 inbound package arriving. Read.
  </div>
  <div class="email-cat-action" style="color:#d68910;">→ Check USPS app for package details. Be home or arrange for secure pickup.</div>
</div>

<!-- Professional Development -->
<div class="email-cat">
  <div class="email-cat-header">
    <span class="email-count-badge badge-purple">4</span>
    <span class="email-cat-title" style="color:#8e44ad;">🟣 Professional Development / AI / Leadership</span>
  </div>
  <div class="email-cat-body">
    1. <span class="unread-dot"></span><strong>AI For Leaders</strong> — "Nvidia's Robots Show Up to Work Already Experienced" (×2 duplicate) — Humanoid robots + simulation training. Unread. In inbox. (Counted as 2 emails.)<br>
    2. <span class="unread-dot"></span><strong>The AI Report</strong> — "⚡ Microsoft bets $2.5B on AI / Alibaba bans Anthropic products" — Major AI industry moves. Unread.<br>
    3. <strong>Martin / The People People Group</strong> — "🦢 Come For The Hot Take, Stay For Björk Take" — HR &amp; people leadership newsletter. Read.
  </div>
  <div class="email-cat-action" style="color:#8e44ad;">→ Read AI For Leaders and The AI Report when time permits — relevant to your HR technology positioning. Deduplicate the AI For Leaders email.</div>
</div>

<!-- Personal -->
<div class="email-cat">
  <div class="email-cat-header">
    <span class="email-count-badge badge-gray2">4</span>
    <span class="email-cat-title" style="color:#555;">⚪ Personal</span>
  </div>
  <div class="email-cat-body">
    1. <strong>Match</strong> — "Michael likes you. See if it's mutual." (×2 — sent at 5:44 AM and 4:49 AM) — Duplicate notification.<br>
    2. <strong>Match</strong> — "Bestheartofall likes you. See if it's mutual." — Read.<br>
    3. <strong>Match</strong> — "Stef likes you. See if it's mutual." — Read.<br>
    4. <strong>Match</strong> — "Stef just sent you a new message. 💌" — Read.
  </div>
  <div class="email-cat-action" style="color:#555;">→ Check Match at your convenience. Stef sent a message — may be worth reading.</div>
</div>

<!-- Newsletters / Subscriptions -->
<div class="email-cat">
  <div class="email-cat-header">
    <span class="email-count-badge badge-purple">10</span>
    <span class="email-cat-title" style="color:#8e44ad;">🟣 Newsletters &amp; Subscriptions</span>
  </div>
  <div class="email-cat-body">
    1. <strong>TLDR Newsletter</strong> — "Amazon's Starlink rival, Nvidia revenue share, agentic autonomy levels" — Tech industry digest. Read.<br>
    2. <strong>Medium Daily Digest</strong> — "Submission Guidelines | Diana Dolea in The Nature Writing Review" — Read.<br>
    3. <strong>Medium Daily Digest</strong> — "Japan Just Beat Claude Mythos…" — AI-focused. Read.<br>
    4. <strong>The Hustle</strong> — "🧩 The jigsaw puzzle king" — Business/culture. Read.<br>
    5. <strong>The Average Joe</strong> (in trash) — "🫧 Bubble-ception / The search for connection" — Finance/investing newsletter. In trash.<br>
    6. <strong>Gemma Bonham-Carter</strong> — "the real reason your AI output kinda… sucks?" — AI productivity tips. Read.<br>
    7. <strong>CoolDeep AI</strong> (in trash) — "Claude just got access to your Gmail, Drive…" — AI tips/marketing. In trash.<br>
    8. <strong>1% Better</strong> (in trash) — "Brooklyn Bridge Burns, EV Surprise, Guide to Modern Fatherhood" — General newsletter. In trash.<br>
    9. <strong>The Daily Skimm</strong> (in trash) — "A royal growth spurt" — News digest. In trash.<br>
    10. <strong>Gemma Bonham-Carter</strong> (in trash) — "❗don't buy another AI tool" — AI marketing. In trash.
  </div>
  <div class="email-cat-action" style="color:#8e44ad;">→ Review TLDR and AI Report as relevant. Consider unsubscribing from lower-value digests to reduce inbox noise.</div>
</div>

<!-- Promotional / Retail -->
<div class="email-cat">
  <div class="email-cat-header">
    <span class="email-count-badge badge-gray2">10</span>
    <span class="email-cat-title" style="color:#7f8c8d;">⚫ Promotional / Retail</span>
  </div>
  <div class="email-cat-body">
    1. <strong>SHEIN</strong> — "All the Style, None of the Splurge 😎" (from market-us.shein.com) — Read.<br>
    2. <strong>SHEIN</strong> — "All the Style, None of the Splurge 😎" (from news.edmmarket.shein.com) — Duplicate. Read.<br>
    3. <strong>SHEIN</strong> — "Start from $2.99 | Fresh finds just dropped!" — Read.<br>
    4. <strong>Gap Factory</strong> — "Layer on an extra 15% off and bonus 10% off" — Read.<br>
    5. <strong>Gap Factory</strong> — "$4 flip-flops, more doorbusters, 50–70% off sitewide" — Unread.<br>
    6. <strong>Kohl's</strong> — "Today only: 20% off home 🤩" — Read.<br>
    7. <strong>Warby Parker</strong> — "Mind answering a quick question?" — Feedback survey. Read.<br>
    8. <strong>Your Local Chick-fil-A</strong> — "A little something from me to you 🎁" — Reward/gift notification. Read.<br>
    9. <strong>Temu</strong> — "You received a thank-you reward" — Promo. Unread.<br>
    10. <strong>YesStyle.com</strong> — "🎂 Wanna be spoiled for your birthday?" — Birthday promo. Read.
  </div>
  <div class="email-cat-action" style="color:#7f8c8d;">→ Delete/archive all. Warby Parker survey worth 2 min if you recently bought glasses. Chick-fil-A gift — log in to redeem if interested.</div>
</div>

<!-- Lisa Rangel -->
<div class="email-cat">
  <div class="email-cat-header">
    <span class="email-count-badge badge-gray2">2</span>
    <span class="email-cat-title" style="color:#7f8c8d;">⚫ Lisa Rangel / Chameleon Resumes (Trash)</span>
  </div>
  <div class="email-cat-body">
    1. <strong>Lisa Rangel</strong> — "how much unhappier do you have to be?" — Unread. In trash.<br>
    2. <strong>Lisa Rangel</strong> — "Please STOP asking this question!" — Unread. In trash.
  </div>
  <div class="email-cat-action" style="color:#7f8c8d;">→ Both trashed. Safe to permanently delete. Consider unsubscribing if you no longer find value.</div>
</div>

<!-- Social / Community -->
<div class="email-cat">
  <div class="email-cat-header">
    <span class="email-count-badge badge-gray2">3</span>
    <span class="email-cat-title" style="color:#7f8c8d;">⚫ Social / Community Notifications</span>
  </div>
  <div class="email-cat-body">
    1. <strong>Facebook Friend Suggestions</strong> — "Rosario Pichardo De Rincon is in your Santo Domingo network" — Read.<br>
    2. <strong>Nextdoor Local News</strong> — "Body found stuffed inside couch at Brooklyn apartment building" — Local news alert. Read.<br>
    3. <strong>Trending on Nextdoor</strong> — "Do NOT tether dogs and leave unattended in New…" — Community post. Unread.
  </div>
  <div class="email-cat-action" style="color:#7f8c8d;">→ Low priority. Archive or delete. Manage Nextdoor notification frequency if overwhelming.</div>
</div>

<!-- TrimRx / Weight Loss -->
<div class="email-cat">
  <div class="email-cat-header">
    <span class="email-count-badge badge-gray2">1</span>
    <span class="email-cat-title" style="color:#7f8c8d;">⚫ Wellness / Weight Loss Marketing (Suspicious Sender)</span>
  </div>
  <div class="email-cat-body">
    1. <strong>TrimRx</strong> (suspicious sender domain: blmwtkujaocrccisqyowmmhlty.us) — "Monthly, 3-month, or 6-month — which plan fits?" — GLP-1 weight loss marketing. Unread. Suspicious domain.
  </div>
  <div class="email-cat-action" style="color:#c0392b;">→ Suspicious sender domain — do not click links. Mark as spam and delete.</div>
</div>

<!-- Casino Spam in Trash -->
<div class="email-cat">
  <div class="email-cat-header">
    <span class="email-count-badge badge-red">1</span>
    <span class="email-cat-title" style="color:#c0392b;">🔴 Casino Spam (Trash)</span>
  </div>
  <div class="email-cat-body">
    1. <strong>"Congratulations!" (ildsupporttizl@sbubsalzqyzfdntyafregyjr.com)</strong> — "200 Free Spins 💰 Pending in your Account 🎰" — Casino spam. Unread. In trash.
  </div>
  <div class="email-cat-action" style="color:#c0392b;">→ Already in trash. Permanently delete. Mark as spam.</div>
</div>

<!-- ══════════════════════════════════════════════ TRASH REVIEW ═══ -->
<div class="section-title">🗑️ Trash Review</div>

<div class="trash-group">
  <div class="trash-group-title trash-restore">✅ RESTORE — Worth Reading</div>
  <div class="trash-item">
    <span class="trash-sender">The Average Joe</span> — "🫧 Bubble-ception" — Finance/investing newsletter you previously subscribed to. May contain relevant market insights. <span class="trash-reason">Reason to restore: Could contain useful financial context for salary negotiation awareness.</span>
  </div>
  <div class="trash-item">
    <span class="trash-sender">1% Better</span> — "Brooklyn Bridge Burns, EV Surprise, Guide to Modern Fatherhood" — General interest newsletter. <span class="trash-reason">Reason to restore: Brooklyn Bridge fire is a local NYC news item that may be relevant.</span>
  </div>
</div>

<div class="trash-group">
  <div class="trash-group-title trash-review">🔍 REVIEW BEFORE DELETING</div>
  <div class="trash-item">
    <span class="trash-sender">Gemma Bonham-Carter</span> — "❗don't buy another AI tool" — AI productivity content creator. <span class="trash-reason">May be marketing-heavy but occasionally has useful AI workflow tips relevant to your executive positioning.</span>
  </div>
  <div class="trash-item">
    <span class="trash-sender">CoolDeep AI</span> — "Claude just got access to your Gmail, Drive… Most people missed this" — AI newsletter. <span class="trash-reason">If Claude/Google Workspace integration is relevant to your work, this may be worth skimming. However, clickbait-style subject — review cautiously.</span>
  </div>
  <div class="trash-item">
    <span class="trash-sender">The Daily Skimm</span> — "A royal growth spurt" — News digest. <span class="trash-reason">Unread. If you still enjoy The Skimm, restore. Otherwise, unsubscribe to reduce inbox noise.</span>
  </div>
</div>

<div class="trash-group">
  <div class="trash-group-title trash-delete">🗑️ SAFE TO PERMANENTLY DELETE</div>
  <div class="trash-item">
    <span class="trash-sender">Lisa Rangel / Chameleon Resumes</span> — (2 emails) "how much unhappier do you have to be?" + "Please STOP asking this question!" — <span class="trash-reason">Career/resume marketing. Already trashed. Permanently delete + consider unsubscribing.</span>
  </div>
  <div class="trash-item">
    <span class="trash-sender">"Congratulations!" Casino Spam</span> — "200 Free Spins Pending in your Account 🎰" — <span class="trash-reason">Obvious spam from fraudulent domain. Permanently delete immediately.</span>
  </div>
  <div class="trash-item">
    <span class="trash-sender">The Average Joe (if not restoring)</span> — "Bubble-ception" — <span class="trash-reason">Safe to delete if you prefer to reduce newsletter subscriptions.</span>
  </div>
</div>

<!-- ═══════════════════════════════════ PROMOTIONAL / RETAIL SUMMARY ═══ -->
<div class="section-title">🛍️ Promotional / Retail Summary</div>
<table>
  <thead>
    <tr>
      <th>Brand / Sender</th>
      <th>Count</th>
      <th>Subject / Theme</th>
      <th>Recommendation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>SHEIN</td>
      <td>3</td>
      <td>Home deals from $0.19; fresh finds from $2.99; style deals (multiple domains)</td>
      <td><span class="fit-low">Delete / Unsubscribe</span> — Multiple duplicate sends from different domains suggests list mismanagement. Low priority.</td>
    </tr>
    <tr>
      <td>Gap Factory</td>
      <td>2</td>
      <td>$4 flip-flops; 50–70% off sitewide; extra 15% off</td>
      <td><span class="fit-med">Review if shopping</span> — Sale pricing is legitimate. Otherwise delete.</td>
    </tr>
    <tr>
      <td>Kohl's</td>
      <td>1</td>
      <td>Today only: 20% off home; summer picks</td>
      <td><span class="fit-low">Delete</span> — Time-limited offer, read only if actively shopping for home goods today.</td>
    </tr>
    <tr>
      <td>Warby Parker</td>
      <td>1</td>
      <td>Customer feedback survey</td>
      <td><span class="fit-med">Quick Review</span> — If you recently purchased, 2-minute survey is courteous. Otherwise archive.</td>
    </tr>
    <tr>
      <td>Chick-fil-A (Local)</td>
      <td>1</td>
      <td>"A little something from me to you 🎁" — points/gift from operator Jared Caldwell</td>
      <td><span class="fit-med">Keep / Redeem</span> — 402 pts noted. Check app for reward details.</td>
    </tr>
    <tr>
      <td>Temu</td>
      <td>1</td>
      <td>"You received a thank-you reward" — TEMU Discount Card</td>
      <td><span class="fit-low">Delete</span> — Standard marketing promo. Low value.</td>
    </tr>
    <tr>
      <td>YesStyle.com</td>
      <td>1</td>
      <td>"Wanna be spoiled for your birthday?" — birthday promo request</td>
      <td><span class="fit-low">Delete / Ignore</span> — Marketing tactic asking for birthday info.</td>
    </tr>
    <tr>
      <td>Ulta Beauty</td>
      <td>1</td>
      <td>"We're getting your order ready!" — Pickup order in progress</td>
      <td><span class="fit-high">Keep / Monitor</span> — Real order notification. Watch for pickup-ready email.</td>
    </tr>
    <tr>
      <td>Sephora</td>
      <td>1</td>
      <td>"Processing: your pickup order"</td>
      <td><span class="fit-high">Keep / Monitor</span> — Real order. Watch for "ready for pickup" follow-up.</td>
    </tr>
    <tr>
      <td>TrimRx (suspicious domain)</td>
      <td>1</td>
      <td>GLP-1 weight loss plan marketing</td>
      <td><span class="fit-low">Mark Spam / Delete</span> — Suspicious sender domain. Do not engage.</td>
    </tr>
  </tbody>
</table>

<!-- ═══════════════════════════════ NEWSLETTERS & SUBSCRIPTIONS ═══ -->
<div class="section-title">📰 Newsletters &amp; Subscriptions</div>
<table>
  <thead>
    <tr>
      <th>Sender</th>
      <th>Topic</th>
      <th>Recommendation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>AI For Leaders</strong> (×2 duplicate)</td>
      <td>AI in the workplace, Nvidia humanoid robots</td>
      <td><span class="fit-high">Keep</span> — Highly relevant to executive positioning in HR + AI. Investigate why duplicate was sent.</td>
    </tr>
    <tr>
      <td><strong>The AI Report</strong></td>
      <td>Microsoft $2.5
<hr>
<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Financial / Billing</td><td>1</td></tr>
<tr><td>Job Search / Recruiters</td><td>3</td></tr>
<tr><td>Medical / Health</td><td>3</td></tr>
<tr><td>Other / Review</td><td>28</td></tr>
<tr><td>Professional Development / Newsletters</td><td>1</td></tr>
<tr><td>Promotional / Retail</td><td>8</td></tr>
<tr><td>Security / Risk</td><td>6</td></tr>
</table>
<p><strong>Audit Note:</strong> Every fetched email was reviewed and assigned to one category. Trash emails were included in review. Promotional and low-value emails were accounted for but deprioritized.</p>

