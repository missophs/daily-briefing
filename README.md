<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa Weiss | July 11, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: flex-start; }
  .header-left h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header-left .subtitle { font-size: 15px; color: #a8b4c8; margin-top: 4px; }
  .header-left .date-line { font-size: 13px; color: #7a8fa6; margin-top: 2px; }
  .header-stats { display: flex; gap: 20px; flex-wrap: wrap; justify-content: flex-end; }
  .stat-box { background: rgba(255,255,255,0.08); border-radius: 10px; padding: 12px 20px; text-align: center; }
  .stat-box .num { font-size: 26px; font-weight: 700; color: #e2e8f0; }
  .stat-box .lbl { font-size: 11px; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.8px; }

  /* SECTION */
  .section { background: #fff; border-radius: 12px; padding: 24px 28px; margin-bottom: 20px; box-shadow: 0 1px 6px rgba(0,0,0,0.07); }
  .section-title { font-size: 17px; font-weight: 700; letter-spacing: -0.2px; margin-bottom: 16px; padding-bottom: 10px; border-bottom: 2px solid #e8ecf0; display: flex; align-items: center; gap: 8px; }
  .section-title .icon { font-size: 18px; }

  /* COLOR BANDS */
  .band-red { border-left: 5px solid #dc2626; }
  .band-yellow { border-left: 5px solid #d97706; }
  .band-blue { border-left: 5px solid #2563eb; }
  .band-green { border-left: 5px solid #16a34a; }
  .band-purple { border-left: 5px solid #7c3aed; }
  .band-gray { border-left: 5px solid #6b7280; }
  .band-teal { border-left: 5px solid #0891b2; }

  /* EXECUTIVE SUMMARY */
  .exec-bullets { list-style: none; display: flex; flex-direction: column; gap: 10px; }
  .exec-bullets li { padding: 12px 16px; border-radius: 8px; font-size: 14px; display: flex; gap: 10px; align-items: flex-start; }
  .exec-bullets li .tag { font-weight: 700; font-size: 11px; text-transform: uppercase; letter-spacing: 0.8px; white-space: nowrap; margin-top: 1px; }
  .exec-bullets li.risk { background: #fef2f2; border-left: 4px solid #dc2626; }
  .exec-bullets li.risk .tag { color: #dc2626; }
  .exec-bullets li.opp { background: #f0fdf4; border-left: 4px solid #16a34a; }
  .exec-bullets li.opp .tag { color: #16a34a; }
  .exec-bullets li.cal { background: #eff6ff; border-left: 4px solid #2563eb; }
  .exec-bullets li.cal .tag { color: #2563eb; }

  /* ACTION CARDS */
  .action-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; }
  .action-card { border-radius: 10px; padding: 16px 18px; border: 1px solid #e2e8f0; }
  .action-card .ac-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
  .action-card .ac-title { font-size: 15px; font-weight: 700; margin-bottom: 4px; }
  .action-card .ac-source { font-size: 11px; color: #64748b; margin-bottom: 8px; }
  .action-card .ac-row { display: flex; gap: 6px; margin-bottom: 4px; font-size: 13px; }
  .action-card .ac-row strong { min-width: 90px; color: #374151; }
  .action-card .ac-due { background: #fef3c7; color: #92400e; font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 12px; display: inline-block; margin-top: 8px; }
  .card-red { background: #fff5f5; border-color: #fecaca; }
  .card-red .ac-label { color: #dc2626; }
  .card-yellow { background: #fffbeb; border-color: #fde68a; }
  .card-yellow .ac-label { color: #d97706; }
  .card-green { background: #f0fdf4; border-color: #bbf7d0; }
  .card-green .ac-label { color: #16a34a; }
  .card-blue { background: #eff6ff; border-color: #bfdbfe; }
  .card-blue .ac-label { color: #2563eb; }
  .card-purple { background: #faf5ff; border-color: #ddd6fe; }
  .card-purple .ac-label { color: #7c3aed; }

  /* CALENDAR */
  .cal-day { margin-bottom: 20px; }
  .cal-day-header { background: #1e293b; color: #fff; border-radius: 8px 8px 0 0; padding: 8px 16px; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; }
  .cal-day-header.today { background: #0f3460; }
  .cal-event { border: 1px solid #e2e8f0; border-top: none; padding: 12px 16px; display: grid; grid-template-columns: 100px 1fr; gap: 12px; background: #fff; }
  .cal-event:last-child { border-radius: 0 0 8px 8px; }
  .cal-event.conflict { background: #fff5f5; border-color: #fecaca; }
  .cal-time { font-size: 13px; font-weight: 600; color: #374151; }
  .cal-allday { font-size: 11px; font-weight: 700; color: #7c3aed; background: #ede9fe; padding: 2px 6px; border-radius: 4px; display: inline-block; }
  .cal-event-name { font-size: 14px; font-weight: 700; color: #1e293b; }
  .cal-meta { font-size: 12px; color: #64748b; margin-top: 2px; }
  .cal-meta a { color: #2563eb; }
  .status-badge { display: inline-block; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; padding: 2px 7px; border-radius: 10px; margin-right: 4px; }
  .status-confirmed { background: #dcfce7; color: #16a34a; }
  .status-accepted { background: #dcfce7; color: #16a34a; }
  .status-needsaction { background: #fef3c7; color: #d97706; }
  .status-declined { background: #fee2e2; color: #dc2626; }
  .conflict-badge { background: #fef2f2; color: #dc2626; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 6px; }

  /* JOB PIPELINE */
  .job-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .job-table th { background: #1e293b; color: #e2e8f0; padding: 9px 12px; text-align: left; font-size: 11px; text-transform: uppercase; letter-spacing: 0.7px; }
  .job-table td { padding: 10px 12px; border-bottom: 1px solid #f1f5f9; vertical-align: top; }
  .job-table tr:last-child td { border-bottom: none; }
  .job-table tr:hover td { background: #f8fafc; }
  .fit-high { color: #16a34a; font-weight: 700; font-size: 11px; }
  .fit-med { color: #d97706; font-weight: 700; font-size: 11px; }
  .fit-low { color: #6b7280; font-weight: 700; font-size: 11px; }
  .pill { display: inline-block; padding: 2px 8px; border-radius: 10px; font-size: 10px; font-weight: 700; text-transform: uppercase; }
  .pill-green { background: #dcfce7; color: #166534; }
  .pill-yellow { background: #fef3c7; color: #92400e; }
  .pill-blue { background: #dbeafe; color: #1e40af; }
  .pill-gray { background: #f1f5f9; color: #475569; }

  /* EMAIL REVIEW */
  .email-cat { margin-bottom: 16px; border-radius: 10px; overflow: hidden; border: 1px solid #e2e8f0; }
  .email-cat-header { padding: 12px 16px; display: flex; justify-content: space-between; align-items: center; }
  .email-cat-header h3 { font-size: 14px; font-weight: 700; }
  .email-cat-header .count-badge { font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 10px; }
  .email-cat-body { padding: 12px 16px; background: #fff; font-size: 13px; }
  .email-cat-body .sender-list { margin: 6px 0 8px 0; }
  .email-cat-body .sender-list li { list-style: none; padding: 3px 0; border-bottom: 1px solid #f1f5f9; }
  .email-cat-body .sender-list li:last-child { border-bottom: none; }
  .rec-action { margin-top: 8px; font-size: 12px; font-weight: 600; }
  .header-red { background: #fef2f2; }
  .header-red h3 { color: #dc2626; }
  .header-red .count-badge { background: #fee2e2; color: #dc2626; }
  .header-yellow { background: #fffbeb; }
  .header-yellow h3 { color: #d97706; }
  .header-yellow .count-badge { background: #fef3c7; color: #d97706; }
  .header-blue { background: #eff6ff; }
  .header-blue h3 { color: #2563eb; }
  .header-blue .count-badge { background: #dbeafe; color: #2563eb; }
  .header-green { background: #f0fdf4; }
  .header-green h3 { color: #16a34a; }
  .header-green .count-badge { background: #dcfce7; color: #16a34a; }
  .header-purple { background: #faf5ff; }
  .header-purple h3 { color: #7c3aed; }
  .header-purple .count-badge { background: #ede9fe; color: #7c3aed; }
  .header-gray { background: #f8fafc; }
  .header-gray h3 { color: #475569; }
  .header-gray .count-badge { background: #e2e8f0; color: #475569; }
  .header-teal { background: #f0fdfa; }
  .header-teal h3 { color: #0891b2; }
  .header-teal .count-badge { background: #cffafe; color: #0891b2; }

  /* TRASH */
  .trash-group { margin-bottom: 16px; }
  .trash-group h4 { font-size: 13px; font-weight: 700; margin-bottom: 8px; padding: 6px 10px; border-radius: 6px; }
  .restore-header { background: #fef3c7; color: #92400e; }
  .review-header { background: #ede9fe; color: #5b21b6; }
  .delete-header { background: #f1f5f9; color: #475569; }
  .trash-item { padding: 8px 12px; border: 1px solid #e2e8f0; border-radius: 6px; margin-bottom: 6px; font-size: 13px; background: #fff; }
  .trash-item .ts { font-weight: 600; color: #1e293b; }
  .trash-item .tr { color: #64748b; margin-top: 2px; }

  /* PROMO */
  .promo-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .promo-table th { background: #374151; color: #f9fafb; padding: 8px 12px; text-align: left; font-size: 11px; text-transform: uppercase; letter-spacing: 0.7px; }
  .promo-table td { padding: 9px 12px; border-bottom: 1px solid #f1f5f9; }
  .promo-table tr:last-child td { border-bottom: none; }
  .rec-delete { color: #dc2626; font-weight: 700; }
  .rec-review { color: #d97706; font-weight: 700; }
  .rec-keep { color: #16a34a; font-weight: 700; }
  .rec-ignore { color: #6b7280; font-weight: 700; }

  /* ACCOUNTING */
  .acct-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .acct-table th { background: #1e293b; color: #e2e8f0; padding: 9px 14px; text-align: left; font-size: 11px; text-transform: uppercase; letter-spacing: 0.7px; }
  .acct-table td { padding: 9px 14px; border-bottom: 1px solid #f1f5f9; }
  .acct-table tr:last-child td { border-bottom: none; }
  .acct-table .total-row td { background: #1e293b; color: #fff; font-weight: 700; }
  .acct-table tr:hover td { background: #f8fafc; }
  .acct-table .total-row:hover td { background: #1e293b; }

  /* DASHBOARD */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-card { border-radius: 10px; padding: 14px 16px; }
  .dash-card .dch { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 8px; }
  .dash-card ul { list-style: none; }
  .dash-card ul li { font-size: 12px; padding: 3px 0; border-bottom: 1px solid rgba(0,0,0,0.06); }
  .dash-card ul li:last-child { border-bottom: none; }
  .dc-red { background: #fef2f2; border: 1px solid #fecaca; }
  .dc-red .dch { color: #dc2626; }
  .dc-yellow { background: #fffbeb; border: 1px solid #fde68a; }
  .dc-yellow .dch { color: #d97706; }
  .dc-green { background: #f0fdf4; border: 1px solid #bbf7d0; }
  .dc-green .dch { color: #16a34a; }
  .dc-blue { background: #eff6ff; border: 1px solid #bfdbfe; }
  .dc-blue .dch { color: #2563eb; }
  .dc-purple { background: #faf5ff; border: 1px solid #ddd6fe; }
  .dc-purple .dch { color: #7c3aed; }
  .dc-gray { background: #f8fafc; border: 1px solid #e2e8f0; }
  .dc-gray .dch { color: #64748b; }

  /* ACTION TABLE */
  .act-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .act-table th { background: #1e293b; color: #e2e8f0; padding: 9px 14px; text-align: left; font-size: 11px; text-transform: uppercase; letter-spacing: 0.7px; }
  .act-table td { padding: 10px 14px; border-bottom: 1px solid #f1f5f9; vertical-align: top; }
  .act-table tr:last-child td { border-bottom: none; }
  .act-table tr:hover td { background: #f8fafc; }
  .pri-high { color: #dc2626; font-weight: 700; font-size: 11px; }
  .pri-med { color: #d97706; font-weight: 700; font-size: 11px; }
  .pri-low { color: #16a34a; font-weight: 700; font-size: 11px; }

  /* TOP 3 */
  .top3 { counter-reset: top3; }
  .top3-item { display: flex; gap: 16px; align-items: flex-start; padding: 14px 18px; border-radius: 10px; margin-bottom: 12px; }
  .top3-item:nth-child(1) { background: #fef2f2; border-left: 5px solid #dc2626; }
  .top3-item:nth-child(2) { background: #f0fdf4; border-left: 5px solid #16a34a; }
  .top3-item:nth-child(3) { background: #eff6ff; border-left: 5px solid #2563eb; }
  .top3-num { font-size: 26px; font-weight: 800; color: #94a3b8; min-width: 32px; line-height: 1; }
  .top3-content h4 { font-size: 15px; font-weight: 700; margin-bottom: 4px; }
  .top3-content p { font-size: 13px; color: #475569; }

  /* MISC */
  .note { font-size: 12px; color: #64748b; font-style: italic; margin-top: 8px; }
  .divider { border: none; border-top: 1px solid #e8ecf0; margin: 12px 0; }
  .scam-badge { background: #fee2e2; color: #991b1b; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 8px; }
  .auto-trash-badge { background: #fef3c7; color: #78350f; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 8px; }

  @media (max-width: 640px) {
    .header { flex-direction: column; gap: 16px; }
    .header-stats { justify-content: flex-start; }
    .action-grid { grid-template-columns: 1fr; }
  }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ═══════════════════════════════════════════════
     1. HEADER
═══════════════════════════════════════════════ -->
<div class="header">
  <div class="header-left">
    <h1>Good Morning, Melissa 👋</h1>
    <div class="subtitle">Executive Briefing — Prepared by Your Chief of Staff</div>
    <div class="date-line">Saturday, July 11, 2026 &nbsp;·&nbsp; New York, NY</div>
  </div>
  <div class="header-stats">
    <div class="stat-box">
      <div class="num">50</div>
      <div class="lbl">Emails Reviewed</div>
    </div>
    <div class="stat-box">
      <div class="num">10</div>
      <div class="lbl">Calendar Events</div>
    </div>
    <div class="stat-box">
      <div class="num">3</div>
      <div class="lbl">Action Required</div>
    </div>
    <div class="stat-box">
      <div class="num">5</div>
      <div class="lbl">Job Alerts</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     2. EXECUTIVE SUMMARY
═══════════════════════════════════════════════ -->
<div class="section band-red">
  <div class="section-title"><span class="icon">📋</span> Executive Summary</div>
  <ul class="exec-bullets">
    <li class="risk">
      <span class="tag">🔴 Biggest Risk</span>
      <span>You have two active Bank of America billing disputes (accounts -2994 and -4018) requiring additional information — one is Step 2 of 3 and awaiting merchant bank review. Northwell Health also posted a new test result this morning. Both require your attention today. Additionally, multiple phishing/scam emails were intercepted and auto-trashed.</span>
    </li>
    <li class="opp">
      <span class="tag">🟢 Top Opportunity</span>
      <span>Five high-caliber LinkedIn job alerts arrived overnight: VP of People (Nitra), Senior Director People BP (GitLab), Senior People BP (BNY), Vice President HR (PeopleOps Jobs), and People Strategy Lead (Ladders, up to $287K). You also emailed yourself 3 LinkedIn job links and a Greenhouse application link Friday evening — strong momentum to act on this weekend.</span>
    </li>
    <li class="cal">
      <span class="tag">🔵 Calendar Priority</span>
      <span>Next week is dense with health appointments (bone density scan + LHRadiology imaging both on Wednesday July 15 at 8:30 AM — confirmed overlap), Stephanie's infusion reminder Monday July 13, and two professional networking Zoom sessions (Wednesday + Thursday) needing RSVPs. Tea with LeiLani on Thursday July 16 is accepted and in-person at T Shop.</span>
    </li>
  </ul>
</div>

<!-- ═══════════════════════════════════════════════
     3. ACTION REQUIRED
═══════════════════════════════════════════════ -->
<div class="section band-yellow">
  <div class="section-title"><span class="icon">⚡</span> Action Required</div>
  <div class="action-grid">

    <div class="action-card card-red">
      <div class="ac-label">🔴 Medical — Urgent</div>
      <div class="ac-title">New Test Result Available — Northwell Health</div>
      <div class="ac-source">From: MyNorthwell &lt;northwell@my.northwellhealth.com&gt;</div>
      <div class="ac-row"><strong>Why it matters:</strong> A new test result was posted at 11:03 AM today. Results may be available before your provider has reviewed them.</div>
      <div class="ac-row"><strong>Next step:</strong> Log into MyNorthwell app or portal now to review your results.</div>
      <span class="ac-due">📅 Due: Today, July 11</span>
    </div>

    <div class="action-card card-yellow">
      <div class="ac-label">🟡 Financial — Action Needed</div>
      <div class="ac-title">BofA Billing Dispute (Account -2994): Additional Info Requested</div>
      <div class="ac-source">From: Bank of America &lt;onlinebanking@ealerts.bankofamerica.com&gt;</div>
      <div class="ac-row"><strong>Why it matters:</strong> Step 2 of 3 in your dispute process — BofA is requesting additional information to proceed.</div>
      <div class="ac-row"><strong>Next step:</strong> Log into Bank of America online banking and submit the requested documentation immediately.</div>
      <span class="ac-due">📅 Due: ASAP — delays may affect outcome</span>
    </div>

    <div class="action-card card-yellow">
      <div class="ac-label">🟡 Financial — In Review</div>
      <div class="ac-title">BofA Billing Dispute (Account -4018): Merchant Bank Review</div>
      <div class="ac-source">From: Bank of America &lt;onlinebanking@ealerts.bankofamerica.com&gt;</div>
      <div class="ac-row"><strong>Why it matters:</strong> Your dispute on account -4018 has been forwarded to the merchant's bank for Step 2 review — no action today, but monitor closely.</div>
      <div class="ac-row"><strong>Next step:</strong> Log in to confirm status; note any deadlines to respond if merchant disputes your claim.</div>
      <span class="ac-due">📅 Monitor daily</span>
    </div>

    <div class="action-card card-yellow">
      <div class="ac-label">🟡 Medical — Scheduling</div>
      <div class="ac-title">Quest Diagnostics Lab Order — Appointment Needed</div>
      <div class="ac-source">From: Quest Diagnostics &lt;NoReply@questdiagnostics.com&gt;</div>
      <div class="ac-row"><strong>Why it matters:</strong> Your healthcare provider sent a test order to Quest Diagnostics on July 9, 2026. You have not yet registered or scheduled your appointment.</div>
      <div class="ac-row"><strong>Next step:</strong> Visit QuestDiagnostics.com to register and book your appointment now.</div>
      <span class="ac-due">📅 Order received July 9 — schedule ASAP</span>
    </div>

    <div class="action-card card-blue">
      <div class="ac-label">🔵 Calendar — RSVP Needed</div>
      <div class="ac-title">HR Networking & Job Search Group — Zoom (Wed + Thu)</div>
      <div class="ac-source">Google Calendar — Status: Needs Action</div>
      <div class="ac-row"><strong>Why it matters:</strong> Two HR networking Zoom sessions this week have no RSVP: Wed July 15 (12–1:30 PM) and Thu July 16 (12–1 PM). Both are open to your existing networking group.</div>
      <div class="ac-row"><strong>Next step:</strong> Accept or decline both calendar invites today.</div>
      <span class="ac-due">📅 Events: July 15 & 16</span>
    </div>

    <div class="action-card card-green">
      <div class="ac-label">🟢 Job Search — Cornerstone</div>
      <div class="ac-title">Cornerstone Profile — Candidate Data Notice</div>
      <div class="ac-source">From: careers@csod.com</div>
      <div class="ac-row"><strong>Why it matters:</strong> Cornerstone (CSOD) reached out about your candidate profile and personal data transparency. This may indicate an active application or recruiter interest.</div>
      <div class="ac-row"><strong>Next step:</strong> Read the full email, verify your profile is complete and up to date on Cornerstone Galaxy.</div>
      <span class="ac-due">📅 Review today</span>
    </div>

    <div class="action-card card-green">
      <div class="ac-label">🟢 Job Search — Self-Submitted Links</div>
      <div class="ac-title">3 Job Links Emailed to Yourself Friday Evening</div>
      <div class="ac-source">From: Melissa W &lt;melissaw212@gmail.com&gt; — 3 emails re: "Job"</div>
      <div class="ac-row"><strong>Why it matters:</strong> You sent yourself 3 job URLs Friday night (LinkedIn x2 + Greenhouse/Garner Health). These need to be reviewed and applied to this weekend.</div>
      <div class="ac-row"><strong>Next step:</strong> Open each link, assess fit, and apply or add to your pipeline tracker.</div>
      <span class="ac-due">📅 This weekend</span>
    </div>

    <div class="action-card card-purple">
      <div class="ac-label">🟣 LinkedIn — Profile Visibility</div>
      <div class="ac-title">Profile Appeared in 3 Searches — Plank Enterprises Found You</div>
      <div class="ac-source">From: LinkedIn &lt;notifications-noreply@linkedin.com&gt;</div>
      <div class="ac-row"><strong>Why it matters:</strong> Someone from Plank Enterprises, Inc. found your profile. You appeared in 3 searches this week — signals active recruiter interest.</div>
      <div class="ac-row"><strong>Next step:</strong> Review who searched for you in LinkedIn "Who Viewed Your Profile" and reach out proactively if appropriate.</div>
      <span class="ac-due">📅 Today or Sunday</span>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════
     4. FULL 7-DAY CALENDAR
═══════════════════════════════════════════════ -->
<div class="section band-blue">
  <div class="section-title"><span class="icon">📅</span> Full 7-Day Calendar &nbsp;<span style="font-size:13px;font-weight:400;color:#64748b;">July 11 – July 17, 2026</span></div>

  <!-- SAT JUL 11 -->
  <div class="cal-day">
    <div class="cal-day-header today">Saturday, July 11, 2026 — TODAY</div>
    <div class="cal-event">
      <div class="cal-time">—</div>
      <div>
        <div class="cal-event-name">No calendar events scheduled today</div>
        <div class="cal-meta">Use today to review medical results, bank disputes, and job applications.</div>
      </div>
    </div>
  </div>

  <!-- SUN JUL 12 -->
  <div class="cal-day">
    <div class="cal-day-header">Sunday, July 12, 2026</div>
    <div class="cal-event">
      <div class="cal-time">—</div>
      <div>
        <div class="cal-event-name">No calendar events scheduled</div>
        <div class="cal-meta">Good day to complete job applications from your self-emailed links and research upcoming roles.</div>
      </div>
    </div>
  </div>

  <!-- MON JUL 13 -->
  <div class="cal-day">
    <div class="cal-day-header">Monday, July 13, 2026</div>
    <div class="cal-event">
      <div class="cal-time"><span class="cal-allday">All Day</span></div>
      <div>
        <div class="cal-event-name">Stephanie — Infusion</div>
        <div class="cal-meta">
          <span class="status-badge status-confirmed">Confirmed</span>
          No location listed · No attendees listed
        </div>
        <div class="cal-meta" style="margin-top:4px;">⚠️ <strong>Prep:</strong> Confirm Stephanie's appointment location and any transportation or support logistics. This is an all-day reminder block (spans July 13–14).</div>
      </div>
    </div>
  </div>

  <!-- TUE JUL 14 -->
  <div class="cal-day">
    <div class="cal-day-header">Tuesday, July 14, 2026</div>
    <div class="cal-event">
      <div class="cal-time">10:00 AM<br><span style="font-size:11px;color:#94a3b8;">11:00 AM</span></div>
      <div>
        <div class="cal-event-name">Stella</div>
        <div class="cal-meta">
          <span class="status-badge status-confirmed">Confirmed</span>
          No location listed · No attendees listed
        </div>
        <div class="cal-meta" style="margin-top:4px;">📝 <strong>Prep:</strong> No description provided. Confirm what this appointment is (personal, professional, or medical) and prepare accordingly.</div>
      </div>
    </div>
  </div>

  <!-- WED JUL 15 -->
  <div class="cal-day">
    <div class="cal-day-header">Wednesday, July 15, 2026</div>

    <div class="cal-event conflict">
      <div class="cal-time">8:30 AM<br><span style="font-size:11px;color:#94a3b8;">9:30 AM</span></div>
      <div>
        <div class="cal-event-name">Bone Density Appointment <span class="conflict-badge">⚠️ TIME CONFLICT</span></div>
        <div class="cal-meta">
          <span class="status-badge status-confirmed">Confirmed</span>
          No location listed
        </div>
        <div class="cal-meta" style="margin-top:4px;">⚠️ <strong>Conflict:</strong> This overlaps exactly with the LHRadiology Imaging Appointment below (both 8:30 AM). Verify whether these are the same appointment or two separate ones requiring coordination.</div>
      </div>
    </div>

    <div class="cal-event conflict">
      <div class="cal-time">8:30 AM<br><span style="font-size:11px;color:#94a3b8;">9:05 AM</span></div>
      <div>
        <div class="cal-event-name">IMAGING APPOINTMENT: LHRadiology <span class="conflict-badge">⚠️ TIME CONFLICT</span></div>
        <div class="cal-meta">
          <span class="status-badge status-confirmed">Confirmed</span>
          📍 400 East 66th Street, New York
        </div>
        <div class="cal-meta" style="margin-top:4px;">📝 <strong>Prep:</strong> Complete pre-registration forms before arrival to reduce check-in time. Bring updated personal information. Check-in time: 8:30 AM. ⚠️ <strong>Possible duplicate/overlap with Bone Density event — confirm with provider.</strong></div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">12:00 PM<br><span style="font-size:11px;color:#94a3b8;">1:30 PM</span></div>
      <div>
        <div class="cal-event-name">HR Networking & Job Search Group — Zoom 2</div>
        <div class="cal-meta">
          <span class="status-badge status-needsaction">⚠️ RSVP Needed</span>
          🔗 <a href="https://us06web.zoom.us/j/81954171722" target="_blank">Zoom Link</a> · ~175+ attendees
        </div>
        <div class="cal-meta" style="margin-top:4px;">📝 <strong>Prep:</strong> Review HR Networking Team Guidelines before joining. Large group session — prepare a brief intro or update. <strong>Action: Accept or decline this invite today.</strong></div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">12:00 PM<br><span style="font-size:11px;color:#94a3b8;">1:30 PM</span></div>
      <div>
        <div class="cal-event-name">Network (Personal Block)</div>
        <div class="cal-meta">
          <span class="status-badge status-confirmed">Confirmed</span>
          No location listed — appears to mirror the Zoom session above
        </div>
        <div class="cal-meta" style="margin-top:4px;">📝 Likely companion block to the HR Networking Zoom. No additional prep needed beyond Zoom session above.</div>
      </div>
    </div>
  </div>

  <!-- THU JUL 16 -->
  <div class="cal-day">
    <div class="cal-day-header">Thursday, July 16, 2026</div>

    <div class="cal-event">
      <div class="cal-time">9:00 AM<br><span style="font-size:11px;color:#94a3b8;">10:30 AM</span></div>
      <div>
        <div class="cal-event-name">Executive Roundtable (John Madigan)</div>
        <div class="cal-meta">
          <span class="status-badge status-declined">Declined</span>
          🔗 <a href="https://us02web.zoom.us/j/207786667" target="_blank">Zoom Link</a> · Meeting ID: 207 786 667 · PW: 205454
        </div>
        <div class="cal-meta" style="margin-top:4px;">ℹ️ You have declined this event. No action needed unless you wish to reconsider — this could be a valuable executive networking opportunity given your job search.</div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">12:00 PM<br><span style="font-size:11px;color:#94a3b8;">1:00 PM</span></div>
      <div>
        <div class="cal-event-name">HR Networking & Job Search: Open Office Hours — Zoom 2</div>
        <div class="cal-meta">
          <span class="status-badge status-needsaction">⚠️ RSVP Needed</span>
          🔗 <a href="https://us06web.zoom.us/j/85945371140" target="_blank">Zoom Link</a> · ~175+ attendees
        </div>
        <div class="cal-meta" style="margin-top:4px;">📝 <strong>Prep:</strong> Casual open discussion — no AI notetakers per organizer. Good forum for job search updates and peer support. <strong>Action: RSVP today.</strong></div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">1:00 PM<br><span style="font-size:11px;color:#94a3b8;">2:00 PM</span></div>
      <div>
        <div class="cal-event-name">Tea with LeiLani | Brew At the Table</div>
        <div class="cal-meta">
          <span class="status-badge status-accepted">Accepted</span>
          📍 T Shop, 247 Elizabeth St, New York, NY 10012
        </div>
        <div class="cal-meta" style="margin-top:4px;">
          👥 Attendees: leilani@bethechangehr.com, tlow@teresalowconsulting.com, leylasnovini@gmail.com, jessi@alvisolutions.com<br>
          📝 <strong>Prep:</strong> In-person event — plan travel time. Great HR/career networking opportunity. Bring business cards or LinkedIn QR. Confirm your Acuity scheduling link if needed.
        </div>
      </div>
    </div>
  </div>

  <!-- FRI JUL 17 -->
  <div class="cal-day">
    <div class="cal-day-header">Friday, July 17, 2026</div>
    <div class="cal-event">
      <div class="cal-time">3:00 PM<br><span style="font-size:11px;color:#94a3b8;">4:00 PM</span></div>
      <div>
        <div class="cal-event-name">Dr. Yuen</div>
        <div class="cal-meta">
          <span class="status-badge status-confirmed">Confirmed</span>
          No location listed · No attendees listed
        </div>
        <div class="cal-meta" style="margin-top:4px;">📝 <strong>Prep:</strong> Confirm appointment location and any forms needed. With Northwell test results arriving today and Quest lab order pending, bring any recent test results to this appointment.</div>
      </div>
    </div>
  </div>

</div><!-- end calendar section -->

<!-- ═══════════════════════════════════════════════
     5. JOB SEARCH & INTERVIEW PIPELINE
═══════════════════════════════════════════════ -->
<div class="section band-green">
  <div class="section-title"><span class="icon">💼</span> Job Search & Interview Pipeline</div>
  <table class="job-table">
    <thead>
      <tr>
        <th>Role</th>
        <th>Company</th>
        <th>Source</th>
        <th>Date</th>
        <th>Fit</th>
        <th>Status</th>
        <th>Next Step</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>VP of People</strong></td>
        <td>Nitra</td>
        <td>LinkedIn Job Alert</td>
        <td>July 8, 2026</td>
        <td><span class="fit-high">HIGH</span></td>
        <td><span class="pill pill-yellow">Alert Received ×2</span></td>
        <td>Open LinkedIn link; apply or save</td>
      </tr>
      <tr>
        <td><strong>Senior Director, People Business Partner</strong></td>
        <td>GitLab</td>
        <td>LinkedIn Job Alert</td>
        <td>July 9, 2026</td>
        <td><span class="fit-high">HIGH</span></td>
        <td><span class="pill pill-yellow">Alert Received</span></td>
        <td>Research role & apply this weekend</td>
      </tr>
      <tr>
        <td><strong>Senior People Business Partner</strong></td>
        <td>BNY</td>
        <td>LinkedIn Job Alert</td>
        <td>July 9, 2026</td>
        <td><span class="fit-high">HIGH</span></td>
        <td><span class="pill pill-yellow">Alert Received</span></td>
        <td>Research BNY culture; apply ASAP</td>
      </tr>
      <tr>
        <td><strong>Vice President Human Resources</strong></td>
        <td>PeopleOps Jobs</td>
        <td>LinkedIn Job Alert</td>
        <td>July 9, 2026</td>
        <td><span class="fit-high">HIGH</span></td>
        <td><span class="pill pill-yellow">Alert Received</span></td>
        <td>Review job board listing; apply</td>
      </tr>
      <tr>
        <td><strong>People Strategy Lead</strong></td>
        <td>Ladders (up to $287K/yr)</td>
        <td>LinkedIn Job Alert</td>
        <td>July 9, 2026</td>
        <td><span class="fit-high">HIGH</span></td>
        <td><span class="pill pill-yellow">Alert Received</span></td>
        <td>Prioritize — strong comp. Apply now</td>
      </tr>
      <tr>
        <td><strong>LinkedIn Job #1</strong></td>
        <td>Unknown (self-sent)</td>
        <td>Self-email: linkedin.com/jobs/view/4427857816</td>
        <td>Jul 10, 2026</td>
        <td><span class="fit-med">REVIEW</span></td>
        <td><span class="pill pill-blue">Self-Tagged</span></td>
        <td>Open link and assess fit this weekend</td>
      </tr>
      <tr>
        <td><strong>LinkedIn Job #2</strong></td>
        <td>Unknown (self-sent)</td>
        <td>Self-email: linkedin.com/jobs/view/4438868575</td>
        <td>Jul 10, 2026</td>
        <td><span class="fit-med">REVIEW</span></td>
        <td><span class="pill pill-blue">Self-Tagged</span></td>
        <td>Open link and assess fit this weekend</td>
      </tr>
      <tr>
        <td><strong>Job via Greenhouse</strong></td>
        <td>Garner Health</td>
        <td>Self-email: greenhouse.io/garnerhealth/jobs/6113093004</td>
        <td>Jul 10, 2026</td>
        <td><span class="fit-med">REVIEW</span></td>
        <td><span class="pill pill-blue">Self-Tagged</span></td>
        <td>Open Greenhouse link; apply if strong fit</td>
      </tr>
      <tr>
        <td><strong>Multiple NYC Roles</strong></td>
        <td>Amazon Web Services, Azaaki Solutions + others</td>
        <td>Glassdoor Jobs (×2 duplicate emails)</td>
        <td>Jul 11, 2026</td>
        <td><span class="fit-low">LOW-MED</span></td>
        <td><span class="pill pill-gray">Alert (Duplicate)</span></td>
        <td>Scan Glassdoor alerts; filter relevant roles</td>
      </tr>
      <tr>
        <td><strong>Cornerstone Profile Review</strong></td>
        <td>Cornerstone OnDemand (CSOD)</td>
        <td>careers@csod.com</td>
        <td>Jul 11, 2026</td>
        <td><span class="fit-med">MEDIUM</span></td>
        <td><span class="pill pill-yellow">Outreach Received</span></td>
        <td>Read full email; update Cornerstone profile</td>
      </tr>
      <tr>
        <td><strong>Profile Viewed × 3 Searches</strong></td>
        <td>Plank Enterprises, Inc. + others</td>
        <td>LinkedIn Notification</td>
        <td>Jul 11, 2026</td>
        <td><span class="fit-med">MEDIUM</span></td>
        <td><span class="pill pill-green">Recruiter Interest</span></td>
        <td>Check who viewed profile; send connection request</td>
      </tr>
      <tr>
        <td><strong>Executive Roundtable</strong></td>
        <td>John Madigan (Zoom)</td>
        <td>Google Calendar</td>
        <td>Jul 16, 2026</td>
        <td><span class="fit-med">MEDIUM</span></td>
        <td><span class="pill pill-gray">Declined</span></td>
        <td>Reconsider — good exec networking during search</td>
      </tr>
      <tr>
        <td><strong>Tea with LeiLani</strong></td>
        <td>Be The Change HR / T Shop NYC</td>
        <td>Google Calendar</td>
        <td>Jul 16, 2026</td>
        <td><span class="fit-high">HIGH</span></td>
        <td><span class="pill pill-green">Accepted ✓</span></td>
        <td>Attend in-person; bring materials, LinkedIn QR</td>
      </tr>
      <tr>
        <td><strong>HR Networking Zoom Group</strong></td>
        <td>HR Job Search Networking Group</td>
        <td>Google Calendar (×2)</td>
        <td>Jul 15 & 16, 2026</td>
        <td><span class="fit-high">HIGH</span></td>
        <td><span class="pill pill-yellow">RSVP Needed</span></td>
        <td>Accept both invites; prepare brief intro</td>
      </tr>
    </tbody>
  </table>
  <p class="note">* VP of People at Nitra appeared in two separate LinkedIn alerts (July 8 date, sent at different times) — counted as one role.</p>
</div>

<!-- ═══════════════════════════════════════════════
     6. FULL EMAIL REVIEW BY CATEGORY
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">📧</span> Full Email Review by Category</div>

  <!-- SECURITY / RISK -->
  <div class="email-cat">
    <div class="email-cat-header header-red">
      <h3>🔴 Security / Risk</h3>
      <span class="count-badge" style="background:#fee2e2;color:#dc2626;">6 emails</span>
    </div>
    <div class="email-cat-body">
      <p><strong>Summary:</strong> Six emails flagged as phishing, scams, or social engineering. Four were auto-trashed by system before delivery. Two remain in non-inbox, non-trash limbo (unactioned).</p>
      <ul class="sender-list">
        <li>
          <span class="scam-badge">PHISHING</span> <strong>"Payout-Confirmation" &lt;khutcrrhkog@breh.vhozsrknquiew.us&gt;</strong> — "Final Step: melissaw212, Confirm Your Account & Unlock Your $5000 Bonus" <span class="auto-trash-badge">AUTO-TRASHED</span><br>
          <span style="font-size:12px;color:#64748b;">Reason: Randomly generated sender domain, uses recipient email username to personalize urgency, fake payout/bonus scam.</span>
        </li>
        <li>
          <span class="scam-badge">PHISHING</span> <strong>"David Wallace" &lt;ariffnazme@oum.edu.my&gt;</strong> — "Account Update: Billing configuration needed" <span class="auto-trash-badge">AUTO-TRASHED</span><br>
          <span style="font-size:12px;color:#64748b;">Reason: Spoofed personal name via academic domain; critical security warning demanding immediate action — credential harvesting attempt.</span>
        </li>
        <li>
          <span class="scam-badge">SCAM</span> <strong>"🔶FUCK-BUDDY SECRET🔶" &lt;info@vwk.ecxdnjmcnxsgk.us&gt;</strong> — Explicit adult spam<br>
          <span style="font-size:12px;color:#64748b;">Located in non-inbox. Delete immediately. Not auto-trashed — manually delete and mark as spam.</span>
        </li>
        <li>
          <span class="scam-badge">SCAM</span> <strong>"Wild_Online♦️" &lt;1vxqsikf5s@ol45y9833v.us&gt;</strong> — "250 Welcome Free Spins [melissaw212]" <span class="auto-trash-badge">AUTO-TRASHED</span><br>
          <span style="font-size:12px;color:#64748b;">Reason: Random domain, targets by username — casino spam/scam lure.</span>
        </li>
        <li>
          <span class="scam-badge">SCAM</span> <strong>melissaw212 &lt;clzsupportnhus@wktjarscmsykqkyihqmkoxsh.com&gt;</strong> — "You received a direct deposited of 8000.00 💲" (in trash)<br>
          <span style="font-size:12px;color:#64748b;">Spoofed as your own address. Yabby Casino scam. In trash — delete permanently.</span>
        </li>
        <li>
          <span class="scam-badge">SCAM</span> <strong>"'Congratulations🎉'" &lt;fffdhhgdmaacbk...@ysh74y...us&gt;</strong> — "130 Free Spins 💰 No deposit Needed"<br>
          <span style="font-size:12px;color:#64748b;">Located in non-inbox. Casino Limitless scam. Delete immediately.</span>
        </li>
      </ul>
      <div class="rec-action" style="color:#dc2626;">⚡ Action: Auto-trashed items require no further action. Manually delete the 3 non-auto-trashed scam emails and mark as spam. Do not click any links.</div>
    </div>
  </div>

  <!-- JOB SEARCH -->
  <div class="email-cat">
    <div class="email-cat-header header-green">
      <h3>🟢 Job Search</h3>
      <span class="count-badge" style="background:#dcfce7;color:#16a34a;">8 emails</span>
    </div>
    <div class="email-cat-body">
      <p><strong>Summary:</strong> 5 LinkedIn job alerts, 2 Glassdoor job alerts (duplicate content), 1 Cornerstone profile inquiry, and 3 self-sent job links (counted under Personal/Self). All warrant action this weekend.</p>
      <ul class="sender-list">
        <li><strong>LinkedIn Job Alerts</strong> — VP of People at Nitra (×2), Senior Director People BP at GitLab, Senior People BP at BNY, Vice President HR at PeopleOps, People Strategy Lead at Ladders ($287K)</li>
        <li><strong>Glassdoor Jobs</strong> (×2) — Azaaki Solutions & others hiring in NY; Amazon Web Services mentioned (duplicate pair)</li>
        <li><strong>Cornerstone (CSOD)</strong> — careers@csod.com — candidate profile/data transparency message</li>
      </ul>
      <div class="rec-action" style="color:#16a34a;">✅ Action: Review all 5 LinkedIn alerts this weekend. Filter Glassdoor duplicates. Read Cornerstone email in full and update profile.</div>
    </div>
  </div>

  <!-- RECRUITERS / NETWORKING -->
  <div class="email-cat">
    <div class="email-cat-header header-green">
      <h3>🟢 Recruiters / Networking</h3>
      <span class="count-badge" style="background:#dcfce7;color:#16a34a;">2 emails</span>
    </div>
    <div class="email-cat-body">
      <p><strong>Summary:</strong> LinkedIn profile search notification from Plank Enterprises and a profile view from Match (personal/social — Vincent, 57, West Orange NJ, not professional networking).</p>
      <ul class="sender-list">
        <li><strong>LinkedIn</strong> — "You appeared in 3 searches" — Someone from Plank Enterprises, Inc. found your profile</li>
        <li><strong>Match</strong> — Profile view from Vincent, 57, West Orange NJ (personal/social)</li>
      </ul>
      <div class="rec-action" style="color:#16a34a;">✅ Action: Check LinkedIn "Who Viewed Your Profile." Review Match notification at your leisure.</div>
    </div>
  </div>

  <!-- CALENDAR / EVENTS -->
  <div class="email-cat">
    <div class="email-cat-header header-blue">
      <h3>🔵 Calendar / Events</h3>
      <span class="count-badge" style="background:#dbeafe;color:#2563eb;">1 email</span>
    </div>
    <div class="email-cat-body">
      <p><strong>Summary:</strong> Facebook notification regarding a comment from Barbara Berkley Simonds — appears to reference a significant personal post from July 7 ("He took care of my health…"). Possibly related to loss or a difficult life event.</p>
      <ul class="sender-list">
        <li><strong>Barbara on Facebook</strong> &lt;close_friend_updates@facebookmail.com&gt; — "Barbara Berkley Simonds commented: 'So sorry. He took care of my health for...'" — refers to a July 7, 2026 post</li>
      </ul>
      <div class="rec-action" style="color:#2563eb;">📌 Action: Review the Facebook post this is responding to. May warrant a personal response.</div>
    </div>
  </div>

  <!-- MEDICAL / HEALTH -->
  <div class="email-cat">
    <div class="email-cat-header header-teal">
      <h3>🩺 Medical / Health</h3>
      <span class="count-badge" style="background:#cffafe;color:#0891b2;">2 emails</span>
    </div>
    <div class="email-cat-body">
      <p><strong>Summary:</strong> Two legitimate, urgent health communications requiring action today.</p>
      <ul class="sender-list">
        <li><strong>MyNorthwell</strong> — New test result available (posted this morning) — Review immediately in MyNorthwell portal</li>
        <li><strong>Quest Diagnostics</strong> — Test order from healthcare provider (July 9) — Make appointment now at questdiagnostics.com</li>
      </ul>
      <div class="rec-action" style="color:#0891b2;">⚡ Action: Both items require same-day attention. See Action Required section above.</div>
    </div>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="email-cat">
    <div class="email-cat-header header-yellow">
      <h3>🟡 Financial / Billing</h3>
      <span class="count-badge" style="background:#fef3c7;color:#d97706;">3 emails</span>
    </div>
    <div class="email-cat-body">
      <p><strong>Summary:</strong> Two active Bank of America billing disputes requiring immediate attention; one Experian Boost opportunity.</p>
      <ul class="sender-list">
        <li><strong>Bank of America</strong> — Dispute account -2994: Step 2 of 3, additional information requested — <span style="color:#dc2626;font-weight:700;">URGENT</span></li>
        <li><strong>Bank of America</strong> — Dispute account -4018: Step 2 of 3, being reviewed by merchant's bank — Monitor</li>
        <li><strong>Experian</strong> — Add insurance bill to Experian Boost® to potentially improve FICO® Score (Membership ID 10016853578021)</li>
      </ul>
      <div class="rec-action" style="color:#d97706;">⚡ Action: Log into BofA now for account -2994. Monitor -4018. Review Experian Boost offer when convenient.</div>
    </div>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="email-cat">
    <div class="email-cat-header header-purple">
      <h3>🟣 Professional Development</h3>
      <span class="count-badge" style="background:#ede9fe;color:#7c3aed;">2 emails</span>
    </div>
    <div class="email-cat-body">
      <p><strong>Summary:</strong> Alison free courses and a Medium digest on Claude AI skills for finance/dev (trashed by Melissa but potentially relevant given active AI interest).</p>
      <ul class="sender-list">
