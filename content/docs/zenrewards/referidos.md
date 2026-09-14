---
title: "Sistema de referidos (referrals.yml)"
description: "Recompensas por invitaciones y menú de hitos."
---

Permite que los jugadores refieran a otros y reciban recompensas tanto el referido como el referente.

---

## ⚙️ Configuración

```yaml
# Recompensas para el jugador que fue referido
referred-rewards:
  commands:
    - "eco give %player% 500"
  messages:
    - "%prefix%&aYou received &e500 Coins&a for entering a referrer!"

# Recompensas para el jugador que hizo la invitación
referrer-rewards:
  commands:
    - "eco give %player% 1000"
  messages:
    - "%prefix%&aYour friend &e%referred%&a entered you as their referrer! You received &e1000 Coins&a."

# Hitos de invitaciones acumuladas
milestones:
  3:
    commands:
      - "eco give %player% 5000"
      - "crate give %player% common 2"
    display:
      name: "&e3 Invites Milestone"
      lore:
        - "&7Refer 3 players to unlock!"
        - "&6+5000 Coins"
        - "&e+2 Common Keys"
  5:
    commands:
      - "eco give %player% 10000"
      - "crate give %player% rare 1"
    display:
      name: "&a5 Invites Milestone"
  10:
    commands:
      - "eco give %player% 25000"
      - "crate give %player% legendary 1"
    display:
      name: "&b10 Invites Master Milestone"
```

---

## 🔁 Variables en mensajes

| Variable | Descripción |
| :-- | :-- |
| `%player%` | Nombre del jugador actual |
| `%referred%` | Nombre del jugador referido |

---

## 🖥️ Menú de referidos (referrals-menu.yml)

```yaml
title: "&8Referral Milestones"
rows: 4

reward_slots:
  - 11
  - 13
  - 15

other_items:
  stats_display:
    slot: 4
    material: PAPER
    name: "&e&lYour Referral Stats"
    lore:
      - "&7Total Successful Invites: &e{player_invites}"
      - "&7Who Invited You: &e{referrer_name}"
      - ""
      - "&fInvite friends by telling them to run:"
      - "&e/referral claim %player%"
```

---

## 🧠 Variables del menú

| Variable | Descripción |
| :-- | :-- |
| `{count}` | Cantidad de invitaciones requeridas |
| `{player_invites}` | Invitaciones del jugador |
| `{referrer_name}` | Nombre de quien lo invitó |
| `{reward_name}` | Nombre de la recompensa del hito |
| `{reward_lore}` | Lore de la recompensa |

---

## 📌 Reglas de referidos

- Un jugador **solo puede establecer un referente una vez**.
- **No se puede auto-referir**.
- El referente debe haber jugado antes en el servidor.
- Si el referente está **offline**, sus recompensas se guardan como **pendientes**.
