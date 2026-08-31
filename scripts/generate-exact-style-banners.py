import os
import sys
from PIL import Image, ImageDraw, ImageFont

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
img_dir = os.path.join(base_dir, 'static', 'images', 'news')
brain_dir = r'C:\Users\caneu\.gemini\antigravity\brain\f0566670-25ee-4739-bb10-e53286d68160'

banners_spec = [
    {
        "dst": "saharanpur-mandal-36-drones-ganna-spraying-2026.webp",
        "bg": os.path.join(brain_dir, "trending_farming_1787488920538.jpg"),
        "l1": "सहारनपुर में 36 ड्रोन से छिड़काव",
        "l2": "5 मिनट में 1 एकड़ में स्प्रे | CaneUp"
    },
    {
        "dst": "sugar-ex-mill-price-drop-30-percent-47-kg-2026.webp",
        "bg": os.path.join(brain_dir, "ws_chini_bhav_cover_1787906314949.jpg"),
        "l1": "चीनी के एक्स-मिल भाव 30% गिरे",
        "l2": "47 रुपये किलो पहुंचे थोक दाम | CaneUp"
    },
    {
        "dst": "up-ganna-bhugtan-1200-crore-release-august-2026.webp",
        "bg": os.path.join(brain_dir, "sugar_mill_payment_1787489145600.jpg"),
        "l1": "1200 करोड़ गन्ना भुगतान जारी",
        "l2": "राज्य में 97.4% बकाया चुकता | CaneUp"
    },
    {
        "dst": "ganna-jaivik-keet-niyantran-trichoderma-distribution-2026.webp",
        "bg": os.path.join(brain_dir, "ws_red_rot_1787597358502.jpg"),
        "l1": "जैविक कीट नियंत्रण महा-अभियान",
        "l2": "1.5 लाख किसानों को फ्री किट | CaneUp"
    },
    {
        "dst": "ganna-beej-upchar-hot-water-treatment-plant-2026.webp",
        "bg": os.path.join(brain_dir, "ws_cos17231_1787597414786.jpg"),
        "l1": "गर्म पानी से गन्ना बीज शोधन",
        "l2": "120 चीनी मिलों में HWT अनिवार्य | CaneUp"
    },
    {
        "dst": "haryana-up-ganna-sap-405-demand-comparison-2026.webp",
        "bg": os.path.join(brain_dir, "ws_bhav_600_1787597306153.jpg"),
        "l1": "हरियाणा में गन्ने का भाव ₹405",
        "l2": "यूपी में ₹400-600 की मांग तेज | CaneUp"
    },
    {
        "dst": "ganna-patti-prabandhan-1000-rupaye-anudan-up-2026.webp",
        "bg": os.path.join(brain_dir, "trench_buwai_1787582649543.jpg"),
        "l1": "गन्ने की पत्ती न जलाने पर अनुदान",
        "l2": "₹1000 प्रति एकड़ प्रोत्साहन राशि | CaneUp"
    },
    {
        "dst": "omc-ethanol-tender-950-crore-litres-sugarcane-allocation-2026.webp",
        "bg": os.path.join(brain_dir, "news9_ethanol_expansion_cover_1787948284345.jpg"),
        "l1": "950 करोड़ लीटर एथेनॉल टेंडर",
        "l2": "गन्ने के रस को सर्वोच्च आवंटन | CaneUp"
    },
    {
        "dst": "pm-kisan-24th-installment-land-seeding-ekyc-deadline-2026.webp",
        "bg": os.path.join(brain_dir, "ws_pmkisan_cover_1787906167254.jpg"),
        "l1": "PM किसान 24वीं किश्त ई-KYC",
        "l2": "10 सितंबर अंतिम तारीख | CaneUp"
    },
    {
        "dst": "up-cooperative-sugar-mills-modernization-650-crore-fund-2026.webp",
        "bg": os.path.join(brain_dir, "ws_sugar_mills_1787597400680.jpg"),
        "l1": "28 सहकारी मिलों का कायाकल्प",
        "l2": "₹650 करोड़ का फंड मंजूर | CaneUp"
    }
]

w, h = 1200, 675
font_devanagari = r'C:\Windows\Fonts\Nirmala.ttc'
if not os.path.exists(font_devanagari):
    font_devanagari = r'C:\Windows\Fonts\arialbd.ttf'

