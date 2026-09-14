---
title: "Placeholders (PlaceholderAPI)"
description: "Listado completo de placeholders de ZenRewards y ejemplos de uso."
---

Requiere **PlaceholderAPI** instalado. Todos los placeholders se registran bajo el identificador `zenrewards`.

---

## ✅ Placeholders disponibles

| Placeholder | Descripción | Ejemplo de salida |
| :-- | :-- | :-- |
| `%zenrewards_streak_current%` | Racha de conexión actual del jugador | `5` |
| `%zenrewards_claimable_count%` | Cantidad de recompensas reclamables | `3` |
| `%zenrewards_playtime_current%` | Tiempo de juego total formateado | `2h 30m 15s` |
| `%zenrewards_playtime_status_<id>%` | Estado de un hito de playtime | `Claimable` / `Claimed` / `Locked` |
| `%zenrewards_referrals_count%` | Total de referidos exitosos | `7` |
| `%zenrewards_referrer%` | Nombre de quien invitó al jugador | `Steve` / `None` |
| `%zenrewards_referrer_name%` | Nombre de quien invitó (alias) | `Steve` / `None` |
| `%zenrewards_cooldown_<id>%` | Tiempo restante del cooldown de una recompensa | `23h 15m` / `Ready` / `Claimed` |
| `%zenrewards_status_<id>%` | Estado actual de una recompensa | `Claimable` / `Cooldown` / `Claimed` / `Locked` |
| `%zenrewards_pending_count%` | Cantidad de recompensas pendientes (offline) | `2` |
| `%zenrewards_has_pending%` | Si tiene recompensas pendientes | `Activated` / `Disabled` |
| `%zenrewards_calendar_claimed_<cal>_<day>%` | Si reclamó un día de calendario | `true` / `false` |

---

## 🧪 Ejemplo de uso

```
Racha: %zenrewards_streak_current% días
Playtime: %zenrewards_playtime_current%
Referidos: %zenrewards_referrals_count%
Recompensas Disponibles: %zenrewards_claimable_count%
```
