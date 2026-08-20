#!/usr/bin/env python3
"""
Generate Google Discover optimized featured images for CaneUp.xyz
Fetches real photos from internet + adds professional text overlay
Requires: pip install Pillow requests pyyaml

IMAGE SOURCES (priority order):
1. Pexels API (free key: https://www.pexels.com/api/)
2. Pixabay API (free key: https://pixabay.com/api/docs/)
3. Lorem Picsum (no key, random real photos)
4. Gradient fallback (last resort)
"""

import os
import re
import sys
import time
import hashlib
import yaml
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
from pathlib import Path

# ============================================================
# CONFIG
# ============================================================
CONTENT_DIR = "content/posts"
OUTPUT_DIR = "static/images/blog"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Google Discover minimum: 1200x630
WIDTH, HEIGHT = 1200, 630

# API Keys (set via environment variables)
PEXELS_API_KEY = os.environ.get("PEXELS_API_KEY", "")
PIXABAY_API_KEY = os.environ.get("PIXABAY_API_KEY", "")

# ============================================================
# CATEGORY CONFIGS — search queries + overlay style
# ============================================================
CATEGORY_CONFIG = {
    "parchi calendar": {
        "search_queries": ["sugarcane harvest", "indian sugarcane farmer field", "sugarcane plantation india"],
        "picsum_seed": "parchi-calendar",
        "accent": (245, 158, 11),
        "text_color": (255, 255, 255),
        "emoji": "📋",
        "label": "पर्ची कैलेंडर",
        "gradient_top": (21, 128, 61, 80),
        "gradient_bottom": (0, 0, 0, 180),
    },
    "msp rate": {
        "search_queries": ["sugarcane price market", "indian farmer money rupee", "sugarcane market"],
        "picsum_seed": "msp-rate",
        "accent": (245, 158, 11),
        "text_color": (255, 255, 255),
        "emoji": "💰",
        "label": "MSP रेट",
        "gradient_top": (245, 158, 11, 60),
        "gradient_bottom": (0, 0, 0, 180),
    },
    "ganna kheti": {
        "search_queries": ["sugarcane farming", "green sugarcane field", "sugarcane plantation"],
        "picsum_seed": "ganna-kheti",
        "accent": (245, 158, 11),
        "text_color": (255, 255, 255),
        "emoji": "🌾",
        "label": "गन्ना खेती",
        "gradient_top": (21, 128, 61, 60),
        "gradient_bottom": (0, 0, 0, 170),
    },
    "sarkari yojana": {
        "search_queries": ["indian government farmer", "pm kisan scheme", "farmer subsidy india"],
        "picsum_seed": "sarkari-yojana",
        "accent": (124, 58, 237),
        "text_color": (255, 255, 255),
        "emoji": "🏛️",
        "label": "सरकारी योजना",
        "gradient_top": (124, 58, 237, 60),
        "gradient_bottom": (0, 0, 0, 180),
    },
    "business": {
        "search_queries": ["sugar mill factory", "jaggery production india", "sugarcane business"],
        "picsum_seed": "business",
        "accent": (245, 158, 11),
        "text_color": (255, 255, 255),
        "emoji": "💼",
        "label": "बिज़नेस",
        "gradient_top": (234, 88, 12, 60),
        "gradient_bottom": (0, 0, 0, 180),
    },
    "eganna app": {
        "search_queries": ["mobile app farmer india", "smartphone agriculture", "digital farming"],
        "picsum_seed": "eganna-app",
        "accent": (14, 165, 233),
        "text_color": (255, 255, 255),
        "emoji": "📱",
        "label": "eGanna App",
        "gradient_top": (14, 165, 233, 60),
        "gradient_bottom": (0, 0, 0, 180),
    },
    "sugar mill": {
        "search_queries": ["sugar mill factory", "sugarcane crushing", "sugar refinery india"],
        "picsum_seed": "sugar-mill",
        "accent": (245, 158, 11),
        "text_color": (255, 255, 255),
        "emoji": "🏭",
        "label": "शुगर मिल",
        "gradient_top": (71, 85, 105, 60),
        "gradient_bottom": (0, 0, 0, 185),
    },
    "kcc loan": {
        "search_queries": ["kisan credit card", "farmer bank loan india", "agriculture loan"],
        "picsum_seed": "kcc-loan",
        "accent": (220, 38, 38),
        "text_color": (255, 255, 255),
        "emoji": "🏦",
        "label": "KCC लोन",
        "gradient_top": (220, 38, 38, 60),
        "gradient_bottom": (0, 0, 0, 180),
    },
    "caneup": {
        "search_queries": ["sugarcane farming india", "green sugarcane field", "indian farmer"],
        "picsum_seed": "caneup",
        "accent": (245, 158, 11),
        "text_color": (255, 255, 255),
        "emoji": "🌾",
        "label": "CaneUp",
        "gradient_top": (21, 128, 61, 60),
        "gradient_bottom": (0, 0, 0, 170),
    },
    "default": {
        "search_queries": ["sugarcane field india", "green farming", "rural india agriculture"],
        "picsum_seed": "default",
        "accent": (245, 158, 11),
        "text_color": (255, 255, 255),
        "emoji": "🌾",
        "label": "गन्ना जानकारी",
        "gradient_top": (21, 128, 61, 60),
        "gradient_bottom": (0, 0, 0, 170),
    },
}

