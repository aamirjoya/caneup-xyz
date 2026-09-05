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
news_dir = os.path.join(base_dir, 'content', 'news')
img_dir = os.path.join(base_dir, 'static', 'images', 'news')
brain_dir = r'C:\Users\caneu\.gemini\antigravity\brain\f0566670-25ee-4739-bb10-e53286d68160'
real_dir = os.path.join(brain_dir, 'real_photos')

chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
if not os.path.exists(chrome_exe):
    chrome_exe = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

banners_to_render = [
    # 5 September 2026 Morning News
    {
        "banner_img": "today-56-tehsils-24-hour-kisan-fast-western-up-2026.webp",
        "bg_img": os.path.join(real_dir, "rakesh_tikait.jpg"),
        "tag": "आज 56 तहसीलों पर उपवास ⚡",
        "h1": "आज पश्चिमी UP की 56 तहसीलों पर उपवास",
        "h2_html": "नलकूपों पर स्मार्ट मीटर और ₹450 भाव पर <span class='sub-highlight'>किसानों का 24 घंटे का बड़ा पहरा</span>"
    },
    {
        "banner_img": "up-ganna-satta-correction-day-5-15-september-deadline-2026.webp",
        "bg_img": os.path.join(brain_dir, "ganna_ghosna_patra_1787582617828.jpg"),
        "tag": "15 सितंबर लास्ट डेट ⚡",
        "h1": "15 सितंबर से पहले सुधारें सट्टे की गलतियां",
        "h2_html": "मुजफ्फरनगर-मेरठ सहित 168 समितियों में <span class='sub-highlight'>शाम 7 बजे तक खुले हैं विशेष काउंटर</span>"
    },
    {
        "banner_img": "shamli-hapur-bijnor-sugar-mills-1936-crore-high-court-recovery-2026.webp",
        "bg_img": os.path.join(real_dir, "high_court_lucknow.jpg"),
        "tag": "बकाया भुगतान राहत ⚡",
        "h1": "चीनी गोदाम सील: 15 अक्टूबर तक भुगतान",
        "h2_html": "शामली, हापुड़ व बिजनौर के किसानों के लिए <span class='sub-highlight'>हाईकोर्ट के आदेश के बाद बड़ी राहत</span>"
    },
    {
        "banner_img": "eganna-app-v6-2-live-parchi-satta-tracking-guide-2026.webp",
        "bg_img": os.path.join(brain_dir, "eganna_v6_app_1787581898745.jpg"),
        "tag": "eGanna ऐप गाइड ⚡",
        "h1": "eGanna App: लाइव पर्ची व सट्टा देखें",
        "h2_html": "पासवर्ड भूल गए तो मात्र 2 मिनट में <span class='sub-highlight'>मोबाइल ओटीपी से ऐसे करें रीसेट</span>"
    },
    {
        "banner_img": "ganna-ghosna-patra-online-declaration-30-september-deadline-2026.webp",
        "bg_img": os.path.join(brain_dir, "satta_pre_cal_1787581882990.jpg"),
        "tag": "30 सितंबर अंतिम तिथि ⚡",
        "h1": "ऑनलाइन घोषणा पत्र कैसे भरें",
        "h2_html": "30 सितंबर लास्ट डेट: <span class='sub-highlight'>बिना घोषणा पत्र के ब्लॉक हो जाएगा सट्टा</span>"
    },
    {
        "banner_img": "co15023-colk15201-certified-seed-booking-50-rupees-subsidy-2026.webp",
        "bg_img": os.path.join(brain_dir, "cos_17231_variety_1787582225246.jpg"),
        "tag": "बीज सब्सिडी ⚡",
        "h1": "Co-15023 व CoLk-15201 बीज बुकिंग",
        "h2_html": "₹50 प्रति क्विंटल सरकारी सब्सिडी: <span class='sub-highlight'>शाहजहांपुर शोध फार्म से ऐसे लें टोकन</span>"
    },
    {
        "banner_img": "800-weighbridge-digital-sealing-farmer-vigilance-committee-2026.webp",
        "bg_img": os.path.join(brain_dir, "chandanpur_mill_cover_1787946872076.jpg"),
        "tag": "घटतौली पर लगाम ⚡",
        "h1": "800 गन्ना कांटों पर लगी बारकोड सील",
        "h2_html": "घटतौली पर पूर्ण रोक: <span class='sub-highlight'>किसानों की 3-सदस्यीय सतर्कता कमेटी को मिले अधिकार</span>"
    },
    {
        "banner_img": "autumn-trench-sugarcane-pusa-mustard-intercropping-40000-profit-2026.webp",
        "bg_img": os.path.join(brain_dir, "trench_buwai_1787582649543.jpg"),
        "tag": "डबल मुनाफा ⚡",
        "h1": "गन्ने के साथ सरसों की ट्रेंच बुवाई",
        "h2_html": "90 दिन में कमाएं अतिरिक्त ₹40,000: <span class='sub-highlight'>पश्चिमी UP के किसानों के लिए डबल मुनाफा फॉर्मूला</span>"
    },
    {
        "banner_img": "50-buffer-dap-fertilizer-hubs-cooperative-dispatch-up-2026.webp",
        "bg_img": os.path.join(brain_dir, "news8_harvester_subsidy_cover_1787948234294.jpg"),
        "tag": "खाद सप्लाई तेज ⚡",
        "h1": "50 बफर हब से DAP खाद की सप्लाई शुरू",
        "h2_html": "समितियों पर पहुंचे 150 ट्रक: <span class='sub-highlight'>₹1,350 सरकारी दर पर ऐसे पाएं खाद</span>"
    },
    {
        "banner_img": "8-september-muzaffarnagar-gic-ground-mahapanchayat-preparations-2026.webp",
        "bg_img": os.path.join(real_dir, "rakesh_tikait.jpg"),
        "tag": "8 सितंबर महापंचायत ⚡",
        "h1": "8 सितंबर मुजफ्फरनगर महापंचायत की तैयारी",
        "h2_html": "GIC मैदान में जुटेंगे 1 लाख किसान: <span class='sub-highlight'>खाप चौधरियों ने दिया 'गांव-गांव कूच' का नारा</span>"
    },
    
    # 4 September 2026 Morning News
    {
        "banner_img": "allahabad-high-court-strict-order-1936-crore-cane-dues-recovery-2026.webp",
        "bg_img": os.path.join(real_dir, "high_court_lucknow.jpg"),
        "tag": "हाईकोर्ट आदेश ⚡",
        "h1": "₹1,936 करोड़ गन्ना बकाए पर हाईकोर्ट सख्त",
        "h2_html": "सभी DM वसूली तेज करें, <span class='sub-highlight'>15 अक्टूबर तक मांगी प्रगति रिपोर्ट</span>"
    },
    {
        "banner_img": "simbhaoli-brijnathpur-sugar-mills-100-crore-clearance-order-2026.webp",
        "bg_img": os.path.join(brain_dir, "sugar_mill_payment_1787489145600.jpg"),
        "tag": "मिल भुगतान ⚡",
        "h1": "सिंभावली मिलों पर ₹100 करोड़ भुगतान का आदेश",
        "h2_html": "15 अक्टूबर से पहले होगा भुगतान, <span class='sub-highlight'>किसानों को मिली सर्वोच्च प्राथमिकता</span>"
    },
    {
        "banner_img": "sp-chief-akhilesh-yadav-promises-24-hour-cane-payment-2026.webp",
        "bg_img": os.path.join(real_dir, "akhilesh_yadav.jpg"),
        "tag": "बड़ा सियासी दांव ⚡",
        "h1": "24 घंटे में गन्ना भुगतान का बड़ा चुनावी वादा",
        "h2_html": "सपा प्रमुख अखिलेश यादव का ऐलान: <span class='sub-highlight'>तौल होते ही खाते में जाएगा पैसा</span>"
    },
    {
        "banner_img": "cm-yogi-cane-review-zero-arrears-order-september-20-2026.webp",
        "bg_img": os.path.join(brain_dir, "cm_yogi_sugar_review_1787488894424.jpg"),
        "tag": "CM योगी का आदेश ⚡",
        "h1": "20 सितंबर तक सभी मिलों का बकाया शून्य करें",
        "h2_html": "CM योगी का सख्त फरमान: <span class='sub-highlight'>लापरवाही पर DM और चीनी मिल प्रबंधन नपेंगे</span>"
    },
    {
        "banner_img": "upneda-approves-18-new-cbg-plants-sugarcane-pressmud-2026.webp",
        "bg_img": os.path.join(brain_dir, "biopolymer_plant_1787550481072.jpg"),
        "tag": "बायोगैस क्रांति ⚡",
        "h1": "गन्ने की मैली से बनेगी बायो-सीएनजी",
        "h2_html": "UP में ₹720 करोड़ के 18 नए CBG प्लांट्स, <span class='sub-highlight'>किसानों को ₹2/किग्रा में खाद</span>"
    },
    {
        "banner_img": "yogi-chini-stock-esma-2026.webp",
        "bg_img": os.path.join(brain_dir, "yogi_sugar_esma_1787564910606.jpg"),
        "tag": "CM योगी एक्शन ⚡",
        "h1": "179 लाख क्विंटल चीनी का रिकॉर्ड स्टॉक",
        "h2_html": "जमाखोरों पर लगेगा ESMA कानून: <span class='sub-highlight'>दुकानदारों पर 400 टन की सख्त सीमा</span>"
    }
]

