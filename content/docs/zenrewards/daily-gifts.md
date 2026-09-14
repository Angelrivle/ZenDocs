---
title: "Daily Gifts (daily-gifts.yml)"
description: "Regalos secuenciales con cooldown y menú de progreso."
---

Sistema de regalos secuenciales que se desbloquean uno a uno.

---

## ⚙️ Configuración

```yaml
# Cooldown entre regalo y regalo
cooldown_between_gifts: "24h"

# Cooldown global al completar TODOS los regalos (ciclo de reinicio)
cycle_cooldown: "24h"

# Regalos secuenciales
gifts:
  1:
    display_name: "&aDaily Gift #1"
    texture: "eyJ0ZXh0dXJlcyI6eyJTS0lOIj..."
    commands:
      - "eco give %player% 100"
    messages:
      - "%prefix%&aYou have claimed Daily Gift #1! &7(+100 Coins)"
  2:
    display_name: "&aDaily Gift #2"
    texture: "eyJ0ZXh0dXJlcyI6eyJTS0lOIj..."
    commands:
      - "eco give %player% 150"
    messages:
      - "%prefix%&aYou have claimed Daily Gift #2! &7(+150 Coins)"
  12:
    display_name: "&6&lDaily Gift #12 &d&l[MEGA]"
    texture: "eyJ0ZXh0dXJlcyI6eyJTS0lOIj..."
    commands:
      - "eco give %player% 1000"
      - "crate give %player% epic_key 1"
    messages:
      - "%prefix%&d&lMEGA CLAIM! &aYou claimed the final Daily Gift #12!"
```

---

## 🖥️ Menú de Daily Gifts (menus/daily-gifts-menu.yml)

```yaml
title: "&8Daily Gifts Progression"
rows: 6

reward_slots:
  - 10
  - 11
  - 12
  - 13
  - 14
  - 15
  - 16
  - 19
  - 20
  - 21
  - 22
  - 23
  - 28
  - 29
  - 30
  - 31
  - 32
  - 33
  - 34

gift_item:
  claimable:
    material: SKULL_ITEM:3
    name: "{display_name} &7(&aClaimable&7)"
    lore:
      - "&e▶ Click to claim!"
  claimed:
    material: SKULL_ITEM:3
    name: "{display_name} &7(&8Claimed&7)"
  cooldown:
    material: BARRIER
    name: "{display_name} &7(&eCooldown&7)"
    lore:
      - "&7Time Remaining: &f%cooldown%"
  locked:
    material: SKULL_ITEM:3
    name: "{display_name} &7(&cLocked&7)"

other_items:
  progress_clock:
    slot: 49
    material: WATCH
    name: "&e&lClaiming Progress &7(%progress%)"
    lore:
      - "&8• &7Gifts Claimed: &a%gifts_claimed% &7/ &e%total_gifts%"
      - "&8• &7Cycle Status: &fRunning"
      - ""
      - "&eNext Cooldown / Reset:"
      - " &8• &f%cooldown%"
```

---

## 🔁 Cómo funciona

1. El jugador empieza con 0 regalos reclamados.
2. Solo puede reclamar el siguiente regalo en la secuencia.
3. Después de reclamar un regalo, debe esperar `cooldown_between_gifts`.
4. Al reclamar **todos** los regalos, se inicia un `cycle_cooldown`.
5. Después del cycle_cooldown, la progresión se reinicia a 0.

---

## 🧠 Variables del menú

| Variable | Descripción |
| :-- | :-- |
| `{display_name}` | Nombre del regalo |
| `%cooldown%` | Tiempo restante del cooldown |
| `%progress%` | Regalos reclamados / total |
| `%gifts_claimed%` | Número de regalos reclamados |
| `%total_gifts%` | Total de regalos configurados |

---

## ➕ Añadir más regalos

1. Añade una nueva entrada en `daily-gifts.yml` bajo `gifts:` (ej. `13:`).
2. Añade slots en `menus/daily-gifts-menu.yml` bajo `reward_slots:`.
3. Si necesitas más espacio, aumenta `rows:`.
4. Ejecuta `/zr reload`.
