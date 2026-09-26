# -*- coding: utf-8 -*-
"""
render_bcml_bioe3_banner.py
Renders an authentic BBC News / BBC Hindi style Discover banner for the
'बलरामपुर चीनी मिल्स को PLA को-पॉलिमर R&D सुविधा के लिए 75 करोड़ रुपये का BioE3 अनुदान' article (<95KB WebP, 1200x675).
"""
import os
import sys
import subprocess
import base64
from PIL import Image

BASE_DIR = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
BLOG_IMG_DIR = os.path.join(BASE_DIR, 'static', 'images', 'blog')
NEWS_IMG_DIR = os.path.join(BASE_DIR, 'static', 'images', 'news')
os.makedirs(BLOG_IMG_DIR, exist_ok=True)
os.makedirs(NEWS_IMG_DIR, exist_ok=True)

BG_PATH = r'C:\Users\caneu\.gemini\antigravity\brain\a9ecd357-12c8-4c55-ba6e-8e8e975fca16\bcml_bioplastic_plant_1790391983707.jpg'

chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
if not os.path.exists(chrome_exe):
    chrome_exe = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

spec = {
    "filename": "balrampur-chini-mills-pla-bioe3-grant-75-crore.webp",
    "tag": "BioE3 मिशन ⚡ ₹75 करोड़",
    "h1": "बलरामपुर चीनी को ₹75 करोड़ का BioE3 अनुदान",
    "h2_html": "यूपी के कुंभी में गन्ने से बनेगा बायोप्लास्टिक • <span class='sub-highlight'>100 TPA R&D सेंटर</span>"
}

with open(BG_PATH, "rb") as f:
    bg_b64 = base64.b64encode(f.read()).decode("utf-8")

html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset='UTF-8'>
<style>
@import url('https://fonts.googleapis.com/css2?family=Mukta:wght@700;800;900&family=Noto+Sans+Devanagari:wght@700;800;900&display=swap');

* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
    width: 1200px;
    height: 675px;
    overflow: hidden;
    background: #000000;
    font-family: 'Mukta', 'Noto Sans Devanagari', sans-serif;
    position: relative;
}}

.canvas {{
    width: 1200px;
    height: 675px;
    position: relative;
    overflow: hidden;
    background: #000;
}}

.bg-img {{
    position: absolute;
    top: 0;
    left: 0;
    width: 1200px;
    height: 675px;
    object-fit: cover;
    filter: brightness(0.92) contrast(1.08);
}}

/* BBC Dark Gradient Overlay */
.dark-gradient {{
    position: absolute;
    bottom: 0;
    left: 0;
    width: 1200px;
    height: 430px;
    background: linear-gradient(to top, rgba(0, 0, 0, 0.98) 0%, rgba(0, 0, 0, 0.86) 55%, rgba(0, 0, 0, 0) 100%);
    z-index: 2;
}}

/* BBC Brand Bar (Top Left) */
.bbc-brand-bar {{
    position: absolute;
    top: 28px;
    left: 36px;
    display: flex;
    align-items: center;
    gap: 8px;
    z-index: 10;
}}

.bbc-box {{
    background: #bb1919;
    color: #ffffff;
    font-family: 'Arial Black', Impact, sans-serif;
    font-size: 26px;
    font-weight: 900;
    padding: 6px 16px;
    letter-spacing: 2px;
    text-transform: uppercase;
    box-shadow: 0 4px 14px rgba(0,0,0,0.7);
}}

.bbc-news-box {{
    background: #ffffff;
    color: #111111;
    font-family: 'Arial Black', Impact, sans-serif;
    font-size: 26px;
    font-weight: 900;
    padding: 6px 14px;
    letter-spacing: 2px;
    text-transform: uppercase;
    box-shadow: 0 4px 14px rgba(0,0,0,0.7);
}}

/* BBC Tag (Top Right) */
.bbc-tag {{
    position: absolute;
    top: 28px;
    right: 36px;
    background: rgba(10, 15, 25, 0.92);
    border-left: 5px solid #bb1919;
    color: #ffffff;
    font-size: 22px;
    font-weight: 800;
    padding: 7px 20px;
    z-index: 10;
    backdrop-filter: blur(8px);
    box-shadow: 0 4px 14px rgba(0,0,0,0.6);
    border-radius: 0 6px 6px 0;
}}

/* BBC Typography Block System */
.bbc-content-wrapper {{
    position: absolute;
    bottom: 28px;
    left: 36px;
    right: 36px;
    z-index: 5;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
}}

.bbc-main-headline {{
    background: #bb1919;
    color: #ffffff;
    font-size: 50px;
    font-weight: 900;
    line-height: 1.18;
    padding: 10px 24px;
    display: inline-block;
    box-shadow: 0 6px 18px rgba(0,0,0,0.85);
    letter-spacing: -0.2px;
    border-radius: 4px;
}}

.bbc-sub-headline {{
    background: #050505;
    color: #ffffff;
    font-size: 33px;
    font-weight: 800;
    line-height: 1.25;
    padding: 8px 22px;
    display: inline-block;
    border-left: 7px solid #facc15;
    box-shadow: 0 6px 18px rgba(0,0,0,0.85);
    border-radius: 0 4px 4px 0;
}}

.sub-highlight {{
    color: #facc15;
}}
</style>
</head>
<body>
<div class='canvas'>
    <img class='bg-img' src='data:image/jpeg;base64,{bg_b64}' />
    <div class='dark-gradient'></div>
    
    <div class='bbc-brand-bar'>
        <div class='bbc-box'>CANEUP</div>
        <div class='bbc-news-box'>NEWS</div>
    </div>
    
    <div class='bbc-tag'>{spec['tag']}</div>
    
    <div class='bbc-content-wrapper'>
        <div class='bbc-main-headline'>{spec['h1']}</div>
        <div class='bbc-sub-headline'>{spec['h2_html']}</div>
    </div>
</div>
</body>
</html>
"""

temp_html = os.path.join(BASE_DIR, "scripts", "temp_bcml_banner.html")
temp_png = os.path.join(BASE_DIR, "scripts", "temp_bcml_banner.png")

with open(temp_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print("[1] Rendering banner via Headless Chrome at 1200x675...")
cmd = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    "--window-size=1200,675",
    "--hide-scrollbars",
    f"--screenshot={temp_png}",
    temp_html
]
subprocess.run(cmd, check=True)

if not os.path.exists(temp_png):
    print("Error: temp_png not created!")
    sys.exit(1)

print("[2] Optimizing image to WebP (<95 KB)...")
im = Image.open(temp_png).convert("RGB")
if im.size != (1200, 675):
    im = im.resize((1200, 675), Image.Resampling.LANCZOS)

target_blog = os.path.join(BLOG_IMG_DIR, spec["filename"])
target_news = os.path.join(NEWS_IMG_DIR, spec["filename"])

quality = 85
for q in range(85, 45, -5):
    im.save(target_blog, "WEBP", quality=q, method=6)
    size_kb = os.path.getsize(target_blog) / 1024
    if size_kb <= 95.0:
        quality = q
        break

im.save(target_news, "WEBP", quality=quality, method=6)

size_blog = os.path.getsize(target_blog) / 1024
size_news = os.path.getsize(target_news) / 1024
print(f"[+] Successfully rendered WebP banner:")
print(f"    Blog: {target_blog} ({size_blog:.1f} KB, Q={quality})")
print(f"    News: {target_news} ({size_news:.1f} KB, Q={quality})")

# Clean temp files
if os.path.exists(temp_html): os.remove(temp_html)
if os.path.exists(temp_png): os.remove(temp_png)
