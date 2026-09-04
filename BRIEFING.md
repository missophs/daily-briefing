html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa — Friday, September 4, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: white; border-radius: 16px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 15px; color: #a8b8d8; margin-top: 6px; }
  .header .meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.1); border-radius: 8px; padding: 8px 16px; font-size: 13px; }
  .header .meta-item span { font-weight: 700; font-size: 18px; display: block; color: #7dd3fc; }

  /* SECTION TITLES */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; padding: 10px 16px; border-radius: 8px 8px 0 0; letter-spacing: 0.3px; display: flex; align-items: center; gap: 8px; }
  .section-body { background: white; border-radius: 0 0 12px 12px; padding: 18px; border: 1px solid #e2e8f0; border-top: none; }

  /* COLOR THEMES */
  .red    { background: #dc2626; color: white; }
  .yellow { background: #d97706; color: white; }
  .blue   { background: #2563eb; color: white; }
  .green  { background: #16a34a; color: white; }
  .purple { background: #7c3aed; color: white; }
  .gray   { background: #64748b; color: white; }
  .teal   { background: #0891b2; color: white; }
  .slate  { background: #334155; color: white; }
  .orange { background: #ea580c; color: white; }

  .red-border   { border-left: 4px solid #dc2626; }
  .yellow-border{ border-left: 4px solid #d97706; }
  .blue-border  { border-left: 4px solid #2563eb; }
  .green-border { border-left: 4px solid #16a34a; }
  .purple-border{ border-left: 4px solid #7c3aed; }
  .gray-border  { border-left: 4px solid #94a3b8; }
  .orange-border{ border-left: 4px solid #ea580c; }

  /* CARDS */
  .card { background: #f8fafc; border-radius: 10px; padding: 14px 16px; margin-bottom: 12px; border: 1px solid #e2e8f0; }
  .card:last-child { margin-bottom: 0; }
  .card-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; }
  .card-title { font-size: 15px; font-weight: 700; margin-bottom: 4px; }
  .card-row { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 4px; }
  .card-field { font-size: 12px; color: #64748b; }
  .card-field strong { color: #1a1a2e; }
  .badge { display: inline-block; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 99px; text-transform: uppercase; }
  .badge-red    { background: #fee2e2; color: #dc2626; }
  .badge-yellow { background: #fef3c7; color: #92400e; }
  .badge-green  { background: #dcfce7; color: #16a34a; }
  .badge-blue   { background: #dbeafe; color: #1d4ed8; }
  .badge-purple { background: #ede9fe; color: #6d28d9; }
  .badge-gray   { background: #f1f5f9; color: #475569; }
  .badge-orange { background: #ffedd5; color: #c2410c; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #f1f5f9; text-align: left; padding: 9px 12px; font-weight: 700; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: #475569; border-bottom: 2px solid #e2e8f0; }
  td { padding: 8px 12px; border-bottom: 1px solid #f1f5f9; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f8fafc; }

  /* EXEC SUMMARY */
  .exec-bullets { list-style: none; }
  .exec-bullets li { padding: 12px 14px; border-radius: 8px; margin-bottom: 8px; font-size: 14px; display: flex; gap: 10px; align-items: flex-start; }
  .exec-bullets li:last-child { margin-bottom: 0; }
  .bullet-icon { font-size: 18px; flex-shrink: 0; }

  /* CALENDAR */
  .cal-day { margin-bottom: 16px; }
  .cal-day-header { font-weight: 700; font-size: 13px; background: #e2e8f0; padding: 6px 12px; border-radius: 6px; margin-bottom: 8px; color: #334155; }
  .cal-event { display: flex; gap: 12px; padding: 10px 12px; background: #f8fafc; border-radius: 8px; margin-bottom: 6px; border-left: 4px solid #2563eb; }
  .cal-time { font-weight: 700; font-size: 12px; color: #2563eb; min-width: 90px; flex-shrink: 0; }
  .cal-details { flex: 1; }
  .cal-summary { font-weight: 700; font-size: 14px; }
  .cal-meta { font-size: 11px; color: #64748b; margin-top: 2px; }
  .cal-rsvp { font-size: 10px; font-weight: 700; padding: 2px 6px; border-radius: 4px; display: inline-block; margin-top: 3px; }
  .rsvp-confirmed { background: #dcfce7; color: #16a34a; }
  .rsvp-needs    { background: #fef3c7; color: #92400e; }
  .rsvp-declined { background: #fee2e2; color: #dc2626; }

  /* DASHBOARD GRID */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 12px; }
  .dash-card { background: white; border-radius: 10px; padding: 14px 16px; border: 1px solid #e2e8f0; text-align: center; }
  .dash-card .dash-num { font-size: 32px; font-weight: 800; }
  .dash-card .dash-label { font-size: 11px; color: #64748b; font-weight: 600; margin-top: 4px; text-transform: uppercase; letter-spacing: 0.5px; }

  /* TOP 3 */
  .top3 { display: flex; gap: 14px; flex-wrap: wrap; }
  .top3-card { flex: 1; min-width: 240px; background: white; border-radius: 12px; padding: 18px; border: 2px solid #e2e8f0; position: relative; }
  .top3-num { font-size: 48px; font-weight: 900; color: #e2e8f0; position: absolute; top: 8px; right: 14px; }
  .top3-title { font-weight: 700; font-size: 15px; margin-bottom: 6px; }
  .top3-desc { font-size: 13px; color: #475569; }

  /* TRIAGE TABLE */
  .triage-status { font-weight: 700; font-size: 12px; white-space: nowrap; }
  .row-rescued { background: #f0fdf4; }
  .row-inbox   { background: #eff6ff; }
  .row-trash   { background: #fafafa; }

  /* MISC */
  .note { font-size: 12px; color: #64748b; font-style: italic; margin-top: 8px; }
  .divider { border: none; border-top: 1px solid #e2e8f0; margin: 14px 0; }
  .tag { display: inline-block; font-size: 10px; padding: 2px 7px; border-radius: 4px; margin: 1px; font-weight: 600; }
  .tag-high   { background: #fee2e2; color: #dc2626; }
  .tag-medium { background: #fef3c7; color: #92400e; }
  .tag-low    { background: #f1f5f9; color: #64748b; }

  .rescued-note { font-size: 11px; background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 4px; padding: 2px 8px; color: #16a34a; display: inline-block; margin-top: 3px; }
  .spam-note { font-size: 11px; background: #fff7ed; border: 1px solid #fed7aa; border-radius: 4px; padding: 2px 8px; color: #c2410c; display: inline-block; margin-top: 3px; }
  .security-note { font-size: 11px; background: #fef2f2; border: 1px solid #fecaca; border-radius: 4px; padding: 2px 8px; color: #dc2626; display: inline-block; margin-top: 3px; }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════ -->
<!-- SECTION 0: EMAIL TRIAGE QUICK LIST                  -->
<!-- ═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title slate">📋 Email Triage Quick List</div>
  <div class="section-body" style="padding:0;">
    <table>
      <thead>
        <tr>
          <th style="width:120px;">Status</th>
          <th style="width:200px;">From</th>
          <th>Subject</th>
          <th>Summary</th>
        </tr>
      </thead>
      <tbody>
        <!-- RESCUED ROWS FIRST -->
        <tr class="row-rescued">
          <td class="triage-status">✅ RESCUED</td>
          <td>Nextdoor (Yorkville)</td>
          <td>Weather Alert: Flood Advisory — New York County</td>
          <td><span class="rescued-note">Rescued from Trash</span> NWS Flood Advisory for Melissa's local area — emergency alert worth keeping.</td>
        </tr>
        <tr class="row-rescued">
          <td class="triage-status">✅ RESCUED</td>
          <td>Supabase Auth</td>
          <td>Reset your password</td>
          <td><span class="rescued-note">Rescued from Trash</span> Legitimate password reset email — account security action.</td>
        </tr>
        <tr class="row-rescued">
          <td class="triage-status">✅ RESCUED</td>
          <td>Google</td>
          <td>You shared some Google Account data with Slack (×2)</td>
          <td><span class="rescued-note">Rescued from Trash</span> Melissa's account (swm3016@gmail.com) used to sign into Slack — security awareness.</td>
        </tr>
        <tr class="row-rescued">
          <td class="triage-status">✅ RESCUED</td>
          <td>Google</td>
          <td>Security alert — New sign-in on Mac OS</td>
          <td><span class="rescued-note">Rescued from Trash</span> New sign-in detected on dhwconsulting3@gmail.com — verify this was Melissa.</td>
        </tr>
        <tr class="row-rescued">
          <td class="triage-status">✅ RESCUED</td>
          <td>Match</td>
          <td>Al likes you. See if it's mutual.</td>
          <td><span class="rescued-note">Rescued from Trash</span> Protected sender — kept in inbox per rule.</td>
        </tr>
        <tr class="row-rescued">
          <td class="triage-status">✅ RESCUED</td>
          <td>Google Play</td>
          <td>Your Google Play Order Receipt from Sep 3, 2026</td>
          <td><span class="rescued-note">Rescued from Trash</span> Legitimate purchase/subscription receipt — keep for records.</td>
        </tr>
        <!-- INBOX ROWS -->
        <tr class="row-inbox">
          <td class="triage-status">📥 INBOX</td>
          <td>Charles Schwab</td>
          <td>Your account eStatement is available</td>
          <td>Monthly eStatement for account ending 284. Review and file.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status">📥 INBOX</td>
          <td>Indeed</td>
          <td>Head of People, US @ Empathy — $180K–$200K</td>
          <td>Strong HR leadership match flagged by Indeed. High-priority lead.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status">📥 INBOX</td>
          <td>Amazon.com</td>
          <td>Shipped: 1 Shoes item</td>
          <td>Shoe order shipped from Amazon. Track delivery.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status">📥 INBOX</td>
          <td>Slack</td>
          <td>"perfomance chat" Slack Pro trial ends in 7 days</td>
          <td>Slack Pro trial for "perfomance chat" workspace expires Sep 11. Decide: upgrade or downgrade.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status">📥 INBOX</td>
          <td>Slack</td>
          <td>"performance" Slack Pro trial ends in 7 days</td>
          <td>Slack Pro trial for "performance" workspace expires Sep 11. Decide: upgrade or downgrade.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status">📥 INBOX</td>
          <td>LinkedIn (Rachelle)</td>
          <td>I still want to connect</td>
          <td>Rachelle Burchette, Executive Communication Coach, awaiting connection response.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status">📥 INBOX</td>
          <td>Match</td>
          <td>You've had a profile view from Nicholas (66, Huntington NY)</td>
          <td>Nicholas viewed Melissa's Match profile.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status">📥 INBOX</td>
          <td>Match</td>
          <td>Melissa, you've still got an unread message</td>
          <td>Unread message waiting on Match — check inbox.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status">📥 INBOX</td>
          <td>Target Circle Mastercard</td>
          <td>Looking for even more ways to save?</td>
          <td>Target Circle Card promotional email. Low priority.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status">📥 INBOX</td>
          <td>Match</td>
          <td>Pete just sent you a new message 💌</td>
          <td>New message from Pete on Match.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status">📥 INBOX</td>
          <td>Match</td>
          <td>Pete likes you. See if it's mutual.</td>
          <td>Pete liked Melissa's Match profile.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status">📥 INBOX</td>
          <td>ChatGPT / OpenAI</td>
          <td>When an edit feels off</td>
          <td>ChatGPT tips newsletter — turn feedback into an editing prompt.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status">📥 INBOX</td>
          <td>SHEIN</td>
          <td>Your SHEIN order has been shipped</td>
          <td>SHEIN order shipped. Track delivery.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status">📥 INBOX</td>
          <td>Teleport Hiring Team</td>
          <td>Thanks for your interest in Teleport</td>
          <td>Rejection for Senior People Business Partner – GTM role at Teleport. Log and move on.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status">📥 INBOX</td>
          <td>LinkedIn News</td>
          <td>Kyle Van Noy makes it LinkedIn official</td>
          <td>NFL veteran joins Minnesota Vikings — LinkedIn trending story. Low priority.</td>
        </tr>
        <!-- SPAM / PHISHING (not auto-trashed flag but clearly spam — in inbox) -->
        <tr class="row-inbox">
          <td class="triage-status">📥 INBOX ⚠️</td>
          <td>"melissaw212" (Raging Bull Casino)</td>
          <td>Please check your Account-ID: 75409193360603</td>
          <td><span class="security-note">Phishing/Scam</span> Fake casino balance notification. Do not click. Delete immediately.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status">📥 INBOX ⚠️</td>
          <td>"F*ckHard" (explicit spam)</td>
          <td>🔞 Unlock the Neuron limiting your Vigor…</td>
          <td><span class="security-note">Explicit Spam/Phishing</span> Malicious explicit spam. Delete immediately. Do not click.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status">📥 INBOX ⚠️</td>
          <td>"FUCK ME" (explicit spam)</td>
          <td>🔞 USE THE RAW SECRET TO FUCK HER FOR 4 HOURS…</td>
          <td><span class="security-note">Explicit Spam/Phishing</span> Malicious explicit spam. Delete immediately. Do not click.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status">📥 INBOX ⚠️</td>
          <td>Betty Wins Casino</td>
          <td>ACTIVATE YOUR 400% BONUS NOW — READY FOR CONFIRMATION</td>
          <td><span class="security-note">Phishing/Scam</span> Fake casino bonus targeting melissaw212. Delete immediately.</td>
        </tr>
        <tr class="row-inbox">
          <td class="triage-status">📥 INBOX</td>
          <td>Coursiv</td>
          <td>Still want to learn AI?</td>
          <td>AI learning plan from quiz still saved. Review if interested.</td>
        </tr>
        <!-- TRASH SUMMARY ROWS -->
        <tr class="row-trash">
          <td class="triage-status">🗂 TRASH (manual)</td>
          <td colspan="3">28 emails in Trash (manually trashed) — see <strong>Trash Review</strong> section for full breakdown, restore/delete recommendations.</td>
        </tr>
      </tbody>
    </table>
    <p class="note" style="padding:10px 12px;">Triage note: Rescued emails appear first, followed by inbox items, then trash summary rows. All 50 emails are accounted for. Counts: 6 rescued | 22 inbox (incl. spam flagged) | 22 manual trash = 50 total.</p>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════ -->
<!-- SECTION 1: HEADER                                   -->
<!-- ═══════════════════════════════════════════════════ -->
<div class="header">
  <div class="section-title" style="background:none;padding:0;font-size:13px;color:#a8b8d8;font-weight:400;letter-spacing:1px;text-transform:uppercase;margin-bottom:4px;">Executive Briefing</div>
  <h1>Good Morning, Melissa 👋</h1>
  <div class="subtitle">Friday, September 4, 2026 · Prepared by Your Executive Chief of Staff</div>
  <div class="meta">
    <div class="meta-item"><span>50</span>Emails Reviewed</div>
    <div class="meta-item"><span>7</span>Calendar Events</div>
    <div class="meta-item"><span>3</span>Action Items (Urgent)</div>
    <div class="meta-item"><span>⚠️ Flood</span>Advisory Active — New York County</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════ -->
<!-- SECTION 2: EXECUTIVE SUMMARY                        -->
<!-- ═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title red">🔴 Executive Summary</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li style="background:#fef2f2; border-left:4px solid #dc2626;">
        <span class="bullet-icon">🚨</span>
        <div><strong>Biggest Risk:</strong> Multiple security events require immediate review — a Google security alert for a new Mac OS sign-in on dhwconsulting3@gmail.com was rescued from Trash; three explicit phishing/spam emails (including two casino scams and two extreme adult-content phishing emails) landed in your inbox and must be deleted. Your Slack Pro trial for two workspaces expires <strong>September 11</strong> — decision needed within 7 days. A NWS Flood Advisory is active for New York County today.</div>
      </li>
      <li style="background:#f0fdf4; border-left:4px solid #16a34a;">
        <span class="bullet-icon">💼</span>
        <div><strong>Biggest Opportunity:</strong> Indeed flagged a <strong>Head of People, US @ Empathy ($180K–$200K)</strong> as a strong match for your HR leadership experience — this is your highest-priority job lead today. Teleport sent a rejection for the Senior People Business Partner–GTM role (log and move on). Glassdoor and job boards surfaced additional HR leads. Your HR Networking & Job Search Group meets next week on Sep 9 and Sep 10.</div>
      </li>
      <li style="background:#eff6ff; border-left:4px solid #2563eb;">
        <span class="bullet-icon">📅</span>
        <div><strong>Biggest Calendar Item:</strong> Your <strong>State Farm bill is due September 7</strong> (Monday — Labor Day weekend). Two HR Networking Zoom sessions next week (Sep 9 & Sep 10) need RSVPs — both still showing "Needs Action." The Executive Roundtable on Sep 10 is currently declined — confirm that's intentional. An M&amp;M meeting with Monte Montoya on Sep 10 at 1 PM also needs a response.</div>
      </li>
    </ul>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════ -->
<!-- SECTION 3: ACTION REQUIRED                          -->
<!-- ═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title yellow">⚡ Action Required</div>
  <div class="section-body">

    <div class="card red-border">
      <div class="card-label" style="color:#dc2626;">🚨 URGENT — SECURITY</div>
      <div class="card-title">Google Security Alert: New Sign-In on Mac OS (dhwconsulting3@gmail.com)</div>
      <div class="card-row">
        <div class="card-field"><strong>Source:</strong> Google &lt;no-reply@accounts.google.com&gt;</div>
        <div class="card-field"><strong>Date:</strong> Sep 4, 2026, 2:13 AM</div>
        <div class="card-field"><span class="badge badge-red">HIGH PRIORITY</span></div>
      </div>
      <div class="card-field" style="margin-top:8px;"><strong>Why it matters:</strong> A new sign-in was detected on a Mac OS device for a Google account (dhwconsulting3@gmail.com). This was auto-trashed and then rescued. If this was not Melissa, the account may be compromised.</div>
      <div class="card-field" style="margin-top:6px;"><strong>Next step:</strong> Log into dhwconsulting3@gmail.com immediately → check Recent Activity → if unrecognized, change password and enable 2FA. Also review the two Slack sign-in notifications for swm3016@gmail.com.</div>
      <div class="card-field"><strong>Due:</strong> <strong>Today — Immediately</strong></div>
    </div>

    <div class="card red-border">
      <div class="card-label" style="color:#dc2626;">🚨 URGENT — DELETE SPAM</div>
      <div class="card-title">Delete 4 Explicit/Phishing Emails From Inbox</div>
      <div class="card-row">
        <div class="card-field"><strong>Source:</strong> "F*ckHard", "FUCK ME", "melissaw212" (Raging Bull Casino), Betty Wins Casino</div>
        <div class="card-field"><span class="badge badge-red">HIGH PRIORITY</span></div>
      </div>
      <div class="card-field" style="margin-top:8px;"><strong>Why it matters:</strong> Four malicious/phishing emails bypassed filters and landed in your inbox. Two contain explicit adult content and phishing links. Two are fake casino scams targeting your username (melissaw212). Do NOT click any links.</div>
      <div class="card-field" style="margin-top:6px;"><strong>Next step:</strong> Select all four → Mark as Spam → Delete. Consider reporting to Gmail as phishing. Review if email address is exposed on data broker sites.</div>
      <div class="card-field"><strong>Due:</strong> <strong>Today</strong></div>
    </div>

    <div class="card yellow-border">
      <div class="card-label" style="color:#d97706;">⚡ URGENT — BILLING</div>
      <div class="card-title">Slack Pro Trial Expiring: Two Workspaces — Sep 11</div>
      <div class="card-row">
        <div class="card-field"><strong>Source:</strong> Slack &lt;no-reply@slack.com&gt; (×2)</div>
        <div class="card-field"><strong>Due:</strong> September 11, 2026</div>
        <div class="card-field"><span class="badge badge-yellow">MEDIUM PRIORITY</span></div>
      </div>
      <div class="card-field" style="margin-top:8px;"><strong>Why it matters:</strong> Both "perfomance chat" and "performance" Slack workspaces will lose premium features on Sep 11 if no action is taken. Given you appear to have two workspaces, evaluate which (if any) to keep on Pro.</div>
      <div class="card-field" style="margin-top:6px;"><strong>Next step:</strong> Determine if either workspace is actively used. Upgrade to Pro or downgrade to Free before Sep 11 to avoid disruption.</div>
      <div class="card-field"><strong>Due:</strong> <strong>By September 11, 2026</strong></div>
    </div>

    <div class="card yellow-border">
      <div class="card-label" style="color:#d97706;">💳 BILLING REMINDER</div>
      <div class="card-title">State Farm Bill Due — Sep 7 (Labor Day Weekend)</div>
      <div class="card-row">
        <div class="card-field"><strong>Source:</strong> Google Calendar — "State farm bill" reminder</div>
        <div class="card-field"><strong>Due:</strong> Monday, September 7, 2026</div>
        <div class="card-field"><span class="badge badge-yellow">MEDIUM PRIORITY</span></div>
      </div>
      <div class="card-field" style="margin-top:8px;"><strong>Why it matters:</strong> Bill is due on Labor Day — banks and payment processors may have delays. Pay before end-of-day today (Friday) to avoid late fees.</div>
      <div class="card-field" style="margin-top:6px;"><strong>Next step:</strong> Log into State Farm portal or use autopay to submit payment today.</div>
      <div class="card-field"><strong>Due:</strong> <strong>Pay Today — Before Monday</strong></div>
    </div>

    <div class="card green-border">
      <div class="card-label" style="color:#16a34a;">💼 JOB OPPORTUNITY</div>
      <div class="card-title">Head of People, US @ Empathy — $180K–$200K (Indeed Match)</div>
      <div class="card-row">
        <div class="card-field"><strong>Source:</strong> Indeed &lt;donotreply@match.indeed.com&gt;</div>
        <div class="card-field"><strong>Date:</strong> Sep 4, 2026</div>
        <div class="card-field"><span class="badge badge-green">HIGH FIT</span></div>
      </div>
      <div class="card-field" style="margin-top:8px;"><strong>Why it matters:</strong> Indeed's algorithm flagged this as a "strong match" for Melissa's extensive HR leadership experience. Compensation is competitive at $180K–$200K.</div>
      <div class="card-field" style="margin-top:6px;"><strong>Next step:</strong> Open the Indeed email → Review full job description → Apply today or save for weekend application. Empathy is a grief-tech company — research mission fit.</div>
      <div class="card-field"><strong>Due:</strong> <strong>Apply ASAP — Labor Day weekend may slow hiring</strong></div>
    </div>

    <div class="card blue-border">
      <div class="card-label" style="color:#2563eb;">📅 RSVP NEEDED</div>
      <div class="card-title">RSVP for Two HR Networking Zoom Sessions (Sep 9 & Sep 10)</div>
      <div class="card-row">
        <div class="card-field"><strong>Source:</strong> Google Calendar — HR Networking & Job Search Group</div>
        <div class="card-field"><strong>Due:</strong> Before September 9 & 10</div>
        <div class="card-field"><span class="badge badge-blue">ACTION NEEDED</span></div>
      </div>
      <div class="card-field" style="margin-top:8px;"><strong>Why it matters:</strong> Both sessions show "Needs Action" status. These are key job search networking calls with 100+ HR professionals. Confirm attendance to ensure you're prepared and have the Zoom links ready.</div>
      <div class="card-field" style="margin-top:6px;"><strong>Next step:</strong> Accept both calendar invites. Sep 9: 12–1:30 PM Zoom. Sep 10: 12–1 PM Zoom. Note: Sep 10 also has an M&amp;M meeting at 1 PM — back-to-back, plan accordingly.</div>
    </div>

    <div class="card yellow-border">
      <div class="card-label" style="color:#d97706;">🏦 FINANCIAL</div>
      <div class="card-title">Charles Schwab eStatement Available (Account ending 284)</div>
      <div class="card-row">
        <div class="card-field"><strong>Source:</strong> Charles Schwab &lt;donotreply@mail.schwab.com&gt;</div>
        <div class="card-field"><strong>Date:</strong> Sep 4, 2026</div>
        <div class="card-field"><span class="badge badge-yellow">REVIEW</span></div>
      </div>
      <div class="card-field" style="margin-top:8px;"><strong>Why it matters:</strong> Monthly investment/brokerage statement is available. Important to review during a job search period for financial planning.</div>
      <div class="card-field" style="margin-top:6px;"><strong>Next step:</strong> Log in to Schwab.com → View eStatement → File or download for records.</div>
    </div>

    <div class="card yellow-border">
      <div class="card-label" style="color:#d97706;">🔒 SECURITY — REVIEW</div>
      <div class="card-title">Supabase Password Reset Email (Rescued from Trash)</div>
      <div class="card-row">
        <div class="card-field"><strong>Source:</strong> Supabase Auth &lt;noreply@mail.app.supabase.io&gt;</div>
        <div class="card-field"><strong>Date:</strong> Sep 4, 2026, 2:23 AM</div>
        <div class="card-field"><span class="badge badge-yellow">VERIFY</span></div>
      </div>
      <div class="card-field" style="margin-top:8px;"><strong>Why it matters:</strong> A password reset was requested for a Supabase account. If Melissa did NOT request this, it may indicate an attempted breach. The link may now be expired.</div>
      <div class="card-field" style="margin-top:6px;"><strong>Next step:</strong> If you requested this reset, confirm the new password is set. If not requested, log in to Supabase directly and review account activity.</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════ -->
<!-- SECTION 4: FULL 7-DAY CALENDAR                      -->
<!-- ═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title blue">📅 Full 7-Day Calendar — Sep 4–10, 2026</div>
  <div class="section-body">

    <div class="cal-day">
      <div class="cal-day-header">📍 Friday, September 4, 2026 — TODAY</div>
      <div class="cal-event" style="border-left-color:#94a3b8; background:#f8fafc;">
        <div class="cal-time">All Day</div>
        <div class="cal-details">
          <div class="cal-summary" style="color:#64748b;">No calendar events scheduled for today</div>
          <div class="cal-meta">⚠️ Active: NWS Flood Advisory for New York County — check conditions before going out. Labor Day weekend begins today — pay State Farm bill before Monday.</div>
        </div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">📍 Saturday, September 5 — Sunday, September 6, 2026</div>
      <div class="cal-event" style="border-left-color:#94a3b8; background:#f8fafc;">
        <div class="cal-time">All Day</div>
        <div class="cal-details">
          <div class="cal-summary" style="color:#64748b;">No calendar events scheduled — Labor Day weekend</div>
          <div class="cal-meta">Consider reviewing the Empathy Head of People role and applying over the weekend. State Farm bill must be paid by Monday.</div>
        </div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">📍 Monday, September 7, 2026 — Labor Day</div>
      <div class="cal-event" style="border-left-color:#d97706;">
        <div class="cal-time">All Day</div>
        <div class="cal-details">
          <div class="cal-summary">💳 State Farm Bill Due</div>
          <div class="cal-meta">Pay before end-of-day today (ideally Friday, Sep 4). Labor Day — banks may be closed.</div>
          <div class="cal-rsvp rsvp-confirmed">✅ Confirmed (Calendar Reminder)</div>
          <div class="cal-meta" style="margin-top:4px;"><strong>⚠️ Prep:</strong> Log into State Farm portal or call to confirm payment. Pay today (Friday) to avoid holiday delays.</div>
        </div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">📍 Tuesday, September 8, 2026</div>
      <div class="cal-event" style="border-left-color:#7c3aed;">
        <div class="cal-time">10:00 AM – 11:00 AM</div>
        <div class="cal-details">
          <div class="cal-summary">💅 Nails Appointment</div>
          <div class="cal-meta">Personal appointment — 1 hour.</div>
          <div class="cal-rsvp rsvp-confirmed">✅ Confirmed</div>
          <div class="cal-meta" style="margin-top:4px;"><strong>📍 Location:</strong> Not specified — confirm appointment details.</div>
          <div class="cal-meta"><strong>Prep:</strong> No prep required. Block travel time.</div>
        </div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">📍 Wednesday, September 9, 2026</div>
      <div class="cal-event" style="border-left-color:#16a34a;">
        <div class="cal-time">12:00 PM – 1:30 PM</div>
        <div class="cal-details">
          <div class="cal-summary">👥 HR Networking & Job Search Group — Zoom 2</div>
          <div class="cal-meta">Large group HR networking session — 100+ professionals. Active job search networking call.</div>
          <div class="cal-rsvp rsvp-needs">⚠️ Needs Action — RSVP Required</div>
          <div class="cal-meta" style="margin-top:4px;"><strong>📍 Zoom:</strong> <a href="https://us06web.zoom.us/j/81954171722" style="color:#2563eb;">Join Meeting</a> · Password embedded in link</div>
          <div class="cal-meta"><strong>Prep:</strong> Review HR Networking Team Guidelines (link in calendar invite). Prepare 30-second intro. Review attendee list for key connections. Accept invite ASAP.</div>
        </div>
      </div>
      <div class="cal-event" style="border-left-color:#94a3b8; background:#f8fafc;">
        <div class="cal-time">12:00 PM – 1:30 PM</div>
        <div class="cal-details">
          <div class="cal-summary" style="color:#64748b;">🗂 Network (duplicate/personal block)</div>
          <div class="cal-meta">Separate "Network" calendar block — same time as HR Networking Zoom. Likely a personal reminder block.</div>
          <div class="cal-rsvp rsvp-confirmed">✅ Confirmed</div>
          <div class="cal-meta" style="margin-top:4px;"><strong>Note:</strong> Appears to overlap with HR Networking Zoom above — treat as the same session or a general networking block. No conflict.</div>
        </div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">📍 Thursday, September 10, 2026</div>
      <div class="cal-event" style="border-left-color:#dc2626;">
        <div class="cal-time">9:00 AM – 10:30 AM</div>
        <div class="cal-details">
          <div class="cal-summary">🏢 Executive Roundtable (John Madigan — Zoom)</div>
          <div class="cal-meta">Zoom meeting hosted by John Madigan. Meeting ID: 207 786 667 · Password: 205454</div>
          <div class="cal-rsvp rsvp-declined">❌ Declined</div>
          <div class="cal-meta" style="margin-top:4px;"><strong>📍 Zoom:</strong> <a href="https://us02web.zoom.us/j/207786667" style="color:#2563eb;">Join Meeting</a></div>
          <div class="cal-meta"><strong>⚠️ Conflict Check:</strong> You have declined this. Verify this was intentional — "Executive Roundtable" could be a valuable networking opportunity during your job search. Consider if you should reinstate.</div>
        </div>
      </div>
      <div class="cal-event" style="border-left-color:#16a34a;">
        <div class="cal-time">12:00 PM – 1:00 PM</div>
        <div class="cal-details">
          <div class="cal-summary">👥 HR Networking & Job Search: Open Office Hours — Zoom 2</div>
          <div class="cal-meta">Open office hours format — less structured, networking and Q&A. No AI notetaking tools per organizer request.</div>
          <div class="cal-rsvp rsvp-needs">⚠️ Needs Action — RSVP Required</div>
          <div class="cal-meta" style="margin-top:4px;"><strong>📍 Zoom:</strong> <a href="https://us06web.zoom.us/j/85945371140" style="color:#2563eb;">Join Meeting</a></div>
          <div class="cal-meta"><strong>⚠️ Schedule Conflict:</strong> This ends at 1 PM — M&amp;M with Monte Montoya starts at 1 PM same day. Back-to-back with no buffer. Plan for hard stop.</div>
          <div class="cal-meta"><strong>Prep:</strong> Turn off AI notetaking. Have job search questions ready. Hard stop at 1 PM for M&amp;M.</div>
        </div>
      </div>
      <div class="cal-event" style="border-left-color:#7c3aed;">
        <div class="cal-time">1:00 PM – 2:00 PM</div>
        <div class="cal-details">
          <div class="cal-summary">🤝 M&amp;M Meeting (Monte Montoya)</div>
          <div class="cal-meta">One-on-one with monte.montoya@gmail.com. Nature/agenda unknown — likely a networking or professional call.</div>
          <div class="cal-rsvp rsvp-needs">⚠️ Needs Action — RSVP Required</div>
          <div class="cal-meta" style="margin-top:4px;"><strong>📍 Location:</strong> Not specified</div>
          <div class="cal-meta"><strong>⚠️ Conflict:</strong> Immediately follows HR Networking Open Office Hours (12–1 PM). Confirm with Monte if 1 PM sharp start is still possible.</div>
          <div class="cal-meta"><strong>Prep:</strong> Send Monte an agenda or confirm purpose of meeting. Accept/decline invite.</div>
        </div>
      </div>
    </div>

    <div style="background:#f0fdf4; border-radius:8px; padding:12px; margin-top:8px; border:1px solid #bbf7d0;">
      <strong style="color:#16a34a;">📅 Calendar Summary:</strong> No events today (Sep 4). Labor Day weekend — use time to apply to Empathy role and pay State Farm bill. Key week ahead: Nails Tue, HR Networking Wed & Thu, Executive Roundtable Thu (declined — verify), M&amp;M Thu.
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════ -->
<!-- SECTION 5: JOB SEARCH & INTERVIEW PIPELINE          -->
<!-- ═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title green">💼 Job Search & Interview Pipeline</div>
  <div class="section-body">

    <h3 style="margin-bottom:12px; color:#16a34a;">🌟 Active Opportunities</h3>
    <table>
      <thead>
        <tr>
          <th>Fit</th>
          <th>Role / Company</th>
          <th>Source</th>
          <th>Salary</th>
          <th>Status</th>
          <th>Next Step</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="badge badge-green">HIGH</span></td>
          <td><strong>Head of People, US</strong><br>Empathy</td>
          <td>Indeed (direct match)</td>
          <td>$180K–$200K</td>
          <td>Not yet applied</td>
          <td>Apply this weekend — strong match flagged by Indeed algorithm</td>
        </tr>
        <tr>
          <td><span class="badge badge-yellow">MEDIUM</span></td>
          <td><strong>HR Generalist, Retail, Northeast + NYC</strong><br>Sephora (+ 7 more)</td>
          <td>Glassdoor</td>
          <td>Not listed</td>
          <td>Not yet reviewed</td>
          <td>Review Glassdoor email — Sephora lead may be relevant</td>
        </tr>
        <tr>
          <td><span class="badge badge-yellow">MEDIUM</span></td>
          <td><strong>Donor Relations Manager</strong><br>Summer Search (+ 4 more NYC)</td>
          <td>Glassdoor</td>
          <td>Not listed</td>
          <td>Not yet reviewed</td>
          <td>Review Glassdoor email — NYC-based roles</td>
        </tr>
        <tr>
          <td><span class="badge badge-gray">CLOSED</span></td>
          <td><strong>Senior People Business Partner – GTM</strong><br>Teleport</td>
          <td>Direct application</td>
          <td>—</td>
          <td>❌ Rejected</td>
          <td>Log rejection. Move on. Thank-you note optional.</td>
        </tr>
      </tbody>
    </table>

    <hr class="divider">

    <h3 style="margin-bottom:12px; color:#16a34a;">🤝 Networking & HR Community</h3>
    <table>
      <thead>
        <tr>
          <th>Event / Contact</th>
          <th>Date</th>
          <th>Status</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>HR Networking & Job Search Group — Zoom 2</strong><br>100+ HR professionals</td>
          <td>Sep 9, 12–1:30 PM</td>
          <td><span class="badge badge-yellow">Needs RSVP</span></td>
          <td>Accept invite. Prep 30-sec intro. Review team guidelines.</td>
        </tr>
        <tr>
          <td><strong>HR Networking Open Office Hours — Zoom 2</strong></td>
          <td>Sep 10, 12–1 PM</td>
          <td><span class="badge badge-yellow">Needs RSVP</span></td>
          <td>Accept invite. Note: back-to-back with M&amp;M at 1 PM.</td>
        </tr>
        <tr>
          <td><strong>M&amp;M with Monte Montoya</strong></td>
          <td>Sep 10, 1–2 PM</td>
          <td><span class="badge badge-yellow">Needs RSVP</span></td>
          <td>Accept/respond. Confirm agenda with Monte.</td>
        </tr>
        <tr>
          <td><strong>Executive Roundtable (John Madigan)</strong></td>
          <td>Sep 10, 9–10:30 AM</td>
          <td><span class="badge badge-red">Declined</span></td>
          <td>Verify decline was intentional — may be worth attending during job search.</td>
        </tr>
        <tr>
          <td><strong>Rachelle Burchette</strong> — Executive Communication Coach<br>LinkedIn connection request pending</td>
          <td>Sep 4</td>
          <td><span class="badge badge-yellow">Pending Response</span></td>
          <td>Review LinkedIn profile. Accept if aligned with professional goals. Could be a useful coach during job search.</td>
        </tr>
      </tbody>
    </table>

    <hr class="divider">
    <h3 style="margin-bottom:8px; color:#16a34a;">📊 Pipeline Summary</h3>
    <div style="display:flex; gap:12px; flex-wrap:wrap;">
      <div class="dash-card" style="border-color:#16a34a;"><div class="dash-num" style="color:#16a34a;">1</div><div class="dash-label">High-Fit Lead (Empathy)</div></div>
      <div class="dash-card" style="border-color:#d97706;"><div class="dash-num" style="color:#d97706;">2+</div><div class="dash-label">Medium Leads (Glassdoor)</div></div>
      <div class="dash-card" style="border-color:#dc2626;"><div class="dash-num" style="color:#dc2626;">1</div><div class="dash-label">Rejection (Teleport)</div></div>
      <div class="dash-card" style="border-color:#2563eb;"><div class="dash-num" style="color:#2563eb;">3</div><div class="dash-label">RSVP Actions Pending</div></div>
      <div class="dash-card" style="border-color:#7c3aed;"><div class="dash-num" style="color:#7c3aed;">0</div><div class="dash-label">Active Interviews</div></div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════ -->
<!-- SECTION 6: FULL EMAIL REVIEW BY CATEGORY            -->
<!-- ═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title slate">📂 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="card red-border">
      <div class="card-label" style="color:#dc2626;">🔴 SECURITY / RISK — 8 Emails</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Google (no-reply@accounts.google.com)</td><td>Security alert — New sign-in on Mac OS (dhwconsulting3@gmail.com)</td><td><span class="rescued-note">✅ Rescued from Trash</span></td><td><strong>🚨 URGENT: Verify sign-in immediately</strong></td></tr>
          <tr><td>Google (noreply-accounts@google.com) ×2</td><td>You shared some Google Account data with Slack (swm3016@gmail.com)</td><td><span class="rescued-note">✅ Rescued from Trash (×2)</span></td><td>Review — note Slack authorization on your account</td></tr>
          <tr><td>Supabase Auth</td><td>Reset your password</td><td><span class="rescued-note">✅ Rescued from Trash</span></td><td>Verify if requested; check account if not</td></tr>
          <tr><td>"FUCK ME" (explicit spam)</td><td>USE THE RAW SECRET… 🔞</td><td><span class="security-note">⚠️ Phishing — In Inbox</span></td><td><strong>Delete immediately. Report as spam.</strong></td></tr>
          <tr><td>"F*ckHard" (explicit spam)</td><td>🔞 Unlock the Neuron limiting your Vigor…</td><td><span class="security-note">⚠️ Phishing — In Inbox (Not Trashed)</span></td><td><strong>Delete immediately. Report as spam.</strong></td></tr>
          <tr><td>"melissaw212" / Raging Bull Casino</td><td>Please check your Account-ID: 75409193360603</td><td><span class="security-note">⚠️ Phishing/Scam — In Inbox (Not Trashed)</span></td><td><strong>Delete immediately. Do not click.</strong></td></tr>
          <tr><td>Betty Wins Casino</td><td>ACTIVATE YOUR 400% BONUS NOW — READY FOR CONFIRMATION</td><td><span class="security-note">⚠️ Phishing/Scam — In Inbox (Not Trashed)</span></td><td><strong>Delete immediately. Do not click.</strong></td></tr>
        </tbody>
      </table>
      <p class="note">⚠️ 4 phishing/scam emails bypassed spam filters and are sitting in inbox. Immediate deletion required. 4 security notifications rescued from trash — review today.</p>
    </div>

    <!-- JOB SEARCH -->
    <div class="card green-border">
      <div class="card-label" style="color:#16a34a;">🟢 JOB SEARCH — 5 Emails</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Location</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Indeed</td><td>Head of People, US @ Empathy — $180K–$200K</td><td>Inbox</td><td><strong>Apply ASAP — High fit</strong></td></tr>
          <tr><td>Teleport Hiring Team</td><td>Thanks for your interest in Teleport (rejection)</td><td>Not trashed / archived</td><td>Log rejection. No action needed.</td></tr>
          <tr><td>Glassdoor Jobs</td><td>Donor Relations Manager @ Summer Search + 4 more NYC roles</td><td>Trash</td><td>Review before deleting — NYC HR roles may be relevant</td></tr>
          <tr><td>Glassdoor Jobs</td><td>HR Generalist, Retail, NE + NYC @ Sephora + 7 more</td><td>Trash</td><td>Review before deleting — Sephora/Medtronic HR roles</td></tr>
          <tr><td>Buffkin / Baker</td><td>Reminder: The HR Brief: August 2026</td><td>Trash</td><td>Executive HR search firm — consider reviewing before deleting</td></tr>
        </tbody>
      </table>
      <p class="note">Note: Glassdoor and Buffkin/Baker emails are in Trash but contain potentially relevant job leads. Rescue before permanent deletion.</p>
    </div>

    <!-- RECRUITERS / NETWORKING -->
    <div class="card green-border">
      <div class="card-label" style="color:#16a34a;">🟢 RECRUITERS / NETWORKING — 1 Email</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Location</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Rachelle Burchette (via LinkedIn)</td><td>I still want to connect — Executive Communication Coach</td><td>Inbox</td><td>Review LinkedIn profile. Accept if aligned. Could support job search.</td></tr>
        </tbody>
      </table>
    </div>

    <!-- CALENDAR / EVENTS -->
    <div class="card blue-border">
      <div class="card-label" style="color:#2563eb;">🔵 CALENDAR / EVENTS — 1 Email</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Location</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>AllEvents</td><td>Melissa, popular events this weekend in York</td><td>Trash</td><td>Delete — generic event promotion. Not actionable.</td></tr>
        </tbody>
      </table>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="card yellow-border">
      <div class="card-label" style="color:#d97706;">🟡 FINANCIAL / BILLING — 4 Emails</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Location</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Charles Schwab</td><td>Your account eStatement is available (acct ending 284)</td><td>Inbox</td><td>Log in and review eStatement. File for records.</td></tr>
          <tr><td>Google Play</td><td>Your Google Play Order Receipt — Sep 3, 2026</td><td><span class="rescued-note">✅ Rescued from Trash</span></td><td>Save for records. Review subscription details.</td></tr>
          <tr><td>Target Circle Mastercard</td><td>Looking for even more ways to save?</td><td>Inbox</td><td>Promotional — low priority. Delete or ignore.</td></tr>
          <tr><td>Slack (×2)</td><td>Slack Pro trial ends in 7 days (Sep 11) — 2 workspaces</td><td>Inbox</td><td><strong>Decide: upgrade or downgrade before Sep 11</strong></td></tr>
        </tbody>
      </table>
      <p class="note">Note: Slack trial expiry counted here as billing/deadline. State Farm bill tracked via calendar.</p>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="card purple-border">
      <div class="card-label" style="color:#7c3aed;">🟣 PROFESSIONAL DEVELOPMENT — 4 Emails</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Location</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>People Action Check (Brevo)</td><td>Interpersonal Conflict — Elevated Risk</td><td>Trash</td><td>Appears to be a HR tool submission/notification. Review — could be work-related.</td></tr>
          <tr><td>People Action Check (Brevo)</td><td>Interpersonal Conflict — Elevated Risk —
