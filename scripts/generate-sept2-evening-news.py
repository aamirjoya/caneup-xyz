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

sept2_evening_data = [
    {
        "slug": "up-ganna-satta-campaign-day-2-36000-objections-resolved-2026",
        "title": "सट्टा सुधार अभियान के दूसरे दिन 36,000 आपत्तियां हल — 30 सितंबर तक घोषणा पत्र भरना अनिवार्य",
        "desc": "उत्तर प्रदेश में गन्ना सट्टा आपत्ति निस्तारण के दूसरे दिन शाम तक कुल 36,200 किसानों के रिकॉर्ड सुधारे गए। गन्ना आयुक्त ने 30 सितंबर तक ऑनलाइन घोषणा पत्र न भरने पर सट्टा बंद करने की चेतावनी दी।",
        "date": "2026-09-02T19:00:00+05:30",
        "categories": ["Breaking News", "CaneUp Guide"],
        "tags": ["सट्टा सुधार अभियान", "Day 2 Satta Report", "Ghosna Patra Deadline", "CaneUp UP", "गन्ना समिति"],
        "keywords": ["up ganna satta campaign day 2 36000 objections 2026", "ghosna patra 30 september deadline up cane", "enquiry caneup in satta pre calendar correction", "ganna samiti scio meeting 2 september 2026"],
        "banner_img": "up-ganna-satta-campaign-day-2-36000-objections-resolved-2026.webp",
        "bg_img": os.path.join(brain_dir, "satta_pre_cal_1787581882990.jpg"),
        "tag": "सट्टा रिपोर्ट ⚡",
        "h1": "सट्टा सुधार के दूसरे दिन 36,000 आपत्तियां हल",
        "h2_html": "30 सितंबर तक घोषणा पत्र न भरने पर <span class='sub-highlight'>सट्टा बंद करने की चेतावनी</span>"
    },
    {
        "slug": "mandi-samiti-inspections-sugar-stock-limit-2000-quintals-2026",
        "title": "चीनी गोदामों पर प्रशासनिक छापे तेज — 2,000 क्विंटल स्टॉक सीमा का कड़ाई से पालन कराने के निर्देश",
        "desc": "मेरठ, मुजफ्फरनगर और हापुड़ की थोक गल्ला मंडियों में खाद्य सुरक्षा और मंडी समिति की संयुक्त टीमों ने चीनी गोदामों की सघन जांच की। स्टॉक रजिस्टर में हेराफेरी पर 2 व्यापारियों को नोटिस जारी।",
        "date": "2026-09-02T19:15:00+05:30",
        "categories": ["Breaking News", "Sugar Industry"],
        "tags": ["चीनी गोदाम छापे", "Sugar Stock Limit 2000 Quintal", "Mandi Inspection", "जमाखोरी नियंत्रण", "CaneUp News"],
        "keywords": ["mandi samiti inspection sugar stock limit 2000 quintals 2026", "meerut muzaffarnagar sugar godown raid", "food safety officer chini checking up", "sugar dealer notice essential commodities act"],
        "banner_img": "mandi-samiti-inspections-sugar-stock-limit-2000-quintals-2026.webp",
        "bg_img": os.path.join(brain_dir, "ws_sugar_mills_1787597400680.jpg"),
        "tag": "प्रशासनिक कार्रवाई ⚡",
        "h1": "चीनी गोदामों पर सघन प्रशासनिक जांच तेज",
        "h2_html": "2000 क्विंटल स्टॉक सीमा नियम पर <span class='sub-highlight'>व्यापारियों को कड़े निर्देश</span>"
    },
    {
        "slug": "shamli-sugar-mills-final-clearance-order-september-10-2026",
        "title": "शामली की तीनों चीनी मिलों को अंतिम अल्टीमेटम — 10 सितंबर तक पूरा बकाया न चुकाने पर आरसी की तैयारी",
        "desc": "शामली डीएम और जिला गन्ना अधिकारी ने अपर दोआब, थानाभवन और ऊन मिलों को 10 सितंबर तक पिछले पेराई सत्र का शत-प्रतिशत बकाया भुगतान निपटाने का अंतिम आदेश दिया है।",
        "date": "2026-09-02T19:30:00+05:30",
        "categories": ["Breaking News", "Ganna Bhugtan"],
        "tags": ["शामली गन्ना भुगतान अल्टीमेटम", "Upper Doab Shamli", "Thanabhawan Sugar Mill", "10 September Deadline", "CaneUp News"],
        "keywords": ["shamli sugar mills final clearance order 10 september 2026", "upper doab shamli thanabhawan un ganna bhugtan", "dco shamli rc notice sugar mills", "ganna kisan payment status 2026"],
        "banner_img": "shamli-sugar-mills-final-clearance-order-september-10-2026.webp",
        "bg_img": os.path.join(brain_dir, "sugar_mill_payment_1787489145600.jpg"),
        "tag": "सख्त अल्टीमेटम ⚡",
        "h1": "शामली की तीनों चीनी मिलों को अंतिम अल्टीमेटम",
        "h2_html": "10 सितंबर तक बकाया न चुकाने पर <span class='sub-highlight'>आरसी जारी करने की तैयारी</span>"
    },
    {
        "slug": "western-up-rain-impact-red-rot-prevention-advisory-2026",
        "title": "पश्चिमी यूपी में 75 मिमी तक बारिश दर्ज — जलभराव से लाल सड़न रोकने को कॉपर फफूंदनाशक एडवाइजरी",
        "desc": "मुजफ्फरनगर, बिजनौर और सहारनपुर में आज तेज बारिश के बाद खेतों में पानी भरने से कृषि वैज्ञानिकों ने तुरंत पानी निकालने और कॉपर ऑक्सीक्लोराइड से जड़ों की ड्रेचिंग करने की सलाह दी है।",
        "date": "2026-09-02T19:45:00+05:30",
        "categories": ["Breaking News", "Ganna Guide"],
        "tags": ["पश्चिमी यूपी बारिश", "Red Rot Drainage Advisory", "कॉपर फफूंदनाशक", "जलभराव बचाव", "September Farming"],
        "keywords": ["western up rain impact red rot prevention advisory 2026", "muzaffarnagar bijnor 75 mm rain sugarcane", "copper oxychloride drenching sugarcane waterlogging", "ganne mein jalbharav se bachav"],
        "banner_img": "western-up-rain-impact-red-rot-prevention-advisory-2026.webp",
        "bg_img": os.path.join(brain_dir, "trench_buwai_1787582649543.jpg"),
        "tag": "फसल सुरक्षा ⚡",
        "h1": "पश्चिमी यूपी में 75 मिमी तक बारिश दर्ज",
        "h2_html": "जलभराव से लाल सड़न रोकने के लिए <span class='sub-highlight'>कॉपर स्प्रे की एडवाइजरी</span>"
    },
    {
        "slug": "autumn-sugarcane-seed-booking-opens-co15023-cos17231-2026",
        "title": "शरदकालीन गन्ना बुवाई के लिए बीज बुकिंग शुरू — Co-15023 व CoS-17231 के प्रमाणित बीज पर सब्सिडी",
        "desc": "उत्तर प्रदेश गन्ना बीज प्रमाणीकरण संस्था और शोध केंद्रों ने 15 सितंबर से शुरू हो रही शरद बुवाई के लिए रोगरोधी प्रजातियों के फाउंडेशन सीड की ऑनलाइन व समिति बुकिंग शुरू कर दी है।",
        "date": "2026-09-02T20:00:00+05:30",
        "categories": ["Breaking News", "Ganna Guide"],
        "tags": ["गन्ना बीज बुकिंग 2026", "Co 15023 Seed", "CoS 17231", "शरदकालीन बुवाई", "CaneUp Subsidy"],
        "keywords": ["autumn sugarcane seed booking opens co15023 cos17231 2026", "certified sugarcane seed booking up cane dept", "upcsr shahjahanpur foundation seed rate", "sharadkalin ganna beej booking"],
        "banner_img": "autumn-sugarcane-seed-booking-opens-co15023-cos17231-2026.webp",
        "bg_img": os.path.join(brain_dir, "ws_cos17231_1787597414786.jpg"),
        "tag": "बीज बुकिंग ⚡",
        "h1": "शरदकालीन गन्ना बुवाई के लिए बीज बुकिंग शुरू",
        "h2_html": "Co-15023 व CoS-17231 प्रमाणित बीज पर <span class='sub-highlight'>सरकारी सब्सिडी उपलब्ध</span>"
    },
    {
        "slug": "uperc-reviews-sugar-mill-green-cogeneration-tariff-2026",
        "title": "चीनी मिलों के 1,500 मेगावाट बायोमास ग्रीन पावर टैरिफ की समीक्षा — पेराई सत्र में निर्बाध ग्रिड सप्लाई",
        "desc": "उत्तर प्रदेश विद्युत नियामक आयोग (UPERC) ने चीनी मिलों के को-जेनरेशन बिजली संयंत्रों से खरीदी जाने वाली हरित बिजली की दरों की समीक्षा की। आगामी सत्र में 1,500 मेगावाट बिजली राज्य ग्रिड को मिलेगी।",
        "date": "2026-09-02T20:15:00+05:30",
        "categories": ["Breaking News", "Sugar Industry"],
        "tags": ["बायोमास ग्रीन पावर", "UPERC Cogeneration Tariff", "Sugar Mill Power", "खोई से बिजली", "Green Energy"],
        "keywords": ["uperc reviews sugar mill green cogeneration tariff 2026", "bagasse power plant sugar mills up grid", "1500 mw biomass green power crushing season", "sugar mill power purchase agreement uperc"],
        "banner_img": "uperc-reviews-sugar-mill-green-cogeneration-tariff-2026.webp",
        "bg_img": os.path.join(brain_dir, "chandanpur_mill_cover_1787946872076.jpg"),
        "tag": "हरित ऊर्जा ⚡",
        "h1": "चीनी मिलों के 1500 MW ग्रीन पावर टैरिफ की समीक्षा",
        "h2_html": "खोई से बनेगी हरित बिजली, <span class='sub-highlight'>राज्य ग्रिड को मिलेगी सप्लाई</span>"
    },
    {
        "slug": "bku-village-panchayats-8-september-muzaffarnagar-mahapanchayat-2026",
        "title": "8 सितंबर की मुजफ्फरनगर महापंचायत की तैयारी तेज — 25 गाँवों में किसान पंचायत कर दिया न्योता",
        "desc": "भाकियू नेताओं ने शामली, बागपत और मुजफ्फरनगर के 25 गाँवों में सघन जनसंपर्क कर गन्ने का भाव ₹450 प्रति क्विंटल घोषित कराने के लिए 8 सितंबर को जीआईसी मैदान में पहुंचने का आह्वान किया।",
        "date": "2026-09-02T20:30:00+05:30",
        "categories": ["Breaking News", "Farmer Protest"],
        "tags": ["मुजफ्फरनगर किसान महापंचायत", "BKU Village Panchayats", "गन्ना मूल्य 450 मांग", "Rakesh Tikait", "GIC Ground"],
        "keywords": ["bku village panchayats 8 september muzaffarnagar mahapanchayat 2026", "gic ground muzaffarnagar kisan rally preparations", "ganna bhav 450 demand western up", "bku sisauli kisan andolan 2026"],
        "banner_img": "bku-village-panchayats-8-september-muzaffarnagar-mahapanchayat-2026.webp",
        "bg_img": os.path.join(brain_dir, "farmer_satisfaction_1787582522776.jpg"),
        "tag": "महापंचायत तैयारी ⚡",
        "h1": "8 सितंबर मुजफ्फरनगर महापंचायत की तैयारी तेज",
        "h2_html": "25 गाँवों में पंचायत कर किसानों को <span class='sub-highlight'>जीआईसी मैदान का दिया न्योता</span>"
    },
    {
        "slug": "haryana-ministerial-panel-clears-405-ganna-sap-2026",
        "title": "हरियाणा मंत्रिमंडलीय उप-समिति ने ₹405 गन्ना भाव को दी मंजूरी — इसी सप्ताह जारी होगी अधिसूचना",
        "desc": "हरियाणा के कृषि एवं सहकारिता मंत्रियों की उच्चस्तरीय समिति ने अगेती गन्ने का राज्य परामर्शित मूल्य ₹405 प्रति क्विंटल करने के मसौदे को अंतिम हरी झंडी दे दी है। औपचारिक अधिसूचना इसी सप्ताह जारी होगी।",
        "date": "2026-09-02T20:45:00+05:30",
        "categories": ["Breaking News", "MSP Rate"],
        "tags": ["हरियाणा गन्ना भाव 405", "Ministerial Panel Approval", "Haryana SAP 405", "Kisan MSP", "Sugar Price"],
        "keywords": ["haryana ministerial panel clears 405 ganna sap 2026", "chd haryana sugar mills 405 quintal rate notification", "haryana ganna bhav cabinet approval september 2026", "yamunanagar sugar mill crushing price"],
        "banner_img": "haryana-ministerial-panel-clears-405-ganna-sap-2026.webp",
        "bg_img": os.path.join(brain_dir, "ws_bhav_600_1787597306153.jpg"),
        "tag": "कैबिनेट मंजूरी ⚡",
        "h1": "हरियाणा: ₹405 गन्ना भाव को औपचारिक मंजूरी",
        "h2_html": "मंत्रिमंडलीय समिति ने दी हरी झंडी, <span class='sub-highlight'>इसी सप्ताह जारी होगी अधिसूचना</span>"
    },
    {
        "slug": "drone-spraying-booking-surge-12000-acres-meerut-moradabad-2026",
        "title": "किसान ड्रोन छिड़काव की जबरदस्त मांग — 36 घंटे में 12,000 एकड़ की बुकिंग, 15 नए ड्रोन तैनात",
        "desc": "गन्ना विकास विभाग की 50% सब्सिडी वाली ड्रोन छिड़काव योजना को किसानों का भारी समर्थन मिला है। 36 घंटे में 12,000 एकड़ से अधिक स्लॉट बुक होने के बाद विभाग ने 15 अतिरिक्त ड्रोन यूनिटें तैनात की हैं।",
        "date": "2026-09-02T21:00:00+05:30",
        "categories": ["Breaking News", "Sarkari Yojana"],
        "tags": ["किसान ड्रोन बुकिंग", "12000 Acres Booked", "50 Percent Subsidy", "Meerut Moradabad", "CaneUp Drone"],
        "keywords": ["drone spraying booking surge 12000 acres meerut moradabad 2026", "kisan drone 15 additional units up cane dept", "caneup in drone booking slot response", "drone spray top borer red rot sugarcane"],
        "banner_img": "drone-spraying-booking-surge-12000-acres-meerut-moradabad-2026.webp",
        "bg_img": os.path.join(brain_dir, "farmer_satisfaction_1787582522776.jpg"),
        "tag": "ड्रोन रिकॉर्ड ⚡",
        "h1": "किसान ड्रोन छिड़काव: 36 घंटे में 12,000 एकड़ बुकिंग",
        "h2_html": "जबरदस्त मांग को देखते हुए <span class='sub-highlight'>15 नए आधुनिक ड्रोन तैनात</span>"
    },
    {
        "slug": "up-cooperative-banks-disburse-140-crore-kcc-loans-day-2-2026",
        "title": "सहकारी बैंकों के KCC महा-अभियान में दूसरे दिन ₹140 करोड़ का ऋण वितरित — 4% ब्याज पर भारी रुझान",
        "slug": "up-cooperative-banks-disburse-140-crore-kcc-loans-day-2-2026",
        "desc": "उत्तर प्रदेश के 45 गन्ना बाहुल्य जिलों में जिला सहकारी बैंकों ने विशेष कैंप के दूसरे दिन 28,000 से अधिक गन्ना किसानों को ₹140 करोड़ के केसीसी नवीनीकरण व नए ऋण स्वीकृत किए।",
        "date": "2026-09-02T21:15:00+05:30",
        "categories": ["Breaking News", "Sarkari Yojana"],
        "tags": ["KCC ऋण वितरण 140 करोड़", "Cooperative Bank Camp Day 2", "4 Percent Interest", "Ganna Kisan Loan", "PACS UP"],
        "keywords": ["up cooperative banks disburse 140 crore kcc loans day 2 2026", "kisan credit card renewal camp report 45 districts", "dccb branch kcc disbursement ganna kisan", "4 percent interest subvention nabard up"],
        "banner_img": "up-cooperative-banks-disburse-140-crore-kcc-loans-day-2-2026.webp",
        "bg_img": os.path.join(brain_dir, "ws_kcc_loan_cover_1787906338029.jpg"),
        "tag": "किसान ऋण ⚡",
        "h1": "KCC कैंप के दूसरे दिन ₹140 करोड़ का ऋण वितरित",
        "h2_html": "4% ब्याज दर पर 28,000 किसानों ने <span class='sub-highlight'>कराया खातों का नवीनीकरण</span>"
    }
]

# Step 1: Render All 10 BBC Style Banners via Headless Chrome
temp_html = os.path.join(img_dir, "_temp_sept2_render.html")
temp_png = os.path.join(img_dir, "_temp_sept2_render.png")

print("Rendering 10 BBC Style Featured Banners for September 2 Evening News...")

for idx, p in enumerate(sept2_evening_data, 1):
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

print("\nAll 10 September 2 Evening BBC Banners rendered successfully!")
