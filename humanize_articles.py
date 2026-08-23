#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Humanize articles - remove AI/robotic phrases, clean up intros,
fix generic conclusions across all 10 numbered articles.
"""
import sys, io, os, re, glob

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

POSTS_DIR = r"content\posts"

# ---------------------------------------------------------------
# Phrase replacements - AI/robotic → human/natural Hindi
# ---------------------------------------------------------------
PHRASE_SUBS = [
    # AI-style "complete guide" phrases
    (r'इस Complete Guide में हम[^।]*।', ''),
    (r'Complete Guide में हम[^।]*।', ''),
    (r'इस लेख में हम आपको[^।]*।\s*', ''),
    (r'इस लेख में हम[^।]*जानकारी देंगे[^।]*।\s*', ''),
    (r'यह Complete Guide [^\n]*\n', ''),
    (r'Complete Guide', 'गाइड'),

    # Robotic transitions
    (r'\n> \*\*लेखक का नोट:\*\*[^\n]*\n', '\n'),
    (r'\n> \*\*आमिर जोया[^\n]*\n', '\n'),

    # AI-style "टिप्पणी" column header in tables → just remove
    # (tables are fine as-is, keep them)

    # Robotic "मुख्य सुझाव:" checklist at end
    (r'\*\*मुख्य सुझाव:\*\*\n((?:- [^\n]+\n)+)', lambda m: ''),

    # Fix "बहुत गंभीर" as severity label in tables
    (r'  बहुत गंभीर', 'बहुत गंभीर'),
    (r'  गंभीर', 'गंभीर'),
    (r'  मध्यम', 'मध्यम'),

    # AI conclusion boilerplate - clean
    (r'\*\*CaneUp\*\* पर[^।\n]*[।\n]', ''),
    (r'CaneUp\.xyz पर[^।\n]*[।\n]', ''),
    (r'यदि यह लेख[^।\n]*शेयर करें[।!]\s*', ''),

    # Cleanup "(टिप्पणी)" and "(विवरण)" as table column headers - fine to keep
    # Remove "Step-by-Step" and replace with simpler Hindi
    # Keep English terms like "Fertigation", "DBT" - they are standard

    # Fix double-space bullet points
    (r'\n\n\n+', '\n\n'),
]

# ---------------------------------------------------------------
# Specific patterns to clean per-article type
# ---------------------------------------------------------------

def apply_phrase_subs(text):
    for pattern, repl in PHRASE_SUBS:
        if callable(repl):
            text = re.sub(pattern, repl, text, flags=re.MULTILINE)
        else:
            text = re.sub(pattern, repl, text, flags=re.MULTILINE)
    return text

def humanize_intro(body):
    """
    Make the opening paragraph more natural.
    Remove AI tells like 'इस Complete Guide', 'पूरी जानकारी देंगे',
    'हर वह जानकारी', etc.
    """
    # Pattern: first paragraph after H1 heading
    # Replace generic "यह Complete Guide 2026 के संदर्भ में आपको हर वह जानकारी..."
    body = re.sub(
        r'यह Complete Guide 2026 के संदर्भ में आपको हर वह जानकारी देगी जिसे आपको[^।]*।',
        '', body
    )
    # "इस Complete Guide में हम X जानकारी देंगे"
    body = re.sub(
        r'इस Complete Guide में हम [^।]{5,100}।\s*',
        '', body
    )
    return body

def clean_conclusion(body):
    """
    Replace generic AI conclusions with natural sign-off.
    Keep the actual summary content but remove the robotic wrap.
    """
    # Remove the generic "CaneUp par padhen" lines
    body = re.sub(
        r'\*\*CaneUp\*\* पर[^\n]*\n',
        '', body
    )
    body = re.sub(
        r'CaneUp\.xyz पर[^\n]*\n',
        '', body
    )
    # Remove "यदि यह लेख अच्छा लगा हो तो..."
    body = re.sub(
        r'यदि यह लेख[^\n]*\n',
        '', body
    )
    # Remove "अगर यह लेख आपके काम आया तो इसे..."
    body = re.sub(
        r'अगर यह लेख[^\n]*\n',
        '', body
    )
    return body

def fix_table_severity(body):
    """Fix garbled severity icons in tables that weren't caught."""
    body = re.sub(r'  Very High', 'Very High', body)
    body = re.sub(r'  High', 'High', body)
    body = re.sub(r'  Medium', 'Medium', body)
    return body

def remove_promotional_lines(body):
    """Remove self-promotional lines."""
    lines = body.split('\n')
    out = []
    for line in lines:
        # Skip "**किसान के लिए वरदान**" type marketing phrasing
        # but only standalone lines, not embedded in real content
        skip = False
        # Generic "यह योजना वरदान है" type
        if re.match(r'^[*_]*PM किसान[^।]*वरदान[^।]*[*_]*$', line.strip()):
            skip = True
        # Lone exclamation marketing
        if re.match(r'^\*\*.*!\*\*$', line.strip()) and len(line.strip()) < 60:
            skip = True
        if not skip:
            out.append(line)
    return '\n'.join(out)

def split_fm(content):
    if not content.startswith('---'):
        return None, content
    idx = content.find('\n---', 3)
    if idx == -1:
        return None, content
    return content[3:idx], content[idx+4:]

def reassemble(fm, body):
    if fm is None:
        return body
    return '---' + fm + '\n---' + body

def process(fp):
    with open(fp, 'r', encoding='utf-8') as f:
        original = f.read()

    fm, body = split_fm(original)

    body = humanize_intro(body)
    body = apply_phrase_subs(body)
    body = clean_conclusion(body)
    body = fix_table_severity(body)
    body = remove_promotional_lines(body)
    body = re.sub(r'\n{4,}', '\n\n\n', body)

    new = reassemble(fm, body)
    if new != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new)
        return True
    return False

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    d = os.path.join(base, POSTS_DIR)

    # Process only numbered articles 01-10
    numbered = [
        '01-ganne-mein-kharpatwar-niyantran.md',
        '02-ganne-mein-sinchai-ka-sahi-tarika.md',
        '03-pm-kisan-samman-nidhi-2026.md',
        '04-ganne-se-ethanol-business-2026.md',
        '05-ganne-ki-nai-kismen-2026.md',
        '06-ganna-msp-rate-2026-27.md',
        '07-eganna-app-download-2026.md',
        '08-kisan-credit-card-kcc-2026.md',
        '09-ganne-mein-keet-aur-rog-prabandhan.md',
        '10-sugar-mill-ganna-registration-2026.md',
        # Also hit the popular farming guides
        'ganne-ki-kheti-guide.md',
        'ganne-ki-kheti-trending-2026.md',
        'ganna-parchi-calendar-2026-27-online.md',
        'ganna-bhugtan-status-2026-online.md',
        'caneup-portal-2026.md',
    ]

    changed = 0
    for fn in numbered:
        fp = os.path.join(d, fn)
        if not os.path.exists(fp):
            print(f"  [NOT FOUND] {fn}")
            continue
        if process(fp):
            changed += 1
            print(f"  [UPDATED] {fn}")
        else:
            print(f"  [ok]      {fn}")

    print(f"\nDone: {changed} files updated")

if __name__ == '__main__':
    main()
