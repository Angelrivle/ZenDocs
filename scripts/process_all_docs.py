import os
import re
import json
import shutil

docs_root = r"c:\Development\Webs\ZenDocs\content\docs"
docs_source = r"c:\Development\Webs\ZenDocs\DOCS"

# Plugin mapping: (DOCS_folder, docs_target_folder, plugin_display_name, has_new_badge)
plugins_to_build = [
    ("ZenAfkZone", "zenafkzone", "ZenAfkZone", True),
    ("ZenAuctions", "zenauctions", "ZenAuctions", True),
    ("ZenChat", "zenchat", "ZenChat", True),
    ("ZenChatGames", "zenchatgames", "ZenChatGames", True),
    ("ZenCosmetics", "zencosmetics", "ZenCosmetics", True),
    ("ZenDuels", "zenduels", "ZenDuels", True),
    ("ZenPvPCore", "zenpvpcore", "ZenPvPCore", True),
]

def clean_slug(title):
    # remove leading numbers like "1.", "2."
    clean = re.sub(r'^[0-9\.\s\-\–\—]+', '', title).strip()
    # remove emojis and special chars
    clean = re.sub(r'[^\w\s\-\(\)\/\.]', '', clean).strip()
    # take filename or main words
    slug = clean.lower()
    # replace dots like config.yml -> config_yml
    slug = slug.replace('.yml', '-yml').replace('.yaml', '-yaml')
    slug = re.sub(r'[^a-z0-9\-]', '_', slug)
    slug = re.sub(r'_+', '_', slug).strip('_')
    return slug

def parse_doc(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Split by ## headers
    pattern = re.compile(r'^##\s+(.+)$', re.MULTILINE)
    matches = list(pattern.finditer(text))
    
    sections = []
    seen_slugs = set()
    
    # Intro content before first ##
    intro_chunk = ""
    if matches:
        intro_chunk = text[:matches[0].start()].strip()
    else:
        intro_chunk = text.strip()
        
    for i, m in enumerate(matches):
        raw_title = m.group(1).strip()
        start = m.end()
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        chunk = text[start:end].strip()
        
        # Skip table of contents
        if 'tabla de contenidos' in raw_title.lower() or 'indice' in raw_title.lower() or 'índice' in raw_title.lower():
            continue
            
        slug = clean_slug(raw_title)
        if not slug:
            slug = f"seccion_{i+1}"
        if slug in seen_slugs:
            slug = f"{slug}_{i+1}"
        seen_slugs.add(slug)
        
        # Clean title for display
        clean_t = re.sub(r'^[0-9\.\s\-\–\—]+', '', raw_title).strip()
        clean_t = re.sub(r'[^\w\s\-\.\(\)\/]', '', clean_t).strip()
        
        sections.append({
            'raw_title': raw_title,
            'clean_title': clean_t if clean_t else raw_title,
            'slug': slug,
            'content': chunk
        })
        
    return intro_chunk, sections

for src_folder, target_name, display_name, is_new in plugins_to_build:
    doc_file = os.path.join(docs_source, src_folder, "DOC.md")
    if not os.path.exists(doc_file):
        print(f"Skipping {src_folder}: DOC.md not found.")
        continue
        
    intro_chunk, sections = parse_doc(doc_file)
    target_dir = os.path.join(docs_root, target_name)
    
    # Clean previous contents of target_dir
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    os.makedirs(target_dir, exist_ok=True)
    
    title_badge = f"{display_name} (New)" if is_new else display_name
    
    # 1. Create index.mdx
    cards_text = ""
    for sec in sections:
        first_line = sec['content'].split('\n')[0].replace('"', "'") if sec['content'] else ''
        if len(first_line) > 90:
            first_line = first_line[:87] + '...'
        cards_text += f'  <Card title="{sec["clean_title"]}" href="/docs/{target_name}/{sec["slug"]}" description="{first_line}" />\n'
        
    # Clean intro lines
    clean_intro_lines = []
    for line in intro_chunk.split('\n'):
        if line.startswith('# '):
            continue
        clean_intro_lines.append(line)
    clean_intro = '\n'.join(clean_intro_lines).strip()
    
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
        
    # 2. Create subpages for each section
    pages_list = ["index"]
    for sec in sections:
        pages_list.append(sec['slug'])
        first_line = sec['content'].split('\n')[0].replace('"', "'") if sec['content'] else ''
        if len(first_line) > 120:
            first_line = first_line[:117] + '...'
            
        page_mdx = f"""---
title: "{sec['clean_title']}"
description: "{first_line}"
---

import {{ Callout }} from 'fumadocs-ui/components/callout';

# {sec['clean_title']}

---

{sec['content']}
"""
        with open(os.path.join(target_dir, f"{sec['slug']}.mdx"), "w", encoding="utf-8") as f:
            f.write(page_mdx)
            
    # 3. Create meta.json
    meta = {
        "title": title_badge,
        "pages": pages_list
    }
    with open(os.path.join(target_dir, "meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)
        
    print(f"Built {display_name}: {len(sections)} sections created.")

print("All plugins from DOCS processed successfully!")
