import os
import glob
import re

content_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore\content\webstories'
img_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore\static\images\webstories'

# Map webstory to query key
stories = {
    'ganna-satta-pre-calendar-2026-guide.md': 'sugarcane-farmer-mobile',
    'eganna-app-v6-features.md': 'smartphone-technology-farmer',
    'ganna-bhav-600-kisan-maang.md': 'indian-farmer-agriculture',
    'red-rot-monsoon-prevention-tips.md': 'farm-pest-control-spraying',
    'up-sugar-mills-start-date-2026.md': 'sugar-factory-mill',
    'cos-17231-colk-16202-new-varieties.md': 'sugarcane-plantation-green',
    'ganna-ghosna-patra-2026-deadline.md': 'document-writing-farmer',
    'ganna-bakaya-bhugtan-15-percent-byaj.md': 'money-bank-finance-farmer',
    'sharad-kalin-trench-buwai-tips.md': 'tractor-farming-mustard-field',
    'caneup-online-grievance-complaint.md': 'office-customer-service-phone'
}

for md_file, query_key in stories.items():
    md_path = os.path.join(content_dir, md_file)
    if not os.path.exists(md_path):
        continue
        
    # Find matching pexels images
    imgs = sorted(glob.glob(os.path.join(img_dir, f"pexels-{query_key}-*.webp")))
    if not imgs:
        imgs = sorted(glob.glob(os.path.join(img_dir, "pexels-*.webp")))
        
    pexels_paths = [f"/images/webstories/{os.path.basename(p)}" for p in imgs]
    
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    img_counter = 0
    in_slides = False
    
    for line in lines:
        if line.strip().startswith('slides:'):
            in_slides = True
            new_lines.append(line)
        elif in_slides and line.strip().startswith('- image:'):
            if img_counter < len(pexels_paths):
                chosen_img = pexels_paths[img_counter]
                img_counter += 1
            else:
                chosen_img = pexels_paths[0] if pexels_paths else "/images/webstories/sugarcane-field.webp"
            new_lines.append(f'  - image: "{chosen_img}"\n')
        elif in_slides and line.strip().startswith('image:'):
            if img_counter < len(pexels_paths):
                chosen_img = pexels_paths[img_counter]
                img_counter += 1
            else:
                chosen_img = pexels_paths[0] if pexels_paths else "/images/webstories/sugarcane-field.webp"
            new_lines.append(f'    image: "{chosen_img}"\n')
        else:
            new_lines.append(line)
            
    with open(md_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
        
    print(f"Updated {md_file} with {img_counter} slide images.")

print("Done updating webstory slides!")
