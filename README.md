<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Briefing — Melissa W — August 14, 2026</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 14px; line-height: 1.5; }
  .page { max-width: 1100px; margin: 0 auto; padding: 24px 16px; }

  /* Header */
  .header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); color: white; border-radius: 14px; padding: 32px 36px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
  .header .subtitle { font-size: 15px; color: #a0aec0; margin-top: 4px; }
  .header .meta { display: flex; gap: 28px; margin-top: 18px; flex-wrap: wrap; }
  .header .meta-item { background: rgba(255,255,255,0.08); border-radius: 8px; padding: 8px 16px; font-size: 13px; }
  .header .meta-item strong { display: block; font-size: 20px; color: #63b3ed; }

  /* Section */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 17px; font-weight: 700; letter-spacing: 0.3px; margin-bottom: 14px; padding: 10px 16px; border-radius: 8px; display: flex; align-items: center; gap: 8px; }

  /* Color themes */
  .theme-red { background: #fff5f5; border-left: 5px solid #e53e3e; }
  .theme-red .section-title { background: #fed7d7; color: #742a2a; }
  .theme-yellow { background: #fffff0; border-left: 5px solid #d69e2e; }
  .theme-yellow .section-title { background: #fefcbf; color: #744210; }
  .theme-blue { background: #ebf8ff; border-left: 5px solid #3182ce; }
  .theme-blue .section-title { background: #bee3f8; color: #1a365d; }
  .theme-green { background: #f0fff4; border-left: 5px solid #38a169; }
  .theme-green .section-title { background: #c6f6d5; color: #1c4532; }
  .theme-purple { background: #faf5ff; border-left: 5px solid #805ad5; }
  .theme-purple .section-title { background: #e9d8fd; color: #44337a; }
  .theme-gray { background: #f7fafc; border-left: 5px solid #a0aec0; }
  .theme-gray .section-title { background: #edf2f7; color: #2d3748; }
  .theme-triage { background: #fff; border-left: 5px solid #2b6cb0; }
  .theme-triage .section-title { background: #ebf8ff; color: #1a365d; }

  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; }

  /* Table */
  table { width: 100%; border-collapse: collapse; border-radius: 8px; overflow: hidden; }
  th { background: #2d3748; color: white; padding: 10px 14px; text-align: left; font-size: 13px; font-weight: 600; }
  td { padding: 9px 14px; border-bottom: 1px solid #e2e8f0; font-size: 13px; vertical-align: top; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #f7fafc; }
  tr:hover td { background: #edf2f7; }

  /* Badges */
  .badge { display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 11px; font-weight: 700; margin-right: 4px; }
  .badge-red { background: #fed7d7; color: #742a2a; }
  .badge-yellow { background: #fefcbf; color: #744210; }
  .badge-green { background: #c6f6d5; color: #1c4532; }
  .badge-blue { background: #bee3f8; color: #1a365d; }
  .badge-purple { background: #e9d8fd; color: #44337a; }
  .badge-gray { background: #edf2f7; color: #4a5568; }
  .badge-orange { background: #feebc8; color: #7b341e; }
  .badge-high { background: #fed7d7; color: #742a2a; }
  .badge-med { background: #fefcbf; color: #744210; }
  .badge-low { background: #c6f6d5; color: #1c4532; }

  /* Action cards */
  .action-card { border-radius: 10px; padding: 16px 20px; margin-bottom: 14px; border: 1px solid; }
  .action-card-red { background: #fff5f5; border-color: #fc8181; }
  .action-card-yellow { background: #fffff0; border-color: #f6e05e; }
  .action-card-green { background: #f0fff4; border-color: #68d391; }
  .action-card-blue { background: #ebf8ff; border-color: #63b3ed; }
  .action-card-purple { background: #faf5ff; border-color: #b794f4; }
  .action-card h4 { font-size: 14px; font-weight: 700; margin-bottom: 6px; }
  .action-card .meta-row { display: flex; gap: 16px; flex-wrap: wrap; margin-top: 8px; font-size: 12px; color: #4a5568; }
  .action-card .meta-row span strong { color: #2d3748; }

  /* Exec summary */
  .exec-bullets { list-style: none; padding: 0; }
  .exec-bullets li { padding: 12px 16px; margin-bottom: 10px; border-radius: 8px; font-size: 14px; display: flex; align-items: flex-start; gap: 10px; }
  .exec-bullets li .icon { font-size: 18px; flex-shrink: 0; }

  /* Calendar */
  .cal-day { background: white; border-radius: 10px; margin-bottom: 14px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }
  .cal-day-header { background: #2d3748; color: white; padding: 9px 16px; font-weight: 700; font-size: 13px; }
  .cal-event { padding: 12px 16px; border-bottom: 1px solid #edf2f7; }
  .cal-event:last-child { border-bottom: none; }
  .cal-event h4 { font-size: 14px; font-weight: 700; color: #1a365d; }
  .cal-event .cal-meta { font-size: 12px; color: #718096; margin-top: 4px; }
  .cal-event .cal-link { font-size: 12px; color: #3182ce; word-break: break-all; }
  .no-events { padding: 12px 16px; color: #a0aec0; font-style: italic; font-size: 13px; }
  .rsvp-confirmed { color: #38a169; font-weight: 700; }
  .rsvp-needs { color: #d69e2e; font-weight: 700; }
  .rsvp-declined { color: #e53e3e; font-weight: 700; }
  .rsvp-accepted { color: #3182ce; font-weight: 700; }

  /* Dashboard grid */
  .dash-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
  .dash-card { background: white; border-radius: 10px; padding: 16px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); border-top: 4px solid #a0aec0; }
  .dash-card.dc-red { border-top-color: #e53e3e; }
  .dash-card.dc-yellow { border-top-color: #d69e2e; }
  .dash-card.dc-green { border-top-color: #38a169; }
  .dash-card.dc-blue { border-top-color: #3182ce; }
  .dash-card.dc-purple { border-top-color: #805ad5; }
  .dash-card h4 { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: #718096; margin-bottom: 8px; }
  .dash-card .dash-num { font-size: 32px; font-weight: 800; color: #1a202c; }
  .dash-card .dash-detail { font-size: 12px; color: #4a5568; margin-top: 4px; }

  /* Priority */
  .priority-box { background: linear-gradient(135deg, #1a1a2e, #0f3460); color: white; border-radius: 12px; padding: 24px 28px; }
  .priority-box h3 { color: #63b3ed; margin-bottom: 16px; font-size: 16px; }
  .priority-item { background: rgba(255,255,255,0.08); border-radius: 8px; padding: 14px 18px; margin-bottom: 10px; display: flex; gap: 14px; align-items: flex-start; }
  .priority-item:last-child { margin-bottom: 0; }
  .priority-num { font-size: 24px; font-weight: 900; color: #63b3ed; flex-shrink: 0; line-height: 1; }
  .priority-text { font-size: 14px; }
  .priority-text strong { display: block; font-size: 15px; margin-bottom: 3px; }

  /* Rescue highlight */
  .rescued-highlight { background: #f0fff4; border: 1px solid #68d391; border-radius: 6px; padding: 4px 8px; font-size: 11px; color: #276749; display: inline-block; margin-top: 4px; }

  /* Triage table */
  .triage-table td.status-rescued { color: #276749; font-weight: 700; }
  .triage-table td.status-inbox { color: #2b6cb0; font-weight: 700; }
  .triage-table td.status-trash { color: #718096; }

  .divider { height: 1px; background: #e2e8f0; margin: 20px 0; }
  .note { font-size: 12px; color: #718096; font-style: italic; margin-top: 6px; }
  .tag-auto { background: #fed7d7; color: #742a2a; font-size: 10px; font-weight: 700; padding: 1px 6px; border-radius: 8px; }
  .tag-rescue { background: #c6f6d5; color: #1c4532; font-size: 10px; font-weight: 700; padding: 1px 6px; border-radius: 8px; }
  .tag-news { background: #e9d8fd; color: #44337a; font-size: 10px; font-weight: 700; padding: 1px 6px; border-radius: 8px; }

  ul.detail-list { padding-left: 18px; }
  ul.detail-list li { margin-bottom: 4px; font-size: 13px; }

  .conflict-warn { background: #fff3cd; border: 1px solid #f6c23e; border-radius: 6px; padding: 4px 10px; font-size: 12px; color: #856404; margin-top: 6px; display: inline-block; }

  @media (max-width: 600px) {
    .header { padding: 20px; }
    .header h1 { font-size: 20px; }
    .dash-grid { grid-template-columns: 1fr 1fr; }
  }
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════════════════════════════════
     HEADER
════════════════════════════════════════════════════════════ -->
<div class="header">
  <h1>📋 Executive Briefing</h1>
  <div class="subtitle">Good morning, Melissa — Friday, August 14, 2026</div>
  <div class="meta">
    <div class="meta-item"><strong>50</strong>Total Emails Reviewed</div>
    <div class="meta-item"><strong>7</strong>Calendar Events</div>
    <div class="meta-item"><strong>4</strong>Action Required</div>
    <div class="meta-item"><strong>5</strong>Job Leads Today</div>
    <div class="meta-item"><strong>3</strong>RSVPs Pending</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 0 — EMAIL TRIAGE QUICK LIST
════════════════════════════════════════════════════════════ -->
<div class="section theme-triage card">
  <div class="section-title">📬 Email Triage Quick List</div>
  <table class="triage-table">
    <thead>
      <tr>
        <th style="width:120px">Status</th>
        <th style="width:200px">From</th>
        <th>Subject</th>
        <th>Summary</th>
      </tr>
    </thead>
    <tbody>
      <!-- RESCUED EMAILS (5) -->
      <tr>
        <td class="status-rescued">✅ RESCUED</td>
        <td>Kohl's</td>
        <td>Nice work! Here's your Kohl's Cash.</td>
        <td><span class="tag-rescue">RESCUED</span> Earned reward from real purchase — keep for redemption</td>
      </tr>
      <tr>
        <td class="status-rescued">✅ RESCUED</td>
        <td>Kohl's</td>
        <td>Your Kohls.com account has been updated.</td>
        <td><span class="tag-rescue">RESCUED</span> Account security notification — keep for records (Aug 13, 23:08)</td>
      </tr>
      <tr>
        <td class="status-rescued">✅ RESCUED</td>
        <td>Kohl's</td>
        <td>Thanks for your order.</td>
        <td><span class="tag-rescue">RESCUED</span> Order confirmation / receipt — keep for records</td>
      </tr>
      <tr>
        <td class="status-rescued">✅ RESCUED</td>
        <td>Kohl's</td>
        <td>Your Kohls.com account has been updated.</td>
        <td><span class="tag-rescue">RESCUED</span> Account security notification — keep for records (Aug 13, 23:05)</td>
      </tr>
      <!-- INBOX EMAILS (individual) -->
      <tr>
        <td class="status-inbox">📥 INBOX</td>
        <td>Lauren Ayala (LinkedIn)</td>
        <td>Interim Chief People Officer Opportunity</td>
        <td>Recruiter outreach for Interim CPO role — high priority, respond today</td>
      </tr>
      <tr>
        <td class="status-inbox">📥 INBOX</td>
        <td>Indeed</td>
        <td>Contract Director of HR @ MRI — $85–$115/hr</td>
        <td>Strong match for background — contract HR director at managed resources</td>
      </tr>
      <tr>
        <td class="status-inbox">📥 INBOX</td>
        <td>LinkedIn Job Alerts</td>
        <td>Head of HRBP (Bilingual English/Chinese) at AfterShip</td>
        <td>Actively recruiting — bilingual requirement; review fit</td>
      </tr>
      <tr>
        <td class="status-inbox">📥 INBOX</td>
        <td>LinkedIn Job Alerts</td>
        <td>People Business Partner Director at Andela</td>
        <td>Actively recruiting — review immediately</td>
      </tr>
      <tr>
        <td class="status-inbox">📥 INBOX</td>
        <td>Monica (monica.im)</td>
        <td>[Monica] Back Up Data Scheduled for Deletion by Aug 23</td>
        <td>⚠️ Data backup deletion deadline Aug 23 — action needed before cutoff</td>
      </tr>
      <tr>
        <td class="status-inbox">📥 INBOX</td>
        <td>Duane Reade Pharmacy</td>
        <td>Your Rx is ready for pickup</td>
        <td>Prescription ready at Duane Reade/Walgreens — pick up today</td>
      </tr>
      <tr>
        <td class="status-inbox">📥 INBOX</td>
        <td>Amazon</td>
        <td>Shipped: 1 Luggage item</td>
        <td>Luggage shipment confirmed and on its way</td>
      </tr>
      <tr>
        <td class="status-inbox">📥 INBOX</td>
        <td>Amazon (return@amazon.com)</td>
        <td>Return request confirmed — Saodimallsu items &amp; 3 others</td>
        <td>Return for Sophie (not Melissa?) — confirm correct account / items</td>
      </tr>
      <tr>
        <td class="status-inbox">📥 INBOX</td>
        <td>Match.com</td>
        <td>Melissa, you've still got an unread message.</td>
        <td>Unread dating app message — personal, low urgency</td>
      </tr>
      <tr>
        <td class="status-inbox">📥 INBOX</td>
        <td>ChatGPT / OpenAI</td>
        <td>Turn your hook into a caption</td>
        <td>Marketing copy tip from ChatGPT — low priority, informational</td>
      </tr>
      <tr>
        <td class="status-inbox">📥 INBOX</td>
        <td>LinkedIn Job Alerts</td>
        <td>Head of People, Prism Media LLC at Soros Fund Management</td>
        <td>6 school alumni — notable employer, review fit</td>
      </tr>
      <tr>
        <td class="status-inbox">📥 INBOX</td>
        <td>LinkedIn Job Alerts</td>
        <td>People Partner, DC Operations at Fluidstack — up to $232K/yr</td>
        <td>High comp, 1 school alum — review requirements</td>
      </tr>
      <tr>
        <td class="status-inbox">📥 INBOX</td>
        <td>Melissa W (self)</td>
        <td>Chat like human</td>
        <td>Self-sent LinkedIn post link on making ChatGPT sound human</td>
      </tr>
      <tr>
        <td class="status-inbox">📥 INBOX</td>
        <td>Melissa W (self)</td>
        <td>(no subject)</td>
        <td>Self-sent LinkedIn post link on Claude AI capabilities</td>
      </tr>
      <tr>
        <td class="status-inbox">📥 INBOX</td>
        <td>Medium Daily Digest</td>
        <td>The Single Most Prevalent AI Writing Tell</td>
        <td><span class="tag-news">NEWSLETTER</span> Newsletter also auto-trashed — see Trash Review</td>
      </tr>
      <!-- TRASH SUMMARY ROWS -->
      <tr style="background:#fff5f5;">
        <td class="status-trash">🗑 TRASHED (auto)</td>
        <td colspan="2"><em>8 emails auto-trashed (phishing / scam / newsletter)</em></td>
        <td>See Trash Review — Security &amp; Newsletter sections</td>
      </tr>
      <tr style="background:#f7fafc;">
        <td class="status-trash">🗂 TRASH (manual)</td>
        <td colspan="2"><em>19 emails in Trash (manual / promotional / newsletters)</em></td>
        <td>See Trash Review section for full breakdown</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 2 — EXECUTIVE SUMMARY
════════════════════════════════════════════════════════════ -->
<div class="section theme-blue card">
  <div class="section-title">⚡ Executive Summary</div>
  <ul class="exec-bullets">
    <li style="background:#fff5f5; border-left:4px solid #e53e3e;">
      <span class="icon">🔴</span>
      <div><strong>Biggest Risk:</strong> Monica (monica.im) is deleting your backed-up data on <strong>August 23</strong> due to a company transition. You must download/export your data before the deadline or it will be permanently lost. Additionally, your Kohl's account shows two rapid "account updated" notifications — verify no unauthorized access occurred.</div>
    </li>
    <li style="background:#f0fff4; border-left:4px solid #38a169;">
      <span class="icon">🟢</span>
      <div><strong>Biggest Job Search Opportunity:</strong> A recruiter named <strong>Lauren Ayala</strong> reached out via LinkedIn about an <strong>Interim Chief People Officer</strong> role — this is your highest-value inbound today. Additionally, Indeed flagged a <strong>Contract HR Director at MRI at $85–$115/hr</strong> and LinkedIn surfaced four more strong leads including a $232K People Partner at Fluidstack and Head of People at Soros Fund Management.</div>
    </li>
    <li style="background:#ebf8ff; border-left:4px solid #3182ce;">
      <span class="icon">🔵</span>
      <div><strong>Biggest Calendar Item:</strong> <strong>Stella's vet appointment</strong> is Tuesday Aug 18, 10–11am (confirmed). The <strong>HR Networking &amp; Job Search Group Zoom</strong> is Wednesday Aug 19, 12–1:30pm — your RSVP is still pending (<em>needsAction</em>). The <strong>Executive Roundtable</strong> on Aug 20 is marked declined — confirm this is intentional.</div>
    </li>
  </ul>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 3 — ACTION REQUIRED
════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title" style="background:#fed7d7; color:#742a2a; border-radius:8px;">🚨 Action Required</div>

  <div class="action-card action-card-red">
    <span class="badge badge-red">URGENT</span> <span class="badge badge-yellow">DEADLINE</span>
    <h4>⚠️ Monica Data Backup — Scheduled Deletion Aug 23</h4>
    <div class="meta-row">
      <span><strong>From:</strong> Monica (noreply@monica.im)</span>
      <span><strong>Due:</strong> August 23, 2026 at 8:00 AM SGT</span>
    </div>
    <p style="margin-top:10px; font-size:13px;">Monica (an AI product by Butterfly Effect, now transitioning to independent operation) will permanently delete your data on Aug 23. You have 9 days. Log in, export your data, and download all backups before the deadline.</p>
    <div class="meta-row"><span><strong>Next Step:</strong> Log into Monica.im → Settings → Export Data → Download all before Aug 22</span></div>
  </div>

  <div class="action-card action-card-green">
    <span class="badge badge-green">JOB SEARCH</span> <span class="badge badge-high">HIGH PRIORITY</span>
    <h4>💼 Respond to Recruiter — Interim Chief People Officer</h4>
    <div class="meta-row">
      <span><strong>From:</strong> Lauren Ayala via LinkedIn</span>
      <span><strong>Due:</strong> Today (Friday Aug 14)</span>
    </div>
    <p style="margin-top:10px; font-size:13px;">Inbound recruiter message for an Interim CPO role. Interim/fractional CPO roles are highly sought after and recruiters move fast. Reply today to express interest and request details.</p>
    <div class="meta-row"><span><strong>Next Step:</strong> Reply to LinkedIn InMail from Lauren Ayala — confirm interest, attach updated resume, ask for role details and timeline</span></div>
  </div>

  <div class="action-card action-card-yellow">
    <span class="badge badge-yellow">RSVP NEEDED</span>
    <h4>📅 RSVP: HR Networking &amp; Job Search Group Zoom — Aug 19</h4>
    <div class="meta-row">
      <span><strong>From:</strong> Google Calendar</span>
      <span><strong>When:</strong> Wednesday, Aug 19, 12:00–1:30 PM ET</span>
    </div>
    <p style="margin-top:10px; font-size:13px;">Your RSVP is marked <em>needsAction</em> for this large HR networking Zoom (150+ attendees). You also have a separate "Network" event confirmed at the same time — likely the same meeting. RSVP formally so organizers can count you in.</p>
    <div class="meta-row"><span><strong>Next Step:</strong> Accept the calendar invite; check Zoom link: us06web.zoom.us/j/81954171722</span></div>
  </div>

  <div class="action-card action-card-yellow">
    <span class="badge badge-yellow">RSVP NEEDED</span>
    <h4>📅 RSVP: HR Networking Open Office Hours — Aug 20</h4>
    <div class="meta-row">
      <span><strong>From:</strong> Google Calendar</span>
      <span><strong>When:</strong> Thursday, Aug 20, 12:00–1:00 PM ET</span>
    </div>
    <p style="margin-top:10px; font-size:13px;">Open office hours networking session with the same HR group. No automated AI notetaking per the organizer's note. Your RSVP is <em>needsAction</em>.</p>
    <div class="meta-row"><span><strong>Next Step:</strong> Accept or decline. If attending, disable any AI note-taking tools as requested by organizer.</span></div>
  </div>

  <div class="action-card action-card-blue">
    <span class="badge badge-blue">HEALTH</span>
    <h4>💊 Prescription Ready for Pickup — Duane Reade / Walgreens</h4>
    <div class="meta-row">
      <span><strong>From:</strong> Duane Reade Pharmacy (donotreply@rxtx.walgreens.com)</span>
      <span><strong>Due:</strong> Today or weekend</span>
    </div>
    <p style="margin-top:10px; font-size:13px;">Your Rx is ready at Duane Reade by Walgreens. Note the email mentions possible recent store hour changes — check hours before going.</p>
    <div class="meta-row"><span><strong>Next Step:</strong> Confirm pharmacy hours, pick up prescription today or this weekend</span></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 4 — FULL 7-DAY CALENDAR
════════════════════════════════════════════════════════════ -->
<div class="section theme-blue card">
  <div class="section-title">📅 Full 7-Day Calendar — Aug 14–20, 2026</div>

  <!-- Friday Aug 14 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Friday, August 14, 2026 — TODAY</div>
    <div class="no-events">No calendar events scheduled today. Focus on email triage, responding to Lauren Ayala (recruiter), and Rx pickup.</div>
  </div>

  <!-- Saturday Aug 15 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Saturday, August 15, 2026</div>
    <div class="no-events">No events scheduled.</div>
  </div>

  <!-- Sunday Aug 16 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Sunday, August 16, 2026</div>
    <div class="no-events">No events scheduled.</div>
  </div>

  <!-- Monday Aug 17 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Monday, August 17, 2026</div>
    <div class="no-events">No events scheduled. Good day to follow up on job applications sent this week.</div>
  </div>

  <!-- Tuesday Aug 18 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Tuesday, August 18, 2026</div>
    <div class="cal-event">
      <h4>🐾 Stella — Vet Appointment</h4>
      <div class="cal-meta">
        <strong>Time:</strong> 10:00 AM – 11:00 AM ET &nbsp;|&nbsp;
        <span class="rsvp-confirmed">✅ Confirmed</span>
      </div>
      <div class="cal-meta"><strong>Location:</strong> Not specified</div>
      <div class="cal-meta"><strong>Note:</strong> Two calendar entries exist for this event ("Vet" and "Stella vet") — same time, both confirmed. Likely a duplicate. No conflict otherwise.</div>
      <div class="cal-meta"><strong>Prep:</strong> Confirm vet address, gather any records/medications, arrange transport for Stella</div>
      <div class="conflict-warn">⚠️ Duplicate event detected: "Vet" and "Stella vet" both at 10–11am. Safe — same appointment, no conflict.</div>
    </div>
  </div>

  <!-- Wednesday Aug 19 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Wednesday, August 19, 2026</div>
    <div class="cal-event">
      <h4>🤝 HR Networking &amp; Job Search Group — Zoom Session 2</h4>
      <div class="cal-meta">
        <strong>Time:</strong> 12:00 PM – 1:30 PM ET &nbsp;|&nbsp;
        <span class="rsvp-needs">⏳ RSVP Pending (needsAction)</span>
      </div>
      <div class="cal-meta"><strong>Attendees:</strong> 150+ HR professionals</div>
      <div class="cal-meta"><strong>Zoom:</strong> <span class="cal-link">https://us06web.zoom.us/j/81954171722?pwd=5jPMH9YWqdAg9bxMvAh3BEKmGfb4DK.1</span></div>
      <div class="cal-meta"><strong>Prep:</strong> Review HR Networking Team Guidelines (link in invite), prepare your 30-second intro / current search status, bring 2–3 job leads to share</div>
      <div class="conflict-warn">⚠️ ACTION REQUIRED: RSVP still pending — accept invite today</div>
    </div>
    <div class="cal-event">
      <h4>📌 Network (duplicate/companion)</h4>
      <div class="cal-meta">
        <strong>Time:</strong> 12:00 PM – 1:30 PM ET &nbsp;|&nbsp;
        <span class="rsvp-confirmed">✅ Confirmed</span>
      </div>
      <div class="cal-meta"><strong>Note:</strong> Appears to be a companion/personal reminder for the HR Networking Zoom above. No separate location listed.</div>
    </div>
    <div class="cal-event">
      <h4>☕ M&amp;m — Meeting with Monte Montoya</h4>
      <div class="cal-meta">
        <strong>Time:</strong> 2:00 PM – 3:00 PM ET &nbsp;|&nbsp;
        <span class="rsvp-accepted">✅ Accepted</span>
      </div>
      <div class="cal-meta"><strong>Attendee:</strong> monte.montoya@gmail.com</div>
      <div class="cal-meta"><strong>Location:</strong> Not specified (likely virtual or in-person TBD)</div>
      <div class="cal-meta"><strong>Prep:</strong> Confirm meeting format (Zoom/phone/in-person) with Monte; prepare agenda or talking points</div>
    </div>
  </div>

  <!-- Thursday Aug 20 -->
  <div class="cal-day">
    <div class="cal-day-header">📅 Thursday, August 20, 2026</div>
    <div class="cal-event">
      <h4>🏢 Executive Roundtable — John Madigan (Zoom)</h4>
      <div class="cal-meta">
        <strong>Time:</strong> 9:00 AM – 10:30 AM ET &nbsp;|&nbsp;
        <span class="rsvp-declined">❌ DECLINED</span>
      </div>
      <div class="cal-meta"><strong>Host:</strong> John Madigan</div>
      <div class="cal-meta"><strong>Zoom:</strong> <span class="cal-link">https://us02web.zoom.us/j/207786667 | Meeting ID: 207 786 667 | Password: 205454</span></div>
      <div class="cal-meta"><strong>Note:</strong> You have declined this event. If this was unintentional or if you want to reconsider, re-RSVP before the meeting date. Executive Roundtables can be valuable networking — confirm decline is intentional.</div>
      <div class="conflict-warn">⚠️ Declined — Verify this was intentional. John Madigan appears to be a known contact worth nurturing.</div>
    </div>
    <div class="cal-event">
      <h4>🤝 HR Networking &amp; Job Search: Open Office Hours — Zoom 2</h4>
      <div class="cal-meta">
        <strong>Time:</strong> 12:00 PM – 1:00 PM ET &nbsp;|&nbsp;
        <span class="rsvp-needs">⏳ RSVP Pending (needsAction)</span>
      </div>
      <div class="cal-meta"><strong>Attendees:</strong> 150+ HR professionals</div>
      <div class="cal-meta"><strong>Zoom:</strong> <span class="cal-link">https://us06web.zoom.us/j/85945371140?pwd=cmD1eXbMqRxNobikQODOI9IpHlVXbX.1</span></div>
      <div class="cal-meta"><strong>Organizer Note:</strong> Please disable AI notetaking tools. Open discussion — no recording.</div>
      <div class="cal-meta"><strong>Prep:</strong> Prepare job search updates, disable AI note-taker, bring connection goals</div>
      <div class="conflict-warn">⚠️ ACTION REQUIRED: RSVP still pending</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 5 — JOB SEARCH & INTERVIEW PIPELINE
════════════════════════════════════════════════════════════ -->
<div class="section theme-green card">
  <div class="section-title">💼 Job Search &amp; Interview Pipeline</div>

  <table>
    <thead>
      <tr>
        <th>Fit</th>
        <th>Role / Employer</th>
        <th>Source</th>
        <th>Details</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="badge badge-high">HIGH</span></td>
        <td><strong>Interim Chief People Officer</strong><br><em>Unknown Employer</em></td>
        <td>LinkedIn InMail — Lauren Ayala (Recruiter)</td>
        <td>Direct recruiter outreach, unread. Interim CPO perfectly matches Melissa's HR leadership background.</td>
        <td>⭐ <strong>Reply TODAY</strong> — highest priority lead</td>
      </tr>
      <tr>
        <td><span class="badge badge-high">HIGH</span></td>
        <td><strong>Contract Director of Human Resources</strong><br><em>Managed Resources, Inc (MRI)</em></td>
        <td>Indeed — donotreply@match.indeed.com</td>
        <td>$85–$115/hr contract. "Extensive HR leadership experience — strong match." Hourly rate is executive-level.</td>
        <td>⭐ <strong>Apply or respond today</strong></td>
      </tr>
      <tr>
        <td><span class="badge badge-high">HIGH</span></td>
        <td><strong>Head of People, Prism Media LLC</strong><br><em>Soros Fund Management</em></td>
        <td>LinkedIn Job Alerts</td>
        <td>6 school alumni at the company — strong network leverage. High-prestige employer.</td>
        <td>Review today, apply if fit</td>
      </tr>
      <tr>
        <td><span class="badge badge-med">MED</span></td>
        <td><strong>People Partner, DC Operations</strong><br><em>Fluidstack</em></td>
        <td>LinkedIn Job Alerts</td>
        <td>Up to $232K/year. 1 school alum. DC-based operations role — confirm location/remote.</td>
        <td>Review requirements, apply if role is remote-friendly</td>
      </tr>
      <tr>
        <td><span class="badge badge-med">MED</span></td>
        <td><strong>People Business Partner Director</strong><br><em>Andela</em></td>
        <td>LinkedIn Job Alerts</td>
        <td>Actively recruiting. Andela is a well-known tech talent company.</td>
        <td>Review today, apply if fit</td>
      </tr>
      <tr>
        <td><span class="badge badge-med">MED</span></td>
        <td><strong>Head of HRBP (Bilingual English/Chinese)</strong><br><em>AfterShip</em></td>
        <td>LinkedIn Job Alerts</td>
        <td>Actively recruiting. Bilingual requirement may limit fit if not fluent in Mandarin/Chinese.</td>
        <td>Review language requirement — apply if bilingual fit</td>
      </tr>
      <tr>
        <td><span class="badge badge-low">LOW</span></td>
        <td><strong>Chief People Officer / Lead Talent Culture Change</strong><br><em>Multiple (JobLeads)</em></td>
        <td>JobLeads alert (in Trash)</td>
        <td>5 new jobs matching saved search for Aug 14. Email was trashed. Worth checking if JobLeads portal has quality matches.</td>
        <td>Log into JobLeads to review 5 matches directly</td>
      </tr>
    </tbody>
  </table>

  <div style="margin-top:14px;">
    <div class="card" style="background:#f0fff4; border:1px solid #68d391;">
      <strong>🤝 Networking Meetings This Week:</strong>
      <ul class="detail-list" style="margin-top:8px;">
        <li><strong>Wed Aug 19, 12–1:30pm</strong> — HR Networking &amp; Job Search Group Zoom (150+ HR pros) — RSVP pending</li>
        <li><strong>Wed Aug 19, 2–3pm</strong> — 1:1 meeting with Monte Montoya (confirmed)</li>
        <li><strong>Thu Aug 20, 12–1pm</strong> — HR Open Office Hours Zoom — RSVP pending</li>
      </ul>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 6 — FULL EMAIL REVIEW BY CATEGORY
════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-title" style="background:#2d3748; color:white; border-radius:8px;">📂 Full Email Review by Category</div>

  <!-- SECURITY / RISK -->
  <div class="section theme-red card" style="margin-top:14px;">
    <div class="section-title">🔴 Security / Risk — 7 Emails</div>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>Kristalina Georgievar (spoofed @whirlpool.com)</td>
          <td>Attn: Beneficiary</td>
          <td><span class="tag-auto">AUTO-TRASHED</span> Phishing — IMF advance-fee scam with fake Swift reference numbers</td>
          <td>No action needed — already removed</td>
        </tr>
        <tr>
          <td>"Ace Hardware" (from yudbm@ma4u3rap.com)</td>
          <td>melissaw212 — You have won a YETI PATRIOTIC Bundle ID#9848</td>
          <td><span class="tag-auto">AUTO-TRASHED</span> Phishing — fake prize/giveaway impersonating Ace Hardware</td>
          <td>No action needed — already removed</td>
        </tr>
        <tr>
          <td>"Payment_Declined" (random domain)</td>
          <td>melissaw212 Account Has been Blocked! Photos/Videos will be Removed</td>
          <td><span class="tag-auto">AUTO-TRASHED</span> Phishing — credential/payment harvesting, account-block threat</td>
          <td>No action needed — already removed</td>
        </tr>
        <tr>
          <td>"Cloud.Storage.Team" (random domain)</td>
          <td>melissaw212 Your photos videos and backups are being erased</td>
          <td><span class="tag-auto">AUTO-TRASHED</span> Phishing — fake cloud storage/antivirus payment failure</td>
          <td>No action needed — already removed</td>
        </tr>
        <tr>
          <td>Kohl's (t.kohls.com)</td>
          <td>Your Kohls.com account has been updated (×2 notifications)</td>
          <td><span class="tag-rescue">RESCUED</span> Legitimate account update — but two notifications in quick succession is notable</td>
          <td>✅ Review Kohl's account for unauthorized changes — change password if unsure</td>
        </tr>
        <tr>
          <td>Monica (noreply@monica.im)</td>
          <td>[Monica] Back Up Data Scheduled for Deletion by Aug 23</td>
          <td>Legitimate — product transition notice</td>
          <td>🚨 Export/download all data before Aug 23, 8am SGT</td>
        </tr>
        <tr>
          <td>Amazon (return@amazon.com)</td>
          <td>Return request confirmed for Sophie (not Melissa)</td>
          <td>⚠️ Addressed to "Sophie" — possible wrong account or shared account concern</td>
          <td>Verify this return was intentional and under correct account</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- JOB SEARCH -->
  <div class="section theme-green card" style="margin-top:14px;">
    <div class="section-title">🟢 Job Search — 7 Emails</div>
    <table>
      <thead><tr><th>Sender</th><th>Role / Subject</th><th>Fit</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>Lauren Ayala (LinkedIn InMail)</td>
          <td>Interim Chief People Officer Opportunity</td>
          <td><span class="badge badge-high">HIGH</span></td>
          <td>Reply today — direct recruiter outreach</td>
        </tr>
        <tr>
          <td>Indeed</td>
          <td>Contract Director of HR @ MRI — $85–$115/hr</td>
          <td><span class="badge badge-high">HIGH</span></td>
          <td>Apply or respond today</td>
        </tr>
        <tr>
          <td>LinkedIn Job Alerts</td>
          <td>Head of People, Prism Media LLC @ Soros Fund Management</td>
          <td><span class="badge badge-high">HIGH</span></td>
          <td>Review and apply — 6 school alumni</td>
        </tr>
        <tr>
          <td>LinkedIn Job Alerts</td>
          <td>People Partner, DC Operations @ Fluidstack — up to $232K/yr</td>
          <td><span class="badge badge-med">MED</span></td>
          <td>Review comp and location fit</td>
        </tr>
        <tr>
          <td>LinkedIn Job Alerts</td>
          <td>People Business Partner Director @ Andela</td>
          <td><span class="badge badge-med">MED</span></td>
          <td>Review and apply if fit</td>
        </tr>
        <tr>
          <td>LinkedIn Job Alerts</td>
          <td>Head of HRBP (Bilingual English/Chinese) @ AfterShip</td>
          <td><span class="badge badge-med">MED</span></td>
          <td>Review bilingual requirement</td>
        </tr>
        <tr>
          <td>JobLeads (in Trash)</td>
          <td>5 new jobs matching CPO/Lead Talent search</td>
          <td><span class="badge badge-low">LOW</span></td>
          <td>Log into JobLeads portal to review matches</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- RECRUITERS / NETWORKING -->
  <div class="section theme-green card" style="margin-top:14px;">
    <div class="section-title">🤝 Recruiters / Networking — 1 Email (see also Job Search)</div>
    <p style="padding:8px 4px; font-size:13px;">Lauren Ayala's LinkedIn InMail is the primary recruiter contact today (covered in Job Search above). The HR Networking Zoom group is covered under Calendar Events.</p>
  </div>

  <!-- CALENDAR / EVENTS -->
  <div class="section theme-blue card" style="margin-top:14px;">
    <div class="section-title">🔵 Calendar / Events — See Full Calendar Section</div>
    <p style="padding:8px 4px; font-size:13px;">All calendar events are covered in the Full 7-Day Calendar section above. RSVPs needed for Aug 19 and Aug 20 Zoom sessions. Executive Roundtable on Aug 20 is declined — verify intentional.</p>
  </div>

  <!-- MEDICAL / HEALTH -->
  <div class="section theme-yellow card" style="margin-top:14px;">
    <div class="section-title">🟡 Medical / Health — 1 Email</div>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>Duane Reade Pharmacy (donotreply@rxtx.walgreens.com)</td>
          <td>Melissa, your Rx is ready for pickup</td>
          <td>✅ Check store hours (may have changed), pick up today or this weekend</td>
        </tr>
      </tbody>
    </table>
    <p class="note">Note: Stella's vet appointment (Aug 18) is on calendar — not from email.</p>
  </div>

  <!-- FINANCIAL / BILLING -->
  <div class="section theme-yellow card" style="margin-top:14px;">
    <div class="section-title">🟡 Financial / Billing — 5 Emails (Kohl's + Amazon + GapCash)</div>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>Kohl's (t.kohls.com)</td>
          <td>Nice work! Here's your Kohl's Cash.</td>
          <td><span class="tag-rescue">RESCUED FROM TRASH</span></td>
          <td>✅ Note your Kohl's Cash amount; use before expiration</td>
        </tr>
        <tr>
          <td>Kohl's (t.kohls.com)</td>
          <td>Your Kohls.com account has been updated (×2)</td>
          <td><span class="tag-rescue">RESCUED FROM TRASH</span></td>
          <td>✅ Keep for records; verify no unauthorized changes</td>
        </tr>
        <tr>
          <td>Kohl's (t.kohls.com)</td>
          <td>Thanks for your order.</td>
          <td><span class="tag-rescue">RESCUED FROM TRASH</span></td>
          <td>✅ Keep as purchase receipt</td>
        </tr>
        <tr>
          <td>Amazon (shipment-tracking@amazon.com)</td>
          <td>Shipped: 1 Luggage item</td>
          <td>In Inbox — legitimate</td>
          <td>Track delivery; note ETA</td>
        </tr>
        <tr>
          <td>Amazon (return@amazon.com)</td>
          <td>Return request confirmed — "Sophie" — 4 items</td>
          <td>In Inbox — addressed to "Sophie" — flag</td>
          <td>⚠️ Verify return is yours; "Sophie" name is unusual — check Amazon account</td>
        </tr>
        <tr>
          <td>GapCash (gap@email.gap.com)</td>
          <td>You earned GapCash</td>
          <td>In Trash (manual)</td>
          <td>Check GapCash amount/expiration — may be worth saving</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- PROFESSIONAL DEVELOPMENT -->
  <div class="section theme-purple card" style="margin-top:14px;">
    <div class="section-title">🟣 Professional Development — 3 Emails</div>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>ChatGPT / OpenAI (noreply@email.openai.com)</td>
          <td>Turn your hook into a caption — draft marketing copy</td>
          <td>Low priority — informational tip on using ChatGPT for content creation</td>
        </tr>
        <tr>
          <td>Google / Coursera (no-reply@m.learn.coursera.org)</td>
          <td>🚀 New Course! Learn to create your own app, no coding required (in Trash)</td>
          <td>Low priority — review if vibe coding/no-code tools interest you</td>
        </tr>
        <tr>
          <td>Melissa W (self — melissaw212@gmail.com)</td>
          <td>"Chat like human" — LinkedIn post link (self-sent)</td>
          <td>Review saved LinkedIn post on humanizing ChatGPT output</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- PERSONAL -->
  <div class="section card" style="background:#faf5ff; border-left:5px solid #805ad5; margin-top:14px;">
    <div class="section-title" style="background:#e9d8fd; color:#44337a; border-radius:8px;">💜 Personal — 3 Emails</div>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>Match.com (mailer@value.match.com)</td>
          <td>Melissa, you've still got an unread message</td>
          <td>Personal — check message when convenient</td>
        </tr>
        <tr>
          <td>Jdate (hello@mail.jdate.com) — in Trash</td>
          <td>You've Caught Someone's Eye 👀</td>
          <td>Personal — in trash; review if desired</td>
        </tr>
        <tr>
          <td>Melissa W (self — melissaw212@gmail.com)</td>
          <td>(no subject) — LinkedIn post link about Claude AI</td>
          <td>Self-sent resource on Claude AI capabilities — review when ready</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- NEWSLETTERS / SUBSCRIPTIONS -->
  <div class="section theme-purple card" style="margin-top:14px;">
    <div class="section-title">📰 Newsletters &amp; Subscriptions — 5 Emails</div>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Recommendation</th></tr></thead>
      <tbody>
        <tr>
          <td>Medium Daily Digest (noreply@medium.com)</td>
          <td>The Single Most Prevalent AI Writing Tell</td>
          <td><span class="tag-news">AUTO-TRASHED (Newsletter)</span></td>
          <td>Unsubscribe or filter to folder — relevant to AI interest but cluttering inbox</td>
        </tr>
        <tr>
          <td>"1% Better" (hello@onepercentimprovements.convertkit.com)</td>
          <td>CA Golden Visas, Europe's Eclipse, and 8 Short Life-Changing Books</td>
          <td>In Trash (manual)</td>
          <td>Unsubscribe if no longer reading</td>
        </tr>
        <tr>
          <td>"Dylan's Diary" (newsletter@lg.behindthemarkets.com)</td>
          <td>Why Have Diamond Prices Crashed 60%?</td>
          <td>In Trash (manual)</td>
          <td>Review if financial content is relevant — otherwise unsubscribe</td>
        </tr>
        <tr>
          <td>The Daily Skimm (dailyskimm@morning7.theskimm.com)</td>
          <td>Marco Rubio got framed for his birthday</td>
          <td>In Trash (manual)</td>
          <td>Keep if you enjoy daily news digest — otherwise unsubscribe</td>
        </tr>
        <tr>
          <td>Alison Courses (noreply@us-news.alison.com)</td>
          <td>Melissa A, your guide to getting better at "adulting"</td>
          <td>In Trash (manual)</td>
          <td>Unsubscribe — low relevance at executive level</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- PROMOTIONAL / RETAIL -->
  <div class="section theme-gray card" style="margin-top:14px;">
    <div class="section-title">🛍️ Promotional / Retail — 6 Emails</div>
    <table>
      <thead><tr><th>Sender</th><th>Subject</th><th>Status</th><th>Recommendation</th></tr></thead>
      <tbody>
        <tr>
          <td>Kohl's (Kohls@s.kohls.com)</td>
          <td>Save 30% — Fill your cart with deals on active gear 🛒</td>
          <td>In Trash (manual)</td>
          <td>Delete — promotional, already trashed</td>
        </tr>
        <tr>
          <td>Gap Factory (gap@email.gapfactory.com)</td>
          <td>Your email-exclusive bonus: extra 15% off + free shipping</td>
          <td>In Trash (manual)</td>
          <td>Delete or use before expiry — 50% off + extra 15%</td>
        </tr>
        <tr>
          <td>GapCash (gap@email.gap.com)</td>
          <td>You earned GapCash</td>
          <td>In Trash (manual)</td>
          <td>✅ Rescue — check GapCash code before it expires</td>
        </tr>
        <tr>
          <td>SHEIN (shein@market-us.shein.com)</td>
          <td>All under $19.99 | Clearance Chic</td>
          <td>In Trash (manual)</td>
          <td>Delete — low priority promotional</td>
        </tr>
        <tr>
          <td>Gemma Bonham-Carter (hello@gemmabonhamcarter.com)</td>
          <td>Last call on the Teachery lifetime deal ($550→$750 at midnight)</td>
          <td>In Trash (manual)</td>
          <td>Review if course creation interests you — deal expired today at midnight</td>
        </tr>
        <tr>
          <td>Blink (noreply@blink.new)</td>
          <td>Some ideas for your first project</td>
          <td>In Trash (manual)</td>
          <td>Delete unless actively using Blink app</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- SPAM / ADULT CONTENT -->
  <div class="section theme-red card" style="margin-top:14px;">
    <div class="section-title">🔴 Spam / Adult / Unsolicited — 9 Emails</div>
    <p style="padding:4px 4px 10px; font-size:13px; color:#742a2a;">These are explicit spam, adult content, and fake health/pharmaceutical scam emails. All should be deleted. None require any action.</p>
    <table>
      <thead><tr><th>Sender</th><th>Subject (summarized)</th><th>Status</th><th>Action</th></tr></thead>
      <tbody>
        <tr>
          <td>Dr. Victor Kane (random domain)</td>
          <td>At-Home Method Doctors Don't Want You to Know (+3.8")</td>
          <td>Not trashed (spam)</td>
          <td>Delete — explicit spam</td>
        </tr>
        <tr>
          <td>"F*ckMeHard" (random domain)</td>
          <td>Explicit adult content subject</td>
          <td>Not trashed (spam)</td>
          <td>Delete — explicit spam</td>
        </tr>
        <tr>
          <td>"Sex Trick" (random domain)</td>
          <td>Naughty porn star reveals secret to staying hard for hours</td>
          <td>Not trashed (spam)</td>
          <td>Delete — explicit spam</td>
        </tr>
        <tr>
          <td>"Sex Without Censorship" (random domain) ×2</td>
          <td>Sydney Sweeney's secret / Your wife will thank you</td>
          <td>Not trashed (spam)</td>
          <td>Delete — explicit spam</td>
