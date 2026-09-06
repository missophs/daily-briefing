<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa | Sunday, September 6, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }

  .page-wrapper { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 16px; padding: 32px 36px; margin-bottom: 24px; box-shadow: 0 8px 32px rgba(0,0,0,0.18); }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 15px; color: #a8b4d0; margin-top: 6px; }
  .header .meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 18px; }
  .header .meta-item .label { font-size: 11px; color: #8899bb; text-transform: uppercase; letter-spacing: 1px; }
  .header .meta-item .value { font-size: 20px; font-weight: 700; color: #e8f0ff; margin-top: 2px; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; letter-spacing: 0.3px; margin-bottom: 14px; padding-bottom: 8px; border-bottom: 2px solid #e2e8f0; display: flex; align-items: center; gap: 8px; }
  .section-title .icon { font-size: 19px; }

  /* CARDS */
  .card { border-radius: 12px; padding: 16px 20px; margin-bottom: 12px; border-left: 5px solid #ccc; background: #fff; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .card.red { border-left-color: #e53e3e; background: #fff5f5; }
  .card.yellow { border-left-color: #d69e2e; background: #fffff0; }
  .card.blue { border-left-color: #3182ce; background: #ebf8ff; }
  .card.green { border-left-color: #38a169; background: #f0fff4; }
  .card.purple { border-left-color: #805ad5; background: #faf5ff; }
  .card.gray { border-left-color: #a0aec0; background: #f7fafc; }
  .card.orange { border-left-color: #dd6b20; background: #fffaf0; }

  .card-title { font-weight: 700; font-size: 14px; margin-bottom: 4px; }
  .card-meta { font-size: 12px; color: #718096; margin-bottom: 6px; }
  .card-body { font-size: 13px; color: #2d3748; }
  .card-row { display: flex; gap: 8px; margin-top: 5px; flex-wrap: wrap; }
  .tag { display: inline-block; border-radius: 5px; padding: 2px 8px; font-size: 11px; font-weight: 600; }
  .tag.red { background: #fed7d7; color: #c53030; }
  .tag.yellow { background: #fef3c7; color: #92400e; }
  .tag.green { background: #c6f6d5; color: #276749; }
  .tag.blue { background: #bee3f8; color: #2b6cb0; }
  .tag.purple { background: #e9d8fd; color: #6b46c1; }
  .tag.gray { background: #e2e8f0; color: #4a5568; }
  .tag.orange { background: #feebc8; color: #9c4221; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  th { background: #1a1a2e; color: #e8f0ff; font-size: 12px; text-transform: uppercase; letter-spacing: 0.8px; padding: 10px 14px; text-align: left; }
  td { padding: 9px 14px; font-size: 13px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #f7fafc; }
  tr:hover td { background: #edf2f7; }

  /* EXEC SUMMARY */
  .exec-summary { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; margin-bottom: 28px; }
  @media (max-width: 750px) { .exec-summary { grid-template-columns: 1fr; } .header .meta { gap: 12px; } }
  .exec-card { border-radius: 12px; padding: 18px 20px; color: #fff; box-shadow: 0 4px 14px rgba(0,0,0,0.12); }
  .exec-card.risk { background: linear-gradient(135deg, #e53e3e, #c53030); }
  .exec-card.opportunity { background: linear-gradient(135deg, #38a169, #276749); }
  .exec-card.calendar { background: linear-gradient(135deg, #3182ce, #2b6cb0); }
  .exec-card .ec-label { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; opacity: 0.85; margin-bottom: 6px; }
  .exec-card .ec-title { font-size: 15px; font-weight: 700; line-height: 1.35; }
  .exec-card .ec-sub { font-size: 12px; opacity: 0.85; margin-top: 6px; }

  /* CALENDAR */
  .cal-day { background: #fff; border-radius: 12px; margin-bottom: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); overflow: hidden; }
  .cal-day-header { background: #1a1a2e; color: #e8f0ff; padding: 10px 18px; font-weight: 700; font-size: 14px; display: flex; align-items: center; gap: 8px; }
  .cal-day-header.today { background: linear-gradient(90deg, #3182ce, #2b6cb0); }
  .cal-event { padding: 12px 18px; border-bottom: 1px solid #e2e8f0; display: grid; grid-template-columns: 110px 1fr; gap: 12px; align-items: start; }
  .cal-event:last-child { border-bottom: none; }
  .cal-time { font-weight: 700; font-size: 13px; color: #3182ce; }
  .cal-event-name { font-weight: 600; font-size: 14px; }
  .cal-detail { font-size: 12px; color: #718096; margin-top: 2px; }
  .cal-badge { display: inline-block; border-radius: 4px; padding: 1px 7px; font-size: 11px; font-weight: 700; margin-right: 5px; margin-top: 3px; }
  .cal-badge.confirmed { background: #c6f6d5; color: #276749; }
  .cal-badge.needs { background: #fef3c7; color: #92400e; }
  .cal-badge.declined { background: #fed7d7; color: #c53030; }
  .cal-badge.accepted { background: #c6f6d5; color: #276749; }
  .cal-badge.conflict { background: #fed7d7; color: #c53030; }
  .cal-badge.highlight { background: #bee3f8; color: #2b6cb0; }

  /* DASHBOARD GRID */
  .dashboard-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  @media (max-width: 650px) { .dashboard-grid { grid-template-columns: 1fr; } }
  .dash-card { background: #fff; border-radius: 12px; padding: 16px 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .dash-card h4 { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px; color: #4a5568; margin-bottom: 10px; border-bottom: 1px solid #e2e8f0; padding-bottom: 6px; }
  .dash-item { display: flex; align-items: flex-start; gap: 8px; margin-bottom: 7px; font-size: 13px; }
  .dash-dot { width: 8px; height: 8px; border-radius: 50%; margin-top: 4px; flex-shrink: 0; }
  .dash-dot.red { background: #e53e3e; }
  .dash-dot.green { background: #38a169; }
  .dash-dot.blue { background: #3182ce; }
  .dash-dot.yellow { background: #d69e2e; }
  .dash-dot.purple { background: #805ad5; }
  .dash-dot.gray { background: #a0aec0; }

  /* TRIAGE TABLE */
  .triage-status { font-size: 12px; font-weight: 700; white-space: nowrap; }
  .triage-from { font-size: 12px; color: #4a5568; }
  .triage-subject { font-size: 12px; font-weight: 600; }
  .triage-summary { font-size: 12px; color: #718096; }

  /* PRIORITY BOXES */
  .priority-boxes { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; }
  @media (max-width: 700px) { .priority-boxes { grid-template-columns: 1fr; } }
  .priority-box { border-radius: 12px; padding: 20px; color: #fff; text-align: center; box-shadow: 0 4px 14px rgba(0,0,0,0.12); }
  .priority-box.p1 { background: linear-gradient(135deg, #e53e3e, #c53030); }
  .priority-box.p2 { background: linear-gradient(135deg, #38a169, #276749); }
  .priority-box.p3 { background: linear-gradient(135deg, #805ad5, #6b46c1); }
  .priority-box .pnum { font-size: 36px; font-weight: 900; opacity: 0.3; line-height: 1; }
  .priority-box .ptitle { font-size: 15px; font-weight: 700; margin-top: 4px; }
  .priority-box .pdesc { font-size: 12px; opacity: 0.88; margin-top: 6px; line-height: 1.4; }

  .divider { height: 1px; background: #e2e8f0; margin: 20px 0; }
  .rescued-note { background: #e9d8fd; border: 1px solid #d6bcfa; border-radius: 6px; padding: 5px 10px; font-size: 11px; color: #553c9a; margin-top: 4px; display: inline-block; }
  .auto-trash-note { background: #fed7d7; border: 1px solid #fc8181; border-radius: 6px; padding: 5px 10px; font-size: 11px; color: #c53030; margin-top: 4px; display: inline-block; }

  .action-card { background: #fff; border-radius: 12px; padding: 18px 20px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); border-top: 4px solid #ccc; }
  .action-card.red { border-top-color: #e53e3e; }
  .action-card.yellow { border-top-color: #d69e2e; }
  .action-card.green { border-top-color: #38a169; }
  .action-card.blue { border-top-color: #3182ce; }
  .action-card.purple { border-top-color: #805ad5; }
  .action-card-label { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; }
  .action-card-label.red { color: #e53e3e; }
  .action-card-label.yellow { color: #d69e2e; }
  .action-card-label.green { color: #38a169; }
  .action-card-label.blue { color: #3182ce; }
  .action-card-label.purple { color: #805ad5; }
  .action-card-title { font-size: 16px; font-weight: 700; margin-bottom: 8px; }
  .action-row { display: grid; grid-template-columns: 130px 1fr; gap: 4px; margin-bottom: 4px; font-size: 13px; }
  .action-row-label { font-weight: 700; color: #4a5568; }

  .accounting-total { background: #1a1a2e; color: #e8f0ff; font-weight: 700; }
  .accounting-total td { color: #e8f0ff !important; background: #1a1a2e !important; }

  .trash-group { margin-bottom: 18px; }
  .trash-group-title { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px; padding: 8px 14px; border-radius: 6px; margin-bottom: 8px; }
  .trash-group-title.restore { background: #fed7d7; color: #c53030; }
  .trash-group-title.review { background: #fef3c7; color: #92400e; }
  .trash-group-title.delete { background: #e2e8f0; color: #4a5568; }

  .footnote { font-size: 11px; color: #718096; text-align: center; margin-top: 28px; padding: 12px; background: #fff; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.05); }
</style>
</head>
<body>
<div class="page-wrapper">

<!-- ═══════════════════════════════════════════════ -->
<!-- SECTION 0: EMAIL TRIAGE QUICK LIST             -->
<!-- ═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">⚡</span> Email Triage Quick List</div>
  <table>
    <thead>
      <tr>
        <th style="width:110px">Status</th>
        <th style="width:180px">From</th>
        <th style="width:260px">Subject</th>
        <th>Summary</th>
      </tr>
    </thead>
    <tbody>
      <!-- RESCUED -->
      <tr style="background:#faf5ff">
        <td class="triage-status" style="color:#805ad5">✅ RESCUED</td>
        <td class="triage-from">melissa (self)</td>
        <td class="triage-subject">VP HRBP Leader — 40% attrition cut, PE-backed</td>
        <td class="triage-summary">Outbound job application to Amy at Cprime. Rescued from Trash — important for job search tracking.</td>
      </tr>
      <!-- INBOX ITEMS -->
      <tr>
        <td class="triage-status" style="color:#3182ce">📥 INBOX</td>
        <td class="triage-from">Match</td>
        <td class="triage-subject">Steven likes you. See if it's mutual.</td>
        <td class="triage-summary">Match.com notification — someone expressed interest.</td>
      </tr>
      <tr>
        <td class="triage-status" style="color:#3182ce">📥 INBOX</td>
        <td class="triage-from">Sakshi Khatri via LinkedIn</td>
        <td class="triage-subject">Sakshi just messaged you</td>
        <td class="triage-summary">Unread LinkedIn DM awaiting response — likely professional outreach.</td>
      </tr>
      <tr>
        <td class="triage-status" style="color:#3182ce">📥 INBOX</td>
        <td class="triage-from">Pranit Naik (Medium)</td>
        <td class="triage-subject">Anthropic Just Dropped Fable 5.1 and Mythos 5.1 (Costs Cut by 45%)</td>
        <td class="triage-summary">AI industry update — Claude vs GPT-6, cost benchmarks. Professional development read.</td>
      </tr>
      <tr>
        <td class="triage-status" style="color:#3182ce">📥 INBOX</td>
        <td class="triage-from">LinkedIn Job Alerts</td>
        <td class="triage-subject">Senior Director, People Strategy &amp; Advisory at BNY and 16 more</td>
        <td class="triage-summary">17 new job alerts. BNY lead position relevant to Melissa's HR executive profile.</td>
      </tr>
      <tr>
        <td class="triage-status" style="color:#3182ce">📥 INBOX</td>
        <td class="triage-from">LinkedIn Job Alerts</td>
        <td class="triage-subject">Assistant VP Human Resources at Columbia University and 3 more</td>
        <td class="triage-summary">$220K–$265K/yr salary range. Columbia University HR leadership role.</td>
      </tr>
      <tr>
        <td class="triage-status" style="color:#3182ce">📥 INBOX</td>
        <td class="triage-from">Match</td>
        <td class="triage-subject">You've had a profile view from Mark</td>
        <td class="triage-summary">Mark, 53, Middletown NJ, viewed Melissa's Match profile.</td>
      </tr>
      <tr>
        <td class="triage-status" style="color:#3182ce">📥 INBOX</td>
        <td class="triage-from">Melissa W (self)</td>
        <td class="triage-subject">[No Subject — Substack link]</td>
        <td class="triage-summary">Self-sent Substack link shared from iOS. Personal reference/save.</td>
      </tr>
      <tr>
        <td class="triage-status" style="color:#3182ce">📥 INBOX</td>
        <td class="triage-from">Melissa W (self)</td>
        <td class="triage-subject">5_Claude_Code_Plugins_Setup_Guide.pdf — Google Drive</td>
        <td class="triage-summary">Self-sent Google Drive link to Claude Code Plugins setup guide.</td>
      </tr>
      <tr>
        <td class="triage-status" style="color:#3182ce">📥 INBOX</td>
        <td class="triage-from">Melissa W (self)</td>
        <td class="triage-subject">The 24 Claude Setup | Made For More</td>
        <td class="triage-summary">Self-sent AI setup guide link from madeformore.ai.</td>
      </tr>
      <tr>
        <td class="triage-status" style="color:#3182ce">📥 INBOX</td>
        <td class="triage-from">Robinhood</td>
        <td class="triage-subject">You started an IRA contribution</td>
        <td class="triage-summary">Roth IRA contribution initiated. Financial confirmation — retain.</td>
      </tr>
      <tr>
        <td class="triage-status" style="color:#3182ce">📥 INBOX</td>
        <td class="triage-from">Robinhood</td>
        <td class="triage-subject">Funds available for investing</td>
        <td class="triage-summary">$5.00 instant deposit available from recent transfer.</td>
      </tr>
      <tr>
        <td class="triage-status" style="color:#3182ce">📥 INBOX</td>
        <td class="triage-from">Robinhood</td>
        <td class="triage-subject">Your IRA contribution is complete</td>
        <td class="triage-summary">Roth IRA contribution confirmed complete.</td>
      </tr>
      <tr>
        <td class="triage-status" style="color:#3182ce">📥 INBOX</td>
        <td class="triage-from">Robinhood</td>
        <td class="triage-subject">Your transfer is complete</td>
        <td class="triage-summary">$0.45 transfer to Roth IRA (••8947) complete.</td>
      </tr>
      <tr>
        <td class="triage-status" style="color:#3182ce">📥 INBOX</td>
        <td class="triage-from">LinkedIn</td>
        <td class="triage-subject">You appeared in 2 searches</td>
        <td class="triage-summary">Someone from Egon Zehnder found Melissa's profile — executive search firm!</td>
      </tr>
      <tr>
        <td class="triage-status" style="color:#3182ce">📥 INBOX</td>
        <td class="triage-from">LinkedIn Job Alerts</td>
        <td class="triage-subject">Vice President, HR Business Partner Leader at Dayforce and 4 more</td>
        <td class="triage-summary">$198K–$310K salary range. VP HRBP roles including Dayforce.</td>
      </tr>
      <tr>
        <td class="triage-status" style="color:#3182ce">📥 INBOX</td>
        <td class="triage-from">OkCupid</td>
        <td class="triage-subject">You have an Intro!</td>
        <td class="triage-summary">New intro message on OkCupid.</td>
      </tr>
      <tr>
        <td class="triage-status" style="color:#3182ce">📥 INBOX</td>
        <td class="triage-from">OkCupid</td>
        <td class="triage-subject">Someone likes you</td>
        <td class="triage-summary">Someone liked Melissa's OkCupid profile.</td>
      </tr>
      <tr>
        <td class="triage-status" style="color:#3182ce">📥 INBOX</td>
        <td class="triage-from">Match</td>
        <td class="triage-subject">You've had a profile view from Chris</td>
        <td class="triage-summary">Chris, 51, Freehold NJ, viewed Melissa's Match profile.</td>
      </tr>
      <tr>
        <td class="triage-status" style="color:#3182ce">📥 INBOX</td>
        <td class="triage-from">Match</td>
        <td class="triage-subject">Billy likes you. See if it's mutual.</td>
        <td class="triage-summary">Match.com — Billy expressed interest.</td>
      </tr>
      <!-- SPAM IN INBOX (not trashed, not rescued) -->
      <tr style="background:#fff5f5">
        <td class="triage-status" style="color:#e53e3e">📥 INBOX ⚠️</td>
        <td class="triage-from">F*ckMeHard (spam)</td>
        <td class="triage-subject">[Explicit spam — not displayed]</td>
        <td class="triage-summary">Explicit spam email in inbox from spoofed address. Delete immediately.</td>
      </tr>
      <tr style="background:#fff5f5">
        <td class="triage-status" style="color:#e53e3e">📥 INBOX ⚠️</td>
        <td class="triage-from">F*ckMeHard (spam)</td>
        <td class="triage-subject">[Explicit spam — duplicate]</td>
        <td class="triage-summary">Second identical explicit spam. Delete immediately.</td>
      </tr>
      <tr style="background:#fff5f5">
        <td class="triage-status" style="color:#e53e3e">📥 INBOX ⚠️</td>
        <td class="triage-from">SteelPower (spam)</td>
        <td class="triage-subject">melissaw212 Discover SteelPower for Men</td>
        <td class="triage-summary">Spam/scam male wellness solicitation. Delete immediately.</td>
      </tr>
      <!-- SUMMARY ROWS -->
      <tr style="background:#faf5ff; font-style:italic;">
        <td class="triage-status" style="color:#c53030">🗑 AUTO-TRASHED</td>
        <td colspan="3" class="triage-summary"><strong>2 emails auto-trashed (phishing/spoofing)</strong> — see Trash Review for details</td>
      </tr>
      <tr style="background:#f7fafc; font-style:italic;">
        <td class="triage-status" style="color:#718096">🗂 TRASH (manual)</td>
        <td colspan="3" class="triage-summary"><strong>25 emails manually trashed</strong> (newsletters, retail spam, promotions) — see Trash Review for details</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════ -->
<!-- SECTION 1: HEADER                              -->
<!-- ═══════════════════════════════════════════════ -->
<div class="header">
  <h1>☀️ Good Morning, Melissa</h1>
  <div class="subtitle">Executive Briefing — Prepared by your Chief of Staff</div>
  <div class="meta">
    <div class="meta-item">
      <div class="label">Date</div>
      <div class="value">Sunday, Sep 6, 2026</div>
    </div>
    <div class="meta-item">
      <div class="label">Emails Reviewed</div>
      <div class="value">50</div>
    </div>
    <div class="meta-item">
      <div class="label">Calendar Events</div>
      <div class="value">11</div>
    </div>
    <div class="meta-item">
      <div class="label">Action Required</div>
      <div class="value" style="color:#fbbf24">7</div>
    </div>
    <div class="meta-item">
      <div class="label">Interviews This Week</div>
      <div class="value" style="color:#6ee7b7">2</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════ -->
<!-- SECTION 2: EXECUTIVE SUMMARY                   -->
<!-- ═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">📋</span> Executive Summary</div>
  <div class="exec-summary">
    <div class="exec-card risk">
      <div class="ec-label">🔴 Biggest Risk</div>
      <div class="ec-title">Phishing &amp; Spam Infiltration</div>
      <div class="ec-sub">2 spoofed/phishing emails auto-trashed; 3 explicit spam emails still sitting in your inbox. Immediate cleanup needed. One iCloud account-spoofing phishing email was flagged and auto-trashed before delivery.</div>
    </div>
    <div class="exec-card opportunity">
      <div class="ec-label">🟢 Biggest Opportunity</div>
      <div class="ec-title">CUNY Vice Chancellor Interview Thursday + Egon Zehnder Search Firm Interest</div>
      <div class="ec-sub">In-person interview at CUNY Central Office Thursday Sept 11 (3–5 PM). Also: Egon Zehnder (top executive search firm) searched your LinkedIn profile. 20+ new job alerts in inbox this week.</div>
    </div>
    <div class="exec-card calendar">
      <div class="ec-label">🔵 Biggest Calendar Item</div>
      <div class="ec-title">State Farm Bill Due Monday + CUNY Interview Thursday</div>
      <div class="ec-sub">State Farm bill reminder fires Monday Sep 7. RSVP still needed for HR Networking Zoom (Wed), Open Office Hours (Thu), and M&amp;M meeting (Thu). Confirm or decline promptly.</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════ -->
<!-- SECTION 3: ACTION REQUIRED                     -->
<!-- ═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">🚨</span> Action Required</div>

  <div class="action-card red">
    <div class="action-card-label red">🔴 Security — Immediate</div>
    <div class="action-card-title">Delete Explicit Spam &amp; Scam Emails Still in Inbox</div>
    <div class="action-row"><span class="action-row-label">Source:</span><span>Gmail Inbox — "F*ckMeHard" (×2), "SteelPower"</span></div>
    <div class="action-row"><span class="action-row-label">Why it matters:</span><span>Three unsolicited explicit/scam emails are currently sitting in your active inbox — not in trash. They contain suspicious links and should never be clicked.</span></div>
    <div class="action-row"><span class="action-row-label">Next Step:</span><span>Open Gmail → select all three → Mark as Spam → Delete. Consider enabling stronger Gmail spam filters.</span></div>
    <div class="action-row"><span class="action-row-label">Due:</span><span><strong>Today</strong></span></div>
  </div>

  <div class="action-card green">
    <div class="action-card-label green">🟢 Job Search — High Priority</div>
    <div class="action-card-title">Prepare for CUNY Vice Chancellor of Human Resources Interview</div>
    <div class="action-row"><span class="action-row-label">Source:</span><span>Google Calendar — Thu, Sep 11, 3:00–5:00 PM, CUNY Central Office (in-person with Elisa Russo &amp; Sujata Malhotra)</span></div>
    <div class="action-row"><span class="action-row-label">Why it matters:</span><span>This is a confirmed, in-person executive interview. Two back-to-back 1-hour slots are blocked. This is the highest-priority job search event this week.</span></div>
    <div class="action-row"><span class="action-row-label">Next Step:</span><span>Research Elisa Russo and Sujata Malhotra. Prepare CUNY-specific talking points. Plan travel to CUNY Central Office. Confirm attire and materials.</span></div>
    <div class="action-row"><span class="action-row-label">Due:</span><span><strong>By Wednesday, Sep 9</strong></span></div>
  </div>

  <div class="action-card green">
    <div class="action-card-label green">🟢 Job Search — Follow Up</div>
    <div class="action-card-title">Reply to Sakshi Khatri's LinkedIn Message</div>
    <div class="action-row"><span class="action-row-label">Source:</span><span>Gmail Inbox — LinkedIn notification, Sun Sep 6, unread</span></div>
    <div class="action-row"><span class="action-row-label">Why it matters:</span><span>A professional outreach message is waiting. Leaving LinkedIn messages unread signals low engagement to recruiters and contacts.</span></div>
    <div class="action-row"><span class="action-row-label">Next Step:</span><span>Open LinkedIn → respond to Sakshi's message today.</span></div>
    <div class="action-row"><span class="action-row-label">Due:</span><span><strong>Today or Tomorrow</strong></span></div>
  </div>

  <div class="action-card green">
    <div class="action-card-label green">🟢 Job Search — Leverage</div>
    <div class="action-card-title">Egon Zehnder Searched Your LinkedIn Profile</div>
    <div class="action-row"><span class="action-row-label">Source:</span><span>LinkedIn notification — "You appeared in 2 searches" — someone from Egon Zehnder</span></div>
    <div class="action-row"><span class="action-row-label">Why it matters:</span><span>Egon Zehnder is a top global executive search firm. A recruiter actively searched your profile. This is a warm signal — reach out proactively.</span></div>
    <div class="action-row"><span class="action-row-label">Next Step:</span><span>Open LinkedIn → Who Viewed Your Profile → identify the Egon Zehnder contact → send a brief, professional connection request or InMail.</span></div>
    <div class="action-row"><span class="action-row-label">Due:</span><span><strong>Today — while profile view is fresh</strong></span></div>
  </div>

  <div class="action-card yellow">
    <div class="action-card-label yellow">🟡 Billing — Deadline</div>
    <div class="action-card-title">State Farm Bill Due Monday, September 7</div>
    <div class="action-row"><span class="action-row-label">Source:</span><span>Google Calendar — All-day event, Mon Sep 7</span></div>
    <div class="action-row"><span class="action-row-label">Why it matters:</span><span>Bill payment reminder is set for tomorrow. Missing an insurance payment can result in a lapse in coverage.</span></div>
    <div class="action-row"><span class="action-row-label">Next Step:</span><span>Log in to State Farm account or check auto-pay status today to ensure payment processes on time.</span></div>
    <div class="action-row"><span class="action-row-label">Due:</span><span><strong>Monday, Sep 7</strong></span></div>
  </div>

  <div class="action-card blue">
    <div class="action-card-label blue">🔵 Calendar — RSVP Needed</div>
    <div class="action-card-title">RSVP to 3 Pending Calendar Events This Week</div>
    <div class="action-row"><span class="action-row-label">Source:</span><span>Google Calendar — HR Networking Zoom (Wed 9/9), Open Office Hours (Thu 9/10), M&amp;M with Monte Montoya (Thu 9/10)</span></div>
    <div class="action-row"><span class="action-row-label">Why it matters:</span><span>Three events show "needsAction" RSVP status. Organizers are waiting for your confirmation, especially the large HR networking groups.</span></div>
    <div class="action-row"><span class="action-row-label">Next Step:</span><span>Open Google Calendar → respond to each invite (Accept or Decline) by Monday.</span></div>
    <div class="action-row"><span class="action-row-label">Due:</span><span><strong>Monday, Sep 7</strong></span></div>
  </div>

  <div class="action-card yellow">
    <div class="action-card-label yellow">🟡 Job Search — Track Application</div>
    <div class="action-card-title">Log VP HRBP Application to Amy (Rescued from Trash)</div>
    <div class="action-row"><span class="action-row-label">Source:</span><span>Gmail — Rescued from Trash — outbound application email sent Tue Sep 8 to Amy (Cprime connection)</span></div>
    <div class="action-row"><span class="action-row-label">Why it matters:</span><span>This was an outbound job application that ended up in Trash. It has been rescued. Add it to your job search tracker and flag for follow-up if no response by next week.</span></div>
    <div class="action-row"><span class="action-row-label">Next Step:</span><span>Add to job search tracker. Note: application sent Tue Sep 8 to Amy re: VP HRBP Leader role at PE-backed company.</span></div>
    <div class="action-row"><span class="action-row-label">Due:</span><span><strong>This week</strong></span></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════ -->
<!-- SECTION 4: FULL 7-DAY CALENDAR                 -->
<!-- ═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">📅</span> Full 7-Day Calendar</div>

  <!-- Sunday Sep 6 -->
  <div class="cal-day">
    <div class="cal-day-header today">☀️ Sunday, September 6, 2026 — TODAY</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div>
        <div class="cal-event-name">No scheduled events</div>
        <div class="cal-detail">Focus day — use time for interview prep, inbox cleanup, and RSVP responses.</div>
      </div>
    </div>
  </div>

  <!-- Monday Sep 7 -->
  <div class="cal-day">
    <div class="cal-day-header">🗓 Monday, September 7, 2026 — Labor Day</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div>
        <div class="cal-event-name">State Farm Bill</div>
        <span class="cal-badge confirmed">Confirmed</span>
        <div class="cal-detail">📍 No location specified</div>
        <div class="cal-detail">⚠️ <strong>Prep:</strong> Verify payment has processed or log in to pay. Do not miss — insurance lapse risk.</div>
      </div>
    </div>
  </div>

  <!-- Tuesday Sep 8 -->
  <div class="cal-day">
    <div class="cal-day-header">🗓 Tuesday, September 8, 2026</div>
    <div class="cal-event">
      <div class="cal-time">10:00–11:00 AM</div>
      <div>
        <div class="cal-event-name">Nails 💅</div>
        <span class="cal-badge confirmed">Confirmed</span>
        <div class="cal-detail">📍 Location not specified</div>
        <div class="cal-detail">Prep: Confirm appointment time/location. Allow travel buffer.</div>
      </div>
    </div>
  </div>

  <!-- Wednesday Sep 9 -->
  <div class="cal-day">
    <div class="cal-day-header">🗓 Wednesday, September 9, 2026</div>
    <div class="cal-event">
      <div class="cal-time">12:00–1:30 PM</div>
      <div>
        <div class="cal-event-name">HR Networking &amp; Job Search Group — Zoom 2</div>
        <span class="cal-badge needs">⚠️ RSVP Needed</span>
        <span class="cal-badge conflict">~190 Attendees</span>
        <div class="cal-detail">📍 <a href="https://us06web.zoom.us/j/81954171722" style="color:#3182ce">Zoom Link</a></div>
        <div class="cal-detail"><strong>Prep:</strong> Review HR Networking Team Guidelines (linked in invite description). Prepare networking talking points. Confirm RSVP today.</div>
        <div class="cal-detail">Note: Also has a duplicate "Network" calendar entry at the same time (confirmed) — both reference the same session.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-time">12:00–1:30 PM</div>
      <div>
        <div class="cal-event-name">Network (duplicate entry)</div>
        <span class="cal-badge confirmed">Confirmed</span>
        <div class="cal-detail">Same session as HR Networking &amp; Job Search Group above. No separate action needed.</div>
      </div>
    </div>
  </div>

  <!-- Thursday Sep 10 -->
  <div class="cal-day">
    <div class="cal-day-header">🗓 Thursday, September 10, 2026</div>
    <div class="cal-event">
      <div class="cal-time">9:00–10:30 AM</div>
      <div>
        <div class="cal-event-name">Executive Roundtable (John Madigan)</div>
        <span class="cal-badge declined">❌ Declined</span>
        <div class="cal-detail">📍 <a href="https://us02web.zoom.us/j/207786667" style="color:#3182ce">Zoom Link</a> | Meeting ID: 207 786 667 | PW: 205454</div>
        <div class="cal-detail">You have declined this event. No action needed unless you wish to reconsider.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-time">12:00–1:00 PM</div>
      <div>
        <div class="cal-event-name">HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
        <span class="cal-badge needs">⚠️ RSVP Needed</span>
        <div class="cal-detail">📍 <a href="https://us06web.zoom.us/j/85945371140" style="color:#3182ce">Zoom Link</a></div>
        <div class="cal-detail"><strong>Note:</strong> Organizer requests NO automated AI notetaking tools. Open discussion format.</div>
        <div class="cal-detail"><strong>Prep:</strong> Confirm RSVP. Prepare 1–2 discussion topics or questions.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-time">1:00–2:00 PM</div>
      <div>
        <div class="cal-event-name">M&amp;M (Meeting with Monte Montoya)</div>
        <span class="cal-badge needs">⚠️ RSVP Needed</span>
        <div class="cal-detail">📧 monte.montoya@gmail.com</div>
        <div class="cal-detail"><strong>Prep:</strong> Confirm RSVP with Monte. Clarify agenda/purpose of meeting.</div>
        <div class="cal-detail">⚠️ <strong>Conflict warning:</strong> This runs 1:00–2:00 PM. CUNY interview is at 3:00 PM same day — allow travel time buffer.</div>
      </div>
    </div>
  </div>

  <!-- Friday Sep 11 -->
  <div class="cal-day">
    <div class="cal-day-header" style="background: linear-gradient(90deg, #38a169, #276749); color:#fff;">🌟 Friday, September 11, 2026 — INTERVIEW DAY</div>
    <div class="cal-event">
      <div class="cal-time">9:30–10:30 AM</div>
      <div>
        <div class="cal-event-name">PT (Physical Therapy)</div>
        <span class="cal-badge confirmed">Confirmed</span>
        <div class="cal-detail">📍 Location not specified</div>
        <div class="cal-detail">Prep: Confirm appointment. This is in the morning — leaves afternoon free for CUNY interview.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-time">3:00–4:00 PM</div>
      <div>
        <div class="cal-event-name">🎯 Vice Chancellor of Human Resources Interview — CUNY</div>
        <span class="cal-badge confirmed">Confirmed</span>
        <span class="cal-badge highlight">In-Person</span>
        <div class="cal-detail">📍 CUNY Central Office | Interviewers: Elisa Russo, Sujata Malhotra</div>
        <div class="cal-detail"><strong>Prep Needed:</strong> Research CUNY's HR structure, recent initiatives, Elisa Russo &amp; Sujata Malhotra LinkedIn profiles. Prepare executive leadership examples. Dress professionally. Bring copies of resume &amp; portfolio.</div>
        <div class="cal-detail">Note: Two calendar entries for this slot (3–4 PM confirmed + 4–5 PM accepted) suggest a 2-hour block. Plan accordingly.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-time">4:00–5:00 PM</div>
      <div>
        <div class="cal-event-name">Vice Chancellor of Human Resources Interview (continued)</div>
        <span class="cal-badge accepted">Accepted</span>
        <div class="cal-detail">📍 CUNY Central Office (continued from 3 PM session)</div>
        <div class="cal-detail">This appears to be the second hour of the same interview block. Prepare for extended discussion.</div>
      </div>
    </div>
  </div>

  <!-- Saturday Sep 12 -->
  <div class="cal-day">
    <div class="cal-day-header">🗓 Saturday, September 12, 2026</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div>
        <div class="cal-event-name">No scheduled events</div>
        <div class="cal-detail">Rest and recovery after interview week. Good opportunity for job search follow-ups.</div>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════ -->
<!-- SECTION 5: JOB SEARCH & INTERVIEW PIPELINE    -->
<!-- ═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">💼</span> Job Search &amp; Interview Pipeline</div>
  <table>
    <thead>
      <tr>
        <th>Fit</th>
        <th>Role / Opportunity</th>
        <th>Source</th>
        <th>Salary</th>
        <th>Status</th>
        <th>Next Step</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="tag green">🔥 HIGH</span></td>
        <td><strong>Vice Chancellor of Human Resources</strong><br><small>CUNY — Central Office</small></td>
        <td>Google Calendar</td>
        <td>N/A</td>
        <td><span class="tag green">Interview Confirmed — Sep 11</span></td>
        <td>Prepare this week. In-person. 2-hour block. With Elisa Russo &amp; Sujata Malhotra.</td>
      </tr>
      <tr>
        <td><span class="tag green">🔥 HIGH</span></td>
        <td><strong>VP, HR Business Partner Leader</strong><br><small>PE-backed (Cprime context)</small></td>
        <td>Gmail — Rescued from Trash</td>
        <td>N/A</td>
        <td><span class="tag yellow">Application Sent to Amy — Sep 8</span></td>
        <td>Log in tracker. Follow up if no response by Sep 15.</td>
      </tr>
      <tr>
        <td><span class="tag green">🔥 HIGH</span></td>
        <td><strong>VP, HR Business Partner Leader</strong><br><small>Dayforce + 4 more roles</small></td>
        <td>LinkedIn Job Alert</td>
        <td>$198K–$310K</td>
        <td><span class="tag blue">New Alert — Unread</span></td>
        <td>Review all 5 roles. Apply to Dayforce if strong fit.</td>
      </tr>
      <tr>
        <td><span class="tag green">HIGH</span></td>
        <td><strong>Senior Director, People Strategy &amp; Advisory</strong><br><small>BNY + 16 more roles</small></td>
        <td>LinkedIn Job Alert</td>
        <td>N/A</td>
        <td><span class="tag blue">New Alert — Unread</span></td>
        <td>Review BNY lead + curated list of 16 additional roles.</td>
      </tr>
      <tr>
        <td><span class="tag green">HIGH</span></td>
        <td><strong>Assistant VP, Human Resources</strong><br><small>Columbia University + 3 more</small></td>
        <td>LinkedIn Job Alert</td>
        <td>$220K–$265K</td>
        <td><span class="tag blue">New Alert — Unread</span></td>
        <td>Columbia is a strong fit — apply if not already done.</td>
      </tr>
      <tr>
        <td><span class="tag yellow">MEDIUM</span></td>
        <td><strong>Sakshi Khatri — LinkedIn Message</strong><br><small>Possibly a recruiter or peer referral</small></td>
        <td>LinkedIn via Gmail</td>
        <td>N/A</td>
        <td><span class="tag yellow">Unread — Awaiting Response</span></td>
        <td>Open LinkedIn and respond today. May be a lead or referral opportunity.</td>
      </tr>
      <tr>
        <td><span class="tag green">HIGH</span></td>
        <td><strong>Egon Zehnder — Profile Search</strong><br><small>Executive Search Firm</small></td>
        <td>LinkedIn Notification</td>
        <td>N/A</td>
        <td><span class="tag orange">Warm Lead — Act Now</span></td>
        <td>Identify the searcher. Send proactive connection or InMail today.</td>
      </tr>
      <tr>
        <td><span class="tag yellow">MEDIUM</span></td>
        <td><strong>HR Networking &amp; Job Search Group Zoom</strong><br><small>~190 HR professionals</small></td>
        <td>Google Calendar — Wed Sep 9</td>
        <td>N/A</td>
        <td><span class="tag yellow">RSVP Pending</span></td>
        <td>Confirm RSVP. Prepare 30-sec intro. Bring 2 referral ask talking points.</td>
      </tr>
      <tr>
        <td><span class="tag yellow">MEDIUM</span></td>
        <td><strong>Open Office Hours — HR Job Search</strong><br><small>Networking group</small></td>
        <td>Google Calendar — Thu Sep 10</td>
        <td>N/A</td>
        <td><span class="tag yellow">RSVP Pending</span></td>
        <td>Confirm RSVP. Prepare 1–2 questions to raise in open discussion.</td>
      </tr>
      <tr>
        <td><span class="tag yellow">MEDIUM</span></td>
        <td><strong>M&amp;M — Meeting with Monte Montoya</strong></td>
        <td>Google Calendar — Thu Sep 10</td>
        <td>N/A</td>
        <td><span class="tag yellow">RSVP Pending</span></td>
        <td>Confirm with Monte. Clarify purpose — networking, referral, or personal.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════ -->
<!-- SECTION 6: FULL EMAIL REVIEW BY CATEGORY       -->
<!-- ═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">📧</span> Full Email Review by Category</div>

  <!-- Security / Risk -->
  <div class="card red">
    <div class="card-title">🔴 Security / Risk — 5 Emails</div>
    <div class="card-meta">Phishing, Explicit Spam, Scam Solicitations</div>
    <div class="card-body">
      <p><strong>Auto-Trashed (Phishing — Before Delivery):</strong></p>
      <ul style="margin: 6px 0 10px 18px;">
        <li><strong>melissaw212 spoofed (walkventure.my.id)</strong> — "We have blocked your account 🚫" — iCloud account-threat phishing. Spoofed domain, urgent language to harvest credentials. <span class="auto-trash-note">Auto-Trashed — Phishing</span></li>
      </ul>
      <p><strong>In Inbox — Delete Immediately:</strong></p>
      <ul style="margin: 6px 0 10px 18px;">
        <li><strong>"F*ckMeHard" (×2)</strong> — Explicit spam from spoofed random domains. Two separate emails sent Sun Sep 6. Do not click any links.</li>
        <li><strong>SteelPower</strong> — "melissaw212 Discover SteelPower for Men" — scam male wellness solicitation from random domain. Do not engage.</li>
      </ul>
      <p><strong>In Trash (not auto-trashed):</strong></p>
      <ul style="margin: 6px 0 10px 18px;">
        <li><strong>"Sex Trick"</strong> — "Watch this Alone" — explicit spam. Already trashed. Permanently delete.</li>
      </ul>
    </div>
    <div class="card-row">
      <span class="tag red">DELETE NOW</span>
      <span class="tag red">DO NOT CLICK LINKS</span>
      <span class="tag red">Report as Spam</span>
    </div>
  </div>

  <!-- Job Search -->
  <div class="card green">
    <div class="card-title">🟢 Job Search — 5 Emails</div>
    <div class="card-meta">LinkedIn Job Alerts, Applications, Recruiter Activity</div>
    <div class="card-body">
      <ul style="margin: 6px 0 10px 18px;">
        <li><strong>LinkedIn Job Alerts</strong> — VP HRBP at Dayforce + 4 more ($198K–$310K) — <em>Unread, in inbox</em></li>
        <li><strong>LinkedIn Job Alerts</strong> — Sr. Director People Strategy at BNY + 16 more — <em>Unread, in inbox</em></li>
        <li><strong>LinkedIn Job Alerts</strong> — AVP HR at Columbia University + 3 more ($220K–$265K) — <em>Unread, in inbox</em></li>
        <li><strong>Melissa (self → Amy)</strong> — VP HRBP Leader application email — <em>Rescued from Trash</em> <span class="rescued-note">✅ Rescued — Outbound job application, retain for tracking</span></li>
        <li><strong>LinkedIn</strong> — You appeared in 2 searches (Egon Zehnder) — <em>Unread, not in inbox, not trashed</em></li>
      </ul>
    </div>
    <div class="card-row">
      <span class="tag green">REVIEW ALL</span>
      <span class="tag green">APPLY THIS WEEK</span>
      <span class="tag green">TRACK APPLICATION</span>
    </div>
  </div>

  <!-- Recruiters / Networking -->
  <div class="card green">
    <div class="card-title">🟢 Recruiters / Networking — 1 Email</div>
    <div class="card-meta">LinkedIn DMs</div>
    <div class="card-body">
      <ul style="margin: 6px 0 10px 18px;">
        <li><strong>Sakshi Khatri via LinkedIn</strong> — "Sakshi just messaged you" — 1 new message awaiting response. Unread, in inbox.</li>
      </ul>
    </div>
    <div class="card-row"><span class="tag green">RESPOND TODAY</span></div>
  </div>

  <!-- Financial / Billing -->
  <div class="card yellow">
    <div class="card-title">🟡 Financial / Billing — 5 Emails</div>
    <div class="card-meta">Robinhood Roth IRA, State Farm (Calendar)</div>
    <div class="card-body">
      <ul style="margin: 6px 0 10px 18px;">
        <li><strong>Robinhood</strong> — "You started an IRA contribution" — Roth IRA initiated. Retain for records.</li>
        <li><strong>Robinhood</strong> — "Funds available for investing" — $5.00 instant deposit available.</li>
        <li><strong>Robinhood</strong> — "Your IRA contribution is complete" — Roth IRA contribution confirmed.</li>
        <li><strong>Robinhood</strong> — "Your transfer is complete" — $0.45 to Roth IRA (••8947).</li>
        <li><strong>SmartAsset Weekender</strong> — "5 Signs It May Be Time to Change Financial Advisors" — In trash. Financial newsletter. <em>Trashed.</em></li>
      </ul>
    </div>
    <div class="card-row">
      <span class="tag yellow">RETAIN ROBINHOOD EMAILS</span>
      <span class="tag gray">SMARTASSET — DELETE</span>
    </div>
  </div>

  <!-- Professional Development -->
  <div class="card purple">
    <div class="card-title">🟣 Professional Development — 5 Emails</div>
    <div class="card-meta">AI Tools, Masterclasses, Medium Articles</div>
    <div class="card-body">
      <ul style="margin: 6px 0 10px 18px;">
        <li><strong>Pranit Naik (Medium)</strong> — "Anthropic Dropped Fable 5.1 &amp; Mythos 5.1 (Costs Cut 45%)" — Unread, in inbox. Relevant AI industry update.</li>
        <li><strong>Melissa (self)</strong> — "5_Claude_Code_Plugins_Setup_Guide.pdf" — Self-sent Google Drive link. In inbox.</li>
        <li><strong>Melissa (self)</strong> — "The 24 Claude Setup | Made For More" — Self-sent AI setup guide. In inbox.</li>
        <li><strong>Melissa (self)</strong> — [No Subject — Substack link] — Self-sent iOS share. In inbox.</li>
        <li><strong>Made For More AI</strong> — "your masterclass, as promised" — AI Consultant Masterclass link. In trash.</li>
      </ul>
    </div>
    <div class="card-row">
      <span class="tag purple">READ THIS WEEK</span>
      <span class="tag purple">SAVE LINKS</span>
      <span class="tag gray">MADE FOR MORE — REVIEW BEFORE DELETE</span>
