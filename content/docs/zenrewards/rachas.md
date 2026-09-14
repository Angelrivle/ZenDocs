---
title: "Rachas de conexión (streaks.yml)"
description: "Configura recompensas por días consecutivos y su menú."
---

Recompensa a los jugadores por conectarse días consecutivos. Si el jugador falla un día, la racha se reinicia a 1.

---

## ⚙️ Configuración

```yaml
# Mensaje de reclamo
claim-message: "%prefix%&aYou have claimed your streak reward for day &e{day}&a!"

# Recompensas por día
rewards:
  1:
    commands:
      - "eco give %player% 100"
    display:
      name: "&aDay 1: Iron Reward"
      lore:
        - "&7Claimed for logging in 1 day."
        - "&6+100 Coins"
  7:
    commands:
      - "eco give %player% 1000"
      - "crate give %player% common 1"
    display:
      name: "&bDay 7: Weekly Reward"
      lore:
        - "&7A full week of logging in!"
        - "&6+1000 Coins"
        - "&e+1 Common Key"
```

---

## 🖥️ Menú de rachas (streak-menu.yml)

```yaml
title: "&8Login Streak"
rows: 4

# Slots donde se muestran los días
reward_slots:
  - 10
  - 11
  - 12
  - 13
  - 14
  - 15
  - 16

# Apariencia según estado
reward_item:
  claimable:           # Disponible para reclamar
    material: STAINED_GLASS_PANE:4
    name: "&eDay {day} Reward! &a(Click to claim)"
  claimed:             # Ya reclamado
    material: STAINED_GLASS_PANE:5
    name: "&aDay {day} - Claimed"
  locked:              # Bloqueado (día no alcanzado)
    material: STAINED_GLASS_PANE:14
    name: "&cDay {day} - Locked"
  unconfigured:        # Sin recompensa configurada
    material: BARRIER
    name: "&cDay {day}"
```

---

## 🧠 Variables del menú

| Variable | Descripción |
| :-- | :-- |
| `{day}` | Número del día |
| `{reward_name}` | Nombre de la recompensa |
| `{reward_lore}` | Lore de la recompensa |

---

## 🔄 Cómo funciona la racha

1. El jugador se conecta → se compara su último login con la fecha actual.
2. Si el último login fue **ayer** → la racha incrementa en 1.
3. Si el último login fue **hoy** → no cambia.
4. Si el último login fue hace **más de 1 día** → la racha se reinicia a 1.
5. Al abrir `/streak`, puede reclamar la recompensa del día correspondiente.
