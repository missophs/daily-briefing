<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa W. — August 6, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px 60px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 16px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header .sub { font-size: 14px; opacity: 0.75; margin-top: 4px; }
  .header-stats { display: flex; gap: 24px; flex-wrap: wrap; }
  .stat-pill { background: rgba(255,255,255,0.12); border-radius: 8px; padding: 8px 18px; text-align: center; }
  .stat-pill .num { font-size: 22px; font-weight: 700; }
  .stat-pill .lbl { font-size: 11px; opacity: 0.7; text-transform: uppercase; letter-spacing: 0.5px; }

  /* SECTION TITLES */
  .section-title { font-size: 17px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin: 32px 0 14px; padding-bottom: 8px; border-bottom: 3px solid currentColor; }
  .section-title.red { color: #c0392b; border-color: #c0392b; }
  .section-title.yellow { color: #d4880a; border-color: #d4880a; }
  .section-title.blue { color: #1565c0; border-color: #1565c0; }
  .section-title.green { color: #1b7a34; border-color: #1b7a34; }
  .section-title.purple { color: #6a1b9a; border-color: #6a1b9a; }
  .section-title.gray { color: #546e7a; border-color: #546e7a; }
  .section-title.dark { color: #1a1a2e; border-color: #1a1a2e; }
  .section-title.teal { color: #00695c; border-color: #00695c; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; border-left: 5px solid transparent; }
  .card.red { background: #fff5f5; border-color: #e53935; }
  .card.yellow { background: #fffde7; border-color: #f9a825; }
  .card.blue { background: #e8f0fe; border-color: #1976d2; }
  .card.green { background: #f1f8f2; border-color: #2e7d32; }
  .card.purple { background: #f3e5f5; border-color: #7b1fa2; }
  .card.gray { background: #f5f5f5; border-color: #90a4ae; }
  .card.teal { background: #e0f2f1; border-color: #00796b; }
  .card-title { font-weight: 700; font-size: 14px; margin-bottom: 4px; }
  .card-meta { font-size: 12px; color: #555; margin-bottom: 6px; }
  .card-body { font-size: 13px; }
  .card-row { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 6px; }
  .badge { display: inline-block; padding: 2px 9px; border-radius: 12px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.4px; }
  .badge.red { background: #ffcdd2; color: #b71c1c; }
  .badge.yellow { background: #fff9c4; color: #f57f17; }
  .badge.blue { background: #bbdefb; color: #0d47a1; }
  .badge.green { background: #c8e6c9; color: #1b5e20; }
  .badge.purple { background: #e1bee7; color: #4a148c; }
  .badge.gray { background: #eceff1; color: #455a64; }
  .badge.teal { background: #b2dfdb; color: #004d40; }
  .badge.orange { background: #ffe0b2; color: #bf360c; }

  /* EXECUTIVE SUMMARY */
  .exec-summary { background: #fff; border-radius: 12px; padding: 20px 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 24px; }
  .exec-summary ul { list-style: none; padding: 0; }
  .exec-summary ul li { padding: 10px 0; border-bottom: 1px solid #f0f0f0; display: flex; gap: 12px; align-items: flex-start; }
  .exec-summary ul li:last-child { border-bottom: none; }
  .exec-icon { font-size: 20px; min-width: 28px; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 6px rgba(0,0,0,0.07); margin-bottom: 20px; }
  th { background: #1a1a2e; color: #fff; padding: 10px 13px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; font-weight: 600; }
  td { padding: 9px 13px; border-bottom: 1px solid #f0f0f0; font-size: 13px; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #fafafa; }
  .triage-status { font-weight: 700; font-size: 13px; white-space: nowrap; }
  .row-red td { background: #fff8f8; }
  .row-yellow td { background: #fffdf0; }
  .row-green td { background: #f6fbf6; }
  .row-gray td { background: #f9f9f9; }
  .row-purple td { background: #fdf5ff; }
  .row-blue td { background: #f5f8ff; }
  .row-teal td { background: #f0faf9; }

  /* CALENDAR */
  .cal-day { margin-bottom: 20px; }
  .cal-day-header { background: #1565c0; color: #fff; padding: 8px 16px; border-radius: 8px 8px 0 0; font-weight: 700; font-size: 14px; }
  .cal-event { background: #fff; border-left: 4px solid #1976d2; padding: 12px 16px; border-bottom: 1px solid #e8eaf0; }
  .cal-event:last-child { border-bottom: none; border-radius: 0 0 8px 8px; }
  .cal-event.conflict { border-left-color: #e53935; background: #fff8f8; }
  .cal-event.declined { border-left-color: #90a4ae; background: #f9f9f9; opacity: 0.85; }
  .cal-event.needs-action { border-left-color: #f9a825; background: #fffde7; }
  .cal-event.allday { border-left-color: #f9a825; background: #fffde7; }
  .cal-time { font-weight: 700; font-size: 13px; color: #1565c0; }
  .cal-name { font-weight: 700; font-size: 14px; margin: 2px 0; }
  .cal-detail { font-size: 12px; color: #555; margin-top: 3px; }
  .cal-conflict-warn { background: #ffebee; border-radius: 6px; padding: 5px 10px; font-size: 12px; color: #b71c1c; font-weight: 600; margin-top: 6px; }

  /* PRIORITY TAGS */
  .pri-high { color: #c0392b; font-weight: 700; }
  .pri-med { color: #d4880a; font-weight: 700; }
  .pri-low { color: #546e7a; font-weight: 700; }

  /* DASHBOARD GRID */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; margin-bottom: 20px; }
  .dash-tile { background: #fff; border-radius: 10px; padding: 16px; box-shadow: 0 1px 6px rgba(0,0,0,0.08); border-top: 4px solid #ccc; }
  .dash-tile.red { border-top-color: #e53935; }
  .dash-tile.yellow { border-top-color: #f9a825; }
  .dash-tile.blue { border-top-color: #1976d2; }
  .dash-tile.green { border-top-color: #2e7d32; }
  .dash-tile.purple { border-top-color: #7b1fa2; }
  .dash-tile.gray { border-top-color: #90a4ae; }
  .dash-tile .tile-num { font-size: 32px; font-weight: 800; }
  .dash-tile .tile-lbl { font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 2px; }
  .dash-tile .tile-detail { font-size: 12px; color: #888; margin-top: 6px; }

  /* TOP 3 */
  .top3 { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; margin-top: 16px; }
  .top3-card { background: #1a1a2e; color: #fff; border-radius: 12px; padding: 20px 22px; position: relative; }
  .top3-num { font-size: 48px; font-weight: 800; opacity: 0.15; position: absolute; top: 10px; right: 18px; }
  .top3-title { font-size: 15px; font-weight: 700; margin-bottom: 6px; }
  .top3-body { font-size: 13px; opacity: 0.85; }

  /* MISC */
  .pill-row { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; }
  .note { font-size: 12px; color: #777; font-style: italic; margin-top: 4px; }
  .divider { border: none; border-top: 1px solid #e0e0e0; margin: 24px 0; }
  .rescued-tag { background: #e8f5e9; color: #1b5e20; border: 1px solid #a5d6a7; border-radius: 10px; padding: 1px 8px; font-size: 11px; font-weight: 700; }
  .auto-trash-tag { background: #ffebee; color: #b71c1c; border: 1px solid #ef9a9a; border-radius: 10px; padding: 1px 8px; font-size: 11px; font-weight: 700; }
  .manual-trash-tag { background: #eceff1; color: #455a64; border: 1px solid #b0bec5; border-radius: 10px; padding: 1px 8px; font-size: 11px; font-weight: 700; }
  a { color: #1565c0; text-decoration: none; }
  a:hover { text-decoration: underline; }
  .self-sent { background: #fff8e1; border-left-color: #ffc107; }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 0: EMAIL TRIAGE QUICK LIST
═══════════════════════════════════════════════════════════════ -->
<h2 class="section-title dark" style="margin-top:0;">📋 Email Triage Quick List</h2>
<table>
  <thead>
    <tr>
      <th style="width:130px;">Status</th>
      <th style="width:200px;">From</th>
      <th>Subject</th>
      <th>Summary</th>
    </tr>
  </thead>
  <tbody>
    <!-- RESCUED -->
    <tr class="row-teal">
      <td class="triage-status">✅ RESCUED</td>
      <td>JetBlue Plus Card (Barclays)</td>
      <td>Activate your 8.99% promo rate now</td>
      <td><span class="rescued-tag">Rescued from Trash</span> Protected sender — Barclays promo rate offer; review if interested.</td>
    </tr>
    <!-- INBOX EMAILS — individual rows -->
    <tr class="row-red">
      <td class="triage-status">📥 INBOX</td>
      <td>Bank of America</td>
      <td>Fraud Claim for account -2994 — Temporary credit issued</td>
      <td><span class="badge red">URGENT</span> Fraud claim Step 2 of 3 — temporary credit issued. Verify via BofA app.</td>
    </tr>
    <tr class="row-red">
      <td class="triage-status">📥 INBOX</td>
      <td>Bank of America</td>
      <td>Fraud Claim for account -2994 — Status updated</td>
      <td><span class="badge red">URGENT</span> Fraud claim status update — monitor resolution closely.</td>
    </tr>
    <tr class="row-green">
      <td class="triage-status">📥 INBOX</td>
      <td>LinkedIn Job Alerts</td>
      <td>Vice President, People Technology at Avalara</td>
      <td><span class="badge green">JOB</span> Active VP-level People Tech role at Avalara — actively recruiting.</td>
    </tr>
    <tr class="row-green">
      <td class="triage-status">📥 INBOX</td>
      <td>LinkedIn Job Alerts</td>
      <td>Director of People (Remote) at GridUnity</td>
      <td><span class="badge green">JOB</span> Remote Director of People — duplicate alert received, strong fit signal.</td>
    </tr>
    <tr class="row-green">
      <td class="triage-status">📥 INBOX</td>
      <td>LinkedIn Job Alerts</td>
      <td>Director of People (Remote) at GridUnity</td>
      <td><span class="badge green">JOB</span> Second alert for GridUnity Director of People (Remote).</td>
    </tr>
    <tr class="row-green">
      <td class="triage-status">📥 INBOX</td>
      <td>LinkedIn Job Alerts</td>
      <td>Senior Director, People Partner at Zeta Global</td>
      <td><span class="badge green">JOB</span> Senior Director People Partner — actively recruiting at Zeta Global.</td>
    </tr>
    <tr class="row-green">
      <td class="triage-status">📥 INBOX</td>
      <td>JobLeads</td>
      <td>Contact recommendation for your field</td>
      <td><span class="badge green">JOB</span> Headhunter match in your field — review recruiter profile.</td>
    </tr>
    <tr class="row-green">
      <td class="triage-status">📥 INBOX</td>
      <td>Melissa W (self)</td>
      <td>Job (LinkedIn link — cape.co)</td>
      <td><span class="badge green">JOB</span> Self-sent job link — cape.co careers posting saved for review.</td>
    </tr>
    <tr class="row-green">
      <td class="triage-status">📥 INBOX</td>
      <td>Melissa W (self)</td>
      <td>[no subject] — LinkedIn job link #1</td>
      <td><span class="badge green">JOB</span> Self-sent LinkedIn job view link (4442081334).</td>
    </tr>
    <tr class="row-green">
      <td class="triage-status">📥 INBOX</td>
      <td>Melissa W (self)</td>
      <td>[no subject] — LinkedIn job link #2</td>
      <td><span class="badge green">JOB</span> Self-sent LinkedIn job view link (4446457434).</td>
    </tr>
    <tr class="row-green">
      <td class="triage-status">📥 INBOX</td>
      <td>Melissa W (self)</td>
      <td>[no subject] — LinkedIn job link #3</td>
      <td><span class="badge green">JOB</span> Self-sent LinkedIn job view link (4449915880).</td>
    </tr>
    <tr class="row-green">
      <td class="triage-status">📥 INBOX</td>
      <td>Melissa W (self)</td>
      <td>[no subject] — LinkedIn profile link</td>
      <td><span class="badge green">NETWORK</span> Self-sent LinkedIn profile link (vanchic) — likely a contact to follow up with.</td>
    </tr>
    <tr class="row-yellow">
      <td class="triage-status">📥 INBOX</td>
      <td>Apify Community</td>
      <td>Pricing change for ⚡ Rapid LinkedIn Jobs Scraper</td>
      <td><span class="badge yellow">BILLING</span> Tool pricing change — review impact on job search automation.</td>
    </tr>
    <tr class="row-yellow">
      <td class="triage-status">📥 INBOX</td>
      <td>Old Navy</td>
      <td>Your Order Is Arriving Soon!</td>
      <td><span class="badge yellow">SHIPPING</span> Order #1RDGPJ0 arriving soon — placed Aug 1.</td>
    </tr>
    <tr class="row-gray">
      <td class="triage-status">📥 INBOX</td>
      <td>CVS ExtraCare</td>
      <td>$2 Coupon!</td>
      <td><span class="badge gray">PROMO</span> $2 ExtraCare coupon — low priority.</td>
    </tr>
    <tr class="row-gray">
      <td class="triage-status">📥 INBOX</td>
      <td>Charles Schwab</td>
      <td>August 2026 Schwab Coaching webcast lineup</td>
      <td><span class="badge purple">LEARNING</span> Monthly Schwab Coaching webcasts — review if interested in financial education.</td>
    </tr>
    <tr class="row-gray">
      <td class="triage-status">📥 INBOX</td>
      <td>Chick-fil-A</td>
      <td>A little thing… from us to you</td>
      <td><span class="badge gray">PROMO</span> Reward points available at local Chick-fil-A.</td>
    </tr>
    <tr class="row-gray">
      <td class="triage-status">📥 INBOX</td>
      <td>Match</td>
      <td>Steve likes you. See if it's mutual.</td>
      <td><span class="badge gray">PERSONAL</span> Match.com notification — Steve, 65, Forest Hills NY.</td>
    </tr>
    <tr class="row-gray">
      <td class="triage-status">📥 INBOX</td>
      <td>Match</td>
      <td>You've had a profile view from Steve</td>
      <td><span class="badge gray">PERSONAL</span> Match.com profile view from same user.</td>
    </tr>
    <!-- TRASH SUMMARY ROWS -->
    <tr class="row-red" style="font-style:italic;">
      <td class="triage-status">🗑 AUTO-TRASHED</td>
      <td colspan="3"><strong>5 emails auto-trashed (phishing/scam/newsletter)</strong> — see Trash Review section below. Includes: 2 phishing (fake AAA prize, spoofed storage alert), 1 newsletter auto-trashed (Quince), and 2 other flagged items.</td>
    </tr>
    <tr class="row-gray" style="font-style:italic;">
      <td class="triage-status">🗂 TRASH (manual)</td>
      <td colspan="3"><strong>13 emails in Trash</strong> — see Trash Review section below. Includes newsletters, digests, retail, and low-value items.</td>
    </tr>
  </tbody>
</table>

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 1: HEADER
═══════════════════════════════════════════════════════════════ -->
<div class="header">
  <div>
    <div style="font-size:13px;opacity:0.65;text-transform:uppercase;letter-spacing:1px;margin-bottom:4px;">Executive Briefing</div>
    <h1>Good morning, Melissa 👋</h1>
    <div class="sub">Thursday, August 6, 2026 &nbsp;|&nbsp; Prepared by your Executive Chief of Staff</div>
  </div>
  <div class="header-stats">
    <div class="stat-pill"><div class="num">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="stat-pill"><div class="num">8</div><div class="lbl">Calendar Events</div></div>
    <div class="stat-pill"><div class="num">2</div><div class="lbl">🚨 Security Alerts</div></div>
    <div class="stat-pill"><div class="num">6</div><div class="lbl">Job Leads</div></div>
    <div class="stat-pill"><div class="num">4</div><div class="lbl">Urgent Actions</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 2: EXECUTIVE SUMMARY
═══════════════════════════════════════════════════════════════ -->
<h2 class="section-title dark">⚡ Executive Summary</h2>
<div class="exec-summary">
  <ul>
    <li>
      <span class="exec-icon">🚨</span>
      <div><strong>Biggest Risk:</strong> Bank of America has issued a <strong>temporary fraud credit on account ending -2994</strong> (Step 2 of 3). Two emails confirm status updates. This requires immediate verification via the official BofA app or phone to ensure the claim is progressing correctly and no unauthorized activity remains unresolved. Additionally, multiple phishing/spam emails were caught (auto-trashed and flagged).</div>
    </li>
    <li>
      <span class="exec-icon">💼</span>
      <div><strong>Biggest Opportunity:</strong> <strong>6 active job leads</strong> arrived today including VP, People Technology at Avalara (actively recruiting), Senior Director People Partner at Zeta Global (actively recruiting), and Director of People (Remote) at GridUnity. You also self-emailed 4 LinkedIn job links last night for review. Strong momentum — prioritize applications today.</div>
    </li>
    <li>
      <span class="exec-icon">📅</span>
      <div><strong>Biggest Calendar Item:</strong> You have a <strong>scheduling conflict today (Aug 6) at 9:00 AM</strong> — "disability" appointment and "Executive Roundtable" (already declined) overlap. The <strong>HR Networking Open Office Hours Zoom</strong> is at 12:00 PM today and your RSVP is pending. Your <strong>Brain MRI</strong> is scheduled for Tuesday, August 11 at 8:50 AM at 159 E 53rd Street — arrive early; bring no valuables.</div>
    </li>
  </ul>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 3: ACTION REQUIRED
═══════════════════════════════════════════════════════════════ -->
<h2 class="section-title red">🔴 Action Required</h2>

<div class="card red">
  <div class="card-row"><span class="badge red">URGENT — FINANCIAL SECURITY</span></div>
  <div class="card-title" style="margin-top:8px;">🏦 Bank of America Fraud Claim — Account -2994</div>
  <div class="card-meta">From: Bank of America &lt;onlinebanking@ealerts.bankofamerica.com&gt; | Wed Aug 5, 2026 (2 emails)</div>
  <div class="card-body">A fraud claim is in progress at Step 2 of 3. A temporary credit has been issued. You must verify the claim is proceeding correctly and monitor for the final resolution (Step 3).</div>
  <div class="card-row" style="margin-top:8px;">
    <strong>Next Step:</strong>&nbsp; Log in to BofA app or call 1-800-432-1000 to confirm claim status and ensure no additional fraud exposure.
  </div>
  <div class="card-row"><span class="badge yellow">Due: Today</span></div>
</div>

<div class="card yellow">
  <div class="card-row"><span class="badge yellow">RSVP NEEDED</span></div>
  <div class="card-title" style="margin-top:8px;">📅 HR Networking & Job Search: Open Office Hours — Today 12:00–1:00 PM</div>
  <div class="card-meta">Calendar Event | Status: Needs Action | Zoom: us06web.zoom.us</div>
  <div class="card-body">Large HR networking group Zoom call today at noon. RSVP is still pending ("needsAction"). This is directly relevant to your active job search.</div>
  <div class="card-row" style="margin-top:8px;"><strong>Next Step:</strong>&nbsp; Accept or decline the calendar invite. If attending, note that AI notetaking tools should be turned off per organizer request.</div>
  <div class="card-row"><span class="badge yellow">Due: Today by 12:00 PM</span></div>
</div>

<div class="card green">
  <div class="card-row"><span class="badge green">JOB SEARCH</span></div>
  <div class="card-title" style="margin-top:8px;">💼 Review & Act on 4 Self-Saved Job Links + 6 New Alerts</div>
  <div class="card-meta">From: Melissa W (self-sent) + LinkedIn Job Alerts + JobLeads | Wed Aug 5 – Thu Aug 6, 2026</div>
  <div class="card-body">You emailed yourself 4 LinkedIn job links + 1 cape.co job link last night. New alerts arrived today for VP People Tech (Avalara), Senior Director People Partner (Zeta Global), Director of People x2 (GridUnity), and a JobLeads headhunter match. These are strong pipeline items.</div>
  <div class="card-row" style="margin-top:8px;"><strong>Next Step:</strong>&nbsp; Open all links, triage by fit, and submit applications for top matches. Prioritize actively-recruiting roles.</div>
  <div class="card-row"><span class="badge yellow">Due: Today or Tomorrow</span></div>
</div>

<div class="card yellow">
  <div class="card-row"><span class="badge yellow">BILLING / DEADLINE</span></div>
  <div class="card-title" style="margin-top:8px;">🗓 State Farm Bill Due — August 7</div>
  <div class="card-meta">Calendar Event | All-day: August 7, 2026</div>
  <div class="card-body">State Farm insurance bill is due tomorrow, August 7. Ensure payment is scheduled or submitted to avoid lapse.</div>
  <div class="card-row" style="margin-top:8px;"><strong>Next Step:</strong>&nbsp; Confirm payment has been made or schedule it today.</div>
  <div class="card-row"><span class="badge red">Due: Tomorrow Aug 7</span></div>
</div>

<div class="card blue">
  <div class="card-row"><span class="badge blue">PREP NEEDED</span></div>
  <div class="card-title" style="margin-top:8px;">🧠 Brain MRI — Tuesday August 11, Arrive 8:50 AM</div>
  <div class="card-meta">Calendar Event | 159 E 53rd Street, 6th Floor, New York, NY 10022 | Phone: 646-754-2800</div>
  <div class="card-body">Appointment begins at 9:20 AM; arrive by 8:50 AM. Remove all body piercings and metal. Do not bring valuables. MRI-safe gown provided. Private dressing rooms available.</div>
  <div class="card-row" style="margin-top:8px;"><strong>Next Step:</strong>&nbsp; Confirm appointment, arrange transportation, review any prep instructions from ordering physician. Leave valuables at home.</div>
  <div class="card-row"><span class="badge blue">Due: Aug 11</span></div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 4: FULL 7-DAY CALENDAR
═══════════════════════════════════════════════════════════════ -->
<h2 class="section-title blue">📅 Full 7-Day Calendar</h2>

<!-- THURSDAY AUG 6 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Thursday, August 6, 2026 — TODAY</div>

  <div class="cal-event conflict">
    <div class="cal-time">9:00 AM – 11:00 AM</div>
    <div class="cal-name">🟡 disability</div>
    <div class="cal-detail"><strong>Status:</strong> Confirmed &nbsp;|&nbsp; <strong>Location:</strong> Not specified &nbsp;|&nbsp; <strong>Attendees:</strong> None listed</div>
    <div class="cal-detail"><strong>Prep:</strong> No details provided — confirm appointment details if needed.</div>
    <div class="cal-conflict-warn">⚠️ CONFLICT: Overlaps with Executive Roundtable (9:00–10:30 AM) — Roundtable already declined ✓</div>
  </div>

  <div class="cal-event declined">
    <div class="cal-time">9:00 AM – 10:30 AM</div>
    <div class="cal-name">❌ Executive Roundtable <span style="font-size:12px;color:#888;">(DECLINED)</span></div>
    <div class="cal-detail"><strong>Status:</strong> Declined &nbsp;|&nbsp; <strong>Host:</strong> John Madigan &nbsp;|&nbsp; <strong>Zoom:</strong> <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09">Meeting ID 207 786 667</a> &nbsp;|&nbsp; PW: 205454</div>
    <div class="cal-detail"><strong>Prep:</strong> None required — already declined. Conflict with disability appointment.</div>
    <div class="cal-conflict-warn">⚠️ CONFLICT: Overlaps with disability appointment (9:00–11:00 AM) — already declined ✓</div>
  </div>

  <div class="cal-event needs-action">
    <div class="cal-time">12:00 PM – 1:00 PM</div>
    <div class="cal-name">⚠️ HR Networking & Job Search: Open Office Hours — Zoom 2 <span style="font-size:12px;color:#888;">(RSVP PENDING)</span></div>
    <div class="cal-detail"><strong>Status:</strong> Needs Action &nbsp;|&nbsp; <strong>Zoom:</strong> <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1">Join Zoom</a> &nbsp;|&nbsp; <strong>Attendees:</strong> ~175 HR professionals</div>
    <div class="cal-detail"><strong>Prep:</strong> Turn off AI notetaking tools per organizer. Review group guidelines before joining. Great opportunity to network with active HR job seekers. RSVP before 12 PM.</div>
  </div>
</div>

<!-- FRIDAY AUG 7 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Friday, August 7, 2026</div>
  <div class="cal-event allday">
    <div class="cal-time">All Day</div>
    <div class="cal-name">📋 State Farm Bill Due</div>
    <div class="cal-detail"><strong>Status:</strong> Confirmed &nbsp;|&nbsp; <strong>Location:</strong> N/A</div>
    <div class="cal-detail"><strong>Prep:</strong> Ensure payment is submitted today (Aug 6) or first thing Aug 7. Check State Farm account or auto-pay status. Do not let this lapse.</div>
  </div>
</div>

<!-- SAT AUG 8 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Saturday, August 8, 2026</div>
  <div class="cal-event" style="background:#f9f9f9; border-left-color:#90a4ae;">
    <div class="cal-time">All Day</div>
    <div class="cal-name" style="color:#666;">No Events Scheduled</div>
    <div class="cal-detail">Free day. Consider using this time to work on job applications from the self-sent links.</div>
  </div>
</div>

<!-- SUN AUG 9 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Sunday, August 9, 2026</div>
  <div class="cal-event" style="background:#f9f9f9; border-left-color:#90a4ae;">
    <div class="cal-time">All Day</div>
    <div class="cal-name" style="color:#666;">No Events Scheduled</div>
    <div class="cal-detail">Prep for MRI on Tuesday: confirm appointment, arrange transportation, review physician instructions.</div>
  </div>
</div>

<!-- MON AUG 10 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Monday, August 10, 2026</div>
  <div class="cal-event" style="background:#f9f9f9; border-left-color:#90a4ae;">
    <div class="cal-time">All Day</div>
    <div class="cal-name" style="color:#666;">No Events Scheduled</div>
    <div class="cal-detail">Day before MRI — confirm arrival time (8:50 AM), address (159 E 53rd St, 6th Fl), and no-valuables policy.</div>
  </div>
</div>

<!-- TUE AUG 11 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Tuesday, August 11, 2026</div>
  <div class="cal-event" style="border-left-color:#e53935; background:#fff8f8;">
    <div class="cal-time">Arrive 8:50 AM | Appt Starts 9:20 AM — ends ~9:40 AM</div>
    <div class="cal-name">🧠 MRI BRAIN W&WO IVC</div>
    <div class="cal-detail"><strong>Status:</strong> Confirmed &nbsp;|&nbsp; <strong>Location:</strong> 159 E 53rd Street, 6th Floor, New York, NY 10022 &nbsp;|&nbsp; <strong>Phone:</strong> 646-754-2800</div>
    <div class="cal-detail"><strong>Prep:</strong> Arrive by 8:50 AM (appointment begins 9:20 AM). Remove all body piercings and metal items. MRI-safe gown provided. Private lockers available. Do NOT bring valuables. Allow extra time for transit.</div>
  </div>
</div>

<!-- WED AUG 12 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Wednesday, August 12, 2026</div>

  <div class="cal-event needs-action">
    <div class="cal-time">9:30 AM – 10:30 AM</div>
    <div class="cal-name">🏥 PT (Physical Therapy)</div>
    <div class="cal-detail"><strong>Status:</strong> Confirmed &nbsp;|&nbsp; <strong>Location:</strong> Not specified &nbsp;|&nbsp; <strong>Attendees:</strong> None listed</div>
    <div class="cal-detail"><strong>Prep:</strong> Confirm appointment location and any intake requirements. Follow up after MRI on Aug 11 if results may be relevant to PT.</div>
  </div>

  <div class="cal-event needs-action">
    <div class="cal-time">12:00 PM – 1:30 PM</div>
    <div class="cal-name">⚠️ HR Networking & Job Search Group — Zoom 2 <span style="font-size:12px;color:#888;">(RSVP PENDING)</span></div>
    <div class="cal-detail"><strong>Status:</strong> Needs Action &nbsp;|&nbsp; <strong>Zoom:</strong> <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1">Join Zoom</a> &nbsp;|&nbsp; <strong>Attendees:</strong> ~175 HR professionals</div>
    <div class="cal-detail"><strong>Prep:</strong> Review HR Networking Team Guidelines (linked in invite). Note: 1.5-hour session. Prepare a brief networking intro and any questions about open roles. RSVP required.</div>
  </div>

  <div class="cal-event" style="border-left-color:#2e7d32; background:#f6fbf6;">
    <div class="cal-time">12:00 PM – 1:30 PM</div>
    <div class="cal-name">📝 Network (Personal Reminder)</div>
    <div class="cal-detail"><strong>Status:</strong> Confirmed &nbsp;|&nbsp; <strong>Note:</strong> This appears to be a personal placeholder for the HR Networking session above — same time slot.</div>
    <div class="cal-detail"><strong>Prep:</strong> Confirmed personal tracking event. Attend the HR Networking Zoom above.</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 5: JOB SEARCH & INTERVIEW PIPELINE
═══════════════════════════════════════════════════════════════ -->
<h2 class="section-title green">💼 Job Search & Interview Pipeline</h2>

<table>
  <thead>
    <tr>
      <th>Source</th>
      <th>Role / Company</th>
      <th>Details</th>
      <th>Fit</th>
      <th>Action</th>
    </tr>
  </thead>
  <tbody>
    <tr class="row-green">
      <td><span class="badge green">LinkedIn</span></td>
      <td><strong>VP, People Technology</strong><br>Avalara</td>
      <td>Actively recruiting — VP-level role in People Technology. Strong alignment with HR tech background.</td>
      <td><span class="pri-high">HIGH</span></td>
      <td>Apply immediately — actively recruiting signal</td>
    </tr>
    <tr class="row-green">
      <td><span class="badge green">LinkedIn</span></td>
      <td><strong>Senior Director, People Partner</strong><br>Zeta Global</td>
      <td>Actively recruiting — Senior Director People Partner at Zeta Global (digital marketing/data).</td>
      <td><span class="pri-high">HIGH</span></td>
      <td>Apply immediately — actively recruiting signal</td>
    </tr>
    <tr class="row-green">
      <td><span class="badge green">LinkedIn</span></td>
      <td><strong>Director of People (Remote)</strong><br>GridUnity</td>
      <td>Two separate alerts received (1:05 AM and 5:05 AM) — strong interest signal. Remote role.</td>
      <td><span class="pri-high">HIGH</span></td>
      <td>Apply — remote, duplicate alert suggests high relevance</td>
    </tr>
    <tr class="row-green">
      <td><span class="badge green">Self-Saved</span></td>
      <td><strong>Job at cape.co</strong><br>Cape</td>
      <td>cape.co/careers link self-emailed last night. Role unknown without clicking — review today.</td>
      <td><span class="pri-med">MEDIUM</span></td>
      <td>Open link, review role details, apply if strong fit</td>
    </tr>
    <tr class="row-green">
      <td><span class="badge green">Self-Saved</span></td>
      <td><strong>LinkedIn Job #1</strong><br>View ID: 4442081334</td>
      <td>Self-saved LinkedIn job link — details unknown without clicking. Saved last night.</td>
      <td><span class="pri-med">MEDIUM</span></td>
      <td>Open link and review today</td>
    </tr>
    <tr class="row-green">
      <td><span class="badge green">Self-Saved</span></td>
      <td><strong>LinkedIn Job #2</strong><br>View ID: 4446457434</td>
      <td>Self-saved LinkedIn job link — details unknown without clicking. Saved last night.</td>
      <td><span class="pri-med">MEDIUM</span></td>
      <td>Open link and review today</td>
    </tr>
    <tr class="row-green">
      <td><span class="badge green">Self-Saved</span></td>
      <td><strong>LinkedIn Job #3</strong><br>View ID: 4449915880</td>
      <td>Self-saved LinkedIn job link — details unknown without clicking. Saved last night.</td>
      <td><span class="pri-med">MEDIUM</span></td>
      <td>Open link and review today</td>
    </tr>
    <tr class="row-green">
      <td><span class="badge green">Self-Saved</span></td>
      <td><strong>LinkedIn Profile</strong><br>vanchic</td>
      <td>Self-emailed LinkedIn profile link — likely a contact or referral to follow up with.</td>
      <td><span class="pri-med">MEDIUM</span></td>
      <td>Review profile — send connection request or message</td>
    </tr>
    <tr class="row-green">
      <td><span class="badge teal">JobLeads</span></td>
      <td><strong>Headhunter Match</strong><br>JobLeads (ID: 5431594)</td>
      <td>Headhunter database match for your field — active as of Aug 6.</td>
      <td><span class="pri-med">MEDIUM</span></td>
      <td>Review recruiter profile and make contact</td>
    </tr>
    <tr class="row-gray">
      <td><span class="badge gray">Glassdoor</span></td>
      <td><strong>10 Jobs in New York, NY</strong><br>Various (incl. Goodwill, Archway)</td>
      <td>In trash — low relevance matches including Community Home Manager. May not fit target level.</td>
      <td><span class="pri-low">LOW</span></td>
      <td>Review if time permits — currently in trash</td>
    </tr>
    <tr class="row-gray">
      <td><span class="badge gray">JobLeads</span></td>
      <td><strong>5 CPO / Culture Jobs (Aug 5)</strong><br>Various</td>
      <td>In trash — saved search for Chief People Officer / Culture / Change. Digest format.</td>
      <td><span class="pri-low">LOW</span></td>
      <td>Review digest in trash — may contain relevant leads</td>
    </tr>
    <tr class="row-blue">
      <td><span class="badge blue">Networking</span></td>
      <td><strong>HR Networking Open Office Hours</strong><br>~175 HR Professionals</td>
      <td>Today 12–1 PM via Zoom. RSVP pending. Great venue for leads, referrals, and warm introductions.</td>
      <td><span class="pri-high">HIGH</span></td>
      <td>RSVP now and attend — turn off AI note tools</td>
    </tr>
    <tr class="row-blue">
      <td><span class="badge blue">Networking</span></td>
      <td><strong>HR Networking Group — Zoom 2</strong><br>~175 HR Professionals</td>
      <td>Aug 12, 12–1:30 PM. RSVP pending. Same community, weekly session.</td>
      <td><span class="pri-high">HIGH</span></td>
      <td>RSVP and prepare brief intro + questions</td>
    </tr>
    <tr class="row-purple">
      <td><span class="badge purple">Recruiter</span></td>
      <td><strong>MoralesHR — Shelly Morales</strong><br>Engineering, Product, GTM roles</td>
      <td>Weekly open roles digest from human-centered recruiter. Already read. Check for relevant roles.</td>
      <td><span class="pri-low">LOW</span></td>
      <td>Scan for any People/HR adjacent opportunities</td>
    </tr>
  </tbody>
</table>

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 6: FULL EMAIL REVIEW BY CATEGORY
═══════════════════════════════════════════════════════════════ -->
<h2 class="section-title dark">📂 Full Email Review by Category</h2>

<!-- SECURITY / RISK -->
<h3 class="section-title red" style="font-size:14px;">🔴 Security / Risk</h3>
<div class="card red">
  <div class="card-title">Count: 7 emails</div>
  <div class="card-body">
    <p><strong>Bank of America (2 emails — REAL, INBOX):</strong> Fraud claim Step 2 of 3 — temporary credit issued on account -2994. Legitimate sender domain (ealerts.bankofamerica.com). Verify claim status immediately via official app.</p>
    <br>
    <p><strong>Auto-Trashed — Phishing (2 emails):</strong></p>
    <ul style="margin-left:18px;margin-top:4px;">
      <li><strong>Fake AAA Prize Scam</strong> — "Re: Congratulations! melissaw212 You've won an AAA Car Cooler" from gedpicqbgedpicqb.ca. Classic credential-harvesting scam impersonating AAA. Auto-trashed. No action needed.</li>
      <li><strong>Spoofed Storage Alert</strong> — "Storage Limit Reached (100%)" appearing to be from melissaw212 but from suspicious domain (fxizycxdwcfoo.harbor.galaxy.funbet1...org). Fake billing urgency to harvest credentials/payment info. Auto-trashed. No action needed.</li>
    </ul>
    <br>
    <p><strong>Adult Spam / Phishing (3 emails — NOT trashed, flagged):</strong> "Hot Sex" sender, "Get Hard" sender, "Bigger Thicker Dick" sender — all from random suspicious domains with exploitative content and malicious links. Do not open or click. Delete immediately.</p>
  </div>
  <div class="pill-row"><span class="badge red">ACTION: Verify BofA Claim</span><span class="badge gray">Auto-Trashed Phishing: No Action</span><span class="badge red">Delete Adult Spam Now</span></div>
</div>

<!-- JOB SEARCH -->
<h3 class="section-title green" style="font-size:14px;">🟢 Job Search</h3>
<div class="card green">
  <div class="card-title">Count: 13 emails</div>
  <div class="card-body">
    <p><strong>LinkedIn Job Alerts (4 emails):</strong> VP People Technology — Avalara (actively recruiting); Senior Director People Partner — Zeta Global (actively recruiting); Director of People Remote — GridUnity (2 alerts, duplicate). All high priority.</p>
    <br>
    <p><strong>Self-Sent Job Links (5 emails from melissaw212@gmail.com):</strong> 3 LinkedIn job view links (IDs: 4442081334, 4446457434, 4449915880), 1 cape.co job link, 1 LinkedIn profile link (vanchic). Saved last night for review today.</p>
    <br>
    <p><strong>JobLeads (2 emails — 1 in inbox, 1 in trash):</strong> Inbox: individual headhunter match (ID 5431594) active today. Trash: 5-job digest for CPO/Culture/Change saved search (Aug 5).</p>
    <br>
    <p><strong>Glassdoor (1 email — trash):</strong> 10 jobs in NY including community manager/Goodwill — likely below target level. Review if time allows.</p>
  </div>
  <div class="pill-row"><span class="badge green">Apply: Avalara, Zeta Global, GridUnity</span><span class="badge yellow">Review: Self-Saved Links</span><span class="badge gray">Low: Glassdoor digest</span></div>
</div>

<!-- RECRUITERS / NETWORKING -->
<h3 class="section-title green" style="font-size:14px;">🟢 Recruiters / Networking</h3>
<div class="card green">
  <div class="card-title">Count: 1 email</div>
  <div class="card-body">
    <p><strong>Shelly Morales / MoralesHR (shelly@moraleshr.com):</strong> Weekly open roles digest — Engineering, Product, Go to Market. Read, not in inbox. Check for any People/HR-adjacent listings that could expand network.</p>
  </div>
  <div class="pill-row"><span class="badge teal">Scan for Relevant Roles</span></div>
</div>

<!-- CALENDAR / EVENTS -->
<h3 class="section-title blue" style="font-size:14px;">🔵 Calendar / Events</h3>
<div class="card blue">
  <div class="card-title">Count: 1 email</div>
  <div class="card-body">
    <p><strong>AllEvents (updates@allevents.in) — In Trash:</strong> Generic event recommendations. Already trashed. No action needed.</p>
  </div>
  <div class="pill-row"><span class="badge gray">In Trash — No Action</span></div>
</div>

<!-- MEDICAL / HEALTH -->
<h3 class="section-title red" style="font-size:14px;">🏥 Medical / Health</h3>
<div class="card red">
  <div class="card-title">Count: 1 email</div>
  <div class="card-body">
    <p><strong>Ozempic by DirectMeds (spam/suspicious):</strong> "What If You Could Lose Weight Effortlessly?" — Not from a legitimate medical provider. Suspicious domain (9z8iyy.dbzl58.r4qoqd.us). Not in inbox. Do not click. Delete.</p>
    <p style="margin-top:6px;font-style:italic;font-size:12px;">Note: Actual medical appointments (MRI, PT, disability) are tracked via Calendar above.</p>
  </div>
  <div class="pill-row"><span class="badge red">Delete — Medical Spam</span></div>
</div>

<!-- FINANCIAL / BILLING -->
<h3 class="section-title yellow" style="font-size:14px;">🟡 Financial / Billing</h3>
<div class="card yellow">
  <div class="card-title">Count: 3 emails</div>
  <div class="card-body">
    <p><strong>Bank of America (2 — URGENT, in inbox):</strong> Fraud claim processing on account -2994. Verify immediately. See Action Required section.</p>
    <br>
    <p><strong>JetBlue Plus Card / Barclays (1 — RESCUED from trash):</strong> 8.99% promo APR offer on purchases. Legitimate sender (emails.barclaysus.com). Rescued from trash as protected sender. Review if you want to activate the promo rate.</p>
    <br>
    <p><strong>Apify Community (1 — in inbox):</strong> Pricing change for Rapid LinkedIn Jobs Scraper tool. Review cost impact on job search automation workflow.</p>
  </div>
  <div class="pill-row"><span class="badge red">URGENT: Verify BofA</span><span class="badge teal">Review: Barclays Promo</span><span class="badge yellow">Note: Apify Pricing Change</span></div>
</div>

<!-- PROFESSIONAL DEVELOPMENT -->
<h3 class="section-title purple" style="font-size:14px;">🟣 Professional Development</h3>
<div class="card purple">
  <div class="card-title">Count: 5 emails</div>
  <div class="card-body">
    <p><strong>BambooHR (1):</strong> "Defense Against Quiet Quitting" free checklist — 20+ culture engagement tactics. Relevant as an HR professional. Not in inbox but not trashed. Review if useful for positioning.</p>
    <br>
    <p><strong>The People People Group (1 — trash):</strong> Community digest — mandatory work trials for engineers, feedback preferences. Trashed but HR-relevant topics.</p>
    <br>
    <p><strong>Charles Schwab Coaching (1 — inbox):</strong> August webcast lineup — financial wellness and investment education. Low urgency but worth scanning for relevant sessions.</p>
    <br>
    <p><strong>Daniel Williams / Claude Code for Non-Coders (1):</strong> Newsletter — "There's No Self-Improving AI. You Still Need to Aim It." Read, not in inbox. AI literacy topic — relevant for staying current in HR tech space.</p>
    <br>
    <p><strong>Medium / DeepSeek V4 Flash (1 — trash):</strong> Open-source AI model review. Trashed. Low priority unless interested in AI tools.</p>
  </div>
  <div class="pill-row"><span class="badge purple">Review: BambooHR Checklist</span><span class="badge gray">Low: Schwab Webcasts</span><span class="badge gray">Trash: Medium/DeepSeek</span></div>
</div>

<!-- PERSONAL -->
<h3 class="section-title gray" style="font-size:14px;">⚪ Personal</h3>
<div class="card gray">
  <div class="card-title">Count: 3 emails</div>
  <div class="card-body">
    <p><strong>Match (2 emails — inbox):</strong> "Steve likes you" and "Steve viewed your profile" — Steve, 65, Forest Hills NY. Two notifications for same user. Personal matter — review at your discretion.</p>
    <br>
    <p><strong>OkCupid (1):</strong> "You're a catch 🎣" — generic engagement notification. Not in inbox. Low priority.</p>
    <br>
    <p><strong>Google Account (1):</strong> "You shared Google Account data with FreeConvert.com" — informational sign-in notification. Legitimate Google email. No action needed unless you don't recognize using FreeConvert.</p>
  </div>
  <div class="pill-row"><span class="badge gray">Personal — Review at Discretion</span><span class="badge blue">Verify: Google/FreeConvert if Unfamiliar</span></div>
</div>

<!-- NEWSLETTERS / SUBSCRIPTIONS -->
<h3 class="section-title purple" style="font-size:14px;">🟣 Newsletters &amp; Subscriptions</h3>
<div class="card purple">
  <div class="card-title">Count: 6 emails</div>
  <div class="card-body">
    <p><strong>1% Better Newsletter (trash):</strong> Dallas Cowboys sale, Chipotle outbreak, Ray Dalio AI bubble warning. General business/news digest. In trash.</p>
    <p><strong>Dylan's Diary — Behind the Markets (trash):</strong> SpaceX-Tesla merger analysis. Finance/markets newsletter. In trash.</p>
    <p><strong>The Daily Skimm (trash):</strong> "Iguana know more" — Aug 6 daily news digest. In trash.</p>
    <p><strong>Gemma Bonham-Carter (trash):</strong> Monthly rewind July 2026. Creator/business newsletter. Auto-newsletter-trashed.</p>
    <p><strong>Quince (auto-newsletter-trashed):</strong> "New tops are in" — retail newsletter. Auto-trashed as newsletter.</p>
    <p><strong>Insider Monkey (trash):</strong> Daily financial newsletter Aug 5. In trash.</p>
  </div>
  <div class="pill-row"><span class="badge gray">All In Trash — No Action Needed</span><span class="badge purple">Consider Unsubscribing from Low-Value Senders</span></div>
</div>

<!-- PROMOTIONAL / RETAIL -->
<h3 class="section-title gray" style="font-size:14px;">⚪ Promotional / Retail</h3>
<div class="card gray">
  <div class="card-title">Count: 8 emails</div>
  <div class="card-body">
    <p><strong>Old Navy (2 — 1 inbox, 1 not):</strong> Order #1RDGPJ0 arriving soon (inbox, read). Super Cash savings code up to $60 — not in inbox, unread.</p>
    <p><strong>Gap Factory (1 — trash):</strong> Extra 15% off + 40-70% sitewide. Trashed.</p>
    <p><strong>Kohl's (1 — trash):</strong> Extra 30% off Exclusive Cardholder Event. Trashed.</p>
    <p><strong>CVS ExtraCare (1 — inbox):</strong> $2 coupon. Low value.</p>
    <p><strong>Chick-fil-A (1 — inbox):</strong> Reward from local store — 402 pts available.</p>
    <p><strong>Alison Courses (1 — trash):</strong> 25% off certifications. Trashed.</p>
    <p><strong>Gemma Bonham-Carter (1 — see Newsletters above)</strong></p>
  </div>
  <div class="pill-row"><span class="badge yellow">Track: Old Navy Order Arriving</span><span class="badge gray">Low: CVS, Chick-fil-A</span><span class="badge gray">Delete: Kohl's, Gap, Alison</span></div>
</div>

<!-- SAFE TO DELETE / IGNORE -->
<h3 class="section-title gray" style="font-
