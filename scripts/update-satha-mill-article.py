import re
import os
import sys
import shutil

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
post_file = os.path.join(base_dir, 'content', 'posts', 'satha-sugar-factory-2026.md')
brain_img = r'C:\Users\caneu\.gemini\antigravity\brain\f0566670-25ee-4739-bb10-e53286d68160\satha_mill_cover_1787926736423.jpg'
site_img = os.path.join(base_dir, 'static', 'images', 'blog', 'satha-sugar-factory-2026.jpg')

# Copy image
shutil.copy2(brain_img, site_img)
print(f"Copied {brain_img} -> {site_img}")

raw_file = os.path.join(base_dir, 'scripts', 'satha_raw.txt')
with open(raw_file, 'r', encoding='utf-8') as fp:
    raw_options = fp.read()

matches = re.findall(r'<option value="([^"]+)">([^<]+)</option>', raw_options)
villages = []
for val, text in matches:
    if val in ["-1", "999999", "512", "10778", "1171", "1091"] or "NON MEMBER" in text or "TEST" in text or "Not allowed" in text:
        continue
    m_name = re.match(r'^(.*?)\s*\((.*?)\)$', text)
    if m_name:
        name = m_name.group(1).strip()
        code = m_name.group(2).strip()
    else:
        name = text.strip()
        code = val.strip()
    villages.append((name, code))

print(f"Parsed {len(villages)} villages for Satha Sugar Mill.")

rows_html = ""
for idx, (vname, vcode) in enumerate(villages, 1):
    rows_html += f'  <tr class="vrow"><td>{idx}</td><td class="vname"><strong>{vname}</strong></td><td class="vcode"><code style="background:#dcfce7;color:#15803d;padding:2px 8px;border-radius:4px;font-weight:700;">{vcode}</code></td><td>साथा चीनी मिल समिति (अलीगढ़)</td></tr>\n'

seo_title = f"साथा शुगर मिल 2026-27: {len(villages)} गांवों की लिस्ट, कोड व पर्ची कैलेंडर | Satha Sugar Mill Aligarh"
seo_desc = f"साथा शुगर मिल (Satha Sahkari Sugar Mill Aligarh Mathura Hathras) 2026-27 के सभी {len(villages)} गांवों की आधिकारिक सूची व Village Code। 1 सेकंड में गांव खोजें, पर्ची कैलेंडर, eGanna App डाउनलोड व भुगतान स्थिति।"

