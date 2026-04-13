# AI Development Guidelines

This repository is for the practical homelab only. Keep edits scoped to self-hosted services, infrastructure, Home Assistant configuration, and homelab documentation.

## Repository layout

```text
projects/homelab/
├─ app/
├─ infrastructure/
├─ home-assistant/
├─ docs/
└─ archive/
```

Rules:
- application stacks go under `app/`
- infrastructure services go under `infrastructure/`
- curated Home Assistant config lives in `home-assistant/`
- repo-specific documentation lives in `docs/`
- standalone product work belongs in sibling repos under `/home/docker/projects/`, not here

## Scope discipline

Do:
- keep service folders isolated with their own compose files and docs
- treat Home Assistant as a curated config repo, not a dump of runtime state
- keep homelab documentation aligned to the current infrastructure reality

Do not:
- recreate agent architecture or routing policy inside this repo
- park unrelated product projects under `app/` just because they are containerized

## Docker rules

Each service should have its own folder and compose file.

Example: `app/mealie/docker-compose.yml`

Do not combine unrelated services in the same compose stack.

## Home Assistant rules

Home Assistant runs in its own HA OS VM, not inside Docker.

Repository rules:
- `home-assistant/` contains managed config artifacts only
- keep source-controlled items such as `configuration.yaml`, dashboards, packages, themes, blueprints, selected `custom_components`, and intentional `www` assets under `home-assistant/`
- do not treat `.storage`, logs, databases, backups, caches, downloaded dependencies, or real `secrets.yaml` as source-controlled config
- production reads may inform repo work, but direct production writes still require explicit approval

## Dashboard direction

The kitchen dashboard is the main household UI.

Design priorities:
1. aesthetics
2. readability
3. simplicity

Avoid:
- crowded dashboards
- too many colors
- small UI elements

