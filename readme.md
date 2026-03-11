# Homelab Project

This repository contains the configuration and infrastructure for a personal homelab used for household management, self-hosting, and smart home control.

Primary goals:

- Host household services locally
- Build a kitchen wall dashboard
- Integrate smart home systems
- Replace some cloud services with self-hosted alternatives

---

# Core Architecture

The homelab runs on a **Lenovo ThinkCentre M720q** server using **Proxmox**.

Proxmox
├─ VM: Ubuntu + Docker
│ ├─ Mealie
│ ├─ Immich
│ ├─ Paperless
│ ├─ Plex
│ └─ Portainer
│
├─ VM: Home Assistant
│
└─ LXC: Pi-hole


---

# Primary Services

## Mealie
Recipe manager and meal planning system.

Public URL:recipes.rosscarhart.com


Functions:

- recipe storage
- meal planning
- grocery lists

---

## Home Assistant

Smart home control system and household dashboard.

Responsibilities:

- kitchen wall dashboard
- Nest integrations
- calendar integration
- chores
- grocery list
- weather
- doorbell camera

---

## Immich

Self-hosted photo backup and management.

---

## Paperless

Document management system.

---

## Plex

Media server.

---

## Pi-hole

Network-wide ad blocking.

---

# Dashboard

A wall-mounted **15-inch landscape display** will run a Home Assistant dashboard.

Design goals:

- dark mode
- minimal aesthetic
- Apple-style UI
- single screen
- tap expansions
- readable from across the room

