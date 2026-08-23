#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix frontmatter SEO across all 149 posts:
1. Add missing descriptions (3 articles)
2. Add missing keywords blocks (11 articles)
3. Fix too-long titles (trim > 65 chars, clean "जो किसानों को जरूर जाननी चाहिए" type AI filler)
4. Fix descriptions containing "complete information" (English phrase)
5. Clean "description" field emojis still remaining
6. Add author field where missing
"""
import sys, io, os, re, glob

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

BASE = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(BASE, r"content\posts")

# ---------------------------------------------------------------
# Patches for specific files
# ---------------------------------------------------------------
SPECIFIC_FIXES = {
    "05-ganne-ki-nai-kismen-2026.md": {
        "add_description": "गन्ने की नई किस्में 2026 — Co-0238, Co-0118 समेत सभी उन्नत किस्मों की तुलना। रिकवरी दर, उपज, मिट्टी और क्षेत्र के अनुसार सही किस्म चुनने की पूरी जानकारी।",
        "fix_title": "गन्ने की नई किस्में 2026 — Co-0238, Co-0118 और बेहतरीन किस्मों की तुलना",
    },
    "09-ganne-mein-keet-aur-rog-prabandhan.md": {
        "add_description": "गन्ने में कीट और रोग प्रबंधन 2026 — लाल सड़न, तना छेदक, धब्बा रोग समेत 10 आम बीमारियों की पहचान और इलाज। फसल बचाने के असरदार तरीके।",
    },
    "ganne-ki-kheti-mein-nuksan.md": {
        "add_description": "गन्ने की खेती में नुकसान से कैसे बचें 2026 — बुआई से कटाई तक 10 बड़ी गलतियां जो उपज घटाती हैं। किसान भाई इन्हें जरूर जानें।",
    },
}

# Keywords to add for the 11 missing-keywords posts
KEYWORD_FIXES = {
    "aligarh-district-sugar-mills-farmers-2026.md": [
        "अलीगढ़ शुगर मिल लिस्ट",
        "aligarh sugar mill 2026",
        "अलीगढ़ गन्ना किसान मिल",
        "anoopshahar sugar factory",
        "mazhawali venus factory",
        "neoli sugar mill",
        "rajpura sugar factory",
        "sabitgarh sugar mill",
        "satha sugar factory",
        "aligarh jila sugar mill",
    ],
    "cm-yogi-sugar-review-2026.md": [
        "सीएम योगी चीनी समीक्षा 2026",
        "CM Yogi sugar stock limit",
        "UP sugar mill payment 2026",
        "गन्ना भुगतान रिकॉर्ड 2026",
        "चीनी जमाखोरी UP",
        "UP sugarcane farmer payment",
        "yogi adityanath sugar mill action",
    ],
    "ginni-rate-trending-2026.md": [
        "चीनी के दाम 2026",
        "sugar rate today UP",
        "ginni rate today",
        "चीनी भाव ट्रेंड 2026",
        "sugar price trend India",
        "daily sugar rate UP",
        "बाजार में चीनी का भाव",
    ],
    "mazhawali-venus-sugar-factory-2026.md": [
        "मझावली वेन्नस शुगर मिल",
        "mazhawali venus factory 2026",
        "venus sugar factory aligarh",
        "मझावली गन्ना किसान",
        "mazhawali mill village list",
        "अलीगढ़ शुगर फैक्टरी",
    ],
    "neoli-sugar-factory-2026.md": [
        "नेवली शुगर मिल 2026",
        "neoli sugar factory aligarh",
        "नेवली गन्ना किसान",
        "neoli mill village list",
        "अलीगढ़ नेवली फैक्टरी",
        "neoli ganna parchi calendar",
    ],
    "pm-kisan-trending-2026.md": [
        "PM Kisan Yojana 2026",
        "pm kisan status check 2026",
        "PM किसान किस्त कब आएगी",
        "pm kisan beneficiary list",
        "PM किसान 2026 अपडेट",
        "pm kisan yojana trending",
        "किसान सम्मान निधि 2026",
    ],
    "rajpura-sugar-factory-2026.md": [
        "राजपूर शुगर मिल 2026",
        "rajpura sugar factory aligarh",
        "राजपूर गन्ना किसान",
        "rajpura mill village list",
        "अलीगढ़ राजपूर फैक्टरी",
        "rajpura ganna parchi",
    ],
    "sabitgarh-sugar-factory-2026.md": [
        "साबितगढ़ शुगर मिल 2026",
        "sabitgarh sugar factory aligarh",
        "साबितगढ़ गन्ना किसान",
        "sabitgarh mill village list",
        "अलीगढ़ साबितगढ़ फैक्टरी",
        "sabitgarh ganna parchi",
    ],
    "satha-sugar-factory-2026.md": [
        "साथा शुगर मिल 2026",
        "satha sugar factory aligarh",
        "साथा गन्ना किसान",
        "satha mill village list",
        "अलीगढ़ साथा फैक्टरी",
        "satha ganna parchi calendar",
    ],
    "sugar-mills-trending-update-2026.md": [
        "चीनी मिल्स ट्रेंडिंग 2026",
        "sugar mill update 2026",
        "UP पेराई सत्र 2026-27",
        "sugar mill list UP 2026",
        "शुगर मिल्स लेटेस्ट न्यूज़",
        "ganna crushing season start",
        "पेराई सीजन शुरू 2026",
    ],
    "ugar-mill-payment-trends-2026.md": [
        "शुगर मिल भुगतान 2026",
        "sugar mill payment status UP",
        "गन्ना भुगतान कब मिलेगा",
        "14 दिन भुगतान नियम",
        "sugar mill payment delay solution",
        "ganna bhugtan 2026",
        "भुगतान न मिले तो क्या करें",
    ],
}

# Title patterns to clean (too long / AI filler phrases)
TITLE_CLEANUPS = [
    (r' — जो किसानों को जरूर जानने चाहिए$', ''),
    (r' जो किसानों को जरूर जाननी चाहिए$', ''),
    (r' जो किसानों को जरूर जाननी चाहिए।', ''),
    (r' - complete information', ' — पूरी जानकारी'),
    (r' - Complete Information', ' — पूरी जानकारी'),
]

# Description cleanups
DESC_CLEANUPS = [
    (r'complete information।', 'पूरी जानकारी।'),
    (r'complete information\.', 'पूरी जानकारी।'),
    (r'complete information', 'पूरी जानकारी'),
]

def split_fm(content):
    if not content.startswith('---'):
        return None, content, 0
    idx = content.find('\n---', 3)
    if idx == -1:
        return None, content, 0
    return content[3:idx], content[idx+4:], idx

def clean_title(title):
    for pat, repl in TITLE_CLEANUPS:
        title = re.sub(pat, repl, title, flags=re.IGNORECASE)
    return title.strip()

def clean_description(desc):
    for pat, repl in DESC_CLEANUPS:
        desc = re.sub(pat, repl, desc, flags=re.IGNORECASE)
    return desc

def process(fp):
    fn = os.path.basename(fp)
    with open(fp, encoding='utf-8') as f:
        original = f.read()

    fm, body, fm_end_idx = split_fm(original)
    if fm is None:
        return False

    changed = False
    fm_lines = fm.split('\n')
    new_fm_lines = []

    has_description = bool(re.search(r'^description\s*:', fm, re.M))
    has_keywords = bool(re.search(r'^keywords\s*:', fm, re.M))
    has_author = bool(re.search(r'^author\s*:', fm, re.M))

    specific = SPECIFIC_FIXES.get(fn, {})
    kw_fix = KEYWORD_FIXES.get(fn)

    i = 0
    while i < len(fm_lines):
        line = fm_lines[i]

        # Fix title
        if re.match(r'^title\s*:', line):
            title_m = re.match(r'^(title\s*:\s*["\'])(.*?)(["\'])$', line)
            if title_m:
                new_title = clean_title(title_m.group(2))
                # If specific fix has a title override
                if specific.get('fix_title'):
                    new_title = specific['fix_title']
                new_line = title_m.group(1) + new_title + title_m.group(3)
                if new_line != line:
                    line = new_line
                    changed = True

        # Fix description
        if re.match(r'^description\s*:', line):
            desc_m = re.match(r'^(description\s*:\s*["\'])(.*?)(["\'])$', line)
            if desc_m:
                new_desc = clean_description(desc_m.group(2))
                new_line = desc_m.group(1) + new_desc + desc_m.group(3)
                if new_line != line:
                    line = new_line
                    changed = True

        # Insert missing description after title block (before categories)
        if not has_description and re.match(r'^categories\s*:', line) and specific.get('add_description'):
            new_fm_lines.append(f'description: "{specific["add_description"]}"')
            changed = True
            has_description = True

        # Insert keywords before or after tags
        if not has_keywords and kw_fix and re.match(r'^tags\s*:', line):
            # Add keywords right after tags block
            new_fm_lines.append(line)
            i += 1
            # Skip all tag list lines
            while i < len(fm_lines) and re.match(r'^[-\s]', fm_lines[i]):
                new_fm_lines.append(fm_lines[i])
                i += 1
            # Now add keywords block
            new_fm_lines.append('keywords:')
            for kw in kw_fix:
                new_fm_lines.append(f'- {kw}')
            changed = True
            has_keywords = True
            continue  # already advanced i

        new_fm_lines.append(line)
        i += 1

    # If description still missing and no categories marker caught it
    if not has_description and specific.get('add_description'):
        # Insert before the last empty line or at end of frontmatter
        new_fm_lines.insert(3, f'description: "{specific["add_description"]}"')
        changed = True

    # Add author if missing
    if not has_author:
        new_fm_lines.append('author: "Randhir Patil"')
        new_fm_lines.append('author_name: "Randhir Patil"')
        new_fm_lines.append('author_image: "/images/authors/randhir-patil.jpg"')
        changed = True

    if changed:
        new_fm = '\n'.join(new_fm_lines)
        new_content = '---' + new_fm + '\n---' + body
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True

    return False

def main():
    files = sorted(glob.glob(os.path.join(POSTS_DIR, '*.md')))
    changed = 0
    for fp in files:
        if process(fp):
            changed += 1
            print(f"  [UPDATED] {os.path.basename(fp)}")
        else:
            print(f"  [ok]      {os.path.basename(fp)}")
    print(f"\nDone: {changed}/{len(files)} files updated")

if __name__ == '__main__':
    main()
