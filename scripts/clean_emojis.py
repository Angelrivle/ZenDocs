import os
import re

# Comprehensive emoji regex
emoji_pattern = re.compile(
    r'[\U00010000-\U0010ffff\u2600-\u26ff\u2700-\u27bf\u2300-\u23ff\u2b50\u2b55\u200d\ufe0f]'
)

total_cleaned = 0

for root, dirs, files in os.walk('content/docs'):
    for file in files:
        if file.endswith('.mdx'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            lines = content.split('\n')
            new_lines = []
            for line in lines:
                # Clean emojis from headers (#, ##, ###), frontmatter title/description, Cards, and list bullets
                stripped = line.strip()
                if (
                    stripped.startswith('#')
                    or stripped.startswith('title:')
                    or stripped.startswith('description:')
                    or 'title="' in line
                    or stripped.startswith('*')
                    or stripped.startswith('-')
                ):
                    cleaned_line = emoji_pattern.sub('', line)
                    # Clean double spaces
                    cleaned_line = re.sub(r'  +', ' ', cleaned_line)
                    new_lines.append(cleaned_line)
                else:
                    new_lines.append(line)

            new_content = '\n'.join(new_lines)
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total_cleaned += 1

print(f"Cleaned emojis in {total_cleaned} files.")
