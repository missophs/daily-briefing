<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa — July 17, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .container { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* Header */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 16px; padding: 36px 40px 28px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 15px; color: #a8b8d8; margin-top: 6px; }
  .header .meta { display: flex; gap: 32px; margin-top: 20px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.08); border-radius: 10px; padding: 10px 18px; text-align: center; }
  .header .meta-item .num { font-size: 24px; font-weight: 700; color: #e0e8ff; }
  .header .meta-item .lbl { font-size: 11px; color: #a8b8d8; text-transform: uppercase; letter-spacing: 1px; }

  /* Section headers */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; padding: 10px 16px; border-radius: 8px 8px 0 0; color: #fff; margin-bottom: 0; }
  .section-body { background: #fff; border-radius: 0 0 12px 12px; padding: 20px; box-shadow: 0 2px 12px rgba(0,0,0,0.07); }

  /* Color themes */
  .red    { background: #c0392b; }
  .yellow { background: #d48c00; }
  .blue   { background: #1565c0; }
  .green  { background: #2e7d32; }
  .purple { background: #6a1b9a; }
  .gray   { background: #5c6370; }
  .teal   { background: #00695c; }
  .navy   { background: #1a237e; }
  .orange { background: #e65100; }

  /* Executive Summary */
  .exec-bullets { list-style: none; }
  .exec-bullets li { padding: 12px 16px; margin-bottom: 10px; border-radius: 8px; font-size: 14px; border-left: 5px solid; }
  .exec-bullets li.risk   { background: #fdecea; border-color: #c0392b; }
  .exec-bullets li.opp    { background: #e8f5e9; border-color: #2e7d32; }
  .exec-bullets li.cal    { background: #e3f2fd; border-color: #1565c0; }
  .exec-bullets li strong { font-weight: 700; }

  /* Action cards */
  .action-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; }
  .action-card { border-radius: 10px; padding: 16px; border-left: 5px solid; }
  .action-card.red    { background: #fdecea; border-color: #c0392b; }
  .action-card.yellow { background: #fff8e1; border-color: #d4ac00; }
  .action-card.green  { background: #e8f5e9; border-color: #2e7d32; }
  .action-card.blue   { background: #e3f2fd; border-color: #1565c0; }
  .action-card.purple { background: #f3e5f5; border-color: #6a1b9a; }
  .action-card .card-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
  .action-card.red .card-label    { color: #c0392b; }
  .action-card.yellow .card-label { color: #b8860b; }
  .action-card.green .card-label  { color: #2e7d32; }
  .action-card.blue .card-label   { color: #1565c0; }
  .action-card.purple .card-label { color: #6a1b9a; }
  .action-card h4 { font-size: 14px; font-weight: 700; margin-bottom: 8px; }
  .action-card .card-row { font-size: 12px; margin-bottom: 4px; }
  .action-card .card-row span { font-weight: 600; }
  .action-card .next-step { margin-top: 10px; padding: 8px 10px; background: rgba(0,0,0,0.05); border-radius: 6px; font-size: 12px; }

  /* Calendar */
  .cal-day { margin-bottom: 16px; }
  .cal-day-header { background: #1565c0; color: #fff; padding: 8px 14px; border-radius: 8px 8px 0 0; font-weight: 700; font-size: 13px; }
  .cal-day-header.today-hdr { background: #0d47a1; }
  .cal-event { display: grid; grid-template-columns: 110px 1fr; gap: 10px; padding: 12px 14px; border-bottom: 1px solid #e8eaf0; background: #fff; font-size: 13px; }
  .cal-event:last-child { border-bottom: none; border-radius: 0 0 8px 8px; }
  .cal-time { font-weight: 700; color: #1565c0; white-space: nowrap; }
  .cal-name { font-weight: 600; }
  .cal-meta { font-size: 11px; color: #555; margin-top: 3px; }
  .badge { display: inline-block; font-size: 10px; padding: 2px 7px; border-radius: 20px; font-weight: 700; margin-left: 6px; vertical-align: middle; }
  .badge.confirmed  { background: #e8f5e9; color: #2e7d32; }
  .badge.needsAction{ background: #fff8e1; color: #b8860b; }
  .badge.declined   { background: #fdecea; color: #c0392b; }
  .badge.allday     { background: #e3f2fd; color: #1565c0; }
  .badge.warning    { background: #fff3e0; color: #e65100; }
  .badge.birthday   { background: #f3e5f5; color: #6a1b9a; }
  .badge.bill       { background: #fce4ec; color: #ad1457; }

  /* Tables */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #f0f2f5; font-weight: 700; padding: 9px 12px; text-align: left; border-bottom: 2px solid #dde1e8; }
  td { padding: 9px 12px; border-bottom: 1px solid #eeeff3; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f9fafb; }
  .priority-high   { color: #c0392b; font-weight: 700; }
  .priority-medium { color: #d4ac00; font-weight: 700; }
  .priority-low    { color: #2e7d32; font-weight: 700; }
  .fit-high   { display:inline-block; background:#e8f5e9; color:#2e7d32; border-radius:4px; padding:1px 7px; font-size:11px; font-weight:700; }
  .fit-medium { display:inline-block; background:#fff8e1; color:#b8860b; border-radius:4px; padding:1px 7px; font-size:11px; font-weight:700; }
  .fit-low    { display:inline-block; background:#fdecea; color:#c0392b; border-radius:4px; padding:1px 7px; font-size:11px; font-weight:700; }

  /* Email category cards */
  .email-cat { border-radius: 10px; margin-bottom: 14px; overflow: hidden; }
  .email-cat-hdr { display: flex; align-items: center; gap: 10px; padding: 10px 16px; color: #fff; font-weight: 700; font-size: 13px; }
  .email-cat-hdr .cnt { background: rgba(255,255,255,0.25); border-radius: 20px; padding: 2px 10px; font-size: 12px; }
  .email-cat-body { background: #fff; padding: 14px 16px; border: 1px solid #e0e0e0; border-top: none; border-radius: 0 0 10px 10px; }
  .email-item { padding: 7px 0; border-bottom: 1px solid #f0f0f0; font-size: 12px; }
  .email-item:last-child { border-bottom: none; }
  .email-item .sender { font-weight: 600; color: #1a1a2e; }
  .email-item .subj { color: #444; }
  .email-item .note { color: #888; font-style: italic; margin-top: 2px; }
  .trash-group { margin-bottom: 12px; }
  .trash-group h4 { font-size: 13px; font-weight: 700; padding: 6px 10px; border-radius: 6px; margin-bottom: 6px; }
  .restore-hdr  { background: #e8f5e9; color: #2e7d32; }
  .review-hdr   { background: #fff8e1; color: #b8860b; }
  .delete-hdr   { background: #fdecea; color: #c0392b; }
  .phish-hdr    { background: #4a0000; color: #ffcccc; }

  /* Dashboard */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 14px; }
  .dash-card { border-radius: 10px; padding: 16px; text-align: center; }
  .dash-card .dash-num { font-size: 32px; font-weight: 800; }
  .dash-card .dash-lbl { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; margin-top: 4px; }
  .dash-card.red-d    { background: #fdecea; color: #c0392b; }
  .dash-card.yellow-d { background: #fff8e1; color: #b8860b; }
  .dash-card.green-d  { background: #e8f5e9; color: #2e7d32; }
  .dash-card.blue-d   { background: #e3f2fd; color: #1565c0; }
  .dash-card.purple-d { background: #f3e5f5; color: #6a1b9a; }
  .dash-card.gray-d   { background: #f5f5f5; color: #5c6370; }

  /* Pill tags */
  .pill { display: inline-block; font-size: 10px; padding: 2px 8px; border-radius: 12px; font-weight: 600; margin: 2px; }
  .pill.red    { background: #fdecea; color: #c0392b; border: 1px solid #f5c6c6; }
  .pill.yellow { background: #fff8e1; color: #b8860b; border: 1px solid #ffe082; }
  .pill.green  { background: #e8f5e9; color: #2e7d32; border: 1px solid #a5d6a7; }
  .pill.gray   { background: #f5f5f5; color: #5c6370; border: 1px solid #ccc; }
  .pill.blue   { background: #e3f2fd; color: #1565c0; border: 1px solid #90caf9; }
  .pill.purple { background: #f3e5f5; color: #6a1b9a; border: 1px solid #ce93d8; }

  .divider { border: none; border-top: 2px solid #e0e4ea; margin: 28px 0; }
  .top3 { background: linear-gradient(135deg, #1a237e, #283593); color: #fff; border-radius: 14px; padding: 28px 32px; margin-top: 10px; }
  .top3 h2 { font-size: 18px; font-weight: 700; margin-bottom: 18px; letter-spacing: 0.5px; }
  .top3-item { display: flex; gap: 14px; margin-bottom: 14px; align-items: flex-start; }
  .top3-num { background: rgba(255,255,255,0.2); border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 16px; flex-shrink: 0; }
  .top3-text { font-size: 14px; color: #e8eeff; }
  .top3-text strong { color: #fff; }

  .warning-box { background: #fff3e0; border-left: 4px solid #e65100; border-radius: 6px; padding: 10px 14px; margin: 10px 0; font-size: 12px; color: #bf360c; }
  .info-box { background: #e3f2fd; border-left: 4px solid #1565c0; border-radius: 6px; padding: 10px 14px; margin: 10px 0; font-size: 12px; color: #0d47a1; }
  .success-box { background: #e8f5e9; border-left: 4px solid #2e7d32; border-radius: 6px; padding: 10px 14px; margin: 10px 0; font-size: 12px; color: #1b5e20; }

  .acct-total { background: #1a1a2e; color: #fff; border-radius: 8px; padding: 12px 18px; font-size: 15px; font-weight: 700; margin-top: 14px; text-align: center; }
  .acct-note { font-size: 11px; color: #aaa; margin-top: 4px; text-align: center; }

  @media (max-width: 600px) {
    .action-grid { grid-template-columns: 1fr; }
    .dash-grid   { grid-template-columns: 1fr 1fr; }
    .cal-event   { grid-template-columns: 90px 1fr; }
    .header .meta { gap: 12px; }
  }
</style>
</head>
<body>
<div class="container">

<!-- ═══════════════════════════════════════════════════════════════
     1. HEADER
════════════════════════════════════════════════════════════════ -->
<div class="header">
  <div class="subtitle">EXECUTIVE BRIEFING &nbsp;·&nbsp; PREPARED BY YOUR CHIEF OF STAFF</div>
  <h1>☀️ Good Morning, Melissa</h1>
  <div class="subtitle">Friday, July 17, 2026 &nbsp;·&nbsp; New York, NY</div>
  <div class="meta">
    <div class="meta-item"><div class="num">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="meta-item"><div class="num">12</div><div class="lbl">Calendar Events</div></div>
    <div class="meta-item"><div class="num">2</div><div class="lbl">Appointments Today</div></div>
    <div class="meta-item"><div class="num">9</div><div class="lbl">Auto-Blocked Phishing</div></div>
    <div class="meta-item"><div class="num">4</div><div class="lbl">RSVP Needed</div></div>
    <div class="meta-item"><div class="num">5</div><div class="lbl">Active Job Leads</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     2. EXECUTIVE SUMMARY
════════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title red">📋 Executive Summary</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li class="risk"><strong>🔴 SECURITY:</strong> Nine phishing/scam emails were auto-blocked and trashed — including spoofed "Cloud Storage" account-lock threats (6 variants), spoofed Lowe's and AAA prize scams, and one fake "Dr. Barbara O'Neill" health broadcast. All used gibberish domains. No action needed on those, but your email address (melissaw212) is being actively targeted — consider a password review and enabling advanced phishing protection.</li>
      <li class="opp"><strong>🟢 JOB SEARCH:</strong> You received a rejection from Legora (Senior People Partner, G&A), but 3 new LinkedIn job alerts are active — including a Director, People Business Partner at CodeRoad Inc, SVP/CHRO at Jeanne D'Arc Credit Union level roles, and an HRBP at TRC Talent Solutions (up to $45/hr). Your LinkedIn profile appeared in 9 searches this week — good visibility signal. HR Networking Group meeting is Wednesday July 22 and needs your RSVP.</li>
      <li class="cal"><strong>🔵 CALENDAR:</strong> You have two medical appointments today — Quest Diagnostics at 10:10 AM (confirmation #FOUGZX, 65 E 76th St) and Dr. Yuen at 3:00 PM. You also have a PT session Monday July 20, an HR Networking Zoom Wednesday July 22 (RSVP pending), and an Executive Roundtable Thursday July 23 that you have declined. Verizon Fios bill and Amy Fink's birthday both fall on July 23.</li>
    </ul>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     3. ACTION REQUIRED
════════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title yellow">⚡ Action Required</div>
  <div class="section-body">
    <div class="action-grid">

      <div class="action-card yellow">
        <div class="card-label">⚡ Billing</div>
        <h4>Bank of America Statement Available</h4>
        <div class="card-row"><span>Source:</span> Bank of America (ealerts.bankofamerica.com)</div>
        <div class="card-row"><span>Why it matters:</span> Money Market Savings account #7633 statement is ready — review for accuracy and any unusual activity.</div>
        <div class="card-row"><span>Due:</span> Review promptly</div>
        <div class="next-step">→ Log in to BofA and review your statement. Ask Erica for assistance via the app.</div>
      </div>

      <div class="action-card yellow">
        <div class="card-label">⚡ Billing</div>
        <h4>JetBlue Plus Card: Credit Score Changed</h4>
        <div class="card-row"><span>Source:</span> Barclays (services.barclaysus.com)</div>
        <div class="card-row"><span>Why it matters:</span> Credit score change notification — could be positive or negative. Important to monitor during a job search.</div>
        <div class="card-row"><span>Due:</span> Today</div>
        <div class="next-step">→ Log in to Barclays and check updated credit score. Note: a separate promo rate email (10.99% APR) is in trash — consider if relevant.</div>
      </div>

      <div class="action-card blue">
        <div class="card-label">📅 Today — RSVP</div>
        <h4>Quest Diagnostics: 10:10 AM Today</h4>
        <div class="card-row"><span>Source:</span> Google Calendar (confirmed)</div>
        <div class="card-row"><span>Location:</span> 65 E 76th St, Ground Floor G, NY 10021</div>
        <div class="card-row"><span>Confirmation:</span> #FOUGZX</div>
        <div class="next-step">→ Depart by 9:45 AM. Bring ID and insurance card. Fasting requirements check if applicable.</div>
      </div>

      <div class="action-card blue">
        <div class="card-label">📅 Today</div>
        <h4>Dr. Yuen Appointment: 3:00 PM Today</h4>
        <div class="card-row"><span>Source:</span> Google Calendar (confirmed)</div>
        <div class="card-row"><span>Duration:</span> 3:00 PM – 4:00 PM</div>
        <div class="card-row"><span>Location:</span> Not specified — confirm address</div>
        <div class="next-step">→ Confirm location and prepare any questions from Quest Diagnostics results if same-day turnaround is possible.</div>
      </div>

      <div class="action-card green">
        <div class="card-label">🟢 Job Search</div>
        <h4>RSVP: HR Networking & Job Search Group — Wed July 22</h4>
        <div class="card-row"><span>Source:</span> Google Calendar (needsAction)</div>
        <div class="card-row"><span>When:</span> Wednesday, July 22 · 12:00 PM – 1:30 PM</div>
        <div class="card-row"><span>Link:</span> Zoom (us06web.zoom.us)</div>
        <div class="next-step">→ Respond to calendar invite. Review HR Networking Team Guidelines (linked in invite). Prepare your 30-second intro and any active opportunities to share.</div>
      </div>

      <div class="action-card green">
        <div class="card-label">🟢 Job Search</div>
        <h4>RSVP: HR Networking Open Office Hours — Thu July 23</h4>
        <div class="card-row"><span>Source:</span> Google Calendar (needsAction)</div>
        <div class="card-row"><span>When:</span> Thursday, July 23 · 12:00 PM – 1:00 PM</div>
        <div class="card-row"><span>Note:</span> Turn off automated AI notetaking tools per organizer request.</div>
        <div class="next-step">→ Confirm attendance. This is separate from the Executive Roundtable (which you declined). Good networking opportunity.</div>
      </div>

      <div class="action-card yellow">
        <div class="card-label">⚡ Deadline</div>
        <h4>Verizon Fios Bill Due — July 23</h4>
        <div class="card-row"><span>Source:</span> Google Calendar</div>
        <div class="card-row"><span>Why it matters:</span> Bill reminder on calendar — ensure payment is scheduled to avoid service interruption.</div>
        <div class="next-step">→ Log in to Verizon and confirm autopay is set, or pay manually by July 23.</div>
      </div>

      <div class="action-card purple">
        <div class="card-label">🎂 Personal</div>
        <h4>Eric Dordick's Birthday — July 21</h4>
        <div class="card-row"><span>Source:</span> Google Calendar</div>
        <div class="card-row"><span>Why it matters:</span> All-day event tomorrow (Tuesday). Don't miss this if Eric is an important contact or friend.</div>
        <div class="next-step">→ Send a birthday message via text, LinkedIn, or card. If professional contact, a warm note on LinkedIn keeps the relationship warm during your job search.</div>
      </div>

      <div class="action-card green">
        <div class="card-label">🟢 Job Search</div>
        <h4>Review Legora Rejection — Reflect & Redirect</h4>
        <div class="card-row"><span>Source:</span> Legora Recruiting Team (no-reply@ashbyhq.com)</div>
        <div class="card-row"><span>Role:</span> Senior People Partner, G&A at Legora</div>
        <div class="card-row"><span>Status:</span> Application declined (email read, in trash)</div>
        <div class="next-step">→ Note for your pipeline tracker. Consider requesting feedback if you had a recruiter contact. Redirect energy to CodeRoad, TRC Talent, and Jeanne D'Arc leads.</div>
      </div>

      <div class="action-card red">
        <div class="card-label">🔴 Security</div>
        <h4>Untrashed Suspicious Email: "Dr. Barbara O'Neill" Health Broadcast</h4>
        <div class="card-row"><span>Source:</span> gbefviotrgttzz.99077826015791@osnf2f.ildgqu.58xjq1.us</div>
        <div class="card-row"><span>Why it matters:</span> This phishing email was NOT auto-trashed and is still sitting untrashed. It uses a celebrity doctor's name to lure clicks. Likely malware or health scam link.</div>
        <div class="next-step">→ Do NOT click any links. Delete immediately. Report as phishing in Gmail (three dots → Report phishing).</div>
      </div>

    </div>
  </div>
</div>

<hr class="divider">

<!-- ═══════════════════════════════════════════════════════════════
     4. FULL 7-DAY CALENDAR
════════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title blue">📅 Full 7-Day Calendar — July 17–23, 2026</div>
  <div class="section-body">

    <!-- Friday July 17 -->
    <div class="cal-day">
      <div class="cal-day-header today-hdr">📍 TODAY — Friday, July 17, 2026</div>
      <div class="cal-event">
        <div class="cal-time">10:10 – 10:25 AM</div>
        <div>
          <div class="cal-name">Quest Diagnostics Appointment <span class="badge confirmed">Confirmed</span></div>
          <div class="cal-meta">📍 65 E 76th St, Professional Apt GR-G, New York, NY 10021 &nbsp;·&nbsp; Confirmation: <strong>#FOUGZX</strong> (All Other Tests)</div>
          <div class="cal-meta">⚠️ <strong>Prep:</strong> Bring ID & insurance card. Depart by 9:45 AM. Check fasting requirements. Allow extra time for street parking/transit.</div>
        </div>
      </div>
      <div class="cal-event">
        <div class="cal-time">3:00 – 4:00 PM</div>
        <div>
          <div class="cal-name">Dr. Yuen <span class="badge confirmed">Confirmed</span></div>
          <div class="cal-meta">📍 Location not specified — confirm address before departing</div>
          <div class="cal-meta">⚠️ <strong>Prep:</strong> Confirm office address. Bring any relevant medical history or previous test results. If Quest results are same-day, bring them.</div>
        </div>
      </div>
    </div>

    <!-- Saturday July 18 -->
    <div class="cal-day">
      <div class="cal-day-header">Saturday, July 18, 2026</div>
      <div class="cal-event">
        <div class="cal-time">All Day</div>
        <div>
          <div class="cal-name"><em>No events scheduled</em></div>
          <div class="cal-meta">Clear day — good opportunity to rest, follow up on job leads, or prepare for the upcoming week.</div>
        </div>
      </div>
    </div>

    <!-- Sunday July 19 -->
    <div class="cal-day">
      <div class="cal-day-header">Sunday, July 19, 2026</div>
      <div class="cal-event">
        <div class="cal-time">All Day</div>
        <div>
          <div class="cal-name"><em>No events scheduled</em></div>
          <div class="cal-meta">Clear day — review job leads, prep for Monday PT session and upcoming networking events.</div>
        </div>
      </div>
    </div>

    <!-- Monday July 20 -->
    <div class="cal-day">
      <div class="cal-day-header">Monday, July 20, 2026</div>
      <div class="cal-event">
        <div class="cal-time">1:45 – 2:45 PM</div>
        <div>
          <div class="cal-name">PT (Physical Therapy) <span class="badge confirmed">Confirmed</span> <span class="badge warning">Duplicate Entry</span></div>
          <div class="cal-meta">📍 Location not specified</div>
          <div class="cal-meta">⚠️ <strong>Note:</strong> This event appears twice on the calendar with identical times — likely a duplicate. No action needed but you may want to delete the duplicate entry.</div>
          <div class="cal-meta"><strong>Prep:</strong> Confirm location. Wear comfortable clothing. Allow transit time.</div>
        </div>
      </div>
    </div>

    <!-- Tuesday July 21 -->
    <div class="cal-day">
      <div class="cal-day-header">Tuesday, July 21, 2026</div>
      <div class="cal-event">
        <div class="cal-time">All Day</div>
        <div>
          <div class="cal-name">🎂 Eric Dordick's Birthday <span class="badge birthday">Birthday</span></div>
          <div class="cal-meta">→ Send birthday message today. If Eric is a professional contact, a LinkedIn note is a great low-pressure touchpoint during your job search.</div>
        </div>
      </div>
      <div class="cal-event">
        <div class="cal-time">10:00 – 11:00 AM</div>
        <div>
          <div class="cal-name">Umi <span class="badge confirmed">Confirmed</span></div>
          <div class="cal-meta">📍 Location not specified</div>
          <div class="cal-meta"><strong>Prep:</strong> Confirm location and purpose of meeting. No details provided — clarify if this is professional, personal, or health-related.</div>
        </div>
      </div>
    </div>

    <!-- Wednesday July 22 -->
    <div class="cal-day">
      <div class="cal-day-header">Wednesday, July 22, 2026</div>
      <div class="cal-event">
        <div class="cal-time">12:00 – 1:30 PM</div>
        <div>
          <div class="cal-name">HR Networking & Job Search Group — Zoom Session 2 <span class="badge needsAction">RSVP Needed</span></div>
          <div class="cal-meta">🔗 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" style="color:#1565c0;">Zoom Link</a> &nbsp;·&nbsp; ~180+ attendees including active HR professionals</div>
          <div class="cal-meta">⚠️ <strong>Action Required:</strong> RSVP not yet submitted. Confirm attendance ASAP.</div>
          <div class="cal-meta"><strong>Prep:</strong> Review HR Networking Team Guidelines (in calendar invite). Prepare 30-sec intro, current job search status, and any roles to share. Check for upcoming openings to discuss.</div>
          <div class="cal-meta">🔗 <strong>Also:</strong> A duplicate "Network" entry exists at the same time — the same event, no details. Keep the detailed entry; delete the duplicate.</div>
        </div>
      </div>
      <div class="cal-event">
        <div class="cal-time">12:00 – 1:30 PM</div>
        <div>
          <div class="cal-name">Network (Duplicate Entry) <span class="badge warning">Likely Duplicate</span></div>
          <div class="cal-meta">Same time slot as HR Networking Zoom above. No location or description — likely the same event. Consider deleting this duplicate.</div>
        </div>
      </div>
    </div>

    <!-- Thursday July 23 -->
    <div class="cal-day">
      <div class="cal-day-header">Thursday, July 23, 2026</div>
      <div class="cal-event">
        <div class="cal-time">All Day</div>
        <div>
          <div class="cal-name">🎂 Amy Fink's Birthday <span class="badge birthday">Birthday</span></div>
          <div class="cal-meta">→ Send birthday wishes to Amy Fink today.</div>
        </div>
      </div>
      <div class="cal-event">
        <div class="cal-time">All Day</div>
        <div>
          <div class="cal-name">💳 Verizon Fios Bill Due <span class="badge bill">Bill</span></div>
          <div class="cal-meta">→ Ensure payment is made or autopay is confirmed. Review current plan if cost is a concern.</div>
        </div>
      </div>
      <div class="cal-event">
        <div class="cal-time">9:00 – 10:30 AM</div>
        <div>
          <div class="cal-name">Executive Roundtable <span class="badge declined">Declined</span></div>
          <div class="cal-meta">🔗 Zoom (us06web.zoom.us) &nbsp;·&nbsp; Hosted by: John Madigan &nbsp;·&nbsp; Meeting ID: 207 786 667</div>
          <div class="cal-meta">You have declined this event. No action needed unless you wish to reconsider — the Zoom credentials are preserved in the invite if you change your mind.</div>
        </div>
      </div>
      <div class="cal-event">
        <div class="cal-time">12:00 – 1:00 PM</div>
        <div>
          <div class="cal-name">HR Networking & Job Search: Open Office Hours — Zoom <span class="badge needsAction">RSVP Needed</span></div>
          <div class="cal-meta">🔗 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" style="color:#1565c0;">Zoom Link</a> &nbsp;·&nbsp; ~180+ attendees</div>
          <div class="cal-meta">⚠️ <strong>Action Required:</strong> RSVP pending. Organizer requests: <em>no automated AI notetaking tools.</em></div>
          <div class="cal-meta"><strong>Conflict Note:</strong> Overlaps with the Executive Roundtable (9–10:30 AM) but not in timing — these are sequential, not overlapping.</div>
          <div class="cal-meta"><strong>Prep:</strong> Disable AI notetaker. This is an open discussion forum — great for 1:1 introductions and sharing job search progress.</div>
        </div>
      </div>
    </div>

  </div>
</div>

<hr class="divider">

<!-- ═══════════════════════════════════════════════════════════════
     5. JOB SEARCH & INTERVIEW PIPELINE
════════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title green">💼 Job Search & Interview Pipeline</div>
  <div class="section-body">
    <div class="warning-box">📌 <strong>Legora Rejection Received:</strong> The Senior People Partner, G&A role at Legora has been declined (email read, in trash). Update your tracker and redirect focus to active leads below.</div>
    <table>
      <thead>
        <tr><th>Fit</th><th>Role / Company</th><th>Source</th><th>Date</th><th>Status</th><th>Next Step</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="fit-high">HIGH</span></td>
          <td><strong>Director, People Business Partner</strong><br>CodeRoad Inc</td>
          <td>LinkedIn Job Alert</td>
          <td>Jul 17, 2026<br><em>(posted 7/14)</em></td>
          <td><span class="pill green">New Alert</span></td>
          <td>Review posting and apply if aligned. Research CodeRoad culture and funding stage.</td>
        </tr>
        <tr>
          <td><span class="fit-high">HIGH</span></td>
          <td><strong>SVP, Chief Human Resources Officer</strong><br>Jeanne D'Arc Credit Union (similar roles)</td>
          <td>LinkedIn Job Alerts</td>
          <td>Jul 17, 2026</td>
          <td><span class="pill green">New Alert</span></td>
          <td>Review similar CHRO/SVP listings. Apply to most aligned. Strong match with your seniority level.</td>
        </tr>
        <tr>
          <td><span class="fit-medium">MEDIUM</span></td>
          <td><strong>Human Resources Business Partner</strong><br>TRC Talent Solutions (up to $45/hr)</td>
          <td>LinkedIn Job Alert</td>
          <td>Jul 17, 2026<br><em>(posted 7/14)</em></td>
          <td><span class="pill green">New Alert</span></td>
          <td>Consider for interim/contract income while targeting permanent roles. Apply if rate is acceptable.</td>
        </tr>
        <tr>
          <td><span class="fit-high">HIGH</span></td>
          <td><strong>HR Networking & Job Search Group</strong><br>Zoom Session 2</td>
          <td>Google Calendar</td>
          <td>Wed, Jul 22</td>
          <td><span class="pill yellow">RSVP Pending</span></td>
          <td>RSVP now. Prep 30-sec pitch, identify 2-3 connections to follow up with post-call.</td>
        </tr>
        <tr>
          <td><span class="fit-high">HIGH</span></td>
          <td><strong>HR Networking: Open Office Hours</strong><br>Zoom</td>
          <td>Google Calendar</td>
          <td>Thu, Jul 23</td>
          <td><span class="pill yellow">RSVP Pending</span></td>
          <td>RSVP now. Disable AI notetaking per organizer request.</td>
        </tr>
        <tr>
          <td><span class="fit-low">LOW</span></td>
          <td><strong>Senior People Partner, G&A</strong><br>Legora</td>
          <td>Email (no-reply@ashbyhq.com)</td>
          <td>Jul 17, 2026</td>
          <td><span class="pill red">Rejected</span></td>
          <td>Close out in pipeline tracker. Request recruiter feedback if a contact was established.</td>
        </tr>
        <tr>
          <td><span class="fit-medium">MEDIUM</span></td>
          <td><strong>LinkedIn Profile: 9 Search Appearances</strong><br>Including DC Recruit</td>
          <td>LinkedIn Notifications</td>
          <td>Jul 17, 2026</td>
          <td><span class="pill blue">Signal</span></td>
          <td>Check who viewed profile (upgrade to Premium if needed). Follow up with DC Recruit if possible — recruiter interest is a warm lead.</td>
        </tr>
        <tr>
          <td><span class="fit-medium">MEDIUM</span></td>
          <td><strong>LinkedIn: 2 New Connection Invitations</strong></td>
          <td>LinkedIn Notifications</td>
          <td>Jul 17, 2026</td>
          <td><span class="pill blue">Pending</span></td>
          <td>Review invitations from Dennis and other contact. Accept strategically — prioritize HR, recruiting, and potential hiring managers.</td>
        </tr>
        <tr>
          <td><span class="fit-medium">MEDIUM</span></td>
          <td><strong>Glassdoor: Cprime Company Reviews</strong></td>
          <td>Glassdoor (noreply@glassdoor.com)</td>
          <td>Jul 17, 2026</td>
          <td><span class="pill blue">Intel</span></td>
          <td>Review Cprime employee ratings if you are targeting or researching the company. Note email addressed to "amy" — may be a misdirected notification.</td>
        </tr>
      </tbody>
    </table>
    <div class="info-box">💡 <strong>Visibility Tip:</strong> Your profile was found by DC Recruit this week. If you are open to relocation or DC-area remote roles, consider updating your LinkedIn "Open to Work" preferences to include the DC market.</div>
  </div>
</div>

<hr class="divider">

<!-- ═══════════════════════════════════════════════════════════════
     6. FULL EMAIL REVIEW BY CATEGORY
════════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title red">🔒 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="email-cat">
      <div class="email-cat-hdr red">🔴 Security / Risk <span class="cnt">11 emails</span></div>
      <div class="email-cat-body">
        <p style="font-size:12px;margin-bottom:10px;color:#555;">Nine emails were auto-trashed as high-confidence phishing before review. Two additional suspicious emails remain untrashed and require manual deletion.</p>

        <div class="trash-group">
          <h4 class="phish-hdr">🚫 Auto-Trashed — Phishing (9 emails)</h4>
          <div class="email-item">
            <div class="sender">"melissaw212" &lt;melissaw212@tkfjojyhkmaiw…&gt;</div>
            <div class="subj">Act now: Your account will be closed within 48 hours if you don't renew</div>
            <div class="note">Auto-Trash Reason: Spoofed 'Cloud' service with urgent account-closure threat, sent from random gibberish domain, credential-harvesting attempt.</div>
          </div>
          <div class="email-item">
            <div class="sender">"Lowe's®" &lt;melissaw212@xuoloqlitwbmi…&gt;</div>
            <div class="subj">We have been trying to reach you - melissaw212 (Kobalt Tool Set)</div>
            <div class="note">Auto-Trash Reason: Spoofed Lowe's brand with fake prize/winner lure from gibberish domain, phishing/credential or personal info harvesting.</div>
          </div>
          <div class="email-item">
            <div class="sender">"melissaw212" &lt;melissaw212@vpvtszuwgkdmg…&gt;</div>
            <div class="subj">We have been trying to reach you - melissaw212 (AAA Car Emergency Kit)</div>
            <div class="note">Auto-Trash Reason: Spoofed AAA brand with fake prize/winner lure from gibberish domain, phishing/info harvesting.</div>
          </div>
          <div class="email-item">
            <div class="sender">"Lowe's®" &lt;melissaw212@ajddebeurgvhd…&gt;</div>
            <div class="subj">We have been trying to reach you - melissaw212 (Kobalt Tool Set — duplicate)</div>
            <div class="note">Auto-Trash Reason: Spoofed Lowe's brand with fake prize/winner lure from gibberish domain, phishing/info harvesting.</div>
          </div>
          <div class="email-item">
            <div class="sender">Payment-Declined &lt;kgegwhqerdl@crra…&gt;</div>
            <div class="subj">melissaw212, Your Cloud ID has been locked on Thu, 16 Jul 2026</div>
            <div class="note">Auto-Trash Reason: Fake 'Cloud Storage' payment-declined/account-locked threat from random gibberish domain, credential-harvesting attempt.</div>
          </div>
          <div class="email-item">
            <div class="sender">𝗣aym𝗲nt_Declin𝗲d© &lt;ojsdmynmtkjhxp…&gt; (lookalike Unicode name)</div>
            <div class="subj">melissaw212, Your Cloud ID has been locked onThu, 16 Jul 2026 20:53:06</div>
            <div class="note">Auto-Trash Reason: Fake 'Cloud' payment-declined/account-locked threat, sender display name uses lookalike Unicode characters, sent from gibberish domain.</div>
          </div>
          <div class="email-item">
            <div class="sender">Payment-Declined &lt;snlzjdihsjy@xiyz…&gt;</div>
            <div class="subj">[melissaw212] Your Cloud Account has been locked on [Thu,16 Jul-2026]</div>
            <div class="note">Auto-Trash Reason: Fake 'Cloud Storage' account-locked threat from random gibberish domain, credential-harvesting attempt.</div>
          </div>
          <div class="email-item">
            <div class="sender">Payment-Declined &lt;eokiikxuwjy@iiab…&gt;</div>
            <div class="subj">melissaw212¸Your Account Has been Blocked! Your Photos and Videos will be Removed Thu,16 Jul-2026</div>
            <div class="note">Auto-Trash Reason: Fake 'Cloud Storage' account-blocked threat from random gibberish domain, credential-harvesting attempt.</div>
          </div>
          <div class="email-item">
            <div class="sender">"melissaw212" &lt;melissaw212@…&gt; (casino spam)</div>
            <div class="subj">Claim your $7000 welcome bonus and 150 free spins 🤑 #048939</div>
            <div class="note">Auto-Trashed (in trash): Casino/gambling spam with fake jackpot winnings lure. No action needed.</div>
          </div>
        </div>

        <div class="trash-group">
          <h4 class="delete-hdr">⚠️ NOT Auto-Trashed — Manual Deletion Required (2 emails)</h4>
          <div class="email-item">
            <div class="sender">"'Dr. Barbara O'Neill'" &lt;gbefviotrgttzz.99077826015791@osnf2f.ildgqu.58xjq1.us&gt;</div>
            <div class="subj">Fwd: Did you see this leaked broadcast on nerve pain?*</div>
            <div class="note">⚠️ UNTRASHED — Phishing. Uses celebrity doctor name to harvest clicks. Do NOT click. Delete immediately and report as phishing.</div>
          </div>
          <div class="email-item">
            <div class="sender">"Cloud.Security" &lt;aamurynevrr@tpnd.czlyrsqutbgvw.us&gt;</div>
            <div class="subj">FINAL NOTICE: Your photos will be deleted tonight [Fri, 17 Jul-2026]</div>
            <div class="note">This copy is in trash (already addressed), but a near-identical variant from the previous day (Thu, 16 Jul) also exists in trash. Both are phishing — confirm both are deleted.</div>
          </div>
        </div>

        <div class="warning-box">🔐 <strong>Security Recommendation:</strong> Your username "melissaw212" is being actively harvested and used in targeted phishing. Recommend: (1) Enable Gmail's Enhanced Safe Browsing, (2) Review account recovery options, (3) Consider using a password manager and rotating credentials for critical accounts.</div>
        <div class="card-row" style="font-size:12px;margin-top:8px;"><span style="font-weight:700;">Recommended Action:</span> No action on auto-trashed items. Manually delete the 2 untrashed phishing emails immediately. Report both as phishing via Gmail.</div>
      </div>
    </div>

    <!-- JOB SEARCH -->
    <div class="email-cat">
      <div class="email-cat-hdr green">💼 Job Search <span class="cnt">5 emails</span></div>
      <div class="email-cat-body">
        <div class="email-item">
          <div class="sender">Legora Recruiting Team (no-reply@ashbyhq.com) — <em>In Trash, Read</em></div>
          <div class="subj">Update on your application to Legora – Senior People Partner, G&A</div>
          <div class="note">Application declined. Update pipeline. Consider requesting feedback from recruiter contact.</div>
        </div>
        <div class="email-item">
          <div class="sender">LinkedIn Job Alerts (jobalerts-noreply@linkedin.com)</div>
          <div class="subj">Director, People Business Partner at CodeRoad Inc</div>
          <div class="note">High-fit alert. Posted 7/14. Review and apply if aligned.</div>
        </div>
        <div class="email-item">
          <div class="sender">LinkedIn Job Alerts (jobalerts-noreply@linkedin.com)</div>
          <div class="subj">Human Resources Business Partner at TRC Talent Solutions: up to $45/hour</div>
          <div class="note">Medium-fit contract/interim role. Good bridge income option.</div>
        </div>
        <div class="email-item">
          <div class="sender">LinkedIn (jobs-noreply@linkedin.com)</div>
          <div class="subj">New jobs similar to Senior Vice President, Chief Human Resources Officer at Jeanne D'Arc Credit Union</div>
          <div class="note">Senior-level CHRO/SVP jobs alert. High fit for Melissa's experience level. Review all listed roles.</div>
        </div>
        <div class="email-item">
          <div class="sender">Glassdoor (noreply@glassdoor.com)</div>
          <div class="subj">Just in at Cprime: This week's employee reviews and more</div>
          <div class="note">Company intelligence on Cprime. Useful if targeting this employer. Note: addressed to "amy" — may be wrong account.</div>
        </div>
        <div class="card-row" style="font-size:12px;margin-top:10px;"><span style="font-weight:700;">Recommended Action:</span> Review CodeRoad and Jeanne D'Arc level roles today. Apply to TRC Talent if open to contract. Update pipeline tracker with Legora rejection.</div>
      </div>
    </div>

    <!-- RECRUITERS / NETWORKING / LINKEDIN -->
    <div class="email-cat">
      <div class="email-cat-hdr green">🤝 Recruiters / Networking / LinkedIn <span class="cnt">2 emails</span></div>
      <div class="email-cat-body">
        <div class="email-item">
          <div class="sender">LinkedIn (notifications-noreply@linkedin.com)</div>
          <div class="subj">You appeared in 9 searches — In Trash</div>
          <div class="note">Someone from DC Recruit found your profile. Strong visibility signal. Check who else searched if Premium is available. This email is in trash but the information is actionable.</div>
        </div>
        <div class="email-item">
          <div class="sender">LinkedIn (notifications-noreply@linkedin.com)</div>
          <div class="subj">You have 2 new invitations — "See who reached out, Dennis"</div>
          <div class="note">2 pending connection requests. Review and accept strategically — prioritize HR community, recruiters, hiring managers.</div>
        </div>
        <div class="card-row" style="font-size:12px;margin-top:10px;"><span style="font-weight:700;">Recommended Action:</span> Accept relevant LinkedIn invitations. Investigate DC Recruit interest via LinkedIn Premium or direct message.</div>
      </div>
    </div>

    <!-- CALENDAR / EVENTS -->
    <div class="email-cat">
      <div class="email-cat-hdr blue">📅 Calendar / Events <span class="cnt">1 email</span></div>
      <div class="email-cat-body">
        <div class="email-item">
          <div class="sender">Facebook Groups (groupupdates@facebookmail.com)</div>
          <div class="subj">Melissa, you're now a member of Seasons EM Homeowners</div>
          <div class="note">Approved to join Seasons EM Homeowners Facebook Group. Community/neighborhood group. No urgent action — join and introduce yourself when convenient.</div>
        </div>
        <div class="card-row" style="font-size:12px;margin-top:10px;"><span style="font-weight:700;">Recommended Action:</span> Visit the group and introduce yourself as a new member when time permits.</div>
      </div>
    </div>

    <!-- MEDICAL / HEALTH -->
    <div class="email-cat">
      <div class="email-cat-hdr" style="background:#00695c;">🏥 Medical / Health <span class="cnt">1 email</span></div>
      <div class="email-cat-body">
        <div class="email-item">
          <div class="sender">Alison Courses (noreply@us-education.alison.com)</div>
          <div class="subj">Melissa A, feel like you never have enough time? Read this ⏰</div>
          <div class="note">This is a course marketing email (time management focus), not a true health/medical email — categorized here due to wellness framing. Low priority; review only if interested in free courses.</div>
        </div>
        <div class="card-row" style="font-size:12px;margin-top:10px;"><span style="font-weight:700;">Recommended Action:</span> If interested in the time management course, review. Otherwise, unsubscribe or ignore.</div>
      </div>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="email-cat">
      <div class="email-cat-hdr yellow">💳 Financial / Billing <span class="cnt">3 emails</span></div>
      <div class="email-cat-body">
        <div class="email-item">
          <div class="sender">Bank of America (onlinebanking@ealerts.bankofamerica.com)</div>
          <div class="subj">Your statement is available — Money Market Savings #7633</div>
          <div class="note">🔴 <strong>Action Required:</strong> Review statement for accuracy and unusual charges. Legitimate email from ealerts.bankofamerica.com domain.</div>
        </div>
        <div class="email-item">
          <div class="sender">JetBlue Plus Card / Barclays (alerts@services.barclaysus.com)</div>
          <div class="subj">Notice: Your credit score has changed</div>
          <div class="note">🔴 <strong>Action Required:</strong> Check updated credit score — important during job search and any future housing/financial decisions.</div>
        </div>
        <div class="email-item">
          <div class="sender">JetBlue Plus Card / Barclays (info@emails.barclaysus.com) — <em>In Trash</em></div>
          <div class="subj">Reminder: Activate your 10.99% promo rate now</div>
          <div class="note">Promotional APR offer on JetBlue Plus Card. In trash. Consider if you plan purchases that could benefit from a low promo rate. Not urgent — safe to leave in trash.</div>
        </div>
        <div class="card-row" style="font-size:12px;margin-top:10px;"><span style="font-weight:700;">Recommended Action:</span> Log in to BofA and Barclays today to review statement and credit score. Promo rate email can remain in trash unless relevant.</div>
      </div>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="email-cat">
      <div class="email-cat-hdr purple">📚 Professional Development <span class="cnt">1 email</span></div>
      <div class="email-cat-body">
        <div class="email-item">
          <div class="sender">Empower (no-reply@rideempower.com)</div>
          <div class="subj">Tampa/Orlando Launch Coming Soon!</div>
          <div class="note">Empower rideshare service launching in Tampa/Orlando. Offers ride credit for referrals. Relevant if Melissa uses or plans to use rideshare in that area. Low priority.</div>
        </div>
        <div class="card-row" style="font-size:12px;margin-top:10px;"><span style="font-weight:700;">Recommended Action:</span> Review only if Tampa/Orlando travel is planned. Otherwise, archive or delete.</div>
      </div>
    </div>

    <!-- PERSONAL -->
    <div class="email-cat">
      <div class="email-cat-hdr" style="background:#ad1457;">💗 Personal <span class="cnt">4 emails</span></div>
      <div class="email-cat-body">
        <div class="email-item">
          <div class="sender">Match (mailer@connect.match.com)</div>
          <div class="subj">You just received a Super Like from Jay</div>
          <div class="note">Active Match.com notification. Review at your leisure.</div>
        </div>
        <div class="email-item">
          <div class="sender">Match (mailer@connect.match.com)</div>
          <div class="subj">You've had a profile view from prodigal-son (60 years old, Jackson, NJ)</div>
          <div class="note">Match.com profile view notification. Review when ready.</div>
        </div>
        <div class="email-item">
          <div class="sender">Match (mailer@value.match.com)</div>
          <div class="subj">Melissa, you've still got an unread message. See what they said. 👉</div>
          <div class="note">Unread message on Match.com. Check when you have a moment.</div>
        </div>
        <div class="email-item">
          <div class="sender">OkCupid (bounces@alerts.oknotify3.com)</div>
          <div class="subj">Someone likes you</div>
          <div class="note">OkCupid like notification. Check your OkCupid app when ready.</div>
        </div>
        <div class="card-row" style="font-size:12px;margin-top:10px;"><span style="font-weight:700;">Recommended Action:</span> Review messages and interactions on Match.com and OkCupid at your leisure. Today is a busy medical day — personal browsing can wait.</div>
      </div>
    </div>

    <!-- NEWSLETTERS / SUBSCRIPTIONS -->
    <div class="email-cat">
      <div class="email-cat-hdr purple">📰
