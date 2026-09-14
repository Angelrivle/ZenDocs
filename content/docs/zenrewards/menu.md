---
title: "Menú Principal (menus/menu.yml)"
description: "Configura el menú principal de recompensas, sus items y variables dinámicas."
---

Configura completamente el inventario GUI del menú de recompensas.

---

## ⚙️ Configuración general

```yaml
title: "&8Reward Menu"    # Título del inventario
rows: 6                   # Número de filas (1-6)

filler_item:              # Item de relleno para slots vacíos
  material: STAINED_GLASS_PANE:15
  name: " "
  lore: []
```

---

## 🧩 Tipos de ítems en el menú

### 1) Ítems de recompensa

Cada ítem de recompensa tiene 3 estados visuales:

```yaml
items:
  mi_recompensa:
    slot: 21                    # Posición en el inventario (0-53)
    reward_id: "daily_reward"   # ID que coincide con rewards.yml

    claimable-item:             # Cuando la recompensa está disponible
      material: CHEST
      name: "&fDaily Reward &7(%status%&7)"
      lore:
        - "&eClick to claim!"

    cooldown-item:              # Cuando está en cooldown
      material: BEDROCK
      name: "&fDaily Reward &7(%status%&7)"
      lore:
        - "&7Remaining Time: &e%cooldown_status%"

    no-permission-item:         # Cuando no tiene permiso
      material: BARRIER
      name: "&cDaily Reward &7(&cNot Available&7)"
```

Para recompensas de tipo `UNIQUE`, también existe:

```yaml
    unique-claimed-item:        # Cuando ya la ha reclamado (UNIQUE)
      material: SKULL_ITEM:3
      name: "&fWelcome Reward &7(%status%&7)"
```

---

### 2) Ítems de opciones (toggles)

```yaml
toggle_notifications_item:
  slot: 48
  type: "OPTION_TOGGLE_NOTIFICATIONS"    # Tipo especial de toggle
  permission: "zenrewards.options.notifications"
  has-permission-item:
    material: BOOK
    name: "&eToggle Notifications"
    lore:
      - "&eStatus: &f%player_notify_status%"
  no-permission-item:
    material: BARRIER
    name: "&eToggle Notifications"
    lore:
      - "&cYou do not have permission to use this option."
```

Tipos disponibles:
- `OPTION_TOGGLE_NOTIFICATIONS` — Activa/desactiva notificaciones al entrar.
- `OPTION_TOGGLE_AUTOCLAIM` — Activa/desactiva el auto-reclamo.

---

### 3) Ítems personalizados (decoración/navegación)

```yaml
close_menu_item:
  slot: 49
  material: BARRIER
  name: "&c&lClose Menu"
  lore:
    - "&7Click to exit."
  commands:
    - "[close]"

hub_item:
  slot: 45
  material: ARROW
  name: "&e&lBack"
  lore:
    - "&7Return to the previous menu."
  commands:
    - "[player] menu"       # Ejecuta /menu como si el jugador lo escribiera
```

---

## 🧠 Variables disponibles en ítems

| Variable | Descripción |
| :-- | :-- |
| `%status%` | Estado de la recompensa (Claimable, Cooldown, Claimed, Locked) |
| `%cooldown_status%` | Tiempo restante del cooldown formateado |
| `%player_notify_status%` | Estado de notificaciones (Activated/Disabled) |
| `%player_autoclaim_status%` | Estado del auto-claim (Activated/Disabled) |

---

## 🧑‍🦲 Cabezas personalizadas

```yaml
material: SKULL_ITEM:3
head-texture-value: "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6..."  # Textura Base64
```

---

## ⚡ Comandos especiales en ítems

| Comando | Acción |
| :-- | :-- |
| `[close]` | Cierra el menú |
| `[player] comando` | Ejecuta el comando como jugador |
| `comando normal` | Se ejecuta desde consola |

Si necesitas más ejemplos, revisa la sección de [Acciones de ítem](acciones).
