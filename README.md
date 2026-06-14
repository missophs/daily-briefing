<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Melissa's Executive Briefing — Sunday, June 14, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 16px; padding: 32px 36px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px; }
  .header-left h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header-left .subtitle { color: #a8b4c8; font-size: 14px; margin-top: 4px; }
  .header-left .date { color: #e2c275; font-size: 16px; font-weight: 600; margin-top: 8px; }
  .header-stats { display: flex; gap: 20px; flex-wrap: wrap; }
  .stat-pill { background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); border-radius: 10px; padding: 12px 20px; text-align: center; }
  .stat-pill .num { font-size: 26px; font-weight: 800; color: #e2c275; }
  .stat-pill .lbl { font-size: 11px; color: #a8b4c8; text-transform: uppercase; letter-spacing: 0.5px; }

  /* SECTIONS */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 18px; font-weight: 700; color: #1a1a2e; margin-bottom: 14px; padding-bottom: 8px; border-bottom: 3px solid #0f3460; display: flex; align-items: center; gap: 8px; }
  .section-title .icon { font-size: 20px; }

  /* EXECUTIVE SUMMARY */
  .exec-summary { background: #fff; border-radius: 12px; border-left: 5px solid #0f3460; padding: 20px 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .exec-bullet { display: flex; gap: 12px; align-items: flex-start; padding: 10px 0; border-bottom: 1px solid #eef0f4; }
  .exec-bullet:last-child { border-bottom: none; }
  .exec-bullet .badge { flex-shrink: 0; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 700; text-transform: uppercase; }
  .badge-red { background: #fde8e8; color: #b91c1c; }
  .badge-green { background: #dcfce7; color: #15803d; }
  .badge-blue { background: #dbeafe; color: #1d4ed8; }
  .badge-yellow { background: #fef9c3; color: #92400e; }
  .badge-purple { background: #f3e8ff; color: #7e22ce; }
  .badge-gray { background: #f1f5f9; color: #475569; }

  /* CARDS */
  .cards-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 16px; }
  .card { border-radius: 12px; padding: 18px 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .card-red { background: #fff5f5; border-left: 5px solid #dc2626; }
  .card-yellow { background: #fffbeb; border-left: 5px solid #f59e0b; }
  .card-blue { background: #eff6ff; border-left: 5px solid #2563eb; }
  .card-green { background: #f0fdf4; border-left: 5px solid #16a34a; }
  .card-purple { background: #faf5ff; border-left: 5px solid #9333ea; }
  .card-gray { background: #f8fafc; border-left: 5px solid #94a3b8; }
  .card-title { font-weight: 700; font-size: 14px; margin-bottom: 4px; }
  .card-meta { font-size: 11px; color: #64748b; margin-bottom: 8px; }
  .card-body { font-size: 13px; color: #374151; }
  .card-action { margin-top: 10px; background: rgba(0,0,0,0.05); border-radius: 6px; padding: 8px 10px; font-size: 12px; }
  .card-label { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 6px; }
  .label-red { background: #dc2626; color: #fff; }
  .label-yellow { background: #f59e0b; color: #fff; }
  .label-blue { background: #2563eb; color: #fff; }
  .label-green { background: #16a34a; color: #fff; }
  .label-purple { background: #9333ea; color: #fff; }
  .label-gray { background: #94a3b8; color: #fff; }

  /* CALENDAR */
  .cal-day { background: #fff; border-radius: 12px; margin-bottom: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); overflow: hidden; }
  .cal-day-header { background: #0f3460; color: #fff; padding: 10px 20px; font-weight: 700; font-size: 14px; display: flex; justify-content: space-between; align-items: center; }
  .cal-day-header .day-label { font-size: 11px; opacity: 0.7; text-transform: uppercase; letter-spacing: 0.5px; }
  .cal-event { padding: 14px 20px; border-bottom: 1px solid #eef0f4; display: grid; grid-template-columns: 100px 1fr; gap: 12px; }
  .cal-event:last-child { border-bottom: none; }
  .cal-time { font-weight: 700; color: #0f3460; font-size: 13px; }
  .cal-name { font-weight: 600; font-size: 14px; }
  .cal-detail { font-size: 12px; color: #64748b; margin-top: 3px; }
  .cal-status { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-top: 4px; }
  .status-confirmed { background: #dcfce7; color: #15803d; }
  .status-accepted { background: #dbeafe; color: #1d4ed8; }
  .status-needs { background: #fef9c3; color: #92400e; }
  .status-declined { background: #fde8e8; color: #b91c1c; }
  .conflict-warn { background: #fef3c7; border: 1px solid #f59e0b; border-radius: 6px; padding: 6px 10px; font-size: 11px; color: #92400e; margin-top: 6px; }
  .prep-note { background: #eff6ff; border-radius: 6px; padding: 5px 10px; font-size: 11px; color: #1d4ed8; margin-top: 6px; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  th { background: #0f3460; color: #fff; padding: 10px 14px; font-size: 12px; text-align: left; font-weight: 600; text-transform: uppercase; letter-spacing: 0.4px; }
  td { padding: 10px 14px; border-bottom: 1px solid #eef0f4; font-size: 13px; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f8fafc; }
  .pri-high { color: #dc2626; font-weight: 700; }
  .pri-med { color: #f59e0b; font-weight: 700; }
  .pri-low { color: #16a34a; font-weight: 700; }
  .fit-high { background: #dcfce7; color: #15803d; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 700; }
  .fit-med { background: #fef9c3; color: #92400e; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 700; }
  .fit-low { background: #fde8e8; color: #b91c1c; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 700; }

  /* CATEGORY BLOCKS */
  .cat-block { background: #fff; border-radius: 12px; padding: 16px 20px; margin-bottom: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .cat-header { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }
  .cat-count { font-size: 22px; font-weight: 800; }
  .cat-name { font-size: 15px; font-weight: 700; }
  .cat-body { font-size: 13px; color: #374151; }
  .cat-action { margin-top: 8px; font-size: 12px; font-style: italic; color: #64748b; }
  .sender-list { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; }
  .sender-tag { background: #f1f5f9; border: 1px solid #e2e8f0; border-radius: 20px; padding: 2px 10px; font-size: 11px; color: #475569; }

  /* DASHBOARD */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 14px; }
  .dash-tile { background: #fff; border-radius: 12px; padding: 16px 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); text-align: center; }
  .dash-tile .tile-num { font-size: 36px; font-weight: 800; }
  .dash-tile .tile-lbl { font-size: 11px; color: #64748b; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px; }
  .tile-red .tile-num { color: #dc2626; }
  .tile-green .tile-num { color: #16a34a; }
  .tile-blue .tile-num { color: #2563eb; }
  .tile-yellow .tile-num { color: #f59e0b; }
  .tile-purple .tile-num { color: #9333ea; }
  .tile-gray .tile-num { color: #64748b; }

  /* PRIORITIES */
  .priority-block { background: linear-gradient(135deg, #0f3460, #16213e); color: #fff; border-radius: 14px; padding: 24px 28px; }
  .priority-item { display: flex; gap: 16px; align-items: flex-start; padding: 14px 0; border-bottom: 1px solid rgba(255,255,255,0.1); }
  .priority-item:last-child { border-bottom: none; }
  .priority-num { width: 36px; height: 36px; border-radius: 50%; background: #e2c275; color: #1a1a2e; font-size: 18px; font-weight: 800; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
  .priority-text { font-size: 14px; color: #e2e8f0; }
  .priority-text strong { color: #fff; font-size: 15px; display: block; margin-bottom: 3px; }

  /* TRASH */
  .trash-group { background: #fff; border-radius: 12px; padding: 16px 20px; margin-bottom: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .trash-group-title { font-weight: 700; font-size: 14px; margin-bottom: 10px; padding-bottom: 6px; border-bottom: 2px solid #eef0f4; }
  .trash-item { padding: 7px 0; border-bottom: 1px solid #f1f5f9; font-size: 12px; }
  .trash-item:last-child { border-bottom: none; }
  .trash-item .sender { font-weight: 600; color: #374151; }
  .trash-item .reason { color: #64748b; }

  /* PROMO */
  .promo-row { display: grid; grid-template-columns: 160px 50px 1fr 100px; gap: 10px; padding: 9px 0; border-bottom: 1px solid #f1f5f9; font-size: 12px; align-items: start; }
  .promo-row:last-child { border-bottom: none; }
  .promo-brand { font-weight: 600; color: #374151; }
  .promo-count { color: #64748b; text-align: center; }
  .promo-theme { color: #64748b; }
  .rec-delete { color: #dc2626; font-weight: 700; }
  .rec-review { color: #f59e0b; font-weight: 700; }
  .rec-ignore { color: #94a3b8; font-weight: 600; }
  .rec-keep { color: #16a34a; font-weight: 700; }

  /* ACCOUNTING */
  .accounting-total { background: #0f3460; color: #fff; font-weight: 700; }
  .accounting-total td { color: #e2c275; font-size: 14px; }
  .note-confirm { background: #f0fdf4; border: 1px solid #86efac; border-radius: 8px; padding: 12px 16px; font-size: 12px; color: #15803d; margin-top: 12px; }

  .no-events { padding: 14px 20px; color: #94a3b8; font-style: italic; font-size: 13px; }
  a { color: #2563eb; text-decoration: none; }
  a:hover { text-decoration: underline; }
  .warning-icon { color: #dc2626; }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ═══════════════════════════════════════════════════════ HEADER -->
<div class="header">
  <div class="header-left">
    <div class="subtitle">EXECUTIVE BRIEFING · CHIEF OF STAFF DAILY DIGEST</div>
    <h1>Good morning, Melissa 👋</h1>
    <div class="date">Sunday, June 14, 2026 · Prepared by your Executive Chief of Staff</div>
  </div>
  <div class="header-stats">
    <div class="stat-pill"><div class="num">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="stat-pill"><div class="num">9</div><div class="lbl">Calendar Events</div></div>
    <div class="stat-pill"><div class="num">3</div><div class="lbl">⚠️ Security Flags</div></div>
    <div class="stat-pill"><div class="num">2</div><div class="lbl">Interviews This Week</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════ EXECUTIVE SUMMARY -->
<div class="section">
  <div class="section-title"><span class="icon">📋</span> Executive Summary</div>
  <div class="exec-summary">
    <div class="exec-bullet">
      <span class="badge badge-red">🚨 Urgent Risk</span>
      <div>Three suspicious/malicious emails are sitting in your inbox or unfiled: a fake "GmailSupportTeam" account-closure threat, a graphic spam email, and a casino spam. These are phishing or scam attempts — do not click any links. Delete immediately and report as phishing.</div>
    </div>
    <div class="exec-bullet">
      <span class="badge badge-green">💼 Top Opportunity</span>
      <div>You have a confirmed SoFi Zoom screen tomorrow (Mon Jun 15 at 2:30 PM ET) for Principal People Business Partner, Finance — a high-fit role. Back-to-back with a 15-min consultation with Netta Jenkins (recruiter/consultant). Prep today.</div>
    </div>
    <div class="exec-bullet">
      <span class="badge badge-blue">📅 Calendar Priority</span>
      <div>Monday June 15 is your most packed day: hair appointment 9:30–11 AM, SoFi interview 2:30 PM, Netta Jenkins consult 3:00 PM. Tuesday you have a Vet appointment. Wednesday: dental cleaning + HR Networking group (RSVP still needed). Review and prep for all.</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════ ACTION REQUIRED -->
<div class="section">
  <div class="section-title"><span class="icon">⚡</span> Action Required</div>
  <div class="cards-grid">

    <div class="card card-red">
      <span class="card-label label-red">🚨 Security — Delete Now</span>
      <div class="card-title">Fake "GmailSupportTeam" Account Closure Threat</div>
      <div class="card-meta">From: 'GmailSupportTeam' (spoofed) · Sun Jun 14</div>
      <div class="card-body">Subject: "melissaw212, Your account will be closed within 48 hours…" — Classic phishing. Sent from a random .us domain, not Google. Google never emails account closure threats this way.</div>
      <div class="card-action">🛡️ <strong>Action:</strong> Delete immediately. Report as phishing in Gmail. Do NOT click any links. Your Gmail account is fine.</div>
    </div>

    <div class="card card-red">
      <span class="card-label label-red">🚨 Security — Delete Now</span>
      <div class="card-title">Graphic Spam / Adult Solicitation Email</div>
      <div class="card-meta">From: "F*ckMeHard" (spoofed domain) · Sun Jun 14</div>
      <div class="card-body">Explicit subject line targeting your Gmail handle. Likely a phishing/malware vector disguised as adult content. Do not open, do not click.</div>
      <div class="card-action">🛡️ <strong>Action:</strong> Delete immediately. Report as spam/phishing. Consider enabling stricter Gmail spam filters.</div>
    </div>

    <div class="card card-red">
      <span class="card-label label-red">🚨 Security — Delete Now</span>
      <div class="card-title">Casino "CashApp" Spam / Free Spins Scam</div>
      <div class="card-meta">From: "💲CashApp💲" (spoofed) · Sun Jun 14</div>
      <div class="card-body">"135 Free Spins" casino offer from a spoofed sender domain. Classic lottery/casino phishing. Not from CashApp. Do not engage.</div>
      <div class="card-action">🛡️ <strong>Action:</strong> Delete and report as phishing.</div>
    </div>

    <div class="card card-yellow">
      <span class="card-label label-yellow">⚠️ RSVP Needed</span>
      <div class="card-title">HR Networking & Job Search Group — Zoom</div>
      <div class="card-meta">Calendar · Wed Jun 17 · 12:00–1:30 PM ET · Status: Needs Action</div>
      <div class="card-body">You have not yet responded to this networking event. You also have a personal "Network" block at the same time — confirm which is the correct one to attend.</div>
      <div class="card-action">📅 <strong>Action:</strong> RSVP Yes or No before Wednesday. Zoom link available.</div>
    </div>

    <div class="card card-yellow">
      <span class="card-label label-yellow">⚠️ RSVP Needed</span>
      <div class="card-title">HR Networking Open Office Hours — Zoom</div>
      <div class="card-meta">Calendar · Thu Jun 18 · 12:00–1:00 PM ET · Status: Needs Action</div>
      <div class="card-body">Another open office hours networking call you have not responded to. Same group as Wednesday.</div>
      <div class="card-action">📅 <strong>Action:</strong> RSVP before Thursday. Consider attending for job search momentum.</div>
    </div>

    <div class="card card-green">
      <span class="card-label label-green">💼 Interview Tomorrow</span>
      <div class="card-title">SoFi — Principal People Business Partner, Finance</div>
      <div class="card-meta">Zoom Screen · Mon Jun 15 · 2:30–2:50 PM ET · Confirmed</div>
      <div class="card-body">20-minute Zoom screen for a senior HRBP role at SoFi (fintech). High-fit opportunity. Short screen — be concise and sharp. Research SoFi's People strategy, recent news, and Finance org.</div>
      <div class="card-action">🎯 <strong>Action:</strong> Prep today. Test Zoom link tonight. Have resume + talking points ready. Due: Tonight/Tomorrow AM.</div>
    </div>

    <div class="card card-green">
      <span class="card-label label-green">💼 Consult Tomorrow</span>
      <div class="card-title">15-Min Consult with Netta Jenkins (HIC Consult)</div>
      <div class="card-meta">Zoom · Mon Jun 15 · 3:00–3:15 PM ET · Accepted</div>
      <div class="card-body">Back-to-back with SoFi interview. Netta Jenkins at HIC Consult — likely a recruiter or career consultant. Have your elevator pitch and target role summary ready.</div>
      <div class="card-action">🎯 <strong>Action:</strong> Prepare 2-min pitch. Know your top 3 target companies/roles. Join Zoom link: Password 424726.</div>
    </div>

    <div class="card card-blue">
      <span class="card-label label-blue">📅 Appointment Tomorrow</span>
      <div class="card-title">Hair Appointment — Elle at UMI Salon</div>
      <div class="card-meta">Mon Jun 15 · 9:30–11:00 AM · 37 W 20th St, Suite 1107, NYC</div>
      <div class="card-body">Single Process with Blowout. Leaves ~3.5 hours before your SoFi interview. Plenty of time.</div>
      <div class="card-action">✅ <strong>Action:</strong> Confirmed. No changes needed. Add commute buffer.</div>
    </div>

    <div class="card card-yellow">
      <span class="card-label label-yellow">🏥 Medical Document</span>
      <div class="card-title">UnitedHealthcare — New Explanation of Benefits Available</div>
      <div class="card-meta">From: UHC Notifications · Sat Jun 13</div>
      <div class="card-body">A new EOB is available online. Review to confirm claims processed correctly and no unexpected charges.</div>
      <div class="card-action">📋 <strong>Action:</strong> Log into UHC portal and review EOB when time permits this week.</div>
    </div>

    <div class="card card-green">
      <span class="card-label label-green">💼 Job Lead</span>
      <div class="card-title">CHRO Role — Empathy Talent (PE/Investment Mgmt)</div>
      <div class="card-meta">LinkedIn Job Alert · Sun Jun 14 · $250K–$300K/year</div>
      <div class="card-body">Chief Human Resources Officer at Empathy Talent — Private Equity/Investment Management focus. Very senior, high-compensation. Worth reviewing for fit.</div>
      <div class="card-action">🎯 <strong>Action:</strong> Review job description. If fit, apply this week before pipeline fills.</div>
    </div>

    <div class="card card-green">
      <span class="card-label label-green">💼 Networking Lead</span>
      <div class="card-title">Pay It Forward HR Job Leads Group — Multiple Leads</div>
      <div class="card-meta">groups.io · Multiple dates this week</div>
      <div class="card-body">3 leads posted: Corporate HR Generalist/HRIS Admin (Atlanta), Contract HR Assistant II (Remote, up to $38.41/hr), Executive HR Director (Easton OH — in-office 5 days). Also: Newtown Career Group meets Mon Jun 15 (7–8:30 PM).</div>
      <div class="card-action">🎯 <strong>Action:</strong> Review each lead. If any fit, reach out to listed recruiters directly.</div>
    </div>

    <div class="card card-blue">
      <span class="card-label label-blue">📦 Shipment</span>
      <div class="card-title">TikTok Shop — Halara Order Shipped</div>
      <div class="card-meta">From: TikTok Shop · Sun Jun 14 (Unread)</div>
      <div class="card-body">Halara DayStretch item shipped to Stella Weiss. Earlier email showed it was packed and awaiting carrier. Now shipped — check tracking link in email.</div>
      <div class="card-action">📦 <strong>Action:</strong> Check tracking info in email for delivery date.</div>
    </div>

    <div class="card card-blue">
      <span class="card-label label-blue">💰 Payment Received</span>
      <div class="card-title">Venmo — Maggie Keogh Paid You $20</div>
      <div class="card-meta">From: Venmo · Sun Jun 14 · 🍕 emoji</div>
      <div class="card-body">$20 received from Maggie Keogh (pizza split?). Already credited to your Venmo account. No action needed unless you need to transfer to bank.</div>
      <div class="card-action">✅ <strong>Action:</strong> Optional — transfer to bank if needed.</div>
    </div>

    <div class="card card-blue">
      <span class="card-label label-blue">🎁 Gift Purchase</span>
      <div class="card-title">Babylist — Gifts for Gabriella & Raymond's Baby Registry</div>
      <div class="card-meta">From: Babylist · Sun Jun 14</div>
      <div class="card-body">Purchase confirmation for baby registry gifts. Confirm items and delivery address are correct.</div>
      <div class="card-action">✅ <strong>Action:</strong> Review confirmation for accuracy.</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════ FULL 7-DAY CALENDAR -->
<div class="section">
  <div class="section-title"><span class="icon">📅</span> Full 7-Day Calendar</div>

  <!-- Sunday June 14 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <div>Sunday, June 14, 2026 <span style="color:#e2c275;margin-left:8px;">TODAY</span></div>
      <div class="day-label">No events scheduled</div>
    </div>
    <div class="no-events">No calendar events today. Use today to prep for tomorrow's packed schedule.</div>
  </div>

  <!-- Monday June 15 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <div>Monday, June 15, 2026</div>
      <div class="day-label">3 Events — Busy Day</div>
    </div>

    <div class="cal-event">
      <div class="cal-time">9:30 AM<br><span style="font-size:11px;color:#94a3b8;">– 11:00 AM</span></div>
      <div>
        <div class="cal-name">💇 Hair Appointment — Elle at UMI Salon</div>
        <div class="cal-detail">Single Process (with Blowout) with Elle M</div>
        <div class="cal-detail">📍 37 West 20th St, Suite 1107, New York, NY 10011</div>
        <span class="cal-status status-confirmed">Confirmed</span>
        <div class="prep-note">💡 Prep: Allow travel time. Appointment ends at 11 AM — 3.5 hrs before interview.</div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">2:30 PM<br><span style="font-size:11px;color:#94a3b8;">– 2:50 PM</span></div>
      <div>
        <div class="cal-name">🎯 Interview with SoFi — Principal People Business Partner, Finance</div>
        <div class="cal-detail">Zoom Screen · 20 minutes</div>
        <div class="cal-detail">📍 Zoom (link in calendar confirmation)</div>
        <span class="cal-status status-confirmed">Confirmed</span>
        <div class="prep-note">💡 Prep: Research SoFi's People org, Finance team structure, recent company news. Have resume ready. Test Zoom TONIGHT. Be concise — only 20 mins.</div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">3:00 PM<br><span style="font-size:11px;color:#94a3b8;">– 3:15 PM</span></div>
      <div>
        <div class="cal-name">🤝 15-Min Consultation — Netta Jenkins (HIC Consult)</div>
        <div class="cal-detail">Attendee: netta@hicconsult.com</div>
        <div class="cal-detail">📍 <a href="https://us06web.zoom.us/j/5224221004?pwd=UU5YNmlFckpjQnlzc2FDMHFlNUhhUT09">Zoom Link</a> · Password: 424726</div>
        <span class="cal-status status-accepted">Accepted</span>
        <div class="conflict-warn">⚠️ Back-to-back with SoFi interview. Only 10-min buffer. End SoFi on time and have Zoom link ready to switch immediately.</div>
        <div class="prep-note">💡 Prep: Know your 2-min pitch, target roles/companies, availability, and compensation range.</div>
      </div>
    </div>
  </div>

  <!-- Tuesday June 16 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <div>Tuesday, June 16, 2026</div>
      <div class="day-label">1 Event</div>
    </div>
    <div class="cal-event">
      <div class="cal-time">10:00 AM<br><span style="font-size:11px;color:#94a3b8;">– 11:00 AM</span></div>
      <div>
        <div class="cal-name">🐾 Vet Appointment</div>
        <div class="cal-detail">1-hour appointment · No location specified</div>
        <span class="cal-status status-confirmed">Confirmed</span>
        <div class="prep-note">💡 Prep: Confirm which pet, bring any necessary records, confirm address/clinic.</div>
      </div>
    </div>
  </div>

  <!-- Wednesday June 17 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <div>Wednesday, June 17, 2026</div>
      <div class="day-label">3 Events — Note: Two events overlap at noon</div>
    </div>

    <div class="cal-event">
      <div class="cal-time">10:45 AM<br><span style="font-size:11px;color:#94a3b8;">– 11:45 AM</span></div>
      <div>
        <div class="cal-name">🦷 Dental Cleaning — Dr. Deutch</div>
        <div class="cal-detail">No location specified · 1 hour</div>
        <span class="cal-status status-confirmed">Confirmed</span>
        <div class="prep-note">💡 Prep: Confirm address and arrive 10 mins early. Ends just before noon networking session.</div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">12:00 PM<br><span style="font-size:11px;color:#94a3b8;">– 1:30 PM</span></div>
      <div>
        <div class="cal-name">🤝 HR Networking & Job Search Group — Zoom 2</div>
        <div class="cal-detail">Large group networking session (180+ attendees)</div>
        <div class="cal-detail">📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1">Zoom Link</a></div>
        <span class="cal-status status-needs">⚠️ RSVP Needed</span>
        <div class="conflict-warn">⚠️ Dental ends at 11:45 AM — only 15-min buffer before this call. Plan to join from phone/laptop if still commuting.</div>
        <div class="prep-note">💡 Action: RSVP now. Prepare brief intro and any job search updates to share with the group.</div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">12:00 PM<br><span style="font-size:11px;color:#94a3b8;">– 1:30 PM</span></div>
      <div>
        <div class="cal-name">🤝 Network (Personal Block)</div>
        <div class="cal-detail">Personal calendar block · Same time as HR Networking Zoom</div>
        <span class="cal-status status-confirmed">Confirmed</span>
        <div class="conflict-warn">⚠️ Duplicate/conflict: You have both "Network" block and the HR Networking Zoom at the same time. Confirm which takes priority.</div>
      </div>
    </div>
  </div>

  <!-- Thursday June 18 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <div>Thursday, June 18, 2026</div>
      <div class="day-label">2 Events — Note: Check declined event</div>
    </div>

    <div class="cal-event">
      <div class="cal-time">9:00 AM<br><span style="font-size:11px;color:#94a3b8;">– 10:30 AM</span></div>
      <div>
        <div class="cal-name">🎤 Executive Roundtable (John Madigan)</div>
        <div class="cal-detail">Hosted by John Madigan · 📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09">Zoom Link</a> · Meeting ID: 207 786 667 · Password: 205454</div>
        <span class="cal-status status-declined">Declined</span>
        <div class="prep-note">💡 Note: You declined this event. If it was an important leadership roundtable, consider whether you want to ask to rejoin. Check who John Madigan is in your network.</div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">12:00 PM<br><span style="font-size:11px;color:#94a3b8;">– 1:00 PM</span></div>
      <div>
        <div class="cal-name">🤝 HR Networking & Job Search: Open Office Hours — Zoom 2</div>
        <div class="cal-detail">Same large networking group · Open discussion, no recording</div>
        <div class="cal-detail">📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1">Zoom Link</a></div>
        <span class="cal-status status-needs">⚠️ RSVP Needed</span>
        <div class="prep-note">💡 Action: RSVP. Note: organizers request NO automated AI notetakers. Good informal networking opportunity.</div>
      </div>
    </div>
  </div>

  <!-- Friday June 19 — Sunday June 20 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <div>Friday, June 19 – Sunday, June 20, 2026</div>
      <div class="day-label">No events scheduled</div>
    </div>
    <div class="no-events">No calendar events. Use Friday for follow-ups after your Monday interviews.</div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════ JOB SEARCH & INTERVIEW PIPELINE -->
<div class="section">
  <div class="section-title"><span class="icon">💼</span> Job Search & Interview Pipeline</div>
  <table>
    <thead>
      <tr>
        <th>Opportunity</th>
        <th>Source</th>
        <th>Type</th>
        <th>Date</th>
        <th>Fit</th>
        <th>Status / Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Principal People Business Partner, Finance — SoFi</strong></td>
        <td>Calendar / Email</td>
        <td>Interview (Zoom Screen)</td>
        <td>Mon Jun 15, 2:30 PM</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>✅ Confirmed. Prep today. Fintech HRBP — strong match for senior HR profile.</td>
      </tr>
      <tr>
        <td><strong>15-Min Consult — Netta Jenkins, HIC Consult</strong></td>
        <td>Calendar</td>
        <td>Recruiter/Consultant Consult</td>
        <td>Mon Jun 15, 3:00 PM</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>✅ Accepted. Prepare pitch. Could open new opportunities.</td>
      </tr>
      <tr>
        <td><strong>CHRO — Empathy Talent (PE/Investment Mgmt)</strong> · $250K–$300K/yr</td>
        <td>LinkedIn Job Alert</td>
        <td>Job Alert</td>
        <td>Sun Jun 14</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>🎯 Review JD. Apply ASAP if fit confirmed. Senior/C-suite level.</td>
      </tr>
      <tr>
        <td><strong>Head of People — Gradle Technologies</strong> (AI software company)</td>
        <td>LinkedIn Job Alerts (×3 alerts)</td>
        <td>Job Alert (Repeated)</td>
        <td>Sun Jun 14 (×3 times)</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>🎯 Review JD. Gradle is an AI-forward company. Good fit for senior People leader. Note: 3 duplicate alerts sent to Trash.</td>
      </tr>
      <tr>
        <td><strong>Senior HRBP — Elliptic</strong> (similar roles)</td>
        <td>LinkedIn Jobs</td>
        <td>Job Alert</td>
        <td>Sun Jun 14</td>
        <td><span class="fit-med">MEDIUM</span></td>
        <td>📋 Review similar roles. Elliptic is a crypto/fintech company.</td>
      </tr>
      <tr>
        <td><strong>Manager, HR BP – Southeast Region — Champion Home Builders</strong> + 6 more</td>
        <td>Glassdoor Jobs</td>
        <td>Job Alert</td>
        <td>Sun Jun 14</td>
        <td><span class="fit-med">MEDIUM</span></td>
        <td>📋 Review 7 roles listed. SE Region may require relocation — check details.</td>
      </tr>
      <tr>
        <td><strong>Executive HR Director — Easton, OH</strong> (in-office 5 days)</td>
        <td>Pay It Forward HR (Lisa Dillon)</td>
        <td>Network Referral</td>
        <td>Sun Jun 14</td>
        <td><span class="fit-med">MEDIUM</span></td>
        <td>📋 In-office 5 days in Ohio — likely not a fit unless open to relocation. Review anyway.</td>
      </tr>
      <tr>
        <td><strong>Corporate HR Generalist & HRIS Administrator — Atlanta, GA</strong></td>
        <td>Pay It Forward HR (Michael Shao)</td>
        <td>Network Referral</td>
        <td>Sat Jun 13</td>
        <td><span class="fit-low">LOW</span></td>
        <td>📋 Atlanta-based, generalist level. Likely too junior. Contact: gary@work22.com if interested.</td>
      </tr>
      <tr>
        <td><strong>Contract HR Assistant II — Remote</strong> · Up to $38.41/hr</td>
        <td>Pay It Forward HR (Michael Shao)</td>
        <td>Network Referral</td>
        <td>Thu Jun 11</td>
        <td><span class="fit-low">LOW</span></td>
        <td>📋 Contract, assistant level — likely too junior. Note for referral or networking purposes.</td>
      </tr>
      <tr>
        <td><strong>Newtown Career Group Meeting</strong> — Newtown Presbyterian Church</td>
        <td>Pay It Forward HR (David Schuchman)</td>
        <td>Networking Event</td>
        <td>Mon Jun 15, 7:00–8:30 PM</td>
        <td><span class="fit-med">MEDIUM</span></td>
        <td>📅 In-person Newtown, PA. Worth attending if you can make it after your interview day.</td>
      </tr>
      <tr>
        <td><strong>HR Networking & Job Search Group Zoom</strong></td>
        <td>Calendar (recurring)</td>
        <td>Networking Event</td>
        <td>Wed Jun 17, 12:00 PM</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>⚠️ RSVP needed. Strong networking group — 180+ HR professionals.</td>
      </tr>
      <tr>
        <td><strong>HR Networking Open Office Hours</strong></td>
        <td>Calendar (recurring)</td>
        <td>Networking Event</td>
        <td>Thu Jun 18, 12:00 PM</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>⚠️ RSVP needed. Informal open discussion — good for relationship building.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════ FULL EMAIL REVIEW BY CATEGORY -->
<div class="section">
  <div class="section-title"><span class="icon">📧</span> Full Email Review by Category</div>

  <!-- Security / Risk -->
  <div class="cat-block" style="border-left: 5px solid #dc2626;">
    <div class="cat-header">
      <div class="cat-count" style="color:#dc2626;">3</div>
      <div>
        <div class="cat-name">🚨 Security / Risk</div>
        <span class="badge badge-red">Immediate Action Required</span>
      </div>
    </div>
    <div class="cat-body">
      Three malicious or phishing emails identified. None are legitimate.
      <div class="sender-list">
        <span class="sender-tag">⚠️ Fake "GmailSupportTeam" — account closure threat</span>
        <span class="sender-tag">⚠️ "F*ckMeHard" — adult spam/phishing</span>
        <span class="sender-tag">⚠️ "💲CashApp💲" — casino free spins scam</span>
      </div>
    </div>
    <div class="cat-action">🛡️ <strong>Action:</strong> Delete all three immediately. Report as phishing in Gmail. Do not click any links.</div>
  </div>

  <!-- Job Search -->
  <div class="cat-block" style="border-left: 5px solid #16a34a;">
    <div class="cat-header">
      <div class="cat-count" style="color:#16a34a;">9</div>
      <div>
        <div class="cat-name">💼 Job Search</div>
        <span class="badge badge-green">High Priority</span>
      </div>
    </div>
    <div class="cat-body">
      Active job leads, alerts, and interview confirmations. Includes LinkedIn alerts, Glassdoor, and network referrals.
      <div class="sender-list">
        <span class="sender-tag">LinkedIn Job Alerts — CHRO at Empathy Talent ($250–300K)</span>
        <span class="sender-tag">LinkedIn Job Alerts — Head of People at Gradle Technologies (×1 in inbox)</span>
        <span class="sender-tag">LinkedIn Jobs — Senior HRBP at Elliptic (similar roles)</span>
        <span class="sender-tag">Glassdoor — Manager HR BP + 6 more roles</span>
        <span class="sender-tag">Pay It Forward HR — Executive HR Director (Easton OH)</span>
        <span class="sender-tag">Pay It Forward HR — Corporate HR Generalist/HRIS (Atlanta)</span>
        <span class="sender-tag">Pay It Forward HR — Contract HR Assistant II (Remote)</span>
        <span class="sender-tag">Pay It Forward HR — Job Search Group Meeting Jun 15</span>
        <span class="sender-tag">Calendar — SoFi Interview confirmed (Mon Jun 15)</span>
      </div>
    </div>
    <div class="cat-action">🎯 <strong>Action:</strong> Prioritize SoFi prep today. Review CHRO role at Empathy Talent. RSVP networking sessions.</div>
  </div>

  <!-- Recruiters / Networking -->
  <div class="cat-block" style="border-left: 5px solid #2563eb;">
    <div class="cat-header">
      <div class="cat-count" style="color:#2563eb;">2</div>
      <div>
        <div class="cat-name">🤝 Recruiters / Networking</div>
        <span class="badge badge-blue">Follow Up</span>
      </div>
    </div>
    <div class="cat-body">
      Direct recruiter and consultant outreach.
      <div class="sender-list">
        <span class="sender-tag">Netta Jenkins — HIC Consult (15-min consult Mon Jun 15)</span>
        <span class="sender-tag">Mo Bunnell via LinkedIn — BD Skill newsletter (networking read)</span>
      </div>
    </div>
    <div class="cat-action">✅ <strong>Action:</strong> Netta consult confirmed for Monday. Mo Bunnell newsletter — review when time permits.</div>
  </div>

  <!-- Calendar / Events -->
  <div class="cat-block" style="border-left: 5px solid #2563eb;">
    <div class="cat-header">
      <div class="cat-count" style="color:#2563eb;">2</div>
      <div>
        <div class="cat-name">📅 Calendar / Events</div>
        <span class="badge badge-blue">Review</span>
      </div>
    </div>
    <div class="cat-body">
      Briefing email and GitHub Actions failure notification.
      <div class="sender-list">
        <span class="sender-tag">Melissa Daily Briefing — Today's briefing email (in inbox)</span>
        <span class="sender-tag">GitHub missophs/daily-briefing — Workflow run failed (in trash)</span>
      </div>
    </div>
    <div class="cat-action">🔧 <strong>Action:</strong> GitHub workflow failure — if you maintain the daily-briefing automation, investigate and fix the webhooks job. Otherwise delegate.</div>
  </div>

  <!-- Medical / Health -->
  <div class="cat-block" style="border-left: 5px solid #f59e0b;">
    <div class="cat-header">
      <div class="cat-count" style="color:#f59e0b;">1</div>
      <div>
        <div class="cat-name">🏥 Medical / Health</div>
        <span class="badge badge-yellow">Review This Week</span>
      </div>
    </div>
    <div class="cat-body">
      <div class="sender-list">
        <span class="sender-tag">UnitedHealthcare — New Explanation of Benefits available online</span>
      </div>
    </div>
    <div class="cat-action">📋 <strong>Action:</strong> Log into UHC portal and review EOB. Confirm claims are correct.</div>
  </div>

  <!-- Financial / Billing -->
  <div class="cat-block" style="border-left: 5px solid #f59e0b;">
    <div class="cat-header">
      <div class="cat-count" style="color:#f59e0b;">1</div>
      <div>
        <div class="cat-name">💰 Financial / Billing</div>
        <span class="badge badge-yellow">FYI</span>
      </div>
    </div>
    <div class="cat-body">
      <div class="sender-list">
        <span class="sender-tag">Venmo — Maggie Keogh paid you $20.00 (🍕)</span>
      </div>
    </div>
    <div class="cat-action">✅ <strong>Action:</strong> Already credited to Venmo. Transfer to bank if desired.</div>
  </div>

  <!-- Professional Development -->
  <div class="cat-block" style="border-left: 5px solid #9333ea;">
    <div class="cat-header">
      <div class="cat-count" style="color:#9333ea;">3</div>
      <div>
        <div class="cat-name">📚 Professional Development</div>
        <span class="badge badge-purple">Review When Time Permits</span>
      </div>
    </div>
    <div class="cat-body">
      AI and leadership content newsletters that may be professionally relevant.
      <div class="sender-list">
        <span class="sender-tag">AI For Leaders — "Why Codex Is Better for Agentic Work" (in trash)</span>
        <span class="sender-tag">The CHRO Office (Substack) — "3 AI Terms Every CHRO Must Know" (in trash)</span>
        <span class="sender-tag">Mo Bunnell/LinkedIn — "BD Skill Your Best People Are Never Taught"</span>
      </div>
    </div>
    <div class="cat-action">📖 <strong>Action:</strong> CHRO Office article may be worth a quick read as a senior HR leader. Others are lower priority.</div>
  </div>

  <!-- Personal -->
  <div class="cat-block" style="border-left: 5px solid #0f3460;">
    <div class="cat-header">
      <div class="cat-count" style="color:#0f3460;">5</div>
      <div>
        <div class="cat-name">👤 Personal</div>
        <span class="badge badge-gray">Low Priority</span>
      </div>
    </div>
    <div class="cat-body">
      Personal emails and account activity.
      <div class="sender-list">
        <span class="sender-tag">Babylist — Gift purchase confirmation for Gabriella & Raymond's registry</span>
        <span class="sender-tag">TikTok Shop — Halara item shipped (to Stella Weiss)</span>
        <span class="sender-tag">TikTok Shop — Order packed/awaiting shipment (earlier update)</span>
        <span class="sender-tag">Google — Shared account data with Halara (Sign in with Google)</span>
        <span class="sender-tag">Melissa W (self) — Draft/note to self: "Nebius"</span>
      </div>
    </div>
    <div class="cat-action">✅ <strong>Action:</strong> Check TikTok tracking. Review Babylist confirmation. Note "Nebius" — is this a company/platform to explore?</div>
  </div>

  <!-- Newsletters / Subscriptions -->
  <div class="cat-block" style="border-left: 5px solid #9333ea;">
    <div class="cat-header">
      <div class="cat-count" style="color:#9333ea;">5</div>
      <div>
        <div class="cat-name">📰 Newsletters / Subscriptions</div>
        <span class="badge badge-purple">Low Priority / Skim or Unsubscribe</span>
      </div>
    </div>
    <div class="cat-body">
      Email newsletters and subscription content received today.
      <div class="sender-list">
        <span class="sender-tag">Medium Daily Digest — "5 AI Terms, Ahead of 90%" (in trash)</span>
        <span class="sender-tag">CoolDeep AI — "The AI roadmap nobody gave me" (in trash)</span>
        <span class="sender-tag">Lisa Rangel / Chameleon Resumes — "The play everyone is running" (in trash)</span>
        <span class="sender-tag">AI with Mariah — "Is the AI challenge right for me?" (in trash)</span>
        <span class="sender-tag">CoinOut — Earn 1,000 Bonus Coins for Day 5 (Food & Beverage Journal)</span>
      </div>
    </div>
    <div class="cat-action">🗑️ <strong>Action:</strong> Lisa Rangel's senior job search content may be worth a quick read. Others can be skimmed or unsubscribed.</div>
  </div>

  <!-- Promotional / Retail -->
  <div class="cat-block" style="border-left: 5px solid #94a3b8;">
    <div class="cat-header">
      <div class="cat-count" style="color:#94a3b8;">14</div>
      <div>
        <div class="cat-name">🛍️ Promotional / Retail</div>
        <span class="badge badge-gray">Safe to Delete</span>
      </div>
    </div>
    <div class="cat-body">
      Retail and promotional emails. See dedicated Promotional section below for full breakdown.
      <div class="sender-list">
        <span class="sender-tag">SHEIN (×4)</span>
        <span class="sender-tag">Old Navy</span>
        <span class="sender-tag">Zappos</span>
        <span class="sender-tag">Quince</span>
        <span class="sender-tag">Shopify</span>
        <span class="sender-tag">VIVAIA</span>
        <span class="sender-tag">Kohl's</span>
        <span class="sender-tag">Gap Factory</span>
        <span class="sender-tag">Walgreens (in trash)</span>
        <span class="sender-tag">Zulily</span>
        <span class="sender-tag">Temu (in trash)</span>
        <span class="sender-tag">Waldo's Rescue (dog calendar contest)</span>
      </div>
    </div>
    <div class="cat-action">🗑️ <strong>Action:</strong> Delete all promotional emails. Unsubscribe from brands you no longer shop at.</div>
  </div>

  <!-- Social / Dating -->
  <div class="cat-block" style="border-left: 5px solid #94a3b8;">
    <div class="cat-header">
      <div class="cat-count" style="color:#94a3b8;">1</div>
      <div>
        <div class="cat-name">💬 Social / Dating</div>
        <span class="badge badge-gray">Optional</span>
      </div>
    </div>
    <div class="cat-body">
      <div class="sender-list">
        <span class="sender-tag">OkCupid — "Someone likes you" · Message them now</span>
      </div>
    </div>
    <div class="cat-action">💌 <strong>Action:</strong> Check when you have personal time. Not urgent.</div>
  </div>

  <!-- Yahoo Account Activity (in trash) -->
  <div class="cat-block" style="border-left: 5px solid #dc2626;">
    <div class="cat-header">
      <div class="cat-count" style="color:#dc2626;">3</div>
      <div>
        <div class="cat-name">🔐 Yahoo Account Activity (Forwarded / Trash)</div>
        <span class="badge badge-red">Monitor — Possibly Sophie's Account</span>
      </div>
    </div>
    <div class="cat-body">
      Three Yahoo emails related to account "sophie / sophiew3016@yahoo.com" — verification code, sign-in notification, and password change. These appear to be for a different person (Sophie) or a shared/family account and were trashed. Phone number: +1 (516) 313-8888 referenced.
      <div class="sender-list">
        <span class="sender-tag">Yahoo — Verification code 186934 (sophiew3016)</span>
        <span class="sender-tag">Yahoo — Sign-in notification (Safari, sophiew3016)</span>
        <span class="sender-tag">Yahoo — Password changed (sophiew3016)</span>
      </div>
    </div>
    <div class="cat-action">⚠️ <strong>Action:</strong> If "Sophie" is a family member, confirm she authorized these sign-in/password changes. These are in trash, which is appropriate. Monitor.</div>
  </div>

  <!-- Safe to Delete -->
  <div class="cat-block" style="border-left: 5px solid #94a3b8;">
    <div class="cat
<hr>
<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Job Search / Recruiters</td><td>13</td></tr>
<tr><td>Medical / Health</td><td>2</td></tr>
<tr><td>Other / Review</td><td>21</td></tr>
<tr><td>Professional Development / Newsletters</td><td>1</td></tr>
<tr><td>Promotional / Retail</td><td>6</td></tr>
<tr><td>Security / Risk</td><td>7</td></tr>
</table>
<p><strong>Audit Note:</strong> Every fetched email was reviewed and assigned to one category. Trash emails were included in review. Promotional and low-value emails were accounted for but deprioritized.</p>

