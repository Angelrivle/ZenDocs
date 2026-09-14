import os
import re
import json
import shutil

docs_root = r"c:\Development\Webs\ZenDocs\content\docs"
docs_source = r"c:\Development\Webs\ZenDocs\DOCS"

plugins = [
    ("ZenAfkZone", "zenafkzone", "ZenAfkZone", True),
    ("ZenAuctions", "zenauctions", "ZenAuctions", True),
    ("ZenChat", "zenchat", "ZenChat", True),
    ("ZenChatGames", "zenchatgames", "ZenChatGames", True),
    ("ZenCosmetics", "zencosmetics", "ZenCosmetics", True),
    ("ZenDuels", "zenduels", "ZenDuels", True),
    ("ZenPvPCore", "zenpvpcore", "ZenPvPCore", True),
    ("ZenRankups", "zenrankups", "ZenRankups", True),
]

def clean_title_and_slug(raw_h2):
    t = raw_h2.strip()
    
    # Strip any leading non-alphanumeric chars (emojis, icons)
    t = re.sub(r'^[^\w]+', '', t).strip()
    
    # Strip leading numbers like "1.", "2.", "10."
    t = re.sub(r'^[0-9]+[\.\)]\s*', '', t).strip()
    
    # Strip non-alphanumeric again in case emojis were behind numbers
    t = re.sub(r'^[^\w]+', '', t).strip()
    
    # Strip trailing punctuation / emojis
    t = re.sub(r'[^\w\s\-\.\(\)\/\*]+$', '', t).strip()
    
    # Slug generation
    slug_base = t.lower()
    slug_base = slug_base.replace('.yml', '-yml').replace('.yaml', '-yaml')
    slug_base = slug_base.replace('.sqlite', '-sqlite').replace('.db', '-db')
    slug_base = re.sub(r'[\(\)\*\/<>]', ' ', slug_base)
    slug_base = re.sub(r'[^a-z0-9\-]', '_', slug_base)
    slug = re.sub(r'_+', '_', slug_base).strip('_')
    
    return t, slug

def extract_clean_summary(content, max_len=110):
    lines = content.split('\n')
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith('```') or stripped.startswith('|') or stripped.startswith('#') or stripped.startswith('---'):
            continue
        # Replace MiniMessage/XML tags by their inner or raw text (e.g. `<gradient:#HEX:#HEX>` -> `gradient`)
        clean = re.sub(r'<([a-zA-Z0-9_#:]+)>', r'\1', stripped)
        clean = re.sub(r'</[a-zA-Z0-9_#:]+>', '', clean)
        clean = re.sub(r'[\*\`\_]', '', clean).strip()
        clean = clean.replace('"', "'")
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
    
    # 1. Fix unclosed lore quote in ZenAfkZone:
    content = re.sub(
        r'(-\s*<gray>Usa esta herramienta para seleccionar una zona\.</gray>\s*)\n\s*-\s*"\s*\n\s*-\s*',
        r'\1\n    - ',
        content
    )
    
    # 2. Fix broken requirements line in ZenAfkZone:
    content = re.sub(r'permission:\s*"(\s*#)', r'permission: ""\1', content)
    
    # 3. Fix 1-space indentation in ZenAfkZone zones YAML block
    # Lines that start with a single space followed by a letter/key should have 2 or 4 spaces
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
            # Fix single space indentation on properties
            # e.g. " min-level: 0" -> "  min-level: 0"
            if re.match(r'^ [a-zA-Z0-9_\-]+:', line):
                # Check what level it belongs to
                line = '  ' + line
            elif re.match(r'^  [a-zA-Z0-9_\-]+:', line) and any(k in line for k in ['REGENERATION:', 'SATURATION:', 'enabled:', 'enter-title:', 'enter-subtitle:', 'exit-title:', 'exit-subtitle:', 'height-offset:', 'lines:', '1800:', '3600:', 'reward_diamonds:', 'reward_vip_key:', 'reward_coins:', 'chance:', 'display:', 'commands:', 'items:', 'custom-model-data:', 'enchants:', 'glowing:']):
                # Needs 4 spaces
                line = '  ' + line
            elif re.match(r'^  - ', line) and any(k in line for k in ['Diamante AFK', 'Obtenido por', '★ ZONA AFK', 'Jugadores descansando', 'Ciclo de recompensa', 'eco give', 'crate give', 'broadcast']):
                line = '    ' + line
        fixed_lines.append(line)
        
    return '\n'.join(fixed_lines)

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
            
        clean_title, slug = clean_title_and_slug(raw_h2)
        if not slug:
            slug = f"seccion_{i+1}"
        if slug in seen_slugs:
            slug = f"{slug}_{i+1}"
        seen_slugs.add(slug)
        
        sec_content = re.sub(r'\n---\s*$', '', sec_content).strip()
        
        sections.append({
            'title': clean_title,
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
    
    # 1. index.mdx
    cards_text = ""
    for sec in sections:
        cards_text += f'  <Card title="{sec["title"]}" href="/docs/{target_folder}/{sec["slug"]}" description="{sec["summary"]}" />\n'
        
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
        page_mdx = f"""---
title: "{sec['title']}"
description: "{sec['summary']}"
---

import {{ Callout }} from 'fumadocs-ui/components/callout';

# {sec['title']}

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
        
    print(f"Processed {display_name}: {len(sections)} sections generated without numbers.")

for src, target, name, is_new in plugins:
    p = os.path.join(docs_source, src, "DOC.md")
    if os.path.exists(p):
        process_plugin(p, target, name, is_new)
    else:
        print(f"File not found: {p}")

print("Complete standard rebuild finished.")
