<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa — Saturday, August 29, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }

  .page-wrapper { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 4px 20px rgba(0,0,0,0.25); }
  .header-left h1 { font-size: 26px; font-weight: 700; letter-spacing: 0.5px; }
  .header-left .subtitle { font-size: 13px; color: #a0aec0; margin-top: 4px; }
  .header-right { text-align: right; }
  .header-right .date { font-size: 15px; font-weight: 600; color: #e2e8f0; }
  .header-right .meta { font-size: 12px; color: #a0aec0; margin-top: 6px; line-height: 1.8; }
  .badge { display: inline-block; background: #e53e3e; color: #fff; border-radius: 20px; padding: 2px 10px; font-size: 11px; font-weight: 700; margin-left: 6px; }
  .badge-blue { background: #3182ce; }
  .badge-green { background: #38a169; }

  /* SECTION HEADERS */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 13px; font-weight: 800; text-transform: uppercase; letter-spacing: 1.2px; padding: 8px 14px; border-radius: 8px 8px 0 0; color: #fff; }
  .section-body { background: #fff; border-radius: 0 0 10px 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.07); overflow: hidden; }

  /* COLOR THEMES */
  .theme-red .section-title { background: #c53030; }
  .theme-red { border: 1px solid #fc8181; border-radius: 10px; }
  .theme-yellow .section-title { background: #b7791f; }
  .theme-yellow { border: 1px solid #f6d860; border-radius: 10px; }
  .theme-blue .section-title { background: #2b6cb0; }
  .theme-blue { border: 1px solid #90cdf4; border-radius: 10px; }
  .theme-green .section-title { background: #276749; }
  .theme-green { border: 1px solid #9ae6b4; border-radius: 10px; }
  .theme-purple .section-title { background: #553c9a; }
  .theme-purple { border: 1px solid #b794f4; border-radius: 10px; }
  .theme-gray .section-title { background: #4a5568; }
  .theme-gray { border: 1px solid #cbd5e0; border-radius: 10px; }
  .theme-dark .section-title { background: #1a1a2e; }
  .theme-dark { border: 1px solid #4a5568; border-radius: 10px; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; }
  th { background: #f7fafc; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; color: #4a5568; padding: 10px 12px; border-bottom: 2px solid #e2e8f0; text-align: left; }
  td { padding: 9px 12px; border-bottom: 1px solid #edf2f7; font-size: 13px; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f7fafc; }

  /* STATUS PILLS */
  .pill { display: inline-block; border-radius: 12px; padding: 2px 10px; font-size: 11px; font-weight: 700; white-space: nowrap; }
  .pill-red { background: #fff5f5; color: #c53030; border: 1px solid #fc8181; }
  .pill-yellow { background: #fffff0; color: #b7791f; border: 1px solid #f6e05e; }
  .pill-green { background: #f0fff4; color: #276749; border: 1px solid #68d391; }
  .pill-blue { background: #ebf8ff; color: #2b6cb0; border: 1px solid #90cdf4; }
  .pill-purple { background: #faf5ff; color: #553c9a; border: 1px solid #d6bcfa; }
  .pill-gray { background: #f7fafc; color: #4a5568; border: 1px solid #cbd5e0; }
  .pill-orange { background: #fffaf0; color: #c05621; border: 1px solid #fbd38d; }

  /* CARDS */
  .card { padding: 16px 18px; border-bottom: 1px solid #edf2f7; }
  .card:last-child { border-bottom: none; }
  .card-title { font-weight: 700; font-size: 14px; margin-bottom: 4px; }
  .card-meta { font-size: 12px; color: #718096; margin-bottom: 6px; }
  .card-body { font-size: 13px; color: #2d3748; }
  .card-label { font-size: 10px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
  .label-red { color: #c53030; }
  .label-yellow { color: #b7791f; }
  .label-green { color: #276749; }
  .label-blue { color: #2b6cb0; }
  .label-purple { color: #553c9a; }
  .label-gray { color: #4a5568; }

  .step { background: #ebf8ff; border-left: 3px solid #3182ce; padding: 6px 10px; border-radius: 0 6px 6px 0; margin-top: 8px; font-size: 12px; color: #2b6cb0; font-weight: 600; }
  .step-red { background: #fff5f5; border-left-color: #c53030; color: #c53030; }
  .step-yellow { background: #fffff0; border-left-color: #d69e2e; color: #b7791f; }
  .step-green { background: #f0fff4; border-left-color: #38a169; color: #276749; }

  /* EXEC SUMMARY */
  .exec-summary { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; padding: 16px; }
  .exec-card { border-radius: 10px; padding: 14px 16px; }
  .exec-card.red { background: #fff5f5; border: 1px solid #fc8181; }
  .exec-card.yellow { background: #fffff0; border: 1px solid #f6e05e; }
  .exec-card.green { background: #f0fff4; border: 1px solid #68d391; }
  .exec-card .ec-icon { font-size: 20px; margin-bottom: 6px; }
  .exec-card .ec-label { font-size: 10px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; }
  .exec-card.red .ec-label { color: #c53030; }
  .exec-card.yellow .ec-label { color: #b7791f; }
  .exec-card.green .ec-label { color: #276749; }
  .exec-card .ec-text { font-size: 13px; color: #2d3748; }

  /* DASHBOARD GRID */
  .dashboard-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; padding: 16px; }
  .dash-card { border-radius: 10px; padding: 14px; text-align: center; }
  .dash-card .dash-num { font-size: 32px; font-weight: 800; line-height: 1; }
  .dash-card .dash-label { font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px; margin-top: 6px; color: #4a5568; }
  .dash-card.d-red { background: #fff5f5; border: 1px solid #fc8181; color: #c53030; }
  .dash-card.d-yellow { background: #fffff0; border: 1px solid #f6e05e; color: #b7791f; }
  .dash-card.d-green { background: #f0fff4; border: 1px solid #68d391; color: #276749; }
  .dash-card.d-blue { background: #ebf8ff; border: 1px solid #90cdf4; color: #2b6cb0; }
  .dash-card.d-purple { background: #faf5ff; border: 1px solid #d6bcfa; color: #553c9a; }
  .dash-card.d-gray { background: #f7fafc; border: 1px solid #cbd5e0; color: #4a5568; }
  .dash-card.d-orange { background: #fffaf0; border: 1px solid #fbd38d; color: #c05621; }

  /* PRIORITIES */
  .priority-list { padding: 16px 18px; }
  .priority-item { display: flex; gap: 14px; align-items: flex-start; padding: 12px 0; border-bottom: 1px solid #edf2f7; }
  .priority-item:last-child { border-bottom: none; }
  .priority-num { background: #1a1a2e; color: #fff; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 15px; flex-shrink: 0; }
  .priority-text strong { font-size: 14px; color: #1a1a2e; }
  .priority-text p { font-size: 13px; color: #4a5568; margin-top: 2px; }

  /* TRIAGE TABLE specifics */
  .triage-status { font-size: 13px; white-space: nowrap; }
  .triage-from { font-weight: 600; font-size: 12px; }
  .triage-subject { font-size: 12px; color: #2d3748; }
  .triage-summary { font-size: 12px; color: #4a5568; }

  .summary-row td { background: #f7fafc; font-style: italic; color: #4a5568; font-size: 12px; }

  /* MISC */
  .note { font-size: 11px; color: #718096; font-style: italic; padding: 8px 14px; background: #f7fafc; border-top: 1px dashed #e2e8f0; }
  .divider { height: 1px; background: #edf2f7; margin: 0; }
  .tag { font-size: 10px; font-weight: 700; text-transform: uppercase; background: #e2e8f0; color: #4a5568; border-radius: 4px; padding: 1px 6px; margin-left: 4px; }
  .tag-high { background: #fff5f5; color: #c53030; }
  .tag-med { background: #fffff0; color: #b7791f; }
  .tag-low { background: #f0fff4; color: #276749; }
  .warning-box { background: #fff5f5; border: 1px solid #fc8181; border-radius: 8px; padding: 10px 14px; margin: 10px 18px; font-size: 12px; color: #c53030; font-weight: 600; }
  .info-box { background: #ebf8ff; border: 1px solid #90cdf4; border-radius: 8px; padding: 10px 14px; margin: 10px 18px; font-size: 12px; color: #2b6cb0; }

  @media (max-width: 700px) {
    .exec-summary { grid-template-columns: 1fr; }
    .dashboard-grid { grid-template-columns: repeat(2, 1fr); }
    .header { flex-direction: column; gap: 12px; }
    .header-right { text-align: left; }
  }
</style>
</head>
<body>
<div class="page-wrapper">

  <!-- ═══════════════════════════════════════════════════════════ -->
  <!--  SECTION 0 — EMAIL TRIAGE QUICK LIST                       -->
  <!-- ═══════════════════════════════════════════════════════════ -->
  <div class="section theme-dark">
    <div class="section-title">📋 Email Triage Quick List — Saturday, August 29, 2026</div>
    <div class="section-body">
      <table>
        <thead>
          <tr>
            <th style="width:120px;">Status</th>
            <th style="width:180px;">From</th>
            <th style="width:260px;">Subject</th>
            <th>Summary</th>
          </tr>
        </thead>
        <tbody>
          <!-- INBOX ROWS (individual) -->
          <tr>
            <td class="triage-status"><span class="pill pill-red">📥 INBOX</span></td>
            <td class="triage-from">Bank of America</td>
            <td class="triage-subject">Online transfer occurred over the limit you set</td>
            <td class="triage-summary">⚠️ Transfer from acct ending 7471 exceeded your set limit — verify immediately</td>
          </tr>
          <tr>
            <td class="triage-status"><span class="pill pill-green">📥 INBOX</span></td>
            <td class="triage-from">IBM Talent Acquisition</td>
            <td class="triage-subject">Action Required: Complete IBM Talent Acquisition Opt-in form</td>
            <td class="triage-summary">IBM expanding talent network post-Confluent acquisition — opt-in required</td>
          </tr>
          <tr>
            <td class="triage-status"><span class="pill pill-green">📥 INBOX</span></td>
            <td class="triage-from">Indeed</td>
            <td class="triage-subject">Senior VP, Human Resources @ Brooklyn Navy Yard Dev Corp</td>
            <td class="triage-summary">$185K–$200K/yr — strong background match flagged</td>
          </tr>
          <tr>
            <td class="triage-status"><span class="pill pill-green">📥 INBOX</span></td>
            <td class="triage-from">LinkedIn Job Alerts</td>
            <td class="triage-subject">Chief Human Resources Officer at ORAU and 19 more</td>
            <td class="triage-summary">CHRO-level alert + 19 additional HR leadership roles</td>
          </tr>
          <tr>
            <td class="triage-status"><span class="pill pill-green">📥 INBOX</span></td>
            <td class="triage-from">LinkedIn Job Alerts</td>
            <td class="triage-subject">Principal HR Business Partner at PeopleOps Jobs and 39 more</td>
            <td class="triage-summary">40 HR roles — includes director/HRBP-level positions</td>
          </tr>
          <tr>
            <td class="triage-status"><span class="pill pill-purple">📥 INBOX</span></td>
            <td class="triage-from">LinkedIn (Precious Babalola)</td>
            <td class="triage-subject">I want to connect</td>
            <td class="triage-summary">Executive VA from Arise Capital Management — pending connection request</td>
          </tr>
          <tr>
            <td class="triage-status"><span class="pill pill-blue">📥 INBOX</span></td>
            <td class="triage-from">Match</td>
            <td class="triage-subject">Sean likes you. See if it's mutual.</td>
            <td class="triage-summary">Match.com notification — Sean expressed interest in Melissa's profile</td>
          </tr>
          <tr>
            <td class="triage-status"><span class="pill pill-blue">📥 INBOX</span></td>
            <td class="triage-from">Match</td>
            <td class="triage-subject">Profile view from GuyUnfinished, 58, Union NJ</td>
            <td class="triage-summary">Match.com — GuyUnfinished viewed Melissa's profile</td>
          </tr>
          <!-- TRASH SUMMARY ROWS -->
          <tr class="summary-row">
            <td><span class="pill pill-red">🗑 AUTO-TRASHED</span></td>
            <td colspan="3">4 emails auto-trashed (phishing/scam) — see Trash Review &amp; Security/Risk sections below</td>
          </tr>
          <tr class="summary-row">
            <td><span class="pill pill-gray">🗂 TRASH (manual)</span></td>
            <td colspan="3">38 emails in Trash (newsletters, spam, retail, adult content, casino) — see Trash Review below</td>
          </tr>
        </tbody>
      </table>
      <div class="note">ℹ️ Inbox emails shown individually. Auto-trashed phishing and manual-trash items collapsed into summary rows. Full details in sections below.</div>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════════ -->
  <!--  HEADER                                                     -->
  <!-- ═══════════════════════════════════════════════════════════ -->
  <div class="header">
    <div class="header-left">
      <h1>☀️ Good Morning, Melissa</h1>
      <div class="subtitle">Executive Briefing — Prepared by your Chief of Staff</div>
    </div>
    <div class="header-right">
      <div class="date">Saturday, August 29, 2026</div>
      <div class="meta">
        Total Emails Reviewed: <strong>50</strong><span class="badge">50</span><br>
        Total Calendar Events: <strong>4</strong><span class="badge badge-blue">4</span><br>
        Unread Inbox Emails: <strong>6</strong><span class="badge badge-green">6</span>
      </div>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════════ -->
  <!--  SECTION 2 — EXECUTIVE SUMMARY                             -->
  <!-- ═══════════════════════════════════════════════════════════ -->
  <div class="section theme-dark">
    <div class="section-title">⚡ Executive Summary</div>
    <div class="section-body">
      <div class="exec-summary">
        <div class="exec-card red">
          <div class="ec-icon">🔴</div>
          <div class="ec-label">Biggest Risk / Urgent</div>
          <div class="ec-text">Bank of America alert: an online transfer from account ending 7471 exceeded your self-set limit. Verify transaction authenticity and check for unauthorized activity immediately. Four phishing emails (fake CashApp) were auto-trashed.</div>
        </div>
        <div class="exec-card green">
          <div class="ec-icon">🟢</div>
          <div class="ec-label">Biggest Opportunity</div>
          <div class="ec-text">Three high-quality job leads arrived: IBM Talent Acquisition opt-in (action required), SVP HR at Brooklyn Navy Yard ($185K–$200K via Indeed), and CHRO-level LinkedIn alert (ORAU + 19 roles). IBM requires active response now.</div>
        </div>
        <div class="exec-card yellow">
          <div class="ec-icon">🟡</div>
          <div class="ec-label">Biggest Calendar Item</div>
          <div class="ec-text">Two HR Networking Zoom sessions need RSVPs: HR Networking &amp; Job Search Group on Sep 2 (12–1:30 PM, status: needsAction) and Open Office Hours on Sep 3 (12–1 PM, status: needsAction). Executive Roundtable on Sep 3 was declined.</div>
        </div>
      </div>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════════ -->
  <!--  SECTION 3 — ACTION REQUIRED                               -->
  <!-- ═══════════════════════════════════════════════════════════ -->
  <div class="section theme-red">
    <div class="section-title">🚨 Action Required</div>
    <div class="section-body">

      <div class="card">
        <div class="card-label label-red">🔴 URGENT — FINANCIAL SECURITY</div>
        <div class="card-title">Bank of America: Transfer Exceeded Your Limit — Account 7471</div>
        <div class="card-meta">From: Bank of America &lt;onlinebanking@ealerts.bankofamerica.com&gt; · Received: Sat Aug 29, 1:50 AM</div>
        <div class="card-body">An online transfer from your account ending in 7471 exceeded the limit you set. Amount: $255+. This may be legitimate activity, but given the high volume of phishing and scam emails targeting you, verify this transaction through the official BofA app or website — do not click email links.</div>
        <div class="step step-red">→ Log in to BofA directly (app or bankofamerica.com) to verify the transfer. If unauthorized, call BofA fraud line immediately: 1-800-432-1000. Due: Today.</div>
      </div>

      <div class="card">
        <div class="card-label label-green">🟢 HIGH PRIORITY — JOB SEARCH</div>
        <div class="card-title">IBM Talent Acquisition: Complete Opt-In Form (Action Required)</div>
        <div class="card-meta">From: IBM Talent Acquisition &lt;talent@ibm.com&gt; · Received: Sat Aug 29, 8:12 AM</div>
        <div class="card-body">IBM is expanding its talent network following the recent acquisition of Confluent. They've reached out to Melissa directly. Email is from the verified ibm.com domain. Completing the opt-in form keeps Melissa visible for upcoming HR leadership roles at a major enterprise tech company.</div>
        <div class="step step-green">→ Open email, complete IBM Talent Acquisition opt-in form. Verify link goes to ibm.com before submitting. Due: Within 48 hours.</div>
      </div>

      <div class="card">
        <div class="card-label label-yellow">🟡 RSVP NEEDED — CALENDAR</div>
        <div class="card-title">RSVP: HR Networking &amp; Job Search Group Zoom — Sep 2</div>
        <div class="card-meta">Calendar Event · Wed Sep 2, 12:00–1:30 PM ET · Status: needsAction</div>
        <div class="card-body">Large HR peer networking group (180+ members). Melissa has not yet responded to this invite. Given active job search, attendance is highly recommended. Zoom link confirmed active.</div>
        <div class="step step-yellow">→ Accept or decline in Google Calendar. Zoom: us06web.zoom.us/j/81954171722. Due: Before Sep 2.</div>
      </div>

      <div class="card">
        <div class="card-label label-yellow">🟡 RSVP NEEDED — CALENDAR</div>
        <div class="card-title">RSVP: HR Networking Open Office Hours — Sep 3</div>
        <div class="card-meta">Calendar Event · Thu Sep 3, 12:00–1:00 PM ET · Status: needsAction</div>
        <div class="card-body">Same HR networking group, open office hours format — free-form discussion, AI notetaking tools should be disabled per host instructions. Melissa has not yet responded.</div>
        <div class="step step-yellow">→ Accept or decline in Google Calendar. Zoom: us06web.zoom.us/j/85945371140. Due: Before Sep 3.</div>
      </div>

      <div class="card">
        <div class="card-label label-green">🟢 MEDIUM PRIORITY — JOB SEARCH</div>
        <div class="card-title">Indeed: SVP Human Resources @ Brooklyn Navy Yard — $185K–$200K</div>
        <div class="card-meta">From: Indeed &lt;donotreply@match.indeed.com&gt; · Received: Sat Aug 29, 8:28 AM</div>
        <div class="card-body">Indeed flagged Melissa's VP/Director HR background as a strong match. Brooklyn Navy Yard Development Corp — nonprofit/quasi-public sector. $185K–$200K salary range. Strong alignment with Melissa's seniority level.</div>
        <div class="step step-green">→ Review full job listing on Indeed. Tailor resume/cover letter if applying. Due: This weekend (roles close fast).</div>
      </div>

      <div class="card">
        <div class="card-label label-purple">🟣 MEDIUM PRIORITY — NETWORKING</div>
        <div class="card-title">LinkedIn Connection: Precious Babalola, Executive VA at Arise Capital Management</div>
        <div class="card-meta">From: LinkedIn Invitations · Received: Sat Aug 29, 7:05 AM</div>
        <div class="card-body">Legitimate LinkedIn connection request from a verified professional. Capital management firm contact may be valuable for expanding professional network during job search.</div>
        <div class="step">→ Review profile on LinkedIn and decide whether to accept or ignore. Due: This week.</div>
      </div>

    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════════ -->
  <!--  SECTION 4 — FULL 7-DAY CALENDAR                          -->
  <!-- ═══════════════════════════════════════════════════════════ -->
  <div class="section theme-blue">
    <div class="section-title">📅 Full 7-Day Calendar — Aug 29 – Sep 4, 2026</div>
    <div class="section-body">

      <div class="card">
        <div class="card-label label-blue">TODAY — SATURDAY, AUGUST 29, 2026</div>
        <div class="card-title">No calendar events scheduled today.</div>
        <div class="card-body" style="color:#718096;">Use today to address urgent BofA alert, review IBM opt-in, and explore job leads from LinkedIn/Indeed.</div>
      </div>

      <div class="divider"></div>

      <div class="card">
        <div class="card-label label-blue">SUNDAY, AUGUST 30 — MONDAY, SEPTEMBER 1</div>
        <div class="card-title">No calendar events scheduled.</div>
        <div class="card-body" style="color:#718096;">Labor Day weekend. Use time to prepare for Wednesday and Thursday networking sessions.</div>
      </div>

      <div class="divider"></div>

      <table>
        <thead>
          <tr>
            <th>Day &amp; Date</th>
            <th>Time</th>
            <th>Event</th>
            <th>RSVP / Status</th>
            <th>Location / Link</th>
            <th>Prep Needed</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Wednesday<br>Sep 2</strong></td>
            <td>12:00 – 1:30 PM ET</td>
            <td>
              <strong>HR Networking &amp; Job Search Group — Zoom 2</strong><br>
              <span style="font-size:11px;color:#718096;">180+ HR professional attendees · Group networking session</span>
            </td>
            <td><span class="pill pill-yellow">⚠️ Needs Action</span></td>
            <td style="font-size:11px;"><a href="https://us06web.zoom.us/j/81954171722" style="color:#2b6cb0;">Zoom Link</a><br>Meeting ID in calendar</td>
            <td>Review team guidelines doc linked in calendar description. Prepare elevator pitch. Log in 5 min early.</td>
          </tr>
          <tr>
            <td><strong>Wednesday<br>Sep 2</strong></td>
            <td>12:00 – 1:30 PM ET</td>
            <td>
              <strong>Network</strong> <span class="tag">Personal Block</span><br>
              <span style="font-size:11px;color:#718096;">Personal calendar block — same time as HR Networking Zoom</span>
            </td>
            <td><span class="pill pill-green">✅ Confirmed</span></td>
            <td>No location set</td>
            <td>
              <span style="color:#c53030;font-weight:600;">⚠️ CONFLICT:</span> Overlaps with HR Networking Group Zoom (same 12–1:30 PM slot). Confirm if this is the same session or a separate commitment.
            </td>
          </tr>
          <tr>
            <td><strong>Thursday<br>Sep 3</strong></td>
            <td>9:00 – 10:30 AM ET</td>
            <td>
              <strong>Executive Roundtable</strong><br>
              <span style="font-size:11px;color:#718096;">Hosted by John Madigan · Zoom meeting</span>
            </td>
            <td><span class="pill pill-gray">❌ Declined</span></td>
            <td style="font-size:11px;"><a href="https://us02web.zoom.us/j/207786667" style="color:#2b6cb0;">Zoom Link</a><br>PW: 205454</td>
            <td>Already declined. No action needed unless you wish to reconsider.</td>
          </tr>
          <tr>
            <td><strong>Thursday<br>Sep 3</strong></td>
            <td>12:00 – 1:00 PM ET</td>
            <td>
              <strong>HR Networking &amp; Job Search: Open Office Hours — Zoom 2</strong><br>
              <span style="font-size:11px;color:#718096;">Same large HR group · Free-form discussion format · No AI notetaking</span>
            </td>
            <td><span class="pill pill-yellow">⚠️ Needs Action</span></td>
            <td style="font-size:11px;"><a href="https://us06web.zoom.us/j/85945371140" style="color:#2b6cb0;">Zoom Link</a></td>
            <td>Disable AI notetaking tools per host request. Prepare 2–3 discussion points or questions relevant to your job search. RSVP first.</td>
          </tr>
        </tbody>
      </table>

      <div class="warning-box">⚠️ SCHEDULE CONFLICT — Sep 2: "Network" personal block (confirmed) overlaps exactly with HR Networking Group Zoom (needsAction). Determine if these are the same event or if there is a double-booking. Recommend resolving before Wednesday.</div>

      <div class="info-box">📅 No events scheduled for Fri Sep 4 or beyond in the current data window.</div>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════════ -->
  <!--  SECTION 5 — JOB SEARCH & INTERVIEW PIPELINE              -->
  <!-- ═══════════════════════════════════════════════════════════ -->
  <div class="section theme-green">
    <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
    <div class="section-body">
      <table>
        <thead>
          <tr>
            <th>Fit</th>
            <th>Source</th>
            <th>Role / Company</th>
            <th>Salary / Detail</th>
            <th>Status</th>
            <th>Next Step</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><span class="tag tag-high">HIGH</span></td>
            <td>IBM Talent Acquisition (ibm.com)</td>
            <td><strong>IBM HR Network Opt-In</strong><br>Post-Confluent acquisition expansion</td>
            <td>Enterprise tech · Multiple roles</td>
            <td><span class="pill pill-red">Action Required</span></td>
            <td>Complete opt-in form immediately</td>
          </tr>
          <tr>
            <td><span class="tag tag-high">HIGH</span></td>
            <td>Indeed</td>
            <td><strong>Senior Vice President, Human Resources</strong><br>Brooklyn Navy Yard Development Corp</td>
            <td>$185,000 – $200,000/yr</td>
            <td><span class="pill pill-yellow">Review &amp; Apply</span></td>
            <td>Review listing, tailor application this weekend</td>
          </tr>
          <tr>
            <td><span class="tag tag-high">HIGH</span></td>
            <td>LinkedIn Job Alerts</td>
            <td><strong>Chief Human Resources Officer</strong><br>ORAU + 19 additional HR roles</td>
            <td>CHRO-level · 20 total alerts</td>
            <td><span class="pill pill-yellow">Review Needed</span></td>
            <td>Open LinkedIn, screen all 20 roles</td>
          </tr>
          <tr>
            <td><span class="tag tag-med">MED</span></td>
            <td>LinkedIn Job Alerts</td>
            <td><strong>Principal HR Business Partner</strong><br>PeopleOps Jobs + 39 more</td>
            <td>40 roles · Various levels</td>
            <td><span class="pill pill-yellow">Review Needed</span></td>
            <td>Screen batch for HRBP/Director+ roles</td>
          </tr>
          <tr>
            <td><span class="tag tag-med">MED</span></td>
            <td>LinkedIn Job Alerts</td>
            <td><strong>Director of People Operations</strong><br>ReKlame Health + 3 more</td>
            <td>$145K–$165K/yr</td>
            <td><span class="pill pill-gray">Read (not unread)</span></td>
            <td>Review if not yet acted on</td>
          </tr>
          <tr>
            <td><span class="tag tag-low">LOW</span></td>
            <td>Glassdoor Jobs</td>
            <td><strong>HR Business Partner</strong><br>CORA Physical Therapy + 8 (Remote)</td>
            <td>Medtronic also hiring</td>
            <td><span class="pill pill-gray">In Trash</span></td>
            <td>Restore from trash if interested; otherwise ignore</td>
          </tr>
          <tr>
            <td><span class="tag tag-low">LOW</span></td>
            <td>Glassdoor Jobs</td>
            <td><strong>Community Coordinator</strong><br>Van Police Dept + 8 (New York, NY)</td>
            <td>Likely below target level</td>
            <td><span class="pill pill-gray">In Trash</span></td>
            <td>Safe to delete — not a strong fit</td>
          </tr>
          <tr>
            <td>—</td>
            <td>LinkedIn Networking</td>
            <td><strong>HR Networking &amp; Job Search Group</strong><br>Sep 2, 12–1:30 PM (Zoom)</td>
            <td>180+ peers, job leads</td>
            <td><span class="pill pill-yellow">RSVP Pending</span></td>
            <td>Accept invite, prepare 60-sec intro</td>
          </tr>
          <tr>
            <td>—</td>
            <td>LinkedIn Networking</td>
            <td><strong>Open Office Hours — HR Network</strong><br>Sep 3, 12–1 PM (Zoom)</td>
            <td>Free-form discussion</td>
            <td><span class="pill pill-yellow">RSVP Pending</span></td>
            <td>Accept invite, prep questions</td>
          </tr>
          <tr>
            <td>—</td>
            <td>LinkedIn Connection</td>
            <td><strong>Precious Babalola</strong><br>Executive VA, Arise Capital Management</td>
            <td>Network expansion</td>
            <td><span class="pill pill-yellow">Pending Decision</span></td>
            <td>Review profile, accept or ignore</td>
          </tr>
          <tr>
            <td>—</td>
            <td>LinkedIn Connection</td>
            <td><strong>Victor Lue-Yat</strong><br>Founder &amp; Managing Partner, Kefika Group</td>
            <td>Network expansion</td>
            <td><span class="pill pill-gray">Already Read</span></td>
            <td>Review profile, decide to accept</td>
          </tr>
        </tbody>
      </table>
      <div class="note">💡 LinkedIn also shared a post by Johnny C. Taylor Jr. (SHRM-SCP) and Roli Agrawal (CSO) — consider engaging with content to boost visibility during job search.</div>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════════ -->
  <!--  SECTION 6 — FULL EMAIL REVIEW BY CATEGORY                -->
  <!-- ═══════════════════════════════════════════════════════════ -->
  <div class="section theme-dark">
    <div class="section-title">📂 Full Email Review by Category</div>
    <div class="section-body">

      <!-- SECURITY / RISK -->
      <div class="card">
        <div class="card-label label-red">🔴 SECURITY / RISK — 5 Emails</div>
        <div class="card-title">Phishing, Scams &amp; Suspicious Activity</div>
        <table style="margin-top:8px;">
          <thead><tr><th>Sender</th><th>Subject</th><th>Location</th><th>Action</th></tr></thead>
          <tbody>
            <tr>
              <td>Fake "CashApp" (random domain)</td>
              <td>Please CONFIRM #3514735901986 — $13,963.99 payment</td>
              <td>🗑 Auto-Trashed</td>
              <td><span class="pill pill-red">Phishing — No Action</span></td>
            </tr>
            <tr>
              <td>Fake "CashApp" (random domain) ×3</td>
              <td>You have received $15.99 — Raging Bull Casino (3 variants)</td>
              <td>🗑 Auto-Trashed</td>
              <td><span class="pill pill-red">Phishing — No Action</span></td>
            </tr>
            <tr>
              <td>Bank of America (legitimate)</td>
              <td>Online transfer exceeded limit — Account 7471, $255+</td>
              <td>📥 Inbox</td>
              <td><span class="pill pill-red">Verify immediately via BofA app</span></td>
            </tr>
          </tbody>
        </table>
        <div class="step step-red">→ 4 phishing emails auto-removed. Verify BofA alert via official channels only. Do not click email links.</div>
      </div>

      <!-- JOB SEARCH -->
      <div class="card">
        <div class="card-label label-green">🟢 JOB SEARCH — 7 Emails</div>
        <div class="card-title">Active Job Leads, Alerts &amp; Applications</div>
        <table style="margin-top:8px;">
          <thead><tr><th>Source</th><th>Role / Detail</th><th>Salary</th><th>Priority</th></tr></thead>
          <tbody>
            <tr><td>IBM Talent Acquisition (ibm.com)</td><td>Talent network opt-in — post-Confluent acquisition</td><td>TBD</td><td><span class="tag tag-high">HIGH — Act Now</span></td></tr>
            <tr><td>Indeed</td><td>SVP Human Resources — Brooklyn Navy Yard Dev Corp</td><td>$185K–$200K</td><td><span class="tag tag-high">HIGH</span></td></tr>
            <tr><td>LinkedIn Job Alerts</td><td>CHRO — ORAU + 19 more roles</td><td>Varies</td><td><span class="tag tag-high">HIGH</span></td></tr>
            <tr><td>LinkedIn Job Alerts</td><td>Principal HRBP — PeopleOps Jobs + 39 more</td><td>Varies</td><td><span class="tag tag-med">MED</span></td></tr>
            <tr><td>LinkedIn Job Alerts</td><td>Director People Operations — ReKlame Health + 3 more ($145K–$165K)</td><td>$145K–$165K</td><td><span class="tag tag-med">MED</span></td></tr>
            <tr><td>Glassdoor (Trash)</td><td>HRBP — CORA Physical Therapy + 8 (Remote)</td><td>—</td><td><span class="tag tag-low">LOW — Review</span></td></tr>
            <tr><td>Glassdoor (Trash)</td><td>Community Coordinator — Van Police Dept + 8 (NYC)</td><td>—</td><td><span class="tag tag-low">LOW — Delete</span></td></tr>
          </tbody>
        </table>
        <div class="step step-green">→ Prioritize IBM opt-in and Brooklyn Navy Yard application this weekend. Screen LinkedIn alerts for CHRO/SVP/VP roles.</div>
      </div>

      <!-- RECRUITERS / NETWORKING -->
      <div class="card">
        <div class="card-label label-purple">🟣 RECRUITERS / NETWORKING — 3 Emails</div>
        <div class="card-title">LinkedIn Connections &amp; Professional Outreach</div>
        <table style="margin-top:8px;">
          <thead><tr><th>Sender</th><th>Detail</th><th>Action</th></tr></thead>
          <tbody>
            <tr><td>Precious Babalola (LinkedIn)</td><td>Executive VA, Arise Capital Management — wants to connect</td><td>Review profile, decide</td></tr>
            <tr><td>Victor Lue-Yat (LinkedIn)</td><td>Founder &amp; Managing Partner, Kefika Group — wants to connect</td><td>Review profile, decide</td></tr>
            <tr><td>LinkedIn (updates)</td><td>Johnny C. Taylor Jr. (SHRM-SCP) shared on LinkedIn</td><td>Engage for visibility (in Trash)</td></tr>
          </tbody>
        </table>
        <div class="step">→ Review both LinkedIn connection requests and accept those who add value to your network. Engage with SHRM content for professional visibility.</div>
      </div>

      <!-- CALENDAR / EVENTS -->
      <div class="card">
        <div class="card-label label-blue">🔵 CALENDAR / EVENTS — 4 Events</div>
        <div class="card-title">Upcoming Google Calendar Events</div>
        <div class="card-body">Covered in detail in the Full 7-Day Calendar section. Summary: HR Networking Group (Sep 2, needsAction), Network personal block (Sep 2, confirmed), Executive Roundtable (Sep 3, declined), Open Office Hours (Sep 3, needsAction). Two RSVPs outstanding.</div>
        <div class="step step-yellow">→ RSVP for Sep 2 and Sep 3 HR networking events. Resolve Sep 2 scheduling conflict.</div>
      </div>

      <!-- MEDICAL / HEALTH -->
      <div class="card">
        <div class="card-label label-gray">⚕️ MEDICAL / HEALTH — 3 Emails (Spam)</div>
        <div class="card-title">Unsolicited Health &amp; GLP-1 Weight Loss Spam</div>
        <table style="margin-top:8px;">
          <thead><tr><th>Sender</th><th>Subject</th><th>Location</th></tr></thead>
          <tbody>
            <tr><td>GLP-1-by-DirectMeds (random domain)</td><td>"melissaw212, DirectMeds GLP-1 treatment helps you lose up to 40 lbs"</td><td>Not in inbox/trash — lingering spam</td></tr>
            <tr><td>GLP-1-by-DirectMeds (random domain)</td><td>"DirectMeds GLP-1 treatment helps you lose up to 40 lbs" (2nd copy)</td><td>Not in inbox/trash</td></tr>
            <tr><td>MEDVi GLP-1 (random domain)</td><td>"Finally serious about losing weight? Take Back Your Body"</td><td>Not in inbox/trash</td></tr>
          </tbody>
        </table>
        <div class="step step-red">→ All three are spam from random domains targeting Melissa's Gmail username. Mark as spam and delete. Do not click any links.</div>
      </div>

      <!-- FINANCIAL / BILLING -->
      <div class="card">
        <div class="card-label label-yellow">🟡 FINANCIAL / BILLING — 2 Emails</div>
        <div class="card-title">Bank of America Account Activity</div>
        <table style="margin-top:8px;">
          <thead><tr><th>Sender</th><th>Subject</th><th>Detail</th><th>Action</th></tr></thead>
          <tbody>
            <tr><td>Bank of America</td><td>Online transfer exceeded limit — Account 7471</td><td>Amount $255+ · Received Aug 29, 1:50 AM</td><td><span class="pill pill-red">Verify immediately</span></td></tr>
            <tr><td>Bank of America</td><td>Direct deposit credited — Account 7471</td><td>$1,900.00 from Goldman Sachs · Aug 28</td><td><span class="pill pill-green">No action — informational</span></td></tr>
          </tbody>
        </table>
        <div class="step step-yellow">→ $1,900 direct deposit from Goldman Sachs is noted (payroll or distribution). Transfer alert requires verification. Both emails are from the legitimate BofA domain.</div>
      </div>

      <!-- PROFESSIONAL DEVELOPMENT -->
      <div class="card">
        <div class="card-label label-purple">🟣 PROFESSIONAL DEVELOPMENT — 3 Emails</div>
        <div class="card-title">LinkedIn Content, Google Account Activity &amp; GitHub Notification</div>
        <table style="margin-top:8px;">
          <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
          <tbody>
            <tr><td>LinkedIn (Roli Agrawal, CSO)</td><td>"NTT DATA AI for Insurance" — strategic post shared</td><td>Read for industry insight</td></tr>
            <tr><td>Google (noreply-accounts)</td><td>You shared Google Account data with Slack — sign-in confirmed</td><td>Verify this was you; no action if expected</td></tr>
            <tr><td>netlify[bot] via GitHub</td><td>PR #8 — Stop treating Employee Handbook as generic (Deploy preview ready)</td><td>Review if Melissa is actively working on this project</td></tr>
          </tbody>
        </table>
        <div class="step">→ GitHub PR deploy preview is ready (missophs/People-Action-Check#8). If this is Melissa's active project, review the preview. Google/Slack auth appears legitimate — verify if unexpected.</div>
      </div>

      <!-- PERSONAL -->
      <div class="card">
        <div class="card-label label-blue">🔵 PERSONAL — 3 Emails</div>
        <div class="card-title">Match.com Notifications &amp; Facebook</div>
        <table style="margin-top:8px;">
          <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
          <tbody>
            <tr><td>Match.com</td><td>Sean likes you — see if it's mutual</td><td>Personal — check when convenient</td></tr>
            <tr><td>Match.com</td><td>GuyUnfinished (58, Union NJ) viewed your profile</td><td>Personal — review profile if interested</td></tr>
            <tr><td>Facebook (Trash)</td><td>13 updates about Vali Valicutza and Rosario De Rincon</td><td>In Trash — check Facebook directly</td></tr>
          </tbody>
        </table>
        <div class="step">→ Match.com emails are legitimate personal notifications. Review at leisure. Facebook notification already in trash — check app directly.</div>
      </div>

      <!-- SUPABASE -->
      <div class="card">
        <div class="card-label label-blue">🔵 ACCOUNT / TECH — 1 Email</div>
        <div class="card-title">Supabase Auth: Sign-In Link</div>
        <div class="card-meta">From: Supabase Auth &lt;noreply@mail.app.supabase.io&gt; · Received: Sat Aug 29, 1:06 AM</div>
        <div class="card-body">Sign-in link sent for a Supabase account (likely connected to the GitHub/People-Action-Check project or another tool Melissa is using). Already read. Link has expired (one-time use, short expiry). No action needed unless login was unsuccessful.</div>
        <div class="step">→ No action needed. If login failed, request a new sign-in link from Supabase.</div>
      </div>

      <!-- ADULT / NSFW SPAM -->
      <div class="card">
        <div class="card-label label-red">🔴 ADULT SPAM — 5 Emails (All Trash / Junk)</div>
        <div class="card-title">Unsolicited Adult Content &amp; Male Enhancement Spam</div>
        <div class="card-body">Five deeply inappropriate and explicit spam emails arrived from random domains. All are in Trash or should be immediately trashed. Subjects include sexual content clearly not targeted appropriately. These are dangerous — some may attempt to harvest credentials or install malware via links.</div>
        <table style="margin-top:8px;">
          <thead><tr><th>Sender Handle</th><th>Subject (sanitized)</th><th>Location</th></tr></thead>
          <tbody>
            <tr><td>F*ckMeHard (random domain)</td><td>[Explicit adult solicitation] melissaw212</td><td>Not in inbox/trash — lingering spam</td></tr>
            <tr><td>Baking Soda Boner (random domain)</td><td>"Every woman's fantasy" (NSFW) — ×2 copies</td><td>Both in Trash</td></tr>
            <tr><td>Get_Hard (random domain)</td><td>"1 simple trick turning men into unstoppable sex machines"</td><td>Not in inbox/trash — lingering spam</td></tr>
            <tr><td>"10-inch" (random domain)</td><td>[Explicit adult content with porn star reference] (Trash)</td><td>In Trash</td></tr>
          </tbody>
        </table>
        <div class="step step-red">→ Mark all as spam immediately. Consider enabling stronger Gmail spam filters. Do not click any links in these emails.</div>
      </div>

      <!-- NEWSLETTERS / SUBSCRIPTIONS -->
      <div class="card">
        <div class="card-label label-purple">🟣 NEWSLETTERS / SUBSCRIPTIONS — 2 Emails</div>
        <div class="card-title">Dylan's Diary (Finance) &amp; Alison Courses</div>
        <table style="margin-top:8px;">
          <thead><tr><th>Sender</th><th>Subject</th><th>Location</th><th>Recommendation</th></tr></thead>
          <tbody>
            <tr><td>Dylan's Diary (Behind the Markets)</td><td>Nvidia's Best Quarter Ever — the company they tried to buy</td><td>In Trash</td><td>Keep if interested in finance/market news; otherwise unsubscribe</td></tr>
            <tr><td>Alison Courses</td><td>"Wondering how credible Alison courses are, Melissa A?"</td><td>In Trash</td><td>Unsubscribe — marketing email, not educational content</td></tr>
          </tbody>
        </table>
        <div class="step">→ Review Dylan's Diary for financial interest. Unsubscribe from Alison if not actively using their platform.</div>
      </div>

      <!-- PROMOTIONAL / RETAIL -->
      <div class="card">
        <div class="card-label label-gray">⬜ PROMOTIONAL / RETAIL — 10 Emails</div>
        <div class="card-title">Old Navy, SHEIN, Kohl's, Amazon — see Promotional section below</div>
        <div class="card-body">10 retail/promotional emails received across 5 brands. Most already in Trash. Full details in the Promotional/Retail Summary section.</div>
        <div class="step">→ Review Promotional section below for deal summaries. Most can be ignored or deleted.</div>
      </div>

      <!-- CASINO / GAMBLING SPAM -->
      <div class="card">
        <div class="card-label label-red">🔴 CASINO / GAMBLING SPAM — 9 Emails</div>
        <div class="card-title">Online Casino Spam — Do Not Engage</div>
        <table style="margin-top:8px;">
          <thead><tr><th>Sender</th><th>Subject</th><th>Location</th></tr></thead>
          <tbody>
            <tr><td>Big Dollar Casino (×2)</td><td>130 Free Spins Pending (×2)</td><td>Both in Trash</td></tr>
            <tr><td>"Congratulations" (×2)</td><td>200 Free Spins No Deposit (×2)</td><td>One in Trash, one lingering</td></tr>
            <tr><td>OnlineCasino</td><td>130 Free Spins Pending</td><td>Not in inbox/trash — lingering</td></tr>
            <tr><td>Extreme_Casino</td><td>Get 200 Free Spins — code GRIFFINS200</td><td>Not in inbox/trash — lingering</td></tr>
            <tr><td>Lucky Creek Casino</td><td>Register Today — 80 Spins Free</td><td>In Trash</td></tr>
            <tr><td>"Congratulations" (Lucky Creek)</td><td>200 Free Spins — code FREESPIN (in Trash)</td><td>In Trash</td></tr>
            <tr><td>Lucky Creek Casino promo</td><td>200 Free Spins — code LITTLE130GRF (lingering)</td><td>Not in inbox/trash</td></tr>
          </tbody>
        </table>
        <div class="step step-red">→ Mark all as spam and delete. These are fraudulent casino promotions from random domains harvesting email addresses. Never click their links.</div>
      </div>

      <!-- OLD NAVY CART ABANDONMENT -->
      <div class="card">
        <div class="card-label label-gray">⬜ SAFE TO DELETE / IGNORE — 3 Emails</div>
        <div class="card-title">Old Navy Cart Abandonment, LinkedIn Digest (Trash), Holy_Vigor Spam</div>
        <table style="margin-top:8px;">
          <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
          <tbody>
            <tr><td>Old Navy</td><td>Your cart has something in it — must-haves waiting</td><td>In Trash — delete</td></tr>
            <tr><td>LinkedIn (Trash)</td><td>Johnny C. Taylor Jr. and others share on LinkedIn</td><td>In Trash — safe to delete or read first</td></tr>
            <tr><td>Holy_Vigor (random domain)</td><td>"Real root cause of limp performances" — explicit spam</td><td>Not in inbox/trash — mark spam, delete</td></tr>
          </tbody>
        </table>
        <div class="step">→ All three are safe to delete. No action required.</div>
      </div>

    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════════ -->
  <!--  SECTION 7 — TRASH REVIEW                                  -->
  <!-- ═══════════════════════════════════════════════════════════ -->
  <div class="section theme-red">
    <div class="section-title">🗑️ Trash Review</div>
    <div class="section-body">

      <div class="card">
        <div class="card-label label-green">✅ RESTORE IMMEDIATELY</div>
        <div class="card-title">No emails in Trash recommend restoration.</div>
        <div class="card-body" style="color:#718096;">All legitimate emails (BofA, IBM, job alerts, LinkedIn) are correctly in the Inbox or other non-trash folders. Nothing currently in Trash requires restoration.</div>
      </div>

      <div class="card">
        <div class="card-label label-yellow">🟡 REVIEW BEFORE DELETING</div>
        <div class="card-title">These may have marginal value — quick glance recommended</div>
        <table style="margin-top:8px;">
          <thead><tr><th>Sender</th><th>Subject</th><th>Reason to Review</th></tr></thead>
          <tbody>
            <tr><td>Glassdoor Jobs</td><td>HR Business Partner at CORA Physical Therapy + 8 (Remote)</td><td>Could contain relevant remote HR roles worth reviewing before deleting</td></tr>
            <tr><td>Glassdoor Jobs</td><td>Community Coordinator at Van Police Dept + 8 (New York)</td><td>Likely below target level but scan quickly if time allows</td></tr>
            <tr><td>Dylan's Diary</td><td>Nvidia's Best Quarter Ever</td><td>Finance/market newsletter — read if you follow Nvidia or market news</td></tr>
            <tr><td>LinkedIn (updates)</td><td>Johnny C. Taylor Jr., SHRM-SCP and others share thoughts</td><td>SHRM leadership content — may be worth engaging for professional visibility</td></tr>
            <tr><td>Facebook</td><td>13 updates about Vali and others</td><td>Personal — check if you want to see updates on these contacts</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card">
        <div class="card-label label-red">🗑 AUTO-TRASHED — PHISHING (4 emails)</div>
        <div class="card-title">Removed before reaching inbox — no action needed</div>
        <table style="margin-top:8px;">
          <thead><tr><th>Sender</th><th>Subject</th><th>Reason</th></tr></thead>
          <tbody>
            <tr><td>Fake "CashApp" (ktwv.iltcwcvtptuyn.us)</td><td>CONFIRM #3514735901986 — $13,963.99 payment</td><td>Auto-Trashed
