<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa Weiss — August 11, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrap { max-width: 1200px; margin: 0 auto; padding: 24px 16px; }

  /* Header */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: white; border-radius: 16px; padding: 36px 40px; margin-bottom: 24px; box-shadow: 0 8px 32px rgba(0,0,0,0.18); }
  .header h1 { font-size: 2rem; font-weight: 700; letter-spacing: -0.5px; }
  .header .subtitle { font-size: 1.05rem; color: #a8b8d8; margin-top: 4px; }
  .header-stats { display: flex; gap: 32px; margin-top: 20px; flex-wrap: wrap; }
  .stat-box { background: rgba(255,255,255,0.1); border-radius: 10px; padding: 12px 22px; text-align: center; }
  .stat-box .num { font-size: 1.6rem; font-weight: 700; color: #e0e8ff; }
  .stat-box .lbl { font-size: 0.75rem; color: #a8b8d8; text-transform: uppercase; letter-spacing: 0.5px; }

  /* Section headers */
  .section { margin-bottom: 28px; }
  .section-header { display: flex; align-items: center; gap: 10px; margin-bottom: 14px; }
  .section-header h2 { font-size: 1.15rem; font-weight: 700; color: #1a1a2e; }
  .section-number { background: #1a1a2e; color: white; border-radius: 50%; width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; font-size: 0.8rem; font-weight: 700; flex-shrink: 0; }

  /* Color bands */
  .band-red { border-left: 5px solid #e53e3e; background: #fff5f5; }
  .band-yellow { border-left: 5px solid #d69e2e; background: #fffff0; }
  .band-blue { border-left: 5px solid #3182ce; background: #ebf8ff; }
  .band-green { border-left: 5px solid #38a169; background: #f0fff4; }
  .band-purple { border-left: 5px solid #805ad5; background: #faf5ff; }
  .band-gray { border-left: 5px solid #718096; background: #f7fafc; }
  .band-orange { border-left: 5px solid #dd6b20; background: #fffaf0; }

  /* Cards */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .card-title { font-weight: 700; font-size: 0.95rem; margin-bottom: 4px; }
  .card-meta { font-size: 0.78rem; color: #555; margin-bottom: 6px; }
  .card-body { font-size: 0.88rem; }
  .card-row { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 6px; }
  .tag { display: inline-block; border-radius: 4px; padding: 2px 8px; font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.4px; }
  .tag-red { background: #fed7d7; color: #9b2c2c; }
  .tag-yellow { background: #fefcbf; color: #744210; }
  .tag-green { background: #c6f6d5; color: #22543d; }
  .tag-blue { background: #bee3f8; color: #2a4365; }
  .tag-purple { background: #e9d8fd; color: #44337a; }
  .tag-gray { background: #e2e8f0; color: #2d3748; }
  .tag-orange { background: #feebc8; color: #7b341e; }

  /* Tables */
  table { width: 100%; border-collapse: collapse; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.07); font-size: 0.84rem; }
  th { background: #1a1a2e; color: white; padding: 10px 12px; text-align: left; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.4px; }
  td { padding: 9px 12px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) { background: #f7fafc; }
  tr:hover { background: #edf2f7; }

  /* Status badges */
  .status-badge { display: inline-block; border-radius: 12px; padding: 2px 10px; font-size: 0.72rem; font-weight: 700; }
  .s-rescued { background: #c6f6d5; color: #22543d; }
  .s-inbox { background: #bee3f8; color: #2a4365; }
  .s-trash-auto { background: #fed7d7; color: #9b2c2c; }
  .s-trash-manual { background: #e2e8f0; color: #4a5568; }
  .s-confirmed { background: #c6f6d5; color: #22543d; }
  .s-declined { background: #fed7d7; color: #9b2c2c; }
  .s-pending { background: #fefcbf; color: #744210; }
  .s-accepted { background: #c6f6d5; color: #22543d; }

  /* Priority */
  .p-high { color: #e53e3e; font-weight: 700; }
  .p-med { color: #d69e2e; font-weight: 700; }
  .p-low { color: #38a169; font-weight: 700; }

  /* Executive Summary */
  .exec-summary { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px; }
  .exec-card { border-radius: 12px; padding: 18px 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); }
  .exec-card .icon { font-size: 1.6rem; margin-bottom: 6px; }
  .exec-card h3 { font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px; font-weight: 700; }
  .exec-card p { font-size: 0.9rem; }

  /* Calendar */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { background: #16213e; color: white; border-radius: 8px 8px 0 0; padding: 8px 16px; font-weight: 700; font-size: 0.9rem; }
  .cal-event { background: white; border-left: 4px solid #3182ce; padding: 12px 16px; border-bottom: 1px solid #e2e8f0; }
  .cal-event:last-child { border-bottom: none; border-radius: 0 0 8px 8px; }
  .cal-event.declined { border-left-color: #e53e3e; background: #fff5f5; }
  .cal-event.pending { border-left-color: #d69e2e; background: #fffff0; }
  .cal-event.medical { border-left-color: #805ad5; background: #faf5ff; }
  .cal-event-title { font-weight: 700; font-size: 0.95rem; }
  .cal-event-time { font-size: 0.8rem; color: #555; margin-top: 2px; }
  .cal-event-detail { font-size: 0.82rem; color: #444; margin-top: 4px; }

  /* Dashboard grid */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; }
  .dash-widget { background: white; border-radius: 12px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .dash-widget h3 { font-size: 0.82rem; text-transform: uppercase; letter-spacing: 0.5px; color: #718096; margin-bottom: 10px; font-weight: 700; }
  .dash-widget ul { list-style: none; }
  .dash-widget li { padding: 4px 0; border-bottom: 1px solid #f0f0f0; font-size: 0.85rem; }
  .dash-widget li:last-child { border-bottom: none; }

  /* Top 3 */
  .top3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }
  .top3-card { background: linear-gradient(135deg, #1a1a2e, #0f3460); color: white; border-radius: 14px; padding: 22px 24px; box-shadow: 0 4px 16px rgba(0,0,0,0.15); }
  .top3-card .num { font-size: 2.5rem; font-weight: 900; color: rgba(255,255,255,0.15); line-height: 1; }
  .top3-card h3 { font-size: 1rem; font-weight: 700; margin-bottom: 6px; color: #e0e8ff; }
  .top3-card p { font-size: 0.85rem; color: #a8b8d8; }

  /* Accounting */
  .accounting-total { background: #1a1a2e; color: white; text-align: center; padding: 12px; border-radius: 8px; font-size: 1.1rem; font-weight: 700; margin-top: 10px; }

  /* Divider */
  .divider { border: none; border-top: 2px solid #e2e8f0; margin: 30px 0; }

  /* Warning box */
  .warn-box { background: #fff5f5; border: 1.5px solid #fc8181; border-radius: 8px; padding: 10px 14px; font-size: 0.85rem; color: #742a2a; margin-bottom: 10px; }
  .info-box { background: #ebf8ff; border: 1.5px solid #63b3ed; border-radius: 8px; padding: 10px 14px; font-size: 0.85rem; color: #2a4365; margin-bottom: 10px; }
  .note-box { background: #f0fff4; border: 1.5px solid #68d391; border-radius: 8px; padding: 10px 14px; font-size: 0.85rem; color: #22543d; margin-bottom: 10px; }

  /* Print */
  @media print { body { background: white; } .page-wrap { padding: 10px; } }

  /* Responsive */
  @media (max-width: 600px) { .header { padding: 20px; } .header h1 { font-size: 1.4rem; } .header-stats { gap: 12px; } }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ═══════════════════════════════════════════════════════ -->
<!--  SECTION 0 — EMAIL TRIAGE QUICK LIST                   -->
<!-- ═══════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">0</div>
    <h2>📋 Email Triage Quick List</h2>
  </div>
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
      <!-- INBOX EMAILS — individual rows -->
      <tr>
        <td><span class="status-badge s-inbox">📥 INBOX</span></td>
        <td>Michael Givner<br><small>mgivner@imgbusinessadvisors.com</small></td>
        <td><strong>Re: Melissa Weiss Resume and Website</strong></td>
        <td>Business advisor asking what ideal role/company looks like; shared your info broadly — <span class="p-high">needs reply</span></td>
      </tr>
      <tr>
        <td><span class="status-badge s-inbox">📥 INBOX</span></td>
        <td>SourceHire Jobs</td>
        <td>Interview Update — Confirm Work Authorization: Sr Director HR REQ93079</td>
        <td>Confidential employer needs visa/sponsorship confirmation to keep application moving — <span class="p-high">action required</span></td>
      </tr>
      <tr>
        <td><span class="status-badge s-inbox">📥 INBOX</span></td>
        <td>Bank of America</td>
        <td>Direct Deposit Credited — $760.38</td>
        <td>NYS DOL UI deposit to Personal Checking/Savings -7471 — <span class="p-high">note for records</span></td>
      </tr>
      <tr>
        <td><span class="status-badge s-inbox">📥 INBOX</span></td>
        <td>Bank of America</td>
        <td>Billing Dispute -2994 — Merchant Credit Issued</td>
        <td>Step 2 of 3 complete; merchant credit posted — monitor for Step 3</td>
      </tr>
      <tr>
        <td><span class="status-badge s-inbox">📥 INBOX</span></td>
        <td>Bank of America</td>
        <td>Billing Dispute -4018 — Merchant Credit Issued</td>
        <td>Step 2 of 3 complete; merchant credit posted — monitor for Step 3</td>
      </tr>
      <tr>
        <td><span class="status-badge s-inbox">📥 INBOX</span></td>
        <td>Bank of America</td>
        <td>Billing Dispute -2994 — Claim Reviewed by Merchant's Bank</td>
        <td>Older update for same dispute; Step 2 in progress</td>
      </tr>
      <tr>
        <td><span class="status-badge s-inbox">📥 INBOX</span></td>
        <td>Bank of America</td>
        <td>Billing Dispute -4018 — Claim Reviewed by Merchant's Bank</td>
        <td>Older update for same dispute; Step 2 in progress</td>
      </tr>
      <tr>
        <td><span class="status-badge s-inbox">📥 INBOX</span></td>
        <td>Anthropic</td>
        <td>Your Claude API Prompt Cache Hit Rate Is Low</td>
        <td>Caching system prompts could reduce API spend — low urgency, review when convenient</td>
      </tr>
      <tr>
        <td><span class="status-badge s-inbox">📥 INBOX</span></td>
        <td>Indeed</td>
        <td>HR Consultant @ EffectiveHiring — $59–$65/hr</td>
        <td>Strong HR leadership match flagged by Indeed — <span class="p-med">worth reviewing</span></td>
      </tr>
      <tr>
        <td><span class="status-badge s-inbox">📥 INBOX</span></td>
        <td>Inclusively</td>
        <td>Check Out These Recommended Jobs for You!</td>
        <td>Profile-based job recommendations from Inclusively platform</td>
      </tr>
      <tr>
        <td><span class="status-badge s-inbox">📥 INBOX</span></td>
        <td>LinkedIn</td>
        <td>Senior HRBP (US) at Viz.ai — up to $180K/year</td>
        <td>High-value senior HR alert — <span class="p-high">review ASAP</span></td>
      </tr>
      <tr>
        <td><span class="status-badge s-inbox">📥 INBOX</span></td>
        <td>SourceHire ATS Jobs</td>
        <td>Good Fit: Senior Program Manager</td>
        <td>Suggested role based on Sr Director HR application — questionable fit</td>
      </tr>
      <tr>
        <td><span class="status-badge s-inbox">📥 INBOX</span></td>
        <td>SourceHire ATS Jobs</td>
        <td>Good Fit: Teacher</td>
        <td>Suggested role based on Sr Director HR application — very low fit</td>
      </tr>
      <tr>
        <td><span class="status-badge s-inbox">📥 INBOX</span></td>
        <td>Dale Winston via LinkedIn</td>
        <td>Dale Accepted Your Invitation — Explore Their Network</td>
        <td>New LinkedIn connection accepted; networking opportunity</td>
      </tr>
      <tr>
        <td><span class="status-badge s-inbox">📥 INBOX</span></td>
        <td>Match.com</td>
        <td>Fred Likes You — See If It's Mutual</td>
        <td>Match.com notification — personal, low priority</td>
      </tr>
      <tr>
        <td><span class="status-badge s-inbox">📥 INBOX</span></td>
        <td>Old Navy</td>
        <td>Your Order Is Arriving Soon! — Order #1RG306N</td>
        <td>Order placed Aug 8; estimated delivery imminent</td>
      </tr>
      <tr>
        <td><span class="status-badge s-inbox">📥 INBOX</span></td>
        <td>Melissa W (Self)</td>
        <td>Job — Workday Link</td>
        <td>Self-sent link to People Relations Partner role (RB Workday) — follow up</td>
      </tr>
      <tr>
        <td><span class="status-badge s-inbox">📥 INBOX</span></td>
        <td>Melissa W (Self)</td>
        <td>(No subject) — LinkedIn Post Link</td>
        <td>Self-sent LinkedIn post about websites paying in USD — low priority</td>
      </tr>
      <tr>
        <td><span class="status-badge s-inbox">📥 INBOX</span></td>
        <td>Daniel Williams / Claude Code for Non-Coders</td>
        <td>You Turned Your Agent Into a Fabrication Engine</td>
        <td>Substack newsletter on AI agent prompting — read when convenient</td>
      </tr>
      <!-- SUMMARY ROW — AUTO TRASHED -->
      <tr style="background:#fff5f5;">
        <td><span class="status-badge s-trash-auto">🗑 TRASHED (auto)</span></td>
        <td colspan="2"><strong>7 emails auto-trashed (phishing/spam) — see Trash Review</strong></td>
        <td>Account_Security phishing, United Healthcare fake promo, adult spam, GLP-1 spam, and others removed automatically</td>
      </tr>
      <!-- SUMMARY ROW — MANUAL TRASH -->
      <tr style="background:#f7fafc;">
        <td><span class="status-badge s-trash-manual">🗂 TRASH (manual)</span></td>
        <td colspan="2"><strong>24 emails in Trash — see Trash Review</strong></td>
        <td>Newsletters, retail promos, job digests, adult spam, and low-value notifications already trashed</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════ -->
<!--  SECTION 1 — HEADER                                    -->
<!-- ═══════════════════════════════════════════════════════ -->
<div class="header">
  <div style="font-size:0.85rem; color:#a8b8d8; text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;">Executive Briefing</div>
  <h1>☀️ Good Morning, Melissa</h1>
  <div class="subtitle">Tuesday, August 11, 2026 &nbsp;|&nbsp; Prepared by Your Chief of Staff</div>
  <div class="header-stats">
    <div class="stat-box"><div class="num">50</div><div class="lbl">Emails Reviewed</div></div>
    <div class="stat-box"><div class="num">7</div><div class="lbl">Calendar Events</div></div>
    <div class="stat-box"><div class="num">3</div><div class="lbl">Action Items</div></div>
    <div class="stat-box"><div class="num">1</div><div class="lbl">Appt Today</div></div>
    <div class="stat-box"><div class="num">2</div><div class="lbl">Security Alerts</div></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════ -->
<!--  SECTION 2 — EXECUTIVE SUMMARY                         -->
<!-- ═══════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">2</div>
    <h2>Executive Summary</h2>
  </div>
  <div class="exec-summary">
    <div class="exec-card band-red card">
      <div class="icon">🚨</div>
      <h3>Biggest Risk / Urgent Item</h3>
      <p>Two phishing emails were auto-trashed (fake "Account_Security" credential harvester + fake United Healthcare prize scam). Multiple unsolicited adult-content and spam messages are in your inbox area — your email address appears on spam lists. No credentials were compromised as far as can be determined, but inbox hygiene is needed.</p>
    </div>
    <div class="exec-card band-green card">
      <div class="icon">💼</div>
      <h3>Biggest Job Search / Opportunity</h3>
      <p>Three high-priority items: (1) SourceHire needs your work authorization confirmation for the Sr Director HR role (REQ93079) — application paused until you reply. (2) Michael Givner (IMG Business Advisors) is actively networking on your behalf and wants to know your ideal target role. (3) Senior HRBP at Viz.ai ($180K/year) is a LinkedIn alert worth immediate review.</p>
    </div>
    <div class="exec-card band-blue card">
      <div class="icon">📅</div>
      <h3>Biggest Calendar / Deadline Item</h3>
      <p><strong>TODAY:</strong> MRI Brain W&amp;WO with IV Contrast at 159 E 53rd St, 6th Floor. Arrive by 8:50 AM; appointment starts 9:20 AM. You are confirmed. Plan travel accordingly and leave valuables at home as instructed. Two networking Zoom meetings on Wednesday require RSVP.</p>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════ -->
<!--  SECTION 3 — ACTION REQUIRED                           -->
<!-- ═══════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">3</div>
    <h2>⚡ Action Required</h2>
  </div>

  <div class="card band-red">
    <div class="card-row"><span class="tag tag-red">🔴 URGENT</span><span class="tag tag-red">Job Search</span></div>
    <div class="card-title" style="margin-top:8px;">Confirm Work Authorization — Sr Director HR Application (REQ93079)</div>
    <div class="card-meta">From: SourceHire Jobs &lt;jobs@sourcehire.app&gt; · Received: Tue Aug 11, 10:20 AM UTC</div>
    <div class="card-body">
      <strong>Why it matters:</strong> "Confidential" employer is actively waiting on your visa/sponsorship eligibility confirmation before advancing your application. Delay = application pause or rejection.<br>
      <strong>Recommended next step:</strong> Reply to SourceHire immediately confirming your work authorization status. If you are a US citizen or permanent resident, simply state that — it's a 2-minute email.<br>
      <strong>Due:</strong> Today — Aug 11, 2026
    </div>
  </div>

  <div class="card band-yellow">
    <div class="card-row"><span class="tag tag-yellow">🟡 HIGH PRIORITY</span><span class="tag tag-green">Job Search / Networking</span></div>
    <div class="card-title" style="margin-top:8px;">Reply to Michael Givner — Define Your Ideal Target Role</div>
    <div class="card-meta">From: Michael Givner &lt;mgivner@imgbusinessadvisors.com&gt; · Received: Tue Aug 11, 4:08 AM UTC</div>
    <div class="card-body">
      <strong>Why it matters:</strong> Michael has already shared your info with multiple people and an employment contact. He needs clarity on your ideal position type and company to direct referrals properly. This is warm, active advocacy — don't let it go cold.<br>
      <strong>Recommended next step:</strong> Send a 3–4 sentence reply: target title (Sr Director / VP HR or CPO), preferred company size/type, and whether you're open to contract vs. full-time. Attach updated resume if not yet sent.<br>
      <strong>Due:</strong> Today — Aug 11, 2026
    </div>
  </div>

  <div class="card band-yellow">
    <div class="card-row"><span class="tag tag-yellow">🟡 MEDIUM PRIORITY</span><span class="tag tag-blue">Calendar</span></div>
    <div class="card-title" style="margin-top:8px;">RSVP — HR Networking &amp; Job Search Group Zoom (Wednesday Aug 12)</div>
    <div class="card-meta">Calendar Event · Status: Needs Action · Wed Aug 12, 12:00–1:30 PM</div>
    <div class="card-body">
      <strong>Why it matters:</strong> Large HR networking session with 170+ attendees. Your RSVP is still pending ("needsAction"). You also have a duplicate "Network" block at the same time that is confirmed — clarify which is the intended event.<br>
      <strong>Recommended next step:</strong> Accept the HR Networking Zoom invite and confirm the Zoom link. Remove or reconcile the duplicate "Network" calendar block. Join: https://us06web.zoom.us/j/81954171722<br>
      <strong>Due:</strong> Before 12:00 PM Wednesday, Aug 12
    </div>
  </div>

  <div class="card band-green">
    <div class="card-row"><span class="tag tag-green">🟢 MEDIUM PRIORITY</span><span class="tag tag-green">Job Search</span></div>
    <div class="card-title" style="margin-top:8px;">Review High-Value Job Alert — Senior HRBP at Viz.ai (up to $180K)</div>
    <div class="card-meta">From: LinkedIn Job Alerts · Received: Tue Aug 11, 3:05 AM UTC</div>
    <div class="card-body">
      <strong>Why it matters:</strong> $180K compensation for a senior HRBP role is well-aligned with your profile. Alert from LinkedIn which typically surfaces roles matched to your application history.<br>
      <strong>Recommended next step:</strong> Open LinkedIn, review the Viz.ai HRBP posting, and apply or save if fit is confirmed. Also review self-sent Workday link for People Relations Partner role.<br>
      <strong>Due:</strong> Today or tomorrow — Aug 11–12, 2026
    </div>
  </div>

  <div class="card band-blue">
    <div class="card-row"><span class="tag tag-blue">🔵 TODAY</span><span class="tag tag-purple">Medical</span></div>
    <div class="card-title" style="margin-top:8px;">MRI Brain Appointment — Arrive by 8:50 AM</div>
    <div class="card-meta">Calendar · 159 E 53rd St, 6th Floor, NY 10022 · Phone: 646-754-2800</div>
    <div class="card-body">
      <strong>Why it matters:</strong> Medical imaging appointment confirmed for today. With IV contrast (W&amp;WO), be sure to follow any pre-scan hydration or fasting instructions.<br>
      <strong>Recommended next step:</strong> Leave home with enough time to arrive by 8:50 AM. Bring ID, insurance card. Leave jewelry/valuables at home per instructions. Appointment starts at 9:20 AM.<br>
      <strong>Due:</strong> TODAY 8:50 AM
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════ -->
<!--  SECTION 4 — FULL 7-DAY CALENDAR                       -->
<!-- ═══════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">4</div>
    <h2>📅 Full 7-Day Calendar (Aug 11–17, 2026)</h2>
  </div>

  <!-- Tuesday Aug 11 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Tuesday, August 11, 2026 — TODAY</div>
    <div class="cal-event medical">
      <div class="cal-event-title">🏥 MRI Brain W&amp;WO IVC (Brain MRI with &amp; without IV Contrast)</div>
      <div class="cal-event-time">⏰ Arrive: 8:50 AM · Appointment starts: 9:20 AM · Ends: ~9:40 AM</div>
      <div class="cal-event-detail">📍 159 E 53rd Street, 6th Floor, New York NY 10022 · 📞 646-754-2800</div>
      <div class="cal-event-detail"><span class="status-badge s-confirmed">✅ Confirmed</span></div>
      <div class="cal-event-detail" style="margin-top:6px;">
        <strong>Prep:</strong> Leave valuables at home. MRI-safe gown provided. Private dressing rooms/lockers available. Remove all body piercings. Arrive early for check-in. Follow any IV contrast pre-scan instructions from your doctor.
      </div>
    </div>
  </div>

  <!-- Wednesday Aug 12 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Wednesday, August 12, 2026</div>
    <div class="cal-event">
      <div class="cal-event-title">🏋️ Pt (Physical Therapy / Personal Training)</div>
      <div class="cal-event-time">⏰ 9:30 AM – 10:30 AM</div>
      <div class="cal-event-detail">📍 Location not specified</div>
      <div class="cal-event-detail"><span class="status-badge s-confirmed">✅ Confirmed</span></div>
      <div class="cal-event-detail" style="margin-top:6px;"><strong>Prep:</strong> Wear comfortable clothing; confirm location if not embedded in invite.</div>
    </div>
    <div class="cal-event pending">
      <div class="cal-event-title">🤝 HR Networking &amp; Job Search Group — Zoom Session 2</div>
      <div class="cal-event-time">⏰ 12:00 PM – 1:30 PM</div>
      <div class="cal-event-detail">📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a> (Meeting ID in invite)</div>
      <div class="cal-event-detail"><span class="status-badge s-pending">⚠️ RSVP Pending — Needs Action</span></div>
      <div class="cal-event-detail" style="margin-top:6px;">
        <strong>⚠️ Conflict:</strong> Overlaps with "Network" event at same time — both 12–1:30 PM. These may be duplicates; reconcile your calendar.<br>
        <strong>Attendees:</strong> 170+ HR professionals<br>
        <strong>Prep:</strong> Accept RSVP, prepare 30-second intro/pitch, review any pre-read materials linked in invite. Review Team Guidelines doc linked in description.
      </div>
    </div>
    <div class="cal-event">
      <div class="cal-event-title">🗂 Network (Duplicate / Placeholder Block)</div>
      <div class="cal-event-time">⏰ 12:00 PM – 1:30 PM</div>
      <div class="cal-event-detail">📍 No location specified</div>
      <div class="cal-event-detail"><span class="status-badge s-confirmed">✅ Confirmed</span></div>
      <div class="cal-event-detail" style="margin-top:6px;"><strong>⚠️ Note:</strong> Appears to be a placeholder that overlaps with the HR Networking Zoom above. Consider deleting or merging to avoid confusion.</div>
    </div>
  </div>

  <!-- Thursday Aug 13 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Thursday, August 13, 2026</div>
    <div class="cal-event declined">
      <div class="cal-event-title">🏢 Executive Roundtable (Hosted by John Madigan)</div>
      <div class="cal-event-time">⏰ 9:00 AM – 10:30 AM</div>
      <div class="cal-event-detail">📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> · Meeting ID: 207 786 667 · PW: 205454</div>
      <div class="cal-event-detail"><span class="status-badge s-declined">❌ You Declined</span></div>
      <div class="cal-event-detail" style="margin-top:6px;"><strong>Note:</strong> You declined this event. No action required unless you want to reverse the decision. Given your active job search, executive roundtables can be high-value networking — consider whether reconsideration makes sense.</div>
    </div>
    <div class="cal-event pending">
      <div class="cal-event-title">🤝 HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
      <div class="cal-event-time">⏰ 12:00 PM – 1:00 PM</div>
      <div class="cal-event-detail">📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a></div>
      <div class="cal-event-detail"><span class="status-badge s-pending">⚠️ RSVP Pending — Needs Action</span></div>
      <div class="cal-event-detail" style="margin-top:6px;"><strong>Note:</strong> No AI notetaking tools per organizer request. Open discussion / informal format. 170+ attendees. Great for warm networking. RSVP and prepare questions.<br><strong>Prep:</strong> Turn off Otter.ai or similar tools before joining.</div>
    </div>
    <div class="cal-event">
      <div class="cal-event-title">👥 m&amp;M (Meeting — likely Monte Montoya)</div>
      <div class="cal-event-time">⏰ 3:30 PM – 4:30 PM</div>
      <div class="cal-event-detail">📍 Location not specified · Attendee: monte.montoya@gmail.com</div>
      <div class="cal-event-detail"><span class="status-badge s-accepted">✅ Accepted</span></div>
      <div class="cal-event-detail" style="margin-top:6px;"><strong>Prep:</strong> Confirm location (virtual or in-person) with Monte. No description provided — clarify purpose of meeting if unknown.</div>
    </div>
  </div>

  <!-- Fri–Mon placeholder -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Friday Aug 14 — Monday Aug 17, 2026</div>
    <div class="cal-event">
      <div class="cal-event-title">📭 No events found for Aug 14–17</div>
      <div class="cal-event-detail">Your calendar appears clear for the remainder of the week. Use this time for follow-up job applications, networking outreach, and rest post-MRI.</div>
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════ -->
<!--  SECTION 5 — JOB SEARCH & INTERVIEW PIPELINE           -->
<!-- ═══════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">5</div>
    <h2>💼 Job Search &amp; Interview Pipeline</h2>
  </div>

  <div class="info-box">📌 You are actively applying for HR leadership roles, with a primary application at <strong>Confidential Employer (Sr Director HR, REQ93079)</strong> via SourceHire. Multiple job alerts, recruiters, and networking groups are active.</div>

  <table>
    <thead>
      <tr>
        <th>Priority</th>
        <th>Source</th>
        <th>Role / Opportunity</th>
        <th>Compensation</th>
        <th>Fit</th>
        <th>Next Step</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="p-high">🔴 HIGH</span></td>
        <td>SourceHire (In Progress)</td>
        <td>Sr Director of Human Resources — Confidential Employer (REQ93079)</td>
        <td>Not listed</td>
        <td><span class="tag tag-green">HIGH FIT</span></td>
        <td>Confirm work authorization TODAY — application on hold</td>
      </tr>
      <tr>
        <td><span class="p-high">🔴 HIGH</span></td>
        <td>LinkedIn Job Alert</td>
        <td>Senior HRBP (US) — Viz.ai</td>
        <td>Up to $180K/year</td>
        <td><span class="tag tag-green">HIGH FIT</span></td>
        <td>Review on LinkedIn and apply if aligned</td>
      </tr>
      <tr>
        <td><span class="p-high">🔴 HIGH</span></td>
        <td>Michael Givner, IMG Business Advisors</td>
        <td>Active referral / networking on Melissa's behalf</td>
        <td>—</td>
        <td><span class="tag tag-green">HIGH VALUE</span></td>
        <td>Reply with ideal role + company type today</td>
      </tr>
      <tr>
        <td><span class="p-med">🟡 MED</span></td>
        <td>Indeed</td>
        <td>HR Consultant — EffectiveHiring</td>
        <td>$59–$65/hr (~$120K+ annualized)</td>
        <td><span class="tag tag-yellow">MED FIT</span></td>
        <td>Review posting; contract vs. perm TBD</td>
      </tr>
      <tr>
        <td><span class="p-med">🟡 MED</span></td>
        <td>Self-Sent (Workday link)</td>
        <td>People Relations Partner — Company via Workday (RB)</td>
        <td>Not listed</td>
        <td><span class="tag tag-yellow">MED FIT</span></td>
        <td>Open the saved Workday link and apply</td>
      </tr>
      <tr>
        <td><span class="p-med">🟡 MED</span></td>
        <td>Inclusively</td>
        <td>Multiple recommended roles — profile-matched</td>
        <td>Varies</td>
        <td><span class="tag tag-yellow">MED FIT</span></td>
        <td>Log in to Inclusively and review recommendations</td>
      </tr>
      <tr>
        <td><span class="p-med">🟡 MED</span></td>
        <td>LinkedIn (PostJobFree / Dennis Gorelik)</td>
        <td>Senior HR Business Partner — Arch Capital Group, Manhattan NY 10001</td>
        <td>Not listed</td>
        <td><span class="tag tag-yellow">MED FIT</span></td>
        <td>Email was in trash — retrieve and review if interested</td>
      </tr>
      <tr>
        <td><span class="p-med">🟡 MED</span></td>
        <td>LinkedIn (Job Alerts)</td>
        <td>Regional HR Business Partner-Unions-NYC — Vaco by Highspring (and similar roles)</td>
        <td>Not listed</td>
        <td><span class="tag tag-yellow">MED FIT</span></td>
        <td>Review on LinkedIn — unions experience required</td>
      </tr>
      <tr>
        <td><span class="p-low">🟢 LOW</span></td>
        <td>SourceHire (Algorithm)</td>
        <td>Senior Program Manager (suggested via HR application)</td>
        <td>—</td>
        <td><span class="tag tag-gray">LOW FIT</span></td>
        <td>Skip — not aligned with HR career path</td>
      </tr>
      <tr>
        <td><span class="p-low">🟢 LOW</span></td>
        <td>SourceHire (Algorithm)</td>
        <td>Teacher (suggested via HR application)</td>
        <td>—</td>
        <td><span class="tag tag-red">NO FIT</span></td>
        <td>Skip — unrelated to target role</td>
      </tr>
      <tr>
        <td><span class="p-low">🟢 LOW</span></td>
        <td>SourceHire (Algorithm)</td>
        <td>Director of Corporate Development (M&amp;A) — suggested</td>
        <td>—</td>
        <td><span class="tag tag-red">NO FIT</span></td>
        <td>Skip — M&amp;A not HR-aligned</td>
      </tr>
      <tr>
        <td><span class="p-low">🟢 LOW</span></td>
        <td>SourceHire (Algorithm)</td>
        <td>Full Stack Developer — suggested</td>
        <td>—</td>
        <td><span class="tag tag-red">NO FIT</span></td>
        <td>Skip — not applicable</td>
      </tr>
      <tr>
        <td><span class="p-low">🟢 LOW</span></td>
        <td>Glassdoor (Trashed)</td>
        <td>ISO Relations Manager — Dexly Finance + 8 others, New York</td>
        <td>—</td>
        <td><span class="tag tag-gray">LOW FIT</span></td>
        <td>In trash — review only if Glassdoor alerts are useful</td>
      </tr>
      <tr>
        <td><span class="p-low">🟢 LOW</span></td>
        <td>JobLeads (Trashed)</td>
        <td>5 roles — Chief People Officer / Lead Talent / Culture / Change</td>
        <td>—</td>
        <td><span class="tag tag-yellow">MED FIT</span></td>
        <td>⚠️ In trash — CPO roles may be worth rescuing before deletion</td>
      </tr>
    </tbody>
  </table>

  <div style="margin-top:14px;">
    <div class="card band-purple">
      <div class="card-title">🤝 Networking Activity</div>
      <div class="card-body">
        <strong>Dale Winston (LinkedIn):</strong> Accepted your connection invite — explore their network for warm introductions.<br>
        <strong>HR Networking Group (Aug 12 &amp; 13):</strong> Two large Zoom networking sessions this week — both pending RSVP.<br>
        <strong>Executive Roundtable (Aug 13):</strong> Declined — reconsider if John Madigan is a valuable contact.<br>
        <strong>m&amp;M with Monte Montoya (Aug 13, 3:30 PM):</strong> Meeting accepted — purpose unclear; confirm agenda.
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════ -->
<!--  SECTION 6 — FULL EMAIL REVIEW BY CATEGORY             -->
<!-- ═══════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">6</div>
    <h2>📧 Full Email Review by Category</h2>
  </div>

  <!-- 6A Security / Risk -->
  <div class="card band-red" style="margin-bottom:14px;">
    <div class="card-row"><span class="tag tag-red">🔴 Security / Risk</span><span class="tag tag-gray">4 emails</span></div>
    <div class="card-title" style="margin-top:8px;">Security &amp; Risk Emails</div>
    <table style="margin-top:10px;">
      <thead><tr><th>Status</th><th>From</th><th>Subject</th><th>Risk</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td><span class="tag tag-red">Auto-Trashed</span></td>
          <td>🚨 Account_Security (spoofed) &lt;4bg7up0vdg@l3w28320wo.us&gt;</td>
          <td>🔴 Your 1TB is Full — Account Lapsed ⚠️ (unicode-obfuscated)</td>
          <td><strong>PHISHING</strong> — credential harvesting. Spoofed sender, random domain, urgent suspension threat, unicode tricks.</td>
          <td>Auto-removed. No action needed. ✅</td>
        </tr>
        <tr>
          <td><span class="tag tag-red">Auto-Trashed</span></td>
          <td>🚨 United_Healthcare_Promo &lt;contact@gl8qdk8hgl8qdk8h.com&gt;</td>
          <td>melissaw212 Claim Your Free Oral-B Dental Kit</td>
          <td><strong>SCAM</strong> — fake UHC promo, random domain, prize/survey lure.</td>
          <td>Auto-removed. No action needed. ✅</td>
        </tr>
        <tr>
          <td><span class="tag tag-gray">In Inbox</span></td>
          <td>Anthropic &lt;no-reply@mail.anthropic.com&gt;</td>
          <td>Your Claude API Prompt Cache Hit Rate Is Low</td>
          <td>Legitimate Anthropic notification — low urgency technical advisory</td>
          <td>Review when convenient. Consider implementing caching to reduce API cost.</td>
        </tr>
        <tr>
          <td><span class="tag tag-gray">Not in inbox</span></td>
          <td>Robinhood &lt;noreply@robinhood.com&gt;</td>
          <td>Your Trade Confirmations Are Available</td>
          <td>Legitimate — recent trades settled</td>
          <td>Log into Robinhood to review confirmations. File for records.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- 6B Job Search -->
  <div class="card band-green" style="margin-bottom:14px;">
    <div class="card-row"><span class="tag tag-green">💼 Job Search</span><span class="tag tag-gray">14 emails</span></div>
    <div class="card-title" style="margin-top:8px;">Job Search Emails — All Sources</div>
    <table style="margin-top:10px;">
      <thead><tr><th>From</th><th>Subject / Role</th><th>Fit</th><th>Location</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>SourceHire Jobs</td><td>Interview Update — Sr Director HR REQ93079 (Work Auth Confirm)</td><td><span class="tag tag-green">HIGH</span></td><td>Confidential</td><td>⚡ Reply TODAY</td></tr>
        <tr><td>LinkedIn Job Alerts</td><td>Senior HRBP (US) — Viz.ai up to $180K</td><td><span class="tag tag-green">HIGH</span></td><td>US Remote</td><td>Review &amp; apply</td></tr>
        <tr><td>Indeed</td><td>HR Consultant — EffectiveHiring $59–$65/hr</td><td><span class="tag tag-yellow">MED</span></td><td>NY</td><td>Review</td></tr>
        <tr><td>Inclusively</td><td>Recommended jobs based on profile</td><td><span class="tag tag-yellow">MED</span></td><td>Various</td><td>Log in and review</td></tr>
        <tr><td>SourceHire ATS</td><td>Senior Program Manager (suggested)</td><td><span class="tag tag-gray">LOW</span></td><td>—</td><td>Skip</td></tr>
        <tr><td>SourceHire ATS</td><td>Teacher (suggested)</td><td><span class="tag tag-red">NO FIT</span></td><td>—</td><td>Skip / Ignore</td></tr>
        <tr><td>SourceHire Jobs</td><td>Director of Corporate Development M&amp;A (suggested)</td><td><span class="tag tag-red">NO FIT</span></td><td>—</td><td>Skip</td></tr>
        <tr><td>SourceHire Jobs</td><td>Full Stack Developer (suggested)</td><td><span class="tag tag-red">NO FIT</span></td><td>—</td><td>Skip</td></tr>
        <tr><td>LinkedIn</td><td>Regional HR Business Partner-Unions-NYC — Vaco by Highspring</td><td><span class="tag tag-yellow">MED</span></td><td>NYC</td><td>Review — unions exp. req.</td></tr>
        <tr><td>Dennis Gorelik / PostJobFree (Trash)</td><td>Senior HR Business Partner — Arch Capital Group, Manhattan</td><td><span class="tag tag-yellow">MED</span></td><td>Manhattan NY 10001</td><td>Rescue from trash &amp; review</td></tr>
        <tr><td>Glassdoor (Trash)</td><td>ISO Relations Manager @ Dexly Finance + 8 others</td><td><span class="tag tag-gray">LOW</span></td><td>New York NY</td><td>Low priority; delete</td></tr>
        <tr><td>JobLeads (Trash)</td><td>5 roles — CPO / Lead Talent / Culture / Change</td><td><span class="tag tag-yellow">MED</span></td><td>Various</td><td>⚠️ Rescue — CPO roles worth reviewing</td></tr>
        <tr><td>Melissa W (Self)</td><td>Job — Workday link (People Relations Partner)</td><td><span class="tag tag-yellow">MED</span></td><td>NY</td><td>Open link and apply</td></tr>
        <tr><td>Melissa W (Self)</td><td>(No subject) — LinkedIn post re: websites paying USD</td><td><span class="tag tag-gray">LOW</span></td><td>—</td><td>Review when convenient</td></tr>
      </tbody>
    </table>
  </div>

  <!-- 6C Recruiters / Networking -->
  <div class="card band-green" style="margin-bottom:14px;">
    <div class="card-row"><span class="tag tag-green">🤝 Recruiters / Networking</span><span class="tag tag-gray">2 emails</span></div>
    <table style="margin-top:10px;">
      <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>Michael Givner, IMG Business Advisors</td><td>Re: Melissa Weiss Resume and Website — What's your ideal role?</td><td>⚡ Reply TODAY — define target role, company type, contract vs. perm</td></tr>
        <tr><td>Dale Winston via LinkedIn</td><td>Dale Accepted Your Invitation — Explore Their Network</td><td>Connect and explore their network; send a personalized note</td></tr>
      </tbody>
    </table>
  </div>

  <!-- 6D Calendar / Events -->
  <div class="card band-blue" style="margin-bottom:14px;">
    <div class="card-row"><span class="tag tag-blue">📅 Calendar / Events</span><span class="tag tag-gray">0 standalone emails</span></div>
    <div class="card-body">All calendar events are reflected directly in the Calendar section above. No standalone calendar-related emails require separate action beyond what is noted in Section 4.</div>
  </div>

  <!-- 6E Medical / Health -->
  <div class="card band-purple" style="margin-bottom:14px;">
    <div class="card-row"><span class="tag tag-purple">🏥 Medical / Health</span><span class="tag tag-gray">1 calendar item (no emails)</span></div>
    <div class="card-body">MRI Brain appointment is calendar-based (see Section 4). No standalone medical emails received today.</div>
  </div>

  <!-- 6F Financial / Billing -->
  <div class="card band-yellow" style="margin-bottom:14px;">
    <div class="card-row"><span class="tag tag-yellow">💰 Financial / Billing</span><span class="tag tag-gray">5 emails</span></div>
    <table style="margin-top:10px;">
      <thead><tr><th>From</th><th>Subject</th><th>Details</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>Bank of America</td><td>Direct Deposit — $760.38 Credited</td><td>NYS DOL UI (Unemployment Insurance) · Account -7471 · Aug 11</td><td>Note for records; confirm amount is correct</td></tr>
        <tr><td>Bank of America</td><td>Billing Dispute -2994 — Merchant Credit Issued</td><td>Step 2 of 3 complete; merchant credited</td><td>Monitor for Step 3 (Final Resolution)</td></tr>
        <tr><td>Bank of America</td><td>Billing Dispute -4018 — Merchant Credit Issued</td><td>Step 2 of 3 complete; merchant credited</td><td>Monitor for Step 3 (Final Resolution)</td></tr>
        <tr><td>Bank of America</td><td>Billing Dispute -2994 — Claim Under Review by Merchant's Bank</td><td>Older Step 2 update for same -2994 dispute</td><td>Superseded by credit notice above; archive</td></tr>
        <tr><td>Bank of America</td><td>Billing Dispute -4018 — Claim Under Review by Merchant's Bank</td><td>Older Step 2 update for same -4018 dispute</td><td>Superseded by credit notice above; archive</td></tr>
      </tbody>
    </table>
    <div class="note-box" style="margin-top:10px;">📌 Two billing disputes on accounts -2994 and -4018 have both progressed to merchant credit (Step 2 of 3). Both are proceeding favorably. Watch for Step 3 final resolution notices.</div>
  </div>

  <!-- 6G Professional Development -->
  <div class="card band-purple" style="margin-bottom:14px;">
    <div class="card-row"><span class="tag tag-purple">📚 Professional Development</span><span class="tag tag-gray">2 emails</span></div>
    <table style="margin-top:10px;">
      <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>BambooHR &lt;email@news.bamboohr.com&gt;</td><td>Are Your Employees Afraid to Come to HR? — 6 barriers to trust</td><td>Relevant to HR leadership role — read when convenient; consider sharing insights in networking calls</td></tr>
        <tr><td>Daniel Williams / Claude Code for Non-Coders (Substack)</td><td>You Turned Your Agent Into a Fabrication Engine</td><td>AI literacy content — read when convenient; aligns with tech-forward HR practice</td></tr>
      </tbody>
    </table>
  </div>

  <!-- 6H Personal -->
  <div class="card band-gray" style="margin-bottom:14px;">
    <div class="card-row"><span class="tag tag-gray">👤 Personal</span><span class="tag tag-gray">2 emails</span></div>
    <table style="margin-top:10px;">
      <thead><tr><th>From</th><th>Subject</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>Match.com</td><td>Fred Likes You — See If It's Mutual</td><td>Personal — check when convenient</td></tr>
        <tr><td>Match.com (Not Inbox)</td><td>Bestheartofall Likes You &amp; Tim Viewed Your Profile</td><td>Personal — not in primary inbox; check Match app when convenient</td></tr>
      </tbody>
    </table>
  </div>

  <!-- 6I Newsletters -->
  <div class="card band-purple" style="margin-bottom:14px;">
    <div class="card-row"><span class="tag tag-purple">📰 Newsletters / Subscriptions</span><span class="tag tag-gray">3 emails</span></div>
    <table style="margin-top:10px;">
      <thead><tr><th>From</th><th>Subject</th><th>Recommendation</th></tr></thead>
      <tbody>
        <tr><td>Dylan's Diary &lt;newsletter@lg.behindthemarkets.com&gt; (Trash)</td><td>The Pentagon Just Made History</td><td>In Trash — Unsubscribe; finance/warfare newsletter not relevant</td></tr>
        <tr><td>The Daily Skim
