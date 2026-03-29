# Home Assistant Config

This folder is the source-controlled, human-managed Home Assistant configuration for the live HA OS VM.

The live runtime config is hosted in the VM and exposed over Samba at `\\192.168.86.21\config`. This repo is intentionally not a full dump of that share. Keep only managed artifacts here and let Home Assistant own its generated/runtime state in the VM.

## Managed structure

```text
home-assistant/
├─ .gitignore
├─ README.md
├─ configuration.yaml
├─ secrets.example.yaml
├─ blueprints/
├─ custom_components/
├─ dashboards/
├─ packages/
├─ themes/
└─ www/
```

Use these paths for source-controlled config:

- `configuration.yaml` for top-level includes and core configuration
- `dashboards/` for Lovelace YAML dashboards
- `packages/` for grouped feature config
- `themes/` for custom themes
- `blueprints/` for shared blueprints you want to keep
- `custom_components/` for intentionally managed custom integrations
- `www/` for static assets you want under version control

Do not commit runtime/generated/sensitive content such as `.storage/`, `.cache/`, `.cloud/`, logs, databases, backups, `deps/`, `tts/`, or `secrets.yaml`.

## Workflow

1. Edit Home Assistant config locally in this repo.
2. Copy the changed managed files to the HA Samba share at `\\192.168.86.21\config`.
3. In Home Assistant, reload the affected YAML config when possible, or restart Home Assistant when required.
4. Keep HA OS backups for full-fidelity restore of the live system, because this repo intentionally does not track runtime state.
