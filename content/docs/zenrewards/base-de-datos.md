---
title: "Base de datos"
description: "SQLite/MySQL, tablas y migración."
---

ZenRewards soporta **SQLite** y **MySQL** con connection pooling vía **HikariCP**.

---

## 🗄️ Tablas

| Tabla | Descripción |
| :-- | :-- |
| `zenrewards_player_data` | Datos del jugador (racha, playtime, login, opciones) |
| `zenrewards_cooldowns` | Cooldowns de cada recompensa por jugador |
| `zenrewards_claimed_calendars` | Días de calendario reclamados |
| `zenrewards_referrals` | Relaciones de referidos |
| `zenrewards_pending_rewards` | Recompensas pendientes (offline) |
| `zenrewards_daily_gifts` | Estado de Daily Gifts por jugador |

---

## 🔄 Migración

```
/zr migrate mysql     # Migra de SQLite a MySQL
/zr migrate sqlite    # Migra de MySQL a SQLite
```

Después de la migración:
1. Actualiza `database.type` en `config.yml`.
2. Ejecuta `/zr reload` o reinicia el servidor.

> La migración se ejecuta de forma asíncrona para no afectar el rendimiento.
