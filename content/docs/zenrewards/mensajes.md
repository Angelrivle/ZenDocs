---
title: "Mensajes (messages.yml)"
description: "Todos los textos del plugin son personalizables."
---

Todos los mensajes del plugin son configurables y soportan códigos de color `&`.

---

## 🧱 Estructura

```yaml
# Prefijo global
prefix: "&e&lZenRewards &8» &r"

# Textos para la variable %status% en los menús
reward-status:
  available: "&aClaimable"
  cooldown: "&eCooldown"
  claimed: "&aClaimed"
  no_permission: "&cLocked"

# Textos para variables de menú
menu-variables:
  status-enabled: "&aActivated"
  status-disabled: "&cDisabled"

# Textos para placeholders
placeholder-outputs:
  ready: "&aReady"
  claimed: "&cClaimed"
  invalid_reward: "&cInvalid Reward"

# Mensajes del sistema
no-permission: "%prefix%&cYou don't have permission to execute this command."
player-only-command: "&cThis command can only be executed by a player."
reload-success: "%prefix%&aZenRewards configuration has been reloaded!"
player-not-found: "%prefix%&cPlayer not found."
reward-reset: "%prefix%&aYou have reset the reward '&e{reward}&a' for {player}."
all-rewards-reset: "%prefix%&aYou have reset all rewards for {player}."
reward-not-found: "%prefix%&cThe reward '{reward}' does not exist."
autoclaim-summary: "%prefix%&aYou have automatically claimed &e{count} &arewards."
```
