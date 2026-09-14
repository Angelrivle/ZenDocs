---
title: "Webhooks de Discord (webhooks.yml)"
description: "Notificaciones embebidas a Discord al reclamar recompensas o hitos."
---

Permite enviar notificaciones embebidas a un canal de Discord mediante webhooks.

---

## ⚙️ Configuración

```yaml
enabled: false
webhook-url: "https://discord.com/api/webhooks/your-webhook-url"

embeds:
  streak-milestone:
    title: "🔥 Streak Milestone Reached!"
    description: "Player **%player%** has achieved a daily streak of **%streak%** days!"
    color: "#FF4500"
    thumbnail: "https://minotar.net/helm/%player%/100.png"
    fields:
      - name: "Player"
        value: "%player%"
        inline: true
      - name: "Current Streak"
        value: "%streak% Days"
        inline: true
    footer:
      text: "ZenRewards system"
      icon-url: ""

  reward-claim:
    title: "🎁 Reward Claimed!"
    description: "Player **%player%** claimed the reward **%reward%**!"
    color: "#32CD32"

  playtime-milestone:
    title: "⏱️ Playtime Milestone Unlocked!"
    description: "Player **%player%** has unlocked the playtime milestone for **%time%**!"
    color: "#1E90FF"

  referral-claim:
    title: "🤝 New Referral Registered!"
    description: "Player **%player%** has set **%referrer%** as their inviter!"
    color: "#DA70D6"
```

---

## 🔁 Variables disponibles

| Evento | Variables |
| :-- | :-- |
| `streak-milestone` | `%player%`, `%streak%` |
| `reward-claim` | `%player%`, `%reward%` |
| `playtime-milestone` | `%player%`, `%time%` |
| `referral-claim` | `%player%`, `%referrer%` |

---

## ✨ Personalización de embeds

Cada embed soporta:
- `title`
- `description`
- `color`
- `thumbnail`
- `fields`
- `footer`
