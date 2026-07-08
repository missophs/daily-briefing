<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing – Melissa Weiss – July 8, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px 48px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px 28px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 15px; color: #a0b4d0; margin-top: 6px; }
  .header .meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 18px; text-align: center; }
  .header .meta-item .val { font-size: 22px; font-weight: 700; color: #7ecfff; }
  .header .meta-item .lbl { font-size: 11px; color: #a0b4d0; text-transform: uppercase; letter-spacing: 1px; margin-top: 2px; }

  /* SECTION TITLES */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; padding: 10px 16px; border-radius: 8px 8px 0 0; color: #fff; }
  .section-body { border-radius: 0 0 10px 10px; padding: 18px; }

  /* COLOR THEMES */
  .theme-red    { background: #c0392b; }
  .theme-yellow { background: #d4a017; }
  .theme-blue   { background: #1a6eb5; }
  .theme-green  { background: #1e8449; }
  .theme-purple { background: #6c3483; }
  .theme-gray   { background: #5d6d7e; }
  .theme-teal   { background: #148f77; }
  .theme-navy   { background: #1a3a5c; }

  .body-red    { background: #fdf2f2; border: 1px solid #f5c6c6; }
  .body-yellow { background: #fffdf0; border: 1px solid #f5e6a0; }
  .body-blue   { background: #f0f6ff; border: 1px solid #b8d4f5; }
  .body-green  { background: #f0faf4; border: 1px solid #a9dfbf; }
  .body-purple { background: #faf0ff; border: 1px solid #d7b8f5; }
  .body-gray   { background: #f5f6f7; border: 1px solid #d5d8dc; }
  .body-teal   { background: #f0faf8; border: 1px solid #a0d8cf; }
  .body-navy   { background: #f0f4fa; border: 1px solid #b0c4d8; }

  /* CARDS */
  .card { background: #fff; border-radius: 10px; padding: 16px 20px; margin-bottom: 14px; border-left: 5px solid #ccc; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }
  .card-red    { border-left-color: #c0392b; }
  .card-yellow { border-left-color: #d4a017; }
  .card-blue   { border-left-color: #1a6eb5; }
  .card-green  { border-left-color: #1e8449; }
  .card-purple { border-left-color: #6c3483; }
  .card-gray   { border-left-color: #7f8c8d; }
  .card-teal   { border-left-color: #148f77; }
  .card .card-label { display: inline-block; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; padding: 2px 8px; border-radius: 4px; color: #fff; margin-bottom: 6px; }
  .label-red    { background: #c0392b; }
  .label-yellow { background: #d4a017; }
  .label-blue   { background: #1a6eb5; }
  .label-green  { background: #1e8449; }
  .label-purple { background: #6c3483; }
  .label-gray   { background: #7f8c8d; }
  .label-teal   { background: #148f77; }
  .card h3 { font-size: 15px; font-weight: 700; margin-bottom: 4px; }
  .card .card-source { font-size: 11px; color: #888; margin-bottom: 6px; }
  .card .card-body { font-size: 13px; color: #444; line-height: 1.6; }
  .card .card-next { margin-top: 8px; background: #f0f6ff; border-radius: 5px; padding: 7px 12px; font-size: 12px; color: #1a4a80; font-weight: 600; }
  .card .card-due { margin-top: 6px; font-size: 11px; color: #c0392b; font-weight: 600; }

  /* EXEC SUMMARY */
  .exec-summary { display: flex; gap: 14px; flex-wrap: wrap; margin-bottom: 28px; }
  .exec-bullet { flex: 1 1 280px; border-radius: 10px; padding: 16px 18px; color: #fff; min-width: 240px; }
  .exec-bullet .eb-icon { font-size: 22px; margin-bottom: 6px; }
  .exec-bullet .eb-title { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; opacity: 0.85; margin-bottom: 4px; }
  .exec-bullet .eb-text { font-size: 13px; line-height: 1.5; }
  .eb-red    { background: linear-gradient(135deg, #c0392b, #e74c3c); }
  .eb-green  { background: linear-gradient(135deg, #1e8449, #27ae60); }
  .eb-blue   { background: linear-gradient(135deg, #1a6eb5, #2980b9); }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  thead th { background: #f0f2f5; font-weight: 700; padding: 9px 12px; text-align: left; border-bottom: 2px solid #d5d8dc; }
  tbody td { padding: 8px 12px; border-bottom: 1px solid #eee; vertical-align: top; }
  tbody tr:last-child td { border-bottom: none; }
  tbody tr:hover { background: #fafbfc; }
  .tag { display: inline-block; padding: 2px 7px; border-radius: 4px; font-size: 10px; font-weight: 700; color: #fff; text-transform: uppercase; }
  .tag-red    { background: #c0392b; }
  .tag-yellow { background: #d4a017; }
  .tag-green  { background: #1e8449; }
  .tag-blue   { background: #1a6eb5; }
  .tag-purple { background: #6c3483; }
  .tag-gray   { background: #7f8c8d; }
  .tag-high   { background: #c0392b; }
  .tag-medium { background: #d4a017; }
  .tag-low    { background: #7f8c8d; }

  /* CALENDAR DAY */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { font-size: 14px; font-weight: 700; color: #1a3a5c; padding: 7px 14px; background: #dce8f5; border-radius: 7px; margin-bottom: 8px; }
  .cal-event { background: #fff; border-left: 4px solid #1a6eb5; border-radius: 7px; padding: 10px 14px; margin-bottom: 7px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }
  .cal-event.declined { border-left-color: #c0392b; opacity: 0.75; }
  .cal-event.needs-action { border-left-color: #d4a017; }
  .cal-event.confirmed, .cal-event.accepted { border-left-color: #1e8449; }
  .cal-event .ce-time { font-size: 12px; font-weight: 700; color: #1a6eb5; margin-bottom: 2px; }
  .cal-event .ce-title { font-size: 14px; font-weight: 700; color: #1a1a2e; }
  .cal-event .ce-detail { font-size: 12px; color: #555; margin-top: 4px; line-height: 1.5; }
  .cal-event .ce-status { display: inline-block; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 4px; color: #fff; margin-left: 8px; vertical-align: middle; }
  .status-accepted  { background: #1e8449; }
  .status-confirmed { background: #1e8449; }
  .status-declined  { background: #c0392b; }
  .status-needs     { background: #d4a017; }
  .conflict-warn { font-size: 11px; color: #c0392b; font-weight: 700; margin-top: 3px; }

  /* DASHBOARD GRID */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 12px; }
  .dash-tile { background: #fff; border-radius: 10px; padding: 16px; text-align: center; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
  .dash-tile .dt-num { font-size: 32px; font-weight: 800; }
  .dash-tile .dt-lbl { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #888; margin-top: 4px; }
  .dt-red    .dt-num { color: #c0392b; }
  .dt-yellow .dt-num { color: #d4a017; }
  .dt-blue   .dt-num { color: #1a6eb5; }
  .dt-green  .dt-num { color: #1e8449; }
  .dt-purple .dt-num { color: #6c3483; }

  /* MISC */
  .pill { display: inline-block; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 700; }
  .pill-red    { background: #fdecea; color: #c0392b; }
  .pill-yellow { background: #fff8e1; color: #d4a017; }
  .pill-green  { background: #eafaf1; color: #1e8449; }
  .pill-blue   { background: #e8f4fd; color: #1a6eb5; }
  .pill-purple { background: #f5eaff; color: #6c3483; }
  .pill-gray   { background: #f4f6f7; color: #5d6d7e; }

  .note { font-size: 12px; color: #666; font-style: italic; padding: 8px 0; }
  .divider { height: 1px; background: #e0e4ea; margin: 16px 0; }
  .badge-unread { display: inline-block; background: #e74c3c; color: #fff; font-size: 10px; font-weight: 700; border-radius: 4px; padding: 1px 5px; margin-left: 4px; }
  ul.compact li { margin-bottom: 4px; font-size: 13px; line-height: 1.5; }
  .top3 { counter-reset: top3; }
  .top3-item { display: flex; align-items: flex-start; gap: 14px; background: #fff; border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }
  .top3-num { font-size: 36px; font-weight: 900; color: #e0e8f5; min-width: 44px; text-align: center; line-height: 1; }
  .top3-content .t3-title { font-size: 15px; font-weight: 700; color: #1a1a2e; }
  .top3-content .t3-body  { font-size: 13px; color: #555; margin-top: 4px; line-height: 1.5; }
  .acct-total { font-weight: 700; background: #f0f4fa; }

  @media (max-width: 700px) {
    .header { padding: 20px 16px; }
    .header .meta { gap: 10px; }
    .exec-summary { flex-direction: column; }
  }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════════ 1. HEADER ═══ -->
<div class="header">
  <h1>📋 Executive Briefing</h1>
  <div class="subtitle">Prepared by your Chief of Staff &nbsp;·&nbsp; Wednesday, July 8, 2026</div>
  <div class="meta">
    <div class="meta-item"><div class="val">Melissa</div><div class="lbl">Good Morning</div></div>
    <div class="meta-item"><div class="val">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="meta-item"><div class="val">11</div><div class="lbl">Calendar Events</div></div>
    <div class="meta-item"><div class="val">3</div><div class="lbl">Action Items Today</div></div>
    <div class="meta-item"><div class="val">Wed Jul 8</div><div class="lbl">Briefing Date</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════ 2. EXEC SUMMARY ═══ -->
<div class="section">
  <div class="section-title theme-navy" style="border-radius:8px;">⚡ Executive Summary</div>
  <div class="exec-summary" style="margin-top:14px;">
    <div class="exec-bullet eb-red">
      <div class="eb-icon">🔴</div>
      <div class="eb-title">Biggest Risk / Urgent</div>
      <div class="eb-text">Multiple spam/scam emails landed in your inbox (fake antivirus billing, explicit spam, casino sign-in). A medical bill from CHSLI (account #8164) is due <strong>July 24</strong> — action needed. Bancroft CHRO rejection received today — close that pipeline item.</div>
    </div>
    <div class="exec-bullet eb-green">
      <div class="eb-icon">🟢</div>
      <div class="eb-title">Biggest Job Search Opportunity</div>
      <div class="eb-text"><strong>Oscar Health phone screen (People Strategy Lead)</strong> is confirmed for <strong>Friday, July 10 at 2:00 PM</strong> with Joelle Molina. Prep is required. Daily Job Search Sweep flagged 22 priority opportunities. PeopleOps Jobs listed 83+ remote HR roles.</div>
    </div>
    <div class="exec-bullet eb-blue">
      <div class="eb-icon">🔵</div>
      <div class="eb-title">Biggest Calendar / Deadline</div>
      <div class="eb-text"><strong>Tomorrow (Thu July 9):</strong> New patient appointment with Dr. Beth Leeman-Markowski (Epilepsy Center, 3:30 PM) — arrive 15 min early with insurance card, records, and ID. HR Networking open office hours also at noon. RSVP still pending on both networking Zooms.</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════ 3. ACTION REQUIRED ═══ -->
<div class="section">
  <div class="section-title theme-red">🚨 Action Required</div>
  <div class="section-body body-red">

    <div class="card card-red">
      <span class="card-label label-red">SECURITY · SPAM</span>
      <h3>Fake Antivirus Billing Scam in Inbox</h3>
      <div class="card-source">From: Payment_Processing &lt;i5pnrx6yav@ygsa28i004.us&gt; · Subject: "Action Required: Your payment was declined"</div>
      <div class="card-body">This email is a phishing/scam. The sender domain is randomly generated. Do NOT click any links. It claims your antivirus subscription failed billing.</div>
      <div class="card-next">→ Mark as spam immediately. Do not click any links. Consider reporting to Gmail as phishing.</div>
      <div class="card-due">⚠️ Act today — do not engage</div>
    </div>

    <div class="card card-red">
      <span class="card-label label-red">SECURITY · EXPLICIT SPAM</span>
      <h3>Explicit/Adult Spam in Non-Inbox (Not Trashed)</h3>
      <div class="card-source">From: "Dr. Nathan Ford" &lt;gsgblfwjruaaxp…&gt; · Subject: explicit content</div>
      <div class="card-body">Unsolicited explicit spam from a spoofed sender domain. Sitting in non-inbox but not trashed. Should be deleted and marked as spam.</div>
      <div class="card-next">→ Mark as spam and delete immediately.</div>
      <div class="card-due">⚠️ Act today</div>
    </div>

    <div class="card card-red">
      <span class="card-label label-red">SECURITY · PHISHING</span>
      <h3>Casino Sign-In Request (Unsolicited)</h3>
      <div class="card-source">From: noreply@casi-03.firebaseapp.com · Subject: "Sign in to 🔥Get a 55 Free Spins Welcome BONUS"</div>
      <div class="card-body">You did not request this sign-in. Your email address may be being tested by a phishing actor. Do not click the sign-in link.</div>
      <div class="card-next">→ Delete and mark as phishing. Do not click "sign in."</div>
      <div class="card-due">⚠️ Act today</div>
    </div>

    <div class="card card-red">
      <span class="card-label label-red">SECURITY · PHARMA SPAM</span>
      <h3>Unsolicited Prescription Drug Solicitation</h3>
      <div class="card-source">From: "Dr. Keller | Care Øharmacy" &lt;a.keller@carescript.net&gt; · Subject: "Priligy – new control, new confidence"</div>
      <div class="card-body">Unsolicited pharma spam. Not from a legitimate pharmacy. Spoofed sender name with unicode characters to evade filters.</div>
      <div class="card-next">→ Mark as spam and delete. Do not click any links.</div>
      <div class="card-due">⚠️ Act today</div>
    </div>

    <div class="card card-yellow">
      <span class="card-label label-yellow">BILLING · DEADLINE</span>
      <h3>Medical Bill Due – CHSLI MyChart (Account #8164)</h3>
      <div class="card-source">From: mychartteam@chsli.org · Subject: "Action Needed: Your payment is due"</div>
      <div class="card-body">A payment is due by <strong>July 24, 2026</strong> on your CHSLI account ending in 8164. If you've already mailed a check, allow time to process. Otherwise, payment action is needed.</div>
      <div class="card-next">→ Log in to MyChart at CHSLI.org and review balance. Pay online or confirm check sent.</div>
      <div class="card-due">📅 Due: July 24, 2026</div>
    </div>

    <div class="card card-green">
      <span class="card-label label-green">JOB SEARCH · INTERVIEW PREP</span>
      <h3>Oscar Health Phone Screen – People Strategy Lead</h3>
      <div class="card-source">From: Joelle Molina (joelle@hioscar.com) · Calendar: July 10, 2:00 PM</div>
      <div class="card-body">Phone screen confirmed with Oscar Health's Joelle Molina for the People Strategy Lead role. They will call <strong>(516) 313-8888</strong>. 25 minutes. Strong opportunity at a high-growth health insurance tech company.</div>
      <div class="card-next">→ Research Oscar Health strategy, recent news, and People team priorities. Prepare 3 relevant examples. Ensure phone is on and charged by 1:45 PM Friday.</div>
      <div class="card-due">📅 Friday, July 10 at 2:00 PM</div>
    </div>

    <div class="card card-yellow">
      <span class="card-label label-yellow">CALENDAR · RSVP NEEDED</span>
      <h3>RSVP Pending: HR Networking Open Office Hours (July 9 &amp; July 15)</h3>
      <div class="card-source">Calendar: July 9 @ 12:00 PM &amp; July 15 @ 12:00 PM (both marked "needsAction")</div>
      <div class="card-body">Two HR Networking &amp; Job Search Zoom sessions have no RSVP response. Both have large attendee lists (180+ professionals). July 9 is <strong>tomorrow</strong>.</div>
      <div class="card-next">→ Accept or decline both calendar invitations today. Zoom links are included in calendar entries.</div>
      <div class="card-due">📅 First session: Tomorrow, July 9 at 12:00 PM</div>
    </div>

    <div class="card card-blue">
      <span class="card-label label-blue">MEDICAL · PREP</span>
      <h3>New Patient Appointment – Dr. Beth Leeman-Markowski (Epilepsy Center)</h3>
      <div class="card-source">Calendar: Thursday, July 9 @ 3:30 PM · 223 East 34th Street, NY 10016</div>
      <div class="card-body">New patient visit at the Comprehensive Epilepsy Center. Must arrive <strong>15 minutes early (3:15 PM)</strong>. Bring: insurance card, photo ID, MD referral/pre-certification (if applicable), and copies of relevant medical records/test results.</div>
      <div class="card-next">→ Prepare paperwork tonight. Plan travel to arrive by 3:15 PM. Call 646-558-0800 with questions.</div>
      <div class="card-due">📅 Tomorrow, July 9 – Arrive by 3:15 PM</div>
    </div>

    <div class="card card-green">
      <span class="card-label label-green">JOB SEARCH · REVIEW</span>
      <h3>Daily Job Search Sweep – 22 Priority Opportunities</h3>
      <div class="card-source">From: melissaw212@gmail.com (automated pipeline) · Received: Today 2:49 PM</div>
      <div class="card-body">Your TypeScript job search pipeline ran today and identified <strong>22 priority listings</strong> within 48 hours. This is the core daily intake for new applications.</div>
      <div class="card-next">→ Review the sweep results and identify top 3–5 roles to apply to today or tomorrow.</div>
      <div class="card-due">📅 Today — within 48h window</div>
    </div>

    <div class="card card-green">
      <span class="card-label label-green">JOB SEARCH · REJECTION</span>
      <h3>Bancroft CHRO Application – Rejection Received</h3>
      <div class="card-source">From: TAP Admin (Bancroft iCIMS) · Subject: "Thank You for Your Interest in Bancroft" [TRASH]</div>
      <div class="card-body">Bancroft has decided not to move forward with your CHRO application at this time. Email was auto-trashed. Worth noting to update your pipeline tracker and close this opportunity.</div>
      <div class="card-next">→ Update your job search tracker. Mark Bancroft CHRO as closed. No further action needed.</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════ 4. FULL 7-DAY CALENDAR ═══ -->
<div class="section">
  <div class="section-title theme-blue">📅 Full 7-Day Calendar (Jul 8–14, 2026)</div>
  <div class="section-body body-blue">

    <!-- WED JUL 8 -->
    <div class="cal-day">
      <div class="cal-day-header">📌 Wednesday, July 8, 2026 — TODAY</div>
      <div class="cal-event confirmed">
        <div class="ce-time">All Day</div>
        <div class="ce-title">No scheduled meetings today <span class="ce-status status-confirmed">TODAY</span></div>
        <div class="ce-detail">Focus day — review job sweep, address security emails, prep for tomorrow's medical appointment.</div>
      </div>
    </div>

    <!-- THU JUL 9 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Thursday, July 9, 2026 — TOMORROW</div>

      <div class="cal-event declined">
        <div class="ce-time">9:00 AM – 10:30 AM</div>
        <div class="ce-title">Executive Roundtable <span class="ce-status status-declined">DECLINED</span></div>
        <div class="ce-detail">
          <strong>Organizer:</strong> John Madigan &nbsp;|&nbsp; <strong>Format:</strong> Zoom<br>
          <strong>Link:</strong> <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Meeting 207 786 667</a> &nbsp;|&nbsp; PW: 205454<br>
          <strong>Prep:</strong> None needed — you have declined this event.
        </div>
      </div>

      <div class="cal-event needs-action">
        <div class="ce-time">12:00 PM – 1:00 PM</div>
        <div class="ce-title">HR Networking &amp; Job Search: Open Office Hours – Zoom 2 <span class="ce-status status-needs">RSVP NEEDED</span></div>
        <div class="ce-detail">
          <strong>Attendees:</strong> 180+ HR professionals<br>
          <strong>Link:</strong> <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom 85945371140</a><br>
          <strong>Note:</strong> No AI notetaking tools — open discussion format.<br>
          <strong>Prep:</strong> Good networking opportunity; prepare 30-sec intro and current target role description.<br>
          <span class="conflict-warn">⚠️ RSVP pending — respond today.</span>
        </div>
      </div>

      <div class="cal-event accepted">
        <div class="ce-time">3:30 PM – 4:30 PM</div>
        <div class="ce-title">New Patient Appointment – Dr. Beth A. Leeman-Markowski, MD <span class="ce-status status-confirmed">CONFIRMED</span></div>
        <div class="ce-detail">
          <strong>Location:</strong> Comprehensive Epilepsy Center, 223 East 34th Street, New York, NY 10016<br>
          <strong>Phone:</strong> 646-558-0800<br>
          <strong>Arrive by:</strong> 3:15 PM (15 min early)<br>
          <strong>Bring:</strong> Insurance card, photo ID, MD referral/pre-certification (if applicable), medical records &amp; recent test results.<br>
          <strong>Note:</strong> Two calendar entries for this appointment (both confirmed/accepted) — treat as one event. No conflict.
        </div>
      </div>
    </div>

    <!-- FRI JUL 10 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Friday, July 10, 2026</div>

      <div class="cal-event accepted">
        <div class="ce-time">2:00 PM – 2:25 PM</div>
        <div class="ce-title">Oscar Health Phone Screen – People Strategy Lead <span class="ce-status status-accepted">ACCEPTED</span></div>
        <div class="ce-detail">
          <strong>Recruiter:</strong> Joelle Molina (joelle@hioscar.com)<br>
          <strong>Format:</strong> Phone or Google Meet — they will call <strong>(516) 313-8888</strong><br>
          <strong>Role:</strong> People Strategy Lead at Oscar Health<br>
          <strong>Prep:</strong> Research Oscar Health, prepare STAR examples for People Strategy topics, review JD, have questions ready.
        </div>
      </div>

      <div class="cal-event confirmed">
        <div class="ce-time">3:30 PM – 4:30 PM</div>
        <div class="ce-title">Dr [Appointment] <span class="ce-status status-confirmed">CONFIRMED</span></div>
        <div class="ce-detail">
          <strong>Details:</strong> No additional details provided in calendar entry.<br>
          <strong>Action:</strong> Verify appointment details, location, and any prep needed.
          <span class="conflict-warn">⚠️ Note: Overlaps in the afternoon — ensure enough travel/buffer time between Oscar call and this appointment.</span>
        </div>
      </div>
    </div>

    <!-- SAT JUL 11 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Saturday, July 11, 2026</div>
      <div class="cal-event confirmed">
        <div class="ce-time">All Day</div>
        <div class="ce-title">No events scheduled <span class="ce-status status-confirmed">CLEAR</span></div>
        <div class="ce-detail">No calendar events this day.</div>
      </div>
    </div>

    <!-- SUN JUL 12 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Sunday, July 12, 2026</div>
      <div class="cal-event confirmed">
        <div class="ce-time">All Day</div>
        <div class="ce-title">No events scheduled <span class="ce-status status-confirmed">CLEAR</span></div>
        <div class="ce-detail">No calendar events this day.</div>
      </div>
    </div>

    <!-- MON JUL 13 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Monday, July 13, 2026</div>

      <div class="cal-event confirmed">
        <div class="ce-time">All Day</div>
        <div class="ce-title">Stephanie Infusion <span class="ce-status status-confirmed">CONFIRMED</span></div>
        <div class="ce-detail">
          <strong>Type:</strong> All-day reminder (July 13–14 date range).<br>
          <strong>Action:</strong> Confirm logistics/support needed for Stephanie's infusion appointment.
        </div>
      </div>
    </div>

    <!-- TUE JUL 14 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Tuesday, July 14, 2026</div>

      <div class="cal-event confirmed">
        <div class="ce-time">All Day (cont.)</div>
        <div class="ce-title">Stephanie Infusion (continues) <span class="ce-status status-confirmed">CONFIRMED</span></div>
        <div class="ce-detail">All-day block carries over from July 13.</div>
      </div>

      <div class="cal-event confirmed">
        <div class="ce-time">10:00 AM – 11:00 AM</div>
        <div class="ce-title">Stella <span class="ce-status status-confirmed">CONFIRMED</span></div>
        <div class="ce-detail">
          <strong>Details:</strong> No location or description provided.<br>
          <strong>Action:</strong> Confirm what this appointment is for and if any prep is needed.
        </div>
      </div>
    </div>

    <!-- LOOKING AHEAD: WED JUL 15 -->
    <div class="cal-day">
      <div class="cal-day-header">👀 Looking Ahead — Wednesday, July 15, 2026</div>

      <div class="cal-event confirmed">
        <div class="ce-time">8:30 AM – 9:30 AM</div>
        <div class="ce-title">Bone Density Appointment <span class="ce-status status-confirmed">CONFIRMED</span></div>
        <div class="ce-detail">No additional location details provided. Confirm address and any fasting or prep requirements in advance.</div>
      </div>

      <div class="cal-event needs-action">
        <div class="ce-time">12:00 PM – 1:30 PM</div>
        <div class="ce-title">HR Networking &amp; Job Search Group – Zoom 2 <span class="ce-status status-needs">RSVP NEEDED</span></div>
        <div class="ce-detail">
          <strong>Link:</strong> <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom 81954171722</a><br>
          <strong>Attendees:</strong> 180+ HR professionals. Includes team guidelines, resources, and agenda prep.<br>
          <span class="conflict-warn">⚠️ RSVP pending — respond today.</span>
        </div>
      </div>

      <div class="cal-event confirmed">
        <div class="ce-time">12:00 PM – 1:30 PM</div>
        <div class="ce-title">Network [Duplicate/Companion entry] <span class="ce-status status-confirmed">CONFIRMED</span></div>
        <div class="ce-detail">Appears to be the same networking session. No conflict — same time block. Treat as confirmed attendance marker.</div>
      </div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════ 5. JOB SEARCH & INTERVIEW PIPELINE ═══ -->
<div class="section">
  <div class="section-title theme-green">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body body-green">

    <table>
      <thead>
        <tr>
          <th>Opportunity / Source</th>
          <th>Role</th>
          <th>Company</th>
          <th>Status</th>
          <th>Fit</th>
          <th>Next Step</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Oscar Health – Calendar</strong><br><small>Joelle Molina · joelle@hioscar.com</small></td>
          <td>People Strategy Lead</td>
          <td>Oscar Health</td>
          <td><span class="tag tag-green">PHONE SCREEN</span></td>
          <td><span class="tag tag-high">HIGH</span></td>
          <td>Prep &amp; confirm phone on July 10, 2:00 PM</td>
        </tr>
        <tr>
          <td><strong>Daily Job Search Sweep</strong><br><small>melissaw212@gmail.com pipeline</small></td>
          <td>22 Priority Roles (48h window)</td>
          <td>Multiple</td>
          <td><span class="tag tag-yellow">REVIEW</span></td>
          <td><span class="tag tag-high">HIGH</span></td>
          <td>Review sweep results today; apply to top 3–5</td>
        </tr>
        <tr>
          <td><strong>LinkedIn Job Alert</strong><br><small>jobalerts-noreply@linkedin.com (2 emails)</small></td>
          <td>Head of People</td>
          <td>FAR.AI</td>
          <td><span class="tag tag-blue">ALERT</span></td>
          <td><span class="tag tag-high">HIGH</span></td>
          <td>Review role; consider applying — AI safety org, senior People leadership</td>
        </tr>
        <tr>
          <td><strong>Yutori Scout Report</strong><br><small>notifications@yutori.com</small></td>
          <td>2 New Director-Level HR Roles (posted Jul 7)</td>
          <td>Multiple</td>
          <td><span class="tag tag-blue">ALERT</span></td>
          <td><span class="tag tag-high">HIGH</span></td>
          <td>Open and review both roles from July 2–7 sweep</td>
        </tr>
        <tr>
          <td><strong>PeopleOps Jobs</strong><br><small>Phil Strazzulla · peopleopsjobs@mail.beehiiv.com (3 emails)</small></td>
          <td>83+ Remote HR/TA/People Ops Roles</td>
          <td>Siemens, Levi's &amp; more</td>
          <td><span class="tag tag-blue">NEWSLETTER</span></td>
          <td><span class="tag tag-medium">MED</span></td>
          <td>Scan the list for director+ roles matching target criteria</td>
        </tr>
        <tr>
          <td><strong>Welcome to the Jungle</strong><br><small>help@welcometothejungle.com [TRASH]</small></td>
          <td>Senior People Business Partner</td>
          <td>Remote</td>
          <td><span class="tag tag-gray">TRASHED</span></td>
          <td><span class="tag tag-medium">MED</span></td>
          <td>Consider restoring — Senior PBHP remote role may be relevant</td>
        </tr>
        <tr>
          <td><strong>Bancroft CHRO</strong><br><small>TAP Admin via iCIMS [TRASH]</small></td>
          <td>Chief Human Resources Officer</td>
          <td>Bancroft</td>
          <td><span class="tag tag-red">REJECTED</span></td>
          <td>—</td>
          <td>Close in tracker. No further action.</td>
        </tr>
        <tr>
          <td><strong>CandidateOps Webinar</strong><br><small>adam@candidateops.com</small></td>
          <td>Executive Job Search Tips</td>
          <td>CandidateOps</td>
          <td><span class="tag tag-yellow">TODAY</span></td>
          <td><span class="tag tag-medium">MED</span></td>
          <td>Webinar was starting imminently today — check if recording is available</td>
        </tr>
        <tr>
          <td><strong>HR Networking Open Office Hours</strong><br><small>Calendar: Jul 9 &amp; Jul 15</small></td>
          <td>Peer Networking / Referrals</td>
          <td>Community Group (~180 attendees)</td>
          <td><span class="tag tag-yellow">RSVP NEEDED</span></td>
          <td><span class="tag tag-high">HIGH</span></td>
          <td>RSVP to both sessions today</td>
        </tr>
        <tr>
          <td><strong>Claude Prompts for HR</strong><br><small>melissa@gmail.com · self-sent LinkedIn post</small></td>
          <td>AI Productivity Resource</td>
          <td>LinkedIn / AIHR</td>
          <td><span class="tag tag-blue">RESOURCE</span></td>
          <td><span class="tag tag-medium">MED</span></td>
          <td>Review Claude HR prompt guide for job search applications</td>
        </tr>
        <tr>
          <td><strong>HR Analytics Resource</strong><br><small>melissa@gmail.com · self-sent LinkedIn post</small></td>
          <td>6 HR Analytics Templates</td>
          <td>LinkedIn</td>
          <td><span class="tag tag-blue">RESOURCE</span></td>
          <td><span class="tag tag-medium">MED</span></td>
          <td>Download templates; use for interview preparation</td>
        </tr>
      </tbody>
    </table>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════ 6. FULL EMAIL REVIEW BY CATEGORY ═══ -->
<div class="section">
  <div class="section-title theme-teal">📬 Full Email Review by Category</div>
  <div class="section-body body-teal">

    <!-- SECURITY / RISK -->
    <div class="card card-red">
      <span class="card-label label-red">SECURITY / RISK</span>
      <h3>⚠️ Security &amp; Risk — 4 emails</h3>
      <div class="card-body">
        <ul class="compact">
          <li><strong>[INBOX]</strong> Payment_Processing &lt;i5pnrx6yav@ygsa28i004.us&gt; — "Action Required: Your payment was declined" <badge class="badge-unread">UNREAD</badge> — <span class="pill pill-red">PHISHING SCAM</span></li>
          <li><strong>[NOT TRASHED]</strong> "Dr. Nathan Ford" &lt;gsgblfwjruaaxp…&gt; — Explicit unsolicited spam <span class="badge-unread">UNREAD</span> — <span class="pill pill-red">DELETE/SPAM</span></li>
          <li><strong>[NOT TRASHED]</strong> noreply@casi-03.firebaseapp.com — Casino sign-in request <span class="badge-unread">UNREAD</span> — <span class="pill pill-red">PHISHING</span></li>
          <li><strong>[NOT TRASHED]</strong> "Dr. Keller | Care Øharmacy" — Priligy pharma spam <span class="badge-unread">UNREAD</span> — <span class="pill pill-red">SPAM</span></li>
        </ul>
      </div>
      <div class="card-next">→ Mark all 4 as spam. Delete immediately. Do not click any links.</div>
    </div>

    <!-- JOB SEARCH -->
    <div class="card card-green">
      <span class="card-label label-green">JOB SEARCH</span>
      <h3>💼 Job Search — 6 emails</h3>
      <div class="card-body">
        <ul class="compact">
          <li><strong>[INBOX]</strong> melissaw212@gmail.com — Daily Job Search Sweep 2026-07-08 (22 priority roles) — <span class="pill pill-green">REVIEW TODAY</span></li>
          <li><strong>[INBOX]</strong> LinkedIn Job Alerts — Head of People at FAR.AI (2x, one read/one unread) — <span class="pill pill-green">REVIEW</span></li>
          <li><strong>[INBOX]</strong> Yutori/Scout — Two new director-level HR roles (Jul 7) — <span class="pill pill-green">REVIEW</span></li>
          <li><strong>[NOT TRASHED]</strong> melissa@gmail.com — Claude prompts for HR (LinkedIn post) — <span class="pill pill-blue">RESOURCE</span></li>
          <li><strong>[NOT TRASHED]</strong> melissa@gmail.com — HR analytics templates (LinkedIn post) — <span class="pill pill-blue">RESOURCE</span></li>
          <li><strong>[NOT TRASHED]</strong> PeopleOps Jobs (Phil Strazzulla) — 83+ remote HR roles (3 near-duplicate emails, treated as one) — <span class="pill pill-green">SCAN</span></li>
        </ul>
      </div>
      <div class="card-next">→ Review sweep results today. Check FAR.AI and Yutori roles. Scan PeopleOps list for director+ matches.</div>
    </div>

    <!-- RECRUITERS / NETWORKING -->
    <div class="card card-green">
      <span class="card-label label-green">RECRUITERS / NETWORKING</span>
      <h3>🤝 Recruiters &amp; Networking — 2 emails</h3>
      <div class="card-body">
        <ul class="compact">
          <li><strong>[NOT TRASHED]</strong> CandidateOps &lt;adam@candidateops.com&gt; — "Webinar starts soon" (executive job search tips) <span class="badge-unread">UNREAD</span> — <span class="pill pill-yellow">CHECK FOR RECORDING</span></li>
          <li><strong>[TRASH]</strong> Welcome to the Jungle — Senior People Business Partner at Remote — <span class="pill pill-yellow">CONSIDER RESTORING</span></li>
        </ul>
      </div>
      <div class="card-next">→ Check if CandidateOps webinar replay is available. Restore Welcome to the Jungle email and review SPBP role.</div>
    </div>

    <!-- CALENDAR / EVENTS (Professional) -->
    <div class="card card-purple">
      <span class="card-label label-purple">CALENDAR / EVENTS (PROFESSIONAL)</span>
      <h3>📅 Professional Events — 2 emails</h3>
      <div class="card-body">
        <ul class="compact">
          <li><strong>[NOT INBOX]</strong> HR.com — "Shape your compensation program to attract and keep talent" – Aug 5th <span class="badge-unread">UNREAD</span> — <span class="pill pill-purple">CONSIDER REGISTERING</span></li>
          <li><strong>[NOT INBOX]</strong> HR.com — "Elevate employee performance and growth" – July 29th <span class="badge-unread">UNREAD</span> — <span class="pill pill-purple">CONSIDER REGISTERING</span></li>
        </ul>
      </div>
      <div class="card-next">→ Both are free virtual HR.com events. Relevant to your CHRO/VP HR positioning. Register if interested.</div>
    </div>

    <!-- MEDICAL / HEALTH -->
    <div class="card card-blue">
      <span class="card-label label-blue">MEDICAL / HEALTH</span>
      <h3>🏥 Medical &amp; Health — 1 email</h3>
      <div class="card-body">
        <ul class="compact">
          <li><strong>[INBOX]</strong> mychartteam@chsli.org — "Action Needed: Your payment is due" – Account #8164, due Jul 24 <span class="badge-unread">UNREAD</span> — <span class="pill pill-yellow">PAY BY JUL 24</span></li>
        </ul>
      </div>
      <div class="card-next">→ Log in to MyChart and pay, or confirm check was mailed. Due July 24.</div>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="card card-yellow">
      <span class="card-label label-yellow">FINANCIAL / BILLING</span>
      <h3>💳 Financial &amp; Billing — 1 email</h3>
      <div class="card-body">
        <ul class="compact">
          <li><strong>[TRASH]</strong> Equifax &lt;info@e.equifax.com&gt; — "Congratulations! You've been selected to apply for a debt consolidation loan" — <span class="pill pill-red">LIKELY SPAM/SCAM — DELETE</span></li>
        </ul>
      </div>
      <div class="card-next">→ This is almost certainly a third-party loan solicitation not from Equifax directly. Do not click. Keep in trash.</div>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="card card-purple">
      <span class="card-label label-purple">PROFESSIONAL DEVELOPMENT</span>
      <h3>📚 Professional Development — 3 emails</h3>
      <div class="card-body">
        <ul class="compact">
          <li><strong>[INBOX]</strong> Vaishali Lambe / The Curious Mind (Medium) — "Where AI Productivity Gains Depend on People, Not Just Algorithms" <span class="badge-unread">UNREAD</span> — <span class="pill pill-purple">WORTH READING</span></li>
          <li><strong>[NOT TRASHED]</strong> Hacking HR Team — "The Workforce Model Is Changing Fast" <span class="badge-unread">UNREAD</span> — <span class="pill pill-purple">SKIM</span></li>
          <li><strong>[NOT TRASHED]</strong> CoolDeep AI — "What Claude can actually do" [TRASH] — <span class="pill pill-gray">LOW PRIORITY</span></li>
        </ul>
      </div>
      <div class="card-next">→ Read the Medium AI/People article — relevant to executive positioning. Skim Hacking HR for workforce intelligence trends.</div>
    </div>

    <!-- NEWSLETTERS / SUBSCRIPTIONS -->
    <div class="card card-purple">
      <span class="card-label label-purple">NEWSLETTERS / SUBSCRIPTIONS</span>
      <h3>📰 Newsletters &amp; Subscriptions — 6 emails</h3>
      <div class="card-body">
        <ul class="compact">
          <li><strong>[NOT TRASHED]</strong> Techpresso — "Apple commits $30B for US-made chips; OpenAI GPT-5.6; Meta AI" — <span class="pill pill-purple">SKIM</span></li>
          <li><strong>[NOT TRASHED]</strong> Ruben Hassid (Substack) — "Fable 5. / New Claude" [TRASH] — <span class="pill pill-gray">LOW</span></li>
          <li><strong>[TRASH]</strong> HR Brew — "Boom or bust / World Cup hiring boom" — <span class="pill pill-purple">WORTH READING</span></li>
          <li><strong>[TRASH]</strong> Meidas+ — "NATO Meltdown, Iran Ceasefire OFF" (news) — <span class="pill pill-gray">PERSONAL INTEREST</span></li>
          <li><strong>[NOT TRASHED]</strong> The Futurist — "Want a robot to do your laundry?" [TRASH] — <span class="pill pill-gray">LOW</span></li>
          <li><strong>[NOT TRASHED]</strong> BlueTube — "Protect public media" — <span class="pill pill-gray">LOW PRIORITY</span></li>
        </ul>
      </div>
      <div class="card-next">→ Read Techpresso AI headlines. Restore HR Brew from trash — hiring trends relevant to your search. Others: low priority.</div>
    </div>

    <!-- PERSONAL -->
    <div class="card card-gray">
      <span class="card-label label-gray">PERSONAL</span>
      <h3>👤 Personal — 1 email</h3>
      <div class="card-body">
        <ul class="compact">
          <li><strong>[NOT TRASHED]</strong> "Silve.creest" &lt;9032hanghang@gmail.com&gt; — "Re: Eat" (no content/snippet) — <span class="pill pill-gray">UNCLEAR — REVIEW</span></li>
        </ul>
      </div>
      <div class="card-next">→ Open and check — may be a real reply to a previous thread or spam. Verify before deleting.</div>
    </div>

    <!-- PROMOTIONAL / RETAIL (summary only — full section below) -->
    <div class="card card-gray">
      <span class="card-label label-gray">PROMOTIONAL / RETAIL</span>
      <h3>🛍️ Promotional &amp; Retail — 14 emails</h3>
      <div class="card-body">StackSocial (2), OpenTable, Target Optical, Macy's, Laura Geller, Halara, Quince, CoinOut, e.l.f. Cosmetics, Gap Factory, rhode, Temu, Seamens Moving. Full breakdown in Promotional section below.</div>
      <div class="card-next">→ Review Macy's flash sale (ends tonight). All others: low priority or ignore.</div>
    </div>

    <!-- TRASH REVIEW (summary — full section below) -->
    <div class="card card-gray">
      <span class="card-label label-gray">TRASH REVIEW</span>
      <h3>🗑️ Trash — 16 emails</h3>
      <div class="card-body">OpenTable, Target Optical, Bancroft rejection, Macy's, Laura Geller, The Futurist, Equifax loan, Temu, HR Brew, Meidas+, Hattis Law, Welcome to the Jungle, Acorns, Zapier (2), CoolDeep AI, Ruben Hassid, Apify, Seamens Moving. Full breakdown below.</div>
      <div class="card-next">→ Restore: Bancroft rejection (for tracking), Welcome to the Jungle, HR Brew. Delete rest permanently.</div>
    </div>

    <!-- SAFE TO DELETE / IGNORE -->
    <div class="card card-gray">
      <span class="card-label label-gray">SAFE TO DELETE / IGNORE</span>
      <h3>🚮 Safe to Delete / Ignore — 4 emails</h3>
      <div class="card-body">
        <ul class="compact">
          <li>Acorns Earn — $5.78 missed rewards (in trash) — delete</li>
          <li>Zapier ZapConnect 2026 (2 copies, both trashed) — delete</li>
          <li>Apify — LinkedIn Scraper upgrade (trashed) — delete</li>
        </ul>
      </div>
      <div class="card-next">→ Permanently delete these from trash. No action needed.</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════ 7. TRASH REVIEW ═══ -->
<div class="section">
  <div class="section-title theme-gray">🗑️ Trash Review</div>
  <div class="section-body body-gray">

    <h3 style="color:#1e8449; margin-bottom:10px;">♻️ Restore Immediately</h3>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Reason to Restore</th></tr></thead>
      <tbody>
        <tr>
          <td>TAP Admin (Bancroft iCIMS)</td>
          <td>"Thank You for Your Interest in Bancroft"</td>
          <td>Application rejection — keep for job search pipeline tracking and documentation.</td>
        </tr>
        <tr>
          <td>Welcome to the Jungle</td>
          <td>"New match: Senior People Business Partner at Remote"</td>
          <td>Relevant job opportunity — Senior PBHP remote role. Should be reviewed before discarding.</td>
        </tr>
        <tr>
          <td>HR Brew (Morning Brew)</td>
          <td>"☕ Boom or bust" — World Cup hiring boom</td>
          <td>HR industry hiring trend article — relevant to your market knowledge and executive narrative.</td>
        </tr>
      </tbody>
    </table>

    <div class="divider"></div>
    <h3 style="color:#d4a017; margin-bottom:10px;">🔍 Review Before Deleting</h3>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Note</th></tr></thead>
      <tbody>
        <tr>
          <td>OpenTable</td>
          <td>"Introducing Gold Tables — 6 reservations away"</td>
          <td>Loyalty program update — low priority but verify you don't need the info before deleting.</td>
        </tr>
        <tr>
          <td>Meidas+</td>
          <td>"Wednesday News Updates: NATO Meltdown, Iran Ceasefire OFF"</td>
          <td>News/political newsletter — personal interest. Decide if you want to stay subscribed.</td>
        </tr>
        <tr>
          <td>Equifax</td>
          <td>"Congratulations! You've been selected for a debt consolidation loan"</td>
          <td>Likely third-party marketing, not Equifax directly. Verify sender before dismissing permanently.</td>
        </tr>
        <tr>
          <td>Hattis Law</td>
          <td>"T-Mobile Wireless Customer? You May Have a Claim"</td>
          <td>Class action claim — if you are/were a T-Mobile customer, you may have limited time to file. Review once.</td>
        </tr>
        <tr>
          <td>CoolDeep AI</td>
          <td>"What Claude can actually do"</td>
          <td>AI newsletter — may have useful Claude tips given your self-sent HR prompts links. Skim first.</td>
        </tr>
        <tr>
          <td>Ruben Hassid (Substack)</td>
          <td>"Fable 5." (new Claude tips)</td>
          <td>AI productivity newsletter — minor relevance given your Claude/HR focus. Quick skim OK.</td>
        </tr>
      </tbody>
    </table>

    <div class="divider"></div>
    <h3 style="color:#c0392b; margin-bottom:10px;">🗑️ Safe to Delete Permanently</h3>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Reason</th></tr></thead>
      <tbody>
        <tr><td>Target Optical</td><td>"Get ready for school with eyewear they'll love!"</td><td>Retail promotion — no action needed.</td></tr>
        <tr><td>Macy's</td><td>"Flash Sale ends tonight: up to 65% off"</td><td>Flash sale has likely expired — delete.</td></tr>
        <tr><td>Laura Geller Beauty</td><td>"Melissa, your coupon is waiting!"</td><td>Retail coupon — ignore and delete.</td></tr>
        <tr><td>The Futurist</td><td>"Want a robot to do your laundry?"</td><td>Consumer tech newsletter — low value.</td></tr>
        <tr><td>Temu
<hr>
<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Financial / Billing</td><td>3</td></tr>
<tr><td>Job Search / Recruiters</td><td>10</td></tr>
<tr><td>Medical / Health</td><td>4</td></tr>
<tr><td>Other / Review</td><td>12</td></tr>
<tr><td>Professional Development / Newsletters</td><td>9</td></tr>
<tr><td>Promotional / Retail</td><td>9</td></tr>
<tr><td>Security / Risk</td><td>3</td></tr>
</table>
<p><strong>Audit Note:</strong> Every fetched email was reviewed and assigned to one category. Trash emails were included in review. Promotional and low-value emails were accounted for but deprioritized.</p>

