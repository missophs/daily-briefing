<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Melissa's Executive Briefing — Wednesday, June 3, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* Header */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 16px; padding: 36px 40px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 1px; }
  .header .sub { font-size: 15px; color: #a8c8ff; margin-top: 6px; }
  .header .meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.1); border-radius: 10px; padding: 10px 20px; text-align: center; }
  .header .meta-item .num { font-size: 26px; font-weight: 700; color: #7dd3fc; }
  .header .meta-item .label { font-size: 11px; color: #cbd5e1; text-transform: uppercase; letter-spacing: 1px; }

  /* Section titles */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 10px 18px; border-radius: 8px 8px 0 0; margin-bottom: 0; }

  /* Color themes */
  .red    { background: #fee2e2; border-left: 5px solid #dc2626; }
  .red .section-title    { background: #dc2626; color: #fff; }
  .yellow { background: #fef9c3; border-left: 5px solid #ca8a04; }
  .yellow .section-title { background: #ca8a04; color: #fff; }
  .blue   { background: #dbeafe; border-left: 5px solid #2563eb; }
  .blue .section-title   { background: #2563eb; color: #fff; }
  .green  { background: #dcfce7; border-left: 5px solid #16a34a; }
  .green .section-title  { background: #16a34a; color: #fff; }
  .purple { background: #f3e8ff; border-left: 5px solid #7c3aed; }
  .purple .section-title { background: #7c3aed; color: #fff; }
  .gray   { background: #f1f5f9; border-left: 5px solid #94a3b8; }
  .gray .section-title   { background: #64748b; color: #fff; }
  .orange { background: #fff7ed; border-left: 5px solid #ea580c; }
  .orange .section-title { background: #ea580c; color: #fff; }

  .section-body { padding: 16px 20px; border-radius: 0 0 8px 8px; }
  .section-wrapper { border-radius: 8px; overflow: hidden; margin-bottom: 20px; }

  /* Cards */
  .card { background: #fff; border-radius: 10px; padding: 14px 18px; margin-bottom: 12px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
  .card-label { display: inline-block; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; padding: 2px 8px; border-radius: 20px; margin-bottom: 6px; }
  .label-red    { background: #fca5a5; color: #7f1d1d; }
  .label-yellow { background: #fde68a; color: #78350f; }
  .label-blue   { background: #93c5fd; color: #1e3a5f; }
  .label-green  { background: #86efac; color: #14532d; }
  .label-purple { background: #c4b5fd; color: #3b0764; }
  .label-gray   { background: #cbd5e1; color: #334155; }
  .label-orange { background: #fdba74; color: #7c2d12; }

  .card h3 { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
  .card .meta-row { display: flex; flex-wrap: wrap; gap: 16px; font-size: 12px; color: #555; margin: 6px 0; }
  .card .meta-row span strong { color: #222; }
  .card p { font-size: 13px; color: #444; margin: 4px 0; }
  .card .action { background: #f0fdf4; border-left: 3px solid #16a34a; padding: 6px 10px; border-radius: 4px; font-size: 12px; margin-top: 8px; color: #166534; }
  .card .warning { background: #fff7ed; border-left: 3px solid #ea580c; padding: 6px 10px; border-radius: 4px; font-size: 12px; margin-top: 6px; color: #9a3412; }

  /* Executive Summary bullets */
  .exec-bullet { display: flex; align-items: flex-start; gap: 12px; padding: 12px 0; border-bottom: 1px solid #e5e7eb; }
  .exec-bullet:last-child { border-bottom: none; }
  .exec-icon { font-size: 22px; min-width: 32px; }
  .exec-text strong { display: block; font-size: 13px; font-weight: 700; }
  .exec-text span { font-size: 12px; color: #555; }

  /* Tables */
  table { width: 100%; border-collapse: collapse; font-size: 13px; margin-top: 8px; }
  th { background: #1e293b; color: #fff; padding: 9px 12px; text-align: left; font-size: 11px; text-transform: uppercase; letter-spacing: 0.8px; }
  td { padding: 8px 12px; border-bottom: 1px solid #e5e7eb; vertical-align: top; }
  tr:nth-child(even) td { background: #f8fafc; }
  tr:hover td { background: #f1f5f9; }

  /* Priority badges */
  .pri-high   { background: #fca5a5; color: #7f1d1d; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 700; }
  .pri-med    { background: #fde68a; color: #78350f; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 700; }
  .pri-low    { background: #bbf7d0; color: #14532d; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 700; }

  /* Status badges */
  .status-confirmed  { background: #dcfce7; color: #166534; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 600; }
  .status-declined   { background: #fee2e2; color: #7f1d1d; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 600; }
  .status-pending    { background: #fef9c3; color: #854d0e; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 600; }
  .status-accepted   { background: #dbeafe; color: #1e3a5f; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 600; }

  /* Fit badges */
  .fit-high { background: #4ade80; color: #14532d; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 700; }
  .fit-med  { background: #93c5fd; color: #1e3a5f; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 700; }
  .fit-low  { background: #e2e8f0; color: #475569; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 700; }

  /* Dashboard grid */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-tile { background: #fff; border-radius: 10px; padding: 16px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); text-align: center; }
  .dash-tile .dt-num { font-size: 32px; font-weight: 800; }
  .dash-tile .dt-label { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #64748b; margin-top: 4px; }
  .dash-tile.dt-red    .dt-num { color: #dc2626; }
  .dash-tile.dt-yellow .dt-num { color: #ca8a04; }
  .dash-tile.dt-blue   .dt-num { color: #2563eb; }
  .dash-tile.dt-green  .dt-num { color: #16a34a; }
  .dash-tile.dt-purple .dt-num { color: #7c3aed; }
  .dash-tile.dt-gray   .dt-num { color: #64748b; }

  /* Trash groups */
  .trash-group { background: #fff; border-radius: 8px; padding: 12px 16px; margin-bottom: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.07); }
  .trash-group h4 { font-size: 13px; font-weight: 700; margin-bottom: 6px; }
  .trash-restore  h4 { color: #16a34a; }
  .trash-review   h4 { color: #ca8a04; }
  .trash-delete   h4 { color: #94a3b8; }

  /* Top 3 */
  .top3 { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; }
  .top3-item { background: #fff; border-radius: 12px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
  .top3-item .num { font-size: 40px; font-weight: 900; color: #e2e8f0; line-height: 1; }
  .top3-item h3 { font-size: 15px; font-weight: 700; margin: 6px 0 4px; }
  .top3-item p { font-size: 12px; color: #64748b; }

  /* Day block */
  .day-block { background: #fff; border-radius: 10px; padding: 14px 18px; margin-bottom: 14px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
  .day-title { font-size: 14px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; color: #1e293b; margin-bottom: 10px; border-bottom: 2px solid #e2e8f0; padding-bottom: 6px; }
  .event-row { display: flex; flex-wrap: wrap; gap: 10px; align-items: flex-start; padding: 8px 0; border-bottom: 1px dashed #e5e7eb; }
  .event-row:last-child { border-bottom: none; }
  .event-time { font-weight: 700; font-size: 12px; color: #2563eb; min-width: 90px; }
  .event-details { flex: 1; }
  .event-details strong { font-size: 13px; }
  .event-details .ev-meta { font-size: 11px; color: #64748b; margin-top: 2px; }

  /* Promo table */
  .promo-item { display: flex; flex-wrap: wrap; align-items: center; gap: 10px; padding: 8px 0; border-bottom: 1px dashed #e5e7eb; font-size: 13px; }
  .promo-item:last-child { border-bottom: none; }
  .promo-brand { font-weight: 700; min-width: 130px; }
  .promo-subject { color: #555; flex: 1; }
  .rec-delete  { background: #fee2e2; color: #7f1d1d; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 600; }
  .rec-review  { background: #fef9c3; color: #854d0e; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 600; }
  .rec-keep    { background: #dcfce7; color: #166534; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 600; }
  .rec-ignore  { background: #f1f5f9; color: #475569; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 600; }
  .rec-unsub   { background: #f3e8ff; color: #5b21b6; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 600; }

  a { color: #2563eb; text-decoration: none; }
  a:hover { text-decoration: underline; }
  .small { font-size: 11px; color: #64748b; }
  ul { padding-left: 18px; }
  ul li { margin-bottom: 4px; font-size: 13px; }
  .conflict-warn { background: #fef3c7; border: 1px solid #f59e0b; border-radius: 6px; padding: 4px 10px; font-size: 11px; color: #92400e; margin-top: 4px; display: inline-block; }
  hr { border: none; border-top: 1px solid #e2e8f0; margin: 14px 0; }
  .footer { text-align: center; color: #94a3b8; font-size: 11px; padding: 20px 0; }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════ HEADER ═══ -->
<div class="header">
  <h1>☀️ Good Morning, Melissa</h1>
  <div class="sub">Wednesday, June 3, 2026 &nbsp;·&nbsp; Executive Chief of Staff Briefing</div>
  <div class="meta">
    <div class="meta-item"><div class="num">50</div><div class="label">Emails Reviewed</div></div>
    <div class="meta-item"><div class="num">10</div><div class="label">Calendar Events</div></div>
    <div class="meta-item"><div class="num">3</div><div class="label">🔴 Security Alerts</div></div>
    <div class="meta-item"><div class="num">5</div><div class="label">🟡 Action Required</div></div>
    <div class="meta-item"><div class="num">4</div><div class="label">🟢 Job Leads</div></div>
    <div class="meta-item"><div class="num">6</div><div class="label">📅 Upcoming Events</div></div>
  </div>
</div>

<!-- ══════════════════════════════════ EXECUTIVE SUMMARY ════ -->
<div class="section-wrapper red">
  <div class="section-title">⚡ Executive Summary</div>
  <div class="section-body">
    <div class="exec-bullet">
      <div class="exec-icon">🔴</div>
      <div class="exec-text">
        <strong>Security Risk — LinkedIn Password Reset + Suspicious Scam Emails</strong>
        <span>Your LinkedIn password was reset today (confirmed via security email). Separately, three highly suspicious scam/phishing emails remain outside Trash — including a fake "cloud account locked" threat, a casino money scam, and a fake gambling promo targeting your email address directly. Immediate review and deletion required.</span>
      </div>
    </div>
    <div class="exec-bullet">
      <div class="exec-icon">🟢</div>
      <div class="exec-text">
        <strong>Job Search — LinkedIn Alert for Senior Director HRBP + Networking Session Tomorrow</strong>
        <span>A high-fit "Senior Director, HR Business Partner (AI-Native)" role at RemoteHunter was flagged in LinkedIn Job Alerts. You also have an HR Networking & Job Search Open Office Hours session tomorrow (Thu Jun 4, 12–1 PM) that requires an RSVP. A 15-min consultation with Netta Jenkins (HIC Consult) is confirmed for June 9.</span>
      </div>
    </div>
    <div class="exec-bullet">
      <div class="exec-icon">🔵</div>
      <div class="exec-text">
        <strong>Calendar — Busy Day Tomorrow (Thu Jun 4) + Scheduling Conflict on Jun 10</strong>
        <span>Tomorrow you have three back-to-back events: Executive Roundtable (declined, 9–10:30 AM), Dr. Husk appointment (confirmed, 10:30–11:30 AM), and HR Networking Open Office Hours (RSVP pending, 12–1 PM). On June 10, you have a potential conflict: HR Networking Group and "Melissa x Meg drinks" overlap between 12–1 PM.</span>
      </div>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════ ACTION REQUIRED ══════ -->
<div class="section-wrapper yellow">
  <div class="section-title">🚨 Action Required</div>
  <div class="section-body">

    <div class="card">
      <span class="card-label label-red">🔴 URGENT — SECURITY</span>
      <h3>LinkedIn Password Was Reset — Verify It Was You</h3>
      <div class="meta-row"><span><strong>Source:</strong> LinkedIn &lt;security-noreply@linkedin.com&gt;</span><span><strong>Date:</strong> Wed, Jun 3, 2026 at 9:17 PM UTC</span></div>
      <p>LinkedIn confirmed your password was successfully reset today. A PIN (606210) was also sent minutes before the reset. If you did not initiate this, your account may be compromised.</p>
      <div class="action">✅ Next Step: Log into LinkedIn immediately. Confirm the reset was yours. If not, enable 2FA and contact LinkedIn support. Review connected apps.</div>
      <div class="warning">⚠️ Due: Immediately — Today</div>
    </div>

    <div class="card">
      <span class="card-label label-red">🔴 URGENT — SCAM / PHISHING</span>
      <h3>3 Suspicious Scam Emails Still in Inbox (Not Trash)</h3>
      <div class="meta-row"><span><strong>Sources:</strong> Casino Yabby, "Limitless VIP" gambling spam, "Payment Declined" cloud lock threat</span></div>
      <p><strong>1.</strong> "Casino Yabby" — fake $13,963.99 payment confirmation targeting melissaw212 (not in trash). <br><strong>2.</strong> "130 Free Spins" gambling spam — targeting your Gmail directly (not in trash).<br><strong>3.</strong> "Payment Declined / Cloud Account Locked" — threatening to delete photos/videos unless you act — classic phishing (not in trash).</p>
      <div class="action">✅ Next Step: Delete all three immediately. Mark as spam. Do not click any links. Consider reporting to Gmail as phishing.</div>
      <div class="warning">⚠️ Due: Today — Do not interact with these emails</div>
    </div>

    <div class="card">
      <span class="card-label label-yellow">🟡 RSVP NEEDED</span>
      <h3>HR Networking & Job Search: Open Office Hours — Tomorrow</h3>
      <div class="meta-row"><span><strong>Source:</strong> Google Calendar</span><span><strong>Date:</strong> Thu, Jun 4, 12:00–1:00 PM ET</span></div>
      <p>Status is "needsAction" — you have not yet RSVP'd. This is a large networking group (150+ HR professionals). Zoom link available.</p>
      <div class="action">✅ Next Step: RSVP Accept or Decline on Google Calendar before tomorrow morning. Note: organizer requests no AI notetaking tools.</div>
      <div class="warning">⚠️ Due: Tonight / tomorrow morning</div>
    </div>

    <div class="card">
      <span class="card-label label-yellow">🟡 BILLING / DEADLINE</span>
      <h3>Netlify Credits at 75% — Morning Briefing Project</h3>
      <div class="meta-row"><span><strong>Source:</strong> Netlify &lt;team@netlify.com&gt;</span><span><strong>Date:</strong> Wed, Jun 3, 9:28 PM UTC</span></div>
      <p>Your Netlify "morning briefing" team has consumed 750 of 1,000 credits this billing cycle. If the daily briefing automation continues running, you will hit the limit soon. Note: GitHub workflow failures were also logged today (2 failed runs).</p>
      <div class="action">✅ Next Step: Log into Netlify dashboard. Review billing cycle reset date. Consider upgrading plan or optimizing briefing workflow to reduce credit consumption. Also investigate the 2 GitHub Actions failures.</div>
      <div class="warning">⚠️ Due: This week</div>
    </div>

    <div class="card">
      <span class="card-label label-yellow">🟡 BILLING REMINDER</span>
      <h3>State Farm Bill Due — June 7</h3>
      <div class="meta-row"><span><strong>Source:</strong> Google Calendar</span><span><strong>Date:</strong> Sun, Jun 7, 2026 (All Day)</span></div>
      <p>Calendar reminder for State Farm insurance bill payment. No additional context provided.</p>
      <div class="action">✅ Next Step: Schedule payment before June 7 to avoid late fees.</div>
      <div class="warning">⚠️ Due: Sunday, June 7</div>
    </div>

    <div class="card">
      <span class="card-label label-blue">🔵 RSVP / CONFIRM</span>
      <h3>Melissa x Meg Drinks — June 10 (Needs Action)</h3>
      <div class="meta-row"><span><strong>Source:</strong> Google Calendar</span><span><strong>Attendee:</strong> megpark@oakleafpartnership.com</span><span><strong>Date:</strong> Wed, Jun 10, 1:00–2:00 PM</span></div>
      <p>Status is "needsAction." Location is listed as "TBC." Potential overlap with HR Networking Group (12–1:30 PM) on the same day.</p>
      <div class="action">✅ Next Step: Confirm location with Meg. Note the 30-min overlap with HR Networking Group (12–1:30 PM). Decide which to prioritize or if networking ends on time.</div>
      <div class="warning">⚠️ Scheduling conflict possible on June 10</div>
    </div>

  </div>
</div>

<!-- ════════════════════════════════ FULL 7-DAY CALENDAR ════ -->
<div class="section-wrapper blue">
  <div class="section-title">📅 Full 7-Day Calendar (Jun 3 – Jun 10, 2026)</div>
  <div class="section-body">

    <div class="day-block">
      <div class="day-title">Wednesday, June 3, 2026 — TODAY</div>
      <div class="event-row">
        <div class="event-time">All Day</div>
        <div class="event-details">
          <strong>No scheduled events today</strong>
          <div class="ev-meta">Use today to review security alerts, action items, and prepare for tomorrow's busy schedule.</div>
        </div>
      </div>
    </div>

    <div class="day-block">
      <div class="day-title">Thursday, June 4, 2026 — TOMORROW</div>
      <div class="event-row">
        <div class="event-time">9:00–10:30 AM</div>
        <div class="event-details">
          <strong>Executive Roundtable</strong>
          <div class="ev-meta">
            <span class="status-declined">DECLINED</span> &nbsp;
            Hosted by: John Madigan &nbsp;|&nbsp;
            <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> &nbsp;|&nbsp; Meeting ID: 207 786 667 &nbsp;|&nbsp; PW: 205454
          </div>
          <div class="ev-meta">⚠️ You declined this event. No prep needed unless you wish to reconsider.</div>
        </div>
      </div>
      <div class="event-row">
        <div class="event-time">10:30–11:30 AM</div>
        <div class="event-details">
          <strong>Dr. Husk (Medical Appointment)</strong>
          <div class="ev-meta"><span class="status-confirmed">CONFIRMED</span> &nbsp; No location listed — confirm address/telehealth link in advance.</div>
          <div class="ev-meta">📋 Prep: Confirm appointment location or call-in details. Prepare any questions or medical records needed.</div>
        </div>
      </div>
      <div class="event-row">
        <div class="event-time">12:00–1:00 PM</div>
        <div class="event-details">
          <strong>HR Networking & Job Search: Open Office Hours – Zoom 2</strong>
          <div class="ev-meta"><span class="status-pending">RSVP NEEDED</span> &nbsp; 150+ attendees &nbsp;|&nbsp; <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a></div>
          <div class="ev-meta">📋 Prep: RSVP today. No AI notetaking tools per organizer request. Prepare elevator pitch for networking.</div>
          <div class="warning">⚠️ RSVP required — status is "needsAction"</div>
        </div>
      </div>
    </div>

    <div class="day-block">
      <div class="day-title">Friday, June 5, 2026</div>
      <div class="event-row">
        <div class="event-time">All Day</div>
        <div class="event-details">
          <strong>No scheduled events</strong>
          <div class="ev-meta">Open day. Good time for job applications, follow-ups, and LinkedIn activity.</div>
        </div>
      </div>
    </div>

    <div class="day-block">
      <div class="day-title">Saturday, June 6, 2026</div>
      <div class="event-row">
        <div class="event-time">All Day</div>
        <div class="event-details">
          <strong>🎂 Jackie's Birthday</strong>
          <div class="ev-meta"><span class="status-confirmed">CONFIRMED</span> &nbsp; All-day event (June 6–7)</div>
          <div class="ev-meta">🎁 Prep: Send birthday message or gift if applicable. Check if any plans were made.</div>
        </div>
      </div>
    </div>

    <div class="day-block">
      <div class="day-title">Sunday, June 7, 2026</div>
      <div class="event-row">
        <div class="event-time">All Day</div>
        <div class="event-details">
          <strong>🎂 Jackie's Birthday (continues)</strong>
          <div class="ev-meta"><span class="status-confirmed">CONFIRMED</span></div>
        </div>
      </div>
      <div class="event-row">
        <div class="event-time">All Day</div>
        <div class="event-details">
          <strong>💰 State Farm Bill Due</strong>
          <div class="ev-meta"><span class="status-confirmed">REMINDER</span> &nbsp; Pay before end of day to avoid late fees.</div>
          <div class="warning">⚠️ Bill due — action required before this date</div>
        </div>
      </div>
    </div>

    <div class="day-block">
      <div class="day-title">Monday, June 8, 2026</div>
      <div class="event-row">
        <div class="event-time">9:00–10:00 AM</div>
        <div class="event-details">
          <strong>👁️ Eye Appointment</strong>
          <div class="ev-meta"><span class="status-confirmed">CONFIRMED</span> &nbsp; No location listed.</div>
          <div class="ev-meta">📋 Prep: Confirm location/address. Bring insurance card. Allow travel time. Note: you may need someone to drive if eyes are dilated.</div>
        </div>
      </div>
    </div>

    <div class="day-block">
      <div class="day-title">Tuesday, June 9, 2026</div>
