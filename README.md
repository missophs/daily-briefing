<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa — September 9, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }

  .page-wrapper { max-width: 1200px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 16px; padding: 36px 40px; margin-bottom: 28px; display: flex; justify-content: space-between; align-items: flex-start; }
  .header-left h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header-left p { font-size: 15px; color: #a0b4d0; margin-top: 4px; }
  .header-stats { display: flex; gap: 24px; margin-top: 16px; }
  .stat-pill { background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.15); border-radius: 24px; padding: 8px 18px; text-align: center; }
  .stat-pill .num { font-size: 22px; font-weight: 700; color: #7dd3fc; }
  .stat-pill .lbl { font-size: 11px; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px; }
  .header-right { text-align: right; }
  .header-right .date-badge { background: rgba(255,255,255,0.12); border-radius: 10px; padding: 12px 20px; }
  .header-right .date-badge .dow { font-size: 13px; color: #7dd3fc; text-transform: uppercase; letter-spacing: 1px; }
  .header-right .date-badge .full-date { font-size: 17px; font-weight: 600; color: #fff; margin-top: 2px; }
  .header-right .byline { font-size: 11px; color: #64748b; margin-top: 10px; }

  /* SECTION HEADERS */
  .section { margin-bottom: 28px; }
  .section-header { display: flex; align-items: center; gap: 10px; margin-bottom: 14px; }
  .section-header h2 { font-size: 17px; font-weight: 700; color: #1a1a2e; }
  .section-number { background: #1a1a2e; color: #fff; border-radius: 50%; width: 26px; height: 26px; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 700; flex-shrink: 0; }
  .section-line { flex: 1; height: 2px; background: linear-gradient(90deg, #e2e8f0, transparent); }

  /* CARDS */
  .card { background: #fff; border-radius: 12px; padding: 18px 22px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); border-left: 5px solid #e2e8f0; margin-bottom: 12px; }
  .card.red { border-left-color: #ef4444; background: #fff8f8; }
  .card.yellow { border-left-color: #f59e0b; background: #fffdf5; }
  .card.blue { border-left-color: #3b82f6; background: #f8fbff; }
  .card.green { border-left-color: #10b981; background: #f4fff9; }
  .card.purple { border-left-color: #8b5cf6; background: #faf8ff; }
  .card.gray { border-left-color: #94a3b8; background: #f8fafc; }
  .card.orange { border-left-color: #f97316; background: #fff8f4; }

  .card-label { display: inline-block; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; padding: 2px 8px; border-radius: 4px; margin-bottom: 6px; }
  .label-red { background: #fee2e2; color: #b91c1c; }
  .label-yellow { background: #fef3c7; color: #92400e; }
  .label-blue { background: #dbeafe; color: #1d4ed8; }
  .label-green { background: #d1fae5; color: #065f46; }
  .label-purple { background: #ede9fe; color: #5b21b6; }
  .label-gray { background: #f1f5f9; color: #475569; }
  .label-orange { background: #ffedd5; color: #9a3412; }

  .card h3 { font-size: 15px; font-weight: 700; margin-bottom: 6px; }
  .card .meta { font-size: 12px; color: #64748b; margin-bottom: 8px; }
  .card .why { font-size: 13px; margin-bottom: 6px; }
  .card .action { font-size: 13px; font-weight: 600; }
  .card .due { font-size: 12px; color: #ef4444; font-weight: 600; margin-top: 4px; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }
  th { background: #1a1a2e; color: #fff; padding: 11px 14px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.6px; text-align: left; }
  td { padding: 10px 14px; font-size: 13px; border-bottom: 1px solid #f1f5f9; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f8fafc; }

  /* STATUS BADGES */
  .badge { display: inline-block; padding: 2px 9px; border-radius: 12px; font-size: 11px; font-weight: 700; }
  .badge-rescued { background: #d1fae5; color: #065f46; }
  .badge-inbox { background: #dbeafe; color: #1d4ed8; }
  .badge-trashed { background: #fee2e2; color: #b91c1c; }
  .badge-manual-trash { background: #f1f5f9; color: #475569; }
  .badge-high { background: #fee2e2; color: #b91c1c; }
  .badge-medium { background: #fef3c7; color: #92400e; }
  .badge-low { background: #f1f5f9; color: #475569; }
  .badge-accepted { background: #d1fae5; color: #065f46; }
  .badge-declined { background: #fee2e2; color: #b91c1c; }
  .badge-needs-action { background: #fef3c7; color: #92400e; }
  .badge-confirmed { background: #dbeafe; color: #1d4ed8; }

  /* GRIDS */
  .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  .three-col { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; }

  /* EXEC SUMMARY */
  .exec-bullets { display: flex; flex-direction: column; gap: 10px; }
  .exec-bullet { background: #fff; border-radius: 10px; padding: 14px 18px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); display: flex; gap: 14px; align-items: flex-start; }
  .exec-bullet .icon { font-size: 22px; flex-shrink: 0; }
  .exec-bullet .text strong { font-size: 14px; display: block; margin-bottom: 3px; }
  .exec-bullet .text span { font-size: 13px; color: #475569; }

  /* CALENDAR */
  .cal-day { background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,0.07); margin-bottom: 14px; }
  .cal-day-header { background: #1a1a2e; color: #fff; padding: 10px 18px; font-size: 14px; font-weight: 700; display: flex; justify-content: space-between; align-items: center; }
  .cal-day-header .day-label { font-size: 11px; color: #7dd3fc; text-transform: uppercase; letter-spacing: 1px; }
  .cal-day-header.today { background: linear-gradient(90deg, #0f3460, #1d4ed8); }
  .cal-event { padding: 12px 18px; border-bottom: 1px solid #f1f5f9; }
  .cal-event:last-child { border-bottom: none; }
  .cal-event .time { font-size: 12px; font-weight: 700; color: #3b82f6; margin-bottom: 3px; }
  .cal-event .summary { font-size: 14px; font-weight: 600; margin-bottom: 4px; }
  .cal-event .detail { font-size: 12px; color: #64748b; margin-bottom: 2px; }
  .cal-event .prep { font-size: 12px; color: #7c3aed; margin-top: 4px; }
  .cal-event .conflict { font-size: 12px; color: #ef4444; font-weight: 600; margin-top: 4px; }
  .no-events { padding: 14px 18px; font-size: 13px; color: #94a3b8; font-style: italic; }

  /* DASHBOARD WIDGETS */
  .dashboard-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-bottom: 14px; }
  .widget { background: #fff; border-radius: 12px; padding: 16px 18px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }
  .widget .w-title { font-size: 11px; text-transform: uppercase; letter-spacing: 0.7px; color: #64748b; margin-bottom: 8px; font-weight: 700; }
  .widget .w-num { font-size: 30px; font-weight: 800; margin-bottom: 4px; }
  .widget .w-sub { font-size: 12px; color: #64748b; }
  .widget.w-red .w-num { color: #ef4444; }
  .widget.w-yellow .w-num { color: #f59e0b; }
  .widget.w-green .w-num { color: #10b981; }
  .widget.w-blue .w-num { color: #3b82f6; }
  .widget.w-purple .w-num { color: #8b5cf6; }

  /* PRIORITY BLOCK */
  .priority-block { background: linear-gradient(135deg, #1a1a2e, #0f3460); color: #fff; border-radius: 16px; padding: 28px 32px; }
  .priority-block h2 { font-size: 18px; font-weight: 700; margin-bottom: 20px; color: #7dd3fc; }
  .priority-item { display: flex; gap: 16px; margin-bottom: 16px; align-items: flex-start; }
  .priority-item:last-child { margin-bottom: 0; }
  .priority-num { background: #0f3460; border: 2px solid #3b82f6; color: #7dd3fc; border-radius: 50%; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 800; flex-shrink: 0; }
  .priority-text strong { font-size: 15px; display: block; margin-bottom: 3px; }
  .priority-text span { font-size: 13px; color: #94a3b8; }

  /* RESCUE NOTICE */
  .rescue-notice { background: #f0fdf4; border: 1px solid #86efac; border-radius: 8px; padding: 8px 12px; font-size: 12px; color: #166534; margin-top: 6px; }

  /* PHISHING NOTICE */
  .phish-notice { background: #fff1f2; border: 1px solid #fca5a5; border-radius: 8px; padding: 8px 12px; font-size: 12px; color: #991b1b; margin-top: 6px; }

  /* DIVIDER */
  .divider { height: 1px; background: #e2e8f0; margin: 8px 0; }

  /* CATEGORY ROW */
  .cat-row { background: #fff; border-radius: 10px; padding: 14px 18px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); margin-bottom: 10px; }
  .cat-row h4 { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
  .cat-row .count-badge { display: inline-block; background: #e2e8f0; color: #334155; font-size: 11px; font-weight: 700; padding: 1px 7px; border-radius: 10px; margin-left: 6px; }
  .cat-row .senders { font-size: 12px; color: #64748b; margin-bottom: 4px; }
  .cat-row .rec { font-size: 13px; font-weight: 600; }

  /* ACCOUNTING TABLE */
  .accounting-table th { background: #0f3460; }
  .accounting-total td { background: #f0f9ff; font-weight: 700; border-top: 2px solid #3b82f6; }

  .note-box { background: #f0fdf4; border: 1px solid #86efac; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #166534; margin-top: 10px; }
  .warn-box { background: #fffbeb; border: 1px solid #fcd34d; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #92400e; margin-top: 10px; }

  a { color: #3b82f6; text-decoration: none; }
  a:hover { text-decoration: underline; }

  @media (max-width: 768px) {
    .two-col, .three-col, .dashboard-grid { grid-template-columns: 1fr; }
    .header { flex-direction: column; gap: 16px; }
    .header-right { text-align: left; }
  }
</style>
</head>
<body>
<div class="page-wrapper">

<!-- ═══════════════════════════════════════════════════
     HEADER
════════════════════════════════════════════════════ -->
<div class="header">
  <div class="header-left">
    <h1>Good morning, Melissa ☀️</h1>
    <p>Your Executive Briefing is ready. Here's everything you need to know.</p>
    <div class="header-stats">
      <div class="stat-pill"><div class="num">50</div><div class="lbl">Emails Reviewed</div></div>
      <div class="stat-pill"><div class="num">10</div><div class="lbl">Calendar Events</div></div>
      <div class="stat-pill"><div class="num">3</div><div class="lbl">Interviews Fri</div></div>
      <div class="stat-pill"><div class="num">5</div><div class="lbl">Action Items</div></div>
    </div>
  </div>
  <div class="header-right">
    <div class="date-badge">
      <div class="dow">Wednesday</div>
      <div class="full-date">September 9, 2026</div>
    </div>
    <div class="byline" style="margin-top:8px;font-size:11px;color:#94a3b8;">Prepared by your Executive Chief of Staff</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 0 — EMAIL TRIAGE QUICK LIST
════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">0</div>
    <h2>Email Triage Quick List</h2>
    <div class="section-line"></div>
  </div>
  <table>
    <thead>
      <tr>
        <th style="width:130px;">Status</th>
        <th style="width:200px;">From</th>
        <th>Subject</th>
        <th>Summary</th>
      </tr>
    </thead>
    <tbody>
      <!-- RESCUED EMAILS FIRST -->
      <tr>
        <td><span class="badge badge-rescued">✅ RESCUED</span></td>
        <td>Center for Veterinary Care</td>
        <td>Autoship of Ursodiol Tablet for Stella</td>
        <td>Upcoming prescription autoship for Stella — important pet health reminder. Rescued from Trash.</td>
      </tr>
      <tr>
        <td><span class="badge badge-rescued">✅ RESCUED</span></td>
        <td>Center for Veterinary Care</td>
        <td>Autoship of Denamarin Chewable Tablets for Stella</td>
        <td>Upcoming prescription autoship for Stella — important pet health reminder. Rescued from Trash.</td>
      </tr>
      <tr>
        <td><span class="badge badge-rescued">✅ RESCUED</span></td>
        <td>ChatGPT / OpenAI</td>
        <td>Check your route before you go</td>
        <td>Protected sender — travel planning tip from OpenAI. Rescued from Trash.</td>
      </tr>
      <tr>
        <td><span class="badge badge-rescued">✅ RESCUED</span></td>
        <td>LinkedIn Job Alerts</td>
        <td>Senior People Partner at Interra Health and 36 more</td>
        <td>36+ new job matches — protected sender. Rescued from Trash.</td>
      </tr>
      <tr>
        <td><span class="badge badge-rescued">✅ RESCUED</span></td>
        <td>Vercel</td>
        <td>New sign-in detected on your Vercel account</td>
        <td>Security alert — new sign-in on melissaw212@gmail.com. Review immediately. Rescued from Trash.</td>
      </tr>
      <tr>
        <td><span class="badge badge-rescued">✅ RESCUED</span></td>
        <td>Match</td>
        <td>You've had a profile view from John</td>
        <td>John, 57, Ronkonkoma NY, viewed your Match profile. Protected sender. Rescued from Trash.</td>
      </tr>
      <!-- INBOX EMAILS -->
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>Bank of America</td>
        <td>A direct deposit was credited to your account</td>
        <td>$760.38 direct deposit (NYS DOL UI) to Personal Checking/Savings Acct #7471.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>Yurii Vlasenko via LinkedIn</td>
        <td>Yurii just messaged you</td>
        <td>1 new LinkedIn message awaiting response from Yurii Vlasenko.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>Anthem Blue Cross Blue Shield</td>
        <td>You have a new explanation of benefits</td>
        <td>New EOB available — log in to review claims details.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>Robinhood</td>
        <td>Your trade confirmations are available</td>
        <td>Recent Robinhood trade confirmations available to view.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>Match</td>
        <td>You've had a profile view from Joe</td>
        <td>Joe, 58, Staten Island NY, viewed your Match profile.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>My Best Buy® Visa® Card (Citi)</td>
        <td>Complete your game-day setup with Best Buy®</td>
        <td>Promotional email — 24-month financing offer for game-day electronics.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>Zoom</td>
        <td>Congratulations! Your seat is reserved!</td>
        <td>Confirmed registration for Claude 101 Workshop INTL — 3-hour webinar.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>Indeed (via Apple relay)</td>
        <td>Senior Director, HR Business Partner @ Vera Therapeutics</td>
        <td>$250K–$285K role — strong match for Melissa's background.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>Brevo</td>
        <td>[Brevo] API Keys will be marked inactive in 7 Days</td>
        <td>Action required — Brevo API keys going inactive. Must respond within 7 days.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>MyDisney via ESPN</td>
        <td>Your one-time passcode for ESPN</td>
        <td>OTP for ESPN login — likely already used. No action needed.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>ESPN Fantasy Games</td>
        <td>Changes Have Been Made to Your ESPN Fantasy Football Draft Settings</td>
        <td>Snake draft scheduled for Wed Sep 09 at 6:30 PM EDT — Fink Family League.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>ESPN Fantasy Games</td>
        <td>You've Successfully Joined your ESPN Fantasy Football League</td>
        <td>Melissa's Magnificent Team joined Fink Family League. Welcome email.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>SHEIN</td>
        <td>Your SHEIN order has been shipped</td>
        <td>SHEIN order shipped — track delivery.</td>
      </tr>
      <tr>
        <td><span class="badge badge-inbox">📥 INBOX</span></td>
        <td>NoReply @ onlinetvsettlement.com</td>
        <td>Biddle v. The Walt Disney Company – Claim Submission Confirmation</td>
        <td>Class action claim submitted. Confirmation code: HTFN3VKX. Save for records.</td>
      </tr>
      <!-- TRASH SUMMARY ROWS -->
      <tr style="background:#fff1f2;">
        <td><span class="badge badge-trashed">🗑 TRASHED (auto)</span></td>
        <td colspan="2"><strong>7 emails auto-trashed (phishing / scam)</strong> — see Trash Review</td>
        <td>Fake payment notifications, spoofed cloud storage threats, casino scams, adult spam, spoofed MyChart prize scam.</td>
      </tr>
      <tr style="background:#f8fafc;">
        <td><span class="badge badge-manual-trash">🗂 TRASH (manual)</span></td>
        <td colspan="2"><strong>23 emails in Trash (manually filtered)</strong> — see Trash Review</td>
        <td>Newsletters, retail promos, job alert digests, LinkedIn digests, miscellaneous subscriptions.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 1 — EXECUTIVE SUMMARY
════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">1</div>
    <h2>Executive Summary</h2>
    <div class="section-line"></div>
  </div>
  <div class="exec-bullets">
    <div class="exec-bullet">
      <div class="icon">🚨</div>
      <div class="text">
        <strong>BIGGEST RISK: Vercel Account Security Alert + 7 Phishing Emails Auto-Trashed</strong>
        <span>A new sign-in was detected on your Vercel account (melissaw212@gmail.com) from an unrecognized location. Review immediately and rotate credentials if you did not initiate this login. Separately, 7 phishing/scam emails were auto-blocked today including fake casino payments, a spoofed cloud storage threat, and adult spam.</span>
      </div>
    </div>
    <div class="exec-bullet">
      <div class="icon">🎯</div>
      <div class="text">
        <strong>BIGGEST OPPORTUNITY: CUNY Vice Chancellor of HR Interview — Friday, September 11</strong>
        <span>You have a confirmed in-person interview at CUNY Central Office this Friday (3:00–5:00 PM) with Elisa Russo and Sujata Malhotra for the Vice Chancellor of Human Resources position. Additionally, a $250K–$285K Senior Director HRBP role at Vera Therapeutics surfaced on Indeed and LinkedIn Job Alerts show 37+ new matches including Senior People Partner roles.</span>
      </div>
    </div>
    <div class="exec-bullet">
      <div class="icon">📅</div>
      <div class="text">
        <strong>BIGGEST CALENDAR ITEM: HR Networking Zoom TODAY at 12:00 PM + Fantasy Football Draft Tonight at 6:30 PM EDT</strong>
        <span>Your HR Networking &amp; Job Search Group Zoom is in ~1 hour (12:00–1:30 PM). RSVP status is "needsAction" — confirm attendance now. Tonight your ESPN Fantasy Football snake draft is scheduled at 6:30 PM EDT. Also, your Brevo API keys expire in 7 days — action required.</span>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 2 — ACTION REQUIRED
════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">2</div>
    <h2>Action Required</h2>
    <div class="section-line"></div>
  </div>

  <div class="card red">
    <span class="card-label label-red">🔴 SECURITY — URGENT</span>
    <h3>Vercel Account: New Sign-In Detected</h3>
    <div class="meta">From: Vercel &lt;notifications@vercel.com&gt; | Wed Sep 9, 2026 | Rescued from Trash</div>
    <div class="why"><strong>Why it matters:</strong> An unrecognized sign-in was detected on your Vercel account (melissaw212@gmail.com). If this wasn't you, your credentials may be compromised. Vercel is connected to your development projects.</div>
    <div class="action">→ Log into Vercel immediately. Check recent activity. If unauthorized: change password, revoke all sessions, enable 2FA if not active.</div>
    <div class="due">⏰ Due: TODAY — Immediately</div>
  </div>

  <div class="card yellow">
    <span class="card-label label-yellow">🟡 RSVP — TODAY</span>
    <h3>HR Networking &amp; Job Search Group Zoom — RSVP Needed</h3>
    <div class="meta">Google Calendar | Today, Wed Sep 9 | 12:00 PM – 1:30 PM EDT | Status: needsAction</div>
    <div class="why"><strong>Why it matters:</strong> This is today at noon — less than 1 hour from now. Your RSVP status is "needsAction." This is a key peer networking call with 170+ HR professionals.</div>
    <div class="action">→ Confirm attendance now. Join link: <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a></div>
    <div class="due">⏰ Due: TODAY at 12:00 PM EDT</div>
  </div>

  <div class="card green">
    <span class="card-label label-green">🟢 INTERVIEW — FRIDAY</span>
    <h3>CUNY Vice Chancellor of Human Resources — In-Person Interview</h3>
    <div class="meta">Google Calendar | Fri Sep 11, 2026 | 3:00 PM – 5:00 PM EDT | CUNY Central Office | Confirmed</div>
    <div class="why"><strong>Why it matters:</strong> This is a prestigious senior executive role. You have two back-to-back interview blocks (3–4 PM and 4–5 PM) with Elisa Russo and Sujata Malhotra. This is an in-person appointment at CUNY Central Office — plan travel accordingly.</div>
    <div class="action">→ Prepare CUNY-specific talking points on HR transformation, DEI, and union relations. Confirm directions to CUNY Central Office. Bring copies of your resume and portfolio. Arrive 15 min early.</div>
    <div class="due">⏰ Due: Friday, September 11 — 3:00 PM EDT</div>
  </div>

  <div class="card yellow">
    <span class="card-label label-yellow">🟡 TECH — 7-DAY DEADLINE</span>
    <h3>Brevo API Keys Going Inactive in 7 Days</h3>
    <div class="meta">From: Brevo &lt;account-alerts@t.brevo.com&gt; | Wed Sep 9, 2026 | Inbox</div>
    <div class="why"><strong>Why it matters:</strong> If your Brevo API keys go inactive, any email automation or marketing workflows you have running through Brevo will break.</div>
    <div class="action">→ Log into Brevo → API &amp; SMTP → Regenerate or activate your API keys before September 16.</div>
    <div class="due">⏰ Deadline: September 16, 2026</div>
  </div>

  <div class="card yellow">
    <span class="card-label label-yellow">🟡 MEDICAL — REVIEW</span>
    <h3>Anthem Blue Cross: New Explanation of Benefits</h3>
    <div class="meta">From: Anthem Blue Cross Blue Shield | Wed Sep 9, 2026 | Inbox</div>
    <div class="why"><strong>Why it matters:</strong> A new EOB is available. Review to confirm claims were processed correctly and identify any unexpected charges or denials.</div>
    <div class="action">→ Log into Anthem member portal to review EOB details and confirm accuracy.</div>
    <div class="due">⏰ Review within 1–2 days</div>
  </div>

  <div class="card yellow">
    <span class="card-label label-yellow">🟡 NETWORKING — RESPOND</span>
    <h3>LinkedIn Message from Yurii Vlasenko</h3>
    <div class="meta">From: LinkedIn | Wed Sep 9, 2026 | Inbox</div>
    <div class="why"><strong>Why it matters:</strong> An unread LinkedIn message is awaiting your response. Given your active job search, this may be a recruiter or potential connection worth engaging.</div>
    <div class="action">→ Open LinkedIn and read/respond to Yurii Vlasenko's message today.</div>
    <div class="due">⏰ Respond: Today or Tomorrow</div>
  </div>

  <div class="card green">
    <span class="card-label label-green">🟢 JOB LEAD — REVIEW</span>
    <h3>Senior Director, HRBP at Vera Therapeutics — $250K–$285K</h3>
    <div class="meta">From: Indeed (via Apple relay) | Wed Sep 9, 2026 | Not in inbox</div>
    <div class="why"><strong>Why it matters:</strong> Compensation is $250K–$285K, strong alignment with your HR executive background. Indeed flagged it as a likely match.</div>
    <div class="action">→ Review job posting on Indeed and apply if aligned with your search criteria.</div>
    <div class="due">⏰ Review: Today or Tomorrow</div>
  </div>

  <div class="card blue">
    <span class="card-label label-blue">🔵 PET HEALTH — AUTOSHIP</span>
    <h3>Stella's Medication Autoship Coming Up (2 Items)</h3>
    <div class="meta">From: Center for Veterinary Care | Wed Sep 9, 2026 | Rescued from Trash</div>
    <div class="why"><strong>Why it matters:</strong> Two prescription medications for Stella (Ursodiol Tablet + Denamarin Chewable Tablets) are coming up for autoship. Ensure payment method is current and the timing is correct.</div>
    <div class="action">→ Verify autoship dates and payment method at your vet portal. Confirm Stella still needs both medications.</div>
    <div class="due">⏰ Review before autoship date</div>
  </div>

  <div class="card yellow">
    <span class="card-label label-yellow">🟡 FINANCIAL — SAVE</span>
    <h3>Class Action Settlement: Biddle v. Walt Disney — Confirmation Code</h3>
    <div class="meta">From: NoReply@onlinetvsettlement.com | Tue Sep 8, 2026 | Inbox</div>
    <div class="why"><strong>Why it matters:</strong> Your claim has been submitted. Save your confirmation code for future reference.</div>
    <div class="action">→ Save confirmation code <strong>HTFN3VKX</strong> to a secure location. Monitor email for payout notices.</div>
    <div class="due">⏰ Save now</div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 3 — FULL 7-DAY CALENDAR
════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">3</div>
    <h2>Full 7-Day Calendar</h2>
    <div class="section-line"></div>
  </div>

  <!-- WEDNESDAY SEP 9 — TODAY -->
  <div class="cal-day">
    <div class="cal-day-header today">
      <span>Wednesday, September 9, 2026</span>
      <span class="day-label">TODAY</span>
    </div>

    <div class="cal-event">
      <div class="time">12:00 PM – 1:30 PM EDT</div>
      <div class="summary">HR Networking &amp; Job Search Group — Zoom (Session 2)</div>
      <div class="detail">📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a> | 170+ HR professionals attending</div>
      <div class="detail">RSVP Status: <span class="badge badge-needs-action">⚠️ Needs Action</span></div>
      <div class="prep">📝 Prep: RSVP immediately. Prepare 30-second intro. Have your job search status ready to share. Review team guidelines via the linked Google Doc in the description.</div>
      <div class="conflict">⚠️ Note: A separate "Network" calendar block is also scheduled at the same time (12:00–1:30 PM) with no details — this appears to be the same event. No conflict.</div>
    </div>

    <div class="cal-event">
      <div class="time">12:00 PM – 1:30 PM EDT</div>
      <div class="summary">Network (Personal Block)</div>
      <div class="detail">📍 No location | No attendees | Status: <span class="badge badge-confirmed">Confirmed</span></div>
      <div class="prep">📝 Likely mirrors the HR Networking Zoom above — treat as same event.</div>
    </div>

    <div class="cal-event">
      <div class="time">6:30 PM EDT</div>
      <div class="summary">🏈 ESPN Fantasy Football Snake Draft — Melissa's Magnificent Team</div>
      <div class="detail">📍 ESPN App / Web | Fink Family League</div>
      <div class="detail">Status: <span class="badge badge-confirmed">Draft Scheduled (Email Confirmed)</span></div>
      <div class="prep">📝 Prep: Review player rankings before 6:30 PM. Have your draft strategy ready. Draft settings were recently updated per the ESPN email.</div>
    </div>
  </div>

  <!-- THURSDAY SEP 10 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span>Thursday, September 10, 2026</span>
      <span class="day-label">TOMORROW</span>
    </div>

    <div class="cal-event">
      <div class="time">9:00 AM – 10:30 AM EDT</div>
      <div class="summary">Executive Roundtable (John Madigan)</div>
      <div class="detail">📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> | Meeting ID: 207 786 667 | Password: 205454</div>
      <div class="detail">RSVP Status: <span class="badge badge-declined">❌ Declined</span></div>
      <div class="prep">📝 You have declined this event. No action required unless you wish to reschedule with John Madigan.</div>
    </div>

    <div class="cal-event">
      <div class="time">12:00 PM – 1:00 PM EDT</div>
      <div class="summary">HR Networking &amp; Job Search: Open Office Hours — Zoom (Session 2)</div>
      <div class="detail">📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a> | 170+ attendees</div>
      <div class="detail">RSVP Status: <span class="badge badge-needs-action">⚠️ Needs Action</span></div>
      <div class="prep">📝 Prep: Note — no AI notetaking tools per organizer request. Open discussion format. Have your job search questions ready. RSVP before the session.</div>
    </div>

    <div class="cal-event">
      <div class="time">1:00 PM – 2:00 PM EDT</div>
      <div class="summary">M&amp;M (Meeting with Monte Montoya)</div>
      <div class="detail">📍 No location specified | Attendee: monte.montoya@gmail.com</div>
      <div class="detail">RSVP Status: <span class="badge badge-accepted">✅ Accepted</span></div>
      <div class="prep">📝 Prep: Confirm agenda with Monte Montoya ahead of time. Check if this is a job search or personal meeting and prepare accordingly.</div>
    </div>
  </div>

  <!-- FRIDAY SEP 11 -->
  <div class="cal-day">
    <div class="cal-day-header" style="background: linear-gradient(90deg, #065f46, #059669);">
      <span>Friday, September 11, 2026</span>
      <span class="day-label" style="color:#d1fae5;">🎯 INTERVIEW DAY</span>
    </div>

    <div class="cal-event">
      <div class="time">9:30 AM – 10:30 AM EDT</div>
      <div class="summary">PT (Physical Therapy / Personal Training)</div>
      <div class="detail">📍 No location | Status: <span class="badge badge-confirmed">Confirmed</span></div>
      <div class="prep">📝 Good timing — before your afternoon interview. Gives you energy and focus for the CUNY meeting.</div>
    </div>

    <div class="cal-event" style="background: #f0fdf4;">
      <div class="time">3:00 PM – 4:00 PM EDT</div>
      <div class="summary">🎯 Vice Chancellor of Human Resources Interview (Block 1)</div>
      <div class="detail">📍 CUNY Central Office | With: Elisa Russo, Sujata Malhotra | Visitor: Melissa Weiss</div>
      <div class="detail">Status: <span class="badge badge-confirmed">✅ Confirmed</span></div>
      <div class="prep">📝 Prep: Prepare CUNY-specific materials — HR transformation, union relations, DEI initiatives, workforce development. Research Elisa Russo and Sujata Malhotra. Bring 3–5 copies of your resume. Plan to arrive by 2:45 PM.</div>
    </div>

    <div class="cal-event" style="background: #f0fdf4;">
      <div class="time">4:00 PM – 5:00 PM EDT</div>
      <div class="summary">🎯 Vice Chancellor of Human Resources Interview (Block 2)</div>
      <div class="detail">📍 CUNY Central Office | Status: <span class="badge badge-accepted">✅ Accepted</span></div>
      <div class="prep">📝 Two back-to-back interview slots — this may be a panel or sequential interview format. Prepare for a 2-hour interview experience. Confirm with CUNY contact what the format will be.</div>
      <div class="conflict">⚠️ Note: Two calendar entries exist for this interview (3–4 PM confirmed, 4–5 PM accepted) — treat as a continuous 2-hour block. No conflict.</div>
    </div>
  </div>

  <!-- SATURDAY SEP 12 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span>Saturday, September 12, 2026</span>
      <span class="day-label">SATURDAY</span>
    </div>
    <div class="no-events">No calendar events scheduled.</div>
  </div>

  <!-- SUNDAY SEP 13 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span>Sunday, September 13, 2026</span>
      <span class="day-label">SUNDAY</span>
    </div>
    <div class="no-events">No calendar events scheduled.</div>
  </div>

  <!-- MONDAY SEP 14 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span>Monday, September 14, 2026</span>
      <span class="day-label">MONDAY</span>
    </div>
    <div class="cal-event">
      <div class="time">8:45 AM – 9:40 AM EDT (Appt Time: 9:00 AM)</div>
      <div class="summary">New Patient Visit — Andrea D. Card</div>
      <div class="detail">📍 53 W 23rd St, 6th Floor, New York NY 10010-4237 | Phone: 212-746-2900</div>
      <div class="detail">Status: <span class="badge badge-accepted">✅ Accepted</span></div>
      <div class="prep">📝 Prep: Arrive by 8:45 AM (15 min early as new patient). Bring insurance card and ID. Note that the office may contact you if additional insurance verification is required. Confirm your insurance is current (check your new Anthem EOB).</div>
    </div>
  </div>

  <!-- TUESDAY SEP 15 -->
  <div class="cal-day">
    <div class="cal-day-header">
      <span>Tuesday, September 15, 2026</span>
      <span class="day-label">TUESDAY</span>
    </div>
    <div class="no-events">No calendar events scheduled.</div>
  </div>

</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 4 — JOB SEARCH & INTERVIEW PIPELINE
════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">4</div>
    <h2>Job Search &amp; Interview Pipeline</h2>
    <div class="section-line"></div>
  </div>

  <table>
    <thead>
      <tr>
        <th>Fit</th>
        <th>Role / Opportunity</th>
        <th>Source</th>
        <th>Compensation</th>
        <th>Status</th>
        <th>Next Step</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="badge badge-high">HIGH</span></td>
        <td><strong>Vice Chancellor of Human Resources</strong><br>CUNY Central Office</td>
        <td>Calendar (Interview Confirmed)</td>
        <td>Not listed</td>
        <td>✅ Interview Confirmed — Fri Sep 11, 3–5 PM</td>
        <td>Prepare materials, research interviewers, confirm CUNY location logistics</td>
      </tr>
      <tr>
        <td><span class="badge badge-high">HIGH</span></td>
        <td><strong>Senior Director, HR Business Partner</strong><br>Vera Therapeutics, Inc.</td>
        <td>Indeed (via Apple relay)</td>
        <td>$250,000 – $285,000/yr</td>
        <td>🔔 New Alert — Not yet applied</td>
        <td>Review posting; apply if aligned</td>
      </tr>
      <tr>
        <td><span class="badge badge-high">HIGH</span></td>
        <td><strong>Senior People Partner</strong><br>Interra Health + 36 more roles</td>
        <td>LinkedIn Job Alerts (Rescued from Trash)</td>
        <td>Varies</td>
        <td>🔔 37 New Matches — Not yet applied</td>
        <td>Review all 37 matches; prioritize top 5</td>
      </tr>
      <tr>
        <td><span class="badge badge-medium">MEDIUM</span></td>
        <td><strong>HR Director — Remote (Law Firm)</strong><br>Capitol Recruiters / Washington DC</td>
        <td>PostJobFree (Dennis Gorelik)</td>
        <td>$150K – $215K++</td>
        <td>🔔 Alert — In Trash</td>
        <td>Review if law firm HR experience aligns; apply if interested</td>
      </tr>
      <tr>
        <td><span class="badge badge-medium">MEDIUM</span></td>
        <td><strong>Chief People Officer / Lead Talent Culture Change</strong><br>Multiple Employers</td>
        <td>JobLeads (In Trash)</td>
        <td>Not listed</td>
        <td>🔔 5 New Matches — In Trash</td>
        <td>Review JobLeads digest for CPO-level matches</td>
      </tr>
      <tr>
        <td><span class="badge badge-low">LOW</span></td>
        <td><strong>Travel and Experience Coordinator</strong><br>3 Dots / New York City</td>
        <td>PostJobFree (In Trash)</td>
        <td>Not listed</td>
        <td>Alert — In Trash</td>
        <td>Likely not aligned with senior HR career. Skip unless pivot intended.</td>
      </tr>
      <tr>
        <td>—</td>
        <td><strong>LinkedIn Message: Yurii Vlasenko</strong></td>
        <td>LinkedIn (Inbox)</td>
        <td>Unknown</td>
        <td>📬 Unread Message</td>
        <td>Open and respond — may be recruiter or networking opportunity</td>
      </tr>
      <tr>
        <td>—</td>
        <td><strong>HR Networking &amp; Job Search Group Zoom</strong><br>170+ HR professionals</td>
        <td>Google Calendar</td>
        <td>N/A</td>
        <td>⚠️ TODAY 12:00 PM — RSVP Needed</td>
        <td>RSVP and attend — strong peer network for HR job search</td>
      </tr>
      <tr>
        <td>—</td>
        <td><strong>Claude 101 Workshop INTL (Webinar)</strong></td>
        <td>Zoom Registration Confirmation (Inbox)</td>
        <td>N/A</td>
        <td>✅ Registered</td>
        <td>Add to calendar; confirm date/time from Zoom confirmation email</td>
      </tr>
      <tr>
        <td>—</td>
        <td><strong>M&amp;M — Monte Montoya</strong></td>
        <td>Google Calendar — Thu Sep 10, 1–2 PM</td>
        <td>N/A</td>
        <td>✅ Accepted</td>
        <td>Confirm agenda; potentially job search related</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 5 — FULL EMAIL REVIEW BY CATEGORY
════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="section-number">5</div>
    <h2>Full Email Review by Category</h2>
    <div class="section-line"></div>
  </div>

  <!-- SECURITY / RISK -->
  <div class="card red">
    <span class="card-label label-red">🔴 Security / Risk</span>
    <h3>Security &amp; Phishing <span class="count-badge" style="background:#fee2e2;color:#b91c1c;font-size:11px;padding:1px 7px;border-radius:10px;font-weight:700;">8 emails</span></h3>
    <div class="meta">Vercel (1 real alert, rescued) + 7 auto-trashed phishing/scam emails</div>
    <div class="divider"></div>

    <div class="rescue-notice">✅ <strong>RESCUED FROM TRASH:</strong> <strong>Vercel</strong> — "New sign-in detected on your Vercel account" — Security alert for melissaw212@gmail.com from new location. <strong>Action: Verify and secure immediately.</strong></div>

    <div style="margin-top:10px;">
      <strong>Auto-Trashed Phishing (7 emails — no further action needed):</strong>
    </div>

    <div class="phish-notice" style="margin-top:8px;">
      🗑 <strong>"Congratulations! You have received a payment $7000.00"</strong> — From: issupportvi@xcgaznlmbhslyuwyxvwutebb.com<br>
      <em>Reason: Fake payment notification from gibberish domain impersonating Casino Yabby. Credential/engagement harvesting.</em>
    </div>
    <div class="phish-notice">
      🗑 <strong>"We've Blocked Your Account! Your photos and videos will be deleted"</strong> — From: qzshmjtyugspcb.13075990805509@tfqlwc.yu9hc6.pcwn1o.us<br>
      <em>Reason: Spoofed cloud storage service with urgent account-threat language, unicode homoglyph obfuscation in sender name, fake payment decline.</em>
    </div>
    <div class="phish-notice">
      🗑 <strong>"48 Hours Left: Claim $15.99 {{Raging Bull Casino}}"</strong> — From: info@qpdstrzqtkyjj (invalid domain)<br>
      <em>Reason: Fake CashApp impersonation with untemplatted variables exposed, casino payment scam.</em>
    </div>
    <div class="phish-notice">
      🗑 <strong>"We have been trying to reach you - melissaw212"</strong> — From: melissaw212@sbnfdazivedir.0048-enterprise-cloud-network-monitoring-center.imperation.org<br>
      <em>Reason: Spoofed MyChart identity from suspicious long domain, fake winner/prize scam targeting user by username.</em>
    </div>
    <div class="phish-notice">
      🗑 <strong>"PORNT5tar 5ecret"</strong> — From: jasupportklvw@tshxqmevbiyyedsdsoxxiqzs.com<br>
      <em>Reason: Adult spam from gibberish domain. Auto-trashed.</em>
    </div>
    <div class="phish-notice">
      🗑 <strong>"Thousands of men are using this trick to increase their size!"</strong> — From: yxztgxkboovwai.31822523420289@uil6ee.j1mxu6.a1qbus.us<br>
      <em>Reason: Adult/enhancement spam from randomized domain. Auto-trashed.</em>
    </div>
    <div class="phish-notice">
      🗑 <strong>"Watch this Alone"</strong> — From: cardsupporthk@duplugwmscpgdbqaoaffygcf.com<br>
      <em>Reason: Adult/clickbait spam from gibberish domain using celebrity name (Kevin Costner). Auto-trashed.</em>
    </div>
    <div class="action" style="margin-top:10px;">→ Secure your Vercel account now. All 7 phishing emails have been removed. No further action needed on those.</div>
  </div>

  <!-- JOB SEARCH -->
  <div class="card green">
    <span class="card-label label-green">🟢 Job Search</span>
    <h3>Job Opportunities &amp; Applications <span class="count-badge" style="background:#d1fae5;color:#065f46;font-size:11px;padding:1px 7px;border-radius:10px;font-weight:700;">3 emails</span></h3>
    <div class="meta">Indeed, LinkedIn Job Alerts, JobLeads</div>
    <div class="divider"></div>
    <table style="margin-top:8px;box-shadow:none;">
      <thead><tr><th>Sender</th><th>Role</th><th>Comp</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>Indeed (Apple relay)</td>
          <td>Senior Director, HRBP @ Vera Therapeutics</td>
          <td>$250K–$285K</td>
          <td>Review &amp; Apply</td>
        </tr>
        <tr>
          <td>LinkedIn Job Alerts <em>(Rescued)</em></td>
          <td>Senior People Partner @ Interra Health + 36 more</td>
          <td>Varies</td>
          <td>Review Top 5 &amp; Apply</td>
        </tr>
        <tr>
          <td>JobLeads <em>(Trash)</em></td>
          <td>CPO / Lead Talent Culture Change — 5 matches</td>
          <td>Not listed</td>
          <td>Review matches</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- RECRUITERS / NETWORKING -->
  <div class="card green">
    <span class="card-label label-green">🟢 Recruiters / Networking</span>
    <h3>Recruiter Outreach &amp; Networking <span class="count-badge" style="background:#d1fae5;color:#065f46;font-size:11px;padding:1px 7px;border-radius:10px;font-weight:700;">3 emails</span></h3>
    <div class="meta">LinkedIn (Yurii Vlasenko message), PostJobFree (Dennis Gorelik x2)</div>
    <div class="divider"></div>
    <p style="font-size:13px;margin-top:6px;"><strong>Yurii Vlasenko via LinkedIn</strong> — Unread message awaiting response (Inbox). Priority: respond today.</p>
    <p style="font-size:13px;margin-top:6px;"><strong>Dennis Gorelik / PostJobFree</strong> — Two job alerts: HR Director Remote (DC, $150K–$215K) and Travel &amp; Experience Coordinator NYC (Trash). Review HR Director role.</p>
    <div class="action" style="margin-top:8px;">→ Respond to Yurii on LinkedIn. Review HR Director posting on PostJobFree.</div>
  </div>

  <!-- CALENDAR / EVENTS -->
  <div class="card blue">
    <span class="card-label label-blue">🔵 Calendar / Events</span>
    <h3>Meetings, Webinars &amp; Events <span class="count-badge" style="background:#dbeafe;color:#1d4ed8;font-size:11px;padding:1px 7px;border-radius:10px;font-weight:700;">2 emails</span></h3>
    <div class="meta">Zoom (Claude 101 Workshop), ESPN Fantasy (Draft + Join)</div>
    <div class="divider"></div>
    <p style="font-size:13px;margin-top:6px;"><strong>Zoom — Claude 101 Workshop INTL:</strong> Seat reserved. 3-hour workshop. Add to calendar.</p>
    <p style="font-size:13px;margin-top:6px;"><strong>ESPN Fantasy Games (2 emails):</strong> Joined Fink Family League (Melissa's Magnificent Team). Snake draft scheduled Wed Sep 9 at 6:30 PM EDT. Draft settings updated.</p>
    <div class="action" style="margin-top:8px;">→ Note draft time tonight. Add Claude 101 webinar to calendar.</div>
  </div>

  <!-- MEDICAL / HEALTH -->
  <div class="card blue">
    <span class="card-label label-blue">🔵 Medical / Health</span>
    <h3
