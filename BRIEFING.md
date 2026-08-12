<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa — August 12, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: white; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 4px 20px rgba(0,0,0,0.25); }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header .subtitle { font-size: 15px; color: #a8b8d8; margin-top: 4px; }
  .header .meta { text-align: right; }
  .header .meta .stat { font-size: 13px; color: #a8b8d8; margin-top: 2px; }
  .badge { display: inline-block; background: #e94560; color: white; border-radius: 20px; padding: 3px 12px; font-size: 12px; font-weight: 700; margin-top: 8px; }

  /* SECTION TITLES */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; letter-spacing: 0.3px; margin-bottom: 14px; padding: 10px 16px; border-radius: 8px; display: flex; align-items: center; gap: 8px; }
  .section-title.red { background: #fff0f0; color: #b91c1c; border-left: 4px solid #ef4444; }
  .section-title.yellow { background: #fffbeb; color: #92400e; border-left: 4px solid #f59e0b; }
  .section-title.blue { background: #eff6ff; color: #1e40af; border-left: 4px solid #3b82f6; }
  .section-title.green { background: #f0fdf4; color: #166534; border-left: 4px solid #22c55e; }
  .section-title.purple { background: #faf5ff; color: #6b21a8; border-left: 4px solid #a855f7; }
  .section-title.gray { background: #f8fafc; color: #475569; border-left: 4px solid #94a3b8; }
  .section-title.dark { background: #1e293b; color: #f1f5f9; border-left: 4px solid #64748b; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; border: 1px solid; }
  .card.red { background: #fff5f5; border-color: #fecaca; }
  .card.yellow { background: #fffcf0; border-color: #fde68a; }
  .card.blue { background: #f0f7ff; border-color: #bfdbfe; }
  .card.green { background: #f0fdf6; border-color: #bbf7d0; }
  .card.purple { background: #fdf4ff; border-color: #e9d5ff; }
  .card.gray { background: #f8fafc; border-color: #e2e8f0; }
  .card.orange { background: #fff7ed; border-color: #fed7aa; }
  .card-label { font-size: 10px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px; }
  .card-label.red { color: #dc2626; }
  .card-label.yellow { color: #d97706; }
  .card-label.blue { color: #2563eb; }
  .card-label.green { color: #16a34a; }
  .card-label.purple { color: #9333ea; }
  .card-label.gray { color: #64748b; }
  .card-label.orange { color: #ea580c; }
  .card-title { font-size: 15px; font-weight: 700; margin-bottom: 4px; }
  .card-source { font-size: 12px; color: #64748b; margin-bottom: 6px; }
  .card-body { font-size: 13px; color: #374151; }
  .card-action { margin-top: 8px; font-size: 12px; font-weight: 600; padding: 5px 12px; border-radius: 6px; display: inline-block; }
  .card-action.red { background: #fee2e2; color: #b91c1c; }
  .card-action.yellow { background: #fef3c7; color: #92400e; }
  .card-action.green { background: #dcfce7; color: #15803d; }
  .card-action.blue { background: #dbeafe; color: #1d4ed8; }
  .card-action.purple { background: #ede9fe; color: #6d28d9; }
  .card-due { font-size: 11px; color: #6b7280; margin-top: 4px; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 6px rgba(0,0,0,0.07); }
  th { background: #1e293b; color: #f1f5f9; padding: 10px 14px; text-align: left; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
  td { padding: 9px 14px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #f8fafc; }
  tr:hover td { background: #f1f5f9; }

  /* TRIAGE TABLE */
  .triage-table th { background: #0f3460; }
  .triage-status { font-size: 12px; font-weight: 700; padding: 3px 8px; border-radius: 12px; white-space: nowrap; display: inline-block; }
  .s-rescued { background: #dcfce7; color: #15803d; }
  .s-inbox { background: #dbeafe; color: #1e40af; }
  .s-autotrash { background: #fee2e2; color: #991b1b; }
  .s-trash { background: #f1f5f9; color: #475569; }

  /* CALENDAR */
  .cal-day { margin-bottom: 16px; }
  .cal-day-header { background: #0f3460; color: white; padding: 8px 16px; border-radius: 8px 8px 0 0; font-weight: 700; font-size: 14px; }
  .cal-event { padding: 12px 16px; border-bottom: 1px solid #e2e8f0; background: white; }
  .cal-event:last-child { border-bottom: none; border-radius: 0 0 8px 8px; }
  .cal-event-time { font-weight: 700; color: #1e40af; font-size: 13px; }
  .cal-event-title { font-weight: 700; font-size: 14px; margin: 2px 0; }
  .cal-event-meta { font-size: 12px; color: #6b7280; margin-top: 3px; }
  .cal-rsvp { font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 10px; display: inline-block; }
  .rsvp-confirmed { background: #dcfce7; color: #15803d; }
  .rsvp-needs { background: #fef3c7; color: #92400e; }
  .rsvp-declined { background: #fee2e2; color: #b91c1c; }
  .rsvp-accepted { background: #dbeafe; color: #1e40af; }
  .cal-conflict { background: #fff7ed; border: 1px solid #fed7aa; border-radius: 6px; padding: 4px 10px; font-size: 11px; color: #c2410c; margin-top: 4px; display: inline-block; }
  .cal-prep { background: #f0f9ff; border-radius: 6px; padding: 4px 10px; font-size: 11px; color: #0369a1; margin-top: 4px; display: inline-block; }

  /* PRIORITY BADGES */
  .pri { font-size: 11px; font-weight: 800; padding: 2px 8px; border-radius: 10px; display: inline-block; }
  .pri-high { background: #fee2e2; color: #b91c1c; }
  .pri-med { background: #fef3c7; color: #92400e; }
  .pri-low { background: #f1f5f9; color: #64748b; }

  /* SUMMARY BULLETS */
  .exec-summary { background: white; border-radius: 12px; padding: 20px 24px; margin-bottom: 20px; box-shadow: 0 1px 8px rgba(0,0,0,0.08); }
  .exec-bullet { display: flex; align-items: flex-start; gap: 12px; padding: 10px 0; border-bottom: 1px solid #f1f5f9; }
  .exec-bullet:last-child { border-bottom: none; }
  .exec-icon { width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 16px; flex-shrink: 0; }
  .exec-icon.red { background: #fee2e2; }
  .exec-icon.green { background: #dcfce7; }
  .exec-icon.blue { background: #dbeafe; }

  /* DASHBOARD GRID */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-card { background: white; border-radius: 10px; padding: 16px; box-shadow: 0 1px 6px rgba(0,0,0,0.07); border-top: 3px solid; }
  .dash-card.red { border-top-color: #ef4444; }
  .dash-card.yellow { border-top-color: #f59e0b; }
  .dash-card.blue { border-top-color: #3b82f6; }
  .dash-card.green { border-top-color: #22c55e; }
  .dash-card.purple { border-top-color: #a855f7; }
  .dash-card.gray { border-top-color: #94a3b8; }
  .dash-card h4 { font-size: 11px; text-transform: uppercase; letter-spacing: 0.8px; color: #6b7280; margin-bottom: 8px; }
  .dash-card .val { font-size: 26px; font-weight: 800; color: #1e293b; }
  .dash-card .sub { font-size: 12px; color: #64748b; margin-top: 4px; }

  /* TOP 3 */
  .top3 { background: linear-gradient(135deg, #0f3460, #1a1a2e); color: white; border-radius: 12px; padding: 24px 28px; }
  .top3 h2 { font-size: 18px; font-weight: 700; margin-bottom: 16px; color: #f1f5f9; }
  .top3-item { display: flex; gap: 14px; align-items: flex-start; padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.1); }
  .top3-item:last-child { border-bottom: none; }
  .top3-num { width: 36px; height: 36px; border-radius: 50%; background: #e94560; color: white; font-size: 18px; font-weight: 800; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
  .top3-text strong { display: block; font-size: 15px; margin-bottom: 3px; }
  .top3-text span { font-size: 13px; color: #a8b8d8; }

  /* UTILITY */
  .rescued-tag { background: #dcfce7; color: #15803d; font-size: 11px; font-weight: 700; padding: 2px 7px; border-radius: 8px; margin-left: 6px; }
  .phish-tag { background: #fee2e2; color: #b91c1c; font-size: 11px; font-weight: 700; padding: 2px 7px; border-radius: 8px; margin-left: 6px; }
  .spam-tag { background: #f1f5f9; color: #475569; font-size: 11px; font-weight: 700; padding: 2px 7px; border-radius: 8px; margin-left: 6px; }
  .divider { height: 1px; background: #e2e8f0; margin: 28px 0; }
  ul.plain { list-style: none; }
  ul.plain li { padding: 3px 0; font-size: 13px; }
  ul.plain li::before { content: "• "; color: #94a3b8; }
  .fit-high { color: #15803d; font-weight: 700; }
  .fit-med { color: #d97706; font-weight: 700; }
  .fit-low { color: #64748b; font-weight: 600; }
  .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  @media(max-width: 700px) { .two-col { grid-template-columns: 1fr; } .header { flex-direction: column; gap: 12px; } .header .meta { text-align: left; } }
  .note { font-size: 12px; color: #6b7280; font-style: italic; margin-top: 6px; }
  .total-row td { font-weight: 800; background: #1e293b !important; color: white !important; }
</style>
</head>
<body>
<div class="page">

<!-- ============================================================ -->
<!--  SECTION 0 — EMAIL TRIAGE QUICK LIST                         -->
<!-- ============================================================ -->
<div class="section">
  <div class="section-title dark">📋 Email Triage Quick List</div>
  <table class="triage-table">
    <thead>
      <tr>
        <th style="width:110px">Status</th>
        <th style="width:180px">From</th>
        <th>Subject</th>
        <th>Summary</th>
      </tr>
    </thead>
    <tbody>
      <!-- RESCUED rows first -->
      <tr>
        <td><span class="triage-status s-rescued">✅ RESCUED</span></td>
        <td>USPS Tracking</td>
        <td>Expected Delivery Wed Aug 12 by 9:00pm</td>
        <td>Package arriving today by 9 PM. Tracking #9200190349635740890939. Was in Trash — rescued as legitimate shipping alert.</td>
      </tr>
      <tr>
        <td><span class="triage-status s-rescued">✅ RESCUED</span></td>
        <td>Center for Veterinary Care</td>
        <td>Autoship of Ursodiol Tablet for Stella — ships in 5 days</td>
        <td>Stella's Ursodiol autoship ships in ~5 days (approx Aug 17). Was in Trash — rescued as important pet medication notice.</td>
      </tr>
      <tr>
        <td><span class="triage-status s-rescued">✅ RESCUED</span></td>
        <td>Center for Veterinary Care</td>
        <td>Autoship of Denamarin Chewable Tablets for Stella — ships in 5 days</td>
        <td>Stella's Denamarin autoship ships in ~5 days (approx Aug 17). Was in Trash — rescued as important pet medication notice.</td>
      </tr>

      <!-- INBOX rows -->
      <tr>
        <td><span class="triage-status s-inbox">📥 INBOX</span></td>
        <td>SourceHire Jobs</td>
        <td>Confidential — Interview Update: Sr Director HR REQ93079 (×3)</td>
        <td>3 duplicate messages asking Melissa to confirm work authorization to keep application active. Action required.</td>
      </tr>
      <tr>
        <td><span class="triage-status s-inbox">📥 INBOX</span></td>
        <td>Old Navy</td>
        <td>An update to your order #1RHKTCJ</td>
        <td>Ship notification & receipt for Old Navy order. Review tracking details.</td>
      </tr>
      <tr>
        <td><span class="triage-status s-inbox">📥 INBOX</span></td>
        <td>Duane Reade Pharmacy</td>
        <td>We're Processing Your Auto Refill Order</td>
        <td>Prescription auto-refill scheduled for pickup Sat Aug 15. Confirm pickup plan.</td>
      </tr>
      <tr>
        <td><span class="triage-status s-inbox">📥 INBOX</span></td>
        <td>Synchrony Bank / CareCredit</td>
        <td>Your CARECREDIT / SYNCHRONY BANK Payment Has Posted</td>
        <td>$250.00 payment posted on account ending in 7483. For records.</td>
      </tr>
      <tr>
        <td><span class="triage-status s-inbox">📥 INBOX</span></td>
        <td>Danaher HR (Workday)</td>
        <td>Application Status Update — Sr Director HRBP</td>
        <td>Danaher responded to Melissa's HRBP application. Read immediately — may be advance, rejection, or info request.</td>
      </tr>
      <tr>
        <td><span class="triage-status s-inbox">📥 INBOX</span></td>
        <td>Match</td>
        <td>Marc likes you. See if it's mutual.</td>
        <td>Match.com notification — Marc expressed interest.</td>
      </tr>
      <tr>
        <td><span class="triage-status s-inbox">📥 INBOX</span></td>
        <td>Match</td>
        <td>Max likes you. See if it's mutual.</td>
        <td>Match.com notification — Max expressed interest.</td>
      </tr>
      <tr>
        <td><span class="triage-status s-inbox">📥 INBOX</span></td>
        <td>Match</td>
        <td>You've had a profile view from Tim</td>
        <td>Tim (66, Carle Place, NY) viewed Melissa's Match profile.</td>
      </tr>
      <tr>
        <td><span class="triage-status s-inbox">📥 INBOX</span></td>
        <td>OkCupid</td>
        <td>Someone likes you</td>
        <td>OkCupid like notification.</td>
      </tr>
      <tr>
        <td><span class="triage-status s-inbox">📥 INBOX</span></td>
        <td>Match</td>
        <td>Torres likes you. See if it's mutual.</td>
        <td>Match.com notification — Torres expressed interest.</td>
      </tr>
      <tr>
        <td><span class="triage-status s-inbox">📥 INBOX</span></td>
        <td>Amazon.com</td>
        <td>Shipped: 1 Jewelry item</td>
        <td>Amazon jewelry item has shipped. Check for tracking details.</td>
      </tr>
      <tr>
        <td><span class="triage-status s-inbox">📥 INBOX</span></td>
        <td>Bank of America</td>
        <td>My Credit: Monthly monitoring summary</td>
        <td>Monthly credit monitoring — no new alerts. Low priority, review for records.</td>
      </tr>
      <tr>
        <td><span class="triage-status s-inbox">📥 INBOX</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>Head of People Operations at Ladders</td>
        <td>Job alert: Head of People Operations — relevant to Melissa's search.</td>
      </tr>
      <tr>
        <td><span class="triage-status s-inbox">📥 INBOX</span></td>
        <td>George Bongiorno via LinkedIn</td>
        <td>GEORGE accepted your invitation — explore their network</td>
        <td>New LinkedIn connection accepted. Good time to send a follow-up message.</td>
      </tr>

      <!-- SUMMARY rows at bottom -->
      <tr>
        <td><span class="triage-status s-autotrash">🗑 AUTO-TRASHED</span></td>
        <td colspan="2"><strong>4 emails auto-trashed (phishing/fraud)</strong> — see Trash Review</td>
        <td>Cloud storage phish, fake CashApp payment, fake payment block notice. Removed before inbox.</td>
      </tr>
      <tr>
        <td><span class="triage-status s-trash">🗂 MANUAL TRASH</span></td>
        <td colspan="2"><strong>27 emails in Trash</strong> — see Trash Review</td>
        <td>Newsletters, spam, promotional emails, political content, adult spam — all in Trash. Includes 3 rescued items noted above.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ============================================================ -->
<!--  SECTION 1 — HEADER                                          -->
<!-- ============================================================ -->
<div class="header">
  <div>
    <div style="font-size:13px; color:#a8b8d8; margin-bottom:4px;">EXECUTIVE BRIEFING</div>
    <h1>Good morning, Melissa ☀️</h1>
    <div class="subtitle">Wednesday, August 12, 2026</div>
    <span class="badge">⚡ Daily Intelligence Brief</span>
  </div>
  <div class="meta">
    <div class="stat">📧 <strong>50</strong> total emails reviewed</div>
    <div class="stat">📅 <strong>8</strong> calendar events reviewed</div>
    <div class="stat" style="margin-top:8px; color:#e94560; font-weight:700;">⚠️ Action items waiting</div>
  </div>
</div>

<!-- ============================================================ -->
<!--  SECTION 2 — EXECUTIVE SUMMARY                               -->
<!-- ============================================================ -->
<div class="section">
  <div class="section-title red">🎯 Executive Summary</div>
  <div class="exec-summary">
    <div class="exec-bullet">
      <div class="exec-icon red">🔴</div>
      <div><strong>Security:</strong> 4 high-confidence phishing emails were auto-trashed before reaching your inbox (fake cloud storage threats, fake CashApp payment, spoofed payment block notice). Additionally, multiple unsolicited spam emails (adult content, casino, fake health products) remain outside inbox but were not auto-deleted — review recommended.</div>
    </div>
    <div class="exec-bullet">
      <div class="exec-icon green">💼</div>
      <div><strong>Job Search:</strong> Danaher HR responded to your Senior Director HRBP application — open immediately. SourceHire sent 3 duplicate messages for a confidential Sr Director of HR role (REQ93079) asking you to confirm work authorization. The LinkedIn alert for Head of People Operations at Ladders is also worth reviewing. Your HR Networking Group meets today at noon.</div>
    </div>
    <div class="exec-bullet">
      <div class="exec-icon blue">📅</div>
      <div><strong>Calendar / Deadlines:</strong> You have a PT appointment at 9:30 AM this morning and an HR Networking Zoom at noon (RSVP still pending on one instance). Stella's medication autoship (Ursodiol + Denamarin) ships in ~5 days — verify address and quantities. Your prescription at Duane Reade is ready Saturday Aug 15.</div>
    </div>
  </div>
</div>

<!-- ============================================================ -->
<!--  SECTION 3 — ACTION REQUIRED                                 -->
<!-- ============================================================ -->
<div class="section">
  <div class="section-title yellow">⚡ Action Required</div>

  <div class="card red">
    <div class="card-label red">🔴 URGENT — JOB SEARCH</div>
    <div class="card-title">Danaher HR: Application Status Update — Sr Director HRBP</div>
    <div class="card-source">From: Danaher HR via Workday &lt;danaher@myworkday.com&gt; | Received: 7:04 AM</div>
    <div class="card-body">Danaher sent an application status update for the Senior Director, Human Resources Business Partner role. This could be an advance, a request for additional info, or a rejection notice. Open immediately and respond if action is required.</div>
    <div><span class="card-action red">👉 Open email now — respond today</span></div>
    <div class="card-due">⏰ Due: Today, August 12, 2026</div>
  </div>

  <div class="card yellow">
    <div class="card-label yellow">🟡 ACTION — JOB SEARCH</div>
    <div class="card-title">SourceHire: Confirm Work Authorization — Sr Director HR REQ93079 (3 duplicates)</div>
    <div class="card-source">From: SourceHire Jobs &lt;jobs@sourcehire.app&gt; | Received: 10:19 AM, 10:46 AM (×2)</div>
    <div class="card-body">Three duplicate messages from SourceHire on behalf of a confidential employer asking you to confirm your visa/work authorization status to keep your application for Sr Director of Human Resources (Full-time) REQ93079 moving. Respond to one, delete the duplicates.</div>
    <div><span class="card-action yellow">👉 Confirm work authorization — reply to one email</span></div>
    <div class="card-due">⏰ Due: Today to keep application active</div>
  </div>

  <div class="card yellow">
    <div class="card-label yellow">🟡 RSVP NEEDED</div>
    <div class="card-title">HR Networking &amp; Job Search Group — Zoom (TODAY 12:00–1:30 PM)</div>
    <div class="card-source">Google Calendar | Status: needsAction</div>
    <div class="card-body">The HR Networking &amp; Job Search Group Zoom 2 is TODAY at noon. Your RSVP status shows "needsAction." The meeting has 180+ attendees in your networking group. You also have a parallel "Network" block confirmed at the same time — you appear to be attending but the formal RSVP needs updating.</div>
    <div><span class="card-action yellow">👉 Confirm RSVP on calendar invite</span></div>
    <div class="card-due">⏰ TODAY at 12:00 PM EDT — Zoom link in calendar</div>
  </div>

  <div class="card green">
    <div class="card-label green">🟢 JOB OPPORTUNITY</div>
    <div class="card-title">LinkedIn Alert: Head of People Operations at Ladders</div>
    <div class="card-source">From: LinkedIn Job Alerts &lt;jobalerts-noreply@linkedin.com&gt; | Received: 3:05 AM</div>
    <div class="card-body">LinkedIn flagged a Head of People Operations role at Ladders with 1 school alum connection. Given Melissa's HR leadership background, this is worth reviewing and potentially applying today while it's fresh.</div>
    <div><span class="card-action green">👉 Review role, apply if aligned</span></div>
    <div class="card-due">⏰ Review today before more applicants submit</div>
  </div>

  <div class="card blue">
    <div class="card-label blue">🔵 MEDICAL — PICKUP</div>
    <div class="card-title">Duane Reade: Prescription Auto-Refill Ready — Pickup Saturday Aug 15</div>
    <div class="card-source">From: Duane Reade Pharmacy (Walgreens) &lt;donotreply@rxtx.walgreens.com&gt;</div>
    <div class="card-body">Your auto-refill prescription is being processed and will be ready for pickup Saturday, August 15, 2026. Walgreens/Duane Reade will send a confirmation when it's ready.</div>
    <div><span class="card-action blue">👉 Plan pickup for Saturday Aug 15</span></div>
    <div class="card-due">⏰ Saturday, August 15, 2026</div>
  </div>

  <div class="card blue">
    <div class="card-label blue">🔵 PET HEALTH — AUTOSHIP</div>
    <div class="card-title">Stella's Medications Shipping in ~5 Days (Ursodiol + Denamarin)</div>
    <div class="card-source">From: Center for Veterinary Care &lt;centerforveterinarycare@outbound.ourvet.com&gt; | Rescued from Trash</div>
    <div class="card-body">Two autoship reminders for Stella's medications: (1) Ursodiol Tablet and (2) Denamarin Chewable Tablets — both shipping in approximately 5 days (~Aug 17). Verify address and quantities are correct before shipment processes.</div>
    <div><span class="card-action blue">👉 Verify autoship details — confirm address & qty</span></div>
    <div class="card-due">⏰ Ships ~August 17 — verify before then</div>
  </div>

  <div class="card green">
    <div class="card-label green">🟢 LINKEDIN NETWORKING</div>
    <div class="card-title">George Bongiorno Accepted Your LinkedIn Connection</div>
    <div class="card-source">From: LinkedIn &lt;invitations@linkedin.com&gt; | Received: 5:05 AM</div>
    <div class="card-body">George Bongiorno accepted your LinkedIn invitation. Strike while the iron is hot — send a brief personalized message to establish the connection and explore any mutual professional interests.</div>
    <div><span class="card-action green">👉 Send a follow-up LinkedIn message to George</span></div>
    <div class="card-due">⏰ Today while connection is fresh</div>
  </div>

  <div class="card orange">
    <div class="card-label orange">📦 DELIVERIES TODAY</div>
    <div class="card-title">USPS Package Arriving Today by 9:00 PM + Amazon Jewelry Shipped</div>
    <div class="card-source">USPS Auto-Reply (rescued from Trash) + Amazon.com</div>
    <div class="card-body">
      <strong>USPS:</strong> Tracking #9200190349635740890939 — expected today by 9 PM.<br>
      <strong>Amazon:</strong> 1 jewelry item has shipped. Check for tracking number in the email.
    </div>
    <div><span class="card-action yellow">👉 Plan to be available for delivery or secure package</span></div>
    <div class="card-due">⏰ USPS: Tonight by 9:00 PM</div>
  </div>

</div>

<!-- ============================================================ -->
<!--  SECTION 4 — FULL 7-DAY CALENDAR                            -->
<!-- ============================================================ -->
<div class="section">
  <div class="section-title blue">📅 Full 7-Day Calendar</div>

  <!-- Wednesday August 12 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Wednesday, August 12, 2026 — TODAY</div>
    <div class="cal-event">
      <div style="display:flex; justify-content:space-between; flex-wrap:wrap; gap:8px;">
        <div>
          <div class="cal-event-time">9:30 AM – 10:30 AM</div>
          <div class="cal-event-title">Pt (Physical Therapy / Personal Training)</div>
          <div class="cal-event-meta">📍 No location listed | No attendees listed</div>
          <span class="cal-rsvp rsvp-confirmed">✅ Confirmed</span>
          <div class="cal-prep" style="display:block; margin-top:6px;">💡 Prep: Bring any notes for your therapist/trainer. Ends at 10:30 AM — you'll have 90 min before the noon Zoom.</div>
        </div>
      </div>
    </div>
    <div class="cal-event">
      <div style="display:flex; justify-content:space-between; flex-wrap:wrap; gap:8px;">
        <div>
          <div class="cal-event-time">12:00 PM – 1:30 PM</div>
          <div class="cal-event-title">HR Networking &amp; Job Search Group — Zoom 2</div>
          <div class="cal-event-meta">📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" style="color:#2563eb;">Zoom Link</a> | ~180+ attendees</div>
          <span class="cal-rsvp rsvp-needs">⚠️ RSVP Needed</span>
          <span class="cal-conflict" style="margin-left:6px;">⚠️ Overlaps with "Network" block (also 12–1:30)</span>
          <div class="cal-prep" style="display:block; margin-top:6px;">💡 Prep: Review HR Networking Team Guidelines before joining. These two entries (HR Networking &amp; "Network") appear to be the same event — confirm RSVP on the formal invite.</div>
        </div>
      </div>
    </div>
    <div class="cal-event">
      <div>
        <div class="cal-event-time">12:00 PM – 1:30 PM</div>
        <div class="cal-event-title">Network</div>
        <div class="cal-event-meta">📍 No location listed | No attendees listed</div>
        <span class="cal-rsvp rsvp-confirmed">✅ Confirmed</span>
        <span class="cal-conflict" style="margin-left:6px;">⚠️ Same time as HR Networking Zoom — likely same event</span>
        <div class="cal-prep" style="display:block; margin-top:6px;">💡 Note: This appears to be a personal reminder block for the same HR Networking Zoom session above.</div>
      </div>
    </div>
  </div>

  <!-- Thursday August 13 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Thursday, August 13, 2026</div>
    <div class="cal-event">
      <div>
        <div class="cal-event-time">9:00 AM – 10:30 AM</div>
        <div class="cal-event-title">Executive Roundtable</div>
        <div class="cal-event-meta">📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" style="color:#2563eb;">Zoom Link</a> (hosted by John Madigan) | Meeting ID: 207 786 667 | PW: 205454</div>
        <span class="cal-rsvp rsvp-declined">❌ Declined</span>
        <div class="cal-prep" style="display:block; margin-top:6px;">💡 Note: You have declined this meeting. If circumstances change, Zoom link is available. No prep needed unless you decide to rejoin.</div>
      </div>
    </div>
    <div class="cal-event">
      <div>
        <div class="cal-event-time">12:00 PM – 1:00 PM</div>
        <div class="cal-event-title">HR Networking &amp; Job Search: Open Office Hours — Zoom 2</div>
        <div class="cal-event-meta">📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" style="color:#2563eb;">Zoom Link</a> | ~180+ attendees | Note: No AI notetaking tools</div>
        <span class="cal-rsvp rsvp-needs">⚠️ RSVP Needed</span>
        <div class="cal-prep" style="display:block; margin-top:6px;">💡 Prep: Open discussion format — no recording. Come prepared with questions about your job search, connections, or strategy. Disable AI notetaking tools per organizer request.</div>
      </div>
    </div>
    <div class="cal-event">
      <div>
        <div class="cal-event-time">3:30 PM – 4:30 PM</div>
        <div class="cal-event-title">m&amp;M (Meeting with Monte Montoya)</div>
        <div class="cal-event-meta">📍 No location listed | Attendee: monte.montoya@gmail.com</div>
        <span class="cal-rsvp rsvp-accepted">✅ Accepted</span>
        <div class="cal-prep" style="display:block; margin-top:6px;">💡 Prep: Prepare any agenda items or discussion points for your meeting with Monte Montoya. Confirm the format (call, video, in-person) if not already set.</div>
      </div>
    </div>
  </div>

  <!-- Friday Aug 14 – Sunday Aug 17: No events -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Friday, August 14 – Sunday, August 17, 2026</div>
    <div class="cal-event">
      <div class="cal-event-meta" style="padding:4px 0;">No calendar events scheduled. Note: Prescription pickup at Duane Reade on Saturday Aug 15 (email reminder — not on calendar yet).</div>
    </div>
  </div>

  <!-- Tuesday August 18 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Tuesday, August 18, 2026</div>
    <div class="cal-event">
      <div>
        <div class="cal-event-time">10:00 AM – 11:00 AM</div>
        <div class="cal-event-title">Vet / Stella Vet Appointment</div>
        <div class="cal-event-meta">📍 No location listed | Two calendar entries for the same time — "Vet" and "Stella vet"</div>
        <span class="cal-rsvp rsvp-confirmed">✅ Confirmed (×2 entries)</span>
        <div class="cal-prep" style="display:block; margin-top:6px;">💡 Prep: Bring Stella's medication list (Ursodiol + Denamarin) and any health notes. Confirm vet address and whether this is a routine checkup or follow-up. The two calendar entries appear to be duplicates — consider merging them.</div>
      </div>
    </div>
  </div>

</div>

<!-- ============================================================ -->
<!--  SECTION 5 — JOB SEARCH & INTERVIEW PIPELINE                 -->
<!-- ============================================================ -->
<div class="section">
  <div class="section-title green">💼 Job Search &amp; Interview Pipeline</div>

  <table>
    <thead>
      <tr>
        <th>Fit</th>
        <th>Opportunity / Employer</th>
        <th>Source</th>
        <th>Status</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="fit-high">🔥 HIGH</span></td>
        <td><strong>Sr Director, Human Resources Business Partner — Danaher</strong></td>
        <td>Danaher HR / Workday</td>
        <td>Application Status Update received — check now</td>
        <td>Open email immediately. Respond same day.</td>
      </tr>
      <tr>
        <td><span class="fit-high">🔥 HIGH</span></td>
        <td><strong>Sr Director of Human Resources (Full-time) — Confidential (REQ93079)</strong></td>
        <td>SourceHire Jobs (×3 duplicate emails)</td>
        <td>Application active — work authorization confirmation requested</td>
        <td>Reply to ONE email confirming work authorization. Delete the 2 duplicates.</td>
      </tr>
      <tr>
        <td><span class="fit-high">🔥 HIGH</span></td>
        <td><strong>Head of People Operations — Ladders</strong></td>
        <td>LinkedIn Job Alerts</td>
        <td>New alert — 1 school alum connection</td>
        <td>Review JD, leverage alumni connection, apply today.</td>
      </tr>
      <tr>
        <td><span class="fit-med">⚡ MED</span></td>
        <td><strong>HR Networking &amp; Job Search Group — Zoom (TODAY noon)</strong></td>
        <td>Google Calendar</td>
        <td>RSVP pending — attending based on "Network" block</td>
        <td>Confirm RSVP. Prepare 30-sec intro and job target summary.</td>
      </tr>
      <tr>
        <td><span class="fit-med">⚡ MED</span></td>
        <td><strong>HR Networking Open Office Hours — Thu Aug 13 noon</strong></td>
        <td>Google Calendar</td>
        <td>RSVP pending</td>
        <td>RSVP and attend. Bring job search questions. Disable AI notetaking.</td>
      </tr>
      <tr>
        <td><span class="fit-med">⚡ MED</span></td>
        <td><strong>George Bongiorno — New LinkedIn Connection</strong></td>
        <td>LinkedIn</td>
        <td>Connection accepted today</td>
        <td>Send a personalized follow-up message. Explore mutual network.</td>
      </tr>
      <tr>
        <td><span class="fit-low">LOW</span></td>
        <td><strong>Executive Roundtable — John Madigan (Thu Aug 13 9 AM)</strong></td>
        <td>Google Calendar</td>
        <td>Declined</td>
        <td>No action needed unless you choose to rejoin.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ============================================================ -->
<!--  SECTION 6 — FULL EMAIL REVIEW BY CATEGORY                   -->
<!-- ============================================================ -->
<div class="section">
  <div class="section-title dark">📬 Full Email Review by Category</div>

  <!-- SECURITY / RISK -->
  <div class="card red" style="margin-bottom:14px;">
    <div class="card-label red">🔴 SECURITY / RISK — 7 emails</div>
    <div class="card-title">Phishing, Fraud &amp; Suspicious Senders</div>
    <div class="card-body">
      <p><strong>Auto-Trashed (4 emails — phishing, removed before inbox):</strong></p>
      <ul class="plain" style="margin:6px 0 12px 0;">
        <li><strong>"Cloud.Security"</strong> — "melissaw212 Your photos will be deleted tonight" — Fake cloud storage threat / credential harvest. <span class="phish-tag">AUTO-TRASHED</span></li>
        <li><strong>"Payment_Declined" (Unicode spoofed)</strong> — "melissaw212 Account Has been Blocked!" — Spoofed payment/cloud block with data deletion threat. <span class="phish-tag">AUTO-TRASHED</span></li>
        <li><strong>"💸CASHAPP💸" (gibberish domain)</strong> — "Please_CONFIRM 💲 #4146585786695" — Fake CashApp $13,963.99 payment lure. <span class="phish-tag">AUTO-TRASHED</span></li>
        <li><strong>"📣melissaw212" (gibberish domain)</strong> — "No Deposit Needed! Get 130 Free Spins" — Casino phishing lure. <span class="phish-tag">AUTO-TRASHED</span></li>
      </ul>
      <p><strong>Remaining in spam/non-inbox (3 emails — not auto-trashed, recommend manual trash):</strong></p>
      <ul class="plain" style="margin:6px 0;">
        <li><strong>Bio Health Insights</strong> — "SteelPower Is Helping Men Get Harder And Last Longer" — Explicit adult spam from gibberish domain. Not in inbox. Recommend delete.</li>
        <li><strong>"Sex Trick?!" (gibberish domain)</strong> — Adult/pornographic spam mentioning Mia Khalifa. Not in inbox. Recommend delete.</li>
        <li><strong>"Lung Clearing Method" (gibberish domain)</strong> — COPD/mucus fake medical spam. Recommend delete.</li>
      </ul>
    </div>
    <div><span class="card-action red">👉 Auto-trashed items: No further action. Remaining 3: Delete manually.</span></div>
  </div>

  <!-- JOB SEARCH -->
  <div class="card green" style="margin-bottom:14px;">
    <div class="card-label green">🟢 JOB SEARCH — 3 emails</div>
    <div class="card-title">Active Applications &amp; Job Alerts</div>
    <div class="card-body">
      <ul class="plain">
        <li><strong>Danaher HR (Workday)</strong> — Application Status Update for Sr Director HRBP. <strong>Read immediately.</strong></li>
        <li><strong>SourceHire Jobs (×3 duplicates)</strong> — Work authorization confirmation for Confidential REQ93079. Reply to one, delete duplicates. Counted as 1 unique action item / 3 emails.</li>
        <li><strong>LinkedIn Job Alerts</strong> — Head of People Operations at Ladders.</li>
      </ul>
    </div>
    <div><span class="card-action green">👉 Act on Danaher and SourceHire today. Review Ladders role.</span></div>
  </div>

  <!-- RECRUITERS / NETWORKING -->
  <div class="card green" style="margin-bottom:14px;">
    <div class="card-label green">🟢 RECRUITERS / NETWORKING — 1 email</div>
    <div class="card-title">LinkedIn Connections</div>
    <div class="card-body">
      <ul class="plain">
        <li><strong>George Bongiorno via LinkedIn</strong> — Accepted Melissa's connection invitation. Explore his network.</li>
      </ul>
    </div>
    <div><span class="card-action green">👉 Send a warm follow-up message to George today.</span></div>
  </div>

  <!-- MEDICAL / HEALTH -->
  <div class="card blue" style="margin-bottom:14px;">
    <div class="card-label blue">🔵 MEDICAL / HEALTH — 3 emails</div>
    <div class="card-title">Prescriptions &amp; Pet Health</div>
    <div class="card-body">
      <ul class="plain">
        <li><strong>Duane Reade Pharmacy (Walgreens)</strong> — Auto-refill prescription processing; pickup ready Sat Aug 15.</li>
        <li><strong>Center for Veterinary Care</strong> — Stella's Ursodiol Tablet autoship in ~5 days. <span class="rescued-tag">RESCUED FROM TRASH</span></li>
        <li><strong>Center for Veterinary Care</strong> — Stella's Denamarin Chewable Tablets autoship in ~5 days. <span class="rescued-tag">RESCUED FROM TRASH</span></li>
      </ul>
    </div>
    <div><span class="card-action blue">👉 Pickup Rx Sat Aug 15. Verify Stella's autoship address/qty before Aug 17.</span></div>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="card yellow" style="margin-bottom:14px;">
    <div class="card-label yellow">🟡 FINANCIAL / BILLING — 2 emails</div>
    <div class="card-title">Payments &amp; Credit Monitoring</div>
    <div class="card-body">
      <ul class="plain">
        <li><strong>Synchrony Bank / CareCredit</strong> — $250.00 payment posted on account ending in 7483. Confirm against your records.</li>
        <li><strong>Bank of America</strong> — Monthly credit monitoring summary: no new alerts. Informational.</li>
      </ul>
    </div>
    <div><span class="card-action yellow">👉 Confirm CareCredit payment in your records. BofA — no action needed.</span></div>
  </div>

  <!-- PERSONAL -->
  <div class="card purple" style="margin-bottom:14px;">
    <div class="card-label purple">💜 PERSONAL — 5 emails</div>
    <div class="card-title">Dating Apps &amp; Social</div>
    <div class="card-body">
      <ul class="plain">
        <li><strong>Match.com</strong> — Marc likes you (inbox)</li>
        <li><strong>Match.com</strong> — Max likes you (inbox)</li>
        <li><strong>Match.com</strong> — Tim viewed your profile, 66 yrs, Carle Place NY (inbox)</li>
        <li><strong>Match.com</strong> — Torres likes you (inbox)</li>
        <li><strong>OkCupid</strong> — Someone likes you (inbox)</li>
      </ul>
    </div>
    <div><span class="card-action purple">👉 Review at your leisure — no urgency.</span></div>
  </div>

  <!-- SHIPPING / ORDERS -->
  <div class="card orange" style="margin-bottom:14px;">
    <div class="card-label orange">📦 SHIPPING / ORDERS — 3 emails</div>
    <div class="card-title">Packages &amp; Order Updates</div>
    <div class="card-body">
      <ul class="plain">
        <li><strong>USPS Tracking</strong> — Package arriving today by 9 PM. Tracking #9200190349635740890939. <span class="rescued-tag">RESCUED FROM TRASH</span></li>
        <li><strong>Amazon.com</strong> — 1 jewelry item has shipped (inbox).</li>
        <li><strong>Old Navy</strong> — Order #1RHKTCJ shipped (inbox).</li>
      </ul>
    </div>
    <div><span class="card-action yellow">👉 Track USPS package for tonight. Check Amazon/Old Navy tracking.</span></div>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="card purple" style="margin-bottom:14px;">
    <div class="card-label purple">💜 PROFESSIONAL DEVELOPMENT — 1 email (in trash)</div>
    <div class="card-title">LinkedIn Newsletters</div>
    <div class="card-body">
      <ul class="plain">
        <li><strong>Disruptive HR via LinkedIn</strong> — "What changes when HR starts trusting leaders?" — Relevant HR thought leadership. Currently in Trash. Consider rescuing if you follow this newsletter.</li>
      </ul>
    </div>
    <div><span class="card-action purple">👉 Rescue from Trash if relevant, or let it go.</span></div>
  </div>

  <!-- NEWSLETTERS / SUBSCRIPTIONS -->
  <div class="card gray" style="margin-bottom:14px;">
    <div class="card-label gray">⚫ NEWSLETTERS / SUBSCRIPTIONS — 6 emails (in trash)</div>
    <div class="card-title">Newsletters &amp; News Digests — All in Trash</div>
    <div class="card-body">
      <ul class="plain">
        <li><strong>1% Better Newsletter</strong> — "Bluetooth Tracking, Luigi Mangione Jury, 3 Career Rules" — In trash. Career + news digest.</li>
        <li><strong>Dylan's Diary / Behind the Markets</strong> — "The Oil Story Nobody is Talking About" — In trash. Finance newsletter.</li>
        <li><strong>The Daily Skimm</strong> — "Sorry, your majesty" — In trash. News digest.</li>
        <li><strong>Jack Cocchiarella / Substack</strong> — "Trump Suffers HUMILIATING Defeat..." (2 emails — post + live notification) — In trash. Political commentary.</li>
        <li><strong>Ruben Hassid / Substack</strong> — "I hate agents." (2 duplicates) — In trash. AI/tech newsletter.</li>
        <li><strong>Alison Courses</strong> — "Create faster without losing your originality" — In trash. Learning platform.</li>
      </ul>
    </div>
    <div><span class="card-action gray">👉 All in Trash — delete or unsubscribe from low-value ones.</span></div>
  </div>

  <!-- PROMOTIONAL / RETAIL -->
  <div class="card gray" style="margin-bottom:14px;">
    <div class="card-label gray">⚫ PROMOTIONAL / RETAIL — 6 emails (in trash)</div>
    <div class="card-title">Retail &amp; Shopping Promotions — All in Trash</div>
    <div class="card-body">
      <ul class="plain">
        <li><strong>Kohl's</strong> — "Save 30% + Earn Kohl's Cash" — In trash.</li>
        <li><strong>SHEIN</strong> — "New Sportswear Arrivals" — In trash.</li>
        <li><strong>YesStyle.com</strong> — "50% OFF K-Beauty favorites" — In trash.</li>
        <li><strong>22 Words</strong> — "Amazon PLUS Walmart Deals" — In trash.</li>
        <li><strong>Chick-fil-A</strong> — Rewards offer (402 pts) — In trash.</li>
        <li><strong>Facebook</strong> — "Here's what's new from Vali and others" — In trash. Social notification.</li>
      </ul>
    </div>
    <div><span class="card-action gray">👉 All in Trash — safe to delete. Unsubscribe from unwanted lists.</span></div>
  </div>

  <!-- SPAM / HEALTH SCAMS (non-phishing, non-inbox) -->
  <div class="card gray" style="margin-bottom:14px;">
    <div class="card-label gray">⚫ SPAM / HEALTH SCAMS — 9 emails (not in inbox)</div>
    <div class="card-title">Unsolicited Health &amp; Weight Loss Spam</div>
    <div class="card-body">
      <ul class="plain">
        <li><strong>MEDVi GLP-1 (multiple senders)</strong> — Weight loss medication spam (×4 emails, gibberish domains): "Your transformation starts the moment you click this," "Why 100,000+ chose MEDVi," "Real results in weeks..." — Not in inbox.</li>
        <li><strong>GLP-1-by-DirectMeds (multiple senders)</strong> — "DirectMeds GLP-1 treatment helps you lose up to 40 lbs" (×3 emails) — Not in inbox.</li>
        <li><strong>Ozempic.by.DirectMeds</strong> — GLP-1 spam — Not in inbox.</li>
        <li><strong>Blood Sugar (gibberish domain)</strong> — "4 Himalayan ingredients reverse Type II Parasite" — Not in inbox.</li>
      </ul>
    </div>
    <div><span class="card-action gray">👉 All spam — delete/ignore. Do not click any links.</span></div>
  </div>

</div>

<!-- ============================================================ -->
<!--  SECTION 7 — TRASH REVIEW                                    -->
<!-- ============================================================ -->
<div class="section">
  <div class="section-title red">🗑 Trash Review</div>

  <div class="card red" style="margin-bottom:14px;">
    <div class="card-label red">✅ RESTORE IMMEDIATELY (Rescued — already actioned)</div>
    <div class="card-title">These 3 emails were rescued from Trash before this briefing</div>
    <div class="card-body">
      <table style="font-size:12px; margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Rescue Reason</th></tr></thead>
        <tbody>
          <tr><td>USPS Tracking</td><td>Expected Delivery Today by 9 PM — #9200190349635740890939</td><td>Legitimate shipping notification with tracking number</td></tr>
          <tr><td>Center for Veterinary Care</td><td>Autoship of Ursodiol Tablet for Stella — 5 days</td><td>Important pet medication autoship notice</td></tr>
          <tr><td>Center for Veterinary Care</td><td>Autoship of Denamarin Chewable Tablets for Stella — 5 days</td><td>Important pet medication autoship notice</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card yellow" style="margin-bottom:14px;">
    <div class="card-label yellow">🔍 REVIEW BEFORE DELETING (4 emails)</div>
    <div class="card-title">May have some value — quick review recommended</div>
    <div class="card-body">
      <table style="font-size:12px; margin-top:8px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Reason to Review</th></tr></thead>
        <tbody>
          <tr><td>Disruptive HR via LinkedIn</td><td>What changes when HR starts trusting leaders?</td><td>Relevant HR leadership content — could be useful during job search</td></tr>
          <tr><td>1% Better Newsletter</td><td>Bluetooth Tracking, Luigi Mangione Jury, 3 Career Rules for 2026</td><td>"3 Career Rules for 2026" may be relevant to job search</td></tr>
          <tr><td>Alison Courses</td><td>Create faster without losing your originality 🚀</td><td>AI/creativity course — potentially useful for professional development</td></tr>
          <tr><td>Chick-fil-A</td><td>A little thing…from us to you (402 pts)</td><td>Rewards offer — check if points expire soon</td></tr>
        </tbody>
      </table>
    </div>
    <div><span class="card-action yellow">👉 Quick scan — restore anything useful, delete the rest.</span></div>
  </div>

  <div class="card gray" style="margin-bottom:14px;">
    <div class="card-label gray">🗑
