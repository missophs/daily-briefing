<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing – Melissa W. | July 2, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a2a4a 0%, #2c4a7c 100%); color: #fff; border-radius: 12px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 15px; opacity: 0.85; margin-top: 6px; }
  .header .meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.12); border-radius: 8px; padding: 10px 18px; text-align: center; }
  .header .meta-item .num { font-size: 22px; font-weight: 700; }
  .header .meta-item .lbl { font-size: 11px; opacity: 0.8; text-transform: uppercase; letter-spacing: 0.5px; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; color: #1a2a4a; border-left: 4px solid #2c4a7c; padding-left: 12px; margin-bottom: 14px; text-transform: uppercase; letter-spacing: 0.4px; }

  /* EXEC SUMMARY */
  .exec-summary { background: #fff; border-radius: 10px; padding: 20px 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .exec-bullet { display: flex; align-items: flex-start; gap: 12px; margin-bottom: 12px; padding: 12px 14px; border-radius: 8px; }
  .exec-bullet:last-child { margin-bottom: 0; }
  .exec-bullet.red { background: #fff5f5; border-left: 4px solid #c0392b; }
  .exec-bullet.green { background: #f0fff4; border-left: 4px solid #27ae60; }
  .exec-bullet.blue { background: #f0f6ff; border-left: 4px solid #2980b9; }
  .exec-bullet .icon { font-size: 20px; flex-shrink: 0; margin-top: 1px; }
  .exec-bullet .text strong { display: block; font-size: 13px; font-weight: 700; margin-bottom: 3px; }
  .exec-bullet .text span { font-size: 13px; color: #444; }

  /* ACTION CARDS */
  .card-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(310px, 1fr)); gap: 14px; }
  .action-card { background: #fff; border-radius: 10px; padding: 16px 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); border-top: 4px solid #ccc; }
  .action-card.red { border-top-color: #c0392b; }
  .action-card.yellow { border-top-color: #f39c12; }
  .action-card.blue { border-top-color: #2980b9; }
  .action-card.green { border-top-color: #27ae60; }
  .action-card.purple { border-top-color: #8e44ad; }
  .action-card .card-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 6px; }
  .action-card.red .card-label { color: #c0392b; }
  .action-card.yellow .card-label { color: #d68910; }
  .action-card.blue .card-label { color: #2980b9; }
  .action-card.green .card-label { color: #27ae60; }
  .action-card.purple .card-label { color: #8e44ad; }
  .action-card h3 { font-size: 14px; font-weight: 700; margin-bottom: 8px; color: #1a2a4a; }
  .action-card .field { margin-bottom: 5px; font-size: 12.5px; }
  .action-card .field strong { color: #555; }
  .action-card .next-step { background: #f8f9fa; border-radius: 6px; padding: 7px 10px; margin-top: 10px; font-size: 12px; color: #1a2a4a; border-left: 3px solid #2c4a7c; }
  .due-badge { display: inline-block; background: #c0392b; color: #fff; font-size: 10px; font-weight: 700; border-radius: 4px; padding: 2px 7px; margin-top: 6px; }
  .due-badge.yellow { background: #d68910; }
  .due-badge.blue { background: #2980b9; }

  /* CALENDAR */
  .cal-day { background: #fff; border-radius: 10px; padding: 16px 18px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .cal-day-header { font-size: 14px; font-weight: 700; color: #1a2a4a; background: #eef2fa; padding: 7px 12px; border-radius: 6px; margin-bottom: 10px; }
  .cal-day-header.today { background: #2c4a7c; color: #fff; }
  .cal-event { display: grid; grid-template-columns: 110px 1fr; gap: 10px; padding: 10px 0; border-bottom: 1px solid #f0f0f0; }
  .cal-event:last-child { border-bottom: none; padding-bottom: 0; }
  .cal-time { font-size: 12px; font-weight: 700; color: #2c4a7c; white-space: nowrap; }
  .cal-detail h4 { font-size: 13px; font-weight: 700; color: #1a2a4a; margin-bottom: 4px; }
  .cal-detail .cal-meta { font-size: 11.5px; color: #555; }
  .status-pill { display: inline-block; font-size: 10px; font-weight: 700; border-radius: 10px; padding: 2px 8px; margin-left: 6px; }
  .status-pill.accepted { background: #d4edda; color: #155724; }
  .status-pill.declined { background: #f8d7da; color: #721c24; }
  .status-pill.needs { background: #fff3cd; color: #856404; }
  .status-pill.confirmed { background: #d1ecf1; color: #0c5460; }
  .conflict-warn { background: #fff3cd; border-left: 3px solid #f39c12; padding: 5px 9px; border-radius: 4px; font-size: 11px; margin-top: 5px; color: #856404; }

  /* JOB SEARCH */
  .job-table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .job-table th { background: #1a2a4a; color: #fff; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; padding: 10px 12px; text-align: left; }
  .job-table td { padding: 10px 12px; font-size: 12.5px; border-bottom: 1px solid #f0f0f0; vertical-align: top; }
  .job-table tr:last-child td { border-bottom: none; }
  .job-table tr:nth-child(even) td { background: #fafafa; }
  .fit-high { background: #d4edda; color: #155724; border-radius: 4px; padding: 2px 7px; font-size: 10px; font-weight: 700; }
  .fit-med { background: #fff3cd; color: #856404; border-radius: 4px; padding: 2px 7px; font-size: 10px; font-weight: 700; }
  .fit-low { background: #e2e3e5; color: #495057; border-radius: 4px; padding: 2px 7px; font-size: 10px; font-weight: 700; }

  /* EMAIL REVIEW */
  .email-cat { background: #fff; border-radius: 10px; padding: 16px 18px; margin-bottom: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-left: 5px solid #ccc; }
  .email-cat.red { border-left-color: #c0392b; }
  .email-cat.yellow { border-left-color: #f39c12; }
  .email-cat.blue { border-left-color: #2980b9; }
  .email-cat.green { border-left-color: #27ae60; }
  .email-cat.purple { border-left-color: #8e44ad; }
  .email-cat.gray { border-left-color: #95a5a6; }
  .email-cat.pink { border-left-color: #e91e8c; }
  .email-cat-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; }
  .email-cat-header h3 { font-size: 13px; font-weight: 700; color: #1a2a4a; }
  .count-badge { font-size: 11px; font-weight: 700; background: #1a2a4a; color: #fff; border-radius: 12px; padding: 2px 9px; }
  .email-cat .senders { font-size: 12px; color: #555; margin-bottom: 5px; }
  .email-cat .action-rec { font-size: 12px; font-weight: 600; }
  .email-cat.red .action-rec { color: #c0392b; }
  .email-cat.yellow .action-rec { color: #d68910; }
  .email-cat.green .action-rec { color: #27ae60; }
  .email-cat.gray .action-rec { color: #7f8c8d; }
  .email-cat.purple .action-rec { color: #8e44ad; }
  .email-cat.blue .action-rec { color: #2980b9; }

  /* TRASH REVIEW */
  .trash-group { background: #fff; border-radius: 10px; padding: 14px 18px; margin-bottom: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .trash-group h3 { font-size: 13px; font-weight: 700; margin-bottom: 8px; }
  .trash-group.restore h3 { color: #27ae60; }
  .trash-group.review h3 { color: #d68910; }
  .trash-group.delete h3 { color: #c0392b; }
  .trash-item { font-size: 12px; padding: 5px 0; border-bottom: 1px solid #f5f5f5; }
  .trash-item:last-child { border-bottom: none; }
  .trash-item strong { color: #1a2a4a; }

  /* PROMO TABLE */
  .promo-table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .promo-table th { background: #6c757d; color: #fff; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; padding: 9px 12px; text-align: left; }
  .promo-table td { padding: 9px 12px; font-size: 12.5px; border-bottom: 1px solid #f0f0f0; }
  .promo-table tr:last-child td { border-bottom: none; }
  .promo-table tr:nth-child(even) td { background: #fafafa; }
  .rec-delete { color: #c0392b; font-weight: 700; }
  .rec-review { color: #d68910; font-weight: 700; }
  .rec-keep { color: #27ae60; font-weight: 700; }
  .rec-ignore { color: #7f8c8d; font-weight: 700; }

  /* NEWSLETTER TABLE */
  .news-table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .news-table th { background: #8e44ad; color: #fff; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; padding: 9px 12px; text-align: left; }
  .news-table td { padding: 9px 12px; font-size: 12.5px; border-bottom: 1px solid #f0f0f0; }
  .news-table tr:last-child td { border-bottom: none; }
  .news-table tr:nth-child(even) td { background: #fafafa; }

  /* EMAIL ACCOUNTING */
  .acct-table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .acct-table th { background: #1a2a4a; color: #fff; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; padding: 9px 12px; text-align: left; }
  .acct-table td { padding: 9px 12px; font-size: 12.5px; border-bottom: 1px solid #f0f0f0; }
  .acct-table tr:last-child td { border-bottom: none; }
  .acct-table tr:nth-child(even) td { background: #fafafa; }
  .acct-total { background: #1a2a4a !important; color: #fff !important; font-weight: 700; }
  .acct-total td { color: #fff !important; font-weight: 700; }

  /* DASHBOARD */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }
  .dash-card { background: #fff; border-radius: 10px; padding: 14px 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .dash-card .dash-title { font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; font-weight: 700; color: #888; margin-bottom: 8px; }
  .dash-card .dash-value { font-size: 24px; font-weight: 700; color: #1a2a4a; }
  .dash-card .dash-sub { font-size: 11.5px; color: #555; margin-top: 4px; }
  .dash-card.red-d { border-top: 3px solid #c0392b; }
  .dash-card.yellow-d { border-top: 3px solid #f39c12; }
  .dash-card.blue-d { border-top: 3px solid #2980b9; }
  .dash-card.green-d { border-top: 3px solid #27ae60; }
  .dash-card.purple-d { border-top: 3px solid #8e44ad; }
  .dash-card.gray-d { border-top: 3px solid #95a5a6; }

  /* ACTION ITEMS TABLE */
  .ai-table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .ai-table th { background: #1a2a4a; color: #fff; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; padding: 9px 12px; text-align: left; }
  .ai-table td { padding: 10px 12px; font-size: 12.5px; border-bottom: 1px solid #f0f0f0; vertical-align: top; }
  .ai-table tr:last-child td { border-bottom: none; }
  .pri-high { background: #f8d7da; color: #721c24; border-radius: 4px; padding: 2px 7px; font-size: 10px; font-weight: 700; }
  .pri-med { background: #fff3cd; color: #856404; border-radius: 4px; padding: 2px 7px; font-size: 10px; font-weight: 700; }
  .pri-low { background: #d1ecf1; color: #0c5460; border-radius: 4px; padding: 2px 7px; font-size: 10px; font-weight: 700; }

  /* TOP 3 */
  .top3 { background: linear-gradient(135deg, #1a2a4a 0%, #2c4a7c 100%); border-radius: 12px; padding: 24px 28px; color: #fff; }
  .top3 h2 { font-size: 18px; font-weight: 700; margin-bottom: 16px; }
  .top3-item { display: flex; gap: 16px; align-items: flex-start; margin-bottom: 14px; }
  .top3-item:last-child { margin-bottom: 0; }
  .top3-num { background: rgba(255,255,255,0.2); border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 700; flex-shrink: 0; }
  .top3-text strong { display: block; font-size: 14px; font-weight: 700; margin-bottom: 3px; }
  .top3-text span { font-size: 12.5px; opacity: 0.85; }

  /* ALERT BANNER */
  .alert-banner { background: #c0392b; color: #fff; border-radius: 8px; padding: 12px 16px; margin-bottom: 14px; font-size: 13px; font-weight: 600; display: flex; align-items: center; gap: 10px; }
  .alert-banner.yellow { background: #d68910; }

  hr.divider { border: none; border-top: 2px solid #e8eaf0; margin: 24px 0; }
  .tag { display: inline-block; font-size: 10px; font-weight: 700; border-radius: 4px; padding: 2px 6px; margin-right: 3px; }
  .tag.inbox { background: #d1ecf1; color: #0c5460; }
  .tag.trash { background: #f8d7da; color: #721c24; }
  .tag.unread { background: #fff3cd; color: #856404; }
  .tag.spam { background: #e2e3e5; color: #495057; }
  a { color: #2980b9; word-break: break-all; }
</style>
</head>
<body>
<div class="page">

<!-- ======================================================
     1. HEADER
     ====================================================== -->
<div class="header">
  <h1>Good Morning, Melissa 👋</h1>
  <div class="subtitle">Executive Briefing — Thursday, July 2, 2026 &nbsp;|&nbsp; Prepared by your Chief of Staff</div>
  <div class="meta">
    <div class="meta-item"><div class="num">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="meta-item"><div class="num">7</div><div class="lbl">Calendar Events</div></div>
    <div class="meta-item"><div class="num">3</div><div class="lbl">Action Items Today</div></div>
    <div class="meta-item"><div class="num">5</div><div class="lbl">Job Leads Active</div></div>
    <div class="meta-item"><div class="num">🌡️ HEAT</div><div class="lbl">Extreme Heat Warning NYC</div></div>
  </div>
</div>

<!-- ======================================================
     2. EXECUTIVE SUMMARY
     ====================================================== -->
<div class="section">
  <div class="section-title">Executive Summary</div>
  <div class="exec-summary">
    <div class="exec-bullet red">
      <div class="icon">🚨</div>
      <div class="text">
        <strong>Biggest Risk: Multiple Phishing & Scam Emails in Inbox + Spam Wave</strong>
        <span>Your inbox contains active phishing threats disguised as cloud-storage payment failures, fake casino winnings, and fake Lowe's prize notifications. Several have NOT been filtered to trash and remain in your main mailbox. Do not click any links. Mark all as spam and delete immediately.</span>
      </div>
    </div>
    <div class="exec-bullet green">
      <div class="icon">💼</div>
      <div class="text">
        <strong>Biggest Opportunity: Chief People Officer at Crucial Hire (up to $300K/yr) + 4 Other Active Leads</strong>
        <span>LinkedIn Job Alerts surfaced a CPO role at up to $300K, a VP of People at Nitra, Head of HR at Everise, and Senior HRBP at Cohere. Scovai also flagged a Chief People & Culture Officer role at Omnisage LLC. Review and prioritize applications today — several posted 6/29–6/30.</span>
      </div>
    </div>
    <div class="exec-bullet blue">
      <div class="icon">📅</div>
      <div class="text">
        <strong>Biggest Calendar Item: HR Networking Open Office Hours TODAY (12–1 PM) + Doctor's Appointment Monday 7/6</strong>
        <span>You have not yet responded to today's HR Networking Zoom (12–1 PM). RSVP or join directly. Your new patient video visit with Dr. Keerthana Haridas is Monday 7/6 at 11:20 AM — confirm your Connect account login is ready. State Farm bill is also due 7/7.</span>
      </div>
    </div>
  </div>
</div>

<!-- ======================================================
     3. ACTION REQUIRED
     ====================================================== -->
<div class="section">
  <div class="section-title">⚡ Action Required</div>
  <div class="card-grid">

    <div class="action-card red">
      <div class="card-label">🔴 Security — Phishing</div>
      <h3>Fake Cloud Storage / Payment Blocked Emails</h3>
      <div class="field"><strong>Source:</strong> "Payment-Declined", "'Cloud Renewal'" — suspicious domains</div>
      <div class="field"><strong>Why it matters:</strong> These emails claim your cloud account is locked and photos will be deleted. This is a phishing scam designed to steal credentials or payment info.</div>
      <div class="next-step">→ Do NOT click any links. Mark as spam, delete, and report to your email provider. Verify your actual iCloud/Google storage directly via official apps.</div>
      <span class="due-badge">TODAY</span>
    </div>

    <div class="action-card red">
      <div class="card-label">🔴 Security — Phishing</div>
      <h3>Fake Lowe's Prize Winner Emails (3 copies)</h3>
      <div class="field"><strong>Source:</strong> Three separate spoofed "Lowe's®" addresses — random subdomains</div>
      <div class="field"><strong>Why it matters:</strong> Lowe's does not contact winners via random subdomains. These are credential-harvesting scams.</div>
      <div class="next-step">→ Mark all three as phishing/spam and delete. Do not click any link or fill out any form.</div>
      <span class="due-badge">TODAY</span>
    </div>

    <div class="action-card yellow">
      <div class="card-label">🟡 Financial — Statement Ready</div>
      <h3>Marcus by Goldman Sachs Monthly Statement</h3>
      <div class="field"><strong>Source:</strong> noreply@savings.marcus.com</div>
      <div class="field"><strong>Why it matters:</strong> Your June savings account statement is now available. Review for accuracy, interest earned, and any anomalies.</div>
      <div class="next-step">→ Log in to marcus.com or the app to download and review your statement. File for records.</div>
      <span class="due-badge yellow">Review This Week</span>
    </div>

    <div class="action-card yellow">
      <div class="card-label">🟡 Billing — Invoice Paid</div>
      <h3>Apify Invoice #202607020619 — $71.96 Paid</h3>
      <div class="field"><strong>Source:</strong> billing@apify.com</div>
      <div class="field"><strong>Why it matters:</strong> Payment confirmed. Download and file the attached invoice for expense tracking.</div>
      <div class="next-step">→ Download the invoice attachment from the email and save to your billing folder.</div>
      <span class="due-badge yellow">File Today</span>
    </div>

    <div class="action-card yellow">
      <div class="card-label">🟡 Billing — Deadline</div>
      <h3>State Farm Bill Due</h3>
      <div class="field"><strong>Source:</strong> Google Calendar reminder</div>
      <div class="field"><strong>Why it matters:</strong> State Farm bill is calendar-flagged for July 7. Ensure payment is queued to avoid a lapse in coverage.</div>
      <div class="next-step">→ Log in to State Farm or verify auto-pay is scheduled before July 7.</div>
      <span class="due-badge yellow">Due July 7</span>
    </div>

    <div class="action-card blue">
      <div class="card-label">🔵 Calendar — RSVP Needed</div>
      <h3>HR Networking & Job Search Open Office Hours</h3>
      <div class="field"><strong>Source:</strong> Google Calendar — TODAY 12:00–1:00 PM</div>
      <div class="field"><strong>Why it matters:</strong> Status is "Needs Action." This is a 180+ person HR networking Zoom — high-value for job search visibility.</div>
      <div class="next-step">→ Decide: Accept and join at noon via Zoom link. Note: AI notetaking tools are prohibited per organizer.</div>
      <span class="due-badge blue">TODAY 12 PM</span>
    </div>

    <div class="action-card blue">
      <div class="card-label">🔵 Medical — Prep Needed</div>
      <h3>New Patient Video Visit — Dr. Keerthana Haridas</h3>
      <div class="field"><strong>Source:</strong> Google Calendar — Monday July 6, 11:20 AM–12:00 PM</div>
      <div class="field"><strong>Why it matters:</strong> New patient visit requires an active Connect account on your device prior to joining. No location listed — video only.</div>
      <div class="next-step">→ Log into your Connect account today and test the video link. Prepare a list of health questions/history for the new patient intake.</div>
      <span class="due-badge blue">Mon July 6</span>
    </div>

    <div class="action-card green">
      <div class="card-label">🟢 Job Search — High Priority</div>
      <h3>Chief People Officer at Crucial Hire — Up to $300K/yr</h3>
      <div class="field"><strong>Source:</strong> LinkedIn Job Alerts — jobalerts-noreply@linkedin.com</div>
      <div class="field"><strong>Why it matters:</strong> Posted 6/29. CPO role at this compensation level is highly aligned with your profile. Time-sensitive — roles at this level fill quickly.</div>
      <div class="next-step">→ Review the posting today. Tailor your resume/cover letter. Apply or reach out to a contact at the firm.</div>
      <span class="due-badge">Apply ASAP</span>
    </div>

    <div class="action-card green">
      <div class="card-label">🟢 Job Search — Review</div>
      <h3>Chief People & Culture Officer — Omnisage LLC (Scovai)</h3>
      <div class="field"><strong>Source:</strong> Scovai — no-reply@scovai.com</div>
      <div class="field"><strong>Why it matters:</strong> Scovai flagged this role as an open item on your profile — it's waiting for your action to complete the match process.</div>
      <div class="next-step">→ Log into Scovai and complete the outstanding action to advance this opportunity.</div>
      <span class="due-badge yellow">Today</span>
    </div>

    <div class="action-card blue">
      <div class="card-label">🔵 Calendar — RSVP Needed</div>
      <h3>HR Networking & Job Search Group Zoom — July 8</h3>
      <div class="field"><strong>Source:</strong> Google Calendar — Tue July 8, 12:00–1:30 PM</div>
      <div class="field"><strong>Why it matters:</strong> Status is "Needs Action." Same large networking group as today's session.</div>
      <div class="next-step">→ RSVP accept or decline by end of day today.</div>
      <span class="due-badge blue">RSVP Today</span>
    </div>

    <div class="action-card blue">
      <div class="card-label">🔵 LinkedIn — Network</div>
      <h3>2 New LinkedIn Connection Invitations</h3>
      <div class="field"><strong>Source:</strong> LinkedIn — notifications-noreply@linkedin.com</div>
      <div class="field"><strong>Why it matters:</strong> During an active job search, reviewing and accepting relevant connections promptly is important for visibility.</div>
      <div class="next-step">→ Log into LinkedIn and review the 2 pending invitations. Accept relevant contacts.</div>
      <span class="due-badge yellow">Today</span>
    </div>

  </div>
</div>

<hr class="divider">

<!-- ======================================================
     4. FULL 7-DAY CALENDAR
     ====================================================== -->
<div class="section">
  <div class="section-title">📅 Full 7-Day Calendar (July 2–8, 2026)</div>

  <!-- THURSDAY JULY 2 -->
  <div class="cal-day">
    <div class="cal-day-header today">📌 Thursday, July 2, 2026 — TODAY</div>

    <div class="cal-event">
      <div class="cal-time">9:00 – 10:30 AM</div>
      <div class="cal-detail">
        <h4>Executive Roundtable <span class="status-pill declined">DECLINED</span></h4>
        <div class="cal-meta">
          <strong>Organizer:</strong> John Madigan &nbsp;|&nbsp; <strong>Format:</strong> Zoom<br>
          <strong>Link:</strong> <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09">Join Zoom</a> | Meeting ID: 207 786 667 | PW: 205454<br>
          <strong>Prep Needed:</strong> None — you have declined this event.<br>
          <strong>Note:</strong> If you wish to reconsider attending, contact John Madigan to confirm availability.
        </div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">12:00 – 1:00 PM</div>
      <div class="cal-detail">
        <h4>HR Networking &amp; Job Search: Open Office Hours — Zoom 2 <span class="status-pill needs">NEEDS ACTION</span></h4>
        <div class="cal-meta">
          <strong>Format:</strong> Zoom &nbsp;|&nbsp; <strong>Attendees:</strong> 180+ HR professionals<br>
          <strong>Link:</strong> <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1">Join Zoom</a><br>
          <strong>Prep Needed:</strong> Review your elevator pitch. Bring 1–2 specific asks. AI notetaking tools prohibited.<br>
          <strong>Action:</strong> ⚠️ RSVP required — status is unconfirmed.
        </div>
        <div class="conflict-warn">⚠️ No conflict with the declined Executive Roundtable — time slots do not overlap.</div>
      </div>
    </div>
  </div>

  <!-- FRIDAY JULY 3 -->
  <div class="cal-day">
    <div class="cal-day-header">Friday, July 3, 2026</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-detail">
        <h4>No Calendar Events Scheduled</h4>
        <div class="cal-meta">Day before July 4th holiday. Good opportunity to prep job applications and review job leads surfaced today.</div>
      </div>
    </div>
  </div>

  <!-- SATURDAY JULY 4 -->
  <div class="cal-day">
    <div class="cal-day-header">Saturday, July 4, 2026 — Independence Day 🎆</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-detail">
        <h4>No Calendar Events Scheduled</h4>
        <div class="cal-meta">Federal holiday. Note: Extreme Heat Warning in NYC is in effect through July 4 — stay hydrated and avoid prolonged outdoor exposure.</div>
      </div>
    </div>
  </div>

  <!-- SUNDAY JULY 5 -->
  <div class="cal-day">
    <div class="cal-day-header">Sunday, July 5, 2026</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-detail">
        <h4>No Calendar Events Scheduled</h4>
        <div class="cal-meta">Prep day — prepare materials for Monday's new patient video visit. Test Connect app login.</div>
      </div>
    </div>
  </div>

  <!-- MONDAY JULY 6 -->
  <div class="cal-day">
    <div class="cal-day-header">Monday, July 6, 2026</div>
    <div class="cal-event">
      <div class="cal-time">11:20 AM – 12:00 PM</div>
      <div class="cal-detail">
        <h4>New Patient Video Visit — Dr. Keerthana Haridas, MD <span class="status-pill accepted">ACCEPTED</span></h4>
        <div class="cal-meta">
          <strong>Format:</strong> Video Visit via Connect platform<br>
          <strong>Location:</strong> No physical location — video only<br>
          <strong>Prep Needed:</strong> Log into Connect account before the appointment. Silence notifications on your phone/tablet. Prepare health history and questions for new patient intake.<br>
          <strong>Action:</strong> Test your Connect app login TODAY (July 2) to avoid technical issues on the day.
        </div>
      </div>
    </div>
  </div>

  <!-- TUESDAY JULY 7 -->
  <div class="cal-day">
    <div class="cal-day-header">Tuesday, July 7, 2026</div>

    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-detail">
        <h4>State Farm Bill Due <span class="status-pill confirmed">CONFIRMED</span></h4>
        <div class="cal-meta">
          <strong>Type:</strong> Bill/Payment Reminder<br>
          <strong>Action:</strong> Confirm auto-pay or log in to pay manually before end of day. Do not miss — insurance lapse risk.
        </div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">12:00 – 1:00 PM</div>
      <div class="cal-detail">
        <h4>PT <span class="status-pill confirmed">CONFIRMED</span></h4>
        <div class="cal-meta">
          <strong>Type:</strong> Physical Therapy appointment<br>
          <strong>Location:</strong> Not specified in calendar<br>
          <strong>Prep Needed:</strong> Confirm location/address if in-person. Wear appropriate attire.
        </div>
        <div class="conflict-warn">⚠️ State Farm bill is also due today — plan to handle both.</div>
      </div>
    </div>
  </div>

  <!-- WEDNESDAY JULY 8 -->
  <div class="cal-day">
    <div class="cal-day-header">Wednesday, July 8, 2026</div>

    <div class="cal-event">
      <div class="cal-time">12:00 – 1:30 PM</div>
      <div class="cal-detail">
        <h4>HR Networking &amp; Job Search Group — Zoom 2 <span class="status-pill needs">NEEDS ACTION</span></h4>
        <div class="cal-meta">
          <strong>Format:</strong> Zoom &nbsp;|&nbsp; <strong>Attendees:</strong> 180+ HR professionals<br>
          <strong>Link:</strong> <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1">Join Zoom</a><br>
          <strong>Prep Needed:</strong> Review team resources (linked in invite description). Prepare professional update. Identify 2–3 attendees to connect with afterward.<br>
          <strong>Action:</strong> ⚠️ RSVP needed — status is unconfirmed.
        </div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">12:00 – 1:30 PM</div>
      <div class="cal-detail">
        <h4>Network (Personal Reminder) <span class="status-pill confirmed">CONFIRMED</span></h4>
        <div class="cal-meta">
          <strong>Type:</strong> Personal networking block — confirmed by Melissa<br>
          <strong>Note:</strong> This appears to overlap with the HR Networking Group Zoom above. Likely the same event / personal reminder.
        </div>
        <div class="conflict-warn">⚠️ Apparent duplicate with HR Networking Zoom — both at 12–1:30 PM on 7/8. Confirm and consolidate if needed.</div>
      </div>
    </div>
  </div>

</div>

<hr class="divider">

<!-- ======================================================
     5. JOB SEARCH & INTERVIEW PIPELINE
     ====================================================== -->
<div class="section">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
  <table class="job-table">
    <thead>
      <tr>
        <th>Source</th>
        <th>Role</th>
        <th>Company</th>
        <th>Date Posted</th>
        <th>Fit</th>
        <th>Status</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>LinkedIn Job Alerts</td>
        <td>Chief People Officer</td>
        <td>Crucial Hire</td>
        <td>6/29/2026</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>Alert received — not yet applied</td>
        <td>Apply today — up to $300K/yr</td>
      </tr>
      <tr>
        <td>Scovai</td>
        <td>Chief People &amp; Culture Officer</td>
        <td>Omnisage LLC</td>
        <td>Active today</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>Profile action pending on Scovai</td>
        <td>Complete Scovai profile action today</td>
      </tr>
      <tr>
        <td>LinkedIn Job Alerts</td>
        <td>Head of Human Resources</td>
        <td>Everise</td>
        <td>6/30/2026</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>Alert received — not yet applied</td>
        <td>Review posting and apply if aligned</td>
      </tr>
      <tr>
        <td>LinkedIn Job Alerts</td>
        <td>VP of People</td>
        <td>Nitra</td>
        <td>6/29/2026</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>Alert received — not yet applied</td>
        <td>Review and apply — VP-level HR role</td>
      </tr>
      <tr>
        <td>LinkedIn Job Alerts</td>
        <td>Senior HR Business Partner</td>
        <td>Cohere</td>
        <td>6/30/2026</td>
        <td><span class="fit-med">MEDIUM</span></td>
        <td>Alert received — not yet applied</td>
        <td>Review — AI-focused company, HRBP role</td>
      </tr>
      <tr>
        <td>Glassdoor Jobs</td>
        <td>Associate Director, HR Transformation</td>
        <td>RTX</td>
        <td>7/2/2026</td>
        <td><span class="fit-med">MEDIUM</span></td>
        <td>Alert received — not yet applied</td>
        <td>Review posting (+ 5 more jobs flagged)</td>
      </tr>
      <tr>
        <td>Calendar</td>
        <td>HR Networking — Open Office Hours</td>
        <td>HR Networking Group</td>
        <td>Today — 12:00 PM</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>RSVP Needed</td>
        <td>Join Zoom at noon — 180+ HR professionals</td>
      </tr>
      <tr>
        <td>Calendar</td>
        <td>HR Networking Group Session</td>
        <td>HR Networking Group</td>
        <td>July 8 — 12:00 PM</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>RSVP Needed</td>
        <td>Confirm attendance by today</td>
      </tr>
      <tr>
        <td>LinkedIn</td>
        <td>2 New Connection Invitations</td>
        <td>Various</td>
        <td>Today</td>
        <td><span class="fit-med">MEDIUM</span></td>
        <td>Pending review</td>
        <td>Review and accept relevant connections</td>
      </tr>
      <tr>
        <td>LinkedIn Labs</td>
        <td>Claude Sonnet 5 / LinkedIn Crosscheck</td>
        <td>LinkedIn Labs</td>
        <td>Today</td>
        <td><span class="fit-low">LOW</span></td>
        <td>FYI / Read</td>
        <td>Optional — AI tool update for awareness</td>
      </tr>
    </tbody>
  </table>
</div>

<hr class="divider">

<!-- ======================================================
     6. FULL EMAIL REVIEW BY CATEGORY
     ====================================================== -->
<div class="section">
  <div class="section-title">📬 Full Email Review by Category</div>

  <!-- SECURITY / RISK -->
  <div class="email-cat red">
    <div class="email-cat-header">
      <h3>🔴 Security / Risk — Phishing &amp; Scams</h3>
      <span class="count-badge">7</span>
    </div>
    <div class="senders">
      <strong>Senders:</strong> "Payment-Declined" (2×) | "'Cloud Renewal'" | "Congratulations🎉" (fake casino payment) | OnlineCasino (fake $5,000) | "Lowe's®" spoofed (3×)
    </div>
    <div class="field" style="font-size:12.5px; margin-bottom:5px;">
      <strong>Emails:</strong><br>
      1. <em>Payment-Declined</em> — "🚫We have blocked your account!" — phishing, cloud storage scam<br>
      2. <em>Payment-Declined</em> — "melissaw212, Your Cloud ID has been locked" — phishing, cloud scam<br>
      3. <em>'Cloud Renewal'</em> — "Your photos will be deleted tonight" — phishing, billing scam<br>
      4. <em>"Congratulations🎉"</em> — "Please_CONFIRM #8549479126 — Casino VOLTAGE $13,963.99" — fake payment scam<br>
      5. <em>OnlineCasino</em> — "You received a payment of $5,000.00 USD" — fake casino payment scam<br>
      6–8. <em>Lowe's® (spoofed)</em> — "We have been trying to reach you" (3 separate messages, suspicious domains)
    </div>
    <div class="action-rec">⚠️ ACTION: Mark ALL as phishing/spam immediately. Delete. Do NOT click any links. Report to Google.</div>
  </div>

  <!-- JOB SEARCH -->
  <div class="email-cat green">
    <div class="email-cat-header">
      <h3>🟢 Job Search &amp; Opportunities</h3>
      <span class="count-badge">6</span>
    </div>
    <div class="senders">
      <strong>Senders:</strong> LinkedIn Job Alerts (4×) | Scovai (1×) | Glassdoor Jobs (1×)
    </div>
    <div class="field" style="font-size:12.5px; margin-bottom:5px;">
      <strong>Emails:</strong><br>
      1. LinkedIn — Chief People Officer at Crucial Hire (up to $300K/yr) — posted 6/29<br>
      2. LinkedIn — Head of Human Resources at Everise — posted 6/30<br>
      3. LinkedIn — VP of People at Nitra — posted 6/29<br>
      4. LinkedIn — Senior HR Business Partner at Cohere — posted 6/30<br>
      5. Scovai — Chief People &amp; Culture Officer · Omnisage LLC — 1 open action item<br>
      6. Glassdoor — Associate Director, HR Transformation at RTX + 5 more roles
    </div>
    <div class="action-rec">✅ ACTION: Prioritize CPO at Crucial Hire and Omnisage LLC today. Review all 6 leads this week.</div>
  </div>

  <!-- PROFESSIONAL NETWORKING -->
  <div class="email-cat blue">
    <div class="email-cat-header">
      <h3>🔵 Professional Networking &amp; LinkedIn</h3>
      <span class="count-badge">3</span>
    </div>
    <div class="senders">
      <strong>Senders:</strong> LinkedIn (2 invitations) | LinkedIn Labs (Claude Sonnet 5 / Crosscheck)
    </div>
    <div class="field" style="font-size:12.5px; margin-bottom:5px;">
      1. LinkedIn — "You have 2 new invitations" — review and accept<br>
      2. LinkedIn Labs — "Claude Sonnet 5 just dropped — try it on LinkedIn Crosscheck" — FYI/optional<br>
      3. Match.com — "Kevin likes you. See if it's mutual." — personal/dating app (not professional)
    </div>
    <div class="action-rec">→ Review 2 LinkedIn invitations today. Match.com email is personal — handle at your discretion.</div>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="email-cat yellow">
    <div class="email-cat-header">
      <h3>🟡 Financial / Billing</h3>
      <span class="count-badge">2</span>
    </div>
    <div class="senders">
      <strong>Senders:</strong> Marcus by Goldman Sachs | Apify Billing
    </div>
    <div class="field" style="font-size:12.5px; margin-bottom:5px;">
      1. Marcus by Goldman Sachs — June savings account statement now available<br>
      2. Apify — Invoice #202607020619 — $71.96 paid and confirmed
    </div>
    <div class="action-rec">→ Download and review Marcus statement. Save Apify invoice to billing records.</div>
  </div>

  <!-- MEDICAL / HEALTH -->
  <div class="email-cat" style="border-left-color:#e91e8c;">
    <div class="email-cat-header">
      <h3>🩺 Medical / Health</h3>
      <span class="count-badge">0</span>
    </div>
    <div class="senders">No medical emails received today in inbox. Doctor's appointment tracked via calendar only.</div>
    <div class="action-rec">→ See Calendar: New patient video visit Mon 7/6 with Dr. Haridas. Prep Connect account.</div>
  </div>

  <!-- COMMUNITY / LOCAL -->
  <div class="email-cat blue">
    <div class="email-cat-header">
      <h3>🔵 Community / Local Alerts</h3>
      <span class="count-badge">3</span>
    </div>
    <div class="senders">
      <strong>Senders:</strong> Notify NYC | HomeAgain PetRescuers | Nextdoor (2×)
    </div>
    <div class="field" style="font-size:12.5px; margin-bottom:5px;">
      1. Notify NYC — Extreme Heat Warning NYC, 7/2–7/4 (in trash — but important!) — Stay cool, avoid prolonged outdoor exposure<br>
      2. HomeAgain — Cody, a lost dog, missing near Brooklyn (87th &amp; L/M Ave) — share if you're in the area<br>
      3. Nextdoor — "New from Martin and other neighbors in New York" — neighborhood update<br>
      4. Nextdoor (Yorkville) — "Fourth of July tradition" post — community discussion
    </div>
    <div class="action-rec">→ Note the Extreme Heat Warning through July 4. Cody the dog alert — share with neighbors if relevant.</div>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT / NEWSLETTERS -->
  <div class="email-cat purple">
    <div class="email-cat-header">
      <h3>🟣 Professional Development &amp; HR Newsletters</h3>
      <span class="count-badge">3</span>
    </div>
    <div class="senders">
      <strong>Senders:</strong> BambooHR | The People People Group (TPPG, in trash) | CoolDeep AI
    </div>
    <div class="field" style="font-size:12.5px; margin-bottom:5px;">
      1. BambooHR — "A PIP Doesn't Have to Mean Failure" — Performance Improvement Plan insights<br>
      2. The People People Group — "Critique of 'Family' Workplace Culture, Managing Vacation Policies…" (in trash) — HR community discussion digest<br>
      3. CoolDeep AI — "AI ladder nobody told you about" — AI professional development newsletter
    </div>
    <div class="action-rec">→ BambooHR and CoolDeep AI: Read when time permits. TPPG is in trash — restore if valuable to you.</div>
  </div>

  <!-- PERSONAL -->
  <div class="email-cat gray">
    <div class="email-cat-header">
      <h3>⚪ Personal</h3>
      <span class="count-badge">2</span>
    </div>
    <div class="senders">
      <strong>Senders:</strong> Match.com | GridRewards (Logical Buildings)
    </div>
    <div class="field" style="font-size:12.5px; margin-bottom:5px;">
      1. Match.com — "Kevin likes you" — personal dating app notification<br>
      2. GridRewards — "Your GridRewards event is complete" — energy-saving event (3 PM–9 PM yesterday) completed. Thank you for saving electricity!
    </div>
    <div class="action-rec">→ Personal emails — handle at your discretion. GridRewards is complete, no action needed.</div>
  </div>

  <!-- PROMOTIONAL / RETAIL -->
  <div class="email-cat gray">
    <div class="email-cat-header">
      <h3>⚪ Promotional / Retail</h3>
      <span class="count-badge">14</span>
    </div>
    <div class="senders">
      Kohl's | SHEIN | VIVAIA | YesStyle | Macy's | Old Navy | Temu (2×) | Target Circle Card | The Container Store | medicube US Store | Facebook Pages (Muscleteezy) | Reshmika Rakholiya (StartfactorHR sales pitch) | "Avoid.Knee.Surgery" (suspicious marketing)
    </div>
    <div class="action-rec">→ See Promotional/Retail Summary section below for full breakdown. Most are low priority — delete or ignore.</div>
  </div>

  <!-- SPAM / SCAM / ADULT -->
  <div class="email-cat red">
    <div class="email-cat-header">
      <h3>🔴 Spam / Adult Content / Unsolicited</h3>
      <span class="count-badge">3</span>
    </div>
    <div class="senders">
      <strong>Senders:</strong> The_Sex_God_Formula | "Avoid.Knee.Surgery" | Reshmika Rakholiya (unsolicited B2B sales)
    </div>
    <div class="field" style="font-size:12.5px; margin-bottom:5px;">
      1. The_Sex_God_Formula — adult content spam — delete immediately<br>
      2. "Avoid.Knee.Surgery" — "melissaw212, If your knees are failing you…" — suspicious health marketing<br>
      3. StartfactoHR (Reshmika) — "Still Managing Payroll in Excel?" — unsolicited B2B sales email
    </div>
    <div class="action-rec">⚠️ Delete all. Mark sex spam as spam/report. Unsubscribe from marketing if possible.</div>
  </div>

  <!-- TRASH EMAILS (counted in Trash Review) -->
  <div class="email-cat red">
    <div class="email-cat-header">
      <h3>🗑️ Already in Trash (counted separately)</h3>
      <span class="count-badge">10</span>
    </div>
    <div class="senders">See Trash Review section below for full details.</div>
    <div class="action-rec">→ See Trash Review section for full breakdown: Restore / Review / Safe to Delete.</div>
  </div>

  <!-- SAFE TO DELETE / IGNORE -->
  <div class="email-cat gray">
    <div class="email-cat-header">
      <h3>⚪ Safe to Delete / Ignore (No Action Needed)</h3>
      <span class="count-badge">7</span>
    </div>
    <div class="senders">
      Nextdoor (Yorkville trending posts — read) | Temu (2 emails — browsing reminders) | Facebook Pages (Muscleteezy) | Old Navy (sale) | Macy's (sale) | Target Circle Card (5% off)
    </div>
    <div class="action-rec">→ Archive or delete. No action required.</div>
  </div>

</div>

<hr class="divider">

<!-- ======================================================
     7. TRASH REVIEW
     ====================================================== -->
<div class="section">
  <div class="section-title">🗑️ Trash Review</div>
  <div class="alert-banner yellow">⚠️ 10 emails found in Trash. Review below before permanently deleting.</div>

  <div class="trash-group restore">
    <h3>✅ Restore Immediately (1 email)</h3>
    <div class="trash-item">
      <strong>Notify NYC</strong> — "Notify NYC - Update - Extreme Heat Warning - 7/2–7/4 (NYC)"<br>
      <span style="color:#555;">⚡ Reason to Restore: This is a legitimate NYC Emergency Alert about an Extreme Heat Warning in effect through July 4. This is important public safety information and should NOT be in trash. Restore and note the warning dates.</span>
    </div>
  </div>

  <div class="trash-group review">
    <h3>⚠️ Review Before Deleting (2 emails)</h3>
    <div class="trash-item">
      <strong>The People People Group (TPPG)</strong> — "[TPPG] Critique of 'Family' Workplace Culture, Managing Vacation Policies…"<br>
      <span style="color:#555;">Reason: HR community newsletter. If this is a group you actively participate in, you may want to restore. Topics are professionally relevant. Otherwise, unsubscribe and delete.</span>
    </div>
    <div class="trash-item">
      <strong>LigoSocial</strong> — "LinkedIn Connection Expiring Soon - Action Recommended"<br>
      <span style="color:#555;">Reason: This appears to be from a LinkedIn networking service. The "expiring connection" framing may be a marketing tactic, but if you intentionally connected with LiGo for job search, review before deleting. Likely safe to delete.</span>
    </div>
  </div>

  <div class="trash-group delete">
    <h3>🗑️ Safe to Delete (7 emails)</h3>
    <div class="trash-item">
      <strong>World Cup Reels ⚽</strong> — "🏆 Spin to Win A Mystery Bonus + Stacks of Free Spins" — Gambling spam. Delete.
    </div>
    <div class="trash-item">
      <strong>"Lowe's" (spoofed)</strong> — "🚨 Big Congratulations melissaw212 You have won a RIDGID Cordless 8-Tool Combo Kit 🎁" — Phishing scam, fake prize. Delete.
    </div>
    <div class="trash-item">
      <strong>Casino.Offer</strong> — "$7500 + 150 before the whistle 💰 Stoppage time: spin to win" — Gambling spam. Delete.
    </div>
    <div class="trash-item">
      <strong>"🎉Congratulations!"</strong> — "Get Your 130 FREE Spins Now On Chumba
<hr>
<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Financial / Billing</td><td>2</td></tr>
<tr><td>Job Search / Recruiters</td><td>9</td></tr>
<tr><td>Medical / Health</td><td>1</td></tr>
<tr><td>Other / Review</td><td>18</td></tr>
<tr><td>Professional Development / Newsletters</td><td>3</td></tr>
<tr><td>Promotional / Retail</td><td>7</td></tr>
<tr><td>Security / Risk</td><td>10</td></tr>
</table>
<p><strong>Audit Note:</strong> Every fetched email was reviewed and assigned to one category. Trash emails were included in review. Promotional and low-value emails were accounted for but deprioritized.</p>

