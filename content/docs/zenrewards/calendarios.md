---
title: "Calendarios temáticos"
description: "Crea calendarios tipo adviento con fechas de desbloqueo."
---

Permite crear calendarios tipo “Adviento” para eventos especiales. Cada día se desbloquea en una fecha específica.

---

## 🧱 Estructura (`calendars/<nombre>.yml`)

```yaml
title: "&4&lChristmas &2&lCalendar"
rows: 4

# Si true, los jugadores pueden reclamar días pasados que no reclamaron
allow-past-claims: false

days:
  1:
    date: "2026-12-01"           # Fecha en la que se desbloquea
    commands:
      - "eco give %player% 500"
    display:
      name: "&aDay 1: Sweet Candy"
      lore:
        - "&7Merry start to the holidays!"
        - "&6+500 Coins"
  24:
    date: "2026-12-24"
    commands:
      - "eco give %player% 10000"
      - "crate give %player% legendary 2"
    display:
      name: "&bDay 24: Christmas Eve Special!"
      lore:
        - "&dMerry Christmas to all!"
        - "&6+10000 Coins"
        - "&d+2 Legendary Keys"

# Slots del menú
reward_slots:
  - 10
  - 11
  - 12
  - 16

# Apariencia de los items
reward_item:
  claimable:
    material: STAINED_GLASS_PANE:4
    name: "&e&lDay {day} Reward! &a(Click to claim)"
  claimed:
    material: STAINED_GLASS_PANE:5
    name: "&a&lDay {day} - Claimed"
  locked:
    material: STAINED_GLASS_PANE:14
    name: "&c&lDay {day} - Locked"
    lore:
      - "&7Unlocks on: &e{date}"
```

---

## 🧠 Variables del menú

| Variable | Descripción |
| :-- | :-- |
| `{day}` | Número del día |
| `{date}` | Fecha de desbloqueo (yyyy-MM-dd) |
| `{reward_name}` | Nombre de la recompensa |
| `{reward_lore}` | Lore de la recompensa |

---

## ➕ Crear un nuevo calendario

1. Crea un archivo en `plugins/ZenRewards/calendars/` (ej. `halloween.yml`).
2. Sigue la misma estructura que `christmas.yml`.
3. El nombre del archivo sin extensión será el ID (ej. `halloween`).
4. Usa `/calendar halloween` para abrirlo.
5. Ejecuta `/zr reload` para cargar el nuevo calendario.

---

## 🔒 Lógica de desbloqueo

- **Fecha actual < fecha del día** → **Locked**.
- **Fecha actual == fecha del día** → **Claimable**.
- **Fecha actual > fecha del día** y `allow-past-claims: true` → **Claimable**.
- **Fecha actual > fecha del día** y `allow-past-claims: false` → **Locked** permanente.
