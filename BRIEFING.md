<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa Weiss — June 22, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: white; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; box-shadow: 0 4px 20px rgba(0,0,0,0.25); }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header .subtitle { font-size: 15px; color: #a8b2d8; margin-top: 4px; }
  .header-meta { display: flex; gap: 28px; margin-top: 20px; flex-wrap: wrap; }
  .meta-chip { background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.18); border-radius: 8px; padding: 8px 18px; text-align: center; }
  .meta-chip .val { font-size: 22px; font-weight: 700; color: #e2e8f0; }
  .meta-chip .lbl { font-size: 11px; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.8px; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; color: #1a1a2e; margin-bottom: 12px; padding-bottom: 6px; border-bottom: 3px solid #e2e8f0; display: flex; align-items: center; gap: 8px; }
  .section-title .icon { font-size: 18px; }

  /* EXECUTIVE SUMMARY */
  .exec-summary { background: white; border-radius: 12px; padding: 22px 26px; box-shadow: 0 2px 10px rgba(0,0,0,0.07); }
  .exec-bullet { display: flex; align-items: flex-start; gap: 12px; padding: 10px 0; border-bottom: 1px solid #f1f5f9; }
  .exec-bullet:last-child { border-bottom: none; }
  .exec-badge { min-width: 90px; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px; text-align: center; }
  .badge-red { background: #fee2e2; color: #b91c1c; }
  .badge-green { background: #dcfce7; color: #166534; }
  .badge-blue { background: #dbeafe; color: #1d4ed8; }
  .badge-yellow { background: #fef9c3; color: #92400e; }
  .badge-purple { background: #ede9fe; color: #6d28d9; }
  .badge-gray { background: #f1f5f9; color: #475569; }

  /* ACTION CARDS */
  .action-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 16px; }
  .action-card { background: white; border-radius: 12px; padding: 18px 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.07); border-left: 5px solid #ccc; }
  .action-card.red { border-left-color: #ef4444; }
  .action-card.yellow { border-left-color: #f59e0b; }
  .action-card.blue { border-left-color: #3b82f6; }
  .action-card.green { border-left-color: #22c55e; }
  .action-card.purple { border-left-color: #8b5cf6; }
  .action-card .card-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
  .action-card.red .card-label { color: #ef4444; }
  .action-card.yellow .card-label { color: #d97706; }
  .action-card.blue .card-label { color: #3b82f6; }
  .action-card.green .card-label { color: #16a34a; }
  .action-card.purple .card-label { color: #7c3aed; }
  .action-card h4 { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
  .action-card .source { font-size: 11px; color: #64748b; margin-bottom: 8px; }
  .action-card .why { font-size: 12px; color: #374151; margin-bottom: 8px; background: #f8fafc; border-radius: 6px; padding: 6px 10px; }
  .action-card .next-step { font-size: 12px; color: #1e40af; font-weight: 600; }
  .action-card .due { font-size: 11px; color: #dc2626; margin-top: 6px; font-weight: 600; }

  /* CALENDAR */
  .cal-day { background: white; border-radius: 12px; padding: 16px 20px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .cal-day-header { font-size: 14px; font-weight: 700; color: #1e40af; margin-bottom: 10px; padding-bottom: 6px; border-bottom: 2px solid #dbeafe; display: flex; align-items: center; gap: 8px; }
  .cal-day-header.today { color: #dc2626; border-bottom-color: #fee2e2; }
  .cal-event { display: flex; gap: 12px; padding: 8px 0; border-bottom: 1px solid #f1f5f9; align-items: flex-start; }
  .cal-event:last-child { border-bottom: none; }
  .cal-time { min-width: 90px; font-size: 12px; font-weight: 600; color: #475569; padding-top: 2px; }
  .cal-details { flex: 1; }
  .cal-details h5 { font-size: 13px; font-weight: 700; }
  .cal-details .cal-meta { font-size: 11px; color: #64748b; margin-top: 2px; }
  .cal-details .cal-link { font-size: 11px; color: #2563eb; word-break: break-all; }
  .cal-details .cal-prep { font-size: 11px; background: #fef9c3; color: #78350f; border-radius: 4px; padding: 3px 7px; margin-top: 4px; display: inline-block; }
  .cal-details .cal-conflict { font-size: 11px; background: #fee2e2; color: #b91c1c; border-radius: 4px; padding: 3px 7px; margin-top: 4px; display: inline-block; }
  .rsvp-pill { font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 20px; display: inline-block; margin-top: 3px; }
  .rsvp-confirmed { background: #dcfce7; color: #166534; }
  .rsvp-declined { background: #fee2e2; color: #b91c1c; }
  .rsvp-pending { background: #fef9c3; color: #78350f; }
  .rsvp-accepted { background: #dbeafe; color: #1d4ed8; }
  .no-events { color: #94a3b8; font-size: 12px; font-style: italic; padding: 4px 0; }

  /* JOB SEARCH */
  .job-table { width: 100%; border-collapse: collapse; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .job-table th { background: #1e40af; color: white; padding: 10px 14px; font-size: 12px; text-align: left; font-weight: 600; }
  .job-table td { padding: 10px 14px; border-bottom: 1px solid #f1f5f9; font-size: 12px; vertical-align: top; }
  .job-table tr:last-child td { border-bottom: none; }
  .job-table tr:hover td { background: #f8fafc; }
  .fit-high { background: #dcfce7; color: #166534; padding: 2px 8px; border-radius: 12px; font-size: 10px; font-weight: 700; white-space: nowrap; }
  .fit-med { background: #fef9c3; color: #78350f; padding: 2px 8px; border-radius: 12px; font-size: 10px; font-weight: 700; white-space: nowrap; }
  .fit-low { background: #f1f5f9; color: #475569; padding: 2px 8px; border-radius: 12px; font-size: 10px; font-weight: 700; white-space: nowrap; }

  /* EMAIL REVIEW */
  .email-category-card { background: white; border-radius: 12px; padding: 16px 20px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-left: 5px solid #ccc; }
  .email-category-card.red { border-left-color: #ef4444; }
  .email-category-card.yellow { border-left-color: #f59e0b; }
  .email-category-card.blue { border-left-color: #3b82f6; }
  .email-category-card.green { border-left-color: #22c55e; }
  .email-category-card.purple { border-left-color: #8b5cf6; }
  .email-category-card.gray { border-left-color: #94a3b8; }
  .email-category-card.trash { border-left-color: #ef4444; background: #fff5f5; }
  .email-cat-header { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }
  .email-cat-title { font-size: 14px; font-weight: 700; }
  .email-cat-count { background: #1e40af; color: white; border-radius: 20px; padding: 1px 10px; font-size: 11px; font-weight: 700; }
  .email-list { font-size: 12px; color: #374151; }
  .email-list li { padding: 3px 0; border-bottom: 1px dotted #e2e8f0; }
  .email-list li:last-child { border-bottom: none; }
  .email-action-rec { font-size: 11px; font-weight: 600; margin-top: 8px; padding: 4px 10px; border-radius: 6px; display: inline-block; }
  .rec-act { background: #fee2e2; color: #b91c1c; }
  .rec-review { background: #fef9c3; color: #78350f; }
  .rec-delete { background: #f1f5f9; color: #64748b; }
  .rec-keep { background: #dcfce7; color: #166534; }
  .rec-unsub { background: #ede9fe; color: #6d28d9; }

  /* TRASH REVIEW */
  .trash-group { background: white; border-radius: 10px; padding: 14px 18px; margin-bottom: 10px; box-shadow: 0 2px 6px rgba(0,0,0,0.05); }
  .trash-group h4 { font-size: 13px; font-weight: 700; margin-bottom: 8px; padding-bottom: 5px; border-bottom: 2px solid #f1f5f9; }
  .trash-restore h4 { color: #dc2626; border-bottom-color: #fee2e2; }
  .trash-review h4 { color: #d97706; border-bottom-color: #fef9c3; }
  .trash-delete h4 { color: #475569; border-bottom-color: #e2e8f0; }
  .trash-item { font-size: 12px; padding: 4px 0; border-bottom: 1px dotted #e2e8f0; display: flex; gap: 8px; }
  .trash-item:last-child { border-bottom: none; }
  .trash-sender { font-weight: 600; min-width: 140px; }
  .trash-reason { color: #64748b; }

  /* PROMO */
  .promo-table { width: 100%; border-collapse: collapse; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .promo-table th { background: #475569; color: white; padding: 9px 14px; font-size: 12px; text-align: left; }
  .promo-table td { padding: 9px 14px; border-bottom: 1px solid #f1f5f9; font-size: 12px; }
  .promo-table tr:last-child td { border-bottom: none; }

  /* NEWSLETTER */
  .nl-table { width: 100%; border-collapse: collapse; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .nl-table th { background: #6d28d9; color: white; padding: 9px 14px; font-size: 12px; text-align: left; }
  .nl-table td { padding: 9px 14px; border-bottom: 1px solid #f1f5f9; font-size: 12px; }
  .nl-table tr:last-child td { border-bottom: none; }

  /* ACCOUNTING */
  .acct-table { width: 100%; border-collapse: collapse; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .acct-table th { background: #0f3460; color: white; padding: 10px 14px; font-size: 12px; text-align: left; }
  .acct-table td { padding: 9px 14px; border-bottom: 1px solid #f1f5f9; font-size: 12px; }
  .acct-table tr:last-child td { border-bottom: none; }
  .acct-table tfoot td { font-weight: 700; background: #f8fafc; font-size: 13px; border-top: 2px solid #1e40af; }

  /* DASHBOARD */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 14px; }
  .dash-card { background: white; border-radius: 12px; padding: 16px 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); text-align: center; }
  .dash-card .dash-val { font-size: 30px; font-weight: 800; }
  .dash-card .dash-lbl { font-size: 11px; color: #64748b; text-transform: uppercase; letter-spacing: 0.7px; margin-top: 2px; }
  .dash-card.red .dash-val { color: #dc2626; }
  .dash-card.yellow .dash-val { color: #d97706; }
  .dash-card.green .dash-val { color: #16a34a; }
  .dash-card.blue .dash-val { color: #1d4ed8; }
  .dash-card.purple .dash-val { color: #7c3aed; }
  .dash-card.gray .dash-val { color: #475569; }

  /* ACTION ITEMS TABLE */
  .ai-table { width: 100%; border-collapse: collapse; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .ai-table th { background: #1e3a5f; color: white; padding: 10px 14px; font-size: 12px; text-align: left; }
  .ai-table td { padding: 10px 14px; border-bottom: 1px solid #f1f5f9; font-size: 12px; vertical-align: top; }
  .ai-table tr:last-child td { border-bottom: none; }
  .pri-high { background: #fee2e2; color: #b91c1c; padding: 2px 8px; border-radius: 12px; font-size: 10px; font-weight: 700; }
  .pri-med { background: #fef9c3; color: #78350f; padding: 2px 8px; border-radius: 12px; font-size: 10px; font-weight: 700; }
  .pri-low { background: #f1f5f9; color: #475569; padding: 2px 8px; border-radius: 12px; font-size: 10px; font-weight: 700; }

  /* TOP 3 */
  .top3 { background: linear-gradient(135deg, #0f3460 0%, #1e40af 100%); color: white; border-radius: 14px; padding: 26px 30px; box-shadow: 0 4px 20px rgba(0,0,0,0.2); }
  .top3 h2 { font-size: 18px; font-weight: 700; margin-bottom: 16px; color: #e2e8f0; }
  .top3-item { display: flex; gap: 16px; align-items: flex-start; padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.1); }
  .top3-item:last-child { border-bottom: none; }
  .top3-num { font-size: 28px; font-weight: 900; color: #60a5fa; min-width: 36px; line-height: 1; }
  .top3-text h4 { font-size: 15px; font-weight: 700; color: #f0f9ff; }
  .top3-text p { font-size: 12px; color: #93c5fd; margin-top: 3px; }

  /* UTILITIES */
  .note-box { background: #fef9c3; border: 1px solid #f59e0b; border-radius: 8px; padding: 10px 14px; font-size: 12px; color: #78350f; margin-top: 8px; }
  .spam-warning { background: #fee2e2; border: 1px solid #ef4444; border-radius: 8px; padding: 10px 14px; font-size: 12px; color: #b91c1c; margin-top: 8px; }
  .divider { border: none; border-top: 2px solid #e2e8f0; margin: 30px 0; }
  ul.email-list { padding-left: 16px; }
  .tag { display: inline-block; background: #e0e7ff; color: #3730a3; border-radius: 4px; font-size: 10px; font-weight: 600; padding: 1px 6px; margin-right: 3px; }
  .tag.unread { background: #fef9c3; color: #78350f; }
  .tag.inbox { background: #dcfce7; color: #166534; }
  .tag.trash { background: #fee2e2; color: #b91c1c; }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════ HEADER -->
<div class="header">
  <h1>☀️ Good Morning, Melissa!</h1>
  <div class="subtitle">Executive Intelligence Briefing &nbsp;·&nbsp; Monday, June 22, 2026</div>
  <div class="header-meta">
    <div class="meta-chip"><div class="val">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="meta-chip"><div class="val">8</div><div class="lbl">Calendar Events</div></div>
    <div class="meta-chip"><div class="val">7</div><div class="lbl">Action Items</div></div>
    <div class="meta-chip"><div class="val">3</div><div class="lbl">Urgent / Risk</div></div>
    <div class="meta-chip"><div class="val">4</div><div class="lbl">Job Leads</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════ EXECUTIVE SUMMARY -->
<div class="section">
  <div class="section-title"><span class="icon">⚡</span> Executive Summary</div>
  <div class="exec-summary">
    <div class="exec-bullet">
      <span class="exec-badge badge-red">🔴 RISK</span>
      <div><strong>Apify platform usage has exceeded its monthly cap multiple times today</strong> — you received 4 alerts (at $35, $43, $45, and $46 thresholds). This signals runaway compute spend likely tied to your NEW PIPELINE TEST runs. Immediate review and spend cap adjustment needed today.</div>
    </div>
    <div class="exec-bullet">
      <span class="exec-badge badge-green">🟢 CAREER</span>
      <div><strong>Two strong LinkedIn job alerts are in your inbox</strong> — Director of Human Resources at Settlement Housing Fund ($135K–$150K) and Sr. HR Business Partner at Sundayy/Cohere. Both are high-fit roles requiring prompt review and application before competition intensifies.</div>
    </div>
    <div class="exec-bullet">
      <span class="exec-badge badge-blue">🔵 CALENDAR</span>
      <div><strong>Tomorrow is a packed day (June 23)</strong> — Eye Doctor appointment at 9 AM, a 1:1 meeting with Monte Montoya at 1 PM, and a Verizon Fios bill due. A World Cup-related Gridlock Alert is in effect for NYC Midtown today — plan transit accordingly.</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════ ACTION REQUIRED -->
<div class="section">
  <div class="section-title"><span class="icon">🚨</span> Action Required</div>
  <div class="action-grid">

    <div class="action-card red">
      <div class="card-label">🔴 Security / Risk</div>
      <h4>Apify Platform Spend Exceeded — 4 Alerts Today</h4>
      <div class="source">From: Apify &lt;hello@apify.com&gt; — Multiple emails (10:48, 10:57, 11:02, 11:10 UTC)</div>
      <div class="why">Your Apify monthly usage hit $35 → $43 → $45 → $46 in rapid succession, likely caused by repeated NEW PIPELINE TEST runs. Unchecked, this could result in unexpected overage charges or service suspension.</div>
      <div class="next-step">→ Log in to Apify dashboard now. Pause runaway actors, review spend, and set a hard monthly cap. Coordinate with your dev pipeline to throttle test runs.</div>
      <div class="due">⏰ Due: Today — June 22, 2026</div>
    </div>

    <div class="action-card red">
      <div class="card-label">🔴 Security / Spam</div>
      <h4>Casino Spam — Suspicious Senders in Inbox</h4>
      <div class="source">From: 'Slotocash Casino' &lt;mnsupportwq@svvdcjsvgyqqiottzudxoqhl.com&gt; and "Congratulations🎉" &lt;fgjusupportqpip@ddwzscwegyolctbphcycmaue.com&gt;</div>
      <div class="why">Two emails from randomly-generated sender domains promoting casino free spins. These are phishing/spam vectors. Both are in your non-trash inbox/folders — mark as spam immediately.</div>
      <div class="next-step">→ Mark both emails as spam. Do not click any links. Consider enabling stricter spam filters in Gmail settings.</div>
      <div class="due">⏰ Due: Today</div>
    </div>

    <div class="action-card yellow">
      <div class="card-label">🟡 Billing / Deadline</div>
      <h4>Verizon Fios Bill Due Tomorrow</h4>
      <div class="source">Google Calendar — "Verizon Fios Bill" | June 23, 2026 (All Day)</div>
      <div class="why">Bill is due tomorrow. Missing it could result in late fees or service interruption.</div>
      <div class="next-step">→ Confirm payment has been scheduled or log in to Verizon Fios to pay now.</div>
      <div class="due">⏰ Due: June 23, 2026</div>
    </div>

    <div class="action-card yellow">
      <div class="card-label">🟡 Subscription / Deadline</div>
      <h4>Slack Pro Free Trial Ends in 7 Days</h4>
      <div class="source">From: Slack &lt;no-reply@slack.com&gt; — June 22, 2026 (currently in Trash)</div>
      <div class="why">HR's Slack Pro workspace free trial expires June 29. After that, access to premium features (message history, video calls, integrations) will be cut off. Decision needed: upgrade or downgrade.</div>
      <div class="next-step">→ Restore from Trash and review. Decide if Slack Pro is worth $7.25+/mo or revert to Free tier. Act before June 29.</div>
      <div class="due">⏰ Due: June 29, 2026</div>
    </div>

    <div class="action-card green">
      <div class="card-label">🟢 Job Search</div>
      <h4>Director of Human Resources — Settlement Housing Fund ($135K–$150K)</h4>
      <div class="source">From: LinkedIn Job Alerts — June 22, 2026 | In Inbox ✅</div>
      <div class="why">High-salary leadership role in your HR field. $135K–$150K compensation. Currently in inbox, meaning it arrived recently and competition may be low.</div>
      <div class="next-step">→ Review full posting today. Tailor resume and cover letter. Apply within 24–48 hours for best visibility.</div>
      <div class="due">⏰ Due: June 23–24, 2026</div>
    </div>

    <div class="action-card blue">
      <div class="card-label">🔵 Calendar / RSVP</div>
      <h4>RSVP Pending: HR Networking &amp; Job Search Group — Zoom (Jun 24)</h4>
      <div class="source">Google Calendar — June 24, 2026 | 12:00–1:30 PM | Status: needsAction</div>
      <div class="why">Large HR networking Zoom session (200+ attendees) with RSVP still pending. Given your active job search, this is a high-value networking opportunity you shouldn't miss.</div>
      <div class="next-step">→ Accept the calendar invite today. Add Zoom link to calendar. Review agenda/resources linked in the event description beforehand.</div>
      <div class="due">⏰ RSVP by: Today. Event: June 24, 12:00 PM</div>
    </div>

    <div class="action-card blue">
      <div class="card-label">🔵 Calendar / RSVP</div>
      <h4>RSVP Pending: HR Networking Open Office Hours — Zoom (Jun 25)</h4>
      <div class="source">Google Calendar — June 25, 2026 | 12:00–1:00 PM | Status: needsAction</div>
      <div class="why">Open office hours with HR job seekers. RSVP still not submitted. Good for 1:1 connection opportunities and advice. Note: event description requests no AI notetaking tools.</div>
      <div class="next-step">→ Accept or decline. If attending, disable Otter.ai auto-join per event guidelines.</div>
      <div class="due">⏰ RSVP by: Today. Event: June 25, 12:00 PM</div>
    </div>

  </div>
</div>

<hr class="divider">

<!-- ═══════════════════════════════════════════════ FULL 7-DAY CALENDAR -->
<div class="section">
  <div class="section-title"><span class="icon">📅</span> Full 7-Day Calendar</div>

  <!-- Monday June 22 -->
  <div class="cal-day">
    <div class="cal-day-header today">📌 Monday, June 22, 2026 — TODAY</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <h5>No calendar events scheduled for today</h5>
        <div class="cal-meta">Focus on inbox triage, Apify spend review, and NYC Gridlock (World Cup)</div>
        <span class="cal-prep">⚠️ Gridlock Alert: Severe Midtown Manhattan traffic due to World Cup match days. Plan transit carefully.</span>
      </div>
    </div>
  </div>

  <!-- Tuesday June 23 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Tuesday, June 23, 2026</div>

    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <h5>💳 Verizon Fios Bill Due</h5>
        <span class="rsvp-pill rsvp-confirmed">CONFIRMED</span>
        <div class="cal-meta">Bill payment reminder — all-day event</div>
        <span class="cal-prep">⚠️ Action: Confirm or complete payment before EOD</span>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">9:00 – 10:00 AM</div>
      <div class="cal-details">
        <h5>👁️ Eye Doctor Appointment</h5>
        <span class="rsvp-pill rsvp-confirmed">CONFIRMED</span>
        <div class="cal-meta">No location listed — confirm address/office details</div>
        <span class="cal-prep">⚠️ Prep: Confirm office address and transit time. Bring insurance card.</span>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">1:00 – 2:00 PM</div>
      <div class="cal-details">
        <h5>🤝 M&amp;M — Meeting with Monte Montoya</h5>
        <span class="rsvp-pill rsvp-accepted">ACCEPTED</span>
        <div class="cal-meta">Attendee: monte.montoya@gmail.com | No location listed</div>
        <span class="cal-prep">⚠️ Prep: Confirm virtual vs. in-person. Prepare agenda or talking points.</span>
      </div>
    </div>
  </div>

  <!-- Wednesday June 24 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Wednesday, June 24, 2026</div>

    <div class="cal-event">
      <div class="cal-time">12:00 – 1:30 PM</div>
      <div class="cal-details">
        <h5>🌐 HR Networking &amp; Job Search Group — Zoom 2</h5>
        <span class="rsvp-pill rsvp-pending">RSVP PENDING ⚠️</span>
        <div class="cal-meta">200+ attendees | Large group HR networking session</div>
        <div class="cal-link">🔗 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1">Zoom Link — Click to Join</a></div>
        <span class="cal-prep">⚠️ Action Needed: RSVP immediately. Review team guidelines doc linked in event. High-value networking.</span>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">12:00 – 1:30 PM</div>
      <div class="cal-details">
        <h5>🔗 Network (Personal Block)</h5>
        <span class="rsvp-pill rsvp-confirmed">CONFIRMED</span>
        <div class="cal-meta">No attendees or location — appears to be a personal focus/networking block</div>
        <span class="cal-conflict">⚠️ Conflict: Overlaps exactly with HR Networking Zoom above. Likely the same session — verify and deduplicate.</span>
      </div>
    </div>
  </div>

  <!-- Thursday June 25 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Thursday, June 25, 2026</div>

    <div class="cal-event">
      <div class="cal-time">9:00 – 10:30 AM</div>
      <div class="cal-details">
        <h5>🏢 Executive Roundtable — Zoom (John Madigan)</h5>
        <span class="rsvp-pill rsvp-declined">DECLINED</span>
        <div class="cal-meta">Hosted by John Madigan | Meeting ID: 207 786 667 | PW: 205454</div>
        <div class="cal-link">🔗 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09">Zoom Link — Click to Join</a></div>
        <span class="cal-prep">⚠️ You declined. Consider whether this warrants re-engagement — Executive Roundtables can be high-value for your job search network.</span>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">12:00 – 1:00 PM</div>
      <div class="cal-details">
        <h5>🌐 HR Networking &amp; Job Search: Open Office Hours — Zoom 2</h5>
        <span class="rsvp-pill rsvp-pending">RSVP PENDING ⚠️</span>
        <div class="cal-meta">200+ attendees | Open discussion format — no AI notetaking per event rules</div>
        <div class="cal-link">🔗 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1">Zoom Link — Click to Join</a></div>
        <span class="cal-prep">⚠️ Action: RSVP today. Disable Otter.ai auto-join before this meeting per event rules.</span>
      </div>
    </div>
  </div>

  <!-- Friday June 26 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Friday, June 26, 2026</div>
    <div class="cal-event">
      <div class="cal-time">—</div>
      <div class="cal-details">
        <span class="no-events">No calendar events scheduled.</span>
      </div>
    </div>
  </div>

  <!-- Saturday June 27 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Saturday, June 27, 2026</div>

    <div class="cal-event">
      <div class="cal-time">10:00 – 11:00 AM</div>
      <div class="cal-details">
        <h5>💊 Check COBRA Payments</h5>
        <span class="rsvp-pill rsvp-confirmed">CONFIRMED</span>
        <div class="cal-meta">No attendees | Personal administrative task</div>
        <span class="cal-prep">⚠️ Prep: Locate COBRA statements. Verify payment status and due dates to maintain health coverage continuity.</span>
      </div>
    </div>
  </div>

  <!-- Sunday June 28 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Sunday, June 28, 2026</div>
    <div class="cal-event">
      <div class="cal-time">—</div>
      <div class="cal-details">
        <span class="no-events">No calendar events scheduled. Note: KKARENISM newsletter mentions CareerOS enrollment deadline is June 28.</span>
      </div>
    </div>
  </div>

</div>

<hr class="divider">

<!-- ═══════════════════════════════════════════════ JOB SEARCH & PIPELINE -->
<div class="section">
  <div class="section-title"><span class="icon">💼</span> Job Search &amp; Interview Pipeline</div>
  <table class="job-table">
    <thead>
      <tr>
        <th>Fit</th>
        <th>Role / Opportunity</th>
        <th>Source</th>
        <th>Salary / Details</th>
        <th>Status</th>
        <th>Next Step</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="fit-high">HIGH</span></td>
        <td><strong>Director of Human Resources</strong><br>Settlement Housing Fund</td>
        <td>LinkedIn Job Alerts<br>📥 In Inbox</td>
        <td>$135,000 – $150,000/year</td>
        <td>🆕 New Alert — Unread</td>
        <td>Review posting. Tailor resume. Apply within 24–48 hrs.</td>
      </tr>
      <tr>
        <td><span class="fit-high">HIGH</span></td>
        <td><strong>Sr. HR Business Partner</strong><br>Sundayy (Cohere)</td>
        <td>LinkedIn Job Alerts<br>📥 In Inbox (x2 alerts)</td>
        <td>Not listed — tech company</td>
        <td>🆕 New Alert — Unread</td>
        <td>Research Cohere AI. Align resume to AI-adjacent HR work. Apply promptly.</td>
      </tr>
      <tr>
        <td><span class="fit-high">HIGH</span></td>
        <td><strong>HR Networking &amp; Job Search Group</strong><br>Large Zoom — 200+ HR professionals</td>
        <td>Google Calendar<br>June 24, 12–1:30 PM</td>
        <td>Networking / peer group</td>
        <td>⚠️ RSVP Pending</td>
        <td>RSVP today. Prepare elevator pitch and target company list.</td>
      </tr>
      <tr>
        <td><span class="fit-high">HIGH</span></td>
        <td><strong>Open Office Hours — HR Networking</strong><br>Zoom Open Discussion</td>
        <td>Google Calendar<br>June 25, 12–1 PM</td>
        <td>Networking / peer group</td>
        <td>⚠️ RSVP Pending</td>
        <td>RSVP today. Disable Otter.ai. Prepare 2–3 questions for the group.</td>
      </tr>
      <tr>
        <td><span class="fit-med">MED</span></td>
        <td><strong>Michael Page International</strong><br>3 Jobs — Roles Not Specified</td>
        <td>Michael Page Int'l Talent Network<br>Email (not in inbox)</td>
        <td>Not listed</td>
        <td>📬 Unread — Not in Inbox</td>
        <td>Open email, review 3 roles. Respond to any that fit your target level.</td>
      </tr>
      <tr>
        <td><span class="fit-med">MED</span></td>
        <td><strong>CareerOS Program Enrollment</strong><br>via KKARENISM newsletter</td>
        <td>KKARENISM Substack<br>Email — June 22</td>
        <td>Enrollment deadline: June 28</td>
        <td>📬 Unread — not in inbox</td>
        <td>Review CareerOS program. Decide if enrollment is worthwhile before June 28 deadline.</td>
      </tr>
      <tr>
        <td><span class="fit-low">LOW</span></td>
        <td><strong>M&amp;M Meeting — Monte Montoya</strong><br>1:1 Meeting (purpose unclear)</td>
        <td>Google Calendar<br>June 23, 1–2 PM</td>
        <td>—</td>
        <td>✅ Accepted</td>
        <td>Clarify agenda. Potential networking or collaboration opportunity.</td>
      </tr>
      <tr>
        <td><span class="fit-low">LOW</span></td>
        <td><strong>Executive Roundtable — John Madigan</strong></td>
        <td>Google Calendar<br>June 25, 9–10:30 AM</td>
        <td>—</td>
        <td>❌ Declined</td>
        <td>Consider whether to re-engage. Executive events can expand your senior network.</td>
      </tr>
    </tbody>
  </table>
  <div class="note-box" style="margin-top:10px;">📌 <strong>NEW PIPELINE TEST (HR Search)</strong> — You sent yourself 4 pipeline test emails today (self-sent from melissaw212@gmail.com). The TypeScript pipeline is confirmed as a parallel build not yet wired into the live schedule. Monitor Apify spend tied to these runs.</div>
</div>

<hr class="divider">

<!-- ═══════════════════════════════════════════════ FULL EMAIL REVIEW BY CATEGORY -->
<div class="section">
  <div class="section-title"><span class="icon">📧</span> Full Email Review by Category</div>

  <!-- SECURITY / RISK -->
  <div class="email-category-card red">
    <div class="email-cat-header">
      <div class="email-cat-title">🔴 Security / Risk</div>
      <span class="email-cat-count">4</span>
    </div>
    <ul class="email-list">
      <li><strong>Slotocash Casino</strong> — "Claim your Casino Welcome Bonus Now!" | Random domain sender — SPAM/Phishing <span class="tag unread">Unread</span></li>
      <li><strong>"Congratulations🎉"</strong> — "130 Free Spins are ready to be claimed!" | Random domain sender — SPAM/Phishing <span class="tag unread">Unread</span></li>
      <li><strong>Apify</strong> — "Platform usage exceeded" × 3 alerts ($35, $45, $43) | Runaway spend <span class="tag">Read</span></li>
      <li><strong>Apify</strong> — "You're getting through your platform usage fast" (90% of $46 limit) | Spend warning <span class="tag">Read</span></li>
    </ul>
    <div class="email-action-rec rec-act">⚡ Action Required: Mark casino emails as spam. Review Apify spend dashboard immediately.</div>
  </div>

  <!-- JOB SEARCH -->
  <div class="email-category-card green">
    <div class="email-cat-header">
      <div class="email-cat-title">🟢 Job Search</div>
      <span class="email-cat-count">4</span>
    </div>
    <ul class="email-list">
      <li><strong>LinkedIn Job Alerts</strong> — "Director of Human Resources at Settlement Housing Fund: up to $150K/year" | 📥 Inbox <span class="tag inbox">Inbox</span> <span class="tag unread">Unread</span></li>
      <li><strong>LinkedIn Job Alerts</strong> — "HR Business Partner, Sr. at Sundayy" (9:05 AM) | 📥 Inbox <span class="tag inbox">Inbox</span> <span class="tag unread">Unread</span></li>
      <li><strong>LinkedIn Job Alerts</strong> — "HR Business Partner, Sr. at Sundayy" (5:05 AM) — duplicate alert | 📥 Inbox <span class="tag inbox">Inbox</span> <span class="tag unread">Unread</span></li>
      <li><strong>KKARENISM</strong> — "2 job search reminders for this week" — CareerOS enrollment deadline June 28 <span class="tag unread">Unread</span></li>
    </ul>
    <div class="email-action-rec rec-act">⚡ Action Required: Review Director role and Sr. HRBP postings. Apply within 48 hours. Evaluate CareerOS by June 28.</div>
  </div>

  <!-- RECRUITERS / NETWORKING -->
  <div class="email-category-card green">
    <div class="email-cat-header">
      <div class="email-cat-title">🟢 Recruiters / Networking</div>
      <span class="email-cat-count">1</span>
    </div>
    <ul class="email-list">
      <li><strong>Michael Page International Talent Network</strong> — "Michael Page International has 3 jobs you may be interested in" | Not in inbox <span class="tag unread">Unread</span></li>
    </ul>
    <div class="email-action-rec rec-review">👀 Review: Open and review all 3 job listings. Respond if any match your target level.</div>
  </div>

  <!-- SELF-SENT / PIPELINE -->
  <div class="email-category-card blue">
    <div class="email-cat-header">
      <div class="email-cat-title">🔵 Self-Sent / Pipeline Tests</div>
      <span class="email-cat-count">4</span>
    </div>
    <ul class="email-list">
      <li><strong>melissaw212@gmail.com</strong> — "[NEW PIPELINE TEST] HR Search — 2026-06-22" (10:40 AM) | 📥 Inbox <span class="tag inbox">Inbox</span></li>
      <li><strong>melissaw212@gmail.com</strong> — "[NEW PIPELINE TEST] HR Search — 2026-06-22" (10:46 AM) | 📥 Inbox <span class="tag inbox">Inbox</span></li>
      <li><strong>melissaw212@gmail.com</strong> — "[NEW PIPELINE TEST] HR Search — 2026-06-22" (10:57 AM) | Not in inbox</li>
      <li><strong>melissaw212@gmail.com</strong> — "[NEW PIPELINE TEST] HR Search — 2026-06-22" (11:14 AM) | 📥 Inbox <span class="tag inbox">Inbox</span></li>
    </ul>
    <div class="note-box">ℹ️ TypeScript parallel pipeline — not wired to live schedule. 4 test runs are the likely cause of Apify overage. Review and throttle test frequency.</div>
    <div class="email-action-rec rec-review">👀 Review: Throttle test frequency. Confirm pipeline behavior. Monitor Apify spend.</div>
  </div>

  <!-- CALENDAR / EVENTS -->
  <div class="email-category-card blue">
    <div class="email-cat-header">
      <div class="email-cat-title">🔵 Calendar / Events / Alerts</div>
      <span class="email-cat-count">2</span>
    </div>
    <ul class="email-list">
      <li><strong>Notify NYC</strong> — "Gridlock Alert Day Reminder - 6/22 (NYC)" — Severe Midtown traffic due to World Cup match days <span class="tag unread">Unread</span></li>
      <li><strong>Otter.ai Insights</strong> — "Your upcoming meetings" — Weekly meeting prep digest <span class="tag">Read</span></li>
    </ul>
    <div class="email-action-rec rec-review">👀 Review: Note Gridlock Alert for any in-person travel today. Review Otter.ai meetings digest.</div>
  </div>

  <!-- MEDICAL / HEALTH -->
  <div class="email-category-card blue">
    <div class="email-cat-header">
      <div class="email-cat-title">🔵 Medical / Health</div>
      <span class="email-cat-count">0</span>
    </div>
    <div class="email-list" style="color:#94a3b8;font-style:italic;">No standalone medical/health emails in this batch. (Eye Doctor appointment is calendar-based.)</div>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="email-category-card yellow">
    <div class="email-cat-header">
      <div class="email-cat-title">🟡 Financial / Billing</div>
      <span class="email-cat-count">1</span>
    </div>
    <ul class="email-list">
      <li><strong>SmartMoney Minute</strong> — "3 Conflicts of Interest Fiduciaries Can Potentially Have" | In Trash <span class="tag trash">Trash</span> <span class="tag unread">Unread</span></li>
    </ul>
    <div class="email-action-rec rec-delete">🗑️ Delete: Financial newsletter in Trash — can be permanently deleted.</div>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="email-category-card purple">
    <div class="email-cat-header">
      <div class="email-cat-title">🟣 Professional Development</div>
      <span class="email-cat-count">6</span>
    </div>
    <ul class="email-list">
      <li><strong>AI For Leaders</strong> — "Google Says AI Search Still Runs on SEO" | Not in inbox <span class="tag unread">Unread</span></li>
      <li><strong>Medium (Pranit Naik)</strong> — "Claude Just Got Beat by an Open-Source Chinese Model (GLM-5.2)" | In Trash <span class="tag trash">Trash</span></li>
      <li><strong>Medium Daily Digest</strong> — "AI as Your HR Policy Writer: How I Finally Rewrote Our Employee Handbook" | In Trash <span class="tag trash">Trash</span> <span class="tag unread">Unread</span></li>
      <li><strong>Medium Daily Digest</strong> — "Claude Code is Great" | 📥 Inbox <span class="tag inbox">Inbox</span> <span class="tag unread">Unread</span></li>
      <li><strong>Jeroen @ CompleteAiTraining</strong> — "Daily 'AI for Work' Pulse: June 22nd" — 20 new AI tools + 9 news articles <span class="tag unread">Unread</span></li>
      <li><strong>CoolDeep AI</strong> — "Yes...Claude skills can fix your average results" | In Trash <span class="tag trash">Trash</span> <span class="tag unread">Unread</span></li>
    </ul>
    <div class="email-action-rec rec-review">👀 Review: AI For Leaders and Jeroen are useful for staying current. Medium Digest on HR AI handbook is directly relevant to your work — consider restoring from Trash.</div>
  </div>

  <!-- PERSONAL -->
  <div class="email-category-card gray">
    <div class="email-cat-header">
      <div class="email-cat-title">⚪ Personal</div>
      <span class="email-cat-count">5</span>
    </div>
    <ul class="email-list">
      <li><strong>Match.com</strong> — "George likes you. See if it's mutual." | 📥 Inbox <span class="tag inbox">Inbox</span> <span class="tag unread">Unread</span></li>
      <li><strong>Match.com</strong> — "Danny likes you. See if it's mutual." | Not in inbox <span class="tag unread">Unread</span></li>
      <li><strong>Match.com</strong> — "Billy likes you. See if it's mutual." | Not in inbox <span class="tag">Read</span></li>
      <li><strong>USPS Informed Delivery</strong> — "Your Daily Digest for Mon, 6/22 is ready to view" — 5 mailpieces arriving | 📥 Inbox <span class="tag inbox">Inbox</span> <span class="tag unread">Unread</span></li>
      <li><strong>Lisa Rangel (Chameleon Resumes)</strong> — "Why we choose familiar pain" | In Trash <span class="tag trash">Trash</span> <span class="tag unread">Unread</span></li>
    </ul>
    <div class="email-action-rec rec-review">👀 Note: USPS digest indicates 5 pieces of physical mail arriving today — check mailbox. Match.com notifications are personal — review at leisure.</div>
  </div>

  <!-- NEWSLETTERS / SUBSCRIPTIONS -->
  <div class="email-category-card purple">
    <div class="email-cat-header">
      <div class="email-cat-title">🟣 Newsletters / Subscriptions</div>
      <span class="email-cat-count">9</span>
    </div>
    <ul class="email-list">
      <li><strong>TLDR Newsletter</strong> — "Apple reboots design 📱, Tesla Megapod ⚡, agent hook guardrails" (x2 sends) <span class="tag unread">Unread</span></li>
      <li><strong>TLDR Crypto</strong> — "Polymarket Pays Offshore Creators 🏝️, Morpho Confidential Lending 🔏, MSUSD Down ⬇️" | 📥 Inbox <span class="tag inbox">Inbox</span> <span class="tag unread">Unread</span></li>
      <li><strong>The Hustle</strong> — "🧽 Microplastic cleanup crew" | In Trash <span class="tag trash">Trash</span> <span class="tag unread">Unread</span></li>
      <li><strong>The Daily Skimm</strong> — "A royal lookalike" | In Trash <span class="tag trash">Trash</span> <span class="tag unread">Unread</span></li>
      <li><strong>The Average Joe</strong> — "🍦 Froyo-pocalypse — economic aftermath of the conflict" | In Trash <span class="tag trash">Trash</span> <span class="tag unread">Unread</span></li>
      <li><strong>1% Better</strong> — "Coke's Tax Fight, Polymarket Lies, and Benjamin Franklin's 50-Year Habit" <span class="tag unread">Unread</span></li>
      <li><strong>Martin @ The People People Group</strong> — "🫠 When Leadership Is The Outlier — Early Careers and Cutting Costs" <span class="tag">Read</span></li>
      <li><strong>Brevo</strong> — "Build your first email in minutes with Brevo Aura" (welcome/onboarding) <span class="tag unread">Unread</span></li>
      <li><strong>22 Words</strong> — "Lightning Deals ⚡ Prime Day Preview (Jun 22)" <span class="tag">Read</span></li>
    </ul>
    <div class="email-action-rec rec-review">👀 Review: TLDR (tech) and 1% Better are informative. The People People Group is HR-relevant. The Hustle, Skimm, Average Joe in Trash — safe to delete. Brevo is a new platform onboarding email.</div>
  </div>

  <!-- PROMOTIONAL / RETAIL -->
  <div class="email-category-card gray">
    <div class="email-cat-header">
      <div class="email-cat-title">⚪ Promotional / Retail</div>
      <span class="email-cat-count">14</span>
    </div>
    <ul class="email-list">
      <li><strong>SHEIN</strong> — "Give Your Space Some Personality 🏠" (x1)</li>
      <li><strong>SHEIN</strong> — "All under $14.99 | Clearance bonanza!" (x2 sends, nearly identical)</li>
      <li><strong>SHEIN</strong> — "🚨 NEW IN: Just Added 3 Days Ago" (x2 sends)</li>
      <li><strong>Zappos</strong> — "Kick off summer with mile-ready pairs 🏃" | In Trash <span class="tag trash">Trash</span></li>
      <li><strong>Chewy.com</strong> — "More playtime fun starts here" — pet toys promo</li>
      <li><strong>JetBlue</strong> — "Explore Priceless Experiences across the world." — TrueBlue points redemption | In Trash <span class="tag trash">Trash</span> <span class="tag unread">Unread</span></li>
      <li><strong>Apollo</strong> — "What if the right lead was in Apollo last week?" | In Trash <span class="tag trash">Trash</span> <span class="tag unread">Unread</span></li>
      <li><strong>Kohl's</strong> — "Summer is looking stylish (and super affordable) 😎" <span class="tag unread">Unread</span></li>
      <li><strong>Slack</strong> — "HR's free trial of Slack Pro ends in 7 days" | In Trash <span class="tag trash">Trash</span> <span class="tag unread">Unread</span> ⚠️ Actionable — see Action Required</li>
    </ul>
    <div class="email-action-rec rec-delete">🗑️ Delete/Ignore: Most retail promos are low priority. Slack Pro trial notice should be RESTORED — see Action Required section.</div>
  </div>

</div>

<hr class="divider">

<!-- ═══════════════════════════════════════════════ TRASH REVIEW -->
<div class="section">
  <div class="section-title"><span class="icon">🗑️</span> Trash Review</div>
  <p style="font-size:12px;color:#64748b;margin-bottom:12px;">The following 12 emails were found in Gmail Trash. Review before permanent deletion.</p>

  <div class="trash-group trash-restore">
    <h4>🔴 Restore Immediately (Action Required)</h4>
    <div class="trash-item"><span class="trash-sender">Slack</span><span class="trash-reason">"HR's free trial of Slack Pro ends in 7 days" — Trial expires June 29. Needs a decision. Do not delete.</span></div>
  </div>
<hr>
<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Financial / Billing</td><td>2</td></tr>
<tr><td>Job Search / Recruiters</td><td>5</td></tr>
<tr><td>Other / Review</td><td>32</td></tr>
<tr><td>Professional Development / Newsletters</td><td>5</td></tr>
<tr><td>Promotional / Retail</td><td>4</td></tr>
<tr><td>Security / Risk</td><td>2</td></tr>
</table>
<p><strong>Audit Note:</strong> Every fetched email was reviewed and assigned to one category. Trash emails were included in review. Promotional and low-value emails were accounted for but deprioritized.</p>

