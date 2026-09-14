---
title: "Módulos del plugin"
description: "Activa o desactiva módulos individuales desde config.yml."
---

Cada módulo puede activarse o desactivarse individualmente desde `config.yml`. Cuando un módulo está desactivado, sus comandos, listeners y menús quedan completamente inactivos.

```yaml
modules:
  rewards: true      # Recompensas principales (diaria, semanal, etc.)
  streak: true       # Rachas de conexión
  playtime: true     # Recompensas por tiempo de juego
  calendars: true    # Calendarios temáticos
  referrals: true    # Sistema de referidos
  daily_gifts: true  # Daily Gifts
```
