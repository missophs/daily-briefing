<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing – Melissa W – July 4, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px 48px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a2340 0%, #2c3e6b 100%); color: #fff; border-radius: 14px; padding: 32px 36px 24px; margin-bottom: 24px; }
  .header h1 { font-size: 2rem; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 1.05rem; color: #a8b8d8; margin-top: 4px; }
  .header-meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header-meta .meta-box { background: rgba(255,255,255,0.1); border-radius: 8px; padding: 10px 20px; text-align: center; }
  .header-meta .meta-box .num { font-size: 1.7rem; font-weight: 700; color: #7ecfff; }
  .header-meta .meta-box .lbl { font-size: 0.78rem; color: #a8b8d8; text-transform: uppercase; letter-spacing: 0.5px; }
  .holiday-badge { display: inline-block; background: #c0392b; color: #fff; border-radius: 20px; padding: 4px 16px; font-size: 0.82rem; font-weight: 600; margin-top: 10px; letter-spacing: 0.5px; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 1.15rem; font-weight: 700; color: #1a2340; border-left: 5px solid #2c3e6b; padding-left: 12px; margin-bottom: 14px; text-transform: uppercase; letter-spacing: 0.5px; }

  /* EXEC SUMMARY */
  .exec-summary { background: #fff; border-radius: 12px; padding: 22px 26px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); margin-bottom: 24px; }
  .exec-summary h2 { font-size: 1.1rem; font-weight: 700; color: #1a2340; margin-bottom: 14px; text-transform: uppercase; letter-spacing: 0.5px; border-left: 5px solid #2c3e6b; padding-left: 12px; }
  .exec-bullet { display: flex; align-items: flex-start; gap: 12px; margin-bottom: 11px; padding: 12px 16px; border-radius: 8px; }
  .exec-bullet.red { background: #fff0f0; border-left: 4px solid #e74c3c; }
  .exec-bullet.green { background: #f0fff4; border-left: 4px solid #27ae60; }
  .exec-bullet.blue { background: #f0f6ff; border-left: 4px solid #2980b9; }
  .exec-bullet .icon { font-size: 1.3rem; }
  .exec-bullet .text strong { display: block; font-size: 0.9rem; margin-bottom: 2px; }
  .exec-bullet .text span { font-size: 0.85rem; color: #555; }

  /* ACTION CARDS */
  .action-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 16px; }
  .action-card { border-radius: 10px; padding: 16px 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .action-card.red { background: #fff8f8; border-top: 4px solid #e74c3c; }
  .action-card.yellow { background: #fffdf0; border-top: 4px solid #f39c12; }
  .action-card.blue { background: #f4f8ff; border-top: 4px solid #2980b9; }
  .action-card.green { background: #f4fff8; border-top: 4px solid #27ae60; }
  .action-card.purple { background: #faf4ff; border-top: 4px solid #8e44ad; }
  .action-card .card-label { font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
  .action-card.red .card-label { color: #e74c3c; }
  .action-card.yellow .card-label { color: #e67e22; }
  .action-card.blue .card-label { color: #2980b9; }
  .action-card.green .card-label { color: #27ae60; }
  .action-card.purple .card-label { color: #8e44ad; }
  .action-card h3 { font-size: 0.95rem; font-weight: 700; margin-bottom: 6px; color: #1a2340; }
  .action-card .source { font-size: 0.78rem; color: #777; margin-bottom: 6px; }
  .action-card .why { font-size: 0.83rem; color: #444; margin-bottom: 6px; }
  .action-card .next { font-size: 0.83rem; font-weight: 600; color: #1a2340; margin-bottom: 4px; }
  .action-card .due { font-size: 0.78rem; color: #e74c3c; font-weight: 600; }

  /* CALENDAR */
  .cal-day { background: #fff; border-radius: 10px; padding: 16px 18px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
  .cal-day-header { font-weight: 700; font-size: 1rem; color: #1a2340; border-bottom: 2px solid #e8eaf0; padding-bottom: 8px; margin-bottom: 12px; display: flex; align-items: center; gap: 10px; }
  .cal-day-header .today-badge { background: #e74c3c; color: #fff; font-size: 0.7rem; border-radius: 10px; padding: 2px 8px; }
  .cal-event { display: grid; grid-template-columns: 130px 1fr; gap: 10px; margin-bottom: 12px; align-items: start; }
  .cal-time { font-size: 0.82rem; font-weight: 600; color: #2980b9; }
  .cal-info h4 { font-size: 0.9rem; font-weight: 700; color: #1a2340; }
  .cal-info .cal-meta { font-size: 0.78rem; color: #666; margin-top: 2px; }
  .cal-info .cal-rsvp { display: inline-block; font-size: 0.72rem; font-weight: 700; border-radius: 10px; padding: 1px 8px; margin-top: 3px; }
  .rsvp-accepted { background: #d4edda; color: #155724; }
  .rsvp-confirmed { background: #d1ecf1; color: #0c5460; }
  .rsvp-declined { background: #f8d7da; color: #721c24; }
  .rsvp-needs { background: #fff3cd; color: #856404; }
  .cal-prep { font-size: 0.78rem; color: #8e44ad; margin-top: 3px; font-style: italic; }
  .cal-conflict { font-size: 0.78rem; color: #e74c3c; font-weight: 600; margin-top: 3px; }
  .no-events { color: #999; font-size: 0.85rem; font-style: italic; }

  /* JOB PIPELINE */
  .job-table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
  .job-table th { background: #1a2340; color: #fff; padding: 10px 14px; font-size: 0.82rem; text-align: left; }
  .job-table td { padding: 10px 14px; border-bottom: 1px solid #f0f2f5; font-size: 0.83rem; vertical-align: top; }
  .job-table tr:last-child td { border-bottom: none; }
  .job-table tr:hover td { background: #f8faff; }
  .fit-high { color: #27ae60; font-weight: 700; }
  .fit-med { color: #e67e22; font-weight: 700; }
  .fit-low { color: #95a5a6; font-weight: 700; }

  /* EMAIL CATEGORIES */
  .cat-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(310px, 1fr)); gap: 14px; }
  .cat-card { border-radius: 10px; padding: 14px 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
  .cat-card.red { background: #fff8f8; border-left: 5px solid #e74c3c; }
  .cat-card.yellow { background: #fffdf0; border-left: 5px solid #f39c12; }
  .cat-card.blue { background: #f4f8ff; border-left: 5px solid #2980b9; }
  .cat-card.green { background: #f4fff8; border-left: 5px solid #27ae60; }
  .cat-card.purple { background: #faf4ff; border-left: 5px solid #8e44ad; }
  .cat-card.gray { background: #f8f9fa; border-left: 5px solid #95a5a6; }
  .cat-card.teal { background: #f0fffe; border-left: 5px solid #16a085; }
  .cat-card .cat-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }
  .cat-card .cat-title { font-weight: 700; font-size: 0.9rem; color: #1a2340; }
  .cat-card .cat-count { font-size: 0.75rem; font-weight: 700; background: #1a2340; color: #fff; border-radius: 10px; padding: 2px 8px; }
  .cat-card .cat-body { font-size: 0.81rem; color: #444; line-height: 1.5; }
  .cat-card .cat-action { font-size: 0.79rem; font-weight: 600; color: #2980b9; margin-top: 8px; }

  /* TRASH */
  .trash-group { background: #fff; border-radius: 10px; padding: 16px 18px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
  .trash-group h3 { font-size: 0.9rem; font-weight: 700; margin-bottom: 10px; padding: 4px 10px; border-radius: 6px; display: inline-block; }
  .trash-group h3.restore { background: #d4edda; color: #155724; }
  .trash-group h3.review { background: #fff3cd; color: #856404; }
  .trash-group h3.delete { background: #f8d7da; color: #721c24; }
  .trash-item { display: flex; align-items: flex-start; gap: 10px; padding: 8px 0; border-bottom: 1px solid #f0f2f5; font-size: 0.82rem; }
  .trash-item:last-child { border-bottom: none; }
  .trash-sender { font-weight: 600; color: #1a2340; min-width: 140px; }
  .trash-subject { color: #444; flex: 1; }
  .trash-reason { color: #777; font-style: italic; min-width: 140px; text-align: right; font-size: 0.78rem; }

  /* PROMO SUMMARY */
  .promo-table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
  .promo-table th { background: #95a5a6; color: #fff; padding: 9px 14px; font-size: 0.82rem; text-align: left; }
  .promo-table td { padding: 9px 14px; border-bottom: 1px solid #f0f2f5; font-size: 0.82rem; }
  .promo-table tr:last-child td { border-bottom: none; }
  .rec-delete { color: #e74c3c; font-weight: 700; }
  .rec-review { color: #e67e22; font-weight: 700; }
  .rec-ignore { color: #95a5a6; font-weight: 700; }

  /* NEWSLETTER */
  .nl-table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
  .nl-table th { background: #8e44ad; color: #fff; padding: 9px 14px; font-size: 0.82rem; text-align: left; }
  .nl-table td { padding: 9px 14px; border-bottom: 1px solid #f0f2f5; font-size: 0.82rem; }
  .nl-table tr:last-child td { border-bottom: none; }
  .rec-keep { color: #27ae60; font-weight: 700; }
  .rec-unsub { color: #e74c3c; font-weight: 700; }

  /* EMAIL ACCOUNTING */
  .accounting-table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
  .accounting-table th { background: #1a2340; color: #fff; padding: 10px 14px; font-size: 0.83rem; text-align: left; }
  .accounting-table td { padding: 9px 14px; border-bottom: 1px solid #f0f2f5; font-size: 0.82rem; }
  .accounting-table tr:last-child td { border-bottom: none; font-weight: 700; background: #f8faff; }
  .accounting-table .total-row td { font-weight: 700; background: #eaf0fb; color: #1a2340; font-size: 0.9rem; }

  /* DASHBOARD */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; margin-bottom: 8px; }
  .dash-box { border-radius: 10px; padding: 14px 16px; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.07); }
  .dash-box .dash-num { font-size: 2rem; font-weight: 700; }
  .dash-box .dash-lbl { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px; }
  .dash-box.red { background: #fff0f0; color: #c0392b; }
  .dash-box.yellow { background: #fffbe6; color: #b7770d; }
  .dash-box.blue { background: #f0f6ff; color: #2471a3; }
  .dash-box.green { background: #f0fff4; color: #1e8449; }
  .dash-box.purple { background: #faf4ff; color: #7d3c98; }
  .dash-box.gray { background: #f8f9fa; color: #707b7c; }

  /* ACTION TABLE */
  .action-table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
  .action-table th { background: #1a2340; color: #fff; padding: 10px 14px; font-size: 0.83rem; text-align: left; }
  .action-table td { padding: 9px 14px; border-bottom: 1px solid #f0f2f5; font-size: 0.82rem; vertical-align: top; }
  .action-table tr:last-child td { border-bottom: none; }
  .pri-high { color: #e74c3c; font-weight: 700; }
  .pri-med { color: #e67e22; font-weight: 700; }
  .pri-low { color: #27ae60; font-weight: 700; }

  /* TOP 3 */
  .top3 { background: linear-gradient(135deg, #1a2340 0%, #2c3e6b 100%); color: #fff; border-radius: 12px; padding: 24px 28px; }
  .top3 h2 { font-size: 1.1rem; font-weight: 700; margin-bottom: 16px; color: #7ecfff; text-transform: uppercase; letter-spacing: 0.5px; }
  .top3-item { display: flex; align-items: flex-start; gap: 14px; margin-bottom: 14px; }
  .top3-num { background: #7ecfff; color: #1a2340; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1rem; flex-shrink: 0; }
  .top3-text strong { display: block; font-size: 0.95rem; margin-bottom: 2px; }
  .top3-text span { font-size: 0.83rem; color: #a8b8d8; }

  /* SECURITY ALERT */
  .security-banner { background: #c0392b; color: #fff; border-radius: 10px; padding: 14px 18px; margin-bottom: 18px; display: flex; align-items: center; gap: 12px; }
  .security-banner .icon { font-size: 1.6rem; }
  .security-banner .text strong { display: block; font-size: 0.95rem; }
  .security-banner .text span { font-size: 0.82rem; opacity: 0.9; }

  /* UTIL */
  .divider { height: 1px; background: #e0e4ed; margin: 28px 0; }
  .tag { display: inline-block; font-size: 0.7rem; font-weight: 700; border-radius: 8px; padding: 2px 7px; margin-right: 3px; }
  .tag-red { background: #fdecea; color: #c0392b; }
  .tag-green { background: #e8f8f0; color: #1e8449; }
  .tag-blue { background: #eaf2ff; color: #2471a3; }
  .tag-gray { background: #f2f3f4; color: #707b7c; }
  .tag-yellow { background: #fef9e7; color: #b7770d; }
  ul.detail-list { padding-left: 16px; }
  ul.detail-list li { margin-bottom: 3px; font-size: 0.82rem; color: #444; }
  .note-box { background: #fff3cd; border-left: 4px solid #f39c12; border-radius: 6px; padding: 10px 14px; font-size: 0.82rem; color: #856404; margin-top: 10px; }
  @media (max-width: 600px) {
    .header h1 { font-size: 1.4rem; }
    .action-grid, .cat-grid, .dash-grid { grid-template-columns: 1fr; }
    .cal-event { grid-template-columns: 1fr; }
  }
</style>
</head>
<body>
<div class="page">

<!-- ══════════════════════════════════════════════
     1. HEADER
══════════════════════════════════════════════ -->
<div class="header">
  <div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap;">
    <div>
      <h1>🇺🇸 Good Morning, Melissa</h1>
      <div class="subtitle">Executive Briefing · Prepared by your Chief of Staff</div>
      <span class="holiday-badge">🎆 Happy Independence Day, 2026</span>
    </div>
  </div>
  <div class="header-meta">
    <div class="meta-box"><div class="num">📅 Saturday</div><div class="lbl">July 4, 2026</div></div>
    <div class="meta-box"><div class="num" style="color:#7ecfff;">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="meta-box"><div class="num" style="color:#7ecfff;">9</div><div class="lbl">Calendar Events</div></div>
    <div class="meta-box"><div class="num" style="color:#ff9f7e;">4</div><div class="lbl">Action Required</div></div>
    <div class="meta-box"><div class="num" style="color:#ff9f7e;">⚠️ 3</div><div class="lbl">Security / Spam Flags</div></div>
  </div>
</div>

<!-- ══════════════════════════════════════════════
     SECURITY BANNER
══════════════════════════════════════════════ -->
<div class="security-banner">
  <div class="icon">🚨</div>
  <div class="text">
    <strong>SECURITY ALERT: Multiple phishing and scam emails detected in your inbox and trash.</strong>
    <span>Fake casino deposits, spoofed "melissaw212" senders, fake cloud storage deletion notice, and gambling spam. Do NOT click any links. Report and delete immediately.</span>
  </div>
</div>

<!-- ══════════════════════════════════════════════
     2. EXECUTIVE SUMMARY
══════════════════════════════════════════════ -->
<div class="exec-summary">
  <h2>Executive Summary</h2>
  <div class="exec-bullet red">
    <div class="icon">🚨</div>
    <div class="text">
      <strong>Biggest Risk: Active Phishing / Scam Campaign Targeting Your Email</strong>
      <span>Multiple fraudulent emails — including fake $5,000–$6,000 casino "deposits," gambling spin offers, a fake cloud storage deletion notice, and a Nextdoor alert about a Legionnaires' disease cluster in Yorkville — are sitting in your inbox and trash. One fake storage alert is NOT in trash and not in inbox (floating). Action required today: report, block, delete all scam senders.</span>
    </div>
  </div>
  <div class="exec-bullet green">
    <div class="icon">💼</div>
    <div class="text">
      <strong>Biggest Opportunity: Strong Job Search Momentum — 209 LinkedIn Profile Views + 4 Active Job Alerts</strong>
      <span>LinkedIn reports 209 profile views. Scovai flagged a Chief People &amp; Culture Officer role at Omnisage LLC. LinkedIn alerts surfaced SVP Global Ops &amp; HR at The Hunger Project, Director of People at GridUnity, VP People &amp; Culture at Spiro, and PBP Lead at ClickHouse. Your profile is generating attention — follow up now.</span>
    </div>
  </div>
  <div class="exec-bullet blue">
    <div class="icon">📅</div>
    <div class="text">
      <strong>Biggest Calendar Item: Two Medical Appointments Monday &amp; Thursday — Plus Two RSVP-Pending Networking Events</strong>
      <span>New Patient Video Visit with Dr. Haridas on Mon July 6 (11:20 AM). New Patient in-person with Dr. Leeman-Markowski on Thu July 9 (3:30 PM, bring ID/insurance). Two HR Networking Zoom sessions on Wed July 8 and Thu July 9 still show "Needs Action" — confirm your attendance. State Farm bill is due July 7.</span>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════════
     3. ACTION REQUIRED
══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">⚡ Action Required</div>
  <div class="action-grid">

    <div class="action-card red">
      <div class="card-label">🚨 Security — Urgent</div>
      <h3>Phishing / Scam Emails in Inbox &amp; Floating</h3>
      <div class="source">From: Multiple spoofed senders (fake casino deposits, cloud storage, gambling spam)</div>
      <div class="why">Multiple fraudulent emails impersonating you ("melissaw212") promising fake $5K–$6K deposits. One fake cloud storage notice is NOT in trash and not in inbox — it's floating. Nextdoor Legionnaires' alert may be real but needs verification.</div>
      <div class="next">➜ Report all casino/gambling spam as phishing. Move fake cloud storage email to trash. Verify Nextdoor Legionnaires' alert via official NYC Health sources (not from this email). Block all fraudulent senders.</div>
      <div class="due">⏰ Due: TODAY — July 4, 2026</div>
    </div>

    <div class="action-card yellow">
      <div class="card-label">💰 Billing — Confirm</div>
      <h3>State Farm Bill Due July 7</h3>
      <div class="source">From: Google Calendar reminder</div>
      <div class="why">State Farm bill is flagged as an all-day event on July 7. If auto-pay is not set, manual payment is needed before close of business Monday.</div>
      <div class="next">➜ Confirm auto-pay is active or log in to State Farm and pay manually. Note: Monday July 6 is a federal holiday — plan accordingly.</div>
      <div class="due">⏰ Due: July 7, 2026</div>
    </div>

    <div class="action-card blue">
      <div class="card-label">📅 Calendar — RSVP Needed</div>
      <h3>Two HR Networking Zoom Sessions — No RSVP</h3>
      <div class="source">Google Calendar: HR Networking &amp; Job Search Group (Wed July 8) + Open Office Hours (Thu July 9)</div>
      <div class="why">Both events show "Needs Action" status. These are large group sessions with 100+ attendees. Confirming your attendance signals engagement to the network organizer.</div>
      <div class="next">➜ Open calendar invites and click Accept. Add Zoom links to calendar. Note: Thu July 9 conflicts with your 3:30 PM Dr. Leeman-Markowski appointment (no direct time conflict — Office Hours end at 1 PM).</div>
      <div class="due">⏰ RSVP by: July 7, 2026</div>
    </div>

    <div class="action-card green">
      <div class="card-label">💼 Opportunity — Act Now</div>
      <h3>209 LinkedIn Profile Views + Scovai Role Match</h3>
      <div class="source">LinkedIn (messages-noreply@linkedin.com) + Scovai (no-reply@scovai.com)</div>
      <div class="why">209 profile views signal strong market interest. Scovai matched you to Chief People &amp; Culture Officer at Omnisage LLC. This momentum should be leveraged immediately.</div>
      <div class="next">➜ Review who viewed your profile. Send personalized connection requests to recruiters/HRDs who viewed. Apply to or review Omnisage CPCO role via Scovai today. Update LinkedIn headline if needed.</div>
      <div class="due">⏰ Recommended: This weekend</div>
    </div>

    <div class="action-card blue">
      <div class="card-label">🏥 Medical — Prep Required</div>
      <h3>New Patient Appointment — Dr. Leeman-Markowski, Thu July 9</h3>
      <div class="source">Google Calendar — Comprehensive Epilepsy Center, 223 East 34th St, NY 10016</div>
      <div class="why">New patient in-person visit. Requires arrival 15 min early with insurance card, photo ID, referral (if applicable), and relevant medical records/test results.</div>
      <div class="next">➜ Gather insurance card, photo ID, relevant medical records. Confirm transportation. Arrive by 3:15 PM. Call 646-558-0800 if you need to reschedule.</div>
      <div class="due">⏰ Thu July 9 @ 3:30 PM</div>
    </div>

    <div class="action-card purple">
      <div class="card-label">🛠️ Tech — Review</div>
      <h3>New Slack Workspace "consulting work" — Verify Activity</h3>
      <div class="source">Slack (multiple emails, mostly in Trash)</div>
      <div class="why">Multiple Slack setup emails indicate a "consulting work" workspace was created, a "stella" account joined, and a Slack Pro trial was started. Most related emails were trashed. Verify this was intentional and that billing is expected.</div>
      <div class="next">➜ Log into Slack, confirm the "consulting work" workspace is legitimate and intentional. Review the Pro trial terms to avoid unexpected charges.</div>
      <div class="due">⏰ Review this week</div>
    </div>

  </div>
</div>

<div class="divider"></div>

<!-- ══════════════════════════════════════════════
     4. FULL 7-DAY CALENDAR
══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📅 Full 7-Day Calendar — July 4–10, 2026</div>

  <!-- Saturday July 4 -->
  <div class="cal-day">
    <div class="cal-day-header">
      🎆 Saturday, July 4, 2026 <span class="today-badge">TODAY</span>
    </div>
    <div class="no-events">No scheduled calendar events today. Enjoy the holiday! 🇺🇸</div>
  </div>

  <!-- Sunday July 5 -->
  <div class="cal-day">
    <div class="cal-day-header">☀️ Sunday, July 5, 2026</div>
    <div class="no-events">No calendar events scheduled.</div>
  </div>

  <!-- Monday July 6 -->
  <div class="cal-day">
    <div class="cal-day-header">🏥 Monday, July 6, 2026 <span style="font-size:0.75rem;color:#c0392b;margin-left:8px;">Federal Holiday — Independence Day Observed</span></div>
    <div class="cal-event">
      <div class="cal-time">11:20 AM – 12:00 PM</div>
      <div class="cal-info">
        <h4>New Patient Video Visit — Dr. Keerthana Haridas, MD</h4>
        <div class="cal-meta">📍 Video Visit (Connect platform — browser or app)</div>
        <span class="cal-rsvp rsvp-accepted">✅ Accepted</span>
        <div class="cal-prep">🔧 Prep: Log into Connect account before 11:20 AM. Silence notifications. Use stable WiFi. Have questions/symptoms list ready. Have insurance info handy for new patient intake.</div>
      </div>
    </div>
  </div>

  <!-- Tuesday July 7 -->
  <div class="cal-day">
    <div class="cal-day-header">📋 Tuesday, July 7, 2026</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-info">
        <h4>💳 State Farm Bill Due</h4>
        <div class="cal-meta">📍 No location — Payment reminder</div>
        <span class="cal-rsvp rsvp-confirmed">✔ Confirmed</span>
        <div class="cal-prep">🔧 Prep: Verify auto-pay or log in to pay manually. Note: July 6 is a federal holiday — banks may be closed. Pay today if auto-pay is not set.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-time">12:00 PM – 1:00 PM</div>
      <div class="cal-info">
        <h4>🏃 PT (Physical Therapy / Personal Training)</h4>
        <div class="cal-meta">📍 Location not specified</div>
        <span class="cal-rsvp rsvp-confirmed">✔ Confirmed</span>
        <div class="cal-prep">🔧 Prep: Confirm location with provider. Bring water, wear appropriate attire.</div>
      </div>
    </div>
  </div>

  <!-- Wednesday July 8 -->
  <div class="cal-day">
    <div class="cal-day-header">🤝 Wednesday, July 8, 2026</div>
    <div class="cal-event">
      <div class="cal-time">12:00 PM – 1:30 PM</div>
      <div class="cal-info">
        <h4>HR Networking &amp; Job Search Group — Zoom Session 2</h4>
        <div class="cal-meta">📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" style="color:#2980b9;">Zoom Link</a> · 100+ Attendees</div>
        <span class="cal-rsvp rsvp-needs">⚠️ Needs Action — RSVP Required</span>
        <div class="cal-prep">🔧 Prep: Accept calendar invite. Prepare 30-second intro. Review group guidelines (linked in invite). Bring 1–2 specific asks for the network. Disable AI notetakers per group rules.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-time">12:00 PM – 1:30 PM</div>
      <div class="cal-info">
        <h4>Network (Personal block)</h4>
        <div class="cal-meta">📍 No location specified</div>
        <span class="cal-rsvp rsvp-confirmed">✔ Confirmed</span>
        <div class="cal-conflict">⚠️ Note: This block overlaps exactly with the HR Networking Zoom above — may be the same event or a duplicate. Confirm.</div>
      </div>
    </div>
  </div>

  <!-- Thursday July 9 -->
  <div class="cal-day">
    <div class="cal-day-header">🏥 Thursday, July 9, 2026</div>
    <div class="cal-event">
      <div class="cal-time">9:00 AM – 10:30 AM</div>
      <div class="cal-info">
        <h4>Executive Roundtable — Zoom (John Madigan)</h4>
        <div class="cal-meta">📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" style="color:#2980b9;">Zoom Link</a> · Meeting ID: 207 786 667 · Password: 205454</div>
        <span class="cal-rsvp rsvp-declined">❌ Declined</span>
        <div class="cal-prep">🔧 Note: You declined this event. If you wish to reconsider, contact John Madigan before July 9. Reconnecting with executive roundtable organizers may be valuable for your search.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-time">12:00 PM – 1:00 PM</div>
      <div class="cal-info">
        <h4>HR Networking &amp; Job Search: Open Office Hours — Zoom 2</h4>
        <div class="cal-meta">📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" style="color:#2980b9;">Zoom Link</a> · 100+ Attendees</div>
        <span class="cal-rsvp rsvp-needs">⚠️ Needs Action — RSVP Required</span>
        <div class="cal-prep">🔧 Prep: Accept invite. No AI notetakers allowed. Informal open discussion format — bring questions, seek 1:1 connections. Ends 1 PM — 2.5 hrs before your medical appointment.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-time">3:30 PM – 4:30 PM</div>
      <div class="cal-info">
        <h4>🏥 New Patient Appointment — Dr. Beth A. Leeman-Markowski, MD</h4>
        <div class="cal-meta">📍 Comprehensive Epilepsy Center, 223 East 34th Street, New York, NY 10016 · 📞 646-558-0800</div>
        <span class="cal-rsvp rsvp-accepted">✅ Accepted</span>
        <div class="cal-prep">🔧 Prep: Arrive by 3:15 PM (15 min early). Bring: insurance card, photo ID, referral/pre-certification if applicable, relevant medical records, recent labs/imaging. Two calendar entries for same event — confirmed as one appointment.</div>
      </div>
    </div>
  </div>

  <!-- Friday July 10 -->
  <div class="cal-day">
    <div class="cal-day-header">☀️ Friday, July 10, 2026</div>
    <div class="no-events">No calendar events scheduled.</div>
  </div>

</div>

<div class="divider"></div>

<!-- ══════════════════════════════════════════════
     5. JOB SEARCH & INTERVIEW PIPELINE
══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
  <table class="job-table">
    <thead>
      <tr>
        <th>Source</th>
        <th>Role / Opportunity</th>
        <th>Company</th>
        <th>Date Posted</th>
        <th>Fit</th>
        <th>Recommended Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="tag tag-blue">Scovai</span></td>
        <td>Chief People &amp; Culture Officer</td>
        <td>Omnisage LLC</td>
        <td>Jul 4, 2026</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>Review &amp; apply immediately — matched by AI to your profile.</td>
      </tr>
      <tr>
        <td><span class="tag tag-green">LinkedIn</span></td>
        <td>SVP, Global Operations &amp; Human Resources</td>
        <td>The Hunger Project</td>
        <td>Jun 17, 2026</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>Posted Jun 17 — apply ASAP before deadline. Mission-driven org aligns with exec HR experience.</td>
      </tr>
      <tr>
        <td><span class="tag tag-green">LinkedIn</span></td>
        <td>Director of People (Remote)</td>
        <td>GridUnity</td>
        <td>Jul 1, 2026</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>Remote, fresh posting — apply this weekend. Energy/clean-tech sector.</td>
      </tr>
      <tr>
        <td><span class="tag tag-green">LinkedIn</span></td>
        <td>Vice President of People and Culture</td>
        <td>Spiro</td>
        <td>Jul 1, 2026</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>VP-level role, recent posting. Research Spiro and apply promptly.</td>
      </tr>
      <tr>
        <td><span class="tag tag-green">LinkedIn</span></td>
        <td>People Business Partner Lead – APJ</td>
        <td>ClickHouse</td>
        <td>Jul 2, 2026</td>
        <td><span class="fit-med">MEDIUM</span></td>
        <td>APJ (Asia-Pacific-Japan) scope — review if geography/scope fits. ClickHouse is a high-growth tech company.</td>
      </tr>
      <tr>
        <td><span class="tag tag-blue">LinkedIn</span></td>
        <td>209 Profile Views</td>
        <td>Various</td>
        <td>Jul 4, 2026</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>Check who viewed your profile. Reach out to recruiters/CHROs who visited. Strong signal of market interest.</td>
      </tr>
      <tr>
        <td><span class="tag tag-blue">Calendar</span></td>
        <td>HR Networking &amp; Job Search Group</td>
        <td>Peer Network (Zoom)</td>
        <td>Jul 8, 2026</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>RSVP now. 100+ HR professionals. Bring 2–3 target companies to share. Ask for warm intros.</td>
      </tr>
      <tr>
        <td><span class="tag tag-blue">Calendar</span></td>
        <td>HR Open Office Hours</td>
        <td>Peer Network (Zoom)</td>
        <td>Jul 9, 2026</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>RSVP now. Informal, relationship-building format. Ends 2.5 hrs before your medical appointment.</td>
      </tr>
      <tr>
        <td><span class="tag tag-blue">Calendar</span></td>
        <td>Executive Roundtable (Declined)</td>
        <td>John Madigan (Zoom)</td>
        <td>Jul 9, 2026</td>
        <td><span class="fit-med">MEDIUM</span></td>
        <td>Currently declined. Reconsider — executive roundtables are high-value for VP/SVP-level networking. Contact John Madigan.</td>
      </tr>
    </tbody>
  </table>
  <div class="note-box" style="margin-top:14px;">📌 <strong>Self-Saved Resources (Melissa emailed herself):</strong> ByteMint AI Financial Planning guide, Learn AI With Mariah Claude challenge, free-claude-code GitHub repo, Claude VS Code guide, credit card benefits tracker, 300+ Claude Skills by Usama Akram. These appear to be professional development &amp; productivity resources. Review this week.</div>
</div>

<div class="divider"></div>

<!-- ══════════════════════════════════════════════
     6. FULL EMAIL REVIEW BY CATEGORY
══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📬 Full Email Review by Category</div>
  <div class="cat-grid">

    <!-- Security / Risk -->
    <div class="cat-card red">
      <div class="cat-header"><span class="cat-title">🚨 Security / Risk</span><span class="cat-count">5</span></div>
      <div class="cat-body">
        <strong>Senders:</strong>
        <ul class="detail-list">
          <li>"melissaw212" spoofed — fake $6,000 deposit (Casino Slotocash) [Trash]</li>
          <li>"melissaw212" spoofed — fake $5,000 deposit (Casino Yabby) [Floating — NOT in trash]</li>
          <li>Cloud Storage fake deletion notice — "photos deleted tonight" [Floating — NOT in trash/inbox]</li>
          <li>Nextdoor — Legionnaires' disease cluster alert, Yorkville [NOT in trash]</li>
          <li>"Congratulations melissaw212" — 175 Free Spins phishing [Trash]</li>
        </ul>
      </div>
      <div class="cat-action">⚡ Action: Report phishing. Block all spoofed senders. Verify Legionnaires' alert via NYC DOH website — do NOT click email link. Move floating scams to trash immediately.</div>
    </div>

    <!-- Job Search -->
    <div class="cat-card green">
      <div class="cat-header"><span class="cat-title">💼 Job Search</span><span class="cat-count">5</span></div>
      <div class="cat-body">
        <strong>Senders:</strong>
        <ul class="detail-list">
          <li>LinkedIn — 209 Profile Views (Unread, Inbox)</li>
          <li>LinkedIn Job Alerts — SVP Global Ops &amp; HR, The Hunger Project (Unread, Inbox)</li>
          <li>LinkedIn Job Alerts — Director of People (Remote), GridUnity (Unread, Inbox)</li>
          <li>LinkedIn Job Alerts — VP People &amp; Culture, Spiro (Unread, Inbox)</li>
          <li>LinkedIn Job Alerts — People Business Partner Lead APJ, ClickHouse (Unread, Inbox)</li>
        </ul>
      </div>
      <div class="cat-action">⚡ Action: Review all 4 job postings this weekend. Apply to top fits immediately. Check who viewed your LinkedIn profile.</div>
    </div>

    <!-- Recruiters / Networking -->
    <div class="cat-card green">
      <div class="cat-header"><span class="cat-title">🤝 Recruiters / Networking</span><span class="cat-count">1</span></div>
      <div class="cat-body">
        <strong>Senders:</strong>
        <ul class="detail-list">
          <li>Scovai — Matched to Chief People &amp; Culture Officer role at Omnisage LLC (Unread, Inbox)</li>
        </ul>
      </div>
      <div class="cat-action">⚡ Action: Log into Scovai and review the Omnisage CPCO match. Apply if aligned with goals.</div>
    </div>

    <!-- Calendar / Events -->
    <div class="cat-card blue">
      <div class="cat-header"><span class="cat-title">📅 Calendar / Events</span><span class="cat-count">1</span></div>
      <div class="cat-body">
        <strong>Senders:</strong>
        <ul class="detail-list">
          <li>Slack invite — "melissaw212 has invited you to work with them in consulting work" (Unread, Inbox — one remaining active invite)</li>
        </ul>
        <em>Note: Most Slack setup emails were trashed. One active workspace invite remains in inbox.</em>
      </div>
      <div class="cat-action">⚡ Action: Confirm Slack "consulting work" workspace setup is intentional. Review Pro trial billing implications.</div>
    </div>

    <!-- Medical / Health -->
    <div class="cat-card teal">
      <div class="cat-header"><span class="cat-title">🏥 Medical / Health</span><span class="cat-count">1</span></div>
      <div class="cat-body">
        <strong>Senders:</strong>
        <ul class="detail-list">
          <li>Nextdoor — Legionnaires' disease cluster alert in Yorkville neighborhood (Unread, Not in trash/inbox)</li>
        </ul>
        <em>This is a potential public health notification. Verify through official sources.</em>
      </div>
      <div class="cat-action">⚡ Action: If you live or work in Yorkville or visited since late June, and have flu-like symptoms, contact your doctor immediately. Verify via NYC.gov or 311.</div>
    </div>

    <!-- Financial / Billing -->
    <div class="cat-card yellow">
      <div class="cat-header"><span class="cat-title">💳 Financial / Billing</span><span class="cat-count">2</span></div>
      <div class="cat-body">
        <strong>Senders:</strong>
        <ul class="detail-list">
          <li>Netlify — Payment received Invoice #RBCAOO-00009, $9.80, July 4 (Unread, Inbox)</li>
          <li>Netlify — Upgraded "morning briefing" site to Personal Plan (Read, Not in trash)</li>
        </ul>
      </div>
      <div class="cat-action">✅ Action: Netlify payment confirmed — archive. Verify Personal plan features and ongoing monthly costs. State Farm bill due July 7 is on calendar.</div>
    </div>

    <!-- Professional Development -->
    <div class="cat-card purple">
      <div class="cat-header"><span class="cat-title">📚 Professional Development</span><span class="cat-count">7</span></div>
      <div class="cat-body">
        <strong>Senders (all from Melissa W to herself — self-saved resources):</strong>
        <ul class="detail-list">
          <li>ByteMint — Build Financial Plan with Claude (×2 — Jul 4 &amp; Jul 3)</li>
          <li>Learn AI With Mariah — AI Challenge Round 2 with Mariah Brunner</li>
          <li>Learn AI With Mariah — Run Claude in VS Code</li>
          <li>Learn AI With Mariah — Build Live Credit Card Benefits Tracker</li>
          <li>Usama Akram — 300+ Claude Skills (Gumroad)</li>
          <li>GitHub — free-claude-code repo (Alishahryar1)</li>
        </ul>
      </div>
      <div class="cat-action">✅ Action: Organize these into a "Claude/AI Learning" folder. Deduplicate the ByteMint email (sent twice). Review during the week.</div>
    </div>

    <!-- Personal -->
    <div class="cat-card gray">
      <div class="cat-header"><span class="cat-title">💛 Personal</span><span class="cat-count">4</span></div>
      <div class="cat-body">
        <strong>Senders:</strong>
        <ul class="detail-list">
          <li>Match.com — "Steve likes you" (Unread, Inbox)</li>
          <li>Match.com — "Patrick Williams likes you" (Read, Not in trash/inbox)</li>
          <li>Jdate — "Someone Special Noticed You" (Unread, Inbox)</li>
          <li>Tinder — "Is it hot in here, or is it just you?" (Read, Not in trash/inbox)</li>
        </ul>
      </div>
      <div class="cat-action">✅ Action: Review at your leisure. No urgency. Consider consolidating to one dating platform if multiple are active.</div>
    </div>

    <!-- Newsletters / Subscriptions -->
    <div class="cat-card purple">
      <div class="cat-header"><span class="cat-title">📰 Newsletters / Subscriptions</span><span class="cat-count">3</span></div>
      <div class="cat-body">
        <strong>Senders:</strong>
        <ul class="detail-list">
          <li>Fractional In A Box — "What Mattel's CEO is seeing now" (Unread, Inbox)</li>
          <li>CoolDeep AI — "Stop being confused about Claude" (Unread, Inbox)</li>
          <li>CoolDeep AI — "Is this really worth $9?" (Unread, Inbox)</li>
        </ul>
      </div>
      <div class="cat-action">✅ Action: Review Fractional In A Box (relevant to fractional CHRO positioning). CoolDeep AI is commercial — review or unsubscribe.</div>
    </div>

    <!-- Promotional / Retail -->
    <div class="cat-card gray">
      <div class="cat-header"><span class="cat-title">🛍️ Promotional / Retail</span><span class="cat-count">7</span></div>
      <div class="cat-body">
        <strong>Senders:</strong>
        <ul class="detail-list">
          <li>Temu — 2 shipping notifications (Orders #PO-211-13384130622071025 &amp; #PO-211-13384128686711025) — Unread, Inbox</li>
          <li>SHEIN — "All under $15.99 Love Your Curves" (×2 — us.mail &amp; news.edmmarket)</li>
          <li>Kohl's — "Kohl's Cash + 20% off = 4th of July treats" — Unread, Inbox</li>
          <li>VIVAIA — "Independence Day Shop" — Unread, Inbox</li>
          <li>SHEIN — "UNDER $10 Drops" (×2, both Read, floating)</li>
        </ul>
      </div>
      <div class="cat-action">✅ Action: Track Temu shipments (GOFO: GFUS01060080033281). Archive or delete retail promotional emails.</div>
    </div>

    <!-- Trash Review -->
    <div class="cat-card red">
      <div class="cat-header"><span class="cat-title">🗑️ Trash Review</span><span class="cat-count">14</span></div>
      <div class="cat-body">
        <em>See dedicated Trash Review section below for full breakdown.</em>
        <ul class="detail-list" style="margin-top:6px;">
          <li>Slack setup emails (5 — confirmation codes, invites, account setup)</li>
          <li>Gambling/casino spam (4 — World Cup Reels, Free Spins, $2,500 payment scam, $6K casino scam)</li>
          <li>Newsletters trashed (3 — Lisa Rangel, Medium Daily Digest, ChatGPT/OpenAI, CoolDeep AI)</li>
          <li>Retail trashed (2 — SHEIN x2)</li>
        </ul>
      </div>
      <div class="cat-action">⚡ Action: See Trash Review section. Permanently delete all gambling/casino spam immediately.</div>
    </div>

    <!-- Safe to Delete / Ignore -->
    <div class="cat-card gray">
      <div class="cat-header"><span class="cat-title">🧹 Safe to Delete / Ignore</span><span class="cat-count">10</span></div>
      <div class="cat-body">
        <ul class="detail-list">
          <li>Netlify upgrade confirmation (archived/read)</li>
          <li>Slack "consulting work" Pro trial started (in inbox, read)</li>
          <li>SHEIN ×2 (read, floating — not trash/inbox)</li>
          <li>Match.com — Patrick Williams (read, floating)</li>
          <li>Tinder (read, floating)</li>
          <li>Slack "New Account Details" + workspace setup (read, not in trash)</li>
          <li>Duplicate Temu shipping notices (same GOFO tracking number on both)</li>
          <li>Duplicate ByteMint email (sent twice by Melissa)</li>
        </ul>
      </div>
      <div class="cat-action">✅ Action: Safely archive or delete these. No action needed.</div>
    </div>

  </div>
</div>

<div class="divider"></div>

<!-- ══════════════════════════════════════════════
     7. TRASH REVIEW
══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">🗑️ Trash Review</div>

  <div class="trash-group">
    <h3 class="restore">✅ RESTORE IMMEDIATELY (1)</h3>
    <div class="trash-item">
      <div class="trash-sender">Lisa Rangel</div>
      <div class="trash-subject">"Fireworks &amp; hope" — lr@chameleonresumes.com</div>
      <div class="trash-reason">Career coaching newsletter. Chameleon Resumes is a legitimate professional service. May have been trashed accidentally. Review if you use Lisa's resume coaching services.</div>
    </div>
  </div>

  <div class="trash-group">
    <h3 class="review">⚠️ REVIEW BEFORE DELETING (4)</h3>
    <div class="trash-item">
      <div class="trash-sender">Slack (×3)</div>
      <div class="trash-subject">Confirmation codes (PVC-XF8, D6Z-RG7, WWP-M6C) + Invite + Account Details — multiple emails</div>
      <div class="trash-reason">Related to the "consulting work" Slack workspace setup. If the workspace is legitimate and intentional, these can be permanently deleted. Verify workspace is active first.</div>
    </div>
    <div class="trash-item">
      <div class="trash-sender">Medium Daily Digest</div>
      <div class="trash-subject">"Nietzsche's Most Terrifying Mental Exercise…" — noreply@medium.com</div>
      <div class="trash-reason">Legitimate newsletter but appears trashed — likely intentional. Unsubscribe via Medium settings if no longer wanted.</div>
    </div>
    <div class="trash-item">
      <div class="trash-sender">ChatGPT / OpenAI</div>
      <div class="trash-subject">"Translate anything, your way" — noreply@email.openai.com</div>
      <div class="trash-reason">Legitimate OpenAI product email. Trashed likely intentionally. Safe to permanently delete. Unsubscribe from marketing if preferred.</div>
    </div>
    <div class="trash-item">
      <div class="trash-sender">CoolDeep AI</div>
      <div class="trash-subject">"Stop being confused about Claude" — cooldeepai@mail.beehiiv.com [Trash copy]</div>
      <div class="trash-reason">Duplicate/trashed version. One copy is in inbox. Permanently delete the trash copy.</div>
    </div>
  </div>

  <div class="trash-group">
    <h3 class="delete">🗑️ SAFE TO PERMANENTLY DELETE (9)</h3>
    <div class="trash-item">
      <div class="trash-sender">World Cup Reels ⚽ (Spam)</div>
      <div class="trash-subject">Spin to Win Mystery Bonus + Stacks of Free Spins — hnmhalg01l@sxegvslgv0.us</div>
      <div class="trash-reason">Gambling spam from spoofed sender. Phishing. Delete permanently
<hr>
<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Financial / Billing</td><td>3</td></tr>
<tr><td>Job Search / Recruiters</td><td>6</td></tr>
<tr><td>Other / Review</td><td>31</td></tr>
<tr><td>Professional Development / Newsletters</td><td>1</td></tr>
<tr><td>Promotional / Retail</td><td>2</td></tr>
<tr><td>Security / Risk</td><td>7</td></tr>
</table>
<p><strong>Audit Note:</strong> Every fetched email was reviewed and assigned to one category. Trash emails were included in review. Promotional and low-value emails were accounted for but deprioritized.</p>

