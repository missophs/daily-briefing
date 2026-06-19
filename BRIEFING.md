<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing – Melissa W. | June 19, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px 60px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px 28px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header .sub { font-size: 14px; color: #a8b2d8; margin-top: 4px; }
  .header-stats { display: flex; gap: 20px; flex-wrap: wrap; }
  .stat-box { background: rgba(255,255,255,0.10); border-radius: 10px; padding: 14px 22px; text-align: center; min-width: 110px; }
  .stat-box .num { font-size: 28px; font-weight: 700; color: #e2e8ff; }
  .stat-box .lbl { font-size: 11px; color: #a8b2d8; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 2px; }

  /* SECTION TITLES */
  .section-title { font-size: 17px; font-weight: 700; color: #1a1a2e; margin: 32px 0 12px; padding-left: 10px; border-left: 4px solid #0f3460; text-transform: uppercase; letter-spacing: 0.4px; }

  /* EXECUTIVE SUMMARY */
  .exec-summary { background: #fff; border-radius: 12px; padding: 22px 26px; box-shadow: 0 2px 10px rgba(0,0,0,0.06); margin-bottom: 8px; }
  .exec-summary ul { list-style: none; }
  .exec-summary ul li { padding: 10px 0; border-bottom: 1px solid #f0f0f0; font-size: 14px; display: flex; gap: 10px; align-items: flex-start; }
  .exec-summary ul li:last-child { border-bottom: none; }
  .exec-summary ul li .badge { flex-shrink: 0; font-size: 11px; font-weight: 700; padding: 3px 9px; border-radius: 20px; text-transform: uppercase; letter-spacing: 0.4px; }
  .badge-red { background: #ffe5e5; color: #c0392b; }
  .badge-green { background: #e5f5e5; color: #1a7a3c; }
  .badge-blue { background: #e5eeff; color: #1a4fa0; }
  .badge-yellow { background: #fff8e1; color: #b07a00; }
  .badge-purple { background: #f2e5ff; color: #6c2fa0; }
  .badge-gray { background: #f0f0f0; color: #666; }

  /* CARDS */
  .card-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 16px; }
  .card { border-radius: 12px; padding: 18px 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .card .card-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px; margin-bottom: 6px; }
  .card .card-title { font-size: 15px; font-weight: 700; margin-bottom: 6px; }
  .card .card-source { font-size: 12px; opacity: 0.75; margin-bottom: 8px; }
  .card .card-why { font-size: 13px; margin-bottom: 8px; line-height: 1.5; }
  .card .card-action { font-size: 13px; font-weight: 600; margin-bottom: 4px; }
  .card .card-due { font-size: 12px; opacity: 0.8; }

  .card-red { background: #fff0f0; border-left: 5px solid #e74c3c; }
  .card-red .card-label { color: #c0392b; }
  .card-yellow { background: #fffde7; border-left: 5px solid #f39c12; }
  .card-yellow .card-label { color: #b07a00; }
  .card-blue { background: #eff6ff; border-left: 5px solid #2980b9; }
  .card-blue .card-label { color: #1a4fa0; }
  .card-green { background: #f0faf0; border-left: 5px solid #27ae60; }
  .card-green .card-label { color: #1a7a3c; }
  .card-purple { background: #f8f0ff; border-left: 5px solid #8e44ad; }
  .card-purple .card-label { color: #6c2fa0; }

  /* CALENDAR */
  .cal-day { background: #fff; border-radius: 12px; margin-bottom: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); overflow: hidden; }
  .cal-day-header { background: #1a1a2e; color: #fff; padding: 10px 18px; font-weight: 700; font-size: 14px; display: flex; justify-content: space-between; align-items: center; }
  .cal-day-header .day-badge { font-size: 11px; background: rgba(255,255,255,0.15); padding: 2px 10px; border-radius: 20px; }
  .cal-event { padding: 12px 18px; border-bottom: 1px solid #f0f0f0; display: flex; gap: 14px; align-items: flex-start; }
  .cal-event:last-child { border-bottom: none; }
  .cal-time { font-size: 13px; font-weight: 700; color: #2980b9; min-width: 90px; flex-shrink: 0; }
  .cal-info { flex: 1; }
  .cal-info .ev-title { font-size: 14px; font-weight: 700; color: #1a1a2e; }
  .cal-info .ev-meta { font-size: 12px; color: #666; margin-top: 3px; }
  .cal-info .ev-prep { font-size: 12px; color: #8e44ad; margin-top: 4px; }
  .cal-info .ev-conflict { font-size: 12px; color: #e74c3c; font-weight: 600; margin-top: 4px; }
  .rsvp-confirmed { background: #e5f5e5; color: #1a7a3c; font-size: 11px; font-weight: 700; padding: 2px 9px; border-radius: 20px; display: inline-block; }
  .rsvp-needs { background: #fff8e1; color: #b07a00; font-size: 11px; font-weight: 700; padding: 2px 9px; border-radius: 20px; display: inline-block; }
  .rsvp-declined { background: #ffe5e5; color: #c0392b; font-size: 11px; font-weight: 700; padding: 2px 9px; border-radius: 20px; display: inline-block; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  table th { background: #1a1a2e; color: #fff; padding: 11px 14px; font-size: 12px; text-align: left; font-weight: 600; text-transform: uppercase; letter-spacing: 0.4px; }
  table td { padding: 10px 14px; font-size: 13px; border-bottom: 1px solid #f0f0f0; vertical-align: top; }
  table tr:last-child td { border-bottom: none; }
  table tr:nth-child(even) td { background: #fafafa; }
  .pri-high { color: #c0392b; font-weight: 700; }
  .pri-med { color: #b07a00; font-weight: 700; }
  .pri-low { color: #666; }
  .fit-high { background: #e5f5e5; color: #1a7a3c; font-size: 11px; font-weight: 700; padding: 2px 9px; border-radius: 20px; display: inline-block; }
  .fit-med { background: #fff8e1; color: #b07a00; font-size: 11px; font-weight: 700; padding: 2px 9px; border-radius: 20px; display: inline-block; }
  .fit-low { background: #f0f0f0; color: #666; font-size: 11px; font-weight: 700; padding: 2px 9px; border-radius: 20px; display: inline-block; }

  /* EMAIL CATEGORIES */
  .cat-block { background: #fff; border-radius: 12px; margin-bottom: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); overflow: hidden; }
  .cat-header { padding: 11px 18px; font-weight: 700; font-size: 14px; display: flex; justify-content: space-between; align-items: center; }
  .cat-body { padding: 14px 18px; }
  .cat-body p { font-size: 13px; margin-bottom: 6px; line-height: 1.6; }
  .cat-body .sender-list { font-size: 12px; color: #555; margin-bottom: 6px; }
  .cat-body .rec { font-size: 12px; font-weight: 700; padding: 3px 10px; border-radius: 20px; display: inline-block; margin-top: 4px; }
  .rec-act { background: #ffe5e5; color: #c0392b; }
  .rec-rev { background: #fff8e1; color: #b07a00; }
  .rec-del { background: #f0f0f0; color: #666; }
  .rec-keep { background: #e5f5e5; color: #1a7a3c; }
  .rec-uns { background: #f2e5ff; color: #6c2fa0; }

  .cat-red .cat-header { background: #ffe5e5; color: #c0392b; }
  .cat-yellow .cat-header { background: #fff8e1; color: #b07a00; }
  .cat-blue .cat-header { background: #e5eeff; color: #1a4fa0; }
  .cat-green .cat-header { background: #e5f5e5; color: #1a7a3c; }
  .cat-purple .cat-header { background: #f2e5ff; color: #6c2fa0; }
  .cat-gray .cat-header { background: #f0f0f0; color: #555; }
  .cat-orange .cat-header { background: #fff3e0; color: #b05a00; }

  .count-pill { font-size: 12px; padding: 2px 10px; border-radius: 20px; background: rgba(0,0,0,0.10); font-weight: 700; }

  /* TRASH */
  .trash-group { background: #fff; border-radius: 10px; margin-bottom: 12px; overflow: hidden; box-shadow: 0 2px 6px rgba(0,0,0,0.05); }
  .trash-group-header { padding: 10px 16px; font-weight: 700; font-size: 13px; }
  .trash-restore { background: #ffe5e5; color: #c0392b; }
  .trash-review { background: #fff8e1; color: #b07a00; }
  .trash-delete { background: #f0f0f0; color: #555; }
  .trash-item { padding: 9px 16px; border-bottom: 1px solid #f5f5f5; font-size: 13px; }
  .trash-item:last-child { border-bottom: none; }
  .trash-item strong { color: #1a1a2e; }

  /* DASHBOARD */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 14px; }
  .dash-card { background: #fff; border-radius: 12px; padding: 18px 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); text-align: center; }
  .dash-card .d-icon { font-size: 28px; margin-bottom: 8px; }
  .dash-card .d-label { font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: #888; margin-bottom: 4px; }
  .dash-card .d-val { font-size: 22px; font-weight: 700; color: #1a1a2e; }
  .dash-card .d-note { font-size: 12px; color: #666; margin-top: 4px; }

  /* PROMO TABLE */
  .promo-table td { font-size: 13px; }

  /* NEWSLETTER TABLE */
  .nl-table td { font-size: 13px; }

  /* PRIORITIES */
  .priority-list { list-style: none; counter-reset: pri; }
  .priority-list li { counter-increment: pri; background: #fff; border-radius: 12px; padding: 18px 20px 18px 70px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); position: relative; font-size: 14px; line-height: 1.6; }
  .priority-list li::before { content: counter(pri); position: absolute; left: 18px; top: 50%; transform: translateY(-50%); width: 36px; height: 36px; background: #1a1a2e; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; font-weight: 700; }
  .priority-list li:nth-child(1)::before { background: #c0392b; }
  .priority-list li:nth-child(2)::before { background: #27ae60; }
  .priority-list li:nth-child(3)::before { background: #2980b9; }
  .priority-list li strong { font-weight: 700; }

  /* ACCOUNTING */
  .acct-total { background: #1a1a2e; color: #fff; font-weight: 700; }
  .acct-total td { color: #fff !important; border-bottom: none; }

  /* ALERT BANNER */
  .alert-banner { background: #c0392b; color: #fff; border-radius: 10px; padding: 13px 20px; margin-bottom: 18px; font-size: 14px; font-weight: 600; display: flex; gap: 12px; align-items: center; }
  .alert-banner .icon { font-size: 20px; flex-shrink: 0; }

  /* RESPONSIVE */
  @media (max-width: 600px) {
    .header { flex-direction: column; }
    .card-grid { grid-template-columns: 1fr; }
    .dashboard-grid { grid-template-columns: repeat(2, 1fr); }
  }

  hr.divider { border: none; border-top: 2px solid #e8e8e8; margin: 28px 0; }
</style>
</head>
<body>
<div class="page">

  <!-- ===================== HEADER ===================== -->
  <div class="header">
    <div>
      <div class="sub">EXECUTIVE BRIEFING</div>
      <h1>Good Morning, Melissa 👋</h1>
      <div class="sub">Friday, June 19, 2026 &nbsp;|&nbsp; Prepared by your Executive Chief of Staff</div>
    </div>
    <div class="header-stats">
      <div class="stat-box"><div class="num">50</div><div class="lbl">Emails Reviewed</div></div>
      <div class="stat-box"><div class="num">7</div><div class="lbl">Calendar Events</div></div>
      <div class="stat-box"><div class="num">3</div><div class="lbl">Action Items</div></div>
      <div class="stat-box"><div class="num">5</div><div class="lbl">Spam / Phishing</div></div>
    </div>
  </div>

  <!-- ===================== SECURITY ALERT BANNER ===================== -->
  <div class="alert-banner">
    <span class="icon">🚨</span>
    <span><strong>SECURITY ALERT:</strong> 5 phishing/scam emails detected in your inbox and untracked folders. Do NOT click any links. See Security / Risk section below for full details.</span>
  </div>

  <!-- ===================== EXECUTIVE SUMMARY ===================== -->
  <div class="section-title">Executive Summary</div>
  <div class="exec-summary">
    <ul>
      <li>
        <span class="badge badge-red">🔴 Urgent Risk</span>
        <span><strong>Multiple phishing/scam emails</strong> are actively targeting your inbox — including fake Lowe's prize scams, fake cloud storage payment decline alerts, and a fraudulent PayPal transaction confirmation from a random Gmail address. These have <em>not</em> all been moved to trash and require immediate deletion. Do not interact with any links or attachments.</span>
      </li>
      <li>
        <span class="badge badge-green">🟢 Opportunity</span>
        <span><strong>Three LinkedIn job alerts</strong> are in your pipeline: Chief People Officer at The Trevor Project ($260K–$280K), VP People at ArcherReview, and Senior HR Business Partner at xAI. You also have an HR Networking & Job Search Zoom group meeting on June 24 that needs an RSVP. Strong week for your search — prioritize the Trevor Project role today.</span>
      </li>
      <li>
        <span class="badge badge-blue">🔵 Calendar</span>
        <span><strong>Dental appointment (Cavity) is TODAY at 10:30 AM.</strong> You also have an Eye Dr appointment on June 23, the Verizon Fios bill due June 23, HR Networking Zoom on June 24, and an Executive Roundtable on June 25 (currently marked as <em>declined</em> — confirm if intentional). Two networking Zoom sessions next week need RSVPs.</span>
      </li>
    </ul>
  </div>

  <!-- ===================== ACTION REQUIRED ===================== -->
  <div class="section-title">⚡ Action Required</div>
  <div class="card-grid">

    <div class="card card-red">
      <div class="card-label">🔴 Security — Phishing</div>
      <div class="card-title">Delete All Phishing / Scam Emails Immediately</div>
      <div class="card-source">Multiple senders (fake Lowe's, fake PayPal, fake cloud storage)</div>
      <div class="card-why">At least 5 phishing emails are sitting in your mail — fake Lowe's prize winners, fake PayPal transaction, and cloud storage account-blocked threats. These are designed to steal credentials or money. They are NOT in trash yet.</div>
      <div class="card-action">➜ Delete all without clicking. Mark as phishing/spam. See Security section for details.</div>
      <div class="card-due">⏰ Due: Today — do not delay</div>
    </div>

    <div class="card card-yellow">
      <div class="card-label">🟡 Financial — Billing</div>
      <div class="card-title">Bank of America Billing Dispute — Credit is Permanent</div>
      <div class="card-source">Bank of America &lt;onlinebanking@ealerts.bankofamerica.com&gt;</div>
      <div class="card-why">Your billing dispute for account ending in 2994 has been resolved. The credit is permanent (Step 3 of 3 complete). Log in to confirm the credit appears correctly on your statement.</div>
      <div class="card-action">➜ Log in to BofA and verify the permanent credit is reflected on account -2994.</div>
      <div class="card-due">⏰ Review today</div>
    </div>

    <div class="card card-yellow">
      <div class="card-label">🟡 Financial — Billing</div>
      <div class="card-title">Chase Credit Card Statement Ready — $126 Min Due</div>
      <div class="card-source">Chase &lt;no.reply.alerts@chase.com&gt;</div>
      <div class="card-why">Your Chase Credit Card (...5892) statement is available. Minimum payment due: $126.00. Due date: July 15, 2026. Review the full statement for any unauthorized charges.</div>
      <div class="card-action">➜ Log in to Chase, review statement, and schedule payment before July 15.</div>
      <div class="card-due">⏰ Payment due: July 15, 2026</div>
    </div>

    <div class="card card-yellow">
      <div class="card-label">🟡 Financial — Investment</div>
      <div class="card-title">Merrill Edge New Trade Confirmation</div>
      <div class="card-source">Merrill Edge &lt;merrilledge@ml.com&gt;</div>
      <div class="card-why">A new trade confirmation is available in your Merrill Edge account. You should verify the trade details match your intentions.</div>
      <div class="card-action">➜ Log in to Merrill Edge and review the trade confirmation details.</div>
      <div class="card-due">⏰ Review today</div>
    </div>

    <div class="card card-blue">
      <div class="card-label">🔵 Calendar — TODAY</div>
      <div class="card-title">Dental Appointment — Cavity Fill</div>
      <div class="card-source">Google Calendar</div>
      <div class="card-why">You have a dental appointment at 10:30 AM – 11:30 AM today. No location on file — confirm address if needed.</div>
      <div class="card-action">➜ Confirm location and depart on time. Avoid eating 2 hrs prior if possible.</div>
      <div class="card-due">⏰ Today, 10:30 AM</div>
    </div>

    <div class="card card-blue">
      <div class="card-label">🔵 Calendar — RSVP Needed</div>
      <div class="card-title">RSVP: HR Networking & Job Search Group Zoom (June 24)</div>
      <div class="card-source">Google Calendar — needsAction</div>
      <div class="card-why">The HR Networking & Job Search Group Zoom on June 24 (12:00–1:30 PM) has your RSVP as "needsAction." This is a large networking group with 190+ attendees — a high-value job search touchpoint.</div>
      <div class="card-action">➜ Accept or decline the invite now. Zoom link: us06web.zoom.us/j/81954171722</div>
      <div class="card-due">⏰ RSVP before June 24</div>
    </div>

    <div class="card card-blue">
      <div class="card-label">🔵 Calendar — RSVP Needed</div>
      <div class="card-title">RSVP: HR Networking Open Office Hours Zoom (June 25)</div>
      <div class="card-source">Google Calendar — needsAction</div>
      <div class="card-why">Another HR Networking open office hours session on June 25 (12:00–1:00 PM) also needs your RSVP. Note: organizer requests NO automated AI notetaking tools.</div>
      <div class="card-action">➜ Accept the invite. Zoom link: us06web.zoom.us/j/85945371140</div>
      <div class="card-due">⏰ RSVP before June 25</div>
    </div>

    <div class="card card-blue">
      <div class="card-label">🔵 Calendar — Confirm</div>
      <div class="card-title">Executive Roundtable — Currently DECLINED (June 25)</div>
      <div class="card-source">Google Calendar — Hosted by John Madigan</div>
      <div class="card-why">You have declined the Executive Roundtable on June 25 (9:00–10:30 AM via Zoom). This conflicts with nothing major. Confirm if declining was intentional — this could be a valuable executive networking opportunity.</div>
      <div class="card-action">➜ Confirm your decline is intentional, or re-accept if you want to attend.</div>
      <div class="card-due">⏰ Confirm before June 25</div>
    </div>

    <div class="card card-green">
      <div class="card-label">🟢 Job Search — High Priority</div>
      <div class="card-title">Apply: Chief People Officer @ The Trevor Project ($260K–$280K)</div>
      <div class="card-source">LinkedIn Job Alerts &lt;jobalerts-noreply@linkedin.com&gt;</div>
      <div class="card-why">A CPO role at The Trevor Project offering $260K–$280K/year. This is likely your highest-value lead this week given salary range and mission alignment (nonprofit + people leadership).</div>
      <div class="card-action">➜ Open LinkedIn alert, review JD, and begin tailoring your resume and cover letter today.</div>
      <div class="card-due">⏰ Apply ASAP — competitive role</div>
    </div>

    <div class="card card-yellow">
      <div class="card-label">🟡 Domain — Action</div>
      <div class="card-title">Domain Expiring in 30 Days — dhwcs.com (Zoho)</div>
      <div class="card-source">Zoho / domain-alerts@opensrs.zohomail.com</div>
      <div class="card-why">Two renewal notices arrived for a domain expiring ~July 18, 2026. One email is addressed to "Dennis" — verify if this domain belongs to you or is misdirected. If yours, ensure auto-renewal is enabled.</div>
      <div class="card-action">➜ Log in to Zoho Domains dashboard. Confirm if dhwcs.com is yours and enable auto-renewal.</div>
      <div class="card-due">⏰ Expires ~July 18, 2026</div>
    </div>

    <div class="card card-yellow">
      <div class="card-label">🟡 Shopping — Pickup</div>
      <div class="card-title">Nordstrom Rack Order Partially Ready for Pickup</div>
      <div class="card-source">Nordstrom Rack &lt;nordstromrack@eml.nordstromrack.com&gt;</div>
      <div class="card-why">Part of your Nordstrom Rack order #1046047427 is ready for pickup. The rest will be ready soon. You'll want to pick up before items are returned to stock.</div>
      <div class="card-action">➜ Visit Nordstrom Rack to pick up your available items. Monitor for full order readiness.</div>
      <div class="card-due">⏰ Pick up soon — today or this weekend</div>
    </div>

    <div class="card card-red">
      <div class="card-label">🔴 Medical — Follow-Up</div>
      <div class="card-title">Follow Up with Meghan (Medical Provider)</div>
      <div class="card-source">Melissa W &lt;melissaw212@gmail.com&gt; — Re: [EXTERNAL] Today</div>
      <div class="card-why">You sent an email to Meghan (a medical provider you've seen about your knee and eye issues) reaching out to reconnect. Monitor for a response and follow up if no reply by end of next week.</div>
      <div class="card-action">➜ Check for a reply from Meghan. Follow up if no response by June 26.</div>
      <div class="card-due">⏰ Follow up by: June 26</div>
    </div>

  </div>

  <!-- ===================== FULL 7-DAY CALENDAR ===================== -->
  <div class="section-title">📅 Full 7-Day Calendar</div>

  <!-- Friday June 19 -->
  <div class="cal-day">
    <div class="cal-day-header">Friday, June 19, 2026 <span class="day-badge">TODAY</span></div>
    <div class="cal-event">
      <div class="cal-time">10:30 AM<br>– 11:30 AM</div>
      <div class="cal-info">
        <div class="ev-title">🦷 Cavity (Dental Appointment)</div>
        <div class="ev-meta"><span class="rsvp-confirmed">✔ Confirmed</span> &nbsp;|&nbsp; Location: Not listed in calendar</div>
        <div class="ev-prep">📋 Prep: Confirm address with dental office. Arrive 10 minutes early. Avoid hard foods beforehand.</div>
      </div>
    </div>
  </div>

  <!-- Saturday June 20 -->
  <div class="cal-day">
    <div class="cal-day-header">Saturday, June 20, 2026</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-info">
        <div class="ev-title">— No events scheduled —</div>
        <div class="ev-meta">Use this time to review job applications, clean up inbox, and do Nordstrom Rack pickup.</div>
      </div>
    </div>
  </div>

  <!-- Sunday June 21 -->
  <div class="cal-day">
    <div class="cal-day-header">Sunday, June 21, 2026 <span class="day-badge">Father's Day</span></div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-info">
        <div class="ev-title">— No events scheduled —</div>
        <div class="ev-meta">Father's Day — plan accordingly if relevant.</div>
      </div>
    </div>
  </div>

  <!-- Monday June 22 -->
  <div class="cal-day">
    <div class="cal-day-header">Monday, June 22, 2026</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-info">
        <div class="ev-title">— No events scheduled —</div>
        <div class="ev-meta">Good day to send job applications and follow-up outreach.</div>
      </div>
    </div>
  </div>

  <!-- Tuesday June 23 -->
  <div class="cal-day">
    <div class="cal-day-header">Tuesday, June 23, 2026</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-info">
        <div class="ev-title">💳 Verizon Fios Bill Due</div>
        <div class="ev-meta"><span class="rsvp-confirmed">✔ Confirmed</span> &nbsp;|&nbsp; All-day billing reminder</div>
        <div class="ev-prep">📋 Prep: Log in to Verizon Fios account and ensure payment is processed by end of day.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-time">9:00 AM<br>– 10:00 AM</div>
      <div class="cal-info">
        <div class="ev-title">👁️ Eye Doctor Appointment</div>
        <div class="ev-meta"><span class="rsvp-confirmed">✔ Confirmed</span> &nbsp;|&nbsp; Location: Not listed in calendar</div>
        <div class="ev-prep">📋 Prep: Confirm location and whether you need a driver (eyes may be dilated). Bring insurance card and any prior prescription notes.</div>
      </div>
    </div>
  </div>

  <!-- Wednesday June 24 -->
  <div class="cal-day">
    <div class="cal-day-header">Wednesday, June 24, 2026</div>
    <div class="cal-event">
      <div class="cal-time">12:00 PM<br>– 1:30 PM</div>
      <div class="cal-info">
        <div class="ev-title">👥 HR Networking & Job Search Group — Zoom Session 2</div>
        <div class="ev-meta"><span class="rsvp-needs">⚠ Needs RSVP</span> &nbsp;|&nbsp; 190+ attendees</div>
        <div class="ev-meta">🔗 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" style="color:#2980b9;">Zoom Link</a> &nbsp;|&nbsp; Meeting ID: 819 5417 1722</div>
        <div class="ev-prep">📋 Prep: Review HR Networking Team Guidelines before joining. Prepare your 30-second professional introduction. RSVP today.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-time">12:00 PM<br>– 1:30 PM</div>
      <div class="cal-info">
        <div class="ev-title">🤝 Network (Personal Block)</div>
        <div class="ev-meta"><span class="rsvp-confirmed">✔ Confirmed</span> &nbsp;|&nbsp; No additional details</div>
        <div class="ev-conflict">⚠ Note: This block overlaps with the HR Networking Zoom above — same time slot. Likely the same session or a personal focus block for networking prep.</div>
      </div>
    </div>
  </div>

  <!-- Thursday June 25 -->
  <div class="cal-day">
    <div class="cal-day-header">Thursday, June 25, 2026</div>
    <div class="cal-event">
      <div class="cal-time">9:00 AM<br>– 10:30 AM</div>
      <div class="cal-info">
        <div class="ev-title">🏛️ Executive Roundtable — John Madigan (Zoom)</div>
        <div class="ev-meta"><span class="rsvp-declined">✘ DECLINED</span> &nbsp;|&nbsp; Host: John Madigan</div>
        <div class="ev-meta">🔗 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" style="color:#2980b9;">Zoom Link</a> &nbsp;|&nbsp; Meeting ID: 207 786 667 &nbsp;|&nbsp; PW: 205454</div>
        <div class="ev-prep">📋 Action: You've declined this. Confirm if intentional — executive roundtables are strong networking opportunities during job search.</div>
        <div class="ev-conflict">⚠ Status: Currently DECLINED. Consider reconsidering.</div>
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-time">12:00 PM<br>– 1:00 PM</div>
      <div class="cal-info">
        <div class="ev-title">💼 HR Networking & Job Search: Open Office Hours — Zoom Session 2</div>
        <div class="ev-meta"><span class="rsvp-needs">⚠ Needs RSVP</span> &nbsp;|&nbsp; 190+ attendees</div>
        <div class="ev-meta">🔗 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" style="color:#2980b9;">Zoom Link</a></div>
        <div class="ev-prep">📋 Prep: No automated notetaking AI tools per organizer request. Come with specific questions and goals. RSVP today.</div>
      </div>
    </div>
  </div>

  <!-- Friday June 26 -->
  <div class="cal-day">
    <div class="cal-day-header">Friday, June 26, 2026</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-info">
        <div class="ev-title">— No events scheduled —</div>
        <div class="ev-meta">Schedule follow-up outreach from this week's networking sessions. Review job application statuses.</div>
      </div>
    </div>
  </div>

  <!-- ===================== JOB SEARCH PIPELINE ===================== -->
  <div class="section-title">💼 Job Search & Interview Pipeline</div>
  <table>
    <thead>
      <tr>
        <th>Type</th>
        <th>Role / Opportunity</th>
        <th>Source</th>
        <th>Details</th>
        <th>Fit</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Job Alert</strong></td>
        <td><strong>Chief People Officer</strong><br>The Trevor Project</td>
        <td>LinkedIn Job Alerts</td>
        <td>$260K–$280K/year | Actively posted | Nonprofit / LGBTQ+ mission</td>
        <td><span class="fit-high">High</span></td>
        <td>Apply today — tailor resume + cover letter</td>
      </tr>
      <tr>
        <td><strong>Job Alert</strong></td>
        <td><strong>Vice President, People</strong><br>ArcherReview</td>
        <td>LinkedIn Job Alerts</td>
        <td>Actively accepting applications | EdTech / Healthcare prep sector</td>
        <td><span class="fit-high">High</span></td>
        <td>Review JD and apply if aligned</td>
      </tr>
      <tr>
        <td><strong>Job Alert</strong></td>
        <td><strong>Senior HR Business Partner</strong><br>xAI (Elon Musk's AI company)</td>
        <td>LinkedIn Job Alerts (Trash)</td>
        <td>High-growth AI startup | Fast-paced culture | Competitive comp expected</td>
        <td><span class="fit-med">Medium</span></td>
        <td>Email was in trash — restore and review if interested</td>
      </tr>
      <tr>
        <td><strong>Networking</strong></td>
        <td><strong>HR Networking & Job Search Group — Zoom #2</strong></td>
        <td>Google Calendar</td>
        <td>June 24, 12–1:30 PM | 190+ HR professionals | Needs RSVP</td>
        <td><span class="fit-high">High</span></td>
        <td>RSVP now. Prepare intro. Review guidelines doc.</td>
      </tr>
      <tr>
        <td><strong>Networking</strong></td>
        <td><strong>HR Networking Open Office Hours — Zoom #2</strong></td>
        <td>Google Calendar</td>
        <td>June 25, 12–1 PM | Open discussion | No AI notetakers | Needs RSVP</td>
        <td><span class="fit-high">High</span></td>
        <td>RSVP now. Bring specific job search questions.</td>
      </tr>
      <tr>
        <td><strong>Personal Note</strong></td>
        <td><strong>Interview Prep Materials</strong></td>
        <td>Melissa W (self-sent emails)</td>
        <td>Multiple self-emails with Instagram links labeled "Interview prep," "Fix resume prompt," "Stock" — appears to be saved content for reference</td>
        <td><span class="fit-med">Medium</span></td>
        <td>Consolidate links into a single doc or notes app for cleaner tracking</td>
      </tr>
      <tr>
        <td><strong>Executive Event</strong></td>
        <td><strong>Executive Roundtable — John Madigan</strong></td>
        <td>Google Calendar</td>
        <td>June 25, 9–10:30 AM | Currently DECLINED | Zoom</td>
        <td><span class="fit-med">Medium</span></td>
        <td>Reconsider attending — executive exposure during job search is valuable</td>
      </tr>
    </tbody>
  </table>

  <!-- ===================== FULL EMAIL REVIEW BY CATEGORY ===================== -->
  <div class="section-title">📬 Full Email Review by Category</div>

  <!-- SECURITY / RISK -->
  <div class="cat-block cat-red">
    <div class="cat-header">🔴 Security / Risk — Phishing & Scams <span class="count-pill">5</span></div>
    <div class="cat-body">
      <p><strong>Summary:</strong> Five confirmed phishing or scam emails. None appear to be legitimate. Do not click any links. Do not reply. Delete and mark as spam immediately.</p>
      <p class="sender-list"><strong>Senders:</strong><br>
        1. <em>"Lowe's®"</em> &lt;zcdpyhfilevwzs.48255136951710@hvwmvy.0ulhez.p07hw6.us&gt; — Fake Lowe's prize winner (Kobalt Tool Set). Domain is clearly fraudulent.<br>
        2. <em>"'Lowe's®'"</em> &lt;rizsupportkvj@ehyqswwvoycqjupayzvgtgos.com&gt; — Duplicate fake Lowe's scam, different fraudulent domain.<br>
        3. <em>"'Payment_Declined'"</em> &lt;ajpnjpacwwudjz.68351734704743@injyn4.4i6sep.34rocm.us&gt; — Fake cloud storage payment decline / account blocked threat. Unicode obfuscation in sender name.<br>
        4. <em>Payment-Declined</em> &lt;uxdphvdkshx@eyyx.ekcyohmjjdksj.us&gt; — Duplicate cloud storage phishing, different fraudulent domain.<br>
        5. <em>ggfyu2892@gmail.com</em> — Fake PayPal transaction confirmation from a random Gmail address (Ref: TXN-EI58-DR7J-M5ZQ). Not a legitimate PayPal email.
      </p>
      <span class="rec rec-act">🔴 ACTION: Delete & Mark as Spam Immediately</span>
    </div>
  </div>

  <!-- JOB SEARCH -->
  <div class="cat-block cat-green">
    <div class="cat-header">🟢 Job Search / Opportunities <span class="count-pill">4</span></div>
    <div class="cat-body">
      <p><strong>Summary:</strong> Three LinkedIn job alerts for senior HR leadership roles (CPO, VP People, Sr. HRBP) and one set of self-sent interview prep links. All are actionable this week.</p>
      <p class="sender-list"><strong>Senders:</strong> LinkedIn Job Alerts (×3 — Chief People Officer at Trevor Project, VP People at ArcherReview, Sr. HRBP at xAI); Melissa W self-sent "Interview prep" email</p>
      <span class="rec rec-act">🟢 ACTION: Review all three roles and apply to highest-fit positions</span>
    </div>
  </div>

  <!-- PERSONAL / SELF-SENT -->
  <div class="cat-block cat-purple">
    <div class="cat-header">🟣 Personal / Self-Sent Notes <span class="count-pill">9</span></div>
    <div class="cat-body">
      <p><strong>Summary:</strong> Melissa sent herself 9 emails from her own Gmail account, mostly Instagram links with subject lines like "Interview prep," "Fix resume prompt," "Stock," "Re: [EXTERNAL] Today" (medical provider outreach). These serve as personal reminders and saved content.</p>
      <p class="sender-list"><strong>Subjects:</strong> "Interview prep" (×2), "Fix resume prompt," "Stock," "(blank subject)" (×4 Instagram links), "Re: [EXTERNAL] Today" (medical note to Meghan)</p>
      <span class="rec rec-rev">🟡 REVIEW: Consolidate all links into a notes app (Notion, Google Keep). Archive the medical email after confirming follow-up.</span>
    </div>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="cat-block cat-yellow">
    <div class="cat-header">🟡 Financial / Billing <span class="count-pill">5</span></div>
    <div class="cat-body">
      <p><strong>Summary:</strong> Important financial activity this morning — a resolved BofA dispute, a new Chase statement, a Merrill Edge trade confirmation, and two Robinhood notifications (IRA contribution started + $15 instant deposit available).</p>
      <p class="sender-list"><strong>Senders:</strong> Bank of America (billing dispute resolved — permanent credit on account -2994), Chase (statement ready — min $126 due July 15, account ...5892), Merrill Edge (new trade confirmation), Robinhood (IRA contribution started), Robinhood (funds available — $15 instant deposit)</p>
      <span class="rec rec-act">🟡 ACTION: Verify BofA credit, review Chase statement, check Merrill trade confirmation</span>
    </div>
  </div>

  <!-- MEDICAL / HEALTH -->
  <div class="cat-block cat-blue">
    <div class="cat-header">🔵 Medical / Health <span class="count-pill">1</span></div>
    <div class="cat-body">
      <p><strong>Summary:</strong> One email from Citizen app reporting a local public safety incident (two men fatally shot, investigation ongoing, no arrests). This is a neighborhood safety notification, not a personal medical issue.</p>
      <p class="sender-list"><strong>Sender:</strong> Citizen &lt;noreply@mail.citizen.com&gt; — Public safety alert for your area in York</p>
      <span class="rec rec-rev">🟡 REVIEW: Stay informed. Adjust your Citizen alert preferences if notifications are too frequent.</span>
    </div>
  </div>

  <!-- DOMAIN / TECHNICAL -->
  <div class="cat-block cat-yellow">
    <div class="cat-header">🟡 Domain Renewal / Technical Notices <span class="count-pill">2</span></div>
    <div class="cat-body">
      <p><strong>Summary:</strong> Two domain renewal notices from Zoho — one addressed to "Dennis" (possible misdirected email) and one general 30-day renewal reminder for dhwcs.com expiring ~July 18, 2026.</p>
      <p class="sender-list"><strong>Senders:</strong> noreply@zoho.com (addressed to Dennis — possible mismatch), domain-alerts@opensrs.zohomail.com (30-day reminder)</p>
      <span class="rec rec-act">🟡 ACTION: Verify if dhwcs.com is your domain. Enable auto-renewal in Zoho Domains dashboard.</span>
    </div>
  </div>

  <!-- SHOPPING / ORDERS -->
  <div class="cat-block cat-blue">
    <div class="cat-header">🔵 Orders / Deliveries (Actionable) <span class="count-pill">4</span></div>
    <div class="cat-body">
      <p><strong>Summary:</strong> Active orders and shipments you should be tracking: Nordstrom Rack order partially ready for pickup, TikTok Shop "Coconut Cutie" order shipped, Sephora order arriving soon, and original Nordstrom Rack order confirmation #1046047427.</p>
      <p class="sender-list"><strong>Senders:</strong> Nordstrom Rack (pickup ready — order partially available), Nordstrom Rack (order #1046047427 confirmation), TikTok Shop (order shipped — Coconut Cutie), Sephora (arriving soon)</p>
      <span class="rec rec-rev">🟡 REVIEW: Pick up Nordstrom Rack items today. Track TikTok Shop and Sephora deliveries.</span>
    </div>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="cat-block cat-purple">
    <div class="cat-header">🟣 Professional Development <span class="count-pill">1</span></div>
    <div class="cat-body">
      <p><strong>Summary:</strong> One email from Alison Courses promoting a digital literacy course to help feel more confident online.</p>
      <p class="sender-list"><strong>Sender:</strong> Alison Courses &lt;noreply@us-news.alison.com&gt; — Digital literacy course promotion</p>
      <span class="rec rec-rev">🟡 REVIEW: Low priority given your current job search focus. Revisit if interested in upskilling later.</span>
    </div>
  </div>

  <!-- SOCIAL / DATING -->
  <div class="cat-block cat-gray">
    <div class="cat-header">⚪ Social / Dating App Notifications <span class="count-pill">4</span></div>
    <div class="cat-body">
      <p><strong>Summary:</strong> Notification emails from Match and OkCupid — unread message on Match, "John likes you" on Match, OkCupid intro received, someone likes you on OkCupid. Low-priority for the executive briefing.</p>
      <p class="sender-list"><strong>Senders:</strong> Match (×2 — unread message + John likes you), OkCupid (×2 — intro + someone likes you)</p>
      <span class="rec rec-del">⚪ LOW PRIORITY: Review at your leisure. Manage notification preferences if volume is excessive.</span>
    </div>
  </div>

  <!-- LG ACCOUNT -->
  <div class="cat-block cat-gray">
    <div class="cat-header">⚪ Account / Platform Notices <span class="count-pill">1</span></div>
    <div class="cat-body">
      <p><strong>Summary:</strong> LG Account notification about termination of Amazon Social Login for LG Electronics services. Low urgency — you may need to set up an alternative login method for LG products.</p>
      <p class="sender-list"><strong>Sender:</strong> LG Account &lt;supportlgaccount@lge.com&gt;</p>
      <span class="rec rec-rev">🟡 LOW PRIORITY: Note for future reference if you use LG services and log in via Amazon.</span>
    </div>
  </div>

  <!-- NEWSLETTERS -->
  <div class="cat-block cat-purple">
    <div class="cat-header">🟣 Newsletters / Subscriptions (Inbox) <span class="count-pill">3</span></div>
    <div class="cat-body">
      <p><strong>Summary:</strong> Three newsletter emails in inbox — "1% Better" (daily optimization/self-improvement), CoolDeep AI (in trash — AI tools roundup), and The Daily Skimm (in trash — lifestyle/news).</p>
      <p class="sender-list"><strong>Senders:</strong> "1% Better" (daily optimization — inbox), CoolDeep AI (AI tools — trash), The Daily Skimm (lifestyle/news — trash)</p>
      <span class="rec rec-rev">🟡 REVIEW: "1% Better" — keep if you find it valuable. Others in trash — confirm deletion.</span>
    </div>
  </div>

  <!-- PROMOTIONAL / RETAIL -->
  <div class="cat-block cat-gray">
    <div class="cat-header">⚪ Promotional / Retail <span class="count-pill">9</span></div>
    <div class="cat-body">
      <p><strong>Summary:</strong> Nine promotional retail emails — Quince (summer red collection), SHEIN (×2 duplicate best sellers), Kohl's (30% off summer), Old Navy (PowerChill 60% off), YesStyle (15% off), Temu (price drop deal), AllEvents (weekend events in York). Low priority today.</p>
      <p class="sender-list"><strong>Senders:</strong> Quince, SHEIN (×2), Kohl's, Old Navy, YesStyle.com, Temu, AllEvents</p>
      <span class="rec rec-del">⚪ LOW PRIORITY: Batch review if shopping. Delete duplicates (SHEIN sent same email twice). Unsubscribe from non-value senders.</span>
    </div>
  </div>

  <!-- TRASH EMAILS (reviewed separately) -->
  <div class="cat-block cat-gray">
    <div class="cat-header">🗑️ Trash Review (see dedicated section below) <span class="count-pill">6</span></div>
    <div class="cat-body">
      <p><strong>Summary:</strong> 6 emails currently in Gmail Trash — reviewed and categorized in the Trash Review section below.</p>
      <p class="sender-list"><strong>Senders:</strong> Stephanie Wigner, TLDR (×2), The Daily Skimm, CoolDeep AI, LinkedIn Job Alerts (Sr. HRBP at xAI)</p>
      <span class="rec rec-del">See Trash Review section for restore/delete recommendations.</span>
    </div>
  </div>

  <!-- TECH / AI NEWS (TLDR) moved here as newsletter but duplicate noted in trash -->
  <div class="cat-block cat-purple">
    <div class="cat-header">🟣 Tech / AI News (TLDR Newsletter — Trash) <span class="count-pill">2</span></div>
    <div class="cat-body">
      <p><strong>Summary:</strong> Two duplicate copies of the same TLDR newsletter email (Midjourney Scanner, AWS vs Nvidia, agent loop architecture) are in trash. Both are the same email sent at slightly different times.</p>
      <p class="sender-list"><strong>Sender:</strong> TLDR &lt;dan@tldrnewsletter.com&gt; — AI/tech news digest</p>
      <span class="rec rec-del">⚪ DELETE: Duplicates. If you enjoy TLDR, keep the subscription but delete redundant copies.</span>
    </div>
  </div>

  <hr class="divider">

  <!-- ===================== TRASH REVIEW ===================== -->
  <div class="section-title">🗑️ Trash Review</div>
  <p style="font-size:13px; color:#666; margin-bottom:14px;">6 emails are currently in Gmail Trash. Reviewed below into three groups.</p>

  <div class="trash-group">
    <div class="trash-group-header trash-restore">🟢 Restore Immediately (1)</div>
    <div class="trash-item">
      <strong>LinkedIn Job Alerts</strong> — "Senior HR Business Partner at xAI"<br>
      <span style="color:#666; font-size:12px;">Reason to restore: This is a legitimate job opportunity at Elon Musk's AI company (xAI). It was likely auto-filtered to trash but belongs in your job search pipeline. Restore, review the JD, and decide if you want to apply.</span>
    </div>
  </div>

  <div class="trash-group">
    <div class="trash-group-header trash-review">🟡 Review Before Deleting (1)</div>
    <div class="trash-item">
      <strong>TLDR Newsletter</strong> — "Midjourney Scanner 🏥, AWS vs Nvidia ⚡, agent loop architecture 👨‍💻" (×2 duplicates — both in trash)<br>
      <span style="color:#666; font-size:12px;">Reason to review: TLDR is a reputable AI/tech newsletter. The content (Midjourney medical hardware, AWS vs. Nvidia, agent loop architecture) may be relevant if you're interested in staying current on AI for job interviews in tech-adjacent HR roles. Review one copy, delete both if not interested, or restore if you want to read it. If you want to keep receiving TLDR, update your filter settings so future emails reach inbox.</span>
    </div>
  </div>

  <div class="trash-group">
    <div class="trash-group-header trash-delete">⚪ Safe to Delete (3)</div>
    <div class="trash-item">
      <strong>Stephanie Wigner</strong> — "What a billionaire's private island taught me about your next move"<br>
      <span style="color:#666; font-size:12px;">Reason: Promotional/motivational marketing email. Low value. Safely deleted.</span>
    </div>
    <div class="trash-item">
      <strong>The Daily Skimm</strong> — "Hello, Melt-In-Your-Mouth Tea Cakes 😍"<br>
      <span style="color:#666; font-size:12px;">Reason: Lifestyle newsletter. Low priority. Safely deleted. Consider unsubscribing if inbox volume is a concern.</span>
    </div>
    <div class="trash-item">
      <strong>CoolDeep AI</strong> — "I tested hundreds of AI tools. I kept 7"<br>
      <span style="color:#666; font-size:12px;">Reason: AI tools newsletter — mildly interesting but low priority given current job search focus. Safely deleted. May be worth a quick scan if AI tools are relevant to your work.</span>
    </div>
  </div>

  <hr class="divider">

  <!-- ===================== PROMOTIONAL / RETAIL SUMMARY ===================== -->
  <div class="section-title">🛍️ Promotional / Retail Summary</div>
  <table class="promo-table">
    <thead>
      <tr>
        <th>Brand / Sender</th>
        <th>Count</th>
        <th>Subject / Theme</th>
        <th>In Inbox?</th>
        <th>Recommendation</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>SHEIN</strong></td>
        <td>2</td>
        <td>"These best sellers are a must-have!" — sent twice (duplicate)</td>
        <td>Yes</td>
        <td><span class="rec rec-del">Delete Duplicate</span></td>
      </tr>
      <tr>
        <td><strong>Quince</strong></td>
        <td>1</td>
        <td>"Introducing the color of the season" — summer red in European linen & cotton gauze</td>
        <td>Yes</td>
        <td><span class="rec rec-rev">Review if interested</span></td>
      </tr>
      <tr>
        <td><strong>Kohl's</strong></td>
        <td>1</td>
        <td>"Save 30% | Find outfits for every summer occasion" — Father's Day gifting + Kohl's Cash</td>
        <td>Yes</td>
        <td><span class="rec rec-rev">Review if shopping</span></td>
      </tr>
      <tr>
        <td><strong>Old Navy</strong></td>
        <td>1</td>
        <td>"ALL women's & girls PowerChill 60% off + sale picks from $8" — free shipping for Encore Members
<hr>
<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Financial / Billing</td><td>4</td></tr>
<tr><td>Job Search / Recruiters</td><td>6</td></tr>
<tr><td>Medical / Health</td><td>3</td></tr>
<tr><td>Other / Review</td><td>29</td></tr>
<tr><td>Professional Development / Newsletters</td><td>1</td></tr>
<tr><td>Promotional / Retail</td><td>2</td></tr>
<tr><td>Security / Risk</td><td>5</td></tr>
</table>
<p><strong>Audit Note:</strong> Every fetched email was reviewed and assigned to one category. Trash emails were included in review. Promotional and low-value emails were accounted for but deprioritized.</p>

