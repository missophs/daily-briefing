<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Daily Briefing – Wednesday, June 3, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; line-height: 1.5; }
  .wrapper { max-width: 860px; margin: 0 auto; padding: 0 0 40px 0; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #0d1b3e 0%, #1a3a6b 100%); color: white; padding: 36px 40px 28px; border-radius: 0 0 16px 16px; }
  .header-greeting { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header-date { font-size: 15px; color: #a8c0e8; margin-top: 4px; }
  .header-meta { font-size: 13px; color: #7a9cc5; margin-top: 10px; }
  .header-badge { display: inline-block; background: rgba(255,255,255,0.15); border-radius: 20px; padding: 3px 12px; font-size: 12px; margin-top: 8px; }

  /* SECTION WRAPPER */
  .section { margin: 24px 20px 0; }
  .section-title { font-size: 20px; font-weight: 800; letter-spacing: -0.3px; margin-bottom: 12px; padding-bottom: 8px; border-bottom: 2px solid #e0e4ef; text-transform: uppercase; color: #0d1b3e; display: flex; align-items: center; gap: 8px; }

  /* EXECUTIVE SUMMARY */
  .exec-summary { background: #0d1b3e; color: white; margin: 20px 20px 0; border-radius: 12px; padding: 24px 28px; }
  .exec-summary h2 { font-size: 16px; text-transform: uppercase; letter-spacing: 1px; color: #a8c0e8; margin-bottom: 14px; }
  .exec-bullet { display: flex; gap: 12px; margin-bottom: 10px; align-items: flex-start; }
  .exec-bullet-icon { font-size: 18px; flex-shrink: 0; margin-top: 1px; }
  .exec-bullet-text { font-size: 14px; color: #dce8f8; line-height: 1.5; }
  .exec-bullet-text strong { color: white; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 10px; border-left: 5px solid transparent; }
  .card-red { background: #fff5f5; border-left-color: #e53e3e; }
  .card-yellow { background: #fffbf0; border-left-color: #d69e2e; }
  .card-blue { background: #f0f6ff; border-left-color: #3182ce; }
  .card-green { background: #f0fff4; border-left-color: #38a169; }
  .card-purple { background: #faf5ff; border-left-color: #805ad5; }
  .card-gray { background: #f7f8fa; border-left-color: #a0aec0; }
  .card-orange { background: #fff8f0; border-left-color: #dd6b20; }

  .card-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px; }
  .label-red { color: #c53030; }
  .label-yellow { color: #b7791f; }
  .label-blue { color: #2b6cb0; }
  .label-green { color: #276749; }
  .label-purple { color: #6b46c1; }
  .label-gray { color: #718096; }
  .label-orange { color: #c05621; }

  .card-title { font-size: 15px; font-weight: 700; margin-bottom: 4px; }
  .card-meta { font-size: 12px; color: #718096; margin-bottom: 6px; }
  .card-body { font-size: 13px; color: #4a5568; margin-bottom: 8px; }
  .card-action { font-size: 12px; font-weight: 600; padding: 4px 10px; border-radius: 20px; display: inline-block; }
  .action-red { background: #fed7d7; color: #c53030; }
  .action-yellow { background: #fefcbf; color: #975a16; }
  .action-blue { background: #bee3f8; color: #2a69ac; }
  .action-green { background: #c6f6d5; color: #22543d; }
  .action-purple { background: #e9d8fd; color: #553c9a; }
  .action-gray { background: #e2e8f0; color: #4a5568; }
  .action-orange { background: #feebc8; color: #9c4221; }

  /* CALENDAR */
  .cal-day { background: white; border-radius: 10px; margin-bottom: 10px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }
  .cal-day-header { background: #1a3a6b; color: white; padding: 10px 18px; font-size: 14px; font-weight: 700; display: flex; justify-content: space-between; align-items: center; }
  .cal-day-header.today { background: #2c5282; }
  .cal-day-header .day-label { font-size: 11px; background: rgba(255,255,255,0.2); border-radius: 10px; padding: 2px 8px; }
  .cal-event { padding: 12px 18px; border-bottom: 1px solid #f0f2f5; }
  .cal-event:last-child { border-bottom: none; }
  .cal-event-time { font-size: 12px; color: #718096; font-weight: 600; margin-bottom: 2px; }
  .cal-event-name { font-size: 14px; font-weight: 700; color: #1a1a2e; margin-bottom: 3px; }
  .cal-event-detail { font-size: 12px; color: #4a5568; margin-bottom: 3px; }
  .cal-event-link { font-size: 12px; color: #3182ce; word-break: break-all; }
  .status-badge { display: inline-block; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 10px; text-transform: uppercase; margin-left: 6px; }
  .status-accepted { background: #c6f6d5; color: #22543d; }
  .status-declined { background: #fed7d7; color: #c53030; }
  .status-pending { background: #fefcbf; color: #975a16; }
  .status-confirmed { background: #bee3f8; color: #2a69ac; }
  .cal-empty { padding: 16px 18px; font-size: 13px; color: #a0aec0; font-style: italic; }
  .conflict-badge { display: inline-block; background: #fed7d7; color: #c53030; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 10px; margin-left: 6px; }

  /* TABLE */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #0d1b3e; color: white; padding: 10px 14px; text-align: left; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; }
  td { padding: 9px 14px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  tr:nth-child(even) td { background: #f7f8fa; }
  tr:last-child td { border-bottom: none; }
  .tbl-wrapper { background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }

  /* PRIORITY */
  .priority-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
  .priority-card { background: white; border-radius: 10px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); border-top: 4px solid; }
  .priority-card.p1 { border-top-color: #e53e3e; }
  .priority-card.p2 { border-top-color: #d69e2e; }
  .priority-card.p3 { border-top-color: #3182ce; }
  .priority-number { font-size: 28px; font-weight: 900; color: #e2e8f0; line-height: 1; }
  .priority-text { font-size: 14px; font-weight: 700; margin-top: 4px; color: #1a1a2e; }
  .priority-sub { font-size: 12px; color: #718096; margin-top: 4px; }

  /* FOOTER */
  .footer { text-align: center; font-size: 12px; color: #a0aec0; margin-top: 32px; padding: 0 20px; }

  /* SECTION END NOTE */
  .section-footer { background: white; border-radius: 8px; padding: 10px 16px; font-size: 12px; color: #4a5568; margin-top: 4px; border-left: 3px solid #cbd5e0; }
  .section-footer strong { color: #1a1a2e; }

  /* WARNING BANNER */
  .warning-banner { background: #fff5f5; border: 1px solid #fc8181; border-radius: 10px; padding: 14px 18px; margin-bottom: 10px; display: flex; gap: 10px; align-items: flex-start; }
  .warning-banner-icon { font-size: 20px; flex-shrink: 0; }
  .warning-banner-text { font-size: 13px; color: #742a2a; }

  /* GROUP BOX */
  .group-box { background: white; border-radius: 10px; padding: 16px 20px; margin-bottom: 10px; box-shadow: 0 1px 4px rgba(0,0,0,0.06); }
  .group-box-title { font-size: 13px; font-weight: 700; margin-bottom: 8px; color: #1a1a2e; }
  .group-item { font-size: 12px; color: #4a5568; padding: 5px 0; border-bottom: 1px solid #f0f2f5; display: flex; justify-content: space-between; align-items: flex-start; gap: 10px; }
  .group-item:last-child { border-bottom: none; }
  .group-item-label { flex: 1; }
  .group-item-tag { font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 10px; white-space: nowrap; flex-shrink: 0; }
  .tag-delete { background: #fed7d7; color: #c53030; }
  .tag-review { background: #fefcbf; color: #975a16; }
  .tag-restore { background: #c6f6d5; color: #22543d; }
  .tag-ignore { background: #e2e8f0; color: #718096; }
  .tag-keep { background: #bee3f8; color: #2a69ac; }
  .tag-spam { background: #fbb6ce; color: #97266d; }

  @media (max-width: 600px) {
    .priority-grid { grid-template-columns: 1fr; }
    .header { padding: 24px 20px 20px; }
    .section { margin: 16px 12px 0; }
    .exec-summary { margin: 16px 12px 0; }
  }
</style>
</head>
<body>
<div class="wrapper">

<!-- ============================================================ -->
<!-- 1. HEADER -->
<!-- ============================================================ -->
<div class="header">
  <div class="header-greeting">☀️ Good morning, Melissa</div>
  <div class="header-date">Wednesday, June 3, 2026</div>
  <div class="header-meta">Your Executive Chief of Staff Daily Briefing</div>
  <div class="header-badge">📋 50 emails reviewed &nbsp;|&nbsp; 9 calendar events this week</div>
</div>

<!-- ============================================================ -->
<!-- 2. EXECUTIVE SUMMARY -->
<!-- ============================================================ -->
<div class="exec-summary">
  <h2>⚡ Executive Summary</h2>
  <div class="exec-bullet">
    <div class="exec-bullet-icon">🔴</div>
    <div class="exec-bullet-text"><strong>Security Alert:</strong> Your LinkedIn password was reset today and a PIN was issued — confirm this was you. Multiple scam/phishing emails also flagged in your inbox (fake cloud lockout, casino spam). Immediate review recommended.</div>
  </div>
  <div class="exec-bullet">
    <div class="exec-bullet-icon">📅</div>
    <div class="exec-bullet-text"><strong>Tomorrow is busy:</strong> You have three events on Thursday June 4 — Executive Roundtable (declined), Dr. Husk appointment at 10:30 AM, and HR Networking Open Office Hours at noon (RSVP still pending). Confirm your attendance.</div>
  </div>
  <div class="exec-bullet">
    <div class="exec-bullet-icon">💼</div>
    <div class="exec-bullet-text"><strong>Job Search Active:</strong> LinkedIn sent a Senior Director, HR Business Partner (AI-Native) role to your inbox. You also have a confirmed 15-min consult with Netta Jenkins on June 9. Drinks with Meg on June 10 needs a venue.</div>
  </div>
</div>

<!-- ============================================================ -->
<!-- 3. ACTION REQUIRED -->
<!-- ============================================================ -->
<div class="section">
  <div class="section-title">🔴 Action Required</div>

  <div class="card card-red">
    <div class="card-label label-red">🚨 Security — Verify Now</div>
    <div class="card-title">LinkedIn Password Reset + PIN Issued</div>
    <div class="card-meta">From: LinkedIn &lt;security-noreply@linkedin.com&gt; · Wed Jun 3, ~9:16–9:17 PM UTC</div>
    <div class="card-body">Two LinkedIn security emails arrived within two minutes: first, a PIN (606210) was issued to verify your identity, then your password was confirmed as successfully reset. If you did not initiate this, your account may be compromised. Both emails are now in Trash — this may mean they were automatically filtered.</div>
    <span class="card-action action-red">⚡ Log into LinkedIn immediately. Verify account activity. Enable 2FA if not already on.</span>
  </div>

  <div class="card card-red">
    <div class="card-label label-red">🚨 Scam / Phishing — Do Not Click</div>
    <div class="card-title">Fake "Cloud Account Locked" Threat Email</div>
    <div class="card-meta">From: "Payment_Declined" &lt;xbtcsupportmd@wcknlkzajfzzlhmducymgdwi.com&gt; · Wed Jun 3</div>
    <div class="card-body">Subject claims your cloud account is locked and photos/videos will be deleted. This is a phishing scam — the sender domain is fake, the subject line uses stylized Unicode to evade filters, and it contains urgency tactics. Do not click any links. Currently NOT in trash — still in inbox-adjacent folders.</div>
    <span class="card-action action-red">🗑️ Delete immediately. Mark as spam/phishing in Gmail.</span>
  </div>

  <div class="card card-yellow">
    <div class="card-label label-yellow">⚠️ RSVP Needed — Tomorrow</div>
    <div class="card-title">HR Networking &amp; Job Search: Open Office Hours</div>
    <div class="card-meta">Calendar Event · Thu Jun 4, 12:00–1:00 PM · Status: Needs Action</div>
    <div class="card-body">You have not yet responded to this networking session. It overlaps with the end of your Dr. Husk appointment (10:30–11:30 AM), so there's a 30-min buffer. Large group session — over 150 attendees. Note requests AI notetaking tools be turned off.</div>
    <span class="card-action action-yellow">📩 RSVP Accept or Decline. Zoom: us06web.zoom.us/j/85945371140</span>
  </div>

  <div class="card card-yellow">
    <div class="card-label label-yellow">⚠️ Venue TBD — Needs Confirming</div>
    <div class="card-title">Melissa x Meg Drinks — Location Still TBC</div>
    <div class="card-meta">Calendar Event · Wed Jun 10, 1:00–2:00 PM · Attendee: megpark@oakleafpartnership.com · Status: Needs Action</div>
    <div class="card-body">Drinks with Meg are on the calendar but the location is listed as "tbc." This also overlaps with the HR Networking Group session (12:00–1:30 PM) on the same day — potential conflict in the 1:00–1:30 PM window.</div>
    <span class="card-action action-yellow">📍 Confirm venue with Meg. Review overlap with HR Networking on June 10.</span>
  </div>

  <div class="card card-yellow">
    <div class="card-label label-yellow">⚠️ Billing Reminder — This Weekend</div>
    <div class="card-title">State Farm Bill Due June 7</div>
    <div class="card-meta">Calendar Reminder · Sun Jun 7 (All Day)</div>
    <div class="card-body">State Farm payment is flagged on the calendar for Sunday June 7. Make sure it's scheduled for auto-pay or manually submitted before the due date.</div>
    <span class="card-action action-yellow">💳 Confirm payment is set up before Sunday.</span>
  </div>

  <div class="card card-yellow">
    <div class="card-label label-yellow">⚠️ Contact Lens Appointment — Confirm Delivery</div>
    <div class="card-title">Contact Appointment Moved to the 10th — Check Delivery</div>
    <div class="card-meta">From: melissa (melissaw212@gmail.com) · To: Jade · Wed Jun 3, 1:59 PM</div>
    <div class="card-body">You emailed Jade to confirm you moved your contact lens appointment to June 10 and said you'd check in late Monday or Tuesday (June 8/9) to see if the contacts have arrived. If they haven't, you'll push to the following week.</div>
    <span class="card-action action-yellow">📅 Add reminder to check in with Jade on Mon June 8 or Tue June 9.</span>
  </div>

  <div class="card card-yellow">
    <div class="card-label label-yellow">⚠️ Netlify Credits at 75%</div>
    <div class="card-title">Netlify Billing Warning — Morning Briefing Project</div>
    <div class="card-meta">From: Netlify &lt;team@netlify.com&gt; · Wed Jun 3, 9:28 PM UTC · In Trash</div>
    <div class="card-body">Your Netlify team "morning briefing" has used 750 of your 1,000 monthly credits. At current usage rates, you may hit the limit before your billing cycle ends. This is related to your daily briefing automation workflow.</div>
    <span class="card-action action-yellow">🔍 Review Netlify usage. Consider upgrading plan or optimizing build frequency.</span>
  </div>

  <div class="card card-yellow">
    <div class="card-label label-yellow">⚠️ GitHub Actions Failing</div>
    <div class="card-title">Daily Briefing Workflow Failed (2 Runs)</div>
    <div class="card-meta">From: missophs &lt;notifications@github.com&gt; · Wed Jun 3, 3:17 PM &amp; 3:25 PM · In Trash</div>
    <div class="card-body">Two GitHub Actions workflow runs for your daily-briefing repo failed today (commits b04c8a4 and 7812f1d). All jobs failed in both runs, which likely explains why earlier briefing attempts arrived as raw markdown or HTML source. The webhook trigger may be misconfigured.</div>
    <span class="card-action action-yellow">🛠️ Review GitHub Actions logs for missophs/daily-briefing. Fix webhook config.</span>
  </div>

  <div class="section-footer"><strong>Action Required Summary:</strong> Act on LinkedIn security now · RSVP for June 4 networking · Confirm Meg's venue · Schedule State Farm payment · Follow up with Jade on June 8/9 · Fix GitHub Actions webhook · Monitor Netlify credits.</div>
</div>

<!-- ============================================================ -->
<!-- 4. TODAY'S SCHEDULE + PREP (Tomorrow, June 4 since it's EOD) -->
<!-- ============================================================ -->
<div class="section">
  <div class="section-title">📅 Tomorrow's Schedule + Prep (Thu, June 4)</div>

  <div class="cal-day">
    <div class="cal-day-header today">
      <span>Thursday, June 4, 2026</span>
      <span class="day-label">Tomorrow</span>
    </div>

    <div class="cal-event">
      <div class="cal-event-time">9:00 AM – 10:30 AM</div>
      <div class="cal-event-name">Executive Roundtable <span class="status-badge status-declined">Declined</span></div>
      <div class="cal-event-detail">Host: John Madigan · Zoom Meeting ID: 207 786 667 · PW: 205454</div>
      <div class="cal-event-detail">⚠️ You declined this event. No prep needed unless you reconsider.</div>
      <div class="cal-event-link"><a href="https://us02web.zoom.us/j/207786667">Zoom Link</a></div>
    </div>

    <div class="cal-event">
      <div class="cal-event-time">10:30 AM – 11:30 AM</div>
      <div class="cal-event-name">Dr. Husk <span class="status-badge status-confirmed">Confirmed</span></div>
      <div class="cal-event-detail">No location listed. Likely a medical/health appointment.</div>
      <div class="cal-event-detail">📋 Prep: Confirm location/address ahead of time. Note: contacts appointment was moved to June 10 — Dr. Husk may be a different provider.</div>
    </div>

    <div class="cal-event">
      <div class="cal-event-time">12:00 PM – 1:00 PM</div>
      <div class="cal-event-name">HR Networking &amp; Job Search: Open Office Hours <span class="status-badge status-pending">RSVP Pending</span></div>
      <div class="cal-event-detail">Large group session (150+ attendees) · No AI notetaking tools</div>
      <div class="cal-event-detail">⚠️ 30-min buffer after Dr. Husk — feasible if appointment runs on time.</div>
      <div class="cal-event-link"><a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1">Zoom Link</a></div>
    </div>
  </div>

  <div class="section-footer"><strong>Schedule Summary:</strong> Executive Roundtable is declined — no conflict. Dr. Husk confirmed at 10:30 AM — verify address. RSVP to HR Networking by tomorrow morning.</div>
</div>

<!-- ============================================================ -->
<!-- 5. JOB SEARCH + INTERVIEW PIPELINE -->
<!-- ============================================================ -->
<div class="section">
  <div class="section-title">💼 Job Search + Interview Pipeline</div>

  <div class="card card-green">
    <div class="card-label label-green">🎯 Job Lead — In Inbox</div>
    <div class="card-title">Senior Director, HR Business Partner (AI-Native) at RemoteHunter</div>
    <div class="card-meta">From: LinkedIn Job Alerts · Wed Jun 3, 9:05 PM UTC · Unread: No · In Inbox: Yes</div>
    <div class="card-body">LinkedIn surfaced this role matching your profile. Title aligns well with your HR leadership background. "AI-Native" framing suggests the org is building an AI-forward HR function — a strong fit given your current interests.</div>
    <span class="card-action action-green">🔍 Open LinkedIn alert, review full JD, and apply if qualified.</span>
  </div>

  <div class="card card-green">
    <div class="card-label label-green">📞 Confirmed Consult — June 9</div>
    <div class="card-title">15-Min Consultation with Netta Jenkins (HIC Consult)</div>
    <div class="card-meta">Calendar Event · Tue Jun 9, 12:00–12:15 PM · netta@hicconsult.com · Status: Accepted</div>
    <div class="card-body">Confirmed Zoom call with Netta Jenkins. Very short window (15 minutes) — come prepared with a clear ask. Likely a coaching or placement discovery call.</div>
    <div class="card-action action-green">📝 Prep 2-min pitch + specific ask. Zoom: us06web.zoom.us/j/5224221004 · PW: 424726</div>
  </div>

  <div class="card card-blue">
    <div class="card-label label-blue">🤝 Networking — RSVP Pending</div>
    <div class="card-title">HR Networking &amp; Job Search Group — Full Session</div>
    <div class="card-meta">Calendar Event · Wed Jun 10, 12:00–1:30 PM · 150+ Attendees · Status: Needs Action</div>
    <div class="card-body">Larger weekly networking group. Resources shared in description include HR Networking Team Guidelines. Conflicts with Melissa x Meg drinks at 1:00 PM — you may need to leave the Zoom early.</div>
    <span class="card-action action-blue">⚠️ RSVP + plan to exit Zoom by 12:55 to make Meg drinks at 1:00 PM.</span>
  </div>

  <div class="card card-blue">
    <div class="card-label label-blue">🤝 Relationship Building</div>
    <div class="card-title">Melissa x Meg Drinks</div>
    <div class="card-meta">Calendar Event · Wed Jun 10, 1:00–2:00 PM · megpark@oakleafpartnership.com · Location: TBC</div>
    <div class="card-body">Drinks with Meg Park (Oakleaf Partnership). Good networking/relationship opportunity. Location is still TBC and overlaps with end of HR Networking session.</div>
    <span class="card-action action-blue">📍 Confirm venue with Meg. Oakleaf Partnership = staffing/HR firm worth cultivating.</span>
  </div>

  <div class="card card-purple">
    <div class="card-label label-purple">📣 LinkedIn Invite — Review</div>
    <div class="card-title">Ilya Volovnik (Vorex Intelligence Group) Sent Connection Request</div>
    <div class="card-meta">From: LinkedIn Invitations · Wed Jun 3, 7:05 PM UTC · In Trash</div>
    <div class="card-body">Ilya Volovnik, Founder &amp; CEO of Vorex Intelligence Group, invited you to connect on LinkedIn. May be worth accepting if relevant to your search — intelligence/strategy sector.</div>
    <span class="card-action action-purple">🔍 Review Ilya's profile before accepting. Could be a worthwhile connection.</span>
  </div>

  <div class="card card-purple">
    <div class="card-label label-purple">📣 Virtual Event Reminder</div>
    <div class="card-title">Virtual Think IT Event — Wed June 17</div>
    <div class="card-meta">From: Quinn Tice, York Solutions · Wed Jun 3, 6:05 PM · Not in trash</div>
    <div class="card-body">Reminder about York Solutions' Virtual Think IT Event on June 17, focused on building a high-functioning engineering culture. May be less relevant unless you're exploring tech-adjacent HR roles.</div>
    <span class="card-action action-purple">📌 Add to calendar if interested. Low priority but professional content.</span>
  </div>

  <div class="section-footer"><strong>Job Search Summary:</strong> Review LinkedIn Senior Director role today. Prep for Netta Jenkins call (June 9). Resolve venue/timing conflict for June 10. LinkedIn connection from Vorex worth reviewing.</div>
</div>

<!-- ============================================================ -->
<!-- 6. IMPORTANT EMAILS -->
<!-- ============================================================ -->
<div class="section">
  <div class="section-title">📬 Important Emails</div>

  <div class="card card-red">
    <div class="card-label label-red">🚨 Phishing / Spam</div>
    <div class="card-title">Casino Yabby NGR Bonus — "$13,963.99 in your account"</div>
    <div class="card-meta">From: 🎲Casino_Yabby🎲 &lt;tfvrniyohli@fknm.iwebcsruiikul.us&gt; · Not in Trash</div>
    <div class="card-body">Classic financial fraud/phishing email with fake payment claims. The sender domain is gibberish. Do not open any links. This email is still in your main mail — not trashed.</div>
    <span class="card
