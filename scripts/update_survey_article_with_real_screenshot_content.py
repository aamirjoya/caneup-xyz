# -*- coding: utf-8 -*-
"""
update_survey_article_with_real_screenshot_content.py
Enriches the Ganna Survey 2026-27 article with the real-world live portal screenshot,
farmer profile analysis, 15 portal tabs breakdown, 4-plot survey data table,
and GPS 4-directional perimeter calculation formula.
"""
import os

blog_file = r"c:\Users\caneu\Downloads\caneup-xyz-restore\content\posts\ganna-survey-data-2026-27-portal-online-check-kaise-kare.md"
news_file = r"c:\Users\caneu\Downloads\caneup-xyz-restore\content\news\ganna-survey-data-2026-27-portal-online-check-kaise-kare.md"

full_article_content = """---
title: "गन्ना सर्वे डेटा (2026-27) पोर्टल पर ऑनलाइन जारी — ऐसे चेक करें गाटा संख्या, रकबा और पेड़ी-पौधा विवरण"
date: 2026-09-25T09:00:00+05:30
lastmod: 2026-09-25T09:10:00+05:30
description: "UP गन्ना विभाग ने पेराई सत्र 2026-27 के लिए गन्ना सर्वे डेटा enquiry.caneup.in पोर्टल और eGanna App पर ऑनलाइन जारी कर दिया है। देखें लाइव पोर्टल स्क्रीनशॉट, गाटा संख्या, 4-दिशा परिमाप, रकबा और 15 मुख्य टैब्स का पूरा विवरण।"
slug: ganna-survey-data-2026-27-portal-online-check-kaise-kare
categories:
  - CaneUp Guide
  - Parchi Calendar
  - Sarkari Yojana
tags:
  - गन्ना सर्वे 2026-27
  - ganna survey check online
  - enquiry caneup in survey
  - gata number ganna survey
  - ganna satta objection
  - up sugarcane survey 2026
  - eGanna app survey
keywords:
  - "गन्ना सर्वे डेटा 2026-27"
  - "ganna survey online check"
  - "enquiry caneup in survey data"
  - "गन्ना सर्वे कैसे देखें"
  - "गाटा अनुसार गन्ना सर्वे"
  - "ganna satta aapatthi"
  - "caneup survey check 2026"
ShowToc: true
author: "Aamir Raza"
authors:
  - "Aamir Raza"
author_name: "Aamir Raza"
author_image: "/images/authors/aamir-raza.webp"
featured_image: "/images/blog/ganna-survey-data-2026-27-portal-online-check.webp"
image: "/images/blog/ganna-survey-data-2026-27-portal-online-check.webp"
---

**गन्ना सर्वे डेटा 2026-27 ऑनलाइन:** उत्तर प्रदेश के 50 लाख से अधिक गन्ना किसानों के लिए राहत भरी और बेहद महत्वपूर्ण खबर है। उत्तर प्रदेश गन्ना एवं चीनी आयुक्त कार्यालय द्वारा आगामी पेराई सत्र 2026-27 के लिए राज्य के सभी 60 गन्ना उत्पादक जिलों का **जीपीएस आधारित गन्ना सर्वे डेटा (GPS C-Cam Survey Data)** आधिकारिक वेब पोर्टल **enquiry.caneup.in** और **eGanna App** पर ऑनलाइन प्रदर्शित (Live) कर दिया गया है।

यदि आप भी उत्तर प्रदेश के किसी भी जिले में गन्ने की खेती करते हैं और चीनी मिल को गन्ना आपूर्ति करते हैं, तो आज ही अपना सर्वे डेटा ऑनलाइन जांच लें। सर्वे डेटा में किसी भी प्रकार की लिपिकीय त्रुटि (जैसे रकबा कम दर्ज होना, पौधा की जगह पेड़ी चढ़ जाना या गाटा संख्या गलत होना) होने पर आपकी पर्चियों की संख्या कम हो सकती है। गन्ना विभाग ने स्पष्ट किया है कि अंतिम सट्टा लॉक होने से पहले किसानों के पास ऑनलाइन और ऑफलाइन आपत्ति दर्ज कराने का यह अंतिम अवसर है।

---

## 📸 लाइव पोर्टल स्क्रीनशॉट: गन्ना सर्वे डेटा (2026-27) कैसा दिखता है?

नीचे दिए गए आधिकारिक पोर्टल स्क्रीनशॉट में आप देख सकते हैं कि जब कोई किसान `enquiry.caneup.in` पर अपना प्रोफाइल खोलता है, तो किस प्रकार उसके किसान कोड, समिति, चीनी मिल, मूल बेसिक कोटे और सभी खेतों के **प्लाटवार सर्वे (Plot-wise Survey)** का पूरा कच्चा-चिट्ठा सामने आता है:

<figure style="margin:24px 0;text-align:center;">
  <img src="/images/blog/ganna-survey-portal-live-screenshot-2026-27.webp" alt="UP Cane Department enquiry.caneup.in Live Survey Data Screenshot 2026-27" style="width:100%;max-width:960px;height:auto;border-radius:10px;border:2px solid #15803d;box-shadow:0 6px 20px rgba(0,0,0,0.12);" loading="lazy">
  <figcaption style="font-size:13px;color:#4b5563;margin-top:10px;font-weight:600;">
    ▲ उत्तर प्रदेश चीनी उद्योग एवं गन्ना विकास विभाग: आधिकारिक पोर्टल enquiry.caneup.in पर लाइव किसान प्रोफाइल एवं प्लाटवार सर्वेक्षण का वास्तविक विवरण
  </figcaption>
</figure>

---

## लाइव उदाहरण द्वारा समझें: असमोली चीनी मिल (सम्भल) का वास्तविक केस-स्टडी

उपरोक्त लाइव स्क्रीनशॉट के आधार पर आइए समझते हैं कि पोर्टल पर दर्ज एक-एक आंकड़े और कॉलम का क्या अर्थ है:

### 1. किसान एवं समिति का प्राथमिक विवरण
* **चीनी मिल एवं समिति:** **Asmauli (असमोली)**, जनपद: **Sambhal (सम्भल)**
* **किसान का नाम व कोड:** **MAROOJ ALAM** (Grower Code: **27630**)
* **पिता का नाम:** HAMMAD AHMAD
* **राजस्व गांव:** **SALEM PUR HAJI PUR** (Village Code: **4071**)
* **आपूर्ति केंद्र (Supply Centre):** **DHAKIYA** (Centre Code: **6**)
* **आपूर्ति माध्यम (Mode of Supply):** **Cart-18 (18 क्विंटल बुग्गी/बैलगाड़ी)**
* **मूल बेसिक कोटा (Basic Quota):** **539.00 क्विंटल**
* **कुल सट्टा (Total Bonding):** **539.00 क्विंटल**
* **औसत उपज (Crop Yield):** **861.08 क्विंटल/हेक्टेयर** (फैक्टरी औसत आपूर्ति: 410.83 क्विंटल/हेक्टेयर)
* **कुल जोत क्षेत्रफल:** **1.148 हेक्टेयर** | **प्रभावी गन्ना क्षेत्रफल:** **1.148 हेक्टेयर**
* **बैंक खाता:** UP GRAMIN BANK (IFSC: BARB0BUPGBX)

---

## 📑 पोर्टल पर उपलब्ध सभी 15 महत्वपूर्ण टैब्स की कार्यप्रणाली

जब आप अपनी किसान प्रोफाइल खोलते हैं, तो स्क्रीन पर हरे रंग की पट्टी में **15 विशिष्ट टैब** दिखाई देते हैं। प्रत्येक टैब का उपयोग निम्न प्रकार है:

1. **सर्वे डेटा (2026-27):** (वर्तमान में एक्टिव) इसमें आपके सभी खेतों के गाटा नंबर, पेड़ी-पौधा किस्म और जीपीएस माप का संपूर्ण विवरण होता है।
2. **प्री कैलेंडर (Pre-Calendar):** सर्वे के आधार पर सत्र शुरू होने से पहले संभावित पर्चियों का कच्चा ड्राफ्ट।
3. **गन्ना कैलेंडर (Cane Calendar):** अंतिम रूप से स्वीकृत 12 पखवाड़े और 15 कॉलम का आपूर्ति कैलेंडर।
4. **अतिरिक्त सट्टा कैलेंडर (Additional Bonding):** बेसिक कोटे से अतिरिक्त स्वीकृत 80-85% गन्ने की पर्चियां।
5. **स्टैंडिंग केन कैलेंडर:** खेत में खड़े गन्ने के भौतिक सत्यापन के आधार पर विशेष पर्ची आवंटन।
6. **सप्लाई टिकट (Supply Ticket):** जारी हो चुकी डिजिटल SMS पर्ची, उसका गेट नंबर और वैधता अवधि।
7. **गन्ना तौल (Cane Weighment):** वर्तमान सत्र में तौल केंद्र पर तुले गन्ने का सकल, खाली और शुद्ध वजन।
8. **गत वर्ष गन्ना तौल:** पिछले 5 वर्षों में की गई वास्तविक गन्ना आपूर्ति का रिकॉर्ड (जिससे बेसिक कोटा तय होता है)।
9. **एस० एम० एस० लॉग (SMS Log):** विभाग द्वारा आपके मोबाइल नंबर पर भेजे गए सभी सरकारी मैसेजों की तारीख व समय।
10. **गन्ना निवेश की उपलब्धता:** आपकी गन्ना विकास समिति में उपलब्ध डीएपी, यूरिया, कीटनाशक व सूक्ष्म पोषक तत्वों का स्टॉक।
11. **गन्ना मूल्य की जानकारी:** राज्य सरकार द्वारा घोषित राज्य समर्थित मूल्य (SAP) और प्रति क्विंटल दर।
12. **फार्म मशीनरी यन्त्रों की बुकिंग:** कस्टम हायरिंग सेंटर (CHC) से ट्रेंच ओपनर, रोटावेटर या रिजर किराए पर बुक करने की सुविधा।
13. **शिकायत की जानकारी (File Complaint):** ऑनलाइन आपत्ति दर्ज कराने और समाधान की स्थिति जांचने का विकल्प।
14. **गन्ना बीज की उपलब्धता:** शोध परिषद (UPCSR) द्वारा उत्पादित प्रमाणित नई किस्मों के बीजों की बुकिंग।
15. **तौल लिपिकों की पोस्टिंग:** आपके आवंटित क्रय केंद्र पर तैनात चीनी मिल के तौल क्लर्क का नाम व ड्यूटी रोस्टर।

---

## 🗺️ प्लाटवार गन्ना सर्वेक्षण विवरण (2026-27): सम्पूर्ण तालिका व डिकोडिंग

लाइव स्क्रीनशॉट में दिए गए लाल हेडर वाले बॉक्स **"प्लाटवार गन्ना सर्वेक्षण का विवरण(2026-27)"** का पूरा विवरण नीचे दिया गया है:

<div style="overflow-x:auto;">
<table style="width:100%;border-collapse:collapse;margin:18px 0;font-size:13px;border:1px solid #cbd5e1;">
  <thead>
    <tr style="background:#dc2626;color:#ffffff;text-align:center;">
      <th style="padding:10px 8px;border:1px solid #b91c1c;">क्रम सं०</th>
      <th style="padding:10px 8px;border:1px solid #b91c1c;">प्लाट ग्राम</th>
      <th style="padding:10px 8px;border:1px solid #b91c1c;">सर्वेक्षण प्लाट (गाटा सं०)</th>
      <th style="padding:10px 8px;border:1px solid #b91c1c;">पेड़ी (Ratoon)</th>
      <th style="padding:10px 8px;border:1px solid #b91c1c;">पौधा (Plant)</th>
      <th style="padding:10px 8px;border:1px solid #b91c1c;">परिमाप (पू०) (मी०)</th>
      <th style="padding:10px 8px;border:1px solid #b91c1c;">परिमाप (प०) (मी०)</th>
      <th style="padding:10px 8px;border:1px solid #b91c1c;">परिमाप (उ०) (मी०)</th>
      <th style="padding:10px 8px;border:1px solid #b91c1c;">परिमाप (द०) (मी०)</th>
      <th style="padding:10px 8px;border:1px solid #b91c1c;">गन्ना क्षेत्रफल (है०)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#ffffff;text-align:center;">
      <td style="padding:9px;border:1px solid #e2e8f0;font-weight:700;">1</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">SALEM PUR HAJI PUR</td>
      <td style="padding:9px;border:1px solid #e2e8f0;font-weight:700;">259</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">—</td>
      <td style="padding:9px;border:1px solid #e2e8f0;color:#15803d;font-weight:700;">Co.-05011(S)</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">139.00</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">142.00</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">33.00</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">28.00</td>
      <td style="padding:9px;border:1px solid #e2e8f0;font-weight:700;color:#0f172a;">0.429</td>
    </tr>
    <tr style="background:#f8fafc;text-align:center;">
      <td style="padding:9px;border:1px solid #e2e8f0;font-weight:700;">2</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">SALEM PUR HAJI PUR</td>
      <td style="padding:9px;border:1px solid #e2e8f0;font-weight:700;">454</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">—</td>
      <td style="padding:9px;border:1px solid #e2e8f0;color:#15803d;font-weight:700;">Co.-05011(S)</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">66.00</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">69.00</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">36.00</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">66.00</td>
      <td style="padding:9px;border:1px solid #e2e8f0;font-weight:700;color:#0f172a;">0.172</td>
    </tr>
    <tr style="background:#ffffff;text-align:center;">
      <td style="padding:9px;border:1px solid #e2e8f0;font-weight:700;">3</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">SALEM PUR HAJI PUR</td>
      <td style="padding:9px;border:1px solid #e2e8f0;font-weight:700;">251</td>
      <td style="padding:9px;border:1px solid #e2e8f0;color:#b45309;font-weight:700;">Co.S.-13235</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">—</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">60.00</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">64.00</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">54.00</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">51.00</td>
      <td style="padding:9px;border:1px solid #e2e8f0;font-weight:700;color:#0f172a;">0.293</td>
    </tr>
    <tr style="background:#f8fafc;text-align:center;">
      <td style="padding:9px;border:1px solid #e2e8f0;font-weight:700;">4</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">SALEM PUR HAJI PUR</td>
      <td style="padding:9px;border:1px solid #e2e8f0;font-weight:700;">1000000031</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">—</td>
      <td style="padding:9px;border:1px solid #e2e8f0;color:#15803d;font-weight:700;">Co.-0118</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">46.00</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">60.00</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">66.00</td>
      <td style="padding:9px;border:1px solid #e2e8f0;">64.00</td>
      <td style="padding:9px;border:1px solid #e2e8f0;font-weight:700;color:#0f172a;">0.344</td>
    </tr>
    <tr style="background:#f1f5f9;font-weight:800;text-align:center;">
      <td colspan="9" style="padding:11px;border:1px solid #cbd5e1;text-align:right;color:#0f172a;font-size:14px;">कुल गन्ने का क्षेत्रफल (Total Sugarcane Area):</td>
      <td style="padding:11px;border:1px solid #cbd5e1;color:#dc2626;font-size:15px;">1.238 हेक्टेयर</td>
    </tr>
  </tbody>
</table>
</div>

---

## 📐 जीपीएस 4-दिशा परिमाप (Perimeter) से रकबा निकालने का गणित

कई किसान सोचते हैं कि सर्वेयर ने खेत का क्षेत्रफल कैसे निकाला। उत्तर प्रदेश गन्ना विभाग में क्षेत्रफल निकालने का स्वीकृत वैज्ञानिक फॉर्मूला निम्नलिखित है:

$$\\text{औसत लंबाई} = \\frac{\\text{पूर्व परिमाप} + \\text{पश्चिम परिमाप}}{2}$$

$$\\text{औसत चौड़ाई} = \\frac{\\text{उत्तर परिमाप} + \\text{दक्षिण परिमाप}}{2}$$

$$\\text{क्षेत्रफल (हेक्टेयर)} = \\frac{\\text{औसत लंबाई} \\times \\text{औसत चौड़ाई}}{10,000}$$

### आइए प्लाट संख्या 1 (गाटा 259) का हिसाब लगाकर देखें:
* पूर्व भुजा = 139.00 मीटर, पश्चिम भुजा = 142.00 मीटर  
  $$\\text{औसत लंबाई} = \\frac{139.00 + 142.00}{2} = 140.50 \\text{ मीटर}$$
* उत्तर भुजा = 33.00 मीटर, दक्षिण भुजा = 28.00 मीटर  
  $$\\text{औसत चौड़ाई} = \\frac{33.00 + 28.00}{2} = 30.50 \\text{ मीटर}$$
* कुल वर्ग मीटर = $140.50 \\times 30.50 = 4,285.25 \\text{ वर्ग मीटर}$
* हेक्टेयर में रकबा = $\\frac{4,285.25}{10,000} = \\mathbf{0.4285 \\approx 0.429 \\text{ हेक्टेयर}}$

इस प्रकार प्रत्येक किसान अपने मोबाइल में स्वयं चेक कर सकता है कि उसके खेत की जीपीएस नपाई बिल्कुल सही हुई है या नहीं।

---

## 🔍 इस केस-स्टडी से किसानों के लिए 3 बड़े सबक:

1. **अगेती पेड़ी का लाभ (Early Ratoon):** इस किसान के पास प्लाट 3 में **Co.S.-13235 पेड़ी (0.293 हेक्टेयर)** है। चूंकि यह स्वीकृत अगेती पेड़ी है, इसलिए अक्टूबर के अंत में मिल चालू होते ही पहले पखवाड़े में इस किसान की सबसे पहली पर्ची कटेगी।
2. **अगेती पौधा किस्म (Early Plant Co 0118):** प्लाट 4 में **Co 0118 पौधा (0.344 हेक्टेयर)** है। यह उत्तम अगेती किस्म होने के कारण किसान को पूरे ₹400 प्रति क्विंटल का उच्चतम भाव और प्राथमिकता सट्टा मिलेगा।
3. **गाटा संख्या का महत्व:** यदि किसान की खतौनी में गाटा नंबर 259, 454, 251 दर्ज हैं और सर्वे में भी यही दिख रहे हैं, तो सट्टा 100% सुरक्षित है। यदि कोई गाटा छूट गया होता, तो किसान को तत्काल फॉर्म-3 भरकर आपत्ति दर्ज करानी पड़ती।

---

## सर्वे डेटा में त्रुटि होने पर आपत्ति दर्ज कराने की अंतिम तिथि

यदि आपके सर्वे डेटा में वास्तविक खेत के मुकाबले कम रकबा दिख रहा है, तो बिल्कुल देर न करें:
* **ऑनलाइन शिकायत:** `enquiry.caneup.in` के ऊपर दिए गए **"File Complaint"** बटन पर क्लिक करके अपनी खतौनी अपलोड करें।
* **ऑफलाइन फॉर्म:** अपनी गन्ना विकास समिति में जाकर सचिव या **ज्येष्ठ गन्ना विकास निरीक्षक (SCBO)** को **प्रारूप-3 (सर्वे संशोधन प्रार्थना पत्र)** भरकर जमा करें।
* **अंतिम समय-सीमा:** सट्टा आपत्तियों के निस्तारण के उपरांत **30 सितंबर 2026** तक सभी सट्टे लॉक कर दिए जाएंगे। इसके बाद पेराई सत्र में कोई संशोधन संभव नहीं होगा।

---

## आधिकारिक हेल्पलाइन नंबर

किसी भी समस्या के समाधान हेतु गन्ना विभाग के टोल-फ्री नंबरों पर तुरंत संपर्क करें:
* **राज्य स्तरीय गन्ना किसान टोल-फ्री नंबर:** `1800-121-3203`
* **मुख्यालय लखनऊ किसान हेल्पलाइन:** `1800-180-1551`
* **आधिकारिक पोर्टल:** `https://enquiry.caneup.in/` एवं `https://caneup.xyz/`

---

## अक्सर पूछे जाने वाले सवाल (FAQs)

### 1. गन्ना सर्वे डेटा 2026-27 ऑनलाइन कैसे देखें?
उत्तर: आधिकारिक वेबसाइट `enquiry.caneup.in` या `eGanna App` पर कैप्चा दर्ज करने के बाद अपना जिला, मिल, समिति, गांव और किसान कोड चुनकर **'Survey Data'** टैब पर क्लिक करें।

### 2. परिमाप (पूर्व, पश्चिम, उत्तर, दक्षिण) का क्या मतलब होता है?
उत्तर: यह जीपीएस मीटर में आपके खेत की चारों दिशाओं की वास्तविक सीमा नाप होती है। इन चारों भुजाओं के औसत से खेत का कुल क्षेत्रफल निकाला जाता है।

### 3. क्या पेड़ी और पौधा गन्ने का अलग-अलग सट्टा बनता है?
उत्तर: हां, पेड़ी गन्ने की पर्चियां पहले पखवाड़ों (अक्टूबर-नवंबर) में आती हैं और पौधा गन्ने की पर्चियां दिसंबर-जनवरी में। इसलिए दोनों का अलग दर्ज होना आवश्यक है।

### 4. यदि सर्वे में कोई खेत छूट गया हो तो क्या करें?
उत्तर: यदि कोई खेत या गाटा संख्या छूट गई है, तो तत्काल खतौनी की प्रति और आधार कार्ड लगाकर अपनी गन्ना समिति में प्रारूप-3 जमा करें अथवा ऑनलाइन Grievance दर्ज करें।
"""

# Write to blog post file
with open(blog_file, "w", encoding="utf-8") as f:
    f.write(full_article_content)

# For news file, change the image src if needed or keep uniform
news_content = full_article_content.replace("/images/blog/ganna-survey-data-2026-27-portal-online-check.webp", "/images/news/ganna-survey-data-2026-27-portal-online-check.webp")
news_content = news_content.replace("/images/blog/ganna-survey-portal-live-screenshot-2026-27.webp", "/images/news/ganna-survey-portal-live-screenshot-2026-27.webp")

with open(news_file, "w", encoding="utf-8") as f:
    f.write(news_content)

words = full_article_content.split()
print(f"Successfully updated blog post and news file! Total words: {len(words)}")
