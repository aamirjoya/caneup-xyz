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

# Base image candidate
bg_path = os.path.join(r'C:\Users\caneu\.gemini\antigravity\brain\f0566670-25ee-4739-bb10-e53286d68160', 'news9_ethanol_expansion_cover_1787948284345.jpg')
if not os.path.exists(bg_path):
    bg_path = os.path.join(base_dir, 'static', 'images', 'news', 'chini-import-10-lmt-2026.webp')

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
    
    # Layer 1: Enhanced Vignette & Bottom Dark Plate for dramatic contrast
    overlay = Image.new('RGBA', (1200, 675), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    
    # Smooth rich gradient from y=300 to 675
    for y in range(280, 675):
        alpha = int(245 * ((y - 280) / 395.0) ** 1.2)
        ov_draw.line([(0, y), (1200, y)], fill=(8, 12, 22, alpha))
        
    # Top subtle dark gradient so top badges pop
    for y in range(0, 140):
        alpha = int(140 * ((140 - y) / 140.0))
        ov_draw.line([(0, y), (1200, y)], fill=(0, 0, 0, alpha))
        
    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    draw = ImageDraw.Draw(img)
    
    # Fonts
    font_path = r'C:\Windows\Fonts\Nirmala.ttc'
    if not os.path.exists(font_path):
        font_path = r'C:\Windows\Fonts\arialbd.ttf'
        
    try:
        font_badge_main = ImageFont.truetype(font_path, 34, index=0)
        font_badge_sub = ImageFont.truetype(font_path, 22, index=0)
        font_stamp = ImageFont.truetype(font_path, 28, index=0)
        font_line1 = ImageFont.truetype(font_path, 66, index=0)
        font_line2 = ImageFont.truetype(font_path, 64, index=0)
        font_sub = ImageFont.truetype(font_path, 32, index=0)
    except Exception:
        font_badge_main = ImageFont.truetype(font_path, 34)
        font_badge_sub = ImageFont.truetype(font_path, 22)
        font_stamp = ImageFont.truetype(font_path, 28)
        font_line1 = ImageFont.truetype(font_path, 66)
        font_line2 = ImageFont.truetype(font_path, 64)
        font_sub = ImageFont.truetype(font_path, 32)
        
    # 1. Top-Left Iconic Yellow Shield/Badge (CANEUP NEWS)
    bx, by = 35, 25
    bw, bh = 250, 100
    # Shadow
    draw.rounded_rectangle([bx + 5, by + 5, bx + bw + 5, by + bh + 5], radius=14, fill=(0, 0, 0))
    # Yellow body
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=14, fill=(255, 215, 0), outline=(255, 255, 255), width=3)
    # Red stripe inside
    draw.rectangle([bx + 12, by + 45, bx + bw - 12, by + 86], fill=(220, 38, 38))
    # Text
    draw.text((bx + 35, by + 6), "CANEUP", font=font_badge_main, fill=(15, 23, 42))
    draw.text((bx + 76, by + 48), "NEWS", font=font_badge_main, fill=(255, 255, 255))
    
    # 2. Top-Right High-CTR Stamp (बड़ा फैसला)
    sx, sy = 940, 25
    sw, sh = 225, 60
    draw.rounded_rectangle([sx + 4, sy + 4, sx + sw + 4, sy + sh + 4], radius=30, fill=(0, 0, 0))
    draw.rounded_rectangle([sx, sy, sx + sw, sy + sh], radius=30, fill=(220, 38, 38), outline=(255, 255, 255), width=2)
    draw.text((sx + 36, sy + 10), "बड़ा फैसला ⚡", font=font_stamp, fill=(255, 255, 255))
    
    # Helper to draw 3D text with thick multi-pass outline & shadow
    def draw_ultra_3d(xy, text, font, fill_color, stroke_color=(10, 15, 25), stroke_width=8, shadow_offset=(5, 6)):
        x, y = xy
        # Deep drop shadow
        draw.text((x + shadow_offset[0], y + shadow_offset[1]), text, font=font, fill=(0, 0, 0), stroke_width=stroke_width + 4, stroke_fill=(0, 0, 0))
        # Stroke & fill
        draw.text((x, y), text, font=font, fill=fill_color, stroke_width=stroke_width, stroke_fill=stroke_color)

    # 3. Line 1: Ultra Large 3D White Text (कच्ची चीनी आयात IGST)
    text1 = "कच्ची चीनी आयात IGST"
    bbox1 = font_line1.getbbox(text1)
    t1_w = bbox1[2] - bbox1[0]
    x1 = (1200 - t1_w) // 2
    y1 = 375
    draw_ultra_3d((x1, y1), text1, font_line1, fill_color=(255, 255, 255), stroke_color=(10, 15, 25), stroke_width=8, shadow_offset=(6, 7))
    
    # 4. Line 2: Red Ribbon Plate with Huge Golden Text (भुगतान प्रक्रिया हुई आसान!)
    text2 = "भुगतान प्रक्रिया हुई आसान!"
    bbox2 = font_line2.getbbox(text2)
    t2_w = bbox2[2] - bbox2[0]
    x2 = (1200 - t2_w) // 2
    y2 = 475
    
    # Red ribbon plate behind Line 2
    rx1 = x2 - 25
    ry1 = y2 - 5
    rx2 = x2 + t2_w + 25
    ry2 = y2 + 82
    draw.rounded_rectangle([rx1 + 4, ry1 + 4, rx2 + 4, ry2 + 4], radius=10, fill=(0, 0, 0))
    draw.rounded_rectangle([rx1, ry1, rx2, ry2], radius=10, fill=(220, 38, 38), outline=(255, 215, 0), width=3)
    
    # Draw Line 2 text in bright gold/yellow
    draw_ultra_3d((x2, y2), text2, font_line2, fill_color=(255, 235, 59), stroke_color=(30, 10, 10), stroke_width=6, shadow_offset=(4, 5))
    
    # 5. Line 3: Bottom Subtext Ribbon (CBIC ने जारी किए नए नियम | 10 लाख टन TRQ)
    text3 = "CBIC ने जारी किए नए नियम | 10 लाख टन TRQ | CaneUp"
    bbox3 = font_sub.getbbox(text3)
    t3_w = bbox3[2] - bbox3[0]
    x3 = (1200 - t3_w) // 2
    y3 = 585
    draw_ultra_3d((x3, y3), text3, font_sub, fill_color=(220, 252, 231), stroke_color=(0, 0, 0), stroke_width=5, shadow_offset=(3, 4))
    
    # Save optimized WebP under 100KB
    quality = 85
    img.save(out_path, 'WEBP', quality=quality, optimize=True)
    kb = os.path.getsize(out_path) / 1024.0
    while kb > 98.0 and quality > 35:
        quality -= 5
        img.save(out_path, 'WEBP', quality=quality, optimize=True)
        kb = os.path.getsize(out_path) / 1024.0

print(f"Successfully generated High-CTR Discover Banner: {out_path} | {kb:.1f} KB")
