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
post_file = os.path.join(base_dir, 'content', 'posts', 'balrampur-chini-akbarpur.md')
post_file_alt = os.path.join(base_dir, 'content', 'posts', 'akbarpur-sugar-factory-2026.md')
brain_img = r'C:\Users\caneu\.gemini\antigravity\brain\f0566670-25ee-4739-bb10-e53286d68160\akbarpur_mill_cover_1787938080798.jpg'
site_img = os.path.join(base_dir, 'static', 'images', 'blog', 'akbarpur-sugar-factory-2026.jpg')

# Copy image
shutil.copy2(brain_img, site_img)
print(f"Copied {brain_img} -> {site_img}")

raw_file = os.path.join(base_dir, 'scripts', 'akbarpur_raw.txt')
with open(raw_file, 'r', encoding='utf-8') as fp:
    raw_options = fp.read()

matches = re.findall(r'<option value="([^"]+)">([^<]+)</option>', raw_options)
villages = []
for val, text in matches:
    if val in ["-1", "999999", "512", "10778"] or "NON MEMBER" in text or "TEST" in text or "Not allowed" in text:
        continue
    m_name = re.match(r'^(.*?)\s*\((.*?)\)$', text)
    if m_name:
        name = m_name.group(1).strip()
        code = m_name.group(2).strip()
    else:
        name = text.strip()
        code = val.strip()
    villages.append((name, code))

print(f"Parsed {len(villages)} villages for Akbarpur Sugar Mill.")

rows_html = ""
for idx, (vname, vcode) in enumerate(villages, 1):
    rows_html += f'  <tr class="vrow"><td>{idx}</td><td class="vname"><strong>{vname}</strong></td><td class="vcode"><code style="background:#dcfce7;color:#15803d;padding:2px 8px;border-radius:4px;font-weight:700;">{vcode}</code></td><td>अकबरपुर गन्ना समिति (अम्बेडकर नगर)</td></tr>\n'

seo_title = f"अकबरपुर चीनी मिल 2026-27: {len(villages)} गांवों की लिस्ट, कोड व पर्ची कैलेंडर | Akbarpur Sugar Mill Ambedkar Nagar"
seo_desc = f"अकबरपुर चीनी मिल (Balrampur Chini Mills Akbarpur Ambedkar Nagar) 2026-27 के सभी {len(villages)} गांवों की आधिकारिक सूची व Village Code। 1 सेकंड में गांव खोजें, पर्ची कैलेंडर, eGanna App डाउनलोड व भुगतान स्थिति।"

