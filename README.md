<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa Weiss — July 27, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 2rem; font-weight: 700; letter-spacing: 1px; }
  .header .sub { font-size: 1.05rem; color: #a8c8f8; margin-top: 6px; }
  .header .meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.08); border-radius: 8px; padding: 8px 18px; }
  .header .meta-item span { display: block; font-size: 0.75rem; color: #90b4e0; text-transform: uppercase; letter-spacing: 1px; }
  .header .meta-item strong { font-size: 1.15rem; color: #fff; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 1.1rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 10px 18px; border-radius: 8px 8px 0 0; color: #fff; }
  .section-body { background: #fff; border-radius: 0 0 10px 10px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }

  /* COLOR BANDS */
  .band-red { background: #c0392b; }
  .band-yellow { background: #d4a017; }
  .band-blue { background: #2471a3; }
  .band-green { background: #1e8449; }
  .band-purple { background: #6c3483; }
  .band-gray { background: #5d6d7e; }
  .band-teal { background: #117a65; }
  .band-dark { background: #1a1a2e; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #f4f6f8; text-align: left; padding: 9px 12px; font-weight: 700; color: #444; border-bottom: 2px solid #dee2e6; }
  td { padding: 8px 12px; border-bottom: 1px solid #eee; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #fafbfc; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 18px; margin-bottom: 14px; border-left: 5px solid; }
  .card-red { background: #fdf3f3; border-color: #c0392b; }
  .card-yellow { background: #fefcf0; border-color: #d4a017; }
  .card-blue { background: #f0f6fb; border-color: #2471a3; }
  .card-green { background: #f0faf4; border-color: #1e8449; }
  .card-purple { background: #f8f0fe; border-color: #6c3483; }
  .card-gray { background: #f8f9fa; border-color: #adb5bd; }
  .card-teal { background: #f0faf8; border-color: #117a65; }
  .card h3 { font-size: 0.95rem; font-weight: 700; margin-bottom: 6px; }
  .card p { font-size: 0.88rem; color: #444; margin-bottom: 4px; }
  .card .label { font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; padding: 2px 8px; border-radius: 20px; display: inline-block; margin-bottom: 6px; }
  .label-red { background: #fde8e8; color: #c0392b; }
  .label-yellow { background: #fef9e7; color: #b7770d; }
  .label-blue { background: #eaf4fb; color: #2471a3; }
  .label-green { background: #eafaf1; color: #1e8449; }
  .label-purple { background: #f5eef8; color: #6c3483; }
  .label-gray { background: #f2f3f4; color: #5d6d7e; }

  /* BADGES */
  .badge { display: inline-block; padding: 2px 10px; border-radius: 20px; font-size: 0.72rem; font-weight: 700; text-transform: uppercase; }
  .badge-high { background: #fde8e8; color: #c0392b; }
  .badge-medium { background: #fef9e7; color: #b7770d; }
  .badge-low { background: #f2f3f4; color: #5d6d7e; }
  .badge-green { background: #eafaf1; color: #1e8449; }
  .badge-blue { background: #eaf4fb; color: #2471a3; }
  .badge-purple { background: #f5eef8; color: #6c3483; }
  .badge-red { background: #fde8e8; color: #c0392b; }
  .badge-yellow { background: #fef9e7; color: #b7770d; }
  .badge-gray { background: #f2f3f4; color: #5d6d7e; }

  /* EXEC SUMMARY */
  .exec-bullets { list-style: none; }
  .exec-bullets li { padding: 12px 16px; margin-bottom: 10px; border-radius: 8px; font-size: 0.95rem; line-height: 1.5; }
  .exec-bullets li::before { font-size: 1.1rem; margin-right: 8px; }
  .exec-red { background: #fdf3f3; border-left: 4px solid #c0392b; }
  .exec-green { background: #f0faf4; border-left: 4px solid #1e8449; }
  .exec-blue { background: #f0f6fb; border-left: 4px solid #2471a3; }

  /* TRIAGE TABLE */
  .status-rescued { color: #1e8449; font-weight: 700; }
  .status-inbox { color: #2471a3; font-weight: 700; }
  .status-auto { color: #c0392b; font-weight: 700; }
  .status-trash { color: #5d6d7e; font-weight: 700; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: #2471a3; border-bottom: 2px solid #2471a3; padding-bottom: 4px; margin-bottom: 10px; }
  .cal-event { background: #f0f6fb; border-left: 4px solid #2471a3; border-radius: 6px; padding: 10px 14px; margin-bottom: 8px; }
  .cal-event.declined { border-color: #adb5bd; background: #f8f9fa; opacity: 0.75; }
  .cal-event.needs-action { border-color: #d4a017; background: #fefcf0; }
  .cal-event.green-event { border-color: #1e8449; background: #f0faf4; }
  .cal-event h4 { font-size: 0.92rem; font-weight: 700; margin-bottom: 4px; }
  .cal-event p { font-size: 0.82rem; color: #555; margin-bottom: 2px; }
  .cal-event a { color: #2471a3; word-break: break-all; font-size: 0.8rem; }

  /* DASHBOARD GRID */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }
  .dash-card { border-radius: 10px; padding: 16px; color: #fff; }
  .dash-card h4 { font-size: 0.78rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; opacity: 0.85; }
  .dash-card .num { font-size: 2rem; font-weight: 700; }
  .dash-card .detail { font-size: 0.8rem; margin-top: 6px; opacity: 0.9; line-height: 1.4; }
  .dc-red { background: linear-gradient(135deg,#c0392b,#e74c3c); }
  .dc-green { background: linear-gradient(135deg,#1e8449,#27ae60); }
  .dc-blue { background: linear-gradient(135deg,#1a5276,#2471a3); }
  .dc-yellow { background: linear-gradient(135deg,#b7770d,#d4a017); }
  .dc-purple { background: linear-gradient(135deg,#5b2c6f,#8e44ad); }
  .dc-gray { background: linear-gradient(135deg,#4a5568,#718096); }

  /* ACCOUNTING */
  .accounting-total { background: #1a1a2e; color: #fff; padding: 12px 18px; border-radius: 8px; margin-top: 14px; font-size: 1rem; font-weight: 700; text-align: center; }

  /* MISC */
  .tip { font-size: 0.8rem; color: #888; font-style: italic; margin-top: 8px; }
  .divider { border: none; border-top: 1px solid #e5e7eb; margin: 16px 0; }
  .pill { display: inline-block; padding: 2px 10px; border-radius: 20px; font-size: 0.75rem; font-weight: 600; margin: 2px; }
  .pill-red { background: #fde8e8; color: #c0392b; }
  .pill-green { background: #eafaf1; color: #1e8449; }
  .pill-blue { background: #eaf4fb; color: #2471a3; }
  .pill-gray { background: #f2f3f4; color: #5d6d7e; }
  .pill-yellow { background: #fef9e7; color: #b7770d; }
  .pill-purple { background: #f5eef8; color: #6c3483; }

  .top3 { counter-reset: top3; }
  .top3-item { counter-increment: top3; display: flex; align-items: flex-start; gap: 14px; padding: 16px; border-radius: 10px; margin-bottom: 12px; }
  .top3-item::before { content: counter(top3); font-size: 2rem; font-weight: 900; color: #fff; background: #1a1a2e; width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
  .top3-item.t1 { background: #fdf3f3; border-left: 5px solid #c0392b; }
  .top3-item.t2 { background: #f0faf4; border-left: 5px solid #1e8449; }
  .top3-item.t3 { background: #f0f6fb; border-left: 5px solid #2471a3; }
  .top3-item h3 { font-size: 0.97rem; font-weight: 700; margin-bottom: 4px; }
  .top3-item p { font-size: 0.85rem; color: #555; }

  .phishing-box { background: #1a0000; color: #ff6b6b; border-radius: 8px; padding: 12px 16px; margin-bottom: 10px; font-size: 0.85rem; }
  .phishing-box strong { color: #ff9090; }

  @media(max-width:600px) {
    .header { padding: 20px; }
    .header h1 { font-size: 1.4rem; }
    .header .meta { gap: 12px; }
    .dashboard-grid { grid-template-columns: 1fr 1fr; }
  }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════════════
     SECTION 0 — EMAIL TRIAGE QUICK LIST
     ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title band-dark">📋 Email Triage Quick List</div>
  <div class="section-body" style="padding:0;">
    <table>
      <thead>
        <tr>
          <th style="width:140px;">Status</th>
          <th style="width:200px;">From</th>
          <th>Subject</th>
          <th>Summary</th>
        </tr>
      </thead>
      <tbody>
        <!-- INBOX ROWS — individual -->
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>Bank of America</td>
          <td>A direct deposit was credited to your account</td>
          <td>$5.00 Venmo Cashout credited to checking account ending 7471 on July 27.</td>
        </tr>
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>Jennifer Collura (manager@seasonsem.com)</td>
          <td>Re: [no subject thread]</td>
          <td>Jennifer confirmed: "Yes that is great see her then" — responding to Fran W about dog drop-off before 10 AM. ⚠️ Unread.</td>
        </tr>
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>Lands' End</td>
          <td>60% off swim: Rashguards & more</td>
          <td>Promotional sale email — 70% off clearance, 50% off almost everything else.</td>
        </tr>
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>Udemy</td>
          <td>Last chance to save on a year of learning.</td>
          <td>Promotional email for Udemy Personal Plan subscription — career learning offer.</td>
        </tr>
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>fran W (franw516@gmail.com)</td>
          <td>[no subject]</td>
          <td>Fran's daughter can bring the dog in before 10 AM — needs acknowledgment/confirmation. ⚠️ Unread &amp; actionable.</td>
        </tr>
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>HR Leaders Events</td>
          <td>Melissa, 48 hours left (and you haven't grabbed your seat)</td>
          <td>Josh Bersin speaking — 48-hour deadline to register for HR event. Unread.</td>
        </tr>
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>USPS Informed Delivery</td>
          <td>Your Daily Digest for Mon, 7/27 is ready to view</td>
          <td>6 mailpieces arriving today, 0 packages.</td>
        </tr>
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>Otter.ai Insights</td>
          <td>Your upcoming meetings</td>
          <td>Weekly meeting prep summary from Otter.ai — review upcoming calendar items.</td>
        </tr>
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>Your Local Chick-fil-A</td>
          <td>Just Because</td>
          <td>Loyalty reward notification — 402 points available. Promotional.</td>
        </tr>
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>LinkedIn Job Alerts</td>
          <td>New jobs similar to VP, People at DomainTools</td>
          <td>LinkedIn job alert — VP-level People roles similar to DomainTools listing. Unread.</td>
        </tr>
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>LinkedIn Job Alerts</td>
          <td>Strategic People Partner at Oyster®: up to $160K/year</td>
          <td>Job alert posted 7/24/2026 — Strategic People Partner role at Oyster, up to $160K. Unread.</td>
        </tr>
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>LinkedIn Job Alerts</td>
          <td>VP, People at DomainTools: up to $275K/year</td>
          <td>Job alert posted 7/25/2026 — VP of People at DomainTools, up to $275K. Unread.</td>
        </tr>
        <!-- TWO SUMMARY ROWS AT BOTTOM -->
        <tr style="background:#fff8f8;">
          <td class="status-auto">🗑 AUTO-TRASHED</td>
          <td colspan="2"><strong>2 emails auto-trashed (phishing)</strong> — see Trash Review</td>
          <td>iCloud spoofing phishing attempts removed automatically.</td>
        </tr>
        <tr style="background:#f8f9fa;">
          <td class="status-trash">🗂 TRASH (manual)</td>
          <td colspan="2"><strong>19 emails in Trash</strong> — see Trash Review</td>
          <td>Mix of newsletters, promotions, and digests moved to Trash.</td>
        </tr>
      </tbody>
    </table>
    <p class="tip" style="padding:10px 14px;">Emails sent from Melissa (BetterUp follow-up) and non-inbox/non-trash emails appear in their respective categories below. All 50 emails accounted for.</p>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 1 — HEADER
     ═══════════════════════════════════════════════════════════ -->
<div class="header">
  <div class="sub" style="font-size:0.85rem; color:#90b4e0; margin-bottom:6px; text-transform:uppercase; letter-spacing:2px;">Executive Briefing</div>
  <h1>Good Morning, Melissa 👋</h1>
  <div class="sub">Monday, July 27, 2026 — Prepared by your Executive Chief of Staff</div>
  <div class="meta">
    <div class="meta-item"><span>Emails Reviewed</span><strong>50</strong></div>
    <div class="meta-item"><span>Calendar Events</span><strong>10</strong></div>
    <div class="meta-item"><span>Action Required</span><strong>7</strong></div>
    <div class="meta-item"><span>Interviews This Week</span><strong>1</strong></div>
    <div class="meta-item"><span>Security Alerts</span><strong>2</strong></div>
    <div class="meta-item"><span>Unread Emails</span><strong>28</strong></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 2 — EXECUTIVE SUMMARY
     ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title band-dark">⚡ Executive Summary</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li class="exec-red"><strong>🔴 Security Risk:</strong> Two sophisticated phishing emails spoofing iCloud/Apple cloud storage were automatically intercepted and removed before reaching your inbox. They used urgent account-blocking language and fake payment threats. No action needed — they are safely quarantined — but be on guard for similar attempts.</li>
      <li class="exec-green"><strong>🟢 Job Search Priority:</strong> You have a confirmed interview with Elliptic (Head of People — U.S.) <strong>tomorrow, Tuesday July 28 at 10:30 AM EDT</strong> via Zoom — prep is needed today. Additionally, high-value LinkedIn alerts flagged VP of People at DomainTools (up to $275K) and a BetterUp follow-up email awaits a response from recruiter Amber.</li>
      <li class="exec-blue"><strong>🔵 Calendar Deadline:</strong> An HR Leaders Events webinar (Josh Bersin speaking) expires in <strong>48 hours</strong> — registration deadline is today or tomorrow. You also have three professional networking/webinar events on Wednesday July 29 that require RSVP decisions.</li>
    </ul>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 3 — ACTION REQUIRED
     ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title band-red">🚨 Action Required</div>
  <div class="section-body">

    <div class="card card-green">
      <span class="label label-green">🟢 INTERVIEW PREP — URGENT</span>
      <h3>Elliptic Interview Tomorrow — Head of People (U.S.)</h3>
      <p><strong>Source:</strong> Google Calendar — confirmed</p>
      <p><strong>Why it matters:</strong> Talent Partner Screen with Christopher Ratcliffe (Talentful/LinkedIn) is scheduled for <strong>Tuesday, July 28 at 10:30–11:00 AM EDT</strong> via Zoom. This is a live interview — preparation should happen today.</p>
      <p><strong>Zoom:</strong> <a href="https://elliptic-co.zoom.us/j/89752444403?pwd=tNtT8ECe9DIsZ4kIXgmuDZGW8RBCDc.1" style="color:#1e8449;">https://elliptic-co.zoom.us/j/89752444403</a> | Meeting ID: 89752444403 | Passcode: %gG9*sA2fV (desktop) | 1168138618 (mobile)</p>
      <p><strong>Recommended next step:</strong> Research Elliptic (blockchain analytics), review your Head of People narrative, prepare 3 key stories, and test Zoom link tonight.</p>
      <p><strong>Due:</strong> Today — prep by end of day July 27</p>
    </div>

    <div class="card card-yellow">
      <span class="label label-yellow">🟡 FOLLOW-UP PENDING</span>
      <h3>BetterUp Recruiter Follow-Up — Awaiting Response from Amber</h3>
      <p><strong>Source:</strong> Gmail — sent by Melissa (melissaw212@gmail.com) at 1:00 PM today</p>
      <p><strong>Why it matters:</strong> You reached out to recruiter Amber this morning asking for a status update on your candidacy. No response yet — monitor inbox and follow up if no reply by Wednesday.</p>
      <p><strong>Recommended next step:</strong> Check for reply from Amber by Wednesday July 29. If no response, send a final polite follow-up or shift focus to other opportunities.</p>
      <p><strong>Due:</strong> Follow up by Wednesday, July 29</p>
    </div>

    <div class="card card-yellow">
      <span class="label label-yellow">🟡 CALENDAR — RSVP NEEDED</span>
      <h3>Call St. Francis — Confirm Insurance is Up to Date</h3>
      <p><strong>Source:</strong> Google Calendar — confirmed, 9:00–10:00 AM today</p>
      <p><strong>Why it matters:</strong> This task is scheduled for this morning (9 AM–10 AM). Phone number: <strong>1-866-367-2901</strong>. Verify insurance is current before the appointment window closes.</p>
      <p><strong>Recommended next step:</strong> Call St. Francis at 1-866-367-2901 immediately — this window may have already started.</p>
      <p><strong>Due:</strong> Today, July 27 — 9:00 AM–10:00 AM</p>
    </div>

    <div class="card card-yellow">
      <span class="label label-yellow">🟡 PERSONAL — RESPONSE NEEDED</span>
      <h3>Fran W — Dog Drop-Off Before 10 AM Confirmed by Jennifer Collura</h3>
      <p><strong>Source:</strong> Gmail inbox — fran W (franw516@gmail.com) + Jennifer Collura (manager@seasonsem.com)</p>
      <p><strong>Why it matters:</strong> Fran messaged at 8:04 AM asking if her daughter can bring the dog in before 10. Jennifer Collura (at Seasons EM — likely a vet or pet care facility) responded "Yes that is great see her then." Fran may still need confirmation from you.</p>
      <p><strong>Recommended next step:</strong> Confirm with Fran that Jennifer's approval is communicated, or simply reply to Fran confirming the drop-off is arranged.</p>
      <p><strong>Due:</strong> Today before 10:00 AM — URGENT (may have already passed)</p>
    </div>

    <div class="card card-yellow">
      <span class="label label-yellow">🟡 FINANCIAL — REVIEW</span>
      <h3>Chase Credit Card Statement Available — Min. Payment $35 Due Aug 23</h3>
      <p><strong>Source:</strong> Gmail — Chase (no.reply.alerts@chase.com)</p>
      <p><strong>Why it matters:</strong> Your Chase credit card statement (...8874) is available. Minimum payment due $35.00, due date August 23, 2026.</p>
      <p><strong>Recommended next step:</strong> Log into Chase to review statement and schedule payment before August 23 to avoid late fees.</p>
      <p><strong>Due:</strong> August 23, 2026</p>
    </div>

    <div class="card card-purple">
      <span class="label label-purple">🟣 PROFESSIONAL EVENT — DEADLINE TODAY</span>
      <h3>HR Leaders Events — Josh Bersin Webinar — 48-Hour Registration Deadline</h3>
      <p><strong>Source:</strong> Gmail inbox — HR Leaders Events (hello@hrleaders.co)</p>
      <p><strong>Why it matters:</strong> Email says "48 hours left" — Josh Bersin is a top HR industry analyst. This type of executive content is directly relevant to your job search positioning and HR leadership brand.</p>
      <p><strong>Recommended next step:</strong> Decide today whether to register. If relevant to your target roles, register immediately — deadline expires tomorrow morning.</p>
      <p><strong>Due:</strong> Tonight or tomorrow morning, July 28</p>
    </div>

    <div class="card card-blue">
      <span class="label label-blue">🔵 RSVP NEEDED — WEDNESDAY</span>
      <h3>Three Wednesday July 29 Events Still Need RSVP Decision</h3>
      <p><strong>Source:</strong> Google Calendar — "needsAction" status on two events</p>
      <p><strong>Why it matters:</strong> "The Future of Benefits" HR Roundtable (12 PM–1 PM) and "HR Networking &amp; Job Search Group — Zoom 2" (12 PM–1:30 PM) overlap and both show "needsAction" RSVP status. "How A VP Talent Builds with AI" (11 AM–12 PM) is accepted but conflicts with the 12 PM events.</p>
      <p><strong>Recommended next step:</strong> Decide which Wednesday event(s) to attend and respond. The networking group (large attendance) and Benefits roundtable conflict — choose one for the noon slot.</p>
      <p><strong>Due:</strong> Today, July 27 — before Wednesday</p>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 4 — FULL 7-DAY CALENDAR
     ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title band-blue">📅 Full 7-Day Calendar</div>
  <div class="section-body">

    <!-- MONDAY JULY 27 -->
    <div class="cal-day">
      <div class="cal-day-header">Monday, July 27, 2026 — TODAY</div>
      <div class="cal-event" style="border-color:#d4a017; background:#fefcf0;">
        <h4>📞 Call St. Francis — Confirm Insurance is Up to Date</h4>
        <p><strong>Time:</strong> 9:00 AM – 10:00 AM EDT</p>
        <p><strong>Status:</strong> <span class="badge badge-green">Confirmed</span></p>
        <p><strong>Phone:</strong> 1-866-367-2901</p>
        <p><strong>Prep:</strong> Have your insurance card and policy number ready. Confirm coverage is current before the call window expires.</p>
        <p><strong>⚠️ Note:</strong> This window may have already started — call immediately if not yet done.</p>
      </div>
    </div>

    <!-- TUESDAY JULY 28 -->
    <div class="cal-day">
      <div class="cal-day-header">Tuesday, July 28, 2026 — TOMORROW</div>
      <div class="cal-event green-event">
        <h4>💼 Interview with Elliptic — Head of People (U.S.) — Talent Partner Screen</h4>
        <p><strong>Time:</strong> 10:30 AM – 11:00 AM EDT</p>
        <p><strong>Interviewer:</strong> Christopher Ratcliffe, Talentful Talent Lead (LinkedIn)</p>
        <p><strong>Status:</strong> <span class="badge badge-green">Accepted ✅</span></p>
        <p><strong>Location:</strong> <a href="https://elliptic-co.zoom.us/j/89752444403?pwd=tNtT8ECe9DIsZ4kIXgmuDZGW8RBCDc.1">Zoom — Meeting ID: 89752444403 | Desktop Passcode: %gG9*sA2fV | Mobile: 1168138618</a></p>
        <p><strong>Prep Needed:</strong> Research Elliptic's mission (blockchain analytics/compliance), prepare 3 leadership stories (STAR format), know your Head of People positioning, test Zoom link 15 min early, have questions ready for Christopher about team size and mandate.</p>
        <p><strong>⚠️ Note:</strong> Two calendar entries exist for this event (one with full details in location field, one as standard Zoom invite) — they are the same meeting. Attend only one Zoom session.</p>
      </div>
    </div>

    <!-- WEDNESDAY JULY 29 -->
    <div class="cal-day">
      <div class="cal-day-header">Wednesday, July 29, 2026</div>
      <div class="cal-event green-event">
        <h4>🤖 How A VP Talent Builds with AI — PromptMates Live</h4>
        <p><strong>Time:</strong> 11:00 AM – 12:00 PM EDT</p>
        <p><strong>Status:</strong> <span class="badge badge-green">Accepted ✅</span></p>
        <p><strong>Location:</strong> <a href="https://luma.com/join/g-sAv9NHMvqDBBXrx">Luma — https://luma.com/join/g-sAv9NHMvqDBBXrx</a></p>
        <p><strong>About:</strong> Free webinar for HR/Recruitment professionals on AI, automation &amp; new tech. Features Emily Gransky (VP Talent).</p>
        <p><strong>Prep:</strong> None required — free attendance.</p>
        <p><strong>⚠️ Conflict:</strong> Ends at 12 PM, which is when the next two events begin — may need to choose between the Benefits Roundtable and HR Networking Group for the 12–1:30 PM slot.</p>
      </div>
      <div class="cal-event needs-action">
        <h4>🏥 The Future of Benefits: Why Healthcare Alone Isn't Enough — HIC HR &amp; L&amp;D Roundtable</h4>
        <p><strong>Time:</strong> 12:00 PM – 1:00 PM EDT</p>
        <p><strong>Status:</strong> <span class="badge badge-yellow">RSVP Needed ⚠️</span></p>
        <p><strong>Location:</strong> <a href="https://us06web.zoom.us/j/5224221004?pwd=UU5YNmlFckpjQnlzc2FDMHFlNUhhUT09">Zoom — Meeting ID: 5224221004</a></p>
        <p><strong>About:</strong> Senior HR/People leaders roundtable featuring CEO of CareCrowd.</p>
        <p><strong>Prep:</strong> RSVP first. Directly relevant to benefits strategy expertise.</p>
        <p><strong>⚠️ Conflict:</strong> Overlaps with HR Networking &amp; Job Search Group (12–1:30 PM) — choose one.</p>
      </div>
      <div class="cal-event needs-action">
        <h4>🤝 HR Networking &amp; Job Search Group — Zoom 2</h4>
        <p><strong>Time:</strong> 12:00 PM – 1:30 PM EDT</p>
        <p><strong>Status:</strong> <span class="badge badge-yellow">RSVP Needed ⚠️</span></p>
        <p><strong>Location:</strong> <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1">Zoom — Meeting ID: 81954171722</a></p>
        <p><strong>About:</strong> Large HR professional networking &amp; job search group (~170+ attendees). Note: AI notetaking tools should be off per instructions.</p>
        <p><strong>⚠️ Conflict:</strong> Overlaps with Benefits Roundtable — choose one for noon slot.</p>
      </div>
      <div class="cal-event">
        <h4>🌐 Network</h4>
        <p><strong>Time:</strong> 12:00 PM – 1:30 PM EDT</p>
        <p><strong>Status:</strong> <span class="badge badge-green">Confirmed ✅</span></p>
        <p><strong>Note:</strong> Likely a personal reminder aligned to the HR Networking Group above. No separate link — treat as the same block.</p>
      </div>
    </div>

    <!-- THURSDAY JULY 30 -->
    <div class="cal-day">
      <div class="cal-day-header">Thursday, July 30, 2026</div>
      <div class="cal-event declined">
        <h4>🚫 Executive Roundtable (John Madigan) — DECLINED</h4>
        <p><strong>Time:</strong> 9:00 AM – 10:30 AM EDT</p>
        <p><strong>Status:</strong> <span class="badge badge-gray">Declined ❌</span></p>
        <p><strong>Location:</strong> <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09">Zoom — Meeting ID: 207 786 667 | Password: 205454</a></p>
        <p><strong>Note:</strong> You have already declined this invite. No prep needed unless you wish to reconsider.</p>
      </div>
      <div class="cal-event needs-action">
        <h4>🤝 HR Networking &amp; Job Search: Open Office Hours — Zoom 2</h4>
        <p><strong>Time:</strong> 12:00 PM – 1:00 PM EDT</p>
        <p><strong>Status:</strong> <span class="badge badge-yellow">RSVP Needed ⚠️</span></p>
        <p><strong>Location:</strong> <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1">Zoom — Meeting ID: 85945371140</a></p>
        <p><strong>About:</strong> Open office hours from the HR Networking &amp; Job Search group. Large attendee list (~170+). Good for 1:1 connection opportunities.</p>
        <p><strong>Prep:</strong> RSVP and review attendee list for warm connections.</p>
      </div>
    </div>

    <!-- FRIDAY JULY 31 -->
    <div class="cal-day">
      <div class="cal-day-header">Friday, July 31, 2026</div>
      <div class="cal-event" style="background:#f8f9fa; border-color:#adb5bd;">
        <h4>📭 No Calendar Events</h4>
        <p>Use this day for follow-ups from the week's interviews and networking.</p>
      </div>
    </div>

    <!-- SATURDAY AUG 1 -->
    <div class="cal-day">
      <div class="cal-day-header">Saturday, August 1, 2026</div>
      <div class="cal-event" style="background:#f8f9fa; border-color:#adb5bd;">
        <h4>📭 No Calendar Events</h4>
        <p>Rest &amp; recharge.</p>
      </div>
    </div>

    <!-- SUNDAY AUG 2 -->
    <div class="cal-day">
      <div class="cal-day-header">Sunday, August 2, 2026 – Monday, August 3</div>
      <div class="cal-event" style="border-color:#8e44ad; background:#f8f0fe;">
        <h4>🎂 Shari's Birthday — All Day Event</h4>
        <p><strong>Dates:</strong> August 2 (all day)</p>
        <p><strong>Status:</strong> <span class="badge badge-green">Confirmed ✅</span></p>
        <p><strong>Note:</strong> Don't forget to send a birthday message or gift!</p>
      </div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 5 — JOB SEARCH & INTERVIEW PIPELINE
     ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title band-green">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">
    <table>
      <thead>
        <tr>
          <th>Fit</th>
          <th>Company / Role</th>
          <th>Source</th>
          <th>Status</th>
          <th>Salary / Notes</th>
          <th>Next Action</th>
        </tr>
      </thead>
      <tbody>
        <tr style="background:#f0faf4;">
          <td><span class="badge badge-high">HIGH</span></td>
          <td><strong>Elliptic — Head of People (U.S.)</strong></td>
          <td>Google Calendar (confirmed)</td>
          <td><span class="badge badge-green">Interview Tomorrow</span></td>
          <td>Blockchain analytics firm — global company</td>
          <td>🔴 Prep today — Zoom tomorrow 10:30 AM</td>
        </tr>
        <tr>
          <td><span class="badge badge-high">HIGH</span></td>
          <td><strong>BetterUp — [Role TBD]</strong></td>
          <td>Gmail — Melissa sent follow-up to Amber today</td>
          <td><span class="badge badge-yellow">Awaiting Response</span></td>
          <td>Coaching/HR platform — strong brand fit</td>
          <td>Monitor inbox — follow up Wed if no reply</td>
        </tr>
        <tr>
          <td><span class="badge badge-high">HIGH</span></td>
          <td><strong>DomainTools — VP, People</strong></td>
          <td>LinkedIn Job Alert (jobalerts-noreply@linkedin.com)</td>
          <td><span class="badge badge-blue">New Alert</span></td>
          <td>Up to $275K/year — posted 7/25/2026</td>
          <td>Review job description — apply or research today</td>
        </tr>
        <tr>
          <td><span class="badge badge-medium">MEDIUM</span></td>
          <td><strong>Oyster® — Strategic People Partner</strong></td>
          <td>LinkedIn Job Alert (jobalerts-noreply@linkedin.com)</td>
          <td><span class="badge badge-blue">New Alert</span></td>
          <td>Up to $160K/year — posted 7/24/2026</td>
          <td>Review scope — may be below VP level target</td>
        </tr>
        <tr>
          <td><span class="badge badge-medium">MEDIUM</span></td>
          <td><strong>VP, People — Similar Roles (LinkedIn batch alert)</strong></td>
          <td>LinkedIn (jobs-noreply@linkedin.com)</td>
          <td><span class="badge badge-blue">New Alerts</span></td>
          <td>Multiple roles similar to VP, People at DomainTools</td>
          <td>Open alert and review list of similar roles</td>
        </tr>
        <tr>
          <td><span class="badge badge-medium">MEDIUM</span></td>
          <td><strong>Profile Visibility — 198 LinkedIn Profile Views</strong></td>
          <td>LinkedIn (messages-noreply@linkedin.com)</td>
          <td><span class="badge badge-blue">Info</span></td>
          <td>Strong visibility signal — active market interest</td>
          <td>Check who viewed — connect with relevant viewers</td>
        </tr>
        <tr>
          <td><span class="badge badge-low">LOW</span></td>
          <td><strong>HR Networking &amp; Job Search Group (Zoom)</strong></td>
          <td>Google Calendar — Wed July 29, 12–1:30 PM</td>
          <td><span class="badge badge-yellow">RSVP Needed</span></td>
          <td>Peer networking — 170+ HR professionals</td>
          <td>RSVP and review attendee list for key connections</td>
        </tr>
        <tr>
          <td><span class="badge badge-low">LOW</span></td>
          <td><strong>HR Networking Open Office Hours</strong></td>
          <td>Google Calendar — Thu July 30, 12–1 PM</td>
          <td><span class="badge badge-yellow">RSVP Needed</span></td>
          <td>Open discussion — no recording</td>
          <td>RSVP if attending</td>
        </tr>
      </tbody>
    </table>
    <div style="margin-top:14px;">
      <div class="card card-purple" style="margin-bottom:0;">
        <span class="label label-purple">🟣 PROFESSIONAL DEVELOPMENT</span>
        <h3>How A VP Talent Builds with AI — PromptMates Live (Wed Jul 29, 11 AM)</h3>
        <p>Free webinar featuring Emily Gransky (VP Talent) on AI tools for HR/Recruitment professionals. Already accepted — attend for ideas you can reference in interviews.</p>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 6 — FULL EMAIL REVIEW BY CATEGORY
     ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title band-dark">📧 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="card card-red">
      <span class="label label-red">🔴 Security / Risk — 2 Emails</span>
      <h3>Auto-Trashed Phishing Emails</h3>
      <p><strong>Important senders:</strong> melissaw212@gwbzubhp.ryth.scopeimpact.biz.id (spoofing your own email); jdrzcxolbbe@jksd.tworcqhlgxxbb.us (spoofing as "Payment-Declined")</p>
      <div class="phishing-box">
        <strong>Email 1 (auto_trashed):</strong> "We have blocked your account 🚫" — Sender spoofed your own email address as display name. Sent from a random subdomain (scopeimpact.biz.id). Claimed iCloud photos/videos will be deleted — classic payment credential harvest scam.<br><br>
        <strong>Email 2 (auto_trashed):</strong> "🚫We have blocked your account! Sun,26 Jul-2026" — Sent from a junk domain (tworcqhlgxxbb.us) using "Payment-Declined" as sender name. Same iCloud/cloud storage account-threat phishing pattern.
      </div>
      <p><strong>Recommended action:</strong> No action needed — both emails were auto-trashed as high-confidence phishing before reaching your inbox. ✅ Handled.</p>
    </div>

    <!-- JOB SEARCH -->
    <div class="card card-green">
      <span class="label label-green">🟢 Job Search — 5 Emails</span>
      <h3>Active Job Search Activity</h3>
      <table style="margin-top:8px;">
        <thead><tr><th>From</th><th>Subject</th><th>Status</th></tr></thead>
        <tbody>
          <tr><td>Melissa (sent)</td><td>Re: Follow Up: BetterUp Information</td><td>Sent today — awaiting reply from Amber</td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>VP, People at DomainTools: up to $275K/year</td><td>📥 Inbox — unread — review today</td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>Strategic People Partner at Oyster®: up to $160K/year</td><td>📥 Inbox — unread — review today</td></tr>
          <tr><td>LinkedIn (jobs-noreply)</td><td>New jobs similar to VP, People at DomainTools</td><td>📥 Inbox — unread — open &amp; review</td></tr>
          <tr><td>LinkedIn (messages-noreply)</td><td>198 people visited your profile</td><td>Strong signal — check viewers</td></tr>
        </tbody>
      </table>
      <p><strong>Recommended action:</strong> Review all LinkedIn alerts today. Research DomainTools VP role immediately — $275K is top of target range.</p>
    </div>

    <!-- RECRUITERS / NETWORKING -->
    <div class="card card-teal">
      <span class="label" style="background:#e0f5f1; color:#117a65;">🟢 Recruiters / Networking — 1 Email</span>
      <h3>Elliptic Interview Confirmation (via Calendar)</h3>
      <p>The Elliptic interview is represented in Calendar. No standalone recruiter email was flagged in the inbox, but the calendar entry contains full recruiter details: <strong>Christopher Ratcliffe, Talentful</strong>.</p>
      <p><strong>Recommended action:</strong> Connect with Christopher Ratcliffe on LinkedIn post-interview. Prepare thoughtful questions about the role mandate.</p>
    </div>

    <!-- CALENDAR / EVENTS -->
    <div class="card card-blue">
      <span class="label label-blue">🔵 Calendar / Events — 2 Emails</span>
      <h3>Otter.ai Weekly Meeting Prep + HR Leaders Events Webinar</h3>
      <table style="margin-top:8px;">
        <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Otter.ai Insights</td><td>Your upcoming meetings</td><td>Read — review upcoming meetings summary</td></tr>
          <tr><td>HR Leaders Events</td><td>Melissa, 48 hours left (and you haven't grabbed your seat)</td><td>⚠️ Register today — Josh Bersin speaking</td></tr>
        </tbody>
      </table>
      <p><strong>Recommended action:</strong> Register for HR Leaders Events webinar today before the 48-hour window closes.</p>
    </div>

    <!-- MEDICAL / HEALTH -->
    <div class="card card-yellow">
      <span class="label label-yellow">🟡 Medical / Health — 1 Email (via Calendar)</span>
      <h3>St. Francis Insurance Verification</h3>
      <p>No separate email — this appears as a calendar task: "Call St. Francis to make sure insurance is up to date" at 9:00–10:00 AM today. Phone: 1-866-367-2901.</p>
      <p><strong>Recommended action:</strong> Call immediately if not yet done.</p>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="card card-yellow">
      <span class="label label-yellow">🟡 Financial / Billing — 2 Emails</span>
      <h3>Bank of America Deposit + Chase Statement</h3>
      <table style="margin-top:8px;">
        <thead><tr><th>From</th><th>Subject</th><th>Detail</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Bank of America</td><td>A direct deposit was credited to your account</td><td>$5.00 Venmo Cashout — Checking 7471 — July 27</td><td>📥 Inbox — informational, no action needed</td></tr>
          <tr><td>Chase</td><td>Your credit card statement is available</td><td>Card ...8874 — Min. $35 due Aug 23, 2026</td><td>Log in to review &amp; schedule payment</td></tr>
        </tbody>
      </table>
      <p><strong>Recommended action:</strong> Review Chase statement online and schedule payment before August 23.</p>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="card card-purple">
      <span class="label label-purple">🟣 Professional Development — 2 Emails</span>
      <h3>Udemy + Perplexity Computer Task</h3>
      <table style="margin-top:8px;">
        <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Udemy</td><td>Last chance to save on a year of learning.</td><td>📥 Inbox — Consider if career-development learning is a current priority</td></tr>
          <tr><td>Perplexity Computer</td><td>Your task is complete: Laura Geller Line Smoother Review</td><td>Personal AI task completed — check results if needed</td></tr>
        </tbody>
      </table>
      <p><strong>Recommended action:</strong> Evaluate Udemy Personal Plan if you want structured learning during job search. Perplexity task — review output at your convenience.</p>
    </div>

    <!-- PERSONAL -->
    <div class="card card-gray">
      <span class="label label-gray">⚪ Personal — 2 Emails</span>
      <h3>Fran W (Dog Drop-Off) + Jennifer Collura (Confirmation)</h3>
      <table style="margin-top:8px;">
        <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>fran W (franw516@gmail.com)</td><td>[no subject] — dog drop-off before 10 AM</td><td>⚠️ Reply to confirm — Fran is waiting</td></tr>
          <tr><td>Jennifer Collura (manager@seasonsem.com)</td><td>Re: — "Yes that is great see her then"</td><td>Pass confirmation back to Fran</td></tr>
        </tbody>
      </table>
      <p><strong>Recommended action:</strong> Reply to Fran confirming the drop-off is arranged with Jennifer at Seasons EM.</p>
    </div>

    <!-- MATCH.COM -->
    <div class="card card-gray">
      <span class="label label-gray">⚪ Personal — Match.com Activity — 7 Emails</span>
      <h3>Match.com Notifications</h3>
      <table style="margin-top:8px;">
        <thead><tr><th>From</th><th>Subject</th><th>Unread</th></tr></thead>
        <tbody>
          <tr><td>Match</td><td>Xnpp likes you. See if it's mutual.</td><td>Yes</td></tr>
          <tr><td>Match</td><td>Rob likes you. See if it's mutual.</td><td>No</td></tr>
          <tr><td>Match</td><td>Michael just sent you a new message. 💌</td><td>No</td></tr>
          <tr><td>Match</td><td>Michael likes you. See if it's mutual.</td><td>No</td></tr>
          <tr><td>Match</td><td>Benton likes you. See if it's mutual.</td><td>No</td></tr>
          <tr><td>Match</td><td>Jeff likes you. See if it's mutual.</td><td>Yes</td></tr>
          <tr><td>Match</td><td>You've had a profile view from Fred</td><td>No</td></tr>
        </tbody>
      </table>
      <p><strong>Recommended action:</strong> Check Match.com app directly. Michael sent you a message — worth a look when you have a moment. Low priority today given interview prep.</p>
    </div>

    <!-- NEWSLETTERS / SUBSCRIPTIONS -->
    <div class="card card-purple">
      <span class="label label-purple">🟣 Newsletters / Subscriptions — 10 Emails (mix of inbox &amp; trash)</span>
      <h3>Various Newsletters &amp; Digests</h3>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Location</th><th>Rec.</th></tr></thead>
        <tbody>
          <tr><td>Medium Daily Digest (noreply@medium.com)</td><td>The Most Reliable $1,000/Month Skill...</td><td>Trash</td><td>Delete — note: Medium membership expires Aug 20</td></tr>
          <tr><td>Medium Daily Digest (noreply@medium.com)</td><td>The Token Trap | Shashank Sane</td><td>Trash</td><td>Delete — different account (amylw)</td></tr>
          <tr><td>Pranit naik via Medium</td><td>Anthropic Just Launched Opus 5...</td><td>Trash</td><td>Delete or read online</td></tr>
          <tr><td>The AI Report</td><td>⚡ Anthropic releases Opus 5</td><td>Trash</td><td>Review if interested in AI news</td></tr>
          <tr><td>TLDR (dan@tldrnewsletter.com)</td><td>Nvidia's $250B OpenAI deal...</td><td>Trash</td><td>Review — relevant AI/tech news</td></tr>
          <tr><td>Dylan's Diary</td><td>The 57-Year Low That Should Worry You</td><td>Trash</td><td>Review — job market context relevant</td></tr>
          <tr><td>The Daily Skimm</td><td>Lip Smackers were the blueprint</td><td>Trash</td><td>Delete — lifestyle content</td></tr>
          <tr><td>The Average Joe</td><td>🦆 Splurge — China's fitness frenzy</td><td>Trash</td><td>Delete — low relevance</td></tr>
          <tr><td>1% Better</td><td>NATO Spy, Outbreak Adjustments...</td><td>Trash</td><td>Delete — general newsletter</td></tr>
          <tr><td>Gemma Bonham-Carter</td><td>it's draft day</td><td>Trash</td><td>Delete — low relevance</td></tr>
        </tbody>
      </table>
      <p><strong>⚠️ Note:</strong> Your Medium membership expires August 20, 2026 — decide whether to renew or let it lapse.</p>
      <p><strong>Recommended action:</strong> Clear trash. Keep TLDR and Dylan's Diary subscriptions if you want job market context. Consider unsubscribing from low-value newsletters.</p>
    </div>

    <!-- PROMOTIONAL / RETAIL -->
    <div class="card card-gray">
      <span class="label label-gray">⚪ Promotional / Retail — 14 Emails</span>
      <h3>Shopping, Retail &amp; Food Promotions</h3>
      <p>See dedicated Promotional / Retail Summary section below for full breakdown.</p>
      <p><strong>Recommended action:</strong> No action required today. Review at leisure or delete.</p>
    </div>

    <!-- USPS -->
    <div class="card card-gray">
      <span class="label label-gray">⚪ USPS / Mail — 1 Email</span>
      <h3>USPS Informed Delivery Daily Digest</h3>
      <p><strong>From:</strong> USPS Informed Delivery — 6 mailpieces arriving today, 0 packages.</p>
      <p><strong>Recommended action:</strong> Check your mailbox today. Informational — no reply needed.</p>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT / EXEC COACHING -->
    <div class="card card-purple">
      <span class="label label-purple">🟣 Executive Coaching / Career Marketing — 2 Emails (Trash)</span>
      <h3>Lisa Rangel + Susanna Madden</h3>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Notes</th></tr></thead>
        <tbody>
          <tr><td>Lisa Rangel (Chameleon Resumes)</td><td>Mistakes costing executives roles they never heard</td><td>In Trash — free training this Wednesday — relevant to job search</td></tr>
          <tr><td>Susanna Madden (Thrive Resources)</td><td>Melissa — The Private Equity Market Has Changed. Have You?</td><td>7-part executive masterclass — not in trash but external marketing</td></tr>
        </tbody>
      </table>
      <p><strong>Recommended action:</strong> Lisa Rangel's Wednesday free training could be worth attending given active job search. Susanna Madden is a cold marketing email — delete unless PE is a target sector.</p>
