<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Monday, August 31, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrapper { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 16px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .date { font-size: 15px; color: #a8b2d8; margin-top: 4px; }
  .header .meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.08); border-radius: 10px; padding: 10px 20px; text-align: center; }
  .header .meta-item .num { font-size: 26px; font-weight: 700; color: #e2e8f0; }
  .header .meta-item .label { font-size: 11px; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; margin-top: 2px; }

  /* SECTION */
  .section { background: #fff; border-radius: 14px; padding: 24px 28px; margin-bottom: 20px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); }
  .section-title { font-size: 17px; font-weight: 700; margin-bottom: 16px; display: flex; align-items: center; gap: 8px; border-bottom: 2px solid #f1f5f9; padding-bottom: 10px; }
  .section-title .icon { font-size: 20px; }

  /* EXECUTIVE SUMMARY */
  .exec-summary .bullet { display: flex; align-items: flex-start; gap: 12px; padding: 12px 16px; border-radius: 10px; margin-bottom: 10px; }
  .exec-summary .bullet:last-child { margin-bottom: 0; }
  .exec-summary .bullet.red { background: #fff1f1; border-left: 4px solid #e53e3e; }
  .exec-summary .bullet.green { background: #f0fff4; border-left: 4px solid #38a169; }
  .exec-summary .bullet.blue { background: #ebf8ff; border-left: 4px solid #3182ce; }
  .exec-summary .bullet .b-icon { font-size: 18px; flex-shrink: 0; margin-top: 2px; }
  .exec-summary .bullet strong { display: block; font-size: 13px; margin-bottom: 2px; }
  .exec-summary .bullet p { font-size: 13px; color: #4a5568; }

  /* TRIAGE TABLE */
  .triage-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .triage-table th { background: #f8fafc; text-align: left; padding: 9px 12px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.8px; color: #64748b; border-bottom: 2px solid #e2e8f0; }
  .triage-table td { padding: 9px 12px; border-bottom: 1px solid #f1f5f9; vertical-align: top; }
  .triage-table tr:last-child td { border-bottom: none; }
  .triage-table tr:hover td { background: #f8fafc; }
  .badge { display: inline-block; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 600; white-space: nowrap; }
  .badge-rescued { background: #d1fae5; color: #065f46; }
  .badge-inbox { background: #dbeafe; color: #1e40af; }
  .badge-trashed-auto { background: #fee2e2; color: #991b1b; }
  .badge-trashed-manual { background: #f1f5f9; color: #475569; }

  /* ACTION CARDS */
  .action-card { border-radius: 12px; padding: 16px 18px; margin-bottom: 14px; border-left: 5px solid; }
  .action-card:last-child { margin-bottom: 0; }
  .action-card.red { background: #fff5f5; border-color: #fc8181; }
  .action-card.yellow { background: #fffbeb; border-color: #f6ad55; }
  .action-card.blue { background: #ebf8ff; border-color: #63b3ed; }
  .action-card.green { background: #f0fff4; border-color: #68d391; }
  .action-card.purple { background: #faf5ff; border-color: #b794f4; }
  .action-card .ac-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px; opacity: 0.7; }
  .action-card h4 { font-size: 14px; font-weight: 700; margin-bottom: 8px; }
  .action-card .ac-row { display: flex; gap: 6px; margin-bottom: 4px; font-size: 12.5px; }
  .action-card .ac-row .ac-key { font-weight: 600; min-width: 130px; color: #4a5568; }
  .action-card .ac-row .ac-val { color: #1a202c; }
  .action-card .ac-step { margin-top: 10px; padding: 8px 12px; background: rgba(0,0,0,0.04); border-radius: 7px; font-size: 12.5px; }
  .action-card .ac-step strong { color: #2d3748; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #3182ce; margin-bottom: 10px; padding: 6px 0; border-bottom: 1px solid #ebf8ff; }
  .cal-event { background: #f0f7ff; border-radius: 10px; padding: 13px 16px; margin-bottom: 10px; border-left: 4px solid #3182ce; }
  .cal-event.declined { border-color: #fc8181; background: #fff5f5; }
  .cal-event.confirmed { border-color: #68d391; background: #f0fff4; }
  .cal-event.needsAction { border-color: #f6ad55; background: #fffbeb; }
  .cal-event h4 { font-size: 14px; font-weight: 700; margin-bottom: 6px; }
  .cal-event .ev-row { font-size: 12.5px; margin-bottom: 3px; display: flex; gap: 6px; }
  .cal-event .ev-row .ev-key { font-weight: 600; color: #4a5568; min-width: 90px; }
  .cal-event .rsvp-badge { display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 11px; font-weight: 700; }
  .rsvp-confirmed { background: #c6f6d5; color: #276749; }
  .rsvp-declined { background: #fed7d7; color: #9b2335; }
  .rsvp-needsAction { background: #fef3c7; color: #92400e; }
  .conflict-warn { background: #fff3cd; border: 1px solid #f6ad55; border-radius: 7px; padding: 6px 12px; font-size: 12px; margin-top: 8px; color: #7c4a00; }

  /* JOB SEARCH */
  .job-row { background: #f9fafb; border-radius: 10px; padding: 12px 16px; margin-bottom: 10px; border-left: 4px solid #38a169; }
  .job-row h4 { font-size: 13.5px; font-weight: 700; margin-bottom: 5px; }
  .job-row .jd-row { font-size: 12.5px; margin-bottom: 3px; display: flex; gap: 6px; }
  .job-row .jd-row .jd-key { font-weight: 600; color: #4a5568; min-width: 100px; }
  .fit-high { display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 11px; font-weight: 700; background: #c6f6d5; color: #276749; }
  .fit-med { display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 11px; font-weight: 700; background: #fef3c7; color: #92400e; }
  .fit-low { display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 11px; font-weight: 700; background: #e2e8f0; color: #4a5568; }

  /* CATEGORY REVIEW */
  .cat-block { border-radius: 12px; padding: 15px 18px; margin-bottom: 12px; }
  .cat-block.red { background: #fff5f5; border-left: 5px solid #e53e3e; }
  .cat-block.yellow { background: #fffbeb; border-left: 5px solid #d69e2e; }
  .cat-block.blue { background: #ebf8ff; border-left: 5px solid #3182ce; }
  .cat-block.green { background: #f0fff4; border-left: 5px solid #38a169; }
  .cat-block.purple { background: #faf5ff; border-left: 5px solid #805ad5; }
  .cat-block.gray { background: #f7f8fa; border-left: 5px solid #a0aec0; }
  .cat-block.orange { background: #fffaf0; border-left: 5px solid #dd6b20; }
  .cat-block h4 { font-size: 13.5px; font-weight: 700; margin-bottom: 8px; }
  .cat-block .cb-row { font-size: 12.5px; margin-bottom: 3px; display: flex; gap: 6px; }
  .cat-block .cb-row .cb-key { font-weight: 600; color: #4a5568; min-width: 140px; }

  /* TRASH REVIEW */
  .trash-group { margin-bottom: 18px; }
  .trash-group h4 { font-size: 13px; font-weight: 700; margin-bottom: 10px; padding: 6px 12px; border-radius: 7px; }
  .trash-group.restore h4 { background: #c6f6d5; color: #276749; }
  .trash-group.review h4 { background: #fef3c7; color: #92400e; }
  .trash-group.delete h4 { background: #e2e8f0; color: #4a5568; }
  .trash-item { padding: 8px 12px; border-bottom: 1px solid #f1f5f9; font-size: 12.5px; }
  .trash-item:last-child { border-bottom: none; }
  .trash-item .ti-from { font-weight: 600; }

  /* PROMO TABLE */
  .promo-table { width: 100%; border-collapse: collapse; font-size: 12.5px; }
  .promo-table th { background: #f8fafc; text-align: left; padding: 8px 12px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.8px; color: #64748b; border-bottom: 2px solid #e2e8f0; }
  .promo-table td { padding: 8px 12px; border-bottom: 1px solid #f1f5f9; vertical-align: top; }
  .promo-table tr:last-child td { border-bottom: none; }

  /* NEWSLETTER TABLE */
  .nl-table { width: 100%; border-collapse: collapse; font-size: 12.5px; }
  .nl-table th { background: #f8fafc; text-align: left; padding: 8px 12px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.8px; color: #64748b; border-bottom: 2px solid #e2e8f0; }
  .nl-table td { padding: 8px 12px; border-bottom: 1px solid #f1f5f9; vertical-align: top; }
  .nl-table tr:last-child td { border-bottom: none; }

  /* ACCOUNTING TABLE */
  .acct-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .acct-table th { background: #1a1a2e; color: #fff; text-align: left; padding: 10px 14px; font-size: 12px; }
  .acct-table td { padding: 9px 14px; border-bottom: 1px solid #f1f5f9; }
  .acct-table tr:nth-child(even) td { background: #f8fafc; }
  .acct-table tr.total-row td { font-weight: 700; background: #e2e8f0; font-size: 14px; }

  /* DASHBOARD */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }
  .dash-card { border-radius: 12px; padding: 16px 18px; }
  .dash-card.red { background: #fff5f5; border: 1px solid #fc8181; }
  .dash-card.yellow { background: #fffbeb; border: 1px solid #f6ad55; }
  .dash-card.blue { background: #ebf8ff; border: 1px solid #63b3ed; }
  .dash-card.green { background: #f0fff4; border: 1px solid #68d391; }
  .dash-card.purple { background: #faf5ff; border: 1px solid #b794f4; }
  .dash-card.gray { background: #f7f8fa; border: 1px solid #cbd5e0; }
  .dash-card h5 { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; color: #4a5568; }
  .dash-card ul { list-style: none; padding: 0; }
  .dash-card ul li { font-size: 12.5px; padding: 3px 0; border-bottom: 1px solid rgba(0,0,0,0.05); }
  .dash-card ul li:last-child { border-bottom: none; }

  /* ACTION ITEMS TABLE */
  .ai-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .ai-table th { background: #1e3a5f; color: #fff; text-align: left; padding: 9px 14px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.8px; }
  .ai-table td { padding: 9px 14px; border-bottom: 1px solid #f1f5f9; vertical-align: top; }
  .ai-table tr:last-child td { border-bottom: none; }
  .pri-high { display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 11px; font-weight: 700; background: #fed7d7; color: #9b2335; }
  .pri-med { display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 11px; font-weight: 700; background: #fef3c7; color: #92400e; }
  .pri-low { display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 11px; font-weight: 700; background: #e2e8f0; color: #4a5568; }

  /* TOP 3 */
  .top3 { counter-reset: top3-counter; }
  .top3-item { display: flex; align-items: flex-start; gap: 16px; padding: 16px 18px; border-radius: 12px; margin-bottom: 12px; background: linear-gradient(135deg, #1a1a2e, #0f3460); color: #fff; }
  .top3-item:last-child { margin-bottom: 0; }
  .top3-num { font-size: 32px; font-weight: 900; opacity: 0.3; line-height: 1; min-width: 36px; }
  .top3-content h4 { font-size: 15px; font-weight: 700; margin-bottom: 5px; }
  .top3-content p { font-size: 12.5px; color: #a8b2d8; }

  /* UTILITY */
  .note-box { background: #f0f7ff; border: 1px solid #bee3f8; border-radius: 8px; padding: 10px 14px; font-size: 12.5px; color: #2b6cb0; margin-top: 10px; }
  .tag { display: inline-block; padding: 2px 8px; border-radius: 10px; font-size: 10.5px; font-weight: 600; margin-left: 6px; }
  .tag-rescued { background: #c6f6d5; color: #276749; }
  .tag-auto { background: #fed7d7; color: #9b2335; }
  .rec-keep { color: #276749; font-weight: 600; }
  .rec-delete { color: #9b2335; font-weight: 600; }
  .rec-review { color: #92400e; font-weight: 600; }
  .rec-unsub { color: #6b46c1; font-weight: 600; }
  .rec-ignore { color: #718096; font-weight: 600; }
  a { color: #3182ce; word-break: break-all; }
  .reminder-note { background: #fef3c7; border: 1px solid #f6ad55; border-radius: 8px; padding: 10px 14px; font-size: 12.5px; color: #7c4a00; margin-top: 8px; }
  .phish-warn { background: #fff5f5; border: 1px solid #fc8181; border-radius: 8px; padding: 8px 12px; font-size: 12px; color: #9b2335; margin-top: 6px; }
</style>
</head>
<body>
<div class="page-wrapper">

<!-- ════════════════════════════════════════════════════════ -->
<!-- SECTION 0: EMAIL TRIAGE QUICK LIST -->
<!-- ════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">⚡</span> Email Triage Quick List</div>
  <table class="triage-table">
    <thead>
      <tr>
        <th>Status</th>
        <th>From</th>
        <th>Subject</th>
        <th>Summary</th>
      </tr>
    </thead>
    <tbody>
      <!-- RESCUED FIRST -->
      <tr>
        <td><span class="badge badge-rescued">✅ RESCUED</span></td>
        <td>303 East 83rd / Equity Apartments</td>
        <td>You have a delivery!</td>
        <td>Package waiting for pickup at Apt 03H (Amazon). Rescued from trash — actionable.</td>
      </tr>
      <tr>
        <td><span class="badge badge-rescued">✅ RESCUED</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>Senior People Business Partner, Product &amp; Marketing at GitLab and 36 more</td>
        <td>High-value job alert. Rescued — protected sender, always keep.</td>
      </tr>
      <!-- INBOX ROWS -->
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>melissa (self)</td>
        <td>Tell Ellie</td>
        <td>Self-reminder: book nail appointment with Dana for next Tuesday at midday sync or wrap-up.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>melissa (self)</td>
        <td>claude senses</td>
        <td>Self-sent link (LinkedIn). Review when relevant.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>LinkedIn</td>
        <td>Your application was viewed by IPC Systems</td>
        <td>Application activity — IPC Systems viewed your profile. Follow up opportunity.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>Sr. Manager, Global People Operations at Tenstorrent and 39 more</td>
        <td>Large job alert batch — Tenstorrent lead role. Review for fit.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>Regional Head of Human Resources at The Forum Group and 2 more</td>
        <td>High-value alert: $220K–$250K/year. Strong fit — review immediately.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>Shubbhi Chaturvedi (LinkedIn)</td>
        <td>I want to connect</td>
        <td>Client Partner CDS at Writer — professional connection request. Accept or review.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>Marc Cleroux @ Ten Fold Marc</td>
        <td>I tested 100 Claude Code skills. 5 mattered.</td>
        <td>Marketing/AI newsletter in inbox. Low priority — consider unsubscribing.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>OkCupid</td>
        <td>Someone likes you</td>
        <td>Dating app notification. Personal — low priority.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>Match</td>
        <td>You've had a profile view from Kurt</td>
        <td>Dating app — Kurt, 56, Bernardsville NJ viewed your profile.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>Match</td>
        <td>Donald likes you. See if it's mutual.</td>
        <td>Dating app like notification. Personal — low priority.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>eBay – premierusa_0</td>
        <td>Message re: Orville Redenbacher's Popcorn #397908271888</td>
        <td>Seller thank-you message on recent purchase. Informational.</td>
      </tr>
      <!-- SUMMARY ROWS AT BOTTOM -->
      <tr>
        <td><span class="badge badge-trashed-auto">🗑 TRASHED (auto)</span></td>
        <td colspan="2">5 emails auto-trashed (phishing/spam) — see Trash Review</td>
        <td>TrimRX GLP-1, Honey-Trick, MEDVi GLP-1, CashApp spoof, Cloud.Storage phish. All removed as high-confidence threats.</td>
      </tr>
      <tr>
        <td><span class="badge badge-trashed-manual">🗂 TRASH (manual)</span></td>
        <td colspan="2">33 emails in Trash — see Trash Review</td>
        <td>Newsletters, retail promos, digests, duplicates, and low-value content. Reviewed below.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ════════════════════════════════════════════════════════ -->
<!-- SECTION 1: HEADER -->
<!-- ════════════════════════════════════════════════════════ -->
<div class="header">
  <h1>Good morning, Melissa ☀️</h1>
  <div class="date">Monday, August 31, 2026 &nbsp;·&nbsp; Executive Daily Briefing</div>
  <div class="meta">
    <div class="meta-item">
      <div class="num">50</div>
      <div class="label">Emails Reviewed</div>
    </div>
    <div class="meta-item">
      <div class="num">5</div>
      <div class="label">Calendar Events</div>
    </div>
    <div class="meta-item">
      <div class="num">2</div>
      <div class="label">Rescued from Trash</div>
    </div>
    <div class="meta-item">
      <div class="num">5</div>
      <div class="label">Auto-Trashed (Phish)</div>
    </div>
    <div class="meta-item">
      <div class="num">4</div>
      <div class="label">Action Items</div>
    </div>
  </div>
</div>

<!-- ════════════════════════════════════════════════════════ -->
<!-- SECTION 2: EXECUTIVE SUMMARY -->
<!-- ════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">📋</span> Executive Summary</div>
  <div class="exec-summary">
    <div class="bullet red">
      <div class="b-icon">🔴</div>
      <div>
        <strong>Security Risk: 5 phishing / spam emails auto-removed; 1 ManForceX explicit spam and 1 Casino Yabby scam not yet trashed</strong>
        <p>Five emails were auto-trashed as high-confidence phishing (fake GLP-1 weight loss, fake CashApp/Raging Bull Casino payment, cloud storage lockout scam, explicit spam). Two additional scam/explicit emails (ManForceX, Casino Yabby) remain untrashed and should be deleted immediately. Your email address "melissaw212" is actively being targeted.</p>
      </div>
    </div>
    <div class="bullet green">
      <div class="b-icon">🟢</div>
      <div>
        <strong>Top Job Opportunity: Regional Head of Human Resources at The Forum Group — $220K–$250K/year</strong>
        <p>LinkedIn flagged a high-value HR leadership role at $220K–$250K. Additionally, IPC Systems viewed your application today (strong signal), GitLab SPBP role was rescued from trash, and Tenstorrent Sr. Manager Global People Ops is in a new batch of 39+ alerts. Your search is active and generating traction.</p>
      </div>
    </div>
    <div class="bullet blue">
      <div class="b-icon">🔵</div>
      <div>
        <strong>Calendar: Two key events this week need RSVP — HR Networking Group (Wed) and Open Office Hours (Thu); coaching call with Rita confirmed Thursday</strong>
        <p>HR Networking &amp; Job Search Group (Wed Sept 2, 12–1:30pm) is pending RSVP. Open Office Hours (Thu Sept 3, 12–1pm) also pending. Coaching call with Rita Ramakrishnan is confirmed for Thursday 10–10:45am. Executive Roundtable (Thu) was declined. RSVPs needed today.</p>
      </div>
    </div>
  </div>
</div>

<!-- ════════════════════════════════════════════════════════ -->
<!-- SECTION 3: ACTION REQUIRED -->
<!-- ════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">⚠️</span> Action Required</div>

  <div class="action-card red">
    <div class="ac-label">🔴 Security — Immediate</div>
    <h4>Delete Remaining Scam / Explicit Spam Emails</h4>
    <div class="ac-row"><span class="ac-key">Source:</span><span class="ac-val">Casino Yabby (scam), ManForceX (explicit), March On PAC (political solicitation), Size.Does.Matter (spam)</span></div>
    <div class="ac-row"><span class="ac-key">Why it matters:</span><span class="ac-val">These emails are not in inbox but are not trashed. They contain click-harvest scams, explicit content, and spoofed payment notifications. Your username is being actively scraped and targeted.</span></div>
    <div class="ac-step"><strong>Next step:</strong> Trash Casino Yabby, ManForceX, Size.Does.Matter, and Honey-Trick manually. Consider setting up a Gmail filter for the spoofed domain patterns (*.us random domains). Review "Samantha via March On PAC" and delete if not subscribed.</div>
    <div class="ac-row" style="margin-top:8px;"><span class="ac-key">Due:</span><span class="ac-val">Today</span></div>
  </div>

  <div class="action-card yellow">
    <div class="ac-label">🟡 Follow-Up — Job Search</div>
    <h4>RSVP: HR Networking &amp; Job Search Group (Wednesday, Sept 2)</h4>
    <div class="ac-row"><span class="ac-key">Source:</span><span class="ac-val">Google Calendar — HR Networking &amp; Job Search Group - Zoom 2</span></div>
    <div class="ac-row"><span class="ac-key">Why it matters:</span><span class="ac-val">Status is "needsAction" — you have not RSVPd. This is a large peer networking group (170+ members) relevant to your HR job search.</span></div>
    <div class="ac-step"><strong>Next step:</strong> Accept or decline the calendar invite. Join Zoom: <a href="https://us06web.zoom.us/j/81954171722">us06web.zoom.us/j/81954171722</a></div>
    <div class="ac-row" style="margin-top:8px;"><span class="ac-key">Due:</span><span class="ac-val">Today (event is Wednesday)</span></div>
  </div>

  <div class="action-card yellow">
    <div class="ac-label">🟡 RSVP Pending</div>
    <h4>RSVP: HR Networking &amp; Job Search Open Office Hours (Thursday, Sept 3)</h4>
    <div class="ac-row"><span class="ac-key">Source:</span><span class="ac-val">Google Calendar — HR Networking &amp; Job Search: Open Office Hours - Zoom 2</span></div>
    <div class="ac-row"><span class="ac-key">Why it matters:</span><span class="ac-val">Status is "needsAction." Same large peer group, different format — open discussion, no recording. Complementary to the Wednesday session.</span></div>
    <div class="ac-step"><strong>Next step:</strong> Accept or decline. Note: no AI notetaking tools per host instructions. Join: <a href="https://us06web.zoom.us/j/85945371140">us06web.zoom.us/j/85945371140</a></div>
    <div class="ac-row" style="margin-top:8px;"><span class="ac-key">Due:</span><span class="ac-val">Today (event is Thursday)</span></div>
  </div>

  <div class="action-card green">
    <div class="ac-label">🟢 Job Search — High Priority</div>
    <h4>Review &amp; Apply: Regional Head of HR at The Forum Group ($220K–$250K)</h4>
    <div class="ac-row"><span class="ac-key">Source:</span><span class="ac-val">LinkedIn Job Alerts — Regional Head of Human Resources at The Forum Group and 2 more</span></div>
    <div class="ac-row"><span class="ac-key">Why it matters:</span><span class="ac-val">Salary range ($220K–$250K) is top-of-market for HR leadership. The Forum Group is a well-known executive recruiting firm. Strong potential fit given your background.</span></div>
    <div class="ac-step"><strong>Next step:</strong> Open LinkedIn alert, review all 3 roles, apply to Forum Group role today. Also review Tenstorrent Sr. Manager, Global People Ops from separate alert (39 roles total).</div>
    <div class="ac-row" style="margin-top:8px;"><span class="ac-key">Due:</span><span class="ac-val">Today / This week</span></div>
  </div>

  <div class="action-card blue">
    <div class="ac-label">🔵 Personal Reminder</div>
    <h4>Nail Appointment Reminder — Book with Dana for Next Tuesday</h4>
    <div class="ac-row"><span class="ac-key">Source:</span><span class="ac-val">Self-email: "Tell Ellie" (melissaw212@gmail.com)</span></div>
    <div class="ac-row"><span class="ac-key">Why it matters:</span><span class="ac-val">You asked to be reminded at the midday sink or wrap-up meeting to book a nail appointment with Dana for next Tuesday (Sept 8).</span></div>
    <div class="ac-step"><strong>Next step:</strong> Raise at today's midday sync or end-of-day wrap-up. Book with Dana for Tue, Sept 8.</div>
    <div class="ac-row" style="margin-top:8px;"><span class="ac-key">Due:</span><span class="ac-val">Today (at midday sync or wrap-up)</span></div>
  </div>

  <div class="action-card yellow">
    <div class="ac-label">🟡 Package Pickup — Rescued from Trash</div>
    <h4>Pick Up Package at Front Desk — Apt 03H</h4>
    <div class="ac-row"><span class="ac-key">Source:</span><span class="ac-val">303 East 83rd / Equity Apartments (rescued from trash)</span></div>
    <div class="ac-row"><span class="ac-key">Why it matters:</span><span class="ac-val">Amazon package is waiting at the front desk of your building. This email was incorrectly sent to trash and rescued.</span></div>
    <div class="ac-step"><strong>Next step:</strong> Pick up package from building front desk at 303 East 83rd Street. Apartment 03H, Amazon tracking noted.</div>
    <div class="ac-row" style="margin-top:8px;"><span class="ac-key">Due:</span><span class="ac-val">Today</span></div>
  </div>

</div>

<!-- ════════════════════════════════════════════════════════ -->
<!-- SECTION 4: FULL 7-DAY CALENDAR -->
<!-- ════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">📅</span> Full 7-Day Calendar</div>

  <div class="note-box">📌 Today (Monday, Aug 31) and Tuesday, Sept 1 have no calendar events scheduled. Next events begin Wednesday, Sept 2.</div>

  <!-- MONDAY -->
  <div class="cal-day" style="margin-top:16px;">
    <div class="cal-day-header">Monday, August 31, 2026</div>
    <div class="cal-event" style="border-color:#a0aec0; background:#f7f8fa;">
      <h4>No events scheduled</h4>
      <div class="ev-row"><span class="ev-key">Note:</span><span>Use today to respond to RSVPs, review job alerts, and handle action items above.</span></div>
    </div>
  </div>

  <!-- TUESDAY -->
  <div class="cal-day">
    <div class="cal-day-header">Tuesday, September 1, 2026</div>
    <div class="cal-event" style="border-color:#a0aec0; background:#f7f8fa;">
      <h4>No events scheduled</h4>
      <div class="ev-row"><span class="ev-key">Note:</span><span>Nail appointment with Dana tentatively targeted for next Tuesday (Sept 8) — confirm today.</span></div>
    </div>
  </div>

  <!-- WEDNESDAY -->
  <div class="cal-day">
    <div class="cal-day-header">Wednesday, September 2, 2026</div>

    <div class="cal-event needsAction">
      <h4>HR Networking &amp; Job Search Group — Zoom 2</h4>
      <div class="ev-row"><span class="ev-key">Time:</span><span>12:00 PM – 1:30 PM ET</span></div>
      <div class="ev-row"><span class="ev-key">RSVP:</span><span><span class="rsvp-badge rsvp-needsAction">⚠️ Needs Action</span></span></div>
      <div class="ev-row"><span class="ev-key">Location:</span><span><a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1">Zoom Link</a></span></div>
      <div class="ev-row"><span class="ev-key">Attendees:</span><span>170+ HR professionals and job seekers</span></div>
      <div class="ev-row"><span class="ev-key">Prep:</span><span>Review team guidelines (linked in description), prepare your 30-second intro and current search status update.</span></div>
      <div class="conflict-warn">⚠️ RSVP REQUIRED — Respond before Wednesday morning.</div>
    </div>

    <div class="cal-event confirmed">
      <h4>Network</h4>
      <div class="ev-row"><span class="ev-key">Time:</span><span>12:00 PM – 1:30 PM ET</span></div>
      <div class="ev-row"><span class="ev-key">RSVP:</span><span><span class="rsvp-badge rsvp-confirmed">✅ Confirmed</span></span></div>
      <div class="ev-row"><span class="ev-key">Location:</span><span>Not specified</span></div>
      <div class="ev-row"><span class="ev-key">Attendees:</span><span>None listed</span></div>
      <div class="ev-row"><span class="ev-key">Prep:</span><span>Appears to be a personal networking block. Verify it doesn't conflict with the HR Networking Zoom above (same time slot).</span></div>
      <div class="conflict-warn">⚠️ CONFLICT: Both this event and the HR Networking Zoom are scheduled 12:00–1:30 PM on Sept 2. Confirm if these are the same event or if one needs to move.</div>
    </div>
  </div>

  <!-- THURSDAY -->
  <div class="cal-day">
    <div class="cal-day-header">Thursday, September 3, 2026</div>

    <div class="cal-event declined">
      <h4>Executive Roundtable (John Madigan)</h4>
      <div class="ev-row"><span class="ev-key">Time:</span><span>9:00 AM – 10:30 AM ET</span></div>
      <div class="ev-row"><span class="ev-key">RSVP:</span><span><span class="rsvp-badge rsvp-declined">❌ Declined</span></span></div>
      <div class="ev-row"><span class="ev-key">Location:</span><span><a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09">Zoom Link</a></span></div>
      <div class="ev-row"><span class="ev-key">Prep:</span><span>None needed — already declined. Keep link in case of change of plans.</span></div>
    </div>

    <div class="cal-event confirmed">
      <h4>Melissa Weiss &amp; Rita Ramakrishnan — Coaching / Consulting</h4>
      <div class="ev-row"><span class="ev-key">Time:</span><span>10:00 AM – 10:45 AM ET</span></div>
      <div class="ev-row"><span class="ev-key">RSVP:</span><span><span class="rsvp-badge rsvp-confirmed">✅ Confirmed</span></span></div>
      <div class="ev-row"><span class="ev-key">Location:</span><span>Google Meet — <a href="https://calendly.com/events/1b967fc3-00ff-4747-9cb9-0d7247562a73/google_meet">Join via Calendly link</a></span></div>
      <div class="ev-row"><span class="ev-key">Attendees:</span><span>Rita Ramakrishnan (rita@iksana.com)</span></div>
      <div class="ev-row"><span class="ev-key">Prep:</span><span>This is an existing coaching/consulting session with Rita. Prepare talking points, any updates from your job search this week, and agenda items you want to cover.</span></div>
    </div>

    <div class="cal-event needsAction">
      <h4>HR Networking &amp; Job Search: Open Office Hours — Zoom 2</h4>
      <div class="ev-row"><span class="ev-key">Time:</span><span>12:00 PM – 1:00 PM ET</span></div>
      <div class="ev-row"><span class="ev-key">RSVP:</span><span><span class="rsvp-badge rsvp-needsAction">⚠️ Needs Action</span></span></div>
      <div class="ev-row"><span class="ev-key">Location:</span><span><a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1">Zoom Link</a></span></div>
      <div class="ev-row"><span class="ev-key">Attendees:</span><span>170+ HR professionals (same group as Wednesday)</span></div>
      <div class="ev-row"><span class="ev-key">Prep:</span><span>Open discussion format — no AI recording tools allowed per host. Come with specific job search questions or challenges to discuss.</span></div>
      <div class="conflict-warn">⚠️ RSVP REQUIRED — Respond today. Note: coaching call with Rita ends at 10:45am; 75-min gap before this session begins at noon.</div>
    </div>
  </div>

  <!-- FRIDAY-SUNDAY -->
  <div class="cal-day">
    <div class="cal-day-header">Friday, September 4 – Sunday, September 6, 2026</div>
    <div class="cal-event" style="border-color:#a0aec0; background:#f7f8fa;">
      <h4>No events scheduled</h4>
      <div class="ev-row"><span class="ev-key">Note:</span><span>Weekend is clear. Consider using Friday to follow up on job applications submitted this week.</span></div>
    </div>
  </div>

</div>

<!-- ════════════════════════════════════════════════════════ -->
<!-- SECTION 5: JOB SEARCH & INTERVIEW PIPELINE -->
<!-- ════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">💼</span> Job Search &amp; Interview Pipeline</div>

  <div class="job-row">
    <h4>Regional Head of Human Resources — The Forum Group <span class="fit-high">HIGH FIT</span></h4>
    <div class="jd-row"><span class="jd-key">Source:</span><span>LinkedIn Job Alerts (unread inbox, Aug 31, 5:05am)</span></div>
    <div class="jd-row"><span class="jd-key">Salary:</span><span>$220,000 – $250,000/year</span></div>
    <div class="jd-row"><span class="jd-key">Additional roles:</span><span>2 more in same alert</span></div>
    <div class="jd-row"><span class="jd-key">Action:</span><span>Open LinkedIn alert → review all 3 roles → apply to Forum Group role today</span></div>
  </div>

  <div class="job-row">
    <h4>IPC Systems — Viewed Your Application <span class="fit-high">HIGH FIT</span></h4>
    <div class="jd-row"><span class="jd-key">Source:</span><span>LinkedIn (unread inbox, Aug 31, 10:52am)</span></div>
    <div class="jd-row"><span class="jd-key">Signal:</span><span>IPC Systems actively viewed your LinkedIn application — strong signal of interest</span></div>
    <div class="jd-row"><span class="jd-key">Action:</span><span>Research IPC Systems now. Prepare for potential outreach. Consider a LinkedIn connection request to their HR/TA team.</span></div>
  </div>

  <div class="job-row">
    <h4>Sr. Manager, Global People Operations — Tenstorrent (+ 39 more) <span class="fit-high">HIGH FIT</span></h4>
    <div class="jd-row"><span class="jd-key">Source:</span><span>LinkedIn Job Alerts (unread inbox, Aug 31, 7:05am)</span></div>
    <div class="jd-row"><span class="jd-key">Highlight:</span><span>Tenstorrent is a leading AI chip company — high-growth, senior HR role</span></div>
    <div class="jd-row"><span class="jd-key">Additional roles:</span><span>39 more in this batch — prioritize reviewing top 5</span></div>
    <div class="jd-row"><span class="jd-key">Action:</span><span>Filter alert by salary/title match; apply to Tenstorrent and at least 2 others this week</span></div>
  </div>

  <div class="job-row">
    <h4>Senior People Business Partner, Product &amp; Marketing — GitLab (+ 36 more) <span class="fit-high">HIGH FIT</span> <span class="tag tag-rescued">✅ Rescued from Trash</span></h4>
    <div class="jd-row"><span class="jd-key">Source:</span><span>LinkedIn Job Alerts (rescued from trash — protected sender)</span></div>
    <div class="jd-row"><span class="jd-key">Highlight:</span><span>GitLab is a major tech company; SPBP Product &amp; Marketing is a strong match for senior HR candidates</span></div>
    <div class="jd-row"><span class="jd-key">Action:</span><span>Review GitLab role + 36 additional alerts. Apply to top matches.</span></div>
  </div>

  <div class="job-row">
    <h4>HR Business Advisor, Executive Director — JPMorganChase (+ 8 more) <span class="fit-high">HIGH FIT</span></h4>
    <div class="jd-row"><span class="jd-key">Source:</span><span>LinkedIn Job Alerts (read, not in inbox, not trashed — Aug 31, 3:05am)</span></div>
    <div class="jd-row"><span class="jd-key">Salary:</span><span>$152,000 – $260,000/year</span></div>
    <div class="jd-row"><span class="jd-key">Action:</span><span>Review JPMorganChase HRBP Executive Director role — salary ceiling of $260K is top-of-market</span></div>
  </div>

  <div class="job-row">
    <h4>Head of People – U.S. — Elliptic (+ 6 more) <span class="fit-med">MEDIUM FIT</span></h4>
    <div class="jd-row"><span class="jd-key">Source:</span><span>LinkedIn Job Alerts (read, not in inbox — Aug 31, 1:05am)</span></div>
    <div class="jd-row"><span class="jd-key">Highlight:</span><span>Elliptic is a crypto compliance leader — niche but growing space</span></div>
    <div class="jd-row"><span class="jd-key">Action:</span><span>Review if crypto/fintech aligns with your target sector</span></div>
  </div>

  <div class="job-row">
    <h4>Director of Human Resources — Managed Resources (Remote, + 8 more) <span class="fit-med">MEDIUM FIT</span></h4>
    <div class="jd-row"><span class="jd-key">Source:</span><span>Glassdoor Jobs (trashed, Aug 31, 1:02am)</span></div>
    <div class="jd-row"><span class="jd-key">Highlight:</span><span>Remote-friendly; Optiv also hiring in this batch</span></div>
    <div class="jd-row"><span class="jd-key">Action:</span><span>Retrieve from trash if interested; check Glassdoor directly for full listing</span></div>
  </div>

  <div class="job-row">
    <h4>Shubbhi Chaturvedi — LinkedIn Connection Request <span class="fit-med">MEDIUM FIT</span></h4>
    <div class="jd-row"><span class="jd-key">Source:</span><span>LinkedIn (unread inbox, Aug 31, 9:05am)</span></div>
    <div class="jd-row"><span class="jd-key">Title:</span><span>Client Partner CDS from Writer (AI writing company)</span></div>
    <div class="jd-row"><span class="jd-key">Action:</span><span>Accept or review profile — Writer is an enterprise AI company, connection may be valuable for your network</span></div>
  </div>

  <div class="job-row">
    <h4>HR Networking &amp; Job Search Group — Peer Networking <span class="fit-med">MEDIUM FIT</span></h4>
    <div class="jd-row"><span class="jd-key">Source:</span><span>Google Calendar (Wed Sept 2 + Thu Sept 3)</span></div>
    <div class="jd-row"><span class="jd-key">Highlight:</span><span>170+ HR professionals, active job search community. Two sessions this week.</span></div>
    <div class="jd-row"><span class="jd-key">Action:</span><span>RSVP both events today. Prepare your search update and targeted questions.</span></div>
  </div>

  <div class="job-row" style="border-color:#a0aec0;">
    <h4>(Remote) HR Consultant / HR Expert — Cinter (+ 11 more) <span class="fit-low">LOW FIT</span></h4>
    <div class="jd-row"><span class="jd-key">Source:</span><span>Glassdoor Jobs (trashed, Aug 30)</span></div>
    <div class="jd-row"><span class="jd-key">Action:</span><span>Review if interested in consulting roles; otherwise safe to ignore</span></div>
  </div>

</div>

<!-- ════════════════════════════════════════════════════════ -->
<!-- SECTION 6: FULL EMAIL REVIEW BY CATEGORY -->
<!-- ════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">📧</span> Full Email Review by Category</div>

  <!-- SECURITY / RISK -->
  <div class="cat-block red">
    <h4>🔴 Security / Risk — 9 emails</h4>
    <div class="cb-row"><span class="cb-key">Emails:</span><span>Size.Does.Matter (spam), TrimRX GLP-1 (auto-trashed phish), Honey-Trick (spam/explicit), MEDVi GLP-1 (auto-trashed phish), Casino Yabby (scam), ManForceX (explicit/scam), CashApp spoof / Raging Bull Casino (auto-trashed phish), Cloud.Storage lockout (auto-trashed phish), COPD Reversal (trashed)</span></div>
    <div class="cb-row"><span class="cb-key">Important senders:</span><span>All spoofed/random domains targeting melissaw212@gmail.com</span></div>
    <div class="cb-row"><span class="cb-key">Auto-Trashed (5):</span><span>TrimRX GLP-1 — fake weight loss offer / data harvest; Honey-Trick — explicit spam; MEDVi GLP-1 — fake promo / data harvest; CashApp / Raging Bull Casino — spoofed payment scam with template injection artifacts; Cloud.Storage — fake account-lock phishing threat</span></div>
    <div class="cb-row"><span class="cb-key">Action:</span><span>Manually trash: Casino Yabby, ManForceX, Size.Does.Matter. COPD Reversal is already in trash. Consider reporting to Gmail as phishing. Set Gmail filters for *.us random-domain patterns.</span></div>
    <div class="phish-warn">⚠️ Your username "melissaw212" is being actively scraped and used in targeted spam campaigns. Do not click any links in these emails.</div>
  </div>

  <!-- JOB SEARCH -->
  <div class="cat-block green">
    <h4>🟢 Job Search — 8 emails</h4>
    <div class="cb-row"><span class="cb-key">Emails:</span><span>LinkedIn: IPC Systems viewed application; LinkedIn Job Alerts (x4: Tenstorrent+39, Forum Group+2, JPMorganChase+8, GitLab+36 rescued, Elliptic+6, Head of People); Glassdoor: Director of HR Managed Resources+8, Glassdoor Community Manager FirstService+7, Glassdoor HR Consultant Cinter+11</span></div>
    <div class="cb-row"><span class="cb-key">Highlights:</span><span>IPC Systems viewed your application (strong signal); Forum Group $220K–$250K; JPMorganChase up to $260K; GitLab SPBP rescued from trash</span></div>
    <div class="cb-row"><span class="cb-key">Action:</span><span>Prioritize Forum Group and IPC Systems today. Review Tenstorrent and GitLab batches. Apply to top matches this week.</span></div>
  </div>

  <!-- RECRUITERS / NETWORKING -->
  <div class="cat-block green">
    <h4>🟢 Recruiters / Networking — 1 email</h4>
    <div class="cb-row"><span class="cb-key">Emails:</span><span>Shubbhi Chaturvedi (LinkedIn) — Connection request from Client Partner CDS at Writer</span></div>
    <div class="cb-row"><span class="cb-key">Action:</span><span>Review profile and accept if relevant. Writer is an enterprise AI company — may be worth maintaining in your network.</span></div>
  </div>

  <!-- CALENDAR / EVENTS -->
  <div class="cat-block blue">
    <h4>🔵 Calendar / Events — 1 email</h4>
    <div class="cb-row"><span class="cb-key">Emails:</span><span>Otter.ai Insights — "Your upcoming meetings" (trashed)</span></div>
    <div class="cb-row"><span class="cb-key">Action:</span><span>Already trashed. Otter.ai appears to be a tool in use — upcoming meeting prep covered by calendar section above. Consider unsubscribing from Otter.ai digest if redundant.</span></div>
  </div>

  <!-- MEDICAL / HEALTH -->
  <div class="cat-block red">
    <h4>🔴 Medical / Health (Spam) — 3 emails</h4>
    <div class="cb-row"><span class="cb-key">Emails:</span><span>TrimRX GLP-1 (auto-trashed), MEDVi GLP-1 (auto-trashed), COPD Reversal (trashed)</span></div>
    <div class="cb-row"><span class="cb-key">Action:</span><span>All three are spam/phishing disguised as health offers. Two auto-trashed; COPD Reversal already in trash. No action needed — do not engage.</span></div>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="cat-block yellow">
    <h4>🟡 Financial / Billing (Scam) — 2 emails</h4>
    <div class="cb-row"><span class="cb-key">Emails:</span><span>Casino Yabby (fake NGR bonus / payment scam); CashApp / Raging Bull Casino spoof (auto-trashed — fake payment notification)</span></div>
    <div class="cb-row"><span class="cb-key">Action:</span><span>Both are scams. CashApp spoof auto-trashed. Casino Yabby should be manually trashed. Do not click. No real payments were made to you.</span></div>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="cat-block purple">
    <h4>🟣 Professional Development — 3 emails</h4>
    <div class="cb-row"><span class="cb-key">Emails:</span><span>Gemma Bonham-Carter — "THIS is why nobody is buying" (trashed); MCP Market / Graeme — "You've hit your limit" (not in inbox, not trashed); Marc Cleroux / Ten Fold Marc — "I tested 100 Claude Code skills" (inbox)</span></div>
    <div class="cb-row"><span class="cb-key">Action:</span><span>MCP Market and Ten Fold Marc are marketing-focused newsletters — review if relevant to your work, otherwise unsubscribe. Gemma Bonham-Carter already trashed — safe to delete.</span></div>
  </div>

  <!-- PERSONAL -->
  <div class="cat-block blue">
    <h4>🔵 Personal — 6 emails</h4>
    <div class="cb-row"><span class="cb-key">Emails:</span><span>Self-email "Tell Ellie" (inbox — nail appointment reminder); Self-email "claude senses" (inbox — LinkedIn link); OkCupid "Someone likes you" (inbox); Match "Profile view from Kurt" (inbox); Match "Donald likes you" (inbox); eBay / premierusa_0 popcorn purchase message (inbox)</span></div>
    <div class="cb-row"><span class="cb-key">Action:</span><span>"Tell Ellie" — raise at today's midday/wrap-up. "claude senses" — review when convenient. Dating app notifications — personal priority. eBay message — informational, no action needed.</span></div>