article_content = f"""---
title: "{seo_title}"
date: 2026-08-28T22:55:00+05:30
lastmod: 2026-08-28T22:55:00+05:30
description: "{seo_desc}"
categories:
- Sugar Mills
tags:
- Akbarpur Sugar Mill
- बलरामपुर चिनी मिल्स अकबरपुर
- अकबरपुर चीनी मिल 2026
- अम्बेडकर नगर गन्ना पर्ची
- eGanna Village List
- CaneUp Village Code
- Akbarpur Mill Village List
slug: akbarpur-sugar-factory-2026
aliases:
- /posts/balrampur-chini-akbarpur/
ShowToc: true
author: "Randhir Patil"
authors:
- "Randhir Patil"
author_name: "Randhir Patil"
author_image: "/images/authors/randhir-patil.webp"
featured_image: "/images/blog/akbarpur-sugar-factory-2026.jpg"
image: "/images/blog/akbarpur-sugar-factory-2026.jpg"
---

{seo_title}

By  
[Randhir Patil](https://caneup.xyz/) - August 28, 2026

**अम्बेडकर नगर / अकबरपुर / जलालपुर / टांडा / कटेहरी / भीटी :** बलरामपुर चिनी मिल्स समूह की प्रमुख इकाई **अकबरपुर चीनी मिल (Akbarpur Sugar Mill, Ambedkar Nagar)** उत्तर प्रदेश के अयोध्या मंडल के अम्बेडकर नगर जिले की सबसे बड़ी निजी चीनी मिल है। आगामी पेराई सत्र 2026-27 के लिए यह चीनी मिल अम्बेडकर नगर, अयोध्या, सुल्तानपुर और आसपास के **{len(villages)} से अधिक पंजीकृत गांवों** से गन्ने की सीधी खरीद करेगी।

यदि आप अकबरपुर चीनी मिल से जुड़े गन्ना किसान हैं और अपने गांव का आधिकारिक **Village Code (गांव कोड)** खोज रहे हैं, तो नीचे दी गई लाइव सर्च टेबल से अपना गांव और कोड 1 सेकंड में खोज सकते हैं।

---

## 🔍 अकबरपुर चीनी मिल — सभी {len(villages)} गांव व कोड लाइव खोजें (Live Search Tool)

नीचे दिए गए सर्च बॉक्स में अपने **गांव का नाम (उदा. AAGAPUR, AKBARPUR, JALALPUR, TANDA, AAMADARVESHPUR, ABBO PUR)** या **गांव कोड (उदा. 81221, 90215, 73603, 12408, 63001)** दर्ज करें:

<div style="margin:20px 0;background:#f0fdf4;border:2px solid #bbf7d0;border-radius:12px;padding:16px;">
  <label for="vsearch" style="font-weight:700;color:#15803d;display:block;margin-bottom:8px;font-size:16px;">🔎 अपने गांव का नाम या गांव कोड टाइप करें:</label>
  <input type="text" id="vsearch" placeholder="उदा. AKBARPUR, JALALPUR, TANDA, 81221, 90215, 73603..." onkeyup="filterVillages()" style="width:100%;padding:12px 16px;border:2px solid #15803d;border-radius:8px;font-size:16px;outline:none;">
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

## 🏭 Akbarpur Sugar Mill Overview & Technical Specifications

| विवरण (Parameter) | आधिकारिक जानकारी (Official Details) |
|---|---|
| **मिल का नाम** | बलरामपुर चिनी मिल्स लिमिटेड (अकबरपुर इकाई) |
| **स्थान व जिला** | मिज़वां/अकबरपुर, जिला अम्बेडकर नगर, उत्तर प्रदेश |
| **समूह (Parent Group)** | बलरामपुर चिनी मिल्स लिमिटेड (BCML) |
| **प्रतिदिन पेराई क्षमता (Crushing Capacity)** | 7,500 TCD (टन प्रति दिन) |
| **संबद्ध कुल गांव (Total Villages)** | **{len(villages)} गांव** |
| **पेराई सत्र 2026-27 प्रारंभ तिथि** | **20 अक्टूबर से 25 अक्टूबर 2026** |
| **गन्ना भुगतान सुविधा** | 14 दिनों में सीधे बैंक खाते में (Escrow Bank Credit) |
| **आधिकारिक पोर्टल** | [enquiry.caneup.in](https://enquiry.caneup.in/) |

---

## 📲 CaneUp व eGanna App पर अकबरपुर मिल का पर्ची कैलेंडर कैसे देखें?

अकबरपुर चीनी मिल से जुड़े किसान भाई अपने मोबाइल पर पर्ची कैलेंडर देखने के लिए इन आसान चरणों का पालन करें:

1. **CaneUp पोर्टल पर जाएं:** अपने मोबाइल ब्राउज़र में **[enquiry.caneup.in](https://enquiry.caneup.in/)** खोलें।
2. **कैप्चा कोड भरें:** स्क्रीन पर दिख रहे Captcha कोड को दर्ज करें।
3. **जिला व मिल चुनें:**
   - **District:** Ambedkar Nagar (अम्बेडकर नगर)
   - **Factory:** Akbarpur (अकबरपुर - बलरामपुर चिनी)
4. **गांव व किसान कोड दर्ज करें:**
   - ऊपर तालिका में दिए गए अपने **Village Code (गांव कोड)** दर्ज करें (उदा. अकबरपुर का कोड `90215`, आलापुर का कोड `73603`, आगापुर का कोड `81221`)।
   - अपना **Grower Code (किसान कोड)** दर्ज करें।
5. **पर्ची व भुगतान स्थिति देखें:** आपकी सभी जारी पर्चियां, वजन विवरण और डीबीटी भुगतान का रिकॉर्ड स्क्रीन पर आ जाएगा।

---

## 💳 अकबरपुर चीनी मिल गन्ना भुगतान स्थिति (Payment Status 2026-27)

- **14 दिनों का नियम:** राज्य सरकार और गन्ना आयुक्त के दिशा-निर्देशों के तहत चीनी बिक्री से प्राप्त 85% राशि एस्क्रो अकाउंट (Escrow Account) के माध्यम से किसानों के बैंक खातों में डीबीटी (DBT) द्वारा ट्रांसफर की जाती है।
- **ब्याज का अधिकार:** यदि चीनी मिल 14 दिनों के भीतर भुगतान में देरी करती है, तो नियमानुसार 15% वार्षिक ब्याज का प्रावधान है।

---

## ❓ अक्सर पूछे जाने वाले सवाल (Frequently Asked Questions)

### Q1. अकबरपुर चीनी मिल का पेराई सत्र 2026-27 कब शुरू होगा?
अकबरपुर चीनी मिल में पेराई सत्र 2026-27 की शुरुआत 20 अक्टूबर से 25 अक्टूबर 2026 के बीच प्रस्तावित है।

### Q2. अकबरपुर चीनी मिल किस ग्रुप की इकाई है?
यह देश के सबसे बड़े चीनी उत्पादक समूहों में से एक **बलरामपुर चिनी मिल्स लिमिटेड (Balrampur Chini Mills Ltd)** की एक प्रमुख अत्याधुनिक इकाई है।

### Q3. यदि पर्ची कैलेंडर में बॉन्डिंग या रकबा गलत हो तो कहां शिकायत करें?
किसान भाई अकबरपुर गन्ना विकास समिति कार्यालय या राज्य सरकार के टोल-फ्री हेल्पलाइन नंबर **`1800-121-3203`** पर संपर्क कर सकते हैं।

---

*अकबरपुर चीनी मिल पर्ची कैलेंडर 2026-27, गांववार कोड और eGanna App की हर अपडेट के लिए [CaneUp.xyz](/) विजिट करते रहें!*
"""

# Write to both paths to ensure zero broken links
with open(post_file, 'w', encoding='utf-8') as f:
    f.write(article_content)

with open(post_file_alt, 'w', encoding='utf-8') as f:
    f.write(article_content)

print(f"Successfully generated SEO-optimized Akbarpur Mill Article with all {len(villages)} villages!")
