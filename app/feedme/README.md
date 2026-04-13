# FeedMe

Initial homelab deployment scaffold for FeedMe.

This stack is configured to use Ollama cloud with a Gemma 4 model by default.

## Running it

```bash
cp .env.example .env
docker compose up -d
```

Environment variables are loaded from `.env`. Commit `.env.example`, keep `.env` untracked, and create the real file on the Docker VM after pulling the repo.

## Stack

| Service | Image |
|---------|-------|
| FeedMe  | `ghcr.io/rcarhart/feedme:latest` |
