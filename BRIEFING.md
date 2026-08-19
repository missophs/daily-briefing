html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa W — August 19, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrap { max-width: 1200px; margin: 0 auto; padding: 20px; }

  /* HEADER */
  .main-header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); color: white; border-radius: 16px; padding: 32px 36px; margin-bottom: 24px; box-shadow: 0 8px 32px rgba(0,0,0,0.25); }
  .main-header h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .main-header .subtitle { font-size: 15px; color: #a8b8d8; margin-top: 6px; }
  .header-meta { display: flex; gap: 28px; margin-top: 18px; flex-wrap: wrap; }
  .header-meta-item { background: rgba(255,255,255,0.1); border-radius: 8px; padding: 8px 16px; font-size: 13px; }
  .header-meta-item strong { color: #7dd3fc; display: block; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; }

  /* SECTION CONTAINERS */
  .section { background: white; border-radius: 12px; padding: 24px; margin-bottom: 20px; box-shadow: 0 2px 12px rgba(0,0,0,0.07); }
  .section-title { font-size: 17px; font-weight: 700; margin-bottom: 16px; display: flex; align-items: center; gap: 10px; padding-bottom: 10px; border-bottom: 2px solid #f0f2f5; }
  .section-title .icon { font-size: 20px; }

  /* COLOR BANDS */
  .band-red { border-left: 5px solid #ef4444; }
  .band-yellow { border-left: 5px solid #f59e0b; }
  .band-blue { border-left: 5px solid #3b82f6; }
  .band-green { border-left: 5px solid #10b981; }
  .band-purple { border-left: 5px solid #8b5cf6; }
  .band-gray { border-left: 5px solid #9ca3af; }
  .band-orange { border-left: 5px solid #f97316; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 18px; margin-bottom: 12px; border: 1px solid transparent; }
  .card-red { background: #fef2f2; border-color: #fca5a5; }
  .card-yellow { background: #fffbeb; border-color: #fcd34d; }
  .card-blue { background: #eff6ff; border-color: #93c5fd; }
  .card-green { background: #f0fdf4; border-color: #86efac; }
  .card-purple { background: #faf5ff; border-color: #c4b5fd; }
  .card-gray { background: #f9fafb; border-color: #e5e7eb; }
  .card-orange { background: #fff7ed; border-color: #fed7aa; }

  .card-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 4px; }
  .card-label-red { color: #dc2626; }
  .card-label-yellow { color: #d97706; }
  .card-label-blue { color: #2563eb; }
  .card-label-green { color: #059669; }
  .card-label-purple { color: #7c3aed; }
  .card-label-gray { color: #6b7280; }
  .card-label-orange { color: #ea580c; }

  .card-title { font-size: 15px; font-weight: 700; margin-bottom: 6px; }
  .card-meta { font-size: 12px; color: #6b7280; margin-bottom: 8px; }
  .card-body { font-size: 13px; }
  .card-row { display: flex; gap: 8px; margin-top: 6px; flex-wrap: wrap; }
  .card-field { font-size: 12px; }
  .card-field strong { color: #374151; }

  /* BADGES */
  .badge { display: inline-block; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 600; }
  .badge-red { background: #fee2e2; color: #dc2626; }
  .badge-yellow { background: #fef3c7; color: #d97706; }
  .badge-green { background: #d1fae5; color: #059669; }
  .badge-blue { background: #dbeafe; color: #2563eb; }
  .badge-purple { background: #ede9fe; color: #7c3aed; }
  .badge-gray { background: #f3f4f6; color: #6b7280; }
  .badge-orange { background: #ffedd5; color: #ea580c; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #f8fafc; font-weight: 600; text-align: left; padding: 10px 12px; border-bottom: 2px solid #e5e7eb; color: #374151; font-size: 12px; text-transform: uppercase; letter-spacing: 0.4px; }
  td { padding: 9px 12px; border-bottom: 1px solid #f0f2f5; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #fafbfc; }
  .triage-rescued td { background: #f0fdf4; }
  .triage-inbox td { background: #eff6ff; }
  .triage-summary td { background: #fafafa; font-style: italic; color: #6b7280; }

  /* EXECUTIVE SUMMARY */
  .exec-bullets { list-style: none; }
  .exec-bullets li { padding: 12px 16px; margin-bottom: 10px; border-radius: 8px; display: flex; gap: 12px; align-items: flex-start; font-size: 14px; }
  .exec-bullets li .bullet-icon { font-size: 22px; flex-shrink: 0; }

  /* CALENDAR */
  .cal-day { margin-bottom: 20px; }
  .cal-day-header { font-size: 14px; font-weight: 700; color: #1e40af; background: #dbeafe; padding: 7px 14px; border-radius: 8px; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center; }
  .cal-event { background: #f8fafc; border: 1px solid #e5e7eb; border-radius: 8px; padding: 12px 14px; margin-bottom: 8px; display: grid; grid-template-columns: 110px 1fr; gap: 12px; }
  .cal-time { font-weight: 700; font-size: 13px; color: #1e40af; }
  .cal-allday { font-size: 11px; color: #6b7280; }
  .cal-event-name { font-weight: 600; font-size: 14px; margin-bottom: 4px; }
  .cal-detail { font-size: 12px; color: #6b7280; margin-top: 2px; }
  .cal-link { color: #2563eb; font-size: 12px; text-decoration: none; word-break: break-all; }
  .cal-link:hover { text-decoration: underline; }
  .conflict-warn { background: #fef3c7; border: 1px solid #fcd34d; border-radius: 6px; padding: 4px 10px; font-size: 12px; color: #92400e; margin-top: 6px; }
  .rsvp-needs { color: #dc2626; font-weight: 600; }
  .rsvp-confirmed { color: #059669; font-weight: 600; }
  .rsvp-declined { color: #6b7280; font-weight: 600; }
  .rsvp-accepted { color: #2563eb; font-weight: 600; }

  /* PRIORITY */
  .priority-high { color: #dc2626; font-weight: 700; }
  .priority-med { color: #d97706; font-weight: 700; }
  .priority-low { color: #6b7280; font-weight: 600; }

  /* DASHBOARD GRID */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 14px; }
  .dash-card { border-radius: 10px; padding: 16px; border: 1px solid #e5e7eb; }
  .dash-card-title { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px; margin-bottom: 10px; }
  .dash-item { padding: 5px 0; border-bottom: 1px solid #f0f2f5; font-size: 13px; }
  .dash-item:last-child { border-bottom: none; }

  /* TOP 3 */
  .top3 { counter-reset: top3; }
  .top3-item { display: flex; gap: 16px; align-items: flex-start; padding: 16px; border-radius: 10px; margin-bottom: 12px; }
  .top3-num { width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 18px; flex-shrink: 0; }
  .top3-1 { background: #fef2f2; } .top3-1 .top3-num { background: #dc2626; color: white; }
  .top3-2 { background: #f0fdf4; } .top3-2 .top3-num { background: #059669; color: white; }
  .top3-3 { background: #eff6ff; } .top3-3 .top3-num { background: #2563eb; color: white; }
  .top3-content h3 { font-size: 15px; font-weight: 700; margin-bottom: 4px; }
  .top3-content p { font-size: 13px; color: #4b5563; }

  /* SEPARATOR */
  .sep { height: 1px; background: #e5e7eb; margin: 10px 0; }

  /* ACCOUNTING TABLE */
  .acct-total { font-weight: 700; background: #1a1a2e !important; color: white !important; }
  .acct-total td { color: white !important; }

  /* RESCUED BANNER */
  .rescued-banner { background: #d1fae5; border: 1px solid #6ee7b7; border-radius: 8px; padding: 8px 14px; font-size: 12px; color: #065f46; margin-bottom: 8px; }
  .phish-banner { background: #fee2e2; border: 1px solid #fca5a5; border-radius: 8px; padding: 8px 14px; font-size: 12px; color: #7f1d1d; margin-bottom: 8px; }

  /* RESPONSIVE */
  @media (max-width: 700px) {
    .cal-event { grid-template-columns: 1fr; }
    .header-meta { gap: 12px; }
    .dashboard-grid { grid-template-columns: 1fr; }
  }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SECTION 0: EMAIL TRIAGE QUICK LIST -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section band-blue">
  <div class="section-title"><span class="icon">⚡</span> Email Triage Quick List</div>
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
      <tr class="triage-rescued">
        <td><span class="badge badge-green">✅ RESCUED</span></td>
        <td>Kohl's (kohls.narvar.com)</td>
        <td>Your Kohl's order is arriving soon!</td>
        <td>Order #6727155633 — arriving soon. Rescued from Trash: transactional shipping notification.</td>
      </tr>
      <!-- INBOX -->
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>NYU Langone MyChart</td>
        <td>New Message in NYU Langone Health MyChart</td>
        <td>New message from your doctor/care team. Log in to view. Action required.</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>Claude</td>
        <td>Self-sent LinkedIn post link about prompt engineering / AI productivity.</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Melissa W (self)</td>
        <td>Job</td>
        <td>Self-sent LinkedIn job listing link — review for application.</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Ather Shahid (LinkedIn)</td>
        <td>Melissa A, I'd like to connect</td>
        <td>LinkedIn connection request from Ather Shahid, Project Manager at REMAP.ai.</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Match</td>
        <td>You've had a profile view from Noah</td>
        <td>Noah, 65, Brooklyn viewed your Match profile.</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>OkCupid</td>
        <td>Someone likes you</td>
        <td>Someone on OkCupid liked your profile — message them now.</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>Google</td>
        <td>You shared Google Account data with Steppa</td>
        <td>Confirmation you used Sign in with Google for Steppa app. Verify if intentional.</td>
      </tr>
      <tr class="triage-inbox">
        <td><span class="badge badge-blue">📥 INBOX</span></td>
        <td>David Schuchman (groups.io)</td>
        <td>[payitforwardhrjobleads] PSG of Mercer County Meeting 08/21</td>
        <td>HR networking event this Thursday 8/21 — Ed Samuel resume workshop.</td>
      </tr>
      <!-- TRASH SUMMARY ROWS -->
      <tr class="triage-summary">
        <td><span class="badge badge-red">🗑 AUTO-TRASHED</span></td>
        <td colspan="3">4 emails auto-trashed (2 phishing, + flagged spam) — see Trash Review &amp; Security/Risk sections below. Includes fake iCloud alerts and spoofed sender scams.</td>
      </tr>
      <tr class="triage-summary">
        <td><span class="badge badge-gray">🗂 TRASH (manual)</span></td>
        <td colspan="3">37 emails in Trash (promotional retail, newsletters, job digests, spam, duplicate sends) — see Trash Review section below.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SECTION 1: HEADER -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="main-header">
  <h1>☀️ Good Morning, Melissa</h1>
  <div class="subtitle">Executive Briefing — Wednesday, August 19, 2026</div>
  <div class="header-meta">
    <div class="header-meta-item"><strong>Date</strong>Wednesday, August 19, 2026</div>
    <div class="header-meta-item"><strong>Emails Reviewed</strong>50 Total</div>
    <div class="header-meta-item"><strong>Calendar Events</strong>11 Events</div>
    <div class="header-meta-item"><strong>Inbox (Active)</strong>8 Items Need Attention</div>
    <div class="header-meta-item"><strong>Auto-Trashed</strong>4 Phishing / Spam</div>
    <div class="header-meta-item"><strong>Today's Meetings</strong>2 Scheduled</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SECTION 2: EXECUTIVE SUMMARY -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section band-red">
  <div class="section-title"><span class="icon">📋</span> Executive Summary</div>
  <ul class="exec-bullets">
    <li class="card-red" style="border-radius:8px;">
      <span class="bullet-icon">🚨</span>
      <div><strong>Security Risk:</strong> 4 phishing/scam emails were auto-trashed before hitting your inbox — including two fake iCloud account-block threats (spoofed from your own address and from a bulk-mail domain). A fraudulent "CashApp $7,000 payment" and a casino/gambling spam are also in trash. Additionally, 5 low-quality spam emails remain in the non-trash folder (including two explicit/adult spam, a fake SiriusXM offer, a fake payment casino spam, and a joint-supplement pitch). <strong>No action needed on auto-trashed items; review non-trash spam for manual cleanup.</strong> Also verify the Google/Steppa sign-in notification was intentional.</div>
    </li>
    <li class="card-green" style="border-radius:8px;">
      <span class="bullet-icon">💼</span>
      <div><strong>Job Search Opportunity:</strong> You self-sent a LinkedIn job link (subject: "Job") and a prompt-engineering AI resource ("Claude") to yourself last night — both are sitting unread in your inbox waiting for action. A Glassdoor digest featuring Senior Director HR at JBT Marel and an Indeed alert for Senior Director, People Partners at Honor ($230K–$255K remote) were in your trash. A recruiter call is scheduled for Tuesday, August 25. <strong>Prioritize reviewing the self-sent job link and the Honor/JBT Marel listings today.</strong></div>
    </li>
    <li class="card-blue" style="border-radius:8px;">
      <span class="bullet-icon">📅</span>
      <div><strong>Calendar Deadline:</strong> You have two events TODAY starting at noon — the HR Networking &amp; Job Search Group Zoom (12:00–1:30 PM, RSVP still pending) and a personal "M&amp;m" meeting with Monte Montoya (2:00–3:00 PM, accepted). Tomorrow, the Executive Roundtable Zoom at 9 AM (you have DECLINED). Friday 8/21 has a PSG Mercer County resume workshop (email received). Next week: hair appointment at Elle at UMI Salon Monday 8/24, recruiter call Tuesday 8/25, and Verizon Fios bill due 8/23. <strong>RSVP to today's networking Zoom immediately.</strong></div>
    </li>
  </ul>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SECTION 3: ACTION REQUIRED -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section band-yellow">
  <div class="section-title"><span class="icon">⚠️</span> Action Required</div>

  <div class="card card-red">
    <div class="card-label card-label-red">🚨 Security — Verify</div>
    <div class="card-title">Google Account Data Shared with Steppa</div>
    <div class="card-meta">From: Google &lt;noreply-accounts@google.com&gt; | Received: Tue Aug 18, 2026</div>
    <div class="card-body">
      <div class="card-row"><span class="card-field"><strong>Why it matters:</strong> Google confirmed you used "Sign in with Google" to connect your account to an app called "Steppa." If this was not you, someone may have access to your Google account.</span></div>
      <div class="card-row"><span class="card-field"><strong>Next step:</strong> Visit myaccount.google.com → Security → Third-party apps — verify Steppa is an app you intentionally authorized, and revoke access if not.</span></div>
      <div class="card-row"><span class="card-field"><strong>Due:</strong> Today, August 19</span></div>
    </div>
  </div>

  <div class="card card-red">
    <div class="card-label card-label-red">🏥 Medical — Urgent</div>
    <div class="card-title">New Message in NYU Langone Health MyChart</div>
    <div class="card-meta">From: mychart.donotreply@nyulangone.org | Received: Tue Aug 18, 9:24 PM</div>
    <div class="card-body">
      <div class="card-row"><span class="card-field"><strong>Why it matters:</strong> A new message from your care team is waiting in MyChart. Could be test results, appointment info, or a clinical note.</span></div>
      <div class="card-row"><span class="card-field"><strong>Next step:</strong> Log in to NYU Langone MyChart immediately to read the message. Download the NYU Langone Health app for quick access.</span></div>
      <div class="card-row"><span class="card-field"><strong>Due:</strong> Today, August 19 — as soon as possible</span></div>
    </div>
  </div>

  <div class="card card-yellow">
    <div class="card-label card-label-yellow">📅 Calendar — RSVP Needed</div>
    <div class="card-title">RSVP: HR Networking &amp; Job Search Group Zoom — TODAY at 12:00 PM</div>
    <div class="card-meta">Calendar Event | Status: needsAction | Zoom Link Available</div>
    <div class="card-body">
      <div class="card-row"><span class="card-field"><strong>Why it matters:</strong> This networking session starts in a matter of hours. Your RSVP status is still "needsAction" — the organizers and 150+ attendees are expecting a response. This is directly tied to your active job search.</span></div>
      <div class="card-row"><span class="card-field"><strong>Next step:</strong> Accept or decline the calendar invite now. If attending, click the Zoom link at noon: <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" style="color:#2563eb">Zoom Link</a></span></div>
      <div class="card-row"><span class="card-field"><strong>Due:</strong> Today, August 19, 12:00 PM ET</span></div>
    </div>
  </div>

  <div class="card card-green">
    <div class="card-label card-label-green">💼 Job Search — High Priority</div>
    <div class="card-title">Review Self-Sent Job Link (LinkedIn)</div>
    <div class="card-meta">From: Melissa W (self-sent) | Subject: "Job" | Received: Tue Aug 18, 9:20 PM</div>
    <div class="card-body">
      <div class="card-row"><span class="card-field"><strong>Why it matters:</strong> You flagged a specific LinkedIn job posting for yourself last night. The link (linkedin.com/jobs/view/4455971608/) is sitting unread in your inbox — review it before other candidates get ahead.</span></div>
      <div class="card-row"><span class="card-field"><strong>Next step:</strong> Open the email, click the LinkedIn job link, assess fit, and apply or add to tracking pipeline. Cross-reference with your recruiter call on 8/25.</span></div>
      <div class="card-row"><span class="card-field"><strong>Due:</strong> Today, August 19</span></div>
    </div>
  </div>

  <div class="card card-green">
    <div class="card-label card-label-green">🤖 Professional Dev — Review</div>
    <div class="card-title">Review Self-Sent Claude / Prompt Engineering Resource</div>
    <div class="card-meta">From: Melissa W (self-sent) | Subject: "Claude" | Received: Tue Aug 18, 9:22 PM</div>
    <div class="card-body">
      <div class="card-row"><span class="card-field"><strong>Why it matters:</strong> You sent yourself a LinkedIn post about prompt engineering from René Remsik ("Stop rewriting your prompts over and over"). Given your active job search in HR/executive roles, AI literacy is a competitive differentiator.</span></div>
      <div class="card-row"><span class="card-field"><strong>Next step:</strong> Read the LinkedIn post. Consider sharing with your network or incorporating key techniques into your workflow/resume narrative.</span></div>
      <div class="card-row"><span class="card-field"><strong>Due:</strong> This week</span></div>
    </div>
  </div>

  <div class="card card-yellow">
    <div class="card-label card-label-yellow">💰 Billing — Upcoming</div>
    <div class="card-title">Verizon Fios Bill Due August 23</div>
    <div class="card-meta">Calendar Reminder | All-Day Event: Aug 23–24</div>
    <div class="card-body">
      <div class="card-row"><span class="card-field"><strong>Why it matters:</strong> Calendar reminder for Verizon Fios bill due this Sunday, August 23.</span></div>
      <div class="card-row"><span class="card-field"><strong>Next step:</strong> Log in to Verizon Fios account or set up auto-pay to ensure on-time payment. Avoid service interruption.</span></div>
      <div class="card-row"><span class="card-field"><strong>Due:</strong> Sunday, August 23</span></div>
    </div>
  </div>

  <div class="card card-green">
    <div class="card-label card-label-green">🔗 Networking — Decide</div>
    <div class="card-title">LinkedIn Connection Request: Ather Shahid, Project Manager @ REMAP.ai</div>
    <div class="card-meta">From: LinkedIn Invitations | Received: Wed Aug 19, 9:05 AM</div>
    <div class="card-body">
      <div class="card-row"><span class="card-field"><strong>Why it matters:</strong> REMAP.ai is an AI-focused company. Connecting with a PM there may open doors to referrals or industry insight during your job search.</span></div>
      <div class="card-row"><span class="card-field"><strong>Next step:</strong> Review Ather's profile on LinkedIn. Accept if relevant to your target roles/industry. Add a brief personalized message when accepting.</span></div>
      <div class="card-row"><span class="card-field"><strong>Due:</strong> This week</span></div>
    </div>
  </div>

  <div class="card card-yellow">
    <div class="card-label card-label-yellow">📦 Order Tracking — Note</div>
    <div class="card-title">Kohl's Order #6727155633 Arriving Soon (Rescued from Trash)</div>
    <div class="card-meta">From: Kohl's (kohls.narvar.com) | Rescued from Trash | Order Date: Aug 14, 2026</div>
    <div class="card-body">
      <div class="card-row"><span class="card-field"><strong>Why it matters:</strong> A transactional order-confirmation/shipping email was auto-trashed but rescued because it contains your order number and delivery status.</span></div>
      <div class="card-row"><span class="card-field"><strong>Next step:</strong> Monitor delivery. Check order status in the email or at kohls.com. Note the expected arrival date.</span></div>
      <div class="card-row"><span class="card-field"><strong>Due:</strong> Monitor this week</span></div>
    </div>
  </div>

  <div class="card card-purple">
    <div class="card-label card-label-purple">📅 Networking Event — This Week</div>
    <div class="card-title">PSG Mercer County Meeting — Thursday Aug 21: Resume Dos &amp; Don'ts</div>
    <div class="card-meta">From: David Schuchman via groups.io | Received: Mon Aug 17</div>
    <div class="card-body">
      <div class="card-row"><span class="card-field"><strong>Why it matters:</strong> FREE HR job-search networking group event this Thursday, August 21. Topic: "Optimize Your Resume: Dos &amp; Don'ts" with Ed Samuel. Directly relevant to your active search.</span></div>
      <div class="card-row"><span class="card-field"><strong>Next step:</strong> Register or confirm attendance. Add to calendar if not already there. Bring your resume for potential review.</span></div>
      <div class="card-row"><span class="card-field"><strong>Due:</strong> Thursday, August 21</span></div>
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SECTION 4: FULL 7-DAY CALENDAR -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section band-blue">
  <div class="section-title"><span class="icon">📅</span> Full 7-Day Calendar (Aug 19–25, 2026)</div>

  <!-- WEDNESDAY AUG 19 (TODAY) -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span>📅 Wednesday, August 19, 2026 — TODAY</span>
      <span class="badge badge-blue">2 Events</span>
    </div>

    <div class="cal-event">
      <div>
        <div class="cal-time">12:00 PM</div>
        <div class="cal-allday">– 1:30 PM</div>
        <div class="cal-allday" style="margin-top:4px;"><span class="badge badge-red">RSVP PENDING</span></div>
      </div>
      <div>
        <div class="cal-event-name">HR Networking &amp; Job Search Group — Zoom 2</div>
        <div class="cal-detail"><strong>Status:</strong> <span class="rsvp-needs">Needs Action — RSVP Required</span></div>
        <div class="cal-detail"><strong>Attendees:</strong> 150+ HR professionals in job search</div>
        <div class="cal-detail"><strong>Location:</strong> <a class="cal-link" href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1">Zoom Link</a></div>
        <div class="cal-detail"><strong>Prep:</strong> Review team guidelines (linked in description). Prepare elevator pitch and any job search updates to share. Have your resume ready.</div>
        <div class="conflict-warn">⚠️ CONFLICT: "Network" personal block also runs 12:00–1:30 PM — this appears to be the same event. Confirm and consolidate.</div>
      </div>
    </div>

    <div class="cal-event">
      <div>
        <div class="cal-time">12:00 PM</div>
        <div class="cal-allday">– 1:30 PM</div>
        <div class="cal-allday" style="margin-top:4px;"><span class="badge badge-green">CONFIRMED</span></div>
      </div>
      <div>
        <div class="cal-event-name">Network (Personal Block)</div>
        <div class="cal-detail"><strong>Status:</strong> <span class="rsvp-confirmed">Confirmed</span></div>
        <div class="cal-detail"><strong>Note:</strong> Likely corresponds to the HR Networking Zoom above. No separate location or attendees listed. May be a personal reminder block.</div>
        <div class="conflict-warn">⚠️ CONFLICT: Overlaps with HR Networking &amp; Job Search Group Zoom (same time slot). Likely duplicate — confirm and clean up calendar.</div>
      </div>
    </div>

    <div class="cal-event">
      <div>
        <div class="cal-time">2:00 PM</div>
        <div class="cal-allday">– 3:00 PM</div>
        <div class="cal-allday" style="margin-top:4px;"><span class="badge badge-green">ACCEPTED</span></div>
      </div>
      <div>
        <div class="cal-event-name">M&amp;m (Meeting with Monte Montoya)</div>
        <div class="cal-detail"><strong>Status:</strong> <span class="rsvp-accepted">Accepted</span></div>
        <div class="cal-detail"><strong>Attendees:</strong> monte.montoya@gmail.com</div>
        <div class="cal-detail"><strong>Location:</strong> Not specified — confirm with Monte if virtual or in-person</div>
        <div class="cal-detail"><strong>Prep:</strong> Confirm meeting details with Monte. Prepare agenda or talking points for whatever you're meeting about (personal or professional).</div>
      </div>
    </div>
  </div>

  <!-- THURSDAY AUG 20 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span>📅 Thursday, August 20, 2026</span>
      <span class="badge badge-blue">2 Events</span>
    </div>

    <div class="cal-event">
      <div>
        <div class="cal-time">9:00 AM</div>
        <div class="cal-allday">– 10:30 AM</div>
        <div class="cal-allday" style="margin-top:4px;"><span class="badge badge-gray">DECLINED</span></div>
      </div>
      <div>
        <div class="cal-event-name">Executive Roundtable (Hosted by John Madigan)</div>
        <div class="cal-detail"><strong>Status:</strong> <span class="rsvp-declined">Declined</span></div>
        <div class="cal-detail"><strong>Location:</strong> <a class="cal-link" href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09">Zoom Link</a> | Meeting ID: 207 786 667 | Password: 205454</div>
        <div class="cal-detail"><strong>Note:</strong> You have declined this event. No action needed unless you want to reconsider — Executive Roundtables can be valuable for your job search.</div>
      </div>
    </div>

    <div class="cal-event">
      <div>
        <div class="cal-time">12:00 PM</div>
        <div class="cal-allday">– 1:00 PM</div>
        <div class="cal-allday" style="margin-top:4px;"><span class="badge badge-red">RSVP PENDING</span></div>
      </div>
      <div>
        <div class="cal-event-name">HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
        <div class="cal-detail"><strong>Status:</strong> <span class="rsvp-needs">Needs Action — RSVP Required</span></div>
        <div class="cal-detail"><strong>Attendees:</strong> 150+ (same HR networking community)</div>
        <div class="cal-detail"><strong>Location:</strong> <a class="cal-link" href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1">Zoom Link</a></div>
        <div class="cal-detail"><strong>Prep:</strong> No automated AI note-taking tools per organizer request. Open discussion format — come with questions about your job search. Good time to raise specific challenges.</div>
        <div class="cal-detail"><strong>Note:</strong> Description emphasizes work-life balance and networking as a break from the job search grind.</div>
      </div>
    </div>
  </div>

  <!-- FRIDAY AUG 21 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span>📅 Friday, August 21, 2026</span>
      <span class="badge badge-gray">No Calendar Events — Email Alert</span>
    </div>
    <div class="cal-event">
      <div>
        <div class="cal-time">TBD</div>
        <div class="cal-allday">From email</div>
      </div>
      <div>
        <div class="cal-event-name">PSG of Mercer County: Resume Workshop — Ed Samuel</div>
        <div class="cal-detail"><strong>Source:</strong> Email from David Schuchman via groups.io (not yet on calendar)</div>
        <div class="cal-detail"><strong>Topic:</strong> "Optimize Your Resume: Dos &amp; Don'ts"</div>
        <div class="cal-detail"><strong>Prep:</strong> Add to Google Calendar. Prepare current resume to bring/share. Free event, open to all.</div>
        <div class="conflict-warn">📌 Reminder: This event from email is NOT yet on your Google Calendar. Add it now.</div>
      </div>
    </div>
  </div>

  <!-- SATURDAY AUG 22 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span>📅 Saturday, August 22, 2026</span>
      <span class="badge badge-gray">No Events</span>
    </div>
    <div class="cal-event">
      <div><div class="cal-time">—</div></div>
      <div><div class="cal-event-name" style="color:#9ca3af; font-style:italic;">No scheduled events.</div></div>
    </div>
  </div>

  <!-- SUNDAY AUG 23 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span>📅 Sunday, August 23, 2026</span>
      <span class="badge badge-yellow">1 Reminder</span>
    </div>
    <div class="cal-event">
      <div>
        <div class="cal-time">All Day</div>
        <div class="cal-allday"><span class="badge badge-yellow">BILL DUE</span></div>
      </div>
      <div>
        <div class="cal-event-name">Verizon Fios Bill Due</div>
        <div class="cal-detail"><strong>Status:</strong> Confirmed reminder</div>
        <div class="cal-detail"><strong>Prep:</strong> Log in to Verizon account or ensure auto-pay is set up. Pay before end of day to avoid late fees.</div>
      </div>
    </div>
  </div>

  <!-- MONDAY AUG 24 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span>📅 Monday, August 24, 2026</span>
      <span class="badge badge-blue">3 Events (incl. 1 Birthday)</span>
    </div>

    <div class="cal-event">
      <div>
        <div class="cal-time">All Day</div>
        <div class="cal-allday"><span class="badge badge-purple">BIRTHDAY</span></div>
      </div>
      <div>
        <div class="cal-event-name">🎂 Michael Rich's Birthday</div>
        <div class="cal-detail"><strong>Status:</strong> Confirmed reminder</div>
        <div class="cal-detail"><strong>Prep:</strong> Send a birthday message, card, or gift today. Don't let it slip by!</div>
      </div>
    </div>

    <div class="cal-event">
      <div>
        <div class="cal-time">9:15 AM</div>
        <div class="cal-allday">– 10:15 AM</div>
        <div class="cal-allday" style="margin-top:4px;"><span class="badge badge-green">CONFIRMED</span></div>
      </div>
      <div>
        <div class="cal-event-name">Elle (Personal Block)</div>
        <div class="cal-detail"><strong>Status:</strong> Confirmed</div>
        <div class="cal-detail"><strong>Note:</strong> Personal block corresponding to the salon appointment below. Likely a duplicate/reminder.</div>
      </div>
    </div>

    <div class="cal-event">
      <div>
        <div class="cal-time">9:15 AM</div>
        <div class="cal-allday">– 10:45 AM</div>
        <div class="cal-allday" style="margin-top:4px;"><span class="badge badge-green">CONFIRMED</span></div>
      </div>
      <div>
        <div class="cal-event-name">💇 Appointment at Elle at UMI Salon — Single Process with Blowout</div>
        <div class="cal-detail"><strong>Status:</strong> <span class="rsvp-confirmed">Confirmed</span></div>
        <div class="cal-detail"><strong>Stylist:</strong> Elle M</div>
        <div class="cal-detail"><strong>Service:</strong> Single Process (with Blowout)</div>
        <div class="cal-detail"><strong>Location:</strong> 37 West 20th Suite 1107, New York, NY 10011</div>
        <div class="cal-detail"><strong>Manage:</strong> <a class="cal-link" href="https://elleatumi.glossgenius.com/a/f3c8e149bb71d70194fb118806b6484d849a">Manage Appointment</a></div>
        <div class="cal-detail"><strong>Prep:</strong> Plan commute to Chelsea by 9:00 AM. Bring cash/card for tip. Confirm appointment 24 hrs in advance if required.</div>
      </div>
    </div>
  </div>

  <!-- TUESDAY AUG 25 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span>📅 Tuesday, August 25, 2026</span>
      <span class="badge badge-blue">2 Events</span>
    </div>

    <div class="cal-event">
      <div>
        <div class="cal-time">9:30 AM</div>
        <div class="cal-allday">– 10:30 AM</div>
        <div class="cal-allday" style="margin-top:4px;"><span class="badge badge-green">CONFIRMED</span></div>
      </div>
      <div>
        <div class="cal-event-name">📞 Recruiter Call</div>
        <div class="cal-detail"><strong>Status:</strong> <span class="rsvp-confirmed">Confirmed</span></div>
        <div class="cal-detail"><strong>Location:</strong> Not specified — likely phone or Zoom</div>
        <div class="cal-detail"><strong>Prep:</strong> Research the recruiter/agency. Update your LinkedIn and resume beforehand. Prepare your 30-second pitch, target role/level/compensation range, and availability. Review the self-sent job link and Honor/JBT Marel opportunities before this call. Have references ready. Look your best given the salon appt the day prior!</div>
      </div>
    </div>

    <div class="cal-event">
      <div>
        <div class="cal-time">4:30 PM</div>
        <div class="cal-allday">– 5:30 PM</div>
        <div class="cal-allday" style="margin-top:4px;"><span class="badge badge-green">CONFIRMED</span></div>
      </div>
      <div>
        <div class="cal-event-name">💅 Nails</div>
        <div class="cal-detail"><strong>Status:</strong> <span class="rsvp-confirmed">Confirmed</span></div>
        <div class="cal-detail"><strong>Location:</strong> Not specified</div>
        <div class="cal-detail"><strong>Prep:</strong> Confirm salon location and appointment. Allow travel time. A nice treat after the recruiter call!</div>
      </div>
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SECTION 5: JOB SEARCH & INTERVIEW PIPELINE -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section band-green">
  <div class="section-title"><span class="icon">💼</span> Job Search &amp; Interview Pipeline</div>

  <table>
    <thead>
      <tr>
        <th>Fit</th>
        <th>Source / Role</th>
        <th>Company</th>
        <th>Details</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="badge badge-red">HIGH</span></td>
        <td>Self-Sent Email (LinkedIn)</td>
        <td>Unknown — Review Link</td>
        <td>You flagged LinkedIn Job #4455971608 for yourself last night. Unread in inbox. Role/company unknown until you open it.</td>
        <td class="priority-high">Open &amp; apply today</td>
      </tr>
      <tr>
        <td><span class="badge badge-red">HIGH</span></td>
        <td>Indeed Alert (Trashed)</td>
        <td>Honor (Remote)</td>
        <td>Senior Director, People Partners — $230K–$255K/yr. Remote. Your background flagged as a match.</td>
        <td class="priority-high">Retrieve from trash, review, apply</td>
      </tr>
      <tr>
        <td><span class="badge badge-orange">MED-HIGH</span></td>
        <td>Glassdoor Alert (Trashed)</td>
        <td>JBT Marel + 8 others</td>
        <td>Senior Director, Human Resources at JBT Marel + 8 additional remote HR roles.</td>
        <td class="priority-med">Retrieve from trash, review JBT Marel listing</td>
      </tr>
      <tr>
        <td><span class="badge badge-green">NETWORK</span></td>
        <td>Calendar — Today 12:00 PM</td>
        <td>HR Networking Group Zoom</td>
        <td>150+ HR professionals. Weekly job search networking call. RSVP pending.</td>
        <td class="priority-high">RSVP &amp; attend today</td>
      </tr>
      <tr>
        <td><span class="badge badge-green">NETWORK</span></td>
        <td>Calendar — Tomorrow 12:00 PM</td>
        <td>HR Open Office Hours Zoom</td>
        <td>Open discussion, no AI note-taking. Good for candid job search support.</td>
        <td class="priority-med">RSVP for tomorrow</td>
      </tr>
      <tr>
        <td><span class="badge badge-green">NETWORK</span></td>
        <td>Email — groups.io</td>
        <td>PSG of Mercer County (8/21)</td>
        <td>Free resume workshop — Ed Samuel. "Optimize Your Resume: Dos &amp; Don'ts."</td>
        <td class="priority-med">Add to calendar, attend Thursday 8/21</td>
      </tr>
      <tr>
        <td><span class="badge badge-yellow">MED</span></td>
        <td>LinkedIn Invitation — Inbox</td>
        <td>REMAP.ai</td>
        <td>Ather Shahid, Project Manager, wants to connect. AI-focused company.</td>
        <td class="priority-med">Review profile, accept or decline</td>
      </tr>
      <tr>
        <td><span class="badge badge-yellow">MED</span></td>
        <td>LinkedIn (email notification)</td>
        <td>Mentor International Group</td>
        <td>Global recruitment specialist — someone you may know at Mentor International Group.</td>
        <td class="priority-low">Review if relevant to your search</td>
      </tr>
      <tr>
        <td><span class="badge badge-gray">PIPELINE</span></td>
        <td>Calendar — Tue Aug 25</td>
        <td>Unknown Recruiter</td>
        <td>Recruiter call confirmed for Tuesday 9:30–10:30 AM. No recruiter/company details in calendar.</td>
        <td class="priority-high">Prep for call — update resume, pitch, target comp</td>
      </tr>
    </tbody>
  </table>

</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SECTION 6: FULL EMAIL REVIEW BY CATEGORY -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title"><span class="icon">📂</span> Full Email Review by Category</div>

  <!-- SECURITY / RISK -->
  <div class="card card-red band-red" style="border-radius:10px; margin-bottom:16px;">
    <div class="card-label card-label-red">🔴 Security / Risk — 6 Emails</div>
    <div class="card-title">Phishing, Scams, and Account Alerts</div>
    <div class="sep"></div>
    <div class="phish-banner">🤖 2 emails were AUTO-TRASHED as high-confidence phishing before reaching your inbox:</div>
    <table style="margin-bottom:10px;">
      <thead><tr><th>Status</th><th>From</th><th>Subject</th><th>Reason</th></tr></thead>
      <tbody>
        <tr>
          <td><span class="badge badge-red">Auto-Trashed — Phishing</span></td>
          <td>'Storage_Support' (bulk-mail domain)</td>
          <td>Storage warning: protect your data now</td>
          <td>Spoofed iCloud storage alert from random domain — credential/payment harvesting phish. <em>No action needed.</em></td>
        </tr>
        <tr>
          <td><span class="badge badge-red">Auto-Trashed — Phishing</span></td>
          <td>melissaw212 (spoofed — signgroup.biz)</td>
          <td>We have blocked your account 🚫 Your photos and videos will be deleted…</td>
          <td>Fake iCloud account-block/deletion threat from spoofed sender demanding payment. <em>No action needed.</em></td>
        </tr>
      </tbody>
    </table>
    <div style="margin-bottom:8px; font-size:13px;"><strong>Additional security-relevant items:</strong></div>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>Google (noreply-accounts@google.com)</td>
          <td>You shared some Google Account data with Steppa</td>
          <td><span class="badge badge-yellow">📥 Inbox — Review</span></td>
          <td>Verify you authorized Steppa. Revoke if not. See Action Required.</td>
        </tr>
        <tr>
          <td>"💲CashApp💲" (fake — fvbfvacytoddqzdctsuogvpt.com)</td>
          <td>𝙔𝙤𝙪 𝙧𝙚𝙘𝙚𝙞𝙫𝙚𝙙 𝙖 𝙥𝙖𝙮𝙢𝙚𝙣𝙩 𝙤𝙛 $7,000.00 𝙐𝙎𝘿</td>
          <td><span class="badge badge-red">Trash (manual) — Scam</span></td>
          <td>Obvious casino/scam. Safe to delete permanently.</td>
        </tr>
        <tr>
          <td>'melissaw212' (fake — mwbyvrynwtrmcgpisdgjnlyr.com)</td>
          <td>Claim your $7000 welcome bonus and 150 free spins 🤑</td>
          <td><span class="badge badge-red">Trash (manual) — Scam</span></td>
          <td>Casino gambling spam. Safe to delete permanently.</td>
        </tr>
        <tr>
          <td>'Congratulations!' (fake domain)</td>
          <td>You have received a payment $2500.00</td>
          <td><span class="badge badge-red">Trash (manual) — Scam</span></td>
          <td>Slots of Vegas casino scam. Safe to delete permanently.</td>
        </tr>
      </tbody>
    </table>
    <div style="margin-top:10px; font-size:12px; color:#7f1d1d;"><strong>Recommended:</strong> Delete all scam/casino emails permanently. Verify Steppa Google sign-in. No credentials have been compromised based on available info, but remain vigilant.</div>
  </div>

  <!-- JOB SEARCH -->
  <div class="card card-green band-green" style="border-radius:10px; margin-bottom:16px;">
    <div class="card-label card-label-green">🟢 Job Search — 4 Emails</div>
    <div class="card-title">Job Alerts, Applications, and Opportunities</div>
    <div class="sep"></div>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>Melissa W (self)</td>
          <td>Job (LinkedIn link)</td>
          <td><span class="badge badge-blue">📥 Inbox — Unread</span></td>
          <td class="priority-high">Open &amp; review today — self-flagged opportunity</td>
        </tr>
        <tr>
          <td>Melissa W (self)</td>
          <td>Claude (LinkedIn prompt engineering post)</td>
          <td><span class="badge badge-blue">📥 Inbox — Unread</span></td>
          <td class="priority-med">Review for AI/productivity skill building</td>
        </tr>
        <tr>
          <td>Indeed (via Apple privaterelay)</td>
          <td>Senior Director, People Partners (Remote) @ Honor — $230K–$255K</td>
          <td><span class="badge badge-gray">Trashed (manual)</span></td>
          <td class="priority-high">Rescue from trash — highly relevant, strong salary</td>
        </tr>
        <tr>
          <td>Glassdoor Jobs</td>
          <td>Senior Director, Human Resources at JBT Marel + 8 more remote jobs</td>
          <td><span class="badge badge-gray">Trashed (manual)</span></td>
          <td class="priority-med">Rescue from trash — review JBT Marel &amp; other listings</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- RECRUITERS / NETWORKING -->
  <div class="card card-green band-green" style="border-radius:10px; margin-bottom:16px;">
    <div class="card-label card-label-green">🟢 Recruiters / Networking — 3 Emails</div>
    <div class="card-title">LinkedIn Connections, Networking Events</div>
    <div class="sep"></div>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>LinkedIn (Ather Shahid invitation)</td>
          <td>Melissa A, I'd like to connect — REMAP.ai PM</td>
          <td><span class="badge badge-blue">📥 Inbox — Unread</span></td>
          <td>Review profile, decide to accept or decline</td>
        </tr>
        <tr>
          <td>LinkedIn (messages-noreply)</td>
          <td>Someone at Mentor International Group you may know</td>
          <td><span class="badge badge-gray">Not in inbox (read)</span></td>
          <td>Review if relevant to your global HR/recruiting network</td>
        </tr>
        <tr>
          <td>David Schuchman (groups.io)</td>
          <td>[payitforwardhrjobleads] PSG of Mercer County Meeting 08/21 — Resume Workshop</td>
          <td><span class="badge badge-purple">Not in inbox — Active</span></td>
          <td class="priority-high">Add to calendar, attend Thursday 8/21</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- CALENDAR / EVENTS -->
  <div class="card card-blue band-blue" style="border-radius:10px; margin-bottom:16px;">
    <div class="card-label card-label-blue">🔵 Calendar / Events — 0 Emails</div>
    <div class="card-title">No dedicated calendar-invitation emails found in this batch — see Google Calendar section above for all events.</div>
  </div>

  <!-- MEDICAL / HEALTH -->
  <div class="card card-red band-red" style="border-radius:10px; margin-bottom:16px;">
    <div class="card-label card-label-red">🔴 Medical / Health — 2 Emails</div>
    <div class="card-title">Healthcare Communications</div>
    <div class="sep"></div>
    <table>
      <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>NYU Langone Health MyChart</td>
          <td>New Message in NYU Langone Health MyChart</td>
          <td><span class="badge badge-blue">📥 Inbox — Unread</span></td>
          <td class="priority-high">Log in to MyChart today — may be urgent clinical message</td
