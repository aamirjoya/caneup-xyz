# -*- coding: utf-8 -*-
import os
import sys

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
posts_dir = os.path.join(base_dir, 'content', 'posts')
os.makedirs(posts_dir, exist_ok=True)

def write_article(slug, title, date, desc, cat, tags, keywords, banner, summary, tweet, sections, faqs):
    cat_str = '\n'.join([f'- {c}' for c in cat])
    tags_str = '\n'.join([f'- {t}' for t in tags])
    kw_str = '\n'.join([f'- {k}' for k in keywords])
    
    sections_text = '\n\n'.join(sections)
    faqs_text = '\n\n'.join([f'**{q}**\n> {a}' for q, a in faqs])
    
    content = f'''---
title: "{title}"
date: {date}
lastmod: 2026-09-05T10:00:00+05:30
description: "{desc}"
categories:
{cat_str}
tags:
{tags_str}
slug: {slug}
keywords:
{kw_str}
ShowToc: true
author: "Randhir Patil"
authors:
- "Randhir Patil"
author_name: "Randhir Patil"
author_image: "/images/authors/randhir-patil.webp"
featured_image: /images/blog/{banner}
image: /images/blog/{banner}
---

> **मुख्य बिंदु (Quick Summary):** {summary}

{tweet}

{sections_text}

---

### ❓ अक्सर पूछे जाने वाले सवाल (Top 10 FAQs)

{faqs_text}

---

### 📞 महत्वपूर्ण हेल्पलाइन और संपर्क सूत्र
- **उत्तर प्रदेश गन्ना किसान टोल-फ्री हेल्पलाइन:** 1800-121-3203
- **गन्ना आयुक्त मुख्यालय लखनऊ कंट्रोल रूम:** 0522-2236403
- **ई-गन्ना ऐप एवं सट्टा पोर्टल:** [enquiry.caneup.in](https://enquiry.caneup.in)
- **विभागीय पोर्टल:** [upcane.gov.in](https://upcane.gov.in)
'''
    fpath = os.path.join(posts_dir, f'{slug}.md')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    words = len(content.split())
    print(f'Saved {slug}.md: {words} words')
    return words

print("Base builder module loaded successfully.")
