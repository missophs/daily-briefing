<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Melissa's Executive Briefing – Wednesday, June 3, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: white; border-radius: 16px; padding: 36px 40px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .date { font-size: 16px; color: #a8b8d8; margin-top: 6px; }
  .header .meta { display: flex; gap: 32px; margin-top: 20px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.1); border-radius: 10px; padding: 10px 20px; text-align: center; }
  .header .meta-item .num { font-size: 26px; font-weight: 700; color: #7ecfff; }
  .header .meta-item .label { font-size: 11px; color: #a8b8d8; text-transform: uppercase; letter-spacing: 1px; margin-top: 2px; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 18px; font-weight: 700; color: #1a1a2e; border-left: 5px solid #0f3460; padding-left: 12px; margin-bottom: 16px; text-transform: uppercase; letter-spacing: 0.5px; }

  /* CARDS */
  .card { border-radius: 12px; padding: 16px 20px; margin-bottom: 12px; border-left: 5px solid; }
  .card-red { background: #fff5f5; border-color: #e53e3e; }
  .card-yellow { background: #fffbf0; border-color: #d69e2e; }
  .card-blue { background: #ebf8ff; border-color: #3182ce; }
  .card-green { background: #f0fff4; border-color: #38a169; }
  .card-purple { background: #faf5ff; border-color: #805ad5; }
  .card-gray { background: #f7f8fa; border-color: #a0aec0; }

  .card-title { font-weight: 700; font-size: 15px; margin-bottom: 4px; }
  .card-red .card-title { color: #c53030; }
  .card-yellow .card-title { color: #975a16; }
  .card-blue .card-title { color: #2b6cb0; }
  .card-green .card-title { color: #276749; }
  .card-purple .card-title { color: #553c9a; }
  .card-gray .card-title { color: #4a5568; }

  .card-meta { font-size: 12px; color: #718096; margin-bottom: 6px; }
  .card-body { font-size: 13px; color: #2d3748; line-height: 1.6; }
  .card-row { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 6px; }
  .badge { display: inline-block; font-size: 11px; font-weight: 600; padding: 2px 10px; border-radius: 20px; }
  .badge-red { background: #fed7d7; color: #c53030; }
  .badge-yellow { background: #fefcbf; color: #975a16; }
  .badge-blue { background: #bee3f8; color: #2b6cb0; }
  .badge-green { background: #c6f6d5; color: #276749; }
  .badge-purple { background: #e9d8fd; color: #553c9a; }
  .badge-gray { background: #e2e8f0; color: #4a5568; }
  .badge-orange { background: #feebc8; color: #c05621; }

  /* EXEC SUMMARY */
  .exec-summary { background: linear-gradient(135deg, #1a1a2e, #0f3460); border-radius: 14px; padding: 24px 28px; margin-bottom: 24px; color: white; }
  .exec-summary h2 { font-size: 16px; text-transform: uppercase; letter-spacing: 1px; color: #7ecfff; margin-bottom: 16px; }
  .exec-bullet { display: flex; align-items: flex-start; gap: 14px; margin-bottom: 14px; padding: 12px 16px; background: rgba(255,255,255,0.08); border-radius: 10px; }
  .exec-bullet .icon { font-size: 22px; flex-shrink: 0; margin-top: 2px; }
  .exec-bullet .text strong { display: block; font-size: 14px; margin-bottom: 3px; }
  .exec-bullet .text span { font-size: 13px; color: #a8b8d8; }

  /* TABLE */
  table { width: 100%; border-collapse: collapse; margin-top: 8px; }
  th { background: #1a1a2e; color: white; padding: 10px 14px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
  td { padding: 10px 14px; border-bottom: 1px solid #e2e8f0; font-size: 13px; vertical-align: top; }
  tr:nth-child(even) td { background: #f7f8fa; }
  tr:hover td { background: #edf2f7; }
  .tbl-wrap { border-radius: 10px; overflow: hidden; box-shadow: 0 1px 6px rgba(0,0,0,0.07); margin-bottom: 16px; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { background: #0f3460; color: white; padding: 8px 16px; border-radius: 8px 8px 0 0; font-weight: 700; font-size: 14px; }
  .cal-event { background: white; border-left: 4px solid #3182ce; padding: 12px 16px; border-bottom: 1px solid #e2e8f0; }
  .cal-event:last-child { border-bottom: none; border-radius: 0 0 8px 8px; }
  .cal-event-title { font-weight: 700; color: #2b6cb0; font-size: 14px; }
  .cal-event-time { font-size: 12px; color: #718096; margin-top: 2px; }
  .cal-event-body { font-size: 13px; color: #4a5568; margin-top: 6px; line-height: 1.6; }
  .cal-conflict { background: #fff5f5; border-left-color: #e53e3e; }
  .cal-event-declined { background: #f7f8fa; border-left-color: #a0aec0; }
  .cal-event-needs { background: #fffbf0; border-left-color: #d69e2e; }

  /* DASHBOARD */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-card { background: white; border-radius: 12px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); border-top: 4px solid; }
  .dash-card .dash-num { font-size: 32px; font-weight: 800; margin-bottom: 4px; }
  .dash-card .dash-label { font-size: 12px; color: #718096; text-transform: uppercase; letter-spacing: 0.8px; }
  .dash-card .dash-detail { font-size: 12px; color: #4a5568; margin-top: 8px; line-height: 1.5; }
  .dash-red { border-color: #e53e3e; } .dash-red .dash-num { color: #e53e3e; }
  .dash-yellow { border-color: #d69e2e; } .dash-yellow .dash-num { color: #d69e2e; }
  .dash-blue { border-color: #3182ce; } .dash-blue .dash-num { color: #3182ce; }
  .dash-green { border-color: #38a169; } .dash-green .dash-num { color: #38a169; }
  .dash-purple { border-color: #805ad5; } .dash-purple .dash-num { color: #805ad5; }
  .dash-gray { border-color: #a0aec0; } .dash-gray .dash-num { color: #a0aec0; }

  /* PRIORITIES */
  .priority-box { background: linear-gradient(135deg, #1a1a2e, #0f3460); color: white; border-radius: 14px; padding: 28px 32px; }
  .priority-box h2 { font-size: 16px; text-transform: uppercase; letter-spacing: 1px; color: #7ecfff; margin-bottom: 18px; }
  .priority-item { display: flex; gap: 16px; align-items: flex-start; margin-bottom: 16px; }
  .priority-num { background: #7ecfff; color: #1a1a2e; font-weight: 800; font-size: 18px; width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
  .priority-text strong { display: block; font-size: 15px; margin-bottom: 3px; }
  .priority-text span { font-size: 13px; color: #a8b8d8; }

  /* MISC */
  .divider { height: 1px; background: #e2e8f0; margin: 20px 0; }
  .sub-header { font-size: 14px; font-weight: 700; color: #2d3748; margin: 14px 0 8px 0; padding-bottom: 4px; border-bottom: 2px solid #e2e8f0; }
  .alert-box { background: #fff5f5; border: 1.5px solid #fc8181; border-radius: 10px; padding: 14px 18px; margin-bottom: 12px; }
  .alert-box-title { font-weight: 700; color: #c53030; font-size: 14px; margin-bottom: 4px; }
  .note { font-size: 12px; color: #718096; font-style: italic; }
  a { color: #3182ce; text-decoration: none; }
  a:hover { text-decoration: underline; }
  .total-row td { font-weight: 700; background: #1a1a2e !important; color: white; }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════
     SECTION 1: HEADER
═══════════════════════════════════════════════ -->
<div class="header">
  <h1>☀️ Good Morning, Melissa</h1>
  <div class="date">Wednesday, June 3, 2026 &nbsp;·&nbsp; Executive Chief of Staff Briefing</div>
  <div class="meta">
    <div class="meta-item"><div class="num">50</div><div class="label">Emails Reviewed</div></div>
    <div class="meta-item"><div class="num">10</div><div class="label">Calendar Events</div></div>
    <div class="meta-item"><div class="num">3</div><div class="label">🔴 Security Flags</div></div>
    <div class="meta-item"><div class="num">5</div><div class="label">🟡 Action Items</div></div>
    <div class="meta-item"><div class="num">4</div><div class="label">📅 Meetings This Week</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 2: EXECUTIVE SUMMARY
═══════════════════════════════════════════════ -->
<div class="exec-summary">
  <h2>⚡ Executive Summary</h2>
  <div class="exec-bullet">
    <div class="icon">🔴</div>
    <div class="text">
      <strong>BIGGEST RISK: Multiple Phishing / Scam Emails in Your Inbox — Immediate Awareness Required</strong>
      <span>At least 3 highly suspicious emails are sitting outside Trash and in active inbox: a fake "Cloud Account Locked" threat, a Casino Yabby fake payment notice, and a fake free spins offer. Your LinkedIn password was also reset today — verify account security immediately.</span>
    </div>
  </div>
  <div class="exec-bullet">
    <div class="icon">🟢</div>
    <div class="text">
      <strong>BIGGEST OPPORTUNITY: Kentik Application Rejected — Pivot to Open LinkedIn Leads & Netta Jenkins Consult</strong>
      <span>Your Sr. People Business Partner application to Kentik was declined. However, a 15-min consult with Netta Jenkins (HIC Consulting) is confirmed for June 9, and a Senior Director HRBP (AI-Native) role at RemoteHunter was flagged via LinkedIn Job Alerts. Review and apply.</span>
    </div>
  </div>
  <div class="exec-bullet">
    <div class="icon">🔵</div>
    <div class="text">
      <strong>BIGGEST CALENDAR ITEM: Tomorrow — Dr. Husk Appointment + HR Networking Open Office Hours RSVP Pending</strong>
      <span>You have Dr. Husk confirmed at 10:30 AM tomorrow (June 4). The HR Networking Open Office Hours at noon on June 4 still shows "Needs Action" — decide now whether to attend. State Farm bill due June 7 and Eye appointment on June 8 also require attention this week.</span>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 3: ACTION REQUIRED
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">🚨 Action Required</div>

  <div class="card card-red">
    <div class="card-meta">SECURITY &nbsp;·&nbsp; LinkedIn &lt;security-noreply@linkedin.com&gt;</div>
    <div class="card-title">⚠️ LinkedIn Password Reset Confirmed + PIN Exposed in Email</div>
    <div class="card-body">
      Your LinkedIn password was successfully reset today at 9:17 PM UTC. A PIN (606210) was also sent via email and is now visible in this briefing data — this PIN should be considered compromised.<br><br>
      <strong>Why it matters:</strong> If you did not initiate this reset, your account may be compromised. Even if you did, the PIN being logged in email is a security exposure.<br>
      <strong>Recommended next step:</strong> Log into LinkedIn immediately, verify account activity, enable two-factor authentication, and change your password again to a new, unique value. Do not use PIN 606210 for anything.
    </div>
    <div class="card-row"><span class="badge badge-red">🔴 URGENT</span><span class="badge badge-red">Do Today</span></div>
  </div>

  <div class="card card-red">
    <div class="card-meta">PHISHING / SCAM &nbsp;·&nbsp; "Payment_Declined" &lt;xbtcsupportmd@wcknlkzajfzzlhmducymgdwi.com&gt;</div>
    <div class="card-title">🚨 Fake "Cloud Account Locked" Threat — Phishing Email NOT in Trash</div>
    <div class="card-body">
      An email claiming your cloud subscription expired and your "photos and videos will be removed" is sitting in your inbox (not trash). Sender domain is clearly fraudulent.<br><br>
      <strong>Why it matters:</strong> This is a classic scare-tactic phishing attempt. Clicking any link could compromise your device or credentials.<br>
      <strong>Recommended next step:</strong> Do NOT click any links. Mark as spam and delete immediately. Report to Google as phishing.
    </div>
    <div class="card-row"><span class="badge badge-red">🔴 PHISHING</span><span class="badge badge-red">Delete Immediately</span></div>
  </div>

  <div class="card card-red">
    <div class="card-meta">SCAM &nbsp;·&nbsp; Casino_Yabby &lt;tfvrniyohli@fknm.iwebcsruiikul.us&gt; + Free Spins &lt;gudvuwhjjks@lmsw.wucbgfmxbenbv.us&gt;</div>
    <div class="card-title">🚨 Two Casino Scam Emails Active in Inbox (Not Trash)</div>
    <div class="card-body">
      Two fraudulent gambling emails claim you have "$13,963.99 ready" and "130 Free Spins" waiting. Both use spoofed suspicious domains.<br><br>
      <strong>Why it matters:</strong> These are credential-harvesting or malware-delivery scams. Neither payment is real.<br>
      <strong>Recommended next step:</strong> Do NOT click. Mark as spam, delete, and report to Google as phishing.
    </div>
    <div class="card-row"><span class="badge badge-red">🔴 SCAM</span><span class="badge badge-red">Delete Immediately</span></div>
  </div>

  <div class="card card-yellow">
    <div class="card-meta">CALENDAR / RSVP &nbsp;·&nbsp; Google Calendar</div>
    <div class="card-title">📅 RSVP Pending: HR Networking Open Office Hours — Tomorrow June 4, 12:00 PM</div>
    <div class="card-body">
      Status shows "Needs Action." This is a large group networking call (180+ attendees) relevant to your active job search.<br><br>
      <strong>Why it matters:</strong> Given your active job search, this is a high-value networking opportunity.<br>
      <strong>Recommended next step:</strong> Accept or decline before tomorrow morning. Note: you also have Dr. Husk at 10:30–11:30 AM, so the noon slot is open.
    </div>
    <div class="card-row"><span class="badge badge-yellow">🟡 RSVP Today</span><span class="badge badge-blue">June 4 @ 12:00 PM</span></div>
  </div>

  <div class="card card-yellow">
    <div class="card-meta">BILLING &nbsp;·&nbsp; Google Calendar Reminder</div>
    <div class="card-title">💰 State Farm Bill Due — June 7</div>
    <div class="card-body">
      You have a calendar reminder for your State Farm insurance bill due this Saturday, June 7.<br><br>
      <strong>Why it matters:</strong> Missing an insurance payment can cause a lapse in coverage.<br>
      <strong>Recommended next step:</strong> Pay or schedule payment before June 7.
    </div>
    <div class="card-row"><span class="badge badge-yellow">🟡 DUE June 7</span></div>
  </div>

  <div class="card card-yellow">
    <div class="card-meta">INFRASTRUCTURE &nbsp;·&nbsp; Netlify &lt;team@netlify.com&gt;</div>
    <div class="card-title">⚠️ Netlify Credits at 75% — Morning Briefing Project</div>
    <div class="card-body">
      Your "morning briefing" Netlify team has used 750 of 1,000 credits this billing cycle.<br><br>
      <strong>Why it matters:</strong> If credits are exhausted, your automated briefing pipeline will break mid-cycle.<br>
      <strong>Recommended next step:</strong> Review usage, consider upgrading plan or optimizing build frequency before hitting the limit.
    </div>
    <div class="card-row"><span class="badge badge-yellow">🟡 Monitor</span><span class="badge badge-orange">75% Used</span></div>
  </div>

  <div class="card card-yellow">
    <div class="card-meta">TECHNICAL &nbsp;·&nbsp; GitHub &lt;notifications@github.com&gt; (in Trash)</div>
    <div class="card-title">⚙️ Daily Briefing GitHub Workflow — 2 Failed Runs Today</div>
    <div class="card-body">
      Two workflow runs for your <strong>missophs/daily-briefing</strong> repository failed today (commits 7812f1d and b04c8a4). All jobs failed.<br><br>
      <strong>Why it matters:</strong> Your automated daily briefing pipeline is broken. This is consistent with the multiple partial briefing drafts sent to yourself today via Gmail.<br>
      <strong>Recommended next step:</strong> Review GitHub Actions logs, debug the webhook trigger, and confirm the pipeline is stable.
    </div>
    <div class="card-row"><span class="badge badge-yellow">🟡 Fix Soon</span></div>
  </div>

  <div class="card card-green">
    <div class="card-meta">JOB SEARCH &nbsp;·&nbsp; Kentik &lt;no-reply@kentik.com&gt; (in Trash)</div>
    <div class="card-title">📋 Kentik Application Rejected — Sr. People Business Partner</div>
    <div class="card-body">
      You received a rejection from Kentik for the Sr. People Business Partner role.<br><br>
      <strong>Why it matters:</strong> Signals the need to redirect energy to active pipeline opportunities.<br>
      <strong>Recommended next step:</strong> Note in your job tracker. Pivot focus to the RemoteHunter HRBP (AI-Native) role and the Netta Jenkins consult on June 9.
    </div>
    <div class="card-row"><span class="badge badge-gray">Closed</span><span class="badge badge-green">Pivot Required</span></div>
  </div>

  <div class="card card-yellow">
    <div class="card-meta">PROFESSIONAL &nbsp;·&nbsp; HR.com &lt;info@events.hr.com&gt;</div>
    <div class="card-title">📚 HR.com Webcast: End of Bundled Maternity Care — June 24, 2026 (Free)</div>
    <div class="card-body">
      A free webcast on changes to maternity care billing relevant to 2027 benefits planning is available June 24.<br><br>
      <strong>Why it matters:</strong> Highly relevant to your HR/People leadership background and demonstrates current expertise.<br>
      <strong>Recommended next step:</strong> Register if interested in keeping benefits knowledge current.
    </div>
    <div class="card-row"><span class="badge badge-yellow">🟡 Optional Register</span><span class="badge badge-blue">June 24</span></div>
  </div>

  <div class="card card-yellow">
    <div class="card-meta">CALENDAR / RSVP &nbsp;·&nbsp; Google Calendar</div>
    <div class="card-title">📅 RSVP Pending: Melissa x Meg Drinks — June 10, 1:00 PM</div>
    <div class="card-body">
      A meeting with Meg (Oak Leaf Partnership) on June 10 at 1:00 PM is marked "Needs Action." Location is TBC.<br><br>
      <strong>Why it matters:</strong> This overlaps with the HR Networking Group session (12:00–1:30 PM) on the same day — potential conflict.<br>
      <strong>Recommended next step:</strong> Confirm with Meg, set a location, and resolve the time overlap with the networking session.
    </div>
    <div class="card-row"><span class="badge badge-yellow">🟡 RSVP + Conflict</span><span class="badge badge-red">Overlap June 10</span></div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════
     SECTION 4: FULL 7-DAY CALENDAR
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📅 Full 7-Day Calendar</div>
  <p class="note" style="margin-bottom:14px;">Showing all 10 events from June 3–10, 2026. Today is Wednesday, June 3 — no events scheduled today.</p>

  <!-- JUNE 3 -->
  <div class="cal-day">
    <div class="cal-day-header">Wednesday, June 3, 2026 — TODAY</div>
    <div class="cal-event" style="background:#f7f8fa;">
      <div class="cal-event-title">No events scheduled today</div>
      <div class="cal-event-body">Use today to address security alerts, catch up on email, and RSVP for tomorrow's events.</div>
    </div>
  </div>

  <!-- JUNE 4 -->
  <div class="cal-day">
    <div class="cal-day-header">Thursday, June 4, 2026 — TOMORROW</div>

    <div class="cal-event cal-event-declined">
      <div class="cal-event-title">Executive Roundtable</div>
      <div class="cal-event-time">⏰ 9:00 AM – 10:30 AM EST</div>
      <div class="cal-event-body">
        <span class="badge badge-gray">DECLINED</span> &nbsp;Hosted by John Madigan via Zoom.<br>
        <strong>Location:</strong> <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09">Zoom Link</a> | Meeting ID: 207 786 667 | PW: 205454<br>
        <strong>Prep:</strong> None needed — you have declined.<br>
        <strong>Note:</strong> Consider whether reconnecting with John Madigan is beneficial for your network.
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-event-title">Dr. Husk</div>
      <div class="cal-event-time">⏰ 10:30 AM – 11:30 AM EST</div>
      <div class="cal-event-body">
        <span class="badge badge-green">CONFIRMED</span> &nbsp;Medical appointment.<br>
        <strong>Location:</strong> Not specified<br>
        <strong>Prep:</strong> Confirm address/telehealth link. Prepare questions. Allow buffer before noon if attending HR networking.
      </div>
    </div>

    <div class="cal-event cal-event-needs">
      <div class="cal-event-title">HR Networking & Job Search: Open Office Hours – Zoom 2</div>
      <div class="cal-event-time">⏰ 12:00 PM – 1:00 PM EST</div>
      <div class="cal-event-body">
        <span class="badge badge-yellow">⚠️ NEEDS ACTION — RSVP PENDING</span><br>
        <strong>Location:</strong> <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1">Zoom Link</a><br>
        <strong>Attendees:</strong> Large group (~180 HR professionals in active job search)<br>
        <strong>Prep:</strong> Prepare a 30-second intro. Bring your job target summary. Note: no AI notetaking tools per host instructions.<br>
        <strong>Action:</strong> Accept or decline today. Schedule allows attendance after Dr. Husk (10:30–11:30 AM).
      </div>
    </div>
  </div>

  <!-- JUNE 5 -->
  <div class="cal-day">
    <div class="cal-day-header">Friday, June 5, 2026</div>
    <div class="cal-event" style="background:#f7f8fa;">
      <div class="cal-event-title">No events scheduled</div>
      <div class="cal-event-body">Good opportunity to follow up on job applications or prepare for the weekend events.</div>
    </div>
  </div>

  <!-- JUNE 6 -->
  <div class="cal-day">
    <div class="cal-day-header">Saturday, June 6, 2026</div>
    <div class="cal-event">
      <div class="cal-event-title">🎂 Jackie's Birthday (All Day)</div>
      <div class="cal-event-time">⏰ All Day (June 6)</div>
      <div class="cal-event-body">
        <span class="badge badge-green">CONFIRMED</span><br>
        <strong>Prep:</strong> Send a birthday message or gift if not already done. Father's Day is June 21 — Amazon Father's Day gift browsing may be relevant if needed.
      </div>
    </div>
  </div>

  <!-- JUNE 7 -->
  <div class="cal-day">
    <div class="cal-day-header">Sunday, June 7, 2026</div>
    <div class="cal-event cal-event-needs">
      <div class="cal-event-title">💰 State Farm Bill (All Day Reminder)</div>
      <div class="cal-event-time">⏰ All Day (due by end of day June 7)</div>
      <div class="cal-event-body">
        <span class="badge badge-green">CONFIRMED</span><br>
        <strong>Why it matters:</strong> Insurance payment — lapse could affect coverage.<br>
        <strong>Action:</strong> Pay or schedule payment before this date.
      </div>
    </div>
  </div>

  <!-- JUNE 8 -->
  <div class="cal-day">
    <div class="cal-day-header">Monday, June 8, 2026</div>
    <div class="cal-event">
      <div class="cal-event-title">👁️ Eye Appointment</div>
      <div class="cal-event-time">
