import os
import sys
import glob
import json
import urllib.request
import urllib.parse
from PIL import Image

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
artifact_dir = r'C:\Users\caneu\.gemini\antigravity\brain\f0566670-25ee-4739-bb10-e53286d68160'
static_ws_dir = os.path.join(base_dir, 'static', 'images', 'webstories')
content_ws_dir = os.path.join(base_dir, 'content', 'webstories')
os.makedirs(static_ws_dir, exist_ok=True)

pexels_key = "RNPmFfg4N6daXX7y7TZmZvKUYJVGhlcmN9GFrQhUftTi0CahDr3fMZf3"

# 10 Web Stories mapping
webstories_data = [
    {
        "file": "ganna-kisan-lakhimpur-protest-2026.md",
        "pattern": "ws_lakhimpur_cover_*.jpg",
        "cover_name": "ws-lakhimpur-protest-cover.webp",
        "query": "sugarcane farmer protest"
    },
    {
        "file": "bareilly-mahila-divyang-parchi-priority-2026.md",
        "pattern": "ws_bareilly_cover_*.jpg",
        "cover_name": "ws-bareilly-priority-cover.webp",
        "query": "smartphone technology farmer"
    },
    {
        "file": "maharashtra-sugar-mill-crushing-permit-2026.md",
        "pattern": "ws_maharashtra_cover_*.jpg",
        "cover_name": "ws-maharashtra-permit-cover.webp",
        "query": "sugar factory mill"
    },
    {
        "file": "karnataka-farmer-900-bonus-demand-2026.md",
        "pattern": "ws_karnataka_cover_*.jpg",
        "cover_name": "ws-karnataka-bonus-cover.webp",
        "query": "indian farmer agriculture"
    },
    {
        "file": "pm-kisan-3-lakh-crore-budget-2030-2026.md",
        "pattern": "ws_pmkisan_cover_*.jpg",
        "cover_name": "ws-pmkisan-2030-cover.webp",
        "query": "money bank finance farmer"
    },
    {
        "file": "digital-agri-mission-farmer-id-guide-2026.md",
        "pattern": "ws_farmer_id_cover_*.jpg",
        "cover_name": "ws-farmer-id-cover.webp",
        "query": "document writing farmer"
    },
    {
        "file": "chini-bhav-36-percent-badha-impact-2026.md",
        "pattern": "ws_chini_bhav_cover_*.jpg",
        "cover_name": "ws-chini-bhav-cover.webp",
        "query": "sugar factory mill"
    },
    {
        "file": "ganna-kisan-kcc-loan-4-percent-2026.md",
        "pattern": "ws_kcc_loan_cover_*.jpg",
        "cover_name": "ws-kcc-loan-cover.webp",
        "query": "money bank finance farmer"
    },
    {
        "file": "trench-method-sarson-intercropping-2026.md",
        "pattern": "ws_trench_buwai_*.jpg",
        "cover_name": "ws-trench-sarson-cover.webp",
        "query": "tractor farming mustard field"
    },
    {
        "file": "caneup-survey-sudhar-last-date-2026.md",
        "pattern": "online_grievance_*.jpg",
        "cover_name": "ws-survey-sudhar-cover.webp",
        "query": "office customer service phone"
    }
]

print("--- Step 1: Processing Cover Images ---")
for item in webstories_data:
    matches = glob.glob(os.path.join(artifact_dir, item["pattern"]))
    out_path = os.path.join(static_ws_dir, item["cover_name"])
    
    if matches:
        src_img = matches[0]
    else:
        # Fallback to any JPG artifact
        all_jpgs = glob.glob(os.path.join(artifact_dir, "*.jpg"))
        src_img = all_jpgs[0] if all_jpgs else None
        
    if src_img and os.path.exists(src_img):
        img = Image.open(src_img)
        img = img.resize((720, 960), Image.LANCZOS)
        
        # Binary search quality tuning for <150KB WebP
        lo, hi = 20, 95
        best_q = lo
        while lo <= hi:
            mid = (lo + hi) // 2
            img.save(out_path, 'WEBP', quality=mid, method=6)
            if os.path.getsize(out_path) <= 145 * 1024:
                best_q = mid
                lo = mid + 1
            else:
                hi = mid - 1
        img.save(out_path, 'WEBP', quality=best_q, method=6)
        size_kb = os.path.getsize(out_path) / 1024.0
        print(f"OK Cover: {item['cover_name']} ({size_kb:.1f} KB)")


def fetch_pexels_slide_images(query, count=6):
    url = f"https://api.pexels.com/v1/search?query={urllib.parse.quote(query)}&per_page={count*2}"
    headers = {
        'Authorization': pexels_key,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    req = urllib.request.Request(url, headers=headers)
    image_paths = []
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            photos = data.get('photos', [])
            for p in photos[:count]:
                img_url = p['src']['large']
                file_name = f"pexels-{query.replace(' ', '-')}-{p['id']}.webp"
                file_path = os.path.join(static_ws_dir, file_name)
                
                if not os.path.exists(file_path):
                    temp_name = file_path + ".tmp"
                    img_req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(img_req) as img_resp, open(temp_name, 'wb') as out_f:
                        out_f.write(img_resp.read())
                        
                    img = Image.open(temp_name)
                    img = img.resize((720, 1280), Image.LANCZOS)
                    
                    lo, hi = 20, 95
                    best_q = lo
                    while lo <= hi:
                        mid = (lo + hi) // 2
                        img.save(file_path, 'WEBP', quality=mid, method=6)
                        if os.path.getsize(file_path) <= 145 * 1024:
                            best_q = mid
                            lo = mid + 1
                        else:
                            hi = mid - 1
                    img.save(file_path, 'WEBP', quality=best_q, method=6)
                    if os.path.exists(temp_name):
                        os.remove(temp_name)
                
                image_paths.append(f"/images/webstories/{file_name}")
    except Exception as e:
        print(f"Pexels error for '{query}':", e)
    return image_paths


print("\n--- Step 2: Fetching Pexels Slide Images & Updating Markdown Files ---")
for item in webstories_data:
    md_path = os.path.join(content_ws_dir, item["file"])
    if not os.path.exists(md_path):
        continue
        
    pexels_slides = fetch_pexels_slide_images(item["query"], count=6)
    if not pexels_slides:
        # Fallback to existing pexels images in static/images/webstories
        existing_imgs = glob.glob(os.path.join(static_ws_dir, "pexels-*.webp"))
        pexels_slides = [f"/images/webstories/{os.path.basename(p)}" for p in existing_imgs[:6]]
        
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    slide_idx = 0
    in_slides = False
    
    for line in lines:
        if line.strip().startswith('featured_image:'):
            new_lines.append(f'featured_image: "/images/webstories/{item["cover_name"]}"\n')
        elif line.strip().startswith('slides:'):
            in_slides = True
            new_lines.append(line)
        elif in_slides and (line.strip().startswith('- image:') or line.strip().startswith('image:')):
            if slide_idx < len(pexels_slides):
                img_url = pexels_slides[slide_idx]
                slide_idx += 1
            else:
                img_url = pexels_slides[0] if pexels_slides else f"/images/webstories/{item['cover_name']}"
                
            prefix = "  - image:" if line.strip().startswith('- image:') else "    image:"
            new_lines.append(f'{prefix} "{img_url}"\n')
        else:
            new_lines.append(line)
            
    with open(md_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
        
    print(f"Updated {item['file']} with cover and {slide_idx} slide images.")

print("\nAll 10 Web Stories processed successfully!")
