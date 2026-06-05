<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing – Melissa | Friday, June 5, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; }
  .wrapper { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 36px 40px 28px; margin-bottom: 24px; }
  .header h1 { font-size: 2rem; font-weight: 700; letter-spacing: 0.5px; }
  .header .sub { font-size: 1rem; color: #a8c0e8; margin-top: 6px; }
  .header .meta-row { display: flex; gap: 32px; margin-top: 20px; flex-wrap: wrap; }
  .header .meta-box { background: rgba(255,255,255,0.1); border-radius: 8px; padding: 10px 20px; text-align: center; }
  .header .meta-box .val { font-size: 1.6rem; font-weight: 700; color: #f0c040; }
  .header .meta-box .lbl { font-size: 0.75rem; color: #aac4e8; text-transform: uppercase; letter-spacing: 1px; }

  /* SECTION */
  .section { background: #fff; border-radius: 12px; padding: 24px 28px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .section-title { font-size: 1.15rem; font-weight: 700; margin-bottom: 16px; padding-bottom: 8px; border-bottom: 2px solid #e5e7eb; display: flex; align-items: center; gap: 8px; }

  /* COLOR BANDS */
  .band-red { border-left: 5px solid #dc2626; }
  .band-yellow { border-left: 5px solid #d97706; }
  .band-blue { border-left: 5px solid #2563eb; }
  .band-green { border-left: 5px solid #16a34a; }
  .band-purple { border-left: 5px solid #7c3aed; }
  .band-gray { border-left: 5px solid #9ca3af; }

  /* PILLS */
  .pill { display: inline-block; border-radius: 20px; padding: 2px 10px; font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
  .pill-red { background: #fee2e2; color: #b91c1c; }
  .pill-yellow { background: #fef3c7; color: #92400e; }
  .pill-blue { background: #dbeafe; color: #1d4ed8; }
  .pill-green { background: #dcfce7; color: #166534; }
  .pill-purple { background: #ede9fe; color: #5b21b6; }
  .pill-gray { background: #f3f4f6; color: #6b7280; }
  .pill-orange { background: #ffedd5; color: #c2410c; }

  /* EXEC SUMMARY */
  .exec-bullet { display: flex; gap: 12px; align-items: flex-start; padding: 12px 0; border-bottom: 1px solid #f3f4f6; }
  .exec-bullet:last-child { border-bottom: none; }
  .exec-icon { font-size: 1.4rem; min-width: 32px; }
  .exec-text strong { display: block; font-size: 0.95rem; }
  .exec-text span { color: #555; font-size: 0.87rem; }

  /* ACTION CARDS */
  .action-card { border-radius: 10px; padding: 16px 18px; margin-bottom: 14px; border: 1px solid #e5e7eb; }
  .action-card .card-header { display: flex; gap: 10px; align-items: center; margin-bottom: 8px; flex-wrap: wrap; }
  .action-card .card-title { font-weight: 700; font-size: 0.98rem; }
  .action-card .card-source { color: #6b7280; font-size: 0.82rem; }
  .action-card .card-why { font-size: 0.87rem; color: #374151; margin-bottom: 6px; }
  .action-card .card-next { font-size: 0.87rem; background: #f9fafb; border-radius: 6px; padding: 6px 10px; }
  .action-card .card-due { font-size: 0.8rem; color: #b91c1c; font-weight: 700; margin-top: 6px; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { font-weight: 700; font-size: 1rem; color: #1d4ed8; background: #eff6ff; border-radius: 6px; padding: 6px 12px; margin-bottom: 8px; }
  .cal-event { display: grid; grid-template-columns: 110px 1fr; gap: 8px; padding: 10px 12px; border-radius: 8px; margin-bottom: 6px; border: 1px solid #e5e7eb; }
  .cal-time { font-weight: 700; font-size: 0.85rem; color: #1d4ed8; }
  .cal-details .ev-title { font-weight: 700; font-size: 0.92rem; }
  .cal-details .ev-meta { font-size: 0.8rem; color: #6b7280; margin-top: 2px; }
  .cal-details .ev-prep { font-size: 0.8rem; color: #374151; margin-top: 4px; background: #f9fafb; padding: 4px 8px; border-radius: 4px; }
  .ev-conflict { font-size: 0.78rem; font-weight: 700; color: #dc2626; margin-top: 4px; }

  /* JOB PIPELINE */
  .job-table { width: 100%; border-collapse: collapse; font-size: 0.86rem; }
  .job-table th { background: #f3f4f6; text-align: left; padding: 8px 10px; font-weight: 700; border-bottom: 2px solid #e5e7eb; }
  .job-table td { padding: 8px 10px; border-bottom: 1px solid #f0f0f0; vertical-align: top; }
  .job-table tr:last-child td { border-bottom: none; }
  .fit-high { color: #16a34a; font-weight: 700; }
  .fit-med { color: #d97706; font-weight: 700; }
  .fit-low { color: #9ca3af; font-weight: 700; }

  /* EMAIL CATEGORIES */
  .email-category { border-radius: 10px; padding: 14px 16px; margin-bottom: 12px; border: 1px solid #e5e7eb; }
  .email-category .cat-header { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }
  .email-category .cat-title { font-weight: 700; font-size: 0.95rem; }
  .email-category .cat-count { font-size: 0.78rem; color: #6b7280; }
  .email-category .cat-body { font-size: 0.85rem; color: #374151; }
  .email-category .cat-senders { font-size: 0.82rem; color: #555; margin: 4px 0; }
  .email-category .cat-action { font-size: 0.82rem; font-weight: 700; margin-top: 6px; padding: 4px 10px; border-radius: 4px; display: inline-block; }

  /* ACCOUNTING TABLE */
  .acct-table { width: 100%; border-collapse: collapse; font-size: 0.86rem; }
  .acct-table th { background: #1a1a2e; color: #fff; padding: 9px 12px; text-align: left; }
  .acct-table td { padding: 8px 12px; border-bottom: 1px solid #f0f0f0; }
  .acct-table tr:nth-child(even) td { background: #f9fafb; }
  .acct-table .total-row td { font-weight: 700; background: #fef3c7; border-top: 2px solid #d97706; }

  /* DASHBOARD */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-card { border-radius: 10px; padding: 16px; border: 1px solid #e5e7eb; }
  .dash-card .dash-icon { font-size: 1.5rem; }
  .dash-card .dash-label { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 1px; color: #6b7280; margin-top: 4px; }
  .dash-card .dash-val { font-size: 1.3rem; font-weight: 700; margin-top: 2px; }
  .dash-card .dash-detail { font-size: 0.78rem; color: #6b7280; margin-top: 4px; }

  /* PRIORITY TABLE */
  .priority-table { width: 100%; border-collapse: collapse; font-size: 0.86rem; }
  .priority-table th { background: #f3f4f6; text-align: left; padding: 8px 10px; font-weight: 700; border-bottom: 2px solid #e5e7eb; }
  .priority-table td { padding: 8px 10px; border-bottom: 1px solid #f0f0f0; vertical-align: top; }
  .priority-table tr:last-child td { border-bottom: none; }

  /* TOP 3 */
  .top3 { counter-reset: top3; }
  .top3-item { display: flex; gap: 16px; align-items: flex-start; padding: 14px 0; border-bottom: 1px solid #f3f4f6; }
  .top3-item:last-child { border-bottom: none; }
  .top3-num { min-width: 36px; height: 36px; border-radius: 50%; background: linear-gradient(135deg, #1a1a2e, #0f3460); color: #f0c040; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; font-weight: 700; flex-shrink: 0; }
  .top3-text strong { display: block; font-size: 0.97rem; }
  .top3-text span { color: #555; font-size: 0.86rem; }

  /* TRASH */
  .trash-group { background: #fafafa; border-radius: 8px; padding: 12px 16px; margin-bottom: 10px; border: 1px solid #e5e7eb; }
  .trash-group-title { font-weight: 700; font-size: 0.9rem; margin-bottom: 6px; }
  .trash-item { font-size: 0.83rem; padding: 3px 0; border-bottom: 1px dotted #e5e7eb; }
  .trash-item:last-child { border-bottom: none; }

  /* NEWSLETTER */
  .nl-table { width: 100%; border-collapse: collapse; font-size: 0.85rem; }
  .nl-table th { background: #ede9fe; color: #5b21b6; padding: 8px 10px; text-align: left; font-weight: 700; }
  .nl-table td { padding: 8px 10px; border-bottom: 1px solid #f3f4f6; }
  .nl-table tr:last-child td { border-bottom: none; }

  /* PROMO TABLE */
  .promo-table { width: 100%; border-collapse: collapse; font-size: 0.85rem; }
  .promo-table th { background: #f3f4f6; padding: 8px 10px; text-align: left; font-weight: 700; border-bottom: 2px solid #e5e7eb; }
  .promo-table td { padding: 7px 10px; border-bottom: 1px solid #f0f0f0; }
  .promo-table tr:last-child td { border-bottom: none; }

  a { color: #2563eb; }
  .flag { display: inline-block; margin-left: 6px; }
  @media(max-width:600px) { .cal-event { grid-template-columns: 1fr; } .dash-grid { grid-template-columns: 1fr 1fr; } }
</style>
</head>
<body>
<div class="wrapper">

<!-- ══════════════════════════════════════════════════════════ -->
<!-- 1. HEADER                                                  -->
<!-- ══════════════════════════════════════════════════════════ -->
<div class="header">
  <div class="sub">📋 Executive Briefing — Prepared by Your Chief of Staff</div>
  <h1>Good Morning, Melissa! ☀️</h1>
  <div class="sub">Friday, June 5, 2026 &nbsp;|&nbsp; Have a great Friday!</div>
  <div class="meta-row">
    <div class="meta-box"><div class="val">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="meta-box"><div class="val">9</div><div class="lbl">Calendar Events</div></div>
    <div class="meta-box"><div class="val">🔴 3</div><div class="lbl">Urgent Items</div></div>
    <div class="meta-box"><div class="val">🟡 5</div><div class="lbl">Action Required</div></div>
    <div class="meta-box"><div class="val">🟢 2</div><div class="lbl">Job Leads</div></div>
  </div>
</div>

<!-- ══════════════════════════════════════════════════════════ -->
<!-- 2. EXECUTIVE SUMMARY                                       -->
<!-- ══════════════════════════════════════════════════════════ -->
<div class="section band-red">
  <div class="section-title">🗂️ Executive Summary</div>

  <div class="exec-bullet">
    <div class="exec-icon">🔴</div>
    <div class="exec-text">
      <strong>URGENT — Anthropic API Disabled + 5 Failed Payments ($21.78 each)</strong>
      <span>Your Claude API access has been <strong>turned off</strong> due to insufficient credits. Separately, Anthropic attempted to charge your credit card multiple times ($21.78 and $16.40) and failed repeatedly today. You also connected a bank account via Link, and one receipt was issued. This payment crisis needs immediate resolution — your briefing system and Claude access depend on it.</span>
    </div>
  </div>

  <div class="exec-bullet">
    <div class="exec-icon">🟢</div>
    <div class="exec-text">
      <strong>OPPORTUNITY — Two Senior HR Job Alerts + Consultation with Netta Jenkins</strong>
      <span>LinkedIn flagged a VP HR (Private Equity) role at Hoxton Circle paying up to $240K/year and a Head/Director of HR at Flatpay up to $200K/year. You also have a 15-minute consultation with Netta Jenkins (HIC Consult) on June 9 via Zoom — a potential career accelerator to prepare for.</span>
    </div>
  </div>

  <div class="exec-bullet">
    <div class="exec-icon">🟡</div>
    <div class="exec-text">
      <strong>DEADLINES — CHRO Office Subscription Expires Tomorrow + Jackie's Birthday Tomorrow + Eye Appt June 8</strong>
      <span>Your paid subscription to The CHRO Office expires tomorrow (June 6). Jackie's birthday is also June 6 — act today. Eye appointment is June 8 at 9 AM. State Farm bill is due June 7. Busy week ahead; see calendar for full picture.</span>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════════════════════ -->
<!-- 3. ACTION REQUIRED                                         -->
<!-- ══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">⚡ Action Required</div>

  <!-- CRITICAL: Anthropic API Off -->
  <div class="action-card band-red" style="background:#fff5f5;">
    <div class="card-header">
      <span class="pill pill-red">🔴 CRITICAL</span>
      <span class="card-title">Claude API Access Is Disabled — Restore Immediately</span>
    </div>
    <div class="card-source">From: Anthropic &lt;no-reply-tg3@mail.anthropic.com&gt;</div>
    <div class="card-why">⚠️ Your Claude API has been turned off because "Melissa's Individual Org" is out of usage credits. This directly breaks your daily briefing automation and any AI-powered workflows. Multiple payment failures ($21.78 attempted 5+ times, $16.40 once) indicate a credit card issue. You have connected a bank account via Stripe Link — confirm that payment method is now active.</div>
    <div class="card-next">➡️ <strong>Go to console.anthropic.com → Billing → Add credits or verify bank account via Link is active. Confirm receipt #2510-6474-3048 is successful.</strong></div>
    <div class="card-due">⏰ DUE: TODAY — API is currently OFF</div>
  </div>

  <!-- CHRO Office Subscription -->
  <div class="action-card band-yellow" style="background:#fffbeb;">
    <div class="card-header">
      <span class="pill pill-yellow">🟡 DEADLINE</span>
      <span class="card-title">The CHRO Office Paid Subscription Expires TOMORROW</span>
    </div>
    <div class="card-source">From: The CHRO Office &lt;thehroffice@substack.com&gt;</div>
    <div class="card-why">Your paid Substack subscription to The CHRO Office expires Saturday, June 6. This is a professional development resource relevant to your HR career. Missing the renewal means losing access to premium content.</div>
    <div class="card-next">➡️ Decide: Renew or let it lapse. If valuable, renew today via Substack settings.</div>
    <div class="card-due">⏰ DUE: Tomorrow, June 6</div>
  </div>

  <!-- Jackie's Birthday -->
  <div class="action-card band-yellow" style="background:#fffbeb;">
    <div class="card-header">
      <span class="pill pill-yellow">🟡 PERSONAL</span>
      <span class="card-title">Jackie's Birthday is TOMORROW — June 6</span>
    </div>
    <div class="card-source">From: Google Calendar</div>
    <div class="card-why">Jackie's birthday is June 6. If you haven't sent a gift, card, or made plans — today is your last chance.</div>
    <div class="card-next">➡️ Send a message, order a gift, or make plans today.</div>
    <div class="card-due">⏰ DUE: Today (event tomorrow June 6)</div>
  </div>

  <!-- State Farm Bill -->
  <div class="action-card band-yellow" style="background:#fffbeb;">
    <div class="card-header">
      <span class="pill pill-yellow">🟡 BILLING</span>
      <span class="card-title">State Farm Bill Due Sunday, June 7</span>
    </div>
    <div class="card-source">From: Google Calendar</div>
    <div class="card-why">State Farm insurance payment is calendared for June 7. Confirm payment is set up or pay manually before the weekend.</div>
    <div class="card-next">➡️ Verify auto-pay is active or log into State Farm and pay now.</div>
    <div class="card-due">⏰ DUE: Sunday, June 7</div>
  </div>

  <!-- Netta Jenkins Zoom -->
  <div class="action-card band-green" style="background:#f0fdf4;">
    <div class="card-header">
      <span class="pill pill-green">🟢 CAREER</span>
      <span class="card-title">Prep for 15-Min Zoom with Netta Jenkins (HIC Consult) — June 9</span>
    </div>
    <div class="card-source">From: Google Calendar | netta@hicconsult.com</div>
    <div class="card-why">You have a confirmed consultation with Netta Jenkins on June 9 at 12:00 PM ET. Zoom link and password available. This is a networking/career consultation — go in prepared.</div>
    <div class="card-next">➡️ Research Netta Jenkins and HIC Consult. Prepare a 2-min career summary + 2–3 specific questions. Save Zoom link: https://us06web.zoom.us/j/5224221004 | Password: 424726</div>
    <div class="card-due">⏰ DUE: Prep by end of day June 8</div>
  </div>

  <!-- HR Networking RSVP -->
  <div class="action-card band-blue" style="background:#eff6ff;">
    <div class="card-header">
      <span class="pill pill-blue">🔵 RSVP NEEDED</span>
      <span class="card-title">RSVP Pending: HR Networking & Job Search Zoom — June 10 & June 11</span>
    </div>
    <div class="card-source">From: Google Calendar</div>
    <div class="card-why">Two HR networking Zoom sessions show status "needsAction" — you have not yet RSVP'd. June 10 (12–1:30 PM) and June 11 Open Office Hours (12–1 PM). These are active job search resources.</div>
    <div class="card-next">➡️ Accept or decline both calendar invites today. Conflicts: June 10 overlaps with "Melissa x Meg drinks" at 1 PM.</div>
    <div class="card-due">⏰ DUE: ASAP — events next week</div>
  </div>

  <!-- Vet / Prescription Policy Update -->
  <div class="action-card band-yellow" style="background:#fffbeb;">
    <div class="card-header">
      <span class="pill pill-yellow">🟡 HEALTH</span>
      <span class="card-title">Center for Veterinary Care — Third Party Prescription Policy Change for Stella</span>
    </div>
    <div class="card-source">From: Center for Veterinary Care &lt;contact@em.thrivepetcare.com&gt;</div>
    <div class="card-why">Your vet has updated their third-party prescription request policy. This affects how you order Stella's medications. Could impact refill process — read carefully.</div>
    <div class="card-next">➡️ Open email and review new prescription request process. Update any pharmacy orders accordingly.</div>
    <div class="card-due">⏰ DUE: Review today if Stella has upcoming prescriptions</div>
  </div>

  <!-- GitHub Workflow Failed -->
  <div class="action-card band-red" style="background:#fff5f5;">
    <div class="card-header">
      <span class="pill pill-red">🔴 SYSTEM</span>
      <span class="card-title">Daily Briefing GitHub Workflow Failed (3x Today)</span>
    </div>
    <div class="card-source">From: missophs &lt;notifications@github.com&gt;</div>
    <div class="card-why">Your Daily Briefing automation (missophs/daily-briefing, webhooks job, commit 41906d6) failed 3 times today. This is directly related to the Claude API being disabled — fixing Anthropic billing should restore the workflow.</div>
    <div class="card-next">➡️ After restoring Claude API credits, re-run the workflow manually and verify success.</div>
    <div class="card-due">⏰ DUE: After Anthropic billing is fixed</div>
  </div>

</div>

<!-- ══════════════════════════════════════════════════════════ -->
<!-- 4. FULL 7-DAY CALENDAR                                     -->
<!-- ══════════════════════════════════════════════════════════ -->
<div class="section band-blue">
  <div class="section-title">📅 Full 7-Day Calendar — June 5–11, 2026</div>

  <!-- Friday June 5 -->
  <div class="cal-day">
    <div class="cal-day-header">📌 Friday, June 5, 2026 — TODAY</div>
    <div class="cal-event" style="background:#f9fafb;">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="ev-title">No calendar events today</div>
        <div class="ev-meta">Focus time — use today to resolve Anthropic billing, prep for Jackie's birthday, and review action items.</div>
      </div>
    </div>
  </div>

  <!-- Saturday June 6 -->
  <div class="cal-day">
    <div class="cal-day-header">🎂 Saturday, June 6, 2026</div>
    <div class="cal-event" style="background:#fef9c3;">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="ev-title">🎂 Jackie's Birthday</div>
        <div class="ev-meta"><span class="pill pill-yellow">Confirmed</span> &nbsp; Personal</div>
        <div class="ev-prep">📌 Prep: Send gift/message/call. Handle TODAY — birthday is tomorrow!</div>
      </div>
    </div>
    <div class="cal-event" style="background:#fff5f5;">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="ev-title">⏰ CHRO Office Subscription Expires</div>
        <div class="ev-meta"><span class="pill pill-red">Deadline</span> &nbsp; Renew or cancel today</div>
        <div class="ev-prep">📌 Prep: Decide renewal before midnight tonight (Friday).</div>
      </div>
    </div>
  </div>

  <!-- Sunday June 7 -->
  <div class="cal-day">
    <div class="cal-day-header">📋 Sunday, June 7, 2026</div>
    <div class="cal-event" style="background:#fffbeb;">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="ev-title">🏦 State Farm Bill Due</div>
        <div class="ev-meta"><span class="pill pill-yellow">Confirmed</span> &nbsp; Insurance Payment</div>
        <div class="ev-prep">📌 Prep: Verify auto-pay or pay manually before end of day Sunday. Set up today.</div>
      </div>
    </div>
  </div>

  <!-- Monday June 8 -->
  <div class="cal-day">
    <div class="cal-day-header">👁️ Monday, June 8, 2026</div>
    <div class="cal-event" style="background:#eff6ff;">
      <div class="cal-time">9:00 – 10:00 AM ET</div>
      <div class="cal-details">
        <div class="ev-title">👁️ Eye Appointment</div>
        <div class="ev-meta"><span class="pill pill-blue">Confirmed</span> &nbsp; Medical</div>
        <div class="ev-prep">📌 Prep: Confirm location. Note: Warby Parker says your prescription expires in 2 weeks — ask your eye doctor about renewal. 1-800 Contacts also flagged you're overdue. Bring insurance card.</div>
      </div>
    </div>
  </div>

  <!-- Tuesday June 9 -->
  <div class="cal-day">
    <div class="cal-day-header">🤝 Tuesday, June 9, 2026</div>
    <div class="cal-event" style="background:#f0fdf4;">
      <div class="cal-time">12:00 – 12:15 PM ET</div>
      <div class="cal-details">
        <div class="ev-title">🤝 Melissa × Netta Jenkins — 15-Min Consultation (Zoom)</div>
        <div class="ev-meta"><span class="pill pill-green">Accepted</span> &nbsp; netta@hicconsult.com</div>
        <div class="ev-meta">🔗 <a href="https://us06web.zoom.us/j/5224221004?pwd=UU5YNmlFckpjQnlzc2FDMHFlNUhhUT09" target="_blank">Zoom Link</a> | Password: 424726</div>
        <div class="ev-prep">📌 Prep: Research Netta Jenkins / HIC Consult. Prepare 2-min career summary + 2-3 specific questions about career opportunities or coaching.</div>
      </div>
    </div>
  </div>

  <!-- Wednesday June 10 -->
  <div class="cal-day">
    <div class="cal-day-header">⚠️ Wednesday, June 10, 2026 — CONFLICT DAY</div>
    <div class="cal-event" style="background:#eff6ff;">
      <div class="cal-time">12:00 – 1:30 PM ET</div>
      <div class="cal-details">
        <div class="ev-title">👥 HR Networking & Job Search Group — Zoom 2</div>
        <div class="ev-meta"><span class="pill pill-red">RSVP NEEDED</span> &nbsp; ~175 attendees</div>
        <div class="ev-meta">🔗 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a></div>
        <div class="ev-prep">📌 Prep: RSVP now. Review team guidelines linked in invite description. Note: NO AI recording tools per event rules.</div>
        <div class="ev-conflict">⚠️ CONFLICT: Overlaps with "Melissa × Meg drinks" at 1:00 PM — 30-min overlap. Resolve now.</div>
      </div>
    </div>
    <div class="cal-event" style="background:#f9fafb;">
      <div class="cal-time">12:00 – 1:30 PM ET</div>
      <div class="cal-details">
        <div class="ev-title">🌐 Network (Personal Reminder)</div>
        <div class="ev-meta"><span class="pill pill-blue">Confirmed</span> &nbsp; Personal note/reminder</div>
        <div class="ev-prep">📌 Appears to be a personal networking reminder block aligned with the HR Zoom session above.</div>
      </div>
    </div>
    <div class="cal-event" style="background:#f0fdf4;">
      <div class="cal-time">1:00 – 2:00 PM ET</div>
      <div class="cal-details">
        <div class="ev-title">🍹 Melissa × Meg Drinks (Meg Park, Oakleaf Partnership)</div>
        <div class="ev-meta"><span class="pill pill-green">Accepted</span> &nbsp; megpark@oakleafpartnership.com | Location: TBC</div>
        <div class="ev-prep">📌 Prep: Confirm location with Meg. Note conflict with HR Networking Zoom (ends 1:30 PM). Consider leaving Zoom early or rescheduling drinks to later.</div>
        <div class="ev-conflict">⚠️ CONFLICT: Overlaps with HR Networking Zoom (12:00–1:30 PM).</div>
      </div>
    </div>
  </div>

  <!-- Thursday June 11 -->
  <div class="cal-day">
    <div class="cal-day-header">📊 Thursday, June 11, 2026</div>
    <div class="cal-event" style="background:#fafafa;">
      <div class="cal-time">9:00 – 10:30 AM ET</div>
      <div class="cal-details">
        <div class="ev-title">📊 Executive Roundtable (Zoom — John Madigan)</div>
        <div class="ev-meta"><span class="pill pill-red">DECLINED</span> &nbsp; Host: John Madigan</div>
        <div class="ev-meta">🔗 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> | Password: 205454</div>
        <div class="ev-prep">📌 You declined this event. If you wish to rejoin, reach out to John Madigan now.</div>
      </div>
    </div>
    <div class="cal-event" style="background:#eff6ff;">
      <div class="cal-time">12:00 – 1:00 PM ET</div>
      <div class="cal-details">
        <div class="ev-title">👥 HR Networking & Job Search: Open Office Hours — Zoom 2</div>
        <div class="ev-meta"><span class="pill pill-red">RSVP NEEDED</span> &nbsp; ~175 attendees</div>
        <div class="ev-meta">🔗 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a></div>
        <div class="ev-prep">📌 Prep: RSVP now. No AI recording tools. Open discussion format — good for Q&A and peer support.</div>
      </div>
    </div>
  </div>

</div>

<!-- ══════════════════════════════════════════════════════════ -->
<!-- 5. JOB SEARCH & INTERVIEW PIPELINE                         -->
<!-- ══════════════════════════════════════════════════════════ -->
<div class="section band-green">
  <div class="section-title">💼 Job Search & Interview Pipeline</div>
  <table class="job-table">
    <thead>
      <tr>
        <th>Type</th>
        <th>Role / Event</th>
        <th>Source / Contact</th>
        <th>Details</th>
        <th>Fit</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="pill pill-green">Job Alert</span></td>
        <td>Vice President Human Resources (Private Equity)</td>
        <td>Hoxton Circle via LinkedIn</td>
        <td>$220K–$240K/year</td>
        <td class="fit-high">HIGH</td>
        <td>Review & apply if aligned</td>
      </tr>
      <tr>
        <td><span class="pill pill-green">Job Alert</span></td>
        <td>Head / Director of HR (US)</td>
        <td>Flatpay via LinkedIn</td>
        <td>$180K–$200K/year | In Trash — was deleted</td>
        <td class="fit-high">HIGH</td>
        <td>Restore from trash, review role</td>
      </tr>
      <tr>
        <td><span class="pill pill-blue">Consultation</span></td>
        <td>15-Min Zoom with Netta Jenkins</td>
        <td>netta@hicconsult.com | HIC Consult</td>
        <td>June 9, 12:00–12:15 PM ET | Accepted</td>
        <td class="fit-high">HIGH</td>
        <td>Prep talking points, research Netta</td>
      </tr>
      <tr>
        <td><span class="pill pill-blue">Networking</span></td>
        <td>HR Networking & Job Search Group Zoom</td>
        <td>Large group (~175 HR professionals)</td>
        <td>June 10, 12–1:30 PM | RSVP needed</td>
        <td class="fit-high">HIGH</td>
        <td>RSVP now; resolve conflict with Meg</td>
      </tr>
      <tr>
        <td><span class="pill pill-blue">Networking</span></td>
        <td>HR Open Office Hours Zoom</td>
        <td>Same HR group</td>
        <td>June 11, 12–1 PM | RSVP needed</td>
        <td class="fit-high">HIGH</td>
        <td>RSVP now</td>
      </tr>
      <tr>
        <td><span class="pill pill-green">Drinks</span></td>
        <td>Melissa × Meg Park (Oakleaf Partnership)</td>
        <td>megpark@oakleafpartnership.com</td>
        <td>June 10, 1–2 PM | Location TBC | Accepted</td>
        <td class="fit-high">HIGH</td>
        <td>Confirm location; resolve scheduling conflict</td>
      </tr>
      <tr>
        <td><span class="pill pill-gray">Roundtable</span></td>
        <td>Executive Roundtable — John Madigan</td>
        <td>Via Calendar</td>
        <td>June 11, 9–10:30 AM | DECLINED</td>
        <td class="fit-med">MEDIUM</td>
        <td>Reconsider — could be valuable network</td>
      </tr>
      <tr>
        <td><span class="pill pill-gray">Group Msg</span></td>
        <td>RNG Tampa Bay — Bank of America Recruiting Contact Request</td>
        <td>Antonio Fiorentino via RNG Tampa Bay Google Group</td>
        <td>Looking for BoA recruiting connection</td>
        <td class="fit-low">LOW</td>
        <td>Reply if you have a contact at BoA</td>
      </tr>
      <tr>
        <td><span class="pill pill-green">Research $</span></td>
        <td>Sago Financial Experiences Study — $100 Incentive</td>
        <td>Sago / focusgroup.com</td>
        <td>$100 for completing financial research study</td>
        <td class="fit-med">MEDIUM</td>
        <td>Complete pre-qualification if interested</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ══════════════════════════════════════════════════════════ -->
<!-- 6. FULL EMAIL REVIEW BY CATEGORY                           -->
<!-- ══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📧 Full Email Review by Category</div>

  <!-- SECURITY / RISK -->
  <div class="email-category band-red" style="background:#fff5f5;">
    <div class="cat-header">
      <span class="pill pill-red">🔴 Security / Risk</span>
      <span class="cat-count">— 10 emails</span>
    </div>
    <div class="cat-body">
      <div class="cat-senders">
        <strong>Anthropic, PBC (failed-payments@mail.anthropic.com):</strong> 5 failed payment alerts — $21.78 (×4 attempts today at 14:14, 14:15, 14:17, 14:22) + $16.40 (14:12). Multiple duplicate attempts suggest a payment retry loop.<br><br>
        <strong>Anthropic, PBC (invoice+statements@mail.anthropic.com):</strong> 2 receipts issued — #2510-6474-3048 (15:08) and #2010-4855-2725 (13:33). Payment may have partially succeeded via bank account.<br><br>
        <strong>Link (notifications@link.com):</strong> 2 notifications — bank account connected to Anthropic, PBC (14:13 and 15:04). Stripe Link used to add bank payment.<br><br>
        <strong>Anthropic (no-reply-tg3@mail.anthropic.com):</strong> Claude API access disabled due to no usage credits — action needed immediately.
      </div>
    </div>
    <div class="cat-action" style="background:#fee2e2; color:#b91c1c;">🔴 ACTION: Fix Anthropic billing NOW. Restore Claude API access. Verify bank account via Link is processed.</div>
  </div>

  <!-- JOB SEARCH -->
  <div class="email-category band-green" style="background:#f0fdf4;">
    <div class="cat-header">
      <span class="pill pill-green">🟢 Job Search</span>
      <span class="cat-count">— 2 emails</span>
    </div>
    <div class="cat-body">
      <div class="cat-senders">
        <strong>LinkedIn Job Alerts:</strong> VP Human Resources (Private Equity) at Hoxton Circle — $220K–$240K/year (in inbox, unread).<br>
        <strong>LinkedIn Job Alerts:</strong> Head/Director of HR (US) at Flatpay — $180K–$200K/year (in trash — was deleted; consider restoring).
      </div>
    </div>
    <div class="cat-action" style="background:#dcfce7; color:#166534;">🟢 ACTION: Review VP HR at Hoxton Circle immediately. Restore Flatpay alert from trash and evaluate.</div>
  </div>

  <!-- RECRUITERS / NETWORKING -->
  <div class="email-category band-green" style="background:#f0fdf4;">
    <div class="cat-header">
      <span class="pill pill-green">🟢 Recruiters / Networking</span>
      <span class="cat-count">— 2 emails</span>
    </div>
    <div class="cat-body">
      <div class="cat-senders">
        <strong>Worldwide Women's Association (Sophia Davis):</strong> Membership invitation — "Things are moving fast at WWA." Could be a networking org for senior women executives. Unread, in inbox.<br>
        <strong>RNG Tampa Bay (Antonio Fiorentino via Google Group):</strong> Seeking Bank of America Recruiting contact. Low-stakes group message; reply if you have a BoA connection.
      </div>
    </div>
    <div class="cat-action" style="background:#dcfce7; color:#166534;">🟢 ACTION: Review WWA membership — could be a high-value executive network. Optionally reply to RNG Tampa Bay if you have a BoA contact.</div>
  </div>

  <!-- CALENDAR / EVENTS -->
  <div class="email-category band-blue" style="background:#eff6ff;">
    <div class="cat-header">
      <span class="pill pill-blue">🔵 Calendar / Events</span>
      <span class="cat-count">— 1 email</span>
    </div>
    <div class="cat-body">
      <div class="cat-senders">
        <strong>Melissa Daily Briefing (melissaw212@gmail.com):</strong> Daily Briefing email sent at 13:50 UTC — previous automated briefing. Confirms the system was running earlier today before API cutoff.
      </div>
    </div>
    <div class="cat-action" style="background:#dbeafe; color:#1d4ed8;">🔵 ACTION: Reference previous briefing. Restore API to ensure tomorrow's briefing runs successfully.</div>
  </div>

  <!-- MEDICAL / HEALTH -->
  <div class="email-category" style="border-left:5px solid #0891b2; background:#ecfeff;">
    <div class="cat-header">
      <span class="pill" style="background:#cffafe;color:#0e7490;">🏥 Medical / Health</span>
      <span class="cat-count">— 1 email</span>
    </div>
    <div class="cat-body">
      <div class="cat-senders">
        <strong>Center for Veterinary Care (Thrive Pet Care):</strong> "Important Update: Third Party Prescription Requests" — policy change affecting Stella's prescriptions. Unread, in inbox.
      </div>
    </div>
    <div class="cat-action" style="background:#cffafe; color:#0e7490;">🏥 ACTION: Read in full. Update prescription ordering process for Stella accordingly.</div>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="email-category band-yellow" style="background:#fffbeb;">
    <div class="cat-header">
      <span class="pill pill-yellow">🟡 Financial / Billing</span>
      <span class="cat-count">— 3 emails</span>
    </div>
    <div class="cat-body">
      <div class="cat-senders">
        <strong>Robinhood:</strong> IRA/401K rollover reminder — earn a retirement match if transferred by June 19. (In trash — previously deleted.)<br>
        <strong>Sago (focusgroup.com):</strong> $100 incentive to complete a financial research study on "Real-Life Money Decisions." In inbox, unread.<br>
        <strong>Focus Group (participate@focusgroup.com):</strong> Update about Focus Group membership and new opportunities. Read, not in inbox.
      </div>
    </div>
    <div class="cat-action" style="background:#fef3c7; color:#92400e;">🟡 ACTION: Consider Sago $100 study if interested. Robinhood retirement match deadline is June 19 — evaluate if worthwhile.</div>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="email-category band-purple" style="background:#faf5ff;">
    <div class="cat-header">
      <span class="pill pill-purple">🟣 Professional Development</span>
      <span class="cat-count">— 4 emails</span>
    </div>
    <div class="cat-body">
      <div class="cat-senders">
        <strong>The CHRO Office (Substack):</strong> Paid subscription expires TOMORROW, June 6. Renewal decision needed today.<br>
        <strong>HR Brain Pickings (newsletter@mail.hrbrainpickings.com):</strong> "The Friday 5" — AI budgets, papal encyclical, sick leave. Unread, in inbox. Good HR intel digest.<br>
        <strong>Phil Strazzulla / SelectSoftware Reviews:</strong> Free webinar on why HR software decisions fail — practical buy-in strategies. Read, not in inbox.<br>
        <strong>Olivia Gamber / Career Evolved:</strong> "The room of 7 (and the block holding you back)" — career coaching email. In trash.
      </div>
    </div>
    <div class="cat-action" style="background:#ede9fe; color:#5b21b6;">🟣 ACTION: Renew CHRO Office today or let lapse. Read HR Brain Pickings Friday 5. Evaluate webinar signup from Phil Strazzulla.</div>
  </div>

  <!-- PERSONAL -->
  <div class="email-category band-gray" style="background:#fafafa;">
    <div class="cat-header">
      <span class="pill pill-gray">⚪ Personal</span>
      <span class="cat-count">— 1 email</span>
    </div>
    <div class="cat-body">
      <div class="cat-senders">
        <strong>Brya Team (hello@brya.com):</strong> Survey reminder — "Still time to share your thoughts." Survey closes end of week. Read, not in inbox.
      </div>
    </div>
    <div class="cat-action" style="background:#f3f4f6; color:#374151;">⚪ ACTION: Complete Brya survey today if you want to participate (deadline: end of this week).</div>
  </div>

  <!-- NEWSLETTERS / SUBSCRIPTIONS -->
  <div class="email-category band-purple" style="background:#faf5ff;">
    <div class="cat-header">
      <span class="pill pill-purple">🟣 Newsletters / Subscriptions</span>
      <span class="cat-count">— 4 emails</span>
    </div>
    <div class="cat-body">
      <div class="cat-senders">
        <strong>Mindstream:</strong> "Google unveils Dreambeans + 1 in 5 teens use AI for mental health." AI news digest. Unread, in inbox.<br>
        <strong>CoolDeep AI (Beehiiv):</strong> "Claude did my Instagram content while I slept." AI workflow tips. Read, not in inbox.<br>
        <strong>Hebba Youssef / I Hate It Here (Workweek):</strong> "Motivation with $0 — metrics + keeping people engaged without budget." HR newsletter. In trash.<br>
        <strong>Pre-IPO Offering / Capital Noted:</strong> "Apple's Starlink Update Sparks Huge Earning Opportunity." Investment/promo newsletter. Not in inbox, not in trash.
      </div>
    </div>
    <div class="cat-action" style="background:#ede9fe; color:#5b21b6;">🟣 ACTION: Read Mindstream and Hebba Youssef for professional relevance. Unsubscribe from Capital Noted (investment promo). CoolDeep AI — skim or archive.</div>
  </div>

  <!-- PROMOTIONAL / RETAIL -->
  <div class="email-category band-gray" style="background:#f9fafb;">
    <div class="cat-header">
      <span class="pill pill-gray">⚪ Promotional / Retail</span>
      <span class="cat-count">— 16 emails</span>
    </div>
    <div class="cat-body">
      <div class="cat-senders">
        <strong>CoinOut:</strong> "Earn up to 7,000 Coins" (inbox, unread) | <strong>BellaVitashop (TikTok Shop):</strong> Flash sale (trash) | <strong>Shoe Station:</strong> Sandal Savings Event (trash) | <strong>1-800 Contacts:</strong> Reorder for National Eyewear Day (trash) | <strong>PUMA:</strong> PUMA x Salehe Bembury (not in inbox/trash) | <strong>Chip City:</strong> 15% off catering (inbox, unread) | <strong>Walgreens:</strong> BOGO vitamins (trash) | <strong>Old Navy:</strong> 50% off active wear (not in inbox/trash) | <strong>Warby Parker:</strong> Prescription expires in 2 weeks (not in inbox/trash — but RELEVANT: eye appt June 8) | <strong>Venmo:</strong> 9% cash back credit card offer (not in inbox/trash) | <strong>Laura Geller (×2):</strong> $20 credit, ends tonight (both in trash) | <strong>Fayced Aesthetics NYC:</strong> Meet Daisy, new nurse injector (trash) | <strong>GLP-1 by DirectMeds:</strong> Spam weight loss email (not in inbox/trash — suspicious sender) | <strong>Mystery Deal:</strong> "The Kind of Find You Didn't Know You Needed" (trash) | <strong>Slack:</strong> "Invite your team to Slack today!" (not in inbox/trash)
      </div>
    </div>
    <div class="cat-action" style="background:#f3f4f6; color:#374151;">⚪ ACTION: Note Warby Parker — prescription expires in 2 weeks; ask eye doctor on June 8. GLP-1 DirectMeds is spam — do not engage. Rest: safe to delete/ignore.</div>
  </div>

  <!-- SYSTEM / TECH -->
  <div class="email-category band-red" style="background:#fff5f5;">
    <div class="cat-header">
      <span class="pill pill-red">🔴 System / Technical</span>
      <span class="cat-count">— 4 emails</span>
    </div>
    <div class="cat-body">
      <div class="cat-senders">
        <strong>missophs / GitHub (notifications@github.com):</strong> 3 workflow failure notifications — Daily Briefing failed (commit 41906d6, webhooks job) at 06:27, 06:33, and 07:02 today. Root cause: Claude API disabled.<br>
        <strong>Slack (no-reply@email.slackhq.com):</strong> "Invite your team to Slack today!" — promotional nudge for Pro trial. Not in inbox.
      </div>
    </div>
    <div class="cat-action" style="background:#fee2e2; color:#b91c1c;">🔴 ACTION: Fix Anthropic API → re-run GitHub workflow. Slack email is low priority — ignore/delete.</div>
  </div>

</div>

<!-- ══════════════════════════════════════════════════════════ -->
<!-- 7. TRASH REVIEW                                            -->
<!-- ══════════════════════════════════════════════════════════ -->
<div class="section band-red">
  <div class="section-title">🗑️ Trash Review</div>
  <p style="font-size:0.85rem;color:#555;margin-bottom:14px;">The following 10 emails are currently in your Gmail Trash. Review before permanent deletion.</p>

  <!-- RESTORE -->
  <div class="trash-group" style="border-left:4px solid #16a34a;">
    <div class="trash-group-title" style="color:#16a34a;">✅ RESTORE — These have value and should be moved back to inbox</div>
    <div class="trash-item">
      <strong>LinkedIn Job Alerts:</strong> "Head / Director of HR (US) at Flatpay: up to $200K/year" — $180K–$200K/year senior HR role. Accidentally trashed — restore and review immediately.
    </div>
    <div class="trash-item">
      <strong>Hebba Youssef / I Hate It Here (Workweek):</strong> "📓 Motivation with $0" — HR newsletter on engagement metrics. Professionally relevant content. Restore or read before deleting.
    </div>
  </div>

  <!-- REVIEW -->
  <div class="trash-group" style="border-left:4px solid #d97706;">
    <div class="trash-group-title" style="color:#d97706;">🔍 REVIEW — May want to read before deleting</div>
    <div class="trash-item">
      <strong>Robinhood:</strong> "Reminder: Claim a retirement match" — IRA/401K transfer by June 19 earns a match. Financial opportunity worth considering before deleting.
    </div>
    <div class="trash-item">
      <strong>Olivia Gamber / Career Evolved:</strong> "The room of 7 (and the block holding you back)" — career coaching email. Could be relevant given active job search. Skim before deleting.
    </div>
  </div>

  <!-- SAFE TO DELETE -->
  <div class="trash-group" style="border-left:4px solid #9ca3af;">
    <div class="trash-group-title" style="color:#6b7280;">🗑️ SAFE TO DELETE — Low value, correctly trashed</div>
    <div class="trash-item"><strong>Fayced Aesthetics NYC:</strong> "Meet Daisy" — new nurse injector promotional. Correctly deleted.</div>
    <div class="trash-item"><strong>BellaVitashop (TikTok Shop):</strong> Flash sale. Correctly deleted.</div>
    <div class="trash-item"><strong>Shoe Station:</strong> Sandal Savings Event. Correctly deleted.</div>
    <div class="trash-item"><strong>1-800 Contacts:</strong> National Eyewear Day reorder promo. Correctly deleted (eye appt June 8 already scheduled).</div>
    <div class="trash-item"><strong>Walgreens:</strong> BOGO vitamins. Correctly deleted.</div>
    <div class="trash-item"><strong>Laura Geller (×2):</strong> "$20 Credit, Ends Tonight" — beauty promo sent twice. Both correctly deleted.</div>
    <div class="trash-item"><strong>Mystery Deal:</strong> "The Kind of Find You Didn't Know You Needed" — generic promo. Correctly deleted.</div>
  </div>
</div>

<!-- ══════════════════════════════════════════════════════════ -->
<!-- 8. PROMOTIONAL / RETAIL SUMMARY                            -->
<!-- ══════════════════════════════════════════════════════════ -->
<div class="section band-gray">
  <div class="section-title">🛍️ Promotional / Retail Summary</div>
  <table class="promo-table">
    <thead>
      <tr>
        <th>Sender / Brand</th>
        <th>Count</th>
        <th>Subject / Theme</th>
        <th>Location</th>
        <th>Recommendation</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>CoinOut</strong></td>
        <td>1</td>
        <td>Earn up to 7,000 Coins — Missions screen</td>
        <td>Inbox</td>
        <td><span class="pill pill-gray">Ignore / Archive</span></td>
      </tr>
      <tr>
        <td><strong>BellaVitashop (TikTok Shop)</strong></td>
        <td>1</td>
        <td>Flash sale starts now</td>
        <td>Trash</td>
        <td><span class="pill pill-red">Delete</span></td>
      </tr>
      <tr>
        <td><strong>Shoe Station</strong></td>
        <td>1</td>
        <td>Sandal Savings Event — under $20 / BOGO</td>
        <td>Trash</td>
        <td><span class="pill pill-red">Delete</span></td>
      </tr>
      <tr>
        <td><strong>1-800 Contacts</strong></td>
        <td>1</td>
        <td>Reorder for National Eyewear Day</td>
        <td>Trash</td>
        <td><span class="pill pill-yellow">Review</span> — eye appt June 8; ask doctor about contacts</td>
      </tr>
      <tr>
        <td><strong>PUMA</strong></td>
        <td>1</td>
        <td>PUMA × Salehe Bembury launch</td>
        <td>Not in inbox</td>
        <td><span class="pill pill-gray">Ignore</span></td>
      </tr>
      <tr>
        <td><strong>Chip City</strong></td>
        <td>1</td>
        <td>15% off catering this summer</td>
        <td>Inbox</td>
        <td><span class="pill pill-gray">Archive</span> — save if planning an event</td>
      </tr>
      <tr>
        <td><strong>Walgreens</strong></td>
        <td>1</td>
        <td>BOGO vitamins / essentials</td>
        <td>Trash</td>
        <td><span class="pill pill-red">Delete</span></td>
      </tr>
      <tr>
        <td><strong>Old Navy</strong></td>
        <td>1
<hr>
<h2>Trash Review</h2>
<p><strong>Purpose:</strong> Review deleted emails for anything important before permanent deletion. Anything from job search, billing, medical, calendar, security, legal, GitHub, Netlify, LinkedIn, recruiters, or professional contacts should be reviewed before deleting.</p>

<h2>Promotional / Retail Summary</h2>
<p><strong>Purpose:</strong> Promotional emails are included in the full email inventory below. Delete or ignore retail/promotional items unless there is a deal you actually plan to use or a sender looks suspicious.</p>

<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Financial / Billing</td><td>10</td></tr>
<tr><td>Job Search / Recruiters</td><td>5</td></tr>
<tr><td>Medical / Health</td><td>3</td></tr>
<tr><td>Other / Review</td><td>16</td></tr>
<tr><td>Professional Development / Newsletters</td><td>7</td></tr>
<tr><td>Promotional / Retail</td><td>7</td></tr>
<tr><td>Security / Risk</td><td>2</td></tr>
</table>

<h2>Full Email Inventory</h2>
<p><strong>Every fetched email is grouped below by category.</strong> Use this section to see what to act on, review, delete, or ignore.</p>

<div style="background:#fffbf0; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Financial / Billing (10)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#2 · Fri, 5 Jun 2026 15:08:38 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Your receipt from Anthropic, PBC #2510-6474-3048</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Anthropic, PBC&quot; &lt;invoice+statements@mail.anthropic.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Your receipt from Anthropic, PBC #2510-6474-3048 ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#6 · Fri, 5 Jun 2026 15:05:34 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">$21.78 payment to Anthropic, PBC was unsuccessful</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Anthropic, PBC&quot; &lt;failed-payments@mail.anthropic.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">We weren&amp;#39;t able to charge the credit card you provided. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#7 · Fri, 5 Jun 2026 15:04:43 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">$21.78 payment to Anthropic, PBC was unsuccessful</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Anthropic, PBC&quot; &lt;failed-payments@mail.anthropic.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">We weren&amp;#39;t able to charge the credit card you provided. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#17 · Fri, 5 Jun 2026 14:22:46 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">$21.78 payment to Anthropic, PBC was unsuccessful again</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Anthropic, PBC&quot; &lt;failed-payments@mail.anthropic.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">We weren&amp;#39;t able to charge the credit card you provided. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#20 · Fri, 5 Jun 2026 14:17:06 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">$21.78 payment to Anthropic, PBC was unsuccessful</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Anthropic, PBC&quot; &lt;failed-payments@mail.anthropic.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">We weren&amp;#39;t able to charge the credit card you provided. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#22 · Fri, 5 Jun 2026 14:15:46 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">$21.78 payment to Anthropic, PBC was unsuccessful</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Anthropic, PBC&quot; &lt;failed-payments@mail.anthropic.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">We weren&amp;#39;t able to charge the credit card you provided. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#24 · Fri, 5 Jun 2026 14:14:14 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">$21.78 payment to Anthropic, PBC was unsuccessful</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Anthropic, PBC&quot; &lt;failed-payments@mail.anthropic.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">We weren&amp;#39;t able to charge the credit card you provided. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#26 · Fri, 5 Jun 2026 14:12:03 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">$16.40 payment to Anthropic, PBC was unsuccessful</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Anthropic, PBC&quot; &lt;failed-payments@mail.anthropic.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">We weren&amp;#39;t able to charge the credit card you provided. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#36 · Fri, 5 Jun 2026 13:33:43 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Your receipt from Anthropic, PBC #2010-4855-2725</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Anthropic, PBC&quot; &lt;invoice+statements@mail.anthropic.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Your receipt from Anthropic, PBC #2010-4855-2725 ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#42 · Fri, 05 Jun 2026 13:18:56 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">[action needed] Your Claude API access is turned off</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Anthropic &lt;no-reply-tg3-12bWhUPY4cJHtPeAoQ@mail.anthropic.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Hello, Your access to the Claude API has been disabled because your organization &amp;#39;Melissa&amp;#39;s Individual Org&amp;#39; is out of usage credits. Go to</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>
</div>

<div style="background:#f0fff4; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Job Search / Recruiters (5)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#4 · Fri, 5 Jun 2026 15:06:20 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Vice President Human Resources (Private Equity) at Hoxton Circle: up to $240K/year</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> LinkedIn Job Alerts &lt;jobalerts-noreply@linkedin.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">$220K-$240K / year salary ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#30 · Fri, 05 Jun 2026 07:02:55 -0700</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">[missophs/daily-briefing] Run failed: Daily Briefing - webhooks (41906d6)</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> missophs &lt;notifications@github.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">[missophs/daily-briefing] Daily Briefing workflow run Daily Briefing: All jobs have failed View workflow run Status Job Annotations Daily Briefing / u</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#35 · Fri, 05 Jun 2026 06:33:57 -0700</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">[missophs/daily-briefing] Run failed: Daily Briefing - webhooks (41906d6)</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> missophs &lt;notifications@github.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">[missophs/daily-briefing] Daily Briefing workflow run Daily Briefing: All jobs have failed View workflow run Status Job Annotations Daily Briefing / u</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#41 · Fri, 05 Jun 2026 06:27:12 -0700</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">[missophs/daily-briefing] Run failed: Daily Briefing - webhooks (41906d6)</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> missophs &lt;notifications@github.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">[missophs/daily-briefing] Daily Briefing workflow run Daily Briefing: All jobs have failed View workflow run Status Job Annotations Daily Briefing / u</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#48 · Fri, 5 Jun 2026 13:05:53 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Head / Director of HR (US) at Flatpay: up to $200K/year</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> LinkedIn Job Alerts &lt;jobalerts-noreply@linkedin.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">$180K-$200K / year salary ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>
</div>

<div style="background:#ebf8ff; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Medical / Health (3)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#1 · Fri, 05 Jun 2026 15:08:29 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Google unveils... Dreambeans</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Mindstream &lt;hello@mindstream.news&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">+ 1 in 5 teens use AI for mental health support ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#21 · Fri, 05 Jun 2026 09:26:42 -0400</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">DirectMeds GLP-1 treatment helps you lose up to 4O lbs by the End of Year</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> GLP-1-by-DirectMeds &lt;makiuxdfydq@clmo.jxstfafscurth.us&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">DirectMeds Medical Portal Looking for Ozempic® or Mounjaro® alternative? Weight loss made simple with Semaglutide or Tirzepatide Genuine prescription </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#38 · Fri, 5 Jun 2026 13:06:13 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">New ways to save on contact lenses!</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Target Optical &lt;news@e.targetoptical.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Find the perfect contact for you at Target Optical View in browser Target Optical ® Eyeglasses Sunglasses Contact lenses Plan your visit More ways to </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>
</div>

<div style="background:#f7fafc; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Other / Review (16)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#3 · Fri, 05 Jun 2026 15:08:04 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Coming Soon: Earn up to 7,000 Coins</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> CoinOut &lt;coinout@news.coinout.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Be on the look-out for your chance to earn up to 7000 Coins! Logo Earn up to 7000 Coins Be on the look-out in your Missions screen over the next few d</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#8 · Fri, 5 Jun 2026 15:04:23 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">You&#x27;ve connected your bank account to Anthropic, PBC</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Link &lt;notifications@link.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">You connected your account with Link ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#9 · Fri, 05 Jun 2026 15:01:43 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Things are moving fast at the WWA, secure your membership spot today!</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Sophia Davis &lt;sophia.davis@worldwidewomensassociation.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Join The Worldwide Women&amp;#39;s Association‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#11 · Fri, 05 Jun 2026 14:57:55 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Reminder: Claim a retirement match</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Robinhood &lt;noreply@robinhood.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Transfer an IRA or rollover a 401K to Robinhood by June 19, and earn a match. ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#15 · Fri, 05 Jun 2026 14:44:00 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Important Update: Third Party Prescription Requests</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Center for Veterinary Care  &lt;contact@em.thrivepetcare.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">We&amp;#39;re committed to seamless care for Stella. Center for Veterinary Care New Home, Now Open Dear Melissa, At Center for Veterinary Care, we&amp;#39;re </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#16 · Fri, 05 Jun 2026 13:28:49 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Reorder in two taps for National Eyewear Day</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> 1-800 Contacts &lt;info@pr.1800contacts.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">You&amp;#39;re overdue, based on your last order date. ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#25 · Fri, 5 Jun 2026 14:13:56 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">You&#x27;ve connected your bank account to Anthropic, PBC</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Link &lt;notifications@link.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">You connected your account with Link ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#27 · Fri, 05 Jun 2026 09:10:22 -0500</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Double the Vitamins, Zero Extra Cost</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Walgreens &lt;walgreens@eml.walgreens.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Stock up on select same-brand essentials—your second item is on us. ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#31 · Fri, 05 Jun 2026 14:00:07 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Still time to share your thoughts 🙏</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Brya Team &lt;hello@brya.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Hi there, Just a quick nudge — we sent a short survey on Tuesday and would love to hear from you before we close the survey at the end of the week. Yo</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#32 · Fri, 5 Jun 2026 14:00:04 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Claude did my Instagram content while I slept</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> CoolDeep AI &lt;cooldeepai@mail.beehiiv.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">The carousel workflow that changed my mornings ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#33 · Fri, 05 Jun 2026 13:59:43 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Your prescription expires in two weeks</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Warby Parker &lt;sayhello@mail1.warbyparker.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Pick out some new frames today. ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#40 · Fri, 5 Jun 2026 06:27:59 -0700 (PDT)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">[RNG Tampa Bay] Bank of America contact</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;&#x27;Antonio Fiorentino&#x27; via RNG Tampa Bay&quot; &lt;RNGTampa@googlegroups.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Hi everyone, I&amp;#39;m looking to connect with someone in Recruiting at Bank of America. If anyone in the group currently works there or has a contact t</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#44 · Fri, 05 Jun 2026 13:16:37 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Earn up to 9% cash back for 6 months with the Venmo Credit Card</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Venmo &lt;venmo@email.venmo.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Apply with no impact to your credit score if declined. ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿ ͏ ‌ ﻿</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#45 · Fri, 05 Jun 2026 13:10:52 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">The room of 7 (and the block holding you back)</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Olivia Gamber &lt;careerevolved=oliviagamber.com@f.kajabimail.net&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Hi Melissa, It is an incredibly frustrating feeling to know exactly what you are capable of, yet watch the door close right at the finish line. To wal</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#47 · Fri, 05 Jun 2026 13:06:04 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Your $20 Credit Is Waiting 🔥 Ends TONIGHT</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Laura Geller &lt;beauty@laurageller.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Save 40% + an Extra 10% ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#49 · Fri, 05 Jun 2026 13:02:59 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Your $20 Credit Is Waiting 🔥 Ends TONIGHT</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Laura Geller &lt;beauty@laurageller.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Save 40% + an Extra 10% ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>
</div>

<div style="background:#faf5ff; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Professional Development / Newsletters (7)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#10 · Fri, 05 Jun 2026 15:00:57 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">The friday 5: AI budgets, papal encyclical, sick leave</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> HR Brain Pickings &lt;newsletter@mail.hrbrainpickings.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">June 05, 2026 | Read online Happy Friday, HR friends! 🙌 Uber&amp;#39;s engineers were told to go all-in on AI coding tools. They did. So enthusiastically,</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#12 · Fri, 05 Jun 2026 10:45:21 -0400</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Let&#x27;s Talk Real-Life Money Decisions</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Sago &lt;Participate@focusgroup.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Hello Melissa We are currently offering $100.00 to our members who qualify and complete a research study on Financial Experiences. Pre-Qualification Q</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#14 · Fri, 05 Jun 2026 06:22:42 -0600</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">It&#x27;s Here: The Sandal Savings Event!</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Shoe Station &lt;customerservice@email.shoestation.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Shop Sandals under $20 + Buy 1 Get 1 FREE Shoe Station You Have 138 Points | Shoe Perks Member $10 coupon offer Sandal Savings Event Sandal Blowout Wo</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#23 · Fri, 05 Jun 2026 14:15:31 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">👨‍💻 [Free Webinar] Why HR Software Decisions Fail</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Phil Strazzulla &lt;ssr-newsletter@mail.beehiiv.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Learn practical ways to build buy-in for your HR software ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#29 · Fri, 5 Jun 2026 14:04:57 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Your subscription ends tomorrow.</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> The CHRO Office &lt;thehroffice@substack.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Melissa, Thank you for your support as a paying subscriber to The CHRO Office. Your paid subscription is about to expire tomorrow. To keep all the ben</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#34 · Fri, 05 Jun 2026 13:50:50 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Melissa Daily Briefing - 2026-06-05 13:50 UTC</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Melissa Daily Briefing &lt;melissaw212@gmail.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Executive Briefing 👋 Good Morning, Melissa! Friday, June 5, 2026 | Prepared by your Executive Chief of Staff 📧 50 Emails Reviewed 📅 9 Calendar Events </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#39 · Fri, 05 Jun 2026 13:29:56 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Important Update About Your Research Opportunities</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Focus Group &lt;participate@focusgroup.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Hello Melissa, We&amp;#39;re reaching out to share an important update about your Focus Group membership and new opportunities available to you. Based on </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>
</div>

<div style="background:#f7fafc; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Promotional / Retail (7)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#5 · Fri,  5 Jun 2026 15:05:00 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Meet Daisy</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Fayced Aesthetics NYC &lt;info@faycedaestheticsnyc.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Our Newest Nurse Injector + Exclusive New Patient Offer Meet the newest member of the Fayced Aesthetics team Daisy 🌼 We are so excited to introduce th</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#13 · Fri, 05 Jun 2026 14:50:06 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Melissa, flash sale starts now!⏰</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> BellaVitashop &lt;bellavitashop@tiktokshop.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Visit the shop and save big today! ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#18 · Fri, 5 Jun 2026 16:17:58 +0200</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">PUMA x SALEHE BEMBURY Is Here</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> PUMA &lt;email@email.us.puma.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Taking the show on the road ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌ ͏‌</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#19 · Fri, 5 Jun 2026 14:18:28 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">15% Off Catering this Summer!</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Chip City &lt;messages+ml5y60byxd19g@squaremktg.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Have questions? Reply to this email and we&amp;#39;ll respond as soon as possible. Business Website Instagram Account Twitter Account Chip City 15-32 127t</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#43 · Fri, 05 Jun 2026 07:16:55 -0600</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Invite your team to Slack today!</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Slack &lt;no-reply@email.slackhq.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">We&amp;#39;ll help you and your team get started Your team is on a free trial of Pro. Try in Slack → Slack from Salesforce It&amp;#39;s time—give Slack a try </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#46 · Fri, 5 Jun 2026 13:06:12 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Apple’s Starlink Update Sparks Huge Earning Opportunity</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Pre-IPO Offering ✍🏻 Capital Noted&quot; &lt;news@editor.capitalnoted.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Apple just secretly added Starlink satellite support to iPhones through iOS 18.3. One of the biggest potential winners? Mode Mobile. Capital Noted log</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#50 · Fri, 05 Jun 2026 13:02:26 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">The Kind of Find You Didn&#x27;t Know You Needed</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;🔥 Mystery Deal 🔥&quot; &lt;marketing@mysterydeal.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">A handful of unexpected picks that have a way of sticking around. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>
</div>

<div style="background:#fff5f5; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Security / Risk (2)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#28 · Fri, 05 Jun 2026 07:33:00 -0600</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Workout drawer: refreshed ✨ Snag 50% OFF all active*</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Old Navy &lt;oldnavy@email.oldnavy.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Plus, Encore Members get ✨ free shipping ✨ on $50+ orders ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Act / Delete if scam</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#37 · Fri, 5 Jun 2026 09:32:18 -0400 (EDT)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">📓 motivation with $0</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Hebba Youssef &lt;ihateithere@workweek.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Proving impact through metrics + keeping people engaged without a budget. I Hate It Here Hebba Youssef Jun 5th, 2026 Read in browser In partnership wi</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Act / Delete if scam</div>
</div>
</div>

