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

morning_urls = [
    'https://caneup.xyz/news/up-ganna-satta-day-3-52000-objections-settled-muzaffarnagar-top-2026/',
    'https://caneup.xyz/news/wholesale-sugar-prices-fall-50-rupees-stock-limit-impact-2026/',
    'https://caneup.xyz/news/digital-weighbridge-calibration-2800-purchase-centers-up-2026/',
    'https://caneup.xyz/news/bijnor-saharanpur-sugar-mills-boiler-puja-dates-september-2026/',
    'https://caneup.xyz/news/upcsr-post-rain-autumn-sugarcane-field-prep-advisory-2026/',
    'https://caneup.xyz/news/up-cooperative-sugar-mills-600-crore-pre-season-modernization-2026/',
    'https://caneup.xyz/news/muzaffarnagar-kisan-yatra-7-september-bku-mobilization-2026/',
    'https://caneup.xyz/news/haryana-sugarfed-14-mills-ready-25-october-crushing-start-2026/',
    'https://caneup.xyz/news/kisan-drone-fleet-expanded-60-units-western-up-2026/',
    'https://caneup.xyz/news/iffco-kribhco-150-mobile-dap-trucks-sugar-belt-up-2026/'
]

success = 0
for url in morning_urls:
    try:
        body = {"url": url, "type": "URL_UPDATED"}
        res = service.urlNotifications().publish(body=body).execute()
        print(f"Success ({res.get('urlNotificationMetadata', {}).get('latestUpdate', {}).get('type', 'OK')}): {url}")
        success += 1
    except Exception as e:
        print(f"Error {url}: {e}")

print(f"\nIndexed {success}/{len(morning_urls)} September 3 Morning News URLs successfully via Google Indexing API!")
