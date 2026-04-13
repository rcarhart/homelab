# Weekly Restore Drill – Operational Checklist

**Owner:** Sir Alex  
**Schedule:** Fridays, automated evidence capture; quarterly full restore drill  
**Version:** 1.0 — 2026-04-03

---

## Purpose

Confirm that the homelab's critical services can actually be restored from backup before a real incident forces the question. This checklist covers:

1. Backup artifact verification (automated, weekly)
2. Container health readiness check (automated, weekly)
3. Manual restore simulation (quarterly, human-driven)

---

## Automated Weekly Steps

These run via the OpenClaw cron job `weekly-restore-drill`. Evidence is written to `/home/docker/projects/homelab/docs/restore-evidence/`.

### Step A — Mealie Backup Artifact Check
```bash
# Confirm backup container is running/healthy or has exited cleanly
docker inspect mealie-backup --format '{{.State.Status}} {{.State.ExitCode}}'

# Confirm backup volume has recent files (within 7 days)
find /var/lib/docker/volumes/ -name "*.zip" -newer /tmp/.restore-drill-anchor 2>/dev/null \
  || docker exec mealie ls /app/data/backups/ 2>/dev/null | tail -5
```

**Pass:** Container healthy or exited 0 AND at least one backup artifact exists within 7 days.  
**Fail:** Container restarting, or no recent artifact — escalate as blocker.

### Step B — Grocy Backup Artifact Check
```bash
# Grocy stores data in a volume; confirm the volume is present and non-empty
docker inspect grocy --format '{{range .Mounts}}{{.Source}} {{.Type}}{{"\n"}}{{end}}'
```

**Pass:** Volume path resolves and is mounted.  
**Fail:** Volume missing or container not running — escalate.

### Step C — Immich / Paperless / Plex Health Ping
```bash
# Confirm containers are still healthy — service health, not backup state
for svc in immich grocy mealie paperless; do
  docker inspect $svc --format "$svc: {{.State.Status}}" 2>/dev/null || echo "$svc: NOT FOUND"
done
```

**Pass:** All critical services show `running`.  
**Fail:** Any service missing or stopped — flag for attention.

### Step D — Write Evidence Artifact
```bash
mkdir -p /home/docker/projects/homelab/docs/restore-evidence
DATESTAMP=$(date +%Y-%m-%d)
echo "Restore drill evidence — $DATESTAMP" > /home/docker/projects/homelab/docs/restore-evidence/$DATESTAMP.txt
docker ps --format "{{.Names}}: {{.Status}}" >> /home/docker/projects/homelab/docs/restore-evidence/$DATESTAMP.txt
echo "Mealie backup check:" >> /home/docker/projects/homelab/docs/restore-evidence/$DATESTAMP.txt
docker inspect mealie-backup --format '{{.State.Status}} exit={{.State.ExitCode}}' >> /home/docker/projects/homelab/docs/restore-evidence/$DATESTAMP.txt 2>&1
```

---

## Quarterly Full Restore Drill (Manual)

Run this with Ross present or after explicit approval. It covers a non-destructive restore simulation.

### Pre-checks
- [ ] Identify the most recent Mealie backup artifact
- [ ] Confirm a **test** Mealie instance exists or can be stood up (`mealie-dev`)
- [ ] Confirm you have the Mealie backup import API endpoint or CLI method documented

### Drill Steps
1. **Copy most recent backup** from backup volume to `/tmp/restore-test/`
2. **Stand up mealie-dev** if not already running
3. **Import backup** via Mealie admin UI or API into the dev instance
4. **Verify** that recipe count, cookbook count, and user data are present
5. **Document result** in `restore-evidence/YYYY-MM-DD-full-drill.txt`
6. **Tear down** test instance if it was spun up just for the drill

### Pass criteria
- Backup imports without error
- Recipe and cookbook counts match the source backup metadata
- No plaintext credentials visible in the restored config

---

## Escalation Path

| Issue | Action |
|---|---|
| `mealie-backup` container in restart loop | Check compose logs; fix backup config; alert Ross if > 24h |
| No backup artifact within 7 days | Alert Ross immediately — data loss window is open |
| Full restore drill fails | Do not promote to production; root-cause and fix before next drill |

---

## Evidence Directory

`/home/docker/projects/homelab/docs/restore-evidence/`

Files: `YYYY-MM-DD.txt` (weekly automated), `YYYY-MM-DD-full-drill.txt` (quarterly manual)

---

## Notes

- `mealie-backup` container is currently in a restart loop (observed 2026-04-03). This is an active gap.
- Plex and Immich backup procedures are not yet fully documented — scope them in the next quarterly cycle.
