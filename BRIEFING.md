<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa Weiss — August 3, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: white; border-radius: 12px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header .subtitle { font-size: 15px; color: #a8c8f0; margin-top: 6px; }
  .header .meta { display: flex; gap: 32px; margin-top: 16px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.1); border-radius: 8px; padding: 8px 16px; font-size: 13px; }
  .header .meta-item strong { display: block; font-size: 20px; color: #7dd3fc; }

  /* SECTION HEADERS */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; padding: 10px 16px; border-radius: 8px 8px 0 0; display: flex; align-items: center; gap: 8px; }
  .section-body { background: white; border-radius: 0 0 10px 10px; padding: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); }

  /* COLOR THEMES */
  .red .section-title { background: #dc2626; color: white; }
  .red .section-body { border-left: 4px solid #dc2626; }
  .yellow .section-title { background: #d97706; color: white; }
  .yellow .section-body { border-left: 4px solid #d97706; }
  .blue .section-title { background: #2563eb; color: white; }
  .blue .section-body { border-left: 4px solid #2563eb; }
  .green .section-title { background: #16a34a; color: white; }
  .green .section-body { border-left: 4px solid #16a34a; }
  .purple .section-title { background: #7c3aed; color: white; }
  .purple .section-body { border-left: 4px solid #7c3aed; }
  .gray .section-title { background: #6b7280; color: white; }
  .gray .section-body { border-left: 4px solid #6b7280; }
  .navy .section-title { background: #0f3460; color: white; }
  .navy .section-body { border-left: 4px solid #0f3460; }
  .teal .section-title { background: #0d9488; color: white; }
  .teal .section-body { border-left: 4px solid #0d9488; }

  /* TABLES */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { background: #f1f5f9; text-align: left; padding: 8px 10px; font-weight: 600; color: #475569; border-bottom: 2px solid #e2e8f0; }
  td { padding: 8px 10px; border-bottom: 1px solid #f1f5f9; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #fafbfc; }

  /* CARDS */
  .card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px 16px; margin-bottom: 12px; }
  .card:last-child { margin-bottom: 0; }
  .card-title { font-weight: 700; font-size: 14px; margin-bottom: 4px; }
  .card-label { display: inline-block; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 4px; text-transform: uppercase; margin-bottom: 6px; }
  .card-row { display: flex; gap: 8px; margin-bottom: 3px; flex-wrap: wrap; }
  .card-key { font-weight: 600; color: #475569; min-width: 110px; font-size: 12px; }
  .card-val { color: #1e293b; font-size: 12px; }

  /* BADGES */
  .badge { display: inline-block; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 12px; }
  .badge-red { background: #fee2e2; color: #dc2626; }
  .badge-yellow { background: #fef3c7; color: #d97706; }
  .badge-green { background: #dcfce7; color: #16a34a; }
  .badge-blue { background: #dbeafe; color: #2563eb; }
  .badge-purple { background: #ede9fe; color: #7c3aed; }
  .badge-gray { background: #f1f5f9; color: #6b7280; }
  .badge-orange { background: #ffedd5; color: #ea580c; }

  /* LABEL COLORS */
  .label-red { background: #dc2626; color: white; }
  .label-yellow { background: #d97706; color: white; }
  .label-green { background: #16a34a; color: white; }
  .label-blue { background: #2563eb; color: white; }
  .label-purple { background: #7c3aed; color: white; }
  .label-gray { background: #6b7280; color: white; }
  .label-teal { background: #0d9488; color: white; }

  /* BULLETS */
  .bullet { display: flex; gap: 10px; align-items: flex-start; margin-bottom: 8px; }
  .bullet-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; margin-top: 5px; }
  .dot-red { background: #dc2626; }
  .dot-yellow { background: #d97706; }
  .dot-green { background: #16a34a; }

  /* PRIORITY */
  .priority-high { color: #dc2626; font-weight: 700; }
  .priority-med { color: #d97706; font-weight: 700; }
  .priority-low { color: #6b7280; font-weight: 600; }

  /* TRIAGE TABLE */
  .triage-rescued { background: #fef9ec; }
  .triage-inbox { background: #f0fdf4; }
  .triage-summary { background: #f8fafc; font-style: italic; color: #64748b; }

  /* CALENDAR */
  .cal-day { margin-bottom: 16px; }
  .cal-day-header { font-weight: 700; font-size: 13px; color: #2563eb; background: #dbeafe; padding: 6px 12px; border-radius: 6px; margin-bottom: 8px; }
  .cal-event { display: flex; gap: 12px; padding: 8px 10px; background: #f8fafc; border-left: 3px solid #2563eb; border-radius: 4px; margin-bottom: 6px; }
  .cal-event.conflict { border-left-color: #dc2626; background: #fff5f5; }
  .cal-event.needs-rsvp { border-left-color: #d97706; background: #fffbeb; }
  .cal-event.declined { border-left-color: #6b7280; background: #f8fafc; opacity: 0.75; }
  .cal-time { font-weight: 700; min-width: 80px; font-size: 12px; color: #475569; }
  .cal-details { flex: 1; }
  .cal-summary { font-weight: 700; font-size: 13px; }
  .cal-meta { font-size: 11px; color: #64748b; margin-top: 2px; }

  /* SUMMARY BOX */
  .exec-summary { background: linear-gradient(135deg, #1e3a5f, #0f3460); color: white; border-radius: 10px; padding: 20px 24px; margin-bottom: 24px; }
  .exec-summary h2 { font-size: 15px; text-transform: uppercase; letter-spacing: 0.8px; color: #7dd3fc; margin-bottom: 14px; }
  .exec-bullet { display: flex; gap: 10px; margin-bottom: 10px; align-items: flex-start; }
  .exec-bullet-icon { font-size: 18px; flex-shrink: 0; }
  .exec-bullet-text { font-size: 13px; line-height: 1.5; }

  /* DASHBOARD */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 12px; }
  .dash-card { background: white; border-radius: 8px; padding: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.07); border-top: 3px solid #2563eb; }
  .dash-card.red-top { border-top-color: #dc2626; }
  .dash-card.yellow-top { border-top-color: #d97706; }
  .dash-card.green-top { border-top-color: #16a34a; }
  .dash-card.purple-top { border-top-color: #7c3aed; }
  .dash-card.gray-top { border-top-color: #6b7280; }
  .dash-card-title { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px; color: #64748b; margin-bottom: 6px; }
  .dash-card-value { font-size: 22px; font-weight: 800; color: #1e293b; }
  .dash-card-sub { font-size: 11px; color: #94a3b8; margin-top: 2px; }

  /* ALERT */
  .alert-box { background: #fef2f2; border: 1px solid #fca5a5; border-radius: 8px; padding: 12px 16px; margin-bottom: 12px; }
  .alert-box.yellow { background: #fffbeb; border-color: #fcd34d; }
  .alert-title { font-weight: 700; color: #dc2626; font-size: 13px; margin-bottom: 4px; }
  .alert-box.yellow .alert-title { color: #92400e; }
  .alert-body { font-size: 12px; color: #7f1d1d; }
  .alert-box.yellow .alert-body { color: #78350f; }

  /* RESCUED */
  .rescued-tag { font-size: 10px; font-weight: 700; background: #fef3c7; color: #92400e; border: 1px solid #fcd34d; padding: 1px 6px; border-radius: 4px; }
  .auto-trash-tag { font-size: 10px; font-weight: 700; background: #fee2e2; color: #dc2626; border: 1px solid #fca5a5; padding: 1px 6px; border-radius: 4px; }

  /* MISC */
  .divider { border: none; border-top: 1px solid #e2e8f0; margin: 12px 0; }
  .note { font-size: 11px; color: #64748b; font-style: italic; margin-top: 6px; }
  .group-header { font-size: 12px; font-weight: 700; color: #475569; background: #f1f5f9; padding: 5px 10px; border-radius: 4px; margin: 8px 0 6px; }
  a { color: #2563eb; text-decoration: none; }
  a:hover { text-decoration: underline; }
  .count-badge { display: inline-block; background: #e2e8f0; color: #475569; font-size: 11px; font-weight: 700; padding: 1px 7px; border-radius: 10px; margin-left: 6px; }
  .total-row { font-weight: 700; background: #f1f5f9 !important; }
  .tag { display: inline-block; font-size: 10px; font-weight: 700; padding: 1px 6px; border-radius: 4px; margin-right: 3px; }
  .tag-rescued { background: #fef3c7; color: #92400e; border: 1px solid #fcd34d; }
  .tag-inbox { background: #dcfce7; color: #166534; border: 1px solid #86efac; }
  .tag-trash { background: #f1f5f9; color: #475569; border: 1px solid #cbd5e1; }
  .tag-phish { background: #fee2e2; color: #dc2626; border: 1px solid #fca5a5; }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 1. HEADER -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="header">
  <h1>☀️ Good morning, Melissa</h1>
  <div class="subtitle">Executive Briefing — Monday, August 3, 2026</div>
  <div class="meta">
    <div class="meta-item"><strong>50</strong>Emails Reviewed</div>
    <div class="meta-item"><strong>9</strong>Calendar Events</div>
    <div class="meta-item"><strong>3</strong>Action Required</div>
    <div class="meta-item"><strong>2</strong>Security Alerts</div>
    <div class="meta-item"><strong>⚠️ Flash Flood</strong>NYC Warning — check conditions</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 2. EXECUTIVE SUMMARY -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="exec-summary">
  <h2>Executive Summary</h2>
  <div class="exec-bullet">
    <div class="exec-bullet-icon">🚨</div>
    <div class="exec-bullet-text"><strong>URGENT — Weather + Security:</strong> A Flash Flood Warning (expired 8:45 AM) and Flood Watch are active for Manhattan/Yorkville. Separately, one phishing email impersonating a health billing service was auto-blocked before reaching your inbox. Multiple spam campaigns (MEDVi GLP-1, ED/penis enlargement) are targeting your address — no action needed, all identified.</div>
  </div>
  <div class="exec-bullet">
    <div class="exec-bullet-icon">💼</div>
    <div class="exec-bullet-text"><strong>JOB SEARCH:</strong> LinkedIn shows someone from IntegriChain searched your profile and you appeared in 2 searches — strong signal of recruiter interest. Active alerts include <em>Senior Director of People</em> at Aescape and <em>Senior HR Business Partner</em> roles. HR Networking Group Zoom is Wednesday (RSVP pending).</div>
  </div>
  <div class="exec-bullet">
    <div class="exec-bullet-icon">📅</div>
    <div class="exec-bullet-text"><strong>CALENDAR / DEADLINES:</strong> Today — call Angel (all-day reminder) + cancel PT. Tomorrow — PT appointment. Wednesday — HR Networking Zoom (needs RSVP). Thursday — disability appointment + Executive Roundtable (you declined). Friday — State Farm bill due. Medium membership expires August 20.</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SECTION 0: EMAIL TRIAGE QUICK LIST -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section navy">
  <div class="section-title">📋 Email Triage Quick List</div>
  <div class="section-body" style="padding: 0;">
    <table>
      <thead>
        <tr>
          <th style="width:110px">Status</th>
          <th style="width:200px">From</th>
          <th>Subject</th>
          <th>Summary</th>
        </tr>
      </thead>
      <tbody>
        <!-- RESCUED ROWS FIRST -->
        <tr class="triage-rescued">
          <td><span class="tag tag-rescued">✅ RESCUED</span></td>
          <td>Duane Reade / Walgreens</td>
          <td>Refill due: it's time to refill your prescription</td>
          <td>Pharmacy prescription refill reminder — likely needs action</td>
        </tr>
        <tr class="triage-rescued">
          <td><span class="tag tag-rescued">✅ RESCUED</span></td>
          <td>Nextdoor — Alerts in Yorkville</td>
          <td>⚠️ Weather Alert: Flood Watch — Manhattan</td>
          <td>NWS Flood Watch for NYC/Manhattan — emergency alert</td>
        </tr>

        <!-- INBOX ROWS -->
        <tr class="triage-inbox">
          <td><span class="tag tag-inbox">📥 INBOX</span></td>
          <td>Notify NYC</td>
          <td>Flash Flood Warning — 8/3 NYC</td>
          <td>NWS Flash Flood Warning until 8:45 AM — review conditions</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="tag tag-inbox">📥 INBOX</span></td>
          <td>Temu</td>
          <td>Temu order refunded — #PO-211-13384130622071025</td>
          <td>Full refund processed; 5–14 business days to reflect</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="tag tag-inbox">📥 INBOX</span></td>
          <td>Temu</td>
          <td>Temu order partially refunded — #PO-211-13384088679031025</td>
          <td>Partial refund; 1–5 business days to reflect</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="tag tag-inbox">📥 INBOX</span></td>
          <td>SHEIN</td>
          <td>Important Update to Our Return Policy</td>
          <td>New Fair Use Policy may affect future returns — review</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="tag tag-inbox">📥 INBOX</span></td>
          <td>Cynergy PT</td>
          <td>August tip for overhead athletes: shoulder warm-up</td>
          <td>PT newsletter — shoulder warm-up tips relevant to your care</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="tag tag-inbox">📥 INBOX</span></td>
          <td>22 Words</td>
          <td>Your Amazon Lightning Deals ⚡ (Aug 3)</td>
          <td>Promotional deals email — low priority</td>
        </tr>
        <tr class="triage-inbox">
          <td><span class="tag tag-inbox">📥 INBOX</span></td>
          <td>LinkedIn</td>
          <td>New jobs similar to Senior HR Business Partner</td>
          <td>Job alert — new HR roles in New York</td>
        </tr>

        <!-- SUMMARY ROWS AT BOTTOM -->
        <tr class="triage-summary">
          <td><span class="tag tag-phish">🗑 AUTO-TRASHED</span></td>
          <td colspan="3">1 email auto-trashed (phishing) — see Trash Review &amp; Security section below</td>
        </tr>
        <tr class="triage-summary">
          <td><span class="tag tag-trash">🗂 TRASH</span></td>
          <td colspan="3">~38 emails in Trash (manual/promotional/spam/newsletters) — see Trash Review section below</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 3. ACTION REQUIRED -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section red">
  <div class="section-title">⚡ Action Required</div>
  <div class="section-body">

    <div class="card" style="border-left: 4px solid #dc2626;">
      <span class="card-label label-red">URGENT</span>
      <div class="card-title">🌊 Flash Flood Warning / Flood Watch — NYC</div>
      <div class="card-row"><span class="card-key">Source:</span><span class="card-val">Notify NYC + Nextdoor Yorkville alerts</span></div>
      <div class="card-row"><span class="card-key">Why it matters:</span><span class="card-val">NWS Flash Flood Warning was active until 8:45 AM today. Flood Watch remains in effect for Manhattan/New York County. Heavy rain may impact travel and safety in your neighborhood (E83rd &amp; 2nd Ave).</span></div>
      <div class="card-row"><span class="card-key">Next step:</span><span class="card-val">Check current conditions before leaving home. Avoid flooded streets or subway stations. Monitor NYC Emergency Management.</span></div>
      <div class="card-row"><span class="card-key">Due:</span><span class="card-val">Today, August 3, 2026 — ongoing</span></div>
    </div>

    <div class="card" style="border-left: 4px solid #d97706;">
      <span class="card-label label-yellow">FOLLOW-UP</span>
      <div class="card-title">💊 Prescription Refill Due — Walgreens / Duane Reade</div>
      <span class="rescued-tag">✅ Rescued from Trash</span>
      <div class="card-row" style="margin-top:6px;"><span class="card-key">Source:</span><span class="card-val">Duane Reade &lt;duanereade@eml.walgreens.com&gt;</span></div>
      <div class="card-row"><span class="card-key">Why it matters:</span><span class="card-val">A prescription refill notification was sent this morning. This email was incorrectly sent to Trash and was rescued because it likely requires pharmacy action.</span></div>
      <div class="card-row"><span class="card-key">Next step:</span><span class="card-val">Log in to Walgreens/Duane Reade app or website to refill your prescription. Confirm pickup time/location.</span></div>
      <div class="card-row"><span class="card-key">Due:</span><span class="card-val">As soon as possible — refill window may be limited</span></div>
    </div>

    <div class="card" style="border-left: 4px solid #d97706;">
      <span class="card-label label-yellow">RSVP NEEDED</span>
      <div class="card-title">📅 HR Networking &amp; Job Search Group — Zoom (Wed Aug 5, 12–1:30 PM)</div>
      <div class="card-row"><span class="card-key">Source:</span><span class="card-val">Google Calendar (status: needsAction)</span></div>
      <div class="card-row"><span class="card-key">Why it matters:</span><span class="card-val">This is a key networking session for your job search with 150+ HR professionals. Your RSVP is still pending.</span></div>
      <div class="card-row"><span class="card-key">Next step:</span><span class="card-val">Confirm attendance via calendar invitation. Zoom link: us06web.zoom.us/j/81954171722</span></div>
      <div class="card-row"><span class="card-key">Due:</span><span class="card-val">Before Wednesday, August 5 at 12:00 PM</span></div>
    </div>

    <div class="card" style="border-left: 4px solid #d97706;">
      <span class="card-label label-yellow">DEADLINE</span>
      <div class="card-title">🏠 State Farm Bill Due — Friday, August 7</div>
      <div class="card-row"><span class="card-key">Source:</span><span class="card-val">Google Calendar reminder (all-day event Aug 7)</span></div>
      <div class="card-row"><span class="card-key">Why it matters:</span><span class="card-val">Insurance payment deadline this week. Missing this could affect coverage.</span></div>
      <div class="card-row"><span class="card-key">Next step:</span><span class="card-val">Schedule or confirm State Farm payment before Friday, August 7.</span></div>
      <div class="card-row"><span class="card-key">Due:</span><span class="card-val">Friday, August 7, 2026</span></div>
    </div>

    <div class="card" style="border-left: 4px solid #d97706;">
      <span class="card-label label-yellow">ACTION TODAY</span>
      <div class="card-title">📞 Call Angel — Today (Reminder Set 10 AM)</div>
      <div class="card-row"><span class="card-key">Source:</span><span class="card-val">Google Calendar — "Call angel" (10 AM – 11 PM)</span></div>
      <div class="card-row"><span class="card-key">Why it matters:</span><span class="card-val">You set this as a reminder for today. The long end time suggests this is a "do it sometime today" task rather than a fixed appointment.</span></div>
      <div class="card-row"><span class="card-key">Next step:</span><span class="card-val">Call Angel today before end of day.</span></div>
      <div class="card-row"><span class="card-key">Due:</span><span class="card-val">Today, August 3</span></div>
    </div>

    <div class="card" style="border-left: 4px solid #6b7280;">
      <span class="card-label label-gray">ADMIN TODAY</span>
      <div class="card-title">❌ Cancel PT Appointment — Today (10 AM slot)</div>
      <div class="card-row"><span class="card-key">Source:</span><span class="card-val">Google Calendar — "Cancel pt" (10 AM – 11 AM)</span></div>
      <div class="card-row"><span class="card-key">Why it matters:</span><span class="card-val">You have a reminder to cancel today's PT session. Tomorrow (Aug 4) has a separate PT appointment — suggesting you're rescheduling, not skipping entirely.</span></div>
      <div class="card-row"><span class="card-key">Next step:</span><span class="card-val">Contact Cynergy PT to cancel today's appointment if not already done. Note: SHEIN return policy update may affect any pending PT-related orders (coincidental).</span></div>
      <div class="card-row"><span class="card-key">Due:</span><span class="card-val">Today, August 3 — before 10 AM ideally</span></div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 4. FULL 7-DAY CALENDAR -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section blue">
  <div class="section-title">📅 Full 7-Day Calendar — Aug 3–9, 2026</div>
  <div class="section-body">

    <!-- MONDAY AUG 3 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Monday, August 3, 2026 — TODAY</div>

      <div class="alert-box yellow" style="margin-bottom:10px;">
        <div class="alert-title">⚠️ Flash Flood Warning (expired 8:45 AM) + Flood Watch Active</div>
        <div class="alert-body">Check current conditions before traveling. Yorkville / Manhattan area affected.</div>
      </div>

      <div class="cal-event conflict">
        <div class="cal-time">10:00 AM<br><span style="font-size:10px;color:#94a3b8;">All day</span></div>
        <div class="cal-details">
          <div class="cal-summary">📞 Call Angel <span class="badge badge-yellow">ACTION TODAY</span></div>
          <div class="cal-meta">Reminder set 10 AM – 11 PM (flexible task window) | No location | Status: Confirmed</div>
          <div class="cal-meta" style="color:#dc2626;">⚠️ Note: Overlaps with "Cancel PT" reminder at same time</div>
        </div>
      </div>

      <div class="cal-event">
        <div class="cal-time">10:00–11:00 AM</div>
        <div class="cal-details">
          <div class="cal-summary">❌ Cancel PT <span class="badge badge-orange">DO THIS NOW</span></div>
          <div class="cal-meta">Reminder to cancel today's physical therapy session | Status: Confirmed</div>
          <div class="cal-meta">Contact Cynergy PT to cancel. Tomorrow's PT (Aug 4) is still on.</div>
        </div>
      </div>
    </div>

    <!-- TUESDAY AUG 4 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Tuesday, August 4, 2026</div>
      <div class="cal-event">
        <div class="cal-time">10:00–11:00 AM</div>
        <div class="cal-details">
          <div class="cal-summary">🏃 PT (Physical Therapy) <span class="badge badge-green">CONFIRMED</span></div>
          <div class="cal-meta">Physical therapy appointment | Status: Confirmed | No location listed</div>
          <div class="cal-meta">Prep: Review Cynergy PT's August shoulder warm-up tip (in your inbox) — 10–15 min warm-up recommended for overhead athletes.</div>
        </div>
      </div>
    </div>

    <!-- WEDNESDAY AUG 5 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Wednesday, August 5, 2026</div>

      <div class="cal-event needs-rsvp">
        <div class="cal-time">12:00–1:30 PM</div>
        <div class="cal-details">
          <div class="cal-summary">🤝 HR Networking &amp; Job Search Group — Zoom 2 <span class="badge badge-yellow">RSVP NEEDED</span></div>
          <div class="cal-meta">Status: <strong>needsAction</strong> — You have NOT confirmed attendance</div>
          <div class="cal-meta">Zoom: <a href="https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1">us06web.zoom.us/j/81954171722</a> | 150+ HR professionals attending</div>
          <div class="cal-meta">⚠️ <strong>Action needed: RSVP before Wednesday.</strong> Review team guidelines link in calendar description before joining.</div>
        </div>
      </div>

      <div class="cal-event">
        <div class="cal-time">12:00–1:30 PM</div>
        <div class="cal-details">
          <div class="cal-summary">🤝 Network <span class="badge badge-green">CONFIRMED</span></div>
          <div class="cal-meta">Personal reminder/block for networking session | Status: Confirmed | No separate link</div>
          <div class="cal-meta">⚠️ This overlaps with HR Networking Zoom above — likely the same session or a paired personal reminder.</div>
        </div>
      </div>
    </div>

    <!-- THURSDAY AUG 6 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Thursday, August 6, 2026</div>

      <div class="cal-event conflict">
        <div class="cal-time">9:00–11:00 AM</div>
        <div class="cal-details">
          <div class="cal-summary">🏥 Disability Appointment <span class="badge badge-yellow">CONFIRMED</span></div>
          <div class="cal-meta">Status: Confirmed | No location listed</div>
          <div class="cal-meta" style="color:#dc2626;">⚠️ CONFLICT: Overlaps with Executive Roundtable (9:00–10:30 AM) — but you have already <strong>declined</strong> the Roundtable, so no conflict in practice.</div>
        </div>
      </div>

      <div class="cal-event declined">
        <div class="cal-time">9:00–10:30 AM</div>
        <div class="cal-details">
          <div class="cal-summary">🎤 Executive Roundtable <span class="badge badge-gray">DECLINED</span></div>
          <div class="cal-meta">Hosted by John Madigan | Status: <strong>Declined</strong></div>
          <div class="cal-meta">Zoom: <a href="https://us02web.zoom.us/j/207786667?pwd=Y3NXSHNVN1ozZjlQOVVFTUkwbHRKZz09">Meeting ID 207 786 667</a> | Password: 205454</div>
          <div class="cal-meta">You have declined this invitation. No action needed.</div>
        </div>
      </div>

      <div class="cal-event needs-rsvp">
        <div class="cal-time">12:00–1:00 PM</div>
        <div class="cal-details">
          <div class="cal-summary">🤝 HR Networking &amp; Job Search: Open Office Hours — Zoom 2 <span class="badge badge-yellow">RSVP NEEDED</span></div>
          <div class="cal-meta">Status: <strong>needsAction</strong> — RSVP pending</div>
          <div class="cal-meta">Zoom: <a href="https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1">us06web.zoom.us/j/85945371140</a></div>
          <div class="cal-meta">Note: No AI recording tools per organizer's request. Open discussion format.</div>
          <div class="cal-meta">⚠️ Action needed: RSVP before Thursday morning.</div>
        </div>
      </div>
    </div>

    <!-- FRIDAY AUG 7 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Friday, August 7, 2026</div>
      <div class="cal-event" style="border-left-color:#d97706; background:#fffbeb;">
        <div class="cal-time">All Day</div>
        <div class="cal-details">
          <div class="cal-summary">💳 State Farm Bill Due <span class="badge badge-yellow">DEADLINE</span></div>
          <div class="cal-meta">Status: Confirmed | All-day reminder | Pay before EOD Friday to avoid late fees</div>
          <div class="cal-meta">⚠️ Schedule payment today or by Thursday at the latest.</div>
        </div>
      </div>
    </div>

    <!-- SAT-SUN AUG 8-9 -->
    <div class="cal-day">
      <div class="cal-day-header">📆 Saturday–Sunday, August 8–9, 2026</div>
      <div class="cal-event" style="border-left-color:#94a3b8; background:#f8fafc; opacity:0.7;">
        <div class="cal-time">—</div>
        <div class="cal-details">
          <div class="cal-summary" style="color:#64748b;">No calendar events scheduled this weekend.</div>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 5. JOB SEARCH & INTERVIEW PIPELINE -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section green">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>
  <div class="section-body">

    <div class="group-header">🔔 Active Job Alerts</div>
    <table>
      <thead>
        <tr><th>Role</th><th>Company</th><th>Source</th><th>Date</th><th>Fit</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Senior Director of People</strong></td>
          <td>Aescape</td>
          <td>LinkedIn Job Alerts</td>
          <td>July 31, 2026 (alerted Aug 3)</td>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>Review &amp; apply — senior-level people leadership role</td>
        </tr>
        <tr>
          <td><strong>Senior HR Business Partner — New York</strong></td>
          <td>Middle Market Review</td>
          <td>LinkedIn</td>
          <td>Aug 3, 2026</td>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>Review similar roles alert — multiple matches surfaced</td>
        </tr>
        <tr>
          <td><strong>Relations Coordinator</strong></td>
          <td>Heard.Help + 2 more</td>
          <td>Glassdoor</td>
          <td>Aug 3, 2026</td>
          <td><span class="badge badge-yellow">MEDIUM</span></td>
          <td>Review — may be below target level; check full list</td>
        </tr>
      </tbody>
    </table>

    <div class="group-header" style="margin-top:16px;">👁️ Recruiter Signals &amp; Profile Activity</div>
    <table>
      <thead>
        <tr><th>Signal</th><th>Source</th><th>Detail</th><th>Fit</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>LinkedIn — 2 Profile Searches</strong></td>
          <td>LinkedIn notifications</td>
          <td>Someone from <strong>IntegriChain</strong> found your profile</td>
          <td><span class="badge badge-green">HIGH</span></td>
          <td>Research IntegriChain — pharmaceutical analytics company. Consider connecting or reaching out proactively.</td>
        </tr>
        <tr>
          <td><strong>LinkedIn Profile View</strong></td>
          <td>Lisa Rangel / Chameleon Resumes</td>
          <td>Employer urgency coaching email (newsletter)</td>
          <td><span class="badge badge-gray">LOW</span></td>
          <td>Newsletter — no action required; unsubscribe if not useful</td>
        </tr>
      </tbody>
    </table>

    <div class="group-header" style="margin-top:16px;">🤝 Networking Sessions (Calendar)</div>
    <table>
      <thead>
        <tr><th>Event</th><th>Date/Time</th><th>RSVP Status</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr style="background:#fffbeb;">
          <td><strong>HR Networking &amp; Job Search Group — Zoom</strong></td>
          <td>Wed Aug 5, 12:00–1:30 PM</td>
          <td><span class="badge badge-yellow">⚠️ Needs Action</span></td>
          <td><strong>RSVP NOW</strong> — 150+ HR professionals; high-value session</td>
        </tr>
        <tr style="background:#fffbeb;">
          <td><strong>HR Networking Open Office Hours — Zoom</strong></td>
          <td>Thu Aug 6, 12:00–1:00 PM</td>
          <td><span class="badge badge-yellow">⚠️ Needs Action</span></td>
          <td><strong>RSVP</strong> — open discussion, no AI recording</td>
        </tr>
        <tr>
          <td>Network (personal block)</td>
          <td>Wed Aug 5, 12:00–1:30 PM</td>
          <td><span class="badge badge-green">Confirmed</span></td>
          <td>Likely mirrors HR Zoom above — no separate action</td>
        </tr>
      </tbody>
    </table>

    <div class="note" style="margin-top:10px;">💡 Glassdoor is now part of Indeed — noted in email. Your Glassdoor profile/activity transfers automatically.</div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 6. FULL EMAIL REVIEW BY CATEGORY -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section red">
  <div class="section-title">🔐 Security / Risk</div>
  <div class="section-body">

    <div class="alert-box">
      <div class="alert-title">🚫 AUTO-TRASHED: Phishing Email Blocked</div>
      <div class="alert-body">
        <strong>From:</strong> no-reply@myhealthpayment.com | <strong>Subject:</strong> "You have a new communication from Billing Services regarding your coverage"<br>
        <strong>Reason:</strong> Suspicious sender domain impersonating a billing/insurance service. Directed to external URL (cobraandbillings...) with urgency language about coverage requiring action — classic credential-harvesting or payment-fraud setup.<br>
        <strong>Action:</strong> Already removed. No further action needed. Do not visit the linked URL.
      </div>
    </div>

    <div class="alert-box" style="margin-top:10px;">
      <div class="alert-title">🌊 Flash Flood Warning — NYC (Active)</div>
      <div class="alert-body">
        <strong>From:</strong> Notify NYC (noreply@everbridge.net) — official NYC Emergency Management<br>
        <strong>Subject:</strong> Flash Flood Warning — 8/3 NYC | Warning until 8:45 AM<br>
        <strong>Also:</strong> Nextdoor Yorkville alert (rescued from trash) — NWS Flood Watch for New York County<br>
        <strong>Action:</strong> Monitor conditions. Check MTA/transit status before traveling.
      </div>
    </div>

    <div class="alert-box yellow" style="margin-top:10px;">
      <div class="alert-title">⚠️ Spam Campaign — MEDVi GLP-1 (5 emails from fake domains)</div>
      <div class="alert-body">
        Multiple emails from randomized/fake sender domains impersonating "MEDVi GLP-1" with weight loss solicitations. Subjects include: "No more excuses," "Stop waiting," "Your transformation starts," "GLP-1 secret celebrities use." All originated from suspicious domain patterns (random character strings). <strong>Do not click any links.</strong> Mark as spam and block if they reach inbox.
      </div>
    </div>

    <div class="alert-box yellow" style="margin-top:10px;">
      <div class="alert-title">⚠️ Spam — "Dr. Arthur Green" (explicit spam, inappropriate content)</div>
      <div class="alert-body">
        <strong>From:</strong> ytcuzvlkqhtaaj...@7zxx6c.myf69j.4ydgbz.us | <strong>Subject:</strong> "Add 3.8 inches naturally with this $3 method"<br>
        Highly suspicious domain. Inappropriate/spam content. Do not engage. Report as spam.
      </div>
    </div>

    <div class="alert-box yellow" style="margin-top:10px;">
      <div class="alert-title">⚠️ Spam — "ED Cure" (explicit spam)</div>
      <div class="alert-body">
        <strong>From:</strong> grkxmsjijicbap...@4ic7a2.aedxdo.ydonw1.us | <strong>Subject:</strong> "Doctors finally admit this about ED*"<br>
        Spam/scam email in Trash. Already removed. No action needed.
      </div>
    </div>

    <div class="alert-box yellow" style="margin-top:10px;">
      <div class="alert-title">⚠️ Political Email — Confirm Receipt</div>
      <div class="alert-body">
        <strong>From:</strong> contact@email.donaldjtrump.com | <strong>Subject:</strong> "Confirm receipt of this email."<br>
        Legitimate domain for Trump campaign emails. "Checking on something very important" — political fundraising/list confirmation. No security risk, but low value. Safe to delete/unsubscribe.
      </div>
    </div>

    <p class="note">Total emails in this category: 8 (1 auto-trashed phishing, 2 weather alerts, 5 spam/MEDVi, 2 ED/penis enlargement spam, 1 political)</p>
  </div>
</div>

<div class="section green">
  <div class="section-title">💼 Job Search &amp; Opportunities</div>
  <div class="section-body">
    <table>
      <thead>
        <tr><th>From</th><th>Subject</th><th>Status</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>LinkedIn Job Alerts</td>
          <td>Senior Director of People at Aescape</td>
          <td><span class="badge badge-green">HIGH FIT</span></td>
          <td>Review and apply — posted 7/31/2026</td>
        </tr>
        <tr>
          <td>LinkedIn</td>
          <td>New jobs similar to Senior HR Business Partner — NY at Middle Market Review</td>
          <td><span class="badge badge-green">HIGH FIT</span></td>
          <td>Review all similar roles listed</td>
        </tr>
        <tr>
          <td>LinkedIn (notifications)</td>
          <td>You appeared in 2 searches — IntegriChain</td>
          <td><span class="badge badge-green">HIGH SIGNAL</span></td>
          <td>Research IntegriChain; consider proactive outreach</td>
        </tr>
        <tr>
          <td>Glassdoor</td>
          <td>Relations Coordinator at Heard.Help + 2 more jobs in NY</td>
          <td><span class="badge badge-yellow">MEDIUM</span></td>
          <td>Review full listing — may be below target level</td>
        </tr>
        <tr>
          <td>LinkedIn Job Alerts (duplicate)</td>
          <td>Senior Director of People at Aescape (duplicate alert)</td>
          <td><span class="badge badge-gray">DUPLICATE</span></td>
          <td>Sent twice — one can be ignored</td>
        </tr>
        <tr>
          <td>Glassdoor</td>
          <td>Glassdoor is now part of Indeed</td>
          <td><span class="badge badge-gray">INFO</span></td>
          <td>FYI only — Glassdoor profiles migrate to Indeed</td>
        </tr>
      </tbody>
    </table>
    <p class="note">Total emails in this category: 6</p>
  </div>
</div>

<div class="section green">
  <div class="section-title">🤝 Recruiters / Professional Networking</div>
  <div class="section-body">
    <table>
      <thead>
        <tr><th>From</th><th>Subject</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Lisa Rangel / Chameleon Resumes</td>
          <td>Employers looked at your profile</td>
          <td>Newsletter-style resume coaching email. Read if useful; unsubscribe if not.</td>
        </tr>
      </tbody>
    </table>
    <p class="note">Total emails in this category: 1</p>
  </div>
</div>

<div class="section yellow">
  <div class="section-title">🏥 Medical / Health</div>
  <div class="section-body">
    <table>
      <thead>
        <tr><th>From</th><th>Subject</th><th>Tag</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr style="background:#fef9ec;">
          <td>Duane Reade / Walgreens</td>
          <td>Refill due: it's time to refill your prescription</td>
          <td><span class="rescued-tag">✅ Rescued from Trash</span></td>
          <td><strong>Refill your prescription today.</strong> Log in to Walgreens app or website.</td>
        </tr>
        <tr>
          <td>Cynergy PT</td>
          <td>August tip for overhead athletes: shoulder warm-up (10–15 min)</td>
          <td><span class="badge badge-blue">INBOX</span></td>
          <td>Read before tomorrow's PT appointment — relevant shoulder prep tips.</td>
        </tr>
      </tbody>
    </table>
    <p class="note">Total emails in this category: 2</p>
  </div>
</div>

<div class="section yellow">
  <div class="section-title">💳 Financial / Billing</div>
  <div class="section-body">
    <table>
      <thead>
        <tr><th>From</th><th>Subject</th><th>Amount/Detail</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Temu (orders@transaction.temu.com)</td>
          <td>Temu order refunded — #PO-211-13384130622071025</td>
          <td>Full refund; 5–14 business days (up to 30)</td>
          <td>Monitor bank account for refund credit. No action needed yet.</td>
        </tr>
        <tr>
          <td>Temu (orders@transaction.temu.com)</td>
          <td>Temu order partially refunded — #PO-211-13384088679031025</td>
          <td>Partial refund; 1–5 business days</td>
          <td>Expect refund shortly. Verify correct amount when posted.</td>
        </tr>
        <tr>
          <td>SHEIN (shein@us.mail.shein.com)</td>
          <td>Important Update to Our Return Policy — Fair Use Policy</td>
          <td>Policy change affecting future returns</td>
          <td>Read policy change — may affect pending or future Temu/SHEIN returns.</td>
        </tr>
        <tr style="background:#fff0f0;">
          <td>no-reply@myhealthpayment.com</td>
          <td>New communication from Billing Services — coverage action required</td>
          <td><span class="auto-trash-tag">🚫 AUTO-TRASHED — PHISHING</span></td>
          <td>Blocked. Do not visit linked URL. No action needed.</td>
        </tr>
      </tbody>
    </table>
    <p class="note">Total emails in this category: 4 (including 1 phishing)</p>
  </div>
</div>

<div class="section blue">
  <div class="section-title">📅 Calendar / Events / Notifications</div>
  <div class="section-body">
    <table>
      <thead>
        <tr><th>From</th><th>Subject</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Notify NYC</td>
          <td>Flash Flood Warning — 8/3 NYC (until 8:45 AM)</td>
          <td>Monitor conditions. Check NYC Emergency Management.</td>
        </tr>
        <tr style="background:#fef9ec;">
          <td>Nextdoor — Yorkville Alerts</td>
          <td>⚠️ Weather Alert: Flood Watch — Manhattan (rescued from trash)</td>
          <td><span class="rescued-tag">✅ Rescued</span> — NWS Flood Watch active. Stay aware of street/transit flooding.</td>
        </tr>
        <tr>
          <td>Notify NYC</td>
          <td>Missing Vulnerable Adult Alert — Joseta Delacruz, 60-year-old female, North Merri...</td>
          <td>FYI community alert. No action required unless you have information.</td>
        </tr>
        <tr>
          <td>Otter.ai Insights (in Trash)</td>
          <td>Your upcoming meetings</td>
          <td>Otter.ai weekly prep digest. Review if you use Otter — then delete. Note: Thursday's HR session requests no AI recording tools.</td>
        </tr>
      </tbody>
    </table>
    <p class="note">Total emails in this category: 4</p>
  </div>
</div>

<div class="section purple">
  <div class="section-title">📚 Professional Development</div>
  <div class="section-body">
    <table>
      <thead>
        <tr><th>From</th><th>Subject</th><th>Action</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Medium Daily Digest</td>
          <td>Claude Design | RH Malini (membership expires Aug 20)</td>
          <td>⚠️ Medium membership expires Aug 20, 2026. Decide: reactivate ($) or let expire.</td>
        </tr>
        <tr>
          <td>Medium Daily Digest</td>
          <td>How to Do Hard Things When You Have Zero Motivation | Darius Foroux</td>
          <td>Motivational productivity content. Read if interested; low priority.</td>
        </tr>
        <tr>
          <td>The AI Report</td>
          <td>⚡ AI kill switch bill hits Congress + Google pulls AI image gen from Earth</td>
          <td>Relevant AI policy news. Skim for professional awareness.</td>
        </tr>
        <tr>
          <td>TLDR Newsletter</td>
          <td>OpenAI Astra 🤖, Larry Ellison's bet, GitHub CLI stacked diffs</td>
          <td>Tech/AI industry news. Skim if relevant to your field.</td>
        </tr>
      </tbody>
    </table>
    <p class="note">Total emails in this category: 4</p>
  </div>
</div>

<div class="section purple">
  <div class="section-title">💛 Personal</div>
  <div class="section-body">
    <table>
      <thead>
        <tr><th>From</th><th>Subject</th><th>Notes</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Match</td>
          <td>Sal (62, Staten Island) viewed your profile</td>
          <td>Dating app notification. Check profile when ready.</td>
        </tr>
        <tr>
          <td>Match</td>
          <td>Rk likes you — see if it's mutual</td>
          <td>Dating app notification.</td>
        </tr>
        <tr>
          <td>Match</td>
          <td>Alden likes you — see if it's mutual</td>
          <td>Dating app notification.</td>
        </tr>
        <tr>
          <td>Hinge</td>
          <td>Andy liked your Prompt</td>
          <td>Dating app notification.</td>
        </tr>
        <tr>
          <td>OkCupid</td>
          <td>You have an Intro! Read their message now</td>
          <td>Dating app — someone messaged you. Check when ready.</td>
        </tr>
      </tbody>
    </table>
    <p class="note">Total emails in this category: 5</p>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- 8. PROMOTIONAL / RETAIL SUMMARY -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="section gray">
  <div class="section-title">🛍️ Promotional / Retail Summary</div>
  <div class="section-body">
    <table>
      <thead>
        <tr><th>Brand</th><th>Count</th><th>Subject / Theme</th><th>Recommendation</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>SHEIN</strong></td>
          <td>3</td>
          <td>🚨 NEW IN (3 days ago) | All under $14.99 Clearance Edit (×2 from different domains)</td>
          <td><span class="badge badge-gray">Delete/Ignore</span> — Clearance edit sent twice from different domains; promotional only. Note return policy update is in Financial/Billing.</td>
        </tr>
        <tr>
          <td><strong>Old Navy</strong></td>
          <td>3</td>
          <td>Super Cash earned (×2 duplicate) | Abandoned cart reminder</td>
          <td><span class="badge badge-yellow">Review</span> — Super Cash has expiry; check if you want to use it. Abandoned cart: decide to purchase or ignore.</td>
        </tr>
        <tr>
          <td><strong>Temu</strong></td>
          <td>1</td>
          <td>$20 loyalty coupon — no minimum spend</td>
          <td><span class="badge badge-gray">Ignore</span> — Coupon available if you plan to shop; otherwise ignore.</td>
        </tr>
        <tr>
          <td><strong>Kohl's</strong></td>
          <td>1</td>
          <td>🚨 ULTIMATE Clearance Event — up to 70% off</td>
          <td><span class="badge badge-gray">Delete</span> — Promotional only. Low priority.</td>
        </tr>
        <tr>
          <td><strong>Uber</strong></td>
          <td>1</td>
          <td>Promo: up to 20% off rides</td>
          <td><span class="badge badge-yellow">Keep briefly</span> — Useful if traveling today given flooding. Check app for promo code.</td>
        </tr>
        <tr>
          <td><strong>22 Words</strong></td>
          <td>1</td>
          <td>Amazon Lightning Deals ⚡ (Aug 3) — 50% off disc, kids kit, shower head</td>
          <td><span class="badge badge-gray">Delete</span> — Promotional deal digest; low priority.</td>
        </tr>
        <tr
