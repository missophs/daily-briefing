html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa W. — August 15, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }

  .page-header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); color: white; padding: 32px 40px; }
  .page-header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .page-header .subtitle { font-size: 15px; color: #a8b8d8; margin-top: 6px; }
  .page-header .meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .page-header .meta-item { background: rgba(255,255,255,0.1); border-radius: 8px; padding: 10px 18px; }
  .page-header .meta-item .label { font-size: 10px; text-transform: uppercase; letter-spacing: 1px; color: #a8b8d8; }
  .page-header .meta-item .value { font-size: 20px; font-weight: 700; color: #fff; }

  .container { max-width: 1200px; margin: 0 auto; padding: 28px 20px; }

  .section { margin-bottom: 32px; }
  .section-header { display: flex; align-items: center; gap: 10px; margin-bottom: 16px; padding-bottom: 10px; border-bottom: 2px solid #e0e4ea; }
  .section-header h2 { font-size: 18px; font-weight: 700; color: #1a1a2e; }
  .section-number { background: #1a1a2e; color: white; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700; flex-shrink: 0; }

  /* Color themes */
  .red { border-left: 4px solid #dc2626; background: #fef2f2; }
  .yellow { border-left: 4px solid #d97706; background: #fffbeb; }
  .blue { border-left: 4px solid #2563eb; background: #eff6ff; }
  .green { border-left: 4px solid #16a34a; background: #f0fdf4; }
  .purple { border-left: 4px solid #7c3aed; background: #faf5ff; }
  .gray { border-left: 4px solid #6b7280; background: #f9fafb; }
  .orange { border-left: 4px solid #ea580c; background: #fff7ed; }

  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; }
  .card-title { font-size: 15px; font-weight: 700; margin-bottom: 4px; }
  .card-sub { font-size: 12px; color: #6b7280; margin-bottom: 8px; }
  .card-body { font-size: 13px; }
  .card-label { display: inline-block; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; padding: 2px 8px; border-radius: 20px; margin-bottom: 8px; }
  .label-red { background: #dc2626; color: white; }
  .label-yellow { background: #d97706; color: white; }
  .label-blue { background: #2563eb; color: white; }
  .label-green { background: #16a34a; color: white; }
  .label-purple { background: #7c3aed; color: white; }
  .label-gray { background: #6b7280; color: white; }
  .label-orange { background: #ea580c; color: white; }

  table { width: 100%; border-collapse: collapse; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
  th { background: #1a1a2e; color: white; padding: 10px 14px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
  td { padding: 9px 14px; border-bottom: 1px solid #e5e7eb; font-size: 13px; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #f8fafc; }
  tr:hover td { background: #eff6ff; }

  .badge { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; }
  .badge-red { background: #fee2e2; color: #dc2626; }
  .badge-yellow { background: #fef3c7; color: #92400e; }
  .badge-green { background: #dcfce7; color: #15803d; }
  .badge-blue { background: #dbeafe; color: #1d4ed8; }
  .badge-purple { background: #ede9fe; color: #6d28d9; }
  .badge-gray { background: #f3f4f6; color: #374151; }
  .badge-orange { background: #ffedd5; color: #c2410c; }

  .summary-box { background: white; border-radius: 10px; padding: 20px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
  .bullet-item { display: flex; gap: 10px; margin-bottom: 10px; padding: 10px; border-radius: 8px; }
  .bullet-icon { font-size: 18px; flex-shrink: 0; }
  .bullet-text strong { display: block; font-size: 14px; margin-bottom: 2px; }
  .bullet-text span { font-size: 13px; color: #4b5563; }

  .day-block { background: white; border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
  .day-label { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #6b7280; margin-bottom: 10px; }
  .event-row { display: flex; gap: 14px; padding: 10px 0; border-bottom: 1px solid #f0f0f0; align-items: flex-start; }
  .event-row:last-child { border-bottom: none; }
  .event-time { font-size: 12px; font-weight: 700; color: #2563eb; min-width: 110px; }
  .event-name { font-size: 14px; font-weight: 600; }
  .event-detail { font-size: 12px; color: #6b7280; margin-top: 3px; }
  .conflict-warn { font-size: 11px; color: #dc2626; font-weight: 700; margin-top: 4px; }

  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 14px; }
  .dash-card { background: white; border-radius: 10px; padding: 16px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); text-align: center; }
  .dash-card .number { font-size: 36px; font-weight: 800; }
  .dash-card .label { font-size: 12px; color: #6b7280; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px; }
  .dash-card.red .number { color: #dc2626; }
  .dash-card.green .number { color: #16a34a; }
  .dash-card.blue .number { color: #2563eb; }
  .dash-card.yellow .number { color: #d97706; }
  .dash-card.purple .number { color: #7c3aed; }

  .priority-tag { font-weight: 700; font-size: 12px; }
  .HIGH { color: #dc2626; }
  .MEDIUM { color: #d97706; }
  .LOW { color: #16a34a; }

  .top3 { counter-reset: top3; }
  .top3-item { display: flex; gap: 16px; align-items: flex-start; background: white; border-radius: 10px; padding: 18px 20px; margin-bottom: 12px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
  .top3-num { font-size: 32px; font-weight: 900; color: #1a1a2e; min-width: 40px; }
  .top3-content strong { font-size: 16px; display: block; margin-bottom: 4px; }
  .top3-content span { font-size: 13px; color: #4b5563; }

  .rescue-badge { display: inline-block; background: #dcfce7; color: #15803d; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 10px; margin-left: 6px; }
  .phish-badge { display: inline-block; background: #fee2e2; color: #dc2626; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 10px; margin-left: 6px; }

  .triage-status { white-space: nowrap; font-size: 13px; }
  .divider { height: 1px; background: #e5e7eb; margin: 24px 0; }

  .note-box { background: #fefce8; border: 1px solid #fde68a; border-radius: 8px; padding: 12px 16px; font-size: 13px; color: #78350f; margin-bottom: 14px; }
  .info-box { background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 12px 16px; font-size: 13px; color: #1e40af; margin-bottom: 14px; }

  @media (max-width: 700px) {
    .page-header { padding: 20px; }
    .page-header .meta { gap: 12px; }
    .container { padding: 16px 10px; }
    th, td { padding: 7px 8px; font-size: 12px; }
    .dashboard-grid { grid-template-columns: repeat(2, 1fr); }
  }
</style>
</head>
<body>

<!-- ═══════════════════════════════════════════════════════════ -->
<!--  PAGE HEADER                                               -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="page-header">
  <h1>☀️ Good Morning, Melissa</h1>
  <div class="subtitle">Executive Briefing — Prepared by Your Chief of Staff</div>
  <div class="meta">
    <div class="meta-item">
      <div class="label">Date</div>
      <div class="value">Saturday, August 15, 2026</div>
    </div>
    <div class="meta-item">
      <div class="label">Emails Reviewed</div>
      <div class="value">50</div>
    </div>
    <div class="meta-item">
      <div class="label">Calendar Events</div>
      <div class="value">7</div>
    </div>
    <div class="meta-item">
      <div class="label">Action Items</div>
      <div class="value">8</div>
    </div>
  </div>
</div>

<div class="container">

<!-- ═══════════════════════════════════════════════════════════ -->
<!--  SECTION 0: EMAIL TRIAGE QUICK LIST                        -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">0</div>
    <h2>Email Triage Quick List</h2>
  </div>
  <div class="info-box">📋 <strong>Reading Guide:</strong> ✅ RESCUED = pulled back from Trash (legitimate). 📥 INBOX = arrived in your inbox. Summary rows collapse all trash items for efficiency.</div>

  <table>
    <thead>
      <tr>
        <th style="width:130px;">Status</th>
        <th style="width:200px;">From</th>
        <th>Subject</th>
        <th>Summary</th>
      </tr>
    </thead>
    <tbody>
      <!-- RESCUED EMAILS — 10 -->
      <tr>
        <td class="triage-status">✅ <span class="rescue-badge">RESCUED</span></td>
        <td>Kohl's</td>
        <td>Part of your order is ready to ship!</td>
        <td>Kohl's shipment notification — legitimate purchase update. Pulled from Trash.</td>
      </tr>
      <tr>
        <td class="triage-status">✅ <span class="rescue-badge">RESCUED</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>Head of HR Business Partnering at Booking Holdings</td>
        <td>Strong job lead — actively recruiting. Pulled from Trash (protected sender).</td>
      </tr>
      <tr>
        <td class="triage-status">✅ <span class="rescue-badge">RESCUED</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>Head of People, Prism Media LLC at Soros Fund Management</td>
        <td>Senior HR leadership role — 6 school alumni. Pulled from Trash (protected sender).</td>
      </tr>
      <tr>
        <td class="triage-status">✅ <span class="rescue-badge">RESCUED</span></td>
        <td>Amazon.com</td>
        <td>Ordered: 2 Jewelry items</td>
        <td>Amazon order confirmation. Legitimate receipt. Pulled from Trash.</td>
      </tr>
      <tr>
        <td class="triage-status">✅ <span class="rescue-badge">RESCUED</span></td>
        <td>Match</td>
        <td>James likes you. See if it's mutual.</td>
        <td>Match.com activity notification. Protected sender — pulled from Trash.</td>
      </tr>
      <tr>
        <td class="triage-status">✅ <span class="rescue-badge">RESCUED</span></td>
        <td>Slack</td>
        <td>performance on Slack: New Account Details</td>
        <td>New "performance" workspace created. Legitimate setup email. Pulled from Trash.</td>
      </tr>
      <tr>
        <td class="triage-status">✅ <span class="rescue-badge">RESCUED</span></td>
        <td>Slack (feedback)</td>
        <td>monty just joined your workspace!</td>
        <td>Monte joined "performance" Slack workspace. Pulled from Trash.</td>
      </tr>
      <tr>
        <td class="triage-status">✅ <span class="rescue-badge">RESCUED</span></td>
        <td>Slack</td>
        <td>Slack confirmation code: NHI-EGQ</td>
        <td>Email verification code for Slack signup. Pulled from Trash.</td>
      </tr>
      <tr>
        <td class="triage-status">✅ <span class="rescue-badge">RESCUED</span></td>
        <td>Slack</td>
        <td>Melissa W has invited you to work with them in performance</td>
        <td>Workspace invitation for "performance." Pulled from Trash.</td>
      </tr>
      <tr>
        <td class="triage-status">✅ <span class="rescue-badge">RESCUED</span></td>
        <td>Google</td>
        <td>You shared some Google Account data with Slack (×2)</td>
        <td>Security notice: Google Sign-In used for Slack. Two instances. Pulled from Trash.</td>
      </tr>
      <!-- INBOX EMAILS — 13 -->
      <tr>
        <td class="triage-status">📥 INBOX</td>
        <td>Chase</td>
        <td>We've received your Chase Slate Visa payment</td>
        <td>Payment applied to Chase Slate Visa. ✔ Confirmed.</td>
      </tr>
      <tr>
        <td class="triage-status">📥 INBOX</td>
        <td>Cencora / Workday</td>
        <td>Thank you for your interest in Cencora</td>
        <td>⚠️ Rejection — Sr. HR Director, Americas (R2612894). Review pipeline.</td>
      </tr>
      <tr>
        <td class="triage-status">📥 INBOX</td>
        <td>IQVIA / Workday</td>
        <td>Your IQVIA Application for R1540601 Human Resources Director</td>
        <td>Application acknowledgment for HR Director role. Awaiting status.</td>
      </tr>
      <tr>
        <td class="triage-status">📥 INBOX</td>
        <td>Amazon.com</td>
        <td>Shipped: 1 Beauty item</td>
        <td>Beauty item shipped. Track delivery.</td>
      </tr>
      <tr>
        <td class="triage-status">📥 INBOX</td>
        <td>Amazon.com (return)</td>
        <td>Advance refund issued for UNCLECAT Womens Crop Tops</td>
        <td>Advance refund issued for return. Addressed to "Sophie" — verify if correct.</td>
      </tr>
      <tr>
        <td class="triage-status">📥 INBOX</td>
        <td>LinkedIn Job Alerts</td>
        <td>Chief Human Resources Officer — up to $350K/year</td>
        <td>CHRO role at Confidential company. 2 school alumni. High-value lead.</td>
      </tr>
      <tr>
        <td class="triage-status">📥 INBOX</td>
        <td>LinkedIn Job Alerts</td>
        <td>HR Business Partner Manager, AAI at Meta — up to $255K/year</td>
        <td>Meta HRBP Manager role. 1 connection. Strong opportunity.</td>
      </tr>
      <tr>
        <td class="triage-status">📥 INBOX</td>
        <td>LinkedIn Job Alerts</td>
        <td>Chief People Officer at Johnson Lambert LLP — up to $240K/year</td>
        <td>CPO role at Johnson Lambert LLP. Review fit.</td>
      </tr>
      <tr>
        <td class="triage-status">📥 INBOX</td>
        <td>Slack</td>
        <td>Trying to sign in to Slack? Use this password-free link.</td>
        <td>Magic link for Slack sign-in. Use immediately or ignore if already signed in.</td>
      </tr>
      <tr>
        <td class="triage-status">📥 INBOX</td>
        <td>Melissa (self)</td>
        <td>Performance Pulse is live in Slack</td>
        <td>Self-sent note to Monte: 1:1 check-in app active in Slack.</td>
      </tr>
      <tr>
        <td class="triage-status">📥 INBOX</td>
        <td>Macy's</td>
        <td>We're processing your credit #4779883290</td>
        <td>Macy's return credit being processed. Track refund.</td>
      </tr>
      <tr>
        <td class="triage-status">📥 INBOX</td>
        <td>Amazon.com</td>
        <td>Shipped: 2 Jewelry items</td>
        <td>Two jewelry items shipped. Track delivery.</td>
      </tr>
      <tr>
        <td class="triage-status">📥 INBOX</td>
        <td>Bank of America</td>
        <td>Your statement is available</td>
        <td>Money Market Savings #7633 statement ready. Review when convenient.</td>
      </tr>
      <!-- SUMMARY ROWS -->
      <tr style="background:#fff7ed;">
        <td class="triage-status"><span class="phish-badge">🗑 AUTO-TRASHED</span></td>
        <td colspan="3"><strong>4 emails auto-trashed (phishing/spam)</strong> — Fake CashApp, fake cloud storage alerts, adult spam. See Trash Review for details.</td>
      </tr>
      <tr style="background:#f9fafb;">
        <td class="triage-status">🗂 TRASH (manual)</td>
        <td colspan="3"><strong>~23 emails in Trash</strong> — Retail promos (SHEIN, Old Navy, Kohl's, VIVAIA), casino spam, newsletters, job digests. See Trash Review for details.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!--  SECTION 1: HEADER (embedded in page-header above)        -->
<!--  SECTION 2: EXECUTIVE SUMMARY                             -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">2</div>
    <h2>Executive Summary</h2>
  </div>
  <div class="summary-box">
    <div class="bullet-item red" style="border-radius:8px; padding:12px 14px;">
      <div class="bullet-icon">🔴</div>
      <div class="bullet-text">
        <strong>SECURITY RISK: Multiple phishing emails detected in non-trash folders</strong>
        <span>4 emails were auto-trashed as high-confidence phishing (fake CashApp, fake cloud payment alerts, adult spam). Several more dangerous emails (casino scams, fake "F*ckMeHard" senders, fake Dr. Eleanor Sterling) remain in non-trash, non-inbox folders and need manual action. Also note: a Slack magic-link sign-in email arrived in your inbox — verify you initiated it.</span>
      </div>
    </div>
    <div class="bullet-item green" style="border-radius:8px; padding:12px 14px; margin-top:8px;">
      <div class="bullet-icon">🟢</div>
      <div class="bullet-text">
        <strong>JOB SEARCH: Three high-value LinkedIn alerts plus one rejection to process</strong>
        <span>A CHRO role paying up to $350K/year, a Meta HRBP Manager at $255K, a CPO at Johnson Lambert LLP ($240K), Head of HR at Booking Holdings (actively recruiting), and Head of People at Soros Fund Management are all live. Cencora rejected your application — update your pipeline accordingly. IQVIA acknowledgment received but no decision yet.</span>
      </div>
    </div>
    <div class="bullet-item blue" style="border-radius:8px; padding:12px 14px; margin-top:8px;">
      <div class="bullet-icon">🔵</div>
      <div class="bullet-text">
        <strong>CALENDAR: Three events next week need your RSVP or attention</strong>
        <span>Stella's vet appointment (Tue 8/18, 10–11 AM) has a duplicate entry — confirm which is correct. HR Networking Zoom (Wed 8/19, 12–1:30 PM) and Open Office Hours (Thu 8/20, 12–1 PM) both show "needsAction" — RSVP required. Executive Roundtable (Thu 8/20, 9–10:30 AM) is declined but conflicts with Open Office Hours — review. M&M meeting with Monte (Wed 8/19, 2–3 PM) is confirmed.</span>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!--  SECTION 3: ACTION REQUIRED                               -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">3</div>
    <h2>Action Required</h2>
  </div>

  <div class="card red">
    <span class="card-label label-red">🔴 SECURITY — URGENT</span>
    <div class="card-title">Verify Slack Magic-Link Sign-In</div>
    <div class="card-sub">Source: Slack &lt;no-reply-l8Nw6HxEaAW4QIlLvpSjab5l@slack.com&gt; · Aug 15, 6:29 AM</div>
    <div class="card-body"><strong>Why it matters:</strong> A password-free sign-in link for Slack arrived in your inbox. If you didn't initiate this login, someone else may be attempting to access your account.<br><strong>Next step:</strong> If you requested it, use it now (links expire). If not, ignore and go to Slack Security Settings → revoke active sessions → change your password.<br><strong>Due:</strong> Today — links expire quickly.</div>
  </div>

  <div class="card red">
    <span class="card-label label-red">🔴 SECURITY — SPAM CLEANUP</span>
    <div class="card-title">Delete Dangerous Phishing Emails Still in Non-Inbox/Non-Trash Folders</div>
    <div class="card-sub">Multiple senders with random domains · Aug 14–15, 2026</div>
    <div class="card-body"><strong>Why it matters:</strong> Several scam/phishing emails are not in inbox but also not trashed: casino scams, fake equity/CashApp offers, adult spam with your username. These should be permanently deleted and senders blocked.<br><strong>Next step:</strong> Open Gmail → search "is:spam" and "label:all" → delete/block: "F*ckMeHard," "Congratulations🎉," "Sex Trick🔞," fake CashApp, fake Dr. Eleanor Sterling, fake equity team, Slots of Vegas.<br><strong>Due:</strong> Today.</div>
  </div>

  <div class="card yellow">
    <span class="card-label label-yellow">🟡 FOLLOW-UP — JOB SEARCH</span>
    <div class="card-title">Update Job Application Pipeline — Cencora Rejection</div>
    <div class="card-sub">Source: Cencora / Workday · Aug 15, 8:24 AM</div>
    <div class="card-body"><strong>Why it matters:</strong> You were not selected for the Sr. HR Director, Americas role (R2612894) at Cencora. Pipeline needs updating.<br><strong>Next step:</strong> Log rejection in your tracker. Review remaining pipeline gaps. Prioritize the CHRO ($350K), Meta HRBP ($255K), Booking Holdings, and Soros leads.<br><strong>Due:</strong> Today / Weekend.</div>
  </div>

  <div class="card yellow">
    <span class="card-label label-yellow">🟡 RSVP REQUIRED</span>
    <div class="card-title">RSVP: HR Networking & Job Search Group — Zoom (Wed Aug 19)</div>
    <div class="card-sub">Source: Google Calendar · needsAction</div>
    <div class="card-body"><strong>Why it matters:</strong> 170+ HR professionals on the invite. This is a core networking event tied to your job search. Status shows "needsAction."<br><strong>Next step:</strong> Accept the calendar invite. Prepare a 30-second update on your search status. Review attendee list for warm contacts.<br><strong>Due:</strong> ASAP — meeting is Wednesday Aug 19.</div>
  </div>

  <div class="card yellow">
    <span class="card-label label-yellow">🟡 RSVP REQUIRED</span>
    <div class="card-title">RSVP: HR Networking Open Office Hours — Zoom (Thu Aug 20)</div>
    <div class="card-sub">Source: Google Calendar · needsAction</div>
    <div class="card-body"><strong>Why it matters:</strong> Open discussion session — no recording tools. Strong peer support opportunity. Status is "needsAction" and conflicts with Executive Roundtable slot (already declined).<br><strong>Next step:</strong> Accept invite. Note: no conflict since Roundtable is already declined.<br><strong>Due:</strong> ASAP — meeting is Thursday Aug 20.</div>
  </div>

  <div class="card green">
    <span class="card-label label-green">🟢 OPPORTUNITY</span>
    <div class="card-title">Review & Apply: CHRO Role — up to $350K/year (Confidential)</div>
    <div class="card-sub">Source: LinkedIn Job Alerts · Aug 15, 7:05 AM</div>
    <div class="card-body"><strong>Why it matters:</strong> Highest-compensation role in today's alerts. 2 school alumni at the company = warm network path.<br><strong>Next step:</strong> Open LinkedIn alert, research company, leverage alumni connections, tailor resume, apply.<br><strong>Due:</strong> This weekend.</div>
  </div>

  <div class="card green">
    <span class="card-label label-green">🟢 OPPORTUNITY</span>
    <div class="card-title">Review & Apply: HR Business Partner Manager, AAI at Meta — up to $255K/year</div>
    <div class="card-sub">Source: LinkedIn Job Alerts · Aug 15, 5:05 AM</div>
    <div class="card-body"><strong>Why it matters:</strong> Meta FAANG-level role with 1 direct connection. High visibility, top compensation.<br><strong>Next step:</strong> Reach out to your connection at Meta first. Apply via LinkedIn with tailored cover note.<br><strong>Due:</strong> This weekend.</div>
  </div>

  <div class="card blue">
    <span class="card-label label-blue">🔵 CALENDAR</span>
    <div class="card-title">Resolve Duplicate Vet Appointment (Tue Aug 18)</div>
    <div class="card-sub">Source: Google Calendar — "Vet" + "Stella vet" both 10:00–11:00 AM</div>
    <div class="card-body"><strong>Why it matters:</strong> Two identical calendar events exist for the same time slot. May cause confusion or double-booking.<br><strong>Next step:</strong> Delete one duplicate entry (likely "Vet" is redundant if "Stella vet" is the specific one).<br><strong>Due:</strong> Before Tuesday Aug 18.</div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!--  SECTION 4: FULL 7-DAY CALENDAR                           -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">4</div>
    <h2>Full 7-Day Calendar (Aug 15–21, 2026)</h2>
  </div>

  <!-- Saturday Aug 15 -->
  <div class="day-block">
    <div class="day-label">📅 Saturday, August 15, 2026 — TODAY</div>
    <div class="event-row">
      <div class="event-time">All Day</div>
      <div>
        <div class="event-name">No scheduled events</div>
        <div class="event-detail">Use today for job applications, pipeline review, and inbox cleanup.</div>
      </div>
    </div>
  </div>

  <!-- Sunday Aug 16 -->
  <div class="day-block">
    <div class="day-label">📅 Sunday, August 16, 2026</div>
    <div class="event-row">
      <div class="event-time">All Day</div>
      <div>
        <div class="event-name">No scheduled events</div>
        <div class="event-detail">Prep day for the week ahead — review job leads, prepare for Wednesday networking call.</div>
      </div>
    </div>
  </div>

  <!-- Monday Aug 17 -->
  <div class="day-block">
    <div class="day-label">📅 Monday, August 17, 2026</div>
    <div class="event-row">
      <div class="event-time">All Day</div>
      <div>
        <div class="event-name">No scheduled events</div>
        <div class="event-detail">Clear calendar. Good day for outreach to LinkedIn connections at Meta and CHRO target company.</div>
      </div>
    </div>
  </div>

  <!-- Tuesday Aug 18 -->
  <div class="day-block">
    <div class="day-label">📅 Tuesday, August 18, 2026</div>
    <div class="event-row">
      <div class="event-time">10:00 – 11:00 AM</div>
      <div>
        <div class="event-name">🐾 Vet Appointment <span class="badge badge-blue">CONFIRMED</span></div>
        <div class="event-detail"><strong>Event:</strong> "Vet" (generic)</div>
        <div class="event-detail">Location: Not specified | No attendees listed</div>
        <div class="event-detail">Prep: Bring Stella's health records, list any concerns.</div>
        <div class="conflict-warn">⚠️ DUPLICATE: "Stella vet" also scheduled at exact same time — delete one entry.</div>
      </div>
    </div>
    <div class="event-row">
      <div class="event-time">10:00 – 11:00 AM</div>
      <div>
        <div class="event-name">🐾 Stella Vet <span class="badge badge-blue">CONFIRMED</span></div>
        <div class="event-detail"><strong>Event:</strong> "Stella vet" — likely the primary/specific entry</div>
        <div class="event-detail">Location: Not specified | No attendees listed</div>
        <div class="conflict-warn">⚠️ DUPLICATE of "Vet" above — remove one. Recommend keeping this one as it names Stella specifically.</div>
      </div>
    </div>
  </div>

  <!-- Wednesday Aug 19 -->
  <div class="day-block">
    <div class="day-label">📅 Wednesday, August 19, 2026</div>
    <div class="event-row">
      <div class="event-time">12:00 – 1:30 PM</div>
      <div>
        <div class="event-name">💼 HR Networking & Job Search Group — Zoom 2 <span class="badge badge-yellow">NEEDS RSVP</span></div>
        <div class="event-detail">Status: needsAction | ~170 attendees</div>
        <div class="event-detail">📹 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" style="color:#2563eb;">Join Zoom</a></div>
        <div class="event-detail">Prep: Review team guidelines linked in invite. Prepare 30-second job search update. Review attendee list for warm contacts. Check HR Networking Team Google Doc.</div>
        <div class="conflict-warn">⚡ Also shows as "Network" on calendar at same time — appears to be same event. Consolidate.</div>
      </div>
    </div>
    <div class="event-row">
      <div class="event-time">12:00 – 1:30 PM</div>
      <div>
        <div class="event-name">🌐 Network <span class="badge badge-blue">CONFIRMED</span></div>
        <div class="event-detail">Status: accepted | No attendees listed separately</div>
        <div class="event-detail">Likely same session as "HR Networking & Job Search Group" above — verify and merge if duplicate.</div>
      </div>
    </div>
    <div class="event-row">
      <div class="event-time">2:00 – 3:00 PM</div>
      <div>
        <div class="event-name">👥 M&M (with Monte Montoya) <span class="badge badge-blue">ACCEPTED</span></div>
        <div class="event-detail">Status: accepted | Attendee: monte.montoya@gmail.com</div>
        <div class="event-detail">Location: Not specified</div>
        <div class="event-detail">Prep: Performance Pulse is now active in Slack ("performance" workspace). Review Monte's recent check-in data before the call. This may be a 1:1 performance or coaching session.</div>
      </div>
    </div>
  </div>

  <!-- Thursday Aug 20 -->
  <div class="day-block">
    <div class="day-label">📅 Thursday, August 20, 2026</div>
    <div class="event-row">
      <div class="event-time">9:00 – 10:30 AM</div>
      <div>
        <div class="event-name">🎤 Executive Roundtable (John Madigan) <span class="badge badge-red">DECLINED</span></div>
        <div class="event-detail">Status: declined | No additional attendees listed</div>
        <div class="event-detail">📹 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" style="color:#2563eb;">Join Zoom</a> | Meeting ID: 207 786 667 | PW: 205454</div>
        <div class="event-detail">Note: You have declined this event. No conflict with Open Office Hours (12 PM). If you wish to reconsider, reach out to John Madigan.</div>
      </div>
    </div>
    <div class="event-row">
      <div class="event-time">12:00 – 1:00 PM</div>
      <div>
        <div class="event-name">💼 HR Networking & Job Search: Open Office Hours — Zoom 2 <span class="badge badge-yellow">NEEDS RSVP</span></div>
        <div class="event-detail">Status: needsAction | ~170 attendees</div>
        <div class="event-detail">📹 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" style="color:#2563eb;">Join Zoom</a></div>
        <div class="event-detail">Prep: No AI notetaking tools allowed. Open discussion format. Good for candid conversation about job search strategy. No conflict since Roundtable is declined.</div>
      </div>
    </div>
  </div>

  <!-- Friday Aug 21 -->
  <div class="day-block">
    <div class="day-label">📅 Friday, August 21, 2026</div>
    <div class="event-row">
      <div class="event-time">All Day</div>
      <div>
        <div class="event-name">No scheduled events</div>
        <div class="event-detail">End-of-week follow-ups on job applications and networking from Wednesday's session.</div>
      </div>
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!--  SECTION 5: JOB SEARCH & INTERVIEW PIPELINE               -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">5</div>
    <h2>Job Search &amp; Interview Pipeline</h2>
  </div>

  <table>
    <thead>
      <tr>
        <th>Fit</th>
        <th>Role / Company</th>
        <th>Source</th>
        <th>Comp Range</th>
        <th>Status</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="badge badge-green">HIGH</span></td>
        <td><strong>Chief Human Resources Officer</strong><br>Confidential Company</td>
        <td>LinkedIn Job Alert</td>
        <td>Up to $350K/yr</td>
        <td><span class="badge badge-yellow">New Alert</span></td>
        <td>Review alumni connections. Apply this weekend.</td>
      </tr>
      <tr>
        <td><span class="badge badge-green">HIGH</span></td>
        <td><strong>HR Business Partner Manager, AAI</strong><br>Meta</td>
        <td>LinkedIn Job Alert</td>
        <td>Up to $255K/yr</td>
        <td><span class="badge badge-yellow">New Alert</span></td>
        <td>1 connection at Meta — reach out first, then apply.</td>
      </tr>
      <tr>
        <td><span class="badge badge-green">HIGH</span></td>
        <td><strong>Head of HR Business Partnering</strong><br>Booking Holdings (NASDAQ: BKNG)</td>
        <td>LinkedIn Job Alert ✅ Rescued</td>
        <td>Not listed</td>
        <td><span class="badge badge-green">Actively Recruiting</span></td>
        <td>Actively hiring — apply now. Global travel company.</td>
      </tr>
      <tr>
        <td><span class="badge badge-green">HIGH</span></td>
        <td><strong>Head of People, Prism Media LLC</strong><br>Soros Fund Management</td>
        <td>LinkedIn Job Alert ✅ Rescued</td>
        <td>Not listed</td>
        <td><span class="badge badge-yellow">New Alert</span></td>
        <td>6 school alumni. Leverage network. Review immediately.</td>
      </tr>
      <tr>
        <td><span class="badge badge-blue">MEDIUM</span></td>
        <td><strong>Chief People Officer</strong><br>Johnson Lambert LLP</td>
        <td>LinkedIn Job Alert</td>
        <td>Up to $240K/yr</td>
        <td><span class="badge badge-yellow">New Alert</span></td>
        <td>CPO level — assess firm size and fit before applying.</td>
      </tr>
      <tr>
        <td><span class="badge badge-blue">MEDIUM</span></td>
        <td><strong>Human Resources Director</strong><br>IQVIA (R1540601)</td>
        <td>Workday / IQVIA</td>
        <td>Not listed</td>
        <td><span class="badge badge-blue">Applied — Acknowledged</span></td>
        <td>Acknowledgment received. Await decision. Follow up in 1–2 weeks.</td>
      </tr>
      <tr>
        <td><span class="badge badge-gray">CLOSED</span></td>
        <td><strong>Sr. Human Resources Director, Americas</strong><br>Cencora (R2612894)</td>
        <td>Workday / Cencora</td>
        <td>Not listed</td>
        <td><span class="badge badge-red">Rejected</span></td>
        <td>Log rejection. Pipeline closed for this role.</td>
      </tr>
      <tr>
        <td><span class="badge badge-blue">MEDIUM</span></td>
        <td><strong>Chief People Officer + 5 other roles</strong><br>Various (JobLeads digest)</td>
        <td>JobLeads (in Trash)</td>
        <td>Varies</td>
        <td><span class="badge badge-gray">In Trash — Review</span></td>
        <td>Check JobLeads digest for Aug 14 — 5 new CPO/Culture/Talent roles.</td>
      </tr>
    </tbody>
  </table>

  <div class="card purple" style="margin-top:14px;">
    <span class="card-label label-purple">NETWORKING</span>
    <div class="card-title">Ashok Jambur, Mentor — Popular in Your Network</div>
    <div class="card-sub">Source: LinkedIn · Aug 15, 4:41 AM</div>
    <div class="card-body">LinkedIn flagged Ashok Jambur (Mentor) as popular in your network. Review their profile — may be a warm path to opportunities or mentorship support during your job search.</div>
  </div>

  <div class="card purple" style="margin-top:0;">
    <span class="card-label label-purple">NETWORKING</span>
    <div class="card-title">HR Professional at MH Markets — LinkedIn Connection Suggestion</div>
    <div class="card-sub">Source: LinkedIn (in Trash) · Aug 15, 2:41 AM</div>
    <div class="card-body">LinkedIn suggested someone in HR at MH Markets. Potentially useful industry connection. Rescue from Trash if relevant to your pipeline.</div>
  </div>

  <div class="card blue" style="margin-top:0;">
    <span class="card-label label-blue">NETWORKING EVENT</span>
    <div class="card-title">HR Networking & Job Search Group — Wed Aug 19 + Thu Aug 20</div>
    <div class="card-sub">Source: Google Calendar</div>
    <div class="card-body">170+ HR professionals across both sessions. Strong community for leads, referrals, and peer support. RSVP required for both (currently "needsAction").</div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!--  SECTION 6: FULL EMAIL REVIEW BY CATEGORY                 -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">6</div>
    <h2>Full Email Review by Category</h2>
  </div>

  <!-- SECURITY / RISK -->
  <div class="card red">
    <span class="card-label label-red">🔴 Security / Risk</span>
    <div class="card-title">11 Emails — Phishing, Spam, Impersonation, Adult Content</div>
    <div class="card-body">
      <table style="margin-top:8px;">
        <thead><tr><th>Type</th><th>Sender / Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td><span class="badge badge-red">AUTO-TRASHED</span></td><td>Fake CashApp — "Please_CONFIRM #2128410707668" ($13,963.99 fake payment)</td><td>Auto-trashed — phishing</td><td>None required — already removed.</td></tr>
          <tr><td><span class="badge badge-red">AUTO-TRASHED</span></td><td>Fake Payment-System — "URGENT: Renewal attempt failed" (fake cloud storage)</td><td>Auto-trashed — phishing</td><td>None required — already removed.</td></tr>
          <tr><td><span class="badge badge-red">AUTO-TRASHED</span></td><td>Fake Payment-Declined — "Your Account Has been Blocked!" (fake cloud storage)</td><td>Auto-trashed — phishing</td><td>None required — already removed.</td></tr>
          <tr><td><span class="badge badge-red">SPAM</span></td><td>"F*ckMeHard" (×2 senders, random domains) — adult/sex spam targeting melissaw212</td><td>Not in inbox, not trashed</td><td>Delete immediately. Block sender domains.</td></tr>
          <tr><td><span class="badge badge-red">SPAM</span></td><td>"Sex Trick🔞" — fake Mia Kalifa TikTok viral adult spam</td><td>Not in inbox, not trashed</td><td>Delete immediately. Block sender.</td></tr>
          <tr><td><span class="badge badge-red">SPAM</span></td><td>Fake Dr. Eleanor Sterling — men's "performance" spam</td><td>In Trash</td><td>Already in Trash — permanently delete.</td></tr>
          <tr><td><span class="badge badge-red">SPAM</span></td><td>zisupportxtz — "$20 Free Chip Pending" (casino, uses your username)</td><td>Not in inbox, not trashed</td><td>Delete. Block. Uses your Gmail username — concerning.</td></tr>
          <tr><td><span class="badge badge-red">SPAM</span></td><td>Fake CashApp (styled) — "You received a direct deposited $2,500" (Slots of Vegas)</td><td>Not in inbox, not trashed</td><td>Delete immediately.</td></tr>
          <tr><td><span class="badge badge-red">SPAM</span></td><td>Fake Equity Team — "Tap into your equity without refinancing" (random domain)</td><td>Not in inbox, not trashed</td><td>Delete. Block domain.</td></tr>
          <tr><td><span class="badge badge-red">SPAM</span></td><td>"Watch this Alone" — Kevin Costner viral recipe spam (random domain)</td><td>Not in inbox, not trashed</td><td>Delete. Block.</td></tr>
          <tr><td><span class="badge badge-yellow">VERIFY</span></td><td>Slack — Password-free magic link (no-reply-l8Nw6HxEaAW4QIlLvpSjab5l@slack.com)</td><td>In Inbox</td><td>Verify you initiated this login. If not, revoke sessions.</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- JOB SEARCH -->
  <div class="card green">
    <span class="card-label label-green">🟢 Job Search</span>
    <div class="card-title">8 Emails — Alerts, Applications, Rejections</div>
    <div class="card-body">
      <strong>Key emails:</strong><br>
      • LinkedIn: CHRO (Confidential, $350K) — Inbox — Review &amp; Apply<br>
      • LinkedIn: Meta HRBP Manager, AAI ($255K) — Inbox — Apply<br>
      • LinkedIn: CPO at Johnson Lambert LLP ($240K) — Inbox — Review<br>
      • LinkedIn: Head of HR Business Partnering, Booking Holdings ✅ Rescued — Apply<br>
      • LinkedIn: Head of People, Soros Fund Management ✅ Rescued — Apply<br>
      • IQVIA Workday: Application acknowledged (R1540601 HR Director) — Inbox — Await<br>
      • Cencora Workday: Rejection (Sr. HR Director, Americas R2612894) — Inbox — Log &amp; Move on<br>
      • JobLeads: 5 new CPO/Talent/Culture roles for Aug 14 — In Trash — Review before deleting<br>
      <br><strong>Recommended action:</strong> Prioritize CHRO and Meta applications this weekend. Log Cencora rejection. Review JobLeads digest before deleting.
    </div>
  </div>

  <!-- RECRUITERS / NETWORKING -->
  <div class="card purple">
    <span class="card-label label-purple">🟣 Recruiters / Networking</span>
    <div class="card-title">2 Emails — LinkedIn Network Activity</div>
    <div class="card-body">
      • LinkedIn: Ashok Jambur, Mentor — popular in your network (not in inbox, not trashed) — Review profile<br>
      • LinkedIn: Someone at MH Markets you may know (HR Manager) — In Trash — Consider connecting<br>
      <br><strong>Recommended action:</strong> Check Ashok Jambur's profile. Rescue MH Markets contact if relevant.
    </div>
  </div>

  <!-- CALENDAR / EVENTS -->
  <div class="card blue">
    <span class="card-label label-blue">🔵 Calendar / Events</span>
    <div class="card-title">0 Standalone Emails — All calendar items are in Google Calendar data above</div>
    <div class="card-body">All scheduling information reviewed directly from Calendar Data. See Section 4 (Full 7-Day Calendar) for complete event details.</div>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="card yellow">
    <span class="card-label label-yellow">🟡 Financial / Billing</span>
    <div class="card-title">4 Emails — Payments, Statements, Refunds</div>
    <div class="card-body">
      • Chase: "We've received your Chase Slate Visa payment" — Inbox — ✔ Applied. No action needed.<br>
      • Bank of America: "Your statement is available" (Money Market Savings #7633) — Not in inbox, not trashed — Review statement when convenient.<br>
      • Macy's: "We're processing your credit #4779883290" — Inbox — Refund in process. Track arrival.<br>
      • Amazon return: "Advance refund issued for UNCLECAT Womens Crop Tops" — Inbox — Note: addressed to "Sophie" — verify this is your account/order.<br>
      <br><strong>Recommended action:</strong> Verify Amazon refund (Sophie name). Track Macy's credit. Review BofA statement.
    </div>
  </div>

  <!-- SLACK / PROFESSIONAL TOOLS -->
  <div class="card purple">
    <span class="card-label label-purple">🟣 Professional Tools — Slack Activity</span>
    <div class="card-title">7 Emails — Slack Workspace Setup ("performance")</div>
    <div class="card-body">
      • ✅ Rescued: Slack — New Account Details for "performance" workspace<br>
      • ✅ Rescued: Slack — monty just joined your workspace (Monte Montoya)<br>
      • ✅ Rescued: Slack — Confirmation code NHI-EGQ<br>
      • ✅ Rescued: Slack — Melissa W invited you to "performance"<br>
      • ✅ Rescued: Google — You shared Google Account data with Slack (×2 emails, Aug 14 and 15)<br>
      • 📥 Inbox: Slack — Password-free sign-in magic link (⚠️ verify you initiated)<br>
      • 📥 Inbox: Melissa (self) — "Performance Pulse is live in Slack" (sent to Monte)<br>
      <br><strong>Summary:</strong> You set up a Slack workspace called "performance" and invited Monte Montoya. Performance Pulse (1:1 check-in app) is active. Magic-link sign-in email in inbox — verify if you initiated.<br>
      <strong>Recommended action:</strong> Confirm magic-link login. Prepare Performance Pulse data for M&M meeting (Wed Aug 19, 2 PM).
    </div>
  </div>

  <!-- PERSONAL -->
  <div class="card gray">
    <span class="card-label label-gray">Personal</span>
    <div class="card-title">3 Emails — Personal Shopping, Dating, Pet</div>
    <div class="card-body">
      • Amazon: 2 Jewelry items shipped (in Inbox) — Track delivery<br>
      • Amazon: 1 Beauty item shipped (in Inbox) — Track delivery<br>
      • Amazon: 2 Jewelry items ordered ✅ Rescued from Trash — Order confirmed<br>
      • Match: "James likes you" ✅ Rescued — Personal notification<br>
      • Vet/Stella vet: Calendar events (Tue Aug 18) — Pet appointment<br>
      <br><strong>Recommended action:</strong> Track Amazon deliveries. Check Match profile when time permits.
    </div>
  </div>

  <!-- NEWSLETTERS -->
  <div class="card purple">
    <span class="card-label label-purple">🟣 Newsletters / Subscriptions</span>
    <div class="card-title">2 Emails — Financial Newsletter, Misc</div>
    <div class="card-body">
      • Dylan's Diary (Behind the Markets): "Elon just confirmed a fourth data center" — In Trash — Financial/tech newsletter. Unsubscribe or keep based on relevance.<br>
      • Amazon Music: "You received 90 days FREE with your purchase" — In Trash — Promotional perk notification.<br>
      <br><strong>Recommended action:</strong> Unsubscribe from Dylan's Diary if not regularly reading. Amazon Music free trial — activate or ignore.
    </div>
  </div>

  <!-- PROMOTIONAL / RETAIL -->
  <div class="card gray">
    <span class="card-label label-gray">Promotional / Retail</span>
    <div class="card-title">13 Emails — SHEIN, Old Navy, Kohl's, VIVAIA, Chick-fil-A, Others</div>
    <div class="card-body">See Section 8 — Promotional / Retail Summary for full breakdown. All in Trash or safely ignored.</div>
  </div>

  <!-- SAFE TO DELETE -->
  <div class="card gray">
    <span class="card-label label-gray">Safe to Delete / Ignore</span>
    <div class="card-title">Casino Spam, Fake Offers, Adult Spam — 7+ Emails</div>
    <div class="card-body">
      • "Congratulations🎉" — Lucky Creek Casino ($7,500 package) — In Trash — Delete<br>
      • OnlineCasino — Raging Bull Casino 100 Free Spins — In Trash — Delete<br>
      • All casino/gambling spam emails — Permanently delete and block domains<br>
      <br><strong>Recommended action:</strong> Bulk delete all casino/gambling spam permanently.
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!--  SECTION 7: TRASH REVIEW                                  -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">7</div>
    <h2>Trash Review</h2>
  </div>

  <!-- RESTORE -->
  <div class="card green" style="margin-bottom:14px;">
    <span class="card-label label-green">✅ RESTORE IMMEDIATELY</span>
    <div class="card-title">Already Rescued (10 emails) — No Action Needed</div>
    <div class="card-body">
      These were automatically pulled from Trash before this briefing was prepared:
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Reason</th></tr></thead>
        <tbody>
          <tr><td>Kohl's</td><td>Part of your order is ready to ship!</td><td>Legitimate purchase/shipment update</td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>Head of HR Business Partnering — Booking Holdings</td><td>Protected sender — job lead</td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>Head of People at Soros Fund Management</td><td>Protected sender — job lead</td></tr>
          <tr><td>Amazon.com</td><td>Ordered: 2 Jewelry items</td><td>Legitimate order confirmation</td></tr>
          <tr><td>Match</td><td>James likes you</td><td>Protected sender — personal</td></tr>
          <tr><td>Slack</td><td>performance on Slack: New Account Details</td><td>Legitimate workspace setup</td></tr>
          <tr><td>Slack (feedback)</td><td>monty just joined your workspace!</td><td>Legitimate workspace
