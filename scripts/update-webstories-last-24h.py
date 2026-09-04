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
ws_dir = os.path.join(base_dir, 'content', 'webstories')
ws_files = sorted(glob.glob(os.path.join(ws_dir, '*.md')))

total_stories = len(ws_files)
print(f"Found {total_stories} web stories to update across last 24 hours...")

# Time window: 2026-09-03 10:00:00 to 2026-09-04 09:35:00 (Last 24 Hours)
start_time = datetime(2026, 9, 3, 10, 0, 0)
time_step = timedelta(seconds=(23.5 * 3600) / max(total_stories - 1, 1))
lastmod_iso = datetime(2026, 9, 4, 9, 35, 0).strftime("%Y-%m-%dT%H:%M:%S+05:30")

updated_count = 0

for i, filepath in enumerate(ws_files):
    filename = os.path.basename(filepath)
    story_time = start_time + (time_step * i)
    story_iso = story_time.strftime("%Y-%m-%dT%H:%M:%S+05:30")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content = content
    
    # 1. Update or insert date
    if re.search(r'^date:\s*.*$', new_content, flags=re.MULTILINE):
        new_content = re.sub(r'^date:\s*.*$', f'date: {story_iso}', new_content, flags=re.MULTILINE)
    else:
        new_content = re.sub(r'^(title:\s*.*)$', f'\\1\ndate: {story_iso}', new_content, flags=re.MULTILINE)
        
    # 2. Update or insert lastmod
    if re.search(r'^lastmod:\s*.*$', new_content, flags=re.MULTILINE):
        new_content = re.sub(r'^lastmod:\s*.*$', f'lastmod: {lastmod_iso}', new_content, flags=re.MULTILINE)
    else:
        new_content = re.sub(r'^(date:\s*.*)$', f'\\1\nlastmod: {lastmod_iso}', new_content, flags=re.MULTILINE)
        
    # 3. Clean any malformed date format
    new_content = re.sub(r'^date:\s*(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\+05:30', r'date: \1T\2+05:30', new_content, flags=re.MULTILINE)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    updated_count += 1
    if updated_count % 15 == 0 or updated_count == total_stories:
        print(f"[{updated_count}/{total_stories}] Updated: {filename} -> Date: {story_iso} | Lastmod: {lastmod_iso}")

print(f"\nSuccessfully updated all {updated_count} web stories to the last 24 hours (3 Sept 10:00 AM to 4 Sept 09:35 AM, 2026)!")
