# -*- coding: utf-8 -*-
import os, glob, re

content_dir = r"c:\Users\caneu\Downloads\caneup-xyz-restore\content"

md_files = glob.glob(os.path.join(content_dir, "**", "*.md"), recursive=True)
print(f"Total markdown files found: {len(md_files)}")

updated_count = 0

for fpath in md_files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    orig = content
    
    # 1. Author Name Replacements
    content = content.replace("Randhir Patil", "Aamir Raza")
    content = content.replace("randhir-patil.webp", "aamir-raza.webp")
    content = content.replace("randhir-patil.jpg", "aamir-raza.webp")
    content = content.replace("randhir-patil", "aamir-raza")
    content = content.replace("https://www.chinimandi.com/author/randhir-patil/", "https://caneup.xyz/authors/aamir-raza/")
    content = content.replace("https://twitter.com/caneupxyz", "https://x.com/caneupupdates")
    content = content.replace("@caneupxyz", "@caneupupdates")

    # 2. Clean any hardcoded duplicate summary box if present in body
    dup_box_pattern = r'<div class="ai-summary-box"[^>]*>[\s\S]*?</div>'
    content = re.sub(dup_box_pattern, '', content)

    # 3. Clean any generic repeated boilerplate paragraph if present
    content = re.sub(r'CaneUp पर इस पोस्ट में गन्ना किसानों के लिए उपयोगी जानकारी दी गई है —[\s\S]*?अपडेट किया जाता है।', '', content)

    if content != orig:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        updated_count += 1

print(f"Successfully updated {updated_count} files to Aamir Raza and @caneupupdates.")
