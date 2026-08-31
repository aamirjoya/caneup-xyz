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
        "l1": "सहारनपुर मंडल में 36 ड्रोन तैनात",
        "l2": "5 मिनट में 1 एकड़ में कीटनाशक स्प्रे!",
        "l3": "जलभराव में बड़ी राहत | शामली व मुजफ्फरनगर में सुविधा",
        "stamp": "हाईटेक ⚡"
    },
    {
        "dst": "sugar-ex-mill-price-drop-30-percent-47-kg-2026.webp",
        "bg": os.path.join(brain_dir, "ws_chini_bhav_cover_1787906314949.jpg"),
        "l1": "चीनी के एक्स-मिल भाव 30% गिरे",
        "l2": "47 रुपये किलो पहुंचे थोक भाव!",
        "l3": "10 लाख टन आयात का असर | खुदरा दाम होंगे कम",
        "stamp": "बाजार भाव ⚡"
    },
    {
        "dst": "up-ganna-bhugtan-1200-crore-release-august-2026.webp",
        "bg": os.path.join(brain_dir, "sugar_mill_payment_1787489145600.jpg"),
        "l1": "1200 करोड़ का गन्ना भुगतान जारी",
        "l2": "राज्य में 97.4% बकाया हुआ चुकता!",
        "l3": "104 मिलों ने किया 100% भुगतान | 15 अक्टूबर से नया सत्र",
        "stamp": "भुगतान रिकॉर्ड ⚡"
    },
    {
        "dst": "ganna-jaivik-keet-niyantran-trichoderma-distribution-2026.webp",
        "bg": os.path.join(brain_dir, "ws_red_rot_1787597358502.jpg"),
        "l1": "जैविक कीट नियंत्रण महा-अभियान",
        "l2": "1.5 लाख किसानों को फ्री बांटे बायो-एजेंट्स!",
        "l3": "ट्राइकोग्रामा कार्ड व ट्राइकोडर्मा से लाल सड़न का खात्मा",
        "stamp": "जैविक खेती ⚡"
    },
    {
        "dst": "ganna-beej-upchar-hot-water-treatment-plant-2026.webp",
        "bg": os.path.join(brain_dir, "ws_cos17231_1787597414786.jpg"),
        "l1": "120 चीनी मिलों में HWT प्लांट अनिवार्य",
        "l2": "52 डिग्री गर्म पानी से बीज शोधन!",
        "l3": "लाल सड़न के बीजाणु होंगे नष्ट | रोगमुक्त शरद बुवाई",
        "stamp": "बीज शोधन ⚡"
    },
    {
        "dst": "haryana-up-ganna-sap-405-demand-comparison-2026.webp",
        "bg": os.path.join(brain_dir, "ws_bhav_600_1787597306153.jpg"),
        "l1": "हरियाणा में गन्ने का भाव ₹405 संभव",
        "l2": "यूपी में ₹400 से ₹600 की मांग तेज!",
        "l3": "लागत ₹340 पार | पेराई सत्र 2026-27 भाव पर फैसला जल्द",
        "stamp": "गन्ना मूल्य ⚡"
    },
    {
        "dst": "ganna-patti-prabandhan-1000-rupaye-anudan-up-2026.webp",
        "bg": os.path.join(brain_dir, "trench_buwai_1787582649543.jpg"),
        "l1": "गन्ने की पत्ती न जलाने पर अनुदान",
        "l2": "1000 रुपये प्रति एकड़ प्रोत्साहन राशि!",
        "l3": "मल्चिंग से बनेगी जैविक खाद | NGT नियमों का पालन",
        "stamp": "पर्यावरण राहत ⚡"
    },
    {
        "dst": "omc-ethanol-tender-950-crore-litres-sugarcane-allocation-2026.webp",
        "bg": os.path.join(brain_dir, "news9_ethanol_expansion_cover_1787948284345.jpg"),
        "l1": "950 करोड़ लीटर एथेनॉल महा-टेंडर",
        "l2": "गन्ने के रस वाले एथेनॉल को प्राथमिकता!",
        "l3": "₹65.61 प्रति लीटर खरीद दर | 10 दिन में मिलों को भुगतान",
        "stamp": "ऊर्जा टेंडर ⚡"
    },
    {
        "dst": "pm-kisan-24th-installment-land-seeding-ekyc-deadline-2026.webp",
        "bg": os.path.join(brain_dir, "ws_pmkisan_cover_1787906167254.jpg"),
        "l1": "PM किसान 24वीं किश्त ई-केवाईसी",
        "l2": "10 सितंबर तक लैंड सीडिंग अनिवार्य!",
        "l3": "अक्टूबर में आएंगे ₹2,000 | pmkisan.gov.in पर जांचें",
        "stamp": "अंतिम तारीख ⚡"
    },
    {
        "dst": "up-cooperative-sugar-mills-modernization-650-crore-fund-2026.webp",
        "bg": os.path.join(brain_dir, "ws_sugar_mills_1787597400680.jpg"),
        "l1": "28 सहकारी चीनी मिलों का कायाकल्प",
        "l2": "650 करोड़ रुपये का रिवॉल्विंग फंड मंजूर!",
        "l3": "ऑटोमेशन व नई मशीनें | 15 अक्टूबर से पहले अपग्रेड",
        "stamp": "आधुनिकीकरण ⚡"
    }
]

