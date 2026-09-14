---
title: "Acciones de ítem"
description: "Comandos especiales para ítems de menú: cierre, ejecución como jugador o consola."
---

ZenRewards permite asignar acciones especiales en la lista `commands:` de cualquier ítem del menú.

---

## ✅ Acciones disponibles

| Comando | Acción |
| :-- | :-- |
| `[close]` | Cierra el menú actual |
| `[player] <comando>` | Ejecuta el comando como jugador |
| `<comando>` | Ejecuta el comando desde consola |

---

## 🧩 Ejemplo

```yaml
close_menu_item:
  slot: 49
  material: BARRIER
  name: "&c&lClose Menu"
  commands:
    - "[close]"

hub_item:
  slot: 45
  material: ARROW
  name: "&e&lBack"
  commands:
    - "[player] menu"

bonus_item:
  slot: 40
  material: SUNFLOWER
  name: "&e¡Bonus!"
  commands:
    - "eco give %player% 50"   # Ejecutado desde consola
```
