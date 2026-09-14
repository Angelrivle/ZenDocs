---
title: "Tiempo de juego (playtime.yml)"
description: "Hitos por tiempo acumulado y menú de playtime."
---

Otorga recompensas cuando el jugador alcanza ciertos hitos de tiempo jugado acumulado en el servidor.

---

## ⚙️ Configuración

```yaml
rewards:
  "30m":                          # Hito de 30 minutos
    commands:
      - "eco give %player% 250"
    display:
      name: "&e30 Minutes Reward"
      lore:
        - "&7Granted for playing 30 minutes!"
        - "&6+250 Coins"
  "1h":                           # Hito de 1 hora
    commands:
      - "eco give %player% 500"
      - "give %player% iron_ingot 5"
    display:
      name: "&a1 Hour Reward"
      lore:
        - "&7Granted for playing 1 hour!"
  "5h":                           # Hito de 5 horas
    commands:
      - "eco give %player% 2500"
      - "crate give %player% common 2"
    display:
      name: "&b5 Hours Reward"
  "24h":                          # Hito de 24 horas
    commands:
      - "eco give %player% 10000"
      - "crate give %player% rare 1"
    display:
      name: "&d24 Hours Master Reward"
```

---

## 🖥️ Menú de playtime (playtime-menu.yml)

```yaml
title: "&8Playtime Rewards"
rows: 4

reward_slots:
  - 10
  - 12
  - 14
  - 16

reward_item:
  claimable:
    material: STAINED_GLASS_PANE:4
    name: "&e{time} Playtime Reward! &a(Click to claim)"
  claimed:
    material: STAINED_GLASS_PANE:5
    name: "&a{time} Playtime - Claimed"
  locked:
    material: STAINED_GLASS_PANE:14
    name: "&c{time} Playtime - Locked"
    lore:
      - "&7Your Playtime: &e{player_playtime}"
```

---

## 🧠 Variables del menú

| Variable | Descripción |
| :-- | :-- |
| `{time}` | Hito de tiempo (ej. `30m`, `1h`, `24h`) |
| `{reward_name}` | Nombre de la recompensa |
| `{reward_lore}` | Lore de la recompensa |
| `{player_playtime}` | Tiempo de juego actual del jugador |

---

## 📈 Cómo se calcula el playtime

- Se trackea en tiempo real mientras el jugador está conectado.
- Al desconectarse, se guarda el tiempo acumulado de la sesión.
- El tiempo total es la suma de todas las sesiones anteriores más la sesión actual.
