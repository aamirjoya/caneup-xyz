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

sept5_urls = [
    'https://caneup.xyz/news/today-56-tehsils-24-hour-kisan-fast-western-up-2026/',
    'https://caneup.xyz/news/up-ganna-satta-correction-day-5-15-september-deadline-2026/',
    'https://caneup.xyz/news/shamli-hapur-bijnor-sugar-mills-1936-crore-high-court-recovery-2026/',
    'https://caneup.xyz/news/eganna-app-v6-2-live-parchi-satta-tracking-guide-2026/',
    'https://caneup.xyz/news/ganna-ghosna-patra-online-declaration-30-september-deadline-2026/',
    'https://caneup.xyz/news/co15023-colk15201-certified-seed-booking-50-rupees-subsidy-2026/',
    'https://caneup.xyz/news/800-weighbridge-digital-sealing-farmer-vigilance-committee-2026/',
    'https://caneup.xyz/news/autumn-trench-sugarcane-pusa-mustard-intercropping-40000-profit-2026/',
    'https://caneup.xyz/news/50-buffer-dap-fertilizer-hubs-cooperative-dispatch-up-2026/',
    'https://caneup.xyz/news/8-september-muzaffarnagar-gic-ground-mahapanchayat-preparations-2026/'
]

print("Submitting 10 September 5 Morning News Articles to Google Indexing API...")

success = 0
for idx, url in enumerate(sept5_urls, 1):
    try:
        body = {"url": url, "type": "URL_UPDATED"}
        res = service.urlNotifications().publish(body=body).execute()
        success += 1
        print(f"[{idx}/10] Success ({res.get('urlNotificationMetadata', {}).get('latestUpdate', {}).get('type', 'OK')}): {url}")
    except Exception as e:
        print(f"Error {url}: {e}")

print(f"\nIndexed {success}/{len(sept5_urls)} September 5 Morning News URLs successfully via Google Indexing API!")