temp_html = os.path.join(img_dir, "_temp_real_render.html")
temp_png = os.path.join(img_dir, "_temp_real_render.png")

print(f"Rendering {len(banners_to_render)} Banners with REAL topic photos...")

for idx, p in enumerate(banners_to_render, 1):
    dst_webp = os.path.join(img_dir, p["banner_img"])
    bg_img_path = p["bg_img"]
    if not os.path.exists(bg_img_path):
        bg_img_path = os.path.join(brain_dir, "ws_sugar_mills_1787597400680.jpg")
        
    with open(bg_img_path, 'rb') as f:
        bg_b64 = base64.b64encode(f.read()).decode('utf-8')
        
    html = f"""<!DOCTYPE html>
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
.dark-gradient {{
    position: absolute;
    bottom: 0;
    left: 0;
    width: 1200px;
    height: 420px;
    background: linear-gradient(to top, rgba(0, 0, 0, 0.98) 0%, rgba(0, 0, 0, 0.82) 48%, rgba(0, 0, 0, 0) 100%);
    z-index: 2;
}}
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
.bbc-tag {{
    position: absolute;
    top: 28px;
    right: 36px;
    background: rgba(0, 0, 0, 0.85);
    border-left: 5px solid #bb1919;
    color: #ffffff;
    font-size: 22px;
    font-weight: 800;
    padding: 6px 18px;
    z-index: 10;
    backdrop-filter: blur(8px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.6);
}}
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
    font-size: 48px;
    font-weight: 900;
    line-height: 1.16;
    padding: 8px 22px;
    display: inline-block;
    box-shadow: 0 6px 16px rgba(0,0,0,0.8);
    letter-spacing: -0.2px;
}}
.bbc-sub-headline {{
    background: #000000;
    color: #ffffff;
    font-size: 32px;
    font-weight: 800;
    line-height: 1.25;
    padding: 6px 20px;
    display: inline-block;
    border-left: 6px solid #facc15;
    box-shadow: 0 6px 16px rgba(0,0,0,0.8);
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
        <div class='bbc-news-box'>UP KISAN</div>
    </div>
    
    <div class='bbc-tag'>{p['tag']}</div>
    
    <div class='bbc-content-wrapper'>
        <div class='bbc-main-headline'>{p['h1']}</div>
        <div class='bbc-sub-headline'>{p['h2_html']}</div>
    </div>
</div>
</body>
</html>
"""
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(html)
        
    cmd = [
        chrome_exe,
        '--headless=new',
        '--disable-gpu',
        '--hide-scrollbars',
        '--window-size=1200,675',
        f'--screenshot={temp_png}',
        f'file:///{temp_html}'
    ]
    subprocess.run(cmd, check=True)
    
    with Image.open(temp_png) as im:
        im = im.crop((0, 0, 1200, 675))
        quality = 82
        im.save(dst_webp, 'WEBP', quality=quality, optimize=True)
        kb = os.path.getsize(dst_webp) / 1024.0
        while kb > 95.0 and quality > 35:
            quality -= 5
            im.save(dst_webp, 'WEBP', quality=quality, optimize=True)
            kb = os.path.getsize(dst_webp) / 1024.0
            
    print(f"[{idx}/{len(banners_to_render)}] Rendered Real Photo Banner: {p['banner_img']} ({kb:.1f} KB)")

if os.path.exists(temp_html):
    os.remove(temp_html)
if os.path.exists(temp_png):
    os.remove(temp_png)

print("\nAll Real Photo Banners rendered successfully!")
