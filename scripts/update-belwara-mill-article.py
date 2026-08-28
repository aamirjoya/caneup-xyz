import re
import os
import sys
from PIL import Image

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
post_file = os.path.join(base_dir, 'content', 'posts', 'belwara-sugar-factory-2026.md')
brain_img = r'C:\Users\caneu\.gemini\antigravity\brain\f0566670-25ee-4739-bb10-e53286d68160\belwara_mill_cover_1787945361500.jpg'
site_img = os.path.join(base_dir, 'static', 'images', 'blog', 'belwara-sugar-factory-2026.webp')

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

# Parse raw villages
raw_file = os.path.join(base_dir, 'scripts', 'belwara_raw.txt')
with open(raw_file, 'r', encoding='utf-8') as fp:
    raw_options = fp.read()

matches = re.findall(r'<option value="([^"]+)">([^<]+)</option>', raw_options)
villages = []
for val, text in matches:
    if val in ["-1", "999999", "36", "6327", "6328", "6326"] or "DUMMY" in text or "NONMEMBER" in text or "TEST" in text:
        continue
    m_name = re.match(r'^(.*?)\s*\((.*?)\)$', text)
    if m_name:
        name = m_name.group(1).strip()
        code = m_name.group(2).strip()
    else:
        name = text.strip()
        code = val.strip()
    villages.append((name, code))

print(f"Parsed {len(villages)} villages for Belwara Sugar Mill.")

rows_html = ""
for idx, (vname, vcode) in enumerate(villages, 1):
    rows_html += f'  <tr class="vrow"><td>{idx}</td><td class="vname"><strong>{vname}</strong></td><td class="vcode"><code style="background:#dcfce7;color:#15803d;padding:2px 8px;border-radius:4px;font-weight:700;">{vcode}</code></td><td>बेलवाड़ा चीनी मिल (Wave Sugar - Code 321)</td></tr>\n'

seo_title = f"बेलवाड़ा चीनी मिल 2026-27: {len(villages)} गांवों की लिस्ट, कोड व CaneUp पर्ची कैलेंडर | Belwara Sugar Mill Amroha Bijnor"
seo_desc = f"बेलवाड़ा चीनी मिल (Belwara Sugar Mill Code 321 Amroha Bijnor) 2026-27 के सभी {len(villages)} गांवों की आधिकारिक सूची व Village Code। 1 सेकंड में गांव खोजें, eGanna पर्ची कैलेंडर व डीबीटी भुगतान स्थिति।"

