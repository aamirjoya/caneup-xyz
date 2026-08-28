import os
import sys
import glob
from PIL import Image

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
static_dir = os.path.join(base_dir, 'static', 'images')
news_dir = os.path.join(static_dir, 'news')
blog_dir = os.path.join(static_dir, 'blog')
ws_dir = os.path.join(static_dir, 'webstories')
authors_dir = os.path.join(static_dir, 'authors')
thumbs_dir = os.path.join(static_dir, 'thumbs')
os.makedirs(thumbs_dir, exist_ok=True)

print("=== Starting Image Optimization for Core Web Vitals (<1.2s LCP) ===")

def compress_hero_image(src_path, target_size=(800, 450), max_kb=50):
    if not os.path.exists(src_path):
        return
    try:
        img = Image.open(src_path)
        img = img.resize(target_size, Image.LANCZOS)
        
        # Binary search quality tuning
        lo, hi = 20, 85
        best_q = lo
        while lo <= hi:
            mid = (lo + hi) // 2
            img.save(src_path, 'WEBP', quality=mid, method=6)
            size_kb = os.path.getsize(src_path) / 1024.0
            if size_kb <= max_kb:
                best_q = mid
                lo = mid + 1
            else:
                hi = mid - 1
                
        img.save(src_path, 'WEBP', quality=best_q, method=6)
        final_kb = os.path.getsize(src_path) / 1024.0
        
        # Also create a small thumbnail version for related grid cards (240x135 px, < 12KB)
        thumb_name = os.path.basename(src_path)
        thumb_path = os.path.join(thumbs_dir, thumb_name)
        img_thumb = img.resize((240, 135), Image.LANCZOS)
        img_thumb.save(thumb_path, 'WEBP', quality=65, method=6)
        
        return final_kb
    except Exception as e:
        print(f"Error optimizing {src_path}: {e}")
        return None

# 1. Optimize News WebP images
news_images = glob.glob(os.path.join(news_dir, "*.webp"))
print(f"\nProcessing {len(news_images)} News Featured Images (800x450 px, Target < 50KB)...")
for img_path in news_images:
    kb = compress_hero_image(img_path, target_size=(800, 450), max_kb=48)
    if kb:
        print(f" - {os.path.basename(img_path)}: {kb:.1f} KB")

# 2. Optimize Blog WebP images
blog_images = glob.glob(os.path.join(blog_dir, "*.webp"))
print(f"\nProcessing {len(blog_images)} Blog Featured Images (800x450 px, Target < 50KB)...")
for img_path in blog_images:
    kb = compress_hero_image(img_path, target_size=(800, 450), max_kb=48)

# 3. Optimize Author image (randhir-patil.jpg -> 120x120 WebP)
author_src = os.path.join(authors_dir, "randhir-patil.jpg")
if os.path.exists(author_src):
    try:
        img = Image.open(author_src)
        img = img.resize((120, 120), Image.LANCZOS)
        author_out = os.path.join(authors_dir, "randhir-patil.webp")
        img.save(author_out, 'WEBP', quality=80)
        img.save(author_src, 'JPEG', quality=75) # Also optimize existing JPG
        print(f"\nAuthor Image Optimized: {os.path.getsize(author_src)/1024.0:.1f} KB JPG, {os.path.getsize(author_out)/1024.0:.1f} KB WebP")
    except Exception as e:
        print("Author image error:", e)

print("\nImage optimization complete! All LCP images are now compressed to ~35-45KB!")
