import os
import re

docs_dir = r"c:\Development\Webs\ZenDocs\content\docs"

# Tags that are legitimate MDX components
ALLOWED_TAGS = {"Callout", "Card", "Cards", "Step", "Steps", "Tab", "Tabs"}

def sanitize_line_outside_code(line):
    # Regex to find <tag_name ...> or <tag_name> or </tag_name>
    def replace_tag(match):
        full = match.group(0)
        tag_name = match.group(1)
        if tag_name in ALLOWED_TAGS:
            return full
        # If it's something like <nombre_zona>, <jugador>, <world>, <x>, <b>, <gradient:...>
        # outside of a codeblock in MDX, it will break JSX parsing.
        # We escape it as `&lt;tag_name&gt;` or simply backtick `full`
        # In markdown text/headings/tables, wrapping in backticks or replacing < with \`<\` is best.
        return f"`{full}`"

    # Replace <something> where something starts with a letter or underscore
    # but not inside already existing backticks
    parts = line.split('`')
    for idx in range(0, len(parts), 2):
        # Even indices are OUTSIDE of backticks
        # Replace <word> with `&lt;word&gt;` or `&lt;...&gt;`
        # Notice also handles closing tags like </rainbow>
        p = parts[idx]
        
        # Replace unescaped <tag> or </tag>
        # e.g. <nombre_zona> or <world> or <x>
        p = re.sub(r'</?([a-zA-Z_][a-zA-Z0-9_\-:#]*)[^>]*>', replace_tag, p)
        parts[idx] = p
        
    return '`'.join(parts)

fixed_files = 0
for root, dirs, files in os.walk(docs_dir):
    for f in files:
        if f.endswith('.mdx'):
            fp = os.path.join(root, f)
            with open(fp, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                
            new_lines = []
            in_code = False
            modified = False
            
            for line in lines:
                if line.strip().startswith('```'):
                    in_code = not in_code
                    new_lines.append(line)
                    continue
                    
                if in_code:
                    new_lines.append(line)
                else:
                    new_l = sanitize_line_outside_code(line)
                    if new_l != line:
                        modified = True
                    new_lines.append(new_l)
                    
            if modified:
                with open(fp, 'w', encoding='utf-8') as file:
                    file.writelines(new_lines)
                fixed_files += 1

print(f"Sanitized MDX in {fixed_files} files.")
