import os
import sys

# Ensure UTF-8
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

webstories_urls = [
    'https://caneup.xyz/webstories/ganna-parchi-calendar-2026-27-kaise-dekhe-webstory/',
    'https://caneup.xyz/webstories/ganna-bhugtan-14-din-niyam-15-percent-byaj-webstory/',
    'https://caneup.xyz/webstories/up-ganna-sap-rate-2026-27-bhav-webstory/',
    'https://caneup.xyz/webstories/eganna-app-v6-download-session-expired-fix-webstory/',
    'https://caneup.xyz/webstories/ganne-mein-lal-sadan-red-rot-top-borer-ilaj-webstory/',
    'https://caneup.xyz/webstories/co-0238-replacement-top-varieties-webstory/',
    'https://caneup.xyz/webstories/sharadkalin-ganna-trench-buwai-sarso-intercropping-webstory/',
    'https://caneup.xyz/webstories/pm-kusum-solar-pump-70-subsidy-up-webstory/',
    'https://caneup.xyz/webstories/kcc-loan-ganna-kisan-4-percent-byaj-webstory/',
    'https://caneup.xyz/webstories/krishi-yantra-bank-80-subsidy-fpo-webstory/'
]

success = 0
for url in webstories_urls:
    try:
        body = {"url": url, "type": "URL_UPDATED"}
        res = service.urlNotifications().publish(body=body).execute()
        print(f"Success ({res.get('urlNotificationMetadata', {}).get('latestUpdate', {}).get('type', 'OK')}): {url}")
        success += 1
    except Exception as e:
        print(f"Error {url}: {e}")

print(f"\nIndexed {success}/{len(webstories_urls)} Web Stories successfully via Google Indexing API!")
