<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa | July 29, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* Header */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 15px; color: #a8c8e8; margin-top: 6px; }
  .header-meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header-meta .meta-item { background: rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 18px; }
  .header-meta .meta-item .label { font-size: 11px; color: #a8c8e8; text-transform: uppercase; letter-spacing: 1px; }
  .header-meta .meta-item .value { font-size: 20px; font-weight: 700; color: #fff; }

  /* Section headers */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; padding: 10px 16px; border-radius: 8px 8px 0 0; margin-bottom: 0; }
  .section-body { background: #fff; border-radius: 0 0 10px 10px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }

  /* Color themes */
  .red .section-title    { background: #c0392b; color: #fff; }
  .yellow .section-title { background: #e67e22; color: #fff; }
  .blue .section-title   { background: #2471a3; color: #fff; }
  .green .section-title  { background: #1e8449; color: #fff; }
  .purple .section-title { background: #6c3483; color: #fff; }
  .gray .section-title   { background: #5d6d7e; color: #fff; }
  .teal .section-title   { background: #117a65; color: #fff; }
  .navy .section-title   { background: #1a1a2e; color: #fff; }
  .orange .section-title { background: #b7770d; color: #fff; }

  /* Executive Summary bullets */
  .exec-bullets { list-style: none; }
  .exec-bullets li { padding: 10px 14px; margin-bottom: 8px; border-radius: 7px; border-left: 5px solid; font-size: 14px; }
  .exec-bullets .risk   { background: #fdecea; border-color: #c0392b; }
  .exec-bullets .opp    { background: #eafaf1; border-color: #1e8449; }
  .exec-bullets .cal    { background: #eaf4fb; border-color: #2471a3; }

  /* Cards */
  .card { border-radius: 8px; padding: 14px 16px; margin-bottom: 12px; border-left: 5px solid; }
  .card-red    { background: #fdecea; border-color: #c0392b; }
  .card-yellow { background: #fef9e7; border-color: #e67e22; }
  .card-blue   { background: #eaf4fb; border-color: #2471a3; }
  .card-green  { background: #eafaf1; border-color: #1e8449; }
  .card-purple { background: #f5eef8; border-color: #6c3483; }
  .card-gray   { background: #f2f3f4; border-color: #85929e; }
  .card-teal   { background: #e8f8f5; border-color: #117a65; }
  .card .card-title { font-weight: 700; font-size: 15px; margin-bottom: 4px; }
  .card .card-meta  { font-size: 12px; color: #555; margin-bottom: 6px; }
  .card .card-body  { font-size: 13px; }
  .card .card-action { margin-top: 8px; font-weight: 600; font-size: 13px; }
  .card .card-due   { font-size: 11px; color: #888; margin-top: 4px; }

  /* Tables */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #1a1a2e; color: #fff; padding: 9px 10px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
  td { padding: 8px 10px; border-bottom: 1px solid #e8e8e8; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #f7f8fa; }
  tr:hover td { background: #eef2ff; }

  /* Badges */
  .badge { display: inline-block; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: 700; margin-left: 4px; }
  .badge-red    { background: #c0392b; color: #fff; }
  .badge-yellow { background: #e67e22; color: #fff; }
  .badge-green  { background: #1e8449; color: #fff; }
  .badge-blue   { background: #2471a3; color: #fff; }
  .badge-purple { background: #6c3483; color: #fff; }
  .badge-gray   { background: #85929e; color: #fff; }
  .badge-teal   { background: #117a65; color: #fff; }

  /* Priority */
  .priority-high   { color: #c0392b; font-weight: 700; }
  .priority-medium { color: #e67e22; font-weight: 700; }
  .priority-low    { color: #1e8449; font-weight: 700; }

  /* Status tags */
  .tag { display: inline-block; padding: 2px 9px; border-radius: 12px; font-size: 11px; font-weight: 700; }
  .tag-accepted { background: #eafaf1; color: #1e8449; border: 1px solid #1e8449; }
  .tag-declined { background: #fdecea; color: #c0392b; border: 1px solid #c0392b; }
  .tag-pending  { background: #fef9e7; color: #b7770d; border: 1px solid #b7770d; }
  .tag-confirmed{ background: #eaf4fb; color: #2471a3; border: 1px solid #2471a3; }
  .tag-phish    { background: #c0392b; color: #fff; }
  .tag-auto     { background: #85929e; color: #fff; }

  /* Divider */
  .divider { border: none; border-top: 2px solid #e0e4ea; margin: 16px 0; }

  /* Triage table */
  .triage-status { font-size: 13px; white-space: nowrap; }
  .triage-subject { font-weight: 600; }
  .triage-summary { color: #444; }

  /* Day header */
  .day-header { background: #1a1a2e; color: #fff; padding: 7px 14px; border-radius: 6px; margin: 14px 0 8px; font-weight: 700; font-size: 14px; }

  /* Cal event row */
  .cal-event { background: #fff; border: 1px solid #dde3ea; border-left: 4px solid #2471a3; border-radius: 6px; padding: 10px 14px; margin-bottom: 8px; }
  .cal-event.confirmed   { border-left-color: #1e8449; }
  .cal-event.declined    { border-left-color: #c0392b; opacity: 0.75; }
  .cal-event.pending     { border-left-color: #e67e22; }
  .cal-event.allday      { border-left-color: #6c3483; }
  .cal-event .ev-title   { font-weight: 700; font-size: 14px; }
  .cal-event .ev-meta    { font-size: 12px; color: #555; margin-top: 3px; }
  .cal-event .ev-prep    { font-size: 12px; color: #2471a3; margin-top: 4px; font-style: italic; }
  .cal-event .ev-conflict{ font-size: 12px; color: #c0392b; font-weight: 700; margin-top: 3px; }

  /* Footer */
  .footer { text-align: center; color: #aaa; font-size: 12px; margin-top: 32px; padding: 16px; }

  /* Grid 2-col */
  .grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  @media(max-width: 700px){ .grid2 { grid-template-columns: 1fr; } .header-meta { gap: 12px; } }

  /* Dashboard widgets */
  .widget { background: #fff; border-radius: 10px; padding: 14px 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .widget h4 { font-size: 13px; text-transform: uppercase; letter-spacing: 0.8px; color: #555; margin-bottom: 10px; }
  .widget .big-num { font-size: 36px; font-weight: 800; }
  .widget ul { list-style: none; }
  .widget ul li { padding: 5px 0; border-bottom: 1px solid #f0f0f0; font-size: 13px; }
  .widget ul li:last-child { border-bottom: none; }

  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)); gap: 14px; }

  /* Accounting total row */
  .total-row td { font-weight: 800; background: #1a1a2e !important; color: #fff; }

  .note { font-size: 12px; color: #777; font-style: italic; margin-top: 8px; }
  .warn { font-size: 12px; color: #c0392b; font-weight: 700; }
  .success { font-size: 12px; color: #1e8449; font-weight: 700; }

  .group-label { font-weight: 700; font-size: 13px; margin: 10px 0 4px; color: #333; }
  .indent { padding-left: 16px; }

  .fit-high   { color: #1e8449; font-weight: 700; }
  .fit-medium { color: #b7770d; font-weight: 700; }
  .fit-low    { color: #85929e; font-weight: 700; }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════
     0. EMAIL TRIAGE QUICK LIST
════════════════════════════════════════════════════ -->
<div class="section navy">
  <div class="section-title">📋 Email Triage Quick List</div>
  <div class="section-body" style="padding:0;">
    <table>
      <thead>
        <tr>
          <th style="width:140px;">Status</th>
          <th style="width:200px;">From</th>
          <th>Subject</th>
          <th>Summary</th>
        </tr>
      </thead>
      <tbody>
        <!-- INBOX EMAILS — individual rows -->
        <tr>
          <td class="triage-status">📥 INBOX</td>
          <td>Zappos</td>
          <td class="triage-subject">The trail isn't going to run itself</td>
          <td class="triage-summary">KEEN shoe promo — low priority retail</td>
        </tr>
        <tr>
          <td class="triage-status">📥 INBOX</td>
          <td>Chewy.com</td>
          <td class="triage-subject">For pets who love game day</td>
          <td class="triage-summary">Pet toys/treats promo — low priority retail</td>
        </tr>
        <tr>
          <td class="triage-status">📥 INBOX</td>
          <td>USPS Informed Delivery</td>
          <td class="triage-subject">Your Daily Digest for Wed, 7/29 is ready</td>
          <td class="triage-summary">1 mailpiece arriving today — review if expecting something</td>
        </tr>
        <tr>
          <td class="triage-status">📥 INBOX</td>
          <td>The Daily Skimm</td>
          <td class="triage-subject">Errand dates forever</td>
          <td class="triage-summary">Morning newsletter — read when convenient</td>
        </tr>
        <tr>
          <td class="triage-status">📥 INBOX</td>
          <td>Linktree</td>
          <td class="triage-subject">Pre-album drop: the Ariana Grande theme</td>
          <td class="triage-summary">Linktree promo/theme update — low priority</td>
        </tr>
        <tr>
          <td class="triage-status">📥 INBOX</td>
          <td>Citizens Careers</td>
          <td class="triage-subject">New jobs for you!</td>
          <td class="triage-summary">Strategy Sr Associate role — review for fit</td>
        </tr>
        <tr>
          <td class="triage-status">📥 INBOX</td>
          <td>Carmel Car Service</td>
          <td class="triage-subject">International Friendship Day 2026 (×2 in inbox)</td>
          <td class="triage-summary">Duplicate marketing emails — delete both</td>
        </tr>
        <tr>
          <td class="triage-status">📥 INBOX</td>
          <td>Bank of America</td>
          <td class="triage-subject">Direct deposit credited — $80 from Acorns</td>
          <td class="triage-summary">$80 Acorns deposit to checking acct #7471 — informational</td>
        </tr>
        <tr>
          <td class="triage-status">📥 INBOX</td>
          <td>Bank of America</td>
          <td class="triage-subject">Billing Dispute acct-2994: Claim being reviewed</td>
          <td class="triage-summary">Dispute Step 2 of 3 — merchant's bank reviewing</td>
        </tr>
        <tr>
          <td class="triage-status">📥 INBOX</td>
          <td>Bank of America</td>
          <td class="triage-subject">Billing Dispute acct-2994: Merchant credit issued</td>
          <td class="triage-summary">Credit issued — monitor account for posting <span class="badge badge-yellow">ACTION</span></td>
        </tr>
        <tr>
          <td class="triage-status">📥 INBOX</td>
          <td>LinkedIn Job Alerts</td>
          <td class="triage-subject">Chief Human Resources Officer at Edged</td>
          <td class="triage-summary">CHRO role — high-fit senior opportunity</td>
        </tr>
        <tr>
          <td class="triage-status">📥 INBOX</td>
          <td>LinkedIn</td>
          <td class="triage-subject">New jobs similar to Head of HR at EWC Growth</td>
          <td class="triage-summary">HR Director-level job matches — review list</td>
        </tr>
        <!-- TRASH SUMMARY ROWS -->
        <tr style="background:#fff3cd;">
          <td class="triage-status">🗑 TRASHED (auto)</td>
          <td colspan="3"><strong>4 emails auto-trashed (2 phishing, 2 spam health/promo)</strong> — see Trash Review for details</td>
        </tr>
        <tr style="background:#f2f3f4;">
          <td class="triage-status">🗂 TRASH (manual)</td>
          <td colspan="3"><strong>~27 emails in Trash</strong> (newsletters, digests, job alerts, retail, misc) — see Trash Review for details</td>
        </tr>
      </tbody>
    </table>
    <p class="note" style="padding:10px 14px;">Sort order: Inbox emails shown individually → Auto-trash summary → Manual trash summary. Rescued emails: none flagged in this data set.</p>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     1. HEADER
════════════════════════════════════════════════════ -->
<div class="header">
  <h1>🌅 Good Morning, Melissa</h1>
  <div class="subtitle">Executive Briefing — Wednesday, July 29, 2026</div>
  <div class="header-meta">
    <div class="meta-item">
      <div class="label">Date</div>
      <div class="value">Wed · Jul 29</div>
    </div>
    <div class="meta-item">
      <div class="label">Emails Reviewed</div>
      <div class="value">50</div>
    </div>
    <div class="meta-item">
      <div class="label">Calendar Events</div>
      <div class="value">10</div>
    </div>
    <div class="meta-item">
      <div class="label">Action Required</div>
      <div class="value" style="color:#f0a500;">6</div>
    </div>
    <div class="meta-item">
      <div class="label">Security Alerts</div>
      <div class="value" style="color:#e74c3c;">4</div>
    </div>
    <div class="meta-item">
      <div class="label">Open Job Leads</div>
      <div class="value" style="color:#2ecc71;">5</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     2. EXECUTIVE SUMMARY
════════════════════════════════════════════════════ -->
<div class="section red">
  <div class="section-title">⚡ Executive Summary</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li class="risk">🔴 <strong>Security:</strong> 4 emails flagged as phishing/spam were removed — 2 auto-trashed before delivery (cloud account lock scams spoofing your username). Additionally, a suspicious "Healthy_Lungs," "Blood Sugar Alert," and "Lung Clearing Method" spam remain in the non-inbox queue. Your accounts are safe; no action required beyond awareness. Billing dispute on BofA acct-2994 has a merchant credit issued — confirm it posts.</li>
      <li class="opp">🟢 <strong>Job Search:</strong> Strong executive pipeline today — CHRO role at Edged (LinkedIn alert), Sr. HR Director up to $350K/yr (LinkedIn), Head of HR at EWC Growth (similar roles), and a Medical Director role at Horizon BCBSNJ. Application viewed by "Super Hire Staff." Citizens Careers flagged a Strategy Sr. Associate role. Today's HR Networking &amp; Job Search Group call is at noon — RSVP still pending.</li>
      <li class="cal">🔵 <strong>Calendar:</strong> You have 3 overlapping commitments from 11 AM–1:30 PM today: PromptMates Live AI webinar (11–12), Benefits Roundtable (12–1, no RSVP), and HR Networking Group Zoom (12–1:30, no RSVP). You also have a personal reminder to email Dr. Hollander at 11 AM. Resolve conflicts and send that email now.</li>
    </ul>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     3. ACTION REQUIRED
════════════════════════════════════════════════════ -->
<div class="section yellow">
  <div class="section-title">🚨 Action Required</div>
  <div class="section-body">

    <div class="card card-red">
      <div class="card-title">🔐 Confirm BofA Billing Dispute Credit Posts</div>
      <div class="card-meta">From: Bank of America | Acct: -2994 | Date: Jul 29</div>
      <div class="card-body">Two separate emails indicate: (1) the merchant's bank is reviewing your claim and (2) a merchant credit has been issued. These may be sequential updates on the same dispute at Step 2 of 3. Confirm the credit appears in your account and monitor for Step 3 (final resolution).</div>
      <div class="card-action">→ Log into BofA and verify the credit posted to acct -2994.</div>
      <div class="card-due">⏰ Due: Today, July 29</div>
    </div>

    <div class="card card-blue">
      <div class="card-title">📧 Email Dr. Hollander</div>
      <div class="card-meta">From: Calendar Reminder | 11:00 AM today</div>
      <div class="card-body">You have a calendar task set for 11 AM to email Dr. Hollander. No details provided — likely a medical follow-up. This conflicts with the PromptMates Live webinar also at 11 AM.</div>
      <div class="card-action">→ Send email to Dr. Hollander before or immediately after 11 AM webinar begins.</div>
      <div class="card-due">⏰ Due: Today by noon</div>
    </div>

    <div class="card card-blue">
      <div class="card-title">📅 RSVP: Benefits Roundtable & HR Networking Zoom</div>
      <div class="card-meta">From: Calendar | 12:00–1:30 PM today | Status: needsAction</div>
      <div class="card-body">Two events at noon require RSVP responses: "The Future of Benefits" HIC HR Roundtable (Zoom, 12–1 PM) and "HR Networking &amp; Job Search Group" (Zoom 2, 12–1:30 PM). These overlap. Choose one and RSVP/decline the other.</div>
      <div class="card-action">→ RSVP to your preferred noon session; decline the other. Both have Zoom links in calendar.</div>
      <div class="card-due">⏰ Due: Before 12:00 PM today</div>
    </div>

    <div class="card card-green">
      <div class="card-title">💼 Review CHRO at Edged — High-Fit Opportunity</div>
      <div class="card-meta">From: LinkedIn Job Alerts | Date: Jul 29</div>
      <div class="card-body">Chief Human Resources Officer role at Edged posted 7/28. This is a senior executive-level match for your profile. Application may be time-sensitive given recent posting date.</div>
      <div class="card-action">→ Review the full posting on LinkedIn and apply or save before it closes.</div>
      <div class="card-due">⏰ Due: Today or tomorrow</div>
    </div>

    <div class="card card-green">
      <div class="card-title">💼 Review Sr. HR Director — Up to $350K/Year</div>
      <div class="card-meta">From: LinkedIn Job Alerts | Date: Jul 29 (posted 7/26)</div>
      <div class="card-body">Confidential company, Sr. HR Director role with compensation up to $350K/year. Posted 7/26 — apply promptly before the window closes.</div>
      <div class="card-action">→ Access LinkedIn alert, review posting, and apply or save immediately.</div>
      <div class="card-due">⏰ Due: Today</div>
    </div>

    <div class="card card-yellow">
      <div class="card-title">🗑️ Clean Up Carmel Car Service Duplicate Emails</div>
      <div class="card-meta">From: Carmel Car Service | 4 copies in various folders</div>
      <div class="card-body">Carmel Car Service sent the same "International Friendship Day" promo at least 4 times across your inbox (2 live in inbox, 2 in non-inbox/read). This is a sign of poor list management or a deliverability issue. Delete all and consider unsubscribing.</div>
      <div class="card-action">→ Delete all 4 Carmel Car Service emails and click Unsubscribe.</div>
      <div class="card-due">⏰ Due: Today (housekeeping)</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     4. FULL 7-DAY CALENDAR
════════════════════════════════════════════════════ -->
<div class="section blue">
  <div class="section-title">📅 Full 7-Day Calendar</div>
  <div class="section-body">

    <div class="day-header">Wednesday, July 29, 2026 — TODAY</div>

    <div class="cal-event confirmed">
      <div class="ev-title">🤖 How A VP Talent Builds with AI — PromptMates Live</div>
      <div class="ev-meta">⏰ 11:00 AM – 12:00 PM &nbsp;|&nbsp; <span class="tag tag-accepted">✅ Accepted</span> &nbsp;|&nbsp; 🔗 <a href="https://luma.com/join/g-sAv9NHMvqDBBXrx" target="_blank">Luma Join Link</a></div>
      <div class="ev-prep">📝 Prep: Free webinar for HR/Recruitment professionals on AI & automation. Emily Gransky, VP Talent, presenting. Join link confirmed. Have questions ready.</div>
      <div class="ev-conflict">⚠️ CONFLICT: Overlaps with "Email Dr. Hollander" reminder (11 AM). Send that email before joining.</div>
    </div>

    <div class="cal-event confirmed">
      <div class="ev-title">📧 Email Dr. Hollander (Personal Task)</div>
      <div class="ev-meta">⏰ 11:00 AM – 12:00 PM &nbsp;|&nbsp; <span class="tag tag-confirmed">✅ Confirmed</span> &nbsp;|&nbsp; 📍 No location</div>
      <div class="ev-prep">📝 Prep: Compose and send email before or right at 11 AM, before joining the webinar.</div>
      <div class="ev-conflict">⚠️ CONFLICT: Same time block as PromptMates Live webinar.</div>
    </div>

    <div class="cal-event pending">
      <div class="ev-title">🏥 The Future of Benefits: Why Healthcare Alone Isn't Enough — HIC HR & L&D Roundtable</div>
      <div class="ev-meta">⏰ 12:00 PM – 1:00 PM &nbsp;|&nbsp; <span class="tag tag-pending">⏳ No RSVP</span> &nbsp;|&nbsp; 🔗 <a href="https://us06web.zoom.us/j/5224221004?pwd=UU5YNmlFckpjQnlzc2FDMHFlNUhhUT09" target="_blank">Zoom Link</a></div>
      <div class="ev-prep">📝 Prep: Roundtable with senior HR and People leaders; CEO of CareCrowd featured. Relevant to benefits strategy knowledge.</div>
      <div class="ev-conflict">⚠️ CONFLICT: Overlaps with HR Networking & Job Search Group (12–1:30 PM). Choose one and RSVP immediately.</div>
    </div>

    <div class="cal-event pending">
      <div class="ev-title">🤝 HR Networking & Job Search Group — Zoom 2</div>
      <div class="ev-meta">⏰ 12:00 PM – 1:30 PM &nbsp;|&nbsp; <span class="tag tag-pending">⏳ No RSVP</span> &nbsp;|&nbsp; 🔗 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a></div>
      <div class="ev-prep">📝 Prep: Large HR networking group (180+ attendees). Active job search networking opportunity. Note: organizer requests NO automated AI notetaking tools.</div>
      <div class="ev-conflict">⚠️ CONFLICT: Overlaps with Benefits Roundtable (12–1 PM). Decision required.</div>
    </div>

    <div class="cal-event confirmed">
      <div class="ev-title">🌐 Network (Personal Reminder)</div>
      <div class="ev-meta">⏰ 12:00 PM – 1:30 PM &nbsp;|&nbsp; <span class="tag tag-confirmed">✅ Confirmed</span> &nbsp;|&nbsp; 📍 No location</div>
      <div class="ev-prep">📝 Prep: Likely a general reminder aligned with one of the noon Zoom sessions. No separate link — no additional action needed.</div>
    </div>

    <hr class="divider">
    <div class="day-header">Thursday, July 30, 2026</div>

    <div class="cal-event declined">
      <div class="ev-title">🏢 Executive Roundtable (John Madigan)</div>
      <div class="ev-meta">⏰ 9:00 AM – 10:30 AM &nbsp;|&nbsp; <span class="tag tag-declined">❌ Declined</span> &nbsp;|&nbsp; 🔗 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a></div>
      <div class="ev-prep">📝 Note: You have declined this event. No action needed unless you wish to reconsider. Host is John Madigan.</div>
    </div>

    <div class="cal-event pending">
      <div class="ev-title">🤝 HR Networking & Job Search: Open Office Hours — Zoom 2</div>
      <div class="ev-meta">⏰ 12:00 PM – 1:00 PM &nbsp;|&nbsp; <span class="tag tag-pending">⏳ No RSVP</span> &nbsp;|&nbsp; 🔗 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a></div>
      <div class="ev-prep">📝 Prep: Open office hours format — lower-pressure networking. Good for 1:1 connection building. Note: AI notetaking tools not permitted per organizer.</div>
    </div>

    <hr class="divider">
    <div class="day-header">Friday, July 31, 2026</div>
    <p style="color:#888; font-style:italic; padding: 8px 4px;">No events scheduled.</p>

    <hr class="divider">
    <div class="day-header">Saturday, August 1, 2026</div>

    <div class="cal-event confirmed">
      <div class="ev-title">👁️ Eye Doctor Appointment</div>
      <div class="ev-meta">⏰ 2:30 PM – 3:30 PM &nbsp;|&nbsp; <span class="tag tag-confirmed">✅ Confirmed</span> &nbsp;|&nbsp; 📍 Location not listed</div>
      <div class="ev-prep">📝 Prep: Confirm appointment address. Arrange transportation if needed — may affect vision temporarily. Block 30–60 min after for recovery.</div>
    </div>

    <hr class="divider">
    <div class="day-header">Sunday, August 2, 2026</div>

    <div class="cal-event allday">
      <div class="ev-title">🎂 Shari's Birthday (All Day)</div>
      <div class="ev-meta">📅 All Day — August 2 &nbsp;|&nbsp; <span class="tag tag-confirmed">✅ Confirmed</span></div>
      <div class="ev-prep">📝 Prep: Send a card, message, or gift today if you haven't already. Note: this is listed as confirmed in your calendar.</div>
    </div>

    <hr class="divider">
    <div class="day-header">Tuesday, August 4, 2026</div>

    <div class="cal-event confirmed">
      <div class="ev-title">🦵 Physical Therapy (PT)</div>
      <div class="ev-meta">⏰ 10:00 AM – 11:00 AM &nbsp;|&nbsp; <span class="tag tag-confirmed">✅ Confirmed</span> &nbsp;|&nbsp; 📍 Location not listed</div>
      <div class="ev-prep">📝 Prep: Confirm PT clinic address and any preparation instructions. Wear comfortable clothing. Block transit time before and after.</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     5. JOB SEARCH & INTERVIEW PIPELINE
════════════════════════════════════════════════════ -->
<div class="section green">
  <div class="section-title">💼 Job Search & Interview Pipeline</div>
  <div class="section-body">
    <table>
      <thead>
        <tr>
          <th>Fit</th>
          <th>Role / Opportunity</th>
          <th>Source</th>
          <th>Status / Notes</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="fit-high">HIGH</span></td>
          <td><strong>Chief Human Resources Officer</strong><br>Edged</td>
          <td>LinkedIn Job Alert</td>
          <td>Posted 7/28 — fresh listing. CHRO-level role directly matching your experience.</td>
          <td>Apply immediately</td>
        </tr>
        <tr>
          <td><span class="fit-high">HIGH</span></td>
          <td><strong>Sr. Human Resources Director</strong><br>Confidential — up to $350K/yr</td>
          <td>LinkedIn Job Alert</td>
          <td>Posted 7/26 — 3 days old. Compensation is top-tier for the market.</td>
          <td>Apply today</td>
        </tr>
        <tr>
          <td><span class="fit-high">HIGH</span></td>
          <td><strong>Head of Human Resources</strong><br>EWC Growth (Similar Roles)</td>
          <td>LinkedIn Jobs</td>
          <td>LinkedIn surfaced similar roles to this position — review the full list for matches.</td>
          <td>Review & apply to best matches</td>
        </tr>
        <tr>
          <td><span class="fit-medium">MEDIUM</span></td>
          <td><strong>Strategy Sr. Associate</strong><br>Citizens Bank</td>
          <td>Citizens Careers Email</td>
          <td>Flagged as matching your interests. Strategy role — may be lateral or below target level.</td>
          <td>Review posting for fit; apply if aligned</td>
        </tr>
        <tr>
          <td><span class="fit-medium">MEDIUM</span></td>
          <td><strong>Med Director, Provider Performance & Clinical Transformation</strong><br>Horizon BCBSNJ — Hopewell, NJ</td>
          <td>PostJobFree alert (Dennis Gorelik)</td>
          <td>Medical Director designing clinical programs. Hopewell, NJ location may require commute. In Trash — verify if relevant to your background.</td>
          <td>Rescue from Trash if interested; review role</td>
        </tr>
        <tr>
          <td><span class="fit-low">LOW</span></td>
          <td><strong>Application Viewed by Super Hire Staff</strong></td>
          <td>LinkedIn</td>
          <td>A previous application was viewed — no interview request yet. Monitor for follow-up.</td>
          <td>No action needed; monitor inbox</td>
        </tr>
        <tr>
          <td colspan="5" style="background:#eafaf1; font-style:italic; color:#1e8449; font-weight:600;">
            📅 Networking Event Today: HR Networking & Job Search Group Zoom — 12:00 PM (RSVP pending — act now)
          </td>
        </tr>
        <tr>
          <td colspan="5" style="background:#eafaf1; font-style:italic; color:#1e8449; font-weight:600;">
            📅 Networking Event Tomorrow: HR Networking Open Office Hours — Thu Jul 30, 12:00 PM (RSVP pending)
          </td>
        </tr>
      </tbody>
    </table>

    <div style="margin-top:16px;">
      <div class="card card-green">
        <div class="card-title">🤖 Today's Webinar: How A VP Talent Builds with AI</div>
        <div class="card-meta">PromptMates Live | 11:00 AM – 12:00 PM | Luma</div>
        <div class="card-body">Free webinar for HR and Recruitment professionals on AI tools and automation. Emily Gransky, VP Talent, is presenting. Highly relevant for positioning yourself as an AI-fluent HR executive. You've accepted — be ready to join at 11 AM sharp.</div>
      </div>
    </div>

    <div style="margin-top:12px;">
      <div class="card card-purple">
        <div class="card-title">📰 Career Development Resources (From Trash)</div>
        <div class="card-meta">Lisa Rangel, Chameleon Resumes | "Why recruiters chase some executives" — In Trash</div>
        <div class="card-body">Free live training at noon ET on executive visibility and being pursued vs. pursuing. This was trashed but may be worth rescuing if relevant to your current search strategy. Note: Lisa Rangel is a legitimate executive resume coach.</div>
        <div class="card-action">→ Optionally rescue from Trash and register if the noon ET timing works.</div>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     6. FULL EMAIL REVIEW BY CATEGORY
════════════════════════════════════════════════════ -->
<div class="section red">
  <div class="section-title">🔐 Category: Security / Risk</div>
  <div class="section-body">
    <p><strong>Count: 6 emails</strong> | 2 auto-trashed phishing, 4 spam/scam (health scam, adult spam, prize scam, cloud account lock)</p>
    <hr class="divider">

    <div class="card card-red">
      <div class="card-title">🚨 AUTO-TRASHED — Phishing: Fake Cloud Storage Lock</div>
      <div class="card-meta">From: "❌melissaw212❌" &lt;qcos704sfx@ibm0fmi76u.us&gt; | Jul 29</div>
      <div class="card-body">Subject: "🚫We have blocked your account! On Wed,29 Jul-2026 your pictures and videos will be deleted." Spoofed sender using your username (melissaw212) with random domain. Urgency-based credential harvesting. <strong>Auto-trashed before delivery.</strong></div>
      <div class="card-action">✅ No action needed — already removed. Do not interact.</div>
    </div>

    <div class="card card-red">
      <div class="card-title">🚨 AUTO-TRASHED — Phishing: Fake Payment Declined / Cloud Lock</div>
      <div class="card-meta">From: "'𝗣aym𝗲nt_Declin𝗲d©'" &lt;random domain&gt; | Jul 28</div>
      <div class="card-body">Subject: "melissaw212, Your Cloud ID has been locked on Tue, 28 Jul 2026." Spoofed payment declined sender using your username, threatening photo/video deletion. Random domain, credential/payment harvesting tactic. <strong>Auto-trashed before delivery.</strong></div>
      <div class="card-action">✅ No action needed — already removed. Do not interact.</div>
    </div>

    <div class="card card-red">
      <div class="card-title">⚠️ SCAM: Fake Prize Winner</div>
      <div class="card-meta">From: "TractorSupply®" &lt;v7xqfbh64t@misotlc5cb.us&gt; | Jul 29 | In Trash</div>
      <div class="card-body">Subject: "Confirmed: You have won a Predator 3500 Watt Inverter Generator." Spoofed Tractor Supply sender, random domain. Classic prize scam. Claims "Google © (Not scam)" in body — red flag.</div>
      <div class="card-action">→ Already in Trash. Delete permanently. Do not click any links.</div>
    </div>

    <div class="card card-red">
      <div class="card-title">⚠️ SPAM: Unsolicited Health Scam (Lung)</div>
      <div class="card-meta">From: Healthy_Lungs &lt;random domain&gt; | Jul 28 | Not in inbox</div>
      <div class="card-body">Subject: "A Simpler Path Toward Comfort." Promotes fake COPD reversal protocol. Random sender domain — unsolicited spam.</div>
      <div class="card-action">→ Delete. Do not click. Mark as spam.</div>
    </div>

    <div class="card card-red">
      <div class="card-title">⚠️ SPAM: Unsolicited Health Scam (Lung Clearing)</div>
      <div class="card-meta">From: Lung_Clearing_Method &lt;random domain&gt; | Jul 28 | Not in inbox</div>
      <div class="card-body">Subject: "Can't Catch Your Breath? Mucus Might Be the Reason." Fake "natural Lung Cement clearing protocol." Random domain, unsolicited.</div>
      <div class="card-action">→ Delete. Mark as spam.</div>
    </div>

    <div class="card card-red">
      <div class="card-title">⚠️ SPAM: Unsolicited Health Scam (Blood Sugar)</div>
      <div class="card-meta">From: Blood Sugar Alert &lt;random domain&gt; | Jul 28 | Not in inbox</div>
      <div class="card-body">Subject: "The hidden reason your blood sugar won't stabilize." Addresses you by username (melissaw212), random domain — typical spam list tactic.</div>
      <div class="card-action">→ Delete. Mark as spam.</div>
    </div>

  </div>
</div>

<div class="section green">
  <div class="section-title">💼 Category: Job Search</div>
  <div class="section-body">
    <p><strong>Count: 5 emails</strong> | LinkedIn alerts, Citizens Careers, PostJobFree — see Job Search Pipeline section for full details.</p>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>LinkedIn Job Alerts</td><td>Chief Human Resources Officer at Edged</td><td><span class="badge badge-green">Inbox</span></td><td>Apply now</td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>Sr Human Resources Director — up to $350K/yr</td><td><span class="badge badge-gray">Not inbox</span></td><td>Apply today</td></tr>
        <tr><td>LinkedIn</td><td>New jobs similar to Head of HR at EWC Growth</td><td><span class="badge badge-green">Inbox</span></td><td>Review list</td></tr>
        <tr><td>Citizens Careers</td><td>New jobs for you! (Strategy Sr Associate)</td><td><span class="badge badge-green">Inbox</span></td><td>Review for fit</td></tr>
        <tr><td>Dennis Gorelik / PostJobFree</td><td>Horizon BCBSNJ — Med Dir., Prov Perf & Clin Transf (Hopewell, NJ)</td><td><span class="badge badge-gray">Trash</span></td><td>Rescue if relevant</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="section green">
  <div class="section-title">🤝 Category: Recruiters / Networking</div>
  <div class="section-body">
    <p><strong>Count: 1 email</strong></p>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Notes</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>LinkedIn</td>
          <td>Your application was viewed by Super Hire Staff</td>
          <td>Application viewed — not yet contacted for interview. Positive signal.</td>
          <td>Monitor; consider a follow-up message to the recruiter</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<div class="section blue">
  <div class="section-title">📅 Category: Calendar / Events</div>
  <div class="section-body">
    <p><strong>Count: 2 emails</strong> | Professional webinars and HR events</p>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Notes</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>Zoho Community (dhivya.ashok@zohocorp.com)</td>
          <td>Two Upcoming Zoho Virtual Meetups for Modern Support Teams</td>
          <td>Zoho community webinars for support teams. Not directly HR-focused but relevant for HR tech. Not in inbox.</td>
          <td>Review dates; register if relevant to current work</td>
        </tr>
        <tr>
          <td>Fireflies.ai (fred@fireflies.ai)</td>
          <td>Share the meeting highlights!</td>
          <td>In Trash. Fireflies AI notetaking feature promotion — highlights sharing tool. Note: the HR Networking group EXPLICITLY bans AI notetaking tools on their calls.</td>
          <td>Delete — in Trash already; do NOT use Fireflies on HR Networking calls</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<div class="section yellow">
  <div class="section-title">🏥 Category: Medical / Health</div>
  <div class="section-body">
    <p><strong>Count: 1 legitimate email + 3 spam (counted in Security)</strong></p>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Notes</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>Google Calendar</td>
          <td>Email Dr. Hollander (Calendar Task)</td>
          <td>Personal calendar task at 11 AM. No email received FROM Dr. Hollander — this is a self-reminder.</td>
          <td>Send email to Dr. Hollander today before noon</td>
        </tr>
      </tbody>
    </table>
    <p class="note">Note: Three health-related spam emails (Healthy_Lungs, Lung_Clearing_Method, Blood Sugar Alert) are counted in Security / Risk — not repeated here.</p>
    <div class="card card-blue" style="margin-top:12px;">
      <div class="card-title">👁️ Eye Doctor — Saturday, August 1</div>
      <div class="card-meta">2:30 PM – 3:30 PM | Calendar Event</div>
      <div class="card-body">Appointment confirmed for Saturday. Confirm address and arrange transport. Vision may be temporarily affected post-appointment.</div>
    </div>
    <div class="card card-blue" style="margin-top:8px;">
      <div class="card-title">🦵 Physical Therapy (PT) — Tuesday, August 4</div>
      <div class="card-meta">10:00 AM – 11:00 AM | Calendar Event</div>
      <div class="card-body">PT session confirmed for next Tuesday. Confirm location and any pre-session instructions.</div>
    </div>
  </div>
</div>

<div class="section yellow">
  <div class="section-title">💳 Category: Financial / Billing</div>
  <div class="section-body">
    <p><strong>Count: 3 emails</strong> | All from Bank of America — legitimate sender domain confirmed</p>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Amount/Account</th><th>Status</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>Bank of America</td>
          <td>Direct deposit credited</td>
          <td>$80.00 — Acorns Invest Transfer — Acct #7471</td>
          <td>✅ Credit posted July 29</td>
          <td>Informational — no action needed</td>
        </tr>
        <tr>
          <td>Bank of America</td>
          <td>Billing Dispute acct-2994: Claim being reviewed by merchant's bank</td>
          <td>Acct -2994 | Step 2 of 3</td>
          <td>⏳ In review</td>
          <td>Monitor for Step 3 notification</td>
        </tr>
        <tr>
          <td>Bank of America</td>
          <td>Billing Dispute acct-2994: Merchant credit issued</td>
          <td>Acct -2994 | Step 2 of 3</td>
          <td>✅ Credit issued by merchant</td>
          <td>Log in and confirm credit posted to account</td>
        </tr>
      </tbody>
    </table>
    <p class="note">⚠️ Note: Two dispute emails may be sequential updates on the same claim (Steps 2a and 2b). Both indicate Step 2 of 3 — final resolution pending. Watch for Step 3 email.</p>
  </div>
</div>

<div class="section purple">
  <div class="section-title">📚 Category: Professional Development</div>
  <div class="section-body">
    <p><strong>Count: 4 emails</strong></p>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Location</th><th>Recommendation</th></tr></thead>
      <tbody>
        <tr>
          <td>Disruptive HR via LinkedIn</td>
          <td>How to help your leaders be more curious</td>
          <td>In Trash</td>
          <td>Relevant to HR leadership. Rescue from Trash if you want to read it.</td>
        </tr>
        <tr>
          <td>Lisa Rangel / Chameleon Resumes</td>
          <td>Why recruiters chase some executives and ignore others (Free live training)</td>
          <td>In Trash</td>
          <td>Legitimate executive career coach. Training was noon ET today. Rescue and register if still available.</td>
        </tr>
        <tr>
          <td>Alison Courses</td>
          <td>Melissa A, take better care of yourself everyday!</td>
          <td>In Trash</td>
          <td>Hospitality course suggestion — not relevant. Delete.</td>
        </tr>
        <tr>
          <td>Zoho Community</td>
          <td>Two Upcoming Zoho Virtual Meetups for Modern Support Teams</td>
          <td>Not in inbox</td>
          <td>Zoho HR tech webinars — review dates for potential relevance.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<div class="section gray">
  <div class="section-title">💜 Category: Personal</div>
  <div class="section-body">
    <p><strong>Count: 5 emails</strong> | Dating apps, social media, personal services</p>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Notes</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>Match</td>
          <td>Csalny likes you. See if it's mutual.</td>
          <td>Not in inbox</td>
          <td>Review at leisure</td>
        </tr>
        <tr>
          <td>Match</td>
          <td>You've had a profile view from Alex (66, Far Rockaway, NY)</td>
          <td>Not in inbox</td>
          <td>Review at leisure</td>
        </tr>
        <tr>
          <td>Coffee Meets Bagel</td>
          <td>See who's putting in the effort</td>
          <td>Not in inbox</td>
          <td>Review at leisure</td>
        </tr>
        <tr>
          <td>Facebook Pages</td>
          <td>Aspoonfullofsugar77 is a new Page suggestion</td>
          <td>Not in inbox</td>
          <td>Low priority — ignore or delete</td>
        </tr>
        <tr>
          <td>USPS Informed Delivery</td>
          <td>Your Daily Digest for Wed, 7/29 — 1 mailpiece arriving</td>
          <td>In Inbox</td>
          <td>Note: 1 piece of mail arriving today. Check mailbox. 0 packages.</td>
        </tr>
      </tbody>
    </table>
    <div class="card card-purple" style="margin-top:12px;">
      <div class="card-title">🎂 Reminder: Shari's Birthday — Sunday, August 2</div>
      <div class="card-meta">Calendar Event (All Day)</div>
      <div class="card-body">Plan a message, card, or gift now so you're not scrambling over the weekend.</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     7. TRASH REVIEW
════════════════════════════════════════════════════ -->
<div class="section red">
  <div class="section-title">🗑️ Trash Review</div>
  <div class="section-body">

    <div class="group-label" style="color:#c0392b; font-size:15px;">🚨 AUTO-TRASHED — Phishing (2 emails)</div>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Reason</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>"❌melissaw212❌" (spoofed)</td>
          <td>🚫 We have blocked your account! Photos/videos deleted Wed Jul 29</td>
          <td>Spoofed sender, random domain, urgent account-lock threat using your username to harvest credentials</td>
          <td><span class="badge badge-red">Auto-Trashed — No Action Needed</span></td>
        </tr>
        <tr>
          <td>"'𝗣aym𝗲nt_Declin𝗲d©'" (spoofed)</td>
          <td>melissaw212, Your Cloud ID has been locked — photos/videos removed!</td>
          <td>Spoofed payment-declined sender, random domain, urgent lock threat targeting username to harvest credentials/payment info</td>
          <td><span class="badge badge-red">Auto-Trashed — No Action Needed</span></td>
        </tr>
      </tbody>
    </table>

    <hr class="divider">

    <div class="group-label" style="color:#c0392b; font-size:15px;">⚠️ RESTORE IMMEDIATELY (1 email)</div>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Reason to Restore</th></tr></thead>
      <tbody>
        <tr>
          <td>Disruptive HR via LinkedIn</td>
          <td>How to help your leaders be more curious</td>
          <td>Legitimate professional development content from LinkedIn. Relevant to HR leadership role. May have been trashed by over-aggressive filtering.</td>
        </tr>
      </tbody>
    </table>

    <hr class="divider">

    <div class="group-label" style="color:#e67e22; font-size:15px;">🔍 REVIEW BEFORE DELETING (5 emails)</div>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Notes</th></tr></thead>
      <tbody>
        <tr>
          <td>Lisa Rangel / Chameleon Resumes</td>
          <td>Why recruiters chase some executives and ignore others</td>
          <td>Legitimate executive resume coach. Free training at noon ET. Restore if you want to access recording/replay.</td>
        </tr>
        <tr>
          <td>Dennis Gorelik / PostJobFree</td>
          <td>Horizon BCBSNJ — Med Dir., Prov Perf & Clin Transf</td>
          <td>Could be relevant if pursuing healthcare exec roles. Review if interested in the Hopewell, NJ area.</td>
        </tr>
        <tr>
          <td>Fireflies.ai</td>
          <td>Share the meeting highlights!</td>
          <td>Legitimate AI notetaking tool. Warning: do NOT use on HR Networking Group calls. Review if you use Fireflies elsewhere.</td>
        </tr>
        <tr>
          <td>The AI Report</td>
          <td>⚡ AI leaders call for slowdown (Claude chats exposed via Google search)</td>
          <td>Relevant AI industry news — Claude/Anthropic privacy issue mentioned. Worth reading if you follow AI trends.</td>
        </tr>
        <tr>
          <td>TLDR Newsletter</td>
          <td>Apple smart home, Anthropic cracks encryption, orchestrator's tax</td>
          <td>Technology briefing — Anthropic item directly relevant to AI professionals. Consider rescuing if you read TLDR.</td>
        </tr>
      </tbody>
    </table>

    <hr class="divider">

    <div class="group-label" style="color:#1e8449; font-size:15px;">✅ SAFE TO DELETE (19 emails in Trash)</div>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Reason</th></tr></thead>
      <tbody>
        <tr><td>"TractorSupply®" (spoofed)</td><td>Confirmed: You have won a Predator 3500W Generator</td><td>Scam/prize fraud — random domain spoofing Tractor Supply</td></tr>
        <tr
