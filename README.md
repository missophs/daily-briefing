<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa | Sunday, June 28, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* Header */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 16px; padding: 36px 40px; margin-bottom: 24px; }
  .header h1 { font-size: 2rem; font-weight: 700; letter-spacing: -0.5px; }
  .header .subtitle { font-size: 1rem; color: #a8c0e8; margin-top: 4px; }
  .header-meta { display: flex; gap: 32px; margin-top: 20px; flex-wrap: wrap; }
  .meta-pill { background: rgba(255,255,255,0.1); border-radius: 8px; padding: 8px 18px; font-size: 0.85rem; }
  .meta-pill span { font-weight: 700; font-size: 1.1rem; display: block; color: #7dd3fc; }

  /* Section headers */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 1.1rem; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; padding: 10px 16px; border-radius: 8px 8px 0 0; margin-bottom: 0; }
  .section-body { background: #fff; border-radius: 0 0 12px 12px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .section-body-standalone { background: #fff; border-radius: 12px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }

  /* Color themes */
  .red-theme .section-title { background: #dc2626; color: #fff; }
  .yellow-theme .section-title { background: #d97706; color: #fff; }
  .blue-theme .section-title { background: #2563eb; color: #fff; }
  .green-theme .section-title { background: #16a34a; color: #fff; }
  .purple-theme .section-title { background: #7c3aed; color: #fff; }
  .gray-theme .section-title { background: #6b7280; color: #fff; }
  .navy-theme .section-title { background: #1e3a5f; color: #fff; }

  /* Executive Summary bullets */
  .exec-bullets { list-style: none; }
  .exec-bullets li { padding: 12px 16px; border-radius: 8px; margin-bottom: 10px; font-size: 0.95rem; display: flex; align-items: flex-start; gap: 10px; }
  .exec-bullets li .icon { font-size: 1.2rem; flex-shrink: 0; }
  .bullet-red { background: #fef2f2; border-left: 4px solid #dc2626; }
  .bullet-green { background: #f0fdf4; border-left: 4px solid #16a34a; }
  .bullet-blue { background: #eff6ff; border-left: 4px solid #2563eb; }

  /* Action cards */
  .action-card { border-radius: 10px; padding: 16px 20px; margin-bottom: 14px; border-left: 5px solid; }
  .action-red { background: #fef2f2; border-color: #dc2626; }
  .action-yellow { background: #fffbeb; border-color: #d97706; }
  .action-blue { background: #eff6ff; border-color: #2563eb; }
  .action-green { background: #f0fdf4; border-color: #16a34a; }
  .action-purple { background: #faf5ff; border-color: #7c3aed; }
  .card-label { font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; }
  .card-title { font-size: 1rem; font-weight: 700; margin-bottom: 6px; }
  .card-row { font-size: 0.85rem; margin-bottom: 3px; color: #374151; }
  .card-row strong { color: #1a1a2e; }
  .card-action { background: #1a1a2e; color: #fff; border-radius: 6px; padding: 4px 12px; font-size: 0.8rem; font-weight: 600; display: inline-block; margin-top: 8px; }

  /* Calendar */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { background: #1e3a5f; color: #fff; font-weight: 700; padding: 8px 14px; border-radius: 8px 8px 0 0; font-size: 0.95rem; }
  .cal-event { background: #f8fafc; border-radius: 0 0 8px 8px; padding: 14px 16px; margin-bottom: 2px; border-left: 4px solid #2563eb; }
  .cal-event + .cal-event { border-radius: 8px; margin-top: 6px; }
  .cal-event-title { font-weight: 700; font-size: 0.95rem; }
  .cal-meta { font-size: 0.82rem; color: #555; margin-top: 3px; }
  .status-confirmed { color: #16a34a; font-weight: 700; }
  .status-needs { color: #d97706; font-weight: 700; }
  .status-declined { color: #dc2626; font-weight: 700; }
  .conflict-warn { background: #fef3c7; border-radius: 6px; padding: 4px 10px; font-size: 0.78rem; color: #92400e; margin-top: 6px; display: inline-block; }

  /* Job pipeline */
  .job-card { background: #f0fdf4; border-left: 4px solid #16a34a; border-radius: 8px; padding: 14px 18px; margin-bottom: 12px; }
  .job-card.medium { background: #f0f9ff; border-color: #0284c7; }
  .job-card.low { background: #fafafa; border-color: #9ca3af; }
  .job-title { font-weight: 700; font-size: 0.95rem; }
  .job-meta { font-size: 0.82rem; color: #555; margin-top: 3px; }
  .fit-badge { display: inline-block; padding: 2px 10px; border-radius: 20px; font-size: 0.72rem; font-weight: 700; text-transform: uppercase; margin-left: 8px; }
  .fit-high { background: #dcfce7; color: #15803d; }
  .fit-medium { background: #dbeafe; color: #1d4ed8; }
  .fit-low { background: #f3f4f6; color: #6b7280; }

  /* Email category blocks */
  .email-cat { border-radius: 10px; padding: 14px 18px; margin-bottom: 12px; }
  .email-cat-red { background: #fef2f2; border-left: 4px solid #dc2626; }
  .email-cat-yellow { background: #fffbeb; border-left: 4px solid #d97706; }
  .email-cat-blue { background: #eff6ff; border-left: 4px solid #2563eb; }
  .email-cat-green { background: #f0fdf4; border-left: 4px solid #16a34a; }
  .email-cat-purple { background: #faf5ff; border-left: 4px solid #7c3aed; }
  .email-cat-gray { background: #f9fafb; border-left: 4px solid #9ca3af; }
  .email-cat h4 { font-size: 0.92rem; font-weight: 700; margin-bottom: 6px; }
  .email-cat .count-badge { display: inline-block; background: #1a1a2e; color: #fff; border-radius: 20px; padding: 1px 10px; font-size: 0.75rem; font-weight: 700; margin-left: 6px; }
  .email-list { list-style: none; font-size: 0.82rem; color: #374151; margin-top: 6px; }
  .email-list li { padding: 2px 0; border-bottom: 1px solid rgba(0,0,0,0.05); }
  .email-list li:last-child { border-bottom: none; }

  /* Trash review */
  .trash-group { border-radius: 10px; padding: 14px 18px; margin-bottom: 12px; }
  .trash-restore { background: #fff7ed; border-left: 4px solid #ea580c; }
  .trash-review { background: #fffbeb; border-left: 4px solid #ca8a04; }
  .trash-delete { background: #f9fafb; border-left: 4px solid #9ca3af; }
  .trash-group h4 { font-weight: 700; font-size: 0.92rem; margin-bottom: 8px; }

  /* Table */
  table { width: 100%; border-collapse: collapse; font-size: 0.84rem; }
  th { background: #1e3a5f; color: #fff; padding: 10px 12px; text-align: left; font-weight: 600; }
  td { padding: 9px 12px; border-bottom: 1px solid #e5e7eb; vertical-align: top; }
  tr:nth-child(even) td { background: #f8fafc; }
  tr:last-child td { border-bottom: none; }
  .priority-high { color: #dc2626; font-weight: 700; }
  .priority-med { color: #d97706; font-weight: 700; }
  .priority-low { color: #6b7280; font-weight: 700; }

  /* Dashboard */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-card { border-radius: 10px; padding: 16px; text-align: center; }
  .dash-card .num { font-size: 2rem; font-weight: 700; }
  .dash-card .lbl { font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px; }
  .dash-red { background: #fef2f2; color: #dc2626; }
  .dash-green { background: #f0fdf4; color: #16a34a; }
  .dash-blue { background: #eff6ff; color: #2563eb; }
  .dash-yellow { background: #fffbeb; color: #d97706; }
  .dash-purple { background: #faf5ff; color: #7c3aed; }
  .dash-gray { background: #f3f4f6; color: #6b7280; }

  /* Top 3 */
  .top3 { counter-reset: top3; }
  .top3-item { counter-increment: top3; background: #fff; border-radius: 10px; padding: 18px 20px 18px 60px; margin-bottom: 12px; position: relative; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .top3-item::before { content: counter(top3); position: absolute; left: 16px; top: 50%; transform: translateY(-50%); font-size: 1.6rem; font-weight: 900; color: #0f3460; }
  .top3-item h4 { font-size: 0.95rem; font-weight: 700; }
  .top3-item p { font-size: 0.85rem; color: #555; margin-top: 4px; }

  /* Misc */
  .tag { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 0.72rem; font-weight: 600; margin: 1px; }
  .tag-red { background: #fee2e2; color: #dc2626; }
  .tag-green { background: #dcfce7; color: #15803d; }
  .tag-gray { background: #f3f4f6; color: #6b7280; }
  .tag-yellow { background: #fef9c3; color: #854d0e; }
  .tag-blue { background: #dbeafe; color: #1d4ed8; }
  .divider { border: none; border-top: 2px solid #e5e7eb; margin: 28px 0; }
  .note { font-size: 0.8rem; color: #6b7280; font-style: italic; margin-top: 8px; }
  .spam-warn { background: #fef2f2; border: 1px solid #fca5a5; border-radius: 6px; padding: 6px 12px; font-size: 0.8rem; color: #991b1b; margin-top: 6px; }
  .total-row td { font-weight: 700; background: #1e3a5f !important; color: #fff; }
  .inline-link { color: #2563eb; font-size: 0.78rem; word-break: break-all; }
</style>
</head>
<body>
<div class="page">

<!-- ============================================================ -->
<!-- 1. HEADER -->
<!-- ============================================================ -->
<div class="header">
  <h1>☀️ Good Morning, Melissa</h1>
  <div class="subtitle">Executive Briefing — Prepared by your Chief of Staff</div>
  <div class="header-meta">
    <div class="meta-pill"><span>Sunday</span>June 28, 2026</div>
    <div class="meta-pill"><span>50</span>Emails Reviewed</div>
    <div class="meta-pill"><span>4</span>Calendar Events</div>
    <div class="meta-pill"><span>3</span>Action Items: Urgent</div>
    <div class="meta-pill"><span>5</span>Job Leads Active</div>
  </div>
</div>

<!-- ============================================================ -->
<!-- 2. EXECUTIVE SUMMARY -->
<!-- ============================================================ -->
<div class="section red-theme">
  <div class="section-title">⚡ Executive Summary</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li class="bullet-red">
        <span class="icon">🔴</span>
        <div><strong>Security Risk:</strong> Multiple high-confidence phishing/spam emails landed in your mailbox impersonating iCloud, payment services, and a casino — including one spoofing your own Gmail address. Your GitHub daily-briefing workflow also failed repeatedly overnight (3 failed runs). Both require immediate attention.</div>
      </li>
      <li class="bullet-green">
        <span class="icon">🟢</span>
        <div><strong>Job Search Momentum:</strong> Two strong LinkedIn alerts arrived for <strong>Head of People at Lumos</strong> and <strong>People Partner, GTM at Anthropic</strong> — both high-fit roles for your background. A cold outreach email to "Blake" (Head of People pitch) is sitting in Trash — review whether it was intentionally sent and deleted. Scovai also flagged a <strong>Chief People & Culture Officer</strong> role at Omnisage LLC.</div>
      </li>
      <li class="bullet-blue">
        <span class="icon">🔵</span>
        <div><strong>Calendar Deadline:</strong> Your <strong>HR Networking &amp; Job Search Group Zoom</strong> is Wednesday July 1 at 12:00 PM — RSVP is still pending (needsAction). You also have a <strong>July 2 Executive Roundtable</strong> that you've declined — confirm this is intentional. Open Office Hours on July 2 at 12 PM also awaits your RSVP.</div>
      </li>
    </ul>
  </div>
</div>

<!-- ============================================================ -->
<!-- 3. ACTION REQUIRED -->
<!-- ============================================================ -->
<div class="section red-theme">
  <div class="section-title">🚨 Action Required</div>
  <div class="section-body">

    <div class="action-card action-red">
      <div class="card-label" style="color:#dc2626;">🔴 Security — Phishing / Spam</div>
      <div class="card-title">Multiple Phishing Emails Detected in Your Mailbox</div>
      <div class="card-row"><strong>Sources:</strong> Random_com[5,9,l]@fzrisqzdcngoudiuespwhglvxe.us · kmeoeyq@1315494.google.virelgrid.my.id · yihngiacndejet...@vr5209... · cpuz.haptuauobnxnc.us</div>
      <div class="card-row"><strong>Why it matters:</strong> Spoofed sender addresses (including your own Gmail), fake iCloud warnings, fake casino deposit, and explicit spam. These are credential-phishing attempts. Do NOT click any links.</div>
      <div class="card-row"><strong>Next Step:</strong> Mark all as phishing/spam in Gmail. Enable or review 2FA on Gmail, iCloud, and GitHub. Change passwords if you clicked any links.</div>
      <span class="card-action">Act Today</span>
    </div>

    <div class="action-card action-red">
      <div class="card-label" style="color:#dc2626;">🔴 Technical — GitHub Workflow Failure</div>
      <div class="card-title">Daily Briefing GitHub Action Failing (3 Runs)</div>
      <div class="card-row"><strong>Source:</strong> notifications@github.com — [missophs/daily-briefing] Run failed (multiple commits)</div>
      <div class="card-row"><strong>Why it matters:</strong> Your automated daily briefing pipeline is broken. All jobs failed across 3 workflow runs overnight. This is likely a webhook misconfiguration or secret expiration.</div>
      <div class="card-row"><strong>Next Step:</strong> Log into GitHub → missophs/daily-briefing → Actions → review error logs. Check webhook secrets/API keys for expiration.</div>
      <span class="card-action">Fix Today</span>
    </div>

    <div class="action-card action-yellow">
      <div class="card-label" style="color:#d97706;">🟡 RSVP Pending — Calendar</div>
      <div class="card-title">HR Networking &amp; Job Search Group — Zoom (Jul 1, 12–1:30 PM)</div>
      <div class="card-row"><strong>Source:</strong> Google Calendar — needsAction status</div>
      <div class="card-row"><strong>Why it matters:</strong> Large networking group (180+ attendees). You have a duplicate "Network" event confirmed at the same time — confirm which is your actual block.</div>
      <div class="card-row"><strong>Next Step:</strong> Accept or decline the group invite. Confirm your personal "Network" placeholder is correctly set. Zoom link ready.</div>
      <div class="card-row"><strong>Due:</strong> Wednesday, July 1 at 12:00 PM ET</div>
      <span class="card-action">RSVP by Tuesday</span>
    </div>

    <div class="action-card action-yellow">
      <div class="card-label" style="color:#d97706;">🟡 RSVP Pending — Calendar</div>
      <div class="card-title">HR Networking Open Office Hours — Zoom (Jul 2, 12–1 PM)</div>
      <div class="card-row"><strong>Source:</strong> Google Calendar — needsAction status</div>
      <div class="card-row"><strong>Why it matters:</strong> A second networking session the next day — open discussion, no AI notetaking tools permitted. Good opportunity for 1:1 connections.</div>
      <div class="card-row"><strong>Next Step:</strong> Accept or decline. Note: AI notetaking tools are explicitly prohibited by organizer.</div>
      <div class="card-row"><strong>Due:</strong> Thursday, July 2 at 12:00 PM ET</div>
      <span class="card-action">RSVP Soon</span>
    </div>

    <div class="action-card action-green">
      <div class="card-label" style="color:#16a34a;">🟢 Job Search — Trash Review</div>
      <div class="card-title">Cold Outreach Email to "Blake" Found in Trash</div>
      <div class="card-row"><strong>Source:</strong> melissa &lt;melissaw212@gmail.com&gt; — Subject: "Head of People | Built this function twice. Ready for what's next."</div>
      <div class="card-row"><strong>Why it matters:</strong> This appears to be a compelling executive pitch email you drafted. It's in Trash — was this intentionally deleted before sending, or did you send it and then trash it? The snippet suggests a strong value proposition targeting a $150M+ company.</div>
      <div class="card-row"><strong>Next Step:</strong> Verify: Did you send this to Blake? If unsent, consider restoring and sending. If sent, follow up.</div>
      <span class="card-action">Verify &amp; Act</span>
    </div>

    <div class="action-card action-green">
      <div class="card-label" style="color:#16a34a;">🟢 Job Search — New Alert</div>
      <div class="card-title">People Partner, GTM at Anthropic — New LinkedIn Alert</div>
      <div class="card-row"><strong>Source:</strong> LinkedIn Job Alerts — jobalerts-noreply@linkedin.com</div>
      <div class="card-row"><strong>Why it matters:</strong> Anthropic is a leading AI company — a People Partner, GTM role aligns with your HR leadership background and your current interest in AI + People strategy. High-fit opportunity.</div>
      <div class="card-row"><strong>Next Step:</strong> Review full job description on LinkedIn. Apply if aligned. Leverage your AI/HR content angle in cover materials.</div>
      <span class="card-action">Apply This Week</span>
    </div>

    <div class="action-card action-yellow">
      <div class="card-label" style="color:#d97706;">🟡 Networking — New Connection</div>
      <div class="card-title">Jason Kippen, SHRM-SCP, SPHR Accepted Your LinkedIn Invitation</div>
      <div class="card-row"><strong>Source:</strong> LinkedIn — invitations@linkedin.com</div>
      <div class="card-row"><strong>Why it matters:</strong> Jason has senior HR credentials (SHRM-SCP, SPHR). Warm connection — good moment to send a personalized note.</div>
      <div class="card-row"><strong>Next Step:</strong> Send a brief LinkedIn message — reference shared interest in People strategy, ask about their current work.</div>
      <span class="card-action">Message Today</span>
    </div>

    <div class="action-card action-yellow">
      <div class="card-label" style="color:#d97706;">🟡 Urgent — Animal Rescue</div>
      <div class="card-title">Waldo's Rescue: Foster Needed Before June 30 Evening Pickup</div>
      <div class="card-row"><strong>Source:</strong> Andi &lt;andi@waldosrescue.org&gt;</div>
      <div class="card-row"><strong>Why it matters:</strong> Pups have waited 100+ days. June 30 is the pickup deadline — that's in 2 days. July 4th coverage may be available as an alternative.</div>
      <div class="card-row"><strong>Next Step:</strong> Reply to Andi by tomorrow (June 29) if you can foster or know someone who can.</div>
      <div class="card-row"><strong>Due:</strong> June 30, 2026</div>
      <span class="card-action">Reply by Tomorrow</span>
    </div>

    <div class="action-card action-yellow">
      <div class="card-label" style="color:#d97706;">🟡 TikTok Shop — Refund Issued</div>
      <div class="card-title">TikTok Shop Issued a $15.23 Refund — No Return Required</div>
      <div class="card-row"><strong>Source:</strong> TikTok Shop &lt;no-reply@shop-us.tiktok.com&gt;</div>
      <div class="card-row"><strong>Why it matters:</strong> Refund was issued via ApplePay. Verify it posts to your account within 3–5 business days.</div>
      <div class="card-row"><strong>Next Step:</strong> Check ApplePay balance this week. No action likely needed.</div>
      <span class="card-action">Monitor</span>
    </div>

  </div>
</div>

<!-- ============================================================ -->
<!-- 4. FULL 7-DAY CALENDAR -->
<!-- ============================================================ -->
<div class="section blue-theme">
  <div class="section-title">📅 Full 7-Day Calendar (June 28 – July 4, 2026)</div>
  <div class="section-body">

    <div class="cal-day">
      <div class="cal-day-header">Sunday, June 28, 2026 — TODAY</div>
      <div class="cal-event" style="border-color:#9ca3af; background:#f9fafb;">
        <div class="cal-event-title" style="color:#6b7280;">No calendar events scheduled today.</div>
        <div class="cal-meta">Use this time for email triage, GitHub fix, and job application review.</div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">Monday, June 30, 2026</div>
      <div class="cal-event" style="border-color:#9ca3af; background:#f9fafb;">
        <div class="cal-event-title" style="color:#6b7280;">No calendar events scheduled.</div>
        <div class="cal-meta">⚠️ <strong>Waldo's Rescue foster deadline is tonight (June 30 evening).</strong> Reply to Andi today if you plan to help.</div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">Wednesday, July 1, 2026</div>

      <div class="cal-event">
        <div class="cal-event-title">HR Networking &amp; Job Search Group — Zoom 2</div>
        <div class="cal-meta">🕐 12:00 PM – 1:30 PM ET &nbsp;|&nbsp; <span class="status-needs">⚠️ RSVP Pending (needsAction)</span></div>
        <div class="cal-meta">📍 <a class="inline-link" href="https://us06web.zoom.us/j/81954171722">https://us06web.zoom.us/j/81954171722</a></div>
        <div class="cal-meta">👥 ~180+ attendees — large HR job search networking group</div>
        <div class="cal-meta">📋 <strong>Prep:</strong> Review team guidelines doc linked in calendar description. Prepare a 30-second intro. Have your target role/companies ready to share.</div>
        <div class="conflict-warn">⚠️ Conflict: "Network" personal placeholder also runs 12:00–1:30 PM — these appear to be the same block. Confirm and remove duplicate.</div>
      </div>

      <div class="cal-event" style="border-color:#16a34a; background:#f0fdf4; margin-top:8px;">
        <div class="cal-event-title">Network (Personal Placeholder)</div>
        <div class="cal-meta">🕐 12:00 PM – 1:30 PM ET &nbsp;|&nbsp; <span class="status-confirmed">✅ Confirmed</span></div>
        <div class="cal-meta">📍 No location set</div>
        <div class="cal-meta">📋 Appears to be a personal block mirroring the Zoom group above. <strong>Recommend removing this duplicate.</strong></div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">Thursday, July 2, 2026</div>

      <div class="cal-event" style="border-color:#dc2626; background:#fef2f2;">
        <div class="cal-event-title">Executive Roundtable — Zoom (John Madigan)</div>
        <div class="cal-meta">🕐 9:00 AM – 10:30 AM ET &nbsp;|&nbsp; <span class="status-declined">❌ Declined</span></div>
        <div class="cal-meta">📍 <a class="inline-link" href="https://us02web.zoom.us/j/207786667">https://us02web.zoom.us/j/207786667</a> &nbsp;|&nbsp; PW: 205454</div>
        <div class="cal-meta">📋 <strong>Verify:</strong> Was this declined intentionally? If so, no action needed. If declined by mistake, contact John Madigan to rejoin.</div>
        <div class="conflict-warn">⚠️ You declined this event. Confirm this was intentional — Executive Roundtables can be valuable networking opportunities.</div>
      </div>

      <div class="cal-event" style="margin-top:8px;">
        <div class="cal-event-title">HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
        <div class="cal-meta">🕐 12:00 PM – 1:00 PM ET &nbsp;|&nbsp; <span class="status-needs">⚠️ RSVP Pending (needsAction)</span></div>
        <div class="cal-meta">📍 <a class="inline-link" href="https://us06web.zoom.us/j/85945371140">https://us06web.zoom.us/j/85945371140</a></div>
        <div class="cal-meta">👥 ~180+ attendees — open discussion format</div>
        <div class="cal-meta">⚠️ <strong>Note from organizer:</strong> Please turn off automated notetaking AI tools. No recording needed.</div>
        <div class="cal-meta">📋 <strong>Prep:</strong> Bring 1–2 specific questions about your job search. Good for 1:1 relationship building. Disable Otter, Fireflies, or similar tools before joining.</div>
      </div>
    </div>

    <div class="cal-day">
      <div class="cal-day-header">Friday, July 3 – Saturday, July 4, 2026</div>
      <div class="cal-event" style="border-color:#9ca3af; background:#f9fafb;">
        <div class="cal-event-title" style="color:#6b7280;">No calendar events scheduled — Independence Day Weekend 🎆</div>
        <div class="cal-meta">Note: Waldo's Rescue mentioned July 4th coverage may be available for fostering if June 30 doesn't work.</div>
      </div>
    </div>

  </div>
</div>

<!-- ============================================================ -->
<!-- 5. JOB SEARCH & INTERVIEW PIPELINE -->
<!-- ============================================================ -->
<div class="section green-theme">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">

    <p style="margin-bottom:14px; font-size:0.85rem; color:#555;">Active job alerts, applications, and networking opportunities detected in email and calendar data.</p>

    <div class="job-card">
      <div class="job-title">People Partner, GTM — Anthropic <span class="fit-badge fit-high">HIGH FIT</span></div>
      <div class="job-meta">📧 LinkedIn Job Alert &nbsp;|&nbsp; Arrived: Sun Jun 28, 1:05 AM &nbsp;|&nbsp; Status: <strong>Unread → Review Now</strong></div>
      <div class="job-meta">💡 Anthropic (leading AI safety company) + GTM People Partner = strong alignment with your HR leadership + AI interest. This is a high-visibility, mission-driven role.</div>
      <div class="job-meta">✅ <strong>Action:</strong> Review JD on LinkedIn. Tailor application to highlight AI-adjacent HR work and your experience building People functions at scale.</div>
    </div>

    <div class="job-card">
      <div class="job-title">Head of People — Lumos <span class="fit-badge fit-high">HIGH FIT</span></div>
      <div class="job-meta">📧 LinkedIn Job Alert (2 alerts sent) &nbsp;|&nbsp; Arrived: Sun Jun 28, 3:05 AM &amp; 7:05 AM &nbsp;|&nbsp; Status: Unread</div>
      <div class="job-meta">💡 Snippet references breach response, audits, and new hires — implies a security-conscious, scaling company. Matches your "built this function twice" profile.</div>
      <div class="job-meta">✅ <strong>Action:</strong> Review JD. Apply. LinkedIn alerted you twice — high relevance signal.</div>
    </div>

    <div class="job-card">
      <div class="job-title">Cold Outreach to "Blake" — Head of People Pitch <span class="fit-badge fit-high">HIGH FIT</span></div>
      <div class="job-meta">📧 From: melissa &lt;melissaw212@gmail.com&gt; &nbsp;|&nbsp; Status: <strong>In Trash — Needs Verification</strong></div>
      <div class="job-meta">💡 Snippet: "The window between $150M raised and true scale is where People strategy either holds the company together or quietly becomes the reason it doesn't." Strong executive pitch language targeting a growth-stage company.</div>
      <div class="job-meta">⚠️ <strong>Action:</strong> Restore from Trash. Verify: Was this sent? If unsent, review and send. If sent, follow up with Blake.</div>
    </div>

    <div class="job-card medium">
      <div class="job-title">Chief People &amp; Culture Officer — Omnisage LLC <span class="fit-badge fit-medium">MEDIUM FIT</span></div>
      <div class="job-meta">📧 Scovai &lt;no-reply@scovai.com&gt; &nbsp;|&nbsp; Arrived: Sun Jun 28, 7:00 AM &nbsp;|&nbsp; Status: Read, Not in Inbox</div>
      <div class="job-meta">💡 Scovai matched this role to your profile. CPCO title is a step up — worth reviewing if Omnisage LLC is a company of interest.</div>
      <div class="job-meta">✅ <strong>Action:</strong> Log into Scovai to review full role details and company profile.</div>
    </div>

    <div class="job-card low">
      <div class="job-title">Overseas HRD — Cornerstone Global Partners (CGP Group) <span class="fit-badge fit-low">LOW FIT</span></div>
      <div class="job-meta">📧 LinkedIn Job Alert (2 alerts sent) &nbsp;|&nbsp; Arrived: Sun Jun 28, 5:05 AM &amp; 9:05 AM</div>
      <div class="job-meta">💡 Role description is in Chinese (CHRO reporting structure, 50–60 person team). Overseas/international focus. Low fit unless you are targeting international roles.</div>
      <div class="job-meta">✅ <strong>Action:</strong> Dismiss unless you have interest in overseas HR leadership. Update LinkedIn job preferences to filter international roles if needed.</div>
    </div>

    <div class="job-card low">
      <div class="job-title">HR Generalist &amp; 6 More — Glassdoor Job Alert <span class="fit-badge fit-low">LOW FIT</span></div>
      <div class="job-meta">📧 Glassdoor &lt;noreply@glassdoor.com&gt; &nbsp;|&nbsp; Arrived: Sun Jun 28, 12:58 AM &nbsp;|&nbsp; Status: Read</div>
      <div class="job-meta">💡 Includes a "Volunteer Opportunity, HR Generalist" — below your target level. Securitas also mentioned. Bundle of 7 remote roles.</div>
      <div class="job-meta">✅ <strong>Action:</strong> Scan quickly. Unlikely to be at your target seniority. Update Glassdoor filters to VP/Director/Head of People level.</div>
    </div>

    <!-- Networking -->
    <hr style="margin:16px 0; border-color:#e5e7eb;">
    <h4 style="font-size:0.9rem; font-weight:700; color:#15803d; margin-bottom:10px;">🤝 Networking</h4>

    <div class="job-card">
      <div class="job-title">Jason Kippen, SHRM-SCP, SPHR — New LinkedIn Connection</div>
      <div class="job-meta">📧 LinkedIn Invitation Acceptance &nbsp;|&nbsp; Arrived: Sun Jun 28, 11:05 AM</div>
      <div class="job-meta">✅ <strong>Action:</strong> Send a warm, personalized LinkedIn message today. Senior HR credentials — potentially a peer connection or referral source.</div>
    </div>

    <div class="job-card">
      <div class="job-title">HR Networking &amp; Job Search Group — Zoom (Jul 1) + Open Office Hours (Jul 2)</div>
      <div class="job-meta">📅 Calendar Events &nbsp;|&nbsp; Both pending RSVP</div>
      <div class="job-meta">✅ <strong>Action:</strong> RSVP to both events. Prepare your 30-second pitch, target company list, and 1–2 questions. Disable AI notetaking for Jul 2 session.</div>
    </div>

    <!-- Self-Sent Notes -->
    <hr style="margin:16px 0; border-color:#e5e7eb;">
    <h4 style="font-size:0.9rem; font-weight:700; color:#15803d; margin-bottom:10px;">📝 Self-Sent Research Notes (melissaw212@gmail.com)</h4>
    <div class="job-card medium">
      <div class="job-title">Self-Sent: "15 HR Analytics Prompts" · "Claude Shortcuts" · "AI Agents for HR"</div>
      <div class="job-meta">📧 Sent Sat Jun 27, ~9:12–9:14 PM &nbsp;|&nbsp; Status: Unread, Not in Inbox (likely Sent folder)</div>
      <div class="job-meta">💡 These are research/resource notes you emailed yourself. May be useful for interview prep, job applications, or professional positioning.</div>
      <div class="job-meta">✅ <strong>Action:</strong> Review and consolidate into a master resource doc or Notion/Google Doc for easy reference.</div>
    </div>

  </div>
</div>

<!-- ============================================================ -->
<!-- 6. FULL EMAIL REVIEW BY CATEGORY -->
<!-- ============================================================ -->
<div class="section navy-theme">
  <div class="section-title">📬 Full Email Review by Category</div>
  <div class="section-body">

    <!-- Security / Risk -->
    <div class="email-cat email-cat-red">
      <h4>🔴 Security / Risk <span class="count-badge">6</span></h4>
      <div class="spam-warn">⚠️ Multiple phishing emails detected. Do NOT click any links in these messages.</div>
      <ul class="email-list">
        <li><strong>melissaw212 (spoofed) — Random_com...@fzrisqzdcngoudiuespwhglvxe.us</strong> · "You received a direct deposit $6,000" · PHISHING — fake casino deposit, spoofs your Gmail</li>
        <li><strong>Payment-Declined — yihngiacndejet...@vr5209.hwdars.d6toc5.us</strong> · "Your Account Has been Blocked!" · PHISHING — fake iCloud storage warning</li>
        <li><strong>melissaw212 (spoofed) — kmeoeyq@1315494.google.virelgrid.my.id</strong> · "🚨 We've blocked your account!" · PHISHING — fake iCloud account block</li>
        <li><strong>'HorseWood Secret' — cilkdectzgcmpw...@mq9tfi.jpefba.hh0jt8.us</strong> · Adult spam/phishing · SPAM — explicit content</li>
        <li><strong>GitHub (legitimate) — noreply@github.com</strong> · Sudo verification codes (2 emails, 04:47 &amp; 04:49 AM) · These appear legitimate — used during your GitHub session early this morning. Codes are now expired.</li>
        <li><strong>missophs/daily-briefing — notifications@github.com</strong> · Run failed x3 (093a16e, 6285ac3 ×2) · Legitimate GitHub notifications — workflow is broken, needs debugging</li>
      </ul>
      <div class="card-row" style="margin-top:8px;"><strong>Recommended Action:</strong> Report phishing emails. Debug GitHub workflow. Verify no accounts were compromised.</div>
    </div>

    <!-- Job Search -->
    <div class="email-cat email-cat-green">
      <h4>🟢 Job Search &amp; Applications <span class="count-badge">9</span></h4>
      <ul class="email-list">
        <li><strong>LinkedIn Job Alerts</strong> · People Partner, GTM at Anthropic · HIGH FIT — apply now</li>
        <li><strong>LinkedIn Job Alerts ×2</strong> · Head of People at Lumos (duplicate alert) · HIGH FIT — apply now</li>
        <li><strong>LinkedIn Job Alerts ×2</strong> · Overseas HRD at Cornerstone Global Partners (duplicate alert) · LOW FIT — likely skip</li>
        <li><strong>Glassdoor</strong> · HR Generalist + 6 more roles · LOW FIT — update filters</li>
        <li><strong>Scovai</strong> · Chief People &amp; Culture Officer at Omnisage LLC · MEDIUM FIT — review on Scovai</li>
        <li><strong>melissa (melissaw212@gmail.com) — IN TRASH</strong> · "Head of People | Built this function twice" pitch to Blake · RESTORE &amp; VERIFY before deciding</li>
        <li><strong>Melissa W (self-sent) ×3</strong> · "15 HR analytics prompts" / "Claude shortcuts" / "AI agents for HR" · Personal research notes — review and file</li>
      </ul>
      <div class="card-row" style="margin-top:8px;"><strong>Recommended Action:</strong> Apply to Anthropic and Lumos roles this week. Restore and review Blake pitch email. File self-sent notes.</div>
    </div>

    <!-- Recruiters / Networking -->
    <div class="email-cat email-cat-green">
      <h4>🤝 Recruiters &amp; Networking <span class="count-badge">1</span></h4>
      <ul class="email-list">
        <li><strong>LinkedIn — Jason Kippen, SHRM-SCP, SPHR</strong> · Accepted your connection invitation · Send a personalized follow-up message today</li>
      </ul>
      <div class="card-row" style="margin-top:8px;"><strong>Recommended Action:</strong> Message Jason on LinkedIn today.</div>
    </div>

    <!-- Animal Rescue / Personal Urgency -->
    <div class="email-cat email-cat-yellow">
      <h4>🟡 Time-Sensitive / Personal <span class="count-badge">2</span></h4>
      <ul class="email-list">
        <li><strong>Andi — andi@waldosrescue.org</strong> · "They've waited over 100 days. Please help them get out." · Foster deadline June 30 evening — reply by tomorrow</li>
        <li><strong>TikTok Shop — no-reply@shop-us.tiktok.com</strong> · "Refund issued — no return required" · $15.23 ApplePay refund issued — verify it posts</li>
      </ul>
      <div class="card-row" style="margin-top:8px;"><strong>Recommended Action:</strong> Reply to Andi by June 29. Monitor ApplePay for refund.</div>
    </div>

    <!-- Financial / Billing -->
    <div class="email-cat email-cat-yellow">
      <h4>🟡 Financial / Billing / Orders <span class="count-badge">1</span></h4>
      <ul class="email-list">
        <li><strong>TikTok Shop Service — service-us@tiktok.com ×2</strong> · "Rate your customer service experience" re: order 577432067516239900 · (Counted separately — 1 in inbox, 1 not in inbox — both read) · Low priority</li>
      </ul>
      <div class="card-row" style="margin-top:8px;"><strong>Recommended Action:</strong> Rate if you have feedback. Otherwise archive.</div>
    </div>

    <!-- Professional Development -->
    <div class="email-cat email-cat-purple">
      <h4>🟣 Professional Development <span class="count-badge">5</span></h4>
      <ul class="email-list">
        <li><strong>David Green 🇺🇦 via LinkedIn</strong> · "The best HR &amp; People Analytics articles of June 2026" · Curated reading — relevant to your HR analytics interest</li>
        <li><strong>Adam Karpiak via LinkedIn</strong> · "Why great careers don't always make great resumes" · Career/resume strategy newsletter</li>
        <li><strong>Mo Bunnell via LinkedIn</strong> · "Your Client Plan Isn't Landing. Here's Why." · Business development / relationship growth newsletter</li>
        <li><strong>Medium Daily Digest</strong> · "8 Crazy Things Claude AI Can Do" · AI tools article — relevant to your AI-for-HR focus</li>
        <li><strong>Claude's Notebook (Substack)</strong> · "I Am a Void. I Wrote This Anyway." · AI/writing newsletter — reads as a philosophical AI perspective piece</li>
      </ul>
      <div class="card-row" style="margin-top:8px;"><strong>Recommended Action:</strong> Batch-read on a Sunday evening. David Green's HR analytics roundup is highest priority for professional value.</div>
    </div>

    <!-- Newsletters (in Trash or Low Value) -->
    <div class="email-cat email-cat-purple">
      <h4>🟣 Newsletters (Trashed / Lower Priority) <span class="count-badge">4</span></h4>
      <ul class="email-list">
        <li><strong>AI For Leaders</strong> · "AI and the Rise of Creative Generalists" · IN TRASH — relevant topic but you trashed it</li>
        <li><strong>Lisa Rangel (Chameleon Resumes)</strong> · "The snake is eating its own tail." · IN TRASH — insider AI hiring insight for job seekers</li>
        <li><strong>Medium Daily Digest (amylw516 account)</strong> · "Agentic AI: How to Save on Tokens" · IN TRASH — appears to be from a secondary Medium account</li>
        <li><strong>CoolDeep AI</strong> · "I wasted a year learning AI wrong" · IN TRASH — AI learning framework newsletter</li>
      </ul>
      <div class="card-row" style="margin-top:8px;"><strong>Recommended Action:</strong> Lisa Rangel's AI hiring insider piece may be worth restoring — relevant to your job search. Others: Safe to delete from trash.</div>
    </div>

    <!-- Promotional / Retail (Inbox) -->
    <div class="email-cat email-cat-gray">
      <h4>⬜ Promotional / Retail (Inbox) <span class="count-badge">10</span></h4>
      <ul class="email-list">
        <li><strong>Target Optical</strong> · 20% off eyewear — limited time</li>
        <li><strong>Kohl's</strong> · "Ends today: Deal Days + FREE shipping" · Expires today (June 28)</li>
        <li><strong>SHEIN ×2</strong> · "Summer Fits Are Live" (duplicate from two domains)</li>
        <li><strong>Gap Factory</strong> · Extra 15% + bonus 10% off, doorbusters from $4</li>
        <li><strong>OkCupid</strong> · "Someone likes you — Message them now"</li>
        <li><strong>Macy's</strong> · 40% off dresses — trending summer styles (Not in inbox)</li>
        <li><strong>Temu</strong> · "Pants set: Was $57.45, Just $6.96" — coupon bundle promo</li>
        <li><strong>Facebook</strong> · "36 notifications about Doudline and others" (Not in inbox)</li>
        <li><strong>22 Words</strong> · "Amazon's Last-Minute Price Drops" · Read, not in inbox</li>
        <li><strong>Shopify</strong> · "11 best print on demand partners" + 3 months for $1</li>
      </ul>
      <div class="card-row" style="margin-top:8px;"><strong>Recommended Action:</strong> Kohl's deal expires today. Target Optical is time-sensitive. Others are low-priority — batch delete or unsubscribe.</div>
    </div>

    <!-- Promotional (Trash) -->
    <div class="email-cat email-cat-gray">
      <h4>⬜ Promotional / Retail (In Trash) <span class="count-badge">5</span></h4>
      <ul class="email-list">
        <li><strong>Walgreens</strong> · "Take an Extra 20% Off Sitewide — code STARS20" · IN TRASH</li>
        <li><strong>Bed Bath &amp; Beyond</strong> · "Star-spangled deals — up to 60% off" · IN TRASH</li>
        <li><strong>VIVAIA</strong> · "FINAL HOURS: Nothing Left After This" · Read, not in trash explicitly but low inbox</li>
        <li><strong>Alison Courses</strong> · "How credible are Alison courses?" · Not in inbox, not in trash</li>
        <li><strong>"Congratulations 🎉" (casino spam)</strong> · "130 Free Spins – No Deposit Needed! Casino Limitless" · SPAM — not in inbox or trash</li>
      </ul>
      <div class="card-row" style="margin-top:8px;"><strong>Recommended Action:</strong> Permanently delete all. Unsubscribe from retail senders if inbox clutter is a concern.</div>
    </div>

    <!-- Safe to Delete / Ignore -->
    <div class="email-cat email-cat-gray">
      <h4>⬜ Safe to Delete / Ignore <span class="count-badge">7</span></h4>
      <ul class="email-list">
        <li><strong>GitHub Sudo Codes ×2</strong> · Expired 15-minute verification codes (4:47 AM &amp; 4:49 AM) — now worthless, safe to archive</li>
        <li><strong>TikTok Shop Service ×2</strong> · Customer service rating survey for order 577432067516239900 (duplicate emails) — rate or delete</li>
        <li><strong>VIVAIA</strong> · "FINAL HOURS" — fashion promo, no action needed</li>
        <li><strong>22 Words</strong> · Amazon deal digest — already read, no action</li>
        <li><strong>Facebook notifications</strong> · 36 notifications re: Doudline &amp; Sorina — check app directly if interested, otherwise ignore email</li>
      </ul>
      <div class="card-row" style="margin-top:8px;"><strong>Recommended Action:</strong> Archive or delete all. No follow-up needed.</div>
    </div>

  </div>
</div>

<!-- ============================================================ -->
<!-- 7. TRASH REVIEW -->
<!-- ============================================================ -->
<div class="section red-theme">
  <div class="section-title">🗑️ Trash Review</div>
  <div class="section-body">

    <div class="trash-group trash-restore">
      <h4>✅ Restore Immediately (2)</h4>
      <ul class="email-list">
        <li><strong>melissa &lt;melissaw212@gmail.com&gt;</strong> · "Head of People | Built this function twice. Ready for what's next." · Your own outreach pitch to "Blake" — compelling executive copy. Verify send status immediately. If unsent, restore and send. If sent, follow up.</li>
        <li><strong>Lisa Rangel &lt;lr@chameleonresumes.com&gt;</strong> · "The snake is eating its own tail." · Insider perspective from a resume expert on AI and hiring tools — directly relevant to your job search strategy. Consider restoring to read.</li>
      </ul>
    </div>

    <div class="trash-group trash-review">
      <h4>👀 Review Before Deleting (3)</h4>
      <ul class="email-list">
        <li><strong>AI For Leaders &lt;team@aiforleaders.com&gt;</strong> · "AI and the Rise of Creative Generalists" · Relevant to your AI+HR positioning. May be worth a quick read before permanent delete. Consider whether you want to stay subscribed.</li>
        <li><strong>Medium Daily Digest (amylw516 account)</strong> · "Agentic AI: How to Save on Tokens" · This appears to be a digest for a different Medium account (amylw516) — if this is not your account, review and unsubscribe that address.</li>
        <li><strong>CoolDeep AI &lt;cooldeepai@mail.beehiiv.com&gt;</strong> · "I wasted a year learning AI wrong" · A quick AI learning framework piece. Worth a 2-minute skim given your AI interest. Then unsubscribe if not finding ongoing value.</li>
      </ul>
    </div>

    <div class="trash-group trash-delete">
      <h4>🗑️ Safe to Permanently Delete (4)</h4>
      <ul class="email-list">
        <li><strong>Walgreens</strong> · "Take an Extra 20% Off Sitewide — code STARS20" · Standard retail promo, no action needed.</li>
        <li><strong>Bed Bath &amp; Beyond</strong> · "Star-spangled deals — up to 60% off" · Retail promotion, delete permanently.</li>
        <li><strong>Macy's &lt;shop@emails.macys.com&gt;</strong> · "40% off dresses from I.N.C., Charter Club &amp; more" · Not in inbox or trash — retail promo, no action needed, safe to ignore/delete.</li>
        <li><strong>Alison Courses</strong> · "How credible are Alison courses?" · Low-priority marketing email from online learning platform. Delete.</li>
      </ul>
    </div>

    <p class="note">Note: Trash emails marked <em>in_trash: true</em> in the data: melissa pitch to Blake, Walgreens 20% off, Bed Bath &amp; Beyond, AI For Leaders, Lisa Rangel, Medium Digest (amylw), CoolDeep AI. Additional emails with spam/phishing content (casino, adult, iCloud spoof) are NOT in Trash — those should be reported as phishing and then deleted.</p>

  </div>
</div>

<!-- ============================================================ -->
<!-- 8. PROMOTIONAL / RETAIL SUMMARY -->
<!-- ============================================================ -->
<div class="section gray-theme">
  <div class="section-title">🛍️ Promotional / Retail Summary</div>
  <div class="section-body">
    <table>
      <thead>
        <tr><th>Sender / Brand</th><th>Count</th><th>Subject / Theme</th><th>Recommendation</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Target Optical</strong></td><td>1</td><td>20% off eyewear — limited time offer</td><td><span class="tag tag-yellow">Review</span> Time-sensitive</td></tr>
        <tr><td><strong>Kohl's</strong></td><td>1</td><td>Deal Days + FREE shipping — ends TODAY</td><td><span class="tag tag-yellow">Review Today</span> Expires June 28</td></tr>
        <tr><td><strong>SHEIN</strong></td><td>2</td><td>"Summer Fits Are Live" — duplicate from 2 domains</td><td><span class="tag tag-gray">Delete</span> Duplicate, unsubscribe one domain</td></tr>
        <tr><td><strong>Gap Factory</strong></td><td>1</td><td>Extra 15% + bonus 10% off, doorbusters from $4</td><td><span class="tag tag-gray">Delete / Ignore</span></td></tr>
        <tr><td><strong>Walgreens</strong> (Trash)</td><td>1</td><td>Extra 20% sitewide — code STARS20</td><td><span class="tag tag-gray">Permanently Delete</span></td></tr>
        <tr><td><strong>Bed Bath &amp; Beyond</strong> (Trash)</td><td>1</td><td>Up to 60% off home essentials — 4th of July</td><td><span class="tag tag-gray">Permanently Delete</span></td></tr>
        <tr><td><strong>VIVAIA</strong></td><td>1</td><td>"FINAL HOURS: Nothing Left After This" — shoes/bags</td><td><span class="tag tag-gray">Ignore / Delete</span></td></tr>
        <tr><td><strong>Macy's</strong></td><td>1</td><td>40% off dresses — summer trending</td><td><span class="tag tag-gray">Delete</span></td></tr>
        <tr><td><strong>Temu</strong></td><td>1</td><td>Pants set: Was $57.45, Now $6.96</td><td><span class="tag tag-gray">Delete / Unsubscribe</span></td></tr>
        <tr><td><strong>OkCupid</strong></td><td>1</td><td>"Someone likes you — Message them now"</td><td><span class="tag tag-gray">Check App / Delete</span></td></tr>
        <tr><td><strong>Shopify</strong></td><td>1</td><td>11 best print-on-demand partners + $1/3 months offer</td><td><span class="tag tag-gray">Ignore</span> Unless starting e-commerce project</td></tr>
        <tr><td><strong>22 Words</strong></td><td>1</td><td>Amazon last-minute price drops — already read</td><td><span class="tag tag-gray">Archive / Delete</span></td></tr>
        <tr><td><strong>Facebook Notifications</strong></td><td>1</td><td>36 notifications — Doudline, Sorina</td><td><span class="tag tag-gray">Check App / Delete</span></td></tr>
        <tr><td><strong>Alison Courses</strong></td><td>1</td><td>Course credibility marketing email</td><td><span class="tag tag-gray">Delete / Unsubscribe</span></td></tr>
        <tr><td><strong>Casino Limitless (Spam)</strong></td><td>1</td><td>"130 Free Spins – No Deposit" spam/scam</td><td><span class="tag tag-red">Report Spam &amp; Delete</span></td></tr>
      </tbody>
    </table>
    <p class="note" style="margin-top:10px;">Total promotional
<hr>
<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Job Search / Recruiters</td><td>15</td></tr>
<tr><td>Medical / Health</td><td>2</td></tr>
<tr><td>Other / Review</td><td>15</td></tr>
<tr><td>Professional Development / Newsletters</td><td>1</td></tr>
<tr><td>Promotional / Retail</td><td>8</td></tr>
<tr><td>Security / Risk</td><td>9</td></tr>
</table>
<p><strong>Audit Note:</strong> Every fetched email was reviewed and assigned to one category. Trash emails were included in review. Promotional and low-value emails were accounted for but deprioritized.</p>

