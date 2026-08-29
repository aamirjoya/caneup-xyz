import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
out_path = os.path.join(base_dir, 'static', 'images', 'news', 'raw-sugar-import-igst-cbic-new-guidelines-2026.webp')
bg_path = os.path.join(r'C:\Users\caneu\.gemini\antigravity\brain\f0566670-25ee-4739-bb10-e53286d68160', 'news9_ethanol_expansion_cover_1787948284345.jpg')

if not os.path.exists(bg_path):
    bg_path = os.path.join(base_dir, 'static', 'images', 'news', 'chini-import-10-lmt-2026.webp')

# Open and resize BG to 1200x675
with Image.open(bg_path) as img:
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
    
    # Create dark vignette / bottom gradient for maximum text readability & punchy contrast
    overlay = Image.new('RGBA', (1200, 675), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    
    # Bottom dark gradient
    for y in range(350, 675):
        alpha = int(220 * ((y - 350) / 325.0) ** 1.3)
        ov_draw.line([(0, y), (1200, y)], fill=(10, 15, 25, alpha))
        
    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    draw = ImageDraw.Draw(img)
    
    # Fonts
    font_path = r'C:\Windows\Fonts\Nirmala.ttc'
    if not os.path.exists(font_path):
        font_path = r'C:\Windows\Fonts\arialbd.ttf'
        
    try:
        font_badge_main = ImageFont.truetype(font_path, 34, index=0)
        font_badge_sub = ImageFont.truetype(font_path, 20, index=0)
        font_line1 = ImageFont.truetype(font_path, 62, index=0)
        font_line2 = ImageFont.truetype(font_path, 60, index=0)
        font_sub = ImageFont.truetype(font_path, 32, index=0)
    except Exception:
        font_badge_main = ImageFont.truetype(font_path, 34)
        font_badge_sub = ImageFont.truetype(font_path, 20)
        font_line1 = ImageFont.truetype(font_path, 62)
        font_line2 = ImageFont.truetype(font_path, 60)
        font_sub = ImageFont.truetype(font_path, 32)
        
    # Draw Top-Left Yellow Badge (Iconic CANEUP NEWS style)
    badge_x, badge_y = 35, 30
    badge_w, badge_h = 240, 105
    
    # Badge shadow
    draw.rounded_rectangle([badge_x + 4, badge_y + 4, badge_x + badge_w + 4, badge_y + badge_h + 4], radius=16, fill=(0, 0, 0, 160))
    # Badge yellow body
    draw.rounded_rectangle([badge_x, badge_y, badge_x + badge_w, badge_y + badge_h], radius=16, fill=(255, 215, 0), outline=(255, 255, 255), width=3)
    
    # Red stripe inside badge
    draw.rectangle([badge_x + 15, badge_y + 45, badge_x + badge_w - 15, badge_y + 88], fill=(220, 38, 38))
    
    # Text in badge
    draw.text((badge_x + 30, badge_y + 6), "CANEUP", font=font_badge_main, fill=(15, 23, 42))
    draw.text((badge_x + 72, badge_y + 50), "NEWS", font=font_badge_main, fill=(255, 255, 255))
    
    # Helper to draw 3D text with thick black outline & shadow
    def draw_3d_text(xy, text, font, fill_color, stroke_color=(0, 0, 0), stroke_width=6, shadow_offset=(4, 5)):
        x, y = xy
        # Shadow
        draw.text((x + shadow_offset[0], y + shadow_offset[1]), text, font=font, fill=(0, 0, 0), stroke_width=stroke_width + 2, stroke_fill=(0, 0, 0))
        # Stroke & fill
        draw.text((x, y), text, font=font, fill=fill_color, stroke_width=stroke_width, stroke_fill=stroke_color)

    # Line 1: White 3D Bold Text
    text1 = "कच्ची चीनी आयात IGST"
    # Center text horizontally
    bbox1 = font_line1.getbbox(text1)
    text1_w = bbox1[2] - bbox1[0]
    x1 = (1200 - text1_w) // 2
    y1 = 405
    draw_3d_text((x1, y1), text1, font_line1, fill_color=(255, 255, 255), stroke_color=(15, 23, 42), stroke_width=7, shadow_offset=(5, 6))
    
    # Line 2: Vibrant Yellow 3D Bold Text
    text2 = "10 लाख टन TRQ पर बड़ा फैसला"
    bbox2 = font_line2.getbbox(text2)
    text2_w = bbox2[2] - bbox2[0]
    x2 = (1200 - text2_w) // 2
    y2 = 490
    draw_3d_text((x2, y2), text2, font_line2, fill_color=(255, 220, 40), stroke_color=(15, 23, 42), stroke_width=7, shadow_offset=(5, 6))
    
    # Line 3: Bottom subtext strip
    text3 = "CBIC ने जारी किए नए दिशा-निर्देश | CaneUp"
    bbox3 = font_sub.getbbox(text3)
    text3_w = bbox3[2] - bbox3[0]
    x3 = (1200 - text3_w) // 2
    y3 = 585
    draw_3d_text((x3, y3), text3, font_sub, fill_color=(240, 253, 244), stroke_color=(0, 0, 0), stroke_width=5, shadow_offset=(3, 4))
    
    # Save optimized WebP under 100KB
    quality = 85
    img.save(out_path, 'WEBP', quality=quality, optimize=True)
    kb = os.path.getsize(out_path) / 1024.0
    while kb > 98.0 and quality > 35:
        quality -= 5
        img.save(out_path, 'WEBP', quality=quality, optimize=True)
        kb = os.path.getsize(out_path) / 1024.0

print(f"Successfully generated High-CTR Discover Banner: {out_path} | {kb:.1f} KB")
