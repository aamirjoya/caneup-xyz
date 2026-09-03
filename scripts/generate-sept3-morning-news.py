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

sept3_morning_data = [
    {
        "slug": "up-ganna-satta-day-3-52000-objections-settled-muzaffarnagar-top-2026",
        "title": "सट्टा सुधार अभियान के तीसरे दिन 52,000 आपत्तियां हल — मुजफ्फरनगर व बिजनौर प्रदेश में सबसे आगे",
        "desc": "उत्तर प्रदेश के 45 जिलों में तीसरे दिन तक 52,400 से अधिक किसानों के सट्टा व सर्वे विवाद हल कर दिए गए हैं। मुजफ्फरनगर और बिजनौर जिले समयबद्ध निस्तारण में पूरे प्रदेश में शीर्ष पर रहे।",
        "date": "2026-09-03T07:00:00+05:30",
        "categories": ["Breaking News", "CaneUp Guide"],
        "tags": ["सट्टा सुधार अभियान 2026", "Day 3 Satta Report", "52000 Objections", "Muzaffarnagar Bijnor", "CaneUp UP"],
        "keywords": ["up ganna satta day 3 52000 objections settled 2026", "muzaffarnagar bijnor ganna survey ranking", "enquiry caneup in satta correction progress", "ganna samiti satta nistaran report 3 september"],
        "banner_img": "up-ganna-satta-day-3-52000-objections-settled-muzaffarnagar-top-2026.webp",
        "bg_img": os.path.join(brain_dir, "satta_pre_cal_1787581882990.jpg"),
        "tag": "सट्टा बुलेटिन ⚡",
        "h1": "सट्टा सुधार अभियान: 52,000 आपत्तियां हल",
        "h2_html": "मुजफ्फरनगर व बिजनौर <span class='sub-highlight'>पूरे प्रदेश में सबसे आगे</span>"
    },
    {
        "slug": "wholesale-sugar-prices-fall-50-rupees-stock-limit-impact-2026",
        "title": "थोक चीनी बाजार में ₹50-80 प्रति क्विंटल की गिरावट — 2,000 क्विंटल स्टॉक सीमा और पाक्षिक कोटे का बड़ा असर",
        "desc": "केंद्र सरकार के पाक्षिक बिक्री कोटे और 2,000 क्विंटल स्टॉक सीमा नियम के प्रभावी होने से उत्तर प्रदेश और दिल्ली की थोक मंडियों में चीनी के भाव में ₹50 से ₹80 प्रति क्विंटल की तीव्र गिरावट दर्ज की गई।",
        "date": "2026-09-03T07:15:00+05:30",
        "categories": ["Breaking News", "Sugar Industry"],
        "tags": ["चीनी मूल्य गिरावट", "Sugar Price Drop", "Wholesale Mandi", "Stock Limit Effect", "Sugar Market"],
        "keywords": ["wholesale sugar prices fall 50 rupees stock limit impact 2026", "up chini mandi wholesale rate september 2026", "m 30 grade sugar price drop delhi up", "fortnight quota sugar market stabilization"],
        "banner_img": "wholesale-sugar-prices-fall-50-rupees-stock-limit-impact-2026.webp",
        "bg_img": os.path.join(brain_dir, "ws_sugar_mills_1787597400680.jpg"),
        "tag": "बाजार भाव ⚡",
        "h1": "थोक चीनी बाजार में ₹50-80/कुंतल की गिरावट",
        "h2_html": "स्टॉक सीमा व पाक्षिक कोटे से <span class='sub-highlight'>जमाखोरों पर कड़ा प्रहार</span>"
    },
    {
        "slug": "digital-weighbridge-calibration-2800-purchase-centers-up-2026",
        "title": "घटतौली पर लगाम — प्रदेश के 2,800 गन्ना कांटों की डिजिटल सीलिंग व इलेक्ट्रॉनिक कैलिब्रेशन शुरू",
        "slug": "digital-weighbridge-calibration-2800-purchase-centers-up-2026",
        "desc": "उत्तर प्रदेश विधिक माप विज्ञान (नाप-तौल विभाग) ने आज से 120 चीनी मिलों के 2,800 बाह्य गन्ना क्रय केंद्रों पर डिजिटल वे-ब्रिज की सरकारी सीलिंग और कैलिब्रेशन का विशेष अभियान शुरू कर दिया है।",
        "date": "2026-09-03T07:30:00+05:30",
        "categories": ["Breaking News", "CaneUp Guide"],
        "tags": ["घटतौली रोकथाम", "Weighbridge Calibration", "2800 Purchase Centers", "नाप-तौल विभाग", "CaneUp News"],
        "keywords": ["digital weighbridge calibration 2800 purchase centers up 2026", "ganna kata ghattoli roktham checking", "electronic weighbridge sealing legal metrology up", "sugar mill purchase center inspection 2026"],
        "banner_img": "digital-weighbridge-calibration-2800-purchase-centers-up-2026.webp",
        "bg_img": os.path.join(brain_dir, "chandanpur_mill_cover_1787946872076.jpg"),
        "tag": "घटतौली रोक ⚡",
        "h1": "2,800 गन्ना कांटों की डिजिटल सीलिंग शुरू",
        "h2_html": "घटतौली रोकने के लिए <span class='sub-highlight'>नाप-तौल विभाग का कड़ा एक्शन</span>"
    },
    {
        "slug": "bijnor-saharanpur-sugar-mills-boiler-puja-dates-september-2026",
        "title": "धामपुर, बरकातपुर व देवबंद चीनी मिलों में बॉयलर पूजा की तारीखें तय — 15 से 20 सितंबर तक शुरू होंगे स्टीम ट्रायल",
        "desc": "बिजनौर और सहारनपुर की प्रमुख निजी व सहकारी चीनी मिलों ने बॉयलर पूजा और स्टीम टेस्टिंग की तिथियां घोषित कर दी हैं। 15 अक्टूबर से अगेती पेराई शुरू करने के लिए युद्धस्तर पर मरम्मत पूरी।",
        "date": "2026-09-03T07:45:00+05:30",
        "categories": ["Breaking News", "Sugar Industry"],
        "tags": ["बॉयलर पूजा 2026", "Dhampur Deoband Sugar Mills", "Steam Trial Dates", "पेराई सत्र 2026-27", "Western UP Mills"],
        "keywords": ["bijnor saharanpur sugar mills boiler puja dates september 2026", "dhampur barkatpur deoband boiler steam trial", "western up sugar mills early crushing schedule", "perai satra 15 october 2026"],
        "banner_img": "bijnor-saharanpur-sugar-mills-boiler-puja-dates-september-2026.webp",
        "bg_img": os.path.join(brain_dir, "asmauli_sugar_factory_1787939335198.jpg"),
        "tag": "मिल शेड्यूल ⚡",
        "h1": "धामपुर, देवबंद मिलों में बॉयलर पूजा की तारीखें तय",
        "h2_html": "15 से 20 सितंबर तक <span class='sub-highlight'>शुरू होंगे हाई-प्रेशर स्टीम ट्रायल</span>"
    },
    {
        "slug": "upcsr-post-rain-autumn-sugarcane-field-prep-advisory-2026",
        "title": "बारिश के बाद खेत तैयारी एडवाइजरी — ट्रेंच विधि से शरदकालीन गन्ना बुवाई के लिए ऐसे तैयार करें जमीन",
        "slug": "upcsr-post-rain-autumn-sugarcane-field-prep-advisory-2026",
        "desc": "गन्ना शोध परिषद शाहजहांपुर ने बारिश के बाद मिट्टी की जुताई, ट्रेंच नालियां बनाने, गोबर की खाद में ट्राइकोडर्मा मिलाने और 15 सितंबर से बुवाई के लिए खेत की धूप से जुताई की विस्तृत गाइड जारी की।",
        "date": "2026-09-03T08:00:00+05:30",
        "categories": ["Breaking News", "Ganna Guide"],
        "tags": ["खेत तैयारी एडवाइजरी", "Trench Field Preparation", "UPCSR Shahjahanpur", "शरदकालीन बुवाई", "Farming Guide"],
        "keywords": ["upcsr post rain autumn sugarcane field prep advisory 2026", "sharadkalin ganna khet taiyari trench vidhi", "trichoderma gobar khad application sugarcane", "september ganna buwai khet jutai"],
        "banner_img": "upcsr-post-rain-autumn-sugarcane-field-prep-advisory-2026.webp",
        "bg_img": os.path.join(brain_dir, "trench_buwai_1787582649543.jpg"),
        "tag": "खेत तैयारी ⚡",
        "h1": "बारिश के बाद खेत तैयारी एडवाइजरी जारी",
        "h2_html": "ट्रेंच विधि से शरद बुवाई के लिए <span class='sub-highlight'>वैज्ञानिक तरीके से तैयार करें जमीन</span>"
    },
    {
        "slug": "up-cooperative-sugar-mills-600-crore-pre-season-modernization-2026",
        "title": "यूपी की 24 सहकारी चीनी मिलों को ₹600 करोड़ का प्री-सीजन पैकेज — आधुनिकीकरण और त्वरित भुगतान की तैयारी",
        "desc": "उत्तर प्रदेश सहकारी चीनी मिल्स संघ ने राज्य की 24 सहकारी चीनी मिलों के तकनीकी आधुनिकीकरण, टरबाइन अपग्रेड और पेराई क्षमता विस्तार के लिए ₹600 करोड़ की कार्यशील पूंजी स्वीकृत की है।",
        "date": "2026-09-03T08:15:00+05:30",
        "categories": ["Breaking News", "Sugar Industry"],
        "tags": ["सहकारी चीनी मिल पैकेज", "600 Crore Modernization", "UP Cooperative Sugar Mills", "पेराई सुधार", "CaneUp News"],
        "keywords": ["up cooperative sugar mills 600 crore pre season modernization 2026", "sahkari chini mill overhaul working capital up", "cooperative sugar mill crushing performance 2026 27", "sugarfed up modernization package"],
        "banner_img": "up-cooperative-sugar-mills-600-crore-pre-season-modernization-2026.webp",
        "bg_img": os.path.join(brain_dir, "news9_ethanol_expansion_cover_1787948284345.jpg"),
        "tag": "सरकारी पैकेज ⚡",
        "h1": "24 सहकारी चीनी मिलों को ₹600 करोड़ का पैकेज",
        "h2_html": "आधुनिकीकरण व त्वरित भुगतान के लिए <span class='sub-highlight'>कार्यशील पूंजी स्वीकृत</span>"
    },
    {
        "slug": "muzaffarnagar-kisan-yatra-7-september-bku-mobilization-2026",
        "title": "मुजफ्फरनगर में 7 सितंबर से शुरू होगी 'किसान संदेश यात्रा' — 8 सितंबर की महापंचायत के लिए आर-पार की तैयारी",
        "slug": "muzaffarnagar-kisan-yatra-7-september-bku-mobilization-2026",
        "desc": "भाकियू ने गन्ने का भाव ₹450 प्रति क्विंटल घोषित कराने और बिजली मीटरों के विरोध में 7 सितंबर को मुजफ्फरनगर के सभी ब्लॉकों में ट्रैक्टरों के साथ किसान संदेश यात्रा निकालने का ऐलान किया है।",
        "date": "2026-09-03T08:30:00+05:30",
        "categories": ["Breaking News", "Farmer Protest"],
        "tags": ["किसान संदेश यात्रा", "Muzaffarnagar Kisan Yatra", "BKU 7 September", "Mahapanchayat Mobilization", "Kisan Andolan"],
        "keywords": ["muzaffarnagar kisan yatra 7 september bku mobilization 2026", "gic ground muzaffarnagar 8 september mahapanchayat", "kisan sandesh yatra tractor march western up", "bku rakesh tikait ganna bhav 450"],
        "banner_img": "muzaffarnagar-kisan-yatra-7-september-bku-mobilization-2026.webp",
        "bg_img": os.path.join(brain_dir, "farmer_satisfaction_1787582522776.jpg"),
        "tag": "किसान यात्रा ⚡",
        "h1": "मुजफ्फरनगर में 7 सितंबर से 'किसान संदेश यात्रा'",
        "h2_html": "8 सितंबर महापंचायत के लिए <span class='sub-highlight'>गाँव-गाँव निकलेगा ट्रैक्टर मार्च</span>"
    },
    {
        "slug": "haryana-sugarfed-14-mills-ready-25-october-crushing-start-2026",
        "title": "हरियाणा शुगरफेड की 14 मिलें 25 अक्टूबर से पेराई को तैयार — ₹405 भाव पर किसानों के बॉन्ड भरने का काम शुरू",
        "slug": "haryana-sugarfed-14-mills-ready-25-october-crushing-start-2026",
        "desc": "हरियाणा राज्य सहकारी चीनी मिल संघ ने राज्य की सभी 14 मिलों में 25 अक्टूबर से पेराई का इंडेंट जारी करने की तैयारी पूरी कर ली है। किसानों के साथ ₹405 प्रति क्विंटल के आधार पर सप्लाई बॉन्ड भरे जा रहे हैं।",
        "date": "2026-09-03T08:45:00+05:30",
        "categories": ["Breaking News", "Sugar Industry"],
        "tags": ["हरियाणा शुगरफेड 14 मिलें", "25 October Crushing", "Haryana SAP 405", "Grower Bond", "Sugar Mills"],
        "keywords": ["haryana sugarfed 14 mills ready 25 october crushing start 2026", "yamunanagar rohtak karnal sugar mill crushing schedule", "haryana ganna supply bond 405 quintal", "sugarfed haryana crushing preparation"],
        "banner_img": "haryana-sugarfed-14-mills-ready-25-october-crushing-start-2026.webp",
        "bg_img": os.path.join(brain_dir, "ws_bhav_600_1787597306153.jpg"),
        "tag": "हरियाणा तैयारी ⚡",
        "h1": "हरियाणा की 14 मिलें 25 अक्टूबर से पेराई को तैयार",
        "h2_html": "₹405 के भाव पर <span class='sub-highlight'>किसानों के सप्लाई बॉन्ड भरने का काम शुरू</span>"
    },
    {
        "slug": "kisan-drone-fleet-expanded-60-units-western-up-2026",
        "title": "पश्चिमी यूपी में किसान ड्रोन फ्लीट बढ़कर 60 हुई — 15,000 एकड़ से अधिक गन्ने पर छिड़काव का लक्ष्य",
        "slug": "kisan-drone-fleet-expanded-60-units-western-up-2026",
        "desc": "गन्ना विकास विभाग ने भारी मांग को देखते हुए मेरठ, सहारनपुर और मुरादाबाद मंडलों में 25 अतिरिक्त किसान ड्रोन शामिल कर फ्लीट 60 कर दी है। प्रति एकड़ ₹250 में 10 मिनट में पूरा हो रहा स्प्रे।",
        "date": "2026-09-03T09:00:00+05:30",
        "categories": ["Breaking News", "Sarkari Yojana"],
        "tags": ["किसान ड्रोन 60 यूनिट्स", "Drone Spraying Expansion", "50 Percent Subsidy", "Western UP Fleet", "CaneUp Drone"],
        "keywords": ["kisan drone fleet expanded 60 units western up 2026", "drone spraying 15000 acres target up cane dept", "custom hiring center drone fleet expansion", "drone spray potash zinc red rot sugarcane"],
        "banner_img": "kisan-drone-fleet-expanded-60-units-western-up-2026.webp",
        "bg_img": os.path.join(brain_dir, "farmer_satisfaction_1787582522776.jpg"),
        "tag": "ड्रोन विस्तार ⚡",
        "h1": "पश्चिमी यूपी में किसान ड्रोन फ्लीट बढ़कर 60 हुई",
        "h2_html": "15,000 एकड़ गन्ने पर <span class='sub-highlight'>तेजी से पूरा होगा रियायती छिड़काव</span>"
    },
    {
        "slug": "iffco-kribhco-150-mobile-dap-trucks-sugar-belt-up-2026",
        "title": "गन्ना बेल्ट में खाद की किल्लत रोकने को इफको के 150 मोबाइल ट्रक तैनात — ₹1,350 में गाँव-गाँव डीएपी वितरण",
        "slug": "iffco-kribhco-150-mobile-dap-trucks-sugar-belt-up-2026",
        "desc": "शरदकालीन गन्ना बुवाई से पहले किसानों को लंबी कतारों से बचाने के लिए सहकारिता विभाग ने मुजफ्फरनगर, शामली, मेरठ और लखीमपुर में 150 सचल उर्वरक वाहनों के जरिए डीएपी और पोटाश का सीधा वितरण शुरू किया।",
        "date": "2026-09-03T09:15:00+05:30",
        "categories": ["Breaking News", "Sarkari Yojana"],
        "tags": ["इफको मोबाइल डीएपी ट्रक", "150 Fertilizer Vans", "DAP 1350 Bag", "Sugar Belt UP", "सहकारी खाद"],
        "keywords": ["iffco kribhco 150 mobile dap trucks sugar belt up 2026", "mobile fertilizer distribution van sugarcane farmers", "dap 1350 bag door to door cooperative up", "sharadkalin ganna khad vitran van"],
        "banner_img": "iffco-kribhco-150-mobile-dap-trucks-sugar-belt-up-2026.webp",
        "bg_img": os.path.join(brain_dir, "news8_harvester_subsidy_cover_1787948234294.jpg"),
        "tag": "खाद वितरण ⚡",
        "h1": "गन्ना बेल्ट में इफको के 150 मोबाइल DAP ट्रक तैनात",
        "h2_html": "शरद बुवाई से पहले <span class='sub-highlight'>गाँव-गाँव ₹1,350 में डीएपी खाद वितरण</span>"
    }
]

# Step 1: Render All 10 BBC Style Banners via Headless Chrome
temp_html = os.path.join(img_dir, "_temp_sept3_render.html")
temp_png = os.path.join(img_dir, "_temp_sept3_render.png")

print("Rendering 10 BBC Style Featured Banners for September 3 Morning News...")

for idx, p in enumerate(sept3_morning_data, 1):
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

print("\nAll 10 September 3 Morning BBC Banners rendered successfully!")
