# Agents

This directory is the source-controlled home for the homelab's agent system design.

See also:
- `MISSION_CONTROL.md` for coordination rules and Discord structure
- `ROSTER.md` for worker names and role mapping

It documents:

- worker roles
- provider/model routing
- access boundaries
- prompt and role design intent
- shared safety rules
- project-specific operating workflows

This is the human-readable control plane for how assistants should behave in this repo.

## Recommended operating model

Start with one main agent that you talk to directly.
That main agent should coordinate a small set of specialized workers rather than trying to make every worker autonomous.

Recommended pattern:

- one main agent for conversation, delegation, and approval collection
- a planner/supervisor worker for sequencing and architecture
- a UI worker for Home Assistant dashboard and UX work
- a Mealie dev worker for source-code changes in a separate dev checkout
- a backup auditor for read-only recovery review
- a security/repo auditor for git hygiene and risky-pattern detection

## Safety model

Use proposal-first and read-mostly defaults.

Prefer:

- repo edits before production edits
- separate dev environments before production rollout
- explicit approval before impactful writes
- scoped workers instead of broad write access

Avoid early:

- direct production writes
- broad shell access everywhere
- hidden hooks and unattended automation
- direct Home Assistant Samba writes by default
- automatic backup deletion or retention mutation

## Structure

```text
agents/
├─ README.md
├─ providers.md
├─ dashboard-access.md
├─ openclaw/
│  ├─ architecture.md
│  ├─ rollout-plan.md
│  └─ discord-approvals.md
├─ workers/
│  ├─ planner.md
│  ├─ ui-worker.md
│  ├─ mealie-dev.md
│  ├─ backup-auditor.md
│  └─ security-auditor.md
└─ skills/
   └─ shared/
      ├─ repo-conventions/
      │  └─ SKILL.md
      └─ prod-safety/
         └─ SKILL.md
```

## Source of truth

Use `agents/` for things like:

- what each worker is responsible for
- which provider/model should be used for which class of work
- what systems agents may access
- role boundaries and handoff rules
- shared safety and repo conventions

Do not use this directory for runtime state, tokens, logs, or generated artifacts.
Those belong in the running OpenClaw environment, not in git.
