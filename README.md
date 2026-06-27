<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing – Melissa | Saturday, June 27, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px 28px; margin-bottom: 24px; }
  .header h1 { font-size: 2rem; font-weight: 700; letter-spacing: -0.5px; }
  .header .subtitle { font-size: 1.05rem; color: #a8b4d0; margin-top: 4px; }
  .header-meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header-meta-item { background: rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 18px; text-align: center; }
  .header-meta-item .val { font-size: 1.6rem; font-weight: 700; color: #e2e8f0; }
  .header-meta-item .lbl { font-size: 0.75rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px; }

  /* SECTION */
  .section { background: #fff; border-radius: 12px; padding: 24px 28px; margin-bottom: 20px; box-shadow: 0 1px 6px rgba(0,0,0,0.07); }
  .section-title { font-size: 1.1rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 16px; padding-bottom: 10px; border-bottom: 2px solid #e2e8f0; display: flex; align-items: center; gap: 8px; }

  /* COLOR BANDS */
  .band-red    { border-left: 5px solid #e53e3e; }
  .band-yellow { border-left: 5px solid #d69e2e; }
  .band-blue   { border-left: 5px solid #3182ce; }
  .band-green  { border-left: 5px solid #38a169; }
  .band-purple { border-left: 5px solid #805ad5; }
  .band-gray   { border-left: 5px solid #a0aec0; }

  /* EXEC SUMMARY */
  .exec-bullet { display: flex; gap: 12px; align-items: flex-start; padding: 12px 14px; border-radius: 8px; margin-bottom: 10px; }
  .exec-bullet:last-child { margin-bottom: 0; }
  .exec-bullet.risk  { background: #fff5f5; border: 1px solid #fed7d7; }
  .exec-bullet.oppty { background: #f0fff4; border: 1px solid #c6f6d5; }
  .exec-bullet.cal   { background: #ebf8ff; border: 1px solid #bee3f8; }
  .exec-icon { font-size: 1.4rem; flex-shrink: 0; margin-top: 2px; }
  .exec-text strong { display: block; font-size: 0.95rem; }
  .exec-text span   { font-size: 0.86rem; color: #4a5568; }

  /* ACTION CARDS */
  .action-cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; }
  .action-card { border-radius: 10px; padding: 16px 18px; }
  .action-card.red    { background: #fff5f5; border: 1.5px solid #fc8181; }
  .action-card.yellow { background: #fffff0; border: 1.5px solid #f6e05e; }
  .action-card.green  { background: #f0fff4; border: 1.5px solid #68d391; }
  .action-card.blue   { background: #ebf8ff; border: 1.5px solid #63b3ed; }
  .action-card.purple { background: #faf5ff; border: 1.5px solid #b794f4; }
  .action-card .card-label { font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 6px; }
  .action-card.red    .card-label { color: #c53030; }
  .action-card.yellow .card-label { color: #b7791f; }
  .action-card.green  .card-label { color: #276749; }
  .action-card.blue   .card-label { color: #2c5282; }
  .action-card.purple .card-label { color: #553c9a; }
  .action-card h4 { font-size: 0.95rem; font-weight: 700; margin-bottom: 4px; }
  .action-card .source { font-size: 0.78rem; color: #718096; margin-bottom: 6px; }
  .action-card .why { font-size: 0.83rem; color: #4a5568; margin-bottom: 8px; }
  .action-card .next { font-size: 0.83rem; font-weight: 600; color: #2d3748; padding: 6px 10px; background: rgba(0,0,0,0.05); border-radius: 6px; margin-bottom: 6px; }
  .action-card .due { font-size: 0.78rem; font-weight: 700; }
  .action-card.red    .due { color: #c53030; }
  .action-card.yellow .due { color: #b7791f; }
  .action-card.green  .due { color: #276749; }
  .action-card.blue   .due { color: #2c5282; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { font-size: 0.9rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px; color: #2c5282; background: #ebf8ff; padding: 6px 14px; border-radius: 6px; margin-bottom: 8px; }
  .cal-event { display: grid; grid-template-columns: 110px 1fr; gap: 10px; background: #f7fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px 14px; margin-bottom: 8px; }
  .cal-time { font-size: 0.82rem; font-weight: 700; color: #4a5568; padding-top: 2px; }
  .cal-event-body h4 { font-size: 0.92rem; font-weight: 700; }
  .cal-event-body .cal-meta { font-size: 0.78rem; color: #718096; margin-top: 3px; }
  .cal-event-body .cal-meta a { color: #3182ce; }
  .badge { display: inline-block; font-size: 0.7rem; font-weight: 700; padding: 2px 8px; border-radius: 10px; margin-left: 6px; vertical-align: middle; }
  .badge-confirmed  { background: #c6f6d5; color: #276749; }
  .badge-declined   { background: #fed7d7; color: #c53030; }
  .badge-needsaction{ background: #fefcbf; color: #b7791f; }
  .badge-conflict   { background: #fed7d7; color: #c53030; }
  .cal-prep { font-size: 0.8rem; color: #553c9a; margin-top: 5px; background: #faf5ff; padding: 4px 8px; border-radius: 5px; display: inline-block; }

  /* JOB SEARCH */
  .job-table { width: 100%; border-collapse: collapse; font-size: 0.84rem; }
  .job-table th { background: #2d3748; color: #fff; padding: 9px 12px; text-align: left; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.5px; }
  .job-table td { padding: 9px 12px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  .job-table tr:last-child td { border-bottom: none; }
  .job-table tr:nth-child(even) { background: #f7fafc; }
  .fit-high   { color: #276749; font-weight: 700; }
  .fit-medium { color: #b7791f; font-weight: 700; }
  .fit-low    { color: #718096; font-weight: 600; }
  .status-badge { font-size: 0.72rem; padding: 2px 8px; border-radius: 10px; font-weight: 700; display: inline-block; }
  .status-hot     { background: #fed7d7; color: #c53030; }
  .status-active  { background: #c6f6d5; color: #276749; }
  .status-alert   { background: #fefcbf; color: #b7791f; }
  .status-review  { background: #bee3f8; color: #2c5282; }
  .status-network { background: #e9d8fd; color: #553c9a; }

  /* EMAIL REVIEW */
  .email-category { margin-bottom: 14px; border-radius: 8px; overflow: hidden; border: 1px solid #e2e8f0; }
  .email-cat-header { display: grid; grid-template-columns: 1fr auto; align-items: center; padding: 10px 16px; font-weight: 700; font-size: 0.88rem; cursor: default; }
  .email-cat-header.red    { background: #fff5f5; color: #c53030; border-bottom: 1px solid #fed7d7; }
  .email-cat-header.yellow { background: #fffff0; color: #b7791f; border-bottom: 1px solid #f6e05e; }
  .email-cat-header.green  { background: #f0fff4; color: #276749; border-bottom: 1px solid #c6f6d5; }
  .email-cat-header.blue   { background: #ebf8ff; color: #2c5282; border-bottom: 1px solid #bee3f8; }
  .email-cat-header.purple { background: #faf5ff; color: #553c9a; border-bottom: 1px solid #e9d8fd; }
  .email-cat-header.gray   { background: #f7fafc; color: #4a5568; border-bottom: 1px solid #e2e8f0; }
  .email-cat-header.trash  { background: #fff5f5; color: #c53030; border-bottom: 1px solid #fed7d7; }
  .email-cat-count { background: rgba(0,0,0,0.08); border-radius: 12px; padding: 1px 10px; font-size: 0.8rem; }
  .email-cat-body { padding: 12px 16px; font-size: 0.83rem; }
  .email-cat-body .senders { color: #4a5568; margin-bottom: 5px; }
  .email-cat-body .action-rec { font-weight: 600; color: #2d3748; }
  .email-list { list-style: none; margin: 6px 0; }
  .email-list li { padding: 3px 0; color: #4a5568; border-bottom: 1px dashed #e2e8f0; }
  .email-list li:last-child { border-bottom: none; }
  .email-list li strong { color: #2d3748; }

  /* TRASH REVIEW */
  .trash-group { margin-bottom: 14px; }
  .trash-group h4 { font-size: 0.88rem; font-weight: 700; padding: 7px 14px; border-radius: 6px; margin-bottom: 8px; }
  .trash-restore { background: #fff5f5; color: #c53030; }
  .trash-review  { background: #fffff0; color: #b7791f; }
  .trash-delete  { background: #f7fafc; color: #718096; }
  .trash-item { font-size: 0.82rem; padding: 6px 14px; border-bottom: 1px solid #e2e8f0; }
  .trash-item:last-child { border-bottom: none; }
  .trash-item strong { color: #2d3748; }

  /* PROMO SUMMARY */
  .promo-table { width: 100%; border-collapse: collapse; font-size: 0.83rem; }
  .promo-table th { background: #4a5568; color: #fff; padding: 8px 12px; text-align: left; font-size: 0.77rem; text-transform: uppercase; letter-spacing: 0.4px; }
  .promo-table td { padding: 8px 12px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  .promo-table tr:last-child td { border-bottom: none; }
  .promo-table tr:nth-child(even) { background: #f7fafc; }
  .rec-delete  { color: #c53030; font-weight: 600; }
  .rec-review  { color: #b7791f; font-weight: 600; }
  .rec-keep    { color: #276749; font-weight: 600; }
  .rec-ignore  { color: #718096; font-weight: 600; }

  /* NEWSLETTER */
  .nl-table { width: 100%; border-collapse: collapse; font-size: 0.83rem; }
  .nl-table th { background: #553c9a; color: #fff; padding: 8px 12px; text-align: left; font-size: 0.77rem; text-transform: uppercase; letter-spacing: 0.4px; }
  .nl-table td { padding: 8px 12px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  .nl-table tr:last-child td { border-bottom: none; }
  .nl-table tr:nth-child(even) { background: #f7fafc; }

  /* ACCOUNTING TABLE */
  .acct-table { width: 100%; border-collapse: collapse; font-size: 0.84rem; }
  .acct-table th { background: #1a1a2e; color: #fff; padding: 9px 14px; text-align: left; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.5px; }
  .acct-table td { padding: 9px 14px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  .acct-table tr:last-child td { border-bottom: none; }
  .acct-table tr:nth-child(even) { background: #f7fafc; }
  .acct-total { background: #ebf8ff !important; font-weight: 700; }
  .acct-note { font-size: 0.8rem; color: #4a5568; margin-top: 10px; padding: 8px 12px; background: #f7fafc; border-radius: 6px; border-left: 3px solid #3182ce; }

  /* DASHBOARD */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 14px; }
  .dash-card { border-radius: 10px; padding: 14px 16px; }
  .dash-card.red    { background: #fff5f5; border: 1.5px solid #fc8181; }
  .dash-card.yellow { background: #fffff0; border: 1.5px solid #f6e05e; }
  .dash-card.blue   { background: #ebf8ff; border: 1.5px solid #63b3ed; }
  .dash-card.green  { background: #f0fff4; border: 1.5px solid #68d391; }
  .dash-card.purple { background: #faf5ff; border: 1.5px solid #b794f4; }
  .dash-card.gray   { background: #f7fafc; border: 1.5px solid #a0aec0; }
  .dash-card .dash-icon { font-size: 1.5rem; margin-bottom: 6px; }
  .dash-card .dash-num  { font-size: 1.8rem; font-weight: 800; }
  .dash-card .dash-lbl  { font-size: 0.75rem; color: #718096; text-transform: uppercase; letter-spacing: 0.5px; }
  .dash-card .dash-detail { font-size: 0.78rem; color: #4a5568; margin-top: 4px; }

  /* PRIORITY TABLE */
  .priority-table { width: 100%; border-collapse: collapse; font-size: 0.84rem; }
  .priority-table th { background: #2d3748; color: #fff; padding: 9px 14px; text-align: left; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.5px; }
  .priority-table td { padding: 9px 14px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  .priority-table tr:last-child td { border-bottom: none; }
  .priority-table tr:nth-child(even) { background: #f7fafc; }
  .pri-high   { color: #c53030; font-weight: 700; }
  .pri-medium { color: #b7791f; font-weight: 700; }
  .pri-low    { color: #718096; font-weight: 600; }

  /* TOP 3 */
  .top3 { counter-reset: top3; }
  .top3-item { counter-increment: top3; display: flex; gap: 14px; align-items: flex-start; padding: 16px 18px; border-radius: 10px; margin-bottom: 12px; background: linear-gradient(135deg, #1a1a2e 0%, #2d3748 100%); color: #fff; }
  .top3-num { font-size: 2rem; font-weight: 900; color: #63b3ed; flex-shrink: 0; line-height: 1; }
  .top3-text strong { display: block; font-size: 1rem; }
  .top3-text span { font-size: 0.84rem; color: #a0aec0; }

  /* SECURITY WARNING */
  .security-alert { background: #fff5f5; border: 2px solid #fc8181; border-radius: 8px; padding: 10px 16px; margin-bottom: 8px; display: flex; gap: 10px; align-items: flex-start; }
  .security-alert .sec-icon { font-size: 1.2rem; flex-shrink: 0; }
  .security-alert .sec-text strong { display: block; font-size: 0.88rem; color: #c53030; }
  .security-alert .sec-text span { font-size: 0.8rem; color: #742a2a; }

  /* MEDIUM STORY DECLINED */
  .medium-declined { background: #fffff0; border: 1.5px solid #f6e05e; border-radius: 8px; padding: 10px 14px; margin-bottom: 8px; font-size: 0.83rem; }

  @media (max-width: 600px) {
    .action-cards { grid-template-columns: 1fr; }
    .dashboard-grid { grid-template-columns: repeat(2, 1fr); }
    .cal-event { grid-template-columns: 1fr; }
    .header h1 { font-size: 1.4rem; }
  }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════ 1. HEADER ═══════════════════════════ -->
<div class="header">
  <div class="header h1" style="font-size:1rem;color:#94a3b8;text-transform:uppercase;letter-spacing:1px;font-weight:600;margin-bottom:4px;">Executive Briefing</div>
  <h1>Good Morning, Melissa ☀️</h1>
  <div class="subtitle">Saturday, June 27, 2026 &nbsp;·&nbsp; Prepared by your Chief of Staff</div>
  <div class="header-meta">
    <div class="header-meta-item"><div class="val">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="header-meta-item"><div class="val">5</div><div class="lbl">Calendar Events</div></div>
    <div class="header-meta-item"><div class="val">3</div><div class="lbl">Emails in Trash</div></div>
    <div class="header-meta-item"><div class="val">4</div><div class="lbl">Action Required</div></div>
    <div class="header-meta-item"><div class="val">2</div><div class="lbl">Hot Job Leads</div></div>
  </div>
</div>

<!-- ═══════════════════════════ 2. EXECUTIVE SUMMARY ═══════════════════════════ -->
<div class="section band-red">
  <div class="section-title">🔍 Executive Summary</div>
  <div class="exec-bullet risk">
    <div class="exec-icon">🔴</div>
    <div class="exec-text">
      <strong>RISK: Suspicious "Robinhood" login-code email from a non-Robinhood domain — potential phishing / credential attack</strong>
      <span>An OTP code email from <em>clientsupportdesk@pressganey.com</em> (not robinhood.com) arrived Friday. Do not use this code. Verify your Robinhood account directly and enable 2FA if not already active. A fake Lowe's prize scam and a payment-blocked threat email are also present.</span>
    </div>
  </div>
  <div class="exec-bullet oppty">
    <div class="exec-icon">🟢</div>
    <div class="exec-text">
      <strong>OPPORTUNITY: Active recruiter outreach from Infillion for SVP, People Operations — you've already replied</strong>
      <span>Sean Little at Infillion reached out Friday, you responded same day. Medium story submission was declined, but two senior HR roles (CHRO @ Goddard Riverside $175–200K; CPO @ Omnisage via Scovai) and multiple Glassdoor alerts are live. LinkedIn "Open to Work" status has lapsed — needs reactivation.</span>
    </div>
  </div>
  <div class="exec-bullet cal">
    <div class="exec-icon">🔵</div>
    <div class="exec-text">
      <strong>CALENDAR: COBRA payment check is on the calendar for 10 AM today — two networking events next week need RSVPs</strong>
      <span>HR Networking & Job Search Group (Jul 1, 12–1:30 PM) and Open Office Hours (Jul 2, 12–1 PM) are both awaiting your response. You declined the Executive Roundtable on Jul 2 — confirm that was intentional.</span>
    </div>
  </div>
</div>

<!-- ═══════════════════════════ 3. ACTION REQUIRED ═══════════════════════════ -->
<div class="section">
  <div class="section-title">⚡ Action Required</div>
  <div class="action-cards">

    <div class="action-card red">
      <div class="card-label">🔴 Security — Urgent</div>
      <h4>Suspicious "Robinhood" OTP Email</h4>
      <div class="source">From: clientsupportdesk@pressganey.com · Fri Jun 26</div>
      <div class="why">This is NOT from Robinhood's official domain. Code <strong>196459</strong> was sent from a Press Ganey address — this is a phishing attempt or credential-stuffing attack. Someone may be attempting to access your Robinhood account.</div>
      <div class="next">→ Log into Robinhood directly (not via any link). Change your password. Enable 2FA. Do NOT use code 196459.</div>
      <div class="due">⏰ Due: TODAY</div>
    </div>

    <div class="action-card yellow">
      <div class="card-label">🟡 Billing — COBRA</div>
      <h4>Check COBRA Payments</h4>
      <div class="source">Google Calendar · Today 10:00–11:00 AM</div>
      <div class="why">COBRA health coverage payment is on your calendar for this morning. Missing a COBRA payment can result in loss of coverage with no grace period warning.</div>
      <div class="next">→ Log into your COBRA administrator portal, confirm payment status, and document the confirmation number.</div>
      <div class="due">⏰ Due: TODAY, 10:00 AM</div>
    </div>

    <div class="action-card green">
      <div class="card-label">🟢 Job Search — Hot Lead</div>
      <h4>Follow Up: Infillion SVP, People Operations</h4>
      <div class="source">Sean Little, Infillion · Fri Jun 26 (you replied same day)</div>
      <div class="why">Recruiter Sean Little reviewed your application and wants to schedule next steps. You replied Friday noting your prior conversation with Brian. This is a warm, active lead — don't let it go cold.</div>
      <div class="next">→ Follow up Monday AM if no response received. Confirm your availability for a screening call this week.</div>
      <div class="due">⏰ Follow up: Monday, Jun 30</div>
    </div>

    <div class="action-card yellow">
      <div class="card-label">🟡 LinkedIn — Open to Work</div>
      <h4>Reactivate "Open to Work" on LinkedIn</h4>
      <div class="source">LinkedIn · Sat Jun 27, 2:44 AM</div>
      <div class="why">LinkedIn notified you that your "Open to Work" status has expired. With active recruiter outreach happening, this is reducing your visibility to hiring managers and recruiters on the platform.</div>
      <div class="next">→ Go to LinkedIn → Me → View Profile → Open to → Finding a new job → Reactivate and update target roles (CPO/CHRO/SVP HR).</div>
      <div class="due">⏰ Due: Today or Tomorrow</div>
    </div>

    <div class="action-card blue">
      <div class="card-label">🔵 Calendar — RSVP Needed</div>
      <h4>RSVP: HR Networking & Job Search Group (Jul 1)</h4>
      <div class="source">Google Calendar · Tue Jul 1, 12:00–1:30 PM via Zoom</div>
      <div class="why">Status is "Needs Action." You also have a personal "Network" event at the same time confirmed — possible duplicate/conflict. Clarify and RSVP to the group session.</div>
      <div class="next">→ Confirm attendance via calendar invite. Zoom: us06web.zoom.us/j/81954171722. Review agenda doc linked in description.</div>
      <div class="due">⏰ RSVP by: Mon Jun 30</div>
    </div>

    <div class="action-card yellow">
      <div class="card-label">🟡 Financial — Venmo</div>
      <h4>Venmo Transfer of $27.85 Initiated (in Trash)</h4>
      <div class="source">Venmo · Sat Jun 27, 1:39 AM — Found in Trash</div>
      <div class="why">A $27.85 standard transfer was initiated. This email was moved to Trash — verify this transfer was intentional and not fraudulent before permanently deleting.</div>
      <div class="next">→ Log into Venmo, verify the transaction ID and recipient, confirm it was authorized.</div>
      <div class="due">⏰ Due: Today</div>
    </div>

    <div class="action-card green">
      <div class="card-label">🟢 Professional — Medium</div>
      <h4>Medium Story Submission Declined</h4>
      <div class="source">Medium · Sat Jun 27, 5:00 AM</div>
      <div class="why">Your article "What if the real value of AI in HR is fewer…" was declined for publication in a Medium publication. This is a professional writing opportunity worth revisiting.</div>
      <div class="next">→ Review the submission. Consider self-publishing on your Medium profile, or resubmitting to a different publication (e.g., HR Brew, SHRM blog, LinkedIn newsletter).</div>
      <div class="due">⏰ When ready</div>
    </div>

    <div class="action-card yellow">
      <div class="card-label">🟡 Billing — Anthropic</div>
      <h4>Anthropic Receipt #2825-5563-5457</h4>
      <div class="source">Anthropic, PBC · Fri Jun 26, 10:13 PM</div>
      <div class="why">A billing receipt arrived from Anthropic. Separately, a rate limit increase notification also arrived today — no action needed on that one, but the receipt should be filed for expense tracking.</div>
      <div class="next">→ Download and file receipt for business/tax records. Note rate limit upgrade — beneficial for your Claude API usage.</div>
      <div class="due">⏰ File this week</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════ 4. FULL 7-DAY CALENDAR ═══════════════════════════ -->
<div class="section band-blue">
  <div class="section-title">📅 Full 7-Day Calendar (Jun 27 – Jul 3, 2026)</div>

  <div class="cal-day">
    <div class="cal-day-header">Saturday, June 27 — TODAY</div>
    <div class="cal-event">
      <div class="cal-time">10:00 AM<br>– 11:00 AM</div>
      <div class="cal-event-body">
        <h4>Check COBRA Payments <span class="badge badge-confirmed">✓ Confirmed</span></h4>
        <div class="cal-meta">📍 No location · Solo reminder</div>
        <div class="cal-prep">🔧 Prep: Log into COBRA portal before 10 AM. Have account number and payment method ready. Confirm amount due and document confirmation #.</div>
      </div>
    </div>
  </div>

  <div class="cal-day">
    <div class="cal-day-header">Sunday, June 29</div>
    <div style="padding: 8px 14px; font-size: 0.83rem; color: #718096; font-style: italic;">No events scheduled.</div>
  </div>

  <div class="cal-day">
    <div class="cal-day-header">Monday, June 30</div>
    <div style="padding: 8px 14px; font-size: 0.83rem; color: #718096; font-style: italic;">No events scheduled. Recommended: follow up with Sean Little (Infillion) + reactivate LinkedIn Open to Work.</div>
  </div>

  <div class="cal-day">
    <div class="cal-day-header">Tuesday, July 1</div>
    <div class="cal-event">
      <div class="cal-time">12:00 PM<br>– 1:30 PM</div>
      <div class="cal-event-body">
        <h4>HR Networking &amp; Job Search Group — Zoom 2 <span class="badge badge-needsaction">⚠ Needs RSVP</span> <span class="badge badge-conflict">Conflict</span></h4>
        <div class="cal-meta">📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a> · ~200 attendees</div>
        <div class="cal-meta">⚠️ <strong>CONFLICT:</strong> "Network" event also confirmed at 12:00–1:30 PM same day — likely a duplicate. Verify.</div>
        <div class="cal-prep">🔧 Prep: Review team guidelines doc (linked in description). Prepare 30-second intro. Bring target companies list. Review attendee list for warm contacts.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-time">12:00 PM<br>– 1:30 PM</div>
      <div class="cal-event-body">
        <h4>Network <span class="badge badge-confirmed">✓ Confirmed</span> <span class="badge badge-conflict">Possible Duplicate</span></h4>
        <div class="cal-meta">📍 No location · No attendees listed</div>
        <div class="cal-prep">⚠️ This appears to be a personal block that overlaps with the HR Networking Zoom above. Confirm whether this is a duplicate or a separate commitment.</div>
      </div>
    </div>
  </div>

  <div class="cal-day">
    <div class="cal-day-header">Wednesday, July 2</div>
    <div class="cal-event">
      <div class="cal-time">9:00 AM<br>– 10:30 AM</div>
      <div class="cal-event-body">
        <h4>Executive Roundtable <span class="badge badge-declined">✗ Declined</span></h4>
        <div class="cal-meta">📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> · Hosted by John Madigan</div>
        <div class="cal-meta">Meeting ID: 207 786 667 · Password: 205454</div>
        <div class="cal-prep">⚠️ You declined this event. Verify this was intentional — Executive Roundtable sessions can be valuable networking. If you want to reverse, contact John Madigan to request re-admission.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-time">12:00 PM<br>– 1:00 PM</div>
      <div class="cal-event-body">
        <h4>HR Networking &amp; Job Search: Open Office Hours — Zoom 2 <span class="badge badge-needsaction">⚠ Needs RSVP</span></h4>
        <div class="cal-meta">📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a> · Same group as Jul 1</div>
        <div class="cal-meta">Note: Organizer requests no automated AI notetaking tools.</div>
        <div class="cal-prep">🔧 Prep: Open discussion format. Come with 1–2 specific job search questions. Great for informal advice on your Infillion opportunity or Medium resubmission strategy.</div>
      </div>
    </div>
  </div>

  <div class="cal-day">
    <div class="cal-day-header">Thursday, July 3</div>
    <div style="padding: 8px 14px; font-size: 0.83rem; color: #718096; font-style: italic;">No events scheduled. Fourth of July weekend begins.</div>
  </div>

</div>

<!-- ═══════════════════════════ 5. JOB SEARCH & INTERVIEW PIPELINE ═══════════════════════════ -->
<div class="section band-green">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
  <table class="job-table">
    <thead>
      <tr>
        <th>Source</th>
        <th>Role / Company</th>
        <th>Status</th>
        <th>Fit</th>
        <th>Next Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Infillion (Recruiter)</strong><br><span style="font-size:0.77rem;color:#718096;">Sean Little · Jun 26</span></td>
        <td>SVP, People Operations<br><em>Infillion</em></td>
        <td><span class="status-badge status-hot">🔥 HOT — Active Exchange</span></td>
        <td class="fit-high">HIGH</td>
        <td>Follow up Mon Jun 30 if no reply. Schedule screening call.</td>
      </tr>
      <tr>
        <td><strong>Indeed Alert</strong><br><span style="font-size:0.77rem;color:#718096;">Jun 27</span></td>
        <td>Chief Human Resources Officer<br><em>Goddard Riverside Community Center</em></td>
        <td><span class="status-badge status-alert">📋 New Alert</span></td>
        <td class="fit-high">HIGH</td>
        <td>$175K–$200K/yr. Review JD and apply if aligned. Nonprofit CHRO — strong match.</td>
      </tr>
      <tr>
        <td><strong>Scovai</strong><br><span style="font-size:0.77rem;color:#718096;">Jun 27</span></td>
        <td>Chief People &amp; Culture Officer<br><em>Omnisage LLC</em></td>
        <td><span class="status-badge status-alert">📋 Profile Match</span></td>
        <td class="fit-high">HIGH</td>
        <td>Log into Scovai, review role details, apply or dismiss from pipeline.</td>
      </tr>
      <tr>
        <td><strong>Glassdoor Alert</strong><br><span style="font-size:0.77rem;color:#718096;">Jun 27</span></td>
        <td>Director, Human Resources (Commercial)<br><em>Oldcastle BuildingEnvelope + 7 more</em></td>
        <td><span class="status-badge status-review">🔍 Alert — Unreviewed</span></td>
        <td class="fit-medium">MEDIUM</td>
        <td>Review 8 job listings. Flag Director-level roles if CPO/CHRO search is primary.</td>
      </tr>
      <tr>
        <td><strong>Glassdoor Alert</strong><br><span style="font-size:0.77rem;color:#718096;">Jun 27</span></td>
        <td>HR Generalist (Volunteer) @ Season To Soar + 7 more<br><em>Various · Remote</em></td>
        <td><span class="status-badge status-review">🔍 Alert — Unreviewed</span></td>
        <td class="fit-low">LOW</td>
        <td>Volunteer and generalist roles are below target level. Review for networking leads only.</td>
      </tr>
      <tr>
        <td><strong>LinkedIn</strong><br><span style="font-size:0.77rem;color:#718096;">Jun 27</span></td>
        <td>Open to Work Status — Expired</td>
        <td><span class="status-badge status-hot">⚠️ Needs Action</span></td>
        <td class="fit-high">HIGH</td>
        <td>Reactivate immediately. Update role preferences to CHRO / CPO / SVP HR.</td>
      </tr>
      <tr>
        <td><strong>Networking · Calendar</strong><br><span style="font-size:0.77rem;color:#718096;">Jul 1 &amp; Jul 2</span></td>
        <td>HR Networking &amp; Job Search Group Zoom<br><em>Open Office Hours (Jul 2)</em></td>
        <td><span class="status-badge status-network">🤝 Networking</span></td>
        <td class="fit-high">HIGH</td>
        <td>RSVP to both. Bring Infillion update + Goddard Riverside research for peer feedback.</td>
      </tr>
      <tr>
        <td><strong>Self-Send</strong><br><span style="font-size:0.77rem;color:#718096;">Jun 26</span></td>
        <td>WeissAMelissa6.26ch.docx — Resume/Cover Letter Version</td>
        <td><span class="status-badge status-active">📄 Document</span></td>
        <td class="fit-medium">MEDIUM</td>
        <td>Ensure this is the current version. Match to Infillion and Goddard Riverside JDs before submitting.</td>
      </tr>
      <tr>
        <td><strong>Self-Send</strong><br><span style="font-size:0.77rem;color:#718096;">Jun 26</span></td>
        <td>KPI LinkedIn Post Link (Josh Sanders)</td>
        <td><span class="status-badge status-review">💡 Research</span></td>
        <td class="fit-medium">MEDIUM</td>
        <td>Review the post on KPI measurement. Potential content for your own LinkedIn or Medium resubmission.</td>
      </tr>
      <tr>
        <td><strong>Scovai Pipeline</strong><br><span style="font-size:0.77rem;color:#718096;">Jun 27</span></td>
        <td>[NEW PIPELINE TEST] HR Search — 2026-06-26</td>
        <td><span class="status-badge status-active">🔧 Pipeline Active</span></td>
        <td class="fit-high">HIGH</td>
        <td>TypeScript pipeline sending daily HR search results at 2 PM ET. Review results and refine filters.</td>
      </tr>
      <tr>
        <td><strong>Medium</strong><br><span style="font-size:0.77rem;color:#718096;">Jun 27</span></td>
        <td>"What if the real value of AI in HR is fewer…" — Article</td>
        <td><span class="status-badge status-hot">❌ Declined</span></td>
        <td class="fit-medium">MEDIUM</td>
        <td>Resubmit to different publication or self-publish. Good thought leadership content.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════ 6. FULL EMAIL REVIEW BY CATEGORY ═══════════════════════════ -->
<div class="section">
  <div class="section-title">📬 Full Email Review by Category</div>

  <!-- SECURITY / RISK -->
  <div class="email-category">
    <div class="email-cat-header red">🔴 Security / Risk <span class="email-cat-count">4</span></div>
    <div class="email-cat-body">
      <ul class="email-list">
        <li><strong>Robinhood (fake) — clientsupportdesk@pressganey.com:</strong> "Your One-Time Login Code: 196459" — <span style="color:#c53030;font-weight:700;">PHISHING. Not from Robinhood.</span> Do not use code. Change password immediately.</li>
        <li><strong>Fake Lowe's Prize Scam — ui4cfq4mje@7t4deas7q1.us:</strong> "You've been chosen! Take your Kobalt tool set For Free" — Classic scam. Do not click. Mark spam.</li>
        <li><strong>Payment-Declined Threat — gejahfnr@crozxnsrdozsvjcppnkhecesod.net:</strong> "Your Account Has been Blocked! Photos/Videos will be Removed" — Fear-based phishing. Ignore and delete.</li>
        <li><strong>FUCK-BUDDY SECRET spam — llbbozdifoooaf...@znrft7.us:</strong> Explicit spam in non-inbox folder. Delete immediately, mark as spam.</li>
      </ul>
      <div class="action-rec">🔴 Recommended Action: Secure Robinhood account NOW. Delete/report all three scam emails. Consider adding spam filters for these sender domains.</div>
    </div>
  </div>

  <!-- JOB SEARCH -->
  <div class="email-category">
    <div class="email-cat-header green">🟢 Job Search — Alerts &amp; Applications <span class="email-cat-count">6</span></div>
    <div class="email-cat-body">
      <ul class="email-list">
        <li><strong>Indeed:</strong> "Chief Human Resources Officer @ Goddard Riverside" — $175–200K — <span class="fit-high">HIGH priority. Review and apply.</span></li>
        <li><strong>Scovai:</strong> "Chief People and Culture Officer · Omnisage LLC" — <span class="fit-high">HIGH priority. Review on Scovai platform.</span></li>
        <li><strong>Glassdoor:</strong> "Director, HR (Commercial) at Oldcastle BuildingEnvelope + 7 more" — Review 8 listings.</li>
        <li><strong>Glassdoor:</strong> "Volunteer HR Generalist at Season To Soar + 7 more" — Low fit for target level; skim for leads.</li>
        <li><strong>Self (melissaw212):</strong> "[NEW PIPELINE TEST] HR Search — 2026-06-26" — Active TypeScript job pipeline. Review daily results.</li>
        <li><strong>Self (melissaw212):</strong> Claude.ai share link — Likely a job search-related AI session. Review for any saved research.</li>
      </ul>
      <div class="action-rec">🟢 Recommended Action: Apply to Goddard Riverside CHRO and Omnisage CPO roles this weekend. Review Glassdoor Director alerts for hidden gems.</div>
    </div>
  </div>

  <!-- RECRUITERS / NETWORKING -->
  <div class="email-category">
    <div class="email-cat-header green">🟢 Recruiters / Networking <span class="email-cat-count">3</span></div>
    <div class="email-cat-body">
      <ul class="email-list">
        <li><strong>Sean Little, Infillion:</strong> "Next Steps with Infillion - SVP, People Operations" — Active recruiter outreach. You replied same day ✓</li>
        <li><strong>melissa (melweiss212):</strong> "Re: Next Steps with Infillion" — Your reply to Sean. Confirmed mention of prior Brian conversation ✓</li>
        <li><strong>LinkedIn:</strong> "You're no longer letting recruiters know you're open to work" — Action needed: reactivate status.</li>
      </ul>
      <div class="action-rec">🟢 Recommended Action: Follow up with Infillion Mon Jun 30. Reactivate LinkedIn Open to Work today.</div>
    </div>
  </div>

  <!-- CALENDAR / EVENTS -->
  <div class="email-category">
    <div class="email-cat-header blue">🔵 Calendar / Events (via email context) <span class="email-cat-count">1</span></div>
    <div class="email-cat-body">
      <ul class="email-list">
        <li><strong>Fractional In A Box:</strong> "How to market when the buyer is not human" — Newsletter with professional content. Secondary note: marketing strategy for AI-era — relevant to HR thought leadership.</li>
      </ul>
      <div class="action-rec">🔵 Recommended Action: Save for reading this weekend. Could inform your Medium article resubmission strategy.</div>
    </div>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="email-category">
    <div class="email-cat-header yellow">🟡 Financial / Billing <span class="email-cat-count">3</span></div>
    <div class="email-cat-body">
      <ul class="email-list">
        <li><strong>Venmo:</strong> "Standard transfer has been initiated — $27.85" — Found in <em>Trash</em>. Verify this transfer was intentional before deleting permanently.</li>
        <li><strong>Anthropic, PBC:</strong> "Receipt #2825-5563-5457" — Legitimate Anthropic billing receipt. File for records.</li>
        <li><strong>My Best Buy Visa (Citi):</strong> "Gas costs add up. Rewards can too" — Credit card rewards promotion. Low priority.</li>
      </ul>
      <div class="action-rec">🟡 Recommended Action: Verify Venmo transfer. File Anthropic receipt. Dismiss Citi promo.</div>
    </div>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="email-category">
    <div class="email-cat-header purple">🟣 Professional Development <span class="email-cat-count">4</span></div>
    <div class="email-cat-body">
      <ul class="email-list">
        <li><strong>Medium:</strong> "New Status on Story Submission — Declined" — Article on AI in HR was declined. Resubmit elsewhere.</li>
        <li><strong>Self (melissa, kpi link):</strong> LinkedIn post on KPI measurement (Josh Sanders) — Research saved for thought leadership.</li>
        <li><strong>Alison Courses:</strong> "Turn your business idea into something real ✨" — Online business course promo. Could be relevant if building HR consulting practice.</li>
        <li><strong>Anthropic Team:</strong> "Higher rate limits on the Claude API" — No action needed. Rate limits increasing for your API usage — beneficial update.</li>
      </ul>
      <div class="action-rec">🟣 Recommended Action: Resubmit Medium article. Review KPI post for LinkedIn content. Note Anthropic rate limit upgrade.</div>
    </div>
  </div>

  <!-- PERSONAL -->
  <div class="email-category">
    <div class="email-cat-header gray">⚪ Personal <span class="email-cat-count">3</span></div>
    <div class="email-cat-body">
      <ul class="email-list">
        <li><strong>Jdate:</strong> "You've Got a Like on Jdate ❤️" — Dating app notification.</li>
        <li><strong>Match.com:</strong> "Endri likes you. See if it's mutual." — Dating app notification.</li>
        <li><strong>OkCupid:</strong> "Someone likes you" — Dating app notification.</li>
      </ul>
      <div class="action-rec">⚪ Recommended Action: Review at your leisure. No professional urgency.</div>
    </div>
  </div>

  <!-- NEWSLETTERS / SUBSCRIPTIONS -->
  <div class="email-category">
    <div class="email-cat-header purple">🟣 Newsletters / Subscriptions <span class="email-cat-count">7</span></div>
    <div class="email-cat-body">
      <ul class="email-list">
        <li><strong>Fractional In A Box:</strong> "How to market when the buyer is not human" — Marketing/AI newsletter.</li>
        <li><strong>Meidas+:</strong> "You Can't Be What You Can't See: Maura Sullivan's Story" — Political/media newsletter (in Trash).</li>
        <li><strong>Meidas+:</strong> "Ok, last chance..." — Subscription push newsletter.</li>
        <li><strong>Nextdoor Local News:</strong> "A Familiar Second Avenue Corner Is About to Look Completely..." — NYC neighborhood news.</li>
        <li><strong>Yorkville Trending Posts:</strong> "Where do you donate clothes and home goods..." — Nextdoor community post.</li>
        <li><strong>Nextdoor:</strong> "Top story: Rising Costs and Slower Business End a 54-Year-Old..." — Cozy Soup n' Burger closure.</li>
        <li><strong>22 Words:</strong> "(Jun 27) Last day for Fan Favorites" — Retail/deal newsletter.</li>
      </ul>
      <div class="action-rec">🟣 Recommended Action: Keep Fractional In A Box (relevant). Review Nextdoor for neighborhood interest. Consider unsubscribing from 22 Words and duplicate Meidas+ sends.</div>
    </div>
  </div>

  <!-- PROMOTIONAL / RETAIL -->
  <div class="email-category">
    <div class="email-cat-header gray">⚪ Promotional / Retail <span class="email-cat-count">16</span></div>
    <div class="email-cat-body">
      <div class="senders"><strong>Brands:</strong> Gap Factory, Kohl's, SHEIN (×3), Amazon Prime Day, Temu (×2), Old Navy, Halara, Lemon8, Fisher Investments, Kickresume (×2), RAD Team (S&amp;P 500), Mystery Deal, Yahoo Mail</div>
      <div class="action-rec">⚪ Recommended Action: Delete/ignore all. Review SHEIN/Temu if personal shopping needed. Kickresume is misdressed to "amy/mel" — duplicate send, not personalized. See Promotional/Retail Summary section below for full breakdown.</div>
    </div>
  </div>

  <!-- MEDICAL / HEALTH -->
  <div class="email-category">
    <div class="email-cat-header yellow">🟡 Medical / Health <span class="email-cat-count">1</span></div>
    <div class="email-cat-body">
      <ul class="email-list">
        <li><strong>Direct.Meds.Weight.Loss:</strong> "Act Fast! Your Weight Loss Journey Starts Now" — Ozempic/Mounjaro marketing spam from suspicious domain (@wgxx.ellqoncpequfu.us). Not a legitimate medical provider.</li>
      </ul>
      <div class="action-rec">🟡 Recommended Action: Mark as spam. If interested in GLP-1 medications, consult your actual physician — do not respond to unsolicited medical spam.</div>
    </div>
  </div>

  <!-- SAFE TO DELETE / IGNORE -->
  <div class="email-category">
    <div class="email-cat-header gray">⚪ Safe to Delete / Ignore <span class="email-cat-count">2</span></div>
    <div class="email-cat-body">
      <ul class="email-list">
        <li><strong>Facebook Friend Suggestions:</strong> "Sorina Luculetiu is a new friend suggestion" — Auto-generated FB notification. Dismiss.</li>
        <li><strong>Self (melissaw212):</strong> "WeissAMelissa6.26ch.docx" — Email to self (likely a document share). Already in non-inbox. File or archive.</li>
      </ul>
      <div class="action-rec">⚪ Recommended Action: Delete FB notification. Archive self-sent document email.</div>
    </div>
  </div>

</div>

<!-- ═══════════════════════════ 7. TRASH REVIEW ═══════════════════════════ -->
<div class="section band-red">
  <div class="section-title">🗑️ Trash Review</div>
  <p style="font-size:0.83rem;color:#4a5568;margin-bottom:14px;">3 emails were found in Gmail Trash. Review before permanent deletion.</p>

  <div class="trash-group">
    <h4 class="trash-restore">🔴 Restore Immediately (1)</h4>
    <div class="trash-item">
      <strong>Venmo &lt;venmo@venmo.com&gt;</strong> — "Your Venmo Standard transfer has been initiated"<br>
      <span style="color:#4a5568;">Transfer of <strong>$27.85</strong> initiated Saturday Jun 27 at 1:39 AM. Transaction ID present. This is a legitimate financial transaction record — <strong>restore and file before deleting</strong>. Verify the transfer was authorized. Do not permanently delete until confirmed.</span>
    </div>
  </div>

  <div class="trash-group">
    <h4 class="trash-review">🟡 Review Before Deleting (1)</h4>
    <div class="trash-item">
      <strong>Meidas+ &lt;meidastouch@substack.com&gt;</strong> — "You Can't Be What You Can't See: Maura Sullivan's Story"<br>
      <span style="color:#4a5568;">A Meidas+ newsletter/video about women in military (Pete Hegseth / Hell Cats). You moved this to Trash, likely intentional. If you were reading content and accidentally deleted, restore. Otherwise, safe to permanently delete. Note: A duplicate Meidas+ email ("Ok, last chance...") exists outside Trash — consider unsubscribing from both.</span>
    </div>
  </div>

  <div class="trash-group">
    <h4 class="trash-delete">⚪ Safe to Delete (1)</h4>
    <div class="trash-item">
      <strong>Amazon Prime Day &lt;store-news@amazon.com&gt;</strong> — "Final hours of Prime Day! Save 50% or more on our Top 125+ deals."<br>
      <span style="color:#4a5568;">Prime Day promotional email. Time-sensitive deals have likely passed. Safe to permanently delete.</span>
    </div>
  </div>
</div>

<!-- ═══════════════════════════ 8. PROMOTIONAL / RETAIL SUMMARY ═══════════════════════════ -->
<div class="section band-gray">
  <div class="section-title">🛍️ Promotional / Retail Summary</div>
  <table class="promo-table">
    <thead>
      <tr>
        <th>Sender / Brand</th>
        <th>Count</th>
        <th>Subject / Theme</th>
        <th>Recommendation</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>SHEIN</strong></td>
        <td>3</td>
        <td>"Under $10 Drops" (×2 from diff domains) + "All under $13.99 | Curvy, Chic, Hot!" — duplicate sends from two SHEIN addresses</td>
        <td><span class="rec-delete">Delete / Unsubscribe</span> — duplicate sends; one domain appears suspicious</td>
      </tr>
      <tr>
        <td><strong>Temu</strong></td>
        <td>2</td>
        <td>Matching set $11.24 (orig $48.99) + Two-piece fashion ($19.65, 43 left)</td>
        <td><span class="rec-ignore">Ignore</span> — if no current shopping need, delete</td>
      </tr>
      <tr>
        <td><strong>Gap Factory</strong></td>
        <td>1</td>
        <td>Fourth of July sale: 50–70% off</td>
        <td><span class="rec-review">Review</span> — if summer wardrobe refresh needed</td>
      </tr>
      <tr>
        <td><strong>Kohl's</strong></td>
        <td>1</td>
        <td>Daily Deals · Free Shipping · Kohl's Cash · up to 75% clearance</td>
        <td><span class="rec-ignore">Ignore</span> — standard promo</td>
      </tr>
      <tr>
        <td><strong>Old Navy</strong></td>
        <td>1</td>
        <td>Sweet summer arrivals from $10 · Free Shipping for Encore Members $50+</td>
        <td><span class="rec-ignore">Ignore</span> — not in inbox, low priority</td>
      </tr>
<hr>
<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Financial / Billing</td><td>2</td></tr>
<tr><td>Job Search / Recruiters</td><td>9</td></tr>
<tr><td>Other / Review</td><td>27</td></tr>
<tr><td>Professional Development / Newsletters</td><td>4</td></tr>
<tr><td>Promotional / Retail</td><td>5</td></tr>
<tr><td>Security / Risk</td><td>3</td></tr>
</table>
<p><strong>Audit Note:</strong> Every fetched email was reviewed and assigned to one category. Trash emails were included in review. Promotional and low-value emails were accounted for but deprioritized.</p>

