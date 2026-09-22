# -*- coding: utf-8 -*-
"""
generate_bbc_banners_22_september.py
Renders 10 authentic BBC News / BBC Hindi style featured banners for Google Discover.
Uses headless Chrome for flawless Devanagari font rendering, OpenType ligatures,
and Google Discover compliance (<95KB WebP, 1200x675).
"""

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

BASE_DIR = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
IMG_DIR = os.path.join(BASE_DIR, 'static', 'images', 'news')
BRAIN_DIR = r'C:\Users\caneu\.gemini\antigravity\brain\f0566670-25ee-4739-bb10-e53286d68160'
FALLBACK_HERO = os.path.join(BASE_DIR, 'static', 'images', 'hero', 'sugarcane-field.jpg')

os.makedirs(IMG_DIR, exist_ok=True)

chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
if not os.path.exists(chrome_exe):
    chrome_exe = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

banners = [
    {
        "dst": "up-sugar-mills-perai-satr-2026-27-boiler-pujan-indent-schedule-live-dates.webp",
        "bg": os.path.join(BRAIN_DIR, "sugar_mill_boiler_puja_1788835913647.jpg"),
        "tag": "पेराई सत्र 2026 ⚡",
        "h1": "UP की 120 चीनी मिलों में 25 अक्टूबर से पेराई",
        "h2_html": "शामली, मवाना, दौराला में <span class='sub-highlight'>बॉयलर टेस्टिंग पूरी</span>, इंडेंट शेड्यूल जारी"
    },
    {
        "dst": "ganna-satta-aapatthi-scrutiny-portal-calendar-lock-process-30-september-2026.webp",
        "bg": os.path.join(BRAIN_DIR, "parchi_calendar_1787515212863.jpg"),
        "tag": "सट्टा कैलेंडर ⚡",
        "h1": "20 सितंबर सट्टा आपत्ति: 4.8 लाख आवेदनों की जांच",
        "h2_html": "168 समितियों में स्क्रूटनी तेज, <span class='sub-highlight'>30 सितंबर तक लॉक होगा</span> अंतिम कैलेंडर"
    },
    {
        "dst": "up-ganna-sap-mulya-cabinet-draft-proposal-400-rupees-rate-decision-2026.webp",
        "bg": os.path.join(BRAIN_DIR, "ganna_bhav_600_1787581913979.jpg"),
        "tag": "कैबिनेट फैसला ⚡",
        "h1": "गन्ने का भाव ₹400 प्रति क्विंटल करने की तैयारी",
        "h2_html": "लखनऊ में ड्राफ्ट तैयार: <span class='sub-highlight'>अगेती प्रजाति पर ₹30 की भारी वृद्धि</span> संभव"
    },
    {
        "dst": "agristack-kisan-farmer-registry-id-ganna-satta-ekyc-csc-camp-guidelines-2026.webp",
        "bg": os.path.join(BRAIN_DIR, "agristack_farmer_id_1787550452017.jpg"),
        "tag": "किसान पहचान पत्र ⚡",
        "h1": "गन्ना किसानों के लिए 'फार्मर रजिस्ट्री' अनिवार्य",
        "h2_html": "31 अक्टूबर तक बनाएं <span class='sub-highlight'>11-अंकीय किसान आईडी</span>, CSC पर ई-केवाईसी"
    },
    {
        "dst": "ganna-bakaya-bhugtan-1240-crore-cane-commissioner-recovery-notice-october-2026.webp",
        "bg": os.path.join(BRAIN_DIR, "farmer_payment_bank_1789057969341.jpg"),
        "tag": "सख्त अल्टीमेटम ⚡",
        "h1": "15 अक्टूबर तक ₹1,240 करोड़ बकाया चुकाएं मिलें",
        "h2_html": "गन्ना आयुक्त का कड़ा आदेश: <span class='sub-highlight'>भुगतान न करने पर क्रशिंग लाइसेंस रद्द</span>"
    },
    {
        "dst": "autumn-sugarcane-planting-campaign-co15023-co0118-shahjahanpur-seed-subsidy-2026.webp",
        "bg": os.path.join(BRAIN_DIR, "trench_buwai_bg_1788691027506.jpg"),
        "tag": "शरदकालीन बुवाई ⚡",
        "h1": "शरद बुवाई शुरू: Co-15023 के 50,000 क्विंटल बीज",
        "h2_html": "ट्रेंच विधि से बुवाई पर <span class='sub-highlight'>₹5,000 सरकारी अनुदान</span> • 25% अधिक उपज"
    },
    {
        "dst": "red-rot-disease-co0238-replacement-seed-treatment-trichoderma-advisory-2026.webp",
        "bg": os.path.join(BRAIN_DIR, "news5_red_rot_alert_cover_1787948112904.jpg"),
        "tag": "रोग चेतावनी ⚡",
        "h1": "Co-0238 पर 20% सट्टा कटौती • लाल सड़न चेतावनी",
        "h2_html": "खेत में फंगस फैलने से रोकें: <span class='sub-highlight'>ट्राइकोडर्मा से बीज शोधन</span> 100% अनिवार्य"
    },
    {
        "dst": "sugar-mill-weighbridge-digital-rfid-sealing-ghattoli-prevention-taskforce-2026.webp",
        "bg": os.path.join(BRAIN_DIR, "cctv_weighbridge_bg_1788690778888.jpg"),
        "tag": "घटतौली पर प्रहार ⚡",
        "h1": "800+ खरीद केंद्रों पर RFID डिजिटल कांटे लगेंगे",
        "h2_html": "हेराफेरी रोकने को <span class='sub-highlight'>संयुक्त टास्क फोर्स गठित</span> • 1800-121-3203 हेल्पलाइन"
    },
    {
        "dst": "ethanol-blending-sugar-diversion-40-lakh-tonnes-distillery-farmer-cashflow-2026.webp",
        "bg": os.path.join(BRAIN_DIR, "news9_ethanol_expansion_cover_1787948284345.jpg"),
        "tag": "इथेनॉल क्रांति ⚡",
        "h1": "इथेनॉल के लिए 40 लाख टन चीनी डायवर्जन मंजूर",
        "h2_html": "UP की 45 डिस्टिलरीज को नकदी तरलता, <span class='sub-highlight'>14 दिन में होगा गन्ना भुगतान</span>"
    },
    {
        "dst": "bku-sisauli-mahapanchayat-28-september-rakesh-tikait-ganna-sap-rate-warning-2026.webp",
        "bg": os.path.join(BRAIN_DIR, "mahapanchayat_gic_1788835901105.jpg"),
        "tag": "सिसौली महापंचायत ⚡",
        "h1": "गन्ना भाव पर 28 सितंबर को सिसौली में महापंचायत",
        "h2_html": "राकेश टिकैत की हुंकार: <span class='sub-highlight'>बिना मूल्य घोषित मिलें चलने नहीं देंगे</span>"
    }
]

