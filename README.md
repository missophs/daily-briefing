<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing – Melissa | Monday, August 24, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }

  /* ── HEADER ── */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; padding: 36px 40px 28px; border-bottom: 4px solid #e94560; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: .5px; }
  .header .subtitle { font-size: 15px; color: #a8b2d8; margin-top: 6px; }
  .header .meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,.08); border-radius: 8px; padding: 10px 18px; text-align: center; }
  .header .meta-item .num { font-size: 22px; font-weight: 700; color: #e2e8f5; }
  .header .meta-item .lbl { font-size: 11px; color: #8892b0; text-transform: uppercase; letter-spacing: .8px; }

  /* ── LAYOUT ── */
  .container { max-width: 1200px; margin: 0 auto; padding: 28px 20px 60px; }

  /* ── SECTION HEADERS ── */
  .section-title { font-size: 18px; font-weight: 700; color: #1a1a2e; margin: 36px 0 14px; padding-bottom: 8px; border-bottom: 3px solid #e94560; letter-spacing: .3px; }
  .section-subtitle { font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: .7px; margin-bottom: 10px; }

  /* ── CARDS ── */
  .card { background: #fff; border-radius: 10px; padding: 18px 22px; margin-bottom: 14px; box-shadow: 0 2px 8px rgba(0,0,0,.07); border-left: 5px solid #ccc; }
  .card.red    { border-left-color: #e53e3e; }
  .card.yellow { border-left-color: #d69e2e; }
  .card.blue   { border-left-color: #3182ce; }
  .card.green  { border-left-color: #38a169; }
  .card.purple { border-left-color: #805ad5; }
  .card.gray   { border-left-color: #a0aec0; }
  .card.orange { border-left-color: #dd6b20; }

  .card h3 { font-size: 15px; font-weight: 700; margin-bottom: 6px; }
  .card .meta-row { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 8px; }
  .card .meta-row span { font-size: 12px; color: #555; }
  .card .meta-row strong { color: #1a1a2e; }
  .card p { font-size: 13px; color: #444; margin-bottom: 6px; }
  .card .action-tag { display: inline-block; background: #e94560; color: #fff; font-size: 11px; font-weight: 700; padding: 3px 10px; border-radius: 12px; margin-top: 6px; letter-spacing: .4px; }
  .card .due-tag { display: inline-block; background: #d69e2e; color: #fff; font-size: 11px; font-weight: 600; padding: 3px 10px; border-radius: 12px; margin-left: 6px; }

  /* ── EXEC SUMMARY ── */
  .exec-summary { background: #fff; border-radius: 10px; padding: 22px 26px; box-shadow: 0 2px 8px rgba(0,0,0,.07); border-top: 4px solid #e94560; margin-bottom: 8px; }
  .exec-summary ul { list-style: none; padding: 0; }
  .exec-summary ul li { padding: 10px 0; border-bottom: 1px solid #f0f0f0; font-size: 14px; color: #2d3748; display: flex; gap: 10px; align-items: flex-start; }
  .exec-summary ul li:last-child { border-bottom: none; }
  .exec-summary .pill { display: inline-block; font-size: 11px; font-weight: 700; padding: 3px 10px; border-radius: 12px; white-space: nowrap; flex-shrink: 0; margin-top: 2px; }
  .pill-red    { background: #fed7d7; color: #c53030; }
  .pill-yellow { background: #fefcbf; color: #744210; }
  .pill-blue   { background: #bee3f8; color: #2b6cb0; }
  .pill-green  { background: #c6f6d5; color: #276749; }
  .pill-purple { background: #e9d8fd; color: #553c9a; }
  .pill-gray   { background: #edf2f7; color: #4a5568; }

  /* ── TRIAGE TABLE ── */
  .triage-table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,.07); }
  .triage-table thead { background: #1a1a2e; color: #fff; }
  .triage-table thead th { padding: 12px 14px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: .7px; }
  .triage-table tbody tr { border-bottom: 1px solid #f0f2f5; }
  .triage-table tbody tr:last-child { border-bottom: none; }
  .triage-table tbody tr:hover { background: #f7fafc; }
  .triage-table tbody td { padding: 10px 14px; font-size: 13px; vertical-align: top; }
  .triage-table .status-badge { display: inline-block; font-size: 11px; font-weight: 700; padding: 3px 9px; border-radius: 12px; white-space: nowrap; }
  .badge-inbox    { background: #bee3f8; color: #2b6cb0; }
  .badge-rescued  { background: #c6f6d5; color: #276749; }
  .badge-autotrash{ background: #fed7d7; color: #c53030; }
  .badge-trash    { background: #edf2f7; color: #4a5568; }

  /* ── CALENDAR ── */
  .cal-day { background: #fff; border-radius: 10px; padding: 16px 20px; margin-bottom: 14px; box-shadow: 0 2px 8px rgba(0,0,0,.07); }
  .cal-day-header { font-size: 15px; font-weight: 700; color: #0f3460; margin-bottom: 12px; padding-bottom: 8px; border-bottom: 2px solid #e2e8f5; display: flex; align-items: center; gap: 10px; }
  .cal-day-header .today-tag { background: #e94560; color: #fff; font-size: 11px; padding: 2px 8px; border-radius: 10px; }
  .cal-event { display: grid; grid-template-columns: 120px 1fr; gap: 12px; padding: 10px 0; border-bottom: 1px solid #f0f2f5; }
  .cal-event:last-child { border-bottom: none; }
  .cal-time { font-size: 12px; font-weight: 700; color: #3182ce; }
  .cal-allday { font-size: 12px; font-weight: 700; color: #805ad5; }
  .cal-title { font-weight: 700; font-size: 14px; color: #1a1a2e; }
  .cal-details { font-size: 12px; color: #555; margin-top: 3px; }
  .cal-rsvp { display: inline-block; font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 10px; margin-top: 4px; }
  .rsvp-confirmed { background: #c6f6d5; color: #276749; }
  .rsvp-declined  { background: #fed7d7; color: #c53030; }
  .rsvp-pending   { background: #fefcbf; color: #744210; }
  .cal-conflict   { background: #fff5f5; border: 1px solid #fc8181; border-radius: 6px; padding: 6px 10px; font-size: 12px; color: #c53030; margin-top: 6px; }
  .cal-prep       { background: #ebf8ff; border: 1px solid #90cdf4; border-radius: 6px; padding: 6px 10px; font-size: 12px; color: #2b6cb0; margin-top: 6px; }

  /* ── TABLES ── */
  .data-table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,.07); }
  .data-table thead { background: #2d3748; color: #fff; }
  .data-table thead th { padding: 11px 14px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: .7px; }
  .data-table tbody tr { border-bottom: 1px solid #f0f2f5; }
  .data-table tbody tr:last-child { border-bottom: none; }
  .data-table tbody tr:hover { background: #f7fafc; }
  .data-table tbody td { padding: 10px 14px; font-size: 13px; vertical-align: top; }
  .data-table tfoot td { padding: 11px 14px; font-weight: 700; background: #edf2f7; font-size: 13px; }

  .rank-high   { color: #276749; font-weight: 700; }
  .rank-med    { color: #744210; font-weight: 700; }
  .rank-low    { color: #4a5568; font-weight: 600; }
  .pri-high    { background: #fed7d7; color: #c53030; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: 700; }
  .pri-med     { background: #fefcbf; color: #744210; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: 700; }
  .pri-low     { background: #edf2f7; color: #4a5568; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: 700; }

  /* ── CATEGORY REVIEW ── */
  .cat-card { background: #fff; border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,.07); }
  .cat-card .cat-header { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }
  .cat-card .cat-icon { font-size: 18px; }
  .cat-card .cat-title { font-size: 15px; font-weight: 700; color: #1a1a2e; }
  .cat-card .cat-count { background: #e2e8f5; color: #2d3748; font-size: 12px; font-weight: 700; padding: 2px 9px; border-radius: 10px; }
  .cat-card .cat-body { font-size: 13px; color: #444; }
  .cat-card .cat-body p { margin-bottom: 5px; }
  .cat-card .rec-tag { display: inline-block; font-size: 11px; font-weight: 700; padding: 3px 10px; border-radius: 12px; margin-top: 8px; }
  .rec-act   { background: #e94560; color: #fff; }
  .rec-rev   { background: #d69e2e; color: #fff; }
  .rec-del   { background: #718096; color: #fff; }
  .rec-keep  { background: #38a169; color: #fff; }
  .rec-unsub { background: #9f7aea; color: #fff; }

  /* ── DASHBOARD ── */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }
  .dash-tile { background: #fff; border-radius: 10px; padding: 18px 20px; box-shadow: 0 2px 8px rgba(0,0,0,.07); }
  .dash-tile .tile-label { font-size: 11px; text-transform: uppercase; letter-spacing: .7px; color: #718096; margin-bottom: 6px; }
  .dash-tile .tile-value { font-size: 26px; font-weight: 800; color: #1a1a2e; }
  .dash-tile .tile-sub { font-size: 12px; color: #718096; margin-top: 4px; }
  .dash-tile.t-red    { border-top: 4px solid #e53e3e; }
  .dash-tile.t-green  { border-top: 4px solid #38a169; }
  .dash-tile.t-blue   { border-top: 4px solid #3182ce; }
  .dash-tile.t-yellow { border-top: 4px solid #d69e2e; }
  .dash-tile.t-purple { border-top: 4px solid #805ad5; }
  .dash-tile.t-gray   { border-top: 4px solid #a0aec0; }

  /* ── TOP 3 ── */
  .top3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }
  .top3-card { background: linear-gradient(135deg, #1a1a2e, #0f3460); color: #fff; border-radius: 10px; padding: 22px 24px; box-shadow: 0 4px 14px rgba(0,0,0,.2); }
  .top3-card .num { font-size: 40px; font-weight: 900; color: #e94560; line-height: 1; margin-bottom: 10px; }
  .top3-card h3 { font-size: 15px; font-weight: 700; margin-bottom: 8px; }
  .top3-card p { font-size: 13px; color: #a8b2d8; }

  /* ── BIRTHDAY BANNER ── */
  .birthday-banner { background: linear-gradient(90deg, #f093fb, #f5576c); color: #fff; border-radius: 10px; padding: 12px 20px; margin-bottom: 14px; font-weight: 700; font-size: 14px; display: flex; align-items: center; gap: 10px; }

  /* ── MISC ── */
  .note-box { background: #fffbeb; border: 1px solid #f6e05e; border-radius: 8px; padding: 12px 16px; font-size: 13px; color: #744210; margin-bottom: 14px; }
  .spam-box  { background: #fff5f5; border: 1px solid #fc8181; border-radius: 8px; padding: 12px 16px; font-size: 13px; color: #c53030; margin-bottom: 14px; }
  a { color: #3182ce; text-decoration: none; }
  a:hover { text-decoration: underline; }
  .divider { height: 1px; background: #e2e8f5; margin: 28px 0; }
  ul.bullet-list { padding-left: 18px; }
  ul.bullet-list li { margin-bottom: 4px; font-size: 13px; color: #444; }
  .email-list-row { display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid #f0f2f5; font-size: 13px; }
  .email-list-row:last-child { border-bottom: none; }
  .trash-group-title { font-size: 14px; font-weight: 700; color: #1a1a2e; margin: 12px 0 8px; padding-left: 8px; border-left: 4px solid #e94560; }
  .trash-group-title.yellow { border-left-color: #d69e2e; }
  .trash-group-title.green  { border-left-color: #38a169; }
  .inline-tag { display: inline-block; font-size: 10px; font-weight: 700; padding: 1px 6px; border-radius: 8px; vertical-align: middle; margin-left: 4px; }
  .tag-auto  { background: #fed7d7; color: #c53030; }
  .tag-spam  { background: #fefcbf; color: #744210; }
  .tag-promo { background: #e9d8fd; color: #553c9a; }
  .tag-news  { background: #bee3f8; color: #2b6cb0; }
</style>
</head>
<body>

<!-- ═══════════════════════════════════════════════════
     HEADER
═══════════════════════════════════════════════════ -->
<div class="header">
  <h1>🌅 Good Morning, Melissa</h1>
  <div class="subtitle">Executive Briefing — prepared by your Chief of Staff</div>
  <div class="meta">
    <div class="meta-item"><div class="num">Monday</div><div class="lbl">August 24, 2026</div></div>
    <div class="meta-item"><div class="num">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="meta-item"><div class="num">12</div><div class="lbl">Calendar Events</div></div>
    <div class="meta-item"><div class="num">4</div><div class="lbl">Action Required</div></div>
    <div class="meta-item"><div class="num">6</div><div class="lbl">Job Leads</div></div>
  </div>
</div>

<div class="container">

<!-- ═══════════════════════════════════════════════════
     SECTION 0 — EMAIL TRIAGE QUICK LIST
═══════════════════════════════════════════════════ -->
<div class="section-title">📋 Email Triage Quick List</div>
<p style="font-size:13px;color:#555;margin-bottom:12px;">One-glance inbox overview. Rescued and Inbox emails shown individually. Trash collapsed to summary rows.</p>

<table class="triage-table">
  <thead>
    <tr>
      <th style="width:130px;">Status</th>
      <th style="width:200px;">From</th>
      <th>Subject</th>
      <th>Summary</th>
    </tr>
  </thead>
  <tbody>
    <!-- ── INBOX rows ── -->
    <tr>
      <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
      <td>Match</td>
      <td>Profile view from Paul</td>
      <td>Paul, 64, Palmerton PA viewed your Match profile. Low urgency — personal.</td>
    </tr>
    <tr>
      <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
      <td>LinkedIn</td>
      <td>New jobs similar to HR Business Partner at Jump Trading</td>
      <td>LinkedIn job recommendations relevant to HRBP search. Review.</td>
    </tr>
    <tr>
      <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
      <td>Match</td>
      <td>Michael likes you. See if it's mutual.</td>
      <td>Michael liked your Match profile. Personal — low urgency.</td>
    </tr>
    <tr>
      <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
      <td>LinkedIn Job Alerts</td>
      <td>You may be a fit for Posh's Head of People role</td>
      <td>Head of People at Posh — strong fit alert. Review today.</td>
    </tr>
    <tr>
      <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
      <td>Hinge Team</td>
      <td>Marc &amp; Melissa, we recommend you to each other.</td>
      <td>Hinge match recommendation — Marc. Personal.</td>
    </tr>
    <tr>
      <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
      <td>Melissa W (self)</td>
      <td>Skills to install in Claude</td>
      <td>Self-sent LinkedIn article link about Claude AI skills. Save for review.</td>
    </tr>
    <tr>
      <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
      <td>Melissa W (self)</td>
      <td>Chat job hunting prompts</td>
      <td>Self-sent LinkedIn link — job hunting prompt resource. Save/review.</td>
    </tr>
    <tr>
      <td><span class="status-badge badge-inbox">📥 INBOX</span></td>
      <td>Melissa W (self)</td>
      <td>Chat job hunting prompts</td>
      <td>Second self-sent link — another job hunting prompt resource.</td>
    </tr>
    <!-- ── TRASH summary rows ── -->
    <tr style="background:#fff5f5;">
      <td><span class="status-badge badge-autotrash">🗑 AUTO-TRASHED</span></td>
      <td colspan="3"><strong>2 emails auto-trashed (phishing/scam)</strong> — see Trash Review section for details. No action needed.</td>
    </tr>
    <tr style="background:#edf2f7;">
      <td><span class="status-badge badge-trash">🗂 TRASH</span></td>
      <td colspan="3"><strong>40 emails in Trash</strong> (newsletters, promotions, spam, digests, manually trashed) — see Trash Review section for full breakdown.</td>
    </tr>
  </tbody>
</table>

<!-- ═══════════════════════════════════════════════════
     SECTION 1 — HEADER (inline above, meta block done)
     SECTION 2 — EXECUTIVE SUMMARY
═══════════════════════════════════════════════════ -->
<div class="section-title">⚡ Executive Summary</div>
<div class="exec-summary">
  <ul>
    <li>
      <span class="pill pill-red">🔴 RISK</span>
      <span>Multiple phishing/scam emails detected (fake CashApp, fake Omaha Steaks, penis enlargement spam, casino scam). Two were auto-trashed before reaching inbox. Two additional spam emails remain untrashed — recommend immediate deletion.</span>
    </li>
    <li>
      <span class="pill pill-green">🟢 JOB SEARCH</span>
      <span>Strong job search momentum: You sent a follow-up to GitLab recruiter Rich this morning for the <strong>Senior Director, People Business Partners</strong> role (referred by Rob Demarais). Also surfaced: <strong>Head of People at Posh</strong>, <strong>VP People at DomainTools ($175K–$275K)</strong>, and <strong>CPO at Kinora Group</strong>. Recruiter call scheduled tomorrow 9:30 AM.</span>
    </li>
    <li>
      <span class="pill pill-blue">🔵 CALENDAR</span>
      <span>Hair appointment with Elle at UMI Salon <strong>TODAY at 9:15 AM</strong> (37 W 20th St, Suite 1107). RSVP still pending for two HR Networking Zoom sessions this week (Aug 26 &amp; Aug 27). You declined the Executive Roundtable on Aug 27 — confirm that's intentional.</span>
    </li>
  </ul>
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 3 — ACTION REQUIRED
═══════════════════════════════════════════════════ -->
<div class="section-title">🚨 Action Required</div>

<div class="card yellow">
  <h3>⚠️ RSVP Needed — HR Networking Zoom (Aug 26 &amp; Aug 27)</h3>
  <div class="meta-row">
    <span><strong>Source:</strong> Google Calendar</span>
    <span><strong>Status:</strong> needsAction (no RSVP sent)</span>
    <span><strong>Due:</strong> Before Aug 26, 12:00 PM</span>
  </div>
  <p><strong>Aug 26:</strong> HR Networking &amp; Job Search Group — Zoom 2 (12:00–1:30 PM). <strong>Aug 27:</strong> HR Networking &amp; Job Search: Open Office Hours — Zoom 2 (12:00–1:00 PM). Both have large attendee lists of HR professionals. High networking value during job search.</p>
  <p><strong>Why it matters:</strong> These are active peer networking sessions with 180+ HR professionals — critical for job search visibility.</p>
  <span class="action-tag">RSVP YES or NO</span><span class="due-tag">Before Aug 26</span>
</div>

<div class="card green">
  <h3>✅ GitLab Application Follow-Up — Confirm Receipt</h3>
  <div class="meta-row">
    <span><strong>Source:</strong> Gmail — Sent (amylw516@gmail.com)</span>
    <span><strong>Date Sent:</strong> Mon Aug 24, 8:35 AM</span>
  </div>
  <p>You emailed recruiter Rich this morning about the <strong>Senior Director, People Business Partners</strong> role at GitLab, referenced Rob Demarais as your referral. This is a high-priority application.</p>
  <p><strong>Why it matters:</strong> Internal referral increases interview chances significantly. Ensure your LinkedIn and resume are current before Rich reviews your profile.</p>
  <span class="action-tag">MONITOR FOR REPLY</span><span class="due-tag">Follow up if no reply by Thu Aug 27</span>
</div>

<div class="card green">
  <h3>🔍 Review Posh Head of People + LinkedIn Job Alerts</h3>
  <div class="meta-row">
    <span><strong>Source:</strong> LinkedIn Job Alerts (jobalerts-noreply@linkedin.com)</span>
    <span><strong>Date:</strong> Mon Aug 24</span>
  </div>
  <p>LinkedIn flagged: <strong>Posh – Head of People</strong> and <strong>VP, People at DomainTools ($175K–$275K/yr)</strong> as strong fits. Also: <strong>CPO at Kinora Group</strong> (fast-growing premium travel &amp; dining). Glassdoor also surfaced remote HR Manager roles at Turing.</p>
  <p><strong>Why it matters:</strong> Multiple senior HR/People leadership roles aligned to your target level. Act before positions fill.</p>
  <span class="action-tag">APPLY / REVIEW TODAY</span>
</div>

<div class="card red">
  <h3>🚫 Delete Remaining Spam/Scam Emails</h3>
  <div class="meta-row">
    <span><strong>Source:</strong> Gmail — not in trash, not in inbox</span>
  </div>
  <p>Four emails remain outside trash and are confirmed spam/scam: (1) "Stamina Boost Formula" — muscle/health spam; (2) "Penis Growth Doctor" — phishing spam; (3) "Penis Growth" (duplicate sender variant); (4) "Omaha Steaks" — fake customer appreciation award via random domain. Also: OkCupid promo and Wayfair email confirmation require quick review.</p>
  <p><strong>Why it matters:</strong> These clutter inbox and some may be phishing attempts.</p>
  <span class="action-tag">DELETE IMMEDIATELY</span>
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 4 — FULL 7-DAY CALENDAR
═══════════════════════════════════════════════════ -->
<div class="section-title">📅 Full 7-Day Calendar</div>

<!-- MONDAY AUG 24 -->
<div class="cal-day">
  <div class="cal-day-header">
    📅 Monday, August 24, 2026 <span class="today-tag">TODAY</span>
  </div>

  <div class="birthday-banner" style="margin-bottom:10px;">🎂 Michael Rich's Birthday — Today! Consider sending a message.</div>

  <div class="cal-event">
    <div>
      <div class="cal-time">All Day</div>
      <div class="cal-allday">🎂 Birthday</div>
    </div>
    <div>
      <div class="cal-title">Michael Rich's Birthday</div>
      <div class="cal-details">Annual reminder. No location.</div>
      <span class="cal-rsvp rsvp-confirmed">✓ Confirmed</span>
      <div class="cal-prep">💡 <strong>Prep:</strong> Send a birthday message or note today.</div>
    </div>
  </div>

  <div class="cal-event">
    <div>
      <div class="cal-time">9:15 AM–10:45 AM</div>
    </div>
    <div>
      <div class="cal-title">💇 Hair Appointment — Elle at UMI Salon</div>
      <div class="cal-details">Single Process with Blowout with Elle M.</div>
      <div class="cal-details">📍 <a href="https://maps.google.com/?q=37+West+20th+Suite+1107+New+York+NY+10011">37 West 20th Suite 1107, New York, NY 10011</a></div>
      <span class="cal-rsvp rsvp-confirmed">✓ Confirmed</span>
      <div class="cal-prep">💡 <strong>Prep:</strong> Allow travel time. Manage appointment at <a href="https://elleatumi.glossgenius.com/a/f3c8e149bb71d70194fb118806b6484d849a">GlossGenius link</a>.</div>
      <div class="cal-conflict" style="margin-top:6px;">⚠️ <strong>Note:</strong> Calendar shows duplicate entries for "Elle" (9:15–10:15) and "Your Appointment at Elle at UMI Salon" (9:15–10:45). The salon booking confirmation is the authoritative record — plan for 10:45 end time.</div>
    </div>
  </div>
</div>

<!-- TUESDAY AUG 25 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Tuesday, August 25, 2026</div>

  <div class="cal-event">
    <div><div class="cal-time">9:30 AM–10:30 AM</div></div>
    <div>
      <div class="cal-title">📞 Recruiter Call</div>
      <div class="cal-details">No additional details provided. Likely tied to active job search.</div>
      <span class="cal-rsvp rsvp-confirmed">✓ Confirmed</span>
      <div class="cal-prep">💡 <strong>Prep:</strong> Review your top target roles (GitLab, Posh, DomainTools, Kinora) before the call. Prepare your 30-second pitch and salary range talking points. Confirm call-in details if not already received.</div>
    </div>
  </div>

  <div class="cal-event">
    <div><div class="cal-time">4:30 PM–5:30 PM</div></div>
    <div>
      <div class="cal-title">💅 Nails</div>
      <div class="cal-details">Personal appointment. No location provided.</div>
      <span class="cal-rsvp rsvp-confirmed">✓ Confirmed</span>
    </div>
  </div>
</div>

<!-- WEDNESDAY AUG 26 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Wednesday, August 26, 2026</div>

  <div class="birthday-banner" style="margin-bottom:10px;">🥂 Amy's Anniversary — Today! Consider sending a congratulations message.</div>

  <div class="cal-event">
    <div><div class="cal-time">All Day</div><div class="cal-allday">🥂 Anniversary</div></div>
    <div>
      <div class="cal-title">Amy's Anniversary</div>
      <div class="cal-details">Annual reminder.</div>
      <span class="cal-rsvp rsvp-confirmed">✓ Confirmed</span>
    </div>
  </div>

  <div class="cal-event">
    <div><div class="cal-time">12:00 PM–1:30 PM</div></div>
    <div>
      <div class="cal-title">🤝 HR Networking &amp; Job Search Group — Zoom 2</div>
      <div class="cal-details">Large group networking session. 180+ HR professionals attending.</div>
      <div class="cal-details">🔗 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1">Zoom Link</a></div>
      <span class="cal-rsvp rsvp-pending">⚠ RSVP Pending — needsAction</span>
      <div class="cal-prep">💡 <strong>Prep:</strong> RSVP immediately. Review Team Guidelines linked in description. Prepare a brief intro and target role summary. Note: AI notetaking tools allowed for this session.</div>
      <div class="cal-conflict">⚠️ <strong>Duplicate entry:</strong> "Network" is also on calendar at 12:00–1:30 PM with no details — likely the same event. Confirm and delete duplicate.</div>
    </div>
  </div>

  <div class="cal-event">
    <div><div class="cal-time">3:00 PM–4:00 PM</div></div>
    <div>
      <div class="cal-title">💅 Nails</div>
      <div class="cal-details">Personal appointment. No location provided.</div>
      <span class="cal-rsvp rsvp-confirmed">✓ Confirmed</span>
      <div class="cal-conflict">⚠️ <strong>Note:</strong> Nails appointment at 3:00 PM follows immediately after Networking session (ends 1:30 PM). Sufficient buffer exists.</div>
    </div>
  </div>
</div>

<!-- THURSDAY AUG 27 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Thursday, August 27, 2026</div>

  <div class="birthday-banner" style="margin-bottom:10px;">🎂 Christian H's Birthday — Today! Consider sending a message.</div>

  <div class="cal-event">
    <div><div class="cal-time">All Day</div><div class="cal-allday">🎂 Birthday</div></div>
    <div>
      <div class="cal-title">Christian H's Birthday</div>
      <span class="cal-rsvp rsvp-confirmed">✓ Confirmed</span>
    </div>
  </div>

  <div class="cal-event">
    <div><div class="cal-time">9:00 AM–10:30 AM</div></div>
    <div>
      <div class="cal-title">🏛 Executive Roundtable (John Madigan)</div>
      <div class="cal-details">Zoom roundtable hosted by John Madigan.</div>
      <div class="cal-details">🔗 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09">Zoom Link</a> | Meeting ID: 207 786 667 | PW: 205454</div>
      <span class="cal-rsvp rsvp-declined">✗ DECLINED</span>
      <div class="cal-prep">💡 <strong>Note:</strong> You declined this event. Confirm that was intentional — given your active job search, executive roundtables can be high-value networking opportunities. Consider attending or following up with John Madigan directly.</div>
    </div>
  </div>

  <div class="cal-event">
    <div><div class="cal-time">12:00 PM–1:00 PM</div></div>
    <div>
      <div class="cal-title">🤝 HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
      <div class="cal-details">Open office hours format. Same large HR community.</div>
      <div class="cal-details">🔗 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1">Zoom Link</a></div>
      <span class="cal-rsvp rsvp-pending">⚠ RSVP Pending — needsAction</span>
      <div class="cal-prep">💡 <strong>Prep:</strong> RSVP required. <strong>Important:</strong> Organizer requests AI notetaking tools be turned OFF for this session. Prepare questions for open discussion. Great opportunity to share job search updates with the group.</div>
      <div class="cal-conflict">⚠️ <strong>Conflict Alert:</strong> Executive Roundtable (9:00–10:30 AM) and Open Office Hours (12:00–1:00 PM) are both on Thursday — no time conflict, but you declined the Roundtable. Both are valuable; consider reversing your Roundtable declination.</div>
    </div>
  </div>
</div>

<!-- NO EVENTS FRI-SUN -->
<div class="cal-day">
  <div class="cal-day-header">📅 Friday, August 28 — Sunday, August 30, 2026</div>
  <div style="font-size:13px;color:#718096;padding:10px 0;">No calendar events scheduled for this period. Use the time for job applications, interview prep, or rest.</div>
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 5 — JOB SEARCH & INTERVIEW PIPELINE
═══════════════════════════════════════════════════ -->
<div class="section-title">💼 Job Search &amp; Interview Pipeline</div>

<table class="data-table">
  <thead>
    <tr>
      <th>Fit</th>
      <th>Role / Company</th>
      <th>Source</th>
      <th>Status / Notes</th>
      <th>Next Step</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="rank-high">HIGH</span></td>
      <td><strong>Senior Director, People Business Partners</strong><br>GitLab</td>
      <td>Email sent (amylw516 → Rich) + LinkedIn Alert</td>
      <td>Applied. Referred by Rob Demarais (GitLab team member). Follow-up sent today 8:35 AM to recruiter Rich.</td>
      <td>Monitor inbox for reply from Rich. Follow up Thursday if no response.</td>
    </tr>
    <tr>
      <td><span class="rank-high">HIGH</span></td>
      <td><strong>Head of People</strong><br>Posh</td>
      <td>LinkedIn Job Alerts</td>
      <td>Flagged as strong fit. Description: "We are all social creatures…" — early-stage social/community company.</td>
      <td>Review full JD on LinkedIn. Apply if aligned to target level.</td>
    </tr>
    <tr>
      <td><span class="rank-high">HIGH</span></td>
      <td><strong>VP, People</strong><br>DomainTools — $175K–$275K/yr</td>
      <td>LinkedIn Job Alerts (2 alerts, Sat + Sun)</td>
      <td>High salary range. Appeared in two separate LinkedIn alerts — signals active posting. Unread.</td>
      <td>Review JD and apply if aligned. Prioritize given salary range.</td>
    </tr>
    <tr>
      <td><span class="rank-med">MED</span></td>
      <td><strong>Chief People Officer</strong><br>Kinora Group</td>
      <td>LinkedIn Job Alerts</td>
      <td>Fast-growing premium travel &amp; dining company. CPO-level role — potentially above or at target level.</td>
      <td>Research Kinora Group. Apply if company stage/size fits your target.</td>
    </tr>
    <tr>
      <td><span class="rank-med">MED</span></td>
      <td><strong>HR Business Partner (similar roles)</strong><br>Jump Trading &amp; others</td>
      <td>LinkedIn — "New jobs similar to HR Business Partner at Jump Trading"</td>
      <td>Batch alert with multiple similar roles. May include roles below target level but worth scanning.</td>
      <td>Scan the alert for senior-level variations. Apply selectively.</td>
    </tr>
    <tr>
      <td><span class="rank-low">LOW</span></td>
      <td><strong>Remote HR Manager</strong><br>Turing &amp; others (7 roles)</td>
      <td>Glassdoor Jobs alert (trashed)</td>
      <td>Trashed by system — likely below target level (Manager vs. Director/VP). Included for awareness.</td>
      <td>Skip unless you want to explore manager-level fallback options.</td>
    </tr>
    <tr style="background:#f0fff4;">
      <td colspan="2"><strong>📅 Recruiter Call — Tomorrow (Tue Aug 25, 9:30 AM)</strong></td>
      <td>Google Calendar</td>
      <td>Details unknown — no recruiter name or company in calendar description.</td>
      <td>Confirm call details. Prep pitch &amp; salary expectations tonight.</td>
    </tr>
    <tr style="background:#f0fff4;">
      <td colspan="2"><strong>🤝 HR Networking Zoom — Wed Aug 26, 12:00 PM (RSVP pending)</strong></td>
      <td>Google Calendar</td>
      <td>Large HR peer network — 180+ members. High visibility opportunity.</td>
      <td>RSVP yes. Prepare intro &amp; current search status.</td>
    </tr>
    <tr style="background:#f0fff4;">
      <td colspan="2"><strong>🤝 HR Open Office Hours — Thu Aug 27, 12:00 PM (RSVP pending)</strong></td>
      <td>Google Calendar</td>
      <td>Open-format networking. AI notetaking off. Good for peer support and leads.</td>
      <td>RSVP yes. Prepare update on active applications.</td>
    </tr>
    <tr style="background:#ebf8ff;">
      <td colspan="2"><strong>🔗 Self-Saved: Job Hunting Prompts &amp; Claude Skills</strong></td>
      <td>Self-sent emails (melissaw212@gmail.com)</td>
      <td>Three self-sent emails with LinkedIn links: Claude AI skills, job hunting prompts (2 links).</td>
      <td>Save links to notes app. Use prompts to optimize applications and LinkedIn profile this week.</td>
    </tr>
  </tbody>
</table>

<!-- LinkedIn Optimization note -->
<div class="note-box" style="margin-top:14px;">
  💡 <strong>LinkedIn Profile Tip:</strong> A LinkedIn notification suggests connecting with <strong>Melissa A Weiss, MPA</strong> (Head of People | VP HR | Senior Director, HR). She may be a valuable network contact in your same job search space. The newsletter "Job Search Unlocked: LinkedIn Optimization – Keywords" (trashed) may also be worth retrieving.
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 6 — FULL EMAIL REVIEW BY CATEGORY
═══════════════════════════════════════════════════ -->
<div class="section-title">📂 Full Email Review by Category</div>

<!-- SECURITY / RISK -->
<div class="cat-card" style="border-left:5px solid #e53e3e;">
  <div class="cat-header">
    <span class="cat-icon">🔴</span>
    <span class="cat-title">Security / Risk</span>
    <span class="cat-count">6 emails</span>
  </div>
  <div class="cat-body">
    <div class="email-list-row">
      <span><strong>Auto-Trashed — Phishing:</strong> "💲CashApp💲" &lt;wgnlsupportyuh@iyoapfdriwifcnuyqsicvrni.com&gt; — Fake CashApp payment notification for "Raging Bull Casino." Uses Unicode obfuscation, random domain, unfilled template variables. <span class="inline-tag tag-auto">AUTO-TRASHED</span></span>
    </div>
    <div class="email-list-row">
      <span><strong>Spam/Scam (not trashed):</strong> "Stamina Boost Formula" &lt;udsupportwm@ngtsyynsrxybsvpxjqnbmcwa.com&gt; — Random domain, unsolicited health spam. Subject: "This Quick Morning Habit Got a 97-year-old Rock Hard…"</span>
    </div>
    <div class="email-list-row">
      <span><strong>Spam/Scam (not trashed):</strong> "'Penis Growth Doctor'" &lt;nwdicdirkqq@gvfc.pazdjyonwkhme.us&gt; — Classic phishing spam. Subject: "Stop Being Small Add 3.8 Inches in 12 Days at Home"</span>
    </div>
    <div class="email-list-row">
      <span><strong>Spam/Scam (not trashed):</strong> "'Penis Growth'" &lt;espavuakjtqfpr…@3ugy0f.qxk9ig.jgccuh.us&gt; — Duplicate variant of above spam.</span>
    </div>
    <div class="email-list-row">
      <span><strong>Fake Brand (not trashed):</strong> "Omaha Steaks" &lt;sldsupportlrm@ciuvlbttfwtsttqpktitcyoj.com&gt; — Spoofed Omaha Steaks sender. Fake "Customer Appreciation Award." Urgent-sounding subject line. Random domain.</span>
    </div>
    <div class="email-list-row">
      <span><strong>Trashed — Casino Scam:</strong> "💰MIAMI-CLUB" &lt;psqzsupportki@kdxxgbjsltivxqwmzutxqbcj.com&gt; — Fake casino winner notification. In trash. <span class="inline-tag tag-auto">IN TRASH</span></span>
    </div>
    <span class="rec-tag rec-act">DELETE IMMEDIATELY (untrashed spam) | Auto-trashed items: No action needed</span>
  </div>
</div>

<!-- JOB SEARCH -->
<div class="cat-card" style="border-left:5px solid #38a169;">
  <div class="cat-header">
    <span class="cat-icon">🟢</span>
    <span class="cat-title">Job Search</span>
    <span class="cat-count">8 emails</span>
  </div>
  <div class="cat-body">
    <div class="email-list-row"><span><strong>SENT:</strong> Melissa → Rich (GitLab) — Senior Director, People Business Partners follow-up. Referred by Rob Demarais. Sent today 8:35 AM. <strong>High priority.</strong></span></div>
    <div class="email-list-row"><span><strong>LinkedIn Alert:</strong> Posh — Head of People role fit alert. Inbox. Unread.</span></div>
    <div class="email-list-row"><span><strong>LinkedIn Alert:</strong> VP, People at DomainTools — $175K–$275K/yr. (2 alerts — Sunday + Monday, both unread, not in trash)</span></div>
    <div class="email-list-row"><span><strong>LinkedIn Alert:</strong> GitLab Senior Director, People Business Partner — alert received Sunday. Read. Not in trash.</span></div>
    <div class="email-list-row"><span><strong>LinkedIn Alert:</strong> Kinora Group CPO — Chief People Officer. Read. Not in trash.</span></div>
    <div class="email-list-row"><span><strong>LinkedIn Alert:</strong> New jobs similar to HR Business Partner at Jump Trading. Inbox. Unread.</span></div>
    <div class="email-list-row"><span><strong>Glassdoor (trashed):</strong> Remote HR Managers at Turing + 7 more remote roles. Trashed.</span></div>
    <div class="email-list-row"><span><strong>Glassdoor (trashed):</strong> Community Property Manager at Orbach Group + 6 NYC roles. Trashed — misaligned to target.</span></div>
    <span class="rec-tag rec-act">REVIEW &amp; APPLY — Posh, DomainTools, Kinora Group</span>
  </div>
</div>

<!-- PROFESSIONAL DEVELOPMENT / NETWORKING -->
<div class="cat-card" style="border-left:5px solid #805ad5;">
  <div class="cat-header">
    <span class="cat-icon">🟣</span>
    <span class="cat-title">Professional Development &amp; Networking</span>
    <span class="cat-count">5 emails</span>
  </div>
  <div class="cat-body">
    <div class="email-list-row"><span><strong>Self-sent:</strong> "Skills to install in Claude" — LinkedIn link (lnkd.in). Inbox. Unread. AI productivity resource.</span></div>
    <div class="email-list-row"><span><strong>Self-sent:</strong> "Chat job hunting prompts" — LinkedIn link (lnkd.in). Inbox. Unread. Job search AI prompts.</span></div>
    <div class="email-list-row"><span><strong>Self-sent:</strong> "Chat job hunting prompts" (second link) — LinkedIn link (lnkd.in). Inbox. Unread.</span></div>
    <div class="email-list-row"><span><strong>LinkedIn (trashed):</strong> "Job Search Unlocked: LinkedIn Optimization: Keywords" — Substack newsletter about keyword optimization for LinkedIn. Trashed.</span></div>
    <div class="email-list-row"><span><strong>LinkedIn:</strong> Suggested connection — Melissa A Weiss, MPA (Head of People | VP HR). Read. Not in trash.</span></div>
    <span class="rec-tag rec-keep">SAVE self-sent links | CONSIDER restoring LinkedIn Optimization newsletter</span>
  </div>
</div>

<!-- CALENDAR / EVENTS -->
<div class="cat-card" style="border-left:5px solid #3182ce;">
  <div class="cat-header">
    <span class="cat-icon">🔵</span>
    <span class="cat-title">Calendar / Events</span>
    <span class="cat-count">1 email</span>
  </div>
  <div class="cat-body">
    <div class="email-list-row"><span><strong>Otter.ai Insights (trashed):</strong> "Your upcoming meetings" — Weekly Otter.ai digest of upcoming meetings and AI notes. Trashed.</span></div>
    <span class="rec-tag rec-del">TRASH — low value; your calendar covers this</span>
  </div>
</div>

<!-- PERSONAL -->
<div class="cat-card" style="border-left:5px solid #ed8936;">
  <div class="cat-header">
    <span class="cat-icon">🟠</span>
    <span class="cat-title">Personal (Dating Apps)</span>
    <span class="cat-count">5 emails</span>
  </div>
  <div class="cat-body">
    <div class="email-list-row"><span><strong>Match (Inbox):</strong> "You've had a profile view from Paul" — Paul, 64, Palmerton PA. Unread.</span></div>
    <div class="email-list-row"><span><strong>Match (Inbox):</strong> "Michael likes you. See if it's mutual." — Unread.</span></div>
    <div class="email-list-row"><span><strong>Match (Read, not in trash):</strong> "You've had a profile view from Charlie" — Charlie, 64, Quinton NJ. Read.</span></div>
    <div class="email-list-row"><span><strong>Hinge (Inbox, Read):</strong> "Marc &amp; Melissa, we recommend you to each other." — Most Compatible match.</span></div>
    <div class="email-list-row"><span><strong>OkCupid (not in trash):</strong> "It's prime time! 💘" — Promo nudge to log in. Unread.</span></div>
    <span class="rec-tag rec-rev">REVIEW when time permits — personal priority</span>
  </div>
</div>

<!-- ACCOUNT / SECURITY NOTICE -->
<div class="cat-card" style="border-left:5px solid #e53e3e;">
  <div class="cat-header">
    <span class="cat-icon">🔐</span>
    <span class="cat-title">Account Notices</span>
    <span class="cat-count">2 emails</span>
  </div>
  <div class="cat-body">
    <div class="email-list-row"><span><strong>Google (not in trash):</strong> "You shared some Google Account data with Kimi" — Legitimate Google notification. You signed in to Kimi (Moonshot AI chatbot) with your Google account. Unread.</span></div>
    <div class="email-list-row"><span><strong>Wayfair (not in trash, read):</strong> "Confirm your email" — Wayfair email confirmation request. Read. May indicate account creation.</span></div>
    <span class="rec-tag rec-rev">REVIEW — Confirm Kimi sign-in was intentional. Complete Wayfair verification if account was intended.</span>
  </div>
</div>

<!-- PROFESSIONAL DEVELOPMENT NEWSLETTERS -->
<div class="cat-card" style="border-left:5px solid #805ad5;">
  <div class="cat-header">
    <span class="cat-icon">🟣</span>
    <span class="cat-title">Newsletters &amp; Subscriptions</span>
    <span class="cat-count">10 emails</span>
  </div>
  <div class="cat-body">
    <div class="email-list-row"><span><strong>Talent Edge Weekly #361</strong> — Brian Heger. HR/talent leadership content. Trashed.</span></div>
    <div class="email-list-row"><span><strong>Dylan's Diary</strong> — "The Walmart Recession Signal Hit Its Highest Level Since 2008." Finance/economic signal. Trashed.</span></div>
    <div class="email-list-row"><span><strong>LinkedIn Daily Rundown</strong> — Moderna's new chapter, R.I.P. summer internships. Trashed.</span></div>
    <div class="email-list-row"><span><strong>Chase Coleman (Substack)</strong> — "My Agency's AI Agents Were Cutting Corners." AI/agency operations content. Trashed.</span></div>
    <div class="email-list-row"><span><strong>Vaishali Lambe / Medium</strong> — "Generative AI and Agentic AI Unveiled Through a Traffic Network Analogy." Trashed.</span></div>
    <div class="email-list-row"><span><strong>Insider Monkey</strong> — Daily newsletter, Aug 23. Finance/investment. Trashed.</span></div>
    <div class="email-list-row"><span><strong>The Daily Skimm</strong> — "What's the beef?" — Aug 24 edition. Women in C-suite career advice. Trashed.</span></div>
    <div class="email-list-row"><span><strong>Medium Daily Digest</strong> — UX/UI Trends by Punit Chawla. Trashed.</span></div>
    <div class="email-list-row"><span><strong>Job Search Unlocked (Substack)</strong> — LinkedIn Optimization: Keywords. Trashed. <span class="inline-tag tag-news">CONSIDER RESTORE</span></span></div>
    <div class="email-list-row"><span><strong>Alison Courses</strong> — "Your future skills are here." Trashed.</span></div>
    <span class="rec-tag rec-rev">REVIEW Talent Edge Weekly + Job Search Unlocked before deleting — HR-relevant content</span>
  </div>
</div>

<!-- PROMOTIONAL / RETAIL -->
<div class="cat-card" style="border-left:5px solid #a0aec0;">
  <div class="cat-header">
    <span class="cat-icon">🛍</span>
    <span class="cat-title">Promotional / Retail</span>
    <span class="cat-count">13 emails</span>
  </div>
  <div class="cat-body">
    <div class="email-list-row"><span>SHEIN — "All under $14.99" (2 duplicate emails — different sender domains). Both trashed.</span></div>
    <div class="email-list-row"><span>Chick-fil-A — "Chicken &amp; Waffles are here" + "A little thing…from us to you" (reward). Both trashed. <strong>402 pts — you have a reward waiting.</strong></span></div>
    <div class="email-list-row"><span>Kohl's — "20% off + Kohl's Cash – Friends &amp; Family." Trashed.</span></div>
    <div class="email-list-row"><span>Gap Factory — "50% off dresses, tees, and pants (up to 75% off)." Trashed.</span></div>
    <div class="email-list-row"><span>VIVAIA — "Something Is Being Reworked." Teaser/new collection. Trashed.</span></div>
    <div class="email-list-row"><span>Temu — "womens clothing is calling." Trashed.</span></div>
    <div class="email-list-row"><span>Laura Geller Beauty — "60% OFF Leaked Early 🫢" (2 duplicate emails). Both trashed.</span></div>
    <div class="email-list-row"><span>YesStyle.com — "⏳ One week left to claim 12% OFF" <span class="inline-tag tag-auto">AUTO-TRASHED (newsletter)</span></span></div>
    <div class="email-list-row"><span>Equifax — "It's your credit. Take control." — Equifax Complete Premier promo. Trashed. (Note: Verify this is from real equifax.com — sender is info@e.