for idx, spec in enumerate(banners_spec, 1):
    dst_path = os.path.join(img_dir, spec["dst"])
    bg_img_path = spec["bg"]
    
    if not os.path.exists(bg_img_path):
        bg_img_path = os.path.join(brain_dir, "ws_sugar_mills_1787597400680.jpg")
        
    with Image.open(bg_img_path) as img:
        img = img.convert('RGB')
        src_w, src_h = img.size
        target_ratio = w / h
        src_ratio = src_w / src_h
        
        if src_ratio > target_ratio:
            new_w = int(src_h * target_ratio)
            left = (src_w - new_w) // 2
            img = img.crop((left, 0, left + new_w, src_h))
        else:
            new_h = int(src_w / target_ratio)
            top = (src_h - new_h) // 2
            img = img.crop((0, top, src_w, top + new_h))
            
        img = img.resize((w, h), Image.Resampling.LANCZOS)
        
        # Create overlay for top-left red glow and bottom solid black plate
        overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        ov_draw = ImageDraw.Draw(overlay)
        
        # Top-left red glow
        for r in range(380, 0, -6):
            alpha = int(185 * (1.0 - r / 380.0))
            ov_draw.ellipse([-50, -50, r, r], fill=(220, 20, 20, alpha))
            
        # Bottom solid black container (smooth transition from 310 to 400, then pure black to bottom)
        for y in range(310, h):
            if y < 400:
                alpha = int(255 * ((y - 310) / 90.0))
            else:
                alpha = 255
            ov_draw.line([(0, y), (w, y)], fill=(0, 0, 0, alpha))
            
        img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
        draw = ImageDraw.Draw(img)
        
        # Draw Top-Left Yellow Triangle Shield Badge
        badge_poly = [(20, 115), (340, 48), (195, 325)]
        draw.polygon(badge_poly, fill=(255, 230, 0), outline=(255, 255, 255), width=7)
        
        # Text on badge (Rotated)
        txt_layer = Image.new('RGBA', (320, 220), (0, 0, 0, 0))
        t_draw = ImageDraw.Draw(txt_layer)
        f_caneup = ImageFont.truetype(r'C:\Windows\Fonts\impact.ttf', 56)
        f_news = ImageFont.truetype(r'C:\Windows\Fonts\impact.ttf', 66)
        t_draw.text((15, 10), 'CANEUP', font=f_caneup, fill=(10, 10, 10))
        t_draw.text((30, 80), 'NEWS', font=f_news, fill=(10, 10, 10))
        txt_rot = txt_layer.rotate(-11.5, expand=1, resample=Image.Resampling.BICUBIC)
        
        img.paste(txt_rot, (42, 50), txt_rot)
        
        # Draw Outer Yellow Border (6px)
        draw.rectangle([0, 0, w - 1, h - 1], outline=(255, 230, 0), width=6)
        
        # Fonts for Devanagari
        # Dynamically fit Line 1 text
        f_size_l1 = 74
        f_l1 = ImageFont.truetype(font_devanagari, f_size_l1, index=0)
        bb1 = f_l1.getbbox(spec["l1"])
        t1_w = bb1[2] - bb1[0]
        while t1_w > 1100 and f_size_l1 > 54:
            f_size_l1 -= 2
            f_l1 = ImageFont.truetype(font_devanagari, f_size_l1, index=0)
            bb1 = f_l1.getbbox(spec["l1"])
            t1_w = bb1[2] - bb1[0]
            
        x1 = (w - t1_w) // 2
        y1 = 430
        
        # 3D Shadow + Outline for Line 1 (White)
        draw.text((x1 + 4, y1 + 5), spec["l1"], font=f_l1, fill=(0, 0, 0), stroke_width=4, stroke_fill=(0, 0, 0))
        draw.text((x1, y1), spec["l1"], font=f_l1, fill=(255, 255, 255), stroke_width=2, stroke_fill=(20, 20, 20))
        
        # Line 2: Large Bold Yellow Text
        f_size_l2 = 48
        f_l2 = ImageFont.truetype(font_devanagari, f_size_l2, index=0)
        bb2 = f_l2.getbbox(spec["l2"])
        t2_w = bb2[2] - bb2[0]
        while t2_w > 1100 and f_size_l2 > 36:
            f_size_l2 -= 2
            f_l2 = ImageFont.truetype(font_devanagari, f_size_l2, index=0)
            bb2 = f_l2.getbbox(spec["l2"])
            t2_w = bb2[2] - bb2[0]
            
        x2 = (w - t2_w) // 2
        y2 = 548
        
        draw.text((x2 + 3, y2 + 3), spec["l2"], font=f_l2, fill=(0, 0, 0), stroke_width=3, stroke_fill=(0, 0, 0))
        draw.text((x2, y2), spec["l2"], font=f_l2, fill=(255, 235, 59), stroke_width=1, stroke_fill=(30, 30, 0))
        
        # Save optimized WebP strictly under 98KB
        quality = 85
        img.save(dst_path, 'WEBP', quality=quality, optimize=True)
        kb = os.path.getsize(dst_path) / 1024.0
        while kb > 98.0 and quality > 35:
            quality -= 5
            img.save(dst_path, 'WEBP', quality=quality, optimize=True)
            kb = os.path.getsize(dst_path) / 1024.0
            
    print(f"[{idx}/10] Generated Exact Style Match Banner: {spec['dst']} | {kb:.1f} KB")

print("\nSuccessfully generated all 10 banners matching the user's exact uploaded reference design!")
