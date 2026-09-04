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
        "slug": "allahabad-high-court-strict-order-1936-crore-cane-dues-recovery-2026",
        "title": "इलाहाबाद हाईकोर्ट का सख्त आदेश — ₹1,936 करोड़ गन्ना बकाए की वसूली तेज करें सभी DM, 15 अक्टूबर तक रिपोर्ट तलब",
        "desc": "इलाहाबाद उच्च न्यायालय की लखनऊ खंडपीठ ने आरसी जारी होने के बावजूद किसानों का ₹1,936 करोड़ बकाया न चुकाने पर कड़ा रुख अपनाया है। सभी जिलाधिकारियों को 15 अक्टूबर तक वसूली रिपोर्ट दाखिल करने के आदेश दिए।",
        "date": "2026-09-04T07:00:00+05:30",
        "categories": ["Breaking News", "Ganna Bhugtan"],
        "tags": ["इलाहाबाद हाईकोर्ट आदेश", "₹1936 करोड़ बकाया", "RC Recovery DM Order", "गन्ना भुगतान 2026", "Lucknow Bench"],
        "keywords": ["allahabad high court strict order 1936 crore cane dues recovery 2026", "lucknow bench high court sugarcane arrears rc order", "dm recovery certificate sugar mill up 15 october", "ganna bhugtan high court hearing up"],
        "banner_img": "allahabad-high-court-strict-order-1936-crore-cane-dues-recovery-2026.webp",
        "bg_img": os.path.join(brain_dir, "sugar_mill_payment_1787489145600.jpg"),
        "tag": "हाईकोर्ट आदेश ⚡",
        "h1": "₹1,936 करोड़ गन्ना बकाए पर हाईकोर्ट सख्त",
        "h2_html": "सभी DM वसूली तेज करें, <span class='sub-highlight'>15 अक्टूबर तक मांगी प्रगति रिपोर्ट</span>"
    },
    {
        "slug": "simbhaoli-brijnathpur-sugar-mills-100-crore-clearance-order-2026",
        "title": "सिंभावली और बृजनाथपुर मिलों पर बड़ा फैसला — 15 अक्टूबर से पहले ₹100 करोड़ भुगतान का आदेश, किसानों को मिलेगी प्राथमिकता",
        "desc": "हापुड़ की सिंभावली और बृजनाथपुर चीनी मिलों पर किसानों के ₹200 करोड़ से अधिक के बकाए के मामले में एनसीएलटी और आईआरपी ने 15 अक्टूबर तक कम से कम ₹100 करोड़ का भुगतान करने का प्रस्ताव स्वीकृत किया है।",
        "date": "2026-09-04T07:15:00+05:30",
        "categories": ["Breaking News", "Ganna Bhugtan"],
        "tags": ["सिंभावली शुगर मिल भुगतान", "Brijnathpur Mill Hapur", "₹100 Crore Clearance", "IRP Resolution", "CaneUp News"],
        "keywords": ["simbhaoli brijnathpur sugar mills 100 crore clearance order 2026", "hapur ganna bhugtan simbhaoli mill ibc", "irp resolution plan farmer dues priority", "simbhaoli brijnathpur 15 october payment"],
        "banner_img": "simbhaoli-brijnathpur-sugar-mills-100-crore-clearance-order-2026.webp",
        "bg_img": os.path.join(brain_dir, "news4_bhugtan_3800cr_cover_1787948066221.jpg"),
        "tag": "मिल भुगतान ⚡",
        "h1": "सिंभावली मिलों पर ₹100 करोड़ भुगतान का आदेश",
        "h2_html": "15 अक्टूबर से पहले होगा भुगतान, <span class='sub-highlight'>किसानों को मिली सर्वोच्च प्राथमिकता</span>"
    },
    {
        "slug": "sp-chief-akhilesh-yadav-promises-24-hour-cane-payment-2026",
        "title": "गन्ना किसानों को 24 घंटे में भुगतान का वादा — 2027 चुनाव से पहले सपा सुप्रीमो अखिलेश यादव का बड़ा चुनावी दांव",
        "slug": "sp-chief-akhilesh-yadav-promises-24-hour-cane-payment-2026",
        "desc": "सपा अध्यक्ष अखिलेश यादव ने मुजफ्फरनगर और शामली में बयान जारी कर कहा कि 2027 में सत्ता में आने पर किसानों को तौल के 24 घंटे के भीतर गन्ना भुगतान सुनिश्चित किया जाएगा और बिजली के निजीकरण को रोका जाएगा।",
        "date": "2026-09-04T07:30:00+05:30",
        "categories": ["Breaking News", "MSP Rate"],
        "tags": ["24 घंटे में गन्ना भुगतान", "Akhilesh Yadav Cane Promise", "2027 Election", "Western UP Kisan", "गन्ना राजनीति"],
        "keywords": ["sp chief akhilesh yadav promises 24 hour cane payment 2026", "akhilesh yadav ganna bhugtan 24 ghante vada", "samajwadi party sugarcane policy western up", "ganna kisan rajneeti up assembly 2027"],
        "banner_img": "sp-chief-akhilesh-yadav-promises-24-hour-cane-payment-2026.webp",
        "bg_img": os.path.join(brain_dir, "farmer_satisfaction_1787582522776.jpg"),
        "tag": "बड़ा सियासी दांव ⚡",
        "h1": "24 घंटे में गन्ना भुगतान का बड़ा चुनावी वादा",
        "h2_html": "सपा प्रमुख अखिलेश यादव का ऐलान: <span class='sub-highlight'>तौल होते ही खाते में जाएगा पैसा</span>"
    },
    {
        "slug": "up-ganna-satta-campaign-day-4-68000-objections-resolved-2026",
        "title": "सट्टा सुधार अभियान के चौथे दिन 68,000 आपत्तियां हल — 45 जिलों में शाम 7 बजे तक खुले रहेंगे काउंटर",
        "slug": "up-ganna-satta-campaign-day-4-68000-objections-resolved-2026",
        "desc": "उत्तर प्रदेश गन्ना विकास विभाग ने चौथे दिन तक 68,500 किसानों की सट्टा व सर्वे त्रुटियों का समाधान किया है। किसानों की भारी भीड़ को देखते हुए समितियों के काउंटर अब शाम 7:00 बजे तक खुले रहेंगे।",
        "date": "2026-09-04T07:45:00+05:30",
        "categories": ["Breaking News", "CaneUp Guide"],
        "tags": ["सट्टा सुधार अभियान Day 4", "68000 Objections Resolved", "Counter Timing 7PM", "CaneUp UP", "गन्ना समिति"],
        "keywords": ["up ganna satta campaign day 4 68000 objections resolved 2026", "ganna samiti counter open till 7pm up", "enquiry caneup in satta correction day 4 report", "up cane commissioner emergency review meeting"],
        "banner_img": "up-ganna-satta-campaign-day-4-68000-objections-resolved-2026.webp",
        "bg_img": os.path.join(brain_dir, "satta_pre_cal_1787581882990.jpg"),
        "tag": "सट्टा प्रगति ⚡",
        "h1": "सट्टा सुधार के चौथे दिन 68,000 आपत्तियां हल",
        "h2_html": "किसानों की भारी भीड़ देख <span class='sub-highlight'>शाम 7 बजे तक खुलेंगे समिति काउंटर</span>"
    },
    {
        "slug": "dfpd-sugar-mills-7-day-quota-liquidation-mandate-2026",
        "title": "चीनी मिलों को केंद्र का सख्त निर्देश — 7 दिन में पाक्षिक कोटा न बेचने पर कोटा रद्द कर दूसरी मिलों को होगा ट्रांसफर",
        "slug": "dfpd-sugar-mills-7-day-quota-liquidation-mandate-2026",
        "desc": "केंद्रीय खाद्य एवं सार्वजनिक वितरण विभाग ने सभी चीनी मिलों को आदेश जारी किया है कि पाक्षिक रिलीज ऑर्डर के 7 दिन के भीतर आवंटित चीनी का डिस्पैच पूरा करें, अन्यथा कोटा जब्त कर अनुपालक मिलों को दिया जाएगा।",
        "date": "2026-09-04T08:00:00+05:30",
        "categories": ["Breaking News", "Sugar Industry"],
        "tags": ["7-Day Quota Rule", "DFPD Sugar Order", "पाक्षिक चीनी कोटा", "बाजार नियंत्रण", "Sugar Mills Penalty"],
        "keywords": ["dfpd sugar mills 7 day quota liquidation mandate 2026", "sugar mill domestic quota cancel reallocation", "food ministry sugar dispatch strict order", "ex mill sugar prices fall 20 percent"],
        "banner_img": "dfpd-sugar-mills-7-day-quota-liquidation-mandate-2026.webp",
        "bg_img": os.path.join(brain_dir, "ws_sugar_mills_1787597400680.jpg"),
        "tag": "मंत्रालय निर्देश ⚡",
        "h1": "7 दिन में पाक्षिक चीनी कोटा बेचना अनिवार्य",
        "h2_html": "लापरवाही पर कोटा रद्द होगा, <span class='sub-highlight'>अनुपालक मिलों को दिया जाएगा आवंटन</span>"
    },
    {
        "slug": "tehsil-24-hour-token-fast-tomorrow-5-september-kisan-morcha-2026",
        "title": "कल 5 सितंबर को 56 तहसीलों पर शुरू होगा 24 घंटे का उपवास — 8 सितंबर महापंचायत से पहले आर-पार का पूर्वाभ्यास",
        "slug": "tehsil-24-hour-token-fast-tomorrow-5-september-kisan-morcha-2026",
        "desc": "पश्चिमी उत्तर प्रदेश की सभी 56 तहसीलों पर कल सुबह 10 बजे से संयुक्त किसान मोर्चा और भाकियू का 24 घंटे का क्रमिक उपवास शुरू होगा। नलकूपों पर मीटर और ₹450 भाव की मांग को लेकर रणनीति तैयार।",
        "date": "2026-09-04T08:15:00+05:30",
        "categories": ["Breaking News", "Farmer Protest"],
        "tags": ["5 सितंबर तहसील उपवास", "56 Tehsils Protest", "SKM BKU Dharna", "Smart Meter Protest", "Mahapanchayat Rehearsal"],
        "keywords": ["tehsil 24 hour token fast tomorrow 5 september kisan morcha 2026", "western up 56 tehsil kisan dharna preparations", "smart meter nalkoop virodh bku sisauli", "gic ground muzaffarnagar mahapanchayat trailer"],
        "banner_img": "tehsil-24-hour-token-fast-tomorrow-5-september-kisan-morcha-2026.webp",
        "bg_img": os.path.join(brain_dir, "farmer_satisfaction_1787582522776.jpg"),
        "tag": "आंदोलन पूर्वाभ्यास ⚡",
        "h1": "कल 56 तहसीलों पर 24 घंटे का किसान उपवास",
        "h2_html": "8 सितंबर महापंचायत से पहले <span class='sub-highlight'>पश्चिमी यूपी में आर-पार की तैयारी</span>"
    },
    {
        "slug": "autumn-sugarcane-mustard-potato-intercropping-guidelines-upcsr-2026",
        "title": "शरद बुवाई में सह-फसली खेती से डबल मुनाफा — सरसों और आलू के साथ गन्ने की वैज्ञानिक बुवाई गाइड",
        "slug": "autumn-sugarcane-mustard-potato-intercropping-guidelines-upcsr-2026",
        "desc": "गन्ना शोध परिषद शाहजहांपुर ने शरद बुवाई में 4.5 फीट की दूरी पर ट्रेंच विधि से गन्ना बोकर बीच में पूसा-31 सरसों या कुफरी आलू लगाकर पहले 90 दिन में ₹50,000 प्रति एकड़ की अतिरिक्त आमदनी का फॉर्मूला दिया है।",
        "date": "2026-09-04T08:30:00+05:30",
        "categories": ["Breaking News", "Ganna Guide"],
        "tags": ["सरसों आलू सह-फसली खेती", "Sugarcane Intercropping Guide", "UPCSR Shahjahanpur", "शरद बुवाई डबल मुनाफा", "Trench Farming"],
        "keywords": ["autumn sugarcane mustard potato intercropping guidelines upcsr 2026", "ganna sarso aalu sah fasli kheti trench", "pusa mustard kufri potato sugarcane intercrop", "sharadkalin ganna sah fasli labh"],
        "banner_img": "autumn-sugarcane-mustard-potato-intercropping-guidelines-upcsr-2026.webp",
        "bg_img": os.path.join(brain_dir, "trench_buwai_1787582649543.jpg"),
        "tag": "डबल मुनाफा ⚡",
        "h1": "गन्ने के साथ सरसों-आलू की सह-फसली खेती",
        "h2_html": "ट्रेंच विधि से बुवाई करें, <span class='sub-highlight'>पहले 90 दिन में कमाएं अतिरिक्त ₹50,000</span>"
    },
    {
        "slug": "soil-health-card-camps-cover-45000-farmers-sugar-belt-up-2026",
        "title": "सॉइल हेल्थ कार्ड महा-अभियान — 45,000 गन्ना किसानों को मिले कार्ड, 60% मिट्टी में जैविक कार्बन की कमी",
        "slug": "soil-health-card-camps-cover-45000-farmers-sugar-belt-up-2026",
        "desc": "प्रदेश की 120 चीनी मिलों में आयोजित निःशुल्क मृदा परीक्षण शिविरों में 45,000 किसानों को सॉइल कार्ड दिए गए। वैज्ञानिकों ने रासायनिक खादों का अंधाधुंध प्रयोग रोककर प्रेसमड और हरी खाद अपनाने की सलाह दी।",
        "date": "2026-09-04T08:45:00+05:30",
        "categories": ["Breaking News", "Ganna Guide"],
        "tags": ["सॉइल हेल्थ कार्ड कैंप", "45000 Farmers Covered", "मृदा परीक्षण रिपोर्ट", "जैविक कार्बन सुधार", "Sugar Mill Zones"],
        "keywords": ["soil health card camps cover 45000 farmers sugar belt up 2026", "soil testing results organic carbon deficiency sugarcane", "pressmud green manure recommendation up", "free soil health card sugar mill up"],
        "banner_img": "soil-health-card-camps-cover-45000-farmers-sugar-belt-up-2026.webp",
        "bg_img": os.path.join(brain_dir, "farmer_satisfaction_1787582522776.jpg"),
        "tag": "मृदा रिपोर्ट ⚡",
        "h1": "45,000 गन्ना किसानों को मिले सॉइल हेल्थ कार्ड",
        "h2_html": "60% खेतों में कार्बन की कमी, <span class='sub-highlight'>वैज्ञानिकों ने दी प्रेसमड खाद की सलाह</span>"
    },
    {
        "slug": "pre-crushing-digital-weighbridge-stamping-completed-800-centers-2026",
        "title": "घटतौली मुक्त पेराई सत्र की ओर कदम — 800 गन्ना क्रय केंद्रों के डिजिटल कांटों की सीलिंग पूरी",
        "slug": "pre-crushing-digital-weighbridge-stamping-completed-800-centers-2026",
        "desc": "नाप-तौल विभाग ने पश्चिमी यूपी के मेरठ, सहारनपुर और मुरादाबाद मंडलों में 800 बाह्य गन्ना क्रय केंद्रों के वे-ब्रिज का इलेक्ट्रॉनिक सत्यापन और बारकोड सीलिंग का पहला चरण पूरा कर लिया है।",
        "date": "2026-09-04T09:00:00+05:30",
        "categories": ["Breaking News", "CaneUp Guide"],
        "tags": ["800 कांटों की सीलिंग पूरी", "Legal Metrology Stamping", "घटतौली रोकथाम 2026", "Digital Weighbridge", "Cane Purchase Center"],
        "keywords": ["pre crushing digital weighbridge stamping completed 800 centers 2026", "weighbridge calibration phase 1 western up", "legal metrology green certificate qr code", "sugar mill purchase center ghattoli roktham"],
        "banner_img": "pre-crushing-digital-weighbridge-stamping-completed-800-centers-2026.webp",
        "bg_img": os.path.join(brain_dir, "chandanpur_mill_cover_1787946872076.jpg"),
        "tag": "कांटा जांच ⚡",
        "h1": "800 गन्ना कांटों की डिजिटल सीलिंग पूरी",
        "h2_html": "घटतौली पर पूर्ण रोक के लिए <span class='sub-highlight'>नाप-तौल विभाग का पहला चरण संपन्न</span>"
    },
    {
        "slug": "kolkata-transit-sugar-stock-limit-4000-quintals-exemption-2026",
        "title": "चीनी स्टॉक सीमा में बड़ा संशोधन — पूर्वोत्तर सप्लाई के चलते कोलकाता क्षेत्र को 4,000 क्विंटल की विशेष छूट",
        "slug": "kolkata-transit-sugar-stock-limit-4000-quintals-exemption-2026",
        "desc": "केंद्रीय खाद्य मंत्रालय ने स्पष्ट किया है कि 15 सितंबर से लागू 2,000 क्विंटल स्टॉक सीमा पूरे देश में प्रभावी होगी, लेकिन पूर्वोत्तर राज्यों के ट्रांजिट हब होने के कारण कोलकाता और आसपास 4,000 क्विंटल की सीमा रहेगी।",
        "date": "2026-09-04T09:15:00+05:30",
        "categories": ["Breaking News", "Sugar Industry"],
        "tags": ["कोलकाता स्टॉक सीमा छूट", "Sugar Stock Limit Kolkata", "DFPD Clarification", "पूर्वोत्तर चीनी सप्लाई", "Sugar Market 2026"],
        "keywords": ["kolkata transit sugar stock limit 4000 quintals exemption 2026", "dfpd notification 2000 quintals dealer limit transit hub", "kolkata sugar wholesale northeast supply", "sugar stock control order amendment 2026"],
        "banner_img": "kolkata-transit-sugar-stock-limit-4000-quintals-exemption-2026.webp",
        "bg_img": os.path.join(brain_dir, "ws_sugar_mills_1787597400680.jpg"),
        "tag": "स्टॉक संशोधन ⚡",
        "h1": "चीनी स्टॉक सीमा: कोलकाता को 4,000 कुंतल की छूट",
        "h2_html": "पूर्वोत्तर राज्यों की सप्लाई के लिए <span class='sub-highlight'>केंद्र सरकार ने दी विशेष राहत</span>"
    }
]

# Step 1: Render All 10 BBC Style Banners via Headless Chrome
temp_html = os.path.join(img_dir, "_temp_sept4_render.html")
temp_png = os.path.join(img_dir, "_temp_sept4_render.png")

print("Rendering 10 BBC Style Featured Banners for September 4 Morning News...")

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

print("\nAll 10 September 4 Morning BBC Banners rendered successfully!")
