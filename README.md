html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa W. — July 15, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px 48px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px 28px; margin-bottom: 24px; box-shadow: 0 4px 18px rgba(0,0,0,0.18); }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 15px; color: #a8c4e0; margin-top: 4px; }
  .header-meta { display: flex; gap: 28px; margin-top: 18px; flex-wrap: wrap; }
  .header-meta .meta-pill { background: rgba(255,255,255,0.1); border-radius: 20px; padding: 6px 16px; font-size: 13px; color: #d6e8f7; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 14px; padding-bottom: 7px; border-bottom: 3px solid currentColor; }

  /* COLOR THEMES */
  .red    { color: #c0392b; }
  .yellow { color: #b8860b; }
  .blue   { color: #1a5fa8; }
  .green  { color: #1a7a3c; }
  .purple { color: #6b2fa0; }
  .gray   { color: #555; }
  .orange { color: #b85c00; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .card-red    { background: #fff5f5; border-left: 5px solid #c0392b; }
  .card-yellow { background: #fffdf0; border-left: 5px solid #e6b800; }
  .card-blue   { background: #f0f6ff; border-left: 5px solid #1a5fa8; }
  .card-green  { background: #f0fff4; border-left: 5px solid #1a7a3c; }
  .card-purple { background: #faf0ff; border-left: 5px solid #6b2fa0; }
  .card-gray   { background: #f8f8f8; border-left: 5px solid #aaa; }
  .card-orange { background: #fff8f0; border-left: 5px solid #b85c00; }

  .card h3 { font-size: 15px; font-weight: 700; margin-bottom: 6px; }
  .card .meta { font-size: 12px; color: #666; margin-bottom: 6px; }
  .card .label { display: inline-block; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 10px; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px; }
  .label-red    { background: #fde8e8; color: #c0392b; }
  .label-yellow { background: #fff3cd; color: #856404; }
  .label-blue   { background: #dbeafe; color: #1a5fa8; }
  .label-green  { background: #d1fae5; color: #1a7a3c; }
  .label-purple { background: #ede9fe; color: #6b2fa0; }
  .label-gray   { background: #e5e7eb; color: #555; }
  .label-orange { background: #ffedd5; color: #b85c00; }

  .card .why { font-size: 13px; color: #444; margin-bottom: 4px; }
  .card .action { font-size: 13px; font-weight: 600; color: #1a5fa8; margin-top: 6px; }
  .card .due { font-size: 12px; color: #c0392b; font-weight: 600; margin-top: 4px; }

  /* EXECUTIVE SUMMARY */
  .exec-summary { background: #fff; border-radius: 12px; padding: 22px 26px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); margin-bottom: 28px; }
  .exec-summary h2 { font-size: 18px; font-weight: 700; color: #1a1a2e; margin-bottom: 14px; }
  .bullet { display: flex; gap: 12px; margin-bottom: 10px; align-items: flex-start; }
  .bullet-icon { width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; flex-shrink: 0; margin-top: 1px; }
  .bullet-text { font-size: 14px; line-height: 1.5; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  th { background: #1a1a2e; color: #fff; padding: 10px 14px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
  td { padding: 9px 14px; border-bottom: 1px solid #f0f0f0; font-size: 13px; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #fafafa; }
  .tag-high   { background: #fde8e8; color: #c0392b; padding: 2px 8px; border-radius: 8px; font-size: 11px; font-weight: 700; }
  .tag-medium { background: #fff3cd; color: #856404; padding: 2px 8px; border-radius: 8px; font-size: 11px; font-weight: 700; }
  .tag-low    { background: #e5e7eb; color: #555; padding: 2px 8px; border-radius: 8px; font-size: 11px; font-weight: 700; }
  .tag-fit-high   { background: #d1fae5; color: #1a7a3c; padding: 2px 8px; border-radius: 8px; font-size: 11px; font-weight: 700; }
  .tag-fit-med    { background: #dbeafe; color: #1a5fa8; padding: 2px 8px; border-radius: 8px; font-size: 11px; font-weight: 700; }
  .tag-fit-low    { background: #e5e7eb; color: #555; padding: 2px 8px; border-radius: 8px; font-size: 11px; font-weight: 700; }

  /* CALENDAR DAY BLOCK */
  .cal-day { background: #fff; border-radius: 10px; margin-bottom: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); overflow: hidden; }
  .cal-day-header { background: #1a1a2e; color: #fff; padding: 9px 18px; font-size: 14px; font-weight: 700; display: flex; align-items: center; gap: 10px; }
  .cal-day-header .today-badge { background: #e6b800; color: #1a1a2e; font-size: 11px; font-weight: 800; padding: 2px 9px; border-radius: 10px; margin-left: 6px; }
  .cal-event { padding: 12px 18px; border-bottom: 1px solid #f0f0f0; }
  .cal-event:last-child { border-bottom: none; }
  .cal-event-time { font-size: 12px; font-weight: 700; color: #1a5fa8; }
  .cal-event-name { font-size: 14px; font-weight: 700; color: #1a1a2e; margin: 2px 0; }
  .cal-event-detail { font-size: 12px; color: #555; margin-top: 2px; }
  .cal-event-conflict { font-size: 12px; color: #c0392b; font-weight: 600; margin-top: 3px; }
  .rsvp-confirmed { color: #1a7a3c; font-weight: 700; }
  .rsvp-accepted  { color: #1a7a3c; font-weight: 700; }
  .rsvp-needs     { color: #b8860b; font-weight: 700; }
  .rsvp-declined  { color: #c0392b; font-weight: 700; }

  /* DASHBOARD GRID */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; margin-bottom: 28px; }
  .dash-tile { background: #fff; border-radius: 10px; padding: 16px 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .dash-tile .tile-num { font-size: 34px; font-weight: 800; line-height: 1; }
  .dash-tile .tile-label { font-size: 12px; color: #666; margin-top: 4px; text-transform: uppercase; letter-spacing: 0.5px; }

  /* ACCOUNTING TABLE */
  .accounting-total { background: #1a1a2e; color: #fff; font-weight: 700; }
  .accounting-total td { color: #fff !important; }

  /* MISC */
  .warning-box { background: #fff3cd; border: 1px solid #e6b800; border-radius: 8px; padding: 10px 14px; margin-bottom: 10px; font-size: 13px; color: #856404; }
  .phishing-box { background: #fde8e8; border: 1px solid #c0392b; border-radius: 8px; padding: 10px 14px; margin-bottom: 10px; font-size: 13px; color: #c0392b; }
  .info-box { background: #f0f6ff; border: 1px solid #1a5fa8; border-radius: 8px; padding: 10px 14px; margin-bottom: 10px; font-size: 13px; color: #1a5fa8; }
  .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  @media (max-width: 700px) { .two-col { grid-template-columns: 1fr; } .header-meta { gap: 10px; } }
  .small { font-size: 12px; color: #777; }
  .bold { font-weight: 700; }
  .mt8 { margin-top: 8px; }
  .mb8 { margin-bottom: 8px; }
  ul.detail-list { padding-left: 18px; margin-top: 4px; }
  ul.detail-list li { margin-bottom: 3px; font-size: 13px; }
  .divider { border: none; border-top: 1px solid #e5e7eb; margin: 18px 0; }
  .top3 { background: linear-gradient(135deg, #1a1a2e 0%, #0f3460 100%); border-radius: 12px; padding: 24px 28px; color: #fff; margin-bottom: 28px; }
  .top3 h2 { font-size: 18px; font-weight: 700; margin-bottom: 16px; color: #a8c4e0; text-transform: uppercase; letter-spacing: 1px; }
  .top3-item { display: flex; gap: 14px; margin-bottom: 14px; align-items: flex-start; }
  .top3-num { width: 36px; height: 36px; border-radius: 50%; background: #e6b800; color: #1a1a2e; font-size: 18px; font-weight: 800; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
  .top3-text { font-size: 15px; line-height: 1.5; color: #f0f0f0; }
  .restore { background: #d1fae5; color: #1a7a3c; padding: 2px 8px; border-radius: 8px; font-size: 11px; font-weight: 700; }
  .review  { background: #fff3cd; color: #856404; padding: 2px 8px; border-radius: 8px; font-size: 11px; font-weight: 700; }
  .delete  { background: #fde8e8; color: #c0392b; padding: 2px 8px; border-radius: 8px; font-size: 11px; font-weight: 700; }
  .phish   { background: #fde8e8; color: #9b1c1c; padding: 2px 8px; border-radius: 8px; font-size: 11px; font-weight: 700; }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 1. HEADER -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="header">
  <h1>🌅 Good Morning, Melissa</h1>
  <div class="subtitle">Executive Briefing — Prepared by Your Chief of Staff</div>
  <div class="header-meta">
    <div class="meta-pill">📅 Wednesday, July 15, 2026</div>
    <div class="meta-pill">📧 50 Emails Reviewed</div>
    <div class="meta-pill">📆 14 Calendar Events Reviewed</div>
    <div class="meta-pill">🚨 4 Phishing Emails Auto-Trashed</div>
    <div class="meta-pill">⚠️ NYC Air Quality Advisory Active</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 2. EXECUTIVE SUMMARY -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="exec-summary">
  <h2>📋 Executive Summary</h2>
  <div class="bullet">
    <div class="bullet-icon" style="background:#fde8e8;">🚨</div>
    <div class="bullet-text"><strong>Biggest Risk:</strong> Four phishing / scam emails were auto-trashed today — two spoofed cloud storage account-lock scams, one fake casino deposit, and one fake Ace Hardware giveaway. Additionally, a Notify NYC alert warns of deteriorating air quality from Canadian wildfires affecting NYC today. No action needed on the phishing; monitor the air quality advisory.</div>
  </div>
  <div class="bullet">
    <div class="bullet-icon" style="background:#d1fae5;">💼</div>
    <div class="bullet-text"><strong>Biggest Opportunity:</strong> Active conversation thread with Monte Montoya (VP, AI Partnerships &amp; Growth at Nimble) has an unread reply from this morning that requires your attention. Separately, an Indeed match for VP, HR at Virtual Technologies Group arrived today and LinkedIn is showing a Sr. HR Director role at up to $350K/year. Your LinkedIn profile received 5 views (3 noticed + 2 profile views) — your search is gaining traction.</div>
  </div>
  <div class="bullet">
    <div class="bullet-icon" style="background:#dbeafe;">📅</div>
    <div class="bullet-text"><strong>Biggest Calendar Item:</strong> TODAY — Bone Density / Imaging Appointment at LH Radiology (400 E 66th St) starts at <strong>8:30 AM</strong> — you need to leave soon. You also have the HR Networking &amp; Job Search Group Zoom at 12:00 PM (RSVP still pending) and a 1:1 conversation with Tobin at 4:00 PM via Microsoft Teams. Tomorrow (Thu 7/16) includes Tea with LeiLani at T Shop — already accepted.</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 3. ACTION REQUIRED -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title red">🔴 Action Required</div>

  <div class="card card-red">
    <span class="label label-red">⚠️ URGENT — LEAVE NOW</span>
    <h3>Medical Imaging Appointment — LH Radiology</h3>
    <div class="meta">📅 Today, July 15 @ 8:30 AM | 📍 400 East 66th Street</div>
    <div class="why">Check-in is at 8:30 AM. The confirmation instructs you to complete pre-registration forms before arrival to reduce check-in time. Conflicts with the calendar "Bone density" event at the same time — these appear to be the same appointment.</div>
    <div class="action">→ Leave immediately. Confirm pre-registration is complete.</div>
    <div class="due">⏰ Due: TODAY 8:30 AM</div>
  </div>

  <div class="card card-yellow">
    <span class="label label-yellow">🟡 RSVP NEEDED</span>
    <h3>HR Networking &amp; Job Search Group — Zoom (Session 2)</h3>
    <div class="meta">📅 Today, July 15 @ 12:00 PM–1:30 PM | Status: Needs Action</div>
    <div class="why">You have not yet RSVPed. This is a 150+ person HR networking group — a key job search resource. There is a duplicate "Network" event at the same time that is confirmed — you are likely attending, but RSVP to the Zoom invite.</div>
    <div class="action">→ RSVP "Accept" on the Zoom invite.</div>
    <div class="due">⏰ Due: Before 12:00 PM Today</div>
  </div>

  <div class="card card-yellow">
    <span class="label label-yellow">🟡 RSVP NEEDED</span>
    <h3>HR Networking &amp; Job Search: Open Office Hours — Zoom (Thu 7/16)</h3>
    <div class="meta">📅 Thursday, July 16 @ 12:00 PM–1:00 PM | Status: Needs Action</div>
    <div class="why">Same HR networking group. RSVP is pending. Tomorrow's session is open office hours — valuable for your active job search.</div>
    <div class="action">→ RSVP Accept or Decline by end of day today.</div>
    <div class="due">⏰ Due: Today EOD</div>
  </div>

  <div class="card card-green">
    <span class="label label-green">💼 JOB SEARCH — URGENT READ</span>
    <h3>Unread Reply from Monte Montoya — VP, AI Partnerships &amp; Growth (Nimble)</h3>
    <div class="meta">📧 From: monte.montoya@gmail.com | Received: Tue 7/14 5:48 PM PT</div>
    <div class="why">Monte sent you notes with role options — VP, AI Partnerships &amp; Growth — and referenced Steve's hiring notes. This is an active opportunity in your pipeline requiring a response or decision. You already asked key questions (equity, goals, hiring, compensation) in your last reply.</div>
    <div class="action">→ Read Monte's latest email carefully. Decide which role option to pursue. Follow up with Steve's questions or confirm next steps with Monte.</div>
    <div class="due">⏰ Due: Today</div>
  </div>

  <div class="card card-green">
    <span class="label label-green">💼 JOB SEARCH — REVIEW</span>
    <h3>VP, HR (People) at Virtual Technologies Group — Indeed Match</h3>
    <div class="meta">📧 From: Indeed | Received: Today 8:31 AM</div>
    <div class="why">Indeed flagged this as a strong match for your VP of Human Resources background. Review the full posting and assess fit.</div>
    <div class="action">→ Open email, review posting, apply if strong fit or save for pipeline tracking.</div>
    <div class="due">⏰ Due: Today or Tomorrow</div>
  </div>

  <div class="card card-blue">
    <span class="label label-blue">📅 CALENDAR — PREP NEEDED</span>
    <h3>Convo with Melissa W. — Tobin (TCG Co.)</h3>
    <div class="meta">📅 Today, July 15 @ 4:00–4:30 PM | 📍 Microsoft Teams</div>
    <div class="why">Tobin from TCG Co. has a confirmed Teams meeting with you this afternoon. Unclear context — likely a recruiter or professional contact call. The invite says "If Teams doesn't work, call 516.313.8888."</div>
    <div class="action">→ Review context (is this a recruiter call or networking?), test Teams link before 4:00 PM, have resume/LinkedIn open.</div>
    <div class="due">⏰ Due: Today 4:00 PM</div>
  </div>

  <div class="card card-blue">
    <span class="label label-blue">📅 PREP NEEDED — TOMORROW</span>
    <h3>Tea with LeiLani | Brew At the Table — Thu 7/16</h3>
    <div class="meta">📅 Thursday, July 16 @ 1:00–2:00 PM | 📍 T Shop, 247 Elizabeth St, NY 10012</div>
    <div class="why">Accepted networking event with LeiLani (leilani@bethechangehr.com) and 3 others including Teresa Low. In-person at a tea shop — allow travel time from any morning activities.</div>
    <div class="action">→ Confirm location logistics, allow 30 min travel. Bring business cards / have LinkedIn ready.</div>
    <div class="due">⏰ Due: Tomorrow 1:00 PM</div>
  </div>

  <div class="card card-yellow">
    <span class="label label-yellow">🟡 FINANCIAL — REVIEW</span>
    <h3>Robinhood — Trade Confirmations Available</h3>
    <div class="meta">📧 From: noreply@robinhood.com | Received: Today 4:33 AM</div>
    <div class="why">Recent trade confirmations are ready for review. Standard notification but worth acknowledging for your financial records.</div>
    <div class="action">→ Log into Robinhood, review and save/archive confirmation for records.</div>
    <div class="due">⏰ Due: This week</div>
  </div>

  <div class="card card-yellow">
    <span class="label label-yellow">🟡 LOYALTY — REVIEW</span>
    <h3>Hilton Honors — July Monthly Statement</h3>
    <div class="meta">📧 From: Hilton Honors | Received: Today 3:04 AM</div>
    <div class="why">Monthly statement shows where you've been and points balance. Worth a quick review for any expiring points or upcoming travel planning.</div>
    <div class="action">→ Open, check points balance and any expiration notices.</div>
    <div class="due">⏰ Due: This week</div>
  </div>

  <div class="card card-red">
    <span class="label label-red">⚠️ HEALTH ALERT</span>
    <h3>Notify NYC — Canadian Wildfires Air Quality Advisory (NYC)</h3>
    <div class="meta">📧 From: Notify NYC / Everbridge | Received: Today 1:30 AM</div>
    <div class="why">NYCEM and DOHMH issued an advisory for potentially deteriorating air quality from Canadian wildfires affecting NYC today, July 15. You have an outdoor/transit commute to your radiology appointment this morning.</div>
    <div class="action">→ Check current AQI before leaving for your appointment. Consider wearing a mask outdoors. Monitor updates at nyc.gov/health.</div>
    <div class="due">⏰ Active: Today</div>
  </div>

  <div class="card card-yellow">
    <span class="label label-yellow">🟡 MATCH.COM — PERSONAL</span>
    <h3>Profile View from "Lt" on Match.com</h3>
    <div class="meta">📧 From: Match.com | Received: Today 12:13 AM</div>
    <div class="why">Lt, 68, Marlboro, NJ viewed your profile. Low urgency but flagged for awareness.</div>
    <div class="action">→ Review at your leisure if interested. No time-sensitive action needed.</div>
    <div class="due">⏰ No deadline</div>
  </div>

  <div class="card card-green">
    <span class="label label-green">💼 JOB APPS — REVIEW SAVED LINKS</span>
    <h3>Two Job Links Sent to Yourself (Trash — Review Before Deleting)</h3>
    <div class="meta">📧 From: melissaw212 to self | Received: Tue 7/14 (now in Trash)</div>
    <div class="why">You emailed yourself links to (1) Beam Living careers job and (2) Accurate Background Principal HRBP role — these are likely jobs you wanted to track. They were filed in trash and may need to be captured before deletion.</div>
    <div class="action">→ Open both links, assess fit, add to your job tracker before trashing the emails.</div>
    <div class="due">⏰ Due: Today</div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 4. FULL 7-DAY CALENDAR -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title blue">📆 Full 7-Day Calendar (July 15–21, 2026)</div>

  <!-- WEDNESDAY JULY 15 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Wednesday, July 15, 2026 <span class="today-badge">TODAY</span></div>

    <div class="cal-event" style="background:#fff8f0;">
      <div class="cal-event-time">8:30 AM – 9:05 AM</div>
      <div class="cal-event-name">🏥 IMAGING APPOINTMENT: LH Radiology</div>
      <div class="cal-event-detail">📍 400 East 66th Street | <span class="rsvp-confirmed">✅ Confirmed</span></div>
      <div class="cal-event-detail">Bone density exam. Check-in at 8:30 AM. Complete pre-registration forms before arrival.</div>
      <div class="cal-event-conflict">⚠️ CONFLICT: "Bone Density" event also at 8:30–9:30 AM — same appointment, duplicate entries. No real conflict.</div>
      <div class="cal-event-detail" style="color:#c0392b; font-weight:600;">⚠️ Air Quality Advisory active — check AQI before leaving.</div>
    </div>

    <div class="cal-event" style="background:#fffdf0;">
      <div class="cal-event-time">8:30 AM – 9:30 AM</div>
      <div class="cal-event-name">🦴 Bone Density (Duplicate Calendar Entry)</div>
      <div class="cal-event-detail"><span class="rsvp-confirmed">✅ Confirmed</span> | Same as LH Radiology appointment above.</div>
    </div>

    <div class="cal-event" style="background:#f0fff4;">
      <div class="cal-event-time">12:00 PM – 1:30 PM</div>
      <div class="cal-event-name">🤝 HR Networking &amp; Job Search Group — Zoom Session 2</div>
      <div class="cal-event-detail">🔗 <a href="https://us06web.zoom.us/j/81954171722" style="color:#1a5fa8;">Zoom Link</a> | <span class="rsvp-needs">⚠️ RSVP: Needs Action</span></div>
      <div class="cal-event-detail">150+ HR professionals. Large group networking session.</div>
      <div class="cal-event-detail" style="color:#b8860b; font-weight:600;">→ RSVP before noon. Test Zoom link in advance.</div>
    </div>

    <div class="cal-event" style="background:#f0f6ff;">
      <div class="cal-event-time">12:00 PM – 1:30 PM</div>
      <div class="cal-event-name">🤝 Network (Personal Reminder Block)</div>
      <div class="cal-event-detail"><span class="rsvp-confirmed">✅ Confirmed</span> | Overlaps with Zoom session above — same time block, personal reminder.</div>
    </div>

    <div class="cal-event" style="background:#f0f6ff;">
      <div class="cal-event-time">4:00 PM – 4:30 PM</div>
      <div class="cal-event-name">💼 Convo with Melissa W. — Tobin (TCG Co.)</div>
      <div class="cal-event-detail">📍 Microsoft Teams | <span class="rsvp-accepted">✅ Accepted</span></div>
      <div class="cal-event-detail">Backup: Call Tobin at 516.313.8888 if Teams doesn't work.</div>
      <div class="cal-event-detail" style="color:#1a5fa8; font-weight:600;">→ Prep: Have resume/LinkedIn open. Test Teams link by 3:45 PM.</div>
    </div>
  </div>

  <!-- THURSDAY JULY 16 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Thursday, July 16, 2026</div>

    <div class="cal-event" style="background:#fde8e8;">
      <div class="cal-event-time">9:00 AM – 10:30 AM</div>
      <div class="cal-event-name">🚫 Executive Roundtable (John Madigan — Zoom)</div>
      <div class="cal-event-detail">🔗 Zoom | <span class="rsvp-declined">❌ Declined</span></div>
      <div class="cal-event-detail">You have declined this event. No action needed. Note for reference only.</div>
    </div>

    <div class="cal-event" style="background:#f0fff4;">
      <div class="cal-event-time">12:00 PM – 1:00 PM</div>
      <div class="cal-event-name">🤝 HR Networking &amp; Job Search: Open Office Hours — Zoom Session 2</div>
      <div class="cal-event-detail">🔗 <a href="https://us06web.zoom.us/j/85945371140" style="color:#1a5fa8;">Zoom Link</a> | <span class="rsvp-needs">⚠️ RSVP: Needs Action</span></div>
      <div class="cal-event-detail">Open discussion; no AI note-taking tools per organizer request.</div>
      <div class="cal-event-detail" style="color:#b8860b; font-weight:600;">→ RSVP by today EOD. No recording — come prepared with questions/topics.</div>
    </div>

    <div class="cal-event" style="background:#f0fff4;">
      <div class="cal-event-time">1:00 PM – 2:00 PM</div>
      <div class="cal-event-name">🍵 Tea with LeiLani | Brew At the Table</div>
      <div class="cal-event-detail">📍 T Shop, 247 Elizabeth St, New York, NY 10012 | <span class="rsvp-accepted">✅ Accepted</span></div>
      <div class="cal-event-detail">With: LeiLani (Be The Change HR), Teresa Low, Leyla Snovini, Jessi (Alvi Solutions)</div>
      <div class="cal-event-detail" style="color:#1a7a3c; font-weight:600;">→ In-person networking. Allow 30 min transit. Bring business cards.</div>
    </div>
  </div>

  <!-- FRIDAY JULY 17 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Friday, July 17, 2026</div>

    <div class="cal-event" style="background:#fff8f0;">
      <div class="cal-event-time">10:10 AM – 10:25 AM</div>
      <div class="cal-event-name">🧪 Quest Diagnostics Appointment</div>
      <div class="cal-event-detail">📍 65 E 76th St, Professional Apt GR-G, New York, NY 10021 | <span class="rsvp-confirmed">✅ Confirmed</span></div>
      <div class="cal-event-detail">Confirmation #: FOUGZX | Activity: All Other Tests</div>
      <div class="cal-event-detail" style="color:#b85c00; font-weight:600;">→ Short appointment (15 min). Arrive a few minutes early. Fast if required.</div>
    </div>

    <div class="cal-event" style="background:#fff8f0;">
      <div class="cal-event-time">3:00 PM – 4:00 PM</div>
      <div class="cal-event-name">🩺 Dr. Yuen Appointment</div>
      <div class="cal-event-detail"><span class="rsvp-confirmed">✅ Confirmed</span> | Location not specified.</div>
      <div class="cal-event-detail" style="color:#b85c00; font-weight:600;">→ Confirm location/address and any prep instructions (labs results from morning may be relevant).</div>
    </div>
  </div>

  <!-- SATURDAY JULY 18 / SUNDAY JULY 19 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Saturday, July 18 &amp; Sunday, July 19, 2026</div>
    <div class="cal-event">
      <div class="cal-event-name" style="color:#888;">No events scheduled. Rest &amp; recharge.</div>
    </div>
  </div>

  <!-- MONDAY JULY 20 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Monday, July 20, 2026</div>

    <div class="cal-event" style="background:#fff8f0;">
      <div class="cal-event-time">1:45 PM – 2:45 PM</div>
      <div class="cal-event-name">🏃 PT (Physical Therapy) — Duplicate Entry</div>
      <div class="cal-event-detail"><span class="rsvp-confirmed">✅ Confirmed</span> | Location not specified. Same event appears twice on calendar.</div>
      <div class="cal-event-detail" style="color:#b85c00; font-weight:600;">→ Confirm location. Delete duplicate calendar entry to avoid confusion.</div>
    </div>
  </div>

  <!-- TUESDAY JULY 21 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Tuesday, July 21, 2026</div>

    <div class="cal-event" style="background:#faf0ff;">
      <div class="cal-event-time">All Day</div>
      <div class="cal-event-name">🎂 Eric Dordick's Birthday</div>
      <div class="cal-event-detail"><span class="rsvp-confirmed">✅ Confirmed</span></div>
      <div class="cal-event-detail" style="color:#6b2fa0; font-weight:600;">→ Send a birthday message or card if you have a relationship with Eric.</div>
    </div>

    <div class="cal-event" style="background:#f0f6ff;">
      <div class="cal-event-time">10:00 AM – 11:00 AM</div>
      <div class="cal-event-name">👤 Umi</div>
      <div class="cal-event-detail"><span class="rsvp-confirmed">✅ Confirmed</span> | No location specified.</div>
      <div class="cal-event-detail" style="color:#1a5fa8; font-weight:600;">→ Confirm location/format (in-person vs. call). Prep conversation agenda if relevant to job search.</div>
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 5. JOB SEARCH & INTERVIEW PIPELINE -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title green">💼 Job Search &amp; Interview Pipeline</div>

  <table>
    <thead>
      <tr>
        <th>Fit</th>
        <th>Role / Source</th>
        <th>Compensation</th>
        <th>Status</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="tag-fit-high">HIGH</span></td>
        <td><strong>VP, AI Partnerships &amp; Growth — Nimble</strong><br><span class="small">Monte Montoya thread | Gmail</span></td>
        <td>TBD (equity + salary TBD)</td>
        <td>Active conversation — unread reply from Monte with role options</td>
        <td>Read email, respond today. Key: equity, goals, comp, scope.</td>
      </tr>
      <tr>
        <td><span class="tag-fit-high">HIGH</span></td>
        <td><strong>VP, HR (People) — Virtual Technologies Group</strong><br><span class="small">Indeed | Today 8:31 AM</span></td>
        <td>Not specified</td>
        <td>New match — unread</td>
        <td>Review posting today. Apply if strong fit.</td>
      </tr>
      <tr>
        <td><span class="tag-fit-high">HIGH</span></td>
        <td><strong>Sr. Human Resources Director — Confidential</strong><br><span class="small">LinkedIn Job Alerts | Two alerts (7/12 &amp; 7/13 postings)</span></td>
        <td>Up to $350K/year</td>
        <td>Alerted twice — unread</td>
        <td>Review posting immediately. High comp — likely worth pursuing.</td>
      </tr>
      <tr>
        <td><span class="tag-fit-high">HIGH</span></td>
        <td><strong>Head of People, North America — Artefact</strong><br><span class="small">LinkedIn Job Alerts | Today 3:05 AM</span></td>
        <td>Not specified</td>
        <td>New alert — unread</td>
        <td>Review today. North America Head of People at a data/AI consultancy — strong fit signal.</td>
      </tr>
      <tr>
        <td><span class="tag-fit-high">HIGH</span></td>
        <td><strong>Head of People — Mars Men (Outbound Application)</strong><br><span class="small">Sent by Melissa to Benjamin | Tue 7/14</span></td>
        <td>Not specified</td>
        <td>Application sent — awaiting reply</td>
        <td>Follow up in 3–5 business days if no response. Note: company hit $100M in 18 months.</td>
      </tr>
      <tr>
        <td><span class="tag-fit-med">MED</span></td>
        <td><strong>Senior HR Business Partner — Goodman Masson</strong><br><span class="small">LinkedIn + Indeed | Multiple alerts</span></td>
        <td>Up to $200K/year</td>
        <td>Alerted multiple times — some read, some in trash</td>
        <td>Decide: interested or not? Clear from alerts if not pursuing.</td>
      </tr>
      <tr>
        <td><span class="tag-fit-med">MED</span></td>
        <td><strong>Senior People Partner, GTM — Rokt</strong><br><span class="small">LinkedIn Job Alerts | Wed 7/15 1:05 AM (Trash)</span></td>
        <td>Up to $235K/year</td>
        <td>In trash — may be unreviewed</td>
        <td>Restore from trash if interested in GTM-aligned people role.</td>
      </tr>
      <tr>
        <td><span class="tag-fit-med">MED</span></td>
        <td><strong>Principal HRBP — Accurate Background (Remote)</strong><br><span class="small">Self-forwarded link | Tue 7/14 (Trash)</span></td>
        <td>Not specified</td>
        <td>Link saved to self — in trash</td>
        <td>Open link before deleting. Assess fit.</td>
      </tr>
      <tr>
        <td><span class="tag-fit-med">MED</span></td>
        <td><strong>Head of People (unspecified) — Beam Living</strong><br><span class="small">Self-forwarded link | Tue 7/14 (Trash)</span></td>
        <td>Not specified</td>
        <td>Link saved to self — in trash</td>
        <td>Open Beam Living careers link before deleting.</td>
      </tr>
      <tr>
        <td><span class="tag-fit-med">MED</span></td>
        <td><strong>Community Manager – Wellness — Jetzy + 6 more NY roles</strong><br><span class="small">Glassdoor | Wed 7/15 1:02 AM (Trash)</span></td>
        <td>Not specified</td>
        <td>In trash</td>
        <td>Wellness/community roles may not align with VP-level search — review briefly, delete if not relevant.</td>
      </tr>
      <tr>
        <td><span class="tag-fit-low">LOW</span></td>
        <td><strong>New Jobs in Remote, US — Multiple (incl. Stanford)</strong><br><span class="small">Glassdoor | Wed 7/15 12:26 AM (Trash)</span></td>
        <td>Varies</td>
        <td>In trash</td>
        <td>Delete — broad/generic alert. Stanford may be worth a quick scan.</td>
      </tr>
      <tr>
        <td><span class="tag-fit-low">LOW</span></td>
        <td><strong>28 New HR Jobs — SHRM HR Jobs</strong><br><span class="small">SHRM | Today 3:24 AM</span></td>
        <td>Varies</td>
        <td>Unread — not in inbox, not in trash</td>
        <td>Scan for relevant senior roles. Not inbox-priority.</td>
      </tr>
      <tr>
        <td><span class="tag-fit-low">LOW</span></td>
        <td><strong>Citizens Careers — Staff Accountant + Others</strong><br><span class="small">Citizens Careers | Today 6:19 AM</span></td>
        <td>Varies</td>
        <td>Unread — inbox</td>
        <td>Likely not relevant to VP-level HR search. Scan briefly, delete.</td>
      </tr>
    </tbody>
  </table>

  <div class="info-box mt8">
    <strong>LinkedIn Profile Visibility:</strong> 5 people noticed you / viewed your profile in the past 24 hours (2 profile views + 3 "noticed you" notifications). Your search is gaining traction — keep your profile active and updated.
  </div>

  <div class="card card-green mt8">
    <span class="label label-green">🤝 NETWORKING MEETINGS THIS WEEK</span>
    <h3>Upcoming Networking Events</h3>
    <ul class="detail-list">
      <li><strong>Today 12:00 PM:</strong> HR Networking &amp; Job Search Group Zoom — 150+ HR pros (RSVP needed)</li>
      <li><strong>Thu 7/16 12:00 PM:</strong> HR Open Office Hours Zoom — open discussion (RSVP needed)</li>
      <li><strong>Thu 7/16 1:00 PM:</strong> Tea with LeiLani at T Shop — accepted, in-person</li>
      <li><strong>Today 4:00 PM:</strong> Convo with Tobin (TCG Co.) — Teams call</li>
      <li><strong>Tue 7/21 10:00 AM:</strong> Umi — confirmed, context TBD</li>
    </ul>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 6. FULL EMAIL REVIEW BY CATEGORY -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title gray">📂 Full Email Review by Category</div>

  <!-- SECURITY / RISK -->
  <div class="card card-red">
    <span class="label label-red">🔴 SECURITY / RISK</span>
    <h3>Security &amp; Phishing — 5 Emails</h3>
    <div class="meta">Including 4 auto-trashed phishing emails + 1 legitimate advisory</div>
    <table style="margin-top:10px;">
      <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>Notify NYC (Everbridge)</td>
          <td>Canadian Wildfires Air Quality — 7/15 (NYC)</td>
          <td><span class="tag-medium">⚠️ LEGITIMATE</span></td>
          <td>Read &amp; monitor AQI today</td>
        </tr>
        <tr style="background:#fde8e8;">
          <td>"Payment_Declined©" (gibberish domain)</td>
          <td>We've Blocked Your Account! Photos/videos deleted Wed 15 Jul</td>
          <td><span class="phish">🚫 AUTO-TRASHED</span></td>
          <td>Spoofed cloud service, Unicode lookalike name, credential harvest. No action.</td>
        </tr>
        <tr style="background:#fde8e8;">
          <td>melissaw212 (gibberish domain)</td>
          <td>You received a direct deposited of $13963.99 — Limitless Casino</td>
          <td><span class="phish">🚫 AUTO-TRASHED</span></td>
          <td>Fake casino deposit scam from spoofed sender. Unrendered template vars. No action.</td>
        </tr>
        <tr style="background:#fde8e8;">
          <td>melissaw212 (gibberish domain)</td>
          <td>Your Cloud ID has been locked — photos/videos will be removed</td>
          <td><span class="phish">🚫 AUTO-TRASHED</span></td>
          <td>Near-identical repeat of cloud lockout phish. No action.</td>
        </tr>
        <tr style="background:#fde8e8;">
          <td>Ace Hardware Giveaway (quixotically.biz)</td>
          <td>Ace Hardware Rewards You with a YETI PATRIOTIC Bundle</td>
          <td><span class="phish">🚫 AUTO-TRASHED</span></td>
          <td>Fake survey/prize scam to harvest personal info. No action.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- JOB SEARCH -->
  <div class="card card-green">
    <span class="label label-green">💼 JOB SEARCH</span>
    <h3>Job Search Emails — 10 Emails</h3>
    <table style="margin-top:10px;">
      <thead><tr><th>Sender</th><th>Subject</th><th>Fit</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>Indeed</td><td>VP, HR (People) @ Virtual Technologies Group</td><td><span class="tag-fit-high">HIGH</span></td><td>Review &amp; apply today</td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>Sr HR Director at Confidential: up to $350K/year (x2 alerts)</td><td><span class="tag-fit-high">HIGH</span></td><td>Review immediately</td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>Head of People, North America at Artefact</td><td><span class="tag-fit-high">HIGH</span></td><td>Review today</td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>Senior HR Business Partner at Goodman Masson: up to $200K (in trash)</td><td><span class="tag-fit-med">MED</span></td><td>Decide — interested or clear alerts</td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>Senior People Partner, GTM at Rokt: up to $235K (in trash)</td><td><span class="tag-fit-med">MED</span></td><td>Restore from trash if interested</td></tr>
        <tr><td>LinkedIn (messages)</td><td>Jobs similar to Senior HR Business Partner at Goodman Masson</td><td><span class="tag-fit-med">MED</span></td><td>Scan for relevant roles</td></tr>
        <tr><td>SHRM HR Jobs</td><td>28 New Human Resources Jobs</td><td><span class="tag-fit-low">LOW</span></td><td>Quick scan, delete</td></tr>
        <tr><td>Citizens Careers</td><td>New jobs for you!</td><td><span class="tag-fit-low">LOW</span></td><td>Scan, likely delete</td></tr>
        <tr><td>Glassdoor</td><td>Community Manager – Wellness at Jetzy + 6 more NY roles (trash)</td><td><span class="tag-fit-low">LOW</span></td><td>Delete if not relevant</td></tr>
        <tr><td>Glassdoor</td><td>New jobs in Remote, US (trash)</td><td><span class="tag-fit-low">LOW</span></td><td>Delete</td></tr>
      </tbody>
    </table>
  </div>

  <!-- RECRUITERS / NETWORKING -->
  <div class="card card-green">
    <span class="label label-green">🤝 RECRUITERS / NETWORKING</span>
    <h3>Recruiter &amp; Networking Emails — 4 Emails</h3>
    <table style="margin-top:10px;">
      <thead><tr><th>Sender</th><th>Subject / Context</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>Monte Montoya (monte.montoya@gmail.com)</td><td>RE: Role options — VP AI Partnerships &amp; Growth at Nimble. Unread latest reply with Steve's notes.</td><td>Read &amp; respond today — HIGH PRIORITY</td></tr>
        <tr><td>Melissa (self-sent)</td><td>Head of People who builds — outbound application to Benjamin at Mars Men</td><td>Awaiting reply. Follow up in 3–5 days.</td></tr>
        <tr><td>LinkedIn</td><td>2 people viewed your profile</td><td>Check who — may be recruiters. Review profiles.</td></tr>
        <tr><td>LinkedIn</td><td>3 people noticed you (in trash)</td><td>Restore if worth reviewing — profile visibility signal.</td></tr>
      </tbody>
    </table>
  </div>

  <!-- CALENDAR / EVENTS -->
  <div class="card card-blue">
    <span class="label label-blue">📅 CALENDAR / EVENTS</span>
    <h3>Calendar &amp; Event Emails — 2 Emails</h3>
    <table style="margin-top:10px;">
      <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>AllEvents</td><td>Events for Melissa, new recommendations</td><td>Review for relevant networking or professional events. Low urgency.</td></tr>
        <tr><td>Work It DAILY Newsletter (trash)</td><td>▶️ Press PLAY On Life! — don't do these 4 things on LinkedIn as job seeker</td><td>Mildly relevant to job search. Review if time permits; otherwise delete.</td></tr>
      </tbody>
    </table>
  </div>

  <!-- MEDICAL / HEALTH -->
  <div class="card card-orange">
    <span class="label label-orange">🏥 MEDICAL / HEALTH</span>
    <h3>Medical / Health Emails — 2 Emails</h3>
    <table style="margin-top:10px;">
      <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>Alison Courses</td><td>Do you know what ADHD really looks like? 🤔</td><td>Educational course alert. Review if interested in ADHD topic; otherwise unsubscribe.</td></tr>
        <tr><td>Notify NYC (also in Security)</td><td>Air Quality Advisory — counted in Security/Risk</td><td>Counted above.</td></tr>
      </tbody>
    </table>
    <div class="small mt8">Note: Alison ADHD course email is the sole pure "Medical/Health" inbox email. The Notify NYC advisory is cross-listed under Security/Risk (counted there).</div>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="card card-yellow">
    <span class="label label-yellow">💰 FINANCIAL / BILLING</span>
    <h3>Financial / Billing Emails — 2 Emails</h3>
    <table style="margin-top:10px;">
      <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>Robinhood (noreply@robinhood.com)</td><td>Your trade confirmations are available</td><td>Log in &amp; review trade confirmations. Archive for records.</td></tr>
        <tr><td>Hilton Honors</td><td>Your July Hilton Honors Monthly Statement</td><td>Review points balance, check for expiring rewards.</td></tr>
      </tbody>
    </table>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="card card-purple">
    <span class="label label-purple">📚 PROFESSIONAL DEVELOPMENT</span>
    <h3>Professional Development Emails — 3 Emails</h3>
    <table style="margin-top:10px;">
      <thead><tr><th>Sender</th><th>Subject</th><th>Recommendation</th></tr></thead>
      <tbody>
        <tr><td>CoolDeep AI (in trash)</td><td>Finally...Claude skills can fix your average results</td><td>In trash. Low value AI newsletter. Delete.</td></tr>
        <tr><td>Pranit Naik via Medium</td><td>Fable 5 vs ChatGPT 5.6: Which AI Model Should You Use?</td><td>Potentially relevant given AI roles in pipeline. Review if time permits.</td></tr>
        <tr><td>Claude Team</td><td>Reminder: Share your 3 Claude Code guest passes (earn $10 credits)</td><td>Referral offer — forward to 3 contacts if you use Claude Code. Low urgency.</td></tr>
      </tbody>
    </table>
  </div>

  <!-- PERSONAL -->
  <div class="card card-purple">
    <span class="label label-purple" style="background:#fce4d6; color:#b85c00;">👤 PERSONAL</span>
    <h3>Personal Emails — 5 Emails</h3>
    <table style="margin-top:10px;">
      <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>Match.com</td><td>You've had a profile view from Lt (68, Marlboro NJ)</td><td>Review at leisure. Return the favor if interested.</td></tr>
        <tr><td>Netflix</td><td>Mel, we just added a movie you might like</td><td>Entertainment. Review when time permits.</td></tr>
        <tr><td>Melissa W (self)</td><td>[no subject] — Beam Living careers link (trash)</td><td>Save link before deleting.</td></tr>
        <tr><td>Melissa W (self)</td><td>[no subject] — Accurate Background HRBP link (trash)</td><td>Save link before deleting.</td></tr>
        <tr><td>LinkedIn (Dennis notification)</td><td>Dennis, add Ogwuru Rosemary — Biomedical Equipment Tech</td><td>Appears to be someone else's LinkedIn notification. Ignore / delete.</td></tr>
      </tbody>
    </table>
  </div>

  <!-- NEWSLETTERS / SUBSCRIPTIONS -->
  <div class="card card-purple">
    <span class="label label-purple">📰 NEWSLETTERS / SUBSCRIPTIONS</span>
    <h3>Newsletters &amp; Subscriptions — 5 Emails</h3>
    <table style="margin-top:10px;">
      <thead><tr><th>Sender</th><th>Subject</th><th>Location</th><th>Recommendation</th></tr></thead>
      <tbody>
        <tr><td>The Daily Skimm (trash)</td><td>Stick to fridge cigs — home smell tips</td><td>Trash</td><td>Delete. Trash already. Unsubscribe if unwanted.</td></tr>
        <tr><td>Melissa Westgate / Midlife Trailblazer (trash)</td><td>My Life Began the Day I Lost 1 Million Dollars</td><td>Trash</td><td>Delete. Personal finance Substack. Unsubscribe if not actively following.</td></tr>
        <tr><td>Work It Daily Newsletter (trash)</td><td>▶️ Press PLAY On Life! — LinkedIn job seeker tips</td><td>Trash</td><td>Mildly relevant. Review tips briefly; unsubscribe if not useful.</td></tr>
        <tr><td>Pranit Naik / Medium</td><td>Fable 5 vs ChatGPT 5.6 AI Comparison</td><td>Inbox</td><td>Keep/Review — relevant to AI-focused job search.</td></tr>
        <tr><td>AllEvents</td><td>Events for Melissa, new recommendations</td><td>Inbox</td><td>Review for networking events. Consider unsubscribing if not useful.</td></tr>
      </tbody>
    </table>
  </div>

  <!-- PROMOTIONAL / RETAIL -->
  <div class="card card-gray
