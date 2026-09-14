import os
import re
import json
import shutil

docs_root = r"c:\Development\Webs\ZenDocs\content\docs"
docs_source = r"c:\Development\Webs\ZenDocs\DOCS"

# Standard mapping of all plugins with DOC.md
# Standard mapping of all plugins that have a DOC.md
plugins = [
    ("ZenAfkZone", "zenafkzone", "ZenAfkZone", True),
    ("ZenAuctions", "zenauctions", "ZenAuctions", True),
    ("ZenBank", "zenbank", "ZenBank", True),
    ("ZenChat", "zenchat", "ZenChat", True),
    ("ZenChatGames", "zenchatgames", "ZenChatGames", True),
    ("ZenCosmetics", "zencosmetics", "ZenCosmetics", True),
    ("ZenDiscord", "zendiscord", "ZenDiscord", True),
    ("ZenDragonEvent", "zendragonevent", "ZenDragonEvent", True),
    ("ZenDuels", "zenduels", "ZenDuels", True),
    ("ZenFairy", "zenfairy", "ZenFairy", False),
    ("ZenForges", "zenforges", "ZenForges", True),
    ("ZenPvPCore", "zenpvpcore", "ZenPvPCore", True),
    ("ZenRankups", "zenrankups", "ZenRankups", True),
]

