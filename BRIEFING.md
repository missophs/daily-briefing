<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa W — August 1, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px 60px; }

  /* Header */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 15px; color: #b0c4de; margin-top: 6px; }
  .header .meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.1); border-radius: 8px; padding: 10px 18px; text-align: center; }
  .header .meta-item .num { font-size: 22px; font-weight: 700; color: #7ec8e3; }
  .header .meta-item .lbl { font-size: 11px; color: #b0c4de; text-transform: uppercase; letter-spacing: 1px; }

  /* Section */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; letter-spacing: 0.3px; padding: 10px 16px; border-radius: 8px 8px 0 0; display: flex; align-items: center; gap: 8px; }
  .section-body { background: #fff; border-radius: 0 0 10px 10px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }

  /* Color themes */
  .red .section-title    { background: #c0392b; color: #fff; }
  .yellow .section-title { background: #f39c12; color: #fff; }
  .blue .section-title   { background: #2471a3; color: #fff; }
  .green .section-title  { background: #1e8449; color: #fff; }
  .purple .section-title { background: #7d3c98; color: #fff; }
  .gray .section-title   { background: #717d7e; color: #fff; }
  .navy .section-title   { background: #1a1a2e; color: #fff; }
  .teal .section-title   { background: #148f77; color: #fff; }

  /* Tables */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #f4f6f8; font-weight: 700; text-align: left; padding: 9px 10px; border-bottom: 2px solid #dde; color: #444; }
  td { padding: 8px 10px; border-bottom: 1px solid #eef; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f9fbff; }

  /* Cards */
  .card { border-left: 5px solid #ccc; background: #fafafa; border-radius: 6px; padding: 14px 16px; margin-bottom: 12px; }
  .card.red    { border-color: #c0392b; background: #fdf3f2; }
  .card.yellow { border-color: #f39c12; background: #fefaf0; }
  .card.blue   { border-color: #2471a3; background: #f0f6fd; }
  .card.green  { border-color: #1e8449; background: #f0faf3; }
  .card.purple { border-color: #7d3c98; background: #f8f0fd; }
  .card.gray   { border-color: #717d7e; background: #f7f7f7; }
  .card.teal   { border-color: #148f77; background: #f0faf8; }
  .card-label { font-size: 10px; font-weight: 800; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 4px; }
  .card-label.red    { color: #c0392b; }
  .card-label.yellow { color: #d68910; }
  .card-label.blue   { color: #2471a3; }
  .card-label.green  { color: #1e8449; }
  .card-label.purple { color: #7d3c98; }
  .card-label.gray   { color: #717d7e; }
  .card-label.teal   { color: #148f77; }
  .card-title { font-size: 15px; font-weight: 700; margin-bottom: 6px; }
  .card-row { display: flex; gap: 6px; margin-bottom: 3px; font-size: 13px; flex-wrap: wrap; }
  .card-field { font-weight: 700; color: #555; min-width: 110px; }

  /* Badges */
  .badge { display: inline-block; border-radius: 12px; padding: 2px 10px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
  .badge-red    { background: #fdecea; color: #c0392b; border: 1px solid #f5c6c2; }
  .badge-yellow { background: #fef9e7; color: #b7770d; border: 1px solid #f9e49a; }
  .badge-green  { background: #eafaf1; color: #1e8449; border: 1px solid #a9dfbf; }
  .badge-blue   { background: #eaf3fb; color: #1a5276; border: 1px solid #a9cce3; }
  .badge-purple { background: #f5eef8; color: #7d3c98; border: 1px solid #d2b4de; }
  .badge-gray   { background: #f2f3f4; color: #717d7e; border: 1px solid #d5d8dc; }
  .badge-teal   { background: #e8f8f5; color: #148f77; border: 1px solid #a2d9ce; }

  /* Executive Summary bullets */
  .exec-bullet { display: flex; align-items: flex-start; gap: 12px; margin-bottom: 12px; padding: 12px 14px; border-radius: 8px; }
  .exec-bullet.risk   { background: #fdf3f2; border: 1px solid #f5c6c2; }
  .exec-bullet.opp    { background: #f0faf3; border: 1px solid #a9dfbf; }
  .exec-bullet.cal    { background: #f0f6fd; border: 1px solid #a9cce3; }
  .exec-icon { font-size: 22px; margin-top: 1px; }
  .exec-text strong { display: block; font-size: 14px; margin-bottom: 3px; }
  .exec-text span { font-size: 13px; color: #555; }

  /* Dashboard grid */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 14px; }
  .dash-card { background: #fff; border-radius: 10px; padding: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); text-align: center; }
  .dash-card .dash-num { font-size: 32px; font-weight: 800; }
  .dash-card .dash-lbl { font-size: 12px; color: #777; margin-top: 4px; text-transform: uppercase; letter-spacing: 0.8px; }
  .dash-card.d-red    { border-top: 4px solid #c0392b; }
  .dash-card.d-yellow { border-top: 4px solid #f39c12; }
  .dash-card.d-green  { border-top: 4px solid #1e8449; }
  .dash-card.d-blue   { border-top: 4px solid #2471a3; }
  .dash-card.d-purple { border-top: 4px solid #7d3c98; }
  .dash-card.d-gray   { border-top: 4px solid #717d7e; }

  /* Priority table */
  .priority-HIGH   { color: #c0392b; font-weight: 800; }
  .priority-MEDIUM { color: #d68910; font-weight: 700; }
  .priority-LOW    { color: #1e8449; font-weight: 600; }

  /* Status icons */
  .status-confirmed { color: #1e8449; }
  .status-declined  { color: #c0392b; }
  .status-needs     { color: #d68910; }

  /* Top 3 */
  .top3 { display: flex; gap: 16px; flex-wrap: wrap; }
  .top3-card { flex: 1; min-width: 220px; background: linear-gradient(135deg, #1a1a2e, #0f3460); color: #fff; border-radius: 12px; padding: 22px 20px; }
  .top3-num { font-size: 40px; font-weight: 900; color: #7ec8e3; line-height: 1; }
  .top3-text { font-size: 15px; margin-top: 8px; line-height: 1.5; }

  /* Triage table status */
  .t-rescued { color: #1e8449; font-weight: 700; }
  .t-inbox   { color: #2471a3; font-weight: 700; }
  .t-trash   { color: #c0392b; font-weight: 700; }
  .t-manual  { color: #717d7e; font-weight: 700; }

  .note { font-size: 12px; color: #888; font-style: italic; margin-top: 8px; }
  .divider { border: none; border-top: 1px solid #e8eaec; margin: 14px 0; }
  .pill { display: inline-block; background: #eef; border-radius: 20px; padding: 2px 10px; font-size: 11px; color: #445; margin: 2px; }

  @media (max-width: 600px) {
    .header .meta { gap: 12px; }
    .top3 { flex-direction: column; }
    .dash-grid { grid-template-columns: repeat(2, 1fr); }
  }
</style>
</head>
<body>
<div class="page">

<!-- ══════════════════════════════════════════════════════
     SECTION 0: EMAIL TRIAGE QUICK LIST
     ══════════════════════════════════════════════════════ -->
<div class="section navy">
  <div class="section-title">⚡ Email Triage Quick List — Saturday, August 1, 2026</div>
  <div class="section-body">
    <p style="font-size:13px;color:#555;margin-bottom:12px;">Rescued emails listed first, then Inbox emails, then collapsed trash summary rows. One row per individual email for items needing attention.</p>
    <table>
      <thead>
        <tr>
          <th style="width:130px;">Status</th>
          <th style="width:200px;">From</th>
          <th>Subject</th>
          <th>Summary</th>
        </tr>
      </thead>
      <tbody>
        <!-- INBOX EMAILS — Individual rows -->
        <tr>
          <td><span class="t-inbox">📥 INBOX</span></td>
          <td>Bank of America</td>
          <td>Billing Dispute for account – 4018</td>
          <td>Step 2 of 3 — BOA needs additional information to proceed with your billing dispute. <strong>Action required.</strong></td>
        </tr>
        <tr>
          <td><span class="t-inbox">📥 INBOX</span></td>
          <td>Bilt Rewards</td>
          <td>Your rent payment is processing</td>
          <td>Rent payment in progress; earning 1.25X Bilt Points. Monitor for confirmation.</td>
        </tr>
        <tr>
          <td><span class="t-inbox">📥 INBOX</span></td>
          <td>Old Navy</td>
          <td>Order Confirmation #1RDGPJ0</td>
          <td>Order placed Fri Jul 31. Retain for records / tracking.</td>
        </tr>
        <tr>
          <td><span class="t-inbox">📥 INBOX</span></td>
          <td>Old Navy</td>
          <td>Re: Order pending! Complete your purchase</td>
          <td>Abandoned cart reminder. Already placed order above — likely safe to ignore.</td>
        </tr>
        <tr>
          <td><span class="t-inbox">📥 INBOX</span></td>
          <td>Verizon</td>
          <td>Your bill is now available online</td>
          <td>Monthly bill ready. Review and schedule payment.</td>
        </tr>
        <tr>
          <td><span class="t-inbox">📥 INBOX</span></td>
          <td>LinkedIn</td>
          <td>New jobs similar to HR Director at NY Post</td>
          <td>Job alert in inbox — review similar roles. Unread.</td>
        </tr>
        <!-- COLLAPSED TRASH ROWS -->
        <tr style="background:#fff8f8;">
          <td><span class="t-trash">🗑 AUTO-TRASHED</span></td>
          <td colspan="3"><strong>1 email auto-trashed (phishing)</strong> — Cloud storage payment-threat scam targeting melissaw212. See Trash Review § for full details.</td>
        </tr>
        <tr style="background:#f7f7f7;">
          <td><span class="t-manual">🗂 TRASH (manual)</span></td>
          <td colspan="3"><strong>3 emails in Trash</strong> (Kohl's promo, Alison Courses newsletter, Jack Cocchiarella Substack, Glassdoor duplicate) — See Trash Review § for full details.</td>
        </tr>
      </tbody>
    </table>
    <p class="note">All remaining emails (non-inbox, non-trashed) reviewed and categorized in Full Email Review section below.</p>
  </div>
</div>

<!-- ══════════════════════════════════════════════════════
     SECTION 1: HEADER
     ══════════════════════════════════════════════════════ -->
<div class="header">
  <div style="font-size:13px;color:#7ec8e3;font-weight:600;letter-spacing:1px;text-transform:uppercase;margin-bottom:6px;">Executive Briefing</div>
  <h1>Good Morning, Melissa ☀️</h1>
  <div class="subtitle">Saturday, August 1, 2026 &nbsp;·&nbsp; Prepared by your Executive Chief of Staff</div>
  <div class="meta">
    <div class="meta-item"><div class="num">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="meta-item"><div class="num">9</div><div class="lbl">Calendar Events</div></div>
    <div class="meta-item"><div class="num">6</div><div class="lbl">Inbox Items</div></div>
    <div class="meta-item"><div class="num">3</div><div class="lbl">Action Required</div></div>
    <div class="meta-item"><div class="num">1</div><div class="lbl">Security Alert</div></div>
    <div class="meta-item"><div class="num">8</div><div class="lbl">Job Leads</div></div>
  </div>
</div>

<!-- ══════════════════════════════════════════════════════
     SECTION 2: EXECUTIVE SUMMARY
     ══════════════════════════════════════════════════════ -->
<div class="section red">
  <div class="section-title">🎯 Executive Summary</div>
  <div class="section-body">
    <div class="exec-bullet risk">
      <div class="exec-icon">🔴</div>
      <div class="exec-text">
        <strong>BIGGEST RISK: Bank of America Billing Dispute — Step 2 of 3 Requires Your Response</strong>
        <span>BOA has flagged account #4018 and is requesting additional information for an active billing dispute. This is time-sensitive and inaction could stall or close the dispute in the other party's favor. Additionally, one phishing email (cloud storage scareware targeting your username) was auto-trashed and flagged for your awareness.</span>
      </div>
    </div>
    <div class="exec-bullet opp">
      <div class="exec-icon">🟢</div>
      <div class="exec-text">
        <strong>BIGGEST OPPORTUNITY: Active Job Search Pipeline with Multiple Senior HR Leads</strong>
        <span>LinkedIn, Glassdoor, and Jobright have surfaced multiple senior-level openings (VP of People at Nitra, Head of People at Adonis, Head of People NA at Artefact, Senior Director PBP via Jobright, HR Director at NY Post area). You also personally sent outreach to Michael (resume + website) and Amy/Sam at CVS for a Corporate Affairs HR role. Two HR networking Zoom sessions are scheduled next week to keep your pipeline warm.</span>
      </div>
    </div>
    <div class="exec-bullet cal">
      <div class="exec-icon">🔵</div>
      <div class="exec-text">
        <strong>BIGGEST CALENDAR ITEM: Eye Doctor Today at 2:30 PM + Two Unconfirmed Zoom Networking Sessions Next Week</strong>
        <span>Eye appointment is today (Aug 1, 2:30–3:30 PM). Two HR networking Zoom sessions on Aug 5 and Aug 6 show status "needsAction" — RSVP needed. State Farm insurance bill due reminder appears Aug 7. Physical therapy is Aug 4.</span>
      </div>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════════════════
     SECTION 3: ACTION REQUIRED
     ══════════════════════════════════════════════════════ -->
<div class="section yellow">
  <div class="section-title">⚠️ Action Required</div>
  <div class="section-body">

    <div class="card yellow">
      <div class="card-label yellow">🔴 URGENT — FINANCIAL</div>
      <div class="card-title">Bank of America — Billing Dispute Step 2 of 3 (Account #4018)</div>
      <div class="card-row"><span class="card-field">Source:</span> Bank of America — onlinebanking@ealerts.bankofamerica.com</div>
      <div class="card-row"><span class="card-field">Why it matters:</span> Active billing dispute is at Step 2 of 3. BOA needs additional information from you to continue. Missing this window could result in the dispute being closed unfavorably.</div>
      <div class="card-row"><span class="card-field">Next Step:</span> Log in to bankofamerica.com or call the number on the email to provide the requested documentation. Do NOT click links in the email — navigate directly.</div>
      <div class="card-row"><span class="card-field">Due Date:</span> As soon as possible — time-sensitive dispute window.</div>
    </div>

    <div class="card yellow">
      <div class="card-label yellow">⚠️ RSVP NEEDED — NETWORKING</div>
      <div class="card-title">RSVP to HR Networking Zoom Sessions — Aug 5 & Aug 6</div>
      <div class="card-row"><span class="card-field">Source:</span> Google Calendar — "HR Networking & Job Search Group – Zoom 2" + "HR Networking Open Office Hours"</div>
      <div class="card-row"><span class="card-field">Why it matters:</span> Both events show status "needsAction" — you have not confirmed attendance. These are large peer networking sessions directly relevant to your job search. Organizers may use RSVPs to manage links.</div>
      <div class="card-row"><span class="card-field">Next Step:</span> Open calendar invites and click Accept. Zoom links are already embedded in both invites.</div>
      <div class="card-row"><span class="card-field">Due Date:</span> Aug 5 (12:00 PM) and Aug 6 (12:00 PM).</div>
    </div>

    <div class="card yellow">
      <div class="card-label yellow">💰 BILLING — REMINDER</div>
      <div class="card-title">Verizon Monthly Bill Now Available + State Farm Bill Due Aug 7</div>
      <div class="card-row"><span class="card-field">Source:</span> Verizon Notification email + State Farm calendar reminder (Aug 7)</div>
      <div class="card-row"><span class="card-field">Why it matters:</span> Two bills converging this weekend. Verizon bill available now; State Farm reminder set for Aug 7.</div>
      <div class="card-row"><span class="card-field">Next Step:</span> Review and pay Verizon bill. Confirm State Farm auto-pay or set manual payment before Aug 7.</div>
      <div class="card-row"><span class="card-field">Due Date:</span> Verizon: review now. State Farm: Aug 7.</div>
    </div>

    <div class="card green">
      <div class="card-label green">💼 JOB SEARCH — FOLLOW-UP</div>
      <div class="card-title">Follow Up on Outreach to Michael, Amy (CVS), and Sam (CVS)</div>
      <div class="card-row"><span class="card-field">Source:</span> Sent emails from melissaw212@gmail.com on Jul 31, 2026</div>
      <div class="card-row"><span class="card-field">Why it matters:</span> You sent a targeted resume + website to "Michael" and two tailored pitches to Amy and Sam at CVS for a Corporate Affairs HR role. These are warm outreach efforts and weekend follow-up planning ensures you're ready to respond quickly Monday.</div>
      <div class="card-row"><span class="card-field">Next Step:</span> Log these contacts in your tracker. If no response by Wednesday, Aug 5, send a brief follow-up note.</div>
      <div class="card-row"><span class="card-field">Due Date:</span> Monitor Mon–Wed, Aug 3–5.</div>
    </div>

  </div>
</div>

<!-- ══════════════════════════════════════════════════════
     SECTION 4: FULL 7-DAY CALENDAR
     ══════════════════════════════════════════════════════ -->
<div class="section blue">
  <div class="section-title">📅 Full 7-Day Calendar — Aug 1–7, 2026</div>
  <div class="section-body">

    <!-- Saturday Aug 1 -->
    <div style="margin-bottom:18px;">
      <div style="font-weight:800;font-size:15px;color:#2471a3;border-bottom:2px solid #d0e8f8;padding-bottom:6px;margin-bottom:10px;">📆 Saturday, August 1, 2026 — TODAY</div>
      <div class="card blue">
        <div class="card-label blue">TODAY · CONFIRMED</div>
        <div class="card-title">👁 Eye Doctor Appointment</div>
        <div class="card-row"><span class="card-field">Time:</span> 2:30 PM – 3:30 PM (1 hour)</div>
        <div class="card-row"><span class="card-field">Location:</span> Not specified in calendar</div>
        <div class="card-row"><span class="card-field">Status:</span> <span class="status-confirmed">✅ Confirmed</span></div>
        <div class="card-row"><span class="card-field">Prep Needed:</span> Confirm address, arrange transportation if needed (dilation may affect driving). Bring insurance card.</div>
        <div class="card-row"><span class="card-field">Conflict:</span> None.</div>
      </div>
    </div>

    <!-- Sunday Aug 2 -->
    <div style="margin-bottom:18px;">
      <div style="font-weight:800;font-size:15px;color:#2471a3;border-bottom:2px solid #d0e8f8;padding-bottom:6px;margin-bottom:10px;">📆 Sunday, August 2, 2026</div>
      <div class="card blue">
        <div class="card-label blue">ALL DAY · CONFIRMED</div>
        <div class="card-title">🎂 Shari's Birthday</div>
        <div class="card-row"><span class="card-field">Time:</span> All Day (Aug 2–2, spans into Aug 3)</div>
        <div class="card-row"><span class="card-field">Status:</span> <span class="status-confirmed">✅ Confirmed</span></div>
        <div class="card-row"><span class="card-field">Prep Needed:</span> Send birthday message, gift, or plan if celebrating together. Don't forget!</div>
        <div class="card-row"><span class="card-field">Conflict:</span> None.</div>
      </div>
    </div>

    <!-- Monday Aug 3 -->
    <div style="margin-bottom:18px;">
      <div style="font-weight:800;font-size:15px;color:#2471a3;border-bottom:2px solid #d0e8f8;padding-bottom:6px;margin-bottom:10px;">📆 Monday, August 3, 2026</div>
      <div style="padding:10px;font-size:13px;color:#888;font-style:italic;">No calendar events scheduled. Good day to follow up on job applications and BOA billing dispute.</div>
    </div>

    <!-- Tuesday Aug 4 -->
    <div style="margin-bottom:18px;">
      <div style="font-weight:800;font-size:15px;color:#2471a3;border-bottom:2px solid #d0e8f8;padding-bottom:6px;margin-bottom:10px;">📆 Tuesday, August 4, 2026</div>
      <div class="card blue">
        <div class="card-label blue">MORNING · CONFIRMED</div>
        <div class="card-title">🏥 Physical Therapy (PT)</div>
        <div class="card-row"><span class="card-field">Time:</span> 10:00 AM – 11:00 AM (1 hour)</div>
        <div class="card-row"><span class="card-field">Location:</span> Not specified</div>
        <div class="card-row"><span class="card-field">Status:</span> <span class="status-confirmed">✅ Confirmed</span></div>
        <div class="card-row"><span class="card-field">Prep Needed:</span> Wear comfortable clothing. Confirm address and any co-pay requirements.</div>
        <div class="card-row"><span class="card-field">Conflict:</span> None.</div>
      </div>
    </div>

    <!-- Wednesday Aug 5 -->
    <div style="margin-bottom:18px;">
      <div style="font-weight:800;font-size:15px;color:#2471a3;border-bottom:2px solid #d0e8f8;padding-bottom:6px;margin-bottom:10px;">📆 Wednesday, August 5, 2026</div>

      <div class="card yellow">
        <div class="card-label yellow">⚠️ RSVP NEEDED — ZOOM</div>
        <div class="card-title">HR Networking &amp; Job Search Group — Zoom Session 2</div>
        <div class="card-row"><span class="card-field">Time:</span> 12:00 PM – 1:30 PM</div>
        <div class="card-row"><span class="card-field">Link:</span> <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" style="color:#2471a3;" target="_blank">Join Zoom Meeting</a></div>
        <div class="card-row"><span class="card-field">Status:</span> <span class="status-needs">⏳ Needs Action — RSVP Required</span></div>
        <div class="card-row"><span class="card-field">Attendees:</span> 160+ HR professionals</div>
        <div class="card-row"><span class="card-field">Prep Needed:</span> Review HR Networking Team Guidelines (link in invite). Prepare 30-second intro. Test Zoom link in advance. Disable AI note-taking tools per organizer request.</div>
        <div class="card-row"><span class="card-field">Conflict:</span> Overlaps with "Network" calendar block (same time, same day — likely the same event double-booked).</div>
      </div>

      <div class="card blue">
        <div class="card-label blue">MIDDAY · CONFIRMED</div>
        <div class="card-title">📡 Network (personal block)</div>
        <div class="card-row"><span class="card-field">Time:</span> 12:00 PM – 1:30 PM</div>
        <div class="card-row"><span class="card-field">Status:</span> <span class="status-confirmed">✅ Confirmed</span></div>
        <div class="card-row"><span class="card-field">Conflict Note:</span> Appears to be the same timeslot as the HR Networking Zoom above — likely a personal reminder block for the same session. No issue.</div>
      </div>
    </div>

    <!-- Thursday Aug 6 -->
    <div style="margin-bottom:18px;">
      <div style="font-weight:800;font-size:15px;color:#2471a3;border-bottom:2px solid #d0e8f8;padding-bottom:6px;margin-bottom:10px;">📆 Thursday, August 6, 2026</div>

      <div class="card red">
        <div class="card-label red">MORNING · CONFIRMED</div>
        <div class="card-title">🦽 Disability Appointment</div>
        <div class="card-row"><span class="card-field">Time:</span> 9:00 AM – 11:00 AM (2 hours)</div>
        <div class="card-row"><span class="card-field">Status:</span> <span class="status-confirmed">✅ Confirmed</span></div>
        <div class="card-row"><span class="card-field">Prep Needed:</span> Bring relevant documentation. Confirm address. Allow travel buffer time.</div>
        <div class="card-row"><span class="card-field">Conflict:</span> <strong>Overlaps with Executive Roundtable (9:00–10:30 AM) — but you have already DECLINED that event.</strong> No conflict issue.</div>
      </div>

      <div class="card red">
        <div class="card-label red">MORNING · DECLINED</div>
        <div class="card-title">💼 Executive Roundtable (Zoom — Declined)</div>
        <div class="card-row"><span class="card-field">Time:</span> 9:00 AM – 10:30 AM</div>
        <div class="card-row"><span class="card-field">Host:</span> John Madigan</div>
        <div class="card-row"><span class="card-field">Link:</span> <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" style="color:#2471a3;" target="_blank">Join Zoom</a> (Meeting ID: 207 786 667 · PW: 205454)</div>
        <div class="card-row"><span class="card-field">Status:</span> <span class="status-declined">❌ Declined</span> — conflicts with Disability appointment.</div>
        <div class="card-row"><span class="card-field">Prep Needed:</span> None — already declined. Consider sending a brief note to John Madigan if you have a relationship with him.</div>
      </div>

      <div class="card yellow">
        <div class="card-label yellow">⚠️ RSVP NEEDED — ZOOM</div>
        <div class="card-title">HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
        <div class="card-row"><span class="card-field">Time:</span> 12:00 PM – 1:00 PM</div>
        <div class="card-row"><span class="card-field">Link:</span> <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" style="color:#2471a3;" target="_blank">Join Zoom Meeting</a></div>
        <div class="card-row"><span class="card-field">Status:</span> <span class="status-needs">⏳ Needs Action — RSVP Required</span></div>
        <div class="card-row"><span class="card-field">Attendees:</span> 160+ HR professionals</div>
        <div class="card-row"><span class="card-field">Prep Needed:</span> This is an open discussion — turn off AI note-taking per organizer request. Great opportunity for 1:1 warm connections in your job search.</div>
        <div class="card-row"><span class="card-field">Conflict:</span> Disability appointment ends at 11:00 AM — 1 hour buffer before noon. Allow travel time home if remote attendance needed.</div>
      </div>
    </div>

    <!-- Friday Aug 7 -->
    <div style="margin-bottom:18px;">
      <div style="font-weight:800;font-size:15px;color:#2471a3;border-bottom:2px solid #d0e8f8;padding-bottom:6px;margin-bottom:10px;">📆 Friday, August 7, 2026</div>
      <div class="card yellow">
        <div class="card-label yellow">💰 BILLING REMINDER</div>
        <div class="card-title">🏠 State Farm Bill Due</div>
        <div class="card-row"><span class="card-field">Time:</span> All Day Reminder</div>
        <div class="card-row"><span class="card-field">Status:</span> <span class="status-confirmed">✅ Confirmed</span></div>
        <div class="card-row"><span class="card-field">Prep Needed:</span> Confirm State Farm payment is scheduled or manually pay before end of day. Check for auto-pay enrollment to avoid late fees.</div>
        <div class="card-row"><span class="card-field">Conflict:</span> None.</div>
      </div>
    </div>

  </div>
</div>

<!-- ══════════════════════════════════════════════════════
     SECTION 5: JOB SEARCH & INTERVIEW PIPELINE
     ══════════════════════════════════════════════════════ -->
<div class="section green">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">
    <p style="font-size:13px;color:#555;margin-bottom:14px;">Active job search activity across LinkedIn, Glassdoor, Jobright, and direct outreach. Melissa is targeting senior HR leadership roles (VP, Head of People, CHRO, HR Director level).</p>

    <table>
      <thead>
        <tr>
          <th>Fit</th>
          <th>Role / Opportunity</th>
          <th>Source / Company</th>
          <th>Date</th>
          <th>Status</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>VP of People</td>
          <td>Nitra — LinkedIn Job Alert</td>
          <td>Aug 1, 2026</td>
          <td>New Alert — Unreviewed</td>
          <td>Review JD and apply if aligned</td>
        </tr>
        <tr>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>Senior Director, People Business Partner</td>
          <td>Jobright.ai (Eric) — Direct invite to Melissa</td>
          <td>Jul 31, 2026</td>
          <td>Personalized outreach — unread</td>
          <td>Open email, review role, respond to Eric</td>
        </tr>
        <tr>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>Head of People, North America</td>
          <td>Artefact — LinkedIn Job Alert</td>
          <td>Aug 1, 2026</td>
          <td>New Alert — Unreviewed</td>
          <td>Review JD and apply if aligned</td>
        </tr>
        <tr>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>HR Director &amp; Similar Roles (NY Post area)</td>
          <td>LinkedIn — Jobs Inbox Alert</td>
          <td>Aug 1, 2026</td>
          <td>In Inbox — Unread</td>
          <td>Review all roles listed in email</td>
        </tr>
        <tr>
          <td><span class="badge badge-yellow">MEDIUM</span></td>
          <td>Head of People</td>
          <td>Adonis — LinkedIn Job Alert (3 alerts sent)</td>
          <td>Jul 29–Aug 1</td>
          <td>Duplicate alerts — role posted Jul 29</td>
          <td>Apply if not already done; mark alert duplicates as read</td>
        </tr>
        <tr>
          <td><span class="badge badge-yellow">MEDIUM</span></td>
          <td>Complex HR Director</td>
          <td>Highgate — Glassdoor (in Trash)</td>
          <td>Jul 31, 2026</td>
          <td>In Trash — manually trashed</td>
          <td>Restore if role still relevant; otherwise delete</td>
        </tr>
        <tr>
          <td><span class="badge badge-yellow">MEDIUM</span></td>
          <td>People Business Partner at Pair Team + 6 Remote Roles</td>
          <td>Glassdoor — Remote US</td>
          <td>Aug 1, 2026</td>
          <td>Unread alert</td>
          <td>Review all 7 roles in the email</td>
        </tr>
        <tr>
          <td><span class="badge badge-yellow">MEDIUM</span></td>
          <td>Community Coordinator + 4 NYC roles</td>
          <td>Glassdoor — New York, NY</td>
          <td>Aug 1, 2026</td>
          <td>Unread alert</td>
          <td>Scan for any senior matches; likely lower-level</td>
        </tr>
        <tr>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>Direct CVS Corporate Affairs Outreach (Amy &amp; Sam)</td>
          <td>Sent by Melissa — melissaw212@gmail.com</td>
          <td>Jul 31, 2026</td>
          <td>Sent — awaiting response</td>
          <td>Log in tracker; follow up Wed Aug 5 if no reply</td>
        </tr>
        <tr>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>Resume + Website sent to Michael</td>
          <td>Sent by Melissa — melissaw212@gmail.com</td>
          <td>Jul 31, 2026</td>
          <td>Sent — awaiting response</td>
          <td>Log in tracker; follow up by mid-week</td>
        </tr>
        <tr>
          <td><span class="badge badge-blue">NETWORKING</span></td>
          <td>HR Networking &amp; Job Search Group Zoom (160+ peers)</td>
          <td>Calendar — Aug 5, 12–1:30 PM</td>
          <td>Aug 5, 2026</td>
          <td>RSVP Needed</td>
          <td>Confirm attendance, prep 30-sec intro</td>
        </tr>
        <tr>
          <td><span class="badge badge-blue">NETWORKING</span></td>
          <td>HR Networking Open Office Hours Zoom</td>
          <td>Calendar — Aug 6, 12–1 PM</td>
          <td>Aug 6, 2026</td>
          <td>RSVP Needed</td>
          <td>Confirm attendance, 1:1 connection opportunity</td>
        </tr>
        <tr>
          <td><span class="badge badge-blue">NETWORKING</span></td>
          <td>LinkedIn — 1 New Connection Invitation</td>
          <td>LinkedIn notifications-noreply</td>
          <td>Aug 1, 2026</td>
          <td>Read — pending review</td>
          <td>Open LinkedIn and review invitation</td>
        </tr>
      </tbody>
    </table>

    <div style="margin-top:14px;" class="card green">
      <div class="card-label green">💡 JOB SEARCH NOTE</div>
      <div class="card-title">LinkedIn Alert Duplication — Head of People at Adonis</div>
      <p style="font-size:13px;color:#444;">This role generated 4 separate LinkedIn Job Alert emails (Jul 31–Aug 1). The role was posted Jul 29. Review once and mark remaining alerts as read. Consider adjusting LinkedIn alert frequency to avoid inbox clutter during active search.</p>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════════════════
     SECTION 6: FULL EMAIL REVIEW BY CATEGORY
     ══════════════════════════════════════════════════════ -->
<div class="section navy">
  <div class="section-title">📬 Full Email Review by Category</div>
  <div class="section-body">

    <!-- 6A: Security / Risk -->
    <div style="margin-bottom:20px;">
      <div style="font-weight:800;font-size:14px;color:#c0392b;margin-bottom:8px;padding:6px 10px;background:#fdf3f2;border-radius:6px;">🔴 SECURITY / RISK (1 email)</div>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr style="background:#fdf3f2;">
            <td><strong>Payment-Declined</strong> (spoofed sender)</td>
            <td>[melissaw212] Your Cloud Account has been locked on [Fri,31 Jul-2026]</td>
            <td><span class="badge badge-red">AUTO-TRASHED — PHISHING</span></td>
            <td>No action needed. Already removed. Do not click any links if you see it. Random domain impersonating cloud storage; classic credential-harvesting scareware.</td>
          </tr>
        </tbody>
      </table>
      <p class="note">Auto-trash reason: Spoofed 'Payment-Declined' sender from random domain, targeting user by username with urgent account-threat language (payment failed, account locked, photos/videos deleted) — credential-harvesting/scareware phishing. Removed before inbox delivery.</p>
    </div>

    <hr class="divider">

    <!-- 6B: Job Search -->
    <div style="margin-bottom:20px;">
      <div style="font-weight:800;font-size:14px;color:#1e8449;margin-bottom:8px;padding:6px 10px;background:#f0faf3;border-radius:6px;">💼 JOB SEARCH (13 emails)</div>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Read?</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>LinkedIn Job Alerts</td><td>VP of People at Nitra</td><td>Read</td><td>Review and apply if aligned — HIGH fit</td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>Head of People at Adonis (×4 duplicate alerts)</td><td>Mixed</td><td>Apply once; delete duplicates</td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>Head of People, North America at Artefact</td><td>Read</td><td>Review JD — HIGH fit</td></tr>
          <tr><td>LinkedIn (Inbox)</td><td>New jobs similar to HR Director at NY Post</td><td>Unread</td><td>Open and review — in inbox</td></tr>
          <tr><td>Glassdoor Jobs</td><td>People Business Partner at Pair Team + 6 Remote roles</td><td>Unread</td><td>Scan all 7 roles</td></tr>
          <tr><td>Glassdoor Jobs</td><td>Community Coordinator at NYC Housing Authority + 4 NYC roles</td><td>Unread</td><td>Scan for senior matches</td></tr>
          <tr><td>Eric at Jobright.com</td><td>Senior Director, People Business Partner — invited Jul 31</td><td>Read</td><td>Respond to Eric — HIGH fit personalized outreach</td></tr>
          <tr><td>melissa (self-sent)</td><td>Melissa Weiss Resume and website → Michael</td><td>Read (sent)</td><td>Track; follow up if no reply by Wed</td></tr>
          <tr><td>melissa (self-sent)</td><td>15 years, one specific fit → Amy (CVS)</td><td>Read (sent)</td><td>Track; follow up Wed Aug 5</td></tr>
          <tr><td>melissa (self-sent)</td><td>15 years, one specific fit → Sam (CVS)</td><td>Read (sent)</td><td>Track; follow up Wed Aug 5</td></tr>
        </tbody>
      </table>
    </div>

    <hr class="divider">

    <!-- 6C: Professional Networking -->
    <div style="margin-bottom:20px;">
      <div style="font-weight:800;font-size:14px;color:#7d3c98;margin-bottom:8px;padding:6px 10px;background:#f8f0fd;border-radius:6px;">🤝 PROFESSIONAL NETWORKING / LINKEDIN (2 emails)</div>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Read?</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>LinkedIn</td><td>You have 1 new invitation</td><td>Read</td><td>Open LinkedIn and review who sent the invite</td></tr>
          <tr><td>Melissa W (self)</td><td>Claude Projects / Learn AI with Mariah (self-forwarded resource)</td><td>Unread</td><td>Save for later — AI learning resource for professional development</td></tr>
        </tbody>
      </table>
    </div>

    <hr class="divider">

    <!-- 6D: Financial / Billing -->
    <div style="margin-bottom:20px;">
      <div style="font-weight:800;font-size:14px;color:#d68910;margin-bottom:8px;padding:6px 10px;background:#fefaf0;border-radius:6px;">💰 FINANCIAL / BILLING (3 emails)</div>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr style="background:#fefaf0;"><td><strong>Bank of America</strong></td><td>Billing Dispute for account – 4018 — Request for additional info</td><td><span class="badge badge-red">URGENT — INBOX</span></td><td>Log into BOA directly and provide required info for Step 2 of 3 dispute process</td></tr>
          <tr><td>Verizon</td><td>Your bill is now available online</td><td><span class="badge badge-yellow">INBOX — Review</span></td><td>Review and pay Verizon bill</td></tr>
          <tr><td>Bilt Rewards</td><td>Your rent payment is processing</td><td><span class="badge badge-green">INBOX — Monitor</span></td><td>Confirm rent payment completes; retain for records</td></tr>
        </tbody>
      </table>
    </div>

    <hr class="divider">

    <!-- 6E: Medical / Health -->
    <div style="margin-bottom:20px;">
      <div style="font-weight:800;font-size:14px;color:#c0392b;margin-bottom:8px;padding:6px 10px;background:#fdf3f2;border-radius:6px;">🏥 MEDICAL / HEALTH (1 email — calendar-related)</div>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Calendar: Eye Dr</td><td>Eye Doctor Appointment — Today 2:30 PM</td><td>Attend. Bring insurance card. Arrange transport if dilation expected.</td></tr>
        </tbody>
      </table>
      <p class="note">Note: Multiple GLP-1 spam/weight loss emails (10 total) are categorized under Spam/Promotional — not medical content.</p>
    </div>

    <hr class="divider">

    <!-- 6F: Personal -->
    <div style="margin-bottom:20px;">
      <div style="font-weight:800;font-size:14px;color:#148f77;margin-bottom:8px;padding:6px 10px;background:#f0faf8;border-radius:6px;">👤 PERSONAL (2 emails)</div>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Match.com</td><td>Henry (66, Wayne NJ) viewed your profile</td><td>Check out Henry's profile if interested — view returned or ignore</td></tr>
          <tr><td>Match.com</td><td>Eliot likes you — see if it's mutual</td><td>Review Eliot's profile if interested</td></tr>
          <tr><td>Match.com</td><td>Paul likes you — see if it's mutual</td><td>Review Paul's profile if interested</td></tr>
        </tbody>
      </table>
    </div>

    <hr class="divider">

    <!-- 6G: Newsletters / Subscriptions -->
    <div style="margin-bottom:20px;">
      <div style="font-weight:800;font-size:14px;color:#7d3c98;margin-bottom:8px;padding:6px 10px;background:#f8f0fd;border-radius:6px;">📰 NEWSLETTERS / SUBSCRIPTIONS (3 emails)</div>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Recommendation</th></tr></thead>
        <tbody>
          <tr><td>Manychat</td><td>Updates to Manychat's Privacy Policy (effective Aug 16, 2026)</td><td>Read</td><td>Review if you actively use Manychat. Note Aug 16 effective date.</td></tr>
          <tr style="background:#fff8f8;"><td>Alison Courses</td><td>Wondering how credible Alison courses are, Melissa A?</td><td><span class="badge badge-red">In Trash (manual)</span></td><td>Delete — already trashed. Consider unsubscribing if not using Alison.</td></tr>
          <tr style="background:#fff8f8;"><td>Jack Cocchiarella (Substack)</td><td>Crying Trump Forced To Quit His Plan</td><td><span class="badge badge-red">In Trash (manual)</span></td><td>Delete — already trashed. Unsubscribe from political Substack if unwanted.</td></tr>
        </tbody>
      </table>
    </div>

    <hr class="divider">

    <!-- 6H: Promotional / Retail -->
    <div style="margin-bottom:20px;">
      <div style="font-weight:800;font-size:14px;color:#717d7e;margin-bottom:8px;padding:6px 10px;background:#f7f7f7;border-radius:6px;">🛍 PROMOTIONAL / RETAIL (17 emails) — See Promotional Summary Section</div>
      <p style="font-size:13px;color:#666;padding:8px;">Includes: Old Navy (3), SHEIN (2), Kohl's (1–trashed), UNIQLO (1), Temu (1), VIVAIA (1), Laura Geller (2), MEDVi GLP-1 spam (10 total across multiple senders). All detailed in Promotional/Retail Summary below.</p>
    </div>

    <hr class="divider">

    <!-- 6I: Political -->
    <div style="margin-bottom:20px;">
      <div style="font-weight:800;font-size:14px;color:#717d7e;margin-bottom:8px;padding:6px 10px;background:#f7f7f7;border-radius:6px;">🏛 POLITICAL / FUNDRAISING (1 email)</div>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>DJT (donaldjtrump.com)</td><td>"Goodnight." — fundraising/engagement email</td><td>Ignore or unsubscribe. Low priority.</td></tr>
        </tbody>
      </table>
    </div>

  </div>
</div>

<!-- ══════════════════════════════════════════════════════
     SECTION 7: TRASH REVIEW
     ══════════════════════════════════════════════════════ -->
<div class="section red">
  <div class="section-title">🗑️ Trash Review</div>
  <div class="section-body">

    <div style="margin-bottom:16px;">
      <div style="font-weight:800;color:#c0392b;margin-bottom:8px;font-size:14px;">🚨 AUTO-TRASHED — PHISHING (1 email)</div>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Reason</th><th>Action</th></tr></thead>
        <tbody>
          <tr style="background:#fdf3f2;">
            <td>Payment-Declined &lt;yawzjehisgl@wklf.avtvlskjxatsi.us&gt;</td>
            <td>[melissaw212] Your Cloud Account has been locked on [Fri,31 Jul-2026]. Your photos and videos will be removed!</td>
            <td>Spoofed sender on random domain; impersonating cloud storage service; targeted by username; urgent threat language; classic phishing/scareware to harvest credentials.</td>
            <td><span class="badge badge-red">No Action — Auto-Removed</span></td>
          </tr>
        </tbody>
      </table>
    </div>

    <hr class="divider">

    <div style="margin-bottom:16px;">
      <div style="font-weight:800;color:#d68910;margin-bottom:8px;font-size:14px;">🔄 RESTORE IMMEDIATELY (1 email)</div>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Why Restore</th></tr></thead>
        <tbody>
          <tr style="background:#fefaf0;">
            <td>Glassdoor Jobs</td>
            <td>Complex HR Director at Highgate and 6 more jobs in New York, NY — Apply Now</td>
            <td>Relevant job leads for active job search. May have been manually trashed by mistake. HR Director at Highgate (NYC) warrants review before discarding.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <hr class="divider">

    <div style="margin-bottom:16px;">
      <div style="font-weight:800;color:#d68910;margin-bottom:8px;font-size:14px;">👀 REVIEW BEFORE DELETING (1 email)</div>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Notes</th></tr></thead>
        <tbody>
          <tr>
            <td>Alison Courses</td>
            <td>Wondering how credible Alison courses are, Melissa A?</td>
            <td>If you enrolled in Alison for professional development, this may be relevant. If not, delete and unsubscribe.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <hr class="divider">

    <div>
      <div style="font-weight:800;color:#717d7e;margin-bottom:8px;font-size:14px;">✅ SAFE TO DELETE (2 emails)</div>
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Reason</th></tr></thead>
        <tbody>
          <tr><td>Kohl's Friends &amp; Family</td><td>Extra 20% off | Discover the denim you deserve</td><td>Standard retail promo — already trashed. Safe to permanently delete.</td></tr>
          <tr><td>Jack Cocchiarella (Substack)</td><td>Crying Trump Forced To Quit His Plan</td><td>Political Substack — already trashed. Permanently delete and unsubscribe.</td></tr>
        </tbody>
      </table>
    </div>

  </div>
</div>

<!-- ══════════════════════════════════════════════════════
     SECTION 8: PROMOTIONAL / RETAIL SUMMARY
     ══════════════════════════════════════════════════════ -->
<div class="section gray">
  <div class="section-title">🛍️ Promotional / Retail Summary</div>
  <div class="section-body">
    <table>
      <thead>
        <tr>
          <th>Brand / Sender</th>
          <th>Count</th>
          <th>Subject / Theme</th>
          <th>Recommendation</th>
        </tr>
      </thead>
      <tbody>
        <tr style="background:#fdf3f2;">
          <td><strong>MEDVi GLP-1 / GLP-1 Spam</strong><br><span style="font-size:11px;color:#888;">Multiple spoofed senders, random domains</span></td>
          <td><strong>10</strong></td>
          <td>Weight loss medication spam — GLP-1 "celebrity secret," 100K+ users, transformation, $179 price point. Multiple variations from MEDVi_Health, MEDVi GLP-1, GLP-1-by-DirectMeds, MEDVi-Patient_Success</td>
          <td><span class="badge badge-red">DELETE + REPORT SPAM</span> — These are mass spam campaigns from randomized domains, not legitimate medical providers. Do not click links.</td>
        </tr>
        <tr>
          <td><strong>Old Navy</strong></td>
          <td><strong>3</strong></td>
          <td>Order Confirmation #1RDGPJ0 (inbox) · Abandoned cart reminder (inbox) · Half-Off-Everything sale ends tonight</td>
          <td><span class="badge badge-green">KEEP</span> Order confirmation — retain for tracking. Cart reminder — you already ordered, ignore. Sale
