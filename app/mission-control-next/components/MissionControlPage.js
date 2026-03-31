import { missionData } from '../lib/data';

const toneClass = {
  blue: 'blue',
  green: 'green',
  yellow: 'yellow',
  purple: 'purple',
  red: 'red',
  default: '',
};

const dotClass = {
  blue: 'dot-blue',
  green: 'dot-green',
  yellow: 'dot-yellow',
  red: 'dot-red',
};

const summaryOrder = [
  ['projectsInFlight', 'Projects in flight', 'Across software, dashboards, audits, and infrastructure work.'],
  ['pendingApproval', 'Pending approval', 'Items currently waiting on Ross before work can continue.'],
  ['agentsOnline', 'Agents online', 'Planner, UI, engineering, backup, security, and researcher workers.'],
  ['urgentBlockers', 'Urgent blockers', 'Dependencies currently slowing execution.'],
];

const columns = [
  ['backlog', 'Backlog'],
  ['inProgress', 'In Progress'],
  ['waitingApproval', 'Waiting on Approval'],
  ['done', 'Done / Demo Ready'],
];

export default function MissionControlPage() {
  return (
    <div className="shell">
      <div className="topbar">
        <div className="title">
          <h1>Mission Control</h1>
          <p>
            A locally hosted Next.js operations dashboard for project status, pending approvals, scheduled cron work,
            and future multi-agent heartbeat.
          </p>
        </div>
        <div className="actions">
          <span className="chip">Next.js build</span>
          <span className="chip">Local host</span>
          <button className="btn">Create New Project</button>
        </div>
      </div>

      <div className="overview">
        {summaryOrder.map(([key, label, sub]) => (
          <div className="panel metric" key={key}>
            <div className="eyebrow">{label}</div>
            <div className="value">{missionData.summary[key]}</div>
            <div className="sub">{sub}</div>
          </div>
        ))}
      </div>

      <div className="main-grid">
        <div className="panel">
          <div className="section-head">
            <h2>Project Board</h2>
            <span className="chip">Kanban + project visibility</span>
          </div>
          <div className="kanban">
            {columns.map(([key, label]) => {
              const items = missionData.projects[key] || [];
              return (
                <div className="column" key={key}>
                  <div className="col-head">
                    <div className="col-title">{label}</div>
                    <div className="count">{items.length}</div>
                  </div>
                  {items.map((item) => (
                    <div className="card" key={item.title}>
                      <h3 className="project-title">{item.title}</h3>
                      <p className="project-desc">{item.description}</p>
                      <div className="tags">
                        {item.tags.map((tag) => (
                          <span className={`tag ${toneClass[tag.tone] || ''}`} key={tag.label}>
                            {tag.label}
                          </span>
                        ))}
                      </div>
                      <div className="meta-row">
                        <span>Owner: {item.owner}</span>
                        <span>Priority: {item.priority}</span>
                      </div>
                    </div>
                  ))}
                </div>
              );
            })}
          </div>
        </div>

        <div className="sidebar">
          <div className="panel">
            <div className="section-head">
              <h2>Pending Approval</h2>
              <span className="chip">Ross queue</span>
            </div>
            <div className="approval-list">
              {missionData.approvals.map((item) => (
                <div className="approval-item" key={item.title}>
                  <strong>{item.title}</strong>
                  <div className="small">{item.description}</div>
                </div>
              ))}
            </div>
          </div>

          <div className="panel">
            <div className="section-head">
              <h2>Agent Heartbeat</h2>
              <span className="chip">Future multi-agent ops</span>
            </div>
            <div className="agent-list">
              {missionData.agents.map((agent) => (
                <div className="agent-item" key={agent.name}>
                  <div className="agent-top">
                    <strong>
                      <span className={`status-dot ${dotClass[agent.tone] || 'dot-blue'}`} />
                      {agent.name}
                    </strong>
                    <span className="small">{agent.status}</span>
                  </div>
                  <div className="small">{agent.detail}</div>
                  <div className="pulse"><span style={{ width: `${agent.pulse}%` }} /></div>
                </div>
              ))}
            </div>
          </div>

          <div className="panel">
            <div className="section-head">
              <h2>Cron Calendar</h2>
              <span className="chip">Scheduled jobs</span>
            </div>
            <div className="calendar-list">
              {missionData.cronJobs.map((job) => (
                <div className="calendar-item" key={job.name}>
                  <strong>{job.name}</strong>
                  <div className="small">{job.description}</div>
                  <div className="calendar-meta">
                    <span>{job.displayDate}</span>
                    <span>{job.displayTime}</span>
                    <span>{job.kind}</span>
                  </div>
                  <div className="status-pill">{job.status}</div>
                </div>
              ))}
            </div>
          </div>

          <div className="panel">
            <div className="section-head">
              <h2>Recent Heartbeats</h2>
              <span className="chip">Activity snapshot</span>
            </div>
            <div className="heartbeat-list">
              {missionData.heartbeats.map((item) => (
                <div className="heartbeat-item" key={item.title}>
                  <strong>{item.title}</strong>
                  <div className="small">{item.description}</div>
                </div>
              ))}
            </div>
            <div className="footer-note">
              This is the Next.js foundation. Next step is wiring live project state, live cron data, and actual agent telemetry.
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
