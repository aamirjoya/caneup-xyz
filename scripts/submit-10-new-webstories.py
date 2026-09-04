import os
import sys

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

new_ws_urls = [
    'https://caneup.xyz/webstories/ganna-satta-sanshodhan-15-september-antim-tithi-webstory/',
    'https://caneup.xyz/webstories/high-court-order-ganna-bhugtan-recovery-webstory/',
    'https://caneup.xyz/webstories/ganna-beej-online-booking-co15023-subsidy-webstory/',
    'https://caneup.xyz/webstories/kisan-drone-spray-50-percent-subsidy-booking-webstory/',
    'https://caneup.xyz/webstories/soil-health-card-ganna-kheti-free-test-webstory/',
    'https://caneup.xyz/webstories/ganna-toul-ghattoli-se-bachav-digital-kanta-webstory/',
    'https://caneup.xyz/webstories/ganna-sarso-sah-fasli-kheti-trench-vidhi-webstory/',
    'https://caneup.xyz/webstories/haryana-punjab-ganna-sap-bhav-up-impact-webstory/',
    'https://caneup.xyz/webstories/ganna-ghosna-patra-online-kaise-bhare-30-september-webstory/',
    'https://caneup.xyz/webstories/ganna-pressmud-cbg-biogas-jaivik-khad-webstory/'
]

print(f"Submitting 10 Brand New Web Stories to Google Indexing API...")

success = 0
for idx, url in enumerate(new_ws_urls, 1):
    try:
        body = {"url": url, "type": "URL_UPDATED"}
        res = service.urlNotifications().publish(body=body).execute()
        success += 1
        print(f"[{idx}/10] Success ({res.get('urlNotificationMetadata', {}).get('latestUpdate', {}).get('type', 'OK')}): {url}")
    except Exception as e:
        print(f"Error {url}: {e}")

print(f"\nIndexed {success}/{len(new_ws_urls)} Brand New Web Stories successfully via Google Indexing API!")
