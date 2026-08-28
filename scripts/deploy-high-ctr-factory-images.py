import os
import shutil

brain_dir = r'C:\Users\caneu\.gemini\antigravity\brain\f0566670-25ee-4739-bb10-e53286d68160'
site_blog_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore\static\images\blog'

images_map = {
    'anoopshahr_mill_cover_1787925027223.jpg': 'anoopshahar-sugar-factory-2026.jpg',
    'mazhawali_mill_cover_1787925060612.jpg': 'mazhawali-venus-sugar-factory-2026.jpg',
    'neoli_mill_cover_1787925098796.jpg': 'neoli-sugar-factory-2026.jpg',
    'rajpura_mill_cover_1787925141772.jpg': 'rajpura-sugar-factory-2026.jpg'
}

for src_name, dst_name in images_map.items():
    src_path = os.path.join(brain_dir, src_name)
    dst_path = os.path.join(site_blog_dir, dst_name)
    shutil.copy2(src_path, dst_path)
    print(f"Copied {src_name} -> {dst_name}")

posts_file_map = {
    r'c:\Users\caneu\Downloads\caneup-xyz-restore\content\posts\anoopshahar-sugar-factory-2026.md': '/images/blog/anoopshahar-sugar-factory-2026.jpg',
    r'c:\Users\caneu\Downloads\caneup-xyz-restore\content\posts\mazhawali-venus-sugar-factory-2026.md': '/images/blog/mazhawali-venus-sugar-factory-2026.jpg',
    r'c:\Users\caneu\Downloads\caneup-xyz-restore\content\posts\neoli-sugar-factory-2026.md': '/images/blog/neoli-sugar-factory-2026.jpg',
    r'c:\Users\caneu\Downloads\caneup-xyz-restore\content\posts\rajpura-sugar-factory-2026.md': '/images/blog/rajpura-sugar-factory-2026.jpg'
}

for post_path, img_url in posts_file_map.items():
    with open(post_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace featured_image and image paths
    content = content.replace('featured_image: "/images/blog/anoopshahar-sugar-factory-2026.webp"', f'featured_image: "{img_url}"')
    content = content.replace('image: "/images/blog/anoopshahar-sugar-factory-2026.webp"', f'image: "{img_url}"')
    
    content = content.replace('featured_image: "/images/blog/mazhawali-venus-sugar-factory-2026.webp"', f'featured_image: "{img_url}"')
    content = content.replace('image: "/images/blog/mazhawali-venus-sugar-factory-2026.webp"', f'image: "{img_url}"')
    
    content = content.replace('featured_image: "/images/blog/neoli-sugar-factory-2026.webp"', f'featured_image: "{img_url}"')
    content = content.replace('image: "/images/blog/neoli-sugar-factory-2026.webp"', f'image: "{img_url}"')
    
    content = content.replace('featured_image: "/images/blog/rajpura-sugar-factory-2026.webp"', f'featured_image: "{img_url}"')
    content = content.replace('image: "/images/blog/rajpura-sugar-factory-2026.webp"', f'image: "{img_url}"')

    with open(post_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated frontmatter in {os.path.basename(post_path)}")

print("All High-CTR images deployed and frontmatter updated successfully!")
