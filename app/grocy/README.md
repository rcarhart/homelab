# Grocy

[Grocy](https://grocy.info) is the easiest path forward for this Home Assistant setup because it can run as a normal Docker app and does not require Home Assistant OS add-ons.

## Why this path

Your Home Assistant install type does not support add-ons. Instead of migrating Home Assistant, run Grocy as its own container and connect Home Assistant to it using the Grocy custom integration already placed in:

- `home-assistant/custom_components/grocy`

This keeps the setup simple and avoids changing your Home Assistant deployment model.

## Run it

```bash
cp .env.example .env
docker compose up -d
```

Grocy will then be available at:

- `http://<your-host>:9192`

If you are running this on the same machine as Home Assistant and keeping the existing plan, that means:

- `http://192.168.86.47:9192`

This is the canonical Grocy URL for this homelab right now and is also documented in:

- `docs/honey-do-dashboard.md`
- `home-assistant/dashboards/honey-do-grocy.yaml`

## First login

Default credentials from the LinuxServer image:

- username: `admin`
- password: `admin`

After logging in:

1. Change the password
2. Create an API key in Grocy
3. In Home Assistant, add the `Grocy` integration
4. Use URL `http://192.168.86.47`
5. Use port `9192`
6. Enable:
   - `sensor.grocy_tasks`
   - `sensor.grocy_chores`
   - `binary_sensor.grocy_overdue_tasks`
   - `binary_sensor.grocy_overdue_chores`

## Seed household data

There is a ready-to-run seed script for the Honey Do setup:

- `scripts/seed-honey-do.ps1`

Run it from the server with your current API key:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\seed-honey-do.ps1 -ApiKey "PASTE_NEW_API_KEY_HERE"
```

It creates:

- Ross and Kelly task categories
- the initial dated project tasks
- the recurring chores

Owner is stored in the task/chore name for simplicity.

## Data layout

- `docker-compose.yml` for the stack definition
- `.env.example` for safe defaults
- `.env` for the real runtime values
- `config/` for Grocy application state and database
