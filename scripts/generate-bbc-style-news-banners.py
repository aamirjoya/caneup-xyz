import os
import sys
import subprocess
import base64
from PIL import Image

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
img_dir = os.path.join(base_dir, 'static', 'images', 'news')
brain_dir = r'C:\Users\caneu\.gemini\antigravity\brain\f0566670-25ee-4739-bb10-e53286d68160'

chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
if not os.path.exists(chrome_exe):
    chrome_exe = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

banners_spec = [
    {
        "dst": "saharanpur-mandal-36-drones-ganna-spraying-2026.webp",
        "bg": os.path.join(brain_dir, "trending_farming_1787488920538.jpg"),
        "tag": "ग्राउंड रिपोर्ट ⚡",
        "h1": "सहारनपुर: 36 ड्रोन से गन्ने पर छिड़काव शुरू",
        "h2_html": "जलभराव के बीच <span class='sub-highlight'>5 मिनट में 1 एकड़</span> में दवा स्प्रे"
    },
    {
        "dst": "sugar-ex-mill-price-drop-30-percent-47-kg-2026.webp",
        "bg": os.path.join(brain_dir, "ws_chini_bhav_cover_1787906314949.jpg"),
        "tag": "बाजार विश्लेषण ⚡",
        "h1": "चीनी के एक्स-मिल भाव 30% गिरे",
        "h2_html": "थोक भाव <span class='sub-highlight'>₹47 किलो पहुंचे</span>, खुदरा में जल्द राहत"
    },
    {
        "dst": "up-ganna-bhugtan-1200-crore-release-august-2026.webp",
        "bg": os.path.join(brain_dir, "sugar_mill_payment_1787489145600.jpg"),
        "tag": "बड़ी राहत ⚡",
        "h1": "यूपी: 1200 करोड़ का गन्ना भुगतान जारी",
        "h2_html": "प्रदेश में <span class='sub-highlight'>97.4% बकाया चुकता</span>, 104 मिलों ने निपटाया"
    },
    {
        "dst": "ganna-jaivik-keet-niyantran-trichoderma-distribution-2026.webp",
        "bg": os.path.join(brain_dir, "ws_red_rot_1787597358502.jpg"),
        "tag": "कृषि तकनीक ⚡",
        "h1": "गन्ने में जैविक कीट नियंत्रण महा-अभियान",
        "h2_html": "<span class='sub-highlight'>1.5 लाख किसानों को</span> फ्री बांटे जा रहे बायो-एजेंट्स"
    },
    {
        "dst": "ganna-beej-upchar-hot-water-treatment-plant-2026.webp",
        "bg": os.path.join(brain_dir, "ws_cos17231_1787597414786.jpg"),
        "tag": "नया आदेश ⚡",
        "h1": "120 चीनी मिलों में गर्म पानी से बीज शोधन",
        "h2_html": "<span class='sub-highlight'>HWT प्लांट अनिवार्य</span>, लाल सड़न के बीजाणु होंगे नष्ट"
    },
    {
        "dst": "haryana-up-ganna-sap-405-demand-comparison-2026.webp",
        "bg": os.path.join(brain_dir, "ws_bhav_600_1787597306153.jpg"),
        "tag": "एसएपी दरें ⚡",
        "h1": "हरियाणा में गन्ने का भाव ₹405 संभव",
        "h2_html": "यूपी में किसान यूनियनों की <span class='sub-highlight'>₹400 से ₹600 मांग</span> तेज"
    },
    {
        "dst": "ganna-patti-prabandhan-1000-rupaye-anudan-up-2026.webp",
        "bg": os.path.join(brain_dir, "trench_buwai_1787582649543.jpg"),
        "tag": "सरकारी योजना ⚡",
        "h1": "गन्ने की पत्ती न जलाने पर ₹1000 अनुदान",
        "h2_html": "खेत में मल्चिंग करने पर <span class='sub-highlight'>सीधे खाते में प्रोत्साहन</span>"
    },
    {
        "dst": "omc-ethanol-tender-950-crore-litres-sugarcane-allocation-2026.webp",
        "bg": os.path.join(brain_dir, "news9_ethanol_expansion_cover_1787948284345.jpg"),
        "tag": "ऊर्जा टेंडर ⚡",
        "h1": "तेल कंपनियों का 950 करोड़ लीटर एथेनॉल टेंडर",
        "h2_html": "गन्ने के रस वाले एथेनॉल को <span class='sub-highlight'>₹65.61 दर व प्राथमिकता</span>"
    },
    {
        "dst": "pm-kisan-24th-installment-land-seeding-ekyc-deadline-2026.webp",
        "bg": os.path.join(brain_dir, "ws_pmkisan_cover_1787906167254.jpg"),
        "tag": "अंतिम तिथि ⚡",
        "h1": "PM किसान: 10 सितंबर तक ई-केवाईसी अनिवार्य",
        "h2_html": "24वीं किश्त से पहले <span class='sub-highlight'>लैंड व आधार सीडिंग</span> जरूरी"
    },
    {
        "dst": "up-cooperative-sugar-mills-modernization-650-crore-fund-2026.webp",
        "bg": os.path.join(brain_dir, "ws_sugar_mills_1787597400680.jpg"),
        "tag": "आधुनिकीकरण ⚡",
        "h1": "यूपी: 28 सहकारी चीनी मिलों का होगा कायाकल्प",
        "h2_html": "<span class='sub-highlight'>₹650 करोड़ मंजूर</span>, 15 अक्टूबर से पहले अपग्रेड"
    }
]

