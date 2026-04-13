# Homelab

This repository is the source-controlled home for the actual homelab: self-hosted services, supporting infrastructure, curated Home Assistant configuration, and homelab-specific documentation.

This repo now lives at `/home/docker/projects/homelab`. It is intentionally narrower than your broader workspace: standalone product repos also live under `/home/docker/projects/`, while the live OpenClaw operating model lives under `/home/docker/.openclaw/`.

## What this repo currently holds

### App services
The `app/` directory currently contains the main homelab service areas:
- `mealie/`
- `feedme/`
- `mealie-dev/`
- `grocy/`
- `immich/`
- `paperless/`
- `plex/`
- `ha-kitchen-demo/`

### Infrastructure
The `infrastructure/` directory is for supporting platform services such as tunnels, proxies, and other operational plumbing.

### Home Assistant
The `home-assistant/` directory is for curated, intentional Home Assistant configuration, not a full runtime dump from the HA OS VM.

### Docs and archive material
- `docs/` contains homelab-specific documentation.
- `archive/` is for small migration notes and historical pointers, not raw runtime payloads.

This repo tracks deployment intent and managed config. Live mutable state still lives on the running systems.

## Repository boundaries

Use this repo for:
- Dockerized homelab services under `app/`
- supporting infrastructure under `infrastructure/`
- curated Home Assistant config under `home-assistant/`
- homelab documentation under `docs/`

Do not use this repo for:
- standalone product projects unrelated to operating the homelab
- OpenClaw identity, routing, or coordination policy
- generated runtime state, secrets, databases, caches, or logs

## Source-of-truth rules

### Docker services and infrastructure
- Git stores deployment intent, human-managed config, docs, and helper scripts.
- Running systems store secrets, databases, media, caches, and other mutable state.
- Backups cover the state intentionally excluded from git.

### Home Assistant
- Git stores curated config artifacts such as dashboards, packages, themes, blueprints, and selected assets.
- The HA OS VM owns runtime internals and generated state.
- Recovery depends on both git-managed config and HA backups.

### Agent/runtime model
- The live OpenClaw operating model is outside this repo under `/home/docker/.openclaw/`.
- This repo should not carry its own parallel agent control-plane layer.

## Repo layout

```text
projects/homelab/
├─ README.md
├─ AGENTS.md
├─ app/
├─ archive/
├─ docs/
├─ home-assistant/
└─ infrastructure/
```

## Working rules

- Keep unrelated services in separate folders and compose stacks.
- Treat `home-assistant/` as curated config, not a backup dump.
- Keep non-homelab product work in sibling repos under `/home/docker/projects/`.
- Prefer deleting stale architecture layers instead of letting duplicate sources of truth accumulate.

## Kitchen dashboard

The kitchen dashboard is still a homelab deliverable and belongs here when the work is tied to Home Assistant and the wall display setup.

Current design direction:
- dark mode
- minimal layout
- single-screen readability
- large touch targets
- readable at distance
