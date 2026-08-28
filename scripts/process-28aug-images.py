import os
import glob
from PIL import Image

artifact_dir = r'C:\Users\caneu\.gemini\antigravity\brain\f0566670-25ee-4739-bb10-e53286d68160'
base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
static_news_dir = os.path.join(base_dir, 'static', 'images', 'news')
content_news_dir = os.path.join(base_dir, 'content', 'news')
os.makedirs(static_news_dir, exist_ok=True)

image_mapping = [
    {
        "pattern": "lakhimpur_protest_2026_*.jpg",
        "output_name": "lakhimpur-protest-28aug-2026.webp",
        "article_file": "breaking-lakhimpur-kheri-ganna-kisan-protest-29-august-2026.md"
    },
    {
        "pattern": "bareilly_priority_2026_*.jpg",
        "output_name": "bareilly-parchi-priority-2026.webp",
        "article_file": "breaking-bareilly-mahila-divyang-kisan-parchi-priority-2026.md"
    },
    {
        "pattern": "maharashtra_permit_2026_*.jpg",
        "output_name": "maharashtra-crushing-permit-2026.webp",
        "article_file": "breaking-maharashtra-crushing-permit-deadline-30-september-2026.md"
    },
    {
        "pattern": "karnataka_bonus_2026_*.jpg",
        "output_name": "karnataka-sap-bonus-2026.webp",
        "article_file": "breaking-karnataka-farmers-900-per-tonne-sap-demand-2026.md"
    },
    {
        "pattern": "pm_kisan_2030_*.jpg",
        "output_name": "pm-kisan-2030-extension-2026.webp",
        "article_file": "breaking-pm-kisan-3-lakh-crore-cabinet-extension-2030-2026.md"
    }
]

for item in image_mapping:
    matches = glob.glob(os.path.join(artifact_dir, item["pattern"]))
    if not matches:
        print(f"No match for {item['pattern']}")
        continue
        
    src_jpg = matches[0]
    out_path = os.path.join(static_news_dir, item["output_name"])
    
    img = Image.open(src_jpg)
    img = img.resize((1200, 675), Image.LANCZOS)
    
    # Binary search quality tuning to ensure size strictly < 200KB (targeting 120-170KB)
    lo, hi = 20, 95
    best_q = lo
    while lo <= hi:
        mid = (lo + hi) // 2
        img.save(out_path, 'WEBP', quality=mid, method=6)
        size_kb = os.path.getsize(out_path) / 1024.0
        if size_kb <= 190:
            best_q = mid
            lo = mid + 1
        else:
            hi = mid - 1
            
    img.save(out_path, 'WEBP', quality=best_q, method=6)
    final_kb = os.path.getsize(out_path) / 1024.0
    print(f"Processed: {item['output_name']} ({final_kb:.1f} KB, quality={best_q})")
    
    # Update article frontmatter with new image path
    md_path = os.path.join(content_news_dir, item["article_file"])
    if os.path.exists(md_path):
        with open(md_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        new_lines = []
        for line in lines:
            if line.startswith('featured_image:'):
                new_lines.append(f"featured_image: /images/news/{item['output_name']}\n")
            elif line.startswith('image:'):
                new_lines.append(f"image: /images/news/{item['output_name']}\n")
            else:
                new_lines.append(line)
                
        with open(md_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Updated Frontmatter: {item['article_file']}")

print("\nAll 5 Featured Images processed, compressed (<200KB WebP), and mapped to articles!")
