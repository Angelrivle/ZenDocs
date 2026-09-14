---
title: "Configuración general (config.yml)"
description: "Módulos, sonidos y base de datos."
---

```yaml
# Toggle de módulos
modules:
  rewards: true
  streak: true
  playtime: true
  calendars: true
  referrals: true
  daily_gifts: true

# Sonidos del plugin (formato: NOMBRE_SONIDO:volumen:pitch)
sounds:
  success: "LEVEL_UP:1.0:1.2"       # Al reclamar una recompensa
  fail: "VILLAGER_NO:1.0:1.0"       # Al intentar reclamar sin cumplir requisitos
  open: "CHEST_OPEN:1.0:1.0"        # Al abrir un menú
  notify: "ORB_PICKUP:1.0:1.5"      # Notificación al conectarse

# Configuración de Base de Datos
database:
  type: "sqlite"  # Opciones: sqlite, mysql
  mysql:
    host: "localhost"
    port: 3306
    database: "zenrewards"
    username: "root"
    password: ""
    ssl: false
```

---

## 🔊 Notas sobre sonidos

Los sonidos utilizan **XSound** internamente, lo que significa que los nombres de los sonidos son cross‑version. Usa nombres genéricos como `LEVEL_UP`, `CHEST_OPEN`, `VILLAGER_NO`, `ORB_PICKUP`, etc. y el plugin resolverá automáticamente el sonido correcto para tu versión de Minecraft.

Formato: `NOMBRE:volumen:pitch`
