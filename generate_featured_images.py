#!/usr/bin/env python3
"""Generate WebP featured images for all Hugo posts - Google Discover optimized (1200x630)"""

import os
import re
import yaml
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# Paths
CONTENT_DIR = "content/posts"
OUTPUT_DIR = "static/images/blog"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Google Discover: 1200x630 minimum
WIDTH, HEIGHT = 1200, 630

# Category configs: gradient colors + emoji
CATEGORY_CONFIG = {
    "parchi calendar": {
        "colors": [(21, 128, 61), (22, 101, 52)],
        "accent": (245, 158, 11),
        "emoji": "📋",
        "label": "पर्ची कैलेंडर"
    },
    "msp rate": {
        "colors": [(245, 158, 11), (217, 119, 6)],
        "accent": (21, 128, 61),
        "emoji": "💰",
        "label": "MSP रेट"
    },
    "ganna kheti": {
        "colors": [(21, 128, 61), (5, 46, 22)],
        "accent": (245, 158, 11),
        "emoji": "🌾",
        "label": "गन्ना खेती"
    },
    "sarkari yojana": {
        "colors": [(124, 58, 237), (109, 40, 217)],
        "accent": (245, 158, 11),
        "emoji": "🏛️",
        "label": "सरकारी योजना"
    },
    "business": {
        "colors": [(245, 158, 11), (234, 88, 12)],
        "accent": (21, 128, 61),
        "emoji": "💼",
        "label": "बिज़नेस"
    },
    "eganna app": {
        "colors": [(14, 165, 233), (2, 132, 199)],
        "accent": (245, 158, 11),
        "emoji": "📱",
        "label": "eGanna App"
    },
    "sugar mill": {
        "colors": [(71, 85, 105), (51, 65, 85)],
        "accent": (245, 158, 11),
        "emoji": "🏭",
        "label": "शुगर मिल"
    },
    "kcc loan": {
        "colors": [(220, 38, 38), (185, 28, 28)],
        "accent": (245, 158, 11),
        "emoji": "🏦",
        "label": "KCC लोन"
    },
    "caneup": {
        "colors": [(21, 128, 61), (22, 101, 52)],
        "accent": (245, 158, 11),
        "emoji": "🌾",
        "label": "CaneUp"
    },
    "default": {
        "colors": [(21, 128, 61), (5, 46, 22)],
        "accent": (245, 158, 11),
        "emoji": "🌾",
        "label": "गन्ना जानकारी"
    }
}

