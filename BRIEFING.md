<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa Weiss — July 21, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 2rem; font-weight: 700; letter-spacing: -.5px; }
  .header .subtitle { font-size: 1.05rem; color: #a8c8f8; margin-top: 4px; }
  .header-meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header-meta-item { background: rgba(255,255,255,.1); border-radius: 8px; padding: 10px 18px; text-align: center; }
  .header-meta-item .num { font-size: 1.6rem; font-weight: 700; color: #7dd3fc; }
  .header-meta-item .lbl { font-size: .78rem; color: #cbd5e1; text-transform: uppercase; letter-spacing: .5px; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 1.1rem; font-weight: 700; text-transform: uppercase; letter-spacing: .8px; padding: 10px 16px; border-radius: 8px 8px 0 0; margin-bottom: 0; }
  .section-body { background: #fff; border-radius: 0 0 10px 10px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,.07); }

  /* COLOR THEMES */
  .red    .section-title { background: #dc2626; color: #fff; }
  .yellow .section-title { background: #d97706; color: #fff; }
  .blue   .section-title { background: #2563eb; color: #fff; }
  .green  .section-title { background: #16a34a; color: #fff; }
  .purple .section-title { background: #7c3aed; color: #fff; }
  .gray   .section-title { background: #6b7280; color: #fff; }
  .navy   .section-title { background: #1e3a5f; color: #fff; }
  .teal   .section-title { background: #0d9488; color: #fff; }

  /* EXEC SUMMARY */
  .exec-bullets { list-style: none; padding: 0; }
  .exec-bullets li { padding: 12px 16px; border-left: 5px solid; margin-bottom: 10px; border-radius: 0 6px 6px 0; font-size: .95rem; }
  .exec-bullets li.risk   { border-color: #dc2626; background: #fef2f2; }
  .exec-bullets li.job    { border-color: #16a34a; background: #f0fdf4; }
  .exec-bullets li.cal    { border-color: #2563eb; background: #eff6ff; }
  .exec-bullets li strong { font-weight: 700; }

  /* CARDS */
  .card { border: 1px solid #e5e7eb; border-radius: 10px; padding: 16px 18px; margin-bottom: 14px; }
  .card-label { display: inline-block; font-size: .7rem; font-weight: 700; text-transform: uppercase; letter-spacing: .7px; padding: 2px 9px; border-radius: 20px; margin-bottom: 8px; }
  .label-red    { background: #fee2e2; color: #b91c1c; }
  .label-yellow { background: #fef3c7; color: #92400e; }
  .label-blue   { background: #dbeafe; color: #1d4ed8; }
  .label-green  { background: #dcfce7; color: #15803d; }
  .label-purple { background: #ede9fe; color: #6d28d9; }
  .label-gray   { background: #f3f4f6; color: #374151; }
  .label-teal   { background: #ccfbf1; color: #0f766e; }
  .label-orange { background: #ffedd5; color: #c2410c; }
  .card h3 { font-size: 1rem; font-weight: 700; margin-bottom: 6px; }
  .card .meta { font-size: .82rem; color: #6b7280; margin-bottom: 6px; }
  .card .why { font-size: .88rem; margin-bottom: 6px; }
  .card .next { font-size: .88rem; font-weight: 600; color: #1d4ed8; }
  .card .due  { font-size: .8rem; color: #b91c1c; font-weight: 600; margin-top: 4px; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { background: #1e3a5f; color: #fff; font-weight: 700; font-size: .9rem; padding: 7px 14px; border-radius: 6px; margin-bottom: 8px; }
  .cal-event { display: grid; grid-template-columns: 110px 1fr; gap: 10px; padding: 10px 12px; border: 1px solid #e5e7eb; border-radius: 8px; margin-bottom: 7px; background: #f9fafb; }
  .cal-time { font-weight: 700; font-size: .85rem; color: #1d4ed8; }
  .cal-details h4 { font-size: .9rem; font-weight: 700; margin-bottom: 3px; }
  .cal-details .cal-meta { font-size: .8rem; color: #6b7280; }
  .cal-status { display: inline-block; font-size: .7rem; font-weight: 700; padding: 1px 8px; border-radius: 10px; }
  .status-confirmed { background: #dcfce7; color: #15803d; }
  .status-needs     { background: #fef3c7; color: #92400e; }
  .status-declined  { background: #fee2e2; color: #b91c1c; }
  .status-bday      { background: #ede9fe; color: #6d28d9; }
  .status-reminder  { background: #e0f2fe; color: #0369a1; }

  /* TABLE */
  table { width: 100%; border-collapse: collapse; font-size: .87rem; }
  th { background: #1e3a5f; color: #fff; padding: 9px 12px; text-align: left; font-size: .8rem; text-transform: uppercase; letter-spacing: .5px; }
  td { padding: 9px 12px; border-bottom: 1px solid #f3f4f6; vertical-align: top; }
  tr:hover td { background: #f8fafc; }
  .priority-high   { color: #dc2626; font-weight: 700; }
  .priority-med    { color: #d97706; font-weight: 700; }
  .priority-low    { color: #16a34a; font-weight: 700; }
  .fit-high        { background: #dcfce7; color: #15803d; border-radius: 10px; padding: 1px 8px; font-size: .75rem; font-weight: 700; }
  .fit-med         { background: #fef3c7; color: #92400e; border-radius: 10px; padding: 1px 8px; font-size: .75rem; font-weight: 700; }
  .fit-low         { background: #f3f4f6; color: #374151; border-radius: 10px; padding: 1px 8px; font-size: .75rem; font-weight: 700; }

  /* DASHBOARD */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-item { background: #fff; border: 1px solid #e5e7eb; border-radius: 10px; padding: 16px; box-shadow: 0 1px 4px rgba(0,0,0,.05); }
  .dash-item .dash-num { font-size: 2rem; font-weight: 800; }
  .dash-item .dash-lbl { font-size: .78rem; text-transform: uppercase; color: #6b7280; letter-spacing: .5px; margin-top: 2px; }
  .dash-item .dash-detail { font-size: .82rem; color: #374151; margin-top: 6px; }
  .dash-red    .dash-num { color: #dc2626; }
  .dash-yellow .dash-num { color: #d97706; }
  .dash-green  .dash-num { color: #16a34a; }
  .dash-blue   .dash-num { color: #2563eb; }
  .dash-purple .dash-num { color: #7c3aed; }
  .dash-gray   .dash-num { color: #6b7280; }

  /* PRIORITIES */
  .priority-block { display: flex; gap: 14px; flex-wrap: wrap; }
  .priority-item { flex: 1; min-width: 280px; border-radius: 10px; padding: 18px; border: 2px solid; }
  .p1 { border-color: #dc2626; background: #fef2f2; }
  .p2 { border-color: #16a34a; background: #f0fdf4; }
  .p3 { border-color: #2563eb; background: #eff6ff; }
  .priority-item .pnum { font-size: 2rem; font-weight: 900; opacity: .2; float: right; line-height: 1; }
  .priority-item h3 { font-size: 1rem; font-weight: 700; margin-bottom: 6px; }
  .priority-item p { font-size: .88rem; }

  /* TRASH */
  .trash-group { margin-bottom: 14px; }
  .trash-group h4 { font-size: .9rem; font-weight: 700; margin-bottom: 6px; padding: 5px 10px; border-radius: 5px; }
  .trash-restore { background: #fef2f2; color: #b91c1c; }
  .trash-review  { background: #fef3c7; color: #92400e; }
  .trash-delete  { background: #f3f4f6; color: #374151; }
  .trash-item { font-size: .84rem; padding: 6px 10px; border-bottom: 1px solid #f3f4f6; }
  .trash-item:last-child { border-bottom: none; }

  /* PILLS */
  .pill { display: inline-block; border-radius: 20px; padding: 2px 10px; font-size: .75rem; font-weight: 600; margin: 2px; }
  .pill-blue   { background: #dbeafe; color: #1d4ed8; }
  .pill-green  { background: #dcfce7; color: #15803d; }
  .pill-red    { background: #fee2e2; color: #b91c1c; }
  .pill-yellow { background: #fef3c7; color: #92400e; }
  .pill-gray   { background: #f3f4f6; color: #374151; }
  .pill-purple { background: #ede9fe; color: #6d28d9; }

  /* MISC */
  .divider { border: none; border-top: 1px solid #e5e7eb; margin: 16px 0; }
  .note { font-size: .8rem; color: #6b7280; font-style: italic; margin-top: 8px; }
  .email-row td:first-child { font-weight: 600; width: 160px; }
  .count-badge { display: inline-block; background: #1e3a5f; color: #fff; border-radius: 20px; padding: 1px 10px; font-size: .78rem; font-weight: 700; margin-left: 8px; }
  .total-row td { font-weight: 800; background: #1e3a5f; color: #fff; }
  .phishing-tag { background: #dc2626; color: #fff; font-size: .7rem; font-weight: 700; padding: 1px 7px; border-radius: 10px; margin-left: 6px; }
  ul.bullets li { margin-left: 18px; font-size: .88rem; margin-bottom: 4px; }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ═══════════════════════════════════════════════════════════ HEADER -->
<div class="header">
  <div class="header-top">
    <h1>Good Morning, Melissa 👋</h1>
    <div class="subtitle">Executive Briefing &nbsp;·&nbsp; Tuesday, July 21, 2026</div>
  </div>
  <div class="header-meta">
    <div class="header-meta-item"><div class="num">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="header-meta-item"><div class="num">12</div><div class="lbl">Calendar Events</div></div>
    <div class="header-meta-item"><div class="num">2</div><div class="lbl">Meetings Today</div></div>
    <div class="header-meta-item"><div class="num">3</div><div class="lbl">Security Alerts</div></div>
    <div class="header-meta-item"><div class="num">8+</div><div class="lbl">Job Leads Active</div></div>
    <div class="header-meta-item"><div class="num">1</div><div class="lbl">Package Arriving Today</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ EXEC SUMMARY -->
<div class="section navy">
  <div class="section-title">⚡ Executive Summary</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li class="risk"><strong>🔴 Biggest Risk:</strong> Multiple security alerts from Google confirm new sign-ins to your account this morning (3:36 AM GMT). One phishing email spoofing a cloud storage service was auto-trashed, and two explicit spam messages remain outside trash. Review Google security activity immediately and permanently delete the spam.</li>
      <li class="job"><strong>🟢 Biggest Opportunity:</strong> Active job search pipeline is strong — a LinkedIn InMail from recruiter Raghav Grover, a confirmed application acknowledgment from Evermore (Head of People & Talent), a VP HR Business Partner rejection from EWS/Zelle to log, a Sr. HR Director role at $350K, and multiple Glassdoor/LinkedIn alerts including roles at The New York Times ($185K–$205K). Today's Daily Job Search Sweep email is in your inbox. Review and prioritize applications.</li>
      <li class="cal"><strong>🔵 Biggest Calendar Item:</strong> Two meetings today — Umi at 10:00 AM and Amber at 2:30 PM. Tomorrow, HR Networking & Job Search Group Zoom (12:00 PM) has no RSVP yet. You also have an Executive Roundtable on Thursday that you've declined — confirm that's intentional. Verizon Fios bill reminder is on Thursday.</li>
    </ul>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ ACTION REQUIRED -->
<div class="section red">
  <div class="section-title">🚨 Action Required</div>
  <div class="section-body">

    <div class="card" style="border-left: 4px solid #dc2626;">
      <span class="card-label label-red">🔐 SECURITY — URGENT</span>
      <h3>New Sign-In Alerts — Google Account</h3>
      <div class="meta">From: Google (no-reply@accounts.google.com) · Received: Tue Jul 21, 3:36 AM GMT</div>
      <div class="why">Google sent two security alerts: one to your primary account (melissaw212@gmail.com) and one to your recovery email (Melweiss212@gmail.com) regarding a new sign-in. Both arrived at 3:36 AM — an unusual hour. You also authorized Claude twice via Google Sign-In (two separate confirmation emails arrived around the same time Mon evening/night). Verify all activity is yours.</div>
      <div class="next">→ Go to myaccount.google.com → Security → Recent activity. Confirm all sign-ins. If any are unrecognized, change password immediately and review connected apps.</div>
      <div class="due">⏰ Due: TODAY — Do not defer</div>
    </div>

    <div class="card" style="border-left: 4px solid #dc2626;">
      <span class="card-label label-red">🚫 SPAM / PHISHING — DELETE</span>
      <h3>Two Explicit Spam Emails Still in Inbox/Not Trashed</h3>
      <div class="meta">From: Sex_Trick (33y5lovu74@v8px4ofgy6.us) · Sex Trick (rxhdgauoqhflht…@5lsocn.g3rx4f.miprg1.us)</div>
      <div class="why">Two explicit/spam emails are currently NOT in trash and NOT in inbox — they exist in your mailbox unsorted. Both are from random .us domains. Unrelated to your email activity but should be permanently deleted.</div>
      <div class="next">→ Permanently delete both immediately. Mark as spam/phishing to train filter. No links should be clicked.</div>
      <div class="due">⏰ Due: TODAY</div>
    </div>

    <div class="card" style="border-left: 4px solid #dc2626;">
      <span class="card-label label-red">⚠️ AUTO-TRASHED PHISHING</span>
      <h3>"Payment Declined" / Cloud Storage Threat — Already Removed</h3>
      <div class="meta">From: 'Payment-Declined' (melissaw212@lupxjlozzlzjj.us) · Mon Jul 20</div>
      <div class="why">This email was automatically trashed as high-confidence phishing. It spoofed a cloud storage provider using your own email address in the sender field, threatened imminent account deletion and data loss to harvest payment credentials. It has been removed from your inbox.</div>
      <div class="next">→ No further action needed. Already removed. Confirm it's permanently deleted from trash.</div>
      <div class="due">✅ Auto-handled — Verify deletion</div>
    </div>

    <div class="card" style="border-left: 4px solid #d97706;">
      <span class="card-label label-yellow">📅 RSVP NEEDED</span>
      <h3>HR Networking & Job Search Group — Zoom (Tomorrow)</h3>
      <div class="meta">Calendar · Wed Jul 22, 12:00–1:30 PM · Status: Needs Action</div>
      <div class="why">This is a large professional networking session (180+ attendees) relevant to your active job search. Your RSVP status is still "needsAction." You have a parallel "Network" calendar block at the same time (already confirmed).</div>
      <div class="next">→ Confirm attendance via calendar invite. Zoom link: us06web.zoom.us/j/81954171722. Review agenda/guidelines linked in event description.</div>
      <div class="due">⏰ Due: Today — RSVP before tomorrow noon</div>
    </div>

    <div class="card" style="border-left: 4px solid #d97706;">
      <span class="card-label label-yellow">📅 RSVP NEEDED</span>
      <h3>HR Networking Open Office Hours — Zoom (Thursday)</h3>
      <div class="meta">Calendar · Thu Jul 23, 12:00–1:00 PM · Status: Needs Action</div>
      <div class="why">Open office hours with the same HR networking group. No RSVP confirmed. Note: organizer specifically asks that automated AI notetaking tools be turned off for this session.</div>
      <div class="next">→ Confirm or decline. Zoom: us06web.zoom.us/j/85945371140. Disable AI notetakers if attending.</div>
      <div class="due">⏰ Due: Before Thursday</div>
    </div>

    <div class="card" style="border-left: 4px solid #d97706;">
      <span class="card-label label-yellow">💰 BILLING REMINDER</span>
      <h3>Verizon Fios Bill Due</h3>
      <div class="meta">Calendar · Thu Jul 23 (all day)</div>
      <div class="why">Verizon Fios bill reminder is on your calendar for Thursday. No email confirmation seen in inbox — may already be set to autopay or bill may not have arrived yet.</div>
      <div class="next">→ Verify autopay status or log in to pay manually before Thursday.</div>
      <div class="due">⏰ Due: July 23</div>
    </div>

    <div class="card" style="border-left: 4px solid #16a34a;">
      <span class="card-label label-green">💼 JOB SEARCH — REVIEW TODAY</span>
      <h3>Daily Job Search Sweep — July 21, 2026</h3>
      <div class="meta">From: melissaw212@gmail.com (self-sent pipeline) · In Inbox · Received: 7:53 AM</div>
      <div class="why">Your TypeScript pipeline auto-generated today's job search sweep. This email is in your inbox unread. Contains curated leads including Director HR Business Partner at The New York Times ($185K–$205K).</div>
      <div class="next">→ Open, review all leads, cross-reference with LinkedIn alerts and Glassdoor notifications received today. Prioritize applications.</div>
      <div class="due">⏰ Due: Today — review by 5 PM</div>
    </div>

    <div class="card" style="border-left: 4px solid #16a34a;">
      <span class="card-label label-green">💼 RECRUITER — RESPOND</span>
      <h3>LinkedIn InMail from Raghav Grover — "Exciting Opportunity"</h3>
      <div class="meta">From: Raghav Grover via LinkedIn · Tue Jul 21, 3:05 AM UTC · In Trash (review before deleting)</div>
      <div class="why">A recruiter reached out with an InMail about an unspecified opportunity. This was moved to trash but may be worth reviewing given your active job search. Subject says "Exciting opportunity."</div>
      <div class="next">→ Retrieve from trash, read full message, assess the role. If relevant, respond within 24–48 hours.</div>
      <div class="due">⏰ Due: Today or tomorrow</div>
    </div>

    <div class="card" style="border-left: 4px solid #16a34a;">
      <span class="card-label label-green">💼 APPLICATION — LOG REJECTION</span>
      <h3>EWS/Zelle — VP, HR Business Partner Role No Longer Available</h3>
      <div class="meta">From: earlywarning@myworkday.com · Tue Jul 21, 7:20 AM · In Trash</div>
      <div class="why">Early Warning Services/Zelle confirmed the VP HR Business Partner role you applied for is no longer available. This is a definitive rejection/withdrawal — update your tracking log.</div>
      <div class="next">→ Update job tracker. Mark EWS/Zelle as closed. No follow-up needed.</div>
      <div class="due">⏰ Log today</div>
    </div>

    <div class="card" style="border-left: 4px solid #16a34a;">
      <span class="card-label label-green">💼 APPLICATION CONFIRMED</span>
      <h3>Evermore — Head of People and Talent Application Received</h3>
      <div class="meta">From: noreply@evermoreoutcomes.com · Tue Jul 21, 2:40 AM · In Trash (restore)</div>
      <div class="why">Application confirmation from Evermore for Head of People and Talent. Company will review and follow up. This should be restored and logged.</div>
      <div class="next">→ Restore from trash. Log in job tracker. Set a follow-up reminder for 7–10 business days if no response.</div>
      <div class="due">⏰ Restore today; follow up ~July 31</div>
    </div>

    <div class="card" style="border-left: 4px solid #0d9488;">
      <span class="card-label label-teal">📦 PACKAGE ARRIVING TODAY</span>
      <h3>Temu Package — Out for Delivery Today</h3>
      <div class="meta">From: Temu (orders@transaction.temu.com) · Order #PO-211-14414847201911025 · In Inbox</div>
      <div class="why">Package is out for delivery today. USPS Informed Delivery also shows 1 mailpiece and 1 inbound package arriving today. Be available or arrange for receipt.</div>
      <div class="next">→ Monitor delivery. Check Temu app for tracking. USPS also has 1 mailpiece en route.</div>
      <div class="due">⏰ Today</div>
    </div>

    <div class="card" style="border-left: 4px solid #d97706;">
      <span class="card-label label-yellow">📅 CALENDAR CONFLICT CHECK</span>
      <h3>Executive Roundtable — Thursday — You've Declined</h3>
      <div class="meta">Calendar · Thu Jul 23, 9:00–10:30 AM · Host: John Madigan · Status: DECLINED</div>
      <div class="why">You declined this Executive Roundtable. Given your active networking and job search, this type of event could be valuable. Confirm the decline was intentional before the event occurs.</div>
      <div class="next">→ Verify your decline was intentional. If you'd like to rejoin, contact John Madigan or use the Zoom link in the calendar event.</div>
      <div class="due">⏰ Decide by Wednesday</div>
    </div>

    <div class="card" style="border-left: 4px solid #d97706;">
      <span class="card-label label-yellow">📞 INSURANCE CALL REMINDER</span>
      <h3>Call St. Francis — Verify Insurance is Up to Date</h3>
      <div class="meta">Calendar · Mon Jul 27, 9:00–10:00 AM · Phone: 1-866-367-2901</div>
      <div class="why">You have a reminder to call St. Francis to confirm insurance is current. Number is already in the calendar event description.</div>
      <div class="next">→ Call 1-866-367-2901 on Monday July 27 at 9 AM. Have your insurance card ready.</div>
      <div class="due">⏰ July 27</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ FULL 7-DAY CALENDAR -->
<div class="section blue">
  <div class="section-title">📅 Full 7-Day Calendar — July 21–27, 2026</div>
  <div class="section-body">

    <!-- Tuesday July 21 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Tuesday, July 21, 2026 — TODAY</div>

      <div class="cal-event">
        <div class="cal-time">All Day</div>
        <div class="cal-details">
          <h4>🎂 Eric Dordick's Birthday</h4>
          <div class="cal-meta"><span class="cal-status status-bday">Birthday</span> &nbsp; No location · No attendees listed</div>
          <div class="cal-meta">Prep: Consider sending a birthday message if Eric is a professional or personal contact worth nurturing.</div>
        </div>
      </div>

      <div class="cal-event">
        <div class="cal-time">10:00–11:00 AM</div>
        <div class="cal-details">
          <h4>☎️ Umi</h4>
          <div class="cal-meta"><span class="cal-status status-confirmed">Confirmed</span> &nbsp; No location listed · No attendees listed</div>
          <div class="cal-meta">Prep: No description provided. If this is a job search / networking call, prepare a brief update on your search status, target companies, and open questions. Confirm whether this is a phone or video call.</div>
        </div>
      </div>

      <div class="cal-event">
        <div class="cal-time">2:30–3:30 PM</div>
        <div class="cal-details">
          <h4>☎️ Amber</h4>
          <div class="cal-meta"><span class="cal-status status-confirmed">Confirmed</span> &nbsp; No location listed · No attendees listed</div>
          <div class="cal-meta">Prep: No description provided. Identify context (recruiter, colleague, friend?). Have talking points ready. Occurs ~3.5 hours after Umi meeting.</div>
        </div>
      </div>
    </div>

    <!-- Wednesday July 22 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Wednesday, July 22, 2026</div>

      <div class="cal-event">
        <div class="cal-time">12:00–1:30 PM</div>
        <div class="cal-details">
          <h4>🤝 HR Networking &amp; Job Search Group — Zoom 2</h4>
          <div class="cal-meta"><span class="cal-status status-needs">⚠️ RSVP Needed</span> &nbsp; 180+ attendees · Zoom: <a href="https://us06web.zoom.us/j/81954171722" style="color:#2563eb;">us06web.zoom.us/j/81954171722</a></div>
          <div class="cal-meta">Prep: Review HR Networking Team Guidelines (linked in calendar event). Prepare 30-second professional intro. Have your target role/companies ready. RSVP today.</div>
          <div class="cal-meta" style="color:#b91c1c; font-weight:600;">⚠️ Conflict: "Network" block is confirmed at same time — appears to be the same event or intentional overlap.</div>
        </div>
      </div>

      <div class="cal-event">
        <div class="cal-time">12:00–1:30 PM</div>
        <div class="cal-details">
          <h4>🤝 Network (Personal Block)</h4>
          <div class="cal-meta"><span class="cal-status status-confirmed">Confirmed</span> &nbsp; No location · No attendees listed</div>
          <div class="cal-meta">Prep: Likely a personal placeholder that corresponds to the HR Networking Zoom above. Confirm whether these are the same event or separate commitments.</div>
        </div>
      </div>
    </div>

    <!-- Thursday July 23 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Thursday, July 23, 2026</div>

      <div class="cal-event">
        <div class="cal-time">All Day</div>
        <div class="cal-details">
          <h4>🎂 Amy Fink's Birthday</h4>
          <div class="cal-meta"><span class="cal-status status-bday">Birthday</span> &nbsp; No location</div>
          <div class="cal-meta">Prep: Send a birthday message if Amy is a contact worth nurturing — especially relevant during job search.</div>
        </div>
      </div>

      <div class="cal-event">
        <div class="cal-time">All Day</div>
        <div class="cal-details">
          <h4>💳 Verizon Fios Bill Due</h4>
          <div class="cal-meta"><span class="cal-status status-reminder">Billing Reminder</span> &nbsp; Verify autopay or pay manually</div>
          <div class="cal-meta">Prep: Log in to Verizon account or confirm autopay is active to avoid late fees.</div>
        </div>
      </div>

      <div class="cal-event">
        <div class="cal-time">9:00–10:30 AM</div>
        <div class="cal-details">
          <h4>🔴 Executive Roundtable (DECLINED)</h4>
          <div class="cal-meta"><span class="cal-status status-declined">Declined</span> &nbsp; Host: John Madigan · Zoom: <a href="https://us02web.zoom.us/j/207786667" style="color:#2563eb;">us02web.zoom.us/j/207786667</a> · PW: 205454</div>
          <div class="cal-meta" style="color:#b91c1c;">⚠️ You've declined this event. Given your active job search, reconsider if this is a valuable executive networking opportunity. Decide by Wednesday.</div>
        </div>
      </div>

      <div class="cal-event">
        <div class="cal-time">12:00–1:00 PM</div>
        <div class="cal-details">
          <h4>🤝 HR Networking &amp; Job Search: Open Office Hours — Zoom 2</h4>
          <div class="cal-meta"><span class="cal-status status-needs">⚠️ RSVP Needed</span> &nbsp; Zoom: <a href="https://us06web.zoom.us/j/85945371140" style="color:#2563eb;">us06web.zoom.us/j/85945371140</a></div>
          <div class="cal-meta">Prep: Turn off AI notetaking tools (organizer's explicit request). Prepare specific questions or challenges for open discussion. RSVP required.</div>
          <div class="cal-meta" style="color:#d97706; font-weight:600;">ℹ️ Note: Follows the declined Executive Roundtable — no conflict if Roundtable remains declined.</div>
        </div>
      </div>
    </div>

    <!-- Friday July 24 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Friday, July 24, 2026</div>

      <div class="cal-event">
        <div class="cal-time">9:00–10:00 AM</div>
        <div class="cal-details">
          <h4>✂️ Stella Grooming</h4>
          <div class="cal-meta"><span class="cal-status status-confirmed">Confirmed</span> &nbsp; No location listed</div>
          <div class="cal-meta">Prep: Confirm groomer appointment and drop-off logistics. Note: LinkedIn connection "Stella Papadopoulos" accepted your invite today — different Stella (likely your pet's groomer vs. the LinkedIn connection).</div>
        </div>
      </div>
    </div>

    <!-- Saturday July 25 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Saturday, July 25, 2026</div>
      <div class="cal-event">
        <div class="cal-time">All Day</div>
        <div class="cal-details">
          <h4>No events scheduled</h4>
          <div class="cal-meta">Clear day — consider using for job application follow-ups or rest.</div>
        </div>
      </div>
    </div>

    <!-- Sunday July 26 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Sunday, July 26, 2026</div>

      <div class="cal-event">
        <div class="cal-time">All Day</div>
        <div class="cal-details">
          <h4>💳 Warby Parker Auto Pay</h4>
          <div class="cal-meta"><span class="cal-status status-reminder">Billing Reminder</span> &nbsp; Auto payment scheduled</div>
          <div class="cal-meta">Prep: Ensure sufficient funds in the linked account. Warby Parker also emailed a feedback survey — may be related to a recent purchase.</div>
        </div>
      </div>
    </div>

    <!-- Monday July 27 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Monday, July 27, 2026</div>

      <div class="cal-event">
        <div class="cal-time">9:00–10:00 AM</div>
        <div class="cal-details">
          <h4>📞 Call St. Francis — Verify Insurance</h4>
          <div class="cal-meta"><span class="cal-status status-confirmed">Confirmed</span> &nbsp; ☎️ 1-866-367-2901</div>
          <div class="cal-meta">Prep: Have your insurance card and policy number ready. Confirm coverage is current. If you recently changed employment status, verify no gaps in coverage.</div>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ JOB SEARCH PIPELINE -->
<div class="section green">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">
    <table>
      <thead>
        <tr>
          <th>Fit</th>
          <th>Source</th>
          <th>Role / Opportunity</th>
          <th>Company</th>
          <th>Salary</th>
          <th>Status</th>
          <th>Next Step</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="fit-high">HIGH</span></td>
          <td><span class="pill pill-blue">Self-Sweep</span></td>
          <td>Director, HR Business Partner, Advertising</td>
          <td>The New York Times</td>
          <td>$185K–$205K</td>
          <td>Lead identified today</td>
          <td>Apply via Greenhouse — top priority</td>
        </tr>
        <tr>
          <td><span class="fit-high">HIGH</span></td>
          <td><span class="pill pill-blue">LinkedIn Alert</span></td>
          <td>Sr. Human Resources Director</td>
          <td>Confidential</td>
          <td>Up to $350K/yr</td>
          <td>Alert received — apply</td>
          <td>Apply immediately; role posted 7/19</td>
        </tr>
        <tr>
          <td><span class="fit-high">HIGH</span></td>
          <td><span class="pill pill-green">Application</span></td>
          <td>Head of People and Talent</td>
          <td>Evermore</td>
          <td>Not specified</td>
          <td>✅ Application confirmed</td>
          <td>Restore from trash; follow up ~July 31</td>
        </tr>
        <tr>
          <td><span class="fit-high">HIGH</span></td>
          <td><span class="pill pill-blue">LinkedIn Alert</span></td>
          <td>VP, People and Culture (similar roles)</td>
          <td>Similar to Solari, Inc.</td>
          <td>Not specified</td>
          <td>Alert — review listings</td>
          <td>Open LinkedIn email in inbox; apply to matches</td>
        </tr>
        <tr>
          <td><span class="fit-med">MED</span></td>
          <td><span class="pill pill-purple">Recruiter</span></td>
          <td>"Exciting Opportunity" (details unknown)</td>
          <td>Unknown (via Raghav Grover)</td>
          <td>Unknown</td>
          <td>InMail in trash — retrieve</td>
          <td>Restore email, read full InMail, assess role</td>
        </tr>
        <tr>
          <td><span class="fit-med">MED</span></td>
          <td><span class="pill pill-green">Glassdoor</span></td>
          <td>HR &amp; Payroll Manager at SeatScope (+5 remote roles)</td>
          <td>Multiple (Remote, US)</td>
          <td>Not specified</td>
          <td>Alert received</td>
          <td>Review — may be below level but worth scanning</td>
        </tr>
        <tr>
          <td><span class="fit-low">LOW</span></td>
          <td><span class="pill pill-green">Glassdoor</span></td>
          <td>Community Manager at Fairstead (+5 NY roles)</td>
          <td>Multiple (New York, NY)</td>
          <td>Not specified</td>
          <td>Alert received</td>
          <td>Community Manager likely below level; scan briefly</td>
        </tr>
        <tr>
          <td><span class="fit-low">LOW</span></td>
          <td><span class="pill pill-purple">Inclusively</span></td>
          <td>Recommended jobs based on profile</td>
          <td>Multiple</td>
          <td>Not specified</td>
          <td>In trash — review if time</td>
          <td>Low priority — inclusively.com recommendations tend to be broad</td>
        </tr>
        <tr>
          <td>—</td>
          <td><span class="pill pill-red">Rejection</span></td>
          <td>VP, HR Business Partner</td>
          <td>Early Warning Services / Zelle</td>
          <td>—</td>
          <td>❌ Role no longer available</td>
          <td>Log as closed in tracker</td>
        </tr>
        <tr>
          <td><span class="fit-high">HIGH</span></td>
          <td><span class="pill pill-blue">Networking</span></td>
          <td>HR Networking &amp; Job Search Group — Zoom</td>
          <td>Peer HR Community</td>
          <td>—</td>
          <td>⚠️ RSVP needed (Wed &amp; Thu)</td>
          <td>RSVP today; prepare intro and target role summary</td>
        </tr>
        <tr>
          <td><span class="fit-med">MED</span></td>
          <td><span class="pill pill-blue">LinkedIn</span></td>
          <td>New connection — Stella Papadopoulos accepted invite</td>
          <td>Unknown</td>
          <td>—</td>
          <td>Connection accepted</td>
          <td>Send a brief follow-up message; explore her network</td>
        </tr>
        <tr>
          <td><span class="fit-med">MED</span></td>
          <td><span class="pill pill-blue">LinkedIn</span></td>
          <td>Brittany Halligan posted: NBCUniversal Principal DevOps Eng. (Remote)</td>
          <td>NBCUniversal</td>
          <td>—</td>
          <td>Contact posted — FYI</td>
          <td>DevOps role not HR — but Brittany may be a useful HR contact</td>
        </tr>
        <tr>
          <td><span class="fit-high">HIGH</span></td>
          <td><span class="pill pill-green">Self-Sweep</span></td>
          <td>Director, HR Business Partner + additional leads</td>
          <td>Various (from Melissa's pipeline)</td>
          <td>Multiple ranges</td>
          <td>Sweep in inbox — unread</td>
          <td>Open today's Daily Job Search Sweep email immediately</td>
        </tr>
        <tr>
          <td><span class="fit-med">MED</span></td>
          <td><span class="pill pill-green">Self-Curated</span></td>
          <td>Job tracker / leads spreadsheet (unnamed email)</td>
          <td>Multiple — includes NYT role</td>
          <td>$185K–$205K visible</td>
          <td>Self-sent notes in mailbox</td>
          <td>Cross-reference with today's sweep; update tracker</td>
        </tr>
      </tbody>
    </table>
    <div class="note">* NYS DOL UI direct deposit of $760.38 received this morning — unemployment benefits active. Ensure continued compliance with job search reporting requirements.</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ FULL EMAIL REVIEW BY CATEGORY -->
<div class="section navy">
  <div class="section-title">📬 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="card" style="border-left: 4px solid #dc2626;">
      <span class="card-label label-red">🔐 Security / Risk</span> <span class="count-badge">5 emails</span>
      <h3>Security Alerts, Phishing, and Spam</h3>
      <table style="margin-top:10px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Google (no-reply@accounts.google.com)</td><td>Security alert for melissaw212@gmail.com</td><td><span class="pill pill-red">Urgent</span></td><td>Review sign-in activity NOW</td></tr>
          <tr><td>Google (no-reply@accounts.google.com)</td><td>Security alert (new sign-in)</td><td><span class="pill pill-red">Urgent</span></td><td>Review sign-in activity NOW</td></tr>
          <tr><td>'Payment-Declined' (spoof domain)</td><td>Account blocked / data deletion threat</td><td><span class="phishing-tag">AUTO-TRASHED PHISHING</span></td><td>Already removed — verify permanent deletion</td></tr>
          <tr><td>Sex_Trick (v8px4ofgy6.us)</td><td>Make her squirt 3x… [explicit spam]</td><td><span class="pill pill-red">Not Trashed</span></td><td>Permanently delete + report spam</td></tr>
          <tr><td>Sex Trick (5lsocn.g3rx4f.miprg1.us)</td><td>What's new in adult entertainment…</td><td><span class="pill pill-red">Not Trashed</span></td><td>Permanently delete + report spam</td></tr>
        </tbody>
      </table>
    </div>

    <!-- JOB SEARCH -->
    <div class="card" style="border-left: 4px solid #16a34a;">
      <span class="card-label label-green">💼 Job Search</span> <span class="count-badge">8 emails</span>
      <h3>Applications, Alerts, and Pipeline</h3>
      <table style="margin-top:10px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>melissaw212@gmail.com (self)</td><td>Daily Job Search Sweep — 2026-07-21</td><td><span class="pill pill-green">In Inbox</span></td><td>Review today — top priority</td></tr>
          <tr><td>melissaw212@gmail.com (self)</td><td>[Unnamed — job leads spreadsheet]</td><td><span class="pill pill-gray">Not in inbox</span></td><td>Cross-reference with sweep</td></tr>
          <tr><td>earlywarning@myworkday.com (EWS/Zelle)</td><td>VP, HR Business Partner — No Longer Available</td><td><span class="pill pill-red">Rejection</span></td><td>Log as closed in tracker</td></tr>
          <tr><td>noreply@evermoreoutcomes.com</td><td>Thank you for applying to evermore</td><td><span class="pill pill-green">Confirmed</span></td><td>Restore from trash; set follow-up</td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>Sr HR Director at Confidential — up to $350K/yr</td><td><span class="pill pill-green">Alert</span></td><td>Apply — high priority</td></tr>
          <tr><td>LinkedIn (jobs-noreply)</td><td>New jobs similar to VP, People and Culture at Solari</td><td><span class="pill pill-green">In Inbox</span></td><td>Review LinkedIn recommendations</td></tr>
          <tr><td>Glassdoor</td><td>HR &amp; Payroll Manager at SeatScope + 5 remote roles</td><td><span class="pill pill-yellow">Review</span></td><td>Scan — may be below level</td></tr>
          <tr><td>Glassdoor</td><td>Community Manager at Fairstead + 5 NY roles</td><td><span class="pill pill-gray">Low fit</span></td><td>Scan briefly or ignore</td></tr>
        </tbody>
      </table>
    </div>

    <!-- RECRUITERS / NETWORKING -->
    <div class="card" style="border-left: 4px solid #7c3aed;">
      <span class="card-label label-purple">🤝 Recruiters / Networking</span> <span class="count-badge">3 emails</span>
      <h3>Recruiter Outreach &amp; LinkedIn Connections</h3>
      <table style="margin-top:10px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Raghav Grover via LinkedIn</td><td>Exciting opportunity (InMail)</td><td><span class="pill pill-yellow">In Trash — Retrieve</span></td><td>Restore, read full message, assess role</td></tr>
          <tr><td>Stella Papadopoulos via LinkedIn</td><td>Stella accepted your invitation</td><td><span class="pill pill-purple">In Trash</span></td><td>Send brief follow-up message; explore network</td></tr>
          <tr><td>LinkedIn (updates)</td><td>Brittany Halligan recently posted (NBCUniversal hiring)</td><td><span class="pill pill-gray">FYI</span></td><td>Note Brittany as HR contact — she's posting roles</td></tr>
        </tbody>
      </table>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="card" style="border-left: 4px solid #d97706;">
      <span class="card-label label-yellow">💰 Financial / Billing</span> <span class="count-badge">2 emails</span>
      <h3>Bank Alerts &amp; Account Activity</h3>
      <table style="margin-top:10px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Bank of America</td><td>Direct deposit credited — $760.38 from NYS DOL UI</td><td><span class="pill pill-green">In Trash</span></td><td>Deposit confirmed. Restore or note — UI benefit received. Ensure job search compliance.</td></tr>
          <tr><td>Inclusively</td><td>melissa weiss — Check out recommended jobs</td><td><span class="pill pill-gray">In Trash</span></td><td>Low priority — job recs from inclusively.com (also counted in job section as supplemental)</td></tr>
        </tbody>
      </table>
      <div class="note">Note: BofA direct deposit is a UI (unemployment insurance) payment from NYS DOL. Counted under Financial/Billing. Verizon Fios and Warby Parker billing reminders are calendar-based, not email-based.</div>
    </div>

    <!-- PACKAGE / SHIPPING -->
    <div class="card" style="border-left: 4px solid #0d9488;">
      <span class="card-label label-teal">📦 Packages &amp; Shipping</span> <span class="count-badge">4 emails</span>
      <h3>Temu Order &amp; USPS Delivery</h3>
      <table style="margin-top:10px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Temu</td><td>Your Temu order out-for-delivery (#PO-211…)</td><td><span class="pill pill-green">In Inbox</span></td><td>Package arriving today — be available</td></tr>
          <tr><td>Temu</td><td>Your Temu conversation from Customer Service</td><td><span class="pill pill-yellow">In Inbox</span></td><td>Review — CS reply may need response</td></tr>
          <tr><td>Temu</td><td>Your Temu package is arriving soon</td><td><span class="pill pill-gray">In Inbox (read)</span></td><td>Superseded by out-for-delivery notice — archive</td></tr>
          <tr><td>USPS Informed Delivery</td><td>Daily Digest — 1 mailpiece, 1 package arriving</td><td><span class="pill pill-gray">In Trash</span></td><td>Confirms package arrival — no further action</td></tr>
        </tbody>
      </table>
    </div>

    <!-- GOOGLE / ACCOUNT -->
    <div class="card" style="border-left: 4px solid #2563eb;">
      <span class="card-label label-blue">🔑 Account / Platform Notifications</span> <span class="count-badge">3 emails</span>
      <h3>Google Sign-In Confirmations &amp; Claude</h3>
      <table style="margin-top:10px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Google (noreply-accounts)</td><td>You shared Google Account data with Claude (1st)</td><td><span class="pill pill-gray">In Trash</span></td><td>Normal OAuth confirmation — archive/delete</td></tr>
          <tr><td>Google (noreply-accounts)</td><td>You shared Google Account data with Claude (2nd)</td><td><span class="pill pill-gray">In Trash</span></td><td>Second confirmation — archive/delete</td></tr>
          <tr><td>Claude Team (no-reply@email.claude.com)</td><td>Fable 5 is now part of your plan</td><td><span class="pill pill-gray">In Trash</span></td><td>Your Max plan now includes Fable 5 — FYI only</td></tr>
        </tbody>
      </table>
    </div>

    <!-- PERSONAL -->
    <div class="card" style="border-left: 4px solid #0d9488;">
      <span class="card-label label-teal">🌸 Personal</span> <span class="count-badge">3 emails</span>
      <h3>Dating Apps, Personal Notes</h3>
      <table style="margin-top:10px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>OkCupid</td><td>Someone likes you</td><td><span class="pill pill-gray">In Trash</span></td><td>Personal — review at leisure or delete</td></tr>
          <tr><td>Match.com</td><td>You've had a profile view from Scott (49, Paramus NJ)</td><td><span class="pill pill-gray">In Trash</span></td><td>Personal — review at leisure or delete</td></tr>
          <tr><td>Match.com</td><td>Green likes you. See if it's mutual.</td><td><span class="pill pill-gray">In Trash</span></td><td>Personal — review at leisure or delete</td></tr>
        </tbody>
      </table>
    </div>

    <!-- SELF NOTES -->
    <div class="card" style="border-left: 4px solid #6b7280;">
      <span class="card-label label-gray">📝 Self-Notes / Drafts</span> <span class="count-badge">2 emails</span>
      <h3>Emails Sent to Self</h3>
      <table style="margin-top:10px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>melissa (melissaw212@gmail.com)</td><td>bug fixing claude</td><td><span class="pill pill-gray">Sent to self</span></td><td>Development/technical notes — archive when done</td></tr>
          <tr><td>melissa (melissaw212@gmail.com)</td><td>[no subject — job leads spreadsheet data]</td><td><span class="pill pill-gray">Sent to self</span></td><td>Job tracker data — cross-reference with sweep</td></tr>
        </tbody>
      </table>
    </div>

    <!-- CHICK-FIL-A -->
    <div class="card" style="border-left: 4px solid #16a34a;">
      <span class="card-label label-green">🍗 Loyalty / Rewards</span> <span class="count-badge">1 email</span>
      <h3>Chick-fil-A — Loyalty Gift</h3>
      <table style="margin-top:10px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Your Local Chick-fil-A (Jared Caldwell)</td><td>A little something from me to you 🎁 (402 pts)</td><td><span class="pill pill-green">In Inbox</span></td><td>A gift from your local operator — redeem if interested</td></tr>
        </tbody>
      </table>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="card" style="border-left: 4px solid #7c3aed;">
      <span class="card-label label-purple">📚 Professional Development / Newsletters</span> <span class="count-badge">6 emails</span>
      <h3>AI, Leadership, and Industry Newsletters</h3>
      <table style="margin-top:10px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Recommendation</th></tr></thead>
        <tbody>
          <tr><td>AI For Leaders</td><td>How Does AI Search the Web</td><td>Keep — relevant to your AI/tech awareness</td></tr>
          <tr><td>The AI Report</td><td>Meta rents Anthropic $10B power; US AI safety head resigns</td><td>Keep — strategic AI landscape news</td></tr>
          <tr><td>TLDR</td><td>Google's Gemini chip, AMD vs Nvidia, agent economics</td><td>Keep — tech market intelligence</td></tr>
          <tr><td>CoolDeep AI</td><td>Does your Claude results feel the same every time</td><td>Review — Claude prompt tips</td></tr>
          <tr><td>BambooHR</td><td>[10 Metrics] How Engaged Are Your
