<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing – Melissa Weiss – July 14, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header .subtitle { font-size: 14px; color: #a8b8d8; margin-top: 4px; }
  .header-meta { text-align: right; }
  .header-meta .date { font-size: 18px; font-weight: 600; color: #e2c97e; }
  .header-meta .stats { font-size: 13px; color: #a8b8d8; margin-top: 6px; }
  .header-meta .stats span { display: inline-block; background: rgba(255,255,255,0.1); border-radius: 20px; padding: 2px 10px; margin: 2px 3px; }

  /* SECTION */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; color: #1a1a2e; border-left: 4px solid #0f3460; padding-left: 12px; margin-bottom: 14px; text-transform: uppercase; letter-spacing: 0.5px; }

  /* EXEC SUMMARY */
  .exec-summary { background: #fff; border-radius: 12px; padding: 20px 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .exec-summary ul { list-style: none; padding: 0; }
  .exec-summary ul li { padding: 10px 0 10px 36px; border-bottom: 1px solid #f0f2f5; position: relative; font-size: 14px; }
  .exec-summary ul li:last-child { border-bottom: none; }
  .exec-bullet-icon { position: absolute; left: 0; top: 10px; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; color: #fff; }
  .bullet-red { background: #dc3545; }
  .bullet-green { background: #28a745; }
  .bullet-blue { background: #0066cc; }

  /* CARDS */
  .card-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 16px; }
  .card { border-radius: 12px; padding: 18px 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); background: #fff; border-top: 4px solid #ccc; }
  .card.red { border-top-color: #dc3545; background: #fff8f8; }
  .card.yellow { border-top-color: #ffc107; background: #fffdf0; }
  .card.blue { border-top-color: #0066cc; background: #f5f9ff; }
  .card.green { border-top-color: #28a745; background: #f5fff8; }
  .card.purple { border-top-color: #6f42c1; background: #faf5ff; }
  .card.gray { border-top-color: #6c757d; background: #f8f9fa; }
  .card-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
  .card.red .card-label { color: #dc3545; }
  .card.yellow .card-label { color: #b8860b; }
  .card.blue .card-label { color: #0066cc; }
  .card.green .card-label { color: #28a745; }
  .card.purple .card-label { color: #6f42c1; }
  .card.gray .card-label { color: #6c757d; }
  .card h3 { font-size: 14px; font-weight: 700; margin-bottom: 8px; color: #1a1a2e; }
  .card .meta { font-size: 12px; color: #666; margin-bottom: 6px; }
  .card .why { font-size: 13px; color: #333; margin-bottom: 8px; }
  .card .action { font-size: 12px; font-weight: 600; padding: 6px 10px; border-radius: 6px; display: inline-block; }
  .card.red .action { background: #fde8e8; color: #dc3545; }
  .card.yellow .action { background: #fff3cd; color: #856404; }
  .card.blue .action { background: #cfe2ff; color: #004499; }
  .card.green .action { background: #d1f2db; color: #155724; }
  .card.purple .action { background: #e8d5ff; color: #4b2580; }
  .card.gray .action { background: #e9ecef; color: #495057; }
  .card .due { font-size: 11px; color: #888; margin-top: 6px; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { background: #1a1a2e; color: #e2c97e; padding: 8px 16px; border-radius: 8px 8px 0 0; font-weight: 700; font-size: 13px; }
  .cal-day-header.today { background: #0f3460; }
  .cal-event-table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 0 0 8px 8px; overflow: hidden; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
  .cal-event-table th { background: #f0f2f5; font-size: 11px; font-weight: 700; text-transform: uppercase; padding: 8px 12px; color: #555; text-align: left; }
  .cal-event-table td { padding: 10px 12px; font-size: 13px; border-bottom: 1px solid #f0f2f5; vertical-align: top; }
  .cal-event-table tr:last-child td { border-bottom: none; }
  .status-confirmed { color: #28a745; font-weight: 600; }
  .status-needs { color: #ffc107; font-weight: 600; }
  .status-declined { color: #dc3545; font-weight: 600; }
  .status-accepted { color: #0066cc; font-weight: 600; }
  .conflict-badge { background: #fde8e8; color: #dc3545; font-size: 10px; font-weight: 700; padding: 2px 6px; border-radius: 10px; margin-left: 6px; }
  .prep-badge { background: #fff3cd; color: #856404; font-size: 10px; font-weight: 600; padding: 2px 6px; border-radius: 10px; }

  /* TABLES */
  .data-table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
  .data-table th { background: #1a1a2e; color: #fff; font-size: 12px; text-transform: uppercase; padding: 10px 14px; text-align: left; letter-spacing: 0.3px; }
  .data-table td { padding: 10px 14px; font-size: 13px; border-bottom: 1px solid #f0f2f5; vertical-align: top; }
  .data-table tr:last-child td { border-bottom: none; }
  .data-table tr:hover td { background: #f8f9ff; }

  /* BADGES */
  .badge { display: inline-block; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 12px; text-transform: uppercase; letter-spacing: 0.3px; }
  .badge-red { background: #fde8e8; color: #dc3545; }
  .badge-yellow { background: #fff3cd; color: #856404; }
  .badge-blue { background: #cfe2ff; color: #004499; }
  .badge-green { background: #d1f2db; color: #155724; }
  .badge-purple { background: #e8d5ff; color: #4b2580; }
  .badge-gray { background: #e9ecef; color: #495057; }
  .badge-orange { background: #ffe5cc; color: #b85c00; }
  .badge-high { background: #dc3545; color: #fff; }
  .badge-medium { background: #ffc107; color: #333; }
  .badge-low { background: #6c757d; color: #fff; }

  /* EMAIL CATEGORY BLOCKS */
  .email-cat-block { background: #fff; border-radius: 10px; padding: 16px 18px; margin-bottom: 12px; box-shadow: 0 1px 5px rgba(0,0,0,0.06); border-left: 5px solid #ccc; }
  .email-cat-block.red { border-left-color: #dc3545; }
  .email-cat-block.yellow { border-left-color: #ffc107; }
  .email-cat-block.blue { border-left-color: #0066cc; }
  .email-cat-block.green { border-left-color: #28a745; }
  .email-cat-block.purple { border-left-color: #6f42c1; }
  .email-cat-block.gray { border-left-color: #adb5bd; }
  .email-cat-block.orange { border-left-color: #fd7e14; }
  .email-cat-title { font-size: 13px; font-weight: 700; color: #1a1a2e; margin-bottom: 6px; display: flex; align-items: center; gap: 8px; }
  .email-cat-body { font-size: 12px; color: #444; }
  .email-list { list-style: none; padding: 0; margin: 6px 0; }
  .email-list li { padding: 3px 0; border-bottom: 1px dotted #eee; font-size: 12px; }
  .email-list li:last-child { border-bottom: none; }

  /* DASHBOARD */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 14px; }
  .dash-tile { background: #fff; border-radius: 10px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.06); text-align: center; }
  .dash-tile .tile-num { font-size: 36px; font-weight: 800; }
  .dash-tile .tile-label { font-size: 11px; color: #666; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px; }
  .dash-tile.red .tile-num { color: #dc3545; }
  .dash-tile.yellow .tile-num { color: #b8860b; }
  .dash-tile.green .tile-num { color: #28a745; }
  .dash-tile.blue .tile-num { color: #0066cc; }
  .dash-tile.purple .tile-num { color: #6f42c1; }
  .dash-tile.gray .tile-num { color: #6c757d; }
  .dash-tile.orange .tile-num { color: #fd7e14; }

  /* TOP 3 */
  .top3 { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; }
  .priority-card { border-radius: 12px; padding: 20px; color: #fff; position: relative; overflow: hidden; }
  .priority-card:nth-child(1) { background: linear-gradient(135deg, #dc3545, #c0392b); }
  .priority-card:nth-child(2) { background: linear-gradient(135deg, #28a745, #1a7a31); }
  .priority-card:nth-child(3) { background: linear-gradient(135deg, #0066cc, #004499); }
  .priority-num { font-size: 48px; font-weight: 900; opacity: 0.2; position: absolute; top: 8px; right: 16px; line-height: 1; }
  .priority-title { font-size: 16px; font-weight: 700; margin-bottom: 8px; }
  .priority-body { font-size: 13px; opacity: 0.9; }

  /* MISC */
  .alert-banner { background: #fde8e8; border: 1px solid #f5c6cb; border-radius: 8px; padding: 12px 16px; margin-bottom: 16px; color: #721c24; font-size: 13px; display: flex; align-items: flex-start; gap: 10px; }
  .alert-icon { font-size: 18px; flex-shrink: 0; }
  .note-box { background: #fffdf0; border: 1px solid #ffc107; border-radius: 8px; padding: 10px 14px; font-size: 12px; color: #555; margin-top: 10px; }
  .section-divider { height: 1px; background: #e0e4ea; margin: 28px 0; }
  .trash-group { margin-bottom: 16px; }
  .trash-group-title { font-size: 13px; font-weight: 700; padding: 6px 12px; border-radius: 6px; margin-bottom: 8px; display: inline-block; }
  .trash-restore { background: #d1f2db; color: #155724; }
  .trash-review { background: #fff3cd; color: #856404; }
  .trash-delete { background: #e9ecef; color: #495057; }
  .small { font-size: 11px; color: #888; }
  .link-style { color: #0066cc; font-size: 12px; word-break: break-all; }
  .total-row { background: #1a1a2e; color: #fff; font-weight: 700; }
  .total-row td { padding: 10px 14px; }
  .auto-trash-badge { background: #1a1a2e; color: #e2c97e; font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 10px; }
  @media (max-width: 600px) {
    .header { flex-direction: column; }
    .header-meta { text-align: left; }
    .card-grid { grid-template-columns: 1fr; }
  }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════════════════ -->
<!-- 1. HEADER -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<div class="header">
  <div>
    <div class="header h1" style="font-size:28px;font-weight:700;letter-spacing:-0.5px;color:#fff;">Good morning, Melissa 👋</div>
    <div class="subtitle">Executive Intelligence Briefing — Prepared by Your Chief of Staff</div>
  </div>
  <div class="header-meta">
    <div class="date">Tuesday, July 14, 2026</div>
    <div class="stats">
      <span>📧 50 Emails Reviewed</span>
      <span>📅 12 Calendar Events</span>
      <span>🗑️ 8 Trash Items</span>
      <span>⚠️ 4 Auto-Trashed (Phishing)</span>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════ -->
<!-- 2. EXECUTIVE SUMMARY -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">Executive Summary</div>
  <div class="exec-summary">
    <ul>
      <li>
        <span class="exec-bullet-icon bullet-red">⚠</span>
        <strong>Biggest Risk:</strong> Multiple phishing and spam attacks targeting your account today — 4 emails were auto-trashed as high-confidence phishing (fake casino spins, account closure threats, spoofed Gmail support). Additional explicit/sexual spam reached your inbox. Several scam emails also remain in your regular folders. No action required on auto-trashed items; manual cleanup recommended for the rest.
      </li>
      <li>
        <span class="exec-bullet-icon bullet-green">💼</span>
        <strong>Biggest Opportunity:</strong> Two strong LinkedIn job alerts arrived today — <em>Head of People Operations at The Patrick J. McGovern Foundation (up to $150K)</em> and <em>Senior People Partner, GTM at Rokt (up to $235K)</em>. Both are unread and in your inbox. Review and apply promptly. Also, an unread LinkedIn message from Rana Saini awaits your response.
      </li>
      <li>
        <span class="exec-bullet-icon bullet-blue">📅</span>
        <strong>Biggest Calendar Item:</strong> Tomorrow (Wed 7/15) is back-to-back: Bone Density / LH Radiology imaging at 8:30 AM at 400 East 66th St, then HR Networking & Job Search Group at noon via Zoom — RSVP still pending (needsAction). Confirm your attendance today.
      </li>
    </ul>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════ -->
<!-- 3. ACTION REQUIRED -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">⚡ Action Required</div>
  <div class="card-grid">

    <div class="card yellow">
      <div class="card-label">📅 RSVP Needed</div>
      <h3>HR Networking & Job Search Group — Zoom</h3>
      <div class="meta">Source: Google Calendar | Wed, Jul 15 · 12:00–1:30 PM</div>
      <div class="why">Status is "needsAction" — you have not confirmed attendance. Large group meeting with 180+ attendees. Your "Network" event at the same time is confirmed, suggesting you plan to attend, but the main invite is unconfirmed.</div>
      <span class="action">✅ Accept or Decline the invite today</span>
      <div class="due">Due: Today, July 14</div>
    </div>

    <div class="card yellow">
      <div class="card-label">📅 RSVP Needed</div>
      <h3>HR Networking & Job Search: Open Office Hours — Zoom</h3>
      <div class="meta">Source: Google Calendar | Thu, Jul 16 · 12:00–1:00 PM</div>
      <div class="why">Status is "needsAction" — you have not confirmed attendance for Thursday's Open Office Hours session. Note: AI notetaking tools are prohibited per event description.</div>
      <span class="action">✅ Accept or Decline the invite today</span>
      <div class="due">Due: Today, July 14</div>
    </div>

    <div class="card green">
      <div class="card-label">💼 Job Opportunity</div>
      <h3>Head of People Operations — The Patrick J. McGovern Foundation</h3>
      <div class="meta">Source: LinkedIn Job Alerts | Up to $150K/year</div>
      <div class="why">Unread LinkedIn job alert in your inbox. Mission-driven foundation role aligned with your HR/People Ops background. Posted 7/12/2026.</div>
      <span class="action">🔍 Review & Apply</span>
      <div class="due">Act promptly — posted 7/12</div>
    </div>

    <div class="card green">
      <div class="card-label">💼 Job Opportunity</div>
      <h3>Senior People Partner, GTM — Rokt</h3>
      <div class="meta">Source: LinkedIn Job Alerts | Up to $235K/year</div>
      <div class="why">Unread LinkedIn job alert in your inbox. High-compensation GTM People Partner role. Posted 7/12/2026. Time-sensitive.</div>
      <span class="action">🔍 Review & Apply</span>
      <div class="due">Act promptly — posted 7/12</div>
    </div>

    <div class="card green">
      <div class="card-label">💬 LinkedIn Message</div>
      <h3>Rana Saini messaged you on LinkedIn</h3>
      <div class="meta">Source: LinkedIn messaging-digest | Tue, Jul 14 · 6:01 AM</div>
      <div class="why">1 new message awaiting your response. Could be a recruiter or networking contact. Email was read — check LinkedIn directly to see the full message and respond.</div>
      <span class="action">💬 Reply on LinkedIn</span>
      <div class="due">Today, July 14</div>
    </div>

    <div class="card yellow">
      <div class="card-label">📦 Package Arriving</div>
      <h3>USPS: 1 Inbound Package Arriving Soon</h3>
      <div class="meta">Source: USPS Informed Delivery | Tue, Jul 14</div>
      <div class="why">USPS Informed Delivery confirms 0 mail pieces and 1 inbound package arriving today or soon. Also, a separate Temu order (#PO-211-14414952059511025) has been transferred to GOFO for delivery and is in transit.</div>
      <span class="action">📦 Track both shipments</span>
      <div class="due">Today / This week</div>
    </div>

    <div class="card yellow">
      <div class="card-label">💊 Prescription</div>
      <h3>Duane Reade / Walgreens: Auto Refill Processing</h3>
      <div class="meta">Source: Duane Reade (Walgreens) | Tue, Jul 14 · 8:43 AM</div>
      <div class="why">Your auto refill order is being processed. Confirm the medication, pickup date, and location are correct. Unread and in your inbox.</div>
      <span class="action">💊 Review prescription details</span>
      <div class="due">Today, July 14</div>
    </div>

    <div class="card blue">
      <div class="card-label">🏥 Medical Prep</div>
      <h3>IMAGING APPOINTMENT — LH Radiology, 400 E 66th St</h3>
      <div class="meta">Source: Google Calendar | Wed, Jul 15 · 8:30 AM (Check-in)</div>
      <div class="why">Imaging appointment tomorrow. Complete pre-registration forms and update personal information before arrival to reduce check-in time. Also note: bone density event at same time — likely the same appointment with two calendar entries.</div>
      <span class="action">📋 Complete pre-registration forms tonight</span>
      <div class="due">Tonight / Before 8:30 AM tomorrow</div>
    </div>

    <div class="card blue">
      <div class="card-label">🩸 Lab Appointment Prep</div>
      <h3>Quest Diagnostics Appointment — Confirmation #FOUGZX</h3>
      <div class="meta">Source: Google Calendar | Thu, Jul 17 · 10:10–10:25 AM · 65 E 76th St</div>
      <div class="why">Lab appointment Thursday morning. Short window (15 min). Confirm fasting requirements or special instructions for "All Other Tests." Bring confirmation number FOUGZX.</div>
      <span class="action">🧪 Confirm prep instructions & fasting requirements</span>
      <div class="due">Before Thu, July 17</div>
    </div>

    <div class="card green">
      <div class="card-label">💼 Job Recommendations</div>
      <h3>Inclusively: Recommended Jobs — Check Your Profile</h3>
      <div class="meta">Source: Inclusively | Tue, Jul 14 · 8:33 AM</div>
      <div class="why">Unread job recommendation email in your inbox based on your profile. Review for any relevant People Ops / HR leadership roles.</div>
      <span class="action">🔍 Review job matches on Inclusively</span>
      <div class="due">Today or this week</div>
    </div>

    <div class="card red">
      <div class="card-label">🚨 Security Cleanup</div>
      <h3>Explicit Spam Emails Still in Folders — Manual Deletion Needed</h3>
      <div class="meta">Source: Gmail | Multiple senders</div>
      <div class="why">Two explicit/sexual spam emails ("FUCK-BUDDY SECRET" and "Squirt Like This") were NOT auto-trashed and remain in your folders. These should be manually deleted and the senders blocked. Additionally, a fake "payment declined" phishing email is already in Trash.</div>
      <span class="action">🗑️ Delete & block these senders now</span>
      <div class="due">Today, July 14</div>
    </div>

    <div class="card yellow">
      <div class="card-label">💳 New API Tool</div>
      <h3>Apify: New Crunchbase Company API Available</h3>
      <div class="meta">Source: Apify Community | Tue, Jul 14 · 11:44 AM</div>
      <div class="why">Unread, in your inbox. You previously used Apify Actors. New Crunchbase Company API (funding, investors, firmographics as JSON) from community developer John — potentially useful for research or job search intelligence.</div>
      <span class="action">🔧 Review if relevant to current projects</span>
      <div class="due">Low urgency — this week</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════ -->
<!-- 4. FULL 7-DAY CALENDAR -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📅 Full 7-Day Calendar (July 14–20, 2026)</div>

  <!-- TUESDAY JULY 14 -->
  <div class="cal-day">
    <div class="cal-day-header today">📍 TODAY — Tuesday, July 14, 2026</div>
    <table class="cal-event-table">
      <tr><th>Time</th><th>Event</th><th>Status</th><th>Location / Link</th><th>Prep / Notes</th></tr>
      <tr>
        <td><strong>10:00–11:00 AM</strong></td>
        <td><strong>Stella</strong></td>
        <td><span class="status-confirmed">✅ Confirmed</span></td>
        <td><em>No location listed</em></td>
        <td><span class="prep-badge">📋 No details — confirm what this is (appointment? call?)</span></td>
      </tr>
    </table>
  </div>

  <!-- WEDNESDAY JULY 15 -->
  <div class="cal-day">
    <div class="cal-day-header">Wednesday, July 15, 2026</div>
    <table class="cal-event-table">
      <tr><th>Time</th><th>Event</th><th>Status</th><th>Location / Link</th><th>Prep / Notes</th></tr>
      <tr>
        <td><strong>8:30–9:30 AM</strong></td>
        <td><strong>Bone Density</strong> <span class="conflict-badge">⚠ Overlaps with Imaging</span></td>
        <td><span class="status-confirmed">✅ Confirmed</span></td>
        <td><em>No location listed</em></td>
        <td><span class="prep-badge">🏥 Likely same appointment as LH Radiology imaging below — verify</span></td>
      </tr>
      <tr>
        <td><strong>8:30–9:05 AM</strong></td>
        <td><strong>IMAGING APPOINTMENT: LH Radiology</strong> <span class="conflict-badge">⚠ Overlaps with Bone Density</span></td>
        <td><span class="status-confirmed">✅ Confirmed</span></td>
        <td>400 East 66th Street</td>
        <td><span class="prep-badge">📋 Complete pre-registration forms tonight. Bring ID/insurance. Check-in 8:30 AM sharp.</span></td>
      </tr>
      <tr>
        <td><strong>12:00–1:30 PM</strong></td>
        <td><strong>HR Networking & Job Search Group — Zoom 2</strong></td>
        <td><span class="status-needs">⚠ RSVP Pending</span></td>
        <td><a class="link-style" href="https://us06web.zoom.us/j/81954171722">Zoom Link</a></td>
        <td><span class="prep-badge">✅ Accept invite. Review team guidelines before joining. 180+ attendees.</span></td>
      </tr>
      <tr>
        <td><strong>12:00–1:30 PM</strong></td>
        <td><strong>Network</strong> <span class="conflict-badge">⚠ Same time as HR Networking Zoom</span></td>
        <td><span class="status-confirmed">✅ Confirmed</span></td>
        <td><em>No location listed</em></td>
        <td><span class="small">Likely duplicate/companion entry to the HR Networking Zoom above.</span></td>
      </tr>
    </table>
  </div>

  <!-- THURSDAY JULY 16 -->
  <div class="cal-day">
    <div class="cal-day-header">Thursday, July 16, 2026</div>
    <table class="cal-event-table">
      <tr><th>Time</th><th>Event</th><th>Status</th><th>Location / Link</th><th>Prep / Notes</th></tr>
      <tr>
        <td><strong>9:00–10:30 AM</strong></td>
        <td><strong>Executive Roundtable</strong> (John Madigan)</td>
        <td><span class="status-declined">❌ Declined</span></td>
        <td><a class="link-style" href="https://us02web.zoom.us/j/207786667">Zoom: 207 786 667 · PW: 205454</a></td>
        <td><span class="small">You have declined. No action needed unless you wish to reconsider.</span></td>
      </tr>
      <tr>
        <td><strong>12:00–1:00 PM</strong></td>
        <td><strong>HR Networking & Job Search: Open Office Hours — Zoom 2</strong></td>
        <td><span class="status-needs">⚠ RSVP Pending</span></td>
        <td><a class="link-style" href="https://us06web.zoom.us/j/85945371140">Zoom Link</a></td>
        <td><span class="prep-badge">⚠ No AI notetaking tools permitted. Accept or decline today.</span></td>
      </tr>
      <tr>
        <td><strong>1:00–2:00 PM</strong></td>
        <td><strong>Tea with LeiLani | Brew At the Table</strong></td>
        <td><span class="status-accepted">✅ Accepted</span></td>
        <td>T Shop, 247 Elizabeth St, New York, NY 10012</td>
        <td><span class="prep-badge">☕ In-person. Attendees: leilani@bethechangehr.com, tlow@teresalowconsulting.com, leylasnovini@gmail.com, jessi@alvisolutions.com. Networking/social.</span></td>
      </tr>
    </table>
  </div>

  <!-- FRIDAY JULY 17 -->
  <div class="cal-day">
    <div class="cal-day-header">Friday, July 17, 2026</div>
    <table class="cal-event-table">
      <tr><th>Time</th><th>Event</th><th>Status</th><th>Location / Link</th><th>Prep / Notes</th></tr>
      <tr>
        <td><strong>10:10–10:25 AM</strong></td>
        <td><strong>Quest Diagnostics Appointment</strong> — Conf. #FOUGZX</td>
        <td><span class="status-confirmed">✅ Confirmed</span></td>
        <td>65 E 76th St, Ground Level-G, NY 10021</td>
        <td><span class="prep-badge">🧪 15-min window. Confirm fasting/prep requirements. Bring confirmation number FOUGZX.</span></td>
      </tr>
      <tr>
        <td><strong>3:00–4:00 PM</strong></td>
        <td><strong>Dr. Yuen</strong></td>
        <td><span class="status-confirmed">✅ Confirmed</span></td>
        <td><em>No location listed</em></td>
        <td><span class="prep-badge">🩺 No details — confirm office location and any pre-visit requirements.</span></td>
      </tr>
    </table>
  </div>

  <!-- SATURDAY JULY 18 -->
  <div class="cal-day">
    <div class="cal-day-header">Saturday, July 18, 2026</div>
    <table class="cal-event-table">
      <tr><th>Time</th><th>Event</th><th>Status</th><th>Location / Link</th><th>Prep / Notes</th></tr>
      <tr>
        <td colspan="5" style="color:#999;font-style:italic;padding:12px;">No events scheduled.</td>
      </tr>
    </table>
  </div>

  <!-- SUNDAY JULY 19 -->
  <div class="cal-day">
    <div class="cal-day-header">Sunday, July 19, 2026</div>
    <table class="cal-event-table">
      <tr><th>Time</th><th>Event</th><th>Status</th><th>Location / Link</th><th>Prep / Notes</th></tr>
      <tr>
        <td colspan="5" style="color:#999;font-style:italic;padding:12px;">No events scheduled.</td>
      </tr>
    </table>
  </div>

  <!-- MONDAY JULY 20 -->
  <div class="cal-day">
    <div class="cal-day-header">Monday, July 20, 2026</div>
    <table class="cal-event-table">
      <tr><th>Time</th><th>Event</th><th>Status</th><th>Location / Link</th><th>Prep / Notes</th></tr>
      <tr>
        <td><strong>1:45–2:45 PM</strong></td>
        <td><strong>PT</strong> (Physical Therapy) — Entry 1</td>
        <td><span class="status-confirmed">✅ Confirmed</span></td>
        <td><em>No location listed</em></td>
        <td><span class="prep-badge">🏋️ Duplicate calendar entry — appears twice. Confirm location and bring relevant paperwork.</span></td>
      </tr>
      <tr>
        <td><strong>1:45–2:45 PM</strong></td>
        <td><strong>PT</strong> (Physical Therapy) — Entry 2 <span class="conflict-badge">⚠ Duplicate</span></td>
        <td><span class="status-confirmed">✅ Confirmed</span></td>
        <td><em>No location listed</em></td>
        <td><span class="small">Exact duplicate of above — consider deleting one entry from Calendar.</span></td>
      </tr>
    </table>
  </div>

  <div class="note-box">⚠️ <strong>Calendar Conflicts & Flags:</strong> (1) Wed 7/15: "Bone Density" and "LH Radiology Imaging" are at the exact same time — likely the same appointment, confirm. (2) Wed 7/15: "Network" personal entry overlaps with the HR Networking Zoom. (3) Mon 7/20: "PT" appears twice — likely a duplicate entry to delete. (4) Thu 7/16: Executive Roundtable (9 AM) and Tea with LeiLani (1 PM) — you've already declined the Roundtable; Tea is confirmed.</div>
</div>

<!-- ═══════════════════════════════════════════════════════════════ -->
<!-- 5. JOB SEARCH & INTERVIEW PIPELINE -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">💼 Job Search & Interview Pipeline</div>
  <table class="data-table">
    <tr>
      <th>Fit</th>
      <th>Role / Opportunity</th>
      <th>Source</th>
      <th>Salary</th>
      <th>Status</th>
      <th>Next Step</th>
    </tr>
    <tr>
      <td><span class="badge badge-high">HIGH</span></td>
      <td><strong>Senior People Partner, GTM — Rokt</strong></td>
      <td>LinkedIn Job Alert</td>
      <td>Up to $235K</td>
      <td><span class="badge badge-yellow">Unread / Inbox</span></td>
      <td>Review & Apply immediately</td>
    </tr>
    <tr>
      <td><span class="badge badge-high">HIGH</span></td>
      <td><strong>Head of People Operations — The Patrick J. McGovern Foundation</strong></td>
      <td>LinkedIn Job Alert</td>
      <td>Up to $150K</td>
      <td><span class="badge badge-yellow">Unread / Inbox</span></td>
      <td>Review & Apply immediately</td>
    </tr>
    <tr>
      <td><span class="badge badge-medium">MED</span></td>
      <td><strong>Fireworks AI — AI Field Engineer</strong> (David Joseph & Co., Manhattan)</td>
      <td>PostJobFree / Dennis Gorelik</td>
      <td>Series C $4B valuation</td>
      <td><span class="badge badge-gray">In Trash</span></td>
      <td>Restore from Trash if interested; review role fit</td>
    </tr>
    <tr>
      <td><span class="badge badge-medium">MED</span></td>
      <td><strong>Job recommendations (multiple roles)</strong></td>
      <td>Inclusively</td>
      <td>Varies</td>
      <td><span class="badge badge-yellow">Unread / Inbox</span></td>
      <td>Review recommended jobs on Inclusively</td>
    </tr>
    <tr>
      <td><span class="badge badge-medium">MED</span></td>
      <td><strong>Hired! members spotlight</strong> (salary benchmarking)</td>
      <td>Ladders (×2 emails)</td>
      <td>Benchmarking</td>
      <td><span class="badge badge-gray">Read / Not Inbox</span></td>
      <td>Review for market intel; one unread</td>
    </tr>
    <tr>
      <td><span class="badge badge-low">LOW</span></td>
      <td><strong>What's Actually Standing Between You and VP?</strong></td>
      <td>Ariana Ruiz via LinkedIn Newsletter</td>
      <td>—</td>
      <td><span class="badge badge-gray">Read / Not Inbox</span></td>
      <td>Read if relevant to career strategy</td>
    </tr>
    <tr>
      <td style="font-style:italic;color:#666;" colspan="6">Networking / Events</td>
    </tr>
    <tr>
      <td><span class="badge badge-high">HIGH</span></td>
      <td><strong>HR Networking & Job Search Group — Zoom</strong></td>
      <td>Google Calendar</td>
      <td>—</td>
      <td><span class="badge badge-yellow">RSVP Pending (Wed 7/15)</span></td>
      <td>Accept today; review team guidelines</td>
    </tr>
    <tr>
      <td><span class="badge badge-high">HIGH</span></td>
      <td><strong>Tea with LeiLani — T Shop, Elizabeth St</strong></td>
      <td>Google Calendar</td>
      <td>—</td>
      <td><span class="badge badge-green">Accepted (Thu 7/16)</span></td>
      <td>In-person networking; prepare talking points</td>
    </tr>
    <tr>
      <td><span class="badge badge-medium">MED</span></td>
      <td><strong>Open Office Hours — HR Networking Zoom</strong></td>
      <td>Google Calendar</td>
      <td>—</td>
      <td><span class="badge badge-yellow">RSVP Pending (Thu 7/16)</span></td>
      <td>Accept or decline today</td>
    </tr>
    <tr>
      <td><span class="badge badge-medium">MED</span></td>
      <td><strong>LinkedIn message from Rana Saini</strong></td>
      <td>LinkedIn</td>
      <td>—</td>
      <td><span class="badge badge-gray">Read / Not Inbox</span></td>
      <td>Check LinkedIn and respond</td>
    </tr>
  </table>
  <div class="note-box">💡 <strong>Bank of America Alert:</strong> A direct deposit of <strong>$760.38</strong> from NYS DOL UI DD was credited to your account today (Account ending 7471). This appears to be an unemployment insurance payment — FYI for your financial tracking.</div>
</div>

<!-- ═══════════════════════════════════════════════════════════════ -->
<!-- 6. FULL EMAIL REVIEW BY CATEGORY -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">📧 Full Email Review by Category</div>

  <!-- SECURITY / RISK -->
  <div class="email-cat-block red">
    <div class="email-cat-title">🚨 Security / Risk <span class="badge badge-red">10 Emails</span></div>
    <div class="email-cat-body">
      <p><strong>Auto-Trashed (Phishing — No Action Required):</strong></p>
      <ul class="email-list">
        <li><span class="auto-trash-badge">AUTO-TRASHED</span> <strong>"Congratulations🎉"</strong> (z4rzv6.gg2fyv domain) — "200 Free Spins 💰 Pending in your Account" — Fake casino spam/phishing from gibberish domain</li>
        <li><span class="auto-trash-badge">AUTO-TRASHED</span> <strong>"Congratulations🎉"</strong> (ipxf08.5qompr domain) — "200 Free Spins 💰 Pending in your Account" — Duplicate fake casino spam/phishing</li>
        <li><span class="auto-trash-badge">AUTO-TRASHED</span> <strong>"📣melissaw212"</strong> (ybpp.hqnfjkrjothzq.us) — "No Deposit Needed!🔥 Get 130 Free Spins..." — Spoofed sender impersonating your username; credential harvesting</li>
        <li><span class="auto-trash-badge">AUTO-TRASHED</span> <strong>"GmailSupportTeam"</strong> (ybr4ek.lras9x domain) — "melissaw212, Your account will be closed within 48 hours..." — Spoofed Gmail threat; classic credential-harvesting urgency scam</li>
      </ul>
      <p style="margin-top:8px;"><strong>Remaining in Folders — Manual Action Needed:</strong></p>
      <ul class="email-list">
        <li><strong>"🔶FUCK-BUDDY SECRET🔶"</strong> (info@ebx.qccnshttaknmq.us) — Explicit sexual spam — <strong>Delete & block immediately</strong></li>
        <li><strong>"Squirt Like This"</strong> (nlnuirqvgnrecmtlsuecpduyyr.net) — Explicit sexual spam — <strong>Delete & block immediately</strong></li>
        <li><strong>"'Payment_Declined©'"</strong> (sendgrid.net.shallowerful.org) — In Trash — "We've Blocked Your Account! Photos/videos will be deleted Tue 7/14" — Phishing; already in Trash — <strong>Permanently delete</strong></li>
        <li><strong>"'OnlineCasino📣'"</strong> (zo0n8v.0aoguk.qblf83.us) — In Trash — "No deposit Needed 🔥 130 Free Spins..." — Casino phishing; already in Trash — <strong>Permanently delete</strong></li>
        <li><strong>Notify NYC</strong> (noreply@everbridge.net) — "Update: Risk of Rip Currents 7/14–7/15 (NYC)" — Official NYC alert. Life-threatening rip currents at NYC beaches 7/14–7/15. <strong>Do not swim in surf zones this week.</strong></li>
      </ul>
      <p style="margin-top:8px;"><em>Note: The Notify NYC rip current warning is a legitimate public safety alert, not a threat, included here for urgent awareness.</em></p>
    </div>
  </div>

  <!-- JOB SEARCH -->
  <div class="email-cat-block green">
    <div class="email-cat-title">💼 Job Search <span class="badge badge-green">5 Emails</span></div>
    <div class="email-cat-body">
      <ul class="email-list">
        <li><strong>LinkedIn Job Alerts</strong> — "Head of People Operations at The Patrick J. McGovern Foundation: up to $150K/year" — <strong>UNREAD / INBOX</strong> — Review & Apply</li>
        <li><strong>LinkedIn Job Alerts</strong> — "Senior People Partner, GTM at Rokt: up to $235K/year" — <strong>UNREAD / INBOX</strong> — Review & Apply</li>
        <li><strong>Inclusively</strong> — "melissa weiss - Check out these recommended jobs for you!" — <strong>UNREAD / INBOX</strong> — Review matches</li>
        <li><strong>Ladders</strong> (×2 emails, near-identical) — "Hired!" member spotlight + salary data — One unread, one read — Review for market benchmarking; possible duplicate send</li>
      </ul>
      <strong>Recommendation:</strong> Prioritize the two LinkedIn alerts and apply today. Check Inclusively for additional matches.
    </div>
  </div>

  <!-- RECRUITERS / NETWORKING -->
  <div class="email-cat-block green">
    <div class="email-cat-title">🤝 Recruiters / Networking <span class="badge badge-green">3 Emails</span></div>
    <div class="email-cat-body">
      <ul class="email-list">
        <li><strong>Rana Saini via LinkedIn</strong> — "Rana just messaged you" — Read, not in inbox — <strong>Check LinkedIn and respond</strong></li>
        <li><strong>Ariana Ruiz via LinkedIn</strong> — "What's Actually Standing Between You and VP?" — LinkedIn newsletter — Read, not inbox — Review when time permits</li>
        <li><strong>Dennis Gorelik / PostJobFree</strong> — "Fireworks AI - AI Field Engineer (David Joseph & Co., Manhattan)" — <strong>In Trash</strong> — Consider restoring if AI/field engineering is of interest; Series C at $4B</li>
      </ul>
      <strong>Recommendation:</strong> Respond to Rana Saini on LinkedIn today. Review the VP article as career strategy content. Decide on Fireworks AI role.
    </div>
  </div>

  <!-- MEDICAL / HEALTH -->
  <div class="email-cat-block blue">
    <div class="email-cat-title">🏥 Medical / Health <span class="badge badge-blue">1 Email</span></div>
    <div class="email-cat-body">
      <ul class="email-list">
        <li><strong>Duane Reade / Walgreens</strong> (donotreply@rxorder.walgreens.com) — "We're Processing Your Auto Refill Order" — <strong>UNREAD / INBOX</strong> — Verify medication, pickup timing, and pharmacy location</li>
      </ul>
      <strong>Recommendation:</strong> Open and confirm the details of the auto refill order today.
    </div>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="email-cat-block yellow">
    <div class="email-cat-title">💰 Financial / Billing <span class="badge badge-yellow">3 Emails</span></div>
    <div class="email-cat-body">
      <ul class="email-list">
        <li><strong>Bank of America</strong> (onlinebanking@ealerts.bankofamerica.com) — "A direct deposit was credited to your account" — $760.38 from NYS DOL UI DD credited to account ending 7471 on July 14 — Read, not inbox — <strong>FYI / Track</strong></li>
        <li><strong>Bank of America</strong> (noreply@mail-mycredit.bankofamerica.com) — "My Credit: Review your monthly monitoring summary" — Monthly credit monitoring summary — Read, not inbox — Review when time permits</li>
        <li><strong>Robinhood</strong> (×2 emails) — "Your trade confirmations are available" + "Your account statements and changes to Customer Agreements are available" — Both read, not inbox — <strong>Review account statements and updated Customer Agreements</strong></li>
      </ul>
      <strong>Note:</strong> Robinhood has updated its Customer Agreements — review the changes before next trade.
    </div>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="email-cat-block purple">
    <div class="email-cat-title">📚 Professional Development <span class="badge badge-purple">3 Emails</span></div>
    <div class="email-cat-body">
      <ul class="email-list">
        <li><strong>AI For Leaders</strong> (team@aiforleaders.com) — "The Philosopher on AI's Payroll" — <strong>In Trash</strong> (unread) — Article on philosophy PhDs finding roles in AI — Consider restoring if relevant to AI leadership interests</li>
        <li><strong>BambooHR</strong> (email@news.bamboohr.com) — "[Free Survey] What Do Your New Hires Really Think?" — Unread, not inbox — HR onboarding tool/survey — Review if relevant to current consulting work</li>
        <li><strong>Apify Community</strong> (hello@community.apify.com) — "New: Crunchbase Company API" — <strong>UNREAD / INBOX</strong> — New tool from community developer; useful for research/intelligence work</li>
      </ul>
      <strong>Recommendation:</strong> Review Apify email (inbox). Consider restoring AI For Leaders from Trash. BambooHR is low priority.
    </div>
  </div>

  <!-- PERSONAL -->
  <div class="email-cat-block orange">
    <div class="email-cat-title">👤 Personal <span class="badge badge-orange">5 Emails</span></div>
    <div class="email-cat-body">
      <ul class="email-list">
        <li><strong>USPS Informed Delivery</strong> — "Your Daily Digest for Tue, 7/14 is ready" — <strong>UNREAD / INBOX</strong> — 0 mail pieces, 1 inbound package — Track your package</li>
        <li><strong>Temu</strong> (orders@transaction.temu.com) — "Your Temu order transferred to GOFO for delivery (#PO-211-14414952059511025)" — <strong>UNREAD / INBOX</strong> — Package cleared customs; track delivery</li>
        <li><strong>Carmel Limo / Carmel Car Service</strong> (noreply@carmellimousine.com) — "Carmel Limo Customer Care Discount" — <strong>UNREAD / INBOX</strong> — Customer discount offer; review if you use Carmel regularly</li>
        <li><strong>Match</strong> (mailer@connect.match.com) — "Tommy likes you. See if it's mutual." — Read, not inbox — Personal; check at your leisure</li>
        <li><strong>Match</strong> (mailer@connect.match.com) — "You've had a profile view from Craig (47, Staten Island)" — Read, not inbox — Personal; check at your leisure</li>
      </ul>
      <strong>Recommendation:</strong> Track USPS and Temu packages. Carmel discount may be worth reviewing if relevant.
    </div>
  </div>

  <!-- NEWSLETTERS / SUBSCRIPTIONS -->
  <div class="email-cat-block purple">
    <div class="email-cat-title">📰 Newsletters / Subscriptions <span class="badge badge-purple">9 Emails</span></div>
    <div class="email-cat-body">
      <ul class="email-list">
        <li><strong>The AI Report</strong> — "⚡ OpenAI, Meta, xAI slash pricing" + Nobel Laureates warn AI could outpace Industrial Revolution — Unread, not inbox</li>
        <li><strong>TLDR</strong> — "Siri AI beta 📱, Starlink v3 🛸, Apple's new speech API" — iOS 27 first public beta — Unread, not inbox</li>
        <li><strong>The Average Joe</strong> — "🌊 AI debt tsunami" — AI investment/debt coverage — Unread, not inbox</li>
        <li><strong>Medium Daily Digest</strong> — "Writing HTML For Documentation Instead of Markdown is a Game-Changer" — Read, not inbox (for Melissa)</li>
        <li><strong>Medium Daily Digest</strong> — "The interface has left the building | Om Prakash in UX Collective" — Read, not inbox (for Amylw)</li>
        <li><strong>Pranit naik via Medium</strong> — "The Biggest Bet in Human History or the Largest Bubble Ever Built?" — AI Bubble 2026 — Read, not inbox</li>
        <li><strong>The Daily Skimm</strong> — "A new kind of space jam" — Read, not inbox — General news digest</li>
        <li><strong>The Hustle</strong> — "🏆 Ranch wins" — <strong>In Trash</strong> — General interest newsletter — Safe to delete</li>
        <li><strong>1% Better</strong> — "Hollywood Showdown, $30M Dinosaur, and How to Explain Anything to Anyone" — Read, not inbox — Self-improvement newsletter</li>
      </ul>
      <strong>Recommendation:</strong> The AI Report and TLDR are high-value for your AI/leadership focus. Review when time permits. Medium second digest appears to be for a different user (Amylw) — possible account association to review.
    </div>
  </div>

  <!-- PROMOTIONAL / RETAIL -->
  <div class="email-cat-block gray">
    <div class="email-cat-title">🛍️ Promotional / Retail <span class="badge badge-gray">8 Emails</span></div>
    <div class="email-cat-body">
      <ul class="email-list">
        <li><strong>Carmel Car Service</strong> (specials@carmelcarservice.com) ×4 — "Nelson Mandela International Day!" — Same promotional email sent to 4 different name variants (Customer, raymond, melissa, Customer) — Promotional/discount codes — <strong>3 read, 1 unread — Ignore or unsubscribe</strong></li>
        <li><strong>Kohl's</strong> — "Save 30% — Time for a home refresh" + earn Kohl's Cash — Read, not inbox — Retail promo</li>
        <li><strong>SHEIN</strong> — "The Budget Boutique Is Open: Everything UNDER $5!" — Read, not inbox — Retail promo</li>
        <li><strong>YesStyle.com</strong> — "🚨 Anua x KPop Demon Hunters Week – Up to 60% OFF!" — Read, not inbox — Retail promo</li>
        <li><strong>Meidas+</strong> (meidastouch@substack.com) — "MeidasTouch Full Podcast - 7/14/26 [AD-FREE]" — Unread, not inbox — Subscription podcast; watch if interested</li>
      </ul>
      <strong>Recommendation:</strong> The Carmel Car Service emails are suspicious (4 copies to different names, suggesting a list/spam issue). Kohl's, SHEIN, YesStyle are standard retail. Meidas+ is a paid subscription you may want to watch.
    </div>
  </div>

  <!-- SAFE TO DELETE / IGNORE -->
  <div class="email-cat-block gray">
    <div class="email-cat-title">🗑️ Safe to Delete / Ignore <span class="badge badge-gray">3 Emails</span></div>
    <div class="email-cat-body">
      <ul class="email-list">
        <li><strong>CoolDeep AI</strong> (cooldeepai@mail.beehiiv.com) — "Cool AI skills which you should not miss" — In Trash — Generic AI clickbait newsletter — Delete</li>
        <li><strong>Lisa Rangel / Chameleon Resumes</strong> (lr@chameleonresumes.com) — "what is the real reason?" — In Trash — Sales email from resume service — Delete</li>
        <li><strong>Carmel Limo</strong> (noreply@carmellimousine.com) — "Carmel Limo Customer Care Discount" — Unread / Inbox — Promotional discount — Review, then delete if not needed (also listed under Personal above as it's in inbox)</li>
      </ul>
    </div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════════════════ -->
<!-- 7. TRASH REVIEW -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title">🗑️ Trash Review</div>

  <div class="trash-group">
    <span class="trash-group-title trash-restore">✅ Restore Immediately</span>
    <table class="data-table">
      <tr><th>Sender</th><th>Subject</th><th>Why Restore</th></tr>
      <tr>
        <td>AI For Leaders (team@aiforleaders.com)</td>
        <td>"The Philosopher on AI's Payroll
