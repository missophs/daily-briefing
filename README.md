<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa Weiss — August 20, 2026</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }

  /* ── Header ── */
  .master-header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; padding: 36px 40px 28px; }
  .master-header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .master-header .sub { font-size: 13px; color: #a8b8d8; margin-top: 6px; }
  .meta-pills { display: flex; gap: 12px; margin-top: 16px; flex-wrap: wrap; }
  .meta-pill { background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); border-radius: 20px; padding: 5px 14px; font-size: 12px; color: #d0dff5; }

  /* ── Layout ── */
  .container { max-width: 1200px; margin: 0 auto; padding: 28px 20px; }

  /* ── Section Headers ── */
  .section-header { display: flex; align-items: center; gap: 10px; margin: 36px 0 16px; }
  .section-header h2 { font-size: 18px; font-weight: 700; color: #1a1a2e; }
  .section-icon { width: 32px; height: 32px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 16px; flex-shrink: 0; }

  /* ── Color Themes ── */
  .red    { background: #fff5f5; border-left: 4px solid #e53e3e; }
  .yellow { background: #fffbeb; border-left: 4px solid #d69e2e; }
  .blue   { background: #ebf8ff; border-left: 4px solid #3182ce; }
  .green  { background: #f0fff4; border-left: 4px solid #38a169; }
  .purple { background: #faf5ff; border-left: 4px solid #805ad5; }
  .gray   { background: #f7fafc; border-left: 4px solid #a0aec0; }
  .orange { background: #fffaf0; border-left: 4px solid #dd6b20; }

  .icon-red    { background: #fed7d7; }
  .icon-yellow { background: #fefcbf; }
  .icon-blue   { background: #bee3f8; }
  .icon-green  { background: #c6f6d5; }
  .icon-purple { background: #e9d8fd; }
  .icon-gray   { background: #e2e8f0; }
  .icon-orange { background: #feebc8; }

  /* ── Cards ── */
  .card { border-radius: 10px; padding: 18px 20px; margin-bottom: 12px; }
  .card-title { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
  .card-source { font-size: 11px; color: #718096; margin-bottom: 6px; }
  .card-body { font-size: 13px; color: #2d3748; }
  .card-action { margin-top: 10px; padding: 8px 12px; background: rgba(255,255,255,0.7); border-radius: 6px; font-size: 12px; }
  .card-action strong { color: #1a1a2e; }

  /* ── Tables ── */
  table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,0.08); margin-bottom: 12px; }
  th { background: #2d3748; color: #fff; padding: 10px 14px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
  td { padding: 10px 14px; border-bottom: 1px solid #e2e8f0; font-size: 13px; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f7fafc; }
  .triage-status { font-weight: 700; white-space: nowrap; }

  /* ── Badges ── */
  .badge { display: inline-block; padding: 2px 9px; border-radius: 12px; font-size: 11px; font-weight: 700; margin-right: 4px; }
  .badge-red    { background: #fed7d7; color: #c53030; }
  .badge-yellow { background: #fefcbf; color: #975a16; }
  .badge-green  { background: #c6f6d5; color: #276749; }
  .badge-blue   { background: #bee3f8; color: #2c5282; }
  .badge-purple { background: #e9d8fd; color: #553c9a; }
  .badge-gray   { background: #e2e8f0; color: #4a5568; }
  .badge-orange { background: #feebc8; color: #7b341e; }

  /* ── Priority Tags ── */
  .pri-high   { background: #e53e3e; color: #fff; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 700; }
  .pri-med    { background: #d69e2e; color: #fff; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 700; }
  .pri-low    { background: #718096; color: #fff; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 700; }

  /* ── Calendar ── */
  .cal-day { background: #fff; border-radius: 10px; margin-bottom: 16px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
  .cal-day-header { background: #2d3748; color: #fff; padding: 10px 18px; font-size: 14px; font-weight: 700; }
  .cal-day-header.today { background: linear-gradient(90deg, #3182ce, #2b6cb0); }
  .cal-event { padding: 12px 18px; border-bottom: 1px solid #e2e8f0; display: grid; grid-template-columns: 120px 1fr; gap: 12px; }
  .cal-event:last-child { border-bottom: none; }
  .cal-time { font-size: 12px; color: #718096; font-weight: 600; }
  .cal-name { font-weight: 700; font-size: 13px; margin-bottom: 3px; }
  .cal-detail { font-size: 12px; color: #4a5568; }
  .cal-rsvp { display: inline-block; padding: 1px 7px; border-radius: 4px; font-size: 10px; font-weight: 700; margin-right: 6px; }
  .rsvp-accepted  { background: #c6f6d5; color: #276749; }
  .rsvp-declined  { background: #fed7d7; color: #c53030; }
  .rsvp-needs     { background: #fefcbf; color: #975a16; }
  .rsvp-confirmed { background: #bee3f8; color: #2c5282; }
  .cal-conflict   { color: #e53e3e; font-size: 11px; font-weight: 700; }

  /* ── Dashboard Grid ── */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; margin-bottom: 20px; }
  .dash-tile { background: #fff; border-radius: 10px; padding: 16px 18px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
  .dash-tile .label { font-size: 11px; color: #718096; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px; }
  .dash-tile .value { font-size: 26px; font-weight: 800; }
  .dash-tile .detail { font-size: 11px; color: #4a5568; margin-top: 4px; }
  .v-red    { color: #e53e3e; }
  .v-yellow { color: #d69e2e; }
  .v-green  { color: #38a169; }
  .v-blue   { color: #3182ce; }
  .v-purple { color: #805ad5; }

  /* ── Executive Summary ── */
  .exec-summary { background: #fff; border-radius: 10px; padding: 20px 24px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); margin-bottom: 16px; }
  .exec-summary ul { list-style: none; }
  .exec-summary li { padding: 10px 0; border-bottom: 1px solid #f0f0f0; display: flex; gap: 12px; align-items: flex-start; }
  .exec-summary li:last-child { border-bottom: none; }
  .exec-bullet { font-size: 20px; flex-shrink: 0; }

  /* ── Top 3 ── */
  .top3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }
  .top3-card { background: #fff; border-radius: 10px; padding: 20px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); text-align: center; }
  .top3-num { font-size: 40px; font-weight: 900; margin-bottom: 8px; }
  .top3-title { font-size: 14px; font-weight: 700; margin-bottom: 6px; }
  .top3-desc { font-size: 12px; color: #4a5568; }

  /* ── Utility ── */
  .tag { display: inline-block; background: #edf2f7; color: #4a5568; padding: 1px 7px; border-radius: 4px; font-size: 11px; margin: 2px; }
  .warn { color: #e53e3e; font-weight: 700; }
  .note { color: #718096; font-style: italic; font-size: 12px; }
  .phish-tag { background: #fed7d7; color: #c53030; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 700; }
  .auto-tag  { background: #feebc8; color: #7b341e; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 700; }
  .divider { border: none; border-top: 2px solid #e2e8f0; margin: 30px 0; }

  @media (max-width: 768px) {
    .top3 { grid-template-columns: 1fr; }
    .cal-event { grid-template-columns: 1fr; }
    .master-header { padding: 20px; }
  }
</style>
</head>
<body>

<!-- ════════════════════════════════════════════════════
     MASTER HEADER
════════════════════════════════════════════════════ -->
<div class="master-header">
  <h1>📋 Executive Briefing — Melissa Weiss</h1>
  <div class="sub">Prepared by your Executive Chief of Staff</div>
  <div class="meta-pills">
    <span class="meta-pill">📅 Thursday, August 20, 2026</span>
    <span class="meta-pill">📧 50 Emails Reviewed</span>
    <span class="meta-pill">📆 14 Calendar Events Reviewed</span>
    <span class="meta-pill">⚠️ 4 Auto-Trashed (Phishing)</span>
    <span class="meta-pill">✅ 1 Auto-Trashed (Newsletter)</span>
    <span class="meta-pill">🗑 16 Manually Trashed</span>
  </div>
</div>

<div class="container">

<!-- ════════════════════════════════════════════════════
     SECTION 0 — EMAIL TRIAGE QUICK LIST
════════════════════════════════════════════════════ -->
<div class="section-header">
  <div class="section-icon icon-blue">⚡</div>
  <h2>Email Triage Quick List</h2>
</div>
<table>
  <thead>
    <tr>
      <th style="width:130px">Status</th>
      <th style="width:220px">From</th>
      <th>Subject</th>
      <th style="width:280px">Summary</th>
    </tr>
  </thead>
  <tbody>
    <!-- ── INBOX rows ── -->
    <tr>
      <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
      <td>Chase</td>
      <td>Your credit card statement is available</td>
      <td>Chase CC ending 2754 — due 09/16/2026, min. payment $391. <span class="warn">Review & schedule payment.</span></td>
    </tr>
    <tr>
      <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
      <td>Target Circle Card</td>
      <td>Your Target Circle Card statement is available</td>
      <td>Statement available for card ending 7697. Review balance & due date.</td>
    </tr>
    <tr>
      <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
      <td>LinkedIn Job Alerts</td>
      <td>Vice President Human Resources at Soni: up to $230K/yr</td>
      <td>$190K–$230K VP HR role at Soni. <span class="warn">High-fit opportunity — review & apply.</span></td>
    </tr>
    <tr>
      <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
      <td>LinkedIn Job Alerts</td>
      <td>You may be a fit for Stripe's People Partner, Technology role</td>
      <td>Stripe hybrid People Partner role — 50% on-site. Strong brand; review fit.</td>
    </tr>
    <tr>
      <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
      <td>LinkedIn Job Alerts</td>
      <td>You may be a fit for Greenbox Capital's VP – People & Culture</td>
      <td>VP P&C, US Remote. Duplicate alert — review once &amp; act.</td>
    </tr>
    <tr>
      <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
      <td>Indeed</td>
      <td>Remote HR Managers @ Turing</td>
      <td>$100–$200/hr remote HR Manager. High pay rate — assess fit.</td>
    </tr>
    <tr>
      <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
      <td>Heather Laing (LinkedIn)</td>
      <td>Melissa A, I'd like to connect</td>
      <td>Founder & CEO, Complex Caregiver Solutions wants to connect. Respond promptly.</td>
    </tr>
    <tr>
      <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
      <td>OkCupid</td>
      <td>Someone likes you</td>
      <td>Personal dating app notification. Low priority.</td>
    </tr>
    <tr>
      <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
      <td>Match</td>
      <td>You've had a profile view from Tim</td>
      <td>Tim, 51, White Plains viewed your profile. Personal; low priority.</td>
    </tr>
    <tr>
      <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
      <td>Amazon.com</td>
      <td>Shipped: 1 Essentials item</td>
      <td>Amazon shipment en route. Track delivery if needed.</td>
    </tr>
    <tr>
      <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
      <td>Michael Givner</td>
      <td>Re: Melissa Weiss Resume and website</td>
      <td>Givner positive on Crothers firm (knows founder 10 yrs), mentions Amy. <span class="warn">Follow up.</span></td>
    </tr>
    <tr>
      <td class="triage-status"><span class="badge badge-blue">📥 INBOX</span></td>
      <td>Facebook</td>
      <td>See 21 updates: about Noor and others</td>
      <td>Facebook notification digest. Personal; low priority.</td>
    </tr>
    <!-- ── Trash summary rows ── -->
    <tr style="background:#fff9f0;">
      <td class="triage-status"><span class="badge badge-gray">🗑 TRASHED (auto)</span></td>
      <td colspan="2"><em>5 emails auto-trashed (4 phishing + 1 newsletter) — see Trash Review</em></td>
      <td class="note">Auto-trashed before delivery. No action needed.</td>
    </tr>
    <tr style="background:#f7f7f7;">
      <td class="triage-status"><span class="badge badge-gray">🗂 TRASH (manual)</span></td>
      <td colspan="2"><em>16 emails in Trash (manual) — see Trash Review</em></td>
      <td class="note">Newsletters, promos, spam trashed by Gmail. Review section below.</td>
    </tr>
  </tbody>
</table>

<!-- ════════════════════════════════════════════════════
     SECTION 1 — EXECUTIVE SUMMARY
════════════════════════════════════════════════════ -->
<div class="section-header">
  <div class="section-icon icon-red">🎯</div>
  <h2>Executive Summary</h2>
</div>
<div class="exec-summary">
  <ul>
    <li>
      <span class="exec-bullet">🔴</span>
      <div><strong>Biggest Risk:</strong> 4 phishing/scam emails were auto-trashed today targeting your Gmail account (fake "GmailSupportTeam" account lock, fake McAfee alert, fake SiriusXM payment, fake Payment-Declined). Additionally, several manual-trash spam emails (ED ads, adult content, "Professional Who's Who" scam) remain undeleted in your mailbox and should be permanently deleted. No credentials should be entered on any links from these senders.</div>
    </li>
    <li>
      <span class="exec-bullet">🟢</span>
      <div><strong>Biggest Opportunity:</strong> Strong VP/Senior HR job leads today — VP HR at Soni ($190K–$230K), VP People & Culture at Greenbox Capital (remote), People Partner at Stripe (hybrid), and a high-paying remote HR Manager role at Turing ($100–$200/hr). Michael Givner also responded positively about Crothers — a well-connected search firm. Your LinkedIn optimization work (Claude prompt in sent email) positions you well for outreach.</div>
    </li>
    <li>
      <span class="exec-bullet">🔵</span>
      <div><strong>Biggest Calendar Item:</strong> HR Networking & Job Search Open Office Hours today at 12:00 PM (RSVP pending — needs action). Tomorrow you have a Teams meeting with Tina from MSearch Advisory at 10:30 AM and a Zoom with Dee Dee at 12:00 PM. Chase CC payment due 09/16 and Target Circle Card statement also need scheduling. Verizon Fios bill due 08/23 — coming up fast.</div>
    </li>
  </ul>
</div>

<!-- ════════════════════════════════════════════════════
     SECTION 3 — ACTION REQUIRED
════════════════════════════════════════════════════ -->
<div class="section-header">
  <div class="section-icon icon-yellow">⚡</div>
  <h2>Action Required</h2>
</div>

<div class="card yellow">
  <div class="card-title">💳 Chase Credit Card Payment Due</div>
  <div class="card-source">From: Chase &lt;no.reply.alerts@chase.com&gt; | Inbox</div>
  <div class="card-body">Your Chase CC statement (ending 2754) is available. Minimum payment <strong>$391.00</strong> due <strong>September 16, 2026</strong>.</div>
  <div class="card-action"><strong>Next Step:</strong> Log into Chase and schedule payment today. Review full statement for any unauthorized charges.</div>
  <div style="margin-top:6px;"><span class="badge badge-yellow">Due: 09/16/2026</span></div>
</div>

<div class="card yellow">
  <div class="card-title">💳 Target Circle Card Statement Available</div>
  <div class="card-source">From: TargetCard.Services@mycirclecard.target.com | Inbox</div>
  <div class="card-body">Statement available for Target Circle Card ending in <strong>7697</strong>. Due date not specified in snippet.</div>
  <div class="card-action"><strong>Next Step:</strong> Log in to Target Circle Card account, check due date, and schedule payment.</div>
  <div style="margin-top:6px;"><span class="badge badge-yellow">Review Today</span></div>
</div>

<div class="card yellow">
  <div class="card-title">📅 Verizon Fios Bill Due Sunday</div>
  <div class="card-source">Google Calendar | All-day event 08/23/2026</div>
  <div class="card-body">Verizon Fios bill is due <strong>Sunday, August 23</strong>. Ensure payment is submitted before the due date.</div>
  <div class="card-action"><strong>Next Step:</strong> Pay Verizon Fios bill online today or by Friday to avoid weekend delays.</div>
  <div style="margin-top:6px;"><span class="badge badge-yellow">Due: 08/23/2026</span></div>
</div>

<div class="card blue">
  <div class="card-title">📅 RSVP Required — HR Networking Open Office Hours (TODAY 12 PM)</div>
  <div class="card-source">Google Calendar | Status: Needs Action</div>
  <div class="card-body">HR Networking & Job Search Open Office Hours via Zoom today 12:00–1:00 PM. Your RSVP is still pending. Large group event — 170+ attendees.</div>
  <div class="card-action"><strong>Next Step:</strong> Confirm or decline attendance now. Zoom link: https://us06web.zoom.us/j/85945371140</div>
  <div style="margin-top:6px;"><span class="badge badge-yellow">⏰ TODAY 12:00 PM</span></div>
</div>

<div class="card blue">
  <div class="card-title">📅 RSVP Required — HR Networking Group (Wed 08/26, 12 PM)</div>
  <div class="card-source">Google Calendar | Status: Needs Action</div>
  <div class="card-body">HR Networking & Job Search Group Zoom on <strong>Wednesday, August 26</strong>, 12:00–1:30 PM. RSVP still pending.</div>
  <div class="card-action"><strong>Next Step:</strong> Respond to calendar invite. Zoom link: https://us06web.zoom.us/j/81954171722</div>
  <div style="margin-top:6px;"><span class="badge badge-yellow">Due: By 08/26</span></div>
</div>

<div class="card green">
  <div class="card-title">💼 VP HR at Soni — Up to $230K (High Priority Lead)</div>
  <div class="card-source">From: LinkedIn Job Alerts | Inbox</div>
  <div class="card-body">LinkedIn matched you to a <strong>VP Human Resources at Soni</strong> paying <strong>$190K–$230K/year</strong>. This is a senior-level, strong-compensation match.</div>
  <div class="card-action"><strong>Next Step:</strong> Review job posting immediately. Tailor resume using your Claude LinkedIn optimization work and apply today.</div>
  <div style="margin-top:6px;"><span class="badge badge-green">HIGH FIT</span></div>
</div>

<div class="card green">
  <div class="card-title">💼 Follow Up — Michael Givner (Crothers / Resume & Website)</div>
  <div class="card-source">From: Michael Givner &lt;mgivner@imgbusinessadvisors.com&gt; | Inbox (read)</div>
  <div class="card-body">Givner confirmed Crothers is a <strong>good, well-connected firm</strong> (knows founder 10 years). He also mentioned Amy and family. This is a warm networking relationship that should be nurtured.</div>
  <div class="card-action"><strong>Next Step:</strong> Send a warm follow-up reply thanking him, sharing any updates on your search, and asking if he can make an introduction at Crothers.</div>
  <div style="margin-top:6px;"><span class="badge badge-green">Respond Today</span></div>
</div>

<div class="card green">
  <div class="card-title">🤝 LinkedIn Connection Request — Heather Laing, CEO (Complex Caregiver Solutions)</div>
  <div class="card-source">From: Heather Laing via LinkedIn | Inbox</div>
  <div class="card-body">Heather Laing, Founder & CEO of Complex Caregiver Solutions, sent a LinkedIn connection request. May be relevant to healthcare/HR sector networking.</div>
  <div class="card-action"><strong>Next Step:</strong> Review her profile before accepting. If relevant to your search, accept and send a brief intro message.</div>
  <div style="margin-top:6px;"><span class="badge badge-green">Review & Respond</span></div>
</div>

<div class="card red">
  <div class="card-title">🗑 Permanently Delete Lingering Spam/Scam Emails Not Yet Trashed</div>
  <div class="card-source">Multiple senders | Not in Inbox / Not Trashed</div>
  <div class="card-body">Several scam/spam emails are sitting in your mailbox (not inbox, not trash): fake "Dr. Tyler-Vance," fake MEDVi GLP-1, adult content senders, "Professional Who's Who" nomination scam, casino spam. These should be permanently removed.</div>
  <div class="card-action"><strong>Next Step:</strong> Trash and permanently delete: Dr. Tyler-Vance (penis enlargement), MEDVi GLP-1 from random domain, F*ckMeHard adult spam, ProfessionalWhosWho scam, BettyWins casino spam, Huang Wei/Whirlpool scam, SHRM HR Jobs (if not wanted), ManForce ED, Sex Trick ED email.</div>
  <div style="margin-top:6px;"><span class="badge badge-red">DO TODAY</span></div>
</div>

<!-- ════════════════════════════════════════════════════
     SECTION 4 — FULL 7-DAY CALENDAR
════════════════════════════════════════════════════ -->
<div class="section-header">
  <div class="section-icon icon-blue">📆</div>
  <h2>Full 7-Day Calendar</h2>
</div>

<!-- Thursday Aug 20 -->
<div class="cal-day">
  <div class="cal-day-header today">📅 Thursday, August 20, 2026 — TODAY</div>
  <div class="cal-event">
    <div class="cal-time">9:00 – 10:30 AM</div>
    <div>
      <div class="cal-name">Executive Roundtable</div>
      <div class="cal-detail">
        <span class="cal-rsvp rsvp-declined">DECLINED</span>
        <span class="tag">Zoom</span>
        <span class="tag">Invited by John Madigan</span><br>
        <span style="color:#718096;">Link: zoom.us/j/207786667 | ID: 207 786 667 | PW: 205454</span><br>
        <span class="note">You declined this event. No action needed unless you want to rejoin.</span>
      </div>
    </div>
  </div>
  <div class="cal-event">
    <div class="cal-time">12:00 – 1:00 PM</div>
    <div>
      <div class="cal-name">HR Networking & Job Search: Open Office Hours – Zoom 2</div>
      <div class="cal-detail">
        <span class="cal-rsvp rsvp-needs">⚠️ NEEDS ACTION</span>
        <span class="tag">170+ Attendees</span>
        <span class="tag">Zoom</span><br>
        <span style="color:#718096;">Link: zoom.us/j/85945371140 | Note: AI notetaking tools must be OFF</span><br>
        <span class="warn">⚠️ RSVP required — respond now. Strong networking opportunity.</span><br>
        <span class="note">Prep: Review group networking guidelines before joining.</span>
      </div>
    </div>
  </div>
</div>

<!-- Friday Aug 21 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Friday, August 21, 2026</div>
  <div class="cal-event">
    <div class="cal-time">10:30 – 11:00 AM</div>
    <div>
      <div class="cal-name">Tina/Melissa Connect</div>
      <div class="cal-detail">
        <span class="cal-rsvp rsvp-accepted">✅ ACCEPTED</span>
        <span class="tag">Microsoft Teams</span>
        <span class="tag">tina@msearchadvisory.com</span><br>
        <span style="color:#718096;">Teams: teams.microsoft.com/meet/250962901087907 | Passcode: eX3yZ9ev</span><br>
        <span class="note">Prep: MSearch Advisory is a search firm — review your talking points, resume, and target roles before this call. Research Tina's background on LinkedIn.</span>
      </div>
    </div>
  </div>
  <div class="cal-event">
    <div class="cal-time">12:00 – 12:30 PM</div>
    <div>
      <div class="cal-name">Zoom with Dee Dee</div>
      <div class="cal-detail">
        <span class="cal-rsvp rsvp-confirmed">✅ CONFIRMED</span>
        <span class="tag">Zoom</span><br>
        <span class="note">No location or description. Confirm Zoom link with Dee Dee in advance. Prep: TBD based on context of relationship.</span><br>
        <span class="cal-conflict">⚠️ Back-to-back with Tina call — allow buffer time between 11 AM and noon.</span>
      </div>
    </div>
  </div>
</div>

<!-- Saturday Aug 22 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Saturday, August 22, 2026</div>
  <div class="cal-event">
    <div class="cal-time">All Day</div>
    <div>
      <div class="cal-name">No Events Scheduled</div>
      <div class="cal-detail"><span class="note">Free day — consider using time for job applications or follow-up emails.</span></div>
    </div>
  </div>
</div>

<!-- Sunday Aug 23 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Sunday, August 23, 2026</div>
  <div class="cal-event">
    <div class="cal-time">All Day</div>
    <div>
      <div class="cal-name">💡 Verizon Fios Bill Due</div>
      <div class="cal-detail">
        <span class="cal-rsvp rsvp-confirmed">📌 REMINDER</span><br>
        <span class="warn">Pay by today to avoid late fees. Recommend paying Friday 8/21.</span>
      </div>
    </div>
  </div>
</div>

<!-- Monday Aug 24 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Monday, August 24, 2026</div>
  <div class="cal-event">
    <div class="cal-time">All Day</div>
    <div>
      <div class="cal-name">🎂 Michael Rich's Birthday</div>
      <div class="cal-detail">
        <span class="cal-rsvp rsvp-confirmed">📌 PERSONAL</span><br>
        <span class="note">Send a birthday message if you haven't already.</span>
      </div>
    </div>
  </div>
  <div class="cal-event">
    <div class="cal-time">9:15 – 10:15 AM</div>
    <div>
      <div class="cal-name">Elle (Personal Block / Placeholder)</div>
      <div class="cal-detail">
        <span class="cal-rsvp rsvp-confirmed">✅ CONFIRMED</span>
        <span class="tag">Personal</span><br>
        <span class="note">Appears to be a placeholder matching the salon appointment below.</span>
      </div>
    </div>
  </div>
  <div class="cal-event">
    <div class="cal-time">9:15 – 10:45 AM</div>
    <div>
      <div class="cal-name">✂️ Appointment at Elle at UMI Salon — Single Process with Blowout</div>
      <div class="cal-detail">
        <span class="cal-rsvp rsvp-confirmed">✅ CONFIRMED</span>
        <span class="tag">37 W 20th St, Suite 1107, NYC 10011</span>
        <span class="tag">Stylist: Elle M</span><br>
        <span style="color:#718096;">Manage: elleatumi.glossgenius.com/a/f3c8e149...</span><br>
        <span class="note">Allow travel time from home. Plan to arrive 5 min early.</span><br>
        <span class="cal-conflict">⚠️ "Elle" placeholder and salon appointment overlap — both show 9:15. Confirm no conflict.</span>
      </div>
    </div>
  </div>
</div>

<!-- Tuesday Aug 25 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Tuesday, August 25, 2026</div>
  <div class="cal-event">
    <div class="cal-time">9:30 – 10:30 AM</div>
    <div>
      <div class="cal-name">📞 Recruiter Call</div>
      <div class="cal-detail">
        <span class="cal-rsvp rsvp-confirmed">✅ CONFIRMED</span><br>
        <span class="note">No recruiter name, company, or dial-in details listed. Prep: Confirm call details via email. Have resume, target companies, and salary expectations ready. Could be related to Tina/MSearch or another outreach.</span>
      </div>
    </div>
  </div>
  <div class="cal-event">
    <div class="cal-time">4:30 – 5:30 PM</div>
    <div>
      <div class="cal-name">💅 Nails</div>
      <div class="cal-detail">
        <span class="cal-rsvp rsvp-confirmed">✅ CONFIRMED</span>
        <span class="tag">Personal</span><br>
        <span class="note">No location listed. Confirm appointment address/time if needed.</span>
      </div>
    </div>
  </div>
</div>

<!-- Wednesday Aug 26 -->
<div class="cal-day">
  <div class="cal-day-header">📅 Wednesday, August 26, 2026</div>
  <div class="cal-event">
    <div class="cal-time">All Day</div>
    <div>
      <div class="cal-name">💍 Amy's Anniversary</div>
      <div class="cal-detail">
        <span class="cal-rsvp rsvp-confirmed">📌 PERSONAL</span><br>
        <span class="note">Send a message or card to Amy. Michael Givner mentioned Amy and family in his email today — connection likely relevant.</span>
      </div>
    </div>
  </div>
  <div class="cal-event">
    <div class="cal-time">12:00 – 1:30 PM</div>
    <div>
      <div class="cal-name">HR Networking & Job Search Group – Zoom 2</div>
      <div class="cal-detail">
        <span class="cal-rsvp rsvp-needs">⚠️ NEEDS ACTION</span>
        <span class="tag">170+ Attendees</span>
        <span class="tag">Zoom</span><br>
        <span style="color:#718096;">Link: zoom.us/j/81954171722</span><br>
        <span class="warn">⚠️ RSVP still pending. Respond to invite. Note: 1.5-hour session with group agenda and resources.</span>
      </div>
    </div>
  </div>
  <div class="cal-event">
    <div class="cal-time">12:00 – 1:30 PM</div>
    <div>
      <div class="cal-name">Network (Personal Placeholder)</div>
      <div class="cal-detail">
        <span class="cal-rsvp rsvp-confirmed">✅ CONFIRMED</span>
        <span class="tag">Personal Block</span><br>
        <span class="note">Appears to be a self-created reminder that overlaps with the HR Networking Zoom above. Likely the same event.</span><br>
        <span class="cal-conflict">⚠️ Duplicate overlap — confirm whether this is the same HR networking session.</span>
      </div>
    </div>
  </div>
  <div class="cal-event">
    <div class="cal-time">3:00 – 4:00 PM</div>
    <div>
      <div class="cal-name">💅 Nails</div>
      <div class="cal-detail">
        <span class="cal-rsvp rsvp-confirmed">✅ CONFIRMED</span>
        <span class="tag">Personal</span><br>
        <span class="note">Second nail appointment this week (also on 8/25). Confirm which one is the actual appointment.</span><br>
        <span class="cal-conflict">⚠️ Two nail appointments in calendar (8/25 and 8/26) — verify and cancel the duplicate.</span>
      </div>
    </div>
  </div>
</div>

<!-- ════════════════════════════════════════════════════
     SECTION 5 — JOB SEARCH & INTERVIEW PIPELINE
════════════════════════════════════════════════════ -->
<div class="section-header">
  <div class="section-icon icon-green">💼</div>
  <h2>Job Search & Interview Pipeline</h2>
</div>

<table>
  <thead>
    <tr>
      <th>Fit</th>
      <th>Role / Company</th>
      <th>Source</th>
      <th>Salary / Type</th>
      <th>Status / Action</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="pri-high">HIGH</span></td>
      <td><strong>Vice President, Human Resources — Soni</strong></td>
      <td>LinkedIn Job Alerts (Inbox)</td>
      <td>$190K–$230K/yr</td>
      <td><span class="badge badge-green">Apply Today</span> Strong comp, VP-level match</td>
    </tr>
    <tr>
      <td><span class="pri-high">HIGH</span></td>
      <td><strong>Remote HR Manager — Turing</strong></td>
      <td>Indeed (Inbox)</td>
      <td>$100–$200/hr, Remote</td>
      <td><span class="badge badge-green">Review & Apply</span> High hourly rate, remote</td>
    </tr>
    <tr>
      <td><span class="pri-high">HIGH</span></td>
      <td><strong>VP, People & Culture — Greenbox Capital</strong></td>
      <td>LinkedIn Job Alerts (Inbox + duplicate)</td>
      <td>US Remote</td>
      <td><span class="badge badge-green">Apply Today</span> Strong level match, remote</td>
    </tr>
    <tr>
      <td><span class="pri-med">MED</span></td>
      <td><strong>People Partner, Technology — Stripe</strong></td>
      <td>LinkedIn Job Alerts (Inbox)</td>
      <td>50% on-site required</td>
      <td><span class="badge badge-yellow">Review Fit</span> Strong brand; hybrid may work</td>
    </tr>
    <tr>
      <td><span class="pri-med">MED</span></td>
      <td><strong>Global HR Business Partner — LeadVenture (+ 9 more)</strong></td>
      <td>Glassdoor (Trash — newsletter)</td>
      <td>Remote, US</td>
      <td><span class="badge badge-yellow">Check Glassdoor</span> HRBP level — assess fit</td>
    </tr>
    <tr>
      <td><span class="pri-med">MED</span></td>
      <td><strong>Senior Manager, Human Resources — Brooklyn Defender Services</strong></td>
      <td>Glassdoor (Trash)</td>
      <td>NYC, Nonprofit</td>
      <td><span class="badge badge-yellow">Consider</span> SM-level; NYC based</td>
    </tr>
    <tr>
      <td><span class="pri-low">LOW</span></td>
      <td><strong>Community Manager — Alpaca Health (+ 6 more)</strong></td>
      <td>Glassdoor (Trash)</td>
      <td>New York, NY</td>
      <td><span class="badge badge-gray">Skip</span> Not HR VP level</td>
    </tr>
  </tbody>
</table>

<!-- Networking & Recruiter -->
<div class="section-header" style="margin-top:20px;">
  <div class="section-icon icon-green">🤝</div>
  <h2>Recruiters & Networking Contacts</h2>
</div>
<table>
  <thead>
    <tr>
      <th>Contact</th>
      <th>Context</th>
      <th>Source</th>
      <th>Action</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Michael Givner</strong>, IMG Business Advisors</td>
      <td>Responded positively re: Crothers firm — knows founder 10 yrs. Warm relationship, mentions Amy.</td>
      <td>Email reply (Inbox, read)</td>
      <td><span class="badge badge-green">Follow Up — Request Crothers Intro</span></td>
    </tr>
    <tr>
      <td><strong>Tina</strong> (tina@msearchadvisory.com)</td>
      <td>MSearch Advisory — connect call scheduled tomorrow 10:30 AM Teams</td>
      <td>Calendar (Accepted)</td>
      <td><span class="badge badge-blue">Prep for tomorrow AM call</span></td>
    </tr>
    <tr>
      <td><strong>Dee Dee</strong></td>
      <td>Zoom call tomorrow 12:00–12:30 PM</td>
      <td>Calendar (Confirmed)</td>
      <td><span class="badge badge-blue">Confirm Zoom link</span></td>
    </tr>
    <tr>
      <td><strong>Heather Laing</strong>, CEO — Complex Caregiver Solutions</td>
      <td>LinkedIn connection request pending</td>
      <td>LinkedIn invite (Inbox)</td>
      <td><span class="badge badge-yellow">Review profile — accept if relevant</span></td>
    </tr>
    <tr>
      <td><strong>HR Networking Group</strong></td>
      <td>Open Office Hours today 12 PM + Group session Wed 8/26</td>
      <td>Calendar (Needs Action)</td>
      <td><span class="badge badge-yellow">RSVP both sessions now</span></td>
    </tr>
    <tr>
      <td><strong>Recruiter (Unknown)</strong></td>
      <td>Call scheduled Tue 8/25, 9:30 AM. No details in calendar.</td>
      <td>Calendar (Confirmed)</td>
      <td><span class="badge badge-yellow">Confirm dial-in details via email</span></td>
    </tr>
    <tr>
      <td><strong>Melissa (self)</strong></td>
      <td>Saved Claude prompt for LinkedIn About section rewrite as conversion copy</td>
      <td>Self-email (melissaw212@gmail.com)</td>
      <td><span class="badge badge-green">Use prompt to update LinkedIn About section</span></td>
    </tr>
    <tr>
      <td><strong>SHRM HR Jobs</strong></td>
      <td>27 new HR job listings (digest)</td>
      <td>SHRM (Not trash, not inbox)</td>
      <td><span class="badge badge-yellow">Browse if time allows</span></td>
    </tr>
  </tbody>
</table>

<!-- ════════════════════════════════════════════════════
     SECTION 6 — FULL EMAIL REVIEW BY CATEGORY
════════════════════════════════════════════════════ -->
<div class="section-header">
  <div class="section-icon icon-red">📂</div>
  <h2>Full Email Review by Category</h2>
</div>

<!-- 6A: Security / Risk -->
<div class="card red" style="margin-bottom:16px;">
  <div class="card-title">🔴 Security / Risk — 7 Emails</div>
  <div class="card-body">
    <table style="margin-top:10px;">
      <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Reason / Action</th></tr></thead>
      <tbody>
        <tr>
          <td>'GmailSupportTeam' &lt;melissaw212@tihmcenwdanxn.us&gt;</td>
          <td>Your Account has been locked on Thu,20 Aug-2026</td>
          <td><span class="phish-tag">AUTO-TRASHED — Phishing</span></td>
          <td>Fake account-lock threat; credential harvesting via urgency. Removed before delivery.</td>
        </tr>
        <tr>
          <td>'Mcafee® Alert' &lt;vxuusupportdso@kjvfxixb...com&gt;</td>
          <td>WARNING: melissaw212 Your McAfee Anti-Virus Expired TODAY</td>
          <td><span class="phish-tag">AUTO-TRASHED — Phishing</span></td>
          <td>Fake McAfee virus scare from random domain. Removed before delivery.</td>
        </tr>
        <tr>
          <td>'Payment-Declined' &lt;pxfvhhyksrargi...us&gt;</td>
          <td>Your Account Sirius XM Will Be Removed Today</td>
          <td><span class="phish-tag">AUTO-TRASHED — Phishing</span></td>
          <td>Fake SiriusXM payment/credential harvesting threat. Removed before delivery.</td>
        </tr>
        <tr>
          <td>'GmailSupportTeam' (melissaw212@tihmcenwdanxn.us)</td>
          <td>Account locked — Final Warning</td>
          <td><span class="phish-tag">AUTO-TRASHED — Phishing</span></td>
          <td>Same auto-trashed phishing email as above (duplicate entry in data). No action needed.</td>
        </tr>
        <tr>
          <td>melissaw212 &lt;zoftsupportmjzt@pelqs...com&gt;</td>
          <td>Your 200 Free Spins Ready To Claim!</td>
          <td><span class="auto-tag">Scam / Spam</span></td>
          <td>Spoofed sender using your own email address. Casino gambling scam. Trash immediately.</td>
        </tr>
        <tr>
          <td>ProfessionalWhosWhoPartner &lt;dxksupportevam@ueqml...com&gt;</td>
          <td>Congratulations, You've been nominated</td>
          <td><span class="auto-tag">Scam / Vanity Listing</span></td>
          <td>Fake "Who's Who" nomination — paid vanity listing scam. Trash immediately.</td>
        </tr>
        <tr>
          <td>Huang Wei &lt;service_tw@whirlpool.com&gt;</td>
          <td>Looking for a reliable replacement</td>
          <td><span class="auto-tag">Suspected Scam / BEC</span></td>
          <td>Spoofed Whirlpool address; "previous supplier passed away" is a classic business email compromise lure. Do not respond. Trash immediately.</td>
        </tr>
      </tbody>
    </table>
    <div class="card-action" style="margin-top:10px;"><strong>Action:</strong> The 4 auto-trashed phishing emails are handled. Manually trash and permanently delete the casino spam (spoofed as you), Who's Who scam, and Huang Wei BEC attempt immediately. Never click links in any of these.</div>
  </div>
</div>

<!-- 6B: Job Search -->
<div class="card green" style="margin-bottom:16px;">
  <div class="card-title">🟢 Job Search — 10 Emails</div>
  <div class="card-body">
    <table style="margin-top:10px;">
      <thead><tr><th>Sender</th><th>Subject</th><th>Fit</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>LinkedIn Job Alerts</td><td>VP Human Resources at Soni: up to $230K/yr</td><td><span class="pri-high">HIGH</span></td><td>Apply today</td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>Stripe People Partner, Technology (Inbox)</td><td><span class="pri-med">MED</span></td><td>Review fit / apply</td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>Greenbox Capital VP P&C (Inbox)</td><td><span class="pri-high">HIGH</span></td><td>Apply today</td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>Greenbox Capital VP P&C (duplicate, read)</td><td><span class="pri-high">HIGH</span></td><td>Already reviewed — ignore duplicate</td></tr>
        <tr><td>Indeed</td><td>Remote HR Managers @ Turing ($100–$200/hr)</td><td><span class="pri-high">HIGH</span></td><td>Apply today</td></tr>
        <tr><td>Glassdoor Jobs</td><td>Global HR BP at LeadVenture + 9 more (Trash)</td><td><span class="pri-med">MED</span></td><td>Review on Glassdoor</td></tr>
        <tr><td>Glassdoor Jobs</td><td>Community Mgr at Alpaca Health + 6 more (Trash)</td><td><span class="pri-low">LOW</span></td><td>Skip — not VP level</td></tr>
        <tr><td>Glassdoor Jobs</td><td>Sr Manager HR at Brooklyn Defender + 4 more (Trash)</td><td><span class="pri-med">MED</span></td><td>Review SM-level roles</td></tr>
        <tr><td>SHRM HR Jobs</td><td>27 New Human Resources Jobs</td><td><span class="pri-low">LOW</span></td><td>Browse if time allows</td></tr>
        <tr><td>Melissa (self)</td><td>Claude prompt — LinkedIn About rewrite</td><td>—</td><td>Use prompt now to update LinkedIn</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- 6C: Recruiters / Networking -->
<div class="card green" style="margin-bottom:16px;">
  <div class="card-title">🤝 Recruiters / Networking — 3 Emails</div>
  <div class="card-body">
    <table style="margin-top:10px;">
      <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>Michael Givner, IMG Business Advisors</td><td>Re: Melissa Weiss Resume and website</td><td>Follow up — request Crothers intro. Warm relationship.</td></tr>
        <tr><td>Heather Laing via LinkedIn</td><td>I'd like to connect — Founder, Complex Caregiver Solutions</td><td>Review profile; accept if relevant to HR search.</td></tr>
        <tr><td>Job Search Unlocked (Substack — Trash)</td><td>LinkedIn Optimization: The Job Titles</td><td>Low value — already in trash. Unsubscribe or delete.</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- 6D: Calendar / Events -->
<div class="card blue" style="margin-bottom:16px;">
  <div class="card-title">📅 Calendar / Events — 1 Email</div>
  <div class="card-body">
    <table style="margin-top:10px;">
      <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>AllEvents (Trash)</td><td>Events for Melissa, new recommendations</td><td>In trash. Low priority — delete or unsubscribe.</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- 6E: Financial / Billing -->
<div class="card yellow" style="margin-bottom:16px;">
  <div class="card-title">💳 Financial / Billing — 3 Emails</div>
  <div class="card-body">
    <table style="margin-top:10px;">
      <thead><tr><th>Sender</th><th>Subject</th><th>Due Date</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>Chase</td><td>Credit card statement available (ending 2754)</td><td>09/16/2026 — Min. $391</td><td>Log in, review statement, schedule payment</td></tr>
        <tr><td>Target Circle Card</td><td>Statement available (ending 7697)</td><td>Check online</td><td>Log in and schedule payment</td></tr>
        <tr><td>My Best Buy® Visa® (Citi)</td><td>Pop quiz: Ready to redeem points?</td><td>—</td><td>Low priority — promotional. Ignore or redeem points at leisure.</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- 6F: Professional Development -->
<div class="card purple" style="margin-bottom:16px;">
  <div class="card-title">📚 Professional Development — 4 Emails</div>
  <div class="card-body">
    <table style="margin-top:10px;">
      <thead><tr><th>Sender</th><th>Subject</th><th>Location</th><th>Recommendation</th></tr></thead>
      <tbody>
        <tr><td>Stanton Chase via LinkedIn (Trash)</td><td>Is Your Executive Leadership Still the Right Fit? Framework for Boards</td><td>Trash</td><td>Relevant to HR exec search — skim before deleting or save</td></tr>
        <tr><td>HRZone via LinkedIn (Trash)</td><td>Four-step framework for turning failure into fuel</td><td>Trash</td><td>Leadership content — skim if relevant, then delete</td></tr>
        <tr><td>BambooHR</td><td>Employee Happiness Up — eNPS Report</td><td>Not trash, not inbox</td><td>Relevant HR data for interviews. Read and save key stats.</td></tr>
        <tr><td>Alison Courses (Trash)</td><td>25% off Digital Certificates & Diplomas</td><td>Trash</td><td>Low value — delete</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- 6G: Personal -->
<div class="card gray" style="margin-bottom:16px;">
  <div class="card-title">👤 Personal — 5 Emails</div>
  <div class="card-body">
    <table style="margin-top:10px;">
      <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>OkCupid (Inbox)</td><td>Someone likes you</td><td>Personal — check at leisure</td></tr>
        <tr><td>Match (Inbox)</td><td>Profile view from Tim, 51, White Plains</td><td>Personal — check at leisure</td></tr>
        <tr><td>Facebook (Inbox)</td><td>21 updates: Noor, Dulce Tejada, Sandru Claudia</td><td>Personal — review when convenient</td></tr>
        <tr><td>Nextdoor — Yorkville Trending (Trash)</td><td>Hi all! (Jeff, Extras Casting Director, Teyana Taylor project)</td><td>Interesting local post — already trashed; fine to delete</td></tr>
        <tr><td>Amazon.com (Inbox)</td><td>Shipped: 1 Essentials item</td><td>Track delivery if needed; no action required</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- 6H: Medical / Health -->
<div class="card gray" style="margin-bottom:16px;">
  <div class="card-title">💊 Medical / Health (Spam) — 5 Emails</div>
  <div class="card-body">
    <p style="margin-bottom:8px;">All of these are spam/scam health product emails from random domains. None are legitimate. Trash and permanently delete all.</p>
    <table style="margin-top:6px;">
      <thead><tr><th>Sender
