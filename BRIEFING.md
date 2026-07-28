<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa Weiss — July 28, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 20px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); color: white; padding: 32px 36px; border-radius: 16px; margin-bottom: 24px; box-shadow: 0 8px 32px rgba(0,0,0,0.3); }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 15px; color: #a8b4d8; margin-top: 6px; }
  .header .meta { display: flex; gap: 24px; margin-top: 16px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.1); padding: 8px 16px; border-radius: 8px; font-size: 13px; }
  .header .meta-item span { font-weight: 700; color: #7ec8e3; }

  /* SECTION HEADERS */
  .section { margin-bottom: 28px; }
  .section-header { display: flex; align-items: center; gap: 10px; margin-bottom: 14px; padding-bottom: 8px; border-bottom: 2px solid #e2e8f0; }
  .section-header h2 { font-size: 17px; font-weight: 700; color: #1a1a2e; }
  .section-number { background: #1a1a2e; color: white; width: 26px; height: 26px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; flex-shrink: 0; }

  /* COLOR BANDS */
  .band-red { border-left: 5px solid #e53e3e; background: #fff5f5; }
  .band-yellow { border-left: 5px solid #d69e2e; background: #fffff0; }
  .band-blue { border-left: 5px solid #3182ce; background: #ebf8ff; }
  .band-green { border-left: 5px solid #38a169; background: #f0fff4; }
  .band-purple { border-left: 5px solid #805ad5; background: #faf5ff; }
  .band-gray { border-left: 5px solid #718096; background: #f7fafc; }
  .band-orange { border-left: 5px solid #dd6b20; background: #fffaf0; }

  /* CARDS */
  .card { padding: 16px 20px; border-radius: 10px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .card h3 { font-size: 14px; font-weight: 700; margin-bottom: 6px; }
  .card .label { display: inline-block; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 12px; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px; }
  .label-red { background: #fed7d7; color: #c53030; }
  .label-yellow { background: #fefcbf; color: #975a16; }
  .label-blue { background: #bee3f8; color: #2b6cb0; }
  .label-green { background: #c6f6d5; color: #276749; }
  .label-purple { background: #e9d8fd; color: #553c9a; }
  .label-gray { background: #e2e8f0; color: #4a5568; }
  .label-orange { background: #feebc8; color: #9c4221; }

  .card .meta-row { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 6px; font-size: 12px; color: #718096; }
  .card .meta-row strong { color: #4a5568; }
  .card .action-next { margin-top: 8px; padding: 8px 12px; background: rgba(0,0,0,0.04); border-radius: 6px; font-size: 13px; }
  .card .action-next strong { color: #2d3748; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #2d3748; color: white; padding: 10px 12px; text-align: left; font-weight: 600; }
  td { padding: 9px 12px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  tr:nth-child(even) td { background: #f7fafc; }
  tr:hover td { background: #edf2f7; }
  .tbl-wrapper { border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 16px; }

  /* STATUS BADGES */
  .badge { display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 11px; font-weight: 700; }
  .badge-red { background: #fed7d7; color: #c53030; }
  .badge-green { background: #c6f6d5; color: #276749; }
  .badge-yellow { background: #fefcbf; color: #975a16; }
  .badge-blue { background: #bee3f8; color: #2b6cb0; }
  .badge-gray { background: #e2e8f0; color: #4a5568; }
  .badge-purple { background: #e9d8fd; color: #553c9a; }
  .badge-orange { background: #feebc8; color: #9c4221; }

  /* EXEC SUMMARY */
  .exec-bullets { list-style: none; padding: 0; }
  .exec-bullets li { padding: 12px 16px; border-radius: 8px; margin-bottom: 8px; font-size: 14px; display: flex; align-items: flex-start; gap: 10px; }
  .exec-bullets li .icon { font-size: 18px; flex-shrink: 0; }

  /* CALENDAR */
  .day-block { margin-bottom: 20px; }
  .day-label { background: #2d3748; color: white; padding: 8px 16px; border-radius: 8px 8px 0 0; font-weight: 700; font-size: 14px; }
  .cal-event { padding: 14px 18px; border-bottom: 1px solid #e2e8f0; background: white; }
  .cal-event:last-child { border-bottom: none; border-radius: 0 0 8px 8px; }
  .cal-event .event-time { font-weight: 700; color: #2b6cb0; font-size: 13px; }
  .cal-event .event-title { font-weight: 700; font-size: 14px; margin: 2px 0; }
  .cal-event .event-detail { font-size: 12px; color: #718096; margin-top: 3px; }
  .cal-event .event-detail a { color: #3182ce; }
  .conflict-warn { background: #fff5f5; border: 1px solid #fc8181; border-radius: 6px; padding: 4px 10px; font-size: 12px; color: #c53030; margin-top: 6px; display: inline-block; }

  /* PRIORITY COLORS */
  .pri-high { color: #c53030; font-weight: 700; }
  .pri-med { color: #d69e2e; font-weight: 700; }
  .pri-low { color: #718096; }

  /* TOP 3 */
  .top3 { counter-reset: top3; }
  .top3-item { display: flex; gap: 16px; align-items: flex-start; padding: 18px 20px; border-radius: 12px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
  .top3-num { font-size: 32px; font-weight: 900; opacity: 0.18; line-height: 1; }
  .top3-content h3 { font-size: 15px; font-weight: 700; margin-bottom: 4px; }
  .top3-content p { font-size: 13px; color: #4a5568; }

  /* DASHBOARD GRID */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-tile { background: white; border-radius: 12px; padding: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
  .dash-tile .tile-label { font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: #718096; font-weight: 600; margin-bottom: 6px; }
  .dash-tile .tile-value { font-size: 26px; font-weight: 800; }
  .dash-tile .tile-sub { font-size: 12px; color: #4a5568; margin-top: 4px; }
  .tv-red { color: #e53e3e; }
  .tv-green { color: #38a169; }
  .tv-blue { color: #3182ce; }
  .tv-yellow { color: #d69e2e; }
  .tv-purple { color: #805ad5; }

  /* TRIAGE TABLE SPECIAL */
  .triage-rescued td { background: #f0fff4 !important; }
  .triage-inbox td { background: #ebf8ff !important; }
  .triage-summary td { background: #f7fafc !important; font-style: italic; }

  /* SPAM WARNING BOX */
  .spam-box { background: #fff5f5; border: 2px solid #fc8181; border-radius: 10px; padding: 14px 18px; margin-bottom: 12px; }
  .spam-box h4 { color: #c53030; font-size: 14px; margin-bottom: 6px; }
  .spam-box p { font-size: 13px; color: #742a2a; }

  /* FOOTNOTE */
  .footnote { font-size: 12px; color: #718096; text-align: center; margin-top: 28px; padding-top: 16px; border-top: 1px solid #e2e8f0; }

  /* RESPONSIVE */
  @media (max-width: 700px) {
    .header .meta { gap: 10px; }
    .dash-grid { grid-template-columns: 1fr 1fr; }
  }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════
     HEADER
════════════════════════════════════════════ -->
<div class="header">
  <h1>☀️ Good Morning, Melissa</h1>
  <div class="subtitle">Executive Briefing — Prepared by Your Chief of Staff</div>
  <div class="meta">
    <div class="meta-item">📅 <span>Tuesday, July 28, 2026</span></div>
    <div class="meta-item">📧 Total Emails Reviewed: <span>50</span></div>
    <div class="meta-item">📆 Calendar Events: <span>10</span></div>
    <div class="meta-item">⚠️ Action Required Items: <span>5</span></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════
     SECTION 0 — EMAIL TRIAGE QUICK LIST
════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">0</div>
    <h2>Email Triage Quick List</h2>
  </div>
  <div class="tbl-wrapper">
    <table>
      <thead>
        <tr>
          <th style="width:130px">Status</th>
          <th style="width:200px">From</th>
          <th>Subject</th>
          <th>Summary</th>
        </tr>
      </thead>
      <tbody>
        <!-- RESCUED -->
        <tr class="triage-rescued">
          <td><span class="badge badge-green">✅ RESCUED</span></td>
          <td>Google</td>
          <td>New privacy settings for Search services and Google Play</td>
          <td>Official Google account privacy update for missyw303@gmail.com — rescued from Trash; review settings.</td>
        </tr>
        <!-- INBOX EMAILS (individual) -->
        <tr class="triage-inbox">
          <td><span class="badge badge-blue">📥 INBOX</span></td>
          <td>NYU Langone MyChart</td>
          <td>New Message in NYU Langone Health MyChart</td>
          <td>Unread health message waiting — log in to view. Could be test results or appointment info.</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="badge badge-blue">📥 INBOX</span></td>
          <td>Bank of America</td>
          <td>Billing Dispute for account -4018 — Claim has been canceled</td>
          <td>Your billing dispute claim was canceled per your request. Companion dispute is being reviewed by merchant's bank.</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="badge badge-blue">📥 INBOX</span></td>
          <td>Bank of America</td>
          <td>Billing Dispute for account -4018 — Please provide additional information ASAP</td>
          <td>⚠️ Action needed — BofA requests additional info to process your dispute. Deadline-sensitive.</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="badge badge-blue">📥 INBOX</span></td>
          <td>Inclusively</td>
          <td>melissa weiss — Check out these recommended jobs for you!</td>
          <td>Job recommendations based on your profile — review for relevant matches.</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="badge badge-blue">📥 INBOX</span></td>
          <td>Chick-fil-A</td>
          <td>A little something to say thank you 🎁</td>
          <td>Free reward available on your account (402 pts). Low priority but expires.</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="badge badge-blue">📥 INBOX</span></td>
          <td>Lands' End</td>
          <td>One day only: 50% off + extra 10% off</td>
          <td>TODAY ONLY promotional sale. Low priority.</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="badge badge-blue">📥 INBOX</span></td>
          <td>Zappos</td>
          <td>On the hunt for your next statement shoe?</td>
          <td>Retail promotional email. Low priority.</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="badge badge-blue">📥 INBOX</span></td>
          <td>Microsoft</td>
          <td>Stop guessing at prompts — master the technique</td>
          <td>Microsoft Copilot AI training sessions. Professional development opportunity.</td>
        </tr>
        <!-- SUMMARY ROWS -->
        <tr class="triage-summary">
          <td><span class="badge badge-gray">🗂 TRASH (manual)</span></td>
          <td colspan="3">19 emails manually in Trash — see Trash Review section for details (includes newsletters, retail, spam, and one rescued Google email).</td>
        </tr>
        <tr class="triage-summary">
          <td><span class="badge badge-gray">🗑 TRASHED (auto)</span></td>
          <td colspan="3">1 email auto-trashed as newsletter (Medium Daily Digest) — see Trash Review &amp; Newsletters sections.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════
     SECTION 1 — EXECUTIVE SUMMARY
════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">1</div>
    <h2>Executive Summary</h2>
  </div>
  <ul class="exec-bullets">
    <li class="card band-red">
      <span class="icon">🚨</span>
      <div><strong>Biggest Risk / Urgent:</strong> Bank of America has flagged your dispute on account ending -4018 as requiring <em>additional information as soon as possible</em> to avoid losing your claim. A second alert confirms a related claim was already canceled. This requires immediate attention today. Additionally, your NYU Langone MyChart has an unread message — could be clinical results requiring timely follow-up.</div>
    </li>
    <li class="card band-green">
      <span class="icon">💼</span>
      <div><strong>Biggest Job Search / Opportunity:</strong> You have a live interview <em>today at 10:30 AM EDT</em> with Elliptic for the Head of People – U.S. role (Talent Partner Screen with Christopher Ratcliffe via Zoom). A direct deposit of $760.38 from NYS DOL UI confirms unemployment benefits are active. Inclusively sent new job recommendations to review.</div>
    </li>
    <li class="card band-blue">
      <span class="icon">📆</span>
      <div><strong>Biggest Calendar / Deadline:</strong> Today's Elliptic interview is your most time-sensitive commitment (10:30 AM). Tomorrow (Wed 7/29) is a packed day with three overlapping or back-to-back events: PromptMates Live (11 AM), HR Benefits Roundtable (12 PM), and HR Networking &amp; Job Search Group (12–1:30 PM) — two of those conflict directly. RSVP decisions needed for Thursday's Gloat live session and the Executive Roundtable (currently declined for Thu 7/30).</div>
    </li>
  </ul>
</div>

<!-- ═══════════════════════════════════════════
     SECTION 2 — ACTION REQUIRED
════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">2</div>
    <h2>Action Required</h2>
  </div>

  <div class="card band-red">
    <span class="label label-red">🔴 URGENT — Financial</span>
    <h3>Bank of America Billing Dispute — Additional Info Needed (Account -4018)</h3>
    <div class="meta-row"><strong>Source:</strong> Bank of America (onlinebanking@ealerts.bankofamerica.com) &nbsp;|&nbsp; <strong>Date:</strong> Mon Jul 27, 11:53 PM</div>
    <div class="meta-row"><strong>Why it matters:</strong> BofA is requesting additional documentation to process your billing dispute. Failure to respond promptly may result in the claim being closed — a separate claim on the same account was already canceled. Step 2 of 3 is pending.</div>
    <div class="action-next"><strong>➡ Next Step:</strong> Log in to BofA online banking immediately and provide the requested documentation. Call 1-800-432-1000 if unclear what is needed.</div>
    <div class="meta-row"><strong>⏰ Due:</strong> As soon as possible — today</div>
  </div>

  <div class="card band-blue">
    <span class="label label-blue">🔵 TODAY — Interview</span>
    <h3>Elliptic — Talent Partner Screen, Head of People U.S.</h3>
    <div class="meta-row"><strong>Source:</strong> Google Calendar (confirmed) &nbsp;|&nbsp; <strong>Time:</strong> 10:30–11:00 AM EDT today</div>
    <div class="meta-row"><strong>Why it matters:</strong> Live Zoom interview with Christopher Ratcliffe (Talentful Talent Lead) for a senior Head of People role at Elliptic.</div>
    <div class="action-next"><strong>➡ Next Step:</strong> Join via Zoom: https://elliptic-co.zoom.us/j/89752444403 | Meeting ID: 89752444403 | Desktop Passcode: %gG9*sA2fV | Dial-in: 1168138618. Prep your elevator pitch, key HR leadership examples, and questions about Elliptic's U.S. people strategy.</div>
    <div class="meta-row"><strong>⏰ Due:</strong> 10:30 AM TODAY</div>
  </div>

  <div class="card band-red">
    <span class="label label-red">🔴 URGENT — Health</span>
    <h3>Unread NYU Langone MyChart Message</h3>
    <div class="meta-row"><strong>Source:</strong> mychart.donotreply@nyulangone.org &nbsp;|&nbsp; <strong>Date:</strong> Tue Jul 28, 8:22 AM</div>
    <div class="meta-row"><strong>Why it matters:</strong> You have an unread message from your NYU Langone provider — could be test results, a prescription update, or appointment follow-up requiring timely response.</div>
    <div class="action-next"><strong>➡ Next Step:</strong> Log in to MyChart at nyulangone.org to read the message after your Elliptic interview.</div>
    <div class="meta-row"><strong>⏰ Due:</strong> Today</div>
  </div>

  <div class="card band-yellow">
    <span class="label label-yellow">🟡 FOLLOW-UP — Calendar</span>
    <h3>Wed Jul 29 Schedule Conflict — HR Roundtable vs. HR Networking Group (both 12:00 PM)</h3>
    <div class="meta-row"><strong>Source:</strong> Google Calendar &nbsp;|&nbsp; <strong>Date:</strong> Wed Jul 29, 12:00–1:00 PM and 12:00–1:30 PM</div>
    <div class="meta-row"><strong>Why it matters:</strong> Two events are scheduled simultaneously — "Future of Benefits HR Roundtable" and "HR Networking &amp; Job Search Group." Both have needsAction RSVP status. A third event "Network" is confirmed at the same time. Decision needed.</div>
    <div class="action-next"><strong>➡ Next Step:</strong> Decide which to attend. The HR Networking Group (12:00–1:30 PM) has 170+ attendees and strong peer networking value; the Benefits Roundtable (12:00–1:00 PM) is content-focused. RSVP to at least one today.</div>
    <div class="meta-row"><strong>⏰ Due:</strong> Today (before Wed)</div>
  </div>

  <div class="card band-green">
    <span class="label label-green">🟢 OPPORTUNITY — Google Privacy</span>
    <h3>Google Account Privacy Settings Update (Rescued from Trash)</h3>
    <div class="meta-row"><strong>Source:</strong> google-noreply@google.com &nbsp;|&nbsp; <strong>Date:</strong> Tue Jul 28, 3:13 AM</div>
    <div class="meta-row"><strong>Why it matters:</strong> Legitimate Google notification about new privacy settings for your missyw303@gmail.com account — covers saved history and personalized recommendations. Was erroneously trashed and rescued.</div>
    <div class="action-next"><strong>➡ Next Step:</strong> Read and adjust your Google account privacy settings as desired. Low urgency but good housekeeping.</div>
    <div class="meta-row"><strong>⏰ Due:</strong> This week</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════
     SECTION 3 — FULL 7-DAY CALENDAR
════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">3</div>
    <h2>Full 7-Day Calendar</h2>
  </div>

  <!-- TODAY -->
  <div class="day-block">
    <div class="day-label">📅 Tuesday, July 28, 2026 — TODAY</div>
    <div style="border-radius:0 0 10px 10px; overflow:hidden; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
      <div class="cal-event band-blue" style="border-left:none;">
        <div class="event-time">10:30 AM – 11:00 AM EDT</div>
        <div class="event-title">🎯 Interview with Elliptic — Talent Partner Screen</div>
        <div class="event-detail">📍 Zoom: <a href="https://elliptic-co.zoom.us/j/89752444403?pwd=tNtT8ECe9DIsZ4kIXgmuDZGW8RBCDc.1" target="_blank">Join Meeting</a> | Meeting ID: 89752444403 | Passcode: %gG9*sA2fV (desktop) / 1168138618 (dial-in)</div>
        <div class="event-detail"><strong>Interviewer:</strong> Christopher Ratcliffe, Talentful Talent Lead | <strong>Role:</strong> Head of People – U.S.</div>
        <div class="event-detail"><strong>RSVP:</strong> <span class="badge badge-green">✅ Accepted</span></div>
        <div class="event-detail"><strong>⚡ Prep:</strong> Prepare HR leadership examples, knowledge of Elliptic (blockchain analytics company), questions about U.S. team structure and growth plans. Test Zoom audio/video 10 min early. Note: two calendar entries for same event — treat as one.</div>
      </div>
    </div>
  </div>

  <!-- WEDNESDAY -->
  <div class="day-block">
    <div class="day-label">📅 Wednesday, July 29, 2026</div>
    <div style="border-radius:0 0 10px 10px; overflow:hidden; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
      <div class="cal-event">
        <div class="event-time">11:00 AM – 12:00 PM EDT</div>
        <div class="event-title">🤖 How A VP Talent Builds with AI — PromptMates Live</div>
        <div class="event-detail">📍 <a href="https://luma.com/join/g-sAv9NHMvqDBBXrx" target="_blank">Luma Join Link</a></div>
        <div class="event-detail"><strong>RSVP:</strong> <span class="badge badge-green">✅ Accepted</span> | Free event for HR/Recruitment professionals on AI &amp; automation.</div>
        <div class="event-detail"><strong>⚡ Prep:</strong> Featured speaker: Emily Gransky (VP Talent). Come with questions about AI in talent acquisition. No conflicts at this time slot.</div>
      </div>
      <div class="cal-event">
        <div class="event-time">12:00 PM – 1:00 PM EDT</div>
        <div class="event-title">💡 The Future of Benefits: Why Healthcare Alone Isn't Enough — HIC HR &amp; L&amp;D Roundtable</div>
        <div class="event-detail">📍 <a href="https://us06web.zoom.us/j/5224221004?pwd=UU5YNmlFckpjQnlzc2FDMHFlNUhhUT09" target="_blank">Zoom Link</a></div>
        <div class="event-detail"><strong>RSVP:</strong> <span class="badge badge-yellow">⚠️ Needs Action</span> | Senior HR leaders roundtable featuring CEO of CareCrowd.</div>
        <div class="conflict-warn">⚠️ CONFLICT: Overlaps with HR Networking &amp; Job Search Group (12:00–1:30 PM). Decide which to attend.</div>
      </div>
      <div class="cal-event">
        <div class="event-time">12:00 PM – 1:30 PM EDT</div>
        <div class="event-title">🤝 HR Networking &amp; Job Search Group — Zoom 2</div>
        <div class="event-detail">📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a></div>
        <div class="event-detail"><strong>RSVP:</strong> <span class="badge badge-yellow">⚠️ Needs Action</span> | Large peer networking group (~170+ attendees) for job seekers in HR.</div>
        <div class="event-detail"><strong>Note:</strong> AI notetaking tools asked to be disabled. Open discussion format.</div>
        <div class="conflict-warn">⚠️ CONFLICT: Overlaps with Benefits Roundtable (12:00–1:00 PM). Choose one — or join Benefits Roundtable first hour then switch.</div>
      </div>
      <div class="cal-event">
        <div class="event-time">12:00 PM – 1:30 PM EDT</div>
        <div class="event-title">🔵 Network (Personal Block)</div>
        <div class="event-detail"><strong>RSVP:</strong> <span class="badge badge-green">✅ Confirmed</span> | Personal networking placeholder — overlaps with above events.</div>
        <div class="conflict-warn">⚠️ NOTE: Three events overlap at noon. Consolidate your plans.</div>
      </div>
    </div>
  </div>

  <!-- THURSDAY -->
  <div class="day-block">
    <div class="day-label">📅 Thursday, July 30, 2026</div>
    <div style="border-radius:0 0 10px 10px; overflow:hidden; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
      <div class="cal-event">
        <div class="event-time">9:00 AM – 10:30 AM EDT</div>
        <div class="event-title">📊 Executive Roundtable — John Madigan (Zoom)</div>
        <div class="event-detail">📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> | Meeting ID: 207 786 667 | Password: 205454</div>
        <div class="event-detail"><strong>RSVP:</strong> <span class="badge badge-red">❌ Declined</span> | You have declined this event. Reconsider if relevant to your job search networking.</div>
      </div>
      <div class="cal-event">
        <div class="event-time">12:00 PM – 1:00 PM EDT</div>
        <div class="event-title">🤝 HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
        <div class="event-detail">📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a></div>
        <div class="event-detail"><strong>RSVP:</strong> <span class="badge badge-yellow">⚠️ Needs Action</span> | Open discussion, no recording. Peer HR networking/job search support.</div>
        <div class="event-detail"><strong>⚡ Prep:</strong> Note from Gloat email — Jeff Schwartz &amp; Heather Yurko live Thursday; check if separate event. Come with a question.</div>
      </div>
    </div>
  </div>

  <!-- FRIDAY / WEEKEND -->
  <div class="day-block">
    <div class="day-label">📅 Friday, July 31 — Sunday, August 2, 2026</div>
    <div style="border-radius:0 0 10px 10px; overflow:hidden; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
      <div class="cal-event">
        <div class="event-time">No events scheduled Fri Jul 31</div>
        <div class="event-title" style="color:#718096; font-style:italic;">Clear day — use for follow-up emails and job applications.</div>
      </div>
      <div class="cal-event">
        <div class="event-time">Sat Aug 1 — 2:30 PM – 3:30 PM EDT</div>
        <div class="event-title">👁️ Eye Doctor Appointment</div>
        <div class="event-detail"><strong>RSVP:</strong> <span class="badge badge-green">✅ Confirmed</span> | Location not specified — confirm address before Sat.</div>
        <div class="event-detail"><strong>⚡ Prep:</strong> Confirm appointment location/address. Allow travel time.</div>
      </div>
      <div class="cal-event">
        <div class="event-time">Sun Aug 2 (All Day)</div>
        <div class="event-title">🎂 Shari's Birthday</div>
        <div class="event-detail"><strong>RSVP:</strong> <span class="badge badge-green">✅ Confirmed</span> | Don't forget to send a message or plan accordingly!</div>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════
     SECTION 4 — JOB SEARCH & INTERVIEW PIPELINE
════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">4</div>
    <h2>Job Search &amp; Interview Pipeline</h2>
  </div>

  <div class="card band-green">
    <span class="label label-green">🟢 ACTIVE INTERVIEW</span>
    <h3>Elliptic — Head of People, U.S.</h3>
    <div class="meta-row"><strong>Stage:</strong> Talent Partner Screen (Christopher Ratcliffe, Talentful) &nbsp;|&nbsp; <strong>Today 10:30 AM EDT</strong></div>
    <div class="meta-row"><strong>Fit:</strong> <span class="badge badge-green">HIGH</span> &nbsp;|&nbsp; Senior People leadership role at blockchain analytics company</div>
    <div class="action-next"><strong>➡ Action:</strong> Attend interview today. Prep your story. Send thank-you note within 2 hours of completion.</div>
  </div>

  <div class="card band-green">
    <span class="label label-green">🟢 JOB ALERTS</span>
    <h3>Inclusively — Recommended Job Matches</h3>
    <div class="meta-row"><strong>Source:</strong> contactus@inclusively.com &nbsp;|&nbsp; <strong>Date:</strong> Tue Jul 28, 8:30 AM &nbsp;|&nbsp; <span class="badge badge-blue">INBOX — UNREAD</span></div>
    <div class="meta-row"><strong>Fit:</strong> <span class="badge badge-yellow">MEDIUM</span> &nbsp;|&nbsp; Inclusively specializes in inclusive hiring; matches based on your profile</div>
    <div class="action-next"><strong>➡ Action:</strong> Review job recommendations after your Elliptic interview. Note any strong matches for applications this week.</div>
  </div>

  <div class="card band-purple">
    <span class="label label-purple">🟣 NETWORKING EVENT</span>
    <h3>Gloat — Live Session: Jeff Schwartz &amp; Heather Yurko, Thursday</h3>
    <div class="meta-row"><strong>Source:</strong> Danny Shteinberg / team@gloat.com &nbsp;|&nbsp; <strong>Date:</strong> Tue Jul 28 (promoting Thu event)</div>
    <div class="meta-row"><strong>Fit:</strong> <span class="badge badge-yellow">MEDIUM</span> &nbsp;|&nbsp; Workforce/talent future of work thought leaders. Relevant to HR strategy roles.</div>
    <div class="action-next"><strong>➡ Action:</strong> Confirm Thursday calendar entry. Come with a question. Good visibility opportunity.</div>
  </div>

  <div class="card band-purple">
    <span class="label label-purple">🟣 NETWORKING EVENT</span>
    <h3>HR Networking &amp; Job Search Group — Wed Jul 29, 12:00 PM</h3>
    <div class="meta-row"><strong>RSVP:</strong> Needs Action &nbsp;|&nbsp; <strong>Fit:</strong> <span class="badge badge-green">HIGH</span> &nbsp;|&nbsp; Large peer HR/job search community, very relevant to active search</div>
    <div class="action-next"><strong>➡ Action:</strong> RSVP today. Conflicts with Benefits Roundtable — choose your priority session.</div>
  </div>

  <div class="card band-purple">
    <span class="label label-purple">🟣 PROFESSIONAL DEVELOPMENT</span>
    <h3>PromptMates Live — How A VP Talent Builds with AI — Wed Jul 29, 11 AM</h3>
    <div class="meta-row"><strong>RSVP:</strong> Accepted &nbsp;|&nbsp; <strong>Fit:</strong> <span class="badge badge-green">HIGH</span> &nbsp;|&nbsp; Directly relevant to AI in HR/Talent; strengthens your skills positioning</div>
    <div class="action-next"><strong>➡ Action:</strong> Attend. Take notes on AI tools to reference in interviews.</div>
  </div>

  <div class="card band-purple">
    <span class="label label-purple">🟣 ROUNDTABLE</span>
    <h3>Future of Benefits HR Roundtable — Wed Jul 29, 12:00 PM</h3>
    <div class="meta-row"><strong>RSVP:</strong> Needs Action &nbsp;|&nbsp; <strong>Fit:</strong> <span class="badge badge-yellow">MEDIUM</span> &nbsp;|&nbsp; Benefits/total rewards knowledge relevant to CPO/Head of People roles</div>
    <div class="action-next"><strong>➡ Action:</strong> RSVP if you choose this over HR Networking. Conflicts with that session — decide today.</div>
  </div>

  <div class="card band-green">
    <span class="label label-green">🟢 LINKEDIN CONNECTIONS</span>
    <h3>New LinkedIn Connections: Michael Sullivan &amp; Holly Hogan accepted your invitations</h3>
    <div class="meta-row"><strong>Source:</strong> invitations@linkedin.com &nbsp;|&nbsp; <strong>Date:</strong> Tue Jul 28</div>
    <div class="meta-row"><strong>Pending:</strong> Praise Boyinde (Founder, Sonaopus) wants to connect — awaiting your response</div>
    <div class="action-next"><strong>➡ Action:</strong> Send warm follow-up message to Michael Sullivan and Holly Hogan. Review Praise Boyinde's profile and decide whether to accept.</div>
  </div>

  <div class="card band-green">
    <span class="label label-green">🟢 RESEARCH STUDY OPPORTUNITY</span>
    <h3>Sago — Fun Dog Owner Study ($225.00) — Aug 10–17, 2026</h3>
    <div class="meta-row"><strong>Source:</strong> Participate@focusgroup.com &nbsp;|&nbsp; <strong>Fit:</strong> <span class="badge badge-yellow">MEDIUM</span> &nbsp;|&nbsp; Supplemental income while job searching</div>
    <div class="action-next"><strong>➡ Action:</strong> Complete pre-qualification survey if interested. $225 for a study between Aug 10–17. Low time investment.</div>
  </div>

  <div class="card band-yellow">
    <span class="label label-yellow">🟡 CAREER COACHING</span>
    <h3>Lisa Rangel / Chameleon Resumes — "Your Career is a Business"</h3>
    <div class="meta-row"><strong>Source:</strong> lr@chameleonresumes.com &nbsp;|&nbsp; <strong>Status:</strong> <span class="badge badge-gray">In Trash</span></div>
    <div class="meta-row"><strong>Fit:</strong> <span class="badge badge-yellow">MEDIUM</span> &nbsp;|&nbsp; Resume/personal brand advice — potentially useful for active job search</div>
    <div class="action-next"><strong>➡ Action:</strong> Rescue from trash and skim if you want career marketing tips. Otherwise safe to delete if not interested.</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════
     SECTION 5 — FULL EMAIL REVIEW BY CATEGORY
════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">5</div>
    <h2>Full Email Review by Category</h2>
  </div>

  <!-- 5A SECURITY / RISK -->
  <div class="card band-red" style="margin-bottom:16px;">
    <span class="label label-red">🔴 Security / Risk</span>
    <h3>Spam / Phishing — 8 Emails Identified</h3>
    <p style="font-size:13px; margin-bottom:10px;">These emails contain explicit spam, phishing attempts, fake casino winnings, or other high-risk content. They should be deleted/blocked immediately. None are in the main inbox.</p>
    <div class="tbl-wrapper">
      <table>
        <thead><tr><th>Sender/Subject</th><th>Status</th><th>Risk Type</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>"Sex Trick" — Make her squirt 3x tonight (×3 variations)</td><td><span class="badge badge-red">Spam/Phishing</span></td><td>Adult spam, random domain</td><td>Delete / Block</td></tr>
          <tr><td>"Missing Teeth?" — ShinySmile Veneers (in Trash)</td><td><span class="badge badge-gray">In Trash</span></td><td>Phishing/scam veneer ad</td><td>Already trashed</td></tr>
          <tr><td>"Rock Hard" — ½ Tsp Brown Powder kills ED</td><td><span class="badge badge-red">Spam</span></td><td>Health scam</td><td>Delete / Block</td></tr>
          <tr><td>Mia Kalifa viral video (Sex Trick)</td><td><span class="badge badge-red">Spam</span></td><td>Adult spam</td><td>Delete / Block</td></tr>
          <tr><td>Lung Clearing Method — COPD natural protocol</td><td><span class="badge badge-red">Spam</span></td><td>Health scam</td><td>Delete / Block</td></tr>
          <tr><td>ManForceX — bedroom performance</td><td><span class="badge badge-red">Spam</span></td><td>Health scam</td><td>Delete / Block</td></tr>
          <tr><td>💲 BANK CHEC K — Raging Bull Casino $50,000 (in Trash)</td><td><span class="badge badge-gray">In Trash</span></td><td>Casino phishing scam</td><td>Already trashed</td></tr>
          <tr><td>Bettywins Casino — 200 Free Spins for melissaw212</td><td><span class="badge badge-red">Spam</span></td><td>Casino phishing scam</td><td>Delete / Block</td></tr>
        </tbody>
      </table>
    </div>
    <div class="spam-box">
      <h4>⚠️ Note on Spam Volume</h4>
      <p>Your email address (melissaw212) appears to be harvested by spam networks. Consider enabling stronger spam filters in Gmail settings, and review whether your address has been exposed in any data breaches via HaveIBeenPwned.com.</p>
    </div>
  </div>

  <!-- 5B JOB SEARCH -->
  <div class="card band-green">
    <span class="label label-green">🟢 Job Search — 3 Emails</span>
    <h3>Active job search emails</h3>
    <div class="tbl-wrapper">
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Inclusively</td><td>melissa weiss — Check out recommended jobs</td><td><span class="badge badge-blue">Inbox / Unread</span></td><td>Review today</td></tr>
          <tr><td>Lisa Rangel (Chameleon Resumes)</td><td>Your career is a business</td><td><span class="badge badge-gray">Trash</span></td><td>Rescue + skim or delete</td></tr>
          <tr><td>Gemma Bonham-Carter</td><td>[Draft Week Day 2] Meet the players who will get you seen</td><td><span class="badge badge-gray">Trash</span></td><td>Rescue if interested in visibility strategy</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 5C RECRUITERS / NETWORKING -->
  <div class="card band-green">
    <span class="label label-green">🟢 Recruiters / Networking — 4 Emails</span>
    <h3>LinkedIn connections and recruiter outreach</h3>
    <div class="tbl-wrapper">
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Michael Sullivan via LinkedIn</td><td>Michael accepted your invitation — explore their network</td><td><span class="badge badge-gray">Read</span></td><td>Send follow-up message</td></tr>
          <tr><td>Holly Hogan via LinkedIn</td><td>Holly accepted your invitation — explore their network</td><td><span class="badge badge-gray">Read</span></td><td>Send follow-up message</td></tr>
          <tr><td>Praise Boyinde via LinkedIn</td><td>I want to connect (Founder, Sonaopus)</td><td><span class="badge badge-gray">Read / Pending</span></td><td>Review profile, accept or decline</td></tr>
          <tr><td>Danny Shteinberg (Gloat)</td><td>Your seat for Thursday's live session</td><td><span class="badge badge-blue">Unread</span></td><td>Confirm attendance, add to calendar</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 5D CALENDAR / EVENTS -->
  <div class="card band-blue">
    <span class="label label-blue">🔵 Calendar / Events — 2 Emails</span>
    <h3>Event invitations and confirmations</h3>
    <div class="tbl-wrapper">
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Sago (Focus Group)</td><td>Fun Dog Owner Study — Aug 10–17, $225</td><td><span class="badge badge-gray">Read</span></td><td>Complete pre-qual if interested</td></tr>
          <tr><td>Notify NYC</td><td>Missing Vulnerable Adult Alert — Joseph Dema (NYC)</td><td><span class="badge badge-orange">Unread / Alert</span></td><td>FYI — No action needed unless you have info</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 5E MEDICAL / HEALTH -->
  <div class="card band-red">
    <span class="label label-red">🔴 Medical / Health — 1 Email</span>
    <h3>NYU Langone MyChart — Unread Message</h3>
    <div class="tbl-wrapper">
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>NYU Langone MyChart</td><td>New Message in NYU Langone Health MyChart</td><td><span class="badge badge-red">INBOX — Unread</span></td><td>Log in to MyChart today — may require timely response</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 5F FINANCIAL / BILLING -->
  <div class="card band-yellow">
    <span class="label label-yellow">🟡 Financial / Billing — 4 Emails</span>
    <h3>Bank of America and direct deposit notifications</h3>
    <div class="tbl-wrapper">
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Bank of America</td><td>Billing Dispute -4018 — Please provide additional information ASAP</td><td><span class="badge badge-red">INBOX — URGENT</span></td><td>Log in to BofA immediately and respond</td></tr>
          <tr><td>Bank of America</td><td>Billing Dispute -4018 — Claim has been canceled</td><td><span class="badge badge-blue">INBOX — Read</span></td><td>Note for your records</td></tr>
          <tr><td>Bank of America</td><td>Billing Dispute -4018 — Claim being reviewed by merchant's bank</td><td><span class="badge badge-gray">Read</span></td><td>Monitor — no action yet</td></tr>
          <tr><td>Bank of America</td><td>Direct deposit credited — $760.38 from NYS DOL UI</td><td><span class="badge badge-green">Read — Good news</span></td><td>Unemployment deposit received. No action needed.</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 5G PROFESSIONAL DEVELOPMENT -->
  <div class="card band-purple">
    <span class="label label-purple">🟣 Professional Development — 3 Emails</span>
    <h3>Learning, AI tools, and HR industry resources</h3>
    <div class="tbl-wrapper">
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Microsoft</td><td>Stop guessing at prompts — master the technique (Copilot)</td><td><span class="badge badge-blue">INBOX — Unread</span></td><td>Review for AI training opportunities — relevant to HR tech positioning</td></tr>
          <tr><td>BambooHR</td><td>⚠️ Why Many Incentive Programs Stall</td><td><span class="badge badge-gray">Unread / Not in inbox</span></td><td>Read when time permits — relevant to compensation/HR strategy</td></tr>
          <tr><td>Google</td><td>New privacy settings (rescued from Trash)</td><td><span class="badge badge-green">✅ RESCUED</span></td><td>Review and update Google account privacy settings</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 5H PERSONAL -->
  <div class="card band-gray">
    <span class="label label-gray">⚪ Personal — 3 Emails</span>
    <h3>Personal account notifications, Match.com, USPS</h3>
    <div class="tbl-wrapper">
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Match</td><td>Persiderna likes you — see if it's mutual</td><td><span class="badge badge-gray">Read</span></td><td>Personal — review when you have time</td></tr>
          <tr><td>Match</td><td>Steve (68, New York) viewed your profile</td><td><span class="badge badge-gray">Read</span></td><td>Personal — review when you have time</td></tr>
          <tr><td>USPS Informed Delivery</td><td>Daily Digest Tue 7/28 — 3 mailpieces arriving</td><td><span class="badge badge-gray">Read</span></td><td>3 pieces of mail arriving today. FYI only.</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 5I NEWSLETTERS / SUBSCRIPTIONS -->
  <div class="card band-purple">
    <span class="label label-purple">🟣 Newsletters / Subscriptions — 8 Emails</span>
    <h3>News digests, industry newsletters, and subscription content</h3>
    <div class="tbl-wrapper">
      <table>
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Recommendation</th></tr></thead>
        <tbody>
          <tr><td>Medium Daily Digest</td><td>Long reads on Medium — membership expiring Aug 20</td><td><span class="badge badge-orange">Auto-Trashed (Newsletter)</span></td><td>⚠️ NOTE: Membership expires Aug 20, 2026 — decide whether to renew</td></tr>
          <tr><td>Medium Daily Digest</td><td>A Look Back at the YS Series (Josh Bycer)</td><td><span class="badge badge-gray">Trash</span></td><td>Delete — not aligned to your interests</td></tr>
          <tr><td>The Daily Skimm</td><td>My Diva Cup runneth over</td><td><span class="badge badge-gray">Unread / Not inbox</span></td><td>Keep or unsubscribe based on reading habits</td></tr>
          <tr><td>TLDR Newsletter</td><td>OpenAI $500B datacenter, Amazon Starlink rival, Nvidia SSI</td><td><span class="badge badge-gray">Trash</span></td><td>Useful tech news — rescue if interested; delete otherwise</td></tr>
          <tr><td>The AI Report</td><td>⚡ NVIDIA leads open AI defense</td><td><span class="badge badge-gray">Trash</span></td><td>Relevant to AI-forward HR positioning — consider rescuing</td></tr>
          <tr><td>Dylan's Diary (Behind the Markets)</td><td>60% Optimistic. 40% Cautious. AI Boom Phase 3.</td><td><span class="badge badge-gray">Trash</span></td><td>Finance/investment newsletter — keep or unsubscribe</td></tr>
          <tr><td>1% Better</td><td>Empty Playgrounds, SpaceX Drops, Side Hustle</td><td><span class="badge badge-gray">Trash</span></td><td>Self-improvement newsletter — delete if not reading</td></tr>
          <tr><td>The Average Joe</td><td>🗽 Risk — Circular finance jitters</td><td><span class="badge badge-gray">Trash</span></td><td>Finance newsletter — delete if not aligned</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 5J PROMOTIONAL / RETAIL -->
  <div class="card band-gray">
    <span class="label label-gray">⚪ Promotional / Retail — 12 Emails</span>
    <h3>Retail promotions, shopping offers, and service marketing</h3>
    <p style="font-size:13px; margin-bottom:10px;">See dedicated Promotional / Retail Summary section below for full breakdown.</p>
    <div class="tbl-wrapper">
      <table>
        <thead><tr><th>Sender</th><th>Subject</th><th>Today Only?</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Lands' End</td><td>One day only: 50% off + extra 10% off</td><td><span class="badge badge-red">TODAY ONLY</span></td><td>Review if interested — expires today</td></tr>
          <tr><td>Zappos</td><td>On the hunt for your next statement shoe?</td><td>No</td><td>Delete / Ignore</td></tr>
          <tr><td>Kohl's (Trash)</td><td>20% off ENDS TODAY</td><td><span class="badge badge-red">TODAY ONLY</span></td><td>Already trashed — ignore</td></tr>
          <tr><td>SHEIN (×2)</td><td>All under $14.99 / UNDER $10 Drops</td><td>No</td><td>Delete / Ignore</td></tr>
          <tr><td>YesStyle.com (Trash)</td><td>Anua x KPop Demon Hunters — up to 60% OFF</td><td>No</td><td>Already trashed — delete</td></tr>
          <tr><td>Carmel Car Service (×5)</td><td>Happy Ice Cream Sandwich Day! (sent to melissa, raymond, Customer)</td><td>No</td><td>Mass marketing — delete all</td></tr>
          <tr><td>Chick-fil-A</td><td>A little something to say thank you 🎁 (free reward)</td><td>No</td><td>Free reward available — claim if interested</td></tr>
        </tbody>
      </table>
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════
     SECTION 6 — TRASH REVIEW
════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">6</div>
    <h2>Trash Review</h2>
  </div>

  <div class="card band-green" style="margin-bottom:12px;">
    <span class="label label-green">✅ ALREADY RESCUED FROM TRASH</span>
    <h3>1 Email Rescued Before Briefing</h3>
    <div class="tbl-wrapper">
      <table>
        <thead><tr><th>Sender</th><th>Subject</th><th>Rescue Reason</th></tr></thead>
        <tbody>
          <tr><td>Google (google-noreply@google.com)</td><td>New privacy settings for Search services and Google Play</td><td>Official Google account notification — addressed to Melissa's Gmail (missyw303@gmail.com). Legitimate and important.</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card band-orange" style="margin-bottom:12px;">
    <span class="label label-orange">⚠️ AUTO-TRASHED — Newsletter</span>