# ============================================================
# FONT HELPER
# ============================================================
def get_font(size, bold=False):
    """Get Hindi-compatible font"""
    font_paths = [
        "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
        "/usr/share/fonts/truetype/noto/NotoSansDevanagari-Bold.ttf" if bold else "/usr/share/fonts/truetype/noto/NotoSansDevanagari-Regular.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf" if bold else "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                return ImageFont.truetype(fp, size)
            except:
                continue
    return ImageFont.load_default()


# ============================================================
# IMAGE FETCHING — Multiple sources with fallback
# ============================================================
def fetch_image_from_pexels(query):
    """Fetch from Pexels API (free key)"""
    if not PEXELS_API_KEY:
        return None
    try:
        headers = {"Authorization": PEXELS_API_KEY}
        params = {"query": query, "per_page": 5, "orientation": "landscape"}
        resp = requests.get("https://api.pexels.com/v1/search", headers=headers, params=params, timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            for photo in data.get("photos", []):
                img_url = photo["src"]["large2x"]
                img_resp = requests.get(img_url, timeout=15)
                if img_resp.status_code == 200:
                    img = Image.open(BytesIO(img_resp.content)).convert("RGB")
                    if img.size[0] >= 800 and img.size[1] >= 400:
                        return img
    except Exception as e:
        print(f"    Pexels error: {e}")
    return None


def fetch_image_from_pixabay(query):
    """Fetch from Pixabay API (free key)"""
    if not PIXABAY_API_KEY:
        return None
    try:
        params = {
            "key": PIXABAY_API_KEY,
            "q": query,
            "image_type": "photo",
            "orientation": "horizontal",
            "min_width": 1000,
            "per_page": 5,
            "safesearch": "true",
        }
        resp = requests.get("https://pixabay.com/api/", params=params, timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            for hit in data.get("hits", []):
                img_url = hit.get("largeImageURL") or hit.get("webformatURL")
                img_resp = requests.get(img_url, timeout=15)
                if img_resp.status_code == 200:
                    img = Image.open(BytesIO(img_resp.content)).convert("RGB")
                    if img.size[0] >= 800 and img.size[1] >= 400:
                        return img
    except Exception as e:
        print(f"    Pixabay error: {e}")
    return None


def fetch_image_from_picsum(seed="sugarcane"):
    """Fetch from Lorem Picsum (no key needed, real photos)"""
    try:
        # Use seed for consistent results per category
        url = f"https://picsum.photos/seed/{seed}/1200/630"
        resp = requests.get(url, timeout=15, allow_redirects=True)
        if resp.status_code == 200 and len(resp.content) > 5000:
            img = Image.open(BytesIO(resp.content)).convert("RGB")
            if img.size[0] >= 800 and img.size[1] >= 400:
                return img
    except Exception as e:
        print(f"    Picsum error: {e}")
    return None


def fetch_real_image(queries, picsum_seed="default"):
    """Try multiple sources with multiple queries"""
    # 1. Try Pexels (best quality, topic-specific)
    if PEXELS_API_KEY:
        for query in queries:
            print(f"    🔍 Pexels: '{query}'...")
            img = fetch_image_from_pexels(query)
            if img:
                print(f"    ✅ Got image from Pexels!")
                return img
            time.sleep(0.3)

    # 2. Try Pixabay (good quality, topic-specific)
    if PIXABAY_API_KEY:
        for query in queries:
            print(f"    🔍 Pixabay: '{query}'...")
            img = fetch_image_from_pixabay(query)
            if img:
                print(f"    ✅ Got image from Pixabay!")
                return img
            time.sleep(0.3)

    # 3. Try Lorem Picsum (random real photo, no key)
    print(f"    🔍 Picsum (real photo, random)...")
    img = fetch_image_from_picsum(picsum_seed)
    if img:
        print(f"    ✅ Got image from Picsum!")
        return img

    # 4. Try Picsum with different seeds
    for alt_seed in ["nature", "landscape", "green", "field", "farm"]:
        print(f"    🔍 Picsum alt: '{alt_seed}'...")
        img = fetch_image_from_picsum(alt_seed)
        if img:
            print(f"    ✅ Got image from Picsum (alt)!")
            return img

    return None


# ============================================================
# IMAGE PROCESSING
# ============================================================
def prepare_background(raw_img, target_w=WIDTH, target_h=HEIGHT):
    """Crop and resize image to exact 1200x630"""
    img_ratio = raw_img.width / raw_img.height
    target_ratio = target_w / target_h

    if img_ratio > target_ratio:
        new_h = raw_img.height
        new_w = int(new_h * target_ratio)
        left = (raw_img.width - new_w) // 2
        raw_img = raw_img.crop((left, 0, left + new_w, new_h))
    else:
        new_w = raw_img.width
        new_h = int(new_w / target_ratio)
        top = (raw_img.height - new_h) // 4
        raw_img = raw_img.crop((0, top, new_w, top + new_h))

    raw_img = raw_img.resize((target_w, target_h), Image.LANCZOS)
    # Slight blur for text readability
    raw_img = raw_img.filter(ImageFilter.GaussianBlur(radius=1.5))
    # Reduce brightness so text pops
    enhancer = ImageEnhance.Brightness(raw_img)
    raw_img = enhancer.enhance(0.70)
    return raw_img


def add_gradient_overlay(img, config):
    """Add gradient overlay from top (transparent) to bottom (dark)"""
    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    top_color = config["gradient_top"]
    bottom_color = config["gradient_bottom"]

    for y in range(HEIGHT):
        ratio = (y / HEIGHT) ** 0.7
        r = int(top_color[0] + (bottom_color[0] - top_color[0]) * ratio)
        g = int(top_color[1] + (bottom_color[1] - top_color[1]) * ratio)
        b = int(top_color[2] + (bottom_color[2] - top_color[2]) * ratio)
        a = int(top_color[3] + (bottom_color[3] - top_color[3]) * ratio)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b, a))

    img = Image.alpha_composite(img.convert("RGBA"), overlay)
    return img


def add_text_overlay(img, title, category, config):
    """Add professional text overlay"""
    draw = ImageDraw.Draw(img)

    # --- Left dark panel for text readability ---
    panel_w = 780
    panel = Image.new("RGBA", (panel_w, HEIGHT), (0, 0, 0, 0))
    panel_draw = ImageDraw.Draw(panel)
    # Gradient panel: dark on left, transparent on right
    for x in range(panel_w):
        ratio = (x / panel_w) ** 1.5
        a = int(180 * (1 - ratio))
        panel_draw.line([(x, 0), (x, HEIGHT)], fill=(0, 0, 0, a))
    img.paste(panel, (0, 0), panel)
    draw = ImageDraw.Draw(img)

    # --- Category Badge ---
    badge_font = get_font(20, bold=True)
    badge_text = f"  {config['emoji']}  {config['label']}  "
    badge_bbox = draw.textbbox((0, 0), badge_text, font=badge_font)
    badge_w = badge_bbox[2] - badge_bbox[0] + 24
    badge_h = badge_bbox[3] - badge_bbox[1] + 16
    badge_x, badge_y = 50, 45

    badge_bg = Image.new("RGBA", (badge_w, badge_h), (0, 0, 0, 0))
    badge_draw = ImageDraw.Draw(badge_bg)
    badge_draw.rounded_rectangle([(0, 0), (badge_w, badge_h)], radius=8, fill=(*config["accent"], 240))
    img.paste(badge_bg, (badge_x, badge_y), badge_bg)
    draw = ImageDraw.Draw(img)
    draw.text((badge_x + 12, badge_y + 4), badge_text, fill=(0, 0, 0), font=badge_font)

    # --- Title ---
    title_font = get_font(44, bold=True)
    title_max_w = 700

    words = title.split()
    lines = []
    current_line = ""
    for word in words:
        test_line = f"{current_line} {word}".strip()
        bbox = draw.textbbox((0, 0), test_line, font=title_font)
        if bbox[2] - bbox[0] <= title_max_w:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)

    lines = lines[:4]
    title_y = badge_y + badge_h + 35
    line_height = 56

    for i, line in enumerate(lines):
        y = title_y + i * line_height
        # Shadow
        draw.text((52, y + 3), line, fill=(0, 0, 0, 220), font=title_font)
        # Main text
        draw.text((50, y), line, fill=config["text_color"], font=title_font)

    # --- Bottom CTA bar ---
    bar_h = 50
    bar_y = HEIGHT - bar_h - 25
    bar_x = 50
    bar_w = 500

    bar_bg = Image.new("RGBA", (bar_w, bar_h), (0, 0, 0, 0))
    bar_draw = ImageDraw.Draw(bar_bg)
    bar_draw.rounded_rectangle([(0, 0), (bar_w, bar_h)], radius=10, fill=(*config["accent"], 220))
    img.paste(bar_bg, (bar_x, bar_y), bar_bg)
    draw = ImageDraw.Draw(img)

    cta_font = get_font(19, bold=True)
    cta_text = "📖  CaneUp.xyz — पूरी जानकारी पढ़ें →"
    draw.text((bar_x + 22, bar_y + 13), cta_text, fill=(0, 0, 0), font=cta_font)

    # --- Right side accent circle ---
    circle_x = WIDTH - 160
    circle_y = HEIGHT // 2 - 50
    circle_r = 75
    circle_bg = Image.new("RGBA", (circle_r * 2, circle_r * 2), (0, 0, 0, 0))
    circle_draw = ImageDraw.Draw(circle_bg)
    circle_draw.ellipse([(0, 0), (circle_r * 2, circle_r * 2)], fill=(*config["accent"], 45))
    img.paste(circle_bg, (circle_x - circle_r, circle_y - circle_r), circle_bg)
    draw = ImageDraw.Draw(img)

    # Large emoji
    emoji_font = get_font(72)
    emoji_bbox = draw.textbbox((0, 0), config["emoji"], font=emoji_font)
    emoji_w = emoji_bbox[2] - emoji_bbox[0]
    emoji_h = emoji_bbox[3] - emoji_bbox[1]
    draw.text(
        (circle_x - emoji_w // 2, circle_y - emoji_h // 2),
        config["emoji"],
        fill=(255, 255, 255, 200),
        font=emoji_font,
    )

    # --- Watermark ---
    wm_font = get_font(16, bold=True)
    wm_text = "🌾 CaneUp.xyz"
    wm_bbox = draw.textbbox((0, 0), wm_text, font=wm_font)
    wm_w = wm_bbox[2] - wm_bbox[0]
    draw.text((WIDTH - wm_w - 25, HEIGHT - 30), wm_text, fill=(255, 255, 255, 160), font=wm_font)

    return img


# ============================================================
# FALLBACK: Gradient-only image
# ============================================================
def create_gradient_fallback(title, config):
    """Create gradient + pattern fallback image"""
    img = Image.new("RGBA", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)

    c1 = config["gradient_top"][:3]
    c2 = config["gradient_bottom"][:3]
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(c1[0] + (c2[0] - c1[0]) * ratio)
        g = int(c1[1] + (c2[1] - c1[1]) * ratio)
        b = int(c1[2] + (c2[2] - c1[2]) * ratio)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b, 255))

    # Add subtle diagonal pattern
    pattern = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    p_draw = ImageDraw.Draw(pattern)
    for i in range(-HEIGHT, WIDTH + HEIGHT, 45):
        p_draw.line([(i, 0), (i + HEIGHT, HEIGHT)], fill=(255, 255, 255, 12), width=1)
    img = Image.alpha_composite(img, pattern)

    return img


