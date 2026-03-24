# Honey Do Dashboard

This repo now contains two Home Assistant dashboard paths for household chores and projects:

- `dashboards/honey-do.yaml`
- `dashboards/honey-do-grocy.yaml`

## Native Home Assistant Version

The native version uses YAML helpers and automations from:

- `packages/honey_do.yaml`

Features:

- fixed-owner project list with due dates
- recurring chores that start unclaimed
- weekly reset every Monday at 5:00 AM
- completion tracking directly from the dashboard

## Grocy Version

The Grocy version is wired for the expected Grocy entities and the custom integration has been copied into:

- `home-assistant/custom_components/grocy`

The original cloned source is currently also present in:

- `home-assistant/custom_components/grocy-repo`

Recommended Grocy modeling:

- recurring chores as Grocy chores
- one-off honey-do items as Grocy tasks
- Ross and Kelly as task categories
- owner also included in task names for clarity

Home Assistant setup:

1. Add the `Grocy` integration in Settings > Devices & Services
2. Use URL `http://192.168.86.47`
3. Use port `9192`
4. Paste the Grocy API key in the config flow
5. Enable:
   - `sensor.grocy_tasks`
   - `sensor.grocy_chores`
   - `binary_sensor.grocy_overdue_tasks`
   - `binary_sensor.grocy_overdue_chores`

The Grocy dashboard uses summary helpers from:

- `packages/grocy_honey_do.yaml`

Canonical Grocy URL for this homelab:

- `http://192.168.86.47:9192`

This is also documented in:

- `app/grocy/README.md`
- `home-assistant/dashboards/honey-do-grocy.yaml`

Seed script for the initial household setup:

- `app/grocy/scripts/seed-honey-do.ps1`

Run it on the server:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\seed-honey-do.ps1 -ApiKey "PASTE_NEW_API_KEY_HERE"
```

## Initial Projects

- Kitchen Countertops - Kelly - 2026-07-01
- Basement Sliding Doors - Ross - 2026-07-01
- Mailbox Sign - Kelly - 2026-06-01
- Bathtub Caulking - Ross - 2026-08-01
- Recessed Lights - Ross - 2026-10-01
- Upstairs Air Condition - Ross - 2026-05-01
- Kitchen Cabinet Painting - Kelly - 2026-05-01
- Dining Room Cabinet Build - Ross - 2026-06-15
- Dining Room Cabinet Organization - Kelly - 2026-07-01
- Sell or Toss Wedding Decorations - Kelly - 2026-06-01
- Remove Clutter - Kelly - 2026-06-01

## Recurring Chores

- Walk the dog - daily
- Vacuum - every 2 days in the initial seed
- Clean upstairs bathroom - weekly
- Clean living room bathroom - weekly
- Clean downstairs bathroom - weekly
- Wash sheets - weekly
- Kelly - Fold laundry - weekly
