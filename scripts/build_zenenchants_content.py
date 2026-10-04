import os
import re
import json

CONTENT_MD_PATH = r"c:\Development\Webs\ZenDocs\DOCS\ZenEnchants\CONTENT.md"
BASE_TARGET = r"c:\Development\Webs\ZenDocs\content\docs\zenenchants"

def sanitize_mdx(text):
    # Escape standalone unescaped angle brackets outside backticks / code blocks
    lines = text.split('\n')
    in_code = False
    new_lines = []
    for line in lines:
        if line.strip().startswith('```'):
            in_code = not in_code
            new_lines.append(line)
            continue
        if in_code:
            new_lines.append(line)
            continue
        
        # Replace unescaped HTML/XML-like brackets if not valid mdx or inside inline code
        # e.g., <num>, <POTION>, <world1>, <rg1>, <0-15>, <ticks>, <arg_name>, <value>, <condition_id>
        parts = line.split('`')
        for i in range(0, len(parts), 2): # outside backticks
            parts[i] = re.sub(r'<([a-zA-Z0-9_\-#:]+)>', r'`<\1>`', parts[i])
        line = '`'.join(parts)
        new_lines.append(line)
    return '\n'.join(new_lines)

with open(CONTENT_MD_PATH, 'r', encoding='utf-8') as f:
    raw_content = f.read()

# 1. Parse Effects
# In CONTENT.md:
# ## ⚡ Efectos (Effects) [185] ... until ## 🎯 Triggers (Disparadores)
effects_section_match = re.search(r'## ⚡ Efectos \(Effects\).*?\n(.*?)## 🎯 Triggers \(Disparadores\)', raw_content, re.DOTALL)
effects_raw = effects_section_match.group(1) if effects_section_match else ""

# Extract each effect: starts with `### ` or `#### `
# e.g. ### `add_damage` or ### `knockback` / `launch` / `pull`
effect_blocks = re.split(r'\n###+ ', '\n' + effects_raw)
effects_data = []

for block in effect_blocks[1:]:
    lines = block.split('\n')
    header_line = lines[0].strip()
    body = '\n'.join(lines[1:]).strip()
    
    # Header could be `add_damage` or `send_message` / `actionbar` / `title`
    # Extract identifiers enclosed in backticks
    ids = [x.strip() for x in re.findall(r'`([^`]+)`', header_line) if x.strip()]
    if not ids:
        continue
    
    main_id = ids[0]
    aliases = ids
    
    # Extract short description from first non-empty line of body
    desc = ""
    for l in lines[1:]:
        l_str = l.strip()
        if l_str and not l_str.startswith('-') and not l_str.startswith('|') and not l_str.startswith('```') and not l_str.startswith('#'):
            desc = l_str
            break
    if not desc:
        desc = f"Efecto {main_id} del motor de ZenEnchants."
        
    # Categories
    cat_match = re.search(r'- \*\*Categorías:\*\* (.*?)$', block, re.MULTILINE)
    categories = cat_match.group(1).strip() if cat_match else "effects"
    
    # Clean description for card
    card_desc = desc
    card_desc = re.sub(r'[\*\_]', '', card_desc).replace('"', "'")
    if len(card_desc) > 90:
        card_desc = card_desc[:87] + '...'
        
    effects_data.append({
        'id': main_id,
        'aliases': aliases,
        'categories': categories,
        'desc': desc,
        'card_desc': card_desc,
        'body': sanitize_mdx(block)
    })

print(f"Extracted {len(effects_data)} effects.")

# 2. Parse Triggers
# ## 🎯 Triggers (Disparadores) ... until ## 🔍 Condiciones (Conditions)
triggers_section_match = re.search(r'## 🎯 Triggers \(Disparadores\)(.*?)## 🔍 Condiciones \(Conditions\)', raw_content, re.DOTALL)
triggers_raw = triggers_section_match.group(1) if triggers_section_match else ""

# Extract table rows: | `trigger_name` | `CONTEXT` | Description |
# Also find subcategory headers: ### Triggers de ...
trigger_subcats = re.split(r'\n### ', '\n' + triggers_raw)
triggers_data = []