article_content = f"""---
title: "{seo_title}"
date: 2026-08-28T19:48:00+05:30
lastmod: 2026-08-28T19:48:00+05:30
description: "{seo_desc}"
categories:
- Sugar Mills
tags:
- Satha Sugar Mill
- साथा शुगर मिल 2026
- अलीगढ़ गन्ना पर्ची
- eGanna Village List
- CaneUp Village Code
- अलीगढ़ सहकारी चीनी मिल
- Satha Mill Village List
slug: satha-sugar-factory-2026
ShowToc: true
author: "Randhir Patil"
authors:
- "Randhir Patil"
author_name: "Randhir Patil"
author_image: "/images/authors/randhir-patil.webp"
featured_image: "/images/blog/satha-sugar-factory-2026.jpg"
image: "/images/blog/satha-sugar-factory-2026.jpg"
---

{seo_title}

By  
[Randhir Patil](https://caneup.xyz/) - August 28, 2026

**अलीगढ़ / साथा / इगलास / अतरौली / हाथरस :** किसान सहकारी चीनी मिल लिमिटेड, साथा (Kisan Sahkari Chini Mills Ltd, Satha, Aligarh) उत्तर प्रदेश के अलीगढ़ जिले की एक प्रमुख सहकारी चीनी मिल है। आगामी पेराई सत्र 2026-27 के लिए यह चीनी मिल अलीगढ़, हाथरस, मथुरा और बुलंदशहर क्षेत्र के लगभग **{len(villages)} से अधिक गांवों** के पंजीकृत गन्ना किसानों से गन्ने की सीधी खरीद करेगी।

यदि आप साथा शुगर मिल से जुड़े गन्ना किसान हैं और अपने गांव का आधिकारिक **Village Code (गांव कोड)** खोज रहे हैं, तो नीचे दी गई लाइव सर्च टेबल से अपना गांव और कोड 1 सेकंड में खोज सकते हैं।

---

## 🔍 साथा शुगर मिल — सभी {len(villages)} गांव व कोड लाइव खोजें (Live Search Tool)

नीचे दिए गए सर्च बॉक्स में अपने **गांव का नाम (उदा. SATHA, IGLAS, ATRAULI, GABHANA, ALIGARH, CHHATARI, KHURJA)** या **गांव कोड (उदा. 1, 491, 181, 733, 5028, 5133)** दर्ज करें:

<div style="margin:20px 0;background:#f0fdf4;border:2px solid #bbf7d0;border-radius:12px;padding:16px;">
  <label for="vsearch" style="font-weight:700;color:#15803d;display:block;margin-bottom:8px;font-size:16px;">🔎 अपने गांव का नाम या गांव कोड टाइप करें:</label>
  <input type="text" id="vsearch" placeholder="उदा. SATHA, IGLAS, ATRAULI, 1, 491, 5028..." onkeyup="filterVillages()" style="width:100%;padding:12px 16px;border:2px solid #15803d;border-radius:8px;font-size:16px;outline:none;">
  <small style="color:#6b7280;display:block;margin-top:6px;">कुल {len(villages)} गांव सूचीबद्ध हैं। टाइप करते ही परिणाम नीचे ऑटोमेटिक दिखेंगे।</small>
</div>

<div class="tbl-wrap">
<table id="vtable">
<thead>
  <tr>
    <th>#</th>
    <th>गांव का नाम (Village Name)</th>
    <th>गांव कोड (Village Code)</th>
    <th>गन्ना समिति / मिल</th>
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

## 🏭 Satha Sugar Mill Overview & Key Details

| विवरण (Parameter) | आधिकारिक जानकारी (Official Details) |
|---|---|
| **मिल का नाम** | किसान सहकारी चीनी मिल लिमिटेड, साथा |
| **स्थान व जिला** | साथा, अनूपशहर रोड, जिला अलीगढ़, उत्तर प्रदेश |
| **प्रबंधन** | यूपी सहकारी चीनी मिल संघ (UP Sugar Federation) |
| **प्रतिदिन पेराई क्षमता (Crushing Capacity)** | 3,000 TCD (टन प्रति दिन) |
| **संबद्ध कुल गांव (Total Villages)** | **{len(villages)} गांव** |
| **पेराई सत्र 2026-27 प्रारंभ तिथि** | **20 अक्टूबर से 25 अक्टूबर 2026** |
| **गन्ना भुगतान** | सीधे बैंक खाते में (Cooperative DBT Credit) |
| **आधिकारिक पोर्टल** | [enquiry.caneup.in](https://enquiry.caneup.in/) |

---

## 📲 CaneUp व eGanna App पर साथा मिल की पर्ची कैलेंडर कैसे देखें?

साथा चीनी मिल के किसान भाई अपने मोबाइल पर सप्लाय पर्ची और कैलेंडर इस प्रकार देख सकते हैं:

1. **CaneUp पोर्टल खोलें:** मोबाइल ब्राउज़र में **[enquiry.caneup.in](https://enquiry.caneup.in/)** पर जाएं।
2. **कैप्चा दर्ज करें:** Captcha कोड दर्ज करके 'Submit' पर क्लिक करें।
3. **जिला व मिल का चयन करें:**
   - **District:** Aligarh (अलीगढ़)
   - **Factory:** Satha (साथा - सहकारी चीनी मिल)
4. **गांव व किसान कोड डालें:**
   - ऊपर दी गई तालिका से अपने गांव का **Village Code** दर्ज करें (उदा. साथा का कोड `1`, इगलास का कोड `491`, अतरौली का कोड `181`, गभाना का कोड `733`)।
   - अपना **Grower Code (किसान कोड)** दर्ज करें।
5. **कैलेंडर व भुगतान देखें:** आपकी पर्चियों का पखवाड़ावार कैलेंडर, कुल जारी पर्चियां और भुगतान स्थिति स्क्रीन पर दिख जाएगी।

---

## 💳 साथा सहकारी चीनी मिल गन्ना भुगतान स्थिति (Payment Status 2026)

- **डीबीटी द्वारा सीधे खाते में:** शासन के निर्देशानुसार साथा चीनी मिल का गन्ना भुगतान सीधे किसानों के आधार-लिंक्ड बैंक खातों में ट्रांसफर किया जाता है।
- **गन्ना विकास समिति सुविधा:** पर्ची या बॉन्डिंग से संबंधित किसी भी समस्या के समाधान के लिए साथा गन्ना विकास समिति कार्यालय में संपर्क कर सकते हैं।

---

## ❓ अक्सर पूछे जाने वाले सवाल (Frequently Asked Questions)

### Q1. साथा चीनी मिल का पेराई सत्र 2026-27 कब शुरू होगा?
साथा सहकारी चीनी मिल में पेराई सत्र 2026-27 की शुरुआत 20 अक्टूबर से 25 अक्टूबर 2026 के मध्य प्रस्तावित है।

### Q2. क्या साथा चीनी मिल में ऑनलाइन पर्ची कैलेंडर देखा जा सकता है?
जी हां, CaneUp Portal ([enquiry.caneup.in](https://enquiry.caneup.in/)) और Android पर **eGanna App** के जरिए किसान भाई 24 घंटे अपनी पर्चियां देख सकते हैं।

### Q3. यदि पर्ची कैलेंडर में रकबा या पर्ची कम दिखे तो क्या करें?
यदि बॉन्डिंग या पर्चियों की संख्या कम है, तो अपनी संबंधित गन्ना विकास समिति (साथा/अलीगढ़) में जाकर 30 सितंबर 2026 तक संशोधन आवेदन जमा करें।

### Q4. गन्ना विभाग का टोल-फ्री हेल्पलाइन नंबर क्या है?
गन्ना भुगतान या पर्ची से जुड़ी शिकायत दर्ज कराने के लिए उत्तर प्रदेश सरकार का टोल-फ्री नंबर **`1800-121-3203`** जारी किया गया है।

---

*साथा चीनी मिल गन्ना पर्ची कैलेंडर 2026-27 और eGanna App की हर ताजा अपडेट के लिए [CaneUp.xyz](/) विजिट करते रहें!*
"""

with open(post_file, 'w', encoding='utf-8') as f:
    f.write(article_content)

print(f"Successfully generated SEO-optimized Satha Mill Article with all {len(villages)} villages!")
