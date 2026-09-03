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

chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
if not os.path.exists(chrome_exe):
    chrome_exe = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

articles_data = [
    {
        "slug": "cm-yogi-cane-review-zero-arrears-order-september-20-2026",
        "title": "CM योगी का कड़ा फरमान — 20 सितंबर तक सभी 120 चीनी मिलों का बकाया शून्य करें, कोताही पर DM नपेंगे",
        "desc": "मुख्यमंत्री योगी आदित्यनाथ ने आज लखनऊ में उच्चस्तरीय बैठक कर पिछले पेराई सत्र का शेष बकाया 20 सितंबर तक शत-प्रतिशत चुकाने के निर्देश दिए। समय पर भुगतान न करने वाली मिलों पर आरसी जारी होगी।",
        "date": "2026-09-03T11:00:00+05:30",
        "categories": ["Breaking News", "Ganna Bhugtan"],
        "tags": ["CM योगी आदेश", "20 September Deadline", "Zero Arrears UP", "चीनी मिल बकाया", "CaneUp News"],
        "keywords": ["cm yogi cane review zero arrears order september 20 2026", "yogi adityanath ganna bhugtan deadline 20 september", "dco dm review sugarcane payment up", "sugar mill 100 percent clearance order 2026"],
        "banner_img": "cm-yogi-cane-review-zero-arrears-order-september-20-2026.webp",
        "bg_img": os.path.join(brain_dir, "news4_bhugtan_3800cr_cover_1787948066221.jpg"),
        "tag": "सीएम आदेश ⚡",
        "h1": "20 सितंबर तक चीनी मिलों का बकाया शून्य करें",
        "h2_html": "CM योगी का कड़ा फरमान: <span class='sub-highlight'>लापरवाही पर नपेंगे संबंधित डीएम</span>"
    },
    {
        "slug": "cabinet-approves-1500-crore-buffer-stock-subsidy-sugar-mills-2026",
        "title": "चीनी मिलों को ₹1,500 करोड़ की बफर स्टॉक सब्सिडी स्वीकृत — किसानों के त्वरित भुगतान में मिलेगी मदद",
        "desc": "केंद्रीय मंत्रिमंडल ने चीनी उद्योग के लिए 40 लाख मीट्रिक टन बफर स्टॉक की त्रैमासिक वहन लागत (कैरिंग कॉस्ट) सब्सिडी के तहत ₹1,500 करोड़ जारी करने को मंजूरी दे दी है।",
        "date": "2026-09-03T12:00:00+05:30",
        "categories": ["Breaking News", "Sugar Industry"],
        "tags": ["बफर स्टॉक सब्सिडी 1500 करोड़", "Cabinet Decision", "Sugar Industry Liquidity", "Kisan Payment", "Sugar Policy"],
        "keywords": ["cabinet approves 1500 crore buffer stock subsidy sugar mills 2026", "buffer stock carrying cost subsidy sugar mills", "dfpd sugar industry financial support", "sugar mill liquidity farmer payment 2026"],
        "banner_img": "cabinet-approves-1500-crore-buffer-stock-subsidy-sugar-mills-2026.webp",
        "bg_img": os.path.join(brain_dir, "ws_sugar_mills_1787597400680.jpg"),
        "tag": "कैबिनेट फैसला ⚡",
        "h1": "चीनी मिलों को ₹1,500 करोड़ की बफर सब्सिडी",
        "h2_html": "किसानों के समयबद्ध भुगतान के लिए <span class='sub-highlight'>केंद्र ने जारी किए फंड</span>"
    },
    {
        "slug": "shamli-upper-doab-deposits-45-crore-escrow-account-2026",
        "title": "प्रशासनिक सख्ती का असर — अपर दोआब शुगर मिल शामली ने एस्क्रो खाते में जमा कराए ₹45 करोड़",
        "desc": "शामली डीएम के कड़े रुख और चीनी गोदामों की निगरानी के बाद आज अपर दोआब शुगर मिल ने चीनी और शीरा बिक्री से प्राप्त ₹45 करोड़ सीधे किसानों के भुगतान एस्क्रो खाते में ट्रांसफर किए।",
        "date": "2026-09-03T13:00:00+05:30",
        "categories": ["Breaking News", "Ganna Bhugtan"],
        "tags": ["शामली अपर दोआब 45 करोड़", "Escrow Account Deposit", "Upper Doab Shamli", "गन्ना भुगतान", "CaneUp News"],
        "keywords": ["shamli upper doab deposits 45 crore escrow account 2026", "upper doab sugar mill shamli payment update", "dco shamli escrow account release", "shamli ganna kisan payment news 3 september"],
        "banner_img": "shamli-upper-doab-deposits-45-crore-escrow-account-2026.webp",
        "bg_img": os.path.join(brain_dir, "sugar_mill_payment_1787489145600.jpg"),
        "tag": "भुगतान अपडेट ⚡",
        "h1": "अपर दोआब मिल ने एस्क्रो खाते में डाले ₹45 करोड़",
        "h2_html": "प्रशासनिक सख्ती के बाद <span class='sub-highlight'>किसानों के खातों में भेजा जा रहा पैसा</span>"
    },
    {
        "slug": "upneda-approves-18-new-cbg-plants-sugarcane-pressmud-2026",
        "title": "गन्ने की मैली (प्रेसमड) से बनेगी बायोगैस — यूपी में ₹720 करोड़ के 18 नए CBG प्लांट्स को हरी झंडी",
        "desc": "यूपीनेडा ने पश्चिमी और मध्य यूपी की 18 चीनी मिलों में प्रेसमड से कंप्रेस्ड बायोगैस (CBG) बनाने के संयंत्रों को अंतिम तकनीकी मंजूरी दे दी है। किसानों को जैविक खाद और वाहन ईंधन दोनों मिलेगा।",
        "date": "2026-09-03T14:00:00+05:30",
        "categories": ["Breaking News", "Sugar Industry"],
        "tags": ["बायोगैस CBG प्लांट 18", "Pressmud to Biogas", "UPNEDA 720 Crore", "Green Bioenergy", "CaneUp News"],
        "keywords": ["upneda approves 18 new cbg plants sugarcane pressmud 2026", "compressed biogas plant sugar mill pressmud up", "satat yojana cbg sugar mills western up", "fermented organic manure fom sugarcane"],
        "banner_img": "upneda-approves-18-new-cbg-plants-sugarcane-pressmud-2026.webp",
        "bg_img": os.path.join(brain_dir, "news9_ethanol_expansion_cover_1787948284345.jpg"),
        "tag": "बायोगैस क्रांति ⚡",
        "h1": "गन्ने की मैली से बनेगी CBG कंप्रेस्ड बायोगैस",
        "h2_html": "यूपी में ₹720 करोड़ के <span class='sub-highlight'>18 नए आधुनिक प्लांट्स को मंजूरी</span>"
    },
    {
        "slug": "icar-iisr-releases-colk-15201-red-rot-resistant-sugarcane-variety-2026",
        "title": "गन्ना किसानों को बड़ा तोहफा — ICAR ने अधिसूचित की नई लाल सड़न रोधी प्रजाति CoLk-15201 (इक्षु-7)",
        "desc": "भारतीय गन्ना अनुसंधान संस्थान लखनऊ ने Co-0238 के बेहतर विकल्प के रूप में CoLk-15201 को औपचारिक रूप से जारी किया है। इसमें 13.5% चीनी रिकवरी और 520 कुंतल प्रति एकड़ पैदावार की क्षमता है।",
        "date": "2026-09-03T15:00:00+05:30",
        "categories": ["Breaking News", "Ganna Guide"],
        "tags": ["CoLk 15201 इक्षु 7", "New Sugarcane Variety", "Red Rot Resistant", "ICAR IISR Lucknow", "High Yield Cane"],
        "keywords": ["icar iisr releases colk 15201 red rot resistant sugarcane variety 2026", "colk 15201 ikshu 7 variety notification up", "co 0238 replacement early variety", "sugar recovery yield colk 15201"],
        "banner_img": "icar-iisr-releases-colk-15201-red-rot-resistant-sugarcane-variety-2026.webp",
        "bg_img": os.path.join(brain_dir, "ws_cos17231_1787597414786.jpg"),
        "tag": "नई प्रजाति ⚡",
        "h1": "ICAR ने जारी की नई प्रजाति CoLk-15201",
        "h2_html": "लाल सड़न प्रतिरोधी व 13.5% रिकवरी, <span class='sub-highlight'>Co-0238 का मजबूत विकल्प</span>"
    },
    {
        "slug": "punjab-sugarcane-board-recommends-410-sap-2026",
        "title": "पंजाब गन्ना नियंत्रण बोर्ड की सिफारिश — आगामी पेराई सत्र के लिए ₹410 प्रति क्विंटल हो गन्ना भाव",
        "desc": "हरियाणा के ₹405 की मंजूरी के बाद पंजाब गन्ना नियंत्रण बोर्ड ने मुख्यमंत्री भगवंत मान को अगेती प्रजाति का भाव ₹410 प्रति क्विंटल घोषित करने का औपचारिक प्रस्ताव भेजा है।",
        "date": "2026-09-03T16:00:00+05:30",
        "categories": ["Breaking News", "MSP Rate"],
        "tags": ["पंजाब गन्ना भाव 410", "Punjab Sugarcane Board SAP", "410 Quintal Demand", "Bhagwant Mann Cabinet", "Kisan MSP"],
        "keywords": ["punjab sugarcane board recommends 410 sap 2026", "punjab ganna rate proposal 410 quintal", "bhagwant mann sugarcane sap notification 2026", "sugar mills punjab crushing rate"],
        "banner_img": "punjab-sugarcane-board-recommends-410-sap-2026.webp",
        "bg_img": os.path.join(brain_dir, "ws_bhav_600_1787597306153.jpg"),
        "tag": "गन्ना भाव प्रस्ताव ⚡",
        "h1": "पंजाब: गन्ना भाव ₹410 प्रति क्विंटल करने की सिफारिश",
        "h2_html": "गन्ना नियंत्रण बोर्ड का प्रस्ताव, <span class='sub-highlight'>कैबिनेट में जल्द लगेगी मुहर</span>"
    },
    {
        "slug": "pmfby-satellite-survey-heavy-rain-damage-sugarcane-up-2026",
        "title": "फसल बीमा का बड़ा फैसला — अगस्त की बारिश और जलभराव से नुकसान का सैटेलाइट सर्वे शुरू",
        "desc": "कृषि बीमा कंपनी (AIC) और उत्तर प्रदेश कृषि विभाग ने पश्चिमी यूपी के 6 जलभराव प्रभावित जिलों में रिमोट सेंसिंग सैटेलाइट के जरिए फसल क्षति का स्वचालित मूल्यांकन शुरू कर दिया है।",
        "date": "2026-09-03T17:00:00+05:30",
        "categories": ["Breaking News", "Sarkari Yojana"],
        "tags": ["फसल बीमा सैटेलाइट सर्वे", "PMFBY Waterlogging Assessment", "AIC Damage Claim", "बाढ़ मुआवजा", "CaneUp Guide"],
        "keywords": ["pmfby satellite survey heavy rain damage sugarcane up 2026", "fasal bima survey waterlogging bijnor muzaffarnagar", "aic remote sensing crop damage evaluation", "pmfby claim settlement sugarcane farmers"],
        "banner_img": "pmfby-satellite-survey-heavy-rain-damage-sugarcane-up-2026.webp",
        "bg_img": os.path.join(brain_dir, "farmer_satisfaction_1787582522776.jpg"),
        "tag": "फसल बीमा ⚡",
        "h1": "बारिश से नुकसान का सैटेलाइट सर्वे शुरू",
        "h2_html": "जलभराव से प्रभावित किसानों को <span class='sub-highlight'>बीमा क्लेम का त्वरित भुगतान</span>"
    },
    {
        "slug": "eganna-app-v6-2-update-tractor-live-queue-tracking-2026",
        "title": "ई-गन्ना ऐप का नया v6.2 अपडेट जारी — मिल यार्ड में लाइव ट्रैक्टर कतार और आसान बायोमेट्रिक लॉगिन",
        "desc": "गन्ना विकास विभाग ने प्ले स्टोर पर eGanna App का वर्जन 6.2 रोलआउट किया है। इसमें मिल गेट पर ट्रॉलियों की लाइव कतार देखने और सर्वर टाइमआउट की समस्या को स्थायी रूप से ठीक किया गया है।",
        "date": "2026-09-03T18:00:00+05:30",
        "categories": ["Breaking News", "CaneUp Guide"],
        "tags": ["eGanna App v6.2 Update", "Live Tractor Queue", "ई-गन्ना ऐप नया फीचर", "Google Play Store", "CaneUp App"],
        "keywords": ["eganna app v6 2 update tractor live queue tracking 2026", "download eganna app latest version play store", "eganna session timeout fix 2026 27", "mill gate live token queue status up"],
        "banner_img": "eganna-app-v6-2-update-tractor-live-queue-tracking-2026.webp",
        "bg_img": os.path.join(brain_dir, "satta_pre_cal_1787581882990.jpg"),
        "tag": "ऐप अपडेट ⚡",
        "h1": "ई-गन्ना ऐप का नया v6.2 अपडेट जारी",
        "h2_html": "मिल गेट पर दिखेगी लाइव कतार, <span class='sub-highlight'>बायोमेट्रिक एरर पूरी तरह ठीक</span>"
    },
    {
        "slug": "kisan-morcha-24-hour-token-fast-tehsils-5-september-2026",
        "title": "5 सितंबर को सभी तहसीलों पर 24 घंटे का उपवास — स्मार्ट मीटर और गन्ना मूल्य पर संयुक्त मोर्चा का ऐलान",
        "slug": "kisan-morcha-24-hour-token-fast-tehsils-5-september-2026",
        "desc": "8 सितंबर की मुजफ्फरनगर महापंचायत से पहले पश्चिमी यूपी के संयुक्त किसान मोर्चे ने 5 सितंबर को सभी तहसील मुख्यालयों पर सांकेतिक उपवास और मुख्यमंत्री को ज्ञापन सौंपने का निर्णय लिया है।",
        "date": "2026-09-03T19:00:00+05:30",
        "categories": ["Breaking News", "Farmer Protest"],
        "tags": ["5 सितंबर तहसील उपवास", "Kisan Morcha Token Fast", "स्मार्ट मीटर विरोध", "गन्ना मूल्य आंदोलन", "SKM UP"],
        "keywords": ["kisan morcha 24 hour token fast tehsils 5 september 2026", "samyukt kisan morcha western up tehsil protest", "smart meter bijli virodh ganna kisan", "muzaffarnagar shamli meerut tehsil dharna"],
        "banner_img": "kisan-morcha-24-hour-token-fast-tehsils-5-september-2026.webp",
        "bg_img": os.path.join(brain_dir, "farmer_satisfaction_1787582522776.jpg"),
        "tag": "आंदोलन ऐलान ⚡",
        "h1": "5 सितंबर को तहसीलों पर 24 घंटे का उपवास",
        "h2_html": "स्मार्ट मीटर व गन्ना मूल्य पर <span class='sub-highlight'>संयुक्त किसान मोर्चे का बड़ा निर्णय</span>"
    },
    {
        "slug": "state-warehousing-corporation-50-fertilizer-buffer-hubs-up-2026",
        "title": "खाद किल्लत पर फुल-स्टॉप — राज्य भंडारण निगम ने बनाए 50 समर्पित बफर हब, 24 घंटे में पहुंचेगी डीएपी",
        "slug": "state-warehousing-corporation-50-fertilizer-buffer-hubs-up-2026",
        "desc": "उत्तर प्रदेश राज्य भंडारण निगम (UPSWC) ने शरद बुवाई के लिए 50 रणनीतिक गोदामों को विशेष उर्वरक हब में बदल दिया है। समितियों से मांग आते ही 24 घंटे में खाद की सीधी डिलीवरी होगी।",
        "date": "2026-09-03T20:00:00+05:30",
        "categories": ["Breaking News", "Sarkari Yojana"],
        "tags": ["50 उर्वरक बफर हब", "State Warehousing Corporation", "DAP Express Delivery", "खाद बफर स्टॉक", "Cooperative UP"],
        "keywords": ["state warehousing corporation 50 fertilizer buffer hubs up 2026", "dap npk buffer godown western up cane belt", "upswc 24 hour fertilizer supply pacs", "sharadkalin ganna khad buffer stock"],
        "banner_img": "state-warehousing-corporation-50-fertilizer-buffer-hubs-up-2026.webp",
        "bg_img": os.path.join(brain_dir, "news8_harvester_subsidy_cover_1787948234294.jpg"),
        "tag": "खाद एक्सप्रेस ⚡",
        "h1": "खाद की निर्बाध सप्लाई को 50 बफर हब तैयार",
        "h2_html": "मांग आते ही 24 घंटे में <span class='sub-highlight'>सीधे समितियों को पहुंचेगी डीएपी खाद</span>"
    }
]

# Step 1: Render All 10 BBC Style Banners via Headless Chrome
temp_html = os.path.join(img_dir, "_temp_sept3_next10h_render.html")
temp_png = os.path.join(img_dir, "_temp_sept3_next10h_render.png")

print("Rendering 10 BBC Style Featured Banners for September 3 Next 10 Hours...")

for idx, p in enumerate(articles_data, 1):
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
    height: 400px;
    background: linear-gradient(to top, rgba(0, 0, 0, 0.96) 0%, rgba(0, 0, 0, 0.8) 45%, rgba(0, 0, 0, 0) 100%);
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
    font-size: 50px;
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
    font-size: 34px;
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
            
    print(f"[{idx}/10] Rendered BBC Banner: {p['banner_img']} ({kb:.1f} KB)")

if os.path.exists(temp_html):
    os.remove(temp_html)
if os.path.exists(temp_png):
    os.remove(temp_png)

print("\nAll 10 September 3 Next 10 Hours BBC Banners rendered successfully!")
