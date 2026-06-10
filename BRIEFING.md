<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Melissa's Executive Daily Briefing — June 10, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; line-height: 1.5; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px 48px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px 28px; margin-bottom: 24px; }
  .header h1 { font-size: 26px; font-weight: 700; letter-spacing: 0.5px; }
  .header .sub { font-size: 13px; color: #aac4ff; margin-top: 4px; }
  .header .meta-row { display: flex; gap: 28px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-pill { background: rgba(255,255,255,0.12); border-radius: 8px; padding: 8px 18px; text-align: center; }
  .header .meta-pill .num { font-size: 22px; font-weight: 700; color: #7dd3fc; }
  .header .meta-pill .lbl { font-size: 11px; color: #cbd5e1; text-transform: uppercase; letter-spacing: 0.5px; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 15px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; padding: 10px 16px; border-radius: 8px 8px 0 0; display: flex; align-items: center; gap: 8px; }
  .section-body { background: #fff; border-radius: 0 0 10px 10px; padding: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }

  /* COLOR THEMES */
  .red-title { background: #fee2e2; color: #b91c1c; border-left: 4px solid #dc2626; }
  .yellow-title { background: #fef9c3; color: #854d0e; border-left: 4px solid #ca8a04; }
  .blue-title { background: #dbeafe; color: #1e40af; border-left: 4px solid #2563eb; }
  .green-title { background: #dcfce7; color: #166534; border-left: 4px solid #16a34a; }
  .purple-title { background: #ede9fe; color: #5b21b6; border-left: 4px solid #7c3aed; }
  .gray-title { background: #f1f5f9; color: #475569; border-left: 4px solid #94a3b8; }
  .orange-title { background: #ffedd5; color: #9a3412; border-left: 4px solid #ea580c; }
  .teal-title { background: #ccfbf1; color: #065f46; border-left: 4px solid #0d9488; }

  /* EXECUTIVE SUMMARY */
  .exec-bullets { list-style: none; padding: 0; }
  .exec-bullets li { padding: 10px 14px; margin-bottom: 8px; border-radius: 8px; font-size: 14px; display: flex; align-items: flex-start; gap: 10px; }
  .exec-bullets li .icon { font-size: 18px; flex-shrink: 0; margin-top: 1px; }
  .bullet-red { background: #fff1f1; border-left: 4px solid #dc2626; }
  .bullet-green { background: #f0fdf4; border-left: 4px solid #16a34a; }
  .bullet-blue { background: #eff6ff; border-left: 4px solid #2563eb; }

  /* ACTION CARDS */
  .action-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 14px; }
  .action-card { border-radius: 10px; padding: 14px 16px; border-left: 5px solid; }
  .ac-red { background: #fff1f1; border-color: #dc2626; }
  .ac-yellow { background: #fefce8; border-color: #ca8a04; }
  .ac-green { background: #f0fdf4; border-color: #16a34a; }
  .ac-blue { background: #eff6ff; border-color: #2563eb; }
  .ac-purple { background: #faf5ff; border-color: #7c3aed; }
  .action-card .label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; opacity: 0.7; }
  .action-card .title { font-size: 14px; font-weight: 700; margin-bottom: 6px; }
  .action-card .source { font-size: 11px; color: #64748b; margin-bottom: 6px; }
  .action-card .why { font-size: 13px; margin-bottom: 6px; }
  .action-card .step { font-size: 12px; background: rgba(0,0,0,0.05); border-radius: 5px; padding: 5px 8px; margin-bottom: 4px; }
  .action-card .due { font-size: 11px; font-weight: 700; color: #b91c1c; margin-top: 4px; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { font-size: 13px; font-weight: 700; color: #1e40af; background: #dbeafe; border-radius: 6px; padding: 5px 12px; margin-bottom: 8px; display: inline-block; }
  .cal-event { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px 14px; margin-bottom: 8px; display: grid; grid-template-columns: 120px 1fr; gap: 8px; }
  .cal-event .cal-time { font-weight: 700; font-size: 13px; color: #1e40af; }
  .cal-event .cal-name { font-weight: 700; font-size: 13px; }
  .cal-event .cal-meta { font-size: 12px; color: #64748b; margin-top: 2px; }
  .cal-event .cal-status { display: inline-block; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 10px; text-transform: uppercase; letter-spacing: 0.5px; }
  .status-confirmed { background: #dcfce7; color: #166534; }
  .status-accepted { background: #dbeafe; color: #1e40af; }
  .status-declined { background: #fee2e2; color: #b91c1c; }
  .status-pending { background: #fef9c3; color: #854d0e; }
  .cal-conflict { font-size: 11px; background: #fee2e2; color: #b91c1c; border-radius: 4px; padding: 2px 7px; font-weight: 700; display: inline-block; margin-top: 3px; }
  .cal-prep { font-size: 11px; background: #fef9c3; color: #854d0e; border-radius: 4px; padding: 2px 7px; display: inline-block; margin-top: 3px; }

  /* JOB SEARCH */
  .job-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 12px; }
  .job-card { background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 9px; padding: 12px 14px; }
  .job-card .jc-role { font-weight: 700; font-size: 13px; }
  .job-card .jc-company { font-size: 12px; color: #166534; }
  .job-card .jc-salary { font-size: 11px; color: #64748b; margin: 2px 0; }
  .badge { display: inline-block; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 10px; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px; }
  .badge-high { background: #16a34a; color: #fff; }
  .badge-medium { background: #ca8a04; color: #fff; }
  .badge-low { background: #94a3b8; color: #fff; }
  .badge-alert { background: #dc2626; color: #fff; }

  /* EMAIL REVIEW TABLE */
  table.email-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  table.email-table th { background: #f1f5f9; text-align: left; padding: 8px 10px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: #475569; border-bottom: 2px solid #e2e8f0; }
  table.email-table td { padding: 8px 10px; border-bottom: 1px solid #f1f5f9; vertical-align: top; }
  table.email-table tr:last-child td { border-bottom: none; }
  table.email-table tr:hover td { background: #f8fafc; }

  /* ACCOUNTING TABLE */
  .accounting-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .accounting-table th { background: #1e293b; color: #f8fafc; text-align: left; padding: 9px 12px; font-size: 12px; }
  .accounting-table td { padding: 8px 12px; border-bottom: 1px solid #e2e8f0; }
  .accounting-table tr:nth-child(even) td { background: #f8fafc; }
  .accounting-table .total-row td { background: #1e293b; color: #7dd3fc; font-weight: 700; }

  /* DASHBOARD */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }
  .dash-card { border-radius: 10px; padding: 14px 16px; text-align: center; }
  .dc-red { background: #fee2e2; border: 1px solid #fca5a5; }
  .dc-green { background: #dcfce7; border: 1px solid #86efac; }
  .dc-blue { background: #dbeafe; border: 1px solid #93c5fd; }
  .dc-yellow { background: #fef9c3; border: 1px solid #fde047; }
  .dc-purple { background: #ede9fe; border: 1px solid #c4b5fd; }
  .dc-gray { background: #f1f5f9; border: 1px solid #cbd5e1; }
  .dash-card .dc-num { font-size: 30px; font-weight: 700; }
  .dash-card .dc-label { font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 2px; opacity: 0.8; }
  .dash-card .dc-detail { font-size: 11px; margin-top: 6px; opacity: 0.7; }

  /* TRASH */
  .trash-group { margin-bottom: 14px; }
  .trash-group-title { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px; padding: 4px 10px; border-radius: 4px; display: inline-block; }
  .tg-restore { background: #fee2e2; color: #b91c1c; }
  .tg-review { background: #fef9c3; color: #854d0e; }
  .tg-delete { background: #f1f5f9; color: #475569; }
  .trash-item { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 7px 12px; margin-bottom: 5px; font-size: 12px; }
  .trash-item .t-sender { font-weight: 700; }
  .trash-item .t-reason { color: #64748b; font-style: italic; }

  /* PROMO */
  .promo-row { display: flex; flex-wrap: wrap; gap: 10px; }
  .promo-card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px 14px; min-width: 200px; flex: 1; }
  .promo-card .p-brand { font-weight: 700; font-size: 13px; }
  .promo-card .p-sub { font-size: 12px; color: #64748b; }
  .promo-card .p-rec { font-size: 11px; font-weight: 700; margin-top: 5px; border-radius: 4px; padding: 2px 7px; display: inline-block; }
  .rec-delete { background: #fee2e2; color: #b91c1c; }
  .rec-ignore { background: #f1f5f9; color: #475569; }
  .rec-review { background: #fef9c3; color: #854d0e; }
  .rec-keep { background: #dcfce7; color: #166534; }

  /* PRIORITIES */
  .priority-card { display: flex; gap: 14px; align-items: flex-start; background: #fff; border-radius: 10px; padding: 14px 18px; margin-bottom: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); border-left: 5px solid; }
  .p1 { border-color: #dc2626; }
  .p2 { border-color: #16a34a; }
  .p3 { border-color: #2563eb; }
  .priority-num { font-size: 28px; font-weight: 700; opacity: 0.2; flex-shrink: 0; }
  .priority-content .p-title { font-weight: 700; font-size: 14px; }
  .priority-content .p-desc { font-size: 13px; color: #475569; margin-top: 3px; }

  /* ACTION ITEMS TABLE */
  .ai-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .ai-table th { background: #1e293b; color: #f8fafc; text-align: left; padding: 9px 12px; font-size: 11px; text-transform: uppercase; }
  .ai-table td { padding: 8px 12px; border-bottom: 1px solid #e2e8f0; }
  .ai-table tr:nth-child(even) td { background: #f8fafc; }
  .pri-high { color: #dc2626; font-weight: 700; }
  .pri-med { color: #ca8a04; font-weight: 700; }
  .pri-low { color: #64748b; font-weight: 700; }

  /* CAT BADGE */
  .cat-badge { display: inline-block; font-size: 10px; padding: 2px 7px; border-radius: 10px; font-weight: 700; }
  .cat-red { background: #fee2e2; color: #b91c1c; }
  .cat-yellow { background: #fef9c3; color: #854d0e; }
  .cat-blue { background: #dbeafe; color: #1e40af; }
  .cat-green { background: #dcfce7; color: #166534; }
  .cat-purple { background: #ede9fe; color: #5b21b6; }
  .cat-gray { background: #f1f5f9; color: #475569; }

  /* EMAIL CATEGORY ROW */
  .email-cat-section { margin-bottom: 16px; }
  .email-cat-header { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; padding: 5px 12px; border-radius: 5px; margin-bottom: 6px; display: flex; justify-content: space-between; align-items: center; }
  .email-item { padding: 6px 12px; border-bottom: 1px solid #f1f5f9; font-size: 12px; display: flex; gap: 8px; align-items: flex-start; }
  .email-item .ei-from { font-weight: 700; min-width: 160px; flex-shrink: 0; }
  .email-item .ei-sub { color: #374151; flex: 1; }
  .email-item .ei-tag { flex-shrink: 0; }
  .unread-dot { display: inline-block; width: 7px; height: 7px; background: #2563eb; border-radius: 50%; margin-right: 4px; flex-shrink: 0; margin-top: 4px; }

  hr.divider { border: none; border-top: 2px solid #e2e8f0; margin: 28px 0; }

  .note-box { background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 10px 14px; font-size: 12px; color: #1e40af; margin-top: 8px; }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ══════════════════════════════════════════════════════════ -->
<!-- 1. HEADER -->
<!-- ══════════════════════════════════════════════════════════ -->
<div class="header">
  <div class="sub">☀️ EXECUTIVE DAILY BRIEFING &nbsp;·&nbsp; Prepared by Your Chief of Staff</div>
  <h1>Good Morning, Melissa 👋</h1>
  <div class="meta-row">
    <div class="meta-pill"><div class="num">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="meta-pill"><div class="num">9</div><div class="lbl">Calendar Events</div></div>
    <div class="meta-pill"><div class="num">Wed</div><div class="lbl">June 10, 2026</div></div>
    <div class="meta-pill"><div class="num">3</div><div class="lbl">Action Items Today</div></div>
    <div class="meta-pill"><div class="num">2</div><div class="lbl">Meetings Today</div></div>
  </div>
</div>

<!-- ══════════════════════════════════════════════════════════ -->
<!-- 2. EXECUTIVE SUMMARY -->
<!-- ══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title red-title">🔍 Executive Summary</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li class="bullet-red">
        <span class="icon">🚨</span>
        <span><strong>Biggest Risk:</strong> Multiple phishing/scam emails reached your inbox and non-trash folders — including a fake Lowe's prize winner email, a spoofed "LOWER'S®" tool giveaway, and a suspicious "FINAL NOTICE CASE#8585538" email. Your GitHub Actions daily briefing workflow also had two consecutive run failures this morning (d723d8b and 61e8609), which may mean your automated briefing pipeline is broken and needs debugging today.</span>
      </li>
      <li class="bullet-green">
        <span class="icon">💼</span>
        <span><strong>Biggest Opportunity:</strong> Two strong C-suite job alerts landed today — a CHRO role at Empathy Talent ($250K–$300K, Private Equity/Financial Services focus) and a Chief People Officer role at Pearl Health. Additionally, Virginie Glaenzer messaged you on LinkedIn (awaiting your response), and you have a confirmed 1:1 networking session with Meg Park today at 1 PM. A 15-minute consultation with Netta Jenkins (HIC Consult) is also confirmed for Friday, June 12.</span>
      </li>
      <li class="bullet-blue">
        <span class="icon">📅</span>
        <span><strong>Biggest Calendar Item:</strong> Today you have a time conflict — your HR Networking &amp; Job Search Group Zoom (12:00–1:30 PM) overlaps with your drinks with Meg Park at Caffè Bacio (1:00–2:00 PM). You are confirmed for Meg but still marked "needsAction" on the Zoom. Also note: your dentist appointment with Rosen &amp; Deutch, DDS PC is Wednesday, June 17 at 9:15 AM — a reminder email arrived today.</span>
      </li>
    </ul>
  </div>
</div>

<!-- ══════════════════════════════════════════════════════════ -->
<!-- 3. ACTION REQUIRED -->
<!-- ══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title red-title">⚡ Action Required</div>
  <div class="section-body">
    <div class="action-grid">

      <div class="action-card ac-red">
        <div class="label">🔴 Security / Phishing</div>
        <div class="title">Fake "Lowe's" Prize Winner Email</div>
        <div class="source">From: "Lowe's®" &lt;pasupportxk@foaxxgyhhhtrnvigodnbtoiz.com&gt;</div>
        <div class="why">Spoofed sender domain, "You Are Our Winner" language — classic phishing attempt targeting your Gmail username melissaw212. <strong>Do not click any links.</strong></div>
        <div class="step">🛡️ Mark as spam and delete immediately. Do not engage.</div>
        <div class="due">Due: Today</div>
      </div>

      <div class="action-card ac-red">
        <div class="label">🔴 GitHub / Tech Alert</div>
        <div class="title">Daily Briefing GitHub Workflow: 2 Failed Runs</div>
        <div class="source">From: missophs &lt;notifications@github.com&gt; — Runs d723d8b &amp; 61e8609</div>
        <div class="why">Both morning runs of your automated daily briefing workflow failed. You are receiving manual briefings (this one), but the automation is broken and may miss future job search results or briefings.</div>
        <div class="step">🔧 Review GitHub Actions logs for both failed runs. Check webhook configuration and secrets.</div>
        <div class="due">Due: Today or Tomorrow</div>
      </div>

      <div class="action-card ac-yellow">
        <div class="label">🟡 LinkedIn — Respond</div>
        <div class="title">Virginie Glaenzer Messaged You on LinkedIn</div>
        <div class="source">From: Virginie Glaenzer via LinkedIn (messaging-digest-noreply@linkedin.com)</div>
        <div class="why">An unread LinkedIn message is awaiting your response. In an active job search, timely responses to LinkedIn messages are critical for maintaining momentum and relationships.</div>
        <div class="step">💬 Open LinkedIn, read Virginie's message, and reply today.</div>
        <div class="due">Due: Today</div>
      </div>

      <div class="action-card ac-green">
        <div class="label">🟢 Job Opportunity</div>
        <div class="title">CHRO Role — Empathy Talent ($250K–$300K)</div>
        <div class="source">From: LinkedIn Job Alerts &lt;jobalerts-noreply@linkedin.com&gt;</div>
        <div class="why">High-salary C-suite CHRO role in Private Equity / Investment Management / Financial Services — aligns with your senior HR executive profile. Strong salary range.</div>
        <div class="step">🎯 Review full job description and apply if qualified. Research Empathy Talent firm.</div>
        <div class="due">Apply ASAP — competitive roles close quickly</div>
      </div>

      <div class="action-card ac-green">
        <div class="label">🟢 Job Opportunity</div>
        <div class="title">Chief People Officer — Pearl Health</div>
        <div class="source">From: LinkedIn Job Alerts &lt;jobalerts-noreply@linkedin.com&gt;</div>
        <div class="why">CPO role at Pearl Health (dedicated to empowering primary care). Health-tech CPO roles are high-demand; this is worth reviewing even if salary wasn't listed.</div>
        <div class="step">🎯 Review role requirements, company background, and decide within 24 hrs whether to apply.</div>
        <div class="due">Within 24 hours</div>
      </div>

      <div class="action-card ac-blue">
        <div class="label">🔵 Calendar — Conflict</div>
        <div class="title">Time Conflict: HR Zoom Overlaps with Meg Park Drinks</div>
        <div class="source">Google Calendar — June 10, 12:00–1:30 PM &amp; 1:00–2:00 PM</div>
        <div class="why">HR Networking Zoom runs 12:00–1:30 PM. Meg Park drinks at Caffè Bacio start at 1:00 PM (1223 3rd Ave). You are confirmed for Meg and "needsAction" on the Zoom. You'll need to leave the Zoom by 12:45 PM to travel to the venue.</div>
        <div class="step">📍 Plan to join Zoom at noon and exit by 12:45 PM for Meg meetup. RSVP to Zoom if attending.</div>
        <div class="due">Today — 12:00 PM</div>
      </div>

      <div class="action-card ac-blue">
        <div class="label">🔵 Medical Reminder</div>
        <div class="title">Dental Appointment — Rosen &amp; Deutch, DDS PC</div>
        <div class="source">From: Rosen &amp; Deutch, DDS PC &lt;noreply@mail.sg.getweave.com&gt;</div>
        <div class="why">Appointment confirmed: Wednesday, June 17 at 9:15 AM. Note: Your calendar shows "cleaning dr deutch" at 10:45 AM on June 17 — there may be a 1.5-hour discrepancy between the reminder (9:15 AM) and calendar entry (10:45 AM). Confirm correct time.</div>
        <div class="step">📞 Confirm appointment time — reminder says 9:15 AM, calendar says 10:45 AM.</div>
        <div class="due">Confirm before June 17</div>
      </div>

      <div class="action-card ac-purple">
        <div class="label">🟣 Professional Event</div>
        <div class="title">CHRO Panel Invite — "The CHRO's Real Superpower" (Tomorrow)</div>
        <div class="source">From: Tiphani Krueger | McLean &amp; Company &lt;krueger.tiphani@mcleanco.com&gt;</div>
        <div class="why">Personal invite from McLean &amp; Company to a CHRO panel tomorrow afternoon. Relevant to your job search and professional positioning as a senior HR leader.</div>
        <div class="step">📋 Review details, register if free/low-cost. Note: no calendar event added yet.</div>
        <div class="due">Event: Tomorrow (June 11)</div>
      </div>

      <div class="action-card ac-yellow">
        <div class="label">🟡 RSVP Pending</div>
        <div class="title">PeopleOps Networking Event — June 23 (8:30–10:30 AM EDT)</div>
        <div class="source">From: Phil Strazzulla &lt;philstrazzulla@luma-mail.com&gt; — "How HR Moves Business Metrics"</div>
        <div class="why">In-person networking event on June 23 at Whoops venue. You are not confirmed. This is a curated PeopleOps event that could support your job search network.</div>
        <div class="step">✅ Decide whether to attend and RSVP by the deadline.</div>
        <div class="due">RSVP needed — June 23 event</div>
      </div>

      <div class="action-card ac-yellow">
        <div class="label">🟡 Calendar RSVP</div>
        <div class="title">Executive Roundtable — Declined (Zoom, Tomorrow 9 AM)</div>
        <div class="source">Google Calendar — June 11, 9:00–10:30 AM (John Madigan)</div>
        <div class="why">You declined this Executive Roundtable. If this was accidental or you want to reconsider, tomorrow is the day. Confirm your non-attendance is intentional.</div>
        <div class="step">✔️ Confirm decline is intentional. If not, contact John Madigan to re-accept.</div>
        <div class="due">Confirm today for tomorrow event</div>
      </div>

      <div class="action-card ac-yellow">
        <div class="label">🟡 Finance</div>
        <div class="title">New Bank of America Credit Card — Account Setup</div>
        <div class="source">From: Bank of America &lt;customerservice@emcom.bankofamerica.com&gt;</div>
        <div class="why">New Customized Cash Rewards Visa Signature card issued. Account tools and security setup should be activated promptly to protect the account.</div>
        <div class="step">💳 Log in to BoA online banking, set up account alerts, and activate security features.</div>
        <div class="due">Within 48 hours</div>
      </div>

      <div class="action-card ac-yellow">
        <div class="label">🟡 Building Notice</div>
        <div class="title">A/C Preventative Maintenance — 27th &amp; 28th Floors (Trashed)</div>
        <div class="source">From: 303 East 83rd &lt;no-reply@callmax.us&gt; — moved to Trash</div>
        <div class="why">Annual A/C maintenance at your building. This was trashed but may require access to your unit or advance notice of disruption. Review before deleting.</div>
        <div class="step">📋 Restore and check if maintenance requires unit access. Confirm dates.</div>
        <div class="due">Review today</div>
      </div>

    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════════════════════ -->
<!-- 4. FULL 7-DAY CALENDAR -->
<!-- ══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title blue-title">📅 Full 7-Day Calendar (June 10–17, 2026)</div>
  <div class="section-body">

    <!-- TODAY: June 10 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Wednesday, June 10, 2026 — TODAY</div>

      <div class="cal-event">
        <div>
          <div class="cal-time">12:00 PM – 1:30 PM</div>
          <span class="cal-status status-pending">Needs Action</span>
          <div class="cal-conflict">⚠️ TIME CONFLICT</div>
        </div>
        <div>
          <div class="cal-name">HR Networking &amp; Job Search Group — Zoom 2</div>
          <div class="cal-meta">📍 <a href="https://us06web.zoom.us/j/81954171722" target="_blank">Zoom Link</a> &nbsp;|&nbsp; Large group session (~175+ attendees)</div>
          <div class="cal-prep">🔧 Prep: Review team guidelines before joining. Plan to exit by 12:45 PM to travel to Meg meetup.</div>
          <div class="cal-meta" style="margin-top:4px;">Note: A Fireflies.ai meeting prep email was sent for this session (trashed — review for key takeaways from last session).</div>
        </div>
      </div>

      <div class="cal-event">
        <div>
          <div class="cal-time">12:00 PM – 1:30 PM</div>
          <span class="cal-status status-confirmed">Confirmed</span>
        </div>
        <div>
          <div class="cal-name">Network (Personal Block)</div>
          <div class="cal-meta">📍 No location specified &nbsp;|&nbsp; No attendees listed</div>
          <div class="cal-prep">💡 Likely a personal reminder to network during this time block. May be redundant with HR Zoom above.</div>
        </div>
      </div>

      <div class="cal-event">
        <div>
          <div class="cal-time">1:00 PM – 2:00 PM</div>
          <span class="cal-status status-accepted">Accepted</span>
          <div class="cal-conflict">⚠️ OVERLAPS WITH ZOOM</div>
        </div>
        <div>
          <div class="cal-name">Melissa × Meg Drinks ☕</div>
          <div class="cal-meta">📍 Caffè Bacio — 1223 3rd Ave, New York &nbsp;|&nbsp; With: Meg Park (megpark@oakleafpartnership.com)</div>
          <div class="cal-prep">🎯 Prep: This is a networking/relationship meeting. Review Meg's background at Oakleaf Partnership. Come prepared with your current job search update and any asks.</div>
          <div class="cal-meta" style="margin-top:4px;">⚠️ Leave Zoom by 12:45 PM to arrive on time.</div>
        </div>
      </div>
    </div>

    <!-- June 11 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Thursday, June 11, 2026</div>

      <div class="cal-event">
        <div>
          <div class="cal-time">9:00 AM – 10:30 AM</div>
          <span class="cal-status status-declined">Declined</span>
        </div>
        <div>
          <div class="cal-name">Executive Roundtable (John Madigan)</div>
          <div class="cal-meta">📍 <a href="https://us02web.zoom.us/j/207786667" target="_blank">Zoom Link</a> &nbsp;|&nbsp; Meeting ID: 207 786 667 &nbsp;|&nbsp; Password: 205454</div>
          <div class="cal-prep">⚠️ You declined this event. Confirm decline is intentional — if not, re-accept today.</div>
        </div>
      </div>

      <div class="cal-event">
        <div>
          <div class="cal-time">12:00 PM – 1:00 PM</div>
          <span class="cal-status status-pending">Needs Action</span>
        </div>
        <div>
          <div class="cal-name">HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
          <div class="cal-meta">📍 <a href="https://us06web.zoom.us/j/85945371140" target="_blank">Zoom Link</a> &nbsp;|&nbsp; Large group session</div>
          <div class="cal-prep">🔧 Prep: Note — AI notetaking tools explicitly asked to be turned off. Open discussion format. RSVP pending.</div>
        </div>
      </div>
    </div>

    <!-- June 12 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Friday, June 12, 2026</div>

      <div class="cal-event">
        <div>
          <div class="cal-time">9:30 AM – 9:45 AM</div>
          <span class="cal-status status-accepted">Accepted</span>
        </div>
        <div>
          <div class="cal-name">Melissa Weiss × Netta Jenkins — 15-Min Consultation</div>
          <div class="cal-meta">📍 <a href="https://us06web.zoom.us/j/5224221004" target="_blank">Zoom Link</a> &nbsp;|&nbsp; Password: 424726 &nbsp;|&nbsp; With: Netta Jenkins (netta@hicconsult.com)</div>
          <div class="cal-prep">🎯 Prep: Research HIC Consult. Prepare a concise intro and your current job search goals for a 15-minute slot. Have your top ask ready.</div>
        </div>
      </div>
    </div>

    <!-- June 13 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Saturday, June 13, 2026</div>
      <div style="padding: 8px 12px; font-size: 13px; color: #94a3b8; font-style: italic;">No calendar events scheduled.</div>
    </div>

    <!-- June 14 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Sunday, June 14, 2026</div>
      <div style="padding: 8px 12px; font-size: 13px; color: #94a3b8; font-style: italic;">No calendar events scheduled.</div>
    </div>

    <!-- June 15 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Monday, June 15, 2026</div>

      <div class="cal-event">
        <div>
          <div class="cal-time">9:30 AM – 11:00 AM</div>
          <span class="cal-status status-confirmed">Confirmed</span>
        </div>
        <div>
          <div class="cal-name">Salon Appointment — Elle at UMI Salon 💇</div>
          <div class="cal-meta">📍 37 West 20th Street, Suite 1107, New York, NY 10011 &nbsp;|&nbsp; With: Elle M</div>
          <div class="cal-meta" style="margin-top:3px;">Service: Single Process with Blowout</div>
          <div class="cal-prep">✂️ Prep: Arrive on time — color + blowout takes 1.5 hrs. Block morning for this. <a href="https://elleatumi.glossgenius.com" target="_blank">Manage appointment</a> if needed.</div>
        </div>
      </div>
    </div>

    <!-- June 16 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Tuesday, June 16, 2026</div>

      <div class="cal-event">
        <div>
          <div class="cal-time">10:00 AM – 11:00 AM</div>
          <span class="cal-status status-confirmed">Confirmed</span>
        </div>
        <div>
          <div class="cal-name">Vet 🐾 (Stella)</div>
          <div class="cal-meta">📍 Location not specified &nbsp;|&nbsp; No attendees listed</div>
          <div class="cal-prep">🐶 Prep: Confirm vet address and bring any records needed. Note: A Chewy email arrived today about 20% off flea &amp; tick meds — relevant to Stella's care.</div>
        </div>
      </div>
    </div>

    <!-- June 17 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Wednesday, June 17, 2026</div>

      <div class="cal-event">
        <div>
          <div class="cal-time">10:45 AM – 11:45 AM</div>
          <span class="cal-status status-confirmed">Confirmed</span>
        </div>
        <div>
          <div class="cal-name">Dental Cleaning — Dr. Deutch 🦷</div>
          <div class="cal-meta">📍 Location not specified in calendar &nbsp;|&nbsp; Reminder email says: 9:15 AM at Rosen &amp; Deutch, DDS PC</div>
          <div class="cal-prep">⚠️ TIME DISCREPANCY: Reminder email says 9:15 AM; your calendar says 10:45 AM. Confirm correct time by calling the office before June 17.</div>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- ══════════════════════════════════════════════════════════ -->
<!-- 5. JOB SEARCH & INTERVIEW PIPELINE -->
<!-- ══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title green-title">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">

    <p style="font-size:13px; color:#374151; margin-bottom:14px;"><strong>Active Leads Today — June 10, 2026</strong></p>

    <div class="job-grid">

      <div class="job-card">
        <div class="jc-role">Chief Human Resources Officer</div>
        <div class="jc-company">Empathy Talent</div>
        <div class="jc-salary">💰 $250,000–$300,000/year | Private Equity / Investment Mgmt / Financial Services</div>
        <div style="font-size:12px; color:#374151;">Requires PE/IM/FS background. Very strong salary range. High-demand niche C-suite role.</div>
        <span class="badge badge-high">HIGH FIT</span>
        <div style="font-size:11px; margin-top:5px; color:#64748b;">Source: LinkedIn Job Alerts (today)</div>
      </div>

      <div class="job-card">
        <div class="jc-role">Chief People Officer</div>
        <div class="jc-company">Pearl Health</div>
        <div class="jc-salary">💰 Salary not listed | Healthcare / Primary Care Tech</div>
        <div style="font-size:12px; color:#374151;">Pearl Health empowers primary care physicians. CPO role at a purpose-driven health-tech company.</div>
        <span class="badge badge-medium">MEDIUM FIT</span>
        <div style="font-size:11px; margin-top:5px; color:#64748b;">Source: LinkedIn Job Alerts (today)</div>
      </div>

      <div class="job-card">
        <div class="jc-role">Director, HR Business Partner</div>
        <div class="jc-company">Omada Health</div>
        <div class="jc-salary">💰 $180K (est.) | Part-time | New York, NY</div>
        <div style="font-size:12px; color:#374151;">ZenSearch personalized match. Director-level HRBP at a digital health company.</div>
        <span class="badge badge-medium">MEDIUM FIT</span>
        <div style="font-size:11px; margin-top:5px; color:#64748b;">Source: ZenSearch Daily Zen (today)</div>
      </div>

      <div class="job-card" style="background:#eff6ff; border-color:#bfdbfe;">
        <div class="jc-role">Y Combinator — Work at a Startup</div>
        <div class="jc-company">Multiple Startups (YC Portfolio)</div>
        <div class="jc-salary">📋 Application status check requested</div>
        <div style="font-size:12px; color:#374151;">YC sent a follow-up asking if you're still job searching. Action required — confirm active status or update profile.</div>
        <span class="badge badge-medium">MEDIUM FIT</span>
        <div style="font-size:11px; margin-top:5px; color:#64748b;">Source: Y Combinator email (today)</div>
      </div>

      <div class="job-card" style="background:#faf5ff; border-color:#c4b5fd;">
        <div class="jc-role">Virginie Glaenzer — LinkedIn Message</div>
        <div class="jc-company">Unknown / TBD (Unread)</div>
        <div class="jc-salary">📩 1 unread message awaiting your response</div>
        <div style="font-size:12px; color:#374151;">Unknown content — could be a referral, job lead, or networking opportunity. Must read and respond today.</div>
        <span class="badge badge-high">RESPOND TODAY</span>
        <div style="font-size:11px; margin-top:5px; color:#64748b;">Source: LinkedIn messaging digest (today)</div>
      </div>

      <div class="job-card" style="background:#faf5ff; border-color:#c4b5fd;">
        <div class="jc-role">Netta Jenkins — 15-Min Consultation</div>
        <div class="jc-company">HIC Consult (netta@hicconsult.com)</div>
        <div class="jc-salary">📅 Friday, June 12 at 9:30 AM — Zoom</div>
        <div style="font-size:12px; color:#374151;">Accepted consultation. Likely a recruiter or career advisor. Prep your 60-second pitch and top priorities.</div>
        <span class="badge badge-high">CONFIRMED</span>
        <div style="font-size:11px; margin-top:5px; color:#64748b;">Source: Google Calendar</div>
      </div>

      <div class="job-card">
        <div class="jc-role">HR Networking &amp; Job Search Group</div>
        <div class="jc-company">Large Peer Group (175+ HR Professionals)</div>
        <div class="jc-salary">📅 Today, 12:00 PM + Tomorrow, 12:00 PM (Office Hours)</div>
        <div style="font-size:12px; color:#374151;">Active HR peer networking community. High value for referrals, leads, and peer support. Both events are pending RSVP.</div>
        <span class="badge badge-high">HIGH VALUE</span>
        <div style="font-size:11px; margin-top:5px; color:#64748b;">Source: Google Calendar</div>
      </div>

      <div class="job-card">
        <div class="jc-role">HR Search AM Automated Results</div>
        <div class="jc-company">Exa (0–1 results) + Apify (17–19 results)</div>
        <div class="jc-salary">📊 2 runs today: Run 27283631679 (7:34 AM) &amp; Run 27277318661 (5:51 AM)</div>
        <div style="font-size:12px; color:#374151;">Automated job search returned 17–19 Apify results and 0–1 Exa results. Review the email for specific job titles surfaced.</div>
        <span class="badge badge-medium">REVIEW</span>
        <div style="font-size:11px; margin-top:5px; color:#64748b;">Source: Self-sent automated emails (today)</div>
      </div>

      <div class="job-card" style="background:#fff7ed; border-color:#fed7aa;">
        <div class="jc-role">PeopleOps Networking Event</div>
        <div class="jc-company">Phil Strazzulla (Select Software Reviews)</div>
        <div class="jc-salary">📅 June 23, 8:30–10:30 AM EDT | In-person (WHOOP venue)</div>
        <div style="font-size:12px; color:#374151;">"How HR Moves Business Metrics" — curated PeopleOps event. Strong networking opportunity for HR leaders.</div>
        <span class="badge badge-medium">RSVP NEEDED</span>
        <div style="font-size:11px; margin-top:5px; color:#64748b;">Source: Phil Strazzulla (Luma invite)</div>
      </div>

    </div>

    <div class="note-box" style="margin-top:14px;">
      📊 <strong>Pipeline Summary:</strong> 3 active job alerts (1 High, 2 Medium) · 1 unread LinkedIn message (respond today) · 1 confirmed consultation Friday · 2 HR networking events this week · 2 automated job search runs reviewed · 1 event RSVP pending (June 23) · 1 YC follow-up requiring action
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════════════════════ -->
<!-- 6. FULL EMAIL REVIEW BY CATEGORY -->
<!-- ══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title purple-title">📧 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="email-cat-section">
      <div class="email-cat-header" style="background:#fee2e2; color:#b91c1c;">
        <span>🔴 Security / Risk</span><span class="cat-badge cat-red">3 emails</span>
      </div>
      <div class="email-item">
        <div class="unread-dot"></div>
        <div class="ei-from">"Lowe's®" (Spoofed)</div>
        <div class="ei-sub">"We have been trying to reach you - melissaw212" — Fake prize winner / phishing. Sender domain foaxxgyhhhtrnvigodnbtoiz.com is clearly fraudulent. <strong>Delete immediately.</strong></div>
        <span class="cat-badge cat-red">PHISHING</span>
      </div>
      <div class="email-item">
        <div class="unread-dot"></div>
        <div class="ei-from">"LOWER'S" (Spoofed)</div>
        <div class="ei-sub">Subject uses unicode/math characters to disguise spam — "melissaw212 𝘆𝗼𝘂 𝘄𝗼𝗻 𝗮 𝗥𝗶𝗱𝗴𝗶𝗱 Cordless 8-Tool Combo Kit" — No valid date. Domain jnt0cil4.ca. <strong>Delete immediately.</strong></div>
        <span class="cat-badge cat-red">PHISHING</span>
      </div>
      <div class="email-item">
        <div class="unread-dot"></div>
        <div class="ei-from">Cloud Notice (kottmandeprato43@hotmail.com)</div>
        <div class="ei-sub">[TRASH] "FINAL NOTICE 15051946551 (C8585538)" — Suspicious "case number" scam email from personal Hotmail. Empty snippet. <strong>Already in Trash — permanently delete.</strong></div>
        <span class="cat-badge cat-red">SCAM</span>
      </div>
      <div style="padding: 6px 12px; font-size: 12px; color: #64748b; font-style: italic;">⚠️ Recommended Action: Delete all 3. Do not click any links. Consider setting Gmail spam filters for these sender domains.</div>
    </div>

    <!-- JOB SEARCH -->
    <div class="email-cat-section">
      <div class="email-cat-header" style="background:#dcfce7; color:#166534;">
        <span>🟢 Job Search</span><span class="cat-badge cat-green">7 emails</span>
      </div>
      <div class="email-item">
        <div class="unread-dot"></div>
        <div class="ei-from">LinkedIn Job Alerts</div>
        <div class="ei-sub">CHRO at Empathy Talent — $250K–$300K/yr (Private Equity/Financial Services). <strong>High priority — review and apply today.</strong></div>
        <span class="cat-badge cat-green">HIGH</span>
      </div>
      <div class="email-item">
        <div class="ei-from">LinkedIn Job Alerts</div>
        <div class="ei-sub">Chief People Officer at Pearl Health — healthcare tech CPO role. Review and decide within 24 hrs.</div>
        <span class="cat-badge cat-green">REVIEW</span>
      </div>
      <div class="email-item">
        <div class="ei-from">Amy from ZenSearch</div>
        <div class="ei-sub">Today's Personalized Job Matches — Director, HR Business Partner at Omada Health (NYC, Part-time, ~$180K). Review full list.</div>
        <span class="cat-badge cat-green">REVIEW</span>
      </div>
      <div class="email-item">
        <div class="ei-from">Y Combinator</div>
        <div class="ei-sub">"Still looking for a job? (action required)" — YC Work at a Startup follow-up. Confirm you're still active to keep profile live.</div>
        <span class="cat-badge cat-yellow">ACTION</span>
      </div>
      <div class="email-item">
        <div class="ei-from">melissaw212@gmail.com (self)</div>
        <div class="ei-sub">HR Search AM — 2026-06-10 — Run 27283631679 (Exa: 0 results, Apify: 19 results)</div>
        <span class="cat-badge cat-green">REVIEW</span>
      </div>
      <div class="email-item">
        <div class="ei-from">melissaw212@gmail.com (self)</div>
        <div class="ei-sub">HR Search AM — 2026-06-10 — Run 27277318661 (Exa: 1 result, Apify: 17 results)</div>
        <span class="cat-badge cat-green">REVIEW</span>
      </div>
      <div class="email-item">
        <div class="ei-from">The Huntr Team</div>
        <div class="ei-sub">Invitation + Free Resume Reviews &amp; Job Search Support — Huntr job tracker platform. Low priority but may be useful for pipeline management.</div>
        <span class="cat-badge cat-gray">LOW</span>
      </div>
      <div style="padding: 6px 12px; font-size: 12px; color: #64748b; font-style: italic;">Recommended Action: Prioritize CHRO at Empathy Talent, respond to YC, review ZenSearch matches.</div>
    </div>

    <!-- RECRUITERS / NETWORKING -->
    <div class="email-cat-section">
      <div class="email-cat-header" style="background:#ede9fe; color:#5b21b6;">
        <span>🟣 Recruiters / Networking</span><span class="cat-badge cat-purple">4 emails</span>
      </div>
      <div class="email-item">
        <div class="unread-dot"></div>
        <div class="ei-from">Virginie Glaenzer (LinkedIn)</div>
        <div class="ei-sub">Unread LinkedIn message. 1 message awaiting response. <strong>Read and respond today.</strong></div>
        <span class="cat-badge cat-purple">RESPOND TODAY</span>
      </div>
      <div class="email-item">
        <div class="unread-dot"></div>
        <div class="ei-from">LinkedIn</div>
        <div class="ei-sub">"2 people noticed you" — 2 LinkedIn profile views. Check who viewed your profile — could be recruiters.</div>
        <span class="cat-badge cat-purple">CHECK</span>
      </div>
      <div class="email-item">
        <div class="ei-from">Darenia Alarcon (via LinkedIn)</div>
        <div class="ei-sub">Complimentary Online Reputation Report from Whitefriar — executive PR/media placement service. Interesting for brand building but likely a sales pitch.</div>
        <span class="cat-badge cat-gray">LOW</span>
      </div>
      <div class="email-item">
        <div class="ei-from">Phil Strazzulla (Luma invite)</div>
        <div class="ei-sub">Invited to PeopleOps Networking Event: "How HR Moves Business Metrics" — June 23, 8:30–10:30 AM. <strong>RSVP decision needed.</strong></div>
        <span class="cat-badge cat-yellow">RSVP</span>
      </div>
      <div style="padding: 6px 12px; font-size: 12px; color: #64748b; font-style: italic;">Recommended Action: Respond to Virginie on LinkedIn today. Check 2 profile viewers. Decide on June 23 RSVP.</div>
    </div>

    <!-- CALENDAR / EVENTS -->
    <div class="email-cat-section">
      <div class="email-cat-header" style="background:#dbeafe; color:#1e40af;">
        <span>🔵 Calendar / Events</span><span class="cat-badge cat-blue">4 emails</span>
      </div>
      <div class="email-item">
        <div class="unread-dot"></div>
        <div class="ei-from">Fred from Fireflies.ai [TRASH]</div>
        <div class="ei-sub">Meeting prep for HR Networking Zoom (today at 12 PM) — includes key takeaways from last session. Was trashed. Consider restoring to review prep notes before the meeting.</div>
        <span class="cat-badge cat-blue">RESTORE?</span>
      </div>
      <div class="email-item">
        <div class="unread-dot"></div>
        <div class="ei-from">Tiphani Krueger | McLean &amp; Company</div>
        <div class="ei-sub">"Join me tomorrow as we discuss the CHRO's real superpower" — Personal CHRO panel invite for June 11 afternoon. Not in trash. Relevant to job search.</div>
        <span class="cat-badge cat-purple">REVIEW/REGISTER</span>
      </div>
      <div class="email-item">
        <div class="ei-from">Melissa Daily Briefing (self)</div>
        <div class="ei-sub">Daily Briefing - 2026-06-10 14:32 UTC — Today's prior briefing (50 emails, 8 calendar events). Already read.</div>
        <span class="cat-badge cat-gray">ARCHIVE</span>
      </div>
      <div class="email-item">
        <div class="unread-dot"></div>
        <div class="ei-from">Melissa Daily Briefing (self, non-inbox)</div>
        <div class="ei-sub">Daily Briefing - 2026-06-10 14:30 UTC (earlier version, unread, not in inbox) — Duplicate/earlier run. Archive.</div>
        <span class="cat-badge cat-gray">ARCHIVE</span>
      </div>
      <div style="padding: 6px 12px; font-size: 12px; color: #64748b; font-style: italic;">Recommended Action: Restore Fireflies prep email. Register for CHRO panel tomorrow. Archive daily briefing duplicates.</div>
    </div>

    <!-- MEDICAL / HEALTH -->
    <div class="email-cat-section">
      <div class="email-cat-header" style="background:#ccfbf1; color:#065f46;">
        <span>🩺 Medical / Health</span><span class="cat-badge" style="
<hr>
<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Job Search / Recruiters</td><td>12</td></tr>
<tr><td>Medical / Health</td><td>2</td></tr>
<tr><td>Other / Review</td><td>24</td></tr>
<tr><td>Professional Development / Newsletters</td><td>7</td></tr>
<tr><td>Promotional / Retail</td><td>4</td></tr>
<tr><td>Security / Risk</td><td>1</td></tr>
</table>
<p><strong>Audit Note:</strong> Every fetched email was reviewed and assigned to one category. Trash emails were included in review. Promotional and low-value emails were accounted for but deprioritized.</p>