def standardize_section_title(raw_h2):
    t = raw_h2.strip()
    
    # 1. Strip emojis and special symbols
    t = re.sub(r'^[^\w]+', '', t).strip()
    
    # 2. Strip leading numbers like "1.", "2.", "10."
    t = re.sub(r'^[0-9]+[\.\)]\s*', '', t).strip()
    
    # 3. Strip emojis again if they were behind the number
    t = re.sub(r'^[^\w]+', '', t).strip()
    
    # 4. Remove code ticks or quotes
    t = t.replace('`', '').replace('"', '').replace("'", "").strip()
    
    # 5. Remove trailing em-dash or symbols
    t = re.sub(r'[^\w\s\-\.\(\)\/\*]+$', '', t).strip()
    
    # 6. UNIFIED CANONICAL NAMES FOR STANDARD SECTIONS
    t_lower = t.lower()
    
    # Structure of files
    if any(k in t_lower for k in ['estructura de archivo', 'estructura del plugin', 'estructura del proyecto', 'estructura del directorio']):
        return "Estructura de Archivos", "estructura_de_archivos"
        
    # Main config: config.yml
    if 'config.yml' in t_lower or 'configuracion principal' in t_lower or 'configuracion general' in t_lower:
        return "Configuración (config.yml)", "config-yml"
        
    # Messages: messages.yml
    if 'messages.yml' in t_lower or ('mensajes' in t_lower and 'muerte' not in t_lower):
        return "Mensajes (messages.yml)", "messages-yml"

    # Moderation
    if 'moderation.yml' in t_lower:
        return "Auditoría de Comandos (moderation.yml)", "moderation-yml"
        
    # Commands and permissions
    if ('comando' in t_lower or 'permiso' in t_lower) and not any(k in t_lower for k in ['lista de permiso', 'auditoria', 'auditoría']):
        return "Comandos y Permisos", "comandos_y_permisos"
    if 'lista de permiso' in t_lower:
        return "Permisos", "permisos"
        
    # Placeholders
    if 'placeholder' in t_lower:
        return "Placeholders (PAPI)", "placeholders"
        
    # Database
    if 'database' in t_lower or 'base de datos' in t_lower:
        return "Base de Datos", "base_de_datos"
        
    # Menus GUI
    if 'menú' in t_lower or 'menu' in t_lower or 'guis' in t_lower or 'interfaces gui' in t_lower or 'menu.yml' in t_lower:
        return "Configuración de Menús (menus/)", "menus"
        
    # Webhooks
    if 'webhook' in t_lower:
        return "Webhooks de Discord", "webhooks"
        
    # Integrations / Dependencies
    if 'integracion' in t_lower or 'integraciones' in t_lower or 'dependencias' in t_lower or 'instalación y dependencias' in t_lower or 'requisitos y dependencias' in t_lower:
        return "Integraciones y Dependencias", "integraciones"

    # Specific common config files / features
    if 'plans.yml' in t_lower or 'planes bancarios' in t_lower:
        return "Planes (plans.yml)", "plans-yml"

    if 'zones/' in t_lower or 'zonas' in t_lower:
        return "Configuración de Zonas (zones/)", "zonas"

    if 'currencies.yml' in t_lower:
        return "Monedas e Impuestos (currencies.yml)", "currencies-yml"

    if 'filters.yml' in t_lower:
        return "Filtros y Restricciones (filters.yml)", "filters-yml"

    if 'categories.yml' in t_lower:
        return "Categorías (categories.yml)", "categories-yml"

    if 'embeds.yml' in t_lower:
        return "Avisos y Eventos (embeds.yml)", "embeds-yml"

    if 'moderation.yml' in t_lower:
        return "Auditoría de Comandos (moderation.yml)", "moderation-yml"

    if 'tops.yml' in t_lower:
        return "Leaderboards e Imágenes (tops.yml)", "tops-yml"

    if 'eye.yml' in t_lower:
        return "Ojo de Invocación (eye.yml)", "eye-yml"

    if 'loot.yml' in t_lower:
        return "Recompensas y Rangos (loot.yml)", "loot-yml"

    if 'dragons/' in t_lower or 'dragones' in t_lower:
        return "Arquetipos de Dragones (dragons/)", "dragons"

    if 'arenas.yml' in t_lower:
        return "Configuración de Arenas (arenas.yml)", "arenas-yml"

    if 'kits' in t_lower:
        return "Configuración de Kits (kits.yml)", "kits-yml"

    if 'scoreboards.yml' in t_lower:
        return "Marcadores en Pantalla (scoreboards.yml)", "scoreboards-yml"

    if 'elo_system.yml' in t_lower:
        return "Sistema ELO (elo_system.yml)", "elo_system-yml"

    if 'winstreak_system.yml' in t_lower:
        return "Rachas de Victorias (winstreak_system.yml)", "winstreak_system-yml"

    if 'bounties_system.yml' in t_lower:
        return "Sistema de Recompensas (bounties_system.yml)", "bounties_system-yml"

    if 'deathmessages/' in t_lower:
        return "Mensajes de Muerte (deathmessages/)", "deathmessages"

    if 'ranks.yml' in t_lower:
        return "Rangos (ranks.yml)", "ranks-yml"

    if 'prestige.yml' in t_lower:
        return "Prestigios (prestige.yml)", "prestige-yml"

    if 'games/' in t_lower or 'minijuegos' in t_lower:
        return "Configuración de Minijuegos (games/)", "games"

    if 'modules/' in t_lower or 'módulos del chat' in t_lower:
        return "Módulos de Chat (modules/)", "modules"

    if 'cosmetics/' in t_lower or 'creación de cosméticos' in t_lower:
        return "Cosméticos (cosmetics/)", "cosmetics"

    if 'formato de colores' in t_lower or 'formato de texto' in t_lower or 'adventure' in t_lower:
        return "Formato de Texto y MiniMessage", "formato_minimessage"

    if 'stations/' in t_lower or 'estaciones de forja' in t_lower:
        return "Estaciones de Forja (stations/)", "stations"

    if 'creations/' in t_lower or 'recetas y creaciones' in t_lower:
        return "Recetas y Creaciones (creations/)", "creations"

    if 'boosters.yml' in t_lower or 'potenciadores' in t_lower:
        return "Potenciadores (boosters.yml)", "boosters-yml"

    if 'powders.yml' in t_lower or 'polvos de minería' in t_lower:
        return "Polvos de Minería (powders.yml)", "powders-yml"

    if 'commissions.yml' in t_lower or 'comisiones' in t_lower:
        return "Comisiones e Hitos (commissions.yml)", "commissions-yml"

    if 'hotm.yml' in t_lower or 'heart of the mountain' in t_lower:
        return "Heart of the Mountain (hotm.yml)", "hotm-yml"

    if 'souls/' in t_lower or 'configuración de almas' in t_lower:
        return "Configuración de Almas (souls/)", "souls"

    if 'sistema de acciones' in t_lower:
        return "Sistema de Acciones Disponibles", "sistema_de_acciones"
        
    # Clean any angle brackets or symbols for general fallback
    clean_title = re.sub(r'<([^>]+)>', r'`<\1>`', t)
    
    # Fallback clean slug
    slug_base = t.lower()
    slug_base = slug_base.replace('.yml', '-yml').replace('.yaml', '-yaml')
    slug_base = re.sub(r'[\(\)\*\/<>]', ' ', slug_base)
    slug_base = re.sub(r'[^a-z0-9\-]', '_', slug_base)
    slug = re.sub(r'_+', '_', slug_base).strip('_')
    
    return clean_title, slug

