<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa W — August 22, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }

  .page-wrapper { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: white; border-radius: 16px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header .subtitle { font-size: 15px; color: #a8b8d8; margin-top: 6px; }
  .header-meta { display: flex; gap: 24px; margin-top: 20px; flex-wrap: wrap; }
  .header-meta-item { background: rgba(255,255,255,0.1); border-radius: 10px; padding: 10px 18px; }
  .header-meta-item .val { font-size: 22px; font-weight: 700; color: #7eb8f7; }
  .header-meta-item .lbl { font-size: 11px; color: #a8b8d8; text-transform: uppercase; letter-spacing: 0.8px; }

  /* SECTION HEADERS */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; letter-spacing: 0.3px; margin-bottom: 12px; padding-bottom: 8px; border-bottom: 2px solid #e4e8f0; display: flex; align-items: center; gap: 8px; }
  .section-number { background: #0f3460; color: white; border-radius: 50%; width: 24px; height: 24px; display: inline-flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 700; flex-shrink: 0; }

  /* COLOR BANDS */
  .band-red { border-left: 5px solid #e53e3e; background: #fff5f5; border-radius: 0 10px 10px 0; }
  .band-yellow { border-left: 5px solid #d69e2e; background: #fffff0; border-radius: 0 10px 10px 0; }
  .band-blue { border-left: 5px solid #3182ce; background: #ebf8ff; border-radius: 0 10px 10px 0; }
  .band-green { border-left: 5px solid #38a169; background: #f0fff4; border-radius: 0 10px 10px 0; }
  .band-purple { border-left: 5px solid #805ad5; background: #faf5ff; border-radius: 0 10px 10px 0; }
  .band-gray { border-left: 5px solid #a0aec0; background: #f7fafc; border-radius: 0 10px 10px 0; }

  /* CARDS */
  .card { border-radius: 12px; padding: 16px 20px; margin-bottom: 12px; }
  .card-title { font-weight: 700; font-size: 14px; margin-bottom: 4px; }
  .card-sub { font-size: 12px; color: #555; margin-bottom: 6px; }
  .card-body { font-size: 13px; }
  .card-row { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 6px; }
  .tag { display: inline-block; padding: 2px 10px; border-radius: 20px; font-size: 11px; font-weight: 600; }
  .tag-red { background: #fed7d7; color: #c53030; }
  .tag-yellow { background: #fefcbf; color: #975a16; }
  .tag-blue { background: #bee3f8; color: #2b6cb0; }
  .tag-green { background: #c6f6d5; color: #276749; }
  .tag-purple { background: #e9d8fd; color: #553c9a; }
  .tag-gray { background: #e2e8f0; color: #4a5568; }
  .tag-orange { background: #feebc8; color: #c05621; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #1a1a2e; color: white; padding: 9px 12px; text-align: left; font-size: 12px; font-weight: 600; letter-spacing: 0.4px; }
  th:first-child { border-radius: 8px 0 0 0; }
  th:last-child { border-radius: 0 8px 0 0; }
  td { padding: 8px 12px; border-bottom: 1px solid #e4e8f0; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #f8fafc; }
  tr:hover td { background: #eef2f7; }
  .table-wrap { border-radius: 10px; overflow: hidden; border: 1px solid #e4e8f0; }

  /* EXEC SUMMARY */
  .exec-bullets { display: flex; flex-direction: column; gap: 10px; }
  .exec-bullet { display: flex; gap: 12px; align-items: flex-start; padding: 14px 18px; border-radius: 10px; }
  .exec-icon { font-size: 22px; flex-shrink: 0; }
  .exec-text strong { display: block; font-size: 14px; font-weight: 700; margin-bottom: 2px; }
  .exec-text span { font-size: 13px; color: #444; }

  /* ACTION CARDS */
  .action-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 14px; }
  .action-card { border-radius: 12px; padding: 16px 20px; }
  .action-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
  .action-title { font-weight: 700; font-size: 14px; margin-bottom: 4px; }
  .action-source { font-size: 11px; color: #666; margin-bottom: 8px; }
  .action-row { display: flex; gap: 6px; margin-top: 4px; flex-wrap: wrap; }
  .action-item { font-size: 12px; }
  .action-item strong { font-weight: 600; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { background: #0f3460; color: white; padding: 8px 16px; border-radius: 8px 8px 0 0; font-weight: 700; font-size: 13px; }
  .cal-event { padding: 10px 16px; border-bottom: 1px solid #dbe4f0; background: white; display: flex; flex-wrap: wrap; gap: 8px; align-items: flex-start; }
  .cal-event:last-child { border-bottom: none; border-radius: 0 0 8px 8px; }
  .cal-time { min-width: 110px; font-weight: 600; font-size: 12px; color: #2b6cb0; }
  .cal-details { flex: 1; }
  .cal-name { font-weight: 700; font-size: 13px; }
  .cal-meta { font-size: 11px; color: #555; margin-top: 3px; }
  .cal-status { font-size: 11px; padding: 2px 8px; border-radius: 10px; font-weight: 600; display: inline-block; }
  .status-confirmed { background: #c6f6d5; color: #276749; }
  .status-needs { background: #fefcbf; color: #975a16; }
  .status-declined { background: #fed7d7; color: #c53030; }

  /* JOB CARDS */
  .job-card { background: white; border-radius: 10px; padding: 14px 18px; margin-bottom: 10px; border: 1px solid #e4e8f0; }
  .job-header { display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 8px; }
  .job-title { font-weight: 700; font-size: 14px; }
  .job-co { font-size: 12px; color: #555; }
  .job-meta { font-size: 12px; color: #666; margin-top: 6px; }

  /* DASHBOARD GRID */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-card { background: white; border-radius: 12px; padding: 16px; border: 1px solid #e4e8f0; }
  .dash-card-title { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; color: #666; margin-bottom: 10px; }
  .dash-card-val { font-size: 28px; font-weight: 700; }
  .dash-card-list { font-size: 12px; color: #444; margin-top: 6px; }
  .dash-card-list li { margin-bottom: 4px; list-style: disc; margin-left: 14px; }

  /* TRIAGE TABLE */
  .triage-status { font-size: 12px; font-weight: 700; white-space: nowrap; }
  .triage-from { font-size: 12px; }
  .triage-subject { font-size: 12px; font-weight: 600; }
  .triage-summary { font-size: 11px; color: #555; }

  /* PRIORITY BOX */
  .priority-box { background: linear-gradient(135deg, #0f3460, #1a1a2e); color: white; border-radius: 14px; padding: 24px 28px; }
  .priority-box h3 { font-size: 16px; font-weight: 700; margin-bottom: 16px; color: #7eb8f7; }
  .priority-item { display: flex; gap: 14px; margin-bottom: 16px; align-items: flex-start; }
  .priority-num { background: #e53e3e; color: white; border-radius: 50%; width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 14px; flex-shrink: 0; }
  .priority-num.two { background: #d69e2e; }
  .priority-num.three { background: #38a169; }
  .priority-text strong { display: block; font-size: 14px; margin-bottom: 2px; }
  .priority-text span { font-size: 12px; color: #a8b8d8; }

  /* MISC */
  .note-box { background: #fffbeb; border: 1px solid #f6e05e; border-radius: 8px; padding: 10px 14px; font-size: 12px; color: #744210; margin-bottom: 10px; }
  .rescued-badge { background: #c6f6d5; color: #276749; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 10px; display: inline-block; }
  .phishing-badge { background: #fed7d7; color: #c53030; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 10px; display: inline-block; }
  .auto-trash-badge { background: #fefcbf; color: #975a16; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 10px; display: inline-block; }
  .divider { height: 1px; background: #e4e8f0; margin: 28px 0; }
  .group-header { font-size: 13px; font-weight: 700; color: #0f3460; margin: 12px 0 6px; text-transform: uppercase; letter-spacing: 0.5px; }
  ul.detail-list { margin-left: 18px; }
  ul.detail-list li { margin-bottom: 3px; font-size: 12px; }
  .conflict-warn { background: #fff5f5; border: 1px solid #fc8181; border-radius: 6px; padding: 4px 10px; font-size: 11px; color: #c53030; margin-top: 4px; }
</style>
</head>
<body>
<div class="page-wrapper">

<!-- ══════════════════════════════════════════════════════════════
     SECTION 0: EMAIL TRIAGE QUICK LIST
══════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="section-number">0</span> Email Triage Quick List</div>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th style="width:120px">Status</th>
          <th style="width:200px">From</th>
          <th>Subject</th>
          <th>Summary</th>
        </tr>
      </thead>
      <tbody>
        <!-- RESCUED -->
        <tr style="background:#f0fff4">
          <td class="triage-status"><span class="rescued-badge">✅ RESCUED</span></td>
          <td class="triage-from">Google Workspace Team</td>
          <td class="triage-subject">You now have exclusive access to AI features</td>
          <td class="triage-summary">Legitimate Google Workspace notification about Gemini AI access — rescued from Trash. Review and activate.</td>
        </tr>
        <!-- INBOX EMAILS (individual rows) -->
        <tr>
          <td class="triage-status"><span class="tag tag-blue">📥 INBOX</span></td>
          <td class="triage-from">Melissa W (self)</td>
          <td class="triage-subject">The Claude-Only Operator Stack (×2)</td>
          <td class="triage-summary">Self-sent Notion link — personal reference/research notes. Two copies in inbox.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="tag tag-blue">📥 INBOX</span></td>
          <td class="triage-from">Melissa W (self)</td>
          <td class="triage-subject">Interview help</td>
          <td class="triage-summary">Self-sent AI interview coaching prompt — active job search prep tool.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="tag tag-blue">📥 INBOX</span></td>
          <td class="triage-from">Melissa W (self)</td>
          <td class="triage-subject">LinkedIn optimization</td>
          <td class="triage-summary">Self-sent LinkedIn profile optimization prompt — job search tool.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="tag tag-blue">📥 INBOX</span></td>
          <td class="triage-from">LinkedIn Job Alerts</td>
          <td class="triage-subject">VP, Human Resources Business Partner — PeopleOps Jobs</td>
          <td class="triage-summary">Senior HRBP role. Matches Melissa's profile. High fit.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="tag tag-blue">📥 INBOX</span></td>
          <td class="triage-from">LinkedIn Job Alerts</td>
          <td class="triage-subject">Head of HR — WHS Inc. (Willow Telehealth)</td>
          <td class="triage-summary">Head of HR at telehealth company. Relevant to CPO/HR leadership track.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="tag tag-blue">📥 INBOX</span></td>
          <td class="triage-from">Sarah S via LinkedIn</td>
          <td class="triage-subject">Melissa A, I'd like to connect — decube (Founder's Office)</td>
          <td class="triage-summary">Inbound LinkedIn connection from decube Founder's Office. Worth reviewing.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="tag tag-blue">📥 INBOX</span></td>
          <td class="triage-from">Mario Linale via LinkedIn</td>
          <td class="triage-subject">Mario accepted your invitation</td>
          <td class="triage-summary">New LinkedIn connection accepted. Explore network.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="tag tag-blue">📥 INBOX</span></td>
          <td class="triage-from">SignalHire</td>
          <td class="triage-subject">You've just got 5 SignalHire credits</td>
          <td class="triage-summary">5 new contact credits added — useful for outreach in active job search.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="tag tag-blue">📥 INBOX</span></td>
          <td class="triage-from">Zoom</td>
          <td class="triage-subject">Your seat is reserved — Claude 101 Workshop</td>
          <td class="triage-summary">Confirmed registration for 3-hour Claude AI workshop. Check date/time.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="tag tag-blue">📥 INBOX</span></td>
          <td class="triage-from">Outskill</td>
          <td class="triage-subject">You're in. Here's what we built for you this time.</td>
          <td class="triage-summary">Rebuilt Claude-focused learning session. Review for upcoming professional dev.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="tag tag-blue">📥 INBOX</span></td>
          <td class="triage-from">Match.com</td>
          <td class="triage-subject">John, Konstantinos, Brendan, Eric, Andrew, Michael like you / Chad viewed</td>
          <td class="triage-summary">Multiple Match.com activity notifications — 6 total (likes + profile view).</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="tag tag-blue">📥 INBOX</span></td>
          <td class="triage-from">OkCupid</td>
          <td class="triage-subject">Someone likes you</td>
          <td class="triage-summary">OkCupid notification — personal.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="tag tag-blue">📥 INBOX</span></td>
          <td class="triage-from">Indeed</td>
          <td class="triage-subject">Senior People Operations Manager @ Mixpanel</td>
          <td class="triage-summary">Relevant senior PeopleOps role match from Indeed. Review and apply.</td>
        </tr>
        <tr>
          <td class="triage-status"><span class="tag tag-blue">📥 INBOX</span></td>
          <td class="triage-from">Glassdoor Jobs</td>
          <td class="triage-subject">Director, HR at Smart Electric Power Alliance + 8 more</td>
          <td class="triage-summary">Director-level HR roles, Remote US. Review listings.</td>
        </tr>
        <!-- TRASH SUMMARY ROWS -->
        <tr style="background:#fff5f5">
          <td class="triage-status"><span class="phishing-badge">🗑 AUTO-TRASHED</span></td>
          <td colspan="3" class="triage-summary" style="font-size:12px; color:#c53030; font-weight:600;">
            5 emails auto-trashed (phishing / credential harvesting) — see Section 6: Security/Risk &amp; Section 7: Trash Review
          </td>
        </tr>
        <tr style="background:#fffff0">
          <td class="triage-status"><span class="auto-trash-badge">🗑 AUTO-TRASHED</span></td>
          <td colspan="3" class="triage-summary" style="font-size:12px; color:#975a16; font-weight:600;">
            2 emails auto-trashed (newsletters/digests) — see Section 9: Newsletters &amp; Subscriptions &amp; Section 7: Trash Review
          </td>
        </tr>
        <tr style="background:#f7fafc">
          <td class="triage-status"><span class="tag tag-gray">🗂 TRASH (manual)</span></td>
          <td colspan="3" class="triage-summary" style="font-size:12px; color:#4a5568; font-weight:600;">
            ~20 emails in Trash (retail promos, newsletters, low-priority digests, spam) — see Section 7: Trash Review
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ══════════════════════════════════════════════════════════════
     SECTION 1: HEADER
══════════════════════════════════════════════════════════════ -->
<div class="header">
  <h1>☀️ Good Morning, Melissa</h1>
  <div class="subtitle">Executive Briefing — Saturday, August 22, 2026</div>
  <div class="header-meta">
    <div class="header-meta-item">
      <div class="val">50</div>
      <div class="lbl">Emails Reviewed</div>
    </div>
    <div class="header-meta-item">
      <div class="val">13</div>
      <div class="lbl">Calendar Events</div>
    </div>
    <div class="header-meta-item">
      <div class="val">5</div>
      <div class="lbl">Phishing Blocked</div>
    </div>
    <div class="header-meta-item">
      <div class="val">7</div>
      <div class="lbl">Job Leads Active</div>
    </div>
    <div class="header-meta-item">
      <div class="val">3</div>
      <div class="lbl">Actions Required</div>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════════════════════════
     SECTION 2: EXECUTIVE SUMMARY
══════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="section-number">2</span> Executive Summary</div>
  <div class="exec-bullets">
    <div class="exec-bullet band-red card">
      <div class="exec-icon">🔴</div>
      <div class="exec-text">
        <strong>Security Risk — 5 Phishing Emails Auto-Blocked Today</strong>
        <span>Five high-confidence phishing attempts hit your inbox today: two fake SiriusXM account-removal threats, two spoofed storage-full scams (including one posing as you), and one fake Cash App casino scam. All have been auto-trashed. No action needed, but awareness is warranted — your email address is being actively targeted. Consider reviewing spam filter settings.</span>
      </div>
    </div>
    <div class="exec-bullet band-green card">
      <div class="exec-icon">🟢</div>
      <div class="exec-text">
        <strong>Strong Job Search Momentum — 7 Active Leads Including VP &amp; Director Roles</strong>
        <span>Today's inbox includes a VP of HR Business Partner role (PeopleOps Jobs), Head of HR at Willow Telehealth, Senior PeopleOps Manager at Mixpanel, Director of HR at Smart Electric Power Alliance (remote), and a CPO/Talent lead alert from JobLeads. You have a Recruiter Call on Monday (Aug 25) and two HR Networking sessions mid-week. Your SignalHire credits just refreshed — strong week ahead.</span>
      </div>
    </div>
    <div class="exec-bullet band-yellow card">
      <div class="exec-icon">🟡</div>
      <div class="exec-text">
        <strong>Busy Week Starting Sunday — Verizon Bill Due, Hair Appointment, Recruiter Call &amp; Networking</strong>
        <span>Verizon Fios bill is due Sunday (Aug 23). Hair appointment with Elle at UMI Salon is Monday (Aug 24) at 9:15 AM. Recruiter Call Monday at 9:30 AM — potential scheduling conflict to monitor. Two HR Networking/Job Search Zoom sessions (Wed + Thu) have no RSVP confirmed yet. Executive Roundtable on Thursday has been declined.</span>
      </div>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════════════════════════
     SECTION 3: ACTION REQUIRED
══════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="section-number">3</span> Action Required</div>
  <div class="action-grid">

    <div class="action-card band-yellow card">
      <div class="action-label" style="color:#975a16;">⚡ URGENT — BILLING</div>
      <div class="action-title">Verizon Fios Bill Due</div>
      <div class="action-source">📅 Google Calendar — Due Aug 23 (Tomorrow)</div>
      <div class="action-item"><strong>Why it matters:</strong> Bill is due tomorrow, Sunday. Missing it may trigger a late fee or service interruption.</div>
      <div class="action-item" style="margin-top:6px"><strong>Next step:</strong> Log into Verizon Fios and confirm payment has processed, or pay now.</div>
      <div class="action-row"><span class="tag tag-yellow">Due: Aug 23</span></div>
    </div>

    <div class="action-card band-blue card">
      <div class="action-label" style="color:#2b6cb0;">📋 RSVP NEEDED</div>
      <div class="action-title">RSVP: HR Networking &amp; Job Search Group Zoom</div>
      <div class="action-source">📅 Calendar — Wed Aug 26, 12:00–1:30 PM &amp; Thu Aug 27, 12:00–1:00 PM</div>
      <div class="action-item"><strong>Why it matters:</strong> Both HR Networking Zoom sessions show status "needsAction" — you haven't formally RSVP'd. These are high-value networking touchpoints during active job search.</div>
      <div class="action-item" style="margin-top:6px"><strong>Next step:</strong> Open calendar invites and click Accept for both sessions. Join links are confirmed in calendar.</div>
      <div class="action-row"><span class="tag tag-blue">RSVP by: Aug 25</span></div>
    </div>

    <div class="action-card band-green card">
      <div class="action-label" style="color:#276749;">💼 JOB SEARCH</div>
      <div class="action-title">Review &amp; Apply: VP HRBP + Sr. PeopleOps + Director HR</div>
      <div class="action-source">LinkedIn, Indeed, Glassdoor — Arrived Today</div>
      <div class="action-item"><strong>Why it matters:</strong> Three high-fit roles landed today: VP of HR Business Partner (PeopleOps Jobs), Senior PeopleOps Manager (Mixpanel via Indeed), Director HR (Smart Electric Power Alliance, Remote). Use your freshly replenished SignalHire credits and AI interview tools.</div>
      <div class="action-item" style="margin-top:6px"><strong>Next step:</strong> Review all three job descriptions today. Use your "Interview help" and "LinkedIn optimization" self-sent prompts to tailor applications.</div>
      <div class="action-row"><span class="tag tag-green">High Priority</span><span class="tag tag-blue">Use SignalHire Credits</span></div>
    </div>

    <div class="action-card band-purple card">
      <div class="action-label" style="color:#553c9a;">🎓 PROFESSIONAL DEV</div>
      <div class="action-title">Confirm: Claude 101 Workshop &amp; Outskill Session</div>
      <div class="action-source">Zoom (from no-reply@zoom.us) + Outskill (hi@mail.outskill.com)</div>
      <div class="action-item"><strong>Why it matters:</strong> Your Zoom seat for Claude 101 Workshop is confirmed. Outskill also rebuilt a Claude-focused session. Both align directly with your interest in the Claude-Only Operator Stack (your self-sent Notion notes). No date visible — verify and add to calendar.</div>
      <div class="action-item" style="margin-top:6px"><strong>Next step:</strong> Open Zoom confirmation email to find workshop date/time and add to calendar. Reply to Outskill to confirm your spot.</div>
      <div class="action-row"><span class="tag tag-purple">Add to Calendar</span></div>
    </div>

    <div class="action-card band-green card">
      <div class="action-label" style="color:#276749;">🔗 NETWORKING</div>
      <div class="action-title">Activate New Google Workspace AI Features</div>
      <div class="action-source">Google Workspace Team — workspace-noreply@google.com — ✅ RESCUED from Trash</div>
      <div class="action-item"><strong>Why it matters:</strong> This legitimate Google email was initially trashed and rescued. You now have access to Gemini AI features within Workspace — directly relevant to your Claude/AI interest stack and job search productivity.</div>
      <div class="action-item" style="margin-top:6px"><strong>Next step:</strong> Open email, click "Get started with Gemini," and explore AI tools in Gmail/Docs/Sheets.</div>
      <div class="action-row"><span class="tag tag-green">High Value</span><span class="rescued-badge">✅ Rescued</span></div>
    </div>

  </div>
</div>

<!-- ══════════════════════════════════════════════════════════════
     SECTION 4: FULL 7-DAY CALENDAR
══════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="section-number">4</span> Full 7-Day Calendar — Aug 22–28, 2026</div>

  <!-- SAT AUG 22 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Saturday, August 22, 2026 — TODAY</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="cal-name">No events scheduled today</div>
        <div class="cal-meta">Use today to review job listings, apply to roles, and prep for Monday's recruiter call.</div>
      </div>
    </div>
  </div>

  <!-- SUN AUG 23 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Sunday, August 23, 2026</div>
    <div class="cal-event" style="background:#fffff0">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="cal-name">💳 Verizon Fios Bill</div>
        <div class="cal-meta">📍 No location</div>
        <div class="cal-meta"><span class="cal-status status-confirmed">✅ Confirmed</span></div>
        <div class="cal-meta" style="margin-top:4px"><strong>⚠️ Action:</strong> Confirm payment is processed. Log in to Verizon Fios today to verify.</div>
      </div>
    </div>
  </div>

  <!-- MON AUG 24 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Monday, August 24, 2026</div>
    <div class="cal-event" style="background:#faf5ff">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="cal-name">🎂 Michael Rich's Birthday</div>
        <div class="cal-meta"><span class="cal-status status-confirmed">✅ Confirmed</span> &nbsp; Send a message or card today.</div>
      </div>
    </div>
    <div class="cal-event" style="background:#ebf8ff">
      <div class="cal-time">9:15 AM – 10:15 AM</div>
      <div class="cal-details">
        <div class="cal-name">💇 Elle (Hair Appointment — UMI Salon)</div>
        <div class="cal-meta">📍 37 West 20th Suite 1107, New York, NY 10011 | With: Elle M | Service: Single Process with Blowout</div>
        <div class="cal-meta"><span class="cal-status status-confirmed">✅ Confirmed</span></div>
        <div class="cal-meta" style="margin-top:4px">Note: Appointment runs until 10:45 AM (per salon confirmation). Manage at: elleatumi.glossgenius.com</div>
        <div class="conflict-warn">⚠️ CONFLICT: Recruiter Call starts at 9:30 AM — overlaps with this appointment (9:15–10:45 AM). Reschedule one or plan accordingly.</div>
      </div>
    </div>
    <div class="cal-event" style="background:#f0fff4">
      <div class="cal-time">9:30 AM – 10:30 AM</div>
      <div class="cal-details">
        <div class="cal-name">📞 Recruiter Call</div>
        <div class="cal-meta">📍 No location provided | No attendees listed</div>
        <div class="cal-meta"><span class="cal-status status-confirmed">✅ Confirmed</span></div>
        <div class="cal-meta" style="margin-top:4px"><strong>Prep needed:</strong> Review target job descriptions, refresh your elevator pitch, prepare STAR-format examples. Confirm call-in number if applicable.</div>
        <div class="conflict-warn">⚠️ CONFLICT: Overlaps with hair appointment (9:15–10:45 AM). Review and resolve this scheduling conflict before Monday.</div>
      </div>
    </div>
  </div>

  <!-- TUE AUG 25 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Tuesday, August 25, 2026</div>
    <div class="cal-event" style="background:#f0fff4">
      <div class="cal-time">9:30 AM – 10:30 AM</div>
      <div class="cal-details">
        <div class="cal-name">📞 Recruiter Call</div>
        <div class="cal-meta"><em>Note: Two "Recruiter Call" events exist — one on Aug 24 and one on Aug 25. Both confirmed.</em></div>
        <div class="cal-meta"><span class="cal-status status-confirmed">✅ Confirmed</span></div>
        <div class="cal-meta" style="margin-top:4px"><strong>Prep needed:</strong> Research company/recruiter, rehearse pitch, review open roles. Confirm if this is the same call or a different one.</div>
      </div>
    </div>
    <div class="cal-event" style="background:#faf5ff">
      <div class="cal-time">4:30 PM – 5:30 PM</div>
      <div class="cal-details">
        <div class="cal-name">💅 Nails</div>
        <div class="cal-meta">📍 No location provided</div>
        <div class="cal-meta"><span class="cal-status status-confirmed">✅ Confirmed</span></div>
      </div>
    </div>
  </div>

  <!-- WED AUG 26 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Wednesday, August 26, 2026</div>
    <div class="cal-event" style="background:#faf5ff">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="cal-name">💍 Amy's Anniversary</div>
        <div class="cal-meta"><span class="cal-status status-confirmed">✅ Confirmed</span> &nbsp; Send a message or note to Amy.</div>
      </div>
    </div>
    <div class="cal-event" style="background:#ebf8ff">
      <div class="cal-time">12:00 PM – 1:30 PM</div>
      <div class="cal-details">
        <div class="cal-name">🤝 HR Networking &amp; Job Search Group — Zoom Session 2</div>
        <div class="cal-meta">📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a></div>
        <div class="cal-meta"><span class="cal-status status-needs">⏳ RSVP Needed</span> &nbsp; 190+ attendees from HR community</div>
        <div class="cal-meta" style="margin-top:4px"><strong>Prep needed:</strong> Review team guidelines (linked in invite description), prepare your 30-second intro, bring job search updates, identify 2–3 people to follow up with.</div>
        <div class="cal-meta"><strong>Also on calendar as:</strong> "Network" — same time slot, personal reminder.</div>
      </div>
    </div>
    <div class="cal-event" style="background:#faf5ff">
      <div class="cal-time">3:00 PM – 4:00 PM</div>
      <div class="cal-details">
        <div class="cal-name">💅 Nails</div>
        <div class="cal-meta">📍 No location provided</div>
        <div class="cal-meta"><span class="cal-status status-confirmed">✅ Confirmed</span></div>
        <div class="cal-meta" style="margin-top:4px"><em>Note: Two "Nails" events this week — Aug 25 at 4:30 PM and Aug 26 at 3:00 PM. Confirm which is correct.</em></div>
      </div>
    </div>
  </div>

  <!-- THU AUG 27 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Thursday, August 27, 2026</div>
    <div class="cal-event" style="background:#faf5ff">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="cal-name">🎂 Christian H's Birthday</div>
        <div class="cal-meta"><span class="cal-status status-confirmed">✅ Confirmed</span> &nbsp; Send a message or card.</div>
      </div>
    </div>
    <div class="cal-event" style="background:#fff5f5">
      <div class="cal-time">9:00 AM – 10:30 AM</div>
      <div class="cal-details">
        <div class="cal-name">🎙️ Executive Roundtable (Declined)</div>
        <div class="cal-meta">📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> | Hosted by: John Madigan</div>
        <div class="cal-meta"><span class="cal-status status-declined">❌ Declined</span></div>
        <div class="cal-meta" style="margin-top:4px">You have declined this event. No action needed unless you wish to reconsider — given active job search, this type of executive networking may be worth attending.</div>
      </div>
    </div>
    <div class="cal-event" style="background:#ebf8ff">
      <div class="cal-time">12:00 PM – 1:00 PM</div>
      <div class="cal-details">
        <div class="cal-name">🤝 HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
        <div class="cal-meta">📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a></div>
        <div class="cal-meta"><span class="cal-status status-needs">⏳ RSVP Needed</span> &nbsp; 190+ attendees | Open discussion format — no AI notetaking</div>
        <div class="cal-meta" style="margin-top:4px"><strong>Prep needed:</strong> Bring specific questions or challenges for open discussion. This is an informal peer support forum — great for real-time job search coaching.</div>
      </div>
    </div>
  </div>

  <!-- FRI AUG 28 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Friday, August 28, 2026</div>
    <div class="cal-event">
      <div class="cal-time">All Day</div>
      <div class="cal-details">
        <div class="cal-name">No events scheduled</div>
        <div class="cal-meta">Use this day for job application follow-ups or rest.</div>
      </div>
    </div>
  </div>

</div>

<!-- ══════════════════════════════════════════════════════════════
     SECTION 5: JOB SEARCH & INTERVIEW PIPELINE
══════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="section-number">5</span> Job Search &amp; Interview Pipeline</div>

  <div class="group-header">🏆 High Fit Opportunities</div>

  <div class="job-card">
    <div class="job-header">
      <div>
        <div class="job-title">Vice President, Human Resources Business Partner</div>
        <div class="job-co">PeopleOps Jobs — via LinkedIn Job Alerts</div>
      </div>
      <span class="tag tag-green">HIGH FIT</span>
    </div>
    <div class="job-meta">📧 Source: LinkedIn Job Alerts (jobalerts-noreply@linkedin.com) | Received: Sat Aug 22, 3:05 AM</div>
    <div class="job-meta">📍 Location: Not specified | 🏢 Company: PeopleOps Jobs (HRBP-focused firm)</div>
    <div class="job-meta" style="margin-top:6px">✅ Direct match to Melissa's HR leadership background. PeopleOps Jobs is an HR-specific job board/agency. Senior HRBP VP role — apply immediately.</div>
    <div class="action-row" style="margin-top:8px"><span class="tag tag-green">Apply Today</span><span class="tag tag-blue">Use SignalHire Credits</span></div>
  </div>

  <div class="job-card">
    <div class="job-header">
      <div>
        <div class="job-title">Senior People Operations Manager</div>
        <div class="job-co">Mixpanel — via Indeed</div>
      </div>
      <span class="tag tag-green">HIGH FIT</span>
    </div>
    <div class="job-header" style="margin-top:4px">
    </div>
    <div class="job-meta">📧 Source: Indeed (via Apple Private Relay) | Received: Sat Aug 22, 1:38 AM</div>
    <div class="job-meta">📍 Location: Not specified | 🏢 Company: Mixpanel (analytics SaaS)</div>
    <div class="job-meta" style="margin-top:6px">✅ "Background could be a match" per Indeed. PeopleOps manager role at a tech company — aligns with Melissa's profile. Submit quick application.</div>
    <div class="action-row" style="margin-top:8px"><span class="tag tag-green">Apply Today</span></div>
  </div>

  <div class="job-card">
    <div class="job-header">
      <div>
        <div class="job-title">Head of HR</div>
        <div class="job-co">WHS Inc. (Willow Telehealth) — via LinkedIn Job Alerts</div>
      </div>
      <span class="tag tag-green">HIGH FIT</span>
    </div>
    <div class="job-meta">📧 Source: LinkedIn Job Alerts | Received: Sat Aug 22, 5:05 AM</div>
    <div class="job-meta">📍 Location: Not specified | 🏢 Company: Willow Telehealth (WHS Inc.)</div>
    <div class="job-meta" style="margin-top:6px">✅ Head of HR at a telehealth company — high-growth sector. Strong leadership mandate. Worth prioritizing alongside VP role.</div>
    <div class="action-row" style="margin-top:8px"><span class="tag tag-green">Apply This Weekend</span></div>
  </div>

  <div class="group-header">📋 Medium Fit Opportunities</div>

  <div class="job-card">
    <div class="job-header">
      <div>
        <div class="job-title">Director, Human Resources + 8 More Remote Roles</div>
        <div class="job-co">Smart Electric Power Alliance + others — via Glassdoor</div>
      </div>
      <span class="tag tag-yellow">MEDIUM FIT</span>
    </div>
    <div class="job-meta">📧 Source: Glassdoor | Received: Sat Aug 22, 1:44 AM | 📍 Remote, US</div>
    <div class="job-meta" style="margin-top:6px">Director-level HR role in clean energy sector — niche industry but strong leadership opportunity. Review all 9 listings in the digest for fit.</div>
    <div class="action-row" style="margin-top:8px"><span class="tag tag-yellow">Review This Weekend</span></div>
  </div>

  <div class="job-card">
    <div class="job-header">
      <div>
        <div class="job-title">Chief People Officer / Lead Talent Culture Change Roles (5 matches)</div>
        <div class="job-co">JobLeads — Saved Search Alert</div>
      </div>
      <span class="tag tag-yellow">MEDIUM FIT</span>
    </div>
    <div class="job-meta">📧 Source: JobLeads (mailer@jobleads.com) — in Trash | Received: Sat Aug 22, 12:37 PM</div>
    <div class="job-meta" style="margin-top:6px">CPO-level roles from Melissa's saved search. Currently in trash (newsletter auto-trashed). Worth retrieving to review the 5 listings.</div>
    <div class="action-row" style="margin-top:8px"><span class="tag tag-yellow">Retrieve from Trash</span></div>
  </div>

  <div class="group-header">🤝 Networking &amp; Recruiter Activity</div>

  <div class="job-card">
    <div class="job-header">
      <div>
        <div class="job-title">Recruiter Call — Monday Aug 24, 9:30 AM (⚠️ Conflicts with Hair Appt)</div>
        <div class="job-co">Unknown Recruiter — Google Calendar</div>
      </div>
      <span class="tag tag-red">CONFLICT!</span>
    </div>
    <div class="job-meta">⚠️ This call overlaps with hair appointment (9:15–10:45 AM). Resolve scheduling conflict today.</div>
  </div>

  <div class="job-card">
    <div class="job-header">
      <div>
        <div class="job-title">HR Networking &amp; Job Search Group — Wed Aug 26 + Thu Aug 27</div>
        <div class="job-co">190+ HR Professionals — Zoom</div>
      </div>
      <span class="tag tag-blue">RSVP NEEDED</span>
    </div>
    <div class="job-meta">Two sessions: Wed 12–1:30 PM (group session) | Thu 12–1:00 PM (open office hours)</div>
    <div class="job-meta" style="margin-top:4px">Large HR peer network — high value for referrals, leads, and mutual support. RSVP to both sessions.</div>
  </div>

  <div class="job-card">
    <div class="job-header">
      <div>
        <div class="job-title">Sarah S (Founder's Office, decube) wants to connect on LinkedIn</div>
        <div class="job-co">LinkedIn — Inbox</div>
      </div>
      <span class="tag tag-yellow">REVIEW</span>
    </div>
    <div class="job-meta">Inbound connection from someone at a startup's Founder's Office. Worth researching decube before accepting.</div>
  </div>

  <div class="job-card">
    <div class="job-header">
      <div>
        <div class="job-title">Mario Linale — New LinkedIn Connection Accepted</div>
        <div class="job-co">LinkedIn — Inbox</div>
      </div>
      <span class="tag tag-gray">NOTE</span>
    </div>
    <div class="job-meta">Mario accepted your invitation. Review his profile and explore mutual connections for warm introductions.</div>
  </div>

  <div class="job-card">
    <div class="job-header">
      <div>
        <div class="job-title">5 New SignalHire Contact Credits</div>
        <div class="job-co">SignalHire — Inbox</div>
      </div>
      <span class="tag tag-green">USE NOW</span>
    </div>
    <div class="job-meta">Credits just refreshed — use to find recruiter/hiring manager contact info for the VP HRBP, Head of HR, and Sr. PeopleOps roles above.</div>
  </div>

  <div class="group-header">🛠️ Job Search Tools &amp; Prep (Self-Sent)</div>

  <div class="job-card">
    <div class="job-header">
      <div>
        <div class="job-title">Interview Answer Engineering Prompt</div>
        <div class="job-co">Self-sent by Melissa W — Inbox</div>
      </div>
      <span class="tag tag-purple">TOOL</span>
    </div>
    <div class="job-meta">AI coaching prompt for interview prep. Use before Monday's recruiter call. "Act as a hiring manager and interview coach..."</div>
  </div>

  <div class="job-card">
    <div class="job-header">
      <div>
        <div class="job-title">LinkedIn Optimization Prompt + The Claude-Only Operator Stack</div>
        <div class="job-co">Self-sent by Melissa W — Inbox (×3 total)</div>
      </div>
      <span class="tag tag-purple">TOOL</span>
    </div>
    <div class="job-meta">LinkedIn rewrite prompt + Notion resource link (sent twice). Use the optimization prompt to update your profile this weekend while Gemini AI is now available.</div>
  </div>

</div>

<!-- ══════════════════════════════════════════════════════════════
     SECTION 6: FULL EMAIL REVIEW BY CATEGORY
══════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="section-number">6</span> Full Email Review by Category</div>

  <!-- SECURITY / RISK -->
  <div class="card band-red" style="margin-bottom:14px; padding:16px 20px">
    <div class="card-title" style="color:#c53030">🔴 Security / Risk — 5 Emails (All Auto-Trashed as Phishing)</div>
    <div class="card-sub">All 5 emails below were automatically trashed before reaching Melissa. No further action required beyond awareness.</div>
    <div class="table-wrap" style="margin-top:10px">
      <table>
        <thead><tr><th>Email ID</th><th>Fake Sender</th><th>Subject Summary</th><th>Threat Type</th></tr></thead>
        <tbody>
          <tr>
            <td>1a0290c9c79a6461</td>
            <td>"SiriusXM.Team" via random domain</td>
            <td>Your account will be removed today — SiriusXM (Version 1)</td>
            <td><span class="phishing-badge">Phishing — Payment/Credential Harvest</span></td>
          </tr>
          <tr>
            <td>1a027f6188abfd99</td>
            <td>"Payment-Declined" via random domain</td>
            <td>Your Account SiriusXM Will Be Removed Today (Version 2)</td>
            <td><span class="phishing-badge">Phishing — Duplicate Campaign</span></td>
          </tr>
          <tr>
            <td>1a02817ec6c3a526</td>
            <td>"Cloud_Storage" via random domain</td>
            <td>Action Required: Storage 100% Full</td>
            <td><span class="phishing-badge">Phishing — Fake Storage Alert</span></td>
          </tr>
          <tr>
            <td>1a027c1aa2e2becb</td>
            <td>melissaw212 (spoofed self) via random domain</td>
            <td>We've blocked your account — photos will be deleted</td>
            <td><span class="phishing-badge">Phishing — Self-Spoof / Credential Harvest</span></td>
          </tr>
          <tr>
            <td>1a028851a3c5b8a7</td>
            <td>"CashApp" via random domain</td>
            <td>Garbled subject — Royal Casino/Cash App prize scam</td>
            <td><span class="phishing-badge">Phishing — Casino Scam</span></td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="note-box" style="margin-top:10px">⚠️ Your email address (melissaw212@gmail.com) is being actively targeted by multiple phishing campaigns today. Consider enabling Google's Advanced Protection Program or reviewing spam filter strength.</div>
  </div>

  <!-- JOB SEARCH -->
  <div class="card band-green" style="margin-bottom:14px; padding:16px 20px">
    <div class="card-title" style="color:#276749">🟢 Job Search — 7 Emails</div>
    <div class="table-wrap" style="margin-top:10px">
      <table>
        <thead><tr><th>From</th><th>Role/Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>LinkedIn Job Alerts</td><td>VP, HR Business Partner — PeopleOps Jobs</td><td><span class="tag tag-green">INBOX</span></td><td>Apply ASAP</td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>Head of HR — WHS Inc. (Willow Telehealth)</td><td><span class="tag tag-green">INBOX (not in trash)</span></td><td>Apply this weekend</td></tr>
          <tr><td>Indeed</td><td>Senior People Operations Manager — Mixpanel</td><td><span class="tag tag-green">INBOX</span></td><td>Apply ASAP</td></tr>
          <tr><td>Glassdoor</td><td>Director, HR + 8 Remote roles (Smart Electric Power Alliance)</td><td><span class="tag tag-yellow">Trashed — newsletter</span></td><td>Review digest</td></tr>
          <tr><td>Glassdoor</td><td>Community Manager at Twin Pines + 7 NY roles</td><td><span class="tag tag-gray">Trashed</span></td><td>Lower fit — skip</td></tr>
          <tr><td>JobLeads</td><td>5 CPO / Talent / Culture roles</td><td><span class="tag tag-yellow">Trashed — newsletter</span></td><td>Retrieve &amp; review</td></tr>
          <tr><td>Alison Courses</td><td>Career change / lifesaving careers promo</td><td><span class="tag tag-gray">Trashed</span></td><td>Delete — low relevance</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- RECRUITERS / NETWORKING -->
  <div class="card band-green" style="margin-bottom:14px; padding:16px 20px">
    <div class="card-title" style="color:#276749">🟢 Recruiters &amp; Networking — 4 Emails</div>
    <div class="table-wrap" style="margin-top:10px">
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Sarah S via LinkedIn</td><td>Melissa A, I'd like to connect — Founder's Office, decube</td><td><span class="tag tag-blue">INBOX</span></td><td>Research decube, then accept/decline</td></tr>
          <tr><td>Mario Linale via LinkedIn</td><td>Mario accepted your invitation</td><td><span class="tag tag-blue">INBOX</span></td><td>Visit profile, explore connections</td></tr>
          <tr><td>SignalHire</td><td>5 new contact credits added</td><td><span class="tag tag-blue">INBOX</span></td><td>Use on target hiring managers now</td></tr>
          <tr><td>LinkedIn</td><td>Someone at Business LEAP you may know (Senior Payroll &amp; Tax Manager)</td><td><span class="tag tag-gray">Trashed</span></td><td>Low relevance — skip</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- CALENDAR / EVENTS / PROFESSIONAL DEV -->
  <div class="card band-purple" style="margin-bottom:14px; padding:16px 20px">
    <div class="card-title" style="color:#553c9a">🟣 Professional Development &amp; Events — 3 Emails</div>
    <div class="table-wrap" style="margin-top:10px">
      <table>
        <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td>Zoom (no-reply@zoom.us)</td>
            <td>
