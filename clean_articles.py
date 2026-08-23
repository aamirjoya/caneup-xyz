#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, io, os, re, glob

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

POSTS_DIR    = r"content\posts"
STORIES_DIR  = r"content\webstories"

# -------------------------------------------------------------------
# Emoji removal — broad range covers all common emoji blocks
# -------------------------------------------------------------------
EMOJI_RE = re.compile(
    "[\U0001F000-\U0001FFFF"   # Misc symbols incl. 🌾 etc
    "\U00002600-\U000027BF"    # Misc symbols ☎ ✅ ⚠ etc
    "\U0000FE00-\U0000FE0F"    # Variation selectors
    "\U00002700-\U000027BF"    # Dingbats
    "\U0001F900-\U0001F9FF"    # Supplemental symbols
    "\U00003000-\U00003300"    # CJK symbols (some emoji here)
    "\u200D"                   # ZWJ
    "\uFE0F"                   # VS16
    "]+",
    flags=re.UNICODE
)

# Extra individual emoji not caught by ranges
EXTRA = [
    '\u2705','\u274C','\u2714','\u2716','\u26A0','\u2728','\u2B50',
    '\u23F0','\u23F3','\u231A','\u231B','\u25B6','\u25C0','\u25AA',
    '\u25AB','\u25FB','\u25FC','\u25FD','\u25FE','\u2614','\u2615',
    '\u2648','\u2649','\u264A','\u264B','\u264C','\u264D','\u264E',
    '\u264F','\u2650','\u2651','\u2652','\u2653','\u267B','\u267F',
    '\u2693','\u26AA','\u26AB','\u26BD','\u26BE','\u26C4','\u26C5',
    '\u26CE','\u26D4','\u26EA','\u26F2','\u26F3','\u26F5','\u26FA',
    '\u26FD','\u2702','\u2708','\u2709','\u270A','\u270B','\u270C',
    '\u270D','\u270F','\u2712','\u2764',
]

def strip_emojis(text):
    text = EMOJI_RE.sub('', text)
    for ch in EXTRA:
        text = text.replace(ch, '')
    return text

# -------------------------------------------------------------------
# Fix garbled rupee like ₹₹₹340, ₹₳40, Unicode digit variants
# -------------------------------------------------------------------
UNICODE_DIGITS = str.maketrans('₀₁₂₃₄₅₆₇₈₉', '0123456789')

def fix_rupee(text):
    text = re.sub(r'₹{2,}', '₹', text)   # ₹₹₹ → ₹
    text = text.replace('₳', '')           # stray variant
    text = text.translate(UNICODE_DIGITS)  # Unicode digit → ASCII
    return text

# -------------------------------------------------------------------
# Remove duplicate / expanded FAQ and second "यह भी पढ़ें" block
# -------------------------------------------------------------------
def remove_duplicates(body):
    """
    1. Remove any heading that says '(Expanded FAQ)' and everything
       until the next ## heading.
    2. Keep only the FIRST ## ...यह भी पढ़ें... block.
    """
    lines = body.split('\n')
    out = []
    skipping = False
    yah_bhi_count = 0

    for line in lines:
        stripped = line.strip()

        # --- detect expanded FAQ section ---
        if re.search(r'Expanded\s+FAQ', stripped, re.IGNORECASE):
            skipping = True
            continue

        # --- detect "यह भी पढ़ें" H2 headings ---
        if re.match(r'^##\s+', stripped) and 'यह भी पढ़ें' in stripped:
            yah_bhi_count += 1
            if yah_bhi_count >= 2:
                skipping = True
                continue
            else:
                # first occurrence — emit it (cleaned of emoji)
                out.append(line)
                continue

        # --- if skipping, stop at next H2 ---
        if skipping:
            if re.match(r'^##\s+', stripped):
                skipping = False
                # check this new heading isn't another yah bhi
                if 'यह भी पढ़ें' in stripped:
                    yah_bhi_count += 1
                    if yah_bhi_count >= 2:
                        skipping = True
                        continue
                out.append(line)
            # else: still skipping, drop line
            continue

        out.append(line)

    return '\n'.join(out)

# -------------------------------------------------------------------
# Clean emojis from every line (headings, bullets, prose, tables)
# -------------------------------------------------------------------
def clean_body(body):
    lines = body.split('\n')
    in_code = False
    out = []
    for line in lines:
        if line.strip().startswith('```'):
            in_code = not in_code
        if not in_code:
            line = strip_emojis(line)
            line = fix_rupee(line)
            # normalise multiple spaces (not inside tables)
            if not re.match(r'^\s*\|', line):
                line = re.sub(r' {2,}', ' ', line)
            line = line.rstrip()
        out.append(line)
    return '\n'.join(out)

# -------------------------------------------------------------------
# Clean frontmatter (title, description)
# -------------------------------------------------------------------
def clean_frontmatter(fm):
    lines = fm.split('\n')
    out = []
    for line in lines:
        if re.match(r'^(title|description)\s*:', line):
            line = strip_emojis(line)
            line = fix_rupee(line)
            line = line.rstrip()
        out.append(line)
    return '\n'.join(out)

# -------------------------------------------------------------------
# Split / reassemble frontmatter
# -------------------------------------------------------------------
def split_fm(content):
    if not content.startswith('---'):
        return None, content
    idx = content.find('\n---', 3)
    if idx == -1:
        return None, content
    fm   = content[3:idx]          # between first --- and second ---
    body = content[idx+4:]         # after second ---\n
    return fm, body

def reassemble(fm, body):
    if fm is None:
        return body
    return '---' + fm + '\n---' + body

# -------------------------------------------------------------------
# Process one file
# -------------------------------------------------------------------
def process(fp):
    with open(fp, 'r', encoding='utf-8') as f:
        original = f.read()

    fm, body = split_fm(original)

    if fm is not None:
        fm = clean_frontmatter(fm)

    body = remove_duplicates(body)
    body = clean_body(body)
    # collapse runs of 3+ blank lines to 2
    body = re.sub(r'\n{4,}', '\n\n\n', body)

    new = reassemble(fm, body)

    if new != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new)
        return True
    return False

# -------------------------------------------------------------------
# Main
# -------------------------------------------------------------------
def main():
    base = os.path.dirname(os.path.abspath(__file__))

    dirs = [
        os.path.join(base, POSTS_DIR),
        os.path.join(base, STORIES_DIR),
    ]

    total = changed = 0
    for d in dirs:
        if not os.path.isdir(d):
            print(f"SKIP (not found): {d}")
            continue
        files = sorted(glob.glob(os.path.join(d, '*.md')))
        print(f"\nProcessing {len(files)} files in {os.path.relpath(d, base)}")
        for fp in files:
            total += 1
            if process(fp):
                changed += 1
                print(f"  [UPDATED] {os.path.basename(fp)}")
            else:
                print(f"  [ok]      {os.path.basename(fp)}")

    print(f"\n{'='*55}")
    print(f"Done: {changed}/{total} files updated")

if __name__ == '__main__':
    main()