font_path = r'C:\Windows\Fonts\Nirmala.ttc'
if not os.path.exists(font_path):
    font_path = r'C:\Windows\Fonts\arialbd.ttf'

try:
    f_badge_main = ImageFont.truetype(font_path, 32, index=0)
    f_stamp = ImageFont.truetype(font_path, 26, index=0)
    f_l1 = ImageFont.truetype(font_path, 52, index=0)
    f_l2 = ImageFont.truetype(font_path, 48, index=0)
    f_sub = ImageFont.truetype(font_path, 28, index=0)
except Exception:
    f_badge_main = ImageFont.truetype(font_path, 32)
    f_stamp = ImageFont.truetype(font_path, 26)
    f_l1 = ImageFont.truetype(font_path, 52)
    f_l2 = ImageFont.truetype(font_path, 48)
    f_sub = ImageFont.truetype(font_path, 28)

for idx, spec in enumerate(banners_spec, 1):
    dst_webp_path = os.path.join(img_dir, spec["dst"])
    bg_img_path = spec["bg"]
    
    if not os.path.exists(bg_img_path):
        bg_img_path = os.path.join(brain_dir, "ws_sugar_mills_1787597400680.jpg")
        
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
        
        # Create solid dark container plate for maximum text contrast
        overlay = Image.new('RGBA', (1200, 675), (0, 0, 0, 0))
        draw_ov = ImageDraw.Draw(overlay)
        
        # Top gradient for badge clarity
        for y in range(0, 130):
            a = int(160 * (1.0 - y / 130.0))
            draw_ov.line([(0, y), (1200, y)], fill=(0, 0, 0, a))
            
        # Bottom solid container plate (y=300 to 675)
        for y in range(300, 675):
            if y < 355:
                a = int(242 * ((y - 300) / 55.0))
            else:
                a = 248
            draw_ov.line([(0, y), (1200, y)], fill=(7, 11, 22, a))
            
        # Gold accent line on top of text container
        draw_ov.line([(40, 350), (1160, 350)], fill=(245, 158, 11, 235), width=3)
        
        img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
        draw = ImageDraw.Draw(img)
        
        # Top-Left Yellow Badge
        bx, by = 35, 25
        bw, bh = 240, 90
        draw.rounded_rectangle([bx + 4, by + 4, bx + bw + 4, by + bh + 4], radius=12, fill=(0, 0, 0))
        draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=12, fill=(255, 215, 0), outline=(255, 255, 255), width=2)
        draw.rectangle([bx + 10, by + 42, bx + bw - 10, by + 78], fill=(220, 38, 38))
        draw.text((bx + 32, by + 6), "CANEUP", font=f_badge_main, fill=(15, 23, 42))
        draw.text((bx + 72, by + 44), "NEWS", font=f_badge_main, fill=(255, 255, 255))
        
        # Top-Right Stamp
        sx, sy = 940, 25
        sw, sh = 225, 55
        draw.rounded_rectangle([sx + 3, sy + 3, sx + sw + 3, sy + sh + 3], radius=28, fill=(0, 0, 0))
        draw.rounded_rectangle([sx, sy, sx + sw, sy + sh], radius=28, fill=(220, 38, 38), outline=(255, 255, 255), width=2)
        draw.text((sx + 36, sy + 10), spec["stamp"], font=f_stamp, fill=(255, 255, 255))
        
        def render_crystal_text(xy, text, font, fill_color, stroke_color=(0, 0, 0), stroke_w=2, shadow_offset=(3, 3)):
            x, y = xy
            draw.text((x + shadow_offset[0], y + shadow_offset[1]), text, font=font, fill=(0, 0, 0), stroke_width=stroke_w + 1, stroke_fill=(0, 0, 0))
            draw.text((x, y), text, font=font, fill=fill_color, stroke_width=stroke_w, stroke_fill=stroke_color)

        # Line 1 (White Ultra Crisp Text)
        bb1 = f_l1.getbbox(spec["l1"])
        t1_w = bb1[2] - bb1[0]
        x1 = (1200 - t1_w) // 2
        y1 = 375
        render_crystal_text((x1, y1), spec["l1"], f_l1, fill_color=(255, 255, 255), stroke_color=(5, 10, 20), stroke_w=2, shadow_offset=(3, 4))
        
        # Line 2 (Vibrant Red Plate with Golden Text)
        bb2 = f_l2.getbbox(spec["l2"])
        t2_w = bb2[2] - bb2[0]
        x2 = (1200 - t2_w) // 2
        y2 = 470
        
        rx1, ry1 = x2 - 22, y2 - 4
        rx2, ry2 = x2 + t2_w + 22, y2 + 66
        draw.rounded_rectangle([rx1 + 3, ry1 + 3, rx2 + 3, ry2 + 3], radius=10, fill=(0, 0, 0))
        draw.rounded_rectangle([rx1, ry1, rx2, ry2], radius=10, fill=(220, 38, 38), outline=(255, 215, 0), width=2)
        render_crystal_text((x2, y2), spec["l2"], f_l2, fill_color=(255, 240, 130), stroke_color=(40, 10, 10), stroke_w=2, shadow_offset=(2, 3))
        
        # Line 3 (Clean Cyan Subtext)
        bb3 = f_sub.getbbox(spec["l3"])
        t3_w = bb3[2] - bb3[0]
        x3 = (1200 - t3_w) // 2
        y3 = 585
        render_crystal_text((x3, y3), spec["l3"], f_sub, fill_color=(186, 230, 253), stroke_color=(0, 0, 0), stroke_w=2, shadow_offset=(2, 2))
        
        # Save optimized WebP strictly under 98KB
        quality = 85
        img.save(dst_webp_path, 'WEBP', quality=quality, optimize=True)
        kb = os.path.getsize(dst_webp_path) / 1024.0
        while kb > 98.0 and quality > 35:
            quality -= 5
            img.save(dst_webp_path, 'WEBP', quality=quality, optimize=True)
            kb = os.path.getsize(dst_webp_path) / 1024.0
            
    print(f"[{idx}/10] Regenerated Crystal-Clear Banner: {spec['dst']} | {kb:.1f} KB")

print("\nSuccessfully regenerated all 10 August 31 Featured Banners with crystal clear, perfectly legible typography!")
