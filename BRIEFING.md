<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing – Melissa W | June 24, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px 48px; }

  /* Header */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px 24px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .sub { font-size: 15px; color: #a8c0e8; margin-top: 6px; }
  .header-stats { display: flex; gap: 24px; margin-top: 20px; flex-wrap: wrap; }
  .hstat { background: rgba(255,255,255,0.1); border-radius: 8px; padding: 10px 20px; text-align: center; }
  .hstat .num { font-size: 22px; font-weight: 700; color: #7ec8e3; }
  .hstat .lbl { font-size: 11px; color: #cdd; text-transform: uppercase; letter-spacing: 0.8px; margin-top: 2px; }

  /* Section Headers */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; letter-spacing: 0.4px; padding: 10px 16px; border-radius: 8px 8px 0 0; display: flex; align-items: center; gap: 8px; }
  .section-body { border-radius: 0 0 8px 8px; padding: 16px; }

  /* Color themes */
  .red .section-title    { background: #c0392b; color: #fff; }
  .red .section-body     { background: #fff5f5; border: 1px solid #f5c6c6; border-top: none; }
  .yellow .section-title { background: #e67e22; color: #fff; }
  .yellow .section-body  { background: #fffbf0; border: 1px solid #fde8b0; border-top: none; }
  .blue .section-title   { background: #2471a3; color: #fff; }
  .blue .section-body    { background: #f0f6ff; border: 1px solid #b8d4f0; border-top: none; }
  .green .section-title  { background: #1e8449; color: #fff; }
  .green .section-body   { background: #f0faf4; border: 1px solid #a9dbb8; border-top: none; }
  .purple .section-title { background: #7d3c98; color: #fff; }
  .purple .section-body  { background: #faf0ff; border: 1px solid #d7b8f0; border-top: none; }
  .gray .section-title   { background: #5d6d7e; color: #fff; }
  .gray .section-body    { background: #f8f9fa; border: 1px solid #dee2e6; border-top: none; }
  .dark .section-title   { background: #2c3e50; color: #fff; }
  .dark .section-body    { background: #f4f6f8; border: 1px solid #c8d0d8; border-top: none; }

  /* Cards */
  .card { border-radius: 8px; padding: 14px 16px; margin-bottom: 12px; border-left: 5px solid #ccc; background: #fff; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }
  .card-red    { border-left-color: #c0392b; background: #fff8f8; }
  .card-yellow { border-left-color: #e67e22; background: #fffdf5; }
  .card-blue   { border-left-color: #2471a3; background: #f5f9ff; }
  .card-green  { border-left-color: #1e8449; background: #f5fff9; }
  .card-purple { border-left-color: #7d3c98; background: #fbf5ff; }
  .card-gray   { border-left-color: #95a5a6; background: #fafafa; }

  .card-title  { font-weight: 700; font-size: 14px; margin-bottom: 4px; }
  .card-meta   { font-size: 12px; color: #666; margin-bottom: 6px; }
  .card-body   { font-size: 13px; color: #333; }
  .card-action { margin-top: 8px; font-size: 12px; background: #eef2f7; border-radius: 5px; padding: 6px 10px; color: #1a5276; font-weight: 600; }

  /* Badges */
  .badge { display: inline-block; border-radius: 12px; padding: 2px 10px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
  .badge-red    { background: #c0392b; color: #fff; }
  .badge-yellow { background: #e67e22; color: #fff; }
  .badge-green  { background: #1e8449; color: #fff; }
  .badge-blue   { background: #2471a3; color: #fff; }
  .badge-purple { background: #7d3c98; color: #fff; }
  .badge-gray   { background: #7f8c8d; color: #fff; }
  .badge-high   { background: #c0392b; color: #fff; }
  .badge-medium { background: #e67e22; color: #fff; }
  .badge-low    { background: #27ae60; color: #fff; }

  /* Tables */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #2c3e50; color: #fff; padding: 9px 12px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
  td { padding: 8px 12px; border-bottom: 1px solid #e8ecef; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #f8f9fa; }
  tr:hover td { background: #eef2f7; }

  /* Calendar */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { background: #2c3e50; color: #fff; padding: 8px 14px; border-radius: 6px; font-weight: 700; font-size: 13px; margin-bottom: 8px; }
  .cal-event { background: #fff; border-radius: 6px; padding: 12px 14px; margin-bottom: 8px; border-left: 4px solid #2471a3; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
  .cal-event.status-declined { border-left-color: #c0392b; background: #fff8f8; }
  .cal-event.status-confirmed { border-left-color: #1e8449; background: #f5fff9; }
  .cal-event.status-needs   { border-left-color: #e67e22; background: #fffdf5; }
  .cal-time { font-weight: 700; font-size: 13px; color: #2471a3; }
  .cal-title { font-weight: 700; font-size: 14px; margin: 2px 0 4px; }
  .cal-detail { font-size: 12px; color: #555; margin-bottom: 2px; }
  .cal-warn { font-size: 12px; background: #fff3cd; border-radius: 4px; padding: 4px 8px; margin-top: 6px; color: #856404; font-weight: 600; }

  /* Summary bullets */
  .exec-bullet { background: #fff; border-radius: 8px; padding: 14px 18px; margin-bottom: 10px; display: flex; gap: 12px; align-items: flex-start; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }
  .exec-bullet-icon { font-size: 22px; }
  .exec-bullet-text { flex: 1; }
  .exec-bullet-text strong { display: block; font-size: 14px; margin-bottom: 2px; }
  .exec-bullet-text span { font-size: 13px; color: #555; }

  /* Grid */
  .grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  @media (max-width: 700px) { .grid2 { grid-template-columns: 1fr; } }

  /* Dashboard tiles */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 14px; }
  .dash-tile { background: #fff; border-radius: 10px; padding: 16px; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.09); border-top: 4px solid #ccc; }
  .dash-tile.t-red    { border-top-color: #c0392b; }
  .dash-tile.t-yellow { border-top-color: #e67e22; }
  .dash-tile.t-blue   { border-top-color: #2471a3; }
  .dash-tile.t-green  { border-top-color: #1e8449; }
  .dash-tile.t-purple { border-top-color: #7d3c98; }
  .dash-tile.t-gray   { border-top-color: #7f8c8d; }
  .dash-num { font-size: 30px; font-weight: 800; margin-bottom: 4px; }
  .dash-lbl { font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 0.6px; }

  /* Top priorities */
  .priority-card { background: #fff; border-radius: 10px; padding: 18px 20px; margin-bottom: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.09); display: flex; gap: 16px; align-items: flex-start; }
  .priority-num { width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; font-weight: 800; color: #fff; flex-shrink: 0; }
  .p1 { background: #c0392b; }
  .p2 { background: #e67e22; }
  .p3 { background: #1e8449; }

  hr.divider { border: none; border-top: 2px solid #e0e4ea; margin: 24px 0; }
  .note { font-size: 12px; color: #888; font-style: italic; margin-top: 6px; }
  ul.email-list { list-style: none; padding: 0; }
  ul.email-list li { padding: 5px 0; border-bottom: 1px dashed #e0e4ea; font-size: 13px; }
  ul.email-list li:last-child { border-bottom: none; }
  .tag-from { color: #2471a3; font-weight: 600; }
  .tag-subj { color: #333; }
  .tag-date { color: #888; font-size: 11px; float: right; }
</style>
</head>
<body>
<div class="page">

<!-- ============================================================ HEADER ============================================================ -->
<div class="header">
  <h1>📋 Executive Morning Briefing</h1>
  <div class="sub">Prepared by your Chief of Staff &nbsp;|&nbsp; Wednesday, June 24, 2026</div>
  <div class="header-stats">
    <div class="hstat"><div class="num">Melissa</div><div class="lbl">Good Morning</div></div>
    <div class="hstat"><div class="num">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="hstat"><div class="num">5</div><div class="lbl">Calendar Events</div></div>
    <div class="hstat"><div class="num">2</div><div class="lbl">Events Today</div></div>
    <div class="hstat"><div class="num">7</div><div class="lbl">Job Leads Active</div></div>
    <div class="hstat"><div class="num">3</div><div class="lbl">Security Flags</div></div>
  </div>
</div>

<!-- ============================================================ EXECUTIVE SUMMARY ============================================================ -->
<div class="section dark">
  <div class="section-title">⚡ Executive Summary</div>
  <div class="section-body">
    <div class="exec-bullet">
      <div class="exec-bullet-icon">🔴</div>
      <div class="exec-bullet-text">
        <strong>Biggest Risk: Multiple Active Phishing / Scam Emails in Your Inbox &amp; Spam Folders</strong>
        <span>At least 3 highly suspicious emails are impersonating "Cloud_Support," posing as your own email address, and a fake casino payment notice. These are phishing attempts targeting your credentials and payment information. Do not click any links. Mark as phishing and delete immediately.</span>
      </div>
    </div>
    <div class="exec-bullet">
      <div class="exec-bullet-icon">🟢</div>
      <div class="exec-bullet-text">
        <strong>Biggest Opportunity: 7 Active Senior HR Job Leads — Including CHRO at $250K–$300K and Senior Director Roles</strong>
        <span>LinkedIn, Indeed, and Glassdoor have surfaced multiple high-fit executive HR opportunities this morning, including a CHRO role via Empathy Talent ($250K–$300K), a Director People Business Partner at Ladders ($226K–$335K), a Senior Director HR at La Pecora Bianca ($180K–$220K), and more. You also sent yourself two LinkedIn job links last night — review and act today.</span>
      </div>
    </div>
    <div class="exec-bullet">
      <div class="exec-bullet-icon">🔵</div>
      <div class="exec-bullet-text">
        <strong>Biggest Calendar Item: HR Networking &amp; Job Search Group Zoom — TODAY 12:00–1:30 PM (RSVP Pending)</strong>
        <span>You have not yet responded to the HR Networking &amp; Job Search Group Zoom happening in just a few hours. Your personal "Network" block is also confirmed for the same timeslot. Additionally, a COBRA payment reminder is due Saturday, June 27. The Executive Roundtable tomorrow has been declined — confirm that was intentional.</span>
      </div>
    </div>
  </div>
</div>

<!-- ============================================================ ACTION REQUIRED ============================================================ -->
<div class="section red">
  <div class="section-title">🚨 Action Required</div>
  <div class="section-body">

    <div class="card card-red">
      <div class="card-title">🔴 PHISHING ALERT — Fake "Cloud_Support" Payment Email</div>
      <div class="card-meta">From: Cloud_Support© &lt;upilhopexhgijz.08934630851130@suy6jc.lp0p8r.ri2jdi.us&gt; | Jun 24, 2026</div>
      <div class="card-body">Claims your cloud storage subscription had a payment issue and photos/videos will be deleted. Sender domain is completely fraudulent. This is a phishing scam designed to steal payment info or login credentials.</div>
      <div class="card-action">⚡ Next Step: Do NOT click any links. Report as phishing in Gmail. Delete immediately. Do not enter any payment info.</div>
    </div>

    <div class="card card-red">
      <div class="card-title">🔴 PHISHING ALERT — Spoofed as Your Own Email Address ("melissaw212")</div>
      <div class="card-meta">From: melissaw212 &lt;pilezjugsmg@wkalslhzsdadew.qss3917.a3917.sgjy.uk.com&gt; | Jun 23, 2026</div>
      <div class="card-body">Email spoofed to appear as if it came from your own account. Claims your "Cloud ID has been locked" and photos will be removed. Classic spoofing + social engineering attack. The sending domain is completely fabricated.</div>
      <div class="card-action">⚡ Next Step: Report as phishing. Delete. Consider enabling Google's Advanced Protection Program if not already active. Due: Today.</div>
    </div>

    <div class="card card-red">
      <div class="card-title">🔴 SCAM — Fake Casino Payment Confirmation ($3,000 USD)</div>
      <div class="card-meta">From: 'melissaw212' &lt;pcyjsupportcxes@dlyobxeujiaodpxkcghrystp.com&gt; | Jun 23, 2026</div>
      <div class="card-body">Claims you received a $3,000.00 USD casino payment and asks you to "confirm your info." This is a scam designed to steal personal/financial information. The sender domain is completely fake.</div>
      <div class="card-action">⚡ Next Step: Do NOT engage. Report as phishing. Delete immediately. Due: Today.</div>
    </div>

    <div class="card card-red">
      <div class="card-title">🔴 EXPLICIT SPAM — Highly Inappropriate Content in Email</div>
      <div class="card-meta">From: 🔶FUCK-BUDDY SECRET🔶 &lt;mrsjdwcvkslhtn.74985135957959@9i5wgl.x2x0b9.fp3qol.us&gt; | Jun 24, 2026</div>
      <div class="card-body">Explicit adult spam with offensive content. Fraudulent sender domain. No action needed other than deletion.</div>
      <div class="card-action">⚡ Next Step: Mark as spam, block sender, delete. Due: Today.</div>
    </div>

    <div class="card card-yellow">
      <div class="card-title">🟡 RSVP NEEDED — HR Networking &amp; Job Search Group Zoom (TODAY)</div>
      <div class="card-meta">Calendar Event | Today, June 24 | 12:00–1:30 PM ET | Status: Needs Action</div>
      <div class="card-body">You have not yet responded to this group Zoom meeting. Over 150 attendees are on the list. Your personal "Network" block is confirmed at the same time — these appear to be the same event.</div>
      <div class="card-action">⚡ Next Step: Accept or confirm attendance. Join via Zoom link: https://us06web.zoom.us/j/81954171722 | Due: Before 12:00 PM today.</div>
    </div>

    <div class="card card-yellow">
      <div class="card-title">🟡 BANKING — Direct Deposit Received: $267.09 from U.S. Government</div>
      <div class="card-meta">From: Bank of America | Jun 24, 2026 | Account ending in 7471</div>
      <div class="card-body">A direct deposit of $267.09 was credited to your personal checking/savings account (ending 7471) from "UNITED STATES" — likely a government payment (SSA, unemployment, tax refund, or similar). Verify source is expected.</div>
      <div class="card-action">⚡ Next Step: Log in to Bank of America to confirm deposit source and that it matches expected amount. Due: Today.</div>
    </div>

    <div class="card card-yellow">
      <div class="card-title">🟡 HEALTH INSURANCE — New UnitedHealthcare Health Statement Available</div>
      <div class="card-meta">From: UnitedHealthcare | Jun 23, 2026 | Already Read</div>
      <div class="card-body">A new health statement has been issued. Given your upcoming COBRA payment reminder (Jun 27), it's important to review this document for coverage accuracy and payment amounts.</div>
      <div class="card-action">⚡ Next Step: Log in to UHC portal and review statement. Cross-reference with COBRA payment due Saturday. Due: Before Jun 27.</div>
    </div>

    <div class="card card-yellow">
      <div class="card-title">🟡 COBRA PAYMENT REMINDER — Calendar Reminder Set for Saturday June 27</div>
      <div class="card-meta">Calendar Event | Saturday, June 27 | 10:00–11:00 AM</div>
      <div class="card-body">You have a self-created reminder to check COBRA payments this Saturday. This should be reviewed in conjunction with the UnitedHealthcare statement received today.</div>
      <div class="card-action">⚡ Next Step: Prepare payment now so you're not rushed Saturday. Confirm COBRA amount against new health statement. Due: Jun 27.</div>
    </div>

    <div class="card card-yellow">
      <div class="card-title">🟡 CLASS ACTION SETTLEMENT — Biddle v. Walt Disney Company (YouTube TV / DirecTV Stream)</div>
      <div class="card-meta">From: Settlement Administrator &lt;OnlineTVSettlement@e.epiqnotice.com&gt; | Jun 23, 2026</div>
      <div class="card-body">Court-ordered notice. If you purchased YouTube TV or DirecTV Stream from April 1, 2019 through March 31, 2026, you may be entitled to a cash payment. This appears to be a legitimate class action settlement notice from Epiq — a known legal notification administrator.</div>
      <div class="card-action">⚡ Next Step: Review the notice carefully. Verify legitimacy at epiqnotice.com directly. File a claim if eligible. Check for submission deadline. Due: Check email for deadline.</div>
    </div>

    <div class="card card-green">
      <div class="card-title">🟢 REVIEW JOBS — You Emailed Yourself 2 LinkedIn Job Links Last Night</div>
      <div class="card-meta">From: Melissa W &lt;melissaw212@gmail.com&gt; | Jun 23, 2026 ~10:09 PM ET</div>
      <div class="card-body">You sent yourself two LinkedIn job listing URLs (Job IDs: 4419211398 and 4419204351) — strong signal you considered these important. Both are unread in inbox.</div>
      <div class="card-action">⚡ Next Step: Open both LinkedIn links, review job descriptions, assess fit, and add to your job pipeline or apply today. Due: Today.</div>
    </div>

    <div class="card card-blue">
      <div class="card-title">🔵 CONFIRM/REVIEW — Executive Roundtable (DECLINED) — Tomorrow, Jun 25</div>
      <div class="card-meta">Calendar Event | Thursday, June 25 | 9:00–10:30 AM | Hosted by John Madigan via Zoom</div>
      <div class="card-body">You have declined this Executive Roundtable. This may be a valuable networking opportunity for an HR executive in job search mode. Confirm that declining was intentional.</div>
      <div class="card-action">⚡ Next Step: Confirm the decline was intentional. If not, re-accept via calendar. Due: Today (before tomorrow morning).</div>
    </div>

    <div class="card card-blue">
      <div class="card-title">🔵 RSVP NEEDED — HR Networking Open Office Hours (TOMORROW, Jun 25)</div>
      <div class="card-meta">Calendar Event | Thursday, June 25 | 12:00–1:00 PM | Status: Needs Action</div>
      <div class="card-body">Another HR networking Zoom session tomorrow also shows "Needs Action" — RSVP is pending. Over 150 attendees invited.</div>
      <div class="card-action">⚡ Next Step: Accept or decline via Google Calendar. Due: Today.</div>
    </div>

    <div class="card card-green">
      <div class="card-title">🟢 JOB OPPORTUNITY — LinkedIn Message from Dr. Craig Beach (MOVED TO TRASH)</div>
      <div class="card-meta">From: Dr. Craig Beach via LinkedIn | Jun 24, 2026 | Currently in Trash</div>
      <div class="card-body">A LinkedIn message notification was routed to trash. Given your active job search, messages from professional contacts should be reviewed — this could be a recruiter or networking contact.</div>
      <div class="card-action">⚡ Next Step: Restore from trash. Read the LinkedIn message. Respond if relevant. Due: Today.</div>
    </div>

  </div>
</div>

<!-- ============================================================ FULL 7-DAY CALENDAR ============================================================ -->
<div class="section blue">
  <div class="section-title">📅 Full 7-Day Calendar — June 24–30, 2026</div>
  <div class="section-body">

    <!-- Wednesday June 24 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Wednesday, June 24, 2026 — TODAY</div>

      <div class="cal-event status-needs">
        <div class="cal-time">12:00 PM – 1:30 PM ET</div>
        <div class="cal-title">HR Networking &amp; Job Search Group – Zoom 2</div>
        <div class="cal-detail"><strong>RSVP Status:</strong> <span class="badge badge-yellow">Needs Action</span> &nbsp; <strong>Location:</strong> <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a></div>
        <div class="cal-detail"><strong>Attendees:</strong> 150+ HR professionals and job seekers</div>
        <div class="cal-detail"><strong>Description:</strong> Group HR networking and job search session. Team guidelines and resources referenced in invite.</div>
        <div class="cal-detail"><strong>Prep Needed:</strong> Review team guidelines linked in invite description. Prepare a brief intro/update on your job search. Have resume ready.</div>
        <div class="cal-warn">⚠️ RSVP PENDING — Respond before 12:00 PM today. Conflict: overlaps with "Network" block below (same event).</div>
      </div>

      <div class="cal-event status-confirmed">
        <div class="cal-time">12:00 PM – 1:30 PM ET</div>
        <div class="cal-title">Network (Personal Block)</div>
        <div class="cal-detail"><strong>RSVP Status:</strong> <span class="badge badge-green">Confirmed</span> &nbsp; <strong>Location:</strong> No location set</div>
        <div class="cal-detail"><strong>Attendees:</strong> None listed (personal block)</div>
        <div class="cal-detail"><strong>Prep Needed:</strong> This is your confirmed personal networking time block — likely mirrors the HR Networking Zoom above.</div>
        <div class="cal-warn">⚠️ CONFLICT: Both events overlap at 12:00–1:30 PM. These appear to be the same activity. Confirm and consolidate.</div>
      </div>
    </div>

    <!-- Thursday June 25 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Thursday, June 25, 2026</div>

      <div class="cal-event status-declined">
        <div class="cal-time">9:00 AM – 10:30 AM ET</div>
        <div class="cal-title">Executive Roundtable (Hosted by John Madigan)</div>
        <div class="cal-detail"><strong>RSVP Status:</strong> <span class="badge badge-red">Declined</span> &nbsp; <strong>Location:</strong> <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a></div>
        <div class="cal-detail"><strong>Meeting ID:</strong> 207 786 667 &nbsp; | &nbsp; <strong>Password:</strong> 205454</div>
        <div class="cal-detail"><strong>Prep Needed:</strong> None required if declining is intentional.</div>
        <div class="cal-warn">⚠️ You have DECLINED this event. As a senior HR executive in active job search, executive roundtables are high-value networking. Confirm this decline was intentional — consider reversing if possible.</div>
      </div>

      <div class="cal-event status-needs">
        <div class="cal-time">12:00 PM – 1:00 PM ET</div>
        <div class="cal-title">HR Networking &amp; Job Search: Open Office Hours – Zoom 2</div>
        <div class="cal-detail"><strong>RSVP Status:</strong> <span class="badge badge-yellow">Needs Action</span> &nbsp; <strong>Location:</strong> <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a></div>
        <div class="cal-detail"><strong>Attendees:</strong> 150+ HR professionals</div>
        <div class="cal-detail"><strong>Description:</strong> Open office hours format — open discussion, no recording. Note: AI notetaking tools should be turned off per organizer instructions.</div>
        <div class="cal-detail"><strong>Prep Needed:</strong> Bring 1–2 specific job search questions. Prepare elevator pitch. Disable any AI note-taking tools (Otter, Fireflies, etc.) per organizer request.</div>
        <div class="cal-warn">⚠️ RSVP PENDING — Respond today.</div>
      </div>
    </div>

    <!-- Friday June 26 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Friday, June 26, 2026</div>
      <div class="cal-event">
        <div class="cal-title">No Events Scheduled</div>
        <div class="cal-detail" style="color:#888;">Calendar is clear for Friday. Suggested use: job applications, follow-ups, and LinkedIn outreach based on today's job leads.</div>
      </div>
    </div>

    <!-- Saturday June 27 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Saturday, June 27, 2026</div>
      <div class="cal-event status-confirmed">
        <div class="cal-time">10:00 AM – 11:00 AM ET</div>
        <div class="cal-title">Check COBRA Payments</div>
        <div class="cal-detail"><strong>RSVP Status:</strong> <span class="badge badge-green">Confirmed (Personal Reminder)</span></div>
        <div class="cal-detail"><strong>Prep Needed:</strong> Log in to COBRA portal. Cross-reference with new UnitedHealthcare health statement received June 23. Confirm payment amount and due date. Process payment if needed.</div>
        <div class="cal-warn">⚠️ Health insurance coverage continuity depends on timely COBRA payment. Do not skip this task.</div>
      </div>
    </div>

    <!-- Sunday June 28 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Sunday, June 28, 2026</div>
      <div class="cal-event">
        <div class="cal-title">No Events Scheduled</div>
        <div class="cal-detail" style="color:#888;">Calendar is clear. Suggested: rest, review class action settlement deadline, and prep for the week ahead.</div>
      </div>
    </div>

    <!-- Monday June 29 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Monday, June 29, 2026</div>
      <div class="cal-event">
        <div class="cal-title">No Events Scheduled</div>
        <div class="cal-detail" style="color:#888;">Calendar is clear. Suggested: follow up on any job applications submitted this week. Check for recruiter responses.</div>
      </div>
    </div>

    <!-- Tuesday June 30 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Tuesday, June 30, 2026</div>
      <div class="cal-event">
        <div class="cal-title">No Events Scheduled</div>
        <div class="cal-detail" style="color:#888;">Calendar is clear. End of month — good day to review job search pipeline progress and set July goals.</div>
      </div>
    </div>

  </div>
</div>

<!-- ============================================================ JOB SEARCH & INTERVIEW PIPELINE ============================================================ -->
<div class="section green">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">

    <table>
      <thead>
        <tr>
          <th>Fit</th>
          <th>Role</th>
          <th>Company</th>
          <th>Salary</th>
          <th>Source</th>
          <th>Status</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="badge badge-high">HIGH</span></td>
          <td>Chief Human Resources Officer (CHRO)</td>
          <td>Empathy Talent (Private Equity / Investment Mgmt)</td>
          <td>$250K–$300K/yr</td>
          <td>LinkedIn Job Alert</td>
          <td>🟡 New Lead</td>
          <td>Apply Today</td>
        </tr>
        <tr>
          <td><span class="badge badge-high">HIGH</span></td>
          <td>Director, People Business Partner</td>
          <td>Ladders</td>
          <td>$226K–$335K/yr</td>
          <td>LinkedIn (×3 alerts) + Indeed</td>
          <td>🟡 New Lead (Repeated)</td>
          <td>Apply Today — High urgency (sent 3 times)</td>
        </tr>
        <tr>
          <td><span class="badge badge-high">HIGH</span></td>
          <td>Senior Director, Human Resources</td>
          <td>La Pecora Bianca</td>
          <td>$180K–$220K/yr</td>
          <td>Indeed</td>
          <td>🟡 New Lead</td>
          <td>Review &amp; Apply</td>
        </tr>
        <tr>
          <td><span class="badge badge-medium">MED</span></td>
          <td>Senior Director of Human Resources</td>
          <td>The Max Foundation (Remote)</td>
          <td>Not stated</td>
          <td>Glassdoor (in Trash)</td>
          <td>🔴 In Trash — Needs Restore</td>
          <td>Restore from Trash, Review</td>
        </tr>
        <tr>
          <td><span class="badge badge-medium">MED</span></td>
          <td>Talent Strategy Lead</td>
          <td>Forus</td>
          <td>$170K–$250K/yr</td>
          <td>LinkedIn Job Alert</td>
          <td>🟡 New Lead</td>
          <td>Review Role &amp; Apply</td>
        </tr>
        <tr>
          <td><span class="badge badge-medium">MED</span></td>
          <td>Project Manager, Retail Network Transformation</td>
          <td>Citizens Bank</td>
          <td>Not stated</td>
          <td>Citizens Careers Email</td>
          <td>🟡 New Lead</td>
          <td>Review — may be lower fit given HR focus</td>
        </tr>
        <tr>
          <td><span class="badge badge-medium">MED</span></td>
          <td>Unknown (Self-Sent Link #1)</td>
          <td>Unknown</td>
          <td>Not stated</td>
          <td>Self-email (LinkedIn Job ID: 4419211398)</td>
          <td>🟡 Unreviewed</td>
          <td>Open link, assess, add to pipeline</td>
        </tr>
        <tr>
          <td><span class="badge badge-medium">MED</span></td>
          <td>Unknown (Self-Sent Link #2)</td>
          <td>Unknown</td>
          <td>Not stated</td>
          <td>Self-email (LinkedIn Job ID: 4419204351)</td>
          <td>🟡 Unreviewed</td>
          <td>Open link, assess, add to pipeline</td>
        </tr>
      </tbody>
    </table>

    <div style="margin-top:16px;">
      <div class="card card-blue">
        <div class="card-title">🔵 LinkedIn Activity — You're Being Noticed</div>
        <div class="card-body">LinkedIn reports 1 person viewed your profile (unread notification), 4 people noticed you (in trash — restore), and 2 new connection invitations are waiting. Your profile is generating recruiter interest — respond promptly to maintain momentum.</div>
        <div class="card-action">⚡ Action: Accept pending connection requests. Review who viewed your profile. Respond to Dr. Craig Beach's LinkedIn message (currently in trash).</div>
      </div>
      <div class="card card-green">
        <div class="card-title">🟢 HR Networking &amp; Job Search Group — TODAY 12:00–1:30 PM</div>
        <div class="card-body">Active participation in this group is a direct job search accelerator. 150+ peers in similar roles. Bring your current target companies, salary range, and ask for warm introductions.</div>
        <div class="card-action">⚡ Action: Attend today's Zoom. Prepare 60-second job search update. Ask the group for referrals at your target companies.</div>
      </div>
    </div>

  </div>
</div>

<!-- ============================================================ FULL EMAIL REVIEW BY CATEGORY ============================================================ -->
<div class="section dark">
  <div class="section-title">📬 Full Email Review by Category</div>
  <div class="section-body">

    <!-- Security / Risk -->
    <div class="card card-red">
      <div class="card-title"><span class="badge badge-red">Security / Risk</span> &nbsp; 4 Emails</div>
      <div class="card-meta">Senders: Cloud_Support©, melissaw212 (spoofed), 🔶FUCK-BUDDY SECRET🔶, Memory.Decline (fake Harvard/UCLA)</div>
      <div class="card-body">
        <ul class="email-list">
          <li><span class="tag-from">Cloud_Support©</span> — <span class="tag-subj">"Cloud sync disabled due to Payment issue!!"</span> — PHISHING. Not in inbox/trash — filtered by Gmail.</li>
          <li><span class="tag-from">melissaw212 (spoofed)</span> — <span class="tag-subj">"Your Cloud ID has been locked"</span> — PHISHING/SPOOFING. Filtered by Gmail.</li>
          <li><span class="tag-from">🔶FUCK-BUDDY SECRET🔶</span> — <span class="tag-subj">Explicit spam</span> — EXPLICIT SPAM/SCAM. Filtered by Gmail.</li>
          <li><span class="tag-from">Memory.Decline</span> — <span class="tag-subj">"Harvard &amp; UCLA Reveal #1 Best Fruit for Improving Memory"</span> — SCAM/SPAM. Fake domain. Filtered by Gmail.</li>
        </ul>
      </div>
      <div class="card-action">✅ Action: Mark all as phishing. Delete. Block sender domains. Verify no credentials were entered. Review Google Account security settings.</div>
    </div>

    <!-- Job Search -->
    <div class="card card-green">
      <div class="card-title"><span class="badge badge-green">Job Search</span> &nbsp; 8 Emails</div>
      <div class="card-meta">Senders: LinkedIn Job Alerts (×4), Indeed, Glassdoor, Citizens Careers, Melissa W (self-sent ×2)</div>
      <div class="card-body">
        <ul class="email-list">
          <li><span class="tag-from">LinkedIn Job Alerts</span> — Director, People Business Partner at Ladders ($226K–$335K) — <em>sent 3 times (9:05 AM, 7:05 AM, 5:05 AM, 1:05 AM — 3 unique + 1 in trash)</em></li>
          <li><span class="tag-from">LinkedIn Job Alerts</span> — CHRO at Empathy Talent ($250K–$300K)</li>
          <li><span class="tag-from">LinkedIn Job Alerts</span> — Talent Strategy Lead at Forus ($170K–$250K)</li>
          <li><span class="tag-from">Indeed</span> — Senior Director, Human Resources at La Pecora Bianca ($180K–$220K)</li>
          <li><span class="tag-from">Glassdoor</span> — Senior Director HR at The Max Foundation + 5 more (in Trash)</li>
          <li><span class="tag-from">Citizens Careers</span> — Project Manager, Retail Network Transformation and other roles</li>
          <li><span class="tag-from">Melissa W (self)</span> — LinkedIn Job ID 4419211398 (no subject)</li>
          <li><span class="tag-from">Melissa W (self)</span> — LinkedIn Job ID 4419204351 (subject: "Job")</li>
        </ul>
      </div>
      <div class="card-action">✅ Action: Review all opportunities today. Prioritize CHRO and Director PBP roles. Apply to top 3 immediately.</div>
    </div>

    <!-- Recruiters / Networking -->
    <div class="card card-blue">
      <div class="card-title"><span class="badge badge-blue">Recruiters / Networking</span> &nbsp; 4 Emails</div>
      <div class="card-meta">Senders: Dr. Craig Beach (LinkedIn), LinkedIn profile views (×2), LinkedIn connection invites</div>
      <div class="card-body">
        <ul class="email-list">
          <li><span class="tag-from">Dr. Craig Beach via LinkedIn</span> — "Dr. Craig just messaged you" — 1 new message — IN TRASH (restore immediately)</li>
          <li><span class="tag-from">LinkedIn</span> — "1 person noticed you" — Profile view notification</li>
          <li><span class="tag-from">LinkedIn</span> — "4 people noticed you" — IN TRASH (restore)</li>
          <li><span class="tag-from">LinkedIn</span> — "You have 2 new invitations" — IN TRASH (restore)</li>
        </ul>
      </div>
      <div class="card-action">✅ Action: Restore Dr. Craig Beach message from trash immediately. Restore LinkedIn notifications. Accept relevant connection requests. Respond to messages today.</div>
    </div>

    <!-- Calendar / Events -->
    <div class="card card-blue">
      <div class="card-title"><span class="badge badge-blue">Calendar / Events</span> &nbsp; 1 Email</div>
      <div class="card-meta">Sender: AllEvents</div>
      <div class="card-body">
        <ul class="email-list">
          <li><span class="tag-from">AllEvents</span> — "Events for Melissa, new recommendations" — Local/personal event suggestions based on interests</li>
        </ul>
      </div>
      <div class="card-action">✅ Action: Low priority. Review if time permits. Consider unsubscribing if not finding value.</div>
    </div>

    <!-- Medical / Health -->
    <div class="card card-yellow">
      <div class="card-title"><span class="badge badge-yellow">Medical / Health</span> &nbsp; 1 Email</div>
      <div class="card-meta">Sender: UnitedHealthcare Notifications</div>
      <div class="card-body">
        <ul class="email-list">
          <li><span class="tag-from">UnitedHealthcare</span> — "Here's your new Health Statement from UnitedHealthcare" — Already read. New statement issued. Important given COBRA review due Jun 27.</li>
        </ul>
      </div>
      <div class="card-action">✅ Action: Log in to UHC portal, review statement before Saturday's COBRA payment check.</div>
    </div>

    <!-- Financial / Billing -->
    <div class="card card-yellow">
      <div class="card-title"><span class="badge badge-yellow">Financial / Billing</span> &nbsp; 2 Emails</div>
      <div class="card-meta">Senders: Bank of America, Settlement Administrator</div>
      <div class="card-body">
        <ul class="email-list">
          <li><span class="tag-from">Bank of America</span> — "A direct deposit was credited to your account" — $267.09 from U.S. government to account ending 7471</li>
          <li><span class="tag-from">Settlement Administrator</span> — "Biddle v. The Walt Disney Company" — Class action settlement notice (YouTube TV / DirecTV Stream). Potential cash payment if eligible.</li>
        </ul>
      </div>
      <div class="card-action">✅ Action: Verify BofA deposit source. Review Disney settlement notice and file claim if eligible before deadline.</div>
    </div>

    <!-- Professional Development -->
    <div class="card card-purple">
      <div class="card-title"><span class="badge badge-purple">Professional Development</span> &nbsp; 3 Emails</div>
      <div class="card-meta">Senders: Ruben Hassid (Substack, ×2 — one in trash), Alison Courses (in trash), Melissa W (LinkedIn post — self-sent)</div>
      <div class="card-body">
        <ul class="email-list">
          <li><span class="tag-from">Ruben Hassid (Substack)</span> — "Why AI Will Fail." — In inbox. AI/tech thought leadership newsletter.</li>
          <li><span class="tag-from">Ruben Hassid (Substack)</span> — "AI will fail." — IN TRASH. Duplicate send.</li>
          <li><span class="tag-from">Alison Courses</span> — "Soft skills can take you further than you think!" — IN TRASH. Online learning platform.</li>
          <li><span class="tag-from">Melissa W (self)</span> — LinkedIn post link about Claude AI tutorials — self-sent for reference</li>
        </ul>
      </div>
      <div class="card-action">✅ Action: Read Ruben Hassid newsletter if relevant to your AI knowledge for HR. Review Claude/AI tutorial post when time permits. Alison Courses in trash — safe to delete if not enrolled.</div>
    </div>

    <!-- Personal -->
    <div class="card card-gray">
      <div class="card-title"><span class="badge badge-gray">Personal</span> &nbsp; 3 Emails</div>
      <div class="card-meta">Senders: Match.com (×2), Melissa W (self — Instagram links ×2)</div>
      <div class="card-body">
        <ul class="email-list">
          <li><span class="tag-from">Match</span> — "Louis likes you. See if it's mutual." — Dating app notification</li>
          <li><span class="tag-from">Match</span> — "Michael likes you. See if it's mutual." — Dating app notification</li>
          <li><span class="tag-from">Melissa W (self)</span> — Instagram post link (DZ7hHUjmGhf) — saved for reference</li>
          <li><span class="tag-from">Melissa W (self)</span> — Instagram post link (DZqBu3pDZMd) — saved for reference</li>
        </ul>
        <p class="note">Note: 2 self-sent Instagram links counted here; 2 self-sent LinkedIn job links counted under Job Search.</p>
      </div>
      <div class="card-action">✅ Action: Personal — address at your leisure. Consider if Match notifications need to go to a separate folder.</div>
    </div>

    <!-- Newsletters / Subscriptions -->
    <div class="card card-purple">
      <div class="card-title"><span class="badge badge-purple">Newsletters / Subscriptions</span> &nbsp; 3 Emails</div>
      <div class="card-meta">Senders: Brevo, Knock Every Door (in trash), Google Terms Update (in trash)</div>
      <div class="card-body">
        <ul class="email-list">
          <li><span class="tag-from">Brevo</span> — "Let Brevo do the heavy lifting" — Marketing platform welcome/onboarding email</li>
          <li><span class="tag-from">Knock Every Door</span> — Political newsletter — IN TRASH</li>
          <li><span class="tag-from">Google</span> — "Learn more about our updated Terms of Service" — IN TRASH. Legitimate Google TOS update notice.</li>
        </ul>
      </div>
      <div class="card-action">✅ Action: If using Brevo for job search marketing, review. Otherwise unsubscribe. Google TOS notice — restore from trash and acknowledge. Political newsletter — safe to delete.</div>
    </div>

    <!-- Promotional / Retail -->
    <div class="card card-gray">
      <div class="card-title"><span class="badge badge-gray">Promotional / Retail</span> &nbsp; 12 Emails</div>
      <div class="card-meta">Senders: Kohl's, SHEIN (×2), Gap Factory, Old Navy (trash), Temu (×2), YesStyle, Netflix (trash), 22 Words (trash), Apify Community (trash)</div>
      <div class="card-body">See full Promotional / Retail Summary section below.</div>
      <div class="card-action">✅ Action: Group and archive or delete. Low priority for executive review.</div>
    </div>

    <!-- Trash Review -->
    <div class="card card-red">
      <div class="card-title"><span class="badge badge-red">Trash Review</span> &nbsp; 14 Emails</div>
      <div class="card-meta">See dedicated Trash Review section below for full breakdown.</div>
      <div class="card-body">Emails currently in Gmail Trash reviewed and categorized into: Restore, Review Before Deleting, and Safe to Delete.</div>
      <div class="card-action">✅ Action: See Trash Review section for specific recommendations.</div>
    </div>

    <!-- Safe to Delete / Ignore -->
    <div class="card card-gray">
      <div class="card-title"><span class="badge badge-gray">Safe to Delete / Ignore</span> &nbsp; 5 Emails</div>
      <div class="card-meta">Senders: GLP-1 spam, LinkedIn (Dennis/Andrew Messerle — misdirected), Nextdoor (trash), SPCA (trash), Temu (not in inbox)</div>
      <div class="card-body">
        <ul class="email-list">
          <li><span class="tag-from">GLP-1-by-DirectMeds</span> — "DirectMeds GLP-1 treatment helps you lose up to 40 lbs" — Spam/unsolicited medical ad. Fake domain.</li>
          <li><span class="tag-from">LinkedIn</span> — "Dennis, add Andrew Messerle - Summer Intern" — Appears to be misdirected/sent to wrong person. Low relevance.</li>
          <li><span class="tag-from">Nextdoor</span> — "Hi!" — In Trash. Standard neighborhood notification.</li>
          <li><span class="tag-from">SPCA International</span> — "Dog Tortured and Burned" — In Trash. Charity solicitation with graphic subject line.</li>
          <li><span class="tag-from">Temu</span> — "midi dress is calling" — Not in inbox or trash (likely filtered). Shopping promo.</li>
        </ul>
      </div>
      <div class="card-action">✅ Action: Delete all. Unsubscribe from any legitimate senders to reduce inbox noise.</div>
    </div>

  </div>
</div>

<!-- ============================================================ TRASH REVIEW ============================================================ -->
<div class="section red">
  <div class="section-title">🗑️ Trash Review — 14 Emails in Gmail Trash</div>
  <div class="section-body">

    <div class="card card-green">
      <div class="card-title">✅ RESTORE IMMEDIATELY — 4 Emails</div>
      <div class="card-body">
        <table>
          <thead>
            <tr><th>Sender</th><th>Subject</th><th>Why Restore</th></tr>
          </thead>
          <tbody>
            <tr>
              <td>Dr. Craig Beach via LinkedIn</td>
              <td>"Dr. Craig just messaged you"</td>
              <td>Professional LinkedIn message — potential recruiter or networking contact. Critical for active job search. Respond immediately.</td>
            </tr>
            <tr>
              <td>Glassdoor Jobs</td>
              <td>"Senior Director of Human Resources at The Max Foundation and 5 more jobs..."</td>
              <td>Active job leads — Senior Director HR roles directly relevant to Melissa's search. Should be in inbox, not trash.</td>
            </tr>
            <tr>
              <td>LinkedIn</td>
              <td>"4 people noticed you"</td>
              <td>Profile views from potentially interested recruiters/employers. Should be reviewed as part of job search strategy.</td>
            </tr>
            <tr>
              <td>LinkedIn</td>
              <td>"You have 2 new invitations"</td>
              <td>Pending LinkedIn connection requests from professionals who sought Melissa out. Accept to expand network during job search.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="card card-yellow">
      <div class="card-title">🔍 REVIEW BEFORE DELETING — 4 Emails</div>
      <div class="card-body">
        <table>
          <thead>
            <tr><th>Sender</th><th>Subject</th><th>Why Review</th></tr>
          </thead>
          <tbody>
            <tr>
              <td>Google</td>
              <td>"Learn more about our updated Terms of Service"</td>
              <td>Legitimate Google TOS update for stellbell212@hotmail.com. Effective date not stated — check if action is required before changes take effect.</td>
            </tr>
            <tr>
              <td>LinkedIn Job Alerts</td>
              <td>"Director, People Business Partner at Ladders: up to $335K/year"</td>
              <td>This is an active, high-value job lead — should NOT be in trash. Same role appearing in inbox multiple times. Already acted on? Confirm application status.</td>
            </tr>
            <tr>
              <td>Ruben Hassid (Substack)</td>
              <td>"AI will fail." (duplicate)</td>
              <td>Duplicate of inbox version. Safe to delete once inbox version is read.</td>
            </tr>
            <tr>
              <td>Alison Courses</td>
              <td>"Soft skills can take you further than you think!"</td>
              <td>Online learning platform — if enrolled, restore. If not enrolled/interested, safe to delete and unsubscribe.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="card card-gray">
      <div class="card-title">🗑️ SAFE TO DELETE — 6 Emails</div>
      <div class="card-body">
        <table>
          <thead>
            <tr><th>Sender</th><th>Subject</th><th>Reason</th></tr>
          </thead>
          <tbody>
            <tr>
              <td>Knock Every Door</td>
              <td>"That is unacceptable, that's treasonous..."</td>
              <td>Political advocacy newsletter. Correctly moved to trash. Safe to permanently delete and unsubscribe.</td>
            </tr>
            <tr>
              <td>Netflix</td>
              <td>"Here's what's leaving Netflix soon"</td>
              <td>Promotional entertainment notification. No action needed.</td>
            </tr>
            <tr>
              <td>Old Navy</td>
              <td>"Make it count! You still have 50% OFF everything"</td>
              <td>Retail promotion. Low priority. Safe to delete.</td>
            </tr>
            <tr>
              <td>Nextdoor</td>
              <td>"Hi!" — Trending neighborhood posts</td>
              <td>Neighborhood notification. No urgent relevance. Safe to delete.</td>
            </tr>
            <tr>
              <td>SPCA International</td>
              <td>"Dog Tortured and Burned"</td>
              <td>Charity donation solicitation with graphic subject. Safe to delete if not donating. Unsubscribe to avoid future distressing subjects.</td>
            </tr>
            <tr>
              <td>Apify Community</td>
              <td>"Reintroducing: Google Hotels Search Scraper"</td>
              <td>Developer tool notification. Not relevant unless actively using Apify for web scraping. Safe to delete.</td>
            </tr>
            <tr>
              <td>22 Words</td>
              <td>"⚡ Your Amazon Prime Lightning Deals"</td>
              <td>Deal aggregator promotional email. Safe to delete.</td>
            </tr>
            <tr>
              <td>SHEIN</td>
              <td>"Looks Better in the Sun 🏖️"</td>
              <td>Retail promotional email. Safe to delete.</td>
            </tr>
          </tbody>
        </table>
        <p class="note">Note: 22 Words, SHEIN (trash), and Nextdoor bring trash count to 14 including both SHEIN trash and Old Navy trash emails.</p>
      </div>
    </div>

  </div>
</div>

<!-- ============================================================ PROMOTIONAL / RETAIL SUMMARY ============================================================ -->
<div class="section gray">
  <div class="section-title">🛍️ Promotional / Retail Summary</div>
  <div class="section-body">
    <table>
      <thead>
        <tr>
          <th>Brand / Sender</th>
          <th>Count</th>
          <th>Subject / Theme</th>
          <th>Location</th>
          <th>Recommendation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Kohl's</td>
          <td>1</td>
          <td>Kohl's Deal Days — new deals daily + Kohl's Cash + free shipping</td>
          <td>Inbox</td>
          <td><span class="badge badge-gray">Review / Delete</span></td>
        </tr>
        <tr>
          <td>SHEIN</td>
          <td>2</td>
          <td>"New Sportswear Arrivals" (inbox) | "Looks Better in the Sun" (trash)</td>
          <td>Inbox + Trash</td>
          <td><span class="badge badge-gray">Delete Both</span></td>
        </tr>
        <tr>
          <td>Gap Factory</td>
          <td>1</td>
          <td>50% OFF Dresses, Skirts &amp; Pants + extra 15% off + free shipping</td>
          <td>Inbox
<hr>
<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Financial / Billing</td><td>2</td></tr>
<tr><td>Job Search / Recruiters</td><td>17</td></tr>
<tr><td>Medical / Health</td><td>2</td></tr>
<tr><td>Other / Review</td><td>17</td></tr>
<tr><td>Professional Development / Newsletters</td><td>4</td></tr>
<tr><td>Promotional / Retail</td><td>1</td></tr>
<tr><td>Security / Risk</td><td>7</td></tr>
</table>
<p><strong>Audit Note:</strong> Every fetched email was reviewed and assigned to one category. Trash emails were included in review. Promotional and low-value emails were accounted for but deprioritized.</p>

