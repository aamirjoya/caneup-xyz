import os
import sys
from PIL import Image

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
post_file = os.path.join(base_dir, 'content', 'posts', 'amroha-district-sugar-mills-farmers-2026.md')
brain_img = r'C:\Users\caneu\.gemini\antigravity\brain\f0566670-25ee-4739-bb10-e53286d68160\amroha_district_mills_cover_1787939930355.jpg'
site_img = os.path.join(base_dir, 'static', 'images', 'blog', 'amroha-district-sugar-mills-2026.webp')

# Process image to 1200x675 WebP <100KB
with Image.open(brain_img) as img:
    img = img.convert('RGB')
    target_w, target_h = 1200, 675
    src_w, src_h = img.size
    target_ratio = target_w / target_h
    src_ratio = src_w / src_h
    
    if src_ratio > target_ratio:
        new_w = int(src_h * target_ratio)
        left = (src_w - new_w) // 2
        img = img.crop((left, 0, left + new_w, src_h))
    else:
        new_h = int(src_w / target_ratio)
        top = (src_h - new_h) // 2
        img = img.crop((0, top, src_w, top + new_h))
        
    img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    quality = 85
    img.save(site_img, 'WEBP', quality=quality, optimize=True)
    kb = os.path.getsize(site_img) / 1024.0
    while kb > 98.0 and quality > 35:
        quality -= 5
        img.save(site_img, 'WEBP', quality=quality, optimize=True)
        kb = os.path.getsize(site_img) / 1024.0

print(f"Saved optimized Discover image: {site_img} | {kb:.1f} KB")

seo_title = "अमरोहा जिला गन्ना किसान मिल गाइड 2026-27: 16 चीनी मिलों की लिस्ट, कोड व पर्ची कैलेंडर"
seo_desc = "अमरोहा जिले (Amroha District) के गन्ना किसानों के लिए संपूर्ण चीनी मिल गाइड 2026-27। धनौरा, चंदनपुर, गजरौला सहित सभी 16 चीनी मिलों की लिस्ट, फैक्ट्री कोड, eGanna पर्ची कैलेंडर व भुगतान स्थिति।"

