<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa W — September 3, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; line-height: 1.5; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px 60px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a237e 0%, #283593 60%, #3949ab 100%); color: #fff; border-radius: 14px; padding: 32px 36px 28px; margin-bottom: 24px; box-shadow: 0 4px 18px rgba(26,35,126,0.18); }
  .header h1 { font-size: 2rem; font-weight: 700; letter-spacing: 0.5px; }
  .header .subtitle { font-size: 1.05rem; opacity: 0.88; margin-top: 6px; }
  .header .meta { display: flex; gap: 28px; margin-top: 16px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.13); border-radius: 8px; padding: 8px 16px; font-size: 0.93rem; }
  .header .meta-item strong { display: block; font-size: 1.1rem; }

  /* SECTION TITLES */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 1.13rem; font-weight: 700; letter-spacing: 0.4px; padding: 10px 18px; border-radius: 8px 8px 0 0; color: #fff; margin-bottom: 0; display: flex; align-items: center; gap: 8px; }
  .section-body { background: #fff; border-radius: 0 0 10px 10px; padding: 18px 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.07); }
  .section-body-standalone { background: #fff; border-radius: 10px; padding: 18px 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.07); }

  /* COLOR THEMES */
  .red .section-title, .red-title { background: #c62828; }
  .yellow .section-title, .yellow-title { background: #f9a825; }
  .blue .section-title, .blue-title { background: #1565c0; }
  .green .section-title, .green-title { background: #2e7d32; }
  .purple .section-title, .purple-title { background: #6a1b9a; }
  .gray .section-title, .gray-title { background: #546e7a; }
  .teal .section-title, .teal-title { background: #00695c; }
  .orange .section-title, .orange-title { background: #e65100; }
  .navy .section-title, .navy-title { background: #1a237e; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #e8eaf6; color: #1a237e; font-weight: 700; padding: 9px 12px; text-align: left; border-bottom: 2px solid #c5cae9; }
  td { padding: 8px 12px; border-bottom: 1px solid #f0f0f0; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f9fbe7; }

  /* BADGES */
  .badge { display: inline-block; padding: 2px 9px; border-radius: 12px; font-size: 11px; font-weight: 700; letter-spacing: 0.3px; }
  .badge-red { background: #ffebee; color: #c62828; }
  .badge-yellow { background: #fff9c4; color: #f57f17; }
  .badge-green { background: #e8f5e9; color: #2e7d32; }
  .badge-blue { background: #e3f2fd; color: #1565c0; }
  .badge-purple { background: #f3e5f5; color: #6a1b9a; }
  .badge-gray { background: #eceff1; color: #546e7a; }
  .badge-orange { background: #fff3e0; color: #e65100; }
  .badge-teal { background: #e0f2f1; color: #00695c; }

  /* CARDS */
  .card { border-left: 5px solid #ccc; border-radius: 6px; padding: 12px 16px; margin-bottom: 12px; background: #fafafa; }
  .card-red { border-left-color: #c62828; background: #fff8f8; }
  .card-yellow { border-left-color: #f9a825; background: #fffde7; }
  .card-green { border-left-color: #2e7d32; background: #f1f8e9; }
  .card-blue { border-left-color: #1565c0; background: #e8f4fd; }
  .card-purple { border-left-color: #6a1b9a; background: #faf0ff; }
  .card-gray { border-left-color: #546e7a; background: #f5f6f7; }
  .card-teal { border-left-color: #00695c; background: #e0f7f4; }
  .card-orange { border-left-color: #e65100; background: #fff8f3; }
  .card h4 { font-size: 0.97rem; font-weight: 700; margin-bottom: 4px; }
  .card .card-meta { font-size: 12px; color: #666; margin-bottom: 6px; }
  .card .card-body { font-size: 13px; }
  .card .card-action { margin-top: 8px; font-size: 12px; font-weight: 700; color: #1565c0; }

  /* EXEC SUMMARY */
  .exec-bullet { display: flex; gap: 12px; align-items: flex-start; padding: 10px 0; border-bottom: 1px solid #eee; }
  .exec-bullet:last-child { border-bottom: none; }
  .exec-bullet .icon { font-size: 1.4rem; min-width: 32px; }
  .exec-bullet .text strong { display: block; font-size: 0.95rem; }
  .exec-bullet .text span { font-size: 13px; color: #555; }

  /* CALENDAR */
  .cal-day { margin-bottom: 16px; }
  .cal-day-title { font-weight: 700; font-size: 0.95rem; color: #1a237e; background: #e8eaf6; padding: 6px 12px; border-radius: 6px; margin-bottom: 8px; }
  .cal-event { display: flex; gap: 12px; padding: 8px 12px; border-radius: 6px; margin-bottom: 6px; background: #f0f4ff; border-left: 4px solid #1565c0; align-items: flex-start; }
  .cal-event.declined { border-left-color: #c62828; background: #fff8f8; }
  .cal-event.accepted { border-left-color: #2e7d32; background: #f1f8e9; }
  .cal-event.needs-action { border-left-color: #f9a825; background: #fffde7; }
  .cal-event.confirmed { border-left-color: #6a1b9a; background: #faf0ff; }
  .cal-time { min-width: 100px; font-weight: 700; font-size: 12px; color: #333; }
  .cal-details { flex: 1; }
  .cal-details h5 { font-size: 0.93rem; font-weight: 700; margin-bottom: 3px; }
  .cal-details p { font-size: 12px; color: #555; margin: 2px 0; }

  /* PRIORITY COLORS */
  .pri-high { color: #c62828; font-weight: 700; }
  .pri-med { color: #f57f17; font-weight: 700; }
  .pri-low { color: #2e7d32; font-weight: 700; }

  /* STATUS CHIPS */
  .status-accepted { background: #e8f5e9; color: #2e7d32; }
  .status-declined { background: #ffebee; color: #c62828; }
  .status-pending { background: #fff9c4; color: #f57f17; }
  .status-confirmed { background: #f3e5f5; color: #6a1b9a; }

  /* TRIAGE TABLE */
  .triage-rescued td { background: #e8f5e9 !important; }
  .triage-inbox td { background: #e3f2fd !important; }
  .triage-autotrash td { background: #fce4ec !important; }
  .triage-trash td { background: #f5f6f7 !important; }

  /* MISC */
  ul.checklist { list-style: none; padding: 0; }
  ul.checklist li { padding: 4px 0; padding-left: 20px; position: relative; font-size: 13px; }
  ul.checklist li::before { content: "•"; position: absolute; left: 6px; color: #1565c0; font-weight: 700; }
  .divider { height: 1px; background: #e0e0e0; margin: 14px 0; }
  .note { font-size: 12px; color: #888; font-style: italic; margin-top: 6px; }
  .rescued-tag { font-size: 11px; background: #e8f5e9; color: #2e7d32; border: 1px solid #a5d6a7; border-radius: 10px; padding: 1px 8px; margin-left: 6px; font-weight: 700; }
  .phishing-tag { font-size: 11px; background: #ffebee; color: #c62828; border: 1px solid #ef9a9a; border-radius: 10px; padding: 1px 8px; margin-left: 6px; font-weight: 700; }
  a { color: #1565c0; text-decoration: none; }
  a:hover { text-decoration: underline; }
  .top3 { counter-reset: top3; }
  .top3-item { display: flex; gap: 14px; align-items: flex-start; padding: 14px 0; border-bottom: 1px solid #eee; }
  .top3-item:last-child { border-bottom: none; }
  .top3-num { font-size: 2rem; font-weight: 900; color: #1a237e; min-width: 40px; line-height: 1; }
  .top3-text h4 { font-size: 1rem; font-weight: 700; }
  .top3-text p { font-size: 13px; color: #555; }
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; }
  .dash-card { background: #f8f9ff; border: 1px solid #e0e0e0; border-radius: 10px; padding: 14px 16px; }
  .dash-card h5 { font-size: 0.85rem; font-weight: 700; color: #666; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px; }
  .dash-card .dash-val { font-size: 1.8rem; font-weight: 900; color: #1a237e; }
  .dash-card .dash-sub { font-size: 12px; color: #666; margin-top: 4px; }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ========== HEADER ========== -->
<div class="header">
  <h1>📋 Executive Briefing</h1>
  <div class="subtitle">Prepared by your Executive Chief of Staff</div>
  <div class="meta">
    <div class="meta-item">📅 <strong>Thursday, September 3, 2026</strong></div>
    <div class="meta-item">📧 <strong>50</strong> Total Emails Reviewed</div>
    <div class="meta-item">📆 <strong>7</strong> Calendar Events Reviewed</div>
    <div class="meta-item">⏰ <strong>Labor Day Weekend</strong> begins Friday</div>
  </div>
</div>

<!-- ========== SECTION 0: EMAIL TRIAGE QUICK LIST ========== -->
<div class="section">
  <div class="section-title navy-title" style="background:#1a237e; color:#fff; padding:10px 18px; border-radius:8px 8px 0 0; font-size:1.13rem; font-weight:700;">⚡ Email Triage Quick List</div>
  <div class="section-body" style="padding:0;">
    <table>
      <thead>
        <tr>
          <th style="width:130px;">Status</th>
          <th style="width:210px;">From</th>
          <th>Subject</th>
          <th>Summary</th>
        </tr>
      </thead>
      <tbody>
        <!-- RESCUED ROWS FIRST -->
        <tr class="triage-rescued">
          <td><span class="badge badge-green">✅ RESCUED</span></td>
          <td>Consumer Indirect Pork Litigation</td>
          <td>Class action notice re consumer pork purchases</td>
          <td>Court-approved pork price-fixing class action — may affect Melissa's legal rights. Rescued from Trash.</td>
        </tr>
        <tr class="triage-rescued">
          <td><span class="badge badge-green">✅ RESCUED</span></td>
          <td>USPS Tracking</td>
          <td>Expected Delivery Thursday, September 3 by 9:00pm</td>
          <td>Official USPS delivery notification — package arriving today. Rescued from Trash.</td>
        </tr>
        <tr class="triage-rescued">
          <td><span class="badge badge-green">✅ RESCUED</span></td>
          <td>My Best Buy® Visa® Card (Citi)</td>
          <td>The Labor Day Sale is live — don't miss it.</td>
          <td>Protected sender — credit card notification. Rescued from Trash.</td>
        </tr>
        <tr class="triage-rescued">
          <td><span class="badge badge-green">✅ RESCUED</span></td>
          <td>Match</td>
          <td>Tom likes you. See if it's mutual.</td>
          <td>Match.com notification — protected sender. Rescued from Trash.</td>
        </tr>
        <!-- INBOX ROWS -->
        <tr class="triage-inbox">
          <td><span class="badge badge-blue">📥 INBOX</span></td>
          <td>Merrill Edge</td>
          <td>You have a new account statement</td>
          <td>New financial statement available — review promptly.</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="badge badge-blue">📥 INBOX</span></td>
          <td>INNBEAUTY PROJECT</td>
          <td>We've got your order</td>
          <td>Order #496622 confirmation dated September 2, 2026.</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="badge badge-blue">📥 INBOX</span></td>
          <td>LinkedIn Job Alerts</td>
          <td>VP, HR North America at OrganOx and 4 more</td>
          <td>Senior HR leadership job alert — high relevance.</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="badge badge-blue">📥 INBOX</span></td>
          <td>LinkedIn Job Alerts</td>
          <td>VP, HR North America at OrganOx and 1 more</td>
          <td>Duplicate VP HR alert earlier in day — review with above.</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="badge badge-blue">📥 INBOX</span></td>
          <td>LinkedIn Job Alerts</td>
          <td>People Partner, GTM at Profound and 30 more</td>
          <td>Large batch of HR/People job alerts — review for fit.</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="badge badge-blue">📥 INBOX</span></td>
          <td>LinkedIn Job Alerts</td>
          <td>People Partner, GTM at Profound and 14 more</td>
          <td>Second batch of HR/People job alerts — consolidate with above.</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="badge badge-blue">📥 INBOX</span></td>
          <td>LinkedIn</td>
          <td>Melissa A, looking for a new job?</td>
          <td>LinkedIn job search prompt — may contain relevant recommendations.</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="badge badge-blue">📥 INBOX</span></td>
          <td>Match</td>
          <td>You've had a profile view from Gino</td>
          <td>Gino, 61, Tinton Falls NJ viewed your Match profile.</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="badge badge-blue">📥 INBOX</span></td>
          <td>OkCupid</td>
          <td>Someone likes you</td>
          <td>New like on OkCupid — message them now.</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="badge badge-blue">📥 INBOX</span></td>
          <td>SHEIN</td>
          <td>SHEIN Order Delivery Notification</td>
          <td>SHEIN order delivery update — check for tracking details.</td>
        </tr>
        <!-- AUTO-TRASH SUMMARY ROW -->
        <tr class="triage-autotrash">
          <td><span class="badge badge-red">🗑 AUTO-TRASHED</span></td>
          <td colspan="2">3 emails auto-trashed (phishing/spoofed) + 1 auto-trashed (newsletter) — see Trash Review &amp; Security sections</td>
          <td>Fake Paramount+, Fake CashApp, Fake "Congratulations" casino spam, Gap Factory newsletter. No action needed.</td>
        </tr>
        <!-- MANUAL TRASH SUMMARY ROW -->
        <tr class="triage-trash">
          <td><span class="badge badge-gray">🗂 TRASHED</span></td>
          <td colspan="2">32 emails in Trash (manual) — see Trash Review section</td>
          <td>Mix of newsletters, promotions, duplicate mailings, spam, and low-priority digests. Review before permanent deletion.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ========== SECTION 2: EXECUTIVE SUMMARY ========== -->
<div class="section">
  <div class="section-title red-title" style="background:#b71c1c; padding:10px 18px; border-radius:8px 8px 0 0; font-size:1.13rem; font-weight:700; color:#fff;">🎯 Executive Summary</div>
  <div class="section-body">
    <div class="exec-bullet">
      <div class="icon">🚨</div>
      <div class="text">
        <strong>Biggest Risk: 3 Phishing Emails Auto-Trashed + Class Action Legal Notice</strong>
        <span>Two confirmed phishing emails (fake Paramount+ and fake CashApp) were automatically removed before reaching the inbox. Additionally, a court-approved pork price-fixing class action legal notice was incorrectly trashed and has been rescued — Melissa should review it as it may affect her consumer rights.</span>
      </div>
    </div>
    <div class="exec-bullet">
      <div class="icon">💼</div>
      <div class="text">
        <strong>Biggest Opportunity: Multiple Senior HR Job Alerts Including VP, HR North America (OrganOx)</strong>
        <span>LinkedIn delivered 4 job alert emails today totaling 50+ HR positions. The VP, HR North America role at OrganOx (commercial-stage medical device company) appears in multiple alerts — this is a high-fit senior leadership opportunity worth immediate review before the holiday weekend.</span>
      </div>
    </div>
    <div class="exec-bullet">
      <div class="icon">📅</div>
      <div class="text">
        <strong>Biggest Calendar Item: Coaching Session with Rita Ramakrishnan at 10:00 AM today + HR Networking at 12:00 PM — RSVP pending</strong>
        <span>Today has two back-to-back commitments: an accepted 45-minute coaching/consulting Google Meet with Rita Ramakrishnan (10:00–10:45 AM) and an HR Networking Open Office Hours Zoom at noon that still requires an RSVP. The State Farm bill deadline is Monday, September 7.</span>
      </div>
    </div>
  </div>
</div>

<!-- ========== SECTION 3: ACTION REQUIRED ========== -->
<div class="section">
  <div class="section-title yellow-title" style="background:#f57f17; padding:10px 18px; border-radius:8px 8px 0 0; font-size:1.13rem; font-weight:700; color:#fff;">⚠️ Action Required</div>
  <div class="section-body">

    <div class="card card-red">
      <h4>🚨 SECURITY — Review Class Action Legal Notice</h4>
      <div class="card-meta">From: Consumer Indirect Pork Litigation Settlement Administrator &lt;overchargedforpork@e.epiqnotice.com&gt; | Thu Sep 3, 2026 <span class="rescued-tag">✅ RESCUED FROM TRASH</span></div>
      <div class="card-body">A court-approved notice regarding pork price-fixing settlements was sent to your inbox but ended up in Trash. This is a legitimate legal notice from Epiq (a well-known class action administrator) and may entitle Melissa to compensation for consumer pork purchases. Failure to respond by any deadline could forfeit rights.</div>
      <div class="card-action">→ Open the email, read the full notice, check filing deadlines, and submit a claim if eligible. <strong>Do not ignore.</strong></div>
    </div>

    <div class="card card-red">
      <h4>🔐 SECURITY — Review Merrill Edge Account Statement</h4>
      <div class="card-meta">From: Merrill Edge &lt;merrilledge@ml.com&gt; | Thu Sep 3, 2026 | 📥 INBOX</div>
      <div class="card-body">A new account statement is available online. Given the volume of phishing activity in today's email, verify this notification is legitimate by logging in directly at merrilledge.com (do not click links in the email) and reviewing the statement for any unusual transactions.</div>
      <div class="card-action">→ Log in directly to Merrill Edge portal and review statement. Do not click email links. <strong>Due: Today.</strong></div>
    </div>

    <div class="card card-yellow">
      <h4>📅 RSVP — HR Networking &amp; Job Search: Open Office Hours (Zoom)</h4>
      <div class="card-meta">Calendar Event | Today, Thu Sep 3 | 12:00 PM – 1:00 PM | Status: ⚠️ Needs Action</div>
      <div class="card-body">Today's HR Networking Open Office Hours Zoom at 12:00 PM has not received an RSVP. This conflicts with the tail end of the Rita Ramakrishnan coaching session (10:00–10:45 AM) but there is sufficient gap. The session has 170+ attendees — a large professional networking event in Melissa's HR job search community.</div>
      <div class="card-action">→ RSVP Accept or Decline immediately. Link: <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a>. <strong>Due: Before noon today.</strong></div>
    </div>

    <div class="card card-yellow">
      <h4>💰 BILLING — State Farm Bill Due Monday</h4>
      <div class="card-meta">Calendar Event | Monday, September 7, 2026 (All Day) | Status: Confirmed</div>
      <div class="card-body">State Farm insurance bill is due on Monday, September 7 — which is Labor Day. Banks may be closed. Melissa should pay this today or Friday to avoid a late fee over the holiday weekend.</div>
      <div class="card-action">→ Pay State Farm bill online today or Friday, September 4, before the holiday. <strong>Due: Sep 7 (pay by Sep 5).</strong></div>
    </div>

    <div class="card card-yellow">
      <h4>📦 DELIVERY — USPS Package Arriving Today by 9:00 PM</h4>
      <div class="card-meta">From: USPS Tracking &lt;auto-reply@tracking.usps.com&gt; | Tracking: 9235990404473500706278 <span class="rescued-tag">✅ RESCUED FROM TRASH</span></div>
      <div class="card-body">USPS expects delivery of a package today, Thursday September 3, by 9:00 PM. The notification was rescued from Trash. Melissa should be available or make arrangements for the delivery.</div>
      <div class="card-action">→ Confirm delivery arrangements. Track at usps.com with #9235990404473500706278. <strong>Due: Today by 9:00 PM.</strong></div>
    </div>

    <div class="card card-green">
      <h4>💼 JOB SEARCH — Review VP, HR North America at OrganOx</h4>
      <div class="card-meta">From: LinkedIn Job Alerts | Thu Sep 3, 2026 | 📥 INBOX</div>
      <div class="card-body">VP, HR North America at OrganOx — a commercial-stage organ preservation medical device company — appeared in multiple LinkedIn job alerts today. This is a senior leadership HR role that appears to be a strong fit. The holiday weekend could mean less competition if applied before Friday.</div>
      <div class="card-action">→ Review the OrganOx posting, update tailored resume/cover letter, and apply before COB Friday Sep 5. <strong>Due: Before Labor Day weekend.</strong></div>
    </div>

    <div class="card card-blue">
      <h4>📅 PREP — Coaching Session with Rita Ramakrishnan at 10:00 AM Today</h4>
      <div class="card-meta">Calendar Event | Today, Thu Sep 3 | 10:00 AM – 10:45 AM | Google Meet | Status: ✅ Accepted</div>
      <div class="card-body">45-minute coaching/consulting session with Rita Ramakrishnan (rita@iksana.com) via Google Meet is confirmed for this morning. Melissa should prepare any notes, questions, or updates for her coach ahead of the session.</div>
      <div class="card-action">→ Prepare session agenda and join via Google Meet link in calendar. <strong>Due: 10:00 AM today.</strong></div>
    </div>

    <div class="card card-yellow">
      <h4>💳 FINANCE — InnBeauty Project Order #496622 Confirmed</h4>
      <div class="card-meta">From: INNBEAUTY PROJECT &lt;help@innbeautyproject.com&gt; | Thu Sep 3, 2026 | 📥 INBOX</div>
      <div class="card-body">Order #496622 from InnBeauty Project was confirmed on September 2. Separately, a "Welcome + 15% Off" email was sent — suggesting this may be a first-time purchase. Melissa should retain the order confirmation for her records and watch for shipping notification.</div>
      <div class="card-action">→ Save order confirmation. Watch for shipping email. Discard the duplicate welcome/promo email.</div>
    </div>

  </div>
</div>

<!-- ========== SECTION 4: FULL 7-DAY CALENDAR ========== -->
<div class="section">
  <div class="section-title blue-title" style="background:#1565c0; padding:10px 18px; border-radius:8px 8px 0 0; font-size:1.13rem; font-weight:700; color:#fff;">📆 Full 7-Day Calendar (Sep 3–9, 2026)</div>
  <div class="section-body">

    <!-- Thursday Sep 3 -->
    <div class="cal-day">
      <div class="cal-day-title">📅 Thursday, September 3, 2026 — TODAY</div>

      <div class="cal-event declined">
        <div class="cal-time">9:00–10:30 AM</div>
        <div class="cal-details">
          <h5>Executive Roundtable <span class="badge badge-red">DECLINED</span></h5>
          <p><strong>Host:</strong> John Madigan (Zoom)</p>
          <p><strong>Location:</strong> <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> | Meeting ID: 207 786 667 | PW: 205454</p>
          <p><strong>Status:</strong> <span class="badge badge-red">Declined by Melissa</span></p>
          <p><strong>Prep:</strong> None required — already declined.</p>
          <p><strong>⚠️ Note:</strong> This overlaps with the Rita Ramakrishnan coaching session (10:00 AM). Declining was the correct call given the scheduling conflict.</p>
        </div>
      </div>

      <div class="cal-event accepted">
        <div class="cal-time">10:00–10:45 AM</div>
        <div class="cal-details">
          <h5>Coaching Session: Melissa Weiss &amp; Rita Ramakrishnan <span class="badge badge-green">ACCEPTED</span></h5>
          <p><strong>Attendee:</strong> rita@iksana.com</p>
          <p><strong>Location:</strong> Google Meet — link via Calendly in calendar description</p>
          <p><strong>Status:</strong> <span class="badge badge-green">Accepted ✅</span></p>
          <p><strong>Prep:</strong> Prepare coaching agenda, job search update, and any questions for Rita. Confirm Google Meet link is working before session.</p>
          <p><strong>⚠️ Conflict:</strong> Slight overlap with Executive Roundtable (already declined — no conflict).</p>
        </div>
      </div>

      <div class="cal-event needs-action">
        <div class="cal-time">12:00–1:00 PM</div>
        <div class="cal-details">
          <h5>HR Networking &amp; Job Search: Open Office Hours — Zoom 2 <span class="badge badge-yellow">RSVP NEEDED</span></h5>
          <p><strong>Attendees:</strong> 170+ HR professionals</p>
          <p><strong>Location:</strong> <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a></p>
          <p><strong>Status:</strong> <span class="badge badge-yellow">⚠️ Needs Action — RSVP Required</span></p>
          <p><strong>Prep:</strong> Review HR networking team guidelines before joining. Note: AI notetaking tools are explicitly prohibited per organizer instructions. Prepare 30-second introduction and any specific networking goals.</p>
          <p><strong>Note:</strong> 75-minute break between coaching session and this event.</p>
        </div>
      </div>
    </div>

    <!-- Friday Sep 4 -->
    <div class="cal-day">
      <div class="cal-day-title">📅 Friday, September 4, 2026</div>
      <div class="cal-event confirmed" style="border-left-color:#546e7a; background:#f5f6f7;">
        <div class="cal-time">All Day</div>
        <div class="cal-details">
          <h5>No Events Scheduled</h5>
          <p>Day before Labor Day weekend. Recommended: Pay State Farm bill, finalize OrganOx application, review Merrill Edge statement.</p>
        </div>
      </div>
    </div>

    <!-- Saturday Sep 5 -->
    <div class="cal-day">
      <div class="cal-day-title">📅 Saturday, September 5, 2026</div>
      <div class="cal-event confirmed" style="border-left-color:#546e7a; background:#f5f6f7;">
        <div class="cal-time">All Day</div>
        <div class="cal-details">
          <h5>No Events Scheduled</h5>
          <p>Labor Day weekend — free day.</p>
        </div>
      </div>
    </div>

    <!-- Sunday Sep 6 -->
    <div class="cal-day">
      <div class="cal-day-title">📅 Sunday, September 6, 2026</div>
      <div class="cal-event confirmed" style="border-left-color:#546e7a; background:#f5f6f7;">
        <div class="cal-time">All Day</div>
        <div class="cal-details">
          <h5>No Events Scheduled</h5>
          <p>Labor Day weekend — free day.</p>
        </div>
      </div>
    </div>

    <!-- Monday Sep 7 -->
    <div class="cal-day">
      <div class="cal-day-title">📅 Monday, September 7, 2026 — Labor Day 🇺🇸</div>
      <div class="cal-event confirmed">
        <div class="cal-time">All Day</div>
        <div class="cal-details">
          <h5>State Farm Bill Due <span class="badge badge-yellow">BILLING DEADLINE</span></h5>
          <p><strong>Status:</strong> Confirmed</p>
          <p><strong>⚠️ Action:</strong> Labor Day — banks and online payment systems may have delays. Pay this today (Sep 3) or by Friday (Sep 5) to avoid any late fee. Log in directly to State Farm portal or call 1-800-STATE-FARM.</p>
        </div>
      </div>
    </div>

    <!-- Tuesday Sep 8 -->
    <div class="cal-day">
      <div class="cal-day-title">📅 Tuesday, September 8, 2026</div>
      <div class="cal-event confirmed">
        <div class="cal-time">10:00–11:00 AM</div>
        <div class="cal-details">
          <h5>Nails 💅 <span class="badge badge-purple">PERSONAL</span></h5>
          <p><strong>Status:</strong> Confirmed</p>
          <p><strong>Location:</strong> Not specified in calendar — confirm appointment address.</p>
          <p><strong>Prep:</strong> Confirm appointment and location. Allow travel time.</p>
        </div>
      </div>
    </div>

    <!-- Wednesday Sep 9 -->
    <div class="cal-day">
      <div class="cal-day-title">📅 Wednesday, September 9, 2026</div>

      <div class="cal-event needs-action">
        <div class="cal-time">12:00–1:30 PM</div>
        <div class="cal-details">
          <h5>HR Networking &amp; Job Search Group — Zoom 2 <span class="badge badge-yellow">RSVP NEEDED</span></h5>
          <p><strong>Attendees:</strong> 170+ HR professionals (same group as today)</p>
          <p><strong>Location:</strong> <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a></p>
          <p><strong>Status:</strong> <span class="badge badge-yellow">⚠️ Needs Action — RSVP Required</span></p>
          <p><strong>Prep:</strong> Review team resources and HR networking guidelines before joining. No AI notetaking tools permitted. This is a 90-minute session (vs. 60 min today).</p>
        </div>
      </div>

      <div class="cal-event confirmed">
        <div class="cal-time">12:00–1:30 PM</div>
        <div class="cal-details">
          <h5>Network <span class="badge badge-green">CONFIRMED</span></h5>
          <p><strong>Status:</strong> Confirmed (separate from HR Networking group above — may be the same event or a different networking call)</p>
          <p><strong>⚠️ Note:</strong> This event overlaps exactly with the HR Networking &amp; Job Search Group Zoom on the same day/time. Verify if these are the same event or if there is a conflict requiring a decision.</p>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- ========== SECTION 5: JOB SEARCH & INTERVIEW PIPELINE ========== -->
<div class="section">
  <div class="section-title green-title" style="background:#2e7d32; padding:10px 18px; border-radius:8px 8px 0 0; font-size:1.13rem; font-weight:700; color:#fff;">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">
    <table>
      <thead>
        <tr>
          <th>Source</th>
          <th>Role / Alert</th>
          <th>Fit</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>LinkedIn Job Alerts</strong></td>
          <td>VP, HR North America at OrganOx (commercial-stage medical device) — appeared in 2 separate alerts today</td>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>Review posting immediately. Apply before Labor Day weekend. Tailor resume to medical/commercial-stage org.</td>
        </tr>
        <tr>
          <td><strong>LinkedIn Job Alerts</strong></td>
          <td>People Partner, GTM at Profound — marketing platform for AI age — appeared in 2 separate alerts (14 more &amp; 30 more)</td>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>Review full alert. Profound is an AI-era marketing company — strong GTM HR fit if Melissa has tech/startup experience.</td>
        </tr>
        <tr>
          <td><strong>LinkedIn Job Alerts</strong></td>
          <td>4 separate alert emails today covering 50+ HR positions total — various levels and functions</td>
          <td><span class="badge badge-yellow">MEDIUM</span></td>
          <td>Set aside 30 min to scan all 4 LinkedIn alerts. Create a shortlist of top 3–5 positions beyond OrganOx and Profound.</td>
        </tr>
        <tr>
          <td><strong>Glassdoor Jobs</strong></td>
          <td>Community Coordinator at Van Police Department + 4 more in New York, NY</td>
          <td><span class="badge badge-gray">LOW</span></td>
          <td>Community Coordinator likely below Melissa's level. Review the other 4 roles — one may be relevant. Email was trashed but worth a quick scan.</td>
        </tr>
        <tr>
          <td><strong>LinkedIn</strong></td>
          <td>"Melissa A, looking for a new job?" — general LinkedIn job discovery prompt</td>
          <td><span class="badge badge-yellow">MEDIUM</span></td>
          <td>Check LinkedIn's recommended jobs section. May surface roles not in alert emails.</td>
        </tr>
        <tr>
          <td><strong>SHRM HR Jobs</strong></td>
          <td>36 New Human Resources Jobs digest</td>
          <td><span class="badge badge-yellow">MEDIUM</span></td>
          <td>SHRM job board is highly relevant for HR professionals. Review digest for senior-level openings.</td>
        </tr>
        <tr>
          <td><strong>Calendar — Networking</strong></td>
          <td>HR Networking &amp; Job Search: Open Office Hours — Today 12 PM (RSVP needed)</td>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>Attend today's Zoom networking session — 170+ HR professionals in active job search community. RSVP now.</td>
        </tr>
        <tr>
          <td><strong>Calendar — Networking</strong></td>
          <td>HR Networking &amp; Job Search Group — Sep 9, 12–1:30 PM (RSVP needed)</td>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>RSVP to next week's 90-minute networking session. Same community — consistent attendance builds relationships.</td>
        </tr>
        <tr>
          <td><strong>Calendar — Coaching</strong></td>
          <td>Coaching session with Rita Ramakrishnan — Today 10:00 AM (Accepted)</td>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>Leverage this session to discuss job search strategy, review target companies, and prep application materials.</td>
        </tr>
        <tr>
          <td><strong>The People People Group</strong></td>
          <td>TPPG Digest — Async Interviews, SHRM-CP Certification in Canada, 8 more topics (trashed)</td>
          <td><span class="badge badge-yellow">MEDIUM</span></td>
          <td>Trashed but potentially valuable — the async interview discussion is highly relevant for current HR job seekers. Consider rescuing from trash.</td>
        </tr>
      </tbody>
    </table>
    <p class="note">⚡ Job search tip: Today is Thursday before Labor Day. Many hiring managers will check email today before the holiday. Sending applications today maximizes visibility.</p>
  </div>
</div>

<!-- ========== SECTION 6: FULL EMAIL REVIEW BY CATEGORY ========== -->
<div class="section">
  <div class="section-title navy-title" style="background:#37474f; padding:10px 18px; border-radius:8px 8px 0 0; font-size:1.13rem; font-weight:700; color:#fff;">📂 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="card card-red">
      <h4>🚨 Security / Risk &nbsp;<span class="badge badge-red">5 emails</span></h4>
      <div class="card-body">
        <table>
          <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
          <tbody>
            <tr><td>Paramount+ Notification &lt;info@zvybphkhshgip&gt;</td><td>90 Days of Paramount+ Free — Limited Time Offer!</td><td><span class="phishing-tag">🗑 AUTO-TRASHED PHISHING</span></td><td>Spoofed sender with invalid domain, fake membership expiry. Removed. No action needed.</td></tr>
            <tr><td>"💲CashApp💲" &lt;info@csgzdjgaovgaj&gt;</td><td>𝗬𝗼𝘂 𝗵𝗮𝘃𝗲 𝗿𝗲𝗰𝗲𝗶𝘃𝗲𝗱 $15.99 — Raging Bull Casino</td><td><span class="phishing-tag">🗑 AUTO-TRASHED PHISHING</span></td><td>Fake CashApp impersonation, casino lure, template injection visible. Removed. No action needed.</td></tr>
            <tr><td>"'Congratulatiaons🎉'" &lt;qppsupportwt@...&gt;</td><td>200 Free Spins 💰 Pending in your Account🎰</td><td><span class="badge badge-red">SPAM/PHISHING — NOT TRASHED</span></td><td>Fake casino spam with misspelled "Congratulations" — suspicious domain. Move to trash immediately.</td></tr>
            <tr><td>Consumer Indirect Pork Litigation Settlement</td><td>Class action notice re consumer pork purchases</td><td><span class="rescued-tag">✅ RESCUED FROM TRASH</span></td><td><strong>LEGITIMATE LEGAL NOTICE.</strong> Court-approved via Epiq. Review, check filing deadline, submit claim if eligible.</td></tr>
            <tr><td>Merrill Edge &lt;merrilledge@ml.com&gt;</td><td>You have a new account statement</td><td><span class="badge badge-blue">📥 INBOX</span></td><td>Verify legitimacy by logging in directly. Do not click email links. Review statement for anomalies.</td></tr>
          </tbody>
        </table>
      </div>
      <div class="card-action">→ Immediate actions: (1) Read pork class action notice. (2) Log into Merrill Edge directly. (3) Trash the casino spam email still sitting outside trash.</div>
    </div>

    <!-- JOB SEARCH -->
    <div class="card card-green">
      <h4>💼 Job Search &nbsp;<span class="badge badge-green">6 emails</span></h4>
      <div class="card-body">
        <table>
          <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Fit</th></tr></thead>
          <tbody>
            <tr><td>LinkedIn Job Alerts</td><td>VP, HR North America at OrganOx and 4 more</td><td>📥 INBOX</td><td><span class="badge badge-green">HIGH</span></td></tr>
            <tr><td>LinkedIn Job Alerts</td><td>VP, HR North America at OrganOx and 1 more</td><td>📥 INBOX</td><td><span class="badge badge-green">HIGH</span></td></tr>
            <tr><td>LinkedIn Job Alerts</td><td>People Partner, GTM at Profound and 30 more</td><td>📥 INBOX</td><td><span class="badge badge-green">HIGH</span></td></tr>
            <tr><td>LinkedIn Job Alerts</td><td>People Partner, GTM at Profound and 14 more</td><td>📥 INBOX</td><td><span class="badge badge-yellow">MED</span></td></tr>
            <tr><td>LinkedIn</td><td>Melissa A, looking for a new job?</td><td>📥 INBOX</td><td><span class="badge badge-yellow">MED</span></td></tr>
            <tr><td>Glassdoor Jobs</td><td>Community Coordinator at Van Police Department and 4 more</td><td>🗂 TRASH</td><td><span class="badge badge-gray">LOW</span></td></tr>
          </tbody>
        </table>
      </div>
      <div class="card-action">→ Review all 4 LinkedIn alerts today. Prioritize OrganOx VP role and Profound People Partner. Scan Glassdoor alert for the other 4 non-coordinator roles.</div>
    </div>

    <!-- RECRUITERS / NETWORKING -->
    <div class="card card-green" style="border-left-color: #1b5e20;">
      <h4>🤝 Recruiters / Networking &nbsp;<span class="badge badge-green">2 emails</span></h4>
      <div class="card-body">
        <table>
          <thead><tr><th>From</th><th>Subject</th><th>Notes</th></tr></thead>
          <tbody>
            <tr><td>SHRM HR Jobs</td><td>36 New Human Resources Jobs</td><td>SHRM premium job board alert — highly relevant for senior HR roles. Review today.</td></tr>
            <tr><td>The People People Group</td><td>TPPG Digest — Async Interviews, SHRM-CP Certification, 8 more topics</td><td>Trashed — community digest with relevant HR topics. Consider reviewing async interview discussion.</td></tr>
          </tbody>
        </table>
      </div>
      <div class="card-action">→ Review SHRM job alert for senior openings. Rescue TPPG Digest from trash for async interview insights.</div>
    </div>

    <!-- CALENDAR / EVENTS -->
    <div class="card card-blue">
      <h4>📅 Calendar / Events &nbsp;<span class="badge badge-blue">2 emails</span></h4>
      <div class="card-body">
        <table>
          <thead><tr><th>From</th><th>Subject</th><th>Notes</th></tr></thead>
          <tbody>
            <tr><td>Transform &lt;community@transform.us&gt;</td><td>Join us at Sequoia Grove Conference</td><td>Trashed — HR/leadership conference invitation. May be worth reviewing if relevant to Melissa's field.</td></tr>
            <tr><td>Melissa W (self-sent)</td><td>Demand for justice in the Noah Animal cruelty case</td><td>Sent by Melissa to District Attorney — advocacy letter, not a calendar event. Kept for reference.</td></tr>
          </tbody>
        </table>
      </div>
      <div class="card-action">→ Review Sequoia Grove Conference details before deleting. The self-sent advocacy email requires no action.</div>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="card card-yellow">
      <h4>💳 Financial / Billing &nbsp;<span class="badge badge-yellow">3 emails</span></h4>
      <div class="card-body">
        <table>
          <thead><tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
          <tbody>
            <tr><td>Merrill Edge</td><td>You have a new account statement</td><td>📥 INBOX</td><td>Review statement — log in directly, don't click links.</td></tr>
            <tr><td>My Best Buy® Visa® Card (Citi)</td><td>The Labor Day Sale is live — don't miss it</td><td><span class="rescued-tag">✅ RESCUED FROM TRASH</span></td><td>Protected sender. Credit card notification. Note any financing offers if applicable.</td></tr>
            <tr><td>Equifax</td><td>Your Apple Card credit limit offer is waiting</td><td>Read/Not in inbox</td><td>Pre-qualification offer for Apple Card from Equifax. No immediate action required — review if interested in new credit line.</td></tr>
          </tbody>
        </table>
      </div>
      <div class="card-action">→ Primary action: Review Merrill Edge statement directly. Secondary: Note State Farm bill due Sep 7 (pay by Sep 5).</div>
    </div>

    <!-- PERSONAL -->
    <div class="card card-purple" style="border-left-color: #880e4f;">
      <h4>💕 Personal &nbsp;<span class="badge badge-purple">5 emails</span></h4>
      <div class="card-body">
        <table>
          <thead><tr><th>From</th><th>Subject</th><th>Notes</th></tr></thead>
          <tbody>
            <tr><td>Match</td><td>You've had a profile view from Gino (61, Tinton Falls NJ)</td><td>📥 INBOX — Dating app notification. Gino viewed Melissa's profile.</td></tr>
            <tr><td>Match</td><td>Tom likes you. See if it's mutual.</td><td><span class="rescued-tag">✅ RESCUED FROM TRASH</span> — Protected sender. Tom liked Melissa's profile.</td></tr>
            <tr><td>OkCupid</td><td>Someone likes you (Thu Sep 3)</td><td>📥 INBOX — New like on OkCupid.</td></tr>
            <tr><td>OkCupid</td><td>Someone likes you (Wed Sep 2)</td><td>Not in inbox — second OkCupid like notification from previous day.</td></tr>
            <tr><td>Ruth on Facebook</td><td>Ruth Hiller Peck commented on a post — "Spectacular image of our front paddock..."</td><td>Facebook close friend notification — no action required.</td></tr>
          </tbody>
        </table>
      </div>
      <div class="card-action">→ Review Match and OkCupid notifications at leisure. No urgent action needed.</div>
    </div>

    <!-- ORDERS / DELIVERIES -->
    <div class="card card-teal">
      <h4>📦 Orders &amp; Deliveries &nbsp;<span class="badge badge-teal">3 emails</span></h4>
      <div class="card-body">
        <table>
          <thead><tr><th>From</th><th>Subject</th><th>Notes</th></tr></thead>
          <tbody>
            <tr><td>USPS Tracking</td><td>Expected Delivery Thursday, Sep 3 by 9:00 PM — Tracking #9235990404473500706278</td><td><span class="rescued-tag">✅ RESCUED FROM TRASH</span> — Package arriving today. Arrange for delivery.</td></tr>
            <tr><td>INNBEAUTY PROJECT</td><td>We've got your order — Order #496622</td><td>📥 INBOX — Order confirmation from Sep 2. Retain for records.</td></tr>
            <tr><td>Amazon &lt;return@amazon.com&gt;</td><td>Advance refund issued for Saodimallsu Womens Short Sleeve + 1 other item — addressed to Sophie</td><td>🗂 TRASH — Addressed to "Sophie" not Melissa. May have been misdirected or sent in error. Verify if this refund applies to Melissa.</td></tr>
          </tbody>
        </table>
      </div>
      <div class="card-action">→ Watch for USPS delivery today. Verify the Amazon refund email — it's addressed to "Sophie" and may not belong to Melissa.</td></div>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="card card-purple">
      <h4>📚 Professional Development &nbsp;<span class="badge badge-purple">3 emails</span></h4>
      <div class="card-body">
        <table>
          <thead><tr><th>From</th><th>Subject</th><th>Recommendation</th></tr></thead>
          <tbody>
            <tr><td>Gemma Bonham-Carter [Noted]</td><td>LinkedIn just killed its own AI writing tool (trashed)</td><td>Relevant for HR professionals using LinkedIn. Consider rescuing — the AI tool update directly affects job search strategy.</td></tr>
            <tr><td>Pranit naik via Medium</td><td>Grok Bot Is Here: xAI's Always-On AI Agent, Explained (trashed)</td><td>AI industry update — useful for staying current on emerging tools. Low priority.</td></tr>
            <tr><td>LinkedIn</td><td>Leah Kavanagh, M.Jur. and others share their thoughts — concierge medical practice hiring</td><td>LinkedIn network activity — "We're hiring" post from a concierge medical practice. Potentially relevant if Melissa is open to healthcare HR roles.</td></tr>
          </tbody>
        </table>
      </div>
      <div class="card-action">→ Rescue Gemma Bonham-Carter newsletter from trash — LinkedIn AI writing tool news is directly relevant to job search.</div>
    </div>

    <!-- ADVOCACY / CIVIC -->
    <div class="card card-orange">
      <h4>🗳️ Civic / Political &nbsp;<span class="badge badge-orange">2 emails</span></h4>
      <div class="card-body">
        <table>
          <thead><tr><th>From</th><th>Subject</th><th>Notes</th></tr></thead>
          <tbody>
            <tr><td>Jon Ossoff &lt;info@e.electjon.com&gt;</td><td>Please</td><td>Political fundraising email from Sen. Jon Ossoff's campaign. No action required.</td></tr>
            <tr><td>Alina for NY &lt;campaign@alinabonsell.com&gt;</td><td>This Ad Is Turning Heads In Taxis All Over Manhattan</td><td>Local NYC political campaign email (Alina Bonsell for NY). Informational only.</td></tr>
          </tbody>
        </table>
      </div>
      <div class="card-action">→ No action required. Unsubscribe from political emails if not wanted.</div>
    </div>

  </div>
</div>

<!-- ========== SECTION 7: TRASH REVIEW ========== -->
<div class="section">
  <div class="section-title red-title" style="background:#c62828; padding:10px 18px; border-radius:8px 8px 0 0; font-size:1.13rem; font-weight:700; color:#fff;">🗑️ Trash Review</div>
  <div class="section-body">

    <h4 style="color:#2e7d32; margin-bottom:10px;">✅ Restore Immediately</h4>
    <table style="margin-bottom:18px;">
      <thead><tr><th>From</th><th>Subject</th><th>Reason to Restore</th></tr></thead>
      <tbody>
        <tr style="background:#e8f5e9;">
          <td>Consumer Indirect Pork Litigation Settlement Administrator</td>
          <td>Class action notice re consumer pork purchases</td>
          <td><strong>Already rescued.</strong> Legitimate court-approved legal notice from Epiq. May entitle Melissa to financial compensation. Must read and act on before deadline.</td>
        </tr>
        <tr style="background:#e8f5e9;">
          <td>USPS Tracking</td>
          <td>Expected Delivery Thursday, Sep 3 by 9:00 PM — #9235990404473500706278</td>
          <td><strong>Already rescued.</strong> Official USPS delivery notification. Package arriving today.</td>
        </tr>
        <tr style="background:#e8f5e9;">
          <td>My Best Buy® Visa® Card (Citi)</td>
          <td>The Labor Day Sale is live — don't miss it</td>
          <td><strong>Already rescued.</strong> Protected sender — credit card correspondence.</td>
        </tr>
        <tr style="background:#e8f5e9;">
          <td>Match</td>
          <td>Tom likes you. See if it's mutual.</td>
          <td><strong>Already rescued.</strong> Protected sender — dating app notification Melissa wants to see.</td>
        </tr>
      </tbody>
    </table>

    <div class="divider"></div>
    <h4 style="color:#f57f17; margin-bottom:10px;">🔍 Review Before Deleting</h4>
    <table style="margin-bottom:18px;">
      <thead><tr><th>From</th><th>Subject</th><th>Review Reason</th></tr></thead>
      <tbody>
        <tr>
          <td>Gemma Bonham-Carter [Noted]</td>
          <td>LinkedIn just killed its own AI writing tool</td>
          <td>
