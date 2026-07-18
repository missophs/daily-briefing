<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa Weiss — July 18, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px 60px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px 24px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 15px; color: #a8c0e8; margin-top: 4px; }
  .header-stats { display: flex; gap: 24px; margin-top: 18px; flex-wrap: wrap; }
  .stat-pill { background: rgba(255,255,255,0.12); border-radius: 8px; padding: 8px 18px; font-size: 13px; color: #dce8ff; }
  .stat-pill strong { color: #fff; font-size: 16px; display: block; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; letter-spacing: 0.3px; padding: 10px 16px; border-radius: 8px 8px 0 0; color: #fff; margin-bottom: 0; }
  .section-body { background: #fff; border-radius: 0 0 10px 10px; padding: 18px 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }

  /* COLOR THEMES */
  .red .section-title    { background: #c0392b; }
  .yellow .section-title { background: #d4830a; }
  .blue .section-title   { background: #1565c0; }
  .green .section-title  { background: #1e7e34; }
  .purple .section-title { background: #6a1b9a; }
  .gray .section-title   { background: #555e6e; }
  .teal .section-title   { background: #00796b; }
  .navy .section-title   { background: #1a1a2e; }

  .red-border    { border-left: 5px solid #c0392b; }
  .yellow-border { border-left: 5px solid #d4830a; }
  .blue-border   { border-left: 5px solid #1565c0; }
  .green-border  { border-left: 5px solid #1e7e34; }
  .purple-border { border-left: 5px solid #6a1b9a; }
  .gray-border   { border-left: 5px solid #888; }
  .teal-border   { border-left: 5px solid #00796b; }

  /* CARDS */
  .card { border-radius: 8px; padding: 14px 16px; margin-bottom: 12px; background: #f8f9fb; }
  .card-title { font-weight: 700; font-size: 14px; margin-bottom: 4px; }
  .card-row { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 4px; }
  .badge { display: inline-block; border-radius: 5px; padding: 2px 9px; font-size: 11px; font-weight: 700; }
  .badge-red    { background: #fdecea; color: #c0392b; }
  .badge-yellow { background: #fff8e1; color: #b7660a; }
  .badge-green  { background: #e8f5e9; color: #1e7e34; }
  .badge-blue   { background: #e3f0fd; color: #1565c0; }
  .badge-purple { background: #f3e5f5; color: #6a1b9a; }
  .badge-gray   { background: #eceff1; color: #546e7a; }
  .badge-teal   { background: #e0f2f1; color: #00796b; }
  .badge-orange { background: #fff3e0; color: #e65100; }

  /* EXEC SUMMARY */
  .exec-bullet { display: flex; align-items: flex-start; gap: 12px; padding: 12px 0; border-bottom: 1px solid #eee; }
  .exec-bullet:last-child { border-bottom: none; }
  .exec-icon { font-size: 22px; min-width: 30px; }
  .exec-text strong { display: block; font-size: 14px; margin-bottom: 2px; }
  .exec-text span { font-size: 13px; color: #555; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { font-weight: 700; font-size: 14px; background: #e3f0fd; color: #1565c0; padding: 6px 14px; border-radius: 6px; margin-bottom: 8px; }
  .cal-event { background: #f0f4ff; border-left: 4px solid #1565c0; border-radius: 5px; padding: 10px 14px; margin-bottom: 8px; }
  .cal-event.declined { border-left-color: #c0392b; background: #fff0ee; }
  .cal-event.needs-action { border-left-color: #d4830a; background: #fffbf0; }
  .cal-event.birthday { border-left-color: #e91e8c; background: #fff0f8; }
  .cal-event.bill { border-left-color: #00796b; background: #e0f2f1; }
  .cal-event-title { font-weight: 700; font-size: 14px; }
  .cal-meta { font-size: 12px; color: #555; margin-top: 3px; }
  .cal-meta span { margin-right: 12px; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #1a1a2e; color: #fff; padding: 9px 12px; text-align: left; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
  td { padding: 8px 12px; border-bottom: 1px solid #eef0f3; vertical-align: top; }
  tr:nth-child(even) td { background: #f8f9fb; }
  tr:hover td { background: #eef4ff; }

  /* EMAIL ROWS */
  .email-row { padding: 9px 0; border-bottom: 1px solid #f0f0f0; display: flex; gap: 10px; align-items: flex-start; }
  .email-row:last-child { border-bottom: none; }
  .email-sender { font-weight: 600; min-width: 160px; font-size: 13px; }
  .email-subject { flex: 1; font-size: 13px; color: #333; }
  .email-note { font-size: 11px; color: #888; min-width: 120px; text-align: right; }

  /* DASHBOARD GRID */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-tile { background: #fff; border-radius: 10px; padding: 16px 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
  .dash-tile .tile-label { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: #888; margin-bottom: 6px; }
  .dash-tile .tile-value { font-size: 26px; font-weight: 800; }
  .dash-tile .tile-sub { font-size: 12px; color: #666; margin-top: 4px; }
  .tile-red    { border-top: 4px solid #c0392b; }
  .tile-yellow { border-top: 4px solid #d4830a; }
  .tile-blue   { border-top: 4px solid #1565c0; }
  .tile-green  { border-top: 4px solid #1e7e34; }
  .tile-purple { border-top: 4px solid #6a1b9a; }
  .tile-gray   { border-top: 4px solid #888; }
  .tile-teal   { border-top: 4px solid #00796b; }

  /* PRIORITY TABLE */
  .pri-high   { color: #c0392b; font-weight: 700; }
  .pri-medium { color: #d4830a; font-weight: 700; }
  .pri-low    { color: #1e7e34; font-weight: 700; }

  /* TOP 3 */
  .top3 { display: flex; gap: 16px; flex-wrap: wrap; }
  .top3-card { flex: 1; min-width: 260px; background: linear-gradient(135deg, #1a1a2e, #0f3460); color: #fff; border-radius: 12px; padding: 20px 22px; }
  .top3-num { font-size: 42px; font-weight: 900; color: rgba(255,255,255,0.15); line-height: 1; }
  .top3-title { font-size: 16px; font-weight: 700; margin-top: -10px; }
  .top3-detail { font-size: 13px; color: #a8c0e8; margin-top: 8px; }

  /* TRASH */
  .trash-group { margin-bottom: 16px; }
  .trash-group-label { font-weight: 700; font-size: 13px; padding: 5px 12px; border-radius: 5px; display: inline-block; margin-bottom: 8px; }
  .trash-restore { background: #e8f5e9; color: #1e7e34; }
  .trash-review  { background: #fff8e1; color: #b7660a; }
  .trash-delete  { background: #fdecea; color: #c0392b; }

  /* ALERT BOX */
  .alert-box { border-radius: 8px; padding: 12px 16px; margin-bottom: 12px; font-size: 13px; }
  .alert-red    { background: #fdecea; border-left: 5px solid #c0392b; color: #7b1a13; }
  .alert-yellow { background: #fff8e1; border-left: 5px solid #d4830a; color: #7a4400; }
  .alert-green  { background: #e8f5e9; border-left: 5px solid #1e7e34; color: #14491e; }
  .alert-blue   { background: #e3f0fd; border-left: 5px solid #1565c0; color: #0d3b7a; }

  .divider { height: 1px; background: #e8eaf0; margin: 16px 0; }
  .tag { display: inline-block; font-size: 11px; padding: 2px 7px; border-radius: 4px; margin-right: 4px; margin-top: 2px; }
  .unread-dot { display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: #1565c0; margin-right: 5px; vertical-align: middle; }
  .muted { color: #888; font-size: 12px; }
  .fit-high   { color: #1e7e34; font-weight: 700; font-size: 12px; }
  .fit-medium { color: #d4830a; font-weight: 700; font-size: 12px; }
  .fit-low    { color: #888; font-weight: 700; font-size: 12px; }

  @media (max-width: 600px) {
    .header { padding: 20px 16px; }
    .top3 { flex-direction: column; }
    .dash-grid { grid-template-columns: 1fr 1fr; }
  }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════════════
     1. HEADER
     ═══════════════════════════════════════════════════════════ -->
<div class="header">
  <div class="subtitle">📋 Executive Morning Briefing</div>
  <h1>Good Morning, Melissa 👋</h1>
  <div class="subtitle">Saturday, July 18, 2026 &nbsp;|&nbsp; Prepared by your Executive Chief of Staff</div>
  <div class="header-stats">
    <div class="stat-pill"><strong>50</strong>Emails Reviewed</div>
    <div class="stat-pill"><strong>10</strong>Calendar Events</div>
    <div class="stat-pill"><strong>3</strong>Security / Risk Flags</div>
    <div class="stat-pill"><strong>9</strong>Job Leads</div>
    <div class="stat-pill"><strong>5</strong>Action Items</div>
    <div class="stat-pill"><strong>7</strong>Days Ahead Covered</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     11. DASHBOARD (moved up for quick scan)
     ═══════════════════════════════════════════════════════════ -->
<div class="section navy">
  <div class="section-title">📊 Dashboard — At a Glance</div>
  <div class="section-body" style="background:#1a1a2e; border-radius:0 0 10px 10px; padding:18px 20px;">
    <div class="dash-grid">
      <div class="dash-tile tile-red">
        <div class="tile-label">🚨 Security Alerts</div>
        <div class="tile-value" style="color:#c0392b;">5</div>
        <div class="tile-sub">Phishing / Scam / Spam flagged</div>
      </div>
      <div class="dash-tile tile-yellow">
        <div class="tile-label">⚡ Action Required</div>
        <div class="tile-value" style="color:#d4830a;">5</div>
        <div class="tile-sub">Zoho invoice, NYU MyChart, RSVPs, Match, Granola privacy</div>
      </div>
      <div class="dash-tile tile-green">
        <div class="tile-label">💼 Open Job Leads</div>
        <div class="tile-value" style="color:#1e7e34;">9</div>
        <div class="tile-sub">LinkedIn + Glassdoor alerts; Nanit application sent</div>
      </div>
      <div class="dash-tile tile-blue">
        <div class="tile-label">📅 Upcoming Meetings</div>
        <div class="tile-value" style="color:#1565c0;">5</div>
        <div class="tile-sub">PT (Mon), Umi (Tue), HR Network x2 (Wed), Exec RT (Thu–declined)</div>
      </div>
      <div class="dash-tile tile-teal">
        <div class="tile-label">💳 Bills / Deadlines</div>
        <div class="tile-value" style="color:#00796b;">3</div>
        <div class="tile-sub">Zoho invoice (paid), Target CC statement, Verizon Fios (Thu)</div>
      </div>
      <div class="dash-tile tile-purple">
        <div class="tile-label">🎂 Birthdays This Week</div>
        <div class="tile-value" style="color:#6a1b9a;">2</div>
        <div class="tile-sub">Eric Dordick (Tue 7/21), Amy Fink (Thu 7/23)</div>
      </div>
      <div class="dash-tile tile-gray">
        <div class="tile-label">🗑️ Trash Items</div>
        <div class="tile-value" style="color:#555;">11</div>
        <div class="tile-sub">9 safe to delete, 1 restore (Zoho renewal), 1 review</div>
      </div>
      <div class="dash-tile tile-yellow">
        <div class="tile-label">📬 Important Unread</div>
        <div class="tile-value" style="color:#d4830a;">6</div>
        <div class="tile-sub">NYU MyChart, Zoho invoice, Granola privacy, Target CC, Match x2</div>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     2. EXECUTIVE SUMMARY
     ═══════════════════════════════════════════════════════════ -->
<div class="section red">
  <div class="section-title">🧭 Executive Summary — Three Things You Need to Know Right Now</div>
  <div class="section-body">
    <div class="exec-bullet">
      <div class="exec-icon">🚨</div>
      <div class="exec-text">
        <strong>BIGGEST RISK: Multiple phishing and scam emails detected — 2 auto-trashed, 3 additional flagged</strong>
        <span>Two emails were automatically removed before reaching your inbox: a spoofed Lowe's prize scam and a Firebase-hosted credential-harvesting attempt. Three additional scam/spam emails (fake casino, adult spam, fake nerve-pain "doctor") are sitting outside trash — verify they are not in your inbox and mark as spam. No credentials appear to have been compromised, but vigilance is required.</span>
      </div>
    </div>
    <div class="exec-bullet">
      <div class="exec-icon">💼</div>
      <div class="exec-text">
        <strong>BIGGEST OPPORTUNITY: 9 senior HR/People leadership roles surfaced — including up to $380K; Nanit application already submitted</strong>
        <span>LinkedIn and Glassdoor surfaced VP/CHRO/Principal HRBP roles ranging from $255K–$380K. You already applied to Nanit (VP, People — confirmation in trash) and received a thank-you. Prioritize reviewing Function Health (Principal HRBP) and Hoxton Circle (VP HR, PE — up to $325K) today while the postings are fresh.</span>
      </div>
    </div>
    <div class="exec-bullet">
      <div class="exec-icon">📅</div>
      <div class="exec-text">
        <strong>BIGGEST CALENDAR ITEM: Two HR Networking sessions need RSVP this week — Wednesday July 22 (12–1:30 PM) and Thursday July 23 (12–1 PM)</strong>
        <span>Both events show status "needsAction" — you have not responded. The Thursday Executive Roundtable (hosted by John Madigan) was declined; confirm that was intentional. Verizon Fios bill is also due Thursday July 23 — schedule payment today.</span>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     3. ACTION REQUIRED
     ═══════════════════════════════════════════════════════════ -->
<div class="section yellow">
  <div class="section-title">⚡ Action Required</div>
  <div class="section-body">

    <div class="card yellow-border">
      <div class="card-row"><span class="badge badge-yellow">BILLING</span><span class="badge badge-teal">TODAY</span></div>
      <div class="card-title">Zoho Invoice #50102280518 — Subscription Payment Received</div>
      <div class="muted">From: Zoho Payments &lt;payments@zohocorp.com&gt; | Received: Sat Jul 18, 2026</div>
      <p style="margin-top:6px;font-size:13px;">Your Zoho subscription payment was processed on Jul 18, 2026. Invoice attached to the email. A second Zoho Workplace renewal confirmation is also in trash from <em>notification@zohostore.com</em>.</p>
      <p style="margin-top:6px;"><strong>Why it matters:</strong> Confirm the charge matches your expected subscription tier. Download invoice for records.</p>
      <p style="margin-top:4px;"><strong>Next step:</strong> Open email, download invoice, file in accounting folder. Cross-check Zoho Workplace renewal (trash item) to ensure no duplicate billing.</p>
    </div>

    <div class="card red-border">
      <div class="card-row"><span class="badge badge-red">MEDICAL</span><span class="badge badge-red">URGENT</span></div>
      <div class="card-title">New Message in NYU Langone Health MyChart</div>
      <div class="muted">From: mychart.donotreply@nyulangone.org | Received: Fri Jul 17, 2026, 11:06 PM</div>
      <p style="margin-top:6px;font-size:13px;">You have an unread message from your NYU Langone Health care team waiting in MyChart. Contents unknown — could be test results, follow-up instructions, or appointment information.</p>
      <p style="margin-top:6px;"><strong>Why it matters:</strong> Medical messages require timely review — could be lab results or action needed.</p>
      <p style="margin-top:4px;"><strong>Next step:</strong> Log in to NYU Langone MyChart app or website now and read the message. Respond or schedule any follow-up care as indicated.</p>
    </div>

    <div class="card yellow-border">
      <div class="card-row"><span class="badge badge-yellow">RSVP NEEDED</span><span class="badge badge-blue">WEDNESDAY</span></div>
      <div class="card-title">HR Networking &amp; Job Search Group — Zoom Session (needs RSVP)</div>
      <div class="muted">Calendar Event | Wed Jul 22, 2026 | 12:00–1:30 PM ET | Zoom</div>
      <p style="margin-top:6px;font-size:13px;">Your calendar status shows "needsAction." Large networking group (~170 attendees). Zoom link: us06web.zoom.us/j/81954171722.</p>
      <p style="margin-top:6px;"><strong>Why it matters:</strong> Active job search — missing this networking session would be a lost opportunity. Organizer may be tracking attendance.</p>
      <p style="margin-top:4px;"><strong>Next step:</strong> Accept or decline the calendar invite today. If attending, prepare your 30-second intro and any questions for the group.</p>
      <p><strong>Due:</strong> RSVP by Sunday Jul 19</p>
    </div>

    <div class="card yellow-border">
      <div class="card-row"><span class="badge badge-yellow">RSVP NEEDED</span><span class="badge badge-blue">THURSDAY</span></div>
      <div class="card-title">HR Networking &amp; Job Search: Open Office Hours — Zoom (needs RSVP)</div>
      <div class="muted">Calendar Event | Thu Jul 23, 2026 | 12:00–1:00 PM ET | Zoom</div>
      <p style="margin-top:6px;font-size:13px;">Separate open office hours session — also "needsAction." Note: organizer requests no AI note-taking tools. Zoom link: us06web.zoom.us/j/85945371140.</p>
      <p style="margin-top:6px;"><strong>Why it matters:</strong> Informal networking sessions often yield the best connections and leads during a job search.</p>
      <p style="margin-top:4px;"><strong>Next step:</strong> Accept or decline. If attending, come with 1–2 specific asks or job leads to discuss.</p>
      <p><strong>Due:</strong> RSVP by Monday Jul 20</p>
    </div>

    <div class="card teal-border">
      <div class="card-row"><span class="badge badge-teal">BILLING</span><span class="badge badge-yellow">THURSDAY</span></div>
      <div class="card-title">Verizon Fios Bill Due — July 23, 2026</div>
      <div class="muted">Calendar Reminder | Thu Jul 23, 2026 (all-day)</div>
      <p style="margin-top:6px;font-size:13px;">Verizon Fios bill appears on your calendar for Thursday. No email invoice visible in current data.</p>
      <p style="margin-top:6px;"><strong>Why it matters:</strong> Late payment could affect service or incur fees.</p>
      <p style="margin-top:4px;"><strong>Next step:</strong> Log in to Verizon or My Fios app to verify amount and pay, or confirm auto-pay is set up.</p>
      <p><strong>Due:</strong> Thu Jul 23</p>
    </div>

    <div class="card purple-border">
      <div class="card-row"><span class="badge badge-purple">PRIVACY</span><span class="badge badge-yellow">REVIEW</span></div>
      <div class="card-title">Granola Updated Privacy Policy</div>
      <div class="muted">From: Granola &lt;notifications@mail.granola.ai&gt; | Received: Sat Jul 18, 2026</div>
      <p style="margin-top:6px;font-size:13px;">Granola (AI note-taking tool) has updated its Privacy Policy. As a user, changes to how your meeting data is stored and used may affect your professional meetings.</p>
      <p style="margin-top:6px;"><strong>Why it matters:</strong> AI note-taking tools capture sensitive meeting content. Privacy policy changes may affect data retention or sharing.</p>
      <p style="margin-top:4px;"><strong>Next step:</strong> Review the updated Privacy Policy. Note the HR Networking group explicitly requests no AI note-taking — this is relevant context.</p>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     4. FULL 7-DAY CALENDAR
     ═══════════════════════════════════════════════════════════ -->
<div class="section blue">
  <div class="section-title">📅 Full 7-Day Calendar — July 18–24, 2026</div>
  <div class="section-body">

    <div class="alert-box alert-blue">
      <strong>Today is Saturday, July 18.</strong> No calendar events scheduled for today. Use the day for job search review, RSVPs, and addressing security items.
    </div>

    <!-- SUNDAY -->
    <div class="cal-day">
      <div class="cal-day-header">☀️ Sunday, July 19, 2026</div>
      <div style="padding:10px;color:#888;font-style:italic;font-size:13px;">No calendar events. Recommended: RSVP to Wednesday HR Networking session; review Nanit application status.</div>
    </div>

    <!-- MONDAY -->
    <div class="cal-day">
      <div class="cal-day-header">📌 Monday, July 20, 2026</div>
      <div class="cal-event">
        <div class="cal-event-title">🏋️ PT (Physical Therapy / Personal Training)</div>
        <div class="cal-meta">
          <span>⏰ 1:45 PM – 2:45 PM ET</span>
          <span class="badge badge-green">Confirmed</span>
        </div>
        <div class="cal-meta" style="margin-top:4px;">📍 Location not specified &nbsp;|&nbsp; No attendees listed &nbsp;|&nbsp; <em>Note: Appears twice in calendar data — likely a duplicate entry.</em></div>
        <div class="cal-meta" style="margin-top:4px;">⚠️ <strong>Duplicate Warning:</strong> This event is listed twice with identical details. Recommend deleting the duplicate from Google Calendar.</div>
        <div class="cal-meta" style="margin-top:4px;"><strong>Prep:</strong> Confirm appointment location and bring any relevant gear/notes.</div>
      </div>
    </div>

    <!-- TUESDAY -->
    <div class="cal-day">
      <div class="cal-day-header">📌 Tuesday, July 21, 2026</div>
      <div class="cal-event birthday">
        <div class="cal-event-title">🎂 Eric Dordick's Birthday</div>
        <div class="cal-meta"><span>All Day</span><span class="badge badge-purple">Birthday</span></div>
        <div class="cal-meta" style="margin-top:4px;"><strong>Prep:</strong> Send a birthday message today — text, call, or LinkedIn note.</div>
      </div>
      <div class="cal-event">
        <div class="cal-event-title">📞 Umi</div>
        <div class="cal-meta">
          <span>⏰ 10:00 AM – 11:00 AM ET</span>
          <span class="badge badge-green">Confirmed</span>
        </div>
        <div class="cal-meta" style="margin-top:4px;">📍 Location not specified &nbsp;|&nbsp; No attendees listed</div>
        <div class="cal-meta" style="margin-top:4px;"><strong>Prep:</strong> Confirm whether this is a phone call, video call, or in-person. Prepare any agenda items in advance.</div>
      </div>
    </div>

    <!-- WEDNESDAY -->
    <div class="cal-day">
      <div class="cal-day-header">📌 Wednesday, July 22, 2026</div>
      <div class="cal-event needs-action">
        <div class="cal-event-title">🤝 HR Networking &amp; Job Search Group — Zoom Session 2</div>
        <div class="cal-meta">
          <span>⏰ 12:00 PM – 1:30 PM ET</span>
          <span class="badge badge-yellow">⚠️ RSVP Needed</span>
        </div>
        <div class="cal-meta" style="margin-top:4px;">📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a> &nbsp;|&nbsp; ~170 attendees</div>
        <div class="cal-meta" style="margin-top:4px;"><strong>Prep:</strong> Accept invite. Prepare 30-second introduction. Review attendee list for warm connections. Have 1–2 specific job targets ready to mention.</div>
      </div>
      <div class="cal-event">
        <div class="cal-event-title">🗒️ Network (Personal Reminder)</div>
        <div class="cal-meta">
          <span>⏰ 12:00 PM – 1:30 PM ET</span>
          <span class="badge badge-green">Confirmed</span>
        </div>
        <div class="cal-meta" style="margin-top:4px;">📍 No location — appears to be a personal blocking note coinciding with the HR Networking Zoom above.</div>
        <div class="cal-meta" style="margin-top:4px;"><strong>Note:</strong> Likely a personal placeholder alongside the HR Networking group event. Confirm they are not conflicting separate events.</div>
      </div>
    </div>

    <!-- THURSDAY -->
    <div class="cal-day">
      <div class="cal-day-header">📌 Thursday, July 23, 2026</div>
      <div class="cal-event birthday">
        <div class="cal-event-title">🎂 Amy Fink's Birthday</div>
        <div class="cal-meta"><span>All Day</span><span class="badge badge-purple">Birthday</span></div>
        <div class="cal-meta" style="margin-top:4px;"><strong>Prep:</strong> Send a birthday message — text, call, card, or social post.</div>
      </div>
      <div class="cal-event bill">
        <div class="cal-event-title">💳 Verizon Fios Bill Due</div>
        <div class="cal-meta"><span>All Day</span><span class="badge badge-teal">Bill Reminder</span></div>
        <div class="cal-meta" style="margin-top:4px;"><strong>Action:</strong> Pay Verizon Fios bill or confirm auto-pay. Log in to My Fios app to verify.</div>
      </div>
      <div class="cal-event declined">
        <div class="cal-event-title">❌ Executive Roundtable (Declined)</div>
        <div class="cal-meta">
          <span>⏰ 9:00 AM – 10:30 AM ET</span>
          <span class="badge badge-red">Declined</span>
        </div>
        <div class="cal-meta" style="margin-top:4px;">📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link (John Madigan)</a></div>
        <div class="cal-meta" style="margin-top:4px;"><strong>Note:</strong> You have already declined this invite. Confirm this was intentional — Executive Roundtables can be valuable networking touchpoints during a job search. Consider sending John Madigan a note explaining your absence and staying connected.</div>
      </div>
      <div class="cal-event needs-action">
        <div class="cal-event-title">🤝 HR Networking &amp; Job Search: Open Office Hours — Zoom</div>
        <div class="cal-meta">
          <span>⏰ 12:00 PM – 1:00 PM ET</span>
          <span class="badge badge-yellow">⚠️ RSVP Needed</span>
        </div>
        <div class="cal-meta" style="margin-top:4px;">📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a> &nbsp;|&nbsp; ~170 attendees</div>
        <div class="cal-meta" style="margin-top:4px;">⚠️ <strong>Note:</strong> Organizer explicitly requests NO AI note-taking tools (relevant given Granola Privacy Policy update).</div>
        <div class="cal-meta" style="margin-top:4px;"><strong>Prep:</strong> RSVP. Come with specific connection asks. Disable Granola or any AI meeting assistant.</div>
      </div>
    </div>

    <!-- FRIDAY -->
    <div class="cal-day">
      <div class="cal-day-header">📌 Friday, July 24, 2026</div>
      <div style="padding:10px;color:#888;font-style:italic;font-size:13px;">No calendar events. Good window for follow-ups from the week's networking and job applications.</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     5. JOB SEARCH & INTERVIEW PIPELINE
     ═══════════════════════════════════════════════════════════ -->
<div class="section green">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">

    <div class="alert-box alert-green">
      <strong>Active Pipeline:</strong> 9 role alerts received, 1 application confirmed (Nanit). Two HR networking sessions this week. No interview confirmations in current data.
    </div>

    <h3 style="font-size:14px;font-weight:700;margin-bottom:10px;color:#1e7e34;">📧 LinkedIn Job Alerts (Unread)</h3>
    <table>
      <thead>
        <tr><th>Role</th><th>Company</th><th>Salary</th><th>Fit</th><th>Status</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>People Business Partner Leader</td>
          <td>Ladders</td>
          <td style="color:#1e7e34;font-weight:700;">Up to $380K</td>
          <td><span class="fit-high">HIGH</span></td>
          <td><span class="badge badge-yellow">Unread (x2 alerts)</span></td>
          <td>Review &amp; Apply Today</td>
        </tr>
        <tr>
          <td>Principal HR Business Partner</td>
          <td>Function Health</td>
          <td style="color:#555;">Not listed</td>
          <td><span class="fit-high">HIGH</span></td>
          <td><span class="badge badge-yellow">Unread</span></td>
          <td>Review &amp; Apply</td>
        </tr>
        <tr>
          <td>VP, People</td>
          <td>Nanit</td>
          <td style="color:#555;">Not listed</td>
          <td><span class="fit-high">HIGH</span></td>
          <td><span class="badge badge-green">Applied ✓</span></td>
          <td>Await response; thank-you email in trash</td>
        </tr>
        <tr>
          <td>Vice President Human Resources (PE)</td>
          <td>Hoxton Circle</td>
          <td style="color:#1e7e34;font-weight:700;">Up to $325K</td>
          <td><span class="fit-high">HIGH</span></td>
          <td><span class="badge badge-gray">Read (older)</span></td>
          <td>Review if not yet applied</td>
        </tr>
        <tr>
          <td>Chief Human Resources Officer</td>
          <td>Nsight Health</td>
          <td style="color:#1e7e34;font-weight:700;">Up to $255K</td>
          <td><span class="fit-high">HIGH</span></td>
          <td><span class="badge badge-yellow">Unread</span></td>
          <td>Review &amp; Apply</td>
        </tr>
      </tbody>
    </table>

    <div class="divider"></div>

    <h3 style="font-size:14px;font-weight:700;margin-bottom:10px;color:#1e7e34;">📧 Glassdoor Job Alerts</h3>
    <table>
      <thead>
        <tr><th>Role / Alert</th><th>Company / Region</th><th>Fit</th><th>Status</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Community Manager + 6 more jobs</td>
          <td>Twin Pines / New York, NY</td>
          <td><span class="fit-medium">MEDIUM</span></td>
          <td><span class="badge badge-yellow">Unread</span></td>
          <td>Scan for relevant HR roles within the batch</td>
        </tr>
        <tr>
          <td>Global Benefits Senior Manager + 7 more</td>
          <td>HackerOne / Remote, US</td>
          <td><span class="fit-high">HIGH</span></td>
          <td><span class="badge badge-gray">Read (older)</span></td>
          <td>Review Remote options — confirm if actioned</td>
        </tr>
      </tbody>
    </table>

    <div class="divider"></div>

    <h3 style="font-size:14px;font-weight:700;margin-bottom:10px;color:#1e7e34;">📬 Application Tracking</h3>
    <table>
      <thead>
        <tr><th>Company</th><th>Role</th><th>Status</th><th>Date</th><th>Next Step</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Nanit</strong></td>
          <td>VP, People (inferred from alert + confirmation)</td>
          <td><span class="badge badge-green">Application Submitted ✓</span></td>
          <td>Jul 18, 2026</td>
          <td>Thank-you email received (in trash). Await ATS/recruiter outreach. Follow up in 5–7 days if no response.</td>
        </tr>
      </tbody>
    </table>

    <div class="divider"></div>

    <h3 style="font-size:14px;font-weight:700;margin-bottom:10px;color:#1e7e34;">🤝 Networking This Week</h3>
    <table>
      <thead>
        <tr><th>Event</th><th>Date/Time</th><th>RSVP Status</th><th>Value</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>HR Networking &amp; Job Search Group — Zoom 2</td>
          <td>Wed Jul 22 | 12–1:30 PM</td>
          <td><span class="badge badge-yellow">Needs RSVP</span></td>
          <td>HIGH — Large group, active HR community</td>
        </tr>
        <tr>
          <td>HR Networking &amp; Job Search: Open Office Hours</td>
          <td>Thu Jul 23 | 12–1 PM</td>
          <td><span class="badge badge-yellow">Needs RSVP</span></td>
          <td>HIGH — Informal, direct connection opportunity</td>
        </tr>
        <tr>
          <td>Umi (meeting)</td>
          <td>Tue Jul 21 | 10–11 AM</td>
          <td><span class="badge badge-green">Confirmed</span></td>
          <td>MEDIUM — Prepare agenda; networking or personal</td>
        </tr>
      </tbody>
    </table>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     6. FULL EMAIL REVIEW BY CATEGORY
     ═══════════════════════════════════════════════════════════ -->
<div class="section red">
  <div class="section-title">🚨 Category 1: Security / Risk (5 emails)</div>
  <div class="section-body">

    <div class="alert-box alert-red">
      <strong>⚠️ WARNING:</strong> Multiple phishing, scam, and predatory spam emails detected. Two were automatically removed. Three remain outside trash — ensure they are spam-reported.
    </div>

    <div class="card red-border">
      <div class="card-row"><span class="badge badge-red">AUTO-TRASHED — PHISHING</span></div>
      <div class="card-title">"We have been trying to reach you" — Fake Lowe's Prize Scam</div>
      <div class="muted">From: melissaw212@bstebvpbgltto.high178.weekend.commerce.gov.throughters.com | ID: 19f74698f296e2d8</div>
      <p style="margin-top:6px;font-size:13px;">Spoofed Lowe's sender via non-Lowe's domain (throughters.com). Claims you won a Kobalt Tool Set. Fake prize winner scam targeting you by username. <strong>Auto-trashed before reaching inbox.</strong></p>
      <p style="margin-top:4px;"><strong>Auto-trash reason:</strong> Spoofed domain, prize scam targeting username. No action needed — already removed.</p>
    </div>

    <div class="card red-border">
      <div class="card-row"><span class="badge badge-red">AUTO-TRASHED — PHISHING</span></div>
      <div class="card-title">"Sign in to get $50 welcome rewards" — Firebase Credential Harvesting</div>
      <div class="muted">From: noreply@fb-project-0ypwvgpz.firebaseapp.com | ID: 19f7446d271042e6</div>
      <p style="margin-top:6px;font-size:13px;">Firebase-hosted fake sign-in page disguised as a $50 reward claim. Designed to steal login credentials. Randomized project domain is a known phishing pattern. <strong>Auto-trashed before reaching inbox.</strong></p>
      <p style="margin-top:4px;"><strong>Auto-trash reason:</strong> Firebase credential harvesting attempt. No action needed — already removed. Do not click any links if seen elsewhere.</p>
    </div>

    <div class="card red-border">
      <div class="card-row"><span class="badge badge-red">SPAM / SCAM</span><span class="badge badge-orange">REPORT SPAM</span></div>
      <div class="card-title">Adult Spam — Explicit Unsolicited Content</div>
      <div class="muted">From: "🔶FUCK-BUDDY SECRET🔶" &lt;info@xxi.upyhuslotjxkh.us&gt; | ID: 19f742e664b7d170</div>
      <p style="margin-top:6px;font-size:13px;">Explicit +18 unsolicited spam. Highly offensive content. Not in inbox, not in trash — mark as spam immediately to train your spam filter.</p>
      <p style="margin-top:4px;"><strong>Next step:</strong> Open Gmail, find this email, click "Report Spam." Do not click any links.</p>
    </div>

    <div class="card red-border">
      <div class="card-row"><span class="badge badge-red">SPAM / HEALTH SCAM</span></div>
      <div class="card-title">"Did you see this leaked broadcast on nerve pain?" — Fake Health Specialist</div>
      <div class="muted">From: 'Nervertin Relief' &lt;pckigrklhglgdi.81040670718556@s8km9k.9qtqxx.lni7tx.us&gt; | ID: 19f74d235bb592af</div>
      <p style="margin-top:6px;font-size:13px;">Health misinformation scam claiming a "forgotten nerve reset" technique. Suspicious obfuscated domain. Not in inbox. Report spam.</p>
      <p style="margin-top:4px;"><strong>Next step:</strong> Report as spam. Delete.</p>
    </div>

    <div class="card red-border">
      <div class="card-row"><span class="badge badge-red">SPAM / HEALTH SCAM</span></div>
      <div class="card-title">"What If You Could Lose Weight Effortlessly?" — Fake Ozempic/GLP-1 Ad</div>
      <div class="muted">From: 'Ozempic by DirectMeds' &lt;oauuuxajjxkeoz.62347250354068@ii41cc.myuzeg.eiag5v.us&gt; | ID: 19f73b0d7b96e0fc</div>
      <p style="margin-top:6px;font-size:13px;">Unregulated medication marketing via obfuscated domain. Potential health and financial risk. Not in inbox. Report spam.</p>
      <p style="margin-top:4px;"><strong>Next step:</strong> Report as spam. Delete. Consult a licensed physician for any GLP-1 medication inquiries.</p>
    </div>

  </div>
</div>

<!-- JOB SEARCH CATEGORY -->
<div class="section green">
  <div class="section-title">💼 Category 2: Job Search (9 emails)</div>
  <div class="section-body">
    <div class="email-row">
      <span class="unread-dot"></span>
      <span class="email-sender">LinkedIn Job Alerts</span>
      <span class="email-subject">People Business Partner Leader at Ladders — up to $380K/year <em>(2 alerts, same role)</em></span>
      <span class="email-note"><span class="badge badge-green">HIGH FIT</span></span>
    </div>
    <div class="email-row">
      <span class="unread-dot"></span>
      <span class="email-sender">LinkedIn Job Alerts</span>
      <span class="email-subject">Principal HR Business Partner at Function Health</span>
      <span class="email-note"><span class="badge badge-green">HIGH FIT</span></span>
    </div>
    <div class="email-row">
      <span class="unread-dot"></span>
      <span class="email-sender">LinkedIn Job Alerts</span>
      <span class="email-subject">Chief Human Resources Officer at Nsight Health — up to $255K/year</span>
      <span class="email-note"><span class="badge badge-green">HIGH FIT</span></span>
    </div>
    <div class="email-row">
      <span class="unread-dot"></span>
      <span class="email-sender">LinkedIn Job Alerts</span>
      <span class="email-subject">VP, People at Nanit <em>(applied — see Nanit application)</em></span>
      <span class="email-note"><span class="badge badge-teal">APPLIED</span></span>
    </div>
    <div class="email-row">
      <span class="email-sender">LinkedIn Job Alerts</span>
      <span class="email-subject">Vice President Human Resources (Private Equity) at Hoxton Circle — up to $325K/year <em>(read)</em></span>
      <span class="email-note"><span class="badge badge-green">HIGH FIT</span></span>
    </div>
    <div class="email-row">
      <span class="unread-dot"></span>
      <span class="email-sender">Glassdoor Jobs</span>
      <span class="email-subject">Community Manager at Twin Pines and 6 more jobs — New York, NY</span>
      <span class="email-note"><span class="badge badge-yellow">REVIEW</span></span>
    </div>
    <div class="email-row">
      <span class="email-sender">Glassdoor Jobs</span>
      <span class="email-subject">Global Benefits Senior Manager at HackerOne + 7 more — Remote, US <em>(read)</em></span>
      <span class="email-note"><span class="badge badge-yellow">REVIEW</span></span>
    </div>
    <div class="email-row">
      <span class="email-sender">Greenhouse / Nanit</span>
      <span class="email-subject">Thank you for applying to Nanit <em>(in trash — see Trash Review)</em></span>
      <span class="email-note"><span class="badge badge-teal">RESTORE</span></span>
    </div>
    <p style="margin-top:10px;font-size:13px;"><strong>Recommended action:</strong> Review all unread LinkedIn alerts today. The Ladders/People Business Partner Leader role has been sent twice — likely high match. Restore the Nanit confirmation from trash for your records.</p>
  </div>
</div>

<!-- MEDICAL -->
<div class="section red">
  <div class="section-title">🏥 Category 3: Medical / Health (1 email)</div>
  <div class="section-body">
    <div class="card red-border">
      <div class="card-row"><span class="badge badge-red">UNREAD</span><span class="badge badge-red">ACTION REQUIRED</span></div>
      <div class="card-title">New Message in NYU Langone Health MyChart</div>
      <div class="muted">From: mychart.donotreply@nyulangone.org | Fri Jul 17, 11:06 PM</div>
      <p style="margin-top:6px;font-size:13px;">Unread message from NYU Langone Health care team. Contents unknown. Could be lab results, follow-up instructions, prescription updates, or appointment information.</p>
      <p style="margin-top:4px;"><strong>Action:</strong> Log in to MyChart immediately. Do not delay medical communications.</p>
    </div>
  </div>
</div>

<!-- FINANCIAL / BILLING -->
<div class="section yellow">
  <div class="section-title">💳 Category 4: Financial / Billing (4 emails)</div>
  <div class="section-body">
    <div class="email-row">
      <span class="unread-dot"></span>
      <span class="email-sender">Zoho Payments</span>
      <span class="email-subject">Invoice #50102280518 — Subscription Paid Jul 18, 2026 <span class="badge badge-yellow">ACTION: Download &amp; File</span></span>
      <span class="email-note">In Inbox</span>
    </div>
    <div class="email-row">
      <span class="email-sender">Zoho Store Notification</span>
      <span class="email-subject">Zoho Workplace Renewal — Payment Processed Successfully <em>(in trash)</em> <span class="badge badge-teal">RESTORE for records</span></span>
      <span class="email-note">In Trash</span>
    </div>
    <div class="email-row">
      <span class="unread-dot"></span>
      <span class="email-sender">Target Circle Card</span>
      <span class="email-subject">Your Target Circle Card Statement Available — Card ending 7697 <span class="badge badge-yellow">REVIEW</span></span>
      <span class="email-note">In Inbox</span>
    </div>
    <div class="email-row">
      <span class="email-sender">Equifax</span>
      <span class="email-subject">Your Apple Card Credit Limit Offer — Preview Now <em>(read)</em></span>
      <span class="email-note"><span class="badge badge-gray">Low Priority</span></span>
    </div>
    <p style="margin-top:10px;font-size:13px;"><strong>Recommended action:</strong> Download Zoho invoice and restore Zoho Workplace renewal from trash for your financial records. Review Target CC statement for any unexpected charges. The Equifax Apple Card offer is unsolicited marketing — safe to ignore.</p>
  </div>
</div>

<!-- PROFESSIONAL DEVELOPMENT -->
<div class="section purple">
  <div class="section-title">📚 Category 5: Professional Development (4 emails)</div>
  <div class="section-body">
    <div class="email-row">
      <span class="email-sender">LinkedIn</span>
      <span class="email-subject">L'Oréal President Consumer Products Division Post — L'Oréal acquiring Innovist <span class="badge badge-purple">Unread</span></span>
      <span class="email-note">Industry insight</span>
    </div>
    <div class="email-row">
      <span class="email-sender">Fractional In A Box</span>
      <span class="email-subject">How executives really make it to the top — Newsletter Jul 17 <em>(read)</em></span>
      <span class="email-note"><span class="badge badge-gray">Read</span></span>
    </div>
    <div class="email-row">
      <span class="email-sender">Vaishali Lambe / Medium</span>
      <span class="email-subject">Why Augmentation Wins Changes of How Teams Compete? <em>(read)</em></span>
      <span class="email-note"><span class="badge badge-gray">Read</span></span>
    </div>
    <div class="email-row">
      <span class="email-sender">Alison Courses</span>
      <span class="email-subject">How Credible Are Alison Courses? — Course Promotion <em>(read)</em></span>
      <span class="email-note"><span class="badge badge-gray">Low Priority</span></span>
    </div>
    <p style="margin-top:10px;font-size:13px;"><strong>Recommended action:</strong> Read the LinkedIn post about L'Oréal acquiring Innovist — relevant industry intelligence. Fractional In A Box and Medium articles are read; archive or delete. Alison Courses — if not actively pursuing, unsubscribe.</p>
  </div>
</div>

<!-- PERSONAL -->
<div class="section purple">
  <div class="section-title">💛 Category 6: Personal (5 emails)</div>
  <div class="section-body">
    <div class="email-row">
      <span class="unread-dot"></span>
      <span class="email-sender">Match.com</span>
      <span class="email-subject">Harry (69, Albrightsville PA) viewed your profile <span class="badge badge-blue">Unread</span></span>
      <span class="email-note">In Inbox</span>
    </div>
    <div class="email-row">
      <span class="unread-dot"></span>
      <span class="email-sender">Match.com</span>
      <span class="email-subject">Niko likes you — See if it's mutual <span class="badge badge-blue">Unread</span></span>
      <span class="email-note">In Inbox</span>
    </div>
    <div class="email-row">
      <span class="email-sender">Match.com</span>
      <span class="email-subject">Bob (62, Enfield CT) viewed your profile <em>(read)</em></span>
      <span class="email-note"><span class="badge badge-gray">Read</span></span>
    </div>
    <div class="email-row">
      <span class="email-sender">Chick-fil-A</span>
      <span class="email-subject">A little gift from us — 402 pts reward, Operator Jared Caldwell <span class="badge badge-green">Unread</span></span>
      <span class="email-note">In Inbox — Review reward</span>
    </div>
    <div class="email-row">
      <span class="email-sender">Nextdoor (Yorkville)</span>
      <span class="email-subject">NYC Health Commissioner: Legionnaires' Disease Community Cluster Update <em>(read)</em></span>
      <span class="email-note"><span class="badge badge-yellow">Health Alert</span></span>
    </div>
    <p style="margin-top:10px;font-size:13px;"><strong>Recommended action:</strong> Check Match.com when you have a free moment — Niko "liked" you (mutual match available). Claim your Chick-fil-A reward (402 pts). Read the Nextdoor Legionnaires' disease update — this is a local public health notice for the Yorkville neighborhood worth being aware of.</p>
  </div>
</div>

<!-- GRANOLA PRIVACY -->
<div class="section purple">
  <div class="section-title">🔒 Category 7: Privacy / Apps (1 email)</div>
  <div class="section-body">
    <div class="email-row">
      <span class="unread-dot"></span>
      <span class="email-sender">Granola AI</span>
      <span class="email-subject">Updated Privacy Policy — How Granola uses and stores your data <span class="badge badge-yellow">Unread — Review</span></span>
      <span class="email-note">In Inbox</span>
    </div>
    <p style="margin-top:10px;font-size:13px;"><strong>Recommended action:</strong> Read the updated Privacy Policy — especially relevant since the HR Networking sessions explicitly ban AI note-taking. Understand what meeting data Granola retains and whether opt-out is appropriate.</p>
  </div>
</div>

<!-- NEWSLETTERS / SUBSCRIPTIONS -->
<div class="section purple">
  <div class="section-title">📰 Category 8: Newsletters &amp; Subscriptions (5 emails)</div>
  <div class="section-body">
    <table>
      <thead>
        <tr><th>Sender</th><th>Topic</th><th>Status</th><th>Recommendation</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>CoolDeep AI (Beehiiv)</td>
          <td>AI productivity habits (in trash)</td>
