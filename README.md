<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa W — Saturday, September 12, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a237e 0%, #283593 60%, #3949ab 100%); color: #fff; border-radius: 12px; padding: 32px 36px 28px; margin-bottom: 24px; box-shadow: 0 4px 18px rgba(26,35,126,0.18); }
  .header h1 { font-size: 2rem; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 1.05rem; opacity: 0.85; margin-top: 4px; }
  .header .meta { margin-top: 14px; display: flex; gap: 28px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.12); border-radius: 8px; padding: 7px 16px; font-size: 0.92rem; }
  .header .meta-item strong { font-weight: 700; }

  /* SECTION HEADERS */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 1.08rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; padding: 10px 18px; border-radius: 8px 8px 0 0; display: flex; align-items: center; gap: 8px; }
  .section-body { background: #fff; border-radius: 0 0 10px 10px; padding: 18px 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }

  /* COLOR THEMES */
  .red .section-title    { background: #c62828; color: #fff; }
  .red .section-body     { border: 2px solid #c62828; border-top: none; }
  .yellow .section-title { background: #f9a825; color: #222; }
  .yellow .section-body  { border: 2px solid #f9a825; border-top: none; }
  .blue .section-title   { background: #1565c0; color: #fff; }
  .blue .section-body    { border: 2px solid #1565c0; border-top: none; }
  .green .section-title  { background: #2e7d32; color: #fff; }
  .green .section-body   { border: 2px solid #2e7d32; border-top: none; }
  .purple .section-title { background: #6a1b9a; color: #fff; }
  .purple .section-body  { border: 2px solid #6a1b9a; border-top: none; }
  .gray .section-title   { background: #546e7a; color: #fff; }
  .gray .section-body    { border: 2px solid #546e7a; border-top: none; }
  .teal .section-title   { background: #00695c; color: #fff; }
  .teal .section-body    { border: 2px solid #00695c; border-top: none; }
  .navy .section-title   { background: #1a237e; color: #fff; }
  .navy .section-body    { border: 2px solid #1a237e; border-top: none; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 0.88rem; }
  th { background: #eceff1; color: #37474f; font-weight: 700; padding: 9px 12px; text-align: left; border-bottom: 2px solid #cfd8dc; }
  td { padding: 8px 12px; border-bottom: 1px solid #eceff1; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f5f5f5; }

  /* BADGES */
  .badge { display: inline-block; border-radius: 20px; padding: 2px 10px; font-size: 0.78rem; font-weight: 700; white-space: nowrap; }
  .badge-red    { background: #ffcdd2; color: #b71c1c; }
  .badge-yellow { background: #fff9c4; color: #827717; }
  .badge-green  { background: #c8e6c9; color: #1b5e20; }
  .badge-blue   { background: #bbdefb; color: #0d47a1; }
  .badge-purple { background: #e1bee7; color: #4a148c; }
  .badge-gray   { background: #eceff1; color: #455a64; }
  .badge-orange { background: #ffe0b2; color: #bf360c; }
  .badge-teal   { background: #b2dfdb; color: #004d40; }
  .badge-high   { background: #ffcdd2; color: #b71c1c; }
  .badge-medium { background: #fff9c4; color: #827717; }
  .badge-low    { background: #eceff1; color: #546e7a; }

  /* CARDS */
  .card { border-radius: 9px; padding: 15px 18px; margin-bottom: 14px; border-left: 5px solid #ccc; }
  .card-red    { background: #fff8f8; border-left-color: #c62828; }
  .card-yellow { background: #fffde7; border-left-color: #f9a825; }
  .card-blue   { background: #e3f2fd; border-left-color: #1565c0; }
  .card-green  { background: #f1f8e9; border-left-color: #2e7d32; }
  .card-purple { background: #f3e5f5; border-left-color: #6a1b9a; }
  .card-gray   { background: #f9fafb; border-left-color: #78909c; }
  .card-teal   { background: #e0f2f1; border-left-color: #00695c; }
  .card-orange { background: #fff3e0; border-left-color: #e65100; }

  .card h4 { font-size: 0.95rem; font-weight: 700; margin-bottom: 5px; }
  .card .meta { font-size: 0.81rem; color: #666; margin-bottom: 6px; }
  .card .why { font-size: 0.85rem; margin-bottom: 4px; }
  .card .action { font-size: 0.84rem; font-weight: 600; }
  .card .due { font-size: 0.8rem; color: #999; margin-top: 4px; }

  /* EXEC SUMMARY */
  .exec-bullet { display: flex; gap: 12px; align-items: flex-start; margin-bottom: 10px; padding: 10px 14px; border-radius: 8px; }
  .exec-bullet .icon { font-size: 1.3rem; flex-shrink: 0; }
  .exec-bullet .text { font-size: 0.93rem; }

  /* CALENDAR */
  .cal-day { margin-bottom: 16px; }
  .cal-day-header { font-weight: 700; font-size: 0.95rem; background: #e3f2fd; color: #1565c0; padding: 7px 14px; border-radius: 6px; margin-bottom: 8px; }
  .cal-event { display: flex; gap: 14px; padding: 10px 14px; border-radius: 7px; margin-bottom: 7px; background: #f9fbff; border: 1px solid #d0e4f7; }
  .cal-time { font-weight: 700; color: #1565c0; min-width: 110px; font-size: 0.85rem; }
  .cal-details h5 { font-size: 0.92rem; font-weight: 700; margin-bottom: 3px; }
  .cal-details .cal-meta { font-size: 0.8rem; color: #555; }
  .cal-details .cal-loc { font-size: 0.8rem; color: #1565c0; }
  .cal-details .cal-prep { font-size: 0.8rem; color: #e65100; font-style: italic; }
  .cal-details .cal-status { font-size: 0.78rem; }

  /* TRIAGE TABLE */
  .triage-inbox td:first-child { color: #1565c0; font-weight: 700; }
  .triage-rescued td:first-child { color: #2e7d32; font-weight: 700; }
  .triage-trash td:first-child { color: #78909c; }

  /* DASHBOARD GRID */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)); gap: 14px; }
  .dash-card { border-radius: 10px; padding: 16px 18px; border: 1px solid #e0e0e0; background: #fff; }
  .dash-card h5 { font-size: 0.82rem; text-transform: uppercase; letter-spacing: 0.8px; color: #888; margin-bottom: 8px; }
  .dash-card .num { font-size: 2rem; font-weight: 700; line-height: 1; }
  .dash-card .detail { font-size: 0.8rem; color: #555; margin-top: 5px; }

  /* MISC */
  .tag { display: inline-block; background: #e8eaf6; color: #3949ab; border-radius: 4px; padding: 1px 7px; font-size: 0.76rem; margin-right: 4px; }
  .rescued-note { font-size: 0.78rem; color: #2e7d32; font-style: italic; }
  .phishing-note { font-size: 0.78rem; color: #b71c1c; font-style: italic; }
  .row-group td { background: #fafafa; font-style: italic; color: #546e7a; }
  ul.bullets { padding-left: 18px; }
  ul.bullets li { margin-bottom: 4px; font-size: 0.88rem; }
  .divider { height: 1px; background: #e0e0e0; margin: 14px 0; }
  .priority-top { background: #1a237e; color: #fff; border-radius: 10px; padding: 20px 24px; margin-bottom: 12px; }
  .priority-top h3 { font-size: 1rem; margin-bottom: 8px; }
  .priority-top ol { padding-left: 20px; }
  .priority-top li { margin-bottom: 8px; font-size: 0.93rem; }
  a { color: #1565c0; }
  .flood-warning { background: #fff3cd; border: 2px solid #f9a825; border-radius: 8px; padding: 10px 16px; margin-bottom: 10px; font-weight: 600; }

  @media (max-width: 700px) {
    .header { padding: 20px 16px; }
    .header h1 { font-size: 1.4rem; }
    .header .meta { gap: 10px; }
    .cal-event { flex-direction: column; gap: 4px; }
    .cal-time { min-width: unset; }
  }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════════════ HEADER -->
<div class="header">
  <div class="subtitle">EXECUTIVE BRIEFING — CHIEF OF STAFF REPORT</div>
  <h1>Good Morning, Melissa 👋</h1>
  <div class="meta">
    <div class="meta-item">📅 <strong>Saturday, September 12, 2026</strong></div>
    <div class="meta-item">📧 <strong>50</strong> Emails Reviewed</div>
    <div class="meta-item">📆 <strong>7</strong> Calendar Events</div>
    <div class="meta-item">⚠️ <strong>FLOOD WATCH</strong> — NYC Tomorrow (9/13)</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ SECTION 0: EMAIL TRIAGE QUICK LIST -->
<div class="section navy">
  <div class="section-title">📋 Section 0 — Email Triage Quick List</div>
  <div class="section-body">
    <table>
      <thead>
        <tr>
          <th style="width:110px">Status</th>
          <th style="width:200px">From</th>
          <th>Subject</th>
          <th>Summary</th>
        </tr>
      </thead>
      <tbody>
        <!-- RESCUED FIRST -->
        <tr class="triage-rescued">
          <td>✅ RESCUED</td>
          <td>Experian Alerts</td>
          <td>Heads up Melissa! You have new alerts on your Experian credit file</td>
          <td><span class="rescued-note">Rescued from Trash — Legitimate Experian credit monitoring alert. Review immediately.</span></td>
        </tr>
        <!-- INBOX EMAILS -->
        <tr class="triage-inbox">
          <td>📥 INBOX</td>
          <td>Notify NYC</td>
          <td>Flood Watch — 9/13 (NYC)</td>
          <td>National Weather Service Flood Watch for NYC: 2 AM – 11 PM Sunday 9/13. Plan accordingly.</td>
        </tr>
        <tr class="triage-inbox">
          <td>📥 INBOX</td>
          <td>LinkedIn</td>
          <td>Human Resources Executive: Target hired near you</td>
          <td>LinkedIn job alert — Target hiring HR Executive roles. Assess fit.</td>
        </tr>
        <tr class="triage-inbox">
          <td>📥 INBOX</td>
          <td>LinkedIn Job Alerts</td>
          <td>PeopleOps Jobs is hiring a Vice President Human Resources</td>
          <td>VP HR role at PeopleOps Jobs via LinkedIn. High-relevance alert.</td>
        </tr>
        <tr class="triage-inbox">
          <td>📥 INBOX</td>
          <td>LinkedIn Job Alerts</td>
          <td>Vice President Human Resources at PeopleOps Jobs</td>
          <td>Duplicate VP HR alert from LinkedIn Job Alerts. Same role as above.</td>
        </tr>
        <tr class="triage-inbox">
          <td>📥 INBOX</td>
          <td>Glassdoor Jobs</td>
          <td>Director of People and Culture at Galvanize USA and 7 more jobs — Remote</td>
          <td>Glassdoor alert with 8 remote HR/People roles. Review for fit.</td>
        </tr>
        <tr class="triage-inbox">
          <td>📥 INBOX</td>
          <td>TikTok Shop</td>
          <td>Your order was packed and awaiting shipment</td>
          <td>TikTok Shop order packed; tracking details to follow.</td>
        </tr>
        <tr class="triage-inbox">
          <td>📥 INBOX</td>
          <td>Match</td>
          <td>John likes you. See if it's mutual.</td>
          <td>Match.com — John (49, Sandusky OH) liked your profile.</td>
        </tr>
        <tr class="triage-inbox">
          <td>📥 INBOX</td>
          <td>Match</td>
          <td>You've had a profile view from John</td>
          <td>Match.com — same John viewed your profile. Companion to above.</td>
        </tr>
        <tr class="triage-inbox">
          <td>📥 INBOX</td>
          <td>Melissa W (self)</td>
          <td>Blotato | #1 Social Media APIs for AI Agents, ChatGPT &amp; Claude</td>
          <td>Self-sent note with Blotato link — personal research bookmark.</td>
        </tr>
        <tr class="triage-inbox">
          <td>📥 INBOX</td>
          <td>Melissa W (self)</td>
          <td>Job Application for Principal People Partner at Pie Insurance</td>
          <td>Self-sent job application link — Pie Insurance Greenhouse listing.</td>
        </tr>
        <tr class="triage-inbox">
          <td>📥 INBOX</td>
          <td>Medium Daily Digest</td>
          <td>Why are lobsters boiled alive? | Giuseppe Frisella</td>
          <td>Medium newsletter — also auto-trashed as newsletter. In inbox &amp; trash.</td>
        </tr>
        <!-- TRASH SUMMARY ROWS -->
        <tr class="row-group">
          <td>🗑 TRASHED (auto)</td>
          <td colspan="3">8 emails auto-trashed (phishing + newsletters) — see Trash Review for full details</td>
        </tr>
        <tr class="row-group">
          <td>🗂 TRASH (manual)</td>
          <td colspan="3">30 emails in Trash — see Trash Review for full details</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ SECTION 1: HEADER (rendered inline above) -->

<!-- ═══════════════════════════════════════════════════════════ SECTION 2: EXECUTIVE SUMMARY -->
<div class="section red">
  <div class="section-title">⚡ Section 2 — Executive Summary</div>
  <div class="section-body">
    <div class="exec-bullet" style="background:#fff8f8; border-left: 4px solid #c62828; border-radius:8px;">
      <div class="icon">🚨</div>
      <div class="text"><strong>Biggest Risk / Urgent Item:</strong> A Flood Watch has been issued for all of NYC from 2 AM to 11 PM on Sunday, September 13. Separately, your Experian credit file has new alerts that were rescued from Trash — log in immediately to check for unauthorized activity. Multiple phishing and spam emails (gambling, adult content, fake prize scams, spoofed cloud storage threats) were auto-trashed; no action needed but your inbox is being targeted heavily.</div>
    </div>
    <div class="exec-bullet" style="background:#f1f8e9; border-left: 4px solid #2e7d32; border-radius:8px;">
      <div class="icon">💼</div>
      <div class="text"><strong>Biggest Job Search / Opportunity Item:</strong> Multiple high-relevance VP/Director-level HR and People roles surfaced today via LinkedIn and Glassdoor — including Vice President Human Resources at PeopleOps Jobs, Director of People &amp; Culture at Galvanize USA (remote), and a Target HR Executive opening. You also self-noted a Principal People Partner application at Pie Insurance. The HR Networking Group meets Wednesday 9/16 and Open Office Hours are Thursday 9/17 — both need RSVPs.</div>
    </div>
    <div class="exec-bullet" style="background:#e3f2fd; border-left: 4px solid #1565c0; border-radius:8px;">
      <div class="icon">📅</div>
      <div class="text"><strong>Biggest Calendar / Deadline Item:</strong> New Patient Visit with Dr. Andrea D. Card is Monday, September 14 at 9:00 AM at 53 W 23rd St, 6th Floor. Confirm insurance coverage, allow extra commute buffer due to Sunday's flood watch impact on Monday morning transit. Wednesday 9/16 has two overlapping entries (HR Networking Group + "Network" block) — both need attention. Executive Roundtable Thursday 9/17 is currently DECLINED — verify that's intentional.</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ SECTION 3: ACTION REQUIRED -->
<div class="section yellow">
  <div class="section-title">✅ Section 3 — Action Required</div>
  <div class="section-body">

    <div class="card card-red">
      <h4>🚨 URGENT — Flood Watch: NYC</h4>
      <div class="meta">Source: Notify NYC / National Weather Service · Received: Sat Sep 12, 2026</div>
      <div class="why"><strong>Why it matters:</strong> Flood Watch issued for all five NYC boroughs from 2:00 AM to 11:00 PM Sunday, September 13. Could affect transit and commute for your Monday 9/14 doctor appointment.</div>
      <div class="action">→ Monitor weather Sunday evening. Check subway/MTA service status before your 8:45 AM departure Monday. Allow extra commute time.</div>
      <div class="due">⏰ Due: Sunday 9/13 evening / Monday 9/14 morning</div>
    </div>

    <div class="card card-red">
      <h4>🔐 URGENT — Experian Credit File Alert</h4>
      <div class="meta">Source: Experian Alerts &lt;support@s.usa.experian.com&gt; · Rescued from Trash · Fri Sep 11, 2026</div>
      <div class="why"><strong>Why it matters:</strong> Your Experian credit file has new unread notifications — could signal a new account opened, hard inquiry, or suspicious activity. Was incorrectly moved to Trash and rescued.</div>
      <div class="action">→ Log in to experian.com or the Experian app immediately. Review all alerts. If suspicious activity found, place a fraud alert or freeze.</div>
      <div class="due">⏰ Due: Today, Saturday 9/12</div>
    </div>

    <div class="card card-yellow">
      <h4>📋 RSVP Needed — HR Networking &amp; Job Search Group (Zoom 2)</h4>
      <div class="meta">Source: Google Calendar · Wednesday, September 16, 12:00–1:30 PM</div>
      <div class="why"><strong>Why it matters:</strong> Large HR professional networking group meeting. Status is "Needs Action" — you have not confirmed attendance.</div>
      <div class="action">→ Accept or decline the calendar invite. Prepare your 30-second intro and any job search updates to share with the group.</div>
      <div class="due">⏰ Due: Before Wednesday 9/16 at noon</div>
    </div>

    <div class="card card-yellow">
      <h4>📋 RSVP Needed — HR Networking Open Office Hours (Zoom)</h4>
      <div class="meta">Source: Google Calendar · Thursday, September 17, 12:00–1:00 PM</div>
      <div class="why"><strong>Why it matters:</strong> Open office hours with the HR networking group. Status is "Needs Action."</div>
      <div class="action">→ Accept or decline the invite. Note: Host requests NO automated AI note-taking tools on this call.</div>
      <div class="due">⏰ Due: Before Thursday 9/17 at noon</div>
    </div>

    <div class="card card-yellow">
      <h4>🏥 Confirm — New Patient Visit with Dr. Andrea D. Card</h4>
      <div class="meta">Source: Google Calendar · Monday, September 14, 9:00 AM · 53 W 23rd St, 6th Floor, NYC</div>
      <div class="why"><strong>Why it matters:</strong> First appointment with a new physician. Office may contact you for insurance verification before the visit.</div>
      <div class="action">→ Confirm insurance card is ready. Allow extra travel time due to potential flood/transit delays from Sunday. Call 212-746-2900 if needed.</div>
      <div class="due">⏰ Due: Monday 9/14 by 8:45 AM</div>
    </div>

    <div class="card card-green">
      <h4>💼 Apply — VP Human Resources at PeopleOps Jobs</h4>
      <div class="meta">Source: LinkedIn Job Alerts · Sat Sep 12, 2026 (two alerts for same role)</div>
      <div class="why"><strong>Why it matters:</strong> Senior VP-level HR role. Highly aligned with your background. Two separate alerts received, indicating strong algorithmic match.</div>
      <div class="action">→ Review full job description on LinkedIn. Tailor resume and apply via PeopleOps Jobs portal. Note for Wednesday networking group discussion.</div>
      <div class="due">⏰ Due: This weekend or early next week</div>
    </div>

    <div class="card card-green">
      <h4>💼 Review — Director of People &amp; Culture at Galvanize USA + 7 Remote Roles</h4>
      <div class="meta">Source: Glassdoor Jobs · Sat Sep 12, 2026</div>
      <div class="why"><strong>Why it matters:</strong> 8 roles in this alert including remote opportunities. Director of People &amp; Culture at Galvanize USA stands out at top of alert.</div>
      <div class="action">→ Open Glassdoor alert and review all 8 roles. Flag best matches. Apply to top 2–3 before Wednesday's networking meeting.</div>
      <div class="due">⏰ Due: Before Wednesday 9/16</div>
    </div>

    <div class="card card-green">
      <h4>💼 Follow Up — Principal People Partner Application (Pie Insurance)</h4>
      <div class="meta">Source: Self-sent email (Melissa W) · Fri Sep 11, 2026 · Greenhouse job board</div>
      <div class="why"><strong>Why it matters:</strong> You self-noted this application link, suggesting intent to apply or track. Confirms active pipeline management.</div>
      <div class="action">→ Confirm whether application was submitted. If not, apply via the Greenhouse link. Log in your job tracker.</div>
      <div class="due">⏰ Due: Today or tomorrow</div>
    </div>

    <div class="card card-yellow">
      <h4>🔍 Verify Intent — Executive Roundtable DECLINED</h4>
      <div class="meta">Source: Google Calendar · Thursday, September 17, 9:00–10:30 AM (John Madigan, Zoom)</div>
      <div class="why"><strong>Why it matters:</strong> You declined this invitation, but it overlaps with Open Office Hours at noon and could be a valuable executive networking opportunity depending on context.</div>
      <div class="action">→ Confirm your decline was intentional. If not, re-accept and add to prep list.</div>
      <div class="due">⏰ Due: Review today</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ SECTION 4: FULL 7-DAY CALENDAR -->
<div class="section blue">
  <div class="section-title">📆 Section 4 — Full 7-Day Calendar (Sep 12–18, 2026)</div>
  <div class="section-body">

    <div class="cal-day">
      <div class="cal-day-header">📅 Saturday, September 12, 2026 — TODAY</div>
      <div class="cal-event" style="background:#fff8e1; border-color:#f9a825;">
        <div class="cal-time">All Day</div>
        <div class="cal-details">
          <h5>No scheduled calendar events today</h5>
          <div class="cal-meta">Use today to review this briefing, check Experian alerts, apply to VP HR roles, and RSVP to upcoming networking events.</div>
        </div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">⚠️ Sunday, September 13, 2026 — FLOOD WATCH IN EFFECT</div>
      <div class="flood-warning">🌊 NYC Flood Watch: 2:00 AM – 11:00 PM · National Weather Service via Notify NYC · Monitor MTA service alerts</div>
      <div class="cal-event" style="background:#fff8e1; border-color:#f9a825;">
        <div class="cal-time">All Day</div>
        <div class="cal-details">
          <h5>No scheduled calendar events — Flood Watch Day</h5>
          <div class="cal-meta">Prepare for potential transit disruptions affecting Monday's doctor appointment. Check MTA Sunday night.</div>
        </div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">🏥 Monday, September 14, 2026</div>
      <div class="cal-event">
        <div class="cal-time">8:45 AM – 9:40 AM</div>
        <div class="cal-details">
          <h5>New Patient Visit — Dr. Andrea D. Card</h5>
          <div class="cal-status"><span class="badge badge-green">✅ Accepted</span></div>
          <div class="cal-loc">📍 53 W 23rd St, 6th Floor, New York, NY 10010 · 📞 212-746-2900</div>
          <div class="cal-meta">Appointment Time: 9:00 AM EDT (arrive by 8:45 AM for new patient paperwork)</div>
          <div class="cal-prep">⚠️ Prep: Bring insurance card. Office may call for insurance verification before visit. Allow extra transit time — post-flood Monday morning may have MTA delays.</div>
        </div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">🤝 Tuesday, September 15, 2026</div>
      <div class="cal-event">
        <div class="cal-time">3:00 PM – 4:00 PM</div>
        <div class="cal-details">
          <h5>M&amp;M</h5>
          <div class="cal-status"><span class="badge badge-green">✅ Accepted</span></div>
          <div class="cal-loc">📍 No location specified</div>
          <div class="cal-meta">Attendee: monte.montoya@gmail.com</div>
          <div class="cal-prep">⚠️ Prep: No description provided. Confirm meeting details with Monte Montoya. Clarify format (phone, Zoom, in-person?).</div>
        </div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">💼 Wednesday, September 16, 2026 — TWO EVENTS (check for overlap)</div>
      <div class="cal-event">
        <div class="cal-time">12:00 PM – 1:30 PM</div>
        <div class="cal-details">
          <h5>HR Networking &amp; Job Search Group — Zoom 2</h5>
          <div class="cal-status"><span class="badge badge-yellow">⚠️ Needs Action (RSVP Required)</span></div>
          <div class="cal-loc">🔗 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a></div>
          <div class="cal-meta">Large group networking session — 170+ attendees. HR professionals in active job search.</div>
          <div class="cal-prep">⚠️ Prep: RSVP immediately. Prepare 30-second professional intro. Bring top 2–3 target roles to discuss. Review VP HR role at PeopleOps Jobs beforehand.</div>
        </div>
      </div>
      <div class="cal-event" style="background:#f3e5f5; border-color:#6a1b9a;">
        <div class="cal-time">12:00 PM – 1:30 PM</div>
        <div class="cal-details">
          <h5>"Network" — Personal Block</h5>
          <div class="cal-status"><span class="badge badge-green">✅ Confirmed</span></div>
          <div class="cal-loc">📍 No location specified</div>
          <div class="cal-meta">No description. Likely a personal reminder block coinciding with the HR Networking Group above.</div>
          <div class="cal-prep">⚠️ Note: Overlaps exactly with HR Networking Group Zoom. Likely intentional placeholder — no conflict.</div>
        </div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">📊 Thursday, September 17, 2026 — TWO EVENTS</div>
      <div class="cal-event" style="background:#fff8f8; border-color:#c62828;">
        <div class="cal-time">9:00 AM – 10:30 AM</div>
        <div class="cal-details">
          <h5>Executive Roundtable (John Madigan — Zoom)</h5>
          <div class="cal-status"><span class="badge badge-red">❌ Declined</span></div>
          <div class="cal-loc">🔗 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom: Meeting ID 207 786 667 · Password 205454</a></div>
          <div class="cal-meta">Dial-in: +1-646-876-9923 (NY) · +1-312-626-6799 (Chicago)</div>
          <div class="cal-prep">⚠️ You declined this invitation. Verify this was intentional — Executive Roundtable with John Madigan may be a valuable leadership networking event.</div>
        </div>
      </div>
      <div class="cal-event">
        <div class="cal-time">12:00 PM – 1:00 PM</div>
        <div class="cal-details">
          <h5>HR Networking &amp; Job Search: Open Office Hours — Zoom 2</h5>
          <div class="cal-status"><span class="badge badge-yellow">⚠️ Needs Action (RSVP Required)</span></div>
          <div class="cal-loc">🔗 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a></div>
          <div class="cal-meta">Open discussion — no recording. Same large HR networking group as Wednesday.</div>
          <div class="cal-prep">⚠️ Prep: RSVP. Turn off AI notetaking tools (host explicitly requested). Bring specific questions or challenges from your job search to discuss openly.</div>
        </div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">🏃 Friday, September 18, 2026</div>
      <div class="cal-event">
        <div class="cal-time">8:45 AM – 9:45 AM</div>
        <div class="cal-details">
          <h5>Pt</h5>
          <div class="cal-status"><span class="badge badge-green">✅ Confirmed</span></div>
          <div class="cal-loc">📍 No location specified</div>
          <div class="cal-meta">No description. Likely Physical Therapy or Personal Training session.</div>
          <div class="cal-prep">⚠️ Prep: Confirm location and format. If PT (physical therapy), bring relevant records from Monday's new patient visit.</div>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ SECTION 5: JOB SEARCH & INTERVIEW PIPELINE -->
<div class="section green">
  <div class="section-title">💼 Section 5 — Job Search &amp; Interview Pipeline</div>
  <div class="section-body">
    <table>
      <thead>
        <tr>
          <th>Fit</th>
          <th>Role / Source</th>
          <th>Company</th>
          <th>Type</th>
          <th>Status</th>
          <th>Next Step</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="badge badge-high">HIGH</span></td>
          <td>Vice President Human Resources</td>
          <td>PeopleOps Jobs</td>
          <td>LinkedIn Job Alert (×2)</td>
          <td>Not yet applied</td>
          <td>Apply ASAP — two separate alerts signal strong match</td>
        </tr>
        <tr>
          <td><span class="badge badge-high">HIGH</span></td>
          <td>Director of People &amp; Culture</td>
          <td>Galvanize USA (Remote)</td>
          <td>Glassdoor Alert</td>
          <td>Not yet applied</td>
          <td>Review Glassdoor alert; apply if qualifications match</td>
        </tr>
        <tr>
          <td><span class="badge badge-high">HIGH</span></td>
          <td>Principal People Partner</td>
          <td>Pie Insurance</td>
          <td>Self-noted (Greenhouse link)</td>
          <td>Intent noted — confirm if submitted</td>
          <td>Verify application submitted; follow up if needed</td>
        </tr>
        <tr>
          <td><span class="badge badge-medium">MED</span></td>
          <td>Human Resources Executive</td>
          <td>Target</td>
          <td>LinkedIn Alert</td>
          <td>Not yet applied</td>
          <td>Review role; Target is large org — assess culture fit</td>
        </tr>
        <tr>
          <td><span class="badge badge-medium">MED</span></td>
          <td>+7 Remote HR/People Roles</td>
          <td>Various (incl. Affirm)</td>
          <td>Glassdoor Alert</td>
          <td>Not yet reviewed</td>
          <td>Open Glassdoor digest and review all 8 roles in batch</td>
        </tr>
        <tr>
          <td><span class="badge badge-medium">MED</span></td>
          <td>+10 NY Metro HR Roles</td>
          <td>Various (incl. LG Electronics NA, IWG)</td>
          <td>Glassdoor Alert (NY)</td>
          <td>Not yet reviewed</td>
          <td>Review; Community Associate is likely low fit — prioritize Sr. roles</td>
        </tr>
        <tr>
          <td><span class="badge badge-high">HIGH</span></td>
          <td>HR Networking &amp; Job Search Group</td>
          <td>Community (170+ HR professionals)</td>
          <td>Networking Event — Wed 9/16 12 PM</td>
          <td>⚠️ RSVP Pending</td>
          <td>Accept invite; prepare intro + target role list</td>
        </tr>
        <tr>
          <td><span class="badge badge-high">HIGH</span></td>
          <td>HR Open Office Hours</td>
          <td>Community (same group)</td>
          <td>Networking Event — Thu 9/17 12 PM</td>
          <td>⚠️ RSVP Pending</td>
          <td>Accept invite; prepare open discussion questions</td>
        </tr>
        <tr>
          <td><span class="badge badge-medium">MED</span></td>
          <td>M&amp;M Meeting (Monte Montoya)</td>
          <td>Individual — monte.montoya@gmail.com</td>
          <td>1:1 Meeting — Tue 9/15 3 PM</td>
          <td>✅ Accepted</td>
          <td>Confirm format; prepare agenda/talking points if job-related</td>
        </tr>
        <tr>
          <td><span class="badge badge-low">LOW</span></td>
          <td>Blotato AI Tool (self-noted)</td>
          <td>Blotato.com</td>
          <td>Self-sent research link</td>
          <td>Bookmarked</td>
          <td>Review when time permits — AI tools for job search or personal brand</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ SECTION 6: FULL EMAIL REVIEW BY CATEGORY -->
<div class="section navy">
  <div class="section-title">📧 Section 6 — Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="card card-red">
      <h4>🔴 Security / Risk — 11 Emails</h4>
      <div class="meta">Includes auto-trashed phishing, active spam in inbox, and financial alerts</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Type</th><th>Sender / Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td><span class="badge badge-green">✅ RESCUED</span></td><td>Experian Alerts — "New alerts on your credit file" <span class="rescued-note">(rescued from Trash)</span></td><td>🔴 Open Experian NOW — review all alerts</td></tr>
          <tr><td><span class="badge badge-red">🗑 AUTO-TRASHED</span></td><td>"Payment_Declined" (unicode spoofed) — "We've Blocked Your Account! Your photos/videos will be deleted on melissaw212"</td><td><span class="phishing-note">Auto-trashed: Spoofed sender with unicode lookalike characters, impersonating cloud storage, urgent account threat. No action needed.</span></td></tr>
          <tr><td><span class="badge badge-red">🗑 AUTO-TRASHED</span></td><td>"Cloud Storage" (gibberish domain) — "Storage Limit Reached (100%)"</td><td><span class="phishing-note">Auto-trashed: Spoofed billing/payment urgency to harvest credentials. No action needed.</span></td></tr>
          <tr><td><span class="badge badge-red">🗑 AUTO-TRASHED</span></td><td>"Lowe's" (spoofed — melissaw212@vtsvjdogykxfe) — "Your Lowe's Kobalt Tool Set Awaits"</td><td><span class="phishing-note">Auto-trashed: Spoofed retail brand with malformed domain (no TLD), fake prize/order scam. No action needed.</span></td></tr>
          <tr><td><span class="badge badge-gray">SPAM</span></td><td>Urology Secrets (gibberish domain) — "1 common food restores hard erections 🍆"</td><td>Delete / mark spam</td></tr>
          <tr><td><span class="badge badge-gray">SPAM</span></td><td>Private_Health_Notes (gibberish) — "The bedroom warning most men miss"</td><td>Delete / mark spam</td></tr>
          <tr><td><span class="badge badge-gray">SPAM</span></td><td>Military_Honey (gibberish) — "Thousands of men are using this trick to increase their size"</td><td>Delete / mark spam</td></tr>
          <tr><td><span class="badge badge-gray">SPAM</span></td><td>"Honey-Boost" (gibberish ×2) — "Watch the Honey Boost Presentation" (two instances)</td><td>Delete / mark spam</td></tr>
          <tr><td><span class="badge badge-gray">SPAM</span></td><td>"Women's-Wellness" (gibberish ×2) — "Better Wellness Starts with One Daily Habit" (two instances)</td><td>Delete / mark spam</td></tr>
          <tr><td><span class="badge badge-gray">SPAM</span></td><td>🔶FUCK-BUDDY SECRET🔴 (gibberish) — explicit adult content</td><td>Delete / mark spam — already in Trash</td></tr>
        </tbody>
      </table>
      <div class="action" style="margin-top:8px;">→ <strong>Immediate:</strong> Check Experian. Report persistent spam domains to Gmail as phishing. Consider enabling stricter spam filters.</div>
    </div>

    <!-- GAMBLING SPAM -->
    <div class="card card-red">
      <h4>🎰 Gambling / Casino Spam — 8 Emails</h4>
      <div class="meta">All from gibberish/spoofed domains. All spam or phishing.</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th></tr></thead>
        <tbody>
          <tr><td>kysupporteubn@cntolvksdqxqmhglbtlmncdp.com (as melissaw212)</td><td>Use Code: 200GETLUCKY for welcome bonus + 30 free spins 💰</td><td>Not trashed — delete</td></tr>
          <tr><td>OrbitSpins.Casino (gibberish)</td><td>A Special Welcome Is Waiting at OrbitSpins</td><td>Not trashed — delete</td></tr>
          <tr><td>Congratulations (gibberish ×2)</td><td>No Deposit Needed! Free Spins — FREESPIN (two instances)</td><td>One in trash, one not — delete both</td></tr>
          <tr><td>Slots_Of_Vegas_Casino (gibberish)</td><td>Your 150 FREESPINS have been reserved.</td><td>Not trashed — delete</td></tr>
          <tr><td>melissaw212 (gibberish, spoofed ×2)</td><td>🎉 Congratulations melissaw212 $1000 Waiting — Miami Casino Club (two instances)</td><td>Both in Trash — safe to delete</td></tr>
          <tr><td>melissaw212 (gibberish spoofed)</td><td>✨ You've Just Won 175 FREE Spins — LITTLE175GRF</td><td>In Trash — safe to delete</td></tr>
        </tbody>
      </table>
      <div class="action" style="margin-top:8px;">→ Delete all. Mark senders as spam. None of these are legitimate.</div>
    </div>

    <!-- JOB SEARCH -->
    <div class="card card-green">
      <h4>💼 Job Search — 7 Emails</h4>
      <div class="meta">LinkedIn Job Alerts, Glassdoor, Self-noted applications</div>
      <ul class="bullets">
        <li><strong>LinkedIn (messages-noreply)</strong> — "Human Resources Executive: Target hired near you" (in inbox, unread) · <em>Review and apply if fit</em></li>
        <li><strong>LinkedIn Job Alerts</strong> — "PeopleOps Jobs is hiring a Vice President Human Resources" (in inbox, unread) · <em>High priority — apply ASAP</em></li>
        <li><strong>LinkedIn Job Alerts</strong> — "Vice President Human Resources at PeopleOps Jobs" (in inbox, unread — duplicate alert) · <em>Same role, confirms strong match signal</em></li>
        <li><strong>Glassdoor</strong> — "Director of People and Culture at Galvanize USA and 7 more jobs — Remote" (in Trash — rescue and review) · <em>High value, was trashed</em></li>
        <li><strong>Glassdoor</strong> — "Community Associate at IWG and 9 more jobs — New York, NY" (in Trash — review before deleting) · <em>Mixed relevance</em></li>
        <li><strong>Melissa W (self)</strong> — "Job Application for Principal People Partner at Pie Insurance" (in inbox, unread) · <em>Confirm application submitted</em></li>
        <li><strong>Melissa W (self)</strong> — "Blotato | #1 Social Media APIs for AI Agents, ChatGPT &amp; Claude" (in inbox, unread) · <em>Personal research / AI tool bookmark</em></li>
      </ul>
      <div class="action" style="margin-top:8px;">→ Prioritize VP HR at PeopleOps Jobs and Director at Galvanize USA. Bring both to Wednesday's HR Networking Group.</div>
    </div>

    <!-- CALENDAR / EVENTS -->
    <div class="card card-blue">
      <h4>📅 Calendar / Events — 1 Email</h4>
      <div class="meta">Notify NYC weather alert affecting upcoming schedule</div>
      <ul class="bullets">
        <li><strong>Notify NYC</strong> — "Flood Watch — 9/13 (NYC)" · In Inbox · Issued 9/12/2026 2:34 AM · <em>Flood Watch valid 2 AM – 11 PM Sunday 9/13</em></li>
      </ul>
      <div class="action">→ Monitor MTA/transit alerts Sunday evening for impact on Monday's 9:00 AM doctor appointment.</div>
    </div>

    <!-- MEDICAL / HEALTH -->
    <div class="card card-orange">
      <h4>🏥 Medical / Health — 2 Emails</h4>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>NewYork-Presbyterian</td><td>Could Varicose Veins Be More Than a Cosmetic Concern? + GLP-1s + fall allergies</td><td>In Trash</td><td>Review if interested in health content; safe to delete otherwise</td></tr>
          <tr><td>Remedy Meds</td><td>Addressing common myths &amp; concerns… (weight loss meds / GLP-1)</td><td>In Trash</td><td>Marketing email — safe to delete; unsubscribe if unwanted</td></tr>
        </tbody>
      </table>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="card card-yellow">
      <h4>💳 Financial / Billing — 1 Email</h4>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Experian Alerts (support@s.usa.experian.com)</td><td>Heads up Melissa! You have new alerts on your Experian credit file</td><td><span class="badge badge-green">✅ RESCUED from Trash</span></td><td>🔴 Log in to Experian TODAY — review all new alerts immediately</td></tr>
        </tbody>
      </table>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="card card-purple">
      <h4>📚 Professional Development — 2 Emails</h4>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Dylan's Diary (newsletter@lg.behindthemarkets.com)</td><td>Diesel Just Hit a Record. Nobody Reported It.</td><td>In Trash</td><td>Finance/market newsletter — review if relevant; otherwise safe to delete</td></tr>
          <tr><td>Justyn The AI Guy (hello@justyn.ca)</td><td>🤓 Nerd alert: My "command center" that saved my sanity (AI productivity)</td><td>In Trash</td><td>AI newsletter — relevant if exploring AI tools for job search; review or delete</td></tr>
        </tbody>
      </table>
    </div>

    <!-- PERSONAL -->
    <div class="card card-teal">
      <h4>👤 Personal — 4 Emails</h4>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Match (mailer@connect.match.com)</td><td>John likes you. See if it's mutual.</td><td>In Inbox (unread)</td><td>Review when time permits — Match.com activity notification</td></tr>
          <tr><td>Match (mailer@connect.match.com)</td><td>You've had a profile view from John (49, Sandusky OH)</td><td>In Inbox (unread)</td><td>Companion to above — same person</td></tr>
          <tr><td>Facebook (reminders@facebookmail.com)</td><td>Here's what's new from Cayla and others (Rosario, Sandru)</td><td>Not in inbox, read</td><td>Social notification — review at leisure; safe to archive</td></tr>
          <tr><td>Debbie on Facebook (close_friend_updates)</td><td>💬 Debbie Mantell Pollack commented: "Amazing! Congratulations!!!"</td><td>Not in inbox, read</td><td>Personal social — already read; archive or delete</td></tr>
        </tbody>
      </table>
    </div>

    <!-- NEWSLETTERS / SUBSCRIPTIONS -->
    <div class="card card-purple">
      <h4>📰 Newsletters &amp; Subscriptions — 2 Emails</h4>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Recommendation</th></tr></thead>
        <tbody>
          <tr><td>Medium Daily Digest (noreply@medium.com)</td><td>Why are lobsters boiled alive? | Giuseppe Frisella</td><td><span class="badge badge-orange">Auto-Trashed (newsletter)</span> + in inbox</td><td>Unsubscribe from Daily Digest if not reading regularly</td></tr>
          <tr><td>LinkedIn (messages-noreply@linkedin.com)</td><td>Human Resources Executive: Target hired near you (earlier version — read)</td><td>Not in inbox, already read</td><td>Keep LinkedIn job alerts — high value for active job search</td></tr>
        </tbody>
      </table>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ SECTION 7: TRASH REVIEW -->
<div class="section gray">
  <div class="section-title">🗑 Section 7 — Trash Review</div>
  <div class="section-body">

    <h4 style="color:#2e7d32; margin-bottom:8px;">✅ RESTORE IMMEDIATELY (1 email)</h4>
    <table style="margin-bottom:18px;">
      <thead><tr><th>Sender</th><th>Subject</th><th>Reason to Restore</th></tr></thead>
      <tbody>
        <tr style="background:#f1f8e9;">
          <td>Experian Alerts (support@s.usa.experian.com)</td>
          <td>Heads up Melissa! You have new alerts on your Experian credit file</td>
          <td><span class="rescued-note">✅ Already rescued. Legitimate Experian domain — critical financial/credit monitoring alert. Review immediately.</span></td>
        </tr>
      </tbody>
    </table>

    <h4 style="color:#f9a825; margin-bottom:8px;">⚠️ REVIEW BEFORE DELETING (4 emails)</h4>
    <table style="margin-bottom:18px;">
      <thead><tr><th>Sender</th><th>Subject</th><th>Why Review</th></tr></thead>
      <tbody>
        <tr>
          <td>Glassdoor Jobs</td>
          <td>Director of People and Culture at Galvanize USA and 7 more jobs — Remote</td>
          <td>High-value job alert. Remote roles include Galvanize USA Director of P&amp;C. Review all 8 before deleting.</td>
        </tr>
        <tr>
          <td>Glassdoor Jobs</td>
          <td>Community Associate at IWG and 9 more jobs — New York, NY</td>
          <td>Mixed relevance. Skim for senior HR/People roles in the 10-job list before deleting.</td>
        </tr>
        <tr>
          <td>NewYork-Presbyterian</td>
          <td>Could Varicose Veins Be More Than a Cosmetic Concern?</td>
          <td>Legitimate health newsletter from NYP. Contains GLP-1 heart info and 50+ checkup reminders. Quick skim if relevant.</td>
        </tr>
        <tr>
          <td>Justyn The AI Guy (hello@justyn.ca)</td>
          <td>🤓 Nerd alert: My "command center" that saved my sanity</td>
          <td>AI productivity content — potentially useful for job search tools exploration (reference to AI CFO finding $5K opportunity). Quick scan.</td>
        </tr>
      </tbody>
    </table>

    <h4 style="color:#c62828; margin-bottom:8px;">🗑 AUTO-TRASHED — Phishing (4 emails)</h4>
    <table style="margin-bottom:18px;">
      <thead><tr><th>Sender</th><th>Subject</th><th>Auto-Trash Reason</th></tr></thead>
      <tbody>
        <tr style="background:#fff8f8;">
          <td>"Payment_Declined" (unicode spoofed)</td>
          <td>We've Blocked Your Account! Your photos/videos will be deleted on melissaw212</td>
          <td class="phishing-note">Spoofed sender with unicode lookalike characters in display name, gibberish domain, impersonating cloud storage with urgent account-threat language</td>
        </tr>
        <tr style="background:#fff8f8;">
          <td>"Cloud Storage" (gibberish domain)</td>
          <td>Storage Limit Reached (100%)</td>
          <td class="phishing-note">Spoofed Cloud Storage sender from random gibberish domain, urgent billing/payment expiry threat demanding immediate action</td>
        </tr>
        <tr style="background:#fff8f8;">
          <td>"Lowe's" (spoofed — melissaw212@vtsvjdogykxfe)</td>
          <td>melissaw212 Your Lowe's Kobalt Tool Set Awaits</td>
          <td class="phishing-note">Spoofed Lowe's brand using recipient's own email as sender, malformed domain with no TLD — fake prize/order scam</td>
        </tr>
        <tr style="background:#fff8f8;">
          <td>Medium Daily Digest (noreply@medium.com)</td>
          <td>Why are lobsters boiled alive? | Giuseppe Frisella</td>
          <td class="rescued-note">Auto-Trashed as Newsletter — legitimate sender but digest auto-removed. Also appears in inbox.</td>
        </tr>
      </tbody>
    </table>

    <h4 style="color:#546e7a; margin-bottom:8px;">🗑 SAFE TO DELETE — Trash (26 emails)</h4>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Reason</th></tr></thead>
      <tbody>
        <tr><td>VIVAIA</td><td>NEW: Ankle Boots Take the Lead 🍂</td><td>Promotional retail — already trashed</td></tr>
        <tr><td>Quince</td><td>New arrivals, fall POV</td><td>Promotional retail