def get_font(size, bold=False):
    """Get a font, falling back to default if needed"""
    font_paths = [
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf" if bold else "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            return ImageFont.truetype(fp, size)
    return ImageFont.load_default()

def draw_gradient(draw, width, height, color1, color2):
    """Draw a horizontal gradient"""
    for y in range(height):
        ratio = y / height
        r = int(color1[0] + (color2[0] - color1[0]) * ratio)
        g = int(color1[1] + (color2[1] - color1[1]) * ratio)
        b = int(color1[2] + (color2[2] - color1[2]) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

def draw_pattern(draw, width, height, color):
    """Draw subtle diagonal line pattern for texture"""
    for i in range(-height, width + height, 40):
        draw.line([(i, 0), (i + height, height)], fill=(*color, 15), width=1)

def wrap_text(text, font, max_width, draw):
    """Wrap text to fit within max_width"""
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        test_line = f"{current_line} {word}".strip()
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines

def create_featured_image(title, category, slug, output_path):
    """Create a professional featured image"""
    cat_lower = category.lower() if category else "default"
    config = CATEGORY_CONFIG.get(cat_lower, CATEGORY_CONFIG["default"])

    img = Image.new("RGB", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)

    # Gradient background
    draw_gradient(draw, WIDTH, HEIGHT, config["colors"][0], config["colors"][1])

    # Subtle pattern overlay
    pattern_img = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    pattern_draw = ImageDraw.Draw(pattern_img)
    draw_pattern(pattern_draw, WIDTH, HEIGHT, (255, 255, 255))
    img = Image.alpha_composite(img.convert("RGBA"), pattern_img)
    draw = ImageDraw.Draw(img)

    # Dark overlay box on left side
    overlay_x, overlay_y = 60, 60
    overlay_w, overlay_h = 680, HEIGHT - 120
    overlay = Image.new("RGBA", (overlay_w, overlay_h), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    # Rounded rectangle approximation
    overlay_draw.rectangle([(0, 0), (overlay_w, overlay_h)], fill=(0, 0, 0, 140))
    overlay_draw.rectangle([(2, 2), (overlay_w-2, overlay_h-2)], fill=(0, 0, 0, 100))
    img.paste(overlay, (overlay_x, overlay_y), overlay)
    draw = ImageDraw.Draw(img)

    # Category label at top
    label_font = get_font(22, bold=True)
    label_text = f"  {config['emoji']}  {config['label']}  "
    label_bbox = draw.textbbox((0, 0), label_text, font=label_font)
    label_w = label_bbox[2] - label_bbox[0]
    label_h = label_bbox[3] - label_bbox[1]
    label_x = overlay_x + 30
    label_y = overlay_y + 30
    # Label background
    draw.rectangle(
        [(label_x - 8, label_y - 4), (label_x + label_w + 8, label_y + label_h + 8)],
        fill=config["accent"]
    )
    draw.text((label_x, label_y), label_text, fill=(0, 0, 0), font=label_font)

    # Title text
    title_font = get_font(42, bold=True)
    title_lines = wrap_text(title, title_font, overlay_w - 80, draw)
    title_y = label_y + label_h + 40
    max_lines = 4
    for i, line in enumerate(title_lines[:max_lines]):
        draw.text((overlay_x + 30, title_y + i * 55), line, fill=(255, 255, 255), font=title_font)

    # Bottom bar with CTA
    bar_y = overlay_y + overlay_h - 70
    draw.rectangle(
        [(overlay_x, bar_y), (overlay_x + overlay_w, overlay_y + overlay_h)],
        fill=(*config["accent"], 200)
    )
    cta_font = get_font(20, bold=True)
    cta_text = "📖  CaneUp.xyz  —  पूरी जानकारी पढ़ें →"
    draw.text((overlay_x + 30, bar_y + 22), cta_text, fill=(0, 0, 0), font=cta_font)

    # Right side: large emoji
    emoji_font = get_font(180)
    # Position emoji on right side
    emoji_x = WIDTH - 300
    emoji_y = HEIGHT // 2 - 100
    draw.text((emoji_x, emoji_y), config["emoji"], fill=(255, 255, 255), font=emoji_font)

    # Decorative circles
    for cx, cy, cr in [(WIDTH - 100, 80, 30), (WIDTH - 60, HEIGHT - 80, 20), (WIDTH - 200, HEIGHT - 40, 15)]:
        draw.ellipse([(cx-cr, cy-cr), (cx+cr, cy+cr)], fill=(*config["accent"], 60))

    # CaneUp logo text at bottom right
    logo_font = get_font(18, bold=True)
    draw.text((WIDTH - 200, HEIGHT - 40), "🌾 CaneUp.xyz", fill=(255, 255, 255, 180), font=logo_font)

    # Convert to RGB and save as WebP
    img_rgb = img.convert("RGB")
    img_rgb.save(output_path, "WEBP", quality=85, method=6)
    return True

def parse_front_matter(filepath):
    """Parse YAML front matter from markdown file"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---"):
        return None, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content
    try:
        fm = yaml.safe_load(parts[1])
        return fm, content
    except:
        return None, content

def update_front_matter(filepath, fm, original_content):
    """Update front matter with featured_image field"""
    parts = original_content.split("---", 2)
    if len(parts) < 3:
        return
    new_fm = yaml.dump(fm, allow_unicode=True, default_flow_style=False, sort_keys=False)
    new_content = f"---\n{new_fm}---{parts[2]}"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

def main():
    posts_dir = Path(CONTENT_DIR)
    if not posts_dir.exists():
        print(f"ERROR: {CONTENT_DIR} not found!")
        return

    md_files = sorted(posts_dir.glob("*.md"))
    print(f"Found {len(md_files)} posts to process\n")

    success = 0
    skipped = 0
    errors = 0

    for md_file in md_files:
        fm, content = parse_front_matter(md_file)
        if not fm:
            print(f"  SKIP (no front matter): {md_file.name}")
            skipped += 1
            continue

        title = fm.get("title", md_file.stem.replace("-", " ").title())
        categories = fm.get("categories", [])
        category = categories[0] if categories else "default"
        slug = md_file.stem

        # Output path
        output_filename = f"{slug}.webp"
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        web_path = f"/images/blog/{output_filename}"

        # Skip if image already exists and front matter already has it
        if os.path.exists(output_path) and fm.get("featured_image") == web_path:
            print(f"  SKIP (exists): {md_file.name}")
            skipped += 1
            continue

        try:
            create_featured_image(title, category, slug, output_path)

            # Update front matter
            fm["featured_image"] = web_path
            if "image" not in fm or not fm["image"]:
                fm["image"] = web_path

            update_front_matter(md_file, fm, content)
            print(f"  ✅ {md_file.name} → {output_filename}")
            success += 1
        except Exception as e:
            print(f"  ❌ {md_file.name}: {e}")
            errors += 1

    print(f"\n{'='*50}")
    print(f"✅ Generated: {success}")
    print(f"⏭️  Skipped:   {skipped}")
    print(f"❌ Errors:    {errors}")
    print(f"📁 Output:    {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
