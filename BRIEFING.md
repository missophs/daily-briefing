<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing – Melissa Weiss | June 16, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 15px; color: #a0b4d0; margin-top: 4px; }
  .header-meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header-meta-item { background: rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 18px; }
  .header-meta-item .label { font-size: 11px; color: #90a8c0; text-transform: uppercase; letter-spacing: 1px; }
  .header-meta-item .value { font-size: 20px; font-weight: 700; color: #fff; }

  /* SECTION HEADERS */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; padding: 8px 16px; border-radius: 6px 6px 0 0; margin-bottom: 0; }
  .section-body { border-radius: 0 0 10px 10px; padding: 18px; }
  .section-wrap { border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 24px; }

  /* COLOR THEMES */
  .red-theme .section-title { background: #c0392b; color: #fff; }
  .red-theme .section-body { background: #fff5f5; border: 1.5px solid #e8b4b8; border-top: none; }
  .yellow-theme .section-title { background: #d4a017; color: #fff; }
  .yellow-theme .section-body { background: #fffef0; border: 1.5px solid #f0d060; border-top: none; }
  .blue-theme .section-title { background: #1565c0; color: #fff; }
  .blue-theme .section-body { background: #f0f6ff; border: 1.5px solid #90caf9; border-top: none; }
  .green-theme .section-title { background: #2e7d32; color: #fff; }
  .green-theme .section-body { background: #f1fdf2; border: 1.5px solid #a5d6a7; border-top: none; }
  .purple-theme .section-title { background: #6a1b9a; color: #fff; }
  .purple-theme .section-body { background: #faf0ff; border: 1.5px solid #ce93d8; border-top: none; }
  .gray-theme .section-title { background: #546e7a; color: #fff; }
  .gray-theme .section-body { background: #f7f8fa; border: 1.5px solid #cfd8dc; border-top: none; }
  .dark-theme .section-title { background: #263238; color: #fff; }
  .dark-theme .section-body { background: #eceff1; border: 1.5px solid #90a4ae; border-top: none; }

  /* CARDS */
  .card { border-radius: 8px; padding: 14px 16px; margin-bottom: 12px; border-left: 4px solid; }
  .card-red { background: #fff0f0; border-color: #c0392b; }
  .card-yellow { background: #fffde7; border-color: #f9a825; }
  .card-blue { background: #e3f0ff; border-color: #1565c0; }
  .card-green { background: #e8f5e9; border-color: #2e7d32; }
  .card-purple { background: #f3e5ff; border-color: #6a1b9a; }
  .card-gray { background: #f5f5f5; border-color: #90a4ae; }
  .card-title { font-weight: 700; font-size: 14px; margin-bottom: 4px; }
  .card-meta { font-size: 12px; color: #555; margin-bottom: 6px; }
  .card-row { display: flex; gap: 8px; margin-top: 6px; flex-wrap: wrap; }
  .badge { display: inline-block; border-radius: 12px; padding: 2px 10px; font-size: 11px; font-weight: 700; }
  .badge-red { background: #fde8e8; color: #c0392b; }
  .badge-yellow { background: #fff9c4; color: #b8860b; }
  .badge-blue { background: #e3f2fd; color: #1565c0; }
  .badge-green { background: #e8f5e9; color: #2e7d32; }
  .badge-purple { background: #f3e5f5; color: #6a1b9a; }
  .badge-gray { background: #eceff1; color: #546e7a; }
  .badge-orange { background: #fff3e0; color: #e65100; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #263238; color: #fff; padding: 8px 10px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.8px; }
  td { padding: 8px 10px; border-bottom: 1px solid #e0e0e0; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: rgba(0,0,0,0.025); }
  .tbl-red td:first-child { color: #c0392b; font-weight: 700; }
  .tbl-green td:first-child { color: #2e7d32; font-weight: 700; }
  .tbl-yellow td:first-child { color: #b8860b; font-weight: 700; }

  /* EXEC SUMMARY */
  .exec-bullets { list-style: none; padding: 0; }
  .exec-bullets li { padding: 10px 14px; border-radius: 7px; margin-bottom: 10px; font-size: 14px; display: flex; align-items: flex-start; gap: 10px; }
  .exec-bullets li .icon { font-size: 20px; flex-shrink: 0; }
  .exec-bullets li.risk { background: #fde8e8; border-left: 4px solid #c0392b; }
  .exec-bullets li.opp { background: #e8f5e9; border-left: 4px solid #2e7d32; }
  .exec-bullets li.cal { background: #e3f2fd; border-left: 4px solid #1565c0; }

  /* CALENDAR */
  .cal-day { margin-bottom: 16px; }
  .cal-day-header { background: #1565c0; color: #fff; border-radius: 6px; padding: 6px 14px; font-weight: 700; font-size: 13px; margin-bottom: 6px; }
  .cal-event { background: #fff; border-radius: 6px; padding: 10px 14px; margin-bottom: 6px; border-left: 4px solid #1565c0; box-shadow: 0 1px 4px rgba(0,0,0,0.06); }
  .cal-event.declined { border-left-color: #c0392b; background: #fff5f5; }
  .cal-event.needs-action { border-left-color: #f9a825; background: #fffde7; }
  .cal-event-title { font-weight: 700; font-size: 14px; }
  .cal-event-detail { font-size: 12px; color: #555; margin-top: 3px; }
  .cal-event-detail a { color: #1565c0; }
  .conflict-warn { background: #fde8e8; color: #c0392b; border-radius: 4px; padding: 2px 8px; font-size: 11px; font-weight: 700; margin-top: 4px; display: inline-block; }
  .prep-note { background: #fff9c4; color: #7a6000; border-radius: 4px; padding: 2px 8px; font-size: 11px; margin-top: 4px; display: inline-block; }

  /* DASHBOARD */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; }
  .dash-card { border-radius: 10px; padding: 16px; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.08); }
  .dash-card .dash-num { font-size: 32px; font-weight: 800; }
  .dash-card .dash-label { font-size: 12px; text-transform: uppercase; letter-spacing: 0.8px; margin-top: 4px; }
  .dash-red { background: #fde8e8; color: #c0392b; }
  .dash-yellow { background: #fffde7; color: #b8860b; }
  .dash-blue { background: #e3f2fd; color: #1565c0; }
  .dash-green { background: #e8f5e9; color: #2e7d32; }
  .dash-purple { background: #f3e5f5; color: #6a1b9a; }
  .dash-gray { background: #eceff1; color: #546e7a; }

  /* PRIORITY TABLE */
  .priority-high { color: #c0392b; font-weight: 700; }
  .priority-med { color: #b8860b; font-weight: 700; }
  .priority-low { color: #2e7d32; font-weight: 700; }

  /* TOP 3 */
  .top3 { counter-reset: top3; }
  .top3-item { display: flex; align-items: flex-start; gap: 16px; background: #fff; border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); border-left: 5px solid; }
  .top3-item:nth-child(1) { border-color: #c0392b; }
  .top3-item:nth-child(2) { border-color: #2e7d32; }
  .top3-item:nth-child(3) { border-color: #1565c0; }
  .top3-num { font-size: 28px; font-weight: 900; color: #aaa; flex-shrink: 0; line-height: 1; }
  .top3-item:nth-child(1) .top3-num { color: #c0392b; }
  .top3-item:nth-child(2) .top3-num { color: #2e7d32; }
  .top3-item:nth-child(3) .top3-num { color: #1565c0; }
  .top3-content .title { font-weight: 700; font-size: 15px; }
  .top3-content .desc { font-size: 13px; color: #555; margin-top: 4px; }

  /* UTILITY */
  .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  @media(max-width:700px){ .two-col { grid-template-columns: 1fr; } .header-meta { gap: 12px; } }
  .tag { display: inline-block; font-size: 11px; padding: 1px 7px; border-radius: 10px; margin-right: 4px; font-weight: 600; }
  .tag-inbox { background: #e3f2fd; color: #1565c0; }
  .tag-trash { background: #fde8e8; color: #c0392b; }
  .tag-unread { background: #fff9c4; color: #7a6000; }
  .tag-spam { background: #fde8e8; color: #7b0000; }
  hr.divider { border: none; border-top: 2px solid #e0e0e0; margin: 18px 0; }
  .small-note { font-size: 12px; color: #777; margin-top: 6px; }
  .acct-total { background: #263238; color: #fff; font-weight: 700; }
  .restore-badge { background: #e8f5e9; color: #2e7d32; border-radius: 10px; padding: 1px 8px; font-size: 11px; font-weight: 700; }
  .review-badge { background: #fff9c4; color: #7a6000; border-radius: 10px; padding: 1px 8px; font-size: 11px; font-weight: 700; }
  .delete-badge { background: #fde8e8; color: #c0392b; border-radius: 10px; padding: 1px 8px; font-size: 11px; font-weight: 700; }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════════
     SECTION 1: HEADER
═══════════════════════════════════════════════════════ -->
<div class="header">
  <div class="header h1" style="font-size:13px;color:#90b0cc;text-transform:uppercase;letter-spacing:2px;margin-bottom:6px;">Executive Briefing</div>
  <h1>Good Morning, Melissa 👋</h1>
  <div class="subtitle">Tuesday, June 16, 2026 &nbsp;|&nbsp; Prepared by your Executive Chief of Staff</div>
  <div class="header-meta">
    <div class="header-meta-item"><div class="label">Emails Reviewed</div><div class="value">50</div></div>
    <div class="header-meta-item"><div class="label">Calendar Events</div><div class="value">7</div></div>
    <div class="header-meta-item"><div class="label">Action Required</div><div class="value">6</div></div>
    <div class="header-meta-item"><div class="label">Today's Events</div><div class="value">1</div></div>
    <div class="header-meta-item"><div class="label">Open Job Leads</div><div class="value">4</div></div>
    <div class="header-meta-item"><div class="label">Security Alerts</div><div class="value">3</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     SECTION 2: EXECUTIVE SUMMARY
═══════════════════════════════════════════════════════ -->
<div class="section-wrap red-theme">
  <div class="section-title">⚡ Executive Summary</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li class="risk">
        <span class="icon">🔴</span>
        <div><strong>Security Risk:</strong> Three phishing/spam emails spoofing your own email address (<em>melissaw212</em>) arrived today — including a casino spam, an explicit adult spam, and a fake loan offer. These were not sent to Trash and remain in your mailbox. Immediate deletion is required. Additionally, a suspicious "Verification Center" loan scam email requires attention.</div>
      </li>
      <li class="opp">
        <span class="icon">🟢</span>
        <div><strong>Job Search Opportunity:</strong> Four high-value LinkedIn job alerts landed today — including an HR Director role paying <strong>$200K–$350K/year</strong> (Confidential) and a VP Global HRBP role at <strong>Circana</strong>. You also sent a follow-up email to Jillian about your deck, and a LinkedIn recruiter (Serafeim Makkas, Guidepoint) messaged about a consulting opportunity. Your pipeline is active — prioritize responses today.</div>
      </li>
      <li class="cal">
        <span class="icon">🔵</span>
        <div><strong>Calendar Urgency:</strong> Your <strong>Vet appointment</strong> is TODAY at 10:00 AM. Tomorrow (June 17) is back-to-back with a dental cleaning and your HR Networking Zoom. You have not RSVP'd to the <strong>HR Networking Group Zoom (Jun 17)</strong> or the <strong>Open Office Hours Zoom (Jun 18)</strong>. The <strong>Executive Roundtable (Jun 18)</strong> shows as Declined — confirm this is intentional.</div>
      </li>
    </ul>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     SECTION 3: ACTION REQUIRED
═══════════════════════════════════════════════════════ -->
<div class="section-wrap red-theme">
  <div class="section-title">🚨 Action Required</div>
  <div class="section-body">

    <div class="card card-red">
      <div class="card-row"><span class="badge badge-red">🔴 URGENT – SECURITY</span></div>
      <div class="card-title">Delete 3 Phishing / Spam Emails Spoofing Your Address</div>
      <div class="card-meta">From: melissaw212 (spoofed) &nbsp;|&nbsp; Received: Today</div>
      <div><strong>Why it matters:</strong> Emails spoofing your own Gmail address ("200 Free Spins," "130 Free Spins," "+18 Video," and a fake "Verification Center" loan offer) are active phishing attempts. They have not been trashed and sit in your main mailbox. These can indicate that your email address is being harvested or tested.</div>
      <div class="card-row" style="margin-top:8px;"><strong>Next Step:</strong> &nbsp;Delete all four immediately. Consider enabling Google's advanced spam filters and reviewing if your email is on any data-breach lists (HaveIBeenPwned.com).</div>
      <div class="card-row"><strong>Due:</strong> <span class="badge badge-red">TODAY</span></div>
    </div>

    <div class="card card-yellow">
      <div class="card-row"><span class="badge badge-yellow">🟡 RSVP NEEDED</span></div>
      <div class="card-title">RSVP: HR Networking & Job Search Group – Zoom 2 (Jun 17)</div>
      <div class="card-meta">Organizer: HR Networking Group &nbsp;|&nbsp; Tomorrow, 12:00–1:30 PM ET</div>
      <div><strong>Why it matters:</strong> Status shows <em>needsAction</em> — you have not confirmed attendance. This is a large, active networking group directly relevant to your job search. A separate "Network" event at the same time is confirmed, suggesting a duplicate or overlap.</div>
      <div class="card-row" style="margin-top:8px;"><strong>Next Step:</strong> &nbsp;Accept or decline the Zoom invite. Clarify whether the duplicate "Network" event on your calendar at the same time is the same session.</div>
      <div class="card-row"><strong>Due:</strong> <span class="badge badge-yellow">TODAY / TOMORROW</span></div>
    </div>

    <div class="card card-yellow">
      <div class="card-row"><span class="badge badge-yellow">🟡 RSVP NEEDED</span></div>
      <div class="card-title">RSVP: HR Networking Open Office Hours – Zoom (Jun 18)</div>
      <div class="card-meta">Organizer: HR Networking Group &nbsp;|&nbsp; Thursday, 12:00–1:00 PM ET</div>
      <div><strong>Why it matters:</strong> Status shows <em>needsAction</em>. Open office hours are a lower-pressure networking format and valuable for your active search.</div>
      <div class="card-row" style="margin-top:8px;"><strong>Next Step:</strong> &nbsp;Accept the Zoom invite. Note: the event description asks participants to disable automated AI notetaking tools.</div>
      <div class="card-row"><strong>Due:</strong> <span class="badge badge-yellow">TODAY / WEDNESDAY</span></div>
    </div>

    <div class="card card-green">
      <div class="card-row"><span class="badge badge-green">🟢 JOB SEARCH</span></div>
      <div class="card-title">Review & Apply: HR Director ($200K–$350K) + VP HRBP at Circana</div>
      <div class="card-meta">From: LinkedIn Job Alerts &nbsp;|&nbsp; Received: Today</div>
      <div><strong>Why it matters:</strong> The HR Director role (Confidential) at $200K–$350K and the VP Global Vertical HRBP Lead at Circana (Business AI, Technology & Product) are both senior roles aligned to your profile. Both are in your inbox.</div>
      <div class="card-row" style="margin-top:8px;"><strong>Next Step:</strong> &nbsp;Open both LinkedIn alerts today. Research Circana (they have a specific AI/Tech focus). Apply or bookmark immediately before postings close.</div>
      <div class="card-row"><strong>Due:</strong> <span class="badge badge-green">TODAY</span></div>
    </div>

    <div class="card card-green">
      <div class="card-row"><span class="badge badge-green">🟢 RECRUITER FOLLOW-UP</span></div>
      <div class="card-title">Respond: Serafeim Makkas – Guidepoint Consulting Opportunity (LinkedIn)</div>
      <div class="card-meta">From: LinkedIn (via Serafeim Makkas) &nbsp;|&nbsp; Received: Today, 8:39 AM</div>
      <div><strong>Why it matters:</strong> A recruiter from Guidepoint reached out about an HR/IT consulting opportunity. You received the message via LinkedIn. This is a warm inbound lead.</div>
      <div class="card-row" style="margin-top:8px;"><strong>Next Step:</strong> &nbsp;Log into LinkedIn and reply to Serafeim Makkas. Ask for a call to learn more about the Guidepoint role scope and compensation.</div>
      <div class="card-row"><strong>Due:</strong> <span class="badge badge-green">TODAY / TOMORROW</span></div>
    </div>

    <div class="card card-yellow">
      <div class="card-row"><span class="badge badge-yellow">🟡 FOLLOW-UP</span></div>
      <div class="card-title">Follow-Up Sent to Jillian Re: Melissa A. Weiss – Deck</div>
      <div class="card-meta">From: melissa (you) &nbsp;|&nbsp; Sent: Today, 9:28 AM</div>
      <div><strong>Why it matters:</strong> You followed up with Jillian this morning about next steps on your deck/presentation. This is an active outreach in your job search pipeline. No reply has been received yet.</div>
      <div class="card-row" style="margin-top:8px;"><strong>Next Step:</strong> &nbsp;Log this as a pending follow-up. If no reply by end of week, consider a phone call or LinkedIn message. Track in your job search log.</div>
      <div class="card-row"><strong>Due:</strong> <span class="badge badge-yellow">FOLLOW UP BY FRI, JUN 20</span></div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     SECTION 4: FULL 7-DAY CALENDAR
═══════════════════════════════════════════════════════ -->
<div class="section-wrap blue-theme">
  <div class="section-title">📅 Full 7-Day Calendar (Jun 16–23, 2026)</div>
  <div class="section-body">

    <!-- Tuesday June 16 -->
    <div class="cal-day">
      <div class="cal-day-header">📌 TODAY — Tuesday, June 16, 2026</div>
      <div class="cal-event">
        <div class="cal-event-title">🐾 Vet Appointment</div>
        <div class="cal-event-detail"><strong>Time:</strong> 10:00 AM – 11:00 AM ET</div>
        <div class="cal-event-detail"><strong>Location:</strong> Not specified</div>
        <div class="cal-event-detail"><strong>Status:</strong> <span class="badge badge-green">Confirmed ✓</span></div>
        <span class="prep-note">📋 Prep: Bring pet records, any medications, note current symptoms or questions for the vet.</span>
      </div>
    </div>

    <!-- Wednesday June 17 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Wednesday, June 17, 2026</div>
      <div class="cal-event">
        <div class="cal-event-title">🦷 Dental Cleaning – Dr. Deutch</div>
        <div class="cal-event-detail"><strong>Time:</strong> 10:45 AM – 11:45 AM ET</div>
        <div class="cal-event-detail"><strong>Location:</strong> Not specified</div>
        <div class="cal-event-detail"><strong>Status:</strong> <span class="badge badge-green">Confirmed ✓</span></div>
        <span class="prep-note">📋 Prep: Allow travel time; ends at 11:45 AM — Zoom starts at 12:00 PM. Very tight turnaround.</span>
        <span class="conflict-warn">⚠ TIGHT WINDOW: Only 15 minutes between dental end and Zoom start</span>
      </div>
      <div class="cal-event needs-action">
        <div class="cal-event-title">🤝 HR Networking & Job Search Group – Zoom 2</div>
        <div class="cal-event-detail"><strong>Time:</strong> 12:00 PM – 1:30 PM ET</div>
        <div class="cal-event-detail"><strong>Link:</strong> <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Join Zoom Meeting</a></div>
        <div class="cal-event-detail"><strong>Attendees:</strong> 100+ HR networking group members</div>
        <div class="cal-event-detail"><strong>Status:</strong> <span class="badge badge-yellow">⚠ Needs Action — RSVP Required</span></div>
        <span class="prep-note">📋 Prep: Review HR Networking Team Guidelines before attending. Prepare your 30-second intro and current search focus.</span>
      </div>
      <div class="cal-event">
        <div class="cal-event-title">🤝 Network (Duplicate/Overlap Event)</div>
        <div class="cal-event-detail"><strong>Time:</strong> 12:00 PM – 1:30 PM ET</div>
        <div class="cal-event-detail"><strong>Location:</strong> Not specified</div>
        <div class="cal-event-detail"><strong>Status:</strong> <span class="badge badge-green">Confirmed ✓</span></div>
        <span class="conflict-warn">⚠ POSSIBLE DUPLICATE: This overlaps exactly with the HR Networking Zoom above. Verify if this is the same event — consider removing one.</span>
      </div>
    </div>

    <!-- Thursday June 18 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Thursday, June 18, 2026</div>
      <div class="cal-event declined">
        <div class="cal-event-title">❌ Executive Roundtable (DECLINED)</div>
        <div class="cal-event-detail"><strong>Time:</strong> 9:00 AM – 10:30 AM ET</div>
        <div class="cal-event-detail"><strong>Host:</strong> John Madigan</div>
        <div class="cal-event-detail"><strong>Link:</strong> <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Meeting 207 786 667</a> | PW: 205454</div>
        <div class="cal-event-detail"><strong>Status:</strong> <span class="badge badge-red">Declined ✗</span></div>
        <span class="prep-note">📋 Note: Confirm this decline was intentional. If this is a professional development or networking opportunity, reconsider attending.</span>
      </div>
      <div class="cal-event needs-action">
        <div class="cal-event-title">🤝 HR Networking & Job Search: Open Office Hours – Zoom 2</div>
        <div class="cal-event-detail"><strong>Time:</strong> 12:00 PM – 1:00 PM ET</div>
        <div class="cal-event-detail"><strong>Link:</strong> <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Join Zoom Meeting</a></div>
        <div class="cal-event-detail"><strong>Attendees:</strong> 100+ HR networking group members</div>
        <div class="cal-event-detail"><strong>Status:</strong> <span class="badge badge-yellow">⚠ Needs Action — RSVP Required</span></div>
        <span class="prep-note">📋 Prep: Disable AI notetaking tools per organizer request. Prepare 1–2 questions about your current search blockers for the open discussion.</span>
      </div>
    </div>

    <!-- Friday June 19 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Friday, June 19, 2026 — Juneteenth (Federal Holiday)</div>
      <div class="cal-event">
        <div class="cal-event-title">No events scheduled</div>
        <div class="cal-event-detail">Free day — good time to review and apply to job postings or prepare for next week.</div>
      </div>
    </div>

    <!-- Saturday June 20 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Saturday, June 20, 2026</div>
      <div class="cal-event">
        <div class="cal-event-title">No events scheduled</div>
        <div class="cal-event-detail">No calendar events. Your Nextdoor neighbor posted a babysitting request for this evening (Sat 06/20, 10 PM+) — likely not relevant to you.</div>
      </div>
    </div>

    <!-- Sunday June 21 – Father's Day -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Sunday, June 21, 2026 — Father's Day</div>
      <div class="cal-event">
        <div class="cal-event-title">No events scheduled</div>
        <div class="cal-event-detail">No calendar events. Father's Day — plan accordingly if applicable.</div>
      </div>
    </div>

    <!-- Monday June 22 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Monday, June 22, 2026</div>
      <div class="cal-event">
        <div class="cal-event-title">No events scheduled</div>
        <div class="cal-event-detail">No calendar events. Good day for follow-ups and job applications.</div>
      </div>
    </div>

    <!-- Tuesday June 23 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Tuesday, June 23, 2026</div>
      <div class="cal-event needs-action">
        <div class="cal-event-title">📱 Verizon Fios Bill Due</div>
        <div class="cal-event-detail"><strong>All Day Event</strong></div>
        <div class="cal-event-detail"><strong>Status:</strong> <span class="badge badge-green">Confirmed ✓</span></div>
        <span class="prep-note">📋 Reminder: Verizon Fios bill is due. Confirm payment is scheduled or autopay is enabled.</span>
      </div>
      <div class="cal-event needs-action">
        <div class="cal-event-title">💰 Robinhood Account Transfer Bonus Deadline</div>
        <div class="cal-event-detail"><strong>Source:</strong> Robinhood email (now in Trash)</div>
        <div class="cal-event-detail">Transfer a taxable brokerage account by June 23 to earn a transfer bonus.</div>
        <span class="prep-note">📋 Note: Review Robinhood offer if interested in the bonus before this deadline passes.</span>
      </div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     SECTION 5: JOB SEARCH & INTERVIEW PIPELINE
═══════════════════════════════════════════════════════ -->
<div class="section-wrap green-theme">
  <div class="section-title">💼 Job Search & Interview Pipeline</div>
  <div class="section-body">

    <div style="margin-bottom:14px;"><strong>Active Outreach</strong></div>
    <div class="card card-green">
      <div class="card-row"><span class="badge badge-green">HIGH FIT</span><span class="badge badge-yellow">IN INBOX</span></div>
      <div class="card-title">HR Director – Confidential Company</div>
      <div class="card-meta">From: LinkedIn Job Alerts &nbsp;|&nbsp; Salary: $200,000–$350,000/year &nbsp;|&nbsp; Posted: Today</div>
      <div><strong>Why it matters:</strong> Exceptionally high compensation range for an HR Director. Confidential posting often signals urgency or sensitivity of the search. Aligns with Melissa's seniority profile.</div>
      <div><strong>Next Step:</strong> Open LinkedIn immediately and review full job description. Apply or save today.</div>
    </div>

    <div class="card card-green">
      <div class="card-row"><span class="badge badge-green">HIGH FIT</span><span class="badge badge-yellow">IN INBOX</span></div>
      <div class="card-title">VP, Global Vertical HRBP Lead – Business AI, Technology & Product (BATP) at Circana</div>
      <div class="card-meta">From: LinkedIn Job Alerts (2 alerts sent) &nbsp;|&nbsp; Received: Today, 3:05 AM &amp; 5:05 AM</div>
      <div><strong>Why it matters:</strong> VP-level HRBP at Circana with a focus on Business AI and Technology — aligns with future-of-work and AI leadership themes. Two alerts sent suggests strong match algorithm confidence.</div>
      <div><strong>Next Step:</strong> Research Circana's BATP division. Review role requirements on LinkedIn. Apply before posting closes.</div>
    </div>

    <div class="card card-green">
      <div class="card-row"><span class="badge badge-orange">MEDIUM FIT</span><span class="badge badge-red">IN TRASH</span></div>
      <div class="card-title">Senior Director – HRBP at Beacon Hill (via LinkedIn)</div>
      <div class="card-meta">From: LinkedIn Jobs &nbsp;|&nbsp; Posted: 6/12/2026 &nbsp;|&nbsp; Recruiter: Actively Recruiting</div>
      <div><strong>Why it matters:</strong> Senior Director HRBP at Beacon Hill — a staffing/professional services firm. Medium fit if open to that sector. Was moved to Trash but worth a look before deleting.</div>
      <div><strong>Next Step:</strong> Restore from Trash and review full job description on LinkedIn if interested.</div>
    </div>

    <div class="card card-green">
      <div class="card-row"><span class="badge badge-orange">MEDIUM FIT</span><span class="badge badge-red">IN TRASH</span></div>
      <div class="card-title">Senior Consultant – Orgvue (Philadelphia, PA)</div>
      <div class="card-meta">From: PostJobFree / Dennis Gorelik &nbsp;|&nbsp; Location: Philadelphia, PA</div>
      <div><strong>Why it matters:</strong> Orgvue is an organizational design and workforce analytics platform. A Senior Consultant role could be a consulting track. Relevant if open to consulting or analyst roles.</div>
      <div><strong>Next Step:</strong> Review if Orgvue consulting work interests you. Restore from Trash and investigate.</div>
    </div>

    <div class="card card-green">
      <div class="card-row"><span class="badge badge-green">HIGH PRIORITY</span><span class="badge badge-red">IN TRASH</span></div>
      <div class="card-title">Guidepoint Consulting Opportunity – Serafeim Makkas (LinkedIn Message)</div>
      <div class="card-meta">From: LinkedIn (via Serafeim Makkas) &nbsp;|&nbsp; Received: Today, 8:39 AM</div>
      <div><strong>Why it matters:</strong> Inbound recruiter message via LinkedIn about HR in IT/Technology Consultancies — a warm lead from a named recruiter at Guidepoint. Higher conversion probability than cold applications.</div>
      <div><strong>Next Step:</strong> Reply on LinkedIn today. Ask for a brief call to discuss scope, level, and compensation.</div>
    </div>

    <div class="card card-green">
      <div class="card-row"><span class="badge badge-orange">MEDIUM FIT</span><span class="badge badge-red">IN TRASH</span></div>
      <div class="card-title">Job Recommendations – Inclusively Platform</div>
      <div class="card-meta">From: Inclusively &nbsp;|&nbsp; Received: Today, 8:29 AM</div>
      <div><strong>Why it matters:</strong> Inclusively is a disability-inclusive hiring platform with curated job recommendations for your profile. Worth a quick scan.</div>
      <div><strong>Next Step:</strong> Log into Inclusively and review recommended roles. Low time investment.</div>
    </div>

    <hr class="divider">
    <div style="margin-bottom:10px;"><strong>Networking Sessions This Week</strong></div>
    <table>
      <tr><th>Date</th><th>Event</th><th>Status</th><th>Priority</th></tr>
      <tr><td>Jun 17, 12–1:30 PM</td><td>HR Networking & Job Search Group – Zoom 2</td><td><span class="badge badge-yellow">RSVP Pending</span></td><td><span class="badge badge-red">HIGH</span></td></tr>
      <tr><td>Jun 17, 12–1:30 PM</td><td>Network (Duplicate Event)</td><td><span class="badge badge-green">Confirmed</span></td><td><span class="badge badge-orange">VERIFY DUPLICATE</span></td></tr>
      <tr><td>Jun 18, 12–1 PM</td><td>HR Networking Open Office Hours – Zoom</td><td><span class="badge badge-yellow">RSVP Pending</span></td><td><span class="badge badge-red">HIGH</span></td></tr>
    </table>

    <hr class="divider">
    <div style="margin-bottom:10px;"><strong>Active Follow-Ups</strong></div>
    <div class="card card-yellow">
      <div class="card-title">📧 Follow-Up Sent to Jillian – "Melissa A. Weiss – Deck"</div>
      <div class="card-meta">Sent by Melissa this morning at 9:28 AM. Awaiting response on next steps.</div>
      <div><strong>Next Step:</strong> If no reply by Friday June 20, send a LinkedIn message or call Jillian directly.</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     SECTION 6: FULL EMAIL REVIEW BY CATEGORY
═══════════════════════════════════════════════════════ -->
<div class="section-wrap dark-theme">
  <div class="section-title">📧 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="card card-red">
      <div class="card-row"><span class="badge badge-red">🔴 SECURITY / RISK — 4 Emails</span></div>
      <div class="card-title">Phishing, Spam & Scam Emails</div>
      <div class="card-meta"><strong>Senders:</strong> melissaw212 (spoofed ×3), 'Verification Center' (spoofed)</div>
      <table style="margin-top:8px;">
        <tr><th>Subject</th><th>From (spoofed)</th><th>Status</th><th>Action</th></tr>
        <tr><td>200 Free Spins 💰 No Deposit Needed 🔥</td><td>melissaw212 (xcvricpmsqhevr…)</td><td><span class="tag-unread tag">Unread</span></td><td>DELETE NOW</td></tr>
        <tr><td>130 Free Spins 💰 No Deposit Needed</td><td>melissaw212 (nejrwkuxwmevrt…)</td><td><span class="tag-unread tag">Unread</span></td><td>DELETE NOW</td></tr>
        <tr><td>WATCH THIS FILTHY +18 VIDEO NOW 🔞</td><td>melissaw212 (nejrwkuxwmevrt…)</td><td><span class="tag-unread tag">Unread</span></td><td>DELETE NOW</td></tr>
        <tr><td>Your Loan Application Status – Pending...</td><td>'Verification Center' (kgrzsnfy…)</td><td><span class="tag-unread tag">Unread</span></td><td>DELETE NOW</td></tr>
      </table>
      <div class="small-note" style="margin-top:8px;">⚠️ All four are NOT in trash — they remain in your mailbox. This is high priority. None are legitimate.</div>
    </div>

    <!-- JOB SEARCH -->
    <div class="card card-green">
      <div class="card-row"><span class="badge badge-green">🟢 JOB SEARCH — 7 Emails</span></div>
      <div class="card-title">Job Alerts, Recruiter Outreach & Job Platforms</div>
      <div class="card-meta"><strong>Senders:</strong> LinkedIn Job Alerts (×3), LinkedIn Recruiter (Serafeim Makkas), Inclusively, PostJobFree (Orgvue), Melissa's own follow-up (Jillian deck)</div>
      <table style="margin-top:8px;">
        <tr><th>Subject</th><th>Location</th><th>Priority</th></tr>
        <tr><td>HR Director at Confidential – $200K–$350K/yr</td><td><span class="tag-inbox tag">Inbox</span></td><td><span class="badge badge-green">HIGH</span></td></tr>
        <tr><td>VP, Global Vertical HRBP Lead – Circana (×2)</td><td><span class="tag-inbox tag">Inbox</span></td><td><span class="badge badge-green">HIGH</span></td></tr>
        <tr><td>Senior Director HRBP – Beacon Hill (LinkedIn)</td><td><span class="tag-trash tag">Trash</span></td><td><span class="badge badge-orange">MEDIUM</span></td></tr>
        <tr><td>Guidepoint Consulting Opportunity – Serafeim Makkas</td><td><span class="tag-trash tag">Trash</span></td><td><span class="badge badge-green">HIGH</span></td></tr>
        <tr><td>Melissa Weiss – Recommended Jobs – Inclusively</td><td><span class="tag-trash tag">Trash</span></td><td><span class="badge badge-orange">MEDIUM</span></td></tr>
        <tr><td>Orgvue Senior Consultant – Philadelphia, PA</td><td><span class="tag-trash tag">Trash</span></td><td><span class="badge badge-orange">MEDIUM</span></td></tr>
        <tr><td>Re: Melissa A Weiss – Deck (follow-up to Jillian)</td><td><span class="tag">Sent</span></td><td><span class="badge badge-green">HIGH</span></td></tr>
      </table>
      <div><strong>Recommended Action:</strong> Act on LinkedIn alerts today. Reply to Serafeim Makkas. Track Jillian response.</div>
    </div>

    <!-- CALENDAR / EVENTS -->
    <div class="card card-blue">
      <div class="card-row"><span class="badge badge-blue">🔵 CALENDAR / EVENTS — 2 Emails (Newsletter-linked)</span></div>
      <div class="card-title">HR Networking Group Emails (tied to calendar events)</div>
      <div class="card-meta"><strong>Senders:</strong> Christopher Rainey via LinkedIn (LinkedIn newsletter, culture), the co-lab (Substack, remote fashion)</div>
      <div>These two inbox newsletters were included because they appeared in the main inbox. See Newsletter section for full details.</div>
      <div><strong>Recommended Action:</strong> Scan headlines when time allows. Low urgency.</div>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="card card-yellow">
      <div class="card-row"><span class="badge badge-yellow">🟡 FINANCIAL / BILLING — 5 Emails</span></div>
      <div class="card-title">Bank, Brokerage & Credit Card Notifications</div>
      <div class="card-meta"><strong>Senders:</strong> Chase, Bank of America (×2), Merrill Edge, Robinhood</div>
      <table style="margin-top:8px;">
        <tr><th>Subject</th><th>Detail</th><th>Location</th><th>Action</th></tr>
        <tr><td>Chase Slate Visa Payment Received</td><td>Payment applied to account</td><td><span class="tag-trash tag">Trash</span></td><td>Confirm receipt, then delete</td></tr>
        <tr><td>BofA: Direct Deposit Credited – $80.00</td><td>From Venmo Cashout – Acct 7471</td><td><span class="tag-trash tag">Trash</span></td><td>Confirm, then delete</td></tr>
        <tr><td>BofA: Your Statement Available – MMS 7549</td><td>Money Market Savings statement</td><td>Not in trash</td><td>Review statement when convenient</td></tr>
        <tr><td>Merrill Edge: New Trade Confirmation</td><td>Trade confirmation available in app</td><td><span class="tag-trash tag">Trash</span></td><td>Review trade, then delete</td></tr>
        <tr><td>Robinhood: Your Bonus Ends This Week (Jun 23)</td><td>Transfer brokerage by June 23 to earn bonus</td><td><span class="tag-trash tag">Trash</span></td><td>Decide by June 23</td></tr>
      </table>
      <div><strong>Recommended Action:</strong> The BofA Money Market statement and Robinhood deadline warrant quick review. Others are routine confirmations.</div>
    </div>

    <!-- MEDICAL / HEALTH -->
    <div class="card card-blue">
      <div class="card-row"><span class="badge badge-blue">🔵 MEDICAL / HEALTH — 1 Email</span></div>
      <div class="card-title">EverPresent: Is It Better to Digitize Photos or Negatives?</div>
      <div class="card-meta"><strong>From:</strong> EverPresent &lt;info@everpresent.com&gt; &nbsp;|&nbsp; Not in inbox, not in trash</div>
      <div>A blog digest from EverPresent, a photo digitization service. Low urgency — personal interest item.</div>
      <div><strong>Recommended Action:</strong> Read if interested in digitizing photos. Otherwise archive or unsubscribe.</div>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="card card-purple">
      <div class="card-row"><span class="badge badge-purple">🟣 PROFESSIONAL DEVELOPMENT — 3 Emails</span></div>
      <div class="card-title">Leadership, AI, Career Development Newsletters</div>
      <div class="card-meta"><strong>Senders:</strong> AI For Leaders, Level Up Newsletter (Ethan Evans), KKARENISM (Substack)</div>
      <table style="margin-top:8px;">
        <tr><th>Subject</th><th>Location</th><th>Relevance</th></tr>
        <tr><td>Human-in-the-Loop Needs to Be a Real Job – AI For Leaders</td><td><span class="tag-trash tag">Trash</span></td><td>High – AI/HR intersection, timely topic</td></tr>
        <tr><td>Why People With Half Your Talent Keep Winning – Level Up</td><td><span class="tag-trash tag">Trash</span></td><td>High – Career visibility &amp; advocacy</td></tr>
        <tr><td>New Industry Hiring Data & What To Do About It – KKARENISM</td><td><span class="tag-trash tag">Trash</span></td><td>High – Job search strategy</td></tr>
      </table>
      <div><strong>Recommended Action:</strong> All three are relevant to your search and leadership brand. Restore from Trash or at least read before deleting.</div>
    </div>

    <!-- PERSONAL -->
    <div class="card card-gray">
      <div class="card-row"><span class="badge badge-gray">⚪ PERSONAL — 3 Emails</span></div>
      <div class="card-title">USPS Informed Delivery, Match.com, Nextdoor Neighbors</div>
      <div class="card-meta"><strong>Senders:</strong> USPS Informed Delivery, Match, Nextdoor (Yorkville neighbors)</div>
      <table style="margin-top:8px;">
        <tr><th>Subject</th><th>Detail</th><th>Action</th></tr>
        <tr><td>USPS: Daily Digest Tue 6/16 – 1 mailpiece, 1 package arriving</td><td>Standard delivery notification</td><td>Note — package coming today</td></tr>
        <tr><td>Match: Dominic likes you</td><td>Dating app notification</td><td>Personal — check if interested</td></tr>
        <tr><td>Nextdoor: Yorkville neighbors seeking babysitter Sat 6/20</td><td>Community board post</td><td>Ignore unless relevant</td></tr>
      </table>
      <div><strong>Recommended Action:</strong> USPS — note package arriving today. Others are personal / low priority.</div>
    </div>

    <!-- NEWSLETTERS / SUBSCRIPTIONS -->
    <div class="card card-purple">
      <div class="card-row"><span class="badge badge-purple">🟣 NEWSLETTERS / SUBSCRIPTIONS — 8 Emails</span></div>
      <div class="card-title">News, Finance, AI, Business Newsletters</div>
      <div class="card-meta"><strong>Senders:</strong> The Hustle, TLDR (×2), TLDR Crypto, The Average Joe, The Daily Skimm, Medium Daily Digest, 1% Better, BambooHR, SmartAsset, Charles Schwab</div>
      <div>(See full breakdown in Newsletters & Subscriptions section below.)</div>
      <div><strong>Recommended Action:</strong> Scan headlines. Most are in Trash and can remain there. Consider unsubscribing from low-value senders.</div>
    </div>

    <!-- PROMOTIONAL / RETAIL -->
    <div class="card card-gray">
      <div class="card-row"><span class="badge badge-gray">⚪ PROMOTIONAL / RETAIL — 12 Emails</span></div>
      <div class="card-title">Retail, Fashion, Travel & Coupon Emails</div>
      <div class="card-meta"><strong>Senders:</strong> Halara, JetBlue Vacations, Zappos, PUMA, Gap Factory, SHEIN (×2), Kohl's, YesStyle, CoinOut, MeidasTouch+, CoolDeep AI</div>
      <div>(See full breakdown in Promotional / Retail Summary section below.)</div>
      <div><strong>Recommended Action:</strong> Most are in Trash — leave or permanently delete. No urgent action required.</div>
    </div>

    <!-- SAFE TO DELETE / IGNORE -->
    <div class="card card-gray">
      <div class="card-row"><span class="badge badge-gray">⚪ SAFE TO DELETE / IGNORE — 5 Emails</span></div>
      <div class="card-title">MeidasTouch Podcast, Lisa Rangel (Career Coach Promo), Meidas+, CoinOut Bonus, Lisa Rangel</div>
      <div class="card-meta">These are lower-priority newsletter or promotional items already in Trash.</div>
      <div><strong>Recommended Action:</strong> Permanently delete from Trash. No action needed.</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     SECTION 7: TRASH REVIEW
═══════════════════════════════════════════════════════ -->
<div class="section-wrap red-theme">
  <div class="section-title">🗑️ Trash Review</div>
  <div class="section-body">
    <p style="margin-bottom:12px;font-size:13px;">The following 29 emails were found in the Gmail Trash. They are reviewed below in three groups.</p>

    <!-- RESTORE -->
    <div style="margin-bottom:16px;">
      <div style="font-weight:700;font-size:14px;margin-bottom:8px;">♻️ <span class="restore-badge">RESTORE IMMEDIATELY</span> — 5 Emails</div>
      <table>
        <tr><th>Sender</th><th>Subject</th><th>Why Restore</th></tr>
        <tr><td>LinkedIn Job Alerts</td><td>Senior Director – HRBP at Beacon Hill (actively recruiting)</td><td>Active job lead, medium-high fit, recruiter actively hiring</td></tr>
        <tr><td>LinkedIn (Serafeim Makkas)</td><td>Guidepoint Consulting Opportunity – HR in IT</td><td>Warm inbound recruiter lead — reply needed</td></tr>
        <tr><td>Inclusively</td><td>melissa weiss – Recommended Jobs</td><td>Profile-matched job recommendations worth reviewing</td></tr>
        <tr><td>AI For Leaders</td><td>Human-in-the-Loop Needs to Be a Real Job</td><td>Directly relevant to AI + HR leadership positioning</td></tr>
        <tr><td>KKARENISM (Substack)</td><td>New Industry Hiring Data & What To Do About It</td><td>Job search strategy intelligence — actionable content</td></tr>
      </table>
    </div>

    <!-- REVIEW BEFORE DELETING -->
    <div style="margin-bottom:16px;">
      <div style="font-weight:700;font-size:14px;margin-bottom:8px;">🔍 <span class="review-badge">REVIEW BEFORE DELETING</span> — 8 Emails</div>
      <table>
        <tr><th>Sender</th><th>Subject</th><th>Why Review</th></tr>
        <tr><td>Robinhood</td><td>Your bonus ends this week (Jun 23 deadline)</td><td>Financial deadline — decide if you want to transfer a brokerage account by June 23</td></tr>
        <tr><td>Merrill Edge</td><td>You have a new trade confirmation</td><td>Confirm trade details before deleting</td></tr>
        <tr><td>Chase</td><td>Chase Slate Visa payment received</td><td>Confirm payment was applied correctly</td></tr>
        <tr><td>Bank of America</td><td>Direct deposit – $80.00 (Venmo Cashout)</td><td>Verify the deposit is expected and correct</td></tr>
        <tr><td>PostJobFree (Dennis Gorelik)</td><td>Orgvue – Senior Consultant, Philadelphia PA</td><td>Consulting/analytics role worth a quick glance if open to that path</td></tr>
        <tr><td>Level Up Newsletter</td><td>Why People With Half Your Talent Keep Winning</td><td>Career advocacy insights relevant to your search</td></tr>
        <tr><td>TLDR</td><td>Anthropic's superpower, Roku acquired (×2 duplicates)</td><td>Tech news relevant to AI+HR positioning. Duplicate — keep one.</td></tr>
        <tr><td>USPS Informed Delivery</td><td>Daily Digest – 1 mailpiece, 1 package</td><td>Package arriving today — useful to note, then delete</td></tr>
      </table>
    </div>

    <!-- SAFE TO DELETE -->
    <div>
      <div style="font-weight:700;font-size:14px;margin-bottom:8px;">🗑️ <span class="delete-badge">SAFE TO DELETE PERMANENTLY</span> — 16 Emails</div>
      <table>
        <tr><th>Sender</th><th>Subject</th><th>Reason</th></tr>
        <tr><td>JetBlue Vacations</td><td>Up to 100% off flights with Norwegian Cruise Line</td><td>Promotional travel offer — no action needed</td></tr>
        <tr><td>Zappos</td><td>Talk about necessary – new styles</td><td>Retail promo — low priority</td></tr>
        <tr><td>PUMA</td><td>Last Chance For $10 Off ⌛</td><td>Retail promo — likely expired</td></tr>
        <tr><td>Kohl's</td><td>Save 30% | Father's Day gifts</td><td>Retail promo — delete</td></tr>
        <tr><td>SHEIN (×2)</td><td>Closet Makeover Time</td><td>Duplicate retail promo — delete both</td></tr>
        <tr><td>Gap Factory</td><td>60% off sitewide + extra 15% off</td><td>Retail promo — delete</td></tr>
        <tr><td>YesStyle</td><td>50% OFF VIRAL SPF ☀️</td><td>Retail promo — delete</td></tr>
        <tr><td>TLDR Crypto</td><td>World Cup prediction markets, SpaceX IPO</td><td>Crypto newsletter — low relevance</td></tr>
        <tr><td>The Hustle</td><td>The economics of mangoes</td><td>General news — low value for your priorities today</td></tr>
        <tr><td>The Average Joe</td><td>⏱️ Microshifting</td><td>Finance newsletter — low urgency</td></tr>
        <tr><td>SmartAsset</td
<hr>
<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Financial / Billing</td><td>1</td></tr>
<tr><td>Job Search / Recruiters</td><td>12</td></tr>
<tr><td>Medical / Health</td><td>1</td></tr>
<tr><td>Other / Review</td><td>21</td></tr>
<tr><td>Professional Development / Newsletters</td><td>8</td></tr>
<tr><td>Promotional / Retail</td><td>4</td></tr>
<tr><td>Security / Risk</td><td>3</td></tr>
</table>
<p><strong>Audit Note:</strong> Every fetched email was reviewed and assigned to one category. Trash emails were included in review. Promotional and low-value emails were accounted for but deprioritized.</p>

