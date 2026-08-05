<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa W — August 5, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a237e 0%, #283593 60%, #3949ab 100%); color: #fff; border-radius: 12px; padding: 28px 32px; margin-bottom: 24px; }
  .header h1 { font-size: 26px; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 15px; opacity: 0.88; margin-top: 4px; }
  .header .meta { display: flex; gap: 32px; margin-top: 16px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.15); border-radius: 8px; padding: 8px 18px; font-size: 13px; }
  .header .meta-item span { font-weight: 700; font-size: 20px; display: block; }

  /* SECTION HEADERS */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 16px; font-weight: 700; letter-spacing: 0.4px; padding: 10px 16px; border-radius: 8px 8px 0 0; display: flex; align-items: center; gap: 8px; }
  .section-body { background: #fff; border-radius: 0 0 8px 8px; padding: 16px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }

  /* COLOR THEMES */
  .red .section-title    { background: #c62828; color: #fff; }
  .red .section-body     { border-left: 4px solid #c62828; }
  .yellow .section-title { background: #f9a825; color: #fff; }
  .yellow .section-body  { border-left: 4px solid #f9a825; }
  .blue .section-title   { background: #1565c0; color: #fff; }
  .blue .section-body    { border-left: 4px solid #1565c0; }
  .green .section-title  { background: #2e7d32; color: #fff; }
  .green .section-body   { border-left: 4px solid #2e7d32; }
  .purple .section-title { background: #6a1b9a; color: #fff; }
  .purple .section-body  { border-left: 4px solid #6a1b9a; }
  .gray .section-title   { background: #546e7a; color: #fff; }
  .gray .section-body    { border-left: 4px solid #546e7a; }
  .teal .section-title   { background: #00695c; color: #fff; }
  .teal .section-body    { border-left: 4px solid #00695c; }
  .navy .section-title   { background: #1a237e; color: #fff; }
  .navy .section-body    { border-left: 4px solid #1a237e; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #eceff1; padding: 8px 10px; text-align: left; font-weight: 700; border-bottom: 2px solid #cfd8dc; }
  td { padding: 7px 10px; border-bottom: 1px solid #eceff1; vertical-align: top; }
  tr:hover td { background: #f9fafb; }
  tr:last-child td { border-bottom: none; }

  /* CARDS */
  .card { border-radius: 8px; padding: 14px 16px; margin-bottom: 12px; }
  .card-red    { background: #ffebee; border-left: 4px solid #c62828; }
  .card-yellow { background: #fffde7; border-left: 4px solid #f9a825; }
  .card-blue   { background: #e3f2fd; border-left: 4px solid #1565c0; }
  .card-green  { background: #e8f5e9; border-left: 4px solid #2e7d32; }
  .card-purple { background: #f3e5f5; border-left: 4px solid #6a1b9a; }
  .card-gray   { background: #f5f5f5; border-left: 4px solid #90a4ae; }
  .card-teal   { background: #e0f2f1; border-left: 4px solid #00695c; }

  .card h3 { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
  .card .meta-row { display: flex; gap: 16px; flex-wrap: wrap; margin: 4px 0; font-size: 12px; color: #555; }
  .card .meta-row strong { color: #333; }
  .card p { font-size: 13px; margin-top: 4px; }

  /* BADGES */
  .badge { display: inline-block; padding: 2px 9px; border-radius: 12px; font-size: 11px; font-weight: 700; letter-spacing: 0.3px; }
  .badge-red    { background: #ffcdd2; color: #b71c1c; }
  .badge-yellow { background: #fff9c4; color: #e65100; }
  .badge-green  { background: #c8e6c9; color: #1b5e20; }
  .badge-blue   { background: #bbdefb; color: #0d47a1; }
  .badge-purple { background: #e1bee7; color: #4a148c; }
  .badge-gray   { background: #eceff1; color: #455a64; }
  .badge-teal   { background: #b2dfdb; color: #004d40; }
  .badge-orange { background: #ffe0b2; color: #bf360c; }

  /* PRIORITY */
  .pri-high   { color: #b71c1c; font-weight: 700; }
  .pri-med    { color: #e65100; font-weight: 700; }
  .pri-low    { color: #558b2f; font-weight: 700; }

  /* TRIAGE TABLE */
  .triage-status { font-weight: 700; white-space: nowrap; }
  .rescued-row td { background: #fff8e1; }
  .inbox-row td   { background: #f1f8e9; }
  .trash-row td   { background: #fafafa; color: #888; }

  /* EXEC SUMMARY BULLETS */
  .exec-bullets { list-style: none; padding: 0; }
  .exec-bullets li { padding: 10px 14px; border-radius: 6px; margin-bottom: 8px; font-size: 14px; }
  .exec-bullets li.risk    { background: #ffebee; border-left: 4px solid #c62828; }
  .exec-bullets li.opp     { background: #e8f5e9; border-left: 4px solid #2e7d32; }
  .exec-bullets li.cal     { background: #e3f2fd; border-left: 4px solid #1565c0; }

  /* CALENDAR */
  .cal-day { background: #e8eaf6; border-radius: 6px; padding: 7px 12px; font-weight: 700; font-size: 13px; color: #1a237e; margin: 10px 0 4px; }
  .cal-event { display: flex; gap: 12px; padding: 8px 10px; border-radius: 6px; margin-bottom: 6px; align-items: flex-start; background: #f8f9ff; border-left: 3px solid #3949ab; }
  .cal-event.conflict { background: #fff3e0; border-left: 3px solid #f57c00; }
  .cal-event.declined { background: #fafafa; border-left: 3px solid #90a4ae; opacity: 0.75; }
  .cal-time { font-weight: 700; font-size: 12px; min-width: 80px; color: #3949ab; }
  .cal-details { flex: 1; }
  .cal-details h4 { font-size: 13px; font-weight: 700; margin-bottom: 2px; }
  .cal-details .cal-meta { font-size: 11px; color: #666; }
  .cal-details a { color: #1565c0; font-size: 11px; word-break: break-all; }

  /* DASHBOARD GRID */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; }
  .dash-tile { border-radius: 8px; padding: 14px 16px; }
  .dash-tile h4 { font-size: 12px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 8px; }
  .dash-tile ul { list-style: none; font-size: 12px; }
  .dash-tile ul li { padding: 3px 0; border-bottom: 1px solid rgba(0,0,0,0.06); }
  .dash-tile ul li:last-child { border-bottom: none; }

  /* TOP 3 */
  .top3 { counter-reset: top3; }
  .top3-item { display: flex; gap: 14px; align-items: flex-start; padding: 14px 16px; border-radius: 8px; margin-bottom: 10px; background: #fff; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
  .top3-num { width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; font-weight: 900; flex-shrink: 0; color: #fff; }
  .top3-num.n1 { background: #c62828; }
  .top3-num.n2 { background: #2e7d32; }
  .top3-num.n3 { background: #1565c0; }
  .top3-text h4 { font-size: 14px; font-weight: 700; margin-bottom: 3px; }
  .top3-text p  { font-size: 13px; color: #555; }

  .note { font-size: 12px; color: #666; font-style: italic; margin-top: 6px; }
  .divider { border: none; border-top: 1px solid #e0e0e0; margin: 14px 0; }
  .rescued-label { background: #fff8e1; border: 1px solid #ffe082; border-radius: 4px; padding: 1px 7px; font-size: 11px; color: #e65100; font-weight: 700; margin-left: 6px; }
  .auto-trash-label { background: #ffebee; border: 1px solid #ef9a9a; border-radius: 4px; padding: 1px 7px; font-size: 11px; color: #b71c1c; font-weight: 700; margin-left: 6px; }

  @media (max-width: 680px) {
    .header .meta { gap: 10px; }
    .cal-event { flex-direction: column; gap: 4px; }
  }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════════════════
     HEADER
════════════════════════════════════════════════════════════════ -->
<div class="header">
  <h1>📋 Executive Briefing — Melissa W</h1>
  <div class="subtitle">Prepared by your Executive Chief of Staff &nbsp;·&nbsp; Wednesday, August 5, 2026</div>
  <div class="meta">
    <div class="meta-item"><span>50</span>Emails Reviewed</div>
    <div class="meta-item"><span>8</span>Calendar Events</div>
    <div class="meta-item"><span>3</span>Action-Required Items</div>
    <div class="meta-item"><span>2</span>Today's Meetings</div>
    <div class="meta-item"><span>🔴 HIGH</span>LinkedIn Account Locked</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 0 — EMAIL TRIAGE QUICK LIST
════════════════════════════════════════════════════════════════ -->
<div class="section navy">
  <div class="section-title">📨 Section 0 — Email Triage Quick List</div>
  <div class="section-body">
    <p class="note" style="margin-bottom:10px;">✅ RESCUED = saved from Trash by protected-sender / importance rules &nbsp;|&nbsp; 📥 INBOX = arrived in inbox normally &nbsp;|&nbsp; Trash rows are collapsed — see Trash Review for details.</p>
    <table>
      <thead>
        <tr>
          <th style="width:120px;">Status</th>
          <th style="width:200px;">From</th>
          <th>Subject</th>
          <th>Summary</th>
        </tr>
      </thead>
      <tbody>
        <!-- RESCUED ROWS -->
        <tr class="rescued-row">
          <td class="triage-status">✅ RESCUED</td>
          <td>JetBlue Plus Card (Barclays)</td>
          <td>Simplify payments for your purchase</td>
          <td>Barclays Easy Pay offer. Rescued — protected financial sender.</td>
        </tr>
        <tr class="rescued-row">
          <td class="triage-status">✅ RESCUED</td>
          <td>LinkedIn (security-noreply)</td>
          <td>Account security alert — Create a new password</td>
          <td>LinkedIn password/security alert. Rescued — verified LinkedIn domain, critical account security.</td>
        </tr>
        <tr class="rescued-row">
          <td class="triage-status">✅ RESCUED</td>
          <td>Google (noreply-accounts)</td>
          <td>You shared some Google Account data with Claude</td>
          <td>Confirms Google data share with Claude. Rescued — legitimate Google account alert.</td>
        </tr>
        <tr class="rescued-row">
          <td class="triage-status">✅ RESCUED</td>
          <td>Charles Schwab</td>
          <td>Your account eStatement is available</td>
          <td>Schwab eStatement for account ending 284. Rescued — protected financial sender.</td>
        </tr>
        <tr class="rescued-row">
          <td class="triage-status">✅ RESCUED</td>
          <td>Match.com</td>
          <td>You've had a profile view from David</td>
          <td>David (66, Briarcliff Manor) viewed Melissa's profile. Rescued — protected sender.</td>
        </tr>
        <!-- INBOX ROWS -->
        <tr class="inbox-row">
          <td class="triage-status">📥 INBOX</td>
          <td>LinkedIn (messages-noreply)</td>
          <td>An update on your appeal</td>
          <td>LinkedIn appeal update — likely related to account restriction. HIGH PRIORITY.</td>
        </tr>
        <tr class="inbox-row">
          <td class="triage-status">📥 INBOX</td>
          <td>LinkedIn (security-noreply)</td>
          <td>Melissa A, here's the link to reset your password</td>
          <td>Password reset link — expires in 24 hours. HIGH PRIORITY.</td>
        </tr>
        <tr class="inbox-row">
          <td class="triage-status">📥 INBOX</td>
          <td>LinkedIn Customer Support</td>
          <td>Help with a Restriction [Case: 260804-031508]</td>
          <td>Auto-response to Melissa's restriction support ticket.</td>
        </tr>
        <tr class="inbox-row">
          <td class="triage-status">📥 INBOX</td>
          <td>LinkedIn Customer Support</td>
          <td>[Case: 260804-031185] — Identity Verification Issue</td>
          <td>LinkedIn support response to identity/backup email login issue.</td>
        </tr>
        <tr class="inbox-row">
          <td class="triage-status">📥 INBOX</td>
          <td>OpenArt Support</td>
          <td>Re: BILLING ISSUE WITH ACCOUNT — MELISSA W</td>
          <td>High volume delay reply to billing issue. Awaiting resolution.</td>
        </tr>
        <tr class="inbox-row">
          <td class="triage-status">📥 INBOX</td>
          <td>Indeed</td>
          <td>Director, Human Resources @ Vestis</td>
          <td>Indeed match for Director HR role at Vestis. Strong potential fit.</td>
        </tr>
        <tr class="inbox-row">
          <td class="triage-status">📥 INBOX</td>
          <td>LinkedIn (messages-noreply)</td>
          <td>Melissa A, add Stacey Gallagher</td>
          <td>CHRO / CPO connection suggestion — senior HR leader.</td>
        </tr>
        <tr class="inbox-row">
          <td class="triage-status">📥 INBOX</td>
          <td>LinkedIn (invitations)</td>
          <td>Charru Prruti invited you to follow Apes 2 Worc</td>
          <td>LinkedIn page follow invitation. Low priority.</td>
        </tr>
        <tr class="inbox-row">
          <td class="triage-status">📥 INBOX</td>
          <td>TikTok Shop</td>
          <td>2026 Stitchy, Handhe... just shipped</td>
          <td>Order shipped — tracking available.</td>
        </tr>
        <tr class="inbox-row">
          <td class="triage-status">📥 INBOX</td>
          <td>Netlify, Inc.</td>
          <td>Payment received — Invoice #RBCAOO-00012</td>
          <td>$9.80 charged. Invoice confirmed paid Aug 5, 2026.</td>
        </tr>
        <tr class="inbox-row">
          <td class="triage-status">📥 INBOX</td>
          <td>CALPAK</td>
          <td>Your 10% Off is Waiting</td>
          <td>10% off promo for next purchase. Low priority.</td>
        </tr>
        <tr class="inbox-row">
          <td class="triage-status">📥 INBOX</td>
          <td>SHEIN</td>
          <td>Have You Seen Our New Sportswear Arrivals?</td>
          <td>Promotional email — new sportswear. Low priority.</td>
        </tr>
        <tr class="inbox-row">
          <td class="triage-status">📥 INBOX</td>
          <td>PooPrints</td>
          <td>Rewards Await 🐾</td>
          <td>PooPrints community welcome / rewards. Low priority.</td>
        </tr>
        <!-- TRASH SUMMARY ROWS -->
        <tr class="trash-row">
          <td class="triage-status">🗑 AUTO-TRASHED</td>
          <td colspan="3">4 emails auto-trashed (phishing / fraud) — see Trash Review for details</td>
        </tr>
        <tr class="trash-row">
          <td class="triage-status">🗂 TRASH (manual)</td>
          <td colspan="3">14 emails in Trash (newsletters, retail promos, misc) — see Trash Review for details</td>
        </tr>
      </tbody>
    </table>
    <p class="note" style="margin-top:8px;">Note: Sent/outbox items from Melissa's own account (3 reply emails) are accounted for in the Full Email Review and Email Accounting table.</p>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 1 — EXECUTIVE SUMMARY
════════════════════════════════════════════════════════════════ -->
<div class="section red">
  <div class="section-title">⚡ Executive Summary</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li class="risk"><strong>🔴 BIGGEST RISK:</strong> Your LinkedIn account has been locked for 24+ hours. You have two open support cases (260804-031508 and 260804-031185), a password reset link expiring in 24 hours, and an appeal update waiting. This is blocking your active job search. Act immediately — use the password reset link before it expires.</li>
      <li class="opp"><strong>🟢 BIGGEST OPPORTUNITY:</strong> Indeed surfaced a Director of Human Resources role at Vestis — flagged as a strong match for your HR leadership background. Your Glassdoor alerts also show an HRBP role at TW Metals (remote) and 9 other positions. Two networking sessions today (12–1:30 PM) and a Stacey Gallagher CHRO connection suggestion offer immediate pipeline-building moments.</li>
      <li class="cal"><strong>🔵 BIGGEST CALENDAR ITEM:</strong> You have two overlapping events today at 12:00–1:30 PM: "HR Networking & Job Search Group Zoom" (RSVP pending) and "Network" (confirmed). Confirm your RSVP and resolve the conflict. Additionally, your MRI Brain appointment is Tuesday, Aug 11 at 8:50 AM — confirm the night before and leave valuables at home.</li>
    </ul>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 2 — ACTION REQUIRED
════════════════════════════════════════════════════════════════ -->
<div class="section red">
  <div class="section-title">🚨 Action Required</div>
  <div class="section-body">

    <div class="card card-red">
      <h3>🔐 LinkedIn Account — Use Password Reset Link NOW</h3>
      <div class="meta-row">
        <span><strong>Source:</strong> LinkedIn (security-noreply@linkedin.com)</span>
        <span><strong>Due:</strong> Within 24 hours of 4:45 AM UTC Aug 5 → expires ~4:45 AM Aug 6</span>
        <span><span class="badge badge-red">URGENT</span></span>
      </div>
      <p><strong>Why it matters:</strong> Your LinkedIn account has been restricted and you've been locked out for 24+ hours. LinkedIn sent a password reset link at 4:45 AM UTC and an appeal update shortly after. This link expires in 24 hours. Failure to act will require restarting the entire recovery process, further delaying your job search.</p>
      <p><strong>Recommended next step:</strong> Open the email "Melissa A, here's the link to reset your password" from security-noreply@linkedin.com and click the reset link immediately. Then check "An update on your appeal" to see the appeal decision. If access is still blocked, reply to Case 260804-031508 with your updated information.</p>
    </div>

    <div class="card card-yellow">
      <h3>💳 OpenArt — Billing Issue Awaiting Resolution</h3>
      <div class="meta-row">
        <span><strong>Source:</strong> OpenArt Support (support@openart.ai)</span>
        <span><strong>Due:</strong> Follow up if no response within 48–72 hours</span>
        <span><span class="badge badge-yellow">FOLLOW-UP</span></span>
      </div>
      <p><strong>Why it matters:</strong> OpenArt acknowledged your billing complaint but cited a backlog delay. A billing issue left unresolved can result in continued charges or service interruption.</p>
      <p><strong>Recommended next step:</strong> Note the date of their auto-reply (Aug 4). If no substantive response by Friday Aug 7, reply to the thread referencing the original case and request an ETA for resolution. Check your bank/card for any unexpected OpenArt charges in the meantime.</p>
    </div>

    <div class="card card-yellow">
      <h3>📅 RSVP — HR Networking & Job Search Group Zoom (Today, 12 PM)</h3>
      <div class="meta-row">
        <span><strong>Source:</strong> Google Calendar</span>
        <span><strong>Due:</strong> Today — event starts at 12:00 PM ET</span>
        <span><span class="badge badge-yellow">RSVP NEEDED</span></span>
      </div>
      <p><strong>Why it matters:</strong> You have not RSVPed to this 90-minute HR networking Zoom (status: needsAction) with 170+ attendees. This is a direct job-search asset while your LinkedIn is locked. You also have a second overlapping "Network" event confirmed at the same time — clarify which one you're attending.</p>
      <p><strong>Recommended next step:</strong> Confirm RSVP for the Zoom (link: https://us06web.zoom.us/j/81954171722) and prepare 1–2 sentences about your background and what roles you're targeting. Resolve the calendar conflict with the "Network" event at 12 PM.</p>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 3 — FULL 7-DAY CALENDAR
════════════════════════════════════════════════════════════════ -->
<div class="section blue">
  <div class="section-title">📅 Full 7-Day Calendar</div>
  <div class="section-body">

    <div class="cal-day">Wednesday, August 5, 2026 — TODAY</div>

    <div class="cal-event">
      <div class="cal-time">8:10 – 9:10 AM</div>
      <div class="cal-details">
        <h4>📞 Call Angel</h4>
        <div class="cal-meta">
          <span class="badge badge-blue">CONFIRMED</span> &nbsp;
          No attendees listed · No location
        </div>
        <div class="cal-meta" style="margin-top:4px;"><strong>Prep:</strong> Confirm what this call is regarding — personal or professional. Add notes if needed before the call.</div>
      </div>
    </div>

    <div class="cal-event conflict">
      <div class="cal-time">12:00 – 1:30 PM</div>
      <div class="cal-details">
        <h4>🌐 HR Networking & Job Search Group — Zoom 2 &nbsp;<span class="badge badge-orange">⚠️ RSVP PENDING</span></h4>
        <div class="cal-meta">
          Status: <strong>needsAction</strong> · 170+ attendees · Large group networking call
        </div>
        <div class="cal-meta"><a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1">Zoom Link (Zoom 2)</a></div>
        <div class="cal-meta" style="margin-top:4px;"><strong>Prep:</strong> Prepare 30-second intro. Review agenda/guidelines in the invitation email. RSVP now.</div>
        <div class="cal-meta" style="color:#e65100;"><strong>⚠️ CONFLICT:</strong> Overlaps with "Network" event below — same time slot.</div>
      </div>
    </div>

    <div class="cal-event conflict">
      <div class="cal-time">12:00 – 1:30 PM</div>
      <div class="cal-details">
        <h4>🤝 Network &nbsp;<span class="badge badge-orange">⚠️ CONFLICT</span></h4>
        <div class="cal-meta">
          Status: <strong>Confirmed</strong> · No attendees listed · No location
        </div>
        <div class="cal-meta" style="margin-top:4px;"><strong>Prep:</strong> Clarify what this event refers to and whether it's the same as the HR Networking Zoom above or a separate commitment.</div>
        <div class="cal-meta" style="color:#e65100;"><strong>⚠️ CONFLICT:</strong> Exact overlap with HR Networking Zoom. Resolve immediately.</div>
      </div>
    </div>

    <div class="cal-day">Thursday, August 6, 2026</div>

    <div class="cal-event">
      <div class="cal-time">9:00 – 11:00 AM</div>
      <div class="cal-details">
        <h4>♿ Disability Appointment</h4>
        <div class="cal-meta">
          Status: <strong>Confirmed</strong> · No attendees · No location listed
        </div>
        <div class="cal-meta" style="margin-top:4px;"><strong>Prep:</strong> Confirm appointment details and location. Bring any required documentation. Note 2-hour block — allow travel time if applicable.</div>
      </div>
    </div>

    <div class="cal-event declined">
      <div class="cal-time">9:00 – 10:30 AM</div>
      <div class="cal-details">
        <h4>🏢 Executive Roundtable — Zoom &nbsp;<span class="badge badge-gray">DECLINED</span></h4>
        <div class="cal-meta">
          Hosted by: John Madigan · Status: <strong>Declined</strong>
        </div>
        <div class="cal-meta"><a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09">Zoom Link</a> · Meeting ID: 207 786 667 · Password: 205454</div>
        <div class="cal-meta" style="margin-top:4px;"><strong>Note:</strong> You declined this event. If reconsideration is warranted, contact John Madigan before the event.</div>
        <div class="cal-meta" style="color:#e65100;"><strong>⚠️ CONFLICT:</strong> Overlaps with Disability appointment 9–11 AM.</div>
      </div>
    </div>

    <div class="cal-event">
      <div class="cal-time">12:00 – 1:00 PM</div>
      <div class="cal-details">
        <h4>🌐 HR Networking & Job Search: Open Office Hours — Zoom 2 &nbsp;<span class="badge badge-orange">RSVP PENDING</span></h4>
        <div class="cal-meta">
          Status: <strong>needsAction</strong> · 170+ attendees · Open discussion (no recording)
        </div>
        <div class="cal-meta"><a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1">Zoom Link</a></div>
        <div class="cal-meta" style="margin-top:4px;"><strong>Prep:</strong> No AI notetaking tools per organizer request. Informal open discussion format — great for 1:1 connections.</div>
      </div>
    </div>

    <div class="cal-day">Friday, August 7, 2026</div>

    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <h4>💰 State Farm Bill Due &nbsp;<span class="badge badge-yellow">DEADLINE</span></h4>
        <div class="cal-meta">Status: Confirmed · All-day reminder</div>
        <div class="cal-meta" style="margin-top:4px;"><strong>Prep:</strong> Pay or verify auto-pay is set up for State Farm insurance premium.</div>
      </div>
    </div>

    <div class="cal-day">Saturday, August 8 — Sunday, August 10, 2026</div>
    <div style="padding: 8px 10px; font-size:13px; color:#888;">No events scheduled.</div>

    <div class="cal-day">Tuesday, August 11, 2026</div>

    <div class="cal-event">
      <div class="cal-time">8:50 AM (appt 9:20 AM)</div>
      <div class="cal-details">
        <h4>🧠 MRI Brain W&WO IVC &nbsp;<span class="badge badge-red">MEDICAL</span></h4>
        <div class="cal-meta">Status: <strong>Confirmed</strong> · Arrive by 8:50 AM · Appointment starts 9:20 AM</div>
        <div class="cal-meta">📍 159 E 53rd Street, 6th Floor, New York, NY 10022 · 📞 646-754-2800</div>
        <div class="cal-meta" style="margin-top:4px;"><strong>Prep:</strong> Do not bring valuables. Remove all body piercings/jewelry before arrival. MRI-safe gown provided. Private dressing rooms available. Confirm appointment day before (Aug 10).</div>
      </div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 4 — JOB SEARCH & INTERVIEW PIPELINE
════════════════════════════════════════════════════════════════ -->
<div class="section green">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">

    <h3 style="margin-bottom:8px;font-size:14px;">🎯 Job Alerts & Leads</h3>
    <table>
      <thead>
        <tr>
          <th>Fit</th>
          <th>Role</th>
          <th>Company</th>
          <th>Source</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>Director, Human Resources</td>
          <td>Vestis</td>
          <td>Indeed (email match)</td>
          <td>Review & apply — flagged as strong match for your HR leadership background</td>
        </tr>
        <tr>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>Human Resource Business Partner – TW Metals</td>
          <td>TW Metals</td>
          <td>Glassdoor alert (Remote, US)</td>
          <td>Review — remote HRBP role aligns with background</td>
        </tr>
        <tr>
          <td><span class="badge badge-yellow">MEDIUM</span></td>
          <td>Talent Acquisition Partner</td>
          <td>Not specified</td>
          <td>Jobright (Eric) — 08/04/2026 (in Trash)</td>
          <td>Retrieve from Trash and review — references your Cprime experience</td>
        </tr>
        <tr>
          <td><span class="badge badge-gray">LOW</span></td>
          <td>Community Associate + 8 more jobs</td>
          <td>Various (NYC)</td>
          <td>Glassdoor alert</td>
          <td>Browse when convenient — mixed relevance to senior HR roles</td>
        </tr>
      </tbody>
    </table>

    <hr class="divider">
    <h3 style="margin-bottom:8px;font-size:14px;">🤝 Networking &amp; Connections</h3>
    <table>
      <thead>
        <tr>
          <th>Fit</th>
          <th>Contact</th>
          <th>Context</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>Stacey Gallagher — CHRO / CPO, M&amp;A Strategist</td>
          <td>LinkedIn connection suggestion</td>
          <td>Accept and send a personalized message referencing shared HR leadership focus</td>
        </tr>
        <tr>
          <td><span class="badge badge-yellow">MEDIUM</span></td>
          <td>HR Networking Group (170+ members)</td>
          <td>Today's Zoom 12–1:30 PM + Tomorrow's Office Hours 12–1 PM</td>
          <td>RSVP today, attend, introduce yourself, follow up 1:1 with relevant attendees</td>
        </tr>
        <tr>
          <td><span class="badge badge-gray">LOW</span></td>
          <td>Charru Prruti — Apes 2 Worc</td>
          <td>LinkedIn page follow invitation</td>
          <td>Review page before following — unknown relevance</td>
        </tr>
      </tbody>
    </table>

    <hr class="divider">
    <h3 style="margin-bottom:8px;font-size:14px;">📩 Sent by Melissa — Escalation to LinkedIn Leadership</h3>
    <div class="card card-green">
      <h3>Email to Mr. Shapero — LinkedIn Executive Escalation</h3>
      <p>Melissa sent a direct escalation email titled <em>"Urgent: Account Locked 24+ Hours, No Response After 8 Support Tickets"</em> to LinkedIn leadership (Mr. Shapero). Two open cases are on file (260804-031508, 260804-031185). This escalation is appropriate given the 24+ hour lockout during an active job search. Monitor for a response today.</p>
    </div>

    <hr class="divider">
    <p class="note">⚠️ LinkedIn lockout is directly impeding your job search. Resolving account access (see Action Required, Section 2) is the #1 prerequisite for all job search activities.</p>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 5 — FULL EMAIL REVIEW BY CATEGORY
════════════════════════════════════════════════════════════════ -->
<div class="section navy">
  <div class="section-title">📂 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="card card-red">
      <h3>🔐 Security / Risk &nbsp;<span class="badge badge-red">6 emails</span></h3>
      <div class="meta-row"><strong>Senders:</strong> LinkedIn (security-noreply ×2), Google (noreply-accounts), Auto-trashed: "💲melissaw212💲" (fake casino deposit), HILTON FINANCIAL MANAGEMENT (fake loan)</div>
      <p><strong>Summary:</strong></p>
      <ul style="margin:6px 0 0 16px;font-size:13px;">
        <li><strong>LinkedIn — Account security alert (rescued from Trash):</strong> Real LinkedIn security alert. RSVP/act on password reset immediately.</li>
        <li><strong>LinkedIn — Password reset link (inbox):</strong> Reset link expires in ~24 hrs from 4:45 AM UTC Aug 5. Use NOW.</li>
        <li><strong>Google — Data shared with Claude (rescued from Trash):</strong> Confirms Claude integration with Google account. Legitimate. Review if unexpected.</li>
        <li><strong>Auto-Trashed — Fake casino deposit "$13,963.99" (boiksupportrn@...):</strong> Classic advance-fee fraud with unrendered template variables. Removed automatically. No action needed.</li>
        <li><strong>Auto-Trashed — HILTON FINANCIAL MANAGEMENT loan (mail@alex-ua.com):</strong> Fake financial institution from unrelated domain. Advance-fee fraud. Removed automatically. No action needed.</li>
        <li><strong>LinkedIn — Appeal update (inbox):</strong> Update on Melissa's LinkedIn account appeal. READ IMMEDIATELY.</li>
      </ul>
      <p><strong>Recommended action:</strong> Act on password reset link now. Review appeal update. The two auto-trashed fraud emails require no further action.</p>
    </div>

    <!-- JOB SEARCH -->
    <div class="card card-green">
      <h3>💼 Job Search &nbsp;<span class="badge badge-green">4 emails</span></h3>
      <div class="meta-row"><strong>Senders:</strong> Indeed, Glassdoor (×2), Jobright (Eric)</div>
      <ul style="margin:6px 0 0 16px;font-size:13px;">
        <li><strong>Indeed — Director HR @ Vestis:</strong> Strong match per Indeed algorithm. Review and apply.</li>
        <li><strong>Glassdoor — HRBP at TW Metals + 9 remote roles:</strong> Includes strong remote HR opportunity.</li>
        <li><strong>Glassdoor — Community Associate + 8 NYC jobs:</strong> Mixed relevance; browse at leisure.</li>
        <li><strong>Jobright (Eric) — Talent Acquisition Partner (in Trash, unread=false):</strong> References Melissa's Cprime background. Retrieve from Trash and review.</li>
      </ul>
      <p><strong>Recommended action:</strong> Apply to Vestis Director HR role today. Review TW Metals HRBP. Retrieve Jobright email from Trash.</p>
    </div>

    <!-- RECRUITERS / NETWORKING -->
    <div class="card card-green">
      <h3>🤝 Recruiters / Networking &nbsp;<span class="badge badge-green">4 emails</span></h3>
      <div class="meta-row"><strong>Senders:</strong> LinkedIn (Stacey Gallagher connection), LinkedIn (Charru Prruti invitation), LinkedIn (1 person noticed you), LinkedIn Customer Support (×2 cases)</div>
      <ul style="margin:6px 0 0 16px;font-size:13px;">
        <li><strong>Add Stacey Gallagher (CHRO/CPO):</strong> High-value senior HR connection. Accept and personalize message.</li>
        <li><strong>Charru Prruti — follow Apes 2 Worc:</strong> Unknown relevance. Review before following.</li>
        <li><strong>1 person noticed you (LinkedIn):</strong> Profile visibility is up. Good sign during job search.</li>
        <li><strong>LinkedIn Support Cases 260804-031508 and 260804-031185:</strong> Account restriction support tickets. Monitor for responses after password reset.</li>
      </ul>
      <p><strong>Recommended action:</strong> Accept Stacey Gallagher connection. Monitor support cases after account recovery.</p>
    </div>

    <!-- CALENDAR / EVENTS -->
    <div class="card card-blue">
      <h3>📅 Calendar / Events &nbsp;<span class="badge badge-blue">2 emails</span></h3>
      <div class="meta-row"><strong>Senders:</strong> (Calendar invites reflected in Google Calendar data above — no standalone calendar emails in inbox beyond what's captured in calendar section)</div>
      <ul style="margin:6px 0 0 16px;font-size:13px;">
        <li>HR Networking Zoom events (Aug 5 &amp; Aug 6) are in calendar with RSVP pending.</li>
        <li>Executive Roundtable (Aug 6) — declined.</li>
      </ul>
      <p><strong>Recommended action:</strong> RSVP to Aug 5 and Aug 6 Networking Zooms.</p>
    </div>

    <!-- MEDICAL / HEALTH -->
    <div class="card card-red">
      <h3>🏥 Medical / Health &nbsp;<span class="badge badge-red">1 email</span></h3>
      <div class="meta-row"><strong>Senders:</strong> (MRI appointment is in Calendar data)</div>
      <ul style="margin:6px 0 0 16px;font-size:13px;">
        <li>MRI Brain W&amp;WO IVC — Aug 11, 8:50 AM, 159 E 53rd St, NYC. Confirmed in calendar.</li>
        <li>Also note: spam health emails (American Vitality water pills, Dr. Arthur_Green) were received but classified under spam/ignore.</li>
      </ul>
      <p><strong>Recommended action:</strong> Confirm appointment on Aug 10. Prepare per instructions (no valuables, remove jewelry).</p>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="card card-yellow">
      <h3>💳 Financial / Billing &nbsp;<span class="badge badge-yellow">7 emails</span></h3>
      <div class="meta-row"><strong>Senders:</strong> OpenArt Support, Netlify, Charles Schwab (rescued), Bank of America, UPS (BofA card delivery), JetBlue Plus Card/Barclays (rescued), Equifax</div>
      <ul style="margin:6px 0 0 16px;font-size:13px;">
        <li><strong>OpenArt — Billing Issue (inbox):</strong> Unresolved. Monitor and follow up by Aug 7.</li>
        <li><strong>Netlify — Payment confirmed $9.80, Invoice #RBCAOO-00012 (inbox):</strong> Paid. No action needed. File for records.</li>
        <li><strong>Charles Schwab — eStatement available, acct ending 284 (rescued):</strong> Log in and review statement.</li>
        <li><strong>Bank of America — Credit card 5690 shipped (Step 2 of 3):</strong> Card in transit. Watch for delivery.</li>
        <li><strong>UPS — BofA card package arriving tomorrow (Aug 6):</strong> Be home or arrange safe delivery.</li>
        <li><strong>JetBlue Plus Card / Barclays — Easy Pay offer (rescued):</strong> Promotional payment plan offer. Review if relevant to current balance.</li>
        <li><strong>Equifax — Apple Card credit limit offer:</strong> Pre-screened offer from Equifax. Review only if seeking new credit; otherwise ignore.</li>
      </ul>
      <p><strong>Recommended action:</strong> Follow up on OpenArt. Watch for BofA card delivery Aug 6. Review Schwab statement. State Farm bill due Aug 7 (calendar).</p>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="card card-purple">
      <h3>📚 Professional Development &nbsp;<span class="badge badge-purple">2 emails</span></h3>
      <div class="meta-row"><strong>Senders:</strong> Ruben Hassid / Substack, Gemma Bonham-Carter</div>
      <ul style="margin:6px 0 0 16px;font-size:13px;">
        <li><strong>Ruben Hassid — "Infographics" (in Trash):</strong> AI infographic guide. Relevant to AI/professional skills.</li>
        <li><strong>Gemma Bonham-Carter — $500 OFF Claude course (in Trash):</strong> Closing enrollment. If interested in Claude AI training, act before door closes.</li>
      </ul>
      <p><strong>Recommended action:</strong> Retrieve Ruben Hassid newsletter if AI skills are a current development goal. Evaluate Claude course if budget allows.</p>
    </div>

    <!-- PERSONAL -->
    <div class="card card-teal">
      <h3>🧍 Personal &nbsp;<span class="badge badge-teal">6 emails</span></h3>
      <div class="meta-row"><strong>Senders:</strong> Melissa W (sent ×3), Match.com (×2 + rescued ×1), OkCupid, HomeAgain PetRescuers, TikTok Shop</div>
      <ul style="margin:6px 0 0 16px;font-size:13px;">
        <li><strong>Melissa — sent emails (×3):</strong> LinkedIn escalation, case replies. Already noted in Job Search section.</li>
        <li><strong>Match — David likes you / David viewed profile (rescued):</strong> Dating app notification. Review when time allows.</li>
        <li><strong>Match — Eddie likes you:</strong> Another match notification.</li>
        <li><strong>OkCupid — "You're a catch":</strong> Promotional engagement email.</li>
        <li><strong>HomeAgain — Lost cat near Glendale, NY (Ref HAP-1920069):</strong> Lost pet alert for your area. Check if you recognize the pet or wish to share locally.</li>
        <li><strong>TikTok Shop — Order shipped (inbox):</strong> Track your shipment.</li>
      </ul>
      <p><strong>Recommended action:</strong> Track TikTok order. Review dating app matches at leisure.</p>
    </div>

    <!-- NEWSLETTERS / SUBSCRIPTIONS -->
    <div class="card card-purple">
      <h3>📰 Newsletters / Subscriptions &nbsp;<span class="badge badge-purple">4 emails</span></h3>
      <div class="meta-row"><strong>Senders:</strong> Ruben Hassid / Substack (×2), Alison Courses (in Trash), Insider Monkey (in Trash)</div>
      <ul style="margin:6px 0 0 16px;font-size:13px;">
        <li><strong>Ruben Hassid — "Infographics" (in Trash):</strong> AI how-to content. Possibly useful.</li>
        <li><strong>Ruben Hassid — "Everything is code, even you" (in Trash):</strong> AI/tech philosophy. Duplicate-like send from same author.</li>
        <li><strong>Alison Courses — "What could you learn in 15 minutes?" (in Trash):</strong> Free online course platform. Review if interested in upskilling.</li>
        <li><strong>Insider Monkey — Daily Newsletter Aug 4 (in Trash):</strong> Stock/investment newsletter. Low priority unless actively investing.</li>
      </ul>
      <p><strong>Recommended action:</strong> Keep Ruben Hassid if AI skills are a priority. Unsubscribe from Insider Monkey if not actively using. Evaluate Alison Courses subscription relevance.</p>
    </div>

    <!-- PROMOTIONAL / RETAIL -->
    <div class="card card-gray">
      <h3>🛍️ Promotional / Retail &nbsp;<span class="badge badge-gray">10 emails</span></h3>
      <div class="meta-row"><strong>Senders:</strong> Kohl's (Trash), YesStyle ×2 (Trash), CALPAK (inbox), SHEIN (inbox), Old Navy (Trash), Gap Factory (Trash), PooPrints (inbox)</div>
      <p>See Promotional / Retail Summary section for full breakdown.</p>
    </div>

    <!-- SPAM / SAFE TO DELETE / IGNORE -->
    <div class="card card-gray">
      <h3>🚫 Spam / Safe to Delete / Ignore &nbsp;<span class="badge badge-gray">6 emails</span></h3>
      <div class="meta-row"><strong>Senders:</strong> American Vitality, DirectMeds Weight Loss, "F*ckMeHard" (adult spam), Dr. Arthur_Green (adult spam), OnlineCasino (casino spam), LinkedIn — "Charru Prruti / Apes 2 Worc" (borderline)</div>
      <ul style="margin:6px 0 0 16px;font-size:13px;">
        <li><strong>American Vitality — "Unlock your body's flow":</strong> Health spam. Not in inbox or trash — likely filtered. Delete/ignore.</li>
        <li><strong>DirectMeds — GLP-1 weight loss:</strong> Unsolicited medical ad. Delete/ignore.</li>
        <li><strong>"F*ckMeHard" — adult spam:</strong> Explicit adult spam from random domain. Delete/block.</li>
        <li><strong>"Dr. Arthur_Green" — add 3.8 inches:</strong> Adult/health spam. Delete/block.</li>
        <li><strong>OnlineCasino — 130 Free Spins:</strong> Casino spam from random domain. Delete/ignore.</li>
      </ul>
      <p><strong>Recommended action:</strong> Mark all as spam and delete. Consider adding domain blocks.</p>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 6 — TRASH REVIEW
════════════════════════════════════════════════════════════════ -->
<div class="section gray">
  <div class="section-title">🗑️ Trash Review</div>
  <div class="section-body">

    <h3 style="margin-bottom:8px;color:#b71c1c;font-size:14px;">🔴 Restore Immediately</h3>
    <table>
      <thead>
        <tr><th>Sender</th><th>Subject</th><th>Reason to Restore</th><th>Status</th></tr>
      </thead>
      <tbody>
        <tr style="background:#fff8e1;">
          <td>LinkedIn (security-noreply)</td>
          <td>Account security alert — Create a new password</td>
          <td>Critical LinkedIn account security notification from verified domain — already restored</td>
          <td><span class="rescued-label">✅ RESCUED</span></td>
        </tr>
        <tr style="background:#fff8e1;">
          <td>Google (noreply-accounts)</td>
          <td>You shared some Google Account data with Claude</td>
          <td>Legitimate Google account activity alert — already restored</td>
          <td><span class="rescued-label">✅ RESCUED</span></td>
        </tr>
        <tr style="background:#fff8e1;">
          <td>Charles Schwab</td>
          <td>Your account eStatement is available</td>
          <td>Protected financial sender — already restored</td>
          <td><span class="rescued-label">✅ RESCUED</span></td>
        </tr>
        <tr style="background:#fff8e1;">
          <td>JetBlue Plus Card / Barclays</td>
          <td>Simplify payments for your purchase</td>
          <td>Protected financial sender — already restored</td>
          <td><span class="rescued-label">✅ RESCUED</span></td>
        </tr>
        <tr style="background:#fff8e1;">
          <td>Match.com</td>
          <td>You've had a profile view from David</td>
          <td>Protected sender — already restored</td>
          <td><span class="rescued-label">✅ RESCUED</span></td>
        </tr>
        <tr>
          <td>Jobright (Eric)</td>
          <td>You are Invited! Talent Acquisition Partner — 08/04/2026</td>
          <td>References your Cprime background — relevant recruiter outreach during active job search</td>
          <td><span class="badge badge-yellow">REVIEW & RESTORE</span></td>
        </tr>
      </tbody>
    </table>

    <hr class="divider">
    <h3 style="margin-bottom:8px;color:#e65100;font-size:14px;">🟡 Review Before Deleting</h3>
    <table>
      <thead>
        <tr><th>Sender</th><th>Subject</th><th>Notes</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Ruben Hassid / Substack</td>
          <td>"Infographics" + "Everything is code, even you"</td>
          <td>AI/professional content. Keep if actively building AI skills; unsubscribe otherwise.</td>
        </tr>
        <tr>
          <td>Gemma Bonham-Carter</td>
          <td>$500 OFF the Claude course</td>
          <td>Course enrollment closing — retrieve if interested in AI training investment.</td>
        </tr>
        <tr>
          <td>Alison Courses</td>
          <td>What could you learn in 15 minutes?</td>
          <td>Free learning platform. Review if upskilling is a current goal.</td>
        </tr>
      </tbody>
    </table>

    <hr class="divider">
    <h3 style="margin-bottom:8px;color:#2e7d32;font-size:14px;">🟢 Safe to Delete</h3>
    <table>
      <thead>
        <tr><th>Sender</th><th>Subject</th><th>Reason</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Kohl's</td>
          <td>Up to 70% off — ULTIMATE Clearance Event</td>
          <td>Retail promotional. Already trashed. Safe to permanently delete.</td>
        </tr>
        <tr>
          <td>YesStyle.com ×2</td>
          <td>Back-to-school sale; Happy 1-Year Anniversary 12% OFF</td>
          <td>Retail promotional. Safe to delete.</td>
        </tr>
        <tr>
          <td>Old Navy Super Cash</td>
          <td>Double win: use your Super Cash on $16 sweatshirts</td>
          <td>Retail promotional. Safe to delete.</td>
        </tr>
        <tr>
          <td>Gap Factory</td>
          <td>50–70% off sitewide — ends tonight</td>
          <td>Retail promotional — offer likely expired. Safe to delete.</td>
        </tr>
        <tr>
          <td>Insider Monkey</td>
          <td>Daily Newsletter Aug 4, 2026</td>
          <td>Investment newsletter. Safe to delete unless actively using.</td>
        </tr>
        <tr>
          <td>"💲melissaw212💲" (boiksupportrn)</td>
          <td>You received a direct deposit of $13,963.99</td>
          <td><span class="auto-trash-label">AUTO-TRASHED — PHISHING</span> Fake payment with unrendered template variables. Advance-fee fraud. Delete permanently.</td>
        </tr>
        <tr>
          <td>HILTON FINANCIAL MANAGEMENT (mail@alex-ua.com)</td>
          <td>LOAN</td>
          <td><span class="auto-trash-label">AUTO-TRASHED — PHISHING</span> Fake financial institution / advance-fee fraud. Delete permanently.</td>
        </tr>
      </tbody>
    </table>

    <p class="note" style="margin-top:8px;">Note: Auto-trashed phishing emails (2) were removed before reaching inbox. No further action required beyond permanent deletion.</p>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 7 — PROMOTIONAL / RETAIL SUMMARY
════════════════════════════════════════════════════════════════ -->
<div class="section gray">
  <div class="section-title">🛍️ Promotional / Retail Summary</div>
  <div class="section-body">
    <table>
      <thead>
        <tr>
          <th>Brand</th>
          <th>Count</th>
          <th>Subject / Theme</th>
          <th>Location</th>
          <th>Recommendation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>CALPAK</td>
          <td>1</td>
          <td>10% off your next purchase — travel gear</td>
          <td>Inbox</td>
          <td><span class="badge badge-blue">REVIEW</span> Keep if planning travel purchase</td>
        </tr>
        <tr>
          <td>SHEIN</td>
          <td>1</td>
          <td>New sportswear
