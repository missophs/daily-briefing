<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa W — Sunday, July 26, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px 24px; margin-bottom: 24px; }
  .header h1 { font-size: 2rem; font-weight: 700; letter-spacing: 0.5px; }
  .header .sub { font-size: 1rem; color: #a8c0e0; margin-top: 6px; }
  .header .meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.1); border-radius: 8px; padding: 8px 18px; font-size: 0.9rem; }
  .header .meta-item span { font-weight: 700; font-size: 1.1rem; display: block; color: #7dd3fc; }

  /* SECTION HEADERS */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 1.05rem; font-weight: 700; letter-spacing: 0.8px; text-transform: uppercase; padding: 10px 16px; border-radius: 8px 8px 0 0; margin-bottom: 0; }
  .section-body { background: #fff; border-radius: 0 0 10px 10px; padding: 18px 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }

  /* COLOR THEMES */
  .red .section-title    { background: #dc2626; color: #fff; }
  .yellow .section-title { background: #d97706; color: #fff; }
  .blue .section-title   { background: #2563eb; color: #fff; }
  .green .section-title  { background: #16a34a; color: #fff; }
  .purple .section-title { background: #7c3aed; color: #fff; }
  .gray .section-title   { background: #6b7280; color: #fff; }
  .navy .section-title   { background: #1e3a5f; color: #fff; }
  .teal .section-title   { background: #0d9488; color: #fff; }
  .orange .section-title { background: #ea580c; color: #fff; }

  /* CARDS */
  .card { border-left: 4px solid #ccc; background: #f8fafc; border-radius: 0 8px 8px 0; padding: 12px 16px; margin-bottom: 12px; }
  .card.red    { border-color: #dc2626; background: #fff5f5; }
  .card.yellow { border-color: #d97706; background: #fffbeb; }
  .card.blue   { border-color: #2563eb; background: #eff6ff; }
  .card.green  { border-color: #16a34a; background: #f0fdf4; }
  .card.purple { border-color: #7c3aed; background: #faf5ff; }
  .card.gray   { border-color: #9ca3af; background: #f9fafb; }
  .card.teal   { border-color: #0d9488; background: #f0fdfa; }
  .card.orange { border-color: #ea580c; background: #fff7ed; }
  .card-label { font-size: 0.7rem; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 4px; }
  .card-label.red    { color: #dc2626; }
  .card-label.yellow { color: #d97706; }
  .card-label.blue   { color: #2563eb; }
  .card-label.green  { color: #16a34a; }
  .card-label.purple { color: #7c3aed; }
  .card-label.gray   { color: #6b7280; }
  .card-label.teal   { color: #0d9488; }
  .card-label.orange { color: #ea580c; }
  .card h3 { font-size: 0.95rem; font-weight: 700; margin-bottom: 4px; }
  .card p  { font-size: 0.85rem; color: #444; line-height: 1.5; margin-bottom: 3px; }
  .card .meta-row { display: flex; gap: 16px; flex-wrap: wrap; margin-top: 6px; }
  .card .meta-row span { font-size: 0.78rem; color: #666; }
  .card .meta-row strong { color: #333; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 0.84rem; }
  th { background: #f1f5f9; font-weight: 700; padding: 8px 10px; text-align: left; border-bottom: 2px solid #e2e8f0; }
  td { padding: 7px 10px; border-bottom: 1px solid #e9ecef; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f8fafc; }

  /* BADGES */
  .badge { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.5px; }
  .badge-red    { background: #fee2e2; color: #dc2626; }
  .badge-yellow { background: #fef3c7; color: #d97706; }
  .badge-blue   { background: #dbeafe; color: #2563eb; }
  .badge-green  { background: #dcfce7; color: #16a34a; }
  .badge-purple { background: #ede9fe; color: #7c3aed; }
  .badge-gray   { background: #f3f4f6; color: #6b7280; }
  .badge-teal   { background: #ccfbf1; color: #0d9488; }
  .badge-orange { background: #ffedd5; color: #ea580c; }

  /* EXEC SUMMARY */
  .exec-summary { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; }
  .exec-bullet { border-radius: 10px; padding: 16px 18px; }
  .exec-bullet.risk    { background: #fff5f5; border: 1.5px solid #fca5a5; }
  .exec-bullet.opp     { background: #f0fdf4; border: 1.5px solid #86efac; }
  .exec-bullet.cal     { background: #eff6ff; border: 1.5px solid #93c5fd; }
  .exec-bullet .icon   { font-size: 1.4rem; margin-bottom: 6px; }
  .exec-bullet h4      { font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 4px; }
  .exec-bullet.risk h4 { color: #dc2626; }
  .exec-bullet.opp  h4 { color: #16a34a; }
  .exec-bullet.cal  h4 { color: #2563eb; }
  .exec-bullet p    { font-size: 0.87rem; color: #444; line-height: 1.5; }

  /* CALENDAR DAY */
  .cal-day { margin-bottom: 16px; }
  .cal-day-header { background: #1e3a5f; color: #fff; font-weight: 700; font-size: 0.88rem; padding: 6px 14px; border-radius: 6px; margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }
  .cal-day-header .today-tag { background: #f59e0b; color: #000; font-size: 0.7rem; padding: 1px 7px; border-radius: 10px; font-weight: 700; }
  .cal-event { display: grid; grid-template-columns: 130px 1fr; gap: 0; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 8px; overflow: hidden; }
  .cal-time { background: #dbeafe; padding: 10px 12px; font-weight: 700; font-size: 0.82rem; color: #1e40af; display: flex; align-items: flex-start; justify-content: center; text-align: center; }
  .cal-detail { padding: 10px 14px; }
  .cal-detail h4 { font-size: 0.9rem; font-weight: 700; margin-bottom: 4px; }
  .cal-detail p  { font-size: 0.8rem; color: #555; margin-bottom: 3px; }
  .cal-event.conflict .cal-time { background: #fee2e2; color: #dc2626; }
  .cal-event.declined .cal-time { background: #f3f4f6; color: #9ca3af; }
  .cal-event.pending .cal-time  { background: #fef3c7; color: #92400e; }

  /* PIPELINE */
  .pipeline-row { display: grid; grid-template-columns: 200px 1fr 80px 80px; gap: 8px; align-items: start; padding: 9px 0; border-bottom: 1px solid #f1f5f9; }
  .pipeline-row:last-child { border-bottom: none; }
  .pipeline-row .role { font-weight: 700; font-size: 0.87rem; }
  .pipeline-row .company { font-size: 0.78rem; color: #666; }
  .pipeline-row .note { font-size: 0.82rem; color: #444; }

  /* DASHBOARD GRID */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }
  .dash-card { background: #fff; border-radius: 10px; padding: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); border-top: 4px solid #ccc; }
  .dash-card.red    { border-top-color: #dc2626; }
  .dash-card.yellow { border-top-color: #d97706; }
  .dash-card.blue   { border-top-color: #2563eb; }
  .dash-card.green  { border-top-color: #16a34a; }
  .dash-card.purple { border-top-color: #7c3aed; }
  .dash-card h4 { font-size: 0.78rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; color: #888; margin-bottom: 8px; }
  .dash-card .big-num { font-size: 2rem; font-weight: 800; line-height: 1; }
  .dash-card.red    .big-num { color: #dc2626; }
  .dash-card.yellow .big-num { color: #d97706; }
  .dash-card.blue   .big-num { color: #2563eb; }
  .dash-card.green  .big-num { color: #16a34a; }
  .dash-card.purple .big-num { color: #7c3aed; }
  .dash-card ul { padding-left: 14px; margin-top: 6px; }
  .dash-card li { font-size: 0.82rem; color: #444; margin-bottom: 3px; }

  /* TOP 3 */
  .top3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; }
  .top3-item { border-radius: 10px; padding: 20px; color: #fff; }
  .top3-item:nth-child(1) { background: linear-gradient(135deg, #dc2626, #b91c1c); }
  .top3-item:nth-child(2) { background: linear-gradient(135deg, #16a34a, #15803d); }
  .top3-item:nth-child(3) { background: linear-gradient(135deg, #2563eb, #1d4ed8); }
  .top3-item .num { font-size: 2.5rem; font-weight: 900; opacity: 0.3; line-height: 1; }
  .top3-item h3 { font-size: 1rem; font-weight: 700; margin-bottom: 6px; }
  .top3-item p  { font-size: 0.85rem; opacity: 0.9; line-height: 1.5; }

  /* TRIAGE TABLE */
  .triage-table th { font-size: 0.78rem; }
  .triage-table td { font-size: 0.82rem; }
  .status-rescued { color: #16a34a; font-weight: 700; }
  .status-inbox   { color: #2563eb; font-weight: 700; }
  .status-trash   { color: #6b7280; font-style: italic; }

  /* ACCOUNTING TABLE */
  .accounting-table tr.total-row { background: #1e3a5f; color: #fff; font-weight: 800; }
  .accounting-table tr.total-row td { color: #fff; border-bottom: none; }

  /* DIVIDER */
  .divider { height: 1px; background: #e2e8f0; margin: 8px 0 14px; }

  /* NOTE BOX */
  .note-box { background: #fef9c3; border: 1px solid #fde047; border-radius: 8px; padding: 10px 14px; font-size: 0.83rem; color: #713f12; margin-bottom: 12px; }

  a { color: #2563eb; word-break: break-all; }

  @media (max-width: 600px) {
    .header h1 { font-size: 1.4rem; }
    .cal-event { grid-template-columns: 1fr; }
    .pipeline-row { grid-template-columns: 1fr; }
  }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ═══════════════════════════════════════════════════ -->
<!-- SECTION 0: EMAIL TRIAGE QUICK LIST                  -->
<!-- ═══════════════════════════════════════════════════ -->
<div class="section navy">
  <div class="section-title">📋 Email Triage Quick List</div>
  <div class="section-body">
    <table class="triage-table">
      <thead>
        <tr>
          <th style="width:110px">Status</th>
          <th style="width:180px">From</th>
          <th>Subject</th>
          <th style="width:220px">Summary</th>
        </tr>
      </thead>
      <tbody>
        <!-- RESCUED FIRST -->
        <tr>
          <td><span class="status-rescued">✅ RESCUED</span></td>
          <td>Match</td>
          <td>Michael likes you. See if it's mutual.</td>
          <td>Rescued from Trash — protected sender, always keep in inbox.</td>
        </tr>
        <!-- INBOX ROWS -->
        <tr>
          <td><span class="status-inbox">📥 INBOX</span></td>
          <td>The Hustle</td>
          <td>🌽 Roomba meets John Deere</td>
          <td>Weekly business digest. Unread.</td>
        </tr>
        <tr>
          <td><span class="status-inbox">📥 INBOX</span></td>
          <td>Shopify</td>
          <td>25 things to make and sell from home</td>
          <td>Promotional — $1/month offer. Unread.</td>
        </tr>
        <tr>
          <td><span class="status-inbox">📥 INBOX</span></td>
          <td>Old Navy</td>
          <td>FIFTY PERCENT OFF EVERYTHING + $16 Wow Jeans</td>
          <td>Retail promo, today only. Unread.</td>
        </tr>
        <tr>
          <td><span class="status-inbox">📥 INBOX</span></td>
          <td>Quince</td>
          <td>First look: our most-wanted restocks</td>
          <td>Retail restock alert. Unread.</td>
        </tr>
        <tr>
          <td><span class="status-inbox">📥 INBOX</span></td>
          <td>Match</td>
          <td>Louis likes you. See if it's mutual.</td>
          <td>Dating app notification. Unread.</td>
        </tr>
        <tr>
          <td><span class="status-inbox">📥 INBOX</span></td>
          <td>LinkedIn Job Alerts</td>
          <td>Chief Human Resources Officer at Metasys Technologies</td>
          <td>Job alert — CHRO role. Posted 7/24. Unread. (Duplicate alerts received.)</td>
        </tr>
        <tr>
          <td><span class="status-inbox">📥 INBOX</span></td>
          <td>LinkedIn Job Alerts</td>
          <td>Chief Human Resources Officer at Metasys Technologies</td>
          <td>Duplicate job alert — same CHRO role. Unread.</td>
        </tr>
        <tr>
          <td><span class="status-inbox">📥 INBOX</span></td>
          <td>LinkedIn Job Alerts</td>
          <td>Chief Human Resources Officer at Metasys Technologies</td>
          <td>Third duplicate alert — same CHRO role. Unread.</td>
        </tr>
        <tr>
          <td><span class="status-inbox">📥 INBOX</span></td>
          <td>LinkedIn Job Alerts</td>
          <td>Sr Human Resources Director — up to $350K/year</td>
          <td>High-value job alert. Posted 7/23. Unread.</td>
        </tr>
        <tr>
          <td><span class="status-inbox">📥 INBOX</span></td>
          <td>LinkedIn Job Alerts</td>
          <td>Senior Human Resources Business Partner (HRBP) at Axion</td>
          <td>HRBP role alert. Posted 7/24. Unread.</td>
        </tr>
        <tr>
          <td><span class="status-inbox">📥 INBOX</span></td>
          <td>LinkedIn Job Alerts</td>
          <td>Director of People (Remote) at GridUnity</td>
          <td>Remote Director role. Posted 7/23. Read.</td>
        </tr>
        <tr>
          <td><span class="status-inbox">📥 INBOX</span></td>
          <td>David Green via LinkedIn</td>
          <td>Best HR & People Analytics articles of July 2026</td>
          <td>HR/AI thought leadership digest. Read.</td>
        </tr>
        <tr>
          <td><span class="status-inbox">📥 INBOX</span></td>
          <td>Melissa W (self)</td>
          <td>🌌 5 Claude Artifacts That Run Your Entire Business</td>
          <td>Self-sent Notion link — AI tools resource.</td>
        </tr>
        <tr>
          <td><span class="status-inbox">📥 INBOX</span></td>
          <td>Melissa W (self)</td>
          <td>Chief Human Resources Officer | Metasys Technologies | LinkedIn</td>
          <td>Self-sent LinkedIn job link — CHRO role.</td>
        </tr>
        <tr>
          <td><span class="status-inbox">📥 INBOX</span></td>
          <td>Sabrina Ramonov 🍄</td>
          <td>Welcome to Sabrina Ramonov 🍄</td>
          <td>New Substack subscription confirmation. Unread.</td>
        </tr>
        <tr>
          <td><span class="status-inbox">📥 INBOX</span></td>
          <td>Glassdoor Jobs</td>
          <td>Corporate Human Resources Manager at Covercraft + 7 more</td>
          <td>Job digest — remote HR roles. Unread.</td>
        </tr>
        <tr>
          <td><span class="status-inbox">📥 INBOX</span></td>
          <td>Slack</td>
          <td>consulting work's free trial of Slack Pro ends in 7 days</td>
          <td>⚠️ Trial ends Aug 2 — decide to upgrade or downgrade. Read.</td>
        </tr>
        <!-- TRASH SUMMARY ROWS -->
        <tr style="background:#fef9c3;">
          <td><span class="status-trash">🗑 TRASHED (auto)</span></td>
          <td colspan="2"><em>4 emails auto-trashed (newsletters/phishing) — see Trash Review</em></td>
          <td>Includes 1 phishing (iCloud spoof) + 3 newsletters/digests.</td>
        </tr>
        <tr style="background:#f3f4f6;">
          <td><span class="status-trash">🗂 TRASH (manual)</span></td>
          <td colspan="2"><em>29 additional emails in Trash — see Trash Review</em></td>
          <td>Spam, retail promos, dating, job digests, newsletters, adult spam.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════ -->
<!-- SECTION 1: HEADER                                   -->
<!-- ═══════════════════════════════════════════════════ -->
<div class="header">
  <div class="sub">EXECUTIVE BRIEFING</div>
  <h1>Good Morning, Melissa ☀️</h1>
  <div class="sub">Sunday, July 26, 2026 · Prepared by your Executive Chief of Staff</div>
  <div class="meta">
    <div class="meta-item"><span>50</span>Total Emails Reviewed</div>
    <div class="meta-item"><span>10</span>Calendar Events</div>
    <div class="meta-item"><span>5</span>Job Opportunities</div>
    <div class="meta-item"><span>1</span>Interview This Week</div>
    <div class="meta-item"><span>1</span>Security Alert</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════ -->
<!-- SECTION 2: EXECUTIVE SUMMARY                        -->
<!-- ═══════════════════════════════════════════════════ -->
<div class="section navy">
  <div class="section-title">⚡ Executive Summary</div>
  <div class="section-body">
    <div class="exec-summary">
      <div class="exec-bullet risk">
        <div class="icon">🚨</div>
        <h4>Biggest Risk / Urgent</h4>
        <p>A spoofed iCloud phishing email (from a .biz.id domain) impersonating Apple was auto-trashed. Additionally, your Slack Pro free trial for "consulting work" expires <strong>August 2</strong> — decide by next Sunday whether to upgrade or revert to the free tier.</p>
      </div>
      <div class="exec-bullet opp">
        <div class="icon">🎯</div>
        <h4>Biggest Job Search / Opportunity</h4>
        <p>You have a confirmed interview <strong>Tuesday, July 28 at 10:30 AM EDT</strong> with Elliptic for the Head of People – U.S. role (Talent Partner screen with Christopher Ratcliffe). Separately, a Sr. HR Director role at a confidential employer is posted at <strong>up to $350K/year</strong> — high priority to review and apply.</p>
      </div>
      <div class="exec-bullet cal">
        <div class="icon">📅</div>
        <h4>Biggest Calendar / Deadline</h4>
        <p>This week is packed: Elliptic interview Tue 7/28, two professional HR webinars on Wed 7/29 (AI in Talent + Future of Benefits), an HR networking group Wed 7/29 and Thu 7/30, and a Warby Parker auto-pay billing event today. Confirm RSVPs for the two Wed events marked "needsAction."</p>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════ -->
<!-- SECTION 3: ACTION REQUIRED                          -->
<!-- ═══════════════════════════════════════════════════ -->
<div class="section yellow">
  <div class="section-title">🔔 Action Required</div>
  <div class="section-body">

    <div class="card yellow">
      <div class="card-label yellow">⚠️ BILLING / DEADLINE</div>
      <h3>Slack Pro Free Trial Ends in 7 Days</h3>
      <div class="meta-row">
        <span><strong>Source:</strong> Slack &lt;no-reply@slack.com&gt;</span>
        <span><strong>Due:</strong> Sunday, August 2, 2026</span>
      </div>
      <p><strong>Why it matters:</strong> Your "consulting work" Slack workspace loses premium features on Aug 2 if no action is taken. This could affect collaboration tools you're actively using.</p>
      <p><strong>Next step:</strong> Decide whether to upgrade to Slack Pro (paid) or allow the workspace to revert to the free tier. Review feature needs before the deadline.</p>
    </div>

    <div class="card blue">
      <div class="card-label blue">📅 INTERVIEW PREP</div>
      <h3>Interview with Elliptic — Head of People, U.S. (Talent Partner Screen)</h3>
      <div class="meta-row">
        <span><strong>Source:</strong> Google Calendar — Confirmed</span>
        <span><strong>Due:</strong> Tuesday, July 28, 2026 · 10:30–11:00 AM EDT</span>
      </div>
      <p><strong>Why it matters:</strong> This is a confirmed interview with a crypto/blockchain compliance firm. Talent Partner Christopher Ratcliffe (Talentful) is conducting the screen.</p>
      <p><strong>Next step:</strong> Prepare talking points on U.S. HR leadership, people strategy, and scaling teams. Review Elliptic's background in blockchain analytics. Zoom link ready: <a href="https://elliptic-co.zoom.us/j/89752444403?pwd=tNtT8ECe9DIsZ4kIXgmuDZGW8RBCDc.1">Join Meeting</a></p>
    </div>

    <div class="card yellow">
      <div class="card-label yellow">📅 RSVP NEEDED</div>
      <h3>RSVP Pending — Future of Benefits: HR & L&D Roundtable (Wed Jul 29, 12–1 PM)</h3>
      <div class="meta-row">
        <span><strong>Source:</strong> Google Calendar — Status: needsAction</span>
        <span><strong>Due:</strong> Wednesday, July 29, 2026</span>
      </div>
      <p><strong>Why it matters:</strong> Senior HR roundtable featuring CEO of CareCrowd. Relevant to your HR leadership focus. Conflicts with HR Networking Group (same time slot).</p>
      <p><strong>Next step:</strong> Decide which event to prioritize at 12 PM on Wed — the Roundtable or the HR Networking Group. RSVP to whichever you'll attend.</p>
    </div>

    <div class="card yellow">
      <div class="card-label yellow">📅 RSVP NEEDED</div>
      <h3>RSVP Pending — HR Networking & Job Search Group (Wed Jul 29, 12–1:30 PM)</h3>
      <div class="meta-row">
        <span><strong>Source:</strong> Google Calendar — Status: needsAction</span>
        <span><strong>Due:</strong> Wednesday, July 29, 2026</span>
      </div>
      <p><strong>Why it matters:</strong> Large peer networking group for HR job seekers. Conflicts with the Benefits Roundtable at the same time.</p>
      <p><strong>Next step:</strong> Confirm or decline this invite once you've decided between the two 12 PM events on Wednesday.</p>
    </div>

    <div class="card yellow">
      <div class="card-label yellow">📞 TASK — TOMORROW</div>
      <h3>Call St. Francis to Confirm Insurance is Up to Date</h3>
      <div class="meta-row">
        <span><strong>Source:</strong> Google Calendar</span>
        <span><strong>Due:</strong> Monday, July 27, 2026 · 9:00–10:00 AM EDT</span>
      </div>
      <p><strong>Why it matters:</strong> Insurance verification is time-sensitive for medical access.</p>
      <p><strong>Next step:</strong> Call 1-866-367-2901 Monday morning between 9–10 AM.</p>
    </div>

    <div class="card green">
      <div class="card-label green">💼 JOB OPPORTUNITY — HIGH PRIORITY</div>
      <h3>Sr. Human Resources Director — Confidential Employer (Up to $350K/year)</h3>
      <div class="meta-row">
        <span><strong>Source:</strong> LinkedIn Job Alerts</span>
        <span><strong>Posted:</strong> 7/23/2026</span>
      </div>
      <p><strong>Why it matters:</strong> This is a high-compensation senior HR leadership role — at the top of your career target range. The confidential posting may indicate urgency.</p>
      <p><strong>Next step:</strong> Open the LinkedIn alert, review the full JD, and apply or bookmark immediately. Posted 3 days ago — act today.</p>
    </div>

    <div class="card yellow">
      <div class="card-label yellow">💳 BILLING — TODAY</div>
      <h3>Warby Parker Auto-Pay — Processes Today</h3>
      <div class="meta-row">
        <span><strong>Source:</strong> Google Calendar</span>
        <span><strong>Due:</strong> Sunday, July 26, 2026</span>
      </div>
      <p><strong>Why it matters:</strong> Auto-pay is scheduled today. Ensure sufficient funds and that payment info is current (especially given the recent Warby Parker featherweight frames email).</p>
      <p><strong>Next step:</strong> Verify account balance and confirm payment processes successfully.</p>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════ -->
<!-- SECTION 4: FULL 7-DAY CALENDAR                      -->
<!-- ═══════════════════════════════════════════════════ -->
<div class="section blue">
  <div class="section-title">📅 Full 7-Day Calendar (Jul 26 – Aug 1, 2026)</div>
  <div class="section-body">

    <!-- SUNDAY JUL 26 -->
    <div class="cal-day">
      <div class="cal-day-header">Sunday, July 26, 2026 <span class="today-tag">TODAY</span></div>
      <div class="cal-event">
        <div class="cal-time">All Day</div>
        <div class="cal-detail">
          <h4>💳 Warby Parker Auto Pay</h4>
          <p><strong>Status:</strong> <span class="badge badge-green">Confirmed</span></p>
          <p><strong>Prep:</strong> Verify bank account balance. Confirm payment processes correctly.</p>
        </div>
      </div>
    </div>

    <!-- MONDAY JUL 27 -->
    <div class="cal-day">
      <div class="cal-day-header">Monday, July 27, 2026</div>
      <div class="cal-event">
        <div class="cal-time">9:00 AM –<br>10:00 AM EDT</div>
        <div class="cal-detail">
          <h4>📞 Call St. Francis — Confirm Insurance is Up to Date</h4>
          <p><strong>Status:</strong> <span class="badge badge-green">Confirmed</span></p>
          <p><strong>Phone:</strong> 1-866-367-2901</p>
          <p><strong>Prep:</strong> Have your insurance card and member ID ready. Know which plan you're verifying (provider + coverage year).</p>
        </div>
      </div>
    </div>

    <!-- TUESDAY JUL 28 -->
    <div class="cal-day">
      <div class="cal-day-header">Tuesday, July 28, 2026</div>
      <div class="cal-event">
        <div class="cal-time">10:30 AM –<br>11:00 AM EDT</div>
        <div class="cal-detail">
          <h4>🎯 Interview with Elliptic — Head of People, U.S. (Talent Partner Screen)</h4>
          <p><strong>Status:</strong> <span class="badge badge-green">Accepted ✓</span></p>
          <p><strong>Interviewer:</strong> Christopher Ratcliffe (Talentful Talent Lead)</p>
          <p><strong>Zoom:</strong> <a href="https://elliptic-co.zoom.us/j/89752444403?pwd=tNtT8ECe9DIsZ4kIXgmuDZGW8RBCDc.1">Join Meeting</a> · Meeting ID: 89752444403 · Desktop Passcode: %gG9*sA2fV · Phone: 1168138618</p>
          <p><strong>Prep:</strong> Research Elliptic (blockchain analytics/compliance). Prepare STAR stories for HR leadership, people strategy, and U.S. org builds. Review your LinkedIn. Test Zoom 10 min early.</p>
          <p><strong>Note:</strong> Two calendar entries exist for this event (one with location in description field, one with proper Zoom link). Both confirmed — no conflict.</p>
        </div>
      </div>
    </div>

    <!-- WEDNESDAY JUL 29 -->
    <div class="cal-day">
      <div class="cal-day-header">Wednesday, July 29, 2026</div>

      <div class="cal-event">
        <div class="cal-time">11:00 AM –<br>12:00 PM EDT</div>
        <div class="cal-detail">
          <h4>🤖 How A VP Talent Builds with AI — PromptMates Live</h4>
          <p><strong>Status:</strong> <span class="badge badge-green">Accepted ✓</span></p>
          <p><strong>Join:</strong> <a href="https://luma.com/join/g-sAv9NHMvqDBBXrx">Luma Link</a></p>
          <p><strong>Topic:</strong> Free webinar for HR/Recruitment professionals on AI, automation & new technology. Featuring Emily Gransky (VP Talent).</p>
          <p><strong>Prep:</strong> Bring questions on AI tools for talent acquisition. Good follow-up to Elliptic interview.</p>
        </div>
      </div>

      <div class="cal-event conflict">
        <div class="cal-time">12:00 PM –<br>1:00 PM EDT<br>⚠️ CONFLICT</div>
        <div class="cal-detail">
          <h4>🏥 Future of Benefits: Why Healthcare Alone Isn't Enough — HIC HR & L&D Roundtable</h4>
          <p><strong>Status:</strong> <span class="badge badge-yellow">⚠️ RSVP Needed</span></p>
          <p><strong>Zoom:</strong> <a href="https://us06web.zoom.us/j/5224221004?pwd=UU5YNmlFckpjQnlzc2FDMHFlNUhhUT09">Join Meeting</a></p>
          <p><strong>Topic:</strong> Senior HR roundtable with CEO of CareCrowd on benefits strategy beyond healthcare.</p>
          <p><strong>⚠️ CONFLICT:</strong> This event runs 12–1 PM, directly overlapping with the HR Networking Group below. Choose one.</p>
        </div>
      </div>

      <div class="cal-event conflict">
        <div class="cal-time">12:00 PM –<br>1:30 PM EDT<br>⚠️ CONFLICT</div>
        <div class="cal-detail">
          <h4>🤝 HR Networking & Job Search Group — Zoom 2</h4>
          <p><strong>Status:</strong> <span class="badge badge-yellow">⚠️ RSVP Needed</span></p>
          <p><strong>Zoom:</strong> <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1">Join Meeting</a></p>
          <p><strong>Attendees:</strong> ~170 HR professionals in the group.</p>
          <p><strong>⚠️ CONFLICT:</strong> Overlaps with Benefits Roundtable (12–1 PM). Runs 30 min longer. Choose one.</p>
          <p><strong>Prep:</strong> Prepare 30-second elevator pitch on job search status if attending.</p>
        </div>
      </div>

      <div class="cal-event">
        <div class="cal-time">12:00 PM –<br>1:30 PM EDT</div>
        <div class="cal-detail">
          <h4>🤝 Network (Personal Reminder)</h4>
          <p><strong>Status:</strong> <span class="badge badge-green">Confirmed</span></p>
          <p><strong>Note:</strong> Personal blocking event for networking time — aligned with the HR Networking Group above.</p>
        </div>
      </div>
    </div>

    <!-- THURSDAY JUL 30 -->
    <div class="cal-day">
      <div class="cal-day-header">Thursday, July 30, 2026</div>

      <div class="cal-event declined">
        <div class="cal-time">9:00 AM –<br>10:30 AM EDT<br>DECLINED</div>
        <div class="cal-detail">
          <h4>❌ Executive Roundtable (Declined)</h4>
          <p><strong>Status:</strong> <span class="badge badge-gray">Declined</span></p>
          <p><strong>Host:</strong> John Madigan</p>
          <p><strong>Zoom:</strong> <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09">Join Meeting</a> · ID: 207 786 667 · PW: 205454</p>
          <p><strong>Note:</strong> You have declined this event. No action needed unless you wish to re-engage.</p>
        </div>
      </div>

      <div class="cal-event pending">
        <div class="cal-time">12:00 PM –<br>1:00 PM EDT</div>
        <div class="cal-detail">
          <h4>🤝 HR Networking & Job Search: Open Office Hours — Zoom 2</h4>
          <p><strong>Status:</strong> <span class="badge badge-yellow">⚠️ RSVP Needed</span></p>
          <p><strong>Zoom:</strong> <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1">Join Meeting</a></p>
          <p><strong>Note:</strong> No recording or AI notetaking per organizer request. Open discussion format.</p>
          <p><strong>Prep:</strong> Good opportunity to debrief post-Elliptic interview with peers. RSVP if attending.</p>
        </div>
      </div>
    </div>

    <!-- FRIDAY JUL 31 – SAT AUG 1 -->
    <div class="cal-day">
      <div class="cal-day-header">Friday, July 31 – Saturday, August 1, 2026</div>
      <div class="card gray" style="margin-top:8px;">
        <p style="font-size:0.85rem;color:#666;">No calendar events scheduled for these days.</p>
      </div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════ -->
<!-- SECTION 5: JOB SEARCH & INTERVIEW PIPELINE          -->
<!-- ═══════════════════════════════════════════════════ -->
<div class="section green">
  <div class="section-title">💼 Job Search & Interview Pipeline</div>
  <div class="section-body">

    <div class="card green">
      <div class="card-label green">🔥 ACTIVE INTERVIEW</div>
      <h3>Elliptic — Head of People, U.S.</h3>
      <div class="meta-row">
        <span><strong>Stage:</strong> Talent Partner Screen</span>
        <span><strong>Date:</strong> Tue Jul 28, 10:30–11:00 AM EDT</span>
        <span><strong>Fit:</strong> <span class="badge badge-green">HIGH</span></span>
      </div>
      <p><strong>Interviewer:</strong> Christopher Ratcliffe, Talentful (LinkedIn-embedded recruiter)</p>
      <p><strong>Type:</strong> Blockchain analytics / compliance tech. U.S. HR leadership build.</p>
      <p><strong>Action:</strong> Prep today. Review Elliptic's product, funding, and team size. Zoom link confirmed.</p>
    </div>

    <div class="card green">
      <div class="card-label green">💰 HIGH COMPENSATION ALERT</div>
      <h3>Sr. Human Resources Director — Confidential Employer (Up to $350K/year)</h3>
      <div class="meta-row">
        <span><strong>Source:</strong> LinkedIn Job Alerts</span>
        <span><strong>Posted:</strong> 7/23/2026</span>
        <span><strong>Fit:</strong> <span class="badge badge-green">HIGH</span></span>
      </div>
      <p><strong>Action:</strong> Review full JD and apply today — posted 3 days ago. Confidential employer suggests urgency or sensitivity.</p>
    </div>

    <div class="card green">
      <div class="card-label green">💼 JOB ALERT — REVIEW</div>
      <h3>Chief Human Resources Officer — Metasys Technologies</h3>
      <div class="meta-row">
        <span><strong>Source:</strong> LinkedIn Job Alerts (3 duplicate alerts) + self-sent LinkedIn link</span>
        <span><strong>Posted:</strong> 7/24/2026</span>
        <span><strong>Fit:</strong> <span class="badge badge-green">HIGH</span></span>
      </div>
      <p><strong>Note:</strong> You received 3 duplicate LinkedIn alerts AND self-sent yourself the LinkedIn job URL — suggesting high interest. You also have a saved Notion link referencing this role.</p>
      <p><strong>Action:</strong> Review the JD if not yet done. Apply or follow up. Suppress duplicate LinkedIn alerts for this role.</p>
    </div>

    <div class="card teal">
      <div class="card-label teal">💼 JOB ALERT — REVIEW</div>
      <h3>Senior HR Business Partner (HRBP) — Axion</h3>
      <div class="meta-row">
        <span><strong>Source:</strong> LinkedIn Job Alerts</span>
        <span><strong>Posted:</strong> 7/24/2026</span>
        <span><strong>Fit:</strong> <span class="badge badge-teal">MEDIUM</span></span>
      </div>
      <p><strong>Action:</strong> Review role — HRBP may be a step below your CHRO/Director target level. Worth scanning if Axion is a strong employer.</p>
    </div>

    <div class="card teal">
      <div class="card-label teal">💼 JOB ALERT — REVIEW</div>
      <h3>Director of People (Remote) — GridUnity</h3>
      <div class="meta-row">
        <span><strong>Source:</strong> LinkedIn Job Alerts</span>
        <span><strong>Posted:</strong> 7/23/2026</span>
        <span><strong>Fit:</strong> <span class="badge badge-teal">MEDIUM</span></span>
      </div>
      <p><strong>Action:</strong> Remote Director of People role — good fit for level and flexibility. Review JD. Posted 3 days ago.</p>
    </div>

    <div class="card teal">
      <div class="card-label teal">📋 JOB DIGEST — REVIEW</div>
      <h3>Glassdoor — Corporate HR Manager at Covercraft + 7 More Remote Roles</h3>
      <div class="meta-row">
        <span><strong>Source:</strong> Glassdoor Jobs</span>
        <span><strong>Fit:</strong> <span class="badge badge-gray">VARIES</span></span>
      </div>
      <p><strong>Action:</strong> Scan for any Director+ level roles within the digest. HR Manager at Covercraft may be below target level.</p>
    </div>

    <div class="card gray">
      <div class="card-label gray">📋 JOB DIGEST — LOW PRIORITY</div>
      <h3>Glassdoor — Assistant Community Manager at Vinyl Real Estate + 5 More (New York, NY)</h3>
      <div class="meta-row">
        <span><strong>Source:</strong> Glassdoor Jobs</span>
        <span><strong>Fit:</strong> <span class="badge badge-gray">LOW</span></span>
      </div>
      <p><strong>Action:</strong> Likely not aligned with HR Director/CHRO target. Skip or skim.</p>
    </div>

    <div class="card purple">
      <div class="card-label purple">🤝 NETWORKING EVENT — THIS WEEK</div>
      <h3>HR Networking & Job Search Group — Wed Jul 29 (12–1:30 PM) + Thu Jul 30 (12–1 PM)</h3>
      <div class="meta-row">
        <span><strong>Source:</strong> Google Calendar</span>
        <span><strong>Attendees:</strong> ~170 HR professionals</span>
      </div>
      <p><strong>Action:</strong> RSVP. Excellent peer network for job leads, referrals, and market intelligence. Prepare your job search status update.</p>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════ -->
<!-- SECTION 6: FULL EMAIL REVIEW BY CATEGORY            -->
<!-- ═══════════════════════════════════════════════════ -->
<div class="section navy">
  <div class="section-title">📂 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="card red" style="margin-bottom:16px;">
      <div class="card-label red">🔴 SECURITY / RISK — 5 EMAILS</div>
      <h3>Security & Spam Threats</h3>
      <table style="margin-top:10px;">
        <thead><tr><th>Email</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td><strong>melissaw212 &lt;…@storagedomain.biz.id&gt;</strong><br><em>"We have blocked your account 🚫 Your photos will be deleted…"</em></td>
            <td><span class="badge badge-red">AUTO-TRASHED — Phishing</span></td>
            <td>Spoofed iCloud threat email from random .biz.id domain. Harvesting payment info. Already removed. No action needed.</td>
          </tr>
          <tr>
            <td><strong>"Hot Sex🔥🔥" &lt;…@ssd6lq.bjzrcx.l0ohso.us&gt;</strong><br><em>"Make her squirt 3x tonight with this porn star secret"</em></td>
            <td><span class="badge badge-red">Spam — Not in Inbox</span></td>
            <td>Adult spam from random .us domain. Delete permanently.</td>
          </tr>
          <tr>
            <td><strong>"Hot Sex" &lt;bisupportie@sysgnloymzvaxoxefxgpqnzk.com&gt;</strong><br><em>"Naughty porn star reveals secret to staying hard for hours"</em></td>
            <td><span class="badge badge-red">Spam — Not in Inbox</span></td>
            <td>Adult spam from gibberish domain. Delete permanently.</td>
          </tr>
          <tr>
            <td><strong>"'Sex Trick🍆'" &lt;wzvysupportkyt@isagekbwtubyvnhvetmokgou.com&gt;</strong><br><em>"The safest 'before sex' trick you've never tried"</em></td>
            <td><span class="badge badge-red">Spam — Not in Inbox</span></td>
            <td>Adult spam with Epstein-files lure. Gibberish domain. Delete permanently.</td>
          </tr>
          <tr>
            <td><strong>"Hot Sex🔥🔥" &lt;…@244gs7.r7957j.is686y.us&gt;</strong><br><em>"Make her squirt 3x tonight with this porn star secret"</em></td>
            <td><span class="badge badge-red">Spam — Not in Inbox</span></td>
            <td>Duplicate adult spam. Random .us domain. Delete permanently.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- JOB SEARCH -->
    <div class="card green" style="margin-bottom:16px;">
      <div class="card-label green">🟢 JOB SEARCH — 10 EMAILS</div>
      <h3>Job Alerts, Applications & Self-Research</h3>
      <table style="margin-top:10px;">
        <thead><tr><th>Email</th><th>Key Detail</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>LinkedIn — CHRO at Metasys Technologies (×3 alerts, 3 different times)</td><td>Posted 7/24. High fit. Self-sent LinkedIn link also received.</td><td>Apply / Review. Suppress duplicate alerts.</td></tr>
          <tr><td>LinkedIn — Sr. HR Director at Confidential (up to $350K/year)</td><td>Posted 7/23. Very high compensation. 1 alert.</td><td>Apply immediately.</td></tr>
          <tr><td>LinkedIn — HRBP at Axion</td><td>Posted 7/24. Medium fit.</td><td>Review JD.</td></tr>
          <tr><td>LinkedIn — Director of People (Remote) at GridUnity</td><td>Posted 7/23. Medium fit.</td><td>Review JD.</td></tr>
          <tr><td>Melissa W (self-sent) — CHRO Metasys LinkedIn link</td><td>Self-research note.</td><td>Open and review link.</td></tr>
          <tr><td>Melissa W (self-sent) — 5 Claude Artifacts That Run Your Entire Business (Notion)</td><td>AI tools resource for business efficiency.</td><td>Read and implement.</td></tr>
          <tr><td>Dennis Gorelik / PostJobFree — Patient Technology Project Lead at CHOP (in Trash)</td><td>Academy Gardens, PA. Not aligned with HR Director target.</td><td>Keep in Trash / Ignore.</td></tr>
          <tr><td>Glassdoor Jobs — Corporate HR Manager at Covercraft + 7 Remote Roles</td><td>HR digest. Varies in level.</td><td>Skim for Director+ roles.</td></tr>
          <tr><td>Glassdoor Jobs — Asst. Community Manager at Vinyl Real Estate + 5 NYC Roles</td><td>Likely below target level.</td><td>Skip.</td></tr>
        </tbody>
      </table>
    </div>

    <!-- RECRUITERS / NETWORKING -->
    <div class="card teal" style="margin-bottom:16px;">
      <div class="card-label teal">🩵 RECRUITERS / NETWORKING — 2 EMAILS</div>
      <h3>Recruiter & Network-Adjacent Emails</h3>
      <table style="margin-top:10px;">
        <thead><tr><th>Email</th><th>Detail</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Glassdoor — "Glassdoor is now part of Indeed" (×2 near-duplicate emails)</td><td>Platform announcement. Two versions sent within 1 min. One read, one unread.</td><td>Note the change. Update job search source to Indeed if needed. Delete duplicate.</td></tr>
        </tbody>
      </table>
    </div>

    <!-- CALENDAR / EVENTS -->
    <div class="card blue" style="margin-bottom:16px;">
      <div class="card-label blue">🔵 CALENDAR / EVENTS — 1 EMAIL (+ handled via Calendar)</div>
      <h3>Event Invitations (reflected in calendar section above)</h3>
      <table style="margin-top:10px;">
        <thead><tr><th>Email</th><th>Detail</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Slack — "consulting work's free trial of Slack Pro ends in 7 days"</td><td>Trial ends Aug 2. Read. Not in inbox.</td><td>Decide on upgrade by Aug 2. See Action Required above.</td></tr>
        </tbody>
      </table>
    </div>

    <!-- MEDICAL / HEALTH -->
    <div class="card orange" style="margin-bottom:16px;">
      <div class="card-label orange">🟠 MEDICAL / HEALTH — 1 EMAIL</div>
      <h3>Health-Related Emails</h3>
      <table style="margin-top:10px;">
        <thead><tr><th>Email</th><th>Detail</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>GLP-1 by AbundRX (×2 — both in Trash, from .biz domains)</td><td>Weight loss medication spam from sketchy .biz domains. Sent at different times.</td><td>Both already in Trash. Delete permanently. Unsubscribe if opt-in was accidental.</td></tr>
        </tbody>
      </table>
      <p style="font-size:0.82rem;color:#666;margin-top:8px;">Note: The GLP-1 emails are counted here for categorization but both are in Trash.</p>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="card yellow" style="margin-bottom:16px;">
      <div class="card-label yellow">🟡 FINANCIAL / BILLING — 2 EMAILS</div>
      <h3>Financial & Credit Emails</h3>
      <table style="margin-top:10px;">
        <thead><tr><th>Email</th><th>Detail</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Equifax — "What's in Your Credit Report?" (in Trash)</td><td>Legitimate Equifax email. In Trash.</td><td>Consider reviewing your credit report. Restore from Trash if desired.</td></tr>
          <tr><td>Dylan's Diary Newsletter — "Gold Gap – Golden Opportunity in Miners?" (in Trash)</td><td>BofA: "Best valuations in 20 years" for gold miners. Finance newsletter. In Trash.</td><td>In Trash. If interested in investing content, move to inbox; otherwise delete.</td></tr>
        </tbody>
      </table>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="card purple" style="margin-bottom:16px;">
      <div class="card-label purple">🟣 PROFESSIONAL DEVELOPMENT — 5 EMAILS</div>
      <h3>Learning, Thought Leadership & HR Content</h3>
      <table style="margin-top:10px;">
        <thead><tr><th>Email</th><th>Detail</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>David Green via LinkedIn — "Best HR & People Analytics Articles of July 2026"</td><td>HR must guide enterprise through AI transformation. Read. In inbox.</td><td>Review — highly relevant to your HR leadership positioning.</td></tr>
          <tr><td>Sabrina Ramonov 🍄 (Substack) — Welcome email</td><td>New subscription to AI/creator-focused newsletter. In inbox. Unread.</td><td>Confirm subscription is intentional. Read first issue.</td></tr>
          <tr><td>Gemma Bonham-Carter — "Draft Week kicks off tomorrow!!" (in Trash)</td><td>Online course/challenge starting soon. In Trash.</td><td>Restore if you enrolled intentionally in Draft Week.</td></tr>
          <tr><td>AI with Mariah — "How I run 2 businesses with AI agents 🫡" (in Trash)</td><td>AI challenge email. Already trashed.</td><td>Keep in Trash unless you want to join the challenge.</td></tr>
          <tr><td>Alison Courses — "Learn career-transforming skills" (in Trash, newsletter_trashed)</td><td>Auto-trashed newsletter. Generic course promo.</td><td>Auto-Trashed — Newsletter. No action needed.</td></tr>
        </tbody>
      </table>
    </div>

    <!-- PERSONAL -->
    <div class="card gray" style="margin-bottom:16px;">
      <div class="card-label gray">⚪ PERSONAL — 7 EMAILS</div>
      <h3>Dating Apps, Personal Subscriptions & Personal Notifications</h3>
      <table style="margin-top:10px;">
        <thead><tr><th>Email</th><th>Detail</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Match — "Louis likes you" (inbox, unread)</td><td>New match notification.</td><td>Check when ready.</td></tr>
          <tr><td>Match — "You've had a profile view from John, 57, Narrowsburg NY" (not inbox, unread)</td><td>Profile view.</td><td>Check when ready.</td></tr>
          <tr><td>Match — "Michael likes you" (RESCUED from Trash, unread)</td><td>Rescued — protected sender.</td><td>Check when ready.</td></tr>
          <tr><td>Match — "Michael likes you" (not inbox, read — earlier duplicate)</td><td>Read, not in inbox.</td><td>No action needed.</td></tr>
          <tr><td>Match — "Ethan likes you" (not inbox, unread)</td><td>Match notification.</td><td>Check when ready.</td></tr>
          <tr><td>Match — "You've had a profile view from Scott, 62, Poughkeepsie NY" (not inbox, read)</td><td>Profile view. Read.</td><td>No action needed.</td></tr>
          <tr><td>J
