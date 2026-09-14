import os
import re
import json
import shutil

base_output = r"c:\Development\Webs\ZenDocs\content\docs\plugins\zencustomitems"

def clean_slug(raw_title):
    # take first identifier before slash
    first_part = raw_title.split('/')[0].strip()
    # remove parenthetical notes like *(Novedad)*, (Evolution), etc.
    clean = re.sub(r'\(.*?\)', '', first_part).strip()
    clean = re.sub(r'[\*\`\(\)\?]', '', clean).strip()
    slug = clean.lower().replace(' ', '_').replace('-', '_')
    slug = re.sub(r'[^a-z0-9_]', '', slug)
    return slug

def parse_doc(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    pattern = re.compile(r'^(##|###)\s+(.+)$', re.MULTILINE)
    matches = list(pattern.finditer(text))
    
    current_category = 'General'
    items = []
    seen_slugs = set()
    
    for i, m in enumerate(matches):
        level, title = m.groups()
        start = m.end()
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        chunk = text[start:end].strip()
        
        if level == '##':
            if 'índice' not in title.lower() and 'indice' not in title.lower():
                current_category = re.sub(r'^[0-9\.\s]+', '', title).strip()
        elif level == '###':
            slug = clean_slug(title)
            if not slug:
                continue
            if slug in seen_slugs:
                slug = slug + '_2'
            seen_slugs.add(slug)
            
            clean_title = re.sub(r'[\*\`]', '', title).strip()
            items.append({
                'title': clean_title,
                'slug': slug,
                'category': current_category,
                'content': chunk
            })
    return items

def generate_folder(folder_name, folder_title, items, overview_desc):
    target_dir = os.path.join(base_output, folder_name)
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    os.makedirs(target_dir, exist_ok=True)
    
    # 1. Write index.mdx
    cards_text = ""
    for item in items:
        desc_line = item['content'].split('\n')[0].replace('"', "'") if item['content'] else ''
        if len(desc_line) > 90:
            desc_line = desc_line[:87] + '...'
        cards_text += f'  <Card title="{item["slug"]}" href="/docs/plugins/zencustomitems/{folder_name}/{item["slug"]}" description="{desc_line}" />\n'
        
    index_content = f"""---
title: "{folder_title}"
description: "{overview_desc}"
---

import {{ Card, Cards }} from 'fumadocs-ui/components/card';
import {{ Callout }} from 'fumadocs-ui/components/callout';

Catálogo completo de **{folder_title}** para ZenCustomItems estilo eco / libreforge, estructurado con páginas individuales por cada elemento para consulta detallada.

## 📑 Lista de {folder_title} ({len(items)})

<Cards>
{cards_text}</Cards>
"""
    with open(os.path.join(target_dir, 'index.mdx'), 'w', encoding='utf-8') as f:
        f.write(index_content)
        
    # 2. Write each individual item page
    pages_list = ['index']
    for item in items:
        pages_list.append(item['slug'])
        first_line = item['content'].split('\n')[0].replace('"', "'") if item['content'] else ''
        if len(first_line) > 120:
            first_line = first_line[:117] + '...'
            
        mdx = f"""---
title: "{item['slug']}"
description: "{first_line}"
---

import {{ Callout }} from 'fumadocs-ui/components/callout';

# `{item['slug']}`

* **Categoría:** `{item['category']}`  
* **Identificador / Alias:** `{item['title']}`

---

{item['content']}
"""
        with open(os.path.join(target_dir, f"{item['slug']}.mdx"), 'w', encoding='utf-8') as f:
            f.write(mdx)
            
    # 3. Write meta.json
    meta = {
        'title': folder_title,
        'pages': pages_list
    }
    with open(os.path.join(target_dir, 'meta.json'), 'w', encoding='utf-8') as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)
        
    print(f"Generated {folder_name}: {len(items)} items created.")

effects = parse_doc(r"c:\Development\Webs\ZenDocs\DOCS\ZenCustomItems\EFFECTS.md")
generate_folder("effects", "Effects", effects, "Catálogo completo de efectos individuales estilo eco/libreforge para ZenCustomItems.")

triggers = parse_doc(r"c:\Development\Webs\ZenDocs\DOCS\ZenCustomItems\TRIGGERS.md")
generate_folder("triggers", "Triggers", triggers, "Catálogo completo de disparadores y eventos de activación para ZenCustomItems.")

conditions = parse_doc(r"c:\Development\Webs\ZenDocs\DOCS\ZenCustomItems\CONDITIONS.md")
generate_folder("conditions", "Conditions", conditions, "Catálogo completo de condiciones y validaciones lógicas para ZenCustomItems.")

root_meta = {
    "title": "ZenCustomItems",
    "pages": [
        "index",
        "configuracion",
        "effects",
        "triggers",
        "conditions",
        "filters-and-mutators",
        "flags",
        "sets-and-mastery"
    ]
}
with open(os.path.join(base_output, "meta.json"), "w", encoding="utf-8") as f:
    json.dump(root_meta, f, indent=2, ensure_ascii=False)

print("Regeneration completed with pristine slugs.")
