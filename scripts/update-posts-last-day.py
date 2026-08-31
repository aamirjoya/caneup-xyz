import os
import sys
import glob
import re
from datetime import datetime, timedelta

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
posts_dir = os.path.join(base_dir, 'content', 'posts')
post_files = sorted(glob.glob(os.path.join(posts_dir, '*.md')))

total_posts = len(post_files)
print(f"Found {total_posts} post articles to update...")

# Start time: 2026-08-30 22:00:00, End time: 2026-08-31 22:10:00 (Last 24 hours)
start_time = datetime(2026, 8, 30, 22, 0, 0)
time_step = timedelta(seconds=(24 * 3600) / max(total_posts, 1))

updated_count = 0

for i, filepath in enumerate(post_files):
    filename = os.path.basename(filepath)
    post_time = start_time + (time_step * i)
    post_iso = post_time.strftime("%Y-%m-%dT%H:%M:%S+05:30")
    lastmod_iso = datetime(2026, 8, 31, 22, 10, 0).strftime("%Y-%m-%dT%H:%M:%S+05:30")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace date and lastmod in frontmatter
    # Regex to match frontmatter date: ... and lastmod: ...
    new_content = content
    
    # 1. Update date
    if re.search(r'^date:\s*.*$', new_content, flags=re.MULTILINE):
        new_content = re.sub(r'^date:\s*.*$', f'date: {post_iso}', new_content, flags=re.MULTILINE)
    else:
        # If no date in frontmatter, insert after title
        new_content = re.sub(r'^(title:\s*.*)$', f'\\1\ndate: {post_iso}', new_content, flags=re.MULTILINE)
        
    # 2. Update lastmod
    if re.search(r'^lastmod:\s*.*$', new_content, flags=re.MULTILINE):
        new_content = re.sub(r'^lastmod:\s*.*$', f'lastmod: {lastmod_iso}', new_content, flags=re.MULTILINE)
    else:
        # Insert lastmod after date
        new_content = re.sub(r'^(date:\s*.*)$', f'\\1\nlastmod: {lastmod_iso}', new_content, flags=re.MULTILINE)
        
    # 3. Update author image extension
    new_content = new_content.replace('/images/authors/randhir-patil.jpg', '/images/authors/randhir-patil.webp')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    updated_count += 1
    if updated_count % 25 == 0 or updated_count == total_posts:
        print(f"[{updated_count}/{total_posts}] Updated: {filename} -> {post_iso}")

print(f"\nSuccessfully updated all {updated_count} post articles to the last 1 day (August 30-31, 2026)!")
