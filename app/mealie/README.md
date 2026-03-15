# Mealie

[Mealie](https://mealie.io) is a self-hosted recipe manager and meal planner. It keeps recipes, meal plans, and grocery lists in one place.

## Running it

```bash
cp .env.example .env
docker compose up -d
```

Environment variables are loaded from `.env`. Commit `.env.example`, keep `.env` untracked, and create the real file on the Docker VM after pulling the repo.

## Stack

| Service | Image |
|---------|-------|
| Mealie  | `ghcr.io/mealie-recipes/mealie:latest` |

## Recommended layout

- `docker-compose.yml` for the stack definition
- `.env.example` for safe defaults and required variables
- `.env` on the VM for real values
- `data/` for runtime state
- `backups/` for local exports
- `scripts/` for maintenance helpers
