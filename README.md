<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa W. — September 2, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px 60px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 16px; padding: 36px 40px 28px; margin-bottom: 24px; box-shadow: 0 6px 24px rgba(0,0,0,0.22); }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header .subtitle { font-size: 14px; color: #a8c0e8; margin-top: 4px; }
  .header .meta { display: flex; gap: 28px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.08); border-radius: 8px; padding: 8px 16px; }
  .header .meta-item span { font-size: 11px; color: #a8c0e8; display: block; }
  .header .meta-item strong { font-size: 18px; color: #e8f4fd; }

  /* SECTION TITLES */
  .section-title { font-size: 13px; font-weight: 700; letter-spacing: 1.4px; text-transform: uppercase; color: #fff; padding: 8px 16px; border-radius: 8px 8px 0 0; margin-bottom: 0; }
  .section-wrap { border-radius: 12px; overflow: hidden; margin-bottom: 24px; box-shadow: 0 2px 12px rgba(0,0,0,0.08); }
  .section-body { background: #fff; padding: 20px 22px; border-radius: 0 0 12px 12px; }

  .title-red { background: #c0392b; }
  .title-yellow { background: #d4a017; }
  .title-blue { background: #2471a3; }
  .title-green { background: #1e8449; }
  .title-purple { background: #6c3483; }
  .title-gray { background: #5d6d7e; }
  .title-dark { background: #1a1a2e; }
  .title-teal { background: #0e7490; }

  /* EXECUTIVE SUMMARY */
  .exec-bullets { list-style: none; padding: 0; }
  .exec-bullets li { display: flex; gap: 12px; align-items: flex-start; padding: 10px 0; border-bottom: 1px solid #f0f0f0; }
  .exec-bullets li:last-child { border-bottom: none; }
  .bullet-icon { font-size: 20px; flex-shrink: 0; }
  .bullet-text strong { display: block; font-size: 13px; color: #333; }
  .bullet-text span { font-size: 13px; color: #555; }

  /* ACTION CARDS */
  .action-cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; }
  .card { border-radius: 10px; padding: 16px 18px; border-left: 5px solid; }
  .card-red { background: #fdf2f2; border-color: #c0392b; }
  .card-yellow { background: #fefce8; border-color: #d4a017; }
  .card-green { background: #f0faf4; border-color: #1e8449; }
  .card-blue { background: #eaf4fb; border-color: #2471a3; }
  .card-purple { background: #f9f3ff; border-color: #6c3483; }
  .card-gray { background: #f7f8f9; border-color: #95a5a6; }
  .card-label { font-size: 10px; font-weight: 800; letter-spacing: 1.2px; text-transform: uppercase; margin-bottom: 6px; }
  .label-red { color: #c0392b; }
  .label-yellow { color: #b7800a; }
  .label-green { color: #1e8449; }
  .label-blue { color: #2471a3; }
  .label-purple { color: #6c3483; }
  .label-gray { color: #5d6d7e; }
  .card h4 { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
  .card .card-source { font-size: 11px; color: #888; margin-bottom: 6px; }
  .card p { font-size: 13px; color: #444; margin-bottom: 6px; }
  .card .card-action { font-size: 12px; font-weight: 600; color: #1a1a2e; background: rgba(0,0,0,0.06); border-radius: 5px; padding: 4px 8px; display: inline-block; margin-top: 4px; }
  .card .card-due { font-size: 11px; color: #888; margin-top: 4px; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #f0f2f5; font-size: 11px; font-weight: 700; letter-spacing: 0.8px; text-transform: uppercase; color: #555; padding: 9px 12px; text-align: left; border-bottom: 2px solid #e0e0e0; }
  td { padding: 9px 12px; border-bottom: 1px solid #f0f0f0; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #fafbfc; }
  .badge { display: inline-block; border-radius: 5px; padding: 2px 8px; font-size: 11px; font-weight: 700; }
  .badge-red { background: #fde8e8; color: #c0392b; }
  .badge-yellow { background: #fef9e7; color: #b7800a; }
  .badge-green { background: #e9f7ef; color: #1e8449; }
  .badge-blue { background: #eaf4fb; color: #1a5276; }
  .badge-purple { background: #f5eef8; color: #6c3483; }
  .badge-gray { background: #f0f0f0; color: #555; }
  .badge-orange { background: #fef0e6; color: #ca6f1e; }

  /* CALENDAR */
  .day-block { margin-bottom: 18px; }
  .day-header { font-size: 13px; font-weight: 800; color: #1a1a2e; background: #eaf4fb; border-radius: 7px; padding: 7px 14px; margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }
  .day-today { background: #d4efff; }
  .event-row { background: #fff; border: 1px solid #e8edf2; border-radius: 8px; padding: 12px 16px; margin-bottom: 8px; display: flex; gap: 14px; align-items: flex-start; }
  .event-time { font-size: 12px; font-weight: 700; color: #2471a3; min-width: 90px; }
  .event-content { flex: 1; }
  .event-title { font-size: 14px; font-weight: 700; color: #1a1a2e; }
  .event-meta { font-size: 12px; color: #666; margin-top: 2px; }
  .event-status { font-size: 11px; margin-top: 4px; }
  .event-prep { font-size: 12px; color: #555; margin-top: 4px; background: #f9f9f9; border-radius: 5px; padding: 4px 8px; }
  .conflict-warn { font-size: 11px; color: #c0392b; font-weight: 700; margin-top: 4px; }

  /* TRIAGE TABLE */
  .triage-status { font-size: 12px; white-space: nowrap; }
  .triage-from { font-size: 12px; color: #333; }
  .triage-subject { font-size: 12px; font-weight: 600; }
  .triage-summary { font-size: 12px; color: #555; }

  /* DASHBOARD GRID */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-card { border-radius: 10px; padding: 16px; text-align: center; }
  .dash-card .dash-num { font-size: 32px; font-weight: 800; }
  .dash-card .dash-label { font-size: 12px; margin-top: 4px; font-weight: 600; }
  .dash-red { background: #fde8e8; color: #c0392b; }
  .dash-yellow { background: #fefce8; color: #b7800a; }
  .dash-green { background: #e9f7ef; color: #1e8449; }
  .dash-blue { background: #eaf4fb; color: #1a5276; }
  .dash-purple { background: #f5eef8; color: #6c3483; }
  .dash-gray { background: #f7f8f9; color: #555; }

  /* PRIORITY TABLE */
  .priority-high { color: #c0392b; font-weight: 800; }
  .priority-medium { color: #d4a017; font-weight: 700; }
  .priority-low { color: #1e8449; font-weight: 600; }

  /* TOP 3 */
  .top3 { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; }
  .top3-card { border-radius: 12px; padding: 20px; color: #fff; position: relative; }
  .top3-card .num { font-size: 48px; font-weight: 900; opacity: 0.15; position: absolute; top: 8px; right: 16px; }
  .top3-card h3 { font-size: 16px; font-weight: 800; margin-bottom: 8px; }
  .top3-card p { font-size: 13px; opacity: 0.92; }
  .top3-1 { background: linear-gradient(135deg,#c0392b,#e74c3c); }
  .top3-2 { background: linear-gradient(135deg,#1e8449,#27ae60); }
  .top3-3 { background: linear-gradient(135deg,#1a5276,#2471a3); }

  .divider { height: 1px; background: #e8edf2; margin: 18px 0; }
  .note { font-size: 12px; color: #888; font-style: italic; }
  .tag { display: inline-block; font-size: 10px; font-weight: 700; letter-spacing: 0.7px; padding: 2px 7px; border-radius: 4px; margin-left: 6px; }
  .tag-rescued { background: #dff0d8; color: #1e8449; }
  .tag-phishing { background: #fde8e8; color: #c0392b; }
  .tag-newsletter { background: #f5eef8; color: #6c3483; }
  .tag-inbox { background: #eaf4fb; color: #1a5276; }

  a { color: #2471a3; }
  ul.plain { list-style: none; padding: 0; }
  ul.plain li { padding: 4px 0; border-bottom: 1px solid #f5f5f5; font-size: 13px; }
  ul.plain li:last-child { border-bottom: none; }

  .cat-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px; }
  .cat-count { font-size: 11px; font-weight: 800; letter-spacing: 0.8px; text-transform: uppercase; }

  .footer { text-align: center; color: #aaa; font-size: 11px; margin-top: 40px; }
</style>
</head>
<body>
<div class="page">

<!-- ============================================================
     SECTION 0: EMAIL TRIAGE QUICK LIST
     ============================================================ -->
<div class="section-wrap">
  <div class="section-title title-dark">📋 Email Triage Quick List — September 2, 2026</div>
  <div class="section-body">
    <p class="note" style="margin-bottom:12px;">Inbox & rescued emails shown individually. Trashed emails collapsed to summary rows. Rescued emails appear first.</p>
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
        <!-- RESCUED -->
        <tr>
          <td class="triage-status"><span class="badge badge-green">✅ RESCUED</span></td>
          <td class="triage-from">LinkedIn Job Alerts</td>
          <td class="triage-subject">Senior Director, People Partnerships at Ladders and 13 more</td>
          <td class="triage-summary">$180K–$230K salary range. Rescued: protected sender — always keep in inbox.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="badge badge-green">✅ RESCUED</span></td>
          <td class="triage-from">Notify NYC</td>
          <td class="triage-subject">MTA Disruption — A &amp; C Trains (MN/BK)</td>
          <td class="triage-summary">Switch malfunction causing delays on A &amp; C lines. Actionable transit info — rescued from trash.</td>
        </tr>
        <!-- INBOX -->
        <tr>
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">Bank of America</td>
          <td class="triage-subject">Billing Dispute for account -2994 — Important update to your claim</td>
          <td class="triage-summary">Step 2 of 3 billing dispute update for account ending 2994. ⚠️ Requires review.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">Silvana Chumaceiro (LinkedIn)</td>
          <td class="triage-subject">Global People Partner Opportunity | Interview Invitation</td>
          <td class="triage-summary">Recruiter interview invitation for Global People Partner role. Action required.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">LinkedIn Job Alerts</td>
          <td class="triage-subject">Vice President, Human Resources at Jobgether and 19 more</td>
          <td class="triage-summary">VP HR and related roles — 20 listings. High-value job search batch.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">LinkedIn Job Alerts</td>
          <td class="triage-subject">Chief Human Resources Officer at Ladders and 39 more</td>
          <td class="triage-summary">CHRO role $207K–$304K + 39 more. Top-tier opportunity batch.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">LinkedIn Job Alerts</td>
          <td class="triage-subject">HR Business Partner at Point72 and 39 more</td>
          <td class="triage-summary">HRBP at Point72 (hedge fund) + 39 more. Notable employer.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">Amazon.com</td>
          <td class="triage-subject">Ordered: 1 Cosmetics item</td>
          <td class="triage-summary">Order confirmation for cosmetics item placed early this morning.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">Amazon.com</td>
          <td class="triage-subject">Shipped: 1 Cosmetics item</td>
          <td class="triage-summary">Cosmetics order has shipped. Track delivery.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">Marcus by Goldman Sachs</td>
          <td class="triage-subject">Your monthly Marcus Savings account statement is now available</td>
          <td class="triage-summary">Monthly savings statement ready to review at marcus.com.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">Apify Billing</td>
          <td class="triage-subject">Apify invoice #202609021150 payment successful</td>
          <td class="triage-summary">$31.58 Apify payment confirmed. No action needed — log for records.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">Match</td>
          <td class="triage-subject">You've had a profile view from John</td>
          <td class="triage-summary">John, 61, Montclair NJ viewed Melissa's Match profile.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">Melissa W (self)</td>
          <td class="triage-subject">How I Built an Animated GitHub Profile README</td>
          <td class="triage-summary">Self-sent link: Animated GitHub README tutorial by Avi Vashishta.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">SHEIN</td>
          <td class="triage-subject">Delay notice</td>
          <td class="triage-summary">Possible SHEIN order delay notification — check if order is pending.</td>
        </tr>
        <!-- AUTO-TRASHED SUMMARY ROW -->
        <tr style="background:#fff8f8;">
          <td class="triage-status"><span class="badge badge-red">🗑 AUTO-TRASHED</span></td>
          <td colspan="2" class="triage-subject">5 emails auto-trashed (phishing/spam) — see Trash Review &amp; Security / Risk</td>
          <td class="triage-summary">Cloud storage spoofs ×3, Casino spam ×2. Removed before inbox. 1 newsletter auto-trashed (Gap Factory).</td>
        </tr>
        <!-- MANUAL TRASH SUMMARY ROW -->
        <tr style="background:#f9f9f9;">
          <td class="triage-status"><span class="badge badge-gray">🗂 TRASH</span></td>
          <td colspan="2" class="triage-subject">30 emails in Trash (manual) — see Trash Review</td>
          <td class="triage-summary">Includes newsletters, retail promos, social media, and unsolicited casino/spam messages.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ============================================================
     SECTION 1: HEADER
     ============================================================ -->
<div class="header">
  <h1>Good morning, Melissa 👋</h1>
  <div class="subtitle">Executive Briefing prepared by your Chief of Staff</div>
  <div class="meta">
    <div class="meta-item"><span>Date</span><strong>Wednesday, September 2, 2026</strong></div>
    <div class="meta-item"><span>Total Emails Reviewed</span><strong>50</strong></div>
    <div class="meta-item"><span>Calendar Events</span><strong>7</strong></div>
    <div class="meta-item"><span>Action Required</span><strong>6 Items</strong></div>
  </div>
</div>

<!-- ============================================================
     SECTION 2: EXECUTIVE SUMMARY
     ============================================================ -->
<div class="section-wrap">
  <div class="section-title title-dark">⚡ Executive Summary</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li>
        <span class="bullet-icon">🔴</span>
        <div class="bullet-text">
          <strong>Security Risk: Multiple Phishing &amp; Spam Emails in Your Inbox</strong>
          <span>5 emails were auto-trashed as high-confidence phishing (cloud storage spoofs, casino scams). Additionally, 3 casino spam emails and 1 fake ESA letter email remain untrashed. Your Bank of America billing dispute (account -2994) also needs review — confirm it is legitimate before clicking any links.</span>
        </div>
      </li>
      <li>
        <span class="bullet-icon">🟢</span>
        <div class="bullet-text">
          <strong>Job Search Priority: Interview Invitation + 4 High-Value LinkedIn Alert Batches</strong>
          <span>Silvana Chumaceiro sent a LinkedIn InMail interview invitation for a Global People Partner role — respond today. Four LinkedIn Job Alert batches include CHRO ($207K–$304K), VP HR, Senior Director People Partnerships ($180K–$230K), and HRBP at Point72 — review all today.</span>
        </div>
      </li>
      <li>
        <span class="bullet-icon">🔵</span>
        <div class="bullet-text">
          <strong>Calendar: HR Networking Zoom Today at Noon + Coaching Call Tomorrow</strong>
          <span>HR Networking &amp; Job Search Group Zoom is today 12:00–1:30 PM (RSVP still needed). Tomorrow: coaching session with Rita Ramakrishnan 10:00–10:45 AM (accepted) and Executive Roundtable at 9 AM (declined — no conflict). State Farm bill due Sept 7.</span>
        </div>
      </li>
    </ul>
  </div>
</div>

<!-- ============================================================
     SECTION 3: ACTION REQUIRED
     ============================================================ -->
<div class="section-wrap">
  <div class="section-title title-yellow">⚠️ Action Required</div>
  <div class="section-body">
    <div class="action-cards">

      <div class="card card-red">
        <div class="card-label label-red">🔴 Security / Risk</div>
        <h4>Bank of America Billing Dispute Update</h4>
        <div class="card-source">From: onlinebanking@ealerts.bankofamerica.com</div>
        <p>Step 2 of 3 billing dispute update for account ending -2994, updated September 2. This appears to be from a legitimate BofA alerts domain — but verify before clicking any links.</p>
        <span class="card-action">➡ Log into bankofamerica.com directly to check dispute status</span>
        <div class="card-due">Due: Today — dispute in progress</div>
      </div>

      <div class="card card-green">
        <div class="card-label label-green">🟢 Job Search — Urgent</div>
        <h4>Interview Invitation: Global People Partner</h4>
        <div class="card-source">From: Silvana Chumaceiro via LinkedIn InMail</div>
        <p>Recruiter has extended an interview invitation for a Global People Partner opportunity. Unread — response window may be limited.</p>
        <span class="card-action">➡ Reply to LinkedIn InMail today to confirm interview interest</span>
        <div class="card-due">Due: Today, September 2</div>
      </div>

      <div class="card card-blue">
        <div class="card-label label-blue">🔵 Calendar — RSVP Needed</div>
        <h4>HR Networking &amp; Job Search Group — Zoom (TODAY)</h4>
        <div class="card-source">Calendar Event — 12:00–1:30 PM ET</div>
        <p>RSVP status is "needsAction" — you have not confirmed. The Zoom session starts at noon today. Large group (~170+ attendees).</p>
        <span class="card-action">➡ Accept or decline the calendar invite immediately</span>
        <div class="card-due">Due: Before 12:00 PM today</div>
      </div>

      <div class="card card-yellow">
        <div class="card-label label-yellow">🟡 Financial / Billing</div>
        <h4>Marcus Savings Monthly Statement Available</h4>
        <div class="card-source">From: Marcus by Goldman Sachs</div>
        <p>Your September statement is ready to view or download at marcus.com or via the app. Good habit to review monthly.</p>
        <span class="card-action">➡ Log into marcus.com to review your statement</span>
        <div class="card-due">No deadline — available now</div>
      </div>

      <div class="card card-yellow">
        <div class="card-label label-yellow">🟡 Financial / Billing — Upcoming Deadline</div>
        <h4>State Farm Bill Due September 7</h4>
        <div class="card-source">Google Calendar — All-day event</div>
        <p>State Farm bill due in 5 days. Ensure payment is scheduled or initiated before the due date.</p>
        <span class="card-action">➡ Pay or verify auto-pay is set up for State Farm</span>
        <div class="card-due">Due: Monday, September 7</div>
      </div>

      <div class="card card-red">
        <div class="card-label label-red">🔴 Security — Spam Cleanup Needed</div>
        <h4>Untrashed Casino / Phishing Emails Still in Mailbox</h4>
        <div class="card-source">Multiple senders — not auto-trashed</div>
        <p>Several casino spam emails (Betty Wins Casino, Casino_Special, CashApp fake, Limitless Casino, Congratulations/Yabby, ESA Letter) were not caught by auto-trash and remain in your mailbox. These should be deleted and senders blocked.</p>
        <span class="card-action">➡ Delete all and block senders — do not click any links</span>
        <div class="card-due">Due: Today</div>
      </div>

    </div>
  </div>
</div>

<!-- ============================================================
     SECTION 4: FULL 7-DAY CALENDAR
     ============================================================ -->
<div class="section-wrap">
  <div class="section-title title-blue">📅 Full 7-Day Calendar</div>
  <div class="section-body">

    <!-- TODAY -->
    <div class="day-block">
      <div class="day-header day-today">📍 TODAY — Wednesday, September 2, 2026</div>

      <div class="event-row">
        <div class="event-time">12:00 PM<br>– 1:30 PM</div>
        <div class="event-content">
          <div class="event-title">HR Networking &amp; Job Search Group — Zoom Session 2</div>
          <div class="event-meta">👥 ~170+ attendees | 📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a></div>
          <div class="event-status"><span class="badge badge-yellow">⚠️ RSVP: NeedsAction</span></div>
          <div class="event-prep">📝 Prep: Review HR Networking Team Guidelines linked in invite. Prepare brief intro and 1–2 job search updates to share. Check agenda in description link.</div>
        </div>
      </div>

      <div class="event-row">
        <div class="event-time">12:00 PM<br>– 1:30 PM</div>
        <div class="event-content">
          <div class="event-title">Network (personal block)</div>
          <div class="event-meta">👤 No attendees listed | No location set</div>
          <div class="event-status"><span class="badge badge-green">✅ Status: Confirmed</span></div>
          <div class="event-prep">📝 Note: Time block overlaps with HR Networking Zoom above — likely intentional as a paired reminder block. No separate action needed.</div>
          <div class="conflict-warn">⚠️ Conflict: Same timeslot as HR Networking Zoom — likely intentional pairing.</div>
        </div>
      </div>
    </div>

    <!-- THURSDAY -->
    <div class="day-block">
      <div class="day-header">📅 Thursday, September 3, 2026</div>

      <div class="event-row">
        <div class="event-time">9:00 AM<br>– 10:30 AM</div>
        <div class="event-content">
          <div class="event-title">Executive Roundtable</div>
          <div class="event-meta">👤 Hosted by John Madigan | 📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> | Meeting ID: 207 786 667 | PW: 205454</div>
          <div class="event-status"><span class="badge badge-red">❌ Status: Declined</span></div>
          <div class="event-prep">📝 No prep needed — you have declined. No conflict with 10 AM meeting (30-min gap).</div>
        </div>
      </div>

      <div class="event-row">
        <div class="event-time">10:00 AM<br>– 10:45 AM</div>
        <div class="event-content">
          <div class="event-title">Coaching Session: Melissa Weiss &amp; Rita Ramakrishnan</div>
          <div class="event-meta">👤 rita@iksana.com | 📍 Google Meet (link in description via Calendly)</div>
          <div class="event-status"><span class="badge badge-green">✅ Status: Accepted</span></div>
          <div class="event-prep">📝 Prep: Existing coaching/consulting client session — 45 minutes. Prepare updates on job search progress, recent interviews, and any strategic questions. Have your LinkedIn profile and target role list ready.</div>
        </div>
      </div>

      <div class="event-row">
        <div class="event-time">12:00 PM<br>– 1:00 PM</div>
        <div class="event-content">
          <div class="event-title">HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
          <div class="event-meta">👥 ~170+ attendees | 📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a></div>
          <div class="event-status"><span class="badge badge-yellow">⚠️ RSVP: NeedsAction</span></div>
          <div class="event-prep">📝 Prep: Open discussion — NO automated AI notetaking tools allowed per organizer. Bring specific questions or topics. Good opportunity for 1:1 connection leads. RSVP decision needed.</div>
        </div>
      </div>
    </div>

    <!-- FRIDAY -->
    <div class="day-block">
      <div class="day-header">📅 Friday, September 4, 2026</div>
      <div class="event-row">
        <div class="event-time">All Day</div>
        <div class="event-content">
          <div class="event-title">No Events Scheduled</div>
          <div class="event-meta" style="color:#aaa;">Free day — use for job applications, follow-ups, or networking.</div>
        </div>
      </div>
    </div>

    <!-- SATURDAY -->
    <div class="day-block">
      <div class="day-header">📅 Saturday, September 5, 2026</div>
      <div class="event-row">
        <div class="event-time">All Day</div>
        <div class="event-content">
          <div class="event-title">No Events Scheduled</div>
          <div class="event-meta" style="color:#aaa;">Weekend — personal time.</div>
        </div>
      </div>
    </div>

    <!-- SUNDAY -->
    <div class="day-block">
      <div class="day-header">📅 Sunday, September 6, 2026</div>
      <div class="event-row">
        <div class="event-time">All Day</div>
        <div class="event-content">
          <div class="event-title">No Events Scheduled</div>
          <div class="event-meta" style="color:#aaa;">Weekend — personal time.</div>
        </div>
      </div>
    </div>

    <!-- MONDAY -->
    <div class="day-block">
      <div class="day-header">📅 Monday, September 7, 2026 — Labor Day</div>
      <div class="event-row">
        <div class="event-time">All Day</div>
        <div class="event-content">
          <div class="event-title">⚡ State Farm Bill Due</div>
          <div class="event-meta">💳 All-day deadline | No location</div>
          <div class="event-status"><span class="badge badge-yellow">⚠️ Billing Deadline</span></div>
          <div class="event-prep">📝 Action: Confirm payment has been made or auto-pay is active. Banks may be closed for Labor Day — process in advance.</div>
        </div>
      </div>
    </div>

    <!-- TUESDAY -->
    <div class="day-block">
      <div class="day-header">📅 Tuesday, September 8, 2026</div>
      <div class="event-row">
        <div class="event-time">10:00 AM<br>– 11:00 AM</div>
        <div class="event-content">
          <div class="event-title">💅 Nails Appointment</div>
          <div class="event-meta">📍 Location not specified | Confirmed</div>
          <div class="event-status"><span class="badge badge-green">✅ Status: Confirmed</span></div>
          <div class="event-prep">📝 Confirm salon appointment address if needed. Allow travel time.</div>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- ============================================================
     SECTION 5: JOB SEARCH & INTERVIEW PIPELINE
     ============================================================ -->
<div class="section-wrap">
  <div class="section-title title-green">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">
    <table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Source / Sender</th>
          <th>Role / Details</th>
          <th>Fit</th>
          <th>Status / Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="badge badge-red">🎯 Interview Invite</span></td>
          <td>Silvana Chumaceiro<br><span style="font-size:11px;color:#888">via LinkedIn InMail</span></td>
          <td>Global People Partner Opportunity</td>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>⚠️ <strong>Unread — Reply Today.</strong> Confirm interest and propose interview times.</td>
        </tr>
        <tr>
          <td><span class="badge badge-green">📋 Job Alerts</span></td>
          <td>LinkedIn Job Alerts</td>
          <td>Chief Human Resources Officer at Ladders + 39 more<br><span style="font-size:11px;color:#888">$207K–$304K / year</span></td>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>Review batch — CHRO at top salary range. Apply to top matches today.</td>
        </tr>
        <tr>
          <td><span class="badge badge-green">📋 Job Alerts</span></td>
          <td>LinkedIn Job Alerts</td>
          <td>Vice President, Human Resources at Jobgether + 19 more</td>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>VP HR listings. Review for fit. Jobgether is a remote-first platform.</td>
        </tr>
        <tr>
          <td><span class="badge badge-green">📋 Job Alerts</span></td>
          <td>LinkedIn Job Alerts <span class="tag tag-rescued">✅ RESCUED</span></td>
          <td>Senior Director, People Partnerships at Ladders + 13 more<br><span style="font-size:11px;color:#888">$180K–$230K / year</span></td>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>Rescued from Trash (protected sender). Strong salary range. Review today.</td>
        </tr>
        <tr>
          <td><span class="badge badge-green">📋 Job Alerts</span></td>
          <td>LinkedIn Job Alerts</td>
          <td>HR Business Partner at Point72 + 39 more</td>
          <td><span class="badge badge-orange">MEDIUM</span></td>
          <td>Point72 (hedge fund) HRBP is a notable employer. Review batch for fit.</td>
        </tr>
        <tr>
          <td><span class="badge badge-blue">🤝 Networking</span></td>
          <td>Google Calendar</td>
          <td>HR Networking &amp; Job Search Group — Zoom (Today, 12–1:30 PM)</td>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>⚠️ RSVP needed. 170+ HR professionals. High-value networking opportunity.</td>
        </tr>
        <tr>
          <td><span class="badge badge-blue">🤝 Networking</span></td>
          <td>Google Calendar</td>
          <td>HR Networking: Open Office Hours — Zoom (Sept 3, 12–1 PM)</td>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>⚠️ RSVP needed. Casual discussion — no AI notetakers. Good for 1:1 connections.</td>
        </tr>
        <tr>
          <td><span class="badge badge-purple">🧑‍💼 Coaching</span></td>
          <td>Google Calendar — Rita Ramakrishnan</td>
          <td>45-Min Coaching Session (Sept 3, 10–10:45 AM) via Google Meet</td>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>Confirmed. Prepare job search updates, questions, and goals for session.</td>
        </tr>
        <tr>
          <td><span class="badge badge-blue">🔗 LinkedIn</span></td>
          <td>LinkedIn Network</td>
          <td>Anvith Murthy, Founder — Popular in your network</td>
          <td><span class="badge badge-gray">LOW</span></td>
          <td>In Trash. Low priority — review if building founder network, otherwise ignore.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ============================================================
     SECTION 6: FULL EMAIL REVIEW BY CATEGORY
     ============================================================ -->
<div class="section-wrap">
  <div class="section-title title-dark">📂 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div style="margin-bottom:20px;">
      <div class="cat-header">
        <strong style="color:#c0392b;">🔴 Security / Risk</strong>
        <span class="cat-count badge badge-red">10 emails</span>
      </div>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>melissaw212 &lt;alert-7590@gdolh.ihi&gt;</td><td>🚨 Action Required: Storage 100% Full</td><td><span class="badge badge-red">AUTO-TRASHED — Phishing</span></td><td>Spoofed sender using victim's own username with random domain — credential harvest. Removed automatically. No further action.</td></tr>
          <tr><td>melissaw212 &lt;ksbpcinbjvh@lazl.jwomenazwfzwf.us&gt;</td><td>Your Cloud ID has been locked (Wed, 02 Sep 2026)</td><td><span class="badge badge-red">AUTO-TRASHED — Phishing</span></td><td>Spoofed sender, fake cloud ID lock/photos deleted urgency — credential harvest. Removed automatically. No further action.</td></tr>
          <tr><td>Cloud-Storage &lt;qzeh16xewx@bfjmeapkbg.us&gt;</td><td>FINAL NOTICE: Your photos will be deleted tonight</td><td><span class="badge badge-red">AUTO-TRASHED — Phishing</span></td><td>Fake cloud storage final notice — credential harvest. Removed automatically. No further action.</td></tr>
          <tr><td>melissaw212 &lt;bpkjnkdwqxz@xzwr.bmzrottwkqbjy.us&gt;</td><td>Your Cloud ID has been locked (Tue, 01 Sep 2026)</td><td><span class="badge badge-red">Phishing — Not Auto-Trashed</span></td><td>Same spoofed cloud storage scam. DELETE immediately. Block sender domain.</td></tr>
          <tr><td>'melissaw212' &lt;ehajeuekwebpfa...@pgx8bo...us&gt;</td><td>You received a direct deposited of $13,963.99 (Limitless Casino)</td><td><span class="badge badge-red">Spam — Not Trashed</span></td><td>Fake casino deposit scam. DELETE. Block sender.</td></tr>
          <tr><td>Betty Wins Casino</td><td>Payment Confirmation: $2,000.00 Deposit Sent to melissaw212</td><td><span class="badge badge-red">Spam — Not Trashed</span></td><td>Fake casino payment scam. DELETE. Block sender.</td></tr>
          <tr><td>Casino_Special &lt;qfsupportjld@...&gt;</td><td>You Won $7000.00 Claim Your Prize Now melissaw212</td><td><span class="badge badge-red">Spam — Not Trashed</span></td><td>Fake prize/casino scam. DELETE. Block sender.</td></tr>
          <tr><td>'CashApp' (fake)</td><td>You have received $15.99 in your account — Raging Bull Casino</td><td><span class="badge badge-red">Spam — Not Trashed</span></td><td>Fake CashApp casino spam. DELETE. Block sender.</td></tr>
          <tr><td>Congratulations 🎉 &lt;vnpiccxdgqv@lxss...&gt;</td><td>175 Free Spins Pending in your Account</td><td><span class="badge badge-red">Spam — Not Trashed</span></td><td>Fake casino free spins. DELETE. Block sender.</td></tr>
          <tr><td>Bank of America</td><td>Billing Dispute for account -2994 — Important update to your claim</td><td><span class="badge badge-yellow">⚠️ Legitimate — Review</span></td><td>Appears legitimate (ealerts.bankofamerica.com). Log into BofA directly to verify dispute status. Do NOT click email links.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="divider"></div>

    <!-- JOB SEARCH -->
    <div style="margin-bottom:20px;">
      <div class="cat-header">
        <strong style="color:#1e8449;">🟢 Job Search</strong>
        <span class="cat-count badge badge-green">5 emails</span>
      </div>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Location</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Silvana Chumaceiro (LinkedIn InMail)</td><td>Global People Partner Opportunity | Interview Invitation</td><td>Inbox</td><td>⚠️ Reply today — interview invite pending.</td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>Chief Human Resources Officer at Ladders + 39 more ($207K–$304K)</td><td>Inbox</td><td>Review batch — top salary range. Apply to best fits.</td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>Vice President, Human Resources at Jobgether + 19 more</td><td>Inbox</td><td>Review VP HR listings.</td></tr>
          <tr><td>LinkedIn Job Alerts <span class="tag tag-rescued">✅ RESCUED</span></td><td>Senior Director, People Partnerships at Ladders + 13 more ($180K–$230K)</td><td>Rescued from Trash</td><td>Rescued — protected sender. Review today.</td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>HR Business Partner at Point72 + 39 more</td><td>Inbox</td><td>Notable employer (Point72). Review batch.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="divider"></div>

    <!-- RECRUITERS / NETWORKING -->
    <div style="margin-bottom:20px;">
      <div class="cat-header">
        <strong style="color:#2471a3;">🔵 Recruiters / Networking</strong>
        <span class="cat-count badge badge-blue">1 email</span>
      </div>
      <ul class="plain">
        <li>LinkedIn — Anvith Murthy, Founder, is popular in your network (In Trash — low priority. Review if expanding founder connections.)</li>
      </ul>
    </div>

    <div class="divider"></div>

    <!-- CALENDAR / EVENTS -->
    <div style="margin-bottom:20px;">
      <div class="cat-header">
        <strong style="color:#2471a3;">📅 Calendar / Events</strong>
        <span class="cat-count badge badge-blue">0 emails</span>
      </div>
      <p class="note">All calendar items handled via Google Calendar data above. No separate calendar emails in inbox.</p>
    </div>

    <div class="divider"></div>

    <!-- MEDICAL / HEALTH -->
    <div style="margin-bottom:20px;">
      <div class="cat-header">
        <strong style="color:#6c3483;">🟣 Medical / Health</strong>
        <span class="cat-count badge badge-purple">1 email</span>
      </div>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Location</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Center for Veterinary Care (Thrive Pet Care)</td><td>Paws &amp; Learn: Is Stella Hiding Pain? — Signs of osteoarthritis in cats</td><td>Trash</td><td>Informational email about feline osteoarthritis for pet Stella. Review if relevant — Stella may benefit from a vet checkup. Otherwise ignore.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="divider"></div>

    <!-- FINANCIAL / BILLING -->
    <div style="margin-bottom:20px;">
      <div class="cat-header">
        <strong style="color:#d4a017;">🟡 Financial / Billing</strong>
        <span class="cat-count badge badge-yellow">2 emails</span>
      </div>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Marcus by Goldman Sachs</td><td>Monthly Marcus Savings account statement now available</td><td>Log into marcus.com to review and download statement for September.</td></tr>
          <tr><td>Apify Billing</td><td>Apify invoice #202609021150 — payment successful ($31.58)</td><td>Payment confirmed. File/archive for expense records. No action needed.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="divider"></div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div style="margin-bottom:20px;">
      <div class="cat-header">
        <strong style="color:#6c3483;">🟣 Professional Development</strong>
        <span class="cat-count badge badge-purple">2 emails</span>
      </div>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Melissa W (self-sent)</td><td>How I Built an Animated GitHub Profile README (ASCII Portrait + Neofetch + Live Graph) | Avi Vashishta</td><td>Self-sent resource for later review. Read when time allows — GitHub profile enhancement technique.</td></tr>
          <tr><td>Coursiv</td><td>Pick up where you left off</td><td>In Trash. Coursiv online course follow-up. Review if you started a course — otherwise ignore/unsubscribe.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="divider"></div>

    <!-- PERSONAL -->
    <div style="margin-bottom:20px;">
      <div class="cat-header">
        <strong style="color:#5d6d7e;">⚫ Personal</strong>
        <span class="cat-count badge badge-gray">3 emails</span>
      </div>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Match</td><td>You've had a profile view from John (61, Montclair NJ)</td><td>In Inbox. Review at your leisure — check profile if interested.</td></tr>
          <tr><td>USA Service Dog Registration</td><td>Unlock Sweet Dreams: Legit ESA Housing Letters</td><td>Not trashed — likely unsolicited marketing. DELETE and unsubscribe unless actively seeking ESA letter.</td></tr>
          <tr><td>Leslie on Facebook (close friend)</td><td>Leslie Schwartz Berlent commented on a reel</td><td>In Trash. Social notification — low priority. View on Facebook if curious.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="divider"></div>

    <!-- NEWSLETTERS / SUBSCRIPTIONS -->
    <div style="margin-bottom:20px;">
      <div class="cat-header">
        <strong style="color:#6c3483;">🟣 Newsletters / Subscriptions</strong>
        <span class="cat-count badge badge-purple">7 emails</span>
      </div>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Location</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Medium Daily Digest</td><td>Upgrading your SEO testing framework for AEO | Kaitlin McMichael</td><td>Trash</td><td>SEO/AEO newsletter. Unsubscribe if not actively needed.</td></tr>
          <tr><td>Dylan's Diary (Behind the Markets)</td><td>What Pets.com Taught Me About the AI Trade</td><td>Trash</td><td>Finance/investing newsletter. Keep if useful — unsubscribe if not reading.</td></tr>
          <tr><td>The Signal by TradeAlgo</td><td>Vanguard and BlackRock ETFs power a trade around the 30% tax</td><td>Trash</td><td>Market/trading newsletter. Unsubscribe if not actively trading ETFs.</td></tr>
          <tr><td>The Daily Skimm</td><td>Introducing, a nepo dog</td><td>Trash</td><td>General news digest. Keep or unsubscribe based on reading habit.</td></tr>
          <tr><td>Ruben Hassid (Substack) ×3</td><td>Give AI a fish, and you feed it for a day (3 duplicate sends)</td><td>Trash (2) + Archive (1)</td><td>3 duplicate sends of same AI newsletter. Unsubscribe or filter. Delete duplicates.</td></tr>
          <tr><td>Gap Factory <span class="tag tag-newsletter">AUTO-TRASHED</span></td><td>Fifty. To. Seventy. Percent. Off (newsletter)</td><td>Auto-Trashed</td><td>Auto-trashed as unwanted newsletter. No action needed.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="divider"></div>

    <!-- PROMOTIONAL / RETAIL -->
    <div style="margin-bottom:20px;">
      <div class="cat-header">
        <strong style="color:#5d6d7e;">🛍️ Promotional / Retail</strong>
        <span class="cat-count badge badge-gray">11 emails</span>
      </div>
      <p class="note" style="margin-bottom:8px;">See full Promotional / Retail Summary section below for detail.</p>
      <ul class="plain">
        <li>Amazon — Ordered: 1 Snack Foods item (not trashed) | Review if unexpected order</li>
        <li>Amazon — Ordered: 2 Beverages and Snack Foods items (not trashed, read) | Archive</li>
        <li>Amazon — Ordered: 1 Cosmetics item (inbox) | Confirmed order</li>
        <li>Amazon — Shipped: 1 Cosmetics item (inbox) | Track delivery</li>
        <li>Amazon — The Holiday Shop is here (trash) | Promotional</li>
        <li>Amazon — Get up to 50% off premium brands for Labor Day (trash) | Promotional</li>
        <li>Chick-fil-A — A little thing…from us to you (trash) | Loyalty reward promo</li>
        <li>Kohl's — Fall home picks at great prices (trash) | Seasonal promotional</li>
        <li>SHEIN — UNDER $10 &amp; Undefeated (trash) | Promotional</li>
        <li>SHEIN — Start from $2.99 Fresh Arrivals (trash) | Promotional</li>
        <li>SHEIN — Delay notice (inbox) | ⚠️ May be order-related — check if you have an active order</li>
        <li>YesStyle — Labor Day Exclusive 15% OFF (trash) | Seasonal promotional</li>
      </ul>
    </div>

    <div class="divider"></div>

    <!-- NOTIFY NYC -->
    <div style="margin-bottom:20px;">
      <div class="cat-header">
        <strong style="color:#0e7490;">🚇 Government / Transit Alerts</strong>
        <span class="cat-count badge" style="background:#e0f7fa;color:#0e7490;">1 email</span>
      </div>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Notify NYC <span class="tag tag-rescued">✅ RESCUED</span></td><td>MTA Disruption — A &amp; C Trains (MN/BK) — Switch malfunction, expect delays both directions</td><td>Rescued from Trash</td><td>Issued 9/1/26 8:55 PM. Check MTA status before traveling on A or C lines today.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="divider"></div>

    <!-- ADULT SPAM / NSFW -->
    <div style="margin-bottom:20px;">
      <div class="cat-header">
        <strong style="color:#c0392b;">🚫 Adult Spam / Unsolicited</strong>
        <span class="cat-count badge badge-red">1 email</span>
      </div>
      <ul class="plain">
        <li>'Unstoppable Sex Machines' — Explicit adult spam (In Trash). DELETE. Block sender. Consider reporting as spam.</li>
      </ul>
    </div>

    <div class="divider"></div>

    <!-- POLITICAL -->
    <div style="margin-bottom:20px;">
      <div class="cat-header">
        <strong style="color:#5d6d7e;">🏛️ Political / Fundraising</strong>
        <span class="cat-count badge badge-gray">1 email</span>
      </div>
      <ul class="plain">
        <li>Trump Campaign (win.donaldjtrump.com) — "Please confirm receipt of this email!" (In Trash). Ignore/delete. Political fundraising email — no action needed.</li>
      </ul>
    </div>

    <div class="divider"></div>

    <!-- CASINO LIMITLESS (SPAM, NOT AUTO-TRASHED) -->
    <div style="margin-bottom:20px;">
      <div class="cat-header">
        <strong style="color:#c0392b;">🎰 Casino Spam — Not Auto-Trashed</strong>
        <span class="cat-count badge badge-red">1 email</span>
      </div>
      <ul class="plain">
        <li>'melissaw212' &lt;qnjsupportjl@...&gt; — "It's Here! Your Exclusive Casino Limitless NGR Bonus 🎰" (In Trash). Spam — delete. Already trashed.</li>
      </ul>
    </div>

  </div>
</div>

<!-- ============================================================
     SECTION 7: TRASH REVIEW
     ============================================================ -->
<div class="section-wrap">
  <div class="section-title title-gray">🗑️ Trash Review</div>
  <div class="section-body">

    <h3 style="color:#1e8449;font-size:14px;margin
