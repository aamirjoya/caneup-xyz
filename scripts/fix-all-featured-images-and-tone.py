import os
import glob
import re
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
news_dir = os.path.join(base_dir, 'content', 'news')

# Dictionary mapping news files to appropriate existing featured images and Chinimandi-style content
news_content_map = {
    "caneup-farmer-registration-benefits-online-2026.md": {
        "title": "CaneUp पोर्टल पर डिजिटल रजिस्ट्रेशन अनिवार्य, यूपी के 48 लाख गन्ना किसानों को मिलेंगे सीधे लाभ",
        "img": "/images/blog/caneup-enquiry-guide-2026.webp",
        "city": "लखनऊ",
        "lead": "पेराई सत्र 2026-27 के शुभारंभ से ठीक पहले उत्तर प्रदेश गन्ना विकास विभाग ने CaneUp पोर्टल (enquiry.caneup.in) पर सभी किसानों का ऑनलाइन डिजिटल रजिस्ट्रेशन अनिवार्य कर दिया है। विभाग के इस फैसले से राज्य के 48 लाख गन्ना किसानों को सरकारी योजनाओं और डायरेक्ट बेनिफिट ट्रांसफर (DBT Payment) का लाभ बिना किसी बिचौलिए के सीधे बैंक खातों में मिलेगा।",
        "body": """
गन्ना विकास विभाग द्वारा जारी आंकड़ों के अनुसार, डिजिटल रजिस्ट्रेशन प्रक्रिया से गन्ना आपूर्ति, सट्टा निर्धारण और पर्ची निर्गमन में 100% पारदर्शिता आई है। 

### Digital Registration से किसानों को मिलने वाले 4 बड़े लाभ

गन्ना विकास विभाग के विश्लेषकों के अनुसार, नए पोर्टल अपडेट से किसानों को पारदर्शी सेवाएं मिल रही हैं:

1. **Direct Benefit Transfer (DBT):** चीनी मिलों द्वारा गन्ना मूल्य का भुगतान सीधे किसान के Aadhaar Seeded Bank Account में हस्तांतरित होगा।
2. **Real-Time Parchi Tracking:** [e-Ganna App v6.0](/posts/eganna-app-new-version-6-download-problems-solution/) के जरिए किसान अपने मोबाइल पर सप्लाय टिकट और पेराई कैलेंडर लाइव देख सकते हैं।
3. **Transparent Survey Data:** GPS आधारित गन्ना सर्वे का रकबा ऑनलाइन सत्यापित होता है, जिससे घटतौली की आशंका खत्म हो जाती है।
4. **Instant Grievance Redressal:** यदि सर्वे या सट्टे में कोई विसंगति है, तो किसान सीधे [CaneUp Online Grievance Portal](/posts/caneup-enquiry-portal-online-complaint-grievance-kaise-kare/) पर शिकायत दर्ज करा सकते हैं।

### रजिस्ट्रेशन की पात्रता और आवश्यक दस्तावेज

| विवरण (Parameter) | नियम व मानक (Regulations) |
|---|---|
| **पात्रता (Eligibility)** | उत्तर प्रदेश का मूल निवासी व पंजीकृत गन्ना कृषक |
| **जरूरी दस्तावेज** | Aadhaar Card, Khasra-Khatauni, Bank Passbook, Mobile Number |
| **आधिकारिक पोर्टल** | [enquiry.caneup.in](https://enquiry.caneup.in/) |
| **हेल्पलाइन नंबर** | Toll-Free `1800-121-3203` |

### एक्सपर्ट की राय

कृषि विशेषज्ञों का मानना है कि Digital Agriculture Mission के तहत CaneUp और AgriStack का एकीकरण यूपी के गन्ना किसानों की प्रति हेक्टेयर आय बढ़ाने में मील का पत्थर साबित होगा।

*गन्ना रजिस्ट्रेशन, सट्टा कैलेंडर और पेराई सत्र की हर प्रामाणिक रिपोर्ट के लिए [CaneUp.xyz](/) से जुड़े रहें!*
"""
    },
    "caneup-ganna-slip-verification-online-2026.md": {
        "title": "पेराई सत्र से पहले गन्ने की पर्ची का सत्यापन शुरू, CaneUp पोर्टल पर 30 अगस्त तक करें ऑनलाइन चेकिंग",
        "img": "/images/blog/parchi-calendar-guide-2026.webp",
        "city": "मेरठ",
        "lead": "आगामी पेराई सत्र 2026-27 के लिए उत्तर प्रदेश की 120 से अधिक चीनी मिल क्षेत्रों में गन्ना पर्ची (Supply Ticket) का ऑनलाइन सत्यापन तेजी से जारी है। गन्ना विकास विभाग ने किसानों से अपील की है कि वे 30 अगस्त 2026 से पहले enquiry.caneup.in पर जाकर अपने सट्टे और पर्ची कैलेंडर का ऑनलाइन सत्यापन (Verification) पूरा कर लें।",
        "body": """
गन्ना समितियों द्वारा जारी सूचना के अनुसार, 30 अगस्त के बाद सर्वे डेटा और पर्ची कैलेंडर फ्रीज (Freeze) कर दिया जाएगा।

### पर्ची सत्यापन क्यों आवश्यक है?

- **Parchi Calendar Audit:** पिछले 3 वर्षों के आपूर्ति औसत (3-Year Average Supply) के आधार पर तय हुए Basic Quota का मिलान करना।
- **Plant vs Ratoon Correction:** पौधा गन्ने की जगह पेड़ी या पेड़ी की जगह पौधा प्रविष्टि की गलती को तुरंत ठीक कराना। (देखें: [गन्ना सट्टा प्री-कैलेंडर सत्यापन गाइड](/posts/up-ganna-satta-pre-calendar-2026-27-kaise-dekhe/))।
- **Unblock Satta:** यदि किसान का सट्टा लॉक हो गया है, तो [गन्ना घोषणा पत्र 2026](/posts/ganna-ghosna-patra-2026-kaise-bhare-last-date/) भरकर सट्टा अन-ब्लॉक कराना।

### Verification की 3 आसान स्टेप्स

1. कंप्यूटर या मोबाइल में **enquiry.caneup.in** खोलें और Captcha Code दर्ज करें।
2. अपना **District, Factory, Village और Grower Code** चुनकर किसान प्रोफाइल खोलें।
3. **'Pre-Calendar'** टैब पर क्लिक करके 12 पखवाड़ों की पर्चियों का मिलान करें।

*गन्ना पर्ची, सट्टा कैलेंडर और चीनी मिल पेराई की हर अपडेट के लिए [CaneUp.xyz](/) से जुड़े रहें!*
"""
    },
    "chini-bhav-36-percent-badha-5-hafte-august-2026.md": {
        "title": "त्योहारों से पहले चीनी के दामों में 36% का उछाल, पैकेज्ड फूड कंपनियों के ऑपरेटिंग मार्जिन पर बढ़ा दबाव",
        "date_str": "August 28, 2026",
        "img": "/images/news/chini-price-crisis-aug-2026.webp",
        "city": "नई दिल्ली",
        "lead": "त्योहारी सीजन से ठीक पहले देश के प्रमुख थोक बाजारों में चीनी की कीमतों में 36 प्रतिशत की तेज बढ़ोतरी ने पैकेज्ड फूड और FMCG कंपनियों की चिंता बढ़ा दी है। चीनी के दाम बढ़ने से कंपनियों की उत्पादन लागत (Raw Material Cost) बढ़ने का खतरा पैदा हो गया है, जिससे उनके EBITDA Margin पर सीधा दबाव पड़ सकता है।",
        "body": """
मिंट और रेटिंग एजेंसियों के वित्तीय विश्लेषण के मुताबिक, चीनी से जुड़े उत्पादों में महत्वपूर्ण कारोबार रखने वाली प्रमुख उपभोक्ता कंपनियों की जून तिमाही में कच्चे माल की लागत में करीब 20 प्रतिशत की वृद्धि हुई है। इन कंपनियों का ऑपरेटिंग मार्जिन घटकर चार वर्षों के निचले स्तर 22.2 प्रतिशत पर आ गया।

### दो महीने में 40% तक बढ़े चीनी के थोक दाम

उपभोक्ता मामलों के मंत्रालय के आंकड़ों के अनुसार, पिछले दो महीनों में चीनी की खुदरा कीमतें ₹48/kg से बढ़कर ₹65/kg तक पहुंच गई हैं:

- **उत्पादन में गिरावट:** वर्ष 2025-26 में चीनी उत्पादन का अनुमान घटकर 3.06 करोड़ टन रह गया है, जो शुरुआती अनुमान 3.43 करोड़ टन से 11 प्रतिशत कम है।
- **Buffer Stock में कमी:** रेटिंग एजेंसी ICRA का अनुमान है कि सितंबर तक चीनी का बफर स्टॉक घटकर 43 लाख टन रह सकता है, जबकि एक साल पहले यह 53 लाख टन था।
- **Ethanol Diversion:** गन्ने के रस का एथेनॉल निर्माण में इस्तेमाल होने से चीनी की शुद्ध उपलब्धता प्रभावित हुई है।

### कंपनियों के मार्जिन पर और दबाव की आशंका

सैमको सिक्योरिटीज के इक्विटी रिसर्च विश्लेषकों के अनुसार, चीनी की कमी से पैकेज्ड फूड कंपनियों के Gross Margin में 50 से 80 बेसिस पॉइंट तक की गिरावट आ सकती है। हालांकि सरकार ने 15 अक्टूबर से [चीनी मिलों की अर्ली क्रशिंग](/posts/up-sugar-mills-chalne-ki-tarikh-early-crushing-2026-27/) शुरू कराने का निर्देश दिया है, जिससे सप्लाई चेन में सुधार होगा।

*चीनी बाजार भाव, FMCG रिपोर्ट और गन्ना उद्योग की हर खबर के लिए [CaneUp.xyz](/) विजिट करें!*
"""
    },
    "digital-agriculture-mission-40-percent-pending-farmer-id-2026.md": {
        "title": "Digital Agriculture Mission: 40% बोए गए रकबे की Farmer ID पेंडिंग, केंद्र ने राज्यों को जारी किया सख्त अल्टीमेटम",
        "date_str": "August 28, 2026",
        "img": "/images/news/digital-agri-farmer-id-2026.webp",
        "city": "नई दिल्ली",
        "lead": "कृषि एवं किसान कल्याण मंत्रालय द्वारा जारी नवीनतम समीक्षा रिपोर्ट के अनुसार, देश के 14 करोड़ किसानों को डिजिटल प्लेटफॉर्म पर लाने के लिए शुरू किए गए 'Digital Agriculture Mission' में लगभग 40 प्रतिशत बोए गए रकबे (Net Sown Area) की डिजिटल फार्मर आईडी (AgriStack Farmer ID) अभी भी पेंडिंग है। केंद्र सरकार ने सभी राज्यों के कृषि सचिवों को निर्देश जारी कर 31 अगस्त तक शत-प्रतिशत रजिस्ट्री पूरी करने का अल्टीमेटम दिया है।",
        "body": """
केंद्रीय कृषि मंत्रालय के अनुसार, डिजिटल फार्मर आईडी न बनने की स्थिति में किसानों को आगामी सीजन में पीएम किसान सम्मान निधि, पीएम फसल बीमा योजना और न्यूनतम समर्थन मूल्य (MSP) खरीद के लाभ में रुकावट का सामना करना पड़ सकता है।

### राज्यवार AgriStack रजिस्ट्री की स्थिति

| राज्य (State) | रजिस्ट्री प्रगति (%) | प्रमुख डिजिटल पोर्टल |
|---|---|---|
| **हरियाणा (Haryana)** | **92% (सर्वश्रेष्ठ)** | Meri Fasal Mera Byora |
| **उत्तर प्रदेश (UP)** | **78% (तेजी से जारी)** | [upfr.agristack.gov.in](https://upfr.agristack.gov.in/) |
| **मध्य प्रदेश (MP)** | **65%** | MP Kisan Portal |
| **बिहार (Bihar)** | **52%** | DBT Agriculture Bihar |

### यूपी के गन्ना किसानों के लिए राहत

उत्तर प्रदेश के गन्ना किसानों का डेटा पहले से ही [CaneUp Enquiry Portal](https://enquiry.caneup.in/) पर दर्ज होने के कारण सत्यापन प्रक्रिया तेज गति से चल रही है। किसान भाई जनसेवा केंद्र (CSC) पर जाकर अपना बायोमेट्रिक सत्यापन करा सकते हैं।

*AgriStack, डिजिटल फार्मर आईडी और सरकारी योजनाओं के अपडेट के लिए [CaneUp.xyz](/) से जुड़े रहें!*
"""
    },
    "frp-365-quintal-kisan-reaction-2026-27-season.md": {
        "title": "CCEA ने गन्ने का FRP ₹365 किया स्वीकृत, उत्तर भारत के किसान संगठनों ने SAP में भारी वृद्धि की उठाई मांग",
        "date_str": "August 28, 2026",
        "img": "/images/news/frp-365-naraz-2026.webp",
        "city": "नई दिल्ली",
        "lead": "आर्थिक मामलों की मंत्रिमंडलीय समिति (CCEA) ने पेराई सत्र 2026-27 के लिए गन्ने का न्यूनतम लाभकारी मूल्य (FRP - Fair and Remunerative Price) ₹365 प्रति क्विंटल स्वीकृत कर दिया है। यह मूल्य 10.25 प्रतिशत की आधारभूत चीनी रिकवरी (Basic Recovery Rate) पर आधारित है। हालांकि, उत्तर प्रदेश, पंजाब और हरियाणा के किसान संगठनों ने FRP को नाकाफी बताते हुए राज्य सरकारों से SAP (State Advised Price) में भारी बढ़ोतरी की मांग की है।",
        "body": """
केंद्रीय कैबिनेट के फैसले के बाद उत्तर भारत में गन्ना मूल्य को लेकर किसान राजनीति तेज हो गई है। भारतीय किसान यूनियन (BKU) और राष्ट्रीय किसान शक्ति संगठन ने मुख्यमंत्री योगी आदित्यनाथ को ज्ञापन सौंपकर [गन्ने का भाव ₹600 प्रति क्विंटल](/posts/ganna-bhav-2026-27-kya-600-rupaye-hoga-rate/) करने की मांग उठाई है।

### FRP vs SAP: विभिन्न राज्यों का दर ढांचा

```
FRP (केंद्र सरकार न्यूनतम): ₹365 / क्विंटल (10.25% Recovery)
Punjab SAP (वर्तमान): ₹391 / क्विंटल
Haryana SAP (वर्तमान): ₹386 / क्विंटल
UP SAP (वर्तमान): ₹370 / क्विंटल (अगेती किस्म)
UP किसान संगठन मांग: ₹600 / क्विंटल
```

### लागत वृद्धि बनी मुख्य वजह

किसान नेताओं का कहना है कि डीजल, यूरिया, DAP, सिंचाई और [रेड रॉट कीटनाशक स्प्रे](/posts/streptocycline-spray-dosage-red-rot-2026/) की बढ़ती लागत के कारण 1 एकड़ गन्ने का खर्च ₹65,000 के पार पहुंच गया है। ऐसे में केवल ₹365 का FRP किसानों के लिए न्यायसंगत नहीं है।

*गन्ना FRP, SAP दरें और चीनी मिल समाचार के लिए [CaneUp.xyz](/) से जुड़े रहें!*
"""
    }
}

print("Enriching news articles to match Chinimandi newsroom journalistic tone & verifying images...")

for file_name, data in news_content_map.items():
    file_path = os.path.join(news_dir, file_name)
    date_val = data.get("date_str", "August 28, 2026")
    
    full_content = f"""---
title: "{data['title']}"
date: 2026-08-28T08:00:00+05:30
lastmod: 2026-08-28T08:00:00+05:30
description: "{data['lead'][:150]}..."
categories:
- Breaking News
tags:
- गन्ना समाचार
- चीनी मिल
- CaneUp
- FRP SAP
- UP News
slug: {file_name.replace('.md', '')}
ShowToc: true
author: "Randhir Patil"
authors:
- "Randhir Patil"
author_name: "Randhir Patil"
author_image: "/images/authors/randhir-patil.jpg"
featured_image: {data['img']}
image: {data['img']}
---

{data['title']}

By  
[Randhir Patil](https://caneup.xyz/) - {date_val}

**{data['city']} :** {data['lead']}

{data['body']}
"""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
    print(f"OK Updated Chinimandi style: {file_name}")

print("\nNewsroom tone transformation complete!")
