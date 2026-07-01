<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing – Melissa A. Weiss | July 1, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrapper { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header-card { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; }
  .header-card h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header-card .subtitle { font-size: 15px; color: #a8b4c8; margin-top: 4px; }
  .header-meta { display: flex; gap: 32px; margin-top: 20px; flex-wrap: wrap; }
  .header-meta-item { background: rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 18px; text-align: center; }
  .header-meta-item .val { font-size: 22px; font-weight: 700; color: #7ecaf2; }
  .header-meta-item .lbl { font-size: 11px; color: #a8b4c8; text-transform: uppercase; letter-spacing: 0.8px; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; padding: 10px 16px; border-radius: 8px 8px 0 0; display: flex; align-items: center; gap: 8px; }
  .section-body { background: #fff; border-radius: 0 0 10px 10px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }

  .sec-red .section-title    { background: #c0392b; color: #fff; }
  .sec-yellow .section-title { background: #f39c12; color: #fff; }
  .sec-blue .section-title   { background: #2471a3; color: #fff; }
  .sec-green .section-title  { background: #1e8449; color: #fff; }
  .sec-purple .section-title { background: #7d3c98; color: #fff; }
  .sec-gray .section-title   { background: #6c757d; color: #fff; }
  .sec-navy .section-title   { background: #1a1a2e; color: #fff; }
  .sec-teal .section-title   { background: #117a65; color: #fff; }
  .sec-orange .section-title { background: #d35400; color: #fff; }
  .sec-indigo .section-title { background: #2c3e7a; color: #fff; }

  /* EXEC SUMMARY */
  .exec-bullets { list-style: none; }
  .exec-bullets li { padding: 10px 14px; margin-bottom: 8px; border-radius: 8px; border-left: 5px solid; font-size: 14px; }
  .exec-bullets li.risk   { background: #fdf2f2; border-color: #c0392b; }
  .exec-bullets li.oppty { background: #f0faf4; border-color: #1e8449; }
  .exec-bullets li.cal   { background: #eaf3fb; border-color: #2471a3; }
  .exec-bullets li strong { font-weight: 700; }

  /* ACTION CARDS */
  .action-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(310px, 1fr)); gap: 14px; }
  .action-card { border-radius: 10px; padding: 16px; border-left: 5px solid; }
  .action-card.red    { background: #fdf2f2; border-color: #c0392b; }
  .action-card.yellow { background: #fefdf0; border-color: #f39c12; }
  .action-card.blue   { background: #eaf3fb; border-color: #2471a3; }
  .action-card.green  { background: #f0faf4; border-color: #1e8449; }
  .action-card.purple { background: #f9f1ff; border-color: #7d3c98; }
  .action-card .label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; }
  .action-card.red    .label { color: #c0392b; }
  .action-card.yellow .label { color: #b7770d; }
  .action-card.blue   .label { color: #2471a3; }
  .action-card.green  .label { color: #1e8449; }
  .action-card.purple .label { color: #7d3c98; }
  .action-card h3 { font-size: 14px; font-weight: 700; margin-bottom: 6px; }
  .action-card .meta { font-size: 12px; color: #555; margin-bottom: 4px; }
  .action-card .next { font-size: 13px; margin-top: 8px; font-weight: 600; }
  .action-card .due  { font-size: 11px; color: #888; margin-top: 4px; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { background: #2471a3; color: #fff; border-radius: 6px; padding: 6px 14px; font-weight: 700; font-size: 13px; margin-bottom: 8px; }
  .cal-event { background: #eaf3fb; border-radius: 8px; padding: 10px 14px; margin-bottom: 8px; border-left: 4px solid #2471a3; }
  .cal-event.declined { border-color: #c0392b; background: #fdf2f2; }
  .cal-event.needs-action { border-color: #f39c12; background: #fefdf0; }
  .cal-event.allday { border-color: #7d3c98; background: #f9f1ff; }
  .cal-event h4 { font-size: 13px; font-weight: 700; margin-bottom: 4px; }
  .cal-event .cal-meta { font-size: 12px; color: #555; margin: 2px 0; }
  .cal-event .cal-badge { display: inline-block; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 10px; margin-top: 4px; }
  .badge-confirmed  { background: #d4efdf; color: #1e8449; }
  .badge-declined   { background: #fadbd8; color: #c0392b; }
  .badge-needs      { background: #fef9e7; color: #b7770d; border: 1px solid #f39c12; }
  .badge-allday     { background: #e8daef; color: #7d3c98; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #f0f2f5; text-align: left; padding: 8px 10px; font-weight: 700; border-bottom: 2px solid #ddd; }
  td { padding: 7px 10px; border-bottom: 1px solid #eee; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f8f9fa; }

  /* TAGS */
  .tag { display: inline-block; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 10px; margin: 1px; }
  .tag-high   { background: #fadbd8; color: #c0392b; }
  .tag-med    { background: #fef9e7; color: #b7770d; }
  .tag-low    { background: #eaecee; color: #555; }
  .tag-green  { background: #d4efdf; color: #1e8449; }
  .tag-blue   { background: #d6eaf8; color: #2471a3; }
  .tag-red    { background: #fadbd8; color: #c0392b; }
  .tag-purple { background: #e8daef; color: #7d3c98; }
  .tag-gray   { background: #eaecee; color: #555; }
  .tag-orange { background: #fde8d8; color: #d35400; }

  /* CATEGORY ROWS */
  .cat-row { background: #fff; border-radius: 8px; padding: 12px 14px; margin-bottom: 10px; border-left: 5px solid; }
  .cat-row.red    { border-color: #c0392b; }
  .cat-row.green  { border-color: #1e8449; }
  .cat-row.blue   { border-color: #2471a3; }
  .cat-row.yellow { border-color: #f39c12; }
  .cat-row.purple { border-color: #7d3c98; }
  .cat-row.gray   { border-color: #6c757d; }
  .cat-row.teal   { border-color: #117a65; }
  .cat-row.orange { border-color: #d35400; }
  .cat-row.navy   { border-color: #1a1a2e; }
  .cat-row h4 { font-size: 13px; font-weight: 700; margin-bottom: 4px; }
  .cat-row .cat-count { font-size: 11px; font-weight: 700; float: right; }
  .cat-row p  { font-size: 12px; color: #444; margin: 2px 0; }

  /* DASHBOARD */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }
  .dash-tile { border-radius: 10px; padding: 14px 16px; }
  .dash-tile.red    { background: #fdf2f2; border: 1px solid #f5b7b1; }
  .dash-tile.yellow { background: #fefdf0; border: 1px solid #f9e79f; }
  .dash-tile.blue   { background: #eaf3fb; border: 1px solid #aed6f1; }
  .dash-tile.green  { background: #f0faf4; border: 1px solid #a9dfbf; }
  .dash-tile.purple { background: #f9f1ff; border: 1px solid #d7bde2; }
  .dash-tile.gray   { background: #f4f6f7; border: 1px solid #d5d8dc; }
  .dash-tile h4 { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 8px; }
  .dash-tile.red    h4 { color: #c0392b; }
  .dash-tile.yellow h4 { color: #b7770d; }
  .dash-tile.blue   h4 { color: #2471a3; }
  .dash-tile.green  h4 { color: #1e8449; }
  .dash-tile.purple h4 { color: #7d3c98; }
  .dash-tile.gray   h4 { color: #555; }
  .dash-tile ul { list-style: none; }
  .dash-tile ul li { font-size: 12px; color: #333; padding: 2px 0; border-bottom: 1px solid rgba(0,0,0,0.05); }
  .dash-tile ul li:last-child { border-bottom: none; }
  .dash-num { font-size: 28px; font-weight: 800; }

  /* PRIORITY TABLE */
  .pri-high   { color: #c0392b; font-weight: 700; }
  .pri-med    { color: #b7770d; font-weight: 700; }
  .pri-low    { color: #555; }

  /* TRASH */
  .trash-group { margin-bottom: 14px; }
  .trash-group h4 { font-size: 13px; font-weight: 700; margin-bottom: 6px; padding: 6px 10px; border-radius: 6px; }
  .trash-restore { background: #d4efdf; color: #1e8449; }
  .trash-review  { background: #fef9e7; color: #b7770d; }
  .trash-delete  { background: #fadbd8; color: #c0392b; }
  .trash-item { font-size: 12px; padding: 5px 10px; border-bottom: 1px solid #eee; }
  .trash-item:last-child { border-bottom: none; }

  /* TOP 3 */
  .top3 { counter-reset: top3; }
  .top3-item { display: flex; gap: 14px; align-items: flex-start; padding: 14px; border-radius: 10px; margin-bottom: 12px; }
  .top3-item:nth-child(1) { background: #fdf2f2; border: 2px solid #c0392b; }
  .top3-item:nth-child(2) { background: #f0faf4; border: 2px solid #1e8449; }
  .top3-item:nth-child(3) { background: #eaf3fb; border: 2px solid #2471a3; }
  .top3-num { font-size: 28px; font-weight: 900; min-width: 36px; line-height: 1; }
  .top3-item:nth-child(1) .top3-num { color: #c0392b; }
  .top3-item:nth-child(2) .top3-num { color: #1e8449; }
  .top3-item:nth-child(3) .top3-num { color: #2471a3; }
  .top3-item h3 { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
  .top3-item p  { font-size: 13px; color: #444; }

  /* MISC */
  .warn-box { background: #fdf2f2; border: 1px solid #f5b7b1; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #c0392b; margin-bottom: 12px; }
  .info-box  { background: #eaf3fb; border: 1px solid #aed6f1; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #2471a3; margin-bottom: 12px; }
  .note-box  { background: #fefdf0; border: 1px solid #f9e79f; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #7d6608; margin-bottom: 12px; }
  hr.divider { border: none; border-top: 1px solid #e0e0e0; margin: 18px 0; }
  .small-note { font-size: 11px; color: #888; margin-top: 6px; }
  a { color: #2471a3; text-decoration: none; }
  a:hover { text-decoration: underline; }
  .footer { text-align: center; color: #aaa; font-size: 11px; margin-top: 30px; padding-bottom: 20px; }
</style>
</head>
<body>
<div class="page-wrapper">

<!-- ══════════════════════════════════════════════════════
     1. HEADER
══════════════════════════════════════════════════════ -->
<div class="header-card">
  <div style="font-size:13px;color:#a8b4c8;text-transform:uppercase;letter-spacing:1.2px;margin-bottom:6px;">Executive Briefing</div>
  <h1>Good Morning, Melissa 👋</h1>
  <div class="subtitle">Wednesday, July 1, 2026 &nbsp;·&nbsp; Prepared by your Executive Chief of Staff</div>
  <div class="header-meta">
    <div class="header-meta-item"><div class="val">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="header-meta-item"><div class="val">6</div><div class="lbl">Calendar Events</div></div>
    <div class="header-meta-item"><div class="val">3</div><div class="lbl">Security / Risk Items</div></div>
    <div class="header-meta-item"><div class="val">5</div><div class="lbl">Job Leads Today</div></div>
    <div class="header-meta-item"><div class="val">2</div><div class="lbl">Events Today</div></div>
    <div class="header-meta-item"><div class="val">1</div><div class="lbl">Pending RSVP</div></div>
  </div>
</div>

<!-- ══════════════════════════════════════════════════════
     2. EXECUTIVE SUMMARY
══════════════════════════════════════════════════════ -->
<div class="section sec-navy">
  <div class="section-title">⚡ Executive Summary</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li class="risk"><strong>🔴 Biggest Risk:</strong> Three suspicious/phishing emails are sitting in your mailbox unread — a fake account-locked notice, a gambling sign-in request, and a fake iCloud storage alert. These are credential-harvest attempts. Do NOT click any links. Mark as spam and delete immediately.</li>
      <li class="oppty"><strong>🟢 Biggest Opportunity:</strong> Datadog sent an application status email for the Senior People Business Partner – NYC role; Legora also has a status update on the Senior People Partner, Finance role. Meanwhile, five new LinkedIn job alerts span VP-to-MD-level HR roles (up to $500K/yr). Your job search is active — review and prioritize today.</li>
      <li class="cal"><strong>🔵 Biggest Calendar Item:</strong> Your HR Networking &amp; Job Search Group Zoom meets TODAY at 12:00 PM – 1:30 PM ET and your RSVP status is still "needs action." Confirm attendance now. Also note: you have a FedEx package from Synergeyes Inc. arriving tomorrow (July 2).</li>
    </ul>
  </div>
</div>

<!-- ══════════════════════════════════════════════════════
     3. ACTION REQUIRED
══════════════════════════════════════════════════════ -->
<div class="section sec-red">
  <div class="section-title">🚨 Action Required</div>
  <div class="section-body">
    <div class="action-grid">

      <div class="action-card red">
        <div class="label">🔴 Security / Phishing</div>
        <h3>Fake "Account Locked" Email</h3>
        <div class="meta"><strong>From:</strong> melissaw212 &lt;rxlapamaenucmw…&gt;</div>
        <div class="meta"><strong>Why it matters:</strong> Spoofed your own username in a phishing attempt. Claims your account is locked and data will be deleted. Classic credential-harvest scam.</div>
        <div class="next">➡ Do NOT click. Mark spam. Delete. Block sender domain.</div>
        <div class="due">⏰ Act immediately</div>
      </div>

      <div class="action-card red">
        <div class="label">🔴 Security / Phishing</div>
        <h3>Fake "Sign In" – Gambling Bonus Scam</h3>
        <div class="meta"><strong>From:</strong> noreply@hg11-97601.firebaseapp.com</div>
        <div class="meta"><strong>Why it matters:</strong> Impersonates a sign-in confirmation for a casino bonus. Firebase subdomain abuse. Likely credential harvesting.</div>
        <div class="next">➡ Do NOT click. Mark spam. Delete immediately.</div>
        <div class="due">⏰ Act immediately</div>
      </div>

      <div class="action-card red">
        <div class="label">🔴 Security / Phishing</div>
        <h3>Fake "iCloud Storage Full" Alert</h3>
        <div class="meta"><strong>From:</strong> "melissaw212" &lt;melissaw212@ytyrfjuxccyas…&gt;</div>
        <div class="meta"><strong>Why it matters:</strong> Spoofs your own username again. Fake iCloud storage warning designed to steal Apple ID credentials.</div>
        <div class="next">➡ Do NOT click. Mark spam. Delete. Check Apple ID login history at appleid.apple.com.</div>
        <div class="due">⏰ Act immediately</div>
      </div>

      <div class="action-card yellow">
        <div class="label">🟡 RSVP Needed – TODAY</div>
        <h3>HR Networking &amp; Job Search Group Zoom</h3>
        <div class="meta"><strong>From:</strong> Google Calendar / HR Networking Group</div>
        <div class="meta"><strong>Why it matters:</strong> Starts TODAY at 12:00 PM ET. Status is "needs action." Large professional network – visibility matters during your search.</div>
        <div class="next">➡ Confirm or decline on calendar. If attending, prepare a 30-sec intro/update.</div>
        <div class="due">⏰ Today 12:00 PM ET</div>
      </div>

      <div class="action-card green">
        <div class="label">🟢 Job Search – Application Update</div>
        <h3>Datadog: Senior People Business Partner – NYC</h3>
        <div class="meta"><strong>From:</strong> Datadog Recruiting &lt;no-reply@recruiting.datadoghq.com&gt;</div>
        <div class="meta"><strong>Why it matters:</strong> Active application update — snippet suggests a thank-you/status communication. Could be advancement or rejection. Must read now.</div>
        <div class="next">➡ Open email, read status. If still active, prepare interview prep materials. If rejected, note and move on.</div>
        <div class="due">⏰ Today</div>
      </div>

      <div class="action-card green">
        <div class="label">🟢 Job Search – Application Update</div>
        <h3>Legora: Senior People Partner, Finance</h3>
        <div class="meta"><strong>From:</strong> Legora Recruiting Team &lt;no-reply@ashbyhq.com&gt;</div>
        <div class="meta"><strong>Why it matters:</strong> Application status update received. Snippet: "After…" – likely a decision. Unread and in inbox.</div>
        <div class="next">➡ Open email now. Determine if pass or rejection. If pass, respond promptly.</div>
        <div class="due">⏰ Today</div>
      </div>

      <div class="action-card green">
        <div class="label">🟢 Job Search – LinkedIn Message</div>
        <h3>Yurii Vlasenko messaged you on LinkedIn</h3>
        <div class="meta"><strong>From:</strong> LinkedIn messaging digest</div>
        <div class="meta"><strong>Why it matters:</strong> Unread LinkedIn message — may be a recruiter, connection, or opportunity. During active job search, response time matters.</div>
        <div class="next">➡ Log into LinkedIn and respond within 24 hours.</div>
        <div class="due">⏰ Today</div>
      </div>

      <div class="action-card yellow">
        <div class="label">🟡 Delivery – Tomorrow</div>
        <h3>FedEx Package from Synergeyes Inc. – Arriving Tomorrow</h3>
        <div class="meta"><strong>From:</strong> FedEx Delivery Manager</div>
        <div class="meta"><strong>Why it matters:</strong> Tracking #531895189723. Synergeyes makes specialty contact lenses — likely a medical/personal delivery. Scheduled for July 2.</div>
        <div class="next">➡ Confirm delivery address is correct. Plan to be available or arrange for package acceptance.</div>
        <div class="due">⏰ July 2, 2026</div>
      </div>

      <div class="action-card yellow">
        <div class="label">🟡 RSVP Needed – Tomorrow</div>
        <h3>HR Networking Open Office Hours Zoom – July 2</h3>
        <div class="meta"><strong>From:</strong> Google Calendar / HR Networking Group</div>
        <div class="meta"><strong>Why it matters:</strong> Status is "needs action." Open office hours for job search support — valuable during active search. 12:00–1:00 PM ET.</div>
        <div class="next">➡ Confirm or decline. Note: AI notetaking tools should be turned off per organizer request.</div>
        <div class="due">⏰ July 2, 12:00 PM ET</div>
      </div>

      <div class="action-card blue">
        <div class="label">🔵 Calendar – Declined</div>
        <h3>Executive Roundtable – July 2 (You Declined)</h3>
        <div class="meta"><strong>From:</strong> John Madigan (Zoom invite)</div>
        <div class="meta"><strong>Why it matters:</strong> You declined. If this was intentional, no action needed. If you want to attend, update your RSVP before tomorrow 9:00 AM.</div>
        <div class="next">➡ Verify this decline was intentional. If not, accept and prepare notes.</div>
        <div class="due">⏰ July 2, 9:00 AM ET</div>
      </div>

      <div class="action-card yellow">
        <div class="label">🟡 Billing Reminder</div>
        <h3>State Farm Bill Due – July 7</h3>
        <div class="meta"><strong>From:</strong> Google Calendar (self-entry)</div>
        <div class="meta"><strong>Why it matters:</strong> All-day calendar reminder for State Farm payment on July 7–8. Ensure payment is scheduled.</div>
        <div class="next">➡ Confirm payment is scheduled or pay now to avoid lapse.</div>
        <div class="due">⏰ July 7, 2026</div>
      </div>

      <div class="action-card blue">
        <div class="label">🔵 Medical / Personal</div>
        <h3>PT Appointment – July 7</h3>
        <div class="meta"><strong>From:</strong> Google Calendar (self-entry)</div>
        <div class="meta"><strong>Why it matters:</strong> Physical therapy session 12:00–1:00 PM on July 7. No location noted.</div>
        <div class="next">➡ Confirm appointment location and any prep needed. Block travel time.</div>
        <div class="due">⏰ July 7, 2026</div>
      </div>

    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════════════════
     4. FULL 7-DAY CALENDAR
══════════════════════════════════════════════════════ -->
<div class="section sec-blue">
  <div class="section-title">📅 Full 7-Day Calendar (July 1–7, 2026)</div>
  <div class="section-body">

    <!-- July 1 -->
    <div class="cal-day">
      <div class="cal-day-header">Wednesday, July 1, 2026 — TODAY</div>

      <div class="cal-event needs-action">
        <h4>HR Networking &amp; Job Search Group – Zoom 2</h4>
        <div class="cal-meta">🕛 12:00 PM – 1:30 PM ET</div>
        <div class="cal-meta">📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a></div>
        <div class="cal-meta">👥 Large group (~175+ HR professionals in job search)</div>
        <div class="cal-meta">📋 <strong>Prep:</strong> Prepare a brief professional update/intro. Review team guidelines linked in the invite description. Confirm your 30-second pitch.</div>
        <div class="cal-meta">⚠️ <strong>Note:</strong> Duplicate event "Network" also shows 12:00–1:30 PM as confirmed — likely the same session with a simpler title. Confirm you are not double-booked.</div>
        <span class="cal-badge badge-needs">⚠ RSVP: Needs Action</span>
      </div>

      <div class="cal-event">
        <h4>Network (Personal Block)</h4>
        <div class="cal-meta">🕛 12:00 PM – 1:30 PM ET</div>
        <div class="cal-meta">📍 No location specified</div>
        <div class="cal-meta">📋 <strong>Prep:</strong> Likely mirrors the HR Networking Zoom above. Appears to be a self-created confirmation block.</div>
        <div class="cal-meta">⚠️ <strong>Conflict Warning:</strong> Overlaps with the HR Networking Zoom. Likely same event — verify no true conflict exists.</div>
        <span class="cal-badge badge-confirmed">✅ Confirmed</span>
      </div>
    </div>

    <!-- July 2 -->
    <div class="cal-day">
      <div class="cal-day-header">Thursday, July 2, 2026</div>

      <div class="cal-event declined">
        <h4>Executive Roundtable (John Madigan – Zoom)</h4>
        <div class="cal-meta">🕘 9:00 AM – 10:30 AM ET</div>
        <div class="cal-meta">📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> | Meeting ID: 207 786 667 | PW: 205454</div>
        <div class="cal-meta">📋 <strong>Prep:</strong> N/A – you declined. Verify this was intentional.</div>
        <div class="cal-meta">⚠️ <strong>Note:</strong> If this is a professional networking or leadership event, reconsider. Re-accepting while in active job search could be valuable.</div>
        <span class="cal-badge badge-declined">❌ Declined</span>
      </div>

      <div class="cal-event needs-action">
        <h4>HR Networking &amp; Job Search: Open Office Hours – Zoom 2</h4>
        <div class="cal-meta">🕛 12:00 PM – 1:00 PM ET</div>
        <div class="cal-meta">📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a></div>
        <div class="cal-meta">👥 Same large HR networking group</div>
        <div class="cal-meta">📋 <strong>Prep:</strong> Open discussion format. No AI notetaking tools per organizer. Come prepared with questions or job search challenges to discuss.</div>
        <div class="cal-meta">⚠️ <strong>Note:</strong> No conflict with Executive Roundtable (different times). Both can be attended if Roundtable is re-accepted.</div>
        <span class="cal-badge badge-needs">⚠ RSVP: Needs Action</span>
      </div>

      <div class="cal-event">
        <h4>📦 FedEx Delivery – Synergeyes Inc. (Expected)</h4>
        <div class="cal-meta">📋 Tracking #531895189723 arriving today</div>
        <div class="cal-meta">📋 Specialty contact lens company — likely a personal medical delivery</div>
        <span class="cal-badge badge-confirmed">📦 Delivery</span>
      </div>
    </div>

    <!-- July 3 -->
    <div class="cal-day">
      <div class="cal-day-header">Friday, July 3, 2026</div>
      <div class="cal-event" style="background:#f4f6f7; border-color:#aaa;">
        <h4>No Events Scheduled</h4>
        <div class="cal-meta">Pre-holiday Friday. Use for job search follow-up, application prep, or rest before the long weekend.</div>
      </div>
    </div>

    <!-- July 4 -->
    <div class="cal-day">
      <div class="cal-day-header">Saturday, July 4, 2026 — Independence Day 🇺🇸</div>
      <div class="cal-event" style="background:#f9f1ff; border-color:#7d3c98;">
        <h4>🇺🇸 Independence Day – Federal Holiday</h4>
        <div class="cal-meta">No events scheduled. Recruiters and hiring teams offline. Good day to rest and recharge.</div>
      </div>
    </div>

    <!-- July 5 -->
    <div class="cal-day">
      <div class="cal-day-header">Sunday, July 5, 2026</div>
      <div class="cal-event" style="background:#f4f6f7; border-color:#aaa;">
        <h4>No Events Scheduled</h4>
        <div class="cal-meta">Post-holiday Sunday. Prepare for the week ahead — review job leads, draft follow-up emails.</div>
      </div>
    </div>

    <!-- July 6 -->
    <div class="cal-day">
      <div class="cal-day-header">Monday, July 6, 2026</div>
      <div class="cal-event" style="background:#f4f6f7; border-color:#aaa;">
        <h4>No Events Scheduled</h4>
        <div class="cal-meta">First business day back after the holiday weekend. Expect recruiter activity to resume. Check email early.</div>
      </div>
    </div>

    <!-- July 7 -->
    <div class="cal-day">
      <div class="cal-day-header">Tuesday, July 7, 2026</div>

      <div class="cal-event allday">
        <h4>💳 State Farm Bill Due</h4>
        <div class="cal-meta">📅 All-day reminder</div>
        <div class="cal-meta">📋 <strong>Prep:</strong> Confirm payment is scheduled or pay now. Insurance lapse risk.</div>
        <span class="cal-badge badge-allday">📅 All Day</span>
      </div>

      <div class="cal-event">
        <h4>🏥 PT (Physical Therapy)</h4>
        <div class="cal-meta">🕛 12:00 PM – 1:00 PM ET</div>
        <div class="cal-meta">📍 No location specified — confirm appointment address</div>
        <div class="cal-meta">📋 <strong>Prep:</strong> Add location. Block travel time before and after. Wear appropriate clothing.</div>
        <span class="cal-badge badge-confirmed">✅ Confirmed</span>
      </div>
    </div>

  </div>
</div>

<!-- ══════════════════════════════════════════════════════
     5. JOB SEARCH & INTERVIEW PIPELINE
══════════════════════════════════════════════════════ -->
<div class="section sec-green">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">
    <div class="note-box">Active search is generating strong signal. Multiple high-level roles surfaced today. Prioritize Datadog and Legora status checks, then review new alerts.</div>
    <table>
      <thead>
        <tr>
          <th>Source</th>
          <th>Role / Company</th>
          <th>Status</th>
          <th>Salary Signal</th>
          <th>Fit</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="tag tag-green">Recruiter Email</span></td>
          <td><strong>Senior People Business Partner – NYC</strong><br>Datadog</td>
          <td>Application status update (unread)</td>
          <td>Competitive (Datadog scale)</td>
          <td><span class="tag tag-high">HIGH</span></td>
          <td>Open email NOW. Determine next step.</td>
        </tr>
        <tr>
          <td><span class="tag tag-green">Recruiter Email</span></td>
          <td><strong>Senior People Partner, Finance</strong><br>Legora</td>
          <td>Application update – likely decision</td>
          <td>Not specified</td>
          <td><span class="tag tag-high">HIGH</span></td>
          <td>Open email. Respond if still active.</td>
        </tr>
        <tr>
          <td><span class="tag tag-blue">LinkedIn Alert</span></td>
          <td><strong>Managing Director, Human Capital – Equity</strong><br>Ladders</td>
          <td>New alert (unread) – posted 6/29</td>
          <td>Up to $500K/yr</td>
          <td><span class="tag tag-high">HIGH</span></td>
          <td>Review and apply if aligned. Posted 6/29 — move quickly.</td>
        </tr>
        <tr>
          <td><span class="tag tag-blue">LinkedIn Alert</span></td>
          <td><strong>VP of People</strong><br>Nitra</td>
          <td>New alert (unread) – posted 6/29</td>
          <td>Not specified</td>
          <td><span class="tag tag-high">HIGH</span></td>
          <td>Research Nitra. Apply if aligned.</td>
        </tr>
        <tr>
          <td><span class="tag tag-blue">LinkedIn Alert</span></td>
          <td><strong>Sr Human Resources Director</strong><br>Confidential</td>
          <td>New alert (unread) – posted 6/28</td>
          <td>Up to $350K/yr</td>
          <td><span class="tag tag-high">HIGH</span></td>
          <td>Review. Confidential listings often mean active urgency.</td>
        </tr>
        <tr>
          <td><span class="tag tag-blue">LinkedIn Alert</span></td>
          <td><strong>Senior HR Business Partner</strong><br>K Health</td>
          <td>New alert (unread) – posted 6/29</td>
          <td>Not specified</td>
          <td><span class="tag tag-med">MED</span></td>
          <td>Tech-adjacent health company. Review fit for HRBP scope.</td>
        </tr>
        <tr>
          <td><span class="tag tag-blue">LinkedIn Jobs</span></td>
          <td><strong>Head of People Operations (Similar Roles)</strong><br>LinkedIn Algorithm Suggestions</td>
          <td>Multiple similar roles surfaced</td>
          <td>Varies</td>
          <td><span class="tag tag-med">MED</span></td>
          <td>Scan list. Shortlist 1–2 additional applications.</td>
        </tr>
        <tr>
          <td><span class="tag tag-purple">SHRM</span></td>
          <td><strong>32 New Human Resources Jobs</strong><br>SHRM HR Jobs Board</td>
          <td>New digest (unread)</td>
          <td>Varies</td>
          <td><span class="tag tag-med">MED</span></td>
          <td>Scan digest for senior-level matches. Don't spend more than 15 min.</td>
        </tr>
        <tr>
          <td><span class="tag tag-green">Scovai</span></td>
          <td><strong>Chief People and Culture Officer</strong><br>Omnisage LLC</td>
          <td>Matched and waiting on profile</td>
          <td>Not specified</td>
          <td><span class="tag tag-med">MED</span></td>
          <td>Review Omnisage. If aligned, respond via Scovai platform.</td>
        </tr>
        <tr>
          <td><span class="tag tag-blue">LinkedIn Message</span></td>
          <td><strong>Message from Yurii Vlasenko</strong><br>LinkedIn DM</td>
          <td>Unread – 1 message awaiting response</td>
          <td>Unknown</td>
          <td><span class="tag tag-med">MED</span></td>
          <td>Log in and respond. Could be recruiter or referral.</td>
        </tr>
        <tr>
          <td><span class="tag tag-purple">Calendar</span></td>
          <td><strong>HR Networking &amp; Job Search Group Zoom</strong><br>Large HR Community</td>
          <td>TODAY 12:00 PM – RSVP needed</td>
          <td>N/A – Networking</td>
          <td><span class="tag tag-high">HIGH</span></td>
          <td>Confirm and attend. 175+ HR peers = referral opportunity.</td>
        </tr>
        <tr>
          <td><span class="tag tag-purple">Calendar</span></td>
          <td><strong>HR Networking Open Office Hours</strong><br>Same HR Community</td>
          <td>July 2, 12:00 PM – RSVP needed</td>
          <td>N/A – Networking</td>
          <td><span class="tag tag-med">MED</span></td>
          <td>Confirm. Bring specific job search challenges.</td>
        </tr>
      </tbody>
    </table>
    <div class="small-note">Citizens Careers job alert (not inbox/unread) noted – review separately when time permits.</div>
  </div>
</div>

<!-- ══════════════════════════════════════════════════════
     6. FULL EMAIL REVIEW BY CATEGORY
══════════════════════════════════════════════════════ -->
<div class="section sec-navy">
  <div class="section-title">📧 Full Email Review by Category</div>
  <div class="section-body">

    <!-- Security / Risk -->
    <div class="cat-row red">
      <h4>🔴 Security / Risk <span class="cat-count">3 emails</span></h4>
      <p><strong>Senders:</strong> melissaw212@rxlapamaenucmw… (fake account lock) | noreply@hg11-97601.firebaseapp.com (gambling sign-in) | melissaw212@ytyrfjuxccyas… (fake iCloud storage)</p>
      <p><strong>Summary:</strong> All three are phishing/spam using your username or spoofed addresses. Classic social engineering: urgency, fear of data loss, fake account alerts.</p>
      <p><strong>Action:</strong> Do NOT click any links. Mark as phishing/spam. Delete. Consider running a password audit if you have clicked any links from similar emails recently.</p>
    </div>

    <!-- Job Search -->
    <div class="cat-row green">
      <h4>🟢 Job Search – Applications &amp; Recruiter Updates <span class="cat-count">2 emails</span></h4>
      <p><strong>Senders:</strong> Datadog Recruiting (Senior People Business Partner – NYC status) | Legora Recruiting Team (Senior People Partner, Finance status)</p>
      <p><strong>Summary:</strong> Two active applications with status updates received today. Datadog is unread/inbox. Legora is read/inbox. Both require immediate attention to determine pipeline status.</p>
      <p><strong>Action:</strong> Read both. Respond to any requests within 24 hours. Log outcomes in your job search tracker.</p>
    </div>

    <!-- Job Alerts & LinkedIn -->
    <div class="cat-row green">
      <h4>🟢 Job Alerts &amp; LinkedIn Notifications <span class="cat-count">6 emails</span></h4>
      <p><strong>Senders:</strong> LinkedIn Job Alerts (Managing Director Human Capital – up to $500K | VP of People at Nitra | Sr HR Director Confidential – up to $350K | Sr HRBP at K Health) | LinkedIn Jobs (Head of People Operations similar roles) | SHRM HR Jobs (32 new HR jobs)</p>
      <p><strong>Summary:</strong> Strong batch of senior HR roles across tech, health, and equity sectors. Several at VP/Director/MD level with strong compensation signals.</p>
      <p><strong>Action:</strong> Prioritize MD Human Capital ($500K), VP People (Nitra), and Sr HR Director ($350K). Apply to top 2–3 today.</p>
    </div>

    <!-- Recruiters / Networking -->
    <div class="cat-row green">
      <h4>🟢 Recruiters / Networking Messages <span class="cat-count">1 email</span></h4>
      <p><strong>Senders:</strong> Yurii Vlasenko via LinkedIn (1 new message)</p>
      <p><strong>Summary:</strong> Unread LinkedIn message. Unknown context — could be recruiter, peer, or referral source.</p>
      <p><strong>Action:</strong> Log into LinkedIn and respond today.</p>
    </div>

    <!-- Calendar / Events -->
    <div class="cat-row blue">
      <h4>🔵 Calendar / Events <span class="cat-count">0 direct emails</span></h4>
      <p><strong>Note:</strong> All calendar items handled via Google Calendar data above. No standalone calendar invite emails in this batch beyond what is captured in the calendar section.</p>
      <p><strong>Action:</strong> See Full 7-Day Calendar section.</p>
    </div>

    <!-- Medical / Health -->
    <div class="cat-row teal">
      <h4>🩺 Medical / Health <span class="cat-count">2 emails</span></h4>
      <p><strong>Senders:</strong> FedEx (Synergeyes Inc. delivery – contact lens company, arriving July 2) | HealthEquity (exclusive lab testing pricing – in trash)</p>
      <p><strong>Summary:</strong> FedEx delivery is actionable. HealthEquity promo is low priority and in trash.</p>
      <p><strong>Action:</strong> Monitor FedEx delivery for July 2. HealthEquity email can remain in trash.</p>
    </div>

    <!-- Financial / Billing -->
    <div class="cat-row yellow">
      <h4>🟡 Financial / Billing <span class="cat-count">3 emails</span></h4>
      <p><strong>Senders:</strong> Robinhood (trade confirmations available) | SmartMoney Minute (irrevocable trusts / estate planning) | The Average Joe (H1 market recap)</p>
      <p><strong>Summary:</strong> Robinhood trade confirmations should be reviewed for accuracy. SmartMoney estate planning content is worth saving for reference. Average Joe is a market newsletter (read or archive).</p>
      <p><strong>Action:</strong> Review Robinhood trade confirmations. Save SmartMoney article if estate planning is on your radar.</p>
    </div>

    <!-- Professional Development -->
    <div class="cat-row purple">
      <h4>🟣 Professional Development <span class="cat-count">3 emails</span></h4>
      <p><strong>Senders:</strong> AI For Leaders (AI work review burden – in trash) | The HR AI Guy (AI &amp; Labor Law research – unread/inbox) | Medium Daily Digest (7 AI models to download free)</p>
      <p><strong>Summary:</strong> The HR AI Guy article on multi-state employment law AI research is highly relevant for a senior HR exec. The others are supplemental.</p>
      <p><strong>Action:</strong> Read The HR AI Guy article today. AI For Leaders is in trash — review or delete. Medium digest can be skimmed or archived.</p>
    </div>

    <!-- Personal -->
    <div class="cat-row navy">
      <h4>⚫ Personal <span class="cat-count">4 emails</span></h4>
      <p><strong>Senders:</strong> Match.com ("Bill likes you") | OkCupid ("Someone likes you") | HomeAgain PetRescuers (lost cat Tovah near Brooklyn) | USPS Informed Delivery (0 mailpieces, 2 packages)</p>
      <p><strong>Summary:</strong> Dating app notifications are low-urgency personal items. HomeAgain lost pet alert (Tovah, near Breeze Hill Dr/E Lake Dr, Brooklyn) is FYI if you're a pet owner or neighbor. USPS confirms 2 inbound packages (one likely the Synergeyes from FedEx).</p>
      <p><strong>Action:</strong> Address dating app notifications at your leisure. Note lost pet alert if you're in the area. USPS digest is FYI only.</p>
    </div>

    <!-- Newsletters / Subscriptions -->
    <div class="cat-row purple">
      <h4>🟣 Newsletters &amp; Subscriptions <span class="cat-count">7 emails</span></h4>
      <p><strong>Senders:</strong> TLDR Crypto (UK crypto framework, OpenUSD, SharpLink ETH) | TLDR Main (Claude Sonnet 5, Meta Kalshi, Fable) [x2 — duplicate send] | The Hustle (3D-printed smiles / FIFA ban) | 1% Better (Boomer Debt / boring wealth path) | The Daily Skimm (July 1 edition) | CoolDeep AI (Cowork vs. Claude chat)</p>
      <p><strong>Summary:</strong> Tech/crypto/business newsletters. TLDR sent a duplicate (both in and out of inbox). The Hustle is in trash. 1% Better and Daily Skimm are read.</p>
      <p><strong>Action:</strong> Skim TLDR and TLDR Crypto for relevant AI/crypto headlines. The Hustle (trash) can be deleted. De-duplicate TLDR.</p>
    </div>

    <!-- Nonprofit / Community -->
    <div class="cat-row teal">
      <h4>🌿 Nonprofit / Community <span class="cat-count">1 email</span></h4>
      <p><strong>Senders:</strong> Voters For Animal Rights / Julie Cappiello ("We need 100 people" – Animal Voter Collective launch)</p>
      <p><strong>Summary:</strong> Animal rights advocacy organization celebrating 10 years. Recruiting 100 founding members for the Animal Voter Collective. Unread, in inbox.</p>
      <p><strong>Action:</strong> Review if this aligns with your values/interests. Respond or archive.</p>
    </div>

    <!-- Promotional / Retail -->
    <div class="cat-row gray">
      <h4>⬜ Promotional / Retail <span class="cat-count">12 emails</span></h4>
      <p><strong>Senders:</strong> Zappos (HOKA Clifton 11) | Gap Factory (4th of July Sale + $25 shorts) [x2] | SHEIN (12% off cart + new sportswear) [x2] | Kohl's (20% off + Kohl's Cash) | Chewy ($5 off app order) | Amazon Business (limited-time deals) | Mercedes-Benz of Manhattan (maintenance offer – addressed "Marvin") | TrimRx (GLP-1 weight loss – suspicious domain)</p>
      <p><strong>Summary:</strong> Mostly routine retail promotions. Mercedes email is addressed to "Marvin" — misdirected or spam. TrimRx uses a suspicious sending domain — treat with caution. Amazon Business deal is in trash.</p>
      <p><strong>Action:</strong> Ignore most. Review Gap/Zappos/Kohl's if you need summer clothing. Delete Mercedes (wrong name). Mark TrimRx suspicious.</p>
    </div>

    <!-- Safe to Delete / Ignore -->
    <div class="cat-row gray">
      <h4>⬜ Safe to Delete / Ignore <span class="cat-count">6 emails</span></h4>
      <p><strong>Senders:</strong> Render (privacy policy update – routine, no action needed) | Lisa Rangel/Chameleon Resumes (resume coaching sales pitch – trash) | LigoSocial (fake LinkedIn expiry warning – trash) | Alison Courses (AI CV upgrade ad – trash) | Dr. Gazala Shaikh / Medium (Doctor's Day article – trash) | Medium Daily Digest (ROS 2 robotics article – trash, not relevant to Melissa)</p>
      <p><strong>Summary:</strong> Routine policy notices, sales pitches, and irrelevant content. All can be deleted without review.</p>
      <p><strong>Action:</strong> Delete / archive. No response required.</p>
    </div>

  </div>
</div>

<!-- ══════════════════════════════════════════════════════
     7. TRASH REVIEW
══════════════════════════════════════════════════════ -->
<div class="section sec-red">
  <div class="section-title">🗑️ Trash Review (8 emails found in Trash)</div>
  <div class="section-body">

    <div class="trash-group">
      <h4 class="trash-restore">✅ RESTORE – Worth Keeping / Action Needed</h4>
      <div style="background:#fff;border-radius:8px;padding:8px 12px;">
        <div class="trash-item"><strong>HealthEquity – "Get a deeper view of your health for only $325"</strong><br>From: HealthEquity@e.healthequity.com | Exclusive lab testing pricing (160+ tests via Function Health) for HealthEquity members. If you have a HealthEquity HSA/FSA account, this may be a legitimate member benefit worth reviewing. <span class="tag tag-green">Restore &amp; Review</span></div>
      </div>
    </div>

    <div class="trash-group">
      <h4 class="trash-review">⚠️ REVIEW BEFORE DELETING – May Have Value</h4>
      <div style="background:#fff;border-radius:8px;padding:8px 12px;">
        <div class="trash-item"><strong>AI For Leaders – "AI Work Is Easy to Create, Hard to Review"</strong><br>From: team@aiforleaders.com | Newsletter about AI workload burden on conscientious employees. Relevant to HR leaders managing AI adoption. Quick read — restore if interested in AI leadership topics. <span class="tag tag-blue">Restore &amp; Skim</span></div>
        <div class="trash-item"><strong>The Hustle – "🦷 3D-printed smiles"</strong><br>From: news@thehustle.co | Business/tech newsletter. 3D dental innovation + FIFA branding ban. Low urgency but occasionally useful for exec awareness. <span class="tag tag-gray">OK to Delete</span></div>
        <div class="trash-item"><strong>Amazon Business – "Top deals for business"</strong><br>From: no-reply@business.amazon.com | Standard Amazon Business deals email. Only worth restoring if you have active business supply needs. <span class="tag tag-gray">OK to Delete</span></div>
      </div>
    </div>

    <div class="trash-group">
      <h4 class="trash-delete">🗑️ SAFE TO DELETE – Spam, Promotions, Irrelevant</h4>
      <div style="background:#fff;border-radius:8px;padding:8px 12px;">
        <div class="trash-item"><strong>Lisa Rangel / Chameleon Resumes – "Why summer is the worst time to pause"</strong><br>Sales email targeting job seekers. No unique value — generic resume coach marketing. <span class="tag tag-red">Delete</span></div>
        <div class="trash-item"><strong>LigoSocial – "LinkedIn Connection Expiring Soon"</strong><br>Fake urgency from a LinkedIn connection service. Likely spam/dark-pattern marketing. Not a real LinkedIn notification. <span class="tag tag-red">Delete + Block</span></div>
        <div class="trash-item"><strong>Dr. Gazala Shaikh via Medium – "Before You Wish Your Doctor Happy Doctor's Day"</strong><br>Medium subscription article — unrelated to Melissa's interests, sent to a secondary Medium account profile (Amylw). Irrelevant. <span class="tag tag-red">Delete</span></div>
        <div class="trash-item"><strong>Alison Courses – "Your CV could use an AI upgrade"</strong><br>Course platform marketing email. Generic AI/career upskilling pitch. No specific value at Melissa's level. <span class="tag tag-red">Delete</span></div>
        <div class="trash-item"><strong>Medium Daily Digest (ROS 2 / Robotics) – "Making Your State Estimator ROS 2 Compliant"</strong><br>Robotics/engineering content delivered to a secondary Medium profile (Amylw). Completely irrelevant to Melissa. <span class="tag tag-red">Delete</span></div>
      </div>
    </div>

  </div>
</div>

<!-- ══════════════════════════════════════════════════════
     8. PROMOTIONAL / RETAIL SUMMARY
══════════════════════════════════════════════════════ -->
<div class="section sec-gray">
  <div class="section-title">🛍️ Promotional / Retail Summary</div>
  <div class="section-body">
    <table>
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
          <td>Zappos</td>
          <td>1</td>
          <td>HOKA Clifton 11 just dropped</td>
          <td><span class="tag tag-gray">Review if need running shoes</span></td>
        </tr>
        <tr>
          <td>Gap Factory</td>
          <td>2</td>
          <td>4th of July Sale (50–70% off) + $25 shorts / extra 15% off</td>
          <td><span class="tag tag-gray">Review if need summer clothing</span></td>
        </tr>
        <tr>
          <td>SHEIN</td>
          <td>2</td>
          <td>12% off cart + new sportswear arrivals</td>
          <td><span class="tag tag-gray">Ignore / Delete</span></td>
        </tr>
        <tr>
          <td>Kohl's</td>
          <td>1</td>
          <td>20% off with code GOSHOP20 + up to 70% off clearance</td>
          <td><span class="tag tag-gray">Review if need basics</span></td>
        </tr>
        <tr>
          <td>Chewy</td>
          <td>1</td>
          <td>$5 off first app order</td>
          <td><span class="tag tag-gray">Keep if you have pets</span></td>
        </tr>
        <tr>
          <td>Amazon Business</td>
          <td>1</td>
          <td>Limited-time business deals (in trash)</td>
          <td><span class="tag tag-red">Delete – already in trash</span></td>
        </tr>
        <tr>
          <td>Mercedes-Benz of Manhattan</td>
          <td>1</td>
          <td>Maintenance offer
<hr>
<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Financial / Billing</td><td>1</td></tr>
<tr><td>Job Search / Recruiters</td><td>14</td></tr>
<tr><td>Medical / Health</td><td>2</td></tr>
<tr><td>Other / Review</td><td>19</td></tr>
<tr><td>Professional Development / Newsletters</td><td>3</td></tr>
<tr><td>Promotional / Retail</td><td>7</td></tr>
<tr><td>Security / Risk</td><td>4</td></tr>
</table>
<p><strong>Audit Note:</strong> Every fetched email was reviewed and assigned to one category. Trash emails were included in review. Promotional and low-value emails were accounted for but deprioritized.</p>

