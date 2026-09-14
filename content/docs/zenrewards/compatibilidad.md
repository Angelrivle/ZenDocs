---
title: "Compatibilidad de versiones"
description: "Soporte legacy y moderno gracias al VersionAdapter."
---

ZenRewards es compatible con Minecraft **1.8** hasta las versiones más recientes gracias a su sistema de **VersionAdapter**.

| Característica | 1.8 - 1.12 (Legacy) | 1.13+ (Modern) |
| :-- | :--: | :--: |
| Materiales con data value | `STAINED_GLASS_PANE:15` | `BLACK_STAINED_GLASS_PANE` |
| Cabezas de jugador | `SKULL_ITEM:3` | `PLAYER_HEAD` |
| Sonidos (XSound) | ✅ | ✅ |
| PlaceholderAPI | ✅ | ✅ |

> Se recomienda usar el formato legacy (`MATERIAL:data`) ya que el plugin los traduce automáticamente.
