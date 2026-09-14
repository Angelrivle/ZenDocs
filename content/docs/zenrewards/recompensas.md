---
title: "Recompensas (rewards.yml)"
description: "Estructura, tipos y variables de las recompensas configurables en ZenRewards."
---

Define todas las recompensas reclamables desde el menú principal. Cada recompensa tiene un identificador único y propiedades configurables.

---

## 🧱 Estructura de una recompensa

```yaml
rewards:
  mi_recompensa:                              # ID único de la recompensa
    type: REPEATABLE                          # REPEATABLE o UNIQUE
    cooldown: "1d"                            # Tiempo de espera para reclamar de nuevo
    permission: "rewardsystem.claim.daily"    # Permiso requerido (opcional)
    display_item:                             # Item de previsualización
      material: DIAMOND
      name: "&fMi Recompensa"
      lore:
        - "&7Descripción de la recompensa"
    commands:                                 # Comandos ejecutados al reclamar
      - "eco give %player% 100"
    messages:                                 # Mensajes enviados al jugador
      - "%prefix%&aHas recibido tu recompensa!"
```

---

## 🧪 Tipos de recompensa

| Tipo | Descripción |
| :-- | :-- |
| `REPEATABLE` | Se puede reclamar múltiples veces. Tras reclamar, entra en cooldown. |
| `UNIQUE` | Solo se puede reclamar una vez. No vuelve a estar disponible. |

---

## 🔁 Variables en comandos

| Variable | Descripción |
| :-- | :-- |
| `%player%` | Nombre del jugador que reclama |

---

## ✅ Ejemplo predeterminado

El plugin incluye recompensas de ejemplo como estas:

| ID | Tipo | Cooldown | Permiso | Descripción |
| :-- | :-- | :-- | :-- | :-- |
| `daily_reward` | REPEATABLE | 1d | `rewardsystem.claim.daily` | +100 Coins |
| `weekly_reward` | REPEATABLE | 7d | `rewardsystem.claim.weekly` | +250 Coins |
| `monthly_reward` | REPEATABLE | 7d | `rewardsystem.claim.monthly` | +500 Coins |
| `welcome_reward` | UNIQUE | 0s | `rewardsystem.claim.starter` | +250 Coins |
| `vip_reward` | REPEATABLE | 30d | `rewardsystem.claim.vip` | +250 Coins + 1 Common Key |
| `vip_plus_reward` | REPEATABLE | 30d | `rewardsystem.claim.vip_plus` | +500 Coins + 1 Uncommon Key |
| `mvp_reward` | REPEATABLE | 30d | `rewardsystem.claim.mvp` | +750 Coins + 1 Rare Key |
| `mvp_plus_reward` | REPEATABLE | 30d | `rewardsystem.claim.mvp_plus` | +1000 Coins + 1 Epic Key |
