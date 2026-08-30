import os
import sys
from PIL import Image, ImageDraw, ImageFont

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
brain_dir = r'C:\Users\caneu\.gemini\antigravity\brain\f0566670-25ee-4739-bb10-e53286d68160'
site_news_img_dir = os.path.join(base_dir, 'static', 'images', 'news')

banners_spec = [
    {
        "dst": "lakhimpur-kheri-ganna-bhugtan-byaj-andolan-2026.webp",
        "bg": os.path.join(brain_dir, "ws_lakhimpur_cover_1787905974379.jpg"),
        "line1": "30 साल के बकाया ब्याज पर धरना",
        "line2": "लखीमपुर खीरी में बड़ा किसान आंदोलन!",
        "line3": "15% ब्याज व ₹600/क्विंटल भाव की मांग | CaneUp",
        "stamp": "आंदोलन ⚡"
    },
    {
        "dst": "co-0238-ganna-replacement-5-approved-varieties-2026.webp",
        "bg": os.path.join(brain_dir, "ws_cos17231_1787597414786.jpg"),
        "line1": "गन्ना किस्म Co-0238 की विदाई",
        "line2": "2026-27 में ये 5 किस्में अनिवार्य!",
        "line3": "Co-15023 व CoLk-14201 बीज वितरण | CaneUp",
        "stamp": "कृषि सलाह ⚡"
    },
    {
        "dst": "up-ganna-rakba-47000-hectare-ghata-analysis-2026.webp",
        "bg": os.path.join(base_dir, "static", "images", "news", "ganna-rakba-gira-2026.webp"),
        "line1": "गन्ना रकबा 47,000 हेक्टेयर घटा",
        "line2": "मक्का-धान की ओर मुड़े किसान!",
        "line3": "चीनी उत्पादन 14% कम होने की आशंका | CaneUp",
        "stamp": "ग्राउंड रिपोर्ट ⚡"
    },
    {
        "dst": "up-chini-mil-15-october-crushing-start-3-lakh-crore-payment-2026.webp",
        "bg": os.path.join(brain_dir, "news2_perai_start_cover_1787948007062.jpg"),
        "line1": "15 अक्टूबर से पेराई सत्र शुरू",
        "line2": "99 चीनी मिलों ने चुकाया 100% भुगतान!",
        "line3": "कुल ₹3.25 लाख करोड़ ट्रांसफर | CaneUp",
        "stamp": "पेराई 2026 ⚡"
    },
    {
        "dst": "sugar-msp-hike-demand-38-41-isma-import-policy-2026.webp",
        "bg": os.path.join(brain_dir, "ws_chini_bhav_cover_1787906314949.jpg"),
        "line1": "चीनी MSP ₹31 से ₹41 करने की मांग",
        "line2": "मिलों की दलील vs 10 लाख टन आयात!",
        "line3": "लागत ₹40/kg | सरकार का नया फॉर्मूला | CaneUp",
        "stamp": "पॉलिसी वॉच ⚡"
    },
    {
        "dst": "agristack-digital-farmer-id-ganna-satta-pm-kisan-mandatory-2026.webp",
        "bg": os.path.join(brain_dir, "ws_farmer_id_cover_1787906299935.jpg"),
        "line1": "डिजिटल किसान आईडी अनिवार्य",
        "line2": "बिना e-KYC सट्टा व पर्ची बंद!",
        "line3": "PM किसान 24वीं किश्त व खाद हेतु जरूरी | CaneUp",
        "stamp": "अलर्ट ⚡"
    },
    {
        "dst": "pipraich-western-up-bio-ethanol-production-10-days-payment-2026.webp",
        "bg": os.path.join(brain_dir, "news9_ethanol_expansion_cover_1787948284345.jpg"),
        "line1": "एथेनॉल क्रांति से बदला चीनी उद्योग",
        "line2": "गन्ने के रस से सीधे फ्यूल उत्पादन!",
        "line3": "किसानों को 10 दिन में मिल रहा भुगतान | CaneUp",
        "stamp": "ऊर्जा क्रांति ⚡"
    },
    {
        "dst": "ganna-drip-irrigation-polytray-nursery-90-percent-subsidy-2026.webp",
        "bg": os.path.join(brain_dir, "news7_drip_subsidy_cover_1787948188598.jpg"),
        "line1": "गन्ने की ड्रिप सिंचाई 90% छूट",
        "line2": "पॉली-ट्रे नर्सरी पर भारी अनुदान!",
        "line3": "₹60,000 का सिस्टम मात्र ₹6,000 में | CaneUp",
        "stamp": "सब्सिडी ⚡"
    },
    {
        "dst": "yogi-action-sugar-hoarding-esma-400-tonne-stock-limit-2026.webp",
        "bg": os.path.join(brain_dir, "yogi_sugar_esma_1787564910606.jpg"),
        "line1": "चीनी जमाखोरों पर योगी का एक्शन",
        "line2": "400 टन स्टॉक लिमिट लागू!",
        "line3": "कालाबाजारी पर लगेगा ESMA | 28 LMT स्टॉक सुरक्षित",
        "stamp": "कड़ा एक्शन ⚡"
    },
    {
        "dst": "eganna-app-pre-calendar-2026-27-live-12-fortnights-verification.webp",
        "bg": os.path.join(brain_dir, "ws_satta_precal_1787597283025.jpg"),
        "line1": "eGanna ऐप पर प्री-कैलेंडर जारी",
        "line2": "12 पखवाड़ों की पर्ची करें चेक!",
        "line3": "सट्टा संशोधन 30 सितंबर तक | CaneUp",
        "stamp": "लाइव ⚡"
    }
]

