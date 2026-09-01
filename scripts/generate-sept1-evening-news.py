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

sept1_evening_data = [
    {
        "slug": "sugar-dealers-stock-limit-halved-2000-quintals-2026",
        "title": "केंद्र का बड़ा फैसला — चीनी व्यापारियों के लिए स्टॉक सीमा घटकर 2,000 क्विंटल हुई, कालाबाजारी पर कड़ा शिकंजा",
        "desc": "खाद्य मंत्रालय ने चीनी व्यापारियों के लिए स्टॉक सीमा 4,000 क्विंटल से घटाकर 2,000 क्विंटल कर दी है। त्योहारी सीजन से पहले जमाखोरी रोकने के लिए 15 सितंबर से 30 नवंबर तक नया नियम लागू रहेगा।",
        "date": "2026-09-01T18:00:00+05:30",
        "categories": ["Breaking News", "Sugar Industry"],
        "tags": ["चीनी स्टॉक सीमा 2000 क्विंटल", "Sugar Stock Limit", "खाद्य मंत्रालय", "जमाखोरी नियंत्रण", "CaneUp News"],
        "keywords": ["sugar dealers stock limit halved 2000 quintals 2026", "food ministry sugar holding limit rules", "chini stock limit 2000 quintal up", "sugar price regulation festive season 2026"],
        "banner_img": "sugar-dealers-stock-limit-halved-2000-quintals-2026.webp",
        "bg_img": os.path.join(brain_dir, "ws_sugar_mills_1787597400680.jpg"),
        "tag": "सख्त नियम ⚡",
        "h1": "चीनी व्यापारियों की स्टॉक सीमा घटकर 2000 क्विंटल",
        "h2_html": "जमाखोरी रोकने के लिए <span class='sub-highlight'>स्टॉक सीमा को आधा किया गया</span>"
    },
    {
        "slug": "up-ganna-satta-disposal-day-1-18400-objections-resolved-2026",
        "title": "यूपी में सट्टा सुधार अभियान के पहले दिन 18,400 आपत्तियां निस्तारित — समितियों में उमड़ी किसानों की भीड़",
        "desc": "उत्तर प्रदेश की 168 गन्ना विकास समितियों में आज 1 सितंबर को सट्टा आपत्ति निस्तारण पखवाड़े के पहले दिन 18,400 से अधिक किसानों के रकबे और सर्वे रिकॉर्ड का मौके पर ही सुधार किया गया।",
        "date": "2026-09-01T18:10:00+05:30",
        "categories": ["Breaking News", "CaneUp Guide"],
        "tags": ["सट्टा सुधार अभियान", "Day 1 Satta Disposal", "18400 Objections", "CaneUp UP", "गन्ना समिति"],
        "keywords": ["up ganna satta disposal day 1 18400 objections 2026", "ganna survey sudhar first day report up", "caneup satta correction samiti camp 2026", "scio ganna satta apatti nistaran"],
        "banner_img": "up-ganna-satta-disposal-day-1-18400-objections-resolved-2026.webp",
        "bg_img": os.path.join(brain_dir, "satta_pre_cal_1787581882990.jpg"),
        "tag": "सट्टा रिपोर्ट ⚡",
        "h1": "सट्टा सुधार के पहले दिन 18,400 आपत्तियां हल",
        "h2_html": "168 गन्ना समितियों में <span class='sub-highlight'>मौके पर ही हुआ सर्वे रिकॉर्ड सुधार</span>"
    },
    {
        "slug": "shamli-bijnor-sugar-mills-release-280-crore-cane-arrears-2026",
        "title": "शामली व बिजनौर की चीनी मिलों ने जारी किए ₹280 करोड़ — पेराई सत्र से पहले बकाए पर डीएम की सख्ती",
        "slug": "shamli-bijnor-sugar-mills-release-280-crore-cane-arrears-2026",
        "desc": "शामली, थानाभवन, ऊन और बिजनौर की चीनी मिलों ने आज शाम ₹280 करोड़ का अतिरिक्त गन्ना भुगतान किसानों के बैंक खातों में डीबीटी द्वारा ट्रांसफर कर दिया है। जिला प्रशासन ने 15 सितंबर तक 100% क्लीयरेंस का अल्टीमेटम दिया।",
        "date": "2026-09-01T18:20:00+05:30",
        "categories": ["Breaking News", "Ganna Bhugtan"],
        "tags": ["गन्ना भुगतान शामली बिजनौर", "280 Crore Payment", "Sugar Mill Arrears", "DM Ultimatum", "CaneUp News"],
        "keywords": ["shamli bijnor sugar mills 280 crore payment 1 september 2026", "thanabhawan un sugar factory ganna bhugtan", "bijnor mill payment clear dm order", "ganna bakaya 2026 up"],
        "banner_img": "shamli-bijnor-sugar-mills-release-280-crore-cane-arrears-2026.webp",
        "bg_img": os.path.join(brain_dir, "sugar_mill_payment_1787489145600.jpg"),
        "tag": "बड़ा भुगतान ⚡",
        "h1": "शामली व बिजनौर मिलों ने ₹280 करोड़ जारी किए",
        "h2_html": "पेराई सत्र से पहले <span class='sub-highlight'>किसानों के खातों में पहुंची धनराशि</span>"
    },
    {
        "slug": "imd-western-up-heavy-rainfall-drainage-advisory-september-2026",
        "title": "मौसम विभाग का अलर्ट — पश्चिमी यूपी में 2 से 4 सितंबर तक भारी बारिश, जलभराव से गन्ने को बचाने की सलाह",
        "desc": "मौसम विज्ञान विभाग (IMD) ने मुजफ्फरनगर, सहारनपुर, बिजनौर और मेरठ में भारी बारिश का येलो अलर्ट जारी किया है। गन्ना आयुक्त ने जलभराव वाले खेतों में तुरंत जल निकासी चैनल बनाने के निर्देश दिए।",
        "date": "2026-09-01T18:30:00+05:30",
        "categories": ["Breaking News", "Weather Alert"],
        "tags": ["मौसम अलर्ट पश्चिमी यूपी", "IMD Rain Warning", "जलभराव प्रबंधन", "गन्ना फसल सुरक्षा", "September Weather"],
        "keywords": ["imd western up heavy rain alert 2 4 september 2026", "muzaffarnagar saharanpur rain forecast sugarcane", "ganna khet waterlogging drainage advisory", "up weather update september 2026"],
        "banner_img": "imd-western-up-heavy-rainfall-drainage-advisory-september-2026.webp",
        "bg_img": os.path.join(brain_dir, "trench_buwai_1787582649543.jpg"),
        "tag": "मौसम अलर्ट ⚡",
        "h1": "पश्चिमी यूपी में 2 से 4 सितंबर भारी बारिश अलर्ट",
        "h2_html": "जलभराव से गन्ने को बचाने के लिए <span class='sub-highlight'>तुरंत जलनिकासी की सलाह</span>"
    },
    {
        "slug": "free-soil-health-card-camps-120-sugar-mill-zones-2026",
        "title": "यूपी के 120 चीनी मिल क्षेत्रों में कल से मुफ्त मृदा परीक्षण कैंप — शरदकालीन बुवाई के लिए मिलेगा सॉइल कार्ड",
        "desc": "गन्ना विकास और कृषि विभाग कल 2 सितंबर से 120 चीनी मिल परिक्षेत्रों में निःशुल्क मिट्टी जांच महा-अभियान शुरू कर रहा है। किसान अपने खेत की मिट्टी जांच कराकर संतुलित डीएपी और पोटाश का उपयोग कर सकेंगे।",
        "date": "2026-09-01T18:40:00+05:30",
        "categories": ["Breaking News", "Sarkari Yojana"],
        "tags": ["मुफ्त मृदा परीक्षण", "Soil Health Card UP", "120 Mill Zones", "शरदकालीन बुवाई", "संतुलित उर्वरक"],
        "keywords": ["free soil health card camps 120 sugar mill zones up", "mridha parikshan ganna buwai september 2026", "soil testing mobile van up cane dept", "sharadkalin ganna fertilizer balance"],
        "banner_img": "free-soil-health-card-camps-120-sugar-mill-zones-2026.webp",
        "bg_img": os.path.join(brain_dir, "farmer_satisfaction_1787582522776.jpg"),
        "tag": "मृदा जांच ⚡",
        "h1": "120 चीनी मिल क्षेत्रों में मुफ्त मृदा परीक्षण कैंप",
        "h2_html": "शरदकालीन बुवाई से पहले <span class='sub-highlight'>खेत की जांच व सॉइल हेल्थ कार्ड</span>"
    },
    {
        "slug": "balrampur-chini-lakhimpur-bioplastic-fmcg-orders-2026",
        "title": "बलरामपुर चीनी के लखीमपुर बायो-प्लास्टिक प्लांट को मिले बड़े कमर्शियल ऑर्डर — गन्ने से बनेगा इको-पैकेजिंग",
        "desc": "लखीमपुर खीरी के कुंभी में स्थापित देश के पहले ₹3,080 करोड़ के बायो-पॉलिमर प्लांट को नवंबर में चालू होने से पूर्व प्रमुख राष्ट्रीय पैकेजिंग और ई-कॉमर्स कंपनियों से आपूर्ति समझौते प्राप्त हुए हैं।",
        "date": "2026-09-01T18:50:00+05:30",
        "categories": ["Breaking News", "Sugar Industry"],
        "tags": ["बलरामपुर चीनी बायोप्लास्टिक", "Balrampur Bioyug PLA", "Lakhimpur Kumbhi", "Eco Packaging", "Green Industry"],
        "keywords": ["balrampur chini lakhimpur bioplastic plant orders 2026", "kumbhi pla biodegradable plastic plant up", "sugarcane to pla commercial launch november 2026", "balrampur bioyug off take agreement"],
        "banner_img": "balrampur-chini-lakhimpur-bioplastic-fmcg-orders-2026.webp",
        "bg_img": os.path.join(brain_dir, "balrampur_biopolymer_2026.webp"),
        "tag": "हरित उद्योग ⚡",
        "h1": "लखीमपुर बायो-प्लास्टिक प्लांट को बड़े कमर्शियल ऑर्डर",
        "h2_html": "गन्ने से बनेगा इको-प्लास्टिक, <span class='sub-highlight'>नवंबर से कमर्शियल उत्पादन</span>"
    },
    {
        "slug": "sugar-industry-demands-ethanol-price-hike-62-50-litre-2026",
        "title": "चीनी मिलों ने की बी-हैवी एथेनॉल दर ₹62.50 करने की मांग — पेट्रोलियम मंत्रालय को सौंपा विस्तृत प्रस्ताव",
        "desc": "इस्मा और यूपी शुगर मिल्स एसोसिएशन ने कच्चे माल की बढ़ती लागत के मद्देनजर बी-हैवी शीरे से बनने वाले एथेनॉल की खरीद दर ₹60.73 से बढ़ाकर ₹62.50 प्रति लीटर करने के लिए पेट्रोलियम मंत्रालय को मांग पत्र सौंपा है।",
        "date": "2026-09-01T19:00:00+05:30",
        "categories": ["Breaking News", "Sugar Industry"],
        "tags": ["एथेनॉल मूल्य वृद्धि", "ISMA Ethanol Pricing", "B Heavy Molasses", "Petroleum Ministry", "Sugar Mills"],
        "keywords": ["sugar industry demands ethanol price hike 62 50 2026", "b heavy ethanol price revision petroleum ministry", "isma sugar mill ethanol pricing formula", "biofuel procurement rates omc 2026 27"],
        "banner_img": "sugar-industry-demands-ethanol-price-hike-62-50-litre-2026.webp",
        "bg_img": os.path.join(brain_dir, "news9_ethanol_expansion_cover_1787948284345.jpg"),
        "tag": "मूल्य मांग ⚡",
        "h1": "बी-हैवी एथेनॉल दर ₹62.50 करने की मांग",
        "h2_html": "चीनी उद्योग ने पेट्रोलियम मंत्रालय को <span class='sub-highlight'>सौंपा विस्तृत लागत प्रस्ताव</span>"
    },
    {
        "slug": "punjab-announces-early-crushing-transport-subsidy-2026",
        "title": "पंजाब सरकार का बड़ा फैसला — 20 अक्टूबर से पहले पेराई शुरू करने वाली मिलों को ₹10/कुंतल ट्रांसपोर्ट सब्सिडी",
        "desc": "पंजाब के कृषि मंत्री ने घोषणा की है कि जो चीनी मिलें 20 अक्टूबर से पहले पेराई सत्र शुरू करेंगी, उन्हें गन्ने की ढुलाई पर प्रति क्विंटल ₹10 की अतिरिक्त राजकीय सहायता दी जाएगी ताकि पराली जलाने की समस्या थमे।",
        "date": "2026-09-01T19:10:00+05:30",
        "categories": ["Breaking News", "Sugar Industry"],
        "tags": ["पंजाब गन्ना पेराई सब्सिडी", "Punjab Early Crushing", "10 Rupees Subsidy", "Sugar Mills", "Kisan Parali"],
        "keywords": ["punjab early crushing transport subsidy 10 quintal 2026", "punjab sugar mills crushing 20 october incentive", "bhagwant mann ganna perai subsidy 2026 27", "sugar mill transport grant punjab"],
        "banner_img": "punjab-announces-early-crushing-transport-subsidy-2026.webp",
        "bg_img": os.path.join(brain_dir, "asmauli_sugar_factory_1787939335198.jpg"),
        "tag": "राजकीय छूट ⚡",
        "h1": "पंजाब: अगेती पेराई पर ₹10/कुंतल ट्रांसपोर्ट सब्सिडी",
        "h2_html": "20 अक्टूबर से पहले मिल चलाने पर <span class='sub-highlight'>मिलेगी अतिरिक्त सरकारी मदद</span>"
    },
    {
        "slug": "bku-7-day-ultimatum-smart-meters-tubewells-meerut-2026",
        "title": "नलकूपों पर स्मार्ट मीटर लगाने के खिलाफ भाकियू का अल्टीमेटम — पीवीवीएनएल मुख्यालय पर 7 दिन का नोटिस",
        "slug": "bku-7-day-ultimatum-smart-meters-tubewells-meerut-2026",
        "desc": "भारतीय किसान यूनियन ने मेरठ स्थित पश्चिमांचल विद्युत वितरण निगम (PVVNL) मुख्यालय पर धरना देकर कृषि नलकूपों पर जबरन स्मार्ट मीटर लगाने के विरोध में 7 दिन का अल्टीमेटम दिया है।",
        "date": "2026-09-01T19:20:00+05:30",
        "categories": ["Breaking News", "Farmer Protest"],
        "tags": ["स्मार्ट मीटर विरोध", "PVVNL Meerut", "BKU Ultimatum", "निःशुल्क कृषि बिजली", "Kisan Andolan"],
        "keywords": ["bku 7 day ultimatum smart meters tubewells meerut 2026", "pvvnl agriculture smart meter protest kisan", "free power sugarcane farmers up government", "bku meerut bijli vibhag dharna"],
        "banner_img": "bku-7-day-ultimatum-smart-meters-tubewells-meerut-2026.webp",
        "bg_img": os.path.join(brain_dir, "ws_kcc_loan_cover_1787906338029.jpg"),
        "tag": "किसान आंदोलन ⚡",
        "h1": "नलकूपों पर स्मार्ट मीटर के खिलाफ 7 दिन का अल्टीमेटम",
        "h2_html": "भाकियू ने पश्चिमांचल विद्युत मुख्यालय पर <span class='sub-highlight'>दिया कड़ा नोटिस</span>"
    },
    {
        "slug": "ccea-reviews-fertilizer-subsidy-dap-uninterrupted-supply-2026",
        "title": "केंद्रीय कैबिनेट का भरोसा — शरदकालीन गन्ना बुवाई के लिए ₹1,350/बोरी पर डीएपी की निर्बाध आपूर्ति रहेगी जारी",
        "desc": "आर्थिक मामलों की मंत्रिमंडलीय समिति (CCEA) ने उर्वरक सब्सिडी की समीक्षा कर आश्वासन दिया है कि आगामी रबी व शरदकालीन गन्ना बुवाई के लिए ₹1,350 प्रति बोरी की रियायती दर पर डीएपी और पोटाश का पर्याप्त बफर स्टॉक उपलब्ध है।",
        "date": "2026-09-01T19:30:00+05:30",
        "categories": ["Breaking News", "Sarkari Yojana"],
        "tags": ["डीएपी सब्सिडी 1350", "CCEA Fertilizer Decision", "शरदकालीन गन्ना खाद", "Subsidy Buffer", "Kisan Khad"],
        "keywords": ["ccea fertilizer subsidy review dap 1350 bag 2026", "uninterrupted dap potash supply sugarcane autumn", "iffco kribhco dap availability up cooperative", "khad subsidy cabinet committee review"],
        "banner_img": "ccea-reviews-fertilizer-subsidy-dap-uninterrupted-supply-2026.webp",
        "bg_img": os.path.join(brain_dir, "news8_harvester_subsidy_cover_1787948234294.jpg"),
        "tag": "खाद सब्सिडी ⚡",
        "h1": "शरदकालीन बुवाई के लिए ₹1,350 पर DAP की निर्बाध आपूर्ति",
        "h2_html": "केंद्रीय कैबिनेट ने उर्वरक बफर स्टॉक की <span class='sub-highlight'>समीक्षा कर दिया भरोसा</span>"
    }
]

# Step 1: Render All 10 BBC Style Banners via Headless Chrome
temp_html = os.path.join(img_dir, "_temp_eve_render.html")
temp_png = os.path.join(img_dir, "_temp_eve_render.png")

print("Rendering 10 BBC Style Featured Banners for September 1 Evening News...")

for idx, p in enumerate(sept1_evening_data, 1):
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
    font-size: 52px;
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

print("\nAll 10 Evening BBC Banners rendered successfully!")
