<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing – Melissa Weiss – July 22, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 16px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header .subtitle { font-size: 15px; color: #a8b8d8; margin-top: 4px; }
  .header-meta { display: flex; gap: 32px; margin-top: 20px; flex-wrap: wrap; }
  .header-meta .stat { background: rgba(255,255,255,0.08); border-radius: 10px; padding: 12px 20px; text-align: center; }
  .header-meta .stat .num { font-size: 24px; font-weight: 700; color: #e2e8f0; }
  .header-meta .stat .lbl { font-size: 11px; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 2px; }

  /* SECTION */
  .section { background: #fff; border-radius: 14px; padding: 24px 28px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .section-title { font-size: 17px; font-weight: 700; color: #1a1a2e; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; margin-bottom: 18px; display: flex; align-items: center; gap: 8px; }
  .section-title .icon { font-size: 18px; }

  /* EXECUTIVE SUMMARY */
  .exec-bullets { list-style: none; }
  .exec-bullets li { padding: 10px 14px; border-radius: 8px; margin-bottom: 8px; font-size: 14px; display: flex; align-items: flex-start; gap: 10px; }
  .exec-bullets li .bullet-icon { font-size: 18px; flex-shrink: 0; margin-top: 1px; }
  .exec-bullets li.risk { background: #fff0f0; border-left: 4px solid #e53e3e; }
  .exec-bullets li.opportunity { background: #f0fff4; border-left: 4px solid #38a169; }
  .exec-bullets li.calendar { background: #ebf8ff; border-left: 4px solid #3182ce; }

  /* ACTION CARDS */
  .action-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; }
  .action-card { border-radius: 10px; padding: 16px 18px; border-left: 5px solid; }
  .action-card.red { background: #fff5f5; border-color: #e53e3e; }
  .action-card.yellow { background: #fffff0; border-color: #d69e2e; }
  .action-card.green { background: #f0fff4; border-color: #38a169; }
  .action-card.blue { background: #ebf8ff; border-color: #3182ce; }
  .action-card.purple { background: #faf5ff; border-color: #805ad5; }
  .action-card .card-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 6px; }
  .action-card.red .card-label { color: #e53e3e; }
  .action-card.yellow .card-label { color: #b7791f; }
  .action-card.green .card-label { color: #276749; }
  .action-card.blue .card-label { color: #2b6cb0; }
  .action-card.purple .card-label { color: #6b46c1; }
  .action-card h3 { font-size: 14px; font-weight: 700; margin-bottom: 6px; color: #1a1a2e; }
  .action-card .meta { font-size: 12px; color: #718096; margin-bottom: 6px; }
  .action-card .why { font-size: 13px; color: #2d3748; margin-bottom: 8px; }
  .action-card .next-step { font-size: 12px; font-weight: 600; color: #4a5568; background: rgba(0,0,0,0.05); border-radius: 6px; padding: 6px 10px; }
  .action-card .due { font-size: 11px; color: #e53e3e; font-weight: 700; margin-top: 6px; }

  /* CALENDAR */
  .cal-day { margin-bottom: 20px; }
  .cal-day-header { font-size: 13px; font-weight: 700; color: #fff; background: #2d3748; border-radius: 6px; padding: 5px 12px; margin-bottom: 8px; display: inline-block; }
  .cal-day-header.today { background: #3182ce; }
  .cal-event { display: flex; gap: 12px; align-items: flex-start; padding: 10px 14px; border-radius: 8px; margin-bottom: 6px; border-left: 4px solid; }
  .cal-event.confirmed { background: #ebf8ff; border-color: #3182ce; }
  .cal-event.needs-action { background: #fffff0; border-color: #d69e2e; }
  .cal-event.declined { background: #fff5f5; border-color: #e53e3e; opacity: 0.75; }
  .cal-event.allday { background: #f7fafc; border-color: #a0aec0; }
  .cal-event .time { font-size: 12px; font-weight: 700; color: #4a5568; min-width: 90px; }
  .cal-event .event-body .title { font-size: 13px; font-weight: 700; color: #1a1a2e; }
  .cal-event .event-body .detail { font-size: 12px; color: #718096; margin-top: 2px; }
  .cal-event .event-body .rsvp-badge { display: inline-block; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 10px; margin-top: 4px; }
  .rsvp-confirmed { background: #c6f6d5; color: #276749; }
  .rsvp-needs { background: #fefcbf; color: #744210; }
  .rsvp-declined { background: #fed7d7; color: #822727; }
  .rsvp-allday { background: #e2e8f0; color: #4a5568; }
  .conflict-warn { font-size: 11px; color: #e53e3e; font-weight: 700; margin-top: 4px; }

  /* JOB SEARCH */
  .job-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .job-table th { background: #2d3748; color: #fff; padding: 9px 12px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
  .job-table td { padding: 9px 12px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  .job-table tr:last-child td { border-bottom: none; }
  .job-table tr:hover td { background: #f7fafc; }
  .fit-high { background: #c6f6d5; color: #276749; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: 700; }
  .fit-med { background: #fefcbf; color: #744210; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: 700; }
  .fit-low { background: #e2e8f0; color: #4a5568; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: 700; }

  /* EMAIL REVIEW */
  .email-category { margin-bottom: 16px; border-radius: 10px; overflow: hidden; border: 1px solid #e2e8f0; }
  .email-cat-header { display: flex; align-items: center; gap: 10px; padding: 10px 16px; font-weight: 700; font-size: 13px; }
  .email-cat-header .count-badge { font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 10px; background: rgba(255,255,255,0.3); }
  .email-cat-body { padding: 12px 16px; font-size: 13px; background: #fff; }
  .email-cat-body .senders { color: #4a5568; margin-bottom: 6px; }
  .email-cat-body .rec { font-weight: 600; }

  .cat-red .email-cat-header { background: #fed7d7; color: #822727; }
  .cat-yellow .email-cat-header { background: #fefcbf; color: #744210; }
  .cat-green .email-cat-header { background: #c6f6d5; color: #276749; }
  .cat-blue .email-cat-header { background: #bee3f8; color: #2a4365; }
  .cat-purple .email-cat-header { background: #e9d8fd; color: #44337a; }
  .cat-gray .email-cat-header { background: #e2e8f0; color: #2d3748; }
  .cat-orange .email-cat-header { background: #feebc8; color: #7b341e; }

  /* TRASH */
  .trash-group { margin-bottom: 16px; }
  .trash-group h4 { font-size: 13px; font-weight: 700; margin-bottom: 8px; padding: 6px 12px; border-radius: 6px; }
  .trash-group.restore h4 { background: #c6f6d5; color: #276749; }
  .trash-group.review h4 { background: #fefcbf; color: #744210; }
  .trash-group.delete h4 { background: #e2e8f0; color: #4a5568; }
  .trash-item { font-size: 12px; padding: 6px 10px; border-bottom: 1px solid #f0f0f0; display: flex; gap: 8px; }
  .trash-item:last-child { border-bottom: none; }
  .trash-item .sender { font-weight: 600; color: #2d3748; min-width: 160px; }
  .trash-item .subj { color: #4a5568; flex: 1; }
  .trash-item .reason { color: #718096; font-style: italic; }

  /* PROMO */
  .promo-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .promo-table th { background: #718096; color: #fff; padding: 8px 12px; text-align: left; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; }
  .promo-table td { padding: 8px 12px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  .promo-table tr:last-child td { border-bottom: none; }
  .rec-ignore { background: #e2e8f0; color: #4a5568; padding: 2px 8px; border-radius: 8px; font-size: 11px; font-weight: 700; }
  .rec-delete { background: #fed7d7; color: #822727; padding: 2px 8px; border-radius: 8px; font-size: 11px; font-weight: 700; }
  .rec-review { background: #fefcbf; color: #744210; padding: 2px 8px; border-radius: 8px; font-size: 11px; font-weight: 700; }
  .rec-keep { background: #c6f6d5; color: #276749; padding: 2px 8px; border-radius: 8px; font-size: 11px; font-weight: 700; }
  .rec-unsub { background: #e9d8fd; color: #44337a; padding: 2px 8px; border-radius: 8px; font-size: 11px; font-weight: 700; }

  /* ACCOUNTING */
  .accounting-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .accounting-table th { background: #1a1a2e; color: #fff; padding: 9px 14px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
  .accounting-table td { padding: 9px 14px; border-bottom: 1px solid #e2e8f0; }
  .accounting-table tr:last-child td { border-bottom: none; font-weight: 700; background: #f7fafc; }
  .accounting-table .total-row td { background: #1a1a2e; color: #fff; font-weight: 700; font-size: 14px; }

  /* DASHBOARD */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-card { border-radius: 10px; padding: 16px; text-align: center; }
  .dash-card .dash-num { font-size: 32px; font-weight: 800; margin-bottom: 4px; }
  .dash-card .dash-label { font-size: 11px; text-transform: uppercase; letter-spacing: 0.6px; font-weight: 600; }
  .dash-card.dc-red { background: #fff5f5; color: #e53e3e; }
  .dash-card.dc-green { background: #f0fff4; color: #38a169; }
  .dash-card.dc-blue { background: #ebf8ff; color: #3182ce; }
  .dash-card.dc-yellow { background: #fffff0; color: #d69e2e; }
  .dash-card.dc-purple { background: #faf5ff; color: #805ad5; }
  .dash-card.dc-gray { background: #f7fafc; color: #718096; }

  /* PRIORITY TABLE */
  .priority-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .priority-table th { background: #2d3748; color: #fff; padding: 9px 14px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
  .priority-table td { padding: 9px 14px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  .priority-table tr:last-child td { border-bottom: none; }
  .pri-high { background: #fed7d7; color: #822727; padding: 2px 8px; border-radius: 8px; font-size: 11px; font-weight: 700; }
  .pri-med { background: #fefcbf; color: #744210; padding: 2px 8px; border-radius: 8px; font-size: 11px; font-weight: 700; }
  .pri-low { background: #e2e8f0; color: #4a5568; padding: 2px 8px; border-radius: 8px; font-size: 11px; font-weight: 700; }

  /* TOP 3 */
  .top3 { counter-reset: top3; }
  .top3-item { display: flex; gap: 16px; align-items: flex-start; padding: 16px; border-radius: 10px; margin-bottom: 12px; }
  .top3-item:nth-child(1) { background: #fff5f5; border-left: 5px solid #e53e3e; }
  .top3-item:nth-child(2) { background: #f0fff4; border-left: 5px solid #38a169; }
  .top3-item:nth-child(3) { background: #ebf8ff; border-left: 5px solid #3182ce; }
  .top3-num { font-size: 28px; font-weight: 900; color: #a0aec0; min-width: 36px; }
  .top3-item:nth-child(1) .top3-num { color: #fc8181; }
  .top3-item:nth-child(2) .top3-num { color: #68d391; }
  .top3-item:nth-child(3) .top3-num { color: #63b3ed; }
  .top3-body h3 { font-size: 15px; font-weight: 700; margin-bottom: 4px; }
  .top3-body p { font-size: 13px; color: #4a5568; }

  /* NEWSLETTER TABLE */
  .nl-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .nl-table th { background: #6b46c1; color: #fff; padding: 8px 12px; text-align: left; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; }
  .nl-table td { padding: 8px 12px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  .nl-table tr:last-child td { border-bottom: none; }

  /* MISC */
  .warn-badge { background: #fed7d7; color: #822727; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 8px; margin-left: 6px; }
  .info-note { background: #ebf8ff; border-left: 4px solid #3182ce; padding: 10px 14px; border-radius: 6px; font-size: 13px; color: #2a4365; margin-top: 10px; }
  .phishing-badge { background: #1a1a2e; color: #fc8181; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 8px; margin-left: 6px; }
  hr.divider { border: none; border-top: 1px solid #e2e8f0; margin: 14px 0; }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ============================================================ HEADER -->
<div class="header">
  <h1>🗂 Executive Briefing</h1>
  <div class="subtitle">Prepared by your Chief of Staff &nbsp;·&nbsp; Wednesday, July 22, 2026</div>
  <div class="header-meta">
    <div class="stat"><div class="num">Good morning,</div><div class="lbl">Melissa Weiss, MPA</div></div>
    <div class="stat"><div class="num">50</div><div class="lbl">Total Emails Reviewed</div></div>
    <div class="stat"><div class="num">14</div><div class="lbl">Calendar Events</div></div>
    <div class="stat"><div class="num">3</div><div class="lbl">🔴 Security Alerts</div></div>
    <div class="stat"><div class="num">4</div><div class="lbl">🟡 Actions Required</div></div>
    <div class="stat"><div class="num">2</div><div class="lbl">🟢 Job Leads (Inbox)</div></div>
  </div>
</div>

<!-- ============================================================ EXECUTIVE SUMMARY -->
<div class="section">
  <div class="section-title"><span class="icon">⚡</span> Executive Summary</div>
  <ul class="exec-bullets">
    <li class="risk">
      <span class="bullet-icon">🔴</span>
      <div><strong>Security / Risk:</strong> Three emails were auto-trashed as confirmed phishing (fake CashApp, spoofed Payment-Declined, and explicit spam). Additionally, two unsolicited pharmaceutical spam emails and a misaddressed Mercedes dealer email remain in your mailbox — none require action but warrant awareness. Your email address is actively being targeted; no links or attachments should be clicked in suspicious messages.</div>
    </li>
    <li class="opportunity">
      <span class="bullet-icon">🟢</span>
      <div><strong>Job Search / Opportunity:</strong> Two high-priority LinkedIn job alerts are sitting unread in your inbox — <em>Chief Human Resources Officer (Confidential)</em> and <em>VP Human Resources at Addition Management (up to $175K)</em>. You also have a confirmed application to Career Team's Senior Director of People &amp; Culture role (application receipt in Trash). Your outreach to "Jade" about contacts is pending a reply. The HR Networking Zoom is today at noon — RSVP is still outstanding.</div>
    </li>
    <li class="calendar">
      <span class="bullet-icon">🔵</span>
      <div><strong>Calendar / Deadline:</strong> Today is packed: Stella's medication pickup (9:30 AM) overlaps with blood work (10:00 AM) — potential timing conflict. HR Networking Zoom is at noon (RSVP pending). Tomorrow: Amy Fink's birthday, Verizon Fios bill due, and an Executive Roundtable you've already declined. Warby Parker auto-pay hits July 26. St. Francis insurance call is July 27.</div>
    </li>
  </ul>
</div>

<!-- ============================================================ ACTION REQUIRED -->
<div class="section">
  <div class="section-title"><span class="icon">✅</span> Action Required</div>
  <div class="action-grid">

    <div class="action-card red">
      <div class="card-label">🔴 Security</div>
      <h3>HPD Housing Connect — Update Your Information</h3>
      <div class="meta">From: HCnotifications@hpd.nyc.gov · Unread · In Inbox</div>
      <div class="why">Official NYC HPD notification requesting you log in to Housing Connect to review an important dashboard message. Legitimate city agency email — requires attention.</div>
      <div class="next-step">➜ Log in to Housing Connect at nyc.gov to review the dashboard message.</div>
      <div class="due">⏰ Time-sensitive — act today</div>
    </div>

    <div class="action-card yellow">
      <div class="card-label">🟡 Follow-Up Needed</div>
      <h3>Follow Up with Jade — Contacts Outreach</h3>
      <div class="meta">From: melissa (melissaw212@gmail.com) · Sent Thu July 23 · Awaiting reply</div>
      <div class="why">You emailed Jade asking about a contacts situation. She recently returned to the office. No reply received yet — this may be career-relevant networking.</div>
      <div class="next-step">➜ If no reply by EOD Thursday, send a brief follow-up nudge to Jade.</div>
      <div class="due">⏰ Follow up by Friday, July 24</div>
    </div>

    <div class="action-card yellow">
      <div class="card-label">🟡 Billing / Deadline</div>
      <h3>Verizon Fios Bill Due Tomorrow</h3>
      <div class="meta">Calendar event: July 23, 2026 (All Day)</div>
      <div class="why">Verizon Fios bill is flagged on your calendar for July 23. Confirm payment is scheduled or paid to avoid service interruption.</div>
      <div class="next-step">➜ Verify payment is scheduled or pay online today.</div>
      <div class="due">⏰ Due: Thursday, July 23</div>
    </div>

    <div class="action-card blue">
      <div class="card-label">🔵 RSVP Needed</div>
      <h3>HR Networking &amp; Job Search Group — Zoom Today</h3>
      <div class="meta">Calendar event: Today 12:00–1:30 PM · Status: Needs Action</div>
      <div class="why">Large HR networking Zoom (100+ attendees) starting at noon today. Your RSVP status is "needsAction" — you haven't confirmed attendance. This is a key job search network event.</div>
      <div class="next-step">➜ Confirm attendance and join at 12:00 PM: zoom.us/j/81954171722</div>
      <div class="due">⏰ Today, July 22 at 12:00 PM</div>
    </div>

    <div class="action-card green">
      <div class="card-label">🟢 Job Search</div>
      <h3>Review: CHRO &amp; VP HR LinkedIn Job Alerts</h3>
      <div class="meta">From: LinkedIn Job Alerts · Unread · In Inbox</div>
      <div class="why">Two unread, high-relevance job alerts: (1) Chief Human Resources Officer at a confidential company, and (2) VP Human Resources at Addition Management up to $175K. Both posted 7/20/2026.</div>
      <div class="next-step">➜ Open both LinkedIn alerts, review roles, and apply or save before they age out.</div>
      <div class="due">⏰ Act today — posted 7/20, now 2 days old</div>
    </div>

    <div class="action-card yellow">
      <div class="card-label">🟡 Medical Reminder</div>
      <h3>Call St. Francis — Confirm Insurance Is Current</h3>
      <div class="meta">Calendar event: Monday, July 27, 9:00–10:00 AM · Phone: 1-866-367-2901</div>
      <div class="why">You have a reminder to call St. Francis to verify insurance is up to date. Ensure this call happens before your PT appointment on July 28.</div>
      <div class="next-step">➜ Call 1-866-367-2901 on Monday morning at 9 AM as scheduled.</div>
      <div class="due">⏰ Monday, July 27 at 9:00 AM</div>
    </div>

  </div>
</div>

<!-- ============================================================ FULL 7-DAY CALENDAR -->
<div class="section">
  <div class="section-title"><span class="icon">📅</span> Full 7-Day Calendar</div>

  <!-- TODAY: July 22 -->
  <div class="cal-day">
    <div class="cal-day-header today">📍 TODAY — Wednesday, July 22, 2026</div>

    <div class="cal-event confirmed">
      <div class="time">9:30 – 10:30 AM</div>
      <div class="event-body">
        <div class="title">💊 Pick up Stella's med</div>
        <div class="detail">Personal errand — pick up medication for Stella</div>
        <span class="rsvp-badge rsvp-confirmed">✔ Confirmed</span>
        <div class="conflict-warn">⚠️ Potential conflict: Blood work starts at 10:00 AM — plan timing carefully</div>
      </div>
    </div>

    <div class="cal-event confirmed">
      <div class="time">10:00 – 11:00 AM</div>
      <div class="event-body">
        <div class="title">🩸 Blood Work</div>
        <div class="detail">Medical appointment — blood work</div>
        <span class="rsvp-badge rsvp-confirmed">✔ Confirmed</span>
        <div class="conflict-warn">⚠️ Overlap window with Stella's med pickup — start pickup no later than 9:30 AM sharp</div>
      </div>
    </div>

    <div class="cal-event needs-action">
      <div class="time">12:00 – 1:30 PM</div>
      <div class="event-body">
        <div class="title">🤝 HR Networking &amp; Job Search Group — Zoom 2</div>
        <div class="detail">100+ HR professionals · Large group networking session</div>
        <div class="detail">📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Join Zoom</a> · Meeting ID: 81954171722</div>
        <span class="rsvp-badge rsvp-needs">⚠ Needs RSVP</span>
        <div class="detail">🗒 Prep: Review team guidelines, prepare brief intro, bring job search status update</div>
      </div>
    </div>

    <div class="cal-event confirmed">
      <div class="time">12:00 – 1:30 PM</div>
      <div class="event-body">
        <div class="title">🗂 Network</div>
        <div class="detail">Personal networking block (confirmed separately on calendar)</div>
        <span class="rsvp-badge rsvp-confirmed">✔ Confirmed</span>
        <div class="detail">Note: Overlaps with HR Networking Zoom — same time window, likely intentional pairing</div>
      </div>
    </div>
  </div>

  <!-- TOMORROW: July 23 -->
  <div class="cal-day">
    <div class="cal-day-header">Thursday, July 23, 2026</div>

    <div class="cal-event allday">
      <div class="time">All Day</div>
      <div class="event-body">
        <div class="title">🎂 Amy Fink's Birthday</div>
        <div class="detail">Send a message or card to Amy Fink today</div>
        <span class="rsvp-badge rsvp-allday">All Day</span>
      </div>
    </div>

    <div class="cal-event allday">
      <div class="time">All Day</div>
      <div class="event-body">
        <div class="title">📱 Verizon Fios Bill Due</div>
        <div class="detail">Pay or confirm scheduled payment for Verizon Fios</div>
        <span class="rsvp-badge rsvp-allday">Billing</span>
      </div>
    </div>

    <div class="cal-event declined">
      <div class="time">9:00 – 10:30 AM</div>
      <div class="event-body">
        <div class="title">🚫 Executive Roundtable (Declined)</div>
        <div class="detail">Host: John Madigan · Zoom Meeting</div>
        <div class="detail">📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> · ID: 207 786 667 · PW: 205454</div>
        <span class="rsvp-badge rsvp-declined">✖ Declined</span>
        <div class="detail">You have already declined this event — no action needed</div>
      </div>
    </div>

    <div class="cal-event needs-action">
      <div class="time">12:00 – 1:00 PM</div>
      <div class="event-body">
        <div class="title">🤝 HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
        <div class="detail">Open discussion format · No recording or AI notetaking</div>
        <div class="detail">📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Join Zoom</a> · ID: 85945371140</div>
        <span class="rsvp-badge rsvp-needs">⚠ Needs RSVP</span>
        <div class="detail">🗒 Note: Organizer requests no automated notetaking AI tools</div>
      </div>
    </div>
  </div>

  <!-- July 24 -->
  <div class="cal-day">
    <div class="cal-day-header">Friday, July 24, 2026</div>
    <div class="cal-event confirmed">
      <div class="time">9:00 – 10:00 AM</div>
      <div class="event-body">
        <div class="title">🐾 Stella Grooming</div>
        <div class="detail">Grooming appointment for Stella</div>
        <span class="rsvp-badge rsvp-confirmed">✔ Confirmed</span>
      </div>
    </div>
  </div>

  <!-- July 25 -->
  <div class="cal-day">
    <div class="cal-day-header">Saturday, July 25, 2026</div>
    <div class="cal-event allday">
      <div class="time">All Day</div>
      <div class="event-body">
        <div class="title">✅ No Events Scheduled</div>
        <span class="rsvp-badge rsvp-allday">Clear</span>
      </div>
    </div>
  </div>

  <!-- July 26 -->
  <div class="cal-day">
    <div class="cal-day-header">Sunday, July 26, 2026</div>
    <div class="cal-event allday">
      <div class="time">All Day</div>
      <div class="event-body">
        <div class="title">💳 Warby Parker Auto Pay</div>
        <div class="detail">Automatic payment scheduled — verify funds available</div>
        <span class="rsvp-badge rsvp-allday">Billing</span>
      </div>
    </div>
  </div>

  <!-- July 27 -->
  <div class="cal-day">
    <div class="cal-day-header">Monday, July 27, 2026</div>
    <div class="cal-event confirmed">
      <div class="time">9:00 – 10:00 AM</div>
      <div class="event-body">
        <div class="title">📞 Call St. Francis — Confirm Insurance Is Current</div>
        <div class="detail">📞 Phone: 1-866-367-2901</div>
        <span class="rsvp-badge rsvp-confirmed">✔ Confirmed</span>
        <div class="detail">🗒 Prep: Have insurance card/info handy before calling</div>
      </div>
    </div>
  </div>

  <!-- July 28 -->
  <div class="cal-day">
    <div class="cal-day-header">Tuesday, July 28, 2026</div>

    <div class="cal-event confirmed">
      <div class="time">11:00 AM – 12:00 PM</div>
      <div class="event-body">
        <div class="title">🏃 PT (Physical Therapy)</div>
        <div class="detail">Physical therapy appointment (listed twice — likely duplicate entry)</div>
        <span class="rsvp-badge rsvp-confirmed">✔ Confirmed</span>
        <div class="detail">⚠️ Duplicate event on calendar — consider deleting one instance</div>
      </div>
    </div>

    <div class="cal-event confirmed">
      <div class="time">12:30 – 1:30 PM</div>
      <div class="event-body">
        <div class="title">📋 Contact</div>
        <div class="detail">Networking or outreach call — no additional details provided</div>
        <span class="rsvp-badge rsvp-confirmed">✔ Confirmed</span>
        <div class="detail">🗒 Consider adding contact name/number to this calendar event for easy reference</div>
      </div>
    </div>
  </div>
</div>

<!-- ============================================================ JOB SEARCH & INTERVIEW PIPELINE -->
<div class="section">
  <div class="section-title"><span class="icon">💼</span> Job Search &amp; Interview Pipeline</div>
  <table class="job-table">
    <thead>
      <tr>
        <th>Source</th>
        <th>Role / Opportunity</th>
        <th>Company</th>
        <th>Fit</th>
        <th>Status</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>LinkedIn Job Alert</td>
        <td>Chief Human Resources Officer</td>
        <td>Confidential</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>Unread · In Inbox</td>
        <td>Review &amp; apply immediately — posted 7/20</td>
      </tr>
      <tr>
        <td>LinkedIn Job Alert</td>
        <td>VP Human Resources (up to $175K/yr)</td>
        <td>Addition Management</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>Unread · In Inbox</td>
        <td>Review &amp; apply immediately — posted 7/20</td>
      </tr>
      <tr>
        <td>LinkedIn Job Alert</td>
        <td>Senior People Business Partner – NYC</td>
        <td>Datadog</td>
        <td><span class="fit-med">MED</span></td>
        <td>In Trash · Unread</td>
        <td>Restore from trash if interested — tech sector SPBP role</td>
      </tr>
      <tr>
        <td>Glassdoor</td>
        <td>Senior Community Manager + 6 more NYC jobs</td>
        <td>Morgan &amp; Morgan / Onyx Equities</td>
        <td><span class="fit-low">LOW</span></td>
        <td>Read · Not in inbox</td>
        <td>Low HR relevance — review briefly or ignore</td>
      </tr>
      <tr>
        <td>Greenhouse ATS</td>
        <td>Senior Director of People &amp; Culture</td>
        <td>Career Team</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>Applied ✔ · Receipt in Trash</td>
        <td>Restore confirmation email from trash for records; await next steps</td>
      </tr>
      <tr>
        <td>Melissa's Outreach</td>
        <td>Outreach to Jade re: Contacts</td>
        <td>Unknown</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>Sent — awaiting reply</td>
        <td>Follow up with Jade by Friday if no response</td>
      </tr>
      <tr>
        <td>Melissa's Draft</td>
        <td>Senior Director note for GitLab (outreach draft)</td>
        <td>GitLab</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>Draft / sent — in mailbox</td>
        <td>Track whether sent; follow up on response</td>
      </tr>
      <tr>
        <td>HR Networking Zoom</td>
        <td>HR Networking &amp; Job Search Group</td>
        <td>Group Session</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>TODAY · 12 PM · RSVP Pending</td>
        <td>Confirm attendance and join Zoom today at noon</td>
      </tr>
      <tr>
        <td>HR Networking Zoom</td>
        <td>Open Office Hours — Networking</td>
        <td>Group Session</td>
        <td><span class="fit-high">HIGH</span></td>
        <td>Tomorrow · 12 PM · RSVP Pending</td>
        <td>RSVP and attend tomorrow at noon</td>
      </tr>
      <tr>
        <td>LinkedIn (Adam Davison)</td>
        <td>Connection request — COO/Director</td>
        <td>Unknown</td>
        <td><span class="fit-med">MED</span></td>
        <td>Pending — awaiting response</td>
        <td>Review Adam Davison's profile; accept if relevant</td>
      </tr>
      <tr>
        <td>LinkedIn</td>
        <td>2 People noticed your profile</td>
        <td>LinkedIn</td>
        <td><span class="fit-low">LOW</span></td>
        <td>Read</td>
        <td>Check who viewed your profile; connect if relevant</td>
      </tr>
      <tr>
        <td>SignalHire</td>
        <td>5 new contact credits added</td>
        <td>SignalHire</td>
        <td><span class="fit-med">MED</span></td>
        <td>Read · Not in inbox</td>
        <td>Use credits to find contact info for target employers</td>
      </tr>
      <tr>
        <td>HRJobsRemote.com</td>
        <td>376 fully remote HR jobs</td>
        <td>HRJobsRemote.com</td>
        <td><span class="fit-med">MED</span></td>
        <td>Unread · In Trash</td>
        <td>Check if any CHRO/VP-level remote roles are listed before deleting</td>
      </tr>
      <tr>
        <td>Lisa Rangel (Chameleon)</td>
        <td>Hidden executive roles — networking insights</td>
        <td>Chameleon Resumes</td>
        <td><span class="fit-low">LOW</span></td>
        <td>Unread · In Trash</td>
        <td>Scan article if time allows; delete afterward</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ============================================================ FULL EMAIL REVIEW BY CATEGORY -->
<div class="section">
  <div class="section-title"><span class="icon">📬</span> Full Email Review by Category</div>

  <!-- SECURITY / RISK -->
  <div class="email-category cat-red">
    <div class="email-cat-header">
      🔴 Security / Risk
      <span class="count-badge">6 emails</span>
    </div>
    <div class="email-cat-body">
      <div class="senders"><strong>Senders:</strong> 'Payment-Declined' spoofed (auto-trashed phishing), CashApp spoofed (auto-trashed phishing), Spoofed melissaw212 explicit spam (auto-trashed), CarePharmacy spam (Levitra), Ozempic DirectMeds spam, HPD Housing Connect (legitimate)</div>
      <hr class="divider">
      <strong>1. Auto-Trashed — Payment-Declined Phishing</strong> <span class="phishing-badge">AUTO-TRASHED</span><br>
      Spoofed "Payment-Declined" sender from random domain ortavalkzuwcy.us. Threatened account block and data deletion to harvest payment info. Classic credential/payment phishing. <em>No action needed — already removed.</em><br><br>
      <strong>2. Auto-Trashed — Fake CashApp $2,500 Deposit</strong> <span class="phishing-badge">AUTO-TRASHED</span><br>
      Fake CashApp sender from gibberish domain koig5q.shllix.z1z31j.us. Lured with fake $2,500 deposit and casino scheme. Advance-fee/credential phishing. <em>No action needed — already removed.</em><br><br>
      <strong>3. Auto-Trashed — Explicit Spam (Spoofed melissaw212)</strong> <span class="phishing-badge">AUTO-TRASHED</span><br>
      Spoofed sender using your own username from gibberish domain wh8oo5.x41bof.p3wl7q.us. Malicious spam with explicit content. <em>No action needed — already removed.</em><br><br>
      <strong>4. CarePharmacy — Unsolicited Levitra Spam</strong><br>
      Sender: market@care-script.org · Obfuscated brand name. Unsolicited pharmaceutical spam. Do not click. <span class="warn-badge">DELETE</span><br><br>
      <strong>5. Ozempic by DirectMeds — Unsolicited Pharmaceutical Spam</strong><br>
      Sender: satsupportko@amzycmdmjkdtjeqgtubxkpxf.com · Suspicious domain. Unsolicited GLP-1/weight loss pitch. Do not click. <span class="warn-badge">DELETE</span><br><br>
      <strong>6. HPD Housing Connect — Reminder to Update Information</strong> <span class="warn-badge" style="background:#c6f6d5;color:#276749;">LEGITIMATE — ACT</span><br>
      Sender: HCnotifications@hpd.nyc.gov · Official NYC HPD email. Log in to Housing Connect dashboard to review the message.
      <hr class="divider">
      <div class="rec">📌 Recommendation: Delete pharmaceutical spam immediately. Log in to Housing Connect today. Auto-trashed items require no further action.</div>
    </div>
  </div>

  <!-- JOB SEARCH -->
  <div class="email-category cat-green">
    <div class="email-cat-header">
      🟢 Job Search
      <span class="count-badge">8 emails</span>
    </div>
    <div class="email-cat-body">
      <div class="senders"><strong>Senders:</strong> LinkedIn Job Alerts (3), Glassdoor (1), Greenhouse / Career Team (1), Lisa Rangel / Chameleon Resumes (1), HRJobsRemote.com (1), Melissa's sent outreach to Jade (1)</div>
      <hr class="divider">
      <strong>LinkedIn Alert — CHRO at Confidential Company</strong> · Unread · Inbox · Posted 7/20 → Review &amp; apply today<br>
      <strong>LinkedIn Alert — VP HR at Addition Management ($175K)</strong> · Unread · Inbox · Posted 7/20 → Review &amp; apply today<br>
      <strong>LinkedIn Alert — Senior People BP at Datadog NYC</strong> · In Trash · Unread → Restore if interested<br>
      <strong>Glassdoor — Senior Community Manager + 6 NYC Jobs</strong> · Read · Not in inbox → Low HR fit; skim or ignore<br>
      <strong>Greenhouse — Thank You for Applying to Career Team</strong> · In Trash · Unread → Application confirmed (Senior Director P&amp;C) — restore for records<br>
      <strong>Lisa Rangel — Hidden Executive Roles (newsletter)</strong> · In Trash → Scan article on hidden C-suite roles; useful perspective<br>
      <strong>HRJobsRemote.com — 376 Remote HR Jobs</strong> · In Trash · Unread → Quick skim for VP/CHRO-level roles before deleting<br>
      <strong>Melissa's outreach to Jade re: Contacts</strong> · Sent 7/23 → Follow up Friday if no reply
      <hr class="divider">
      <div class="rec">📌 Recommendation: Prioritize CHRO and VP HR LinkedIn alerts today. Restore Career Team application receipt from trash. Follow up with Jade by Friday.</div>
    </div>
  </div>

  <!-- RECRUITERS / NETWORKING -->
  <div class="email-category cat-green">
    <div class="email-cat-header">
      🤝 Recruiters &amp; Networking
      <span class="count-badge">4 emails</span>
    </div>
    <div class="email-cat-body">
      <div class="senders"><strong>Senders:</strong> LinkedIn (Adam Davison connection), LinkedIn (2 people noticed you), SignalHire (5 credits), Melissa's GitLab outreach draft/sent</div>
      <hr class="divider">
      <strong>Adam Davison (COO/Director) — LinkedIn Connection Request</strong> · Pending → Review profile; accept if strategically relevant<br>
      <strong>LinkedIn — 2 People Noticed You</strong> · Read → Log in to see who viewed your profile<br>
      <strong>SignalHire — 5 New Contact Credits</strong> · Read → Use credits to find contact info for target companies/hiring managers<br>
      <strong>Melissa's GitLab Outreach Note</strong> · Sent — Senior Director role inquiry → Track response; follow up if needed
      <hr class="divider">
      <div class="rec">📌 Recommendation: Review Adam Davison's profile, check LinkedIn profile views, and use SignalHire credits strategically for job search outreach.</div>
    </div>
  </div>

  <!-- CALENDAR / EVENTS -->
  <div class="email-category cat-blue">
    <div class="email-cat-header">
      🔵 Calendar &amp; Events
      <span class="count-badge">2 emails</span>
    </div>
    <div class="email-cat-body">
      <div class="senders"><strong>Senders:</strong> AllEvents.in (event recommendations), Giulia Guerrieri (AI Content Masterclass today)</div>
      <hr class="divider">
      <strong>AllEvents — Events for Melissa (Recommendations)</strong> · Read → Review if any career or networking events are relevant; otherwise ignore<br>
      <strong>Giulia Guerrieri — AI Content System Masterclass (11 AM ET Today)</strong> · Unread · Inbox → Event was today at 11 AM ET. Likely missed unless you acted earlier. Check for recording link.
      <hr class="divider">
      <div class="rec">📌 Recommendation: Check if masterclass recording is available. AllEvents can be reviewed briefly — unsubscribe if not useful.</div>
    </div>
  </div>

  <!-- MEDICAL / HEALTH -->
  <div class="email-category cat-orange">
    <div class="email-cat-header">
      🏥 Medical &amp; Health
      <span class="count-badge">2 emails</span>
    </div>
    <div class="email-cat-body">
      <div class="senders"><strong>Senders:</strong> Warby Parker (vision insurance info), Alison Courses (micro-credentials — not strictly medical but career/health adjacent)</div>
      <hr class="divider">
      <strong>Warby Parker — Vision Insurance 101</strong> · In Trash · Unread → Useful if you need to use vision benefits; restore or review before deleting<br>
      <strong>Alison Courses — Micro-credentials for CV</strong> · Read · Not in inbox → Professional development overlap; low priority
      <hr class="divider">
      <div class="rec">📌 Recommendation: Review Warby Parker vision insurance info if your benefits coverage needs verification. Alison Courses — review if actively pursuing credentials.</div>
    </div>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="email-category cat-yellow">
    <div class="email-cat-header">
      🟡 Financial &amp; Billing
      <span class="count-badge">2 emails</span>
    </div>
    <div class="email-cat-body">
      <div class="senders"><strong>Senders:</strong> Mail Delivery Subsystem (bounce to lizaridgway@yahoo.com), Mercedes-Benz of Manhattan (wrong recipient — "Marvin")</div>
      <hr class="divider">
      <strong>Mail Delivery Subsystem — Delivery Failure to lizaridgway@yahoo.com</strong> · Read · In Inbox → Your sent email bounced; recipient inbox full. If message was important, try an alternate contact method.<br>
      <strong>Mercedes-Benz of Manhattan — Maintenance Offer for "Marvin"</strong> · Unread · Not in inbox → Addressed to "Marvin" — misdirected marketing email. Not relevant to you.
      <hr class="divider">
      <div class="rec">📌 Recommendation: Follow up with Liza Ridgway via a different channel if that message was important. Delete the Mercedes-Benz misdirected email.</div>
    </div>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="email-category cat-purple">
    <div class="email-cat-header">
      🟣 Professional Development
      <span class="count-badge">5 emails</span>
    </div>
    <div class="email-cat-body">
      <div class="senders"><strong>Senders:</strong> AI For Leaders, Ariana Ruiz via LinkedIn, LinkedIn Lindsey, Ladders (HBS Executive Education), Dave D'Angelo via LinkedIn (Barcelona newsletter)</div>
      <hr class="divider">
      <strong>AI For Leaders — "AI Can Make the Wrong Process Faster"</strong> · Unread · Inbox → Relevant leadership insight on AI strategy; worth a quick read<br>
      <strong>Ariana Ruiz (LinkedIn) — "How Do You Know When Your VP Is Competing With You?"</strong> · Unread · Inbox → Useful career navigation content for senior leaders<br>
      <strong>LinkedIn Lindsey — "Do You Need to Be the Loudest to Be Heard?"</strong> · Unread · Inbox → LinkedIn visibility/content strategy — relevant for job search brand building<br>
      <strong>Ladders — HBS Advanced Management Program (Sep–Nov 2026)</strong> · Read → Executive education opportunity; assess ROI vs. cost and timing<br>
      <strong>Dave D'Angelo (LinkedIn) — "Great and Greater" (moving to Barcelona)</strong> · Read → Personal newsletter; low priority
      <hr class="divider">
      <div class="rec">📌 Recommendation: Read AI For Leaders and Ariana Ruiz articles today (job search relevant). HBS program — revisit when employed. Others are low priority reads.</div>
    </div>
  </div>

  <!-- PERSONAL -->
  <div class="email-category cat-blue">
    <div class="email-cat-header">
      💙 Personal
      <span class="count-badge">3 emails</span>
    </div>
    <div class="email-cat-body">
      <div class="senders"><strong>Senders:</strong> Match (Frank profile view), Match (Michael likes you), Tomas from Kickresume (free premium voucher — addressed to "Amy")</div>
      <hr class="divider">
      <strong>Match — Frank (66, Westwood NJ) viewed your profile</strong> · Read → Review profile if interested<br>
      <strong>Match — Michael likes you</strong> · Read → Check mutual interest if you want to connect<br>
      <strong>Kickresume — Free 7-day Premium Voucher (addressed to "Amy")</strong> · Read → Note: addressed to "Amy" not Melissa — may be a misdirected or account-shared email. Check your Kickresume account login.
      <hr class="divider">
      <div class="rec">📌 Recommendation: Check Match notifications at leisure. Kickresume — verify account; the voucher may still be applied automatically on login.</div>
    </div>
  </div>

  <!-- NEWSLETTERS / SUBSCRIPTIONS -->
  <div class="email-category cat-purple">
    <div class="email-cat-header">
      📰 Newsletters &amp; Subscriptions
      <span class="count-badge">7 emails</span>
    </div>
    <div class="email-cat-body">
      <div class="senders"><strong>Senders:</strong> The AI Report, The Average Joe, TLDR Newsletter, 1% Better (in trash), Claude's Notebook (in trash), The Hustle, Medium Daily Digest (MCP is Dead)</div>
      <hr class="divider">
      See full breakdown in <strong>Newsletters &amp; Subscriptions</strong> section below.
      <hr class="divider">
      <div class="rec">📌 Recommendation: Review AI-focused newsletters (AI Report, TLDR, Claude's Notebook) for industry awareness relevant to HR leadership conversations.</div>
    </div>
  </div>

  <!-- PROMOTIONAL / RETAIL -->
  <div class="email-category cat-gray">
    <div class="email-cat-header">
      🛍 Promotional &amp; Retail
      <span class="count-badge">9 emails</span>
    </div>
    <div class="email-cat-body">
      <div class="senders"><strong>Senders:</strong> SHEIN (3 emails), Old Navy, Kohl's, Temu (trash), Quince (trash), YesStyle, Gemma Bonham-Carter</div>
      <hr class="divider">
      See full breakdown in <strong>Promotional / Retail Summary</strong> section below.
      <hr class="divider">
      <div class="rec">📌 Recommendation: Kohl's 40% off ends tonight — only relevant if you need to shop. All others are low priority; batch-delete or unsubscribe.</div>
    </div>
  </div>

  <!-- SAFE TO DELETE / IGNORE -->
  <div class="email-category cat-gray">
    <div class="email-cat-header">
      🗑 Safe to Delete / Ignore
      <span class="count-badge">2 emails</span>
    </div>
    <div class="email-cat-body">
      <div class="senders"><strong>Senders:</strong> CoolDeep AI (in trash — Claude monetization pitch), Medium Daily Digest (ETFs/salary replacement — in trash)</div>
      <hr class="divider">
      <strong>CoolDeep AI — "I spent 10 hours learning Claude into cash!"</strong> · In Trash → Low-quality monetization pitch. Safe to delete permanently.<br>
      <strong>Medium Daily Digest — "Buy These 5 ETFs to Replace Your Salary"</strong> · In Trash → Generic financial clickbait. Safe to delete permanently.
      <hr class="divider">
      <div class="rec">📌 Recommendation: Permanently delete both. No action needed.</div>
    </div>
  </div>

</div>

<!-- ============================================================ TRASH REVIEW -->
<div class="section">
  <div class="section-title"><span class="icon">🗑</span> Trash Review</div>
  <p style="font-size:13px;color:#718096;margin-bottom:16px;">Reviewing all emails marked as trash or auto-trashed. Total in trash/auto-trashed: <strong>13 emails</strong>.</p>

  <div class="trash-group restore">
    <h4>♻️ Restore Immediately (2 emails)</h4>
    <div class="trash-item">
      <span class="sender">Greenhouse / Career Team</span>
      <span class="subj">"Thank you for applying to Career Team" — Senior Director of People &amp; Culture</span>
      <span class="reason">Important application confirmation — restore for your job search records</span>
    </div>
    <div class="trash-item">
      <span class="sender">LinkedIn Job Alerts</span>
      <span class="subj">Senior People Business Partner – NYC at Datadog</span>
      <span class="reason">Relevant HR leadership role — restore and review if interested in tech sector</span>
    </div>
  </div>

  <div class="trash-group review">
    <h4>🔍 Review Before Deleting (4 emails)</h4>
    <div class="trash-item">
      <span class="sender">Warby Parker</span>
      <span class="subj">Vision Insurance 101</span>
      <span class="reason">Contains vision insurance benefit information — useful if you
