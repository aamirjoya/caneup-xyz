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

next10h_urls = [
    'https://caneup.xyz/news/cm-yogi-cane-review-zero-arrears-order-september-20-2026/',
    'https://caneup.xyz/news/cabinet-approves-1500-crore-buffer-stock-subsidy-sugar-mills-2026/',
    'https://caneup.xyz/news/shamli-upper-doab-deposits-45-crore-escrow-account-2026/',
    'https://caneup.xyz/news/upneda-approves-18-new-cbg-plants-sugarcane-pressmud-2026/',
    'https://caneup.xyz/news/icar-iisr-releases-colk-15201-red-rot-resistant-sugarcane-variety-2026/',
    'https://caneup.xyz/news/punjab-sugarcane-board-recommends-410-sap-2026/',
    'https://caneup.xyz/news/pmfby-satellite-survey-heavy-rain-damage-sugarcane-up-2026/',
    'https://caneup.xyz/news/eganna-app-v6-2-update-tractor-live-queue-tracking-2026/',
    'https://caneup.xyz/news/kisan-morcha-24-hour-token-fast-tehsils-5-september-2026/',
    'https://caneup.xyz/news/state-warehousing-corporation-50-fertilizer-buffer-hubs-up-2026/'
]

success = 0
for url in next10h_urls:
    try:
        body = {"url": url, "type": "URL_UPDATED"}
        res = service.urlNotifications().publish(body=body).execute()
        print(f"Success ({res.get('urlNotificationMetadata', {}).get('latestUpdate', {}).get('type', 'OK')}): {url}")
        success += 1
    except Exception as e:
        print(f"Error {url}: {e}")

print(f"\nIndexed {success}/{len(next10h_urls)} Next 10 Hours News URLs successfully via Google Indexing API!")
