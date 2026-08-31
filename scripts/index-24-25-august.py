import os
import glob
import re
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
files = glob.glob(os.path.join(base_dir, 'content', 'news', '*.md')) + \
        glob.glob(os.path.join(base_dir, 'content', 'posts', '*.md')) + \
        glob.glob(os.path.join(base_dir, 'content', 'webstories', '*.md'))

target_urls = []

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
        
    date_match = re.search(r'date:\s*["\']?(2026-08-24|2026-08-25)', txt)
    slug_match = re.search(r'slug:\s*["\']?([^\s"\']+)', txt)
    
    if date_match:
        norm_path = f.replace('\\', '/')
        if 'content/news' in norm_path:
            sec = 'news'
        elif 'content/webstories' in norm_path:
            sec = 'webstories'
        else:
            sec = 'posts'
            
        if slug_match:
            slug = slug_match.group(1).strip()
        else:
            slug = os.path.basename(f).replace('.md', '')
            
        url = f"https://caneup.xyz/{sec}/{slug}/"
        target_urls.append(url)

# Remove duplicates while preserving order
seen = set()
unique_urls = []
for u in target_urls:
    if u not in seen:
        seen.add(u)
        unique_urls.append(u)

print(f"Total 24 & 25 Aug 2026 URLs found: {len(unique_urls)}")
for i, u in enumerate(unique_urls, 1):
    print(f" {i:2d}. {u}")

# Save to temporary file for batch submitting
list_file = os.path.join(base_dir, 'scripts', 'aug24_25_urls.txt')
with open(list_file, 'w', encoding='utf-8') as out_f:
    out_f.write('\n'.join(unique_urls))

print(f"\nSaved URL list to: {list_file}")
