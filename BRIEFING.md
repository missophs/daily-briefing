<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing – Melissa | June 15, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .container { max-width: 1100px; margin: 0 auto; padding: 20px; }

  /* Header */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); color: white; border-radius: 12px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 300; letter-spacing: 1px; margin-bottom: 6px; }
  .header h2 { font-size: 16px; font-weight: 400; opacity: 0.75; margin-bottom: 16px; }
  .header-stats { display: flex; gap: 24px; flex-wrap: wrap; margin-top: 16px; }
  .header-stat { background: rgba(255,255,255,0.12); border-radius: 8px; padding: 10px 18px; text-align: center; }
  .header-stat .num { font-size: 22px; font-weight: 700; }
  .header-stat .lbl { font-size: 11px; opacity: 0.75; text-transform: uppercase; letter-spacing: 0.5px; }

  /* Section */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; border-left: 5px solid #0f3460; padding-left: 12px; margin-bottom: 16px; color: #0f3460; }

  /* Executive Summary */
  .exec-summary { background: white; border-radius: 10px; padding: 20px 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .exec-bullet { display: flex; align-items: flex-start; gap: 12px; padding: 10px 0; border-bottom: 1px solid #f0f0f0; }
  .exec-bullet:last-child { border-bottom: none; }
  .exec-badge { border-radius: 6px; padding: 4px 10px; font-size: 11px; font-weight: 700; text-transform: uppercase; white-space: nowrap; }
  .badge-red { background: #fde8e8; color: #c0392b; }
  .badge-green { background: #e8f8f0; color: #1e8449; }
  .badge-blue { background: #e8f0fe; color: #1a6bbf; }
  .badge-yellow { background: #fef9e7; color: #b7770d; }
  .badge-purple { background: #f3e8fd; color: #7d3c98; }
  .badge-gray { background: #f2f3f4; color: #5d6d7e; }

  /* Cards */
  .card { border-radius: 10px; padding: 18px 20px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.07); }
  .card-red { background: #fff5f5; border-left: 5px solid #e74c3c; }
  .card-yellow { background: #fffdf0; border-left: 5px solid #f1c40f; }
  .card-blue { background: #f0f6ff; border-left: 5px solid #2980b9; }
  .card-green { background: #f0fff8; border-left: 5px solid #27ae60; }
  .card-purple { background: #fdf0ff; border-left: 5px solid #8e44ad; }
  .card-gray { background: #f8f9fa; border-left: 5px solid #95a5a6; }
  .card-title { font-size: 15px; font-weight: 700; margin-bottom: 6px; }
  .card-meta { font-size: 12px; color: #666; margin-bottom: 6px; }
  .card-row { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 4px; }
  .card-label { font-size: 11px; font-weight: 700; text-transform: uppercase; color: #888; min-width: 120px; }
  .card-value { font-size: 13px; color: #1a1a2e; }
  .card-action { margin-top: 10px; background: rgba(0,0,0,0.04); border-radius: 6px; padding: 8px 12px; font-size: 13px; }
  .card-action strong { color: #0f3460; }

  /* Tables */
  table { width: 100%; border-collapse: collapse; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  th { background: #0f3460; color: white; padding: 10px 14px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
  td { padding: 10px 14px; border-bottom: 1px solid #f0f0f0; font-size: 13px; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #fafbfc; }
  .pill { display: inline-block; border-radius: 12px; padding: 2px 10px; font-size: 11px; font-weight: 700; }
  .pill-red { background: #fde8e8; color: #c0392b; }
  .pill-green { background: #e8f8f0; color: #1e8449; }
  .pill-yellow { background: #fef9e7; color: #b7770d; }
  .pill-blue { background: #e8f0fe; color: #1a6bbf; }
  .pill-purple { background: #f3e8fd; color: #7d3c98; }
  .pill-gray { background: #f2f3f4; color: #5d6d7e; }
  .pill-orange { background: #fef0e6; color: #ca6f1e; }

  /* Calendar */
  .cal-day { background: white; border-radius: 10px; margin-bottom: 16px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .cal-day-header { background: #0f3460; color: white; padding: 10px 18px; font-weight: 700; font-size: 14px; }
  .cal-day-header.today { background: linear-gradient(90deg, #1a6bbf, #0f3460); }
  .cal-event { padding: 14px 18px; border-bottom: 1px solid #f0f0f0; }
  .cal-event:last-child { border-bottom: none; }
  .cal-event-time { font-weight: 700; color: #0f3460; font-size: 13px; margin-bottom: 4px; }
  .cal-event-title { font-size: 15px; font-weight: 700; margin-bottom: 6px; }
  .cal-event-row { display: flex; gap: 6px; align-items: flex-start; margin-bottom: 3px; font-size: 12px; color: #555; }
  .cal-event-label { font-weight: 700; min-width: 80px; color: #888; }
  .conflict-warn { background: #fde8e8; border-radius: 6px; padding: 5px 10px; font-size: 12px; color: #c0392b; margin-top: 6px; }

  /* Dashboard grid */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; }
  .dash-card { background: white; border-radius: 10px; padding: 16px 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); text-align: center; }
  .dash-card .big-num { font-size: 36px; font-weight: 800; }
  .dash-card .dash-label { font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; color: #666; margin-top: 4px; }
  .dash-red .big-num { color: #e74c3c; }
  .dash-green .big-num { color: #27ae60; }
  .dash-blue .big-num { color: #2980b9; }
  .dash-yellow .big-num { color: #b7770d; }
  .dash-purple .big-num { color: #8e44ad; }
  .dash-gray .big-num { color: #7f8c8d; }

  /* Priority today */
  .priority-block { background: linear-gradient(135deg, #0f3460, #1a6bbf); color: white; border-radius: 10px; padding: 24px 28px; }
  .priority-item { display: flex; align-items: flex-start; gap: 16px; padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.15); }
  .priority-item:last-child { border-bottom: none; }
  .priority-num { font-size: 28px; font-weight: 800; opacity: 0.5; min-width: 36px; }
  .priority-text { font-size: 15px; }
  .priority-text strong { font-size: 16px; display: block; margin-bottom: 3px; }

  /* Misc */
  .trash-group-title { font-weight: 700; font-size: 14px; margin: 14px 0 8px; color: #0f3460; }
  .email-row { display: flex; align-items: flex-start; gap: 8px; padding: 6px 0; border-bottom: 1px solid #f5f5f5; font-size: 13px; }
  .email-row:last-child { border-bottom: none; }
  .email-sender { font-weight: 600; min-width: 180px; color: #1a1a2e; }
  .email-subject { color: #444; flex: 1; }
  .email-tag { font-size: 11px; font-weight: 700; border-radius: 4px; padding: 2px 7px; white-space: nowrap; }
  .tag-restore { background: #e8f8f0; color: #1e8449; }
  .tag-review { background: #fef9e7; color: #b7770d; }
  .tag-delete { background: #fde8e8; color: #c0392b; }
  .note-box { background: #e8f0fe; border-radius: 8px; padding: 12px 16px; font-size: 13px; color: #1a6bbf; margin-top: 10px; }
  .total-row td { font-weight: 700; background: #eef2f7 !important; color: #0f3460; }
  .scam-warn { background: #fde8e8; border: 1px solid #e74c3c; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #c0392b; margin-top: 8px; }
  .section-divider { border: none; border-top: 2px solid #e8ecf0; margin: 28px 0; }
  .inline-badge { border-radius: 4px; padding: 2px 8px; font-size: 11px; font-weight: 700; }
</style>
</head>
<body>
<div class="container">

<!-- ═══════════════════════════════════════════════════════════════
     1. HEADER
═══════════════════════════════════════════════════════════════ -->
<div class="header">
  <h1>Good Morning, Melissa ☀️</h1>
  <h2>Executive Briefing — Monday, June 15, 2026</h2>
  <div class="header-stats">
    <div class="header-stat"><div class="num">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="header-stat"><div class="num">8</div><div class="lbl">Calendar Events</div></div>
    <div class="header-stat"><div class="num">2</div><div class="lbl">Interviews Today</div></div>
    <div class="header-stat"><div class="num">1</div><div class="lbl">Security Alert</div></div>
    <div class="header-stat"><div class="num">3</div><div class="lbl">RSVPs Needed</div></div>
    <div class="header-stat"><div class="num">29</div><div class="lbl">Trash Emails</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     2. EXECUTIVE SUMMARY
═══════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">Executive Summary</div>
  <div class="exec-summary">
    <div class="exec-bullet">
      <span class="exec-badge badge-red">🔴 URGENT RISK</span>
      <div>A <strong>highly suspicious phishing/scam email</strong> from a spoofed "Payment_Declined" sender is sitting in your inbox (not trash) warning of a blocked account and cloud storage suspension. Do <em>not</em> click any links — this is almost certainly a phishing attack. Delete immediately and verify your Google and cloud storage accounts are secure.</div>
    </div>
    <div class="exec-bullet">
      <span class="exec-badge badge-green">🟢 JOB SEARCH</span>
      <div>You have <strong>two confirmed job interviews today</strong>: a 15-min consultation with Netta Jenkins at 1:45 PM (Zoom, status: tentative — confirm ASAP) and a <strong>screen for Principal People Business Partner, Finance at SoFi</strong> at 2:30 PM (confirmed). Also in your inbox: a Yutori Scout alert with 2 new Director+ HR/People roles posted today, and a LinkedIn alert for a People Partner, Sales role at Figma.</div>
    </div>
    <div class="exec-bullet">
      <span class="exec-badge badge-blue">🔵 CALENDAR</span>
      <div>Three upcoming events need your RSVP or attention: <strong>HR Networking &amp; Job Search Group on Tue Jun 17</strong> (needsAction), <strong>HR Networking Open Office Hours on Thu Jun 18</strong> (needsAction), and <strong>Executive Roundtable on Thu Jun 18</strong> (currently declined — verify intent). Also: Warby Parker flagged your <strong>prescription is about to expire</strong> — schedule an eye appointment soon.</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     3. ACTION REQUIRED
═══════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">⚡ Action Required</div>

  <!-- Phishing -->
  <div class="card card-red">
    <div class="card-title">🚨 PHISHING / SCAM — Delete Immediately</div>
    <div class="card-row"><span class="card-label">Source:</span><span class="card-value">"Payment_Declined©" &lt;dyimcwyhldplyl...&gt;</span></div>
    <div class="card-row"><span class="card-label">Subject:</span><span class="card-value">⚠️ WARNING: Failure Notice — We've Blocked Your Account!</span></div>
    <div class="card-row"><span class="card-label">Why It Matters:</span><span class="card-value">This is a classic phishing/account-hijacking attempt. The sender address is randomly generated. It is NOT in Trash — it is sitting in your email storage. Claims your cloud storage is blocked and billing needs updating. Do not click.</span></div>
    <div class="card-action"><strong>Next Step:</strong> Delete this email. Do NOT click any links. Verify your Google account at myaccount.google.com and confirm your storage/billing are unaffected.</div>
    <div class="card-row"><span class="card-label">Due:</span><span class="card-value"><strong>Immediately</strong></span></div>
  </div>

  <!-- Netta Jenkins -->
  <div class="card card-yellow">
    <div class="card-title">📅 RSVP Needed — Confirm Netta Jenkins Consultation Today</div>
    <div class="card-row"><span class="card-label">Source:</span><span class="card-value">Google Calendar — netta@hicconsult.com</span></div>
    <div class="card-row"><span class="card-label">Time:</span><span class="card-value">1:45 PM – 2:00 PM EDT TODAY</span></div>
    <div class="card-row"><span class="card-label">Status:</span><span class="card-value"><span class="pill pill-yellow">Tentative</span> — needs confirmation</span></div>
    <div class="card-row"><span class="card-label">Why It Matters:</span><span class="card-value">15-minute Zoom consultation — likely networking/consulting discussion. Your status is tentative. Given you have a SoFi interview at 2:30 PM the same day, the 1:45 PM slot leaves only 30 minutes buffer — confirm you're good on timing.</span></div>
    <div class="card-action"><strong>Next Step:</strong> Accept the calendar invite. Zoom: https://us06web.zoom.us/j/5224221004 | Password: 424726</div>
    <div class="card-row"><span class="card-label">Due:</span><span class="card-value"><strong>Today, before 1:45 PM</strong></span></div>
  </div>

  <!-- SoFi Interview -->
  <div class="card card-green">
    <div class="card-title">🎯 Interview Today — Principal People Business Partner, Finance @ SoFi</div>
    <div class="card-row"><span class="card-label">Source:</span><span class="card-value">Google Calendar — Interview with SoFi</span></div>
    <div class="card-row"><span class="card-label">Time:</span><span class="card-value">2:30 PM – 2:50 PM EDT TODAY</span></div>
    <div class="card-row"><span class="card-label">Status:</span><span class="card-value"><span class="pill pill-green">Confirmed</span></span></div>
    <div class="card-row"><span class="card-label">Why It Matters:</span><span class="card-value">This is a confirmed Zoom screen interview at SoFi for a Principal HRBP Finance role — a high-fit, senior opportunity. 20-minute screen — prep concise STAR stories and key fintech/finance HRBP experience points.</span></div>
    <div class="card-action"><strong>Next Step:</strong> Prep 2–3 STAR stories. Research SoFi's recent growth/news. Log on 5 min early to the Zoom link (check calendar event). Send a thank-you note immediately after.</div>
    <div class="card-row"><span class="card-label">Due:</span><span class="card-value"><strong>Today at 2:30 PM EDT</strong></span></div>
  </div>

  <!-- Yutori Scout -->
  <div class="card card-green">
    <div class="card-title">📋 New Job Leads — 2 Director+ HR/People Roles (Yutori Scout)</div>
    <div class="card-row"><span class="card-label">Source:</span><span class="card-value">Yutori &lt;notifications@yutori.com&gt; — In Inbox</span></div>
    <div class="card-row"><span class="card-label">Subject:</span><span class="card-value">[Scout] Two New Director+ HR/People Roles (June 15)</span></div>
    <div class="card-row"><span class="card-label">Why It Matters:</span><span class="card-value">Fresh Director-and-above HR/People roles posted today, June 15. Rolling 3-day scan — these are the newest listings. Act quickly before competition builds.</span></div>
    <div class="card-action"><strong>Next Step:</strong> Open email, review both roles, apply or save within 24 hours for best visibility.</div>
    <div class="card-row"><span class="card-label">Due:</span><span class="card-value"><strong>Today / Tomorrow</strong></span></div>
  </div>

  <!-- LinkedIn Figma -->
  <div class="card card-green">
    <div class="card-title">💼 Job Alert — People Partner, Sales @ Figma</div>
    <div class="card-row"><span class="card-label">Source:</span><span class="card-value">LinkedIn Job Alerts — In Inbox</span></div>
    <div class="card-row"><span class="card-label">Why It Matters:</span><span class="card-value">Figma is a high-growth tech company. People Partner, Sales is a strong HRBP match. LinkedIn job alerts are time-sensitive — roles fill quickly.</span></div>
    <div class="card-action"><strong>Next Step:</strong> Review the full job description. If fit is strong, apply today or save to pipeline and apply by Wednesday.</div>
    <div class="card-row"><span class="card-label">Due:</span><span class="card-value"><strong>This week</strong></span></div>
  </div>

  <!-- Virginie LinkedIn Message -->
  <div class="card card-yellow">
    <div class="card-title">💬 Unread LinkedIn Message — Virginie Glaenzer</div>
    <div class="card-row"><span class="card-label">Source:</span><span class="card-value">Virginie Glaenzer via LinkedIn (messaging digest)</span></div>
    <div class="card-row"><span class="card-label">Why It Matters:</span><span class="card-value">A LinkedIn message is awaiting your response. In an active job search, prompt responses to network contacts are important. Could be a lead, referral, or collaboration.</span></div>
    <div class="card-action"><strong>Next Step:</strong> Log into LinkedIn and respond to Virginie's message today.</div>
    <div class="card-row"><span class="card-label">Due:</span><span class="card-value"><strong>Today</strong></span></div>
  </div>

  <!-- Warby Parker Rx -->
  <div class="card card-yellow">
    <div class="card-title">👓 Prescription Expiring — Warby Parker Reminder</div>
    <div class="card-row"><span class="card-label">Source:</span><span class="card-value">Warby Parker &lt;sayhello@mail1.warbyparker.com&gt;</span></div>
    <div class="card-row"><span class="card-label">Why It Matters:</span><span class="card-value">Your eye prescription is about to expire. If you wear contacts or glasses, you'll need an up-to-date prescription to reorder. Both Warby Parker and Target Optical have contacted you about contacts/lenses this week.</span></div>
    <div class="card-action"><strong>Next Step:</strong> Schedule an eye exam this week. Call your optometrist or book online at Target Optical or Warby Parker.</div>
    <div class="card-row"><span class="card-label">Due:</span><span class="card-value"><strong>This week</strong></span></div>
  </div>

  <!-- HR Networking RSVPs -->
  <div class="card card-blue">
    <div class="card-title">📅 RSVP Needed — HR Networking Events (Jun 17 & 18)</div>
    <div class="card-row"><span class="card-label">Source:</span><span class="card-value">Google Calendar</span></div>
    <div class="card-row"><span class="card-label">Events:</span><span class="card-value">Jun 17 (Tue) 12–1:30 PM: HR Networking &amp; Job Search Group — Zoom 2 | Jun 18 (Thu) 12–1 PM: HR Networking Open Office Hours — Zoom 2</span></div>
    <div class="card-row"><span class="card-label">Status:</span><span class="card-value"><span class="pill pill-yellow">Needs Action</span> on both</span></div>
    <div class="card-action"><strong>Next Step:</strong> Accept or decline both calendar invites. These are large HR networking groups — strong job search value. Recommend accepting.</div>
    <div class="card-row"><span class="card-label">Due:</span><span class="card-value"><strong>Before Jun 17</strong></span></div>
  </div>

  <!-- Self-sent GitHub link -->
  <div class="card card-blue">
    <div class="card-title">🔗 Self-Sent Note — GitHub claude-mem Project</div>
    <div class="card-row"><span class="card-label">Source:</span><span class="card-value">Melissa W &lt;melissaw212@gmail.com&gt; — In Inbox</span></div>
    <div class="card-row"><span class="card-label">Why It Matters:</span><span class="card-value">You emailed yourself a GitHub link to "claude-mem" — a tool for persistent AI context across sessions. This was likely intentional and deserves a follow-up review when time permits.</span></div>
    <div class="card-action"><strong>Next Step:</strong> Review the GitHub repo when you have 15 minutes. Assess if this is relevant to a current project or AI workflow.</div>
    <div class="card-row"><span class="card-label">Due:</span><span class="card-value"><strong>This week</strong></span></div>
  </div>
</div>

<hr class="section-divider">

<!-- ═══════════════════════════════════════════════════════════════
     4. FULL 7-DAY CALENDAR
═══════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📅 Full 7-Day Calendar</div>

  <!-- Monday June 15 -->
  <div class="cal-day">
    <div class="cal-day-header today">📍 TODAY — Monday, June 15, 2026</div>

    <div class="cal-event">
      <div class="cal-event-time">1:45 PM – 2:00 PM EDT</div>
      <div class="cal-event-title">Melissa weoss and Netta Jenkins — 15 Min Consultation</div>
      <div class="cal-event-row"><span class="cal-event-label">Status:</span><span class="pill pill-yellow">Tentative — RSVP Needed</span></div>
      <div class="cal-event-row"><span class="cal-event-label">Location:</span><span>Zoom: https://us06web.zoom.us/j/5224221004 | Password: 424726</span></div>
      <div class="cal-event-row"><span class="cal-event-label">Attendees:</span><span>netta@hicconsult.com</span></div>
      <div class="cal-event-row"><span class="cal-event-label">Prep:</span><span>Know your ask — consulting inquiry, networking, or role discussion? Prepare 1-min intro and 2 key questions.</span></div>
      <div class="conflict-warn">⚠️ Back-to-back with SoFi interview at 2:30 PM — only 30-minute buffer. End on time.</div>
    </div>

    <div class="cal-event">
      <div class="cal-event-time">2:30 PM – 2:50 PM EDT</div>
      <div class="cal-event-title">Interview with SoFi — Principal People Business Partner, Finance</div>
      <div class="cal-event-row"><span class="cal-event-label">Status:</span><span class="pill pill-green">Confirmed</span></div>
      <div class="cal-event-row"><span class="cal-event-label">Location:</span><span>Zoom — check calendar invite for link</span></div>
      <div class="cal-event-row"><span class="cal-event-label">Prep:</span><span>Research SoFi (fintech, IPO, growth stage). Prepare 2–3 STAR stories around Finance HRBP work, M&A, and scaling teams. Have questions ready. Send thank-you within 1 hour post-call.</span></div>
      <div class="cal-event-row"><span class="cal-event-label">Priority:</span><span><span class="pill pill-green">HIGH — Senior Role</span></span></div>
    </div>
  </div>

  <!-- Tuesday June 16 -->
  <div class="cal-day">
    <div class="cal-day-header">Tuesday, June 16, 2026</div>
    <div class="cal-event">
      <div class="cal-event-time">10:00 AM – 11:00 AM EDT</div>
      <div class="cal-event-title">Vet Appointment</div>
      <div class="cal-event-row"><span class="cal-event-label">Status:</span><span class="pill pill-green">Confirmed</span></div>
      <div class="cal-event-row"><span class="cal-event-label">Location:</span><span>No address listed — confirm location in advance</span></div>
      <div class="cal-event-row"><span class="cal-event-label">Prep:</span><span>Confirm address and bring pet health records. Allow extra time if traveling with a pet.</span></div>
    </div>
  </div>

  <!-- Wednesday June 17 -->
  <div class="cal-day">
    <div class="cal-day-header">Wednesday, June 17, 2026</div>

    <div class="cal-event">
      <div class="cal-event-time">10:45 AM – 11:45 AM EDT</div>
      <div class="cal-event-title">Dental Cleaning — Dr. Deutch</div>
      <div class="cal-event-row"><span class="cal-event-label">Status:</span><span class="pill pill-green">Confirmed</span></div>
      <div class="cal-event-row"><span class="cal-event-label">Location:</span><span>No address listed — confirm office address and parking</span></div>
      <div class="cal-event-row"><span class="cal-event-label">Prep:</span><span>Confirm appointment. Allow 15 min for transit/parking.</span></div>
    </div>

    <div class="cal-event">
      <div class="cal-event-time">12:00 PM – 1:30 PM EDT</div>
      <div class="cal-event-title">HR Networking &amp; Job Search Group — Zoom 2</div>
      <div class="cal-event-row"><span class="cal-event-label">Status:</span><span class="pill pill-yellow">Needs Action — RSVP</span></div>
      <div class="cal-event-row"><span class="cal-event-label">Location:</span><span>Zoom: https://us06web.zoom.us/j/81954171722</span></div>
      <div class="cal-event-row"><span class="cal-event-label">Attendees:</span><span>Large group (~100+ HR professionals)</span></div>
      <div class="cal-event-row"><span class="cal-event-label">Prep:</span><span>Review group guidelines linked in invite. Prepare elevator pitch and target companies. Strong networking opportunity for job search.</span></div>
      <div class="conflict-warn">⚠️ Potential conflict: Dental cleaning ends at 11:45 AM — 15-minute buffer before Zoom. Confirm you'll be home/ready in time.</div>
    </div>

    <div class="cal-event">
      <div class="cal-event-time">12:00 PM – 1:30 PM EDT</div>
      <div class="cal-event-title">Network (Personal Note)</div>
      <div class="cal-event-row"><span class="cal-event-label">Status:</span><span class="pill pill-green">Confirmed</span></div>
      <div class="cal-event-row"><span class="cal-event-label">Note:</span><span>This appears to be a personal reminder overlapping with the HR Networking Group session — likely the same Zoom or a reminder block.</span></div>
      <div class="conflict-warn">⚠️ Exact overlap with HR Networking Group (12:00–1:30 PM). Review if these are the same event or separate.</div>
    </div>
  </div>

  <!-- Thursday June 18 -->
  <div class="cal-day">
    <div class="cal-day-header">Thursday, June 18, 2026</div>

    <div class="cal-event">
      <div class="cal-event-time">9:00 AM – 10:30 AM EDT</div>
      <div class="cal-event-title">Executive Roundtable (John Madigan)</div>
      <div class="cal-event-row"><span class="cal-event-label">Status:</span><span class="pill pill-red">Declined</span></div>
      <div class="cal-event-row"><span class="cal-event-label">Location:</span><span>Zoom: https://us02web.zoom.us/j/207786667 | Password: 205454</span></div>
      <div class="cal-event-row"><span class="cal-event-label">Prep:</span><span>You have declined this event. Verify if the decline was intentional. If it was an error or if circumstances changed, reach out to John Madigan to re-join.</span></div>
    </div>

    <div class="cal-event">
      <div class="cal-event-time">12:00 PM – 1:00 PM EDT</div>
      <div class="cal-event-title">HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
      <div class="cal-event-row"><span class="cal-event-label">Status:</span><span class="pill pill-yellow">Needs Action — RSVP</span></div>
      <div class="cal-event-row"><span class="cal-event-label">Location:</span><span>Zoom: https://us06web.zoom.us/j/85945371140</span></div>
      <div class="cal-event-row"><span class="cal-event-label">Note:</span><span>No AI notetaking tools per organizer's request. Open discussion format. Same large HR group as Jun 17 session.</span></div>
      <div class="cal-event-row"><span class="cal-event-label">Prep:</span><span>Accept invite. Prepare 1–2 specific job search questions or challenges to discuss.</span></div>
    </div>
  </div>

  <!-- Fri–Sun: No events -->
  <div class="cal-day">
    <div class="cal-day-header">Friday, June 19 — Sunday, June 21, 2026</div>
    <div class="cal-event">
      <div class="cal-event-time">All Day</div>
      <div class="cal-event-title">No Calendar Events Scheduled</div>
      <div class="cal-event-row"><span class="cal-event-label">Note:</span><span>Use this window for follow-up emails, job applications, and prep for the following week.</span></div>
    </div>
  </div>
</div>

<hr class="section-divider">

<!-- ═══════════════════════════════════════════════════════════════
     5. JOB SEARCH & INTERVIEW PIPELINE
═══════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
  <table>
    <thead>
      <tr>
        <th>Type</th>
        <th>Role / Source</th>
        <th>Company</th>
        <th>Fit</th>
        <th>Status / Action</th>
        <th>Due</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="pill pill-green">Interview</span></td>
        <td>Principal People Business Partner, Finance</td>
        <td><strong>SoFi</strong></td>
        <td><span class="pill pill-green">High</span></td>
        <td>✅ Confirmed. Prep &amp; attend today 2:30 PM EDT.</td>
        <td><strong>Today 2:30 PM</strong></td>
      </tr>
      <tr>
        <td><span class="pill pill-yellow">Consultation</span></td>
        <td>15-Min Consultation</td>
        <td><strong>Netta Jenkins / HIC Consult</strong></td>
        <td><span class="pill pill-yellow">Medium</span></td>
        <td>⚠️ Tentative — confirm RSVP. Zoom 1:45 PM today.</td>
        <td><strong>Today 1:45 PM</strong></td>
      </tr>
      <tr>
        <td><span class="pill pill-green">Job Alert</span></td>
        <td>Two New Director+ HR/People Roles</td>
        <td><strong>Various (Yutori Scout)</strong></td>
        <td><span class="pill pill-green">High</span></td>
        <td>📬 In Inbox (unread). Open &amp; review both listings today.</td>
        <td><strong>Today</strong></td>
      </tr>
      <tr>
        <td><span class="pill pill-green">Job Alert</span></td>
        <td>People Partner, Sales</td>
        <td><strong>Figma</strong></td>
        <td><span class="pill pill-green">High</span></td>
        <td>📬 In Inbox (unread). Review JD and apply if strong fit.</td>
        <td><strong>This week</strong></td>
      </tr>
      <tr>
        <td><span class="pill pill-blue">Networking</span></td>
        <td>HR Networking &amp; Job Search Group</td>
        <td><strong>HR Community — Zoom</strong></td>
        <td><span class="pill pill-green">High</span></td>
        <td>⚠️ Needs RSVP. June 17, 12–1:30 PM EDT. ~100 HR pros.</td>
        <td><strong>Before Jun 17</strong></td>
      </tr>
      <tr>
        <td><span class="pill pill-blue">Networking</span></td>
        <td>HR Networking Open Office Hours</td>
        <td><strong>HR Community — Zoom</strong></td>
        <td><span class="pill pill-green">High</span></td>
        <td>⚠️ Needs RSVP. June 18, 12–1 PM EDT. Open discussion.</td>
        <td><strong>Before Jun 18</strong></td>
      </tr>
      <tr>
        <td><span class="pill pill-purple">Message</span></td>
        <td>LinkedIn Message — Awaiting Response</td>
        <td><strong>Virginie Glaenzer</strong></td>
        <td><span class="pill pill-yellow">Medium</span></td>
        <td>📩 Unread (not trash). Respond on LinkedIn today.</td>
        <td><strong>Today</strong></td>
      </tr>
      <tr>
        <td><span class="pill pill-gray">FYI</span></td>
        <td>20 New Fractional Jobs + S-Corp Tax Tip</td>
        <td><strong>FractionalJobs.io</strong></td>
        <td><span class="pill pill-yellow">Medium</span></td>
        <td>🗑️ In Trash. Restore if fractional HR roles are of interest.</td>
        <td>Optional</td>
      </tr>
      <tr>
        <td><span class="pill pill-gray">Webinar</span></td>
        <td>LIVE HR Risk Session — Doctor's Notes</td>
        <td><strong>Katie Spadoro, PHR via LinkedIn</strong></td>
        <td><span class="pill pill-yellow">Medium</span></td>
        <td>🗑️ In Trash. Likely missed (sent today). Check for replay.</td>
        <td>Missed / Optional</td>
      </tr>
      <tr>
        <td><span class="pill pill-gray">Networking</span></td>
        <td>Executive Roundtable</td>
        <td><strong>John Madigan — Zoom</strong></td>
        <td><span class="pill pill-yellow">Medium</span></td>
        <td>❌ Declined. Verify if intentional; reach out if not.</td>
        <td>Jun 18, 9 AM</td>
      </tr>
    </tbody>
  </table>
</div>

<hr class="section-divider">

<!-- ═══════════════════════════════════════════════════════════════
     6. FULL EMAIL REVIEW BY CATEGORY
═══════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📬 Full Email Review by Category</div>

  <!-- Security / Risk -->
  <div class="card card-red">
    <div class="card-title">🔴 Security / Risk — 1 Email</div>
    <div class="email-row"><span class="email-sender">"Payment_Declined©"</span><span class="email-subject">⚠️ WARNING: Failure Notice — We've Blocked Your Account!</span><span class="email-tag tag-delete">DELETE NOW</span></div>
    <div class="scam-warn">⚠️ SCAM / PHISHING: Spoofed sender, fake cloud storage warning. NOT in trash — currently stored in your inbox area. Delete immediately. Do not click any links.</div>
    <div><strong>Recommended Action:</strong> Delete. Verify accounts at myaccount.google.com.</div>
  </div>

  <!-- Job Search -->
  <div class="card card-green">
    <div class="card-title">🟢 Job Search — 4 Emails</div>
    <div class="email-row"><span class="email-sender">Yutori / Scout</span><span class="email-subject">[Scout] Two New Director+ HR/People Roles (June 15) — IN INBOX</span><span class="email-tag tag-restore">REVIEW NOW</span></div>
    <div class="email-row"><span class="email-sender">LinkedIn Job Alerts</span><span class="email-subject">People Partner, Sales at Figma — IN INBOX</span><span class="email-tag tag-restore">REVIEW NOW</span></div>
    <div class="email-row"><span class="email-sender">Taylor Crane / FractionalJobs.io</span><span class="email-subject">20 New Fractional Jobs + Last Chance to Save on Taxes — TRASH</span><span class="email-tag tag-review">REVIEW</span></div>
    <div class="email-row"><span class="email-sender">Austin Belcak / Cultivated Culture</span><span class="email-subject">Use the "Rule of 5" to win more job interviews — TRASH</span><span class="email-tag tag-delete">LOW VALUE</span></div>
    <div><strong>Recommended Action:</strong> Open Yutori and Figma/LinkedIn emails first. Review fractional jobs if interested in consulting. Belcak email is generic job-search advice.</div>
  </div>

  <!-- Recruiters / Networking -->
  <div class="card card-green">
    <div class="card-title">🟢 Recruiters / Networking — 2 Emails</div>
    <div class="email-row"><span class="email-sender">Virginie Glaenzer via LinkedIn</span><span class="email-subject">Virginie just messaged you (1 new message)</span><span class="email-tag tag-restore">RESPOND TODAY</span></div>
    <div class="email-row"><span class="email-sender">Austin Belcak / Cultivated Culture</span><span class="email-subject">🗣️ Live: 3 reasons nobody's replying to you (not your resume)</span><span class="email-tag tag-review">LOW VALUE</span></div>
    <div><strong>Recommended Action:</strong> Respond to Virginie on LinkedIn today. Belcak email is a generic job search newsletter — low priority.</div>
  </div>

  <!-- Calendar / Events -->
  <div class="card card-blue">
    <div class="card-title">🔵 Calendar / Events — 3 Emails</div>
    <div class="email-row"><span class="email-sender">Netta Jenkins</span><span class="email-subject">Updated invitation: Melissa and Netta Jenkins @ Jun 15, 1:45 PM — TRASH (×2)</span><span class="email-tag tag-review">REVIEW</span></div>
    <div class="email-row"><span class="email-sender">Melissa W (self)</span><span class="email-subject">GitHub — claude-mem persistent context tool — IN INBOX</span><span class="email-tag tag-restore">REVIEW THIS WEEK</span></div>
    <div><strong>Note:</strong> The two Netta Jenkins calendar update emails are duplicates in Trash. The calendar event itself is on your calendar. The self-sent GitHub link is likely intentional.</div>
    <div><strong>Recommended Action:</strong> No action needed on Netta trash emails (calendar already shows event). Review GitHub link at your convenience.</div>
  </div>

  <!-- Medical / Health -->
  <div class="card card-yellow">
    <div class="card-title">🟡 Medical / Health — 4 Emails</div>
    <div class="email-row"><span class="email-sender">Warby Parker</span><span class="email-subject">Friendly reminder, Melissa — Prescription about to expire</span><span class="email-tag tag-restore">ACTION NEEDED</span></div>
    <div class="email-row"><span class="email-sender">Target Optical</span><span class="email-subject">Stock up and save on contacts!</span><span class="email-tag tag-review">FYI</span></div>
    <div class="email-row"><span class="email-sender">1-800 Contacts</span><span class="email-subject">What the heck is a GPP? — TRASH</span><span class="email-tag tag-delete">LOW VALUE</span></div>
    <div class="email-row"><span class="email-sender">1-800 Contacts</span><span class="email-subject">Can you believe it's been 2 years? — TRASH</span><span class="email-tag tag-delete">PROMO</span></div>
    <div><strong>Recommended Action:</strong> Schedule an eye exam. Warby Parker &amp; Target Optical are actionable. 1-800 Contacts emails are promotional — delete.</div>
  </div>

  <!-- Financial / Billing -->
  <div class="card card-yellow">
    <div class="card-title">🟡 Financial / Billing — 1 Email</div>
    <div class="email-row"><span class="email-sender">CoinOut</span><span class="email-subject">Check Your Progress — submit receipts for rewards</span><span class="email-tag tag-review">LOW PRIORITY</span></div>
    <div><strong>Recommended Action:</strong> Low priority. Check if you have pending receipts to submit. Otherwise ignore.</div>
  </div>

  <!-- Professional Development -->
  <div class="card card-purple">
    <div class="card-title">🟣 Professional Development — 4 Emails</div>
    <div class="email-row"><span class="email-sender">Phil Strazzulla / SSR</span><span class="email-subject">2026 ATS Comparison Guide + $100 Gift Card</span><span class="email-tag tag-review">USEFUL</span></div>
    <div class="email-row"><span class="email-sender">HR.com eBulletin</span><span class="email-subject">[General HR] Upgrade your LOA Strategy to Boost ROI</span><span class="email-tag tag-review">USEFUL</span></div>
    <div class="email-row"><span class="email-sender">Katie Spadoro, PHR via LinkedIn</span><span class="email-subject">LIVE HR Risk Session — Doctor's Notes — TRASH</span><span class="email-tag tag-review">MISSED — CHECK REPLAY</span></div>
    <div class="email-row"><span class="email-sender">Hacking HR via LinkedIn</span><span class="email-subject">A Hiring Framework to Find Great Candidates — TRASH</span><span class="email-tag tag-review">USEFUL IF RELEVANT</span></div>
    <div><strong>Recommended Action:</strong> ATS guide is useful for HR leaders — review when job searching involves ATS tools. LOA strategy bulletin worth a skim. Check if HR Risk webinar has a replay.</div>
  </div>

  <!-- Personal -->
  <div class="card card-gray">
    <div class="card-title">⚪ Personal — 3 Emails</div>
    <div class="email-row"><span class="email-sender">Giulia Guerrieri</span><span class="email-subject">My dad has run a bakery for 40 years — personal story</span><span class="email-tag tag-review">PERSONAL / READ LATER</span></div>
    <div class="email-row"><span class="email-sender">Giulia Guerrieri</span><span class="email-subject">What happens after we fix your AI + content leak — TRASH</span><span class="email-tag tag-delete">NEWSLETTER</span></div>
    <div class="email-row"><span class="email-sender">Google</span><span class="email-subject">Correction: Regarding our recent email about child privacy settings — TRASH</span><span class="email-tag tag-review">REVIEW</span></div>
    <div><strong>Recommended Action:</strong> Google correction email may be worth reading — it's from a legitimate Google sender. Giulia emails appear to be a personal newsletter — read or unsubscribe at your discretion.</div>
  </div>

  <!-- Newsletters / Subscriptions -->
  <div class="card card-purple">
    <div class="card-title">🟣 Newsletters / Subscriptions — 6 Emails</div>
    <div class="email-row"><span class="email-sender">HR Brew</span><span class="email-subject">☕ ICHRA? We hardly know ya — HR healthcare trends — TRASH</span><span class="email-tag tag-review">USEFUL IF RELEVANT</span></div>
    <div class="email-row"><span class="email-sender">Mindstream</span><span class="email-subject">Google's AI lied, now it's paying — AI news — TRASH</span><span class="email-tag tag-delete">LOW PRIORITY</span></div>
    <div class="email-row"><span class="email-sender">CoolDeep AI</span><span class="email-subject">I was using AI like a foo — AI tips — TRASH</span><span class="email-tag tag-delete">UNSUBSCRIBE</span></div>
    <div class="email-row"><span class="email-sender">TIME via LinkedIn</span><span class="email-subject">London Mayor Sadiq Khan on climate — TRASH</span><span class="email-tag tag-delete">LOW PRIORITY</span></div>
    <div class="email-row"><span class="email-sender">Stephanie Adams, SPHR via LinkedIn</span><span class="email-subject">HR Is Not Therapy — TRASH</span><span class="email-tag tag-review">USEFUL IF KEPT</span></div>
    <div class="email-row"><span class="email-sender">Hacking HR via LinkedIn</span><span class="email-subject">A Hiring Framework — High-Volume Market — TRASH</span><span class="email-tag tag-review">USEFUL IF RELEVANT</span></div>
    <div><strong>Recommended Action:</strong> HR-focused newsletters (HR Brew, Stephanie Adams, Hacking HR) are worth reviewing given your job search. AI/tech news newsletters are lower priority unless you're using AI in your workflow.</div>
  </div>

  <!-- Promotional / Retail -->
  <div class="card card-gray">
    <div class="card-title">⚪ Promotional / Retail — 22 Emails</div>
    <div style="font-size:13px; color:#555; margin-bottom:8px;">Retail, shopping, beauty, dating, gaming, and other promotional emails. Full breakdown in Section 8 below.</div>
    <div class="email-row"><span class="email-sender">StackSocial, Old Navy, H&M, SHEIN (×2)</span><span class="email-subject">Sales, deals, fashion promotions</span><span class="email-tag tag-delete">DELETE</span></div>
    <div class="email-row"><span class="email-sender">Laura Geller (×4), Container Store</span><span class="email-subject">Beauty &amp; home promotions</span><span class="email-tag tag-delete">DELETE</span></div>
    <div class="email-row"><span class="email-sender">Shoe Carnival, Shoe Station, Acorns, Walgreens</span><span class="email-subject">Rewards, referrals, pharmacy deals</span><span class="email-tag tag-delete">DELETE</span></div>
    <div class="email-row"><span class="email-sender">Macy's, 22 Words, Mystery Deal, BellaVita</span><span class="email-subject">Sales and deals newsletters</span><span class="email-tag tag-delete">DELETE</span></div>
    <div class="email-row"><span class="email-sender">eHarmony, OkCupid, Solitaire Clash, Fureverdock, Ladders</span><span class="email-subject">Dating, gaming, apps, resume services</span><span class="email-tag tag-delete">DELETE</span></div>
    <div><strong>Recommended Action:</strong> All promotional. Mass delete or unsubscribe from senders you no longer find relevant.</div>
  </div>

</div>

<hr class="section-divider">

<!-- ═══════════════════════════════════════════════════════════════
     7. TRASH REVIEW
═══════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">🗑️ Trash Review — 29 Emails in Trash</div>

  <div class="trash-group-title">✅ Restore Immediately (3 emails)</div>
  <table>
    <thead><tr><th>Sender</th><th>Subject</th><th>Reason to Restore</th></tr></thead>
    <tbody>
      <tr><td>Taylor Crane / FractionalJobs.io</td><td>20 New Fractional Jobs + Tax Savings</td><td>If fractional/consulting HR roles interest you, this has actionable job leads. Also contains S-Corp tax deadline info (2 weeks left).</td></tr>
      <tr><td>Katie Spadoro, PHR via LinkedIn</td><td>LIVE HR Risk Session — Doctor's Notes</td><td>Practical HR compliance content. Check if a replay is available — directly relevant to HR professional practice.</td></tr>
      <tr><td>Hacking HR via LinkedIn</td><td>A Hiring Framework for High-Volume Markets</td><td>Relevant HR professional content, especially if interviewing for HRBP roles where recruiting knowledge is valued.</td></tr>
    </tbody>
  </table>

  <div class="trash-group-title">⚠️ Review Before Deleting (4 emails)</div>
  <table>
    <thead><tr><th>Sender</th><th>Subject</th><th>Reason to Review</th></tr></thead>
    <tbody>
      <tr><td>Google &lt;google-noreply@google.com&gt;</td><td>Correction: Regarding our recent email about child privacy settings</td><td>Legitimate Google sender — may contain important correction about a previous privacy notification. Quick read recommended.</td></tr>
      <tr><td>Netta Jenkins (×2)</td><td>Updated invitation: Melissa and Netta Jenkins @ Jun 15, 1:45 PM</td><td>Duplicate calendar update emails — confirm the Zoom details match what's on your calendar. Then delete.</td></tr>
      <tr><td>HR Brew</td><td>☕ ICHRA? We hardly know ya</td><td>Healthcare cost trends for HR leaders — potentially relevant if you're advising on benefits. Quick skim before deleting.</td></tr>
    </tbody>
  </table>

  <div class="trash-group-title">🗑️ Safe to Delete — All Remaining (22 emails)</div>
  <table>
    <thead><tr><th>Sender / Group</th><th>Emails</th><th>Reason</th></tr></thead>
    <tbody>
      <tr><td>Laura Geller (×4)</td><td>4</td><td>Duplicate beauty promo emails — all identical, all promotional. Safe to delete.</td></tr>
      <tr><td>SHEIN (×2)</td><td>2</td><td>Duplicate fast fashion promotional emails.</td></tr>
      <tr><td>Netta Jenkins (×2 — already counted above as review)</td><td>—</td><td>Accounted for above.</td></tr>
      <tr><td>StackSocial</td><td>1</td><td>Generic deal newsletter.</td></tr>
      <tr><td>TIME via LinkedIn</td><td>1</td><td>General news article, low relevance.</td></tr>
      <tr><td>Container Store</td><td>1</td><td>Sale ends today — promotional only.</td></tr>
      <tr><td>Austin Belcak / Cultivated Culture</td><td>1</td><td>Generic job search advice newsletter.</td></tr>
      <tr><td>Mindstream</td><td>1</td><td>AI news newsletter — low priority.</td></tr>
      <tr><td>CoolDeep AI</td><td>1</td><td>AI tips newsletter — generic.</td></tr>
      <tr><td>Acorns</td><td>1</td><td>Referral bonus promo.</td></tr>
      <tr><td>eHarmony</td><td>1</td><td>Dating app promo.</td></tr>
      <tr><td>Stephanie Adams SPHR via LinkedIn</td><td>1</td><td>HR newsletter in trash — restore if desired, otherwise delete.</td></tr>
      <tr><td>Giulia Guerrieri (content/AI email)</td><td>1</td><td>Marketing newsletter — low priority.</td></tr>
      <tr><td>Shoe Carnival</td><td>1</td><td>Reward email promo.</td></tr>
      <tr><td>Shoe Station</td><td>1</td><td>Sneaker promo.</td></tr>
      <tr><td>Walgreens</td><td>1</td><td>Pharmacy promo.</td></tr>
      <tr><td>Macy's</td><td>1</td><td>Sale ends tonight — already past.</td></tr>
      <tr><td>BellaVita (TikTok Shop)</td><td>1</td><td>Free shipping promo.</td></tr>
      <tr><td>22 Words</td><td>1</td><td>Amazon deals digest.</td></tr>
      <tr><td>Mystery Deal</td><td>1</td><td>Unknown deal newsletter.</td></tr>
      <tr><td>Solitaire Clash</td><td>1</td><td>Mobile gaming promo.</td></tr>
      <tr><td>Ladders</td><td>1</td><td>Resume review promo — low value given your level.</td></tr>
      <tr><td>1-800 Contacts (×2)</td><td>2</td><td>Contacts promo — Rx context handled by Warby Parker above.</td></tr>
    </tbody>
  </table>
</div>

<hr class="section-divider">

<!-- ═══════════════════════════════════════════════════════════════
     8. PROMOTIONAL / RETAIL SUMMARY
═══════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">🛍️ Promotional / Retail Summary</div>
  <table>
    <thead>
      <tr><th>Brand / Sender</th><th>Count
<hr>
<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Job Search / Recruiters</td><td>10</td></tr>
<tr><td>Medical / Health</td><td>3</td></tr>
<tr><td>Other / Review</td><td>21</td></tr>
<tr><td>Professional Development / Newsletters</td><td>5</td></tr>
<tr><td>Promotional / Retail</td><td>7</td></tr>
<tr><td>Security / Risk</td><td>4</td></tr>
</table>
<p><strong>Audit Note:</strong> Every fetched email was reviewed and assigned to one category. Trash emails were included in review. Promotional and low-value emails were accounted for but deprioritized.</p>