temp_html_path = os.path.join(img_dir, "_temp_bbc_render.html")
temp_png_path = os.path.join(img_dir, "_temp_bbc_render.png")

for idx, spec in enumerate(banners_spec, 1):
    dst_webp_path = os.path.join(img_dir, spec["dst"])
    bg_img_path = spec["bg"]
    
    if not os.path.exists(bg_img_path):
        bg_img_path = os.path.join(brain_dir, "ws_sugar_mills_1787597400680.jpg")
        
    with open(bg_img_path, 'rb') as f:
        bg_b64 = base64.b64encode(f.read()).decode('utf-8')
        
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset='UTF-8'>
<style>
@import url('https://fonts.googleapis.com/css2?family=Mukta:wght@700;800;900&family=Noto+Sans+Devanagari:wght@700;800;900&family=Teko:wght@700&display=swap');

* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
    width: 1200px;
    height: 675px;
    overflow: hidden;
    background: #0b0c10;
    font-family: 'Mukta', 'Noto Sans Devanagari', sans-serif;
    position: relative;
}}

.canvas {{
    width: 1200px;
    height: 675px;
    position: relative;
    background: #000;
    overflow: hidden;
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
    height: 400px;
    background: linear-gradient(to top, rgba(0, 0, 0, 0.96) 0%, rgba(0, 0, 0, 0.8) 45%, rgba(0, 0, 0, 0) 100%);
    z-index: 2;
}}

/* BBC Header / Brand Badge (Top Left) */
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
    box-shadow: 0 4px 12px rgba(0,0,0,0.6);
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
    box-shadow: 0 4px 12px rgba(0,0,0,0.6);
}}

/* BBC Tag (Top Right) */
.bbc-tag {{
    position: absolute;
    top: 28px;
    right: 36px;
    background: rgba(0, 0, 0, 0.8);
    border-left: 4px solid #bb1919;
    color: #ffffff;
    font-size: 22px;
    font-weight: 800;
    padding: 6px 18px;
    z-index: 10;
    backdrop-filter: blur(8px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.5);
}}

/* BBC Typography Block System */
.bbc-content-wrapper {{
    position: absolute;
    bottom: 32px;
    left: 36px;
    right: 36px;
    z-index: 5;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
}}

.bbc-main-headline {{
    background: #bb1919;
    color: #ffffff;
    font-size: 56px;
    font-weight: 900;
    line-height: 1.15;
    padding: 8px 22px;
    display: inline-block;
    box-shadow: 0 6px 16px rgba(0,0,0,0.7);
    letter-spacing: -0.2px;
}}

.bbc-sub-headline {{
    background: #000000;
    color: #ffffff;
    font-size: 38px;
    font-weight: 800;
    line-height: 1.2;
    padding: 6px 20px;
    display: inline-block;
    border-left: 6px solid #facc15;
    box-shadow: 0 6px 16px rgba(0,0,0,0.7);
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
    with open(temp_html_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    cmd = [
        chrome_exe,
        '--headless=new',
        '--disable-gpu',
        '--hide-scrollbars',
        '--window-size=1200,675',
        f'--screenshot={temp_png_path}',
        f'file:///{temp_html_path}'
    ]
    subprocess.run(cmd, check=True)
    
    with Image.open(temp_png_path) as im:
        im = im.crop((0, 0, 1200, 675))
        quality = 82
        im.save(dst_webp_path, 'WEBP', quality=quality, optimize=True)
        kb = os.path.getsize(dst_webp_path) / 1024.0
        while kb > 95.0 and quality > 35:
            quality -= 5
            im.save(dst_webp_path, 'WEBP', quality=quality, optimize=True)
            kb = os.path.getsize(dst_webp_path) / 1024.0
            
    print(f"[{idx}/10] BBC Style Banner Generated: {spec['dst']} | {kb:.1f} KB")

# Cleanup temporary render files
if os.path.exists(temp_html_path):
    os.remove(temp_html_path)
if os.path.exists(temp_png_path):
    os.remove(temp_png_path)

print("\nSuccessfully rendered all 10 banners in BBC News / BBC Hindi style!")