def extract_clean_summary(content, max_len=110):
    lines = content.split('\n')
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith('```') or stripped.startswith('|') or stripped.startswith('#') or stripped.startswith('---'):
            continue
        # Replace MiniMessage/XML tags
        clean = re.sub(r'<([a-zA-Z0-9_#:]+)>', r'\1', stripped)
        clean = re.sub(r'</[a-zA-Z0-9_#:]+>', '', clean)
        clean = re.sub(r'[\*\`\_]', '', clean).strip()
        clean = clean.replace('"', "'")
        clean = re.sub(r'<[^>]*>', '', clean)
        if not clean:
            continue
        if len(clean) > max_len:
            cut = clean[:max_len]
            if ' ' in cut:
                clean = cut.rsplit(' ', 1)[0] + '...'
            else:
                clean = cut + '...'
        return clean
    return "Guía y detalles de configuración del módulo."

def fix_yaml_formatting(content):
    content = content.replace('\ufeff', '')
    
    # Fix lore quote in ZenAfkZone:
    content = re.sub(
        r'(-\s*<gray>Usa esta herramienta para seleccionar una zona\.</gray>\s*)\n\s*-\s*"\s*\n\s*-\s*',
        r'\1\n    - ',
        content
    )
    
    # Fix broken requirements line in ZenAfkZone:
    content = re.sub(r'permission:\s*"(\s*#)', r'permission: ""\1', content)
    
    # Fix indentation in ZenAfkZone YAML blocks
    fixed_lines = []
    in_yaml = False
    for line in content.split('\n'):
        if line.strip().startswith('```yaml'):
            in_yaml = True
            fixed_lines.append(line)
            continue
        elif in_yaml and line.strip().startswith('```'):
            in_yaml = False
            fixed_lines.append(line)
            continue
            
        if in_yaml:
            if re.match(r'^ [a-zA-Z0-9_\-]+:', line):
                line = '  ' + line
            elif re.match(r'^  [a-zA-Z0-9_\-]+:', line) and any(k in line for k in ['REGENERATION:', 'SATURATION:', 'enabled:', 'enter-title:', 'enter-subtitle:', 'exit-title:', 'exit-subtitle:', 'height-offset:', 'lines:', '1800:', '3600:', 'reward_diamonds:', 'reward_vip_key:', 'reward_coins:', 'chance:', 'display:', 'commands:', 'items:', 'custom-model-data:', 'enchants:', 'glowing:']):
                line = '  ' + line
            elif re.match(r'^  - ', line) and any(k in line for k in ['Diamante AFK', 'Obtenido por', '★ ZONA AFK', 'Jugadores descansando', 'Ciclo de recompensa', 'eco give', 'crate give', 'broadcast']):
                line = '    ' + line
        fixed_lines.append(line)
        
    return '\n'.join(fixed_lines)

# Allowed MDX components
ALLOWED_TAGS = {"Callout", "Card", "Cards", "Step", "Steps", "Tab", "Tabs"}

