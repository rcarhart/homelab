# Repository Structure

This repo is organized so each homelab system has a clear boundary without mixing deployment definitions, secrets, runtime state, and unrelated product work.

## Folder layout

```text
projects/homelab/
├─ README.md
├─ AGENTS.md
├─ app/
├─ infrastructure/
├─ home-assistant/
├─ archive/
└─ docs/
```

## Source of truth by area

### `app/` and `infrastructure/`
Use these for Dockerized homelab services and supporting infrastructure components.

Git should contain:
- `docker-compose.yml`
- `.env.example`
- `README.md`
- maintenance scripts
- human-managed config files

Git should not contain:
- real `.env` files
- databases
- uploaded media
- service backups
- logs and caches

Rule: if something is a standalone product rather than a homelab-operated service, it belongs in a sibling repo under `/home/docker/projects/`, not `projects/homelab/app/`.

### `home-assistant/`
Use this for curated, source-controlled Home Assistant configuration only.

Git should contain intentionally managed artifacts such as:
- `configuration.yaml`
- `dashboards/`
- `packages/`
- `themes/`
- `blueprints/`
- selected `custom_components/`
- selected `www/` assets
- `secrets.example.yaml`

Git should not contain runtime-generated or sensitive artifacts such as:
- `.storage/`
- `.cache/`
- logs
- databases
- backups
- `deps/`
- `tts/`
- real `secrets.yaml`

### `archive/`
Use this for lightweight migration notes and small archive markers only.

Do not place raw runtime dumps, secrets, databases, or generated Home Assistant state in git archives.

## Agent boundary

- OpenClaw source of truth lives under `/home/docker/.openclaw/`
- this repo should not maintain its own parallel agent control-plane directory

## Per-service Docker pattern

Each Dockerized homelab service should usually follow this shape:

```text
service/
├─ docker-compose.yml
├─ .env.example
├─ README.md
├─ scripts/
└─ runtime folders ignored by git
```

## Environment file workflow

`git pull` does not copy secrets from `.env.example` into `.env`.

The intended workflow is:

1. Commit `.env.example` with placeholder values and variable names only.
2. Keep the real `.env` file out of git.
3. On the target machine, copy `.env.example` to `.env` once and fill in the real values.
4. Reuse that same `.env` on future pulls unless the example file adds new variables.

## Recovery model

- Git stores desired config and human-managed artifacts.
- Running systems store live mutable state.
- Backups must cover the parts intentionally excluded from git.
