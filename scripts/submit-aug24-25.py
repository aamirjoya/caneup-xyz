import os
import sys
import importlib.util

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
script_path = os.path.join(base_dir, 'scripts', 'google-index.py')
list_path = os.path.join(base_dir, 'scripts', 'aug24_25_urls.txt')

spec = importlib.util.spec_from_file_location('google_index', script_path)
gi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gi)

if os.path.exists(list_path):
    with open(list_path, 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f if line.strip()]

    print(f"Submitting {len(urls)} URLs from 24 and 25 August 2026 to Google Indexing API...\n")
    gi.batch_submit(urls, dry_run=False)
else:
    print(f"URL list file not found: {list_path}")
