<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Melissa's Executive Briefing — Friday, June 5, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* Header */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: white; border-radius: 16px; padding: 32px 36px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px; }
  .header-left h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header-left .subtitle { font-size: 14px; color: #a0b4c8; margin-top: 4px; }
  .header-right { text-align: right; }
  .header-right .stat { background: rgba(255,255,255,0.1); border-radius: 10px; padding: 8px 16px; margin-bottom: 8px; font-size: 13px; color: #e0eaff; }
  .header-right .stat strong { color: #fff; font-size: 18px; display: block; }
  .badge-row { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 12px; }
  .badge { border-radius: 20px; padding: 4px 12px; font-size: 11px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; }
  .badge-red { background: #ff4757; color: white; }
  .badge-yellow { background: #ffa502; color: #1a1a2e; }
  .badge-green { background: #2ed573; color: #1a1a2e; }
  .badge-blue { background: #1e90ff; color: white; }

  /* Section */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; letter-spacing: 0.3px; padding: 10px 16px; border-radius: 10px 10px 0 0; color: white; display: flex; align-items: center; gap: 8px; }
  .section-body { background: white; border-radius: 0 0 12px 12px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .section-solo { background: white; border-radius: 12px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }

  .title-red { background: #c0392b; }
  .title-yellow { background: #d4a017; }
  .title-blue { background: #1565c0; }
  .title-green { background: #1b5e20; }
  .title-purple { background: #4a148c; }
  .title-gray { background: #546e7a; }
  .title-dark { background: #1a1a2e; }
  .title-teal { background: #00695c; }
  .title-orange { background: #e65100; }

  /* Executive Summary */
  .exec-summary { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; }
  .exec-card { border-radius: 12px; padding: 16px 18px; border-left: 5px solid; }
  .exec-card.red { background: #fff5f5; border-color: #e53e3e; }
  .exec-card.green { background: #f0fff4; border-color: #38a169; }
  .exec-card.blue { background: #ebf8ff; border-color: #3182ce; }
  .exec-card .ec-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
  .exec-card.red .ec-label { color: #c53030; }
  .exec-card.green .ec-label { color: #276749; }
  .exec-card.blue .ec-label { color: #2b6cb0; }
  .exec-card h3 { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
  .exec-card p { font-size: 13px; color: #444; }

  /* Action Cards */
  .action-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; }
  .action-card { border-radius: 12px; padding: 16px; border-top: 4px solid; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
  .action-card.red { border-color: #e53e3e; background: #fffafa; }
  .action-card.yellow { border-color: #d69e2e; background: #fffbeb; }
  .action-card.green { border-color: #38a169; background: #f0fff4; }
  .action-card.blue { border-color: #3182ce; background: #ebf8ff; }
  .action-card.purple { border-color: #805ad5; background: #faf5ff; }
  .action-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
  .action-card.red .action-label { color: #c53030; }
  .action-card.yellow .action-label { color: #b7791f; }
  .action-card.green .action-label { color: #276749; }
  .action-card.blue .action-label { color: #2b6cb0; }
  .action-card.purple .action-label { color: #553c9a; }
  .action-card h3 { font-size: 14px; font-weight: 700; margin-bottom: 10px; }
  .action-row { display: flex; gap: 6px; margin-bottom: 4px; font-size: 12px; flex-wrap: wrap; }
  .action-key { font-weight: 700; color: #555; min-width: 120px; }
  .action-val { color: #222; }
  .action-step { background: rgba(0,0,0,0.05); border-radius: 6px; padding: 6px 10px; margin-top: 8px; font-size: 12px; font-weight: 600; }

  /* Calendar */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { background: #1565c0; color: white; border-radius: 8px 8px 0 0; padding: 8px 14px; font-weight: 700; font-size: 13px; }
  .cal-event { background: #f8faff; border-left: 4px solid #1e90ff; padding: 10px 14px; margin-bottom: 2px; }
  .cal-event:last-child { border-radius: 0 0 8px 8px; }
  .cal-event-title { font-weight: 700; font-size: 13px; margin-bottom: 4px; }
  .cal-meta { font-size: 11px; color: #555; display: flex; gap: 12px; flex-wrap: wrap; }
  .cal-meta span { display: flex; align-items: center; gap: 3px; }
  .status-confirmed { color: #276749; font-weight: 700; }
  .status-accepted { color: #2b6cb0; font-weight: 700; }
  .status-declined { color: #c53030; font-weight: 700; }
  .status-needs { color: #b7791f; font-weight: 700; }
  .conflict-warn { background: #fff3cd; border: 1px solid #ffc107; border-radius: 6px; padding: 4px 8px; margin-top: 6px; font-size: 11px; color: #856404; font-weight: 600; }

  /* Tables */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #1a1a2e; color: white; padding: 9px 12px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
  td { padding: 8px 12px; border-bottom: 1px solid #eee; vertical-align: top; }
  tr:nth-child(even) td { background: #f8f9fa; }
  tr:hover td { background: #eef2ff; }
  .pri-high { background: #ffe8e8; color: #c0392b; font-weight: 700; border-radius: 4px; padding: 2px 7px; font-size: 11px; }
  .pri-med { background: #fff3cd; color: #856404; font-weight: 700; border-radius: 4px; padding: 2px 7px; font-size: 11px; }
  .pri-low { background: #e8f5e9; color: #2e7d32; font-weight: 700; border-radius: 4px; padding: 2px 7px; font-size: 11px; }
  .rec-keep { color: #2e7d32; font-weight: 600; }
  .rec-review { color: #b7791f; font-weight: 600; }
  .rec-delete { color: #c53030; font-weight: 600; }
  .rec-unsub { color: #805ad5; font-weight: 600; }
  .rec-restore { color: #2b6cb0; font-weight: 600; }

  /* Category blocks */
  .cat-block { border-radius: 10px; padding: 14px 16px; margin-bottom: 12px; border-left: 5px solid; }
  .cat-block.red { background: #fff5f5; border-color: #fc8181; }
  .cat-block.yellow { background: #fffbeb; border-color: #f6c90e; }
  .cat-block.green { background: #f0fff4; border-color: #68d391; }
  .cat-block.blue { background: #ebf8ff; border-color: #63b3ed; }
  .cat-block.purple { background: #faf5ff; border-color: #b794f4; }
  .cat-block.gray { background: #f7f7f7; border-color: #a0aec0; }
  .cat-block.teal { background: #e6fffa; border-color: #4fd1c5; }
  .cat-block.orange { background: #fff5f0; border-color: #fc9867; }
  .cat-block h4 { font-size: 13px; font-weight: 700; margin-bottom: 6px; display: flex; align-items: center; gap: 8px; }
  .cat-count { background: #1a1a2e; color: white; border-radius: 10px; padding: 1px 8px; font-size: 11px; font-weight: 700; }
  .cat-block p, .cat-block ul { font-size: 12px; color: #444; }
  .cat-block ul { margin-left: 16px; margin-top: 4px; }
  .cat-block li { margin-bottom: 2px; }
  .cat-action { margin-top: 6px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }

  /* Trash groups */
  .trash-group { border-radius: 10px; padding: 14px 16px; margin-bottom: 12px; }
  .trash-restore { background: #ebf8ff; border: 2px solid #3182ce; }
  .trash-review { background: #fffbeb; border: 2px solid #d69e2e; }
  .trash-delete { background: #fff5f5; border: 2px solid #e53e3e; }
  .trash-group h4 { font-size: 13px; font-weight: 700; margin-bottom: 8px; }
  .trash-group ul { font-size: 12px; margin-left: 16px; }
  .trash-group li { margin-bottom: 3px; }

  /* Dashboard */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; }
  .dash-card { border-radius: 12px; padding: 14px 16px; text-align: center; }
  .dash-card.red { background: linear-gradient(135deg, #ffe0e0, #ffcdd2); border: 1px solid #ef9a9a; }
  .dash-card.yellow { background: linear-gradient(135deg, #fff9e6, #fff3cd); border: 1px solid #ffe082; }
  .dash-card.green { background: linear-gradient(135deg, #e8f5e9, #c8e6c9); border: 1px solid #a5d6a7; }
  .dash-card.blue { background: linear-gradient(135deg, #e3f2fd, #bbdefb); border: 1px solid #90caf9; }
  .dash-card.purple { background: linear-gradient(135deg, #f3e5f5, #e1bee7); border: 1px solid #ce93d8; }
  .dash-card .dash-num { font-size: 36px; font-weight: 800; line-height: 1.1; }
  .dash-card.red .dash-num { color: #c62828; }
  .dash-card.yellow .dash-num { color: #f57f17; }
  .dash-card.green .dash-num { color: #2e7d32; }
  .dash-card.blue .dash-num { color: #1565c0; }
  .dash-card.purple .dash-num { color: #6a1b9a; }
  .dash-card .dash-label { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin-top: 4px; }
  .dash-card .dash-detail { font-size: 11px; color: #555; margin-top: 4px; }

  /* Top 3 */
  .top3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }
  .top3-card { border-radius: 14px; padding: 20px; color: white; position: relative; overflow: hidden; }
  .top3-card.one { background: linear-gradient(135deg, #c62828, #b71c1c); }
  .top3-card.two { background: linear-gradient(135deg, #1b5e20, #2e7d32); }
  .top3-card.three { background: linear-gradient(135deg, #1565c0, #0d47a1); }
  .top3-card .num { font-size: 48px; font-weight: 900; opacity: 0.2; position: absolute; top: 10px; right: 16px; line-height: 1; }
  .top3-card h3 { font-size: 15px; font-weight: 700; margin-bottom: 6px; }
  .top3-card p { font-size: 12px; opacity: 0.9; }

  /* Job pipeline */
  .job-row td:first-child { font-weight: 600; }
  .fit-high { color: #2e7d32; font-weight: 700; }
  .fit-med { color: #f57f17; font-weight: 700; }
  .fit-low { color: #c62828; font-weight: 700; }

  /* Divider */
  .divider { height: 2px; background: linear-gradient(to right, #1a1a2e, transparent); margin: 24px 0; border-radius: 2px; }

  /* Pill */
  .pill { display: inline-block; border-radius: 12px; padding: 2px 8px; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
  .pill-red { background: #ffe8e8; color: #c0392b; }
  .pill-yellow { background: #fff3cd; color: #856404; }
  .pill-green { background: #e8f5e9; color: #2e7d32; }
  .pill-blue { background: #e3f2fd; color: #1565c0; }
  .pill-gray { background: #f0f0f0; color: #555; }

  .note { font-size: 11px; color: #777; font-style: italic; margin-top: 6px; }
  .unread-dot { display: inline-block; width: 8px; height: 8px; background: #e53e3e; border-radius: 50%; margin-right: 4px; }

  .total-row td { font-weight: 700; background: #1a1a2e !important; color: white; }
  
  @media (max-width: 600px) {
    .header { flex-direction: column; }
    .header-right { text-align: left; }
  }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 1. HEADER -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="header">
  <div class="header-left">
    <h1>👋 Good morning, Melissa!</h1>
    <div class="subtitle">Executive Briefing — Friday, June 5, 2026</div>
    <div class="badge-row">
      <span class="badge badge-red">⚠ 3 Security Alerts</span>
      <span class="badge badge-yellow">⏰ 4 Actions Required</span>
      <span class="badge badge-green">🎯 Active Job Search</span>
      <span class="badge badge-blue">📅 9 Calendar Events</span>
    </div>
  </div>
  <div class="header-right">
    <div class="stat"><strong>50</strong> Total Emails Reviewed</div>
    <div class="stat"><strong>9</strong> Calendar Events (Next 7 Days)</div>
    <div class="stat"><strong>12</strong> Emails in Trash</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 2. EXECUTIVE SUMMARY -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title title-dark">⚡ Executive Summary</div>
  <div class="section-body">
    <div class="exec-summary">
      <div class="exec-card red">
        <div class="ec-label">🔴 Biggest Risk / Urgent</div>
        <h3>Multiple Phishing & Spam Attacks Detected</h3>
        <p>At least 5 phishing/scam emails identified (fake claims, fake storage alerts, explicit spam, fake Lowe's prize). Do NOT click any links. Mark all as spam immediately. Also: a Robinhood IRA distribution email in Trash needs verification — confirm you initiated this withdrawal.</p>
      </div>
      <div class="exec-card green">
        <div class="ec-label">🟢 Biggest Job Search / Opportunity</div>
        <h3>HR Search Pipeline Active — 4 Priority Leads + Netta Jenkins Meeting Tue 6/9</h3>
        <p>Your automated HR job search (GitHub Actions) surfaced 4 priority leads and 10 strategic leads today. You have a 15-min Zoom consultation with Netta Jenkins (netta@hicconsult.com) on Tuesday June 9 at noon. Your outreach email to Jillian re: deck/board meeting follow-up was sent this morning — awaiting response.</p>
      </div>
      <div class="exec-card blue">
        <div class="ec-label">🔵 Biggest Calendar / Deadline Item</div>
        <h3>State Farm Bill Due Sunday 6/7 + Doctor's Appointment Monday 6/8</h3>
        <p>State Farm payment is flagged as due on June 7. Dr. Robert Lippe appointment is confirmed for June 8 at 2:15 PM in Massapequa. You also have a TikTok Shop order out for delivery today and Bank of America credit card (ending 4018) arriving today.</p>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 3. ACTION REQUIRED -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title title-red">🚨 Action Required</div>
  <div class="section-body">
    <div class="action-grid">

      <div class="action-card red">
        <div class="action-label">🔴 Security — Verify Immediately</div>
        <h3>Robinhood IRA Distribution Initiated</h3>
        <div class="action-row"><span class="action-key">Source:</span><span class="action-val">Robinhood (noreply@robinhood.com) — found in Trash</span></div>
        <div class="action-row"><span class="action-key">Why It Matters:</span><span class="action-val">An IRA withdrawal was initiated from your Robinhood account. This may be legitimate, but if you did NOT authorize this, it requires immediate action to prevent tax penalties and unauthorized account access.</span></div>
        <div class="action-row"><span class="action-key">Trade Confirmations:</span><span class="action-val">Separate Robinhood email (in Inbox) also shows trade confirmations available to review.</span></div>
        <div class="action-step">✅ NEXT STEP: Log in to Robinhood directly (do not click email link) and verify both the IRA distribution and trade confirmations. If unauthorized, contact Robinhood support immediately.</div>
        <div class="action-row" style="margin-top:8px;"><span class="action-key">Due:</span><span class="action-val"><strong>TODAY — June 5, 2026</strong></span></div>
      </div>

      <div class="action-card red">
        <div class="action-label">🔴 Security — Do Not Engage</div>
        <h3>5 Phishing / Scam Emails Detected</h3>
        <div class="action-row"><span class="action-key">Sources:</span><span class="action-val">Fake "Claims Department" (yzvkmh.lt), Fake "Payment Declined" cloud storage (×2), Fake Lowe's prize, Explicit spam</span></div>
        <div class="action-row"><span class="action-key">Why It Matters:</span><span class="action-val">These are sophisticated phishing attempts using your Gmail username. Several impersonate legitimate brands. The explicit spam email appears to use your own email address as sender (spoofed).</span></div>
        <div class="action-step">✅ NEXT STEP: Mark all as spam/phishing. Do NOT click any links. Consider enabling Gmail's enhanced safe browsing. Change password if concerned about the spoofed sender.</div>
        <div class="action-row" style="margin-top:8px;"><span class="action-key">Due:</span><span class="action-val"><strong>TODAY — June 5, 2026</strong></span></div>
      </div>

      <div class="action-card yellow">
        <div class="action-label">🟡 Billing / Deadline</div>
        <h3>State Farm Bill Due June 7</h3>
        <div class="action-row"><span class="action-key">Source:</span><span class="action-val">Google Calendar — "State farm bill" (all-day event June 7)</span></div>
        <div class="action-row"><span class="action-key">Why It Matters:</span><span class="action-val">Insurance payment deadline is this Sunday. Missing it could affect coverage.</span></div>
        <div class="action-step">✅ NEXT STEP: Schedule or confirm State Farm payment before Sunday June 7.</div>
        <div class="action-row" style="margin-top:8px;"><span class="action-key">Due:</span><span class="action-val"><strong>Sunday, June 7, 2026</strong></span></div>
      </div>

      <div class="action-card yellow">
        <div class="action-label">🟡 RSVP Required</div>
        <h3>HR Networking Group — 2 Events Need RSVP</h3>
        <div class="action-row"><span class="action-key">Source:</span><span class="action-val">Google Calendar — June 10 (12–1:30 PM) & June 11 (12–1 PM) Zoom</span></div>
        <div class="action-row"><span class="action-key">Why It Matters:</span><span class="action-val">Both HR Networking Zoom events show status "needsAction" — you have not RSVP'd. The June 10 event conflicts with your "Melissa x Meg drinks" meeting at 1 PM.</span></div>
        <div class="action-step">✅ NEXT STEP: RSVP to both events. Note the conflict on June 10 between the networking call (ends 1:30 PM) and drinks with Meg (starts 1:00 PM) — reschedule or adjust one.</div>
        <div class="action-row" style="margin-top:8px;"><span class="action-key">Due:</span><span class="action-val"><strong>Before June 10–11</strong></span></div>
      </div>

      <div class="action-card green">
        <div class="action-label">🟢 Job Search — Follow-Up</div>
        <h3>Follow-Up: Jillian / Deck Opportunity</h3>
        <div class="action-row"><span class="action-key">Source:</span><span class="action-val">Sent email — "Re: Melissa A Weiss - Deck" (Fri Jun 5, 8:25 AM)</span></div>
        <div class="action-row"><span class="action-key">Why It Matters:</span><span class="action-val">You sent a follow-up to Jillian this morning referencing a board meeting and a career opportunity. Awaiting her response.</span></div>
        <div class="action-step">✅ NEXT STEP: If no response by EOD Monday June 8, send a brief follow-up. Flag Jillian's email for follow-up reminder.</div>
        <div class="action-row" style="margin-top:8px;"><span class="action-key">Due:</span><span class="action-val"><strong>Follow-up by Monday, June 8</strong></span></div>
      </div>

      <div class="action-card blue">
        <div class="action-label">🔵 Medical — Appointment Prep</div>
        <h3>Dr. Robert Lippe Appointment — Monday June 8</h3>
        <div class="action-row"><span class="action-key">Source:</span><span class="action-val">MyNorthwell email + Calendar "Eye" event, June 8, 9:00–10:00 AM / Northwell: 2:15 PM</span></div>
        <div class="action-row"><span class="action-key">Why It Matters:</span><span class="action-val">Northwell Health reminder for Dr. Robert Lippe, MD at 660 Broadway, Massapequa NY at 2:15 PM on June 8. Calendar also shows an "Eye" appointment at 9 AM the same day — confirm both are the same or separate.</span></div>
        <div class="action-step">✅ NEXT STEP: Confirm whether the 9 AM "Eye" calendar event and the 2:15 PM Northwell appointment are the same or two separate appointments on June 8. Prepare insurance card and any required forms.</div>
        <div class="action-row" style="margin-top:8px;"><span class="action-key">Due:</span><span class="action-val"><strong>Monday, June 8, 2026</strong></span></div>
      </div>

      <div class="action-card yellow">
        <div class="action-label">🟡 Delivery — Today</div>
        <h3>Bank of America Credit Card (4018) Out for Delivery</h3>
        <div class="action-row"><span class="action-key">Source:</span><span class="action-val">Bank of America (ealerts.bankofamerica.com) — Step 3 of 3</span></div>
        <div class="action-row"><span class="action-key">Why It Matters:</span><span class="action-val">Your new credit card ending in 4018 is out for delivery today. Plan to be available or check your mailbox. Activate promptly upon receipt.</span></div>
        <div class="action-step">✅ NEXT STEP: Retrieve card from mailbox today. Activate and store securely. Also note: a $40 Venmo cashout direct deposit was credited to your checking account (–7471) overnight.</div>
        <div class="action-row" style="margin-top:8px;"><span class="action-key">Due:</span><span class="action-val"><strong>TODAY — June 5, 2026</strong></span></div>
      </div>

      <div class="action-card yellow">
        <div class="action-label">🟡 Amazon Returns</div>
        <h3>Amazon Return: Vetinee Jean Shorts — Drop Off by July 5</h3>
        <div class="action-row"><span class="action-key">Source:</span><span class="action-val">Amazon return@amazon.com — addressed to "Sophie"</span></div>
        <div class="action-row"><span class="action-key">Why It Matters:</span><span class="action-val">Return request confirmed. Drop off at any UPS location by Sunday, July 5. Note: this Amazon account appears to be under "Sophie Weiss" — confirm this is your account/family member.</span></div>
        <div class="action-step">✅ NEXT STEP: Package item and drop off at UPS before July 5. Note the "Sophie Weiss" naming on several Amazon emails — verify account ownership if needed.</div>
<hr>
<h2>Trash Review</h2>
<p><strong>Purpose:</strong> Review deleted emails for anything important before permanent deletion. Anything from job search, billing, medical, calendar, security, legal, GitHub, Netlify, LinkedIn, recruiters, or professional contacts should be reviewed before deleting.</p>

<h2>Promotional / Retail Summary</h2>
<p><strong>Purpose:</strong> Promotional emails are included in the full email inventory below. Delete or ignore retail/promotional items unless there is a deal you actually plan to use or a sender looks suspicious.</p>

<h2>Email Accounting</h2>
<p><strong>Total Emails Reviewed:</strong> 50</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Category</th><th>Count</th></tr>
<tr><td>Job Search / Recruiters</td><td>1</td></tr>
<tr><td>Medical / Health</td><td>4</td></tr>
<tr><td>Other / Review</td><td>36</td></tr>
<tr><td>Professional Development / Newsletters</td><td>3</td></tr>
<tr><td>Promotional / Retail</td><td>3</td></tr>
<tr><td>Security / Risk</td><td>3</td></tr>
</table>

<h2>Full Email Inventory</h2>
<p><strong>Every fetched email is listed below.</strong> Use this section to see what to act on, review, delete, or ignore.</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr>
  <th>#</th>
  <th>Category</th>
  <th>From</th>
  <th>Subject</th>
  <th>Date</th>
  <th>Labels</th>
  <th>Snippet</th>
  <th>Recommendation</th>
</tr>

<div style="background:#f0fff4; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Job Search / Recruiters (1)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#33 · Fri, 05 Jun 2026 05:34:33 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Melissa A, simple ways to make a difference this World Environment Day. 💚</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Alison Courses &lt;noreply@us-news.alison.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Learn how to take care of the environment. View in web browser Share on social Share on Facebook Share on Twitter Share on Linkedin Alison My Dashboar</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review for opportunity or follow-up</div>
</div>
</div>

<div style="background:#ebf8ff; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Medical / Health (4)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#2 · Fri, 05 Jun 2026 12:30:41 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Sensitive Skin, Simplified</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Paul Labrecque Salon &amp; Skincare Spa&quot; &lt;customercare@paullabrecque.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Calm, soothe, rebalance ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#13 · Fri, 05 Jun 2026 11:28:40 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Get ready for your visit on 6/8</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> MyNorthwell &lt;northwell@my.northwellhealth.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">We look forward to seeing you Melissa, get ready for your visit June 8, 2026 2:15 PM With Dr. Robert Lippe, MD 660 Broadway Massapequa NY 11758-1204 G</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#21 · Fri, 05 Jun 2026 11:02:53 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Bypassing Hormuz, GLP-1 Returns, and Your Most Important Health Metric</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;1% Better&quot; &lt;hello@onepercentimprovements.convertkit.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">You improve every day. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#35 · Fri, 05 Jun 2026 05:16:47 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Big Mid-Year Energy: Extra 15% OFF starts NOW! ⚡No min. spend</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;YesStyle.com&quot; &lt;crm@shop.yesstyle.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">We&amp;#39;ve got a secret (and it&amp;#39;s 15% OFF) View in Browser YesStyle.com Beauty Women Men Health We&amp;#39;ve got a secret (and it&amp;#39;s 15% OFF) *Term</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>
</div>

<div style="background:#f7fafc; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Other / Review (36)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#1 · Fri, 05 Jun 2026 12:33:03 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">[Final Reminder] Live with the Smart Cups founder, Today June 5</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Highlander Updates &lt;hello@news.highlander.ai&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">An hour with Chris Kanik on the technology, the partnerships, the road ahead. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#4 · Fri, 05 Jun 2026 13:26:09 +0100</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">🚨Final Notice🚨: melissaw212 Claim Your Funds Now💸_KS</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;&#x27;Claims_Department&#x27;&quot; &lt;fzhzH@yzvkmh.lt&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">💰 Unclaimed Assets Alert! Name melissaw212 – melissaw212@gmail.com To: melissaw212@gmail.com Dear melissaw212, 🔎 We&amp;#39;ve identified unclaimed financ</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#5 · Fri, 5 Jun 2026 08:25:44 -0400</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Re: Melissa A Weiss - Deck</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> melissa &lt;melissaw212@gmail.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">﻿Hi Jillian, Happy Friday! I hope you&amp;#39;re doing well and that the board meeting was a success. I wanted to follow up regarding the opportunity, as </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#6 · Fri, 05 Jun 2026 06:09:06 -0600</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Delivery status of credit card - 4018 - We&#x27;ve updated your status</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Bank of America &lt;onlinebanking@ealerts.bankofamerica.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">We&amp;#39;ve updated your status Delivery status of credit card - 4018 Step 3 of 3 Your card is out for delivery Updated June 05 You can expect to have y</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#7 · Fri, 05 Jun 2026 12:07:49 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">IRA distribution initiated</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Robinhood &lt;noreply@robinhood.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Your withdrawal from your IRA is on the way You withdrew money from your IRA Hi Melissa, Your money is on the way! Here are the details of your withdr</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#8 · Fri, 05 Jun 2026 06:03:22 -0600</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Make soccer your whole personality⚽</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Zappos &lt;cs@emails.zappos.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Styles worth rooting for ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#12 · Fri, 05 Jun 2026 11:30:00 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">How to Master Claude: 8 Simple Habits That Separate Power Users From Everyone Else. | Mouez Yazidi in Towards AI</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Medium Daily Digest &lt;noreply@medium.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Melissaw Stories for Melissaw @melissaw212·Become a member Medium daily digest Today&amp;#39;s highlights Mouez Yazidi Mouez YazidiinTowards AI How to Mas</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#14 · Fri, 05 Jun 2026 11:21:57 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">(how to move forward)</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Lisa Rangel &lt;lr@chameleonresumes.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">(how to move forward) Some senior leaders carry the past around like luggage they never unpacked. The tactics that used to work and then stopped. The </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#15 · Fri, 05 Jun 2026 11:21:35 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Your Daily Digest for Fri, 6/5 is ready to view</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> USPS Informed Delivery &lt;USPSInformeddelivery@email.informeddelivery.usps.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">COMING TO YOU SOON Hi, Meliss! You have 1 mailpiece(s) and 1 inbound package(s) arriving soon. Friday 5 June 2026 1 Mailpiece(s) 1 Package(s) Hi, Meli</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#16 · Fri, 05 Jun 2026 07:19:10 -0400</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">WATCH THIS FILTHY +18 VIDEO NOW🔞</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> melissaw212 &lt;lplmgktcovtlio.91392785654833@qbpr5a.w83ksr.68ved3.us&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Explicit +18 – Destroy her pussy tonight with this raw 7-second trick. 🍆 DESTROY HER PUSSY TONIGHT 💦 FUCK HER TILL SHE SQUIRTS, SCREAMS &amp;amp; CAN&amp;#39;</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#18 · Fri, 5 Jun 2026 04:12:30 -0700</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Melissa&#x27;s Daily Briefing - June 5, 2026</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> melissa &lt;melissaw212@gmail.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">📋 MELISSA&amp;#39;S DAILY BRIEFING Friday, June 5, 2026 | Good morning, Melissa! Here&amp;#39;s everything you need to know today. ⚡ EXECUTIVE SUMMARY 🔴 URGEN</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#20 · Fri, 05 Jun 2026 21:06:13 +1000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">😐 It’s mid</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> The Average Joe &lt;joe@readthejoe.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Transport stocks hit the spotlight ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#22 · Fri, 5 Jun 2026 06:43:06 -0400</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">🏀  Merch gets a makeover </div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> The Hustle &lt;news@thehustle.co&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Plus: A farmer turned influencer, a different Dracula, and more. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#23 · Fri, 5 Jun 2026 06:13:14 -0400 (EDT)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">The father, son, and energy drink</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> The Daily Skimm &lt;dailyskimm@morning7.theskimm.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">But first: this clairvoyant corgi is off to a rocky start — Check out what we Skimm&amp;#39;d for you today June 5, 2026 Subscribe Read in browser Header </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#24 · Fri, 5 Jun 2026 09:51:59 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Do you get scared of &quot;prompt engineering&quot;?</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> CoolDeep AI &lt;cooldeepai@mail.beehiiv.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Most people blame Claude. The problem is actually the prompt. ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#25 · Fri, 05 Jun 2026 05:12:10 -0400</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">We have been trying to reach you - melissaw212</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot; &#x27;Lowe&#x27;s®&#x27; &quot; &lt;melissaw212@jmixpqpckiood.q2k9zmn7.edge-relay.cloudpilot.org.carvellingo.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Lowe&amp;#39;s - Fri,05 Jun-2026 Dear melissaw212, Congratulations! YOU ARE OUR WINNER Kobalt Tool Set from Lowe&amp;#39;s You&amp;#39;ve been chosen to receive a</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#27 · Fri, 05 Jun 2026 02:38:43 -0600</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">A direct deposit was credited to your account</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Bank of America &lt;onlinebanking@ealerts.bankofamerica.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">A direct deposit was credited to your account Amount $40.00 Account PERSONAL CHECKING/SAVINGS ACCOUNT - 7471 Date June 05, 2026 From VENMO CASHOUT VIE</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#28 · Fri, 05 Jun 2026 08:13:06 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Just in at Cprime: This week&#x27;s employee reviews and more</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Glassdoor &lt;noreply@glassdoor.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Hey, Sophie! Check out recent updates from Cprime and stay on top of your work game. ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​‍‎‏﻿ ‌​</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#29 · Fri, 5 Jun 2026 07:41:23 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Your Carmel Points for the month of May</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Carmel Points &lt;Points@carmelcarservice.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Dear, Melissa! Thank you for being a Carmel Customer. We hope you are enjoying the Carmel Points program. Here is your monthly statement for the month</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#31 · Fri, 05 Jun 2026 00:49:37 -0500</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">You&#x27;re getting attention: Jim viewed your profile.</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Match &lt;mailer@value.match.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">See who&amp;#39;s viewed your profile ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#32 · Fri, 5 Jun 2026 05:45:39 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Shipped: &quot;Blooming Jelly Women&#x27;s...&quot;</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Amazon.com&quot; &lt;shipment-tracking@amazon.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Shipped: &amp;quot;Blooming Jelly Women&amp;#39;s...&amp;quot;͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#34 · Fri, 05 Jun 2026 00:30:24 -0500</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Melissa, you&#x27;ve still got an unread message. See what they said. 👉</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Match &lt;mailer@value.match.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">You know you&amp;#39;re curious. ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#36 · Fri, 05 Jun 2026 04:43:19 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Your trade confirmations are available</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Robinhood &lt;noreply@robinhood.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">View your trade confirmations Your trade confirmations are available Hi Melissa, your recent trade confirmations are available. Trade confirmations de</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#37 · Fri, 5 Jun 2026 04:10:49 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Shipped: &quot;Daci Black One Shoulder One...&quot;</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Amazon.com&quot; &lt;shipment-tracking@amazon.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Shipped: &amp;quot;Daci Black One Shoulder One...&amp;quot;͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#38 · Fri, 5 Jun 2026 03:40:28 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Sophie Weiss, will you rate your transaction at Amazon.com?</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Amazon Marketplace &lt;marketplace-messages@amazon.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Hi Sophie Weiss, Rate your experience with the seller, Cabanana-US: 1 (Awful) 2 (Poor) 3 (Neutral) 4 (Good) 5 (Excellent) Cabanana-US (Fulfilled by Am</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#39 · Thu, 04 Jun 2026 22:38:25 -0500</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Someone likes you</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> OkCupid &lt;bounces@alerts.oknotify3.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Message them now ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#40 · Fri, 5 Jun 2026 03:26:12 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Ordered: &quot;Air Wick Essential Mist...&quot;</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Amazon.com&quot; &lt;auto-confirm@amazon.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Ordered: &amp;quot;Air Wick Essential Mist...&amp;quot;͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#41 · Mon, 25 May 2026 13:00:00 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">[Oracle University Learning Community] Oracle University Learning Community – Weekly Digest</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Oracle University Learning Community (NO-REPLY)&quot; &lt;ou.oracle@vanillaforums.email&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Oracle University Learning Community Oracle University Learning Community – Weekly Digest You&amp;#39;re receiving this weekly update because you follow o</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#42 · Fri, 5 Jun 2026 02:36:25 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Return request confirmed for Vetinee Jean Shorts for Women...</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;return@amazon.com&quot; &lt;return@amazon.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Amazon Amazon Hello Sophie, Your return request is confirmed. View return request Drop off by Sun, Jul 5 Dropoff location Any UPS Dropoff location Ite</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#43 · Fri, 5 Jun 2026 02:17:17 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Delivered: &quot;Vetinee Stretch Jean Shorts...&quot;</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Amazon.com&quot; &lt;order-update@amazon.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Delivered: &amp;quot;Vetinee Stretch Jean Shorts...&amp;quot;͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#44 · Fri, 5 Jun 2026 02:17:16 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Delivered: &quot;Utopia Towels, 35 by 70...&quot;</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Amazon.com&quot; &lt;order-update@amazon.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Delivered: &amp;quot;Utopia Towels, 35 by 70...&amp;quot;͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#45 · Fri, 05 Jun 2026 01:56:11 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Your Reimbursement Is Ready!</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Temu &lt;email@news.temuemail.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Your purchase is on us for 24H. ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#46 · Thu, 04 Jun 2026 20:44:38 -0500</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">You&#x27;re getting attention: Jim viewed your profile.</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Match &lt;mailer@value.match.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">See who&amp;#39;s viewed your profile ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#47 · Thu, 04 Jun 2026 18:38:07 -0700 (PDT)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">HR search AM — 2026-06-05 | 4 Priority · 10 Strategic · 14 Total</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> melissaw212@gmail.com</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">HR Search AM — 2026-06-05 Melissa Weiss · melissaw212@gmail.com · Exa (0 results) + Apify (14 results) · GitHub Actions 4 48h Priority 10 90h Strategi</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#48 · Fri, 05 Jun 2026 01:34:06 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">New from Olivia and other neighbors in New York</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Nextdoor &lt;no-reply@is.email.nextdoor.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Melissa, see your unread notifications͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#50 · Thu, 04 Jun 2026 18:28:00 -0700 (PDT)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">HR search AM — 2026-06-05 | 3 Priority · 6 Strategic · 9 Total</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> melissaw212@gmail.com</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">HR Search AM — 2026-06-05 Melissa Weiss · melissaw212@gmail.com · Exa (0 results) + Apify (9 results) · GitHub Actions 3 48h Priority 6 90h Strategic </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>
</div>

<div style="background:#faf5ff; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Professional Development / Newsletters (3)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#3 · Fri, 5 Jun 2026 12:29:12 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">(live rec.) Claude masterclass in HR ft. Sara Skowronski</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> The CHRO Office &lt;thehroffice@substack.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Sara Skowronski walked Insider Members through her real HR Claude workflow. Her exact prompts, her project setup, and the one rule she puts at the end</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#19 · Fri, 5 Jun 2026 11:02:49 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">MeidasTouch Full Podcast - 6/5/26 [AD-FREE]</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Meidas+&quot; &lt;meidastouch@substack.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Watch now (78 mins) | Watch the latest episode ad-free on the Meidas+ Substack ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#49 · Thu, 4 Jun 2026 18:33:12 -0700</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">VSU Multi-Purpose Center: See the latest updates</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> Facebook Pages &lt;pageupdates@facebookmail.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Check out what they share on Facebook. Explore this Page on Facebook. RECOMMENDED FOR YOU VSU Multi-Purpose Center Event Space 9K people follow this V</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Review</div>
</div>
</div>

<div style="background:#f7fafc; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Promotional / Retail (3)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#10 · Fri, 5 Jun 2026 12:01:16 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">A linen refresh: 25-40% off for her</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Macy&#x27;s&quot; &lt;shop@emails.macys.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Plus, $39.99 linen polos for him &amp;amp; more ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#17 · Fri, 05 Jun 2026 11:14:45 +0000</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">New Shades. For Every Summer Plan.</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> VIVAIA &lt;hello@edm.vivaia.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Lightweight comfort designed for spontaneous summer escapes. New｜Best Sellers｜Collection｜Sale NEW NEW NEW NEW NEW NEW NEW Flats｜Loafers｜Sneakers｜Bags </div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#30 · Fri, 05 Jun 2026 01:31:10 -0600</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Prices so LOW, your cart can&#x27;t keep up 🛒🛒</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;Kohl&#x27;s Lowest Prices of the Season&quot; &lt;kohls@s.kohls.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Plus, take up to 85% off clearance &amp;amp; earn Kohl&amp;#39;s Cash. ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Delete or ignore unless useful</div>
</div>
</div>

<div style="background:#fff5f5; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; margin:16px 0;">
  <h3 style="margin:0 0 8px 0; font-size:16px; color:#1a202c;">Security / Risk (3)</h3>
  
<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#9 · Fri, 05 Jun 2026 12:03:53 +0000 (UTC)</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">Your order is out for delivery!</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> TikTok Shop &lt;no-reply@shop-us.tiktok.com&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">Orders | Shopping cart Out for delivery Great news—your order is out for delivery! Here&amp;#39;s the tracking number to follow along: 4201002892612903397</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Act / Delete if scam</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#11 · Fri, 05 Jun 2026 07:56:41 -0400</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">melissaw212¸Your Account Has been Blocked! Your Photos and Videos will be Removed Fri,05 Jun-2026 . take action!</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;&#x27;&#x27;𝗣aym𝗲nt_Declin𝗲d&#x27;&quot; &lt;cdqxwyzmcsgbxj.28059046901028@8b7dwr.0xdpi7.1mvboh.us&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">☁️ Cloud We couldn&amp;#39;t renew your cloud storage subscription 0 GB 48.9 GB / 50 GB Please update your billing details to keep your storage active. Yo</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Act / Delete if scam</div>
</div>

<div style="border-left:4px solid #cbd5e0; background:#ffffff; margin:8px 0; padding:10px 12px; border-radius:8px;">
  <div style="font-size:12px; color:#718096; font-weight:700;">#26 · Fri, 05 Jun 2026 04:43:36 -0400</div>
  <div style="font-size:14px; font-weight:700; color:#1a202c;">melissaw212¸Your Account Has been Blocked! Your Photos and Videos will be Removed Fri,05 Jun-2026 . take action!</div>
  <div style="font-size:12px; color:#4a5568;"><strong>From:</strong> &quot;&#x27;𝗣aym𝗲nt_Declin𝗲d&#x27;&quot; &lt;jawveeeynklpti.25945690620630@r0g4k5.jm661g.t9w9z3.us&gt;</div>
  <div style="font-size:12px; color:#4a5568; margin-top:4px;">☁️ Cloud We couldn&amp;#39;t renew your cloud storage subscription 0 GB 48.9 GB / 50 GB Please update your billing details to keep your storage active. Yo</div>
  <div style="font-size:12px; font-weight:700; color:#2b6cb0; margin-top:6px;">Recommendation: Act / Delete if scam</div>
</div>
</div>
</table>

