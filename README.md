<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Melissa's Daily Briefing – Wednesday, June 3, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 15px; line-height: 1.6; }
  .wrapper { max-width: 860px; margin: 0 auto; padding: 20px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #0d1b4b 0%, #1a2f7a 100%); color: white; padding: 36px 32px; border-radius: 14px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .date { font-size: 16px; opacity: 0.8; margin-top: 6px; }
  .header .subtitle { font-size: 13px; opacity: 0.6; margin-top: 4px; letter-spacing: 1px; text-transform: uppercase; }

  /* SECTION HEADERS */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 19px; font-weight: 700; color: #0d1b4b; border-left: 5px solid #1a2f7a; padding-left: 12px; margin-bottom: 14px; text-transform: uppercase; letter-spacing: 0.5px; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; border-left: 5px solid; }
  .card-red    { background: #fff5f5; border-color: #e53e3e; }
  .card-yellow { background: #fffdf0; border-color: #d69e2e; }
  .card-blue   { background: #f0f6ff; border-color: #3182ce; }
  .card-green  { background: #f0fff4; border-color: #38a169; }
  .card-purple { background: #faf5ff; border-color: #805ad5; }
  .card-gray   { background: #f7f7f7; border-color: #a0aec0; }
  .card-orange { background: #fffaf0; border-color: #dd6b20; }

  .card .label { display: inline-block; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; padding: 2px 8px; border-radius: 20px; margin-bottom: 6px; }
  .label-red    { background: #fed7d7; color: #c53030; }
  .label-yellow { background: #fefcbf; color: #975a16; }
  .label-blue   { background: #bee3f8; color: #2b6cb0; }
  .label-green  { background: #c6f6d5; color: #276749; }
  .label-purple { background: #e9d8fd; color: #6b46c1; }
  .label-gray   { background: #e2e8f0; color: #4a5568; }
  .label-orange { background: #fbd38d; color: #7b341e; }

  .card .title { font-size: 15px; font-weight: 700; color: #1a202c; margin-bottom: 4px; }
  .card .source { font-size: 12px; color: #718096; margin-bottom: 6px; }
  .card .body { font-size: 14px; color: #2d3748; margin-bottom: 8px; }
  .card .next-step { font-size: 13px; font-weight: 600; color: #2b6cb0; }
  .card .next-step span { background: #ebf8ff; padding: 2px 8px; border-radius: 4px; }

  /* EXECUTIVE SUMMARY */
  .exec-summary { background: linear-gradient(135deg, #1a2f7a, #2d4aad); color: white; border-radius: 12px; padding: 24px 28px; margin-bottom: 28px; }
  .exec-summary h2 { font-size: 17px; font-weight: 700; margin-bottom: 14px; text-transform: uppercase; letter-spacing: 1px; opacity: 0.9; }
  .exec-summary ul { list-style: none; }
  .exec-summary ul li { padding: 6px 0; padding-left: 24px; position: relative; font-size: 14px; }
  .exec-summary ul li::before { content: "▶"; position: absolute; left: 0; opacity: 0.7; font-size: 10px; top: 9px; }

  /* CALENDAR TABLE */
  .cal-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .cal-table th { background: #0d1b4b; color: white; padding: 10px 12px; text-align: left; }
  .cal-table td { padding: 10px 12px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  .cal-table tr:nth-child(even) td { background: #f7fafc; }
  .cal-table .day-header td { background: #ebf4ff; font-weight: 700; color: #1a2f7a; font-size: 13px; }
  .status-accepted  { color: #276749; font-weight: 700; }
  .status-declined  { color: #c53030; font-weight: 700; }
  .status-pending   { color: #975a16; font-weight: 700; }
  .status-confirmed { color: #276749; font-weight: 700; }
  .conflict-badge   { background: #fed7d7; color: #c53030; font-size: 11px; font-weight: 700; padding: 2px 6px; border-radius: 4px; }

  /* EMAIL ACCOUNTING TABLE */
  .acct-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .acct-table th { background: #0d1b4b; color: white; padding: 10px 12px; text-align: left; }
  .acct-table td { padding: 9px 12px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  .acct-table tr:nth-child(even) td { background: #f7fafc; }
  .acct-table .total-row td { font-weight: 700; background: #ebf4ff; }

  /* ACTION ITEMS TABLE */
  .action-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .action-table th { background: #1a2f7a; color: white; padding: 10px 12px; text-align: left; }
  .action-table td { padding: 9px 12px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  .action-table tr:nth-child(even) td { background: #f7fafc; }
  .pri-1 { color: #c53030; font-weight: 700; }
  .pri-2 { color: #975a16; font-weight: 700; }
  .pri-3 { color: #276749; font-weight: 700; }

  /* TOP 3 */
  .top3 { background: linear-gradient(135deg, #0d1b4b, #1a2f7a); color: white; border-radius: 12px; padding: 24px 28px; margin-bottom: 28px; }
  .top3 h2 { font-size: 17px; font-weight: 700; margin-bottom: 14px; text-transform: uppercase; letter-spacing: 1px; }
  .top3-item { display: flex; align-items: flex-start; gap: 14px; padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.1); }
  .top3-item:last-child { border-bottom: none; }
  .top3-num { font-size: 28px; font-weight: 900; opacity: 0.3; line-height: 1; min-width: 36px; }
  .top3-text h3 { font-size: 15px; font-weight: 700; margin-bottom: 3px; }
  .top3-text p { font-size: 13px; opacity: 0.8; }

  /* PROMO GROUP */
  .promo-group { background: #f7f7f7; border-radius: 10px; padding: 14px 18px; margin-bottom: 10px; }
  .promo-group .brand { font-weight: 700; font-size: 14px; color: #2d3748; }
  .promo-group .subject { font-size: 13px; color: #4a5568; }
  .promo-group .rec { font-size: 12px; font-weight: 700; margin-top: 4px; }
  .rec-delete  { color: #c53030; }
  .rec-keep    { color: #276749; }
  .rec-review  { color: #975a16; }
  .rec-ignore  { color: #718096; }

  .divider { border: none; border-top: 2px solid #e2e8f0; margin: 24px 0; }
  .section-footer { font-size: 13px; font-weight: 600; color: #4a5568; background: #edf2f7; padding: 8px 14px; border-radius: 6px; margin-top: 10px; }

  .trash-badge { display: inline-block; background: #fed7d7; color: #c53030; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 10px; margin-left: 6px; text-transform: uppercase; }
  .restore-badge { display: inline-block; background: #c6f6d5; color: #276749; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 10px; }
  .safe-del-badge { display: inline-block; background: #fed7d7; color: #c53030; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 10px; }
  .review-badge { display: inline-block; background: #fefcbf; color: #975a16; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 10px; }

  a { color: #3182ce; }
  @media (max-width: 600px) {
    .wrapper { padding: 10px; }
    .header { padding: 22px 16px; }
    .header h1 { font-size: 22px; }
    .cal-table, .acct-table, .action-table { font-size: 12px; }
  }
</style>
</head>
<body>
<div class="wrapper">

  <!-- ═══════════════════════════════════════════ -->
  <!-- 1. HEADER -->
  <!-- ═══════════════════════════════════════════ -->
  <div class="header">
    <div class="subtitle">Executive Chief of Staff Briefing</div>
    <h1>Good morning, Melissa ☀️</h1>
    <div class="date">Wednesday, June 3, 2026 &nbsp;·&nbsp; 50 emails reviewed &nbsp;·&nbsp; 10 calendar events this week</div>
  </div>

  <!-- ═══════════════════════════════════════════ -->
  <!-- 2. EXECUTIVE SUMMARY -->
  <!-- ═══════════════════════════════════════════ -->
  <div class="exec-summary">
    <h2>⚡ Executive Summary</h2>
    <ul>
      <li><strong>🔴 Security Alert:</strong> Your LinkedIn password was reset and a PIN was sent — verify this was you and check for unauthorized access immediately. Multiple phishing/scam emails also received today.</li>
      <li><strong>📅 Tomorrow is busy:</strong> You have 3 calendar events on June 4th — including an Executive Roundtable you <em>declined</em>, a Dr. Husk appointment at 10:30 AM, and an HR Networking session at noon (RSVP still pending).</li>
      <li><strong>💼 Job search active:</strong> A LinkedIn job alert landed for Senior Director, HR Business Partner (AI-Native). Networking call with Netta Jenkins confirmed for June 9th. PSC Spring Social is cancelled — check next event.</li>
    </ul>
  </div>

  <!-- ═══════════════════════════════════════════ -->
  <!-- 3. ACTION REQUIRED -->
  <!-- ═══════════════════════════════════════════ -->
  <div class="section">
    <div class="section-title">🔴 Action Required</div>

    <div class="card card-red">
      <div class="label label-red">🔐 Security — Urgent</div>
      <div class="title">LinkedIn Password Reset + PIN Sent</div>
      <div class="source">From: LinkedIn &lt;security-noreply@linkedin.com&gt; · Wed June 3, 9:16 PM &amp; 9:17 PM</div>
      <div class="body">LinkedIn sent two security emails in quick succession: a verification PIN (606210) and a confirmation that your password was successfully reset. If you did not initiate this, your account may have been compromised. Even if you did reset it, confirm no unauthorized sessions exist.</div>
      <div class="next-step">→ Next Step: <span>Log into LinkedIn NOW, check active sessions under Settings &gt; Security, and enable two-factor authentication if not already on.</span></div>
    </div>

    <div class="card card-red">
      <div class="label label-red">⚠️ Phishing/Scam — Delete</div>
      <div class="title">"Cloud Account Locked" Extortion Email</div>
      <div class="source">From: 'Payment_Declined' &lt;xbtcsupportmd@wcknlkzajfzzlhmducymgdwi.com&gt; · Wed June 3</div>
      <div class="body">Fake alert claiming your cloud subscription expired and photos/videos will be deleted. Suspicious sender domain, urgency tactics — classic phishing. Do NOT click any links.</div>
      <div class="next-step">→ Next Step: <span>Mark as spam and delete. Do not engage.</span></div>
    </div>

    <div class="card card-red">
      <div class="label label-red">⚠️ Scam — Delete</div>
      <div class="title">Casino Yabby "NGR Bonus" Payment Scam</div>
      <div class="source">From: 💲Casino_Yabby💲 &lt;tfvrniyohli@fknm.iwebcsruiikul.us&gt; · Wed June 3</div>
      <div class="body">Fake payment of $13,963.99 claimed to be ready for confirmation. Spoofed sender, gibberish domain. This is a financial scam — do not confirm anything.</div>
      <div class="next-step">→ Next Step: <span>Delete immediately. Report as phishing.</span></div>
    </div>

    <div class="card card-red">
      <div class="label label-red">⚠️ Scam — Delete</div>
      <div class="title">Casino "130 Free Spins" Spam</div>
      <div class="source">From: 📣melissaw212 &lt;gudvuwhjjks@lmsw.wucbgfmxbenbv.us&gt; · Wed June 3</div>
      <div class="body">Spoofed sender using your own email handle. "Limitless VIP" assignment. Fake gambling offer. Your email address is being used in spam loops — a sign of address exposure.</div>
      <div class="next-step">→ Next Step: <span>Delete. Consider updating your Gmail spam filters and checking haveibeenpwned.com.</span></div>
    </div>

    <div class="card card-yellow">
      <div class="label label-yellow">📅 RSVP Needed</div>
      <div class="title">HR Networking &amp; Job Search — Open Office Hours (June 4, 12–1 PM)</div>
      <div class="source">Calendar Event · Status: Needs Action</div>
      <div class="body">You have not responded to this Zoom networking session scheduled for tomorrow at noon. With 170+ attendees invited, this is a large group session — valuable for job search networking.</div>
      <div class="next-step">→ Next Step: <span>RSVP Accept or Decline on your calendar before tomorrow morning.</span></div>
    </div>

    <div class="card card-yellow">
      <div class="label label-yellow">💬 Follow-Up Sent</div>
      <div class="title">Contact Question / Jade — Appointment Moved to the 10th</div>
      <div class="source">From: melissa &lt;melissaw212@gmail.com&gt; · Wed June 3, 1:59 PM (Sent)</div>
      <div class="body">You replied to Jade confirming you moved your appointment to June 10th and will check in late Monday or Tuesday to see if something arrived.</div>
      <div class="next-step">→ Next Step: <span>Add a reminder to follow up with Jade on Monday June 8 or Tuesday June 9.</span></div>
    </div>

    <div class="card card-yellow">
      <div class="label label-yellow">💰 Billing Due Soon</div>
      <div class="title">State Farm Bill Due — June 7</div>
      <div class="source">Google Calendar · All-day event June 7</div>
      <div class="body">State Farm bill payment reminder on your calendar for Saturday, June 7.</div>
      <div class="next-step">→ Next Step: <span>Schedule or confirm payment before June 7.</span></div>
    </div>

    <div class="card card-yellow">
      <div class="label label-yellow">🌐 Usage Alert</div>
      <div class="title">Netlify — 75% of Credits Used on Morning Briefing Project</div>
      <div class="source">From: Netlify &lt;team@netlify.com&gt; · Wed June 3, 9:28 PM (in Trash)</div>
      <div class="body">Your Netlify team "morning briefing" has consumed 750 of 1,000 credits this billing cycle. At the current pace you may hit the limit before the cycle ends.</div>
      <div class="next-step">→ Next Step: <span>Review Netlify usage dashboard. Consider upgrading or optimizing to avoid service interruption.</span></div>
    </div>

    <div class="section-footer">✅ Action: Address LinkedIn security first. Then RSVP tomorrow's networking session. Pay State Farm by June 7. Delete all scam emails.</div>
  </div>

  <hr class="divider">

  <!-- ═══════════════════════════════════════════ -->
  <!-- 4. TODAY'S SCHEDULE + PREP -->
  <!-- ═══════════════════════════════════════════ -->
  <div class="section">
    <div class="section-title">📅 Today's Schedule — Wednesday, June 3</div>
    <div class="card card-gray">
      <div class="label label-gray">No Events Today</div>
      <div class="title">Wednesday June 3 — No calendar events scheduled</div>
      <div class="body">Your calendar is clear today. Use this time to address security items, process email, and prep for tomorrow's busy schedule.</div>
    </div>
    <div class="section-footer">✅ Use today to: secure LinkedIn, RSVP for June 4 networking, prep for Dr. Husk appt tomorrow.</div>
  </div>

  <hr class="divider">

  <!-- ═══════════════════════════════════════════ -->
  <!-- 5. JOB SEARCH + INTERVIEW PIPELINE -->
  <!-- ═══════════════════════════════════════════ -->
  <div class="section">
    <div class="section-title">💼 Job Search + Interview Pipeline</div>

    <div class="card card-green">
      <div class="label label-green">🟢 Job Alert</div>
      <div class="title">Senior Director, HR Business Partner (AI-Native) — RemoteHunter</div>
      <div class="source">From: LinkedIn Job Alerts &lt;jobalerts-noreply@linkedin.com&gt; · Wed June 3, 9:05 PM</div>
      <div class="body">LinkedIn flagged a role that matches your profile: Senior Director, HR Business Partner with an AI-Native focus at RemoteHunter. This aligns with your HR leadership background and the AI-forward market shift.</div>
      <div class="next-step">→ Next Step: <span>Open LinkedIn and review the full posting. Apply if it fits your target criteria.</span></div>
    </div>

    <div class="card card-green">
      <div class="label label-green">📞 Confirmed Meeting</div>
      <div class="title">Melissa x Netta Jenkins — 15-Min Consultation (June 9, 12:00–12:15 PM)</div>
      <div class="source">Google Calendar · Zoom · Status: Accepted</div>
      <div class="body">You have a confirmed 15-minute Zoom consultation with Netta Jenkins from HIC Consult. Short window — prepare your key questions and talking points in advance. Zoom password: 424726.</div>
      <div class="next-step">→ Next Step: <span>Prep 2–3 focused questions for Netta. Have your resume/LinkedIn ready to reference.</span></div>
    </div>

    <div class="card card-green">
      <div class="label label-green">🌐 LinkedIn Invite</div>
      <div class="title">Connection Request from Ilya Volovnik, Founder &amp; CEO — Vorex Intelligence Group</div>
      <div class="source">From: LinkedIn &lt;invitations@linkedin.com&gt; · Wed June 3, 7:05 PM</div>
      <div class="body">Ilya Volovnik, a Founder &amp; CEO, is waiting for your connection response. Could be a valuable contact given your job search — worth reviewing his profile before accepting.</div>
      <div class="next-step">→ Next Step: <span>Review Ilya's LinkedIn profile. Accept if he's in your target industry.</span></div>
    </div>

    <div class="card card-yellow">
      <div class="label label-yellow">🤝 Networking Event</div>
      <div class="title">HR Networking &amp; Job Search: Open Office Hours (June 4, 12–1 PM)</div>
      <div class="source">Google Calendar · Zoom · Status: Needs Action</div>
      <div class="body">Large group networking call tomorrow at noon with 170+ HR professionals. Open discussion format. Note: automated notetaking AI tools are not permitted. Good opportunity for job search connections.</div>
      <div class="next-step">→ Next Step: <span>RSVP and prepare a brief personal introduction and 1–2 networking goals.</span></div>
    </div>

    <div class="card card-yellow">
      <div class="label label-yellow">🤝 Networking Event</div>
      <div class="title">HR Networking &amp; Job Search Group — Zoom 2 (June 10, 12–1:30 PM)</div>
      <div class="source">Google Calendar · Zoom · Status: Needs Action</div>
      <div class="body">A second HR networking group session next Wednesday from 12:00–1:30 PM. Same group, large attendee list. Conflicts with "Melissa x Meg Drinks" which starts at 1 PM — overlap risk if this runs long.</div>
      <div class="next-step">→ Next Step: <span>RSVP and flag the 1 PM conflict with Meg drinks. Consider the overlap carefully.</span></div>
    </div>

    <div class="card card-yellow">
      <div class="label label-yellow">🤝 Networking</div>
      <div class="title">Melissa x Meg Drinks (June 10, 1–2 PM) — Location TBC</div>
      <div class="source">Google Calendar · Status: Needs Action · Attendee: megpark@oakleafpartnership.com</div>
      <div class="body">Informal drinks with Meg from Oakleaf Partnership. Location still TBC. Conflicts with HR Networking Zoom ending at 1:30 PM.</div>
      <div class="next-step">→ Next Step: <span>Confirm location with Meg. Adjust timing to avoid conflict with the 12–1:30 networking call.</span></div>
    </div>

    <div class="card card-purple">
      <div class="label label-purple">📣 PSC Event Cancelled</div>
      <div class="title">People Strategy Collective — Spring Social Cancelled (Was Tomorrow, June 4)</div>
      <div class="source">From: People Strategy Collective &lt;membership@mg.peoplestrategycollective.org&gt; · Wed June 3, 6:40 PM</div>
      <div class="body">PSC's Spring Social scheduled for tomorrow is cancelled. Next event is Tuesday, July (date not specified in snippet). No action needed beyond noting this on your calendar.</div>
      <div class="next-step">→ Next Step: <span>Note PSC July event when details arrive. No action needed today.</span></div>
    </div>

    <div class="card card-purple">
      <div class="label label-purple">💡 Virtual Event Reminder</div>
      <div class="title">Virtual Think IT Event — June 17 (York Solutions)</div>
      <div class="source">From: Quinn Tice &lt;qtice@yorksolutions.net&gt; · Wed June 3, 6:05 PM</div>
      <div class="body">Reminder about a virtual Think IT event on Wednesday, June 17 covering building a high-functioning engineering culture. Professional development angle — worth attending if it applies to your HR/leadership work.</div>
      <div class="next-step">→ Next Step: <span>Review full details and add June 17 to your calendar if interested.</span></div>
    </div>

    <div class="section-footer">✅ Act: Apply to RemoteHunter role. RSVP June 4 networking. Prep for Netta Jenkins call June 9. Confirm Meg drinks timing.</div>
  </div>

  <hr class="divider">

  <!-- ═══════════════════════════════════════════ -->
  <!-- 6. IMPORTANT EMAILS -->
  <!-- ═══════════════════════════════════════════ -->
  <div class="section">
    <div class="section-title">📬 Important Emails — Professional &amp; Personal</div>

    <div class="card card-purple">
      <div class="label label-purple">📚 Professional Development</div>
      <div class="title">Transform: "Tech Fatigue is Real — How to Lead Organized, Effective Change"</div>
      <div class="source">From: Transform &lt;community@transform.us&gt; · Wed June 3, 8:54 PM</div>
      <div class="body">Article posted in the New York City Chapter of Transform about managing tech fatigue and leading change in organizations. Relevant to your HR leadership and change management background.</div>
      <div class="next-step">→ Next Step: <span>Read when you have 10 minutes. Good content to reference in interviews.</span></div>
    </div>

    <div class="card card-purple">
      <div class="label label-purple">📚 HR Research</div>
      <div class="title">HR.com Research Survey — Total Rewards &amp; Compensation Strategy</div>
      <div class="source">From: Research Institute at HR.com &lt;research@research.hr.com&gt; · Wed June 3, 8:23 PM</div>
      <div class="body">Survey asking HR leaders if their compensation and total rewards strategy is strong enough to retain top talent. Quick survey — could position you as a thought leader in HR.com research findings.</div>
      <div class="next-step">→ Next Step: <span>Review and complete the survey if it takes under 5 minutes. Good for professional visibility.</span></div>
    </div>

    <div class="card card-purple">
      <div class="label label-purple">📚 HR Webcast</div>
      <div class="title">HR.com — "The End of Bundled Maternity Care" Webcast, June 24, 2026</div>
      <div class="source">From: Rhonda from HR.com &lt;info@events.hr.com&gt; · Wed June 3, 6:49 PM</div>
      <div class="body">Free webcast on upcoming changes to maternity care billing and adapting benefits strategy for 2027. Relevant if you work in or are targeting Total Rewards / Benefits leadership roles.</div>
      <div class="next-step">→ Next Step: <span>Register if benefits is in your portfolio. It's free and on June 24.</span></div>
    </div>

    <div class="card card-purple">
      <div class="label label-purple">📚 Research Alert</div>
      <div class="title">Mobius Engine Hub — "Resilience Tested: Navigating Job Market Decline"</div>
      <div class="source">From: Ashwin &lt;ashwin@mobiusenginehub.com&gt; · Wed June 3, 6:42 PM</div>
      <div class="body">New research publication on navigating competitive job market conditions and evolving job roles. Useful context for your own job search strategy and conversations with hiring managers.</div>
      <div class="next-step">→ Next Step: <span>Skim the research. Incorporate insights into your job search narrative if relevant.</span></div>
    </div>

    <div class="card card-purple">
      <div class="label label-purple">🗓️ EEO Training</div>
      <div class="title">Eventbrite — Workplace EEO Investigator Training MD-110, Nov 3–6, 2026 (Virtual)</div>
      <div class="source">From: Eventbrite &lt;noreply@reminder.eventbrite.com&gt; · Wed June 3, 8:36 PM (Trash)</div>
      <div class="body">Amediate, LLC added a new virtual EEO Investigator Training (MD-110 format) for November 3–6. If you do EEO work or want to add a credential, this is worth bookmarking early — it was in your trash.</div>
      <div class="next-step">→ Next Step: <span>Restore from trash and save the link. Registration for November may fill up.</span></div>
    </div>

    <div class="card card-blue">
      <div class="label label-blue">🔧 Tool Tip</div>
      <div class="title">