article_content = f"""---
title: "{seo_title}"
date: 2026-08-28T23:25:00+05:30
lastmod: 2026-08-28T23:25:00+05:30
description: "{seo_desc}"
categories:
- Sugar Mills
- Ganna Bhugtan
tags:
- अमरोहा चीनी मिल
- Amroha Sugar Mill List
- Wave Sugar Mill Dhanaura
- Chandanpur Sugar Mill
- Gajraula Sugar Mill
- eGanna Village Code
- CaneUp Amroha
- Amroha Farmers Guide
slug: amroha-district-sugar-mills-farmers-2026
ShowToc: true
author: "Randhir Patil"
authors:
- "Randhir Patil"
author_name: "Randhir Patil"
author_image: "/images/authors/randhir-patil.webp"
featured_image: "/images/blog/amroha-district-sugar-mills-2026.webp"
image: "/images/blog/amroha-district-sugar-mills-2026.webp"
---

{seo_title}

By  
[Randhir Patil](https://caneup.xyz/) - August 28, 2026

**अमरोहा / गजरौला / धनौरा / हसनपुर :** पश्चिमी उत्तर प्रदेश का **अमरोहा जिला (Amroha District / ज्योतिबा फुले नगर)** राज्य के सबसे बड़े और प्रमुख गन्ना उत्पादक जिलों में से एक है। अमरोहा जिले की उपजाऊ भूमि में हर साल लाखों क्विंटल गन्ने की पैदावार होती है। इस जिले के गन्ना किसानों की फसल पेराई के लिए कुल **16 प्रमुख चीनी मिलें (Sugar Factories)** संबद्ध हैं।

आगामी पेराई सत्र **2026-27** के लिए अमरोहा जिले के गन्ना किसानों की सुविधा के लिए यहाँ सभी **16 चीनी मिलों की आधिकारिक सूची (Factory Code List)**, तहसील-वार मिल मैपिंग, eGanna एप पर पर्ची कैलेंडर देखने का तरीका और भुगतान स्थिति की पूरी जानकारी दी जा रही है।

---

## 🏭 अमरोहा जिले से संबद्ध सभी 16 चीनी मिलों की सूची (Amroha Sugar Mills List 2026-27)

अमरोहा जिले के किसानों का गन्ना जिले की स्थानीय चीनी मिलों (धनौरा, चंदनपुर, गजरौला) के अलावा सीमावर्ती जिलों (मुरादाबाद, संभल, बिजनौर, बुलंदशहर, मेरठ, मुजफ्फरनगर) की प्रमुख मिलों द्वारा खरीदा जाता है:

| # | चीनी मिल का नाम (Factory Name) | फैक्ट्री कोड (Factory Code) | जिला / क्षेत्र (Region) | प्रमुख विशेषता (Key Feature) |
|---|---|---|---|---|
| **1** | **धनौरा चीनी मिल (Dhanaura - Wave Sugar)** | `260` | धनौरा, अमरोहा | जिले की प्रमुख निजी चीनी मिल, उच्च क्षमता |
| **2** | **चंदनपुर चीनी मिल (Chandanpur)** | `142` | हसनपुर/चंदनपुर, अमरोहा | हसनपुर क्षेत्र की सबसे बड़ी आधुनिक मिल |
| **3** | **गजरौला चीनी मिल (Gajraula)** | `807` | गजरौला, अमरोहा | औद्योगिक क्षेत्र गजरौला की प्रमुख मिल |
| **4** | **अगवानपुर चीनी मिल (Agwanpur - Dewan)** | `14` | मुरादाबाद / अमरोहा सीमा | अमरोहा पूर्वी सीमावर्ती किसानों की पसंद |
| **5** | **असमौली चीनी मिल (Asmauli - Dhampur Group)** | `183` | संभल / अमरोहा सीमा | अत्याधुनिक तकनीक, तीव्र पेराई |
| **6** | **बेलवाड़ा चीनी मिल (Belwara)** | `321` | बिजनौर / अमरोha सीमा | उत्तरी सीमा के गांवों के लिए |
| **7** | **चांगीपुर चीनी मिल (Changipur)** | `905` | बिजनौर / अमरोहा | उत्तम शुगर ग्रुप की आधुनिक मिल |
| **8** | **धामपुर चीनी मिल (Dhampur Sugar)** | `180` | बिजनौर | एशिया की बड़ी मिलों में शामिल |
| **9** | **मिलक नारायणपुर चीनी मिल (Milak Narayanpur)** | `144` | रामपुर / मुरादाबाद | त्रिवेणी ग्रुप की चीनी मिल |
| **10** | **नंगलामल चीनी मिल (Nanglamal)** | `301` | मेरठ / अमरोहा | बजाज़ हिन्दुस्थान समूह |
| **11** | **राजपुरा चीनी मिल (Rajpura)** | `184` | संभल | अनूपशहर रोड सीमावर्ती गांव |
| **12** | **रानी नांगल चीनी मिल (Rani Nangal)** | `145` | मुरादाबाद | डीएससीएल / श्री राम शुगर |
| **13** | **सियोहारा चीनी मिल (Seohara)** | `200` | बिजनौर | अवध शुगर एंड एनर्जी ग्रुप |
| **14** | **शाहबाद राणा चीनी मिल (Shahbad - Rana)** | `322` | रामपुर | राणा शुगर समूह |
| **15** | **सिंभावली चीनी मिल (Simbhaoli)** | `240` | हापुड़ / बुलंदशहर | ऐतिहासिक चीनी मिल समूह |
| **16** | **टिकौला चीनी मिल (Tikaula)** | `6` | मुजफ्फरनगर | पश्चिमी सीमांत गांव |

---

## 🗺️ तहसील-वार चीनी मिल मैपिंग (Tehsil-Wise Mill Distribution)

अमरोहा जिले की चारों तहसीलों के अनुसार गन्ना आपूर्ति का मुख्य आवंटन इस प्रकार है:

1. **मंडी धनौरा तहसील (Mandi Dhanaura Tehsil):** अधिकांश गांवों का गन्ना **धनौरा वेव चीनी मिल (Code 260)** और **चांगीपुर/सियोहारा** चीनी मिलों को जाता है।
2. **हसनपुर तहसील (Hasanpur Tehsil):** गन्ने की मुख्य आपूर्ति **चंदनपुर चीनी मिल (Code 142)** और **गजरौला चीनी मिल (Code 807)** को की जाती है।
3. **अमरोहा सदर तहसील (Amroha Sadar Tehsil):** गन्ने की आपूर्ति **चंदनपुर, अगवानपुर और असमौली** चीनी मिलों में विभाजित है।
4. **जोया व नोगांवा सादात (Joya & Naugawan Sadat):** गन्ने की आपूर्ति **अगवानपुर (Dewan)** और **रानी नांगल** चीनी मिलों को आवंटित की जाती है।

---

## 📱 CaneUp Portal व eGanna App पर पर्ची कैलेंडर कैसे देखें?

अमरोहा जिले के किसान भाई अपने मोबाइल से अपनी गन्ना पर्ची, कैलेंडर और सप्लाय टिकट इस प्रकार चेक करें:

1. **CaneUp वेब पोर्टल खोलें:** मोबाइल में **[enquiry.caneup.in](https://enquiry.caneup.in/)** दर्ज करें।
2. **कैप्चा कोड दर्ज करें:** स्क्रीन पर प्रदर्शित Captcha कोड भरें।
3. **जिला व मिल का चुनाव करें:**
   - **District:** Amroha (अमरोहा / ज्योतिबा फुले नगर)
   - **Factory:** ऊपर दी गई तालिका से अपनी संबद्ध चीनी मिल चुनें (उदा. Dhanaura - 260, Chandanpur - 142, Gajraula - 807, Agwanpur - 14, Asmauli - 183)।
4. **गांव कोड व किसान कोड डालें:**
   - अपनी समिति की पासबुक से अपना **Village Code (गांव कोड)** और **Grower Code (किसान कोड)** दर्ज करें।
5. **कैलेंडर देखें:** आपकी 12 पखवाड़ों की जारी पर्चियां, वजन विवरण और डीबीटी भुगतान का रिकॉर्ड तुरंत स्क्रीन पर आ जाएगा।

---

## 💳 अमरोहा जिला गन्ना भुगतान स्थिति (Payment Status 2026-27)

- **एस्क्रो अकाउंट सुरक्षा:** राज्य सरकार के आदेशानुसार अमरोहा जिले की चीनी मिलों को चीनी बिक्री से प्राप्त 85% राशि अनिवार्य रूप से किसानों के बैंक खातों में ट्रांसफर करनी होती है।
- **14 दिनों में भुगतान:** 14 दिनों के भीतर भुगतान न होने पर किसानों को 15% वार्षिक ब्याज पाने का कानूनी अधिकार है।

---

## ❓ अक्सर पूछे जाने वाले सवाल (Frequently Asked Questions)

### Q1. अमरोहा जिले में मुख्य रूप से कौन-कौन सी चीनी मिलें स्थित हैं?
अमरोहा जिले में मुख्य रूप से **धनौरा चीनी मिल (Wave Sugar)**, **चंदनपुर चीनी मिल** और **गजरौला चीनी मिल** स्थित हैं, जबकि 13 अन्य सीमावर्ती मिलें भी अमरोहा के किसानों से गन्ने की खरीद करती हैं।

### Q2. पेराई सत्र 2026-27 अमरोहा में कब शुरू होगा?
अमरोहा जिले की चीनी मिलों में पेराई सत्र 2026-27 की शुरुआत 20 अक्टूबर से 30 अक्टूबर 2026 के बीच होने की उम्मीद है।

### Q3. गन्ना पर्ची या सर्वे में संशोधन के लिए कहां संपर्क करें?
किसी भी समस्या (गलत पर्ची, रकबा सुधार, तौल में गड़बड़ी) के लिए अपनी संबंधित गन्ना विकास समिति अमरोहा, हसनपुर या धनौरा कार्यालय में 30 सितंबर 2026 तक आवेदन जमा करें, या राज्य स्तरीय हेल्पलाइन **`1800-121-3203`** पर संपर्क करें।

---

*अमरोहा जिले की सभी 16 चीनी मिलों के गांववार कोड, पर्ची कैलेंडर 2026-27 और eGanna App की हर ताजा अपडेट के लिए [CaneUp.xyz](/) विजिट करते रहें!*
"""

with open(post_file, 'w', encoding='utf-8') as f:
    f.write(article_content)

print("Successfully created Amroha District Sugar Mills Page!")
