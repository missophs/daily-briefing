<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa W. — Sunday, August 16, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 15px; color: #a0b4d0; margin-top: 6px; }
  .header .meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 18px; }
  .header .meta-item .label { font-size: 11px; color: #7a9abf; text-transform: uppercase; letter-spacing: 1px; }
  .header .meta-item .value { font-size: 18px; font-weight: 700; color: #fff; margin-top: 2px; }

  /* SECTION HEADERS */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; padding: 10px 16px; border-radius: 8px 8px 0 0; margin-bottom: 0; }
  .section-body { background: #fff; border-radius: 0 0 10px 10px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }

  /* COLOR THEMES */
  .red .section-title    { background: #c0392b; color: #fff; }
  .yellow .section-title { background: #e67e22; color: #fff; }
  .blue .section-title   { background: #2980b9; color: #fff; }
  .green .section-title  { background: #27ae60; color: #fff; }
  .purple .section-title { background: #8e44ad; color: #fff; }
  .gray .section-title   { background: #7f8c8d; color: #fff; }
  .navy .section-title   { background: #1a1a2e; color: #fff; }
  .teal .section-title   { background: #16a085; color: #fff; }
  .orange .section-title { background: #d35400; color: #fff; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #f4f6f8; color: #555; text-transform: uppercase; font-size: 11px; letter-spacing: 0.8px; padding: 9px 12px; text-align: left; border-bottom: 2px solid #e0e4ea; }
  td { padding: 9px 12px; border-bottom: 1px solid #f0f2f5; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #fafbfc; }

  /* CARDS */
  .card { border-radius: 8px; padding: 14px 16px; margin-bottom: 12px; border-left: 4px solid; }
  .card-red    { background: #fdf2f2; border-color: #c0392b; }
  .card-yellow { background: #fef9ec; border-color: #e67e22; }
  .card-blue   { background: #eaf4fb; border-color: #2980b9; }
  .card-green  { background: #eafaf1; border-color: #27ae60; }
  .card-purple { background: #f5eef8; border-color: #8e44ad; }
  .card-gray   { background: #f8f9fa; border-color: #95a5a6; }
  .card-teal   { background: #e8f8f5; border-color: #16a085; }
  .card-orange { background: #fef0e6; border-color: #d35400; }

  .card .card-title { font-weight: 700; font-size: 14px; margin-bottom: 4px; }
  .card .card-source { font-size: 11px; color: #888; margin-bottom: 6px; }
  .card .card-row { font-size: 13px; margin-bottom: 3px; }
  .card .card-row span { font-weight: 600; }

  /* BADGES */
  .badge { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 11px; font-weight: 700; margin-left: 6px; }
  .badge-red    { background: #fadbd8; color: #922b21; }
  .badge-green  { background: #d5f5e3; color: #1e8449; }
  .badge-yellow { background: #fdebd0; color: #935116; }
  .badge-blue   { background: #d6eaf8; color: #1a5276; }
  .badge-purple { background: #e8daef; color: #6c3483; }
  .badge-gray   { background: #ecf0f1; color: #555; }
  .badge-orange { background: #fde8d8; color: #7e5109; }

  /* PRIORITY */
  .priority-high   { color: #c0392b; font-weight: 700; }
  .priority-med    { color: #e67e22; font-weight: 700; }
  .priority-low    { color: #27ae60; font-weight: 700; }

  /* STATUS ICONS */
  .status-confirmed { color: #27ae60; }
  .status-declined  { color: #c0392b; }
  .status-pending   { color: #e67e22; }

  /* EXEC SUMMARY */
  .exec-bullets { list-style: none; padding: 0; }
  .exec-bullets li { padding: 12px 16px; border-radius: 8px; margin-bottom: 10px; font-size: 14px; line-height: 1.5; }
  .exec-bullets li.risk    { background: #fdf2f2; border-left: 4px solid #c0392b; }
  .exec-bullets li.opp     { background: #eafaf1; border-left: 4px solid #27ae60; }
  .exec-bullets li.cal     { background: #eaf4fb; border-left: 4px solid #2980b9; }

  /* DASHBOARD GRID */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }
  .dash-tile { background: #fff; border-radius: 10px; padding: 16px 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); border-top: 4px solid; }
  .dash-tile .tile-label { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #888; margin-bottom: 6px; }
  .dash-tile .tile-value { font-size: 26px; font-weight: 800; }
  .dash-tile .tile-sub   { font-size: 12px; color: #666; margin-top: 4px; }
  .dt-red    { border-color: #c0392b; } .dt-red .tile-value    { color: #c0392b; }
  .dt-green  { border-color: #27ae60; } .dt-green .tile-value  { color: #27ae60; }
  .dt-blue   { border-color: #2980b9; } .dt-blue .tile-value   { color: #2980b9; }
  .dt-yellow { border-color: #e67e22; } .dt-yellow .tile-value { color: #e67e22; }
  .dt-purple { border-color: #8e44ad; } .dt-purple .tile-value { color: #8e44ad; }
  .dt-gray   { border-color: #7f8c8d; } .dt-gray .tile-value   { color: #7f8c8d; }

  /* TRIAGE TABLE STATUS CELLS */
  .s-rescued  { background: #d5f5e3; color: #1a5632; font-weight: 700; border-radius: 6px; padding: 2px 6px; white-space: nowrap; }
  .s-inbox    { background: #d6eaf8; color: #1a5276; font-weight: 700; border-radius: 6px; padding: 2px 6px; white-space: nowrap; }
  .s-autotrash{ background: #fadbd8; color: #922b21; font-weight: 700; border-radius: 6px; padding: 2px 6px; white-space: nowrap; }
  .s-trash    { background: #f2f3f4; color: #555; font-weight: 700; border-radius: 6px; padding: 2px 6px; white-space: nowrap; }

  .divider { border: none; border-top: 2px solid #e8eaed; margin: 10px 0 18px; }

  .pill { display: inline-block; padding: 3px 10px; border-radius: 12px; font-size: 11px; font-weight: 700; }
  .pill-high   { background: #fadbd8; color: #c0392b; }
  .pill-medium { background: #fdebd0; color: #935116; }
  .pill-low    { background: #d5f5e3; color: #1e8449; }

  .warning-box { background: #fdf2f2; border: 1px solid #f5b7b1; border-radius: 8px; padding: 12px 16px; margin-top: 10px; }
  .info-box    { background: #eaf4fb; border: 1px solid #a9cce3; border-radius: 8px; padding: 12px 16px; margin-top: 10px; }
  .success-box { background: #eafaf1; border: 1px solid #a9dfba; border-radius: 8px; padding: 12px 16px; margin-top: 10px; }

  .group-header { background: #f4f6f8; padding: 8px 12px; border-radius: 6px; font-weight: 700; font-size: 13px; margin: 12px 0 6px; color: #333; }

  .small-note { font-size: 11px; color: #888; font-style: italic; }

  .rescued-badge { display: inline-block; background: #d5f5e3; color: #1a5632; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: 700; margin-left: 8px; }
  .auto-trash-badge { display: inline-block; background: #fadbd8; color: #922b21; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: 700; margin-left: 8px; }

  ul.plain { list-style: none; padding-left: 0; }
  ul.plain li { padding: 4px 0; border-bottom: 1px solid #f0f2f5; }
  ul.plain li:last-child { border-bottom: none; }

  @media (max-width: 700px) {
    .header h1 { font-size: 20px; }
    .dash-grid { grid-template-columns: 1fr 1fr; }
  }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════
     SECTION 0 — EMAIL TRIAGE QUICK LIST
═══════════════════════════════════════════════════ -->
<div class="section navy">
  <div class="section-title">📋 Email Triage Quick List</div>
  <div class="section-body" style="padding:0;">
    <table>
      <thead>
        <tr>
          <th style="width:130px;">Status</th>
          <th style="width:220px;">From</th>
          <th>Subject</th>
          <th>Summary</th>
        </tr>
      </thead>
      <tbody>
        <!-- RESCUED -->
        <tr style="background:#f0fdf4;">
          <td><span class="s-rescued">✅ RESCUED</span></td>
          <td>Nextdoor — Yorkville</td>
          <td>Good afternoon.</td>
          <td>Neighborhood safety alert: delivery scam on Melissa's street using her address. Rescued from Trash — local safety notice.</td>
        </tr>
        <!-- INBOX EMAILS (individual rows) -->
        <tr>
          <td><span class="s-inbox">📥 INBOX</span></td>
          <td>Nader / Building Leverage</td>
          <td>We built a billionaire's personal brand…</td>
          <td>LinkedIn personal brand playbook — Richard Harpin case study. Professional development newsletter.</td>
        </tr>
        <tr>
          <td><span class="s-inbox">📥 INBOX</span></td>
          <td>Match</td>
          <td>You've had a profile view from Kevin</td>
          <td>Kevin, 58, Jamesburg NJ viewed your Match profile.</td>
        </tr>
        <tr>
          <td><span class="s-inbox">📥 INBOX</span></td>
          <td>LinkedIn Job Alerts</td>
          <td>Human Resources Director at Iceberg: up to $210K/year</td>
          <td>HR Director role, actively recruiting. High fit alert. (Duplicate alerts also in inbox.)</td>
        </tr>
        <tr>
          <td><span class="s-inbox">📥 INBOX</span></td>
          <td>LinkedIn Job Alerts</td>
          <td>Chief People Officer at Kinora Group</td>
          <td>CPO role alert from LinkedIn. High-priority opportunity.</td>
        </tr>
        <tr>
          <td><span class="s-inbox">📥 INBOX</span></td>
          <td>Apple</td>
          <td>Your receipt from Apple.</td>
          <td>Purchase receipt: "A Bar Song (Irish Folk)" and other items. Legitimate Apple receipt — verify charge.</td>
        </tr>
        <tr>
          <td><span class="s-inbox">📥 INBOX</span></td>
          <td>Ruben Hassid / Substack</td>
          <td>Cowork.</td>
          <td>Instructions for setting up Claude Cowork. AI/productivity newsletter.</td>
        </tr>
        <tr>
          <td><span class="s-inbox">📥 INBOX</span></td>
          <td>Ruben Hassid / Substack</td>
          <td>Cowork (August 2026).</td>
          <td>August edition of Claude Cowork setup guide. Appears to be a duplicate of above.</td>
        </tr>
        <tr>
          <td><span class="s-inbox">📥 INBOX</span></td>
          <td>LinkedIn Job Alerts</td>
          <td>Human Resources Director at Iceberg: up to $210K/year (2nd alert)</td>
          <td>Second LinkedIn alert for same Iceberg HR Director role.</td>
        </tr>
        <tr>
          <td><span class="s-inbox">📥 INBOX</span></td>
          <td>LinkedIn Job Alerts</td>
          <td>Chief People Officer at Kinora Group (2nd alert)</td>
          <td>Second LinkedIn alert for same Kinora Group CPO role.</td>
        </tr>
        <tr>
          <td><span class="s-inbox">📥 INBOX</span></td>
          <td>LinkedIn Job Alerts</td>
          <td>VP of People at Orbital</td>
          <td>VP of People role at Orbital. New opportunity to review.</td>
        </tr>
        <tr>
          <td><span class="s-inbox">📥 INBOX</span></td>
          <td>LinkedIn Job Alerts</td>
          <td>Human Resources Director at Iceberg: up to $210K/year (3rd alert)</td>
          <td>Third alert for Iceberg HR Director — LinkedIn sending duplicates. Same role.</td>
        </tr>
        <tr>
          <td><span class="s-inbox">📥 INBOX</span></td>
          <td>Melissa W (self-sent)</td>
          <td>How To Remove The New Claude Watermarks | Maverick AI</td>
          <td>Self-sent link to mavgpt.ai resource. Likely a saved reference. Review URL before clicking.</td>
        </tr>
        <!-- AUTO-TRASHED SUMMARY ROW -->
        <tr style="background:#fff5f5;">
          <td><span class="s-autotrash">🗑 AUTO-TRASHED</span></td>
          <td colspan="2"><strong>7 emails auto-trashed (phishing / spam)</strong> — see Trash Review</td>
          <td>Includes 3 credential-harvesting phishing emails (iCloud spoofs), 3 explicit spam, 1 online casino spam.</td>
        </tr>
        <!-- MANUAL TRASH SUMMARY ROW -->
        <tr style="background:#f8f9fa;">
          <td><span class="s-trash">🗂 MANUAL TRASH</span></td>
          <td colspan="2"><strong>30 emails in Trash</strong> — see Trash Review</td>
          <td>Mix of newsletters, retail promos, job alerts, dating app notices, and low-value digests.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 1 — HEADER
═══════════════════════════════════════════════════ -->
<div class="header">
  <div class="subtitle">EXECUTIVE BRIEFING</div>
  <h1>Good Morning, Melissa 👋</h1>
  <div class="subtitle">Prepared by your Executive Chief of Staff</div>
  <div class="meta">
    <div class="meta-item">
      <div class="label">Date</div>
      <div class="value">Sunday, August 16, 2026</div>
    </div>
    <div class="meta-item">
      <div class="label">Total Emails Reviewed</div>
      <div class="value">50</div>
    </div>
    <div class="meta-item">
      <div class="label">Calendar Events</div>
      <div class="value">7</div>
    </div>
    <div class="meta-item">
      <div class="label">Action Items</div>
      <div class="value">8</div>
    </div>
    <div class="meta-item">
      <div class="label">Security Alerts</div>
      <div class="value" style="color:#ff6b6b;">3 Phishing</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 2 — EXECUTIVE SUMMARY
═══════════════════════════════════════════════════ -->
<div class="section navy">
  <div class="section-title">⚡ Executive Summary</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li class="risk">
        🔴 <strong>Security Risk:</strong> Three confirmed credential-harvesting phishing emails (iCloud/Cloud spoofs with fake payment-declined / account-lock threats) were automatically intercepted and trashed before reaching your inbox. Your username <em>melissaw212</em> is being actively targeted. Do <strong>not</strong> click any links in emails about iCloud payment issues — go directly to <a href="https://appleid.apple.com" target="_blank">appleid.apple.com</a> if you need to verify your account. Additionally, a <strong>neighborhood delivery scam</strong> was flagged on your Yorkville block (rescued from Trash — worth reading).
      </li>
      <li class="opp">
        🟢 <strong>Job Search Opportunity:</strong> Multiple high-fit senior HR leadership roles are actively surfacing: <strong>HR Director at Iceberg (up to $210K/yr)</strong>, <strong>CPO at Kinora Group</strong>, <strong>VP of People at Orbital</strong>, and a <strong>Director of HR at Roads to Success (Manhattan)</strong> via Indeed/PostJobFree. Your LinkedIn profile appeared in <strong>5 searches this week</strong>. Your HR Networking Group meets Tuesday and Wednesday — prime opportunities to advance your pipeline.
      </li>
      <li class="cal">
        🔵 <strong>Calendar Priority:</strong> You have <strong>Stella's vet appointment Tuesday Aug 18 (10–11am)</strong> — no RSVP issues there. Your <strong>HR Networking &amp; Job Search Group Zoom</strong> is Tuesday Aug 19 12–1:30pm (RSVP pending — action needed). You have a <strong>1:1 with Monte Montoya (M&amp;m)</strong> Tuesday at 2pm. The <strong>Executive Roundtable with John Madigan</strong> on Thursday Aug 20 is currently showing as <em>Declined</em> — confirm this is intentional.
      </li>
    </ul>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 3 — ACTION REQUIRED
═══════════════════════════════════════════════════ -->
<div class="section yellow">
  <div class="section-title">⚠️ Action Required</div>
  <div class="section-body">

    <div class="card card-red">
      <div class="card-title">🔴 Do NOT click — Phishing Targeting Your Account <span class="badge badge-red">SECURITY</span></div>
      <div class="card-source">Source: 3 auto-trashed phishing emails (iCloud/Cloud spoofs)</div>
      <div class="card-row"><span>Why it matters:</span> Your username <em>melissaw212</em> is being harvested and used in spoofed sender addresses. Three separate phishing attempts mimicked iCloud/Apple payment failures and threatened photo/video deletion to force credential entry.</div>
      <div class="card-row"><span>Recommended action:</span> If you have any concern about your iCloud account, go directly to appleid.apple.com — never via email link. Consider enabling advanced phishing filters or two-factor authentication review. These emails have already been removed.</div>
      <div class="card-row"><span>Due:</span> Today</div>
    </div>

    <div class="card card-yellow">
      <div class="card-title">🟡 RSVP Needed — HR Networking &amp; Job Search Group Zoom <span class="badge badge-yellow">RSVP</span></div>
      <div class="card-source">Source: Google Calendar — Tue Aug 19, 12:00–1:30pm</div>
      <div class="card-row"><span>Why it matters:</span> Status shows <em>needsAction</em> (no RSVP). This is your primary HR peer networking group with 150+ attendees. Missing it without a response is a missed professional touchpoint.</div>
      <div class="card-row"><span>Recommended action:</span> Accept the invite. Zoom link: <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Join Zoom</a></div>
      <div class="card-row"><span>Due:</span> Before Tuesday Aug 19</div>
    </div>

    <div class="card card-yellow">
      <div class="card-title">🟡 RSVP Needed — HR Networking Open Office Hours Zoom <span class="badge badge-yellow">RSVP</span></div>
      <div class="card-source">Source: Google Calendar — Wed Aug 20, 12:00–1:00pm</div>
      <div class="card-row"><span>Why it matters:</span> Status shows <em>needsAction</em>. A second HR networking session — open office hours format. Great for 1:1 connections during job search.</div>
      <div class="card-row"><span>Recommended action:</span> Accept or decline. Zoom link: <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Join Zoom</a></div>
      <div class="card-row"><span>Due:</span> Before Wednesday Aug 20</div>
    </div>

    <div class="card card-red">
      <div class="card-title">🔴 Confirm or Reconsider — Executive Roundtable (Currently DECLINED) <span class="badge badge-red">CALENDAR</span></div>
      <div class="card-source">Source: Google Calendar — Thu Aug 20, 9:00–10:30am (John Madigan)</div>
      <div class="card-row"><span>Why it matters:</span> You have declined this Executive Roundtable. If this is a senior-level networking opportunity during an active job search, declining may be worth reconsidering. Verify this was intentional.</div>
      <div class="card-row"><span>Recommended action:</span> Confirm the decline was deliberate. If not, reverse your RSVP promptly. Zoom: <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Join Zoom</a></div>
      <div class="card-row"><span>Due:</span> Today (before Thu)</div>
    </div>

    <div class="card card-green">
      <div class="card-title">🟢 Review &amp; Apply — HR Director at Iceberg (up to $210K/yr) <span class="badge badge-green">JOB LEAD</span></div>
      <div class="card-source">Source: LinkedIn Job Alerts (3 separate alert emails)</div>
      <div class="card-row"><span>Why it matters:</span> LinkedIn sent three separate alerts for this role — marked "Actively Recruiting." Strong salary range for an HR Director position. High urgency given repeated alerts.</div>
      <div class="card-row"><span>Recommended action:</span> Open LinkedIn, review the Iceberg posting, and apply or save immediately.</div>
      <div class="card-row"><span>Due:</span> This week</div>
    </div>

    <div class="card card-green">
      <div class="card-title">🟢 Review &amp; Apply — CPO at Kinora Group &amp; VP of People at Orbital <span class="badge badge-green">JOB LEAD</span></div>
      <div class="card-source">Source: LinkedIn Job Alerts</div>
      <div class="card-row"><span>Why it matters:</span> Two senior-level leadership roles (CPO and VP of People) surfaced this morning. Both align with your HR executive background.</div>
      <div class="card-row"><span>Recommended action:</span> Review both postings on LinkedIn this weekend; prepare tailored materials before the Tuesday networking session.</div>
      <div class="card-row"><span>Due:</span> This week</div>
    </div>

    <div class="card card-yellow">
      <div class="card-title">🟡 Verify Apple Purchase Receipt <span class="badge badge-yellow">BILLING</span></div>
      <div class="card-source">Source: Apple &lt;no_reply@email.apple.com&gt; — Sun Aug 16</div>
      <div class="card-row"><span>Why it matters:</span> Legitimate Apple receipt for "A Bar Song (Irish Folk)" and other items. Confirm you recognize all charges.</div>
      <div class="card-row"><span>Recommended action:</span> Check your Apple ID purchase history at appleid.apple.com to confirm all items are recognized.</div>
      <div class="card-row"><span>Due:</span> Today</div>
    </div>

    <div class="card card-teal">
      <div class="card-title">🔔 Read — Neighborhood Delivery Scam Alert (Your Street) <span class="rescued-badge">✅ RESCUED FROM TRASH</span></div>
      <div class="card-source">Source: Nextdoor — Yorkville (E83st-2ndAve) Safety Posts — Sun Aug 16</div>
      <div class="card-row"><span>Why it matters:</span> A neighbor reports someone from Guttenberg is using your address and a neighbor's address in a delivery scam. This directly affects your building/street.</div>
      <div class="card-row"><span>Recommended action:</span> Read the full Nextdoor post. If packages arrive that you didn't order, do not open them — report to USPS or local police. Alert building management if applicable.</div>
      <div class="card-row"><span>Due:</span> Today</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 4 — FULL 7-DAY CALENDAR
═══════════════════════════════════════════════════ -->
<div class="section blue">
  <div class="section-title">📅 Full 7-Day Calendar (Aug 16–22, 2026)</div>
  <div class="section-body">

    <div class="group-header">Sunday, August 16, 2026 — TODAY</div>
    <div class="card card-blue">
      <div class="card-row" style="color:#888; font-style:italic;">No calendar events scheduled today. Use this day for job search prep, reviewing alerts, and RSVPing to this week's events.</div>
    </div>

    <div class="group-header">Monday, August 17, 2026</div>
    <div class="card card-blue">
      <div class="card-row" style="color:#888; font-style:italic;">No calendar events scheduled. Good prep day for Tuesday's vet and networking sessions.</div>
    </div>

    <div class="group-header">Tuesday, August 18, 2026</div>
    <table>
      <thead>
        <tr><th>Time</th><th>Event</th><th>RSVP</th><th>Location</th><th>Prep Needed</th><th>Notes</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>10:00–11:00am</td>
          <td><strong>Vet</strong> (also listed as "Stella vet")</td>
          <td><span class="status-confirmed">✅ Confirmed</span></td>
          <td>TBD (no location listed)</td>
          <td>Confirm vet address; prepare carrier/leash; bring records if new visit</td>
          <td><span class="badge badge-yellow">DUPLICATE EVENT</span> Both "Vet" and "Stella vet" are at the same time — same appointment, two calendar entries. No conflict, just redundant.</td>
        </tr>
      </tbody>
    </table>

    <div class="group-header">Wednesday, August 19, 2026</div>
    <table>
      <thead>
        <tr><th>Time</th><th>Event</th><th>RSVP</th><th>Location</th><th>Prep Needed</th><th>Notes</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>12:00–1:30pm</td>
          <td><strong>HR Networking &amp; Job Search Group — Zoom #2</strong></td>
          <td><span class="status-pending">⏳ RSVP Needed</span></td>
          <td><a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a></td>
          <td>Review team guidelines; prepare 30-sec intro update; review new job leads to share</td>
          <td><span class="badge badge-yellow">ACTION NEEDED</span> 150+ attendees; also listed as "Network" on same timeslot — same event, two entries.</td>
        </tr>
        <tr>
          <td>12:00–1:30pm</td>
          <td><strong>Network</strong> (duplicate of above)</td>
          <td><span class="status-confirmed">✅ Confirmed</span></td>
          <td>No location listed</td>
          <td>—</td>
          <td><span class="badge badge-yellow">DUPLICATE</span> Same time as HR Networking Zoom. Appears to be a personal reminder entry.</td>
        </tr>
        <tr>
          <td>2:00–3:00pm</td>
          <td><strong>M&amp;m</strong> (1:1 with Monte Montoya)</td>
          <td><span class="status-confirmed">✅ Accepted</span></td>
          <td>No location listed</td>
          <td>Prepare agenda for Monte meeting; confirm if in-person or virtual; bring job search update</td>
          <td>monte.montoya@gmail.com is the sole attendee. Likely a personal 1:1 or mentor/peer check-in. Back-to-back with Networking — allow buffer time.</td>
        </tr>
      </tbody>
    </table>
    <div class="warning-box">⚠️ <strong>Conflict Note:</strong> The "Network" entry and "HR Networking &amp; Job Search Group — Zoom #2" overlap completely (both 12–1:30pm Wed). These appear to be the same event entered twice. No true conflict. However, the M&amp;m meeting at 2pm starts only 30 minutes after the networking call ends — plan to exit the Zoom on time.</div>

    <div class="group-header">Thursday, August 20, 2026</div>
    <table>
      <thead>
        <tr><th>Time</th><th>Event</th><th>RSVP</th><th>Location</th><th>Prep Needed</th><th>Notes</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>9:00–10:30am</td>
          <td><strong>Executive Roundtable</strong> (John Madigan)</td>
          <td><span class="status-declined">❌ Declined</span></td>
          <td><a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a></td>
          <td>If reconsidering: prepare exec-level intro and talking points</td>
          <td><span class="badge badge-red">DECLINED — VERIFY INTENT</span> Consider un-declining if this is a valuable executive networking event during active job search.</td>
        </tr>
        <tr>
          <td>12:00–1:00pm</td>
          <td><strong>HR Networking &amp; Job Search: Open Office Hours — Zoom #2</strong></td>
          <td><span class="status-pending">⏳ RSVP Needed</span></td>
          <td><a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a></td>
          <td>No AI notetaking per organizer request; informal discussion format</td>
          <td><span class="badge badge-yellow">ACTION NEEDED</span> No recording permitted. Great for 1:1 relationship building with HR peers.</td>
        </tr>
      </tbody>
    </table>

    <div class="group-header">Friday, August 21 — Saturday, August 22, 2026</div>
    <div class="card card-blue">
      <div class="card-row" style="color:#888; font-style:italic;">No calendar events scheduled for Friday or Saturday.</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 5 — JOB SEARCH & INTERVIEW PIPELINE
═══════════════════════════════════════════════════ -->
<div class="section green">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">

    <div class="group-header">🏆 Active Job Leads</div>
    <table>
      <thead>
        <tr><th>Role</th><th>Company</th><th>Salary</th><th>Source</th><th>Fit</th><th>Status</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Human Resources Director</strong></td>
          <td>Iceberg</td>
          <td>Up to $210K/yr</td>
          <td>LinkedIn Job Alerts (3 alerts)</td>
          <td><span class="pill pill-high">HIGH</span></td>
          <td>Actively Recruiting</td>
          <td>Review &amp; apply immediately</td>
        </tr>
        <tr>
          <td><strong>Chief People Officer</strong></td>
          <td>Kinora Group</td>
          <td>Not listed</td>
          <td>LinkedIn Job Alerts (2 alerts)</td>
          <td><span class="pill pill-high">HIGH</span></td>
          <td>New alert</td>
          <td>Review &amp; apply this week</td>
        </tr>
        <tr>
          <td><strong>VP of People</strong></td>
          <td>Orbital</td>
          <td>Not listed</td>
          <td>LinkedIn Job Alerts</td>
          <td><span class="pill pill-high">HIGH</span></td>
          <td>New alert</td>
          <td>Review &amp; apply this week</td>
        </tr>
        <tr>
          <td><strong>Director of Human Resources</strong></td>
          <td>Roads to Success (Manhattan, NY 10261)</td>
          <td>Not listed</td>
          <td>PostJobFree via Dennis Gorelik</td>
          <td><span class="pill pill-high">HIGH</span></td>
          <td>In Trash — worth reviewing</td>
          <td>Rescue from Trash; review role</td>
        </tr>
        <tr>
          <td><strong>Senior Manager, Corporate Programs</strong></td>
          <td>Avalara</td>
          <td>$136,400–$272,500/yr</td>
          <td>Indeed (via Apple Private Relay)</td>
          <td><span class="pill pill-medium">MEDIUM</span></td>
          <td>In non-trashed folder — not inbox</td>
          <td>Review if interested in Corp Programs track</td>
        </tr>
        <tr>
          <td><strong>Chief People Officer</strong> (search match)</td>
          <td>Various (5 roles)</td>
          <td>Not listed</td>
          <td>JobLeads (mailer@jobleads.com) — in Trash</td>
          <td><span class="pill pill-medium">MEDIUM</span></td>
          <td>In Trash</td>
          <td>Consider restoring to review matches</td>
        </tr>
      </tbody>
    </table>

    <div class="group-header">📡 LinkedIn Profile Visibility</div>
    <div class="card card-green">
      <div class="card-row">You appeared in <strong>5 LinkedIn searches this week</strong> (from LinkedIn notifications email). This signals recruiter activity. Ensure your profile is optimized and open-to-work settings are current.</div>
    </div>

    <div class="group-header">🤝 Networking Events This Week</div>
    <table>
      <thead>
        <tr><th>Date</th><th>Event</th><th>Type</th><th>RSVP</th><th>Prep Needed</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Wed Aug 19, 12–1:30pm</td>
          <td>HR Networking &amp; Job Search Group — Zoom</td>
          <td>Group networking</td>
          <td><span class="status-pending">⏳ Pending</span></td>
          <td>Updated intro, new job leads, questions for peers</td>
        </tr>
        <tr>
          <td>Wed Aug 19, 2–3pm</td>
          <td>M&amp;m — Monte Montoya 1:1</td>
          <td>1:1 peer/mentor</td>
          <td><span class="status-confirmed">✅ Accepted</span></td>
          <td>Agenda: job search update, ask for referrals/intros</td>
        </tr>
        <tr>
          <td>Thu Aug 20, 12–1pm</td>
          <td>HR Networking Open Office Hours</td>
          <td>Open networking</td>
          <td><span class="status-pending">⏳ Pending</span></td>
          <td>No AI notetaking; bring 2–3 specific asks</td>
        </tr>
        <tr>
          <td>Thu Aug 20, 9–10:30am</td>
          <td>Executive Roundtable (John Madigan)</td>
          <td>Executive networking</td>
          <td><span class="status-declined">❌ Declined</span></td>
          <td>Reconsider — exec-level visibility opportunity</td>
        </tr>
      </tbody>
    </table>

    <div class="group-header">📊 LinkedIn Content Opportunity</div>
    <div class="card card-purple">
      <div class="card-row">Building Leverage newsletter (Nader) covers Richard Harpin's LinkedIn personal brand strategy. <strong>Consider reviewing</strong> for ideas to boost your own executive presence on LinkedIn — especially relevant during active job search.</div>
      <div class="card-row">David Green's LinkedIn newsletter "How HR can own Workforce Transformation in the AI era" (in Trash) is also relevant to your expertise positioning.</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 6 — FULL EMAIL REVIEW BY CATEGORY
═══════════════════════════════════════════════════ -->
<div class="section navy">
  <div class="section-title">📂 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="group-header" style="background:#fdf2f2; color:#922b21; border-left: 4px solid #c0392b;">🔴 Security / Risk — 6 Emails</div>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Notes</th></tr></thead>
      <tbody>
        <tr style="background:#fdf2f2;">
          <td>Payment_Declined© (spoofed)</td>
          <td>Your Cloud ID has been locked...</td>
          <td><span class="auto-trash-badge">AUTO-TRASHED — Phishing</span></td>
          <td>Credential-harvesting: spoofed sender, fake iCloud lock, photo/video deletion threat targeting melissaw212. Removed automatically.</td>
        </tr>
        <tr style="background:#fdf2f2;">
          <td>melissaw212 (spoofed self-sender)</td>
          <td>We have blocked your account 🚫 Your photos and videos will be deleted...</td>
          <td><span class="auto-trash-badge">AUTO-TRASHED — Phishing</span></td>
          <td>Credential-harvesting: sender spoofs recipient's own username via fake domain, impersonates iCloud. Removed automatically.</td>
        </tr>
        <tr style="background:#fdf2f2;">
          <td>Admin Alert (spoofed)</td>
          <td>Immediate verification required</td>
          <td><span class="auto-trash-badge">AUTO-TRASHED — Phishing</span></td>
          <td>Credential-harvesting: randomized domain, cloud storage subscription payment failure language. Removed automatically.</td>
        </tr>
        <tr style="background:#fdf2f2;">
          <td>melissaw212 (spoofed)</td>
          <td>Bang her all night with this stay hard trick — Watch Now 🔞</td>
          <td>Not in inbox / not auto-trashed</td>
          <td>Explicit sexual spam from malicious spoofed domain. Manually trash and block domain.</td>
        </tr>
        <tr style="background:#fdf2f2;">
          <td>Sex Trick 💋 (spoofed)</td>
          <td>🔞Naughty porn star reveals secret to staying hard for hours</td>
          <td>Not in inbox / not auto-trashed</td>
          <td>Explicit sexual spam. Trash and block.</td>
        </tr>
        <tr style="background:#fdf2f2;">
          <td>Nextdoor — Yorkville E83st</td>
          <td>Good afternoon. [Delivery scam alert]</td>
          <td><span class="rescued-badge">✅ RESCUED FROM TRASH</span></td>
          <td>Neighborhood safety: delivery scam using Melissa's address. Read and act locally.</td>
        </tr>
      </tbody>
    </table>
    <div class="small-note" style="margin-top:6px;">Recommended action: The 3 phishing emails are already removed. Manually trash the 2 explicit spam emails. Read the Nextdoor rescue.</div>

    <hr class="divider">

    <!-- JOB SEARCH -->
    <div class="group-header" style="background:#eafaf1; color:#1a5632; border-left: 4px solid #27ae60;">🟢 Job Search — 9 Emails</div>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Location</th><th>Fit</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>LinkedIn Job Alerts (inbox)</td>
          <td>Human Resources Director at Iceberg: up to $210K/yr</td>
          <td>Actively recruiting</td>
          <td><span class="pill pill-high">HIGH</span></td>
          <td>Apply now — 3 alerts sent</td>
        </tr>
        <tr>
          <td>LinkedIn Job Alerts (inbox)</td>
          <td>Human Resources Director at Iceberg: up to $210K/yr (2nd)</td>
          <td>Duplicate alert</td>
          <td><span class="pill pill-high">HIGH</span></td>
          <td>Same role — de-dupe</td>
        </tr>
        <tr>
          <td>LinkedIn Job Alerts (inbox)</td>
          <td>Human Resources Director at Iceberg: up to $210K/yr (3rd)</td>
          <td>Duplicate alert</td>
          <td><span class="pill pill-high">HIGH</span></td>
          <td>Same role — de-dupe</td>
        </tr>
        <tr>
          <td>LinkedIn Job Alerts (inbox)</td>
          <td>Chief People Officer at Kinora Group</td>
          <td>New alert</td>
          <td><span class="pill pill-high">HIGH</span></td>
          <td>Review &amp; apply</td>
        </tr>
        <tr>
          <td>LinkedIn Job Alerts (inbox)</td>
          <td>Chief People Officer at Kinora Group (2nd)</td>
          <td>Duplicate alert</td>
          <td><span class="pill pill-high">HIGH</span></td>
          <td>Same role — de-dupe</td>
        </tr>
        <tr>
          <td>LinkedIn Job Alerts (inbox)</td>
          <td>VP of People at Orbital</td>
          <td>New alert</td>
          <td><span class="pill pill-high">HIGH</span></td>
          <td>Review &amp; apply</td>
        </tr>
        <tr>
          <td>Indeed / Dennis Gorelik (PostJobFree)</td>
          <td>Senior Manager, Corporate Programs @ Avalara ($136K–$272K)</td>
          <td>Not in inbox</td>
          <td><span class="pill pill-medium">MEDIUM</span></td>
          <td>Review if interested</td>
        </tr>
        <tr>
          <td>PostJobFree / Dennis Gorelik (Trash)</td>
          <td>Roads to Success — Director of HR, Manhattan NY</td>
          <td>In Trash</td>
          <td><span class="pill pill-high">HIGH</span></td>
          <td>Restore from Trash; review role</td>
        </tr>
        <tr>
          <td>JobLeads (Trash)</td>
          <td>5 new jobs matching CPO / Lead Talent Culture Change</td>
          <td>In Trash</td>
          <td><span class="pill pill-medium">MEDIUM</span></td>
          <td>Consider restoring to review matches</td>
        </tr>
      </tbody>
    </table>
    <div class="small-note" style="margin-top:6px;">Note: LinkedIn is sending duplicate alerts for Iceberg (3x) and Kinora (2x). Consider adjusting LinkedIn alert frequency settings.</div>

    <hr class="divider">

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="group-header" style="background:#f5eef8; color:#6c3483; border-left: 4px solid #8e44ad;">🟣 Professional Development — 3 Emails</div>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Location</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>Nader / Building Leverage (inbox)</td>
          <td>We built a billionaire's personal brand… (Richard Harpin LinkedIn playbook)</td>
          <td>Inbox</td>
          <td>Read — relevant to your LinkedIn job search strategy</td>
        </tr>
        <tr>
          <td>Ruben Hassid / Substack (inbox)</td>
          <td>Cowork. (Claude Cowork setup guide)</td>
          <td>Inbox</td>
          <td>Review if interested in AI productivity tools</td>
        </tr>
        <tr>
          <td>Ruben Hassid / Substack (inbox)</td>
          <td>Cowork (August 2026). (duplicate)</td>
          <td>Inbox</td>
          <td>Duplicate of above — archive one</td>
        </tr>
      </tbody>
    </table>

    <hr class="divider">

    <!-- FINANCIAL / BILLING -->
    <div class="group-header" style="background:#fef9ec; color:#935116; border-left: 4px solid #e67e22;">🟡 Financial / Billing — 1 Email</div>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>Apple &lt;no_reply@email.apple.com&gt; (inbox)</td>
          <td>Your receipt from Apple. ("A Bar Song (Irish Folk)" + other items)</td>
          <td>Verify all charges at appleid.apple.com — legitimate receipt from verified Apple domain</td>
        </tr>
      </tbody>
    </table>

    <hr class="divider">

    <!-- PERSONAL -->
    <div class="group-header" style="background:#eaf4fb; color:#1a5276; border-left: 4px solid #2980b9;">🔵 Personal — 3 Emails</div>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Notes</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>Match (inbox)</td>
          <td>Profile view from Kevin, 58, Jamesburg NJ</td>
          <td>Dating app notification</td>
          <td>View at your discretion</td>
        </tr>
        <tr>
          <td>Jdate (Trash)</td>
          <td>You've Got a Like on Jdate ❤️</td>
          <td>Dating app, went to Trash</td>
          <td>Check app directly if interested; safe to delete email</td>
        </tr>
        <tr>
          <td>Melissa W / self (inbox)</td>
          <td>How To Remove The New Claude Watermarks | Maverick AI</td>
          <td>Self-sent link to mavgpt.ai resource</td>
          <td>Review URL carefully before clicking — verify this is a link you sent yourself for legitimate use</td>
        </tr>
      </tbody>
    </table>
    <div class="small-note" style="margin-top:6px;">Note: OkCupid "Someone likes you" (Trash) also falls in this category — see Trash Review.</div>

    <hr class="divider">

    <!-- NEWSLETTERS / SUBSCRIPTIONS -->
    <div class="group-header" style="background:#f5eef8; color:#6c3483; border-left: 4px solid #8e44ad;">🟣 Newsletters &amp; Subscriptions — 7 Emails</div>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Location</th><th>Recommendation</th></tr></thead>
      <tbody>
        <tr>
          <td>Medium Daily Digest (Trash)</td>
          <td>Product Discovery Beginner's Guide for Business Analysis</td>
          <td>Trash</td>
          <td>Unsubscribe or review on Medium directly</td>
        </tr>
        <tr>
          <td>The Hustle (Trash)</td>
          <td>🍕 Pizza fight! This week's wildest business stories</td>
          <td>Trash</td>
          <td>Keep subscription if you enjoy it; delete email</td>
        </tr>
        <tr>
          <td>Dylan's Diary / Behind the Markets (Trash)</td>
          <td>Washington just put $3 billion behind one gold mine</td>
          <td>Trash</td>
          <td>Finance/investment newsletter — review if relevant; otherwise unsubscribe</td>
        </tr>
        <tr>
          <td>LinkedIn (Trash)</td>
          <td>Daily Rundown: Meta and SpaceX strike back; Workers' heat risk rises</td>
          <td>Trash</td>
          <td>Professional news — read on LinkedIn app; delete email</td>
        </tr>
        <tr>
          <td>David Green via LinkedIn (Trash)</td>
          <td>How HR can own Workforce Transformation in the AI era</td>
          <td>Trash</td>
          <td>Relevant to HR expertise — consider reading before deleting</td>
        </tr>
        <tr>
          <td>Insider Monkey (Trash)</td>
          <td>Daily Newsletter Aug 15 — Undervalued AI Stock</td>
          <td>Trash</td>
          <td>Investment/finance newsletter — delete or unsubscribe</td>
        </tr>
        <tr>
          <td>Vaishali Lambe / Medium (Trash)</td>
          <td>Navigating AI's Progress Puzzle: Lessons for Roadmap Builders</td>
          <td>Trash</td>
          <td>AI/strategy content — skim if relevant to your work; otherwise delete</td>
        </tr>
      </tbody>
    </table>

    <hr class="divider">

    <!-- PROMOTIONAL / RETAIL -->
    <div class="group-header" style="background:#f8f9fa; color:#555; border-left: 4px solid #95a5a6;">⬜ Promotional / Retail — 9 Emails (all in Trash)</div>
    <table>
      <thead><tr><th>Brand</th><th>Subject</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>CVS ExtraCare (Trash)</td><td>Your New York Store Has Special Sale Prices</td><td>Delete — no urgency</td></tr>
        <tr><td>Kohl's (Trash)</td><td>Your deal is waiting to be revealed 👀</td><td>Delete</td></tr>
        <tr><td>Gap Factory (Trash — auto newsletter)</td><td>50% off everything* (new arrivals included)</td><td>Auto-trashed newsletter — delete</td></tr>
        <tr><td>VIVAIA (Trash)</td><td>New In: Jewelry for Your Loafers ✨💎</td><td>Delete</td></tr>
        <tr><td>SHEIN (Trash)</td><td>New PRE-FALL Faves Have Entered the Chat 😏</td><td>Delete</td></tr>
        <tr><td>Laura Geller (Trash, 2 emails)</td><td>Up to 70% OFF Sale Picks Ends Soon ⏰ (sent twice)</td><td>Delete both — duplicate send</td></tr>
        <tr><td>Temu (Trash)</td><td>Makeup organizer is receiving stellar reviews</td><td>Delete</td></tr>
        <tr><td>Equifax (Trash)</td><td>Checked your credit score lately? 👀 ($1 for 30 days)</td><td>Delete — promotional offer, check credit free at annualcreditreport.com</td></tr>
      </tbody>
    </table>

    <hr class="divider">

    <!-- SPAM / SAFE TO DELETE -->
    <div class="group-header" style="background:#fdf2f2; color:#922b21; border-left: 4px solid #c0392b;">🔴 Spam / Safe to Delete — 10 Emails</div>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Category</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>Congratulations 🎉 (spoofed)</td><td>$7,500 Welcome Package + 30 Free Spins 🎁 (in Trash)</td><td>Casino spam</td><td>Delete — already trashed</td></tr>
        <tr><td>OnlineCasino 🚀 (spoofed)</td><td>No Deposit Needed🔥 claim your 55 Free Spins instantly!</td><td>Casino spam</td><td>Delete — trash manually</td></tr>
        <tr><td>Casino Exclusive (spoofed)</td><td>Use Code: 200GETLUCKY for welcome bonus + 30 free spins 💰</td><td>Casino spam</td><td>Delete — trash manually</td></tr>
        <tr><td>Penis Growth Doctor (spoofed)</td><td>Stop Being Small Add 3.8 Inches in 12 Days at Home</td><td>Medical spam</td><td>Delete — trash manually</td></tr>
        <tr><td>MaleVitalityInsider (spoofed)</td><td>The 1-minute trick for lasting 30+ minutes</td><td>Sexual spam</td><td>Delete — trash manually</td></tr>
        <tr><td>Dr. Mark (spoofed)</td><td>The ED cause nobody is talking about</td><td>Sexual spam</td><td>Delete — trash manually</td></tr>
        <tr><td>Skinny You (spoofed)</td><td>Over 10 Million Americans are already losing weight the easy way</td><td>Weight loss spam</td><td>Delete — trash manually</td></tr>
        <tr><td>Perfect Vision (Trash)</td><td>The Overlooked Reason Eyes Feel Strained</td><td>Health spam</td><td>Delete — already trashed</td></tr>
        <tr><td>Lung
