<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa — Friday, August 28, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }

  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px 60px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px; }
  .header h1 { font-size: 26px; font-weight: 700; letter-spacing: 0.5px; }
  .header .sub { font-size: 13px; color: #a8b4c8; margin-top: 6px; }
  .header-stats { display: flex; gap: 20px; flex-wrap: wrap; }
  .stat-pill { background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); border-radius: 20px; padding: 8px 18px; text-align: center; }
  .stat-pill .num { font-size: 22px; font-weight: 700; color: #e2e8f0; }
  .stat-pill .lbl { font-size: 11px; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.8px; }

  /* SECTION TITLE */
  .section-title { font-size: 16px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; margin: 28px 0 12px; padding-left: 12px; border-left: 4px solid; }
  .st-red { border-color: #dc2626; color: #dc2626; }
  .st-yellow { border-color: #d97706; color: #d97706; }
  .st-blue { border-color: #2563eb; color: #2563eb; }
  .st-green { border-color: #16a34a; color: #16a34a; }
  .st-purple { border-color: #7c3aed; color: #7c3aed; }
  .st-gray { border-color: #6b7280; color: #6b7280; }
  .st-dark { border-color: #1a1a2e; color: #1a1a2e; }
  .st-teal { border-color: #0891b2; color: #0891b2; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; border-left: 5px solid; }
  .card-red { background: #fef2f2; border-color: #dc2626; }
  .card-yellow { background: #fffbeb; border-color: #d97706; }
  .card-blue { background: #eff6ff; border-color: #2563eb; }
  .card-green { background: #f0fdf4; border-color: #16a34a; }
  .card-purple { background: #faf5ff; border-color: #7c3aed; }
  .card-gray { background: #f9fafb; border-color: #9ca3af; }
  .card-teal { background: #ecfeff; border-color: #0891b2; }

  .card h3 { font-size: 14px; font-weight: 700; margin-bottom: 6px; }
  .card .meta { font-size: 12px; color: #64748b; margin-bottom: 6px; }
  .card p { font-size: 13px; }
  .card .tag { display: inline-block; font-size: 11px; font-weight: 600; border-radius: 4px; padding: 2px 7px; margin-right: 4px; margin-top: 4px; }
  .tag-red { background: #fee2e2; color: #b91c1c; }
  .tag-yellow { background: #fef3c7; color: #92400e; }
  .tag-blue { background: #dbeafe; color: #1d4ed8; }
  .tag-green { background: #dcfce7; color: #15803d; }
  .tag-purple { background: #ede9fe; color: #6d28d9; }
  .tag-gray { background: #f3f4f6; color: #374151; }
  .tag-teal { background: #cffafe; color: #0e7490; }
  .tag-orange { background: #ffedd5; color: #c2410c; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; margin-bottom: 16px; }
  th { background: #1a1a2e; color: #e2e8f0; text-align: left; padding: 10px 12px; font-size: 12px; text-transform: uppercase; letter-spacing: 0.6px; }
  td { padding: 9px 12px; font-size: 13px; border-bottom: 1px solid #e5e7eb; vertical-align: top; }
  tr:nth-child(even) td { background: #f8fafc; }
  tr:hover td { background: #f1f5f9; }
  .tbl-wrap { background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,0.07); margin-bottom: 16px; }

  /* EXEC SUMMARY */
  .exec-summary { background: #fff; border-radius: 12px; padding: 22px 26px; margin-bottom: 16px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }
  .exec-bullet { display: flex; gap: 12px; align-items: flex-start; margin-bottom: 12px; }
  .exec-bullet:last-child { margin-bottom: 0; }
  .exec-icon { font-size: 20px; min-width: 28px; }
  .exec-text strong { display: block; font-size: 13px; font-weight: 700; margin-bottom: 2px; }
  .exec-text span { font-size: 13px; color: #374151; }

  /* DASHBOARD GRID */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; margin-bottom: 16px; }
  .dash-tile { background: #fff; border-radius: 10px; padding: 16px 18px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); border-top: 4px solid; }
  .dt-red { border-color: #dc2626; }
  .dt-yellow { border-color: #d97706; }
  .dt-blue { border-color: #2563eb; }
  .dt-green { border-color: #16a34a; }
  .dt-purple { border-color: #7c3aed; }
  .dt-gray { border-color: #9ca3af; }
  .dt-teal { border-color: #0891b2; }
  .dash-tile .dt-num { font-size: 28px; font-weight: 700; }
  .dash-tile .dt-lbl { font-size: 12px; color: #64748b; margin-top: 2px; }
  .dash-tile .dt-items { font-size: 12px; color: #374151; margin-top: 8px; border-top: 1px solid #f0f0f0; padding-top: 8px; }

  /* PRIORITY STRIP */
  .priority-strip { display: flex; gap: 14px; flex-wrap: wrap; margin-bottom: 20px; }
  .priority-card { flex: 1; min-width: 240px; background: #fff; border-radius: 12px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); border-top: 5px solid; }
  .pc-red { border-color: #dc2626; }
  .pc-yellow { border-color: #d97706; }
  .pc-blue { border-color: #2563eb; }
  .priority-card .pc-num { font-size: 32px; font-weight: 800; color: #e5e7eb; }
  .priority-card .pc-title { font-size: 15px; font-weight: 700; margin: 4px 0 6px; }
  .priority-card .pc-body { font-size: 13px; color: #374151; }

  /* BADGE */
  .badge { display: inline-block; border-radius: 12px; padding: 3px 10px; font-size: 11px; font-weight: 700; }
  .badge-red { background: #fee2e2; color: #b91c1c; }
  .badge-yellow { background: #fef3c7; color: #92400e; }
  .badge-green { background: #dcfce7; color: #15803d; }
  .badge-blue { background: #dbeafe; color: #1d4ed8; }
  .badge-gray { background: #f3f4f6; color: #374151; }
  .badge-purple { background: #ede9fe; color: #6d28d9; }
  .badge-orange { background: #ffedd5; color: #c2410c; }

  /* DIVIDER */
  hr.divider { border: none; border-top: 1px solid #e5e7eb; margin: 20px 0; }

  /* TRIAGE TABLE row colors */
  .row-rescued td { background: #f0fdf4 !important; }
  .row-inbox td { background: #eff6ff !important; }
  .row-trash td { background: #f9fafb !important; }

  /* MISC */
  .note { font-size: 12px; color: #6b7280; font-style: italic; margin-top: 6px; }
  .inline-list { padding-left: 18px; }
  .inline-list li { margin-bottom: 4px; font-size: 13px; }
  .accounting-total td { font-weight: 700; background: #1a1a2e !important; color: #fff; }
  .section-wrap { background: #fff; border-radius: 12px; padding: 20px 22px; margin-bottom: 18px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ════════════════════════════════════════════════════════
     0. EMAIL TRIAGE QUICK LIST
     ════════════════════════════════════════════════════════ -->
<div class="section-title st-dark" style="margin-top:0;">📋 Email Triage Quick List</div>
<div class="tbl-wrap">
<table>
  <thead>
    <tr>
      <th style="width:120px">Status</th>
      <th style="width:200px">From</th>
      <th>Subject</th>
      <th>Summary</th>
    </tr>
  </thead>
  <tbody>
    <!-- RESCUED ROWS FIRST -->
    <tr class="row-rescued">
      <td><span class="badge badge-green">✅ RESCUED</span></td>
      <td>Delta Air Lines</td>
      <td>First Time Ever: Earn 2 Delta Comfort Flight Certificates + 50K Bonus Miles</td>
      <td>Loyalty offer — 50K miles + 2 Comfort certs. Protected sender rescued from Trash.</td>
    </tr>
    <tr class="row-rescued">
      <td><span class="badge badge-green">✅ RESCUED</span></td>
      <td>My Best Buy® Visa® Card (Citi)</td>
      <td>Elevate your home with the Labor Day Appliances Sale</td>
      <td>Citi card promo — 18–24 mo. financing on appliances. Protected sender rescued from Trash.</td>
    </tr>
    <!-- INBOX ROWS -->
    <tr class="row-inbox">
      <td><span class="badge badge-blue">📥 INBOX</span></td>
      <td>Kevin Caldwell via LinkedIn</td>
      <td>Kevin accepted your invitation, explore their network</td>
      <td>New LinkedIn connection confirmed — explore Kevin's network for referrals.</td>
    </tr>
    <tr class="row-inbox">
      <td><span class="badge badge-blue">📥 INBOX</span></td>
      <td>LinkedIn Job Alerts</td>
      <td>Vice President – Absence Operations at ComPsych</td>
      <td>VP-level HR alert in inbox — high relevance, review promptly.</td>
    </tr>
    <tr class="row-inbox">
      <td><span class="badge badge-blue">📥 INBOX</span></td>
      <td>Ulta Beauty Orders</td>
      <td>We've received your order 👍</td>
      <td>Order confirmation received — track shipment as needed.</td>
    </tr>
    <!-- TRASH SUMMARY ROWS -->
    <tr class="row-trash">
      <td><span class="badge badge-gray">🗑 TRASHED (auto)</span></td>
      <td colspan="3">1 email auto-trashed (phishing) — see Trash Review. Auto-trashed: Fake SiriusXM subscription expiration (spoofed domain, payment harvesting).</td>
    </tr>
    <tr class="row-trash">
      <td><span class="badge badge-gray">🗂 TRASH (manual)</span></td>
      <td colspan="3">16 emails in Trash — see Trash Review. Includes newsletters, retail promos, spam, and junk flagged by Gmail filters.</td>
    </tr>
  </tbody>
</table>
</div>

<!-- ════════════════════════════════════════════════════════
     1. HEADER
     ════════════════════════════════════════════════════════ -->
<div class="header">
  <div>
    <div class="header h1" style="font-size:26px;font-weight:700;color:#fff;">Good Morning, Melissa ☀️</div>
    <div class="sub">Executive Briefing &nbsp;|&nbsp; Friday, August 28, 2026 &nbsp;|&nbsp; Prepared by your Chief of Staff</div>
  </div>
  <div class="header-stats">
    <div class="stat-pill"><div class="num">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="stat-pill"><div class="num">6</div><div class="lbl">Calendar Events</div></div>
    <div class="stat-pill"><div class="num">1</div><div class="lbl">Meeting Today</div></div>
    <div class="stat-pill"><div class="num">3</div><div class="lbl">Actions Required</div></div>
  </div>
</div>

<!-- ════════════════════════════════════════════════════════
     2. EXECUTIVE SUMMARY
     ════════════════════════════════════════════════════════ -->
<div class="section-title st-dark">🧭 Executive Summary</div>
<div class="exec-summary">
  <div class="exec-bullet">
    <div class="exec-icon">🔴</div>
    <div class="exec-text">
      <strong>Security / Risk — Ulta Account Address Change Requires Verification</strong>
      <span>Two Ulta emails arrived overnight confirming an address was <em>added</em> and then <em>updated</em> on your account — seconds apart. If you did not make these changes, your Ulta account may be compromised. Contact Ulta Guest Services immediately. Additionally, a Google notification confirms you shared data with SoundCloud — verify this was intentional.</span>
    </div>
  </div>
  <div class="exec-bullet">
    <div class="exec-icon">🟢</div>
    <div class="exec-text">
      <strong>Job Search — Strong Pipeline of VP/SVP-Level Opportunities Active</strong>
      <span>Multiple high-value alerts landed today: VP–Absence Operations at ComPsych (in inbox), Head of People at Anterior ($180K–$230K), Director HRBP–Commercial at Alnylam ($199K–$270K), and a $250K InMail from a recruiter on LinkedIn. Your networking group meets September 2 and 3.</span>
    </div>
  </div>
  <div class="exec-bullet">
    <div class="exec-icon">🔵</div>
    <div class="exec-text">
      <strong>Calendar — Virtual Call with Bryce Lowery at 10:30 AM Today + Reminder: Transfer Money Due Today</strong>
      <span>You have a confirmed VP, P&amp;C virtual call with bryce.lowery@intalegence.io at 10:30–11:15 AM ET. There is also an all-day reminder to transfer money today. Two networking sessions are upcoming Sep 2–3 (RSVP still needed for both). You declined the Sep 3 Executive Roundtable.</span>
    </div>
  </div>
</div>

<!-- ════════════════════════════════════════════════════════
     3. ACTION REQUIRED
     ════════════════════════════════════════════════════════ -->
<div class="section-title st-red">⚡ Action Required</div>

<div class="card card-red">
  <span class="tag tag-red">🔴 URGENT — SECURITY</span>
  <h3>Ulta Account: Address Added &amp; Updated Overnight — Verify Immediately</h3>
  <div class="meta">From: service@ecom.ulta.com &nbsp;|&nbsp; Received: Fri Aug 28, 2026 ~2:07 AM UTC</div>
  <p>Two automated emails arrived within seconds of each other: one confirming a new address was <strong>added</strong> to your Ulta profile, a second confirming it was <strong>updated</strong>. This pattern is consistent with account takeover attempts where a bad actor updates the shipping address before placing fraudulent orders using your stored payment method.</p>
  <p style="margin-top:8px;"><strong>Why it matters:</strong> You have an active Ulta order placed last night. A shipping address change could redirect your order, and your stored credit card could be used for unauthorized purchases.</p>
  <p style="margin-top:8px;"><strong>Recommended next step:</strong> Log in to Ulta.com directly (do not click any email links), verify your address, check recent orders and payment methods, and change your password. If you did not make the change, contact Ulta Guest Services at 1-866-983-8582 to lock the account.</p>
  <p style="margin-top:6px;"><span class="tag tag-red">⏰ Due: TODAY</span></p>
</div>

<div class="card card-yellow">
  <span class="tag tag-yellow">🟡 FOLLOW-UP — CALENDAR</span>
  <h3>RSVP Needed: HR Networking &amp; Job Search Group — Sep 2 &amp; Sep 3</h3>
  <div class="meta">From: Google Calendar &nbsp;|&nbsp; Events: Sep 2, 12:00–1:30 PM &amp; Sep 3, 12:00–1:00 PM</div>
  <p>You have two upcoming HR Networking Zoom sessions where your RSVP status is still <strong>"Needs Action"</strong>. Both appear highly relevant to your active job search. The Sep 2 session has 170+ attendees — strong networking opportunity.</p>
  <p style="margin-top:8px;"><strong>Recommended next step:</strong> Accept both calendar invites. Prepare 1–2 sentences about your current search focus and target roles before each session.</p>
  <p style="margin-top:6px;"><span class="tag tag-yellow">⏰ RSVP by: Today or Monday</span></p>
</div>

<div class="card card-yellow">
  <span class="tag tag-yellow">🟡 REMINDER — FINANCIAL</span>
  <h3>Transfer Money — All-Day Calendar Reminder</h3>
  <div class="meta">From: Google Calendar &nbsp;|&nbsp; Date: Friday, August 28, 2026</div>
  <p>You have an all-day calendar reminder to transfer money today. No additional context was provided in the event description. Ensure this is completed before end of business today.</p>
  <p style="margin-top:8px;"><strong>Recommended next step:</strong> Complete the transfer. Cross-reference with your Robinhood Vanguard Total Stock Market ETF notification (new investor documents published) — may be related.</p>
  <p style="margin-top:6px;"><span class="tag tag-yellow">⏰ Due: Today, Aug 28</span></p>
</div>

<div class="card card-blue">
  <span class="tag tag-blue">🔵 PREP — MEETING TODAY</span>
  <h3>Virtual Call: VP, P&amp;C with Bryce Lowery (Intalegence) — 10:30 AM ET Today</h3>
  <div class="meta">Attendee: bryce.lowery@intalegence.io &nbsp;|&nbsp; Duration: 10:30–11:15 AM ET (45 min)</div>
  <p>You have a confirmed virtual call with Bryce Lowery at Intalegence this morning. The title references VP, P&amp;C (People &amp; Culture). Prepare your executive narrative, key accomplishments, and target comp range.</p>
  <p style="margin-top:8px;"><strong>Recommended next step:</strong> Confirm meeting link with Bryce if not already done. Review Intalegence's LinkedIn profile. Have your resume and comp expectations ready.</p>
  <p style="margin-top:6px;"><span class="tag tag-blue">⏰ Starts: 10:30 AM TODAY</span></p>
</div>

<!-- ════════════════════════════════════════════════════════
     4. FULL 7-DAY CALENDAR
     ════════════════════════════════════════════════════════ -->
<div class="section-title st-blue">📅 Full 7-Day Calendar</div>

<!-- FRIDAY AUG 28 -->
<div class="card card-blue">
  <h3>📅 Friday, August 28, 2026 — TODAY</h3>
  <div class="tbl-wrap" style="margin-top:10px;">
  <table>
    <thead><tr><th>Time</th><th>Event</th><th>Status</th><th>Location / Link</th><th>Prep Needed</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>All Day</strong></td>
        <td>Transfer Money 💰</td>
        <td><span class="badge badge-yellow">Confirmed</span></td>
        <td>—</td>
        <td>Complete the bank/investment transfer before EOD. Check Robinhood Vanguard notification for context.</td>
      </tr>
      <tr>
        <td><strong>10:30 – 11:15 AM ET</strong></td>
        <td>Virtual Call w/ Melissa — VP, P&amp;C (Bryce Lowery, Intalegence)</td>
        <td><span class="badge badge-green">Accepted ✓</span></td>
        <td>Virtual (link not in calendar — confirm with Bryce)</td>
        <td>⚠️ <strong>Prep required:</strong> Review Intalegence background, executive narrative, target comp, key wins. Starts in ~hours — act now.</td>
      </tr>
    </tbody>
  </table>
  </div>
</div>

<!-- SATURDAY AUG 29 -->
<div class="card card-gray">
  <h3>📅 Saturday, August 29, 2026</h3>
  <p style="margin-top:8px; color:#6b7280;">No calendar events scheduled. Weekend — opportunity for job search prep, networking follow-ups, or rest.</p>
</div>

<!-- SUNDAY AUG 30 -->
<div class="card card-gray">
  <h3>📅 Sunday, August 30, 2026</h3>
  <p style="margin-top:8px; color:#6b7280;">No calendar events scheduled.</p>
</div>

<!-- MONDAY AUG 31 -->
<div class="card card-gray">
  <h3>📅 Monday, August 31, 2026</h3>
  <p style="margin-top:8px; color:#6b7280;">No calendar events scheduled. Labor Day weekend — plan for reduced recruiter activity this week.</p>
</div>

<!-- TUESDAY SEP 1 -->
<div class="card card-gray">
  <h3>📅 Tuesday, September 1, 2026</h3>
  <p style="margin-top:8px; color:#6b7280;">No calendar events scheduled.</p>
</div>

<!-- WEDNESDAY SEP 2 -->
<div class="card card-blue">
  <h3>📅 Wednesday, September 2, 2026</h3>
  <div class="tbl-wrap" style="margin-top:10px;">
  <table>
    <thead><tr><th>Time</th><th>Event</th><th>Status</th><th>Location / Link</th><th>Prep Needed</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>12:00 – 1:30 PM ET</strong></td>
        <td>HR Networking &amp; Job Search Group — Zoom 2</td>
        <td><span class="badge badge-orange">⚠️ Needs Action</span></td>
        <td><a href="https://us06web.zoom.us/j/81954171722" style="color:#2563eb;">Zoom Link</a></td>
        <td>RSVP immediately. Prepare 30-second pitch, target role summary, and questions for group. 170+ attendees — excellent networking reach.</td>
      </tr>
      <tr>
        <td><strong>12:00 – 1:30 PM ET</strong></td>
        <td>Network (Personal Reminder)</td>
        <td><span class="badge badge-green">Confirmed ✓</span></td>
        <td>—</td>
        <td>Overlaps with Zoom group above. Same time block — likely the same session. Confirmed as personal reminder.</td>
      </tr>
    </tbody>
  </table>
  </div>
  <p class="note">⚠️ Note: "Network" personal event and "HR Networking &amp; Job Search Group" overlap at 12:00 PM — they appear to be the same session. No conflict.</p>
</div>

<!-- THURSDAY SEP 3 -->
<div class="card card-blue">
  <h3>📅 Thursday, September 3, 2026</h3>
  <div class="tbl-wrap" style="margin-top:10px;">
  <table>
    <thead><tr><th>Time</th><th>Event</th><th>Status</th><th>Location / Link</th><th>Prep Needed</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>9:00 – 10:30 AM ET</strong></td>
        <td>Executive Roundtable (John Madigan / Zoom)</td>
        <td><span class="badge badge-gray">Declined ✗</span></td>
        <td><a href="https://us02web.zoom.us/j/207786667" style="color:#2563eb;">Zoom Link</a></td>
        <td>You have declined this event. No action needed unless you wish to reconsider — could be networking value as a job seeker.</td>
      </tr>
      <tr>
        <td><strong>12:00 – 1:00 PM ET</strong></td>
        <td>HR Networking &amp; Job Search: Open Office Hours — Zoom 2</td>
        <td><span class="badge badge-orange">⚠️ Needs Action</span></td>
        <td><a href="https://us06web.zoom.us/j/85945371140" style="color:#2563eb;">Zoom Link</a></td>
        <td>RSVP needed. Open Office Hours format — great for 1:1 conversation with organizer or smaller group. Prepare specific questions or job search challenges to discuss.</td>
      </tr>
    </tbody>
  </table>
  </div>
  <p class="note">💡 Consider reconsidering the Executive Roundtable — networking at executive level could surface leads during your job search.</p>
</div>

<!-- ════════════════════════════════════════════════════════
     5. JOB SEARCH & INTERVIEW PIPELINE
     ════════════════════════════════════════════════════════ -->
<div class="section-title st-green">💼 Job Search &amp; Interview Pipeline</div>

<div class="section-wrap">
<h3 style="color:#16a34a; margin-bottom:12px;">🏆 High-Priority Opportunities</h3>
<div class="tbl-wrap">
<table>
  <thead><tr><th>Fit</th><th>Role / Company</th><th>Source</th><th>Salary</th><th>Status</th><th>Action</th></tr></thead>
  <tbody>
    <tr>
      <td><span class="badge badge-green">HIGH</span></td>
      <td>Director, HRBP – Commercial @ Alnylam</td>
      <td>Indeed (via Apple relay)</td>
      <td>$199,800 – $270,300/yr</td>
      <td>Alert received</td>
      <td>Review JD and apply if aligned</td>
    </tr>
    <tr>
      <td><span class="badge badge-green">HIGH</span></td>
      <td>VP – Absence Operations @ ComPsych</td>
      <td>LinkedIn Job Alert (Inbox)</td>
      <td>Not listed</td>
      <td>In Inbox — unread</td>
      <td>Open, review, apply</td>
    </tr>
    <tr>
      <td><span class="badge badge-green">HIGH</span></td>
      <td>Head of People @ Anterior</td>
      <td>LinkedIn Job Alert</td>
      <td>$180K – $230K/yr</td>
      <td>Alert received</td>
      <td>Review JD and apply</td>
    </tr>
    <tr>
      <td><span class="badge badge-yellow">MEDIUM</span></td>
      <td>$250K LinkedIn InMail from Swetha Glory B, MBA</td>
      <td>LinkedIn InMail</td>
      <td>~$250K implied</td>
      <td>Unread</td>
      <td>Open InMail, read full message</td>
    </tr>
    <tr>
      <td><span class="badge badge-yellow">MEDIUM</span></td>
      <td>Senior Manager, Human Resources @ Mortenson (+9 more)</td>
      <td>Glassdoor (in Trash — was valid)</td>
      <td>Not listed</td>
      <td>In Trash — manual</td>
      <td>Restore from Trash, review roles</td>
    </tr>
    <tr>
      <td><span class="badge badge-yellow">MEDIUM</span></td>
      <td>Senior VP Coach @ Fulchester Consultants</td>
      <td>LinkedIn Job Alert</td>
      <td>Not listed</td>
      <td>Read, not in inbox</td>
      <td>Review if coaching-adjacent interests you</td>
    </tr>
    <tr>
      <td><span class="badge badge-gray">LOW</span></td>
      <td>CPO / Lead Talent Culture Change (5 roles)</td>
      <td>JobLeads (in Trash)</td>
      <td>Not listed</td>
      <td>In Trash</td>
      <td>Restore if CPO roles are of interest</td>
    </tr>
  </tbody>
</table>
</div>

<h3 style="color:#16a34a; margin-bottom:10px; margin-top:16px;">🤝 Networking &amp; Connections</h3>
<div class="tbl-wrap">
<table>
  <thead><tr><th>Contact</th><th>Platform</th><th>Status</th><th>Action</th></tr></thead>
  <tbody>
    <tr>
      <td>Kevin Caldwell</td>
      <td>LinkedIn</td>
      <td><span class="badge badge-green">Connected ✓</span></td>
      <td>Explore Kevin's network — look for mutual connections at target companies. Send a warm follow-up message.</td>
    </tr>
    <tr>
      <td>Bryce Lowery (Intalegence)</td>
      <td>Google Calendar / Virtual Call</td>
      <td><span class="badge badge-blue">Call Today 10:30 AM</span></td>
      <td>Prep executive story, comp expectations, and questions about the VP P&amp;C role.</td>
    </tr>
    <tr>
      <td>HR Networking Group (170+ members)</td>
      <td>Zoom (Sep 2 &amp; Sep 3)</td>
      <td><span class="badge badge-orange">RSVP Needed</span></td>
      <td>RSVP now. Prepare pitch and target role clarity.</td>
    </tr>
  </tbody>
</table>
</div>

<div class="card card-green" style="margin-top:8px;">
  <span class="tag tag-green">💡 KKARENISM Substack Note</span>
  <p>A Substack post arrived (in Trash): "Laid off → Landed new offer exceeding salary expectations" — career content relevant to your search. Consider restoring and reading for job search strategy tips.</p>
</div>
</div>

<!-- ════════════════════════════════════════════════════════
     6. FULL EMAIL REVIEW BY CATEGORY
     ════════════════════════════════════════════════════════ -->
<div class="section-title st-dark">📬 Full Email Review by Category</div>

<!-- 6A: SECURITY / RISK -->
<div class="card card-red">
  <span class="tag tag-red">🔴 SECURITY / RISK</span> <span class="tag tag-gray">6 emails</span>
  <h3>Security &amp; Risk Alerts</h3>
  <ul class="inline-list" style="margin-top:8px;">
    <li><strong>Ulta — Address Added</strong> (service@ecom.ulta.com, Aug 28 2:07 AM UTC) — <span class="badge badge-red">ACTION REQUIRED</span> Profile address added — verify immediately.</li>
    <li><strong>Ulta — Address Updated</strong> (service@ecom.ulta.com, Aug 28 2:07 AM UTC) — <span class="badge badge-red">ACTION REQUIRED</span> Address updated seconds later — possible account compromise.</li>
    <li><strong>Google Account</strong> (noreply-accounts@google.com) — You shared Google Account data with SoundCloud. Verify this was intentional. Review connected apps at myaccount.google.com.</li>
    <li><strong>Fake SiriusXM</strong> (garbage domain) — <span class="badge badge-red">AUTO-TRASHED — PHISHING</span> Spoofed SiriusXM sender, fake subscription expiration, credential/payment harvesting. Already removed. No action needed.</li>
    <li><strong>"Raw Footage" adult spam</strong> (garbage domains ×2) — Clearly malicious senders with explicit content and phishing tactics. Should be in Trash/blocked.</li>
    <li><strong>"Hard as Steel" adult spam</strong> (garbage domain) — Same pattern. Block sender.</li>
  </ul>
  <p class="note" style="margin-top:8px;">⚠️ Priority: Verify Ulta account and Google/SoundCloud connection TODAY.</p>
</div>

<!-- 6B: JOB SEARCH -->
<div class="card card-green">
  <span class="tag tag-green">🟢 JOB SEARCH</span> <span class="tag tag-gray">7 emails</span>
  <h3>Job Alerts &amp; Applications</h3>
  <ul class="inline-list" style="margin-top:8px;">
    <li><strong>LinkedIn — VP, Absence Operations @ ComPsych</strong> (Inbox, unread) — High priority. Review and apply.</li>
    <li><strong>LinkedIn — Head of People @ Anterior</strong> ($180K–$230K) — High priority. Review and apply.</li>
    <li><strong>LinkedIn — Senior VP Coach @ Fulchester Consultants</strong> (Remote) — Medium. Review if aligned.</li>
    <li><strong>Indeed — Director HRBP Commercial @ Alnylam</strong> ($199K–$270K) — High priority. Apply if aligned.</li>
    <li><strong>Glassdoor — Senior Manager HR @ Mortenson + 9 more</strong> (in Trash — restore) — Medium. Worth reviewing the 10 listings.</li>
    <li><strong>JobLeads — CPO / Lead Talent Culture Change (5 roles)</strong> (in Trash) — Low-Medium. Review if CPO roles interest you.</li>
    <li><strong>LinkedIn InMail — $250K opportunity from Swetha Glory B, MBA</strong> — Medium. Open and read full message; verify legitimacy.</li>
  </ul>
  <p class="note">Recommended action: Prioritize Alnylam Director, ComPsych VP, and Anterior Head of People applications this weekend.</p>
</div>

<!-- 6C: RECRUITERS / NETWORKING -->
<div class="card card-green">
  <span class="tag tag-green">🟢 RECRUITERS / NETWORKING</span> <span class="tag tag-gray">2 emails</span>
  <h3>Recruiters &amp; Professional Connections</h3>
  <ul class="inline-list" style="margin-top:8px;">
    <li><strong>Kevin Caldwell via LinkedIn</strong> (Inbox, unread) — Accepted your invitation. Explore his network and send a warm follow-up message today.</li>
    <li><strong>Bryce Lowery (Intalegence)</strong> — Virtual call today 10:30 AM ET (VP, P&amp;C). Confirmed on calendar. Prep required now.</li>
  </ul>
</div>

<!-- 6D: CALENDAR / EVENTS -->
<div class="card card-blue">
  <span class="tag tag-blue">🔵 CALENDAR / EVENTS</span> <span class="tag tag-gray">1 email</span>
  <h3>Event Notifications</h3>
  <ul class="inline-list" style="margin-top:8px;">
    <li><strong>AllEvents — Popular events this weekend in York</strong> (in Trash) — Weekend event digest. Low priority. Already trashed.</li>
  </ul>
</div>

<!-- 6E: FINANCIAL / BILLING -->
<div class="card card-yellow">
  <span class="tag tag-yellow">🟡 FINANCIAL / BILLING</span> <span class="tag tag-gray">3 emails</span>
  <h3>Financial &amp; Billing Emails</h3>
  <ul class="inline-list" style="margin-top:8px;">
    <li><strong>Robinhood — Vanguard Total Stock Market ETF</strong> (unread, not in inbox) — New investor documents published. Review when convenient; may be related to your Transfer Money reminder.</li>
    <li><strong>My Best Buy® Visa® (Citi)</strong> — <span class="badge badge-green">RESCUED FROM TRASH</span> Labor Day Appliances Sale — 18–24 mo. financing. Review if you have appliance needs.</li>
    <li><strong>Fake SiriusXM subscription</strong> — <span class="badge badge-red">PHISHING — AUTO-TRASHED</span> Already removed. Do not engage.</li>
  </ul>
</div>

<!-- 6F: PROFESSIONAL DEVELOPMENT -->
<div class="card card-purple">
  <span class="tag tag-purple">🟣 PROFESSIONAL DEVELOPMENT</span> <span class="tag tag-gray">2 emails</span>
  <h3>Professional Development</h3>
  <ul class="inline-list" style="margin-top:8px;">
    <li><strong>KKARENISM Substack — "Laid off → Landed new offer exceeding salary expectations"</strong> (in Trash) — Career coaching content. Consider restoring; directly relevant to your job search situation.</li>
    <li><strong>LinkedIn InMail — Swetha Glory B, MBA — "$250K Reason to Check LinkedIn"</strong> — Read the full InMail. Could be a recruiter pitch or consulting offer. Verify legitimacy before engaging.</li>
  </ul>
</div>

<!-- 6G: PERSONAL -->
<div class="card card-teal">
  <span class="tag tag-teal">🔵 PERSONAL</span> <span class="tag tag-gray">5 emails</span>
  <h3>Personal &amp; Social</h3>
  <ul class="inline-list" style="margin-top:8px;">
    <li><strong>OkCupid — "Someone likes you"</strong> (×2, read/unread) — Dating app notifications. Review at your leisure.</li>
    <li><strong>Match — "Persiderna likes you"</strong> (read) — Dating app notification.</li>
    <li><strong>Match — "Melissa, you've still got an unread message"</strong> (unread) — Unread message on Match. Check when ready.</li>
    <li><strong>Match — "Profile view from Richard, 68, Manhattan"</strong> (read) — Profile view notification.</li>
  </ul>
</div>

<!-- 6H: MEDICAL / HEALTH -->
<div class="card card-gray">
  <span class="tag tag-gray">⚕️ MEDICAL / HEALTH</span> <span class="tag tag-gray">2 emails</span>
  <h3>Health &amp; Medical Emails (Spam)</h3>
  <ul class="inline-list" style="margin-top:8px;">
    <li><strong>GLP-1-by-DirectMeds</strong> (×2, garbage domains) — Unsolicited weight loss medication ads (Ozempic/Mounjaro alternatives). Spam. Block and delete.</li>
  </ul>
  <p class="note">These are not from legitimate medical providers. Do not click any links.</p>
</div>

<!-- 6I: NEWSLETTERS / SUBSCRIPTIONS -->
<div class="card card-purple">
  <span class="tag tag-purple">🟣 NEWSLETTERS / SUBSCRIPTIONS</span> <span class="tag tag-gray">4 emails</span>
  <h3>Newsletters &amp; Subscriptions</h3>
  <ul class="inline-list" style="margin-top:8px;">
    <li><strong>1% Better Newsletter</strong> — "Sandlot Reunion, Nepal Flood, and The Trouble with Starting" (in Trash). Motivational/productivity newsletter. Consider keeping if valuable.</li>
    <li><strong>Dylan's Diary — "What Everyone Missed in Nvidia's Blowout Earnings"</strong> (in Trash). Finance/markets newsletter. Keep if you follow markets; delete if not.</li>
    <li><strong>The Daily Skimm — "But how does the Trix rabbit feel?"</strong> (in Trash). Daily news digest. Keep or unsubscribe based on usage.</li>
    <li><strong>Netflix — "Mel, we just added a documentary series you might like"</strong> (in Trash). Content recommendation about Mica Miller documentary. Personal interest.</li>
  </ul>
</div>

<!-- 6J: PROMOTIONAL / RETAIL -->
<div class="card card-gray">
  <span class="tag tag-gray">🛍️ PROMOTIONAL / RETAIL</span> <span class="tag tag-gray">8 emails</span>
  <h3>Retail &amp; Promotional Emails</h3>
  <ul class="inline-list" style="margin-top:8px;">
    <li><strong>Ulta Beauty Orders</strong> — Order confirmation (in Inbox). Track your order. ✓ Legitimate.</li>
    <li><strong>Delta Air Lines</strong> — <span class="badge badge-green">RESCUED FROM TRASH</span> 50K bonus miles + 2 Comfort certs. Review if traveling.</li>
    <li><strong>Kohl's</strong> — 20% off + 50% Sephora beauty (in Trash). Shopping promo.</li>
    <li><strong>Old Navy</strong> (×2) — 50% PJ sale &amp; abandoned cart reminder (both in Trash).</li>
    <li><strong>VIVAIA</strong> — New work shoes collection (in Trash).</li>
    <li><strong>SHEIN</strong> — All under $14.99 wardrobe styles. Not in Trash — delete if not interested.</li>
    <li><strong>Macy's</strong> — Product review request + chance to win $500 gift card. Not in Trash — low priority.</li>
    <li><strong>Facebook Friend Suggestions</strong> — Cayla Friesz from Sonoma (read). Social suggestion. Safe to ignore.</li>
  </ul>
</div>

<!-- 6K: SAFE TO DELETE / IGNORE -->
<div class="card card-gray">
  <span class="tag tag-gray">🗑️ SAFE TO DELETE / IGNORE</span> <span class="tag tag-gray">10 emails</span>
  <h3>Spam, Adult Content, Gambling &amp; Scam Emails</h3>
  <ul class="inline-list" style="margin-top:8px;">
    <li><strong>"Unstoppable Sex Machines"</strong> (×3, garbage domains) — Adult spam. Already in Trash or should be deleted. Block all.</li>
    <li><strong>"Sex Trick" / Naughty porn star</strong> (garbage domain) — Adult spam. Delete and block.</li>
    <li><strong>"Raw Footage" adult spam</strong> (×2, garbage domains) — Adult/phishing content. Delete and block.</li>
    <li><strong>BettyWins Casino / "200 Free Spins"</strong> (×3, various senders) — Gambling spam. Two in Trash, one not in Trash. Delete all and block.</li>
    <li><strong>Hidden Treasure / "Jackpota"</strong> (garbage domain, in Trash) — Gambling scam. Already in Trash.</li>
    <li><strong>OnlineCasino / "30 Free Spins"</strong> (garbage domain) — Gambling spam. Delete.</li>
    <li><strong>"You received a payment of $13,999.99" (Slots of Vegas)</strong> (in Trash) — Classic scam. Already in Trash.</li>
    <li><strong>Facebook — "Here's what's new from Jacqueline and others"</strong> (in Trash) — Social notification. Low value, already trashed.</li>
  </ul>
</div>

<!-- ════════════════════════════════════════════════════════
     7. TRASH REVIEW
     ════════════════════════════════════════════════════════ -->
<div class="section-title st-red">🗑️ Trash Review</div>

<div class="section-wrap">

<h3 style="color:#16a34a; margin-bottom:10px;">✅ Restore Immediately</h3>
<div class="tbl-wrap">
<table>
  <thead><tr><th>Sender</th><th>Subject</th><th>Reason to Restore</th></tr></thead>
  <tbody>
    <tr><td>Glassdoor</td><td>Senior Manager of HR at Mortenson + 9 more jobs</td><td>Active job search — 10 HR leadership roles worth reviewing. Likely trashed by filter error.</td></tr>
    <tr><td>JobLeads</td><td>5 new jobs: Chief People Officer / Lead Talent Culture Change</td><td>CPO-level opportunities matching your saved search. Worth reviewing.</td></tr>
    <tr><td>KKARENISM Substack</td><td>Laid off → Landed new offer exceeding salary expectations</td><td>Career coaching content directly relevant to your job search transition. Consider reading.</td></tr>
  </tbody>
</table>
</div>

<h3 style="color:#d97706; margin-bottom:10px; margin-top:16px;">🔍 Review Before Deleting</h3>
<div class="tbl-wrap">
<table>
  <thead><tr><th>Sender</th><th>Subject</th><th>Notes</th></tr></thead>
  <tbody>
    <tr><td>1% Better Newsletter</td><td>Sandlot Reunion, Nepal Flood, and The Trouble with Starting</td><td>Motivational newsletter you subscribed to — keep if you read it, unsubscribe if not.</td></tr>
    <tr><td>Dylan's Diary</td><td>What Everyone Missed in Nvidia's Blowout Earnings</td><td>Finance newsletter — relevant if you track markets. Keep or unsubscribe.</td></tr>
    <tr><td>The Daily Skimm</td><td>But how does the Trix rabbit feel?</td><td>News digest. Keep if you read it, unsubscribe if it's consistently trashed.</td></tr>
    <tr><td>Netflix</td><td>Mel, we just added a documentary series you might like</td><td>Personal interest — Mica Miller documentary. Delete or save for weekend viewing.</td></tr>
    <tr><td>AllEvents</td><td>Melissa, popular events this weekend in York</td><td>Local weekend events. Quick glance before deleting.</td></tr>
  </tbody>
</table>
</div>

<h3 style="color:#dc2626; margin-bottom:10px; margin-top:16px;">🗑️ Safe to Delete (Confirmed Junk/Spam/Trash)</h3>
<div class="tbl-wrap">
<table>
  <thead><tr><th>Sender</th><th>Subject</th><th>Reason</th></tr></thead>
  <tbody>
    <tr><td>SiriusXM (FAKE) — <strong>AUTO-TRASHED PHISHING</strong></td><td>Your Account Will Be Removed Today</td><td>Spoofed sender on garbage domain. Payment harvesting phishing. Already auto-trashed. No action needed.</td></tr>
    <tr><td>Unstoppable Sex Machines (×2)</td><td>What is blocking penile growth in men today?</td><td>Adult spam from garbage domains. Already in Trash. Block senders.</td></tr>
    <tr><td>BettyWins Casino "Congratulations🎉"</td><td>melissaw212, Get 200 free spins — code LOVERFS</td><td>Gambling spam. Already in Trash. Safe to delete.</td></tr>
    <tr><td>Hidden___Treasure</td><td>See how others are winning thousands online!</td><td>Gambling scam (Jackpota). Already in Trash. Delete.</td></tr>
    <tr><td>"Congratulations?" — Slots of Vegas</td><td>You received a payment of $13,999.99</td><td>Classic advance-fee / casino scam. Already in Trash. Delete.</td></tr>
    <tr><td>Kohl's Friends &amp; Family</td><td>20% off 🤗 New styles for less</td><td>Retail promo. In Trash. Delete if not shopping.</td></tr>
    <tr><td>Old Navy (×2)</td><td>PJ Sale / Abandoned Cart Reminder</td><td>Retail promos. In Trash. Delete.</td></tr>
    <tr><td>VIVAIA</td><td>Introducing RE | Your Work Shoes Just Got Promoted</td><td>Retail promo. In Trash. Delete.</td></tr>
    <tr><td>Facebook</td><td>Here's what's new from Jacqueline and others</td><td>Social notification. In Trash. Delete.</td></tr>
  </tbody>
</table>
</div>
</div>

<!-- ════════════════════════════════════════════════════════
     8. PROMOTIONAL / RETAIL SUMMARY
     ════════════════════════════════════════════════════════ -->
<div class="section-title st-gray">🛍️ Promotional / Retail Summary</div>

<div class="tbl-wrap">
<table>
  <thead><tr><th>Sender / Brand</th><th>Count</th><th>Subject / Theme</th><th>Recommendation</th></tr></thead>
  <tbody>
    <tr><td><strong>Ulta Beauty</strong></td><td>1</td><td>Order confirmation for recent purchase</td><td><span class="badge badge-green">Keep — Track Order</span></td></tr>
    <tr><td><strong>Delta Air Lines</strong></td><td>1</td><td>50K bonus miles + 2 Comfort Flight Certificates (1st time ever offer) — <em>Rescued from Trash</em></td><td><span class="badge badge-yellow">Review — Loyalty Offer</span></td></tr>
    <tr><td><strong>My Best Buy® Visa® (Citi)</strong></td><td>1</td><td>Labor Day Appliances Sale, 18–24 mo. financing — <em>Rescued from Trash</em></td><td><span class="badge badge-yellow">Review — Financing Offer</span></td></tr>
    <tr><td><strong>Macy's</strong></td><td>1</td><td>Write a product review — chance to win $500 gift card</td><td><span class="badge badge-gray">Low Priority — Ignore or Review</span></td></tr>
    <tr><td><strong>SHEIN</strong></td><td>1</td><td>All under $14.99 wardrobe updates</td><td><span class="badge badge-gray">Delete if not shopping</span></td></tr>
    <tr><td><strong>Old Navy</strong></td><td>2</td><td>50% PJ sale; Abandoned cart reminder (both in Trash)</td><td><span class="badge badge-red">Delete — Already Trashed</span></td></tr>
    <tr><td><strong>Kohl's</strong></td><td>1</td><td>20% off + 50% Sephora beauty (in Trash)</td><td><span class="badge badge-red">Delete — Already Trashed</span></td></tr>
    <tr><td><strong>VIVAIA</strong></td><td>1</td><td>New work shoe styles (in Trash)</td><td><span class="badge badge-red">Delete — Already Trashed</span></td></tr>
    <tr><td><strong>Facebook Friend Suggestions</strong></td><td>1</td><td>You may know Cayla Friesz from Sonoma</td><td><span class="badge badge-gray">Ignore — Low value</span></td></tr>
  </tbody>
</table>
</div>

<!-- ════════════════════════════════════════════════════════
     9. NEWSLETTERS & SUBSCRIPTIONS
     ════════════════════════════════════════════════════════ -->
<div class="section-title st-purple">📰 Newsletters &amp; Subscriptions</div>

<div class="tbl-wrap">
<table>
  <thead><tr><th>Sender</th><th>Topic</th><th>Location</th><th>Recommendation</th></tr></thead>
  <tbody>
    <tr><td><strong>1% Better</strong></td><td>Motivational / personal growth / news (Sandlot, Nepal, starting habits)</td><td>In Trash</td><td><span class="badge badge-yellow">Review — Keep if you read it; Unsubscribe if not</span></td></tr>
    <tr><td><strong>Dylan's Diary (Behind the Markets)</strong></td><td>Finance / markets — Nvidia earnings analysis</td><td>In Trash</td><td><span class="badge badge-yellow">Review — Keep if you follow markets; Unsubscribe if not</span></td></tr>
    <tr><td><strong>The Daily Skimm</strong></td><td>Daily news digest / pop culture</td><td>In Trash</td><td><span class="badge badge-yellow">Review — Unsubscribe if consistently unread</span></td></tr>
    <tr><td><strong>KKARENISM (Substack)</strong></td><td>Career coaching — job search / layoff recovery</td><td>In Trash</td><td><span class="badge badge-green">Restore &amp; Read — Relevant to current situation</span></td></tr>
    <tr><td><strong>Netflix</strong></td><td>Content recommendation — Mica Miller documentary</td><td>In Trash</td><td><span class="badge badge-gray">Delete or save for weekend</span></td></tr>
  </tbody>
</table>
</div>

<!-- ════════════════════════════════════════════════════════
     10. EMAIL ACCOUNTING
     ════════════════════════════════════════════════════════ -->
<div class="section-title st-dark">📊 Email Accounting</div>

<div class="tbl-wrap">
<table>
  <thead><tr><th>Category</th><th>Count</th><th>Summary</th><th>Recommendation</th></tr></thead>
  <tbody>
    <tr><td>🔴 Security / Risk</td><td>6</td><td>Ulta address changes (×2), Google/SoundCloud data share, fake SiriusXM phishing (auto-trashed), "Raw Footage" adult spam (×2)</td><td>Act immediately on Ulta &amp; Google. Auto-trash already handled phishing.</td></tr>
    <tr><td>🟢 Job Search Alerts</td><td>7</td><td>LinkedIn VP ComPsych, LinkedIn Head of People Anterior, LinkedIn SVP Coach Fulchester, LinkedIn InMail $250K, Indeed Director HRBP Alnylam, Glassdoor 10 roles (trash), JobLeads 5 CPO roles (trash)</td><td>Apply to top 3 this weekend. Restore Glassdoor &amp; JobLeads from Trash.</td></tr>
    <tr><td>🟢 Recruiters / Networking</td><td>2</td><td>Kevin Caldwell LinkedIn connection accepted; Bryce Lowery virtual call today (calendar)</td><td>Follow up with Kevin; prep for 10:30 AM call.</td></tr>
    <tr><td>🔵 Calendar / Events</td><td>1</td><td>AllEvents weekend York events (in Trash)</td><td>Delete — already trashed.</td></tr>
    <tr><td>🟡 Financial / Billing</td><td>3</td><td>Robinhood Vanguard ETF documents, Citi Best Buy Visa promo (rescued), fake SiriusXM (auto-trashed — counted under Security)</td><td>Review Robinhood documents. Citi promo is legitimate.</td></tr>
    <tr><td>🟣 Professional Development</td><td>2</td><td>KKARENISM Substack career post (trash), LinkedIn InMail $250K (also counted in Job Search)</td><td>Restore KKARENISM. Read InMail carefully.</td></tr>
    <tr><td>🔵 Personal / Social / Dating</td><td>5</td><td>OkCupid ×2, Match ×3 (profile view, message reminder, Persiderna like)</td><td>Review at leisure. Low priority.</td></tr>
    <tr><td>⚕️ Medical / Health (Spam)</td><td>2</td><td>GLP-1 DirectMeds ×2 (garbage domains)</td><td>Delete and block. Not legitimate providers.</td></tr>
    <tr><td>🛍️ Promotional / Retail</td><td>9</td><td>Ulta order confirm, Delta rescued, Citi rescued, Macy's review, SHEIN, Old Navy ×2, Kohl's, VIVAIA, Facebook friend suggestion</td><td>Keep Ulta/Delta/Citi. Delete rest if not shopping.</td></tr>
    <tr><td>📰 Newsletters / Subscriptions</td><td>5</td><td>1% Better, Dylan's Diary, Daily Skimm, KKARENISM Substack, Netflix
