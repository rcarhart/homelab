#!/bin/sh
set -eu

STAMP="$(date +%Y-%m-%d_%H-%M-%S)"
DEST="/backups/mealie-data-${STAMP}.tar.gz"

mkdir -p /backups
tar -czf "$DEST" -C /source .

find /backups -type f -name 'mealie-data-*.tar.gz' | sort | head -n -14 | xargs -r rm -f

echo "Backup complete: $DEST"