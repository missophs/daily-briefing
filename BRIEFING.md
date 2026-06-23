<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa Weiss — June 23, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px 28px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header .sub { font-size: 15px; opacity: 0.75; margin-top: 4px; }
  .header-meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header-meta .stat { background: rgba(255,255,255,0.1); border-radius: 8px; padding: 10px 20px; text-align: center; }
  .header-meta .stat .num { font-size: 22px; font-weight: 700; }
  .header-meta .stat .lbl { font-size: 11px; opacity: 0.7; text-transform: uppercase; letter-spacing: 0.5px; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; letter-spacing: 0.2px; padding: 10px 16px; border-radius: 8px 8px 0 0; margin-bottom: 0; display: flex; align-items: center; gap: 8px; }
  .section-body { background: #fff; border-radius: 0 0 10px 10px; padding: 18px 20px; border: 1px solid #e2e8f0; border-top: none; }

  /* COLOR THEMES */
  .red .section-title    { background: #c0392b; color: #fff; }
  .yellow .section-title { background: #f39c12; color: #fff; }
  .blue .section-title   { background: #2980b9; color: #fff; }
  .green .section-title  { background: #27ae60; color: #fff; }
  .purple .section-title { background: #8e44ad; color: #fff; }
  .gray .section-title   { background: #7f8c8d; color: #fff; }
  .navy .section-title   { background: #1a1a2e; color: #fff; }
  .teal .section-title   { background: #16a085; color: #fff; }
  .orange .section-title { background: #d35400; color: #fff; }

  /* EXEC SUMMARY */
  .exec-bullets { list-style: none; }
  .exec-bullets li { padding: 10px 14px; border-radius: 7px; margin-bottom: 8px; font-size: 14px; display: flex; align-items: flex-start; gap: 10px; }
  .exec-bullets li.risk   { background: #fdecea; border-left: 4px solid #c0392b; }
  .exec-bullets li.oppty { background: #eafaf1; border-left: 4px solid #27ae60; }
  .exec-bullets li.cal   { background: #eaf4fb; border-left: 4px solid #2980b9; }
  .exec-bullets li .icon { font-size: 18px; flex-shrink: 0; margin-top: 1px; }

  /* CARDS */
  .card { border-radius: 9px; padding: 14px 16px; margin-bottom: 12px; border: 1px solid #e0e0e0; background: #fff; }
  .card.red-card    { border-left: 5px solid #c0392b; background: #fff8f8; }
  .card.yellow-card { border-left: 5px solid #f39c12; background: #fffdf0; }
  .card.blue-card   { border-left: 5px solid #2980b9; background: #f4f8fe; }
  .card.green-card  { border-left: 5px solid #27ae60; background: #f4fdf7; }
  .card.purple-card { border-left: 5px solid #8e44ad; background: #faf4fe; }
  .card.gray-card   { border-left: 5px solid #7f8c8d; background: #f9f9f9; }
  .card .card-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; }
  .card.red-card .card-label    { color: #c0392b; }
  .card.yellow-card .card-label { color: #e67e22; }
  .card.blue-card .card-label   { color: #2980b9; }
  .card.green-card .card-label  { color: #27ae60; }
  .card.purple-card .card-label { color: #8e44ad; }
  .card.gray-card .card-label   { color: #7f8c8d; }
  .card h3 { font-size: 15px; font-weight: 700; margin-bottom: 6px; }
  .card .meta { font-size: 12px; color: #666; margin-bottom: 6px; }
  .card .why { font-size: 13px; margin-bottom: 6px; }
  .card .next { font-size: 13px; font-weight: 600; }
  .card .due { font-size: 11px; color: #888; margin-top: 4px; }

  /* TABLE */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  thead tr { background: #f0f2f5; }
  th { padding: 9px 10px; text-align: left; font-weight: 700; font-size: 12px; text-transform: uppercase; letter-spacing: 0.4px; color: #444; border-bottom: 2px solid #d0d4da; }
  td { padding: 8px 10px; border-bottom: 1px solid #eee; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #fafbfc; }

  /* BADGES */
  .badge { display: inline-block; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.4px; }
  .badge-red    { background: #fdecea; color: #c0392b; }
  .badge-yellow { background: #fef9e7; color: #e67e22; }
  .badge-green  { background: #eafaf1; color: #1e8449; }
  .badge-blue   { background: #eaf4fb; color: #1a5276; }
  .badge-gray   { background: #f2f3f4; color: #5d6d7e; }
  .badge-purple { background: #f4ecf7; color: #6c3483; }
  .badge-high   { background: #c0392b; color: #fff; }
  .badge-medium { background: #f39c12; color: #fff; }
  .badge-low    { background: #7f8c8d; color: #fff; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { background: #1a1a2e; color: #fff; padding: 7px 14px; border-radius: 7px; font-weight: 700; font-size: 13px; margin-bottom: 8px; }
  .cal-event { background: #f4f8fe; border-left: 4px solid #2980b9; border-radius: 5px; padding: 10px 14px; margin-bottom: 7px; }
  .cal-event.status-declined { border-left-color: #c0392b; background: #fff8f8; }
  .cal-event.status-needs   { border-left-color: #f39c12; background: #fffdf0; }
  .cal-event.status-confirmed { border-left-color: #27ae60; background: #f4fdf7; }
  .cal-event.status-allday   { border-left-color: #f39c12; background: #fffdf0; }
  .cal-event h4 { font-size: 14px; font-weight: 700; }
  .cal-event .cal-meta { font-size: 12px; color: #555; margin-top: 3px; }
  .cal-event .cal-prep { font-size: 12px; color: #2980b9; margin-top: 3px; }
  .cal-event .cal-warn { font-size: 12px; color: #c0392b; margin-top: 3px; font-weight: 600; }

  /* DASHBOARD */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-card { background: #fff; border-radius: 10px; padding: 16px 18px; border: 1px solid #e2e8f0; }
  .dash-card .dash-num { font-size: 30px; font-weight: 800; }
  .dash-card .dash-lbl { font-size: 12px; color: #666; margin-top: 4px; text-transform: uppercase; letter-spacing: 0.4px; }
  .dash-card.red-d    { border-top: 4px solid #c0392b; }
  .dash-card.yellow-d { border-top: 4px solid #f39c12; }
  .dash-card.green-d  { border-top: 4px solid #27ae60; }
  .dash-card.blue-d   { border-top: 4px solid #2980b9; }
  .dash-card.purple-d { border-top: 4px solid #8e44ad; }
  .dash-card.gray-d   { border-top: 4px solid #7f8c8d; }

  /* PRIORITY TABLE */
  .priority-high td { background: #fff8f8; }
  .priority-medium td { background: #fffdf0; }
  .priority-low td { background: #f9f9f9; }

  /* TOP 3 */
  .top3 { display: flex; gap: 14px; flex-wrap: wrap; }
  .top3-card { flex: 1; min-width: 220px; border-radius: 10px; padding: 18px 20px; }
  .top3-card.t1 { background: linear-gradient(135deg, #c0392b, #e74c3c); color: #fff; }
  .top3-card.t2 { background: linear-gradient(135deg, #27ae60, #2ecc71); color: #fff; }
  .top3-card.t3 { background: linear-gradient(135deg, #2980b9, #3498db); color: #fff; }
  .top3-card .num { font-size: 36px; font-weight: 800; opacity: 0.3; }
  .top3-card h3 { font-size: 16px; font-weight: 700; margin-top: -8px; }
  .top3-card p { font-size: 13px; opacity: 0.9; margin-top: 6px; }

  /* MISC */
  .tag { display: inline-block; background: #e8f0fe; color: #1a73e8; border-radius: 4px; padding: 2px 7px; font-size: 11px; margin: 2px; }
  .note { font-size: 12px; color: #888; font-style: italic; margin-top: 8px; }
  .divider { border: none; border-top: 1px solid #e8eaed; margin: 16px 0; }
  .warning-box { background: #fdecea; border: 1px solid #f5c6cb; border-radius: 7px; padding: 10px 14px; margin-bottom: 10px; color: #c0392b; font-size: 13px; font-weight: 600; }
  .info-box { background: #eaf4fb; border: 1px solid #bee3f8; border-radius: 7px; padding: 10px 14px; margin-bottom: 10px; color: #1a5276; font-size: 13px; }
  ul.bullet { padding-left: 18px; }
  ul.bullet li { margin-bottom: 4px; font-size: 13px; }
  .total-row td { font-weight: 700; background: #f0f2f5; border-top: 2px solid #d0d4da; }

  @media (max-width: 600px) {
    .header { padding: 20px 16px; }
    .header h1 { font-size: 20px; }
    .header-meta { gap: 12px; }
    .top3 { flex-direction: column; }
  }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════════
     SECTION 1 — HEADER
═══════════════════════════════════════════════════════ -->
<div class="header">
  <div class="sub">EXECUTIVE BRIEFING · PREPARED BY YOUR CHIEF OF STAFF</div>
  <h1>Good Morning, Melissa ☀️</h1>
  <div class="sub">Tuesday, June 23, 2026 &nbsp;|&nbsp; New York, NY</div>
  <div class="header-meta">
    <div class="stat"><div class="num">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="stat"><div class="num">8</div><div class="lbl">Calendar Events</div></div>
    <div class="stat"><div class="num">2</div><div class="lbl">🔴 Security Alerts</div></div>
    <div class="stat"><div class="num">7</div><div class="lbl">🟢 Job Leads</div></div>
    <div class="stat"><div class="num">4</div><div class="lbl">📅 Today's Events</div></div>
    <div class="stat"><div class="num">2</div><div class="lbl">🟡 Bills Due</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     SECTION 2 — EXECUTIVE SUMMARY
═══════════════════════════════════════════════════════ -->
<div class="section navy">
  <div class="section-title">📋 Executive Summary</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li class="risk">
        <span class="icon">🔴</span>
        <span><strong>Biggest Risk:</strong> Two phishing/spam emails with your username (melissaw212) spoofed as senders — one claiming your account is blocked, one offering a "$1,000 welcome bonus" from a gambling site. These are active credential-harvesting attempts. Do not click any links. Mark as phishing immediately. Additionally, your Apify platform usage hit 75% of the $60 monthly cap — a cost overrun is imminent if unchecked.</span>
      </li>
      <li class="oppty">
        <span class="icon">🟢</span>
        <span><strong>Biggest Opportunity:</strong> Active job search momentum — you applied to Danaher (Sr. Director, HR Business Partner) today, applied to Glocap Search via LinkedIn, and have a promising LinkedIn lead saved (<em>Job</em> email to yourself). You received a direct deposit of <strong>$760.38</strong> from NYS DOL UI, providing short-term financial runway. The HR Networking Zoom on Jun 24 is a high-value touchpoint worth confirming.</span>
      </li>
      <li class="cal">
        <span class="icon">🔵</span>
        <span><strong>Biggest Calendar Item:</strong> You have <strong>4 events today</strong> — Eye Dr at 9 AM (in progress or just ended), M&amp;M meeting at 1 PM with monte.montoya@gmail.com (confirmed), plus Verizon Fios Bill due today. The HR Networking Zoom on Jun 24 still shows "Needs Action" — RSVP needed. Cobra payment review is due Jun 27 — don't miss it.</span>
      </li>
    </ul>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     SECTION 3 — ACTION REQUIRED
═══════════════════════════════════════════════════════ -->
<div class="section red">
  <div class="section-title">⚡ Action Required</div>
  <div class="section-body">

    <div class="card red-card">
      <div class="card-label">🔴 Security — Phishing</div>
      <h3>Account Blocked Phishing Email</h3>
      <div class="meta">From: melissaw212 &lt;rhdcazbkmqu@mipg.gakdzkbrgdgzu.us&gt; — Spoofed your own username</div>
      <div class="why">⚠️ This is a phishing attack spoofing your Gmail username claiming a "payment issue" with cloud storage and threatening account deletion. Classic credential harvesting. Do NOT click any links.</div>
      <div class="next">→ Mark as phishing in Gmail. Block sender. Do not click any link. Consider enabling Google Advanced Protection.</div>
      <div class="due">Due: Immediately</div>
    </div>

    <div class="card red-card">
      <div class="card-label">🔴 Security — Phishing / Gambling Scam</div>
      <h3>"Claim your $1,000 welcome bonus" — Voltage Bet</h3>
      <div class="meta">From: melissaw212 &lt;ES.hpotsupporteqks@ujcdauydrhrrzwtopifsjhxo.com&gt; — Spoofed your username</div>
      <div class="why">⚠️ Another spoofed sender using your username, promoting a fake gambling registration. This is a scam. Your email address may be on a compromised list.</div>
      <div class="next">→ Mark as phishing. Block sender. Do not engage. Consider changing Gmail password and reviewing login activity.</div>
      <div class="due">Due: Immediately</div>
    </div>

    <div class="card yellow-card">
      <div class="card-label">🟡 Billing — Due Today</div>
      <h3>Verizon Fios Bill Due</h3>
      <div class="meta">Calendar Event — All Day, June 23, 2026</div>
      <div class="why">Bill is due today. No payment confirmation received in inbox.</div>
      <div class="next">→ Log in to Verizon Fios and confirm payment or pay now.</div>
      <div class="due">Due: Today, June 23, 2026</div>
    </div>

    <div class="card yellow-card">
      <div class="card-label">🟡 RSVP Needed</div>
      <h3>HR Networking & Job Search Group — Zoom (Jun 24, 12–1:30 PM)</h3>
      <div class="meta">Calendar: Status = Needs Action | 180+ attendees</div>
      <div class="why">This is a high-value networking call for your job search. Status is unconfirmed. You have a separate "Network" event on the same slot — may be the same event.</div>
      <div class="next">→ RSVP "Accept" on the calendar invitation. Add Zoom link to your calendar. Prepare a 30-second intro and have your resume ready.</div>
      <div class="due">Due: By end of day today (Jun 23) — event is tomorrow</div>
    </div>

    <div class="card yellow-card">
      <div class="card-label">🟡 RSVP Needed</div>
      <h3>HR Networking & Job Search: Open Office Hours — Zoom (Jun 25, 12–1 PM)</h3>
      <div class="meta">Calendar: Status = Needs Action</div>
      <div class="why">Second networking session this week — still pending your RSVP. Open discussion format, no recording allowed.</div>
      <div class="next">→ Review and RSVP. If you plan to attend, confirm by end of today.</div>
      <div class="due">Due: ASAP — event is Thu Jun 25</div>
    </div>

    <div class="card green-card">
      <div class="card-label">🟢 Job Application — Confirm Receipt</div>
      <h3>Danaher — Sr. Director, HR Business Partner (Corporate)</h3>
      <div class="meta">From: Danaher HR &lt;danaher@myworkday.com&gt; — In Trash (review!)</div>
      <div class="why">Application confirmed received. This is a senior-level role that matches your HR leadership background. Email was auto-trashed — rescue it.</div>
      <div class="next">→ Move email from Trash to Inbox. Set a follow-up reminder for 7–10 business days. Research Danaher's HR team on LinkedIn. Prep tailored cover points.</div>
      <div class="due">Follow-up: ~July 2–7, 2026</div>
    </div>

    <div class="card green-card">
      <div class="card-label">🟢 Job Application — Confirm</div>
      <h3>LinkedIn Application Sent to Glocap Search</h3>
      <div class="meta">From: LinkedIn &lt;jobs-noreply@linkedin.com&gt; — In Trash (review!)</div>
      <div class="why">Application confirmation was auto-trashed. Glocap Search is a well-known executive search firm — this is a high-value lead.</div>
      <div class="next">→ Restore from Trash. Log application. Research the specific role. Consider connecting with Glocap recruiters on LinkedIn directly.</div>
      <div class="due">Follow-up: Within 5 business days</div>
    </div>

    <div class="card green-card">
      <div class="card-label">🟢 Job Lead — Self-Saved</div>
      <h3>LinkedIn Job Saved: Job ID 4427764308</h3>
      <div class="meta">From: Melissa W &lt;melissaw212@gmail.com&gt; — In Inbox</div>
      <div class="why">You emailed yourself a LinkedIn job link — this means you flagged it as interesting. You haven't yet reviewed or applied.</div>
      <div class="next">→ Open the LinkedIn link. Review the posting. Apply today if it's a strong fit.</div>
      <div class="due">Due: Today</div>
    </div>

    <div class="card yellow-card">
      <div class="card-label">🟡 Financial — Direct Deposit</div>
      <h3>Bank of America — Direct Deposit $760.38 (NYS DOL UI)</h3>
      <div class="meta">From: Bank of America &lt;onlinebanking@ealerts.bankofamerica.com&gt;</div>
      <div class="why">Unemployment insurance direct deposit received. Important for budgeting and tracking benefit status.</div>
      <div class="next">→ Log this deposit. Confirm UI claim is current and next certification date. Budget accordingly.</div>
      <div class="due">Received today — no action deadline but log promptly</div>
    </div>

    <div class="card yellow-card">
      <div class="card-label">🟡 Financial — Trade Confirmations</div>
      <h3>Merrill Edge + Robinhood — New Trade Confirmations</h3>
      <div class="meta">Merrill Edge (04:46 AM) + Robinhood (08:01 AM)</div>
      <div class="why">Two trade confirmations received this morning. Review to confirm accuracy and tax implications.</div>
      <div class="next">→ Log into both Merrill Edge and Robinhood. Review trade details. Save confirmations for tax records.</div>
      <div class="due">Review by end of day</div>
    </div>

    <div class="card yellow-card">
      <div class="card-label">🟡 Billing — Anthropic Subscription</div>
      <h3>Anthropic Receipt #2816-9498-5487</h3>
      <div class="meta">From: Anthropic, PBC &lt;invoice+statements@mail.anthropic.com&gt;</div>
      <div class="why">Subscription charge processed. Verify amount is correct and expected.</div>
      <div class="next">→ Open receipt and confirm charge amount. Save for expense records.</div>
      <div class="due">Today</div>
    </div>

    <div class="card yellow-card">
      <div class="card-label">🟡 Platform Usage — Apify Near Limit</div>
      <h3>Apify Usage at 75% of $60 Monthly Cap</h3>
      <div class="meta">From: Apify &lt;hello@apify.com&gt; — In Trash (restore!)</div>
      <div class="why">Your pipeline tests are consuming Apify credits fast. At this rate, you'll hit $60 before month-end, triggering overages. This email was incorrectly trashed.</div>
      <div class="next">→ Restore from Trash. Log into Apify. Review which actors/runs are consuming credits. Pause non-essential runs. Consider upgrading plan if pipeline is production-critical.</div>
      <div class="due">Immediate — before hitting 100%</div>
    </div>

    <div class="card blue-card">
      <div class="card-label">🔵 Technical — Pipeline Test</div>
      <h3>[NEW PIPELINE TEST] HR Search — 2026-06-23 (3 instances)</h3>
      <div class="meta">From: melissaw212@gmail.com — Inbox &amp; Trash</div>
      <div class="why">Your TypeScript parallel-build HR Search pipeline sent 3 test emails to yourself. The pipeline is not yet wired into the live schedule. Multiple sends suggest retry loops or duplicate triggers.</div>
      <div class="next">→ Review pipeline logs. Investigate why 3 identical emails were sent. Verify deduplication logic before going live. Archive old test emails.</div>
      <div class="due">Before next scheduled pipeline run</div>
    </div>

    <div class="card yellow-card">
      <div class="card-label">🟡 Calendar — Today</div>
      <h3>M&M Meeting — 1:00–2:00 PM Today</h3>
      <div class="meta">Calendar: Confirmed | Attendee: monte.montoya@gmail.com</div>
      <div class="why">Meeting confirmed for 1 PM with Monte Montoya. No location or agenda provided in calendar entry.</div>
      <div class="next">→ Confirm meeting format (virtual/in-person). Prepare any relevant discussion points. Reach out to Monte if agenda is unclear.</div>
      <div class="due">Today at 1:00 PM</div>
    </div>

    <div class="card yellow-card">
      <div class="card-label">🟡 Health Insurance</div>
      <h3>COBRA Payment Check Due Jun 27</h3>
      <div class="meta">Calendar: Confirmed | Jun 27, 10:00–11:00 AM</div>
      <div class="why">COBRA health coverage continuity depends on timely payments. This reminder is 4 days away.</div>
      <div class="next">→ Log into your COBRA portal. Confirm payment status. Schedule payment if due.</div>
      <div class="due">June 27, 2026</div>
    </div>

    <div class="card blue-card">
      <div class="card-label">🔵 Calendar — Declined Event</div>
      <h3>Executive Roundtable — Jun 25, 9–10:30 AM (DECLINED)</h3>
      <div class="meta">Organizer: John Madigan | Zoom | Status: Declined</div>
      <div class="why">You have declined this event. Given your active job search, executive roundtables can be high-value networking — worth reconsidering.</div>
      <div class="next">→ Review why you declined. If circumstances changed, consider reversing RSVP. The event is 2 days away.</div>
      <div class="due">Jun 25 at 9:00 AM</div>
    </div>

    <div class="card purple-card">
      <div class="card-label">🟣 Community Alert</div>
      <h3>Lost Cat "Misty" — Near Chauncey St &amp; Bushwick Ave</h3>
      <div class="meta">From: HomeAgain PetRescuers | Ref. ID: HAP-1872388</div>
      <div class="why">A neighbor's cat is missing near your area. This is a community alert — worth being aware of.</div>
      <div class="next">→ Keep an eye out if you're in that neighborhood. Optional: share on Nextdoor.</div>
      <div class="due">Non-urgent</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     SECTION 4 — FULL 7-DAY CALENDAR
═══════════════════════════════════════════════════════ -->
<div class="section blue">
  <div class="section-title">📅 Full 7-Day Calendar (Jun 23 – Jun 29, 2026)</div>
  <div class="section-body">

    <!-- TUESDAY JUN 23 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Tuesday, June 23, 2026 — TODAY</div>

      <div class="cal-event status-allday">
        <h4>💳 Verizon Fios Bill — ALL DAY</h4>
        <div class="cal-meta">Status: Confirmed | No location | Billing deadline</div>
        <div class="cal-prep">⚡ Action: Log in to Verizon Fios and pay or confirm autopay has processed.</div>
      </div>

      <div class="cal-event status-confirmed">
        <h4>👁️ Eye Dr — 9:00 AM – 10:00 AM</h4>
        <div class="cal-meta">Status: Confirmed | No location specified | Solo event</div>
        <div class="cal-prep">🔵 Prep: Confirm appointment address/location. Bring insurance card. This appointment may already be underway.</div>
      </div>

      <div class="cal-event status-confirmed">
        <h4>🤝 M&amp;M Meeting — 1:00 PM – 2:00 PM</h4>
        <div class="cal-meta">Status: Accepted | Attendee: monte.montoya@gmail.com | No location or agenda</div>
        <div class="cal-prep">🔵 Prep: Confirm virtual vs. in-person. Prepare agenda. No link in calendar — confirm meeting format with Monte.</div>
        <div class="cal-warn">⚠️ No location or Zoom link — confirm with Monte before meeting.</div>
      </div>
    </div>

    <!-- WEDNESDAY JUN 24 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Wednesday, June 24, 2026</div>

      <div class="cal-event status-needs">
        <h4>🌐 HR Networking &amp; Job Search Group — Zoom 2 — 12:00 PM – 1:30 PM</h4>
        <div class="cal-meta">Status: ⚠️ NEEDS ACTION (RSVP Required) | 180+ attendees</div>
        <div class="cal-meta">Zoom: https://us06web.zoom.us/j/81954171722</div>
        <div class="cal-prep">🔵 Prep: RSVP today. Prepare 30-second professional intro. Review HR Networking Team Guidelines linked in event description. Have resume ready.</div>
        <div class="cal-warn">⚠️ RSVP PENDING — Confirm attendance immediately.</div>
      </div>

      <div class="cal-event status-confirmed">
        <h4>🌐 Network — 12:00 PM – 1:30 PM</h4>
        <div class="cal-meta">Status: Confirmed | No location | Solo event (likely same as above)</div>
        <div class="cal-warn">⚠️ Potential duplicate of HR Networking Zoom above — same time slot. Confirm these are not two separate meetings requiring split attention.</div>
        <div class="cal-prep">🔵 Prep: If this is a separate event, clarify. If same, no duplicate prep needed.</div>
      </div>
    </div>

    <!-- THURSDAY JUN 25 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Thursday, June 25, 2026</div>

      <div class="cal-event status-declined">
        <h4>🎙️ Executive Roundtable — 9:00 AM – 10:30 AM (DECLINED)</h4>
        <div class="cal-meta">Status: ❌ DECLINED | Organizer: John Madigan | Zoom</div>
        <div class="cal-meta">Zoom: https://us02web.zoom.us/j/207786667 | PW: 205454</div>
        <div class="cal-prep">🔵 Consideration: Given active job search, executive roundtables = high-value networking. Consider reversing decline before Jun 25.</div>
        <div class="cal-warn">⚠️ You declined — reconsider if this aligns with your job search networking goals.</div>
      </div>

      <div class="cal-event status-needs">
        <h4>🌐 HR Networking &amp; Job Search: Open Office Hours — Zoom 2 — 12:00 PM – 1:00 PM</h4>
        <div class="cal-meta">Status: ⚠️ NEEDS ACTION | 180+ attendees</div>
        <div class="cal-meta">Zoom: https://us06web.zoom.us/j/85945371140</div>
        <div class="cal-prep">🔵 Prep: RSVP today. No AI notetaking tools per event description. Open discussion format — come with a question or update.</div>
        <div class="cal-warn">⚠️ RSVP PENDING.</div>
      </div>
    </div>

    <!-- FRIDAY JUN 26 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Friday, June 26, 2026</div>
      <div class="info-box">No calendar events scheduled for Friday, June 26.</div>
    </div>

    <!-- SATURDAY JUN 27 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Saturday, June 27, 2026</div>

      <div class="cal-event status-confirmed">
        <h4>🏥 Check COBRA Payments — 10:00 AM – 11:00 AM</h4>
        <div class="cal-meta">Status: Confirmed | No location | Solo task</div>
        <div class="cal-prep">🔵 Prep: Log into your COBRA portal before this time block. Have your insurance documents ready. Confirm payment amount and due date.</div>
      </div>
    </div>

    <!-- SUNDAY JUN 28 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Sunday, June 28, 2026</div>
      <div class="info-box">No calendar events scheduled for Sunday, June 28.</div>
    </div>

    <!-- MONDAY JUN 29 -->
    <div class="cal-day">
      <div class="cal-day-header">📅 Monday, June 29, 2026</div>
      <div class="info-box">No calendar events scheduled for Monday, June 29.</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     SECTION 5 — JOB SEARCH & INTERVIEW PIPELINE
═══════════════════════════════════════════════════════ -->
<div class="section green">
  <div class="section-title">🟢 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">

    <table>
      <thead>
        <tr>
          <th>Fit</th>
          <th>Company / Role</th>
          <th>Source</th>
          <th>Status</th>
          <th>Next Step</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="badge badge-high">HIGH</span></td>
          <td><strong>Danaher</strong><br>Senior Director, HR Business Partner (Corporate)</td>
          <td>Workday / Direct Apply</td>
          <td><span class="badge badge-green">Applied ✓</span><br>Confirmation received (in Trash)</td>
          <td>Restore confirmation email. Follow up in 7–10 business days. Research Danaher CHRO on LinkedIn.</td>
        </tr>
        <tr>
          <td><span class="badge badge-high">HIGH</span></td>
          <td><strong>Glocap Search</strong><br>Role not specified</td>
          <td>LinkedIn Easy Apply</td>
          <td><span class="badge badge-green">Applied ✓</span><br>Confirmation in Trash</td>
          <td>Restore confirmation email. Glocap is an executive search firm — connect with their recruiters directly on LinkedIn.</td>
        </tr>
        <tr>
          <td><span class="badge badge-high">HIGH</span></td>
          <td><strong>LinkedIn Job #4427764308</strong><br>Role not specified (self-saved)</td>
          <td>Self-email (melissaw212)</td>
          <td><span class="badge badge-yellow">Saved — Not Applied</span></td>
          <td>Open link today. Review posting. Apply if strong fit. Time-sensitive.</td>
        </tr>
        <tr>
          <td><span class="badge badge-high">HIGH</span></td>
          <td><strong>Ladders</strong><br>VP, People Business Partners &amp; Talent Development</td>
          <td>LinkedIn Job Alert</td>
          <td><span class="badge badge-yellow">Unreviewed — Posted 6/17</span></td>
          <td>Review posting immediately. VP-level role in your field — high relevance. Apply before it closes.</td>
        </tr>
        <tr>
          <td><span class="badge badge-medium">MED</span></td>
          <td><strong>Intuvia Technologies</strong><br>Talent Acquisition Coordinator / HR Coordinator (Onsite NYC)</td>
          <td>PostJobFree / Dennis Gorelik</td>
          <td><span class="badge badge-gray">Unreviewed</span></td>
          <td>Review role — fully onsite at NYC 10020. May be below target level but worth evaluating for fit.</td>
        </tr>
        <tr>
          <td><span class="badge badge-medium">MED</span></td>
          <td><strong>Inclusively</strong><br>Multiple recommended jobs</td>
          <td>Inclusively.com email</td>
          <td><span class="badge badge-gray">Unreviewed</span></td>
          <td>Log into Inclusively and review personalized job recommendations. Flag relevant roles.</td>
        </tr>
        <tr>
          <td><span class="badge badge-medium">MED</span></td>
          <td><strong>Keith Bogen Group — HR Job Leads</strong><br>Multiple roles (see Trash Review)</td>
          <td>groups.io / PayItForwardHRJobLeads</td>
          <td><span class="badge badge-gray">In Trash — Unreviewed</span></td>
          <td>Restore from Trash and review. Multiple roles including: HR Director FL, HRIS Payroll Mgr (Remote), Payroll &amp; HR Specialist NYC, HR Contract NJ/CT, Sr. Compensation Analyst NJ. Several NYC/NJ roles are relevant.</td>
        </tr>
      </tbody>
    </table>

    <hr class="divider">
    <h4 style="margin-bottom:10px; color:#27ae60;">📅 Networking Events This Week</h4>
    <table>
      <thead>
        <tr><th>Date</th><th>Event</th><th>Format</th><th>RSVP Status</th><th>Priority</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Jun 24</td>
          <td>HR Networking &amp; Job Search Group — Zoom 2</td>
          <td>Zoom | 180+ Attendees</td>
          <td><span class="badge badge-yellow">Needs Action</span></td>
          <td><span class="badge badge-high">HIGH</span></td>
        </tr>
        <tr>
          <td>Jun 25</td>
          <td>HR Networking &amp; Job Search: Open Office Hours</td>
          <td>Zoom | Open Discussion</td>
          <td><span class="badge badge-yellow">Needs Action</span></td>
          <td><span class="badge badge-high">HIGH</span></td>
        </tr>
        <tr>
          <td>Jun 25</td>
          <td>Executive Roundtable (John Madigan)</td>
          <td>Zoom</td>
          <td><span class="badge badge-red">Declined</span></td>
          <td><span class="badge badge-medium">MED — Reconsider</span></td>
        </tr>
        <tr>
          <td>Jun 26</td>
          <td>PSG of Mercer County — Summer BYO Networking Picnic</td>
          <td>In-Person, Plainsboro NJ</td>
          <td><span class="badge badge-gray">In Trash — Unreviewed</span></td>
          <td><span class="badge badge-medium">MED</span></td>
        </tr>
      </tbody>
    </table>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     SECTION 6 — FULL EMAIL REVIEW BY CATEGORY
═══════════════════════════════════════════════════════ -->
<div class="section navy">
  <div class="section-title">📧 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="card red-card">
      <div class="card-label">🔴 Security / Risk — 2 Emails</div>
      <h3>Phishing / Scam Emails</h3>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Risk Level</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td>melissaw212 &lt;rhdcazbkmqu@mipg.gakdzkbrgdgzu.us&gt;</td>
            <td>Your Account Has been Blocked! Photos/Videos removed Mon 22-Jun</td>
            <td><span class="badge badge-red">CRITICAL</span></td>
            <td>Mark as phishing. Block.</td>
          </tr>
          <tr>
            <td>melissaw212 &lt;ES.hpotsupporteqks@ujcdauydrhrrzwtopifsjhxo.com&gt;</td>
            <td>Claim your $1000 welcome bonus — Voltage Bet</td>
            <td><span class="badge badge-red">CRITICAL</span></td>
            <td>Mark as phishing. Block.</td>
          </tr>
        </tbody>
      </table>
      <div class="note">Both emails spoof your Gmail username. Your email may be on a compromised marketing list. Do not click any links. Change password as a precaution.</div>
    </div>

    <!-- JOB SEARCH -->
    <div class="card green-card">
      <div class="card-label">🟢 Job Search — 5 Emails</div>
      <h3>Applications, Leads &amp; Self-Saved Jobs</h3>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td>Danaher HR (Workday)</td>
            <td>Application Received — Sr. Director, HRBP Corporate</td>
            <td><span class="badge badge-green">Applied ✓</span> — In Trash</td>
            <td>Restore. Log. Follow up Jul 2–7.</td>
          </tr>
          <tr>
            <td>LinkedIn</td>
            <td>Application sent to Glocap Search</td>
            <td><span class="badge badge-green">Applied ✓</span> — In Trash</td>
            <td>Restore. Research role. Follow up.</td>
          </tr>
          <tr>
            <td>Melissa W (self)</td>
            <td>Job — LinkedIn link #4427764308</td>
            <td><span class="badge badge-yellow">Saved — Review</span></td>
            <td>Open and apply today if fit.</td>
          </tr>
          <tr>
            <td>LinkedIn</td>
            <td>Ladders hiring VP, People Business Partners &amp; Talent Dev</td>
            <td><span class="badge badge-yellow">Unreviewed</span></td>
            <td>Apply before deadline. High-fit role.</td>
          </tr>
          <tr>
            <td>Dennis Gorelik / PostJobFree</td>
            <td>Intuvia Technologies — Talent Acquisition Coordinator NYC</td>
            <td><span class="badge badge-yellow">Unreviewed</span></td>
            <td>Review for fit. Fully onsite NYC.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- RECRUITERS / NETWORKING -->
    <div class="card green-card">
      <div class="card-label">🟢 Recruiters / Networking — 2 Emails</div>
      <h3>Job Network Groups &amp; Recommendations</h3>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td>Inclusively</td>
            <td>melissa weiss — Check out these recommended jobs for you!</td>
            <td>Log in and review personalized job matches.</td>
          </tr>
          <tr>
            <td>LinkedIn</td>
            <td>New jobs similar to HRBP at BBG Ventures</td>
            <td>In Trash — Restore if unreviewed. Check similar postings.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- CALENDAR / EVENTS -->
    <div class="card blue-card">
      <div class="card-label">🔵 Calendar / Events — 1 Email</div>
      <h3>HR Networking Group Updates</h3>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td>David Schuchman via groups.io</td>
            <td>PSG of Mercer County Meeting (06/26): Annual Summer BYO Networking Picnic — In Trash</td>
            <td>Restore and review. In-person networking event Jun 26 in Plainsboro NJ. Relevant if you're near the area.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- MEDICAL / HEALTH -->
    <div class="card purple-card">
      <div class="card-label">🟣 Medical / Health — 1 Email</div>
      <h3>Women's Health Newsletter</h3>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td>Dr Gazala Shaikh via Medium</td>
            <td>Walking Is Not Enough: Reasons We Are Missing Women's Health Needs</td>
            <td>Read when time allows. Health-relevant content about strength training for women.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="card yellow-card">
      <div class="card-label">🟡 Financial / Billing — 4 Emails</div>
      <h3>Banking, Investments &amp; Subscriptions</h3>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td>Bank of America</td>
            <td>Direct deposit credited — $760.38 from NYS DOL UI (Jun 23)</td>
            <td>Log deposit. Confirm UI certification is current.</td>
          </tr>
          <tr>
            <td>Merrill Edge</td>
            <td>New trade confirmation available</td>
            <td>Log in and review trade details. Save for tax records.</td>
          </tr>
          <tr>
            <td>Robinhood</td>
            <td>Your trade confirmations are available</td>
            <td>Log in and review. Save for records.</td>
          </tr>
          <tr>
            <td>Anthropic, PBC</td>
            <td>Receipt #2816-9498-5487</td>
            <td>Verify charge. Save receipt for expense tracking.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="card purple-card">
      <div class="card-label">🟣 Professional Development — 2 Emails</div>
      <h3>HR Tools, Benchmarking &amp; Tech Learning</h3>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td>BambooHR</td>
            <td>💡 Turn Market Data Into Better Pay Decisions</td>
            <td>Review benchmarking guide — useful for comp strategy knowledge in interviews.</td>
          </tr>
          <tr>
            <td>CoolDeep AI</td>
            <td>Are you using ChatGPT like an autocorrect tool?</td>
            <td>Read when time allows. May contain useful AI productivity tips.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- PERSONAL -->
    <div class="card gray-card">
      <div class="card-label">⚫ Personal — 3 Emails</div>
      <h3>OkCupid, Community (Nextdoor), Lost Pet</h3>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td>OkCupid</td>
            <td>"Someone likes you" (×2 — Jun 22 &amp; Jun 23)</td>
            <td>Review at leisure. Low priority for this briefing.</td>
          </tr>
          <tr>
            <td>HomeAgain PetRescuers</td>
            <td>Misty, a lost Cat, missing — near Chauncey St &amp; Bushwick Ave</td>
            <td>Be aware. Share locally if near that area.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- TECHNICAL / PIPELINE -->
    <div class="card blue-card">
      <div class="card-label">🔵 Technical / Pipeline — 3 Emails</div>
      <h3>Self-Sent Pipeline Test Emails</h3>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Location</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td>melissaw212@gmail.com</td>
            <td>[NEW PIPELINE TEST] HR Search — 2026-06-23 (03:27 AM)</td>
            <td>Inbox</td>
            <td>Review. Note: "not yet wired into live schedule."</td>
          </tr>
          <tr>
            <td>melissaw212@gmail.com</td>
            <td>[NEW PIPELINE TEST] HR Search — 2026-06-23 (02:42 AM)</td>
            <td>Inbox</td>
            <td>Duplicate send — investigate retry logic.</td>
          </tr>
          <tr>
            <td>melissaw212@gmail.com</td>
            <td>[NEW PIPELINE TEST] HR Search — 2026-06-23 (01:55 AM)</td>
            <td>Trash</td>
            <td>Third duplicate — fix dedup before going live.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- NEWSLETTERS / SUBSCRIPTIONS -->
    <div class="card purple-card">
      <div class="card-label">🟣 Newsletters / Subscriptions — 2 Emails</div>
      <h3>Medium, Nextdoor Community</h3>
      <table>
        <thead><tr><th>From</th><th>Topic</th><th>Recommendation</th></tr></thead>
        <tbody>
          <tr>
            <td>Medium (Dr. Gazala Shaikh)</td>
            <td>Women's health — strength training</td>
            <td>Keep — useful personal health content</td>
          </tr>
          <tr>
            <td>Nextdoor — Free Items (Yorkville E83st)</td>
            <td>100+ free items from neighbors incl. Black Sofa Bed</td>
            <td>Review if you need home items — otherwise ignore</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- GOOGLE NOTIFICATIONS -->
    <div class="card gray-card">
      <div class="card-label">⚫ Google Notifications — 3 Emails (All in Trash)</div>
      <h3>Google Privacy Settings Updates</h3>
      <table>
        <thead><tr><th>Account</th><th>Date</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td>melweiss212@gmail.com</td>
            <td>Jun 22 (Trash)</td>
            <td>Review privacy settings at your convenience. Safe to delete after review.</td>
          </tr>
          <tr>
            <td>stellbell212@hotmail.com</td>
            <td>Jun 22 (Trash)</td>
            <td>Different account — confirm this is your Hotmail. Review settings.</td>
          </tr>
          <tr>
            <td>swm3016@gmail.com</td>
            <td>Jun 22 (Trash)</td>
            <td>Different account — confirm ownership. Review.</td>
          </tr>
        </tbody>
      </table>
      <div class="note">Note: Three different email accounts receiving Google privacy updates — confirm all accounts are yours and secure.</div>
    </div>

    <!-- PROMOTIONAL / RETAIL -->
    <div class="card gray-card">
      <div class="card-label">⚫ Promotional / Retail — 12 Emails</div>
      <h3>Retail &amp; Shopping Promotions (see full breakdown in Section 8)</h3>
      <div class="note">Includes: SHEIN (×2), Kohl's, Best Buy/Citi, YesStyle, Macy's, Gap Factory, Temu, NYC Singles (Nextdoor), Nextdoor Trending Posts. All grouped in Section 8 below.</div>
    </div>

    <!-- APIFY -->
    <div class="card yellow-card">
      <div class="card-label">🟡 Platform Billing — 1 Email (Trash)</div>
      <h3>Apify — Usage Alert (75% of $60 cap)</h3>
      <div class="note">In Trash — restore immediately. Action required before overages hit. See Action Required section.</div>
    </div>

    <!-- SAFE TO DELETE -->
    <div class="card gray-card">
      <div class="card-label">⚫ Safe to Delete / Ignore — 8 Emails</div>
      <h3>Keith Bogen Job Leads (Trash — Out of Target)</h3>
      <div class="note">8 Keith Bogen group job leads auto-trashed — includes roles in LA, Stamford CT, CA Central Valley, Edison NJ, Piscataway NJ, Lakeland FL. Most are outside NYC/NJ target area or below target level. Review briefly, then delete. See full Trash Review in Section 7.</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     SECTION 7 — TRASH REVIEW
═══════════════════════════════════════════════════════ -->
<div class="section red">
  <div class="section-title">🗑️ Trash Review (18 Emails in Trash)</div>
  <div class="section-body">

    <div class="warning-box">⚠️ 18 emails are in Gmail Trash. Review before permanent deletion. Several contain important career and financial information.</div>

    <h4 style="color:#c0392b; margin-bottom:10px;">🔴 RESTORE IMMEDIATELY — 5 Emails</h4>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Why Restore</th></tr></thead>
      <tbody>
        <tr>
          <td>Danaher HR (Workday)</td>
          <td>Application Received — Sr. Director, HR Business Partner</td>
          <td><strong>Active job application confirmation.</strong> Must keep for records and follow-up tracking.</td>
        </tr>
        <tr>
          <td>LinkedIn</td>
          <td>Application sent to Glocap Search</td>
          <td><strong>Active job application confirmation.</strong> Executive search firm — high-value lead.</td>
        </tr>
        <tr>
          <td>Apify</td>
          <td>You're getting through your platform usage fast (75% of $60 cap)</td>
          <td><strong>Billing alert — immediate action needed</strong> to prevent overages on your pipeline.</td>
        </tr>
        <tr>
          <td>melissaw212@gmail.com</td>
          <td>[NEW PIPELINE TEST] HR Search — 2026-06-23 (01:55 AM)</td>
          <td><strong>Your own technical pipeline email</strong> — review for debugging duplicate send issue.</td>
        </tr>
        <tr>
          <td>LinkedIn</td>
          <td>New jobs similar to HRBP at BBG Ventures</td>
          <td><strong>Job search intelligence</strong> — may contain relevant leads matching recent application.</td>
        </tr>
      </tbody>
    </table>

    <hr class="divider">
    <h4 style="color:#e67e22; margin-bottom:10px;">🟡 REVIEW BEFORE DELETING — 7 Emails</h4>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Why Review</th></tr></thead>
      <tbody>
        <tr>
          <td>David Schuchman via groups.io</td>
          <td>PSG of Mercer County Meeting 06/26 — Summer Networking Picnic</td>
          <td>In-person HR networking event Jun 26 in Plainsboro. May be worth attending during job search.</td>
        </tr>
        <tr>
          <td>Keith Bogen via groups.io</td>
<hr>
<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Financial / Billing</td><td>2</td></tr>
<tr><td>Job Search / Recruiters</td><td>18</td></tr>
<tr><td>Medical / Health</td><td>2</td></tr>
<tr><td>Other / Review</td><td>19</td></tr>
<tr><td>Professional Development / Newsletters</td><td>1</td></tr>
<tr><td>Promotional / Retail</td><td>4</td></tr>
<tr><td>Security / Risk</td><td>4</td></tr>
</table>
<p><strong>Audit Note:</strong> Every fetched email was reviewed and assigned to one category. Trash emails were included in review. Promotional and low-value emails were accounted for but deprioritized.</p>

