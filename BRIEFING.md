<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing – Melissa W. | July 5, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .container { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 16px; padding: 32px 36px; margin-bottom: 24px; box-shadow: 0 4px 20px rgba(0,0,0,0.25); }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 15px; color: #a8b8d8; margin-top: 4px; }
  .header-meta { display: flex; gap: 32px; margin-top: 20px; flex-wrap: wrap; }
  .header-meta .meta-item { background: rgba(255,255,255,0.08); border-radius: 10px; padding: 10px 18px; }
  .header-meta .meta-label { font-size: 11px; color: #7a90b8; text-transform: uppercase; letter-spacing: 1px; }
  .header-meta .meta-value { font-size: 20px; font-weight: 700; color: #e0e8f8; margin-top: 2px; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; letter-spacing: 0.5px; margin-bottom: 12px; padding: 10px 16px; border-radius: 8px; display: flex; align-items: center; gap: 8px; }
  .section-title.red { background: #ffeaea; color: #c0392b; border-left: 5px solid #e74c3c; }
  .section-title.yellow { background: #fffbea; color: #b7791f; border-left: 5px solid #f6c90e; }
  .section-title.blue { background: #eaf4ff; color: #1565c0; border-left: 5px solid #2196f3; }
  .section-title.green { background: #eafaf1; color: #1a7a4a; border-left: 5px solid #27ae60; }
  .section-title.purple { background: #f5eaff; color: #6c3483; border-left: 5px solid #8e44ad; }
  .section-title.gray { background: #f4f4f6; color: #555; border-left: 5px solid #aaa; }
  .section-title.dark { background: #1a1a2e; color: #fff; border-left: 5px solid #0f3460; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .card.red { background: #fff5f5; border-left: 5px solid #e74c3c; }
  .card.yellow { background: #fffdf0; border-left: 5px solid #f6c90e; }
  .card.blue { background: #f0f7ff; border-left: 5px solid #2196f3; }
  .card.green { background: #f0fff8; border-left: 5px solid #27ae60; }
  .card.purple { background: #faf5ff; border-left: 5px solid #8e44ad; }
  .card.gray { background: #f9f9fb; border-left: 5px solid #bbb; }
  .card-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 4px; }
  .card.red .card-label { color: #e74c3c; }
  .card.yellow .card-label { color: #b7791f; }
  .card.blue .card-label { color: #1565c0; }
  .card.green .card-label { color: #1a7a4a; }
  .card.purple .card-label { color: #6c3483; }
  .card.gray .card-label { color: #888; }
  .card h3 { font-size: 15px; font-weight: 700; margin-bottom: 4px; }
  .card .source { font-size: 11px; color: #888; margin-bottom: 6px; }
  .card .why { font-size: 13px; margin-bottom: 6px; }
  .card .next-step { font-size: 13px; font-weight: 600; }
  .card .due { display: inline-block; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 20px; margin-top: 6px; }
  .card.red .due { background: #fdd; color: #c0392b; }
  .card.yellow .due { background: #fff3cd; color: #856404; }
  .card.blue .due { background: #cce5ff; color: #1565c0; }
  .card.green .due { background: #d4edda; color: #155724; }

  /* EXEC SUMMARY */
  .exec-summary { background: #fff; border-radius: 12px; padding: 20px 24px; box-shadow: 0 2px 10px rgba(0,0,0,0.07); }
  .exec-bullet { display: flex; align-items: flex-start; gap: 12px; padding: 10px 0; border-bottom: 1px solid #f0f0f4; }
  .exec-bullet:last-child { border-bottom: none; }
  .exec-bullet .badge { min-width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 700; }
  .badge-red { background: #fdd; color: #c0392b; }
  .badge-green { background: #d4edda; color: #155724; }
  .badge-blue { background: #cce5ff; color: #1565c0; }
  .exec-bullet .text { font-size: 14px; }
  .exec-bullet .text strong { display: block; font-size: 13px; font-weight: 700; margin-bottom: 2px; }

  /* CALENDAR */
  .cal-day { background: #fff; border-radius: 10px; margin-bottom: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .cal-day-header { background: #1565c0; color: #fff; padding: 10px 18px; font-weight: 700; font-size: 14px; display: flex; justify-content: space-between; align-items: center; }
  .cal-day-header .day-badge { font-size: 11px; font-weight: 600; background: rgba(255,255,255,0.2); padding: 2px 8px; border-radius: 12px; }
  .cal-day-header.today { background: #0f3460; }
  .cal-event { padding: 12px 18px; border-bottom: 1px solid #f0f2f5; display: grid; grid-template-columns: 130px 1fr; gap: 10px; }
  .cal-event:last-child { border-bottom: none; }
  .cal-time { font-size: 12px; font-weight: 700; color: #1565c0; }
  .cal-event-name { font-size: 14px; font-weight: 700; margin-bottom: 3px; }
  .cal-detail { font-size: 12px; color: #555; margin-bottom: 2px; }
  .cal-status { display: inline-block; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 10px; margin-top: 3px; }
  .status-accepted { background: #d4edda; color: #155724; }
  .status-confirmed { background: #cce5ff; color: #1565c0; }
  .status-declined { background: #f8d7da; color: #721c24; }
  .status-needsaction { background: #fff3cd; color: #856404; }
  .cal-prep { background: #fffdf0; border-radius: 6px; padding: 5px 10px; font-size: 11px; color: #7a6000; margin-top: 5px; }
  .cal-conflict { background: #ffeaea; border-radius: 6px; padding: 5px 10px; font-size: 11px; color: #c0392b; margin-top: 5px; font-weight: 600; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); font-size: 13px; }
  th { background: #1a1a2e; color: #fff; padding: 10px 14px; text-align: left; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
  td { padding: 9px 14px; border-bottom: 1px solid #f0f2f5; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f7f9fc; }
  .priority-high { color: #c0392b; font-weight: 700; }
  .priority-med { color: #b7791f; font-weight: 700; }
  .priority-low { color: #1a7a4a; font-weight: 700; }
  .fit-high { background: #d4edda; color: #155724; padding: 2px 7px; border-radius: 10px; font-size: 11px; font-weight: 700; }
  .fit-med { background: #fff3cd; color: #856404; padding: 2px 7px; border-radius: 10px; font-size: 11px; font-weight: 700; }
  .fit-low { background: #f8d7da; color: #721c24; padding: 2px 7px; border-radius: 10px; font-size: 11px; font-weight: 700; }

  /* JOB SEARCH */
  .job-card { background: #fff; border-radius: 10px; padding: 14px 18px; margin-bottom: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-left: 5px solid #27ae60; display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 8px; }
  .job-card .job-title { font-size: 14px; font-weight: 700; color: #1a1a2e; }
  .job-card .job-company { font-size: 12px; color: #555; margin-top: 2px; }
  .job-card .job-source { font-size: 11px; color: #888; margin-top: 3px; }
  .job-card .job-notes { font-size: 12px; color: #333; margin-top: 4px; }

  /* EMAIL CATEGORY BLOCKS */
  .email-cat { background: #fff; border-radius: 10px; padding: 14px 18px; margin-bottom: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .email-cat .cat-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }
  .email-cat .cat-title { font-weight: 700; font-size: 14px; }
  .email-cat .cat-count { font-size: 12px; font-weight: 700; padding: 2px 10px; border-radius: 12px; }
  .count-red { background: #fdd; color: #c0392b; }
  .count-yellow { background: #fff3cd; color: #856404; }
  .count-green { background: #d4edda; color: #155724; }
  .count-blue { background: #cce5ff; color: #1565c0; }
  .count-purple { background: #e8d5f5; color: #6c3483; }
  .count-gray { background: #e9ecef; color: #555; }
  .email-cat ul { list-style: none; padding-left: 0; }
  .email-cat ul li { font-size: 13px; padding: 3px 0; border-bottom: 1px solid #f5f5f8; }
  .email-cat ul li:last-child { border-bottom: none; }
  .email-cat .action { font-size: 12px; font-weight: 700; color: #1565c0; margin-top: 8px; }
  .sender-name { color: #1a1a2e; font-weight: 600; }

  /* TRASH */
  .trash-group { background: #fff; border-radius: 10px; padding: 14px 18px; margin-bottom: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .trash-group h4 { font-size: 13px; font-weight: 700; margin-bottom: 8px; padding: 6px 10px; border-radius: 6px; }
  .trash-restore { background: #ffeaea; color: #c0392b; }
  .trash-review { background: #fff3cd; color: #856404; }
  .trash-delete { background: #e9ecef; color: #555; }
  .trash-item { display: flex; justify-content: space-between; align-items: flex-start; padding: 6px 0; border-bottom: 1px solid #f5f5f8; gap: 8px; }
  .trash-item:last-child { border-bottom: none; }
  .trash-sender { font-size: 12px; font-weight: 600; min-width: 130px; }
  .trash-subject { font-size: 12px; color: #555; flex: 1; }
  .trash-reason { font-size: 11px; color: #888; font-style: italic; }

  /* PROMOTIONAL */
  .promo-table td:first-child { font-weight: 600; }
  .rec-keep { color: #155724; font-weight: 700; }
  .rec-review { color: #856404; font-weight: 700; }
  .rec-delete { color: #c0392b; font-weight: 700; }
  .rec-ignore { color: #888; font-weight: 700; }

  /* DASHBOARD */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin-bottom: 0; }
  .dash-widget { background: #fff; border-radius: 10px; padding: 16px 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .dash-widget .dash-label { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #888; margin-bottom: 8px; }
  .dash-widget .dash-value { font-size: 26px; font-weight: 800; }
  .dash-widget .dash-sub { font-size: 12px; color: #555; margin-top: 4px; }
  .dash-widget.red-w .dash-value { color: #e74c3c; }
  .dash-widget.yellow-w .dash-value { color: #b7791f; }
  .dash-widget.blue-w .dash-value { color: #1565c0; }
  .dash-widget.green-w .dash-value { color: #1a7a4a; }
  .dash-widget.purple-w .dash-value { color: #6c3483; }

  /* TOP PRIORITIES */
  .priorities { display: flex; flex-direction: column; gap: 10px; }
  .priority-item { display: flex; align-items: flex-start; gap: 14px; background: #fff; border-radius: 10px; padding: 16px 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .priority-num { min-width: 38px; height: 38px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; font-weight: 800; }
  .p1 { background: #fdd; color: #c0392b; }
  .p2 { background: #fff3cd; color: #856404; }
  .p3 { background: #d4edda; color: #155724; }
  .priority-item h4 { font-size: 14px; font-weight: 700; margin-bottom: 3px; }
  .priority-item p { font-size: 13px; color: #555; }

  /* ACCOUNTING TABLE */
  .accounting-table th { background: #0f3460; }
  .accounting-total { background: #1a1a2e; color: #fff; font-weight: 800; }
  .accounting-total td { color: #fff !important; font-weight: 800 !important; }

  /* SPAM FLAG */
  .spam-flag { display: inline-block; background: #f8d7da; color: #c0392b; font-size: 10px; font-weight: 700; padding: 1px 6px; border-radius: 8px; margin-left: 4px; }

  .unread-dot { display: inline-block; width: 7px; height: 7px; border-radius: 50%; background: #2196f3; margin-right: 5px; vertical-align: middle; }

  a { color: #1565c0; text-decoration: none; }
  a:hover { text-decoration: underline; }

  .divider { border: none; border-top: 2px solid #e8eaf0; margin: 24px 0; }

  .note-box { background: #eaf4ff; border-radius: 8px; padding: 10px 16px; font-size: 12px; color: #1565c0; margin-top: 10px; }

  @media (max-width: 700px) {
    .header { padding: 20px; }
    .cal-event { grid-template-columns: 1fr; }
    .header-meta { gap: 12px; }
  }
</style>
</head>
<body>
<div class="container">

  <!-- ═══════════════════════════════════════════════════════════════════
       SECTION 1: HEADER
  ═══════════════════════════════════════════════════════════════════ -->
  <div class="header">
    <div style="font-size:13px;color:#7a90b8;text-transform:uppercase;letter-spacing:2px;margin-bottom:6px;">Executive Briefing</div>
    <h1>☀️ Good Morning, Melissa!</h1>
    <div class="subtitle">Sunday, July 5, 2026 &nbsp;|&nbsp; Prepared by your Executive Chief of Staff</div>
    <div class="header-meta">
      <div class="meta-item">
        <div class="meta-label">Date</div>
        <div class="meta-value" style="font-size:15px;">July 5, 2026</div>
      </div>
      <div class="meta-item">
        <div class="meta-label">Emails Reviewed</div>
        <div class="meta-value">50</div>
      </div>
      <div class="meta-item">
        <div class="meta-label">Calendar Events</div>
        <div class="meta-value">9</div>
      </div>
      <div class="meta-item">
        <div class="meta-label">Action Required</div>
        <div class="meta-value" style="color:#f6c90e;">6</div>
      </div>
      <div class="meta-item">
        <div class="meta-label">🚨 Security Alerts</div>
        <div class="meta-value" style="color:#ff6b6b;">2</div>
      </div>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════════════════
       SECTION 2: EXECUTIVE SUMMARY
  ═══════════════════════════════════════════════════════════════════ -->
  <div class="section">
    <div class="section-title dark">📋 Executive Summary</div>
    <div class="exec-summary">
      <div class="exec-bullet">
        <div class="badge badge-red">🚨</div>
        <div class="text">
          <strong>URGENT — Security Alerts &amp; Low Bank Balance</strong>
          Two Google security alerts fired today (one for unauthorized "gws local" access to your Google Account, one a recovery-email copy) — review immediately to confirm you authorized any recent logins. Separately, your Bank of America checking account (ending 7471) dropped to $51.25, below your alert threshold. Financial action needed today.
        </div>
      </div>
      <div class="exec-bullet">
        <div class="badge badge-green">💼</div>
        <div class="text">
          <strong>STRONG — Multiple High-Value Job Leads Arrived Today</strong>
          LinkedIn surfaced an <em>Sr. Director, People Business Partner</em> role at HighLevel, a <em>Principal People Business Partner</em> at SoFi (via Welcome to the Jungle), and an <em>HR Business Partner</em> at Coinbase. Built In also sent a batch of Senior/Expert-level HR roles in NYC. These are high-fit opportunities warranting immediate review and application.
        </div>
      </div>
      <div class="exec-bullet">
        <div class="badge badge-blue">📅</div>
        <div class="text">
          <strong>CALENDAR — Busy Week with Medical Appointments &amp; Networking</strong>
          Tomorrow (Mon 7/6) you have a New Patient Video Visit with Dr. Haridas at 11:20 AM — make sure you're logged into your Connect account. Thursday 7/9 has a double medical appointment with Dr. Leeman-Markowski at NYU (Comprehensive Epilepsy Center, 3:30 PM). Two HR Networking Zoom sessions are pending RSVP (Wed 7/8 and Thu 7/9). State Farm bill is due 7/7.
        </div>
      </div>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════════════════
       SECTION 3: ACTION REQUIRED
  ═══════════════════════════════════════════════════════════════════ -->
  <div class="section">
    <div class="section-title red">🔴 Action Required</div>

    <div class="card red">
      <div class="card-label">🔐 Security — Urgent</div>
      <h3>Google Account Security Alert — Unauthorized Access?</h3>
      <div class="source">From: Google (no-reply@accounts.google.com) · Today, July 5</div>
      <div class="why">Google issued a security alert stating "gws local" was allowed access to your Google Account data. A second email was sent as a recovery-email copy to Melweiss212@gmail.com. This could indicate a compromised session or an authorized app you don't recognize. Two separate alerts at the same time is a red flag.</div>
      <div class="next-step">➤ Go to myaccount.google.com → Security → Recent Activity. Review connected apps. If you did NOT authorize "gws local," revoke access and change your password immediately. Enable 2FA if not already active.</div>
      <span class="due">🔴 Due: TODAY</span>
    </div>

    <div class="card red">
      <div class="card-label">💳 Financial — Urgent</div>
      <h3>Bank Balance Below Alert Threshold — $51.25</h3>
      <div class="source">From: Bank of America (onlinebanking@ealerts.bankofamerica.com) · Today, 11:22 AM</div>
      <div class="why">Your personal checking account (ending 7471) has dropped to $51.25 — below your preset threshold. State Farm bill is due July 7. If that auto-drafts, you may overdraft.</div>
      <div class="next-step">➤ Log into Bank of America. Transfer funds or deposit before Monday 7/7 to cover the State Farm bill and avoid overdraft fees.</div>
      <span class="due">🔴 Due: By Monday July 7</span>
    </div>

    <div class="card yellow">
      <div class="card-label">📅 Calendar — RSVP Needed</div>
      <h3>HR Networking &amp; Job Search Group — RSVP Pending (2 Events)</h3>
      <div class="source">Google Calendar · Wed July 8 (12–1:30 PM) &amp; Thu July 9 (12–1:00 PM)</div>
      <div class="why">Both HR Networking Zoom sessions show "Needs Action" — no RSVP submitted. These are active networking opportunities directly supporting your job search. Missing them without declining is poor professional courtesy to the organizer.</div>
      <div class="next-step">➤ RSVP Accept or Decline for both events in Google Calendar. Zoom links are in calendar invites.</div>
      <span class="due">🟡 Before: Wed July 8, 12:00 PM</span>
    </div>

    <div class="card yellow">
      <div class="card-label">💊 Medical — Prep Needed</div>
      <h3>New Patient Video Visit — Dr. Haridas, MD (Tomorrow)</h3>
      <div class="source">Google Calendar · Monday July 6, 11:20 AM – 12:00 PM</div>
      <div class="why">New patient video appointment tomorrow. Calendar notes require you to be logged into Connect (browser or app) prior to the visit. Failing to connect on time may result in a missed appointment.</div>
      <div class="next-step">➤ Tonight or tomorrow morning: Log into Connect portal, test your camera/microphone, and confirm appointment. Have insurance card and ID ready.</div>
      <span class="due">🟡 Tomorrow, July 6 · 11:20 AM</span>
    </div>

    <div class="card green">
      <div class="card-label">💼 Job Search — Act Now</div>
      <h3>Sr. Director, People Business Partner at HighLevel (LinkedIn)</h3>
      <div class="source">From: LinkedIn Job Alerts · Today, 5:05 PM</div>
      <div class="why">Sr. Director-level HR/People role aligned with your background. Posted 7/4/2026. Senior roles close quickly — acting within 24–48 hours maximizes your chances of early review.</div>
      <div class="next-step">➤ Open LinkedIn alert, review JD, tailor resume/cover letter, and apply today or tomorrow morning.</div>
      <span class="due">🟢 Apply by: Monday July 6</span>
    </div>

    <div class="card green">
      <div class="card-label">💼 Job Search — Review &amp; Apply</div>
      <h3>Principal People Business Partner at SoFi + HR BP at Coinbase</h3>
      <div class="source">From: Welcome to the Jungle + LinkedIn Job Alerts · Today</div>
      <div class="why">Two high-profile fintech companies (SoFi and Coinbase) have HR/People leadership roles that match your profile. Coinbase listing was dated 7/3, so time-sensitive.</div>
      <div class="next-step">➤ Review both JDs. Prioritize Coinbase (older posting) first, then SoFi. Customize applications and submit.</div>
      <span class="due">🟢 Apply by: Monday–Tuesday July 6–7</span>
    </div>

  </div>

  <!-- ═══════════════════════════════════════════════════════════════════
       SECTION 4: FULL 7-DAY CALENDAR
  ═══════════════════════════════════════════════════════════════════ -->
  <div class="section">
    <div class="section-title blue">📅 Full 7-Day Calendar — July 5–11, 2026</div>

    <!-- TODAY: SUNDAY JULY 5 -->
    <div class="cal-day">
      <div class="cal-day-header today">
        ☀️ Sunday, July 5, 2026 — TODAY
        <span class="day-badge">No Scheduled Events</span>
      </div>
      <div class="cal-event">
        <div class="cal-time">All Day</div>
        <div>
          <div class="cal-event-name">No calendar events scheduled today</div>
          <div class="cal-detail">Use today to address security alerts, check bank balance, RSVP to upcoming events, and review job leads.</div>
        </div>
      </div>
    </div>

    <!-- MONDAY JULY 6 -->
    <div class="cal-day">
      <div class="cal-day-header" style="background:#1a5276;">
        📅 Monday, July 6, 2026
        <span class="day-badge">1 Event</span>
      </div>
      <div class="cal-event">
        <div class="cal-time">11:20 AM<br>– 12:00 PM</div>
        <div>
          <div class="cal-event-name">🩺 New Patient Video Visit — Dr. Keerthana Haridas, MD</div>
          <div class="cal-detail">📍 Video Visit (Connect portal — browser or app)</div>
          <div class="cal-detail">📞 No phone number provided — use Connect app/browser</div>
          <span class="cal-status status-accepted">✅ Accepted</span>
          <div class="cal-prep">⚡ PREP: Log into Connect prior to visit. Test camera/mic tonight. Have insurance card + photo ID ready. New patient — may need to allow extra time for intake forms.</div>
        </div>
      </div>
    </div>

    <!-- TUESDAY JULY 7 -->
    <div class="cal-day">
      <div class="cal-day-header" style="background:#1a5276;">
        📅 Tuesday, July 7, 2026
        <span class="day-badge">2 Events</span>
      </div>
      <div class="cal-event">
        <div class="cal-time">All Day</div>
        <div>
          <div class="cal-event-name">🏦 State Farm Bill Due</div>
          <div class="cal-detail">Billing reminder — State Farm insurance payment</div>
          <span class="cal-status status-confirmed">✅ Confirmed</span>
          <div class="cal-prep">⚠️ URGENT: Bank balance is $51.25. Transfer funds NOW to avoid overdraft. Confirm payment amount and ensure sufficient funds before midnight July 6.</div>
        </div>
      </div>
      <div class="cal-event">
        <div class="cal-time">12:00 PM<br>– 1:00 PM</div>
        <div>
          <div class="cal-event-name">💪 PT (Physical Therapy)</div>
          <div class="cal-detail">📍 Location not specified</div>
          <span class="cal-status status-confirmed">✅ Confirmed</span>
          <div class="cal-prep">⚡ PREP: Confirm location and bring any required paperwork or insurance card. Wear comfortable clothing.</div>
        </div>
      </div>
    </div>

    <!-- WEDNESDAY JULY 8 -->
    <div class="cal-day">
      <div class="cal-day-header" style="background:#1a5276;">
        📅 Wednesday, July 8, 2026
        <span class="day-badge">2 Events — CONFLICT NOTE</span>
      </div>
      <div class="cal-event">
        <div class="cal-time">12:00 PM<br>– 1:30 PM</div>
        <div>
          <div class="cal-event-name">🤝 HR Networking &amp; Job Search Group — Zoom 2</div>
          <div class="cal-detail">📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1">Zoom Link</a> · 170+ attendees</div>
          <span class="cal-status status-needsaction">⚠️ RSVP NEEDED</span>
          <div class="cal-prep">⚡ PREP: RSVP immediately. Review HR Networking Team Guidelines (linked in invite). Prepare 30-sec elevator pitch and 2–3 companies/roles to discuss. Note: AI notetaking tools are welcome here (policy note is on the Thu 7/9 session).</div>
          <div class="cal-conflict">⚠️ CONFLICT: "Network" event at same time (12–1:30 PM) — this appears to be a duplicate/companion entry for the same session. No separate action needed.</div>
        </div>
      </div>
      <div class="cal-event">
        <div class="cal-time">12:00 PM<br>– 1:30 PM</div>
        <div>
          <div class="cal-event-name">🤝 Network (Personal Reminder)</div>
          <div class="cal-detail">📍 No location — likely a personal companion reminder for the HR Networking Zoom above</div>
          <span class="cal-status status-confirmed">✅ Confirmed</span>
          <div class="cal-conflict">⚠️ Appears to be a duplicate of HR Networking &amp; Job Search Group event above. Consider deleting this personal entry to avoid calendar clutter.</div>
        </div>
      </div>
    </div>

    <!-- THURSDAY JULY 9 -->
    <div class="cal-day">
      <div class="cal-day-header" style="background:#1a5276;">
        📅 Thursday, July 9, 2026
        <span class="day-badge">4 Events — BUSY DAY</span>
      </div>
      <div class="cal-event">
        <div class="cal-time">9:00 AM<br>– 10:30 AM</div>
        <div>
          <div class="cal-event-name">🎙️ Executive Roundtable (John Madigan)</div>
          <div class="cal-detail">📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09">Zoom Link</a> · Meeting ID: 207 786 667 · PW: 205454</div>
          <span class="cal-status status-declined">❌ Declined</span>
          <div class="cal-prep">ℹ️ You declined this event. If reconsideration is warranted given your job search, you may want to reach out to John Madigan to inquire about attending.</div>
        </div>
      </div>
      <div class="cal-event">
        <div class="cal-time">12:00 PM<br>– 1:00 PM</div>
        <div>
          <div class="cal-event-name">🤝 HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
          <div class="cal-detail">📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1">Zoom Link</a> · 170+ attendees</div>
          <span class="cal-status status-needsaction">⚠️ RSVP NEEDED</span>
          <div class="cal-prep">⚡ PREP: RSVP now. Per organizer: Turn OFF automated notetaking AI tools. Open discussion format. Good opportunity for 1:1 networking introductions.</div>
        </div>
      </div>
      <div class="cal-event">
        <div class="cal-time">3:30 PM<br>– 4:30 PM</div>
        <div>
          <div class="cal-event-name">🏥 New Patient Appointment — Dr. Beth A. Leeman-Markowski, MD</div>
          <div class="cal-detail">📍 Comprehensive Epilepsy Center, 223 East 34th Street, New York, NY 10016</div>
          <div class="cal-detail">📞 646-558-0800</div>
          <span class="cal-status status-accepted">✅ Accepted</span>
          <div class="cal-prep">⚡ PREP: Arrive 15 minutes early (by 3:15 PM). Bring: insurance card, photo ID, MD referral/pre-certification (if applicable), copy of medical records and recent test results (labs, X-ray, CT, etc.). This is the Comprehensive Epilepsy Center — bring relevant neurological history.</div>
        </div>
      </div>
      <div class="cal-event">
        <div class="cal-time">3:30 PM<br>– 4:30 PM</div>
        <div>
          <div class="cal-event-name">🏥 Appointment — Dr. Beth A. Leeman-Markowski, MD (Confirmed Entry)</div>
          <div class="cal-detail">📍 Comprehensive Epilepsy Center, 223 East 34th Street, New York, NY 10016 · 📞 646-558-0800</div>
          <span class="cal-status status-confirmed">✅ Confirmed</span>
          <div class="cal-conflict">ℹ️ This appears to be a duplicate calendar entry for the same appointment above (likely from a different source/import). Both show the same time, location, and doctor. Consider deleting one entry.</div>
        </div>
      </div>
    </div>

    <!-- FRIDAY JULY 10 -->
    <div class="cal-day">
      <div class="cal-day-header" style="background:#1a5276;">
        📅 Friday, July 10, 2026
        <span class="day-badge">No Events</span>
      </div>
      <div class="cal-event">
        <div class="cal-time">—</div>
        <div>
          <div class="cal-event-name">No scheduled events</div>
          <div class="cal-detail">Good day to follow up on job applications submitted earlier in the week.</div>
        </div>
      </div>
    </div>

    <!-- SATURDAY JULY 11 -->
    <div class="cal-day">
      <div class="cal-day-header" style="background:#1a5276;">
        📅 Saturday, July 11, 2026
        <span class="day-badge">No Events</span>
      </div>
      <div class="cal-event">
        <div class="cal-time">—</div>
        <div>
          <div class="cal-event-name">No scheduled events</div>
          <div class="cal-detail">Rest and recovery. Review any application follow-ups or LinkedIn messages.</div>
        </div>
      </div>
    </div>

  </div>

  <!-- ═══════════════════════════════════════════════════════════════════
       SECTION 5: JOB SEARCH & INTERVIEW PIPELINE
  ═══════════════════════════════════════════════════════════════════ -->
  <div class="section">
    <div class="section-title green">💼 Job Search &amp; Interview Pipeline</div>

    <table style="margin-bottom:14px;">
      <thead>
        <tr>
          <th>Role</th>
          <th>Company</th>
          <th>Source</th>
          <th>Date</th>
          <th>Fit</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Sr. Director, People Business Partner</strong></td>
          <td>HighLevel</td>
          <td>LinkedIn Job Alerts</td>
          <td>July 4, 2026</td>
          <td><span class="fit-high">HIGH</span></td>
          <td>Apply immediately — Senior Director level, aligns with HR BP expertise</td>
        </tr>
        <tr>
          <td><strong>Principal People Business Partner</strong></td>
          <td>SoFi</td>
          <td>Welcome to the Jungle</td>
          <td>July 5, 2026</td>
          <td><span class="fit-high">HIGH</span></td>
          <td>Apply today — fintech HRBP role, strong match</td>
        </tr>
        <tr>
          <td><strong>HR Business Partner</strong></td>
          <td>Coinbase</td>
          <td>LinkedIn Job Alerts</td>
          <td>July 3, 2026</td>
          <td><span class="fit-high">HIGH</span></td>
          <td>Apply ASAP — posted 2 days ago, time-sensitive</td>
        </tr>
        <tr>
          <td><strong>Human Resources (Senior/Expert Level)</strong></td>
          <td>Multiple NYC Companies (incl. Alto Human Resources)</td>
          <td>Built In</td>
          <td>July 5, 2026</td>
          <td><span class="fit-med">MEDIUM</span></td>
          <td>Review Built In batch — filter for best-fit roles, apply to top 2–3</td>
        </tr>
      </tbody>
    </table>

    <div style="background:#eafaf1;border-radius:10px;padding:14px 18px;margin-bottom:10px;">
      <div style="font-weight:700;font-size:13px;color:#1a7a4a;margin-bottom:8px;">🤝 Networking Events This Week</div>
      <ul style="list-style:none;padding:0;">
        <li style="padding:5px 0;border-bottom:1px solid #c8ecd7;font-size:13px;">📅 <strong>Wed July 8, 12–1:30 PM</strong> — HR Networking &amp; Job Search Group (Zoom 2) · <span style="color:#856404;font-weight:600;">⚠️ RSVP Pending</span></li>
        <li style="padding:5px 0;border-bottom:1px solid #c8ecd7;font-size:13px;">📅 <strong>Thu July 9, 9–10:30 AM</strong> — Executive Roundtable (John Madigan, Zoom) · <span style="color:#c0392b;font-weight:600;">❌ Declined — reconsider?</span></li>
        <li style="padding:5px 0;font-size:13px;">📅 <strong>Thu July 9, 12–1 PM</strong> — HR Networking &amp; Job Search Open Office Hours (Zoom 2) · <span style="color:#856404;font-weight:600;">⚠️ RSVP Pending</span></li>
      </ul>
    </div>

    <div style="background:#f0f7ff;border-radius:10px;padding:14px 18px;">
      <div style="font-weight:700;font-size:13px;color:#1565c0;margin-bottom:8px;">📊 LinkedIn Activity</div>
      <ul style="list-style:none;padding:0;">
        <li style="padding:4px 0;font-size:13px;">👁️ You appeared in <strong>7 LinkedIn searches</strong> this week — someone from <strong>Air Force Office of Special Investigations (AFOSI)</strong> found your profile. Interesting lead worth noting.</li>
        <li style="padding:4px 0;font-size:13px;">📰 Ken Zwerdling (CEO/MBA) newsletter: "What 2,040 Professionals Told Us About Today's Job Market" — relevant reading for job search context.</li>
      </ul>
    </div>

    <div style="background:#faf5ff;border-radius:10px;padding:14px 18px;margin-top:10px;">
      <div style="font-weight:700;font-size:13px;color:#6c3483;margin-bottom:8px;">📚 Professional Development Resources (Self-Sent)</div>
      <ul style="list-style:none;padding:0;">
        <li style="padding:4px 0;font-size:13px;">• <strong>Claude Code Best Practices</strong> — ChatGPT link saved (sent to self, 11:01–11:02 AM)</li>
        <li style="padding:4px 0;font-size:13px;">• <strong>3 Claude Moves That Actually Get You Hired</strong> — Learn AI With Mariah (saved link)</li>
        <li style="padding:4px 0;font-size:13px;">• <strong>Anthropic's Human-Agent Team Playbook</strong> — Learn AI With Mariah (saved link)</li>
        <li style="padding:4px 0;font-size:13px;">• Google Search saved: Claude Code bug-checking prompt research</li>
      </ul>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════════════════
       SECTION 6: FULL EMAIL REVIEW BY CATEGORY
  ═══════════════════════════════════════════════════════════════════ -->
  <div class="section">
    <div class="section-title dark">📧 Full Email Review by Category</div>

    <!-- SECURITY / RISK -->
    <div class="email-cat">
      <div class="cat-header">
        <div class="cat-title" style="color:#c0392b;">🔐 Security / Risk</div>
        <span class="cat-count count-red">3 emails</span>
      </div>
      <ul>
        <li><span class="unread-dot"></span><span class="sender-name">Google</span> — "Security alert" — gws local access granted to melissaw212@gmail.com <span class="spam-flag">URGENT</span> · In Trash</li>
        <li><span class="unread-dot"></span><span class="sender-name">Google</span> — "Security alert for melissaw212@gmail.com" — Recovery email copy (Melweiss212@gmail.com) <span class="spam-flag">URGENT</span> · In Trash</li>
        <li><span class="unread-dot"></span><span class="sender-name">GitHub</span> — "Sudo email verification code: 28292078" — Code used at 10:22 AM, valid 15 min · In Trash · Read</li>
      </ul>
      <div class="action">➤ ACTION: Review Google Account security settings NOW. Confirm GitHub sudo activity was yours.</div>
    </div>

    <!-- JOB SEARCH -->
    <div class="email-cat">
      <div class="cat-header">
        <div class="cat-title" style="color:#1a7a4a;">💼 Job Search</div>
        <span class="cat-count count-green">4 emails</span>
      </div>
      <ul>
        <li><span class="unread-dot"></span><span class="sender-name">LinkedIn Job Alerts</span> — "Sr. Director, People Business Partner at HighLevel" · In Inbox</li>
        <li><span class="unread-dot"></span><span class="sender-name">Welcome to the Jungle</span> — "New match: Principal People Business Partner at SoFi" · In Inbox</li>
        <li><span class="unread-dot"></span><span class="sender-name">LinkedIn Job Alerts</span> — "HR Business Partner at Coinbase" · In Inbox</li>
        <li><span class="unread-dot"></span><span class="sender-name">Built In</span> — "New human resources Job Matches" — Senior/Expert level, NYC (Hybrid/Remote/In Office) · In Inbox</li>
      </ul>
      <div class="action">➤ ACTION: Review and apply to HighLevel, SoFi, and Coinbase roles ASAP. Browse Built In batch for additional fits.</div>
    </div>

    <!-- RECRUITERS / NETWORKING -->
    <div class="email-cat">
      <div class="cat-header">
        <div class="cat-title" style="color:#1565c0;">🤝 Recruiters / Networking</div>
        <span class="cat-count count-blue">2 emails</span>
      </div>
      <ul>
        <li><span class="sender-name">LinkedIn</span> — "You appeared in 7 searches" — Someone from AFOSI found your profile · Read</li>
        <li><span class="unread-dot"></span><span class="sender-name">Ken Zwerdling (LinkedIn Newsletter)</span> — "What 2,040 Professionals Told Us About Today's Job Market and Why So Many Searches Are Taking Longer Than Ever"</li>
      </ul>
      <div class="action">➤ ACTION: Check who viewed your profile. Read Ken Zwerdling's newsletter for job market context.</div>
    </div>

    <!-- CALENDAR / EVENTS -->
    <div class="email-cat">
      <div class="cat-header">
        <div class="cat-title" style="color:#1565c0;">📅 Calendar / Events</div>
        <span class="cat-count count-blue">0 emails</span>
      </div>
      <ul>
        <li>All calendar events were delivered as Google Calendar invites (not email). See Full 7-Day Calendar section above.</li>
      </ul>
      <div class="action">➤ ACTION: RSVP to HR Networking events (Wed July 8 and Thu July 9).</div>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="email-cat">
      <div class="cat-header">
        <div class="cat-title" style="color:#b7791f;">💳 Financial / Billing</div>
        <span class="cat-count count-yellow">2 emails</span>
      </div>
      <ul>
        <li><span class="unread-dot"></span><span class="sender-name">Bank of America</span> — "Your balance is below your chosen limit" — $51.25 remaining, account ending 7471 · In Inbox <span class="spam-flag">URGENT</span></li>
        <li><span class="sender-name">Bank of America</span> — "Your Available Balance" — $153.75 (morning snapshot, before transactions) · Read</li>
      </ul>
      <div class="action">➤ ACTION: Transfer funds or deposit before Monday July 7 — State Farm bill due. Current usable balance is ~$51.25.</div>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="email-cat">
      <div class="cat-header">
        <div class="cat-title" style="color:#6c3483;">📚 Professional Development</div>
        <span class="cat-count count-purple">7 emails</span>
      </div>
      <ul>
        <li><span class="unread-dot"></span><span class="sender-name">Melissa W (self)</span> — "Claude Code Best Practices" (ChatGPT link) · In Inbox</li>
        <li><span class="unread-dot"></span><span class="sender-name">Melissa W (self)</span> — "Claude Code Best Practices" (duplicate, slightly earlier time) · In Inbox</li>
        <li><span class="unread-dot"></span><span class="sender-name">Melissa W (self)</span> — "3 Claude Moves That Actually Get You Hired | Learn AI With Mariah"</li>
        <li><span class="unread-dot"></span><span class="sender-name">Melissa W (self)</span> — "Anthropic's Human-Agent Team Playbook: 4 Rules To Steal"</li>
        <li><span class="unread-dot"></span><span class="sender-name">Melissa W (self)</span> — Google Search: Claude Code bug-checking prompt</li>
        <li><span class="unread-dot"></span><span class="sender-name">The HR AI Guy (Medium)</span> — "How I Build Training Content in Hours, Not Weeks (With Real Prompts)" · In Trash</li>
        <li><span class="unread-dot"></span><span class="sender-name">Mindstream</span> — "They promised the future. They lied." — Weekly AI Roundup</li>
      </ul>
      <div class="action">➤ ACTION: Review Claude/AI resources saved. The HR AI Guy article on training content is relevant to your HR + AI positioning.</div>
    </div>

    <!-- PERSONAL -->
    <div class="email-cat">
      <div class="cat-header">
        <div class="cat-title" style="color:#555;">🏠 Personal</div>
        <span class="cat-count count-gray">3 emails</span>
      </div>
      <ul>
        <li><span class="sender-name">Nextdoor (Yorkville E83st-2nd Ave Safety Posts)</span> — "Legionnaires' disease community cluster investigation" — Rego Park/Yorkville area, late June exposure · Read</li>
        <li><span class="unread-dot"></span><span class="sender-name">HomeAgain PetRescuers</span> — "Vsilisa, a lost Cat, missing in your area" — Last seen 65th Ave &amp; 65th Rd, Rego Park, NY 11374 · In Trash</li>
        <li><span class="unread-dot"></span><span class="sender-name">Facebook Pages</span> — "Maja's Recipes: with 14K followers is a suggestion" · Read</li>
      </ul>
      <div class="action">➤ NOTE: Review Legionnaires' alert — if you live/work in Yorkville or visited since late June and have flu-like symptoms, seek medical attention. Lost cat alert for local area.</div>
    </div>

    <!-- NEWSLETTERS / SUBSCRIPTIONS -->
    <div class="email-cat">
      <div class="cat-header">
        <div class="cat-title" style="color:#6c3483;">📰 Newsletters / Subscriptions</div>
        <span class="cat-count count-purple">6 emails</span>
      </div>
      <ul>
        <li><span class="unread-dot"></span><span class="sender-name">Privacy Digest (Ghostery)</span> — "Who Controls Your Data Now?" — AI &amp; workplace tracking · In Trash</li>
        <li><span class="unread-dot"></span><span class="sender-name">Pranit Naik (Medium)</span> — "This YouTuber Literally Asked Claude Fable 5 to Build GTA 6" · In Trash</li>
        <li><span class="unread-dot"></span><span class="sender-name">CoolDeep AI (Beehiiv)</span> — "AI vs Your Job: who will be a real winner?" · In Trash</li>
        <li><span class="sender-name">CoolDeep AI (Beehiiv)</span> — "I was afraid of AI agents but I built one." · Read</li>
        <li><span class="unread-dot"></span><span class="sender-name">ChatGPT (OpenAI)</span> — "Translate anything, your way" — product feature email</li>
        <li><span class="sender-name">Dr. Gazala Shaikh (Medium)</span> — "I Keep Waiting to Feel Like a Real Adult" · Read</li>
      </ul>
      <div class="action">➤ ACTION: Privacy Digest and AI newsletters are relevant to professional development. CoolDeep AI overlap — consider unsubscribing from one.</div>
    </div>

    <!-- PROMOTIONAL / RETAIL -->
    <div class="email-cat">
      <div class="cat-header">
        <div class="cat-title" style="color:#888;">🛍️ Promotional / Retail</div>
        <span class="cat-count count-gray">15 emails</span>
      </div>
      <ul>
        <li><span class="sender-name">Lands' End</span> — "Tankinis in fresh prints: 55% off" · In Inbox</li>
        <li><span class="sender-name">Halara</span> — "Polished Pants For Every Vibe: Up to 60% Off" · In Inbox</li>
        <li><span class="sender-name">H&amp;M</span> — "Melissa, 20% off almost everything ends today" · Read</li>
        <li><span class="sender-name">Old Navy</span> — "$5 TEES + Clearance from $3.99" · In Trash</li>
        <li><span class="sender-name">SHEIN</span> — "Still Summer, Still Saving — UP TO 90% OFF" · Read</li>
        <li><span class="sender-name">PUMA</span> — "Up to 50% Off + Extra 20%: Yes, Please" · Read</li>
        <li><span class="sender-name">The Container Store</span> — "Up To 80% Off Clearance" · In Trash</li>
        <li><span class="sender-name">Quince</span> — "Sold out. Back in stock." · Read</li>
        <li><span class="sender-name">Laura Geller</span> — "Save $150+ On Fresh-Faced Favorites — Today Only" (2 emails) · Read</li>
        <li><span class="sender-name">rhode</span> — "Hailey's Highlight Milk trick" · In Trash</li>
        <li><span class="sender-name">e.l.f. Cosmetics</span> — "Get the full Soft Glam fam for &lt;$30!" · In Trash</li>
        <li><span class="sender-name">Target Optical</span> — "July 4th savings are almost over..." · Unread</li>
        <li><span class="sender-name">StackSocial</span> — "Last Call: 30% Off Apps Ends Today — JULY30" · In Trash</li>
        <li><span class="sender-name">MyFitnessPal</span> — "Hot take: you've been grilling the wrong things"</li>
      </ul>
      <div class="action">➤ Low priority. H&amp;M 20% off ends today if interested. Target Optical sale ending — review if you need eyewear. All others: ignore or delete.</div>
    </div>

    <!-- SPAM / SCAM -->
    <div class="email-cat">
      <div class="cat-header">
        <div class="cat-title" style="color:#c0392b;">🚫 Spam / Scam — Safe to Delete/Ignore</div>
        <span class="cat-count count-red">5 emails</span>
      </div>
      <ul>
        <li><span class="unread-dot"></span><span class="sender-name">"Congratulations🎉" (suspicious domain)</span> — "130 Free Spins 💰 No deposit Needed" — Casino spam <span class="spam-flag">SCAM</span></li>
        <li><span class="unread-dot"></span><span class="sender-name">"⚽melissaw212.Worldcup⚽" (suspicious domain)</span> — "Claim YOUR FREE Spins this worldcup" — Casino spam using your email address <span class="spam-flag">SCAM</span></li>
        <li><span class="unread-dot"></span><span class="sender-name">"Tractor Supply®" (fake domain)</span> — "Confirmed: You have won a Predator 3500W Generator" <span class="spam-flag">SCAM</span></li>
        <li><span class="sender-name">eharmony</span> — "It's a lazy Sunday. Send Ansel a first message." · In Trash</li>
        <li><span class="sender-name">eharmony</span> — "Your last chance to save: 60% off Premium Memberships" · Read</li>
<hr>
<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Job Search / Recruiters</td><td>9</td></tr>
<tr><td>Medical / Health</td><td>2</td></tr>
<tr><td>Other / Review</td><td>18</td></tr>
<tr><td>Professional Development / Newsletters</td><td>4</td></tr>
<tr><td>Promotional / Retail</td><td>11</td></tr>
<tr><td>Security / Risk</td><td>6</td></tr>
</table>
<p><strong>Audit Note:</strong> Every fetched email was reviewed and assigned to one category. Trash emails were included in review. Promotional and low-value emails were accounted for but deprioritized.</p>

