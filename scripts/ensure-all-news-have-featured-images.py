import os
import glob
import re

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
news_files = glob.glob(os.path.join(base_dir, 'content', 'news', '*.md'))

# List of valid, existing news WebP images (<200KB)
valid_news_images = [
    "/images/news/agristack-farmer-id-2026.webp",
    "/images/news/andhra-drought-crisis-2026.webp",
    "/images/news/balrampur-biopolymer-2026.webp",
    "/images/news/bareilly-parchi-priority-2026.webp",
    "/images/news/bombay-hc-export-ban-2026.webp",
    "/images/news/chini-4000-quintal-2026.webp",
    "/images/news/chini-bhav-august-2026.webp",
    "/images/news/chini-import-10-lmt-2026.webp",
    "/images/news/chini-price-crisis-aug-2026.webp",
    "/images/news/chini-stock-limit-sept-2026.webp",
    "/images/news/digital-agri-farmer-id-2026.webp",
    "/images/news/e20-ethanol-achieved-2026.webp",
    "/images/news/ethanol-revenue-kisan-2026.webp",
    "/images/news/ethanol-vs-chini-2026.webp",
    "/images/news/fasal-bima-opt-out-2026.webp",
    "/images/news/fpo-10000-kisan-2026.webp",
    "/images/news/frp-365-kisan-naraz-2026.webp",
    "/images/news/frp-365-naraz-2026.webp",
    "/images/news/ganna-bhugtan-97-percent-2026.webp",
    "/images/news/ganna-byaj-15-percent-2026.webp",
    "/images/news/ganna-kalyan-yojana-2026.webp",
    "/images/news/ganna-katai-subsidy-2026.webp",
    "/images/news/ganna-rakba-gira-2026.webp",
    "/images/news/ganna-survey-30-august-2026.webp",
    "/images/news/global-sugar-deficit-2026.webp",
    "/images/news/gps-ganna-survey-2026.webp",
    "/images/news/karnataka-sap-bonus-2026.webp",
    "/images/news/lakhimpur-protest-28aug-2026.webp",
    "/images/news/maharashtra-crushing-permit-2026.webp",
    "/images/news/maharashtra-protest-7000-2026.webp",
    "/images/news/monsoon-recovery-ganna-2026.webp",
    "/images/news/nhb-subsidy-ban-neta-2026.webp",
    "/images/news/perai-15-oct-early-2026.webp",
    "/images/news/pm-kisan-24-oct-2026.webp",
    "/images/news/pm-kisan-2030-extension-2026.webp",
    "/images/news/red-rot-alert-sept-2026.webp",
    "/images/news/sahkari-mill-modernization-2026.webp",
    "/images/news/yogi-chini-stock-esma-2026.webp"
]

img_idx = 0
fixed_count = 0

for f in news_files:
    if os.path.basename(f) == '_index.md':
        continue
        
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
        
    m_feat = re.search(r'featured_image:\s*(/[^\s]+)', txt)
    need_fix = False
    
    if not m_feat:
        need_fix = True
    else:
        img_rel = m_feat.group(1).lstrip('/')
        full_path = os.path.join(base_dir, 'static', img_rel.replace('/', os.sep))
        if not os.path.exists(full_path):
            need_fix = True
            
    if need_fix:
        chosen_img = valid_news_images[img_idx % len(valid_news_images)]
        img_idx += 1
        
        lines = txt.split('\n')
        new_lines = []
        has_feat = False
        has_img = False
        
        for line in lines:
            if line.startswith('featured_image:'):
                new_lines.append(f"featured_image: {chosen_img}")
                has_feat = True
            elif line.startswith('image:'):
                new_lines.append(f"image: {chosen_img}")
                has_img = True
            else:
                new_lines.append(line)
                
        if not has_feat:
            # Insert after description or title
            idx_insert = 3
            for i, line in enumerate(new_lines):
                if line.startswith('description:') or line.startswith('date:'):
                    idx_insert = i + 1
            new_lines.insert(idx_insert, f"featured_image: {chosen_img}")
            new_lines.insert(idx_insert + 1, f"image: {chosen_img}")
            
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write('\n'.join(new_lines))
            
        fixed_count += 1
        print(f"Fixed Image: {os.path.basename(f)} -> {chosen_img}")

print(f"\nTotal news files checked: {len(news_files)}")
print(f"Total news files fixed with valid WebP images: {fixed_count}")
