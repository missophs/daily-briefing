<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa — June 20, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* Header */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 2rem; font-weight: 700; letter-spacing: 1px; }
  .header .subtitle { font-size: 1.05rem; color: #a8c8f8; margin-top: 6px; }
  .header-meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header-meta .meta-box { background: rgba(255,255,255,0.1); border-radius: 8px; padding: 10px 20px; text-align: center; }
  .header-meta .meta-box .num { font-size: 1.6rem; font-weight: 700; color: #7dd3fc; }
  .header-meta .meta-box .label { font-size: 0.75rem; color: #cbd5e1; text-transform: uppercase; letter-spacing: 1px; }

  /* Section */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 1.1rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 10px 16px; border-radius: 8px 8px 0 0; margin-bottom: 0; }
  .section-body { background: #fff; border-radius: 0 0 10px 10px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .section-wrapper { border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 24px; }

  /* Color themes */
  .red .section-title    { background: #dc2626; color: #fff; }
  .yellow .section-title { background: #d97706; color: #fff; }
  .blue .section-title   { background: #2563eb; color: #fff; }
  .green .section-title  { background: #16a34a; color: #fff; }
  .purple .section-title { background: #7c3aed; color: #fff; }
  .gray .section-title   { background: #6b7280; color: #fff; }
  .navy .section-title   { background: #1e3a5f; color: #fff; }
  .teal .section-title   { background: #0d9488; color: #fff; }

  /* Executive Summary bullets */
  .exec-bullets { list-style: none; padding: 0; }
  .exec-bullets li { padding: 10px 14px; margin-bottom: 8px; border-radius: 8px; font-size: 0.97rem; display: flex; align-items: flex-start; gap: 10px; }
  .exec-bullets li .icon { font-size: 1.2rem; flex-shrink: 0; }
  .bullet-red    { background: #fef2f2; border-left: 4px solid #dc2626; }
  .bullet-green  { background: #f0fdf4; border-left: 4px solid #16a34a; }
  .bullet-blue   { background: #eff6ff; border-left: 4px solid #2563eb; }

  /* Cards */
  .card { border-radius: 10px; padding: 16px 18px; margin-bottom: 14px; border-left: 5px solid #ccc; background: #fff; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }
  .card-red    { border-left-color: #dc2626; background: #fff5f5; }
  .card-yellow { border-left-color: #d97706; background: #fffbeb; }
  .card-blue   { border-left-color: #2563eb; background: #eff6ff; }
  .card-green  { border-left-color: #16a34a; background: #f0fdf4; }
  .card-purple { border-left-color: #7c3aed; background: #f5f3ff; }
  .card-gray   { border-left-color: #9ca3af; background: #f9fafb; }
  .card-teal   { border-left-color: #0d9488; background: #f0fdfa; }

  .card-title { font-weight: 700; font-size: 0.97rem; margin-bottom: 6px; }
  .card-row { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 3px; }
  .badge { display: inline-block; font-size: 0.7rem; font-weight: 700; padding: 2px 8px; border-radius: 20px; text-transform: uppercase; letter-spacing: 0.5px; }
  .badge-red    { background: #fee2e2; color: #991b1b; }
  .badge-yellow { background: #fef3c7; color: #92400e; }
  .badge-blue   { background: #dbeafe; color: #1e40af; }
  .badge-green  { background: #dcfce7; color: #166534; }
  .badge-purple { background: #ede9fe; color: #5b21b6; }
  .badge-gray   { background: #f3f4f6; color: #374151; }
  .badge-teal   { background: #ccfbf1; color: #115e59; }
  .badge-orange { background: #ffedd5; color: #9a3412; }

  .card-meta { font-size: 0.82rem; color: #555; margin-top: 2px; }
  .card-action { font-size: 0.85rem; font-weight: 600; color: #1e3a5f; margin-top: 6px; padding-top: 6px; border-top: 1px dashed #e5e7eb; }

  /* Tables */
  table { width: 100%; border-collapse: collapse; font-size: 0.85rem; }
  th { background: #f1f5f9; color: #374151; font-weight: 700; padding: 9px 12px; text-align: left; border-bottom: 2px solid #e2e8f0; }
  td { padding: 8px 12px; border-bottom: 1px solid #f0f0f0; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f8fafc; }

  /* Calendar */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { background: #1e3a5f; color: #fff; padding: 7px 14px; border-radius: 6px; font-weight: 700; font-size: 0.9rem; margin-bottom: 8px; }
  .cal-event { display: flex; gap: 12px; align-items: flex-start; padding: 10px 14px; background: #fff; border-radius: 8px; margin-bottom: 6px; border-left: 4px solid #2563eb; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }
  .cal-event.declined { border-left-color: #9ca3af; background: #f9fafb; opacity: 0.8; }
  .cal-event.needs-action { border-left-color: #d97706; background: #fffbeb; }
  .cal-event.bill { border-left-color: #dc2626; background: #fff5f5; }
  .cal-time { font-weight: 700; font-size: 0.82rem; color: #2563eb; min-width: 80px; }
  .cal-detail .title { font-weight: 700; font-size: 0.9rem; }
  .cal-detail .meta { font-size: 0.78rem; color: #666; margin-top: 2px; }
  .cal-detail .prep { font-size: 0.78rem; color: #7c3aed; margin-top: 3px; font-style: italic; }
  .cal-detail .conflict { font-size: 0.78rem; color: #dc2626; font-weight: 600; margin-top: 3px; }

  /* Priority */
  .priority-high   { color: #dc2626; font-weight: 700; }
  .priority-medium { color: #d97706; font-weight: 700; }
  .priority-low    { color: #6b7280; font-weight: 600; }

  /* Dashboard grid */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 14px; }
  .dash-tile { background: #fff; border-radius: 10px; padding: 16px; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.08); }
  .dash-tile .num { font-size: 2rem; font-weight: 800; }
  .dash-tile .lbl { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; color: #6b7280; margin-top: 4px; }
  .red-num    { color: #dc2626; }
  .yellow-num { color: #d97706; }
  .blue-num   { color: #2563eb; }
  .green-num  { color: #16a34a; }
  .purple-num { color: #7c3aed; }
  .gray-num   { color: #6b7280; }

  /* Top 3 */
  .top3 { counter-reset: top3; }
  .top3-item { display: flex; align-items: flex-start; gap: 16px; padding: 16px; background: #fff; border-radius: 10px; margin-bottom: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.08); }
  .top3-num { width: 42px; height: 42px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; font-weight: 800; flex-shrink: 0; }
  .top3-num-1 { background: #fef2f2; color: #dc2626; }
  .top3-num-2 { background: #f0fdf4; color: #16a34a; }
  .top3-num-3 { background: #eff6ff; color: #2563eb; }
  .top3-content .title { font-weight: 700; font-size: 1rem; }
  .top3-content .desc { font-size: 0.87rem; color: #555; margin-top: 4px; }

  /* Divider */
  .divider { border: none; border-top: 2px dashed #e5e7eb; margin: 24px 0; }

  /* Spam warning */
  .spam-warning { background: #fef2f2; border: 1px solid #fca5a5; border-radius: 8px; padding: 10px 14px; font-size: 0.83rem; color: #7f1d1d; margin-top: 8px; }

  /* Group row */
  .group-row { background: #f8fafc; border-radius: 8px; padding: 10px 14px; margin-bottom: 8px; border-left: 3px solid #e2e8f0; }
  .group-row .gr-title { font-weight: 700; font-size: 0.9rem; }
  .group-row .gr-meta { font-size: 0.8rem; color: #666; margin-top: 2px; }
  .group-row .gr-rec { font-size: 0.8rem; color: #2563eb; font-weight: 600; margin-top: 4px; }

  a { color: #2563eb; text-decoration: none; }
  a:hover { text-decoration: underline; }

  .footnote { font-size: 0.78rem; color: #9ca3af; margin-top: 10px; font-style: italic; }

  @media(max-width:600px) {
    .header h1 { font-size: 1.3rem; }
    .header-meta { gap: 12px; }
    .dashboard-grid { grid-template-columns: repeat(2, 1fr); }
    .cal-event { flex-direction: column; gap: 4px; }
  }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════════════ HEADER -->
<div class="header">
  <div class="subtitle">✦ EXECUTIVE DAILY BRIEFING ✦</div>
  <h1>Good Morning, Melissa 👋</h1>
  <div class="subtitle">Saturday, June 20, 2026 &nbsp;·&nbsp; Prepared by Your Executive Chief of Staff</div>
  <div class="header-meta">
    <div class="meta-box"><div class="num">50</div><div class="label">Emails Reviewed</div></div>
    <div class="meta-box"><div class="num">8</div><div class="label">Calendar Events</div></div>
    <div class="meta-box"><div class="num">5</div><div class="label">Action Items</div></div>
    <div class="meta-box"><div class="num">3</div><div class="label">Security / Risk Flags</div></div>
    <div class="meta-box"><div class="num">3</div><div class="label">Days to Busy Week</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ EXECUTIVE SUMMARY -->
<div class="section-wrapper navy">
  <div class="section-title">📋 Executive Summary</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li class="bullet-red">
        <span class="icon">🔴</span>
        <span><strong>Security &amp; Risk:</strong> Three high-confidence phishing / spam emails (fake Lowe's prize, fake CloudStorage deletion threat, suspicious Lowe's domain) are sitting in your mailbox undeleted — plus your GitHub Daily Briefing workflow has failed twice. Immediate cleanup and workflow investigation needed.</span>
      </li>
      <li class="bullet-green">
        <span class="icon">🟢</span>
        <span><strong>Job Search Opportunity:</strong> LinkedIn flagged you as a potential fit for Orbital's <em>VP of People</em> role (posted 6/10/2026). This aligns directly with your HR leadership background. You also sent a personal outreach email (now in Trash) to a Shannon — review if follow-up is needed. Your Medium membership was just activated, giving you a writing &amp; thought leadership platform.</span>
      </li>
      <li class="bullet-blue">
        <span class="icon">🔵</span>
        <span><strong>Calendar Priority:</strong> Next week is packed — Eye Doctor appointment Monday at 9 AM, M&amp;M meeting with Monte at 1 PM, HR Networking Zoom (RSVP pending) Tuesday, Executive Roundtable Thursday (you've <em>declined</em> — confirm intentional), and a COBRA payment check Friday. Chase credit card statement is due <strong>July 16</strong> with a minimum payment of $399 — review soon.</span>
      </li>
    </ul>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ ACTION REQUIRED -->
<div class="section-wrapper red">
  <div class="section-title">⚡ Action Required — Items Needing Your Attention</div>
  <div class="section-body">

    <div class="card card-red">
      <div class="card-row">
        <span class="badge badge-red">🔴 SECURITY</span>
        <span class="badge badge-yellow">URGENT</span>
      </div>
      <div class="card-title">Phishing / Spam Emails — Do Not Click</div>
      <div class="card-meta"><strong>Senders:</strong> "CloudStorage — Urgent" (hcg6ltd5f@pcyaaype.zus.tgatkyw.biz) &amp; Fake Lowe's (hhsupportsk@jyyvfceddgzopslvzxoagefb.com)</div>
      <div class="card-meta"><strong>Why It Matters:</strong> Both are textbook phishing — fake urgency (file deletion, prize winner), suspicious domains, using your username. Not in trash, still in your inbox area.</div>
      <div class="card-action">✅ Next Step: Do NOT click any links. Mark both as spam/phishing and delete immediately. Consider enabling Gmail's enhanced spam filtering.</div>
    </div>

    <div class="card card-red">
      <div class="card-row">
        <span class="badge badge-red">🔴 TECH</span>
        <span class="badge badge-yellow">INVESTIGATE</span>
      </div>
      <div class="card-title">GitHub Daily Briefing Workflow Failed (Twice)</div>
      <div class="card-meta"><strong>Sender:</strong> missophs / notifications@github.com — Repo: missophs/daily-briefing, commit d758cae</div>
      <div class="card-meta"><strong>Why It Matters:</strong> Your automated daily briefing via GitHub Actions has failed in all jobs (runs at ~7 AM and ~2 AM PT). The webhook is broken — your automation pipeline is down.</div>
      <div class="card-action">✅ Next Step: Go to GitHub Actions → daily-briefing → review logs on d758cae. Check webhook URL/secret or API keys. Fix before Monday.</div>
      <div class="card-meta">Due: Today / This weekend</div>
    </div>

    <div class="card card-yellow">
      <div class="card-row">
        <span class="badge badge-yellow">💛 BILLING</span>
        <span class="badge badge-blue">DEADLINE</span>
      </div>
      <div class="card-title">Chase Credit Card Statement Available — $399 Min Due July 16</div>
      <div class="card-meta"><strong>Sender:</strong> Chase (no.reply.alerts@chase.com) — Account ending in 2754</div>
      <div class="card-meta"><strong>Why It Matters:</strong> Statement is ready. Minimum payment due $399 by July 16, 2026. Also note Verizon FiOS bill is due June 23.</div>
      <div class="card-action">✅ Next Step: Review full statement online. Schedule payment now. Also confirm Verizon FiOS payment by June 23.</div>
      <div class="card-meta">Due: July 16 (Chase) | June 23 (Verizon)</div>
    </div>

    <div class="card card-green">
      <div class="card-row">
        <span class="badge badge-green">🟢 JOB SEARCH</span>
        <span class="badge badge-yellow">REVIEW</span>
      </div>
      <div class="card-title">LinkedIn Job Alert — Orbital VP of People Role</div>
      <div class="card-meta"><strong>Sender:</strong> LinkedIn (jobs-listings@linkedin.com) — Posted June 10, 2026</div>
      <div class="card-meta"><strong>Why It Matters:</strong> LinkedIn identified you as a potential fit. This is an executive-level People/HR role — directly aligned with your background. Posted 10 days ago; window may be closing.</div>
      <div class="card-action">✅ Next Step: Open LinkedIn email, review full job description, apply or flag if not a fit. Don't let this age further.</div>
      <div class="card-meta">Due: Today or Sunday</div>
    </div>

    <div class="card card-yellow">
      <div class="card-row">
        <span class="badge badge-yellow">💛 RSVP</span>
        <span class="badge badge-blue">CALENDAR</span>
      </div>
      <div class="card-title">HR Networking Zoom — RSVP Pending (Tuesday + Wednesday)</div>
      <div class="card-meta"><strong>Events:</strong> HR Networking &amp; Job Search Group (Tue Jun 24, 12–1:30 PM) | HR Open Office Hours (Wed Jun 25, 12–1 PM)</div>
      <div class="card-meta"><strong>Why It Matters:</strong> Both events show "needsAction" — you haven't confirmed. These are active networking events critical to your job search.</div>
      <div class="card-action">✅ Next Step: RSVP to both events in Google Calendar. Zoom links are available in calendar entries.</div>
      <div class="card-meta">Due: Before Tuesday Jun 24</div>
    </div>

    <div class="card card-blue">
      <div class="card-row">
        <span class="badge badge-blue">📅 CALENDAR</span>
        <span class="badge badge-yellow">CONFIRM</span>
      </div>
      <div class="card-title">Executive Roundtable (Thursday Jun 25) — You Declined. Intentional?</div>
      <div class="card-meta"><strong>Host:</strong> John Madigan via Zoom — Thu Jun 25, 9:00–10:30 AM</div>
      <div class="card-meta"><strong>Why It Matters:</strong> Given your active job search, Executive Roundtables are high-value networking. Confirm your decline was intentional and not accidental.</div>
      <div class="card-action">✅ Next Step: Review invite — if decline was unintentional, reach out to John Madigan and re-accept. If intentional, no action needed.</div>
      <div class="card-meta">Due: Before Thursday</div>
    </div>

    <div class="card card-yellow">
      <div class="card-row">
        <span class="badge badge-yellow">💛 HEALTH</span>
        <span class="badge badge-blue">PREP</span>
      </div>
      <div class="card-title">Warby Parker — Prescription Expired</div>
      <div class="card-meta"><strong>Sender:</strong> Warby Parker (sayhello@mail3.warbyparker.com)</div>
      <div class="card-meta"><strong>Why It Matters:</strong> You have an Eye Doctor appointment Monday June 23, 9–10 AM. Your Warby Parker prescription is expired — coordinate renewal at your appointment.</div>
      <div class="card-action">✅ Next Step: At your Eye Dr. appointment Monday, request an updated prescription. Bring the Warby Parker email to streamline the glasses ordering process afterward.</div>
      <div class="card-meta">Due: Monday, June 23</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ FULL 7-DAY CALENDAR -->
<div class="section-wrapper blue">
  <div class="section-title">📅 Full 7-Day Calendar — June 20–27, 2026</div>
  <div class="section-body">

    <div class="cal-day">
      <div class="cal-day-header">📅 Saturday, June 20, 2026 — TODAY</div>
      <div class="cal-event" style="border-left-color:#6b7280; background:#f9fafb;">
        <div class="cal-time">All Day</div>
        <div class="cal-detail">
          <div class="title">No scheduled meetings today</div>
          <div class="meta">Use today to handle action items: fix GitHub workflow, review Chase statement, apply to Orbital VP role, delete phishing emails.</div>
          <div class="prep">🎯 Prep: Address all Action Required items above.</div>
        </div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">☀️ Sunday, June 21, 2026</div>
      <div class="cal-event" style="border-left-color:#6b7280; background:#f9fafb;">
        <div class="cal-time">All Day</div>
        <div class="cal-detail">
          <div class="title">No scheduled meetings</div>
          <div class="meta">No calendar events. Use for job search review and RSVP to Tuesday/Wednesday Zoom sessions.</div>
          <div class="prep">🎯 Prep: RSVP to HR Networking events. Note: early voting ends Sunday per VFAR email.</div>
        </div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">🏥 Monday, June 23, 2026 — 3 Events</div>

      <div class="cal-event bill">
        <div class="cal-time">All Day</div>
        <div class="cal-detail">
          <div class="title">💳 Verizon FiOS Bill Due</div>
          <div class="meta">Status: Confirmed | Bill payment deadline</div>
          <div class="prep">⚠️ Confirm payment is scheduled or pay today.</div>
        </div>
      </div>

      <div class="cal-event">
        <div class="cal-time">9:00–10:00 AM</div>
        <div class="cal-detail">
          <div class="title">👁️ Eye Doctor Appointment</div>
          <div class="meta">Status: Confirmed | Location: TBD (no location provided)</div>
          <div class="prep">🎯 Prep: Bring insurance card. Ask for updated Rx — Warby Parker prescription is expired. Coordinate order after appointment.</div>
        </div>
      </div>

      <div class="cal-event">
        <div class="cal-time">1:00–2:00 PM</div>
        <div class="cal-detail">
          <div class="title">🤝 M&amp;M Meeting — with Monte Montoya</div>
          <div class="meta">Status: Accepted | Attendee: monte.montoya@gmail.com | Location: TBD</div>
          <div class="prep">🎯 Prep: Confirm agenda with Monte. Is this a networking/job search call or a personal meeting? No description provided — clarify beforehand.</div>
        </div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">🌐 Tuesday, June 24, 2026 — 2 Events (Overlap Conflict)</div>

      <div class="cal-event needs-action">
        <div class="cal-time">12:00–1:30 PM</div>
        <div class="cal-detail">
          <div class="title">🌐 HR Networking &amp; Job Search Group — Zoom Session 2</div>
          <div class="meta">Status: <strong>RSVP PENDING (needsAction)</strong> | 170+ attendees</div>
          <div class="meta">📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a></div>
          <div class="prep">🎯 Prep: Review team guidelines linked in calendar description. Prepare your elevator pitch and any questions for the group.</div>
          <div class="conflict">⚠️ CONFLICT: "Network" event at same time — same Zoom or duplicate? Verify.</div>
        </div>
      </div>

      <div class="cal-event">
        <div class="cal-time">12:00–1:30 PM</div>
        <div class="cal-detail">
          <div class="title">🌐 Network (Personal Calendar Block)</div>
          <div class="meta">Status: Confirmed | No attendees listed | No location</div>
          <div class="conflict">⚠️ CONFLICT: Same time as HR Networking Zoom above — likely a personal reminder duplicate. Confirm and merge or delete one.</div>
        </div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">🎙️ Wednesday, June 25, 2026 — 2 Events</div>

      <div class="cal-event declined">
        <div class="cal-time">9:00–10:30 AM</div>
        <div class="cal-detail">
          <div class="title">🎙️ Executive Roundtable — Hosted by John Madigan</div>
          <div class="meta">Status: <strong>DECLINED</strong> | Zoom Meeting ID: 207 786 667</div>
          <div class="meta">📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> | Password: 205454</div>
          <div class="prep">⚠️ You declined this. Confirm intentional — high-value networking event for an active job seeker. Consider re-accepting.</div>
        </div>
      </div>

      <div class="cal-event needs-action">
        <div class="cal-time">12:00–1:00 PM</div>
        <div class="cal-detail">
          <div class="title">🌐 HR Networking &amp; Job Search — Open Office Hours (Zoom 2)</div>
          <div class="meta">Status: <strong>RSVP PENDING (needsAction)</strong> | 170+ attendees</div>
          <div class="meta">📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a></div>
          <div class="prep">🎯 Prep: Open discussion format — no recording. Come with specific questions or challenges you want the group to help with.</div>
        </div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">📅 Thursday, June 26, 2026</div>
      <div class="cal-event" style="border-left-color:#6b7280; background:#f9fafb;">
        <div class="cal-time">All Day</div>
        <div class="cal-detail">
          <div class="title">No scheduled meetings</div>
          <div class="meta">Use for job applications, follow-ups, and professional development.</div>
        </div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">🏥 Friday, June 27, 2026 — 1 Event</div>

      <div class="cal-event" style="border-left-color: #d97706; background:#fffbeb;">
        <div class="cal-time">10:00–11:00 AM</div>
        <div class="cal-detail">
          <div class="title">🏥 Check COBRA Payments</div>
          <div class="meta">Status: Confirmed | Personal reminder | No attendees</div>
          <div class="prep">🎯 Prep: Log into COBRA portal, verify payment status and upcoming amounts. Note any deadlines. Keep health coverage active.</div>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ JOB SEARCH PIPELINE -->
<div class="section-wrapper green">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">

    <table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Source / Sender</th>
          <th>Details</th>
          <th>Fit</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="badge badge-green">Job Alert</span></td>
          <td>LinkedIn</td>
          <td><strong>VP of People — Orbital</strong><br><span style="font-size:0.8rem;">Posted 6/10/2026 — LinkedIn flagged as potential fit</span></td>
          <td><span class="priority-high">HIGH</span></td>
          <td>Review &amp; apply ASAP — 10 days old</td>
        </tr>
        <tr>
          <td><span class="badge badge-purple">Outreach</span></td>
          <td>Melissa → Shannon (Trash)</td>
          <td><strong>Sent: "Helping leaders turn AI, growth, and org change into real workforce outcomes"</strong><br><span style="font-size:0.8rem;">Personal outreach to Shannon — found in Trash. Scheduled for Sun Jun 21.</span></td>
          <td><span class="priority-high">HIGH</span></td>
          <td>Restore from Trash &amp; confirm sent; follow up if no response</td>
        </tr>
        <tr>
          <td><span class="badge badge-blue">Networking</span></td>
          <td>Google Calendar</td>
          <td><strong>HR Networking &amp; Job Search Group Zoom</strong><br><span style="font-size:0.8rem;">Tue Jun 24, 12–1:30 PM | 170+ HR professionals</span></td>
          <td><span class="priority-high">HIGH</span></td>
          <td>RSVP now — pending status</td>
        </tr>
        <tr>
          <td><span class="badge badge-blue">Networking</span></td>
          <td>Google Calendar</td>
          <td><strong>HR Networking Open Office Hours Zoom</strong><br><span style="font-size:0.8rem;">Wed Jun 25, 12–1 PM | Open discussion</span></td>
          <td><span class="priority-high">HIGH</span></td>
          <td>RSVP now — pending status</td>
        </tr>
        <tr>
          <td><span class="badge badge-teal">Meeting</span></td>
          <td>Google Calendar</td>
          <td><strong>M&amp;M with Monte Montoya</strong><br><span style="font-size:0.8rem;">Mon Jun 23, 1–2 PM — no agenda described</span></td>
          <td><span class="priority-medium">MEDIUM</span></td>
          <td>Confirm agenda — may be networking/referral opportunity</td>
        </tr>
        <tr>
          <td><span class="badge badge-purple">Roundtable</span></td>
          <td>Google Calendar</td>
          <td><strong>Executive Roundtable — John Madigan</strong><br><span style="font-size:0.8rem;">Thu Jun 25, 9–10:30 AM — currently DECLINED</span></td>
          <td><span class="priority-medium">MEDIUM</span></td>
          <td>Review decline — consider re-accepting for executive networking</td>
        </tr>
        <tr>
          <td><span class="badge badge-purple">Newsletter</span></td>
          <td>Katy McFee via LinkedIn</td>
          <td><strong>"What comes up when your name comes up?"</strong><br><span style="font-size:0.8rem;">Personal brand insights — relevant to active job search</span></td>
          <td><span class="priority-medium">MEDIUM</span></td>
          <td>Read — personal branding is directly relevant right now</td>
        </tr>
        <tr>
          <td><span class="badge badge-gray">Thought Leadership</span></td>
          <td>Medium (New Membership)</td>
          <td><strong>Medium membership activated today</strong><br><span style="font-size:0.8rem;">1 new subscriber. Writing platform for HR/AI thought leadership.</span></td>
          <td><span class="priority-medium">MEDIUM</span></td>
          <td>Plan first article — AI + HR leadership is your niche</td>
        </tr>
        <tr>
          <td><span class="badge badge-gray">Civic</span></td>
          <td>VFAR Elections Team</td>
          <td><strong>Final Weekend to Vote Early</strong><br><span style="font-size:0.8rem;">Early voting ends Sunday June 21 in NJ — animal rights candidates</span></td>
          <td><span class="priority-low">LOW (Personal)</span></td>
          <td>If interested, vote before Sunday closing</td>
        </tr>
      </tbody>
    </table>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ FULL EMAIL REVIEW -->
<div class="section-wrapper navy">
  <div class="section-title">📬 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="card card-red" style="margin-bottom:14px;">
      <div class="card-row"><span class="badge badge-red">🔴 SECURITY / RISK</span><span class="badge badge-gray">3 Emails</span></div>
      <div class="card-title">Security, Phishing &amp; Technical Alerts</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td>CloudStorage — Urgent (hcg6ltd5f@pcyaaype…)</td>
            <td>🔴 FINAL NOTICE — Your files are being deleted in 24 hours</td>
            <td><span class="badge badge-red">PHISHING</span></td>
            <td>Delete immediately — do NOT click</td>
          </tr>
          <tr>
            <td>'Lowe's®' (hhsupportsk@jyyvfceddgzop…)</td>
            <td>We have been trying to reach you - melissaw212</td>
            <td><span class="badge badge-red">PHISHING</span></td>
            <td>Delete immediately — fake prize scam</td>
          </tr>
          <tr>
            <td>GitHub (noreply@github.com)</td>
            <td>[GitHub] Sudo email verification code: 48423169</td>
            <td><span class="badge badge-yellow">REVIEW</span></td>
            <td>Code valid 15 min (expired) — you triggered this. Safe to delete.</td>
          </tr>
        </tbody>
      </table>
      <div class="spam-warning">⚠️ Two confirmed phishing emails. Neither is in Trash. Mark as spam and report before deleting.</div>
    </div>

    <!-- JOB SEARCH -->
    <div class="card card-green">
      <div class="card-row"><span class="badge badge-green">💼 JOB SEARCH</span><span class="badge badge-gray">3 Emails</span></div>
      <div class="card-title">Job Opportunities, Applications &amp; Outreach</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Priority</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td>LinkedIn</td>
            <td>You may be a fit for Orbital's VP of People role</td>
            <td><span class="priority-high">HIGH</span></td>
            <td>Review &amp; apply today</td>
          </tr>
          <tr>
            <td>Melissa (Trash)</td>
            <td>Helping leaders turn AI, growth, and org change into real workforce outcomes (to Shannon)</td>
            <td><span class="priority-high">HIGH</span></td>
            <td>Restore from Trash — confirm delivery &amp; follow up</td>
          </tr>
          <tr>
            <td>Fractional In A Box</td>
            <td>Five minutes to momentum</td>
            <td><span class="priority-low">LOW</span></td>
            <td>Read if time permits — fractional leadership content</td>
          </tr>
        </tbody>
      </table>
    </div>

    <br/>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="card card-purple">
      <div class="card-row"><span class="badge badge-purple">📚 PROFESSIONAL DEVELOPMENT</span><span class="badge badge-gray">5 Emails</span></div>
      <div class="card-title">Learning, AI, HR Leadership, Certifications</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td>Katy McFee via LinkedIn</td>
            <td>What comes up when your name comes up?</td>
            <td>Read — personal branding relevance during job search</td>
          </tr>
          <tr>
            <td>Medium Daily Digest</td>
            <td>I Tested Claude vs ChatGPT for Writing</td>
            <td>Read — AI writing tools comparison</td>
          </tr>
          <tr>
            <td>Medium (noreply@medium.com)</td>
            <td>✨ Welcome to your membership</td>
            <td>Save — platform confirmed active</td>
          </tr>
          <tr>
            <td>Medium (noreply@medium.com)</td>
            <td>👋 Welcome to Medium (CEO Tony note)</td>
            <td>Save — onboarding email</td>
          </tr>
          <tr>
            <td>HRCI (Trash)</td>
            <td>Upcoming HRCI Webinars</td>
            <td>Restore from Trash — HRCI is directly relevant to HR credentialing</td>
          </tr>
        </tbody>
      </table>
    </div>

    <br/>

    <!-- MEDIUM / AUDIENCE -->
    <div class="card card-teal">
      <div class="card-row"><span class="badge badge-teal">✍️ MEDIUM PLATFORM</span><span class="badge badge-gray">1 Email</span></div>
      <div class="card-title">Medium — Your Audience Is Growing</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td>Medium</td>
            <td>Your audience is growing — 1 new subscriber (Amy)</td>
            <td>Save — track audience growth. Post content soon.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <br/>

    <!-- CALENDAR / EVENTS -->
    <div class="card card-blue">
      <div class="card-row"><span class="badge badge-blue">📅 CALENDAR / EVENTS</span><span class="badge badge-gray">1 Email</span></div>
      <div class="card-title">Civic / Voting</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td>VFAR Elections Team</td>
            <td>Final Weekend to Vote Early + New Animal Rights Candidates Added</td>
            <td>Early voting ends Sunday — act if interested</td>
          </tr>
        </tbody>
      </table>
    </div>

    <br/>

    <!-- MEDICAL / HEALTH -->
    <div class="card card-yellow">
      <div class="card-row"><span class="badge badge-yellow">🏥 MEDICAL / HEALTH</span><span class="badge badge-gray">1 Email</span></div>
      <div class="card-title">Vision / Prescription</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td>Warby Parker</td>
            <td>Your prescription is expired</td>
            <td>Coordinate updated Rx at Monday Eye Dr. appt</td>
          </tr>
        </tbody>
      </table>
    </div>

    <br/>

    <!-- FINANCIAL / BILLING -->
    <div class="card card-yellow">
      <div class="card-row"><span class="badge badge-yellow">💳 FINANCIAL / BILLING</span><span class="badge badge-gray">2 Emails</span></div>
      <div class="card-title">Bills, Statements &amp; Finance</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Due Date</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td>Chase</td>
            <td>Your credit card statement is available — Account …2754</td>
            <td>July 16, 2026 | Min $399</td>
            <td>Review statement &amp; schedule payment</td>
          </tr>
          <tr>
            <td>SmartAsset Headlines</td>
            <td>How Could a Family Trust Help Protect Your Estate in 2026?</td>
            <td>—</td>
            <td>Read if interested in estate planning / financial planning</td>
          </tr>
        </tbody>
      </table>
    </div>

    <br/>

    <!-- PERSONAL -->
    <div class="card card-gray">
      <div class="card-row"><span class="badge badge-gray">💜 PERSONAL</span><span class="badge badge-gray">4 Emails</span></div>
      <div class="card-title">Dating Apps, Social, Neighbors</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td>OkCupid</td>
            <td>Someone likes you</td>
            <td>Personal — check when time permits</td>
          </tr>
          <tr>
            <td>Match</td>
            <td>Richard likes you. See if it's mutual.</td>
            <td>Personal — check when time permits</td>
          </tr>
          <tr>
            <td>Match</td>
            <td>Howard likes you. See if it's mutual.</td>
            <td>Personal — check when time permits</td>
          </tr>
          <tr>
            <td>Trending on Nextdoor</td>
            <td>This woman just brought a very small ball into the...</td>
            <td>Low priority — neighborhood chatter</td>
          </tr>
        </tbody>
      </table>
    </div>

    <br/>

    <!-- NEWSLETTERS / SUBSCRIPTIONS -->
    <div class="card card-purple">
      <div class="card-row"><span class="badge badge-purple">📰 NEWSLETTERS / SUBSCRIPTIONS</span><span class="badge badge-gray">5 Emails</span></div>
      <div class="card-title">Newsletters, AI Digests, Productivity</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Topic</th><th>Recommendation</th></tr></thead>
        <tbody>
          <tr>
            <td>AI For Leaders</td>
            <td>Americans Spend 2x More Time With AI Companions</td>
            <td>Keep &amp; Read — HR/AI leadership relevance</td>
          </tr>
          <tr>
            <td>CoolDeep AI (Inbox)</td>
            <td>AI roadmap nobody gave you (in Trash)</td>
            <td>In Trash — Review before deleting</td>
          </tr>
          <tr>
            <td>Giulia Guerrieri</td>
            <td>30 days from now, will anything actually be different?</td>
            <td>Review — career/business growth coaching content</td>
          </tr>
          <tr>
            <td>Chelsea with IFTTT</td>
            <td>We tested 24 Applets so you don't have to</td>
            <td>Review — productivity automation; relevant for briefing workflow</td>
          </tr>
          <tr>
            <td>USPS Informed Delivery</td>
            <td>Your Daily Digest for Sat, 6/20 — 2 mailpieces arriving</td>
            <td>Review — check what mail is coming</td>
          </tr>
        </tbody>
      </table>
    </div>

    <br/>

    <!-- PROMOTIONAL / RETAIL -->
    <div class="card card-gray">
      <div class="card-row"><span class="badge badge-gray">🛍️ PROMOTIONAL / RETAIL</span><span class="badge badge-gray">25 Emails</span></div>
      <div class="card-title">Shopping, Beauty, Fashion, Food, Travel — See full breakdown in Section 8 below</div>
      <div class="card-meta" style="margin-top:8px;">Brands include: PUMA, Sephora (×2), Gap Factory, INNBEAUTY, Halara, Kulfi Beauty (×2), Laura Geller (×2), ONE/SIZE, Old Navy, Zappos, VIVAIA, Target, Photoroom, JetBlue Vacations (Trash), Total Wine &amp; More (Trash), Facebook login notice (Trash)</div>
      <div class="card-action">✅ Bulk delete most. Review any active sales. See full categorization below.</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ TRASH REVIEW -->
<div class="section-wrapper red">
  <div class="section-title">🗑️ Trash Review — 12 Emails in Trash</div>
  <div class="section-body">

    <h3 style="color:#16a34a; margin-bottom:10px;">✅ Restore Immediately (2)</h3>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Why Restore</th></tr></thead>
      <tbody>
        <tr>
          <td>Melissa (self)</td>
          <td>Helping leaders turn AI, growth, and org change into real workforce outcomes</td>
          <td>This is Melissa's own outreach email to Shannon — active job search correspondence. Confirm delivery and track follow-up.</td>
        </tr>
        <tr>
          <td>HRCI (hrcimarketing@hrci.org)</td>
          <td>Upcoming HRCI Webinars</td>
          <td>HRCI webinars are directly relevant to Melissa's HR professional development and certification maintenance.</td>
        </tr>
      </tbody>
    </table>

    <h3 style="color:#d97706; margin-top:18px; margin-bottom:10px;">⚠️ Review Before Deleting (3)</h3>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Why Review</th></tr></thead>
      <tbody>
        <tr>
          <td>CoolDeep AI</td>
          <td>AI roadmap nobody gave you / The AI system that took me from burritos to $3M</td>
          <td>AI content may be useful for thought leadership. Quick scan — if low quality, delete.</td>
        </tr>
        <tr>
          <td>Facebook (notification@facebookmail.com)</td>
          <td>You logged into Medium with Facebook</td>
          <td>Confirms you used Facebook login for Medium account — keep as a record of account creation if needed.</td>
        </tr>
        <tr>
          <td>Lisa Rangel (lr@chameleonresumes.com)</td>
          <td>starting things sucks.</td>
          <td>Chameleon Resumes is a professional resume service — may have useful job search content. Quick scan.</td>
        </tr>
      </tbody>
    </table>

    <h3 style="color:#dc2626; margin-top:18px; margin-bottom:10px;">🗑️ Safe to Delete (7)</h3>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Reason</th></tr></thead>
      <tbody>
        <tr>
          <td>Sephora Sale (×2)</td>
          <td>Your beauty wins are turning up the heat ☀️</td>
          <td>Duplicate promotional emails — already trashed, delete permanently.</td>
        </tr>
        <tr>
          <td>ONE/SIZE Beauty</td>
          <td>2 DAYS ONLY: 2X Rewards!</td>
          <td>Promotional — deal likely expired. Delete.</td>
        </tr>
        <tr>
          <td>Total Wine &amp; More</td>
          <td>Save BIG on Father's Day Gifts!</td>
          <td>Father's Day has passed — delete.</td>
        </tr>
        <tr>
          <td>JetBlue Vacations</td>
          <td>Final call! Save up to 100% on flights with a package.</td>
          <td>Promotional travel — already trashed. Delete.</td>
        </tr>
        <tr>
          <td>Stephanie Wigner</td>
          <td>The AI systems running our 5 clinics.</td>
          <td>Unsolicited marketing email — delete.</td>
        </tr>
      </tbody>
    </table>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ PROMOTIONAL / RETAIL SUMMARY -->
<div class="section-wrapper gray">
  <div class="section-title">🛍️ Promotional / Retail Summary</div>
  <div class="section-body">

    <table>
      <thead>
        <tr>
          <th>Brand / Sender</th>
          <th>Count</th>
          <th>Subject / Theme</th>
          <th>In Trash?</th>
          <th>Recommendation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>PUMA</td>
          <td>1</td>
          <td>Your Perfect Running Shoes — shoe quiz</td>
          <td>No</td>
          <td><span class="badge badge-gray">Delete/Ignore</span></td>
        </tr>
        <tr>
          <td>Sephora Sale</td>
          <td>2</td>
          <td>25% off shampoos &amp; conditioners (duplicate)</td>
          <td>Yes (both)</td>
          <td><span class="badge badge-red">Delete from Trash</span></td>
        </tr>
        <tr>
          <td>Gap Factory</td>
          <td>1</td>
          <td>Summer dresses — free shipping + 15% off</td>
          <td>No</td>
          <td><span class="badge badge-gray">Review if interested, else Delete</span></td>
        </tr>
        <tr>
          <td>INNBEAUTY Project</td>
          <td>1</td>
          <td>Pro C Vitamin C serum — brightness + dark spots</td>
          <td>No</td>
          <td><span class="badge badge-gray">Delete/Ignore</span></td>
        </tr>
        <tr>
          <td>Kulfi Beauty</td>
          <td>2</td>
          <td>Browsing help + lip stain promo</td>
          <td>No</td>
          <td><span class="badge badge-gray">Delete/Ignore</span></td>
        </tr>
        <tr>
          <td>Laura Geller</td>
          <td>2</td>
          <td>$30 store credit + 55% off (duplicate)</td>
          <td>No</td>
          <td><span class="badge badge-gray">Delete — duplicate &amp; time-sensitive deal likely expired</span></td>
        </tr>
        <tr>
          <td>ONE/SIZE Beauty</td>
          <td>1</td>
          <td>2X Rewards (2 days only)</td>
          <td>Yes</td>
          <td><span class="badge badge-red">Delete from Trash — expired</span></td>
        </tr>
        <tr>
          <td>Total Wine &amp; More</td>
          <td>1</td>
          <td>Father's Day gifts sale</td>
          <td>Yes</td>
          <td><span class="badge badge-red">Delete from Trash — event passed</span></td>
        </tr>
        <tr>
          <td>Halara</td>
          <td>1</td>
          <td>Friday Treat — styles under $19.95</td>
          <td>No</td>
          <td><span class="badge badge-gray">Delete/Ignore</span></td>
        </tr>
        <tr>
          <td>Warby Parker</td>
          <td>1</td>
          <td>Prescription expired — renew notification</td>
          <td>No</td>
          <td><span class="badge badge-yellow">Keep — actionable (Eye Dr. Mon)</span></td>
        </tr>
        <tr>
          <td>Old Navy</td>
          <td>1</td>
          <td>60% off swim &amp; shorts, $5 dresses</td>
          <td>No</td>
          <td><span class="badge badge-gray">Delete/Ignore</span></td>
        </tr>
        <tr>
          <td>Zappos</td>
          <td>1</td>
          <td>Office-ready footwear</td>
          <td>No</td>
          <td><span class="badge badge-gray">Delete/Ignore</span></td>
        </tr>
        <tr>
          <td>VIVAIA</td>
          <td>1</td>
          <td>New comfort shoes — APMA certified</td>
          <td>No</td>
          <td><span class="badge badge-gray">Delete/Ignore</span></td>
        </tr>
        <tr>
          <td>Target</td>
          <td>1</td>
          <td>Text deals sign-up + 20% off LEGO</td>
          <td>No</td>
          <td><span class="badge badge-gray">Delete/Ignore</span></td>
        </tr>
        <tr>
          <td>Photoroom</td>
          <td>1</td>
          <td>New brand rebrand announcement</td>
          <td>No</td>
          <td><span class="badge badge-gray">Delete/Ignore unless you use Photoroom</span></td>
        </tr>
        <tr>
          <td>JetBlue Vacations</td>
          <td>1</td>
          <td>Norwegian Cruise package "final call"</td>
          <td>Yes</td>
          <td><span class="badge badge-red">Delete from Trash</span></td>
        </tr>
        <tr>
          <td>Trending on Nextdoor (×2)</td>
          <td>2</td>
          <td>Neighborhood trending posts (cat, small ball)</td>
          <td>No</td>
          <td><span class="badge badge-gray">Delete/Ignore</span></td>
        </tr>
      </tbody>
    </table>
    <p class="footnote">* Warby Parker is listed here as a retail email but is also actionable (see Medical/Health). Counted once in Email Accounting under Medical/Health.</p>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ NEWSLETTERS & SUBSCRIPTIONS -->
<div class="section-wrapper purple">
  <div class="section-title">📰 Newsletters &amp; Subscriptions</div>
  <div class="section-body">
    <table>
      <thead>
        <tr>
          <th>Sender</th>
