<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Melissa's Executive Briefing — Tuesday, June 9, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrapper { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 16px; padding: 36px 40px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header .subtitle { font-size: 15px; color: #a0b4d0; margin-top: 4px; }
  .header-meta { display: flex; gap: 32px; margin-top: 20px; flex-wrap: wrap; }
  .header-meta-item { background: rgba(255,255,255,0.08); border-radius: 10px; padding: 10px 20px; text-align: center; }
  .header-meta-item .val { font-size: 22px; font-weight: 700; color: #e0eaff; }
  .header-meta-item .lbl { font-size: 11px; color: #8ca3be; text-transform: uppercase; letter-spacing: 0.5px; }
  .prep-badge { display: inline-block; background: #e74c3c; color: #fff; border-radius: 20px; padding: 3px 12px; font-size: 11px; font-weight: 700; margin-left: 10px; vertical-align: middle; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; padding: 10px 18px; border-radius: 10px 10px 0 0; color: #fff; letter-spacing: 0.2px; display: flex; align-items: center; gap: 8px; }
  .section-body { background: #fff; border-radius: 0 0 12px 12px; padding: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.07); }

  /* COLOR THEMES */
  .red-header { background: linear-gradient(90deg, #c0392b, #e74c3c); }
  .yellow-header { background: linear-gradient(90deg, #b8860b, #e6ac00); }
  .blue-header { background: linear-gradient(90deg, #1565c0, #1976d2); }
  .green-header { background: linear-gradient(90deg, #1a6b3a, #27ae60); }
  .purple-header { background: linear-gradient(90deg, #6a0572, #9b59b6); }
  .gray-header { background: linear-gradient(90deg, #555, #888); }
  .navy-header { background: linear-gradient(90deg, #1a1a2e, #16213e); }
  .teal-header { background: linear-gradient(90deg, #006064, #00838f); }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 18px; margin-bottom: 14px; border-left: 5px solid; }
  .card-red { background: #fff5f5; border-left-color: #e74c3c; }
  .card-yellow { background: #fffbef; border-left-color: #e6ac00; }
  .card-blue { background: #f0f6ff; border-left-color: #1976d2; }
  .card-green { background: #f0faf4; border-left-color: #27ae60; }
  .card-purple { background: #faf0ff; border-left-color: #9b59b6; }
  .card-gray { background: #f7f8fa; border-left-color: #aaa; }
  .card-teal { background: #f0fafa; border-left-color: #00838f; }

  .card .card-title { font-weight: 700; font-size: 14px; margin-bottom: 6px; }
  .card .card-meta { font-size: 12px; color: #666; margin-bottom: 8px; }
  .card .card-row { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 4px; }
  .card .card-row strong { min-width: 120px; color: #444; }
  .badge { display: inline-block; border-radius: 12px; padding: 2px 10px; font-size: 11px; font-weight: 700; }
  .badge-red { background: #fde8e8; color: #c0392b; }
  .badge-yellow { background: #fff3cd; color: #856404; }
  .badge-green { background: #d4edda; color: #155724; }
  .badge-blue { background: #d0e8ff; color: #1a5276; }
  .badge-purple { background: #f3e5f5; color: #6a0572; }
  .badge-gray { background: #e9ecef; color: #555; }
  .badge-orange { background: #ffe5cc; color: #7a3800; }

  /* EXEC SUMMARY */
  .exec-bullets { list-style: none; padding: 0; }
  .exec-bullets li { display: flex; gap: 12px; align-items: flex-start; margin-bottom: 14px; padding: 14px 16px; border-radius: 10px; }
  .exec-bullets li .icon { font-size: 22px; flex-shrink: 0; }
  .exec-bullets li .text strong { display: block; font-size: 14px; margin-bottom: 3px; }
  .exec-bullets li .text span { font-size: 13px; color: #555; }
  .bullet-red { background: #fff5f5; border-left: 4px solid #e74c3c; }
  .bullet-green { background: #f0faf4; border-left: 4px solid #27ae60; }
  .bullet-blue { background: #f0f6ff; border-left: 4px solid #1976d2; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #f0f2f5; color: #333; font-weight: 700; padding: 10px 12px; text-align: left; border-bottom: 2px solid #ddd; }
  td { padding: 9px 12px; border-bottom: 1px solid #eee; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #fafbfc; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-title { font-weight: 700; font-size: 14px; color: #1a1a2e; background: #e8edf5; border-radius: 8px; padding: 6px 14px; margin-bottom: 8px; }
  .cal-day-title .today-tag { background: #1976d2; color: #fff; border-radius: 8px; padding: 2px 8px; font-size: 11px; margin-left: 8px; }
  .cal-event { background: #f7f9fc; border-radius: 8px; padding: 12px 16px; margin-bottom: 8px; border-left: 4px solid #1976d2; }
  .cal-event.declined { border-left-color: #e74c3c; opacity: 0.8; }
  .cal-event.needs-action { border-left-color: #e6ac00; }
  .cal-event.confirmed { border-left-color: #27ae60; }
  .cal-event .ce-time { font-weight: 700; font-size: 13px; color: #1976d2; }
  .cal-event .ce-name { font-weight: 700; font-size: 14px; margin: 2px 0; }
  .cal-event .ce-detail { font-size: 12px; color: #555; margin-top: 2px; }
  .conflict-warn { background: #fff3cd; border-radius: 6px; padding: 6px 10px; font-size: 12px; color: #856404; margin-top: 6px; }

  /* EMAIL ACCOUNTING */
  .accounting-total { background: #1a1a2e; color: #fff; border-radius: 8px; padding: 12px 20px; margin-top: 12px; font-size: 15px; font-weight: 700; text-align: center; }

  /* DASHBOARD */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; }
  .dash-tile { border-radius: 12px; padding: 16px 18px; text-align: center; }
  .dash-tile .dt-val { font-size: 32px; font-weight: 800; }
  .dash-tile .dt-lbl { font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px; }
  .dt-red { background: #fde8e8; color: #c0392b; }
  .dt-yellow { background: #fff9e6; color: #856404; }
  .dt-green { background: #d4edda; color: #155724; }
  .dt-blue { background: #d0e8ff; color: #1a5276; }
  .dt-purple { background: #f3e5f5; color: #6a0572; }
  .dt-gray { background: #e9ecef; color: #444; }

  /* PRIORITIES */
  .priority-block { display: flex; gap: 14px; align-items: flex-start; background: #f7f9fc; border-radius: 12px; padding: 16px 18px; margin-bottom: 12px; }
  .priority-num { background: #1a1a2e; color: #fff; border-radius: 50%; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; font-size: 18px; font-weight: 800; flex-shrink: 0; }
  .priority-text strong { display: block; font-size: 15px; margin-bottom: 4px; }
  .priority-text span { font-size: 13px; color: #555; }

  /* MISC */
  .divider { border: none; border-top: 1px solid #e5e9f0; margin: 16px 0; }
  .note { background: #fffbef; border-radius: 8px; padding: 10px 14px; font-size: 12px; color: #7a5c00; margin-top: 10px; }
  .security-alert { background: #fff0f0; border: 1px solid #e74c3c; border-radius: 8px; padding: 12px 16px; margin-bottom: 10px; }
  a { color: #1976d2; text-decoration: none; }
  a:hover { text-decoration: underline; }
  .tag { display: inline-block; background: #e8edf5; color: #333; border-radius: 6px; padding: 1px 7px; font-size: 11px; margin-right: 4px; }

  @media (max-width: 600px) {
    .header-meta { gap: 12px; }
    .header { padding: 24px 18px; }
    .section-body { padding: 14px; }
  }
</style>
</head>
<body>
<div class="page-wrapper">

<!-- ===== HEADER ===== -->
<div class="header">
  <div style="display:flex; align-items:center; gap:14px; flex-wrap:wrap;">
    <div>
      <h1>☀️ Good Morning, Melissa</h1>
      <div class="subtitle">Executive Briefing &nbsp;·&nbsp; Tuesday, June 9, 2026 &nbsp;·&nbsp; Prepared by your Executive Chief of Staff</div>
    </div>
  </div>
  <div class="header-meta">
    <div class="header-meta-item"><div class="val">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="header-meta-item"><div class="val">7</div><div class="lbl">Calendar Events</div></div>
    <div class="header-meta-item"><div class="val">3</div><div class="lbl">Action Required</div></div>
    <div class="header-meta-item"><div class="val">1</div><div class="lbl">Today's Meeting</div></div>
    <div class="header-meta-item"><div class="val">2</div><div class="lbl">Security Flags</div></div>
  </div>
</div>

<!-- ===== EXECUTIVE SUMMARY ===== -->
<div class="section">
  <div class="section-title red-header">⚡ Executive Summary</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li class="bullet-red">
        <div class="icon">🚨</div>
        <div class="text">
          <strong>Biggest Risk: Two Security / Spam Threats in Your Inbox</strong>
          <span>A phishing email impersonating "Cloud Monitoring Alerts" landed in your account (not inbox, not trash — flagged in limbo). A casino spam email with a suspicious domain is also lurking outside your inbox. Neither has been trashed. Immediate action needed — do not click any links.</span>
        </div>
      </li>
      <li class="bullet-green">
        <div class="icon">💼</div>
        <div class="text">
          <strong>Biggest Opportunity: LinkedIn HR Director Alert — Up to $350K/yr</strong>
          <span>A LinkedIn job alert surfaced a Human Resources Director role at a confidential company paying up to $350K/year. Your Adderall refill has been confirmed by Emily Ridge at Spectrum Neuroscience, so you're clear on that front. RSVP needed for two upcoming HR Networking Zoom sessions (June 10 & June 11).</span>
        </div>
      </li>
      <li class="bullet-blue">
        <div class="icon">📅</div>
        <div class="text">
          <strong>Biggest Calendar Item: Zoom Consultation with Netta Jenkins — TODAY at 12:00 PM</strong>
          <span>Your 15-minute Zoom consultation with Netta Jenkins (HIC Consult) is happening today at noon EDT. It's accepted. Drinks with Meg (Oakleaf Partnership) tomorrow at 1 PM still shows location as TBC — confirm venue. Hair appointment at Elle at UMI Salon on June 15 is confirmed.</span>
        </div>
      </li>
    </ul>
  </div>
</div>

<!-- ===== ACTION REQUIRED ===== -->
<div class="section">
  <div class="section-title yellow-header">⚠️ Action Required</div>
  <div class="section-body">

    <div class="card card-red">
      <div class="card-title">🚨 SECURITY THREAT — Phishing Email: "Your Cloud Data May Have Been Exposed"</div>
      <div class="card-meta">From: Cloud Monitoring Alerts &lt;mtfrktokpqgkjw.71368643574109@250r5t.wby2q1.tacckt.us&gt; · Tue, Jun 9</div>
      <div class="card-row"><strong>Why It Matters:</strong> <span>Highly suspicious sender domain. Subject line uses fear tactics ("Urgent: Cloud Data Leak Detected"). Classic phishing format. Email is <em>not in inbox, not in trash</em> — it exists in a gray zone. Do NOT click any links.</span></div>
      <div class="card-row"><strong>Next Step:</strong> <span>Delete immediately. Mark as phishing/spam in Gmail. Do not click any links or reply.</span></div>
      <div class="card-row"><strong>Due:</strong> <span><strong>Today</strong></span></div>
    </div>

    <div class="card card-red">
      <div class="card-title">🎰 SECURITY THREAT — Spam/Scam: "Claim Your 50 Free Spins Now! No Deposit Needed!"</div>
      <div class="card-meta">From: welcome_bonus 🎁 &lt;jnsupportbrc@cmxiqpfnpyyohzjkpvjcfcak.com&gt; · Tue, Jun 9, 9:01 AM</div>
      <div class="card-row"><strong>Why It Matters:</strong> <span>Classic gambling scam — suspicious random domain, not in inbox or trash, sitting in limbo. Potential malware vector.</span></div>
      <div class="card-row"><strong>Next Step:</strong> <span>Delete immediately. Report as spam. Do not engage.</span></div>
      <div class="card-row"><strong>Due:</strong> <span><strong>Today</strong></span></div>
    </div>

    <div class="card card-yellow">
      <div class="card-title">✅ Medical Confirmed — Adderall Refill: Reply from Emily Ridge</div>
      <div class="card-meta">From: Emily Ridge &lt;emilysachs@spectrumneuroscience.org&gt; · Tue, Jun 9, 9:28 AM</div>
      <div class="card-row"><strong>Why It Matters:</strong> <span>Emily replied "Done" to your refill request — your prescription has been sent. Confirm pharmacy received it and check pickup timing.</span></div>
      <div class="card-row"><strong>Next Step:</strong> <span>Call or check your pharmacy to confirm receipt and schedule pickup.</span></div>
      <div class="card-row"><strong>Due:</strong> <span>Today or tomorrow</span></div>
    </div>

    <div class="card card-yellow">
      <div class="card-title">📅 RSVP Needed — HR Networking & Job Search Group Zoom (Jun 10 & Jun 11)</div>
      <div class="card-meta">From: Calendar · Jun 10 12–1:30 PM & Jun 11 12–1 PM</div>
      <div class="card-row"><strong>Why It Matters:</strong> <span>Both HR Networking Zoom events show status "needsAction" — you have not RSVP'd. These are key job-search networking sessions with 170+ attendees.</span></div>
      <div class="card-row"><strong>Next Step:</strong> <span>Accept or decline both calendar invites today.</span></div>
      <div class="card-row"><strong>Due:</strong> <span>Before Jun 10, 12 PM</span></div>
    </div>

    <div class="card card-blue">
      <div class="card-title">📍 Confirm Venue — Melissa x Meg Drinks (Jun 10, 1 PM)</div>
      <div class="card-meta">With: Meg Park, Oakleaf Partnership &lt;megpark@oakleafpartnership.com&gt;</div>
      <div class="card-row"><strong>Why It Matters:</strong> <span>Location is listed as "TBC." Meeting is tomorrow — you need a confirmed spot.</span></div>
      <div class="card-row"><strong>Next Step:</strong> <span>Email or text Meg today to confirm location.</span></div>
      <div class="card-row"><strong>Due:</strong> <span>Today</span></div>
    </div>

    <div class="card card-green">
      <div class="card-title">💼 Review — HR Director Role Up to $350K (LinkedIn Job Alert)</div>
      <div class="card-meta">From: LinkedIn Job Alerts &lt;jobalerts-noreply@linkedin.com&gt; · Tue, Jun 9, 11:05 AM</div>
      <div class="card-row"><strong>Why It Matters:</strong> <span>High-value opportunity — HR Director at a confidential company, range $20K–$350K/yr. Your profile likely triggered this match.</span></div>
      <div class="card-row"><strong>Next Step:</strong> <span>Open LinkedIn Job Alerts email and review the posting. Apply or save.</span></div>
      <div class="card-row"><strong>Due:</strong> <span>This week</span></div>
    </div>

  </div>
</div>

<!-- ===== FULL 7-DAY CALENDAR ===== -->
<div class="section">
  <div class="section-title blue-header">📅 Full 7-Day Calendar (Jun 9–15, 2026)</div>
  <div class="section-body">

    <!-- TODAY: TUE JUN 9 -->
    <div class="cal-day">
      <div class="cal-day-title">Tuesday, June 9, 2026 <span class="today-tag">TODAY</span></div>

      <div class="cal-event confirmed">
        <div class="ce-time">12:00 PM – 12:15 PM</div>
        <div class="ce-name">Melissa & Netta Jenkins — 15-Min Consultation</div>
        <div class="ce-detail">📍 <a href="https://us06web.zoom.us/j/5224221004?pwd=UU5YNmlFckpjQnlzc2FDMHFlNUhhUT09&omn=81785592238" target="_blank">Zoom Link</a> &nbsp;|&nbsp; Password: 424726</div>
        <div class="ce-detail">👤 Attendee: netta@hicconsult.com</div>
        <div class="ce-detail">✅ Status: <span class="badge badge-green">Accepted</span></div>
        <div class="ce-detail">📝 Prep: Review what you want to discuss with HIC Consult. Have your resume/LinkedIn ready. 15 minutes — be crisp and direct.</div>
      </div>
    </div>

    <!-- WED JUN 10 -->
    <div class="cal-day">
      <div class="cal-day-title">Wednesday, June 10, 2026</div>

      <div class="cal-event needs-action">
        <div class="ce-time">12:00 PM – 1:30 PM</div>
        <div class="ce-name">HR Networking & Job Search Group — Zoom Session 2</div>
        <div class="ce-detail">📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a></div>
        <div class="ce-detail">👥 Large group session — 170+ attendees</div>
        <div class="ce-detail">⚠️ Status: <span class="badge badge-yellow">RSVP Needed</span></div>
        <div class="ce-detail">📝 Prep: Review HR Networking Team Guidelines (linked in calendar description). Prepare your elevator pitch. Have job targets ready.</div>
        <div class="conflict-warn">⚠️ CONFLICT: Overlaps with "Melissa x Meg Drinks" (1:00–2:00 PM). The networking session ends at 1:30 PM and drinks start at 1:00 PM — 30-minute overlap. Coordinate timing.</div>
      </div>

      <div class="cal-event confirmed">
        <div class="ce-time">12:00 PM – 1:30 PM</div>
        <div class="ce-name">Network (Personal Block)</div>
        <div class="ce-detail">📍 No location specified</div>
        <div class="ce-detail">✅ Status: <span class="badge badge-green">Confirmed</span></div>
        <div class="ce-detail">📝 This appears to be a personal reminder block coinciding with the HR Networking session. May be redundant — consider removing.</div>
      </div>

      <div class="cal-event confirmed">
        <div class="ce-time">1:00 PM – 2:00 PM</div>
        <div class="ce-name">Melissa x Meg Drinks</div>
        <div class="ce-detail">📍 Location: TBC — <strong>confirm today</strong></div>
        <div class="ce-detail">👤 Meg Park — megpark@oakleafpartnership.com (Oakleaf Partnership)</div>
        <div class="ce-detail">✅ Status: <span class="badge badge-green">Accepted</span></div>
        <div class="ce-detail">📝 Prep: Research Oakleaf Partnership. Prepare talking points for conversation — is this a networking/recruiting meeting? Confirm location ASAP.</div>
        <div class="conflict-warn">⚠️ CONFLICT: HR Networking Zoom ends at 1:30 PM. Drinks with Meg begin at 1:00 PM. You'll need to leave the Zoom 30 minutes early or reschedule one of these.</div>
      </div>
    </div>

    <!-- THU JUN 11 -->
    <div class="cal-day">
      <div class="cal-day-title">Thursday, June 11, 2026</div>

      <div class="cal-event declined">
        <div class="ce-time">9:00 AM – 10:30 AM</div>
        <div class="ce-name">Executive Roundtable (John Madigan)</div>
        <div class="ce-detail">📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> &nbsp;|&nbsp; PW: 205454</div>
        <div class="ce-detail">❌ Status: <span class="badge badge-red">Declined</span></div>
        <div class="ce-detail">📝 You declined this event. If this was intentional, no action needed. If it was a mistake, reconsider — "Executive Roundtable" may be a valuable networking opportunity.</div>
      </div>

      <div class="cal-event needs-action">
        <div class="ce-time">12:00 PM – 1:00 PM</div>
        <div class="ce-name">HR Networking & Job Search: Open Office Hours — Zoom 2</div>
        <div class="ce-detail">📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a></div>
        <div class="ce-detail">👥 Large group — same attendees as Jun 10 session</div>
        <div class="ce-detail">⚠️ Status: <span class="badge badge-yellow">RSVP Needed</span></div>
        <div class="ce-detail">📝 Open office hours format. Note in description: <em>please turn off automated AI notetaking tools.</em> Good for 1:1 connection and visibility in the network.</div>
      </div>
    </div>

    <!-- FRI JUN 12 — SUN JUN 14 -->
    <div class="cal-day">
      <div class="cal-day-title">Friday, June 12 – Sunday, June 14, 2026</div>
      <div class="cal-event" style="border-left-color:#aaa; background:#fafafa;">
        <div class="ce-time">All Day</div>
        <div class="ce-name">No Events Scheduled</div>
        <div class="ce-detail">Use this window for job applications, follow-ups, and interview prep.</div>
      </div>
    </div>

    <!-- MON JUN 15 -->
    <div class="cal-day">
      <div class="cal-day-title">Monday, June 15, 2026</div>

      <div class="cal-event confirmed">
        <div class="ce-time">9:30 AM – 11:00 AM</div>
        <div class="ce-name">Hair Appointment — Elle at UMI Salon</div>
        <div class="ce-detail">📍 37 West 20th Street, Suite 1107, New York, NY 10011</div>
        <div class="ce-detail">💇 Service: Single Process with Blowout (with Elle M)</div>
        <div class="ce-detail">✅ Status: <span class="badge badge-green">Confirmed</span></div>
        <div class="ce-detail">📝 Manage/modify at: <a href="https://elleatumi.glossgenius.com/a/f2ab675761428d8ce73a61087c11ef34fd0c" target="_blank">GlossGenius Link</a> | Allow 90 minutes. Plan commute from home.</div>
      </div>
    </div>

  </div>
</div>

<!-- ===== JOB SEARCH & INTERVIEW PIPELINE ===== -->
<div class="section">
  <div class="section-title green-header">💼 Job Search & Interview Pipeline</div>
  <div class="section-body">

    <table>
      <thead>
        <tr>
          <th>Source</th>
          <th>Opportunity / Signal</th>
          <th>Fit</th>
          <th>Status</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>LinkedIn Job Alerts</strong></td>
          <td>Human Resources Director at Confidential Company — up to $350K/yr</td>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>Unread alert</td>
          <td>Review & apply immediately</td>
        </tr>
        <tr>
          <td><strong>LinkedIn (Job Alerts)</strong></td>
          <td>Lead People Business Partner roles similar to Braze position</td>
          <td><span class="badge badge-blue">MEDIUM</span></td>
          <td>Unread</td>
          <td>Review job matches, save or apply</td>
        </tr>
        <tr>
          <td><strong>Calendar — Netta Jenkins</strong></td>
          <td>15-min consultation with HIC Consult (TODAY 12 PM)</td>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>Accepted / Today</td>
          <td>Attend Zoom — have goals/questions ready</td>
        </tr>
        <tr>
          <td><strong>Calendar — Meg Park</strong></td>
          <td>Drinks with Meg (Oakleaf Partnership) — Jun 10, 1 PM</td>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>Accepted / Location TBC</td>
          <td>Confirm venue today; research Oakleaf Partnership</td>
        </tr>
        <tr>
          <td><strong>Calendar — HR Networking Zoom</strong></td>
          <td>HR Networking & Job Search Group — Jun 10 (12 PM) & Jun 11 (12 PM)</td>
          <td><span class="badge badge-blue">MEDIUM</span></td>
          <td>No RSVP</td>
          <td>RSVP both sessions; prepare elevator pitch</td>
        </tr>
        <tr>
          <td><strong>Calendar — Executive Roundtable</strong></td>
          <td>Executive Roundtable (John Madigan) — Jun 11, 9 AM</td>
          <td><span class="badge badge-blue">MEDIUM</span></td>
          <td>Declined</td>
          <td>Reconsider if relevant to executive network</td>
        </tr>
        <tr>
          <td><strong>Sago (Focus Group)</strong></td>
          <td>$75 paid research study on "Delicious Meals" — Jun 18–19</td>
          <td><span class="badge badge-gray">LOW</span></td>
          <td>Invite received</td>
          <td>Optional — complete pre-screening if interested</td>
        </tr>
      </tbody>
    </table>

    <div class="note">💡 Key Insight: You have active networking this week via Netta Jenkins, Meg Park, and two HR Zoom sessions. Prioritize the $350K HR Director role immediately — high comp and matches your background.</div>

  </div>
</div>

<!-- ===== FULL EMAIL REVIEW BY CATEGORY ===== -->
<div class="section">
  <div class="section-title navy-header">📬 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="card card-red">
      <div class="card-title">🔴 Security / Risk &nbsp;<span class="badge badge-red">2 Emails</span></div>
      <div class="card-meta">Senders: "Cloud Monitoring Alerts" (phishing domain) · "welcome_bonus🎁" (casino scam domain)</div>
      <div class="card-row"><strong>Summary:</strong><span>Two dangerous emails — one phishing impersonating cloud security alerts, one casino gambling spam scam. Neither is in inbox or trash (gray zone). Both use manipulative subject lines.</span></div>
      <div class="card-row"><strong>Action:</strong><span><strong>Delete both immediately. Report as phishing. Do not click any links.</strong></span></div>
    </div>

    <!-- JOB SEARCH -->
    <div class="card card-green">
      <div class="card-title">🟢 Job Search &nbsp;<span class="badge badge-green">2 Emails</span></div>
      <div class="card-meta">Senders: LinkedIn Job Alerts (HR Director, up to $350K) · LinkedIn (Lead People Business Partner roles similar to Braze)</div>
      <div class="card-row"><strong>Summary:</strong><span>Two LinkedIn job alert emails — one high-value HR Director role at a confidential company (up to $350K), one batch of similar roles to Lead PBP at Braze.</span></div>
      <div class="card-row"><strong>Action:</strong><span>Review both alerts. Apply to HR Director role promptly. Save relevant Braze-similar roles for pipeline tracking.</span></div>
    </div>

    <!-- RECRUITERS / NETWORKING -->
    <div class="card card-teal">
      <div class="card-title">🔵 Recruiters / Networking &nbsp;<span class="badge badge-blue">3 Emails</span></div>
      <div class="card-meta">Senders: James Ellison (Executive Branding, Beehiiv) · HR Leaders Events (Wellbeing benefits webinar) · Sago (Focus group, $75 study Jun 18–19)</div>
      <div class="card-row"><strong>Summary:</strong><span>James Ellison's email (executive branding/visibility) is likely a marketing email but touches on professional positioning. HR Leaders Events is a webinar invite re: wellbeing gaps. Sago is a paid research study opportunity ($75).</span></div>
      <div class="card-row"><strong>Action:</strong><span>Scan James Ellison's email for relevance. Review HR Leaders Events invite for professional value. Decide on Sago study pre-screening before Jun 18.</span></div>
    </div>

    <!-- CALENDAR / EVENTS -->
    <div class="card card-blue">
      <div class="card-title">🔵 Calendar / Events &nbsp;<span class="badge badge-blue">2 Emails</span></div>
      <div class="card-meta">Senders: Slack (Getting Started guide) · Brya Team (Outdoor Concert in Central Park, Tue Jun 9, 7:30 PM)</div>
      <div class="card-row"><strong>Summary:</strong><span>Slack guide for team onboarding to free Pro trial — relevant if you're actively using Slack. Brya event: free outdoor concert at Naumburg Bandshell, Central Park — TODAY at 7:30 PM (fun personal option).</span></div>
      <div class="card-row"><strong>Action:</strong><span>Review Slack guide. Decide if Central Park concert interests you tonight.</span></div>
    </div>

    <!-- MEDICAL / HEALTH -->
    <div class="card card-yellow">
      <div class="card-title">🟡 Medical / Health &nbsp;<span class="badge badge-yellow">2 Emails</span></div>
      <div class="card-meta">Senders: Emily Ridge, Spectrum Neuroscience (Adderall refill confirmed) · USA Service Dog Registration (ESA letter expiration)</div>
      <div class="card-row"><strong>Summary:</strong><span>Emily Ridge confirmed Adderall refill with "Done." Separately, USA Service Dog Registration is alerting about ESA letter expiration (letters valid 1 year; landlords checking).</span></div>
      <div class="card-row"><strong>Action:</strong><span>Confirm pharmacy pickup for Adderall. Review ESA letter date — if relevant to your housing situation, renew promptly.</span></div>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="card card-yellow">
      <div class="card-title">🟡 Financial / Billing &nbsp;<span class="badge badge-yellow">3 Emails</span></div>
      <div class="card-meta">Senders: Robinhood (IRA contribution complete) · Robinhood (Transfer completed, $5.00 to Roth IRA from bank ****7471) · SmartAsset Headlines (How to Teach Kids About Money — in Trash)</div>
      <div class="card-row"><strong>Summary:</strong><span>Two Robinhood confirmation emails: $5.00 transfer completed + Roth IRA contribution marked complete. SmartAsset newsletter (in Trash) — low priority personal finance content.</span></div>
      <div class="card-row"><strong>Action:</strong><span>No urgent action — Robinhood transactions confirmed. SmartAsset: already trashed, safe to permanently delete.</span></div>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="card card-purple">
      <div class="card-title">🟣 Professional Development &nbsp;<span class="badge badge-purple">5 Emails</span></div>
      <div class="card-meta">Senders: Jeff Su (How I'd Learn AI From Scratch — Trash) · The HR Takeaways × 3 (Future Ready Hiring — Trash) · CoolDeep AI (AI vs Your Job — Inbox) · PromptMates × 2 (Managing AI Costs — Trash)</div>
      <div class="card-row"><strong>Summary:</strong><span>Multiple AI/HR professional development newsletters. The HR Takeaways sent 3 duplicates (all trashed). Jeff Su (Trash), PromptMates × 2 (Trash), CoolDeep AI (Inbox). Topics: AI learning, HR hiring trends, AI cost management.</span></div>
      <div class="card-row"><strong>Action:</strong><span>CoolDeep AI — read if time allows. Trashed duplicates: permanently delete. Consider unsubscribing from duplicate senders to reduce noise.</span></div>
    </div>

    <!-- PERSONAL -->
    <div class="card card-gray">
      <div class="card-title">⚪ Personal &nbsp;<span class="badge badge-gray">5 Emails</span></div>
      <div class="card-meta">Senders: Match.com (Al likes you) · The Average Joe (Apple WWDC / Profits) · The Daily Skimm (Willy Wonka food pyramid) · MeidasTouch (6/9/26 podcast) · Melissa Daily Briefing (Previous briefing sent at 1:13 PM UTC)</div>
      <div class="card-row"><strong>Summary:</strong><span>Match.com like notification. Personal news/podcast subscriptions. Previous daily briefing from your own account.</span></div>
      <div class="card-row"><strong>Action:</strong><span>Match.com — check if interested. Previous briefing: archive or delete. Others: read at leisure or unsubscribe.</span></div>
    </div>

    <!-- NEWSLETTERS / SUBSCRIPTIONS -->
    <div class="card card-purple">
      <div class="card-title">🟣 Newsletters / Subscriptions &nbsp;<span class="badge badge-purple">8 Emails</span></div>
      <div class="card-meta">Senders: The Hustle (Trash) · Christopher Rainey via LinkedIn (Future of Learning) · the co-lab (AI Job Search, Substack) · Medium Daily Digest (Claude Code open-source) · TradeAlgo Daily Bulletin (Chip stocks — Trash) · "1% Better" (Siri's Makeover — Trash) · Glassdoor (Market Pay Report: Software Engineer) · USPS Informed Delivery (0 mail, 0 packages)</div>
      <div class="card-row"><strong>Summary:</strong><span>Mix of business/tech/HR newsletters. Some trashed. USPS: 0 deliveries today. Glassdoor pay report is for Software Engineer (may be misdirected). LinkedIn learning podcast and co-lab AI job search content are relevant.</span></div>
      <div class="card-row"><strong>Action:</strong><span>Read co-lab (AI job search) and LinkedIn (Future of Learning) when relevant. USPS: no action. Glassdoor: verify this is the right report for you. Trashed newsletters: permanently delete.</span></div>
    </div>

    <!-- PROMOTIONAL / RETAIL -->
    <div class="card card-gray">
      <div class="card-title">⚪ Promotional / Retail &nbsp;<span class="badge badge-gray">18 Emails</span></div>
      <div class="card-meta">Senders: Shoe Station (Trash) · INNBEAUTY Project · Amazon Business (Trash) · 1-800 Contacts · Laura Geller ×2 · Mystery Deal · Olivia Gamber (Trash) · Macy's (Trash) · Halara · TJ Maxx (Trash) · Paul Labrecque Salon (Trash) · Kulfi Beauty (Trash) · Bed Bath & Beyond (Trash) · Target Optical · Zappos · Amazon Business (Trash)</div>
      <div class="card-row"><strong>Summary:</strong><span>Large volume of retail/beauty/fashion promotional emails. Most already trashed. Active inbox promos include INNBEAUTY, 1-800 Contacts, Laura Geller (×2 duplicate), Mystery Deal, and Halara.</span></div>
      <div class="card-row"><strong>Action:</strong><span>Review 1-800 Contacts if you need contacts. Permanently delete trashed promos. Unsubscribe from repeated senders to reduce volume.</span></div>
    </div>

  </div>
</div>

<!-- ===== TRASH REVIEW ===== -->
<div class="section">
  <div class="section-title red-header">🗑️ Trash Review</div>
  <div class="section-body">

    <p style="margin-bottom:14px; font-size:13px; color:#555;">The following <strong>15 emails</strong> are currently in your Gmail Trash. Review before permanent deletion.</p>

    <!-- RESTORE -->
    <div class="card card-yellow">
      <div class="card-title">♻️ Restore Immediately — 0 Emails</div>
      <div class="card-row"><span>No trash emails appear to require restoration. All trashed items appear intentional or low-value.</span></div>
    </div>

    <!-- REVIEW BEFORE DELETING -->
    <div class="card card-yellow">
      <div class="card-title">🔍 Review Before Deleting — 3 Emails</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Reason to Review</th></tr></thead>
        <tbody>
          <tr>
            <td>TradeAlgo Daily Bulletin</td>
            <td>Chip stocks lead the bounce</td>
            <td>Market update re: AI/chip stocks bounce — may be useful if tracking investments or market trends</td>
          </tr>
          <tr>
            <td>The HR Takeaways ×3 (duplicates)</td>
            <td>Future Ready Hiring, Fair Relocation, and Compliance Gaps To Watch</td>
            <td>Sent 3 times (duplicates at :36, :42, :43 sec). Only one needs review; the other two are exact duplicates. Uber cut 23% of HR division headline is notable for HR professionals.</td>
          </tr>
          <tr>
            <td>SmartAsset Headlines</td>
            <td>How to Teach Kids About Money</td>
            <td>Personal finance content — scan if relevant to your situation, otherwise delete</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- SAFE TO DELETE -->
    <div class="card card-gray">
      <div class="card-title">✅ Safe to Permanently Delete — 12 Emails</div>
      <table style="margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Reason</th></tr></thead>
        <tbody>
          <tr><td>Shoe Station</td><td>Ends Today: Skechers starting at $49.98</td><td>Retail promo, expired offer, no value</td></tr>
          <tr><td>Amazon Business</td><td>Prime business savings start here</td><td>Generic promotional email</td></tr>
          <tr><td>Jeff Su</td><td>How I'd Learn AI From Scratch in 2026</td><td>Marketing newsletter, low personal priority</td></tr>
          <tr><td>Olivia Gamber</td><td>She was crawling and clawing her way back</td><td>Motivational marketing email, no actionable content</td></tr>
          <tr><td>PromptMates ×2</td><td>You're Managing AI Costs Wrong</td><td>Duplicate emails, newsletter marketing</td></tr>
          <tr><td>Macy's</td><td>Starts now: 30% off our best brands + 15% off beauty</td><td>Retail promo</td></tr>
          <tr><td>TJ Maxx</td><td>SANDALS you want from $29.99</td><td>Retail promo</td></tr>
          <tr><td>Paul Labrecque Salon</td><td>Shop By Skin Type</td><td>Retail/beauty promo</td></tr>
          <tr><td>Kulfi Beauty</td><td>Your summer lip, sorted 💋</td><td>Beauty promo</td></tr>
          <tr><td>Bed Bath & Beyond</td><td>The Beyond Big Savings Event starts NOW</td><td>Retail promo</td></tr>
          <tr><td>The Hustle</td><td>🌿 Answering nature's call</td><td>Newsletter — already trashed, safe to permanently delete</td></tr>
          <tr><td>1% Better</td><td>Siri's Makeover, SpaceX's War Biz…</td><td>Newsletter — already trashed, low priority</td></tr>
        </tbody>
      </table>
    </div>

  </div>
</div>

<!-- ===== PROMOTIONAL / RETAIL SUMMARY ===== -->
<div class="section">
  <div class="section-title gray-header">🛍️ Promotional / Retail Summary</div>
  <div class="section-body">

    <table>
      <thead>
        <tr><th>Sender / Brand</th><th>Count</th><th>Subject / Theme</th><th>Location</th><th>Recommendation</th></tr>
      </thead>
      <tbody>
        <tr><td>Shoe Station</td><td>1</td><td>Skechers from $49.98, Nike 30% off</td><td>Trash</td><td><span class="badge badge-red">Delete</span></td></tr>
        <tr><td>INNBEAUTY Project</td><td>1</td><td>Brightening Trio skincare launch</td><td>Inbox</td><td><span class="badge badge-gray">Ignore / Delete</span></td></tr>
        <tr><td>Amazon Business</td><td>1</td><td>Prime Business Savings</td><td>Trash</td><td><span class="badge badge-red">Delete</span></td></tr>
        <tr><td>1-800 Contacts</td><td>1</td><td>Rediscover the better way to get contacts</td><td>Inbox</td><td><span class="badge badge-yellow">Review</span> if contacts needed</td></tr>
        <tr><td>Laura Geller</td><td>2</td><td>Click to Reveal Your Savings (×2 duplicates)</td><td>Inbox</td><td><span class="badge badge-red">Delete</span> — duplicate</td></tr>
        <tr><td>Mystery Deal 🔥</td><td>1</td><td>"Something in Here Is Going to Surprise You"</td><td>Inbox</td><td><span class="badge badge-red">Delete</span> — low credibility sender</td></tr>
        <tr><td>Olivia Gamber</td><td>1</td><td>Motivational/career email</td><td>Trash</td><td><span class="badge badge-red">Delete</span></td></tr>
        <tr><td>Macy's Friends & Family</td><td>1</td><td>30% off best brands + 15% off beauty</td><td>Trash</td><td><span class="badge badge-red">Delete</span></td></tr>
        <tr><td>Halara</td><td>1</td><td>Buy 2 for $69 — activewear</td><td>Not inbox/trash</td><td><span class="badge badge-gray">Ignore / Delete</span></td></tr>
        <tr><td>TJ Maxx</td><td>1</td><td>Sandals from $29.99</td><td>Trash</td><td><span class="badge badge-red">Delete</span></td></tr>
        <tr><td>Paul Labrecque Salon</td><td>1</td><td>Shop By Skin Type</td><td>Trash</td><td><span class="badge badge-red">Delete</span></td></tr>
        <tr><td>Kulfi Beauty</td><td>1</td><td>Summer lip looks</td><td>Trash</td><td><span class="badge badge-red">Delete</span></td></tr>
        <tr><td>Bed Bath & Beyond</td><td>1</td><td>Up to 60% off furniture, rugs, bedding</td><td>Trash</td><td><span class="badge badge-red">Delete</span></td></tr>
        <tr><td>Target Optical</td><td>1</td><td>Buy online & collect in store</td><td>Archive</td><td><span class="badge badge-gray">Ignore</span></td></tr>
        <tr><td>Zappos</td><td>1</td><td>Father's Day gift — Cole Haan shoes</td><td>Archive</td><td><span class="badge badge-gray">Ignore</span></td></tr>
        <tr style="background:#f0f8ff;"><td><strong>TOTALS</strong></td><td><strong>16</strong></td><td colspan="2"></td><td>Most safe to delete</td></tr>
      </tbody>
    </table>
    <div class="note">💡 Tip: Consider using Gmail's unsubscribe feature or a service like Unroll.me to batch-unsubscribe from retail senders. You received 16+ promotional emails today alone.</div>

  </div>
</div>

<!-- ===== NEWSLETTERS & SUBSCRIPTIONS ===== -->
<div class="section">
  <div class="section-title purple-header">📰 Newsletters & Subscriptions</div>
  <div class="section-body">
    <table>
      <thead>
        <tr><th>Sender</th><th>Topic</th><th>Location</th><th>Recommendation</th></tr>
      </thead>
      <tbody>
        <tr><td>The HR Takeaways ×3</td><td>HR news: Uber cutting HR division, future hiring, compliance</td><td>Trash (3 duplicates)</td><td><span class="badge badge-red">Unsubscribe</span> — duplicate sends are a problem</td></tr>
        <tr><td>Jeff Su</td><td>AI learning from scratch in 2026</td><td>Trash</td><td><span class="badge badge-red">Unsubscribe</span></td></tr>
        <tr><td>PromptMates ×2</td><td>AI cost management, HR tech framework</td><td>Trash (2 duplicates)</td><td><span class="badge badge-red">Unsubscribe</span> — duplicate sends</td></tr>
        <tr><td>CoolDeep AI</td><td>AI vs jobs — workforce displacement</td><td>Inbox</td><td><span class="badge badge-yellow">Review</span> — HR-relevant content</td></tr>
        <tr><td>TradeAlgo Daily Bulletin</td><td>Chip stocks / AI market bounce</td><td>Trash</td><td><span class="badge badge-gray">Keep or Delete</span> — if tracking markets</td></tr>
        <tr><td>The Hustle</td><td>Business/tech news — Amazon pizza, brainrot Monopoly</td><td>Trash</td><td><span class="badge badge-red">Unsubscribe</span> if not reading</td></tr>
        <tr><td>Christopher Rainey via LinkedIn</td><td>Future of Learning at Work</td><td>Archive</td><td><span class="badge badge-green">Keep</span> — HR/L&D professional value</td></tr>
        <tr><td>the co-lab (Substack)</td><td>AI job search tools, community, layoff navigation</td><td>Archive</td><td><span class="badge badge-green">Keep</span> — directly relevant to your search</td></tr>
        <tr><td>Medium Daily Digest</td><td>Claude Code open-source projects, AI tools</td><td>Archive</td><td><span class="badge badge-yellow">Review</span> — AI-adjacent, skim when time permits</td></tr>
        <tr><td>1% Better</td><td>Siri, SpaceX, Stoic morning routines</td><td>Trash</td><td><span class="badge badge-gray">Delete</span></td></tr>
        <tr><td>Glassdoor</td><td>Market Pay Report — Software Engineer</td><td>Archive</td><td><span class="badge badge-gray">Ignore</span> — likely wrong role match</td></tr>
        <tr><td>USPS Informed Delivery</td><td>Daily digest — 0 mail, 0 packages today</td><td>Archive</td><td><span class="badge badge-green">Keep</span> — useful daily utility</td></tr>
        <tr><td>The Average Joe</td><td>Apple WWDC report card / market profits</td><td>Archive</td><td><span class="badge badge-yellow">Review</span> at leisure</td></tr>
        <tr><td>The Daily Skimm</td><td>General news — cowboy boot summer, Willy Wonka</td><td>Archive</td><td><span class="badge badge-yellow">Review</span> at leisure or unsubscribe if not reading</td></tr>
        <tr><td>MeidasTouch (Substack)</td><td>Political podcast — ad-free 73 min episode</td><td>Archive</td><td><span class="badge badge-yellow">Keep</span> if listening; archive otherwise</td></tr>
        <tr><td>SmartAsset Headlines</td><td>Teaching kids about money</td><td>Trash</td><td><span class="badge badge-red">Delete</span></td></tr>
        <tr><td>HR Leaders Events</td><td>Wellbeing benefits — gaps for 1 in 5 employees</td><td>Archive</td><td><span class="badge badge-green">Keep</span> — HR professional relevance</td></tr>
        <tr><td>James Ellison (Exec Branding)</td><td>"The room you are not in" — executive visibility</td><td>Inbox</td><td><span class="badge badge-yellow">Review</span> — possibly relevant to your job search</td></tr>
        <tr><td>Melissa Daily Briefing (self)</td><td>Previous executive briefing from this morning</td><td>Inbox</td><td><span class="badge badge-gray">Archive</span> — superseded by this briefing</td></tr>
        <tr><td>Slack (Getting Started)</td><td>Slack Pro free trial setup guide</td><td>Inbox</td><td><span class="badge badge-yellow">Review</span> — if using Slack for networking/job search</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ===== EMAIL ACCOUNTING ===== -->
<div class="section">
  <div class="section-title navy-header">📊 Email Accounting — Full Count Verification</div>
  <div class="section-body">

    <table>
      <thead>
        <tr><th>Category</th><th>Count</th><th>Summary</th><th>Recommendation</th></tr>
      </thead>
      <tbody>
        <tr style="background:#fff5f5;"><td>🔴 Security / Risk</td><td style="font-weight:700;">2</td><td>Phishing (Cloud Monitoring Alerts) + Casino scam (welcome_bonus)</td><td>Delete immediately, report as phishing</td></tr>
        <tr style="background:#f0faf4;"><td>🟢 Job Search (LinkedIn Alerts)</td><td style="font-weight:700;">2</td><td>HR Director $350K alert + Lead PBP similar-to-Braze batch</td><td>Review and apply</td></tr>
        <tr style="background:#f0fafa;"><td>🔵 Recruiters / Networking</td><td style="font-weight:700;">3</td><td>James Ellison (exec branding) + HR Leaders Events + Sago focus group</td><td>Review; Sago opt-in if interested</td></tr>
        <tr style="background:#f0f6ff;"><td>🔵 Calendar / Events</td><td style="font-weight:700;">2</td><td>Slack getting started + Brya (Central Park concert)</td><td>Review Slack; optional event tonight</td></tr>
        <tr style="background:#fffbef;"><td>🟡 Medical / Health</td><td style="font-weight:700;">2</td><td>Emily Ridge Adderall refill confirmed + ESA letter expiration notice</td><td>Confirm pharmacy; check ESA letter</td></tr>
        <tr style="background:#fffbef;"><td>🟡 Financial / Billing</td><td style="font-weight:700;">3</td><td>Robinhood IRA contribution ×2 + SmartAsset (Trash)</td><td>No urgent action; delete SmartAsset</td></tr>
        <tr style="background:#faf0ff;"><td>🟣 Professional Development</td><td style="font-weight:700;">5</td><td>Jeff Su (Trash) + HR Takeaways ×3 (Trash) + CoolDeep AI + PromptMates ×2 (Trash)</td><td>Read CoolDeep AI; delete rest</td></tr>
        <tr style="background:#f7f8fa;"><td>⚪ Personal</td><td style="font-weight:700;">5</td><td>Match.com + Average Joe + Daily Skimm + MeidasTouch + Melissa Daily Briefing (self)</td><td>Archive; read at leisure</td></tr>
        <tr style="background:#faf0ff;"><td>🟣 Newsletters / Subscriptions</td><td style="font-weight:700;">8</td><td>The Hustle (Trash), Christopher Rainey LinkedIn, co-lab Substack, Medium, TradeAlgo (Trash), 1% Better (Trash), Glassdoor, USPS Informed Delivery</td><td>Keep relevant; unsubscribe noisy ones</td></tr>
        <tr style="background:#f7f8fa;"><td>⚪ Promotional / Retail</td><td style="font-weight:700;">16</td><td>Shoe Station (T), INNBEAUTY, Amazon Biz (T), 1-800
