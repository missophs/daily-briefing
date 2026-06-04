<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Melissa's Executive Briefing — Thursday, June 4, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; }
  .page { max-width: 1100px; margin: 0 auto; padding: 20px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); color: white; padding: 32px 36px; border-radius: 16px; margin-bottom: 24px; box-shadow: 0 8px 32px rgba(0,0,0,0.3); }
  .header h1 { font-size: 28px; font-weight: 300; letter-spacing: 1px; }
  .header h1 span { font-weight: 700; color: #e94560; }
  .header .subtitle { font-size: 13px; color: #a8b2d8; margin-top: 4px; letter-spacing: 2px; text-transform: uppercase; }
  .header-stats { display: flex; gap: 24px; margin-top: 20px; flex-wrap: wrap; }
  .stat-pill { background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); border-radius: 20px; padding: 6px 16px; font-size: 12px; color: #e2e8f0; }
  .stat-pill span { font-weight: 700; color: #fff; }

  /* SECTION HEADERS */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 11px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: #64748b; margin-bottom: 12px; padding-left: 4px; border-left: 3px solid #e94560; padding-left: 10px; }

  /* EXECUTIVE SUMMARY */
  .exec-summary { background: white; border-radius: 12px; padding: 24px; box-shadow: 0 2px 12px rgba(0,0,0,0.08); }
  .exec-bullet { display: flex; align-items: flex-start; gap: 12px; padding: 10px 0; border-bottom: 1px solid #f1f5f9; }
  .exec-bullet:last-child { border-bottom: none; }
  .exec-icon { width: 32px; height: 32px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 16px; flex-shrink: 0; }
  .icon-red { background: #fee2e2; }
  .icon-green { background: #dcfce7; }
  .icon-blue { background: #dbeafe; }
  .exec-bullet-text strong { font-size: 13px; display: block; margin-bottom: 2px; }
  .exec-bullet-text p { font-size: 12px; color: #64748b; }

  /* COLOR CARDS */
  .card { border-radius: 12px; padding: 18px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .card-red { background: #fff5f5; border-left: 4px solid #ef4444; }
  .card-yellow { background: #fffbeb; border-left: 4px solid #f59e0b; }
  .card-blue { background: #eff6ff; border-left: 4px solid #3b82f6; }
  .card-green { background: #f0fdf4; border-left: 4px solid #22c55e; }
  .card-purple { background: #faf5ff; border-left: 4px solid #a855f7; }
  .card-gray { background: #f8fafc; border-left: 4px solid #94a3b8; }

  .card-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px; }
  .card-label { font-size: 10px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; padding: 2px 8px; border-radius: 4px; }
  .label-red { background: #fee2e2; color: #dc2626; }
  .label-yellow { background: #fef3c7; color: #d97706; }
  .label-blue { background: #dbeafe; color: #2563eb; }
  .label-green { background: #dcfce7; color: #16a34a; }
  .label-purple { background: #ede9fe; color: #7c3aed; }
  .label-gray { background: #f1f5f9; color: #64748b; }

  .card h3 { font-size: 14px; font-weight: 600; margin-bottom: 4px; }
  .card .source { font-size: 11px; color: #94a3b8; margin-bottom: 8px; }
  .card p { font-size: 12px; color: #475569; line-height: 1.5; }
  .card .action { margin-top: 8px; padding: 6px 10px; background: rgba(0,0,0,0.05); border-radius: 6px; font-size: 11px; font-weight: 600; color: #1e293b; }
  .card .due { font-size: 10px; color: #94a3b8; margin-top: 4px; }

  /* BADGE */
  .badge { display: inline-block; padding: 2px 8px; border-radius: 10px; font-size: 10px; font-weight: 700; }
  .badge-high { background: #fee2e2; color: #dc2626; }
  .badge-medium { background: #fef3c7; color: #d97706; }
  .badge-low { background: #f1f5f9; color: #64748b; }
  .badge-confirmed { background: #dcfce7; color: #16a34a; }
  .badge-declined { background: #fee2e2; color: #dc2626; }
  .badge-pending { background: #fef3c7; color: #d97706; }
  .badge-accepted { background: #dbeafe; color: #2563eb; }

  /* CALENDAR */
  .cal-day { background: white; border-radius: 12px; padding: 16px 20px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .cal-day-header { font-size: 13px; font-weight: 700; color: #1e293b; margin-bottom: 12px; padding-bottom: 8px; border-bottom: 2px solid #f1f5f9; display: flex; align-items: center; gap: 8px; }
  .today-badge { background: #e94560; color: white; font-size: 10px; padding: 2px 8px; border-radius: 10px; }
  .cal-event { display: grid; grid-template-columns: 100px 1fr auto; gap: 12px; padding: 8px 0; border-bottom: 1px solid #f8fafc; align-items: start; }
  .cal-event:last-child { border-bottom: none; }
  .cal-time { font-size: 11px; font-weight: 600; color: #64748b; }
  .cal-info h4 { font-size: 13px; font-weight: 600; margin-bottom: 2px; }
  .cal-info p { font-size: 11px; color: #94a3b8; }
  .cal-info .cal-prep { font-size: 11px; color: #7c3aed; margin-top: 3px; }
  .cal-info .cal-conflict { font-size: 11px; color: #dc2626; margin-top: 3px; font-weight: 600; }
  .cal-info a { font-size: 11px; color: #3b82f6; word-break: break-all; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 12px; }
  th { background: #1a1a2e; color: white; padding: 10px 12px; text-align: left; font-size: 11px; letter-spacing: 1px; text-transform: uppercase; }
  td { padding: 9px 12px; border-bottom: 1px solid #f1f5f9; vertical-align: top; }
  tr:nth-child(even) td { background: #f8fafc; }
  tr:hover td { background: #f1f5f9; }
  .table-wrap { background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); margin-bottom: 12px; overflow-x: auto; }

  /* CATEGORY BLOCKS */
  .cat-block { background: white; border-radius: 12px; padding: 16px 20px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .cat-block h3 { font-size: 13px; font-weight: 700; margin-bottom: 6px; display: flex; align-items: center; gap: 8px; }
  .count-badge { background: #e2e8f0; color: #475569; font-size: 11px; padding: 2px 8px; border-radius: 10px; font-weight: 700; }
  .cat-block p { font-size: 12px; color: #64748b; line-height: 1.6; }
  .cat-block .senders { font-size: 11px; color: #94a3b8; margin: 4px 0; }
  .cat-block .rec { font-size: 11px; font-weight: 600; margin-top: 6px; padding: 4px 8px; border-radius: 6px; display: inline-block; }
  .rec-action { background: #fee2e2; color: #dc2626; }
  .rec-review { background: #fef3c7; color: #d97706; }
  .rec-delete { background: #f1f5f9; color: #64748b; }
  .rec-keep { background: #dcfce7; color: #16a34a; }

  /* DASHBOARD */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }
  .dash-card { background: white; border-radius: 12px; padding: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .dash-card .dash-label { font-size: 10px; letter-spacing: 2px; text-transform: uppercase; color: #94a3b8; margin-bottom: 6px; }
  .dash-card .dash-value { font-size: 22px; font-weight: 700; color: #1a1a2e; }
  .dash-card .dash-sub { font-size: 11px; color: #64748b; margin-top: 4px; }
  .dash-card.dash-red { border-top: 3px solid #ef4444; }
  .dash-card.dash-yellow { border-top: 3px solid #f59e0b; }
  .dash-card.dash-green { border-top: 3px solid #22c55e; }
  .dash-card.dash-blue { border-top: 3px solid #3b82f6; }
  .dash-card.dash-purple { border-top: 3px solid #a855f7; }
  .dash-card.dash-gray { border-top: 3px solid #94a3b8; }

  /* PRIORITIES */
  .priority-block { background: white; border-radius: 12px; padding: 20px 24px; box-shadow: 0 2px 12px rgba(0,0,0,0.08); }
  .priority-item { display: flex; gap: 16px; align-items: flex-start; padding: 14px 0; border-bottom: 1px solid #f1f5f9; }
  .priority-item:last-child { border-bottom: none; }
  .priority-num { width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 800; flex-shrink: 0; }
  .p1 { background: #fee2e2; color: #dc2626; }
  .p2 { background: #fef3c7; color: #d97706; }
  .p3 { background: #dbeafe; color: #2563eb; }
  .priority-text h4 { font-size: 14px; font-weight: 600; margin-bottom: 3px; }
  .priority-text p { font-size: 12px; color: #64748b; }

  /* FOOTER */
  .footer { text-align: center; padding: 20px; color: #94a3b8; font-size: 11px; margin-top: 10px; }

  /* GRID 2COL */
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
  @media (max-width: 700px) { .grid-2 { grid-template-columns: 1fr; } .cal-event { grid-template-columns: 80px 1fr; } }

  .divider { height: 1px; background: #e2e8f0; margin: 20px 0; }
  .emoji { margin-right: 4px; }

  /* TRASH GROUPS */
  .trash-group { background: white; border-radius: 12px; padding: 16px 20px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .trash-group h3 { font-size: 13px; font-weight: 700; margin-bottom: 8px; padding: 4px 10px; border-radius: 6px; display: inline-block; }
  .trash-restore { color: #16a34a; background: #dcfce7; }
  .trash-review { color: #d97706; background: #fef3c7; }
  .trash-delete { color: #64748b; background: #f1f5f9; }
  .trash-item { font-size: 12px; padding: 4px 0; border-bottom: 1px solid #f8fafc; color: #475569; }
  .trash-item:last-child { border-bottom: none; }
  .trash-item strong { color: #1e293b; }

  .total-row td { font-weight: 700; background: #1a1a2e !important; color: white; }
</style>
</head>
<body>
<div class="page">

<!-- ════════════════════════════════════════════════════════
     SECTION 1 · HEADER
════════════════════════════════════════════════════════ -->
<div class="header">
  <div class="subtitle">Executive Chief of Staff Briefing &nbsp;·&nbsp; Prepared Fresh</div>
  <h1>Good Morning, <span>Melissa</span> ☀️</h1>
  <div class="header-stats">
    <div class="stat-pill">📅 <span>Thursday, June 4, 2026</span></div>
    <div class="stat-pill">📧 Emails Reviewed: <span>50</span></div>
    <div class="stat-pill">📥 In Inbox: <span>8</span></div>
    <div class="stat-pill">🗑️ In Trash: <span>38</span></div>
    <div class="stat-pill">📆 Calendar Events: <span>10</span></div>
    <div class="stat-pill">⚠️ Action Required: <span>7 items</span></div>
  </div>
</div>

<!-- ════════════════════════════════════════════════════════
     SECTION 2 · EXECUTIVE SUMMARY
════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">Executive Summary</div>
  <div class="exec-summary">
    <div class="exec-bullet">
      <div class="exec-icon icon-red">🚨</div>
      <div class="exec-bullet-text">
        <strong>Biggest Risk: Phishing Scam + Dayforce Rejection in Trash</strong>
        <p>A confirmed phishing email ("Final Notice — Claim Your Funds") landed in trash from a suspicious .lt domain. Also in trash: a Dayforce rejection for the Senior HRBP role — confirm if intentional and log it in your pipeline. Review both before permanent deletion.</p>
      </div>
    </div>
    <div class="exec-bullet">
      <div class="exec-icon icon-green">💼</div>
      <div class="exec-bullet-text">
        <strong>Biggest Opportunity: 16 New Qualifying VP+ HR Roles (Today's PM Sweep)</strong>
        <p>Your Apify-sourced job sweep surfaced 16 qualifying roles (14 direct hire, 2 staffing) across 33 boards in the 72-hour window June 1–4. LinkedIn also sent 4 alerts for CHRO at Nsight Health ($215K–$255K). Glassdoor flagged HR Director at Corporate Castle + 10 more. This requires same-day review.</p>
      </div>
    </div>
    <div class="exec-bullet">
      <div class="exec-icon icon-blue">📆</div>
      <div class="exec-bullet-text">
        <strong>Biggest Calendar Item: HR Networking Open Office Hours at Noon + RSVP Needed</strong>
        <p>Today at 12:00 PM ET — HR Networking &amp; Job Search Open Office Hours (Zoom, 200+ attendees). Status is "needsAction" — you have not yet RSVP'd. Also: your 15-min Netta Jenkins consultation on June 9 is confirmed. Jackie's birthday is June 6 — gift/message needed. State Farm bill due June 7.</p>
      </div>
    </div>
  </div>
</div>

<!-- ════════════════════════════════════════════════════════
     SECTION 3 · ACTION REQUIRED
════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">⚡ Action Required</div>

  <div class="card card-green">
    <div class="card-header">
      <span class="card-label label-green">🟢 JOB SEARCH — URGENT</span>
    </div>
    <h3>Review Today's VP+ HR Job Sweep — 16 Qualifying Roles</h3>
    <div class="source">From: melissa &lt;melissaw212@gmail.com&gt; · Thu Jun 4, 2026 · 📥 In Inbox</div>
    <p>Your Apify-sourced PM sweep returned 16 qualifying VP+ HR roles (14 direct hire, 2 staffing) across 33 boards in the June 1–4 window. This is 4 more than yesterday's sweep of 12. High-velocity moment — act today before roles close.</p>
    <div class="action">➡ Open the sweep email, triage all 16 roles, and apply or queue the top 5 today.</div>
    <div class="due">Due: Today, June 4, 2026</div>
  </div>

  <div class="card card-green">
    <div class="card-header">
      <span class="card-label label-green">🟢 JOB SEARCH — HIGH PRIORITY</span>
    </div>
    <h3>CHRO at Nsight Health — Up to $255K/Year (LinkedIn Alert × 4)</h3>
    <div class="source">From: LinkedIn Job Alerts · Multiple sends (3:05 AM, 7:06 AM, 9:05 AM, 11:05 AM) · 📥 In Inbox</div>
    <p>LinkedIn sent this alert 4 times throughout the morning — $215K–$255K/year salary range. The repeated alerts suggest strong algorithmic match. Don't let this slip through the cracks amid duplicate noise.</p>
    <div class="action">➡ Open the LinkedIn listing, assess fit, and apply or add to tracker today.</div>
    <div class="due">Due: Today — roles at this level fill fast</div>
  </div>

  <div class="card card-green">
    <div class="card-header">
      <span class="card-label label-green">🟢 JOB SEARCH</span>
    </div>
    <h3>Glassdoor: HR Director at Corporate Castle + 10 More Remote Roles</h3>
    <div class="source">From: Glassdoor Jobs · Thu Jun 4, 2026 · 📥 In Inbox</div>
    <p>Progressive Insurance is among the hiring companies. 10+ remote HR roles in a single alert. Requires triage to identify VP+ or Director-level fits.</p>
    <div class="action">➡ Open Glassdoor alert, filter for VP/Director/CHRO level, apply to top 2–3 today.</div>
    <div class="due">Due: Today</div>
  </div>

  <div class="card card-blue">
    <div class="card-header">
      <span class="card-label label-blue">🔵 CALENDAR — RSVP NEEDED</span>
    </div>
    <h3>HR Networking Open Office Hours — RSVP Pending (Noon Today)</h3>
    <div class="source">Calendar: HR Networking &amp; Job Search: Open Office Hours - Zoom 2 · 12:00–1:00 PM ET</div>
    <p>This 200+ attendee Zoom networking session starts at noon today. Your status is "needsAction." Given your active job search, this is a high-value touchpoint. Note: organizer asks that automated AI notetaking tools be turned off.</p>
    <div class="action">➡ RSVP and join at noon. No AI notetakers. Bring your 30-second intro and open questions.</div>
    <div class="due">Due: 12:00 PM ET TODAY</div>
  </div>

  <div class="card card-yellow">
    <div class="card-header">
      <span class="card-label label-yellow">🟡 BILLING — REVIEW</span>
    </div>
    <h3>UnitedHealthcare: New Explanation of Benefits Available</h3>
    <div class="source">From: UnitedHealthcare Notifications · Thu Jun 4, 2026 · 📥 In Inbox</div>
    <p>A new EOB is available online. Review to confirm benefits were applied correctly, especially if you had any recent claims or procedures (eye appointment June 8 is upcoming).</p>
    <div class="action">➡ Log in to UHC portal and review the EOB. File or note any discrepancies.</div>
    <div class="due">Due: This week</div>
  </div>

  <div class="card card-yellow">
    <div class="card-header">
      <span class="card-label label-yellow">🟡 FINANCIAL — REVIEW</span>
    </div>
    <h3>Merrill Edge: New Trade Confirmation</h3>
    <div class="source">From: Merrill Edge · Thu Jun 4, 2026 · 📥 In Trash (possible misfile)</div>
    <p>A trade confirmation was issued today. This ended up in Trash — verify it was auto-filed or if it needs your review and acknowledgment. Financial transactions should not be ignored.</p>
    <div class="action">➡ Log in to Merrill Edge and review the trade confirmation for accuracy.</div>
    <div class="due">Due: Today</div>
  </div>

  <div class="card card-yellow">
    <div class="card-header">
      <span class="card-label label-yellow">🟡 DEADLINE — UPCOMING</span>
    </div>
    <h3>State Farm Bill Due June 7 + Jackie's Birthday June 6</h3>
    <div class="source">Calendar: "State farm bill" · June 7 &nbsp;|&nbsp; "Jackie bday" · June 6</div>
    <p>State Farm payment is due Sunday June 7. Jackie's birthday is Saturday June 6 — only 2 days away. Plan ahead if a gift, card, or message is needed.</p>
    <div class="action">➡ Schedule State Farm payment. Send birthday message or gift to Jackie by Saturday.</div>
    <div class="due">Due: June 6 (Jackie) · June 7 (State Farm)</div>
  </div>

</div>

<!-- ════════════════════════════════════════════════════════
     SECTION 4 · FULL 7-DAY CALENDAR
════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📅 Full 7-Day Calendar — June 4–10, 2026</div>

  <!-- Thursday June 4 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Thursday, June 4, 2026 <span class="today-badge">TODAY</span></div>

    <div class="cal-event">
      <div class="cal-time">9:00–10:30 AM</div>
      <div class="cal-info">
        <h4>Executive Roundtable</h4>
        <p>Hosted by John Madigan via Zoom</p>
        <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Join Zoom · ID: 207 786 667 · PW: 205454</a>
        <p class="cal-prep">Prep: No prep needed — you declined this event.</p>
      </div>
      <div><span class="badge badge-declined">DECLINED</span></div>
    </div>

    <div class="cal-event">
      <div class="cal-time">10:30–11:30 AM</div>
      <div class="cal-info">
        <h4>Dr Husk</h4>
        <p>No location provided</p>
        <p class="cal-prep">⚠️ Prep: Confirm appointment details/location. No address on file.</p>
      </div>
      <div><span class="badge badge-confirmed">CONFIRMED</span></div>
    </div>

    <div class="cal-event">
      <div class="cal-time">12:00–1:00 PM</div>
      <div class="cal-info">
        <h4>HR Networking &amp; Job Search: Open Office Hours — Zoom 2</h4>
        <p>~200+ attendees · Group networking session</p>
        <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Join Zoom Link</a>
        <p class="cal-prep">🔔 RSVP NEEDED · No AI notetakers. Prep your 30-sec intro &amp; questions.</p>
        <p class="cal-conflict">⚠️ Conflict: Follows Dr Husk — allow travel/wrap-up time.</p>
      </div>
      <div><span class="badge badge-pending">RSVP NEEDED</span></div>
    </div>
  </div>

  <!-- Friday June 5 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Friday, June 5, 2026</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-info">
        <h4>No events scheduled</h4>
        <p>Clear day — good for job applications, follow-ups, and prep.</p>
        <p class="cal-prep">💡 Suggested: Apply to top roles from today's job sweep.</p>
      </div>
      <div></div>
    </div>
  </div>

  <!-- Saturday June 6 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Saturday, June 6, 2026</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-info">
        <h4>🎂 Jackie's Birthday</h4>
        <p>All-day reminder</p>
        <p class="cal-prep">🎁 Action: Send gift, card, or birthday message today!</p>
      </div>
      <div><span class="badge badge-confirmed">CONFIRMED</span></div>
    </div>
  </div>

  <!-- Sunday June 7 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Sunday, June 7, 2026</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-info">
        <h4>💳 State Farm Bill Due</h4>
        <p>Payment deadline reminder</p>
        <p class="cal-prep">⚠️ Action: Schedule or confirm payment before Sunday to avoid late fee.</p>
      </div>
      <div><span class="badge badge-confirmed">CONFIRMED</span></div>
    </div>
  </div>

  <!-- Monday June 8 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Monday, June 8, 2026</div>
    <div class="cal-event">
      <div class="cal-time">9:00–10:00 AM</div>
      <div class="cal-info">
        <h4>Eye (Appointment)</h4>
        <p>No location provided — confirm address/provider</p>
        <p class="cal-prep">⚠️ Prep: Confirm location and provider. Bring insurance card (UHC EOB just arrived). Allow travel time.</p>
      </div>
      <div><span class="badge badge-confirmed">CONFIRMED</span></div>
    </div>
  </div>

  <!-- Tuesday June 9 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Tuesday, June 9, 2026</div>
    <div class="cal-event">
      <div class="cal
<hr>
<h2>Trash Review</h2>
<p><strong>Purpose:</strong> Review deleted emails for anything important before permanent deletion. Anything from job search, billing, medical, calendar, security, legal, GitHub, Netlify, LinkedIn, recruiters, or professional contacts should be reviewed before deleting.</p>

<h2>Promotional / Retail Summary</h2>
<p><strong>Purpose:</strong> Promotional emails are included in the full email inventory below. Delete or ignore retail/promotional items unless there is a deal you actually plan to use or a sender looks suspicious.</p>

<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Financial / Billing</td><td>3</td></tr>
<tr><td>Job Search / Recruiters</td><td>15</td></tr>
<tr><td>Medical / Health</td><td>1</td></tr>
<tr><td>Other / Review</td><td>22</td></tr>
<tr><td>Professional Development / Newsletters</td><td>2</td></tr>
<tr><td>Promotional / Retail</td><td>4</td></tr>
<tr><td>Security / Risk</td><td>3</td></tr>
</table>

<h2>Full Email Inventory</h2>
<p><strong>Every fetched email is listed below.</strong> Use this section to see what to act on, review, delete, or ignore.</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr>
  <th>#</th>
  <th>Category</th>
  <th>From</th>
  <th>Subject</th>
  <th>Date</th>
  <th>Labels</th>
  <th>Snippet</th>
  <th>Recommendation</th>
</tr>

<div style="background:#fffbf0; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Financial / Billing (3)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#8 · Thu, 4 Jun 2026 12:03:22 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">[Netlify] You&#x27;ve used 50% of your credits on morning briefing</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Netlify &lt;team@netlify.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">You&amp;#39;re using your credits! Your credit usage on team morning briefing has reached 50% of your 1000 credit allowance in the current billing cycle f</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#23 · Thu, 04 Jun 2026 10:54:35 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Nvidia Pays Your Bill, Congress Rebukes Trump, and Anthony Bourdain on Risk</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;1% Better&quot; &lt;hello@onepercentimprovements.convertkit.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">You improve every day. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#45 · Thu, 4 Jun 2026 02:22:34 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Your receipt from Anthropic, PBC #2036-5009-8840</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Anthropic, PBC&quot; &lt;invoice+statements@mail.anthropic.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Your receipt from Anthropic, PBC #2036-5009-8840 ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>
</div>

<div style="background:#f0fff4; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Job Search / Recruiters (15)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#2 · Thu, 04 Jun 2026 05:20:03 -0700</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">[missophs/daily-briefing] Run failed: Email Daily Briefing - webhooks (d4a4f29)</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> missophs &lt;notifications@github.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">[missophs/daily-briefing] Email Daily Briefing workflow run Email Daily Briefing: All jobs have failed View workflow run Status Job Annotations Email </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#4 · Thu, 4 Jun 2026 12:19:10 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">#188 - You&#x27;re Reading Job Descriptions Backwards</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Adam Karpiak via LinkedIn &lt;newsletters-noreply@linkedin.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">The latest issue is out now! Read it here!… ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#5 · Thu, 4 Jun 2026 07:18:29 -0500</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">HR search PM — 2026-06-04 | 16 Qualifying Roles · Apify-sourced</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> melissa &lt;melissaw212@gmail.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">VP+ HR Job Sweep Run date: Thursday, June 4, 2026 | 72-hour window: June 1–4, 2026 | PM Sweep | 33 boards searched 16Qualifying Roles 14Direct Hire 2S</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#11 · Thu, 4 Jun 2026 12:00:24 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">The AI Shift Every HR Leader Needs to Prepare for in 2026</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Christopher Rainey via LinkedIn &lt;newsletters-noreply@linkedin.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">🎧 Listen to the full episode on YouTube | Apple | Spotify Get the 3 minute… ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#20 · Thu, 4 Jun 2026 11:05:43 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Chief Human Resources Officer at Nsight Health: up to $255K/year</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> LinkedIn Job Alerts &lt;jobalerts-noreply@linkedin.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">$215K-$255K / year salary ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#22 · Thu, 4 Jun 2026 10:56:45 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">How Industrial Leaders Are Underestimating AI Workforce Disruption</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Stanton Chase: Executive Search &amp; Leadership Consultants via LinkedIn&quot; &lt;newsletters-noreply@linkedin.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Industrial is the sector where physical AI is arriving first, and it is also… ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#29 · Thu, 4 Jun 2026 09:05:46 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Chief Human Resources Officer at Nsight Health: up to $255K/year</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> LinkedIn Job Alerts &lt;jobalerts-noreply@linkedin.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">$215K-$255K / year salary ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#34 · Thu, 4 Jun 2026 07:06:03 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Chief Human Resources Officer at Nsight Health: up to $255K/year</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> LinkedIn Job Alerts &lt;jobalerts-noreply@linkedin.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">$215K-$255K / year salary ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#37 · Thu, 4 Jun 2026 05:05:44 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">You have an invitation ✉️</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Liam Sheridan &lt;invitations@linkedin.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Liam, Founder from Leads That Show is waiting for your response ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#41 · Thu, 04 Jun 2026 03:30:04 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Human Resources Director at Corporate Castle and 10 more jobs in Remote, US for you. Apply Now.</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Glassdoor Jobs &lt;noreply@glassdoor.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Progressive Insurance is hiring ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#43 · Thu, 4 Jun 2026 03:05:44 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Chief Human Resources Officer at Nsight Health: up to $255K/year</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> LinkedIn Job Alerts &lt;jobalerts-noreply@linkedin.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">$215K-$255K / year salary ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#46 · Wed, 3 Jun 2026 21:20:24 -0500</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">HR search PM — 2026-06-03 | 12 Qualifying Roles · Apify-sourced</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> melissa &lt;melissaw212@gmail.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">VP+ HR Job Sweep Run date: Wednesday, June 3, 2026 | 72-hour window: June 1–3, 2026 (PM sweep) | 36 sources searched 12Qualifying Roles 10Direct Hire </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#47 · Wed, 3 Jun 2026 19:05:39 -0700</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">HR search PM — 2026-06-03 | 12 Qualifying Roles · Apify-sourced</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> melissa &lt;melissaw212@gmail.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">VP+ HR Job Sweep Run date: Wednesday, June 3, 2026 | 72-hour window: June 1–3, 2026 (PM sweep) | 36 sources searched 12Qualifying Roles 10Direct Hire </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#48 · Thu, 4 Jun 2026 00:47:58 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">You have 3 new invitations</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> LinkedIn &lt;notifications-noreply@linkedin.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">See who reached out, Dennis 🤝 ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#49 · Thu, 4 Jun 2026 00:41:50 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">👤 Melissa, add Thet Hnin Aung - Human Resources Coordinator</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> LinkedIn &lt;messages-noreply@linkedin.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">HR Generalist | HR Operations &amp;amp; Employee Relations | HRIS (Workday, ADP, Dayforce) | Data-Driven HR &amp;amp; Compliance ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>
</div>

<div style="background:#ebf8ff; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Medical / Health (1)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#36 · Thu, 04 Jun 2026 00:09:26 -0600</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Now Online: A new Explanation of Benefits is available</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> UnitedHealthcare Notifications &lt;Notifications@edelivery.uhc.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">It&amp;#39;s easy to access this important information ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>
</div>

<div style="background:#f7fafc; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Other / Review (22)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#1 · Thu, 04 Jun 2026 12:25:28 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Melissa Daily Briefing - 2026-06-04 12:25 UTC</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Melissa Daily Briefing &lt;melissaw212@gmail.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">☀️ Good Morning, Melissa Thursday, June 4, 2026 · Executive Chief of Staff Briefing · Prepared fresh — everything you need, nothing you don&amp;#39;t. 50 </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#6 · Thu, 04 Jun 2026 12:15:11 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Wait, your liner doesn’t stain? 👀</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Kulfi Beauty &lt;hello@kulfibeauty.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Creamy glide. Cute after. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#7 · Thu, 04 Jun 2026 06:03:28 -0600</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">When in doubt, Sam Edelman</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Zappos &lt;cs@emails.zappos.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Pairs you&amp;#39;ll wear again &amp;amp; again &amp;amp; again ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#13 · Thu, 04 Jun 2026 12:40:36 +0100</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">🚨Final Notice🚨: melissaw212 Claim Your Funds Now💸_Fq</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;&#x27;Claims_Department&#x27;&quot; &lt;DrsjU@hoiutj.lt&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">💰 Unclaimed Assets Alert! Name melissaw212 – melissaw212@gmail.com To: melissaw212@gmail.com Dear melissaw212, 🔎 We&amp;#39;ve identified unclaimed financ</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#14 · 04 Jun 2026 11:40:35 -0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">EARLY ACCESS starts now! 🎉​</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> TJ MAXX EARLY ACCESS &lt;tjmaxx@eml.tjmaxx.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">(New arrivals just for you). ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#15 · Thu, 04 Jun 2026 11:30:00 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">I Made Claude Smarter by Connecting It to NotebookLM. Here’s How | The PyCoach in Artificial Corner</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Medium Daily Digest &lt;noreply@medium.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Melissaw Stories for Melissaw @melissaw212·Become a member Medium daily digest Today&amp;#39;s highlights The PyCoach The PyCoachinArtificial Corner I Mad</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#16 · Thu, 04 Jun 2026 11:22:28 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Your Daily Digest for Thu, 6/4 is ready to view</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> USPS Informed Delivery &lt;USPSInformeddelivery@email.informeddelivery.usps.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">COMING TO YOU SOON Hi, Meliss! You have 0 mailpiece(s) and 1 inbound package(s) arriving soon. Thursday 4 June 2026 0 Mailpiece(s) 1 Package(s) Hi, Me</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#18 · Thu, 4 Jun 2026 06:13:15 -0500</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Melissa&#x27;s Daily Briefing - June 4, 2026</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> melissa &lt;melissaw212@gmail.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">☀️ MELISSA&amp;#39;S DAILY BRIEFING Thursday, June 4, 2026 | Prepared from Gmail, Google Calendar &amp;amp; Slack 💡 Executive Summary 🔴 Top 3 Requiring Attent</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#21 · Thu, 04 Jun 2026 11:00:41 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Gift Tax, Explained: 2025 and 2026 Exemptions and Rates</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> SmartAsset Headlines &lt;hello@hello.smartasset.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Plus: Costly capital gains tax mistakes seniors should avoid. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#24 · Thu, 4 Jun 2026 06:36:45 -0400</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">🌱  Plants talk back</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> The Hustle &lt;news@thehustle.co&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Plus: An accidental corporate AI splurge, an analysis of similes, and more. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#25 · Thu, 4 Jun 2026 06:15:39 -0400 (EDT)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Turn the whimsy up to 11</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> The Daily Skimm &lt;dailyskimm@morning7.theskimm.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">But first: we cracked the code to making dinner less stressful — Check out what we Skimm&amp;#39;d for you today June 4, 2026 Subscribe Read in browser To</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#26 · Thu, 04 Jun 2026 04:11:59 -0600</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">$3 Coupon!</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> CVS ExtraCare &lt;extracare@mystore.cvs.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">************************************ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#27 · Thu, 4 Jun 2026 10:00:39 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Claude hustle is printing cash for beginners</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> CoolDeep AI &lt;cooldeepai@mail.beehiiv.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Someone with zero experience made $3300 in 2 weeks. Here is how. ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#28 · Thu, 04 Jun 2026 05:38:33 -0400</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">You have a new trade confirmation</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Merrill Edge &lt;merrilledge@ml.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">You have a new trade confirmation A new trade confirmation is now available online and in our mobile app. View trade confirmations The Merrill Edge ap</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#30 · Thu, 04 Jun 2026 09:05:28 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">[TPPG] Advice on ATS for Scaling…, AnonQ and 8 more topics</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> The People People Group &lt;community@thepeoplepeoplegroup.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Here are some of the most popular new topics discussed in the The People People Group last week: Myranda Heipel 🎯 Recruiting ✚ Advice on ATS for Scali</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#31 · Thu, 04 Jun 2026 09:00:14 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">ThePeoplePeopleGroup Digest - 6/04/26</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> ThePeoplePeopleGroup &lt;Digest@meetwaves.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">ThePeoplePeopleGroup Weekly digest From standout threads to must-read insights, we&amp;#39;ve rounded up the most useful, thought-provoking, and talked-ab</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#35 · Thu, 04 Jun 2026 06:22:35 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Three new Actors this week: Google Images ($0.10/1K), Local pack, Maps Places Lite</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Apify Community &lt;hello@community.apify.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Apify This is a message from an Apify community developer John (johnvc), which you&amp;#39;re receiving because you&amp;#39;ve recently used one of the Actors</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#39 · Thu, 04 Jun 2026 00:00:40 -0400</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Thank you for your interest in Senior Human Resources Business Partner position</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> notify@dayforce.com</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Dear MELISSA, Thank you for your interest in the Senior Human Resources Business Partner position and for the time and effort you invested in the appl</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#40 · Thu, 4 Jun 2026 03:35:11 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Shipped: &quot;Utopia Towels, 35 by 70...&quot;</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Amazon.com&quot; &lt;shipment-tracking@amazon.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Shipped: &amp;quot;Utopia Towels, 35 by 70...&amp;quot;͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#42 · Thu, 4 Jun 2026 03:11:57 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">It&#x27;s been a week — we’d love your thoughts</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;noreply@notice.halara.com&quot; &lt;noreply@notice.halara.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Your experience helps us improve — and gets you rewards. Hi Melissa , It&amp;#39;s been a week since your package arrived — we hope you&amp;#39;ve been enjoyi</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#44 · Wed, 03 Jun 2026 21:49:35 -0500</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Someone likes you</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> OkCupid &lt;bounces@alerts.oknotify3.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Message them now ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#50 · Wed, 03 Jun 2026 17:28:25 -0700</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Your Google Play Order Receipt from Jun 3, 2026</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Google Play &lt;googleplay-noreply@google.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Google Play Thank you Your subscription from Google LLC on Google Play continues and you&amp;#39;ve been charged. Manage your subscriptions Order number: </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>
</div>

<div style="background:#faf5ff; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Professional Development / Newsletters (2)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#3 · Thu, 4 Jun 2026 12:19:52 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">How a CHRO uses Claude for turnover pattern analysis</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> The CHRO Office &lt;thehroffice@substack.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Yesterday Sara Skowronski walked Insider Members through her real workflow. Her exact prompts, her project setup, and the one rule she puts at the end</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#10 · Thu, 4 Jun 2026 12:01:29 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Melissa, Can You Name Which Roles AI Will Change First?</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> HR Leaders Events &lt;hello@hrleaders.co&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Learn what Microsoft, Alstom and Inditex are tracking first. ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​ ͏​</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>
</div>

<div style="background:#f7fafc; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Promotional / Retail (4)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#12 · Thu, 04 Jun 2026 06:47:40 -0500</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Clearance Drop! Score Deals Before They&#x27;re Gone</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Walgreens &lt;walgreens@eml.walgreens.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Find Your Favorites for Less—Up to 60% Off Clearance ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#32 · Thu, 04 Jun 2026 02:05:47 -0600</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Super low prices 🤝 Kohl&#x27;s Cash 🙌</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Kohl&#x27;s Lowest Prices of the Season&quot; &lt;kohls@s.kohls.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">And don&amp;#39;t miss up to 85% off clearance. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#33 · Thu, 04 Jun 2026 07:39:35 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Early Access | Our Anniversary celebration begins with you</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> VIVAIA &lt;hello@edm.vivaia.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Six Years of Moving Forward, Beautifully. New｜Best Sellers｜Collection｜Sale NEW NEW NEW NEW NEW NEW Flats｜Loafers｜Sneakers｜Bags &amp;amp; Accs Facebook ins</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#38 · Thu, 04 Jun 2026 04:05:31 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Need a Fit? Co-Ords up to 50% OFF</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> SHEIN &lt;shein@news.edmmarket.shein.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Less styling, more serving—shop sets here 👇 ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>
</div>

<div style="background:#fff5f5; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Security / Risk (3)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#9 · Thu, 04 Jun 2026 12:01:52 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Instagram&#x27;s AI chatbot gave away passwords</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Mindstream &lt;hello@mindstream.news&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">+ Scorsese thinks AI is great for film makers ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Act / Delete if scam</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#17 · Thu, 04 Jun 2026 11:22:12 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Don&#x27;t follow your passion</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Lisa Rangel &lt;lr@chameleonresumes.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">(an unpopular career opinion) If you listen to certain celebrities and motivational types, you should walk out of any job you hate. Today. And look, n</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Act / Delete if scam</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#19 · Thu, 04 Jun 2026 21:07:55 +1000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">🛡️ Cybersecurity’s verdict</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> The Average Joe &lt;joe@readthejoe.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Chasing the physical AI trade ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Act / Delete if scam</div>
</div>
</div>
</table>

