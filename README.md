<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Melissa's Executive Briefing — Sunday, July 12, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; line-height: 1.5; }
  .container { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* Header */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 16px; color: #a0b4cc; margin-top: 6px; }
  .header-meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header-meta .meta-item { background: rgba(255,255,255,0.1); border-radius: 8px; padding: 10px 18px; text-align: center; }
  .header-meta .meta-item .num { font-size: 22px; font-weight: 700; color: #7ecfff; }
  .header-meta .meta-item .label { font-size: 11px; color: #a0b4cc; text-transform: uppercase; letter-spacing: 0.5px; }

  /* Section headers */
  .section-header { font-size: 17px; font-weight: 700; padding: 10px 16px; border-radius: 8px 8px 0 0; margin-bottom: 0; letter-spacing: 0.3px; }
  .section-wrap { border-radius: 10px; overflow: hidden; margin-bottom: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
  .section-body { background: #fff; padding: 18px 20px; border-radius: 0 0 10px 10px; }

  /* Color themes */
  .red-header { background: #c0392b; color: #fff; }
  .red-body { border-left: 4px solid #c0392b; }
  .yellow-header { background: #e67e22; color: #fff; }
  .yellow-body { border-left: 4px solid #e67e22; }
  .blue-header { background: #2980b9; color: #fff; }
  .blue-body { border-left: 4px solid #2980b9; }
  .green-header { background: #27ae60; color: #fff; }
  .green-body { border-left: 4px solid #27ae60; }
  .purple-header { background: #8e44ad; color: #fff; }
  .purple-body { border-left: 4px solid #8e44ad; }
  .gray-header { background: #7f8c8d; color: #fff; }
  .gray-body { border-left: 4px solid #7f8c8d; }
  .dark-header { background: #2c3e50; color: #fff; }

  /* Cards */
  .card { border-radius: 8px; padding: 14px 16px; margin-bottom: 12px; border: 1px solid #e0e0e0; background: #fff; }
  .card.red { border-left: 5px solid #c0392b; background: #fff8f8; }
  .card.yellow { border-left: 5px solid #e67e22; background: #fffaf3; }
  .card.blue { border-left: 5px solid #2980b9; background: #f4f9ff; }
  .card.green { border-left: 5px solid #27ae60; background: #f4fff8; }
  .card.purple { border-left: 5px solid #8e44ad; background: #fdf6ff; }
  .card.gray { border-left: 5px solid #95a5a6; background: #f9f9f9; }

  .card-title { font-weight: 700; font-size: 14px; margin-bottom: 4px; }
  .card-meta { font-size: 12px; color: #666; margin-bottom: 6px; }
  .card-row { display: flex; gap: 8px; align-items: flex-start; margin-bottom: 3px; font-size: 13px; }
  .card-row .lbl { font-weight: 600; min-width: 110px; color: #444; }
  .card-row .val { color: #222; }

  /* Badges */
  .badge { display: inline-block; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 20px; text-transform: uppercase; letter-spacing: 0.5px; margin-right: 4px; }
  .badge-red { background: #fde8e8; color: #c0392b; border: 1px solid #c0392b; }
  .badge-yellow { background: #fef6e4; color: #e67e22; border: 1px solid #e67e22; }
  .badge-green { background: #e8f8ee; color: #27ae60; border: 1px solid #27ae60; }
  .badge-blue { background: #e8f3ff; color: #2980b9; border: 1px solid #2980b9; }
  .badge-purple { background: #f5e8ff; color: #8e44ad; border: 1px solid #8e44ad; }
  .badge-gray { background: #f0f0f0; color: #555; border: 1px solid #aaa; }
  .badge-phish { background: #1a0000; color: #ff6b6b; border: 1px solid #ff6b6b; }

  /* Tables */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #f0f2f5; font-weight: 700; padding: 8px 10px; text-align: left; border-bottom: 2px solid #ddd; }
  td { padding: 8px 10px; border-bottom: 1px solid #eee; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f9f9f9; }

  /* Priority colors in tables */
  .p-high { color: #c0392b; font-weight: 700; }
  .p-med { color: #e67e22; font-weight: 700; }
  .p-low { color: #27ae60; font-weight: 700; }

  /* Calendar day block */
  .cal-day { margin-bottom: 16px; }
  .cal-day-header { background: #2c3e50; color: #fff; padding: 7px 14px; border-radius: 6px; font-weight: 700; font-size: 13px; margin-bottom: 6px; }
  .cal-day-header.today { background: #2980b9; }
  .cal-event { background: #f4f9ff; border-left: 4px solid #2980b9; border-radius: 5px; padding: 10px 14px; margin-bottom: 6px; }
  .cal-event.declined { border-left-color: #95a5a6; background: #f9f9f9; opacity: 0.8; }
  .cal-event.needs-action { border-left-color: #e67e22; background: #fffaf3; }
  .cal-event.conflict { border-left-color: #c0392b; background: #fff8f8; }
  .cal-event-title { font-weight: 700; font-size: 14px; }
  .cal-event-detail { font-size: 12px; color: #555; margin-top: 2px; }

  /* Dashboard grid */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; }
  .dash-card { border-radius: 10px; padding: 16px; text-align: center; }
  .dash-card .num { font-size: 30px; font-weight: 800; }
  .dash-card .lbl { font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px; }
  .dash-red { background: #fde8e8; color: #c0392b; }
  .dash-yellow { background: #fef6e4; color: #e67e22; }
  .dash-green { background: #e8f8ee; color: #27ae60; }
  .dash-blue { background: #e8f3ff; color: #2980b9; }
  .dash-purple { background: #f5e8ff; color: #8e44ad; }
  .dash-gray { background: #f0f0f0; color: #555; }

  /* Top 3 */
  .top3 { counter-reset: top3; }
  .top3-item { display: flex; gap: 14px; align-items: flex-start; margin-bottom: 14px; }
  .top3-num { background: #1a1a2e; color: #7ecfff; font-size: 22px; font-weight: 900; min-width: 44px; height: 44px; display: flex; align-items: center; justify-content: center; border-radius: 50%; flex-shrink: 0; }
  .top3-text { font-size: 14px; }
  .top3-text strong { display: block; font-size: 15px; margin-bottom: 2px; }

  /* Exec summary bullets */
  .exec-bullet { display: flex; gap: 12px; align-items: flex-start; padding: 10px 0; border-bottom: 1px solid #eee; }
  .exec-bullet:last-child { border-bottom: none; }
  .exec-icon { font-size: 20px; min-width: 30px; }

  /* Inline pill */
  .pill { display: inline-block; font-size: 11px; padding: 1px 8px; border-radius: 12px; font-weight: 600; margin-left: 6px; }
  .pill-red { background: #fde8e8; color: #c0392b; }
  .pill-green { background: #e8f8ee; color: #27ae60; }
  .pill-yellow { background: #fef6e4; color: #e67e22; }
  .pill-blue { background: #e8f3ff; color: #2980b9; }
  .pill-gray { background: #f0f0f0; color: #555; }

  .divider { height: 1px; background: #e0e0e0; margin: 12px 0; }
  .note { font-size: 12px; color: #888; font-style: italic; margin-top: 6px; }
  .count-badge { display: inline-block; background: #e0e0e0; color: #333; font-weight: 700; font-size: 11px; padding: 1px 7px; border-radius: 12px; margin-left: 6px; }

  .warn { background: #fff3cd; border-left: 4px solid #e67e22; border-radius: 5px; padding: 8px 12px; font-size: 12px; margin-top: 8px; }
  .phish-row { background: #1a0000; color: #ff9999; border-radius: 5px; padding: 8px 12px; margin-bottom: 6px; font-size: 12px; }
  .phish-row strong { color: #ffcccc; }

  @media (max-width: 700px) {
    .header { padding: 20px 16px; }
    .header h1 { font-size: 20px; }
    .header-meta { gap: 12px; }
    .dashboard-grid { grid-template-columns: repeat(2, 1fr); }
  }
</style>
</head>
<body>
<div class="container">

<!-- ═══════════════════════════════════════════════════════════════
     1. HEADER
═══════════════════════════════════════════════════════════════ -->
<div class="header">
  <div class="header h1" style="font-size:13px;color:#a0b4cc;text-transform:uppercase;letter-spacing:1px;margin-bottom:4px;">Executive Briefing</div>
  <h1>Good Morning, Melissa 👋</h1>
  <div class="subtitle">Sunday, July 12, 2026 &nbsp;|&nbsp; Prepared by your Executive Chief of Staff</div>
  <div class="header-meta">
    <div class="meta-item"><div class="num">50</div><div class="label">Emails Reviewed</div></div>
    <div class="meta-item"><div class="num">11</div><div class="label">Calendar Events</div></div>
    <div class="meta-item"><div class="num">10</div><div class="label">Auto-Trashed Phishing</div></div>
    <div class="meta-item"><div class="num">3</div><div class="label">RSVPs Needed</div></div>
    <div class="meta-item"><div class="num">5</div><div class="label">Job Leads Active</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     2. EXECUTIVE SUMMARY
═══════════════════════════════════════════════════════════════ -->
<div class="section-wrap">
  <div class="section-header dark-header">⚡ Executive Summary — Top 3 Things That Matter Today</div>
  <div class="section-body">
    <div class="exec-bullet">
      <div class="exec-icon">🚨</div>
      <div><strong>BIGGEST RISK:</strong> Your inbox received a wave of 10 high-confidence phishing emails (all auto-trashed) spoofing cloud storage payment threats, fake prize scams, and spam. No action needed on those — but be aware your email address is actively being targeted. Additionally, one GLP-1 spam and one adult-spam email remain in limbo (not trashed, not inbox) — flag for manual permanent delete.</div>
    </div>
    <div class="exec-bullet">
      <div class="exec-icon">💼</div>
      <div><strong>BIGGEST JOB OPPORTUNITY:</strong> Indeed flagged a <strong>Chief People Officer at Pearl Health ($270K–$310K)</strong> as a strong match for your HR leadership background. LinkedIn also surfaced a <strong>Senior Director, People Business Partner at GitLab</strong> and a <strong>Chief People Officer at Sunday</strong>. These are high-fit, high-urgency — review and apply today before the week fills up.</div>
    </div>
    <div class="exec-bullet">
      <div class="exec-icon">📅</div>
      <div><strong>BIGGEST CALENDAR ITEM:</strong> You have a <strong>time conflict on Wednesday, July 15</strong>: your Bone Density / LH Radiology imaging appointment (8:30 AM) overlaps directly with your HR Networking & Job Search Group Zoom (12:00 PM — no real conflict there, but two calendar entries exist for same slot). More urgently, you have <strong>two RSVPs pending</strong> (HR Networking Zoom on 7/15 and Open Office Hours on 7/16) — respond today.</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     3. ACTION REQUIRED
═══════════════════════════════════════════════════════════════ -->
<div class="section-wrap">
  <div class="section-header yellow-header">⚠️ Action Required — Items Melissa Must Act On</div>
  <div class="section-body">

    <div class="card yellow">
      <div class="card-title"><span class="badge badge-yellow">RSVP</span> HR Networking & Job Search Group — Zoom #2</div>
      <div class="card-meta">Source: Google Calendar invite — Wed Jul 15, 12:00–1:30 PM</div>
      <div class="card-row"><span class="lbl">Why it matters:</span><span class="val">Status is "needsAction" — organizer and 170+ attendees are active; your RSVP is expected.</span></div>
      <div class="card-row"><span class="lbl">Next step:</span><span class="val">Accept or decline the calendar invite now. Zoom link: us06web.zoom.us/j/81954171722</span></div>
      <div class="card-row"><span class="lbl">Due:</span><span class="val">Today, Sunday July 12</span></div>
    </div>

    <div class="card yellow">
      <div class="card-title"><span class="badge badge-yellow">RSVP</span> HR Networking & Job Search: Open Office Hours — Zoom #2</div>
      <div class="card-meta">Source: Google Calendar invite — Thu Jul 16, 12:00–1:00 PM</div>
      <div class="card-row"><span class="lbl">Why it matters:</span><span class="val">Status is "needsAction" — same large group; professional visibility at stake.</span></div>
      <div class="card-row"><span class="lbl">Next step:</span><span class="val">Accept or decline. Zoom link: us06web.zoom.us/j/85945371140</span></div>
      <div class="card-row"><span class="lbl">Due:</span><span class="val">Today, Sunday July 12</span></div>
    </div>

    <div class="card green">
      <div class="card-title"><span class="badge badge-green">JOB LEAD</span> Chief People Officer @ Pearl Health — $270K–$310K</div>
      <div class="card-meta">Source: Indeed — donotreply@match.indeed.com — Sun Jul 12, 8:31 AM</div>
      <div class="card-row"><span class="lbl">Why it matters:</span><span class="val">Salary range is top-tier for your level. Indeed flagged it as a strong match for your HR leadership background. Posted recently — high urgency before applications surge.</span></div>
      <div class="card-row"><span class="lbl">Next step:</span><span class="val">Review full JD today. Tailor resume/cover letter. Apply this week.</span></div>
      <div class="card-row"><span class="lbl">Due:</span><span class="val">Apply by Monday/Tuesday Jul 13–14</span></div>
    </div>

    <div class="card green">
      <div class="card-title"><span class="badge badge-green">JOB LEAD</span> Senior Director, People Business Partner @ GitLab</div>
      <div class="card-meta">Source: LinkedIn Job Alerts — Sun Jul 12, 7:05 AM (posted 7/9/2026)</div>
      <div class="card-row"><span class="lbl">Why it matters:</span><span class="val">GitLab is a high-profile remote-first company. Sr. Director HRBP aligns with your strategic HR background. Posted 3 days ago — competitive window is closing.</span></div>
      <div class="card-row"><span class="lbl">Next step:</span><span class="val">Review role. Apply via LinkedIn today.</span></div>
      <div class="card-row"><span class="lbl">Due:</span><span class="val">Apply by Monday Jul 13</span></div>
    </div>

    <div class="card green">
      <div class="card-title"><span class="badge badge-green">JOB LEAD</span> VP of Human Resources @ Tiberius Aerospace (Similar Roles)</div>
      <div class="card-meta">Source: LinkedIn — jobs-noreply@linkedin.com — Sun Jul 12, 9:05 AM</div>
      <div class="card-row"><span class="lbl">Why it matters:</span><span class="val">LinkedIn surfaced similar VP HR roles based on your Tiberius Aerospace interest. Review the new listings before they expire.</span></div>
      <div class="card-row"><span class="lbl">Next step:</span><span class="val">Open LinkedIn and review "similar jobs" list. Save or apply to best fits.</span></div>
      <div class="card-row"><span class="lbl">Due:</span><span class="val">This week</span></div>
    </div>

    <div class="card green">
      <div class="card-title"><span class="badge badge-green">JOB LEAD</span> Chief People Officer @ Sunday (Duplicate Alert)</div>
      <div class="card-meta">Source: LinkedIn Job Alerts — 2 identical alerts sent (3:05 AM and 5:05 AM) — Sun Jul 12</div>
      <div class="card-row"><span class="lbl">Why it matters:</span><span class="val">Duplicate alerts — role posted 7/10/2026. Review once; do not apply twice.</span></div>
      <div class="card-row"><span class="lbl">Next step:</span><span class="val">Review CPO @ Sunday role on LinkedIn. Apply if it's a fit.</span></div>
      <div class="card-row"><span class="lbl">Due:</span><span class="val">This week</span></div>
    </div>

    <div class="card yellow">
      <div class="card-title"><span class="badge badge-yellow">BILLING</span> CareCredit / Synchrony Bank — $250.00 Payment Posted</div>
      <div class="card-meta">Source: Synchrony Bank — customer.service@mail.synchronybank.com — Sun Jul 12, 8:00 AM</div>
      <div class="card-row"><span class="lbl">Why it matters:</span><span class="val">Payment of $250.00 on account ending 7483 was confirmed. Verify amount is correct and check for any remaining balance.</span></div>
      <div class="card-row"><span class="lbl">Next step:</span><span class="val">Log into CareCredit account to verify payment applied correctly and check remaining balance.</span></div>
      <div class="card-row"><span class="lbl">Due:</span><span class="val">This week</span></div>
    </div>

    <div class="card yellow">
      <div class="card-title"><span class="badge badge-yellow">LOGISTICS</span> USPS — 1 Inbound Package Arriving Soon</div>
      <div class="card-meta">Source: USPS Informed Delivery — Sun Jul 12, 11:24 AM</div>
      <div class="card-row"><span class="lbl">Why it matters:</span><span class="val">1 package inbound — track it to confirm delivery window given your medical appointments this week.</span></div>
      <div class="card-row"><span class="lbl">Next step:</span><span class="val">Check USPS Informed Delivery for tracking details. Plan to be available or arrange pickup.</span></div>
      <div class="card-row"><span class="lbl">Due:</span><span class="val">This week</span></div>
    </div>

    <div class="card yellow">
      <div class="card-title"><span class="badge badge-yellow">SOCIAL</span> Tea with LeiLani | Brew at the Table — Confirmed</div>
      <div class="card-meta">Source: Google Calendar — Thu Jul 16, 1:00–2:00 PM | T Shop, 247 Elizabeth St, NYC</div>
      <div class="card-row"><span class="lbl">Why it matters:</span><span class="val">You've accepted this in-person networking tea. It falls immediately after Open Office Hours Zoom (12–1 PM) on the same day — tight but manageable.</span></div>
      <div class="card-row"><span class="lbl">Next step:</span><span class="val">Confirm location logistics. Allow travel time from wherever you'll be at 1 PM. Prepare light talking points with LeiLani's group.</span></div>
      <div class="card-row"><span class="lbl">Due:</span><span class="val">Thursday Jul 16</span></div>
    </div>

    <div class="card red">
      <div class="card-title"><span class="badge badge-red">SPAM/RISK</span> Untrashed Spam Emails Still in Limbo — Manual Delete Needed</div>
      <div class="card-meta">Source: Multiple spam senders — not in inbox, not in trash, not auto-trashed</div>
      <div class="card-row"><span class="lbl">Why it matters:</span><span class="val">Several spam/scam emails were NOT auto-trashed and are sitting outside your inbox in an ambiguous state. These should be permanently deleted and senders blocked.</span></div>
      <div class="card-row"><span class="lbl">Senders:</span><span class="val">GLP-1-by-DirectMe (garbage domain), "Sex.Trick🍆" x2, "Dr. Arthur Green" (penis enlargement), Knock Every Door (political), Ashwin/MobiusEngineHub</span></div>
      <div class="card-row"><span class="lbl">Next step:</span><span class="val">Manually delete and block all. Report phishing/spam senders to Gmail.</span></div>
      <div class="card-row"><span class="lbl">Due:</span><span class="val">Today</span></div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     4. FULL 7-DAY CALENDAR
═══════════════════════════════════════════════════════════════ -->
<div class="section-wrap">
  <div class="section-header blue-header">📅 Full 7-Day Calendar — July 12–18, 2026</div>
  <div class="section-body">

    <!-- Sunday Jul 12 -->
    <div class="cal-day">
      <div class="cal-day-header today">☀️ Sunday, July 12, 2026 — TODAY</div>
      <div class="cal-event">
        <div class="cal-event-title">No scheduled events today.</div>
        <div class="cal-event-detail">Use today to RSVP for Wednesday/Thursday events, review job leads, and prepare for the medical-heavy week ahead.</div>
      </div>
    </div>

    <!-- Monday Jul 13 -->
    <div class="cal-day">
      <div class="cal-day-header">Monday, July 13, 2026</div>
      <div class="cal-event">
        <div class="cal-event-title">🏥 Stephanie — Infusion (All Day)</div>
        <div class="cal-event-detail">
          <span class="pill pill-blue">All Day</span>
          <span class="badge badge-green">CONFIRMED</span><br>
          Status: Confirmed &nbsp;|&nbsp; Location: Not specified<br>
          <strong>Prep:</strong> This appears to be a medical infusion appointment for Stephanie (possibly a family member). Confirm timing/location if you need to accompany. Block availability as needed.
        </div>
      </div>
    </div>

    <!-- Tuesday Jul 14 -->
    <div class="cal-day">
      <div class="cal-day-header">Tuesday, July 14, 2026</div>
      <div class="cal-event">
        <div class="cal-event-title">🐾 Stella — 10:00–11:00 AM</div>
        <div class="cal-event-detail">
          <span class="badge badge-green">CONFIRMED</span><br>
          Status: Confirmed &nbsp;|&nbsp; Location: Not specified (likely vet or dog groomer)<br>
          <strong>Prep:</strong> Confirm appointment location. Allow travel time. No conflicts noted.
        </div>
      </div>
    </div>

    <!-- Wednesday Jul 15 -->
    <div class="cal-day">
      <div class="cal-day-header">Wednesday, July 15, 2026 ⚠️ CONFLICT ALERT</div>

      <div class="cal-event conflict">
        <div class="cal-event-title">🦴 Bone Density Scan — 8:30–9:30 AM</div>
        <div class="cal-event-detail">
          <span class="badge badge-green">CONFIRMED</span>
          <span class="badge badge-red">SAME TIME AS IMAGING</span><br>
          Location: Not specified separately (see Imaging below)<br>
          <div class="warn">⚠️ CONFLICT: Both "Bone Density" (8:30–9:30 AM) and "IMAGING APPOINTMENT: LHRadiology" (8:30–9:05 AM) are at the same time. These appear to be the <strong>same appointment</strong> entered twice. Confirm with your calendar — no action needed if duplicate. If separate, you cannot attend both simultaneously.</div>
        </div>
      </div>

      <div class="cal-event conflict">
        <div class="cal-event-title">🏥 IMAGING APPOINTMENT: LH Radiology — 8:30–9:05 AM</div>
        <div class="cal-event-detail">
          <span class="badge badge-green">CONFIRMED</span><br>
          Location: 400 East 66th Street, NYC<br>
          Check-in: 8:30 AM Wednesday, July 15, 2026<br>
          <strong>Exam:</strong> Details in description. Complete pre-registration forms before arrival.<br>
          <strong>Prep:</strong> Review pre-registration requirements. Arrive 10–15 min early. Check what exam is scheduled (details were cut off in data).
        </div>
      </div>

      <div class="cal-event needs-action">
        <div class="cal-event-title">💼 HR Networking & Job Search Group — Zoom #2 — 12:00–1:30 PM</div>
        <div class="cal-event-detail">
          <span class="badge badge-yellow">RSVP NEEDED</span><br>
          Location: <a href="https://us06web.zoom.us/j/81954171722" style="color:#2980b9;">Zoom Link</a> &nbsp;|&nbsp; 170+ attendees<br>
          <strong>Prep:</strong> RSVP today. Review team guidelines linked in invite description. Prepare a 30-second professional update if speaking. This event ends at 1:30 PM — comfortable buffer after radiology.
        </div>
      </div>

      <div class="cal-event">
        <div class="cal-event-title">🤝 Network — 12:00–1:30 PM</div>
        <div class="cal-event-detail">
          <span class="badge badge-green">CONFIRMED</span><br>
          Note: This appears to be a personal reminder/duplicate of the HR Networking Zoom above. Same time slot. Verify if this is a separate engagement or a duplicate entry.
        </div>
      </div>
    </div>

    <!-- Thursday Jul 16 -->
    <div class="cal-day">
      <div class="cal-day-header">Thursday, July 16, 2026</div>

      <div class="cal-event declined">
        <div class="cal-event-title">🚫 Executive Roundtable — 9:00–10:30 AM (DECLINED)</div>
        <div class="cal-event-detail">
          <span class="badge badge-gray">DECLINED</span><br>
          Host: John Madigan &nbsp;|&nbsp; Location: <a href="https://us02web.zoom.us/j/207786667" style="color:#2980b9;">Zoom Link</a><br>
          Meeting ID: 207 786 667 | Password: 205454<br>
          <strong>Note:</strong> You declined this event. No action needed unless you wish to reinstate.
        </div>
      </div>

      <div class="cal-event needs-action">
        <div class="cal-event-title">💼 HR Networking & Job Search: Open Office Hours — Zoom #2 — 12:00–1:00 PM</div>
        <div class="cal-event-detail">
          <span class="badge badge-yellow">RSVP NEEDED</span><br>
          Location: <a href="https://us06web.zoom.us/j/85945371140" style="color:#2980b9;">Zoom Link</a> &nbsp;|&nbsp; 170+ attendees<br>
          <strong>Note:</strong> Organizer requests NO automated AI notetakers. Open discussion format.<br>
          <strong>Prep:</strong> RSVP today. Ends at 1:00 PM — allows travel time to Tea below.
        </div>
      </div>

      <div class="cal-event">
        <div class="cal-event-title">🍵 Tea with LeiLani | Brew At the Table — 1:00–2:00 PM</div>
        <div class="cal-event-detail">
          <span class="badge badge-green">ACCEPTED</span><br>
          Location: T Shop, 247 Elizabeth St, New York, NY 10012<br>
          Attendees: leilani@bethechangehr.com, tlow@teresalowconsulting.com, leylasnovini@gmail.com, jessi@alvisolutions.com<br>
          <strong>Prep:</strong> Zoom ends at 1 PM — plan travel to Elizabeth St (Lower Manhattan). Prepare brief personal pitch. Research LeiLani and other attendees beforehand.
          <div class="warn">⚠️ Tight timing: Zoom #2 ends at 1:00 PM, Tea starts at 1:00 PM. If Zoom runs long, you may be slightly late. Plan accordingly.</div>
        </div>
      </div>
    </div>

    <!-- Friday Jul 17 -->
    <div class="cal-day">
      <div class="cal-day-header">Friday, July 17, 2026</div>

      <div class="cal-event">
        <div class="cal-event-title">🩺 Quest Diagnostics Appointment — 10:10–10:25 AM</div>
        <div class="cal-event-detail">
          <span class="badge badge-green">CONFIRMED</span><br>
          Location: 65 E 76th St, Professional Apt GR-G, New York, NY 10021<br>
          Confirmation #: FOUGZX &nbsp;|&nbsp; Activity: All Other Tests<br>
          <strong>Prep:</strong> Short appointment (15 min). Fast if required for bloodwork. Bring confirmation number FOUGZX. Allow travel time to Upper East Side.
        </div>
      </div>

      <div class="cal-event">
        <div class="cal-event-title">👩‍⚕️ Dr. Yuen — 3:00–4:00 PM</div>
        <div class="cal-event-detail">
          <span class="badge badge-green">CONFIRMED</span><br>
          Location: Not specified<br>
          <strong>Prep:</strong> Confirm location/address. Bring any recent test results (Quest results from this morning may be relevant depending on turnaround time). Prepare list of questions.
        </div>
      </div>
    </div>

    <!-- Saturday Jul 18 -->
    <div class="cal-day">
      <div class="cal-day-header">Saturday, July 18, 2026</div>
      <div class="cal-event">
        <div class="cal-event-title">No scheduled events.</div>
        <div class="cal-event-detail">Rest and recovery after a medical-heavy week. Good day to follow up on job applications submitted earlier in the week.</div>
      </div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     5. JOB SEARCH & INTERVIEW PIPELINE
═══════════════════════════════════════════════════════════════ -->
<div class="section-wrap">
  <div class="section-header green-header">💼 Job Search & Interview Pipeline</div>
  <div class="section-body">
    <table>
      <thead>
        <tr>
          <th>Fit</th>
          <th>Role / Company</th>
          <th>Source</th>
          <th>Salary</th>
          <th>Date Surfaced</th>
          <th>Status / Next Step</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="p-high">HIGH</span></td>
          <td><strong>Chief People Officer</strong><br>Pearl Health</td>
          <td>Indeed</td>
          <td>$270K–$310K</td>
          <td>Jul 12, 2026</td>
          <td>⭐ Review JD &amp; apply this week. Strong match per Indeed algorithm.</td>
        </tr>
        <tr>
          <td><span class="p-high">HIGH</span></td>
          <td><strong>Senior Director, People Business Partner</strong><br>GitLab</td>
          <td>LinkedIn Alerts</td>
          <td>Not listed</td>
          <td>Jul 9, 2026</td>
          <td>⭐ Apply ASAP — posted 3 days ago. Remote-first culture.</td>
        </tr>
        <tr>
          <td><span class="p-med">MED</span></td>
          <td><strong>Chief People Officer</strong><br>Sunday</td>
          <td>LinkedIn Alerts (x2)</td>
          <td>Not listed</td>
          <td>Jul 10, 2026</td>
          <td>Review role; research company. Duplicate alerts — apply once.</td>
        </tr>
        <tr>
          <td><span class="p-med">MED</span></td>
          <td><strong>VP Human Resources (Similar Roles)</strong><br>Tiberius Aerospace &amp; others</td>
          <td>LinkedIn Job Alerts</td>
          <td>Not listed</td>
          <td>Jul 12, 2026</td>
          <td>Open LinkedIn to review full list of similar roles. Save best fits.</td>
        </tr>
        <tr>
          <td><span class="p-low">LOW</span></td>
          <td><strong>HR Leader — 160over90 Application</strong><br>(Sent by Melissa)</td>
          <td>Gmail Sent/Trash</td>
          <td>N/A</td>
          <td>Jul 12, 2026</td>
          <td>Application sent to Brianne at 160over90. Email found in trash — confirm it was intentionally discarded or follow up if still interested.</td>
        </tr>
        <tr style="background:#f0f2f5;">
          <td colspan="6"><strong>Networking Events This Week:</strong>
            <ul style="margin:6px 0 0 18px;">
              <li><strong>Jul 15:</strong> HR Networking &amp; Job Search Group Zoom #2 — RSVP NEEDED</li>
              <li><strong>Jul 16:</strong> HR Networking Open Office Hours Zoom #2 — RSVP NEEDED</li>
              <li><strong>Jul 16:</strong> Tea with LeiLani @ T Shop NYC — ACCEPTED ✅</li>
            </ul>
          </td>
        </tr>
      </tbody>
    </table>
    <div class="divider"></div>
    <div class="card purple" style="margin-bottom:0;">
      <div class="card-title">📰 Professional Insight: Adam Karpiak — "AI Ruined Resume Writing" (LinkedIn Newsletter)</div>
      <div class="card-meta">Source: LinkedIn Newsletter — Sun Jul 12, 11:00 AM</div>
      Relevant to your job search. AI-generated resumes are flooding applicant pools — differentiate yours with specific metrics, storytelling, and authenticity. Worth a read before submitting applications this week.
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     6. FULL EMAIL REVIEW BY CATEGORY
═══════════════════════════════════════════════════════════════ -->
<div class="section-wrap">
  <div class="section-header red-header">🔒 Security / Risk <span class="count-badge">14 emails</span></div>
  <div class="section-body">
    <p style="margin-bottom:12px;font-size:13px;"><strong>Summary:</strong> 10 emails were auto-trashed as high-confidence phishing before review. 4 additional spam/scam emails remain in limbo (not inbox, not trashed). All phishing attempts used spoofed display names with random garbage domains. Do not click any links. No action needed on auto-trashed items beyond awareness.</p>

    <div class="phish-row"><strong>🤖 AUTO-TRASHED — Phishing:</strong> "Cloud.Storage" (5 separate emails) — Spoofed cloud storage payment threats targeting melissaw212. All sent from garbage .us domains. <em>Reason: Credential/payment harvesting.</em></div>
    <div class="phish-row"><strong>🤖 AUTO-TRASHED — Phishing:</strong> "Cloud.Security" (3 separate emails) — Identical pattern to Cloud.Storage scams. Fake "FINAL NOTICE" photo deletion threats. <em>Reason: Credential/payment harvesting.</em></div>
    <div class="phish-row"><strong>🤖 AUTO-TRASHED — Phishing:</strong> "Payment-Declined" / "𝙿aym𝚎nt_Declin𝚎d" (2 separate emails, one with Unicode obfuscation) — Fake cloud account locks targeting melissaw212 by Gmail handle. <em>Reason: Payment harvesting.</em></div>
    <div class="phish-row"><strong>🤖 AUTO-TRASHED — Phishing:</strong> Fake "Lowe's" prize winner scam — Spoofed Lowe's domain, fake Kobalt Tool Set prize, targets by username. <em>Reason: Classic phishing lure.</em></div>

    <div class="divider"></div>
    <p style="font-size:13px;font-weight:700;margin-bottom:8px;">⚠️ NOT Auto-Trashed — Require Manual Action:</p>

    <div class="card red">
      <div class="card-title"><span class="badge badge-red">SPAM — DELETE</span> "GLP-1-by-DirectMe" — Weight Loss Prescription Spam</div>
      <div class="card-meta">From: dfapgqehbbo@fgdr.ncneveaswrhtd.us — Sat Jul 11, 5:45 AM | Not in inbox, not in trash</div>
      Unsolicited prescription medication spam (Semaglutide/Tirzepatide) from garbage domain. <strong>Delete and block sender.</strong>
    </div>

    <div class="card red">
      <div class="card-title"><span class="badge badge-red">SPAM — DELETE</span> "Sex.Trick🍆" — Adult Spam (×2 identical emails)</div>
      <div class="card-meta">Two separate emails: Sat Jul 11, 9:27 PM and 9:21 PM | Not in inbox, not in trash</div>
      Explicit adult spam with offensive subject lines from garbage domains. <strong>Delete both and block sender.</strong>
    </div>

    <div class="card red">
      <div class="card-title"><span class="badge badge-red">SPAM — DELETE</span> "Dr. Arthur Green" — Penis Enlargement Scam</div>
      <div class="card-meta">From: jukxkdwbnbwhtf.26076492291058@ynu7xe.8g3f04.r5rdpp.us — Sat Jul 11, 9:50 PM | Not in inbox</div>
      Targets melissaw212 by name. Classic predatory spam. <strong>Delete and block.</strong>
    </div>
  </div>
</div>

<div class="section-wrap">
  <div class="section-header green-header">💼 Job Search <span class="count-badge">6 emails</span></div>
  <div class="section-body">
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Date</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>Indeed</td><td>Chief People Officer @ Pearl Health — $270K–$310K</td><td>Jul 12</td><td><span class="badge badge-green">Apply This Week</span></td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>Senior Director, People Business Partner at GitLab</td><td>Jul 12</td><td><span class="badge badge-green">Apply ASAP</span></td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>Chief People Officer at Sunday (×2 alerts)</td><td>Jul 12</td><td><span class="badge badge-yellow">Review &amp; Apply Once</span></td></tr>
        <tr><td>LinkedIn</td><td>New jobs similar to VP of Human Resources at Tiberius Aerospace</td><td>Jul 12</td><td><span class="badge badge-yellow">Review List</span></td></tr>
        <tr><td>Melissa (Self-sent)</td><td>HR Leader for 160over90 — 13 Years in Media &amp; Creative</td><td>Jul 12</td><td><span class="badge badge-gray">In Trash — Verify Intent</span></td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="section-wrap">
  <div class="section-header purple-header">🤝 Recruiters / Networking <span class="count-badge">2 emails</span></div>
  <div class="section-body">
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Date</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>Lisa Rangel (Chameleon Resumes)</td><td>"Worth a closer look." — Executive Resume Tips (5 conference flubs)</td><td>Jul 12</td><td><span class="badge badge-gray">In Trash — Review if interested in executive branding tips</span></td></tr>
        <tr><td>Ashwin @ MobiusEngineHub</td><td>$200 in service value — 2 weeks free job application service</td><td>Jul 12</td><td><span class="badge badge-gray">Low priority — not in inbox; evaluate vendor before engaging</span></td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="section-wrap">
  <div class="section-header blue-header">📅 Calendar / Events <span class="count-badge">1 email</span></div>
  <div class="section-body">
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Date</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>Melissa (Self-sent)</td><td>Melissa's Daily Briefing — 2026-07-12</td><td>Jul 12, 6:15 AM</td><td><span class="badge badge-blue">Reference Only — Superseded by this briefing</span></td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="section-wrap">
  <div class="section-header" style="background:#e74c3c;color:#fff;">🏥 Medical / Health <span class="count-badge">1 email</span></div>
  <div class="section-body">
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Date</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>Alison Courses</td><td>"Melissa A, you don't have to be 'The Overconfident Striker.'" — Workplace skills free courses</td><td>Jul 12</td><td><span class="badge badge-gray">Low priority — wellness/professional development crossover; review if relevant</span></td></tr>
      </tbody>
    </table>
    <div class="note">Note: Medical appointments are covered in the Calendar section. No medical correspondence emails in this batch.</div>
  </div>
</div>

<div class="section-wrap">
  <div class="section-header yellow-header">💳 Financial / Billing <span class="count-badge">1 email</span></div>
  <div class="section-body">
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Date</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>Synchrony Bank</td><td>Your CareCredit / Synchrony Bank Payment Has Posted — $250.00 on acct ending 7483</td><td>Jul 12, 8:00 AM</td><td><span class="badge badge-yellow">Verify balance — log into account</span></td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="section-wrap">
  <div class="section-header purple-header">📚 Professional Development <span class="count-badge">3 emails</span></div>
  <div class="section-body">
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Date</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>Adam Karpiak (LinkedIn Newsletter)</td><td>ICYMI: AI Ruined Resume Writing</td><td>Jul 12</td><td><span class="badge badge-purple">Read — directly relevant to job search</span></td></tr>
        <tr><td>Medium (Jerry PM)</td><td>12 AI Prompt Websites Worth Bookmarking</td><td>Jul 12</td><td><span class="badge badge-purple">Read if time — useful AI tools</span></td></tr>
        <tr><td>Medium (Marina Wyss) — In Trash</td><td>Should You Still Learn to Code in 2026?</td><td>Jul 12</td><td><span class="badge badge-gray">In Trash — skim if interested in tech upskilling</span></td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="section-wrap">
  <div class="section-header" style="background:#e91e8c;color:#fff;">💕 Personal / Dating <span class="count-badge">3 emails</span></div>
  <div class="section-body">
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Date</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>Match.com</td><td>You've had a profile view from Seth (51, Torrington CT)</td><td>Jul 12, 1:01 AM</td><td><span class="badge badge-gray">Review Seth's profile at your leisure</span></td></tr>
        <tr><td>Jdate</td><td>You've Caught Someone's Eye 👀</td><td>Jul 12, 6:01 AM</td><td><span class="badge badge-gray">Check Jdate profile — new connection waiting</span></td></tr>
        <tr><td>Facebook</td><td>40 notifications about Jacqueline and others</td><td>Sat Jul 11</td><td><span class="badge badge-gray">Check Facebook when convenient</span></td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="section-wrap">
  <div class="section-header purple-header">📰 Newsletters / Subscriptions <span class="count-badge">4 emails</span></div>
  <div class="section-body">
    <table>
      <thead><tr><th>Sender</th><th>Topic</th><th>Date</th><th>Recommendation</th></tr></thead>
      <tbody>
        <tr><td>Adam Karpiak (LinkedIn)</td><td>AI &amp; Resume Writing — career-relevant</td><td>Jul 12</td><td><span class="badge badge-green">KEEP — Read</span></td></tr>
        <tr><td>Medium Daily Digest (@melissaw212)</td><td>AI Prompt Websites, Coding in 2026</td><td>Jul 12</td><td><span class="badge badge-purple">KEEP — Review when time permits</span></td></tr>
        <tr><td>Medium Daily Digest (@amylw516) — In Trash</td><td>Should You Learn to Code in 2026?</td><td>Jul 12</td><td><span class="badge badge-gray">Different account — consider unsubscribing duplicate Medium account</span></td></tr>
        <tr><td>CoolDeep AI (Beehiiv)</td><td>Claude AI morning prompt tips</td><td>Jul 12</td><td><span class="badge badge-yellow">Review — AI productivity tips; keep if useful</span></td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="section-wrap">
  <div class="section-header gray-header">🛍️ Promotional / Retail <span class="count-badge">11 emails</span></div>
  <div class="section-body">
    <p style="font-size:13px;margin-bottom:12px;">Full detail in Promotional / Retail Summary section below. Summary here for accounting.</p>
    <table>
      <thead><tr><th>Brand</th><th>Subject</th><th>Date</th><th>Recommendation</th></tr></thead>
      <tbody>
        <tr><td>VIVAIA</td><td>Barely There. Fully Summer. | Summer Returns</td><td>Jul 12</td><td><span class="badge badge-gray">Delete / Ignore</span></td></tr>
        <tr><td>Old Navy</td><td>Cart-worthy Clearance from $3.99</td><td>Jul 12</td><td><span class="badge badge-gray">Delete / Ignore</span></td></tr>
        <tr><td>Shopify</td><td>The best business ideas are seasonal</td><td>Jul 12</td><td><span class="badge badge-gray">Delete / Ignore</span></td></tr>
        <tr><td>Kohl's</td><td>Save 30% | Summer looks</td><td>Jul 12</td><td><span class="badge badge-gray">Delete / Ignore</span></td></tr>
        <tr><td>SHEIN (×2)</td><td>Your Summer Mood Board ☀️ (duplicate send)</td><td>Jul 12</td><td><span class="badge badge-gray">Delete Both</span></td></tr>
        <tr><td>Laura Geller (×2)</td><td>Final Deal Alert 🔔 45% OFF (duplicate send)</td><td>Jul 12</td><td><span class="badge badge-gray">Delete Both</span></td></tr>
        <tr><td>TikTok Shop</td><td>Your order is confirmed!</td><td>Jul 12</td><td><span class="badge badge-yellow">Keep for Order Tracking</span></td></tr>
        <tr><td>YesStyle.com</td><td>🚨 Adorable items + EXTRA 15% off</td><td>Jul 12</td><td><span class="badge badge-gray">Delete / Ignore</span></td></tr>
        <tr><td>Pranit Naik (Medium)</td><td>ChatGPT 5.6 Just Launched for the Public</td><td>Jul 12</td><td><span class="badge badge-purple">Skim if interested in AI news</span></td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     7. TRASH REVIEW
═══════════════════════════════════════════════════════════════ -->
<div class="section-wrap">
  <div class="section-header red-header">🗑️ Trash Review</div>
  <div class="section-body">

    <h3 style="margin-bottom:10px;color:#27ae60;">✅ Restore Immediately</h3>
    <div class="card green">
      <div class="card-title">None — No emails in trash require immediate restoration.</div>
      <div class="card-meta">No legitimate emails found in trash that require action or restoration.</div>
    </div>

    <div class="divider"></div>
    <h3 style="margin-bottom:10px;color:#e67e22;">⚠️ Review Before Deleting</h3>

    <div class="card yellow">
      <div class="card-title">Melissa → Brianne (160over90): "HR Leader for 160over90 — 13 Years in Media &amp; Creative"</div>
      <div class="card-meta">From: melissaw212@gmail.com | Sun Jul 12, 7:43 PM | Found in Trash</div>
      This is an outbound email <em>you sent</em> (or drafted) to Brianne at 160over90 pitching yourself for an HR leadership role. It was found in your Trash. <strong>Review: Did you intentionally trash this (decided not to send/pursue), or was this accidentally deleted?</strong> If you want to follow up with Brianne, restore this thread and verify the email was actually sent.
    </div>

    <div class="card yellow">
      <div class="card-title">Lisa Rangel (Chameleon Resumes): "Worth a closer look."</div>
      <div class="card-meta">From: lr@chameleonresumes.com | Sun Jul 12, 11:22 AM | In Trash</div>
      Executive resume coach newsletter — "five conference flubs to avoid." Legitimate sender; content may be relevant to your job search. <strong>Review the tips on conference networking before deleting.</strong>
    </div>

    <div class="card yellow">
      <div class="card-title">Medium Daily Digest (@amylw516): "Should You Still Learn to Code in 2026?"</div>
      <div class="card-meta">From: noreply@medium.com | Sun Jul 12, 11:00 AM | In Trash</div>
      Appears to be a Medium digest for a secondary account (amylw516 vs. your main melissaw212 account). Likely intentionally trashed. <strong>Consider: Do you use this second Medium account? If not, unsubscribe.</strong>
    </div>

    <div class="card yellow">
      <div class="card-title">TrimRx.Weight.Care: "12 months from now you'll either have done this or not"</div>
      <div class="card-meta">From: mcfpxyvrqbw@hxmv.uxcudrfxvjkjr.us | Sun Jul 12, 6:06 AM | In Trash</div>
      GLP-1 weight loss medication promo from a garbage domain. Could be legitimate telehealth spam or a phishing attempt. <strong>Do not click links — permanently delete.</strong>
    </div>

    <div class="card yellow">
      <div class="card-title">Casino Spam: "200 Free Spins — GRIFFINS200"</div>
      <div class="card-meta">From: cfgtbijuoioyke@7bwamx.km8rfy.d8j4gp.us | Sat Jul 11, 11:39 PM | In Trash</div>
      Obvious casino spam with fake prize/free spins offer from garbage domain. Already in trash. <strong>Permanently delete.</strong>
    </div>

    <div class="divider"></div>
    <h3 style="margin-bottom:10px;color:#c0392b;">🗑️ Safe to Delete Permanently</h3>

    <div class="card gray">
      <div class="card-title">All 10 Auto-Trashed Phishing Emails</div>
      <div class="card-meta">Cloud.Storage (×5), Cloud.Security (×3), Payment-Declined (×2) — all from garbage .us domains</div>
      Already auto-trashed. <strong>Permanently delete from trash. No action needed.</strong>
    </div>

    <div class="card gray">
      <div class="card-title">SHEIN (×2 duplicates), Laura Geller (×2 duplicates)</div>
      <div class="card-meta">Already read/archived — promotional duplicates</div>
      <strong>Safe to permanently delete.</strong>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     8. PROMOTIONAL / RETAIL SUMMARY
═══════════════════════════════════════════════════════════════ -->
<div class="section-wrap">
  <div class="section-header gray-header">🛍️ Promotional
