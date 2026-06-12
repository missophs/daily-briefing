<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa — June 12, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* Header */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 16px; padding: 36px 40px; margin-bottom: 24px; }
  .header h1 { font-size: 2rem; font-weight: 700; letter-spacing: -0.5px; }
  .header .subtitle { font-size: 1rem; color: #a8b8d8; margin-top: 4px; }
  .header-meta { display: flex; gap: 28px; margin-top: 20px; flex-wrap: wrap; }
  .header-meta .chip { background: rgba(255,255,255,0.12); border-radius: 20px; padding: 6px 16px; font-size: 0.85rem; color: #e0e8f8; }

  /* Section headers */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 1.05rem; font-weight: 700; letter-spacing: 0.4px; text-transform: uppercase; margin-bottom: 12px; padding-bottom: 6px; border-bottom: 2px solid currentColor; }

  /* Color themes */
  .red    { color: #c0392b; border-color: #c0392b; }
  .yellow { color: #b7791f; border-color: #d4a017; }
  .blue   { color: #1565c0; border-color: #1565c0; }
  .green  { color: #1b5e20; border-color: #2e7d32; }
  .purple { color: #4a148c; border-color: #6a1b9a; }
  .gray   { color: #555; border-color: #aaa; }

  /* Cards */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; border-left: 5px solid; }
  .card-red    { background: #fdf3f3; border-left-color: #c0392b; }
  .card-yellow { background: #fffbf0; border-left-color: #d4a017; }
  .card-blue   { background: #f0f5ff; border-left-color: #1565c0; }
  .card-green  { background: #f0faf2; border-left-color: #2e7d32; }
  .card-purple { background: #f7f0ff; border-left-color: #6a1b9a; }
  .card-gray   { background: #f7f7f7; border-left-color: #aaa; }

  .card-label { font-size: 0.7rem; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 4px; }
  .card-title { font-size: 1rem; font-weight: 700; margin-bottom: 6px; }
  .card-row { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 6px; }
  .card-meta { font-size: 0.8rem; color: #555; }
  .card-meta strong { color: #1a1a2e; }

  /* Executive Summary */
  .exec-summary { background: #fff; border-radius: 12px; padding: 20px 24px; border: 1px solid #e0e4ed; margin-bottom: 24px; }
  .exec-summary ul { list-style: none; padding: 0; }
  .exec-summary ul li { padding: 10px 0; border-bottom: 1px solid #f0f2f5; display: flex; align-items: flex-start; gap: 12px; }
  .exec-summary ul li:last-child { border-bottom: none; }
  .exec-summary .badge { min-width: 80px; text-align: center; border-radius: 6px; padding: 3px 8px; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; }
  .badge-red    { background: #fde8e8; color: #c0392b; }
  .badge-green  { background: #e8f5e9; color: #1b5e20; }
  .badge-blue   { background: #e3f0ff; color: #1565c0; }

  /* Tables */
  table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; margin-bottom: 16px; }
  th { background: #1a1a2e; color: #fff; padding: 10px 14px; text-align: left; font-size: 0.8rem; letter-spacing: 0.5px; text-transform: uppercase; }
  td { padding: 9px 14px; border-bottom: 1px solid #f0f2f5; font-size: 0.85rem; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #fafbfd; }
  .priority-high   { color: #c0392b; font-weight: 700; }
  .priority-med    { color: #b7791f; font-weight: 700; }
  .priority-low    { color: #555; }
  .fit-high   { background: #e8f5e9; color: #1b5e20; border-radius: 4px; padding: 2px 7px; font-size: 0.75rem; font-weight: 700; }
  .fit-med    { background: #fff8e1; color: #b7791f; border-radius: 4px; padding: 2px 7px; font-size: 0.75rem; font-weight: 700; }
  .fit-low    { background: #f5f5f5; color: #555; border-radius: 4px; padding: 2px 7px; font-size: 0.75rem; font-weight: 700; }

  /* Status pills */
  .status { border-radius: 10px; padding: 2px 9px; font-size: 0.73rem; font-weight: 700; display: inline-block; }
  .status-confirmed  { background: #e8f5e9; color: #1b5e20; }
  .status-accepted   { background: #e3f0ff; color: #1565c0; }
  .status-declined   { background: #fde8e8; color: #c0392b; }
  .status-pending    { background: #fff8e1; color: #b7791f; }
  .status-needs      { background: #fff3e0; color: #e65100; }

  /* Dashboard grid */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; margin-bottom: 24px; }
  .dash-tile { background: #fff; border-radius: 12px; padding: 18px 20px; border: 1px solid #e0e4ed; text-align: center; }
  .dash-tile .tile-num { font-size: 2rem; font-weight: 800; }
  .dash-tile .tile-label { font-size: 0.78rem; color: #777; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px; }
  .dash-red    .tile-num { color: #c0392b; }
  .dash-yellow .tile-num { color: #b7791f; }
  .dash-blue   .tile-num { color: #1565c0; }
  .dash-green  .tile-num { color: #1b5e20; }
  .dash-purple .tile-num { color: #6a1b9a; }
  .dash-gray   .tile-num { color: #555; }

  /* Top 3 */
  .top3 { background: linear-gradient(135deg, #0f3460, #1a1a2e); border-radius: 14px; padding: 28px 32px; color: #fff; }
  .top3 h2 { font-size: 1.1rem; margin-bottom: 18px; color: #a8c8ff; text-transform: uppercase; letter-spacing: 0.5px; }
  .top3 .item { display: flex; gap: 16px; align-items: flex-start; margin-bottom: 16px; }
  .top3 .num { background: #0f3460; border: 2px solid #4a90e2; border-radius: 50%; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; font-size: 1rem; font-weight: 800; color: #4a90e2; flex-shrink: 0; }
  .top3 .item-body strong { color: #fff; font-size: 0.95rem; }
  .top3 .item-body p { color: #a8b8d8; font-size: 0.83rem; margin-top: 3px; }

  /* Tags */
  .tag { display: inline-block; border-radius: 4px; padding: 1px 7px; font-size: 0.72rem; font-weight: 700; margin-right: 4px; }
  .tag-red    { background: #fde8e8; color: #c0392b; }
  .tag-yellow { background: #fff8e1; color: #b7791f; }
  .tag-green  { background: #e8f5e9; color: #1b5e20; }
  .tag-blue   { background: #e3f0ff; color: #1565c0; }
  .tag-gray   { background: #f0f0f0; color: #555; }
  .tag-purple { background: #f3e5ff; color: #6a1b9a; }

  /* Misc */
  .divider { height: 1px; background: #e0e4ed; margin: 8px 0; }
  .note { font-size: 0.78rem; color: #888; font-style: italic; margin-top: 6px; }
  .sub-header { font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.4px; color: #555; margin: 14px 0 6px; }
  .trash-group { background: #fff; border-radius: 10px; padding: 14px 18px; margin-bottom: 10px; border: 1px solid #e0e4ed; }
  .trash-group h4 { font-size: 0.88rem; font-weight: 700; margin-bottom: 8px; }
  .trash-restore h4 { color: #c0392b; }
  .trash-review  h4 { color: #b7791f; }
  .trash-delete  h4 { color: #555; }

  @media (max-width: 600px) {
    .header { padding: 22px 18px; }
    .header h1 { font-size: 1.4rem; }
    .dash-grid { grid-template-columns: repeat(2, 1fr); }
  }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════
     1. HEADER
═══════════════════════════════════════════════════ -->
<div class="header">
  <div class="subtitle">Executive Briefing — Prepared by Your Chief of Staff</div>
  <h1>Good Morning, Melissa ☀️</h1>
  <div class="header-meta">
    <div class="chip">📅 Friday, June 12, 2026</div>
    <div class="chip">📧 50 Emails Reviewed</div>
    <div class="chip">📆 9 Calendar Events</div>
    <div class="chip">🚨 3 Action Items Require Your Attention</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     2. EXECUTIVE SUMMARY
═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title red">⚡ Executive Summary</div>
  <div class="exec-summary">
    <ul>
      <li>
        <span class="badge badge-red">🚨 Risk</span>
        <span><strong>Prescription Delay + Insurance Issue:</strong> Duane Reade flagged an insurance problem with your medication order. Separately, Dr. Eric Hollander sent a new Rx for Dexedrine 15mg ER to Duane Reade. Confirm the insurance issue is resolved and that the new Rx has been received and filled.</span>
      </li>
      <li>
        <span class="badge badge-green">🎯 Opportunity</span>
        <span><strong>Strong VP/Head of People Job Leads + Monday Interview:</strong> Multiple alerts for VP People at Novo (LinkedIn × 2, Welcome to the Jungle), a Head of People (Global) invite from Jobright, and a Sr. Director HRBP at Scholar Rock. You have a confirmed SoFi interview at 2:30 PM on Monday, June 15 — prep is needed this weekend.</span>
      </li>
      <li>
        <span class="badge badge-blue">📆 Calendar</span>
        <span><strong>Packed Monday — Three Back-to-Back Commitments:</strong> Hair appointment 9:30–11:00 AM, SoFi Zoom interview 2:30–2:50 PM, and a 15-minute Zoom consultation with Netta Jenkins at 3:00 PM — all on Monday, June 15. Also: BofA transfer alert exceeded your set limit on account ending 7471 — review today.</span>
      </li>
    </ul>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     3. ACTION REQUIRED
═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title red">🔴 Action Required</div>

  <div class="card card-red">
    <div class="card-label red">🚨 Urgent — Medical</div>
    <div class="card-title">Prescription Delay: Insurance Issue at Duane Reade</div>
    <div class="card-row">
      <span class="card-meta"><strong>From:</strong> Duane Reade / Dr. Eric Hollander</span>
      <span class="card-meta"><strong>Date:</strong> Today, June 12</span>
    </div>
    <div class="divider"></div>
    <div class="card-meta"><strong>Why it matters:</strong> Your prescription order is delayed due to an insurance issue. Dr. Hollander has separately sent a new Rx for Dexedrine 15mg ER Spansules to Duane Reade. You need to confirm (a) the insurance issue is resolved, and (b) the new Rx has been received by the pharmacy and is being processed.</div>
    <div class="card-meta" style="margin-top:6px"><strong>Next step:</strong> Call Duane Reade pharmacy today to confirm receipt of Dr. Hollander's new Rx and get insurance issue resolved. If pharmacy cannot resolve, contact your insurance directly or consider transferring to Capsule (see promotional email from them today — they offer free delivery).</div>
    <div class="card-meta" style="margin-top:6px"><strong>Due:</strong> Today, June 12, 2026</div>
  </div>

  <div class="card card-red">
    <div class="card-label red">🚨 Urgent — Financial Alert</div>
    <div class="card-title">Bank of America: Transfer Exceeded Your Set Limit — Account Ending 7471</div>
    <div class="card-row">
      <span class="card-meta"><strong>From:</strong> Bank of America</span>
      <span class="card-meta"><strong>Amount:</strong> $400+</span>
      <span class="card-meta"><strong>Date:</strong> Today, June 12</span>
    </div>
    <div class="divider"></div>
    <div class="card-meta"><strong>Why it matters:</strong> An online transfer exceeded the threshold you set on your account. This may be routine but warrants verification that the transfer was authorized and that no unauthorized activity occurred.</div>
    <div class="card-meta" style="margin-top:6px"><strong>Next step:</strong> Log in to Bank of America online banking today to review the transfer. If unauthorized, contact BofA fraud immediately at 1-800-432-1000. If authorized, consider adjusting your alert threshold.</div>
    <div class="card-meta" style="margin-top:6px"><strong>Due:</strong> Today, June 12, 2026</div>
  </div>

  <div class="card card-red">
    <div class="card-label red">⚠️ Technical — GitHub Workflow Failure</div>
    <div class="card-title">Daily Briefing GitHub Action Failed: "webhooks" Job (Run 03b4338)</div>
    <div class="card-row">
      <span class="card-meta"><strong>From:</strong> GitHub (missophs/daily-briefing)</span>
      <span class="card-meta"><strong>Date:</strong> Today, June 12, 1:21 PM</span>
    </div>
    <div class="divider"></div>
    <div class="card-meta"><strong>Why it matters:</strong> Your automated Daily Briefing workflow failed — all jobs failed on the "webhooks" step. This could mean your briefing automation did not run completely today and may impact future automated output.</div>
    <div class="card-meta" style="margin-top:6px"><strong>Next step:</strong> Review the failed workflow run on GitHub (missophs/daily-briefing). Check the webhook configuration, secrets, or API keys that may have expired. Re-run or fix before the weekend.</div>
    <div class="card-meta" style="margin-top:6px"><strong>Due:</strong> Today or by Saturday, June 13</div>
  </div>

  <div class="card card-yellow">
    <div class="card-label yellow">📋 RSVP Needed</div>
    <div class="card-title">HR Networking & Job Search Group — Zoom (June 17) + Open Office Hours (June 18)</div>
    <div class="card-row">
      <span class="card-meta"><strong>Status:</strong> needsAction (no RSVP on both events)</span>
      <span class="card-meta"><strong>Date:</strong> Wed June 17 @ 12:00 PM & Thu June 18 @ 12:00 PM</span>
    </div>
    <div class="divider"></div>
    <div class="card-meta"><strong>Why it matters:</strong> Both events are already on your calendar with pending RSVP status. These are key networking opportunities during your job search. Hosts and co-attendees may be tracking RSVPs.</div>
    <div class="card-meta" style="margin-top:6px"><strong>Next step:</strong> Accept or decline both calendar invites before the weekend.</div>
    <div class="card-meta" style="margin-top:6px"><strong>Due:</strong> By Sunday, June 14</div>
  </div>

  <div class="card card-yellow">
    <div class="card-label yellow">📦 Personal</div>
    <div class="card-title">Package Arrived at 303 East 83rd — Pick Up Required</div>
    <div class="card-row">
      <span class="card-meta"><strong>From:</strong> 303 East 83rd (Equity Apartments)</span>
      <span class="card-meta"><strong>Carrier:</strong> UPS — Apartment 03H</span>
      <span class="card-meta"><strong>Date:</strong> Today, June 12</span>
    </div>
    <div class="divider"></div>
    <div class="card-meta"><strong>Next step:</strong> Stop by the building's package room to retrieve your UPS package.</div>
    <div class="card-meta" style="margin-top:6px"><strong>Due:</strong> Today or this weekend</div>
  </div>

  <div class="card card-green">
    <div class="card-label green">💼 Job Search — Interview Prep</div>
    <div class="card-title">SoFi Zoom Screen: Principal People Business Partner, Finance — Monday 2:30 PM</div>
    <div class="card-row">
      <span class="card-meta"><strong>Date:</strong> Monday, June 15 @ 2:30–2:50 PM ET</span>
      <span class="card-meta"><strong>Format:</strong> Zoom screen</span>
    </div>
    <div class="divider"></div>
    <div class="card-meta"><strong>Why it matters:</strong> Confirmed interview this coming Monday. Prep time is limited — the weekend is your only window.</div>
    <div class="card-meta" style="margin-top:6px"><strong>Next step:</strong> Research SoFi's people strategy, recent news, and Finance HRBP scope this weekend. Prepare STAR examples. Confirm the Zoom link from the calendar invite description.</div>
    <div class="card-meta" style="margin-top:6px"><strong>Due:</strong> Before Monday, June 15 @ 2:30 PM</div>
  </div>

  <div class="card card-green">
    <div class="card-label green">💼 Job Search — Outreach</div>
    <div class="card-title">Review & Apply: VP People at Novo + Head of People (Global) — Jobright Invite</div>
    <div class="card-row">
      <span class="card-meta"><strong>Sources:</strong> LinkedIn × 2, Welcome to the Jungle, Jobright (Eric)</span>
      <span class="card-meta"><strong>Date:</strong> Today, June 12</span>
    </div>
    <div class="divider"></div>
    <div class="card-meta"><strong>Why it matters:</strong> Multiple platforms surfaced the VP People at Novo role today — a venture-backed fintech for small businesses. Jobright also sent a personalized invite for a Head of People (Global) role based on your profile (Cprime, etc.). Both appear high-fit for your background.</div>
    <div class="card-meta" style="margin-top:6px"><strong>Next step:</strong> Review both roles this weekend. Apply or respond to Jobright before Monday.</div>
    <div class="card-meta" style="margin-top:6px"><strong>Due:</strong> By Sunday, June 14</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     4. FULL 7-DAY CALENDAR
═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title blue">📆 Full 7-Day Calendar</div>

  <!-- Friday June 12 -->
  <div class="sub-header">Friday, June 12 (Today)</div>
  <div class="card card-gray">
    <div class="card-meta"><em>No calendar events scheduled for today. Focus on email triage, prescription follow-up, BofA alert review, and GitHub fix.</em></div>
  </div>

  <!-- Saturday June 13 -->
  <div class="sub-header">Saturday, June 13</div>
  <div class="card card-gray">
    <div class="card-meta"><em>No calendar events. Recommended: SoFi interview prep, VP People at Novo application research.</em></div>
  </div>

  <!-- Sunday June 14 -->
  <div class="sub-header">Sunday, June 14</div>
  <div class="card card-gray">
    <div class="card-meta"><em>No calendar events. Final SoFi prep day. RSVP to networking Zoom events (June 17 & 18) before tonight.</em></div>
  </div>

  <!-- Monday June 15 -->
  <div class="sub-header">Monday, June 15 ⚠️ Busy Day</div>

  <div class="card card-blue">
    <div class="card-label blue">9:30 AM – 11:00 AM</div>
    <div class="card-title">💇 Hair Appointment — Elle at UMI Salon</div>
    <div class="card-row">
      <span class="status status-confirmed">Confirmed</span>
      <span class="card-meta">Single Process with Blowout · Elle M</span>
    </div>
    <div class="card-meta"><strong>Location:</strong> 37 West 20th Suite 1107, New York, NY 10011</div>
    <div class="card-meta"><strong>Prep:</strong> Allow extra travel time downtown. Appointment ends at 11:00 AM, leaving 3.5 hours before your interview.</div>
    <div class="card-meta"><strong>Manage:</strong> <a href="https://elleatumi.glossgenius.com/a/f2ab675761428d8ce73a61087c11ef34fd0c" style="color:#1565c0">Modify appointment</a></div>
  </div>

  <div class="card card-green">
    <div class="card-label green">2:30 PM – 2:50 PM</div>
    <div class="card-title">💼 Interview — SoFi: Principal People Business Partner, Finance</div>
    <div class="card-row">
      <span class="status status-confirmed">Confirmed</span>
      <span class="card-meta">Zoom Screen · 20 minutes</span>
    </div>
    <div class="card-meta"><strong>Format:</strong> Zoom (link in calendar invite description)</div>
    <div class="card-meta"><strong>Prep needed:</strong> ⚠️ HIGH. Research SoFi Finance org, HRBP scope, prepare STAR examples. Dress professionally even for Zoom. Test audio/video beforehand.</div>
    <div class="card-meta"><strong>Buffer:</strong> 3.5 hrs gap after salon — use for lunch, prep, and test connection.</div>
  </div>

  <div class="card card-blue">
    <div class="card-label blue">3:00 PM – 3:15 PM</div>
    <div class="card-title">🤝 Zoom Consultation — Netta Jenkins (HIC Consult)</div>
    <div class="card-row">
      <span class="status status-accepted">Accepted</span>
      <span class="card-meta">15-min · netta@hicconsult.com</span>
    </div>
    <div class="card-meta"><strong>Location:</strong> <a href="https://us06web.zoom.us/j/5224221004?pwd=UU5YNmlFckpjQnlzc2FDMHFlNUhhUT09" style="color:#1565c0">Zoom Link</a> · Password: 424726</div>
    <div class="card-meta"><strong>⚠️ Conflict Warning:</strong> Begins only 10 minutes after SoFi interview ends. Keep SoFi wrap-up brief. Have this Zoom link ready to launch immediately.</div>
    <div class="card-meta"><strong>Prep:</strong> Know what you want from this consultation (career coaching? referral? resume review?). Have 1–2 questions ready.</div>
  </div>

  <!-- Tuesday June 16 -->
  <div class="sub-header">Tuesday, June 16</div>

  <div class="card card-blue">
    <div class="card-label blue">10:00 AM – 11:00 AM</div>
    <div class="card-title">🐾 Vet Appointment</div>
    <div class="card-row">
      <span class="status status-confirmed">Confirmed</span>
    </div>
    <div class="card-meta"><strong>Location:</strong> Not specified in calendar</div>
    <div class="card-meta"><strong>Prep:</strong> Confirm location and bring any pet records if needed. Allow travel time.</div>
  </div>

  <!-- Wednesday June 17 -->
  <div class="sub-header">Wednesday, June 17</div>

  <div class="card card-blue">
    <div class="card-label blue">10:45 AM – 11:45 AM</div>
    <div class="card-title">🦷 Dental Cleaning — Dr. Deutch</div>
    <div class="card-row">
      <span class="status status-confirmed">Confirmed</span>
    </div>
    <div class="card-meta"><strong>Location:</strong> Not specified — confirm address before Wednesday.</div>
    <div class="card-meta"><strong>Prep:</strong> No special prep noted. Ends at 11:45 — 15 min buffer before networking Zoom at 12:00.</div>
  </div>

  <div class="card card-purple">
    <div class="card-label purple">12:00 PM – 1:30 PM</div>
    <div class="card-title">🤝 HR Networking & Job Search Group — Zoom Session 2</div>
    <div class="card-row">
      <span class="status status-needs">⚠️ RSVP Needed</span>
      <span class="card-meta">~170+ attendees</span>
    </div>
    <div class="card-meta"><strong>Location:</strong> <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" style="color:#6a1b9a">Zoom Link</a></div>
    <div class="card-meta"><strong>⚠️ RSVP PENDING — Accept or Decline before Sunday.</strong></div>
    <div class="card-meta"><strong>⚠️ Conflict Warning:</strong> Dental cleaning ends at 11:45 AM — only 15 minutes before this Zoom. Plan to join from home/phone if needed.</div>
    <div class="card-meta"><strong>Prep:</strong> Review team guidelines and update your pitch. Large group networking session — be ready to introduce yourself.</div>
  </div>

  <div class="card card-purple">
    <div class="card-label purple">12:00 PM – 1:30 PM</div>
    <div class="card-title">🤝 Network (Personal Block)</div>
    <div class="card-row">
      <span class="status status-confirmed">Confirmed</span>
    </div>
    <div class="card-meta"><em>Note: This overlaps with the HR Networking Zoom above — appears to be a personal reminder block for the same time window.</em></div>
  </div>

  <!-- Thursday June 18 -->
  <div class="sub-header">Thursday, June 18</div>

  <div class="card card-gray">
    <div class="card-label gray">9:00 AM – 10:30 AM</div>
    <div class="card-title">❌ Executive Roundtable (Declined)</div>
    <div class="card-row">
      <span class="status status-declined">Declined</span>
      <span class="card-meta">Hosted by John Madigan</span>
    </div>
    <div class="card-meta"><strong>Location:</strong> <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" style="color:#555">Zoom Link</a> · Meeting ID: 207 786 667 · PW: 205454</div>
    <div class="card-meta"><strong>Status:</strong> You have already declined this event. No action needed unless you wish to reconsider.</div>
  </div>

  <div class="card card-purple">
    <div class="card-label purple">12:00 PM – 1:00 PM</div>
    <div class="card-title">🤝 HR Networking & Job Search: Open Office Hours — Zoom Session 2</div>
    <div class="card-row">
      <span class="status status-needs">⚠️ RSVP Needed</span>
      <span class="card-meta">~170+ attendees</span>
    </div>
    <div class="card-meta"><strong>Location:</strong> <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" style="color:#6a1b9a">Zoom Link</a></div>
    <div class="card-meta"><strong>Note:</strong> No AI notetaking tools per host instructions. Open discussion format — great for informal networking and job search support.</div>
    <div class="card-meta"><strong>⚠️ RSVP PENDING — Accept or Decline before Sunday.</strong></div>
  </div>

  <!-- Friday June 19 -->
  <div class="sub-header">Friday, June 19</div>
  <div class="card card-gray">
    <div class="card-meta"><em>No calendar events. Available for follow-ups from the week's interviews and networking.</em></div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════
     5. JOB SEARCH & INTERVIEW PIPELINE
═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title green">💼 Job Search & Interview Pipeline</div>
  <table>
    <thead>
      <tr>
        <th>Role</th>
        <th>Company</th>
        <th>Source</th>
        <th>Fit</th>
        <th>Status</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Principal People Business Partner, Finance</strong></td>
        <td>SoFi</td>
        <td>Recruiter (Calendar)</td>
        <td><span class="fit-high">HIGH</span></td>
        <td><span class="status status-confirmed">Interview Mon 6/15 2:30 PM</span></td>
        <td>Prep this weekend. Confirm Zoom link.</td>
      </tr>
      <tr>
        <td><strong>Vice President, People</strong></td>
        <td>Novo</td>
        <td>LinkedIn Alerts × 2 + Welcome to the Jungle</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>3 alerts today — not yet applied</td>
        <td>Review & apply this weekend.</td>
      </tr>
      <tr>
        <td><strong>Head of People (Global)</strong></td>
        <td>TBD</td>
        <td>Jobright (Eric) — Personalized Invite</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>Invited — not yet responded</td>
        <td>Reply to Eric at Jobright before Monday.</td>
      </tr>
      <tr>
        <td><strong>Sr. Director, HR Business Partner (US & Global Ops)</strong></td>
        <td>Scholar Rock</td>
        <td>LinkedIn Jobs Alert</td>
        <td><span class="fit-med">MEDIUM</span></td>
        <td>Saved job — not applied</td>
        <td>Review role scope; apply if strong fit.</td>
      </tr>
      <tr>
        <td><strong>15-Min Zoom Consultation</strong></td>
        <td>HIC Consult (Netta Jenkins)</td>
        <td>Calendar — Accepted</td>
        <td><span class="fit-high">HIGH</span></td>
        <td><span class="status status-accepted">Mon 6/15 3:00 PM</span></td>
        <td>Prepare 1–2 specific questions for Netta.</td>
      </tr>
      <tr>
        <td><strong>HR Networking Group Session</strong></td>
        <td>HR Networking & Job Search</td>
        <td>Calendar — RSVP Pending</td>
        <td><span class="fit-med">MEDIUM</span></td>
        <td><span class="status status-needs">Wed 6/17 12:00 PM — RSVP Needed</span></td>
        <td>RSVP by Sunday. Large peer group opportunity.</td>
      </tr>
      <tr>
        <td><strong>Open Office Hours — Job Search Support</strong></td>
        <td>HR Networking & Job Search</td>
        <td>Calendar — RSVP Pending</td>
        <td><span class="fit-med">MEDIUM</span></td>
        <td><span class="status status-needs">Thu 6/18 12:00 PM — RSVP Needed</span></td>
        <td>RSVP by Sunday.</td>
      </tr>
      <tr>
        <td><strong>Daily Job Search Sweep (Automated)</strong></td>
        <td>Self (melissaw212 → melissahr212)</td>
        <td>Gmail — Self-sent (Run 2026-06-12)</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>17 results (Exa + Indeed MCP + Dice MCP)</td>
        <td>Review sweep results in melissahr212 inbox.</td>
      </tr>
      <tr>
        <td><strong>HR Search PM Automated Run #27434092039</strong></td>
        <td>Self (GitHub Actions)</td>
        <td>Gmail — Self-sent</td>
        <td><span class="fit-med">MEDIUM</span></td>
        <td>18 results (Exa 2 + Apify 16)</td>
        <td>Review results. Note: workflow also failed today (GitHub alert).</td>
      </tr>
      <tr>
        <td><strong>Remote & Hybrid Hiring Research</strong></td>
        <td>Mobius Engine Hub (Ashwin)</td>
        <td>Email — Not in inbox</td>
        <td><span class="fit-low">LOW</span></td>
        <td>Promo email with PROMO15 discount</td>
        <td>Review research publication; ignore promo offer.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════
     6. FULL EMAIL REVIEW BY CATEGORY
═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title gray">📂 Full Email Review by Category</div>

  <!-- Security / Risk -->
  <div class="card card-red">
    <div class="card-label red">🔒 Security / Risk — 2 Emails</div>
    <div class="card-title">BofA Transfer Alert + GitHub Workflow Failure</div>
    <div class="card-meta"><strong>Senders:</strong> Bank of America · GitHub (missophs)</div>
    <div class="card-meta"><strong>Summary:</strong> (1) BofA flagged an online transfer over your set limit on account ending 7471 — $400+ amount. (2) GitHub notified you that all jobs in your Daily Briefing workflow failed on the "webhooks" step (run 03b4338).</div>
    <div class="card-meta"><strong>Action:</strong> Review BofA account NOW. Fix GitHub workflow before weekend. Both are unread and require action today.</div>
  </div>

  <!-- Medical / Health -->
  <div class="card card-red">
    <div class="card-label red">💊 Medical / Health — 3 Emails</div>
    <div class="card-title">Prescription Delay, New Rx from Dr. Hollander, Capsule Pharmacy Offer</div>
    <div class="card-meta"><strong>Senders:</strong> Duane Reade · Eric Hollander MD · Capsule</div>
    <div class="card-meta"><strong>Summary:</strong> (1) Duane Reade flagged an insurance issue delaying your prescription. (2) Dr. Hollander replied that he sent a new Rx for Dexedrine 15mg ER Spansules to Duane Reade. (3) Capsule pharmacy marketed free delivery as an alternative pharmacy option.</div>
    <div class="card-meta"><strong>Action:</strong> Call Duane Reade today. Capsule email — keep for reference as a backup pharmacy option if insurance issues persist.</div>
  </div>

  <!-- Financial / Billing -->
  <div class="card card-yellow">
    <div class="card-label yellow">💳 Financial / Billing — 1 Email</div>
    <div class="card-title">BofA Transfer Alert (already noted in Security section — cross-referenced)</div>
    <div class="card-meta"><strong>Note:</strong> Counted once under Security/Risk. See above.</div>
  </div>

  <!-- Job Search -->
  <div class="card card-green">
    <div class="card-label green">💼 Job Search — 5 Emails</div>
    <div class="card-title">Alerts, Interviews, Automated Sweeps, and Invitations</div>
    <div class="card-meta"><strong>Senders:</strong> LinkedIn (VP People at Novo × 2) · Welcome to the Jungle (VP People at Novo) · LinkedIn (Sr. Director HRBP Scholar Rock) · Jobright/Eric (Head of People Global)</div>
    <div class="card-meta"><strong>Summary:</strong> VP People at Novo surfaced on 3 platforms today. Sr. Director HRBP at Scholar Rock flagged as a saved job. Jobright sent a personalized invitation for Head of People (Global) based on your profile including Cprime experience.</div>
    <div class="card-meta"><strong>Action:</strong> Apply to Novo VP this weekend. Respond to Jobright's Eric. Review Scholar Rock role fit.</div>
  </div>

  <!-- Personal (self-sent) -->
  <div class="card card-blue">
    <div class="card-label blue">📋 Personal / Self-Sent — 3 Emails</div>
    <div class="card-title">Automated Job Search Reports + Personal Draft</div>
    <div class="card-meta"><strong>Senders:</strong> melissa (melissaw212 → melissahr212) Daily Job Search Sweep · melissaw212@gmail.com HR Search PM Run #27434092039 · Melissa W (blank subject, snippet: "Second honeymoon")</div>
    <div class="card-meta"><strong>Summary:</strong> Two automated job search reports were generated and sent to yourself. One personal note/draft with the text "Second honeymoon" — likely a personal reminder or draft email.</div>
    <div class="card-meta"><strong>Action:</strong> Review job search sweep results. "Second honeymoon" draft — confirm this was intentional or follow up if needed.</div>
  </div>

  <!-- Recruiters / Networking -->
  <div class="card card-purple">
    <div class="card-label purple">🤝 Recruiters / Networking — 2 Emails</div>
    <div class="card-title">Mobius Engine Hub + Waldo's Rescue (Foster)</div>
    <div class="card-meta"><strong>Senders:</strong> Ashwin at Mobius Engine Hub · Andi at Waldo's Rescue</div>
    <div class="card-meta"><strong>Summary:</strong> Ashwin sent research on remote/hybrid hiring in 2026 with a job application service pitch. Andi from Waldo's Rescue asked if you can foster a dog this week (not in inbox — likely filtered).</div>
    <div class="card-meta"><strong>Action:</strong> Mobius email — read the research, ignore the promo. Waldo's Rescue — respond if interested in fostering this weekend.</div>
  </div>

  <!-- Professional Development -->
  <div class="card card-purple">
    <div class="card-label purple">📚 Professional Development — 2 Emails</div>
    <div class="card-title">Transform Community Digest + HRinsidr Newsletter (in Trash)</div>
    <div class="card-meta"><strong>Senders:</strong> Transform Community · HRinsidr (Camille)</div>
    <div class="card-meta"><strong>Summary:</strong> Transform Community digest covers people strategy keynotes, HR team growth, and employee enablement. HRinsidr newsletter focuses on emotional intelligence and decision-making in the workplace (currently in Trash).</div>
    <div class="card-meta"><strong>Action:</strong> Transform — read when time permits. HRinsidr — restore from Trash if valuable; unsubscribe if not.</div>
  </div>

  <!-- Newsletters / Subscriptions -->
  <div class="card card-purple">
    <div class="card-label purple">📰 Newsletters / Subscriptions — 4 Emails</div>
    <div class="card-title">Techpresso, The Futurist, Meidas+, Nextdoor (×2)</div>
    <div class="card-meta"><strong>Senders:</strong> Techpresso (SpaceX IPO × 3 — duplicates) · The Futurist (in Trash) · Meidas+ Friday News (in Trash) · Nextdoor Trending (×2 — duplicate delivery, Apple relay)</div>
    <div class="card-meta"><strong>Summary:</strong> Techpresso sent 3 copies of the same SpaceX IPO newsletter — possible delivery issue. The Futurist and Meidas+ are in Trash. Nextdoor sent the same trending story to two email addresses (your main + Apple relay).</div>
    <div class="card-meta"><strong>Action:</strong> Read one Techpresso copy; delete duplicates. Restore Futurist or Meidas+ from Trash if desired. Unsubscribe Nextdoor from Apple relay alias to reduce duplicates.</div>
  </div>

  <!-- Calendar / Events -->
  <div class="card card-blue">
    <div class="card-label blue">📅 Calendar / Events — 1 Email</div>
    <div class="card-title">BRC Volunteer Update — Meal Service (June 13–21) — In Trash</div>
    <div class="card-meta"><strong>Sender:</strong> Rick Akin, BRC</div>
    <div class="card-meta"><strong>Summary:</strong> BRC (Bowery Residents' Committee) is seeking meal service volunteers Saturday June 13 through Sunday June 21.</div>
    <div class="card-meta"><strong>Action:</strong> If you volunteer with BRC, restore from Trash and review scheduling. Otherwise safe to delete.</div>
  </div>

  <!-- Promotional / Retail -->
  <div class="card card-gray">
    <div class="card-label gray">🛍️ Promotional / Retail — 19 Emails</div>
    <div class="card-title">Fashion, Beauty, Food, Lifestyle & More (see full Promotional section below)</div>
    <div class="card-meta"><strong>Senders:</strong> NBC · Chick-fil-A · Warby Parker · StackSocial · SHEIN (Trash) · Ulta Beauty (Trash) · Old Navy (Trash) · Photoroom (Trash) · Seamless · Amazon Prime Day (Trash) · Quince · Macy's · Total Wine (Trash) · Gap Factory · Halara · Paul Labrecque · e.l.f. Cosmetics · GU USA · Chip City · INNBEAUTY PROJECT · SHRM (Trash)</div>
    <div class="card-meta"><strong>Action:</strong> See Promotional / Retail Summary section below.</div>
  </div>

  <!-- Spam / Suspicious -->
  <div class="card card-red">
    <div class="card-label red">⚠️ Spam / Suspicious — 1 Email</div>
    <div class="card-title">"Ozempic by DirectMeds" — Suspicious Sender</div>
    <div class="card-meta"><strong>From:</strong> Random_com[5,9,l]@mstltcmuekjvttwefsskaagmcm.us (spoofed)</div>
    <div class="card-meta"><strong>Subject:</strong> melissaw212: What If You Could Lose Weight Effortlessly?</div>
    <div class="card-meta"><strong>Action:</strong> Do NOT click any links. Mark as spam and delete. The sender domain is clearly malicious/spoofed. Your email address was exposed in subject line — monitor for further phishing attempts.</div>
  </div>

  <!-- Safe to Delete / Ignore -->
  <div class="card card-gray">
    <div class="card-label gray">🗑️ Safe to Delete / Ignore — 5 Emails</div>
    <div class="card-title">Duplicate Newsletters, Irrelevant Offers, Spam</div>
    <div class="card-meta"><strong>Items:</strong> Techpresso duplicate × 2 · Nextdoor duplicate (Apple relay) · Ozempic spam · NYC Whine & Dine Networking event (Trash) · Amazon Prime Day sweepstakes (Trash) · CoolDeep AI newsletter (Trash)</div>
    <div class="card-meta"><strong>Action:</strong> Delete all. Mark spam as appropriate.</div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════
     7. TRASH REVIEW
═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title red">🗑️ Trash Review</div>
  <p class="note" style="margin-bottom:12px;">11 emails were found in Trash. Reviewed below across three groups.</p>

  <div class="trash-group trash-restore">
    <h4>♻️ Restore — Consider Recovering These</h4>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Why Restore?</th></tr></thead>
      <tbody>
        <tr>
          <td>Rick Akin, BRC</td>
          <td>Volunteer Update — Meal Service Jun 13–21</td>
          <td>If you are a BRC volunteer, this contains scheduling details for next week's meal service.</td>
        </tr>
        <tr>
          <td>HRinsidr (Camille)</td>
          <td>Melissa, do your emotions show up at work?</td>
          <td>HR professional development content on emotional intelligence — relevant to your field and job search narrative.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="trash-group trash-review">
    <h4>🔍 Review Before Deleting</h4>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Notes</th></tr></thead>
      <tbody>
        <tr>
          <td>Meidas+ (Substack)</td>
          <td>Friday News Updates: What's the Deal? — 6/12/26</td>
          <td>News/political newsletter — review if you follow this publication, otherwise delete and unsubscribe.</td>
        </tr>
        <tr>
          <td>The Futurist</td>
          <td>Spidey can't fix this</td>
          <td>Tech/innovation newsletter — skim headline. Unsubscribe if not reading regularly.</td>
        </tr>
        <tr>
          <td>NYC Whine & Dine Networking</td>
          <td>W&D NY: NYC 6/16 (Special Rooftop) & Long Island 6/17</td>
          <td>Networking event this coming Tuesday — if you want to attend the 6/16 rooftop networking event in NYC, restore and RSVP. Otherwise delete.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="trash-group trash-delete">
    <h4>✅ Safe to Delete — Permanently</h4>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Reason</th></tr></thead>
      <tbody>
        <tr>
          <td>SHEIN</td>
          <td>📞 Your Cart Called...</td>
          <td>Retail promotional. No action needed.</td>
        </tr>
        <tr>
          <td>Ulta Beauty Orders</td>
          <td>So, how'd we do?</td>
          <td>Post-purchase survey. No urgency.</td>
        </tr>
        <tr>
          <td>Old Navy</td>
          <td>EXTRA 30% OFF + $16 shirts</td>
          <td>Retail promo. Low priority.</td>
        </tr>
        <tr>
          <td>Photoroom</td>
          <td>Discover what we built for product fidelity</td>
          <td>Product update email. Irrelevant to current needs.</td>
        </tr>
        <tr>
          <td>Amazon Prime Day</td>
          <td>Enter for a chance to win a $1,000 Gift Card</td>
          <td>Sweepstakes marketing. Delete.</td>
        </tr>
        <tr>
          <td>Total Wine & More</td>
          <td>Hello, Summer Flavors!</td>
          <td>Retail promo. Delete.</td>
        </tr>
        <tr>
          <td>CoolDeep AI</td>
          <td>Claude just got access to your Gmail, Drive…</td>
          <td>Clickbait AI newsletter. Delete and unsubscribe.</td>
        </tr>
        <tr>
          <td>SHRM Membership</td>
          <td>Your FREE Bogg Bag is waiting</td>
          <td>Membership promo with gift incentive. Delete unless considering SHRM membership.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     8. PROMOTIONAL / RETAIL SUMMARY
═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title gray">🛍️ Promotional / Retail Summary</div>
  <table>
    <thead>
      <tr>
        <th>Brand / Sender</th>
        <th>Count</th>
        <th>Subject / Theme</th>
        <th>Inbox / Trash</th>
        <th>Recommendation</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>NBC</td>
        <td>1</td>
        <td>Stream Love Island, AGT and more</td>
        <td>Inbox</td>
        <td><span class="tag tag-gray">Ignore</span> Low priority entertainment promo.</td>
      </tr>
      <tr>
        <td>Chick-fil-A</td>
        <td>1</td>
        <td>Planning something special? (catering pitch)</td>
        <td>Inbox</td>
        <td><span class="tag tag-gray">Delete</span> Unless planning a catered event.</td>
      </tr>
      <tr>
        <td>Warby Parker</td>
        <td>1</td>
        <td>Bestselling sunglasses</td>
        <td>Inbox</td>
        <td><span class="tag tag-yellow">Review</span> If you need sunglasses.</td>
      </tr>
      <tr>
        <td>StackSocial</td>
        <td>1</td>
        <td>Lifetime cloud storage (Internxt) — cut Google Drive</td>
        <td>Inbox</td>
        <td><span class="tag tag-gray">Delete</span> Likely unnecessary given Google Workspace use.</td>
      </tr>
      <tr>
        <td>SHEIN</td>
        <td>1</td>
        <td>Cart abandonment</td>
        <td>Trash ✓</td>
        <td><span class="tag tag-gray">Delete</span> Already in Trash.</td>
      </tr>
      <tr>
        <td>Ulta Beauty</td>
        <td>1</td>
        <td>Post-purchase survey</td>
        <td>Trash ✓</td>
        <td><span class="tag tag-gray">Delete</span> Already in Trash.</td>
      </tr>
      <tr>
        <td>Old Navy</td>
        <td>1</td>
        <td>Extra 30% off + $16 shirts</td>
        <td>Trash ✓</td>
        <td><span class="tag tag-gray">Delete</span> Already in Trash.</td>
      </tr>
      <tr>
        <td>Photoroom</td>
        <td>1</td>
        <td>Product fidelity features update</td>
        <td>Trash ✓</td>
        <td><span class="tag tag-gray">Delete</span> Not relevant currently.</td>
      </tr>
      <tr>
        <td>Seamless / Grubhub</td>
        <td>1</td>
        <td>50% off Grubhub+ / 7-day free trial</td>
        <td>Not in inbox</td>
        <td><span class="tag tag-yellow">Review</span> If you use food delivery frequently.</td>
      </tr>
      <tr>
        <td>Amazon Prime Day</td>
        <td>1</td>
        <td>$1,000 gift card sweepstakes + early deals</td>
        <td>Trash ✓</td>
        <td><span class="tag tag-gray">Delete</span> Sweepstakes spam.</td>
      </tr>
      <tr>
        <td>Quince</td>
        <td>1</td>
        <td>Vacation capsule wardrobe by Kate Young</td>
        <td>Not in inbox</td>
        <td><span class="tag tag-yellow">Review</span> If planning travel ("second honeymoon"?).</td>
      </tr>
      <tr>
        <td>Macy's</td>
        <td>1</td>
        <td>Earn Star Money — Michael Kors, MFK, Friends & Family</td>
        <td>Not in inbox</td>
        <td><span class="tag tag-yellow">Review</span> If you shop Macy's regularly.</td>
      </tr>
      <tr>
        <td>Total Wine & More</td>
        <td>1</td>
        <td>Summer flavors — pool, picnics</td>
        <td>Trash ✓</td>
        <td><span class="tag tag-gray">Delete</span> Already in Trash.</td>
      </tr>
      <tr>
        <td>Gap Factory</td>
        <td>1</td>
        <td>Last chance: extra 10% + bonus 10% + 75% off</td>
        <td>Not in inbox</td>
        <td><span class="tag tag-gray">Ignore</span> Sale-based retail promo.</td>
      </tr>
      <tr>
        <td>Halara</td>
        <td>1</td>
        <td>Activewear tops — up to 60% off</td>
        <td>Not in inbox</td>
        <td><span class="tag tag-gray">Ignore</span> Low priority.</td>
      </tr>
      <tr>
        <td>Paul Labrecque Salon</td>
        <td>1</td>
        <td>Father's Day Edit — luxury gifts</td>
        <td>Not in inbox</td>
        <td><span class="tag tag-yellow">Review</span> Father's Day is June 21 — if buying a gift, browse.</td>
      </tr>
      <tr>
        <td>e.l.f. Cosmetics</td>
        <td>1</td>
        <td>Halo Glow Skin Tint SPF 50 summer launch</td>
        <td>Not in inbox</td>
        <td><span class="tag tag-yellow">Review</span> If interested in summer skincare.</td>
      </tr>
      <tr>
        <td>GU USA</td>
        <td>1</td>
        <td>Summer style starting at $9.90</td>
        <td>Not in inbox</td>
        <td><span class="tag tag-gray">Ignore</span> Low priority retail.</td>
      </tr>
      <tr>
        <td>Chip City</td>
        <td>1</td>
        <td>Free
<hr>
<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Job Search / Recruiters</td><td>8</td></tr>
<tr><td>Medical / Health</td><td>5</td></tr>
<tr><td>Other / Review</td><td>26</td></tr>
<tr><td>Professional Development / Newsletters</td><td>1</td></tr>
<tr><td>Promotional / Retail</td><td>9</td></tr>
<tr><td>Security / Risk</td><td>1</td></tr>
</table>
<p><strong>Audit Note:</strong> Every fetched email was reviewed and assigned to one category. Trash emails were included in review. Promotional and low-value emails were accounted for but deprioritized.</p>

