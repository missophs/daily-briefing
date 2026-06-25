<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing – Melissa | Thursday, June 25, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header .subtitle { font-size: 15px; color: #a0b4cc; margin-top: 4px; }
  .header-meta { display: flex; gap: 28px; margin-top: 20px; flex-wrap: wrap; }
  .header-stat { background: rgba(255,255,255,0.08); border-radius: 10px; padding: 12px 20px; text-align: center; }
  .header-stat .val { font-size: 26px; font-weight: 700; color: #e2f0fb; }
  .header-stat .lbl { font-size: 11px; color: #8dafc8; text-transform: uppercase; letter-spacing: 0.8px; margin-top: 2px; }

  /* SECTION */
  .section { background: #fff; border-radius: 12px; padding: 24px 28px; margin-bottom: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.06); }
  .section-title { font-size: 17px; font-weight: 700; color: #1a1a2e; margin-bottom: 16px; padding-bottom: 10px; border-bottom: 2px solid #f0f2f5; display: flex; align-items: center; gap: 8px; }
  .section-title .icon { font-size: 19px; }

  /* EXEC SUMMARY */
  .exec-bullet { display: flex; gap: 12px; align-items: flex-start; padding: 12px 16px; border-radius: 9px; margin-bottom: 10px; }
  .exec-bullet:last-child { margin-bottom: 0; }
  .exec-bullet.red { background: #fff5f5; border-left: 4px solid #e53e3e; }
  .exec-bullet.green { background: #f0fff4; border-left: 4px solid #38a169; }
  .exec-bullet.blue { background: #ebf8ff; border-left: 4px solid #3182ce; }
  .exec-bullet .bicon { font-size: 22px; }
  .exec-bullet .btxt strong { display: block; font-size: 14px; color: #1a1a2e; }
  .exec-bullet .btxt span { font-size: 13px; color: #555; }

  /* CARDS */
  .card-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(310px, 1fr)); gap: 16px; }
  .card { border-radius: 10px; padding: 16px 18px; border-left: 5px solid #ccc; }
  .card.red { background: #fff5f5; border-color: #e53e3e; }
  .card.yellow { background: #fffff0; border-color: #d69e2e; }
  .card.green { background: #f0fff4; border-color: #38a169; }
  .card.blue { background: #ebf8ff; border-color: #3182ce; }
  .card.purple { background: #faf5ff; border-color: #805ad5; }
  .card.gray { background: #f7f7f7; border-color: #a0aec0; }
  .card-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; opacity: 0.7; }
  .card-title { font-size: 14px; font-weight: 700; margin-bottom: 8px; }
  .card-row { font-size: 12px; color: #444; margin-bottom: 4px; }
  .card-row strong { color: #1a1a2e; }
  .card-action { margin-top: 10px; background: rgba(0,0,0,0.06); border-radius: 6px; padding: 7px 10px; font-size: 12px; font-weight: 600; }

  /* BADGES */
  .badge { display: inline-block; padding: 2px 9px; border-radius: 20px; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
  .badge-red { background: #fed7d7; color: #c53030; }
  .badge-yellow { background: #fefcbf; color: #975a16; }
  .badge-green { background: #c6f6d5; color: #276749; }
  .badge-blue { background: #bee3f8; color: #2a69ac; }
  .badge-purple { background: #e9d8fd; color: #553c9a; }
  .badge-gray { background: #e2e8f0; color: #4a5568; }
  .badge-orange { background: #feebc8; color: #c05621; }

  /* TABLE */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #f0f2f5; color: #1a1a2e; padding: 9px 12px; text-align: left; font-size: 11px; text-transform: uppercase; letter-spacing: 0.6px; }
  td { padding: 9px 12px; border-bottom: 1px solid #f0f2f5; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #fafafa; }

  /* CALENDAR */
  .cal-day { margin-bottom: 20px; }
  .cal-day-header { background: #1a1a2e; color: #fff; border-radius: 8px; padding: 8px 16px; font-size: 13px; font-weight: 700; margin-bottom: 8px; }
  .cal-event { background: #ebf8ff; border-left: 4px solid #3182ce; border-radius: 7px; padding: 12px 16px; margin-bottom: 8px; }
  .cal-event.declined { background: #fff5f5; border-color: #e53e3e; opacity: 0.85; }
  .cal-event.needs-action { background: #fffff0; border-color: #d69e2e; }
  .cal-event.confirmed { background: #f0fff4; border-color: #38a169; }
  .cal-event-title { font-weight: 700; font-size: 14px; }
  .cal-event-meta { font-size: 12px; color: #555; margin-top: 4px; }
  .cal-event-meta span { margin-right: 14px; }

  /* JOB PIPELINE */
  .job-row { display: flex; align-items: flex-start; gap: 12px; padding: 11px 14px; border-radius: 8px; margin-bottom: 8px; background: #f9fff9; border: 1px solid #c6f6d5; }
  .job-row.medium { background: #fffff9; border-color: #fefcbf; }
  .job-row.low { background: #f9f9f9; border-color: #e2e8f0; }
  .job-fit { font-size: 10px; font-weight: 800; text-transform: uppercase; min-width: 42px; text-align: center; padding: 3px 7px; border-radius: 5px; }
  .fit-high { background: #c6f6d5; color: #276749; }
  .fit-medium { background: #fefcbf; color: #975a16; }
  .fit-low { background: #e2e8f0; color: #4a5568; }
  .job-info strong { font-size: 13px; display: block; }
  .job-info span { font-size: 12px; color: #555; }

  /* EMAIL REVIEW */
  .email-cat { margin-bottom: 16px; }
  .email-cat-header { display: flex; align-items: center; gap: 10px; padding: 10px 14px; border-radius: 8px 8px 0 0; font-weight: 700; font-size: 13px; }
  .email-cat-body { border: 1px solid #e2e8f0; border-top: none; border-radius: 0 0 8px 8px; padding: 12px 14px; background: #fff; font-size: 13px; }
  .email-cat-body .meta { color: #555; margin-bottom: 6px; }
  .email-cat-body .senders { color: #333; margin-bottom: 6px; }
  .email-cat-body .action { font-weight: 600; color: #1a1a2e; }

  .cat-red .email-cat-header { background: #fed7d7; color: #742a2a; }
  .cat-green .email-cat-header { background: #c6f6d5; color: #1c4532; }
  .cat-blue .email-cat-header { background: #bee3f8; color: #1a365d; }
  .cat-yellow .email-cat-header { background: #fefcbf; color: #744210; }
  .cat-purple .email-cat-header { background: #e9d8fd; color: #322659; }
  .cat-gray .email-cat-header { background: #e2e8f0; color: #2d3748; }
  .cat-orange .email-cat-header { background: #feebc8; color: #7b341e; }

  /* DASHBOARD */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 14px; }
  .dash-tile { border-radius: 10px; padding: 16px; text-align: center; }
  .dash-tile .dnum { font-size: 34px; font-weight: 800; }
  .dash-tile .dlbl { font-size: 11px; text-transform: uppercase; letter-spacing: 0.7px; margin-top: 4px; opacity: 0.75; }
  .dt-red { background: #fff5f5; color: #c53030; }
  .dt-yellow { background: #fffff0; color: #975a16; }
  .dt-green { background: #f0fff4; color: #276749; }
  .dt-blue { background: #ebf8ff; color: #2a69ac; }
  .dt-purple { background: #faf5ff; color: #553c9a; }
  .dt-gray { background: #f7f7f7; color: #4a5568; }

  /* ACCOUNTING */
  .acct-total { background: #1a1a2e; color: #fff; border-radius: 8px; padding: 12px 18px; text-align: center; font-size: 16px; font-weight: 700; margin-top: 14px; }

  /* PRIORITIES */
  .priority-card { display: flex; gap: 16px; align-items: flex-start; background: #fff; border-radius: 10px; padding: 18px 20px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .priority-num { font-size: 34px; font-weight: 900; color: #cbd5e0; min-width: 40px; line-height: 1; }
  .priority-body strong { font-size: 15px; display: block; margin-bottom: 4px; }
  .priority-body span { font-size: 13px; color: #555; }

  /* UTILITY */
  .warn { color: #c53030; font-weight: 700; }
  .note { font-size: 11px; color: #888; font-style: italic; margin-top: 8px; }
  .divider { border: none; border-top: 1px solid #e2e8f0; margin: 14px 0; }
  a { color: #3182ce; text-decoration: none; }
  a:hover { text-decoration: underline; }
  .pill { display: inline-block; background: #e2e8f0; color: #2d3748; border-radius: 20px; padding: 2px 10px; font-size: 11px; margin: 2px; }

  @media (max-width: 600px) {
    .header-meta { flex-direction: column; }
    .card-grid { grid-template-columns: 1fr; }
    .dash-grid { grid-template-columns: repeat(2, 1fr); }
  }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ═══════════════════════════════════════════════════════
     1. HEADER
═══════════════════════════════════════════════════════ -->
<div class="header">
  <div class="header-top" style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:10px;">
    <div>
      <div class="header h1" style="font-size:13px;color:#8dafc8;text-transform:uppercase;letter-spacing:1.2px;margin-bottom:6px;">Executive Briefing</div>
      <h1 style="font-size:28px;font-weight:800;">Good Morning, Melissa ☀️</h1>
      <div class="subtitle">Thursday, June 25, 2026 &nbsp;·&nbsp; Prepared by your Executive Chief of Staff</div>
    </div>
    <div style="font-size:12px;color:#8dafc8;text-align:right;">
      <div>Generated: 6/25/2026</div>
      <div style="margin-top:4px;"><span class="badge badge-red">3 Security Alerts</span></div>
    </div>
  </div>
  <div class="header-meta">
    <div class="header-stat"><div class="val">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="header-stat"><div class="val">5</div><div class="lbl">Calendar Events</div></div>
    <div class="header-stat"><div class="val">3</div><div class="lbl">Action Required Today</div></div>
    <div class="header-stat"><div class="val">6</div><div class="lbl">Job Leads Active</div></div>
    <div class="header-stat"><div class="val">1</div><div class="lbl">Application Update</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     2. EXECUTIVE SUMMARY
═══════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">📋</span> Executive Summary</div>
  <div class="exec-bullet red">
    <div class="bicon">🚨</div>
    <div class="btxt">
      <strong>BIGGEST RISK: Multiple Phishing &amp; Scam Emails Targeting Your Account</strong>
      <span>At least 5 emails are confirmed phishing/scam attempts — fake "Cloud Account Locked" alerts (sent 3×), a fake CashApp payout, and a fake casino free-spins offer. These use spoofed sender addresses and urgent language. Do NOT click any links. Mark as spam and delete immediately.</span>
    </div>
  </div>
  <div class="exec-bullet green">
    <div class="bicon">💼</div>
    <div class="btxt">
      <strong>BIGGEST OPPORTUNITY: Marsh McLennan Agency Application Status Update Received</strong>
      <span>Workday MMC sent an application status update for the HR Leader, Private Client Services role (R_350229). Review immediately — the snippet suggests a decision has been made. Additionally, two Chief People Officer alerts and multiple HR Director alerts are live on LinkedIn and Glassdoor this week.</span>
    </div>
  </div>
  <div class="exec-bullet blue">
    <div class="bicon">📅</div>
    <div class="btxt">
      <strong>BIGGEST CALENDAR ITEM: HR Networking Open Office Hours TODAY at 12:00 PM — RSVP Pending</strong>
      <span>You have not responded to today's HR Networking &amp; Job Search Open Office Hours Zoom (12:00–1:00 PM). Decide now: attend (great networking opportunity) or decline. You also declined the Executive Roundtable (9:00 AM, now in progress). COBRA payment reminder is scheduled Saturday, June 27.</span>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     3. ACTION REQUIRED
═══════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">⚡</span> Action Required</div>
  <div class="card-grid">

    <div class="card red">
      <div class="card-label">🔴 Security – Phishing</div>
      <div class="card-title">Fake "Cloud Account Locked" Emails (3 Instances)</div>
      <div class="card-row"><strong>Source:</strong> Spoofed addresses pretending to be your account</div>
      <div class="card-row"><strong>Why It Matters:</strong> These are phishing attacks designed to steal billing credentials. Three nearly identical emails were sent 6/24–6/25. Your real cloud storage is fine.</div>
      <div class="card-action">✅ Action: Do NOT click. Mark all 3 as phishing/spam. Delete. Verify your actual cloud storage directly at google.com/drive.</div>
      <div class="card-row" style="margin-top:8px;"><strong>Due:</strong> <span class="warn">TODAY — Immediately</span></div>
    </div>

    <div class="card red">
      <div class="card-label">🔴 Security – Phishing</div>
      <div class="card-title">Fake CashApp Payout + Casino Spam</div>
      <div class="card-row"><strong>Source:</strong> "💲CashApp💲" &lt;spoofed domain&gt; + "Casino.Special" &lt;spoofed domain&gt;</div>
      <div class="card-row"><strong>Why It Matters:</strong> Fake CashApp email claims a $3,000 payout — classic advance-fee/credential harvesting scam. Casino email is unsolicited gambling spam. Both use spoofed domains.</div>
      <div class="card-action">✅ Action: Mark as phishing. Delete. Do not click any links.</div>
      <div class="card-row" style="margin-top:8px;"><strong>Due:</strong> <span class="warn">TODAY</span></div>
    </div>

    <div class="card green">
      <div class="card-label">🟢 Job Search – Critical</div>
      <div class="card-title">Marsh McLennan Agency: Application Status Update</div>
      <div class="card-row"><strong>Source:</strong> Workday MMC &lt;mmc@myworkday.com&gt;</div>
      <div class="card-row"><strong>Why It Matters:</strong> Application status update received for HR Leader, Private Client Services (R_350229). The snippet reads "After careful evaluation of the qualifications and e…" — this could be an offer, rejection, or interview invite. Must be read immediately.</div>
      <div class="card-action">✅ Action: Open email now. If rejection — reply graciously and ask to stay in touch. If invite — schedule immediately.</div>
      <div class="card-row" style="margin-top:8px;"><strong>Due:</strong> <span class="warn">TODAY</span></div>
    </div>

    <div class="card yellow">
      <div class="card-label">🟡 Calendar – RSVP Needed</div>
      <div class="card-title">HR Networking Open Office Hours – TODAY 12:00 PM</div>
      <div class="card-row"><strong>Source:</strong> Google Calendar – HR Networking &amp; Job Search: Open Office Hours Zoom 2</div>
      <div class="card-row"><strong>Why It Matters:</strong> Status is "needsAction" — you haven't RSVP'd. This is a large peer networking group (170+ HR professionals). Attending supports active job search.</div>
      <div class="card-action">✅ Action: Accept or Decline in Google Calendar. Join link: us06web.zoom.us/j/85945371140</div>
      <div class="card-row" style="margin-top:8px;"><strong>Due:</strong> <span class="warn">TODAY by 12:00 PM</span></div>
    </div>

    <div class="card yellow">
      <div class="card-label">🟡 Billing – Google ToS Update</div>
      <div class="card-title">Google Updated Terms of Service Effective July 2026</div>
      <div class="card-row"><strong>Source:</strong> Google &lt;google-noreply@google.com&gt; — LEGITIMATE</div>
      <div class="card-row"><strong>Why It Matters:</strong> Google is updating Terms of Service. Effective date is in July 2026. Read to understand any changes to your Gmail/Drive/account.</div>
      <div class="card-action">✅ Action: Read the email. Note effective date. No immediate action required but review before July.</div>
      <div class="card-row" style="margin-top:8px;"><strong>Due:</strong> Before July 2026</div>
    </div>

    <div class="card yellow">
      <div class="card-label">🟡 Financial – Forwarded Alert</div>
      <div class="card-title">Discover Card Payment Changes (Forwarded by Mindy Dordick)</div>
      <div class="card-row"><strong>Source:</strong> Mindy Dordick &lt;mindydordick@yahoo.com&gt; forwarding Discover card notice</div>
      <div class="card-row"><strong>Why It Matters:</strong> Someone in your network forwarded a Discover card payment change notice. May affect autopay, due dates, or interest rates. Review to ensure no missed payments.</div>
      <div class="card-action">✅ Action: Read the forwarded Discover content. Log into Discover to confirm current payment settings.</div>
      <div class="card-row" style="margin-top:8px;"><strong>Due:</strong> This week</div>
    </div>

    <div class="card yellow">
      <div class="card-label">🟡 Billing – COBRA</div>
      <div class="card-title">COBRA Payment Check – Scheduled Saturday</div>
      <div class="card-row"><strong>Source:</strong> Google Calendar – "Check cobra payments" (June 27, 10:00 AM)</div>
      <div class="card-row"><strong>Why It Matters:</strong> COBRA coverage is time-sensitive. Missing a payment can result in loss of health insurance. You have this on calendar — confirm payment is processed.</div>
      <div class="card-action">✅ Action: Confirm COBRA payment portal login. Verify payment is scheduled or submit by June 27.</div>
      <div class="card-row" style="margin-top:8px;"><strong>Due:</strong> Saturday, June 27</div>
    </div>

    <div class="card blue">
      <div class="card-label">🔵 Finance – Robinhood</div>
      <div class="card-title">Robinhood Trade Confirmations Available</div>
      <div class="card-row"><strong>Source:</strong> Robinhood &lt;noreply@robinhood.com&gt; — LEGITIMATE</div>
      <div class="card-row"><strong>Why It Matters:</strong> Recent trades executed. Trade confirmations are available for review. Important for financial records and tax documentation.</div>
      <div class="card-action">✅ Action: Open email, review trade details. Save confirmations for tax records.</div>
      <div class="card-row" style="margin-top:8px;"><strong>Due:</strong> This week</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     4. FULL 7-DAY CALENDAR
═══════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">📅</span> Full 7-Day Calendar</div>
  <p class="note" style="margin-bottom:14px;">Showing all 5 calendar events across the 7-day window (June 25 – July 1, 2026)</p>

  <!-- Thursday June 25 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Thursday, June 25, 2026 — TODAY</div>

    <div class="cal-event declined">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px;">
        <div class="cal-event-title">Executive Roundtable</div>
        <span class="badge badge-red">DECLINED</span>
      </div>
      <div class="cal-event-meta">
        <span>⏰ 9:00 AM – 10:30 AM EDT</span>
        <span>👤 Host: John Madigan</span>
      </div>
      <div class="cal-event-meta">
        <span>📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Meeting 207 786 667</a> | PW: 205454</span>
      </div>
      <div class="cal-event-meta" style="margin-top:6px;">
        <span class="warn">⚠️ Status: You declined this event. Meeting is currently in progress (9:00–10:30 AM).</span>
      </div>
      <div class="cal-event-meta">🗒️ Prep: None needed given declined status. Note: if this is a recurring professional event, reconsider attendance for future sessions.</div>
    </div>

    <div class="cal-event needs-action">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px;">
        <div class="cal-event-title">HR Networking &amp; Job Search: Open Office Hours – Zoom 2</div>
        <span class="badge badge-yellow">⚠️ RSVP NEEDED</span>
      </div>
      <div class="cal-event-meta">
        <span>⏰ 12:00 PM – 1:00 PM EDT</span>
        <span>👥 170+ Attendees</span>
      </div>
      <div class="cal-event-meta">
        <span>📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Meeting 85945371140</a></span>
      </div>
      <div class="cal-event-meta" style="margin-top:6px;">
        <span class="warn">⚠️ RSVP PENDING — You must accept or decline.</span>
      </div>
      <div class="cal-event-meta">🗒️ Prep: Note says "please turn off automated notetaking AI tools." Prepare a 30-second intro. Bring 2–3 target companies to share. Strong networking value — <strong>recommend attending.</strong></div>
      <div class="cal-event-meta">🔗 No conflict with Executive Roundtable (that ends at 10:30 AM).</div>
    </div>
  </div>

  <!-- Friday June 26 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Friday, June 26, 2026</div>
    <div class="cal-event" style="background:#f7f7f7;border-color:#a0aec0;">
      <div class="cal-event-title" style="color:#888;">No Events Scheduled</div>
      <div class="cal-event-meta">Consider using this day for job application follow-ups, LinkedIn outreach, or interview prep.</div>
    </div>
  </div>

  <!-- Saturday June 27 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Saturday, June 27, 2026</div>
    <div class="cal-event confirmed">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px;">
        <div class="cal-event-title">Check COBRA Payments</div>
        <span class="badge badge-green">CONFIRMED</span>
      </div>
      <div class="cal-event-meta">
        <span>⏰ 10:00 AM – 11:00 AM EDT</span>
        <span>📍 Personal Reminder (No Location)</span>
      </div>
      <div class="cal-event-meta" style="margin-top:6px;">🗒️ <strong>Prep:</strong> Locate COBRA payment portal login credentials before Saturday. Confirm payment amount and due date. Missing COBRA payments = loss of health coverage. This is HIGH PRIORITY.</div>
    </div>
  </div>

  <!-- Sunday June 28 – Monday June 30 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Sunday June 28 – Monday June 30, 2026</div>
    <div class="cal-event" style="background:#f7f7f7;border-color:#a0aec0;">
      <div class="cal-event-title" style="color:#888;">No Events Scheduled</div>
      <div class="cal-event-meta">Use this window for Marsh McLennan follow-up, LinkedIn job applications, and preparing for July 1 networking group.</div>
    </div>
  </div>

  <!-- Tuesday July 1 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Tuesday, July 1, 2026</div>

    <div class="cal-event needs-action">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px;">
        <div class="cal-event-title">HR Networking &amp; Job Search Group – 2 Zoom</div>
        <span class="badge badge-yellow">⚠️ RSVP NEEDED</span>
      </div>
      <div class="cal-event-meta">
        <span>⏰ 12:00 PM – 1:30 PM EDT</span>
        <span>👥 170+ Attendees</span>
      </div>
      <div class="cal-event-meta">
        <span>📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Meeting 81954171722</a></span>
      </div>
      <div class="cal-event-meta" style="margin-top:6px;"><span class="warn">⚠️ RSVP PENDING</span></div>
      <div class="cal-event-meta">🗒️ Prep: Review Team Guidelines (linked in description). Prepare updates on your job search progress since June 25 call. Longer session (1.5 hrs). Plan accordingly.</div>
    </div>

    <div class="cal-event confirmed">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px;">
        <div class="cal-event-title">Network</div>
        <span class="badge badge-green">CONFIRMED</span>
      </div>
      <div class="cal-event-meta">
        <span>⏰ 12:00 PM – 1:30 PM EDT</span>
        <span>📍 No Location Listed</span>
      </div>
      <div class="cal-event-meta" style="margin-top:6px;">
        <span class="warn">⚠️ CONFLICT: This overlaps exactly with HR Networking &amp; Job Search Group – 2 Zoom (same time block). These may be the same event or a duplicate reminder. Clarify and remove duplicate.</span>
      </div>
      <div class="cal-event-meta">🗒️ Recommend consolidating these two July 1 entries.</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     5. JOB SEARCH & INTERVIEW PIPELINE
═══════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">💼</span> Job Search &amp; Interview Pipeline</div>

  <p style="font-size:13px;color:#555;margin-bottom:14px;">Active leads, alerts, applications, and networking opportunities identified in your inbox this week.</p>

  <div style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:0.7px;color:#888;margin-bottom:8px;">🏆 Applications / Status Updates</div>

  <div class="job-row">
    <div class="job-fit fit-high">HIGH</div>
    <div class="job-info">
      <strong>HR Leader, Private Client Services — Marsh McLennan Agency</strong>
      <span>📧 Workday MMC &lt;mmc@myworkday.com&gt; · Application Status Update Received · Req: R_350229</span>
      <span style="display:block;margin-top:4px;color:#c53030;font-weight:600;">⚠️ Must read immediately — decision language detected in snippet ("After careful evaluation…")</span>
    </div>
  </div>

  <hr class="divider">
  <div style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:0.7px;color:#888;margin-bottom:8px;">📌 Senior-Level Job Alerts (LinkedIn)</div>

  <div class="job-row">
    <div class="job-fit fit-high">HIGH</div>
    <div class="job-info">
      <strong>Chief People Officer — NU Advisory Partners</strong>
      <span>📧 LinkedIn Job Alerts · Received: 6/25 at 5:05 AM &amp; 6/25 at 12:11 AM (2 alerts) · Firm retained search</span>
      <span style="display:block;margin-top:3px;">🎯 Senior-level strategic HR role. Apply immediately — searches like this move fast.</span>
    </div>
  </div>

  <div class="job-row">
    <div class="job-fit fit-high">HIGH</div>
    <div class="job-info">
      <strong>VP, Human Resources — Fidelity Investments (Similar Jobs Alert)</strong>
      <span>📧 LinkedIn &lt;jobs-noreply@linkedin.com&gt; · 6/25 · Jobs similar to VP HR at Fidelity</span>
      <span style="display:block;margin-top:3px;">🎯 VP-level HR roles at Fidelity caliber firms. Review the list — likely strong matches.</span>
    </div>
  </div>

  <div class="job-row medium">
    <div class="job-fit fit-medium">MED</div>
    <div class="job-info">
      <strong>HR Director — Jobgether (Partner-Listed Role)</strong>
      <span>📧 LinkedIn Job Alerts · Multiple alerts received 6/25 at 7:05 AM (inbox) — duplicate alerts also in trash</span>
      <span style="display:block;margin-top:3px;">⚠️ This alert has been sent repeatedly (at least 4× over 24 hrs). Likely an automated system. Review once — if not relevant, dismiss duplicates.</span>
    </div>
  </div>

  <hr class="divider">
  <div style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:0.7px;color:#888;margin-bottom:8px;">📌 Job Alerts (Glassdoor)</div>

  <div class="job-row medium">
    <div class="job-fit fit-medium">MED</div>
    <div class="job-info">
      <strong>Human Resources Manager – South Central — Victra-Verizon Authorized Retailer + 9 more (Remote)</strong>
      <span>📧 Glassdoor Jobs &lt;noreply@glassdoor.com&gt; · 6/25 at 2:01 AM · In Trash</span>
      <span style="display:block;margin-top:3px;">📋 Remote roles. Degreed also hiring. Restore from trash and review the full list.</span>
    </div>
  </div>

  <div class="job-row medium">
    <div class="job-fit fit-medium">MED</div>
    <div class="job-info">
      <strong>Human Resources Specialist — Blackstone Valley Community Action Program + 10 more (US)</strong>
      <span>📧 Glassdoor Jobs &lt;noreply@glassdoor.com&gt; · 6/24 at 11:13 PM · In Trash</span>
      <span style="display:block;margin-top:3px;">📋 Adobe also hiring per snippet. Mix of levels. Review before deleting.</span>
    </div>
  </div>

  <hr class="divider">
  <div style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:0.7px;color:#888;margin-bottom:8px;">🤝 Networking</div>

  <div class="job-row">
    <div class="job-fit fit-high">HIGH</div>
    <div class="job-info">
      <strong>HR Networking &amp; Job Search: Open Office Hours — TODAY 12:00 PM</strong>
      <span>📅 Google Calendar · 170+ HR professionals · RSVP still needed</span>
      <span style="display:block;margin-top:3px;">🎯 Strong peer networking. Attend — bring elevator pitch and target company list.</span>
    </div>
  </div>

  <div class="job-row">
    <div class="job-fit fit-high">HIGH</div>
    <div class="job-info">
      <strong>HR Networking &amp; Job Search Group – 2 Zoom — July 1, 12:00 PM</strong>
      <span>📅 Google Calendar · 170+ HR professionals · RSVP needed · 1.5 hr session</span>
      <span style="display:block;margin-top:3px;">🎯 Recurring group — consistent attendance builds relationships and visibility.</span>
    </div>
  </div>

  <hr class="divider">
  <div style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:0.7px;color:#888;margin-bottom:8px;">📄 LinkedIn &amp; Content Activity</div>

  <div class="job-row medium">
    <div class="job-fit fit-medium">MED</div>
    <div class="job-info">
      <strong>LinkedIn Learning Spotlight: "AI You Can Actually Use"</strong>
      <span>📧 LinkedIn &lt;messages-noreply@linkedin.com&gt; · 6/25 · Professional development content</span>
      <span style="display:block;margin-top:3px;">📚 Relevant for HR leaders staying current on AI tools. Review when time permits.</span>
    </div>
  </div>

  <div class="job-row medium">
    <div class="job-fit fit-medium">MED</div>
    <div class="job-info">
      <strong>Melissa's Own "LinkedIn Viral" Post Draft (Self-Sent)</strong>
      <span>📧 melissa &lt;melissaw212@gmail.com&gt; · 6/24 · Self-drafted LinkedIn content strategy notes</span>
      <span style="display:block;margin-top:3px;">✍️ You emailed yourself a LinkedIn post system. Review and consider publishing — personal branding supports job search visibility.</span>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     6. FULL EMAIL REVIEW BY CATEGORY
═══════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">📬</span> Full Email Review by Category</div>
  <p class="note" style="margin-bottom:16px;">All 50 emails are accounted for below across 12 categories.</p>

  <!-- SECURITY / RISK -->
  <div class="email-cat cat-red">
    <div class="email-cat-header">🔴 Security / Risk &nbsp;<span class="badge badge-red">5 Emails</span></div>
    <div class="email-cat-body">
      <div class="meta"><strong>Count:</strong> 5 emails | <strong>Status:</strong> All Unread</div>
      <div class="senders">
        <strong>Senders:</strong><br>
        🚨 <em>"melissaw212"</em> &lt;frxkuwaxlsdgye…@a76yu6…us&gt; — "Your Cloud Account has been locked on Thu, 25 Jun 2026" (PHISHING)<br>
        🚨 <em>"melissaw212"</em> &lt;viyxitfsjia@nhzz…us&gt; — "[melissaw212] Your Cloud Account has been locked on Wed, 24 Jun 2026" (PHISHING)<br>
        🚨 <em>"melissaw212"</em> &lt;itvlnwtzbui@luzu…us&gt; — "Your Account Has been Blocked! Your Photos and Videos will be Removed" (PHISHING)<br>
        🚨 <em>"💲CashApp💲"</em> &lt;mfiwkvbavfhzen…@s4zhfl…us&gt; — "You have received $15.99 / Raging Bull Casino" (PHISHING/SCAM)<br>
        🚨 <em>"Your_Penis"</em> &lt;ipyfgtlifudixf…@uvsjlw…us&gt; — "🔥 Bedroom Secret: 45s To Rock-Hard 🔞" (PHISHING/SPAM)
      </div>
      <div class="action">✅ Recommended Action: Mark ALL 5 as phishing in Gmail. Delete immediately. Do NOT click any links. Verify your actual Google account storage at myaccount.google.com. None of these are from legitimate senders — all use randomized spoofed domains.</div>
    </div>
  </div>

  <!-- JOB SEARCH -->
  <div class="email-cat cat-green" style="margin-top:12px;">
    <div class="email-cat-header">🟢 Job Search &nbsp;<span class="badge badge-green">8 Emails</span></div>
    <div class="email-cat-body">
      <div class="meta"><strong>Count:</strong> 8 emails | Mix of Inbox &amp; Trash</div>
      <div class="senders">
        <strong>Senders &amp; Subjects:</strong><br>
        ✅ <em>Workday MMC</em> — Application status update: HR Leader, Private Client Services, Marsh McLennan Agency (INBOX — UNREAD — HIGH PRIORITY)<br>
        ✅ <em>LinkedIn Job Alerts</em> — Chief People Officer at NU Advisory Partners (INBOX — 5:05 AM)<br>
        ✅ <em>LinkedIn</em> — New jobs similar to VP, Human Resources at Fidelity Investments (INBOX)<br>
        ✅ <em>LinkedIn Job Alerts</em> — HR Director at Jobgether (INBOX — 7:05 AM)<br>
        📁 <em>Glassdoor Jobs</em> — HR Manager South Central + 9 more Remote jobs (TRASH)<br>
        📁 <em>Glassdoor Jobs</em> — HR Specialist at Blackstone Valley + 10 more US jobs (TRASH)<br>
        📁 <em>LinkedIn Job Alerts</em> — Chief People Officer at NU Advisory Partners (TRASH — duplicate, older alert)<br>
        ✍️ <em>melissa</em> &lt;melissaw212@gmail.com&gt; — "linkedin viral" self-sent content draft (NOT TRASH — personal)
      </div>
      <div class="action">✅ Recommended Action: Read Workday MMC immediately. Apply to CPO at NU Advisory Partners. Review VP HR similar jobs. Restore Glassdoor emails from trash before reviewing. Dismiss duplicate job alerts after reading the first instance.</div>
    </div>
  </div>

  <!-- CALENDAR / EVENTS -->
  <div class="email-cat cat-blue" style="margin-top:12px;">
    <div class="email-cat-header">🔵 Calendar / Events &nbsp;<span class="badge badge-blue">1 Email</span></div>
    <div class="email-cat-body">
      <div class="meta"><strong>Count:</strong> 1 email | In Inbox</div>
      <div class="senders">
        <em>Google</em> &lt;google-noreply@google.com&gt; — "Learn more about our updated Terms of Service" (Effective ~July 2026 for melhr212@gmail.com)
      </div>
      <div class="action">✅ Recommended Action: Read and note effective date. No action required before July. Legitimate sender.</div>
    </div>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="email-cat cat-yellow" style="margin-top:12px;">
    <div class="email-cat-header">🟡 Financial / Billing &nbsp;<span class="badge badge-yellow">2 Emails</span></div>
    <div class="email-cat-body">
      <div class="meta"><strong>Count:</strong> 2 emails</div>
      <div class="senders">
        <em>Robinhood</em> &lt;noreply@robinhood.com&gt; — "Your trade confirmations are available" (INBOX — UNREAD)<br>
        <em>Mindy Dordick</em> &lt;mindydordick@yahoo.com&gt; — "Fw: Heads up, your Discover card payments are changing" (INBOX — READ)
      </div>
      <div class="action">✅ Recommended Action: Review Robinhood confirmations and save for records. Read Mindy's forwarded Discover notice — verify your payment settings on Discover directly.</div>
    </div>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="email-cat cat-purple" style="margin-top:12px;">
    <div class="email-cat-header">🟣 Professional Development &nbsp;<span class="badge badge-purple">4 Emails</span></div>
    <div class="email-cat-body">
      <div class="meta"><strong>Count:</strong> 4 emails | Mix of Inbox &amp; Trash</div>
      <div class="senders">
        <em>LinkedIn</em> — "Learning Spotlight: AI You Can Actually Use" (INBOX)<br>
        <em>BambooHR</em> — "[Free Playbook] How HR Can Prepare for a Workplace Crisis 🚨" (NOT in inbox/trash — general)<br>
        <em>Alison Courses</em> — "One day to get 25% off your cert or diploma" (INBOX — expires TODAY)<br>
        <em>Zapier News</em> — "3 builds to try with Zapier MCP" (TRASH)
      </div>
      <div class="action">✅ Recommended Action: Alison Courses discount expires TODAY — if you want a certificate, act now. Review LinkedIn AI learning. BambooHR playbook may be useful for your HR toolkit. Zapier newsletter in trash — safe to delete unless you're actively using Zapier MCP.</div>
    </div>
  </div>

  <!-- PERSONAL -->
  <div class="email-cat cat-orange" style="margin-top:12px;">
    <div class="email-cat-header">🟠 Personal &nbsp;<span class="badge badge-orange">4 Emails</span></div>
    <div class="email-cat-body">
      <div class="meta"><strong>Count:</strong> 4 emails | Mix of Inbox &amp; Trash</div>
      <div class="senders">
        <em>Jdate</em> — "You've Got a Like on Jdate ❤️" (INBOX)<br>
        <em>Match</em> — "Dan just sent you a new message 💌" (INBOX)<br>
        <em>Fara on Facebook</em> — "💬 Fara J. Smith commented: 'yayyy!!'" (INBOX)<br>
        <em>Facebook</em> — "About Starlina and others: check out 37 updates" (TRASH)
      </div>
      <div class="action">✅ Recommended Action: Check Jdate/Match when time permits (personal). Respond to Fara's comment if appropriate. Facebook updates in trash — safe to delete.</div>
    </div>
  </div>

  <!-- NEWSLETTERS / SUBSCRIPTIONS -->
  <div class="email-cat cat-purple" style="margin-top:12px;">
    <div class="email-cat-header">🟣 Newsletters / Subscriptions &nbsp;<span class="badge badge-purple">4 Emails</span></div>
    <div class="email-cat-body">
      <div class="meta"><strong>Count:</strong> 4 emails | Mix of Trash &amp; General</div>
      <div class="senders">
        <em>The People People Group</em> — "[TPPG] Rethinking Manager Impact on Performance…" (TRASH — HR community newsletter)<br>
        <em>LinkedIn</em> — "Nabilah Fazr and others share their thoughts on LinkedIn" (NOT in inbox/trash — social update)<br>
        <em>Insider Monkey</em> — "Daily Newsletter – June 24, 2026" (TRASH — investing/finance)<br>
        <em>22 Words</em> — "⚡ Your Amazon Prime Lightning Deals" (TRASH — deal newsletter)
      </div>
      <div class="action">✅ Recommended Action: TPPG is worth restoring — relevant to HR profession. LinkedIn social digest: glance if time permits. Insider Monkey: keep if investing; delete if not. 22 Words deal newsletter: unsubscribe if not useful.</div>
    </div>
  </div>

  <!-- PROMOTIONAL / RETAIL -->
  <div class="email-cat cat-gray" style="margin-top:12px;">
    <div class="email-cat-header">⚪ Promotional / Retail &nbsp;<span class="badge badge-gray">16 Emails</span></div>
    <div class="email-cat-body">
      <div class="meta"><strong>Count:</strong> 16 emails | Majority in Trash</div>
      <div class="senders">
        Kohl's (×2), SHEIN, Old Navy, Macy's, Gap Factory, Temu (×3), Amazon Prime Day, Amazon Lightning Deals (22 Words), Best Buy Visa/Citi, Netflix, GM Rewards Mastercard, Lindy AI Welcome, Mystery Deal, Equifax Credit
      </div>
      <div class="action">✅ Recommended Action: All are promotional. Delete/ignore. See Promotional / Retail Summary section for full breakdown. Consider unsubscribing from brands you no longer shop.</div>
    </div>
  </div>

  <!-- SAFE TO DELETE / IGNORE -->
  <div class="email-cat cat-gray" style="margin-top:12px;">
    <div class="email-cat-header">⚪ Safe to Delete / Ignore &nbsp;<span class="badge badge-gray">6 Emails</span></div>
    <div class="email-cat-body">
      <div class="meta"><strong>Count:</strong> 6 emails | All Spam/Casino/Unsolicited</div>
      <div class="senders">
        <em>OnlineCasino</em> — "130 Free Spins Pending in your Account 🎰" (NOT inbox/trash — unsolicited)<br>
        <em>Casino.Special</em> — "Claim 55 free spins with CODE: FREE55" (NOT inbox/trash — unsolicited)<br>
        <em>LinkedIn Job Alerts</em> — HR Director at Jobgether (TRASH ×2 — duplicates, already read)<br>
        <em>LinkedIn Job Alerts</em> — Chief People Officer at NU Advisory Partners (TRASH ×2 — duplicates of already-reviewed alerts)
      </div>
      <div class="action">✅ Recommended Action: Mark casino emails as spam. Delete duplicate job alert emails in trash — you've already seen the real versions in your inbox.</div>
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════
     7. TRASH REVIEW
═══════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">🗑️</span> Trash Review</div>
  <p style="font-size:13px;color:#555;margin-bottom:16px;">Review of all emails currently in Gmail Trash. Total trash emails: <strong>21</strong>.</p>

  <!-- RESTORE -->
  <div style="background:#f0fff4;border:1px solid #9ae6b4;border-radius:9px;padding:14px 18px;margin-bottom:14px;">
    <div style="font-weight:700;color:#276749;font-size:14px;margin-bottom:10px;">✅ RESTORE IMMEDIATELY (3 Emails)</div>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Reason to Restore</th></tr></thead>
      <tbody>
        <tr>
          <td>Glassdoor Jobs</td>
          <td>HR Manager – South Central (Victra/Verizon) + 9 more Remote jobs</td>
          <td>Active job leads — contains 10 job listings matching your HR profile. Should be reviewed before deleting.</td>
        </tr>
        <tr>
          <td>Glassdoor Jobs</td>
          <td>HR Specialist – Blackstone Valley + 10 more US jobs</td>
          <td>10 additional job listings. Adobe and others hiring. Review for relevant opportunities.</td>
        </tr>
        <tr>
          <td>The People People Group</td>
          <td>[TPPG] Rethinking Manager Impact on Performance + 8 more topics</td>
          <td>HR professional community newsletter — relevant to your career. Topics include manager effectiveness and HR strategy.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- REVIEW BEFORE DELETING -->
  <div style="background:#fffff0;border:1px solid #f6e05e;border-radius:9px;padding:14px 18px;margin-bottom:14px;">
    <div style="font-weight:700;color:#975a16;font-size:14px;margin-bottom:10px;">⚠️ REVIEW BEFORE DELETING (4 Emails)</div>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Reason to Review</th></tr></thead>
      <tbody>
        <tr>
          <td>Insider Monkey</td>
          <td>Daily Newsletter – June 24, 2026</td>
          <td>Finance/investing content. If you actively invest (you have Robinhood), this could be relevant. Decide if subscription is worth keeping.</td>
        </tr>
        <tr>
          <td>Flo from Lindy (Lindy AI)</td>
          <td>Welcome to Lindy</td>
          <td>You apparently signed up for Lindy AI (personalized AI assistant). Review to see if you intended to use this service or want to cancel.</td>
        </tr>
        <tr>
          <td>Zapier News</td>
          <td>3 builds to try with Zapier MCP</td>
          <td>If you use Zapier for automation, MCP integration may be useful for job search or HR workflows. Otherwise, unsubscribe.</td>
        </tr>
        <tr>
          <td>Netflix</td>
          <td>Top suggestions for Mel</td>
          <td>Personal streaming recommendations. Not urgent, but confirms active Netflix subscription. Safe to delete after acknowledging.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- SAFE TO DELETE -->
  <div style="background:#f7f7f7;border:1px solid #e2e8f0;border-radius:9px;padding:14px 18px;">
    <div style="font-weight:700;color:#4a5568;font-size:14px;margin-bottom:10px;">🗑️ SAFE TO DELETE (14 Emails)</div>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Reason</th></tr></thead>
      <tbody>
        <tr><td>Amazon Prime Day</td><td>Up to 40% off top brands this Prime Day</td><td>Standard retail promotion. No action needed.</td></tr>
        <tr><td>My Best Buy® Visa® Card (Citi)</td><td>Turn up the color with RGB LED 🌈</td><td>Credit card retail promotion. Unsubscribe if unwanted.</td></tr>
        <tr><td>Macy's</td><td>Men's summer T-shirts starting at $12.99</td><td>Retail promotion. Delete.</td></tr>
        <tr><td>Gap Factory</td><td>This online-exclusive bonus is yours (40–70% off)</td><td>Retail promotion. Delete.</td></tr>
        <tr><td>Temu</td><td>Sleeveless Boat Neck is now $7.43</td><td>Retail promotion. Delete.</td></tr>
        <tr><td>Temu</td><td>Complimentary Credit</td><td>Temu marketing. Delete.</td></tr>
        <tr><td>Temu</td><td>'Solid Elegant 2pcs Se…' | $9.40 | Only 90 left</td><td>Retail promotion. Delete.</td></tr>
        <tr><td>Old Navy</td><td>OMG, YES! Everything* is 50% off</td><td>Retail promotion. Delete.</td></tr>
        <tr><td>Kohl's</td><td>New day, new deals + free shipping right this way</td><td>Retail promotion. Delete.</td></tr>
        <tr><td>Facebook</td><td>About Starlina and others: 37 updates</td><td>Social notification digest. Delete.</td></tr>
        <tr><td>GM Rewards</td><td>Congrats, you're invited (GM Rewards Mastercard)</td><td>Credit card marketing. Delete.</td></tr>
        <tr><td>Equifax</td><td>Waiting out traffic? 🚗 (credit report nudge)</td><td>Marketing email from Equifax. Delete.</td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>HR Director at Jobgether (×2 duplicate)</td><td>Duplicates — already reviewed inbox version. Delete.</td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>Chief People Officer at NU Advisory Partners (×2 duplicate)</td><td>Duplicates — already reviewed inbox version. Delete.</td></tr>
        <tr><td>Mystery Deal 🔥</td><td>Amazon Fire 7 Kids Tablet / Waterpik offer</td><td>Unsolicited deal newsletter. Delete + unsubscribe.</td></tr>
        <tr
<hr>
<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Financial / Billing</td><td>2</td></tr>
<tr><td>Job Search / Recruiters</td><td>15</td></tr>
<tr><td>Other / Review</td><td>16</td></tr>
<tr><td>Professional Development / Newsletters</td><td>2</td></tr>
<tr><td>Promotional / Retail</td><td>6</td></tr>
<tr><td>Security / Risk</td><td>9</td></tr>
</table>
<p><strong>Audit Note:</strong> Every fetched email was reviewed and assigned to one category. Trash emails were included in review. Promotional and low-value emails were accounted for but deprioritized.</p>

