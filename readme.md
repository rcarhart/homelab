# Homelab Project

This repository contains the practical homelab app and service directories Ross is actively using for self-hosted software, experiments, and product work.

It is no longer the control plane for agent architecture.
The OpenClaw agent system now lives under the active OpenClaw workspace and runtime, not in a parallel planning layer inside this repo.

## What this repo is for

Use this repository for:
- app and service directories under `app/`
- deployment files such as `docker-compose.yml`, `Dockerfile`, and helper scripts
- project-specific runtime-adjacent docs that belong with the homelab apps
- practical implementation work tied to self-hosted services

Do not use this repo as the primary source of truth for:
- agent identity design
- worker rosters
- old roleplay-style agent naming systems
- OpenClaw routing or coordination policy

Those now belong in the active OpenClaw workspace and runtime.

## Current structure

```text
homelab/
├─ app/
│  ├─ mealie/
│  ├─ mealie-dev/
│  ├─ mission-control/
│  ├─ mission-control-next/
│  ├─ grocy/
│  ├─ immich/
│  ├─ paperless/
│  ├─ plex/
│  └─ ...
├─ docs/
├─ archive/
└─ README.md
```

## Key areas

### `app/`
Primary service and project directories.
This is the main reason the repo still exists.

Examples:
- `app/mealie/` — deployed Mealie instance, backups, scripts, and related runtime files
- `app/mealie-dev/` — source checkout / dev environment for Mealie feature work
- `app/mission-control-next/` — current Next.js Mission Control implementation path
- `app/mission-control/` — older Mission Control prototype that should be reviewed for retirement or archival

### `docs/`
Supporting repository/project docs that still belong to the homelab itself.

### `archive/`
Legacy material intentionally preserved for review before deletion.
Not active source-of-truth by default.

## Current project reality

The active coordination model is now:
- **Sir Alex** — main front-door assistant
- **Bruno** — supervisor / internal orchestrator
- specialist agents used behind the scenes when needed

Mission Control is now treated as an active project and should evolve into the main dashboard Ross uses to understand project status, ownership, blockers, next steps, and repo hygiene.

## Repo hygiene rules

- keep files that clearly support active projects
- remove stale planning layers when they duplicate newer OpenClaw sources of truth
- avoid keeping historical architecture docs in multiple places
- generated build output and installed dependencies should not be treated as intentional long-term project structure

## Notes

This repo has evolved over time. Some historical layers made sense when access and tooling were more limited, but they now create duplication and confusion.

The goal going forward is simple:
- one clear source of truth for agent architecture
- one clear source of truth for active project work
- fewer stale layers pretending to still be important
