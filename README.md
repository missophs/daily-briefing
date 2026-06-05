<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa Weiss | June 5, 2026</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: white; border-radius: 16px; padding: 36px 40px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px; }
  .header-left h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header-left p { font-size: 14px; color: #a8b4c8; margin-top: 4px; }
  .header-stats { display: flex; gap: 20px; flex-wrap: wrap; }
  .stat-pill { background: rgba(255,255,255,0.12); border: 1px solid rgba(255,255,255,0.18); border-radius: 50px; padding: 10px 20px; text-align: center; }
  .stat-pill .num { font-size: 22px; font-weight: 700; color: #e0f0ff; display: block; }
  .stat-pill .lbl { font-size: 11px; color: #a8b4c8; text-transform: uppercase; letter-spacing: 0.5px; }

  /* SECTION HEADERS */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; color: #1a1a2e; border-left: 5px solid #0f3460; padding-left: 12px; margin-bottom: 14px; text-transform: uppercase; letter-spacing: 0.4px; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 10px; border-left: 5px solid; }
  .card-red    { background: #fff5f5; border-color: #e53e3e; }
  .card-yellow { background: #fffdf0; border-color: #d69e2e; }
  .card-blue   { background: #f0f7ff; border-color: #3182ce; }
  .card-green  { background: #f0fff4; border-color: #38a169; }
  .card-purple { background: #faf5ff; border-color: #805ad5; }
  .card-gray   { background: #f7f7f7; border-color: #a0aec0; }

  .card .card-title { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
  .card .card-meta  { font-size: 12px; color: #666; margin-bottom: 6px; }
  .card .card-body  { font-size: 13px; color: #333; }
  .card .card-action { margin-top: 8px; font-size: 12px; font-weight: 600; padding: 4px 10px; border-radius: 4px; display: inline-block; }
  .action-red    { background: #fed7d7; color: #c53030; }
  .action-yellow { background: #fefcbf; color: #975a16; }
  .action-blue   { background: #bee3f8; color: #2b6cb0; }
  .action-green  { background: #c6f6d5; color: #276749; }
  .action-purple { background: #e9d8fd; color: #553c9a; }
  .action-gray   { background: #e2e8f0; color: #4a5568; }

  /* BADGES */
  .badge { display: inline-block; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 50px; margin-right: 4px; }
  .badge-red    { background: #fed7d7; color: #c53030; }
  .badge-yellow { background: #fefcbf; color: #975a16; }
  .badge-green  { background: #c6f6d5; color: #276749; }
  .badge-blue   { background: #bee3f8; color: #2b6cb0; }
  .badge-purple { background: #e9d8fd; color: #553c9a; }
  .badge-gray   { background: #e2e8f0; color: #4a5568; }
  .badge-orange { background: #feebc8; color: #c05621; }

  /* SUMMARY BULLETS */
  .exec-summary { background: #fff; border-radius: 12px; padding: 20px 28px; border: 1px solid #e2e8f0; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .exec-summary ul { list-style: none; }
  .exec-summary li { padding: 10px 0; border-bottom: 1px solid #f0f0f0; font-size: 14px; display: flex; gap: 10px; align-items: flex-start; }
  .exec-summary li:last-child { border-bottom: none; }
  .bullet-icon { font-size: 18px; flex-shrink: 0; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 6px rgba(0,0,0,0.06); margin-bottom: 10px; }
  th { background: #1a1a2e; color: white; padding: 10px 14px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.4px; }
  td { padding: 9px 14px; border-bottom: 1px solid #f0f0f0; font-size: 13px; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #fafafa; }
  tr:hover td { background: #f0f7ff; }

  /* CALENDAR */
  .cal-day { background: #fff; border-radius: 10px; margin-bottom: 12px; overflow: hidden; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
  .cal-day-header { background: #0f3460; color: white; padding: 10px 18px; font-weight: 700; font-size: 13px; display: flex; justify-content: space-between; align-items: center; }
  .cal-day-header .day-label { font-size: 15px; }
  .cal-event { padding: 12px 18px; border-bottom: 1px solid #f0f0f0; display: grid; grid-template-columns: 110px 1fr; gap: 12px; }
  .cal-event:last-child { border-bottom: none; }
  .cal-time { font-size: 12px; color: #666; font-weight: 600; padding-top: 2px; }
  .cal-details .cal-name { font-weight: 700; font-size: 14px; margin-bottom: 3px; }
  .cal-details .cal-sub { font-size: 12px; color: #555; }
  .cal-details a { color: #3182ce; font-size: 12px; word-break: break-all; }
  .conflict-warn { background: #fff5f5; border: 1px solid #feb2b2; border-radius: 4px; padding: 3px 8px; font-size: 11px; color: #c53030; margin-top: 4px; display: inline-block; font-weight: 600; }

  /* PRIORITY TABLE */
  .priority-high   { color: #c53030; font-weight: 700; }
  .priority-medium { color: #975a16; font-weight: 700; }
  .priority-low    { color: #4a5568; font-weight: 600; }

  /* DASHBOARD GRID */
  .dashboard { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 14px; margin-bottom: 10px; }
  .dash-card { background: #fff; border-radius: 10px; padding: 16px; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.07); border-top: 4px solid; }
  .dash-card .dash-num { font-size: 32px; font-weight: 800; }
  .dash-card .dash-label { font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 0.4px; margin-top: 4px; }
  .dash-red   { border-top-color: #e53e3e; } .dash-red .dash-num   { color: #e53e3e; }
  .dash-yellow{ border-top-color: #d69e2e; } .dash-yellow .dash-num{ color: #d69e2e; }
  .dash-blue  { border-top-color: #3182ce; } .dash-blue .dash-num  { color: #3182ce; }
  .dash-green { border-top-color: #38a169; } .dash-green .dash-num { color: #38a169; }
  .dash-purple{ border-top-color: #805ad5; } .dash-purple .dash-num{ color: #805ad5; }
  .dash-gray  { border-top-color: #a0aec0; } .dash-gray .dash-num  { color: #a0aec0; }

  /* TOP 3 */
  .top3 { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 14px; }
  .top3-card { background: #fff; border-radius: 12px; padding: 22px; box-shadow: 0 4px 12px rgba(0,0,0,0.09); border-top: 5px solid; }
  .top3-num { font-size: 40px; font-weight: 900; opacity: 0.12; position: absolute; top: 12px; right: 16px; }
  .top3-card { position: relative; overflow: hidden; }
  .top3-card:nth-child(1) { border-color: #e53e3e; } .top3-card:nth-child(1) .top3-num { color: #e53e3e; }
  .top3-card:nth-child(2) { border-color: #38a169; } .top3-card:nth-child(2) .top3-num { color: #38a169; }
  .top3-card:nth-child(3) { border-color: #3182ce; } .top3-card:nth-child(3) .top3-num { color: #3182ce; }
  .top3-card h3 { font-size: 15px; font-weight: 700; margin-bottom: 8px; }
  .top3-card p { font-size: 13px; color: #444; }

  /* DIVIDER */
  .divider { border: none; border-top: 2px solid #e2e8f0; margin: 28px 0; }

  /* EMAIL GROUPS */
  .email-group { background: #fff; border-radius: 10px; margin-bottom: 10px; overflow: hidden; box-shadow: 0 2px 6px rgba(0,0,0,0.05); }
  .email-group-header { padding: 12px 18px; font-weight: 700; font-size: 14px; display: flex; justify-content: space-between; align-items: center; }
  .email-group-body { padding: 12px 18px; border-top: 1px solid #f0f0f0; font-size: 13px; color: #333; }
  .email-row { padding: 7px 0; border-bottom: 1px solid #f7f7f7; display: flex; gap: 8px; align-items: flex-start; flex-wrap: wrap; }
  .email-row:last-child { border-bottom: none; }
  .email-sender { font-weight: 600; color: #1a1a2e; min-width: 160px; }
  .email-subject { color: #444; flex: 1; }
  .unread-dot { width: 8px; height: 8px; background: #3182ce; border-radius: 50%; flex-shrink: 0; margin-top: 5px; }

  .egr  { background: #fff5f5; } .egr .email-group-header  { background: #fed7d7; color: #742a2a; }
  .egy  { background: #fffdf0; } .egy .email-group-header  { background: #fefcbf; color: #744210; }
  .egb  { background: #f0f7ff; } .egb .email-group-header  { background: #bee3f8; color: #1a365d; }
  .egg  { background: #f0fff4; } .egg .email-group-header  { background: #c6f6d5; color: #1c4532; }
  .egp  { background: #faf5ff; } .egp .email-group-header  { background: #e9d8fd; color: #322659; }
  .eggy { background: #f7f7f7; } .eggy .email-group-header { background: #e2e8f0; color: #2d3748; }

  /* TRASH */
  .trash-group { border-radius: 10px; padding: 16px 20px; margin-bottom: 10px; }
  .trash-restore { background: #f0fff4; border: 2px solid #38a169; }
  .trash-review  { background: #fffdf0; border: 2px solid #d69e2e; }
  .trash-delete  { background: #f7f7f7; border: 2px solid #a0aec0; }
  .trash-group h4 { font-size: 14px; font-weight: 700; margin-bottom: 8px; }

  /* ACCOUNTING */
  .acct-total { background: #1a1a2e; color: white; }
  .acct-total td { color: white; font-weight: 700; }

  @media (max-width: 600px) {
    .header { padding: 22px 18px; }
    .header-left h1 { font-size: 20px; }
    .cal-event { grid-template-columns: 1fr; }
    .top3 { grid-template-columns: 1fr; }
    .dashboard { grid-template-columns: repeat(2, 1fr); }
  }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════
     1. HEADER
═══════════════════════════════════════════════ -->
<div class="header">
  <div class="header-left">
    <h1>👋 Good Morning, Melissa!</h1>
    <p>Executive Briefing &nbsp;·&nbsp; <strong>Friday, June 5, 2026</strong> &nbsp;·&nbsp; Prepared by your Executive Chief of Staff</p>
  </div>
  <div class="header-stats">
    <div class="stat-pill"><span class="num">50</span><span class="lbl">Emails Reviewed</span></div>
    <div class="stat-pill"><span class="num">9</span><span class="lbl">Calendar Events</span></div>
    <div class="stat-pill"><span class="num">🔴 5</span><span class="lbl">Urgent Items</span></div>
    <div class="stat-pill"><span class="num">📅 7</span><span class="lbl">Days Ahead</span></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     2. EXECUTIVE SUMMARY
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📋 Executive Summary</div>
  <div class="exec-summary">
    <ul>
      <li>
        <span class="bullet-icon">🔴</span>
        <div><strong>URGENT — Anthropic API Disabled + 5 Failed Payments:</strong> Your Claude API access has been shut off due to exhausted usage credits on your "Melissa's Individual Org." Multiple failed payment attempts ($21.78 and $16.40) flooded your inbox today. A bank account was connected via Link (Stripe) to resolve this — confirm the payment went through and restore API access immediately, as this directly impacts your daily briefing automation pipeline.</div>
      </li>
      <li>
        <span class="bullet-icon">🟢</span>
        <div><strong>JOB SEARCH — VP HR Role Alert ($220K–$240K) + Netta Jenkins Consult Scheduled:</strong> LinkedIn surfaced a Vice President of Human Resources (Private Equity) role at Hoxton Circle paying up to $240K/year. Your 15-minute consult with Netta Jenkins (HIC Consult) is confirmed for Tuesday, June 9 at 12:00 PM. HR Search AM report shows 14 active leads (3 priority / 48h, 11 strategic / 90h). Strong week for pipeline activity.</div>
      </li>
      <li>
        <span class="bullet-icon">🟡</span>
        <div><strong>DEADLINES — Jackie's Birthday Tomorrow, Eye Appt Monday, CHRO Office Subscription Expires Tomorrow, Render DB Suspended Soon, Netlify Credits at 75%:</strong> Several time-sensitive items converge this weekend: Jackie's birthday is June 6, your eye appointment is June 8, The CHRO Office paid subscription expires June 6, your Render PostgreSQL database (performance-chat-db) faces imminent suspension, and Netlify credits hit 75% of 1,000 — all requiring decisions before Monday.</div>
      </li>
    </ul>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     3. ACTION REQUIRED
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">⚡ Action Required</div>

  <div class="card card-red">
    <div class="card-title">🔴 CRITICAL — Claude API Access Disabled</div>
    <div class="card-meta">From: Anthropic &lt;no-reply-tg3@mail.anthropic.com&gt; | Received: Fri Jun 5, ~1:18 PM | In Inbox</div>
    <div class="card-body">Your Claude API is turned off because your organization "Melissa's Individual Org" is out of usage credits. This breaks your daily briefing automation and any other Claude-powered workflows.</div>
    <span class="card-action action-red">➡ Go to console.anthropic.com → Add credits or upgrade plan. Verify payment method is working. Do this TODAY.</span>
  </div>

  <div class="card card-red">
    <div class="card-title">🔴 URGENT — 5+ Failed Anthropic Payments ($21.78 &amp; $16.40)</div>
    <div class="card-meta">From: Anthropic failed-payments@mail.anthropic.com | Multiple emails today | In Inbox + unlabeled</div>
    <div class="card-body">At least five failed payment notifications for $21.78 (×4) and $16.40 (×1) hit your inbox in rapid succession between ~2:12 PM and ~3:05 PM, alongside a Link/Stripe bank account connection. This cascade suggests a card failure followed by attempted bank account resolution. Confirm the bank connection succeeded and the latest charge cleared.</div>
    <span class="card-action action-red">➡ Log into Anthropic billing. Confirm payment method. Check bank/card statements. Resolve immediately.</span>
  </div>

  <div class="card card-yellow">
    <div class="card-title">🟡 DEADLINE TOMORROW — The CHRO Office Subscription Expires June 6</div>
    <div class="card-meta">From: The CHRO Office &lt;thehroffice@substack.com&gt; | Fri Jun 5, ~2:04 PM | In Inbox</div>
    <div class="card-body">Your paid subscription to The CHRO Office newsletter expires tomorrow. As an active HR professional in job search mode, this is likely worth renewing for industry intelligence and credibility content.</div>
    <span class="card-action action-yellow">➡ Decide: Renew or let lapse. Due: Saturday, June 6.</span>
  </div>

  <div class="card card-yellow">
    <div class="card-title">🟡 URGENT — Render Free Database Expiring Soon (performance-chat-db)</div>
    <div class="card-meta">From: Render &lt;no-reply@render.com&gt; | Fri Jun 5, 3:25 PM | In Inbox | UNREAD</div>
    <div class="card-body">Your free PostgreSQL database "performance-chat-db" on Render is set to be suspended. If this supports any live application or briefing pipeline, data could be lost.</div>
    <span class="card-action action-yellow">➡ Upgrade to paid tier, migrate data, or back up immediately. Act before suspension date.</span>
  </div>

  <div class="card card-yellow">
    <div class="card-title">🟡 WARNING — Netlify Credits at 75% (Morning Briefing Project)</div>
    <div class="card-meta">From: Netlify &lt;team@netlify.com&gt; | Fri Jun 5, 3:34 PM | In Inbox | UNREAD</div>
    <div class="card-body">Your "morning briefing" Netlify project has consumed 750 of your 1,000 credit allowance this billing cycle. At current usage rate, you may hit the cap before the billing cycle ends.</div>
    <span class="card-action action-yellow">➡ Review usage in Netlify dashboard. Consider upgrading plan or optimizing build frequency.</span>
  </div>

  <div class="card card-yellow">
    <div class="card-title">🟡 GitHub Actions — Daily Briefing Workflow Failing (3× Today)</div>
    <div class="card-meta">From: missophs &lt;notifications@github.com&gt; | Multiple times today | In Inbox + unlabeled</div>
    <div class="card-body">Your GitHub Actions "Daily Briefing - webhooks" workflow (commit 41906d6) has failed at least 3 times today. This is likely related to the Anthropic API being disabled and/or Netlify/Render issues.</div>
    <span class="card-action action-yellow">➡ After restoring Anthropic credits, re-run workflow. Check logs for secondary errors. Due: Today.</span>
  </div>

  <div class="card card-blue">
    <div class="card-title">🔵 RSVP NEEDED — HR Networking &amp; Job Search Group Zoom (June 10)</div>
    <div class="card-meta">Calendar | Wed Jun 10, 12:00–1:30 PM | Status: needsAction</div>
    <div class="card-body">You have not yet responded to the HR Networking &amp; Job Search Group Zoom on June 10. Separately, a "Network" calendar block is already confirmed at the same time — you appear to have a duplicate/overlap.</div>
    <span class="card-action action-blue">➡ Confirm or decline the group Zoom invite. Resolve the calendar overlap with "Network" block.</span>
  </div>

  <div class="card card-blue">
    <div class="card-title">🔵 RSVP NEEDED — HR Networking Open Office Hours (June 11)</div>
    <div class="card-meta">Calendar | Thu Jun 11, 12:00–1:00 PM | Status: needsAction</div>
    <div class="card-body">You have not responded to the HR Networking &amp; Job Search Open Office Hours Zoom for June 11.</div>
    <span class="card-action action-blue">➡ Accept or decline. Due: ASAP.</span>
  </div>

  <div class="card card-green">
    <div class="card-title">🟢 OPPORTUNITY — VP HR (Private Equity) at Hoxton Circle — $220K–$240K</div>
    <div class="card-meta">From: LinkedIn Job Alerts | Fri Jun 5, 3:06 PM | In Trash (review!)</div>
    <div class="card-body">LinkedIn surfaced a VP Human Resources role in Private Equity at Hoxton Circle paying $220K–$240K/year. This email was auto-sent to Trash — do not ignore it.</div>
    <span class="card-action action-green">➡ Restore from Trash. Review full role. Apply if fit. High priority.</span>
  </div>

  <div class="card card-blue">
    <div class="card-title">🔵 UPCOMING — Eye Appointment Monday June 8, 9:00 AM</div>
    <div class="card-meta">Calendar | Mon Jun 8, 9:00–10:00 AM</div>
    <div class="card-body">Eye appointment confirmed for Monday morning. Note: Warby Parker flagged your prescription expires in two weeks, and 1-800 Contacts noted you're overdue for a reorder.</div>
    <span class="card-action action-blue">➡ Prepare insurance info. Bring current frames/contacts Rx. Consider placing contact reorder after appointment.</span>
  </div>

  <div class="card card-yellow">
    <div class="card-title">🟡 PERSONAL — Jackie's Birthday Tomorrow (June 6)</div>
    <div class="card-meta">Calendar | All Day | Sat Jun 6</div>
    <div class="card-body">Jackie's birthday is tomorrow. No gift or plans noted.</div>
    <span class="card-action action-yellow">➡ Send message / arrange gift if not already done. Due: Today.</span>
  </div>

  <div class="card card-yellow">
    <div class="card-title">🟡 BILLING — State Farm Bill Due June 7</div>
    <div class="card-meta">Calendar | All Day | Sun Jun 7</div>
    <div class="card-body">State Farm insurance bill is due this Sunday.</div>
    <span class="card-action action-yellow">➡ Confirm payment scheduled or pay manually. Due: Sunday, June 7.</span>
  </div>

  <div class="card card-blue">
    <div class="card-title">🔵 PREP NEEDED — Consult with Netta Jenkins (June 9, 12:00 PM)</div>
    <div class="card-meta">Calendar | Tue Jun 9, 12:00–12:15 PM | Zoom | Accepted</div>
    <div class="card-body">15-minute consultation with Netta Jenkins (HIC Consult) via Zoom. Short meeting — have your top 2–3 talking points ready and know what outcome you want from this call.</div>
    <span class="card-action action-blue">➡ Prepare agenda/talking points by Monday. Zoom PW: 424726.</span>
  </div>

  <div class="card card-blue">
    <div class="card-title">🔵 PREP — Melissa x Meg Drinks (June 10, 1:00 PM)</div>
    <div class="card-meta">Calendar | Wed Jun 10, 1:00–2:00 PM | Location: TBC | Accepted</div>
    <div class="card-body">Drinks with Meg (Oakleaf Partnership). Location not yet confirmed.</div>
    <span class="card-action action-blue">➡ Confirm location with Meg by Monday. Note: this overlaps with the HR Networking session — review schedule.</span>
  </div>

  <div class="card card-purple">
    <div class="card-title">🟣 FYI — Stella's Vet: Third-Party Prescription Policy Update</div>
    <div class="card-meta">From: Center for Veterinary Care | Fri Jun 5, 2:44 PM | In Inbox | UNREAD</div>
    <div class="card-body">Center for Veterinary Care (Stella's vet) has updated their policy on third-party prescription requests. This may affect where/how you get Stella's medications.</div>
    <span class="card-action action-purple">➡ Read the full email. Understand new prescription process before next refill.</span>
  </div>

</div>

<!-- ═══════════════════════════════════════════════
     4. FULL 7-DAY CALENDAR
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📅 Full 7-Day Calendar (Jun 5 – Jun 11, 2026)</div>

  <!-- Friday June 5 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span class="day-label">📅 Friday, June 5, 2026</span>
      <span><span class="badge badge-blue">TODAY</span> <span class="badge badge-gray">0 events</span></span>
    </div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="cal-name">No calendar events today</div>
        <div class="cal-sub">Use today to resolve urgent Anthropic/billing issues, prep for weekend, and plan next week.</div>
      </div>
    </div>
  </div>

  <!-- Saturday June 6 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span class="day-label">📅 Saturday, June 6, 2026</span>
      <span><span class="badge badge-yellow">1 EVENT</span></span>
    </div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="cal-name">🎂 Jackie's Birthday</div>
        <div class="cal-sub"><span class="badge badge-green">CONFIRMED</span> Personal reminder — all-day event.</div>
        <div class="cal-sub" style="margin-top:4px;"><strong>Prep:</strong> Send birthday message, give gift, or make plans. <strong>⚠ Act today if not done.</strong></div>
        <div class="cal-sub" style="margin-top:4px;"><strong>Note:</strong> The CHRO Office subscription also expires today — renew/cancel decision needed.</div>
      </div>
    </div>
  </div>

  <!-- Sunday June 7 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span class="day-label">📅 Sunday, June 7, 2026</span>
      <span><span class="badge badge-yellow">1 EVENT</span></span>
    </div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="cal-name">🏦 State Farm Bill Due</div>
        <div class="cal-sub"><span class="badge badge-green">CONFIRMED</span> Insurance payment due.</div>
        <div class="cal-sub" style="margin-top:4px;"><strong>Prep:</strong> Verify autopay is set or manually submit payment before end of day.</div>
      </div>
    </div>
  </div>

  <!-- Monday June 8 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span class="day-label">📅 Monday, June 8, 2026</span>
      <span><span class="badge badge-blue">1 EVENT</span></span>
    </div>
    <div class="cal-event">
      <div class="cal-time">9:00 – 10:00 AM<br><span style="color:#888;font-size:11px;">Eastern</span></div>
      <div class="cal-details">
        <div class="cal-name">👁️ Eye Appointment</div>
        <div class="cal-sub"><span class="badge badge-green">CONFIRMED</span> Medical appointment — location not specified.</div>
        <div class="cal-sub" style="margin-top:4px;"><strong>Prep:</strong> Insurance card, current glasses/contacts, list of concerns. Note: Warby Parker says prescription expires in 2 weeks; 1-800 Contacts says you're overdue for reorder. Coordinate with results of this visit.</div>
      </div>
    </div>
  </div>

  <!-- Tuesday June 9 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span class="day-label">📅 Tuesday, June 9, 2026</span>
      <span><span class="badge badge-green">1 EVENT</span></span>
    </div>
    <div class="cal-event">
      <div class="cal-time">12:00 – 12:15 PM<br><span style="color:#888;font-size:11px;">Eastern</span></div>
      <div class="cal-details">
        <div class="cal-name">💼 Melissa Weiss x Netta Jenkins — 15-Min Consultation</div>
        <div class="cal-sub"><span class="badge badge-green">ACCEPTED</span> Attendee: <strong>netta@hicconsult.com</strong></div>
        <div class="cal-sub" style="margin-top:4px;"><strong>Location:</strong> <a href="https://us06web.zoom.us/j/5224221004?pwd=UU5YNmlFckpjQnlzc2FDMHFlNUhhUT09" target="_blank">Zoom Link</a> | Password: 424726</div>
        <div class="cal-sub" style="margin-top:4px;"><strong>Prep:</strong> Prepare 2–3 specific questions or objectives for Netta. Know your target role, level, and compensation. This is a brief but high-value networking/consulting call — be concise and clear on your ask.</div>
      </div>
    </div>
  </div>

  <!-- Wednesday June 10 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span class="day-label">📅 Wednesday, June 10, 2026</span>
      <span><span class="badge badge-yellow">3 EVENTS</span> <span class="badge badge-red">⚠ CONFLICT</span></span>
    </div>
    <div class="cal-event">
      <div class="cal-time">12:00 – 1:30 PM<br><span style="color:#888;font-size:11px;">Eastern</span></div>
      <div class="cal-details">
        <div class="cal-name">👥 HR Networking &amp; Job Search Group — Zoom 2</div>
        <div class="cal-sub"><span class="badge badge-red">NEEDS ACTION (No RSVP)</span> Large group session — 170+ attendees.</div>
        <div class="cal-sub" style="margin-top:4px;"><strong>Location:</strong> <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a></div>
        <div class="cal-sub" style="margin-top:4px;"><strong>Prep:</strong> Review team guidelines (linked in event). Prepare intro and any agenda items.</div>
        <div class="conflict-warn">⚠ CONFLICT: Overlaps with "Network" block (12–1:30 PM) — appears to be same event. Resolve duplicate.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-time">12:00 – 1:30 PM<br><span style="color:#888;font-size:11px;">Eastern</span></div>
      <div class="cal-details">
        <div class="cal-name">🌐 Network (Personal Block)</div>
        <div class="cal-sub"><span class="badge badge-green">CONFIRMED</span> No attendees listed — likely a personal reminder block.</div>
        <div class="cal-sub" style="margin-top:4px;"><strong>Note:</strong> Overlaps with HR Networking Group Zoom above. May be same event or a separate networking activity. Clarify and remove duplicate if needed.</div>
        <div class="conflict-warn">⚠ CONFLICT: Same time as HR Networking Zoom above.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-time">1:00 – 2:00 PM<br><span style="color:#888;font-size:11px;">Eastern</span></div>
      <div class="cal-details">
        <div class="cal-name">🥂 Melissa x Meg — Drinks (Oakleaf Partnership)</div>
        <div class="cal-sub"><span class="badge badge-green">ACCEPTED</span> Attendee: <strong>megpark@oakleafpartnership.com</strong> (Oakleaf Partnership)</div>
        <div class="cal-sub" style="margin-top:4px;"><strong>Location:</strong> TBC — confirm with Meg.</div>
        <div class="cal-sub" style="margin-top:4px;"><strong>Prep:</strong> Confirm location/address. Oakleaf Partnership is a talent/HR executive search firm — this is a high-value relationship meeting. Prepare your updated positioning, key targets, and ask clearly.</div>
        <div class="conflict-warn">⚠ CONFLICT: Overlaps last 30 min of HR Networking Zoom (12–1:30 PM). Plan departure from Zoom by 12:45 PM to arrive on time.</div>
      </div>
    </div>
  </div>

  <!-- Thursday June 11 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span class="day-label">📅 Thursday, June 11, 2026</span>
      <span><span class="badge badge-yellow">2 EVENTS</span></span>
    </div>
    <div class="cal-event">
      <div class="cal-time">9:00 – 10:30 AM<br><span style="color:#888;font-size:11px;">Eastern</span></div>
      <div class="cal-details">
        <div class="cal-name">🏛️ Executive Roundtable</div>
        <div class="cal-sub"><span class="badge badge-gray">DECLINED</span> Hosted by: John Madigan via Zoom.</div>
        <div class="cal-sub" style="margin-top:4px;"><strong>Location:</strong> <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> | PW: 205454</div>
        <div class="cal-sub" style="margin-top:4px;"><strong>Note:</strong> You have declined this event. Consider whether this was intentional — Executive Roundtables can be high-value for networking during job search. You may want to reconsider attendance.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-time">12:00 – 1:00 PM<br><span style="color:#888;font-size:11px;">Eastern</span></div>
      <div class="cal-details">
        <div class="cal-name">👥 HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
        <div class="cal-sub"><span class="badge badge-red">NEEDS ACTION (No RSVP)</span> Large group — 170+ attendees. Note: AI notetaking tools should be turned off per organizer.</div>
        <div class="cal-sub" style="margin-top:4px;"><strong>Location:</strong> <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a></div>
        <div class="cal-sub" style="margin-top:4px;"><strong>Prep:</strong> Prepare talking points or questions for open discussion. Bring updates on your job search status.</div>
      </div>
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════
     5. JOB SEARCH & INTERVIEW PIPELINE
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">🟢 Job Search &amp; Interview Pipeline</div>

  <table>
    <thead>
      <tr>
        <th>Type</th>
        <th>Opportunity / Event</th>
        <th>Source / Date</th>
        <th>Fit</th>
        <th>Status / Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="badge badge-green">JOB ALERT</span></td>
        <td><strong>VP Human Resources (Private Equity)</strong><br>Hoxton Circle — $220K–$240K/year</td>
        <td>LinkedIn Job Alerts<br>Jun 5, 2026</td>
        <td><span class="priority-high">HIGH FIT</span></td>
        <td>⚠ In Trash — restore immediately. Review JD, assess PE experience match, apply if qualified.</td>
      </tr>
      <tr>
        <td><span class="badge badge-blue">CONSULT</span></td>
        <td><strong>15-Min Call: Melissa x Netta Jenkins</strong><br>HIC Consult (netta@hicconsult.com)</td>
        <td>Google Calendar<br>Tue Jun 9, 12:00 PM</td>
        <td><span class="priority-high">HIGH</span></td>
        <td>✅ Accepted. Prep agenda. Zoom PW: 424726. High-value: HR consulting firm connection.</td>
      </tr>
      <tr>
        <td><span class="badge badge-green">NETWORKING</span></td>
        <td><strong>Melissa x Meg Drinks</strong><br>Meg Park, Oakleaf Partnership (HR executive search)</td>
        <td>Google Calendar<br>Wed Jun 10, 1:00 PM</td>
        <td><span class="priority-high">HIGH</span></td>
        <td>✅ Accepted. Confirm location TBC. Oakleaf is an HR executive search firm — prime referral opportunity.</td>
      </tr>
      <tr>
        <td><span class="badge badge-purple">GROUP</span></td>
        <td><strong>HR Networking &amp; Job Search Group — Zoom 2</strong><br>170+ HR professionals</td>
        <td>Google Calendar<br>Wed Jun 10, 12:00 PM</td>
        <td><span class="priority-medium">MEDIUM</span></td>
        <td>⚠ RSVP needed. Overlaps with Meg drinks — plan accordingly. Good group visibility.</td>
      </tr>
      <tr>
        <td><span class="badge badge-purple">GROUP</span></td>
        <td><strong>HR Networking Open Office Hours — Zoom 2</strong><br>170+ HR professionals</td>
        <td>Google Calendar<br>Thu Jun 11, 12:00 PM</td>
        <td><span class="priority-medium">MEDIUM</span></td>
        <td>⚠ RSVP needed. Open discussion format. No AI notetaking. Attend if schedule allows.</td>
      </tr>
      <tr>
        <td><span class="badge badge-blue">ROUNDTABLE</span></td>
        <td><strong>Executive Roundtable</strong><br>John Madigan (Zoom)</td>
        <td>Google Calendar<br>Thu Jun 11, 9:00 AM</td>
        <td><span class="priority-medium">MEDIUM</span></td>
        <td>❌ You declined. Reconsider — executive roundtables often yield senior connections. Review if topic is relevant.</td>
      </tr>
      <tr>
        <td><span class="badge badge-green">AM REPORT</span></td>
        <td><strong>HR Search AM Report</strong><br>14 total leads: 3 Priority (48h) · 11 Strategic (90h)</td>
        <td>melissaw212@gmail.com<br>Jun 5, 8:48 AM</td>
        <td><span class="priority-high">HIGH</span></td>
        <td>✅ Reviewed. Follow up on 3 priority leads within 48 hours. Strategic leads within 90 hours. Exa: 0 results; Apify: 14 results.</td>
      </tr>
      <tr>
        <td><span class="badge badge-blue">COMMUNITY</span></td>
        <td><strong>RNG Tampa Bay — Bank of America Recruiting Contact Requested</strong><br>Antonio Fiorentino seeking BoA Recruiting contact</td>
        <td>RNG Tampa Bay Google Group<br>Jun 5, 6:27 AM</td>
        <td><span class="priority-low">LOW (for Melissa)</span></td>
        <td>Review. If you have a BoA contact, this is a goodwill networking opportunity. Respond if you can help.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════
     6. FULL EMAIL REVIEW BY CATEGORY
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📧 Full Email Review by Category</div>

  <!-- Security / Risk -->
  <div class="email-group egr">
    <div class="email-group-header">
      🔴 Security / Risk
      <span class="badge badge-red">5 emails</span>
    </div>
    <div class="email-group-body">
      <div class="email-row"><span class="unread-dot"></span><span class="email-sender">Anthropic (API Disabled)</span><span class="email-subject">[action needed] Your Claude API access is turned off — <em>In Inbox, read</em></span></div>
      <div class="email-row"><span class="unread-dot"></span><span class="email-sender">Anthropic (failed-payments ×3, Inbox)</span><span class="email-subject">$21.78 payment unsuccessful (×2 unread, in Inbox) · $21.78 unsuccessful again (unread, in Inbox)</span></div>
      <div class="email-row"><span class="email-sender">Link (Stripe)</span><span class="email-subject">You've connected your bank account to Anthropic, PBC — <em>In Inbox, UNREAD</em></span></div>
      <div style="margin-top:8px; font-size:13px;"><strong>Why it matters:</strong> API disabled + 5 failed payment cascades + a new bank account linked = active billing crisis. The Link/Stripe bank connection is a security event — verify you initiated it.<br><strong>Action:</strong> Resolve Anthropic billing immediately. Confirm Link bank connection was authorized. Monitor for unauthorized activity.</div>
    </div>
  </div>

  <!-- Job Search -->
  <div class="email-group egg">
    <div class="email-group-header">
      🟢 Job Search
      <span class="badge badge-green">2 emails</span>
    </div>
    <div class="email-group-body">
      <div class="email-row"><span class="email-sender">melissaw212@gmail.com</span><span class="email-subject">HR Search AM — 2026-06-05 | 3 Priority · 11 Strategic · 14 Total — <em>In Inbox, read</em></span></div>
      <div class="email-row"><span class="unread-dot"></span><span class="email-sender">LinkedIn Job Alerts</span><span class="email-subject">VP Human Resources (PE) at Hoxton Circle: up to $240K/year — <em>In Trash — RESTORE</em></span></div>
      <div style="margin-top:8px; font-size:13px;"><strong>Action:</strong> Review AM search results. Restore LinkedIn VP HR job alert from Trash. Pursue Hoxton Circle opportunity immediately.</div>
    </div>
  </div>

  <!-- Recruiters / Networking -->
  <div class="email-group egg">
    <div class="email-group-header">
      🟢 Recruiters / Networking
      <span class="badge badge-green">1 email</span>
    </div>
    <div class="email-group-body">
      <div class="email-row"><span class="unread-dot"></span><span class="email-sender">Antonio Fiorentino via RNG Tampa Bay</span><span class="email-subject">[RNG Tampa Bay] Bank of America contact — <em>Not in inbox, not in trash, read</em></span></div>
      <div style="margin-top:8px; font-size:13px;"><strong>Action:</strong> Respond if you have a BoA Recruiting contact. Goodwill networking. Low urgency.</div>
    </div>
  </div>

  <!-- Financial / Billing -->
  <div class="email-group egy">
    <div class="email-group-header">
      🟡 Financial / Billing
      <span class="badge badge-yellow">9 emails</span>
    </div>
    <div class="email-group-body">
      <div class="email-row"><span class="unread-dot"></span><span class="email-sender">Anthropic (receipt #2510-6474-3048)</span><span class="email-subject">Your receipt from Anthropic, PBC — UNREAD, In Inbox</span></div>
      <div class="email-row"><span class="email-sender">Anthropic (receipt #2010-4855-2725)</span><span class="email-subject">Your receipt from Anthropic, PBC — Read, In Inbox</span></div>
      <div class="email-row"><span class="email-sender">Anthropic (failed ×4 — outside inbox)</span><span class="email-subject">$21.78 unsuccessful (×3 read) · $16.40 unsuccessful (×1 read) — not in inbox, not in trash</span></div>
      <div class="email-row"><span class="email-sender">Link (Stripe) — Trash</span><span class="email-subject">You've connected your bank account to Anthropic, PBC — In Trash, read</span></div>
      <div style="margin-top:8px; font-size:13px;"><strong>Summary:</strong> Two Anthropic receipts (charges appear to have eventually gone through) plus multiple failed payment notices. Cross-reference receipt amounts with failed charges to understand billing history.<br><strong>Action:</strong> Archive receipts after review. Confirm total charges. Investigate why so many failures occurred.</div>
    </div>
  </div>

  <!-- Technical / Infrastructure -->
  <div class="email-group egr">
    <div class="email-group-header">
      🔴 Technical / Infrastructure
      <span class="badge badge-red">5 emails</span>
    </div>
    <div class="email-group-body">
      <div class="email-row"><span class="unread-dot"></span><span class="email-sender">Netlify</span><span class="email-subject">[Netlify] You've used 75% of credits on morning briefing — In Inbox, UNREAD</span></div>
      <div class="email-row"><span class="unread-dot"></span><span class="email-sender">Render</span><span class="email-subject">Your free Render database expires soon: performance-chat-db — In Inbox, UNREAD</span></div>
      <div class="email-row"><span class="email-sender">missophs/GitHub Actions</span><span class="email-subject">Run failed: Daily Briefing - webhooks (41906d6) — In Inbox, read</span></div>
      <div class="email-row"><span class="email-sender">missophs/GitHub Actions</span><span class="email-subject">Run failed: Daily Briefing - webhooks (×2 more) — not in inbox, read</span></div>
      <div style="margin-top:8px; font-size:13px;"><strong>Action:</strong> Address Render DB before suspension. Monitor Netlify credits. Fix GitHub Actions after restoring Anthropic API. All 3 issues are interconnected.</div>
    </div>
  </div>

  <!-- Medical / Health -->
  <div class="email-group egp">
    <div class="email-group-header">
      🟣 Medical / Health
      <span class="badge badge-purple">1 email</span>
    </div>
    <div class="email-group-body">
      <div class="email-row"><span class="unread-dot"></span><span class="email-sender">Center for Veterinary Care</span><span class="email-subject">Important Update: Third Party Prescription Requests (Stella) — In Inbox, UNREAD</span></div>
      <div style="margin-top:8px; font-size:13px;"><strong>Action:</strong> Read fully. Understand new prescription request policy for Stella. Act before next refill is needed.</div>
    </div>
  </div>

  <!-- Professional Development -->
  <div class="email-group egp">
    <div class="email-group-header">
      🟣 Professional Development
      <span class="badge badge-purple">3 emails</span>
    </div>
    <div class="email-group-body">
      <div class="email-row"><span class="email-sender">The CHRO Office (Substack)</span><span class="email-subject">Your subscription ends tomorrow — In Inbox, read</span></div>
      <div class="email-row"><span class="email-sender">Phil Strazzulla (SSR Newsletter)</span><span class="email-subject">👨‍💻 [Free Webinar] Why HR Software Decisions Fail — not in inbox, read</span></div>
      <div class="email-row"><span class="email-sender">Brya Team</span><span class="email-subject">Still time to share your thoughts 🙏 (survey) — not in inbox, read</span></div>
      <div style="margin-top:8px; font-size:13px;"><strong>Action:</strong> Decide on CHRO Office renewal TODAY (expires tomorrow). Consider the SSR webinar if relevant to current HR tech interests. Complete Brya survey before end of week if interested.</div>
    </div>
  </div>

  <!-- Personal -->
  <div class="email-group egb">
    <div class="email-group-header">
      🔵 Personal
      <span class="badge badge-blue">1 email</span>
    </div>
    <div class="email-group-body">
      <div class="email-row"><span class="unread-dot"></span><span class="email-sender">Melissa Daily Briefing</span><span class="email-subject">Melissa Daily Briefing - 2026-06-05 13:50 UTC — In Inbox, UNREAD (automated self-send)</span></div>
      <div style="margin-top:8px; font-size:13px;"><strong>Action:</strong> This is the automated briefing from your pipeline (which ran successfully at 1:50 PM UTC despite later GitHub failures). Archive after review.</div>
    </div>
  </div>

  <!-- Newsletters / Subscriptions (Inbox) -->
  <div class="email-group egp">
    <div class="email-group-header">
      🟣 Newsletters / Subscriptions
      <span class="badge badge-purple">4 emails</span>
    </div>
    <div class="email-group-body">
      <div class="email-row"><span class="email-sender">HR Brain Pickings</span><span class="email-subject">The Friday 5: AI budgets, papal encyclical, sick leave — In Trash, UNREAD</span></div>
      <div class="email-row"><span class="email-sender">Hebba Youssef (I Hate It Here)</span><span class="email-subject">📓 motivation with $0 — In Trash, UNREAD</span></div>
      <div class="email-row"><span class="email-sender">Mindstream</span><span class="email-subject">Google unveils... Dreambeans — In Trash, UNREAD</span></div>
      <div class="email-row"><span class="email-sender">CoolDeep AI</span><span class="email-subject">Claude did my Instagram content while I slept — not in inbox/trash, read</span></div>
      <div style="margin-top:8px; font-size:13px;"><strong>Action:</strong> HR Brain Pickings and I Hate It Here are relevant HR newsletters — consider restoring from Trash. Mindstream is AI news. CoolDeep AI is low value. Batch-read or unsubscribe from low-signal ones.</div>
    </div>
  </div>

  <!-- Promotional / Retail (non-trash) -->
  <div class="email-group eggy">
    <div class="email-group-header">
      ⚪ Promotional / Retail (Non-Trash)
      <span class="badge badge-gray">5 emails</span>
    </div>
    <div class="email-group-body">
      <div class="email-row"><span class="unread-dot"></span><span class="email-sender">Sago / Focus Group</span><span class="email-subject">Let's Talk Real-Life Money Decisions ($100 research study) — In Inbox, UNREAD</span></div>
      <div class="email-row"><span class="email-sender">Warby Parker</span><span class="email-subject">Your prescription expires in two weeks — not in inbox/trash, UNREAD</span></div>
      <div class="email-row"><span class="email-sender">Slack</span><span class="email-subject">Invite your team to Slack today! (free trial Pro) — not in inbox/trash, UNREAD</span></div>
      <div class="email-row"><span class="email-sender">Venmo</span><span class="email-subject">Earn up to 9% cash back (Venmo Credit Card) — not in inbox/trash, UNREAD</span></div>
      <div class="email-row"><span class="email-sender">Chip City</span><span class="email-subject">15% Off Catering this Summer! — In Inbox, UNREAD</span></div>
      <div style="margin-top:8px; font-size:13px;"><strong>Action:</strong> Warby Parker prescription reminder is timely given eye appointment Monday — keep. Sago focus group: $100 for a study, could be worth it. Others: ignore/archive.</div>
    </div>
  </div>

  <!-- Promotional / Retail (Trash) -->
  <div class="email-group eggy">
    <div class="email-group-header">
      ⚪ Promotional / Retail (Trash)
      <span class="badge badge-gray">14 emails</span>
    </div>
    <div class="email-group-body">
      <div class="email-row"><span class="unread-dot"></span><span class="email-sender">Fayced Aesthetics NYC</span><span class="email-subject">Meet Daisy (new nurse injector + new patient offer) — Trash, UNREAD</span></div>
      <div class="email-row"><span class="unread-dot"></span><span class="email-sender">BellaVitashop (TikTok Shop)</span><span class="email-subject">Melissa, flash sale starts now! ⏰ — Trash, UNREAD</span></div>
      <div class="email-row"><span class="email-sender">Shoe Station</span><span class="email-subject">It's Here: The Sandal Savings Event! — Trash, UNREAD</span></div>
      <div class="email-row"><span class="unread-dot"></span><span class="email-sender">Walgreens</span><span class="email-subject">Double the Vitamins, Zero Extra Cost — Trash, UNREAD</span></div>
      <div class="email-row"><span class="unread-dot"></span><span class="email-sender">1-800 Contacts</span><span class
