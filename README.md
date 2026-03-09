# Mealie

Self-hosted recipe manager running in Docker.

## Setup

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Clone this repo
3. Run the stack:

```bash
docker compose up -d
```

4. Open [http://localhost:9925](http://localhost:9925)
5. Log in with the default credentials:
   - **Email:** `changeme@example.com`
   - **Password:** `MyPassword`

> Change your email and password after first login.

## Stack

| Service | Image | Port |
|---------|-------|------|
| Mealie  | `ghcr.io/mealie-recipes/mealie:latest` | `9925` |

## Data

Recipe data, images, and the database are persisted in the `./data` directory (excluded from git).