# ============================================================
# MAIN GENERATOR
# ============================================================
def create_featured_image(title, category, slug, output_path, force=False):
    """Create a professional featured image"""
    cat_lower = category.lower() if category else "default"
    config = CATEGORY_CONFIG.get(cat_lower, CATEGORY_CONFIG["default"])

    # 1. Fetch real image
    print(f"  📸 Fetching image for: {title[:50]}...")
    raw_img = fetch_real_image(config["search_queries"], config["picsum_seed"])

    if raw_img:
        bg = prepare_background(raw_img).convert("RGBA")
        print(f"    🖼️  Image ready ({bg.size[0]}x{bg.size[1]})")
    else:
        print(f"    ⚠️ No internet image, using gradient fallback")
        bg = create_gradient_fallback(title, config)

    # 2. Add gradient overlay
    bg = add_gradient_overlay(bg, config)

    # 3. Add text overlay
    bg = add_text_overlay(bg, title, category, config)

    # 4. Save as WebP
    final = bg.convert("RGB")
    final.save(output_path, "WEBP", quality=88, method=6)
    file_size = os.path.getsize(output_path)
    print(f"    💾 Saved: {output_path} ({file_size // 1024}KB)")
    return True


# ============================================================
# FRONT MATTER
# ============================================================
def parse_front_matter(filepath):
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
    parts = original_content.split("---", 2)
    if len(parts) < 3:
        return
    new_fm = yaml.dump(fm, allow_unicode=True, default_flow_style=False, sort_keys=False)
    new_content = f"---\n{new_fm}---{parts[2]}"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)


