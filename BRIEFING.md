<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa White — September 10, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrapper { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: white; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; box-shadow: 0 4px 20px rgba(0,0,0,0.25); }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .sub { font-size: 15px; color: #a0b4cc; margin-top: 6px; }
  .header .meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 18px; }
  .header .meta-item .label { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #7fb3d3; }
  .header .meta-item .value { font-size: 20px; font-weight: 700; color: #ffffff; }

  /* SECTION */
  .section { background: white; border-radius: 12px; padding: 24px 28px; margin-bottom: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.07); }
  .section-title { font-size: 17px; font-weight: 700; color: #1a1a2e; border-bottom: 2px solid #e8ecf0; padding-bottom: 10px; margin-bottom: 18px; display: flex; align-items: center; gap: 8px; }
  .section-number { background: #1a1a2e; color: white; border-radius: 50%; width: 26px; height: 26px; display: inline-flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; flex-shrink: 0; }

  /* EXECUTIVE SUMMARY */
  .exec-bullet { display: flex; align-items: flex-start; gap: 12px; padding: 12px 16px; border-radius: 8px; margin-bottom: 10px; }
  .exec-bullet.red { background: #fff5f5; border-left: 4px solid #e53e3e; }
  .exec-bullet.green { background: #f0fff4; border-left: 4px solid #38a169; }
  .exec-bullet.blue { background: #ebf8ff; border-left: 4px solid #3182ce; }
  .exec-bullet .icon { font-size: 20px; flex-shrink: 0; margin-top: 2px; }
  .exec-bullet .text strong { display: block; font-size: 13px; font-weight: 700; margin-bottom: 2px; }
  .exec-bullet .text span { font-size: 13px; color: #444; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #f7f9fc; color: #444; font-weight: 700; padding: 9px 12px; text-align: left; border-bottom: 2px solid #e2e8f0; white-space: nowrap; }
  td { padding: 8px 12px; border-bottom: 1px solid #f0f2f5; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #fafbfc; }

  /* BADGES */
  .badge { display: inline-block; padding: 2px 9px; border-radius: 99px; font-size: 11px; font-weight: 700; white-space: nowrap; }
  .badge-red { background: #fff5f5; color: #c53030; border: 1px solid #feb2b2; }
  .badge-yellow { background: #fffff0; color: #b7791f; border: 1px solid #fbd38d; }
  .badge-blue { background: #ebf8ff; color: #2b6cb0; border: 1px solid #bee3f8; }
  .badge-green { background: #f0fff4; color: #276749; border: 1px solid #9ae6b4; }
  .badge-purple { background: #faf5ff; color: #6b46c1; border: 1px solid #d6bcfa; }
  .badge-gray { background: #f7f9fc; color: #666; border: 1px solid #e2e8f0; }
  .badge-orange { background: #fffaf0; color: #c05621; border: 1px solid #fbd38d; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 18px; margin-bottom: 14px; border-left: 5px solid; }
  .card-red { background: #fff5f5; border-color: #e53e3e; }
  .card-yellow { background: #fffff0; border-color: #d69e2e; }
  .card-blue { background: #ebf8ff; border-color: #3182ce; }
  .card-green { background: #f0fff4; border-color: #38a169; }
  .card-purple { background: #faf5ff; border-color: #805ad5; }
  .card-gray { background: #f7f9fc; border-color: #a0aec0; }
  .card-title { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
  .card-meta { font-size: 12px; color: #666; margin-bottom: 6px; }
  .card-body { font-size: 13px; color: #333; }
  .card-row { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 8px; align-items: center; }
  .card-label { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: #888; min-width: 80px; }
  .card-value { font-size: 13px; color: #333; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { background: #1a1a2e; color: white; border-radius: 8px 8px 0 0; padding: 8px 16px; font-weight: 700; font-size: 13px; letter-spacing: 0.5px; }
  .cal-event { display: grid; grid-template-columns: 130px 1fr; gap: 0; border: 1px solid #e2e8f0; border-top: none; }
  .cal-event:last-child { border-radius: 0 0 8px 8px; }
  .cal-time { background: #f7f9fc; padding: 10px 14px; font-size: 12px; font-weight: 700; color: #555; border-right: 1px solid #e2e8f0; display: flex; flex-direction: column; justify-content: center; }
  .cal-details { padding: 10px 14px; }
  .cal-name { font-weight: 700; font-size: 13px; margin-bottom: 4px; }
  .cal-info { font-size: 12px; color: #666; }
  .cal-info span { display: inline-block; margin-right: 12px; margin-top: 2px; }
  .conflict-warn { background: #fff5f5; border: 1px solid #feb2b2; border-radius: 6px; padding: 4px 10px; font-size: 11px; color: #c53030; font-weight: 700; margin-top: 4px; display: inline-block; }
  .prep-note { background: #ebf8ff; border-radius: 6px; padding: 4px 10px; font-size: 11px; color: #2b6cb0; margin-top: 4px; display: inline-block; }

  /* JOB PIPELINE */
  .job-card { border-radius: 10px; padding: 14px 16px; margin-bottom: 12px; border: 1px solid; }
  .job-card-high { background: #f0fff4; border-color: #68d391; }
  .job-card-medium { background: #fffff0; border-color: #f6e05e; }
  .job-card-low { background: #f7f9fc; border-color: #cbd5e0; }
  .job-title { font-weight: 700; font-size: 14px; }
  .job-meta { font-size: 12px; color: #666; margin: 3px 0 6px; }
  .job-tags { display: flex; gap: 6px; flex-wrap: wrap; }

  /* CATEGORY BLOCK */
  .cat-block { border-radius: 8px; padding: 14px 16px; margin-bottom: 12px; }
  .cat-block-red { background: #fff5f5; border-left: 4px solid #e53e3e; }
  .cat-block-yellow { background: #fffff0; border-left: 4px solid #d69e2e; }
  .cat-block-blue { background: #ebf8ff; border-left: 4px solid #3182ce; }
  .cat-block-green { background: #f0fff4; border-left: 4px solid #38a169; }
  .cat-block-purple { background: #faf5ff; border-left: 4px solid #805ad5; }
  .cat-block-gray { background: #f7f9fc; border-left: 4px solid #a0aec0; }
  .cat-title { font-weight: 700; font-size: 13px; margin-bottom: 6px; display: flex; align-items: center; gap: 8px; }
  .cat-count { background: #1a1a2e; color: white; border-radius: 99px; padding: 1px 8px; font-size: 11px; }
  .cat-body { font-size: 12px; color: #444; }
  .cat-row { margin-bottom: 3px; }

  /* TRASH */
  .trash-group { margin-bottom: 20px; }
  .trash-group-title { font-weight: 700; font-size: 14px; padding: 8px 14px; border-radius: 8px 8px 0 0; }
  .trash-restore { background: #276749; color: white; }
  .trash-review { background: #b7791f; color: white; }
  .trash-delete { background: #718096; color: white; }
  .trash-item { padding: 8px 14px; border: 1px solid #e2e8f0; border-top: none; font-size: 12px; }
  .trash-item:last-child { border-radius: 0 0 8px 8px; }
  .trash-from { font-weight: 600; color: #333; }
  .trash-subj { color: #555; }
  .trash-why { color: #888; font-style: italic; margin-top: 2px; }

  /* PROMO */
  .promo-table td:first-child { font-weight: 600; }

  /* DASHBOARD */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }
  .dash-card { border-radius: 10px; padding: 16px; border: 1px solid #e2e8f0; }
  .dash-card-title { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #888; margin-bottom: 8px; font-weight: 700; }
  .dash-card-value { font-size: 24px; font-weight: 800; margin-bottom: 6px; }
  .dash-card-body { font-size: 12px; color: #555; }
  .dash-red { background: #fff5f5; border-color: #feb2b2; }
  .dash-red .dash-card-value { color: #c53030; }
  .dash-yellow { background: #fffff0; border-color: #fbd38d; }
  .dash-yellow .dash-card-value { color: #b7791f; }
  .dash-blue { background: #ebf8ff; border-color: #bee3f8; }
  .dash-blue .dash-card-value { color: #2b6cb0; }
  .dash-green { background: #f0fff4; border-color: #9ae6b4; }
  .dash-green .dash-card-value { color: #276749; }
  .dash-purple { background: #faf5ff; border-color: #d6bcfa; }
  .dash-purple .dash-card-value { color: #6b46c1; }
  .dash-gray { background: #f7f9fc; border-color: #e2e8f0; }
  .dash-gray .dash-card-value { color: #555; }

  /* ACTION TABLE */
  .priority-high { color: #c53030; font-weight: 800; }
  .priority-med { color: #b7791f; font-weight: 700; }
  .priority-low { color: #718096; font-weight: 600; }

  /* TOP 3 */
  .top3 { display: flex; flex-direction: column; gap: 12px; }
  .top3-item { display: flex; align-items: flex-start; gap: 14px; background: linear-gradient(135deg, #1a1a2e, #0f3460); color: white; border-radius: 10px; padding: 18px 20px; }
  .top3-num { font-size: 32px; font-weight: 900; color: #4fc3f7; line-height: 1; flex-shrink: 0; }
  .top3-content strong { font-size: 15px; display: block; margin-bottom: 4px; }
  .top3-content span { font-size: 13px; color: #a0c4e8; }

  /* TRIAGE TABLE */
  .triage-status { font-weight: 700; white-space: nowrap; }
  .triage-from { font-size: 12px; max-width: 160px; }
  .triage-subject { font-size: 12px; max-width: 220px; }
  .triage-summary { font-size: 12px; color: #555; }
  .triage-summary-row td { background: #f7f9fc; font-style: italic; color: #666; }

  /* ACCOUNTING */
  .accounting-total { background: #1a1a2e; color: white; font-weight: 700; font-size: 14px; }

  /* RESPONSIVE */
  @media (max-width: 700px) {
    .header { padding: 20px; }
    .header .meta { gap: 12px; }
    .section { padding: 16px; }
    .cal-event { grid-template-columns: 1fr; }
    .cal-time { border-right: none; border-bottom: 1px solid #e2e8f0; }
  }

  .pill { display: inline-block; padding: 2px 8px; border-radius: 99px; font-size: 11px; font-weight: 600; }
  .pill-high { background: #c6f6d5; color: #276749; }
  .pill-med { background: #fefcbf; color: #744210; }
  .pill-low { background: #e2e8f0; color: #4a5568; }
  .pill-warn { background: #fed7d7; color: #9b2c2c; }
  .pill-info { background: #bee3f8; color: #2a4a6b; }

  .auto-trash-note { background: #fed7d7; border: 1px solid #fc8181; border-radius: 6px; padding: 4px 10px; font-size: 11px; color: #9b2c2c; font-weight: 700; display: inline-block; margin-left: 6px; }
  .newsletter-trash-note { background: #e9d8fd; border: 1px solid #b794f4; border-radius: 6px; padding: 4px 10px; font-size: 11px; color: #553c9a; font-weight: 700; display: inline-block; margin-left: 6px; }

  hr.section-hr { border: none; border-top: 1px solid #e2e8f0; margin: 14px 0; }
  .small-note { font-size: 11px; color: #888; font-style: italic; margin-top: 6px; }
</style>
</head>
<body>
<div class="page-wrapper">

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SECTION 0: EMAIL TRIAGE QUICK LIST -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section" style="border-top: 5px solid #1a1a2e;">
  <div class="section-title"><span class="section-number">0</span> Email Triage Quick List</div>
  <p style="font-size:12px;color:#666;margin-bottom:12px;">Compact scannable overview. Rescued emails first → Inbox emails → Trash summary rows.</p>
  <table>
    <thead>
      <tr>
        <th style="width:120px;">Status</th>
        <th style="width:180px;">From</th>
        <th style="width:230px;">Subject</th>
        <th>Summary</th>
      </tr>
    </thead>
    <tbody>
      <!-- INBOX EMAILS (individual rows) -->
      <tr>
        <td class="triage-status"><span class="badge badge-yellow">📥 INBOX</span></td>
        <td class="triage-from">Chase</td>
        <td class="triage-subject">Your Chase Slate Visa payment is due Sep 15</td>
        <td class="triage-summary">⚠️ Payment due in 5 days. Action required.</td>
      </tr>
      <tr>
        <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
        <td class="triage-from">Zoom</td>
        <td class="triage-subject">Congratulations! Your seat is reserved — Claude 101 Workshop INTL</td>
        <td class="triage-summary">Registration confirmed for 3-hour Claude 101 workshop. No recording provided.</td>
      </tr>
      <tr>
        <td class="triage-status"><span class="badge badge-green">📥 INBOX</span></td>
        <td class="triage-from">LinkedIn Job Alerts</td>
        <td class="triage-subject">Human Resources Business Partner at Worldhire and 15 more</td>
        <td class="triage-summary">VP–HR Business Partner roles. Review and apply.</td>
      </tr>
      <tr>
        <td class="triage-status"><span class="badge badge-green">📥 INBOX</span></td>
        <td class="triage-from">Indeed</td>
        <td class="triage-subject">VP of People @ Nitra — $325,000/yr</td>
        <td class="triage-summary">High-salary VP People role. Strong match flagged.</td>
      </tr>
      <tr>
        <td class="triage-status"><span class="badge badge-purple">📥 INBOX</span></td>
        <td class="triage-from">LinkedIn News</td>
        <td class="triage-subject">A viral debate over the dangers of AI</td>
        <td class="triage-summary">Anthropic researcher resignation going viral. Relevant to AI strategy awareness.</td>
      </tr>
      <tr>
        <td class="triage-status"><span class="badge badge-green">📥 INBOX</span></td>
        <td class="triage-from">LinkedIn Job Alerts</td>
        <td class="triage-subject">Lead HR Business Partner at Circle and 39 more</td>
        <td class="triage-summary">Circle (NYSE:CRCL) and 39 other roles. Review.</td>
      </tr>
      <tr>
        <td class="triage-status"><span class="badge badge-yellow">📥 INBOX</span></td>
        <td class="triage-from">Bank of America</td>
        <td class="triage-subject">My Credit: Review your monthly monitoring summary</td>
        <td class="triage-summary">Monthly credit monitoring report. Review for anomalies.</td>
      </tr>
      <tr>
        <td class="triage-status"><span class="badge badge-green">📥 INBOX</span></td>
        <td class="triage-from">LinkedIn Job Alerts</td>
        <td class="triage-subject">Executive – HR Business Partnership – USCAN Service Delivery at Ladders and 8 more</td>
        <td class="triage-summary">$192K–$288K/yr range. Strong pipeline.</td>
      </tr>
      <tr>
        <td class="triage-status"><span class="badge badge-green">📥 INBOX</span></td>
        <td class="triage-from">LinkedIn Job Alerts</td>
        <td class="triage-subject">Chief People Officer at Talent Harbor and 4 more</td>
        <td class="triage-summary">$190K–$230K CPO roles. High-fit alert.</td>
      </tr>
      <tr>
        <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
        <td class="triage-from">Claude's Notebook (Substack)</td>
        <td class="triage-subject">Unmerged Voices</td>
        <td class="triage-summary">AI philosophy essay. Low urgency; read when time permits.</td>
      </tr>
      <tr>
        <td class="triage-status"><span class="badge badge-gray">📥 INBOX</span></td>
        <td class="triage-from">Match</td>
        <td class="triage-subject">Robert likes you. See if it's mutual.</td>
        <td class="triage-summary">Personal / dating app notification.</td>
      </tr>
      <tr>
        <td class="triage-status"><span class="badge badge-gray">📥 INBOX</span></td>
        <td class="triage-from">Melissa W (self)</td>
        <td class="triage-subject">10-Prompts-You-Need-For-GPT-6-Astra.pdf — Google Drive</td>
        <td class="triage-summary">Self-sent Google Drive link. Verify legitimacy before opening.</td>
      </tr>
      <tr>
        <td class="triage-status"><span class="badge badge-gray">📥 INBOX</span></td>
        <td class="triage-from">Ms_G Mahjong</td>
        <td class="triage-subject">Re: Bootcamp</td>
        <td class="triage-summary">Reply re: Mahjong Bootcamp. Has flyer. Review details (capped at 8).</td>
      </tr>
      <!-- TRASH SUMMARY ROWS -->
      <tr class="triage-summary-row">
        <td colspan="4"><span class="badge badge-red">🗑 AUTO-TRASHED</span> &nbsp; <strong>4 emails auto-trashed</strong> (phishing / credential fraud / spam) — see Trash Review section for details.</td>
      </tr>
      <tr class="triage-summary-row">
        <td colspan="4"><span class="badge badge-purple">🗑 AUTO-TRASHED</span> &nbsp; <strong>3 emails auto-trashed</strong> (political fundraising newsletters) — see Trash Review section for details.</td>
      </tr>
      <tr class="triage-summary-row">
        <td colspan="4"><span class="badge badge-gray">🗂 TRASH (manual)</span> &nbsp; <strong>30 emails in Trash</strong> (promotions, newsletters, spam, retail) — see Trash Review section for full details.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SECTION 1: HEADER -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="header">
  <h1>☀️ Good Morning, Melissa</h1>
  <div class="sub">Executive Briefing — Thursday, September 10, 2026</div>
  <div class="meta">
    <div class="meta-item">
      <div class="label">Total Emails Reviewed</div>
      <div class="value">50</div>
    </div>
    <div class="meta-item">
      <div class="label">Calendar Events</div>
      <div class="value">10</div>
    </div>
    <div class="meta-item">
      <div class="label">Action Required</div>
      <div class="value">7</div>
    </div>
    <div class="meta-item">
      <div class="label">Interviews This Week</div>
      <div class="value">2</div>
    </div>
    <div class="meta-item">
      <div class="label">Security Alerts</div>
      <div class="value" style="color:#fc8181;">6</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SECTION 2: EXECUTIVE SUMMARY -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="section-number">2</span> Executive Summary</div>
  <div class="exec-bullet red">
    <div class="icon">🚨</div>
    <div class="text">
      <strong>BIGGEST RISK: 6 phishing / scam emails detected in inbox — plus Chase credit payment due Sep 15</strong>
      <span>Multiple phishing attempts were auto-trashed or remain in inbox untrashed (casino spam, fake CashApp, fake food stamp approval, male enhancement spam). Review the Security section immediately. Additionally, your Chase Slate Visa payment is due in 5 days — schedule payment today.</span>
    </div>
  </div>
  <div class="exec-bullet green">
    <div class="icon">💼</div>
    <div class="text">
      <strong>BIGGEST OPPORTUNITY: CUNY Vice Chancellor of HR Interview TOMORROW — plus $325K VP of People at Nitra</strong>
      <span>You have a confirmed in-person interview at CUNY Central Office tomorrow (Sep 11) at 3:00–4:00 PM (with a possible extension 4–5 PM). Prep is critical today. Separately, Indeed flagged a $325,000/yr VP of People role at Nitra that is a strong background match — apply immediately.</span>
    </div>
  </div>
  <div class="exec-bullet blue">
    <div class="icon">📅</div>
    <div class="text">
      <strong>BIGGEST CALENDAR ITEM: CUNY Interview tomorrow + M&amp;M meeting today at 1 PM + HR Networking at noon today (RSVP pending)</strong>
      <span>Today you have an HR Networking Open Office Hours at noon (no RSVP submitted yet) and an M&amp;M meeting with Monte Montoya at 1 PM. Tomorrow brings your CUNY interview. You also need to RSVP or decline the Sep 16 HR Networking Group session.</span>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SECTION 3: ACTION REQUIRED -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="section-number">3</span> Action Required</div>

  <div class="card card-red">
    <div class="card-title">🚨 Review &amp; Delete Security/Phishing Emails Still in Inbox</div>
    <div class="card-meta">Source: Multiple senders — 'Sex Trick', 'Congratulations!', SteelPower, Military_Honey, casino spam, etc.</div>
    <div class="card-body">Several phishing/spam emails are NOT in Trash and NOT auto-trashed. They need to be manually moved to trash and blocked. Do not click any links. See Security section for full list.</div>
    <div class="card-row"><span class="card-label">Next Step:</span><span class="card-value">Delete all identified phishing emails immediately. Mark as spam / block senders.</span></div>
    <div class="card-row"><span class="card-label">Due:</span><span class="badge badge-red">TODAY — ASAP</span></div>
  </div>

  <div class="card card-yellow">
    <div class="card-title">💳 Chase Slate Visa Payment Due September 15, 2026</div>
    <div class="card-meta">Source: Chase — no.reply.alerts@chase.com</div>
    <div class="card-body">Your credit card payment is due in 5 days. If payment is not already scheduled, log in to Chase and schedule it today to avoid late fees.</div>
    <div class="card-row"><span class="card-label">Next Step:</span><span class="card-value">Log into Chase and confirm or schedule payment.</span></div>
    <div class="card-row"><span class="card-label">Due:</span><span class="badge badge-yellow">Sep 15, 2026</span></div>
  </div>

  <div class="card card-green">
    <div class="card-title">🏛️ PREP: CUNY Vice Chancellor of Human Resources Interview — TOMORROW</div>
    <div class="card-meta">Source: Google Calendar — CUNY Central Office, Sep 11, 3:00–5:00 PM</div>
    <div class="card-body">You have confirmed interviews with Elisa Russo and Sujata Malhotra at CUNY Central Office (in-person). There are TWO back-to-back interview slots: 3–4 PM (confirmed) and 4–5 PM (accepted). This is a significant career opportunity — use today to prepare thoroughly: research CUNY's HR strategy, review your portfolio, and plan your commute. PT appointment in the morning gives you time to prep in the afternoon.</div>
    <div class="card-row"><span class="card-label">Next Step:</span><span class="card-value">Research CUNY HR initiatives, prepare behavioral examples, plan route to Central Office.</span></div>
    <div class="card-row"><span class="card-label">Due:</span><span class="badge badge-green">Sep 11, 2026 — 3:00 PM</span></div>
  </div>

  <div class="card card-green">
    <div class="card-title">💼 Apply: VP of People at Nitra — $325,000/yr (Strong Match)</div>
    <div class="card-meta">Source: Indeed — donotreply@match.indeed.com</div>
    <div class="card-body">Indeed flagged this role as a strong match for your VP of Human Resources background. At $325K/yr this is the highest-compensation opportunity in today's inbox.</div>
    <div class="card-row"><span class="card-label">Next Step:</span><span class="card-value">Review the full job description and apply today or tomorrow after CUNY interview.</span></div>
    <div class="card-row"><span class="card-label">Due:</span><span class="badge badge-green">ASAP — within 48 hours</span></div>
  </div>

  <div class="card card-blue">
    <div class="card-title">📋 RSVP: HR Networking &amp; Job Search Open Office Hours — TODAY Noon</div>
    <div class="card-meta">Source: Google Calendar — Zoom, Sep 10, 12:00–1:00 PM</div>
    <div class="card-body">Your RSVP status is "needsAction" — you have not responded. The session starts at noon today. Decide now whether to attend or decline. No AI notetaking tools permitted per organizer instructions.</div>
    <div class="card-row"><span class="card-label">Next Step:</span><span class="card-value">Accept or decline the calendar invite immediately. If attending, join Zoom 5 min early.</span></div>
    <div class="card-row"><span class="card-label">Due:</span><span class="badge badge-blue">TODAY — 12:00 PM</span></div>
  </div>

  <div class="card card-yellow">
    <div class="card-title">🏦 Review Bank of America Credit Monitoring Summary</div>
    <div class="card-meta">Source: Bank of America — noreply@mail-mycredit.bankofamerica.com</div>
    <div class="card-body">Monthly credit monitoring summary arrived. Given the volume of phishing activity targeting your email this week, it's worth reviewing this summary carefully for any unauthorized activity or new accounts.</div>
    <div class="card-row"><span class="card-label">Next Step:</span><span class="card-value">Log into Bank of America directly (do not click email links) and review the credit monitoring report.</span></div>
    <div class="card-row"><span class="card-label">Due:</span><span class="badge badge-yellow">Today</span></div>
  </div>

  <div class="card card-blue">
    <div class="card-title">🎓 Mahjong Bootcamp — Review Details from Ms_G</div>
    <div class="card-meta">Source: Ms_G Mahjong — msgmahjong@gmail.com</div>
    <div class="card-body">Ms_G replied to your Facebook inquiry about the Mahjong Bootcamp. She capped it at 8 people and attached a flyer. Review her Instagram reels and the flyer to decide if you want to register.</div>
    <div class="card-row"><span class="card-label">Next Step:</span><span class="card-value">Read the email, check the flyer, and confirm or decline participation.</span></div>
    <div class="card-row"><span class="card-label">Due:</span><span class="badge badge-gray">This week</span></div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SECTION 4: FULL 7-DAY CALENDAR -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="section-number">4</span> Full 7-Day Calendar</div>
  <p class="small-note" style="margin-bottom:14px;">All 10 calendar events shown. Sep 10–16, 2026.</p>

  <!-- THURSDAY SEP 10 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Thursday, September 10, 2026 — TODAY</div>

    <div class="cal-event">
      <div class="cal-time">9:00 AM – 10:30 AM</div>
      <div class="cal-details">
        <div class="cal-name">Executive Roundtable</div>
        <div class="cal-info">
          <span><span class="badge badge-red">DECLINED</span></span>
          <span>📍 Zoom (John Madigan)</span>
        </div>
        <div class="cal-info">You declined this meeting. No action needed. Meeting ID: 207 786 667.</div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">12:00 PM – 1:00 PM</div>
      <div class="cal-details">
        <div class="cal-name">HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
        <div class="cal-info">
          <span><span class="badge badge-yellow">⚠️ RSVP NEEDED</span></span>
          <span>📍 <a href="https://us06web.zoom.us/j/85945371140" style="color:#3182ce;">Zoom Link</a></span>
        </div>
        <div class="cal-info">Large group (175+ attendees). No AI notetaking tools permitted. Open discussion format.</div>
        <div class="prep-note">⚡ RSVP immediately — session starts in hours</div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">1:00 PM – 2:00 PM</div>
      <div class="cal-details">
        <div class="cal-name">M&amp;M (Meeting with Monte Montoya)</div>
        <div class="cal-info">
          <span><span class="badge badge-green">✅ ACCEPTED</span></span>
          <span>📍 Location TBD</span>
        </div>
        <div class="cal-info">One-on-one with monte.montoya@gmail.com. No description provided. Confirm agenda or location if needed.</div>
        <div class="prep-note">🔵 Confirm meeting details / agenda with Monte if not already done</div>
      </div>
    </div>
  </div>

  <!-- FRIDAY SEP 11 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Friday, September 11, 2026 — TOMORROW ⭐ KEY DAY</div>

    <div class="cal-event">
      <div class="cal-time">9:30 AM – 10:30 AM</div>
      <div class="cal-details">
        <div class="cal-name">PT (Physical Therapy / Personal Training)</div>
        <div class="cal-info">
          <span><span class="badge badge-green">✅ CONFIRMED</span></span>
          <span>📍 Location not listed</span>
        </div>
        <div class="cal-info">Appointment confirmed. Use morning time to also finalize CUNY interview prep after PT.</div>
        <div class="prep-note">🔵 After PT: finalize interview notes and plan commute to CUNY Central Office</div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">3:00 PM – 4:00 PM</div>
      <div class="cal-details">
        <div class="cal-name">🏛️ Vice Chancellor of Human Resources Interview — Appointment with Elisa Russo &amp; Sujata Malhotra</div>
        <div class="cal-info">
          <span><span class="badge badge-green">✅ CONFIRMED</span></span>
          <span>📍 CUNY Central Office</span>
        </div>
        <div class="cal-info">Visitor: Melissa Weiss. In-person interview. This is the primary interview block.</div>
        <div class="prep-note">🔵 PREP: Research CUNY HR structure, budget, and recent initiatives. Prepare 5 STAR behavioral examples. Plan commute with buffer time.</div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">4:00 PM – 5:00 PM</div>
      <div class="cal-details">
        <div class="cal-name">🏛️ Vice Chancellor of Human Resources Interview — Extended / Second Block</div>
        <div class="cal-info">
          <span><span class="badge badge-green">✅ ACCEPTED</span></span>
          <span>📍 CUNY Central Office</span>
        </div>
        <div class="cal-info">Second back-to-back interview block. May involve additional interviewers or panel. Bring extra resume copies.</div>
        <div class="conflict-warn">⚠️ Two consecutive CUNY interview slots — plan for 2-hour block total (3–5 PM)</div>
      </div>
    </div>
  </div>

  <!-- SAT SEP 12 / SUN SEP 13 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Saturday–Sunday, September 12–13, 2026</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="cal-name">No calendar events scheduled</div>
        <div class="cal-info">Consider using this weekend to follow up on CUNY interview, review job leads, and apply to Nitra VP of People role.</div>
      </div>
    </div>
  </div>

  <!-- MON SEP 14 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Monday, September 14, 2026</div>
    <div class="cal-event">
      <div class="cal-time">8:45 AM – 9:40 AM<br><small style="color:#888;">(Appt Time: 9:00 AM)</small></div>
      <div class="cal-details">
        <div class="cal-name">New Patient Visit with Andrea D. Card</div>
        <div class="cal-info">
          <span><span class="badge badge-green">✅ ACCEPTED</span></span>
          <span>📍 53 W 23rd St, 6th Floor, New York NY 10010</span>
        </div>
        <div class="cal-info">Phone: 212-746-2900. New patient appointment. Office may contact you about insurance. Arrive by 8:45 AM.</div>
        <div class="prep-note">🔵 Bring insurance card. Arrive 15 min early as new patient. Office at 6th floor — plan elevator time.</div>
      </div>
    </div>
  </div>

  <!-- TUE SEP 15 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Tuesday, September 15, 2026 ⚠️ Bill Due</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="cal-name">No calendar events — but Chase Slate Visa payment DUE TODAY</div>
        <div class="cal-info"><span class="badge badge-yellow">💳 PAYMENT DUE</span> Schedule Chase payment now to avoid late fees.</div>
      </div>
    </div>
  </div>

  <!-- WED SEP 16 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Wednesday, September 16, 2026</div>

    <div class="cal-event">
      <div class="cal-time">12:00 PM – 1:30 PM</div>
      <div class="cal-details">
        <div class="cal-name">HR Networking &amp; Job Search Group — Zoom 2</div>
        <div class="cal-info">
          <span><span class="badge badge-yellow">⚠️ RSVP NEEDED</span></span>
          <span>📍 <a href="https://us06web.zoom.us/j/81954171722" style="color:#3182ce;">Zoom Link</a></span>
        </div>
        <div class="cal-info">Large group networking session (175+ attendees). 90-minute session. Agenda includes professional networking and team resources. Check HR Networking Team Guidelines before attending.</div>
        <div class="prep-note">🔵 RSVP and review team guidelines ahead of session</div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">12:00 PM – 1:30 PM</div>
      <div class="cal-details">
        <div class="cal-name">Network (Personal)</div>
        <div class="cal-info">
          <span><span class="badge badge-green">✅ CONFIRMED</span></span>
          <span>📍 Location not listed</span>
        </div>
        <div class="cal-info">Confirmed networking block. Overlaps exactly with HR Networking Group Zoom.</div>
        <div class="conflict-warn">⚠️ CONFLICT: Both events run 12–1:30 PM on Sep 16. Confirm which takes priority.</div>
      </div>
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SECTION 5: JOB SEARCH & INTERVIEW PIPELINE -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="section-number">5</span> Job Search &amp; Interview Pipeline</div>

  <div class="job-card job-card-high">
    <div class="job-title">🏛️ Vice Chancellor of Human Resources — CUNY Central Office</div>
    <div class="job-meta">📅 Interview: Friday, Sep 11, 3:00–5:00 PM | 📍 In-Person | Interviewers: Elisa Russo, Sujata Malhotra</div>
    <div class="job-tags">
      <span class="pill pill-high">HIGH FIT</span>
      <span class="pill pill-warn">⭐ INTERVIEW TOMORROW</span>
      <span class="badge badge-blue">In-Person</span>
    </div>
    <div style="font-size:12px;color:#444;margin-top:8px;">Two back-to-back confirmed interview slots (3–4 PM confirmed, 4–5 PM accepted). CUNY Central Office location. This is the highest-priority interview in the pipeline. Prepare today.</div>
  </div>

  <div class="job-card job-card-high">
    <div class="job-title">💼 VP of People — Nitra ($325,000/yr)</div>
    <div class="job-meta">📧 Source: Indeed | 💰 $325,000/year | Status: Not yet applied</div>
    <div class="job-tags">
      <span class="pill pill-high">HIGH FIT</span>
      <span class="pill pill-warn">APPLY NOW</span>
      <span class="badge badge-green">Indeed Match</span>
    </div>
    <div style="font-size:12px;color:#444;margin-top:8px;">Indeed flagged your VP of Human Resources background as a strong match. Highest compensation opportunity in today's inbox. Apply within 48 hours.</div>
  </div>

  <div class="job-card job-card-high">
    <div class="job-title">💼 Chief People Officer — Talent Harbor and 4 more ($190K–$230K)</div>
    <div class="job-meta">📧 Source: LinkedIn Job Alerts | 💰 $190K–$230K/yr | Status: Not yet reviewed</div>
    <div class="job-tags">
      <span class="pill pill-high">HIGH FIT</span>
      <span class="badge badge-green">CPO Level</span>
    </div>
    <div style="font-size:12px;color:#444;margin-top:8px;">5 CPO-level roles. Review each for fit and apply to top 2–3 after CUNY interview.</div>
  </div>

  <div class="job-card job-card-high">
    <div class="job-title">💼 Executive – HR Business Partnership USCAN — Ladders and 8 more ($192K–$288K)</div>
    <div class="job-meta">📧 Source: LinkedIn Job Alerts | 💰 $192K–$288K/yr | Status: Not yet reviewed</div>
    <div class="job-tags">
      <span class="pill pill-high">HIGH FIT</span>
      <span class="badge badge-green">Executive Level</span>
    </div>
    <div style="font-size:12px;color:#444;margin-top:8px;">9 executive-level HR business partnership roles. Strong compensation range. Prioritize after Nitra application.</div>
  </div>

  <div class="job-card job-card-medium">
    <div class="job-title">💼 Lead HR Business Partner — Circle (NYSE: CRCL) and 39 more</div>
    <div class="job-meta">📧 Source: LinkedIn Job Alerts | Status: Not yet reviewed</div>
    <div class="job-tags">
      <span class="pill pill-med">MEDIUM FIT</span>
      <span class="badge badge-green">40 Roles</span>
    </div>
    <div style="font-size:12px;color:#444;margin-top:8px;">Large batch alert — 40 roles including Circle, a major fintech firm. Filter for VP/Director-level and apply selectively.</div>
  </div>

  <div class="job-card job-card-medium">
    <div class="job-title">💼 Human Resources Business Partner — Worldhire VP and 15 more</div>
    <div class="job-meta">📧 Source: LinkedIn Job Alerts | Status: Not yet reviewed</div>
    <div class="job-tags">
      <span class="pill pill-med">MEDIUM FIT</span>
      <span class="badge badge-green">16 Roles</span>
    </div>
    <div style="font-size:12px;color:#444;margin-top:8px;">VP-level HRBP roles at Worldhire and 15 others. Review for compensation and level fit.</div>
  </div>

  <div class="job-card job-card-medium">
    <div class="job-title">💼 People Business Partner — Transcarent and 6 more (Remote)</div>
    <div class="job-meta">📧 Source: Glassdoor Jobs | Status: Not yet reviewed</div>
    <div class="job-tags">
      <span class="pill pill-med">MEDIUM FIT</span>
      <span class="badge badge-blue">Remote</span>
    </div>
    <div style="font-size:12px;color:#444;margin-top:8px;">DoorDash also hiring. Remote roles included. Review Transcarent — health tech sector.</div>
  </div>

  <div class="job-card job-card-low">
    <div class="job-title">🤝 HR Networking Open Office Hours — Today 12 PM &amp; Sep 16</div>
    <div class="job-meta">📅 Today: 12–1 PM | Sep 16: 12–1:30 PM | Source: Calendar</div>
    <div class="job-tags">
      <span class="pill pill-low">NETWORKING</span>
      <span class="badge badge-yellow">RSVP NEEDED</span>
    </div>
    <div style="font-size:12px;color:#444;margin-top:8px;">Large HR professional networking group. Valuable for referrals and job leads. RSVP for both sessions.</div>
  </div>

  <div class="job-card job-card-low">
    <div class="job-title">📁 Self-Sent: 10 Prompts for GPT-6 Astra (Google Drive)</div>
    <div class="job-meta">📧 Source: melissaw212@gmail.com (self-sent) | Note: Verify link authenticity</div>
    <div class="job-tags">
      <span class="pill pill-low">AI SKILLS DEV</span>
      <span class="badge badge-yellow">Verify Before Opening</span>
    </div>
    <div style="font-size:12px;color:#444;margin-top:8px;">Self-sent Google Drive link to an AI prompts PDF. Relevant to Claude 101 Workshop prep. Verify it's your own file before opening.</div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SECTION 6: FULL EMAIL REVIEW BY CATEGORY -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="section-number">6</span> Full Email Review by Category</div>
  <p class="small-note" style="margin-bottom:14px;">All 50 emails are accounted for across these categories. Each email appears in exactly one category.</p>

  <!-- SECURITY / RISK -->
  <div class="cat-block cat-block-red">
    <div class="cat-title">🚨 Security / Risk <span class="cat-count">6</span></div>
    <div class="cat-body">
      <div class="cat-row"><strong>Auto-Trashed — Phishing:</strong></div>
      <div class="cat-row">• <strong>Fake Food Stamp Approval</strong> (noreply@project2-4a627.firebaseapp.com) — "Sign in to unlock your application for Food Stamp Assistance Approved!" — Credential harvesting via fake government benefit lure. <span class="auto-trash-note">AUTO-TRASHED</span></div>
      <div class="cat-row">• <strong>Fake CashApp Payment</strong> ("💲CashApp💲" from random domain) — Spoofed CashApp sender, broken template variables, fake $15.99 payment notification. Classic credential fraud. <span class="auto-trash-note">AUTO-TRASHED</span></div>
      <div class="cat-row" style="margin-top:8px;"><strong>In Inbox / NOT Trashed — Delete Immediately:</strong></div>
      <div class="cat-row">• <strong>'Sex Trick'</strong> (xkcqsupportisr@bkmohuslkjdgknrzoauxzrvs.com) — "Thousands of men are using this trick…" — Spam/scam from suspicious domain. Delete &amp; block.</div>
      <div class="cat-row">• <strong>Sex-Trick</strong> (uvwncbmxwvc@thlh.aadlielxlajux.us) — "Watch this Alone" — Same scam pattern. Delete &amp; block.</div>
      <div class="cat-row">• <strong>'Congratulations!'</strong> (fnwbsupportqpfb@ovjiiskxoeapnhilqibxtyfr.com) — "Score Big – $7500 Welcome Bonus + 30 Free Spins" — Casino spam with broken mail-merge. Delete.</div>
      <div class="cat-row">• <strong>'SteelPower'</strong> (random domain) — "Ready to Feel Like a Man Again?" — Male enhancement scam. Delete &amp; block.</div>
      <div class="cat-row" style="margin-top:6px;"><strong>Recommended Action:</strong> Delete all 4 non-auto-trashed items immediately. Mark as phishing. Block all domains.</div>
    </div>
  </div>

  <!-- JOB SEARCH -->
  <div class="cat-block cat-block-green">
    <div class="cat-title">💼 Job Search <span class="cat-count">7</span></div>
    <div class="cat-body">
      <div class="cat-row">• <strong>Indeed</strong> — VP of People @ Nitra, $325K/yr (strong match flagged)</div>
      <div class="cat-row">• <strong>LinkedIn Job Alerts</strong> — Human Resources Business Partner at Worldhire + 15 more (inbox)</div>
      <div class="cat-row">• <strong>LinkedIn Job Alerts</strong> — Lead HR Business Partner at Circle + 39 more (inbox)</div>
      <div class="cat-row">• <strong>LinkedIn Job Alerts</strong> — Executive HR Business Partnership USCAN at Ladders + 8 more, $192K–$288K (inbox)</div>
      <div class="cat-row">• <strong>LinkedIn Job Alerts</strong> — Chief People Officer at Talent Harbor + 4 more, $190K–$230K (inbox)</div>
      <div class="cat-row">• <strong>Glassdoor Jobs</strong> — People Business Partner at Transcarent + 6 more, Remote US (trashed)</div>
      <div class="cat-row">• <strong>Melissa W (self)</strong> — Self-sent Google Drive link to "10-Prompts-You-Need-For-GPT-6-Astra.pdf" (inbox — verify before opening)</div>
      <div class="cat-row" style="margin-top:6px;"><strong>Recommended Action:</strong> Apply to Nitra today. Review all LinkedIn alerts. Restore Glassdoor email from trash and review.</div>
    </div>
  </div>

  <!-- RECRUITERS / NETWORKING -->
  <div class="cat-block cat-block-green">
    <div class="cat-title">🤝 Recruiters / Networking <span class="cat-count">1</span></div>
    <div class="cat-body">
      <div class="cat-row">• <strong>The People People Group</strong> (community@thepeoplepeoplegroup.com) — TPPG Digest covering Parental Leave Policy Inquiry, Managing Employee Laptop Issues + 8 more HR topics. In Trash.</div>
      <div class="cat-row" style="margin-top:6px;"><strong>Recommended Action:</strong> Restore from trash — TPPG is a professional HR community relevant to your career. Review the digest topics.</div>
    </div>
  </div>

  <!-- CALENDAR / EVENTS -->
  <div class="cat-block cat-block-blue">
    <div class="cat-title">📅 Calendar / Events <span class="cat-count">3</span></div>
    <div class="cat-body">
      <div class="cat-row">• <strong>Zoom</strong> — "Congratulations! Your seat is reserved — Claude 101 Workshop INTL" (inbox) — 3-hour webinar. No recording provided.</div>
      <div class="cat-row">• <strong>Zoom</strong> — "1 Hour to Go for Day -1 of the Claude 101 Workshop!" — Reminder that was sent. Workshop already occurred or is imminent. Not in inbox, not trashed.</div>
      <div class="cat-row">• <strong>Melissa W (self)</strong> — "Bootcamp" inquiry sent to Ms_G Mahjong. Reference email in sent/archive.</div>
      <div class="cat-row" style="margin-top:6px;"><strong>Recommended Action:</strong> Note the Claude 101 Workshop date from the Zoom confirmation. The Day -1 reminder suggests a multi-day event — check Zoom confirmation for full schedule.</div>
    </div>
  </div>

  <!-- MEDICAL / HEALTH -->
  <div class="cat-block cat-block-blue">
    <div class="cat-title">🏥 Medical / Health <span class="cat-count">0 emails</span></div>
    <div class="cat-body">
      <div class="cat-row">No medical emails in inbox today. However, note the New Patient Visit with Andrea D. Card on Sep 14 at 53 W 23rd St. Contact 212-746-2900 if you need to reschedule or provide insurance info.</div>
    </div>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="cat-block cat-block-yellow">
    <div class="cat-title">💳 Financial / Billing <span class="cat-count">2</span></div>
    <div class="cat-body">
      <div class="cat-row">• <strong>Chase</strong> (no.reply.alerts@chase.com) — Chase Slate Visa payment due September 15, 2026. (Inbox — UNREAD)</div>
      <div class="cat-row">• <strong>Bank of America</strong> (noreply@mail-mycredit.bankofamerica.com) — Monthly My Credit monitoring summary. (Inbox — UNREAD)</div>
      <div class="cat-row" style="margin-top:6px;"><strong>Recommended Action:</strong> Schedule Chase payment today. Review BofA credit report directly via bankofamerica.com (not via email link).</div>
    </div>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="cat-block cat-block-purple">
    <div class="cat-title">📚 Professional Development <span class="cat-count">3</span></div>
    <div class="cat-body">
