export const missionData = {
  nav: [
    { key: 'tasks', label: 'Tasks' },
    { key: 'agents', label: 'Agents' },
    { key: 'approvals', label: 'Approvals' },
    { key: 'calendar', label: 'Calendar' },
    { key: 'projects', label: 'Projects' },
    { key: 'memory', label: 'Memory' },
    { key: 'docs', label: 'Docs' },
    { key: 'office', label: 'Office' },
    { key: 'team', label: 'Team' },
  ],
  summary: {
    thisWeek: 12,
    inProgress: 3,
    total: 9,
    completion: '68%'
  },
  tasks: {
    backlog: [
      {
        title: 'Home Assistant VM Access Hardening',
        description: 'Stabilize access path and validate safe workflow for live dashboard implementation work.',
        owner: 'Zeus',
        tags: [
          { label: 'Infrastructure', tone: 'blue' },
          { label: 'Blocked', tone: 'yellow' }
        ]
      },
      {
        title: 'Plex Local-First Deployment Plan',
        description: 'Define media mount strategy, local-only rollout, and data path expectations before install.',
        owner: 'Steve',
        tags: [
          { label: 'Media', tone: 'purple' },
          { label: 'Planning', tone: 'default' }
        ]
      }
    ],
    inProgress: [
      {
        title: 'Mission Control UI Rebuild',
        description: 'Rebuild the app around the dark premium layout, left nav, KPI strip, kanban board, and live activity rail.',
        owner: 'Kelly',
        tags: [
          { label: 'UI', tone: 'blue' },
          { label: 'Active', tone: 'green' }
        ]
      },
      {
        title: 'Mealie Shared Collections',
        description: 'Continue the fork with canonical sharing, scoped comments, and a cleaner demo checkpoint.',
        owner: 'Steve',
        tags: [
          { label: 'Product', tone: 'purple' },
          { label: 'Backend', tone: 'blue' }
        ]
      },
      {
        title: 'Backup Auditor Automation',
        description: 'Turn Charlie’s first host audit into a recurring job with deterministic checks and lightweight summary output.',
        owner: 'Charlie',
        tags: [
          { label: 'Backups', tone: 'green' },
          { label: 'Host Ops', tone: 'yellow' }
        ]
      }
    ],
    review: [
      {
        title: 'Kitchen Dashboard Live Rollout',
        description: 'Hero Meal First design is approved visually; waiting for Ross to approve the next implementation phase into the live HA dashboard.',
        owner: 'Kelly',
        tags: [
          { label: 'Approval Needed', tone: 'red' },
          { label: 'Kitchen', tone: 'blue' }
        ]
      },
      {
        title: 'PittsburghDivorce Backend Direction',
        description: 'Need a decision on where leads should go first: email, CRM, sheet, or internal admin queue.',
        owner: 'Steve',
        tags: [
          { label: 'Approval Needed', tone: 'red' },
          { label: 'Revenue', tone: 'green' }
        ]
      },
      {
        title: 'Mission Control Product Scope',
        description: 'Need approval on whether to focus first on Tasks, Agents, Approvals, and Calendar as the MVP.',
        owner: 'Zeus',
        tags: [
          { label: 'Approval Needed', tone: 'red' },
          { label: 'Product', tone: 'purple' }
        ]
      }
    ],
    done: [
      {
        title: 'Kitchen Dashboard Direction Approved',
        description: 'Hero Meal First chosen as the live kitchen dashboard direction.',
        owner: 'Kelly',
        tags: [
          { label: 'Approved', tone: 'green' },
          { label: 'UI', tone: 'blue' }
        ]
      }
    ],
    activity: [
      {
        time: '2m ago',
        title: 'Kelly updated Mission Control layout',
        detail: 'Reworked Tasks to match the screenshot-inspired layout with review lane and right-side live activity.'
      },
      {
        time: '11m ago',
        title: 'Charlie inspected Proxmox backup disk',
        detail: 'Confirmed 1.8T backup drive mounted at /mnt/usb-backups with healthy free space.'
      },
      {
        time: '24m ago',
        title: 'Kelly gained read access to Home Assistant config',
        detail: 'Mounted the HA config share read-only and located kitchen dashboard, theme, and Mealie integration files.'
      },
      {
        time: '38m ago',
        title: 'Steve pushed Mealie scaffolding',
        detail: 'Shared collections route, schema, and migration scaffolding were pushed to the feature branch.'
      },
      {
        time: '57m ago',
        title: 'Zeus routed active projects',
        detail: 'Rebalanced current project ownership across Kelly, Steve, Charlie, Zhou, and Kevin.'
      }
    ]
  },
  agents: [
    {
      name: 'Zeus',
      role: 'Planner / Supervisor',
      status: 'Active',
      tone: 'blue',
      heartbeat: '1 minute ago',
      detail: 'Orchestrating active projects, choosing next steps, and managing review flow.'
    },
    {
      name: 'Kelly',
      role: 'UI / Frontend',
      status: 'Busy',
      tone: 'green',
      heartbeat: 'just now',
      detail: 'Owns Mission Control design and Home Assistant dashboard design work.'
    },
    {
      name: 'Steve',
      role: 'Software Engineer',
      status: 'Busy',
      tone: 'yellow',
      heartbeat: '5 minutes ago',
      detail: 'Owns Mealie implementation, app builds, and infrastructure app setup.'
    },
    {
      name: 'Charlie',
      role: 'Backup Auditor',
      status: 'Active',
      tone: 'green',
      heartbeat: '8 minutes ago',
      detail: 'Owns backup health checks, restore-readiness, and host storage auditing.'
    },
    {
      name: 'Zhou',
      role: 'Researcher',
      status: 'Idle-ready',
      tone: 'blue',
      heartbeat: '27 minutes ago',
      detail: 'Owns external research, comparisons, and implementation references.'
    },
    {
      name: 'Kevin',
      role: 'Security / Repo Auditor',
      status: 'Partial',
      tone: 'red',
      heartbeat: '42 minutes ago',
      detail: 'Owns repo hygiene, secret handling review, and security checks.'
    }
  ],
  approvals: [
    'Kitchen dashboard implementation phase',
    'Mission Control MVP scope',
    'PittsburghDivorce backend route',
    'Mealie demo milestone definition'
  ],
  calendar: [
    {
      date: 'Apr 12',
      time: '17:37 UTC',
      title: 'archive-cleanup:home-assistant-legacy-delete',
      kind: 'one-time'
    }
  ],
  projects: [
    {
      title: 'Mission Control',
      status: 'In Progress',
      owner: 'Kelly',
      detail: 'Core operations app where project, agent, approval, and activity views come together.'
    },
    {
      title: 'Kitchen Dashboard',
      status: 'Approved Design',
      owner: 'Kelly',
      detail: 'Hero Meal First approved; implementation plan now grounded in real Home Assistant config.'
    },
    {
      title: 'Mealie Fork',
      status: 'In Progress',
      owner: 'Steve',
      detail: 'Selective recipe sharing and canonical model implementation are underway.'
    }
  ],
  memory: {
    daily: [
      '2026-03-29 — Mealie spec and worker system planning expanded heavily.',
      '2026-03-30 — Kitchen dashboard approved and host/HA access improved.'
    ],
    longTerm: [
      'Ross prefers specialized named agents with visible ownership in Mission Control.',
      'Kitchen dashboard should follow the Hero Meal First pattern with Skylight-inspired styling.'
    ]
  },
  docs: [
    'Worker System Plan',
    'Mealie Product Spec',
    'Mealie Milestone 1 Implementation Plan',
    'Mealie Codebase Gap Analysis',
    'Mealie Schema Proposal v1',
    'Mealie Backend Touchpoints',
    'Kitchen dashboard demo files',
    'PittsburghDivorce demo files'
  ],
  team: {
    mission: 'Build, monitor, and improve Ross’s systems through specialized agents with clear ownership and approvals.',
    structure: [
      { parent: 'Zeus', child: 'Kelly' },
      { parent: 'Zeus', child: 'Steve' },
      { parent: 'Zeus', child: 'Charlie' },
      { parent: 'Zeus', child: 'Zhou' },
      { parent: 'Zeus', child: 'Kevin' }
    ]
  }
};