# ============================================================
# MAIN
# ============================================================
def main():
    force = "--force" in sys.argv
    limit = None
    for arg in sys.argv[1:]:
        if arg.startswith("--limit="):
            limit = int(arg.split("=")[1])

    posts_dir = Path(CONTENT_DIR)
    if not posts_dir.exists():
        print(f"ERROR: {CONTENT_DIR} not found!")
        return

    md_files = sorted(posts_dir.glob("*.md"))
    if limit:
        md_files = md_files[:limit]

    print(f"Found {len(md_files)} posts to process")
    print(f"Force mode: {force}")
    print(f"Pexels API: {'✅ Set' if PEXELS_API_KEY else '❌ Not set'}")
    print(f"Pixabay API: {'✅ Set' if PIXABAY_API_KEY else '❌ Not set'}")
    print(f"{'=' * 60}\n")

    success = 0
    skipped = 0
    errors = 0

    for i, md_file in enumerate(md_files, 1):
        fm, content = parse_front_matter(md_file)
        if not fm:
            print(f"[{i}/{len(md_files)}] SKIP (no front matter): {md_file.name}")
            skipped += 1
            continue

        title = fm.get("title", md_file.stem.replace("-", " ").title())
        categories = fm.get("categories", [])
        category = categories[0] if categories else "default"
        slug = md_file.stem

        output_filename = f"{slug}.webp"
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        web_path = f"/images/blog/{output_filename}"

        if not force and os.path.exists(output_path) and fm.get("featured_image") == web_path:
            print(f"[{i}/{len(md_files)}] SKIP (exists): {md_file.name}")
            skipped += 1
            continue

        print(f"[{i}/{len(md_files)}] Processing: {md_file.name}")

        try:
            create_featured_image(title, category, slug, output_path, force)

            fm["featured_image"] = web_path
            fm["image"] = web_path
            update_front_matter(md_file, fm, content)
            print(f"  ✅ Done!\n")
            success += 1

            if i < len(md_files):
                time.sleep(1)

        except Exception as e:
            print(f"  ❌ Error: {e}\n")
            errors += 1

    print(f"\n{'=' * 60}")
    print(f"✅ Generated: {success}")
    print(f"⏭️  Skipped:   {skipped}")
    print(f"❌ Errors:    {errors}")
    print(f"📁 Output:    {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
