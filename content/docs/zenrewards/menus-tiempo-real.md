---
title: "Menús GUI en tiempo real"
description: "Actualización dinámica de cooldowns y estados en menús."
---

Los menús de ZenRewards se actualizan **en tiempo real** sin necesidad de cerrar y reabrir el inventario.

---

## ✅ Características

- **Temporizadores dinámicos** — Los cooldowns se actualizan cada segundo.
- **Estado en vivo** — Los ítems cambian de estado mientras el menú está abierto.
- **Reclamo sin parpadeo** — Actualiza el ítem sin recargar todo el menú.
- **Menús soportados:**
  - Menú Principal de Recompensas
  - Menú de Rachas
  - Menú de Playtime
  - Menú de Calendarios
  - Menú de Referidos
  - Menú de Daily Gifts
  - Menú de Pendientes

---

## ⚙️ Implementación técnica

Los menús usan un `MenuUpdateTask` (BukkitRunnable) que se ejecuta cada segundo y actualiza dinámicamente los contenidos del inventario abierto. Al cerrar el menú, la tarea se cancela automáticamente.
