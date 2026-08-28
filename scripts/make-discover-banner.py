import os
import sys
from PIL import Image, ImageDraw, ImageFont

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'

def make_discover_banner(bg_img_path, dst_webp_path, badge_text, headline_text, subtext):
    with Image.open(bg_img_path) as img:
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
        
        draw = ImageDraw.Draw(img)
        
        # Load Hindi font
        font_nirmala = r'C:\Windows\Fonts\Nirmala.ttc'
        font_mangal = r'C:\Windows\Fonts\mangalb.ttf'
        
        if os.path.exists(font_mangal):
            font_path = font_mangal
        elif os.path.exists(font_nirmala):
            font_path = font_nirmala
        else:
            font_path = r'C:\Windows\Fonts\arialbd.ttf'
            
        try:
            font_badge = ImageFont.truetype(font_path, 28, index=0)
            font_headline = ImageFont.truetype(font_path, 50, index=0)
            font_sub = ImageFont.truetype(font_path, 36, index=0)
        except Exception:
            font_badge = ImageFont.truetype(font_path, 28)
            font_headline = ImageFont.truetype(font_path, 50)
            font_sub = ImageFont.truetype(font_path, 36)
            
        # Draw dark translucent newsroom banner at bottom
        banner_h = 240
        overlay = Image.new('RGBA', (1200, banner_h), (11, 15, 25, 235))
        img.paste(overlay, (0, 675 - banner_h), overlay)
        
        # Red top accent line
        draw.rectangle([0, 675 - banner_h, 1200, 675 - banner_h + 8], fill=(239, 68, 68))
        
        # Yellow Badge (Top Left of Banner)
        draw.rectangle([40, 675 - banner_h + 20, 360, 675 - banner_h + 65], fill=(250, 204, 21))
        draw.text((55, 675 - banner_h + 24), badge_text, font=font_badge, fill=(15, 23, 42))
        
        # Main Headline (White)
        draw.text((40, 675 - banner_h + 80), headline_text, font=font_headline, fill=(255, 255, 255))
        
        # Subtitle (Yellow)
        draw.text((40, 675 - banner_h + 155), subtext, font=font_sub, fill=(250, 204, 21))
        
        # Save optimized WebP under 100KB
        quality = 80
        img.save(dst_webp_path, 'WEBP', quality=quality, optimize=True)
        kb = os.path.getsize(dst_webp_path) / 1024.0
        while kb > 98.0 and quality > 35:
            quality -= 5
            img.save(dst_webp_path, 'WEBP', quality=quality, optimize=True)
            kb = os.path.getsize(dst_webp_path) / 1024.0
            
        print(f"Created 100% Accurate Discover Banner: {dst_webp_path} | {kb:.1f} KB")

if __name__ == '__main__':
    src = r'C:\Users\caneu\.gemini\antigravity\brain\f0566670-25ee-4739-bb10-e53286d68160\agwanpur_mill_cover_1787941015390.jpg'
    dst = os.path.join(base_dir, 'static', 'images', 'blog', 'agwanpur-sugar-factory-2026.webp')
    make_discover_banner(
        src,
        dst,
        "CANEUP BADA UPDATE",
        "अगवानपुर चीनी मिल — 204 गांवों की लिस्ट जारी!",
        "गांव कोड व पर्ची कैलेंडर 2026-27 | eGanna App"
    )