for subcat in trigger_subcats[1:]:
    lines = subcat.split('\n')
    subcat_name = lines[0].replace('Triggers de ', '').strip()
    for line in lines[1:]:
        line = line.strip()
        if not line.startswith('|') or 'Trigger' in line or ':---' in line:
            continue
        parts = [p.strip() for p in line.split('|')]
        # parts: ['', '`trigger`', 'context', 'desc', '']
        if len(parts) >= 4:
            trig_col = parts[1]
            ctx_col = parts[2]
            desc_col = parts[3]
            
            # Extract name(s)
            trig_names = re.findall(r'`([^`]+)`', trig_col)
            if not trig_names:
                continue
            main_trig = trig_names[0]
            
            clean_desc = desc_col.replace('"', "'")
            card_desc = clean_desc
            if len(card_desc) > 90:
                card_desc = card_desc[:87] + '...'
                
            triggers_data.append({
                'id': main_trig,
                'aliases': trig_names,
                'category': subcat_name,
                'context': ctx_col,
                'desc': desc_col,
                'card_desc': card_desc
            })

print(f"Extracted {len(triggers_data)} triggers.")

# 3. Parse Conditions
# ## 🔍 Condiciones (Conditions) ... until ## 🔀 Mutadores (Mutators)
conds_section_match = re.search(r'## 🔍 Condiciones \(Conditions\)(.*?)## 🔀 Mutadores \(Mutators\)', raw_content, re.DOTALL)
conds_raw = conds_section_match.group(1) if conds_section_match else ""

cond_subcats = re.split(r'\n### ', '\n' + conds_raw)
conditions_data = []

for subcat in cond_subcats[1:]:
    lines = subcat.split('\n')
    subcat_name = lines[0].replace('Condiciones de ', '').strip()
    if 'Formato de Configuración' in subcat_name:
        continue
    for line in lines[1:]:
        line = line.strip()
        if not line.startswith('|') or 'Condición ID' in line or ':---' in line:
            continue
        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 4:
            cond_col = parts[1]
            args_col = parts[2]
            desc_col = parts[3]
            
            cond_names = re.findall(r'`([^`]+)`', cond_col)
            if not cond_names:
                continue
            main_cond = cond_names[0]
            
            clean_desc = desc_col.replace('"', "'")
            card_desc = clean_desc
            if len(card_desc) > 90:
                card_desc = card_desc[:87] + '...'
                
            conditions_data.append({
                'id': main_cond,
                'aliases': cond_names,
                'category': subcat_name,
                'args': sanitize_mdx(args_col),
                'desc': sanitize_mdx(desc_col),
                'card_desc': sanitize_mdx(card_desc)
            })

print(f"Extracted {len(conditions_data)} conditions.")

# 4. Generate Effects files
effects_dir = os.path.join(BASE_TARGET, "effects")
os.makedirs(effects_dir, exist_ok=True)

# effects meta.json
effect_slugs = ["index"] + [e['id'] for e in effects_data]
with open(os.path.join(effects_dir, "meta.json"), "w", encoding="utf-8") as f:
    json.dump({"title": "Efectos (Effects)", "pages": effect_slugs}, f, indent=2, ensure_ascii=False)

# effects index.mdx
eff_cards = "\n".join([f'  <Card title="{e["id"]}" href="/docs/zenenchants/effects/{e["id"]}" description="{e["card_desc"]}" />' for e in effects_data])
eff_index_content = f"""---
title: "Efectos (Effects)"
description: "Catálogo completo de efectos ejecutables individuales estilo eco / libreforge para ZenEnchants."
---

import {{ Card, Cards }} from 'fumadocs-ui/components/card';
import {{ Callout }} from 'fumadocs-ui/components/callout';

Catálogo completo de **Effects** para ZenEnchants estilo eco / libreforge, estructurado con páginas individuales por cada elemento para consulta detallada.

## 📑 Lista de Efectos ({len(effects_data)})

<Cards>
{eff_cards}
</Cards>
"""
with open(os.path.join(effects_dir, "index.mdx"), "w", encoding="utf-8") as f:
    f.write(eff_index_content)

