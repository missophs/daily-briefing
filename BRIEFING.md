<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa Weiss — September 8, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px 60px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px 24px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 15px; color: #a0b4cc; margin-top: 6px; }
  .header .meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 18px; }
  .header .meta-item .label { font-size: 11px; color: #8aabcc; text-transform: uppercase; letter-spacing: 0.8px; }
  .header .meta-item .value { font-size: 20px; font-weight: 700; color: #fff; margin-top: 2px; }

  /* SECTION HEADERS */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; color: #1a1a2e; border-left: 5px solid #0f3460; padding-left: 12px; margin-bottom: 14px; text-transform: uppercase; letter-spacing: 0.6px; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; border-left: 5px solid transparent; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }
  .card-red { background: #fff5f5; border-left-color: #e53e3e; }
  .card-yellow { background: #fffbf0; border-left-color: #d69e2e; }
  .card-blue { background: #f0f6ff; border-left-color: #3182ce; }
  .card-green { background: #f0fff4; border-left-color: #38a169; }
  .card-purple { background: #faf5ff; border-left-color: #805ad5; }
  .card-gray { background: #f7f7f7; border-left-color: #a0aec0; }
  .card-orange { background: #fff8f0; border-left-color: #e67e22; }

  .card .card-title { font-weight: 700; font-size: 15px; margin-bottom: 4px; }
  .card .card-meta { font-size: 12px; color: #666; margin-bottom: 8px; }
  .card .card-body { font-size: 13px; line-height: 1.6; }
  .card .card-action { margin-top: 10px; font-size: 12px; font-weight: 600; background: rgba(0,0,0,0.05); border-radius: 6px; padding: 6px 10px; display: inline-block; }

  /* EXEC SUMMARY */
  .exec-summary { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-bottom: 28px; }
  @media(max-width: 700px) { .exec-summary { grid-template-columns: 1fr; } }
  .exec-card { border-radius: 10px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
  .exec-card .icon { font-size: 22px; margin-bottom: 8px; }
  .exec-card .title { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.7px; margin-bottom: 6px; }
  .exec-card .body { font-size: 13px; line-height: 1.5; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,0.07); margin-bottom: 14px; }
  th { background: #1a1a2e; color: #fff; padding: 10px 14px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.6px; }
  td { padding: 9px 14px; border-bottom: 1px solid #eee; font-size: 13px; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f8f9ff; }
  .badge { display: inline-block; border-radius: 12px; padding: 2px 10px; font-size: 11px; font-weight: 700; }
  .badge-red { background: #fed7d7; color: #c53030; }
  .badge-yellow { background: #fefcbf; color: #975a16; }
  .badge-green { background: #c6f6d5; color: #276749; }
  .badge-blue { background: #bee3f8; color: #2a4a7f; }
  .badge-purple { background: #e9d8fd; color: #553c9a; }
  .badge-gray { background: #e2e8f0; color: #4a5568; }
  .badge-orange { background: #feebc8; color: #c05621; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { background: #0f3460; color: #fff; border-radius: 8px 8px 0 0; padding: 8px 16px; font-weight: 700; font-size: 14px; }
  .cal-event { background: #fff; border-left: 4px solid #3182ce; padding: 10px 16px; border-bottom: 1px solid #eee; }
  .cal-event:last-child { border-bottom: none; border-radius: 0 0 8px 8px; }
  .cal-event .time { font-weight: 700; color: #0f3460; font-size: 13px; }
  .cal-event .name { font-weight: 600; font-size: 14px; }
  .cal-event .detail { font-size: 12px; color: #555; margin-top: 3px; }
  .cal-event.declined { border-left-color: #e53e3e; background: #fff8f8; }
  .cal-event.needs-action { border-left-color: #d69e2e; background: #fffdf0; }
  .cal-event.interview { border-left-color: #38a169; background: #f0fff4; }
  .cal-event.alert { border-left-color: #e53e3e; }

  /* TRIAGE TABLE */
  .triage-status { font-weight: 700; white-space: nowrap; }
  .row-rescued { background: #f0fff4; }
  .row-inbox { background: #f0f6ff; }
  .row-autotrash { background: #fff8f0; }
  .row-trash { background: #f7f7f7; }

  /* DASHBOARD GRID */
  .dashboard-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }
  @media(max-width: 800px) { .dashboard-grid { grid-template-columns: repeat(2, 1fr); } }
  @media(max-width: 450px) { .dashboard-grid { grid-template-columns: 1fr; } }
  .dash-tile { border-radius: 10px; padding: 16px 18px; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.08); }
  .dash-tile .big { font-size: 32px; font-weight: 800; }
  .dash-tile .label { font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.6px; margin-top: 4px; }

  /* TOP 3 */
  .top3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
  @media(max-width: 700px) { .top3 { grid-template-columns: 1fr; } }
  .top3-card { border-radius: 12px; padding: 20px; box-shadow: 0 3px 10px rgba(0,0,0,0.10); color: #fff; }
  .top3-card .num { font-size: 40px; font-weight: 900; opacity: 0.25; line-height: 1; }
  .top3-card .t { font-size: 15px; font-weight: 700; margin: 4px 0; }
  .top3-card .d { font-size: 13px; opacity: 0.9; }

  /* DIVIDER */
  .divider { height: 2px; background: linear-gradient(90deg, #0f3460, transparent); border: none; margin: 32px 0 24px; border-radius: 2px; }

  /* PILL */
  .pill { display: inline-block; border-radius: 20px; padding: 3px 12px; font-size: 11px; font-weight: 700; margin-right: 4px; margin-top: 3px; }
  .pill-red { background: #fed7d7; color: #c53030; }
  .pill-green { background: #c6f6d5; color: #276749; }
  .pill-blue { background: #bee3f8; color: #2a4a7f; }
  .pill-yellow { background: #fefcbf; color: #975a16; }
  .pill-gray { background: #e2e8f0; color: #4a5568; }
  .pill-purple { background: #e9d8fd; color: #553c9a; }

  .note { font-size: 12px; color: #666; font-style: italic; margin-top: 6px; }
  .warn { color: #c53030; font-weight: 700; }
  .good { color: #276749; font-weight: 700; }
  .info-box { background: #e8f4fd; border-left: 4px solid #3182ce; border-radius: 6px; padding: 10px 14px; font-size: 13px; margin-bottom: 12px; }
  .warn-box { background: #fff5f5; border-left: 4px solid #e53e3e; border-radius: 6px; padding: 10px 14px; font-size: 13px; margin-bottom: 12px; }
  .success-box { background: #f0fff4; border-left: 4px solid #38a169; border-radius: 6px; padding: 10px 14px; font-size: 13px; margin-bottom: 12px; }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ═══════════════════════════════════════════════════════
     SECTION 0 — EMAIL TRIAGE QUICK LIST
══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📋 Email Triage Quick List</div>
  <p class="note" style="margin-bottom:10px;">Rescued emails first → Inbox emails → Collapsed trash rows at bottom. All 50 emails accounted for.</p>
  <table>
    <thead>
      <tr>
        <th style="width:130px;">Status</th>
        <th style="width:220px;">From</th>
        <th>Subject</th>
        <th>Summary</th>
      </tr>
    </thead>
    <tbody>
      <!-- RESCUED -->
      <tr class="row-rescued">
        <td class="triage-status">✅ RESCUED</td>
        <td>Google (noreply-accounts@google.com)</td>
        <td>You shared some Google Account data with makebestmusic</td>
        <td>Google security alert — Melissa connected her Google account to makebestmusic. Important account activity to review.</td>
      </tr>
      <tr class="row-rescued">
        <td class="triage-status">✅ RESCUED</td>
        <td>Suno (suno@creators.suno.com)</td>
        <td>Welcome to Suno!</td>
        <td>Welcome/account confirmation from Suno creative platform — confirms successful registration.</td>
      </tr>
      <tr class="row-rescued">
        <td class="triage-status">✅ RESCUED</td>
        <td>Google (noreply-accounts@google.com)</td>
        <td>You shared some Google Account data with Suno</td>
        <td>Google security alert — Melissa connected her Google account to Suno. Account activity to review.</td>
      </tr>
      <!-- INBOX -->
      <tr class="row-inbox">
        <td class="triage-status">📥 INBOX</td>
        <td>OkCupid (bounces@alerts.oknotify3.com)</td>
        <td>Someone likes you</td>
        <td>Dating app notification — someone liked Melissa's profile. Low priority personal.</td>
      </tr>
      <tr class="row-inbox">
        <td class="triage-status">📥 INBOX</td>
        <td>Inclusively (contactus@inclusively.com)</td>
        <td>melissa weiss - Check out these recommended jobs for you!</td>
        <td>Job platform recommendations based on profile — review for relevant HR roles.</td>
      </tr>
      <tr class="row-inbox">
        <td class="triage-status">📥 INBOX</td>
        <td>Slack (no-reply@slack.com)</td>
        <td>You have 3 more days to access Slack's premium features (×2)</td>
        <td>Slack Pro trial ends Sept 10. Two duplicate notices — decision needed on upgrade or downgrade. <span class="warn">Deadline in 2 days.</span></td>
      </tr>
      <tr class="row-inbox">
        <td class="triage-status">📥 INBOX</td>
        <td>LinkedIn Job Alerts (jobalerts-noreply@linkedin.com)</td>
        <td>Lead HR Business Partner at Circle and 5 more</td>
        <td>Strong HR leadership job alert including Circle (NYSE: CRCL). High fit — review ASAP.</td>
      </tr>
      <tr class="row-inbox">
        <td class="triage-status">📥 INBOX</td>
        <td>LinkedIn (updates-noreply@linkedin.com)</td>
        <td>Jill Rosenfeld — Cyperus Group Managing Director posted</td>
        <td>Recruiter/industry contact post about candidate contention — networking signal worth reading.</td>
      </tr>
      <tr class="row-inbox">
        <td class="triage-status">📥 INBOX</td>
        <td>Coursiv (no-reply@updates.coursiv.co)</td>
        <td>Your plan isn't active yet</td>
        <td>Coursiv plan saved but not activated — one step remaining. Follow up to complete setup.</td>
      </tr>
      <tr class="row-inbox">
        <td class="triage-status">📥 INBOX</td>
        <td>fran W (franw516@gmail.com)</td>
        <td>(no subject)</td>
        <td>Personal email from Fran — no subject or body snippet. May require a reply or follow-up.</td>
      </tr>
      <!-- COLLAPSED TRASH ROWS -->
      <tr class="row-autotrash">
        <td class="triage-status">🗑 TRASHED (auto)</td>
        <td colspan="2"><strong>5 emails auto-trashed (phishing/scams)</strong> — see Trash Review &amp; Security section</td>
        <td>Includes: fake cloud lockout, 419 scam, spoofed self-send, adult spam (×2). All removed automatically.</td>
      </tr>
      <tr class="row-trash">
        <td class="triage-status">🗂 TRASH (manual)</td>
        <td colspan="2"><strong>36 emails in Trash</strong> — see Trash Review, Promotions &amp; Newsletters sections</td>
        <td>Mix of retail promotions, newsletters, job digests, and low-value notifications already in trash.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════
     SECTION 1 — HEADER
══════════════════════════════════════════════════════════ -->
<div class="header">
  <h1>☀️ Good Morning, Melissa</h1>
  <div class="subtitle">Executive Briefing — Prepared by your Chief of Staff</div>
  <div class="meta">
    <div class="meta-item"><div class="label">Date</div><div class="value">Tuesday, Sept 8, 2026</div></div>
    <div class="meta-item"><div class="label">Emails Reviewed</div><div class="value">50</div></div>
    <div class="meta-item"><div class="label">Calendar Events</div><div class="value">11</div></div>
    <div class="meta-item"><div class="label">Action Items</div><div class="value">8</div></div>
    <div class="meta-item"><div class="label">Interviews This Week</div><div class="value">1 🎯</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     SECTION 2 — EXECUTIVE SUMMARY
══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📊 Executive Summary</div>
  <div class="exec-summary">
    <div class="exec-card card-red">
      <div class="icon">🔴</div>
      <div class="title">Biggest Risk</div>
      <div class="body">5 phishing/scam emails were auto-trashed including a fake cloud lockout, a 419 advance-fee scam, and a spoofed self-send from your own Gmail address — possible account probe. Two new third-party Google Account connections (Suno, makebestmusic) also need review.</div>
    </div>
    <div class="exec-card card-green">
      <div class="icon">🟢</div>
      <div class="title">Biggest Opportunity</div>
      <div class="body"><strong>CUNY Vice Chancellor of HR Interview is THIS FRIDAY, Sept 11</strong> at CUNY Central Office (3–5 PM). This is a major role. LinkedIn alerts also surfaced Lead HR BP at Circle (NYSE) and 5 more strong leads. You also sent a VP HRBP application to Amy this morning — strong momentum.</div>
    </div>
    <div class="exec-card card-blue">
      <div class="icon">🔵</div>
      <div class="title">Biggest Calendar Item</div>
      <div class="body">CUNY interview Friday Sept 11 (3–5 PM, two back-to-back slots) is the week's centerpiece. Before that: Nails today at 10 AM, HR Networking Group tomorrow (RSVP pending), M&amp;M meeting Thursday. Slack Pro trial expires Sept 10 — decide before then.</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     SECTION 3 — ACTION REQUIRED
══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">⚡ Action Required</div>

  <div class="card card-red">
    <div class="card-title">🔐 SECURITY — Review New Third-Party App Connections</div>
    <div class="card-meta">Source: Google (noreply-accounts@google.com) × 2 — Rescued from Trash</div>
    <div class="card-body">Your Google account was connected to <strong>makebestmusic</strong> and <strong>Suno</strong> via Sign In with Google. If you authorized these, no action needed beyond awareness. If either was unexpected, revoke access immediately at <strong>myaccount.google.com → Security → Third-party apps</strong>.</div>
    <div class="card-action">→ Visit myaccount.google.com/permissions to verify both apps | Due: Today</div>
  </div>

  <div class="card card-red">
    <div class="card-title">🚨 SECURITY — Spoofed Self-Send from Your Gmail Address</div>
    <div class="card-meta">Source: Melissa W &lt;melissaw212@gmail.com&gt; — Auto-Trashed (Phishing)</div>
    <div class="card-body">An email was sent from your own Gmail address containing an unformatted tracking URL with unfilled template variables — a strong indicator of account probing or spoofing. Auto-trashed. <strong>Change your Gmail password and review recent login activity.</strong></div>
    <div class="card-action">→ Go to myaccount.google.com → Security → Recent activity | Due: Today, Urgent</div>
  </div>

  <div class="card card-yellow">
    <div class="card-title">⏰ DEADLINE — Slack Pro Trial Expires September 10</div>
    <div class="card-meta">Source: Slack (no-reply@slack.com) — 2 duplicate emails in Inbox</div>
    <div class="card-body">Your Slack Pro trial for "performance" ends September 10 — just 2 days away. Decide whether to upgrade (paid plan) or let it downgrade to the free tier. Two duplicate notices received; likely a send error on Slack's end.</div>
    <div class="card-action">→ Log into Slack admin and decide upgrade vs. free | Due: Sept 10</div>
  </div>

  <div class="card card-green">
    <div class="card-title">🎯 INTERVIEW PREP — CUNY Vice Chancellor of Human Resources</div>
    <div class="card-meta">Source: Google Calendar — Confirmed | Sept 11, 3:00–5:00 PM | CUNY Central Office</div>
    <div class="card-body">You have two back-to-back interview slots confirmed for Friday. Interviewers: <strong>Elisa Russo</strong> and <strong>Sujata Malhotra</strong>. Location: CUNY Central Office. This is a VP/Executive-level HR role at a major public university system. Prep is essential.</div>
    <div class="card-action">→ Research CUNY HR strategy, prepare STAR stories for PE restructuring / attrition wins | Due: By Thursday EOD</div>
  </div>

  <div class="card card-yellow">
    <div class="card-title">📅 RSVP PENDING — HR Networking &amp; Job Search Group (Zoom)</div>
    <div class="card-meta">Source: Google Calendar — Status: Needs Action | Sept 9, 12:00–1:30 PM</div>
    <div class="card-body">Tomorrow's HR Networking Zoom session has your RSVP as "needs action." Large group (150+ peers). Given your active job search, this is a high-value networking opportunity. Confirm or decline today.</div>
    <div class="card-action">→ RSVP via calendar invite | Due: Today</div>
  </div>

  <div class="card card-green">
    <div class="card-title">📬 REVIEW — LinkedIn Job Alert: Lead HR BP at Circle (NYSE) + 5 More</div>
    <div class="card-meta">Source: LinkedIn Job Alerts (jobalerts-noreply@linkedin.com) — In Inbox</div>
    <div class="card-body">Circle (NYSE: CRCL) is a leading fintech company. Lead HR Business Partner is a strong match for Melissa's HRBP leader profile. Five additional roles also included — review for fit before they close.</div>
    <div class="card-action">→ Open alert, apply to top fits today | Due: Today</div>
  </div>

  <div class="card card-yellow">
    <div class="card-title">⚙️ INCOMPLETE SETUP — Coursiv Plan Not Activated</div>
    <div class="card-meta">Source: Coursiv (no-reply@updates.coursiv.co) — In Inbox</div>
    <div class="card-body">Your Coursiv plan (#-20260908) is saved but not yet activated. One step remaining. If you intended to enroll, complete the setup; otherwise cancel to avoid any billing.</div>
    <div class="card-action">→ Log into Coursiv and activate or cancel | Due: This week</div>
  </div>

  <div class="card card-yellow">
    <div class="card-title">📩 FOLLOW-UP — Email from Fran W (No Subject/Body)</div>
    <div class="card-meta">Source: fran W &lt;franw516@gmail.com&gt; — In Inbox</div>
    <div class="card-body">Personal email arrived with no subject line and no body content. Could be an accidental send, a forwarded attachment that didn't render, or a genuine message that got cut off. Follow up with Fran to confirm.</div>
    <div class="card-action">→ Reply to Fran asking if she meant to send something | Due: Today</div>
  </div>

</div>

<hr class="divider">

<!-- ═══════════════════════════════════════════════════════
     SECTION 4 — FULL 7-DAY CALENDAR
══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📅 Full 7-Day Calendar</div>

  <!-- TUESDAY SEPT 8 -->
  <div class="cal-day">
    <div class="cal-day-header">Tuesday, September 8, 2026 — TODAY</div>
    <div class="cal-event">
      <div class="time">10:00 AM – 11:00 AM</div>
      <div class="name">💅 Nails</div>
      <div class="detail">
        <span class="badge badge-green">Confirmed</span>
        &nbsp;Personal appointment. No location listed. No action needed.
      </div>
    </div>
  </div>

  <!-- WEDNESDAY SEPT 9 -->
  <div class="cal-day">
    <div class="cal-day-header">Wednesday, September 9, 2026</div>
    <div class="cal-event needs-action">
      <div class="time">12:00 PM – 1:30 PM</div>
      <div class="name">🤝 HR Networking &amp; Job Search Group — Zoom 2</div>
      <div class="detail">
        <span class="badge badge-yellow">⚠️ RSVP NEEDED</span>
        &nbsp;<strong>Zoom:</strong> <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Join Meeting</a><br>
        150+ attendees. Weekly HR job-search peer network. <strong>Prep:</strong> Review team guidelines linked in calendar description. RSVP required today.
      </div>
    </div>
    <div class="cal-event">
      <div class="time">12:00 PM – 1:30 PM</div>
      <div class="name">🤝 Network</div>
      <div class="detail">
        <span class="badge badge-green">Confirmed</span>
        &nbsp;Duplicate/companion event to HR Networking Zoom. No location. Likely self-reminder block.
      </div>
    </div>
  </div>

  <!-- THURSDAY SEPT 10 -->
  <div class="cal-day">
    <div class="cal-day-header">Thursday, September 10, 2026</div>
    <div class="cal-event declined">
      <div class="time">9:00 AM – 10:30 AM</div>
      <div class="name">❌ Executive Roundtable (DECLINED)</div>
      <div class="detail">
        <span class="badge badge-red">Declined</span>
        &nbsp;Hosted by <strong>John Madigan</strong> via Zoom.<br>
        <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> | Meeting ID: 207 786 667 | PW: 205454<br>
        You declined this event. No action required unless you wish to reconsider.
      </div>
    </div>
    <div class="cal-event needs-action">
      <div class="time">12:00 PM – 1:00 PM</div>
      <div class="name">🤝 HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
      <div class="detail">
        <span class="badge badge-yellow">⚠️ RSVP NEEDED</span>
        &nbsp;<strong>Zoom:</strong> <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Join Meeting</a><br>
        Open office hours / informal networking. <strong>Note:</strong> AI notetaking tools should be turned off per organizer. Good opportunity to discuss Friday's CUNY prep.<br>
        <span class="warn">⚠️ Slack Pro trial ALSO expires today — handle that before this meeting.</span>
      </div>
    </div>
    <div class="cal-event">
      <div class="time">1:00 PM – 2:00 PM</div>
      <div class="name">🤝 M&amp;M Meeting</div>
      <div class="detail">
        <span class="badge badge-green">Accepted</span>
        &nbsp;Attendee: <strong>monte.montoya@gmail.com</strong>. No description. Personal or professional 1:1. Clarify agenda if needed ahead of time.
      </div>
    </div>
  </div>

  <!-- FRIDAY SEPT 11 — HIGH PRIORITY -->
  <div class="cal-day">
    <div class="cal-day-header">⭐ Friday, September 11, 2026 — INTERVIEW DAY</div>
    <div class="cal-event">
      <div class="time">9:30 AM – 10:30 AM</div>
      <div class="name">🏃 PT (Physical Therapy)</div>
      <div class="detail">
        <span class="badge badge-green">Confirmed</span>
        &nbsp;Personal/health appointment in the morning. Good buffer before afternoon interviews.
      </div>
    </div>
    <div class="cal-event interview">
      <div class="time">3:00 PM – 4:00 PM</div>
      <div class="name">🎯 INTERVIEW — Vice Chancellor of Human Resources (Appointment with Elisa Russo &amp; Sujata Malhotra)</div>
      <div class="detail">
        <span class="badge badge-green">Confirmed</span>
        &nbsp;<strong>Location:</strong> CUNY Central Office, 205 E 42nd St, New York, NY<br>
        <strong>Interviewers:</strong> Elisa Russo, Sujata Malhotra<br>
        <strong>Prep Needed:</strong> Research CUNY HR priorities, prepare restructuring/attrition stories (40% cut at Cprime), rehearse STAR method answers, bring copies of resume, arrive 10–15 min early.
      </div>
    </div>
    <div class="cal-event interview">
      <div class="time">4:00 PM – 5:00 PM</div>
      <div class="name">🎯 INTERVIEW — Vice Chancellor of Human Resources (Second Block — Accepted)</div>
      <div class="detail">
        <span class="badge badge-green">Accepted</span>
        &nbsp;Back-to-back second interview hour at CUNY Central Office. Teams meeting link available.<br>
        <span class="warn">⚠️ Conflict Note:</span> Two calendar entries show 3–4 PM and 4–5 PM for the same role — this appears intentional (two interview panels). Confirm with CUNY if both slots are sequential with the same or different interviewers.
      </div>
    </div>
  </div>

  <!-- MON SEPT 14 -->
  <div class="cal-day">
    <div class="cal-day-header">Monday, September 14, 2026</div>
    <div class="cal-event">
      <div class="time">8:45 AM – 9:40 AM (Appointment Time: 9:00 AM)</div>
      <div class="name">🏥 New Patient Visit — Dr. Andrea D. Card</div>
      <div class="detail">
        <span class="badge badge-green">Accepted</span>
        &nbsp;<strong>Location:</strong> 53 W 23rd St, 6th Floor, New York, NY 10010 | Phone: 212-746-2900<br>
        <strong>Prep:</strong> Arrive at 8:45 AM. Bring insurance card, ID, and any prior medical records. Office may contact you in advance to verify insurance coverage.
      </div>
    </div>
  </div>

</div>

<hr class="divider">

<!-- ═══════════════════════════════════════════════════════
     SECTION 5 — JOB SEARCH & INTERVIEW PIPELINE
══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">🎯 Job Search &amp; Interview Pipeline</div>

  <div class="success-box">🏆 <strong>CUNY Vice Chancellor of HR — Interview this Friday, Sept 11 at 3–5 PM.</strong> This is your most advanced and highest-priority opportunity this week.</div>

  <table>
    <thead>
      <tr>
        <th>Opportunity</th>
        <th>Source</th>
        <th>Status</th>
        <th>Fit</th>
        <th>Next Step</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Vice Chancellor of Human Resources — CUNY</strong></td>
        <td>Calendar / Booking</td>
        <td><span class="badge badge-green">Interview Fri Sept 11</span></td>
        <td><span class="badge badge-green">HIGH</span></td>
        <td>Prep STAR stories, research CUNY strategy, confirm location &amp; both interview blocks</td>
      </tr>
      <tr>
        <td><strong>VP, HR Business Partner Leader — [Amy's Company]</strong></td>
        <td>Gmail (sent by Melissa)</td>
        <td><span class="badge badge-blue">Application Sent</span></td>
        <td><span class="badge badge-green">HIGH</span></td>
        <td>Monitor for reply from Amy; follow up in 3–5 business days if no response</td>
      </tr>
      <tr>
        <td><strong>Lead HR Business Partner — Circle (NYSE: CRCL)</strong></td>
        <td>LinkedIn Job Alert — Inbox</td>
        <td><span class="badge badge-yellow">New — Not Applied</span></td>
        <td><span class="badge badge-green">HIGH</span></td>
        <td>Open alert, review JD, apply today if strong fit</td>
      </tr>
      <tr>
        <td><strong>5 Additional Roles — LinkedIn Alert</strong></td>
        <td>LinkedIn Job Alert — Inbox</td>
        <td><span class="badge badge-yellow">New — Not Applied</span></td>
        <td><span class="badge badge-blue">MEDIUM</span></td>
        <td>Review each for fit; apply to top 2–3</td>
      </tr>
      <tr>
        <td><strong>Cove HR Manager — Communities Overcoming Violent Encounters &amp; 6 more</strong></td>
        <td>Glassdoor (in Trash)</td>
        <td><span class="badge badge-gray">In Trash</span></td>
        <td><span class="badge badge-gray">LOW</span></td>
        <td>Glassdoor digest in Trash — restore if interested in nonprofit HR manager roles</td>
      </tr>
      <tr>
        <td><strong>Recommended Jobs — Inclusively</strong></td>
        <td>Inclusively — Inbox</td>
        <td><span class="badge badge-yellow">Review Needed</span></td>
        <td><span class="badge badge-blue">MEDIUM</span></td>
        <td>Open email and scan recommendations for disability-inclusive employer roles matching VP HRBP profile</td>
      </tr>
      <tr>
        <td><strong>Ladders Resume — Stale Profile</strong></td>
        <td>Ladders (not in inbox)</td>
        <td><span class="badge badge-red">Stale — Last Updated Dec 2016</span></td>
        <td><span class="badge badge-blue">MEDIUM</span></td>
        <td>Update Ladders profile — 10-year-old resume is hurting discoverability on that platform</td>
      </tr>
      <tr>
        <td><strong>HR Networking Group — Zoom (Wed Sept 9)</strong></td>
        <td>Calendar — Needs Action</td>
        <td><span class="badge badge-yellow">RSVP Pending</span></td>
        <td><span class="badge badge-green">HIGH (Networking)</span></td>
        <td>RSVP today; use session to share CUNY opportunity and collect leads</td>
      </tr>
      <tr>
        <td><strong>HR Open Office Hours — Zoom (Thu Sept 10)</strong></td>
        <td>Calendar — Needs Action</td>
        <td><span class="badge badge-yellow">RSVP Pending</span></td>
        <td><span class="badge badge-green">HIGH (Networking)</span></td>
        <td>RSVP today; use session for CUNY interview prep support</td>
      </tr>
      <tr>
        <td><strong>Jill Rosenfeld (Cyperus Group) LinkedIn Post</strong></td>
        <td>LinkedIn — Inbox</td>
        <td><span class="badge badge-blue">Awareness</span></td>
        <td><span class="badge badge-blue">MEDIUM</span></td>
        <td>Read post (about candidate contention); consider engaging / commenting to build visibility</td>
      </tr>
    </tbody>
  </table>
</div>

<hr class="divider">

<!-- ═══════════════════════════════════════════════════════
     SECTION 6 — FULL EMAIL REVIEW BY CATEGORY
══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📬 Full Email Review by Category</div>

  <!-- SECURITY / RISK -->
  <div class="card card-red">
    <div class="card-title">🔐 Security / Risk — 5 Emails</div>
    <div class="card-meta">Auto-trashed: 4 | Rescued: 2 | Active concern: 1</div>
    <div class="card-body">
      <p><strong>✅ RESCUED — Google Security: makebestmusic</strong> — Your Google account was shared with makebestmusic app. Verify you authorized this at myaccount.google.com.</p>
      <p style="margin-top:6px;"><strong>✅ RESCUED — Google Security: Suno</strong> — Your Google account was shared with Suno creative platform. Same verification step advised.</p>
      <p style="margin-top:6px;"><strong>🗑 AUTO-TRASHED — Fake Cloud Lockout</strong> (info@ykqwtclekicjc) — Spoofed "Payment_Declined" sender. Classic credential harvesting. Removed. No action.</p>
      <p style="margin-top:6px;"><strong>🗑 AUTO-TRASHED — 419 Advance Fee Scam</strong> (MA, info@promisegcc.com) — "SHK Mubarak from Qatar" profit venture scam. Removed. No action.</p>
      <p style="margin-top:6px;"><strong>🗑 AUTO-TRASHED — Spoofed Self-Send</strong> (melissaw212@gmail.com) — Email from your own address with unfilled tracking URL. Possible account compromise. <span class="warn">Change password immediately.</span></p>
    </div>
    <div class="card-action">→ Review Google account permissions + change Gmail password today</div>
  </div>

  <!-- JOB SEARCH -->
  <div class="card card-green">
    <div class="card-title">💼 Job Search — 6 Emails</div>
    <div class="card-meta">In Inbox: 3 | Sent: 1 | Trash: 1 | Other: 1</div>
    <div class="card-body">
      <p><strong>VP HRBP Leader Application (Melissa → Amy)</strong> — Sent 7:29 AM. Strong cover-letter framing with 40% attrition reduction at Cprime during PE restructuring. Follow up in 3–5 days.</p>
      <p style="margin-top:6px;"><strong>LinkedIn Job Alert: Lead HR BP at Circle + 5 More</strong> — In Inbox. Circle (NYSE: CRCL) fintech — high fit. Review today.</p>
      <p style="margin-top:6px;"><strong>Inclusively: Recommended Jobs</strong> — In Inbox. Disability-inclusive employer network jobs for melissa weiss profile. Review for senior HR roles.</p>
      <p style="margin-top:6px;"><strong>Glassdoor Alert: Cove HR Manager + 6 More</strong> — In Trash. Nonprofit HR manager roles may be below target level. Low priority.</p>
      <p style="margin-top:6px;"><strong>Ladders Resume Report</strong> — Resume is stale (last updated Dec 2016). Update Ladders profile to improve discoverability.</p>
      <p style="margin-top:6px;"><strong>Job Search Unlocked Substack</strong> (in Trash) — "Cultural Fit Predicts Nothing a CEO Cares About" — 30 years of hiring data. Potentially useful insight for interviews.</p>
    </div>
    <div class="card-action">→ Apply to Circle today; update Ladders profile; rescue Glassdoor email if interested</div>
  </div>

  <!-- RECRUITERS / NETWORKING -->
  <div class="card card-green">
    <div class="card-title">🤝 Recruiters / Networking — 2 Emails</div>
    <div class="card-meta">In Inbox: 1 | Sent: 0</div>
    <div class="card-body">
      <p><strong>LinkedIn: Jill Rosenfeld (Cyperus Group, Managing Director)</strong> — In Inbox. Post about candidate contention — relevant content for active job seekers. Engaging may increase visibility with this recruiter.</p>
      <p style="margin-top:6px;"><strong>Coursiv: Plan Not Activated</strong> — In Inbox. Unclear if this is a job search tool or professional development platform. Complete setup or cancel to avoid accidental billing.</p>
    </div>
    <div class="card-action">→ Read Jill Rosenfeld's post and consider engaging; resolve Coursiv plan</div>
  </div>

  <!-- CALENDAR / EVENTS -->
  <div class="card card-blue">
    <div class="card-title">📅 Calendar / Events — 2 Emails</div>
    <div class="card-meta">Decision Required: 1 | FYI: 1</div>
    <div class="card-body">
      <p><strong>Slack Pro Trial Expiring (×2 duplicate emails)</strong> — Trial for "performance" workspace ends September 10. Two nearly identical emails sent 2 minutes apart — likely a Slack send glitch. Only one action needed: decide upgrade vs. free plan by Sept 10.</p>
    </div>
    <div class="card-action">→ Log into Slack admin before Sept 10 and make the call on Pro vs. Free</div>
  </div>

  <!-- MEDICAL / HEALTH -->
  <div class="card card-blue">
    <div class="card-title">🏥 Medical / Health — 1 Email</div>
    <div class="card-meta">In Inbox/Calendar: Confirmed appointment Sept 14</div>
    <div class="card-body">
      <p><strong>New Patient Visit with Dr. Andrea D. Card</strong> — Sept 14, 9:00 AM at 53 W 23rd St, 6th Floor. Phone: 212-746-2900. Arrive 8:45 AM. Bring insurance info. Office may reach out ahead to verify coverage. Already on calendar and accepted.</p>
    </div>
    <div class="card-action">→ Confirm insurance; prepare any relevant medical history for new patient intake</div>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="card card-yellow">
    <div class="card-title">💳 Financial / Billing — 1 Email</div>
    <div class="card-meta">Deadline: Sept 10</div>
    <div class="card-body">
      <p><strong>Slack Pro Trial — Billing Decision</strong> — If no action, workspace may auto-downgrade or auto-charge depending on Slack settings. Review billing settings before trial ends Sept 10.</p>
    </div>
    <div class="card-action">→ Check Slack billing settings to avoid surprise charge | Due: Sept 10</div>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="card card-purple">
    <div class="card-title">📚 Professional Development — 3 Emails</div>
    <div class="card-meta">Trash: 2 | Inbox: 1</div>
    <div class="card-body">
      <p><strong>Job Search Unlocked (Substack, in Trash)</strong> — "Cultural Fit Predicts Nothing a CEO Cares About." 30 years of hiring data — genuinely useful insight for CUNY interview prep. Consider rescuing.</p>
      <p style="margin-top:6px;"><strong>Vaishali Lambe — Designing Trust: Ethical Review and Leadership in AI Innovation (Medium, in Trash)</strong> — Relevant to HR tech leadership. Low urgency but worth reading this week.</p>
      <p style="margin-top:6px;"><strong>Coursiv — Plan Not Activated (Inbox)</strong> — If Coursiv is a professional skills platform, activating it could support job search or skills development.</p>
    </div>
    <div class="card-action">→ Rescue Job Search Unlocked email for CUNY prep context; evaluate Coursiv</div>
  </div>

  <!-- PERSONAL -->
  <div class="card card-blue">
    <div class="card-title">👤 Personal — 4 Emails</div>
    <div class="card-meta">In Inbox: 2 | Not in Inbox: 2</div>
    <div class="card-body">
      <p><strong>Fran W (franw516@gmail.com)</strong> — In Inbox. Empty subject, no body. Follow up to ask if she meant to send something.</p>
      <p style="margin-top:6px;"><strong>OkCupid — Someone likes you</strong> — In Inbox. Dating app notification. Personal, low priority.</p>
      <p style="margin-top:6px;"><strong>Match — Michael viewed your profile (66, New Rochelle)</strong> — Not in inbox. Dating app notification. Personal, read.</p>
      <p style="margin-top:6px;"><strong>ChatGPT — Temporary Login Code (310212)</strong> — Not in inbox. One-time login code already used. No action needed.</p>
    </div>
    <div class="card-action">→ Reply to Fran W; dating app notifications — personal discretion</div>
  </div>

  <!-- NEWSLETTERS / SUBSCRIPTIONS -->
  <div class="card card-purple">
    <div class="card-title">📰 Newsletters / Subscriptions — 5 Emails</div>
    <div class="card-meta">All in Trash</div>
    <div class="card-body">
      <p><strong>Dylan's Diary — "The Three Moats Worth Owning"</strong> (Trash) — Investment/finance newsletter. Evaluate subscription relevance.</p>
      <p style="margin-top:6px;"><strong>The Daily Skimm — "Before you buy another water bottle"</strong> (Trash) — Lifestyle/news digest with GLP-1 ad partnership.</p>
      <p style="margin-top:6px;"><strong>The Signal by TradeAlgo — NHS crisis / healthcare</strong> (Trash) — Markets + healthcare capacity crisis newsletter.</p>
      <p style="margin-top:6px;"><strong>TriNet — "HR challenges grow fast"</strong> (Trash) — HR vendor promotional newsletter.</p>
      <p style="margin-top:6px;"><strong>Justyn The AI Guy — "The business collapsed"</strong> (Trash) — Business/entrepreneurship newsletter email.</p>
    </div>
    <div class="card-action">→ See Newsletters section for individual recommendations; consider unsubscribing to reduce inbox volume</div>
  </div>

  <!-- PROMOTIONAL / RETAIL -->
  <div class="card card-gray">
    <div class="card-title">🛍 Promotional / Retail — 14 Emails</div>
    <div class="card-meta">All in Trash</div>
    <div class="card-body">
      Kohl's, Gap Factory (×3), Amazon (×3), SHEIN, Quince, YesStyle, NiceToMeet, Higgsfield, makebestmusic, HomeAgain PetRescuers. All are promotional retail or lifestyle emails already in Trash. See Promotional / Retail Summary section for details.
    </div>
    <div class="card-action">→ All in Trash — safe to delete; unsubscribe to reduce future volume</div>
  </div>

  <!-- SPAM / MALICIOUS — NOT AUTO-TRASHED -->
  <div class="card card-red">
    <div class="card-title">🚫 Spam / Malicious (Not Auto-Trashed) — 7 Emails</div>
    <div class="card-meta">In Inbox or Not in Inbox, Not in Trash — Require Manual Trash</div>
    <div class="card-body">
      <p><strong>"Sex Trick" (apciesrpjoprqw...)</strong> — Adult spam, random domain. Trash &amp; mark spam.</p>
      <p style="margin-top:4px;"><strong>"Congratulations 🎉 RE: 130 Free Spins" (info@mycwtngrrfaoy)</strong> — Casino spam. Trash &amp; mark spam.</p>
      <p style="margin-top:4px;"><strong>💦FUCK💧ME💦 (hcsupportnwml@ayqcytkfmybtuvqrceujnzmi.com)</strong> — Explicit adult spam. Trash &amp; mark spam.</p>
      <p style="margin-top:4px;"><strong>💰MIAMI-CLUB (ghfsupportjr@zrtwizkoqplnjwlbtvfpyfmy.com)</strong> — Already in Trash. Casino winner scam.</p>
      <p style="margin-top:4px;"><strong>GLP-1 by DirectMeds (hlsupportgriz@hrxxlgyafpvaiigojnltauhg.com)</strong> — Fake pharma spam. Trash &amp; mark spam.</p>
      <p style="margin-top:4px;"><strong>GLP-1by.DirectMeds (xpyinohgmufakc...)</strong> — Duplicate fake pharma spam from spoofed domain. Trash &amp; mark spam.</p>
      <p style="margin-top:4px;"><strong>WATCH THIS FILTHY +18 VIDEO (cdsupporttknv@jrsgzodnmhediqxpqmydoajh.com)</strong> — Explicit adult spam with spoofed Gmail username. Trash &amp; mark spam.</p>
    </div>
    <div class="card-action">→ Manually trash + report as spam all of the above immediately</div>
  </div>

  <!-- MISC / OTHER -->
  <div class="card card-gray">
    <div class="card-title">📍 Misc / Alerts — 2 Emails</div>
    <div class="card-meta">FYI — no action required</div>
    <div class="card-body">
      <p><strong>Notify NYC — Missing Vulnerable Adult Alert: James Dean Lawrence</strong> — 89-year-old missing from Port Jefferson area. NYC emergency alert system. Read and be aware. No action required unless you have relevant information.</p>
      <p style="margin-top:6px;"><strong>popcornpotential.com.au — "Don't Follow Me… Except This Time"</strong> (Trash) — Inspirational/coaching newsletter. Low priority.</p>
    </div>
    <div class="card-action">→ FYI only</div>
  </div>

</div>

<hr class="divider">

<!-- ═══════════════════════════════════════════════════════
     SECTION 7 — TRASH REVIEW
══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">🗑 Trash Review</div>

  <div class="warn-box">⚠️ <strong>Total items in Trash (including auto-trashed):</strong> 41 items reviewed below. Auto-trashed phishing emails are noted separately and require no restore.</div>

  <!-- RESTORE -->
  <div class="card card-green" style="margin-bottom:14px;">
    <div class="card-title">✅ Restore Immediately (3 Items — Already Rescued)</div>
    <div class="card-body">
      <table>
        <thead><tr><th>Sender</th><th>Subject</th><th>Reason to Restore</th></tr></thead>
        <tbody>
          <tr><td>Google (noreply-accounts@google.com)</td><td>You shared Google Account data with makebestmusic</td><td>Google security notification — important account activity. Already rescued.</td></tr>
          <tr><td>Suno (suno@creators.suno.com)</td><td>Welcome to Suno!</td><td>Account confirmation email from legitimate creative platform. Already rescued.</td></tr>
          <tr><td>Google (noreply-accounts@google.com)</td><td>You shared Google Account data with Suno</td><td>Google security notification — important account activity. Already rescued.</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- REVIEW BEFORE DELETING -->
  <div class="card card-yellow" style="margin-bottom:14px;">
    <div class="card-title">🔍 Review Before Deleting (5 Items)</div>
    <div class="card-body">
      <table>
        <thead><tr><th>Sender</th><th>Subject</th><th>Reason to Review</th></tr></thead>
        <tbody>
          <tr><td>Job Search Unlocked (Substack)</td><td>Cultural Fit Predicts Nothing a CEO Cares About</td><td>Useful hiring insight — relevant for CUNY or future interviews. Read before deleting.</td></tr>
          <tr><td>Glassdoor Jobs</td><td>Cove HR Manager + 6 more jobs</td><td>Job digest — scan for senior HR matches before deleting.</td></tr>
          <tr><td>Vaishali Lambe / Medium</td><td>Designing Trust: Ethical Review and Leadership in AI Innovation</td><td>HR + AI leadership — relevant to executive HR trajectory. Skim before deleting.</td></tr>
          <tr><td>LinkedIn Daily Rundown</td><td>Tim Cook's new role; Deadly Amazon plane crash</td><td>Tim Cook news may be relevant for executive business awareness. Quick read.</td></tr>
          <tr><td>HomeAgain PetRescuers</td><td>Ash, a lost Cat, missing in Bronx area</td><td>Community alert — Bronx area. No action required but worth noting if you live nearby.</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- AUTO-TRASHED — PHISHING -->
  <div class="card card-red" style="margin-bottom:14px;">
    <div class="card-title">🚨 Auto-Trashed — Phishing / Scams (5 Items — No Restore Needed)</div>
    <div class="card-body">
      <table>
        <thead><tr><th>Sender</th><th>Subject</th><th>Reason</th></tr></thead>
        <tbody>
          <tr><td>info@ykqwtclekicjc</td><td>Your Cloud ID has been locked…</td><td>Fake cloud lockout / credential harvesting — spoofed domain targeting Gmail username</td></tr>
          <tr><td>info@promisegcc.com (MA)</td><td>G - J1 / Important Message for melissaw212</td><td>419 advance-fee fraud impersonating foreign official</td></tr>
          <tr><td>melissaw212@gmail.com (Melissa W)</td><td>Become a Member</td><td>Spoofed/compromised self-send with unfilled tracking URL template — account probe</td></tr>
          <tr><td>apciesrpjoprqw... (Sex Trick)</td><td>Watch this Alone</td><td>Adult spam / malicious link lure</td></tr>
          <tr><td>cdsupporttknv@jrsgzodnmhediqxpqmydoajh.com</td><td>WATCH THIS FILTHY +18 VIDEO NOW 🔞</td><td>Explicit adult spam with spoofed Gmail username</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- SAFE TO DELETE -->
  <div class="card card-gray">
    <div class="card-title">🗑 Safe to Delete (33 Items)</div>
    <div class="card-body">
      <table>
        <thead><tr><th>Category</th><th>Count</th><th>Senders</th></tr></thead>
        <tbody>
          <tr><td>Retail Promotions</td><td>10</td><td>Kohl's, Gap Factory (×3), Amazon (×3), SHEIN, Quince, YesStyle</td></tr>
          <tr><td>Casino / Spam (in Trash)</td><td>2</td><td>💰MIAMI-CLUB, "Congratulations 🎉" casino spins</td></tr>
          <tr><td>Newsletter / Finance</td><td>3</td><td>Dylan's Diary, The Signal (TradeAlgo), TriNet</td></tr>
          <tr><td>Newsletter / Lifestyle</td><td>2</td><td>The Daily Skimm, popcornpotential.com.au</td></tr>
          <tr><td>Newsletter / Business</td><td>2</td><td>Justyn The AI Guy, NiceToMeet</td></tr>
          <tr><td>Pharma Spam (in Trash)</td><td>1</td><td>💰MIAMI-CLUB GLP-1 variant (already in trash)</td></tr>
          <tr><td>Fake pharma (not trashed)</td><td>2</td><td>DirectMeds ×2 (spoofed domains)</td></tr>
          <tr><td>Promo AI/Music</td><td>2</td><td>Higgsfield AI ("We got a better offer"), makebestmusic promo</td></tr>
          <tr><td>Amazon Cart Reminder</td><td>1</td><td>Amazon —
