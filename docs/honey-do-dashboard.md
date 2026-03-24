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

The Grocy version is scaffolded and intended to be wired after the Grocy integration is installed.

Recommended Grocy modeling:

- recurring chores as Grocy chores
- one-off honey-do items as Grocy tasks
- Ross and Kelly as assignment labels, categories, or task naming convention

## Initial Projects

- Kitchen Countertops — Kelly — 2026-07-01
- Basement Sliding Doors — Ross — 2026-07-01
- Mailbox Sign — Kelly — 2026-06-01
- Bathtub Caulking — Ross — 2026-08-01
- Recessed Lights — Ross — 2026-10-01
- Upstairs Air Condition — Ross — 2026-05-01
- Kitchen Cabinet Painting — Kelly — 2026-05-01
- Dining Room Cabinet Build — Ross — 2026-06-15
- Dining Room Cabinet Organization — Kelly — 2026-07-01
- Sell or Toss Wedding Decorations — Kelly — 2026-06-01
- Remove Clutter — Kelly — 2026-06-01

## Recurring Chores

- Walk the dog
- Vacuum
- Clean upstairs bathroom
- Clean living room bathroom
- Clean downstairs bathroom
- Wash sheets
- Fold laundry