for e in effects_data:
    # Build individual effect page
    alias_str = " / ".join([f"`{a}`" for a in e['aliases']])
    body_clean = e['body']
    # remove the first header line if already present in body
    lines = body_clean.split('\n')
    if lines[0].strip().startswith('`'):
        body_clean = '\n'.join(lines[1:]).strip()
    
    eff_page = f"""---
title: "{e['id']}"
description: "{e['card_desc']}"
---

import {{ Callout }} from 'fumadocs-ui/components/callout';

# `{e['id']}`

* **Categorías:** {e['categories']}  
* **Identificador / Alias:** {alias_str}

---

{body_clean}
"""
    with open(os.path.join(effects_dir, f"{e['id']}.mdx"), "w", encoding="utf-8") as f:
        f.write(eff_page)

# 5. Generate Triggers files
triggers_dir = os.path.join(BASE_TARGET, "triggers")
os.makedirs(triggers_dir, exist_ok=True)

trigger_slugs = ["index"] + [t['id'] for t in triggers_data]
with open(os.path.join(triggers_dir, "meta.json"), "w", encoding="utf-8") as f:
    json.dump({"title": "Triggers (Disparadores)", "pages": trigger_slugs}, f, indent=2, ensure_ascii=False)

trig_cards = "\n".join([f'  <Card title="{t["id"]}" href="/docs/zenenchants/triggers/{t["id"]}" description="{t["card_desc"]}" />' for t in triggers_data])
trig_index_content = f"""---
title: "Triggers (Disparadores)"
description: "Catálogo completo de disparadores y eventos de activación para ZenEnchants."
---

import {{ Card, Cards }} from 'fumadocs-ui/components/card';
import {{ Callout }} from 'fumadocs-ui/components/callout';

Catálogo completo de **Triggers** para ZenEnchants estilo eco / libreforge, estructurado con páginas individuales por cada elemento para consulta detallada.

## 📑 Lista de Triggers ({len(triggers_data)})

<Cards>
{trig_cards}
</Cards>
"""
with open(os.path.join(triggers_dir, "index.mdx"), "w", encoding="utf-8") as f:
    f.write(trig_index_content)

for t in triggers_data:
    alias_str = " / ".join([f"`{a}`" for a in t['aliases']])
    trig_page = f"""---
title: "{t['id']}"
description: "{t['card_desc']}"
---

import {{ Callout }} from 'fumadocs-ui/components/callout';

# `{t['id']}`

* **Categoría:** `{t['category']}`  
* **Identificador / Alias:** {alias_str}  
* **Contexto Inyectado:** {t['context']}

---

{t['desc']}

### Ejemplo de Configuración:
```yaml
effects:
  - id: play_sound
    args:
      sound: ENTITY_EXPERIENCE_ORB_PICKUP
      volume: 1.0
      pitch: 1.0
    triggers:
      - {t['id']}
```
"""
    with open(os.path.join(triggers_dir, f"{t['id']}.mdx"), "w", encoding="utf-8") as f:
        f.write(trig_page)

# 6. Generate Conditions files
conds_dir = os.path.join(BASE_TARGET, "conditions")
os.makedirs(conds_dir, exist_ok=True)

cond_slugs = ["index"] + [c['id'] for c in conditions_data]
with open(os.path.join(conds_dir, "meta.json"), "w", encoding="utf-8") as f:
    json.dump({"title": "Condiciones (Conditions)", "pages": cond_slugs}, f, indent=2, ensure_ascii=False)

cond_cards = "\n".join([f'  <Card title="{c["id"]}" href="/docs/zenenchants/conditions/{c["id"]}" description="{c["card_desc"]}" />' for c in conditions_data])
cond_index_content = f"""---
title: "Condiciones (Conditions)"
description: "Catálogo completo de condiciones lógicas y restricciones para ZenEnchants."
---

import {{ Card, Cards }} from 'fumadocs-ui/components/card';
import {{ Callout }} from 'fumadocs-ui/components/callout';

Catálogo completo de **Conditions** para ZenEnchants estilo eco / libreforge, estructurado con páginas individuales por cada elemento para consulta detallada.

## 📑 Lista de Condiciones ({len(conditions_data)})

<Cards>
{cond_cards}
</Cards>
"""
with open(os.path.join(conds_dir, "index.mdx"), "w", encoding="utf-8") as f:
    f.write(cond_index_content)

