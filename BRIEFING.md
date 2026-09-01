<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa W — September 1, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 12px; padding: 32px 36px 24px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .sub { font-size: 15px; color: #a8c8ff; margin-top: 6px; }
  .header .meta { display: flex; gap: 28px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.1); border-radius: 8px; padding: 8px 16px; font-size: 13px; color: #e0eaff; }
  .header .meta-item span { font-weight: 700; color: #fff; font-size: 18px; display: block; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; padding: 10px 16px; border-radius: 8px 8px 0 0; letter-spacing: 0.3px; display: flex; align-items: center; gap: 8px; }
  .section-body { background: #fff; border-radius: 0 0 10px 10px; padding: 18px; border: 1px solid #e0e4ea; border-top: none; }

  /* COLOR THEMES */
  .theme-red .section-title { background: #c0392b; color: #fff; }
  .theme-red { border: 1px solid #e74c3c; border-radius: 10px; }
  .theme-yellow .section-title { background: #e67e22; color: #fff; }
  .theme-yellow { border: 1px solid #f39c12; border-radius: 10px; }
  .theme-blue .section-title { background: #2471a3; color: #fff; }
  .theme-blue { border: 1px solid #3498db; border-radius: 10px; }
  .theme-green .section-title { background: #1e8449; color: #fff; }
  .theme-green { border: 1px solid #27ae60; border-radius: 10px; }
  .theme-purple .section-title { background: #7d3c98; color: #fff; }
  .theme-purple { border: 1px solid #9b59b6; border-radius: 10px; }
  .theme-gray .section-title { background: #5d6d7e; color: #fff; }
  .theme-gray { border: 1px solid #99a3a4; border-radius: 10px; }
  .theme-navy .section-title { background: #1a1a2e; color: #fff; }
  .theme-navy { border: 1px solid #2c3e50; border-radius: 10px; }
  .theme-teal .section-title { background: #0e7490; color: #fff; }
  .theme-teal { border: 1px solid #0891b2; border-radius: 10px; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #f4f6f9; color: #444; font-weight: 700; padding: 9px 12px; text-align: left; border-bottom: 2px solid #dde1e7; }
  td { padding: 8px 12px; border-bottom: 1px solid #eaedf0; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f9fafc; }

  /* BADGES */
  .badge { display: inline-block; padding: 2px 9px; border-radius: 12px; font-size: 11px; font-weight: 700; letter-spacing: 0.3px; }
  .badge-red { background: #fdecea; color: #c0392b; border: 1px solid #e74c3c; }
  .badge-yellow { background: #fef9e7; color: #b7770d; border: 1px solid #f39c12; }
  .badge-green { background: #eafaf1; color: #1a7a3c; border: 1px solid #27ae60; }
  .badge-blue { background: #ebf5fb; color: #1a5276; border: 1px solid #3498db; }
  .badge-purple { background: #f5eef8; color: #6c3483; border: 1px solid #9b59b6; }
  .badge-gray { background: #f2f3f4; color: #5d6d7e; border: 1px solid #aab; }
  .badge-orange { background: #fef5e7; color: #a04000; border: 1px solid #e67e22; }
  .badge-teal { background: #e0f7fa; color: #006064; border: 1px solid #0891b2; }

  /* CARDS */
  .card { background: #fff; border-radius: 10px; padding: 16px 20px; margin-bottom: 14px; border-left: 5px solid #ccc; box-shadow: 0 1px 4px rgba(0,0,0,0.06); }
  .card-red { border-left-color: #e74c3c; }
  .card-yellow { border-left-color: #f39c12; }
  .card-blue { border-left-color: #3498db; }
  .card-green { border-left-color: #27ae60; }
  .card-purple { border-left-color: #9b59b6; }
  .card-gray { border-left-color: #99a3a4; }
  .card-teal { border-left-color: #0891b2; }
  .card h3 { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
  .card .card-meta { font-size: 12px; color: #777; margin-bottom: 6px; }
  .card .card-label { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px; }
  .card p { font-size: 13px; color: #444; }
  .card .next-step { margin-top: 8px; background: #f4f6f9; border-radius: 6px; padding: 7px 12px; font-size: 12px; color: #333; }
  .card .next-step strong { color: #1a1a2e; }

  /* EXEC SUMMARY */
  .exec-bullets { list-style: none; padding: 0; }
  .exec-bullets li { padding: 10px 14px; margin-bottom: 8px; border-radius: 8px; font-size: 14px; display: flex; gap: 10px; align-items: flex-start; }
  .exec-bullets li .icon { font-size: 20px; flex-shrink: 0; }
  .exec-bullets li.risk { background: #fdecea; border-left: 4px solid #e74c3c; }
  .exec-bullets li.opp { background: #eafaf1; border-left: 4px solid #27ae60; }
  .exec-bullets li.cal { background: #ebf5fb; border-left: 4px solid #3498db; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { background: #1a1a2e; color: #fff; padding: 7px 14px; border-radius: 7px; font-weight: 700; font-size: 13px; margin-bottom: 8px; }
  .cal-event { background: #f9fafc; border: 1px solid #dde3ec; border-radius: 8px; padding: 12px 16px; margin-bottom: 8px; }
  .cal-event .time { font-weight: 700; color: #2471a3; font-size: 13px; }
  .cal-event .title { font-weight: 700; font-size: 14px; margin: 2px 0; }
  .cal-event .detail { font-size: 12px; color: #666; margin-top: 3px; }
  .cal-event .rsvp-accepted { color: #1e8449; font-weight: 700; }
  .cal-event .rsvp-declined { color: #c0392b; font-weight: 700; }
  .cal-event .rsvp-pending { color: #e67e22; font-weight: 700; }
  .cal-event .rsvp-confirmed { color: #1e8449; font-weight: 700; }

  /* PRIORITIES */
  .priority-item { display: flex; gap: 14px; align-items: flex-start; padding: 14px 18px; margin-bottom: 12px; background: #fff; border-radius: 10px; border: 1px solid #e0e4ea; box-shadow: 0 1px 4px rgba(0,0,0,0.05); }
  .priority-num { background: #1a1a2e; color: #fff; width: 34px; height: 34px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 16px; flex-shrink: 0; }
  .priority-content h3 { font-size: 15px; font-weight: 700; }
  .priority-content p { font-size: 13px; color: #555; margin-top: 3px; }

  /* DASHBOARD GRID */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-card { background: #fff; border-radius: 10px; padding: 14px 16px; border: 1px solid #e0e4ea; box-shadow: 0 1px 4px rgba(0,0,0,0.05); }
  .dash-card .dc-title { font-size: 11px; font-weight: 700; text-transform: uppercase; color: #888; letter-spacing: 0.5px; margin-bottom: 6px; }
  .dash-card .dc-value { font-size: 26px; font-weight: 800; color: #1a1a2e; }
  .dash-card .dc-sub { font-size: 12px; color: #666; margin-top: 4px; }
  .dash-card.dc-red { border-top: 4px solid #e74c3c; }
  .dash-card.dc-yellow { border-top: 4px solid #f39c12; }
  .dash-card.dc-green { border-top: 4px solid #27ae60; }
  .dash-card.dc-blue { border-top: 4px solid #3498db; }
  .dash-card.dc-purple { border-top: 4px solid #9b59b6; }
  .dash-card.dc-gray { border-top: 4px solid #99a3a4; }

  /* TRIAGE TABLE */
  .triage-status { font-size: 13px; white-space: nowrap; }
  .triage-from { font-size: 12px; color: #444; }
  .triage-subject { font-size: 13px; font-weight: 600; }
  .triage-summary { font-size: 12px; color: #666; }
  .row-inbox { background: #f0f7ff; }
  .row-trash { background: #f9f9f9; }
  .row-auto { background: #fff5f5; }

  /* MISC */
  .pill { display: inline-block; padding: 1px 8px; border-radius: 10px; font-size: 11px; font-weight: 600; margin-right: 4px; }
  .pill-high { background: #fdecea; color: #c0392b; }
  .pill-medium { background: #fef9e7; color: #b7770d; }
  .pill-low { background: #f2f3f4; color: #5d6d7e; }
  .divider { border: none; border-top: 1px solid #eaecef; margin: 14px 0; }
  .note { font-size: 12px; color: #888; font-style: italic; margin-top: 6px; }
  .warning { background: #fef9e7; border: 1px solid #f39c12; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #7d4e00; margin-bottom: 10px; }
  .danger { background: #fdecea; border: 1px solid #e74c3c; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #7b1a1a; margin-bottom: 10px; }
  .info { background: #ebf5fb; border: 1px solid #3498db; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #1a4a6b; margin-bottom: 10px; }
  a { color: #2471a3; text-decoration: none; }
  a:hover { text-decoration: underline; }
  .group-row td { background: #f4f6f9; font-weight: 700; }
  .indent td { padding-left: 28px; }
  .footer { text-align: center; color: #aaa; font-size: 12px; padding: 18px 0 8px; }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════════ HEADER ═══ -->
<div class="header">
  <h1>📋 Executive Briefing — Melissa W.</h1>
  <div class="sub">Prepared by your Executive Chief of Staff</div>
  <div class="meta">
    <div class="meta-item"><span>Tuesday</span>September 1, 2026</div>
    <div class="meta-item"><span>50</span>Emails Reviewed</div>
    <div class="meta-item"><span>6</span>Calendar Events</div>
    <div class="meta-item"><span>6</span>Auto-Trashed (Phishing/Newsletter)</div>
    <div class="meta-item"><span>3</span>Action Required Today</div>
  </div>
</div>

<!-- ═══════════════════════════════════ SECTION 0: EMAIL TRIAGE QUICK LIST ═══ -->
<div class="section theme-navy">
  <div class="section-title">⚡ Email Triage Quick List</div>
  <div class="section-body" style="padding:0;">
    <table>
      <thead>
        <tr>
          <th style="width:120px;">Status</th>
          <th style="width:200px;">From</th>
          <th style="width:280px;">Subject</th>
          <th>Summary</th>
        </tr>
      </thead>
      <tbody>
        <!-- INBOX EMAILS (individual rows) -->
        <tr class="row-inbox">
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">Notify NYC</td>
          <td class="triage-subject">Silver Alert — Sabato Noto</td>
          <td class="triage-summary">81-year-old male last seen near Amsterdam Ave. Community alert — FYI only.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">Elisa Russo via LinkedIn</td>
          <td class="triage-subject">Job Opportunity — Vice Chancellor for Human Resources</td>
          <td class="triage-summary">Recruiter outreach via LinkedIn InMail for VP/VC-level HR role. Review &amp; respond.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">Match</td>
          <td class="triage-subject">You've had a profile view from Stephen</td>
          <td class="triage-summary">Stephen, 63, New City NY viewed your Match profile.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">Bank of America</td>
          <td class="triage-subject">Direct deposit credited — $760.38 (NYS DOL UI)</td>
          <td class="triage-summary">Unemployment insurance deposit received today. Account ending 7471.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">Inclusively</td>
          <td class="triage-subject">Check out these recommended jobs for you!</td>
          <td class="triage-summary">Platform job recommendations based on your profile. Review when convenient.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">Indeed</td>
          <td class="triage-subject">SVP, Chief People Officer @ Community Reinvestment Fund USA</td>
          <td class="triage-summary">$215K–$253K. Strong match flagged for your HR leadership background.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">LinkedIn Job Alerts</td>
          <td class="triage-subject">Head of HR, Americas Distribution at Invesco + 1 more</td>
          <td class="triage-summary">Senior HR alert from LinkedIn. Invesco lead role. Review &amp; apply if interested.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">Amazon.com</td>
          <td class="triage-subject">Shipped: 5 Candy, Skincare, and other items</td>
          <td class="triage-summary">Order shipped. Track delivery as needed.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">Amazon.com</td>
          <td class="triage-subject">Promotional credit from your recent Amazon order</td>
          <td class="triage-summary">Promo credit issued for Order 114-3698716-8192259. Note for future use.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">Apple</td>
          <td class="triage-subject">Your receipt from Apple.</td>
          <td class="triage-summary">Purchase: "Im Blunt Cause God Rolled Me That Way" + other items. Verify if authorized.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status"><span class="badge badge-yellow">📥 INBOX ⚠️</span></td>
          <td class="triage-from">Bank of America</td>
          <td class="triage-subject">Online transfer over the limit you set</td>
          <td class="triage-summary">$300+ transfer exceeded alert threshold. Account 7471. Review immediately.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">Ulta Beauty</td>
          <td class="triage-subject">Your package arrives soon! Order #M217756814</td>
          <td class="triage-summary">Ulta order arriving soon. Placed Aug 28.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">Melissa W (self)</td>
          <td class="triage-subject">GitHub Profile Masterclass — @hey__jay93</td>
          <td class="triage-summary">Self-sent link to GitHub profile guide resource. Review when ready.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">LinkedIn Job Alerts</td>
          <td class="triage-subject">Vice President Human Resources at DSD Recruitment + 7 more</td>
          <td class="triage-summary">VP HR role alert plus 7 additional matches. Review batch.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">LinkedIn Job Alerts</td>
          <td class="triage-subject">People Business Partner Lead – APJ at ClickHouse + 9 more</td>
          <td class="triage-summary">10 HR job matches. Review for relevant fits.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">LinkedIn Job Alerts</td>
          <td class="triage-subject">People Business Partner Lead – APJ at ClickHouse + 35 more</td>
          <td class="triage-summary">35+ HR job matches digest. Large batch — review top picks.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
          <td class="triage-from">Adam Broda via LinkedIn</td>
          <td class="triage-subject">Adam just messaged you</td>
          <td class="triage-summary">1 unread LinkedIn message awaiting response. Reply promptly.</td>
        </tr>
        <!-- SUMMARY ROWS FOR TRASH -->
        <tr class="row-auto">
          <td class="triage-status"><span class="badge badge-red">🗑 AUTO-TRASHED</span></td>
          <td colspan="3" class="triage-summary"><strong>6 emails auto-trashed (phishing × 5 + newsletter × 1)</strong> — See Trash Review section for details. No action needed.</td>
        </tr>
        <tr class="row-trash">
          <td class="triage-status"><span class="badge badge-gray">🗂 TRASH</span></td>
          <td colspan="3" class="triage-summary"><strong>17 emails manually in Trash</strong> (newsletters, retail promos, low-value digests) — See Trash Review section for details.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════ SECTION 2: EXECUTIVE SUMMARY ═══ -->
<div class="section theme-navy">
  <div class="section-title">🎯 Executive Summary</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li class="risk">
        <span class="icon">🔴</span>
        <div><strong>Biggest Risk:</strong> Bank of America flagged an online transfer exceeding your self-set alert threshold on account ending 7471 (transferred ~$300). Combined with today's UI deposit of $760.38, review your account activity now to confirm the transfer was authorized and no unauthorized access occurred. Additionally, 5 phishing emails were auto-trashed overnight targeting you with fake payment notifications and cloud storage scams.</div>
      </li>
      <li class="opp">
        <span class="icon">🟢</span>
        <div><strong>Biggest Opportunity:</strong> Strong executive-level job search activity today — Indeed flags a CPO role at Community Reinvestment Fund ($215K–$253K), LinkedIn surfaces Head of HR at Invesco + 40+ additional HR leadership roles, and recruiter Elisa Russo reached out via LinkedIn InMail for a Vice Chancellor of Human Resources position. Review and prioritize applications today.</div>
      </li>
      <li class="cal">
        <span class="icon">🔵</span>
        <div><strong>Biggest Calendar Item:</strong> Tomorrow (Wed Sep 2) you have the HR Networking &amp; Job Search Group Zoom at 12:00 PM ET (RSVP pending — action needed). Thursday Sep 3 includes your confirmed 1:1 coaching session with Rita Ramakrishnan at 10:00 AM via Google Meet, plus the Open Office Hours Zoom at 12:00 PM (RSVP pending). The Executive Roundtable on Sep 3 at 9:00 AM was declined. State Farm bill due Sep 7.</div>
      </li>
    </ul>
  </div>
</div>

<!-- ═══════════════════════════════════ SECTION 3: ACTION REQUIRED ═══ -->
<div class="section theme-yellow">
  <div class="section-title">⚠️ Action Required</div>
  <div class="section-body">

    <div class="card card-red">
      <div class="card-label" style="color:#c0392b;">🔴 URGENT — Financial Security</div>
      <h3>Bank of America: Online Transfer Exceeded Your Alert Limit</h3>
      <div class="card-meta">From: Bank of America &lt;onlinebanking@ealerts.bankofamerica.com&gt; · Mon Aug 31, 2026 · Account ending 7471</div>
      <p>An online transfer from your account exceeded the threshold you set. Amount appears to be ~$300. This alert arrived shortly after midnight. Verify this transfer was authorized and no unauthorized account activity occurred.</p>
      <div class="next-step"><strong>Next Step:</strong> Log in to Bank of America online banking or call 1-800-432-1000 to review the transfer. If unauthorized, request immediate freeze and fraud investigation. <strong>Due: TODAY</strong></div>
    </div>

    <div class="card card-yellow">
      <div class="card-label" style="color:#b7770d;">🟡 RSVP NEEDED — Calendar</div>
      <h3>HR Networking &amp; Job Search Group — Zoom (Session 2) · Sep 2 @ 12:00 PM</h3>
      <div class="card-meta">Calendar Event · Tomorrow · Status: Needs Action (no RSVP submitted)</div>
      <p>Large HR networking group Zoom session tomorrow. 150+ attendees from your professional network. Your RSVP is pending. You have a parallel "Network" block confirmed at the same time — confirm which one you're attending.</p>
      <div class="next-step"><strong>Next Step:</strong> Accept or decline the HR Networking Zoom invite. Zoom link: <a href="https://us06web.zoom.us/j/81954171722" target="_blank">Join Zoom</a>. <strong>Due: Today (before tomorrow noon)</strong></div>
    </div>

    <div class="card card-green">
      <div class="card-label" style="color:#1e8449;">🟢 OPPORTUNITY — Job Search</div>
      <h3>Recruiter Outreach: Vice Chancellor for Human Resources (LinkedIn InMail)</h3>
      <div class="card-meta">From: Elisa Russo, MBA HRM, SHRM-CP via LinkedIn · Tue Sep 1, 2026 · 9:05 AM</div>
      <p>A lead recruiter contacted you directly on LinkedIn for a Vice Chancellor for Human Resources position. This is a C-suite adjacent role. The message is in your inbox — review and respond promptly while the lead is fresh.</p>
      <div class="next-step"><strong>Next Step:</strong> Open LinkedIn InMail from Elisa Russo. Review role details, compensation, and org. Reply within 24 hours expressing interest or requesting more details. <strong>Due: Today / Tomorrow</strong></div>
    </div>

    <div class="card card-yellow">
      <div class="card-label" style="color:#b7770d;">🟡 RSVP NEEDED — Calendar</div>
      <h3>HR Networking Open Office Hours — Zoom · Sep 3 @ 12:00 PM</h3>
      <div class="card-meta">Calendar Event · Thursday · Status: Needs Action (no RSVP submitted)</div>
      <p>Second networking RSVP pending for Thursday's Open Office Hours session. Note: organizer requests no AI notetaking tools active during this session.</p>
      <div class="next-step"><strong>Next Step:</strong> Accept or decline by Wednesday. Zoom link: <a href="https://us06web.zoom.us/j/85945371140" target="_blank">Join Zoom</a>.</div>
    </div>

    <div class="card card-yellow">
      <div class="card-label" style="color:#b7770d;">🟡 BILLING REMINDER</div>
      <h3>State Farm Bill Due September 7</h3>
      <div class="card-meta">Calendar Event · All-Day · Sep 7, 2026</div>
      <p>Calendar reminder set for State Farm bill payment. Ensure payment is scheduled or autopay is active to avoid lapse in coverage.</p>
      <div class="next-step"><strong>Next Step:</strong> Confirm payment is scheduled or log in to State Farm to pay. <strong>Due: Sep 7</strong></div>
    </div>

    <div class="card card-blue">
      <div class="card-label" style="color:#1a5276;">🔵 PREP NEEDED — Coaching</div>
      <h3>1:1 with Rita Ramakrishnan — 45-Min Coaching Session · Sep 3 @ 10:00 AM</h3>
      <div class="card-meta">Calendar Event · Thursday · Status: Accepted · Google Meet</div>
      <p>Confirmed coaching/consulting call with Rita Ramakrishnan (rita@iksana.com). Session is 45 minutes via Google Meet. Prepare agenda, updates, and any questions in advance.</p>
      <div class="next-step"><strong>Next Step:</strong> Prepare 2–3 agenda items for Rita. Access meeting via Calendly Google Meet link. <strong>Due: Wednesday EOD</strong></div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════ SECTION 4: FULL 7-DAY CALENDAR ═══ -->
<div class="section theme-blue">
  <div class="section-title">📅 Full 7-Day Calendar (Sep 1 – Sep 7, 2026)</div>
  <div class="section-body">

    <div class="cal-day">
      <div class="cal-day-header">Tuesday, September 1, 2026 — TODAY</div>
      <div class="cal-event" style="border-left:4px solid #99a3a4;">
        <div class="time">All Day</div>
        <div class="title" style="color:#666;">No calendar events today</div>
        <div class="detail">Use today for job search follow-up, bank review, and RSVP actions.</div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">Wednesday, September 2, 2026</div>
      <div class="cal-event" style="border-left:4px solid #e67e22;">
        <div class="time">12:00 PM – 1:30 PM ET</div>
        <div class="title">HR Networking &amp; Job Search Group — Zoom (Session 2)</div>
        <span class="rsvp-pending">⚠️ RSVP Pending — Needs Action</span>
        <div class="detail">📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a> · 150+ attendees · Large HR professional network group</div>
        <div class="detail">📝 <strong>Prep:</strong> Review HR Networking Team Guidelines before joining. Prepare your elevator pitch and any job search updates to share.</div>
        <div class="detail" style="color:#e67e22;">⚠️ <strong>Conflict:</strong> "Network" block is also confirmed 12:00–1:30 PM same day. Confirm which event takes priority.</div>
      </div>
      <div class="cal-event" style="border-left:4px solid #27ae60;">
        <div class="time">12:00 PM – 1:30 PM ET</div>
        <div class="title">Network (Personal Block)</div>
        <span class="rsvp-confirmed">✅ Confirmed (no attendees listed)</span>
        <div class="detail">📍 No location set · Personal networking placeholder block</div>
        <div class="detail" style="color:#e67e22;">⚠️ <strong>Conflict:</strong> Overlaps exactly with HR Networking Zoom above. Resolve which to keep.</div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">Thursday, September 3, 2026</div>
      <div class="cal-event" style="border-left:4px solid #e74c3c;">
        <div class="time">9:00 AM – 10:30 AM ET</div>
        <div class="title">Executive Roundtable (hosted by John Madigan)</div>
        <span class="rsvp-declined">❌ DECLINED</span>
        <div class="detail">📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> · Meeting ID: 207 786 667 · Password: 205454</div>
        <div class="detail">📝 Already declined. No action needed unless you want to reverse.</div>
      </div>
      <div class="cal-event" style="border-left:4px solid #27ae60;">
        <div class="time">10:00 AM – 10:45 AM ET</div>
        <div class="title">1:1 Coaching — Melissa Weiss &amp; Rita Ramakrishnan</div>
        <span class="rsvp-accepted">✅ ACCEPTED</span>
        <div class="detail">📍 Google Meet · <a href="https://calendly.com/events/1b967fc3-00ff-4747-9cb9-0d7247562a73/google_meet" target="_blank">Join via Calendly</a> · rita@iksana.com</div>
        <div class="detail">📝 <strong>Prep:</strong> Prepare 2–3 key discussion topics. This is your confirmed coaching/consulting session — arrive with agenda items ready.</div>
      </div>
      <div class="cal-event" style="border-left:4px solid #e67e22;">
        <div class="time">12:00 PM – 1:00 PM ET</div>
        <div class="title">HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
        <span class="rsvp-pending">⚠️ RSVP Pending — Needs Action</span>
        <div class="detail">📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a> · 150+ attendees</div>
        <div class="detail">📝 <strong>Note:</strong> Organizer requests NO AI notetaking tools. Open discussion format. No recording.</div>
        <div class="detail" style="color:#e67e22;">⚠️ <strong>Note:</strong> Follows immediately after Rita coaching call. Build in a 15-min buffer.</div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">Friday, September 4, 2026</div>
      <div class="cal-event" style="border-left:4px solid #99a3a4;">
        <div class="time">All Day</div>
        <div class="title" style="color:#666;">No events scheduled</div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">Saturday, September 5, 2026</div>
      <div class="cal-event" style="border-left:4px solid #99a3a4;">
        <div class="time">All Day</div>
        <div class="title" style="color:#666;">No events scheduled</div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">Sunday, September 6, 2026</div>
      <div class="cal-event" style="border-left:4px solid #99a3a4;">
        <div class="time">All Day</div>
        <div class="title" style="color:#666;">No events scheduled</div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">Monday, September 7, 2026 — Labor Day</div>
      <div class="cal-event" style="border-left:4px solid #f39c12;">
        <div class="time">All Day</div>
        <div class="title">💳 State Farm Bill Due</div>
        <span class="rsvp-confirmed">✅ Confirmed (personal reminder)</span>
        <div class="detail">📍 No location · Insurance payment deadline</div>
        <div class="detail">📝 <strong>Action:</strong> Ensure State Farm payment is processed before or on this date. Verify autopay or pay manually.</div>
      </div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════ SECTION 5: JOB SEARCH PIPELINE ═══ -->
<div class="section theme-green">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">

    <div class="info">Active job search signals across LinkedIn, Indeed, Glassdoor, Inclusively, and direct recruiter outreach. Strong CPO/VP HR level opportunities in today's batch.</div>

    <table>
      <thead>
        <tr>
          <th>Fit</th>
          <th>Role / Company</th>
          <th>Source</th>
          <th>Compensation</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="pill pill-high">HIGH</span></td>
          <td><strong>SVP, Chief People Officer</strong><br>Community Reinvestment Fund, USA</td>
          <td>Indeed</td>
          <td>$215,000 – $253,000/yr</td>
          <td>Review &amp; Apply Today</td>
        </tr>
        <tr>
          <td><span class="pill pill-high">HIGH</span></td>
          <td><strong>Vice Chancellor for Human Resources</strong><br>(via Elisa Russo, Lead Recruiter)</td>
          <td>LinkedIn InMail</td>
          <td>Not disclosed</td>
          <td>Reply to Elisa TODAY</td>
        </tr>
        <tr>
          <td><span class="pill pill-high">HIGH</span></td>
          <td><strong>Head of HR, Americas Distribution</strong><br>Invesco</td>
          <td>LinkedIn Job Alert</td>
          <td>Not disclosed</td>
          <td>Review &amp; Apply</td>
        </tr>
        <tr>
          <td><span class="pill pill-high">HIGH</span></td>
          <td><strong>Vice President, Human Resources</strong><br>DSD Recruitment (+7 more)</td>
          <td>LinkedIn Job Alert</td>
          <td>Not disclosed</td>
          <td>Review batch; filter top 3</td>
        </tr>
        <tr>
          <td><span class="pill pill-medium">MED</span></td>
          <td><strong>Sr. Manager, HR Technology</strong><br>Safelite AutoGlass (Remote)</td>
          <td>Glassdoor (Trashed)</td>
          <td>Not disclosed</td>
          <td>Check if interested before deleting</td>
        </tr>
        <tr>
          <td><span class="pill pill-medium">MED</span></td>
          <td><strong>Director of Human Resources</strong><br>Managed Resources (+8 more, US-wide)</td>
          <td>Glassdoor (Trashed)</td>
          <td>Not disclosed</td>
          <td>Review if Director-level is of interest</td>
        </tr>
        <tr>
          <td><span class="pill pill-medium">MED</span></td>
          <td><strong>People Business Partner Lead – APJ</strong><br>ClickHouse (+9 or +35 more)</td>
          <td>LinkedIn Job Alert (×2)</td>
          <td>Not disclosed</td>
          <td>Review; APJ scope may not be a fit — skip if so</td>
        </tr>
        <tr>
          <td><span class="pill pill-medium">MED</span></td>
          <td><strong>Recommended jobs digest</strong><br>Inclusively platform</td>
          <td>Inclusively</td>
          <td>Varies</td>
          <td>Log in and review recommendations</td>
        </tr>
        <tr>
          <td><span class="pill pill-low">LOW</span></td>
          <td><strong>Community Coordinator</strong><br>Van Police Department, NY (+6 more)</td>
          <td>Glassdoor (Trashed)</td>
          <td>Not disclosed</td>
          <td>Likely not a fit — safe to ignore</td>
        </tr>
      </tbody>
    </table>

    <hr class="divider">
    <h3 style="margin-bottom:10px; font-size:14px; color:#1e8449;">🤝 Networking &amp; Recruiter Activity</h3>
    <table>
      <thead>
        <tr><th>Person</th><th>Platform</th><th>Status</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Adam Broda</strong></td>
          <td>LinkedIn</td>
          <td>Sent you a message (unread)</td>
          <td>Open LinkedIn and reply</td>
        </tr>
        <tr>
          <td><strong>Elisa Russo, SHRM-CP</strong></td>
          <td>LinkedIn InMail</td>
          <td>Recruiter outreach (inbox, unread)</td>
          <td>Reply today — high priority</td>
        </tr>
        <tr>
          <td><strong>HR Networking Group (150+ members)</strong></td>
          <td>Zoom / Calendar</td>
          <td>Sep 2 &amp; Sep 3 — RSVP pending</td>
          <td>RSVP to both sessions</td>
        </tr>
      </tbody>
    </table>

  </div>
</div>

<!-- ═══════════════════════════════════ SECTION 6: FULL EMAIL REVIEW BY CATEGORY ═══ -->
<div class="section theme-navy">
  <div class="section-title">📂 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="card card-red">
      <div class="card-label" style="color:#c0392b;">🔴 SECURITY / RISK — 7 Emails</div>
      <h3>Phishing, Scams &amp; Financial Alerts</h3>
      <p><strong>Auto-Trashed Phishing (5 emails — no action needed):</strong></p>
      <table style="margin:8px 0;">
        <thead><tr><th>Sender (spoofed)</th><th>Subject</th><th>Reason</th></tr></thead>
        <tbody>
          <tr><td>melissaw212 (fake)</td><td>You received a direct deposit of $5,500 (Raging Bull Casino)</td><td>Fake casino payment notification — phishing</td></tr>
          <tr><td>'CashApp' (fake)</td><td>You have received $15.99 — Raging Bull Casino</td><td>Fake CashApp payment, broken template variables — phishing</td></tr>
          <tr><td>'melissaw212' (fake)</td><td>You Received a Payment of $3,000.00 USD</td><td>Fake casino deposit notification — credential harvest</td></tr>
          <tr><td>Cloud Storage (fake)</td><td>FINAL NOTICE: Your photos will be deleted tonight</td><td>Fake cloud deletion threat — credential/payment harvest</td></tr>
          <tr><td>Cloud.Storage (fake)</td><td>Your Cloud Account has been locked [Aug 31]</td><td>Fake cloud locked threat — credential/payment harvest</td></tr>
          <tr><td>melissaw212 (fake)</td><td>Your Cloud ID has been locked — photos/videos will be removed</td><td>Fake Cloud ID locked — credential/payment harvest</td></tr>
        </tbody>
      </table>
      <p style="margin-top:8px;"><strong>Real Financial Alert — Action Required:</strong></p>
      <ul style="margin:6px 0 0 16px; font-size:13px;">
        <li><strong>Bank of America:</strong> Online transfer exceeded your self-set limit on account 7471 (inbox, unread). <strong>Review immediately.</strong></li>
      </ul>
      <div class="next-step"><strong>Recommended Action:</strong> Auto-trashed phishing emails require no further action. Log in to Bank of America immediately to review the flagged transfer. If unauthorized, freeze account and report fraud.</div>
    </div>

    <!-- JOB SEARCH -->
    <div class="card card-green">
      <div class="card-label" style="color:#1e8449;">🟢 JOB SEARCH — 9 Emails</div>
      <h3>Alerts, Applications &amp; Recruiter Outreach</h3>
      <table style="margin:8px 0;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th></tr></thead>
        <tbody>
          <tr><td>Indeed</td><td>SVP, Chief People Officer @ Community Reinvestment Fund ($215K–$253K)</td><td><span class="badge badge-green">Inbox — Apply</span></td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>Head of HR, Americas Distribution at Invesco + 1 more</td><td><span class="badge badge-green">Inbox — Review</span></td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>Vice President HR at DSD Recruitment + 7 more</td><td><span class="badge badge-green">Inbox — Review</span></td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>People Business Partner Lead – APJ at ClickHouse + 9 more</td><td><span class="badge badge-green">Inbox — Review</span></td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>People Business Partner Lead – APJ at ClickHouse + 35 more</td><td><span class="badge badge-green">Inbox — Review</span></td></tr>
          <tr><td>Inclusively</td><td>Recommended jobs for melissa weiss</td><td><span class="badge badge-green">Inbox — Review</span></td></tr>
          <tr><td>Glassdoor Jobs</td><td>Community Coordinator at Van Police Dept + 6 more (NY)</td><td><span class="badge badge-gray">Trashed — Low priority</span></td></tr>
          <tr><td>Glassdoor Jobs</td><td>Sr. Manager HR Technology at Safelite + 7 more (Remote)</td><td><span class="badge badge-gray">Trashed — Review if interested</span></td></tr>
          <tr><td>Glassdoor Jobs</td><td>Director of Human Resources at Managed Resources + 8 more</td><td><span class="badge badge-gray">Trashed — Review if interested</span></td></tr>
        </tbody>
      </table>
      <div class="next-step"><strong>Recommended Action:</strong> Prioritize the CPO role at Community Reinvestment Fund and Invesco Head of HR today. Review LinkedIn batch digests for additional fits. Glassdoor alerts in trash can be restored if role levels match your target.</div>
    </div>

    <!-- RECRUITERS / NETWORKING -->
    <div class="card card-green">
      <div class="card-label" style="color:#1e8449;">🟢 RECRUITERS / NETWORKING — 2 Emails</div>
      <h3>Direct Outreach &amp; LinkedIn Messages</h3>
      <table style="margin:8px 0;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th></tr></thead>
        <tbody>
          <tr><td>Elisa Russo, MBA HRM, SHRM-CP (LinkedIn)</td><td>Job Opportunity — Vice Chancellor for Human Resources</td><td><span class="badge badge-green">Inbox — Reply Today</span></td></tr>
          <tr><td>Adam Broda via LinkedIn</td><td>Adam just messaged you</td><td><span class="badge badge-blue">Inbox — Reply Soon</span></td></tr>
        </tbody>
      </table>
      <div class="next-step"><strong>Recommended Action:</strong> Reply to Elisa Russo's InMail today. Check and respond to Adam Broda's message on LinkedIn.</div>
    </div>

    <!-- CALENDAR / EVENTS -->
    <div class="card card-blue">
      <div class="card-label" style="color:#1a5276;">🔵 CALENDAR / EVENTS — 0 Standalone Emails</div>
      <h3>All calendar items are captured in the Calendar section above.</h3>
      <p class="note">Calendar data sourced directly from Google Calendar. No separate calendar-related emails in inbox beyond the LinkedIn InMail (categorized under Recruiters).</p>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="card card-yellow">
      <div class="card-label" style="color:#b7770d;">🟡 FINANCIAL / BILLING — 2 Emails</div>
      <h3>Bank Alerts &amp; Receipts</h3>
      <table style="margin:8px 0;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Bank of America</td><td>Direct deposit credited — $760.38 (NYS DOL UI) — Account 7471</td><td><span class="badge badge-green">FYI — UI payment received</span></td></tr>
          <tr><td>Bank of America</td><td>Online transfer exceeded limit — Account 7471</td><td><span class="badge badge-red">URGENT — Verify now</span></td></tr>
        </tbody>
      </table>
      <div class="next-step"><strong>Recommended Action:</strong> UI deposit is normal — no action. Transfer alert requires immediate review of account activity.</div>
    </div>

    <!-- PERSONAL -->
    <div class="card card-teal">
      <div class="card-label" style="color:#006064;">🔵 PERSONAL — 6 Emails</div>
      <h3>Personal Accounts, Orders &amp; Lifestyle</h3>
      <table style="margin:8px 0;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Amazon.com</td><td>Shipped: 5 Candy, Skincare &amp; other items</td><td>Track delivery</td></tr>
          <tr><td>Amazon.com</td><td>Promotional credit from recent order (Order 114-3698716)</td><td>Note credit; use on next order</td></tr>
          <tr><td>Apple</td><td>Your receipt from Apple (music + items)</td><td>Verify purchase is authorized</td></tr>
          <tr><td>Ulta Beauty</td><td>Your package arrives soon! Order #M217756814</td><td>Expect delivery soon</td></tr>
          <tr><td>Notify NYC</td><td>Silver Alert — Sabato Noto, 81yo last seen Amsterdam Ave</td><td>Community alert — FYI only</td></tr>
          <tr><td>Melissa W (self)</td><td>GitHub Profile Masterclass — @hey__jay93 (self-sent link)</td><td>Review when ready for GitHub optimization</td></tr>
        </tbody>
      </table>
      <div class="next-step"><strong>Recommended Action:</strong> Verify Apple purchase if you don't recognize items. Track Amazon/Ulta deliveries. Silver Alert is community info only.</div>
    </div>

    <!-- MATCH / DATING -->
    <div class="card card-teal">
      <div class="card-label" style="color:#006064;">🔵 PERSONAL — Match.com — 3 Emails</div>
      <h3>Match.com Activity</h3>
      <table style="margin:8px 0;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th></tr></thead>
        <tbody>
          <tr><td>Match</td><td>You've had a profile view from Stephen (63, New City NY)</td><td>Inbox — review when ready</td></tr>
          <tr><td>Match</td><td>Lou just sent you a new message 💌</td><td>Not in inbox — check app</td></tr>
          <tr><td>Match</td><td>Lou likes you. See if it's mutual.</td><td>Not in inbox — check app</td></tr>
        </tbody>
      </table>
      <div class="next-step"><strong>Recommended Action:</strong> Check Match app for Lou's message and Stephen's profile view when convenient.</div>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="card card-purple">
      <div class="card-label" style="color:#6c3483;">🟣 PROFESSIONAL DEVELOPMENT — 2 Emails</div>
      <h3>HR Thought Leadership &amp; Learning</h3>
      <table style="margin:8px 0;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Coursiv</td><td>Your AI plan is ready — welcome to the community!</td><td>Review AI learning path when ready</td></tr>
          <tr><td>LinkedIn (Leah Kavanagh et al.)</td><td>Leah Kavanagh, M.Jur. and others share thoughts on LinkedIn</td><td>Skim feed; concierge medical hiring post noted</td></tr>
        </tbody>
      </table>
      <div class="next-step"><strong>Recommended Action:</strong> Check Coursiv AI learning plan — relevant for AI upskilling. LinkedIn digest is low-priority read.</div>
    </div>

    <!-- MEDICAL / HEALTH -->
    <div class="card card-gray">
      <div class="card-label" style="color:#5d6d7e;">⚪ MEDICAL / HEALTH — 6 Emails (Spam/Promotional)</div>
      <h3>Unsolicited GLP-1 / Weight Loss / Health Spam</h3>
      <table style="margin:8px 0;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th></tr></thead>
        <tbody>
          <tr><td>MEDVi GLP-1 (random domain)</td><td>Why 100,000+ people chose MEDVi for weight loss</td><td>Spam — not in inbox/trash</td></tr>
          <tr><td>MEDVi GLP-1 (repeat, random domain)</td><td>Why 100,000+ people chose MEDVi for weight loss</td><td>Spam duplicate — not in inbox</td></tr>
          <tr><td>DirectMeds/Ozempic (random domain)</td><td>GLP-1 treatment — lose up to 40 lbs by end of year</td><td>Spam — not in inbox</td></tr>
          <tr><td>TrimRX GLP-1 (random domain)</td><td>GLP-1 Bundle — $200 off</td><td>Spam — not in inbox</td></tr>
          <tr><td>TrimRx (random domain)</td><td>Welcome offer: $120 off + free shipping</td><td>Spam — not in inbox</td></tr>
          <tr><td>'Lung Clearing Method' (random domain)</td><td>Can't Catch Your Breath? Mucus Might Be the Reason</td><td>Health spam — not in inbox</td></tr>
        </tbody>
      </table>
      <div class="next-step"><strong>Recommended Action:</strong> All are unsolicited spam from random domains. Mark as spam and block senders. Do not click any links.</div>
    </div>

    <!-- NEWSLETTERS / SUBSCRIPTIONS -->
    <div class="card card-purple">
      <div class="card-label" style="color:#6c3483;">🟣 NEWSLETTERS / SUBSCRIPTIONS — 6 Emails</div>
      <h3>HR Digests, News &amp; Industry Newsletters</h3>
      <table style="margin:8px 0;">
        <thead><tr><th>Sender</th><th>Topic</th><th>Status</th></tr></thead>
        <tbody>
          <tr><td>HR Brew (Morning Brew)</td><td>ICE I-9 rule changes — compliance alert</td><td>Trashed — worth skimming before delete</td></tr>
          <tr><td>Johnny C. Taylor Jr. via LinkedIn</td><td>Manager burnout signs — SHRM perspective</td><td>Trashed newsletter</td></tr>
          <tr><td>BambooHR</td><td>1:1 manager check-in best practices</td><td>Not in inbox — low priority</td></tr>
          <tr><td>Dylan's Diary (Behind the Markets)</td><td>Where Bill Gates holds his money</td><td>Trashed — finance newsletter</td></tr>
          <tr><td>The Daily Skimm</td><td>Y2K fashion + daily news digest</td><td>Trashed — general news</td></tr>
          <tr><td>I AM PRESIDENT TRUMP (auto-trashed newsletter)</td><td>"You've been audited by Trump!" political fundraising</td><td>Auto-Trashed Newsletter — no action needed</td></tr>
        </tbody>
      </table>
      <div class="next-step"><strong>Recommended Action:</strong> The HR Brew I-9 article may be professionally relevant — skim before deleting. BambooHR and SHRM newsletter content is generic. Consider unsubscribing from non-essential newsletters to reduce inbox noise.</div>
    </div>

    <!-- PROMOTIONAL / RETAIL -->
    <div class="card card-gray">
      <div class="card-label" style="color:#5d6d7e;">