article_content = f"""---
title: "{seo_title}"
date: 2026-08-29T01:00:00+05:30
lastmod: 2026-08-29T01:00:00+05:30
description: "{seo_desc}"
categories:
- Sugar Mills
- Ganna Bhugtan
tags:
- Belwara Sugar Mill
- बेलवाड़ा चीनी मिल 2026
- Amroha Sugar Mill List
- Wave Sugar Belwara
- CaneUp Village Code
- eGanna Parchi Calendar
- CaneUp Amroha
- Belwara Mill Village List
slug: belwara-sugar-factory-2026
ShowToc: true
author: "Randhir Patil"
authors:
- "Randhir Patil"
author_name: "Randhir Patil"
author_image: "/images/authors/randhir-patil.webp"
featured_image: "/images/blog/belwara-sugar-factory-2026.webp"
image: "/images/blog/belwara-sugar-factory-2026.webp"
---

# {seo_title}

By  
[Randhir Patil](https://caneup.xyz/) - August 29, 2026

**अमरोहा / धनौरा / बिजनौर / चांदपुर / गजरौला :** वेव ग्रुप द्वारा संचालित **बेलवाड़ा चीनी मिल (Belwara Sugar Mill - CaneUp Mill Code 321)** पश्चिमी उत्तर प्रदेश के **[अमरोहा जिले (Amroha District)](/posts/amroha-district-sugar-mills-farmers-2026/)** और बिजनौर जिले की सीमा पर स्थित एक प्रमुख और आधुनिक निजी चीनी मिल है। पेराई सत्र **2026-27** के लिए उत्तर प्रदेश सरकार के गन्ना विकास एवं चीनी उद्योग विभाग (Cane Development Department UP) ने अमरोहा (मंडी धनौरा, गजरौला, अमरोहा सदर) तथा बिजनौर (चांदपुर, नूरपुर) क्षेत्र के **{len(villages)} से अधिक पंजीकृत गांवों** का गन्ना आवंटन बेलवाड़ा चीनी मिल को किया है।

यदि आप बेलवाड़ा चीनी मिल से जुड़े गन्ना किसान हैं और **[enquiry.caneup.in](https://enquiry.caneup.in/)** अथवा **[eGanna App 2026](/posts/eganna-app-download-2026/)** के माध्यम से अपने गांव का **CaneUp Village Code (गांव कोड)**, सप्लाय पर्ची कैलेंडर और **[गन्ना भुगतान स्टेटस](/posts/ganna-bhugtan-status-kaise-check-kare-2026/)** देखना चाहते हैं, तो नीचे दी गई लाइव सर्च टेबल से अपना गांव 1 सेकंड में खोज सकते हैं।

---

## 🔍 बेलवाड़ा चीनी मिल — सभी {len(villages)} गांव व कोड लाइव खोजें (Live Search Tool)

नीचे दिए गए सर्च बॉक्स में अपने **गांव का नाम (उदा. ABBASPUR, AHMADNAGAR, BELWARA, CHANDANPUR, DHANAURA, JOYA, NAJARPUR)** या **गांव कोड (उदा. 25181, 2815, 2028, 2469, 2755, 2787, 2789)** दर्ज करें:

<div style="margin:20px 0;background:#f0fdf4;border:2px solid #bbf7d0;border-radius:12px;padding:16px;">
  <label for="vsearch" style="font-weight:700;color:#15803d;display:block;margin-bottom:8px;font-size:16px;">🔎 अपने गांव का नाम या गांव कोड टाइप करें:</label>
  <input type="text" id="vsearch" placeholder="उदा. BELWARA, CHANDANPUR, DHANAURA, 2028, 2469, 2755..." onkeyup="filterVillages()" style="width:100%;padding:12px 16px;border:2px solid #15803d;border-radius:8px;font-size:16px;outline:none;">
  <small style="color:#6b7280;display:block;margin-top:6px;">कुल {len(villages)} गांव सूचीबद्ध हैं। टाइप करते ही परिणाम नीचे ऑटोमेटिक दिखेंगे।</small>
</div>

<div class="tbl-wrap">
<table id="vtable">
<thead>
  <tr>
    <th>#</th>
    <th>गांव का नाम (Village Name)</th>
    <th>CaneUp गांव कोड (Village Code)</th>
    <th>संबद्ध चीनी मिल व कोड</th>
  </tr>
</thead>
<tbody>
{rows_html}
</tbody>
</table>
</div>

<script>
function filterVillages() {{
  var input = document.getElementById("vsearch");
  var filter = input.value.toUpperCase();
  var table = document.getElementById("vtable");
  var tr = table.getElementsByTagName("tr");
  for (var i = 1; i < tr.length; i++) {{
    var tdName = tr[i].getElementsByClassName("vname")[0];
    var tdCode = tr[i].getElementsByClassName("vcode")[0];
    if (tdName || tdCode) {{
      var txtName = tdName.textContent || tdName.innerText;
      var txtCode = tdCode.textContent || tdCode.innerText;
      if (txtName.toUpperCase().indexOf(filter) > -1 || txtCode.toUpperCase().indexOf(filter) > -1) {{
        tr[i].style.display = "";
      }} else {{
        tr[i].style.display = "none";
      }}
    }}
  }}
}}
</script>

---

## 🏭 Belwara Sugar Mill Overview & Key Details (CaneUp Code 321)

| विवरण (Parameter) | आधिकारिक जानकारी (Official Details) |
|---|---|
| **चीनी मिल का पूरा नाम** | वेव चीनी मिल लिमिटेड, बेलवाड़ा (Wave Sugar Mill Belwara) |
| **CaneUp फैक्ट्री कोड** | **`321`** |
| **मुख्य स्थान व जिला** | बेलवाड़ा, जिला अमरोहा / बिजनौर सीमा, उत्तर प्रदेश |
| **संबद्ध जिले** | **[अमरोहा (J.P. Nagar)](/posts/amroha-district-sugar-mills-farmers-2026/)** एवं बिजनौर |
| **प्रतिदिन पेराई क्षमता (Crushing Capacity)** | 6,500 TCD (टन प्रति दिन) |
| **संबद्ध कुल गांव (Total Villages)** | **{len(villages)} पंजीकृत गांव** |
| **पेराई सत्र 2026-27 प्रारंभ तिथि** | **22 अक्टूबर से 30 अक्टूबर 2026** |
| **गन्ना भुगतान ट्रांसफर** | सीधे किसान के आधार-लिंक्ड बैंक खाते में (Escrow DBT) |
| **आधिकारिक CaneUp पोर्टल** | [enquiry.caneup.in](https://enquiry.caneup.in/) |

---

## 📱 CaneUp Portal (enquiry.caneup.in) व eGanna App पर पर्ची कैलेंडर कैसे देखें?

बेलवाड़ा चीनी मिल से जुड़े किसान भाई अपने स्मार्टफोन पर सप्लाय पर्ची कैलेंडर देखने के लिए इन आसान चरणों का पालन करें (विस्तृत जानकारी के लिए **[गन्ना पर्ची कैलेंडर 2026-27 कैसे देखें](/posts/ganna-parchi-calendar-2026-27-kaise-dekhe/)** पढ़ें):

1. **पोर्टल खोलें:** अपने मोबाइल ब्राउज़र में **[enquiry.caneup.in](https://enquiry.caneup.in/)** दर्ज करें।
2. **Captcha सुरक्षा कोड भरें:** स्क्रीन पर प्रदर्शित सिक्योरिटी कैप्चा कोड दर्ज करें।
3. **जिला व चीनी मिल का चुनाव करें:**
   - **District:** Amroha (अमरोहा) या Bijnor (बिजनौर)
   - **Factory:** Belwara - **`Code 321`**
4. **गांव व किसान कोड डालें:**
   - ऊपर तालिका में दिए गए अपने **CaneUp Village Code** भरें (उदा. बेलवाड़ा कोड `2028`, अहमदपुर कोड `2317`, अतरिया कोड `2439`)।
   - अपनी समिति पासबुक से अपना **Grower Code (किसान कोड)** दर्ज करें।
5. **सप्लाय पर्ची व भुगतान स्थिति देखें:** आपके सामने 12 पखवाड़ों की जारी पर्चियां, वजन ब्योरा और बैंक भुगतान रिकॉर्ड खुल जाएगा। एंड्रॉइड यूजर **[eGanna App Download](/posts/eganna-app-download-2026/)** करके भी यह ब्योरा प्राप्त कर सकते हैं।

---

## 💳 बेलवाड़ा चीनी मिल गन्ना भुगतान नियम व एस्क्रो अकाउंट सुरक्षा (Payment Status 2026-27)

- **डीबीटी एस्क्रो बैंक ट्रांसफर:** यूपी सरकार के आदेशानुसार बेलवाड़ा चीनी मिल द्वारा चीनी बिक्री की 85% राशि सीधे विशेष एस्क्रो खाते से किसानों के आधार-लिंक्ड बैंक खाते में भेजी जाती है।
- **14 दिनों में भुगतान का नियम:** 14 दिनों के भीतर भुगतान न होने पर किसानों को 15% वार्षिक ब्याज पाने का कानूनी अधिकार है। अधिक जानकारी के लिए **[गन्ना भुगतान नियम व स्टेटस](/posts/ganna-bhugtan-status-kaise-check-kare-2026/)** पढ़ें।
- **हेल्पलाइन सहायता:** किसी भी समस्या के लिए हमारे **[गन्ना विभाग हेल्पलाइन डायरेक्टरी](/posts/ganna-vibhag-helpline-number-jilewar/)** के माध्यम से टोल-फ्री नंबर **`1800-121-3203`** पर संपर्क करें।

---

## ❓ अक्सर पूछे जाने वाले सवाल (Frequently Asked Questions)

### Q1. बेलवाड़ा चीनी मिल का CaneUp फैक्ट्री कोड क्या है?
बेलवाड़ा (वेव ग्रुप) चीनी मिल का आधिकारिक CaneUp फैक्ट्री कोड **`321`** है।

### Q2. बेलवाड़ा चीनी मिल का पेराई सत्र 2026-27 कब शुरू होगा?
बेलवाड़ा चीनी मिल का पेराई सत्र 2026-27 दिनांक 22 अक्टूबर से 30 अक्टूबर 2026 के मध्य शुरू होना प्रस्तावित है।

### Q3. यदि पर्ची कैलेंडर या सर्वे में त्रुटि हो तो कहां शिकायत करें?
किसान भाई अपनी संबंधित गन्ना विकास समिति (धनौरा / अमरोहा) कार्यालय में 30 सितंबर 2026 तक संशोधन आवेदन जमा कर सकते हैं।

---

*बेलवाड़ा चीनी मिल पर्ची कैलेंडर 2026-27, गांववार कोड और eGanna App की हर अपडेट के लिए [CaneUp.xyz](/) विजिट करते रहें!*
"""

with open(post_file, 'w', encoding='utf-8') as f:
    f.write(article_content)

print(f"Successfully generated SEO-optimized Belwara Mill Article with all {len(villages)} villages!")
