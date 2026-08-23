<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa | Sunday, August 23, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }

  .page-header {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    color: white; padding: 32px 40px; border-bottom: 4px solid #e94560;
  }
  .page-header h1 { font-size: 28px; font-weight: 300; letter-spacing: 2px; margin-bottom: 6px; }
  .page-header h2 { font-size: 16px; font-weight: 600; color: #e94560; letter-spacing: 1px; margin-bottom: 16px; }
  .header-meta { display: flex; gap: 32px; flex-wrap: wrap; margin-top: 12px; }
  .header-meta span { font-size: 13px; color: #a0b4c8; }
  .header-meta strong { color: #ffffff; }

  .container { max-width: 1200px; margin: 0 auto; padding: 28px 20px; }

  .section { margin-bottom: 32px; }
  .section-title {
    font-size: 13px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;
    padding: 10px 16px; border-radius: 6px 6px 0 0; display: flex; align-items: center; gap: 8px;
  }
  .section-body { background: #fff; border-radius: 0 0 8px 8px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }

  /* Color themes */
  .theme-red .section-title { background: #c0392b; color: white; }
  .theme-red .section-body { border-left: 4px solid #c0392b; }

  .theme-yellow .section-title { background: #e67e22; color: white; }
  .theme-yellow .section-body { border-left: 4px solid #e67e22; }

  .theme-blue .section-title { background: #2980b9; color: white; }
  .theme-blue .section-body { border-left: 4px solid #2980b9; }

  .theme-green .section-title { background: #27ae60; color: white; }
  .theme-green .section-body { border-left: 4px solid #27ae60; }

  .theme-purple .section-title { background: #8e44ad; color: white; }
  .theme-purple .section-body { border-left: 4px solid #8e44ad; }

  .theme-gray .section-title { background: #7f8c8d; color: white; }
  .theme-gray .section-body { border-left: 4px solid #7f8c8d; }

  .theme-dark .section-title { background: #2c3e50; color: white; }
  .theme-dark .section-body { border-left: 4px solid #2c3e50; }

  .theme-teal .section-title { background: #16a085; color: white; }
  .theme-teal .section-body { border-left: 4px solid #16a085; }

  /* Tables */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #f4f6f8; color: #2c3e50; font-weight: 700; padding: 10px 12px; text-align: left; border-bottom: 2px solid #dee2e6; }
  td { padding: 9px 12px; border-bottom: 1px solid #f0f0f0; vertical-align: top; }
  tr:hover td { background: #fafbfc; }
  tr:last-child td { border-bottom: none; }

  /* Cards */
  .card { border-radius: 8px; padding: 16px 18px; margin-bottom: 14px; border-left: 5px solid #ccc; background: #fff; box-shadow: 0 1px 4px rgba(0,0,0,0.06); }
  .card-red { border-left-color: #c0392b; background: #fff8f7; }
  .card-yellow { border-left-color: #e67e22; background: #fffcf5; }
  .card-blue { border-left-color: #2980b9; background: #f5faff; }
  .card-green { border-left-color: #27ae60; background: #f5fff8; }
  .card-purple { border-left-color: #8e44ad; background: #fdf5ff; }
  .card-gray { border-left-color: #95a5a6; background: #f9f9f9; }
  .card-teal { border-left-color: #16a085; background: #f0fdf9; }

  .card-title { font-size: 14px; font-weight: 700; margin-bottom: 6px; }
  .card-meta { font-size: 12px; color: #666; margin-bottom: 8px; }
  .card-body { font-size: 13px; }
  .card-row { display: flex; gap: 8px; margin-top: 5px; font-size: 12px; }
  .card-label { font-weight: 700; color: #555; min-width: 120px; }

  /* Badges */
  .badge { display: inline-block; padding: 2px 9px; border-radius: 12px; font-size: 11px; font-weight: 700; text-transform: uppercase; }
  .badge-red { background: #fdecea; color: #c0392b; border: 1px solid #f5c6c2; }
  .badge-yellow { background: #fef9ec; color: #e67e22; border: 1px solid #fce4b0; }
  .badge-green { background: #eafaf1; color: #27ae60; border: 1px solid #a9dfbf; }
  .badge-blue { background: #ebf5fb; color: #2980b9; border: 1px solid #aed6f1; }
  .badge-purple { background: #f5eef8; color: #8e44ad; border: 1px solid #d2b4de; }
  .badge-gray { background: #f2f3f4; color: #7f8c8d; border: 1px solid #d5d8dc; }
  .badge-teal { background: #e8f8f5; color: #16a085; border: 1px solid #a2d9ce; }
  .badge-orange { background: #fef5e7; color: #d35400; border: 1px solid #f8c471; }

  /* Exec summary bullets */
  .exec-bullet { display: flex; align-items: flex-start; gap: 12px; margin-bottom: 14px; padding: 14px 16px; border-radius: 8px; }
  .exec-bullet-icon { font-size: 22px; min-width: 32px; }
  .exec-bullet-content strong { display: block; font-size: 14px; margin-bottom: 3px; }
  .exec-bullet-content span { font-size: 13px; color: #555; }
  .exec-red { background: #fef2f2; border: 1px solid #fca5a5; }
  .exec-green { background: #f0fdf4; border: 1px solid #86efac; }
  .exec-blue { background: #eff6ff; border: 1px solid #93c5fd; }

  /* Calendar day */
  .cal-day { margin-bottom: 20px; }
  .cal-day-header { font-size: 13px; font-weight: 700; color: #2980b9; border-bottom: 2px solid #2980b9; padding-bottom: 6px; margin-bottom: 10px; letter-spacing: 1px; text-transform: uppercase; }
  .cal-today .cal-day-header { color: #c0392b; border-bottom-color: #c0392b; }
  .cal-event { display: flex; gap: 12px; padding: 10px 12px; border-radius: 6px; margin-bottom: 8px; font-size: 13px; }
  .cal-event-allday { background: #f0f2f5; border-left: 3px solid #95a5a6; }
  .cal-event-confirmed { background: #f0fdf4; border-left: 3px solid #27ae60; }
  .cal-event-pending { background: #fffcf5; border-left: 3px solid #e67e22; }
  .cal-event-declined { background: #fff8f7; border-left: 3px solid #c0392b; }
  .cal-time { font-weight: 700; min-width: 90px; color: #2c3e50; }
  .cal-info { flex: 1; }
  .cal-name { font-weight: 700; margin-bottom: 2px; }
  .cal-detail { font-size: 12px; color: #666; margin-top: 2px; }
  .cal-conflict { font-size: 11px; font-weight: 700; color: #c0392b; background: #fdecea; border-radius: 4px; padding: 2px 7px; display: inline-block; margin-top: 3px; }
  .cal-prep { font-size: 11px; color: #8e44ad; font-style: italic; margin-top: 2px; }

  /* Priority table */
  .priority-high { color: #c0392b; font-weight: 700; }
  .priority-medium { color: #e67e22; font-weight: 700; }
  .priority-low { color: #27ae60; font-weight: 700; }

  /* Triage table status */
  .status-rescued { color: #27ae60; font-weight: 700; }
  .status-inbox { color: #2980b9; font-weight: 700; }
  .status-trash-auto { color: #c0392b; font-weight: 700; }
  .status-trash-manual { color: #7f8c8d; font-weight: 700; }

  /* Dashboard grid */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; }
  .dash-card { background: #fff; border-radius: 8px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.07); text-align: center; }
  .dash-card .number { font-size: 36px; font-weight: 800; margin: 6px 0; }
  .dash-card .label { font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 1px; }
  .dash-red .number { color: #c0392b; }
  .dash-green .number { color: #27ae60; }
  .dash-blue .number { color: #2980b9; }
  .dash-yellow .number { color: #e67e22; }
  .dash-purple .number { color: #8e44ad; }
  .dash-gray .number { color: #7f8c8d; }

  /* Misc */
  .alert-box { background: #fdecea; border: 1px solid #e74c3c; border-radius: 8px; padding: 14px 16px; margin-bottom: 14px; }
  .alert-box strong { color: #c0392b; }
  .info-box { background: #ebf5fb; border: 1px solid #3498db; border-radius: 8px; padding: 14px 16px; margin-bottom: 14px; }
  .info-box strong { color: #2980b9; }
  .rescued-box { background: #eafaf1; border: 1px solid #27ae60; border-radius: 8px; padding: 10px 14px; margin-bottom: 10px; font-size: 13px; }
  .rescued-box strong { color: #27ae60; }
  .divider { border: none; border-top: 1px solid #e9ecef; margin: 18px 0; }
  .note { font-size: 12px; color: #888; font-style: italic; margin-top: 8px; }
  .tag { display: inline-block; background: #e9ecef; border-radius: 4px; padding: 2px 8px; font-size: 11px; margin: 2px; color: #555; }
  a { color: #2980b9; text-decoration: none; }
  a:hover { text-decoration: underline; }
  .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  @media (max-width: 700px) { .two-col { grid-template-columns: 1fr; } .header-meta { flex-direction: column; gap: 8px; } }
  .group-header { font-size: 13px; font-weight: 700; color: #2c3e50; margin: 14px 0 8px 0; padding-bottom: 4px; border-bottom: 1px solid #dee2e6; }
  .sub-note { font-size: 12px; color: #888; margin-top: 4px; }
  .fit-high { color: #27ae60; font-weight: 700; }
  .fit-medium { color: #e67e22; font-weight: 700; }
  .fit-low { color: #95a5a6; font-weight: 700; }
  .top-priority { display: flex; align-items: flex-start; gap: 14px; padding: 18px; border-radius: 10px; margin-bottom: 14px; }
  .priority-num { font-size: 28px; font-weight: 900; min-width: 36px; }
  .priority-1 { background: linear-gradient(135deg, #fdecea, #fff); border: 2px solid #e74c3c; }
  .priority-1 .priority-num { color: #e74c3c; }
  .priority-2 { background: linear-gradient(135deg, #f0fdf4, #fff); border: 2px solid #27ae60; }
  .priority-2 .priority-num { color: #27ae60; }
  .priority-3 { background: linear-gradient(135deg, #eff6ff, #fff); border: 2px solid #3b82f6; }
  .priority-3 .priority-num { color: #3b82f6; }
</style>
</head>
<body>

<!-- ══════════════════════════════════════════════ PAGE HEADER ══════════════════════════════════════════════ -->
<div class="page-header">
  <h1>Executive Briefing</h1>
  <h2>Good morning, Melissa ☀️</h2>
  <div class="header-meta">
    <span>📅 <strong>Sunday, August 23, 2026</strong></span>
    <span>📧 <strong>50 emails</strong> reviewed</span>
    <span>📆 <strong>13 calendar events</strong> reviewed</span>
    <span>🔒 <strong>10 phishing emails</strong> auto-trashed</span>
    <span>⚠️ <strong>Flash Flood Warning</strong> — Brooklyn, Staten Island, Manhattan</span>
  </div>
</div>

<div class="container">

<!-- ══════════════════════════════════════════════ SECTION 0: EMAIL TRIAGE QUICK LIST ══════════════════════════════════════════════ -->
<div class="section theme-dark">
  <div class="section-title">📋 Section 0 — Email Triage Quick List</div>
  <div class="section-body">
    <table>
      <thead>
        <tr>
          <th style="width:130px">Status</th>
          <th style="width:200px">From</th>
          <th>Subject</th>
          <th>Summary</th>
        </tr>
      </thead>
      <tbody>
        <!-- RESCUED -->
        <tr>
          <td class="status-rescued">✅ RESCUED</td>
          <td>Melissa (self)</td>
          <td>Senior Director, People Business Partners – referred by Rob Demarais</td>
          <td>Job application email Melissa sent to GitLab hiring contact Rich, referencing a referral from Rob Demarais. Rescued from Trash — direct professional correspondence.</td>
        </tr>
        <!-- INBOX -->
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>Notify NYC</td>
          <td>Flash Flood Warning — Brooklyn, Staten Island, Manhattan</td>
          <td>Official city emergency alert issued 08-23-2026 at 6:25 AM. Immediate safety awareness required.</td>
        </tr>
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>Match</td>
          <td>Mark likes you. See if it's mutual.</td>
          <td>Match.com notification — user Mark liked Melissa's profile.</td>
        </tr>
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>Match</td>
          <td>Junior likes you. See if it's mutual.</td>
          <td>Match.com notification — user Junior liked Melissa's profile.</td>
        </tr>
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>Match</td>
          <td>Konstantinos just sent you a new message. 💌</td>
          <td>Match.com notification — new message from Konstantinos awaiting response.</td>
        </tr>
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>Gopalan Arumugam via LinkedIn</td>
          <td>Gopalan just messaged you</td>
          <td>New LinkedIn message from Gopalan Arumugam awaiting response.</td>
        </tr>
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>LinkedIn Customer Support</td>
          <td>LMS Case Created by Virtual Chat Assistant [Case: 260822-012578]</td>
          <td>LinkedIn support case #260822-012578 — Status: Closed. May reply for up to 14 days.</td>
        </tr>
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>Melissa W (self)</td>
          <td>Remote websites</td>
          <td>Melissa emailed herself a LinkedIn link — likely a remote job board resource.</td>
        </tr>
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>Melissa W (self)</td>
          <td>Abacus</td>
          <td>Melissa emailed herself a link to Abacus AI supercomputer — AI tool reference.</td>
        </tr>
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>Melissa W (self)</td>
          <td>(no subject)</td>
          <td>Melissa emailed herself a LinkedIn link — likely a resource or job lead.</td>
        </tr>
        <tr>
          <td class="status-inbox">📥 INBOX</td>
          <td>Melissa W (self)</td>
          <td>Remote job boards</td>
          <td>Melissa emailed herself a LinkedIn link to remote job board resources.</td>
        </tr>
        <!-- TRASH SUMMARY ROWS -->
        <tr style="background:#fff3cd;">
          <td class="status-trash-auto">🗑 AUTO-TRASHED (10)</td>
          <td colspan="3"><strong>10 emails auto-trashed (phishing/scams)</strong> — spoofed SiriusXM, fake cloud storage alerts, fake CashApp payout, adult spam. See <em>Trash Review</em> for full details.</td>
        </tr>
        <tr style="background:#f4f6f8;">
          <td class="status-trash-manual">🗂 TRASH — MANUAL (19)</td>
          <td colspan="3"><strong>19 emails in Trash</strong> — spam, casino, adult content, retail promo, newsletters already discarded. See <em>Trash Review</em> for full details.</td>
        </tr>
      </tbody>
    </table>
    <p class="note">ℹ️ Inbox and rescued emails shown individually. Trashed emails collapsed into summary rows. See Section 7 (Trash Review) for full breakdown.</p>
  </div>
</div>

<!-- ══════════════════════════════════════════════ SECTION 1: HEADER / EXEC SUMMARY ══════════════════════════════════════════════ -->
<div class="section theme-dark">
  <div class="section-title">🗂 Section 1 — Executive Summary</div>
  <div class="section-body">
    <div class="exec-bullet exec-red">
      <div class="exec-bullet-icon">🚨</div>
      <div class="exec-bullet-content">
        <strong>URGENT — Flash Flood Warning + 10 Phishing Emails Auto-Removed</strong>
        <span>NYC issued a Flash Flood Warning this morning for Brooklyn, Staten Island, and Manhattan. Exercise caution if going out today. Separately, 10 phishing/scam emails (spoofed SiriusXM, fake cloud storage alerts, adult spam) were automatically quarantined before reaching your inbox.</span>
      </div>
    </div>
    <div class="exec-bullet exec-green">
      <div class="exec-bullet-icon">💼</div>
      <div class="exec-bullet-content">
        <strong>Job Search — GitLab Application + Recruiter Call Tuesday + Strong LinkedIn Leads</strong>
        <span>Your GitLab Senior Director, People Business Partners application (referred by Rob Demarais) was rescued from Trash — confirm Rich received it. A recruiter call is confirmed for Tuesday 9:30 AM. Two high-fit LinkedIn job alerts arrived: VP People at DomainTools ($175K–$275K) and CHRO via PeopleOps Jobs.</span>
      </div>
    </div>
    <div class="exec-bullet exec-blue">
      <div class="exec-bullet-icon">📅</div>
      <div class="exec-bullet-content">
        <strong>Busy Week Ahead — Hair Monday, Recruiter Tuesday, Networking Wednesday &amp; Thursday</strong>
        <span>Verizon Fios bill due today (Sunday). Hair appointment at Elle at UMI Salon tomorrow (Mon) 9:15 AM. Michael Rich's birthday is Monday. Recruiter call Tuesday 9:30 AM + nails 4:30 PM. HR Networking Zoom Wednesday 12 PM (RSVP pending). Open Office Hours Zoom Thursday 12 PM (RSVP pending). Executive Roundtable Thursday — you declined. Amy's anniversary Wednesday; Christian H's birthday Thursday.</span>
      </div>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════════ SECTION 3: ACTION REQUIRED ══════════════════════════════════════════════ -->
<div class="section theme-red">
  <div class="section-title">⚡ Section 3 — Action Required</div>
  <div class="section-body">

    <div class="card card-red">
      <div class="card-title">🌊 Flash Flood Warning — NYC</div>
      <div class="card-meta">From: Notify NYC | Received: Sun, Aug 23, 2026 | <span class="badge badge-red">URGENT</span></div>
      <div class="card-body">
        <div class="card-row"><span class="card-label">Why It Matters:</span> Official National Weather Service Flash Flood Warning for Brooklyn, Staten Island, and Manhattan, issued 6:25 AM today.</div>
        <div class="card-row"><span class="card-label">Next Step:</span> Avoid travel if possible today. Monitor NYC Emergency Management updates. Do not walk near underpasses, subway stairs, or low-lying areas.</div>
        <div class="card-row"><span class="card-label">Due:</span> <strong>TODAY — Sunday, August 23</strong></div>
      </div>
    </div>

    <div class="card card-yellow">
      <div class="card-title">💳 Verizon Fios Bill Due Today</div>
      <div class="card-meta">From: Google Calendar | Date: Sun, Aug 23, 2026 | <span class="badge badge-yellow">BILLING</span></div>
      <div class="card-body">
        <div class="card-row"><span class="card-label">Why It Matters:</span> Verizon Fios bill is due today per your calendar reminder. Pay to avoid late fees.</div>
        <div class="card-row"><span class="card-label">Next Step:</span> Log in to Verizon Fios account and confirm payment or schedule it immediately.</div>
        <div class="card-row"><span class="card-label">Due:</span> <strong>TODAY — Sunday, August 23</strong></div>
      </div>
    </div>

    <div class="card card-green">
      <div class="card-title">💼 GitLab Application — Confirm Receipt by Rich (referred by Rob Demarais)</div>
      <div class="card-meta">From: Melissa (self, rescued from Trash) | Sent: Mon, Aug 24 | <span class="badge badge-green">JOB SEARCH</span></div>
      <div class="card-body">
        <div class="card-row"><span class="card-label">Why It Matters:</span> This email was sent by Melissa to a GitLab hiring contact (Rich) for the Senior Director, People Business Partners role with a referral from Rob Demarais. It was mistakenly sent to Trash and has been rescued.</div>
        <div class="card-row"><span class="card-label">Next Step:</span> Confirm Rich received the email. If no reply within 2–3 business days, follow up. Coordinate with Rob Demarais to ensure the referral is active in the system.</div>
        <div class="card-row"><span class="card-label">Due:</span> Follow up by Wed, Aug 26 if no response.</div>
      </div>
    </div>

    <div class="card card-green">
      <div class="card-title">📞 Recruiter Call — Tuesday, August 25 at 9:30 AM</div>
      <div class="card-meta">From: Google Calendar | <span class="badge badge-green">INTERVIEW PREP</span></div>
      <div class="card-body">
        <div class="card-row"><span class="card-label">Why It Matters:</span> Confirmed recruiter call 9:30–10:30 AM Tuesday. No details on company/role in calendar yet.</div>
        <div class="card-row"><span class="card-label">Next Step:</span> Locate the recruiter's details, research the company/role, and prepare your elevator pitch and target comp range. Confirm dial-in details.</div>
        <div class="card-row"><span class="card-label">Due:</span> Prep by Monday evening, Aug 24.</div>
      </div>
    </div>

    <div class="card card-blue">
      <div class="card-title">📅 RSVP Required — HR Networking &amp; Job Search Group Zoom (Wed Aug 26)</div>
      <div class="card-meta">From: Google Calendar — HR Networking Group | Status: <span class="badge badge-yellow">NEEDS ACTION</span></div>
      <div class="card-body">
        <div class="card-row"><span class="card-label">Why It Matters:</span> Large HR networking Zoom on Wednesday, Aug 26 at 12–1:30 PM. Your RSVP status is "Needs Action." ~170+ attendees. High-value networking opportunity.</div>
        <div class="card-row"><span class="card-label">Next Step:</span> Accept or decline. If attending, review the team guidelines and prepare a brief intro/update.</div>
        <div class="card-row"><span class="card-label">Due:</span> RSVP ASAP, before Wednesday.</div>
      </div>
    </div>

    <div class="card card-blue">
      <div class="card-title">📅 RSVP Required — HR Networking Open Office Hours Zoom (Thu Aug 27)</div>
      <div class="card-meta">From: Google Calendar — HR Networking Group | Status: <span class="badge badge-yellow">NEEDS ACTION</span></div>
      <div class="card-body">
        <div class="card-row"><span class="card-label">Why It Matters:</span> Open office hours Zoom on Thursday, Aug 27 at 12–1 PM. RSVP pending. Separate from Wednesday's session.</div>
        <div class="card-row"><span class="card-label">Next Step:</span> Accept or decline. If attending, prepare any specific job search questions to maximize the session.</div>
        <div class="card-row"><span class="card-label">Due:</span> RSVP ASAP, before Thursday.</div>
      </div>
    </div>

    <div class="card card-purple">
      <div class="card-title">💬 LinkedIn Message from Gopalan Arumugam — Unread</div>
      <div class="card-meta">From: Gopalan Arumugam via LinkedIn | Sun, Aug 23 | <span class="badge badge-purple">NETWORKING</span></div>
      <div class="card-body">
        <div class="card-row"><span class="card-label">Why It Matters:</span> Unread LinkedIn message. Given active job search, may be a recruiter or professional contact worth engaging.</div>
        <div class="card-row"><span class="card-label">Next Step:</span> Open LinkedIn and read/respond to Gopalan's message today.</div>
        <div class="card-row"><span class="card-label">Due:</span> Today or Monday.</div>
      </div>
    </div>

    <div class="card card-teal">
      <div class="card-title">✂️ Hair Appointment Tomorrow — Elle at UMI Salon, 9:15 AM</div>
      <div class="card-meta">From: Google Calendar | Mon, Aug 24, 9:15–10:45 AM | <span class="badge badge-teal">APPOINTMENT</span></div>
      <div class="card-body">
        <div class="card-row"><span class="card-label">Why It Matters:</span> Single Process with Blowout at UMI Salon, 37 West 20th St Suite 1107, NYC. Confirmed. Back-to-back with recruiter call Tuesday — look sharp!</div>
        <div class="card-row"><span class="card-label">Next Step:</span> Confirm appointment via GlossGenius link if needed. Plan travel time from Flatiron area.</div>
        <div class="card-row"><span class="card-label">Due:</span> Monday, Aug 24 — arrive by 9:10 AM.</div>
      </div>
    </div>

    <div class="card card-gray">
      <div class="card-title">📂 Bank of America Statement Available</div>
      <div class="card-meta">From: Bank of America | Sat, Aug 22 | <span class="badge badge-gray">FINANCIAL</span></div>
      <div class="card-body">
        <div class="card-row"><span class="card-label">Why It Matters:</span> Monthly statement for ADV Relationship Banking account ending 7471 is now available.</div>
        <div class="card-row"><span class="card-label">Next Step:</span> Log in and review your statement this week. Confirm no unauthorized charges.</div>
        <div class="card-row"><span class="card-label">Due:</span> This week.</div>
      </div>
    </div>

    <div class="card card-gray">
      <div class="card-title">🐾 Missing Pets in Your Area — Luna (Cat) &amp; Caramel (Dog)</div>
      <div class="card-meta">From: HomeAgain PetRescuers | Sat–Sun, Aug 22–23 | <span class="badge badge-gray">COMMUNITY</span></div>
      <div class="card-body">
        <div class="card-row"><span class="card-label">Why It Matters:</span> Luna (cat) last seen near Bromley Ave &amp; Emerson Ave, Teaneck, NJ. Caramel (dog, female) last seen near Castle Hill Ave &amp; Lacombe Ave, Bronx, NY 10473.</div>
        <div class="card-row"><span class="card-label">Next Step:</span> Keep an eye out. You recently joined the Pets in NJ &amp; PA Rehoming &amp; Rescue Facebook group — consider sharing these alerts there.</div>
        <div class="card-row"><span class="card-label">Due:</span> As soon as possible — time-sensitive for lost pets.</div>
      </div>
    </div>

  </div>
</div>

<!-- ══════════════════════════════════════════════ SECTION 4: FULL 7-DAY CALENDAR ══════════════════════════════════════════════ -->
<div class="section theme-blue">
  <div class="section-title">📅 Section 4 — Full 7-Day Calendar (Aug 23–29, 2026)</div>
  <div class="section-body">

    <!-- SUNDAY AUG 23 -->
    <div class="cal-day cal-today">
      <div class="cal-day-header">📍 TODAY — Sunday, August 23, 2026</div>
      <div class="cal-event cal-event-allday">
        <div class="cal-time">All Day</div>
        <div class="cal-info">
          <div class="cal-name">💳 Verizon Fios Bill Due</div>
          <div class="cal-detail">Status: Confirmed | No location</div>
          <div class="cal-detail" style="color:#c0392b; font-weight:700;">⚠️ PAY TODAY to avoid late fees</div>
          <div class="cal-prep">Prep: Log in to Verizon Fios account and complete payment.</div>
        </div>
      </div>
      <div class="cal-event" style="background:#fff3cd; border-left:3px solid #e67e22;">
        <div class="cal-time">6:25 AM</div>
        <div class="cal-info">
          <div class="cal-name">🌊 Flash Flood Warning — Brooklyn, Staten Island, Manhattan</div>
          <div class="cal-detail">Issued by National Weather Service | Source: Notify NYC alert</div>
          <div class="cal-detail" style="color:#c0392b; font-weight:700;">⚠️ Avoid unnecessary travel. Monitor updates.</div>
        </div>
      </div>
    </div>

    <!-- MONDAY AUG 24 -->
    <div class="cal-day">
      <div class="cal-day-header">Monday, August 24, 2026</div>
      <div class="cal-event cal-event-allday">
        <div class="cal-time">All Day</div>
        <div class="cal-info">
          <div class="cal-name">🎂 Michael Rich's Birthday</div>
          <div class="cal-detail">Status: Confirmed | Personal reminder</div>
          <div class="cal-prep">Prep: Send a birthday message or card today.</div>
        </div>
      </div>
      <div class="cal-event cal-event-confirmed">
        <div class="cal-time">9:15 – 10:45 AM</div>
        <div class="cal-info">
          <div class="cal-name">✂️ Hair Appointment — Elle at UMI Salon</div>
          <div class="cal-detail">Service: Single Process with Blowout | With: Elle M</div>
          <div class="cal-detail">📍 37 West 20th St, Suite 1107, New York, NY 10011</div>
          <div class="cal-detail">Status: Confirmed | <a href="https://elleatumi.glossgenius.com/a/f3c8e149bb71d70194fb118806b6484d849a" target="_blank">Manage Appointment</a></div>
          <div class="cal-prep">Prep: Arrive by 9:10 AM. Plan Flatiron transit. Check for weather delays given flood warning.</div>
          <span class="cal-conflict">⚠️ Note: Two overlapping calendar entries for this slot (Elle + Your Appointment at Elle at UMI Salon) — same event, no true conflict.</span>
        </div>
      </div>
    </div>

    <!-- TUESDAY AUG 25 -->
    <div class="cal-day">
      <div class="cal-day-header">Tuesday, August 25, 2026</div>
      <div class="cal-event cal-event-confirmed">
        <div class="cal-time">9:30 – 10:30 AM</div>
        <div class="cal-info">
          <div class="cal-name">📞 Recruiter Call</div>
          <div class="cal-detail">Status: Confirmed | No dial-in link on file | No company listed</div>
          <div class="cal-prep">Prep: Research company/role tonight. Prepare elevator pitch, target comp ($175K+), key HR accomplishments. Confirm call details with recruiter.</div>
        </div>
      </div>
      <div class="cal-event cal-event-confirmed">
        <div class="cal-time">4:30 – 5:30 PM</div>
        <div class="cal-info">
          <div class="cal-name">💅 Nails</div>
          <div class="cal-detail">Status: Confirmed | No location listed</div>
          <div class="cal-prep">Prep: Confirm salon appointment and allow travel time after recruiter call.</div>
        </div>
      </div>
    </div>

    <!-- WEDNESDAY AUG 26 -->
    <div class="cal-day">
      <div class="cal-day-header">Wednesday, August 26, 2026</div>
      <div class="cal-event cal-event-allday">
        <div class="cal-time">All Day</div>
        <div class="cal-info">
          <div class="cal-name">💍 Amy's Anniversary</div>
          <div class="cal-detail">Status: Confirmed | Personal reminder</div>
          <div class="cal-prep">Prep: Send a congratulatory message to Amy.</div>
        </div>
      </div>
      <div class="cal-event cal-event-pending">
        <div class="cal-time">12:00 – 1:30 PM</div>
        <div class="cal-info">
          <div class="cal-name">🌐 HR Networking &amp; Job Search Group — Zoom 2</div>
          <div class="cal-detail">Status: <span class="badge badge-yellow">RSVP NEEDED</span> | ~170+ attendees</div>
          <div class="cal-detail">📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Join Zoom</a></div>
          <div class="cal-prep">Prep: Accept/decline ASAP. Review team guidelines. Prepare brief job search status update and key asks.</div>
          <span class="cal-conflict">⚠️ Duplicate entry: "Network" event also shows 12–1:30 PM — same session, no true conflict.</span>
        </div>
      </div>
      <div class="cal-event cal-event-confirmed">
        <div class="cal-time">3:00 – 4:00 PM</div>
        <div class="cal-info">
          <div class="cal-name">💅 Nails</div>
          <div class="cal-detail">Status: Confirmed | No location listed</div>
          <div class="cal-prep">Prep: Note — you also have a nails appointment Tuesday 4:30 PM. Confirm which is the intended booking.</div>
          <span class="cal-conflict">⚠️ Potential duplicate: Nails also appear Tuesday 4:30 PM. Verify and cancel duplicate if needed.</span>
        </div>
      </div>
    </div>

    <!-- THURSDAY AUG 27 -->
    <div class="cal-day">
      <div class="cal-day-header">Thursday, August 27, 2026</div>
      <div class="cal-event cal-event-allday">
        <div class="cal-time">All Day</div>
        <div class="cal-info">
          <div class="cal-name">🎂 Christian H's Birthday</div>
          <div class="cal-detail">Status: Confirmed | Personal reminder</div>
          <div class="cal-prep">Prep: Send a birthday message.</div>
        </div>
      </div>
      <div class="cal-event cal-event-declined">
        <div class="cal-time">9:00 – 10:30 AM</div>
        <div class="cal-info">
          <div class="cal-name">🚫 Executive Roundtable (Declined)</div>
          <div class="cal-detail">Status: <span class="badge badge-red">DECLINED</span> | Hosted by John Madigan</div>
          <div class="cal-detail">📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link (on file)</a></div>
          <div class="cal-prep">No prep needed — you declined. Note for awareness.</div>
        </div>
      </div>
      <div class="cal-event cal-event-pending">
        <div class="cal-time">12:00 – 1:00 PM</div>
        <div class="cal-info">
          <div class="cal-name">🌐 HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
          <div class="cal-detail">Status: <span class="badge badge-yellow">RSVP NEEDED</span> | Same attendee group as Wednesday</div>
          <div class="cal-detail">📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Join Zoom</a></div>
          <div class="cal-prep">Prep: Accept/decline. Prepare specific job search questions. No recording — open discussion format.</div>
        </div>
      </div>
    </div>

    <!-- FRIDAY–SATURDAY AUG 28–29 -->
    <div class="cal-day">
      <div class="cal-day-header">Friday, August 28 – Saturday, August 29, 2026</div>
      <div class="cal-event cal-event-allday">
        <div class="cal-time">All Day</div>
        <div class="cal-info">
          <div class="cal-name">📭 No Calendar Events Scheduled</div>
          <div class="cal-detail">Enjoy the weekend! Consider using Friday for job application follow-ups.</div>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- ══════════════════════════════════════════════ SECTION 5: JOB SEARCH & INTERVIEW PIPELINE ══════════════════════════════════════════════ -->
<div class="section theme-green">
  <div class="section-title">💼 Section 5 — Job Search &amp; Interview Pipeline</div>
  <div class="section-body">

    <div class="group-header">🏆 Active Applications</div>
    <table>
      <thead>
        <tr><th>Role</th><th>Company</th><th>Status</th><th>Fit</th><th>Action Needed</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Senior Director, People Business Partners</strong></td>
          <td>GitLab</td>
          <td><span class="badge badge-green">Applied + Referred</span></td>
          <td><span class="fit-high">HIGH</span></td>
          <td>Confirm Rich received email. Coordinate with Rob Demarais re: referral status. Follow up by Wed Aug 26.</td>
        </tr>
      </tbody>
    </table>

    <div class="group-header">📋 LinkedIn Job Alerts</div>
    <table>
      <thead>
        <tr><th>Role</th><th>Company</th><th>Salary Range</th><th>Fit</th><th>Action Needed</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>VP, People</strong></td>
          <td>DomainTools</td>
          <td>$175K – $275K/year</td>
          <td><span class="fit-high">HIGH</span></td>
          <td>Review full posting. Apply if strong fit. Senior-level HR VP role with strong comp.</td>
        </tr>
        <tr>
          <td><strong>Chief Human Resources Officer</strong></td>
          <td>PeopleOps Jobs</td>
          <td>Not listed</td>
          <td><span class="fit-high">HIGH</span></td>
          <td>Review CHRO posting via LinkedIn. CHRO-level opportunity — aligns with career trajectory.</td>
        </tr>
      </tbody>
    </table>

    <div class="group-header">📞 Recruiter Calls &amp; Interviews Scheduled</div>
    <table>
      <thead>
        <tr><th>Event</th><th>Date &amp; Time</th><th>Status</th><th>Prep Needed</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Recruiter Call</strong></td>
          <td>Tue, Aug 25 | 9:30–10:30 AM</td>
          <td><span class="badge badge-green">CONFIRMED</span></td>
          <td>Research company/role. Prepare elevator pitch + comp targets. Confirm dial-in details.</td>
        </tr>
      </tbody>
    </table>

    <div class="group-header">🌐 Professional Networking</div>
    <table>
      <thead>
        <tr><th>Event</th><th>Date &amp; Time</th><th>RSVP</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>HR Networking &amp; Job Search Group — Zoom 2</strong></td>
          <td>Wed, Aug 26 | 12:00–1:30 PM</td>
          <td><span class="badge badge-yellow">NEEDS ACTION</span></td>
          <td>RSVP + prepare job search update. 170+ HR peers attending.</td>
        </tr>
        <tr>
          <td><strong>HR Networking Open Office Hours — Zoom 2</strong></td>
          <td>Thu, Aug 27 | 12:00–1:00 PM</td>
          <td><span class="badge badge-yellow">NEEDS ACTION</span></td>
          <td>RSVP + prepare specific Q&amp;A. Open discussion — no recording.</td>
        </tr>
        <tr>
          <td><strong>LinkedIn Message — Gopalan Arumugam</strong></td>
          <td>Sun, Aug 23</td>
          <td><span class="badge badge-red">UNREAD</span></td>
          <td>Read and respond. May be a recruiter or peer connection.</td>
        </tr>
        <tr>
          <td><strong>LinkedIn — Pooja Kapur, CPO (popular in network)</strong></td>
          <td>Sun, Aug 23</td>
          <td>—</td>
          <td>LinkedIn recommended connection. Consider reaching out to expand CPO network.</td>
        </tr>
      </tbody>
    </table>

    <div class="group-header">🔗 Resources Saved (Self-Emails)</div>
    <table>
      <thead>
        <tr><th>Subject</th><th>Link/Resource</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Remote websites</td>
          <td><a href="https://lnkd.in/p/gk8NVuCf" target="_blank">lnkd.in/p/gk8NVuCf</a></td>
          <td>Review remote job board resources. Organize into a tracker.</td>
        </tr>
        <tr>
          <td>Abacus AI</td>
          <td><a href="https://supercomputer.abacus.ai/sjh" target="_blank">supercomputer.abacus.ai</a></td>
          <td>Explore Abacus AI tool — may be useful for job search or HR analytics.</td>
        </tr>
        <tr>
          <td>(no subject)</td>
          <td><a href="https://lnkd.in/p/gvDHQtHe" target="_blank">lnkd.in/p/gvDHQtHe</a></td>
          <td>Open link and identify resource — file or bookmark.</td>
        </tr>
        <tr>
          <td>Remote job boards</td>
          <td><a href="https://lnkd.in/p/gAjFyUE9" target="_blank">lnkd.in/p/gAjFyUE9</a></td>
          <td>Review curated remote job board list from LinkedIn.</td>
        </tr>
      </tbody>
    </table>

    <div class="group-header">📌 LinkedIn Support</div>
    <table>
      <thead>
        <tr><th>Case</th><th>Status</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>LMS Case #260822-012578 (Virtual Chat Assistant)</td>
          <td><span class="badge badge-gray">CLOSED</span></td>
          <td>Case is closed. May reply within 14 days. Review if issue is resolved.</td>
        </tr>
      </tbody>
    </table>

  </div>
</div>

<!-- ══════════════════════════════════════════════ SECTION 6: FULL EMAIL REVIEW BY CATEGORY ══════════════════════════════════════════════ -->
<div class="section theme-dark">
  <div class="section-title">📂 Section 6 — Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="group-header" style="color:#c0392b;">🔴 Security / Risk</div>
    <div class="alert-box">
      <strong>10 phishing/scam emails were automatically removed before reaching your inbox.</strong> Details below. No action required on these — they have been quarantined.
    </div>
    <table>
      <thead>
        <tr><th>Sender</th><th>Subject</th><th>Disposition</th><th>Reason</th></tr>
      </thead>
      <tbody>
        <tr><td>"Cloud.Security"</td><td>You have reached your storage limit (×3 instances)</td><td><span class="badge badge-red">Auto-Trashed — Phishing</span></td><td>Fake cloud storage alert from random domains impersonating a security service — credential-harvesting with urgent account-threat language.</td></tr>
        <tr><td>"Cloud.Security.Alert"</td><td>Storage limit detected on your account (×3 instances)</td><td><span class="badge badge-red">Auto-Trashed — Phishing</span></td><td>Fake cloud storage suspension alerts from random domains — same credential-harvesting campaign.</td></tr>
        <tr><td>"Payment-Declined"</td><td>Your Account Sirius XM Will Be Removed Today (×2 instances)</td><td><span class="badge badge-red">Auto-Trashed — Phishing</span></td><td>Spoofed SiriusXM payment failure notices from random domains — credential/payment harvesting.</td></tr>
        <tr><td>SiriusXM (spoofed)</td><td>melissaw212: Your SiriusXM Membership has Expired</td><td><span class="badge badge-red">Auto-Trashed — Phishing</span></td><td>Spoofed SiriusXM membership expiration from non-SiriusXM domain.</td></tr>
        <tr><td>"CashApp" (spoofed)</td><td>You have received 15.99$ — Raging Bull Casino payout verification</td><td><span class="badge badge-red">Auto-Trashed — Phishing</span></td><td>Fake CashApp payout from spoofed random domain — personal info harvesting scam.</td></tr>
      </tbody>
    </table>
    <p class="note">Count: 10 emails | Recommendation: No action needed. All quarantined automatically.</p>

    <hr class="divider">

    <!-- JOB SEARCH -->
    <div class="group-header" style="color:#27ae60;">🟢 Job Search</div>
    <table>
      <thead>
        <tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr style="background:#eafaf1;">
          <td>Melissa (self) <span class="badge badge-green">RESCUED</span></td>
          <td>Senior Director, People Business Partners – referred by Rob Demarais</td>
          <td>Rescued from Trash</td>
          <td>Confirm receipt by Rich at GitLab. Coordinate referral with Rob Demarais.</td>
        </tr>
        <tr>
          <td>LinkedIn Job Alerts</td>
          <td>VP, People at DomainTools: up to $275K/year</td>
          <td>Read</td>
          <td>Review and apply if strong fit. High comp — $175K–$275K.</td>
        </tr>
        <tr>
          <td>LinkedIn Job Alerts</td>
          <td>Chief Human Resources Officer — PeopleOps Jobs</td>
          <td>Read</td>
          <td>Review CHRO listing. CHRO-level — strong career alignment.</td>
        </tr>
      </tbody>
    </table>
    <p class="note">Count: 3 emails | Recommendation: Act on all three. GitLab follow-up is highest priority.</p>

    <hr class="divider">

    <!-- RECRUITERS / NETWORKING -->
    <div class="group-header" style="color:#27ae60;">🟢 Recruiters / Networking</div>
    <table>
      <thead>
        <tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Gopalan Arumugam via LinkedIn</td>
          <td>Gopalan just messaged you</td>
          <td><span class="badge badge-red">UNREAD</span></td>
          <td>Read and respond today. Potential recruiter or peer.</td>
        </tr>
        <tr>
          <td>LinkedIn</td>
          <td>Pooja Kapur, Chief People Officer, is popular in your network</td>
          <td>Unread (in Trash)</td>
          <td>Consider connecting with Pooja Kapur — CPO-level peer in your network.</td>
        </tr>
        <tr>
          <td>LinkedIn Customer Support</td>
          <td>LMS Case #260822-012578 — Closed</td>
          <td>Read — Inbox</td>
          <td>Case closed. Verify your LinkedIn issue is resolved. May reply within 14 days.</td>
        </tr>
      </tbody>
    </table>
    <p class="note">Count: 3 emails | Recommendation: Respond to Gopalan today. Review LinkedIn case.</p>

    <hr class="divider">

    <!-- CALENDAR / EVENTS -->
    <div class="group-header" style="color:#2980b9;">🔵 Calendar / Events</div>
    <table>
      <thead>
        <tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Notify NYC</td>
          <td>Flash Flood Warning — Brooklyn, Staten Island, Manhattan</td>
          <td><span class="badge badge-red">URGENT — UNREAD</span></td>
          <td>Avoid unnecessary travel today. Monitor NYC Emergency Management.</td>
        </tr>
      </tbody>
    </table>
    <p class="note">Count: 1 email | Recommendation: Safety awareness — act immediately.</p>

    <hr class="divider">

    <!-- FINANCIAL / BILLING -->
    <div class="group-header" style="color:#e67e22;">🟡 Financial / Billing</div>
    <table>
      <thead>
        <tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Bank of America</td>
          <td>Your statement is available (Account ending 7471)</td>
          <td>Read</td>
          <td>Log in and review statement. Confirm no unauthorized activity.</td>
        </tr>
      </tbody>
    </table>
    <p class="note">Count: 1 email | Recommendation: Review statement this week.</p>

    <hr class="divider">

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="group-header" style="color:#8e44ad;">🟣 Professional Development</div>
    <table>
      <thead>
        <tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Ruben Hassid (Substack)</td>
          <td>If I had absolutely no money, I'd use these free AI.</td>
          <td>Unread</td>
          <td>Read when time allows — free AI tools list may be relevant for job search &amp; productivity.</td>
        </tr>
      </tbody>
    </table>
    <p class="note">Count: 1 email | Recommendation: Read when convenient. Relevant to AI tools research.</p>

    <hr class="divider">

    <!-- PERSONAL -->
    <div class="group-header" style="color:#16a085;">🩵 Personal</div>
    <table>
      <thead>
        <tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Match</td>
          <td>Mark likes you. See if it's mutual.</td>
          <td><span class="badge badge-red">UNREAD — Inbox</span></td>
          <td>Review when ready. Check Mark's profile.</td>
        </tr>
        <tr>
          <td>Match</td>
          <td>Junior likes you. See if it's mutual.</td>
          <td><span class="badge badge-red">UNREAD — Inbox</span></td>
          <td>Review when ready. Check Junior's profile.</td>
        </tr>
        <tr>
          <td>Match</td>
          <td>Konstantinos just sent you a new message. 💌</td>
          <td><span class="badge badge-red">UNREAD — Inbox</span></td>
          <td>Read and respond when ready.</td>
        </tr>
        <tr>
          <td>Match</td>
          <td>You've had a profile view from Paul (60, Manhattan)</td>
          <td>Unread (not in inbox)</td>
          <td>Review Paul's profile at your convenience.</td>
        </tr>
        <tr>
          <td>Match</td>
          <td>Gino just sent you a new message. 💌</td>
          <td>Read</td>
          <td>
