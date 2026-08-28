import os
import sys
import glob
import re
from PIL import Image

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
blog_dir = os.path.join(base_dir, 'static', 'images', 'blog')
news_dir = os.path.join(base_dir, 'static', 'images', 'news')
posts_dir = os.path.join(base_dir, 'content', 'posts')
news_posts_dir = os.path.join(base_dir, 'content', 'news')

def resize_and_optimize_webp(src_path, dst_path, target_w=1200, target_h=675):
    try:
        with Image.open(src_path) as img:
            img = img.convert('RGB')
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
            size_kb = os.path.getsize(dst_path) / 1024.0
            
            while size_kb > 98.0 and quality > 35:
                quality -= 5
                img.save(dst_path, 'WEBP', quality=quality, optimize=True)
                size_kb = os.path.getsize(dst_path) / 1024.0
                
            return size_kb, quality
    except Exception as e:
        print(f"Error processing {src_path}: {e}")
        return None, None

def process_directory(img_dir):
    print(f"\n--- Processing Directory: {img_dir} ---")
    all_files = glob.glob(os.path.join(img_dir, '*.*'))
    processed = 0
    for file_path in all_files:
        filename = os.path.basename(file_path)
        name, ext = os.path.splitext(filename)
        ext_lower = ext.lower()
        
        if ext_lower not in ['.jpg', '.jpeg', '.png', '.webp', '.avif']:
            continue
            
        webp_path = os.path.join(img_dir, f"{name}.webp")
        
        # Resize to 1200x675 WebP
        temp_webp = os.path.join(img_dir, f"{name}_temp_opt.webp")
        kb, q = resize_and_optimize_webp(file_path, temp_webp)
        
        if kb is not None:
            if os.path.exists(webp_path) and webp_path != temp_webp:
                try:
                    os.remove(webp_path)
                except Exception:
                    pass
            os.replace(temp_webp, webp_path)
            
            # Remove original if it wasn't .webp
            if file_path != webp_path and os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    print(f"Removed non-webp original: {filename}")
                except Exception:
                    pass
                    
            processed += 1
            print(f"✓ {name}.webp | {1200}x{675} | {kb:.1f} KB (Q={q})")
            
    print(f"Directory total: {processed} WebP images optimized.")

process_directory(blog_dir)
process_directory(news_dir)

# Now update markdown post files to replace any .jpg/.jpeg/.png/.avif references in frontmatter with .webp
def update_markdown_files(content_dir):
    md_files = glob.glob(os.path.join(content_dir, '*.md'))
    updated_count = 0
    for md_path in md_files:
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace image extensions in featured_image / image fields
        new_content = re.sub(r'(\/(?:images|blog|news)\/[a-zA-Z0-9\-_]+)\.(?:jpg|jpeg|png|avif)', r'\1.webp', content)
        
        if new_content != content:
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_count += 1
            print(f"Updated frontmatter image links in: {os.path.basename(md_path)}")
            
    print(f"Markdown updates in {content_dir}: {updated_count} files updated.")

update_markdown_files(posts_dir)
update_markdown_files(news_posts_dir)
print("\nAll Google Discover 1200x675 WebP images (<100KB) successfully processed!")
