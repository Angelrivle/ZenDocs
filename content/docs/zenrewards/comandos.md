---
title: "Comandos"
description: "Listado completo de comandos de jugador, consola y administrador en ZenRewards."
---

## 🎮 Comandos de jugador

| Comando | Aliases | Descripción | Soporte consola |
| :-- | :-- | :-- | :--: |
| `/rewards` | `/recompensa`, `/reward`, `/recompensas` | Abre el menú principal de recompensas | ❌ |
| `/rewards pending` | — | Abre el menú de recompensas pendientes (offline) | ❌ |
| `/streak` | `/racha` | Abre el menú de rachas de conexión | ✅* |
| `/playtime` | `/tiempodejuego` | Abre el menú de tiempo de juego | ✅* |
| `/calendar <nombre>` | `/calendario <nombre>` | Abre un calendario temático | ✅* |
| `/referral claim <jugador>` | `/referido claim`, `/refer claim` | Establece quién te invitó | ✅* |
| `/referral gui` | `/referral menu`, `/referral stats` | Abre el menú de hitos de referidos | ❌ |
| `/dailygifts` | `/gifts`, `/regalos` | Abre el menú de Daily Gifts | ❌ |
| `/dailygifts claim` | — | Reclama el siguiente regalo disponible | ❌ |

> **Soporte de consola:** los comandos marcados con ✅* tienen variantes para consola que ejecutan acciones en nombre de un jugador.

---

## 🖥️ Comandos de consola

| Comando | Descripción |
| :-- | :-- |
| `/streak claim <jugador> <día>` | Reclama la recompensa de racha del día X para un jugador |
| `/playtime claim <jugador> <milestone>` | Reclama un hito de playtime para un jugador |
| `/calendar claim <jugador> <calendario> <día>` | Reclama un día de calendario para un jugador |
| `/referral claim <referido> <referente>` | Registra un referido desde consola |

---

## 🛠️ Comandos de administrador

| Comando | Aliases | Descripción | Permiso |
| :-- | :-- | :-- | :-- |
| `/zr reload` | `/zenrewards reload` | Recarga todos los archivos de configuración | `zenrewards.admin` |
| `/zr reset <jugador> <id\|all>` | — | Reinicia cooldowns de recompensas de un jugador | `zenrewards.admin` |
| `/zr migrate <sqlite\|mysql>` | — | Migra la base de datos entre tipos | `zenrewards.admin` |

---

## ⌨️ Autocompletado (tab completion)

- `/zr` → `reload`, `reset`, `migrate`
- `/zr reset` → nombres de jugadores
- `/zr reset <jugador>` → `all` + IDs de recompensas
- `/zr migrate` → `sqlite`, `mysql`
- `/calendar` → `claim` + nombres de calendarios cargados
- `/referral` → `claim`, `gui`
- `/referral claim` → nombres de jugadores online
- `/streak claim` → nombres de jugadores + números de día
- `/playtime claim` → nombres de jugadores + hitos configurados
- `/rewards` → `pending`
- `/dailygifts` → `claim`
