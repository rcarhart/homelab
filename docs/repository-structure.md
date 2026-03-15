# Repository Structure

This repo is organized so the Docker VM can pull cleanly while keeping secrets and runtime data local.

## Folder layout

```text
homelab/
├─ app/
│  ├─ mealie/
│  ├─ immich/
│  ├─ paperless/
│  └─ plex/
├─ infrastructure/
│  ├─ cloudflared/
│  └─ portainer/
├─ home-assistant/
└─ docs/
```

## Per-service pattern

Each Dockerized service should follow the same shape:

```text
service/
├─ docker-compose.yml
├─ .env.example
├─ README.md
├─ scripts/
└─ runtime folders ignored by git
```

## Environment file workflow

`git pull` does not pull secrets from `.env.example` into `.env`.

The intended workflow is:

1. Commit `.env.example` with placeholder values and variable names only.
2. Keep the real `.env` file out of git.
3. On the Docker VM, copy `.env.example` to `.env` once and fill in the real values.
4. Reuse that same `.env` on future pulls unless the example file adds new variables.

Example:

```bash
cd app/mealie
cp .env.example .env
docker compose up -d
```

## What should stay out of git

- `.env`
- database files
- uploaded media
- service backups
- cache and logs
