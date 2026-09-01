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

sept1_news_data = [
    {
        "slug": "sugar-stock-limit-order-effective-1-september-2026",
        "title": "चीनी स्टॉक सीमा का नया नियम आज 1 सितंबर से लागू — थोक उपभोक्ताओं पर 15 दिन के स्टॉक की पाबंदी",
        "desc": "केंद्र सरकार का चीनी स्टॉक सीमा आदेश आज 1 सितंबर से 30 नवंबर तक प्रभावी हो गया है। 10 मीट्रिक टन से अधिक खपत वाले थोक उपभोक्ताओं पर 15 दिन की सीमा और व्यापारियों पर सख्त निगरानी।",
        "date": "2026-09-01T07:00:00+05:30",
        "categories": ["Breaking News", "Sugar Industry"],
        "tags": ["चीनी स्टॉक सीमा", "Sugar Stock Limit", "खाद्य मंत्रालय", "जमाखोरी नियंत्रण", "CaneUp News"],
        "keywords": ["sugar stock limit order 1 september 2026", "bulk consumers 15 days stock sugar", "chini stock limit rules up", "sugar price regulation september 2026"],
        "banner_img": "sugar-stock-limit-order-effective-1-september-2026.webp",
        "bg_img": os.path.join(brain_dir, "ws_sugar_mills_1787597400680.jpg"),
        "tag": "बाजार नियम ⚡",
        "h1": "चीनी स्टॉक सीमा नियम आज 1 सितंबर से लागू",
        "h2_html": "थोक उपभोक्ताओं पर <span class='sub-highlight'>15 दिन के स्टॉक</span> की पाबंदी व कड़े नियम"
    },
    {
        "slug": "september-first-fortnight-13-lakh-tonne-sugar-sales-quota-2026",
        "title": "सितंबर के पहले पखवाड़े के लिए 13 लाख टन चीनी बिक्री कोटा जारी — त्योहारों से पहले बाजार में पर्याप्त आपूर्ति",
        "desc": "केंद्रीय खाद्य एवं सार्वजनिक वितरण मंत्रालय ने 1 से 15 सितंबर 2026 के लिए 13 लाख मीट्रिक टन चीनी का घरेलू बिक्री कोटा जारी किया है। नई पाक्षिक कोटा प्रणाली से कीमतों में स्थिरता की उम्मीद।",
        "date": "2026-09-01T07:10:00+05:30",
        "categories": ["Breaking News", "Sugar Industry"],
        "tags": ["चीनी बिक्री कोटा", "Sugar Quota September 2026", "13 LMT Quota", "खाद्य मंत्रालय", "Sugar Prices"],
        "keywords": ["september sugar sales quota 13 lmt 2026", "first fortnight sugar quota notification", "sugar mill domestic sales quota up", "chini quota release september 2026"],
        "banner_img": "september-first-fortnight-13-lakh-tonne-sugar-sales-quota-2026.webp",
        "bg_img": os.path.join(brain_dir, "news9_ethanol_expansion_cover_1787948284345.jpg"),
        "tag": "आपूर्ति कोटा ⚡",
        "h1": "सितंबर पखवाड़े के लिए 13 लाख टन चीनी कोटा",
        "h2_html": "त्योहारों से पहले बाजार में <span class='sub-highlight'>पर्याप्त आपूर्ति व मूल्य स्थिरता</span>"
    },
    {
        "slug": "up-ganna-satta-objection-disposal-campaign-1-15-september-2026",
        "title": "यूपी गन्ना सट्टा आपत्ति निस्तारण अभियान आज से शुरू — 15 सितंबर तक समितियों में होगा रिकॉर्ड सुधार",
        "desc": "उत्तर प्रदेश गन्ना विकास विभाग ने आज 1 सितंबर से 15 सितंबर तक 45 जिलों में विशेष सट्टा संशोधन अभियान शुरू किया है। सर्वे आंकड़ों में त्रुटि, बेसिक कोटा और रकबा सुधार के लिए 3-सदस्यीय कमेटी करेगी सुनवाई।",
        "date": "2026-09-01T07:20:00+05:30",
        "categories": ["Breaking News", "CaneUp Guide"],
        "tags": ["सट्टा संशोधन अभियान", "Ganna Satta Sudhar", "गन्ना विकास समिति", "15 September Deadline", "CaneUp"],
        "keywords": ["up ganna satta apatti nistaran 1 september 2026", "ganna survey sudhar committee meeting", "caneup satta pre calendar correction up", "ganna samiti satta sanshodhan 2026"],
        "banner_img": "up-ganna-satta-objection-disposal-campaign-1-15-september-2026.webp",
        "bg_img": os.path.join(brain_dir, "satta_pre_cal_1787581882990.jpg"),
        "tag": "सट्टा अभियान ⚡",
        "h1": "गन्ना सट्टा आपत्ति निस्तारण अभियान शुरू",
        "h2_html": "1 से 15 सितंबर तक <span class='sub-highlight'>समितियों में होगा रिकॉर्ड सुधार</span>"
    },
    {
        "slug": "western-up-sugar-mills-boiler-trial-maintenance-start-2026",
        "title": "पश्चिमी यूपी की 120 चीनी मिलों में मरम्मत का अंतिम चरण शुरू — 15 अक्टूबर से पेराई के लिए स्टीम ट्रायल",
        "desc": "मुजफ्फरनगर, शामली, मेरठ, बिजनौर और सहारनपुर की सभी चीनी मिलों में आज 1 सितंबर से बॉयलर टेस्टिंग और पेराई मशीनों का स्टीम ट्रायल शुरू कर दिया गया है। 15 अक्टूबर से अगेती पेराई की तैयारी।",
        "date": "2026-09-01T07:30:00+05:30",
        "categories": ["Breaking News", "Sugar Industry"],
        "tags": ["चीनी मिल मरम्मत", "Boiler Steam Trial", "15 October Crushing", "Western UP Mills", "Perai Season"],
        "keywords": ["western up sugar mills boiler trial 1 september 2026", "sugar mill maintenance early crushing 15 october", "muzaffarnagar meerut sugar factory preparation", "ganna perai satra 2026 27"],
        "banner_img": "western-up-sugar-mills-boiler-trial-maintenance-start-2026.webp",
        "bg_img": os.path.join(brain_dir, "chandanpur_mill_cover_1787946872076.jpg"),
        "tag": "मिल तैयारी ⚡",
        "h1": "120 चीनी मिलों में स्टीम ट्रायल व मरम्मत शुरू",
        "h2_html": "15 अक्टूबर से पेराई सत्र के लिए <span class='sub-highlight'>बॉयलर टेस्टिंग तेज</span>"
    },
    {
        "slug": "upcsr-september-ganna-potash-zinc-foliar-spray-advisory-2026",
        "title": "गन्ना शोध परिषद की सितंबर एडवाइजरी — पोटाश व जिंक के छिड़काव से 0.5% बढ़ेगी चीनी रिकवरी",
        "desc": "यूपी गन्ना शोध परिषद शाहजहांपुर ने सितंबर माह के लिए फसल पोषण एडवाइजरी जारी की है। 0:0:50 पोटेशियम सल्फेट और चिलेटेड जिंक के पर्णीय छिड़काव से गन्ने में सुक्रोज संचय और वजन में भारी बढ़ोतरी होगी।",
        "date": "2026-09-01T07:40:00+05:30",
        "categories": ["Breaking News", "Ganna Guide"],
        "tags": ["गन्ना शोध परिषद", "पोटाश स्प्रे", "जिंक छिड़काव", "Sugar Recovery", "September Farming"],
        "keywords": ["upcsr shahjahanpur september sugarcane advisory 2026", "potash 0 0 50 foliar spray sugarcane", "zinc spray sugarcane sugar recovery boost", "september ganne ki dekhbhal"],
        "banner_img": "upcsr-september-ganna-potash-zinc-foliar-spray-advisory-2026.webp",
        "bg_img": os.path.join(brain_dir, "trench_buwai_1787582649543.jpg"),
        "tag": "वैज्ञानिक सलाह ⚡",
        "h1": "गन्ना शोध परिषद की सितंबर एडवाइजरी",
        "h2_html": "पोटाश व जिंक छिड़काव से <span class='sub-highlight'>0.5% बढ़ेगी चीनी रिकवरी</span>"
    },
    {
        "slug": "meerut-saharanpur-drone-spraying-50-percent-subsidy-booking-2026",
        "title": "मेरठ व सहारनपुर मंडल में किसान ड्रोन छिड़काव पर 50% सब्सिडी — आज से ऑनलाइन स्लॉट बुकिंग शुरू",
        "desc": "गन्ना विकास विभाग ने मेरठ, सहारनपुर और मुरादाबाद मंडल के 8 जिलों में ड्रोन द्वारा कीटनाशक व नैनो यूरिया छिड़काव के लिए 50% सब्सिडी स्लॉट बुकिंग शुरू की है। प्रति एकड़ ₹250 में होगा छिड़काव।",
        "date": "2026-09-01T07:50:00+05:30",
        "categories": ["Breaking News", "Sarkari Yojana"],
        "tags": ["किसान ड्रोन सब्सिडी", "Drone Spraying UP", "मेरठ सहारनपुर", "गन्ना छिड़काव", "50 Percent Subsidy"],
        "keywords": ["meerut saharanpur drone spraying booking 1 september 2026", "kisan drone subsidy 50 percent up cane", "drone spray red rot top borer sugarcane", "caneup drone booking portal 2026"],
        "banner_img": "meerut-saharanpur-drone-spraying-50-percent-subsidy-booking-2026.webp",
        "bg_img": os.path.join(brain_dir, "farmer_satisfaction_1787582522776.jpg"),
        "tag": "ड्रोन सब्सिडी ⚡",
        "h1": "ड्रोन छिड़काव पर 50% सरकारी सब्सिडी शुरू",
        "h2_html": "मेरठ व सहारनपुर में <span class='sub-highlight'>₹250 प्रति एकड़ में होगा स्प्रे</span>"
    },
    {
        "slug": "nbcc-sugarcane-syrup-ethanol-allocation-2026-27-boost",
        "title": "राष्ट्रीय जैव ईंधन समन्वय समिति ने गन्ने के रस से एथेनॉल उत्पादन को दी हरी झंडी — मिलों को प्रोत्साहन",
        "desc": "पेट्रोलियम मंत्रालय की जैव ईंधन समन्वय समिति (NBCC) ने 2026-27 आपूर्ति वर्ष के लिए गन्ने के सीधे रस और बी-हैवी शीरे से एथेनॉल उत्पादन की मात्रा को मंजूरी दे दी है। चीनी मिलों को अतिरिक्त लिक्विडिटी मिलेगी।",
        "date": "2026-09-01T08:00:00+05:30",
        "categories": ["Breaking News", "Sugar Industry"],
        "tags": ["एथेनॉल आवंटन", "Sugarcane Ethanol", "NBCC Decision", "Sugar Mills", "Biofuel Policy"],
        "keywords": ["nbcc sugarcane syrup ethanol allocation 2026 27", "b heavy molasses ethanol diversion boost", "sugar mill ethanol tender omc september 2026", "ethanol blending target india"],
        "banner_img": "nbcc-sugarcane-syrup-ethanol-allocation-2026-27-boost.webp",
        "bg_img": os.path.join(brain_dir, "ws_sugar_mills_1787597400680.jpg"),
        "tag": "जैव ईंधन ⚡",
        "h1": "गन्ने के रस से एथेनॉल उत्पादन को हरी झंडी",
        "h2_html": "2026-27 सत्र के लिए <span class='sub-highlight'>चीनी मिलों को बड़ा प्रोत्साहन</span>"
    },
    {
        "slug": "up-cooperative-banks-10-day-kcc-renewal-camps-september-2026",
        "title": "यूपी सहकारी बैंकों का 10 दिवसीय विशेष KCC नवीनीकरण अभियान शुरू — 4% ब्याज दर का लाभ उठाएं किसान",
        "desc": "उत्तर प्रदेश राज्य सहकारी बैंक और जिला सहकारी बैंकों ने आज 1 सितंबर से 10 सितंबर तक 45 गन्ना बाहुल्य जिलों में विशेष केसीसी कैंप शुरू किए हैं। समय पर रिन्युअल कराने वाले किसानों को 3% ब्याज छूट मिलेगी।",
        "date": "2026-09-01T08:10:00+05:30",
        "categories": ["Breaking News", "Sarkari Yojana"],
        "tags": ["KCC नवीनीकरण", "Cooperative Bank Camp", "4 Percent Interest", "Kisan Loan", "Ganna Kisan"],
        "keywords": ["up cooperative bank kcc renewal camp 1 september 2026", "kisan credit card 4 percent interest renewal", "dccb branch kcc camp 45 districts up", "ganna kisan kcc loan benefit 2026"],
        "banner_img": "up-cooperative-banks-10-day-kcc-renewal-camps-september-2026.webp",
        "bg_img": os.path.join(brain_dir, "ws_kcc_loan_cover_1787906338029.jpg"),
        "tag": "किसान ऋण ⚡",
        "h1": "सहकारी बैंकों का 10 दिवसीय KCC कैंप शुरू",
        "h2_html": "समय पर रिन्युअल पर <span class='sub-highlight'>मात्र 4% ब्याज का लाभ</span> उठाएं"
    },
    {
        "slug": "bku-muzaffarnagar-kisan-mahapanchayat-450-sap-demand-2026",
        "title": "मुजफ्फरनगर में 8 सितंबर को किसान महापंचायत का ऐलान — गन्ने का भाव ₹450 प्रति क्विंटल घोषित करने की मांग",
        "desc": "भारतीय किसान यूनियन (भाकियू) ने पेराई सत्र 2026-27 के लिए गन्ने का मूल्य ₹450 प्रति क्विंटल करने की मांग को लेकर 8 सितंबर को मुजफ्फरनगर के जीआईसी मैदान में विशाल किसान महापंचायत बुलाई है।",
        "date": "2026-09-01T08:20:00+05:30",
        "categories": ["Breaking News", "Farmer Protest"],
        "tags": ["किसान महापंचायत", "BKU Muzaffarnagar", "गन्ना मूल्य 450 मांग", "Rakesh Tikait", "Kisan Andolan"],
        "keywords": ["bku muzaffarnagar kisan mahapanchayat 8 september 2026", "ganna bhav 450 demand bku tikait", "muzaffarnagar kisan panchayat ganna sap", "up kisan morcha sugar mill protest 2026"],
        "banner_img": "bku-muzaffarnagar-kisan-mahapanchayat-450-sap-demand-2026.webp",
        "bg_img": os.path.join(brain_dir, "farmer_satisfaction_1787582522776.jpg"),
        "tag": "किसान महापंचायत ⚡",
        "h1": "मुजफ्फरनगर में 8 सितंबर को किसान महापंचायत",
        "h2_html": "गन्ने का भाव <span class='sub-highlight'>₹450/कुंतल घोषित करने</span> की मांग"
    },
    {
        "slug": "haryana-cabinet-ganna-sap-405-quintal-proposal-review-2026",
        "title": "हरियाणा कैबिनेट में गन्ने का भाव ₹405 करने का प्रस्ताव तैयार — देश में सबसे महंगे गन्ने का रिकॉर्ड कायम",
        "desc": "हरियाणा कृषि एवं किसान कल्याण विभाग ने आगामी पेराई सत्र के लिए गन्ने का राज्य परामर्शित मूल्य ₹405 प्रति क्विंटल करने का अंतिम कैबिनेट नोट तैयार कर लिया है। मुख्यमंत्री की अध्यक्षता में इस सप्ताह मुहर लगने की संभावना।",
        "date": "2026-09-01T08:30:00+05:30",
        "categories": ["Breaking News", "MSP Rate"],
        "tags": ["हरियाणा गन्ना भाव", "Haryana Ganna SAP 405", "Cabinet Proposal", "Kisan MSP", "Sugar Price"],
        "keywords": ["haryana cabinet ganna sap 405 proposal 2026", "haryana sugarcane price 405 quintal record", "chd ganna bhav haryana assembly review", "up haryana ganna sap rate comparison 2026"],
        "banner_img": "haryana-cabinet-ganna-sap-405-quintal-proposal-review-2026.webp",
        "bg_img": os.path.join(brain_dir, "ws_bhav_600_1787597306153.jpg"),
        "tag": "कैबिनेट फैसला ⚡",
        "h1": "हरियाणा में गन्ने का भाव ₹405 करने का प्रस्ताव",
        "h2_html": "देश में <span class='sub-highlight'>सबसे महंगे गन्ने का रिकॉर्ड</span> बनाने की तैयारी"
    }
]

# Step 1: Render All 10 BBC Style Banners via Chrome Headless
temp_html = os.path.join(img_dir, "_temp_news_render.html")
temp_png = os.path.join(img_dir, "_temp_news_render.png")

print("Rendering 10 BBC Style Featured Banners for September 1 Morning News...")

for idx, p in enumerate(sept1_news_data, 1):
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
    font-size: 54px;
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
    font-size: 36px;
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

# Cleanup temporary render files
if os.path.exists(temp_html):
    os.remove(temp_html)
if os.path.exists(temp_png):
    os.remove(temp_png)

print("\nAll 10 BBC Banners rendered successfully!")
