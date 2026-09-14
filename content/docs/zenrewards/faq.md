---
title: "Preguntas frecuentes (FAQ)"
description: "Respuestas rápidas a las dudas más comunes."
---

### ¿Cómo añado una nueva recompensa?

1. Defínela en `rewards.yml` con un ID único.
2. Añade un item en `menus/menu.yml` con el `reward_id` correspondiente.
3. Ejecuta `/zr reload`.

### ¿Cómo cambio el tamaño del menú?

Modifica el valor `rows` en el archivo de menú correspondiente (1-6 filas, 9 slots por fila).

### ¿Puedo tener más de un calendario activo?

Sí. Cada archivo `.yml` en `plugins/ZenRewards/calendars/` se carga como un calendario independiente. Usa `/calendar <nombre>` para abrir cada uno.

### ¿Qué pasa si un jugador reclama un referido estando offline?

Las recompensas se guardan como "pendientes" en la base de datos. Al conectarse, recibirá una notificación y podrá reclamarlas desde `/rewards pending`.

### ¿Puedo usar el plugin sin PlaceholderAPI?

Sí. El plugin funciona sin PlaceholderAPI, pero los placeholders `%zenrewards_...%` no estarán disponibles.

### ¿Cómo reinicio la racha de un jugador?

Usa `/zr reset <jugador> all` o modifica la base de datos directamente.

### ¿Los Daily Gifts se reinician automáticamente?

Sí. Tras reclamar todos los regalos, se espera `cycle_cooldown` y el progreso se reinicia.

### ¿Puedo añadir más de 12 Daily Gifts?

Sí. Añade más entradas en `daily-gifts.yml` y los slots correspondientes en `menus/daily-gifts-menu.yml`.

### ¿Es seguro migrar de SQLite a MySQL en un servidor activo?

La migración se ejecuta de forma asíncrona. Es seguro ejecutarla con el servidor activo, pero se recomienda hacerlo con pocos jugadores online.
