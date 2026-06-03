<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Melissa's Daily Briefing – Wednesday, June 3, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 15px; line-height: 1.6; }
  .wrapper { max-width: 860px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #0d1b4b 0%, #1a2f7a 100%); color: #fff; border-radius: 14px; padding: 36px 32px; margin-bottom: 28px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .date { font-size: 15px; color: #a8bfff; margin-top: 6px; }
  .header .subtitle { font-size: 13px; color: #7a9fff; margin-top: 4px; letter-spacing: 0.3px; }

  /* SECTION HEADERS */
  .section { margin-bottom: 32px; }
  .section-title { font-size: 19px; font-weight: 700; margin-bottom: 14px; padding-bottom: 8px; border-bottom: 2.5px solid #e0e4ef; color: #0d1b4b; display: flex; align-items: center; gap: 10px; }
  .section-title .icon { font-size: 20px; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 18px; margin-bottom: 12px; border-left: 5px solid transparent; }
  .card-red { background: #fff5f5; border-left-color: #e53e3e; }
  .card-yellow { background: #fffbf0; border-left-color: #d69e2e; }
  .card-blue { background: #f0f6ff; border-left-color: #3182ce; }
  .card-green { background: #f0fff4; border-left-color: #38a169; }
  .card-purple { background: #faf5ff; border-left-color: #805ad5; }
  .card-gray { background: #f7f8fa; border-left-color: #a0aec0; }
  .card-orange { background: #fffaf0; border-left-color: #dd6b20; }

  .card .card-label { font-size: 10px; font-weight: 700; letter-spacing: 1.2px; text-transform: uppercase; margin-bottom: 4px; }
  .label-red { color: #e53e3e; }
  .label-yellow { color: #b7791f; }
  .label-blue { color: #2b6cb0; }
  .label-green { color: #276749; }
  .label-purple { color: #553c9a; }
  .label-gray { color: #718096; }
  .label-orange { color: #c05621; }

  .card .card-title { font-size: 15px; font-weight: 700; margin-bottom: 4px; }
  .card .card-meta { font-size: 12px; color: #718096; margin-bottom: 6px; }
  .card .card-body { font-size: 13.5px; color: #2d3748; margin-bottom: 8px; }
  .card .card-action { font-size: 12.5px; font-weight: 600; }
  .action-red { color: #c53030; }
  .action-yellow { color: #975a16; }
  .action-blue { color: #2b6cb0; }
  .action-green { color: #276749; }
  .action-purple { color: #553c9a; }
  .action-gray { color: #4a5568; }

  /* EXEC SUMMARY */
  .exec-summary { background: linear-gradient(135deg, #1a2f7a 0%, #2a4db0 100%); color: #fff; border-radius: 12px; padding: 22px 26px; margin-bottom: 28px; }
  .exec-summary h2 { font-size: 17px; font-weight: 700; margin-bottom: 14px; color: #a8c8ff; letter-spacing: 0.5px; }
  .exec-summary ul { list-style: none; padding: 0; }
  .exec-summary ul li { padding: 7px 0; border-bottom: 1px solid rgba(255,255,255,0.1); font-size: 14px; display: flex; gap: 10px; }
  .exec-summary ul li:last-child { border-bottom: none; }
  .exec-summary ul li .bullet { font-size: 16px; }

  /* CALENDAR TABLE */
  .cal-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .cal-table th { background: #0d1b4b; color: #fff; padding: 10px 12px; text-align: left; font-weight: 600; }
  .cal-table td { padding: 10px 12px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  .cal-table tr:nth-child(even) td { background: #f7f9ff; }
  .cal-table tr:hover td { background: #edf2ff; }
  .status-confirmed { color: #276749; font-weight: 600; }
  .status-declined { color: #c53030; font-weight: 600; }
  .status-pending { color: #b7791f; font-weight: 600; }
  .status-accepted { color: #276749; font-weight: 600; }
  .cal-day-header td { background: #edf2ff; font-weight: 700; color: #0d1b4b; font-size: 13.5px; }
  .conflict-badge { background: #fed7d7; color: #c53030; border-radius: 4px; padding: 2px 6px; font-size: 10px; font-weight: 700; }

  /* PRIORITY TABLE */
  .priority-table { width: 100%; border-collapse: collapse; font-size: 13.5px; }
  .priority-table th { background: #1a2f7a; color: #fff; padding: 10px 14px; text-align: left; }
  .priority-table td { padding: 10px 14px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  .priority-table tr:nth-child(even) td { background: #f7f8fa; }

  /* ACCOUNTING TABLE */
  .acct-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .acct-table th { background: #2d3748; color: #fff; padding: 9px 12px; text-align: left; }
  .acct-table td { padding: 9px 12px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  .acct-table tr:nth-child(even) td { background: #f7f8fa; }
  .acct-table .total-row td { background: #edf2ff; font-weight: 700; }

  /* SECTION FOOTER */
  .section-footer { font-size: 12px; font-weight: 600; color: #4a5568; background: #edf2ff; border-radius: 6px; padding: 8px 14px; margin-top: 6px; }

  /* TOP 3 */
  .top3 { background: linear-gradient(135deg, #0d1b4b 0%, #1a2f7a 100%); color: #fff; border-radius: 14px; padding: 28px 30px; margin-top: 28px; }
  .top3 h2 { font-size: 18px; font-weight: 700; margin-bottom: 16px; color: #a8c8ff; }
  .top3-item { display: flex; gap: 14px; align-items: flex-start; margin-bottom: 14px; }
  .top3-num { background: #3182ce; color: #fff; border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 16px; flex-shrink: 0; }
  .top3-text { font-size: 14px; }
  .top3-text strong { display: block; font-size: 15px; margin-bottom: 2px; }

  /* SPAM BADGE */
  .spam-badge { background: #fed7d7; color: #c53030; border-radius: 4px; padding: 1px 6px; font-size: 10px; font-weight: 700; margin-left: 6px; }
  .trash-badge { background: #e2e8f0; color: #4a5568; border-radius: 4px; padding: 1px 6px; font-size: 10px; font-weight: 700; margin-left: 6px; }
  .restore-badge { background: #c6f6d5; color: #276749; border-radius: 4px; padding: 1px 6px; font-size: 10px; font-weight: 700; }
  .delete-badge { background: #fed7d7; color: #c53030; border-radius: 4px; padding: 1px 6px; font-size: 10px; font-weight: 700; }
  .review-badge { background: #fefcbf; color: #975a16; border-radius: 4px; padding: 1px 6px; font-size: 10px; font-weight: 700; }

  a { color: #3182ce; }
  .divider { border: none; border-top: 2px solid #e0e4ef; margin: 28px 0; }
  .tag { display: inline-block; border-radius: 4px; padding: 1px 7px; font-size: 10px; font-weight: 700; margin-right: 4px; }
  .tag-urgent { background: #fed7d7; color: #c53030; }
  .tag-unread { background: #bee3f8; color: #2b6cb0; }
  .tag-read { background: #e2e8f0; color: #4a5568; }
</style>
</head>
<body>
<div class="wrapper">

  <!-- ═══════════════════════════════════════════ -->
  <!-- 1. HEADER -->
  <!-- ═══════════════════════════════════════════ -->
  <div class="header">
    <div class="subtitle">☀ Your Executive Chief of Staff Briefing</div>
    <h1>Good morning, Melissa</h1>
    <div class="date">Wednesday, June 3, 2026 &nbsp;|&nbsp; 50 emails reviewed &nbsp;|&nbsp; 10 calendar events this week</div>
  </div>

  <!-- ═══════════════════════════════════════════ -->
  <!-- 2. EXECUTIVE SUMMARY -->
  <!-- ═══════════════════════════════════════════ -->
  <div class="exec-summary">
    <h2>⚡ Executive Summary</h2>
    <ul>
      <li><span class="bullet">🔴</span><span><strong>Security Alert:</strong> Your LinkedIn password was reset and a PIN was sent today — verify these actions were yours. Multiple phishing/scam emails also detected and flagged for deletion.</span></li>
      <li><span class="bullet">📅</span><span><strong>Tomorrow is busy:</strong> You have 3 calendar events on June 4 — Dr. Husk appointment (10:30 AM, confirmed), Executive Roundtable (9 AM, declined), and HR Networking Open Office Hours (noon, no RSVP). You also have a scheduling conflict on June 10.</span></li>
      <li><span class="bullet">🟢</span><span><strong>Job Search Active:</strong> A LinkedIn job alert (Senior Director, HR Business Partner AI-Native) came in, a LinkedIn connection request from Ilya Volovnik (Vorex Intelligence Group CEO) is pending, and your consultation with Netta Jenkins is confirmed for June 9 at noon.</span></li>
    </ul>
  </div>

  <!-- ═══════════════════════════════════════════ -->
  <!-- 3. ACTION REQUIRED -->
  <!-- ═══════════════════════════════════════════ -->
  <div class="section">
    <div class="section-title"><span class="icon">🔴</span> Action Required</div>

    <div class="card card-red">
      <div class="card-label label-red">🔐 Security — Urgent</div>
      <div class="card-title">LinkedIn Password Reset + PIN Sent</div>
      <div class="card-meta">From: LinkedIn &lt;security-noreply@linkedin.com&gt; &nbsp;|&nbsp; Today, ~9:16–9:17 PM UTC</div>
      <div class="card-body">Two emails arrived in quick succession: a PIN verification (606210) followed immediately by confirmation that your LinkedIn password was successfully reset. This is only safe if you initiated it. If you did not request a reset, your account may be compromised.</div>
      <div class="card-action action-red">→ ACT NOW: Log in to LinkedIn and verify your account activity. If you did not initiate this, change your password immediately and enable 2FA. Do not use the PIN 606210 if you didn't request it.</div>
    </div>

    <div class="card card-yellow">
      <div class="card-label label-yellow">📋 RSVP Needed</div>
      <div class="card-title">HR Networking &amp; Job Search: Open Office Hours — Tomorrow, June 4, Noon</div>
      <div class="card-meta">Calendar Event &nbsp;|&nbsp; Status: No Response (needsAction)</div>
      <div class="card-body">Tomorrow's HR Networking Open Office Hours (Zoom, noon–1 PM) has not been RSVP'd. This is a peer job-search group with 150+ attendees. Note: AI notetaking tools are not allowed in this session.</div>
      <div class="card-action action-yellow">→ RSVP now — Accept or Decline. Link: <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1">Join Zoom</a></div>
    </div>

    <div class="card card-yellow">
      <div class="card-label label-yellow">📋 RSVP Needed</div>
      <div class="card-title">HR Networking &amp; Job Search Group — June 10, Noon–1:30 PM</div>
      <div class="card-meta">Calendar Event &nbsp;|&nbsp; Status: No Response (needsAction)</div>
      <div class="card-body">Second recurring HR Networking group session also shows no RSVP. Conflicts with "Melissa x Meg drinks" (starts at 1 PM same day — overlapping end times).</div>
      <div class="card-action action-yellow">→ RSVP and review June 10 conflict with Meg drinks. <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1">Join Zoom</a></div>
    </div>

    <div class="card card-yellow">
      <div class="card-label label-yellow">📋 RSVP Needed</div>
      <div class="card-title">Melissa x Meg Drinks — June 10, 1–2 PM (Location TBC)</div>
      <div class="card-meta">Calendar Event with Meg Park (Oakleaf Partnership) &nbsp;|&nbsp; Status: No Response</div>
      <div class="card-body">Drinks with Meg Park (megpark@oakleafpartnership.com) — location TBC. Overlaps with the tail end of the HR Networking group session (noon–1:30 PM). Plan accordingly or confirm location early.</div>
      <div class="card-action action-yellow">→ Respond to Meg and confirm location. Check conflict with noon networking session.</div>
    </div>

    <div class="card card-yellow">
      <div class="card-label label-yellow">🔔 Reminder — PSC Event Cancelled</div>
      <div class="card-title">Spring Social Cancelled — Next Event: Tuesday, June [date TBD]</div>
      <div class="card-meta">From: People Strategy Collective &lt;membership@mg.peoplestrategycollective.org&gt;</div>
      <div class="card-body">Tomorrow's PSC Spring Social has been cancelled. The next PSC event is on a Tuesday in June — date not fully specified in the snippet.</div>
      <div class="card-action action-yellow">→ Note cancellation. Check PSC website for next event date. Update calendar.</div>
    </div>

    <div class="card card-yellow">
      <div class="card-label label-yellow">🗓 Personal — Reminder</div>
      <div class="card-title">Contact Question Follow-Up (Jade) — Appointment Moved to June 10</div>
      <div class="card-meta">From: melissa &lt;melissaw212@gmail.com&gt; — Sent reply to Jade</div>
      <div class="card-body">You emailed Jade confirming your appointment was moved to June 10 and that you'll check in late Monday or Tuesday to confirm whether something arrived; otherwise will plan for the week after.</div>
      <div class="card-action action-yellow">→ Add reminder to follow up with Jade on Monday June 8 or Tuesday June 9.</div>
    </div>

    <div class="section-footer">→ Summary: 6 action items — security check is most urgent. RSVP to both Zoom networking sessions. Resolve June 10 schedule conflict.</div>
  </div>

  <!-- ═══════════════════════════════════════════ -->
  <!-- 4. TODAY'S SCHEDULE + PREP -->
  <!-- ═══════════════════════════════════════════ -->
  <div class="section">
    <div class="section-title"><span class="icon">📅</span> Today's Schedule (Wednesday, June 3)</div>

    <div class="card card-blue">
      <div class="card-label label-blue">Today's Overview</div>
      <div class="card-title">No calendar events scheduled for today, June 3.</div>
      <div class="card-body">Your first events begin tomorrow. Use today to: respond to urgent security items, RSVP to networking sessions, review job leads, and prep for tomorrow's Dr. Husk appointment.</div>
    </div>

    <div class="section-footer">→ Today is a clear day — focus on action items and prep for tomorrow.</div>
  </div>

  <!-- ═══════════════════════════════════════════ -->
  <!-- 5. JOB SEARCH + INTERVIEW PIPELINE -->
  <!-- ═══════════════════════════════════════════ -->
  <div class="section">
    <div class="section-title"><span class="icon">🟢</span> Job Search + Interview Pipeline</div>

    <div class="card card-green">
      <div class="card-label label-green">💼 Job Alert</div>
      <div class="card-title">Senior Director, HR Business Partner (AI-Native) — RemoteHunter</div>
      <div class="card-meta">From: LinkedIn Job Alerts &nbsp;|&nbsp; Today, 9:05 PM UTC &nbsp;|&nbsp; <span class="tag tag-unread">UNREAD</span></div>
      <div class="card-body">LinkedIn surfaced a Senior Director HRBP role with an "AI-Native" designation at RemoteHunter — remote position. Aligns well with your HR background and apparent interest in AI-integrated roles.</div>
      <div class="card-action action-green">→ Review full job posting on LinkedIn. Apply if it fits. Save to your job tracker.</div>
    </div>

    <div class="card card-green">
      <div class="card-label label-green">🤝 LinkedIn Connection</div>
      <div class="card-title">Invitation from Ilya Volovnik — Founder &amp; CEO, Vorex Intelligence Group</div>
      <div class="card-meta">From: LinkedIn &lt;invitations@linkedin.com&gt; &nbsp;|&nbsp; Today, 7:05 PM UTC &nbsp;|&nbsp; <span class="tag tag-unread">UNREAD</span></div>
      <div class="card-body">Ilya Volovnik (Founder &amp; CEO of Vorex Intelligence Group) sent a LinkedIn connection request. Potentially a valuable networking contact in the intelligence/consulting space.</div>
      <div class="card-action action-green">→ Review Ilya's profile. Accept if relevant to your search. Consider sending a message.</div>
    </div>

    <div class="card card-green">
      <div class="card-label label-green">📞 Confirmed Consultation</div>
      <div class="card-title">Melissa x Netta Jenkins — 15-Min Zoom Consultation</div>
      <div class="card-meta">Calendar &nbsp;|&nbsp; Tuesday, June 9, 12:00–12:15 PM &nbsp;|&nbsp; Status: Accepted ✓</div>
      <div class="card-body">Confirmed consultation with Netta Jenkins (netta@hicconsult.com) via Zoom. 15 minutes — come prepared with specific questions. Password: 424726.</div>
      <div class="card-action action-green">→ Prep 2–3 focused questions for Netta ahead of Tuesday. <a href="https://us06web.zoom.us/j/5224221004?pwd=UU5YNmlFckpjQnlzc2FDMHFlNUhhUT09">Join Zoom</a></div>
    </div>

    <div class="card card-green">
      <div class="card-label label-green">🗓 Networking</div>
      <div class="card-title">HR Networking &amp; Job Search Open Office Hours (Tomorrow, June 4, Noon)</div>
      <div class="card-meta">Calendar &nbsp;|&nbsp; June 4, 12–1 PM &nbsp;|&nbsp; Status: No RSVP yet</div>
      <div class="card-body">Peer HR job-search networking session. 150+ members. Good opportunity for warm connections and referrals.</div>
      <div class="card-action action-green">→ RSVP and attend. No AI notetaking allowed per organizer instructions.</div>
    </div>

    <div class="card card-purple">
      <div class="card-label label-purple">🎓 Research — Job Market</div>
      <div class="card-title">New Research: Navigating a More Competitive Job Market</div>
      <div class="card-meta">From: Ashwin &lt;ashwin@mobiusenginehub.com&gt; &nbsp;|&nbsp; Today &nbsp;|&nbsp; <span class="tag tag-unread">UNREAD</span></div>
      <div class="card-body">"Resilience Tested: Navigating Job Market Decline" — new research on how HR roles are evolving with changing labor markets. Potentially useful context for interviews.</div>
      <div class="card-action action-purple">→ Skim for interview talking points on labor market resilience.</div>
    </div>

    <div class="card card-purple">
      <div class="card-label label-purple">🎓 Virtual Event Reminder</div>
      <div class="card-title">Virtual Think IT Event — Wednesday, June 17</div>
      <div class="card-meta">From: Quinn Tice &lt;qtice@yorksolutions.net&gt; &nbsp;|&nbsp; Read</div>
      <div class="card-body">Reminder about a Virtual Think IT event on June 17, focused on building a high-functioning engineering culture. Potentially useful for cross-functional HR/tech leadership perspective.</div>
      <div class="card-action action-purple">→ Add to calendar if interested. Review registration details.</div>
    </div>

    <div class="section-footer">→ Summary: 1 job alert to review, 1 LinkedIn invitation to accept, 1 confirmed consultation to prep for, 2 networking sessions to RSVP, 1 research article to skim.</div>
  </div>

  <!-- ═══════════════════════════════════════════ -->
  <!-- 6. IMPORTANT EMAILS -->
  <!-- ═══════════════════════════════════════════ -->
  <div class="section">
    <div class="section-title"><span class="icon">📬</span> Important Emails — Flagged for Attention</div>

    <div class="card card-red">
      <div class="card-label label-red">⚠ Phishing / Scam — Do Not Engage</div>
      <div class="card-title">"Cloud Account Locked — Photos Will Be Deleted"</div>
      <div class="card-meta">From: 'Payment_Declined' &lt;xbtcsupportmd@...&gt; &nbsp;|&nbsp; <span class="tag tag-unread">UNREAD</span> <span class="spam-badge">PHISHING</span></div>
      <div class="card-body">Fake cloud subscription expiration threat designed to get you to click a link or pay. Suspicious sender domain, urgent fear-based language, fake subscription ID. Classic phishing pattern.</div>
      <div class="card-action action-red">→ DELETE immediately. Do not click any links. Mark as spam.</div>
    </div>

    <div class="card card-red">
      <div class="card-label label-red">⚠ Spam / Scam — Casino</div>
      <div class="card-title">Casino Yabby "NGR Bonus Ready" — $13,963.99 in Account</div>
      <div class="card-meta">From: Casino_Yabby &lt;tfvrniyohli@fknm.iwebcsruiikul.us&gt; &nbsp;|&nbsp; <span class="spam-badge">SCAM</span></div>
      <div class="card-body">Fraudulent casino spam claiming a large payment is ready. Completely fake, suspicious domain, designed to steal credentials or payment info.</div>
      <div class="card-action action-red">→ DELETE. Mark as spam. Do not engage.</div>
    </div>

    <div class="card card-red">
      <div class="card-label label-red">⚠ Spam / Scam — Gambling</div>
      <div class="card-title">130 Free Spins / No Deposit Casino Offer</div>
      <div class="card-meta">From: melissaw212 (spoofed) &lt;gudvuwhjjks@lmsw.wucbgfmxbenbv.us&gt; &nbsp;|&nbsp; <span class="spam-badge">SCAM</span></div>
      <div class="card-body">Gambling spam using your own email address in the sender name (spoofed). Fake "VIP" casino offer. Suspicious domain. Do not click.</div>
      <div class="card-action action-red">→ DELETE. Mark as spam.</div>
    </div>

    <div class="card card-yellow">
      <div class="card-label label-yellow">💜 Professional — HR Community</div>
      <div class="card-title">Tech Fatigue: Leading Effective Change — Transform Community Post</div>
      <div class="card-meta">From: Transform &lt;community@transform.us&gt; &nbsp;|&nbsp; NYC Chapter &nbsp;|&nbsp; <span class="tag tag-unread">UNREAD</span></div>
      <div class="card-body">Jaison Williams (NYC Chapter) posted about tech fatigue and leading organized change. Relevant to HR leadership roles and interview conversations.</div>
      <div class="card-action action-yellow">→ Skim and save relevant talking points. Keep subscription.</div>
    </div>

    <div class="card card-yellow">
      <div class="card-label label-yellow">💼 HR.com Webcast</div>
      <div class="card-title">Is Your Benefits Plan Ready for 2027? — End of Bundled Maternity Care Webcast</div>
      <div class="card-meta">From: Rhonda from HR.com &lt;info@events.hr.com&gt; &nbsp;|&nbsp; Webcast: June 24, 2026 &nbsp;|&nbsp; Free</div>
      <div class="card-body">Free webcast on upcoming changes to bundled maternity care billing — relevant for total rewards strategy. HR.com hosted event on June 24.</div>
      <div class="card-action action-yellow">→ Register if relevant to current/target role. Add to calendar.</div>
    </div>

    <div class="card card-yellow">
      <div class="card-label label-yellow">📊 HR Survey</div>
      <div class="card-title">Total Rewards Strategy Survey — HR.com Research</div>
      <div class="card-meta">From: Research Institute at HR.com &lt;research@research.hr.com&gt; &nbsp;|&nbsp; <span class="tag tag-unread">UNREAD</span></div>
      <div class="card-body">Survey on compensation and retention strategies. Participating can give you access to benchmark data useful for job search and interviews.</div>
      <div class="card-action action-yellow">→ Complete if you want benchmark data. Low time cost.</div>
    </div>

    <div class="card card-gray">
      <div class="card-label label-gray">🏡 Neighborhood</div>
      <div class="card-title">Nextdoor: NYU Research Study + No-Tipping Restaurant Post</div>
      <div class="card-meta">From: Nextdoor (Yorkville E83st–2ndAve) &nbsp;|&nbsp; <span class="tag tag-unread">UNREAD</span></div>
      <div class="card-body">Two Nextdoor posts: (1) NYU Graduate Research Assistant seeking study participants, (2) community discussion about a no-tipping restaurant.</div>
      <div class="card-action action-gray">→ Read if interested. Low priority. Safe to ignore.</div>
    </div>

    <div class="section-footer">→ Summary: 3 scam/phishing emails flagged for immediate deletion. 3 professional emails worth reading. 1 neighborhood digest — low priority.</div>
  </div>

  <!-- ═══════════════════════════════════════════ -->
  <!-- 7. CALENDAR RISKS THIS WEEK -->
  <!-- ═══════════════════════════════════════════ -->
  <div class="section">
    <div class="section-title"><span class="icon">⚠</span> Calendar Risks This Week</div>

    <div class="card card-red">
      <div class="card-label label-red">⚠ Scheduling Conflict</div
