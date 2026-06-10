<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Melissa's Executive Briefing — June 10, 2026</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 16px; padding: 36px 40px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 16px; }
  .header-left h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header-left .date { font-size: 15px; color: #a8b2d8; margin-top: 4px; }
  .header-left .greeting { font-size: 18px; color: #e2e8f0; margin-bottom: 6px; }
  .header-stats { display: flex; gap: 20px; flex-wrap: wrap; }
  .stat-pill { background: rgba(255,255,255,0.12); border-radius: 10px; padding: 10px 18px; text-align: center; }
  .stat-pill .num { font-size: 24px; font-weight: 700; color: #63b3ed; }
  .stat-pill .lbl { font-size: 11px; color: #a8b2d8; text-transform: uppercase; letter-spacing: 0.5px; }

  /* SECTION TITLES */
  .section-title { font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin: 28px 0 12px; padding-left: 10px; border-left: 4px solid #4a5568; color: #2d3748; }
  .section-title.red { border-color: #e53e3e; color: #c53030; }
  .section-title.yellow { border-color: #d69e2e; color: #b7791f; }
  .section-title.blue { border-color: #3182ce; color: #2b6cb0; }
  .section-title.green { border-color: #38a169; color: #276749; }
  .section-title.purple { border-color: #805ad5; color: #6b46c1; }
  .section-title.gray { border-color: #718096; color: #4a5568; }
  .section-title.orange { border-color: #dd6b20; color: #c05621; }

  /* CARDS */
  .card { border-radius: 12px; padding: 16px 20px; margin-bottom: 12px; border-left: 5px solid #ccc; background: #fff; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }
  .card.red { border-color: #e53e3e; background: #fff5f5; }
  .card.yellow { border-color: #d69e2e; background: #fffff0; }
  .card.blue { border-color: #3182ce; background: #ebf8ff; }
  .card.green { border-color: #38a169; background: #f0fff4; }
  .card.purple { border-color: #805ad5; background: #faf5ff; }
  .card.gray { border-color: #718096; background: #f7fafc; }
  .card.orange { border-color: #dd6b20; background: #fffaf0; }

  .card h3 { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
  .card .meta { font-size: 12px; color: #718096; margin-bottom: 6px; }
  .card .why { font-size: 13px; margin-bottom: 4px; }
  .card .action { font-size: 13px; font-weight: 600; margin-top: 6px; }
  .card .due { font-size: 12px; color: #e53e3e; font-weight: 600; margin-top: 4px; }

  /* EXEC SUMMARY */
  .exec-summary { background: #fff; border-radius: 12px; padding: 20px 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 12px; }
  .exec-summary ul { list-style: none; padding: 0; }
  .exec-summary ul li { padding: 8px 0; border-bottom: 1px solid #e2e8f0; font-size: 14px; }
  .exec-summary ul li:last-child { border-bottom: none; }
  .badge { display: inline-block; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 700; margin-right: 8px; text-transform: uppercase; }
  .badge.red { background: #fed7d7; color: #c53030; }
  .badge.yellow { background: #fefcbf; color: #744210; }
  .badge.blue { background: #bee3f8; color: #2a4a7f; }
  .badge.green { background: #c6f6d5; color: #22543d; }
  .badge.purple { background: #e9d8fd; color: #553c9a; }
  .badge.gray { background: #e2e8f0; color: #4a5568; }
  .badge.orange { background: #feebc8; color: #7b341e; }

  /* CALENDAR */
  .cal-day { background: #fff; border-radius: 12px; padding: 14px 18px; margin-bottom: 12px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }
  .cal-day h3 { font-size: 14px; font-weight: 700; color: #2b6cb0; border-bottom: 1px solid #bee3f8; padding-bottom: 6px; margin-bottom: 10px; }
  .cal-event { display: grid; grid-template-columns: 110px 1fr; gap: 8px; padding: 8px 0; border-bottom: 1px dashed #e2e8f0; }
  .cal-event:last-child { border-bottom: none; }
  .cal-time { font-size: 12px; font-weight: 700; color: #4a5568; }
  .cal-details .title { font-weight: 700; font-size: 13px; }
  .cal-details .loc { font-size: 12px; color: #718096; }
  .cal-details .status { font-size: 11px; margin-top: 2px; }
  .cal-details .prep { font-size: 12px; color: #553c9a; margin-top: 2px; }
  .cal-details .conflict { font-size: 12px; color: #e53e3e; font-weight: 600; margin-top: 2px; }
  .status-pill { display: inline-block; padding: 1px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; }
  .status-pill.accepted { background: #c6f6d5; color: #22543d; }
  .status-pill.confirmed { background: #c6f6d5; color: #22543d; }
  .status-pill.needs { background: #fefcbf; color: #744210; }
  .status-pill.declined { background: #fed7d7; color: #c53030; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,0.07); margin-bottom: 16px; }
  th { background: #2d3748; color: #fff; padding: 10px 14px; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; text-align: left; }
  td { padding: 9px 14px; font-size: 13px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #f7fafc; }
  .pri-high { color: #c53030; font-weight: 700; }
  .pri-med { color: #b7791f; font-weight: 700; }
  .pri-low { color: #276749; font-weight: 700; }
  .fit-high { display: inline-block; background: #c6f6d5; color: #22543d; padding: 1px 7px; border-radius: 10px; font-size: 11px; font-weight: 700; }
  .fit-med { display: inline-block; background: #fefcbf; color: #744210; padding: 1px 7px; border-radius: 10px; font-size: 11px; font-weight: 700; }
  .fit-low { display: inline-block; background: #e2e8f0; color: #4a5568; padding: 1px 7px; border-radius: 10px; font-size: 11px; font-weight: 700; }

  /* DASHBOARD GRID */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; margin-bottom: 16px; }
  .dash-tile { background: #fff; border-radius: 12px; padding: 16px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); border-top: 4px solid #ccc; }
  .dash-tile.red { border-top-color: #e53e3e; }
  .dash-tile.yellow { border-top-color: #d69e2e; }
  .dash-tile.blue { border-top-color: #3182ce; }
  .dash-tile.green { border-top-color: #38a169; }
  .dash-tile.purple { border-top-color: #805ad5; }
  .dash-tile.gray { border-top-color: #718096; }
  .dash-tile h4 { font-size: 11px; text-transform: uppercase; letter-spacing: 0.7px; color: #718096; margin-bottom: 6px; }
  .dash-tile .big-num { font-size: 28px; font-weight: 800; margin-bottom: 4px; }
  .dash-tile .big-num.red { color: #e53e3e; }
  .dash-tile .big-num.yellow { color: #d69e2e; }
  .dash-tile .big-num.blue { color: #3182ce; }
  .dash-tile .big-num.green { color: #38a169; }
  .dash-tile .big-num.purple { color: #805ad5; }
  .dash-tile ul { list-style: none; font-size: 12px; color: #4a5568; }
  .dash-tile ul li { padding: 2px 0; border-bottom: 1px solid #f0f0f0; }
  .dash-tile ul li:last-child { border-bottom: none; }

  /* TOP 3 */
  .top3 { background: linear-gradient(135deg, #1a1a2e, #0f3460); color: #fff; border-radius: 14px; padding: 24px 30px; margin-top: 28px; }
  .top3 h2 { font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #63b3ed; margin-bottom: 16px; }
  .top3-item { display: flex; gap: 16px; align-items: flex-start; margin-bottom: 14px; }
  .top3-num { font-size: 32px; font-weight: 900; color: #63b3ed; line-height: 1; min-width: 36px; }
  .top3-text h3 { font-size: 15px; font-weight: 700; color: #e2e8f0; margin-bottom: 2px; }
  .top3-text p { font-size: 13px; color: #a8b2d8; }

  /* ACCOUNTING */
  .accounting-total { background: #2d3748; color: #fff; font-weight: 700; }
  .accounting-total td { color: #63b3ed; font-size: 14px; }

  /* MISC */
  .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
  @media (max-width: 680px) { .two-col { grid-template-columns: 1fr; } .header { flex-direction: column; align-items: flex-start; } .cal-event { grid-template-columns: 1fr; } }
  .spam-warn { font-size: 12px; background: #fed7d7; color: #c53030; border-radius: 6px; padding: 4px 10px; display: inline-block; font-weight: 700; margin-left: 6px; }
  .divider { border: none; border-top: 2px solid #e2e8f0; margin: 20px 0; }
  .note-box { background: #ebf8ff; border-left: 4px solid #3182ce; border-radius: 6px; padding: 10px 14px; font-size: 13px; color: #2b6cb0; margin-bottom: 12px; }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ═══════════════════════════════════════════════════════════════
     1. HEADER
════════════════════════════════════════════════════════════════ -->
<div class="header">
  <div class="header-left">
    <div class="greeting">☀️ Good Morning, Melissa!</div>
    <h1>Executive Daily Briefing</h1>
    <div class="date">Wednesday, June 10, 2026 &nbsp;·&nbsp; Prepared by Your Chief of Staff</div>
  </div>
  <div class="header-stats">
    <div class="stat-pill"><div class="num">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="stat-pill"><div class="num">9</div><div class="lbl">Calendar Events</div></div>
    <div class="stat-pill"><div class="num">3</div><div class="lbl">Action Required</div></div>
    <div class="stat-pill"><div class="num">2</div><div class="lbl">Today's Meetings</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     2. EXECUTIVE SUMMARY
════════════════════════════════════════════════════════════════ -->
<div class="section-title red">⚡ Executive Summary</div>
<div class="exec-summary">
  <ul>
    <li><span class="badge red">🚨 Risk</span> <strong>Phishing / Scam Emails Detected:</strong> At least 2 confirmed scam emails are sitting unread in your inbox/non-trash — a fake "Lowe's" prize winner email from a suspicious domain and a similarly styled scam (RIDGID Cordless kit offer). Do NOT click. Flag and delete immediately.</li>
    <li><span class="badge green">💼 Opportunity</span> <strong>LinkedIn CPO Alert — Pearl Health:</strong> A Chief People Officer role at Pearl Health hit your LinkedIn Job Alerts today. You also have a 15-minute Zoom consultation with Netta Jenkins (Fri, Jun 12) and a Guidepoint HR consulting inquiry to respond to. Active pipeline requires attention.</li>
    <li><span class="badge yellow">📅 Deadline</span> <strong>Chase Payment Due Jun 15 + Dentist Appointment Jun 17:</strong> Your Chase Slate Visa payment is due in 5 days. Dentist appointment confirmed at Rosen &amp; Deutch for Wed Jun 17 at 9:15 AM. Also: <strong>today's HR Networking Zoom starts at 12:00 PM ET</strong> — RSVP is still pending.</li>
  </ul>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     3. ACTION REQUIRED
════════════════════════════════════════════════════════════════ -->
<div class="section-title red">🔴 Action Required</div>

<div class="card red">
  <h3>🚨 Delete Phishing / Scam Emails Immediately</h3>
  <div class="meta">From: "LOWER" (Noreply-JnT0CIl4@jnt0cil4jnt0cil4.ca) &amp; "Lowe's®" (pasupportxk@foaxxgyhhhtrnvigodnbtoiz.com)</div>
  <div class="why"><strong>Why it matters:</strong> Both emails impersonate Lowe's with prize/tool-kit offers using clearly fraudulent domains. One targets your username (melissaw212) directly. These are credential phishing attempts.</div>
  <div class="action">✅ Next Step: Do NOT click any links. Mark as phishing/spam in Gmail and delete from all folders.</div>
  <div class="due">⏰ Due: Immediately</div>
</div>

<div class="card yellow">
  <h3>💳 Chase Slate Visa Payment Due</h3>
  <div class="meta">From: Chase &lt;no.reply.alerts@chase.com&gt; — Jun 10, 2026</div>
  <div class="why"><strong>Why it matters:</strong> Your credit card payment is due June 15, 2026. Missing this will result in a late fee and potential credit score impact.</div>
  <div class="action">✅ Next Step: Log into Chase and confirm a scheduled payment of at least the minimum (or full balance) before June 15.</div>
  <div class="due">⏰ Due: June 15, 2026</div>
</div>

<div class="card yellow">
  <h3>📅 RSVP: HR Networking Zoom — TODAY at 12:00 PM ET</h3>
  <div class="meta">From: Fireflies.ai meeting prep + Calendar (needsAction)</div>
  <div class="why"><strong>Why it matters:</strong> Your calendar shows this event with status "needsAction." Fireflies.ai sent a meeting prep reminder 1 hour in advance. This is your core job-search networking group.</div>
  <div class="action">✅ Next Step: Confirm attendance and join Zoom: https://us06web.zoom.us/j/81954171722</div>
  <div class="due">⏰ Due: TODAY — 12:00 PM ET</div>
</div>

<div class="card yellow">
  <h3>🦷 Confirm Dentist Appointment — Jun 17</h3>
  <div class="meta">From: Rosen &amp; Deutch, DDS PC — Jun 10, 2026</div>
  <div class="why"><strong>Why it matters:</strong> You have an appointment Wednesday, June 17th at 9:15 AM. The reminder asks you to confirm. Note: your calendar shows a cleaning at 10:45 AM on Jun 17 — there may be a 90-minute gap or a time discrepancy to verify.</div>
  <div class="action">✅ Next Step: Confirm the appointment via the link in the email. Verify exact time vs. calendar entry.</div>
  <div class="due">⏰ Due: Before June 17</div>
</div>

<div class="card green">
  <h3>💼 Respond to Guidepoint HR Consulting Inquiry (LinkedIn InMail)</h3>
  <div class="meta">From: Serafeim Makkas via LinkedIn — Jun 10, 2026</div>
  <div class="why"><strong>Why it matters:</strong> A recruiter from Guidepoint is reaching out about HR consulting opportunities in IT/Technology consultancies. This is a paid expert-network gig or consulting role that fits your HR background.</div>
  <div class="action">✅ Next Step: Review the InMail on LinkedIn and respond to Accept or Decline the opportunity.</div>
  <div class="due">⏰ Due: Within 48 hours</div>
</div>

<div class="card green">
  <h3>💼 Review CPO Role: Chief People Officer — Pearl Health (LinkedIn)</h3>
  <div class="meta">From: LinkedIn Job Alerts — Jun 10, 2026</div>
  <div class="why"><strong>Why it matters:</strong> A Chief People Officer role at Pearl Health (health tech) just appeared in your job alerts. This is likely a high-fit senior role given your HR leadership background.</div>
  <div class="action">✅ Next Step: Open the LinkedIn alert, review the role, and apply or save to job tracker immediately (roles like this close fast).</div>
  <div class="due">⏰ Due: Today or Tomorrow</div>
</div>

<div class="card blue">
  <h3>🏠 A/C Preventative Maintenance — 27th &amp; 28th Floors</h3>
  <div class="meta">From: 303 East 83rd &lt;no-reply@callmax.us&gt; — Jun 10, 2026 (UNREAD, IN INBOX)</div>
  <div class="why"><strong>Why it matters:</strong> Annual A/C maintenance is being scheduled at your building. You may need to confirm access to your unit or be home during the service window.</div>
  <div class="action">✅ Next Step: Read the full email to get the scheduled date/window and confirm access or request a different time if needed.</div>
  <div class="due">⏰ Due: Check email for specific date</div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     4. FULL 7-DAY CALENDAR
════════════════════════════════════════════════════════════════ -->
<div class="section-title blue">📅 Full 7-Day Calendar</div>
<div class="note-box">📌 Showing all 9 events from calendar data spanning June 10–17, 2026.</div>

<!-- Wednesday June 10 -->
<div class="cal-day">
  <h3>📅 Wednesday, June 10, 2026 — TODAY</h3>

  <div class="cal-event">
    <div class="cal-time">12:00 PM – 1:30 PM</div>
    <div class="cal-details">
      <div class="title">HR Networking &amp; Job Search Group – Zoom 2</div>
      <div class="loc">🔗 <a href="https://us06web.zoom.us/j/81954171722" target="_blank">Zoom Link</a></div>
      <div class="status"><span class="status-pill needs">⚠️ Needs Action / RSVP Pending</span></div>
      <div class="prep">🟣 Prep: Fireflies.ai sent meeting prep — review key takeaways from last session. Prepare your 30-second networking intro and any job search updates to share.</div>
      <div class="conflict">⚠️ CONFLICT: "Melissa x Meg Drinks" overlaps at 1:00 PM — Networking ends at 1:30 PM, drinks start at 1:00 PM. You will be 30 minutes late or need to leave Zoom early.</div>
    </div>
  </div>

  <div class="cal-event">
    <div class="cal-time">12:00 PM – 1:30 PM</div>
    <div class="cal-details">
      <div class="title">Network (Personal Calendar Block)</div>
      <div class="loc">📍 No location listed</div>
      <div class="status"><span class="status-pill confirmed">✅ Confirmed</span></div>
      <div class="prep">🔵 This appears to be a personal block that mirrors the HR Networking Zoom. No additional prep needed — it's likely a reminder.</div>
    </div>
  </div>

  <div class="cal-event">
    <div class="cal-time">1:00 PM – 2:00 PM</div>
    <div class="cal-details">
      <div class="title">Melissa x Meg Drinks ☕</div>
      <div class="loc">📍 Caffè Bacio — 1223 3rd Ave, New York</div>
      <div class="status"><span class="status-pill accepted">✅ Accepted</span></div>
      <div class="prep">🟢 Meg Park (megpark@oakleafpartnership.com) — likely a professional networking contact. Come prepared to discuss job search status, mutual connections, and next steps. Bring business cards or LinkedIn QR code.</div>
      <div class="conflict">⚠️ CONFLICT: Overlaps with HR Networking Zoom (ends 1:30 PM). Plan to leave Zoom at 1:00 PM sharp or arrive late to Caffè Bacio.</div>
    </div>
  </div>
</div>

<!-- Thursday June 11 -->
<div class="cal-day">
  <h3>📅 Thursday, June 11, 2026</h3>

  <div class="cal-event">
    <div class="cal-time">9:00 AM – 10:30 AM</div>
    <div class="cal-details">
      <div class="title">Executive Roundtable (Zoom — John Madigan)</div>
      <div class="loc">🔗 <a href="https://us02web.zoom.us/j/207786667" target="_blank">Zoom Link</a> · Meeting ID: 207 786 667 · PW: 205454</div>
      <div class="status"><span class="status-pill declined">❌ Declined</span></div>
      <div class="prep">⚠️ You have declined this event. If you wish to reconsider, contact John Madigan. No prep required unless you reverse this decision.</div>
    </div>
  </div>

  <div class="cal-event">
    <div class="cal-time">12:00 PM – 1:00 PM</div>
    <div class="cal-details">
      <div class="title">HR Networking &amp; Job Search: Open Office Hours – Zoom 2</div>
      <div class="loc">🔗 <a href="https://us06web.zoom.us/j/85945371140" target="_blank">Zoom Link</a></div>
      <div class="status"><span class="status-pill needs">⚠️ Needs Action / RSVP Pending</span></div>
      <div class="prep">🟣 Prep: Open office hours format — no agenda required, but come with specific questions about your job search or resume. Note: event description asks to turn off AI notetaking tools.</div>
    </div>
  </div>
</div>

<!-- Friday June 12 -->
<div class="cal-day">
  <h3>📅 Friday, June 12, 2026</h3>

  <div class="cal-event">
    <div class="cal-time">9:30 AM – 9:45 AM</div>
    <div class="cal-details">
      <div class="title">Melissa Weiss x Netta Jenkins — 15-Min Zoom Consultation</div>
      <div class="loc">🔗 <a href="https://us06web.zoom.us/j/5224221004" target="_blank">Zoom Link</a> · PW: 424726</div>
      <div class="status"><span class="status-pill accepted">✅ Accepted</span></div>
      <div class="prep">🟢 Netta Jenkins from Hicconsult.com. This is a consulting or coaching session — come with 3 specific goals or questions. Review her LinkedIn profile beforehand. It's only 15 minutes so be sharp and prepared.</div>
    </div>
  </div>
</div>

<!-- Sat Jun 13, Sun Jun 14 — no events -->
<div class="cal-day">
  <h3>📅 Saturday, June 13 – Sunday, June 14, 2026</h3>
  <div class="cal-event">
    <div class="cal-time">All Day</div>
    <div class="cal-details">
      <div class="title">No calendar events scheduled this weekend.</div>
      <div class="prep">✨ Consider using this time to apply to the Pearl Health CPO role and review your ZenSearch job matches.</div>
    </div>
  </div>
</div>

<!-- Monday June 15 -->
<div class="cal-day">
  <h3>📅 Monday, June 15, 2026</h3>

  <div class="cal-event">
    <div class="cal-time">9:30 AM – 11:00 AM</div>
    <div class="cal-details">
      <div class="title">Hair Appointment — Elle at UMI Salon (Single Process + Blowout)</div>
      <div class="loc">📍 37 West 20th Street, Suite 1107, New York, NY 10011</div>
      <div class="status"><span class="status-pill confirmed">✅ Confirmed</span></div>
      <div class="prep">🔵 Appointment with Elle M. Manage or cancel at: elleatumi.glossgenius.com. Block 90 min + travel time. <br><strong>⚠️ DEADLINE REMINDER:</strong> Chase Slate Visa payment is also due today — pay before you leave!</div>
    </div>
  </div>
</div>

<!-- Tuesday June 16 -->
<div class="cal-day">
  <h3>📅 Tuesday, June 16, 2026</h3>

  <div class="cal-event">
    <div class="cal-time">10:00 AM – 11:00 AM</div>
    <div class="cal-details">
      <div class="title">Vet Appointment (Stella 🐾)</div>
      <div class="loc">📍 Location not listed in calendar</div>
      <div class="status"><span class="status-pill confirmed">✅ Confirmed</span></div>
      <div class="prep">🔵 Chewy sent a 20% off flea &amp; tick prescription offer today — consider ordering at the same time if Stella needs a refill. Add vet address/details to calendar entry.</div>
    </div>
  </div>
</div>

<!-- Wednesday June 17 -->
<div class="cal-day">
  <h3>📅 Wednesday, June 17, 2026</h3>

  <div class="cal-event">
    <div class="cal-time">10:45 AM – 11:45 AM</div>
    <div class="cal-details">
      <div class="title">Dentist Cleaning — Dr. Deutch</div>
      <div class="loc">📍 Location not listed in calendar</div>
      <div class="status"><span class="status-pill confirmed">✅ Confirmed</span></div>
      <div class="prep">⚠️ Note: Rosen &amp; Deutch appointment reminder email says 9:15 AM but calendar shows 10:45 AM. Verify the correct time before June 17 and update your calendar accordingly. Confirm via the reminder email link.</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     5. JOB SEARCH & INTERVIEW PIPELINE
════════════════════════════════════════════════════════════════ -->
<div class="section-title green">💼 Job Search &amp; Interview Pipeline</div>

<table>
  <thead>
    <tr>
      <th>Type</th>
      <th>Opportunity / Source</th>
      <th>Details</th>
      <th>Fit</th>
      <th>Action</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="badge green">JOB ALERT</span></td>
      <td>Chief People Officer — Pearl Health</td>
      <td>LinkedIn Job Alerts, Jun 10. Health tech CPO role — senior executive level.</td>
      <td><span class="fit-high">HIGH</span></td>
      <td>Review &amp; apply immediately. CPO roles close fast.</td>
    </tr>
    <tr>
      <td><span class="badge green">JOB MATCH</span></td>
      <td>Director, HR Business Partner — Omada Health</td>
      <td>ZenSearch Daily Zen. New York, NY. Part-time. $18X (salary truncated).</td>
      <td><span class="fit-high">HIGH</span></td>
      <td>Open ZenSearch email and review full job description. Apply if fit.</td>
    </tr>
    <tr>
      <td><span class="badge purple">RECRUITER</span></td>
      <td>Guidepoint HR Consulting — IT &amp; Tech Consultancies</td>
      <td>LinkedIn InMail from Serafeim Makkas. Expert network / consulting engagement.</td>
      <td><span class="fit-high">HIGH</span></td>
      <td>Accept/Decline InMail within 48 hours on LinkedIn.</td>
    </tr>
    <tr>
      <td><span class="badge blue">NETWORKING</span></td>
      <td>HR Networking &amp; Job Search Group — Zoom</td>
      <td>TODAY 12:00–1:30 PM ET. Large group (180+ attendees). RSVP pending.</td>
      <td><span class="fit-high">HIGH</span></td>
      <td>Confirm attendance. Join Zoom. Prepare 30-sec intro.</td>
    </tr>
    <tr>
      <td><span class="badge blue">NETWORKING</span></td>
      <td>Melissa x Meg Drinks — Caffè Bacio</td>
      <td>TODAY 1:00–2:00 PM. Meg Park, Oakleaf Partnership. 1223 3rd Ave.</td>
      <td><span class="fit-high">HIGH</span></td>
      <td>Attend. Research Meg's background. Discuss mutual opportunities.</td>
    </tr>
    <tr>
      <td><span class="badge blue">CONSULTATION</span></td>
      <td>15-Min Zoom with Netta Jenkins — HIC Consult</td>
      <td>Fri Jun 12, 9:30 AM. Coaching or consulting session. Accepted.</td>
      <td><span class="fit-high">HIGH</span></td>
      <td>Prep 3 focused questions/goals. Review Netta's profile.</td>
    </tr>
    <tr>
      <td><span class="badge blue">NETWORKING</span></td>
      <td>HR Networking Open Office Hours — Zoom (Jun 11)</td>
      <td>Thu Jun 11, 12:00–1:00 PM. RSVP pending. No AI notetaking requested.</td>
      <td><span class="fit-med">MEDIUM</span></td>
      <td>RSVP and attend. Bring specific job search questions.</td>
    </tr>
    <tr>
      <td><span class="badge purple">EVENT INVITE</span></td>
      <td>PeopleOps Networking: How HR Moves Business Metrics</td>
      <td>From Phil Strazzulla (SelectSoftware). Tue Jun 23, 8:30–10:30 AM EDT. Whoops? (NYC venue implied).</td>
      <td><span class="fit-med">MEDIUM</span></td>
      <td>Review invite and RSVP if aligned with networking goals.</td>
    </tr>
    <tr>
      <td><span class="badge purple">EVENT INVITE</span></td>
      <td>CHRO Panel: "The CHRO's Real Superpower"</td>
      <td>Tiphani Krueger, McLean &amp; Company. Tomorrow afternoon (Thu Jun 11).</td>
      <td><span class="fit-med">MEDIUM</span></td>
      <td>Review email and register if interested in CHRO-level content.</td>
    </tr>
    <tr>
      <td><span class="badge gray">JOB SEARCH</span></td>
      <td>HR Search AM Automated Runs (x2)</td>
      <td>Self-sent via GitHub Actions. Run 27283631679 (19 Apify results) + Run 27277318661 (17 Apify results + 1 Exa).</td>
      <td><span class="fit-med">MEDIUM</span></td>
      <td>Open both result emails and scan for new relevant postings.</td>
    </tr>
    <tr>
      <td><span class="badge gray">JOB PLATFORM</span></td>
      <td>Y Combinator Work at a Startup — Action Required</td>
      <td>Profile may be stale. YC following up on application status.</td>
      <td><span class="fit-low">LOW</span></td>
      <td>Decide: update profile or unsubscribe if no longer targeting startups.</td>
    </tr>
    <tr>
      <td><span class="badge gray">OUTREACH</span></td>
      <td>Whitefriar Online Reputation / Media Placement</td>
      <td>Darenia Alarcon via LinkedIn — Forbes/Bloomberg placement offer. Sales pitch.</td>
      <td><span class="fit-low">LOW</span></td>
      <td>Low priority. Review only if actively building personal brand PR.</td>
    </tr>
  </tbody>
</table>

<!-- ═══════════════════════════════════════════════════════════════
     6. FULL EMAIL REVIEW BY CATEGORY
════════════════════════════════════════════════════════════════ -->
<div class="section-title red">📧 Full Email Review by Category</div>

<!-- SECURITY / RISK -->
<div class="card red">
  <h3>🔴 Security / Risk — 2 Emails</h3>
  <div class="meta">Senders: "LOWER" (jnt0cil4jnt0cil4.ca) · "Lowe's®" (foaxxgyhhhtrnvigodnbtoiz.com)</div>
  <div class="why"><strong>Summary:</strong> Two confirmed phishing/scam emails impersonating Lowe's brand. One targets username "melissaw212" with a RIDGID Cordless Tool combo kit offer. Other claims you are a "winner" of a Kobalt Tool Set. Both use fake domains and obfuscated Unicode text to bypass spam filters.</div>
  <div class="action">🚨 Recommended Action: DO NOT CLICK. Report as phishing in Gmail. Delete immediately from all folders including non-trash locations.</div>
</div>

<!-- JOB SEARCH -->
<div class="card green">
  <h3>🟢 Job Search — 4 Emails</h3>
  <div class="meta">Senders: LinkedIn Job Alerts · ZenSearch · HR Search AM (x2 self-sent)</div>
  <div class="why"><strong>Summary:</strong> Chief People Officer alert (Pearl Health, LinkedIn); Director HRBP at Omada Health (ZenSearch); two automated HR Search AM result emails from GitHub Actions (combined 36+ job results via Apify/Exa). High-quality pipeline activity today.</div>
  <div class="action">✅ Recommended Action: Open all four emails. Prioritize Pearl Health CPO and Omada Health HRBP. Scan automated results for new leads.</div>
</div>

<!-- RECRUITERS / NETWORKING -->
<div class="card green">
  <h3>🟢 Recruiters / Networking — 5 Emails</h3>
  <div class="meta">Senders: Serafeim Makkas (Guidepoint/LinkedIn) · Phil Strazzulla (PeopleOps Event) · Tiphani Krueger (McLean &amp; Co CHRO Panel) · Darenia Alarcon (Whitefriar/LinkedIn) · Fireflies.ai (Meeting Prep)</div>
  <div class="why"><strong>Summary:</strong> Guidepoint consulting InMail is a strong monetizable opportunity. PeopleOps networking event Jun 23 is relevant for HR professionals. McLean &amp; Co CHRO panel is tomorrow. Whitefriar is a sales pitch for media placement. Fireflies.ai sent meeting prep for today's HR Zoom (useful).</div>
  <div class="action">✅ Recommended Action: Respond to Guidepoint InMail. Register for CHRO panel (tomorrow). Review PeopleOps event. Ignore Whitefriar unless PR is a priority.</div>
</div>

<!-- CALENDAR / EVENTS -->
<div class="card blue">
  <h3>🔵 Calendar / Events — 1 Email</h3>
  <div class="meta">Sender: Substack (Ken Harbaugh Show / Meidas Defense Weekly)</div>
  <div class="why"><strong>Summary:</strong> Live Substack video notification — Meidas Defense Weekly Update, June 10. Not directly calendar-related but a time-sensitive live event.</div>
  <div class="action">📌 Recommended Action: Watch if interested in current events. Low priority for executive action.</div>
</div>

<!-- MEDICAL / HEALTH -->
<div class="card blue">
  <h3>🔵 Medical / Health — 1 Email</h3>
  <div class="meta">Sender: Rosen &amp; Deutch, DDS PC</div>
  <div class="why"><strong>Summary:</strong> Appointment reminder for Melissa Weiss — Wednesday, June 17th at 9:15 AM. Note: calendar entry shows 10:45 AM. Time discrepancy needs to be reconciled.</div>
  <div class="action">✅ Recommended Action: Confirm appointment via link in email. Verify and correct time on calendar.</div>
</div>

<!-- FINANCIAL / BILLING -->
<div class="card yellow">
  <h3>🟡 Financial / Billing — 5 Emails</h3>
  <div class="meta">Senders: Chase · Bank of America · Robinhood (x2) · Acorns (Trash)</div>
  <div class="why"><strong>Summary:</strong> Chase Slate Visa payment due June 15 — ACTION REQUIRED. Bank of America new Customized Cash Rewards Visa card — review account tools. Robinhood: order executed ($3.05 NVDA buy, account ••5739); New feature — connect AI agent to Robinhood (informational). Acorns promo (in Trash — low priority).</div>
  <div class="action">✅ Recommended Action: Pay Chase by Jun 15. Activate BoA card features if new card. Note NVDA trade execution. Skip Robinhood AI feature for now. Acorns promo = trash.</div>
</div>

<!-- PROFESSIONAL DEVELOPMENT -->
<div class="card purple">
  <h3>🟣 Professional Development — 3 Emails</h3>
  <div class="meta">Senders: Hacking HR (Trash) · Ariana Ruiz / LinkedIn Newsletter · Hebba Youssef (I Hate It Here)</div>
  <div class="why"><strong>Summary:</strong> Hacking HR newsletter (Who Owns Ethical AI — in Trash); Ariana Ruiz's "Empowered Leadership Exchange" on LinkedIn (unread, inbox); Hebba Youssef's HR newsletter about AI rollout and employee TikTok behavior (read, not in inbox). All relevant to HR leadership and AI-in-workplace trends.</div>
  <div class="action">📌 Recommended Action: Read Ariana Ruiz and Hebba Youssef newsletters — high relevance to current job search and CHRO positioning. Hacking HR can stay in trash unless you want to restore.</div>
</div>

<!-- PERSONAL -->
<div class="card orange">
  <h3>🟠 Personal — 3 Emails</h3>
  <div class="meta">Senders: 303 East 83rd (A/C Maintenance) · 303 East 83rd (Carpet Cleaning) · USPS Informed Delivery</div>
  <div class="why"><strong>Summary:</strong> A/C preventative maintenance notice for 27th &amp; 28th floors (UNREAD, needs response). Common area carpet cleaning scheduled today, completed by end of day (informational). USPS: 3 mailpieces arriving today, 0 packages.</div>
  <div class="action">✅ Recommended Action: Read A/C notice and confirm access. Carpet cleaning = no action. USPS = monitor mailbox today.</div>
</div>

<!-- NEWSLETTERS / SUBSCRIPTIONS -->
<div class="card purple">
  <h3>🟣 Newsletters / Subscriptions — 8 Emails</h3>
  <div class="meta">Senders: Mindstream (Trash) · Phil Strazzulla/SelectSoftware · Medium Daily Digest · CoolDeep AI · Techpresso/AI Academy · Mindstream AI newsletter · The Huntr Team · "1% Better"</div>
  <div class="why"><strong>Summary:</strong> Mindstream (Siri/OpenAI, in Trash). Phil Strazzulla SelectSoftware — HR &amp; IT internal requests reduction by 65% (relevant HR ops insight). Medium — Microsoft told engineers to stop using AI (notable). CoolDeep AI — AI news digest (low priority, unsubscribe candidate). Techpresso — AI skills gap newsletter. Huntr Team — job search "You're Hired" messaging. 1% Better — general improvement newsletter.</div>
  <div class="action">📌 Recommended Action: Read Medium and Phil Strazzulla articles. Consider unsubscribing from CoolDeep AI and 1% Better if inbox is cluttered. Huntr = useful for job search.</div>
</div>

<!-- PROMOTIONAL / RETAIL -->
<div class="card gray">
  <h3>⚫ Promotional / Retail — 11 Emails</h3>
  <div class="meta">Senders: Ulta Beauty · Shoe Station · Old Navy · Halara · Amazon · Chewy · Popsugar · AI with Mariah · OmniSignal · SHRM Membership (Trash) · Solitaire Clash</div>
  <div class="why"><strong>Summary:</strong> Ulta order ready (actionable — check order status). Chewy flea &amp; tick 20% off (Stella — consider before vet visit). Amazon order placed (LOMON Womens Fashion). Shoe Station/Old Navy/Halara — retail sales (low priority). Popsugar serum ad. AI with Mariah 30-Day Challenge (promotional). OmniSignal AI strategy tool pitch. SHRM Membership Bogg Bag promo (Trash). Solitaire Clash (game promo).</div>
  <div class="action">📌 Recommended Action: Check Ulta order status. Consider Chewy offer for Stella's flea prevention. Archive or delete all others.</div>
</div>

<!-- SAFE TO DELETE / IGNORE -->
<div class="card gray">
  <h3>⚫ Safe to Delete / Ignore — 5 Emails</h3>
  <div class="meta">Senders: Classmates.com · LinkedIn (2 people noticed you) · CoinOut · LinkedIn Lindsey (vacation tip)</div>
  <div class="why"><strong>Summary:</strong> Classmates.com profile visit notification (Michele Rosen). LinkedIn "2 people noticed you" (engagement metric, low priority). CoinOut 1,000 bonus coins food journal. LinkedIn Lindsey — away message vacation tip (promotional email disguised as career advice).</div>
  <div class="action">🗑️ Recommended Action: Archive or delete all. No action needed.</div>
</div>

<!-- DAILY BRIEFINGS (SELF-GENERATED) -->
<div class="card gray">
  <h3>⚫ Daily Briefings (Self-Generated) — 2 Emails</h3>
  <div class="meta">Sender: Melissa Daily Briefing &lt;melissaw212@gmail.com&gt;</div>
  <div class="why"><strong>Summary:</strong> Two auto-generated daily briefings from earlier today (14:30 UTC and 14:32 UTC). The 14:32 version is the most recent and was read. The 14:30 version is unread and not in inbox.</div>
  <div class="action">🗑️ Recommended Action: Archive both older briefings. This current briefing supersedes them.</div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     7. TRASH REVIEW
════════════════════════════════════════════════════════════════ -->
<div class="section-title red">🗑️ Trash Review</div>
<div class="note-box">📌 4 emails are currently in Gmail Trash. Review before permanent deletion.</div>

<div class="two-col">
  <div>
    <div class="card yellow">
      <h3>🔄 Restore? — 1 Email</h3>
      <div class="meta">Sender: Hacking HR (Clara Adams) — "Who Owns Ethical AI?"</div>
      <div class="why"><strong>Why review:</strong> This newsletter discusses ethical AI ownership in the workplace — directly relevant to your HR and CHRO career positioning. May have been accidentally trashed.</div>
      <div class="action">💡 Recommendation: Restore if you want to keep up with Hacking HR content. Otherwise leave in trash — content is available on their website.</div>
    </div>
    <div class="card yellow">
      <h3>🔄 Restore? — 1 Email</h3>
      <div class="meta">Sender: Mindstream — "Say goodbye to the old Siri"</div>
      <div class="why"><strong>Why review:</strong> Contains AI industry news (new Siri + "the number that could sink OpenAI"). Relevant if you follow AI trends for professional purposes.</div>
      <div class="action">💡 Recommendation: Restore only if you actively read Mindstream. Otherwise safe to delete — news is widely covered elsewhere.</div>
    </div>
  </div>
  <div>
    <div class="card gray">
      <h3>✅ Safe to Delete — 2 Emails</h3>
      <div class="meta">
        1. SHRM Membership — "The FREE Bogg Bag is a bonus" (code BOGG26)<br>
        2. Acorns — "Auto-earn bonuses with every swipe of your cards!"
      </div>
      <div class="why"><strong>Why safe to delete:</strong> SHRM Membership promo — if you're not renewing now, this offer is not time-critical (and promotional). Acorns credit card link promo — standard marketing, no personal data needed.</div>
      <div class="action">🗑️ Recommendation: Permanently delete both. No value retained.</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════
     8. PROMOTIONAL / RETAIL SUMMARY
════════════════════════════════════════════════════════════════ -->
<div class="section-title gray">🛍️ Promotional / Retail Summary</div>

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
    <tr>
      <td>Ulta Beauty Orders</td>
      <td>1</td>
      <td>"Your order is ready to go 🙌" — Order confirmation/ready for pickup</td>
      <td><strong>Keep / Review</strong> — Check order status and pickup details</td>
    </tr>
    <tr>
      <td>Chewy.com</td>
      <td>1</td>
      <td>Save 20% on flea &amp; tick meds — First pharmacy order discount</td>
      <td><strong>Review</strong> — Relevant ahead of vet appt (Jun 16). Order if Stella needs it.</td>
    </tr>
    <tr>
      <td>Amazon.com</td>
      <td>1</td>
      <td>Order confirmed: "LOMON Womens Fashion 2..." — Fashion item ordered</td>
      <td><strong>Keep</strong> — Order confirmation. Archive after reviewing delivery date.</td>
    </tr>
    <tr>
      <td>Old Navy</td>
      <td>1</td>
      <td>Men's Sale: Snag his faves from $10, $15 &amp; $20</td>
      <td><strong>Delete / Ignore</strong> — Men's sale, not likely relevant</td>
    </tr>
    <tr>
      <td>Shoe Station</td>
      <td>1</td>
      <td>Just For Him: HEYDUDE starting at $39.98</td>
      <td><strong>Delete / Ignore</strong> — Men's footwear promo</td>
    </tr>
    <tr>
      <td>Halara</td>
      <td>1</td>
      <td>Our Most Dynamic Duos: Buy 2 for $59</td>
      <td><strong>Review or Delete</strong> — Activewear deal if interested</td>
    </tr>
    <tr>
      <td>Popsugar Dedicated</td>
      <td>1</td>
      <td>The Serum of the Summer: Danucera D7 (sponsored content)</td>
      <td><strong>Delete / Ignore</strong> — Advertiser content</td>
    </tr>
    <tr>
      <td>AI with Mariah</td>
      <td>1</td>
      <td>🔥 Early Access: 30 Day AI Challenge</td>
      <td><strong>Review</strong> — Could be useful if you want structured AI skill-building</td>
    </tr>
    <tr>
      <td>OmniSignal / CrossLike</td>
      <td>1</td>
      <td>▶️ Watch: OmniSignal Builds Your Strategy in 3 Minutes</td>
      <td><strong>Delete / Ignore</strong> — B2B SaaS pitch, likely not relevant</td>
    </tr>
    <tr>
      <td>SHRM Membership (Trash)</td>
      <td>1</td>
      <td>Free Bogg Bag with SHRM membership (code BOGG26)</td>
      <td><strong>Delete</strong> — Already in Trash. Permanently delete.</td>
    </tr>
    <tr>
      <td>Solitaire Clash</td>
      <td>1</td>
      <td>Win Signed Jerseys &amp; Amazon Gift Cards — Soccer Carnival</td>
      <td><strong>Delete / Ignore</strong> — Mobile game promo</td>
    </tr>
  </tbody>
</table>

<!-- ═══════════════════════════════════════════════════════════════
     9. NEWSLETTERS & SUBSCRIPTIONS
════════════════════════════════════════════════════════════════ -->
<div class="section-title purple">📰 Newsletters &amp; Subscriptions</div>

<table>
  <thead>
    <tr>
      <th>Sender</th>
      <th>Topic</th>
      <th>Recommendation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Hacking HR (Clara Adams) — <em>Trash</em></td>
      <td>Ethical AI ownership in the workplace; AI Hackathon; AI Experience Summit</td>
      <td><strong>Keep / Restore</strong> — Highly relevant to HR career &amp; CHRO positioning</td>
    </tr>
    <tr>
      <td>Mindstream — <em>Trash</em></td>
      <td>New Siri; the number that could sink OpenAI</td>
      <td><strong>Review then Delete</strong> — AI news, easily found elsewhere</td>
    </tr>
    <tr>
      <td>Ariana Ruiz / LinkedIn (Empowered Leadership Exchange)</td>
      <td>Professional visibility &amp; leadership for executives</td>
      <td><strong>Keep &amp; Read</strong> — Relevant to personal brand during job search</td>
    </tr>
    <tr>
      <td>Hebba Youssef (I Hate It Here)</td>
      <td>Employee AI rollout; TikTok &amp; workplace culture</td>
      <td><strong>Keep &amp; Read</strong> — Well-regarded HR newsletter, strong signal content</td>
    </tr>
    <tr>
      <td>Phil Strazzulla / SelectSoftware Reviews</td>
      <td>How HR &amp; IT cut internal requests by up to 65%</td>
      <td><strong>Keep &amp; Read</strong> — Practical HR ops insights</td>
    </tr>
    <tr>
      <td>Medium Daily Digest</td>
      <td>"Microsoft Told Its Engineers to Stop Using AI" — tech news</td>
      <td><strong>Keep &amp; Read</strong> — This specific article is notable and worth reading</td>
    </tr>
    <tr>
      <td>CoolDeep AI</td>
      <td>AI news digest — "Clear, practical, no fluff"</td>
      <td><strong>Unsubscribe</strong> — Duplicative if already reading Mindstream/Techpresso</td>
    </tr>
    <tr>
      <td>Techpresso / AI Academy (Louis)</td>
      <td>AI skills gap; "AI won't replace you. But…"</td>
      <td><strong>Review</strong> — Useful AI career framing. Keep if content is actionable.</td>
    </tr>
    <tr>
      <td>The Huntr Team</td>
      <td>Job search support; free resume reviews; "You're Hired" framing</td>
      <td><strong>Keep</strong> — Relevant to active job search. Check for free resume review offer.</td>
    </tr>
    <tr>
      <td>"1% Better"</td>
      <td>Mythos Unleashed, World Cup Flop, bad-knee fix — general improvement</td>
      <td><strong>Unsubscribe</strong> — Off-topic and low professional value</td>
    </tr>
    <tr>
      <td>Substack (Ken Harbaugh / Meidas Defense)</td>
      <td>Meidas Defense Weekly Update — live political/defense news</td>
      <td><strong>Keep or Unsubscribe</strong> — Personal interest only, not professional</td>
    </tr>
    <tr>
      <td>SmartMoney Minute</td>
      <td>Capital gains mistakes for retirees; take-home pay estimation</td>
      <td><strong>Keep</strong> — Relevant financial literacy content</td>
    </tr>
    <tr>
      <td>LinkedIn Lindsey (McMillionConsulting)</td>
      <td>LinkedIn away message tips — "Ready for vacation?"</td>
      <td><strong>Unsubscribe</strong> — Promotional disguised as career tips</td>
    </tr>
  </tbody>
</table>

<!-- ═══════════════════════════════════════════════════════════════
     10. EMAIL ACCOUNTING
════════════════════════════════════════════════════════════════ -->
<div class="section-title gray">📊 Email Accounting — All 50 Emails Verified</div>

<table>
  <thead>
    <tr>
      <th>Category</th>
      <th style="width:60px;">Count</th>
      <th>Emails Included</th>
      <th>Recommendation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>🔴 Security / Risk (Phishing/Scam)</td>
      <td>2</td>
      <td>"LOWER" RIDGID kit scam; "Lowe's®" Kobalt tool set scam</td>
      <td>Delete immediately / Report as phishing</td>
    </tr>
    <tr>
      <td>🟢 Job Search (Alerts &amp; Automated)</td>
      <td>4</td>
      <td>LinkedIn CPO (Pearl Health); ZenSearch daily matches; HR Search AM Run 1; HR Search AM Run 2</td>
      <td>Review and act on high-fit roles</td>
    </tr>
    <tr>
      <td>🟢 Recruiters / Networking</td>
      <td>5</td>
      <td>Serafeim
