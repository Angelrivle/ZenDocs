---
title: "Estructura de archivos"
description: "Carpetas y archivos generados por ZenRewards."
---

```
plugins/ZenRewards/
├── config.yml                    # Configuración general, módulos, sonidos, DB
├── rewards.yml                   # Definición de recompensas
├── messages.yml                  # Todos los mensajes del plugin
├── streaks.yml                   # Recompensas de rachas
├── playtime.yml                  # Hitos de tiempo de juego
├── referrals.yml                 # Sistema de referidos
├── daily-gifts.yml               # Configuración de Daily Gifts
├── webhooks.yml                  # Webhooks de Discord
├── menus/
│   ├── menu.yml                  # Menú principal de recompensas
│   ├── streak-menu.yml           # Menú de rachas
│   ├── playtime-menu.yml         # Menú de playtime
│   ├── referrals-menu.yml        # Menú de referidos
│   └── daily-gifts-menu.yml      # Menú de Daily Gifts
├── calendars/
│   └── christmas.yml             # Calendario de Navidad (ejemplo)
└── zenrewards.db                 # Base de datos SQLite (si se usa)
```
