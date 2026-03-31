export const missionData = {
  nav: [
    { key: 'overview', label: 'Overview' },
    { key: 'tasks', label: 'Tasks' },
    { key: 'calendar', label: 'Calendar' },
    { key: 'projects', label: 'Projects' },
    { key: 'memories', label: 'Memories' },
    { key: 'docs', label: 'Docs' },
    { key: 'team', label: 'Team' },
    { key: 'office', label: 'Office' },
  ],
  summary: {
    projectsInFlight: 9,
    pendingApproval: 4,
    agentsOnline: 6,
    urgentBlockers: 2,
  },
  tasks: {
    backlog: [
      {
        title: 'Home Assistant VM Access',
        description: 'Establish reliable access to the Home Assistant OS virtual machine so live dashboard work can begin.',
        owner: 'Ross + Planner',
        priority: 'High',
        tags: [
          { label: 'Infrastructure', tone: 'blue' },
          { label: 'Blocked', tone: 'yellow' },
        ],
      },
      {
        title: 'Lead Pipeline Backend',
        description: 'Add real submission capture, storage, and routing for PittsburghDivorce attorney leads.',
        owner: 'Software Engineer',
        priority: 'Medium',
        tags: [
          { label: 'Revenue', tone: 'green' },
          { label: 'Backend', tone: 'default' },
        ],
      },
    ],
    inProgress: [
      {
        title: 'Mission Control Next.js Build',
        description: 'Restructure the app into a sidebar-first workflow with task board, review lane, and live activity feed.',
        owner: 'Planner + UI',
        priority: 'High',
        tags: [
          { label: 'Ops UI', tone: 'blue' },
          { label: 'Active', tone: 'green' },
        ],
      },
      {
        title: 'Mealie Shared Collections',
        description: 'Canonical sharing model, scoped comments, and demo checkpoint work are underway.',
        owner: 'Software Engineer',
        priority: 'High',
        tags: [
          { label: 'Product', tone: 'purple' },
          { label: 'Backend', tone: 'blue' },
        ],
      },
      {
        title: 'PittsburghDivorce Site',
        description: 'Front-end concept is live while backend lead handling remains to be built.',
        owner: 'Software Engineer',
        priority: 'Medium',
        tags: [
          { label: 'Lead Gen', tone: 'green' },
          { label: 'Needs Backend', tone: 'yellow' },
        ],
      },
    ],
    review: [
      {
        title: 'Kitchen Dashboard Live Implementation',
        description: 'Hero Meal First design is approved visually; next move is whether to proceed once Home Assistant access is ready.',
        owner: 'UI Worker',
        priority: 'High',
        tags: [
          { label: 'Approval Needed', tone: 'red' },
          { label: 'UI', tone: 'blue' },
        ],
      },
      {
        title: 'Mealie Demo Scope',
        description: 'Need a decision on what the first demo-ready milestone should include before deeper buildout.',
        owner: 'Planner',
        priority: 'High',
        tags: [
          { label: 'Product Review', tone: 'purple' },
          { label: 'Approval Needed', tone: 'red' },
        ],
      },
      {
        title: 'PittsburghDivorce Backend Route',
        description: 'Need approval on whether initial leads should route to email, CRM, sheet, or custom admin queue.',
        owner: 'Software Engineer',
        priority: 'Medium',
        tags: [
          { label: 'Business Decision', tone: 'yellow' },
          { label: 'Approval Needed', tone: 'red' },
        ],
      },
      {
        title: 'Mission Control Data Source Plan',
        description: 'Decide whether to connect live cron/heartbeat/project stores next or keep iterating the UI first.',
        owner: 'Planner',
        priority: 'Medium',
        tags: [
          { label: 'Ops Decision', tone: 'blue' },
          { label: 'Approval Needed', tone: 'red' },
        ],
      },
    ],
    liveActivity: [
      {
        time: 'just now',
        title: 'Mission Control',
        detail: 'Next.js app reshaped toward sidebar-first task operations.',
      },
      {
        time: '14m ago',
        title: 'Kitchen Dashboard',
        detail: 'Hero Meal First concept approved and queued for implementation after HA access is ready.',
      },
      {
        time: '29m ago',
        title: 'Mealie',
        detail: 'Migration and route scaffolding pushed to feature branch for shared collections.',
      },
      {
        time: '46m ago',
        title: 'PittsburghDivorce',
        detail: 'Lead-gen front-end demo deployed locally for review.',
      },
    ],
  },
  cronJobs: [
    {
      name: 'archive-cleanup:home-assistant-legacy-delete',
      kind: 'one-time',
      displayDate: 'Sun Apr 12, 2026',
      displayTime: '17:37 UTC',
      status: 'scheduled',
      description: 'Two-week reminder to delete the archived Home Assistant legacy folder if it is no longer needed.',
    },
  ],
  projects: [
    {
      title: 'Kitchen Dashboard',
      status: 'Approved Design',
      detail: 'Ready for live Home Assistant implementation once VM access is established.',
    },
    {
      title: 'Mealie Fork',
      status: 'In Progress',
      detail: 'Specs, schema proposal, migrations, and shared-collection scaffolding exist.',
    },
    {
      title: 'PittsburghDivorce',
      status: 'Demo Ready',
      detail: 'Front-end concept is running locally; backend lead processing is not yet built.',
    },
  ],
  memories: [
    'Searchable long-term notes and journal history will live here.',
    'Daily files and curated memory views should surface decisions, milestones, and context.',
  ],
  docs: [
    'Specs, plans, reports, and generated documents should be searchable here.',
    'This can eventually index workspace specs and homelab project docs.',
  ],
  team: {
    mission: 'Coordinate multiple agents around real projects with clear approvals, visibility, and follow-through.',
    members: [
      'Planner / Supervisor',
      'UI / Frontend',
      'Software Engineer',
      'Researcher',
      'Backup Auditor',
      'Security / Repo Auditor',
    ],
  },
};
