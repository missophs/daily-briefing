<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa W. — August 26, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page-wrapper { max-width: 1100px; margin: 0 auto; padding: 24px 16px 60px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 16px; padding: 36px 40px 28px; margin-bottom: 28px; box-shadow: 0 8px 32px rgba(0,0,0,0.18); }
  .header h1 { font-size: 2rem; font-weight: 700; letter-spacing: -0.5px; margin-bottom: 4px; }
  .header .subtitle { font-size: 1rem; color: #a8c6fa; margin-bottom: 18px; }
  .header-meta { display: flex; gap: 28px; flex-wrap: wrap; margin-top: 10px; }
  .header-meta-item { background: rgba(255,255,255,0.1); border-radius: 8px; padding: 8px 16px; font-size: 0.85rem; color: #e0e8ff; }
  .header-meta-item strong { color: #fff; display: block; font-size: 1.1rem; }

  /* SECTION HEADERS */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 1.1rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; padding: 10px 18px; border-radius: 8px 8px 0 0; display: flex; align-items: center; gap: 8px; }
  .section-body { background: #fff; border-radius: 0 0 12px 12px; padding: 20px; box-shadow: 0 2px 12px rgba(0,0,0,0.07); }
  .section-title.red { background: #c0392b; color: #fff; }
  .section-title.yellow { background: #f39c12; color: #fff; }
  .section-title.blue { background: #2980b9; color: #fff; }
  .section-title.green { background: #27ae60; color: #fff; }
  .section-title.purple { background: #8e44ad; color: #fff; }
  .section-title.gray { background: #7f8c8d; color: #fff; }
  .section-title.navy { background: #1a1a2e; color: #fff; }
  .section-title.teal { background: #16a085; color: #fff; }
  .section-title.orange { background: #e67e22; color: #fff; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 0.875rem; }
  th { background: #f0f2f5; color: #555; font-weight: 700; text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.5px; padding: 9px 12px; text-align: left; border-bottom: 2px solid #e0e0e0; }
  td { padding: 9px 12px; border-bottom: 1px solid #f0f2f5; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f8f9ff; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 18px; margin-bottom: 14px; border-left: 5px solid; }
  .card-red { background: #fff5f5; border-color: #c0392b; }
  .card-yellow { background: #fffbf0; border-color: #f39c12; }
  .card-blue { background: #f0f6ff; border-color: #2980b9; }
  .card-green { background: #f0fff4; border-color: #27ae60; }
  .card-purple { background: #fdf5ff; border-color: #8e44ad; }
  .card-gray { background: #f8f8f8; border-color: #95a5a6; }
  .card-orange { background: #fff8f0; border-color: #e67e22; }
  .card h3 { font-size: 0.95rem; font-weight: 700; margin-bottom: 6px; }
  .card .meta { font-size: 0.78rem; color: #888; margin-bottom: 6px; }
  .card p { font-size: 0.875rem; margin-bottom: 4px; }
  .card .label { display: inline-block; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; padding: 2px 8px; border-radius: 20px; margin-bottom: 6px; }
  .label-red { background: #fde8e8; color: #c0392b; }
  .label-yellow { background: #fef9e7; color: #b7770d; }
  .label-blue { background: #eaf3ff; color: #2471a3; }
  .label-green { background: #e9f7ef; color: #1d8348; }
  .label-purple { background: #f4ecff; color: #7d3c98; }
  .label-gray { background: #f2f3f4; color: #666; }
  .label-orange { background: #fef0e0; color: #b7530a; }

  /* BADGES */
  .badge { display: inline-block; font-size: 0.7rem; font-weight: 700; padding: 2px 8px; border-radius: 12px; }
  .badge-high { background: #c0392b; color: #fff; }
  .badge-medium { background: #f39c12; color: #fff; }
  .badge-low { background: #95a5a6; color: #fff; }
  .badge-rescued { background: #27ae60; color: #fff; }
  .badge-inbox { background: #2980b9; color: #fff; }
  .badge-trashed { background: #e74c3c; color: #fff; }
  .badge-manual-trash { background: #95a5a6; color: #fff; }

  /* EXEC SUMMARY */
  .exec-bullets { list-style: none; }
  .exec-bullets li { padding: 10px 14px; border-radius: 8px; margin-bottom: 8px; font-size: 0.92rem; display: flex; align-items: flex-start; gap: 10px; }
  .exec-bullets li.risk { background: #fff0f0; border-left: 4px solid #c0392b; }
  .exec-bullets li.opp { background: #f0fff4; border-left: 4px solid #27ae60; }
  .exec-bullets li.cal { background: #f0f6ff; border-left: 4px solid #2980b9; }
  .exec-bullets li span.icon { font-size: 1.2rem; flex-shrink: 0; }

  /* CALENDAR */
  .cal-day { margin-bottom: 18px; }
  .cal-day-header { font-weight: 700; font-size: 0.95rem; color: #1a1a2e; background: #e8edf5; padding: 7px 14px; border-radius: 6px; margin-bottom: 8px; }
  .cal-event { background: #f5f8ff; border-left: 4px solid #2980b9; border-radius: 6px; padding: 10px 14px; margin-bottom: 8px; }
  .cal-event.declined { border-color: #e74c3c; background: #fff5f5; }
  .cal-event.needs-action { border-color: #f39c12; background: #fffbf0; }
  .cal-event.all-day { border-color: #8e44ad; background: #fdf5ff; }
  .cal-event .event-title { font-weight: 700; font-size: 0.92rem; }
  .cal-event .event-meta { font-size: 0.78rem; color: #666; margin-top: 3px; }
  .cal-event .event-tag { display: inline-block; font-size: 0.68rem; font-weight: 700; padding: 1px 7px; border-radius: 10px; margin-left: 8px; }
  .tag-confirmed { background: #d5f5e3; color: #1d8348; }
  .tag-declined { background: #fde8e8; color: #c0392b; }
  .tag-needs-action { background: #fef9e7; color: #b7770d; }

  /* DASHBOARD GRID */
  .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-card { background: #fff; border-radius: 10px; padding: 16px; box-shadow: 0 2px 10px rgba(0,0,0,0.07); border-top: 4px solid; }
  .dash-card.red { border-color: #c0392b; }
  .dash-card.yellow { border-color: #f39c12; }
  .dash-card.blue { border-color: #2980b9; }
  .dash-card.green { border-color: #27ae60; }
  .dash-card.purple { border-color: #8e44ad; }
  .dash-card.gray { border-color: #95a5a6; }
  .dash-card .dash-num { font-size: 2rem; font-weight: 800; line-height: 1; margin-bottom: 4px; }
  .dash-card .dash-label { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.5px; color: #888; margin-bottom: 8px; }
  .dash-card .dash-detail { font-size: 0.8rem; color: #555; }

  /* TRIAGE TABLE */
  .triage-status { font-size: 0.85rem; white-space: nowrap; }
  .triage-from { font-size: 0.82rem; color: #333; }
  .triage-subject { font-size: 0.82rem; font-weight: 600; }
  .triage-summary { font-size: 0.8rem; color: #555; }

  /* PRIORITY TABLE */
  .priority-table td { font-size: 0.85rem; }

  /* TOP 3 */
  .top3 { display: flex; flex-direction: column; gap: 12px; }
  .top3-item { display: flex; align-items: flex-start; gap: 14px; background: #fff; border-radius: 10px; padding: 16px 18px; box-shadow: 0 2px 10px rgba(0,0,0,0.07); }
  .top3-num { font-size: 2rem; font-weight: 900; color: #2980b9; flex-shrink: 0; line-height: 1; }
  .top3-content h4 { font-size: 0.95rem; font-weight: 700; margin-bottom: 4px; }
  .top3-content p { font-size: 0.85rem; color: #555; }

  /* MISC */
  .divider { height: 1px; background: #e0e0e0; margin: 16px 0; }
  .pill { display: inline-block; font-size: 0.7rem; font-weight: 700; padding: 2px 9px; border-radius: 12px; margin: 2px; }
  .pill-green { background: #d5f5e3; color: #1d8348; }
  .pill-red { background: #fde8e8; color: #c0392b; }
  .pill-yellow { background: #fef9e7; color: #b7770d; }
  .pill-gray { background: #f2f3f4; color: #555; }
  .pill-blue { background: #eaf3ff; color: #2471a3; }
  .rescued-note { font-size: 0.75rem; color: #27ae60; font-style: italic; margin-top: 3px; }
  .phishing-note { font-size: 0.75rem; color: #c0392b; font-style: italic; }
  ul.detail-list { padding-left: 18px; margin-top: 6px; }
  ul.detail-list li { font-size: 0.85rem; margin-bottom: 3px; }
  .warn-box { background: #fff0f0; border: 1px solid #e74c3c; border-radius: 8px; padding: 10px 14px; margin-bottom: 10px; font-size: 0.85rem; }
  .info-box { background: #f0f6ff; border: 1px solid #2980b9; border-radius: 8px; padding: 10px 14px; margin-bottom: 10px; font-size: 0.85rem; }
  .success-box { background: #f0fff4; border: 1px solid #27ae60; border-radius: 8px; padding: 10px 14px; margin-bottom: 10px; font-size: 0.85rem; }
  @media (max-width: 700px) {
    .header h1 { font-size: 1.4rem; }
    .header-meta { gap: 12px; }
    table, th, td { font-size: 0.78rem; }
    .dashboard-grid { grid-template-columns: 1fr 1fr; }
  }
</style>
</head>
<body>
<div class="page-wrapper">

  <!-- ═══════════════════════════════════════════════════════
       SECTION 0: EMAIL TRIAGE QUICK LIST
  ═══════════════════════════════════════════════════════ -->
  <div class="section">
    <div class="section-title navy">📋 Email Triage Quick List</div>
    <div class="section-body" style="padding:0;">
      <table>
        <thead>
          <tr>
            <th style="width:120px;">Status</th>
            <th style="width:200px;">From</th>
            <th style="width:260px;">Subject</th>
            <th>Summary</th>
          </tr>
        </thead>
        <tbody>
          <!-- RESCUED emails first -->
          <tr>
            <td><span class="badge badge-rescued">✅ RESCUED</span></td>
            <td class="triage-from">Uber Talent (no-reply@uber.com)</td>
            <td class="triage-subject">Confirm your identity for 301310 - Sr HR Business Partner</td>
            <td class="triage-summary">Identity verification needed for Uber HRBP application — legitimate email rescued from Trash. <span class="rescued-note">Rescued: Official Uber domain, job application identity confirmation.</span></td>
          </tr>
          <tr>
            <td><span class="badge badge-rescued">✅ RESCUED</span></td>
            <td class="triage-from">Mail Delivery Subsystem (mailer-daemon@googlemail.com)</td>
            <td class="triage-subject">Delivery Status Notification (Failure)</td>
            <td class="triage-summary">Melissa's outreach to nneka.ogbourne@mongodb.com bounced — need alternate contact. <span class="rescued-note">Rescued: Bounce notification for job search outreach at MongoDB.</span></td>
          </tr>
          <tr>
            <td><span class="badge badge-rescued">✅ RESCUED</span></td>
            <td class="triage-from">melissa (melissaw212@gmail.com)</td>
            <td class="triage-subject">Built an HRBP bench that lifted promotions 23–32%</td>
            <td class="triage-summary">Melissa's sent outreach to Nneka at MongoDB re: Senior Director HRBP role — keep as record. <span class="rescued-note">Rescued: Melissa's own outreach email, important job search record.</span></td>
          </tr>
          <tr>
            <td><span class="badge badge-rescued">✅ RESCUED</span></td>
            <td class="triage-from">Acorns (acorns@proxyvote.com)</td>
            <td class="triage-subject">Reports for funds in your Acorns portfolio are here</td>
            <td class="triage-summary">Portfolio fund reports available. <span class="rescued-note">Rescued: Financial document, Melissa's own investment account.</span></td>
          </tr>
          <!-- INBOX emails -->
          <tr>
            <td><span class="badge badge-inbox">📥 INBOX</span></td>
            <td class="triage-from">Bank of America</td>
            <td class="triage-subject">A direct deposit was credited to your account</td>
            <td class="triage-summary">$34.33 Venmo cashout deposited to personal checking account ending 7471.</td>
          </tr>
          <tr>
            <td><span class="badge badge-inbox">📥 INBOX</span></td>
            <td class="triage-from">Merrill Lynch</td>
            <td class="triage-subject">VANGUARD FUNDS Important Information</td>
            <td class="triage-summary">Important proxy vote / fund documents available for Vanguard holdings.</td>
          </tr>
          <tr>
            <td><span class="badge badge-inbox">📥 INBOX</span></td>
            <td class="triage-from">Match</td>
            <td class="triage-subject">Buck likes you. See if it's mutual.</td>
            <td class="triage-summary">Match.com notification — Buck liked your profile.</td>
          </tr>
          <tr>
            <td><span class="badge badge-inbox">📥 INBOX</span></td>
            <td class="triage-from">Indeed</td>
            <td class="triage-subject">Vice President, HR @ Thrivent Financial for Lutherans</td>
            <td class="triage-summary">VP HR role, $247K–$371K/yr. Strong match flagged by Indeed based on Melissa's background.</td>
          </tr>
          <tr>
            <td><span class="badge badge-inbox">📥 INBOX</span></td>
            <td class="triage-from">accurateb@myworkday.com</td>
            <td class="triage-subject">Thank You for Your Interest in Accurate Background!</td>
            <td class="triage-summary">Application acknowledgment from Accurate Background — review for outcome.</td>
          </tr>
          <tr>
            <td><span class="badge badge-inbox">📥 INBOX</span></td>
            <td class="triage-from">Robinhood</td>
            <td class="triage-subject">Your trade confirmations are available</td>
            <td class="triage-summary">Recent Robinhood trades confirmed — review for accuracy.</td>
          </tr>
          <tr>
            <td><span class="badge badge-inbox">📥 INBOX</span></td>
            <td class="triage-from">LinkedIn</td>
            <td class="triage-subject">New jobs similar to Regional Senior HR Business Partner – Director at Bozzuto's Inc</td>
            <td class="triage-summary">LinkedIn job alert with Director-level HR roles matching Melissa's target profile.</td>
          </tr>
          <tr>
            <td><span class="badge badge-inbox">📥 INBOX</span></td>
            <td class="triage-from">Apple</td>
            <td class="triage-subject">Your receipt from Apple.</td>
            <td class="triage-summary">Apple Account purchase receipt for "Name my meat" app — verify if intentional.</td>
          </tr>
          <tr>
            <td><span class="badge badge-inbox">📥 INBOX</span></td>
            <td class="triage-from">Match</td>
            <td class="triage-subject">You've had a profile view from Mike</td>
            <td class="triage-summary">Mike, 67, Maltaville NY viewed Melissa's Match profile.</td>
          </tr>
          <tr>
            <td><span class="badge badge-inbox">📥 INBOX</span></td>
            <td class="triage-from">Match</td>
            <td class="triage-subject">Marty likes you. See if it's mutual.</td>
            <td class="triage-summary">Match.com notification — Marty liked your profile.</td>
          </tr>
          <tr>
            <td><span class="badge badge-inbox">📥 INBOX</span></td>
            <td class="triage-from">Uber Talent</td>
            <td class="triage-subject">Your recent job application for 301310 - Sr HR Business Partner</td>
            <td class="triage-summary">Uber confirmed receipt of Sr HRBP application — identity verification also required (see rescued email).</td>
          </tr>
          <tr>
            <td><span class="badge badge-inbox">📥 INBOX</span></td>
            <td class="triage-from">Jo-Anne Kruse via LinkedIn</td>
            <td class="triage-subject">Jo-Anne accepted your invitation, explore their network</td>
            <td class="triage-summary">New LinkedIn connection accepted — Jo-Anne Kruse. Explore her network for opportunities.</td>
          </tr>
          <tr>
            <td><span class="badge badge-inbox">📥 INBOX</span></td>
            <td class="triage-from">Melissa W (melissaw212@gmail.com)</td>
            <td class="triage-subject">GitHub — free-claude-code (1.3B+ free tokens)</td>
            <td class="triage-summary">Melissa emailed herself a GitHub link for free Claude Code tool — personal reference.</td>
          </tr>
          <!-- TRASH SUMMARY ROWS -->
          <tr style="background:#fff8f8;">
            <td><span class="badge badge-trashed">🗑 TRASHED (auto)</span></td>
            <td colspan="2"><strong>6 emails auto-trashed (phishing/spoofed) — see Trash Review</strong></td>
            <td class="triage-summary">SiriusXM spoof, Payment Declined spoof, iCloud security spoof, cloud storage spoof (×2), adult spam. All removed automatically.</td>
          </tr>
          <tr style="background:#f8f8f8;">
            <td><span class="badge badge-manual-trash">🗂 TRASH (manual)</span></td>
            <td colspan="2"><strong>27 emails in Trash — see Trash Review</strong></td>
            <td class="triage-summary">Mix of newsletters, retail promos, adult/casino spam, and subscription marketing. Details in Trash Review section.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════
       SECTION 1: HEADER
  ═══════════════════════════════════════════════════════ -->
  <div class="header">
    <div class="subtitle">Executive Daily Briefing</div>
    <h1>Good Morning, Melissa 👋</h1>
    <div class="header-meta">
      <div class="header-meta-item"><strong>Wednesday</strong>August 26, 2026</div>
      <div class="header-meta-item"><strong>50</strong>Emails Reviewed</div>
      <div class="header-meta-item"><strong>8</strong>Calendar Events</div>
      <div class="header-meta-item"><strong>4</strong>Emails Rescued from Trash</div>
      <div class="header-meta-item"><strong>6</strong>Auto-Trashed (Phishing)</div>
      <div class="header-meta-item"><strong>2</strong>Events Need RSVP</div>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════
       SECTION 2: EXECUTIVE SUMMARY
  ═══════════════════════════════════════════════════════ -->
  <div class="section">
    <div class="section-title red">⚡ Executive Summary</div>
    <div class="section-body">
      <ul class="exec-bullets">
        <li class="risk">
          <span class="icon">🔴</span>
          <div><strong>Biggest Risk:</strong> Six phishing/spoofed emails were auto-trashed today — including fake SiriusXM, fake payment-declined, fake iCloud storage alerts, and adult spam. Additionally, Melissa's outreach email to <strong>nneka.ogbourne@mongodb.com bounced</strong> — that contact is unreachable and needs an alternate path. Action required on Uber identity verification (rescued from trash).</div>
        </li>
        <li class="opp">
          <span class="icon">🟢</span>
          <div><strong>Biggest Opportunity:</strong> Strong job search momentum — <strong>Uber Sr HRBP application</strong> received + identity confirmation needed; <strong>Indeed flagged a VP HR role at Thrivent Financial ($247K–$371K)</strong>; LinkedIn alerts for Director-level HR roles; new connection Jo-Anne Kruse accepted; and Keith Bogen's group posted multiple HR openings including Director of HR at Don Roberto Jewelers.</div>
        </li>
        <li class="cal">
          <span class="icon">🔵</span>
          <div><strong>Biggest Calendar Item:</strong> <strong>TODAY at 12:00 PM</strong> — HR Networking & Job Search Group Zoom (Zoom 2). RSVP is pending (needsAction). Also note: <strong>Amy's anniversary is today</strong> — consider sending a note. Tomorrow's Executive Roundtable has been <strong>declined</strong>, and Christian H's birthday is tomorrow.</div>
        </li>
      </ul>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════
       SECTION 3: ACTION REQUIRED
  ═══════════════════════════════════════════════════════ -->
  <div class="section">
    <div class="section-title yellow">⚠️ Action Required</div>
    <div class="section-body">

      <div class="card card-red">
        <span class="label label-red">🔴 URGENT — Job Search</span>
        <h3>Confirm Your Identity — Uber Sr HR Business Partner Application</h3>
        <div class="meta">From: Uber Talent &lt;no-reply@uber.com&gt; | Rescued from Trash | Wed Aug 26, 2026 3:00 AM</div>
        <p><strong>Why it matters:</strong> Without completing Uber's identity confirmation, your application for Sr HRBP (Req #301310) will not be considered. This is a time-sensitive step from a legitimate Uber domain.</p>
        <p><strong>Recommended Action:</strong> Open the email immediately and complete the identity verification process via Uber's official portal.</p>
        <p><strong>Due:</strong> ASAP — likely short window before application expires.</p>
      </div>

      <div class="card card-red">
        <span class="label label-red">🔴 URGENT — Job Search</span>
        <h3>MongoDB Contact Bounced — Find Alternate Contact for Nneka Ogbourne</h3>
        <div class="meta">From: Mail Delivery Subsystem | Rescued from Trash | Tue Aug 25, 2026</div>
        <p><strong>Why it matters:</strong> Melissa's outreach email to <strong>nneka.ogbourne@mongodb.com</strong> re: Senior Director HRBP role was undeliverable. The address is invalid or inactive.</p>
        <p><strong>Recommended Action:</strong> Search LinkedIn for Nneka Ogbourne at MongoDB. Find a current email or connect directly on LinkedIn. Re-send the outreach via the correct channel.</p>
        <p><strong>Due:</strong> Today or tomorrow — don't let momentum lapse.</p>
      </div>

      <div class="card card-yellow">
        <span class="label label-yellow">⚠️ RSVP Needed — Today</span>
        <h3>HR Networking & Job Search Group — Zoom 2 (TODAY 12–1:30 PM ET)</h3>
        <div class="meta">Google Calendar | Status: needsAction | Wed Aug 26, 12:00–1:30 PM</div>
        <p><strong>Why it matters:</strong> Large HR networking Zoom call (130+ attendees) today at noon. RSVP is still pending. This is a key networking touchpoint during your job search.</p>
        <p><strong>Recommended Action:</strong> RSVP via Google Calendar. Join link: us06web.zoom.us/j/81954171722</p>
        <p><strong>Due:</strong> Before 12:00 PM TODAY.</p>
      </div>

      <div class="card card-yellow">
        <span class="label label-yellow">⚠️ Review — Financial</span>
        <h3>Merrill Lynch — Vanguard Funds Important Information (Proxy Vote)</h3>
        <div class="meta">From: MERRILL LYNCH &lt;id@proxyvote.com&gt; | Inbox | Wed Aug 26, 4:52 AM</div>
        <p><strong>Why it matters:</strong> Proxy voting documents are available for your Vanguard holdings via Merrill Lynch. These may require action before a deadline.</p>
        <p><strong>Recommended Action:</strong> Log into Merrill Lynch portal and review proxy vote documents. Submit vote if a deadline applies.</p>
        <p><strong>Due:</strong> Check for proxy vote deadline — likely within 1–2 weeks.</p>
      </div>

      <div class="card card-green">
        <span class="label label-green">🟢 Opportunity — High Priority</span>
        <h3>Indeed: VP of HR at Thrivent Financial — $247K–$371K/Year</h3>
        <div class="meta">From: Indeed | Inbox | Wed Aug 26, 8:29 AM</div>
        <p><strong>Why it matters:</strong> Indeed flagged this VP HR role as a strong match based on Melissa's background. Salary range is the highest seen in this inbox ($247K–$371K). Thrivent Financial for Lutherans is a Fortune 500-equivalent firm.</p>
        <p><strong>Recommended Action:</strong> Open the Indeed email, review the full job description, and apply today if the role fits.</p>
        <p><strong>Due:</strong> Apply today while the lead is fresh.</p>
      </div>

      <div class="card card-yellow">
        <span class="label label-yellow">⚠️ Review — Apple Receipt</span>
        <h3>Apple Receipt — "Name My Meat" App Purchase</h3>
        <div class="meta">From: Apple &lt;no_reply@email.apple.com&gt; | Inbox | Wed Aug 26, 6:50 AM</div>
        <p><strong>Why it matters:</strong> An Apple purchase receipt was issued today for an app called "Name my meat." Verify this was intentional. If not, it may indicate an unauthorized purchase on your Apple Account.</p>
        <p><strong>Recommended Action:</strong> Check your Apple Account purchase history. If unauthorized, contact Apple Support immediately to dispute the charge.</p>
        <p><strong>Due:</strong> Today.</p>
      </div>

      <div class="card card-green">
        <span class="label label-green">🟢 Opportunity — Networking</span>
        <h3>Jo-Anne Kruse Accepted LinkedIn Invitation — Engage Now</h3>
        <div class="meta">From: LinkedIn | Inbox | Wed Aug 26, 5:05 AM</div>
        <p><strong>Why it matters:</strong> A new LinkedIn connection accepted — strike while it's warm. Explore her network for mutual connections and relevant HR opportunities.</p>
        <p><strong>Recommended Action:</strong> Send Jo-Anne a brief thank-you note on LinkedIn and explore her network. Mention your current search focus.</p>
        <p><strong>Due:</strong> Within 24 hours.</p>
      </div>

      <div class="card card-yellow">
        <span class="label label-yellow">⚠️ Reminder — Personal</span>
        <h3>Amy's Anniversary — Today (Aug 26)</h3>
        <div class="meta">Google Calendar | All-Day Event | Confirmed</div>
        <p><strong>Why it matters:</strong> Amy's anniversary is today. Consider sending a message or card.</p>
        <p><strong>Recommended Action:</strong> Send a congratulatory note, text, or card to Amy today.</p>
        <p><strong>Due:</strong> Today.</p>
      </div>

      <div class="card card-blue">
        <span class="label label-blue">🔵 RSVP Pending — Tomorrow</span>
        <h3>HR Networking & Job Search: Open Office Hours — Zoom 2 (Aug 27, 12–1 PM)</h3>
        <div class="meta">Google Calendar | Status: needsAction | Thu Aug 27, 12:00–1:00 PM</div>
        <p><strong>Why it matters:</strong> Open office hours with HR networking group tomorrow. RSVP is pending. Note: AI notetaking tools asked to be turned off.</p>
        <p><strong>Recommended Action:</strong> RSVP via Google Calendar. Join link: us06web.zoom.us/j/85945371140</p>
        <p><strong>Due:</strong> Before noon tomorrow.</p>
      </div>

      <div class="card card-yellow">
        <span class="label label-yellow">⚠️ Reminder — Financial</span>
        <h3>Transfer Money — Reminder Flagged for Aug 28</h3>
        <div class="meta">Google Calendar | All-Day Event | Confirmed | Aug 28</div>
        <p><strong>Why it matters:</strong> A calendar reminder was set to transfer money on Friday, Aug 28. No additional details are available.</p>
        <p><strong>Recommended Action:</strong> Identify the transfer destination and amount. Execute transfer on or before Aug 28.</p>
        <p><strong>Due:</strong> Friday, August 28.</p>
      </div>

    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════
       SECTION 4: FULL 7-DAY CALENDAR
  ═══════════════════════════════════════════════════════ -->
  <div class="section">
    <div class="section-title blue">📅 Full 7-Day Calendar</div>
    <div class="section-body">

      <!-- WEDNESDAY AUG 26 -->
      <div class="cal-day">
        <div class="cal-day-header">📅 Wednesday, August 26, 2026 — TODAY</div>

        <div class="cal-event all-day">
          <div class="event-title">🎂 Amy's Anniversary <span class="event-tag tag-confirmed">Confirmed</span></div>
          <div class="event-meta">All-Day Event | No location | No attendees</div>
          <div class="event-meta" style="margin-top:4px;"><strong>Prep:</strong> Send a congratulatory message or card today. <span class="pill pill-yellow">ACTION TODAY</span></div>
        </div>

        <div class="cal-event needs-action">
          <div class="event-title">👥 HR Networking & Job Search Group — Zoom 2 <span class="event-tag tag-needs-action">RSVP Pending</span></div>
          <div class="event-meta">12:00 PM – 1:30 PM ET | <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" style="color:#2980b9;">Zoom Link</a> | 130+ attendees</div>
          <div class="event-meta" style="margin-top:4px;"><strong>Prep:</strong> Review HR networking team guidelines (linked in description). Prepare a brief intro and current job search status update. RSVP immediately. <span class="pill pill-red">⚠️ RSVP NEEDED</span></div>
        </div>

        <div class="cal-event">
          <div class="event-title">🌐 Network <span class="event-tag tag-confirmed">Confirmed</span></div>
          <div class="event-meta">12:00 PM – 1:30 PM ET | No location | No attendees listed</div>
          <div class="event-meta" style="margin-top:4px;"><strong>Note:</strong> Overlaps with HR Networking Zoom above — may be the same event or a separate networking block. Confirm before noon. <span class="pill pill-yellow">⚠️ OVERLAP</span></div>
        </div>

        <div class="cal-event">
          <div class="event-title">💅 Nails <span class="event-tag tag-confirmed">Confirmed</span></div>
          <div class="event-meta">3:00 PM – 4:00 PM ET | No location listed</div>
          <div class="event-meta" style="margin-top:4px;"><strong>Prep:</strong> None required. Personal appointment — confirm salon if needed.</div>
        </div>
      </div>

      <!-- THURSDAY AUG 27 -->
      <div class="cal-day">
        <div class="cal-day-header">📅 Thursday, August 27, 2026 — Tomorrow</div>

        <div class="cal-event all-day">
          <div class="event-title">🎂 Christian H's Birthday <span class="event-tag tag-confirmed">Confirmed</span></div>
          <div class="event-meta">All-Day Event | No location | No attendees</div>
          <div class="event-meta" style="margin-top:4px;"><strong>Prep:</strong> Send a birthday message to Christian H. Consider doing this today so you don't forget. <span class="pill pill-yellow">ACTION TONIGHT</span></div>
        </div>

        <div class="cal-event declined">
          <div class="event-title">🚫 Executive Roundtable <span class="event-tag tag-declined">Declined</span></div>
          <div class="event-meta">9:00 AM – 10:30 AM ET | <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" style="color:#c0392b;">Zoom Link</a> | Hosted by John Madigan</div>
          <div class="event-meta" style="margin-top:4px;"><strong>Note:</strong> You have declined this event. No action needed unless you wish to reverse the RSVP. If this was accidental, reach out to John Madigan promptly. <span class="pill pill-red">Declined</span></div>
        </div>

        <div class="cal-event needs-action">
          <div class="event-title">👥 HR Networking & Job Search: Open Office Hours — Zoom 2 <span class="event-tag tag-needs-action">RSVP Pending</span></div>
          <div class="event-meta">12:00 PM – 1:00 PM ET | <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" style="color:#2980b9;">Zoom Link</a> | 130+ attendees</div>
          <div class="event-meta" style="margin-top:4px;"><strong>Prep:</strong> Open informal discussion — no AI notetaking allowed. Come with questions or updates from today's search. RSVP needed. <span class="pill pill-red">⚠️ RSVP NEEDED</span></div>
        </div>
      </div>

      <!-- FRIDAY AUG 28 -->
      <div class="cal-day">
        <div class="cal-day-header">📅 Friday, August 28, 2026</div>

        <div class="cal-event all-day">
          <div class="event-title">💸 Transfer Money <span class="event-tag tag-confirmed">Confirmed</span></div>
          <div class="event-meta">All-Day Reminder | No attendees | No details listed</div>
          <div class="event-meta" style="margin-top:4px;"><strong>Prep:</strong> Identify the transfer amount and destination. Check Bank of America / Robinhood / Acorns accounts as context. Execute on or before this date. <span class="pill pill-yellow">ACTION FRIDAY</span></div>
        </div>
      </div>

      <!-- SAT AUG 29 – TUE SEP 1 -->
      <div class="cal-day">
        <div class="cal-day-header">📅 Saturday, August 29 — Tuesday, September 1, 2026</div>
        <div class="cal-event" style="border-color:#95a5a6; background:#f8f8f8;">
          <div class="event-title" style="color:#666;">No Events Scheduled</div>
          <div class="event-meta">Weekend and early next week are clear based on current calendar data.</div>
        </div>
      </div>

      <!-- NOTE ABOUT PSG MEETING -->
      <div class="info-box" style="margin-top:8px;">
        <strong>📌 Note from Email:</strong> Keith Bogen's email mentions a <strong>PSG of Mercer County Meeting on Thursday, August 28</strong> featuring Career Coach Alan Kirshner — "Ask a Career Coach" session, held in Plainsboro. This is not yet on your calendar. Consider adding it.
      </div>

    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════
       SECTION 5: JOB SEARCH & INTERVIEW PIPELINE
  ═══════════════════════════════════════════════════════ -->
  <div class="section">
    <div class="section-title green">💼 Job Search & Interview Pipeline</div>
    <div class="section-body">

      <div class="card card-red">
        <span class="label label-red">🔴 ACTION TODAY</span>
        <h3>Uber — Sr HR Business Partner (Req #301310)</h3>
        <div class="meta">Source: Uber Talent (uber.com) | Application confirmed + Identity verification rescued from Trash</div>
        <p><strong>Status:</strong> Application received. Identity confirmation email was sent to Melissa but landed in Trash — rescued. Must complete ID verification to be considered.</p>
        <p><strong>Fit:</strong> <span class="badge badge-high">HIGH</span></p>
        <p><strong>Next Step:</strong> Complete Uber identity verification NOW via the rescued email. Do not delay.</p>
      </div>

      <div class="card card-red">
        <span class="label label-red">🔴 BOUNCED — Find Alternate Route</span>
        <h3>MongoDB — Senior Director, HR Business Partner</h3>
        <div class="meta">Source: Melissa's sent email (rescued) + Bounce notification (rescued) | Outreach to nneka.ogbourne@mongodb.com</div>
        <p><strong>Status:</strong> Email bounced. Contact address is invalid or no longer active at MongoDB.</p>
        <p><strong>Fit:</strong> <span class="badge badge-high">HIGH</span></p>
        <p><strong>Next Step:</strong> Search LinkedIn for Nneka Ogbourne at MongoDB. Find current title and contact. Re-send Melissa's strong outreach ("Built an HRBP bench that lifted promotions 23–32%") via correct channel.</p>
      </div>

      <div class="card card-green">
        <span class="label label-green">🟢 APPLY TODAY</span>
        <h3>Thrivent Financial for Lutherans — Vice President, HR</h3>
        <div class="meta">Source: Indeed alert | Salary: $247,496 – $371,243/year | Wed Aug 26</div>
        <p><strong>Status:</strong> Job alert flagged by Indeed as a strong match for Melissa's VP HR background. Highest salary range in today's inbox.</p>
        <p><strong>Fit:</strong> <span class="badge badge-high">HIGH</span></p>
        <p><strong>Next Step:</strong> Open Indeed email → review JD → apply today with tailored resume.</p>
      </div>

      <div class="card card-green">
        <span class="label label-green">🟢 REVIEW</span>
        <h3>SearchPointNY — Executive Vice President of Human Resources</h3>
        <div class="meta">Source: LinkedIn Job Alert | Salary: $175K–$240K/year | Wed Aug 26</div>
        <p><strong>Status:</strong> LinkedIn job alert. EVP-level role, strong salary range, likely a placement firm posting.</p>
        <p><strong>Fit:</strong> <span class="badge badge-high">HIGH</span></p>
        <p><strong>Next Step:</strong> Review full posting on LinkedIn. If compelling, apply or reach out directly.</p>
      </div>

      <div class="card card-green">
        <span class="label label-green">🟢 REVIEW</span>
        <h3>LinkedIn — New Jobs Similar to Regional Senior HR Business Partner – Director (Bozzuto's Inc)</h3>
        <div class="meta">Source: LinkedIn Jobs | Wed Aug 26, 7:05 AM</div>
        <p><strong>Status:</strong> LinkedIn alert with similar Director-level HRBP roles. Review individual listings for fit.</p>
        <p><strong>Fit:</strong> <span class="badge badge-medium">MEDIUM</span> (varies by role)</p>
        <p><strong>Next Step:</strong> Open LinkedIn email → scan job listings → shortlist and apply to strongest matches.</p>
      </div>

      <div class="card card-green">
        <span class="label label-green">🟢 REVIEW</span>
        <h3>Keith Bogen — Director of HR @ Don Roberto Jewelers (San Clemente, CA)</h3>
        <div class="meta">Source: [payitforwardhrjobleads] via groups.io | Wed Aug 26, 3:45 AM | Reports to CFO</div>
        <p><strong>Status:</strong> Apply directly. Director of HR role in CA. No application link provided — apply through company site.</p>
        <p><strong>Fit:</strong> <span class="badge badge-medium">MEDIUM</span> (location: CA)</p>
        <p><strong>Next Step:</strong> Research Don Roberto Jewelers → find HR contact or career page → apply directly.</p>
      </div>

      <div class="card card-green">
        <span class="label label-green">🟢 REVIEW</span>
        <h3>Keith Bogen — Several HR Roles: Baltimore, CA, NJ, Philly, Phoenix, DC (Gilbane + others)</h3>
        <div class="meta">Source: [payitforwardhrjobleads] | Wed Aug 26, 3:37 AM | Hybrid — 3 days/week onsite</div>
        <p><strong>Status:</strong> Multiple open HR roles across several cities. Some with Gilbane. Salary range available in original email.</p>
        <p><strong>Fit:</strong> <span class="badge badge-medium">MEDIUM–HIGH</span> (NJ/NY roles most relevant)</p>
        <p><strong>Next Step:</strong> Open email → identify NJ/NY-area roles → apply to strongest fits.</p>
      </div>

      <div class="card card-gray">
        <span class="label label-gray">⬜ LOW FIT / REVIEW</span>
        <h3>Keith Bogen — Payroll Consultant (Remote, iSolved preferred, 15–20 hrs/week)</h3>
        <div class="meta">Source: [payitforwardhrjobleads] | Wed Aug 26, 3:39 AM | 100% Remote</div>
        <p><strong>Status:</strong> Part-time remote payroll consulting. May not align with Melissa's VP/Director-level target. iSolved experience preferred.</p>
        <p><strong>Fit:</strong> <span class="badge badge-low">LOW</span></p>
        <p><strong>Next Step:</strong> Review if interested in consulting income — otherwise skip.</p>
      </div>

      <div class="card card-yellow">
        <span class="label label-yellow">⚠️ APPLICATION ACKNOWLEDGED</span>
        <h3>Accurate Background — Application Acknowledgment</h3>
        <div class="meta">Source: accurateb@myworkday.com | Inbox | Wed Aug 26, 7:32 AM</div>
        <p><strong>Status:</strong> "Thank you for your interest" email received. Snippet says "After reviewing your resume and experience, we've d..." — likely a decision email (accept or reject). Full email not shown.</p>
        <p><strong>Fit:</strong> <span class="badge badge-medium">MEDIUM</span></p>
        <p><strong>Next Step:</strong> Open full email to determine outcome. If rejection, log it. If interview invitation, prioritize immediately.</p>
      </div>

      <div class="card card-blue">
        <span class="label label-blue">🔵 NETWORKING — TODAY</span>
        <h3>HR Networking & Job Search Group Zoom (12–1:30 PM TODAY)</h3>
        <div class="meta">Source: Google Calendar | 130+ HR professionals | Wed Aug 26</div>
        <p><strong>Status:</strong> Large HR peer networking group. RSVP pending. Strong opportunity to connect, share search status, and learn from peers.</p>
        <p><strong>Next Step:</strong> RSVP and join at noon. Prepare a 30-second intro and your target role description.</p>
      </div>

      <div class="card card-blue">
        <span class="label label-blue">🔵 NETWORKING — NEW CONNECTION</span>
        <h3>Jo-Anne Kruse — LinkedIn Connection Accepted</h3>
        <div class="meta">Source: LinkedIn | Inbox | Wed Aug 26, 5:05 AM</div>
        <p><strong>Status:</strong> New LinkedIn connection. Warm outreach window is open.</p>
        <p><strong>Next Step:</strong> Send a personalized thank-you message on LinkedIn. Share your target role. Ask to connect further or for an introductory call.</p>
      </div>

      <div class="card card-purple">
        <span class="label label-purple">🟣 PROFESSIONAL DEV — CONSIDER ATTENDING</span>
        <h3>PSG of Mercer County — "Ask a Career Coach" with Alan Kirshner (Aug 28, Plainsboro)</h3>
        <div class="meta">Source: David Schuchman via groups.io | Mon Aug 24 | In-person, Plainsboro NJ</div>
        <p><strong>Status:</strong> Free career coaching session this Thursday — not yet on calendar. Relevant for job search strategy.</p>
        <p><strong>Next Step:</strong> Confirm attendance details and add to Google Calendar if planning to attend.</p>
      </div>

    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════
       SECTION 6: FULL EMAIL REVIEW BY CATEGORY
  ═══════════════════════════════════════════════════════ -->
  <div class="section">
    <div class="section-title navy">📂 Full Email Review by Category</div>
    <div class="section-body">

      <!-- SECURITY / RISK -->
      <div class="card card-red">
        <span class="label label-red">🔴 Security / Risk</span>
        <h3>Security / Risk — 7 Emails</h3>
        <div class="divider"></div>
        <p><strong>Auto-Trashed Phishing (6 emails):</strong></p>
        <ul class="detail-list">
          <li><strong>"SiriusXM©"</strong> (spoofed, random domain) — Fake subscription expiration to harvest payment/credentials. <span class="phishing-note">Auto-Trashed: Phishing</span></li>
          <li><strong>"'Payment_Declined'"</strong> (spoofed, random domain) — Fake cloud storage blocking threat. <span class="phishing-note">Auto-Trashed: Phishing</span></li>
          <li><strong>"Cloud®Support-Desk™"</strong> (spoofed, random domain) — Fake iCloud critical alert to harvest credentials. <span class="phishing-note">Auto-Trashed: Phishing</span></li>
          <li><strong>melissaw212 (njdfekjpgoy@rpmd...)</strong> — Spoofed as Melissa's own address, fake cloud storage deletion threat. <span class="phishing-note">Auto-Trashed: Phishing</span></li>
          <li><strong>melissaw212 (zartiqkangl@lwik...)</strong> — Spoofed as Melissa's own address, fake Cloud ID locked threat. <span class="phishing-note">Auto-Trashed: Phishing</span></li>
          <li><strong>"💦FUCK💋ME💦"</strong> (bxsupportpl@vbursvvl...) — Adult spam/phishing. <span class="phishing-note">Not auto-trashed but clearly spam — safely ignored.</span></li>
        </ul>
        <div class="divider"></div>
        <p><strong>Apple Receipt — Verify Purchase (1 email):</strong></p>
        <ul class="detail-list">
          <li><strong>Apple (no_reply@email.apple.com)</strong> — Purchase of "Name my meat" app. From legitimate Apple domain but unusual purchase — verify authorization.</li>
        </ul>
        <p style="margin-top:8px;"><strong>Recommended Action:</strong> No action needed on auto-trashed phishing emails — already removed. Review Apple receipt immediately. If unauthorized, dispute with Apple.</p>
      </div>

      <!-- JOB SEARCH -->
      <div class="card card-green">
        <span class="label label-green">🟢 Job Search — 9 Emails</span>
        <h3>Job Search — 9 Emails</h3>
        <div class="divider"></div>
        <ul class="detail-list">
          <li><strong>Uber Talent</strong> — Application confirmed for Sr HRBP #301310 (Inbox)</li>
          <li><strong>Uber Talent</strong> — Identity confirmation needed for #301310 ✅ Rescued from Trash</li>
          <li><strong>melissa (melissaw212)</strong> — Sent outreach to Nneka at MongoDB re: Sr Director HRBP ✅ Rescued from Trash</li>
          <li><strong>Mail Delivery Subsystem</strong> — Bounce notification for MongoDB outreach ✅ Rescued from Trash</li>
          <li><strong>Indeed</strong> — VP HR at Thrivent Financial, $247K–$371K (Inbox)</li>
          <li><strong>LinkedIn Job Alerts</strong> — EVP HR at SearchPointNY, $175K–$240K (Archive)</li>
          <li><strong>LinkedIn</strong> — New jobs similar to Sr HRBP Director at Bozzuto's (Inbox)</li>
          <li><strong>accurateb@myworkday.com</strong> — Accurate Background application response (Inbox)</li>
          <li><strong>Melissa W (self-sent)</strong> — GitHub link for free Claude Code tool (Inbox — personal reference)</li>
        </ul>
        <p style="margin-top:8px;"><strong>Recommended Action:</strong> Prioritize Uber ID verification → MongoDB alternate contact → Thrivent VP HR application → review LinkedIn + Indeed alerts.</p>
      </div>

      <!-- RECRUITERS / NETWORKING -->
      <div class="card card-green">
        <span class="label label-green">🟢 Recruiters / Networking — 4 Emails</span>
        <h3>Recruiters / Networking — 4 Emails</h3>
        <div class="divider"></div>
        <ul class="detail-list">
          <li><strong>Jo-Anne Kruse via LinkedIn</strong> — LinkedIn invitation accepted (Inbox) — warm outreach window open</li>
          <li><strong>Keith Bogen via groups.io</strong> — Director of HR at Don Roberto Jewelers (Archive)</li>
          <li><strong>Keith Bogen via groups.io</strong> — Payroll Consultant remote role (Archive)</li>
          <li><strong>Keith Bogen via groups.io</strong> — Several HR roles across Baltimore, CA, NJ, Philly, Phoenix, DC (Archive)</li>
        </ul>
        <p style="margin-top:8px;"><strong>Recommended Action:</strong> Message Jo-Anne Kruse on LinkedIn. Review Keith Bogen's postings for NJ/NY fits. Consider attending PSG Mercer County meeting Aug 28.</p>
      </div>

      <!-- CALENDAR / EVENTS -->
      <div class="card card-blue">
        <span class="label label-blue">🔵 Calendar / Events — 1 Email</span>
        <h3>Calendar / Events — 1 Email</h3>
        <div class="divider"></div>
        <ul class="detail-list">
          <li><strong>David Schuchman via groups.io</strong> — PSG of Mercer County Meeting Aug 28: "Ask a Career Coach" with Alan Kirshner (Archive — not in trash)</li>
        </ul>
        <p style="margin-top:8px;"><strong>Recommended Action:</strong> Add to calendar if planning to attend. Session is in Plainsboro, NJ on Thursday August 28.</p>
      </div>

      <!-- FINANCIAL / BILLING -->
      <div class="card card-yellow">
        <span class="label label-yellow">⚠️ Financial / Billing — 4 Emails</span>
        <h3>Financial / Billing — 4 Emails</h3>
        <div class="divider"></div>
        <ul class="detail-list">
          <li><strong>Bank of America</strong> — $34.33 Venmo cashout deposited to checking acct ending 7471 (Inbox)</li>
          <li><strong>Merrill Lynch</strong> — Vanguard Funds proxy vote documents available (Inbox)</li>
          <li><strong>Robinhood</strong> — Trade confirmations available (Inbox)</li>
          <li><strong>Acorns</strong> — Portfolio fund reports available ✅ Rescued from Trash</li>
        </ul>
        <p style="margin-top:8px;"><strong>Recommended Action:</strong> Review Merrill Lynch proxy docs promptly. Check Robinhood trade confirmations for accuracy. Log BofA deposit. Review Acorns fund report.</p>
      </div>

      <!-- PROFESSIONAL DEVELOPMENT -->
      <div class="card card-purple">
        <span class="label label-purple">🟣 Professional Development — 1 Email</span>
        <h3>Professional Development — 1 Email</h3>
        <div class="divider"></div>
        <ul class="detail-list">
          <li><strong>Muse (hello@joinmuse.com)</strong> — Two welcome/verify email emails for a new Muse account (both read, not in inbox or trash). Muse is a job search/career platform. Account appears set up.</li>
        </ul>
        <p style="margin-top:8px;"><strong>Recommended Action:</strong> Confirm Muse account is set up and explore platform for additional job opportunities.</p>
      </div>

      <!-- PERSONAL -->
      <div class="card card-blue">
        <span class="label label-blue">🔵 Personal — 4 Emails</span>
        <h3>Personal — 4 Emails</h3>
        <div class="divider"></div>
        <ul class="detail-list">
          <li><strong>Match (mailer@connect.match.com)</strong> — Buck likes you (Inbox)</li>
          <li><strong>Match (mailer@connect.match.com)</strong> — Marty likes you (Inbox)</li>
          <li><strong>Match (mailer@connect.match.com)</strong> — Mike (67, Maltaville NY) viewed profile (Inbox)</li>
          <li><strong>HomeAgain PetRescuers</strong> — Lost cat Spencer near you, Englewood NJ (Read, archive)</li>
        </ul>
        <p style="margin-top:8px;"><strong>Recommended Action:</strong> Review Match notifications at leisure. If interested in Spencer's case, report sighting to HomeAgain using Ref ID HAP-1942789.
