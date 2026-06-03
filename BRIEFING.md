<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Daily Briefing – Wednesday, June 3, 2026</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #1a1a2e; font-size: 15px; line-height: 1.6; }
  .wrapper { max-width: 900px; margin: 0 auto; padding: 20px; }

  /* HEADER */
  .header { background: linear-gradient(135deg, #0d1b4b 0%, #1a3a8f 100%); color: white; padding: 36px 32px; border-radius: 14px; margin-bottom: 24px; }
  .header h1 { font-size: 28px; font-weight: 700; letter-spacing: 0.5px; }
  .header .date { font-size: 16px; opacity: 0.85; margin-top: 6px; }
  .header .subtitle { font-size: 13px; opacity: 0.65; margin-top: 4px; letter-spacing: 1px; text-transform: uppercase; }

  /* SECTION TITLES */
  .section { margin-bottom: 28px; }
  .section-title { font-size: 19px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.8px; padding: 10px 16px; border-radius: 8px 8px 0 0; margin-bottom: 0; }

  /* CARDS */
  .card { border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; border-left: 5px solid; }
  .card-red { background: #fff5f5; border-color: #e53e3e; }
  .card-yellow { background: #fffbf0; border-color: #d69e2e; }
  .card-blue { background: #f0f6ff; border-color: #3182ce; }
  .card-green { background: #f0fff4; border-color: #38a169; }
  .card-purple { background: #faf5ff; border-color: #805ad5; }
  .card-gray { background: #f7f7f7; border-color: #a0aec0; }
  .card-orange { background: #fff8f0; border-color: #dd6b20; }

  .card .label { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px; }
  .label-red { color: #c53030; }
  .label-yellow { color: #b7791f; }
  .label-blue { color: #2b6cb0; }
  .label-green { color: #276749; }
  .label-purple { color: #553c9a; }
  .label-gray { color: #718096; }
  .label-orange { color: #c05621; }

  .card .title { font-size: 16px; font-weight: 700; margin-bottom: 4px; }
  .card .meta { font-size: 12px; color: #666; margin-bottom: 6px; }
  .card .summary { font-size: 14px; color: #333; margin-bottom: 8px; }
  .card .next-step { font-size: 13px; font-weight: 600; padding: 6px 10px; border-radius: 5px; display: inline-block; }
  .next-red { background: #fed7d7; color: #9b2c2c; }
  .next-yellow { background: #fefcbf; color: #744210; }
  .next-blue { background: #bee3f8; color: #1a365d; }
  .next-green { background: #c6f6d5; color: #22543d; }
  .next-purple { background: #e9d8fd; color: #322659; }
  .next-gray { background: #e2e8f0; color: #2d3748; }
  .next-orange { background: #feebc8; color: #7b341e; }

  /* SECTION HEADER COLORS */
  .sh-red { background: #e53e3e; color: white; }
  .sh-yellow { background: #d69e2e; color: white; }
  .sh-blue { background: #2b6cb0; color: white; }
  .sh-green { background: #276749; color: white; }
  .sh-purple { background: #553c9a; color: white; }
  .sh-gray { background: #718096; color: white; }
  .sh-orange { background: #dd6b20; color: white; }
  .sh-navy { background: #1a3a8f; color: white; }
  .sh-teal { background: #2c7a7b; color: white; }

  /* EXECUTIVE SUMMARY */
  .exec-summary { background: white; border-radius: 10px; padding: 22px 26px; margin-bottom: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
  .exec-summary h2 { font-size: 18px; font-weight: 800; color: #1a3a8f; margin-bottom: 14px; text-transform: uppercase; letter-spacing: 0.6px; }
  .exec-bullet { display: flex; align-items: flex-start; margin-bottom: 10px; }
  .exec-icon { font-size: 20px; margin-right: 12px; flex-shrink: 0; }
  .exec-text { font-size: 14px; color: #2d3748; }

  /* CALENDAR TABLE */
  .cal-table { width: 100%; border-collapse: collapse; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); margin-bottom: 12px; }
  .cal-table th { background: #2b6cb0; color: white; padding: 10px 14px; text-align: left; font-size: 13px; font-weight: 700; }
  .cal-table td { padding: 10px 14px; border-bottom: 1px solid #e2e8f0; font-size: 13px; vertical-align: top; }
  .cal-table tr:last-child td { border-bottom: none; }
  .cal-table tr:nth-child(even) td { background: #f7faff; }
  .status-confirmed { color: #276749; font-weight: 700; }
  .status-declined { color: #c53030; font-weight: 700; }
  .status-pending { color: #b7791f; font-weight: 700; }
  .status-allday { color: #553c9a; font-weight: 700; }

  /* ACTION TABLE */
  .action-table { width: 100%; border-collapse: collapse; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); margin-bottom: 12px; }
  .action-table th { background: #0d1b4b; color: white; padding: 10px 14px; text-align: left; font-size: 13px; font-weight: 700; }
  .action-table td { padding: 10px 14px; border-bottom: 1px solid #e2e8f0; font-size: 13px; vertical-align: top; }
  .action-table tr:last-child td { border-bottom: none; }
  .action-table tr:nth-child(even) td { background: #f9f9ff; }
  .priority-high { color: #c53030; font-weight: 700; }
  .priority-med { color: #b7791f; font-weight: 700; }
  .priority-low { color: #718096; font-weight: 700; }

  /* TOP 3 */
  .top3 { background: linear-gradient(135deg, #0d1b4b, #2b6cb0); color: white; border-radius: 12px; padding: 26px 30px; margin-bottom: 24px; }
  .top3 h2 { font-size: 20px; font-weight: 800; margin-bottom: 18px; text-transform: uppercase; letter-spacing: 0.8px; }
  .top3-item { display: flex; align-items: flex-start; margin-bottom: 14px; }
  .top3-num { background: rgba(255,255,255,0.2); border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 16px; flex-shrink: 0; margin-right: 14px; }
  .top3-text { font-size: 15px; line-height: 1.5; }
  .top3-text strong { font-size: 16px; display: block; }

  /* EMAIL ACCOUNTING */
  .accounting { background: white; border-radius: 10px; padding: 22px 26px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); margin-bottom: 24px; }
  .accounting h2 { font-size: 16px; font-weight: 800; color: #1a3a8f; margin-bottom: 14px; text-transform: uppercase; }
  .acct-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 10px; }
  .acct-cell { background: #f0f4ff; border-radius: 7px; padding: 10px 14px; }
  .acct-cell .cat { font-size: 12px; font-weight: 700; color: #2b6cb0; text-transform: uppercase; }
  .acct-cell .count { font-size: 22px; font-weight: 800; color: #0d1b4b; }

  /* DIVIDER */
  .section-wrap { background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); margin-bottom: 28px; }

  /* PROMO TABLE */
  .promo-table { width: 100%; border-collapse: collapse; }
  .promo-table th { background: #e2e8f0; color: #2d3748; padding: 8px 14px; text-align: left; font-size: 12px; font-weight: 700; text-transform: uppercase; }
  .promo-table td { padding: 9px 14px; border-bottom: 1px solid #f0f0f0; font-size: 13px; }
  .promo-table tr:last-child td { border-bottom: none; }
  .rec-delete { color: #c53030; font-weight: 700; }
  .rec-review { color: #b7791f; font-weight: 700; }
  .rec-keep { color: #276749; font-weight: 700; }
  .rec-ignore { color: #718096; font-weight: 700; }

  .section-end { font-size: 13px; font-style: italic; color: #666; padding: 10px 20px 14px; border-top: 1px solid #e2e8f0; margin-top: 6px; }

  a { color: #2b6cb0; }
  .conflict-badge { background: #fed7d7; color: #9b2c2c; font-size: 11px; font-weight: 700; padding: 2px 7px; border-radius: 10px; margin-left: 6px; }
  .day-header { background: #eef2ff; font-weight: 800; color: #1a3a8f; }
</style>
</head>
<body>
<div class="wrapper">

  <!-- ============================== HEADER ============================== -->
  <div class="header">
    <div class="subtitle">Executive Chief of Staff · Daily Briefing</div>
    <h1>Good morning, Melissa ☀️</h1>
    <div class="date">Wednesday, June 3, 2026</div>
  </div>

  <!-- ============================== EXECUTIVE SUMMARY ============================== -->
  <div class="exec-summary">
    <h2>⚡ Executive Summary</h2>
    <div class="exec-bullet">
      <div class="exec-icon">🔴</div>
      <div class="exec-text"><strong>Security Alert:</strong> Your LinkedIn password was reset today and a verification PIN (606210) was sent — confirm this was you. A separate phishing email is impersonating a cloud storage service claiming your account is locked; do not click it.</div>
    </div>
    <div class="exec-bullet">
      <div class="exec-icon">📅</div>
      <div class="exec-text"><strong>Tomorrow's Schedule (Thu, Jun 4):</strong> You have a Dr. Husk appointment at 10:30 AM (confirmed), and an HR Networking open office session at noon (no RSVP yet). You declined the Executive Roundtable at 9 AM — no action needed there.</div>
    </div>
    <div class="exec-bullet">
      <div class="exec-icon">🟢</div>
      <div class="exec-text"><strong>Job Search & Networking:</strong> A LinkedIn job alert flagged a Senior Director HRBP (AI-Native) role. You have a Zoom consult with Netta Jenkins (Jun 9) and a confirmed networking session (Jun 10). Ilya Volovnik from Vorex Intelligence Group sent a LinkedIn connection request — worth reviewing. PSC Spring Social is cancelled (Jun 4).</div>
    </div>
  </div>

  <!-- ============================== ACTION REQUIRED ============================== -->
  <div class="section-wrap">
    <div class="section-title sh-red">🔴 Action Required</div>

    <div style="padding: 16px 20px;">

      <div class="card card-red">
        <div class="label label-red">🔐 Security — Urgent</div>
        <div class="title">LinkedIn Password Reset + PIN Sent</div>
        <div class="meta">From: LinkedIn Security &lt;security-noreply@linkedin.com&gt; · Today</div>
        <div class="summary">Two back-to-back emails: (1) A PIN 606210 was sent to verify your identity, and (2) your LinkedIn password was successfully reset. If you did not initiate this, your account may be compromised.</div>
        <span class="next-step next-red">→ Log into LinkedIn NOW. If you didn't reset it, change your password immediately and enable 2FA.</span>
      </div>

      <div class="card card-red">
        <div class="label label-red">🚨 Phishing — Do Not Click</div>
        <div class="title">"Your Cloud Account Has Been Locked" — Scam Email</div>
        <div class="meta">From: "Payment_Declined" &lt;xbtcsupportmd@wcknlkzajfzzlhmducymgdwi.com&gt; · Today</div>
        <div class="summary">Fraudulent email claiming your cloud subscription expired and photos/videos will be deleted. Fake sender domain, urgency tactics, fake account ID. Classic phishing. Do not click any links.</div>
        <span class="next-step next-red">→ Mark as phishing/spam and delete immediately. Do not open any links.</span>
      </div>

      <div class="card card-yellow">
        <div class="label label-yellow">📬 RSVP Needed — Tomorrow</div>
        <div class="title">HR Networking &amp; Job Search: Open Office Hours</div>
        <div class="meta">Calendar Event · Thu, Jun 4 · 12:00–1:00 PM · Zoom · Status: No Response</div>
        <div class="summary">You haven't responded to this networking event yet. Large group session relevant to your active job search. Meeting note: AI notetaking tools should be turned off per organizer request.</div>
        <span class="next-step next-yellow">→ Accept or decline before tomorrow morning. Join link: us06web.zoom.us</span>
      </div>

      <div class="card card-yellow">
        <div class="label label-yellow">🤝 LinkedIn Connection — Review</div>
        <div class="title">Ilya Volovnik (Founder &amp; CEO, Vorex Intelligence Group) Wants to Connect</div>
        <div class="meta">From: LinkedIn Invitations · Today, 7:05 PM</div>
        <div class="summary">Pending LinkedIn connection request from a founder/CEO. Could be a relevant professional contact given your HR/job search focus.</div>
        <span class="next-step next-yellow">→ Review Ilya's profile on LinkedIn and accept or ignore.</span>
      </div>

      <div class="card card-yellow">
        <div class="label label-yellow">🗓 PSC Event Cancellation</div>
        <div class="title">People Strategy Collective Spring Social — CANCELLED</div>
        <div class="meta">From: People Strategy Collective &lt;membership@mg.peoplestrategycollective.org&gt; · Today</div>
        <div class="summary">Tomorrow's PSC Spring Social has been cancelled. Next PSC event is Tuesday, July (date TBD per email). Remove from your calendar if it was blocked.</div>
        <span class="next-step next-yellow">→ Remove from schedule. Watch for next PSC event in July.</span>
      </div>

      <div class="card card-yellow">
        <div class="label label-yellow">💬 Unread Slack Message</div>
        <div class="title">1 Unread Message in #all-hr Slack Channel</div>
        <div class="meta">From: HR via Slack &lt;notification@slack.com&gt; · Today (now in Trash)</div>
        <div class="summary">Slack notification about an unread message in the #all-hr channel. Note: this email is currently in trash — may have been auto-archived, but the Slack message itself may still need attention.</div>
        <span class="next-step next-yellow">→ Check Slack #all-hr channel for any pending messages.</span>
      </div>

    </div>
    <div class="section-end">📋 Summary: 2 urgent security items require immediate attention. 3 items need RSVP/response today.</div>
  </div>

  <!-- ============================== TODAY'S SCHEDULE ============================== -->
  <div class="section-wrap">
    <div class="section-title sh-blue">📅 Full Week Calendar (Jun 3–10, 2026)</div>
    <div style="padding: 16px 20px;">

    <table class="cal-table">
      <thead>
        <tr>
          <th>Day / Time</th>
          <th>Event</th>
          <th>Status</th>
          <th>Location / Link</th>
          <th>Notes &amp; Prep</th>
        </tr>
      </thead>
      <tbody>
        <!-- WED Jun 3 -->
        <tr class="day-header"><td colspan="5">Wednesday, June 3 — TODAY</td></tr>
        <tr><td>All Day</td><td>No calendar events scheduled</td><td class="status-confirmed">Clear</td><td>—</td><td>Focus on security items + email triage</td></tr>

        <!-- THU Jun 4 -->
        <tr class="day-header"><td colspan="5">Thursday, June 4</td></tr>
        <tr>
          <td>9:00 – 10:30 AM</td>
          <td>Executive Roundtable (John Madigan)</td>
          <td class="status-declined">Declined</td>
          <td><a href="https://us02web.zoom.us/j/207786667">Zoom Link</a></td>
          <td>You declined — no action needed. PW: 205454 if you change mind.</td>
        </tr>
        <tr>
          <td>10:30 – 11:30 AM</td>
          <td>Dr. Husk Appointment</td>
          <td class="status-confirmed">Confirmed ✅</td>
          <td>Location TBD</td>
          <td>Medical appointment — confirm address/location. Allow travel time. No overlap with prior (declined) event.</td>
        </tr>
        <tr>
          <td>12:00 – 1:00 PM</td>
          <td>HR Networking &amp; Job Search: Open Office Hours</td>
          <td class="status-pending">No Response ⚠️</td>
          <td><a href="https://us06web.zoom.us/j/85945371140">Zoom Link</a></td>
          <td><strong>RSVP needed.</strong> Large group (150+ attendees). No AI notetaking per organizer. Back-to-back with Dr. Husk — confirm you'll be done in time.</td>
        </tr>

        <!-- FRI Jun 5 -->
        <tr class="day-header"><td colspan="5">Friday, June 5</td></tr>
        <tr><td>All Day</td><td>No events scheduled</td><td>—</td><td>—</td><td>Open day</td></tr>

        <!-- SAT Jun 6 -->
        <tr class="day-header"><td colspan="5">Saturday, June 6</td></tr>
        <tr>
          <td>All Day</td>
          <td>🎂 Jackie's Birthday</td>
          <td class="status-allday">All-Day</td>
          <td>—</td>
          <td>Send birthday message / gift if planned. Event spans Jun 6–7.</td>
        </tr>

        <!-- SUN Jun 7 -->
        <tr class="day-header"><td colspan="5">Sunday, June 7</td></tr>
        <tr>
          <td>All Day</td>
          <td>🎂 Jackie's Birthday (cont.)</td>
          <td class="status-allday">All-Day</td>
          <td>—</td>
          <td>—</td>
        </tr>
        <tr>
          <td>All Day</td>
          <td>💳 State Farm Bill Due</td>
          <td class="status-allday">Reminder</td>
          <td>—</td>
          <td><strong>Pay or verify auto-pay is set up for State Farm.</strong></td>
        </tr>

        <!-- MON Jun 8 -->
        <tr class="day-header"><td colspan="5">Monday, June 8</td></tr>
        <tr>
          <td>9:00 – 10:00 AM</td>
          <td>👁 Eye Appointment</td>
          <td class="status-confirmed">Confirmed ✅</td>
          <td>Location TBD</td>
          <td>Confirm address. Allow travel time. Check if you need to bring insurance card or prior prescription.</td>
        </tr>

        <!-- TUE Jun 9 -->
        <tr class="day-header"><td colspan="5">Tuesday, June 9</td></tr>
        <tr>
          <td>12:00 – 12:15 PM</td>
          <td>🤝 Melissa x Netta Jenkins (15-min Zoom Consult)</td>
          <td class="status-confirmed">Accepted ✅</td>
          <td><a href="https://us06web.zoom.us/j/5224221004">Zoom Link</a> · PW: 424726</td>
          <td>Short 15-min consult. Prepare 1–2 key questions. Netta is at HIC Consult. Be on time — tight window.</td>
        </tr>

        <!-- WED Jun 10 -->
        <tr class="day-header"><td colspan="5">Wednesday, June 10</td></tr>
        <tr>
          <td>12:00 – 1:30 PM</td>
          <td>HR Networking &amp; Job Search Group — Zoom 2</td>
          <td class="status-pending">No Response ⚠️</td>
          <td><a href="https://us06web.zoom.us/j/81954171722">Zoom Link</a></td>
          <td>RSVP needed. Large group. Review team guidelines beforehand (link in event description).</td>
        </tr>
        <tr>
          <td>12:00 – 1:30 PM</td>
          <td>Network (personal block)</td>
          <td class="status-confirmed">Confirmed ✅</td>
          <td>—</td>
          <td>Overlaps with HR Networking Zoom above — same time window, likely intentional double-block.</td>
        </tr>
        <tr>
          <td>1:00 – 2:00 PM</td>
          <td>☕ Melissa x Meg Drinks</td>
          <td class="status-pending">No Response ⚠️ <span class="conflict-badge">⚠ CONFLICT</span></td>
          <td>TBC</td>
          <td><strong>Time conflict</strong> — overlaps with HR Networking (noon–1:30 PM). Location TBC. RSVP to Meg (megpark@oakleafpartnership.com) and sort timing. Confirm venue.</td>
        </tr>
      </tbody>
    </table>

    <div class="card card-red" style="margin-top:12px;">
      <div class="label label-red">⚠️ Calendar Conflict Alert — June 10</div>
      <div class="title">HR Networking (12–1:30 PM) conflicts with Melissa x Meg Drinks (1–2 PM)</div>
      <div class="summary">The networking call runs until 1:30 PM; drinks with Meg start at 1:00 PM. You will need to either leave the Zoom early or push drinks to 2:00 PM. Location for drinks is also TBC.</div>
      <span class="next-step next-red">→ Email Meg to adjust to 2:00 PM or confirm early departure from networking call.</span>
    </div>

    <div class="card card-yellow" style="margin-top:12px;">
      <div class="label label-yellow">💳 Upcoming Bill Reminder — June 7</div>
      <div class="title">State Farm Insurance Bill Due Sunday</div>
      <div class="summary">State Farm bill is due Sunday, June 7. Confirm auto-pay is active or pay manually before the weekend.</div>
      <span class="next-step next-yellow">→ Verify auto-pay or pay State Farm by Sunday, June 7.</span>
    </div>

    </div>
    <div class="section-end">📋 Summary: Confirm Dr. Husk location (tomorrow). RSVP to two networking sessions. Resolve Jun 10 scheduling conflict with Meg. Pay State Farm by Sunday. Prepare for Netta Jenkins consult on Jun 9.</div>
  </div>

  <!-- ============================== JOB SEARCH + PIPELINE ============================== -->
  <div class="section-wrap">
    <div class="section-title sh-green">💼 Job Search &amp; Professional Networking</div>
    <div style="padding: 16px 20px;">

      <div class="card card-green">
        <div class="label label-green">🎯 Job Alert — Strong Match</div>
        <div class="title">Senior Director, HR Business Partner (AI-Native) at RemoteHunter</div>
        <div class="meta">From: LinkedIn Job Alerts · Today, 9:05 PM</div>
        <div class="summary">LinkedIn surfaced a Senior Director HRBP role with an AI-native focus — closely aligned with your background in HR leadership and current interest in AI-integrated roles. Remote position via RemoteHunter.</div>
        <span class="next-step next-green">→ Open LinkedIn job alert and review/apply if it fits. Save the posting in case it closes.</span>
      </div>

      <div class="card card-green">
        <div class="label label-green">🤝 Networking Consult — Confirmed</div>
        <div class="title">Melissa x Netta Jenkins (HIC Consult) — 15-Min Zoom</div>
        <div class="meta">Calendar · Tuesday, June 9 · 12:00–12:15 PM · Zoom</div>
        <div class="summary">Short consult already accepted. Netta Jenkins is at HIC Consult. Prep 1–2 specific questions about your job search, positioning, or HR market before the call.</div>
        <span class="next-step next-green">→ Prepare agenda for Netta call by Monday, June 8.</span>
      </div>

      <div class="card card-green">
        <div class="label label-green">👥 Networking Group — RSVP Needed</div>
        <div class="title">HR Networking Open Office Hours (Jun 4) &amp; Group Session (Jun 10)</div>
        <div class="meta">Calendar Events · Both status: No Response</div>
        <div class="summary">Two recurring HR job-search networking sessions this week. Both are unconfirmed. These are active job-search support groups with 150+ HR professionals. Valuable for leads and community.</div>
        <span class="next-step next-green">→ RSVP Yes to both. Review team guidelines doc linked in Jun 10 invite.</span>
      </div>

      <div class="card card-green">
        <div class="label label-green">🔗 LinkedIn Connection — Incoming</div>
        <div class="title">Ilya Volovnik, Founder &amp; CEO · Vorex Intelligence Group</div>
        <div class="meta">From: LinkedIn Invitations · Today, 7:05 PM</div>
        <div class="summary">CEO-level connection request. Could be relevant for executive job search networking. Vorex Intelligence Group — review before accepting.</div>
        <span class="next-step next-green">→ Research Vorex Intelligence Group on LinkedIn and decide whether to accept.</span>
      </div>

      <div class="card card-yellow">
        <div class="label label-yellow">📅 Virtual Tech Event — June 17</div>
        <div class="title">Virtual Think IT Event — "Building High-Functioning Engineering Culture"</div>
        <div class="meta">From: Quinn Tice, York Solutions · Today (read, not in inbox)</div>
        <div class="summary">Reminder about a virtual event on Wednesday, June 17. HR-adjacent tech leadership topic. Relevance depends on your interest in tech-side org design. Currently not on your calendar.</div>
        <span class="next-step next-yellow">→ Review and add to calendar if relevant. No RSVP deadline mentioned.</span>
      </div>

      <div class="card card-yellow">
        <div class="label label-yellow">📅 Save the Date — EEO Training</div>
        <div class="title">Workplace EEO Investigator Training MD-110 (Virtual) — Nov 3–6, 2026</div>
        <div class="meta">From: Eventbrite / Amediate LLC · Today (in Trash)</div>
        <div class="summary">Professional development training for EEO investigators, November 2026. Currently in trash —
