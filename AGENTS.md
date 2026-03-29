# AI Development Guidelines

This repository is used for infrastructure-as-code for a personal homelab.

Agents editing this repo should follow these rules.

---

# Infrastructure Layout
homelab/
├─ app/
│ ├─ mealie/
│ ├─ immich/
│ ├─ paperless/
│ └─ plex/
│
├─ infrastructure/
│ ├─ cloudflared/
│ └─ portainer/
│
├─ home-assistant/
│ ├─ configuration.yaml
│ ├─ dashboards/
│ │ └─ kitchen.yaml
│ └─ themes/
│ └─ kitchen-dark.yaml
│
└─ docs/

Rules:

- application stacks go under **app**
- infrastructure services go under **infrastructure**
- Home Assistant configs live in **home-assistant**
- documentation lives in **docs**

---

# Docker Rules

Each service should have its own folder and compose file.

Example:app/mealie/docker-compose.yml


Do not combine unrelated services in the same compose stack.

---

# Cloudflare Tunnel

Cloudflare tunnel runs as its own container.

It routes public hostnames to internal services.

Example: recipes.rosscarhart.com -> mealie


---

# Home Assistant

Home Assistant runs in its **own HA OS VM**, not inside Docker.

The live production configuration is available over Samba at:

`\\192.168.86.21\config`

Repository rules:

- `home-assistant/` contains **managed config artifacts only**, not a full dump of runtime-generated Home Assistant files
- keep source-controlled items such as `configuration.yaml`, dashboards, packages, themes, blueprints, selected `custom_components`, and intentional `www` assets under `home-assistant/`
- do not treat `.storage`, logs, databases, backups, caches, downloaded dependencies, or `secrets.yaml` as source-controlled config
- `home-assistant-legacy/` refers to the directory on the actual server from the old installation path and is **not live**
- agents may read production config from the Samba share for reference, but should only write to repo dev/staged files unless the user explicitly approves writing to production config


---

# Kitchen Dashboard Design

The kitchen dashboard is the main household UI.

Hardware:

- 15-inch landscape wall display

Design requirements:

- dark mode
- minimal UI
- Apple-style aesthetic
- large cards
- single screen layout
- tap expansions

---

# Dashboard Layout
Top Row
Time | Weather | Today | House

Middle
Dinner Tonight | Grocery List

Lower
Chores | Home

Footer
Doorbell Camera


---

# Design Philosophy

Prioritize:

1. aesthetics
2. readability
3. simplicity

Avoid:

- crowded dashboards
- too many colors
- small UI elements

