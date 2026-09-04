import os
import sys
import glob

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from google.oauth2 import service_account
from googleapiclient.discovery import build

creds_path = os.path.expanduser("~/.config/caneup-google-service-account.json")
if not os.path.exists(creds_path):
    print("Service account file not found at", creds_path)
    sys.exit(0)

SCOPES = ["https://www.googleapis.com/auth/indexing"]
credentials = service_account.Credentials.from_service_account_file(
    creds_path, scopes=SCOPES
)
service = build("indexing", "v3", credentials=credentials)

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
ws_dir = os.path.join(base_dir, 'content', 'webstories')
ws_files = sorted(glob.glob(os.path.join(ws_dir, '*.md')))

urls = []
for f in ws_files:
    slug = os.path.basename(f).replace('.md', '')
    url = f"https://caneup.xyz/webstories/{slug}/"
    urls.append(url)

print(f"Submitting {len(urls)} web stories to Google Indexing API...")

success = 0
for idx, url in enumerate(urls, 1):
    try:
        body = {"url": url, "type": "URL_UPDATED"}
        res = service.urlNotifications().publish(body=body).execute()
        success += 1
        if idx % 15 == 0 or idx == len(urls):
            print(f"[{idx}/{len(urls)}] Success ({res.get('urlNotificationMetadata', {}).get('latestUpdate', {}).get('type', 'OK')}): {url}")
    except Exception as e:
        print(f"Error {url}: {e}")

print(f"\nIndexed {success}/{len(urls)} Web Stories successfully via Google Indexing API!")
