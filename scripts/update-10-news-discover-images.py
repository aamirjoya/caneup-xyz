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

image_mappings = [
    ("news1_sap_bhav_cover_1787947977342.jpg", "pashchimi-up-ganna-bhav-sap-400-demand-2026.webp"),
    ("news2_perai_start_cover_1787948007062.jpg", "amroha-moradabad-meerut-muzaffarnagar-perai-15-october-2026.webp"),
    ("news3_survey_gps_cover_1787948035006.jpg", "ganna-survey-gps-correction-deadline-september-2026.webp"),
    ("news4_bhugtan_3800cr_cover_1787948066221.jpg", "amroha-moradabad-meerut-ganna-bhugtan-3800-crore-2026.webp"),
    ("news5_red_rot_alert_cover_1787948112904.jpg", "red-rot-top-borer-western-up-september-alert-2026.webp"),
    ("news6_farmer_id_agristack_cover_1787948146713.jpg", "digital-farmer-id-agristack-western-up-kyc-2026.webp"),
    ("news7_drip_subsidy_cover_1787948188598.jpg", "ganna-drip-irrigation-90-percent-subsidy-up-2026.webp"),
    ("news8_harvester_subsidy_cover_1787948234294.jpg", "ganna-harvester-machine-80-percent-subsidy-up-2026.webp"),
    ("news9_ethanol_expansion_cover_1787948284345.jpg", "western-up-sugar-mills-ethanol-expansion-premium-2026.webp")
]

for src_name, dst_name in image_mappings:
    src_path = os.path.join(brain_dir, src_name)
    dst_path = os.path.join(site_news_img_dir, dst_name)
    
    with Image.open(src_path) as img:
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
        
        quality = 85
        img.save(dst_path, 'WEBP', quality=quality, optimize=True)
        kb = os.path.getsize(dst_path) / 1024.0
        while kb > 98.0 and quality > 35:
            quality -= 5
            img.save(dst_path, 'WEBP', quality=quality, optimize=True)
            kb = os.path.getsize(dst_path) / 1024.0
            
    print(f"Processed 1200x675 Discover Image: {dst_name} | {kb:.1f} KB")

# Process News 10 using Pillow Discover Banner
bg_10 = os.path.join(brain_dir, "chandanpur_mill_cover_1787946872076.jpg")
dst_10 = os.path.join(site_news_img_dir, "ganna-parchi-pre-calendar-verification-eganna-2026.webp")

with Image.open(bg_10) as img:
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
    
    font_path = r'C:\Windows\Fonts\Nirmala.ttc'
    if not os.path.exists(font_path):
        font_path = r'C:\Windows\Fonts\arialbd.ttf'
        
    try:
        font_badge = ImageFont.truetype(font_path, 28, index=0)
        font_headline = ImageFont.truetype(font_path, 44, index=0)
        font_sub = ImageFont.truetype(font_path, 34, index=0)
    except Exception:
        font_badge = ImageFont.truetype(font_path, 28)
        font_headline = ImageFont.truetype(font_path, 44)
        font_sub = ImageFont.truetype(font_path, 34)
        
    banner_h = 240
    overlay = Image.new('RGBA', (1200, banner_h), (11, 15, 25, 235))
    img.paste(overlay, (0, 675 - banner_h), overlay)
    
    draw.rectangle([0, 675 - banner_h, 1200, 675 - banner_h + 8], fill=(239, 68, 68))
    draw.rectangle([40, 675 - banner_h + 20, 380, 675 - banner_h + 65], fill=(250, 204, 21))
    draw.text((55, 675 - banner_h + 24), "CANEUP NEWS", font=font_badge, fill=(15, 23, 42))
    
    draw.text((40, 675 - banner_h + 80), "गन्ना पर्ची प्री-कैलेंडर 2026-27 जारी!", font=font_headline, fill=(255, 255, 255))
    draw.text((40, 675 - banner_h + 155), "eGanna App पर 12 पखवाड़ों की पर्ची देखें | CaneUp", font=font_sub, fill=(250, 204, 21))
    
    quality = 85
    img.save(dst_10, 'WEBP', quality=quality, optimize=True)
    kb = os.path.getsize(dst_10) / 1024.0
    while kb > 98.0 and quality > 35:
        quality -= 5
        img.save(dst_10, 'WEBP', quality=quality, optimize=True)
        kb = os.path.getsize(dst_10) / 1024.0
        
print(f"Processed 1200x675 Discover Image 10/10: ganna-parchi-pre-calendar-verification-eganna-2026.webp | {kb:.1f} KB")

print("\nSuccessfully updated all 10 News Featured Images to Custom 1200x675 WebP (<100KB)!")
