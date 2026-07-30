<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa A. Weiss, MPA — July 30, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a2340 0%, #2d3f6b 100%); color: white; border-radius: 12px; padding: 28px 32px; margin-bottom: 24px; }
  .header h1 { font-size: 26px; font-weight: 700; letter-spacing: -0.5px; }
  .header .subtitle { font-size: 14px; opacity: 0.8; margin-top: 4px; }
  .header .meta { display: flex; gap: 24px; margin-top: 14px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.12); border-radius: 8px; padding: 8px 16px; font-size: 13px; }
  .header .meta-item span { font-weight: 700; font-size: 18px; display: block; }

  /* SECTION HEADERS */
  .section-title { font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin: 28px 0 12px 0; padding-bottom: 6px; border-bottom: 2px solid #dde1ea; color: #1a2340; display: flex; align-items: center; gap: 8px; }
  .section-title .icon { font-size: 18px; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; border-left: 5px solid #ccc; background: white; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }
  .card.red { border-left-color: #e53935; background: #fff8f8; }
  .card.yellow { border-left-color: #f9a825; background: #fffdf0; }
  .card.blue { border-left-color: #1e88e5; background: #f5f9ff; }
  .card.green { border-left-color: #2e7d32; background: #f4faf4; }
  .card.purple { border-left-color: #6a1b9a; background: #faf5ff; }
  .card.gray { border-left-color: #9e9e9e; background: #fafafa; }
  .card.orange { border-left-color: #e65100; background: #fff8f3; }

  .card-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; }
  .card-label.red { color: #e53935; }
  .card-label.yellow { color: #f9a825; }
  .card-label.blue { color: #1e88e5; }
  .card-label.green { color: #2e7d32; }
  .card-label.purple { color: #6a1b9a; }
  .card-label.gray { color: #757575; }
  .card-label.orange { color: #e65100; }

  .card h3 { font-size: 14px; font-weight: 700; margin-bottom: 4px; color: #1a2340; }
  .card .from { font-size: 12px; color: #666; margin-bottom: 6px; }
  .card p { font-size: 13px; color: #444; margin-bottom: 4px; }
  .card .action { font-size: 13px; font-weight: 600; margin-top: 8px; }
  .card .action.red { color: #c62828; }
  .card .action.yellow { color: #f57f17; }
  .card .action.green { color: #2e7d32; }
  .card .action.blue { color: #1565c0; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,0.07); margin-bottom: 16px; }
  th { background: #1a2340; color: white; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px; padding: 10px 14px; text-align: left; }
  td { padding: 9px 14px; border-bottom: 1px solid #eef0f4; font-size: 13px; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #f7f8fb; }
  tr:hover td { background: #eef2ff; }

  /* PRIORITY BADGES */
  .badge { display: inline-block; border-radius: 4px; padding: 2px 8px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
  .badge.high { background: #ffebee; color: #c62828; }
  .badge.medium { background: #fff8e1; color: #f57f17; }
  .badge.low { background: #f1f8e9; color: #33691e; }
  .badge.rescued { background: #e8f5e9; color: #1b5e20; }
  .badge.inbox { background: #e3f2fd; color: #0d47a1; }
  .badge.trashed { background: #fce4ec; color: #880e4f; }
  .badge.archived { background: #f3e5f5; color: #4a148c; }
  .badge.fit-high { background: #e8f5e9; color: #1b5e20; }
  .badge.fit-med { background: #fff8e1; color: #e65100; }
  .badge.fit-low { background: #fafafa; color: #757575; }

  /* STATUS ICONS */
  .status-confirmed { color: #2e7d32; font-weight: 700; }
  .status-declined { color: #c62828; font-weight: 700; }
  .status-pending { color: #f57f17; font-weight: 700; }

  /* EXEC SUMMARY BULLETS */
  .exec-bullets { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 0; }
  .exec-bullet { flex: 1; min-width: 280px; border-radius: 10px; padding: 14px 18px; border-left: 5px solid; }
  .exec-bullet.risk { border-color: #e53935; background: #fff8f8; }
  .exec-bullet.opp { border-color: #2e7d32; background: #f4faf4; }
  .exec-bullet.cal { border-color: #1e88e5; background: #f5f9ff; }
  .exec-bullet .bul-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; }
  .exec-bullet.risk .bul-label { color: #e53935; }
  .exec-bullet.opp .bul-label { color: #2e7d32; }
  .exec-bullet.cal .bul-label { color: #1e88e5; }
  .exec-bullet p { font-size: 13px; color: #333; }

  /* DASHBOARD */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; margin-bottom: 16px; }
  .dash-tile { background: white; border-radius: 10px; padding: 14px 18px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); border-top: 4px solid; }
  .dash-tile.red { border-top-color: #e53935; }
  .dash-tile.yellow { border-top-color: #f9a825; }
  .dash-tile.blue { border-top-color: #1e88e5; }
  .dash-tile.green { border-top-color: #2e7d32; }
  .dash-tile.purple { border-top-color: #6a1b9a; }
  .dash-tile.gray { border-top-color: #9e9e9e; }
  .dash-tile .tile-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; color: #888; margin-bottom: 6px; }
  .dash-tile .tile-value { font-size: 26px; font-weight: 800; color: #1a2340; }
  .dash-tile .tile-sub { font-size: 12px; color: #666; margin-top: 4px; }

  /* TRIAGE TABLE special coloring */
  .triage-rescued td { background: #f0fff4 !important; }
  .triage-inbox td { background: #f5f9ff !important; }
  .triage-trash td { background: #fafafa !important; }

  /* CALENDAR DAY */
  .cal-day { font-weight: 700; font-size: 13px; color: #1a2340; background: #e8ecf7; padding: 6px 14px; border-radius: 6px; margin: 10px 0 6px 0; }
  .cal-today { background: #1e88e5; color: white; }

  /* TOP 3 */
  .top3 { display: flex; gap: 12px; flex-wrap: wrap; }
  .top3-item { flex: 1; min-width: 260px; background: white; border-radius: 10px; padding: 18px 20px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); border-top: 5px solid #1e88e5; }
  .top3-item .num { font-size: 32px; font-weight: 900; color: #1e88e5; opacity: 0.25; line-height: 1; }
  .top3-item h4 { font-size: 14px; font-weight: 700; color: #1a2340; margin-top: -10px; }
  .top3-item p { font-size: 13px; color: #555; margin-top: 6px; }

  /* MISC */
  .note { font-size: 12px; color: #888; font-style: italic; margin-top: 8px; }
  .divider { border: none; border-top: 1px solid #e0e4ed; margin: 20px 0; }
  .tag { display: inline-block; background: #eef2ff; color: #3949ab; border-radius: 4px; padding: 1px 7px; font-size: 11px; font-weight: 600; margin-right: 4px; }
  .tag.red { background: #ffebee; color: #c62828; }
  .tag.green { background: #e8f5e9; color: #2e7d32; }
  .tag.yellow { background: #fff8e1; color: #e65100; }
  .warn { color: #e53935; font-weight: 700; font-size: 12px; }
  .rescued-note { font-size: 11px; background: #e8f5e9; color: #1b5e20; border-radius: 4px; padding: 2px 8px; font-weight: 600; display: inline-block; margin-left: 6px; }
  .auto-trash-note { font-size: 11px; background: #ffebee; color: #c62828; border-radius: 4px; padding: 2px 8px; font-weight: 600; display: inline-block; margin-left: 6px; }
</style>
</head>
<body>
<div class="page">

<!-- ============================================================ -->
<!-- SECTION 0: EMAIL TRIAGE QUICK LIST -->
<!-- ============================================================ -->
<div class="section-title"><span class="icon">⚡</span> Email Triage Quick List</div>
<table>
  <thead>
    <tr>
      <th style="width:120px">Status</th>
      <th style="width:200px">From</th>
      <th>Subject</th>
      <th style="width:280px">Summary</th>
    </tr>
  </thead>
  <tbody>
    <!-- RESCUED -->
    <tr class="triage-rescued">
      <td><span class="badge rescued">✅ RESCUED</span></td>
      <td>LinkedIn Job Alerts</td>
      <td>Head of People and Talent at Bluemercury</td>
      <td>Protected sender — kept in inbox. Posted 7/28. Review ASAP.</td>
    </tr>
    <!-- INBOX EMAILS (individual) -->
    <tr class="triage-inbox">
      <td><span class="badge inbox">📥 INBOX</span></td>
      <td>Bank of America</td>
      <td>A direct deposit was credited to your account ($582.09)</td>
      <td>$582.09 direct deposit — USDC/gov payment. Received 7/30.</td>
    </tr>
    <tr class="triage-inbox">
      <td><span class="badge inbox">📥 INBOX</span></td>
      <td>Bank of America</td>
      <td>A direct deposit was credited to your account ($3,200.00)</td>
      <td>$3,200 deposit from Goldman Sachs Bank. Received 7/29.</td>
    </tr>
    <tr class="triage-inbox">
      <td><span class="badge inbox">📥 INBOX</span></td>
      <td>Robert T. Sicora, EdD via LinkedIn</td>
      <td>Robert T. just messaged you</td>
      <td>Unread LinkedIn message awaiting your response.</td>
    </tr>
    <tr class="triage-inbox">
      <td><span class="badge inbox">📥 INBOX</span></td>
      <td>Indeed</td>
      <td>Senior VP Human Resources @ Highgate Hotels</td>
      <td>$270K–$320K role in NYC. Strong match per Indeed.</td>
    </tr>
    <tr class="triage-inbox">
      <td><span class="badge inbox">📥 INBOX</span></td>
      <td>LinkedIn Job Alerts</td>
      <td>Head of People and Talent at Bluemercury (2nd alert)</td>
      <td>Duplicate alert — posted 7/28. Review and apply.</td>
    </tr>
    <tr class="triage-inbox">
      <td><span class="badge inbox">📥 INBOX</span></td>
      <td>LinkedIn Job Alerts</td>
      <td>Head of People and Talent at Bluemercury (3rd alert)</td>
      <td>Third alert for same role. Deduplicate.</td>
    </tr>
    <tr class="triage-inbox">
      <td><span class="badge inbox">📥 INBOX</span></td>
      <td>LinkedIn Job Alerts</td>
      <td>Chief Human Resources Officer at Edged</td>
      <td>CHRO role, posted 7/28. Review for fit.</td>
    </tr>
    <tr class="triage-inbox">
      <td><span class="badge inbox">📥 INBOX</span></td>
      <td>Rana Saini via LinkedIn</td>
      <td>Rana just messaged you</td>
      <td>Unread LinkedIn message awaiting response.</td>
    </tr>
    <tr class="triage-inbox">
      <td><span class="badge inbox">📥 INBOX</span></td>
      <td>Melissa W (self)</td>
      <td>AI Interview Prep: How To Answer All 3 | Learn AI With Mariah</td>
      <td>Self-forwarded resource on AI interview prep.</td>
    </tr>
    <tr class="triage-inbox">
      <td><span class="badge inbox">📥 INBOX</span></td>
      <td>Melissa W (self)</td>
      <td>5 AI Design Skills That Give Claude Real Taste</td>
      <td>Self-forwarded AI design skills guide.</td>
    </tr>
    <tr class="triage-inbox">
      <td><span class="badge inbox">📥 INBOX</span></td>
      <td>Glassdoor Jobs</td>
      <td>Community Manager at Vinyl Real Estate + 4 more jobs (NYC)</td>
      <td>5 roles in NYC including Citizens Bank listing.</td>
    </tr>
    <tr class="triage-inbox">
      <td><span class="badge inbox">📥 INBOX</span></td>
      <td>22 Words</td>
      <td>Your Amazon Lightning Deals ⚡ (Jul 30)</td>
      <td>Amazon deals newsletter in inbox — low priority.</td>
    </tr>
    <tr class="triage-inbox">
      <td><span class="badge inbox">📥 INBOX</span></td>
      <td>Hinge Team</td>
      <td>Eli &amp; Melissa, we recommend you to each other.</td>
      <td>New Hinge match recommendation.</td>
    </tr>
    <!-- AUTO-TRASHED SUMMARY ROW -->
    <tr class="triage-trash">
      <td><span class="badge trashed">🗑 TRASHED (auto)</span></td>
      <td colspan="2">3 emails auto-trashed (phishing/scam) — see Trash Review &amp; Security section</td>
      <td>Hilton Financial LOAN scam, account lockout phishing, Slots of Vegas casino spam</td>
    </tr>
    <!-- MANUAL TRASH SUMMARY ROW -->
    <tr class="triage-trash">
      <td><span class="badge archived">🗂 TRASH (manual)</span></td>
      <td colspan="2">22 emails in Trash — see Trash Review section</td>
      <td>Newsletters, marketing, digests, job alerts, adult spam — review before permanent delete</td>
    </tr>
  </tbody>
</table>

<!-- ============================================================ -->
<!-- SECTION 1: HEADER -->
<!-- ============================================================ -->
<div class="header">
  <h1>Good morning, Melissa 👋</h1>
  <div class="subtitle">Executive Briefing — Prepared by your Chief of Staff</div>
  <div class="meta">
    <div class="meta-item"><span>Thursday</span>July 30, 2026</div>
    <div class="meta-item"><span>50</span>Emails Reviewed</div>
    <div class="meta-item"><span>7</span>Calendar Events</div>
    <div class="meta-item"><span>2</span>Urgent Actions</div>
    <div class="meta-item"><span>5+</span>Open Job Leads</div>
  </div>
</div>

<!-- ============================================================ -->
<!-- SECTION 2: EXECUTIVE SUMMARY -->
<!-- ============================================================ -->
<div class="section-title"><span class="icon">📋</span> Executive Summary</div>
<div class="exec-bullets">
  <div class="exec-bullet risk">
    <div class="bul-label">🔴 Biggest Risk / Urgent</div>
    <p>3 phishing/scam emails were auto-trashed (a fake loan company, an account-lockout credential-harvesting attempt, and casino spam). Additionally, multiple explicit spam and adult-content emails landed in your inbox and folders — your spam filters need strengthening immediately.</p>
  </div>
  <div class="exec-bullet opp">
    <div class="bul-label">🟢 Biggest Opportunity</div>
    <p>A Senior VP of Human Resources role at Highgate Hotels (NYC, $270K–$320K) matched by Indeed, plus two unread LinkedIn messages from Robert T. Sicora, EdD and Rana Saini — respond today to keep momentum. The Head of People &amp; Talent at Bluemercury was alerted 3 times and rescued from Trash — review now.</p>
  </div>
  <div class="exec-bullet cal">
    <div class="bul-label">🔵 Biggest Calendar / Deadline</div>
    <p>Today's HR Networking &amp; Job Search Open Office Hours (12–1 PM, Zoom) has no RSVP yet — confirm attendance. Slack Pro trial ends August 1st (3 days). Medium membership expires August 20th. Eye doctor appointment on Saturday Aug 1.</p>
  </div>
</div>

<!-- ============================================================ -->
<!-- SECTION 3: ACTION REQUIRED -->
<!-- ============================================================ -->
<div class="section-title"><span class="icon">🚨</span> Action Required</div>

<div class="card red">
  <div class="card-label red">🔴 SECURITY — PHISHING CAUGHT</div>
  <h3>3 Phishing/Scam Emails Auto-Trashed</h3>
  <div class="from">Auto-trashed before delivery to inbox</div>
  <p><strong>Hilton Financial Management</strong> (fake loan company, Indonesian domain) — classic advance-fee scam. <strong>melissaw212 account lockout</strong> (credential harvesting, Unicode subject, random subdomain). <strong>CashApp/Slots of Vegas</strong> (spoofed casino spam, obfuscated Unicode).</p>
  <p class="action red">→ No further action needed — already removed. Consider enabling Google's Enhanced Safe Browsing and reviewing spam filter settings.</p>
</div>

<div class="card red">
  <div class="card-label red">🔴 SECURITY — SPAM IN INBOX/FOLDERS</div>
  <h3>Explicit Adult Spam &amp; Suspicious Senders Not Yet Trashed</h3>
  <div class="from">Multiple senders via random subdomains</div>
  <p>Explicit adult spam ("FUCK-BUDDY SECRET," "Hot Sex," "Sex.Trick") arrived in folders. "DirectMeds" GLP-1 spam (2 emails), "Smart-Beauty Alternatives" hair spray spam, and "Slots of Vegas casino payment" all arrived from random subdomain addresses and should be deleted immediately.</p>
  <p class="action red">→ Delete all immediately. Mark as spam. Consider unrolling or reviewing Gmail spam settings.</p>
</div>

<div class="card yellow">
  <div class="card-label yellow">🟡 DEADLINE — SLACK TRIAL ENDING</div>
  <h3>Slack Pro Trial Expires August 1, 2026 (3 days)</h3>
  <div class="from">Slack &lt;no-reply@slack.com&gt;</div>
  <p>Your consulting work's Slack Pro plan trial ends August 1st. Decide now: upgrade to paid Pro plan or downgrade to free tier before losing premium features.</p>
  <p class="action yellow">→ Review usage and decide by August 1st. Act today to avoid disruption.</p>
  <p><strong>Due:</strong> August 1, 2026</p>
</div>

<div class="card yellow">
  <div class="card-label yellow">🟡 RSVP NEEDED — TODAY</div>
  <h3>HR Networking &amp; Job Search Open Office Hours — No RSVP</h3>
  <div class="from">Google Calendar — Today 12:00–1:00 PM ET</div>
  <p>This event starts in hours and your status is "Needs Action." 100+ attendees are registered. This is a core job-search networking session.</p>
  <p class="action yellow">→ RSVP now and add Zoom link to your browser: https://us06web.zoom.us/j/85945371140</p>
  <p><strong>Due:</strong> Today, July 30 — 12:00 PM ET</p>
</div>

<div class="card green">
  <div class="card-label green">🟢 JOB LEAD — HIGH PRIORITY</div>
  <h3>SVP Human Resources — Highgate Hotels, NYC ($270K–$320K)</h3>
  <div class="from">Indeed &lt;donotreply@match.indeed.com&gt;</div>
  <p>Indeed flagged this as a strong match based on your HR leadership experience. NYC-based, senior executive level, hospitality industry.</p>
  <p class="action green">→ Review full posting today and apply or save. Prepare tailored resume and cover letter.</p>
  <p><strong>Due:</strong> Review today</p>
</div>

<div class="card green">
  <div class="card-label green">🟢 LINKEDIN MESSAGES — RESPOND TODAY</div>
  <h3>Unread Messages: Robert T. Sicora, EdD &amp; Rana Saini</h3>
  <div class="from">LinkedIn via Gmail</div>
  <p>Two separate LinkedIn messages are unread and awaiting response. Both could be recruiter outreach, networking, or referral opportunities during an active job search.</p>
  <p class="action green">→ Log into LinkedIn and respond to both today. Do not let these go cold.</p>
  <p><strong>Due:</strong> Today, July 30</p>
</div>

<div class="card green">
  <div class="card-label green">🟢 JOB LEAD — RESCUED FROM TRASH</div>
  <h3>Head of People and Talent — Bluemercury (Rescued)</h3>
  <div class="from">LinkedIn Job Alerts — Rescued from Trash</div>
  <p>This alert was sent 3 times and one instance was rescued from Trash (protected sender rule). Posted 7/28/2026. Bluemercury is a luxury beauty brand (Macy's Inc.).</p>
  <p class="action green">→ Review role details on LinkedIn. Assess fit and apply if aligned.</p>
  <p><strong>Due:</strong> Today — time-sensitive posting</p>
</div>

<div class="card yellow">
  <div class="card-label yellow">🟡 MEMBERSHIP EXPIRY</div>
  <h3>Medium Membership Expires August 20, 2026</h3>
  <div class="from">Medium Daily Digest (in Trash)</div>
  <p>Your Medium membership will expire on August 20, 2026. If you use Medium for professional development articles, decide whether to renew.</p>
  <p class="action yellow">→ Decide by August 20 whether to reactivate or let lapse.</p>
  <p><strong>Due:</strong> August 20, 2026</p>
</div>

<!-- ============================================================ -->
<!-- SECTION 4: FULL 7-DAY CALENDAR -->
<!-- ============================================================ -->
<div class="section-title"><span class="icon">📅</span> Full 7-Day Calendar</div>

<div class="cal-day cal-today">📅 TODAY — Thursday, July 30, 2026</div>
<table>
  <thead>
    <tr><th>Time</th><th>Event</th><th>Status</th><th>Location / Link</th><th>Prep Needed</th><th>Notes</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>9:00–10:30 AM</td>
      <td><strong>Executive Roundtable</strong></td>
      <td><span class="status-declined">❌ DECLINED</span></td>
      <td><a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" style="color:#1e88e5;">Zoom Link</a><br><small>ID: 207 786 667 / PW: 205454</small></td>
      <td>None — declined</td>
      <td><span class="warn">You declined this meeting.</span> Host: John Madigan. If you wish to rejoin, contact organizer before 9 AM.</td>
    </tr>
    <tr>
      <td>12:00–1:00 PM</td>
      <td><strong>HR Networking &amp; Job Search: Open Office Hours</strong></td>
      <td><span class="status-pending">⚠️ RSVP NEEDED</span></td>
      <td><a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" style="color:#1e88e5;">Zoom Link</a></td>
      <td>Prepare intro, network talking points, job targets. No AI notetakers.</td>
      <td><strong class="warn">⚠️ RSVP NOW.</strong> 100+ attendees. Open discussion — no recording. This is a core networking session during active job search.</td>
    </tr>
  </tbody>
</table>

<div class="cal-day">📅 Friday, July 31, 2026</div>
<table>
  <thead><tr><th>Time</th><th>Event</th><th>Status</th><th>Location</th><th>Prep Needed</th><th>Notes</th></tr></thead>
  <tbody>
    <tr>
      <td colspan="6" style="color:#888; font-style:italic; text-align:center;">No events scheduled. Good day to job search, apply, and follow up on LinkedIn messages.</td>
    </tr>
  </tbody>
</table>

<div class="cal-day">📅 Saturday, August 1, 2026</div>
<table>
  <thead><tr><th>Time</th><th>Event</th><th>Status</th><th>Location</th><th>Prep Needed</th><th>Notes</th></tr></thead>
  <tbody>
    <tr>
      <td>2:30–3:30 PM</td>
      <td><strong>Eye Doctor Appointment</strong></td>
      <td><span class="status-confirmed">✅ Confirmed</span></td>
      <td>TBD — no location set</td>
      <td>Confirm office address. Bring insurance card.</td>
      <td><strong class="warn">⚠️ Also: Slack Pro trial expires today.</strong> Decide on Slack plan before end of day.</td>
    </tr>
  </tbody>
</table>

<div class="cal-day">📅 Sunday, August 2, 2026</div>
<table>
  <thead><tr><th>Time</th><th>Event</th><th>Status</th><th>Location</th><th>Prep Needed</th><th>Notes</th></tr></thead>
  <tbody>
    <tr>
      <td>All Day</td>
      <td><strong>🎂 Shari's Birthday</strong></td>
      <td><span class="status-confirmed">✅ Confirmed</span></td>
      <td>—</td>
      <td>Send card/message or plan celebration if applicable.</td>
      <td>All-day event. Don't forget to reach out!</td>
    </tr>
  </tbody>
</table>

<div class="cal-day">📅 Monday, August 3, 2026</div>
<table>
  <thead><tr><th>Time</th><th>Event</th><th>Status</th><th>Location</th><th>Prep Needed</th><th>Notes</th></tr></thead>
  <tbody>
    <tr>
      <td colspan="6" style="color:#888; font-style:italic; text-align:center;">No events scheduled. Shari's Birthday (all-day event) carries over from Sunday.</td>
    </tr>
  </tbody>
</table>

<div class="cal-day">📅 Tuesday, August 4, 2026</div>
<table>
  <thead><tr><th>Time</th><th>Event</th><th>Status</th><th>Location</th><th>Prep Needed</th><th>Notes</th></tr></thead>
  <tbody>
    <tr>
      <td>10:00–11:00 AM</td>
      <td><strong>PT (Physical Therapy)</strong></td>
      <td><span class="status-confirmed">✅ Confirmed</span></td>
      <td>No location set</td>
      <td>Confirm provider address. Wear comfortable clothing.</td>
      <td>Personal health appointment. No conflict.</td>
    </tr>
  </tbody>
</table>

<div class="cal-day">📅 Wednesday, August 5, 2026</div>
<table>
  <thead><tr><th>Time</th><th>Event</th><th>Status</th><th>Location</th><th>Prep Needed</th><th>Notes</th></tr></thead>
  <tbody>
    <tr>
      <td>12:00–1:30 PM</td>
      <td><strong>HR Networking &amp; Job Search Group — Zoom 2</strong></td>
      <td><span class="status-pending">⚠️ RSVP NEEDED</span></td>
      <td><a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" style="color:#1e88e5;">Zoom Link</a></td>
      <td>Review team guidelines. Prepare networking agenda. No AI notetakers.</td>
      <td><span class="warn">⚠️ RSVP pending.</span> 100+ attendees. This is the weekly group session — longer format (1.5 hrs).</td>
    </tr>
    <tr>
      <td>12:00–1:30 PM</td>
      <td><strong>Network</strong> <span style="color:#888;font-size:12px;">(personal note)</span></td>
      <td><span class="status-confirmed">✅ Confirmed</span></td>
      <td>No location set</td>
      <td>Same time as group Zoom — likely a reminder note for yourself.</td>
      <td><strong class="warn">⚠️ Exact time overlap</strong> with HR Networking Group Zoom. These may be the same event. Confirm and merge if so.</td>
    </tr>
  </tbody>
</table>

<!-- ============================================================ -->
<!-- SECTION 5: JOB SEARCH & INTERVIEW PIPELINE -->
<!-- ============================================================ -->
<div class="section-title"><span class="icon">💼</span> Job Search &amp; Interview Pipeline</div>
<table>
  <thead>
    <tr><th>Fit</th><th>Role / Opportunity</th><th>Company</th><th>Source</th><th>Compensation</th><th>Status</th><th>Action</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="badge fit-high">HIGH</span></td>
      <td>Senior Vice President, Human Resources</td>
      <td>Highgate Hotels</td>
      <td>Indeed (email)</td>
      <td>$270K–$320K</td>
      <td>🆕 New Alert</td>
      <td>Review &amp; apply today — NYC-based, exec-level, strong match</td>
    </tr>
    <tr>
      <td><span class="badge fit-high">HIGH</span></td>
      <td>Head of People and Talent</td>
      <td>Bluemercury (Macy's)</td>
      <td>LinkedIn Job Alerts (×3 alerts + rescued)</td>
      <td>Not listed</td>
      <td>⚠️ Alerted 3x — urgent</td>
      <td>Review on LinkedIn immediately — multiple alerts suggest strong match signal</td>
    </tr>
    <tr>
      <td><span class="badge fit-high">HIGH</span></td>
      <td>Chief Human Resources Officer</td>
      <td>Edged</td>
      <td>LinkedIn Job Alerts</td>
      <td>Not listed</td>
      <td>🆕 New Alert (7/28)</td>
      <td>Review role — CHRO level, check company profile and apply if fit</td>
    </tr>
    <tr>
      <td><span class="badge fit-med">MED</span></td>
      <td>Human Resources Generalist + 6 more</td>
      <td>Brown &amp; Buchanan Ventures + others</td>
      <td>Glassdoor (remote roles)</td>
      <td>Not listed</td>
      <td>📋 Alert — review</td>
      <td>Scan listings for senior-level fits; skip generalist roles if below target level</td>
    </tr>
    <tr>
      <td><span class="badge fit-med">MED</span></td>
      <td>Community Manager + 4 more (NYC)</td>
      <td>Vinyl Real Estate Mgmt + others</td>
      <td>Glassdoor (NYC)</td>
      <td>Not listed</td>
      <td>📋 Alert — review</td>
      <td>Scan for HR leadership roles — Community Manager may be below target level</td>
    </tr>
    <tr>
      <td><span class="badge fit-high">HIGH</span></td>
      <td>LinkedIn Message — Robert T. Sicora, EdD</td>
      <td>Unknown</td>
      <td>LinkedIn (email notification)</td>
      <td>—</td>
      <td>📩 Unread — respond</td>
      <td>Open LinkedIn and reply today — EdD title suggests executive/academic/consulting context</td>
    </tr>
    <tr>
      <td><span class="badge fit-high">HIGH</span></td>
      <td>LinkedIn Message — Rana Saini</td>
      <td>Unknown</td>
      <td>LinkedIn (email notification)</td>
      <td>—</td>
      <td>📩 Unread — respond</td>
      <td>Open LinkedIn and reply today — may be recruiter or peer referral</td>
    </tr>
    <tr>
      <td><span class="badge fit-med">MED</span></td>
      <td>HR Networking Open Office Hours</td>
      <td>Job Search Group</td>
      <td>Calendar — Today 12–1 PM</td>
      <td>—</td>
      <td>⚠️ RSVP needed</td>
      <td>RSVP &amp; attend today — networking is job search pipeline</td>
    </tr>
    <tr>
      <td><span class="badge fit-med">MED</span></td>
      <td>HR Networking Group Zoom</td>
      <td>Job Search Group</td>
      <td>Calendar — Aug 5, 12–1:30 PM</td>
      <td>—</td>
      <td>⚠️ RSVP needed</td>
      <td>RSVP for Aug 5 session</td>
    </tr>
    <tr>
      <td><span class="badge fit-med">MED</span></td>
      <td>What's Changing in Private Equity</td>
      <td>Thrive Resources / Susanna Madden</td>
      <td>Email — inbox-adjacent</td>
      <td>—</td>
      <td>📬 Unread — review</td>
      <td>PE-focused leadership content — may include executive roles or sponsor evaluation intel</td>
    </tr>
    <tr>
      <td><span class="badge fit-low">LOW</span></td>
      <td>AI Interview Prep (self-forwarded)</td>
      <td>Learn AI With Mariah</td>
      <td>Self-email (melissaw212)</td>
      <td>—</td>
      <td>📌 Resource</td>
      <td>Review both AI interview prep guides before next interview</td>
    </tr>
    <tr>
      <td><span class="badge fit-low">LOW</span></td>
      <td>Claude Debugging Prompts (self-email)</td>
      <td>Self</td>
      <td>Self-email (melissaw212)</td>
      <td>—</td>
      <td>📌 Resource</td>
      <td>Agentic AI work notes — file for reference</td>
    </tr>
  </tbody>
</table>

<!-- ============================================================ -->
<!-- SECTION 6: FULL EMAIL REVIEW BY CATEGORY -->
<!-- ============================================================ -->
<div class="section-title"><span class="icon">📧</span> Full Email Review by Category</div>

<!-- SECURITY / RISK -->
<div class="card red">
  <div class="card-label red">🔴 SECURITY / RISK — 6 Emails</div>
  <h3>Phishing, Scams &amp; Suspicious Senders</h3>
  <p><strong>Auto-Trashed (3):</strong></p>
  <p>• <strong>HILTON FINANCIAL MANAGEMENT</strong> (pipin.samsuri@ustp.co.id) — Subject: "LOAN" — Fake financial company from Indonesian domain, advance-fee/loan scam. <span class="auto-trash-note">AUTO-TRASHED</span></p>
  <p>• <strong>melissaw212 (spoofed)</strong> (random subdomain) — Subject: "Your Account has been locked…" — Credential-harvesting phishing attempt with obfuscated Unicode subject. <span class="auto-trash-note">AUTO-TRASHED</span></p>
  <p>• <strong>'CashApp' (spoofed)</strong> (random subdomain) — Subject: "You received a payment…" (Slots of Vegas casino spam) — Spoofed CashApp sender, casino fraud. <span class="auto-trash-note">AUTO-TRASHED</span></p>
  <p style="margin-top:8px;"><strong>Remaining in Folders — Delete Immediately (3):</strong></p>
  <p>• <strong>"FUCK-BUDDY SECRET"</strong> (random subdomain) — Explicit adult spam — delete immediately, mark as spam.</p>
  <p>• <strong>"Hot Sex 🔥🔥"</strong> (random subdomain) — Explicit adult spam — in Trash already but confirm permanent delete.</p>
  <p>• <strong>"Sex.Trick 🍆"</strong> (random subdomain) — Explicit adult spam — delete immediately.</p>
  <p class="action red">→ 3 already auto-trashed. Delete remaining 3 immediately. Mark all as spam. Review spam filter settings.</p>
</div>

<!-- JOB SEARCH -->
<div class="card green">
  <div class="card-label green">🟢 JOB SEARCH — 9 Emails</div>
  <h3>Job Alerts, Applications &amp; Platforms</h3>
  <p>• <strong>Indeed</strong> — SVP Human Resources @ Highgate Hotels ($270K–$320K NYC) — <strong>HIGH priority, apply today</strong></p>
  <p>• <strong>LinkedIn Job Alerts (×4)</strong> — Head of People &amp; Talent @ Bluemercury (posted 7/28, alerted 3x + rescued from trash); CHRO @ Edged (7/28)</p>
  <p>• <strong>Glassdoor (×2)</strong> — NYC roles (Community Manager + 4) and Remote US roles (HR Generalist + 6)</p>
  <p>• <strong>Melissa W (self, ×2)</strong> — AI Interview Prep resources forwarded to self</p>
  <p>• <strong>melissa (self)</strong> — Claude debugging prompts (AI workflow notes)</p>
  <p class="action green">→ Apply to SVP Highgate Hotels and review Bluemercury/Edged roles today. Scan Glassdoor alerts for senior-level fits. Review AI prep guides before next interview.</p>
</div>

<!-- RECRUITERS / NETWORKING -->
<div class="card green">
  <div class="card-label green">🟢 RECRUITERS / NETWORKING — 3 Emails</div>
  <h3>LinkedIn Messages &amp; Recruiter Outreach</h3>
  <p>• <strong>Robert T. Sicora, EdD (LinkedIn)</strong> — Unread message awaiting response. Academic/executive title — likely meaningful contact.</p>
  <p>• <strong>Rana Saini (LinkedIn)</strong> — Unread message awaiting response.</p>
  <p>• <strong>Susanna Madden / Thrive Resources</strong> — "What's Changing in Private Equity" — market intel from executive search firm; sponsor evaluation and PE leadership trends.</p>
  <p class="action green">→ Respond to both LinkedIn messages today. Read Thrive Resources email for PE market intelligence relevant to your search.</p>
</div>

<!-- CALENDAR / EVENTS -->
<div class="card blue">
  <div class="card-label blue">🔵 CALENDAR / EVENTS — 0 Emails</div>
  <h3>No standalone calendar invite emails in inbox today</h3>
  <p>All calendar events are already loaded in Google Calendar. See the Full 7-Day Calendar section above.</p>
  <p class="action blue">→ No action needed here — calendar is up to date.</p>
</div>

<!-- MEDICAL / HEALTH -->
<div class="card blue">
  <div class="card-label blue">🔵 MEDICAL / HEALTH — 1 Email</div>
  <h3>BambooHR Employee Handbook Checklist</h3>
  <p>• <strong>BambooHR</strong> — "What Is Your Employee Handbook Missing?" — Free checklist for HR professionals. Professional relevance, not personal health.</p>
  <p class="note">(Note: DirectMeds GLP-1 and Smart-Beauty hair growth spam are categorized under Security/Spam — not legitimate medical contacts.)</p>
  <p class="action blue">→ Review BambooHR checklist if currently building or auditing an employee handbook. Otherwise, archive.</p>
</div>

<!-- FINANCIAL / BILLING -->
<div class="card yellow">
  <div class="card-label yellow">🟡 FINANCIAL / BILLING — 3 Emails</div>
  <h3>Banking &amp; Investment Notifications</h3>
  <p>• <strong>Bank of America</strong> — Direct deposit $582.09 (July 30) — Account ending 7471. From: United States (likely government/payroll).</p>
  <p>• <strong>Bank of America</strong> — Direct deposit $3,200.00 (July 29) — Account ending 7471. From: Goldman Sachs Bank.</p>
  <p>• <strong>Merrill Lynch / American Funds</strong> (via proxyvote.com) — Semi-annual report available. Investment fund report notification — legitimate.</p>
  <p class="action yellow">→ Log into BofA to confirm both deposits posted correctly. Access American Funds semi-annual report when time allows.</p>
</div>

<!-- PROFESSIONAL DEVELOPMENT -->
<div class="card purple">
  <div class="card-label purple">🟣 PROFESSIONAL DEVELOPMENT — 2 Emails</div>
  <h3>Executive &amp; AI Leadership Intel</h3>
  <p>• <strong>Stanton Chase / LinkedIn Newsletter</strong> (in Trash) — "Why Can't 82% of Executives Report Positive Quantified AI Returns Yet? — HKUST J-Curve" — Highly relevant for executive interviews discussing AI ROI.</p>
  <p>• <strong>BambooHR</strong> — Employee handbook checklist — practical HR tool.</p>
  <p class="action purple">→ Rescue the Stanton Chase AI J-Curve article from Trash if not read — directly relevant for executive AI conversations. Review BambooHR checklist as needed.</p>
</div>

<!-- PERSONAL -->
<div class="card blue">
  <div class="card-label blue">🔵 PERSONAL — 4 Emails</div>
  <h3>Dating Apps, Personal Finance, Personal Notes</h3>
  <p>• <strong>Match.com</strong> — Michael (59, Northport NY) viewed your profile. Unread.</p>
  <p>• <strong>Hinge Team</strong> — Eli &amp; Melissa match recommendation. In inbox.</p>
  <p>• <strong>USPS Informed Delivery</strong> — 1 mailpiece arriving today, 0 packages. Already read.</p>
  <p>• <strong>melissa (self)</strong> — "unsubscribe" — auto-generated Gmail message. No action needed.</p>
  <p class="action blue">→ Check Match and Hinge when you have personal time. Check mailbox today. No urgent action needed.</p>
</div>

<!-- NEWSLETTERS / SUBSCRIPTIONS -->
<div class="card purple">
  <div class="card-label purple">🟣 NEWSLETTERS &amp; SUBSCRIPTIONS — 10 Emails</div>
  <h3>News, Career, AI, Finance, Lifestyle Newsletters</h3>
  <p>• <strong>Medium Daily Digest (×2)</strong> (Trash) — "I Woke Up at 4:30 AM for 30 Days" + "How To Become an Agentic AI Engineer in 6 Months" — Membership expires Aug 20. Decide on renewal.</p>
  <p>• <strong>The AI Report</strong> (Trash) — "Altman faces Congress after hack; Fiverr stock crashes 20%" — AI market news.</p>
  <p>• <strong>TLDR Newsletter</strong> (Trash) — Starlink cell network, DoorDash drones, ChatGPT optimizations.</p>
  <p>• <strong>Dylan's Diary / Behind the Markets</strong> (Trash) — "Is the Mag Seven Dead? Robots changing everything."</p>
  <p>• <strong>Stanton Chase via LinkedIn</strong> (Trash) — AI ROI J-Curve study — highly relevant for exec interviews.</p>
  <p>• <strong>The Daily Skimm</strong> (Trash) — "A whale of a tale / Simone Biles" — general news digest.</p>
  <p>• <strong>The People People Group (TPPG)</strong> (Trash) — New hire orientation, employee engagement digest.</p>
  <p>• <strong>Gemma Bonham-Carter</strong> (Trash) — Draft Week Day 4.</p>
  <p>• <strong>1% Better Newsletter</strong> (Trash) — Fauci, jet lag, Jon Bernthal workout.</p>
  <p>• <strong>Lisa Rangel / Chameleon Resumes</strong> (Trash) — "Are you blaming a database for your fate?" — resume/job search coaching.</p>
  <p class="action purple">→ Consider rescuing Stanton Chase AI article and TPPG digest. Review Medium renewal decision. Unsubscribe from low-value newsletters.</p>
</div>

<!-- PROMOTIONAL / RETAIL -->
<div class="card gray">
  <div class="card-label gray">⬜ PROMOTIONAL / RETAIL — 8 Emails</div>
  <h3>Retail, Shopping, Rewards Emails</h3>
  <p>• <strong>22 Words</strong> (inbox) — Amazon Lightning Deals (33% off lunch box, fire pit, batteries)</p>
  <p>• <strong>Kohl's</strong> (Trash) — Extra 20% off Friends &amp; Family</p>
  <p>• <strong>Gap Factory</strong> (Trash) — 60% off ends tonight + extra 20% + free shipping</p>
  <p>• <strong>Old Navy</strong> (Trash) — $17 PowerSoft leggings, 50% off everything</p>
  <p>• <strong>DSW</strong> — VIP Program changes coming Sept 8</p>
  <p>• <strong>Microsoft Rewards</strong> — Harry Styles tickets or Xbox Series X raffle</p>
  <p>• <strong>Smart-Beauty Alternatives</strong> — Hair growth spray spam (suspicious subdomain)</p>
  <p>• <strong>DirectMeds / GLP-1 (×2)</strong> — Semaglutide/Tirzepatide weight loss spam (suspicious subdomains)</p>
  <p class="action gray">→ Delete/ignore most. DSW VIP note is worth reading (program changing Sept 8). Gap sale expired. Mark Smart-Beauty and DirectMeds as spam.</p>
</div>

<!-- TRASH REVIEW (detailed in section 7 below) -->
<!-- SAFE TO DELETE / IGNORE -->
<div class="card gray">
  <div class="card-label gray">⬜ SAFE TO DELETE / IGNORE — 4 Emails</div>
  <h3>Low-Value, Expired, or Redundant Emails</h3>
  <p>• <strong>Top Class Actions</strong> — FedEx/Kroger/UPS unpaid wage class action solicitation — not applicable.</p>
  <p>• <strong>melissaw212 "Payment Sent" (Slots of Vegas spam)</strong> — already categorized under security/spam.</p>
  <p>• <strong>melissa (self) "unsubscribe"</strong> — auto-generated Gmail unsubscribe confirmation.</p>
  <p>• <strong>Microsoft Rewards</strong> — Raffle email, already read, low priority.</p>
  <p class="action gray">→ Delete all. No action required.</p>
</div>

<!-- ============================================================ -->
<!-- SECTION 7: TRASH REVIEW -->
<!-- ============================================================ -->
<div class="section-title"><span class="icon">🗑️</span> Trash Review</div>

<div class="card green">
  <div class="card-label green">✅ RESTORE IMMEDIATELY</div>
  <h3>Emails Worth Rescuing from Trash</h3>
  <table>
    <thead><tr><th>Sender</th><th>Subject</th><th>Why Restore</th></tr></thead>
    <tbody>
      <tr>
        <td>LinkedIn Job Alerts <span class="rescued-note">✅ ALREADY RESCUED</span></td>
        <td>Head of People and Talent at Bluemercury</td>
        <td>Protected sender — already rescued and returned to inbox. Apply immediately.</td>
      </tr>
      <tr>
        <td>Stanton Chase via LinkedIn</td>
        <td>Why Can't 82% of Executives Report Positive AI Returns? (J-Curve)</td>
        <td>Highly relevant executive AI ROI research — valuable for interviews and strategy discussions.</td>
      </tr>
      <tr>
        <td>The People People Group (TPPG)</td>
        <td>TPPG Digest — New Hire Orientation, Employee Engagement</td>
        <td>Professional HR community digest — directly relevant to your field.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="card yellow">
  <div class="card-label yellow">🟡 REVIEW BEFORE DELETING</div>
  <h3>May Have Value — Check Before Permanent Delete</h3>
  <table>
    <thead><tr><th>Sender</th><th>Subject</th><th>Notes</th></tr></thead>
    <tbody>
      <tr>
        <td>Medium Daily Digest (×2)</td>
        <td>"I Woke Up at 4:30 AM…" / "How to Become an Agentic AI Engineer"</td>
        <td>Membership expires Aug 20 — decide on renewal. Agentic AI article may be worth reading.</td>
      </tr>
      <tr>
        <td>The AI Report</td>
        <td>Altman faces Congress after hack; Fiverr/AI/gig economy</td>
        <td>AI market news — relevant for exec conversations about AI disruption.</td>
      </tr>
      <tr>
        <td>TLDR Newsletter</td>
        <td>Starlink cell network, DoorDash drones, ChatGPT optimizations</td>
        <td>Tech briefing — relevant if you follow AI/tech trends for interview prep.</td>
      </tr>
      <tr>
        <td>Dylan's Diary / Behind the Markets</td>
        <td>Is the Mag Seven Dead?</td>
        <td>Finance/investing newsletter — scan if relevant to your portfolio.</td>
      </tr>
      <tr>
        <td>Lisa Rangel / Chameleon Resumes</td>
        <td>Are you blaming a database for your fate?</td>
        <td>Resume/job search coaching — potentially useful during active search.</td>
      </tr>
      <tr>
        <td>Glassdoor Jobs</td>
        <td>HR Generalist at Brown &amp; Buchanan + 6 remote roles</td>
        <td>Remote roles — scan for any senior-level HR fits before deleting.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="card gray">
  <div class="card-label gray">⬜ SAFE TO DELETE PERMANENTLY</div>
  <h3>No Value — Permanent Delete Recommended</h3>
  <table>
    <thead><tr><th>Sender</th><th>Subject</th><th>Reason</th></tr></thead>
    <tbody>
      <tr>
        <td>HILTON FINANCIAL MANAGEMENT <span class="auto-trash-note">AUTO-TRASHED</span></td>
        <td>LOAN</td>
        <td>Advance-fee loan scam from Indonesian domain. Already auto-trashed.</td>
      </tr>
      <tr>
        <td>melissaw212 spoofed <span class="auto-trash-note">AUTO-TRASHED</span></td>
        <td>Your Account has been locked (Unicode)</td>
        <td>Credential-harvesting phishing. Already auto-trashed.</td>
      </tr>
      <tr>
        <td>'CashApp' spoofed <span class="auto-trash-note">AUTO-TRASHED</span></td>
        <td>You received $2,500 (Slots of Vegas casino)</td>
        <td>Spoofed CashApp casino fraud. Already auto-trashed.</td>
      </tr>
      <tr>
        <td>'Hot Sex 🔥🔥'</td>
        <td>Make her squirt 3x tonight…</td>
        <td>Explicit adult spam. In Trash — permanently delete.</td>
      </tr>
      <tr>
        <td>Kohl's Friends &amp; Family</td>
        <td>Extra 20% off for friends &amp; family</td>
        <td>Standard retail promotional — offer has likely expired.</td>
      </tr>
      <tr>
        <td>Gap Factory</td>
        <td>60% off ends tonight (extra 20% + free shipping)</td>
        <td>Time-limited sale — ended last night. Delete.</td>
      </tr>
      <tr>
        <td>Old Navy</td>
        <td>$17 PowerSoft leggings, 50% off everything</td>
        <td>Time-limited sale — likely expired. Delete.</td>
      </tr>
      <tr>
        <td>Gemma Bonham-Carter</td>
        <td>[Draft Week Day 4] meet the quiet MVPs</td>
        <td>Content marketing newsletter — low value. Delete or unsubscribe.</td>
      </tr>
      <tr>
        <td>1% Better Newsletter</td>
        <td>Fauci Pleads Fifth, Jet Lag Relief, Jon Bernthal Workout</td>
        <td>Lifestyle/wellness digest — low professional relevance. Delete or unsubscribe.</td>
      </tr>
      <tr>
        <td>The Daily Skimm</td>
        <td>A whale of a tale</td>
        <td>General news digest — low priority. Delete or unsubscribe.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ============================================================ -->
<!-- SECTION 8: PROMOTIONAL / RETAIL SUMMARY -->
<!-- ============================================================ -->
<div class="section-title"><span class="icon">🛍️</span> Promotional / Retail Summary</div>
<table>
  <thead>
    <tr><th>Sender / Brand</th><th>Count</th><th>Subject / Theme</th><th>Location</th><th>Recommendation</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>22 Words (Amazon)</td>
      <td>1</td>
      <td>Amazon Lightning Deals — 33% off lunch box, fire pit, batteries</td>
      <td>Inbox
