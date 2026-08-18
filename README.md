<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa — August 18, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header .sub { font-size: 14px; opacity: 0.75; margin-top: 4px; }
  .header .meta { display: flex; gap: 28px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.1); border-radius: 8px; padding: 8px 16px; font-size: 13px; }
  .header .meta-item strong { display: block; font-size: 20px; font-weight: 700; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; color: #1a1a2e; border-left: 5px solid #0f3460; padding-left: 12px; margin-bottom: 14px; letter-spacing: 0.3px; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; border-left: 5px solid transparent; }
  .card-red    { background: #fff5f5; border-left-color: #e53e3e; }
  .card-yellow { background: #fffff0; border-left-color: #d69e2e; }
  .card-blue   { background: #ebf8ff; border-left-color: #3182ce; }
  .card-green  { background: #f0fff4; border-left-color: #38a169; }
  .card-purple { background: #faf5ff; border-left-color: #805ad5; }
  .card-gray   { background: #f7f7f7; border-left-color: #a0aec0; }
  .card-orange { background: #fffaf0; border-left-color: #dd6b20; }

  .card-title { font-weight: 700; font-size: 14px; margin-bottom: 4px; }
  .card-sub   { font-size: 12px; color: #555; margin-bottom: 6px; }
  .card-body  { font-size: 13px; }
  .card-action { margin-top: 8px; font-size: 12px; font-weight: 600; }
  .badge { display: inline-block; border-radius: 4px; padding: 1px 7px; font-size: 11px; font-weight: 700; margin-right: 4px; }
  .badge-red    { background: #fed7d7; color: #c53030; }
  .badge-yellow { background: #fefcbf; color: #975a16; }
  .badge-green  { background: #c6f6d5; color: #276749; }
  .badge-blue   { background: #bee3f8; color: #2b6cb0; }
  .badge-purple { background: #e9d8fd; color: #553c9a; }
  .badge-gray   { background: #e2e8f0; color: #4a5568; }
  .badge-orange { background: #feebc8; color: #7b341e; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }
  th { background: #1a1a2e; color: #fff; padding: 10px 12px; text-align: left; font-size: 12px; letter-spacing: 0.5px; text-transform: uppercase; }
  td { padding: 9px 12px; border-bottom: 1px solid #edf2f7; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f7fafc; }
  .tbl-status { white-space: nowrap; font-weight: 700; font-size: 12px; }

  /* SUMMARY BULLETS */
  .exec-bullets { list-style: none; }
  .exec-bullets li { padding: 10px 16px; margin-bottom: 8px; border-radius: 8px; font-size: 13.5px; position: relative; padding-left: 34px; }
  .exec-bullets li::before { content: attr(data-icon); position: absolute; left: 10px; font-size: 16px; }
  .bullet-red    { background: #fff5f5; border: 1px solid #feb2b2; }
  .bullet-green  { background: #f0fff4; border: 1px solid #9ae6b4; }
  .bullet-blue   { background: #ebf8ff; border: 1px solid #90cdf4; }

  /* PRIORITY TAGS */
  .pri-high   { color: #c53030; font-weight: 700; }
  .pri-medium { color: #975a16; font-weight: 700; }
  .pri-low    { color: #276749; font-weight: 700; }

  /* DASHBOARD GRID */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-box { background: #fff; border-radius: 10px; padding: 16px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
  .dash-box h4 { font-size: 11px; text-transform: uppercase; letter-spacing: 0.7px; color: #718096; margin-bottom: 8px; }
  .dash-box .dash-val { font-size: 26px; font-weight: 800; color: #1a1a2e; }
  .dash-box .dash-label { font-size: 12px; color: #555; margin-top: 2px; }
  .dash-box ul { list-style: none; padding: 0; margin: 0; }
  .dash-box ul li { font-size: 12px; padding: 3px 0; border-bottom: 1px solid #f0f0f0; }
  .dash-box ul li:last-child { border-bottom: none; }

  /* TRIAGE TABLE ROW COLORS */
  .row-rescued td { background: #f0fff4; }
  .row-inbox   td { background: #ebf8ff; }
  .row-trash   td { background: #f7f7f7; }
  .row-auto    td { background: #fff5f5; }

  /* TOP 3 */
  .top3 { display: flex; gap: 14px; flex-wrap: wrap; }
  .top3-card { flex: 1; min-width: 260px; background: linear-gradient(135deg, #1a1a2e, #0f3460); color: #fff; border-radius: 12px; padding: 20px 22px; }
  .top3-card .num { font-size: 36px; font-weight: 900; opacity: 0.3; line-height: 1; }
  .top3-card .top3-title { font-size: 15px; font-weight: 700; margin-top: 4px; }
  .top3-card .top3-body { font-size: 12px; opacity: 0.8; margin-top: 6px; }

  /* DIVIDER */
  .divider { border: none; border-top: 2px solid #e2e8f0; margin: 22px 0; }

  /* ALERT BOX */
  .alert-box { border-radius: 8px; padding: 12px 16px; font-size: 13px; margin-bottom: 10px; }
  .alert-red { background: #fed7d7; border-left: 4px solid #e53e3e; color: #742a2a; }
  .alert-yellow { background: #fefcbf; border-left: 4px solid #d69e2e; color: #744210; }
  .alert-green { background: #c6f6d5; border-left: 4px solid #38a169; color: #1c4532; }

  /* SMALL LABEL */
  .lbl { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px; color: #718096; }

  /* RESCUED BANNER */
  .rescued-note { font-size: 11px; font-style: italic; color: #276749; margin-top: 4px; }
  .auto-trash-note { font-size: 11px; font-style: italic; color: #c53030; margin-top: 4px; }

  @media(max-width: 600px) {
    .header { padding: 20px 16px; }
    .top3 { flex-direction: column; }
    .dash-grid { grid-template-columns: 1fr 1fr; }
  }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ═══════════════════════════════════════════════════════════
     SECTION 0 — EMAIL TRIAGE QUICK LIST
════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📋 Email Triage Quick List</div>
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
      <!-- RESCUED FIRST -->
      <tr class="row-rescued">
        <td class="tbl-status"><span class="badge badge-green">✅ RESCUED</span></td>
        <td>Spotify</td>
        <td>306787 — Your Spotify login code</td>
        <td>Login verification code rescued from Trash — official Spotify domain, account security email.</td>
      </tr>
      <tr class="row-rescued">
        <td class="tbl-status"><span class="badge badge-green">✅ RESCUED</span></td>
        <td>Tune My Music</td>
        <td>Welcome to Tune My Music! 🎶</td>
        <td>Welcome/confirmation email rescued from Trash — legitimate music transfer service Melissa signed up for.</td>
      </tr>

      <!-- INBOX EMAILS -->
      <tr class="row-inbox">
        <td class="tbl-status"><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Outskill</td>
        <td>You missed the Claude Workshop… here's your second chance</td>
        <td>Second-chance offer to attend Claude AI workshop — professional development opportunity.</td>
      </tr>
      <tr class="row-inbox">
        <td class="tbl-status"><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Inclusively</td>
        <td>melissa weiss — Check out these recommended jobs for you!</td>
        <td>Personalized job recommendations from Inclusively platform based on profile.</td>
      </tr>
      <tr class="row-inbox">
        <td class="tbl-status"><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Bank of America</td>
        <td>A direct deposit was credited to your account</td>
        <td>NYS DOL UI (unemployment) deposit of $760.38 credited to account ending 7471.</td>
      </tr>
      <tr class="row-inbox">
        <td class="tbl-status"><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Match</td>
        <td>You've had a profile view from Keith</td>
        <td>Keith, 62, New York viewed Melissa's Match profile.</td>
      </tr>
      <tr class="row-inbox">
        <td class="tbl-status"><span class="badge badge-blue">📥 INBOX</span></td>
        <td>OkCupid</td>
        <td>You have an Intro!</td>
        <td>New intro/message received on OkCupid — unread.</td>
      </tr>
      <tr class="row-inbox">
        <td class="tbl-status"><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Judy Boreham via LinkedIn</td>
        <td>Judy accepted your invitation, explore their network</td>
        <td>LinkedIn connection Judy Boreham accepted Melissa's invitation.</td>
      </tr>
      <tr class="row-inbox">
        <td class="tbl-status"><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Judy Boreham via LinkedIn</td>
        <td>Judy just messaged you</td>
        <td>Judy Boreham sent a LinkedIn message — awaiting response.</td>
      </tr>
      <tr class="row-inbox">
        <td class="tbl-status"><span class="badge badge-blue">📥 INBOX</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>VP, People Business Partners &amp; Talent Development at Clio</td>
        <td>Senior VP-level HR role at Clio (legal AI company) — strong match alert.</td>
      </tr>
      <tr class="row-inbox">
        <td class="tbl-status"><span class="badge badge-blue">📥 INBOX</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>People Business Partner Director, Engineering at Brex</td>
        <td>Director-level HRBP role at Brex (fintech) — strong match alert.</td>
      </tr>

      <!-- SPAM/PHISHING NOT IN TRASH (in inbox or unorganized) -->
      <tr class="row-inbox">
        <td class="tbl-status"><span class="badge badge-red">⚠️ SPAM</span></td>
        <td>Sex.Pheromones / various</td>
        <td>[Multiple explicit spam emails]</td>
        <td>Multiple explicit/adult spam emails in non-trash folders — see Security/Spam section. Flag and delete immediately.</td>
      </tr>
      <tr class="row-inbox">
        <td class="tbl-status"><span class="badge badge-red">🔐 SECURITY</span></td>
        <td>Google</td>
        <td>Security alert — TuneMyMusic access granted</td>
        <td>4 Google security alerts re: TuneMyMusic access to Google Account — verify this was intentional.</td>
      </tr>
      <tr class="row-inbox">
        <td class="tbl-status"><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Zoom</td>
        <td>Congratulations! Your seat is reserved! (Claude 101 Workshop)</td>
        <td>Two Zoom confirmations for Claude 101 Workshop registration — duplicate confirmation.</td>
      </tr>
      <tr class="row-inbox">
        <td class="tbl-status"><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Google / Spotify / TuneMyMusic</td>
        <td>Account activity (shared data, sign-in)</td>
        <td>Google shared data alerts for Spotify and TuneMyMusic sign-ins — routine account activity.</td>
      </tr>
      <tr class="row-inbox">
        <td class="tbl-status"><span class="badge badge-blue">📥 INBOX</span></td>
        <td>BambooHR (Sadie)</td>
        <td>[HR Hub] Your Back-to-School Edition for HR Growth ✏️</td>
        <td>Monthly HR newsletter — professional development content.</td>
      </tr>
      <tr class="row-inbox">
        <td class="tbl-status"><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Match</td>
        <td>Amir likes you. See if it's mutual.</td>
        <td>Amir liked Melissa's Match profile — not in inbox but active notification.</td>
      </tr>

      <!-- TRASH SUMMARY ROWS -->
      <tr class="row-auto">
        <td class="tbl-status"><span class="badge badge-red">🗑 AUTO-TRASHED</span></td>
        <td colspan="3"><strong>1 email auto-trashed (phishing)</strong> — "Payment-System" fake cloud storage renewal alert designed to harvest credentials. See Trash Review → Auto-Trashed Phishing.</td>
      </tr>
      <tr class="row-trash">
        <td class="tbl-status"><span class="badge badge-gray">🗂 MANUAL TRASH</span></td>
        <td colspan="3"><strong>~20 emails in Trash (manual)</strong> — Newsletters (1% Better, Dylan's Diary, Daily Skimm, BambooHR digest), promotional retail (Kohl's ×2, YesStyle, Old Navy, Gap Factory, Amazon), Chick-fil-A reward, Trump fundraising, SlicethePie, Glassdoor job alerts ×2, LinkedIn digest, deleted ChatGPT link, and explicit spam. See Trash Review for full breakdown.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 1 — HEADER
════════════════════════════════════════════════════════════ -->
<div class="header">
  <div class="sub">EXECUTIVE BRIEFING — PREPARED BY YOUR CHIEF OF STAFF</div>
  <h1>Good morning, Melissa ☀️</h1>
  <div class="sub">Tuesday, August 18, 2026 &nbsp;|&nbsp; Your day at a glance</div>
  <div class="meta">
    <div class="meta-item"><strong>50</strong>Total Emails Reviewed</div>
    <div class="meta-item"><strong>11</strong>Calendar Events</div>
    <div class="meta-item"><strong>2</strong>Events Today</div>
    <div class="meta-item"><strong>$760.38</strong>UI Deposit Received</div>
    <div class="meta-item"><strong>2</strong>Hot Job Leads</div>
    <div class="meta-item"><strong>⚠️ 4+</strong>Security Alerts</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 2 — EXECUTIVE SUMMARY
════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">🧠 Executive Summary</div>
  <ul class="exec-bullets">
    <li class="bullet-red" data-icon="🔴"><strong>SECURITY RISK:</strong> Multiple explicit spam emails remain outside of Trash (not auto-removed) and 4 Google security alerts were triggered by TuneMyMusic account access. Verify the TuneMyMusic connection was intentional and immediately mark/delete all adult spam emails from your inbox and unorganized folders.</li>
    <li class="bullet-green" data-icon="🟢"><strong>JOB SEARCH OPPORTUNITY:</strong> Two strong senior HR leadership job alerts arrived — VP, People Business Partners &amp; Talent Development at Clio and Director HRBP Engineering at Brex. Judy Boreham (new LinkedIn connection) has already messaged you, presenting a warm networking opportunity. Review and respond today.</li>
    <li class="bullet-blue" data-icon="🔵"><strong>CALENDAR &amp; DEADLINES:</strong> Stella's vet appointment is this morning 10–11 AM. Tomorrow (Aug 19) includes two back-to-back commitments: HR Networking &amp; Job Search Group (noon–1:30 PM, needs RSVP) and a 1:1 with Monte Montoya (2–3 PM). The Executive Roundtable on Aug 20 has been declined — confirm this is intentional.</li>
  </ul>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 3 — ACTION REQUIRED
════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">⚡ Action Required</div>

  <div class="card card-red">
    <div class="card-title">🔐 Verify TuneMyMusic Google Account Access</div>
    <div class="card-sub">Source: Google Security Alert (×4) — no-reply@accounts.google.com</div>
    <div class="card-body">Google sent 4 security alerts confirming TuneMyMusic was granted access to your Google Account data. If you intentionally signed up for TuneMyMusic (the welcome email was rescued from Trash), this is routine. However, verify the access scope at <strong>myaccount.google.com/permissions</strong> and revoke if unexpected.</div>
    <div class="card-action">👉 Action: Go to myaccount.google.com → Security → Third-party apps → Review TuneMyMusic access. <span class="badge badge-red">TODAY</span></div>
  </div>

  <div class="card card-red">
    <div class="card-title">🚫 Clean Up Explicit / Adult Spam in Non-Trash Folders</div>
    <div class="card-sub">Source: Multiple spoofed senders — Sex.Pheromones, FuckMyPussy, Men's Health Advisory, Watch this Alone, Harvard Researcher, and others</div>
    <div class="card-body">At least 8 explicit/adult spam emails landed outside Trash and were not auto-removed. These come from spoofed random domains and contain malicious links. Do not click anything. Mark all as spam immediately.</div>
    <div class="card-action">👉 Action: Select all, mark as spam, block senders. Consider enabling stronger spam filters. <span class="badge badge-red">TODAY</span></div>
  </div>

  <div class="card card-yellow">
    <div class="card-title">📋 RSVP — HR Networking &amp; Job Search Group (Zoom)</div>
    <div class="card-sub">Source: Calendar — HR Networking &amp; Job Search Group — Zoom 2 | Aug 19, 12:00–1:30 PM</div>
    <div class="card-body">This meeting shows as <strong>needsAction</strong> on your calendar — you have not yet confirmed attendance. This is your regular networking group with 150+ HR professionals. High-value for job search momentum.</div>
    <div class="card-action">👉 Action: RSVP Yes and confirm attendance. Link: https://us06web.zoom.us/j/81954171722 <span class="badge badge-yellow">BY EOD TODAY</span></div>
  </div>

  <div class="card card-yellow">
    <div class="card-title">📋 RSVP — HR Networking Open Office Hours (Zoom)</div>
    <div class="card-sub">Source: Calendar — HR Networking &amp; Job Search: Open Office Hours — Zoom 2 | Aug 20, 12:00–1:00 PM</div>
    <div class="card-body">Also shows as <strong>needsAction</strong>. Open office hours with the same HR networking group. Low-pressure, high-value for connection and job leads.</div>
    <div class="card-action">👉 Action: RSVP Yes. Link: https://us06web.zoom.us/j/85945371140 <span class="badge badge-yellow">BY EOD TODAY</span></div>
  </div>

  <div class="card card-green">
    <div class="card-title">💼 Review &amp; Apply — VP, People Business Partners &amp; Talent Development at Clio</div>
    <div class="card-sub">Source: LinkedIn Job Alerts — jobalerts-noreply@linkedin.com</div>
    <div class="card-body">Clio is the global leader in legal AI technology. This VP-level role aligns directly with your HR leadership background. Strong fit. Applications move quickly for senior roles.</div>
    <div class="card-action">👉 Action: Review the listing on LinkedIn and apply today or add to your pipeline. <span class="badge badge-green">TODAY</span></div>
  </div>

  <div class="card card-green">
    <div class="card-title">💼 Review &amp; Apply — People Business Partner Director, Engineering at Brex</div>
    <div class="card-sub">Source: LinkedIn Job Alerts — jobalerts-noreply@linkedin.com</div>
    <div class="card-body">Brex is a high-growth fintech company. Director-level HRBP role supporting engineering. Strong cultural and experience fit based on your profile.</div>
    <div class="card-action">👉 Action: Review on LinkedIn and apply or tailor your resume this week. <span class="badge badge-green">THIS WEEK</span></div>
  </div>

  <div class="card card-green">
    <div class="card-title">💬 Respond to Judy Boreham on LinkedIn</div>
    <div class="card-sub">Source: LinkedIn — messaging-digest-noreply@linkedin.com | Also: Connection accepted</div>
    <div class="card-body">Judy Boreham accepted your connection request AND immediately sent you a message. This is a warm, proactive networking contact — respond promptly to keep the momentum going.</div>
    <div class="card-action">👉 Action: Log into LinkedIn, read Judy's message, and reply thoughtfully today. <span class="badge badge-green">TODAY</span></div>
  </div>

  <div class="card card-yellow">
    <div class="card-title">🏦 Acknowledge UI Deposit — $760.38</div>
    <div class="card-sub">Source: Bank of America — onlinebanking@ealerts.bankofamerica.com</div>
    <div class="card-body">NYS DOL Unemployment Insurance direct deposit of $760.38 credited to your Personal Checking/Savings Account ending 7471 on August 18, 2026. No action needed beyond acknowledgment — confirm amount matches your expected UI payment.</div>
    <div class="card-action">👉 Action: Verify amount in Bank of America app and update your budget tracker. <span class="badge badge-yellow">TODAY</span></div>
  </div>

  <div class="card card-blue">
    <div class="card-title">🎓 Evaluate Claude 101 Workshop (Second Chance Offer)</div>
    <div class="card-sub">Source: Outskill — hi@mail.outskill.com (Inbox) + Zoom Confirmations (×2)</div>
    <div class="card-body">You are already registered for a Claude 101 Workshop (two Zoom confirmation emails received). Outskill also sent a "second chance" offer for anyone who missed the first session. You appear to be registered — review your Zoom confirmations for the event date/time and add to your calendar if not already there.</div>
    <div class="card-action">👉 Action: Check Zoom confirmation emails for workshop date/time. Add to calendar. <span class="badge badge-blue">TODAY</span></div>
  </div>

  <div class="card card-yellow">
    <div class="card-title">📅 Verizon Fios Bill Due</div>
    <div class="card-sub">Source: Calendar — Verizon Fios Bill | Aug 23, 2026 (All Day)</div>
    <div class="card-body">Your Verizon Fios bill is flagged on your calendar for August 23. Ensure payment is queued or auto-pay is confirmed to avoid service interruption.</div>
    <div class="card-action">👉 Action: Verify auto-pay or schedule manual payment before Aug 23. <span class="badge badge-yellow">BY AUG 23</span></div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 4 — FULL 7-DAY CALENDAR
════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📅 Full 7-Day Calendar — Aug 18–24, 2026</div>

  <!-- TODAY AUG 18 -->
  <div class="card card-blue" style="margin-bottom:8px;">
    <div class="card-title">📌 TODAY — Tuesday, August 18, 2026</div>
  </div>
  <table style="margin-bottom:16px;">
    <thead><tr><th>Time</th><th>Event</th><th>Status</th><th>Location / Link</th><th>Prep / Notes</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>10:00 AM – 11:00 AM</strong></td>
        <td>🐾 Vet <em>(also listed as "Stella Vet")</em></td>
        <td><span class="badge badge-green">Confirmed</span></td>
        <td>No location listed</td>
        <td>⚠️ <strong>Duplicate entry</strong> — "Vet" and "Stella Vet" appear to be the same appointment. Confirm location and bring Stella's records/vaccination history. This is happening NOW — make sure you are on your way or already there.</td>
      </tr>
    </tbody>
  </table>

  <!-- AUG 19 -->
  <div class="card card-blue" style="margin-bottom:8px;">
    <div class="card-title">📌 Wednesday, August 19, 2026</div>
  </div>
  <table style="margin-bottom:16px;">
    <thead><tr><th>Time</th><th>Event</th><th>Status</th><th>Location / Link</th><th>Prep / Notes</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>12:00 PM – 1:30 PM</strong></td>
        <td>HR Networking &amp; Job Search Group — Zoom 2 <em>(also listed as "Network")</em></td>
        <td><span class="badge badge-yellow">Needs RSVP</span></td>
        <td><a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a></td>
        <td>⚠️ <strong>RSVP PENDING.</strong> Review agenda in calendar description. Large group session (150+ HR professionals). Prepare 30-second intro update on job search status. ⚠️ Duplicate: "Network" event at same time — same meeting, remove duplicate.</td>
      </tr>
      <tr>
        <td><strong>2:00 PM – 3:00 PM</strong></td>
        <td>M&amp;m — 1:1 with Monte Montoya</td>
        <td><span class="badge badge-green">Accepted</span></td>
        <td>No location listed (likely Zoom or phone)</td>
        <td>Confirm meeting format with monte.montoya@gmail.com. Prepare agenda or talking points. Could be a networking/mentoring session — prepare your current job search update.</td>
      </tr>
    </tbody>
  </table>

  <!-- AUG 20 -->
  <div class="card card-blue" style="margin-bottom:8px;">
    <div class="card-title">📌 Thursday, August 20, 2026</div>
  </div>
  <table style="margin-bottom:16px;">
    <thead><tr><th>Time</th><th>Event</th><th>Status</th><th>Location / Link</th><th>Prep / Notes</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>9:00 AM – 10:30 AM</strong></td>
        <td>Executive Roundtable (John Madigan)</td>
        <td><span class="badge badge-red">Declined</span></td>
        <td><a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom — Meeting ID: 207 786 667</a></td>
        <td>You have <strong>declined</strong> this event. Confirm this was intentional — Executive Roundtable events can be valuable for senior HR networking. If you wish to reverse this, respond to the organizer.</td>
      </tr>
      <tr>
        <td><strong>12:00 PM – 1:00 PM</strong></td>
        <td>HR Networking &amp; Job Search: Open Office Hours — Zoom 2</td>
        <td><span class="badge badge-yellow">Needs RSVP</span></td>
        <td><a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a></td>
        <td>⚠️ <strong>RSVP PENDING.</strong> Note: description says to turn off automated AI notetaking tools. Bring specific questions or job search challenges to discuss openly.</td>
      </tr>
    </tbody>
  </table>

  <!-- AUG 21-22 -->
  <div class="card card-gray" style="margin-bottom:8px;">
    <div class="card-title">📌 Friday, August 21 &amp; Saturday, August 22, 2026</div>
  </div>
  <table style="margin-bottom:16px;">
    <thead><tr><th>Time</th><th>Event</th><th>Status</th><th>Notes</th></tr></thead>
    <tbody>
      <tr><td colspan="4" style="color:#718096; font-style:italic;">No calendar events scheduled for Aug 21–22. Good time for job applications, LinkedIn outreach, or rest.</td></tr>
    </tbody>
  </table>

  <!-- AUG 23 -->
  <div class="card card-yellow" style="margin-bottom:8px;">
    <div class="card-title">📌 Sunday, August 23, 2026</div>
  </div>
  <table style="margin-bottom:16px;">
    <thead><tr><th>Time</th><th>Event</th><th>Status</th><th>Notes</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>All Day</strong></td>
        <td>💳 Verizon Fios Bill Due</td>
        <td><span class="badge badge-yellow">Confirmed</span></td>
        <td>Ensure payment is scheduled or auto-pay is active before this date.</td>
      </tr>
    </tbody>
  </table>

  <!-- AUG 24 -->
  <div class="card card-blue" style="margin-bottom:8px;">
    <div class="card-title">📌 Monday, August 24, 2026</div>
  </div>
  <table style="margin-bottom:16px;">
    <thead><tr><th>Time</th><th>Event</th><th>Status</th><th>Location / Link</th><th>Prep / Notes</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>All Day</strong></td>
        <td>🎂 Michael Rich's Birthday</td>
        <td><span class="badge badge-green">Noted</span></td>
        <td>—</td>
        <td>Send a birthday message or card today if you haven't already.</td>
      </tr>
      <tr>
        <td><strong>9:15 AM – 10:45 AM</strong></td>
        <td>✂️ Hair Appointment — Elle at UMI Salon <em>(also listed as "Elle" 9:15–10:15)</em></td>
        <td><span class="badge badge-green">Confirmed</span></td>
        <td>37 West 20th Suite 1107, New York, NY 10011</td>
        <td>Service: Single Process with Blowout with Elle M. ⚠️ Duplicate entry ("Elle" shows 9:15–10:15, confirmation shows 9:15–10:45) — actual end time is 10:45 AM per the salon confirmation. Manage appointment: https://elleatumi.glossgenius.com if changes needed.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 5 — JOB SEARCH & INTERVIEW PIPELINE
════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>

  <div class="alert-box alert-green">🟢 <strong>Active Search Mode:</strong> UI deposit confirmed ($760.38), job alerts active across LinkedIn, Glassdoor, and Inclusively. Two senior-level HR roles identified as strong fits today.</div>

  <table>
    <thead>
      <tr>
        <th>Fit</th>
        <th>Role / Company</th>
        <th>Source</th>
        <th>Status</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="pri-high">HIGH</span></td>
        <td><strong>VP, People Business Partners &amp; Talent Development</strong> — Clio (Legal AI, global leader)</td>
        <td>LinkedIn Job Alerts</td>
        <td>New Alert — Not Yet Applied</td>
        <td>Review &amp; apply today — senior role, fast-moving</td>
      </tr>
      <tr>
        <td><span class="pri-high">HIGH</span></td>
        <td><strong>People Business Partner Director, Engineering</strong> — Brex (Fintech)</td>
        <td>LinkedIn Job Alerts</td>
        <td>New Alert — Not Yet Applied</td>
        <td>Tailor resume to engineering HRBP focus this week</td>
      </tr>
      <tr>
        <td><span class="pri-medium">MEDIUM</span></td>
        <td><strong>HRBP &amp; multiple HR roles</strong> — Talkiatry, Brown &amp; Brown + 8 more (Remote)</td>
        <td>Glassdoor — in Trash</td>
        <td>Trashed — Not Reviewed</td>
        <td>Rescue from Trash if interested in remote HRBP roles</td>
      </tr>
      <tr>
        <td><span class="pri-medium">MEDIUM</span></td>
        <td><strong>Director, Community Cat Program</strong> — Flatbush Cats + 11 more NY roles</td>
        <td>Glassdoor — in Trash</td>
        <td>Trashed — likely non-match</td>
        <td>Low fit for senior HR; review only if curious about mission-driven orgs</td>
      </tr>
      <tr>
        <td><span class="pri-medium">MEDIUM</span></td>
        <td><strong>Recommended jobs</strong> — multiple roles via Inclusively platform</td>
        <td>Inclusively (Inbox)</td>
        <td>New — Unreviewed</td>
        <td>Review Inclusively recommendations — platform specializes in inclusive employers</td>
      </tr>
      <tr>
        <td><span class="pri-high">HIGH</span></td>
        <td><strong>Networking — Judy Boreham</strong> (New LinkedIn connection + message)</td>
        <td>LinkedIn</td>
        <td>Message Unread — Urgent</td>
        <td>Respond to Judy's message today; warm lead</td>
      </tr>
      <tr>
        <td><span class="pri-high">HIGH</span></td>
        <td><strong>HR Networking &amp; Job Search Group</strong> — 150+ HR professionals</td>
        <td>Calendar (Aug 19, Noon)</td>
        <td>RSVP Pending</td>
        <td>RSVP Yes today; prepare 30-second update</td>
      </tr>
      <tr>
        <td><span class="pri-medium">MEDIUM</span></td>
        <td><strong>1:1 with Monte Montoya</strong> (M&amp;m)</td>
        <td>Calendar (Aug 19, 2 PM)</td>
        <td>Accepted</td>
        <td>Confirm format; prepare job search update &amp; questions</td>
      </tr>
      <tr>
        <td><span class="pri-medium">MEDIUM</span></td>
        <td><strong>HR Open Office Hours</strong> — Networking group</td>
        <td>Calendar (Aug 20, Noon)</td>
        <td>RSVP Pending</td>
        <td>RSVP Yes; bring specific questions</td>
      </tr>
      <tr>
        <td><span class="pri-low">LOW</span></td>
        <td><strong>Claude 101 Workshop</strong> — AI skills training</td>
        <td>Zoom Confirmations + Outskill (Inbox)</td>
        <td>Registered — Date TBD</td>
        <td>Confirm workshop date from Zoom confirmation; add to calendar</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 6 — FULL EMAIL REVIEW BY CATEGORY
════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📂 Full Email Review by Category</div>

  <!-- SECURITY / RISK -->
  <div class="card card-red">
    <div class="card-title">🔐 Security / Risk — 13 emails</div>
    <div class="card-sub">Auto-trashed phishing (1), Google security alerts (4), explicit spam not in trash (7), fake payment alert (1 — auto-trashed)</div>
    <div class="card-body">
      <strong>Auto-Trashed (Phishing):</strong><br>
      • <em>Payment-System</em> — "URGENT: Renewal attempt failed" — Spoofed sender from random domain. Fake cloud storage renewal designed to harvest credentials. <span class="auto-trash-note">✅ Auto-trashed before delivery. No action needed.</span><br><br>
      <strong>Google Security Alerts (4 emails — legitimate):</strong><br>
      • <em>Google</em> — "Security alert — TuneMyMusic access" (×2 sent to melissaw212 + Melweiss212 recovery email)<br>
      • <em>Google</em> — "Security alert for melissaw212@gmail.com" (×2 copies)<br>
      → TuneMyMusic was granted access to your Google account. Verify at myaccount.google.com/permissions. Likely intentional as you signed up for TuneMyMusic today.<br><br>
      <strong>Explicit / Adult Spam — NOT in Trash (7 emails — DELETE IMMEDIATELY):</strong><br>
      • Sex.Pheromones — "Stroke this homemade mixture on for 13 seconds"<br>
      • 'Watch this Alone' (×2) — "Everyone's talking about this trick" / "Fix ED at home with this recipe"<br>
      • melissaw212 spoofed — "USE THE RAW SECRET TO FUCK HER FOR 4 HOURS STRAIGHT"<br>
      • Men's Health Advisory — "the real reason younger men stay hard so long"<br>
      • Get_Hard spoofed — "1 simple trick is turning men into unstoppable sex machines"<br>
      • Harvard Researcher spoofed — "Simple Recipe That's" (knee surgery/arthritis spam)<br>
      • Sex💊 — "The Special EXERCISE that Gives Porn Stars their Stamina"<br>
      → These are in non-trash folders. Mark as spam, block, delete all.
    </div>
    <div class="card-action">👉 Action: Mark all spam emails as spam → block senders → delete. Review Google app permissions. <span class="badge badge-red">URGENT — TODAY</span></div>
  </div>

  <!-- JOB SEARCH -->
  <div class="card card-green">
    <div class="card-title">💼 Job Search — 5 emails</div>
    <div class="card-sub">LinkedIn job alerts (×2 inbox), Glassdoor alerts (×2 trash), Inclusively recommendations (×1 inbox)</div>
    <div class="card-body">
      • <em>LinkedIn Job Alerts</em> — VP, People Business Partners &amp; Talent Development at Clio <span class="badge badge-green">HIGH FIT</span><br>
      • <em>LinkedIn Job Alerts</em> — People Business Partner Director, Engineering at Brex <span class="badge badge-green">HIGH FIT</span><br>
      • <em>Inclusively</em> — Recommended jobs for melissa weiss (inbox) — review platform <span class="badge badge-yellow">MEDIUM FIT</span><br>
      • <em>Glassdoor</em> (Trash) — HRBP at Talkiatry + 8 more remote roles <span class="badge badge-yellow">MEDIUM</span><br>
      • <em>Glassdoor</em> (Trash) — Director, Community Cat Program at Flatbush Cats + 11 more NY roles <span class="badge badge-gray">LOW</span>
    </div>
    <div class="card-action">👉 Action: Apply to Clio and Brex today. Review Inclusively. Consider rescuing Glassdoor HRBP email if remote roles are of interest.</div>
  </div>

  <!-- RECRUITERS / NETWORKING -->
  <div class="card card-green">
    <div class="card-title">🤝 Recruiters / Networking — 3 emails</div>
    <div class="card-sub">LinkedIn connection accepted, LinkedIn message received, LinkedIn digest (trashed)</div>
    <div class="card-body">
      • <em>Judy Boreham via LinkedIn</em> — Accepted your connection request (Inbox) ✅<br>
      • <em>Judy Boreham via LinkedIn</em> — Sent you a message — UNREAD (Inbox) ⚠️<br>
      • <em>LinkedIn</em> — Patrick Burnell and others share their thoughts (Trash — digest) — community solar IPP hiring mention
    </div>
    <div class="card-action">👉 Action: Respond to Judy Boreham's message today. Low priority: LinkedIn digest in trash can be deleted.</div>
  </div>

  <!-- CALENDAR / EVENTS -->
  <div class="card card-blue">
    <div class="card-title">📅 Calendar / Events — 3 emails</div>
    <div class="card-sub">Zoom workshop confirmations (×2), Outskill second-chance offer (×1)</div>
    <div class="card-body">
      • <em>Zoom</em> (×2) — "Congratulations! Your seat is reserved!" — Claude 101 Workshop registration confirmed for Melissa White (one in inbox, one archived). Duplicate confirmations — keep one.<br>
      • <em>Outskill</em> — "You missed the Claude Workshop… here's your second chance" (Inbox) — You are already registered per Zoom confirmations; this may be an upsell or for a different session.
    </div>
    <div class="card-action">👉 Action: Check Zoom confirmation for workshop date/time and add to calendar. Outskill email may be irrelevant if already registered — archive.</div>
  </div>

  <!-- MEDICAL / HEALTH -->
  <div class="card card-orange">
    <div class="card-title">🏥 Medical / Health — 0 standalone emails</div>
    <div class="card-sub">Vet appointment reflected in Calendar only — no medical emails received today.</div>
    <div class="card-body">Stella's vet appointment is on your calendar (10 AM–11 AM today). No health or medical emails in inbox.</div>
    <div class="card-action">👉 Action: Attend Stella's vet appointment this morning.</div>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="card card-yellow">
    <div class="card-title">💰 Financial / Billing — 1 email</div>
    <div class="card-sub">Bank of America UI deposit notification</div>
    <div class="card-body">
      • <em>Bank of America</em> — Direct deposit of <strong>$760.38</strong> from NYS DOL UI DD credited to Personal Checking/Savings Account ending 7471 on August 18, 2026.
    </div>
    <div class="card-action">👉 Action: Confirm amount matches expected UI payment. Update budget. Calendar note: Verizon Fios bill due Aug 23.</div>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="card card-purple">
    <div class="card-title">📚 Professional Development — 2 emails</div>
    <div class="card-sub">BambooHR HR Hub newsletter, Outskill Claude Workshop (dual-counted with Calendar)</div>
    <div class="card-body">
      • <em>BambooHR (Sadie)</em> — [HR Hub] Back-to-School Edition for HR Growth ✏️ — Monthly HR newsletter, not in trash. Relevant for an HR professional. <span class="badge badge-purple">KEEP</span><br>
      • <em>Tune My Music</em> (rescued from trash) — Welcome/onboarding email for music transfer service. Not strictly professional development but a legitimate service email. <span class="rescued-note">✅ Rescued from Trash — legitimate signup confirmation.</span>
    </div>
    <div class="card-action">👉 Action: Read BambooHR HR Hub when time permits. Tune My Music welcome — archive after reading.</div>
  </div>

  <!-- PERSONAL -->
  <div class="card card-purple">
    <div class="card-title">❤️ Personal — 5 emails</div>
    <div class="card-sub">Dating apps (×3), Spotify (rescued), self-sent ChatGPT link (trashed), personal draft (trashed)</div>
    <div class="card-body">
      • <em>Match</em> — Keith, 62, New York viewed your profile (Inbox)<br>
      • <em>Match</em> — Amir likes you (not in inbox but active notification)<br>
      • <em>OkCupid</em> — You have an Intro! (Inbox) — unread message waiting<br>
      • <em>Spotify</em> — Login code 306787 <span class="rescued-note">✅ Rescued from Trash — official Spotify domain, account security.</span><br>
      • <em>Melissa W (self)</em> — ChatGPT 5-Step Setup guide link (Trash) — self-sent reference<br>
      • <em>Melissa W (self)</em> — Personal draft/note (Trash) — partial message about past experiences with giving
    </div>
    <div class="card-action">👉 Action: Check OkCupid intro when ready. Review Match notifications. Spotify code is expired (20-min window) — no action needed.</div>
  </div>

  <!-- NEWSLETTERS -->
  <div class="card card-gray">
    <div class="card-title">📰 Newsletters / Subscriptions — 4 emails (all in trash or low-value)</div>
    <div class="card-sub">1% Better, Dylan's Diary, Daily Skimm, LinkedIn Posts Digest</div>
    <div class="card-body">
      • <em>1% Better</em> — "Meta Trial, Volcano Power, and Earning 13x More" (Trash)<br>
      • <em>Dylan's Diary</em> — "The 800 Pound Gorilla Nobody is Talking About" (Trash)<br>
      • <em>Daily Skimm</em> — "A divisive Trader Joe's ingredient" (Trash)<br>
      • <em>LinkedIn</em> — Patrick Burnell and others share thoughts (Trash)
    </div>
    <div class="card-action">👉 Action: All in Trash — delete. Consider unsubscribing from newsletters that consistently go unread.</div>
  </div>

  <!-- PROMOTIONAL / RETAIL -->
  <div class="card card-gray">
    <div class="card-title">🛍️ Promotional / Retail — 8 emails (all in trash)</div>
    <div class="card-sub">Kohl's ×2, YesStyle, Old Navy, Gap Factory, Amazon, Chick-fil-A, SlicethePie</div>
    <div class="card-body">All retail/promotional emails were in Trash. See Promotional / Retail Summary section below for full details.</div>
    <div class="card-action">👉 Action: All safe to delete from Trash. Unsubscribe from retailers you no longer shop.</div>
  </div>

  <!-- SAFE TO DELETE / IGNORE -->
  <div class="card card-gray">
    <div class="card-title">🗑 Safe to Delete / Ignore — 6 emails</div>
    <div class="card-sub">Trump fundraising (Trash), SlicethePie notification (Trash), duplicate Zoom confirmation (keep one), Google data-sharing notifications (routine, already read)</div>
    <div class="card-body">
      • <em>President Donald J. Trump</em> — Fundraising email (Trash) — delete<br>
      • <em>SlicethePie</em> — Nielsen Pulse earn $1.35 notification (Trash) — delete<br>
      • <em>Zoom</em> — Duplicate Claude 101 confirmation (×2 received — archive one)<br>
      • <em>Google</em> — "You shared Google Account data with Spotify" — routine, already read<br>
      • <em>Google</em> — "You shared Google Account data with TuneMyMusic" — routine, already read<br>
      • <em>Penis Growth Doctor</em> (×2 — one in Trash, one not) — adult spam, delete/block
    </div>
    <div class="card-action">👉 Action: Delete all. No follow-up required.</div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 7 — TRASH REVIEW
════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">🗑 Trash Review</div>

  <div class="alert-box alert-green">✅ <strong>Rescued from Trash (2 emails — already restored):</strong></div>
  <table style="margin-bottom:14px;">
    <thead><tr><th>Sender</th><th>Subject</th><th>Rescue Reason</th></tr></thead>
    <tbody>
      <tr>
        <td>Spotify (no-reply@alerts.spotify.com)</td>
        <td>306787 — Your Spotify login code</td>
        <td>Official Spotify domain; login verification code — account security email. Melissa was logging into Spotify.</td>
      </tr>
      <tr>
        <td>Tune My Music (hi@tunemymusic.com)</td>
        <td>Welcome to Tune My Music! 🎶</td>
        <td>Legitimate music transfer service welcome/confirmation. Melissa signed up for TuneMyMusic (corroborated by Google data-sharing alert).</td>
      </tr>
    </tbody>
  </table>

  <div class="alert-box alert-red">🚫 <strong>Auto-Trashed — Phishing (1 email):</strong></div>
  <table style="margin-bottom:14px;">
    <thead><tr><th>Sender</th><th>Subject</th><th>Reason</th></tr></thead>
    <tbody>
      <tr>
        <td>Payment-System &lt;429xxs0r40@y8mszaz3hw.us&gt;</td>
        <td>URGENT: Renewal attempt failed</td>
        <td>Spoofed "Payment-System" from random domain. Fake urgent cloud storage renewal failure alert designed to harvest credentials or payment info. Auto-trashed before delivery. No action needed.</td>
      </tr>
    </tbody>
  </table>

  <div class="alert-box alert-yellow">⚠️ <strong>Restore Immediately — 0 emails.</strong> Both restorable emails were already rescued.</div>

  <div style="margin-bottom:8px;"><strong>🔍 Review Before Deleting:</strong></div>
  <table style="margin-bottom:14px;">
    <thead><tr><th>Sender</th><th>Subject</th><th>Why Review</th></tr></thead>
    <tbody>
      <tr>
        <td>Glassdoor Jobs</td>
        <td>HRBP at Talkiatry + 8 more jobs (Remote)</td>
        <td>May contain relevant HR job leads — review if open to remote HRBP roles before deleting.</td>
      </tr>
      <tr>
        <td>Glassdoor Jobs</td>
        <td>Director, Community Cat Program at Flatbush Cats + 11 more NY roles</td>
        <td>Likely low fit for senior HR; scan briefly for any hidden senior roles before deleting.</td>
      </tr>
      <tr>
        <td>Melissa W (self-sent)</td>
        <td>The 5-Step ChatGPT Setup: Beginner to Real AI System</td>
        <td>Self-sent reference link. Review if you haven't already bookmarked the resource, then delete.</td>
      </tr>
      <tr>
        <td>Melissa W (self — no subject)</td>
        <td>[No subject — partial personal message draft]</td>
        <td>Personal draft/note — review if this was meant to be sent or saved somewhere. Snippet suggests it was a candid personal communication.</td>
      </tr>
    </tbody>
  </table>

  <div style="margin-bottom:8px;"><strong>✅ Safe to Delete from Trash:</strong></div>
  <table>
    <thead><tr><th>Sender</th><th>Subject / Theme</th><th>Reason</th></tr></thead>
    <tbody>
      <tr><td>1% Better Newsletter</td><td>Meta Trial, Volcano Power, 13x More</td><td>Newsletter — consistently unread, in trash. Delete &amp; unsubscribe.</td></tr>
      <tr><td>Dylan's Diary Newsletter</td><td>The 800 Pound Gorilla Nobody is Talking About</td><td>Newsletter — in trash. Delete &amp; unsubscribe.</td></tr>
      <tr><td>Daily Skimm</td><td>A divisive Trader Joe's ingredient</td><td>Newsletter — in trash. Delete &amp; unsubscribe if not reading.</td></tr>
      <tr><td>Kohl's (×2)</td><td>Intimates Sale / Pick up where you left off</td><td>Retail promotional. Delete.</td></tr>
      <tr><td>YesStyle</td><td>COSRX Week discounts + FREE gifts</td><td>Retail promotional. Delete.</td></tr>
      <tr><td>Old Navy</td><td>Cardi B Fall Denim + 60% off tees</td><td>Retail promotional. Delete.</td></tr>
      <tr><td>Gap Factory</td><td>Extra 50% off clearance</td><td>Retail promotional. Delete.</td></tr>
      <tr><td>Amazon</td><td>The latest from TandTTwintalk</td><td>Amazon storefront digest. Delete.</td></tr>
      <tr><td>Chick-fil-A</td><td>A little thing… from us to you (reward)</td><td>Loyalty reward email. Delete if not planning to use.</td></tr>
      <tr><td>SlicethePie</td><td>Melissa, you have a notification — Nielsen Pulse $1.35</td><td>Survey site notification. Delete.</td></tr>
      <tr
