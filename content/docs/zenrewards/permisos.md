---
title: "Permisos"
description: "Lista de permisos disponibles en ZenRewards y su uso recomendado."
---

## 🔐 Permisos

| Permiso | Descripción | Default |
| :-- | :-- | :-- |
| `zenrewards.admin` | Acceso a comandos admin (`/zr reload`, `/zr reset`, `/zr migrate`) | OP |
| `zenrewards.use` | Permite abrir el menú `/rewards` | true |
| `zenrewards.options.notifications` | Permite usar el toggle de notificaciones | — |
| `zenrewards.options.autoclaim` | Permite usar el toggle de auto-claim | — |
| `rewardsystem.claim.<reward>` | Permiso para reclamar una recompensa específica | — |

> **Nota:** Los permisos de recompensa (`rewardsystem.claim.*`) son completamente configurables. El permiso real se define en `rewards.yml`.
