# Homelab Project

This repository contains the practical homelab app and service directories Ross is actively using for self-hosted software, experiments, and product work.

It is no longer the control plane for agent architecture.
The OpenClaw agent system now lives under the active OpenClaw workspace and runtime, not in a parallel planning layer inside this repo.

Mission Control also no longer lives here.
Mission Control is now a standalone project because it manages the broader Ross + Sir Alex operating relationship, not just homelab services.

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
- Mission Control planning or implementation

Those now belong in the active OpenClaw workspace/runtime or the standalone Mission Control project.

## Current structure

```text
homelab/
├─ app/
│  ├─ mealie/
│  ├─ mealie-dev/
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
- `app/grocy/`, `app/immich/`, `app/paperless/`, `app/plex/` — service-specific folders

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

Mission Control is a separate project outside this repo.
Homelab-related work may appear inside Mission Control, but Mission Control itself is not a homelab app.

## Repo hygiene rules

- keep files that clearly support active homelab projects
- remove stale planning layers when they duplicate newer OpenClaw sources of truth
- avoid keeping historical architecture docs in multiple places
- generated build output and installed dependencies should not be treated as intentional long-term project structure

## Notes

This repo has evolved over time. Some historical layers made sense when access and tooling were more limited, but they now create duplication and confusion.

The goal going forward is simple:
- one clear source of truth for agent architecture
- one clear source of truth for active homelab work
- Mission Control kept separate as its own project
- fewer stale layers pretending to still be important
