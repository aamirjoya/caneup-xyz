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
posts_dir = os.path.join(base_dir, 'content', 'posts')
img_dir = os.path.join(base_dir, 'static', 'images', 'blog')
brain_dir = r'C:\Users\caneu\.gemini\antigravity\brain\f0566670-25ee-4739-bb10-e53286d68160'

chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
if not os.path.exists(chrome_exe):
    chrome_exe = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

# 10 Top-Priority Cornerstone Blog Guides
cornerstone_posts = [
    {
        "slug": "ganna-parchi-calendar-2026-27-online-check-step-by-step",
        "title": "गन्ना पर्ची कैलेंडर 2026-27 कैसे देखें — enquiry.caneup.in पर 3 सबसे आसान तरीके (Step-by-Step Guide)",
        "desc": "गन्ना पर्ची कैलेंडर 2026-27 ऑनलाइन देखने का पूरा तरीका। enquiry.caneup.in पोर्टल, eGanna ऐप और SMS के जरिए 12 पखवाड़े का कैलेंडर, बेसिक सट्टा कोटा और सप्लाई टिकट कैसे चेक करें।",
        "date": "2026-08-31T18:00:00+05:30",
        "categories": ["CaneUp Guide", "Parchi Calendar"],
        "tags": ["गन्ना पर्ची कैलेंडर", "CaneUp Enquiry", "eGanna App", "गन्ना सट्टा 2026", "UP Sugarcane"],
        "keywords": ["ganna parchi calendar kaise dekhe", "गन्ना पर्ची कैलेंडर 2026-27", "enquiry caneup in ganna parchi", "ganna calendar 12 pakhwada", "ganna pre calendar 2026-27"],
        "banner_img": "ganna-parchi-calendar-2026-27-guide.webp",
        "bg_img": os.path.join(brain_dir, "satta_pre_cal_1787581882990.jpg"),
        "tag": "संपूर्ण गाइड ⚡",
        "h1": "गन्ना पर्ची कैलेंडर 2026-27 कैसे देखें?",
        "h2_html": "enquiry.caneup.in पर <span class='sub-highlight'>12 पखवाड़े का कैलेंडर</span> व सट्टा चेक करें"
    },
    {
        "slug": "ganna-bhugtan-status-check-online-14-din-niyam-2026",
        "title": "गन्ना भुगतान स्टेटस कैसे चेक करें 2026 — 14 दिन नियम, 15% ब्याज क्लेम व मिल-वार पेमेंट स्थिति",
        "desc": "उत्तर प्रदेश में गन्ने का बकाया भुगतान ऑनलाइन कैसे चेक करें। 14 दिन में भुगतान का कानूनी नियम, 15% विलंबित ब्याज क्लेम करने की प्रक्रिया और टोल-फ्री हेल्पलाइन नंबर।",
        "date": "2026-08-31T18:30:00+05:30",
        "categories": ["CaneUp Guide", "Ganna Bhugtan"],
        "tags": ["गन्ना भुगतान", "Cane Payment Status", "14 Din Niyam", "Sugar Mill Payment", "15 Percent Byaj"],
        "keywords": ["ganna bhugtan status kaise check kare", "ganna payment check online up", "ganna bakaya bhugtan 15 percent byaj", "mill wise ganna payment status"],
        "banner_img": "ganna-bhugtan-status-check-2026.webp",
        "bg_img": os.path.join(brain_dir, "sugar_mill_payment_1787489145600.jpg"),
        "tag": "भुगतान गाइड ⚡",
        "h1": "गन्ना भुगतान स्टेटस 2026: कैसे चेक करें?",
        "h2_html": "14 दिन का कानूनी नियम व <span class='sub-highlight'>15% ब्याज क्लेम</span> करने का पूरा तरीका"
    },
    {
        "slug": "up-ganna-sap-rate-2026-27-bhav-suchi-tulna",
        "title": "यूपी गन्ना मूल्य (SAP Rate) 2026-27 — अगेती व सामान्य प्रजाति भाव सूची, लागत विश्लेषण व तुलना",
        "desc": "पेराई सत्र 2026-27 के लिए उत्तर प्रदेश में गन्ने का नया राज्य परामर्शित मूल्य (SAP)। अगेती और सामान्य गन्ने का भाव, उत्पादन लागत और हरियाणा-पंजाब से विस्तृत तुलना।",
        "date": "2026-08-31T19:00:00+05:30",
        "categories": ["MSP Rate", "Ganna News"],
        "tags": ["गन्ना मूल्य 2026-27", "UP Ganna SAP Rate", "गन्ने का भाव", "Sugar Mill Crushing", "Kisan MSP"],
        "keywords": ["गन्ना मूल्य 2026-27 उत्तर प्रदेश", "up ganna sap rate 2026-27", "ganna ka rate kya hai 2026", "sap vs frp rate 2026"],
        "banner_img": "up-ganna-sap-rate-2026-27-guide.webp",
        "bg_img": os.path.join(brain_dir, "ws_bhav_600_1787597306153.jpg"),
        "tag": "भाव विश्लेषण ⚡",
        "h1": "यूपी गन्ना मूल्य 2026-27: क्या होगा नया भाव?",
        "h2_html": "अगेती व सामान्य किस्मों की <span class='sub-highlight'>भाव सूची व उत्पादन लागत</span> विश्लेषण"
    },
    {
        "slug": "eganna-app-download-latest-version-login-problem-solution-2026",
        "title": "eGanna App Download 2026 — Latest Version 6.0 | Login, Session Expired व पर्ची देखने का समाधान",
        "desc": "eGanna App का नया वर्जन 6.0 डाउनलोड करें। ऐप में लॉगिन समस्या, Session Expired एरर ठीक करने, किसान कोड खोजने और पर्ची नोटिफिकेशन ऑन करने का स्टेप-बाय-स्टेप तरीका।",
        "date": "2026-08-31T19:30:00+05:30",
        "categories": ["eGanna App", "Tech Guide"],
        "tags": ["eGanna App Download", "eGanna Version 6", "Login Problem Solution", "Grower Code", "Parchi App"],
        "keywords": ["eganna app download latest version 2026", "eganna app login session expired problem", "eganna app se parchi kaise nikale", "eganna v6 apk download"],
        "banner_img": "eganna-app-download-latest-version-2026.webp",
        "bg_img": os.path.join(brain_dir, "ws_eganna_v6_1787597294561.jpg"),
        "tag": "ऐप गाइड ⚡",
        "h1": "eGanna App Version 6.0 कैसे डाउनलोड करें?",
        "h2_html": "Session Expired एरर ठीक करें व <span class='sub-highlight'>मोबाइल पर पर्ची देखें</span>"
    },
    {
        "slug": "ganne-mein-lal-sadan-red-rot-rog-ka-pakka-ilaj-2026",
        "title": "गन्ने में लाल सड़न (Red Rot) रोग का पक्का इलाज 2026 — 7 वैज्ञानिक उपाय, दवा स्प्रे व बीज शोधन",
        "desc": "गन्ने में लाल सड़न (रेड रॉट) रोग के लक्षण, कारण और 100% रोकथाम के 7 वैज्ञानिक उपाय। हॉट वाटर ट्रीटमेंट, ट्राइकोडर्मा का प्रयोग और अनुशंसित फफूंदनाशक दवाओं की सही खुराक।",
        "date": "2026-08-31T20:00:00+05:30",
        "categories": ["Ganna Kheti", "Disease Management"],
        "tags": ["लाल सड़न रोग", "Red Rot Treatment", "ट्राइकोडर्मा", "गन्ना बीज शोधन", "Crop Protection"],
        "keywords": ["ganne mein lal sadan rog ka ilaj", "red rot disease treatment sugarcane", "top borer keetnashak spray dosage", "streptocycline pyraclostrobin dosage"],
        "banner_img": "ganne-mein-lal-sadan-red-rot-ilaj-2026.webp",
        "bg_img": os.path.join(brain_dir, "ws_red_rot_1787597358502.jpg"),
        "tag": "फसल सुरक्षा ⚡",
        "h1": "गन्ने में लाल सड़न (Red Rot) का पक्का इलाज",
        "h2_html": "हॉट वाटर बीज शोधन व <span class='sub-highlight'>ट्राइकोडर्मा के 7 अचूक उपाय</span>"
    },
    {
        "slug": "co-0238-replacement-top-5-ganna-kismen-2026",
        "title": "Co-0238 की जगह लगाएं ये 5 उन्नत गन्ना किस्में — 500 कुंतल प्रति एकड़ पैदावार और 13% चीनी रिकवरी",
        "desc": "Co-0238 में लाल सड़न के प्रकोप के बाद भारतीय गन्ना अनुसंधान संस्थान (IISR) द्वारा अनुमोदित 5 श्रेष्ठ गन्ना किस्में (Co-15023, CoS-17231, CoLk-14201)। पैदावार, रिकवरी व बीज नर्सरी गाइड।",
        "date": "2026-08-31T20:30:00+05:30",
        "categories": ["Ganna Kheti", "Seed Varieties"],
        "tags": ["Co-0238 Replacement", "Co-15023", "CoS-17231", "CoLk-14201", "उन्नत गन्ना किस्में"],
        "keywords": ["co 0238 replacement varieties", "co 15023 ganna kism paidwar", "cos 17231 beej nursery booking", "colk 14201 vs co 0118"],
        "banner_img": "co-0238-replacement-top-5-varieties-2026.webp",
        "bg_img": os.path.join(brain_dir, "ws_cos17231_1787597414786.jpg"),
        "tag": "उन्नत किस्में ⚡",
        "h1": "Co-0238 की जगह लगाएं 5 श्रेष्ठ किस्में",
        "h2_html": "<span class='sub-highlight'>500 कुंतल/एकड़ पैदावार</span> व लाल सड़न से 100% सुरक्षा"
    },
    {
        "slug": "sharadkalin-ganna-trench-buwai-sarso-aalu-intercropping-guide-2026",
        "title": "शरदकालीन गन्ना बुवाई ट्रेंच विधि 2026 — 4.5 फीट दूरी, सरसों-आलू सह-फसल से ₹30,000 अतिरिक्त आय",
        "desc": "शरदकालीन गन्ना बुवाई ट्रेंच विधि से कैसे करें। 4.5 से 5 फीट की दूरी पर सिंगल बड बुवाई, सरसों और आलू की इंटरक्रॉपिंग और प्रति एकड़ 550 कुंतल बंपर पैदावार लेने का पूरा फॉर्मूला।",
        "date": "2026-08-31T21:00:00+05:30",
        "categories": ["Ganna Kheti", "Trench Method"],
        "tags": ["शरदकालीन गन्ना बुवाई", "ट्रेंच विधि", "सरसों सह-फसल", "Intercropping", "Organic Farming"],
        "keywords": ["sharadkalin ganna trench buwai method", "ganne ke sath sarso intercropping", "ganna trench vidhi 4-5 feet spacing", "ganna paidwar per acre 500 quintal"],
        "banner_img": "sharadkalin-trench-buwai-intercropping-2026.webp",
        "bg_img": os.path.join(brain_dir, "trench_buwai_1787582649543.jpg"),
        "tag": "बुवाई तकनीक ⚡",
        "h1": "शरदकालीन ट्रेंच बुवाई: 500 कुंतल पैदावार",
        "h2_html": "सरसों व आलू सह-फसल से <span class='sub-highlight'>₹30,000 प्रति एकड़ अतिरिक्त आय</span>"
    },
    {
        "slug": "pm-kusum-yojana-up-solar-pump-70-percent-subsidy-online-apply-2026",
        "title": "PM कुसुम योजना यूपी 2026 — सोलर पंप पर 70% सरकारी सब्सिडी, ऑनलाइन आवेदन व टोकन बुकिंग प्रक्रिया",
        "desc": "उत्तर प्रदेश में पीएम कुसुम योजना के तहत 3HP, 5HP और 7.5HP सोलर सिंचाई पंप पर 70% सब्सिडी कैसे पाएं। upagriculture.com पर ऑनलाइन टोकन बुकिंग, आवश्यक दस्तावेज और लागत विवरण।",
        "date": "2026-08-31T21:30:00+05:30",
        "categories": ["Sarkari Yojana", "Solar Subsidy"],
        "tags": ["PM Kusum Yojana", "Solar Pump Subsidy UP", "70 Percent Anudan", "Kisan Sinchai", "Token Booking"],
        "keywords": ["pm kusum solar pump 70 percent subsidy up", "up solar pump online registration 2026", "3hp 5hp 7.5hp solar pump cost", "upagriculture token booking"],
        "banner_img": "pm-kusum-solar-pump-70-subsidy-2026.webp",
        "bg_img": os.path.join(brain_dir, "sarkari_yojana_1787514939813.jpg"),
        "tag": "सरकारी योजना ⚡",
        "h1": "PM कुसुम योजना: सोलर पंप पर 70% सब्सिडी",
        "h2_html": "3HP, 5HP पंप की लागत, <span class='sub-highlight'>टोकन बुकिंग व ऑनलाइन अप्लाई</span>"
    },
    {
        "slug": "kisan-credit-card-kcc-ganna-kisan-3-lakh-loan-4-percent-2026",
        "title": "गन्ना किसानों को KCC लोन मात्र 4% ब्याज पर — ₹3 लाख तक बिना गारंटी ऋण, पात्रता व आवेदन फॉर्मूला",
        "desc": "गन्ना किसानों के लिए किसान क्रेडिट कार्ड (KCC) लोन 2026। नाबार्ड व सरकार की 3% ब्याज छूट से प्रभावी 4% दर पर ऋण, स्केल ऑफ फाइनेंस (प्रति एकड़ ₹50,000 लिमिट) और बैंक आवेदन प्रक्रिया।",
        "date": "2026-08-31T22:00:00+05:30",
        "categories": ["Sarkari Yojana", "Kisan Finance"],
        "tags": ["KCC Loan 2026", "Kisan Credit Card", "4 Percent Interest", "Ganna Kisan Loan", "SBI KCC"],
        "keywords": ["kisan credit card ganna kisan 3 lakh loan", "kcc loan 4 percent interest scheme", "kcc online apply sbi pnb cooperative bank", "scale of finance sugarcane"],
        "banner_img": "kcc-loan-ganna-kisan-4-percent-2026.webp",
        "bg_img": os.path.join(brain_dir, "ws_kcc_loan_cover_1787906338029.jpg"),
        "tag": "किसान ऋण ⚡",
        "h1": "गन्ना किसानों को KCC लोन मात्र 4% ब्याज पर",
        "h2_html": "₹3 लाख तक फसली ऋण, <span class='sub-highlight'>स्केल ऑफ फाइनेंस व आसान आवेदन</span>"
    },
    {
        "slug": "krishi-yantra-anudan-fpo-farm-machinery-bank-80-percent-subsidy-2026",
        "title": "गन्ना कृषि यंत्र बैंक पर 80% सरकारी अनुदान — FPO व किसान समूहों को ₹12 लाख तक सब्सिडी (Apply Guide)",
        "desc": "उत्तर प्रदेश कृषि यंत्र अनुदान योजना 2026। गन्ना कटाई मशीन, मल्चर, ट्रैश कटर और रोटावेटर के कस्टम हायरिंग सेंटर (CHC) की स्थापना पर 80% सरकारी अनुदान और ई-लॉटरी टोकन व्यवस्था।",
        "date": "2026-08-31T22:30:00+05:30",
        "categories": ["Sarkari Yojana", "Machinery Grant"],
        "tags": ["कृषि यंत्र अनुदान", "Farm Machinery Bank", "80 Percent Subsidy", "FPO Grant", "Ganna Harvester"],
        "keywords": ["krishi yantra bank fpo 80 percent grant", "ganna katai machine subsidy 80 percent", "up agriculture token booking 2026", "custom hiring center up"],
        "banner_img": "krishi-yantra-bank-80-subsidy-2026.webp",
        "bg_img": os.path.join(brain_dir, "news8_harvester_subsidy_cover_1787948234294.jpg"),
        "tag": "मशीनरी ग्रांट ⚡",
        "h1": "गन्ना कृषि यंत्र बैंक पर 80% सरकारी अनुदान",
        "h2_html": "ट्रैश कटर, मल्चर व हार्वेस्टर पर <span class='sub-highlight'>₹12 लाख तक सब्सिडी</span>"
    }
]

# Step 1: Render BBC-Style Banners for all 10 posts
temp_html = os.path.join(img_dir, "_temp_blog_render.html")
temp_png = os.path.join(img_dir, "_temp_blog_render.png")

for idx, p in enumerate(cornerstone_posts, 1):
    dst_webp_path = os.path.join(img_dir, p["banner_img"])
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

/* BBC Header / Brand Badge */
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
        <div class='bbc-news-box'>GUIDE</div>
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
        im.save(dst_webp_path, 'WEBP', quality=quality, optimize=True)
        kb = os.path.getsize(dst_webp_path) / 1024.0
        while kb > 95.0 and quality > 35:
            quality -= 5
            im.save(dst_webp_path, 'WEBP', quality=quality, optimize=True)
            kb = os.path.getsize(dst_webp_path) / 1024.0
            
    print(f"[{idx}/10] Rendered BBC Banner: {p['banner_img']} | {kb:.1f} KB")

# Cleanup temporary render files
if os.path.exists(temp_html):
    os.remove(temp_html)
if os.path.exists(temp_png):
    os.remove(temp_png)

print("\nAll 10 BBC Style Banners rendered successfully!")
