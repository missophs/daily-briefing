<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa | August 7, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; }
  .page-wrap { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: #fff; border-radius: 14px; padding: 32px 36px 24px; margin-bottom: 24px; }
  .header h1 { font-size: 2rem; font-weight: 700; letter-spacing: -0.5px; }
  .header .subtitle { font-size: 1.05rem; color: #a8c0e8; margin-top: 4px; }
  .header-meta { display: flex; gap: 32px; margin-top: 18px; flex-wrap: wrap; }
  .header-meta-item { background: rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 18px; }
  .header-meta-item .val { font-size: 1.4rem; font-weight: 700; color: #7ecef4; }
  .header-meta-item .lbl { font-size: 0.75rem; color: #a8c0e8; text-transform: uppercase; letter-spacing: 0.5px; }

  /* SECTION TITLES */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 1.05rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; padding: 10px 16px; border-radius: 8px 8px 0 0; margin-bottom: 0; display: flex; align-items: center; gap: 8px; }
  .section-body { background: #fff; border-radius: 0 0 10px 10px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .section-body-standalone { background: #fff; border-radius: 10px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }

  /* COLOR THEMES */
  .red-title { background: #c0392b; color: #fff; }
  .red-card { border-left: 5px solid #c0392b; background: #fff5f5; border-radius: 0 8px 8px 0; padding: 14px 16px; margin-bottom: 12px; }
  .yellow-title { background: #d4a017; color: #fff; }
  .yellow-card { border-left: 5px solid #f0b429; background: #fffdf0; border-radius: 0 8px 8px 0; padding: 14px 16px; margin-bottom: 12px; }
  .blue-title { background: #1565c0; color: #fff; }
  .blue-card { border-left: 5px solid #1976d2; background: #f0f6ff; border-radius: 0 8px 8px 0; padding: 14px 16px; margin-bottom: 12px; }
  .green-title { background: #2e7d32; color: #fff; }
  .green-card { border-left: 5px solid #388e3c; background: #f0fff2; border-radius: 0 8px 8px 0; padding: 14px 16px; margin-bottom: 12px; }
  .purple-title { background: #6a1b9a; color: #fff; }
  .purple-card { border-left: 5px solid #8e24aa; background: #fdf0ff; border-radius: 0 8px 8px 0; padding: 14px 16px; margin-bottom: 12px; }
  .gray-title { background: #607d8b; color: #fff; }
  .gray-card { border-left: 5px solid #90a4ae; background: #f8f9fa; border-radius: 0 8px 8px 0; padding: 14px 16px; margin-bottom: 12px; }
  .orange-title { background: #e65100; color: #fff; }
  .orange-card { border-left: 5px solid #ef6c00; background: #fff8f0; border-radius: 0 8px 8px 0; padding: 14px 16px; margin-bottom: 12px; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #1a1a2e; color: #fff; padding: 9px 12px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
  td { padding: 9px 12px; border-bottom: 1px solid #eee; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f7f9fc; }
  .triage-table th { background: #16213e; }

  /* BADGES */
  .badge { display: inline-block; padding: 2px 9px; border-radius: 20px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.4px; }
  .badge-red { background: #fde8e8; color: #c0392b; }
  .badge-yellow { background: #fff9db; color: #a0690a; }
  .badge-green { background: #e8f5e9; color: #2e7d32; }
  .badge-blue { background: #e3f0ff; color: #1565c0; }
  .badge-gray { background: #eceff1; color: #546e7a; }
  .badge-purple { background: #f3e5f5; color: #6a1b9a; }
  .badge-orange { background: #fff3e0; color: #e65100; }
  .badge-rescued { background: #e8f5e9; color: #1b5e20; border: 1px solid #4caf50; }
  .badge-inbox { background: #e3f0ff; color: #0d47a1; border: 1px solid #2196f3; }
  .badge-trash { background: #eceff1; color: #455a64; }
  .badge-autotrash { background: #fce4ec; color: #880e4f; }

  .priority-high { color: #c0392b; font-weight: 700; }
  .priority-med { color: #d4a017; font-weight: 700; }
  .priority-low { color: #2e7d32; font-weight: 700; }

  /* EXEC SUMMARY */
  .exec-bullets { list-style: none; }
  .exec-bullets li { padding: 12px 16px; border-radius: 8px; margin-bottom: 10px; display: flex; align-items: flex-start; gap: 10px; font-size: 14px; line-height: 1.55; }
  .exec-bullets li.risk { background: #fff0f0; border-left: 4px solid #c0392b; }
  .exec-bullets li.oppty { background: #f0fff4; border-left: 4px solid #2e7d32; }
  .exec-bullets li.cal { background: #f0f6ff; border-left: 4px solid #1565c0; }
  .exec-icon { font-size: 1.3rem; flex-shrink: 0; }

  /* CARD DETAILS */
  .card-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.7px; margin-bottom: 4px; opacity: 0.65; }
  .card-title { font-size: 15px; font-weight: 700; margin-bottom: 6px; }
  .card-row { font-size: 12.5px; margin-bottom: 3px; color: #444; }
  .card-row strong { color: #1a1a2e; }

  /* CALENDAR */
  .cal-day { background: #16213e; color: #fff; border-radius: 8px; padding: 8px 14px; margin: 14px 0 8px; font-weight: 700; font-size: 0.95rem; }
  .cal-event { background: #f0f6ff; border-left: 4px solid #1976d2; border-radius: 0 8px 8px 0; padding: 12px 14px; margin-bottom: 8px; }
  .cal-event.declined { background: #f9f9f9; border-left-color: #bbb; opacity: 0.75; }
  .cal-event.needs-rsvp { background: #fffdf0; border-left-color: #f0b429; }
  .cal-event.all-day { background: #fff0f5; border-left-color: #e91e63; }
  .cal-event-title { font-weight: 700; font-size: 14px; }
  .cal-meta { font-size: 12px; color: #555; margin-top: 4px; }
  .cal-prep { font-size: 12px; color: #c0392b; margin-top: 4px; font-style: italic; }
  .cal-conflict { font-size: 12px; color: #e65100; font-weight: 700; margin-top: 4px; }

  /* DASHBOARD GRID */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }
  .dash-tile { background: #fff; border-radius: 10px; padding: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }
  .dash-tile .tile-num { font-size: 2.2rem; font-weight: 800; line-height: 1; }
  .dash-tile .tile-label { font-size: 11px; text-transform: uppercase; letter-spacing: 0.6px; color: #666; margin-top: 4px; }
  .dash-tile .tile-detail { font-size: 12px; color: #444; margin-top: 8px; line-height: 1.5; }
  .tile-red .tile-num { color: #c0392b; }
  .tile-yellow .tile-num { color: #d4a017; }
  .tile-green .tile-num { color: #2e7d32; }
  .tile-blue .tile-num { color: #1565c0; }
  .tile-purple .tile-num { color: #6a1b9a; }
  .tile-gray .tile-num { color: #607d8b; }

  /* DIVIDER */
  .divider { border: none; border-top: 2px solid #e8ecf0; margin: 22px 0; }

  /* TOP 3 */
  .top3 { display: flex; flex-direction: column; gap: 14px; }
  .top3-item { display: flex; gap: 16px; align-items: flex-start; background: #fff; border-radius: 10px; padding: 16px 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
  .top3-num { font-size: 2rem; font-weight: 900; color: #1a1a2e; opacity: 0.12; line-height: 1; flex-shrink: 0; width: 36px; }
  .top3-content { flex: 1; }
  .top3-content h3 { font-size: 15px; font-weight: 700; margin-bottom: 4px; }
  .top3-content p { font-size: 13px; color: #555; line-height: 1.5; }

  .rescued-note { font-size: 11px; color: #1b5e20; background: #e8f5e9; border: 1px solid #81c784; border-radius: 4px; padding: 2px 7px; display: inline-block; margin-top: 4px; }
  .autotrash-note { font-size: 11px; color: #880e4f; background: #fce4ec; border: 1px solid #f48fb1; border-radius: 4px; padding: 2px 7px; display: inline-block; margin-top: 4px; }
  .spam-warn { font-size: 11px; color: #7b1fa2; background: #f3e5f5; border: 1px solid #ce93d8; border-radius: 4px; padding: 2px 7px; display: inline-block; margin-top: 4px; }

  .small { font-size: 12px; color: #666; }
  .mt4 { margin-top: 4px; }
  .mt8 { margin-top: 8px; }
  .mt12 { margin-top: 12px; }
  .mb4 { margin-bottom: 4px; }
  .bold { font-weight: 700; }
  .italic { font-style: italic; }

  @media (max-width: 600px) {
    .header { padding: 20px; }
    .header h1 { font-size: 1.4rem; }
    .header-meta { gap: 12px; }
    th, td { padding: 7px 8px; font-size: 12px; }
  }
</style>
</head>
<body>
<div class="page-wrap">

<!-- ═══════════════════════════════════════════════
     SECTION 0: EMAIL TRIAGE QUICK LIST
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title blue-title">⚡ Email Triage Quick List</div>
  <div class="section-body" style="padding:0;">
    <table class="triage-table">
      <thead>
        <tr>
          <th style="width:110px;">Status</th>
          <th style="width:200px;">From</th>
          <th>Subject</th>
          <th>Summary</th>
        </tr>
      </thead>
      <tbody>
        <!-- RESCUED -->
        <tr>
          <td><span class="badge badge-rescued">✅ RESCUED</span></td>
          <td>American Airlines</td>
          <td>See what's coming for AAdvantage® members</td>
          <td>Loyalty program update; rescued from Trash — protected sender.</td>
        </tr>
        <!-- INBOX EMAILS -->
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>Bank of America</td>
          <td>Billing Dispute for account -2994 — Request for additional information</td>
          <td>⚠️ Urgent: BofA needs more info (Step 2 of 3) on billing dispute. Action required.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>Anthem Blue Cross Blue Shield</td>
          <td>You have a new explanation of benefits</td>
          <td>New EOB posted — log in to review claims details.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>NY Dept. of Labor</td>
          <td>Invited to the Harlem Recruitment Wednesday! 8/12</td>
          <td>Networking/recruiting event Aug 12 in Harlem — RSVP decision needed.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>LinkedIn Job Alerts</td>
          <td>Global Head of HR (Private Equity) at Empathy Talent — up to $300K/year</td>
          <td>High-fit senior HR role, actively recruiting. Review ASAP.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>Melissa W (self)</td>
          <td>HRBP/Senior HRBP | Howden Re | LinkedIn</td>
          <td>Self-forwarded job link — Howden Re HRBP role. Review and apply.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>Melissa W (self)</td>
          <td>(no subject)</td>
          <td>Self-forwarded LinkedIn job link (view/4450294235). Review and act.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>LinkedIn</td>
          <td>New jobs similar to SVP, Human Resources at Brooklyn Navy Yard</td>
          <td>Job alert digest with similar SVP-level HR roles. Review.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>Jolene A. Yee via LinkedIn</td>
          <td>I'd like to connect 👤</td>
          <td>SVP, General Counsel at Delicato Family Wines wants to connect. High-value contact.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>Dani Pfeiffer via LinkedIn</td>
          <td>Dani accepted your invitation — explore their network</td>
          <td>New LinkedIn connection accepted. Explore their network.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>Acorns</td>
          <td>Reports for funds in your Acorns portfolio are here</td>
          <td>Investment fund reports available. Review when ready.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>HomeAgain PetRescuers</td>
          <td>Luffy, a lost Dog, is missing in your area. Ref. ID: HAP-1922407</td>
          <td>Lost dog near 168 St & Washington Ave, Bronx. Community alert — share if possible.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>Match.com</td>
          <td>You've had a profile view from Ps</td>
          <td>Ps, 65, New York — viewed your profile on Match.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>Match.com</td>
          <td>Melissa, you've still got an unread message</td>
          <td>Unread message waiting on Match. Check when ready.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>OkCupid</td>
          <td>You have an Intro!</td>
          <td>Someone sent you an intro on OkCupid.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>OkCupid</td>
          <td>Someone likes you</td>
          <td>Someone liked your OkCupid profile.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>Grzegorz Sadowski (AppFolio)</td>
          <td>Emergency do to repair main pipeline H line</td>
          <td>Building water shutoff tomorrow (8/7) 10am–1pm, floors 18H+. Already read — note for today.</td>
        </tr>
        <tr>
          <td><span class="badge badge-inbox">📥 INBOX</span></td>
          <td>LinkedIn Job Alerts</td>
          <td>Head of People Operations at Private Company</td>
          <td>Job alert — actively recruiting. Review and consider applying.</td>
        </tr>
        <!-- TRASH SUMMARY ROWS -->
        <tr style="background:#fce4ec;">
          <td><span class="badge badge-autotrash">🗑 AUTO-TRASHED</span></td>
          <td colspan="3"><strong>7 emails auto-trashed</strong> (phishing / spam / newsletters) — see <strong>Trash Review</strong> section below for full details.</td>
        </tr>
        <tr style="background:#f5f5f5;">
          <td><span class="badge badge-trash">🗂 TRASH</span></td>
          <td colspan="3"><strong>~26 emails in Trash</strong> (manually trashed or promotional) — see <strong>Trash Review</strong> section below for full details.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 1: HEADER
═══════════════════════════════════════════════ -->
<div class="header">
  <div class="subtitle">Executive Briefing — Prepared by Your Chief of Staff</div>
  <h1>Good Morning, Melissa ☀️</h1>
  <div class="header-meta">
    <div class="header-meta-item">
      <div class="val">Friday</div>
      <div class="lbl">August 7, 2026</div>
    </div>
    <div class="header-meta-item">
      <div class="val">50</div>
      <div class="lbl">Emails Reviewed</div>
    </div>
    <div class="header-meta-item">
      <div class="val">7</div>
      <div class="lbl">Calendar Events</div>
    </div>
    <div class="header-meta-item">
      <div class="val">5+</div>
      <div class="lbl">Action Items</div>
    </div>
    <div class="header-meta-item">
      <div class="val">⚠️</div>
      <div class="lbl">Security Alerts</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 2: EXECUTIVE SUMMARY
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title red-title">📋 Executive Summary</div>
  <div class="section-body">
    <ul class="exec-bullets">
      <li class="risk">
        <span class="exec-icon">🚨</span>
        <div><strong>Biggest Risk:</strong> Bank of America needs additional information for your billing dispute on account ending -2994 (Step 2 of 3). This is time-sensitive — failure to respond could stall or close your dispute. Also note: multiple phishing/spam emails are in your inbox that were not auto-trashed (Dr. ArthurGreen, Sex_Trick, GLP-1 fakes, Slots of Vegas) and require manual deletion.</div>
      </li>
      <li class="oppty">
        <span class="exec-icon">💼</span>
        <div><strong>Biggest Opportunity:</strong> LinkedIn alert for <strong>Global Head of Human Resources at Empathy Talent</strong> (Private Equity / Financial Services) paying up to <strong>$300K/year</strong> — actively recruiting and highly aligned with your background. Also: your self-forwarded Howden Re HRBP link and a VP of People / Head of People Ops cluster of roles merit immediate review. Jolene A. Yee (SVP, General Counsel, Delicato Family Wines) is requesting a LinkedIn connection — high-value networking opportunity.</div>
      </li>
      <li class="cal">
        <span class="exec-icon">📅</span>
        <div><strong>Biggest Calendar Item:</strong> Your <strong>MRI Brain W&WO IVC</strong> appointment is Tuesday, August 11 at 9:20 AM (arrive 8:50 AM) at 159 E 53rd St, 6th Floor. You also have two unresolved RSVPs on August 12 (HR Networking Zoom) and August 13 (HR Open Office Hours Zoom) — both marked "needsAction." The Executive Roundtable on August 13 shows as <em>declined</em> — confirm that was intentional.</div>
      </li>
    </ul>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 3: ACTION REQUIRED
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title yellow-title">⚡ Action Required</div>
  <div class="section-body">

    <div class="yellow-card">
      <div class="card-label">🏦 Financial / Billing</div>
      <div class="card-title">Bank of America Billing Dispute — Account -2994 (Step 2 of 3)</div>
      <div class="card-row"><strong>Source:</strong> onlinebanking@ealerts.bankofamerica.com — received 8/7/2026</div>
      <div class="card-row"><strong>Why it matters:</strong> BofA is requesting additional information to proceed with your billing dispute. Step 2 of 3 — if you miss this, the dispute may be closed in the merchant's favor.</div>
      <div class="card-row"><strong>Next Step:</strong> Log in to BofA online banking and submit the required documentation today. Confirm email is from legitimate BofA domain before clicking links — this one appears legitimate.</div>
      <div class="card-row"><strong>Due:</strong> As soon as possible — today if possible</div>
    </div>

    <div class="green-card">
      <div class="card-label">💼 Job Search — HIGH FIT</div>
      <div class="card-title">Global Head of HR at Empathy Talent — Up to $300K/year</div>
      <div class="card-row"><strong>Source:</strong> LinkedIn Job Alerts — jobalerts-noreply@linkedin.com</div>
      <div class="card-row"><strong>Why it matters:</strong> Private Equity, Investment Management, Financial Services focus — actively recruiting. Compensation up to $300K/year. High alignment with your SVP/CHRO-level background.</div>
      <div class="card-row"><strong>Next Step:</strong> Review the full listing on LinkedIn today and submit a tailored application. Note the PE/IM requirement in your cover letter.</div>
      <div class="card-row"><strong>Due:</strong> Review today; apply ASAP — actively recruiting</div>
    </div>

    <div class="green-card">
      <div class="card-label">💼 Job Search — Self-Forwarded Leads</div>
      <div class="card-title">Two Self-Forwarded LinkedIn Job Links — Howden Re HRBP + Unknown Role</div>
      <div class="card-row"><strong>Source:</strong> Melissa W (melissaw212@gmail.com) — two emails forwarded to yourself</div>
      <div class="card-row"><strong>Why it matters:</strong> You bookmarked these yourself — Howden Re HRBP/Senior HRBP and a second LinkedIn job (ID: 4450294235). These were clearly flagged for follow-through.</div>
      <div class="card-row"><strong>Next Step:</strong> Open both LinkedIn links, review job descriptions, and decide whether to apply. Set a reminder if not applying today.</div>
      <div class="card-row"><strong>Due:</strong> Today — before weekend</div>
    </div>

    <div class="yellow-card">
      <div class="card-label">📅 Calendar RSVP</div>
      <div class="card-title">HR Networking & Job Search Group — Zoom (Aug 12, 12–1:30 PM)</div>
      <div class="card-row"><strong>Source:</strong> Google Calendar — status: needsAction</div>
      <div class="card-row"><strong>Why it matters:</strong> Large peer networking group with 150+ HR professionals. Your attendance status is unconfirmed — organizer is waiting.</div>
      <div class="card-row"><strong>Next Step:</strong> Accept or decline the calendar invite. Link: https://us06web.zoom.us/j/81954171722</div>
      <div class="card-row"><strong>Due:</strong> RSVP today</div>
    </div>

    <div class="yellow-card">
      <div class="card-label">📅 Calendar RSVP</div>
      <div class="card-title">HR Networking Open Office Hours — Zoom (Aug 13, 12–1 PM)</div>
      <div class="card-row"><strong>Source:</strong> Google Calendar — status: needsAction</div>
      <div class="card-row"><strong>Why it matters:</strong> Open discussion format for job search support — same large HR peer group. Note: AI notetaking tools are prohibited per organizer's request.</div>
      <div class="card-row"><strong>Next Step:</strong> Accept or decline. Zoom: https://us06web.zoom.us/j/85945371140</div>
      <div class="card-row"><strong>Due:</strong> RSVP today</div>
    </div>

    <div class="blue-card">
      <div class="card-label">🏥 Medical</div>
      <div class="card-title">MRI Brain W&WO IVC — Tuesday Aug 11, Arrive 8:50 AM</div>
      <div class="card-row"><strong>Source:</strong> Google Calendar (confirmed)</div>
      <div class="card-row"><strong>Why it matters:</strong> Medical appointment with strict arrival time — 30 min before scan start. Remove all body piercings/metal beforehand. Lockers available. Leave valuables at home.</div>
      <div class="card-row"><strong>Next Step:</strong> Confirm transportation to 159 E 53rd St, 6th Floor, NYC. Phone: 646-754-2800. Remove metal/piercings morning of.</div>
      <div class="card-row"><strong>Due:</strong> Tuesday, August 11 — arrive 8:50 AM</div>
    </div>

    <div class="red-card">
      <div class="card-label">🗑 Inbox Cleanup — Spam/Phishing</div>
      <div class="card-title">Multiple Spam/Phishing Emails Still in Inbox — Manual Deletion Required</div>
      <div class="card-row"><strong>Source:</strong> Various fraudulent senders (Dr. ArthurGreen, Sex_Trick, GLP-1 DirectMeds x3, Medvi, Slots of Vegas, Match profile from Adam — not in inbox)</div>
      <div class="card-row"><strong>Why it matters:</strong> Several explicit spam/phishing emails bypassed auto-trash and are sitting unread. These carry reputational and security risk if accidentally clicked. One was tagged auto-trashed (Cloud.Security phishing) but others were not.</div>
      <div class="card-row"><strong>Next Step:</strong> Delete/report as spam: Dr. ArthurGreen (x2), Sex_Trick, Sex_Without_Censorship, GLP-1 DirectMeds (x3), Medvi GLP-1, Slots of Vegas. Mark sender domains as spam.</div>
      <div class="card-row"><strong>Due:</strong> Today</div>
    </div>

    <div class="yellow-card">
      <div class="card-label">🔗 Professional Networking</div>
      <div class="card-title">Jolene A. Yee (SVP, General Counsel, Delicato Family Wines) — LinkedIn Connection Request</div>
      <div class="card-row"><strong>Source:</strong> invitations@linkedin.com</div>
      <div class="card-row"><strong>Why it matters:</strong> SVP-level executive from a notable company reaching out. Could open wine/beverage industry HR doors or expand your C-suite network.</div>
      <div class="card-row"><strong>Next Step:</strong> Accept and send a brief personalized message noting your HR background and interest in connecting.</div>
      <div class="card-row"><strong>Due:</strong> Within 24–48 hours</div>
    </div>

    <div class="blue-card">
      <div class="card-label">🏥 Insurance</div>
      <div class="card-title">Anthem Blue Cross — New Explanation of Benefits Posted</div>
      <div class="card-row"><strong>Source:</strong> DoNotReply-MemberComm@email.anthem.com</div>
      <div class="card-row"><strong>Why it matters:</strong> New EOB = a claim was processed. Review to confirm accuracy and check for any balance due or errors.</div>
      <div class="card-row"><strong>Next Step:</strong> Log in to Anthem account and review the EOB. File any corrections if needed.</div>
      <div class="card-row"><strong>Due:</strong> This week</div>
    </div>

    <div class="blue-card">
      <div class="card-label">🏠 Building / Utilities</div>
      <div class="card-title">Water Shutoff TODAY — 10 AM to 1 PM (Floors 18H and Up)</div>
      <div class="card-row"><strong>Source:</strong> Grzegorz Sadowski via AppFolio — already read</div>
      <div class="card-row"><strong>Why it matters:</strong> Main pipeline repair — no water in both bathrooms, sinks, toilets, or showers from 10 AM–1 PM today.</div>
      <div class="card-row"><strong>Next Step:</strong> Plan accordingly — shower/use facilities before 10 AM. Fill water bottles if needed. Already read, so you may already know.</div>
      <div class="card-row"><strong>Due:</strong> TODAY — 10 AM</div>
    </div>

    <div class="gray-card">
      <div class="card-label">📅 State Farm Bill</div>
      <div class="card-title">State Farm Bill — Due Today (Aug 7 All-Day Event)</div>
      <div class="card-row"><strong>Source:</strong> Google Calendar (confirmed)</div>
      <div class="card-row"><strong>Why it matters:</strong> Bill payment reminder on your calendar — confirm whether it auto-pays or requires manual action.</div>
      <div class="card-row"><strong>Next Step:</strong> Confirm payment is scheduled or submit manually through State Farm portal.</div>
      <div class="card-row"><strong>Due:</strong> Today, August 7</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 4: FULL 7-DAY CALENDAR
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title blue-title">📅 Full 7-Day Calendar</div>
  <div class="section-body">

    <div class="cal-day">📅 Friday, August 7, 2026 — TODAY</div>

    <div class="cal-event all-day">
      <div class="cal-event-title">💳 State Farm Bill — Payment Due</div>
      <div class="cal-meta">⏰ All Day &nbsp;|&nbsp; 📍 No location &nbsp;|&nbsp; ✅ Confirmed</div>
      <div class="cal-prep">⚡ Action: Confirm payment is processing or submit manually. Do not let this lapse.</div>
    </div>

    <div class="cal-event">
      <div class="cal-event-title">🔧 Building Water Shutoff — Main Pipeline Repair</div>
      <div class="cal-meta">⏰ 10:00 AM – 1:00 PM &nbsp;|&nbsp; 📍 Your Building (Floors 18H and above)</div>
      <div class="cal-meta">From: AppFolio notice — Grzegorz Sadowski</div>
      <div class="cal-prep">⚡ No water in bathrooms, sinks, toilets, showers. Plan ahead — shower before 10 AM.</div>
    </div>

    <div class="cal-day">📅 Saturday, August 8 – Monday, August 10, 2026</div>
    <div class="gray-card" style="margin:0 0 8px;">
      <div class="small">No calendar events scheduled for Saturday Aug 8 through Monday Aug 10. State Farm billing event ends Aug 8 (end date of all-day event). Use the weekend to prepare for Tuesday's MRI and to review job applications.</div>
    </div>

    <div class="cal-day">📅 Tuesday, August 11, 2026</div>

    <div class="cal-event">
      <div class="cal-event-title">🧠 MRI Brain W&WO IVC</div>
      <div class="cal-meta">⏰ Arrive: 8:50 AM &nbsp;|&nbsp; Appointment: 9:20 AM – 9:40 AM &nbsp;|&nbsp; ✅ Confirmed</div>
      <div class="cal-meta">📍 159 E 53rd Street, 6th Floor, New York, NY 10022 &nbsp;|&nbsp; ☎️ 646-754-2800</div>
      <div class="cal-prep">⚡ Prep: Arrive by 8:50 AM. MRI-safe gown provided. Private dressing rooms with lockers available. Remove ALL body piercings and metal before scan. Leave valuables at home. Plan transit to arrive early.</div>
    </div>

    <div class="cal-day">📅 Wednesday, August 12, 2026</div>

    <div class="cal-event">
      <div class="cal-event-title">🏋️ PT (Physical Therapy)</div>
      <div class="cal-meta">⏰ 9:30 AM – 10:30 AM &nbsp;|&nbsp; ✅ Confirmed</div>
      <div class="cal-meta">📍 No location listed</div>
      <div class="cal-prep">⚡ Back-to-back with networking Zoom at noon — schedule travel/rest between appointments.</div>
    </div>

    <div class="cal-event needs-rsvp">
      <div class="cal-event-title">🤝 HR Networking &amp; Job Search Group — Zoom Session 2</div>
      <div class="cal-meta">⏰ 12:00 PM – 1:30 PM &nbsp;|&nbsp; ⚠️ RSVP: needsAction</div>
      <div class="cal-meta">📍 <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1" target="_blank">Zoom Link</a> &nbsp;|&nbsp; 150+ attendees</div>
      <div class="cal-prep">⚡ RSVP TODAY. Review team guidelines and resources before joining. Large peer HR group — excellent networking opportunity during job search.</div>
      <div class="cal-conflict">⚠️ Note: Harlem Recruitment Event (from NYS DOL email) also on Aug 12 — confirm no time conflict.</div>
    </div>

    <div class="cal-event">
      <div class="cal-event-title">📋 Network (Personal Note)</div>
      <div class="cal-meta">⏰ 12:00 PM – 1:30 PM &nbsp;|&nbsp; ✅ Confirmed</div>
      <div class="cal-meta">📍 No location listed (likely a personal reminder matching the HR Networking Zoom above)</div>
      <div class="cal-prep">⚡ Appears to overlap with HR Networking Zoom. Treat as a reminder to attend same session. No action needed if attending the Zoom above.</div>
      <div class="cal-conflict">⚠️ Possible duplicate of HR Networking Zoom — verify and remove if redundant.</div>
    </div>

    <div class="cal-day">📅 Thursday, August 13, 2026</div>

    <div class="cal-event declined">
      <div class="cal-event-title">🚫 Executive Roundtable (DECLINED)</div>
      <div class="cal-meta">⏰ 9:00 AM – 10:30 AM &nbsp;|&nbsp; ❌ Status: Declined</div>
      <div class="cal-meta">📍 <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09" target="_blank">Zoom Link</a> — Meeting ID: 207 786 667 / PW: 205454</div>
      <div class="cal-meta">Invited by: John Madigan</div>
      <div class="cal-prep">⚡ You declined this event. If this was accidental, reach out to John Madigan to request reinstatement. Otherwise, no action needed.</div>
    </div>

    <div class="cal-event needs-rsvp">
      <div class="cal-event-title">🤝 HR Networking &amp; Job Search: Open Office Hours — Zoom</div>
      <div class="cal-meta">⏰ 12:00 PM – 1:00 PM &nbsp;|&nbsp; ⚠️ RSVP: needsAction</div>
      <div class="cal-meta">📍 <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1" target="_blank">Zoom Link</a> &nbsp;|&nbsp; 150+ attendees</div>
      <div class="cal-prep">⚡ RSVP TODAY. Note: Organizer requests NO automated AI notetaking tools. Open discussion format — great for 1:1 connection follow-ups from Aug 12 session.</div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 5: JOB SEARCH & INTERVIEW PIPELINE
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title green-title">💼 Job Search & Interview Pipeline</div>
  <div class="section-body">

    <div class="green-card">
      <div class="card-label">🔥 HIGH FIT — Actively Recruiting</div>
      <div class="card-title">Global Head of Human Resources — Empathy Talent (Private Equity / Financial Services)</div>
      <div class="card-row"><strong>Source:</strong> LinkedIn Job Alerts</div>
      <div class="card-row"><strong>Compensation:</strong> Up to $300,000/year</div>
      <div class="card-row"><strong>Requirement:</strong> PE, Investment Management, Financial Services experience a MUST</div>
      <div class="card-row"><strong>Status:</strong> Actively recruiting — apply immediately</div>
      <div class="card-row"><strong>Action:</strong> Tailor resume to PE/IM language. Apply today.</div>
    </div>

    <div class="green-card">
      <div class="card-label">🔥 HIGH FIT — Self-Identified</div>
      <div class="card-title">HRBP / Senior HRBP — Howden Re</div>
      <div class="card-row"><strong>Source:</strong> Self-forwarded email (melissaw212@gmail.com) — LinkedIn job ID: 4449108141</div>
      <div class="card-row"><strong>Status:</strong> You flagged this yourself — strong signal of interest</div>
      <div class="card-row"><strong>Action:</strong> Open LinkedIn link, review full JD, apply if fit confirmed.</div>
    </div>

    <div class="green-card">
      <div class="card-label">🔥 HIGH FIT — Self-Identified</div>
      <div class="card-title">Unknown Role — LinkedIn Job View #4450294235</div>
      <div class="card-row"><strong>Source:</strong> Self-forwarded email (melissaw212@gmail.com)</div>
      <div class="card-row"><strong>Status:</strong> You bookmarked this — review the full listing</div>
      <div class="card-row"><strong>Action:</strong> Open https://www.linkedin.com/jobs/view/4450294235/ — apply or save for follow-up.</div>
    </div>

    <div class="green-card">
      <div class="card-label">🟡 MEDIUM FIT — SVP-Level Alert</div>
      <div class="card-title">SVP Human Resources (Similar Roles) — Brooklyn Navy Yard Development Corporation cluster</div>
      <div class="card-row"><strong>Source:</strong> LinkedIn — jobs-noreply@linkedin.com</div>
      <div class="card-row"><strong>Status:</strong> Job alert digest — multiple similar SVP HR roles</div>
      <div class="card-row"><strong>Action:</strong> Review digest and cherry-pick best-fit roles for application this week.</div>
    </div>

    <div class="green-card">
      <div class="card-label">🟡 MEDIUM FIT — People Ops</div>
      <div class="card-title">Head of People Operations — Private Company</div>
      <div class="card-row"><strong>Source:</strong> LinkedIn Job Alerts — already in inbox, marked not read</div>
      <div class="card-row"><strong>Status:</strong> Actively recruiting</div>
      <div class="card-row"><strong>Action:</strong> Review company details on LinkedIn. Apply if company/comp aligns.</div>
    </div>

    <div class="green-card">
      <div class="card-label">🟡 MEDIUM FIT — CPO Role</div>
      <div class="card-title">Chief People Officer / Lead Talent Culture Change — 5 New Matches</div>
      <div class="card-row"><strong>Source:</strong> JobLeads (mailer@jobleads.com) — in Trash</div>
      <div class="card-row"><strong>Status:</strong> Based on your saved search for "Chief People Officer Lead Talent Culture Change" — 5 new matches Aug 7</div>
      <div class="card-row"><strong>Action:</strong> Rescue email from Trash or log in to JobLeads to review matches before they expire.</div>
    </div>

    <div class="green-card">
      <div class="card-label">🟢 LOW-MEDIUM FIT — Tech Company</div>
      <div class="card-title">Senior People Partner, Technology — MrBeast</div>
      <div class="card-row"><strong>Source:</strong> LinkedIn Job Alerts (already read — not in inbox)</div>
      <div class="card-row"><strong>Status:</strong> 2 school alumni at MrBeast. Already seen.</div>
      <div class="card-row"><strong>Action:</strong> Review if tech/content creator industry interests you. Lower priority vs. financial services roles.</div>
    </div>

    <div class="green-card">
      <div class="card-label">🟢 LOW-MEDIUM FIT</div>
      <div class="card-title">VP of People — Nitra</div>
      <div class="card-row"><strong>Source:</strong> LinkedIn Job Alerts (already read — not in inbox)</div>
      <div class="card-row"><strong>Status:</strong> 1 school alum. Already seen.</div>
      <div class="card-row"><strong>Action:</strong> Review Nitra's profile and determine fit. Lower priority if fintech isn't a target.</div>
    </div>

    <div class="section" style="margin-top:16px; margin-bottom:0;">
      <div style="font-weight:700; font-size:13px; margin-bottom:8px; color:#1a1a2e;">🤝 Networking & Connection Updates</div>
      <table>
        <thead>
          <tr><th>Contact</th><th>Action</th><th>Priority</th></tr>
        </thead>
        <tbody>
          <tr>
            <td>Jolene A. Yee — SVP, General Counsel, Delicato Family Wines</td>
            <td>Incoming LinkedIn connection request — accept &amp; personalize message</td>
            <td><span class="priority-high">HIGH</span></td>
          </tr>
          <tr>
            <td>Dani Pfeiffer — LinkedIn</td>
            <td>Accepted your connection. Explore their network &amp; send thank-you note.</td>
            <td><span class="priority-med">MEDIUM</span></td>
          </tr>
          <tr>
            <td>HR Networking Group — Zoom (Aug 12)</td>
            <td>RSVP needed — 150+ HR peers, job search group</td>
            <td><span class="priority-high">HIGH</span></td>
          </tr>
          <tr>
            <td>HR Open Office Hours — Zoom (Aug 13)</td>
            <td>RSVP needed — no AI recording tools</td>
            <td><span class="priority-high">HIGH</span></td>
          </tr>
          <tr>
            <td>Harlem Recruitment Event — Aug 12 (NYS DOL)</td>
            <td>In-person networking event, same day as HR Zoom — check times and attend if feasible</td>
            <td><span class="priority-med">MEDIUM</span></td>
          </tr>
        </tbody>
      </table>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 6: FULL EMAIL REVIEW BY CATEGORY
═══════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title red-title">📂 Full Email Review by Category</div>
  <div class="section-body">

    <!-- SECURITY / RISK -->
    <div class="red-card">
      <div class="card-label">🔴 Security / Risk</div>
      <div class="card-title">Security / Risk — 7 Emails</div>
      <div class="card-row"><strong>Count:</strong> 7 (1 auto-trashed phishing + 6 spam/scam still untrashed)</div>
      <table style="margin-top:10px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td>Cloud.Security (spoof)</td>
            <td>FINAL NOTICE: Your photos will be deleted tonight</td>
            <td><span class="autotrash-note">🗑 Auto-Trashed — Phishing</span></td>
            <td>No action — removed automatically. Fake cloud storage credential harvest.</td>
          </tr>
          <tr>
            <td>Dr. ArthurGreen (er95ytdhte@66ynzvic5k.us)</td>
            <td>Add 3.8 inches naturally with this $3 method 🍆</td>
            <td><span class="badge badge-red">Spam — Inbox</span></td>
            <td>Delete immediately. Report as spam.</td>
          </tr>
          <tr>
            <td>Dr. ArthurGreen (nggg6qa604@scimpnt7mn.us)</td>
            <td>Add 3.8 inches naturally with this $3 method 🍆</td>
            <td><span class="badge badge-red">Spam — Not Inbox</span></td>
            <td>Delete immediately. Report as spam.</td>
          </tr>
          <tr>
            <td>Sex_Trick (p637qgeoj6@ph9iftpm8g.us)</td>
            <td>Make her squirt 3x tonight 🔥 with this military mixture</td>
            <td><span class="badge badge-red">Explicit Spam</span></td>
            <td>Delete immediately. Report as spam.</td>
          </tr>
          <tr>
            <td>Sex_Without_Censorship (szpucr@kfrvoftsdlopjdlbjcitapumcp.net)</td>
            <td>Sydney Sweeney's secret that keeps men hard for hours</td>
            <td><span class="badge badge-red">Explicit Spam</span></td>
            <td>Delete immediately. Report as spam.</td>
          </tr>
          <tr>
            <td>Slots Of Vegas Casino (spoofed address)</td>
            <td>Your 150 FREESPINS have been reserved</td>
            <td><span class="badge badge-red">Phishing / Scam</span></td>
            <td>Delete. Do not click. Fake casino credential harvest.</td>
          </tr>
          <tr>
            <td>'MEDVI' (info@htjnzxegdngiv — invalid domain)</td>
            <td>Lose weight with Medvi — or get your money back</td>
            <td><span class="badge badge-red">Spam / Scam</span></td>
            <td>Delete. Spoofed sender with invalid domain.</td>
          </tr>
        </tbody>
      </table>
      <div class="card-row mt8"><strong>Recommended Action:</strong> Delete all 6 non-auto-trashed items. Report to Gmail as spam. Consider enabling stronger spam filters.</div>
    </div>

    <!-- JOB SEARCH -->
    <div class="green-card">
      <div class="card-label">🟢 Job Search</div>
      <div class="card-title">Job Search — 9 Emails</div>
      <div class="card-row"><strong>Count:</strong> 9</div>
      <table style="margin-top:10px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Fit</th></tr></thead>
        <tbody>
          <tr><td>LinkedIn Job Alerts</td><td>Global Head of HR — Empathy Talent ($300K)</td><td><span class="priority-high">HIGH</span></td></tr>
          <tr><td>Melissa W (self)</td><td>HRBP/Senior HRBP | Howden Re</td><td><span class="priority-high">HIGH</span></td></tr>
          <tr><td>Melissa W (self)</td><td>(no subject) — LinkedIn job view #4450294235</td><td><span class="priority-high">HIGH</span></td></tr>
          <tr><td>LinkedIn</td><td>New jobs similar to SVP HR at Brooklyn Navy Yard</td><td><span class="priority-med">MEDIUM</span></td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>Head of People Operations at Private Company</td><td><span class="priority-med">MEDIUM</span></td></tr>
          <tr><td>JobLeads (in Trash)</td><td>5 new jobs — Chief People Officer / Lead Talent</td><td><span class="priority-med">MEDIUM</span></td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>Senior People Partner, Technology — MrBeast</td><td><span class="priority-low">LOW-MED</span></td></tr>
          <tr><td>LinkedIn Job Alerts</td><td>VP of People — Nitra</td><td><span class="priority-low">LOW-MED</span></td></tr>
          <tr><td>GLP-1 by DirectMeds (fake email)</td><td>What If You Could Lose Weight Effortlessly?</td><td><span class="badge badge-red">SPAM</span></td></tr>
        </tbody>
      </table>
      <div class="card-row mt8"><strong>Recommended Action:</strong> Prioritize Empathy Talent ($300K) and self-forwarded roles. Apply to at least two this weekend.</div>
    </div>

    <!-- RECRUITERS / NETWORKING -->
    <div class="green-card">
      <div class="card-label">🤝 Recruiters / Networking</div>
      <div class="card-title">Recruiters / Networking — 3 Emails</div>
      <table style="margin-top:10px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Jolene A. Yee via LinkedIn</td><td>I'd like to connect 👤 — SVP, General Counsel, Delicato Family Wines</td><td>Accept + personalize message</td></tr>
          <tr><td>Dani Pfeiffer via LinkedIn</td><td>Dani accepted your invitation — explore their network</td><td>Send thank-you note, explore network</td></tr>
          <tr><td>NY Dept. of Labor</td><td>Invited to Harlem Recruitment Wednesday! 8/12</td><td>Attend if schedule allows — same day as HR Zoom</td></tr>
        </tbody>
      </table>
    </div>

    <!-- CALENDAR / EVENTS -->
    <div class="blue-card">
      <div class="card-label">📅 Calendar / Events</div>
      <div class="card-title">Calendar / Events — 1 Email</div>
      <div class="card-row"><strong>Sender:</strong> Grzegorz Sadowski via AppFolio (donotreply@appfolio.com)</div>
      <div class="card-row"><strong>Subject:</strong> Emergency — Repair main pipeline H line (water shutoff today 10 AM–1 PM)</div>
      <div class="card-row"><strong>Status:</strong> Already read. Water shutoff affects floors 18H and above. Plan accordingly.</div>
      <div class="card-row"><strong>Action:</strong> Acknowledged — no further action if you've already prepared.</div>
    </div>

    <!-- MEDICAL / HEALTH -->
    <div class="blue-card">
      <div class="card-label">🏥 Medical / Health</div>
      <div class="card-title">Medical / Health — 1 Email (+ Calendar)</div>
      <div class="card-row"><strong>Sender:</strong> Anthem Blue Cross and Blue Shield (DoNotReply-MemberComm@email.anthem.com)</div>
      <div class="card-row"><strong>Subject:</strong> You have a new explanation of benefits</div>
      <div class="card-row"><strong>Action:</strong> Log in to Anthem portal, review EOB for accuracy. Note any balance or errors. Cross-reference with your upcoming MRI (Aug 11) to ensure coverage is active.</div>
    </div>

    <!-- FINANCIAL / BILLING -->
    <div class="yellow-card">
      <div class="card-label">💰 Financial / Billing</div>
      <div class="card-title">Financial / Billing — 3 Emails</div>
      <table style="margin-top:10px;">
        <thead><tr><th>Sender</th><th>Subject</th><th>Priority</th><th>Action</th></tr></thead>
        <tbody>
          <tr>
            <td>Bank of America</td>
            <td>Billing Dispute -2994 — Step 2 of 3, Additional Info Needed</td>
            <td><span class="priority-high">HIGH</span></td>
            <td>Log in to BofA today and submit required documentation.</td>
          </tr>
          <tr>
            <td>Bank of America</td>
            <td>Credit Card -5690 Delivery Status — Step 3 of 3: Card Delivered</td>
            <td><span class="priority-low">LOW</span></td>
            <td>Already read. Activate your new card if you haven't already.</td>
          </tr>
          <tr>
            <td>Acorns (proxyvote.com)</td>
            <td>Reports for funds in your Acorns portfolio are here</td>
            <td><span class="priority-low">LOW</span></td>
            <td>Review investment fund reports when convenient. Stay informed.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- PROFESSIONAL DEVELOPMENT -->
    <div class="purple-card">
      <div class="card-label">📚 Professional Development</div>
      <div class="card-title">Professional Development — 1 Email</div>
      <div class="card-row"><strong>Sender:</strong> American Airlines (AAdvantage member update)</div>
      <div class="card
