html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa W — Sunday, August 30, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }

  .page-wrapper { max-width: 1200px; margin: 0 auto; padding: 20px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); color: white; border-radius: 16px; padding: 32px 40px; margin-bottom: 24px; box-shadow: 0 8px 32px rgba(0,0,0,0.3); }
  .header h1 { font-size: 28px; font-weight: 300; letter-spacing: 1px; margin-bottom: 6px; }
  .header h1 span { font-weight: 700; color: #e94560; }
  .header .date { font-size: 16px; color: #a8b2d8; margin-bottom: 16px; }
  .header-stats { display: flex; gap: 24px; flex-wrap: wrap; }
  .stat-pill { background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); border-radius: 20px; padding: 6px 18px; font-size: 13px; color: #e0e6ff; }
  .stat-pill strong { color: white; }

  /* SECTION HEADERS */
  .section { margin-bottom: 28px; }
  .section-header { display: flex; align-items: center; gap: 10px; margin-bottom: 14px; padding-bottom: 8px; border-bottom: 2px solid #e0e6ff; }
  .section-header h2 { font-size: 18px; font-weight: 700; color: #1a1a2e; }
  .section-icon { font-size: 20px; }
  .section-number { background: #1a1a2e; color: white; border-radius: 50%; width: 28px; height: 28px; display: inline-flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; flex-shrink: 0; }

  /* CARDS */
  .card { background: white; border-radius: 12px; padding: 18px 22px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); border-left: 5px solid #ccc; }
  .card.red { border-left-color: #e94560; background: #fff8f8; }
  .card.yellow { border-left-color: #f0a500; background: #fffdf0; }
  .card.blue { border-left-color: #0078d4; background: #f0f7ff; }
  .card.green { border-left-color: #107c10; background: #f0fff0; }
  .card.purple { border-left-color: #7b2d8b; background: #fdf0ff; }
  .card.gray { border-left-color: #888; background: #f8f8f8; }
  .card.orange { border-left-color: #e07000; background: #fff8f0; }

  .card-title { font-size: 15px; font-weight: 700; margin-bottom: 4px; }
  .card-sub { font-size: 12px; color: #666; margin-bottom: 8px; }
  .card-body { font-size: 13px; color: #333; }
  .card-row { display: flex; gap: 8px; margin-top: 6px; flex-wrap: wrap; }
  .tag { display: inline-block; border-radius: 10px; padding: 2px 10px; font-size: 11px; font-weight: 600; }
  .tag.red { background: #fce4ec; color: #b71c1c; }
  .tag.yellow { background: #fff9c4; color: #856404; }
  .tag.green { background: #e8f5e9; color: #1b5e20; }
  .tag.blue { background: #e3f2fd; color: #0d47a1; }
  .tag.purple { background: #f3e5f5; color: #4a148c; }
  .tag.gray { background: #f0f0f0; color: #444; }
  .tag.orange { background: #fff3e0; color: #bf360c; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
  th { background: #1a1a2e; color: white; padding: 10px 14px; font-size: 12px; text-align: left; font-weight: 600; letter-spacing: 0.5px; }
  td { padding: 9px 14px; font-size: 13px; border-bottom: 1px solid #f0f0f0; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #fafbfc; }
  tr:hover td { background: #f0f7ff; }

  /* STATUS BADGES */
  .badge { display: inline-block; border-radius: 6px; padding: 2px 8px; font-size: 11px; font-weight: 700; }
  .badge.rescued { background: #e8f5e9; color: #1b5e20; }
  .badge.inbox { background: #e3f2fd; color: #0d47a1; }
  .badge.trashed { background: #fce4ec; color: #b71c1c; }
  .badge.auto { background: #f3e5f5; color: #4a148c; }
  .badge.high { background: #fce4ec; color: #b71c1c; }
  .badge.medium { background: #fff9c4; color: #856404; }
  .badge.low { background: #f0f0f0; color: #555; }
  .badge.accepted { background: #e8f5e9; color: #1b5e20; }
  .badge.declined { background: #fce4ec; color: #b71c1c; }
  .badge.needs { background: #fff9c4; color: #856404; }
  .badge.confirmed { background: #e8f5e9; color: #1b5e20; }

  /* EXECUTIVE SUMMARY */
  .exec-summary { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-bottom: 8px; }
  .exec-bullet { border-radius: 12px; padding: 18px 20px; color: white; }
  .exec-bullet.risk { background: linear-gradient(135deg, #c62828, #e94560); }
  .exec-bullet.opp { background: linear-gradient(135deg, #1b5e20, #2e7d32); }
  .exec-bullet.cal { background: linear-gradient(135deg, #0d47a1, #1565c0); }
  .exec-bullet h3 { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; opacity: 0.85; margin-bottom: 8px; }
  .exec-bullet p { font-size: 13px; line-height: 1.5; }

  /* CALENDAR */
  .cal-day { background: white; border-radius: 12px; margin-bottom: 14px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
  .cal-day-header { background: linear-gradient(90deg, #0f3460, #0078d4); color: white; padding: 10px 18px; font-size: 14px; font-weight: 700; }
  .cal-event { padding: 14px 18px; border-bottom: 1px solid #f0f0f0; }
  .cal-event:last-child { border-bottom: none; }
  .cal-event-title { font-weight: 700; font-size: 14px; margin-bottom: 4px; }
  .cal-event-meta { display: flex; gap: 10px; flex-wrap: wrap; font-size: 12px; color: #555; margin-bottom: 6px; }
  .cal-event-meta span { display: flex; align-items: center; gap: 4px; }
  .cal-note { font-size: 12px; background: #fff9c4; border-radius: 6px; padding: 5px 10px; color: #856404; display: inline-block; margin-top: 4px; }
  .cal-conflict { font-size: 12px; background: #fce4ec; border-radius: 6px; padding: 5px 10px; color: #b71c1c; display: inline-block; margin-top: 4px; margin-left: 6px; }

  /* DASHBOARD */
  .dashboard-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }
  .dash-card { background: white; border-radius: 12px; padding: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); text-align: center; }
  .dash-card .dash-num { font-size: 32px; font-weight: 800; line-height: 1.1; }
  .dash-card .dash-label { font-size: 12px; color: #666; margin-top: 4px; }
  .dash-card.red .dash-num { color: #e94560; }
  .dash-card.yellow .dash-num { color: #f0a500; }
  .dash-card.green .dash-num { color: #107c10; }
  .dash-card.blue .dash-num { color: #0078d4; }
  .dash-card.purple .dash-num { color: #7b2d8b; }
  .dash-card.gray .dash-num { color: #666; }

  /* TRIAGE TABLE */
  .triage-status { white-space: nowrap; }
  .triage-from { max-width: 180px; }
  .triage-subject { max-width: 260px; }
  .triage-summary { }

  /* PRIORITY TOP 3 */
  .priority-list { display: flex; flex-direction: column; gap: 12px; }
  .priority-item { display: flex; align-items: flex-start; gap: 14px; background: white; border-radius: 12px; padding: 16px 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
  .priority-num { font-size: 28px; font-weight: 900; min-width: 36px; }
  .priority-num.p1 { color: #e94560; }
  .priority-num.p2 { color: #f0a500; }
  .priority-num.p3 { color: #0078d4; }
  .priority-text h3 { font-size: 15px; font-weight: 700; margin-bottom: 4px; }
  .priority-text p { font-size: 13px; color: #444; }

  /* FOOTER */
  .footer { text-align: center; color: #999; font-size: 12px; padding: 20px; margin-top: 10px; }

  /* ACCOUNTING TABLE */
  .accounting-total td { background: #1a1a2e !important; color: white; font-weight: 700; }

  /* RESPONSIVE */
  @media (max-width: 900px) {
    .exec-summary { grid-template-columns: 1fr; }
    .dashboard-grid { grid-template-columns: repeat(2, 1fr); }
    .header-stats { flex-direction: column; gap: 8px; }
  }
  @media (max-width: 600px) {
    .dashboard-grid { grid-template-columns: repeat(2, 1fr); }
    .page-wrapper { padding: 10px; }
    .header { padding: 20px; }
  }

  .divider { border: none; border-top: 2px solid #e0e6ff; margin: 30px 0; }
  .rescued-note { background: #e8f5e9; border-radius: 6px; padding: 4px 10px; font-size: 11px; color: #1b5e20; display: inline-block; margin-top: 4px; }
  .auto-trash-note { background: #f3e5f5; border-radius: 6px; padding: 4px 10px; font-size: 11px; color: #4a148c; display: inline-block; margin-top: 4px; }
  .phishing-note { background: #fce4ec; border-radius: 6px; padding: 4px 10px; font-size: 11px; color: #b71c1c; display: inline-block; margin-top: 4px; }
</style>
</head>
<body>
<div class="page-wrapper">

<!-- ═══════════════════════════════════════════════════════════
     SECTION 0: EMAIL TRIAGE QUICK LIST
════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-number">0</span>
    <span class="section-icon">⚡</span>
    <h2>Email Triage Quick List</h2>
  </div>
  <table>
    <thead>
      <tr>
        <th class="triage-status">Status</th>
        <th class="triage-from">From</th>
        <th class="triage-subject">Subject</th>
        <th class="triage-summary">Summary / Note</th>
      </tr>
    </thead>
    <tbody>
      <!-- RESCUED EMAILS FIRST -->
      <tr>
        <td><span class="badge rescued">✅ RESCUED</span></td>
        <td>Melissa W (self)</td>
        <td>"Tell Ellie" — Prep questions for Rita</td>
        <td>Personal reminder: prep questions for Rita on Thursday. Rescued from Trash. <span class="rescued-note">🗂 Rescued from Trash — important reminder</span></td>
      </tr>
      <tr>
        <td><span class="badge rescued">✅ RESCUED</span></td>
        <td>Melissa W (self)</td>
        <td>"Tell Ellie" — Call the dentist Monday</td>
        <td>Personal reminder: call the dentist Monday. Rescued from Trash. <span class="rescued-note">🗂 Rescued from Trash — appointment-related</span></td>
      </tr>
      <tr>
        <td><span class="badge rescued">✅ RESCUED</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>Director, People Business Partners at FloQast and 9 more</td>
        <td>Job alert — protected sender, rescued from Trash automatically. <span class="rescued-note">🗂 Rescued from Trash — protected sender</span></td>
      </tr>

      <!-- INBOX EMAILS -->
      <tr>
        <td><span class="badge inbox">📥 INBOX</span></td>
        <td>Settlement Administrator (Epiq)</td>
        <td>Biddle v. Walt Disney Company — Class Action Reminder</td>
        <td>If you subscribed to YouTube TV or DirecTV Stream (Apr 2019–Mar 2026), you may be owed cash. Deadline likely approaching.</td>
      </tr>
      <tr>
        <td><span class="badge inbox">📥 INBOX</span></td>
        <td>Amazon.com</td>
        <td>Shipped: 1 Kitchen Tools item</td>
        <td>Order shipped — track delivery.</td>
      </tr>
      <tr>
        <td><span class="badge inbox">📥 INBOX</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>Human Resources Business Partner Senior Director at Ladders and 39 more</td>
        <td>Top alert: $227K–$341K/yr. 40 jobs. High priority review.</td>
      </tr>
      <tr>
        <td><span class="badge inbox">📥 INBOX</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>Head of People – U.S. at Elliptic and 4 more</td>
        <td>Head of People role at Elliptic (blockchain analytics). Review for fit.</td>
      </tr>
      <tr>
        <td><span class="badge inbox">📥 INBOX</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>Director, People Business Partners at FloQast and 39 more</td>
        <td>Director-level HRBP role. 40 listings total. High volume alert.</td>
      </tr>
      <tr>
        <td><span class="badge inbox">📥 INBOX</span></td>
        <td>HomeAgain PetRescuers</td>
        <td>Lee, a lost Cat, is missing — Ref. HAP-1947148</td>
        <td>Lost cat near Huron St & Manhattan Ave, Brooklyn NY 11222. Community alert.</td>
      </tr>
      <tr>
        <td><span class="badge inbox">📥 INBOX</span></td>
        <td>Match</td>
        <td>Thomas likes you. See if it's mutual.</td>
        <td>Match.com — Thomas liked your profile.</td>
      </tr>
      <tr>
        <td><span class="badge inbox">📥 INBOX</span></td>
        <td>Match</td>
        <td>Frank likes you. See if it's mutual.</td>
        <td>Match.com — Frank liked your profile.</td>
      </tr>
      <tr>
        <td><span class="badge inbox">📥 INBOX</span></td>
        <td>Match</td>
        <td>You've had a profile view from Bill (66, New York)</td>
        <td>Match.com — Bill viewed your profile.</td>
      </tr>
      <tr>
        <td><span class="badge inbox">📥 INBOX</span></td>
        <td>OkCupid</td>
        <td>You have an Intro!</td>
        <td>Someone sent you a message on OkCupid.</td>
      </tr>
      <tr>
        <td><span class="badge inbox">📥 INBOX</span></td>
        <td>Old Navy</td>
        <td>$16 & under pants, jeans & skirts + 50% off $100+ orders</td>
        <td>Promotional sale — Encore Members get free shipping on $50+.</td>
      </tr>
      <tr>
        <td><span class="badge inbox">📥 INBOX</span></td>
        <td>The Hustle</td>
        <td>🌶️ Chili's is back, baby</td>
        <td>Newsletter — weekly business digest.</td>
      </tr>

      <!-- TRASH SUMMARY ROWS -->
      <tr style="background:#fce4ec;">
        <td><span class="badge auto">🗑 AUTO-TRASHED</span></td>
        <td colspan="2"><strong>3 emails auto-trashed (phishing + newsletter)</strong> — Medium Daily Digest (newsletter_trashed), + 2 phishing "Payment Declined" clones</td>
        <td>See Trash Review / Security sections for details.</td>
      </tr>
      <tr style="background:#f8f8f8;">
        <td><span class="badge trashed">🗂 TRASH</span></td>
        <td colspan="2"><strong>34 additional emails in Trash</strong> — spam, casino scams, retail promos, newsletters, job digests, social digests, duplicate Substack</td>
        <td>See Trash Review for Restore / Review / Delete breakdown.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 1: HEADER
════════════════════════════════════════════════════════════ -->
<div class="header">
  <h1>Good morning, <span>Melissa</span> 👋</h1>
  <div class="date">Sunday, August 30, 2026 · Executive Briefing prepared by your Chief of Staff</div>
  <div class="header-stats">
    <div class="stat-pill">📧 <strong>50</strong> Emails Reviewed</div>
    <div class="stat-pill">📅 <strong>5</strong> Calendar Events</div>
    <div class="stat-pill">🔴 <strong>2</strong> Security Threats Intercepted</div>
    <div class="stat-pill">💼 <strong>8</strong> Job Alerts</div>
    <div class="stat-pill">📅 <strong>3</strong> Meetings This Week</div>
    <div class="stat-pill">✅ <strong>3</strong> Items Rescued from Trash</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 2: EXECUTIVE SUMMARY
════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-number">2</span>
    <span class="section-icon">📋</span>
    <h2>Executive Summary</h2>
  </div>
  <div class="exec-summary">
    <div class="exec-bullet risk">
      <h3>🔴 Biggest Risk</h3>
      <p>Two confirmed phishing emails impersonating "Payment Declined" cloud storage alerts were auto-intercepted and trashed before reaching you. Additionally, multiple casino scam emails and spam are in your inbox area — <strong>do not click any links</strong>. Your email address (melissaw212) appears on spam lists.</p>
    </div>
    <div class="exec-bullet opp">
      <h3>🟢 Biggest Opportunity</h3>
      <p>LinkedIn Job Alerts are showing <strong>Senior Director HRBP at $227K–$341K/yr</strong> plus 39 more roles, Head of People at Elliptic, Director HRBP at FloQast, and VP Talent Acquisition — a strong pipeline of senior HR/People leadership roles aligned to your profile.</p>
    </div>
    <div class="exec-bullet cal">
      <h3>🔵 Biggest Calendar Item</h3>
      <p>Your <strong>coaching session with Rita Ramakrishnan is Thursday Sept 3 at 10:00 AM</strong> — you've accepted. You have a self-note rescued from Trash reminding you to <strong>prep questions for Rita on Thursday</strong>. RSVP still needed for two HR Networking Zoom sessions on Sept 2 and Sept 3.</p>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 3: ACTION REQUIRED
════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-number">3</span>
    <span class="section-icon">⚠️</span>
    <h2>Action Required</h2>
  </div>

  <div class="card red">
    <div class="card-title">🔴 SECURITY — Phishing Attempts Intercepted</div>
    <div class="card-sub">Source: Auto-Trashed Emails × 2 | Priority: IMMEDIATE AWARENESS</div>
    <div class="card-body">Two "Payment Declined" phishing emails impersonating cloud storage services were automatically quarantined. Your username (melissaw212) is being actively targeted. Your real email is also appearing in casino spam and GLP-1 weight loss spam — your address is on purchased lists.</div>
    <div class="card-row">
      <span class="tag red">⚡ Urgent</span>
      <span class="tag red">Do Not Click</span>
    </div>
    <div class="card-body" style="margin-top:8px;"><strong>Recommended:</strong> No action needed on the auto-trashed items — they are safely removed. Consider enabling Google Advanced Protection and reviewing what services have your email address.</div>
  </div>

  <div class="card yellow">
    <div class="card-title">🟡 CLASS ACTION SETTLEMENT — Biddle v. Walt Disney (YouTube TV / DirecTV Stream)</div>
    <div class="card-sub">Source: Settlement Administrator &lt;OnlineTVSettlement@e.epiqnotice.com&gt; | Received: Sat Aug 29</div>
    <div class="card-body">If you purchased YouTube TV or DirecTV Stream from April 1, 2019 – March 31, 2026, you may be entitled to a cash payment. This is a legitimate class action reminder from Epiq — a major settlement administrator.</div>
    <div class="card-row"><span class="tag yellow">⏰ Deadline Likely Approaching</span></div>
    <div class="card-body" style="margin-top:8px;"><strong>Recommended:</strong> Open email, verify claim deadline, and file if eligible. Do this today or tomorrow.</div>
  </div>

  <div class="card yellow">
    <div class="card-title">🟡 PERSONAL REMINDER — Call the Dentist Monday</div>
    <div class="card-sub">Source: Self-email (rescued from Trash) | Sent: Sat Aug 29</div>
    <div class="card-body">You sent yourself a note: "Call the dentist Monday." Tomorrow is Monday, August 31 — action needed first thing in the morning.</div>
    <div class="card-row"><span class="tag yellow">⏰ Due: Tomorrow, Mon Aug 31</span></div>
    <div class="card-body" style="margin-top:8px;"><strong>Recommended:</strong> Call dentist Monday morning.</div>
  </div>

  <div class="card blue">
    <div class="card-title">🔵 CALENDAR RSVP — HR Networking & Job Search Group Zoom (Wed Sept 2)</div>
    <div class="card-sub">Source: Calendar | Status: Needs Action | 12:00–1:30 PM ET</div>
    <div class="card-body">You have two overlapping calendar entries for Wed Sept 2 at 12–1:30 PM: the HR Networking Group Zoom (200+ attendees, awaiting RSVP) and a personal "Network" block (confirmed). RSVP to the group Zoom if you plan to attend.</div>
    <div class="card-row"><span class="tag blue">📅 Wed Sept 2</span><span class="tag yellow">RSVP Pending</span></div>
    <div class="card-body" style="margin-top:8px;"><strong>Recommended:</strong> Confirm or decline the group Zoom by Monday.</div>
  </div>

  <div class="card blue">
    <div class="card-title">🔵 CALENDAR RSVP — HR Networking Open Office Hours Zoom (Thurs Sept 3)</div>
    <div class="card-sub">Source: Calendar | Status: Needs Action | 12:00–1:00 PM ET</div>
    <div class="card-body">Open Office Hours Zoom on Thurs Sept 3 at noon — RSVP still pending. Note this is 1.25 hours after your Rita coaching call ends (10:45 AM). No conflict.</div>
    <div class="card-row"><span class="tag blue">📅 Thu Sept 3</span><span class="tag yellow">RSVP Pending</span></div>
    <div class="card-body" style="margin-top:8px;"><strong>Recommended:</strong> Confirm or decline by Monday.</div>
  </div>

  <div class="card blue">
    <div class="card-title">🔵 PREP — Coaching Session with Rita Ramakrishnan (Thurs Sept 3, 10:00 AM)</div>
    <div class="card-sub">Source: Calendar + Rescued Trash Note | Status: Accepted | Google Meet</div>
    <div class="card-body">You accepted a 45-minute coaching call with Rita at rita@iksana.com. You also left yourself a note: "Prep questions for Rita on Thursday." Prep this week before Thursday.</div>
    <div class="card-row"><span class="tag blue">📅 Thu Sept 3 · 10:00–10:45 AM</span><span class="tag green">Accepted</span></div>
    <div class="card-body" style="margin-top:8px;"><strong>Recommended:</strong> Draft your coaching questions by Wednesday evening.</div>
  </div>

  <div class="card green">
    <div class="card-title">🟢 JOB SEARCH — Review High-Value LinkedIn Job Alerts</div>
    <div class="card-sub">Source: LinkedIn Job Alerts × 5 alerts | Received: Today</div>
    <div class="card-body">Multiple senior HR/People leadership alerts received today. Top opportunity: Senior Director HRBP at Ladders ($227K–$341K). Also: Head of People at Elliptic, Director People BPs at FloQast, VP Talent Acquisition at New Story, Head of People at Cape.</div>
    <div class="card-row"><span class="tag green">💼 High Priority</span><span class="tag green">$227K–$341K range</span></div>
    <div class="card-body" style="margin-top:8px;"><strong>Recommended:</strong> Block 2 hours today or tomorrow to review and apply to top matches.</div>
  </div>

  <div class="card green">
    <div class="card-title">🟢 JOB SEARCH — Glassdoor Alerts: Director HR Employee Relations & More</div>
    <div class="card-sub">Source: Glassdoor Jobs (2 emails in Trash) | Received: Today</div>
    <div class="card-body">Glassdoor flagged: Director of HR – Employee Relations at Guild Garage Group (Remote), HR Manager at LIFE Camp, and Medtronic, Teladoc Health, Rippling hiring. These were trashed but rescued for your review.</div>
    <div class="card-row"><span class="tag green">💼 Review</span></div>
    <div class="card-body" style="margin-top:8px;"><strong>Recommended:</strong> Check Glassdoor app for full listings; apply to any matches.</div>
  </div>

  <div class="card yellow">
    <div class="card-title">🟡 AMAZON ORDER — Kitchen Tools Item Shipped</div>
    <div class="card-sub">Source: Amazon.com | Ordered: Sun Aug 30 1:55 AM | Shipped: Sun Aug 30 7:54 AM</div>
    <div class="card-body">You ordered 1 Kitchen Tools item overnight and it has already shipped. Track delivery via Amazon app.</div>
    <div class="card-row"><span class="tag yellow">📦 In Transit</span></div>
    <div class="card-body" style="margin-top:8px;"><strong>Recommended:</strong> Track package — likely arriving Monday or Tuesday.</div>
  </div>
</div>

<hr class="divider">

<!-- ═══════════════════════════════════════════════════════════
     SECTION 4: FULL 7-DAY CALENDAR
════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-number">4</span>
    <span class="section-icon">📅</span>
    <h2>Full 7-Day Calendar</h2>
  </div>

  <div class="cal-day">
    <div class="cal-day-header">☀️ Sunday, August 30, 2026 — Today</div>
    <div class="cal-event">
      <div class="cal-event-title">No calendar events scheduled today.</div>
      <div class="card-body" style="font-size:13px; color:#555;">Use today to review job alerts, prep for the week, draft Rita coaching questions, and respond to calendar RSVPs.</div>
    </div>
  </div>

  <div class="cal-day">
    <div class="cal-day-header">📅 Monday, August 31, 2026</div>
    <div class="cal-event">
      <div class="cal-event-title">No calendar events scheduled.</div>
      <div class="card-body" style="font-size:13px; color:#555;">⚡ Self-reminder: <strong>Call the dentist today.</strong></div>
    </div>
  </div>

  <div class="cal-day">
    <div class="cal-day-header">📅 Tuesday, September 1, 2026</div>
    <div class="cal-event">
      <div class="cal-event-title">No calendar events scheduled.</div>
    </div>
  </div>

  <div class="cal-day">
    <div class="cal-day-header">📅 Wednesday, September 2, 2026</div>

    <div class="cal-event">
      <div class="cal-event-title">🌐 HR Networking & Job Search Group — Zoom Session 2</div>
      <div class="cal-event-meta">
        <span>🕐 12:00 PM – 1:30 PM ET</span>
        <span><span class="badge needs">⏳ Needs RSVP</span></span>
        <span>👥 ~190 attendees</span>
      </div>
      <div class="card-body"><strong>Location:</strong> <a href="https://us06web.zoom.us/j/81954171722" target="_blank" style="color:#0078d4;">Zoom Link</a></div>
      <div class="card-body" style="margin-top:4px;"><strong>Invited by:</strong> HR Networking Group (large professional group, 190+ attendees)</div>
      <span class="cal-note">⚠️ RSVP Pending — Confirm or Decline by Monday</span>
      <span class="cal-conflict">⚡ CONFLICT: Overlaps with personal "Network" block (also 12–1:30 PM, confirmed)</span>
    </div>

    <div class="cal-event">
      <div class="cal-event-title">📌 Network (Personal Block)</div>
      <div class="cal-event-meta">
        <span>🕐 12:00 PM – 1:30 PM ET</span>
        <span><span class="badge confirmed">✅ Confirmed</span></span>
      </div>
      <div class="card-body">Personal networking time block — confirmed. Likely tied to the HR Networking Zoom above.</div>
      <span class="cal-note">This may be a duplicate placeholder for the Zoom above — verify.</span>
    </div>
  </div>

  <div class="cal-day">
    <div class="cal-day-header">📅 Thursday, September 3, 2026</div>

    <div class="cal-event">
      <div class="cal-event-title">🎯 Executive Roundtable — Zoom (John Madigan)</div>
      <div class="cal-event-meta">
        <span>🕐 9:00 AM – 10:30 AM ET</span>
        <span><span class="badge declined">❌ Declined</span></span>
      </div>
      <div class="card-body"><strong>Location:</strong> <a href="https://us02web.zoom.us/j/207786667" target="_blank" style="color:#0078d4;">Zoom Link</a> | Meeting ID: 207 786 667 | Password: 205454</div>
      <div class="card-body" style="margin-top:4px;">Hosted by John Madigan. You have declined this event.</div>
      <span class="cal-note">📌 Already declined — no action needed.</span>
    </div>

    <div class="cal-event">
      <div class="cal-event-title">🧭 Coaching Session: Melissa Weiss & Rita Ramakrishnan</div>
      <div class="cal-event-meta">
        <span>🕐 10:00 AM – 10:45 AM ET</span>
        <span><span class="badge accepted">✅ Accepted</span></span>
        <span>📍 Google Meet</span>
      </div>
      <div class="card-body"><strong>Attendee:</strong> rita@iksana.com | <strong>Type:</strong> 45-minute coaching/consulting session</div>
      <div class="card-body" style="margin-top:4px;"><strong>Prep:</strong> You have a self-note (rescued from Trash): "Prep questions for Rita on Thursday." Draft questions before Wednesday night.</div>
      <span class="cal-note">📝 Prep Due: Wednesday evening · Draft coaching questions now</span>
    </div>

    <div class="cal-event">
      <div class="cal-event-title">🌐 HR Networking & Job Search: Open Office Hours — Zoom 2</div>
      <div class="cal-event-meta">
        <span>🕐 12:00 PM – 1:00 PM ET</span>
        <span><span class="badge needs">⏳ Needs RSVP</span></span>
        <span>👥 ~190 attendees</span>
      </div>
      <div class="card-body"><strong>Location:</strong> <a href="https://us06web.zoom.us/j/85945371140" target="_blank" style="color:#0078d4;">Zoom Link</a></div>
      <div class="card-body" style="margin-top:4px;">Open discussion format — note-taking AI tools are discouraged per organizer. Starts 1 hr 15 min after coaching call ends — no conflict.</div>
      <span class="cal-note">⚠️ RSVP Pending — Confirm or Decline by Monday</span>
    </div>
  </div>

  <div class="cal-day">
    <div class="cal-day-header">📅 Friday, September 4 — Sunday, September 6, 2026</div>
    <div class="cal-event">
      <div class="cal-event-title">No calendar events scheduled (Labor Day Weekend).</div>
      <div class="card-body" style="font-size:13px; color:#555;">Labor Day is Monday, September 7. Plan accordingly for any week-of outreach or follow-ups.</div>
    </div>
  </div>
</div>

<hr class="divider">

<!-- ═══════════════════════════════════════════════════════════
     SECTION 5: JOB SEARCH & INTERVIEW PIPELINE
════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-number">5</span>
    <span class="section-icon">💼</span>
    <h2>Job Search &amp; Interview Pipeline</h2>
  </div>

  <table>
    <thead>
      <tr>
        <th>Fit</th>
        <th>Source</th>
        <th>Role / Company</th>
        <th>Details</th>
        <th>Status / Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="badge high">🔴 HIGH</span></td>
        <td>LinkedIn Job Alert</td>
        <td>Senior Director, HRBP at Ladders (+39 more)</td>
        <td>$227K–$341K/yr salary range. 40 total listings in this alert.</td>
        <td>📥 Inbox — Review &amp; Apply Today</td>
      </tr>
      <tr>
        <td><span class="badge high">🔴 HIGH</span></td>
        <td>LinkedIn Job Alert</td>
        <td>Head of People – U.S. at Elliptic (+4 more)</td>
        <td>Elliptic is leader in blockchain analytics. U.S.-based Head of People role.</td>
        <td>📥 Inbox — Review &amp; Apply</td>
      </tr>
      <tr>
        <td><span class="badge high">🔴 HIGH</span></td>
        <td>LinkedIn Job Alert</td>
        <td>Director, People Business Partners at FloQast (+39 more)</td>
        <td>FloQast: accounting close automation. Sophisticated HRBP profile needed.</td>
        <td>📥 Inbox — Review &amp; Apply</td>
      </tr>
      <tr>
        <td><span class="badge medium">🟡 MED</span></td>
        <td>LinkedIn Job Alert</td>
        <td>Director, People Business Partners at FloQast (+9 more) [2nd alert]</td>
        <td>Duplicate/overlapping alert — same FloQast listing. Cross-reference with above.</td>
        <td>✅ Rescued from Trash — Already in Pipeline</td>
      </tr>
      <tr>
        <td><span class="badge medium">🟡 MED</span></td>
        <td>LinkedIn Job Alert</td>
        <td>VP, Talent Acquisition at New Story (+14 more)</td>
        <td>"Every child has…" — mission-driven org. VP TA role.</td>
        <td>📧 Inbox (read) — Review</td>
      </tr>
      <tr>
        <td><span class="badge medium">🟡 MED</span></td>
        <td>LinkedIn Job Alert</td>
        <td>Head of People at Cape (+4 more)</td>
        <td>Cape: America's privacy-first mobile company. Head of People role.</td>
        <td>📧 Inbox (read) — Review</td>
      </tr>
      <tr>
        <td><span class="badge medium">🟡 MED</span></td>
        <td>Glassdoor Alert</td>
        <td>Director of HR – Employee Relations at Guild Garage Group (+9 Remote jobs)</td>
        <td>Remote US. Also: Medtronic hiring. 10 total listings.</td>
        <td>🗂 Was in Trash — Review on Glassdoor</td>
      </tr>
      <tr>
        <td><span class="badge medium">🟡 MED</span></td>
        <td>Glassdoor Alert</td>
        <td>HR Manager at LIFE Camp, Inc. (+9 NYC jobs) / New jobs Remote US</td>
        <td>NY-based HR Manager role. Also Teladoc Health, Rippling hiring.</td>
        <td>🗂 Was in Trash — Review on Glassdoor</td>
      </tr>
      <tr>
        <td><span class="badge low">⚪ LOW</span></td>
        <td>LinkedIn Newsletter</td>
        <td>Best HR &amp; People Analytics Articles — Aug 2026 (David Green 🇺🇦)</td>
        <td>Professional reading — HR analytics thought leadership. Was auto-trashed.</td>
        <td>🗂 In Trash — Optional Read</td>
      </tr>
      <tr>
        <td><span class="badge low">⚪ LOW</span></td>
        <td>Calendar</td>
        <td>HR Networking &amp; Job Search Group — Zoom (Wed Sept 2)</td>
        <td>Large professional HR networking group. 190+ members. RSVP needed.</td>
        <td>⏳ RSVP PENDING — Confirm by Monday</td>
      </tr>
      <tr>
        <td><span class="badge low">⚪ LOW</span></td>
        <td>Calendar</td>
        <td>HR Networking Open Office Hours — Zoom (Thurs Sept 3)</td>
        <td>Open discussion, no recording. Good for informal job search support.</td>
        <td>⏳ RSVP PENDING — Confirm by Monday</td>
      </tr>
      <tr>
        <td><span class="badge low">⚪ LOW</span></td>
        <td>LinkedIn</td>
        <td>Pedro Miguel Nogueira (Project Manager, Drata) — Connection Request</td>
        <td>LinkedIn connection invite. Was in Trash.</td>
        <td>🗂 In Trash — Optional: Accept or Ignore</td>
      </tr>
    </tbody>
  </table>

  <div class="card blue" style="margin-top:14px;">
    <div class="card-title">📅 Upcoming: Rita Ramakrishnan Coaching Session — Thursday Sept 3, 10:00 AM</div>
    <div class="card-body">Career coaching call accepted. Prep questions this week. Self-note rescued from Trash confirms prep is needed.</div>
  </div>
</div>

<hr class="divider">

<!-- ═══════════════════════════════════════════════════════════
     SECTION 6: FULL EMAIL REVIEW BY CATEGORY
════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-number">6</span>
    <span class="section-icon">📂</span>
    <h2>Full Email Review by Category</h2>
  </div>

  <!-- SECURITY / RISK -->
  <div class="card red">
    <div class="card-title">🔴 Security / Risk — 6 Emails</div>
    <div class="card-sub">Phishing, scams, spam targeting your username</div>
    <table style="margin-top:10px;">
      <thead><tr><th>Status</th><th>From</th><th>Subject</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td><span class="badge auto">Auto-Trashed</span></td>
          <td>Spoofed "Payment_Declined" (random .us domain)</td>
          <td>melissaw212 Your account will be closed within 48 hours if you don't renew</td>
          <td><span class="phishing-note">🛡️ Auto-Trashed — Phishing: spoofed sender, urgent threat, credential harvesting for cloud storage</span></td>
        </tr>
        <tr>
          <td><span class="badge auto">Auto-Trashed</span></td>
          <td>Spoofed "Payment_Declined" (duplicate, random .us domain)</td>
          <td>melissaw212 Your account will be closed within 48 hours if you don't renew [Duplicate]</td>
          <td><span class="phishing-note">🛡️ Auto-Trashed — Phishing: duplicate of above, identical threat language</span></td>
        </tr>
        <tr>
          <td><span class="badge trashed">In Trash</span></td>
          <td>Casino_Special (random .us domain)</td>
          <td>You Won $7000.00 Claim Your Prize Now melissaw212 💰🎁 795279</td>
          <td>Spam/Scam — Delete permanently</td>
        </tr>
        <tr>
          <td><span class="badge trashed">In Trash</span></td>
          <td>"melissaw212" Casino Limitless (random .us domain)</td>
          <td>You Received a Payment of $7,000.00 USD</td>
          <td>Spam/Scam — Delete permanently</td>
        </tr>
        <tr>
          <td><span class="badge trashed">In Trash</span></td>
          <td>"Casino Exclusive" (random .com domain)</td>
          <td>Use Code: 200GETLUCKY + 30 free spins 💰</td>
          <td>Spam/Scam — Delete permanently</td>
        </tr>
        <tr>
          <td><span class="badge trashed">In Trash</span></td>
          <td>Your_Sex_Life (random .us domain)</td>
          <td>Porn Industry Secret for Explosive Stiffys</td>
          <td>Explicit spam — Delete permanently</td>
        </tr>
      </tbody>
    </table>
    <div class="card-body" style="margin-top:10px;"><strong>Recommended:</strong> Auto-trashed items are handled. Permanently delete all casino/spam. Consider enabling Google's Advanced Protection Program for your account.</div>
  </div>

  <!-- JOB SEARCH -->
  <div class="card green">
    <div class="card-title">🟢 Job Search — 10 Emails</div>
    <div class="card-sub">LinkedIn Job Alerts, Glassdoor, Career Networking</div>
    <table style="margin-top:10px;">
      <thead><tr><th>Source</th><th>Role / Alert</th><th>Status</th></tr></thead>
      <tbody>
        <tr><td>LinkedIn Job Alerts</td><td>Senior Director HRBP at Ladders + 39 more ($227K–$341K)</td><td>📥 Inbox — Unread — HIGH PRIORITY</td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>Head of People – U.S. at Elliptic + 4 more</td><td>📥 Inbox — Unread</td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>Director, People Business Partners at FloQast + 39 more</td><td>📥 Inbox — Unread</td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>Director, People Business Partners at FloQast + 9 more</td><td>✅ Rescued from Trash — Protected Sender</td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>VP, Talent Acquisition at New Story + 14 more</td><td>📧 Read — Review</td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>Head of People at Cape + 4 more</td><td>📧 Read — Review</td></tr>
        <tr><td>Glassdoor Jobs</td><td>Director HR – Employee Relations at Guild Garage Group + 9 Remote jobs</td><td>🗂 In Trash — Rescue &amp; Review</td></tr>
        <tr><td>Glassdoor Jobs</td><td>New jobs in Remote, US (Teladoc Health hiring)</td><td>🗂 In Trash — Review</td></tr>
        <tr><td>Glassdoor Jobs</td><td>HR Manager at LIFE Camp + 9 NYC jobs (Rippling hiring)</td><td>🗂 In Trash — Review</td></tr>
        <tr><td>LinkedIn Newsletter</td><td>David Green 🇺🇦 — Best HR &amp; People Analytics Articles Aug 2026</td><td>🗂 Auto-Trashed (Newsletter) — Optional Read</td></tr>
      </tbody>
    </table>
    <div class="card-body" style="margin-top:10px;"><strong>Recommended:</strong> Dedicate 2 hours today or Monday morning to reviewing and applying to top-fit roles. Glassdoor emails in Trash should be reviewed before permanent deletion.</div>
  </div>

  <!-- RECRUITERS / NETWORKING -->
  <div class="card purple">
    <div class="card-title">🟣 Recruiters / Networking — 2 Emails</div>
    <div class="card-sub">LinkedIn connections, professional outreach</div>
    <table style="margin-top:10px;">
      <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>Pedro Miguel Nogueira via LinkedIn</td>
          <td>I want to connect (Project Manager, Drata)</td>
          <td>🗂 In Trash</td>
          <td>Review — Drata is a compliance platform; may be worth connecting depending on your network goals.</td>
        </tr>
        <tr>
          <td>LinkedIn</td>
          <td>Daily Rundown: The new resume must-have; Higher ed's AI upheaval [Duplicate]</td>
          <td>🗂 In Trash</td>
          <td>Delete — Duplicate notification</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- CALENDAR / EVENTS -->
  <div class="card blue">
    <div class="card-title">🔵 Calendar / Events — 0 Separate Emails</div>
    <div class="card-sub">Calendar events covered in Section 4 above. No standalone calendar-related emails outside of calendar data.</div>
  </div>

  <!-- FINANCIAL / BILLING / LEGAL -->
  <div class="card yellow">
    <div class="card-title">🟡 Financial / Billing / Legal — 1 Email</div>
    <div class="card-sub">Class action settlement notice</div>
    <table style="margin-top:10px;">
      <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>Settlement Administrator (Epiq)</td>
          <td>Biddle v. Walt Disney Company — Class Action Reminder (YouTube TV / DirecTV Stream)</td>
          <td>📥 Inbox — Read</td>
          <td>⚡ File claim if eligible — deadline may be imminent</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- AMAZON ORDERS -->
  <div class="card yellow">
    <div class="card-title">🟡 Orders &amp; Deliveries — 3 Emails</div>
    <div class="card-sub">Amazon order confirmation, shipment, reorder prompt</div>
    <table style="margin-top:10px;">
      <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>Amazon.com</td>
          <td>Ordered: 1 Kitchen Tools item</td>
          <td>📧 Read / Sent folder</td>
          <td>Order placed — confirmed</td>
        </tr>
        <tr>
          <td>Amazon.com</td>
          <td>Shipped: 1 Kitchen Tools item</td>
          <td>📥 Inbox — Unread</td>
          <td>📦 Track delivery in Amazon app</td>
        </tr>
        <tr>
          <td>Amazon.com</td>
          <td>Ready to reorder? (Save up to 15% on essentials)</td>
          <td>🗂 In Trash</td>
          <td>Promotional — safely delete</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- PERSONAL -->
  <div class="card orange">
    <div class="card-title">🟠 Personal — 4 Emails</div>
    <div class="card-sub">Self-reminders, dating apps, community notice</div>
    <table style="margin-top:10px;">
      <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>Melissa W (self)</td>
          <td>"Tell Ellie" — Prep questions for Rita on Thursday</td>
          <td>✅ Rescued from Trash</td>
          <td>⚡ Draft coaching questions before Thursday</td>
        </tr>
        <tr>
          <td>Melissa W (self)</td>
          <td>"Tell Ellie" — Call the dentist Monday</td>
          <td>✅ Rescued from Trash</td>
          <td>⚡ Call dentist Monday morning</td>
        </tr>
        <tr>
          <td>Melissa W (self)</td>
          <td>Unique id — "missing my ID for the claim"</td>
          <td>📧 Read / Sent</td>
          <td>Review — may relate to the Disney class action claim. Check if ID was received.</td>
        </tr>
        <tr>
          <td>HomeAgain PetRescuers</td>
          <td>Lee, a lost Cat, near you — Huron St &amp; Manhattan Ave, Brooklyn NY 11222</td>
          <td>📥 Inbox — Unread</td>
          <td>Community alert — share if you've seen Lee</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- DATING -->
  <div class="card orange">
    <div class="card-title">🟠 Personal / Dating Apps — 4 Emails</div>
    <div class="card-sub">Match.com and OkCupid notifications</div>
    <table style="margin-top:10px;">
      <thead><tr><th>From</th><th>Subject</th><th>Status</th></tr></thead>
      <tbody>
        <tr><td>Match</td><td>Thomas likes you. See if it's mutual.</td><td>📥 Inbox — Unread</td></tr>
        <tr><td>Match</td><td>Frank likes you. See if it's mutual.</td><td>📥 Inbox — Unread</td></tr>
        <tr><td>Match</td><td>Bill (66, New York) viewed your profile</td><td>📥 Inbox — Unread</td></tr>
        <tr><td>OkCupid</td><td>You have an Intro!</td><td>📥 Inbox — Unread</td></tr>
      </tbody>
    </table>
    <div class="card-body" style="margin-top:8px;"><strong>Recommended:</strong> Check apps at your leisure.</div>
  </div>

  <!-- OkCupid in Trash -->
  <div class="card gray">
    <div class="card-title">⚫ OkCupid (Trash) — 1 Email</div>
    <table style="margin-top:10px;">
      <thead><tr><th>From</th><th>Subject</th><th>Status</th></tr></thead>
      <tbody>
        <tr><td>OkCupid</td><td>Someone likes you</td><td>🗂 In Trash — Safe to Delete</td></tr>
      </tbody>
    </table>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="card purple">
    <div class="card-title">🟣 Professional Development — 3 Emails</div>
    <div class="card-sub">LinkedIn professional content, Substack newsletters</div>
    <table style="margin-top:10px;">
      <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>LinkedIn (notifications)</td>
          <td>Daily Rundown: The new resume must-have; Higher ed's AI upheaval</td>
          <td>🗂 In Trash (2 copies — duplicate)</td>
          <td>Delete duplicates — read one if interested</td>
        </tr>
        <tr>
          <td>Ruben Hassid (Substack)</td>
          <td>My mother &amp; Claude. (AI/Claude usage story)</td>
          <td>🗂 In Trash (2 identical copies)</td>
          <td>Duplicate — read one, delete both</td>
        </tr>
        <tr>
          <td>Marc Cleroux @ Ten Fold Marc</td>
          <td>Your guide is here</td>
          <td>🗂 In Trash (Read)</td>
          <td>Content guide sent — review if you requested it, otherwise delete</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- MEDICAL / SPAM HEALTH -->
  <div class="card red">
    <div class="card-title">🔴 Medical / Health Spam — 2 Emails</div>
    <div class="card-sub">Unsolicited GLP-1 / weight loss spam targeting your username</div>
    <table style="margin-top:10px;">
      <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>"melissaw212" MED
