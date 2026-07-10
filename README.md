<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Melissa's Executive Briefing — Friday, July 10, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrapper { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: white; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px; }
  .header-left h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header-left .subtitle { font-size: 15px; color: #a8b2d8; margin-top: 4px; }
  .header-right { text-align: right; }
  .header-right .date { font-size: 18px; font-weight: 600; color: #e2e8f0; }
  .header-right .meta { font-size: 13px; color: #a8b2d8; margin-top: 6px; }
  .meta-pill { display: inline-block; background: rgba(255,255,255,0.12); border-radius: 20px; padding: 4px 14px; margin: 3px 2px; font-size: 12px; font-weight: 600; }

  /* SECTION HEADERS */
  .section-title { font-size: 17px; font-weight: 700; letter-spacing: 0.4px; margin-bottom: 14px; padding-bottom: 8px; border-bottom: 2px solid currentColor; display: flex; align-items: center; gap: 8px; }
  .section-wrapper { background: white; border-radius: 12px; padding: 22px 24px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }

  /* COLOR THEMES */
  .red { color: #c0392b; border-color: #e74c3c !important; }
  .yellow { color: #b7770d; border-color: #f39c12 !important; }
  .blue { color: #1565c0; border-color: #1976d2 !important; }
  .green { color: #1b5e20; border-color: #2e7d32 !important; }
  .purple { color: #4a148c; border-color: #6a1b9a !important; }
  .gray { color: #546e7a; border-color: #90a4ae !important; }

  .bg-red { background: #fff5f5; border-left: 5px solid #e53e3e; }
  .bg-yellow { background: #fffbf0; border-left: 5px solid #d69e2e; }
  .bg-blue { background: #f0f7ff; border-left: 5px solid #1976d2; }
  .bg-green { background: #f0fff4; border-left: 5px solid #276749; }
  .bg-purple { background: #faf5ff; border-left: 5px solid #6b46c1; }
  .bg-gray { background: #f7fafc; border-left: 5px solid #a0aec0; }

  /* EXECUTIVE SUMMARY */
  .exec-summary { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px; }
  .exec-card { border-radius: 10px; padding: 16px 18px; }
  .exec-card .label { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
  .exec-card .title { font-size: 15px; font-weight: 700; margin-bottom: 6px; }
  .exec-card .body { font-size: 13px; color: #4a5568; }

  /* ACTION CARDS */
  .action-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px; }
  .action-card { border-radius: 10px; padding: 16px 18px; }
  .action-card .ac-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
  .action-card .ac-title { font-size: 15px; font-weight: 700; margin-bottom: 8px; }
  .action-card .ac-row { display: flex; gap: 8px; margin-bottom: 4px; font-size: 13px; }
  .ac-key { font-weight: 600; min-width: 110px; color: #4a5568; }
  .ac-val { flex: 1; }
  .badge { display: inline-block; border-radius: 20px; padding: 2px 10px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
  .badge-red { background: #fed7d7; color: #c53030; }
  .badge-yellow { background: #feebc8; color: #c05621; }
  .badge-green { background: #c6f6d5; color: #276749; }
  .badge-blue { background: #bee3f8; color: #2a69ac; }
  .badge-gray { background: #e2e8f0; color: #4a5568; }
  .badge-purple { background: #e9d8fd; color: #553c9a; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { background: #1a1a2e; color: white; border-radius: 8px 8px 0 0; padding: 8px 16px; font-weight: 700; font-size: 13px; letter-spacing: 0.5px; }
  .cal-event { padding: 12px 16px; border-bottom: 1px solid #e2e8f0; display: grid; grid-template-columns: 110px 1fr; gap: 12px; }
  .cal-event:last-child { border-bottom: none; border-radius: 0 0 8px 8px; }
  .cal-event.today-event { background: #f0f7ff; }
  .cal-time { font-weight: 700; font-size: 13px; color: #1565c0; }
  .cal-body .ev-title { font-weight: 700; font-size: 14px; margin-bottom: 4px; }
  .cal-body .ev-row { font-size: 12px; color: #4a5568; margin-bottom: 2px; }
  .cal-body .ev-row strong { color: #1a1a2e; }
  .status-chip { display: inline-block; border-radius: 4px; padding: 1px 8px; font-size: 11px; font-weight: 700; }
  .status-accepted { background: #c6f6d5; color: #276749; }
  .status-confirmed { background: #bee3f8; color: #2a69ac; }
  .status-declined { background: #fed7d7; color: #c53030; }
  .status-needs { background: #feebc8; color: #c05621; }
  .conflict-warn { background: #fff5f5; border: 1px solid #feb2b2; border-radius: 6px; padding: 4px 10px; font-size: 12px; color: #c53030; margin-top: 6px; font-weight: 600; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #1a1a2e; color: white; padding: 9px 12px; text-align: left; font-size: 12px; letter-spacing: 0.3px; }
  td { padding: 8px 12px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #f7fafc; }
  .priority-high { color: #c53030; font-weight: 700; }
  .priority-med { color: #c05621; font-weight: 700; }
  .priority-low { color: #276749; font-weight: 700; }

  /* EMAIL CATEGORY CARDS */
  .email-cat-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 14px; }
  .email-cat-card { border-radius: 10px; padding: 14px 16px; }
  .ecc-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }
  .ecc-title { font-weight: 700; font-size: 14px; }
  .ecc-count { font-size: 12px; font-weight: 700; background: rgba(0,0,0,0.08); border-radius: 20px; padding: 2px 10px; }
  .ecc-senders { font-size: 12px; color: #4a5568; margin-bottom: 6px; }
  .ecc-action { font-size: 12px; font-weight: 600; }

  /* DASHBOARD */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; }
  .dash-card { border-radius: 10px; padding: 16px; text-align: center; }
  .dash-card .dash-num { font-size: 32px; font-weight: 800; margin-bottom: 4px; }
  .dash-card .dash-label { font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; color: #4a5568; }

  /* TOP 3 */
  .top3-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; }
  .top3-card { border-radius: 12px; padding: 20px 22px; position: relative; }
  .top3-num { font-size: 48px; font-weight: 900; opacity: 0.12; position: absolute; top: 10px; right: 18px; }
  .top3-label { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; }
  .top3-title { font-size: 16px; font-weight: 700; margin-bottom: 8px; }
  .top3-body { font-size: 13px; }

  /* MISC */
  .tag { display: inline-block; background: #edf2f7; border-radius: 4px; padding: 1px 8px; font-size: 11px; margin: 2px; }
  .alert-box { border-radius: 8px; padding: 12px 16px; margin-bottom: 10px; font-size: 13px; display: flex; gap: 10px; align-items: flex-start; }
  .alert-icon { font-size: 18px; flex-shrink: 0; }
  hr.divider { border: none; border-top: 1px solid #e2e8f0; margin: 12px 0; }
  .trash-group { margin-bottom: 16px; }
  .trash-group-title { font-weight: 700; font-size: 13px; margin-bottom: 8px; padding: 4px 10px; border-radius: 6px; display: inline-block; }
  .trash-item { font-size: 12px; padding: 6px 10px; border-bottom: 1px solid #e2e8f0; }
  .trash-item:last-child { border-bottom: none; }
  .promo-table-wrap { overflow-x: auto; }
  a { color: #1565c0; text-decoration: none; }
  a:hover { text-decoration: underline; }
  .footnote { font-size: 11px; color: #718096; margin-top: 10px; font-style: italic; }
  .section-intro { font-size: 13px; color: #4a5568; margin-bottom: 14px; }
  .nowrap { white-space: nowrap; }
</style>
</head>
<body>
<div class="page-wrapper">

<!-- ============================================================ HEADER ============================================================ -->
<div class="header">
  <div class="header-left">
    <h1>☀️ Good Morning, Melissa</h1>
    <div class="subtitle">Executive Daily Briefing — Prepared by Your Chief of Staff</div>
    <div style="margin-top:12px;">
      <span class="meta-pill">📧 50 Emails Reviewed</span>
      <span class="meta-pill">📅 10 Calendar Events</span>
      <span class="meta-pill">🔒 2 Phishing Emails Auto-Trashed</span>
      <span class="meta-pill">⚡ 7 Action Items</span>
    </div>
  </div>
  <div class="header-right">
    <div class="date">Friday, July 10, 2026</div>
    <div class="meta" style="margin-top:8px;">Today's Agenda: 2 meetings · 1 package pickup</div>
    <div class="meta">Job Pipeline: 2 active leads · 1 interview today</div>
  </div>
</div>

<!-- ============================================================ EXECUTIVE SUMMARY ============================================================ -->
<div class="section-wrapper">
  <div class="section-title red">⚡ Executive Summary</div>
  <div class="exec-summary">
    <div class="exec-card bg-red">
      <div class="label red">🔴 Biggest Risk</div>
      <div class="title">GitHub Workflow Failures + Security Alert Activity</div>
      <div class="body">Your Daily Briefing GitHub Actions workflow failed 3 times this morning. Separately, Google sent two security alerts (now in trash) about account access by "gws local" — and two phishing emails were auto-trashed. Investigate the workflow failures and review any recent Google account activity.</div>
    </div>
    <div class="exec-card bg-green">
      <div class="label green">🟢 Biggest Opportunity</div>
      <div class="title">Oscar Health Phone Screen — TODAY at 2:00 PM</div>
      <div class="body">You have a confirmed phone screen with Joelle Molina at Oscar Health for the People Strategy Lead role at 2:00 PM. They will call 516-313-8888. Additionally, a CHRO role at the City of New York posted 7/9/2026 — a strong fit worth reviewing immediately.</div>
    </div>
    <div class="exec-card bg-yellow">
      <div class="label yellow">🟡 Biggest Deadline</div>
      <div class="title">Water Shutdown 7/14 + Bone Density Appt 7/15 + LHR Checklist</div>
      <div class="body">Your building has a water shutdown Monday 7/14 from 9 AM–2 PM. Your bone density appointment is Wednesday 7/15 at 8:30 AM and requires you to complete a pre-visit checklist from Lenox Hill Radiology (unread in inbox). RSVP also needed for two HR networking events on 7/15 and 7/16.</div>
    </div>
  </div>
</div>

<!-- ============================================================ ACTION REQUIRED ============================================================ -->
<div class="section-wrapper">
  <div class="section-title yellow">🎯 Action Required</div>
  <div class="action-grid">

    <div class="action-card bg-red">
      <div class="ac-label red">🔴 Urgent — Technical</div>
      <div class="ac-title">Daily Briefing GitHub Workflow Failed (×3)</div>
      <div class="ac-row"><span class="ac-key">Source:</span><span class="ac-val">melissaw212@gmail.com (self-alert)</span></div>
      <div class="ac-row"><span class="ac-key">Why it matters:</span><span class="ac-val">Your automated briefing system failed 3 times this morning. The pipeline is broken and needs repair.</span></div>
      <div class="ac-row"><span class="ac-key">Next step:</span><span class="ac-val">Visit <a href="https://github.com/missophs/daily-briefing/actions" target="_blank">GitHub Actions</a>, review run logs, and fix the failing workflow step.</span></div>
      <div class="ac-row"><span class="ac-key">Due:</span><span class="ac-val"><span class="badge badge-red">TODAY</span></span></div>
    </div>

    <div class="action-card bg-green">
      <div class="ac-label green">🟢 High Priority — Career</div>
      <div class="ac-title">Oscar Health Phone Screen — People Strategy Lead</div>
      <div class="ac-row"><span class="ac-key">Source:</span><span class="ac-val">joelle@hioscar.com via Google Calendar</span></div>
      <div class="ac-row"><span class="ac-key">Why it matters:</span><span class="ac-val">Confirmed interview today. They will call 516-313-8888 at 2:00 PM sharp.</span></div>
      <div class="ac-row"><span class="ac-key">Next step:</span><span class="ac-val">Prepare talking points for People Strategy Lead role. Ensure phone is charged and available at 2:00 PM.</span></div>
      <div class="ac-row"><span class="ac-key">Due:</span><span class="ac-val"><span class="badge badge-red">TODAY 2:00 PM</span></span></div>
    </div>

    <div class="action-card bg-yellow">
      <div class="ac-label yellow">🟡 Follow-Up — Medical</div>
      <div class="ac-title">Lenox Hill Radiology Pre-Visit Checklist</div>
      <div class="ac-row"><span class="ac-key">Source:</span><span class="ac-val">lenoxhillradiology@contact.radnet.com (Inbox, Unread)</span></div>
      <div class="ac-row"><span class="ac-key">Why it matters:</span><span class="ac-val">Your LHR appointment requires completing a checklist before your visit. Appointment date not confirmed in email — may be related to bone density on 7/15.</span></div>
      <div class="ac-row"><span class="ac-key">Next step:</span><span class="ac-val">Open email, click "GO TO CHECKLIST" and complete all pre-visit fields today.</span></div>
      <div class="ac-row"><span class="ac-key">Due:</span><span class="ac-val"><span class="badge badge-yellow">TODAY — Before visit</span></span></div>
    </div>

    <div class="action-card bg-yellow">
      <div class="ac-label yellow">🟡 Follow-Up — Building</div>
      <div class="ac-title">Package Pickup — UPS Delivery at 303 East 83rd (Apt 03H)</div>
      <div class="ac-row"><span class="ac-key">Source:</span><span class="ac-val">303 East 83rd via Equity Apartments (Inbox, Unread)</span></div>
      <div class="ac-row"><span class="ac-key">Why it matters:</span><span class="ac-val">A UPS package is waiting for pickup at the front desk/package room at your building.</span></div>
      <div class="ac-row"><span class="ac-key">Next step:</span><span class="ac-val">Stop by the building management/concierge to pick up your UPS package when convenient today.</span></div>
      <div class="ac-row"><span class="ac-key">Due:</span><span class="ac-val"><span class="badge badge-yellow">TODAY</span></span></div>
    </div>

    <div class="action-card bg-yellow">
      <div class="ac-label yellow">🟡 Heads Up — Building</div>
      <div class="ac-title">Water Shutdown Monday 7/14: 9 AM – 2 PM</div>
      <div class="ac-row"><span class="ac-key">Source:</span><span class="ac-val">Madeline Casiano via AppFolio (Inbox, Read)</span></div>
      <div class="ac-row"><span class="ac-key">Why it matters:</span><span class="ac-val">No water in building Monday 7/14 from 9 AM to 2 PM due to plumbing maintenance. Plan ahead.</span></div>
      <div class="ac-row"><span class="ac-key">Next step:</span><span class="ac-val">Fill water, shower before 9 AM, and plan any errands outside the building during the shutdown window.</span></div>
      <div class="ac-row"><span class="ac-key">Due:</span><span class="ac-val"><span class="badge badge-yellow">MONDAY 7/14</span></span></div>
    </div>

    <div class="action-card bg-yellow">
      <div class="ac-label yellow">🟡 RSVP Needed — Networking</div>
      <div class="ac-title">RSVP: HR Networking & Job Search Group — Zoom (7/15 & 7/16)</div>
      <div class="ac-row"><span class="ac-key">Source:</span><span class="ac-val">Google Calendar — "needsAction" status on both events</span></div>
      <div class="ac-row"><span class="ac-key">Why it matters:</span><span class="ac-val">Two HR networking events (7/15 and 7/16) show status "needsAction" — you have not yet RSVP'd to either. These are valuable job search networking sessions.</span></div>
      <div class="ac-row"><span class="ac-key">Next step:</span><span class="ac-val">Review calendar invites and respond Accept or Decline for 7/15 (12–1:30 PM) and 7/16 (12–1 PM) Zoom sessions.</span></div>
      <div class="ac-row"><span class="ac-key">Due:</span><span class="ac-val"><span class="badge badge-yellow">Before 7/15</span></span></div>
    </div>

    <div class="action-card bg-green">
      <div class="ac-label green">🟢 Opportunity — Career</div>
      <div class="ac-title">CHRO Role — City of New York (LinkedIn Alert)</div>
      <div class="ac-row"><span class="ac-key">Source:</span><span class="ac-val">LinkedIn Job Alerts (Inbox, Unread) — posted 7/9/2026</span></div>
      <div class="ac-row"><span class="ac-key">Why it matters:</span><span class="ac-val">Chief Human Resources Officer at City of New York — a senior, high-impact role directly aligned with your background. Posted yesterday.</span></div>
      <div class="ac-row"><span class="ac-key">Next step:</span><span class="ac-val">Open LinkedIn alert, review role requirements, and apply or identify a referral connection today.</span></div>
      <div class="ac-row"><span class="ac-key">Due:</span><span class="ac-val"><span class="badge badge-green">ASAP — Posted 7/9</span></span></div>
    </div>

  </div>
</div>

<!-- ============================================================ FULL 7-DAY CALENDAR ============================================================ -->
<div class="section-wrapper">
  <div class="section-title blue">📅 Full 7-Day Calendar</div>
  <p class="section-intro">All 10 calendar events displayed. Events span Friday July 10 through Thursday July 16, 2026.</p>

  <!-- FRIDAY JULY 10 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 FRIDAY · JULY 10, 2026 — TODAY</div>

    <div class="cal-event today-event">
      <div class="cal-time">2:00 PM<br>– 2:25 PM</div>
      <div class="cal-body">
        <div class="ev-title">🟢 Oscar Health Phone Screen — People Strategy Lead</div>
        <div class="ev-row"><strong>With:</strong> Joelle Molina (joelle@hioscar.com) · Oscar Health</div>
        <div class="ev-row"><strong>Location:</strong> Phone — they will call 516-313-8888 · or Google Meet</div>
        <div class="ev-row"><strong>Status:</strong> <span class="status-chip status-accepted">✅ Accepted</span></div>
        <div class="ev-row"><strong>Prep:</strong> Review Oscar Health People Strategy priorities; prepare STAR examples for strategic HR leadership; have questions ready about the role scope and team structure. Phone must be on and available at 2:00 PM.</div>
      </div>
    </div>

    <div class="cal-event today-event">
      <div class="cal-time">3:30 PM<br>– 4:30 PM</div>
      <div class="cal-body">
        <div class="ev-title">🔵 Dr. Appointment</div>
        <div class="ev-row"><strong>Location:</strong> Not specified</div>
        <div class="ev-row"><strong>Status:</strong> <span class="status-chip status-confirmed">🔵 Confirmed</span></div>
        <div class="ev-row"><strong>Prep:</strong> Confirm location and bring any relevant paperwork or insurance card. Note: this event follows immediately after the Oscar phone screen ends — allow yourself transition time.</div>
        <div class="conflict-warn">⚠️ Tight back-to-back: Oscar screen ends at 2:25 PM; Dr. appt at 3:30 PM. 65-minute buffer — manageable but plan commute.</div>
      </div>
    </div>
  </div>

  <!-- MONDAY JULY 13 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 MONDAY · JULY 13, 2026</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-body">
        <div class="ev-title">💙 Stephanie Infusion</div>
        <div class="ev-row"><strong>Type:</strong> All-day marker (July 13)</div>
        <div class="ev-row"><strong>Status:</strong> <span class="status-chip status-confirmed">🔵 Confirmed</span></div>
        <div class="ev-row"><strong>Note:</strong> Personal/family event — plan schedule around Stephanie's infusion appointment. No further details provided.</div>
      </div>
    </div>
  </div>

  <!-- TUESDAY JULY 14 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 TUESDAY · JULY 14, 2026</div>

    <div class="cal-event">
      <div class="cal-time">9:00 AM<br>– 2:00 PM</div>
      <div class="cal-body">
        <div class="ev-title">🟡 ⚠️ Building Water Shutdown</div>
        <div class="ev-row"><strong>Source:</strong> Email from Madeline Casiano / AppFolio</div>
        <div class="ev-row"><strong>Status:</strong> Informational — not a calendar event yet</div>
        <div class="ev-row"><strong>Prep:</strong> Fill water containers Sunday night. Shower before 9 AM. Plan to be out of the apartment or have bottled water available. Consider adding to calendar.</div>
        <div class="conflict-warn">⚠️ Water service off from 9 AM to 2 PM — plan accordingly.</div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">10:00 AM<br>– 11:00 AM</div>
      <div class="cal-body">
        <div class="ev-title">🔵 Stella</div>
        <div class="ev-row"><strong>Location:</strong> Not specified</div>
        <div class="ev-row"><strong>Status:</strong> <span class="status-chip status-confirmed">🔵 Confirmed</span></div>
        <div class="ev-row"><strong>Prep:</strong> No details provided. Confirm any prep or materials needed with Stella ahead of time.</div>
        <div class="conflict-warn">⚠️ Water shutdown active during this time (9 AM–2 PM). If meeting is at home, plan ahead.</div>
      </div>
    </div>
  </div>

  <!-- WEDNESDAY JULY 15 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 WEDNESDAY · JULY 15, 2026</div>

    <div class="cal-event">
      <div class="cal-time">8:30 AM<br>– 9:30 AM</div>
      <div class="cal-body">
        <div class="ev-title">🏥 Bone Density Appointment</div>
        <div class="ev-row"><strong>Location:</strong> Not specified (likely Lenox Hill Radiology — confirm)</div>
        <div class="ev-row"><strong>Status:</strong> <span class="status-chip status-confirmed">🔵 Confirmed</span></div>
        <div class="ev-row"><strong>Prep:</strong> Complete the LHR pre-visit checklist TODAY (see Action Required). Bring insurance card. Confirm location from the email. Avoid calcium supplements 24 hours prior if instructed.</div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">12:00 PM<br>– 1:30 PM</div>
      <div class="cal-body">
        <div class="ev-title">🟣 HR Networking &amp; Job Search Group — Zoom Session 2</div>
        <div class="ev-row"><strong>Location:</strong> <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a></div>
        <div class="ev-row"><strong>Attendees:</strong> Large group (170+ HR professionals)</div>
        <div class="ev-row"><strong>Status:</strong> <span class="status-chip status-needs">⚠️ RSVP Needed</span></div>
        <div class="ev-row"><strong>Prep:</strong> RSVP now. Disable automated notetaking AI tools per host request. Review team guidelines before joining. Good networking opportunity during job search.</div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">12:00 PM<br>– 1:30 PM</div>
      <div class="cal-body">
        <div class="ev-title">🟣 Network (Personal Reminder)</div>
        <div class="ev-row"><strong>Status:</strong> <span class="status-chip status-confirmed">🔵 Confirmed</span></div>
        <div class="ev-row"><strong>Note:</strong> Personal calendar block coinciding with the HR Networking Zoom. Likely a self-reminder for the same session.</div>
        <div class="conflict-warn">⚠️ Two calendar events at same time (12–1:30 PM). Likely duplicates — confirm and consolidate.</div>
      </div>
    </div>
  </div>

  <!-- THURSDAY JULY 16 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 THURSDAY · JULY 16, 2026</div>

    <div class="cal-event">
      <div class="cal-time">9:00 AM<br>– 10:30 AM</div>
      <div class="cal-body">
        <div class="ev-title">❌ Executive Roundtable (John Madigan — Zoom)</div>
        <div class="ev-row"><strong>Location:</strong> <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> · Meeting ID: 207 786 667 · Password: 205454</div>
        <div class="ev-row"><strong>Status:</strong> <span class="status-chip status-declined">❌ Declined</span></div>
        <div class="ev-row"><strong>Note:</strong> You have declined this event. No action needed unless you wish to reconsider.</div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">12:00 PM<br>– 1:00 PM</div>
      <div class="cal-body">
        <div class="ev-title">🟣 HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
        <div class="ev-row"><strong>Location:</strong> <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a></div>
        <div class="ev-row"><strong>Attendees:</strong> Large group (170+ HR professionals)</div>
        <div class="ev-row"><strong>Status:</strong> <span class="status-chip status-needs">⚠️ RSVP Needed</span></div>
        <div class="ev-row"><strong>Prep:</strong> RSVP now. Open discussion format — no AI notetaking tools per host. Good opportunity for 1:1 networking connections.</div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">1:00 PM<br>– 2:00 PM</div>
      <div class="cal-body">
        <div class="ev-title">🟢 Tea with LeiLani | Brew At the Table — T Shop</div>
        <div class="ev-row"><strong>Location:</strong> T Shop · 247 Elizabeth St, New York, NY 10012</div>
        <div class="ev-row"><strong>Attendees:</strong> LeiLani (leilani@bethechangehr.com), Teresa Low, Leyla Snovini, Jessi (Alvi Solutions)</div>
        <div class="ev-row"><strong>Status:</strong> <span class="status-chip status-accepted">✅ Accepted</span></div>
        <div class="ev-row"><strong>Prep:</strong> Small group HR professional networking. Great relationship-building opportunity. Note location in Nolita — plan commute from Upper East Side (~30 min). Back-to-back with Zoom office hours — leave Zoom promptly at 1:00 PM.</div>
        <div class="conflict-warn">⚠️ Back-to-back: Zoom Office Hours ends 1:00 PM → Tea at LeiLani also starts 1:00 PM. Plan to exit Zoom on time and commute promptly.</div>
      </div>
    </div>
  </div>
</div>

<!-- ============================================================ JOB SEARCH & INTERVIEW PIPELINE ============================================================ -->
<div class="section-wrapper">
  <div class="section-title green">💼 Job Search &amp; Interview Pipeline</div>
  <table>
    <thead>
      <tr>
        <th>Priority</th>
        <th>Opportunity</th>
        <th>Source</th>
        <th>Status</th>
        <th>Next Step</th>
        <th>Due</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="priority-high">HIGH</span></td>
        <td><strong>People Strategy Lead</strong><br>Oscar Health</td>
        <td>joelle@hioscar.com<br>Google Calendar</td>
        <td><span class="badge badge-green">Phone Screen TODAY</span></td>
        <td>Be available at 516-313-8888 at 2:00 PM. Prepare STAR stories, role research, questions.</td>
        <td class="nowrap">TODAY 2 PM</td>
      </tr>
      <tr>
        <td><span class="priority-high">HIGH</span></td>
        <td><strong>Chief Human Resources Officer</strong><br>City of New York</td>
        <td>LinkedIn Job Alerts<br>(Inbox, Unread)</td>
        <td><span class="badge badge-yellow">New — Unreviewed</span></td>
        <td>Open LinkedIn alert. Review JD. Apply or find internal referral connection ASAP. Posted 7/9.</td>
        <td class="nowrap">ASAP</td>
      </tr>
      <tr>
        <td><span class="priority-med">MEDIUM</span></td>
        <td><strong>ZenSearch Daily Job Matches</strong><br>Principal GTM Recruiter · Talentful (NYC Hybrid) + others</td>
        <td>Amy from ZenSearch<br>(Inbox)</td>
        <td><span class="badge badge-blue">New Matches</span></td>
        <td>Review today's ZenSearch matches. Flag any roles for application or tracking.</td>
        <td class="nowrap">Today</td>
      </tr>
      <tr>
        <td><span class="priority-med">MEDIUM</span></td>
        <td><strong>HR Networking &amp; Job Search Group</strong><br>Zoom — 170+ HR Professionals</td>
        <td>Google Calendar<br>7/15 &amp; 7/16</td>
        <td><span class="badge badge-yellow">RSVP Needed</span></td>
        <td>RSVP to both Zoom sessions (7/15 and 7/16). Strong networking pool for referrals and leads.</td>
        <td class="nowrap">Before 7/15</td>
      </tr>
      <tr>
        <td><span class="priority-med">MEDIUM</span></td>
        <td><strong>Tea with LeiLani | Brew At the Table</strong><br>T Shop, 247 Elizabeth St, NYC</td>
        <td>Google Calendar<br>LeiLani (Be The Change HR)</td>
        <td><span class="badge badge-green">Accepted — 7/16 1 PM</span></td>
        <td>Research LeiLani and other attendees (Teresa Low, Jessi/Alvi Solutions). Bring business cards or LinkedIn QR.</td>
        <td class="nowrap">7/16</td>
      </tr>
      <tr>
        <td><span class="priority-low">LOW</span></td>
        <td><strong>Scholar Rock — Application Rejected</strong></td>
        <td>no-reply@hire.lever.co<br>(Trash)</td>
        <td><span class="badge badge-gray">Rejected</span></td>
        <td>Note the rejection. Consider sending a gracious follow-up to keep the relationship open. Remove from active pipeline.</td>
        <td class="nowrap">Optional</td>
      </tr>
    </tbody>
  </table>
  <div class="alert-box bg-yellow" style="margin-top:14px;">
    <div class="alert-icon">💡</div>
    <div><strong>Pipeline Note:</strong> Your existing Daily Briefing previously noted an Oscar Health phone screen at 2:00 PM as the top HIGH priority item — fully confirmed. The CHRO at City of New York is a rare, high-visibility opportunity posted yesterday. Prioritize both today.</div>
  </div>
</div>

<!-- ============================================================ FULL EMAIL REVIEW BY CATEGORY ============================================================ -->
<div class="section-wrapper">
  <div class="section-title blue">📬 Full Email Review by Category</div>
  <p class="section-intro">All 50 emails reviewed and categorized below. Each email appears in exactly one category.</p>
  <div class="email-cat-grid">

    <!-- SECURITY / RISK -->
    <div class="email-cat-card bg-red">
      <div class="ecc-header"><span class="ecc-title red">🔴 Security / Risk</span><span class="ecc-count">6 emails</span></div>
      <div class="ecc-senders">
        <strong>Senders:</strong> melissaw212@gmail.com (×3 workflow failure alerts) · Google Accounts (×2 security alerts) · Fake GmailSupportTeam (×1 phishing — auto-trashed) · Fake CVSRewards (×1 phishing — auto-trashed)
      </div>
      <div style="font-size:12px; margin-bottom:8px;">
        <div>• <span class="badge badge-red">AUTO-TRASHED</span> Fake "CVSRewards" — credential-harvesting prize scam</div>
        <div style="margin-top:3px;">• <span class="badge badge-red">AUTO-TRASHED</span> Fake "GmailSupportTeam" — 48-hour account closure phishing</div>
        <div style="margin-top:3px;">• <span class="badge badge-yellow">REVIEW</span> Google: "Security alert" — gws local access to Google Account</div>
        <div style="margin-top:3px;">• <span class="badge badge-yellow">REVIEW</span> Google: Security alert copy for recovery email</div>
        <div style="margin-top:3px;">• <span class="badge badge-red">URGENT</span> Self-alert ×3: GitHub workflow FAILED (two unread in inbox, one in trash)</div>
      </div>
      <div class="ecc-action red">🔴 Action: Fix GitHub workflow immediately. Review Google account access log for "gws local." Both phishing emails already auto-trashed — no further action needed.</div>
    </div>

    <!-- JOB SEARCH -->
    <div class="email-cat-card bg-green">
      <div class="ecc-header"><span class="ecc-title green">🟢 Job Search</span><span class="ecc-count">3 emails</span></div>
      <div class="ecc-senders">
        <strong>Senders:</strong> LinkedIn Job Alerts (CHRO — City of New York) · Amy from ZenSearch (daily job matches) · Scholar Rock / Lever (rejection)
      </div>
      <div style="font-size:12px; margin-bottom:8px;">
        <div>• <span class="badge badge-green">HIGH FIT</span> CHRO at City of New York — LinkedIn (Inbox, Unread)</div>
        <div style="margin-top:3px;">• <span class="badge badge-green">REVIEW</span> ZenSearch: Principal GTM Recruiter + matches (Inbox, Read)</div>
        <div style="margin-top:3px;">• <span class="badge badge-gray">CLOSED</span> Scholar Rock — Application rejected (Trash)</div>
      </div>
      <div class="ecc-action green">✅ Action: Review CHRO alert and apply. Review ZenSearch matches. Note Scholar Rock rejection.</div>
    </div>

    <!-- MEDICAL / HEALTH -->
    <div class="email-cat-card bg-yellow">
      <div class="ecc-header"><span class="ecc-title yellow">🟡 Medical / Health</span><span class="ecc-count">1 email</span></div>
      <div class="ecc-senders">
        <strong>Senders:</strong> Lenox Hill Radiology (Inbox, Unread)
      </div>
      <div style="font-size:12px; margin-bottom:8px;">
        <div>• <span class="badge badge-yellow">ACTION NEEDED</span> LHR pre-visit checklist — "GO TO CHECKLIST" required before your visit</div>
      </div>
      <div class="ecc-action yellow">🟡 Action: Complete pre-visit checklist TODAY. Confirm appointment date and location.</div>
    </div>

    <!-- PERSONAL / BUILDING -->
    <div class="email-cat-card bg-yellow">
      <div class="ecc-header"><span class="ecc-title yellow">🟡 Personal / Building</span><span class="ecc-count">2 emails</span></div>
      <div class="ecc-senders">
        <strong>Senders:</strong> 303 East 83rd / Equity Apartments (UPS delivery, Inbox) · Madeline Casiano / AppFolio (water shutdown notice, Inbox)
      </div>
      <div style="font-size:12px; margin-bottom:8px;">
        <div>• <span class="badge badge-yellow">PICK UP</span> UPS package waiting at front desk — Apt 03H</div>
        <div style="margin-top:3px;">• <span class="badge badge-yellow">PLAN AHEAD</span> Water shutdown 7/14, 9 AM–2 PM</div>
      </div>
      <div class="ecc-action yellow">🟡 Action: Pick up package today. Prepare for water shutdown Monday.</div>
    </div>

    <!-- CALENDAR / EVENTS -->
    <div class="email-cat-card bg-blue">
      <div class="ecc-header"><span class="ecc-title blue">🔵 Calendar / Events</span><span class="ecc-count">1 email</span></div>
      <div class="ecc-senders">
        <strong>Senders:</strong> Yorkville Safety Posts / Nextdoor (neighborhood safety — white van observation, Not in trash, Not in inbox)
      </div>
      <div style="font-size:12px; margin-bottom:8px;">
        <div>• Nextdoor neighborhood post from Yorkville (E83 St / 2nd Ave) area — resident reported seeing masked person in white van at Hamilton Park. Low direct risk but local awareness.</div>
      </div>
      <div class="ecc-action blue">🔵 Action: Noted for local awareness. No immediate action required.</div>
    </div>

    <!-- DAILY BRIEFING -->
    <div class="email-cat-card bg-blue">
      <div class="ecc-header"><span class="ecc-title blue">🔵 Daily Briefing (Self)</span><span class="ecc-count">2 emails</span></div>
      <div class="ecc-senders">
        <strong>Senders:</strong> melissaw212@gmail.com — Daily Briefing 2026-07-10 (Inbox, Read) · melissa — same briefing earlier draft (Trash)
      </div>
      <div style="font-size:12px; margin-bottom:8px;">
        <div>• <span class="badge badge-blue">READ</span> Today's briefing (delivered at 7:12 AM) — already reviewed</div>
        <div style="margin-top:3px;">• <span class="badge badge-gray">TRASH</span> Earlier draft of today's briefing — safe to delete</div>
      </div>
      <div class="ecc-action blue">✅ No action. Keep inbox copy for reference. Delete trash copy.</div>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="email-cat-card bg-purple">
      <div class="ecc-header"><span class="ecc-title purple">🟣 Professional Development</span><span class="ecc-count">4 emails</span></div>
      <div class="ecc-senders">
        <strong>Senders:</strong> Payscale (retention/compensation newsletter) · SHRM Membership (2026 Benefits Survey) · HR Brain Pickings (Friday newsletter) · Transform Community (workplace ecosystems digest)
      </div>
      <div style="font-size:12px; margin-bottom:8px;">
        <div>• Payscale — Compference26, flight risk, AI compensation (Not in trash)</div>
        <div style="margin-top:3px;">• SHRM — 2026 Benefits Survey (Trash)</div>
        <div style="margin-top:3px;">• HR Brain Pickings — reverse DEI, HR hackathons, AI bets (Trash)</div>
        <div style="margin-top:3px;">• Transform Community — workplace ecosystems, change management (Trash)</div>
      </div>
      <div class="ecc-action purple">🟣 Action: Review Payscale newsletter (relevant to job search). SHRM survey worth completing if time allows. Others: review or delete.</div>
    </div>

    <!-- NEWSLETTERS / SUBSCRIPTIONS -->
    <div class="email-cat-card bg-purple">
      <div class="ecc-header"><span class="ecc-title purple">🟣 Newsletters / Subscriptions</span><span class="ecc-count">6 emails</span></div>
      <div class="ecc-senders">
        <strong>Senders:</strong> HR Brew · Talent Realist · Mindstream (GPT-5.6) · Meidas+ (Substack) · Substack (live video alert) · Hebba Youssef / I Hate It Here
      </div>
      <div style="font-size:12px; margin-bottom:8px;">
        <div>• HR Brew — summertime working parents (Trash)</div>
        <div style="margin-top:3px;">• Talent Realist — AI vendor credibility for staffing (Trash)</div>
        <div style="margin-top:3px;">• Mindstream — GPT-5.6 imminent (Trash)</div>
        <div style="margin-top:3px;">• Meidas+ — Defense Week-in-Review 10JUL26 (Trash)</div>
        <div style="margin-top:3px;">• Substack — Ken Harbaugh Show live alert (Trash)</div>
        <div style="margin-top:3px;">• Hebba Youssef — nine cultures/PE firms (Trash)</div>
      </div>
      <div class="ecc-action purple">🟣 Action: Read if interested; safe to delete if not. See Newsletter section for full recommendations.</div>
    </div>

    <!-- PROMOTIONAL / RETAIL -->
    <div class="email-cat-card bg-gray">
      <div class="ecc-header"><span class="ecc-title gray">⚪ Promotional / Retail</span><span class="ecc-count">16 emails</span></div>
      <div class="ecc-senders">
        <strong>Brands:</strong> Macy's · e.l.f. Hair · Container Store · Laura Geller (×2) · Lands' End · H&amp;M · Verizon · eharmony · PAVOI · Walgreens · Old Navy · VIVAIA · HULKEN · Phil Strazzulla / SelectSoftware · CoolDeep AI · USA Service Dog Registration
      </div>
      <div style="font-size:12px; margin-bottom:8px;">Most are in Trash. e.l.f. Hair is in Inbox (unread). See Promotional section for full breakdown.</div>
      <div class="ecc-action gray">⚪ Action: Delete most. Review e.l.f. Hair restock alert if interested. See full Promotional section below.</div>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="email-cat-card bg-yellow">
      <div class="ecc-header"><span class="ecc-title yellow">🟡 Financial / Billing</span><span class="ecc-count">1 email</span></div>
      <div class="ecc-senders">
        <strong>Senders:</strong> My Best Buy Visa / Citi (Trash)
      </div>
      <div style="font-size:12px; margin-bottom:8px;">
        <div>• <span class="badge badge-yellow">REMINDER</span> Choose your 5% bonus category — offer ends 9/30/26</div>
      </div>
      <div class="ecc-action yellow">🟡 Action: If you use this card regularly, log in and select your bonus category before 9/30/26. Currently in trash — restore if relevant.</div>
    </div>

    <!-- SAFE TO DELETE / IGNORE -->
    <div class="email-cat-card bg-gray">
      <div class="ecc-header"><span class="ecc-title gray">⚪ Safe to Delete / Ignore</span><span class="ecc-count">8 emails</span></div>
      <div class="ecc-senders">
        <strong>Senders:</strong> GitHub (sudo verification code — expired) · Nextdoor Local News (e-bike crash Central Park — Trash) · Lisa Rangel / Chameleon Resumes (resume tips — Trash) · USPS feedback survey (Trash) · StackSocial (weekend deals — Trash) · The Muse (companies hiring in June — Trash) · U.S. Postal Service survey (Trash) · Payscale (already categorized separately)
      </div>
      <div style="font-size:12px; margin-bottom:8px;">All are low priority, expired, or already in trash. No action needed.</div>
      <div class="ecc-action gray">⚪ Action: Safe to delete permanently.</div>
    </div>

  </div>
</div>

<!-- ============================================================ TRASH REVIEW ============================================================ -->
<div class="section-wrapper">
  <div class="section-title red">🗑️ Trash Review</div>
  <p class="section-intro">Review of all emails in Gmail Trash plus auto-trashed phishing emails. Organized into three groups.</p>

  <!-- RESTORE -->
  <div class="trash-group">
    <div class="trash-group-title" style="background:#feebc8; color:#c05621;">🟡 RESTORE IMMEDIATELY (2 emails)</div>
    <div class="trash-item">
      <strong>My Best Buy® Visa® Card / Citi</strong> — "Reminder: Choose your bonus category" (ends 9/30/26)<br>
      <span style="color:#718096;">Reason to restore: This is a legitimate financial reminder with a real deadline. 5% back in rewards through September. If you use this card, log in and select your category.</span>
    </div>
    <div class="trash-item">
      <strong>Daily Briefing Alert (melissaw212 — 8:57 AM)</strong> — "ALERT: Daily Briefing workflow FAILED"<br>
      <span style="color:#718096;">Reason: Earliest of the three failure alerts — useful for diagnosing workflow timeline. Already read. Keep for reference if troubleshooting GitHub Actions.</span>
    </div>
  </div>

  <!-- REVIEW BEFORE DELETING -->
  <div class="trash-group">
    <div class="trash-group-title" style="background:#fed7d7; color:#c53030;">🔴 REVIEW BEFORE DELETING (4 emails)</div>
    <div class="trash-item">
      <strong>Google / no-reply@accounts.google.com</strong> — "Security alert for melissaw212@gmail.com"<br>
      <span style="color:#718096;">Reason: Legitimate Google security email about recovery account. Review the alert to confirm the access was authorized. Already read. Safe to delete after review.</span>
    </div>
    <div class="trash-item">
      <strong>Google / no-reply@accounts.google.com</strong> — "Security alert" — gws local access<br>
      <span style="color:#718096;">Reason: Legitimate Google alert about "gws local" accessing your account data. Verify this was an expected access (e.g., a local app or tool). If unrecognized, revoke access immediately in Google Account Security settings.</span>
    </div>
    <div class="trash-item">
      <strong>GitHub / noreply@github.com</strong> — "Sudo email verification code: 25515511"<br>
      <span style="color:#718096;">Reason: Already read and used (or expired — valid only 15 minutes). Confirms you (missophs) authenticated to GitHub around 8:43 AM. This is consistent with debugging the workflow failures. Safe to delete after confirming.</span>
    </div>
    <div class="trash-item">
      <strong>Scholar Rock / Lever</strong> — "Thanks for your interest in Scholar Rock, Melissa" (rejection)<br>
      <span style="color:#718096;">Reason: Application rejection. Review before deleting — consider sending a gracious reply to keep the recruiter relationship warm. Then delete or archive.</span>
    </div>
  </div>

  <!-- SAFE TO DELETE -->
  <div class="trash-group">
    <div class="trash-group-title" style="background:#e2e8f0; color:#4a5568;">⚪ SAFE TO DELETE (26 emails in trash)</div>
    <table style="margin-top:4px;">
      <thead>
        <tr><th>Sender</th><th>Subject</th><th>Reason</th></tr>
      </thead>
      <tbody>
        <tr><td>Macy's</td><td>Up to 60% off clearance</td><td>Retail promo — irrelevant</td></tr>
        <tr><td>Container Store</td><td>Lower Prices on Hundreds of Items</td><td>Retail promo — irrelevant</td></tr>
        <tr><td>Transform Community</td><td>Enhancing Workplace Ecosystems</td><td>Newsletter — read or delete</td></tr>
        <tr><td>My Best Buy® Visa®</td><td>Choose your bonus category</td><td>Restore if you want to act; otherwise delete</td></tr>
        <tr><td>Laura Geller (×2)</td><td>Melissa Gorga's Foundation</td><td>Retail beauty — duplicate + irrelevant</td></tr>
        <tr><td>The Muse</td><td>Companies Hiring in June</td><td>Outdated job listings (says "June" in July)</td></tr>
        <tr><td>StackSocial</td><td>THIS WEEKEND ONLY: Lowest Prices</td><td>Retail/tech deals — low priority</td></tr>
        <tr><td>HR Brew</td><td>The great hustle</td><td>Newsletter — read if interested, else delete</td></tr>
        <tr><td>melissaw212 (8:57 AM alert)</td><td>Workflow FAILED alert</td><td>Duplicate of inbox alerts — already reviewed</td></tr>
        <tr><td>Lands' End</td><td>Still thinking about your cart?</td><td>Cart abandonment email — delete</td></tr>
        <tr><td>Meidas+</td><td>Meidas Defense Week-in-Review</td><td>Political newsletter — delete</td></tr>
        <tr><td>H&amp;M</td><td>Sorted: your city summer wardrobe</td><td>Retail fashion — delete</td></tr>
        <tr><td>Verizon</td><td>FIFA World Cup 2026 / FOX One</td><td>Telecom upsell — delete</td></tr>
        <tr><td>Substack</td><td>Live video: Ken Harbaugh Show</td><td>Event alert — already live, delete</td></tr>
        <tr><td>eharmony</td><td>Your weekend highlight</td><td>Dating app promo — delete</td></tr>
        <tr><td>Talent Realist</td><td>Your AI Vendor Has Never Placed a Candidate</td><td>Newsletter — read if useful, else delete</td></tr>
        <tr><td>Mindstream</td><td>GPT-5.6 is imminent</td><td>AI newsletter — delete or read</td></tr>
        <tr><td>HR Brain Pickings</td><td>the friday 🖐️: reverse dei, hr hackathons</td><td>Newsletter — read if interested, delete</td></tr>
        <tr><td>SHRM Membership</td><td>2026 Benefits Survey</td><td>Professional survey — complete or delete</td></tr>
        <tr><td>USA Service Dog Registration</td><td>Is Your ESA Legit?</td><td>Spam/marketing — delete</td></tr>
        <tr><td>PAVOI / TikTok Shop</td><td>Save big on your favorite brands</td><td>Retail promo — delete</td></tr>
        <tr><td>Walgreens</td><td>Extra savings for seniors</td><td>Retail promo / mis-targeted — delete</td></tr>