temp_html_path = os.path.join(IMG_DIR, "_temp_bbc_render.html")
temp_png_path = os.path.join(IMG_DIR, "_temp_bbc_render.png")

print(f"[+] Generating 10 BBC News / BBC Hindi Style Banners for Google Discover...")

for idx, spec in enumerate(banners, 1):
    dst_webp_path = os.path.join(IMG_DIR, spec["dst"])
    bg_img_path = spec["bg"]
    if not os.path.exists(bg_img_path):
        bg_img_path = FALLBACK_HERO
        
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
    height: 420px;
    background: linear-gradient(to top, rgba(0, 0, 0, 0.97) 0%, rgba(0, 0, 0, 0.85) 50%, rgba(0, 0, 0, 0) 100%);
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
    background: rgba(10, 15, 25, 0.90);
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
    bottom: 30px;
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
    font-size: 52px;
    font-weight: 900;
    line-height: 1.18;
    padding: 10px 24px;
    display: inline-block;
    box-shadow: 0 6px 18px rgba(0,0,0,0.8);
    letter-spacing: -0.2px;
    border-radius: 4px;
}}

.bbc-sub-headline {{
    background: #050505;
    color: #ffffff;
    font-size: 35px;
    font-weight: 800;
    line-height: 1.25;
    padding: 8px 22px;
    display: inline-block;
    border-left: 7px solid #facc15;
    box-shadow: 0 6px 18px rgba(0,0,0,0.8);
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
        quality = 84
        im.save(dst_webp_path, 'WEBP', quality=quality, optimize=True)
        kb = os.path.getsize(dst_webp_path) / 1024.0
        while kb > 95.0 and quality > 35:
            quality -= 4
            im.save(dst_webp_path, 'WEBP', quality=quality, optimize=True)
            kb = os.path.getsize(dst_webp_path) / 1024.0
            
    print(f"[{idx}/10] BBC Style Banner Generated: {spec['dst']} ({kb:.1f} KB)")

# Cleanup temporary render files
if os.path.exists(temp_html_path):
    os.remove(temp_html_path)
if os.path.exists(temp_png_path):
    os.remove(temp_png_path)

print("\n[+] All 10 BBC News / BBC Hindi Style Banners generated successfully!")