def sanitize_mdx_outside_code(text):
    lines = text.split('\n')
    new_lines = []
    in_code = False
    for line in lines:
        if line.strip().startswith('```'):
            in_code = not in_code
            new_lines.append(line)
            continue
        if in_code:
            new_lines.append(line)
        else:
            parts = line.split('`')
            for idx in range(0, len(parts), 2):
                def repl(m):
                    full_match = m.group(0)
                    tag = m.group(1)
                    if tag in ALLOWED_TAGS:
                        return full_match
                    return f"`{full_match}`"
                parts[idx] = re.sub(r'</?([a-zA-Z_][a-zA-Z0-9_\-:#]*)[^>]*>', repl, parts[idx])
            new_lines.append('`'.join(parts))
    return '\n'.join(new_lines)

def process_plugin(doc_path, target_folder, display_name, is_new):
    with open(doc_path, 'r', encoding='utf-8') as f:
        full_text = f.read()
        
    full_text = fix_yaml_formatting(full_text)
    
    pattern = re.compile(r'^##\s+(.+)$', re.MULTILINE)
    matches = list(pattern.finditer(full_text))
    
    intro_chunk = full_text[:matches[0].start()].strip() if matches else full_text.strip()
    
    sections = []
    seen_slugs = set()
    
    for i, m in enumerate(matches):
        raw_h2 = m.group(1).strip()
        start = m.end()
        end = matches[i+1].start() if i+1 < len(matches) else len(full_text)
        sec_content = full_text[start:end].strip()
        
        if any(k in raw_h2.lower() for k in ['tabla de contenidos', 'indice', 'índice']):
            continue
            
        std_title, slug = standardize_section_title(raw_h2)
        if not slug:
            slug = f"seccion_{i+1}"
        if slug in seen_slugs:
            slug = f"{slug}_{i+1}"
        seen_slugs.add(slug)
        
        sec_content = re.sub(r'\n---\s*$', '', sec_content).strip()
        sec_content = sanitize_mdx_outside_code(sec_content)
        
        # Clean title for MDX heading (no unescaped tags)
        h1_title = std_title.replace('<', '').replace('>', '')
        
        sections.append({
            'title': std_title,
            'h1_title': h1_title,
            'slug': slug,
            'content': sec_content,
            'summary': extract_clean_summary(sec_content)
        })
        
    target_dir = os.path.join(docs_root, target_folder)
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    os.makedirs(target_dir, exist_ok=True)
    
    clean_intro_lines = []
    for line in intro_chunk.split('\n'):
        if line.startswith('# '):
            continue
        clean_intro_lines.append(line)
    clean_intro = '\n'.join(clean_intro_lines).strip()
    clean_intro = re.sub(r'\n---\s*$', '', clean_intro).strip()
    clean_intro = sanitize_mdx_outside_code(clean_intro)
    
    # 1. index.mdx
    cards_text = ""
    for sec in sections:
        card_title = sec["title"].replace('"', "'").replace('<', '').replace('>', '')
        card_desc = sec["summary"].replace('"', "'")
        cards_text += f'  <Card title="{card_title}" href="/docs/{target_folder}/{sec["slug"]}" description="{card_desc}" />\n'
        
    index_mdx = f"""---
title: "{display_name}"
description: "Documentación oficial, guías de configuración y arquitectura de {display_name}."
---

import {{ Card, Cards }} from 'fumadocs-ui/components/card';
import {{ Callout }} from 'fumadocs-ui/components/callout';

# {display_name}

{clean_intro}

---

## 📑 Secciones de la Documentación

<Cards>
{cards_text}</Cards>
"""
    with open(os.path.join(target_dir, "index.mdx"), "w", encoding="utf-8") as f:
        f.write(index_mdx)
        
    # 2. Individual section pages
    pages_list = ["index"]
    for sec in sections:
        pages_list.append(sec['slug'])
        page_title_frontmatter = sec['title'].replace('"', "'").replace('<', '').replace('>', '')
        summary_safe = sec['summary'].replace('"', "'")
        page_mdx = f"""---
title: "{page_title_frontmatter}"
description: "{summary_safe}"
---

import {{ Callout }} from 'fumadocs-ui/components/callout';

# {sec['h1_title']}

---

{sec['content']}
"""
        with open(os.path.join(target_dir, f"{sec['slug']}.mdx"), "w", encoding="utf-8") as f:
            f.write(page_mdx)
            
    # 3. meta.json
    title_with_badge = f"{display_name} (New)" if is_new else display_name
    meta_json = {
        "title": title_with_badge,
        "pages": pages_list
    }
    with open(os.path.join(target_dir, "meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta_json, f, indent=2, ensure_ascii=False)
        
    print(f"Processed {display_name}: {len(sections)} standardized sections.")

def main():
    for folder, target, display_name, is_new in plugins:
        doc_path = os.path.join(docs_source, folder, "DOC.md")
        if os.path.exists(doc_path):
            process_plugin(doc_path, target, display_name, is_new)
        else:
            print(f"File not found: {doc_path}")

    # Check for ZenDiscord/API.md to include developer API documentation
    api_path = os.path.join(docs_source, "ZenDiscord", "API.md")
    zendiscord_target = os.path.join(docs_root, "zendiscord")
    if os.path.exists(api_path) and os.path.exists(zendiscord_target):
        with open(api_path, 'r', encoding='utf-8') as f:
            api_text = f.read()
        api_text = sanitize_mdx_outside_code(api_text)
        
        # Remove top H1 if present
        api_clean_lines = []
        for line in api_text.split('\n'):
            if line.startswith('# '):
                continue
            api_clean_lines.append(line)
        api_body = '\n'.join(api_clean_lines).strip()
        api_body = re.sub(r'\n---\s*$', '', api_body).strip()
        
        api_mdx = f"""---
title: "API para Desarrolladores"
description: "Guía completa para desarrolladores y referencia de la API de ZenDiscord."
---

import {{ Callout }} from 'fumadocs-ui/components/callout';

# API para Desarrolladores

---

{api_body}
"""
        with open(os.path.join(zendiscord_target, "api.mdx"), "w", encoding="utf-8") as f:
            f.write(api_mdx)
            
        # Add card to zendiscord/index.mdx
        index_file = os.path.join(zendiscord_target, "index.mdx")
        with open(index_file, "r", encoding="utf-8") as f:
            index_content = f.read()
        if 'href="/docs/zendiscord/api"' not in index_content:
            new_card = '  <Card title="API para Desarrolladores" href="/docs/zendiscord/api" description="Guía completa para desarrolladores y referencia de la API de ZenDiscord." />\n</Cards>'
            index_content = index_content.replace('</Cards>', new_card)
            with open(index_file, "w", encoding="utf-8") as f:
                f.write(index_content)
                
        # Add to zendiscord/meta.json
        meta_file = os.path.join(zendiscord_target, "meta.json")
        with open(meta_file, "r", encoding="utf-8") as f:
            meta_data = json.load(f)
        if "api" not in meta_data.get("pages", []):
            meta_data["pages"].append("api")
            with open(meta_file, "w", encoding="utf-8") as f:
                json.dump(meta_data, f, indent=2, ensure_ascii=False)
        print("Processed ZenDiscord API.md as 'api.mdx'")

    # Verify root meta.json
    root_meta_path = os.path.join(docs_root, "meta.json")
    with open(root_meta_path, "r", encoding="utf-8") as f:
        root_meta = json.load(f)
        
    # Remove any deleted plugins if still present
    for bad in ["zenhub", "zenwardrobe", "zenprofiles"]:
        if bad in root_meta.get("pages", []):
            root_meta["pages"].remove(bad)
            
    with open(root_meta_path, "w", encoding="utf-8") as f:
        json.dump(root_meta, f, indent=2, ensure_ascii=False)

    print("Standardization of titles completed.")

if __name__ == "__main__":
    main()