for c in conditions_data:
    alias_str = " / ".join([f"`{a}`" for a in c['aliases']])
    args_display = c['args'] if c['args'] else "*(Ninguno)*"
    cond_page = f"""---
title: "{c['id']}"
description: "{c['card_desc']}"
---

import {{ Callout }} from 'fumadocs-ui/components/callout';

# `{c['id']}`

* **Categoría:** `{c['category']}`  
* **Identificador / Alias:** {alias_str}  
* **Argumentos Soportados:** {args_display}

---

{c['desc']}

### Estructura Canónica:
```yaml
conditions:
  - id: {c['id']}
    args:
      # {c['args']}
    not: false
```
"""
    with open(os.path.join(conds_dir, f"{c['id']}.mdx"), "w", encoding="utf-8") as f:
        f.write(cond_page)

# 7. Generate filters-and-mutators.mdx
# Extract Mutators and Filters sections from raw_content
mut_match = re.search(r'## 🔀 Mutadores \(Mutators\)(.*?)## 🎯 Filtros \(Filters\)', raw_content, re.DOTALL)
mut_text = mut_match.group(1).strip() if mut_match else ""

filt_match = re.search(r'## 🎯 Filtros \(Filters\)(.*?)## ⚙️ Argumentos Opcionales Comunes', raw_content, re.DOTALL)
filt_text = filt_match.group(1).strip() if filt_match else ""

filters_and_mutators_content = f"""---
title: "Filtros y Mutadores"
description: "Transforma parámetros de contexto y filtra entidades, bloques y orígenes de daño en ZenEnchants."
---

import {{ Callout }} from 'fumadocs-ui/components/callout';

Los **Filtros (Filters)** y **Mutadores (Mutators)** permiten acotar y alterar con exactitud los parámetros del evento antes de que se despachen los efectos en ZenEnchants.

---

## 🔀 Mutadores (Mutators)

{sanitize_mdx(mut_text)}

---

## 🎯 Filtros (Filters)

{sanitize_mdx(filt_text)}
"""

with open(os.path.join(BASE_TARGET, "filters-and-mutators.mdx"), "w", encoding="utf-8") as f:
    f.write(filters_and_mutators_content)

# 8. Generate placeholders.mdx (including common optional arguments & placeholders)
opt_match = re.search(r'## ⚙️ Argumentos Opcionales Comunes(.*?)## 🧮 Placeholders de Contexto Dinámico', raw_content, re.DOTALL)
opt_text = opt_match.group(1).strip() if opt_match else ""

placeholders_match = re.search(r'## 🧮 Placeholders de Contexto Dinámico(.*)$', raw_content, re.DOTALL)
placeholders_text = placeholders_match.group(1).strip() if placeholders_match else ""

placeholders_content = f"""---
title: "Placeholders y Argumentos Comunes"
description: "Variables de contexto dinámico, expresiones matemáticas y modificadores comunes de efectos."
---

import {{ Callout }} from 'fumadocs-ui/components/callout';

ZenEnchants proporciona soporte nativo para placeholders dinámicos de evento y modificadores de ejecución universal (`chance`, `cooldown`, `delay`, `repeat`, etc.).

---

## ⚙️ Argumentos Opcionales Comunes

{sanitize_mdx(opt_text)}

---

## 🧮 Placeholders de Contexto Dinámico

{sanitize_mdx(placeholders_text)}
"""

with open(os.path.join(BASE_TARGET, "placeholders.mdx"), "w", encoding="utf-8") as f:
    f.write(placeholders_content)

# 9. Update root meta.json for zenenchants
root_meta = {
  "title": "ZenEnchants (New)",
  "pages": [
    "index",
    "requisitos_del_sistema",
    "instalacion",
    "comandos_y_permisos",
    "estructura_de_archivos",
    "config-yml",
    "targets-yml",
    "items-yml",
    "messages-yml",
    "rarities-yml",
    "creacion_encantamientos",
    "menus",
    "mecanicas_especiales",
    "effects",
    "triggers",
    "conditions",
    "filters-and-mutators",
    "placeholders",
    "api"
  ]
}

with open(os.path.join(BASE_TARGET, "meta.json"), "w", encoding="utf-8") as f:
    json.dump(root_meta, f, indent=2, ensure_ascii=False)

