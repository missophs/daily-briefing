<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa W. — August 8, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px 60px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px 28px; margin-bottom: 24px; box-shadow: 0 4px 18px rgba(0,0,0,0.18); }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .sub { font-size: 15px; color: #a8b8d8; margin-top: 6px; }
  .header .meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.09); border-radius: 8px; padding: 10px 18px; }
  .header .meta-item .label { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #a8b8d8; }
  .header .meta-item .value { font-size: 20px; font-weight: 700; color: #fff; margin-top: 2px; }

  /* SECTION TITLES */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; padding: 10px 16px; border-radius: 8px 8px 0 0; margin-bottom: 0; }
  .section-body { background: #fff; border-radius: 0 0 10px 10px; padding: 18px 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.07); }

  .title-red { background: #c0392b; color: #fff; }
  .title-yellow { background: #e67e22; color: #fff; }
  .title-blue { background: #1a6fa8; color: #fff; }
  .title-green { background: #1e8449; color: #fff; }
  .title-purple { background: #6c3483; color: #fff; }
  .title-gray { background: #6c757d; color: #fff; }
  .title-dark { background: #1a1a2e; color: #fff; }
  .title-teal { background: #117a65; color: #fff; }

  /* EXECUTIVE SUMMARY */
  .exec-bullets { list-style: none; padding: 0; }
  .exec-bullets li { padding: 10px 14px; margin-bottom: 8px; border-radius: 8px; border-left: 5px solid; font-size: 14px; line-height: 1.5; }
  .exec-bullets li.risk { background: #fdf0ef; border-color: #c0392b; }
  .exec-bullets li.job { background: #eafaf1; border-color: #1e8449; }
  .exec-bullets li.cal { background: #eaf3fb; border-color: #1a6fa8; }

  /* TRIAGE TABLE */
  .triage-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .triage-table th { background: #1a1a2e; color: #fff; padding: 9px 12px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.8px; }
  .triage-table td { padding: 8px 12px; border-bottom: 1px solid #eee; vertical-align: top; }
  .triage-table tr:last-child td { border-bottom: none; }
  .triage-table tr:nth-child(even) td { background: #fafafa; }
  .badge { display: inline-block; padding: 3px 9px; border-radius: 12px; font-size: 11px; font-weight: 700; white-space: nowrap; }
  .badge-rescued { background: #d5f5e3; color: #1e8449; }
  .badge-inbox { background: #d6eaf8; color: #1a6fa8; }
  .badge-trash-auto { background: #fadbd8; color: #922b21; }
  .badge-trash-manual { background: #fdebd0; color: #784212; }

  /* ACTION CARDS */
  .action-cards { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
  @media (max-width: 700px) { .action-cards { grid-template-columns: 1fr; } }
  .action-card { border-radius: 10px; padding: 16px 18px; border-left: 5px solid; }
  .action-card.red { background: #fdf0ef; border-color: #c0392b; }
  .action-card.yellow { background: #fef9e7; border-color: #e67e22; }
  .action-card.green { background: #eafaf1; border-color: #1e8449; }
  .action-card.blue { background: #eaf3fb; border-color: #1a6fa8; }
  .action-card.purple { background: #f4ecf7; border-color: #6c3483; }
  .action-card .card-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px; }
  .action-card.red .card-label { color: #c0392b; }
  .action-card.yellow .card-label { color: #e67e22; }
  .action-card.green .card-label { color: #1e8449; }
  .action-card.blue .card-label { color: #1a6fa8; }
  .action-card.purple .card-label { color: #6c3483; }
  .action-card h3 { font-size: 14px; font-weight: 700; margin-bottom: 6px; }
  .action-card .meta-row { font-size: 12px; color: #555; margin-bottom: 3px; }
  .action-card .meta-row strong { color: #222; }
  .action-card .next-step { margin-top: 8px; background: rgba(0,0,0,0.05); border-radius: 6px; padding: 7px 10px; font-size: 12px; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { background: #1a6fa8; color: #fff; border-radius: 7px 7px 0 0; padding: 8px 16px; font-weight: 700; font-size: 14px; }
  .cal-event { background: #f5f9fd; border-left: 4px solid #1a6fa8; margin: 0; padding: 11px 16px; border-bottom: 1px solid #e3edf5; }
  .cal-event:last-child { border-bottom: none; border-radius: 0 0 7px 7px; }
  .cal-event.declined { border-left-color: #e74c3c; background: #fdf6f6; }
  .cal-event.needs-action { border-left-color: #e67e22; background: #fefaf5; }
  .cal-event .event-name { font-weight: 700; font-size: 14px; }
  .cal-event .event-meta { font-size: 12px; color: #555; margin-top: 3px; }
  .cal-event .rsvp { display: inline-block; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: 700; margin-left: 8px; }
  .rsvp-confirmed { background: #d5f5e3; color: #1e8449; }
  .rsvp-declined { background: #fadbd8; color: #c0392b; }
  .rsvp-needs { background: #fdebd0; color: #e67e22; }
  .cal-no-events { color: #888; font-style: italic; padding: 10px; background: #f9f9f9; border-radius: 0 0 7px 7px; }

  /* JOB SEARCH */
  .job-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .job-table th { background: #1e8449; color: #fff; padding: 8px 12px; text-align: left; font-size: 12px; text-transform: uppercase; }
  .job-table td { padding: 8px 12px; border-bottom: 1px solid #eee; vertical-align: top; }
  .job-table tr:last-child td { border-bottom: none; }
  .fit-high { color: #1e8449; font-weight: 700; }
  .fit-med { color: #e67e22; font-weight: 700; }
  .fit-low { color: #888; font-weight: 700; }

  /* CATEGORY REVIEW */
  .cat-card { background: #fff; border-radius: 10px; margin-bottom: 14px; box-shadow: 0 1px 6px rgba(0,0,0,0.07); overflow: hidden; }
  .cat-card-header { display: flex; align-items: center; padding: 11px 16px; gap: 12px; }
  .cat-card-header .cat-count { font-size: 22px; font-weight: 800; min-width: 36px; text-align: center; }
  .cat-card-header .cat-title { font-weight: 700; font-size: 15px; }
  .cat-card-header .cat-tag { font-size: 11px; background: rgba(0,0,0,0.1); border-radius: 10px; padding: 2px 8px; margin-left: auto; }
  .cat-card-body { padding: 12px 16px; border-top: 1px solid #f0f0f0; font-size: 13px; }
  .cat-card-body .senders { color: #555; margin-bottom: 6px; }
  .cat-card-body .rec { font-weight: 600; color: #222; }

  .cat-red { background: #fdf0ef; }
  .cat-red .cat-count { color: #c0392b; }
  .cat-yellow { background: #fef9e7; }
  .cat-yellow .cat-count { color: #e67e22; }
  .cat-blue { background: #eaf3fb; }
  .cat-blue .cat-count { color: #1a6fa8; }
  .cat-green { background: #eafaf1; }
  .cat-green .cat-count { color: #1e8449; }
  .cat-purple { background: #f4ecf7; }
  .cat-purple .cat-count { color: #6c3483; }
  .cat-gray { background: #f5f5f5; }
  .cat-gray .cat-count { color: #6c757d; }

  /* TRASH REVIEW */
  .trash-group { margin-bottom: 16px; }
  .trash-group-title { font-weight: 700; font-size: 13px; padding: 7px 14px; border-radius: 6px; margin-bottom: 8px; }
  .tg-restore { background: #d5f5e3; color: #1e8449; }
  .tg-review { background: #fdebd0; color: #784212; }
  .tg-delete { background: #f2f3f4; color: #555; }
  .trash-item { background: #fff; border: 1px solid #e8e8e8; border-radius: 7px; padding: 9px 14px; margin-bottom: 6px; font-size: 13px; }
  .trash-item .ti-from { font-weight: 600; color: #222; }
  .trash-item .ti-sub { color: #444; margin-top: 2px; }
  .trash-item .ti-reason { color: #777; font-style: italic; margin-top: 3px; font-size: 12px; }
  .trash-item .ti-tag { display: inline-block; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: 700; margin-top: 4px; }
  .tag-auto-phish { background: #fadbd8; color: #c0392b; }
  .tag-auto-news { background: #e8daef; color: #6c3483; }
  .tag-rescued { background: #d5f5e3; color: #1e8449; }
  .tag-manual { background: #fdebd0; color: #784212; }

  /* PROMO */
  .promo-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .promo-table th { background: #6c757d; color: #fff; padding: 8px 12px; text-align: left; font-size: 12px; text-transform: uppercase; }
  .promo-table td { padding: 8px 12px; border-bottom: 1px solid #eee; vertical-align: top; }
  .promo-table tr:last-child td { border-bottom: none; }

  /* NEWSLETTER */
  .nl-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .nl-table th { background: #6c3483; color: #fff; padding: 8px 12px; text-align: left; font-size: 12px; text-transform: uppercase; }
  .nl-table td { padding: 8px 12px; border-bottom: 1px solid #eee; vertical-align: top; }
  .nl-table tr:last-child td { border-bottom: none; }

  /* ACCOUNTING */
  .acct-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .acct-table th { background: #1a1a2e; color: #fff; padding: 9px 12px; text-align: left; font-size: 12px; text-transform: uppercase; }
  .acct-table td { padding: 8px 12px; border-bottom: 1px solid #eee; vertical-align: top; }
  .acct-table tr:last-child td { border-bottom: none; background: #eaf3fb; font-weight: 700; }
  .acct-table .total-row td { background: #1a1a2e; color: #fff; font-weight: 700; }

  /* DASHBOARD */
  .dashboard-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; }
  @media (max-width: 800px) { .dashboard-grid { grid-template-columns: 1fr 1fr; } }
  @media (max-width: 500px) { .dashboard-grid { grid-template-columns: 1fr; } }
  .dash-card { border-radius: 10px; padding: 14px 16px; }
  .dash-card .dash-label { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; font-weight: 700; margin-bottom: 6px; }
  .dash-card .dash-value { font-size: 26px; font-weight: 800; }
  .dash-card .dash-detail { font-size: 12px; margin-top: 4px; color: #555; }
  .dash-red { background: #fdf0ef; } .dash-red .dash-label { color: #c0392b; } .dash-red .dash-value { color: #c0392b; }
  .dash-green { background: #eafaf1; } .dash-green .dash-label { color: #1e8449; } .dash-green .dash-value { color: #1e8449; }
  .dash-blue { background: #eaf3fb; } .dash-blue .dash-label { color: #1a6fa8; } .dash-blue .dash-value { color: #1a6fa8; }
  .dash-yellow { background: #fef9e7; } .dash-yellow .dash-label { color: #e67e22; } .dash-yellow .dash-value { color: #e67e22; }
  .dash-purple { background: #f4ecf7; } .dash-purple .dash-label { color: #6c3483; } .dash-purple .dash-value { color: #6c3483; }
  .dash-gray { background: #f5f5f5; } .dash-gray .dash-label { color: #6c757d; } .dash-gray .dash-value { color: #6c757d; }

  /* ACTION ITEMS TABLE */
  .ai-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .ai-table th { background: #1a1a2e; color: #fff; padding: 9px 12px; text-align: left; font-size: 12px; text-transform: uppercase; }
  .ai-table td { padding: 8px 12px; border-bottom: 1px solid #eee; vertical-align: top; }
  .ai-table tr:last-child td { border-bottom: none; }
  .pri-high { background: #fadbd8; color: #c0392b; font-weight: 700; border-radius: 8px; padding: 2px 8px; font-size: 11px; white-space: nowrap; }
  .pri-med { background: #fdebd0; color: #784212; font-weight: 700; border-radius: 8px; padding: 2px 8px; font-size: 11px; white-space: nowrap; }
  .pri-low { background: #eaf3fb; color: #1a6fa8; font-weight: 700; border-radius: 8px; padding: 2px 8px; font-size: 11px; white-space: nowrap; }

  /* TOP 3 */
  .top3 { display: flex; gap: 16px; flex-wrap: wrap; }
  .top3-item { flex: 1; min-width: 240px; border-radius: 12px; padding: 20px 22px; }
  .top3-item .num { font-size: 38px; font-weight: 900; opacity: 0.18; line-height: 1; }
  .top3-item h3 { font-size: 15px; font-weight: 700; margin-top: -8px; }
  .top3-item p { font-size: 13px; margin-top: 6px; line-height: 1.5; }
  .top3-1 { background: #fdf0ef; border-left: 5px solid #c0392b; }
  .top3-2 { background: #eafaf1; border-left: 5px solid #1e8449; }
  .top3-3 { background: #eaf3fb; border-left: 5px solid #1a6fa8; }

  hr.divider { border: none; border-top: 2px solid #e0e0e0; margin: 10px 0 22px; }
  .note { font-size: 12px; color: #777; font-style: italic; margin-top: 8px; }
  ul.detail-list { padding-left: 18px; margin-top: 6px; }
  ul.detail-list li { margin-bottom: 3px; font-size: 13px; }
  .rescued-note { display: inline-block; background: #d5f5e3; color: #1e8449; border-radius: 8px; font-size: 11px; padding: 2px 8px; font-weight: 700; margin-left: 6px; }
  .spam-note { display: inline-block; background: #fadbd8; color: #c0392b; border-radius: 8px; font-size: 11px; padding: 2px 8px; font-weight: 700; margin-left: 6px; }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ═══════════════════════════════════════════════
     SECTION 0: EMAIL TRIAGE QUICK LIST
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title title-dark">📋 Email Triage Quick List</div>
  <div class="section-body" style="padding:0;">
    <table class="triage-table">
      <thead>
        <tr>
          <th style="width:130px;">Status</th>
          <th style="width:180px;">From</th>
          <th>Subject</th>
          <th>Summary</th>
        </tr>
      </thead>
      <tbody>
        <!-- RESCUED EMAILS (5) -->
        <tr>
          <td><span class="badge badge-rescued">✅ RESCUED</span></td>
          <td>Melissa → Kelly</td>
          <td>What happens to acquired talent once the deal closes</td>
          <td>Melissa's own outreach to Kelly re: Howden M&amp;A activity — rescued from Trash. Important professional correspondence.</td>
        </tr>
        <tr>
          <td><span class="badge badge-rescued">✅ RESCUED</span></td>
          <td>Google</td>
          <td>You shared some Google Account data with Canva</td>
          <td>Security alert: Google account data shared with Canva via Sign-in — rescued from Trash. Review for awareness.</td>
        </tr>
        <tr>
          <td><span class="badge badge-rescued">✅ RESCUED</span></td>
          <td>HRISWorkday / Howden</td>
          <td>Your recent Howden Job Application for HRBP/Senior HRBP</td>
          <td>Application acknowledgment from Howden for HRBP role — rescued from Trash. Monitor for next steps.</td>
        </tr>
        <tr>
          <td><span class="badge badge-rescued">✅ RESCUED</span></td>
          <td>Amazon Security</td>
          <td>amazon.com: Sign-in</td>
          <td>Account sign-in alert: Sophie Weiss, Chrome/macOS, near New York, Aug 7 — rescued from Trash. Verify this was you.</td>
        </tr>
        <tr>
          <td><span class="badge badge-rescued">✅ RESCUED</span></td>
          <td>Amazon.com</td>
          <td>Ordered: 1 Beverages item</td>
          <td>Order confirmation for a beverages item — rescued from Trash. Keep for records.</td>
        </tr>
        <!-- INBOX EMAILS (individual) -->
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>Indeed</td>
          <td>Contract Leadership Development Trainer @ Community Based Services</td>
          <td>$150–$175/hr contract role in leadership/HR development. Possibly relevant given Melissa's background.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>Bank of America</td>
          <td>Fraud Claim for account -2994 - Claim has been canceled</td>
          <td>BofA fraud claim on account ending 2994 has been canceled per request. Verify this action was intentional.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>Match</td>
          <td>You've had a profile view from Nicholas</td>
          <td>Nicholas, 49, Medford NY viewed Melissa's Match.com profile. Personal / low priority.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>Melissa W (self)</td>
          <td>Job (LinkedIn link 1)</td>
          <td>Self-sent LinkedIn job link: linkedin.com/jobs/view/4450767496</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>Melissa W (self)</td>
          <td>Job (LinkedIn link 2)</td>
          <td>Self-sent LinkedIn job link: linkedin.com/jobs/view/4450730549</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>Melissa W (self)</td>
          <td>Job (LinkedIn link 3)</td>
          <td>Self-sent LinkedIn job link: linkedin.com/jobs/view/4450757831</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>LinkedIn</td>
          <td>Olivia Hanninen, PhD accepted your invitation</td>
          <td>New LinkedIn connection accepted. Explore Olivia's network for opportunities.</td>
        </tr>
        <!-- SPAM / PHISHING still in inbox (not trashed) -->
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>DirectMeds (spam)</td>
          <td>DirectMeds GLP-1 treatment… (multiple)</td>
          <td>⚠️ Phishing/spam — GLP-1 weight loss scam emails (3 variants). Not auto-trashed. Delete immediately.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>CashApp scam / Casino spam</td>
          <td>You Received a Payment of $3,000 / Free Spins / Penis enlargement spam (multiple)</td>
          <td>⚠️ Phishing/adult spam — multiple scam emails not yet trashed. Delete immediately.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>Mail Delivery Subsystem</td>
          <td>Delivery Status Notification (Failure) ×2</td>
          <td>Two bounce-backs for nikki_perez@nebius.com and nikki.perez@nebius.com — address not found. Verify correct email.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>Match</td>
          <td>Robert likes you.</td>
          <td>Robert liked Melissa's Match.com profile. Personal / low priority.</td>
        </tr>
        <!-- TRASH SUMMARY ROWS -->
        <tr style="background:#fef3f3;">
          <td><span class="badge badge-trash-auto">🗑 AUTO-TRASHED</span></td>
          <td colspan="2"><strong>2 emails auto-trashed (newsletters/digests)</strong> — Medium Daily Digest, OpenArt</td>
          <td>See Trash Review → Auto-Trashed Newsletter section</td>
        </tr>
        <tr style="background:#fef8f0;">
          <td><span class="badge badge-trash-manual">🗂 TRASH (manual)</span></td>
          <td colspan="2"><strong>~26 emails in Trash (manual)</strong> — retail promos, newsletters, dating, adult spam, misc</td>
          <td>See Trash Review for full breakdown of Restore / Review / Delete</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 1: HEADER
═══════════════════════════════════════════════ -->
<div class="header">
  <h1>Good Morning, Melissa 👋</h1>
  <div class="sub">Executive Briefing — Saturday, August 8, 2026</div>
  <div class="meta">
    <div class="meta-item">
      <div class="label">Emails Reviewed</div>
      <div class="value">50</div>
    </div>
    <div class="meta-item">
      <div class="label">Calendar Events</div>
      <div class="value">7</div>
    </div>
    <div class="meta-item">
      <div class="label">Action Required</div>
      <div class="value">6</div>
    </div>
    <div class="meta-item">
      <div class="label">Emails Rescued</div>
      <div class="value">5</div>
    </div>
    <div class="meta-item">
      <div class="label">Upcoming Medical</div>
      <div class="value">3</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 2: EXECUTIVE SUMMARY
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title title-dark">🔍 Executive Summary</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li class="risk">🔴 <strong>BIGGEST RISK:</strong> An Amazon sign-in alert (rescued from Trash) shows a login attributed to "Sophie Weiss" on your account from near New York on Aug 7 — verify this was you. Additionally, a Bank of America fraud claim on account -2994 was canceled; confirm this was intentional. Multiple phishing/spam emails (GLP-1 scams, casino spam, adult spam) remain untrashed in your inbox and need immediate deletion.</li>
      <li class="job">🟢 <strong>BIGGEST OPPORTUNITY:</strong> Your Howden HRBP/Senior HRBP application is under review (rescued from Trash — Workday confirmation). You've also self-flagged 3 LinkedIn job links and received an Indeed alert for a $150–$175/hr contract L&amp;D trainer role. Olivia Hanninen, PhD just accepted your LinkedIn connection — explore her network. The HR Networking &amp; Job Search Group meets Wednesday Aug 12.</li>
      <li class="cal">🔵 <strong>BIGGEST CALENDAR ITEM:</strong> A packed medical week begins Monday: Stephanie's infusion (Aug 10), your MRI Brain W&amp;WO with IV contrast at 159 E 53rd St (Aug 11 — arrive 8:50 AM, appt 9:20 AM), and PT (Aug 12). You have not yet RSVPed to two HR networking sessions on Aug 12 and Aug 13. You declined the Executive Roundtable on Aug 13.</li>
    </ul>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 3: ACTION REQUIRED
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title title-red">⚡ Action Required</div>
  <div class="section-body">
    <div class="action-cards">

      <div class="action-card red">
        <div class="card-label">🔴 Security Alert</div>
        <h3>Amazon Sign-In: "Sophie Weiss" — Verify Now</h3>
        <div class="meta-row"><strong>Source:</strong> Amazon Security — amazon.com (rescued from Trash)</div>
        <div class="meta-row"><strong>Why it matters:</strong> Sign-in on Aug 7 ~8:58 PM ET from Chrome/macOS near New York under a name that may not be yours. Could indicate unauthorized access or a shared account.</div>
        <div class="next-step">➡️ Log in to Amazon, review recent orders and account activity. Change password if unauthorized. Check if "Sophie Weiss" is a legitimate sub-user.</div>
        <div class="meta-row" style="margin-top:8px;"><strong>Due:</strong> Today — August 8</div>
      </div>

      <div class="action-card red">
        <div class="card-label">🔴 Financial Alert</div>
        <h3>BofA Fraud Claim on Account -2994 Was Canceled</h3>
        <div class="meta-row"><strong>Source:</strong> Bank of America — ealerts.bankofamerica.com</div>
        <div class="meta-row"><strong>Why it matters:</strong> Fraud claims protect you. If you did not request cancellation, your account may be vulnerable.</div>
        <div class="next-step">➡️ Call BofA directly (number on the back of your card) to confirm you authorized this cancellation. If not, re-open the claim immediately.</div>
        <div class="meta-row" style="margin-top:8px;"><strong>Due:</strong> Today — August 8</div>
      </div>

      <div class="action-card red">
        <div class="card-label">🔴 Inbox Hygiene / Security</div>
        <h3>Delete Phishing &amp; Adult Spam Emails in Inbox Now</h3>
        <div class="meta-row"><strong>Source:</strong> DirectMeds (×3), CashApp scam, Casino Limitless, "F*ckMeHard," Sex_Trick, Natural Size Boost (×2), Prime_Network, Match bounce</div>
        <div class="meta-row"><strong>Why it matters:</strong> These malicious/scam emails are sitting in your inbox (not yet trashed). Some may be tracking opens.</div>
        <div class="next-step">➡️ Select all and delete without opening. Consider enabling stronger spam filters in Gmail settings.</div>
        <div class="meta-row" style="margin-top:8px;"><strong>Due:</strong> Today — August 8</div>
      </div>

      <div class="action-card yellow">
        <div class="card-label">🟡 Failed Outreach — Follow-Up</div>
        <h3>Bounced Emails to Nikki Perez at Nebius.com</h3>
        <div class="meta-row"><strong>Source:</strong> Mail Delivery Subsystem (×2 failures)</div>
        <div class="meta-row"><strong>Why it matters:</strong> Two attempts to reach nikki_perez@nebius.com and nikki.perez@nebius.com both failed. Your message was not delivered.</div>
        <div class="next-step">➡️ Find Nikki Perez's correct email on LinkedIn or Nebius's website. Resend your outreach.</div>
        <div class="meta-row" style="margin-top:8px;"><strong>Due:</strong> This weekend</div>
      </div>

      <div class="action-card green">
        <div class="card-label">🟢 Job Search</div>
        <h3>RSVP / Confirm HR Networking Sessions (Aug 12 &amp; Aug 13)</h3>
        <div class="meta-row"><strong>Source:</strong> Calendar — HR Networking &amp; Job Search Group (needsAction ×2)</div>
        <div class="meta-row"><strong>Why it matters:</strong> Both sessions show "needsAction" — you haven't confirmed attendance. Active networking is critical for your job search.</div>
        <div class="next-step">➡️ Accept both calendar invites. Prepare a brief intro and any targeted ask for Wednesday's group session.</div>
        <div class="meta-row" style="margin-top:8px;"><strong>Due:</strong> Before Aug 12</div>
      </div>

      <div class="action-card blue">
        <div class="card-label">🔵 Medical Prep</div>
        <h3>MRI Brain W&amp;WO IVC — Arrive 8:50 AM Tuesday</h3>
        <div class="meta-row"><strong>Source:</strong> Calendar — 159 E 53rd St, 6th Floor, NY 10022 | ☎ 646-754-2800</div>
        <div class="meta-row"><strong>Why it matters:</strong> Appointment starts 9:20 AM; arrive by 8:50 AM. Remove all body piercings beforehand. Leave valuables at home. MRI-safe gown provided.</div>
        <div class="next-step">➡️ Confirm transport to 159 E 53rd St. Remove metal jewelry/piercings before arrival. Bring ID and insurance card.</div>
        <div class="meta-row" style="margin-top:8px;"><strong>Due:</strong> Tuesday, August 11</div>
      </div>

    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 4: FULL 7-DAY CALENDAR
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title title-blue">📅 Full 7-Day Calendar (Aug 8–14, 2026)</div>
  <div class="section-body" style="padding:0;">

    <!-- Saturday Aug 8 -->
    <div class="cal-day">
      <div class="cal-day-header">Saturday, August 8, 2026 — TODAY</div>
      <div class="cal-no-events">No calendar events scheduled today. Use this time to address security alerts, delete spam, and RSVP to networking sessions.</div>
    </div>

    <!-- Sunday Aug 9 -->
    <div class="cal-day">
      <div class="cal-day-header">Sunday, August 9, 2026</div>
      <div class="cal-no-events">No calendar events scheduled. Good time to review the 3 LinkedIn job links you sent yourself and research Howden HRBP role.</div>
    </div>

    <!-- Monday Aug 10 -->
    <div class="cal-day">
      <div class="cal-day-header">Monday, August 10, 2026</div>
      <div class="cal-event">
        <div class="event-name">Stephanie Infusion <span class="rsvp rsvp-confirmed">✅ Confirmed</span></div>
        <div class="event-meta">🕗 8:00 AM – 9:00 AM</div>
        <div class="event-meta">📍 Location not specified</div>
        <div class="event-meta">📝 <strong>Prep:</strong> Confirm location and transportation in advance. Note this takes about 1 hour.</div>
      </div>
    </div>

    <!-- Tuesday Aug 11 -->
    <div class="cal-day">
      <div class="cal-day-header">Tuesday, August 11, 2026</div>
      <div class="cal-event">
        <div class="event-name">MRI Brain W&amp;WO IVC <span class="rsvp rsvp-confirmed">✅ Confirmed</span></div>
        <div class="event-meta">🕗 Arrive: 8:50 AM | Appt Starts: 9:20 AM | End: ~9:40 AM</div>
        <div class="event-meta">📍 159 E 53rd Street, 6th Floor, New York, NY 10022 | ☎ 646-754-2800</div>
        <div class="event-meta">📝 <strong>Prep:</strong> Remove all body piercings/metal before arriving. Leave valuables at home. MRI-safe gown provided. Private dressing rooms with lockers available. Arrive 30 min before exam time.</div>
        <div class="event-meta" style="color:#c0392b; margin-top:4px;">⚠️ <strong>Important:</strong> Do NOT bring metal objects. Arrive by 8:50 AM sharp — exam begins at 9:20 AM.</div>
      </div>
    </div>

    <!-- Wednesday Aug 12 -->
    <div class="cal-day">
      <div class="cal-day-header">Wednesday, August 12, 2026</div>
      <div class="cal-event">
        <div class="event-name">PT (Physical Therapy) <span class="rsvp rsvp-confirmed">✅ Confirmed</span></div>
        <div class="event-meta">🕤 9:30 AM – 10:30 AM</div>
        <div class="event-meta">📍 Location not specified</div>
        <div class="event-meta">📝 <strong>Prep:</strong> Confirm location. Wear comfortable clothing.</div>
      </div>
      <div class="cal-event needs-action">
        <div class="event-name">HR Networking &amp; Job Search Group — Zoom Session 2 <span class="rsvp rsvp-needs">⚠️ Needs RSVP</span></div>
        <div class="event-meta">🕛 12:00 PM – 1:30 PM</div>
        <div class="event-meta">📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a></div>
        <div class="event-meta">👥 ~180+ attendees — large HR professional networking group</div>
        <div class="event-meta">📝 <strong>Prep:</strong> Review HR Networking Team Guidelines. Prepare a 30-second intro and a specific ask (referrals, job leads). Accept the calendar invite now.</div>
        <div class="event-meta" style="color:#e67e22; margin-top:4px;">⚠️ <strong>Conflicts:</strong> Back-to-back with PT — allow travel/transition time after 10:30 AM before noon Zoom.</div>
      </div>
      <div class="cal-event">
        <div class="event-name">Network <span class="rsvp rsvp-confirmed">✅ Confirmed</span></div>
        <div class="event-meta">🕛 12:00 PM – 1:30 PM</div>
        <div class="event-meta">📍 Location not specified</div>
        <div class="event-meta">📝 <strong>Note:</strong> This appears to overlap with the HR Networking Zoom — may be the same session or a duplicate calendar block. Confirm which takes priority.</div>
        <div class="event-meta" style="color:#e67e22; margin-top:4px;">⚠️ <strong>Conflict:</strong> Exact same time as HR Networking Zoom above. Verify if duplicate.</div>
      </div>
    </div>

    <!-- Thursday Aug 13 -->
    <div class="cal-day">
      <div class="cal-day-header">Thursday, August 13, 2026</div>
      <div class="cal-event declined">
        <div class="event-name">Executive Roundtable <span class="rsvp rsvp-declined">❌ Declined</span></div>
        <div class="event-meta">🕘 9:00 AM – 10:30 AM</div>
        <div class="event-meta">📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> | Host: John Madigan | Meeting ID: 207 786 667 | PW: 205454</div>
        <div class="event-meta">📝 <strong>Note:</strong> You declined this event. If you wish to attend, contact John Madigan to re-accept.</div>
      </div>
      <div class="cal-event needs-action">
        <div class="event-name">HR Networking &amp; Job Search: Open Office Hours — Zoom 2 <span class="rsvp rsvp-needs">⚠️ Needs RSVP</span></div>
        <div class="event-meta">🕛 12:00 PM – 1:00 PM</div>
        <div class="event-meta">📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a></div>
        <div class="event-meta">👥 ~180+ attendees — open discussion format, no recording/AI notetaking</div>
        <div class="event-meta">📝 <strong>Prep:</strong> This is an open discussion. Good for 1:1 connection-making. Accept calendar invite. Note: no automated notetaking tools allowed per organizer instructions.</div>
      </div>
    </div>

    <!-- Friday Aug 14 -->
    <div class="cal-day">
      <div class="cal-day-header">Friday, August 14, 2026</div>
      <div class="cal-no-events">No calendar events scheduled.</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 5: JOB SEARCH & INTERVIEW PIPELINE
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title title-green">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body" style="padding:0;">
    <table class="job-table">
      <thead>
        <tr>
          <th>Fit</th>
          <th>Type</th>
          <th>Source</th>
          <th>Role / Detail</th>
          <th>Status / Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="fit-high">HIGH</td>
          <td>Application Pending</td>
          <td>Workday / Howden <span class="rescued-note">RESCUED</span></td>
          <td><strong>HRBP / Senior HRBP at Howden</strong> — Howden bought Atlantic Group in Jan 2026, raised $703M in Feb 2026, actively expanding. Melissa also drafted outreach to Kelly about Howden M&amp;A talent strategy.</td>
          <td>Application under review. Monitor inbox for interview invite. Follow up after ~5 business days if no response.</td>
        </tr>
        <tr>
          <td class="fit-high">HIGH</td>
          <td>Self-flagged Lead</td>
          <td>Melissa W (self-email)</td>
          <td><strong>LinkedIn Job: /jobs/view/4450767496</strong> — Role unknown; self-saved for review</td>
          <td>Open and review. Apply if relevant to HR/OD background.</td>
        </tr>
        <tr>
          <td class="fit-high">HIGH</td>
          <td>Self-flagged Lead</td>
          <td>Melissa W (self-email)</td>
          <td><strong>LinkedIn Job: /jobs/view/4450730549</strong> — Role unknown; self-saved for review</td>
          <td>Open and review. Apply if relevant.</td>
        </tr>
        <tr>
          <td class="fit-high">HIGH</td>
          <td>Self-flagged Lead</td>
          <td>Melissa W (self-email)</td>
          <td><strong>LinkedIn Job: /jobs/view/4450757831</strong> — Role unknown; self-saved for review</td>
          <td>Open and review. Apply if relevant.</td>
        </tr>
        <tr>
          <td class="fit-med">MEDIUM</td>
          <td>Job Alert</td>
          <td>Indeed (Inbox)</td>
          <td><strong>Contract Leadership Development Trainer</strong> @ Community Based Services — $150–$175/hr. Leadership &amp; HR development contract role.</td>
          <td>Review full posting. Contract rate is strong. Consider applying if scope aligns.</td>
        </tr>
        <tr>
          <td class="fit-med">MEDIUM</td>
          <td>Job Alert</td>
          <td>Glassdoor (Trashed)</td>
          <td><strong>HR Business Partner at Offit Kurman + 10 more</strong> — Remote, US. Brown &amp; Brown hiring among others.</td>
          <td>Alert was trashed — rescue if relevant. Review HR BP roles in alert.</td>
        </tr>
        <tr>
          <td class="fit-low">LOW</td>
          <td>Job Alert</td>
          <td>Glassdoor (Trashed)</td>
          <td><strong>Community Manager(s) at Bridgeworks LLC + 11 more</strong> — New York, NY. Twitch and others hiring.</td>
          <td>Trashed — likely not a fit for HR/OD background. Review briefly.</td>
        </tr>
        <tr>
          <td class="fit-high">HIGH</td>
          <td>Networking</td>
          <td>Calendar</td>
          <td><strong>HR Networking &amp; Job Search Group (Zoom)</strong> — Aug 12, 12–1:30 PM. 180+ HR professionals.</td>
          <td>⚠️ RSVP not yet submitted. Accept invite. Prep intro + ask.</td>
        </tr>
        <tr>
          <td class="fit-high">HIGH</td>
          <td>Networking</td>
          <td>Calendar</td>
          <td><strong>HR Networking Open Office Hours (Zoom)</strong> — Aug 13, 12–1 PM. Open discussion.</td>
          <td>⚠️ RSVP not yet submitted. Accept invite. No AI notetaking allowed.</td>
        </tr>
        <tr>
          <td class="fit-high">HIGH</td>
          <td>New Connection</td>
          <td>LinkedIn (Inbox)</td>
          <td><strong>Olivia Hanninen, PhD</strong> accepted your LinkedIn connection request</td>
          <td>Review her profile and connections. Send a personalized follow-up message.</td>
        </tr>
        <tr>
          <td class="fit-med">MEDIUM</td>
          <td>Professional Outreach</td>
          <td>Melissa → Kelly (Rescued)</td>
          <td><strong>Email to Kelly re: Howden M&amp;A talent strategy</strong> — Melissa reaching out about acquired talent post-deal close</td>
          <td>Monitor for reply from Kelly. If no response in 3–5 days, send a gentle follow-up.</td>
        </tr>
        <tr>
          <td class="fit-low">LOW</td>
          <td>Email Bounce</td>
          <td>Mail Delivery Subsystem</td>
          <td><strong>Nikki Perez @ Nebius.com</strong> — Two delivery failures (different email variants)</td>
          <td>Find correct email via LinkedIn. Resend outreach.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 6: FULL EMAIL REVIEW BY CATEGORY
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title title-dark">📂 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="cat-card">
      <div class="cat-card-header cat-red">
        <div class="cat-count">9</div>
        <div class="cat-title">🔴 Security / Risk</div>
        <div class="cat-tag">IMMEDIATE ATTENTION</div>
      </div>
      <div class="cat-card-body">
        <div class="senders"><strong>Senders:</strong> Amazon Security (sign-in alert, rescued), Bank of America (fraud claim canceled), Mail Delivery Subsystem ×2 (bounced outreach to Nikki Perez), DirectMeds ×3 (phishing/spam), CashApp scam ("$3,000 payment"), Casino scam ("200 Free Spins"), "F*ckMeHard" adult spam, "Sex_Trick" adult spam, Natural Size Boost ×2 (spam), Prime_Network (phishing)</div>
        <ul class="detail-list">
          <li><strong>Amazon Sign-In Alert</strong> (rescued from Trash) — "Sophie Weiss" logged in Aug 7. Verify immediately.</li>
          <li><strong>BofA Fraud Claim Canceled</strong> — Account -2994. Confirm you authorized cancellation.</li>
          <li><strong>Mail Delivery Failures ×2</strong> — nikki_perez@nebius.com and nikki.perez@nebius.com both failed. Find correct address.</li>
          <li><strong>DirectMeds GLP-1 Spam ×3</strong> — Obfuscated domains, scam weight loss offers. Delete without opening.</li>
          <li><strong>CashApp Scam ("$3,000 USD Payment")</strong> — Fake crypto/casino scam. Delete immediately.</li>
          <li><strong>Casino / Free Spins Spam</strong> — "200 Free Spins No Deposit." Delete.</li>
          <li><strong>Adult Spam</strong> — "F*ckMeHard," "Sex_Trick," "Natural Size Boost" ×2, Prime_Network. Delete without opening.</li>
          <li><strong>Google/Canva Data Sharing Alert</strong> (rescued) — You signed in to Canva with Google. Awareness item only.</li>
        </ul>
        <div class="rec">⚡ Recommended: Address Amazon and BofA alerts today. Delete all phishing/spam immediately. Enable Gmail advanced spam filtering.</div>
      </div>
    </div>

    <!-- JOB SEARCH -->
    <div class="cat-card">
      <div class="cat-card-header cat-green">
        <div class="cat-count">8</div>
        <div class="cat-title">🟢 Job Search</div>
        <div class="cat-tag">HIGH PRIORITY</div>
      </div>
      <div class="cat-card-body">
        <div class="senders"><strong>Senders:</strong> HRISWorkday/Howden (rescued), Indeed, Glassdoor ×2, Melissa W self-emails ×3, Olivia Hanninen/LinkedIn (connection)</div>
        <ul class="detail-list">
          <li><strong>Howden HRBP Application Confirmation</strong> (rescued from Trash) — Under review. High-fit opportunity.</li>
          <li><strong>Indeed Alert</strong> — Contract L&amp;D Trainer $150–$175/hr. Worth reviewing.</li>
          <li><strong>Glassdoor Alert 1</strong> (trashed) — HR Business Partner at Offit Kurman + 10 more, Remote US.</li>
          <li><strong>Glassdoor Alert 2</strong> (trashed) — Community Manager at Bridgeworks + 11 more, NY.</li>
          <li><strong>Self-sent LinkedIn Jobs ×3</strong> — Three saved job links. Review and apply this weekend.</li>
          <li><strong>Olivia Hanninen, PhD LinkedIn Connection</strong> — New connection accepted. Follow up.</li>
        </ul>
        <div class="rec">✅ Recommended: Review all 3 LinkedIn job links, follow up on Howden application, send personalized note to Olivia Hanninen, RSVP to both networking sessions.</div>
      </div>
    </div>

    <!-- PROFESSIONAL NETWORKING / OUTREACH -->
    <div class="cat-card">
      <div class="cat-card-header cat-green">
        <div class="cat-count">3</div>
        <div class="cat-title">🟢 Recruiters / Networking / Professional Outreach</div>
        <div class="cat-tag">FOLLOW UP</div>
      </div>
      <div class="cat-card-body">
        <div class="senders"><strong>Senders:</strong> Melissa → Kelly (rescued from Trash), LinkedIn (Matt Quick suggestion — trashed), Mail Delivery Subsystem ×2 (bounce)</div>
        <ul class="detail-list">
          <li><strong>Melissa → Kelly re: Howden M&amp;A</strong> (rescued) — Outreach to Kelly about talent impact of Howden deal. Monitor for reply.</li>
          <li><strong>LinkedIn: Matt Quick, Head of Military Affairs trending</strong> (trashed) — Network suggestion. Low priority.</li>
          <li><strong>Bounced emails to Nikki Perez</strong> — Two failed delivery attempts. Find correct address on LinkedIn/Nebius site.</li>
        </ul>
        <div class="rec">✅ Recommended: Monitor for Kelly's reply. Fix Nikki Perez email address and resend. Discard LinkedIn suggestion notification.</div>
      </div>
    </div>

    <!-- CALENDAR / EVENTS -->
    <div class="cat-card">
      <div class="cat-card-header cat-blue">
        <div class="cat-count">0</div>
        <div class="cat-title">🔵 Calendar / Events</div>
        <div class="cat-tag">MANAGED VIA CALENDAR</div>
      </div>
      <div class="cat-card-body">
        <div class="senders">All calendar events are managed directly in the 7-Day Calendar section above. No standalone calendar emails in inbox.</div>
        <div class="rec">✅ See Full 7-Day Calendar section for all events and RSVP status.</div>
      </div>
    </div>

    <!-- MEDICAL / HEALTH -->
    <div class="cat-card">
      <div class="cat-card-header cat-blue">
        <div class="cat-count">2</div>
        <div class="cat-title">🔵 Medical / Health</div>
        <div class="cat-tag">CALENDAR-CONFIRMED</div>
      </div>
      <div class="cat-card-body">
        <div class="senders"><strong>Events:</strong> Stephanie Infusion (Aug 10), MRI Brain W&amp;WO IVC (Aug 11), PT (Aug 12)</div>
        <ul class="detail-list">
          <li>These are calendar events, not emails. See Calendar section for full details.</li>
          <li>MRI is the most prep-intensive — arrive 8:50 AM at 159 E 53rd St, remove all metal beforehand.</li>
          <li>No health-related emails in inbox (spam GLP-1 ads are categorized under Security/Risk).</li>
        </ul>
        <div class="rec">✅ Recommended: Confirm logistics for Monday and Tuesday appointments. Review MRI prep instructions carefully.</div>
      </div>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="cat-card">
      <div class="cat-card-header cat-yellow">
        <div class="cat-count">3</div>
        <div class="cat-title">🟡 Financial / Billing</div>
        <div class="cat-tag">ACTION NEEDED</div>
      </div>
      <div class="cat-card-body">
        <div class="senders"><strong>Senders:</strong> Bank of America (fraud claim canceled), Amazon order confirmation (rescued), 1-800 Contacts (20% off — expires tonight, trashed)</div>
        <ul class="detail-list">
          <li><strong>BofA Fraud Claim Canceled</strong> — Account -2994. Verify you authorized this cancellation today.</li>
          <li><strong>Amazon Order: 1 Beverages Item</strong> (rescued) — Purchase confirmation. Keep for records.</li>
          <li><strong>1-800 Contacts: 20% off expires tonight</strong> (trashed) — Save instantly by 11:59 PM MT. If you need contacts, act before midnight tonight.</li>
        </ul>
        <div class="rec">⚡ Recommended: Verify BofA claim status NOW. Note 1-800 Contacts discount expires tonight if relevant.</div>
      </div>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="cat-card">
      <div class="cat-card-header cat-purple">
        <div class="cat-count">1</div>
        <div class="cat-title">🟣 Professional Development</div>
        <div class="cat-tag">OPTIONAL</div>
      </div>
      <div class="cat-card-body">
        <div class="senders"><strong>Senders:</strong> Alison Courses (trashed)</div>
        <ul class="detail-list">
          <li>
