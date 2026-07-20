<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa Weiss — July 20, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1200px; margin: 0 auto; padding: 20px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); color: white; padding: 32px 40px; border-radius: 16px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; }
  .header-left h1 { font-size: 28px; font-weight: 300; letter-spacing: 1px; }
  .header-left h1 span { font-weight: 700; color: #e2b96f; }
  .header-left .date { font-size: 14px; color: #a0aec0; margin-top: 4px; }
  .header-stats { display: flex; gap: 24px; }
  .stat-box { background: rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 20px; text-align: center; }
  .stat-box .num { font-size: 26px; font-weight: 700; color: #e2b96f; }
  .stat-box .lbl { font-size: 11px; color: #a0aec0; text-transform: uppercase; letter-spacing: 1px; }

  /* SECTION HEADERS */
  .section { margin-bottom: 28px; }
  .section-header { display: flex; align-items: center; gap: 10px; margin-bottom: 14px; padding-bottom: 8px; border-bottom: 2px solid #e2e8f0; }
  .section-header h2 { font-size: 17px; font-weight: 700; color: #1a1a2e; text-transform: uppercase; letter-spacing: 1px; }
  .section-icon { font-size: 18px; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; border-left: 5px solid transparent; }
  .card-red { background: #fff5f5; border-left-color: #e53e3e; }
  .card-yellow { background: #fffbeb; border-left-color: #d69e2e; }
  .card-blue { background: #ebf8ff; border-left-color: #3182ce; }
  .card-green { background: #f0fff4; border-left-color: #38a169; }
  .card-purple { background: #faf5ff; border-left-color: #805ad5; }
  .card-gray { background: #f7fafc; border-left-color: #a0aec0; }
  .card-orange { background: #fffaf0; border-left-color: #dd6b20; }

  .card-title { font-weight: 700; font-size: 14px; margin-bottom: 6px; }
  .card-meta { font-size: 12px; color: #718096; margin-bottom: 6px; }
  .card-body { font-size: 13px; }
  .badge { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 11px; font-weight: 700; text-transform: uppercase; margin-right: 6px; }
  .badge-red { background: #fed7d7; color: #c53030; }
  .badge-yellow { background: #fefcbf; color: #975a16; }
  .badge-green { background: #c6f6d5; color: #276749; }
  .badge-blue { background: #bee3f8; color: #2c5282; }
  .badge-purple { background: #e9d8fd; color: #553c9a; }
  .badge-gray { background: #e2e8f0; color: #4a5568; }
  .badge-orange { background: #feebc8; color: #7b341e; }

  /* EXECUTIVE SUMMARY */
  .exec-summary { display: grid; grid-template-columns: repeat(3,1fr); gap: 16px; margin-bottom: 28px; }
  .exec-card { border-radius: 12px; padding: 20px; color: white; }
  .exec-card.risk { background: linear-gradient(135deg, #c53030, #e53e3e); }
  .exec-card.jobs { background: linear-gradient(135deg, #276749, #38a169); }
  .exec-card.calendar { background: linear-gradient(135deg, #2c5282, #3182ce); }
  .exec-card h3 { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; opacity: 0.85; margin-bottom: 8px; }
  .exec-card p { font-size: 13px; font-weight: 600; line-height: 1.5; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #2d3748; color: white; padding: 10px 12px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
  td { padding: 9px 12px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  tr:nth-child(even) td { background: #f7fafc; }
  tr:hover td { background: #edf2f7; }

  /* CALENDAR */
  .cal-day { margin-bottom: 20px; }
  .cal-day-header { background: #2d3748; color: white; padding: 8px 14px; border-radius: 8px 8px 0 0; font-weight: 700; font-size: 13px; }
  .cal-day-header.today { background: linear-gradient(90deg, #3182ce, #2c5282); }
  .cal-event { display: grid; grid-template-columns: 110px 1fr 90px 100px; gap: 10px; padding: 10px 14px; border-bottom: 1px solid #e2e8f0; background: white; font-size: 12.5px; }
  .cal-event:last-child { border-bottom: none; border-radius: 0 0 8px 8px; }
  .cal-event-time { font-weight: 700; color: #3182ce; }
  .cal-event-title { font-weight: 600; }
  .cal-event-status { }
  .cal-event-note { color: #718096; font-style: italic; }
  .status-confirmed { color: #38a169; font-weight: 700; }
  .status-declined { color: #e53e3e; font-weight: 700; }
  .status-needs { color: #d69e2e; font-weight: 700; }
  .allday-event { display: grid; grid-template-columns: 110px 1fr; gap: 10px; padding: 8px 14px; border-bottom: 1px solid #e2e8f0; background: #faf5ff; font-size: 12.5px; }
  .allday-label { color: #805ad5; font-weight: 700; font-size: 11px; }

  /* GRID LAYOUTS */
  .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  .three-col { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; }

  /* ACTION ITEMS TABLE */
  .priority-high { color: #c53030; font-weight: 700; }
  .priority-med { color: #d69e2e; font-weight: 700; }
  .priority-low { color: #38a169; font-weight: 700; }

  /* DASHBOARD */
  .dashboard { display: grid; grid-template-columns: repeat(4,1fr); gap: 14px; margin-bottom: 28px; }
  .dash-widget { background: white; border-radius: 10px; padding: 16px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); text-align: center; }
  .dash-widget .dw-num { font-size: 30px; font-weight: 800; }
  .dash-widget .dw-lbl { font-size: 11px; color: #718096; text-transform: uppercase; letter-spacing: 0.8px; margin-top: 4px; }
  .dash-widget.dw-red .dw-num { color: #e53e3e; }
  .dash-widget.dw-yellow .dw-num { color: #d69e2e; }
  .dash-widget.dw-green .dw-num { color: #38a169; }
  .dash-widget.dw-blue .dw-num { color: #3182ce; }
  .dash-widget.dw-purple .dw-num { color: #805ad5; }
  .dash-widget.dw-gray .dw-num { color: #718096; }

  /* PILL TAGS */
  .tag { display: inline-block; padding: 1px 7px; border-radius: 10px; font-size: 11px; margin: 1px; }
  .tag-red { background:#fed7d7; color:#c53030; }
  .tag-green { background:#c6f6d5; color:#276749; }
  .tag-yellow { background:#fefcbf; color:#975a16; }
  .tag-blue { background:#bee3f8; color:#2c5282; }
  .tag-gray { background:#e2e8f0; color:#4a5568; }

  /* TOP PRIORITIES */
  .top3 { display: grid; grid-template-columns: repeat(3,1fr); gap: 16px; }
  .top3-card { background: linear-gradient(135deg, #1a1a2e, #16213e); color: white; border-radius: 14px; padding: 24px; position: relative; overflow: hidden; }
  .top3-card::before { content: attr(data-num); position: absolute; top: -10px; right: 14px; font-size: 80px; font-weight: 900; color: rgba(255,255,255,0.05); }
  .top3-card h3 { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #e2b96f; margin-bottom: 10px; }
  .top3-card p { font-size: 13px; font-weight: 600; line-height: 1.6; }

  /* ACCOUNTING TABLE */
  .accounting-table th { background: #1a1a2e; }
  .accounting-total td { background: #2d3748 !important; color: white; font-weight: 700; }

  /* FOOTER */
  .footer { text-align: center; padding: 20px; color: #a0aec0; font-size: 12px; border-top: 1px solid #e2e8f0; margin-top: 30px; }

  /* SCAM WARNING */
  .scam-banner { background: #1a1a2e; border: 2px solid #e53e3e; border-radius: 10px; padding: 12px 18px; margin-bottom: 10px; }
  .scam-banner .scam-title { color: #fc8181; font-weight: 700; font-size: 13px; }
  .scam-banner .scam-reason { color: #a0aec0; font-size: 12px; margin-top: 3px; }

  /* INLINE LIST */
  ul.ilist { list-style: none; padding: 0; }
  ul.ilist li { padding: 4px 0; border-bottom: 1px solid #e2e8f0; font-size: 13px; }
  ul.ilist li:last-child { border-bottom: none; }

  @media (max-width: 900px) {
    .exec-summary, .two-col, .three-col, .dashboard, .top3 { grid-template-columns: 1fr; }
    .header { flex-direction: column; gap: 16px; }
    .header-stats { flex-wrap: wrap; }
    .cal-event { grid-template-columns: 1fr 1fr; }
  }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════════════
     1. HEADER
═══════════════════════════════════════════════════════════ -->
<div class="header">
  <div class="header-left">
    <h1>Good morning, <span>Melissa</span> ☀️</h1>
    <div class="date">Monday, July 20, 2026 &nbsp;|&nbsp; Executive Daily Briefing &nbsp;|&nbsp; Prepared by Your Chief of Staff</div>
  </div>
  <div class="header-stats">
    <div class="stat-box"><div class="num">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="stat-box"><div class="num">11</div><div class="lbl">Calendar Events</div></div>
    <div class="stat-box"><div class="num">5</div><div class="lbl">Auto-Trashed Phishing</div></div>
    <div class="stat-box"><div class="num">3</div><div class="lbl">Action Items</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     2. EXECUTIVE SUMMARY
═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header"><span class="section-icon">⚡</span><h2>Executive Summary</h2></div>
  <div class="exec-summary">
    <div class="exec-card risk">
      <h3>🔴 Biggest Risk / Urgent</h3>
      <p>5 phishing/scam emails were auto-trashed today — including fake iCloud threats, prize scams, and a Firebase credential-harvesting attempt. Multiple additional suspicious emails remain untrashed (nerve pain "Dr. O'Neill," Kieja platform access, GLP-1 spam). No action needed on auto-trashed items, but verify your accounts are secure.</p>
    </div>
    <div class="exec-card jobs">
      <h3>🟢 Job Search / Opportunity</h3>
      <p>Three active LinkedIn job alerts arrived today: SVP Human Resources at Eaton Fiber, Senior Manager Global HR at Omada Search (in inbox), and VP HR Operations at Opensity Solutions (in inbox). Scovai matched you 84% to a Chief People & Culture Officer role at Omnisage LLC. Review and apply this week.</p>
    </div>
    <div class="exec-card calendar">
      <h3>🔵 Calendar / Deadlines</h3>
      <p>Physical therapy is TODAY at 1:45 PM. Two HR Networking Zoom events on Wednesday need RSVPs (status: needsAction). Chase credit card statement due 08/16 — minimum $387. Verizon Fios Bill and Amy Fink's birthday both fall Thursday 7/23. Eric Dordick's birthday is tomorrow — send a note!</p>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     3. ACTION REQUIRED
═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header"><span class="section-icon">🎯</span><h2>Action Required</h2></div>

  <div class="card card-red">
    <div class="card-title"><span class="badge badge-red">SECURITY</span> Multiple Phishing / Scam Emails in Inbox or Not Trashed</div>
    <div class="card-meta">Source: Gmail — Various senders with gibberish domains</div>
    <div class="card-body">
      Several suspicious emails were NOT auto-trashed and remain in non-trash folders. These include: "GLP-1 DirectMeds" (random domain), "Kieja Support" (Croatian T-Com domain impersonation), "Dr. Barbara O'Neill nerve pain" (gibberish domain), and a men's health spam (gibberish domain). These are almost certainly spam/phishing. <strong>Manually trash all of them. Do not click any links.</strong>
      <br><br><strong>Recommended Action:</strong> Trash immediately. Run a quick account security check on Google, Chase, and Robinhood. No credentials should have been exposed.
      <br><strong>Due:</strong> Today
    </div>
  </div>

  <div class="card card-yellow">
    <div class="card-title"><span class="badge badge-yellow">RSVP NEEDED</span> HR Networking & Job Search Group — Two Zoom Sessions Wednesday</div>
    <div class="card-meta">Source: Google Calendar — Wednesday, July 22, 2026 | 12:00–1:30 PM & Thursday 7/23 12:00–1:00 PM (Open Office Hours)</div>
    <div class="card-body">
      Both events show status <strong>needsAction</strong> — you have not confirmed or declined. These are large networking groups relevant to your job search. Review the Zoom links and RSVP before Wednesday.
      <br><strong>Recommended Action:</strong> Confirm or decline both events in Google Calendar. Join if available — large HR network group.
      <br><strong>Due:</strong> Before Wednesday, July 22
    </div>
  </div>

  <div class="card card-yellow">
    <div class="card-title"><span class="badge badge-yellow">BILLING</span> Chase Credit Card Statement Available — $387 Minimum Due</div>
    <div class="card-meta">Source: Chase <no.reply.alerts@chase.com> — Received today, July 20, 2026</div>
    <div class="card-body">
      Your Chase Credit Card (••••2754) statement is ready. Minimum payment due: <strong>$387.00</strong>. Due date: <strong>August 16, 2026</strong>. Log in to Chase to review statement and schedule payment.
      <br><strong>Recommended Action:</strong> Review statement online. Schedule payment before 8/16.
      <br><strong>Due:</strong> August 16, 2026
    </div>
  </div>

  <div class="card card-green">
    <div class="card-title"><span class="badge badge-green">JOB SEARCH</span> Review 4 New Job Leads — Including 84% Scovai Match</div>
    <div class="card-meta">Source: LinkedIn Job Alerts + Scovai — Received today</div>
    <div class="card-body">
      Four new opportunities surfaced today: <strong>SVP Human Resources @ Eaton Fiber</strong> (LinkedIn, trashed), <strong>Senior Manager Global HR @ Omada Search</strong> (LinkedIn, inbox), <strong>VP HR Operations @ Opensity Solutions</strong> (LinkedIn, inbox), and <strong>Chief People & Culture Officer @ Omnisage LLC</strong> (84% Scovai match, trashed). Review and apply to strongest fits.
      <br><strong>Recommended Action:</strong> Pull up all four listings and apply to top matches today. Restore trashed LinkedIn alerts if needed.
      <br><strong>Due:</strong> Today or tomorrow
    </div>
  </div>

  <div class="card card-blue">
    <div class="card-title"><span class="badge badge-blue">TODAY</span> Physical Therapy — 1:45 PM to 2:45 PM</div>
    <div class="card-meta">Source: Google Calendar — Today, July 20, 2026</div>
    <div class="card-body">
      You have PT confirmed for this afternoon. No location listed — confirm address/details if needed. Appears twice on calendar (possible duplicate entry).
      <br><strong>Recommended Action:</strong> No action needed other than showing up. Check for duplicate calendar entry to clean up.
      <br><strong>Due:</strong> Today, 1:45 PM
    </div>
  </div>

  <div class="card card-orange">
    <div class="card-title"><span class="badge badge-orange">DELIVERY</span> Temu Order In Transit — Transferred to GOFO for Delivery</div>
    <div class="card-meta">Source: Temu <orders@transaction.temu.com> — Received today (2 emails, in inbox)</div>
    <div class="card-body">
      Your Temu order (#PO-211-14414847201911025) has been transferred to GOFO. Tracking number: <strong>GFUS01061647700548</strong>. Shipping to 303 E 83rd (your address). Monitor delivery status.
      <br><strong>Recommended Action:</strong> Track via GOFO tracking number. Expect delivery soon.
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════
     4. FULL 7-DAY CALENDAR
═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header"><span class="section-icon">📅</span><h2>Full 7-Day Calendar</h2></div>

  <!-- MONDAY JULY 20 -->
  <div class="cal-day">
    <div class="cal-day-header today">📍 TODAY — Monday, July 20, 2026</div>
    <div class="cal-event">
      <div class="cal-event-time">1:45 – 2:45 PM</div>
      <div class="cal-event-title">🏋️ Pt (Physical Therapy) <span class="tag tag-yellow">⚠️ Duplicate Entry</span></div>
      <div class="cal-event-status"><span class="status-confirmed">✔ Confirmed</span></div>
      <div class="cal-event-note">No location listed. Confirm address. Appears twice on calendar — delete duplicate.</div>
    </div>
    <div class="cal-event">
      <div class="cal-event-time">1:45 – 2:45 PM</div>
      <div class="cal-event-title">🏋️ Pt (Physical Therapy) — <em>Duplicate</em></div>
      <div class="cal-event-status"><span class="status-confirmed">✔ Confirmed</span></div>
      <div class="cal-event-note">Delete this duplicate entry.</div>
    </div>
  </div>

  <!-- TUESDAY JULY 21 -->
  <div class="cal-day">
    <div class="cal-day-header">Tuesday, July 21, 2026</div>
    <div class="allday-event">
      <div class="allday-label">🎂 ALL DAY</div>
      <div><strong>Eric Dordick's Birthday</strong> — Send a message or card today!</div>
    </div>
    <div class="cal-event">
      <div class="cal-event-time">10:00 – 11:00 AM</div>
      <div class="cal-event-title">Umi</div>
      <div class="cal-event-status"><span class="status-confirmed">✔ Confirmed</span></div>
      <div class="cal-event-note">No location or description. Confirm details.</div>
    </div>
  </div>

  <!-- WEDNESDAY JULY 22 -->
  <div class="cal-day">
    <div class="cal-day-header">Wednesday, July 22, 2026</div>
    <div class="cal-event">
      <div class="cal-event-time">12:00 – 1:30 PM</div>
      <div class="cal-event-title">🌐 HR Networking &amp; Job Search Group — Zoom 2 <span class="tag tag-yellow">RSVP NEEDED</span></div>
      <div class="cal-event-status"><span class="status-needs">⚠ Needs Action</span></div>
      <div class="cal-event-note"><a href="https://us06web.zoom.us/j/81954171722" style="color:#3182ce;">Zoom Link</a> — Large group (190+ attendees). Review agenda/guidelines before joining. RSVP required.</div>
    </div>
    <div class="cal-event">
      <div class="cal-event-time">12:00 – 1:30 PM</div>
      <div class="cal-event-title">📡 Network (Personal copy of same event)</div>
      <div class="cal-event-status"><span class="status-confirmed">✔ Confirmed</span></div>
      <div class="cal-event-note">Personal calendar copy of HR Networking Zoom. Appears to be same timeslot — no conflict.</div>
    </div>
  </div>

  <!-- THURSDAY JULY 23 -->
  <div class="cal-day">
    <div class="cal-day-header">Thursday, July 23, 2026</div>
    <div class="allday-event">
      <div class="allday-label">🎂 ALL DAY</div>
      <div><strong>Amy Fink's Birthday</strong> — Send a birthday message!</div>
    </div>
    <div class="allday-event">
      <div class="allday-label">💳 ALL DAY</div>
      <div><strong>Verizon Fios Bill Due</strong> — Review and pay if not on autopay.</div>
    </div>
    <div class="cal-event">
      <div class="cal-event-time">9:00 – 10:30 AM</div>
      <div class="cal-event-title">📊 Executive Roundtable (John Madigan via Zoom) <span class="tag tag-red">DECLINED</span></div>
      <div class="cal-event-status"><span class="status-declined">✘ Declined</span></div>
      <div class="cal-event-note"><a href="https://us02web.zoom.us/j/207786667" style="color:#3182ce;">Zoom Link</a> — You declined. Confirm if you need to notify John Madigan.</div>
    </div>
    <div class="cal-event">
      <div class="cal-event-time">12:00 – 1:00 PM</div>
      <div class="cal-event-title">🤝 HR Networking &amp; Job Search: Open Office Hours — Zoom 2 <span class="tag tag-yellow">RSVP NEEDED</span></div>
      <div class="cal-event-status"><span class="status-needs">⚠ Needs Action</span></div>
      <div class="cal-event-note"><a href="https://us06web.zoom.us/j/85945371140" style="color:#3182ce;">Zoom Link</a> — Note: AI notetaking tools should be turned off. RSVP required.</div>
    </div>
  </div>

  <!-- FRIDAY JULY 24 -->
  <div class="cal-day">
    <div class="cal-day-header">Friday, July 24, 2026</div>
    <div style="background:white; padding:12px 14px; border-radius: 0 0 8px 8px; font-size:13px; color:#718096; font-style:italic;">No calendar events scheduled.</div>
  </div>

  <!-- SATURDAY JULY 25 -->
  <div class="cal-day">
    <div class="cal-day-header">Saturday, July 25, 2026</div>
    <div style="background:white; padding:12px 14px; border-radius: 0 0 8px 8px; font-size:13px; color:#718096; font-style:italic;">No calendar events scheduled.</div>
  </div>

  <!-- SUNDAY JULY 26 -->
  <div class="cal-day">
    <div class="cal-day-header">Sunday, July 26, 2026</div>
    <div class="allday-event">
      <div class="allday-label">💳 ALL DAY</div>
      <div><strong>Warby Parker Auto Pay</strong> — Automatic payment processing today. Verify sufficient funds in linked account.</div>
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════
     5. JOB SEARCH & INTERVIEW PIPELINE
═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header"><span class="section-icon">💼</span><h2>Job Search &amp; Interview Pipeline</h2></div>

  <table>
    <thead>
      <tr>
        <th>Source</th>
        <th>Role / Opportunity</th>
        <th>Company</th>
        <th>Fit</th>
        <th>Status</th>
        <th>Recommended Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="tag tag-green">Scovai</span></td>
        <td>Chief People &amp; Culture Officer</td>
        <td>Omnisage LLC</td>
        <td><span class="badge badge-green">HIGH — 84%</span></td>
        <td>New match, in trash</td>
        <td>Restore from trash, review posting, apply if aligned</td>
      </tr>
      <tr>
        <td><span class="tag tag-blue">LinkedIn</span></td>
        <td>Senior Vice President Human Resources</td>
        <td>Eaton Fiber</td>
        <td><span class="badge badge-green">HIGH</span></td>
        <td>Alert received, in trash</td>
        <td>Restore, review full listing, apply ASAP (posted 7/17)</td>
      </tr>
      <tr>
        <td><span class="tag tag-blue">LinkedIn</span></td>
        <td>Senior Manager of Global Human Resources</td>
        <td>Omada Search</td>
        <td><span class="badge badge-yellow">MEDIUM-HIGH</span></td>
        <td>Alert in inbox</td>
        <td>Review listing and apply; note this is a search firm</td>
      </tr>
      <tr>
        <td><span class="tag tag-blue">LinkedIn</span></td>
        <td>VP, Human Resources Operations</td>
        <td>Opensity Solutions</td>
        <td><span class="badge badge-yellow">MEDIUM</span></td>
        <td>Alert in inbox</td>
        <td>Review scope and comp; apply if VP-level is target</td>
      </tr>
      <tr>
        <td><span class="tag tag-gray">HR Recruit</span></td>
        <td>Chief Human Resources Officer</td>
        <td>Unknown (follow-up email)</td>
        <td><span class="badge badge-red">LOW — Suspicious</span></td>
        <td>Follow-up email from noreply@hr-recruit.com, in trash</td>
        <td>Do not engage — likely spam recruiter or data harvester. Ignore.</td>
      </tr>
      <tr>
        <td><span class="tag tag-purple">Networking</span></td>
        <td>HR Networking &amp; Job Search Group Zoom</td>
        <td>Large HR Network (190+ members)</td>
        <td><span class="badge badge-green">HIGH — Networking</span></td>
        <td>Wednesday 7/22, RSVP pending</td>
        <td>RSVP confirm, prepare brief intro and target role statement</td>
      </tr>
      <tr>
        <td><span class="tag tag-purple">Networking</span></td>
        <td>HR Networking Open Office Hours</td>
        <td>Same HR Network Group</td>
        <td><span class="badge badge-green">HIGH — Networking</span></td>
        <td>Thursday 7/23, RSVP pending</td>
        <td>RSVP confirm; no AI notetaking per organizer request</td>
      </tr>
      <tr>
        <td><span class="tag tag-blue">Calendar</span></td>
        <td>Umi (meeting)</td>
        <td>Unknown</td>
        <td><span class="badge badge-gray">REVIEW</span></td>
        <td>Tuesday 7/21 10:00 AM, confirmed</td>
        <td>Confirm context of "Umi" meeting — is this a recruiter, coach, or personal contact?</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════════
     6. FULL EMAIL REVIEW BY CATEGORY
═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header"><span class="section-icon">📧</span><h2>Full Email Review by Category</h2></div>

  <!-- SECURITY / RISK -->
  <div class="card card-red">
    <div class="card-title">🔴 Security / Risk — 9 Emails</div>
    <div class="card-meta">Includes auto-trashed phishing, active scam/spam in non-trash folders, and suspicious recruiters</div>
    <div class="card-body">

      <p style="font-weight:700; margin: 8px 0 6px;">🤖 AUTO-TRASHED (Phishing — No Action Needed)</p>

      <div class="scam-banner">
        <div class="scam-title">⛔ melissaw212 — "Your Cloud ID has been locked" (xamjwceudsv@snqo…)</div>
        <div class="scam-reason">Auto-Trashed Reason: Fake iCloud/cloud storage account-lock threat with urgency about photo/video deletion; sent from random gibberish domain impersonating Apple/cloud service.</div>
      </div>
      <div class="scam-banner">
        <div class="scam-title">⛔ "Tractor Supply" — "You've won a Predator 3500 Watt Generator" (gibberish domain)</div>
        <div class="scam-reason">Auto-Trashed Reason: Fake prize/sweepstakes scam impersonating Tractor Supply; sent from random gibberish domain; "You are our winner" lure.</div>
      </div>
      <div class="scam-banner">
        <div class="scam-title">⛔ Firebase App — "Sign in to Get a Kobalt 100-piece Tool Set" (noreply@casi-04.firebaseapp.com)</div>
        <div class="scam-reason">Auto-Trashed Reason: Fake sign-in/prize lure using Firebase app domain; credential harvesting attempt.</div>
      </div>
      <div class="scam-banner">
        <div class="scam-title">⛔ "Payment_Declined©" — "We've Blocked Your Account! Photos deleted Sun 19 Jul" (gibberish domain)</div>
        <div class="scam-reason">Auto-Trashed Reason: Fake payment-declined account-block threat; random gibberish domain; unicode obfuscation in sender name to evade filters.</div>
      </div>
      <div class="scam-banner">
        <div class="scam-title">⛔ "Congratulations🎉" — "Get 130 Free Spins LITTLE130GRF" (ckvufaqqu@yrisoszwmomaytztrzgrfkhvdb.net)</div>
        <div class="scam-reason">Auto-Trashed Reason: Casino spam/phishing lure from gibberish domain (found in trash, confirms auto-trash worked).</div>
      </div>

      <p style="font-weight:700; margin: 12px 0 6px;">⚠️ NOT YET TRASHED — Manual Action Required</p>
      <ul class="ilist">
        <li><span class="badge badge-red">TRASH NOW</span> <strong>GLP-1-by-DirectMeds</strong> (hwdefuppqrf@ipkn.dlozmqpynixvx.us) — Fake medical ad from gibberish domain. Not in trash. Delete immediately.</li>
        <li><span class="badge badge-red">TRASH NOW</span> <strong>"Dr. Barbara O'Neill"</strong> (arpxypmzymp@xbgl.ltvrsdwozddbk.us) — Health misinformation/nerve pain scam from gibberish domain. Not in trash.</li>
        <li><span class="badge badge-red">TRASH NOW</span> <strong>Kieja Support</strong> (krunoslav.stamenkovic@sk.t-com.hr) — Suspicious "platform access details" email from Croatian T-Com domain. Not in trash. Do not click any links.</li>
        <li><span class="badge badge-red">TRASH NOW</span> <strong>"Mens-Midlife-Performance🍌"</strong> (wjaldrjflxg@rbgx.kjwnsquypxelr.us) — Men's health spam from gibberish domain. Not in trash (Melissa's inbox).</li>
      </ul>
      <br><strong>Recommended Action:</strong> Manually trash all 4 items above. Accounts are likely safe since these appear to be inbound spam, not responses to clicks — but change passwords if you're concerned.
    </div>
  </div>

  <!-- JOB SEARCH -->
  <div class="card card-green">
    <div class="card-title">🟢 Job Search — 5 Emails</div>
    <div class="card-meta">LinkedIn Job Alerts (3), Scovai (1), HR Recruit follow-up (1)</div>
    <div class="card-body">
      <ul class="ilist">
        <li><span class="badge badge-green">IN INBOX</span> <strong>LinkedIn</strong> — Senior Manager Global HR @ Omada Search (7/17/2026)</li>
        <li><span class="badge badge-green">IN INBOX</span> <strong>LinkedIn</strong> — VP, Human Resources Operations @ Opensity Solutions (7/17/2026)</li>
        <li><span class="badge badge-gray">TRASHED</span> <strong>LinkedIn</strong> — SVP Human Resources @ Eaton Fiber (7/17/2026) — Restore and review</li>
        <li><span class="badge badge-gray">TRASHED</span> <strong>Scovai</strong> — Chief People &amp; Culture Officer @ Omnisage LLC — 84% match — Restore and apply</li>
        <li><span class="badge badge-red">IGNORE</span> <strong>HR Recruit</strong> (noreply@hr-recruit.com) — Suspicious CHRO follow-up — likely data harvesting. Do not engage.</li>
      </ul>
      <strong>Recommended Action:</strong> Review all 4 legitimate job alerts. Restore trashed items. Apply to top 2–3 today.
    </div>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="card card-yellow">
    <div class="card-title">🟡 Financial / Billing — 3 Emails</div>
    <div class="card-meta">Chase (1), Robinhood (1), Indeed ToS (1)</div>
    <div class="card-body">
      <ul class="ilist">
        <li><span class="badge badge-yellow">IN INBOX</span> <strong>Chase</strong> — Credit card statement ready. Account ••••2754. Min payment: $387. Due: 8/16/2026.</li>
        <li><span class="badge badge-yellow">TRASHED</span> <strong>Robinhood</strong> — Withdrawal of $484.83 completed from individual (•••5739) to Money Market Savings. Confirm receipt.</li>
        <li><span class="badge badge-gray">TRASHED</span> <strong>Indeed</strong> — Terms of Service update notice. Low priority; safe to delete after review.</li>
      </ul>
      <strong>Recommended Action:</strong> Log into Chase to review statement and schedule payment. Verify Robinhood transfer landed in savings account. Note calendar reminders: Verizon Fios bill due 7/23, Warby Parker auto-pay 7/26.
    </div>
  </div>

  <!-- PERSONAL -->
  <div class="card card-blue">
    <div class="card-title">🔵 Personal — 2 Emails</div>
    <div class="card-meta">Match.com (2 — both trashed)</div>
    <div class="card-body">
      <ul class="ilist">
        <li><span class="badge badge-gray">TRASHED</span> <strong>Match</strong> — Eric (63, Wall Township NJ) viewed your profile.</li>
        <li><span class="badge badge-gray">TRASHED</span> <strong>Match</strong> — Johnny likes you.</li>
      </ul>
      <strong>Recommended Action:</strong> Already in trash. Check Match app directly if interested.
    </div>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="card card-purple">
    <div class="card-title">🟣 Professional Development — 3 Emails</div>
    <div class="card-meta">The HR AI Guy (1 — inbox), AI For Leaders (1 — trash), Otter.ai (1 — trash)</div>
    <div class="card-body">
      <ul class="ilist">
        <li><span class="badge badge-green">IN INBOX</span> <strong>The HR AI Guy (Medium)</strong> — "AI-Generated Birthday Songs: The Silliest Thing I Do That Gets the Biggest Reaction" — Fun, practical HR/AI tip relevant to your field.</li>
        <li><span class="badge badge-gray">TRASHED</span> <strong>AI For Leaders</strong> — "You've Already Trained a Robot" — Physical AI/humanoid robots leadership article.</li>
        <li><span class="badge badge-gray">TRASHED</span> <strong>Otter.ai Insights</strong> — Upcoming meetings summary for the week.</li>
      </ul>
      <strong>Recommended Action:</strong> Read The HR AI Guy article when time permits — relevant to your HR leadership work. AI For Leaders is worth restoring if interested in physical AI trends.
    </div>
  </div>

  <!-- NEXTDOOR / LOCAL NEWS -->
  <div class="card card-gray">
    <div class="card-title">⚫ Local News / Nextdoor — 2 Emails</div>
    <div class="card-meta">Nextdoor Local News (1 — not trashed, not inbox), Yorkville Nextdoor (1 — trashed)</div>
    <div class="card-body">
      <ul class="ilist">
        <li><span class="badge badge-yellow">NOT IN INBOX OR TRASH</span> <strong>Nextdoor Local News</strong> — "North Arlington Shooting Under Investigation" (Sunday July 19). Unread. Worth a quick scan for local awareness.</li>
        <li><span class="badge badge-gray">TRASHED</span> <strong>Your Yorkville Neighbors (Nextdoor)</strong> — Rant about electric motor vehicles / e-bikes. Safe to delete.</li>
      </ul>
      <strong>Recommended Action:</strong> Skim the North Arlington shooting article for local awareness. Trash the Yorkville rant.
    </div>
  </div>

  <!-- DELIVERIES -->
  <div class="card card-blue">
    <div class="card-title">🔵 Deliveries / Packages — 2 Emails</div>
    <div class="card-meta">Temu (2 — both in inbox)</div>
    <div class="card-body">
      <ul class="ilist">
        <li><span class="badge badge-blue">IN INBOX</span> <strong>Temu</strong> — Order shipped, GOFO tracking # GFUS01061647700548 (Order #PO-211-14414847201911025)</li>
        <li><span class="badge badge-blue">IN INBOX</span> <strong>Temu</strong> — Package transferred to GOFO, shipping to 303 E 83rd.</li>
      </ul>
      <strong>Recommended Action:</strong> Track your package using GOFO tracking number. No further action needed.
    </div>
  </div>

  <!-- USPS -->
  <div class="card card-gray">
    <div class="card-title">⚫ USPS Informed Delivery — 1 Email (Trashed)</div>
    <div class="card-meta">USPS (1 — trashed)</div>
    <div class="card-body">
      <ul class="ilist">
        <li><span class="badge badge-gray">TRASHED</span> <strong>USPS Informed Delivery</strong> — 4 mailpieces + 1 inbound package arriving today, Monday July 20.</li>
      </ul>
      <strong>Recommended Action:</strong> Check mailbox/building lobby. You have a package and 4 pieces of mail arriving today. Safe to delete after noting.
    </div>
  </div>

  <!-- NEWSLETTERS -->
  <div class="card card-purple">
    <div class="card-title">🟣 Newsletters / Subscriptions — 7 Emails (all trashed)</div>
    <div class="card-meta">Medium (2), The AI Report (1), TLDR (1), The Average Joe (1), The Hustle (1), 1% Better (1)</div>
    <div class="card-body">
      <ul class="ilist">
        <li><span class="badge badge-gray">TRASHED</span> <strong>Medium Daily Digest (@melissaw212)</strong> — "I Made $2,840 With Claude AI in 30 Days"</li>
        <li><span class="badge badge-gray">TRASHED</span> <strong>Medium Daily Digest (@amylw)</strong> — "What Happened to Gen AI Games..."</li>
        <li><span class="badge badge-gray">TRASHED</span> <strong>The AI Report</strong> — "Current AI builds free global web / Netflix paid $587M for Ben Affleck's AI startup"</li>
        <li><span class="badge badge-gray">TRASHED</span> <strong>TLDR</strong> — "Meta Anthropic deal, SpaceX Pentagon compute, AI code migrations"</li>
        <li><span class="badge badge-gray">TRASHED</span> <strong>The Average Joe</strong> — "Summer — Here comes the 40% correction?"</li>
        <li><span class="badge badge-gray">TRASHED</span> <strong>The Hustle</strong> — "Protein from thin air, grape seeds to space, beluga whale transport"</li>
        <li><span class="badge badge-gray">TRASHED</span> <strong>1% Better</strong> — "World Cup Winner, AI-Driven GDP, Matt Damon's Odysseus Workout"</li>
      </ul>
      <strong>Recommended Action:</strong> All were trashed. If you want to read any, restore from trash. Consider creating a newsletter digest folder rather than trashing to keep inbox clean.
    </div>
  </div>

  <!-- PROMOTIONAL / RETAIL -->
  <div class="card card-gray">
    <div class="card-title">⚫ Promotional / Retail — 14 Emails (all trashed)</div>
    <div class="card-meta">SHEIN (5), Gap Factory (2), Kohl's (1), Target Optical (1), Quince (1), Uber (1), Chick-fil-A (1), Gemma Bonham-Carter (1), Lisa Rangel (1)</div>
    <div class="card-body">See Promotional / Retail Summary section below for full breakdown.<br>
      <strong>Recommended Action:</strong> All are in trash. Delete permanently unless you want to shop.
    </div>
  </div>

  <!-- OTHER / MISC IN-INBOX -->
  <div class="card card-gray">
    <div class="card-title">⚫ Other / Misc — 2 Emails</div>
    <div class="card-meta">CoolDeep AI (trashed), Martin / People People Group (trashed)</div>
    <div class="card-body">
      <ul class="ilist">
        <li><span class="badge badge-gray">TRASHED</span> <strong>CoolDeep AI</strong> — "5 Cowork tips" newsletter-style email. Low relevance.</li>
        <li><span class="badge badge-gray">TRASHED</span> <strong>Martin @ The People People Group</strong> — HR newsletter: wildfire safety + "You Can't Make This Stuff Up."</li>
      </ul>
      <strong>Recommended Action:</strong> Safe to delete.
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════
     7. TRASH REVIEW
═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header"><span class="section-icon">🗑️</span><h2>Trash Review</h2></div>

  <div class="card card-green">
    <div class="card-title">✅ Restore Immediately (2 Items)</div>
    <div class="card-body">
      <table>
        <thead><tr><th>Sender</th><th>Subject</th><th>Why Restore</th></tr></thead>
        <tbody>
          <tr><td>LinkedIn Job Alerts</td><td>Senior Vice President Human Resources at Eaton Fiber</td><td>High-fit job lead — SVP level; posted 7/17. Apply ASAP.</td></tr>
          <tr><td>Scovai</td><td>1 new position matches your profile (Chief People &amp; Culture Officer @ Omnisage — 84% match)</td><td>84% algorithmic match to CHRO-level role. Strong lead worth reviewing.</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card card-yellow">
    <div class="card-title">⚠️ Review Before Deleting (8 Items)</div>
    <div class="card-body">
      <table>
        <thead><tr><th>Sender</th><th>Subject</th><th>Why Review</th></tr></thead>
        <tbody>
          <tr><td>Robinhood</td><td>Withdrawal Completed — $484.83</td><td>Financial transaction. Confirm funds arrived in Money Market savings. Then delete.</td></tr>
          <tr><td>Match</td><td>Eric viewed your profile / Johnny likes you</td><td>Personal — check Match app if interested. Then delete.</td></tr>
          <tr><td>USPS Informed Delivery</td><td>4 mailpieces + 1 package arriving today</td><td>Check mailbox. Then delete.</td></tr>
          <tr><td>Otter.ai Insights</td><td>Your upcoming meetings</td><td>May contain useful meeting prep context. Scan before deleting.</td></tr>
          <tr><td>AI For Leaders</td><td>You've Already Trained a Robot</td><td>Professional development — Physical AI trends. Optional read.</td></tr>
          <tr><td>Indeed</td><td>Terms of Service Updates</td><td>Skim for any material changes to your account. Then delete.</td></tr>
          <tr><td>The AI Report</td><td>Current AI builds free global web</td><td>Netflix/$587M Ben Affleck AI story — interesting market intel. Quick scan optional.</td></tr>
          <tr><td>TLDR</td><td>Meta Anthropic deal, SpaceX Pentagon compute</td><td>Relevant AI industry news — quick scan if interested in sector trends.</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card card-gray">
    <div class="card-title">🗑️ Safe to Delete Permanently (All Remaining Trash — 28 Items)</div>
    <div class="card-body">
      <table>
        <thead><tr><th>Category</th><th>Senders</th><th>Count</th></tr></thead>
        <tbody>
          <tr><td>SHEIN Promotional</td><td>SHEIN (market-us, news.edmmarket, us.mail domains)</td><td>5</td></tr>
          <tr><td>Gap Factory</td><td>Gap Factory, Gap Factory Cyber Sale</td><td>2</td></tr>
          <tr><td>Retail/Promo</td><td>Kohl's, Target Optical, Quince, Uber</td><td>4</td></tr>
          <tr><td>Course / Online Business Marketing</td><td>Gemma Bonham-Carter ($1.5M from one course), Lisa Rangel (resume), 1% Better</td><td>3</td></tr>
          <tr><td>Newsletters</td><td>Medium (2), The Average Joe, The Hustle, Martin/People People</td><td>5</td></tr>
          <tr><td>Phishing (Auto-Trashed)</td><td>Cloud ID lock, Tractor Supply generator, Firebase tool set, Payment declined block, Casino spins</td><td>5</td></tr>
          <tr><td>Local / Nextdoor</td><td>Yorkville Nextdoor rant</td><td>1</td></tr>
          <tr><td>AI/Tech Newsletters (low priority)</td><td>CoolDeep AI, HR AI Guy (can keep if preferred)</td><td>2</td></tr>
          <tr><td>Chick-fil-A / Food</td><td>Chick-fil-A (breakfast promo)</td><td>1</td></tr>
        </tbody>
      </table>
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════
     8. PROMOTIONAL / RETAIL SUMMARY
═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header"><span class="section-icon">🛍️</span><h2>Promotional / Retail Summary</h2></div>
  <table>
    <thead>
      <tr>
        <th>Brand / Sender</th>
        <th>Count</th>
        <th>Subject / Theme</th>
        <th>In Trash?</th>
        <th>Recommendation</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>SHEIN</td>
        <td>5</td>
        <td>"Room So Good You'll Stay In Tonight," "NEW IN: Just Added 3 Days Ago" (x2), "Start from $4.99 Trending Now" (x2)</td>
        <td>✅ Yes</td>
        <td><span class="badge badge-gray">Delete</span> — Excessive duplicate sends. Unsubscribe to reduce volume.</td>
      </tr>
      <tr>
        <td>Gap Factory</td>
        <td>2</td>
        <td>"60% off + extra 20% + free shipping" / "Last chance 60% off back-to-class essentials (ends tonight)"</td>
        <td>✅ Yes</td>
        <td><span class="badge badge-gray">Delete</span> — Sale ended. Unsubscribe if not shopping Gap regularly.</td>
      </tr>
      <tr>
        <td>Kohl's</td>
        <td>1</td>
        <td>"Up to 85% off clearance STARTS TODAY"</td>
        <td>✅ Yes</td>
        <td><span class="badge badge-gray">Delete</span></td>
      </tr>
      <tr>
        <td>Target Optical</td>
        <td>1</td>
        <td>"Save up to $200 during the Contact Lens Deal Days"</td>
        <td>✅ Yes</td>
        <td><span class="badge badge-yellow">Review</span> — If you need contacts, this deal may be worth checking.</td>
      </tr>
      <tr>
        <td>Quince</td>
        <td>1</td>
        <td>"Just for you — new black tops"</td>
        <td>✅ Yes</td>
        <td><span class="badge badge-gray">Delete / Ignore</span></td>
      </tr>
      <tr>
        <td>Uber</td>
        <td>1</td>
        <td>"Melissa, you have a promo 🎉 — up to 20% off"</td>
        <td>✅ Yes</td>
        <td><span class="badge badge-yellow">Keep / Review</span> — Uber promo codes are useful. Check app before deleting.</td>
      </tr>
      <tr>
        <td>Chick-fil-A</td>
        <td>1</td>
        <td>"Tomorrow, set your alarm to chicken o'clock" (breakfast promo, 402 pts)</td>
        <td>❌ No (In Inbox)</td>
        <td><span class="badge badge-gray">Ignore / Delete</span> — Low priority. Trash after reading.</td>
      </tr>
      <tr>
        <td>Gemma Bonham-Carter</td>
        <td>1</td>
        <td>"$1.5M from one course" — course marketing email</td>
        <td>✅ Yes</td>
        <td><span class="badge badge-gray">Delete / Unsubscribe</span></td>
      </tr>
      <tr>
        <td>Lisa Rangel (Chameleon Resumes)</td>
        <td>1</td>
        <td>"It felt like too much" — resume service marketing</td>
        <td>✅ Yes</td>
        <td><span class="badge badge-yellow">Review</span> — Resume coaching could be relevant to job search. Assess if service is useful.</td>
      </tr>
      <tr style="font-weight:700; background:#f7fafc;">
        <td>TOTAL</td>
        <td>14</td>
        <td>—</td>
        <td>13 in trash, 1 in inbox</td>
        <td>Mostly safe to delete. Target Optical, Uber promos worth a quick check.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════════
     9. NEWSLETTERS & SUBSCRIPTIONS
═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header"><span class="section-icon">📰</span><h2>Newsletters &amp; Subscriptions</h2></div>
  <table>
    <thead>
      <tr><th>Sender</th><th>Topic / Focus</th><th>Today's Subject</th><th>In Trash?</th><th>Recommendation</th></tr>
    </thead>
    <tbody>
      <tr>
        <td>The HR AI Guy (Medium)</td>
        <td>HR + AI leadership tips</td>
        <td>"AI-Generated Birthday Songs That Get the Biggest Reaction"</td>
        <td>❌ No (In Inbox)</td>
        <td><span class="badge badge-green">Keep</span> — Relevant to your HR career and AI interest</td>
      </tr>
      <tr>
        <td>AI For Leaders</td>
        <td>AI strategy for executives</td>
        <td>"You've Already Trained a Robot"</td>
        <td>✅ Yes</td>
        <td><span class="badge badge-green">Keep / Restore</span> — Strong professional development value</td>
      </tr>
      <tr>
        <td>The AI Report (beehiiv)</td>
        <td>AI news &amp; market intel</td>
        <td>"Current AI builds free global web / Netflix $587M Ben Affleck AI startup"</td>
        <td>✅ Yes</td>
        <td><span class="badge badge-yellow">Review</span> — Good market awareness. Keep if you read it regularly.</td>
      </tr>
      <tr>
        <td>TLDR Newsletter</td>
        <td>Tech/AI headlines</td>
        <td>"Meta Anthropic deal, SpaceX Pentagon compute"</td>
        <td>✅ Yes</td>
        <td><span class="badge badge-yellow">Review</span> — Quick daily tech brief. Keep if useful.</td>
      </tr>
      <tr>
        <td>The Hustle</td>
        <td>Business/tech news &amp; stories</td>
        <td>"Protein from thin air, grape seeds to space"</td>
        <td>✅ Yes</td>
