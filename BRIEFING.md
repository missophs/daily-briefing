<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing – Melissa Weiss – June 18, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 16px; padding: 36px 40px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .date { font-size: 15px; color: #a8b8d8; margin-top: 4px; }
  .header .meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.1); border-radius: 10px; padding: 10px 20px; text-align: center; }
  .header .meta-item .num { font-size: 26px; font-weight: 700; color: #e2b96f; }
  .header .meta-item .label { font-size: 11px; color: #a8b8d8; text-transform: uppercase; letter-spacing: 1px; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; letter-spacing: 0.4px; padding: 10px 16px; border-radius: 8px 8px 0 0; text-transform: uppercase; display: flex; align-items: center; gap: 8px; }
  .section-body { background: #fff; border-radius: 0 0 10px 10px; padding: 18px; border: 1px solid #e2e8f0; border-top: none; }

  /* COLOR THEMES */
  .theme-red .section-title    { background: #dc2626; color: #fff; }
  .theme-yellow .section-title { background: #d97706; color: #fff; }
  .theme-blue .section-title   { background: #1d4ed8; color: #fff; }
  .theme-green .section-title  { background: #059669; color: #fff; }
  .theme-purple .section-title { background: #7c3aed; color: #fff; }
  .theme-gray .section-title   { background: #6b7280; color: #fff; }
  .theme-dark .section-title   { background: #1a1a2e; color: #fff; }
  .theme-orange .section-title { background: #ea580c; color: #fff; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 18px; margin-bottom: 14px; border-left: 5px solid; }
  .card-red    { background: #fef2f2; border-color: #dc2626; }
  .card-yellow { background: #fffbeb; border-color: #d97706; }
  .card-blue   { background: #eff6ff; border-color: #1d4ed8; }
  .card-green  { background: #f0fdf4; border-color: #059669; }
  .card-purple { background: #f5f3ff; border-color: #7c3aed; }
  .card-gray   { background: #f9fafb; border-color: #9ca3af; }
  .card-orange { background: #fff7ed; border-color: #ea580c; }
  .card h3 { font-size: 14px; font-weight: 700; margin-bottom: 6px; }
  .card .meta-row { display: flex; gap: 16px; flex-wrap: wrap; font-size: 12px; color: #4b5563; margin-bottom: 6px; }
  .card .meta-row span { background: rgba(0,0,0,0.06); border-radius: 4px; padding: 2px 8px; }
  .card p { font-size: 13px; color: #374151; margin-top: 4px; }
  .card .action-line { margin-top: 8px; font-size: 13px; font-weight: 600; color: #1a1a2e; }

  /* EXEC SUMMARY */
  .exec-bullets { list-style: none; }
  .exec-bullets li { display: flex; align-items: flex-start; gap: 12px; padding: 12px 0; border-bottom: 1px solid #e5e7eb; }
  .exec-bullets li:last-child { border-bottom: none; }
  .exec-bullets .bullet-icon { font-size: 20px; flex-shrink: 0; }
  .exec-bullets .bullet-text strong { display: block; font-size: 14px; margin-bottom: 2px; }
  .exec-bullets .bullet-text span { font-size: 13px; color: #4b5563; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #f1f5f9; color: #374151; font-weight: 700; padding: 9px 12px; text-align: left; border-bottom: 2px solid #cbd5e1; }
  td { padding: 9px 12px; border-bottom: 1px solid #e5e7eb; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f8fafc; }

  /* BADGES */
  .badge { display: inline-block; font-size: 11px; font-weight: 700; padding: 2px 9px; border-radius: 20px; text-transform: uppercase; letter-spacing: 0.5px; }
  .badge-red    { background: #fee2e2; color: #dc2626; }
  .badge-yellow { background: #fef3c7; color: #92400e; }
  .badge-green  { background: #d1fae5; color: #065f46; }
  .badge-blue   { background: #dbeafe; color: #1e40af; }
  .badge-purple { background: #ede9fe; color: #5b21b6; }
  .badge-gray   { background: #f3f4f6; color: #374151; }
  .badge-orange { background: #ffedd5; color: #9a3412; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { font-weight: 700; font-size: 14px; background: #e0e7ff; color: #1e40af; padding: 7px 14px; border-radius: 6px; margin-bottom: 8px; }
  .cal-event { display: flex; gap: 14px; align-items: flex-start; padding: 10px 12px; background: #f8fafc; border-radius: 8px; border-left: 4px solid #1d4ed8; margin-bottom: 7px; }
  .cal-event .time { font-weight: 700; color: #1d4ed8; min-width: 105px; font-size: 12px; }
  .cal-event .event-detail .title { font-weight: 700; font-size: 14px; }
  .cal-event .event-detail .sub { font-size: 12px; color: #4b5563; margin-top: 2px; }
  .cal-event.declined { border-color: #9ca3af; background: #f9fafb; opacity: 0.75; }
  .cal-event.needs-rsvp { border-color: #d97706; background: #fffbeb; }

  /* PILLS */
  .pill { display: inline-block; padding: 3px 12px; border-radius: 20px; font-size: 11px; font-weight: 700; margin: 2px 3px; }
  .pill-high   { background: #fee2e2; color: #dc2626; }
  .pill-medium { background: #fef3c7; color: #92400e; }
  .pill-low    { background: #f0fdf4; color: #065f46; }

  /* DASHBOARD GRID */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; }
  .dash-tile { border-radius: 10px; padding: 16px; text-align: center; }
  .dash-tile .num { font-size: 30px; font-weight: 800; }
  .dash-tile .lbl { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; margin-top: 4px; }
  .dt-red    { background: #fee2e2; color: #dc2626; }
  .dt-yellow { background: #fef3c7; color: #92400e; }
  .dt-green  { background: #d1fae5; color: #065f46; }
  .dt-blue   { background: #dbeafe; color: #1e40af; }
  .dt-purple { background: #ede9fe; color: #5b21b6; }
  .dt-gray   { background: #f3f4f6; color: #374151; }

  /* PRIORITIES */
  .priority-list { counter-reset: prio; list-style: none; }
  .priority-list li { counter-increment: prio; display: flex; align-items: flex-start; gap: 14px; padding: 14px; background: #fff; border-radius: 10px; margin-bottom: 12px; border: 1px solid #e2e8f0; }
  .priority-list li::before { content: counter(prio); background: #1a1a2e; color: #e2b96f; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 16px; flex-shrink: 0; }

  /* ACCOUNTING */
  .acct-total { background: #1a1a2e; color: #e2b96f; font-weight: 800; }
  .acct-total td { padding: 11px 12px; }

  /* MISC */
  .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  @media(max-width:680px){ .two-col { grid-template-columns: 1fr; } .header .meta { gap: 12px; } }
  .tag { font-size: 11px; font-weight: 600; background: #e0e7ff; color: #1e40af; border-radius: 4px; padding: 1px 7px; }
  .warn { color: #dc2626; font-weight: 700; font-size: 12px; }
  .note { font-size: 12px; color: #6b7280; font-style: italic; margin-top: 8px; }
  hr.divider { border: none; border-top: 1px solid #e2e8f0; margin: 14px 0; }
  .sub-header { font-size: 13px; font-weight: 700; color: #374151; margin: 14px 0 8px; text-transform: uppercase; letter-spacing: 0.5px; border-bottom: 1px solid #e5e7eb; padding-bottom: 4px; }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ════════════════════════════════════════════════
     1. HEADER
════════════════════════════════════════════════ -->
<div class="header">
  <div class="date">Thursday, June 18, 2026 &nbsp;|&nbsp; Executive Morning Briefing</div>
  <h1>Good Morning, Melissa 👋</h1>
  <div class="meta">
    <div class="meta-item"><div class="num">50</div><div class="label">Emails Reviewed</div></div>
    <div class="meta-item"><div class="num">7</div><div class="label">Calendar Events</div></div>
    <div class="meta-item"><div class="num">5</div><div class="label">⚠️ Security / Spam</div></div>
    <div class="meta-item"><div class="num">7</div><div class="label">🟢 Job Leads</div></div>
    <div class="meta-item"><div class="num">2</div><div class="label">🔵 RSVPs Needed</div></div>
    <div class="meta-item"><div class="num">1</div><div class="label">📦 Delivery Tomorrow</div></div>
  </div>
</div>

<!-- ════════════════════════════════════════════════
     2. EXECUTIVE SUMMARY
════════════════════════════════════════════════ -->
<div class="section theme-dark">
  <div class="section-title">⚡ Executive Summary</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li>
        <span class="bullet-icon">🔴</span>
        <div class="bullet-text">
          <strong>Biggest Risk: Multiple Phishing / Spam Emails in Your Inbox & Junk</strong>
          <span>Several highly suspicious emails remain unread and NOT in trash — including fake "TEMU Mystery Box," fake CVS prize, fake cloud storage block, and a sexually explicit spam. These must be marked as phishing and deleted immediately. One Bank of America transfer alert (account ending 7471, $200+) also requires verification.</span>
        </div>
      </li>
      <li>
        <span class="bullet-icon">🟢</span>
        <div class="bullet-text">
          <strong>Biggest Opportunity: CHRO Role ($250K–$300K) + VP of People at Hometown Soccer Holdings</strong>
          <span>LinkedIn Job Alerts surfaced a CHRO role in Private Equity/Investment Management via Empathy Talent (up to $300K/year) — received twice, suggesting high relevance. Additionally, Indeed flagged VP, People &amp; Culture at Hometown Soccer Holdings. You also emailed yourself multiple LinkedIn job links overnight — review and prioritize today.</span>
        </div>
      </li>
      <li>
        <span class="bullet-icon">🔵</span>
        <div class="bullet-text">
          <strong>Biggest Calendar Item: HR Networking Open Office Hours — TODAY 12:00 PM (RSVP Pending)</strong>
          <span>A large-group HR networking/job search Zoom is scheduled for today at noon (1 hr). Status is "needsAction" — you have not RSVP'd. Also note: FedEx shipment from Synergeyes Inc. is scheduled for delivery TOMORROW, June 19, and your dental appointment (Cavity) is also tomorrow at 10:30 AM.</span>
        </div>
      </li>
    </ul>
  </div>
</div>

<!-- ════════════════════════════════════════════════
     3. ACTION REQUIRED
════════════════════════════════════════════════ -->
<div class="section theme-red">
  <div class="section-title">🚨 Action Required</div>
  <div class="section-body">

    <div class="card card-red">
      <div class="meta-row"><span class="badge badge-red">URGENT – SECURITY</span><span>From: Multiple Phishing Senders</span><span>Received: Jun 18</span></div>
      <h3>🚫 Phishing / Spam Emails — NOT in Trash — Require Immediate Deletion</h3>
      <p><strong>Emails at risk:</strong><br>
      • <em>"'TEMU' — melissaw212, You have won a TEMU Mystery Box"</em> (spoofed sender)<br>
      • <em>"CVSRewards — melissaw212, You Are Our 3rd Winner!!"</em> (spoofed CVS)<br>
      • <em>"melissaw212 — Your Account Has been Blocked! Photos will be Removed"</em> (fake cloud warning)<br>
      • <em>"'Cloud-team' — We've blocked your account! melissaw212!"</em> (fake cloud warning)<br>
      • <em>"'Lost Biblical Secret' — Biblical erection center"</em> (explicit spam)</p>
      <p class="action-line">➡ Mark all as phishing/spam, delete immediately, and do NOT click any links.</p>
      <div class="meta-row"><span>Due: TODAY</span></div>
    </div>

    <div class="card card-red">
      <div class="meta-row"><span class="badge badge-red">URGENT – FINANCIAL</span><span>From: Bank of America</span><span>Received: Wed Jun 17 (Trash)</span></div>
      <h3>💳 Bank of America — Online Transfer Over Limit (Account ending 7471, $200+)</h3>
      <p>An alert was sent indicating a transfer exceeded the limit you set on account ending 7471. The email was sent to Trash — verify this was done by you and that no unauthorized transfer occurred.</p>
      <p class="action-line">➡ Log in directly to BankofAmerica.com (do not click email link) and verify the transfer. Confirm it was authorized.</p>
      <div class="meta-row"><span>Due: TODAY</span></div>
    </div>

    <div class="card card-yellow">
      <div class="meta-row"><span class="badge badge-yellow">RSVP NEEDED</span><span>From: Google Calendar</span><span>Today 12:00 PM – 1:00 PM</span></div>
      <h3>📅 HR Networking &amp; Job Search: Open Office Hours — Zoom (Status: Needs Action)</h3>
      <p>You have not responded to today's HR networking Zoom at 12:00 PM. This is a large group (170+ attendees) focused on job search and professional networking — highly relevant to your current situation.</p>
      <p class="action-line">➡ RSVP "Accept" and join at noon. Link: https://us06web.zoom.us/j/85945371140</p>
      <div class="meta-row"><span>Due: TODAY by 12:00 PM</span></div>
    </div>

    <div class="card card-yellow">
      <div class="meta-row"><span class="badge badge-yellow">RSVP NEEDED</span><span>From: Google Calendar</span><span>Wed Jun 24, 12:00 PM – 1:30 PM</span></div>
      <h3>📅 HR Networking &amp; Job Search Group — Zoom (Jun 24, Status: Needs Action)</h3>
      <p>A follow-up group networking session is on Jun 24 at noon (1.5 hrs). Status is still "needsAction." Note: You also have a separate "Network" event confirmed at the same time on Jun 24 — potential duplicate/conflict.</p>
      <p class="action-line">➡ RSVP and reconcile with the "Network" event already confirmed for the same time slot.</p>
      <div class="meta-row"><span>Due: Before Jun 24</span></div>
    </div>

    <div class="card card-green">
      <div class="meta-row"><span class="badge badge-green">HIGH PRIORITY – JOB SEARCH</span><span>From: LinkedIn Job Alerts</span><span>Received: Jun 18</span></div>
      <h3>💼 CHRO Role at Empathy Talent — $250K–$300K (Private Equity / Investment Mgmt)</h3>
      <p>This alert arrived TWICE (3:05 AM and 10:06 AM), suggesting your job alert pipeline flagged it as highly relevant. PE/investment management CHRO roles at this comp level are rare. Review immediately and apply if qualified.</p>
      <p class="action-line">➡ Open LinkedIn alert, review full JD, and apply or engage recruiter today.</p>
      <div class="meta-row"><span>Due: TODAY (competitive role)</span></div>
    </div>

    <div class="card card-green">
      <div class="meta-row"><span class="badge badge-green">HIGH PRIORITY – JOB SEARCH</span><span>From: Indeed</span><span>Received: Jun 18</span></div>
      <h3>💼 VP, People &amp; Culture — Hometown Soccer Holdings</h3>
      <p>Indeed matched your profile to a VP of People &amp; Culture role at Hometown Soccer Holdings. Sports industry HR leadership role — unique vertical worth evaluating.</p>
      <p class="action-line">➡ Review the full job posting on Indeed and assess fit. Apply or save for follow-up.</p>
      <div class="meta-row"><span>Due: TODAY or Tomorrow</span></div>
    </div>

    <div class="card card-green">
      <div class="meta-row"><span class="badge badge-green">JOB SEARCH</span><span>From: Yourself (melissaw212@gmail.com)</span><span>Received: Wed Jun 17 (late night)</span></div>
      <h3>📎 5 Self-Sent LinkedIn Job / Article Links — Review &amp; Organize</h3>
      <p>You emailed yourself 5 items overnight (4 job links + 1 LinkedIn article about CHROs using Claude). These are unsorted leads in your inbox. One appears to be a duplicate subject "Jobs" + blank subject pointing to the same LinkedIn job ID (4428782243).</p>
      <p class="action-line">➡ Review all 5 links, add to your job tracker, and delete duplicate emails. Consider the Claude/CHRO article for your LinkedIn writing pipeline.</p>
      <div class="meta-row"><span>Due: Today</span></div>
    </div>

    <div class="card card-yellow">
      <div class="meta-row"><span class="badge badge-yellow">BILLING</span><span>From: Anthropic PBC</span><span>Received: Jun 18, 2:25 AM</span></div>
      <h3>🧾 Anthropic Receipt #2906-3703-7416</h3>
      <p>A new receipt from Anthropic arrived overnight. Given your active use of Claude for job search automation (pipeline diagnostics, scheduled runs), confirm the charge is expected.</p>
      <p class="action-line">➡ Open receipt, verify amount, file for records.</p>
      <div class="meta-row"><span>Due: This week</span></div>
    </div>

    <div class="card card-yellow">
      <div class="meta-row"><span class="badge badge-yellow">BILLING</span><span>From: Target Circle Card</span><span>Received: Jun 18</span></div>
      <h3>💳 Target Circle Card Statement Available (ending in 7697)</h3>
      <p>Your monthly statement is ready online. Review and pay before the due date.</p>
      <p class="action-line">➡ Log in to Target Circle Card portal and review/pay statement.</p>
      <div class="meta-row"><span>Due: Check statement for due date</span></div>
    </div>

    <div class="card card-yellow">
      <div class="meta-row"><span class="badge badge-yellow">BILLING / DEADLINE</span><span>From: Google Calendar</span><span>Jun 23 (All Day)</span></div>
      <h3>📆 Verizon Fios Bill Due — June 23</h3>
      <p>Reminder flagged on your calendar that Verizon Fios bill is due on June 23.</p>
      <p class="action-line">➡ Pay Verizon Fios bill before June 23 to avoid service interruption.</p>
      <div class="meta-row"><span>Due: Jun 23</span></div>
    </div>

    <div class="card card-blue">
      <div class="meta-row"><span class="badge badge-blue">DELIVERY</span><span>From: FedEx Delivery Manager</span><span>Received: Jun 18</span></div>
      <h3>📦 FedEx Delivery Tomorrow — Synergeyes Inc. (Tracking: 530738347896)</h3>
      <p>A shipment from Synergeyes Inc. (contact lens / eye care company) is scheduled for delivery TOMORROW, Friday June 19. Note: your Eye Dr. appointment is also June 23.</p>
      <p class="action-line">➡ Ensure you're home or have a secure delivery location tomorrow. Track via FedEx Delivery Manager.</p>
      <div class="meta-row"><span>Due: Tomorrow, Jun 19</span></div>
    </div>

    <div class="card card-purple">
      <div class="meta-row"><span class="badge badge-purple">NETWORKING EVENT</span><span>From: Bon Sanchez / Be The Change HR</span><span>Received: Jun 18</span></div>
      <h3>🍵 Tea with LeiLani — July In-Person Gathering (Thursday, July ~1st)</h3>
      <p>You were personally invited by Bon Sanchez to LeiLani's in-person tea gathering in July. This is a professional/community networking event relevant to your HR career. No date confirmed in snippet but described as "Thursday, July 1" area.</p>
      <p class="action-line">➡ Reply to Bon Sanchez to confirm attendance. Add to calendar.</p>
      <div class="meta-row"><span>Due: RSVP this week</span></div>
    </div>

  </div>
</div>

<!-- ════════════════════════════════════════════════
     4. FULL 7-DAY CALENDAR
════════════════════════════════════════════════ -->
<div class="section theme-blue">
  <div class="section-title">📅 Full 7-Day Calendar — Jun 18–24, 2026</div>
  <div class="section-body">

    <!-- Thursday June 18 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Thursday, June 18, 2026 — TODAY</div>

      <div class="cal-event declined">
        <div class="time">9:00 – 10:30 AM</div>
        <div class="event-detail">
          <div class="title">Executive Roundtable <span class="badge badge-gray">DECLINED</span></div>
          <div class="sub">Hosted by: John Madigan &nbsp;|&nbsp; Zoom: <a href="https://us02web.zoom.us/j/207786667" target="_blank">Meeting ID 207 786 667</a> &nbsp;|&nbsp; PW: 205454</div>
          <div class="sub">ℹ️ You declined this event. No action needed unless you wish to rejoin.</div>
        </div>
      </div>

      <div class="cal-event needs-rsvp">
        <div class="time">12:00 – 1:00 PM</div>
        <div class="event-detail">
          <div class="title">HR Networking &amp; Job Search: Open Office Hours — Zoom 2 <span class="badge badge-yellow">⚠ RSVP NEEDED</span></div>
          <div class="sub">170+ attendees &nbsp;|&nbsp; <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Join Zoom</a></div>
          <div class="sub">📝 Note: AI notetaking tools are asked to be disabled. Open discussion format.</div>
          <div class="sub">⚡ <strong>Prep:</strong> Review recent job leads before noon. Prepare 30-sec intro if speaking.</div>
          <div class="sub warn">⚠ ACTION NEEDED: RSVP before session starts.</div>
        </div>
      </div>
    </div>

    <!-- Friday June 19 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Friday, June 19, 2026</div>

      <div class="cal-event">
        <div class="time">10:30 – 11:30 AM</div>
        <div class="event-detail">
          <div class="title">Cavity (Dental Appointment) <span class="badge badge-green">CONFIRMED</span></div>
          <div class="sub">📍 Location not specified in calendar — confirm address with your dentist.</div>
          <div class="sub">⚡ <strong>Prep:</strong> Allow travel time. Confirm office address if not memorized.</div>
          <div class="sub">📦 <strong>Note:</strong> FedEx delivery from Synergeyes also expected today — plan accordingly.</div>
        </div>
      </div>

      <div class="cal-event" style="border-color:#059669;background:#f0fdf4;">
        <div class="time">All Day</div>
        <div class="event-detail">
          <div class="title">📦 FedEx Delivery — Synergeyes Inc. <span class="badge badge-green">TRACKING: 530738347896</span></div>
          <div class="sub">Ensure someone is available to receive the package, or arrange a secure drop location.</div>
        </div>
      </div>
    </div>

    <!-- Saturday June 20 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Saturday, June 20, 2026</div>
      <div class="cal-event" style="border-color:#9ca3af;background:#f9fafb;">
        <div class="time">All Day</div>
        <div class="event-detail">
          <div class="title">No Events Scheduled</div>
          <div class="sub">📌 Nextdoor FYI: Part-time Event Assistant needed in Carl Schurz Park (Upper East Side) — Saturday June 20. Not relevant to Melissa's role but noted from email.</div>
        </div>
      </div>
    </div>

    <!-- Sunday June 21 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Sunday, June 21, 2026</div>
      <div class="cal-event" style="border-color:#9ca3af;background:#f9fafb;">
        <div class="time">All Day</div>
        <div class="event-detail">
          <div class="title">No Events Scheduled</div>
          <div class="sub">🌟 Father's Day. Plan accordingly.</div>
        </div>
      </div>
    </div>

    <!-- Monday June 22 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Monday, June 22, 2026</div>
      <div class="cal-event" style="border-color:#9ca3af;background:#f9fafb;">
        <div class="time">All Day</div>
        <div class="event-detail">
          <div class="title">No Events Scheduled</div>
          <div class="sub">Good window for job applications and follow-ups.</div>
        </div>
      </div>
    </div>

    <!-- Tuesday June 23 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Tuesday, June 23, 2026</div>

      <div class="cal-event" style="border-color:#d97706;background:#fffbeb;">
        <div class="time">All Day</div>
        <div class="event-detail">
          <div class="title">💡 Verizon Fios Bill Due <span class="badge badge-yellow">DEADLINE</span></div>
          <div class="sub">Pay Verizon Fios bill today to avoid interruption. Set up autopay if not already configured.</div>
        </div>
      </div>

      <div class="cal-event">
        <div class="time">9:00 – 10:00 AM</div>
        <div class="event-detail">
          <div class="title">Eye Dr. Appointment <span class="badge badge-green">CONFIRMED</span></div>
          <div class="sub">📍 Location not specified. &nbsp;|&nbsp; FedEx delivery (Synergeyes — eye care) arrived Jun 19; may be related.</div>
          <div class="sub">⚡ <strong>Prep:</strong> Confirm office address. Arrange transportation if needed (dilated eyes = no driving).</div>
        </div>
      </div>
    </div>

    <!-- Wednesday June 24 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Wednesday, June 24, 2026</div>

      <div class="cal-event needs-rsvp">
        <div class="time">12:00 – 1:30 PM</div>
        <div class="event-detail">
          <div class="title">HR Networking &amp; Job Search Group — Zoom <span class="badge badge-yellow">⚠ RSVP NEEDED</span></div>
          <div class="sub">170+ attendees &nbsp;|&nbsp; <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Join Zoom</a></div>
          <div class="sub">⚡ <strong>Prep:</strong> Review HR Networking Team Guidelines (linked in description). Prepare updates on job search status.</div>
          <div class="sub warn">⚠ CONFLICT: "Network" event also confirmed for 12:00–1:30 PM same day. These appear to be the same event — reconcile and remove duplicate.</div>
        </div>
      </div>

      <div class="cal-event" style="border-color:#059669;background:#f0fdf4;">
        <div class="time">12:00 – 1:30 PM</div>
        <div class="event-detail">
          <div class="title">Network <span class="badge badge-green">CONFIRMED</span> <span class="badge badge-red">⚠ DUPLICATE?</span></div>
          <div class="sub">No additional details. Appears to be a personal reminder overlapping with the Zoom networking event above.</div>
          <div class="sub warn">➡ Reconcile: determine if this is a duplicate of the HR Networking Zoom or a separate commitment.</div>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- ════════════════════════════════════════════════
     5. JOB SEARCH & INTERVIEW PIPELINE
════════════════════════════════════════════════ -->
<div class="section theme-green">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">

    <div class="sub-header">🔔 Active Job Alerts / Leads (Inbox)</div>
    <table>
      <tr>
        <th>Role</th>
        <th>Company / Source</th>
        <th>Comp</th>
        <th>Fit</th>
        <th>Status</th>
        <th>Action</th>
      </tr>
      <tr>
        <td><strong>Chief Human Resources Officer</strong> (PE / Investment Mgmt)</td>
        <td>Empathy Talent via LinkedIn<br><small>Received twice: 3:05 AM &amp; 10:06 AM</small></td>
        <td>$250K–$300K/yr</td>
        <td><span class="pill pill-high">HIGH</span></td>
        <td><span class="badge badge-yellow">Unread × 2</span></td>
        <td>Review JD &amp; apply TODAY</td>
      </tr>
      <tr>
        <td><strong>VP, People &amp; Culture</strong></td>
        <td>Hometown Soccer Holdings via Indeed</td>
        <td>Not specified</td>
        <td><span class="pill pill-high">HIGH</span></td>
        <td><span class="badge badge-yellow">Unread</span></td>
        <td>Review &amp; assess fit today</td>
      </tr>
      <tr>
        <td><strong>LinkedIn Job (ID: 4428782243)</strong></td>
        <td>Self-sent link (melissaw212) — emailed twice</td>
        <td>Unknown</td>
        <td><span class="pill pill-medium">MEDIUM</span></td>
        <td><span class="badge badge-yellow">Unread</span></td>
        <td>Open link, identify role, add to tracker</td>
      </tr>
      <tr>
        <td><strong>LinkedIn Job (ID: 4427336822)</strong></td>
        <td>Self-sent link (melissaw212)</td>
        <td>Unknown</td>
        <td><span class="pill pill-medium">MEDIUM</span></td>
        <td><span class="badge badge-yellow">Unread</span></td>
        <td>Open link, identify role, add to tracker</td>
      </tr>
      <tr>
        <td><strong>LinkedIn Job (ID: 4419482348)</strong></td>
        <td>Self-sent link (melissaw212)</td>
        <td>Unknown</td>
        <td><span class="pill pill-medium">MEDIUM</span></td>
        <td><span class="badge badge-yellow">Unread</span></td>
        <td>Open link, identify role, add to tracker</td>
      </tr>
      <tr>
        <td><strong>Senior HRBP</strong></td>
        <td>Axion via LinkedIn Job Alerts</td>
        <td>Not specified</td>
        <td><span class="pill pill-medium">MEDIUM</span></td>
        <td><span class="badge badge-yellow">Unread, Inbox</span></td>
        <td>Review — Founded 2021 startup HRBP; assess level vs. goals</td>
      </tr>
      <tr>
        <td><strong>Director of Human Resources</strong></td>
        <td>Lighthouse Employees Inc. via Glassdoor (Remote)</td>
        <td>Not specified</td>
        <td><span class="pill pill-medium">MEDIUM</span></td>
        <td><span class="badge badge-gray">Read, Trash</span></td>
        <td>Was sent to Trash — confirm intentional skip or restore</td>
      </tr>
      <tr>
        <td><strong>VP of People</strong></td>
        <td>Nitra via LinkedIn (Trash)</td>
        <td>Not specified</td>
        <td><span class="pill pill-low">LOW–MED</span></td>
        <td><span class="badge badge-gray">Read, Trash</span></td>
        <td>In Trash — confirm if intentional skip</td>
      </tr>
    </table>

    <div class="sub-header" style="margin-top:18px;">🔗 LinkedIn Article (Self-Saved)</div>
    <div class="card card-green">
      <h3>📰 "CHROs Can Use Claude to Find Out Why Their [Employees]..." — LinkedIn Post by Warren Wang</h3>
      <p>You saved this LinkedIn post overnight. Potentially relevant both as a content idea for your own LinkedIn/Medium article (you noted in a draft email: "thoughts for a LinkedIn article...") and as a professional insight.</p>
      <p class="action-line">➡ Review post. Consider referencing it in your LinkedIn article in development.</p>
    </div>

    <div class="sub-header" style="margin-top:18px;">🤝 Networking Events</div>
    <table>
      <tr>
        <th>Event</th>
        <th>Date/Time</th>
        <th>Status</th>
        <th>Action</th>
      </tr>
      <tr>
        <td>HR Networking &amp; Job Search: Open Office Hours — Zoom 2</td>
        <td>TODAY, Jun 18 &nbsp;12:00–1:00 PM</td>
        <td><span class="badge badge-yellow">Needs RSVP</span></td>
        <td>RSVP &amp; join today</td>
      </tr>
      <tr>
        <td>HR Networking &amp; Job Search Group — Zoom</td>
        <td>Jun 24, 12:00–1:30 PM</td>
        <td><span class="badge badge-yellow">Needs RSVP</span></td>
        <td>RSVP before Jun 24</td>
      </tr>
      <tr>
        <td>Tea with LeiLani (Be The Change HR)</td>
        <td>Thursday ~July 1</td>
        <td><span class="badge badge-orange">Invited, No RSVP</span></td>
        <td>Reply to Bon Sanchez to confirm</td>
      </tr>
    </table>

    <div class="sub-header" style="margin-top:18px;">🤖 Job Search Automation (Your Pipeline)</div>
    <div class="card card-blue">
      <h3>⚙️ Automated HR Search Pipeline — Active & Functioning</h3>
      <p>Your automated pipeline (GitHub Actions → Exa + Apify → melissaw212@gmail.com) sent a results digest on Jun 17 (Run 27730008322: 1 Exa + 17 Apify results) and a TEST2 diagnostic on Jun 18. Files are backed up locally on your Mac at <code>~/Documents/Claude/Scheduled/job-search/local-fallback/</code>.</p>
      <p class="action-line">➡ Review the Jun 17 pipeline results (now in Trash — restore or review before deleting). Confirm TEST2 diagnostic passed.</p>
    </div>

  </div>
</div>

<!-- ════════════════════════════════════════════════
     6. FULL EMAIL REVIEW BY CATEGORY
════════════════════════════════════════════════ -->
<div class="section theme-dark">
  <div class="section-title">📬 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="sub-header" style="color:#dc2626;">🔴 Security / Risk — 6 Emails</div>
    <table>
      <tr><th>From</th><th>Subject</th><th>Location</th><th>Action</th></tr>
      <tr><td>'Lost Biblical Secret' (spoofed)</td><td>Biblical explicit spam</td><td>Not in Trash</td><td><span class="badge badge-red">Delete + Mark Phishing</span></td></tr>
      <tr><td>'TEMU' (spoofed)</td><td>TEMU Mystery Box winner</td><td>Not in Trash</td><td><span class="badge badge-red">Delete + Mark Phishing</span></td></tr>
      <tr><td>CVSRewards (spoofed)</td><td>3rd Winner!! CVS Gift Card</td><td>Not in Trash</td><td><span class="badge badge-red">Delete + Mark Phishing</span></td></tr>
      <tr><td>melissaw212 (spoofed)</td><td>Your Account Has Been Blocked – Photos will be Removed</td><td>Not in Trash</td><td><span class="badge badge-red">Delete + Mark Phishing</span></td></tr>
      <tr><td>'Cloud-team' (spoofed)</td><td>We've blocked your account! melissaw212!</td><td>Not in Trash</td><td><span class="badge badge-red">Delete + Mark Phishing</span></td></tr>
      <tr><td>'melissaw212' casino (spoofed)</td><td>$4000 Payout Verification – Miami Club Casino</td><td>Trash ✓</td><td><span class="badge badge-gray">Already in Trash — permanently delete</span></td></tr>
    </table>

    <!-- JOB SEARCH -->
    <div class="sub-header" style="color:#059669;margin-top:18px;">🟢 Job Search — 12 Emails</div>
    <table>
      <tr><th>From</th><th>Subject</th><th>Location</th><th>Action</th></tr>
      <tr><td>LinkedIn Job Alerts</td><td>CHRO at Empathy Talent ($250K–$300K) — received TWICE</td><td>Inbox ×2</td><td><span class="badge badge-green">Review &amp; Apply TODAY</span></td></tr>
      <tr><td>Indeed</td><td>VP, People &amp; Culture @ Hometown Soccer Holdings</td><td>Inbox</td><td><span class="badge badge-green">Review &amp; Apply</span></td></tr>
      <tr><td>LinkedIn Job Alerts</td><td>Senior HRBP at Axion</td><td>Inbox</td><td><span class="badge badge-green">Review</span></td></tr>
      <tr><td>LinkedIn Job Alerts</td><td>VP of People at Nitra</td><td>Trash</td><td><span class="badge badge-yellow">Confirm skip or restore</span></td></tr>
      <tr><td>Glassdoor Jobs</td><td>Director of HR at Lighthouse Employees Inc. + 2 more (Remote)</td><td>Trash</td><td><span class="badge badge-yellow">Confirm skip or restore</span></td></tr>
      <tr><td>Glassdoor</td><td>Cprime employee reviews update — addressed to "Larry"</td><td>Trash</td><td><span class="badge badge-gray">Possible wrong account — delete</span></td></tr>
      <tr><td>Melissa W (self)</td><td>"Jobs" — LinkedIn job ID 4428782243</td><td>Inbox</td><td><span class="badge badge-green">Open, log, delete duplicate</span></td></tr>
      <tr><td>Melissa W (self)</td><td>(blank) — LinkedIn job ID 4428782243 (duplicate)</td><td>Inbox</td><td><span class="badge badge-gray">Delete duplicate</span></td></tr>
      <tr><td>Melissa W (self)</td><td>(blank) — LinkedIn job ID 4427336822</td><td>Inbox</td><td><span class="badge badge-green">Open &amp; log</span></td></tr>
      <tr><td>Melissa W (self)</td><td>(blank) — LinkedIn post CHROs + Claude</td><td>Inbox</td><td><span class="badge badge-green">Save for LinkedIn article</span></td></tr>
      <tr><td>Melissa W (self)</td><td>(blank) — LinkedIn job ID 4419482348</td><td>Inbox</td><td><span class="badge badge-green">Open &amp; log</span></td></tr>
      <tr><td>melissaw212 (self-automated)</td><td>HR Search PM – TEST2 – pipeline diagnostic</td><td>Sent/Archive</td><td><span class="badge badge-blue">Confirm TEST2 passed</span></td></tr>
    </table>

    <!-- PROFESSIONAL DEVELOPMENT / NETWORKING -->
    <div class="sub-header" style="color:#7c3aed;margin-top:18px;">🟣 Professional Development &amp; Networking — 4 Emails</div>
    <table>
      <tr><th>From</th><th>Subject</th><th>Location</th><th>Action</th></tr>
      <tr><td>Bon Sanchez / Be The Change HR</td><td>Tea with LeiLani (July In-Person Gathering)</td><td>Inbox</td><td><span class="badge badge-purple">RSVP to Bon Sanchez</span></td></tr>
      <tr><td>The People People Group (TPPG)</td><td>Guidelines for Employment Letters + 8 more topics</td><td>Trash</td><td><span class="badge badge-yellow">Review before deleting — HR insights</span></td></tr>
      <tr><td>Stanton Chase via LinkedIn</td><td>Inclusive Leadership in Professional Services</td><td>Archive (not Inbox)</td><td><span class="badge badge-purple">Read when time permits</span></td></tr>
      <tr><td>melissa (self)</td><td>"thoughts for a LinkedIn article..." (draft idea)</td><td>Sent/Archive</td><td><span class="badge badge-purple">Develop article — use Warren Wang LinkedIn post as anchor</span></td></tr>
    </table>

    <!-- CALENDAR / EVENTS -->
    <div class="sub-header" style="color:#1d4ed8;margin-top:18px;">🔵 Calendar / Events — 1 Email</div>
    <table>
      <tr><th>From</th><th>Subject</th><th>Location</th><th>Action</th></tr>
      <tr><td>Nextdoor (Yorkville)</td><td>Part-time Event Assistant Needed – Saturday June 20 (Carl Schurz Park)</td><td>Archive</td><td><span class="badge badge-gray">Not relevant — ignore</span></td></tr>
    </table>

    <!-- FINANCIAL / BILLING -->
    <div class="sub-header" style="color:#d97706;margin-top:18px;">🟡 Financial / Billing — 4 Emails</div>
    <table>
      <tr><th>From</th><th>Subject</th><th>Location</th><th>Action</th></tr>
      <tr><td>Anthropic PBC</td><td>Receipt #2906-3703-7416</td><td>Inbox</td><td><span class="badge badge-yellow">Verify charge &amp; file</span></td></tr>
      <tr><td>Target Circle Card</td><td>Statement available (ending 7697)</td><td>Inbox</td><td><span class="badge badge-yellow">Log in &amp; pay</span></td></tr>
      <tr><td>Bank of America</td><td>Online transfer occurred over limit (account 7471, $200+)</td><td>Trash</td><td><span class="badge badge-red">Verify transaction was authorized</span></td></tr>
      <tr><td>My Best Buy Visa (Citi) ×2</td><td>4th of July Appliances Sale / Fan e-gift cards</td><td>Trash ×2</td><td><span class="badge badge-gray">Already in trash — delete</span></td></tr>
    </table>

    <!-- DELIVERY / HEALTH -->
    <div class="sub-header" style="color:#059669;margin-top:18px;">🟢 Medical / Health &amp; Delivery — 1 Email</div>
    <table>
      <tr><th>From</th><th>Subject</th><th>Location</th><th>Action</th></tr>
      <tr><td>FedEx Delivery Manager</td><td>Shipment from Synergeyes Inc. — delivery tomorrow (tracking 530738347896)</td><td>Inbox</td><td><span class="badge badge-yellow">Plan to receive tomorrow</span></td></tr>
    </table>

    <!-- PERSONAL -->
    <div class="sub-header" style="color:#374151;margin-top:18px;">⚪ Personal — 4 Emails</div>
    <table>
      <tr><th>From</th><th>Subject</th><th>Location</th><th>Action</th></tr>
      <tr><td>Match.com</td><td>Howard likes you. See if it's mutual.</td><td>Not Inbox/Not Trash</td><td><span class="badge badge-gray">Personal — review at leisure</span></td></tr>
      <tr><td>Match.com</td><td>Larry likes you. See if it's mutual.</td><td>Archive (read)</td><td><span class="badge badge-gray">Personal — already read</span></td></tr>
      <tr><td>Match.com</td><td>Eric likes you. See if it's mutual.</td><td>Archive (read)</td><td><span class="badge badge-gray">Personal — already read</span></td></tr>
      <tr><td>Jdate</td><td>You've Got a Like on Jdate ❤️</td><td>Trash</td><td><span class="badge badge-gray">Already in trash</span></td></tr>
    </table>

    <!-- NEWSLETTERS / SUBSCRIPTIONS -->
    <div class="sub-header" style="color:#7c3aed;margin-top:18px;">🟣 Newsletters / Subscriptions — 5 Emails</div>
    <table>
      <tr><th>From</th><th>Subject</th><th>Location</th><th>Action</th></tr>
      <tr><td>TLDR Newsletter</td><td>iPhone Air 2, Anthropic ban, Claude Design + Code</td><td>Trash</td><td><span class="badge badge-yellow">Review — Claude/AI content relevant</span></td></tr>
      <tr><td>The Hustle</td><td>Seeing travel differently</td><td>Trash</td><td><span class="badge badge-gray">Already in trash — delete</span></td></tr>
      <tr><td>The Daily Skimm</td><td>Insert favorite dad joke here (Father's Day issue)</td><td>Archive (not Inbox)</td><td><span class="badge badge-gray">Read later or delete</span></td></tr>
      <tr><td>BambooHR (Sadie)</td><td>[HR Hub] Burnout, Belonging &amp; More</td><td>Trash</td><td><span class="badge badge-yellow">Review before deleting — HR relevant</span></td></tr>
      <tr><td>CoolDeep AI</td><td>Content engine with zero designers</td><td>Trash</td><td><span class="badge badge-gray">Already in trash — delete</span></td></tr>
    </table>

    <!-- COMMUNITY / LOCAL -->
    <div class="sub-header" style="color:#374151;margin-top:18px;">⚪ Community / Local — 1 Email</div>
    <table>
      <tr><th>From</th><th>Subject</th><th>Location</th><th>Action</th></tr>
      <tr><td>Yorkville Nextdoor Trending Posts</td><td>What's a place around New York you find yourself going back to?</td><td>Archive</td><td><span class="badge badge-gray">Low priority — read at leisure</span></td></tr>
    </table>

    <!-- PIPELINE / AUTOMATION -->
    <div class="sub-header" style="color:#374151;margin-top:18px;">⚙️ Pipeline / Automation (Self) — 2 Emails</div>
    <table>
      <tr><th>From</th><th>Subject</th><th>Location</th><th>Action</th></tr>
      <tr><td>melissaw212@gmail.com (automated)</td><td>HR Search PM — 2026-06-18 — Run 27730008322 (Exa + Apify results)</td><td>Trash</td><td><span class="badge badge-yellow">Restore — review 17 Apify results before deleting</span></td></tr>
      <tr><td>melissa (self)</td><td>(blank) — Mac local-fallback folder confirmation</td><td>Sent/Archive</td><td><span class="badge badge-gray">Note kept — no action needed</span></td></tr>
    </table>

    <!-- PROMOTIONAL / RETAIL -->
    <div class="sub-header" style="color:#6b7280;margin-top:18px;">⬜ Promotional / Retail — 10 Emails</div>
    <table>
      <tr><th>From</th><th>Subject</th><th>Location</th><th>Action</th></tr>
      <tr><td>SHEIN ×3</td><td>Up to 70% OFF / 50% OFF deals (×3 — 2 identical)</td><td>Trash ×3</td><td><span class="badge badge-gray">Delete — duplicates</span></td></tr>
      <tr><td>Kohl's</td><td>Save 30% — Summer style on a budget</td><td>Trash</td><td><span class="badge badge-gray">Delete</span></td></tr>
      <tr><td>Gap Factory</td><td>60% Off Sitewide</td><td>Archive (read)</td><td><span class="badge badge-gray">Delete</span></td></tr>
      <tr><td>Old Navy Men's Sale</td><td>Men's styles from $10, $15, $20</td><td>Trash</td><td><span class="badge badge-gray">Delete — men's section mismatch</span></td></tr>
      <tr><td>Temu (legitimate)</td><td>We decided to surprise you with this (3 items for $10)</td><td>Trash</td><td><span class="badge badge-gray">Delete</span></td></tr>
      <tr><td>Delta Air Lines</td><td>Earn up to 90K Bonus Miles — SkyMiles Gold Amex Card</td><td>Trash</td><td><span class="badge badge-yellow">Review if interested in card offer</span></td></tr>
      <tr><td>My Best Buy Visa (Citi) ×2</td><td>Appliances 4th of July Sale / Fan e-gift cards</td><td>Trash ×2</td><td><span class="badge badge-gray">Delete</span></td></tr>
    </table>
    <p class="note">Note: My Best Buy Visa counted here; also noted under Financial/Billing above — counted only once in Email Accounting (under Promotional).</p>

  </div>
</div>

<!-- ════════════════════════════════════════════════
     7. TRASH REVIEW
════════════════════════════════════════════════ -->
<div class="section theme-orange">
  <div class="section-title">🗑️ Trash Review — 22 Emails in Trash</div>
  <div class="section-body">

    <div class="sub-header" style="color:#dc2626;">🔴 Restore Immediately (3 Items)</div>
    <table>
      <tr><th>Sender</th><th>Subject</th><th>Why Restore</th></tr>
      <tr>
        <td>melissaw212@gmail.com (automated)</td>
        <td>HR Search PM — 2026-06-18 — Run 27730008322</td>
        <td><strong>Your job search pipeline results</strong> — contains 1 Exa + 17 Apify job leads. Review before discarding.</td>
      </tr>
      <tr>
        <td>The People People Group (TPPG)</td>
        <td>[TPPG] Guidelines for Issuing Employment Letters + 8 more HR topics</td>
        <td><strong>HR professional content</strong> — directly relevant to your field. Employment letters guidance may be useful.</td>
      </tr>
      <tr>
        <td>Bank of America</td>
        <td>Online transfer occurred over limit — Account ending 7471, $200+</td>
        <td><strong>Financial security alert</strong> — verify this transfer was authorized before permanently deleting.</td>
      </tr>
    </table>

    <div class="sub-header" style="color:#d97706;margin-top:16px;">🟡 Review Before Deleting (5 Items)</div>
    <table>
      <tr><th>Sender</th><th>Subject</th><th>Why Review</th></tr>
      <tr>
        <td>TLDR Newsletter</td>
        <td>iPhone Air 2, Anthropic ban, Claude Design + Code</td>
        <td>Contains Anthropic/Claude news — relevant to your AI-assisted job search and potential LinkedIn article content.</td>
      </tr>
      <tr>
        <td>BambooHR (Sadie)</td>
        <td>[HR Hub] People Need People: Burnout, Belonging &amp; More</td>
        <td>HR professional newsletter — burnout &amp; belonging topics relevant to CHRO/VP People roles you're targeting.</td>
      </tr>
      <tr>
        <td>LinkedIn Job Alerts</td>
        <td>VP of People at Nitra</td>
        <td>HR leadership role — confirm this was intentionally skipped before deleting.</td>
      </tr>
      <tr>
        <td>Glassdoor Jobs</td>
        <td>Director of HR at Lighthouse Employees Inc. + 2 more (Remote)</td>
        <td>Remote HR roles — confirm these were intentionally skipped. Note: addressed to "Larry" — possible wrong name in system.</td>
      </tr>
      <tr>
        <td>Delta Air Lines</td>
        <td>Earn Up To 90K Bonus Miles —
