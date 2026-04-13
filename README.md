# Homelab Project

This repository contains the configuration, infrastructure, automation, and curated smart home configuration for a personal homelab.

Primary goals:

- host household services locally
- build a kitchen wall dashboard
- integrate smart home systems
- replace some cloud services with self-hosted alternatives
- create a clear source-of-truth model for apps, Home Assistant, agents, and recovery

---

# Core Architecture

The homelab runs on a **Lenovo ThinkCentre M720q** server using **Proxmox**.

```text
Proxmox
├─ VM: Ubuntu + Docker
│  ├─ FeedMe (Mealie fork)
│  ├─ Mealie
│  ├─ Immich
│  ├─ Paperless
│  ├─ Plex
│  ├─ Grocy
│  └─ supporting Docker services
├─ VM: Home Assistant OS
└─ LXC: Pi-hole
```

## Repository Layout

```text
homelab/
├─ README.md
├─ agents/
├─ openclaw/
├─ app/
├─ infrastructure/
├─ home-assistant/
└─ docs/
```

## Source-of-truth model

### Docker apps
For Dockerized services under `app/` and `infrastructure/`:

- Git stores deployment intent and human-managed configuration
- the target machine stores real secrets and runtime data
- backups protect persistent application state that git intentionally excludes

### Home Assistant
For `home-assistant/`:

- Git stores curated, human-managed Home Assistant configuration
- the live Home Assistant OS VM owns runtime state and generated internals
- Home Assistant backups provide full-fidelity recovery for the parts not kept in git

### Agents and OpenClaw
For `agents/` and `openclaw/`:

- `agents/` documents worker roles, provider choices, and access boundaries
- `openclaw/` stores deployment intent, examples, scripts, and operations docs
- live credentials, tokens, runtime state, and generated session data remain outside git

---

# Primary Areas

## app/
User-facing self-hosted services such as Mealie, Grocy, Immich, Paperless, and Plex.

## infrastructure/
Supporting infrastructure such as tunnels, proxies, and control-plane plumbing.

## home-assistant/
Curated Home Assistant configuration for the live HA OS VM.

## agents/
Human-readable documentation for assistant workers, roles, and access policies.

## openclaw/
Deployment and operational home for the OpenClaw runtime.

---

# Dashboard

A wall-mounted **15-inch landscape display** will run a Home Assistant dashboard.

Design goals:

- dark mode
- minimal aesthetic
- Apple-style UI
- single screen
- tap expansions
- readable from across the room