for idx, spec in enumerate(banners_spec, 1):
    dst_webp_path = os.path.join(site_news_img_dir, spec["dst"])
    bg_img_path = spec["bg"]
    
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
        
        # Bottom dark gradient plate for readability
        overlay = Image.new('RGBA', (1200, 675), (0, 0, 0, 0))
        ov_draw = ImageDraw.Draw(overlay)
        
        for y in range(280, 675):
            alpha = int(245 * ((y - 280) / 395.0) ** 1.2)
            ov_draw.line([(0, y), (1200, y)], fill=(8, 12, 22, alpha))
            
        for y in range(0, 140):
            alpha = int(140 * ((140 - y) / 140.0))
            ov_draw.line([(0, y), (1200, y)], fill=(0, 0, 0, alpha))
            
        img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
        draw = ImageDraw.Draw(img)
        
        font_path = r'C:\Windows\Fonts\Nirmala.ttc'
        if not os.path.exists(font_path):
            font_path = r'C:\Windows\Fonts\arialbd.ttf'
            
        try:
            font_badge_main = ImageFont.truetype(font_path, 34, index=0)
            font_stamp = ImageFont.truetype(font_path, 28, index=0)
            font_line1 = ImageFont.truetype(font_path, 64, index=0)
            font_line2 = ImageFont.truetype(font_path, 60, index=0)
            font_sub = ImageFont.truetype(font_path, 32, index=0)
        except Exception:
            font_badge_main = ImageFont.truetype(font_path, 34)
            font_stamp = ImageFont.truetype(font_path, 28)
            font_line1 = ImageFont.truetype(font_path, 64)
            font_line2 = ImageFont.truetype(font_path, 60)
            font_sub = ImageFont.truetype(font_path, 32)
            
        # Top-Left Yellow Badge
        bx, by = 35, 25
        bw, bh = 250, 100
        draw.rounded_rectangle([bx + 5, by + 5, bx + bw + 5, by + bh + 5], radius=14, fill=(0, 0, 0))
        draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=14, fill=(255, 215, 0), outline=(255, 255, 255), width=3)
        draw.rectangle([bx + 12, by + 45, bx + bw - 12, by + 86], fill=(220, 38, 38))
        draw.text((bx + 35, by + 6), "CANEUP", font=font_badge_main, fill=(15, 23, 42))
        draw.text((bx + 76, by + 48), "NEWS", font=font_badge_main, fill=(255, 255, 255))
        
        # Top-Right Stamp
        sx, sy = 940, 25
        sw, sh = 225, 60
        draw.rounded_rectangle([sx + 4, sy + 4, sx + sw + 4, sy + sh + 4], radius=30, fill=(0, 0, 0))
        draw.rounded_rectangle([sx, sy, sx + sw, sy + sh], radius=30, fill=(220, 38, 38), outline=(255, 255, 255), width=2)
        draw.text((sx + 36, sy + 10), spec["stamp"], font=font_stamp, fill=(255, 255, 255))
        
        def draw_ultra_3d(xy, text, font, fill_color, stroke_color=(10, 15, 25), stroke_width=8, shadow_offset=(5, 6)):
            x, y = xy
            draw.text((x + shadow_offset[0], y + shadow_offset[1]), text, font=font, fill=(0, 0, 0), stroke_width=stroke_width + 4, stroke_fill=(0, 0, 0))
            draw.text((x, y), text, font=font, fill=fill_color, stroke_width=stroke_width, stroke_fill=stroke_color)

        # Line 1 (White 3D Text)
        bbox1 = font_line1.getbbox(spec["line1"])
        t1_w = bbox1[2] - bbox1[0]
        x1 = (1200 - t1_w) // 2
        y1 = 375
        draw_ultra_3d((x1, y1), spec["line1"], font_line1, fill_color=(255, 255, 255), stroke_color=(10, 15, 25), stroke_width=8, shadow_offset=(6, 7))
        
        # Line 2 (Red ribbon with Golden 3D Text)
        bbox2 = font_line2.getbbox(spec["line2"])
        t2_w = bbox2[2] - bbox2[0]
        x2 = (1200 - t2_w) // 2
        y2 = 475
        rx1, ry1 = x2 - 25, y2 - 5
        rx2, ry2 = x2 + t2_w + 25, y2 + 80
        draw.rounded_rectangle([rx1 + 4, ry1 + 4, rx2 + 4, ry2 + 4], radius=10, fill=(0, 0, 0))
        draw.rounded_rectangle([rx1, ry1, rx2, ry2], radius=10, fill=(220, 38, 38), outline=(255, 215, 0), width=3)
        draw_ultra_3d((x2, y2), spec["line2"], font_line2, fill_color=(255, 235, 59), stroke_color=(30, 10, 10), stroke_width=6, shadow_offset=(4, 5))
        
        # Line 3 (Bottom Subtext)
        bbox3 = font_sub.getbbox(spec["line3"])
        t3_w = bbox3[2] - bbox3[0]
        x3 = (1200 - t3_w) // 2
        y3 = 585
        draw_ultra_3d((x3, y3), spec["line3"], font_sub, fill_color=(220, 252, 231), stroke_color=(0, 0, 0), stroke_width=5, shadow_offset=(3, 4))
        
        # Save optimized WebP under 100KB
        quality = 85
        img.save(dst_webp_path, 'WEBP', quality=quality, optimize=True)
        kb = os.path.getsize(dst_webp_path) / 1024.0
        while kb > 98.0 and quality > 35:
            quality -= 5
            img.save(dst_webp_path, 'WEBP', quality=quality, optimize=True)
            kb = os.path.getsize(dst_webp_path) / 1024.0
            
    print(f"[{idx}/10] Created Unique Discover Banner: {spec['dst']} (from {os.path.basename(bg_img_path)}) | {kb:.1f} KB")

print("\nSuccessfully updated all 10 Discover Featured Banners with 100% Unique, Custom Topic Backgrounds!")
