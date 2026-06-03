<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Melissa's Daily Briefing – June 3, 2026</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; line-height: 1.5; }
  .wrapper { max-width: 780px; margin: 0 auto; padding: 20px; }

  /* Header */
  .header { background: linear-gradient(135deg, #0d1b3e, #1a3a6e); border-radius: 14px; padding: 36px 32px; margin-bottom: 24px; text-align: center; }
  .header h1 { color: #ffffff; font-size: 2rem; font-weight: 700; letter-spacing: 0.5px; }
  .header p { color: #a8c4e8; font-size: 1rem; margin-top: 8px; letter-spacing: 0.3px; }
  .header .badge { display: inline-block; background: rgba(255,255,255,0.15); color: #e0ecff; border-radius: 20px; padding: 4px 14px; font-size: 0.82rem; margin-top: 10px; letter-spacing: 0.4px; }

  /* Section Headers */
  .section-title { font-size: 1.1rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin: 28px 0 12px 0; color: #0d1b3e; border-left: 5px solid #1a3a6e; padding-left: 12px; }

  /* Cards */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; border-left: 5px solid; display: grid; gap: 4px; }
  .card-label { font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; opacity: 0.75; }
  .card-title { font-size: 1rem; font-weight: 700; }
  .card-source { font-size: 0.82rem; opacity: 0.7; }
  .card-why { font-size: 0.88rem; margin-top: 4px; }
  .card-action { font-size: 0.85rem; margin-top: 6px; font-weight: 600; }
  .card-action::before { content: "▶ Next Step: "; }

  /* Red */
  .red { background: #fff0f0; border-color: #d32f2f; }
  .red .card-label { color: #b71c1c; }
  .red .card-title { color: #c62828; }
  .red .card-action { color: #b71c1c; }

  /* Yellow */
  .yellow { background: #fffde7; border-color: #f9a825; }
  .yellow .card-label { color: #e65100; }
  .yellow .card-title { color: #bf6f00; }
  .yellow .card-action { color: #e65100; }

  /* Blue */
  .blue { background: #e8f0fe; border-color: #1565c0; }
  .blue .card-label { color: #0d47a1; }
  .blue .card-title { color: #1565c0; }
  .blue .card-action { color: #0d47a1; }

  /* Green */
  .green { background: #e8f5e9; border-color: #2e7d32; }
  .green .card-label { color: #1b5e20; }
  .green .card-title { color: #2e7d32; }
  .green .card-action { color: #1b5e20; }

  /* Purple */
  .purple { background: #f3e5f5; border-color: #6a1b9a; }
  .purple .card-label { color: #4a148c; }
  .purple .card-title { color: #6a1b9a; }
  .purple .card-action { color: #4a148c; }

  /* Gray */
  .gray { background: #f5f5f5; border-color: #9e9e9e; }
  .gray .card-label { color: #616161; }
  .gray .card-title { color: #424242; }
  .gray .card-action { color: #616161; }

  /* Executive Summary */
  .exec-summary { background: linear-gradient(135deg, #1a3a6e, #0d2855); border-radius: 12px; padding: 24px 28px; margin-bottom: 8px; }
  .exec-summary h2 { color: #a8c4e8; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 14px; }
  .exec-summary ul { list-style: none; padding: 0; }
  .exec-summary ul li { color: #e8f0fe; font-size: 0.95rem; padding: 7px 0; border-bottom: 1px solid rgba(255,255,255,0.1); display: flex; align-items: flex-start; gap: 10px; }
  .exec-summary ul li:last-child { border-bottom: none; }
  .exec-summary ul li::before { content: "●"; color: #64b5f6; font-size: 0.7rem; margin-top: 4px; flex-shrink: 0; }

  /* Schedule table */
  .schedule-table { width: 100%; border-collapse: collapse; border-radius: 10px; overflow: hidden; font-size: 0.88rem; }
  .schedule-table th { background: #1a3a6e; color: #e8f0fe; padding: 10px 14px; text-align: left; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.8px; }
  .schedule-table td { padding: 10px 14px; border-bottom: 1px solid #e0e0e0; background: #ffffff; vertical-align: top; }
  .schedule-table tr:last-child td { border-bottom: none; }
  .status-badge { display: inline-block; border-radius: 12px; padding: 2px 10px; font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
  .status-confirmed { background: #c8e6c9; color: #1b5e20; }
  .status-declined { background: #ffcdd2; color: #b71c1c; }
  .status-pending { background: #fff9c4; color: #f57f17; }
  .status-allday { background: #e1bee7; color: #4a148c; }
  .conflict-flag { color: #d32f2f; font-weight: 700; font-size: 0.78rem; }

  /* Action Table */
  .action-table { width: 100%; border-collapse: collapse; font-size: 0.86rem; border-radius: 10px; overflow: hidden; }
  .action-table th { background: #0d1b3e; color: #a8c4e8; padding: 10px 14px; text-align: left; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.8px; }
  .action-table td { padding: 10px 14px; border-bottom: 1px solid #e0e0e0; background: #fff; vertical-align: top; }
  .action-table tr:last-child td { border-bottom: none; }
  .priority-high { color: #b71c1c; font-weight: 700; }
  .priority-med { color: #e65100; font-weight: 700; }
  .priority-low { color: #388e3c; font-weight: 700; }

  /* Top 3 */
  .top3 { background: linear-gradient(135deg, #0d1b3e, #1a3a6e); border-radius: 14px; padding: 28px 32px; margin-top: 8px; }
  .top3 h2 { color: #a8c4e8; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 16px; }
  .top3-item { display: flex; align-items: flex-start; gap: 16px; margin-bottom: 16px; }
  .top3-item:last-child { margin-bottom: 0; }
  .top3-num { background: #f9a825; color: #0d1b3e; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1rem; flex-shrink: 0; }
  .top3-text { color: #e8f0fe; font-size: 0.95rem; }
  .top3-text strong { color: #ffffff; display: block; font-size: 1rem; margin-bottom: 2px; }

  .divider { height: 1px; background: #dde3ec; margin: 8px 0 4px 0; }
  .footer { text-align: center; color: #9e9e9e; font-size: 0.78rem; margin-top: 28px; padding-bottom: 20px; }
</style>
</head>
<body>
<div class="wrapper">

  <!-- HEADER -->
  <div class="header">
    <h1>Good morning, Melissa ☀️</h1>
    <p>Your Executive Daily Briefing</p>
    <span class="badge">Wednesday, June 3, 2026</span>
  </div>

  <!-- EXECUTIVE SUMMARY -->
  <div class="exec-summary">
    <h2>Executive Summary</h2>
    <ul>
      <li><strong>Security Alert:</strong> A phishing email impersonating a cloud service is in your inbox — do not click any links; it is a scam and should be deleted immediately.</li>
      <li><strong>Tomorrow is busy:</strong> You have three calendar items on June 4 — Dr. Husk appointment at 10:30 AM is confirmed, an HR networking session at noon needs your RSVP, and the Executive Roundtable you've already declined.</li>
      <li><strong>Job Pipeline is Active:</strong> Three strong LinkedIn/job-board leads arrived today — Chief People Officer at Conexus (up to $350K), Sr. Director HRBP (AI-Native), and Director of Global People Ops at Sonatype — all warrant review today.</li>
    </ul>
  </div>

  <!-- SECTION 1: ACTION REQUIRED -->
  <div class="section-title">🔴 Action Required</div>

  <div class="card red">
    <span class="card-label">🚨 Security — Phishing Scam</span>
    <span class="card-title">"Your Cloud Account Has Been Locked" — Fake Payment Decline Notice</span>
    <span class="card-source">From: xbtcsupportmd@wcknlkzajfzzlhmducymgdwi.com · Unread · Not in Inbox/Trash</span>
    <span class="card-why">Classic phishing attack: spoofed sender domain, urgent scare language about photos/videos being deleted, impersonates a cloud subscription service. The sender address is gibberish and the display name uses lookalike Unicode characters ("Payment_Declined"). Do not open, do not click any links.</span>
    <span class="card-action">Mark as spam and delete immediately. No action needed on any "account."</span>
  </div>

  <div class="card red">
    <span class="card-label">⚠️ Suspicious — Fake "Costco Early Access"</span>
    <span class="card-title">"Wanted" — Empty-body email from Gmail address posing as Costco</span>
    <span class="card-source">From: dandreakwallace@gmail.com · Not in Inbox</span>
    <span class="card-why">Unsolicited email with no body from a personal Gmail address disguised as "Costco Early Access." Likely a phishing probe or spoofed outreach. Costco does not communicate from Gmail accounts.</span>
    <span class="card-action">Mark as spam and delete. Do not reply.</span>
  </div>

  <div class="card yellow">
    <span class="card-label">📅 Pending RSVP — Tomorrow</span>
    <span class="card-title">HR Networking &amp; Job Search: Open Office Hours — Zoom (June 4, 12–1 PM)</span>
    <span class="card-source">Google Calendar · Status: Needs Action</span>
    <span class="card-why">You haven't responded to this invite. It overlaps with your morning medical appointment (Dr. Husk ends at 11:30 AM), giving you 30 minutes before this starts. Worth attending given active job search.</span>
    <span class="card-action">Confirm or decline the calendar invite today. Zoom link: us06web.zoom.us/j/85945371140</span>
  </div>

  <div class="card yellow">
    <span class="card-label">💰 Billing Reminder — This Weekend</span>
    <span class="card-title">State Farm Bill Due — June 7</span>
    <span class="card-source">Google Calendar · All-Day Event · Sat Jun 7</span>
    <span class="card-why">State Farm payment is flagged on your calendar for Saturday. No lead time remaining if you haven't paid.</span>
    <span class="card-action">Confirm payment is scheduled or log in to pay before Friday.</span>
  </div>

  <div class="card yellow">
    <span class="card-label">📬 Personal Follow-Up</span>
    <span class="card-title">Contact Question — Reply to Jade re: Appointment Moved to June 10</span>
    <span class="card-source">From: melissa (you) · Sent Wed Jun 3 · Not in Inbox</span>
    <span class="card-why">You emailed Jade confirming you moved your appointment to the 10th and will check in Monday or Tuesday about whether something has arrived. Action item lives with you.</span>
    <span class="card-action">Set a reminder to follow up with Jade on Monday, June 8.</span>
  </div>

  <!-- SECTION 2: TODAY'S SCHEDULE + PREP -->
  <div class="section-title">📅 Today's Schedule + Upcoming Week Prep</div>

  <div class="card blue">
    <span class="card-label">📆 Today — Wednesday, June 3</span>
    <span class="card-title">No meetings scheduled today — use this time strategically</span>
    <span class="card-source">Google Calendar</span>
    <span class="card-why">Your calendar is clear today. Ideal window to respond to job leads, confirm/decline tomorrow's networking session, process job applications, and handle billing.</span>
    <span class="card-action">Block focused time today for job search and follow-ups (see priorities below).</span>
  </div>

  <table class="schedule-table" style="margin-bottom:12px;">
    <tr>
      <th>Date</th>
      <th>Time</th>
      <th>Event</th>
      <th>Status</th>
      <th>Notes</th>
    </tr>
    <tr
