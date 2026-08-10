<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa | Monday, August 10, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header .subtitle { font-size: 15px; color: #a0b4d6; margin-top: 6px; }
  .header-meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header-meta div { background: rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 18px; }
  .header-meta .label { font-size: 11px; color: #7a9cc0; text-transform: uppercase; letter-spacing: 0.8px; }
  .header-meta .value { font-size: 20px; font-weight: 700; color: #e0ecff; }

  /* SECTION HEADERS */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: #fff; padding: 8px 16px; border-radius: 6px 6px 0 0; display: flex; align-items: center; gap: 8px; }
  .section-title.red { background: #c0392b; }
  .section-title.yellow { background: #d4a017; }
  .section-title.blue { background: #1565c0; }
  .section-title.green { background: #1b7a3e; }
  .section-title.purple { background: #6a1b9a; }
  .section-title.gray { background: #5a6475; }
  .section-title.dark { background: #1a1a2e; }
  .section-title.teal { background: #00695c; }
  .section-title.orange { background: #bf360c; }

  .section-body { background: #fff; border-radius: 0 0 8px 8px; padding: 18px 20px; border: 1px solid #e0e4ef; border-top: none; }

  /* CARDS */
  .card { border-radius: 8px; padding: 14px 16px; margin-bottom: 12px; border-left: 4px solid; }
  .card.red { background: #fff5f5; border-color: #c0392b; }
  .card.yellow { background: #fffdf0; border-color: #d4a017; }
  .card.blue { background: #f0f6ff; border-color: #1565c0; }
  .card.green { background: #f0fff4; border-color: #1b7a3e; }
  .card.purple { background: #fdf5ff; border-color: #6a1b9a; }
  .card.gray { background: #f7f8fa; border-color: #9aa3b2; }
  .card.teal { background: #f0faf8; border-color: #00695c; }
  .card-title { font-weight: 700; font-size: 13px; margin-bottom: 4px; }
  .card-meta { font-size: 11px; color: #6b7280; margin-bottom: 6px; }
  .card-row { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 4px; }
  .badge { display: inline-block; font-size: 10px; font-weight: 700; text-transform: uppercase; padding: 2px 8px; border-radius: 10px; letter-spacing: 0.6px; }
  .badge.red { background: #fde8e8; color: #c0392b; }
  .badge.yellow { background: #fef9e7; color: #a07800; }
  .badge.blue { background: #e8f0fe; color: #1565c0; }
  .badge.green { background: #e6f4ea; color: #1b7a3e; }
  .badge.purple { background: #f3e8fd; color: #6a1b9a; }
  .badge.gray { background: #edf0f5; color: #5a6475; }
  .badge.orange { background: #fde8e0; color: #bf360c; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #f3f4f8; color: #374151; font-weight: 700; padding: 9px 12px; text-align: left; border-bottom: 2px solid #d1d5db; font-size: 11px; text-transform: uppercase; letter-spacing: 0.6px; }
  td { padding: 9px 12px; border-bottom: 1px solid #e5e7eb; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f9fafb; }
  .triage-status { font-weight: 700; white-space: nowrap; }
  .status-inbox { color: #1565c0; }
  .status-rescued { color: #1b7a3e; }
  .status-trash-auto { color: #c0392b; }
  .status-trash-manual { color: #9aa3b2; }

  /* EXEC SUMMARY */
  .exec-bullets { list-style: none; }
  .exec-bullets li { padding: 10px 14px; margin-bottom: 8px; border-radius: 6px; font-size: 13px; font-weight: 500; display: flex; gap: 10px; align-items: flex-start; }
  .exec-bullets li.risk { background: #fff0f0; border-left: 4px solid #c0392b; }
  .exec-bullets li.opp { background: #f0fff4; border-left: 4px solid #1b7a3e; }
  .exec-bullets li.cal { background: #f0f6ff; border-left: 4px solid #1565c0; }

  /* CAL EVENTS */
  .cal-day { margin-bottom: 16px; }
  .cal-day-header { font-size: 12px; font-weight: 700; text-transform: uppercase; color: #1565c0; letter-spacing: 1px; margin-bottom: 8px; border-bottom: 2px solid #1565c0; padding-bottom: 4px; }
  .cal-event { background: #f0f6ff; border: 1px solid #bfd4f5; border-radius: 7px; padding: 10px 14px; margin-bottom: 8px; }
  .cal-event-title { font-weight: 700; font-size: 13px; color: #1a1a2e; }
  .cal-event-time { font-size: 11px; color: #1565c0; font-weight: 600; margin-bottom: 4px; }
  .cal-event-meta { font-size: 11px; color: #555; margin-top: 4px; }
  .cal-rsvp.confirmed { color: #1b7a3e; font-weight: 700; }
  .cal-rsvp.needsAction { color: #d4a017; font-weight: 700; }
  .cal-rsvp.declined { color: #c0392b; font-weight: 700; }
  .cal-conflict { background: #fff3cd; border: 1px solid #f0c030; border-radius: 5px; font-size: 11px; color: #7a5500; padding: 4px 8px; margin-top: 6px; font-weight: 600; }

  /* ACTION ITEMS */
  .priority-high { color: #c0392b; font-weight: 700; }
  .priority-med { color: #d4a017; font-weight: 700; }
  .priority-low { color: #1b7a3e; font-weight: 700; }
  .fit-high { background: #e6f4ea; color: #1b7a3e; }
  .fit-med { background: #fef9e7; color: #a07800; }
  .fit-low { background: #f3f4f8; color: #5a6475; }

  /* DASHBOARD */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-card { background: #fff; border-radius: 9px; padding: 14px 16px; border: 1px solid #e0e4ef; }
  .dash-card-label { font-size: 10px; text-transform: uppercase; letter-spacing: 0.8px; color: #7a9cc0; font-weight: 700; margin-bottom: 6px; }
  .dash-card-value { font-size: 24px; font-weight: 800; color: #1a1a2e; }
  .dash-card-sub { font-size: 11px; color: #6b7280; margin-top: 4px; }

  /* TOP 3 */
  .top3 { counter-reset: top3; }
  .top3-item { background: linear-gradient(90deg, #1a1a2e 0%, #0f3460 100%); color: #fff; border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; display: flex; gap: 16px; align-items: flex-start; }
  .top3-num { font-size: 32px; font-weight: 900; color: rgba(255,255,255,0.18); line-height: 1; min-width: 36px; }
  .top3-content h3 { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
  .top3-content p { font-size: 12px; color: #a0b4d6; }

  /* MISC */
  .pill { display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 11px; font-weight: 600; margin-right: 4px; }
  .pill.red { background: #fde8e8; color: #c0392b; }
  .pill.green { background: #e6f4ea; color: #1b7a3e; }
  .pill.yellow { background: #fef9e7; color: #a07800; }
  .pill.blue { background: #e8f0fe; color: #1565c0; }
  .pill.gray { background: #edf0f5; color: #5a6475; }
  .note { font-size: 11px; color: #6b7280; font-style: italic; margin-top: 6px; }
  .divider { border: none; border-top: 1px solid #e5e7eb; margin: 14px 0; }
  .warn { color: #c0392b; font-weight: 700; }
  a { color: #1565c0; text-decoration: none; }
  .sub-header { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; color: #374151; margin: 14px 0 6px; border-bottom: 1px solid #e5e7eb; padding-bottom: 4px; }
  .email-row td:first-child { white-space: nowrap; }
  .accounting-total td { font-weight: 700; background: #f3f4f8; border-top: 2px solid #1a1a2e; }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ═══════════════════════════════════════════════════════════
     SECTION 0 — EMAIL TRIAGE QUICK LIST
═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title dark">⚡ Email Triage Quick List</div>
  <div class="section-body" style="padding:0;">
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
        <!-- INBOX EMAILS (individual rows) -->
        <tr>
          <td class="triage-status status-inbox">📥 INBOX</td>
          <td>Match</td>
          <td>Kevin likes you. See if it's mutual.</td>
          <td>Dating app notification — Match.com</td>
        </tr>
        <tr>
          <td class="triage-status status-inbox">📥 INBOX</td>
          <td>Match</td>
          <td>David Timberland likes you. See if it's mutual.</td>
          <td>Dating app notification — Match.com</td>
        </tr>
        <tr>
          <td class="triage-status status-inbox">📥 INBOX</td>
          <td>Scovai</td>
          <td>1 new position matches your profile</td>
          <td>Strong match: Chief People &amp; Culture Officer — Omnisage LLC</td>
        </tr>
        <tr>
          <td class="triage-status status-inbox">📥 INBOX</td>
          <td>Notify NYC</td>
          <td>Missing Child Alert — Tarunvir Garcha (NYC)</td>
          <td>NYC emergency alert — 18-yr-old missing from Jericho, NY</td>
        </tr>
        <tr>
          <td class="triage-status status-inbox">📥 INBOX</td>
          <td>SourceHire Jobs</td>
          <td>Confidential — Interview Update (Sr Director HR) REQ93079 [1 of 2]</td>
          <td>Confirm work authorization to keep application moving</td>
        </tr>
        <tr>
          <td class="triage-status status-inbox">📥 INBOX</td>
          <td>SourceHire Jobs</td>
          <td>Confidential — Interview Update (Sr Director HR) REQ93079 [2 of 2]</td>
          <td>Duplicate — same request, earlier send time</td>
        </tr>
        <tr>
          <td class="triage-status status-inbox">📥 INBOX</td>
          <td>Carmel Points</td>
          <td>Your Carmel Points for July [Copy 1]</td>
          <td>Monthly loyalty statement — review points balance</td>
        </tr>
        <tr>
          <td class="triage-status status-inbox">📥 INBOX</td>
          <td>Carmel Points</td>
          <td>Your Carmel Points for July [Copy 2]</td>
          <td>Duplicate of above — likely a send error</td>
        </tr>
        <tr>
          <td class="triage-status status-inbox">📥 INBOX</td>
          <td>Match</td>
          <td>You've had a profile view from Phil (67, Union City NJ)</td>
          <td>Dating app notification — Match.com</td>
        </tr>
        <tr>
          <td class="triage-status status-inbox">📥 INBOX</td>
          <td>LinkedIn</td>
          <td>New jobs similar to Director of HR at Special Narcotics Prosecutor</td>
          <td>LinkedIn job alert — HR Director-level roles</td>
        </tr>
        <tr>
          <td class="triage-status status-inbox">📥 INBOX</td>
          <td>ChatGPT / OpenAI</td>
          <td>Check your route before you go</td>
          <td>OpenAI travel/route tip email</td>
        </tr>
        <tr>
          <td class="triage-status status-inbox">📥 INBOX</td>
          <td>Match</td>
          <td>Jay likes you. See if it's mutual.</td>
          <td>Dating app notification — Match.com</td>
        </tr>
        <tr>
          <td class="triage-status status-inbox">📥 INBOX</td>
          <td>LinkedIn Job Alerts</td>
          <td>Head of People Operations (Canada) at CSC Generation</td>
          <td>LinkedIn job alert — Head of People role</td>
        </tr>
        <tr>
          <td class="triage-status status-inbox">📥 INBOX</td>
          <td>Match</td>
          <td>Endri likes you. See if it's mutual.</td>
          <td>Dating app notification — Match.com</td>
        </tr>
        <tr>
          <td class="triage-status status-inbox">📥 INBOX</td>
          <td>Amazon</td>
          <td>Return request confirmed — UPNET Women's high Waisted...</td>
          <td>Amazon return accepted for "Sophie" — verify account</td>
        </tr>
        <tr>
          <td class="triage-status status-inbox">📥 INBOX</td>
          <td>Amazon</td>
          <td>Return request confirmed — Arach&amp;Cloz Women's...</td>
          <td>Amazon return accepted for "Sophie" — verify account</td>
        </tr>
        <!-- TRASH SUMMARY ROWS -->
        <tr style="background:#fff8f8;">
          <td class="triage-status status-trash-auto">🗑 AUTO-TRASHED</td>
          <td colspan="2"><strong>4 emails auto-trashed (phishing/scam)</strong> — see Trash Review</td>
          <td>Advance-fee scam, fake account suspension, casino spam, adult spam</td>
        </tr>
        <tr style="background:#f7f8fa;">
          <td class="triage-status status-trash-manual">🗂 TRASH (manual)</td>
          <td colspan="2"><strong>30 emails in Trash</strong> — see Trash Review</td>
          <td>Newsletters, retail promos, dating apps, adult spam, misc unsubscribes</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 1 — HEADER
═══════════════════════════════════════════════════════════ -->
<div class="header">
  <h1>☀️ Good Morning, Melissa</h1>
  <div class="subtitle">Executive Briefing — Prepared by Your Chief of Staff</div>
  <div class="header-meta">
    <div>
      <div class="label">Date</div>
      <div class="value" style="font-size:15px;">Monday, August 10, 2026</div>
    </div>
    <div>
      <div class="label">Emails Reviewed</div>
      <div class="value">50</div>
    </div>
    <div>
      <div class="label">Calendar Events</div>
      <div class="value">7</div>
    </div>
    <div>
      <div class="label">Action Required</div>
      <div class="value" style="color:#ffcc80;">6</div>
    </div>
    <div>
      <div class="label">Security Flags</div>
      <div class="value" style="color:#ff8a80;">4</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 2 — EXECUTIVE SUMMARY
═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title red">🔍 Executive Summary</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li class="risk">🚨 <strong>Security Risk:</strong> 4 emails were auto-trashed as high-confidence phishing/scam (advance-fee fraud, fake account suspension, casino scam, adult spam). Additionally, 2 Amazon return confirmations addressed to "Sophie" arrived in your inbox — verify your Amazon account for unauthorized activity immediately.</li>
      <li class="opp">💼 <strong>Job Search:</strong> Two active job leads require immediate attention: SourceHire sent duplicate emails requesting you confirm work authorization for a Sr. Director of HR role (REQ93079). Scovai flagged a strong-match Chief People &amp; Culture Officer role at Omnisage LLC. LinkedIn also surfaced additional Head of People alerts.</li>
      <li class="cal">📅 <strong>Calendar / Deadline:</strong> Your MRI Brain W&amp;WO with IV Contrast is tomorrow (Tuesday, Aug 11) at 9:20 AM — arrive by 8:50 AM at 159 E 53rd St, 6th Floor. Two HR Networking Zoom meetings on Wednesday (Aug 12) have no RSVP yet. The Executive Roundtable on Thursday (Aug 13) shows as declined.</li>
    </ul>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 3 — ACTION REQUIRED
═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title yellow">⚠️ Action Required</div>
  <div class="section-body">

    <div class="card red">
      <div class="card-row"><span class="badge red">🚨 URGENT — SECURITY</span></div>
      <div class="card-title">Suspicious Amazon Returns for "Sophie" — Verify Account</div>
      <div class="card-meta">From: return@amazon.com | Received: Mon Aug 10, 12:37 AM</div>
      <p>Two return confirmations arrived addressed to <strong>"Sophie"</strong> — not Melissa. This may indicate unauthorized account use, account sharing, or an account merge issue.</p>
      <p style="margin-top:6px;"><strong>Next Step:</strong> Log into Amazon immediately and verify recent orders, returns, and account access. Check if any unauthorized addresses are on your account. If not your returns, contact Amazon support.</p>
      <p class="note">Due: Today, August 10</p>
    </div>

    <div class="card red">
      <div class="card-row"><span class="badge red">🚨 URGENT — JOB SEARCH</span></div>
      <div class="card-title">SourceHire: Confirm Work Authorization — Sr Director HR (REQ93079)</div>
      <div class="card-meta">From: SourceHire Jobs &lt;jobs@sourcehire.app&gt; | 2 duplicate emails received</div>
      <p>A confidential employer is requesting you confirm your visa/sponsorship status to keep your Sr. Director of Human Resources application active. Two identical emails were sent (5:49 AM and 7:03 AM). The duplicate suggests possible urgency or a system re-send.</p>
      <p style="margin-top:6px;"><strong>Next Step:</strong> Reply to SourceHire confirming your work authorization status. Disregard one of the duplicates. Flag if the sender domain seems suspicious.</p>
      <p class="note">Due: Today, August 10 — application may stall without response</p>
    </div>

    <div class="card yellow">
      <div class="card-row"><span class="badge yellow">📅 RSVP NEEDED</span></div>
      <div class="card-title">HR Networking &amp; Job Search Group — Zoom (Wed Aug 12, 12–1:30 PM)</div>
      <div class="card-meta">From: Calendar Invite | Status: Needs Action (no RSVP)</div>
      <p>Large HR networking Zoom with 170+ attendees. RSVP is pending. A separate "Network" block at the same time is confirmed — likely representing the same event. Confirm whether you are attending and update your RSVP.</p>
      <p style="margin-top:6px;"><strong>Next Step:</strong> Accept or decline the HR Networking Zoom invite before Wednesday.</p>
      <p class="note">Due: Before Wednesday, Aug 12, 12:00 PM</p>
    </div>

    <div class="card yellow">
      <div class="card-row"><span class="badge yellow">📅 RSVP NEEDED</span></div>
      <div class="card-title">HR Networking Open Office Hours — Zoom (Thu Aug 13, 12–1 PM)</div>
      <div class="card-meta">From: Calendar Invite | Status: Needs Action (no RSVP)</div>
      <p>Open office hours Zoom for HR job seekers. Note says: turn off automated notetaking AI tools. Status is "needsAction."</p>
      <p style="margin-top:6px;"><strong>Next Step:</strong> Accept or decline. If attending, disable Otter.ai or similar tools per the host's request.</p>
      <p class="note">Due: Before Thursday, Aug 13</p>
    </div>

    <div class="card blue">
      <div class="card-row"><span class="badge blue">📋 PREP NEEDED</span></div>
      <div class="card-title">MRI Brain W&amp;WO IVC — Tomorrow, Tuesday Aug 11 (Arrive 8:50 AM)</div>
      <div class="card-meta">Location: 159 E 53rd Street, 6th Floor, NY 10022 | Phone: 646-754-2800</div>
      <p>Appointment time is 9:20 AM; arrive no later than 8:50 AM. Remove all body piercings. Leave valuables at home. MRI-safe gown will be provided. IV contrast will be administered.</p>
      <p style="margin-top:6px;"><strong>Next Step:</strong> Plan travel tonight. Leave valuables at home. No metal accessories.</p>
      <p class="note">Due: Tomorrow morning, August 11</p>
    </div>

    <div class="card green">
      <div class="card-row"><span class="badge green">💼 OPPORTUNITY</span></div>
      <div class="card-title">Scovai: Strong Match — Chief People &amp; Culture Officer at Omnisage LLC</div>
      <div class="card-meta">From: Scovai &lt;no-reply@scovai.com&gt; | Received: Mon Aug 10, 9:04 AM</div>
      <p>Scovai flagged this as a "Strong Match" for your profile. Chief People and Culture Officer is a C-suite level role — well aligned to your HR Director/VP-level background.</p>
      <p style="margin-top:6px;"><strong>Next Step:</strong> Log into Scovai and review the full posting. Apply if aligned. Research Omnisage LLC before applying.</p>
      <p class="note">Due: This week</p>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 4 — FULL 7-DAY CALENDAR
═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title blue">📅 Full 7-Day Calendar (Aug 10–16, 2026)</div>
  <div class="section-body">

    <div class="cal-day">
      <div class="cal-day-header">Monday, August 10, 2026 — TODAY</div>
      <div class="cal-event">
        <div class="cal-event-time">8:00 AM – 9:00 AM</div>
        <div class="cal-event-title">💉 Stephanie Infusion</div>
        <div class="cal-event-meta"><span class="cal-rsvp confirmed">✅ Confirmed</span> &nbsp;|&nbsp; Location: Not specified &nbsp;|&nbsp; No attendees listed</div>
        <div class="cal-event-meta" style="margin-top:4px;"><strong>Prep:</strong> This event appears to be an infusion appointment for someone named Stephanie — possibly a caregiver obligation or personal health appointment. Confirm location and any needed supplies.</div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">Tuesday, August 11, 2026</div>
      <div class="cal-event" style="background:#fff0f0; border-color:#c0392b;">
        <div class="cal-event-time" style="color:#c0392b;">8:50 AM ARRIVE → 9:20 AM Appointment – 9:40 AM Est. End</div>
        <div class="cal-event-title">🧠 MRI Brain W&amp;WO IVC (with IV Contrast)</div>
        <div class="cal-event-meta"><span class="cal-rsvp confirmed">✅ Confirmed</span> &nbsp;|&nbsp; <strong>Location:</strong> 159 E 53rd Street, 6th Floor, New York, NY 10022 &nbsp;|&nbsp; Phone: 646-754-2800</div>
        <div class="cal-event-meta" style="margin-top:4px;"><strong>Prep Required:</strong> Arrive by 8:50 AM (appointment is 9:20 AM). Leave valuables at home. Remove all body piercings and metal. MRI-safe gown provided. Private dressing rooms available. IV contrast will be used — notify staff of any allergies or kidney concerns.</div>
        <div class="cal-conflict">⚠️ Allow ample transit time from your location to 159 E 53rd St by 8:50 AM.</div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">Wednesday, August 12, 2026</div>
      <div class="cal-event">
        <div class="cal-event-time">9:30 AM – 10:30 AM</div>
        <div class="cal-event-title">🏥 PT (Physical Therapy)</div>
        <div class="cal-event-meta"><span class="cal-rsvp confirmed">✅ Confirmed</span> &nbsp;|&nbsp; Location: Not specified &nbsp;|&nbsp; No attendees listed</div>
        <div class="cal-event-meta" style="margin-top:4px;"><strong>Prep:</strong> Wear comfortable attire. Confirm location/provider if not on file.</div>
      </div>
      <div class="cal-event" style="background:#fdf5ff; border-color:#6a1b9a;">
        <div class="cal-event-time" style="color:#6a1b9a;">12:00 PM – 1:30 PM</div>
        <div class="cal-event-title">🤝 HR Networking &amp; Job Search Group — Zoom 2</div>
        <div class="cal-event-meta"><span class="cal-rsvp needsAction">⚠️ RSVP PENDING</span> &nbsp;|&nbsp; <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a> &nbsp;|&nbsp; 170+ attendees</div>
        <div class="cal-event-meta" style="margin-top:4px;"><strong>Prep:</strong> Review HR Networking Team Guidelines. Prepare brief intro. Respond to RSVP before meeting.</div>
        <div class="cal-conflict">⚠️ Duplicate "Network" block also at 12:00–1:30 PM (confirmed) — likely same event. No conflict if same meeting.</div>
      </div>
      <div class="cal-event">
        <div class="cal-event-time">12:00 PM – 1:30 PM</div>
        <div class="cal-event-title">🔗 Network (Personal Calendar Block)</div>
        <div class="cal-event-meta"><span class="cal-rsvp confirmed">✅ Confirmed</span> &nbsp;|&nbsp; No location &nbsp;|&nbsp; Likely same as HR Networking Zoom above</div>
        <div class="cal-event-meta" style="margin-top:4px;"><strong>Prep:</strong> Confirm this is the same Zoom. If separate, identify the meeting link.</div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">Thursday, August 13, 2026</div>
      <div class="cal-event" style="background:#fff5f5; border-color:#c0392b;">
        <div class="cal-event-time" style="color:#c0392b;">9:00 AM – 10:30 AM</div>
        <div class="cal-event-title">🏢 Executive Roundtable (John Madigan)</div>
        <div class="cal-event-meta"><span class="cal-rsvp declined">❌ DECLINED</span> &nbsp;|&nbsp; <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> &nbsp;|&nbsp; Meeting ID: 207 786 667 | PW: 205454</div>
        <div class="cal-event-meta" style="margin-top:4px;"><strong>Note:</strong> You have declined this event. If this was intentional, no action needed. If you wish to rejoin, contact John Madigan and update your RSVP.</div>
      </div>
      <div class="cal-event" style="background:#fdf5ff; border-color:#6a1b9a;">
        <div class="cal-event-time" style="color:#6a1b9a;">12:00 PM – 1:00 PM</div>
        <div class="cal-event-title">🤝 HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
        <div class="cal-event-meta"><span class="cal-rsvp needsAction">⚠️ RSVP PENDING</span> &nbsp;|&nbsp; <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a> &nbsp;|&nbsp; 170+ attendees</div>
        <div class="cal-event-meta" style="margin-top:4px;"><strong>Prep:</strong> Disable automated AI notetaking tools (Otter.ai, etc.) per host request. Open discussion format — no recording. RSVP before meeting.</div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">Friday, August 14 — Sunday, August 16, 2026</div>
      <div class="cal-event" style="background:#f7f8fa; border-color:#9aa3b2;">
        <div class="cal-event-title" style="color:#5a6475;">No calendar events scheduled</div>
        <div class="cal-event-meta">Use this time for job search follow-ups, self-care, or rest.</div>
      </div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 5 — JOB SEARCH & INTERVIEW PIPELINE
═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title green">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">

    <div class="sub-header">🔴 Immediate Action — Recruiter Outreach</div>
    <table>
      <thead>
        <tr><th>Fit</th><th>Role</th><th>Company</th><th>Source</th><th>Status</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="badge green fit-high">HIGH</span></td>
          <td>Chief People &amp; Culture Officer</td>
          <td>Omnisage LLC</td>
          <td>Scovai</td>
          <td>New match, unreviewed</td>
          <td>Log in &amp; apply today</td>
        </tr>
        <tr>
          <td><span class="badge yellow fit-med">MED</span></td>
          <td>Sr. Director of Human Resources (Full-Time) REQ93079</td>
          <td>Confidential</td>
          <td>SourceHire Jobs</td>
          <td>⚠️ Awaiting work auth confirmation (2 emails sent)</td>
          <td>Reply to SourceHire TODAY</td>
        </tr>
      </tbody>
    </table>

    <div class="sub-header">🟡 Active Job Alerts — Review This Week</div>
    <table>
      <thead>
        <tr><th>Fit</th><th>Role</th><th>Company</th><th>Source</th><th>Status</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="badge yellow fit-med">MED</span></td>
          <td>Head of People - U.S.</td>
          <td>Elliptic</td>
          <td>LinkedIn Job Alerts</td>
          <td>Unread alert (prior day)</td>
          <td>Review role &amp; apply if fit</td>
        </tr>
        <tr>
          <td><span class="badge yellow fit-med">MED</span></td>
          <td>Head of People Operations (Canada)</td>
          <td>CSC Generation</td>
          <td>LinkedIn Job Alerts</td>
          <td>New alert today</td>
          <td>Review — note: Canada-based</td>
        </tr>
        <tr>
          <td><span class="badge yellow fit-med">MED</span></td>
          <td>Director of Human Resources (similar roles)</td>
          <td>Various</td>
          <td>LinkedIn Jobs</td>
          <td>Similar to SNP/NYC role</td>
          <td>Review &amp; filter for fit</td>
        </tr>
      </tbody>
    </table>

    <div class="sub-header">🟣 Networking Events — Calendar</div>
    <table>
      <thead>
        <tr><th>Date</th><th>Event</th><th>RSVP</th><th>Priority</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Wed Aug 12, 12–1:30 PM</td>
          <td>HR Networking &amp; Job Search Group — Zoom 2 (170+ attendees)</td>
          <td class="warn">⚠️ Pending</td>
          <td><span class="badge green">HIGH</span></td>
        </tr>
        <tr>
          <td>Thu Aug 13, 12–1:00 PM</td>
          <td>HR Networking Open Office Hours — Zoom 2</td>
          <td class="warn">⚠️ Pending</td>
          <td><span class="badge green">HIGH</span></td>
        </tr>
        <tr>
          <td>Thu Aug 13, 9–10:30 AM</td>
          <td>Executive Roundtable (John Madigan) — Zoom</td>
          <td style="color:#c0392b; font-weight:700;">❌ Declined</td>
          <td><span class="badge gray">LOW</span></td>
        </tr>
      </tbody>
    </table>

    <p class="note" style="margin-top:10px;">💡 Tip: The HR Networking Group has 170+ active members — strong pipeline for referrals and leads. Prioritize attendance on Wednesday.</p>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 6 — FULL EMAIL REVIEW BY CATEGORY
═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title dark">📂 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="sub-header" style="color:#c0392b;">🔴 Security / Risk (4 emails)</div>
    <div class="card red">
      <div class="card-title">Auto-Trashed — Advance-Fee / 419 Scam</div>
      <div class="card-meta">From: "Cheng Saephan" &lt;service_tw@whirlpool.com&gt; (spoofed) | Subject: "You have been Gifted 15 MILLION USD"</div>
      <p>Classic advance-fee fraud spoofing a Whirlpool service address. Auto-trashed. <strong>No action needed.</strong></p>
    </div>
    <div class="card red">
      <div class="card-title">Auto-Trashed — Credential Harvesting Phishing</div>
      <div class="card-meta">From: "melissaw212🔔" &lt;yzssupporttna@rfnpekdepfpxwyypnhcfsova.com&gt; | Subject: "We've blocked your account! Photos/videos will be deleted..."</div>
      <p>Spoofs Melissa's own username. Fake account-suspension threat demanding payment info. Auto-trashed. <strong>No action needed.</strong></p>
    </div>
    <div class="card yellow">
      <div class="card-title">⚠️ Verify — Amazon Returns Addressed to "Sophie"</div>
      <div class="card-meta">From: return@amazon.com | 2 emails | Items: UPNET Women's High Waisted &amp; Arach&amp;Cloz Women's</div>
      <p>Both returns confirmed for a "Sophie" — not Melissa. Possible unauthorized account use. <strong>Action: Log into Amazon and audit account immediately.</strong></p>
    </div>
    <div class="card red">
      <div class="card-title">Google Account Data Share — Neriva Service</div>
      <div class="card-meta">From: Google &lt;noreply-accounts@google.com&gt; | Date: Sun Aug 9</div>
      <p>Google notified that your account data was shared with "Neriva Service." If you did not authorize this, revoke access in Google Account → Security → Third-party apps. <strong>Review.</strong></p>
    </div>

    <hr class="divider">

    <!-- JOB SEARCH -->
    <div class="sub-header" style="color:#1b7a3e;">💼 Job Search (5 emails)</div>
    <div class="card green">
      <div class="card-title">Scovai: Chief People &amp; Culture Officer — Omnisage LLC (Strong Match)</div>
      <div class="card-meta">From: Scovai &lt;no-reply@scovai.com&gt; | Mon Aug 10, 9:04 AM | INBOX</div>
      <p>Strong match flagged by AI job matching platform. C-suite HR leadership role. <strong>Action: Review and apply this week.</strong></p>
    </div>
    <div class="card green">
      <div class="card-title">SourceHire: Sr. Director HR REQ93079 — Work Auth Request (×2)</div>
      <div class="card-meta">From: SourceHire Jobs &lt;jobs@sourcehire.app&gt; | 2 emails (5:49 AM &amp; 7:03 AM) | INBOX</div>
      <p>Duplicate emails requesting work authorization confirmation to keep application active. <strong>Action: Reply TODAY.</strong></p>
    </div>
    <div class="card green">
      <div class="card-title">LinkedIn: New Jobs Similar to Director of HR at SNP NYC</div>
      <div class="card-meta">From: LinkedIn &lt;jobs-noreply@linkedin.com&gt; | Mon Aug 10, 5:05 AM | INBOX</div>
      <p>Job alert with similar Director-level HR roles. <strong>Action: Review listing this week.</strong></p>
    </div>
    <div class="card green">
      <div class="card-title">LinkedIn Job Alert: Head of People Operations (Canada) — CSC Generation</div>
      <div class="card-meta">From: LinkedIn Job Alerts | Mon Aug 10, 3:05 AM | INBOX</div>
      <p>Head of People role at CSC Generation — Canada location may limit fit. <strong>Action: Review and determine eligibility.</strong></p>
    </div>
    <div class="card green">
      <div class="card-title">LinkedIn Job Alert: Head of People - U.S. at Elliptic</div>
      <div class="card-meta">From: LinkedIn Job Alerts | Mon Aug 10, 1:05 AM | Read</div>
      <p>U.S.-based Head of People role in crypto/blockchain sector. <strong>Action: Review if sector is of interest.</strong></p>
    </div>

    <hr class="divider">

    <!-- PERSONAL -->
    <div class="sub-header" style="color:#6a1b9a;">👤 Personal (5 emails)</div>
    <div class="card purple">
      <div class="card-title">Match.com: Kevin, David Timberland, Jay, Endri likes you; Phil viewed your profile</div>
      <div class="card-meta">From: Match &lt;mailer@connect.match.com&gt; | Multiple emails | Some in INBOX, some read</div>
      <p>Dating app notifications. Kevin, David Timberland, Jay, and Endri "liked" you. Phil (67, Union City NJ) viewed your profile. <strong>Action: Review at your discretion.</strong></p>
    </div>
    <div class="card purple">
      <div class="card-title">Match.com: John sent a message 💌</div>
      <div class="card-meta">From: Match | Sun Aug 9, 7:56 PM | Read</div>
      <p>New message from John on Match. <strong>Action: Read and reply if interested.</strong></p>
    </div>
    <div class="card purple">
      <div class="card-title">Carmel Car Service: July Points Statement (×2 duplicates)</div>
      <div class="card-meta">From: Carmel Points &lt;Points@carmelcarservice.com&gt; | Mon Aug 10, 6:05 AM | INBOX ×2</div>
      <p>Monthly loyalty points statement — sent twice (likely a system error). <strong>Action: Review points balance; delete one duplicate.</strong></p>
    </div>
    <div class="card purple">
      <div class="card-title">ChatGPT / OpenAI: Check your route before you go</div>
      <div class="card-meta">From: ChatGPT &lt;noreply@email.openai.com&gt; | Mon Aug 10, 4:08 AM | INBOX</div>
      <p>OpenAI travel prep tip email — possibly related to tomorrow's MRI appointment. <strong>Action: Review for travel planning if relevant.</strong></p>
    </div>
    <div class="card purple">
      <div class="card-title">Notify NYC: Missing Child Alert — Tarunvir Garcha (NYC)</div>
      <div class="card-meta">From: Notify NYC / Everbridge | Mon Aug 10, 8:53 AM | INBOX</div>
      <p>Official NYC missing child alert — 18-year-old Asian male, Jericho NY. FYI/public safety. No action required from Melissa unless she has relevant information.</p>
    </div>

    <hr class="divider">

    <!-- MEDICAL / HEALTH -->
    <div class="sub-header" style="color:#1565c0;">🏥 Medical / Health (1 email)</div>
    <div class="card blue">
      <div class="card-title">MRI Appointment — Calendar Entry (Aug 11)</div>
      <div class="card-meta">No email, but calendar event confirmed | 159 E 53rd St, 6th Floor | 646-754-2800</div>
      <p>See Calendar section for full prep details. Arrive 8:50 AM. IV contrast. No metal/piercings. Leave valuables at home.</p>
    </div>
    <p class="note">Note: Calendar event accounts for medical entry. No standalone health email (the Stephanie Infusion is a calendar entry, not an email).</p>

    <hr class="divider">

    <!-- NEWSLETTERS -->
    <div class="sub-header" style="color:#6a1b9a;">📰 Newsletters &amp; Subscriptions (4 emails)</div>
    <div class="card purple">
      <div class="card-title">Alison Courses — "One new skill can make a big difference" | Auto-Trashed (Newsletter)</div>
      <div class="card-meta">From: Alison Courses | Mon Aug 10, 12:36 AM | newsletter_trashed: true</div>
      <p>Professional development course newsletter. Auto-trashed. <strong>Recommendation: Unsubscribe or review for relevant HR courses.</strong></p>
    </div>
    <div class="card purple">
      <div class="card-title">Nextdoor Local News — "Bayonne Police Officer Joseph Giordano Dies Suddenly, 43" | Auto-Trashed (Newsletter)</div>
      <div class="card-meta">From: Nextdoor | Mon Aug 10, 12:35 AM | newsletter_trashed: true</div>
      <p>Local news digest. Auto-trashed. <strong>Recommendation: Adjust Nextdoor notification settings if unwanted.</strong></p>
    </div>
    <div class="card purple">
      <div class="card-title">1% Better Newsletter — "Misunderstood Barbarians, Vegetables Vanishing, F. Scott Fitzgerald"</div>
      <div class="card-meta">From: 1% Better &lt;hello@onepercentimprovements.convertkit.com&gt; | Mon Aug 10, 10:59 AM | In Trash</div>
      <p>Self-improvement newsletter. Already in trash. <strong>Recommendation: Unsubscribe if no longer relevant.</strong></p>
    </div>
    <div class="card purple">
      <div class="card-title">Dylan's Diary — "Why the Market Rallied On Bad News" (Bank of America note)</div>
      <div class="card-meta">From: Dylan's Diary &lt;newsletter@lg.behindthemarkets.com&gt; | Mon Aug 10, 6:24 AM | In Trash</div>
      <p>Market/finance newsletter. Already in trash. <strong>Recommendation: Unsubscribe if not actively reading.</strong></p>
    </div>

    <hr class="divider">

    <!-- PROMOTIONAL / RETAIL -->
    <div class="sub-header" style="color:#5a6475;">🛍 Promotional / Retail (9 emails)</div>
    <div class="card gray">
      <p>Gap Factory (×2), Old Navy (×1), Kohl's (×1), GapCash (×1), SHEIN (×1), Laura Geller Beauty (×1), The Daily Skimm (×1, promo), Gemma Bonham-Carter / software tip (×1). All in Trash or low priority. See Promotional/Retail Summary section for details.</p>
    </div>

    <hr class="divider">

    <!-- SAFE TO DELETE / IGNORE -->
    <div class="sub-header" style="color:#9aa3b2;">🗑 Safe to Delete / Ignore (17 emails)</div>
    <div class="card gray">
      <p>Includes: spam/adult content (4 not yet trashed), casino spam (1 not yet trashed), GLP-1 diet spam (2), fake CashApp (1), OkCupid (trashed), Jdate (trashed), Chick-fil-A reward (trashed), Otter.ai digest (trashed), OpenArt 24h deadline (trashed), Amazon review request (read/not actioned), Match.com Donald (read). All are low-priority, no action required. Recommend batch-deleting and unsubscribing where possible.</p>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 7 — TRASH REVIEW
═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title orange">🗑 Trash Review</div>
  <div class="section-body">

    <div class="sub-header" style="color:#1b7a3e;">✅ Restore Immediately</div>
    <p style="color:#6b7280; font-style:italic; font-size:12px; margin-bottom:8px;">No emails from Trash appear to require restoration. All trashed emails are either spam, promotions, newsletters, or phishing.</p>

    <div class="sub-header" style="color:#d4a017;">⚠️ Review Before Deleting</div>
    <table>
      <thead>
        <tr><th>Sender</th><th>Subject</th><th>Reason to Review</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>1% Better Newsletter</td>
          <td>Misunderstood Barbarians, Vegetables Vanishing...</td>
          <td>Subscribed newsletter — consider keeping if valuable; unsubscribe otherwise</td>
        </tr>
        <tr>
          <td>Dylan's Diary</td>
          <td>Why the Market Rallied On Bad News</td>
          <td>Finance newsletter — may have relevant market insights; unsubscribe if not reading</td>
        </tr>
        <tr>
          <td>Otter.ai Insights</td>
          <td>Your upcoming meetings</td>
          <td>Otter.ai meeting digest — note host asked to disable AI notetaking on Thu call</td>
        </tr>
      </tbody>
    </table>

    <div class="sub-header" style="color:#c0392b;">🗑 Auto-Trashed — Phishing / Scam (2 emails)</div>
    <table>
      <thead>
        <tr><th>Sender</th><th>Subject</th><th>Auto-Trash Reason</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>"Cheng Saephan" (spoofed Whirlpool)</td>
          <td>You have been Gifted 15 MILLION USD</td>
          <td>Classic advance-fee/419 scam spoofing a Whirlpool service address. No action needed.</td>
        </tr>
        <tr>
          <td>"melissaw212🔔" (random domain)</td>
          <td>We've blocked your account! Photos/videos will be deleted...</td>
          <td>Credential-harvesting phishing spoofing recipient's own username with fake account suspension threat. No action needed.</td>
        </tr>
      </tbody>
    </table>

    <div class="sub-header" style="color:#6b7280;">🗂 Auto-Trashed — Newsletters (2 emails)</div>
    <table>
      <thead>
        <tr><th>Sender</th><th>Subject</th><th>Note</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Alison Courses</td>
          <td>Melissa A, one new skill can make a big difference 💡</td>
          <td>Auto-Trashed — Newsletter. No action needed.</td>
        </tr>
        <tr>
          <td>Nextdoor Local News</td>
          <td>Bayonne Police Officer Joseph Giordano Dies Suddenly, 43</td>
          <td>Auto-Trashed — Newsletter. No action needed.</td>
        </tr>
      </tbody>
    </table>

    <div class="sub-header" style="color:#9aa3b2;">✅ Safe to Delete</div>
    <table>
      <thead>
        <tr><th>Sender</th><th>Subject / Theme</th><th>Reason</th></tr>
      </thead>
      <tbody>
        <tr><td>Gap Factory (×2)</td><td>Essentials jeans / 50% off sitewide</td><td>Retail promo — delete</td></tr>
        <tr><td>Old Navy</td><td>Forgot to check out?</td><td>Abandoned cart promo — delete</td></tr>
        <tr><td>Kohl's</td><td>Take 30% off | Fall home finds</td><td>Retail promo — delete</td></tr>
        <tr><td>GapCash</td><td>You earned GapCash</td><td>Loyalty promo — delete if not using</td></tr>
        <tr><td>SHEIN</td><td>NEW IN: Just Added 3 Days Ago</td><td>Retail promo — delete</td></tr>
        <tr><td>Laura Geller Beauty</td><td>Early Bird Sale Ends Soon ⏳ 45% OFF</td><td>Beauty promo — delete</td></tr>
        <tr><td>The Daily Skimm</td><td>Finally, a chance to do the worm</td><td>News/lifestyle digest — delete or unsubscribe</td></tr>
        <tr><td>Chick-fil-A</td><td>A little thing… from us to you (402 pts)</td><td>Loyalty reward — review if you want to use points; delete otherwise</td></tr>
        <tr><td>OpenArt</td><td>🚨 24h left! Save your OpenArt assets</td><td>Marketing urgency email — delete unless you use OpenArt</td></tr>
        <tr><td>Gemma Bonham-Carter</td><td>the software bill I don't have</td><td>Newsletter/marketing — delete</td></tr>
        <tr><td>OkCupid</td><td>Someone likes you</td><td>Dating app — delete or unsubscribe</td></tr>
        <tr><td>Jdate</td><td>You've Caught Someone's Eye 👀</td><td>Dating app — delete or unsubscribe</td></tr>
      </tbody>
    </table>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 8 — PROMOTIONAL / RETAIL SUMMARY
═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title gray">🛍 Promotional / Retail Summary</div>
  <div class="section-body">
    <table>
      <thead>
        <tr><th>Sender / Brand</th><th>Count</th><th>Subject / Theme</th><th>Recommendation</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Gap Factory</td>
          <td>2</td>
          <td>Essentials jeans in three fits; 50% off sitewide sale</td>
          <td><span class="badge gray">Delete / Unsubscribe</span></td>
        </tr>
        <tr>
          <td>Old Navy</td>
          <td>1</td>
          <td>Abandoned cart reminder — your cart is still ready</td>
          <td><span class="badge gray">Delete</span></td>
        </tr>
        <tr>
          <td>Kohl's</td>
          <td>1</td>
          <td>30% off fall home finds + Kohl's Cash</td>
          <td><span class="badge gray">Delete / Unsubscribe</span></td>
        </tr>
        <tr>
          <td>GapCash</td>
          <td>1</td>
          <td>GapCash earned — see inside for code</td>
          <td><span class="badge yellow">Review</span> — check expiry date on GapCash code</td>
        </tr>
        <tr>
          <td>SHEIN</td>
          <td>1</td>
          <td>New arrivals added 3 days ago</td>
          <td><span class="
