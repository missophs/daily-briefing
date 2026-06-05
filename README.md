<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Melissa's Executive Briefing — Friday, June 5, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .sub { font-size: 15px; color: #a0b4d0; margin-top: 6px; }
  .header .meta-row { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-box { background: rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 20px; text-align: center; }
  .header .meta-box .num { font-size: 26px; font-weight: 700; color: #7dd3fc; }
  .header .meta-box .lbl { font-size: 11px; color: #a0b4d0; text-transform: uppercase; letter-spacing: 1px; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; letter-spacing: 0.3px; margin-bottom: 14px; padding-bottom: 6px; border-bottom: 2px solid #e2e8f0; display: flex; align-items: center; gap: 8px; }

  /* COLOR BANDS */
  .band-red { border-left: 5px solid #ef4444; background: #fff5f5; }
  .band-yellow { border-left: 5px solid #f59e0b; background: #fffbeb; }
  .band-blue { border-left: 5px solid #3b82f6; background: #eff6ff; }
  .band-green { border-left: 5px solid #22c55e; background: #f0fdf4; }
  .band-purple { border-left: 5px solid #8b5cf6; background: #faf5ff; }
  .band-gray { border-left: 5px solid #94a3b8; background: #f8fafc; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }
  .card .card-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 4px; }
  .card .card-title { font-size: 15px; font-weight: 700; margin-bottom: 6px; }
  .card .card-row { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 6px; }
  .card .chip { font-size: 11px; padding: 2px 10px; border-radius: 20px; font-weight: 600; }
  .chip-red { background: #fee2e2; color: #b91c1c; }
  .chip-yellow { background: #fef3c7; color: #92400e; }
  .chip-blue { background: #dbeafe; color: #1e40af; }
  .chip-green { background: #dcfce7; color: #15803d; }
  .chip-purple { background: #ede9fe; color: #6d28d9; }
  .chip-gray { background: #e2e8f0; color: #475569; }

  /* EXEC SUMMARY */
  .exec-summary { background: #1e293b; color: #f1f5f9; border-radius: 12px; padding: 22px 28px; margin-bottom: 24px; }
  .exec-summary h2 { font-size: 15px; text-transform: uppercase; letter-spacing: 1px; color: #94a3b8; margin-bottom: 14px; }
  .exec-summary .bullet { display: flex; align-items: flex-start; gap: 12px; margin-bottom: 10px; }
  .exec-summary .bullet-icon { font-size: 18px; min-width: 26px; }
  .exec-summary .bullet-text { font-size: 14px; line-height: 1.5; }
  .exec-summary .bullet-text strong { color: #7dd3fc; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #1e293b; color: #e2e8f0; padding: 9px 12px; text-align: left; font-size: 11px; text-transform: uppercase; letter-spacing: 0.8px; }
  td { padding: 9px 12px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #f8fafc; }
  .table-wrap { border-radius: 10px; overflow: hidden; box-shadow: 0 1px 6px rgba(0,0,0,0.08); margin-bottom: 16px; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #475569; background: #e2e8f0; border-radius: 6px; padding: 6px 14px; margin-bottom: 8px; }
  .cal-event { background: #fff; border-radius: 8px; padding: 12px 16px; margin-bottom: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); display: flex; gap: 14px; align-items: flex-start; }
  .cal-time { font-size: 12px; font-weight: 700; color: #3b82f6; min-width: 90px; padding-top: 2px; }
  .cal-details { flex: 1; }
  .cal-event-title { font-weight: 700; font-size: 14px; margin-bottom: 4px; }
  .cal-meta { font-size: 12px; color: #64748b; margin-top: 3px; }
  .cal-conflict { background: #fef2f2; border: 1px solid #fca5a5; border-radius: 6px; padding: 4px 10px; font-size: 11px; color: #dc2626; margin-top: 6px; font-weight: 600; }
  .cal-prep { background: #eff6ff; border-radius: 6px; padding: 4px 10px; font-size: 11px; color: #1e40af; margin-top: 4px; }

  /* STATUS CHIPS */
  .status-accepted { background: #dcfce7; color: #15803d; }
  .status-confirmed { background: #dbeafe; color: #1e40af; }
  .status-declined { background: #fee2e2; color: #b91c1c; }
  .status-pending { background: #fef3c7; color: #92400e; }

  /* DASHBOARD */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }
  .dash-box { background: #fff; border-radius: 10px; padding: 16px 18px; box-shadow: 0 1px 6px rgba(0,0,0,0.08); }
  .dash-box .dash-title { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #64748b; margin-bottom: 8px; font-weight: 700; }
  .dash-box .dash-num { font-size: 32px; font-weight: 800; }
  .dash-box .dash-list { font-size: 12px; color: #374151; margin-top: 6px; line-height: 1.7; }
  .dash-red .dash-num { color: #ef4444; }
  .dash-yellow .dash-num { color: #f59e0b; }
  .dash-blue .dash-num { color: #3b82f6; }
  .dash-green .dash-num { color: #22c55e; }
  .dash-purple .dash-num { color: #8b5cf6; }
  .dash-gray .dash-num { color: #94a3b8; }

  /* PRIORITY TABLE */
  .pri-high { color: #b91c1c; font-weight: 700; }
  .pri-med { color: #92400e; font-weight: 700; }
  .pri-low { color: #15803d; font-weight: 700; }

  /* TOP 3 */
  .top3 { display: flex; flex-direction: column; gap: 12px; }
  .top3-item { background: #fff; border-radius: 10px; padding: 16px 20px; box-shadow: 0 1px 6px rgba(0,0,0,0.08); display: flex; gap: 16px; align-items: flex-start; }
  .top3-num { font-size: 32px; font-weight: 900; color: #3b82f6; min-width: 44px; line-height: 1; }
  .top3-content .top3-title { font-size: 15px; font-weight: 700; margin-bottom: 4px; }
  .top3-content .top3-desc { font-size: 13px; color: #64748b; }

  /* CATEGORIES */
  .cat-block { background: #fff; border-radius: 10px; padding: 14px 18px; margin-bottom: 10px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }
  .cat-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; }
  .cat-name { font-weight: 700; font-size: 14px; }
  .cat-count { font-size: 12px; font-weight: 700; padding: 2px 10px; border-radius: 20px; }
  .cat-detail { font-size: 12px; color: #475569; line-height: 1.6; }
  .cat-action { font-size: 12px; font-weight: 600; margin-top: 6px; }

  /* TRASH */
  .trash-group { margin-bottom: 16px; }
  .trash-group-title { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; padding: 6px 14px; border-radius: 6px; margin-bottom: 8px; }
  .trash-restore { background: #dcfce7; color: #15803d; }
  .trash-review { background: #fef3c7; color: #92400e; }
  .trash-delete { background: #fee2e2; color: #b91c1c; }

  /* MISC */
  .note { font-size: 12px; color: #64748b; font-style: italic; margin-top: 6px; }
  .fit-high { color: #15803d; font-weight: 700; }
  .fit-med { color: #1e40af; font-weight: 600; }
  .fit-low { color: #64748b; }
  a { color: #3b82f6; text-decoration: none; }
  a:hover { text-decoration: underline; }
  .total-row td { font-weight: 700; background: #1e293b !important; color: #f1f5f9 !important; }
  @media (max-width: 600px) { .header .meta-row { gap: 12px; } .cal-event { flex-direction: column; } }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ═══════════════════════════════════════════ HEADER ═══════════════════════════════════════════ -->
<div class="header">
  <div style="font-size:12px;color:#7dd3fc;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:6px;">Executive Briefing · Prepared by Your Chief of Staff</div>
  <h1>👋 Good Morning, Melissa!</h1>
  <div class="sub">Friday, June 5, 2026 &nbsp;|&nbsp; Your day at a glance</div>
  <div class="meta-row">
    <div class="meta-box"><div class="num">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="meta-box"><div class="num">9</div><div class="lbl">Calendar Events</div></div>
    <div class="meta-box"><div class="num">🔴 3</div><div class="lbl">Urgent Items</div></div>
    <div class="meta-box"><div class="num">⚡ 8</div><div class="lbl">Action Required</div></div>
    <div class="meta-box"><div class="num">💼 2</div><div class="lbl">Job Alerts</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════ EXECUTIVE SUMMARY ═══════════════════════════════════════════ -->
<div class="exec-summary">
  <h2>⚡ Executive Summary</h2>
  <div class="bullet">
    <div class="bullet-icon">🔴</div>
    <div class="bullet-text"><strong>Biggest Risk:</strong> Your Anthropic/Claude API account is in critical payment failure — 5+ failed charges totaling ~$21.78–$16.40, your Claude API access is already <strong>turned off</strong>, and a receipt was issued suggesting a payment did process. Immediate billing resolution required or your AI tools remain offline.</div>
  </div>
  <div class="bullet">
    <div class="bullet-icon">💼</div>
    <div class="bullet-text"><strong>Biggest Opportunity:</strong> Two strong LinkedIn job alerts today — <strong>VP of HR (Private Equity) at Hoxton Circle ($220K–$240K)</strong> and <strong>Head/Director of HR at Flatpay ($180K–$200K)</strong>. Plus a confirmed 15-min consultation with <strong>Netta Jenkins (HIC Consult)</strong> on Tue Jun 9 — great pipeline momentum.</div>
  </div>
  <div class="bullet">
    <div class="bullet-icon">📅</div>
    <div class="bullet-text"><strong>Biggest Calendar Item:</strong> <strong>Jackie's birthday is tomorrow (June 6)</strong> — no gift/plan noted. Also, your <strong>CHRO Office Substack paid subscription expires tomorrow (June 6)</strong> — decide today whether to renew. Eye appointment Monday June 8 and drinks with Meg on June 10 need location confirmation.</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════ ACTION REQUIRED ═══════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">⚡ Action Required</div>

  <div class="card band-red">
    <div class="card-label" style="color:#b91c1c;">🔴 Critical — Resolve Today</div>
    <div class="card-title">Claude API Access is Turned Off — Payment Failure</div>
    <div class="card-detail" style="font-size:13px;margin-top:4px;">Anthropic sent <strong>multiple failed payment notices</strong> for $21.78 and $16.40, and your Claude API is now <em>disabled</em>. A receipt (#2510-6474-3048) was also issued today suggesting a payment did go through — there is a conflict between receipts and failures. Your bank account was connected via Link (Plaid) around 3:04 PM — this may be a resolution in progress, but needs verification.</div>
    <div class="card-row">
      <span class="chip chip-red">API Offline</span>
      <span class="chip chip-red">Multiple Failed Charges</span>
      <span class="chip chip-yellow">Bank Connected via Link</span>
      <span class="chip chip-blue">Receipt Issued Today</span>
    </div>
    <div style="font-size:13px;margin-top:10px;"><strong>Source:</strong> Anthropic, PBC (failed-payments@mail.anthropic.com &amp; invoice+statements@mail.anthropic.com)</div>
    <div style="font-size:13px;margin-top:4px;"><strong>Why It Matters:</strong> Your daily briefing workflow and AI tools are offline. Your GitHub Actions run also failed today — likely related.</div>
    <div style="font-size:13px;margin-top:4px;"><strong>Next Step:</strong> Log into <a href="https://console.anthropic.com">console.anthropic.com</a>, verify billing status, confirm whether the bank connection via Link resolved the issue, and check that the API is re-enabled. Archive duplicate failure emails.</div>
    <div style="font-size:13px;margin-top:4px;"><strong>Due:</strong> Today, ASAP</div>
  </div>

  <div class="card band-red">
    <div class="card-label" style="color:#b91c1c;">🔴 Urgent — Tech</div>
    <div class="card-title">GitHub Actions Daily Briefing Workflow — All Jobs Failed</div>
    <div class="card-detail" style="font-size:13px;margin-top:4px;">Three failure notifications from GitHub (missophs/daily-briefing) for commit 41906d6 — the "Daily Briefing - webhooks" workflow failed on all jobs. Likely connected to API key/credits being disabled.</div>
    <div class="card-row"><span class="chip chip-red">Workflow Down</span><span class="chip chip-yellow">3 Failure Notices</span></div>
    <div style="font-size:13px;margin-top:10px;"><strong>Source:</strong> notifications@github.com</div>
    <div style="font-size:13px;margin-top:4px;"><strong>Next Step:</strong> Once Anthropic billing is resolved, re-run the workflow and confirm the automation is restored. Check webhook secrets/API keys in repo settings.</div>
    <div style="font-size:13px;margin-top:4px;"><strong>Due:</strong> Today</div>
  </div>

  <div class="card band-yellow">
    <div class="card-label" style="color:#92400e;">🟡 Deadline Tomorrow</div>
    <div class="card-title">CHRO Office Substack — Paid Subscription Expires TOMORROW</div>
    <div class="card-detail" style="font-size:13px;margin-top:4px;">The CHRO Office newsletter notified you that your paid subscription expires on <strong>Saturday, June 6</strong>. Decide today whether to renew to maintain access to premium HR executive content.</div>
    <div class="card-row"><span class="chip chip-yellow">Expires Jun 6</span><span class="chip chip-purple">Professional Resource</span></div>
    <div style="font-size:13px;margin-top:10px;"><strong>Source:</strong> thehroffice@substack.com</div>
    <div style="font-size:13px;margin-top:4px;"><strong>Next Step:</strong> Decide: Renew or let lapse. Given active job search, this may be worth keeping for executive HR insights.</div>
    <div style="font-size:13px;margin-top:4px;"><strong>Due:</strong> Today (expires Jun 6)</div>
  </div>

  <div class="card band-yellow">
    <div class="card-label" style="color:#92400e;">🟡 Tomorrow — Personal</div>
    <div class="card-title">Jackie's Birthday — June 6</div>
    <div class="card-detail" style="font-size:13px;margin-top:4px;">Jackie's birthday is marked on your calendar for tomorrow, June 6. No gift, card, or plan is noted.</div>
    <div class="card-row"><span class="chip chip-yellow">Tomorrow</span></div>
    <div style="font-size:13px;margin-top:10px;"><strong>Source:</strong> Google Calendar</div>
    <div style="font-size:13px;margin-top:4px;"><strong>Next Step:</strong> Send a message, card, or arrange a plan today before it's too late.</div>
    <div style="font-size:13px;margin-top:4px;"><strong>Due:</strong> Today</div>
  </div>

  <div class="card band-yellow">
    <div class="card-label" style="color:#92400e;">🟡 Bill Reminder</div>
    <div class="card-title">State Farm Bill Due — June 7</div>
    <div class="card-detail" style="font-size:13px;margin-top:4px;">State Farm bill is due Sunday, June 7. No amount noted in calendar entry — verify and arrange payment.</div>
    <div class="card-row"><span class="chip chip-yellow">Due Jun 7</span></div>
    <div style="font-size:13px;margin-top:10px;"><strong>Source:</strong> Google Calendar</div>
    <div style="font-size:13px;margin-top:4px;"><strong>Next Step:</strong> Log into State Farm, confirm bill amount, and pay or schedule payment before Sunday.</div>
    <div style="font-size:13px;margin-top:4px;"><strong>Due:</strong> June 7</div>
  </div>

  <div class="card band-green">
    <div class="card-label" style="color:#15803d;">💼 Job Alert — High Priority</div>
    <div class="card-title">VP of Human Resources (Private Equity) — Hoxton Circle ($220K–$240K)</div>
    <div class="card-detail" style="font-size:13px;margin-top:4px;">Strong LinkedIn job alert for a VP HR role in Private Equity. Salary range $220K–$240K/year. Hoxton Circle is a specialist HR executive search firm — this could be a direct placement opportunity.</div>
    <div class="card-row"><span class="chip chip-green">$220K–$240K</span><span class="chip chip-green">High Fit</span></div>
    <div style="font-size:13px;margin-top:10px;"><strong>Source:</strong> LinkedIn Job Alerts</div>
    <div style="font-size:13px;margin-top:4px;"><strong>Next Step:</strong> Review the full posting on LinkedIn, tailor resume/cover letter, and apply. Note: Hoxton Circle is also a recruiter — reaching out directly may accelerate placement.</div>
    <div style="font-size:13px;margin-top:4px;"><strong>Due:</strong> Apply ASAP</div>
  </div>

  <div class="card band-yellow">
    <div class="card-label" style="color:#92400e;">🟡 RSVP Needed</div>
    <div class="card-title">HR Networking & Job Search Group Zoom — Jun 10 &amp; Jun 11 (No RSVP Yet)</div>
    <div class="card-detail" style="font-size:13px;margin-top:4px;">Two recurring HR Networking Zoom sessions (Jun 10 12–1:30 PM and Jun 11 12–1 PM) show status "needsAction" — you have not responded. Conflict warning: Jun 10 overlaps with Melissa x Meg drinks (1–2 PM).</div>
    <div class="card-row"><span class="chip chip-yellow">RSVP Pending</span><span class="chip chip-blue">Jun 10 &amp; 11</span></div>
    <div style="font-size:13px;margin-top:10px;"><strong>Source:</strong> Google Calendar</div>
    <div style="font-size:13px;margin-top:4px;"><strong>Next Step:</strong> Accept or decline both events. Note the Jun 10 overlap with Meg drinks — plan accordingly.</div>
    <div style="font-size:13px;margin-top:4px;"><strong>Due:</strong> Before Jun 10</div>
  </div>

  <div class="card band-yellow">
    <div class="card-label" style="color:#92400e;">🟡 Health / Medical</div>
    <div class="card-title">Vet Prescription Update — Center for Veterinary Care (Stella)</div>
    <div class="card-detail" style="font-size:13px;margin-top:4px;">Center for Veterinary Care sent an important update about third-party prescription requests for Stella. Policy changes may affect how you refill Stella's prescriptions.</div>
    <div class="card-row"><span class="chip chip-yellow">Action May Be Needed</span></div>
    <div style="font-size:13px;margin-top:10px;"><strong>Source:</strong> Center for Veterinary Care / Thrive Pet Care</div>
    <div style="font-size:13px;margin-top:4px;"><strong>Next Step:</strong> Read the full email. If Stella has any upcoming prescription refills, confirm the new process before your next order.</div>
    <div style="font-size:13px;margin-top:4px;"><strong>Due:</strong> Before next refill</div>
  </div>

</div>

<!-- ═══════════════════════════════════════════ FULL 7-DAY CALENDAR ═══════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📅 Full 7-Day Calendar <span style="font-size:12px;font-weight:400;color:#64748b;">(June 5–11, 2026)</span></div>

  <!-- TODAY: Friday June 5 -->
  <div class="cal-day">
    <div class="cal-day-header">📌 Today — Friday, June 5, 2026</div>
    <div class="cal-event band-gray" style="border-left:5px solid #94a3b8;border-radius:8px;">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="cal-event-title">No scheduled calendar events today</div>
        <div class="cal-meta">Focus time available. Use it to resolve Anthropic billing and review job applications.</div>
      </div>
    </div>
  </div>

  <!-- Saturday June 6 -->
  <div class="cal-day">
    <div class="cal-day-header">🎂 Saturday, June 6, 2026</div>
    <div class="cal-event band-yellow" style="border-left:5px solid #f59e0b;border-radius:8px;">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="cal-event-title">🎂 Jackie's Birthday</div>
        <div class="cal-meta">Status: <span class="chip chip-blue status-confirmed">Confirmed</span> &nbsp; | &nbsp; No attendees listed</div>
        <div class="cal-prep">⚡ Prep: Send message, card, or gift TODAY before it's too late.</div>
      </div>
    </div>
  </div>

  <!-- Sunday June 7 -->
  <div class="cal-day">
    <div class="cal-day-header">💳 Sunday, June 7, 2026</div>
    <div class="cal-event band-yellow" style="border-left:5px solid #f59e0b;border-radius:8px;">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="cal-event-title">💳 State Farm Bill Due</div>
        <div class="cal-meta">Status: <span class="chip chip-blue status-confirmed">Confirmed</span> &nbsp; | &nbsp; No amount listed</div>
        <div class="cal-prep">⚡ Prep: Log in to State Farm account and pay before end of day. Confirm amount and payment method.</div>
      </div>
    </div>
  </div>

  <!-- Monday June 8 -->
  <div class="cal-day">
    <div class="cal-day-header">👁️ Monday, June 8, 2026</div>
    <div class="cal-event band-blue" style="border-left:5px solid #3b82f6;border-radius:8px;">
      <div class="cal-time">9:00 AM<br><span style="color:#94a3b8;font-weight:400;">–10:00 AM</span></div>
      <div class="cal-details">
        <div class="cal-event-title">👁️ Eye Appointment</div>
        <div class="cal-meta">Status: <span class="chip chip-blue status-confirmed">Confirmed</span> &nbsp; | &nbsp; Location: Not listed (confirm address)</div>
        <div class="cal-prep">⚡ Prep: Confirm location. Note: Warby Parker says your prescription expires in 2 weeks — bring insurance card. 1-800 Contacts also flagged you as overdue for a reorder. Use this appointment to get an updated prescription.</div>
      </div>
    </div>
  </div>

  <!-- Tuesday June 9 -->
  <div class="cal-day">
    <div class="cal-day-header">🤝 Tuesday, June 9, 2026</div>
    <div class="cal-event band-green" style="border-left:5px solid #22c55e;border-radius:8px;">
      <div class="cal-time">12:00 PM<br><span style="color:#94a3b8;font-weight:400;">–12:15 PM</span></div>
      <div class="cal-details">
        <div class="cal-event-title">🤝 Melissa &amp; Netta Jenkins — 15-Min Consultation</div>
        <div class="cal-meta">Status: <span class="chip chip-green status-accepted">Accepted</span> &nbsp; | &nbsp; Attendee: netta@hicconsult.com &nbsp; | &nbsp; <a href="https://us06web.zoom.us/j/5224221004?pwd=UU5YNmlFckpjQnlzc2FDMHFlNUhhUT09&omn=81785592238">Zoom Link</a> &nbsp; | &nbsp; Password: 424726</div>
        <div class="cal-prep">⚡ Prep: Research HIC Consult and Netta Jenkins. Prepare a 60-second career summary. Have your target roles/industries ready. This is a short window — be crisp and direct about what you're looking for.</div>
      </div>
    </div>
  </div>

  <!-- Wednesday June 10 -->
  <div class="cal-day">
    <div class="cal-day-header">🌐 Wednesday, June 10, 2026</div>
    <div class="cal-event band-purple" style="border-left:5px solid #8b5cf6;border-radius:8px;">
      <div class="cal-time">12:00 PM<br><span style="color:#94a3b8;font-weight:400;">–1:30 PM</span></div>
      <div class="cal-details">
        <div class="cal-event-title">🌐 HR Networking &amp; Job Search Group — Zoom Session 2</div>
        <div class="cal-meta">Status: <span class="chip chip-yellow status-pending">Needs Action ⚠️</span> &nbsp; | &nbsp; 190+ attendees &nbsp; | &nbsp; <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1">Zoom Link</a></div>
        <div class="cal-prep">⚡ Prep: RSVP. Review HR Networking Team Guidelines (linked in invite). Note: No automated notetaking AI tools per organizer rules.</div>
        <div class="cal-conflict">⚠️ CONFLICT: Overlaps with Melissa x Meg Drinks (1:00–2:00 PM) — 30-min overlap. Plan transition.</div>
      </div>
    </div>
    <div class="cal-event" style="background:#fff;border-radius:8px;box-shadow:0 1px 4px rgba(0,0,0,0.07);">
      <div class="cal-time">12:00 PM<br><span style="color:#94a3b8;font-weight:400;">–1:30 PM</span></div>
      <div class="cal-details">
        <div class="cal-event-title">📌 Network (Personal Calendar Block)</div>
        <div class="cal-meta">Status: <span class="chip chip-blue status-confirmed">Confirmed</span> &nbsp; | &nbsp; Personal reminder — no location or attendees</div>
        <div class="cal-meta" style="margin-top:4px;">Appears to be a personal reminder aligned with the HR Networking Zoom session above.</div>
      </div>
    </div>
    <div class="cal-event band-green" style="border-left:5px solid #22c55e;border-radius:8px;">
      <div class="cal-time">1:00 PM<br><span style="color:#94a3b8;font-weight:400;">–2:00 PM</span></div>
      <div class="cal-details">
        <div class="cal-event-title">🥂 Melissa x Meg Drinks</div>
        <div class="cal-meta">Status: <span class="chip chip-green status-accepted">Accepted</span> &nbsp; | &nbsp; Attendee: megpark@oakleafpartnership.com &nbsp; | &nbsp; Location: TBC</div>
        <div class="cal-prep">⚡ Prep: Confirm location with Meg ASAP. Note the overlap with HR Networking Zoom (ends 1:30 PM). Oakleaf Partnership is an HR consulting/recruitment firm — great networking opportunity.</div>
        <div class="cal-conflict">⚠️ CONFLICT: Overlaps with HR Networking Zoom (12:00–1:30 PM) — plan your exit from Zoom at 1:00 PM sharp.</div>
      </div>
    </div>
  </div>

  <!-- Thursday June 11 -->
  <div class="cal-day">
    <div class="cal-day-header">🏆 Thursday, June 11, 2026</div>
    <div class="cal-event band-gray" style="border-left:5px solid #ef4444;border-radius:8px;">
      <div class="cal-time">9:00 AM<br><span style="color:#94a3b8;font-weight:400;">–10:30 AM</span></div>
      <div class="cal-details">
        <div class="cal-event-title">🏆 Executive Roundtable (Zoom)</div>
        <div class="cal-meta">Status: <span class="chip chip-red status-declined">Declined</span> &nbsp; | &nbsp; Hosted by: John Madigan &nbsp; | &nbsp; <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09">Zoom Link</a> &nbsp; | &nbsp; Password: 205454</div>
        <div class="cal-meta" style="margin-top:4px;color:#ef4444;font-weight:600;">⚠️ You have declined this event. Reconsider — Executive Roundtables are strong networking opportunities during an active job search.</div>
      </div>
    </div>
    <div class="cal-event band-purple" style="border-left:5px solid #8b5cf6;border-radius:8px;">
      <div class="cal-time">12:00 PM<br><span style="color:#94a3b8;font-weight:400;">–1:00 PM</span></div>
      <div class="cal-details">
        <div class="cal-event-title">🌐 HR Networking &amp; Job Search: Open Office Hours — Zoom</div>
        <div class="cal-meta">Status: <span class="chip chip-yellow status-pending">Needs Action ⚠️</span> &nbsp; | &nbsp; 190+ attendees &nbsp; | &nbsp; <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1">Zoom Link</a></div>
        <div class="cal-prep">⚡ Prep: RSVP. Open discussion format, no recording per organizer. Great opportunity for 1:1 connections with other HR professionals in job search.</div>
      </div>
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════ JOB SEARCH & PIPELINE ═══════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Role / Opportunity</th>
          <th>Source / Sender</th>
          <th>Salary / Details</th>
          <th>Fit</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="chip chip-green">Job Alert</span></td>
          <td><strong>VP Human Resources (Private Equity)</strong><br>Hoxton Circle</td>
          <td>LinkedIn Job Alerts</td>
          <td>$220K–$240K / year</td>
          <td><span class="fit-high">HIGH</span></td>
          <td>Review posting &amp; apply ASAP. Hoxton Circle is also a recruiter — reach out directly.</td>
        </tr>
        <tr>
          <td><span class="chip chip-green">Job Alert</span></td>
          <td><strong>Head / Director of HR (US)</strong><br>Flatpay</td>
          <td>LinkedIn Job Alerts (Trash)</td>
          <td>$180K–$200K / year</td>
          <td><span class="fit-high">HIGH</span></td>
          <td>Restore from trash &amp; review full posting. FinTech HR leadership role — strong fit if PE/tech experience applies.</td>
        </tr>
        <tr>
          <td><span class="chip chip-blue">Networking</span></td>
          <td><strong>15-Min Consultation — Netta Jenkins</strong><br>HIC Consult (netta@hicconsult.com)</td>
          <td>Google Calendar</td>
          <td>Tue Jun 9 | 12:00–12:15 PM | Zoom</td>
          <td><span class="fit-high">HIGH</span></td>
          <td>Prep talking points. 15 mins only — be sharp. Research HIC Consult before the call.</td>
        </tr>
        <tr>
          <td><span class="chip chip-blue">Networking</span></td>
          <td><strong>Melissa x Meg Drinks</strong><br>Meg Park (Oakleaf Partnership)</td>
          <td>Google Calendar</td>
          <td>Wed Jun 10 | 1:00–2:00 PM | TBC</td>
          <td><span class="fit-high">HIGH</span></td>
          <td>Confirm location. Oakleaf Partnership is an HR specialist — treat as a key networking meeting.</td>
        </tr>
        <tr>
          <td><span class="chip chip-purple">Networking Event</span></td>
          <td><strong>HR Networking &amp; Job Search Group — Zoom 2</strong><br>~190 HR professionals</td>
          <td>Google Calendar</td>
          <td>Wed Jun 10 | 12:00–1:30 PM | RSVP Needed</td>
          <td><span class="fit-med">MEDIUM</span></td>
          <td>RSVP. Good for broadening network. Note conflict with Meg drinks at 1 PM.</td>
        </tr>
        <tr>
          <td><span class="chip chip-purple">Networking Event</span></td>
          <td><strong>HR Networking &amp; Job Search: Open Office Hours</strong></td>
          <td>Google Calendar</td>
          <td>Thu Jun 11 | 12:00–1:00 PM | RSVP Needed</td>
          <td><span class="fit-med">MEDIUM</span></td>
          <td>RSVP. Open discussion format — ideal for 1:1 connections.</td>
        </tr>
        <tr>
          <td><span class="chip chip-gray">Declined</span></td>
          <td><strong>Executive Roundtable</strong><br>Hosted by John Madigan</td>
          <td>Google Calendar</td>
          <td>Thu Jun 11 | 9:00–10:30 AM | Zoom — DECLINED</td>
          <td><span class="fit-med">MEDIUM</span></td>
          <td>Consider reversing your decline — executive roundtables offer high-value peer networking during job search.</td>
        </tr>
        <tr>
          <td><span class="chip chip-gray">Community</span></td>
          <td><strong>RNG Tampa Bay — Bank of America Recruiting Contact Request</strong><br>Antonio Fiorentino</td>
          <td>RNGTampa@googlegroups.com</td>
          <td>Group networking request</td>
          <td><span class="fit-low">LOW</span></td>
          <td>Review. If you have a BoA recruiting contact, consider sharing. Good community engagement.</td>
        </tr>
        <tr>
          <td><span class="chip chip-green">Membership</span></td>
          <td><strong>Worldwide Women's Association — Membership Outreach</strong><br>Sophia Davis</td>
          <td>worldwidewomensassociation.com</td>
          <td>Professional membership</td>
          <td><span class="fit-low">LOW</span></td>
          <td>Evaluate value vs. cost. Low priority during active job search unless it provides direct HR executive connections.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════ FULL EMAIL REVIEW BY CATEGORY ═══════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📧 Full Email Review by Category</div>

  <!-- Security / Risk -->
  <div class="cat-block band-red" style="border-radius:10px;">
    <div class="cat-header">
      <div class="cat-name">🔴 Security / Risk</div>
      <span class="cat-count chip-red chip">7 emails</span>
    </div>
    <div class="cat-detail">
      <strong>Anthropic — Failed Payment ($21.78, ×4 attempts):</strong> failed-payments@mail.anthropic.com sent multiple identical failures. These appear to be rapid retries, not separate charges. Timestamps: 14:14, 14:15, 14:17, 14:22 (also one earlier at 15:04–15:05).<br>
      <strong>Anthropic — Failed Payment ($16.40, ×1):</strong> One failure for a different amount — possible second subscription tier.<br>
      <strong>Anthropic — [Action Needed] API Access Turned Off:</strong> no-reply-tg3@mail.anthropic.com — API is currently disabled due to no usage credits.<br>
      <strong>GitHub — Daily Briefing Workflow Failed (×3):</strong> missophs/daily-briefing all jobs failed for commit 41906d6. Likely downstream from API failure.<br>
      <em>Note: The Link (Plaid) bank connection emails are listed under Financial/Billing below.</em>
    </div>
    <div class="cat-action" style="color:#b91c1c;">⚡ Action: Resolve Anthropic billing immediately. Re-run GitHub workflow once fixed. Archive duplicate failure emails.</div>
  </div>

  <!-- Job Search -->
  <div class="cat-block band-green" style="border-radius:10px;margin-top:10px;">
    <div class="cat-header">
      <div class="cat-name">💼 Job Search</div>
      <span class="cat-count chip-green chip">2 emails</span>
    </div>
    <div class="cat-detail">
      <strong>LinkedIn — VP Human Resources (Private Equity) at Hoxton Circle ($220K–$240K):</strong> Unread, in inbox. High priority.<br>
      <strong>LinkedIn — Head / Director of HR (US) at Flatpay ($180K–$200K):</strong> Unread, in <em>trash</em> — was deleted. Restore and review.
    </div>
    <div class="cat-action" style="color:#15803d;">⚡ Action: Review both postings immediately. Apply to both. Restore the Flatpay alert from trash.</div>
  </div>

  <!-- Recruiters / Networking -->
  <div class="cat-block band-green" style="border-radius:10px;margin-top:10px;">
    <div class="cat-header">
      <div class="cat-name">🤝 Recruiters / Networking</div>
      <span class="cat-count chip-green chip">2 emails</span>
    </div>
    <div class="cat-detail">
      <strong>Sophia Davis — WWA Membership:</strong> Worldwide Women's Association outreach. Evaluate relevance to your job search.<br>
      <strong>RNG Tampa Bay (Antonio Fiorentino) — Bank of America Recruiting Contact:</strong> Community group looking for BoA recruiting connection. Low urgency.
    </div>
    <div class="cat-action" style="color:#15803d;">⚡ Action: Evaluate WWA membership value. Respond to RNG Tampa Bay if you have a BoA contact to share.</div>
  </div>

  <!-- Calendar / Events -->
  <div class="cat-block band-blue" style="border-radius:10px;margin-top:10px;">
    <div class="cat-header">
      <div class="cat-name">📅 Calendar / Events</div>
      <span class="cat-count chip-blue chip">1 email</span>
    </div>
    <div class="cat-detail">
      <strong>Melissa Daily Briefing (melissaw212@gmail.com):</strong> Self-sent daily briefing generated at 13:50 UTC today. Workflow ran before the API failure was fully resolved — partial output. This briefing supersedes it.
    </div>
    <div class="cat-action" style="color:#1e40af;">⚡ Action: Archive. This briefing replaces the self-generated one.</div>
  </div>

  <!-- Medical / Health -->
  <div class="cat-block" style="border-left:5px solid #ec4899;background:#fdf2f8;border-radius:10px;margin-top:10px;">
    <div class="cat-header">
      <div class="cat-name">🏥 Medical / Health</div>
      <span class="cat-count" style="background:#fce7f3;color:#9d174d;" class="chip">1 email</span>
    </div>
    <div class="cat-detail">
      <strong>Center for Veterinary Care (Thrive Pet Care) — Stella Prescription Update:</strong> Important update re: third-party prescription requests. Policy change may affect Stella's medication refills.
    </div>
    <div class="cat-action" style="color:#9d174d;">⚡ Action: Read full email. Confirm whether Stella has any upcoming refills affected by this change.</div>
  </div>

  <!-- Financial / Billing -->
  <div class="cat-block band-yellow" style="border-radius:10px;margin-top:10px;">
    <div class="cat-header">
      <div class="cat-name">💳 Financial / Billing</div>
      <span class="cat-count chip-yellow chip">5 emails</span>
    </div>
    <div class="cat-detail">
      <strong>Anthropic Receipt #2510-6474-3048 (15:08 today):</strong> A successful payment receipt — may indicate the bank link resolved billing.<br>
      <strong>Anthropic Receipt #2010-4855-2725 (13:33 today):</strong> Earlier receipt — verify this wasn't a duplicate charge.<br>
      <strong>Link / Plaid — Bank Account Connected to Anthropic (×2):</strong> Two bank connection notifications (14:13 and 15:04) — suggests multiple attempts to connect payment. Confirm only one active connection.<br>
      <strong>The CHRO Office Substack — Subscription Expires Tomorrow:</strong> Paid subscription ends Jun 6. Decide to renew or let lapse.
    </div>
    <div class="cat-action" style="color:#92400e;">⚡ Action: Verify Anthropic billing is resolved and you haven't been double-charged. Confirm only one Plaid connection is active. Decide on CHRO Office subscription renewal today.</div>
  </div>

  <!-- Professional Development -->
  <div class="cat-block band-purple" style="border-radius:10px;margin-top:10px;">
    <div class="cat-header">
      <div class="cat-name">🎓 Professional Development</div>
      <span class="cat-count chip-purple chip">2 emails</span>
    </div>
    <div class="cat-detail">
      <strong>Phil Strazzulla (SSR Newsletter) — [Free Webinar] Why HR Software Decisions Fail:</strong> Practical buy-in strategies for HR software — relevant for HR leaders.<br>
      <strong>Olivia Gamber (Career Evolved) — "The Room of 7" (Trash):</strong> Career coaching content — was trashed. Evaluate if relevant.
    </div>
    <div class="cat-action" style="color:#6d28d9;">⚡ Action: Consider the free webinar if timing works. Olivia Gamber email — safe to delete if coaching outreach is unsolicited.</div>
  </div>

  <!-- Personal -->
  <div class="cat-block band-gray" style="border-radius:10px;margin-top:10px;">
    <div class="cat-header">
      <div class="cat-name">👤 Personal</div>
      <span class="cat-count chip-gray chip">1 email</span>
    </div>
    <div class="cat-detail">
      <strong>Brya Team — Survey Reminder:</strong> Short survey sent Tuesday, closes end of week. Brya appears to be a platform you've used. Low urgency but closing today.
    </div>
    <div class="cat-action" style="color:#475569;">⚡ Action: Complete if relevant, takes ~2 minutes. Otherwise ignore.</div>
  </div>

  <!-- Newsletters / Subscriptions -->
  <div class="cat-block band-purple" style="border-radius:10px;margin-top:10px;">
    <div class="cat-header">
      <div class="cat-name">📰 Newsletters / Subscriptions</div>
      <span class="cat-count chip-purple chip">4 emails</span>
    </div>
    <div class="cat-detail">
      <strong>Mindstream — "Google unveils Dreambeans" + AI mental health stats:</strong> Tech/AI newsletter. AI mental health content (1 in 5 teens using AI for support) relevant if you work with employee wellness.<br>
      <strong>HR Brain Pickings — The Friday 5 (AI budgets, sick leave, papal encyclical):</strong> HR-specific newsletter with Uber AI coding tools story + sick leave policy. Relevant HR content.<br>
      <strong>Hebba Youssef (I Hate It Here) — Motivation with $0 (Trash):</strong> Popular HR newsletter trashed — evaluate if you want to keep receiving.<br>
      <strong>CoolDeep AI — "Claude did my Instagram content while I slept" (not in inbox):</strong> AI workflow newsletter. Low priority given current Claude billing issues.
    </div>
    <div class="cat-action" style="color:#6d28d9;">⚡ Action: Read HR Brain Pickings Friday 5 — relevant HR intel. Consider restoring Hebba Youssef from trash. CoolDeep AI: unsubscribe if not valuable.</div>
  </div>

  <!-- Promotional / Retail (Inbox) -->
  <div class="cat-block band-gray" style="border-radius:10px;margin-top:10px;">
    <div class="cat-header">
      <div class="cat-name">🛍️ Promotional / Retail (In Inbox)</div>
      <span class="cat-count chip-gray chip">6 emails</span>
    </div>
    <div class="cat-detail">
      <strong>Fetch — "Get more points for your $":</strong> Supercharged offers. Rewards app promo.<br>
      <strong>CoinOut — "Earn up to 7,000 Coins":</strong> Receipt scanning app promo.<br>
      <strong>Sago (Focus Group) — "$100 Research Study on Financial Experiences":</strong> Paid research study — $100 incentive. Low effort opportunity.<br>
      <strong>Chip City — 15% Off Catering this Summer:</strong> Cookie shop catering promo. NYC-based.<br>
      <strong>Robinhood — Claim a Retirement Match (Trash):</strong> IRA/401K rollover promo, deadline June 19. In trash.<br>
      <strong>Warby Parker — Prescription Expires in Two Weeks:</strong> Not a promo — see Health section below. Noted here for completeness — your prescription expires in ~2 weeks. Eye appointment June 8 is timely.
    </div>
    <div class="cat-action" style="color:#475569;">⚡ Action: Sago study — worth $100 if qualifying takes minimal time. Chip City, Fetch, CoinOut — delete. Warby Parker — address at eye appointment June 8.</div>
  </div>

  <!-- Promotional / Retail (Not in inbox, not trash) -->
  <div class="cat-block band-gray" style="border-radius:10px;margin-top:10px;">
    <div class="cat-header">
      <div class="cat-name">🛍️ Promotional / Retail (Not in Inbox)</div>
      <span class="cat-count chip-gray chip">8 emails</span>
    </div>
    <div class="cat-detail">
      <strong>PUMA — PUMA x SALEHE BEMBURY collaboration launch:</strong> Not in inbox/trash — likely filtered.<br>
      <strong>Old Navy — 50% off active wear:</strong> Not in inbox.<br>
      <strong>Venmo — Earn up to 9% cash back (credit card offer):</strong> Not in inbox.<br>
      <strong>Slack — Invite your team (free trial Pro):</strong> Not in inbox. If you're actively using Slack for networking groups, worth reviewing.<br>
      <strong>Robinhood — IRA/401K Rollover Match (Trash, deadline Jun 19):</strong> Restore if interested — deadline is June 19.<br>
      <strong>Pre-IPO / Capital Noted — Apple Starlink/Mode Mobile promo:</strong> Investment newsletter promo. Likely spam-adjacent.<br>
      <strong>Focus Group (participate@focusgroup.com) — Research Opportunities Update:</strong> Update about Focus Group membership and new opportunities.<br>
      <strong>GLP-1 by DirectMeds — Weight loss promo (spam domain):</strong> Obvious spam/phishing-adjacent domain (clmo.jxstfafscurth.us). Do not click any links.
    </div>
    <div class="cat-action" style="color:#475569;">⚡ Action: GLP-1 email — mark as spam, do not click. Robinhood — restore if interested (Jun 19 deadline). All others — delete/ignore.</div>
  </div>

  <!-- Trash Review (in email categories) -->
  <div class="cat-block" style="border-left:5px solid #ef4444;background:#fff5f5;border-radius:10px;margin-top:10px;">
    <div class="cat-header">
      <div class="cat-name">🗑️ Trash Review</div>
      <span class="cat-count chip-red chip">9 emails (in trash)</span>
    </div>
    <div class="cat-detail">
      See dedicated Trash Review section below for full breakdown with Restore / Review / Delete recommendations.
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════ TRASH REVIEW ═══════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">🗑️ Trash Review</div>
  <p style="font-size:13px;color:#64748b;margin-bottom:14px;">9 emails currently in Gmail Trash. Reviewed and categorized below.</p>

  <div class="trash-group">
    <div class="trash-group-title trash-restore">✅ RESTORE — Do Not Delete</div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Sender</th><th>Subject</th><th>Why Restore</th></tr></thead>
        <tbody>
          <tr>
            <td>LinkedIn Job Alerts</td>
            <td>Head / Director of HR (US) at Flatpay: up to $200K/year</td>
            <td>High-value job alert ($180K–$200K). Should not have been trashed. Review and apply.</td>
          </tr>
          <tr>
            <td>Hebba Youssef (I Hate It Here)</td>
            <td>📓 Motivation with $0</td>
            <td>Popular HR newsletter — metrics &amp; engagement without budget. Relevant to HR executive job search discussions. Restore if you want to keep the subscription.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="trash-group">
    <div class="trash-group-title trash-review">🔍 REVIEW BEFORE DELETING</div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Sender</th><th>Subject</th><th>Why Review</th></tr></thead>
        <tbody>
          <tr>
            <td>Robinhood</td>
            <td>Reminder: Claim a retirement match</td>
            <td>Deadline June 19 — if you have an IRA or 401K to roll over, this is a real financial opportunity (3% match). Restore if interested.</td>
          </tr>
          <tr>
            <td>Olivia Gamber (Career Evolved)</td>
            <td>The room of 7 (and the block holding you back)</td>
            <td>Career coaching email. May be relevant during job search. Review sender — if unsolicited sales funnel, safe to delete.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="trash-group">
    <div class="trash-group-title trash-delete">🗑️ SAFE TO PERMANENTLY DELETE</div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Sender</th><th>Subject</th><th>Reason</th></tr></thead>
        <tbody>
          <tr>
            <td>Fayced Aesthetics NYC</td>
            <td>Meet Daisy (Nurse Injector promo)</td>
            <td>Promotional marketing. No action needed.</td>
          </tr>
          <tr>
            <td>BellaVitashop (TikTok Shop)</td>
            <td>Flash sale starts now!</td>
            <td>Generic TikTok Shop promo. Safe to delete.</td>
          </tr>
          <tr>
            <td>Shoe Station</td>
            <td>It's Here: The Sandal Savings Event!</td>
            <td>
<hr>
<h2>Trash Review</h2>
<p><strong>Purpose:</strong> Review deleted emails for anything important before permanent deletion. Anything from job search, billing, medical, calendar, security, legal, GitHub, Netlify, LinkedIn, recruiters, or professional contacts should be reviewed before deleting.</p>

<h2>Promotional / Retail Summary</h2>
<p><strong>Purpose:</strong> Promotional emails are included in the full email inventory below. Delete or ignore retail/promotional items unless there is a deal you actually plan to use or a sender looks suspicious.</p>

<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Financial / Billing</td><td>10</td></tr>
<tr><td>Job Search / Recruiters</td><td>5</td></tr>
<tr><td>Medical / Health</td><td>3</td></tr>
<tr><td>Other / Review</td><td>16</td></tr>
<tr><td>Professional Development / Newsletters</td><td>7</td></tr>
<tr><td>Promotional / Retail</td><td>7</td></tr>
<tr><td>Security / Risk</td><td>2</td></tr>
</table>

<h2>Full Email Inventory</h2>
<p><strong>Every fetched email is grouped below by category.</strong> Use this section to see what to act on, review, delete, or ignore.</p>

<div style="background:#fffbf0; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Financial / Billing (10)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#3 · Fri, 5 Jun 2026 15:08:38 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Your receipt from Anthropic, PBC #2510-6474-3048</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Anthropic, PBC&quot; &lt;invoice+statements@mail.anthropic.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Your receipt from Anthropic, PBC #2510-6474-3048 ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#7 · Fri, 5 Jun 2026 15:05:34 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">$21.78 payment to Anthropic, PBC was unsuccessful</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Anthropic, PBC&quot; &lt;failed-payments@mail.anthropic.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">We weren&amp;#39;t able to charge the credit card you provided. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#8 · Fri, 5 Jun 2026 15:04:43 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">$21.78 payment to Anthropic, PBC was unsuccessful</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Anthropic, PBC&quot; &lt;failed-payments@mail.anthropic.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">We weren&amp;#39;t able to charge the credit card you provided. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#18 · Fri, 5 Jun 2026 14:22:46 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">$21.78 payment to Anthropic, PBC was unsuccessful again</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Anthropic, PBC&quot; &lt;failed-payments@mail.anthropic.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">We weren&amp;#39;t able to charge the credit card you provided. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#21 · Fri, 5 Jun 2026 14:17:06 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">$21.78 payment to Anthropic, PBC was unsuccessful</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Anthropic, PBC&quot; &lt;failed-payments@mail.anthropic.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">We weren&amp;#39;t able to charge the credit card you provided. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#23 · Fri, 5 Jun 2026 14:15:46 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">$21.78 payment to Anthropic, PBC was unsuccessful</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Anthropic, PBC&quot; &lt;failed-payments@mail.anthropic.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">We weren&amp;#39;t able to charge the credit card you provided. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#25 · Fri, 5 Jun 2026 14:14:14 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">$21.78 payment to Anthropic, PBC was unsuccessful</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Anthropic, PBC&quot; &lt;failed-payments@mail.anthropic.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">We weren&amp;#39;t able to charge the credit card you provided. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#27 · Fri, 5 Jun 2026 14:12:03 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">$16.40 payment to Anthropic, PBC was unsuccessful</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Anthropic, PBC&quot; &lt;failed-payments@mail.anthropic.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">We weren&amp;#39;t able to charge the credit card you provided. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#37 · Fri, 5 Jun 2026 13:33:43 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Your receipt from Anthropic, PBC #2010-4855-2725</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Anthropic, PBC&quot; &lt;invoice+statements@mail.anthropic.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Your receipt from Anthropic, PBC #2010-4855-2725 ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#43 · Fri, 05 Jun 2026 13:18:56 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">[action needed] Your Claude API access is turned off</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Anthropic &lt;no-reply-tg3-12bWhUPY4cJHtPeAoQ@mail.anthropic.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Hello, Your access to the Claude API has been disabled because your organization &amp;#39;Melissa&amp;#39;s Individual Org&amp;#39; is out of usage credits. Go to</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>
</div>

<div style="background:#f0fff4; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Job Search / Recruiters (5)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#5 · Fri, 5 Jun 2026 15:06:20 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Vice President Human Resources (Private Equity) at Hoxton Circle: up to $240K/year</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> LinkedIn Job Alerts &lt;jobalerts-noreply@linkedin.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">$220K-$240K / year salary ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#31 · Fri, 05 Jun 2026 07:02:55 -0700</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">[missophs/daily-briefing] Run failed: Daily Briefing - webhooks (41906d6)</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> missophs &lt;notifications@github.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">[missophs/daily-briefing] Daily Briefing workflow run Daily Briefing: All jobs have failed View workflow run Status Job Annotations Daily Briefing / u</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#36 · Fri, 05 Jun 2026 06:33:57 -0700</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">[missophs/daily-briefing] Run failed: Daily Briefing - webhooks (41906d6)</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> missophs &lt;notifications@github.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">[missophs/daily-briefing] Daily Briefing workflow run Daily Briefing: All jobs have failed View workflow run Status Job Annotations Daily Briefing / u</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#42 · Fri, 05 Jun 2026 06:27:12 -0700</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">[missophs/daily-briefing] Run failed: Daily Briefing - webhooks (41906d6)</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> missophs &lt;notifications@github.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">[missophs/daily-briefing] Daily Briefing workflow run Daily Briefing: All jobs have failed View workflow run Status Job Annotations Daily Briefing / u</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#49 · Fri, 5 Jun 2026 13:05:53 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Head / Director of HR (US) at Flatpay: up to $200K/year</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> LinkedIn Job Alerts &lt;jobalerts-noreply@linkedin.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">$180K-$200K / year salary ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>
</div>

<div style="background:#ebf8ff; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Medical / Health (3)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#2 · Fri, 05 Jun 2026 15:08:29 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Google unveils... Dreambeans</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Mindstream &lt;hello@mindstream.news&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">+ 1 in 5 teens use AI for mental health support ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#22 · Fri, 05 Jun 2026 09:26:42 -0400</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">DirectMeds GLP-1 treatment helps you lose up to 4O lbs by the End of Year</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> GLP-1-by-DirectMeds &lt;makiuxdfydq@clmo.jxstfafscurth.us&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">DirectMeds Medical Portal Looking for Ozempic® or Mounjaro® alternative? Weight loss made simple with Semaglutide or Tirzepatide Genuine prescription </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#39 · Fri, 5 Jun 2026 13:06:13 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">New ways to save on contact lenses!</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Target Optical &lt;news@e.targetoptical.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Find the perfect contact for you at Target Optical View in browser Target Optical ® Eyeglasses Sunglasses Contact lenses Plan your visit More ways to </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>
</div>

<div style="background:#f7fafc; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Other / Review (16)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#4 · Fri, 05 Jun 2026 15:08:04 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Coming Soon: Earn up to 7,000 Coins</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> CoinOut &lt;coinout@news.coinout.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Be on the look-out for your chance to earn up to 7000 Coins! Logo Earn up to 7000 Coins Be on the look-out in your Missions screen over the next few d</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#9 · Fri, 5 Jun 2026 15:04:23 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">You&#x27;ve connected your bank account to Anthropic, PBC</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Link &lt;notifications@link.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">You connected your account with Link ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#10 · Fri, 05 Jun 2026 15:01:43 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Things are moving fast at the WWA, secure your membership spot today!</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Sophia Davis &lt;sophia.davis@worldwidewomensassociation.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Join The Worldwide Women&amp;#39;s Association‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#12 · Fri, 05 Jun 2026 14:57:55 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Reminder: Claim a retirement match</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Robinhood &lt;noreply@robinhood.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Transfer an IRA or rollover a 401K to Robinhood by June 19, and earn a match. ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#16 · Fri, 05 Jun 2026 14:44:00 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Important Update: Third Party Prescription Requests</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Center for Veterinary Care  &lt;contact@em.thrivepetcare.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">We&amp;#39;re committed to seamless care for Stella. Center for Veterinary Care New Home, Now Open Dear Melissa, At Center for Veterinary Care, we&amp;#39;re </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#17 · Fri, 05 Jun 2026 13:28:49 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Reorder in two taps for National Eyewear Day</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> 1-800 Contacts &lt;info@pr.1800contacts.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">You&amp;#39;re overdue, based on your last order date. ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#26 · Fri, 5 Jun 2026 14:13:56 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">You&#x27;ve connected your bank account to Anthropic, PBC</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Link &lt;notifications@link.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">You connected your account with Link ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#28 · Fri, 05 Jun 2026 09:10:22 -0500</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Double the Vitamins, Zero Extra Cost</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Walgreens &lt;walgreens@eml.walgreens.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Stock up on select same-brand essentials—your second item is on us. ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#32 · Fri, 05 Jun 2026 14:00:07 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Still time to share your thoughts 🙏</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Brya Team &lt;hello@brya.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Hi there, Just a quick nudge — we sent a short survey on Tuesday and would love to hear from you before we close the survey at the end of the week. Yo</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#33 · Fri, 5 Jun 2026 14:00:04 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Claude did my Instagram content while I slept</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> CoolDeep AI &lt;cooldeepai@mail.beehiiv.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">The carousel workflow that changed my mornings ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#34 · Fri, 05 Jun 2026 13:59:43 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Your prescription expires in two weeks</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Warby Parker &lt;sayhello@mail1.warbyparker.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Pick out some new frames today. ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#41 · Fri, 5 Jun 2026 06:27:59 -0700 (PDT)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">[RNG Tampa Bay] Bank of America contact</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;&#x27;Antonio Fiorentino&#x27; via RNG Tampa Bay&quot; &lt;RNGTampa@googlegroups.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Hi everyone, I&amp;#39;m looking to connect with someone in Recruiting at Bank of America. If anyone in the group currently works there or has a contact t</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#45 · Fri, 05 Jun 2026 13:16:37 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Earn up to 9% cash back for 6 months with the Venmo Credit Card</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Venmo &lt;venmo@email.venmo.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Apply with no impact to your credit score if declined. ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#46 · Fri, 05 Jun 2026 13:10:52 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">The room of 7 (and the block holding you back)</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Olivia Gamber &lt;careerevolved=oliviagamber.com@f.kajabimail.net&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Hi Melissa, It is an incredibly frustrating feeling to know exactly what you are capable of, yet watch the door close right at the finish line. To wal</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#48 · Fri, 05 Jun 2026 13:06:04 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Your $20 Credit Is Waiting 🔥 Ends TONIGHT</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Laura Geller &lt;beauty@laurageller.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Save 40% + an Extra 10% ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#50 · Fri, 05 Jun 2026 13:02:59 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Your $20 Credit Is Waiting 🔥 Ends TONIGHT</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Laura Geller &lt;beauty@laurageller.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Save 40% + an Extra 10% ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>
</div>

<div style="background:#faf5ff; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Professional Development / Newsletters (7)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#11 · Fri, 05 Jun 2026 15:00:57 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">The friday 5: AI budgets, papal encyclical, sick leave</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> HR Brain Pickings &lt;newsletter@mail.hrbrainpickings.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">June 05, 2026 | Read online Happy Friday, HR friends! 🙌 Uber&amp;#39;s engineers were told to go all-in on AI coding tools. They did. So enthusiastically,</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#13 · Fri, 05 Jun 2026 10:45:21 -0400</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Let&#x27;s Talk Real-Life Money Decisions</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Sago &lt;Participate@focusgroup.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Hello Melissa We are currently offering $100.00 to our members who qualify and complete a research study on Financial Experiences. Pre-Qualification Q</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#15 · Fri, 05 Jun 2026 06:22:42 -0600</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">It&#x27;s Here: The Sandal Savings Event!</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Shoe Station &lt;customerservice@email.shoestation.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Shop Sandals under $20 + Buy 1 Get 1 FREE Shoe Station You Have 138 Points | Shoe Perks Member $10 coupon offer Sandal Savings Event Sandal Blowout Wo</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#24 · Fri, 05 Jun 2026 14:15:31 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">👨‍💻 [Free Webinar] Why HR Software Decisions Fail</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Phil Strazzulla &lt;ssr-newsletter@mail.beehiiv.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Learn practical ways to build buy-in for your HR software ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#30 · Fri, 5 Jun 2026 14:04:57 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Your subscription ends tomorrow.</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> The CHRO Office &lt;thehroffice@substack.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Melissa, Thank you for your support as a paying subscriber to The CHRO Office. Your paid subscription is about to expire tomorrow. To keep all the ben</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#35 · Fri, 05 Jun 2026 13:50:50 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Melissa Daily Briefing - 2026-06-05 13:50 UTC</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Melissa Daily Briefing &lt;melissaw212@gmail.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Executive Briefing 👋 Good Morning, Melissa! Friday, June 5, 2026 | Prepared by your Executive Chief of Staff 📧 50 Emails Reviewed 📅 9 Calendar Events </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#40 · Fri, 05 Jun 2026 13:29:56 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Important Update About Your Research Opportunities</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Focus Group &lt;participate@focusgroup.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Hello Melissa, We&amp;#39;re reaching out to share an important update about your Focus Group membership and new opportunities available to you. Based on </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>
</div>

<div style="background:#f7fafc; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Promotional / Retail (7)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#1 · Fri, 05 Jun 2026 15:20:09 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">‼️Get more points for your $</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Fetch &lt;fetch@e.fetch.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Supercharged offers to make your points POP off ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#6 · Fri,  5 Jun 2026 15:05:00 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Meet Daisy</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Fayced Aesthetics NYC &lt;info@faycedaestheticsnyc.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Our Newest Nurse Injector + Exclusive New Patient Offer Meet the newest member of the Fayced Aesthetics team Daisy 🌼 We are so excited to introduce th</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#14 · Fri, 05 Jun 2026 14:50:06 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Melissa, flash sale starts now!⏰</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> BellaVitashop &lt;bellavitashop@tiktokshop.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Visit the shop and save big today! ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#19 · Fri, 5 Jun 2026 16:17:58 +0200</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">PUMA x SALEHE BEMBURY Is Here</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> PUMA &lt;email@email.us.puma.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Taking the show on the road ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#20 · Fri, 5 Jun 2026 14:18:28 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">15% Off Catering this Summer!</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Chip City &lt;messages+ml5y60byxd19g@squaremktg.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Have questions? Reply to this email and we&amp;#39;ll respond as soon as possible. Business Website Instagram Account Twitter Account Chip City 15-32 127t</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#44 · Fri, 05 Jun 2026 07:16:55 -0600</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Invite your team to Slack today!</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Slack &lt;no-reply@email.slackhq.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">We&amp;#39;ll help you and your team get started Your team is on a free trial of Pro. Try in Slack → Slack from Salesforce It&amp;#39;s time—give Slack a try </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#47 · Fri, 5 Jun 2026 13:06:12 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Apple’s Starlink Update Sparks Huge Earning Opportunity</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Pre-IPO Offering ✍🏻 Capital Noted&quot; &lt;news@editor.capitalnoted.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Apple just secretly added Starlink satellite support to iPhones through iOS 18.3. One of the biggest potential winners? Mode Mobile. Capital Noted log</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>
</div>

<div style="background:#fff5f5; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Security / Risk (2)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#29 · Fri, 05 Jun 2026 07:33:00 -0600</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Workout drawer: refreshed ✨ Snag 50% OFF all active*</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Old Navy &lt;oldnavy@email.oldnavy.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Plus, Encore Members get ✨ free shipping ✨ on $50+ orders ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Act / Delete if scam</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#38 · Fri, 5 Jun 2026 09:32:18 -0400 (EDT)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">📓 motivation with $0</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Hebba Youssef &lt;ihateithere@workweek.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Proving impact through metrics + keeping people engaged without a budget. I Hate It Here Hebba Youssef Jun 5th, 2026 Read in browser In partnership wi</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Act / Delete if scam</div>
</div>
</div>

