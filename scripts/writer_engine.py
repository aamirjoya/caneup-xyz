# -*- coding: utf-8 -*-
import os

posts_dir = r"c:\Users\caneu\Downloads\caneup-xyz-restore\content\posts"
os.makedirs(posts_dir, exist_ok=True)

def write_article(slug, title, date, desc, cat, tags, banner, summary, tweet, sections, faqs, **kwargs):
    kw = kwargs.get("keywords", kwargs.get("kw", []))
    cat_s = "\n".join([f"- {c}" for c in cat])
    tags_s = "\n".join([f"- {t}" for t in tags])
    kw_s = "\n".join([f"- {k}" for k in kw])
    
    sections_s = "\n\n".join(sections)
    faqs_s = "\n\n".join([f"**{q}**\n> {a}" for q, a in faqs])
    
    md_content = f"""---
title: "{title}"
date: {date}
lastmod: 2026-09-05T10:00:00+05:30
description: "{desc}"
categories:
{cat_s}
tags:
{tags_s}
slug: {slug}
keywords:
{kw_s}
ShowToc: true
author: "Aamir Raza"
authors:
- "Aamir Raza"
author_name: "Aamir Raza"
author_image: "/images/authors/aamir-raza.webp"
featured_image: /images/blog/{banner}
image: /images/blog/{banner}
---

> **मुख्य बिंदु (Quick Summary):** {summary}

{tweet}

{sections_s}

---

### ❓ अक्सर पूछे जाने वाले सवाल (Top 10 FAQs)

{faqs_s}

---

### 📞 महत्वपूर्ण हेल्पलाइन और संपर्क सूत्र
- **उत्तर प्रदेश गन्ना किसान टोल-फ्री हेल्पलाइन:** 1800-121-3203
- **गन्ना आयुक्त मुख्यालय लखनऊ कंट्रोल रूम:** 0522-2236403
- **ई-गन्ना ऐप एवं सट्टा पोर्टल:** [enquiry.caneup.in](https://enquiry.caneup.in)
- **विभागीय पोर्टल:** [upcane.gov.in](https://upcane.gov.in)
"""
    fpath = os.path.join(posts_dir, f"{slug}.md")
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(md_content)
    words = len(md_content.split())
    print(f"Saved {slug}.md -> {words} words")
    return words

print("writer_engine.py updated with flexible kwargs.")
