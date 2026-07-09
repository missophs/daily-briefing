<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing – Melissa A. Weiss | July 9, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px 60px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px 28px; margin-bottom: 24px; box-shadow: 0 4px 24px rgba(0,0,0,0.18); }
  .header h1 { font-size: 2rem; font-weight: 700; letter-spacing: 0.5px; }
  .header .sub { font-size: 1rem; color: #a8c0e8; margin-top: 4px; }
  .header-meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header-meta .meta-box { background: rgba(255,255,255,0.09); border-radius: 8px; padding: 10px 18px; text-align: center; }
  .header-meta .meta-box .num { font-size: 1.6rem; font-weight: 700; color: #7ec8e3; }
  .header-meta .meta-box .label { font-size: 0.75rem; color: #bcd0ef; text-transform: uppercase; letter-spacing: 0.5px; }
  .timestamp { margin-top: 14px; font-size: 0.78rem; color: #7a9cc5; }

  /* SECTION HEADERS */
  .section-title { font-size: 1.05rem; font-weight: 700; letter-spacing: 0.4px; padding: 8px 16px; border-radius: 7px 7px 0 0; margin-bottom: 0; text-transform: uppercase; }
  .section-wrap { background: #fff; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.07); margin-bottom: 22px; overflow: hidden; }
  .section-body { padding: 18px 20px; }

  /* COLOR THEMES */
  .red-head { background: #c0392b; color: #fff; }
  .yellow-head { background: #e67e22; color: #fff; }
  .blue-head { background: #2471a3; color: #fff; }
  .green-head { background: #1e8449; color: #fff; }
  .purple-head { background: #6c3483; color: #fff; }
  .gray-head { background: #717d7e; color: #fff; }
  .navy-head { background: #1a1a2e; color: #fff; }
  .teal-head { background: #148f77; color: #fff; }

  .red-card { border-left: 5px solid #c0392b; background: #fdf2f2; border-radius: 7px; padding: 14px 16px; margin-bottom: 12px; }
  .yellow-card { border-left: 5px solid #e67e22; background: #fef9f0; border-radius: 7px; padding: 14px 16px; margin-bottom: 12px; }
  .blue-card { border-left: 5px solid #2471a3; background: #eaf4fb; border-radius: 7px; padding: 14px 16px; margin-bottom: 12px; }
  .green-card { border-left: 5px solid #1e8449; background: #eafaf1; border-radius: 7px; padding: 14px 16px; margin-bottom: 12px; }
  .purple-card { border-left: 5px solid #6c3483; background: #f5eef8; border-radius: 7px; padding: 14px 16px; margin-bottom: 12px; }
  .gray-card { border-left: 5px solid #717d7e; background: #f4f6f7; border-radius: 7px; padding: 14px 16px; margin-bottom: 12px; }
  .teal-card { border-left: 5px solid #148f77; background: #e8f8f5; border-radius: 7px; padding: 14px 16px; margin-bottom: 12px; }

  .card-title { font-weight: 700; font-size: 0.95rem; margin-bottom: 4px; }
  .card-meta { font-size: 0.78rem; color: #555; margin-bottom: 6px; }
  .card-body { font-size: 0.85rem; }
  .badge { display: inline-block; padding: 2px 8px; border-radius: 10px; font-size: 0.72rem; font-weight: 700; margin-right: 4px; margin-bottom: 2px; text-transform: uppercase; }
  .badge-red { background: #c0392b; color: #fff; }
  .badge-yellow { background: #e67e22; color: #fff; }
  .badge-green { background: #1e8449; color: #fff; }
  .badge-blue { background: #2471a3; color: #fff; }
  .badge-purple { background: #6c3483; color: #fff; }
  .badge-gray { background: #717d7e; color: #fff; }
  .badge-teal { background: #148f77; color: #fff; }

  /* EXEC SUMMARY */
  .exec-bullets { list-style: none; padding: 0; }
  .exec-bullets li { padding: 10px 14px; border-radius: 7px; margin-bottom: 10px; font-size: 0.92rem; font-weight: 500; }
  .bullet-red { background: #fdf2f2; border-left: 5px solid #c0392b; }
  .bullet-green { background: #eafaf1; border-left: 5px solid #1e8449; }
  .bullet-blue { background: #eaf4fb; border-left: 5px solid #2471a3; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 0.83rem; }
  th { background: #1a1a2e; color: #fff; padding: 9px 12px; text-align: left; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.3px; }
  td { padding: 8px 12px; border-bottom: 1px solid #e8ecef; vertical-align: top; }
  tr:nth-child(even) td { background: #f8f9fa; }
  tr:last-child td { border-bottom: none; }
  .priority-high { color: #c0392b; font-weight: 700; }
  .priority-med { color: #e67e22; font-weight: 700; }
  .priority-low { color: #717d7e; font-weight: 600; }

  /* CALENDAR */
  .cal-day { margin-bottom: 16px; }
  .cal-day-header { background: #16213e; color: #7ec8e3; padding: 7px 14px; border-radius: 6px; font-weight: 700; font-size: 0.88rem; margin-bottom: 8px; letter-spacing: 0.3px; }
  .cal-event { display: flex; gap: 12px; padding: 10px 14px; background: #eaf4fb; border-radius: 7px; margin-bottom: 7px; border-left: 4px solid #2471a3; }
  .cal-time { min-width: 90px; font-weight: 700; font-size: 0.82rem; color: #2471a3; }
  .cal-detail .ev-title { font-weight: 700; font-size: 0.9rem; }
  .cal-detail .ev-meta { font-size: 0.78rem; color: #555; margin-top: 2px; }
  .cal-event.declined { border-left-color: #c0392b; background: #fdf2f2; }
  .cal-event.needs-action { border-left-color: #e67e22; background: #fef9f0; }
  .cal-event.confirmed { border-left-color: #1e8449; background: #eafaf1; }
  .cal-event.all-day { border-left-color: #6c3483; background: #f5eef8; }
  .conflict-warn { font-size: 0.75rem; color: #c0392b; font-weight: 700; margin-top: 3px; }

  /* DASHBOARD GRID */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; }
  .dash-box { border-radius: 9px; padding: 14px 16px; text-align: center; }
  .dash-box .dash-num { font-size: 2rem; font-weight: 800; }
  .dash-box .dash-label { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 2px; }
  .db-red { background: #fdf2f2; border: 2px solid #c0392b; color: #c0392b; }
  .db-yellow { background: #fef9f0; border: 2px solid #e67e22; color: #e67e22; }
  .db-green { background: #eafaf1; border: 2px solid #1e8449; color: #1e8449; }
  .db-blue { background: #eaf4fb; border: 2px solid #2471a3; color: #2471a3; }
  .db-purple { background: #f5eef8; border: 2px solid #6c3483; color: #6c3483; }
  .db-gray { background: #f4f6f7; border: 2px solid #717d7e; color: #717d7e; }

  /* TOP 3 */
  .top3 { display: flex; gap: 14px; flex-wrap: wrap; }
  .top3-item { flex: 1; min-width: 260px; border-radius: 10px; padding: 18px 20px; color: #fff; }
  .top3-num { font-size: 2.5rem; font-weight: 900; opacity: 0.3; line-height: 1; }
  .top3-text { font-size: 0.95rem; font-weight: 600; margin-top: 4px; }
  .top3-sub { font-size: 0.78rem; opacity: 0.85; margin-top: 4px; }
  .t3-red { background: linear-gradient(135deg, #c0392b, #e74c3c); }
  .t3-green { background: linear-gradient(135deg, #1e8449, #27ae60); }
  .t3-blue { background: linear-gradient(135deg, #1a5276, #2471a3); }

  /* MISC */
  .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
  .fit-high { color: #1e8449; font-weight: 700; }
  .fit-med { color: #e67e22; font-weight: 700; }
  .fit-low { color: #717d7e; font-weight: 600; }
  .tag { display: inline-block; background: #eaf4fb; color: #2471a3; border-radius: 4px; padding: 1px 7px; font-size: 0.72rem; font-weight: 700; margin-right: 3px; }
  hr.divider { border: none; border-top: 1px solid #e0e4ea; margin: 12px 0; }
  .note { font-size: 0.78rem; color: #777; font-style: italic; margin-top: 8px; }
  a { color: #2471a3; text-decoration: none; }
  .spam-warn { background: #fdf2f2; border: 1px solid #c0392b; border-radius: 6px; padding: 8px 12px; font-size: 0.82rem; color: #c0392b; font-weight: 600; margin-bottom: 8px; }
  .restore-tag { background: #1e8449; color: #fff; border-radius: 4px; padding: 1px 7px; font-size: 0.72rem; font-weight: 700; }
  .review-tag { background: #e67e22; color: #fff; border-radius: 4px; padding: 1px 7px; font-size: 0.72rem; font-weight: 700; }
  .delete-tag { background: #717d7e; color: #fff; border-radius: 4px; padding: 1px 7px; font-size: 0.72rem; font-weight: 700; }
  @media(max-width:700px){ .two-col{grid-template-columns:1fr;} .top3{flex-direction:column;} }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ===== HEADER ===== -->
<div class="header">
  <h1>☀️ Good Morning, Melissa</h1>
  <div class="sub">Executive Briefing — Thursday, July 9, 2026</div>
  <div class="header-meta">
    <div class="meta-box"><div class="num">50</div><div class="label">Emails Reviewed</div></div>
    <div class="meta-box"><div class="num">11</div><div class="label">Calendar Events</div></div>
    <div class="meta-box"><div class="num">3</div><div class="label">Action Items</div></div>
    <div class="meta-box"><div class="num">2</div><div class="label">Packages Arriving</div></div>
    <div class="meta-box"><div class="num">1</div><div class="label">Interview Tomorrow</div></div>
  </div>
  <div class="timestamp">Prepared by your Executive Chief of Staff · All 50 emails accounted for · 11 calendar events reviewed</div>
</div>

<!-- ===== EXECUTIVE SUMMARY ===== -->
<div class="section-wrap">
  <div class="section-title red-head">⚡ Executive Summary</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li class="bullet-red">🚨 <strong>Security Risk:</strong> Two confirmed phishing/spam emails (fake "Cloud.Security" storage threats and a casino spam) are sitting in your inbox folders. Do not click any links. Mark as phishing and delete immediately. Your Apify subscription has also hit 50% of its monthly $69 usage — review before overage charges hit.</li>
      <li class="bullet-green">💼 <strong>Career Opportunity:</strong> You have a phone screen tomorrow (Fri, July 10 at 2:00 PM) with Joelle Molina at Oscar Health for the <strong>People Strategy Lead</strong> role — your highest-priority job lead this week. Also, a new LinkedIn InMail from RWJBarnabas Health about an HR Business Opportunity requires your response today.</li>
      <li class="bullet-blue">📅 <strong>Calendar Priority:</strong> You have a <strong>medical appointment today at 3:30 PM</strong> with Dr. Beth A. Leeman-Markowski at the Comprehensive Epilepsy Center (223 E 34th St) — arrive by 3:15 PM. Also, your Northwell MyNorthwell reminder for a visit tomorrow July 10 at 3:30 PM with Dr. Crystal Lee needs attention.</li>
    </ul>
  </div>
</div>

<!-- ===== ACTION REQUIRED ===== -->
<div class="section-wrap">
  <div class="section-title yellow-head">⚠️ Action Required</div>
  <div class="section-body">

    <div class="red-card">
      <div class="card-meta"><span class="badge badge-red">🚨 URGENT – SECURITY</span> From: "Cloud.Security" &lt;owcjsfmabrw@gbnn.uukpwcysoityj.us&gt; | Today</div>
      <div class="card-title">FINAL NOTICE: Your photos will be deleted tonight [Thu, 09 Jul-2026]</div>
      <div class="card-body">⚠️ <strong>This is a phishing email.</strong> The sender domain is fake and suspicious. Do NOT click any links or update any billing info. This is a social engineering scare tactic.<br><strong>Action:</strong> Mark as phishing → Delete permanently. Do not interact.</div>
    </div>

    <div class="red-card">
      <div class="card-meta"><span class="badge badge-red">🚨 URGENT – SECURITY</span> From: "Payment_Declined" &lt;jgmdsupportnxrq@diinpfbukskjshgedzlhkmbm.com&gt; | Today</div>
      <div class="card-title">Your Account Has Been Blocked! Your Photos and Videos will be Removed Thu, 09 Jul-2026</div>
      <div class="card-body">⚠️ <strong>This is a phishing email.</strong> Fake cloud storage threat from an obviously malicious domain. Do not click.<br><strong>Action:</strong> Mark as phishing → Delete permanently.</div>
    </div>

    <div class="green-card">
      <div class="card-meta"><span class="badge badge-green">💼 HIGH PRIORITY – JOB</span> From: Ayesha Sadiqua via LinkedIn | Today</div>
      <div class="card-title">HR Business Opportunity at RWJBarnabas Health Corporate Services</div>
      <div class="card-body">A recruiter reached out directly via LinkedIn InMail about an HR role at RWJBarnabas Health. No expiry listed but InMails are time-sensitive.<br><strong>Action:</strong> Review full InMail on LinkedIn. Respond today if interested. <strong>Due: Today, July 9</strong></div>
    </div>

    <div class="green-card">
      <div class="card-meta"><span class="badge badge-green">💼 HIGH PRIORITY – INTERVIEW</span> Google Calendar | Tomorrow, July 10</div>
      <div class="card-title">Oscar Health Phone Screen – People Strategy Lead (2:00 PM)</div>
      <div class="card-body">Phone screen with Joelle Molina (joelle@hioscar.com). They will call 516-313-8888. Role: People Strategy Lead.<br><strong>Action:</strong> Prepare talking points, review Oscar Health's People/HR strategy, confirm your phone is available. <strong>Due: Tonight / Tomorrow AM</strong></div>
    </div>

    <div class="blue-card">
      <div class="card-meta"><span class="badge badge-blue">📅 TODAY – MEDICAL</span> From: MyNorthwell | Today</div>
      <div class="card-title">Doctor Visit Tomorrow (July 10) – Dr. Crystal Lee, MD — 178 East 85th Street, 2nd Floor, 3:30 PM</div>
      <div class="card-body">Northwell sent a "get ready for your visit" reminder for July 10 at 3:30 PM with Dr. Crystal Lee. Confirm insurance card, ID, and any required forms.<br><strong>Action:</strong> Review pre-visit checklist. Confirm appointment if needed. <strong>Due: Tonight</strong></div>
    </div>

    <div class="blue-card">
      <div class="card-meta"><span class="badge badge-blue">📅 TODAY – MEDICAL</span> Google Calendar | Today, 3:30 PM</div>
      <div class="card-title">Appointment with Dr. Beth A. Leeman-Markowski, MD – Comprehensive Epilepsy Center</div>
      <div class="card-body">223 East 34th Street, New York, NY 10016. Arrive 15 minutes early (3:15 PM). Bring: insurance card, photo ID, medical records, recent labs/test results.<br><strong>Action:</strong> Leave in time. Phone: 646-558-0800 if you need to reschedule. <strong>Due: Today by 3:15 PM</strong></div>
    </div>

    <div class="yellow-card">
      <div class="card-meta"><span class="badge badge-yellow">💳 BILLING</span> From: Conservice | Today</div>
      <div class="card-title">Monthly Utility Statement for 303 East 83rd – Due 8/1/2026</div>
      <div class="card-body">Your utility bill for account ending in 3876 is ready. Due date: August 1, 2026.<br><strong>Action:</strong> Review statement and schedule payment before 8/1/2026.</div>
    </div>

    <div class="yellow-card">
      <div class="card-meta"><span class="badge badge-yellow">⚙️ PLATFORM</span> From: Apify | Today</div>
      <div class="card-title">Apify Platform Usage at 50% of $69.00 Monthly Budget</div>
      <div class="card-body">You've used 50% of your Apify platform budget mid-cycle. If usage continues at this pace, you may exceed the plan.<br><strong>Action:</strong> Log into Apify, review active actors/runs, and pause anything non-essential. <strong>Due: Today</strong></div>
    </div>

    <div class="yellow-card">
      <div class="card-meta"><span class="badge badge-yellow">📦 DELIVERY</span> From: Temu | Today</div>
      <div class="card-title">2 Temu Packages Out for Delivery Today</div>
      <div class="card-body">Orders #PO-211-13384130622071025 and #PO-211-13384128686711025 are both out for delivery. Be available to receive.<br><strong>Action:</strong> Ensure someone is available or check building mailroom. <strong>Due: Today</strong></div>
    </div>

    <div class="yellow-card">
      <div class="card-meta"><span class="badge badge-yellow">📬 CALENDAR RSVP</span> Google Calendar | Today 12:00 PM</div>
      <div class="card-title">HR Networking & Job Search Open Office Hours – Zoom (RSVP Pending)</div>
      <div class="card-body">Status: "Needs Action" — you have not responded. Session runs 12:00–1:00 PM today with a large HR networking group.<br><strong>Action:</strong> Accept or decline. If relevant to your search, attend. Link: us06web.zoom.us/j/85945371140. <strong>Due: Before noon today</strong></div>
    </div>

    <div class="yellow-card">
      <div class="card-meta"><span class="badge badge-yellow">🤝 LINKEDIN</span> From: Muhammad Hanzla via LinkedIn | Today</div>
      <div class="card-title">Message Replied: Career Opportunity – Outsourced HR Business Partner | New York</div>
      <div class="card-body">Someone replied "sure..." to a conversation about an HR Business Partner role in New York. Follow up to keep the thread warm.<br><strong>Action:</strong> Review the full LinkedIn message thread and reply with next steps. <strong>Due: Today</strong></div>
    </div>

    <div class="teal-card">
      <div class="card-meta"><span class="badge badge-teal">💻 AUTOMATION</span> From: no-reply-claude@mail.anthropic.com | Today</div>
      <div class="card-title">Daily Briefing Dispatch FAILED – GitHub Action Not Running</div>
      <div class="card-body">Two emails confirm that the daily-briefing-dispatch Claude routine failed at 7:08 AM ET due to no GitHub connector or gh CLI in environment. Manual trigger required.<br><strong>Action:</strong> Go to github.com/missophs/daily-briefing → Actions → Daily Briefing → Run workflow → branch: webhooks. <strong>Due: Today</strong></div>
    </div>

    <div class="teal-card">
      <div class="card-meta"><span class="badge badge-teal">🐾 COMMUNITY</span> From: HomeAgain PetRescuers | Today</div>
      <div class="card-title">Lost Cat "Lecter" — Throop Ave between Hart St and Pulaski St, Brooklyn (Ref. HAP-1890967)</div>
      <div class="card-body">A cat named Lecter is missing near Brooklyn, NY 11206. If you're near that area or know someone who is, check the listing.<br><strong>Action:</strong> Share with neighbors/community if applicable. Optional community action.</div>
    </div>

    <div class="teal-card">
      <div class="card-meta"><span class="badge badge-teal">💰 SIDE INCOME</span> From: UserTesting (Remi) | Today</div>
      <div class="card-title">Invited to First Paid Study – Earn $125</div>
      <div class="card-body">UserTesting has invited you to apply for a paid study. First study invitation.<br><strong>Action:</strong> Review email, apply if you have time. Easy $125. Check availability requirements. <strong>Time-sensitive</strong></div>
    </div>

  </div>
</div>

<!-- ===== FULL 7-DAY CALENDAR ===== -->
<div class="section-wrap">
  <div class="section-title blue-head">📅 Full 7-Day Calendar</div>
  <div class="section-body">

    <!-- THURSDAY JULY 9 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Thursday, July 9, 2026 — TODAY</div>

      <div class="cal-event declined">
        <div class="cal-time">9:00–10:30 AM</div>
        <div class="cal-detail">
          <div class="ev-title">Executive Roundtable</div>
          <div class="ev-meta"><span class="badge badge-red">DECLINED</span> Hosted by John Madigan · Zoom: us02web.zoom.us/j/207786667 · PW: 205454</div>
          <div class="ev-meta">No prep needed — already declined.</div>
        </div>
      </div>

      <div class="cal-event needs-action">
        <div class="cal-time">12:00–1:00 PM</div>
        <div class="cal-detail">
          <div class="ev-title">HR Networking & Job Search: Open Office Hours – Zoom 2</div>
          <div class="ev-meta"><span class="badge badge-yellow">RSVP NEEDED</span> ~195 attendees · Zoom: us06web.zoom.us/j/85945371140 · No AI notetaking allowed</div>
          <div class="ev-meta">⚠️ <strong>Action needed:</strong> Accept or decline before noon. Valuable for active job search.</div>
          <div class="conflict-warn">⚡ RSVP PENDING — Respond now</div>
        </div>
      </div>

      <div class="cal-event confirmed">
        <div class="cal-time">3:30–4:30 PM</div>
        <div class="cal-detail">
          <div class="ev-title">New Patient Appointment – Dr. Beth A. Leeman-Markowski, MD</div>
          <div class="ev-meta"><span class="badge badge-green">CONFIRMED</span> Comprehensive Epilepsy Center · 223 East 34th Street, New York, NY 10016 · 📞 646-558-0800</div>
          <div class="ev-meta"><strong>Prep:</strong> Arrive by 3:15 PM. Bring insurance card, photo ID, medical records, recent labs/imaging. Bring referral/pre-certification if applicable.</div>
        </div>
      </div>

    </div>

    <!-- FRIDAY JULY 10 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Friday, July 10, 2026 — TOMORROW</div>

      <div class="cal-event confirmed">
        <div class="cal-time">2:00–2:25 PM</div>
        <div class="cal-detail">
          <div class="ev-title">📞 Oscar Health Phone Screen – People Strategy Lead</div>
          <div class="ev-meta"><span class="badge badge-green">ACCEPTED</span> With Joelle Molina (joelle@hioscar.com) · They will call: <strong>516-313-8888</strong> · Phone or Google Meet</div>
          <div class="ev-meta"><strong>Prep:</strong> Research Oscar Health's People & HR strategy. Prepare your leadership narrative. Confirm phone availability. Review job description for People Strategy Lead. Do NOT miss this call.</div>
        </div>
      </div>

      <div class="cal-event confirmed">
        <div class="cal-time">3:30–4:30 PM</div>
        <div class="cal-detail">
          <div class="ev-title">Dr. (Appointment – Details TBD)</div>
          <div class="ev-meta"><span class="badge badge-green">CONFIRMED</span> Location not listed · No additional details in description</div>
          <div class="ev-meta"><strong>Prep:</strong> Verify appointment details and location. Could conflict with Oscar phone screen if it runs long — monitor timing.</div>
          <div class="conflict-warn">⚡ Potential timing conflict if Oscar call runs long — keep buffer</div>
        </div>
      </div>

      <div class="cal-event blue-card" style="border-left: 4px solid #2471a3; background: #eaf4fb; margin-bottom:7px;">
        <div class="cal-time">All Day (prep)</div>
        <div class="cal-detail">
          <div class="ev-title">🏥 Northwell Visit – Dr. Crystal Lee, MD</div>
          <div class="ev-meta"><span class="badge badge-blue">REMINDER</span> 178 East 85th Street, 2nd Floor, New York NY · 3:30 PM (confirmed via email)</div>
          <div class="ev-meta"><strong>Note:</strong> MyNorthwell sent prep email today. Confirm paperwork and bring required docs.</div>
        </div>
      </div>

    </div>

    <!-- MONDAY JULY 13 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Monday, July 13, 2026</div>
      <div class="cal-event all-day">
        <div class="cal-time">All Day</div>
        <div class="cal-detail">
          <div class="ev-title">Stephanie Infusion</div>
          <div class="ev-meta"><span class="badge badge-purple">CONFIRMED</span> All-day marker (July 13–14) · No location listed</div>
          <div class="ev-meta"><strong>Prep:</strong> Personal/family commitment. Keep calendar clear for support if needed.</div>
        </div>
      </div>
    </div>

    <!-- TUESDAY JULY 14 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Tuesday, July 14, 2026</div>
      <div class="cal-event all-day">
        <div class="cal-time">All Day</div>
        <div class="cal-detail">
          <div class="ev-title">Stephanie Infusion (cont.)</div>
          <div class="ev-meta"><span class="badge badge-purple">CONFIRMED</span> Continues from July 13 · All-day marker</div>
        </div>
      </div>
      <div class="cal-event confirmed">
        <div class="cal-time">10:00–11:00 AM</div>
        <div class="cal-detail">
          <div class="ev-title">Stella</div>
          <div class="ev-meta"><span class="badge badge-green">CONFIRMED</span> No location listed · Personal/professional appointment</div>
          <div class="ev-meta"><strong>Prep:</strong> Add location/details if needed. Confirm if this is virtual or in-person.</div>
        </div>
      </div>
    </div>

    <!-- WEDNESDAY JULY 15 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Wednesday, July 15, 2026</div>

      <div class="cal-event confirmed">
        <div class="cal-time">8:30–9:30 AM</div>
        <div class="cal-detail">
          <div class="ev-title">Bone Density Scan</div>
          <div class="ev-meta"><span class="badge badge-green">CONFIRMED</span> No location listed · Medical appointment</div>
          <div class="ev-meta"><strong>Prep:</strong> Confirm location and any prep instructions (no calcium supplements 24 hrs before, etc.). Add address to calendar.</div>
        </div>
      </div>

      <div class="cal-event needs-action">
        <div class="cal-time">12:00–1:30 PM</div>
        <div class="cal-detail">
          <div class="ev-title">HR Networking & Job Search Group – Zoom 2</div>
          <div class="ev-meta"><span class="badge badge-yellow">RSVP NEEDED</span> ~195 attendees · Zoom: us06web.zoom.us/j/81954171722 · 1.5 hours</div>
          <div class="ev-meta"><strong>Prep:</strong> Respond to RSVP. Prepare your 30-second intro if attending.</div>
          <div class="conflict-warn">⚡ RSVP PENDING — Respond before the event</div>
        </div>
      </div>

      <div class="cal-event confirmed">
        <div class="cal-time">12:00–1:30 PM</div>
        <div class="cal-detail">
          <div class="ev-title">Network (personal reminder)</div>
          <div class="ev-meta"><span class="badge badge-green">CONFIRMED</span> No location · Personal networking block — overlaps with HR Networking Zoom</div>
          <div class="ev-meta"><strong>Note:</strong> Appears to be a personal note/reminder that overlaps with the HR Networking session above.</div>
        </div>
      </div>

    </div>

  </div>
</div>

<!-- ===== JOB SEARCH & INTERVIEW PIPELINE ===== -->
<div class="section-wrap">
  <div class="section-title green-head">💼 Job Search & Interview Pipeline</div>
  <div class="section-body">
    <table>
      <thead>
        <tr>
          <th>Priority</th>
          <th>Role / Opportunity</th>
          <th>Company</th>
          <th>Source</th>
          <th>Status</th>
          <th>Next Step</th>
          <th>Fit</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="priority-high">HIGH</td>
          <td><strong>People Strategy Lead</strong></td>
          <td>Oscar Health</td>
          <td>LinkedIn Job Alert + Calendar (Phone Screen Tomorrow)</td>
          <td><span class="badge badge-green">Phone Screen Jul 10, 2:00 PM</span></td>
          <td>Prep tonight. They call 516-313-8888. Contact: Joelle Molina (joelle@hioscar.com)</td>
          <td class="fit-high">HIGH</td>
        </tr>
        <tr>
          <td class="priority-high">HIGH</td>
          <td><strong>HR Business Opportunity</strong></td>
          <td>RWJBarnabas Health Corporate Services</td>
          <td>LinkedIn InMail from Ayesha Sadiqua</td>
          <td><span class="badge badge-yellow">Unread / Unresponded</span></td>
          <td>Read full InMail on LinkedIn. Respond today with interest/availability.</td>
          <td class="fit-high">HIGH</td>
        </tr>
        <tr>
          <td class="priority-med">MED</td>
          <td><strong>Outsourced HR Business Partner – New York</strong></td>
          <td>Unknown (via LinkedIn)</td>
          <td>LinkedIn message from Muhammad Hanzla (replied "sure")</td>
          <td><span class="badge badge-yellow">Thread Active – Follow Up</span></td>
          <td>Review full LinkedIn thread. Send next steps or availability for call.</td>
          <td class="fit-med">MED</td>
        </tr>
        <tr>
          <td class="priority-med">MED</td>
          <td><strong>HR Networking Open Office Hours</strong></td>
          <td>HR Job Search Group</td>
          <td>Google Calendar (RSVP Pending – Today 12–1 PM)</td>
          <td><span class="badge badge-yellow">RSVP Needed</span></td>
          <td>Accept/decline before noon. Valuable networking touchpoint during active search.</td>
          <td class="fit-med">MED</td>
        </tr>
        <tr>
          <td class="priority-med">MED</td>
          <td><strong>HR Networking Group – Zoom Session</strong></td>
          <td>HR Networking Group</td>
          <td>Google Calendar (July 15, 12–1:30 PM, RSVP Pending)</td>
          <td><span class="badge badge-yellow">RSVP Needed</span></td>
          <td>Respond to calendar invite. Good ongoing networking touch.</td>
          <td class="fit-med">MED</td>
        </tr>
        <tr>
          <td class="priority-low">LOW</td>
          <td><strong>Paid UserTesting Study – $125</strong></td>
          <td>UserTesting</td>
          <td>Email from Remi at UserTesting</td>
          <td><span class="badge badge-blue">Application Open</span></td>
          <td>Review requirements and apply if schedule permits. Easy supplemental income.</td>
          <td class="fit-low">LOW (side income)</td>
        </tr>
      </tbody>
    </table>

    <hr class="divider">
    <div style="margin-top:10px;">
      <strong>📰 Job Alerts Received Today:</strong>
      <ul style="margin-top:6px; padding-left:18px; font-size:0.85rem;">
        <li><strong>People Strategy Lead at Oscar Health</strong> — LinkedIn Job Alert (posted 7/7/2026) · Already have phone screen scheduled ✅</li>
        <li><strong>#193 – How AI Changed Resume Writing</strong> (Adam Karpiak via LinkedIn) — Newsletter on resume/AI trends. Useful context for current job search.</li>
      </ul>
    </div>
  </div>
</div>

<!-- ===== FULL EMAIL REVIEW BY CATEGORY ===== -->
<div class="section-wrap">
  <div class="section-title navy-head">📬 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="red-card">
      <div class="card-title">🚨 Security / Risk — 4 Emails</div>
      <div class="card-body">
        <table>
          <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
          <tbody>
            <tr><td>"Cloud.Security" (fake domain)</td><td>FINAL NOTICE: Your photos will be deleted tonight</td><td><span class="badge badge-red">PHISHING</span></td><td>Mark as phishing, delete</td></tr>
            <tr><td>"Payment_Declined" (fake domain)</td><td>Your Account Has Been Blocked! Photos Removed Thu 09 Jul</td><td><span class="badge badge-red">PHISHING</span></td><td>Mark as phishing, delete</td></tr>
            <tr><td>"Wild_Online" (random domain)</td><td>Congratulations! 250 Welcome Free Spins 🔥</td><td><span class="badge badge-red">SPAM/SCAM</span></td><td>Delete, mark as spam</td></tr>
            <tr><td>"Congratulations 🎉" (fake casino)</td><td>130 Free Spins – No Deposit Needed!</td><td><span class="badge badge-red">SPAM/SCAM</span></td><td>Delete, mark as spam</td></tr>
          </tbody>
        </table>
        <div class="note">All 4 are phishing or casino spam. Do not click any links. Mark as phishing in Gmail for improved filtering.</div>
      </div>
    </div>

    <!-- JOB SEARCH -->
    <div class="green-card">
      <div class="card-title">💼 Job Search — 3 Emails</div>
      <div class="card-body">
        <table>
          <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
          <tbody>
            <tr><td>LinkedIn Job Alerts</td><td>People Strategy Lead at Oscar Health</td><td>Already have phone screen scheduled — review job description tonight</td></tr>
            <tr><td>Muhammad Hanzla (LinkedIn)</td><td>Message Replied: Career Opportunity – Outsourced HR Business Partner | NY</td><td>Follow up on LinkedIn thread today</td></tr>
            <tr><td>Adam Karpiak via LinkedIn</td><td>#193 – How AI Changed Resume Writing</td><td>Read for context on AI-era resume trends</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- RECRUITERS / NETWORKING -->
    <div class="green-card">
      <div class="card-title">🤝 Recruiters / Networking — 1 Email</div>
      <div class="card-body">
        <table>
          <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
          <tbody>
            <tr><td>Ayesha Sadiqua via LinkedIn</td><td>HR Business Opportunity at RWJBarnabas Health Corporate Services</td><td>Read full InMail and respond today — high-value inbound recruiter contact</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- CALENDAR / EVENTS -->
    <div class="blue-card">
      <div class="card-title">📅 Calendar / Events — 2 Emails</div>
      <div class="card-body">
        <table>
          <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
          <tbody>
            <tr><td>MyNorthwell</td><td>Get ready for your visit on 7/10 – Dr. Crystal Lee, MD, 178 E 85th St</td><td>Confirm visit, bring docs, check insurance</td></tr>
            <tr><td>New York Events (Nextdoor)</td><td>Weekend events you'll love – 5 events</td><td>Review if you want local NYC weekend activity ideas</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- MEDICAL / HEALTH -->
    <div class="blue-card">
      <div class="card-title">🏥 Medical / Health — 1 Email</div>
      <div class="card-body">
        <table>
          <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
          <tbody>
            <tr><td>HomeAgain PetRescuers</td><td>Lecter, a lost Cat, is missing in your area (Brooklyn, Throop Ave) – Ref. HAP-1890967</td><td>Share with neighbors/community if near Brooklyn — optional</td></tr>
          </tbody>
        </table>
        <div class="note">Note: Classified under community/personal care. Not a medical email for Melissa directly.</div>
      </div>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="yellow-card">
      <div class="card-title">💳 Financial / Billing — 3 Emails</div>
      <div class="card-body">
        <table>
          <thead><tr><th>Sender</th><th>Subject</th><th>Due Date</th><th>Action</th></tr></thead>
          <tbody>
            <tr><td>Conservice</td><td>Monthly Utility Statement for 303 East 83rd – Account ending 3876</td><td>8/1/2026</td><td>Review statement and schedule payment</td></tr>
            <tr><td>Apify</td><td>Platform usage at 50% of $69.00 monthly plan</td><td>Ongoing</td><td>Log in and review usage — pause non-essential actors</td></tr>
            <tr><td>CVS ExtraCare</td><td>$5 Coupon!</td><td>Check expiry</td><td>Use at next CVS visit or ignore</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="purple-card">
      <div class="card-title">📚 Professional Development — 5 Emails</div>
      <div class="card-body">
        <table>
          <thead><tr><th>Sender</th><th>Subject</th><th>Recommendation</th></tr></thead>
          <tbody>
            <tr><td>The CHRO Office (Substack)</td><td>Install CHRO Claude Skill – Build HR Dashboards in 10 Minutes</td><td>Read — directly relevant to HR + AI work</td></tr>
            <tr><td>Christopher Rainey via LinkedIn</td><td>How to Build a Human-First AI Strategy That Actually Works</td><td>Review — relevant to HR leadership strategy</td></tr>
            <tr><td>Stanton Chase via LinkedIn</td><td>What Makes Family Business Succession Work</td><td>Skim — useful for HR leadership context</td></tr>
            <tr><td>BambooHR</td><td>500 HR Pros Shared Their Hiring Secrets (Talent Acquisition Guide)</td><td>Download guide — relevant to HR role interviews</td></tr>
            <tr><td>The People People Group</td><td>TPPG Digest – Exit Interviews, Engagement, Milestone Rewards (in Trash)</td><td>Restore if you want — relevant HR community digest</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- PERSONAL -->
    <div class="teal-card">
      <div class="card-title">👤 Personal — 4 Emails</div>
      <div class="card-body">
        <table>
          <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
          <tbody>
            <tr><td>Match (x3)</td><td>Kevin likes you · Michael likes you · Jeff likes you</td><td>Check Match.com when you have time — 3 new likes</td></tr>
            <tr><td>UserTesting (Remi)</td><td>Invited to First Paid Study – Earn $125</td><td>Apply if schedule allows — easy side income</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- NEWSLETTERS / SUBSCRIPTIONS -->
    <div class="purple-card">
      <div class="card-title">📰 Newsletters / Subscriptions — 7 Emails</div>
      <div class="card-body">
        <table>
          <thead><tr><th>Sender</th><th>Subject / Topic</th><th>Recommendation</th></tr></thead>
          <tbody>
            <tr><td>The AI Report</td><td>Grok 4.5 drops, Meta $9B Canadian data center (in Trash)</td><td>Skim in trash or restore if AI news matters</td></tr>
            <tr><td>TLDR</td><td>GPT-Live, Grok matches Opus, Bun rewrite</td><td>Keep — useful AI/tech digest</td></tr>
            <tr><td>The Hustle</td><td>The new country club / iPhone infertility</td><td>Read for entertainment/business culture</td></tr>
            <tr><td>The Average Joe</td><td>The defense boom / Media giants chase World Cup rights</td><td>Skim for business/market context</td></tr>
            <tr><td>Medium Daily Digest (x2)</td><td>Claude usage limits + CLAUDE.md file went viral</td><td>Read if interested in AI tool optimization</td></tr>
            <tr><td>AI For Leaders</td><td>AI Leaves Companies With Three Roles (in Trash)</td><td>Restore/review — relevant to HR leadership</td></tr>
            <tr><td>USPS Informed Delivery</td><td>Daily Digest Thu 7/9 – 1 mailpiece, 1 package arriving</td><td>Note: 1 mail item + 1 inbound package on the way</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- PROMOTIONAL / RETAIL -->
    <div class="gray-card">
      <div class="card-title">🛍️ Promotional / Retail — 10 Emails</div>
      <div class="card-body">
        <p style="font-size:0.83rem;">Temu (x3: 2 out-for-delivery + 1 arriving soon), Halara (BOGO VIP Deal), Zappos (walking shoes), SHEIN (27% off cart), Kohl's (30% Cardholder Event), Lands' End (up to 70% off), 22 Words (Amazon Lightning Deals Jul 9), JetBlue Vacations (up to $500 off — in Trash).<br>
        <strong>Recommendation:</strong> Temu deliveries are real/actionable (see Action Required). All others are promotional noise — review Kohl's if cardholder event is expiring, delete/ignore the rest.</p>
      </div>
    </div>

    <!-- SYSTEM / AUTOMATION -->
    <div class="blue-card">
      <div class="card-title">⚙️ System / Automation — 3 Emails</div>
      <div class="card-body">
        <table>
          <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
          <tbody>
            <tr><td>no-reply-claude@anthropic.com (x2)</td><td>Daily briefing dispatch FAILED – GitHub action not running</td><td>Manually trigger: github.com/missophs/daily-briefing → Actions → Run workflow → branch: webhooks</td></tr>
            <tr><td>Etsy Conversations</td><td>41 unread Etsy messages waiting</td><td>Check Etsy inbox if you have an active shop/orders</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- MISC / SAFE TO IGNORE -->
    <div class="gray-card">
      <div class="card-title">🗑️ Safe to Delete / Ignore — 7 Emails</div>
      <div class="card-body">
        <table>
          <thead><tr><th>Sender</th><th>Subject</th><th>Reason</th></tr></thead>
          <tbody>
            <tr><td>Lisa Rangel (Chameleon Resumes) – in Trash</td><td>"one small favor to ask you today"</td><td>Marketing email asking you to forward. Delete.</td></tr>
            <tr><td>1% Better – in Trash</td><td>Fake Airbags, Powerful Cells, Breaking Out of Survival Mode</td><td>Generic self-improvement newsletter. Delete.</td></tr>
            <tr><td>CoolDeep AI – in Trash</td><td>The AI system that took me from burritos to $3M</td><td>Clickbait marketing. Delete.</td></tr>
            <tr><td>The Daily Skimm – in Trash</td><td>"Really really really wanna"</td><td>General news digest. Already in trash. Delete.</td></tr>
            <tr><td>Gemma Bonham-Carter – in Trash</td><td>"made you a video 👀" (sales close)</td><td>Sales/marketing email. Delete.</td></tr>
            <tr><td>Ziemek from Hunter</td><td>Plan your next quarter of emails (Hunter.io newsletter)</td><td>Email outreach tool marketing. Unsubscribe or delete.</td></tr>
            <tr><td>Medium Daily Digest – in Trash</td><td>How to Never Hit Claude's Usage Limit Again</td><td>Interesting but already in trash. Restore only if needed.</td></tr>
          </tbody>
        </table>
      </div>
    </div>

  </div>
</div>

<!-- ===== TRASH REVIEW ===== -->
<div class="section-wrap">
  <div class="section-title red-head">🗑️ Trash Review</div>
  <div class="section-body">
    <p style="font-size:0.85rem; margin-bottom:14px;">The following <strong>9 emails</strong> were found in Gmail Trash. Review before permanent deletion.</p>

    <div style="margin-bottom:14px;">
      <div style="font-weight:700; font-size:0.93rem; margin-bottom:8px;"><span class="restore-tag">RESTORE</span> Consider Restoring</div>
      <table>
        <thead><tr><th>Sender</th><th>Subject</th><th>Why Restore</th></tr></thead>
        <tbody>
          <tr><td>The People People Group</td><td>TPPG Digest – Rethinking Exit Interviews and Engagement + 8 more topics</td><td>Active HR community digest. Relevant to your HR professional network and job search prep.</td></tr>
          <tr><td>AI For Leaders</td><td>AI Leaves Companies With Three Roles</td><td>Directly relevant to HR leadership + AI strategy thinking. Useful for interview prep.</td></tr>
          <tr><td>Medium Daily Digest</td><td>How to Never Hit Claude's Usage Limit Again</td><td>Practical Claude AI tips. Relevant given your daily briefing automation work.</td></tr>
        </tbody>
      </table>
    </div>

    <div style="margin-bottom:14px;">
      <div style="font-weight:700; font-size:0.93rem; margin-bottom:8px;"><span class="review-tag">REVIEW</span> Review Before Deleting</div>
      <table>
        <thead><tr><th>Sender</th><th>Subject</th><th>Note</th></tr></thead>
        <tbody>
          <tr><td>JetBlue Vacations</td><td>Up to $500 off — Seas the deal 🌊</td><td>If you're considering summer travel to Bermuda, review before it expires. Otherwise delete.</td></tr>
          <tr><td>The AI Report</td><td>⚡ SpaceXAI drops Grok 4.5</td><td>AI news digest. Skim headlines if you track AI developments. Otherwise safe to delete.</td></tr>
        </tbody>
      </table>
    </div>

    <div>
      <div style="font-weight:700; font-size:0.93rem; margin-bottom:8px;"><span class="delete-tag">DELETE</span> Safe To Delete Permanently</div>
      <table>
        <thead><tr><th>Sender</th><th>Subject</th><th>Reason</th></tr></thead>
        <tbody>
          <tr><td>Lisa Rangel (Chameleon Resumes)</td><td>"one small favor to ask you today"</td><td>Marketing/referral ask. No action needed.</td></tr>
          <tr><td>1% Better Newsletter</td><td>Fake Airbags, Powerful Cells, Breaking Out of Survival Mode</td><td>Generic self-improvement content. Low relevance.</td></tr>
          <tr><td>CoolDeep AI</td><td>The AI system that took me from burritos to $3M</td><td>Clickbait marketing email. Delete permanently.</td></tr>
          <tr><td>The Daily Skimm</td><td>"Really really really wanna"</td><td>General pop news digest. Already trashed — delete.</td></tr>
          <tr><td>Gemma Bonham-Carter</td><td>"made you a video 👀"</td><td>Sales closing email for online course/product. Delete.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="note" style="margin-top:10px;">Total Trash emails reviewed: 9 (3 restore candidates, 2 review, 5 safe to delete permanently)</div>
  </div>
</div>

<!-- ===== PROMOTIONAL / RETAIL SUMMARY ===== -->
<div class="section-wrap">
  <div class="section-title gray-head">🛍️ Promotional / Retail Summary</div>
  <div class="section-body">
    <table>
      <thead>
        <tr>
          <th>Brand / Sender</th>
          <th>Count</th>
          <th>Subject / Offer</th>
          <th>In Trash?</th>
          <th>Recommendation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Temu</strong></td>
          <td>3</td>
          <td>2× Out for Delivery (#PO-211-13384130622071025, #PO-211-13384128686711025) + 1 "Arriving Soon"</td>
          <td>No</td>
          <td><span class="badge badge-green">ACTION</span> Be home for delivery today. Track packages.</td>
        </tr>
        <tr>
          <td><strong>Match.com</strong></td>
          <td>3</td>
          <td>Kevin, Michael, and Jeff each liked you. "See if it's mutual."</td>
          <td>No</td>
          <td><span class="badge badge-blue">REVIEW</span> Check Match.com when you have downtime.</td>
        </tr>
        <tr>
          <td><strong>Kohl's</strong></td>
          <td>1</td>
          <td>Save 30% during Exclusive Cardholder Event — new summer styles</td>
          <td>No</td>
          <td><span class="badge badge-yellow">REVIEW</span> Check event expiration date. Use if you need items.</td>
        </tr>
        <tr>
          <td><strong>Halara</strong></td>
          <td>1</td>
          <td>VIP Deal: Buy One, Get One Free (not in inbox)</td>
          <td>No</td>
          <td><span class="badge badge-gray">IGNORE</span> Only if interested in athleisure clothing.</td>
        </tr>
        <tr>
          <td><strong>Zappos</strong></td>
          <td>1</td>
          <td>"Your walking era starts now 🚶" — shoes to close exercise ring</td>
          <td>No</td>
          <td><span class="badge badge-gray">IGNORE</span> Browse only if in market for walking shoes.</td>
        </tr>
        <tr>
          <td><strong>SHEIN</strong></td>
          <td>1</td>
          <td>27% OFF — Your Cart Awaits</td>
          <td>No</td>
          <td><span class="badge badge-gray">IGNORE</span> Only if you have items in your cart.</td>
        </tr>
        <tr>
          <td><strong>Lands' End</strong></td>
          <td>1</td>
          <td>New markdowns! Up to 70% off sale & clearance + 50% off order + 55% off swim</td>
          <td>No</td>
          <td><span class="badge badge-gray">REVIEW</span> Strong discount — browse if you need summer/swim items.</td>
        </tr>
        <tr>
          <td><strong>22 Words</strong></td>
          <td>1</td>
          <td>Amazon Lightning Deals ⚡ Jul 9 — Steel Garage Hooks, Air Fryer Liners, Padded
