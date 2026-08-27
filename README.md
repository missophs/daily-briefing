<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa W — August 27, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 16px; padding: 36px 40px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: flex-start; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header .date { font-size: 15px; opacity: 0.75; margin-top: 4px; }
  .header .meta { text-align: right; }
  .header .meta .badge { display: inline-block; background: rgba(255,255,255,0.15); border-radius: 20px; padding: 4px 14px; font-size: 13px; margin-left: 8px; margin-top: 4px; }

  /* SECTION HEADERS */
  .section { margin-bottom: 28px; }
  .section-header { display: flex; align-items: center; gap: 10px; margin-bottom: 14px; }
  .section-title { font-size: 18px; font-weight: 700; color: #1a1a2e; letter-spacing: -0.3px; }
  .section-icon { font-size: 20px; }
  .section-divider { height: 3px; border-radius: 2px; margin-bottom: 14px; }

  /* COLOR BANDS */
  .band-red { background: #e53e3e; }
  .band-yellow { background: #d69e2e; }
  .band-blue { background: #3182ce; }
  .band-green { background: #38a169; }
  .band-purple { background: #805ad5; }
  .band-gray { background: #718096; }
  .band-orange { background: #dd6b20; }

  /* CARDS */
  .card { border-radius: 12px; padding: 18px 22px; margin-bottom: 12px; border-left: 5px solid transparent; }
  .card-red { background: #fff5f5; border-left-color: #e53e3e; }
  .card-yellow { background: #fffff0; border-left-color: #d69e2e; }
  .card-blue { background: #ebf8ff; border-left-color: #3182ce; }
  .card-green { background: #f0fff4; border-left-color: #38a169; }
  .card-purple { background: #faf5ff; border-left-color: #805ad5; }
  .card-gray { background: #f7fafc; border-left-color: #718096; }
  .card-orange { background: #fffaf0; border-left-color: #dd6b20; }

  .card-label { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
  .label-red { color: #e53e3e; }
  .label-yellow { color: #b7791f; }
  .label-blue { color: #2b6cb0; }
  .label-green { color: #276749; }
  .label-purple { color: #553c9a; }
  .label-gray { color: #4a5568; }
  .label-orange { color: #c05621; }

  .card-title { font-size: 15px; font-weight: 700; margin-bottom: 6px; }
  .card-meta { font-size: 12px; color: #718096; margin-bottom: 8px; }
  .card-body { font-size: 13px; color: #2d3748; }
  .card-body p { margin-bottom: 5px; }
  .card-body strong { color: #1a1a2e; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 6px rgba(0,0,0,0.07); margin-bottom: 12px; }
  th { background: #2d3748; color: #fff; padding: 11px 14px; text-align: left; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.7px; }
  td { padding: 10px 14px; border-bottom: 1px solid #edf2f7; font-size: 13px; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f7fafc; }

  /* BADGES / PILLS */
  .pill { display: inline-block; border-radius: 12px; padding: 2px 10px; font-size: 11px; font-weight: 700; }
  .pill-red { background: #fed7d7; color: #9b2c2c; }
  .pill-yellow { background: #fefcbf; color: #744210; }
  .pill-green { background: #c6f6d5; color: #22543d; }
  .pill-blue { background: #bee3f8; color: #2a4365; }
  .pill-purple { background: #e9d8fd; color: #44337a; }
  .pill-gray { background: #e2e8f0; color: #4a5568; }
  .pill-orange { background: #feebc8; color: #7b341e; }

  /* EXEC SUMMARY */
  .exec-bullets { list-style: none; }
  .exec-bullets li { padding: 12px 18px; border-radius: 10px; margin-bottom: 10px; font-size: 14px; display: flex; align-items: flex-start; gap: 12px; }
  .exec-bullets li .bullet-icon { font-size: 20px; flex-shrink: 0; margin-top: 1px; }
  .bullet-risk { background: #fff5f5; border-left: 4px solid #e53e3e; }
  .bullet-opp { background: #f0fff4; border-left: 4px solid #38a169; }
  .bullet-cal { background: #ebf8ff; border-left: 4px solid #3182ce; }

  /* TRIAGE TABLE STATUS */
  .status-rescued { color: #276749; font-weight: 700; }
  .status-inbox { color: #2b6cb0; font-weight: 700; }
  .status-autotrash { color: #9b2c2c; font-weight: 700; }
  .status-trash { color: #718096; font-weight: 700; }

  /* CALENDAR */
  .cal-day { background: #fff; border-radius: 12px; margin-bottom: 14px; overflow: hidden; box-shadow: 0 1px 6px rgba(0,0,0,0.07); }
  .cal-day-header { background: #2d3748; color: #fff; padding: 10px 18px; font-weight: 700; font-size: 14px; }
  .cal-today-header { background: linear-gradient(90deg, #3182ce, #2b6cb0); }
  .cal-event { padding: 14px 18px; border-bottom: 1px solid #edf2f7; }
  .cal-event:last-child { border-bottom: none; }
  .cal-event-time { font-size: 12px; font-weight: 700; color: #3182ce; margin-bottom: 3px; }
  .cal-event-name { font-size: 14px; font-weight: 700; margin-bottom: 5px; }
  .cal-event-meta { font-size: 12px; color: #718096; }
  .cal-event-meta span { margin-right: 14px; }
  .cal-conflict { background: #fff5f5; border-left: 3px solid #e53e3e; padding: 5px 10px; border-radius: 6px; font-size: 12px; color: #c53030; margin-top: 5px; }
  .cal-prep { background: #ebf8ff; border-left: 3px solid #3182ce; padding: 5px 10px; border-radius: 6px; font-size: 12px; color: #2b6cb0; margin-top: 5px; }

  /* PRIORITY TABLE */
  .priority-high { color: #e53e3e; font-weight: 700; }
  .priority-medium { color: #d69e2e; font-weight: 700; }
  .priority-low { color: #718096; font-weight: 700; }

  /* TOP 3 */
  .top3 { display: flex; gap: 16px; flex-wrap: wrap; }
  .top3-card { flex: 1; min-width: 280px; background: linear-gradient(135deg, #1a1a2e, #2d3748); color: #fff; border-radius: 14px; padding: 22px 22px; }
  .top3-num { font-size: 36px; font-weight: 900; opacity: 0.2; line-height: 1; margin-bottom: 6px; }
  .top3-title { font-size: 15px; font-weight: 700; margin-bottom: 6px; }
  .top3-body { font-size: 13px; opacity: 0.8; }

  /* DASHBOARD GRID */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-widget { background: #fff; border-radius: 12px; padding: 18px; box-shadow: 0 1px 6px rgba(0,0,0,0.07); }
  .dash-widget-title { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; color: #718096; margin-bottom: 8px; }
  .dash-widget-value { font-size: 28px; font-weight: 800; margin-bottom: 4px; }
  .dash-widget-sub { font-size: 12px; color: #718096; }
  .val-red { color: #e53e3e; }
  .val-green { color: #38a169; }
  .val-blue { color: #3182ce; }
  .val-yellow { color: #d69e2e; }
  .val-purple { color: #805ad5; }

  /* MISC */
  .note-box { background: #fffbeb; border: 1px solid #f6e05e; border-radius: 10px; padding: 12px 16px; font-size: 13px; color: #744210; margin-bottom: 14px; }
  .info-box { background: #ebf8ff; border: 1px solid #bee3f8; border-radius: 10px; padding: 12px 16px; font-size: 13px; color: #2a4365; margin-bottom: 14px; }
  .tag { display: inline-block; background: #edf2f7; border-radius: 6px; padding: 1px 7px; font-size: 11px; color: #4a5568; margin-right: 4px; }
  ul.item-list { list-style: none; padding: 0; }
  ul.item-list li { padding: 5px 0; border-bottom: 1px solid #edf2f7; font-size: 13px; }
  ul.item-list li:last-child { border-bottom: none; }
  .rescued-note { background: #c6f6d5; color: #22543d; border-radius: 6px; padding: 2px 8px; font-size: 11px; font-weight: 700; }
  .auto-trash-note { background: #fed7d7; color: #9b2c2c; border-radius: 6px; padding: 2px 8px; font-size: 11px; font-weight: 700; }
  .section-sub { font-size: 13px; color: #4a5568; margin-bottom: 12px; }
  hr.light { border: none; border-top: 1px solid #e2e8f0; margin: 18px 0; }

  @media (max-width: 700px) {
    .header { flex-direction: column; gap: 16px; }
    .header .meta { text-align: left; }
    .top3 { flex-direction: column; }
  }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ═══════════════════════════════════════════════════════ -->
<!-- SECTION 0 — EMAIL TRIAGE QUICK LIST -->
<!-- ═══════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-icon">⚡</span>
    <span class="section-title">Email Triage Quick List</span>
  </div>
  <div class="section-divider band-blue"></div>
  <div class="info-box">Sorted: ✅ Rescued → 📥 Inbox → 🗑 Auto-Trashed (summary) → 🗂 Trash (summary). Inbox &amp; rescued emails shown individually; trash collapsed into summary rows.</div>
  <table>
    <thead>
      <tr>
        <th style="width:120px">Status</th>
        <th style="width:210px">From</th>
        <th>Subject</th>
        <th>Summary</th>
      </tr>
    </thead>
    <tbody>
      <!-- RESCUED -->
      <tr>
        <td><span class="status-rescued">✅ RESCUED</span></td>
        <td>JetBlue Plus Card (Barclays)</td>
        <td>Reminder: Activate your 8.99% promo rate now</td>
        <td><span class="rescued-note">Rescued from Trash</span> — Protected financial sender. Low promo APR offer on purchases. Review &amp; activate if desired.</td>
      </tr>
      <!-- INBOX -->
      <tr>
        <td><span class="status-inbox">📥 INBOX</span></td>
        <td>OkCupid</td>
        <td>Someone likes you</td>
        <td>Dating app notification. Personal — low priority for briefing.</td>
      </tr>
      <tr>
        <td><span class="status-inbox">📥 INBOX</span></td>
        <td>Chase</td>
        <td>Your credit card statement is available</td>
        <td>⚠️ Chase card (...8874) statement ready. Min payment $35 due 09/23/2026.</td>
      </tr>
      <tr>
        <td><span class="status-inbox">📥 INBOX</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>Principal HRBP, GTM at Atlassian</td>
        <td>Strong job lead. HRBP role at Atlassian. Review &amp; apply.</td>
      </tr>
      <tr>
        <td><span class="status-inbox">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>Website</td>
        <td>Self-sent link — LinkedIn URL saved for reference.</td>
      </tr>
      <tr>
        <td><span class="status-inbox">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>Connect request</td>
        <td>Self-sent Claude AI share link — networking/connect script reference.</td>
      </tr>
      <tr>
        <td><span class="status-inbox">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>Ai tools for recruitment</td>
        <td>Self-sent link to talent-stack.io — AI recruiting tools research.</td>
      </tr>
      <tr>
        <td><span class="status-inbox">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>Income ideas</td>
        <td>Self-sent LinkedIn link — side income research.</td>
      </tr>
      <tr>
        <td><span class="status-inbox">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>McKinsey</td>
        <td>McKinsey article on HR for the agentic AI era. Professional development.</td>
      </tr>
      <tr>
        <td><span class="status-inbox">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>Ai prompts</td>
        <td>Self-sent LinkedIn link — AI prompts collection.</td>
      </tr>
      <tr>
        <td><span class="status-inbox">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>Remote job site</td>
        <td>Self-sent LinkedIn link — remote job board resource.</td>
      </tr>
      <tr>
        <td><span class="status-inbox">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>How Claude's Text Watermark Works</td>
        <td>Self-sent AI content watermarking article. Professional development/research.</td>
      </tr>
      <!-- AUTO-TRASHED SUMMARY -->
      <tr style="background:#fff5f5;">
        <td><span class="status-autotrash">🗑 AUTO-TRASHED</span></td>
        <td colspan="2"><strong>2 emails auto-trashed (phishing/scam)</strong> — see Trash Review &amp; Security/Risk section</td>
        <td><span class="auto-trash-note">Removed before inbox</span> — Spoofed CashApp payment scams from gibberish domains. No action needed.</td>
      </tr>
      <!-- MANUAL TRASH SUMMARY -->
      <tr style="background:#f7fafc;">
        <td><span class="status-trash">🗂 TRASH (manual)</span></td>
        <td colspan="2"><strong>~15 emails in Trash</strong> — see Trash Review section</td>
        <td>Mix of newsletters, retail promos, job digests, adult spam &amp; low-value content. See Trash Review for details.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════ -->
<!-- SECTION 1 — HEADER -->
<!-- ═══════════════════════════════════════════════════════ -->
<div class="header">
  <div>
    <div style="font-size:13px;opacity:0.65;margin-bottom:4px;text-transform:uppercase;letter-spacing:1px;">Executive Briefing</div>
    <h1>Good morning, Melissa ☀️</h1>
    <div class="date">Thursday, August 27, 2026 &nbsp;·&nbsp; Prepared by Your Executive Chief of Staff</div>
  </div>
  <div class="meta">
    <div style="font-size:13px;opacity:0.75;margin-bottom:6px;">Today's Snapshot</div>
    <div><span class="badge">📧 50 Emails Reviewed</span></div>
    <div style="margin-top:6px;"><span class="badge">📅 7 Calendar Events</span></div>
    <div style="margin-top:6px;"><span class="badge">🔴 2 Security Flags</span></div>
    <div style="margin-top:6px;"><span class="badge">💼 5 Job Leads</span></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════ -->
<!-- SECTION 2 — EXECUTIVE SUMMARY -->
<!-- ═══════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-icon">📋</span>
    <span class="section-title">Executive Summary</span>
  </div>
  <div class="section-divider band-red"></div>
  <ul class="exec-bullets">
    <li class="bullet-risk">
      <span class="bullet-icon">🔴</span>
      <span><strong>Security Risk:</strong> Two spoofed "CashApp" phishing emails (from gibberish domains) were auto-trashed before reaching your inbox. Additionally, multiple unsolicited health/ED spam emails arrived from suspicious senders. Your inbox is secure, but your email address is clearly on active spam lists — no credentials were compromised.</span>
    </li>
    <li class="bullet-opp">
      <span class="bullet-icon">💼</span>
      <span><strong>Job Search Opportunity:</strong> Five active job leads today including a VP of HR role at Vaco ($225K–$250K), an EVP HR role at SearchPointNY ($175K–$240K), a Principal HRBP at Atlassian, and an HRBP in Fairfield County, CT. Your Deckers Brands Sr. Manager application received a "Thank You" acknowledgment, and your Modivcare VP HRBP application has a status update to review.</span>
    </li>
    <li class="bullet-cal">
      <span class="bullet-icon">📅</span>
      <span><strong>Calendar &amp; Deadline:</strong> Today's HR Networking Open Office Hours (12:00–1:00 PM, Zoom) has not been RSVP'd — decision needed now. Your Chase credit card statement is ready with a minimum payment of $35 due 09/23/2026. Tomorrow's "Transfer Money" calendar reminder is flagged for your attention.</span>
    </li>
  </ul>
</div>

<!-- ═══════════════════════════════════════════════════════ -->
<!-- SECTION 3 — ACTION REQUIRED -->
<!-- ═══════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-icon">🚨</span>
    <span class="section-title">Action Required</span>
  </div>
  <div class="section-divider band-red"></div>

  <div class="card card-yellow">
    <div class="card-label label-yellow">⚠️ BILLING — DEADLINE</div>
    <div class="card-title">Chase Credit Card Statement Available</div>
    <div class="card-meta">From: Chase &lt;no.reply.alerts@chase.com&gt; · Received: Aug 27, 2026</div>
    <div class="card-body">
      <p><strong>Account:</strong> Chase Credit Card (…8874)</p>
      <p><strong>Minimum Payment Due:</strong> $35.00 &nbsp;|&nbsp; <strong>Due Date:</strong> September 23, 2026</p>
      <p><strong>Why it matters:</strong> Missing the due date triggers late fees and potential credit score impact.</p>
      <p><strong>Next Step:</strong> Log into Chase online to review full statement balance and set up payment or auto-pay before 09/23.</p>
    </div>
  </div>

  <div class="card card-yellow">
    <div class="card-label label-yellow">⚠️ FINANCIAL — REVIEW</div>
    <div class="card-title">JetBlue Plus Card — Activate 8.99% Promo APR</div>
    <div class="card-meta">From: JetBlue Plus Card / Barclays · <span class="rescued-note">✅ Rescued from Trash</span></div>
    <div class="card-body">
      <p><strong>Why it matters:</strong> This is a legitimate offer from a protected financial sender that was initially trashed. A low promo APR could be useful if you have purchases planned.</p>
      <p><strong>Next Step:</strong> Open email, review terms, and activate if the promo rate aligns with your financial strategy. Check expiry date of the offer.</p>
    </div>
  </div>

  <div class="card card-blue">
    <div class="card-label label-blue">📅 RSVP NEEDED — TODAY</div>
    <div class="card-title">HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
    <div class="card-meta">Calendar Event · Today, Aug 27 · 12:00 PM – 1:00 PM ET · Status: Needs Action</div>
    <div class="card-body">
      <p><strong>Why it matters:</strong> This is a high-value networking session directly relevant to your active job search. 190+ HR professionals in attendance. You have not RSVP'd.</p>
      <p><strong>Zoom Link:</strong> https://us06web.zoom.us/j/85945371140</p>
      <p><strong>Note:</strong> Organizer asks — please turn off automated AI notetaking tools.</p>
      <p><strong>Next Step:</strong> RSVP and join at noon if attending. Block prep time now. Confirm or decline the calendar invite.</p>
      <p><strong>Due:</strong> TODAY — 12:00 PM ET</p>
    </div>
  </div>

  <div class="card card-green">
    <div class="card-label label-green">💼 JOB SEARCH — FOLLOW UP</div>
    <div class="card-title">Modivcare — Application Status Update: VP, HR Business Partner</div>
    <div class="card-meta">From: modivcare@myworkday.com · Received: Aug 27, 2026</div>
    <div class="card-body">
      <p><strong>Why it matters:</strong> You received an application update on a VP-level HRBP role. The snippet is cut off — status could be interview invite or rejection.</p>
      <p><strong>Next Step:</strong> Open email immediately to determine outcome. If advancing, prepare materials. If rejected, note for tracking.</p>
    </div>
  </div>

  <div class="card card-green">
    <div class="card-label label-green">💼 JOB SEARCH — REVIEW</div>
    <div class="card-title">Deckers Brands — Application Acknowledged: Sr. Manager, People &amp; Experience</div>
    <div class="card-meta">From: workday deckers &lt;deckers@myworkday.com&gt; · Received: Aug 27, 2026</div>
    <div class="card-body">
      <p><strong>Why it matters:</strong> Application confirmed received. No interview yet — track status and follow up in 7–10 business days if no further response.</p>
      <p><strong>Next Step:</strong> Log application in your tracker. Set a follow-up reminder for ~Sept 8, 2026.</p>
    </div>
  </div>

  <div class="card card-green">
    <div class="card-label label-green">💼 JOB SEARCH — HIGH PRIORITY</div>
    <div class="card-title">LinkedIn Alert: VP of Human Resources at Vaco by Highspring — Up to $250K/year</div>
    <div class="card-meta">From: LinkedIn Job Alerts · Received: Aug 27, 2026 · Salary: $225K–$250K</div>
    <div class="card-body">
      <p><strong>Why it matters:</strong> This is the highest-compensation role in today's alerts and directly matches your VP HR profile.</p>
      <p><strong>Next Step:</strong> Review full job description on LinkedIn and apply today if aligned. Tailor resume using your ATS prompt process.</p>
    </div>
  </div>

  <div class="card card-orange">
    <div class="card-label label-orange">📅 CALENDAR REMINDER</div>
    <div class="card-title">LinkedIn Post — Due Today</div>
    <div class="card-meta">Calendar Event · Aug 27 (All Day)</div>
    <div class="card-body">
      <p><strong>Why it matters:</strong> You've scheduled a LinkedIn post for today. Consistent posting boosts visibility during your job search.</p>
      <p><strong>Next Step:</strong> Draft and publish your LinkedIn post today. Consider using the McKinsey HR/AI article or one of your self-saved resources as content inspiration.</p>
    </div>
  </div>

  <div class="card card-orange">
    <div class="card-label label-orange">📅 BIRTHDAY REMINDER</div>
    <div class="card-title">Christian H's Birthday — Today</div>
    <div class="card-meta">Calendar Event · Aug 27 (All Day)</div>
    <div class="card-body">
      <p><strong>Next Step:</strong> Send a birthday message, call, or LinkedIn note to Christian H today.</p>
    </div>
  </div>

  <div class="card card-yellow">
    <div class="card-label label-yellow">⚠️ AMAZON — ACTION NEEDED</div>
    <div class="card-title">Amazon Associates Program Application Rejected</div>
    <div class="card-meta">From: Amazon Associates &lt;associates@amazon.com&gt; · Received: Aug 27, 2026</div>
    <div class="card-body">
      <p><strong>Account:</strong> modernluxlist-20</p>
      <p><strong>Why it matters:</strong> Your Amazon Associates application was rejected. If this was intended as a side income stream, you'll need to review the rejection reason and decide whether to reapply or pivot strategy.</p>
      <p><strong>Next Step:</strong> Review full rejection email for reason. Address qualifying criteria (site traffic, content policy, etc.) and consider reapplying or exploring alternative affiliate programs.</p>
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════ -->
<!-- SECTION 4 — FULL 7-DAY CALENDAR -->
<!-- ═══════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-icon">📅</span>
    <span class="section-title">Full 7-Day Calendar</span>
  </div>
  <div class="section-divider band-blue"></div>

  <!-- TODAY: AUG 27 -->
  <div class="cal-day">
    <div class="cal-day-header cal-today-header">📍 TODAY — Thursday, August 27, 2026</div>

    <div class="cal-event">
      <div class="cal-event-time">ALL DAY</div>
      <div class="cal-event-name">🎂 Christian H's Birthday</div>
      <div class="cal-event-meta">
        <span><strong>Status:</strong> Confirmed</span>
        <span><strong>Attendees:</strong> None listed (personal)</span>
      </div>
      <div class="cal-prep">💡 Action: Send a birthday message or call today.</div>
    </div>

    <div class="cal-event">
      <div class="cal-event-time">ALL DAY</div>
      <div class="cal-event-name">📝 LinkedIn Post</div>
      <div class="cal-event-meta">
        <span><strong>Status:</strong> Confirmed</span>
        <span><strong>Attendees:</strong> None</span>
      </div>
      <div class="cal-prep">💡 Prep: Draft post content. Consider using McKinsey AI/HR article, Claude watermark article, or AI tools research as inspiration. Publish before end of day.</div>
    </div>

    <div class="cal-event" style="background:#fff5f5;">
      <div class="cal-event-time">9:00 AM – 10:30 AM ET</div>
      <div class="cal-event-name">🟡 Executive Roundtable <span class="pill pill-yellow">DECLINED</span></div>
      <div class="cal-event-meta">
        <span><strong>Host:</strong> John Madigan</span>
        <span><strong>Location:</strong> Zoom — Meeting ID: 207 786 667 / PW: 205454</span>
        <span><strong>Status:</strong> Declined</span>
      </div>
      <div class="cal-conflict">⚠️ You declined this event. No action needed unless you wish to rejoin — contact John Madigan.</div>
    </div>

    <div class="cal-event" style="background:#f0fff4;">
      <div class="cal-event-time">12:00 PM – 1:00 PM ET</div>
      <div class="cal-event-name">🟢 HR Networking &amp; Job Search: Open Office Hours — Zoom 2 <span class="pill pill-yellow">RSVP NEEDED</span></div>
      <div class="cal-event-meta">
        <span><strong>Status:</strong> Needs Action</span>
        <span><strong>Attendees:</strong> 190+ HR professionals</span>
      </div>
      <div class="cal-event-meta" style="margin-top:5px;">
        <span><strong>Zoom:</strong> <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" style="color:#3182ce;">Join Meeting</a></span>
      </div>
      <div class="cal-prep">💡 RSVP immediately. High-value networking session for active job seekers. Note: No AI notetaking tools per organizer request. Prepare your 30-second intro and 1–2 questions for the group.</div>
    </div>
  </div>

  <!-- AUG 28 -->
  <div class="cal-day">
    <div class="cal-day-header">Friday, August 28, 2026</div>
    <div class="cal-event">
      <div class="cal-event-time">ALL DAY</div>
      <div class="cal-event-name">💸 Transfer Money</div>
      <div class="cal-event-meta">
        <span><strong>Status:</strong> Confirmed</span>
        <span><strong>Attendees:</strong> None</span>
      </div>
      <div class="cal-prep">💡 Reminder: Execute your scheduled money transfer. Coordinate with Chase statement review (due 9/23). Confirm accounts and amounts.</div>
    </div>
  </div>

  <!-- AUG 29–SEP 1 -->
  <div class="cal-day">
    <div class="cal-day-header">Saturday Aug 29 – Monday Aug 31, 2026</div>
    <div class="cal-event">
      <div class="cal-event-time">No events scheduled</div>
      <div class="cal-event-name" style="color:#718096;">— Clear calendar —</div>
      <div class="cal-prep">💡 Consider using weekend time for: LinkedIn post drafting, job application research, Amazon Associates reapplication strategy, or following up on networking contacts.</div>
    </div>
  </div>

  <!-- LABOR DAY -->
  <div class="cal-day">
    <div class="cal-day-header">Monday, August 31 / Tuesday, September 1, 2026</div>
    <div class="cal-event">
      <div class="cal-event-time">No events scheduled</div>
      <div class="cal-event-name" style="color:#718096;">— Clear calendar — Note: Labor Day weekend</div>
      <div class="cal-prep">💡 Hiring activity may be slower over Labor Day weekend (Aug 30–Sept 1). Use time to finalize Vaco VP application and prep for Sept 2 networking session.</div>
    </div>
  </div>

  <!-- SEP 2 -->
  <div class="cal-day">
    <div class="cal-day-header">Tuesday, September 2, 2026</div>

    <div class="cal-event" style="background:#f0fff4;">
      <div class="cal-event-time">12:00 PM – 1:30 PM ET</div>
      <div class="cal-event-name">🟢 HR Networking &amp; Job Search Group — Zoom 2 <span class="pill pill-yellow">RSVP NEEDED</span></div>
      <div class="cal-event-meta">
        <span><strong>Status:</strong> Needs Action</span>
        <span><strong>Attendees:</strong> 190+ HR professionals</span>
        <span><strong>Zoom:</strong> <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" style="color:#3182ce;">Join Meeting</a></span>
      </div>
      <div class="cal-prep">💡 Prep: Review team guidelines linked in event description before joining. 90-minute session — longer than today's call. Prepare updates on your job search progress and specific ask/ask-for from the group.</div>
    </div>

    <div class="cal-event">
      <div class="cal-event-time">12:00 PM – 1:30 PM ET</div>
      <div class="cal-event-name">📌 Network <span class="pill pill-green">CONFIRMED</span></div>
      <div class="cal-event-meta">
        <span><strong>Status:</strong> Confirmed (personal block)</span>
        <span><strong>Note:</strong> Overlaps with HR Networking Group Zoom — this appears to be your personal confirmed placeholder for the same block.</span>
      </div>
      <div class="cal-conflict">⚠️ Overlap: "Network" block runs same time as HR Networking Group Zoom. No conflict if these are the same event — confirm and consolidate calendar entries.</div>
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════ -->
<!-- SECTION 5 — JOB SEARCH & INTERVIEW PIPELINE -->
<!-- ═══════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-icon">💼</span>
    <span class="section-title">Job Search &amp; Interview Pipeline</span>
  </div>
  <div class="section-divider band-green"></div>

  <table>
    <thead>
      <tr>
        <th>Fit</th>
        <th>Company / Role</th>
        <th>Source</th>
        <th>Compensation</th>
        <th>Status</th>
        <th>Next Step</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="pill pill-red">HIGH</span></td>
        <td><strong>VP of Human Resources</strong><br>Vaco by Highspring</td>
        <td>LinkedIn Job Alert</td>
        <td>$225K–$250K/yr</td>
        <td><span class="pill pill-yellow">Not Applied</span></td>
        <td>Apply today — highest comp role in pipeline</td>
      </tr>
      <tr>
        <td><span class="pill pill-red">HIGH</span></td>
        <td><strong>EVP of Human Resources</strong><br>SearchPointNY</td>
        <td>LinkedIn Job Alert</td>
        <td>$175K–$240K/yr</td>
        <td><span class="pill pill-yellow">Not Applied</span></td>
        <td>Review full description; apply if aligned</td>
      </tr>
      <tr>
        <td><span class="pill pill-red">HIGH</span></td>
        <td><strong>Principal HRBP, GTM</strong><br>Atlassian</td>
        <td>LinkedIn Job Alert (2 alerts)</td>
        <td>Not listed</td>
        <td><span class="pill pill-yellow">Not Applied</span></td>
        <td>In inbox — review &amp; apply; sent twice, strong signal</td>
      </tr>
      <tr>
        <td><span class="pill pill-green">MEDIUM</span></td>
        <td><strong>VP, HR Business Partner</strong><br>Modivcare</td>
        <td>Workday application</td>
        <td>Not listed</td>
        <td><span class="pill pill-blue">Update Received</span></td>
        <td>Open email to check status — could be interview invite</td>
      </tr>
      <tr>
        <td><span class="pill pill-green">MEDIUM</span></td>
        <td><strong>Sr. Manager, People &amp; Experience</strong><br>Deckers Brands</td>
        <td>Workday application</td>
        <td>Not listed</td>
        <td><span class="pill pill-green">Applied — Acknowledged</span></td>
        <td>Track; follow up ~Sept 8 if no response</td>
      </tr>
      <tr>
        <td><span class="pill pill-green">MEDIUM</span></td>
        <td><strong>HR Business Partner</strong><br>RightPro Staffing — Fairfield County, CT</td>
        <td>PostJobFree / Dennis Gorelik</td>
        <td>Not listed</td>
        <td><span class="pill pill-gray">In Trash</span></td>
        <td>Restore from trash if CT location is acceptable</td>
      </tr>
      <tr>
        <td><span class="pill pill-gray">LOW</span></td>
        <td><strong>Global Benefits Lead</strong><br>insightsoftware &amp; 7 more roles</td>
        <td>Glassdoor</td>
        <td>Not listed</td>
        <td><span class="pill pill-gray">In Trash</span></td>
        <td>Restore from trash to review all 8 roles listed</td>
      </tr>
      <tr>
        <td><span class="pill pill-gray">REF</span></td>
        <td><strong>ICF Careers</strong><br>Multiple open roles</td>
        <td>ICF Careers email</td>
        <td>Not listed</td>
        <td><span class="pill pill-yellow">Unread — Not Applied</span></td>
        <td>Browse ICF open jobs; complete profile if interested</td>
      </tr>
    </tbody>
  </table>

  <div class="card card-green">
    <div class="card-label label-green">🤝 NETWORKING</div>
    <div class="card-title">HR Networking Group — Active Participation</div>
    <div class="card-body">
      <p><strong>Today:</strong> Open Office Hours Zoom (12–1 PM) — RSVP needed</p>
      <p><strong>Sept 2:</strong> Full Group Session (12–1:30 PM) — RSVP needed</p>
      <p><strong>Community:</strong> 190+ HR professionals. High-value for referrals, leads, and peer support during job search.</p>
      <p><strong>Self-Research Saved:</strong> AI tools for recruitment (talent-stack.io), remote job site, AI prompts, income ideas, connect request templates, McKinsey HR/AI article — all self-emailed for reference.</p>
    </div>
  </div>

  <div class="card card-purple">
    <div class="card-label label-purple">🧠 AI JOB SEARCH TOOLS IN USE</div>
    <div class="card-title">ATS Resume Scanner + AI Recruitment Tools</div>
    <div class="card-body">
      <p>You've self-emailed an ATS resume scanning prompt and links to AI recruitment tools. You're actively using ChatGPT (now with Health integration enabled) and Claude for job search optimization.</p>
      <p><strong>Recommendation:</strong> Use your ATS prompt on the Vaco VP and Atlassian HRBP job descriptions before applying today.</p>
    </div>
  </div>

  <div class="card card-yellow">
    <div class="card-label label-yellow">⚠️ SIDE INCOME</div>
    <div class="card-title">Amazon Associates — Application Rejected (modernluxlist-20)</div>
    <div class="card-body">
      <p>Your affiliate application was rejected. Review the rejection reason. Common causes: insufficient site traffic, thin content, or policy issues. Consider reapplying after building content on your site.</p>
      <p><strong>Alternative:</strong> You self-emailed an "Income ideas" LinkedIn link — review for alternative side income options.</p>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════ -->
<!-- SECTION 6 — FULL EMAIL REVIEW BY CATEGORY -->
<!-- ═══════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-icon">📬</span>
    <span class="section-title">Full Email Review by Category</span>
  </div>
  <div class="section-divider band-red"></div>

  <!-- SECURITY / RISK -->
  <div class="card card-red">
    <div class="card-label label-red">🔴 SECURITY / RISK — 7 EMAILS</div>
    <div class="card-title">Phishing, Scam, Spam &amp; Suspicious Senders</div>
    <div class="card-body">
      <table>
        <thead><tr><th>Status</th><th>From</th><th>Subject</th><th>Threat Type</th></tr></thead>
        <tbody>
          <tr>
            <td><span class="auto-trash-note">Auto-Trashed</span></td>
            <td>"💲CashApp💲" &lt;info@tislfdedeglxu&gt;</td>
            <td>You have received 15.99$ — Raging Bull Casino</td>
            <td>Spoofed CashApp from gibberish domain. Fake payment/casino credential harvest scam. <strong>No action needed.</strong></td>
          </tr>
          <tr>
            <td><span class="auto-trash-note">Auto-Trashed</span></td>
            <td>"💲CashApp💲" &lt;info@qyukrsspyuqmq&gt;</td>
            <td>You have received 15.99$ — Raging Bull Casino</td>
            <td>Duplicate spoofed CashApp campaign. Same scam, different domain. <strong>No action needed.</strong></td>
          </tr>
          <tr>
            <td><span class="pill pill-red">Spam — Suspicious</span></td>
            <td>Reverse.Type.2.Diabetes &lt;inggnmyanvx@jgwk.dgirumszqqsfw.us&gt;</td>
            <td>Whats lurking in your pancreas could be causing your Type 2 Diabetes</td>
            <td>"Biblical Regimen" parasite cure — health misinformation scam. Do not click.</td>
          </tr>
          <tr>
            <td><span class="pill pill-red">Spam — Suspicious</span></td>
            <td>Protection &lt;jzmpsupportby@apdlayhjokqfzrjhuemmlwun.com&gt;</td>
            <td>Understanding the Basics of Blood Sugar Health</td>
            <td>Same "Biblical Regimen" scam campaign. Gibberish domain. Do not click.</td>
          </tr>
          <tr>
            <td><span class="pill pill-red">Spam — In Trash</span></td>
            <td>"'Congratulations!'" &lt;duzssupportshsa@fylvfcpqzaugbdupwaqkgeiq.com&gt;</td>
            <td>💲 You have received a payment $2500.00 💲</td>
            <td>Casino fake payment scam. Already trashed. No action needed.</td>
          </tr>
          <tr>
            <td><span class="pill pill-red">Adult Spam — Suspicious</span></td>
            <td>Holy_Vigor &lt;pvgoansyrrl@knwm.vbkyjrcyofolu.us&gt;</td>
            <td>Real root cause of limp performances 🔥</td>
            <td>Adult product spam from gibberish domain. Do not engage. Mark spam.</td>
          </tr>
          <tr>
            <td><span class="pill pill-red">Phishing-Style — Suspicious</span></td>
            <td>GLP-1-by-DirectMeds &lt;qbgqkeydhax@udmq.ohgxajcullrie.us&gt;</td>
            <td>DirectMeds GLP-1 treatment helps you lose up to 40 lbs</td>
            <td>Unregulated prescription medication solicitation from gibberish domain. Do not click.</td>
          </tr>
        </tbody>
      </table>
      <p style="margin-top:10px;"><strong>Recommended Action:</strong> Auto-trashed emails — no action. Remaining suspicious emails: Mark as spam in Gmail to train filter. Do NOT click any links in these messages. Your email address is on multiple spam/scam lists.</p>
    </div>
  </div>

  <!-- JOB SEARCH -->
  <div class="card card-green">
    <div class="card-label label-green">💼 JOB SEARCH — 9 EMAILS</div>
    <div class="card-title">Applications, Job Alerts &amp; Recruiter Activity</div>
    <div class="card-body">
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Status</th></tr></thead>
        <tbody>
          <tr><td>LinkedIn Job Alerts</td><td>Principal HRBP, GTM at Atlassian (in inbox)</td><td><span class="pill pill-yellow">Review &amp; Apply</span></td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>VP of Human Resources at Vaco — up to $250K/yr</td><td><span class="pill pill-yellow">Review &amp; Apply</span></td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>EVP of Human Resources at SearchPointNY — up to $240K</td><td><span class="pill pill-yellow">Review &amp; Apply</span></td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>Principal HRBP, GTM at Atlassian (duplicate, earlier)</td><td><span class="pill pill-gray">Duplicate — Archive</span></td></tr>
          <tr><td>Glassdoor</td><td>Global Benefits Lead at insightsoftware + 7 more (in trash)</td><td><span class="pill pill-yellow">Restore &amp; Review</span></td></tr>
          <tr><td>Dennis Gorelik / PostJobFree</td><td>RightPro Staffing — HRBP in Fairfield County, CT (in trash)</td><td><span class="pill pill-yellow">Restore if CT OK</span></td></tr>
          <tr><td>Workday Deckers</td><td>Thank You — Sr. Manager, People &amp; Experience application</td><td><span class="pill pill-green">Applied — Tracking</span></td></tr>
          <tr><td>Modivcare / Workday</td><td>Update on your Application — VP, HR Business Partner</td><td><span class="pill pill-red">Read Immediately</span></td></tr>
          <tr><td>ICF Careers</td><td>Explore life at ICF — discover new opportunities</td><td><span class="pill pill-yellow">Review ICF roles</span></td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- NETWORKING -->
  <div class="card card-green">
    <div class="card-label label-green">🤝 RECRUITERS / NETWORKING — 1 EMAIL + SELF-NOTES</div>
    <div class="card-title">HR Networking &amp; Professional Outreach</div>
    <div class="card-body">
      <p><strong>People People Group Digest</strong> (in trash) — temp staffing agency recommendations and 8+ HR networking topics. Consider restoring to review recommendations.</p>
      <p><strong>Stanton Chase via LinkedIn</strong> (in trash) — "Is Your Executive Leadership Still the Right Fit? A Three-Step Framework for Boards." Relevant executive content; restore if desired for reading.</p>
    </div>
  </div>

  <!-- CALENDAR / EVENTS -->
  <div class="card card-blue">
    <div class="card-label label-blue">📅 CALENDAR / EVENTS — 2 EMAILS</div>
    <div class="card-title">Event Invitations &amp; Meeting Links</div>
    <div class="card-body">
      <p><strong>HR Networking Open Office Hours (Today 12–1 PM)</strong> — Calendar invite with 190+ attendees. RSVP needed. Zoom link active.</p>
      <p><strong>HR Networking Group — Sept 2 (12–1:30 PM)</strong> — Larger session, team guidelines linked in description. RSVP needed.</p>
    </div>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="card card-yellow">
    <div class="card-label label-yellow">💳 FINANCIAL / BILLING — 3 EMAILS</div>
    <div class="card-title">Credit Cards, Banking &amp; Financial Offers</div>
    <div class="card-body">
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Chase</td><td>Credit card statement ready — (...8874), Min $35 due 9/23</td><td><span class="pill pill-red">Review &amp; Pay</span></td></tr>
          <tr><td>JetBlue Plus Card / Barclays</td><td>Activate 8.99% promo APR — ✅ Rescued from Trash</td><td><span class="pill pill-yellow">Review Offer</span></td></tr>
          <tr><td>Temu</td><td>Payment will be returned as Credit Back</td><td><span class="pill pill-gray">Low priority — note credit</span></td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- MEDICAL / HEALTH -->
  <div class="card card-red">
    <div class="card-label label-red">🏥 MEDICAL / HEALTH — 2 EMAILS (SPAM)</div>
    <div class="card-title">Unsolicited Health &amp; Medical Spam</div>
    <div class="card-body">
      <p><strong>"'GLP-1-by-DirectMeds'"</strong> — Fake Ozempic/Mounjaro prescription solicitation from gibberish domain. <strong>Do not engage.</strong></p>
      <p><strong>BambooHR</strong> — "[Updated for 2026] Your Open Enrollment Survival Kit" — Legitimate HR software newsletter. Relevant if you are planning open enrollment cycles. Low priority but keep if useful professionally.</p>
      <p><strong>Note:</strong> The two "Biblical Regimen" diabetes cure emails are classified under Security/Risk as they are scam campaigns, not legitimate health information.</p>
    </div>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="card card-purple">
    <div class="card-label label-purple">📚 PROFESSIONAL DEVELOPMENT — 5 EMAILS</div>
    <div class="card-title">AI, HR Strategy, Career Learning Resources</div>
    <div class="card-body">
      <table>
        <thead><tr><th>From / Source</th><th>Topic</th><th>Recommendation</th></tr></thead>
        <tbody>
          <tr><td>Self (Melissa W)</td><td>McKinsey — HR for the Agentic AI Era</td><td><span class="pill pill-green">Read Today</span></td></tr>
          <tr><td>Self (Melissa W)</td><td>AI prompts (LinkedIn)</td><td><span class="pill pill-green">Save &amp; Use</span></td></tr>
          <tr><td>Self (Melissa W)</td><td>AI tools for recruitment — talent-stack.io</td><td><span class="pill pill-green">Explore Site</span></td></tr>
          <tr><td>Self (Melissa W)</td><td>Claude Text Watermark — Learn AI With Mariah</td><td><span class="pill pill-green">Read</span></td></tr>
          <tr><td>Self (Melissa W)</td><td>ai resume help (ATS scanning prompt)</td><td><span class="pill pill-green">Use on Vaco/Atlassian JDs</span></td></tr>
        </tbody>
      </table>
      <p style="margin-top:8px;"><strong>Stanton Chase LinkedIn Article</strong> (in trash) — "Is Your Executive Leadership Still the Right Fit? Board Framework" — Restore for strategic reading.</p>
    </div>
  </div>

  <!-- PERSONAL -->
  <div class="card card-purple">
    <div class="card-label label-purple">👤 PERSONAL — 6 EMAILS</div>
    <div class="card-title">Dating Apps, Personal Research &amp; Self-Emails</div>
    <div class="card-body">
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Notes</th></tr></thead>
        <tbody>
          <tr><td>OkCupid</td><td>Someone likes you</td><td>In inbox. Personal — review at your leisure.</td></tr>
          <tr><td>Match</td><td>Profile view from Steve (56, Great Neck NY)</td><td>Read — personal.</td></tr>
          <tr><td>Match</td><td>Profile view from BestIsYetToCome (68, Great Neck NY)</td><td>Read — personal.</td></tr>
          <tr><td>ChatGPT / OpenAI</td><td>You now have access to Health in ChatGPT</td><td>New Apple Health integration — review if interested.</td></tr>
          <tr><td>Self (Melissa W)</td><td>Website (LinkedIn link)</td><td>Self-saved reference. Archive after review.</td></tr>
          <tr><td>Self (Melissa W)</td><td>Connect request (Claude AI share link)</td><td>Self-saved networking template. Archive after review.</td></tr>
        </tbody>
      </table>
      <p style="margin-top:8px;"><strong>Also:</strong> Self-email (no subject) — snippet about NY law on job posting intentions. Likely saved as a professional reference. Archive after review.</p>
    </div>
  </div>

  <!-- NEWSLETTERS -->
  <div class="card card-purple">
    <div class="card-label label-purple">📰 NEWSLETTERS / SUBSCRIPTIONS — 5 EMAILS</div>
    <div class="card-title">Digests, Newsletters &amp; Subscriptions</div>
    <div class="card-body">
      <p>See full Newsletters &amp; Subscriptions section below for detailed breakdown.</p>
      <ul class="item-list">
        <li>Medium Daily Digest — "China Classifies Single Women as Leftovers" (in trash)</li>
        <li>Medium / Pranit naik — "Apple Mac Mini M6 Buying Guide" (in trash)</li>
        <li>The Daily Skimm — "Baby's first physics lesson" (in trash)</li>
        <li>Gemma Bonham-Carter — "Is your content secretly watermarked?" (in trash)</li>
        <li>BambooHR — "Open Enrollment Survival Kit 2026"</li>
      </ul>
    </div>
  </div>

  <!-- PROMOTIONAL / RETAIL -->
  <div class="card card-gray">
    <div class="card-label label-gray">🛍 PROMOTIONAL / RETAIL — 7 EMAILS</div>
    <div class="card-title">Retail, Restaurant &amp; Shopping Promotions</div>
    <div class="card-body">
      <p>See full Promotional / Retail Summary section below. Senders include: Chick-fil-A, Kohl's, Old Navy, Gap Factory, Temu, and more. All low priority.</p>
    </div>
  </div>

  <!-- TRASH REVIEW -->
  <div class="card card-gray">
