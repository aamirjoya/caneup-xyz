import os
import sys
import json
import urllib.request
from PIL import Image

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

artifact_dir = r'C:\Users\caneu\.gemini\antigravity\brain\f0566670-25ee-4739-bb10-e53286d68160'
ws_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore\static\images\webstories'
content_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore\content\webstories'

os.makedirs(ws_dir, exist_ok=True)

# 1. Process Generated Featured Covers
featured_mapping = {
    'ganna-satta-pre-calendar-2026-guide.md': ('ws_satta_precal_1787597283025.jpg', 'ws-satta-precal-cover.webp'),
    'eganna-app-v6-features.md': ('ws_eganna_v6_1787597294561.jpg', 'ws-eganna-v6-cover.webp'),
    'ganna-bhav-600-kisan-maang.md': ('ws_bhav_600_1787597306153.jpg', 'ws-bhav-600-cover.webp'),
    'red-rot-monsoon-prevention-tips.md': ('ws_red_rot_1787597358502.jpg', 'ws-red-rot-cover.webp'),
    'up-sugar-mills-start-date-2026.md': ('ws_sugar_mills_1787597400680.jpg', 'ws-sugar-mills-cover.webp'),
    'cos-17231-colk-16202-new-varieties.md': ('ws_cos17231_1787597414786.jpg', 'ws-cos17231-cover.webp'),
    'ganna-ghosna-patra-2026-deadline.md': ('ws_ghosna_patra_1787597497431.jpg', 'ws-ghosna-patra-cover.webp'),
    'ganna-bakaya-bhugtan-15-percent-byaj.md': ('ws_bakaya_bhugtan_1787597630507.jpg', 'ws-bakaya-bhugtan-cover.webp'),
    'sharad-kalin-trench-buwai-tips.md': ('ws_sharad_buwai_1787597643580.jpg', 'ws-sharad-buwai-cover.webp'),
    'caneup-online-grievance-complaint.md': ('ws_grievance_1787597656680.jpg', 'ws-grievance-cover.webp')
}

print("--- Processing High CTR Featured Images ---")
for md_file, (src_jpg, dst_webp) in featured_mapping.items():
    src_path = os.path.join(artifact_dir, src_jpg)
    dst_path = os.path.join(ws_dir, dst_webp)
    if os.path.exists(src_path):
        img = Image.open(src_path)
        img = img.resize((720, 960), Image.LANCZOS)
        
        lo, hi = 10, 85
        best_q = lo
        while lo <= hi:
            mid = (lo + hi) // 2
            img.save(dst_path, 'WEBP', quality=mid, method=6)
            if os.path.getsize(dst_path) <= 150 * 1024:
                best_q = mid
                lo = mid + 1
            else:
                hi = mid - 1
        img.save(dst_path, 'WEBP', quality=best_q, method=6)
        print(f"OK Cover: {dst_webp} ({round(os.path.getsize(dst_path)/1024)}KB)")

# 2. Pexels API Fetcher
pexels_key = 'RNPmFfg4N6daXX7y7TZmZvKUYJVGhlcmN9GFrQhUftTi0CahDr3fMZf3'

def fetch_pexels_images(query, count=6):
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
            for i, p in enumerate(photos[:count]):
                img_url = p['src']['large']
                file_name = f"pexels-{query.replace(' ', '-')}-{p['id']}.webp"
                file_path = os.path.join(ws_dir, file_name)
                
                if not os.path.exists(file_path):
                    # Download image using Request with headers
                    temp_name = file_path + ".tmp"
                    img_req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(img_req) as img_resp, open(temp_name, 'wb') as out_f:
                        out_f.write(img_resp.read())
                        
                    img = Image.open(temp_name)
                    img = img.resize((720, 1280), Image.LANCZOS)
                    
                    lo, hi = 10, 85
                    best_q = lo
                    while lo <= hi:
                        mid = (lo + hi) // 2
                        img.save(file_path, 'WEBP', quality=mid, method=6)
                        if os.path.getsize(file_path) <= 150 * 1024:
                            best_q = mid
                            lo = mid + 1
                        else:
                            hi = mid - 1
                    img.save(file_path, 'WEBP', quality=best_q, method=6)
                    if os.path.exists(temp_name):
                        os.remove(temp_name)
                
                image_paths.append(f"/images/webstories/{file_name}")
    except Exception as e:
        print(f"Pexels fetch error for '{query}':", e)
    return image_paths

# 3. WebStory Specific Pexels Searches & MD Update
ws_queries = {
    'ganna-satta-pre-calendar-2026-guide.md': ('sugarcane farmer mobile', 'ws-satta-precal-cover.webp'),
    'eganna-app-v6-features.md': ('smartphone technology farmer', 'ws-eganna-v6-cover.webp'),
    'ganna-bhav-600-kisan-maang.md': ('indian farmer agriculture', 'ws-bhav-600-cover.webp'),
    'red-rot-monsoon-prevention-tips.md': ('farm pest control spraying', 'ws-red-rot-cover.webp'),
    'up-sugar-mills-start-date-2026.md': ('sugar factory mill', 'ws-sugar-mills-cover.webp'),
    'cos-17231-colk-16202-new-varieties.md': ('sugarcane plantation green', 'ws-cos17231-cover.webp'),
    'ganna-ghosna-patra-2026-deadline.md': ('document writing farmer', 'ws-ghosna-patra-cover.webp'),
    'ganna-bakaya-bhugtan-15-percent-byaj.md': ('money bank finance farmer', 'ws-bakaya-bhugtan-cover.webp'),
    'sharad-kalin-trench-buwai-tips.md': ('tractor farming mustard field', 'ws-sharad-buwai-cover.webp'),
    'caneup-online-grievance-complaint.md': ('office customer service phone', 'ws-grievance-cover.webp')
}

print("\n--- Fetching Pexels Images and Updating WebStories ---")
import re

for md_file, (search_query, cover_webp) in ws_queries.items():
    md_path = os.path.join(content_dir, md_file)
    if not os.path.exists(md_path):
        continue
    
    pexels_imgs = fetch_pexels_images(search_query, count=6)
    if len(pexels_imgs) < 6:
        # Fallback query
        extra = fetch_pexels_images("agriculture farmer", count=6)
        pexels_imgs = (pexels_imgs + extra)[:6]
        
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Update featured_image
    content = re.sub(r'featured_image:\s*".*?"', f'featured_image: "/images/webstories/{cover_webp}"', content)
    
    # Update slide images
    lines = content.split('\n')
    slide_idx = 0
    new_lines = []
    for line in lines:
        if line.strip().startswith('image:'):
            if slide_idx < len(pexels_imgs):
                new_line = f'    image: "{pexels_imgs[slide_idx]}"'
                slide_idx += 1
            else:
                new_line = line
            new_lines.append(new_line)
        else:
            new_lines.append(line)
            
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
        
    print(f"Updated {md_file} with cover /images/webstories/{cover_webp} and {slide_idx} Pexels slide images.")

print("\nAll Web Stories processed successfully!")
