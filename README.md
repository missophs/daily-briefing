<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing – Melissa Weiss | June 30, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* Header */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 16px; padding: 36px 40px 28px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 15px; color: #a8b4c8; margin-top: 4px; }
  .header .meta { display: flex; gap: 32px; margin-top: 20px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 18px; }
  .header .meta-item .label { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #a8b4c8; }
  .header .meta-item .value { font-size: 20px; font-weight: 700; color: #e2e8f0; }

  /* Section containers */
  .section { background: #fff; border-radius: 12px; padding: 24px 28px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .section-title { font-size: 17px; font-weight: 700; border-bottom: 2px solid #e8ecf0; padding-bottom: 10px; margin-bottom: 18px; display: flex; align-items: center; gap: 8px; }
  .section-title .icon { font-size: 20px; }

  /* Color bands */
  .band-red { border-left: 5px solid #e53e3e; }
  .band-yellow { border-left: 5px solid #d69e2e; }
  .band-blue { border-left: 5px solid #3182ce; }
  .band-green { border-left: 5px solid #38a169; }
  .band-purple { border-left: 5px solid #805ad5; }
  .band-gray { border-left: 5px solid #a0aec0; }

  /* Exec summary bullets */
  .exec-bullet { display: flex; align-items: flex-start; gap: 12px; padding: 12px 16px; border-radius: 8px; margin-bottom: 10px; }
  .exec-bullet.risk { background: #fff5f5; border: 1px solid #fed7d7; }
  .exec-bullet.opp { background: #f0fff4; border: 1px solid #c6f6d5; }
  .exec-bullet.cal { background: #ebf8ff; border: 1px solid #bee3f8; }
  .exec-bullet .eb-icon { font-size: 22px; flex-shrink: 0; margin-top: 1px; }
  .exec-bullet .eb-text strong { display: block; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 2px; }

  /* Action cards */
  .action-card { border-radius: 10px; padding: 16px 20px; margin-bottom: 14px; }
  .action-card.red { background: #fff5f5; border: 1px solid #fc8181; }
  .action-card.yellow { background: #fffff0; border: 1px solid #f6e05e; }
  .action-card.green { background: #f0fff4; border: 1px solid #68d391; }
  .action-card.blue { background: #ebf8ff; border: 1px solid #90cdf4; }
  .action-card.purple { background: #faf5ff; border: 1px solid #d6bcfa; }
  .action-card .ac-label { display: inline-block; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; padding: 2px 8px; border-radius: 20px; margin-bottom: 6px; }
  .label-red { background: #e53e3e; color: #fff; }
  .label-yellow { background: #d69e2e; color: #fff; }
  .label-green { background: #38a169; color: #fff; }
  .label-blue { background: #3182ce; color: #fff; }
  .label-purple { background: #805ad5; color: #fff; }
  .label-gray { background: #718096; color: #fff; }
  .ac-title { font-size: 15px; font-weight: 700; margin-bottom: 6px; }
  .ac-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 4px 16px; font-size: 13px; }
  .ac-grid .field { color: #718096; font-weight: 600; }
  .ac-grid .value { color: #2d3748; }
  .ac-next { margin-top: 10px; background: rgba(0,0,0,0.04); border-radius: 6px; padding: 8px 12px; font-size: 13px; }
  .ac-next strong { color: #2d3748; }

  /* Calendar */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #3182ce; background: #ebf8ff; padding: 6px 14px; border-radius: 6px; margin-bottom: 8px; }
  .cal-event { display: grid; grid-template-columns: 130px 1fr; gap: 10px; padding: 10px 14px; border-radius: 8px; margin-bottom: 6px; background: #f7fafc; border: 1px solid #e2e8f0; }
  .cal-time { font-weight: 700; font-size: 13px; color: #3182ce; }
  .cal-name { font-weight: 700; font-size: 14px; }
  .cal-detail { font-size: 12px; color: #718096; margin-top: 2px; }
  .status-badge { display: inline-block; font-size: 10px; font-weight: 700; text-transform: uppercase; padding: 2px 8px; border-radius: 20px; margin-left: 6px; }
  .status-confirmed { background: #c6f6d5; color: #276749; }
  .status-needs { background: #feebc8; color: #7b341e; }
  .status-declined { background: #fed7d7; color: #742a2a; }
  .conflict-warn { background: #fff5f5; border: 1px solid #fc8181; border-radius: 6px; padding: 4px 10px; font-size: 12px; color: #c53030; margin-top: 4px; display: inline-block; }

  /* Tables */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #edf2f7; color: #4a5568; text-transform: uppercase; letter-spacing: 0.5px; font-size: 11px; padding: 8px 12px; text-align: left; }
  td { padding: 8px 12px; border-bottom: 1px solid #e8ecf0; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f7fafc; }

  /* Priority badges */
  .pri-high { background: #e53e3e; color: #fff; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 20px; }
  .pri-med { background: #d69e2e; color: #fff; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 20px; }
  .pri-low { background: #a0aec0; color: #fff; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 20px; }
  .fit-high { background: #38a169; color: #fff; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 20px; }
  .fit-med { background: #3182ce; color: #fff; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 20px; }
  .fit-low { background: #a0aec0; color: #fff; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 20px; }

  /* Category cards */
  .cat-card { padding: 14px 18px; border-radius: 8px; margin-bottom: 12px; border: 1px solid #e2e8f0; }
  .cat-card .cat-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px; }
  .cat-card .cat-name { font-weight: 700; font-size: 14px; }
  .cat-card .cat-count { font-size: 12px; background: #edf2f7; padding: 2px 8px; border-radius: 12px; font-weight: 600; }
  .cat-card .cat-body { font-size: 13px; color: #4a5568; }
  .cat-card .cat-action { margin-top: 6px; font-size: 12px; font-style: italic; color: #718096; }

  .cat-red { background: #fff5f5; border-color: #fc8181; }
  .cat-green { background: #f0fff4; border-color: #68d391; }
  .cat-blue { background: #ebf8ff; border-color: #90cdf4; }
  .cat-yellow { background: #fffff0; border-color: #f6e05e; }
  .cat-purple { background: #faf5ff; border-color: #d6bcfa; }
  .cat-gray { background: #f7fafc; border-color: #cbd5e0; }
  .cat-pink { background: #fff5f7; border-color: #fed7e2; }

  /* Dashboard grid */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-tile { border-radius: 10px; padding: 16px 18px; }
  .dash-tile .dt-label { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; font-weight: 700; margin-bottom: 6px; }
  .dash-tile .dt-value { font-size: 26px; font-weight: 800; }
  .dash-tile .dt-sub { font-size: 12px; margin-top: 4px; color: #718096; }
  .dt-red { background: #fff5f5; border: 1px solid #fc8181; }
  .dt-red .dt-label { color: #c53030; }
  .dt-red .dt-value { color: #e53e3e; }
  .dt-yellow { background: #fffff0; border: 1px solid #f6e05e; }
  .dt-yellow .dt-label { color: #b7791f; }
  .dt-yellow .dt-value { color: #d69e2e; }
  .dt-blue { background: #ebf8ff; border: 1px solid #90cdf4; }
  .dt-blue .dt-label { color: #2b6cb0; }
  .dt-blue .dt-value { color: #3182ce; }
  .dt-green { background: #f0fff4; border: 1px solid #68d391; }
  .dt-green .dt-label { color: #276749; }
  .dt-green .dt-value { color: #38a169; }
  .dt-purple { background: #faf5ff; border: 1px solid #d6bcfa; }
  .dt-purple .dt-label { color: #553c9a; }
  .dt-purple .dt-value { color: #805ad5; }
  .dt-gray { background: #f7fafc; border: 1px solid #cbd5e0; }
  .dt-gray .dt-label { color: #4a5568; }
  .dt-gray .dt-value { color: #718096; }

  /* Top 3 priorities */
  .priority-card { display: flex; gap: 16px; align-items: flex-start; padding: 18px 20px; border-radius: 10px; margin-bottom: 12px; }
  .priority-card.p1 { background: linear-gradient(135deg, #fff5f5, #ffe); border: 1px solid #fc8181; }
  .priority-card.p2 { background: linear-gradient(135deg, #f0fff4, #ebf8ff); border: 1px solid #68d391; }
  .priority-card.p3 { background: linear-gradient(135deg, #faf5ff, #ebf8ff); border: 1px solid #d6bcfa; }
  .priority-num { font-size: 36px; font-weight: 900; opacity: 0.15; flex-shrink: 0; line-height: 1; }
  .priority-text h3 { font-size: 16px; font-weight: 700; margin-bottom: 4px; }
  .priority-text p { font-size: 13px; color: #4a5568; }

  /* Trash section */
  .trash-group { margin-bottom: 16px; }
  .trash-group-title { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px; padding: 4px 10px; border-radius: 4px; display: inline-block; }
  .tg-restore { background: #c6f6d5; color: #276749; }
  .tg-review { background: #feebc8; color: #7b341e; }
  .tg-delete { background: #e2e8f0; color: #4a5568; }
  .trash-item { padding: 8px 12px; border-radius: 6px; margin-bottom: 5px; font-size: 13px; border: 1px solid #e2e8f0; background: #fafafa; }
  .trash-item .ti-sender { font-weight: 600; }
  .trash-item .ti-reason { color: #718096; font-size: 12px; }

  /* Newsletter pills */
  .nl-pill { display: inline-block; font-size: 11px; padding: 3px 10px; border-radius: 20px; margin: 2px; }
  .nl-keep { background: #c6f6d5; color: #276749; }
  .nl-review { background: #bee3f8; color: #2b6cb0; }
  .nl-unsub { background: #fed7d7; color: #742a2a; }
  .nl-delete { background: #e2e8f0; color: #4a5568; }

  /* Accounting table highlight */
  .acct-total td { background: #edf2f7; font-weight: 700; }

  /* Spam warning */
  .spam-banner { background: #742a2a; color: #fff; padding: 12px 18px; border-radius: 8px; margin-bottom: 14px; font-size: 13px; }
  .spam-banner strong { font-size: 14px; }

  /* Responsive */
  @media (max-width: 700px) {
    .header { padding: 20px; }
    .ac-grid { grid-template-columns: 1fr; }
    .cal-event { grid-template-columns: 1fr; }
    .dash-grid { grid-template-columns: 1fr 1fr; }
  }

  hr.divider { border: none; border-top: 1px solid #e2e8f0; margin: 18px 0; }
  .tag { display: inline-block; font-size: 11px; padding: 2px 8px; border-radius: 12px; background: #edf2f7; color: #4a5568; margin: 2px; }
  .unread-dot { display: inline-block; width: 7px; height: 7px; border-radius: 50%; background: #e53e3e; margin-right: 4px; vertical-align: middle; }
  a { color: #3182ce; text-decoration: none; }
  a:hover { text-decoration: underline; }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 1. HEADER -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="header">
  <h1>🌅 Good Morning, Melissa!</h1>
  <div class="subtitle">Executive Briefing &nbsp;·&nbsp; Tuesday, June 30, 2026</div>
  <div class="meta">
    <div class="meta-item">
      <div class="label">Total Emails Reviewed</div>
      <div class="value">50</div>
    </div>
    <div class="meta-item">
      <div class="label">Calendar Events</div>
      <div class="value">5</div>
    </div>
    <div class="meta-item">
      <div class="label">Action Required</div>
      <div class="value">7</div>
    </div>
    <div class="meta-item">
      <div class="label">Security Alerts</div>
      <div class="value">🔴 4</div>
    </div>
    <div class="meta-item">
      <div class="label">Upcoming Events (7 days)</div>
      <div class="value">5</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 2. EXECUTIVE SUMMARY -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section band-red">
  <div class="section-title"><span class="icon">⚡</span> Executive Summary</div>

  <div class="exec-bullet risk">
    <div class="eb-icon">🚨</div>
    <div class="eb-text">
      <strong>Biggest Risk / Urgent Item</strong>
      Your inbox contains 4 high-risk security threats today: two phishing/spam emails spoofing your own address (melissaw212@gmail.com) — one with explicit content, one a cloud-storage scam — plus a fake CashApp payment notification and a suspicious Bilt "new login" alert. Delete all immediately and verify your Bilt account was not compromised.
    </div>
  </div>

  <div class="exec-bullet opp">
    <div class="eb-icon">🌟</div>
    <div class="eb-text">
      <strong>Biggest Job Search / Opportunity Item</strong>
      LinkedIn is surfacing a Sr. HR Director role paying up to $350K/year, and Michael De Jongh sent you a message on LinkedIn awaiting reply. The HR Networking & Job Search Group meets tomorrow (July 1) on Zoom — you have not yet RSVPed. These three items together represent your highest-value job search actions this week.
    </div>
  </div>

  <div class="exec-bullet cal">
    <div class="eb-icon">📅</div>
    <div class="eb-text">
      <strong>Biggest Calendar / Deadline Item</strong>
      You have two HR Networking Zoom sessions this week (July 1 & July 2) still awaiting your RSVP. The Executive Roundtable on July 2 (hosted by John Madigan) is currently marked <em>declined</em> — confirm that is intentional. Your State Farm bill is due July 7. Hilton Honors double-points promo ends July 24 — worth noting if any travel is planned.
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 3. ACTION REQUIRED -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section band-red">
  <div class="section-title"><span class="icon">✅</span> Action Required</div>

  <!-- SECURITY -->
  <div class="spam-banner">
    ⚠️ <strong>SPAM / PHISHING ALERT:</strong> Four emails in your mailbox are confirmed malicious or high-risk. Do NOT click any links. Mark as phishing and delete.
  </div>

  <div class="action-card red">
    <div class="ac-label label-red">🔴 Security – Critical</div>
    <div class="ac-title">Phishing: Fake "WATCH THIS" Email from Spoofed Address</div>
    <div class="ac-grid">
      <span class="field">Source:</span><span class="value">melissaw212 &lt;iywwrhrovynvro…@2ha1tb…&gt; (spoofed)</span>
      <span class="field">Why It Matters:</span><span class="value">Your email address is being spoofed to deliver explicit phishing spam. This indicates your address may be on a spam list.</span>
      <span class="field">Due:</span><span class="value">Immediately</span>
    </div>
    <div class="ac-next"><strong>Next Step:</strong> Mark as phishing, delete. Check Gmail "sent" folder for any unauthorized activity. Consider enabling 2FA if not already active.</div>
  </div>

  <div class="action-card red">
    <div class="ac-label label-red">🔴 Security – Critical</div>
    <div class="ac-title">Phishing: Fake CashApp Payment "$13,963.99"</div>
    <div class="ac-grid">
      <span class="field">Source:</span><span class="value">"💸CASHAPP💸" &lt;fksjtpsuovh@oqyn…&gt; (spoofed/phishing)</span>
      <span class="field">Why It Matters:</span><span class="value">Classic lottery/casino payment phishing scam. Clicking any link could compromise financial or personal data.</span>
      <span class="field">Due:</span><span class="value">Immediately</span>
    </div>
    <div class="ac-next"><strong>Next Step:</strong> Do NOT click. Mark as phishing, delete permanently.</div>
  </div>

  <div class="action-card red">
    <div class="ac-label label-red">🔴 Security – Critical</div>
    <div class="ac-title">Phishing: Fake "Cloud Account Locked" from Spoofed Address</div>
    <div class="ac-grid">
      <span class="field">Source:</span><span class="value">melissaw212 &lt;opxfbiadgldqmn…@9to5w6…&gt; (spoofed)</span>
      <span class="field">Why It Matters:</span><span class="value">Creates false urgency about cloud storage to harvest credentials.</span>
      <span class="field">Due:</span><span class="value">Immediately</span>
    </div>
    <div class="ac-next"><strong>Next Step:</strong> Mark as phishing, delete permanently. Do not visit any linked site.</div>
  </div>

  <div class="action-card red">
    <div class="ac-label label-red">🔴 Security – High</div>
    <div class="ac-title">Bilt: New Login on Your Account</div>
    <div class="ac-grid">
      <span class="field">Source:</span><span class="value">Bilt &lt;no-reply@alerts.bilt.com&gt;</span>
      <span class="field">Why It Matters:</span><span class="value">A new login was detected on your Bilt account. Rent payment is processing simultaneously — if account was accessed by bad actor, financial exposure is possible.</span>
      <span class="field">Due:</span><span class="value">Today</span>
    </div>
    <div class="ac-next"><strong>Next Step:</strong> Log into Bilt directly (not via this email link) and verify login activity. Change password if unrecognized. Confirm rent payment status.</div>
  </div>

  <div class="action-card yellow">
    <div class="ac-label label-yellow">🟡 RSVP Needed</div>
    <div class="ac-title">HR Networking & Job Search Group – Zoom (July 1)</div>
    <div class="ac-grid">
      <span class="field">Source:</span><span class="value">Google Calendar</span>
      <span class="field">Why It Matters:</span><span class="value">Status is "Needs Action" — you have not confirmed. Large group networking call (150+ attendees). Key job search resource.</span>
      <span class="field">Due:</span><span class="value">Tomorrow, July 1 · 12:00–1:30 PM ET</span>
    </div>
    <div class="ac-next"><strong>Next Step:</strong> Accept or decline the calendar invite now. Add Zoom link to calendar notes.</div>
  </div>

  <div class="action-card yellow">
    <div class="ac-label label-yellow">🟡 RSVP Needed</div>
    <div class="ac-title">HR Networking & Job Search: Open Office Hours – Zoom (July 2)</div>
    <div class="ac-grid">
      <span class="field">Source:</span><span class="value">Google Calendar</span>
      <span class="field">Why It Matters:</span><span class="value">Status is "Needs Action." Note reminder: AI notetaking tools must be turned off per organizer instructions.</span>
      <span class="field">Due:</span><span class="value">July 2 · 12:00–1:00 PM ET</span>
    </div>
    <div class="ac-next"><strong>Next Step:</strong> Accept or decline. If attending, disable AI recording tools before the call.</div>
  </div>

  <div class="action-card green">
    <div class="ac-label label-green">🟢 Job Search</div>
    <div class="ac-title">LinkedIn Message from Michael De Jongh – Awaiting Reply</div>
    <div class="ac-grid">
      <span class="field">Source:</span><span class="value">LinkedIn messaging digest</span>
      <span class="field">Why It Matters:</span><span class="value">A real person reached out on LinkedIn. Unanswered professional messages reduce network responsiveness and may represent an opportunity.</span>
      <span class="field">Due:</span><span class="value">Today or tomorrow</span>
    </div>
    <div class="ac-next"><strong>Next Step:</strong> Open LinkedIn and respond to Michael De Jongh. Review his profile before replying to tailor your response.</div>
  </div>

  <div class="action-card yellow">
    <div class="ac-label label-yellow">🟡 Billing</div>
    <div class="ac-title">State Farm Bill Due July 7</div>
    <div class="ac-grid">
      <span class="field">Source:</span><span class="value">Google Calendar (reminder event)</span>
      <span class="field">Why It Matters:</span><span class="value">Insurance bill deadline. Missing it could result in a lapse in coverage.</span>
      <span class="field">Due:</span><span class="value">July 7, 2026</span>
    </div>
    <div class="ac-next"><strong>Next Step:</strong> Schedule or confirm payment before July 7. Set a calendar reminder for July 5 if needed.</div>
  </div>

  <div class="action-card yellow">
    <div class="ac-label label-yellow">🟡 Medical</div>
    <div class="ac-title">Stella's Vet Visit Is Due (Center for Veterinary Care)</div>
    <div class="ac-grid">
      <span class="field">Source:</span><span class="value">Center for Veterinary Care / Vetspire</span>
      <span class="field">Why It Matters:</span><span class="value">Stella (pet) is due for a health visit. Routine preventive care keeps her in good health and avoids more costly urgent care later.</span>
      <span class="field">Due:</span><span class="value">Soon — schedule this week</span>
    </div>
    <div class="ac-next"><strong>Next Step:</strong> Call the Center for Veterinary Care to schedule Stella's appointment.</div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 4. FULL 7-DAY CALENDAR -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section band-blue">
  <div class="section-title"><span class="icon">📅</span> Full 7-Day Calendar &nbsp;<span style="font-size:12px;font-weight:400;color:#718096;">(June 30 – July 6, 2026)</span></div>

  <!-- Tuesday June 30 -->
  <div class="cal-day">
    <div class="cal-day-header">📆 Tuesday, June 30, 2026 — TODAY</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div>
        <div class="cal-name">No calendar events scheduled today</div>
        <div class="cal-detail">Use today to respond to security threats, reply to LinkedIn message, and RSVP to tomorrow's networking call.</div>
      </div>
    </div>
  </div>

  <!-- Wednesday July 1 -->
  <div class="cal-day">
    <div class="cal-day-header">📆 Wednesday, July 1, 2026</div>

    <div class="cal-event">
      <div class="cal-time">12:00 PM – 1:30 PM ET</div>
      <div>
        <div class="cal-name">HR Networking &amp; Job Search Group – Zoom 2 <span class="status-badge status-needs">⚠️ Needs RSVP</span></div>
        <div class="cal-detail">📍 <a href="https://us06web.zoom.us/j/81954171722" target="_blank">Zoom Link</a> &nbsp;|&nbsp; ~170+ attendees</div>
        <div class="cal-detail">⚙️ <strong>Prep:</strong> Review HR Networking Team Guidelines (link in calendar description). Prepare a 30-second intro / status update on your search.</div>
        <div class="cal-detail">📋 <strong>Status:</strong> Needs Action — RSVP immediately.</div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">12:00 PM – 1:30 PM ET</div>
      <div>
        <div class="cal-name">Network <span class="status-badge status-confirmed">✅ Confirmed</span></div>
        <div class="cal-detail">📍 No location specified &nbsp;|&nbsp; No attendees listed (personal block)</div>
        <div class="cal-detail">⚙️ <strong>Prep:</strong> May overlap with HR Networking Zoom above — confirm this is a separate event or a placeholder block.</div>
        <div class="cal-detail"><span class="conflict-warn">⚠️ Potential time conflict with HR Networking Zoom (same 12:00–1:30 PM slot)</span></div>
      </div>
    </div>
  </div>

  <!-- Thursday July 2 -->
  <div class="cal-day">
    <div class="cal-day-header">📆 Thursday, July 2, 2026</div>

    <div class="cal-event">
      <div class="cal-time">9:00 AM – 10:30 AM ET</div>
      <div>
        <div class="cal-name">Executive Roundtable (John Madigan) <span class="status-badge status-declined">❌ Declined</span></div>
        <div class="cal-detail">📍 <a href="https://us02web.zoom.us/j/207786667" target="_blank">Zoom Link</a> &nbsp;|&nbsp; Meeting ID: 207 786 667 &nbsp;|&nbsp; PW: 205454</div>
        <div class="cal-detail">⚙️ <strong>Prep:</strong> None needed if decline is intentional. Consider whether this is a valuable networking opportunity and if you'd like to re-accept.</div>
        <div class="cal-detail">📋 <strong>Note:</strong> Verify your declination was intentional — Executive Roundtables may carry significant networking value.</div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">12:00 PM – 1:00 PM ET</div>
      <div>
        <div class="cal-name">HR Networking &amp; Job Search: Open Office Hours – Zoom 2 <span class="status-badge status-needs">⚠️ Needs RSVP</span></div>
        <div class="cal-detail">📍 <a href="https://us06web.zoom.us/j/85945371140" target="_blank">Zoom Link</a> &nbsp;|&nbsp; ~170+ attendees</div>
        <div class="cal-detail">⚙️ <strong>Prep:</strong> Have specific questions ready. Turn off all AI notetaking tools per organizer request (Otter, Fireflies, etc.).</div>
        <div class="cal-detail">📋 <strong>Status:</strong> Needs Action — RSVP required.</div>
      </div>
    </div>
  </div>

  <!-- Friday July 3 -->
  <div class="cal-day">
    <div class="cal-day-header">📆 Friday, July 3, 2026</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div>
        <div class="cal-name">No calendar events scheduled</div>
        <div class="cal-detail">Day before Independence Day. Good day to prep for the holiday weekend or do focused job search work.</div>
      </div>
    </div>
  </div>

  <!-- Saturday July 4 -->
  <div class="cal-day">
    <div class="cal-day-header">🇺🇸 Saturday, July 4, 2026 — Independence Day</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div>
        <div class="cal-name">No calendar events scheduled</div>
        <div class="cal-detail">Federal holiday. Most professional contacts will be unavailable.</div>
      </div>
    </div>
  </div>

  <!-- Sunday July 5 -->
  <div class="cal-day">
    <div class="cal-day-header">📆 Sunday, July 5, 2026</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div>
        <div class="cal-name">No calendar events scheduled</div>
        <div class="cal-detail">Weekend. Suggested: Review job pipeline and prep for the following week.</div>
      </div>
    </div>
  </div>

  <!-- Monday July 6 -->
  <div class="cal-day">
    <div class="cal-day-header">📆 Monday, July 6, 2026</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div>
        <div class="cal-name">No calendar events scheduled</div>
        <div class="cal-detail">First business day after July 4th holiday. Great day to reconnect with recruiters and follow up on applications.</div>
      </div>
    </div>
  </div>

  <!-- Tuesday July 7 -->
  <div class="cal-day">
    <div class="cal-day-header">📆 Tuesday, July 7, 2026 — ⚠️ BILL DUE</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div>
        <div class="cal-name">🧾 State Farm Bill Due <span class="status-badge status-confirmed">📅 Reminder Set</span></div>
        <div class="cal-detail">⚙️ <strong>Prep:</strong> Confirm payment method. Pay by July 6 to avoid any processing delays.</div>
      </div>
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 5. JOB SEARCH & INTERVIEW PIPELINE -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section band-green">
  <div class="section-title"><span class="icon">💼</span> Job Search &amp; Interview Pipeline</div>

  <table>
    <thead>
      <tr>
        <th>Type</th>
        <th>Source / Sender</th>
        <th>Details</th>
        <th>Fit</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="tag">🔔 Job Alert</span></td>
        <td>LinkedIn Job Alerts</td>
        <td><strong>Sr. Human Resources Director</strong> at Confidential Company &nbsp;|&nbsp; Up to <strong>$350K/year</strong> &nbsp;|&nbsp; Posted 6/28/2026</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>Review the posting immediately; apply or save. This is top-tier compensation for an HR Director role.</td>
      </tr>
      <tr>
        <td><span class="tag">💬 LinkedIn Message</span></td>
        <td>Michael De Jongh via LinkedIn</td>
        <td>1 new LinkedIn message awaiting reply. Nature of message unknown — could be recruiter, referral, or peer outreach.</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>Open LinkedIn and respond today. Profile review recommended before replying.</td>
      </tr>
      <tr>
        <td><span class="tag">🤝 Networking</span></td>
        <td>HR Networking Group (Calendar)</td>
        <td>HR Networking &amp; Job Search Group Zoom – July 1 &nbsp;|&nbsp; 12:00–1:30 PM &nbsp;|&nbsp; 170+ HR professionals</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>RSVP today. Prepare brief status update on your search. Review team guidelines before attending.</td>
      </tr>
      <tr>
        <td><span class="tag">🤝 Networking</span></td>
        <td>HR Networking Group (Calendar)</td>
        <td>Open Office Hours – July 2 &nbsp;|&nbsp; 12:00–1:00 PM &nbsp;|&nbsp; Small-group open discussion format</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>RSVP today. Prepare targeted questions. Disable AI notetaking tools.</td>
      </tr>
      <tr>
        <td><span class="tag">🏛️ Roundtable</span></td>
        <td>John Madigan (Calendar)</td>
        <td>Executive Roundtable – July 2 &nbsp;|&nbsp; 9:00–10:30 AM &nbsp;|&nbsp; Currently <strong>Declined</strong></td>
        <td><span class="fit-med">MEDIUM</span></td>
        <td>Reconsider whether to attend — Executive Roundtables often carry meaningful peer-level networking value for senior HR professionals.</td>
      </tr>
      <tr>
        <td><span class="tag">📖 Career Dev</span></td>
        <td>Level Up Newsletter (Substack)</td>
        <td>"Executive Presence: Own the Room, Be Heard, Get Credit" — directly relevant to senior leadership positioning</td>
        <td><span class="fit-med">MEDIUM</span></td>
        <td>Read when time permits. Valuable prep for executive interviews.</td>
      </tr>
      <tr>
        <td><span class="tag">📊 AI/HR Insight</span></td>
        <td>PromptMates Newsletter</td>
        <td>"Workers Using AI Survived Layoffs at 3x the Rate" — relevant to HR strategy &amp; AI adoption in the workplace</td>
        <td><span class="fit-med">MEDIUM</span></td>
        <td>Read for talking points in interviews and professional conversations.</td>
      </tr>
      <tr>
        <td><span class="tag">💡 Tools</span></td>
        <td>Jeff Su / Gemini Spark</td>
        <td>Beginner-friendly AI agent overview — relevant if exploring AI tools for HR workflow or job search</td>
        <td><span class="fit-low">LOW</span></td>
        <td>Review when convenient. Low urgency.</td>
      </tr>
      <tr>
        <td><span class="tag">📢 Sponsored</span></td>
        <td>SHRM / Software Advice</td>
        <td>LMS Pricing Guide for 2026 — useful if evaluating learning management systems in HR role</td>
        <td><span class="fit-low">LOW</span></td>
        <td>Save for reference if relevant to your current or target HR role scope. Otherwise delete.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 6. FULL EMAIL REVIEW BY CATEGORY -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">📬</span> Full Email Review by Category</div>

  <!-- Security / Risk -->
  <div class="cat-card cat-red">
    <div class="cat-header">
      <div class="cat-name">🔴 Security / Risk</div>
      <div class="cat-count">4 emails</div>
    </div>
    <div class="cat-body">
      <strong>Senders:</strong> melissaw212 (spoofed, phishing – explicit), "💸CASHAPP💸" (phishing – fake payment), melissaw212 (spoofed, phishing – fake cloud warning), Bilt (new login alert – legitimate but warrants investigation)<br>
      <strong>Summary:</strong> Three confirmed phishing/spam emails spoofing your identity or known brands. One legitimate security alert from Bilt regarding a new account login occurring simultaneously with a rent payment processing.
    </div>
    <div class="cat-action">⚡ Immediate: Delete the three phishing emails. Verify your Bilt account manually.</div>
  </div>

  <!-- Job Search -->
  <div class="cat-card cat-green">
    <div class="cat-header">
      <div class="cat-name">🟢 Job Search</div>
      <div class="cat-count">1 email</div>
    </div>
    <div class="cat-body">
      <strong>Sender:</strong> LinkedIn Job Alerts<br>
      <strong>Summary:</strong> Sr. Human Resources Director role at a confidential company — up to $350K/year. Posted 6/28/2026.
    </div>
    <div class="cat-action">✅ Review and apply if qualified. High-value opportunity.</div>
  </div>

  <!-- Recruiters / Networking -->
  <div class="cat-card cat-green">
    <div class="cat-header">
      <div class="cat-name">🟢 Recruiters / Networking</div>
      <div class="cat-count">1 email</div>
    </div>
    <div class="cat-body">
      <strong>Sender:</strong> Michael De Jongh via LinkedIn<br>
      <strong>Summary:</strong> A LinkedIn contact sent 1 message awaiting response. Content unknown — likely professional outreach.
    </div>
    <div class="cat-action">✅ Reply on LinkedIn today. Do not leave professional messages unanswered for more than 24 hours.</div>
  </div>

  <!-- Calendar / Events -->
  <div class="cat-card cat-blue">
    <div class="cat-header">
      <div class="cat-name">🔵 Calendar / Events</div>
      <div class="cat-count">0 emails</div>
    </div>
    <div class="cat-body">No calendar-related emails in inbox today. All event data came directly from Google Calendar.</div>
    <div class="cat-action">ℹ️ No action needed from email.</div>
  </div>

  <!-- Medical / Health -->
  <div class="cat-card cat-pink">
    <div class="cat-header">
      <div class="cat-name">🩺 Medical / Health</div>
      <div class="cat-count">1 email</div>
    </div>
    <div class="cat-body">
      <strong>Sender:</strong> Center for Veterinary Care (Vetspire)<br>
      <strong>Subject:</strong> "Health Reminder for Stella"<br>
      <strong>Summary:</strong> Stella (the Weiss family pet) is due for a wellness visit at the vet.
    </div>
    <div class="cat-action">📞 Call to schedule Stella's appointment this week.</div>
  </div>

  <!-- Financial / Billing -->
  <div class="cat-card cat-yellow">
    <div class="cat-header">
      <div class="cat-name">🟡 Financial / Billing</div>
      <div class="cat-count">2 emails</div>
    </div>
    <div class="cat-body">
      <strong>Senders:</strong> Bilt (rent payment processing), State Farm bill (calendar reminder)<br>
      <strong>Summary:</strong> Bilt rent payment is processing and earning up to 1.25X points. State Farm bill due July 7 per calendar event. (Note: The Bilt payment email was in trash — this may mean it was auto-filed there, but the alert email about a new login was flagged separately.)
    </div>
    <div class="cat-action">✅ Verify rent payment processed correctly via Bilt. Pay State Farm bill before July 7.</div>
  </div>

  <!-- Professional Development -->
  <div class="cat-card cat-purple">
    <div class="cat-header">
      <div class="cat-name">🟣 Professional Development</div>
      <div class="cat-count">7 emails</div>
    </div>
    <div class="cat-body">
      <strong>Senders:</strong> Jeff Su (Gemini Spark AI agent), PromptMates (×2 – AI &amp; layoffs), SHRM/Software Advice (LMS Pricing Guide), Level Up Newsletter (Executive Presence), the co-lab (pay cut advice), Medium/Pranit Naik (AI regulation)<br>
      <strong>Summary:</strong> Mix of AI tools education, HR/career advice, and industry news. Two PromptMates copies are duplicates.
    </div>
    <div class="cat-action">📖 Prioritize: Level Up (Executive Presence), PromptMates (AI survival data). Delete PromptMates duplicate. Archive SHRM sponsored message unless LMS is relevant.</div>
  </div>

  <!-- Personal (sent by Melissa) -->
  <div class="cat-card cat-gray">
    <div class="cat-header">
      <div class="cat-name">👤 Personal (Sent by Melissa)</div>
      <div class="cat-count">2 emails</div>
    </div>
    <div class="cat-body">
      <strong>Senders:</strong> melissa &lt;melissaw212@gmail.com&gt; (to self)<br>
      <strong>Subjects:</strong> "Re: linkedin viral" (Claude AI prompt for LinkedIn posts) and "ai agents" (LinkedIn post about 50 AI agent resources)<br>
      <strong>Summary:</strong> Self-sent notes/resources Melissa saved for herself — useful AI &amp; LinkedIn content she was collecting.
    </div>
    <div class="cat-action">📁 Archive or move to a "Resources" label. These are reference materials.</div>
  </div>

  <!-- Newsletters / Subscriptions -->
  <div class="cat-card cat-purple">
    <div class="cat-header">
      <div class="cat-name">📰 Newsletters / Subscriptions</div>
      <div class="cat-count">9 emails</div>
    </div>
    <div class="cat-body">
      <strong>Senders:</strong> Substack (new notes from Ruben Hassid &amp; Zach Williams), Medium Daily Digest (Substack-first strategy), TLDR Crypto (Clarity Act), TradeAlgo Daily Bulletin (in trash), Medium Daily Digest (Chinese AI – in trash), TLDR (iPhone 18 – in trash ×2), The Hustle (in trash), 1% Better (Cyborg Cockroaches / fun trivia)<br>
      <strong>Summary:</strong> Broad range of newsletters — finance, tech, AI, career. Several are in trash already. A few are duplicates.
    </div>
    <div class="cat-action">📬 Read Substack notes if time permits. Evaluate TLDR Crypto and TradeAlgo relevance — unsubscribe if not actively trading.</div>
  </div>

  <!-- Promotional / Retail -->
  <div class="cat-card cat-gray">
    <div class="cat-header">
      <div class="cat-name">🛍️ Promotional / Retail</div>
      <div class="cat-count">14 emails</div>
    </div>
    <div class="cat-body">
      <strong>Senders:</strong> ONE/SIZE Beauty (trash), Sephora (trash), Laura Geller ×2 (one inbox, one inbox – duplicate), Sierra Clearance, Halara, Zappos, Macy's (trash), Kulfi Beauty, SHEIN, Bed Bath &amp; Beyond (trash), Hilton Honors (trash), Target Optical (trash)<br>
      <strong>Summary:</strong> Heavy volume of retail promotions, predominantly beauty, fashion, and home goods. Many already in trash.
    </div>
    <div class="cat-action">🗑️ Most are safe to delete. Review Hilton Honors (100% bonus points promo ends July 24) if travel is planned. Delete Laura Geller duplicate.</div>
  </div>

  <!-- Trash Review -->
  <div class="cat-card cat-gray">
    <div class="cat-header">
      <div class="cat-name">🗑️ Trash Review</div>
      <div class="cat-count">23 emails in trash</div>
    </div>
    <div class="cat-body">See dedicated Trash Review section below for full breakdown.</div>
    <div class="cat-action">🔍 Several trash items reviewed below. Most are safe to permanently delete.</div>
  </div>

  <!-- Safe to Delete / Ignore -->
  <div class="cat-card cat-gray">
    <div class="cat-header">
      <div class="cat-name">⚫ Safe to Delete / Ignore (Not in Trash Yet)</div>
      <div class="cat-count">6 emails</div>
    </div>
    <div class="cat-body">
      <strong>Senders:</strong> Nextdoor (trending post), Nextdoor/Yorkville (event assistant – already in trash), OkCupid (someone likes you – in trash), Halara (not in inbox/trash — in promotions), melissaw212 phishing ×2, CASHAPP phishing<br>
      <strong>Summary:</strong> Phishing emails (already covered in security), Nextdoor trending post, OkCupid notification. Low value.
    </div>
    <div class="cat-action">🗑️ Delete. No action needed.</div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 7. TRASH REVIEW -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section band-gray">
  <div class="section-title"><span class="icon">🗑️</span> Trash Review</div>
  <p style="font-size:13px;color:#718096;margin-bottom:16px;">23 emails currently in Gmail Trash. Reviewed below — grouped by recommended action.</p>

  <!-- RESTORE -->
  <div class="trash-group">
    <div class="trash-group-title tg-restore">✅ Restore Immediately (1)</div>
    <div class="trash-item">
      <div class="ti-sender">Bilt — "New login on your Bilt account" &amp; "Your Bilt sign-in link"</div>
      <div class="ti-reason">⚠️ These are legitimate security notifications from Bilt (no-reply@alerts.bilt.com). While they may have been auto-trashed, you should review the new login alert to confirm it was you. Consider restoring or at minimum reading before permanent deletion. Also: "Your rent payment is processing" (Bilt) is in trash — verify the payment completed successfully.</div>
    </div>
  </div>

  <!-- REVIEW BEFORE DELETING -->
  <div class="trash-group">
    <div class="trash-group-title tg-review">🔍 Review Before Deleting (4)</div>
    <div class="trash-item">
      <div class="ti-sender">Hilton Honors — "Get 100% more Points until July 24"</div>
      <div class="ti-reason">If any travel is planned before July 24, this promo doubles your Honors points. Worth a 10-second check before deleting.</div>
    </div>
    <div class="trash-item">
      <div class="ti-sender">USPS Informed Delivery — "Your Daily Digest for Tue, 6/30"</div>
      <div class="ti-reason">1 mailpiece and 1 inbound package arriving. Worth checking if you're expecting anything. Then delete.</div>
    </div>
    <div class="trash-item">
      <div class="ti-sender">Nextdoor — "SLUMLORD in my building in LONG ISLAND CITY posted eviction..."</div>
      <div class="ti-reason">If you live in or near Long Island City, this may be relevant neighborhood news. Review if applicable, then delete.</div>
    </div>
    <div class="trash-item">
      <div class="ti-sender">Medium Daily Digest — "Six Months Into Going Substack-First: What Actually Happened"</div>
      <div class="ti-reason">If you're considering building a Substack or newsletter presence as part of your personal brand, this article is directly relevant. Otherwise safe to delete.</div>
    </div>
  </div>

  <!-- SAFE TO DELETE -->
  <div class="trash-group">
    <div class="trash-group-title tg-delete">🗑️ Safe to Delete Permanently (18)</div>
    <div class="trash-item">
      <div class="ti-sender">ONE/SIZE Beauty — "Oily girl holy grail!"</div>
      <div class="ti-reason">Beauty promotional email. No action needed.</div>
    </div>
    <div class="trash-item">
      <div class="ti-sender">Sephora Insider — "NEW and EXCLUSIVE: Your favorite soda, now a scent"</div>
      <div class="ti-reason">Retail promotion. No action needed.</div>
    </div>
    <div class="trash-item">
      <div class="ti-sender">TradeAlgo Daily Bulletin — "The dip-buyers are still winning"</div>
      <div class="ti-reason">Finance/trading newsletter. Already trashed. Safe to delete permanently.</div>
    </div>
    <div class="trash-item">
      <div class="ti-sender">Macy's — "July 4th Sale starts today—up to 60% off"</div>
      <div class="ti-reason">Retail promotion. Safe to delete.</div>
    </div>
    <div class="trash-item">
      <div class="ti-sender">Bed Bath &amp; Beyond — "Red, white &amp; rug deals"</div>
      <div class="ti-reason">Retail/home goods promotion. Safe to delete.</div>
    </div>
    <div class="trash-item">
      <div class="ti-sender">Target Optical — "Enjoy savings on PRECISION1® contact lenses"</div>
      <div class="ti-reason">Retail promotion. Safe to delete.</div>
    </div>
    <div class="trash-item">
      <div class="ti-sender">Hinge Team — "Jonathan liked you!"</div>
      <div class="ti-reason">Dating app notification. Already trashed. Safe to delete permanently.</div>
    </div>
    <div class="trash-item">
      <div class="ti-sender">Medium Daily Digest — "This New Chinese AI will Make You Think" (Ignacio de Gregorio)</div>
      <div class="ti-reason">General AI newsletter. Already trashed. Safe to delete.</div>
    </div>
    <div class="trash-item">
      <div class="ti-sender">Nextdoor/Yorkville — "EVENT ASSISTANT NEEDED"</div>
      <div class="ti-reason">Local neighborhood post for a temp job. Not relevant. Safe to delete.</div>
    </div>
    <div class="trash-item">
      <div class="ti-sender">OkCupid — "Someone likes you"</div>
      <div class="ti-reason">Dating app notification. Already trashed. Safe to delete permanently.</div>
    </div>
    <div class="trash-item">
      <div class="ti-sender">Lisa Rangel (Chameleon Resumes) — "Throw better spaghetti"</div>
      <div class="ti-reason">Resume/career marketing email. Already trashed. Safe to delete.</div>
    </div>
    <div class="trash-item">
      <div class="ti-sender">Meidas+ — "MeidasTouch Full Podcast - 6/29/26 [AD-FREE]"</div>
      <div class="ti-reason">Political podcast notification. Already trashed. Safe to delete.</div>
    </div>
    <div class="trash-item">
      <div class="ti-sender">The Average Joe — "🍄 Work harder"</div>
      <div class="ti-reason">Finance/investing newsletter. Already trashed. Safe to delete.</div>
    </div>
    <div class="trash-item">
      <div class="ti-sender">TLDR — "iPhone 18 leaks" (×2 copies — duplicate)</div>
      <div class="ti-reason">Tech newsletter duplicates. Both in trash. Safe to permanently delete.</div>
    </div>
    <div class="trash-item">
      <div class="ti-sender">The Hustle — "🌴 Paid paid time off"</div>
      <div class="ti-reason">Business/lifestyle newsletter. Already trashed. Safe to delete.</div>
    </div>
    <div class="trash-item">
      <div class="ti-sender">The Daily Skimm — "Blanche Devereaux, you would have loved this"</div>
      <div class="ti-reason">Lifestyle newsletter. Already trashed. Safe to delete.</div>
    </div>
    <div class="trash-item">
      <div class="ti-sender">CoolDeep AI — "I deleted almost every AI app on my phone"</div>
      <div class="ti-reason">AI newsletter. Already trashed. Safe to delete.</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 8. PROMOTIONAL / RETAIL SUMMARY -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section band-gray">
  <div class="section-title"><span class="icon">🛍️</span> Promotional / Retail Summary</div>
  <p style="font-size:13px;color:#718096
<hr>
<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Financial / Billing</td><td>1</td></tr>
<tr><td>Job Search / Recruiters</td><td>5</td></tr>
<tr><td>Medical / Health</td><td>2</td></tr>
<tr><td>Other / Review</td><td>20</td></tr>
<tr><td>Professional Development / Newsletters</td><td>12</td></tr>
<tr><td>Promotional / Retail</td><td>7</td></tr>
<tr><td>Security / Risk</td><td>3</td></tr>
</table>
<p><strong>Audit Note:</strong> Every fetched email was reviewed and assigned to one category. Trash emails were included in review. Promotional and low-value emails were accounted for but deprioritized.</p>