# 10. Update zenenchants/index.mdx to remove catalogo_motor and link to sections
zenenchants_index = f"""---
title: "ZenEnchants"
description: "Documentación oficial, guías de configuración y arquitectura de ZenEnchants."
---

import {{ Card, Cards }} from 'fumadocs-ui/components/card';
import {{ Callout }} from 'fumadocs-ui/components/callout';

# ZenEnchants

Bienvenido a la documentación oficial de **ZenEnchants**, un plugin avanzado de encantamientos personalizados desarrollado para **Paper 1.21+** utilizando la API moderna de Adventure (MiniMessage), arquitectura declarativa basada en Libreforge (Triggers, Conditions, Effects, Mutators) y compatibilidad total con servidores modernos.

---

## 📑 Secciones de la Documentación

<Cards>
  <Card title="Requisitos del Sistema" href="/docs/zenenchants/requisitos_del_sistema" description="- Servidor: Paper, Purpur o forks derivados compatibles con Minecraft 1.21.x en adelante." />
  <Card title="Instalación" href="/docs/zenenchants/instalacion" description="1. Descarga el archivo compilado ZenEnchants-1.0.0.jar." />
  <Card title="Comandos y Permisos" href="/docs/zenenchants/comandos_y_permisos" description="Guía y detalles de configuración del módulo." />
  <Card title="Estructura de Archivos" href="/docs/zenenchants/estructura_de_archivos" description="plugins/ZenEnchants/" />
  <Card title="Configuración (config.yml)" href="/docs/zenenchants/config-yml" description="El archivo config.yml controla el comportamiento de los encantamientos en el mundo:" />
  <Card title="Categorías y Objetivos (targets.yml)" href="/docs/zenenchants/targets-yml" description="Categoriza sobre qué objetos se aplican encantamientos y tags de equipo." />
  <Card title="Ítems Especiales (items.yml)" href="/docs/zenenchants/items-yml" description="Personaliza el aspecto, materiales y textos de libros, polvos mágicos y pergaminos." />
  <Card title="Mensajes (messages.yml)" href="/docs/zenenchants/messages-yml" description="Todos los textos soportan formato moderno MiniMessage y degradados." />
  <Card title="Sistema de Rarezas (rarities.yml)" href="/docs/zenenchants/rarities-yml" description="Define la jerarquía, colores y peso de aparición de cada rareza:" />
  <Card title="Creación de Encantamientos" href="/docs/zenenchants/creacion_encantamientos" description="Para crear un nuevo encantamiento, simplemente añade un archivo .yml en plugins/ZenEnchants/enchants/..." />
  <Card title="Configuración de Menús (menus/)" href="/docs/zenenchants/menus" description="El menú interactivo de encantamientos y enciclopedia." />
  <Card title="Mecánicas Especiales y Mystery Enchants" href="/docs/zenenchants/mecanicas_especiales" description="Tasas de éxito y destrucción, orbes, polvo arcano y pergaminos." />
  <Card title="Effects ({len(effects_data)})" href="/docs/zenenchants/effects" description="Catálogo completo de efectos ejecutables con páginas individuales por slug." />
  <Card title="Triggers ({len(triggers_data)})" href="/docs/zenenchants/triggers" description="Catálogo completo de disparadores y eventos con páginas individuales por slug." />
  <Card title="Conditions ({len(conditions_data)})" href="/docs/zenenchants/conditions" description="Catálogo completo de condiciones lógicas con páginas individuales por slug." />
  <Card title="Filtros y Mutadores" href="/docs/zenenchants/filters-and-mutators" description="Especificaciones de filtrado de entidades/bloques y mutadores matemáticos." />
  <Card title="Placeholders y Argumentos" href="/docs/zenenchants/placeholders" description="Placeholders dinámicos de evento y argumentos universales." />
  <Card title="API para Desarrolladores" href="/docs/zenenchants/api" description="Guía completa para desarrolladores y referencia de la API de ZenEnchants." />
</Cards>
"""

with open(os.path.join(BASE_TARGET, "index.mdx"), "w", encoding="utf-8") as f:
    f.write(zenenchants_index)

# Delete obsolete catalogo_motor.mdx if exists
cat_motor = os.path.join(BASE_TARGET, "catalogo_motor.mdx")
if os.path.exists(cat_motor):
    os.remove(cat_motor)
    print("Deleted obsolete catalogo_motor.mdx")

print("ZenEnchants architecture generation complete!")
