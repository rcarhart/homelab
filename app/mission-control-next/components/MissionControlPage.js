'use client';

import { useMemo, useState } from 'react';
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
  ['projectsInFlight', 'Projects in flight'],
  ['pendingApproval', 'Pending approval'],
  ['agentsOnline', 'Agents online'],
  ['urgentBlockers', 'Urgent blockers'],
];

export default function MissionControlPage() {
  const [activeView, setActiveView] = useState('tasks');
  const reviewCount = missionData.tasks.review.length;

  const content = useMemo(() => {
    if (activeView === 'tasks') {
      return <TasksView />;
    }
    if (activeView === 'calendar') {
      return <CalendarView />;
    }
    if (activeView === 'projects') {
      return <ProjectsView />;
    }
    if (activeView === 'memories') {
      return <MemoriesView />;
    }
    if (activeView === 'docs') {
      return <DocsView />;
    }
    if (activeView === 'team') {
      return <TeamView />;
    }
    if (activeView === 'office') {
      return <OfficeView />;
    }
    return <OverviewView />;
  }, [activeView]);

  return (
    <div className="app-shell">
      <aside className="sidebar-nav">
        <div className="brand-block">
          <div className="brand-mark">MC</div>
          <div>
            <div className="brand-title">Mission Control</div>
            <div className="brand-subtitle">Linear-style ops layer</div>
          </div>
        </div>

        <nav className="nav-list">
          {missionData.nav.map((item) => {
            const isActive = activeView === item.key;
            const badge = item.key === 'tasks' ? reviewCount : null;
            return (
              <button
                key={item.key}
                className={`nav-item ${isActive ? 'active' : ''}`}
                onClick={() => setActiveView(item.key)}
              >
                <span>{item.label}</span>
                {badge ? <span className="nav-badge">{badge}</span> : null}
              </button>
            );
          })}
        </nav>

        <div className="sidebar-footer">
          <div className="footer-card">
            <strong>Heartbeat contract</strong>
            <div className="small">
              Every heartbeat should check the tasks board, especially backlog, in progress, review, and live activity.
            </div>
          </div>
        </div>
      </aside>

      <main className="content-shell">
        <div className="content-topbar">
          <div>
            <h1>{activeView === 'tasks' ? 'Tasks' : activeView.charAt(0).toUpperCase() + activeView.slice(1)}</h1>
            <p>
              {activeView === 'tasks'
                ? 'Backlog, In Progress, Review, and Live Activity define the operational loop.'
                : 'Mission Control sections can evolve into live connected modules over time.'}
            </p>
          </div>
          <div className="topbar-actions">
            <span className="chip">Next.js</span>
            <span className="chip">Local host</span>
            <button className="btn-primary">New Item</button>
          </div>
        </div>

        <div className="summary-row">
          {summaryOrder.map(([key, label]) => (
            <div className="summary-card" key={key}>
              <div className="summary-label">{label}</div>
              <div className="summary-value">{missionData.summary[key]}</div>
            </div>
          ))}
        </div>

        {content}
      </main>
    </div>
  );
}

function TasksView() {
  const columns = [
    ['backlog', 'Backlog'],
    ['inProgress', 'In Progress'],
    ['review', 'Review'],
  ];

  return (
    <div className="tasks-layout">
      <section className="board-panel">
        <div className="section-head">
          <h2>Task Board</h2>
          <span className="chip">Review lane = Ross approval</span>
        </div>
        <div className="kanban-grid three">
          {columns.map(([key, label]) => {
            const items = missionData.tasks[key] || [];
            return (
              <div className="board-column" key={key}>
                <div className="column-head">
                  <div className="column-title">{label}</div>
                  <div className="count-pill">{items.length}</div>
                </div>
                {items.map((item) => (
                  <div className="task-card" key={item.title}>
                    <h3>{item.title}</h3>
                    <p>{item.description}</p>
                    <div className="tags">
                      {item.tags.map((tag) => (
                        <span className={`tag ${toneClass[tag.tone] || ''}`} key={tag.label}>
                          {tag.label}
                        </span>
                      ))}
                    </div>
                    <div className="meta-row">
                      <span>{item.owner}</span>
                      <span>{item.priority}</span>
                    </div>
                  </div>
                ))}
              </div>
            );
          })}
        </div>
      </section>

      <aside className="activity-panel">
        <div className="section-head">
          <h2>Live Activity</h2>
          <span className="chip">Heartbeat feed</span>
        </div>
        <div className="activity-list">
          {missionData.tasks.liveActivity.map((item) => (
            <div className="activity-item" key={`${item.time}-${item.title}`}>
              <div className="activity-time">{item.time}</div>
              <strong>{item.title}</strong>
              <div className="small">{item.detail}</div>
            </div>
          ))}
        </div>
      </aside>
    </div>
  );
}

function CalendarView() {
  return (
    <section className="single-panel">
      <div className="section-head">
        <h2>Cron Calendar</h2>
        <span className="chip">Scheduled tasks and proactive work</span>
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
    </section>
  );
}

function ProjectsView() {
  return (
    <section className="single-panel">
      <div className="section-head">
        <h2>Projects</h2>
        <span className="chip">High-level focus layer</span>
      </div>
      <div className="project-list">
        {missionData.projects.map((project) => (
          <div className="project-card" key={project.title}>
            <h3>{project.title}</h3>
            <div className="status-inline">{project.status}</div>
            <p>{project.detail}</p>
          </div>
        ))}
      </div>
    </section>
  );
}

function MemoriesView() {
  return (
    <section className="single-panel">
      <div className="section-head">
        <h2>Memories</h2>
        <span className="chip">Searchable journal layer</span>
      </div>
      <div className="note-list">
        {missionData.memories.map((item) => (
          <div className="note-card" key={item}>{item}</div>
        ))}
      </div>
    </section>
  );
}

function DocsView() {
  return (
    <section className="single-panel">
      <div className="section-head">
        <h2>Docs</h2>
        <span className="chip">Searchable documents</span>
      </div>
      <div className="note-list">
        {missionData.docs.map((item) => (
          <div className="note-card" key={item}>{item}</div>
        ))}
      </div>
    </section>
  );
}

function TeamView() {
  return (
    <section className="single-panel">
      <div className="section-head">
        <h2>Team</h2>
        <span className="chip">Roles + mission alignment</span>
      </div>
      <div className="team-mission">{missionData.team.mission}</div>
      <div className="team-grid">
        {missionData.agents.map((agent) => (
          <div className="team-card" key={agent.name}>
            <strong><span className={`status-dot ${dotClass[agent.tone] || 'dot-blue'}`} />{agent.name}</strong>
            <div className="small">{agent.status}</div>
            <p>{agent.detail}</p>
          </div>
        ))}
      </div>
    </section>
  );
}

function OfficeView() {
  return (
    <section className="single-panel">
      <div className="section-head">
        <h2>Office</h2>
        <span className="chip">Pixel-art activity view later</span>
      </div>
      <div className="office-placeholder">
        <div className="office-box">Office view will become the playful, visual representation of agent activity after the real task + heartbeat data model is stable.</div>
      </div>
    </section>
  );
}

function OverviewView() {
  return (
    <section className="single-panel">
      <div className="section-head">
        <h2>Overview</h2>
        <span className="chip">Top-level summary</span>
      </div>
      <div className="project-list">
        <div className="project-card">
          <h3>Focus right now</h3>
          <p>Tasks is the main operational center. Heartbeats should always check backlog, in progress, review, and live activity.</p>
        </div>
      </div>
    </section>
  );
}
