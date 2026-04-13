# Mealie Dev

This directory is the local development fork/worktree for Mealie inside the homelab repo.

It exists so product-specific changes can be developed and tested separately from the deployed Mealie stack in `../mealie/`.

## What this directory is for

- upstream Mealie application source
- local product changes for the shared-cookbook and related roadmap work
- backend-first development before rollout to the deployed stack

## What this directory is not for

- deployed production state
- broad homelab architecture notes
- runtime secrets committed to git

## Local role in this repo

- `app/mealie/` is the deployed/service-oriented Mealie directory
- `app/mealie-dev/` is the code-focused development area

Keep production and development concerns separate.

## Upstream reference

This project is based on Mealie upstream.

- Upstream repo: `https://github.com/mealie-recipes/mealie`
- Upstream docs: `https://docs.mealie.io/`

Use upstream documentation for framework internals, contributor setup, and general Mealie behavior. Use this README only for the local role of this fork inside the homelab repo.
