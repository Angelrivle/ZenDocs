import os
import json

docs_dir = r"c:\Development\Webs\ZenDocs\content\docs"

new_plugins = [
    ("zenafkzone", "ZenAfkZone (New)"),
    ("zenauctions", "ZenAuctions (New)"),
    ("zenbank", "ZenBank (New)"),
    ("zenchat", "ZenChat (New)"),
    ("zenchatgames", "ZenChatGames (New)"),
    ("zencosmetics", "ZenCosmetics (New)"),
    ("zenpvpcore", "ZenPvPCore (New)"),
    ("zensacks", "ZenSacks (New)")
]

for folder, title in new_plugins:
    target_dir = os.path.join(docs_dir, folder)
    os.makedirs(target_dir, exist_ok=True)
    
    meta = {
        "title": title,
        "pages": ["introduccion"]
    }
    with open(os.path.join(target_dir, "meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)
        
    clean_title = title.replace("(New)", "").strip()
    intro_content = f"""---
title: "{clean_title}"
description: "Documentación oficial y guías de configuración para {clean_title}."
---

import {{ Callout }} from 'fumadocs-ui/components/callout';

# {clean_title}

Bienvenido a la documentación oficial de **{clean_title}** de ZenForge Studio.

<Callout type="info" title="✨ Nueva Sección">
Esta sección ha sido creada recientemente. Estamos incorporando todas las guías detalladas, ejemplos de configuración y comandos.
</Callout>

## 🚀 Próximamente

* 📘 Guías de instalación y despliegue paso a paso.
* ⚙️ Plantillas de configuración `.yml` optimizadas para producción.
* 🔗 Integración fluida con el ecosistema de ZenForge.
"""
    with open(os.path.join(target_dir, "introduccion.mdx"), "w", encoding="utf-8") as f:
        f.write(intro_content)
    print(f"Created plugin: {folder} -> {title}")

# Update root meta.json
root_meta_path = os.path.join(docs_dir, "meta.json")
with open(root_meta_path, "r", encoding="utf-8") as f:
    root_meta = json.load(f)

current_pages = set(root_meta["pages"])
for folder, _ in new_plugins:
    current_pages.add(folder)

pages_info = []
for p in current_pages:
    folder_path = os.path.join(docs_dir, p)
    meta_path = os.path.join(folder_path, "meta.json")
    title = p
    if os.path.exists(meta_path):
        with open(meta_path, "r", encoding="utf-8") as mf:
            d = json.load(mf)
            title = d.get("title", p)
    clean_title = title.replace("(New)", "").replace("(Soon)", "").strip()
    pages_info.append((p, clean_title))

pages_info.sort(key=lambda x: x[1].lower())

root_meta["pages"] = [p[0] for p in pages_info]

with open(root_meta_path, "w", encoding="utf-8") as f:
    json.dump(root_meta, f, indent=2, ensure_ascii=False)

print("Root meta.json successfully updated and sorted alphabetically!")
