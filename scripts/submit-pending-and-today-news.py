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

# 1. September 3 Next 10h News (Pending Indexing)
pending_sept3_urls = [
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

# 2. September 5 Today Morning News
today_sept5_urls = [
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

all_urls = list(dict.fromkeys(pending_sept3_urls + today_sept5_urls))

print(f"Submitting {len(all_urls)} URLs to Google Indexing API...\n")

success = 0
for idx, url in enumerate(all_urls, 1):
    try:
        body = {"url": url, "type": "URL_UPDATED"}
        res = service.urlNotifications().publish(body=body).execute()
        update_type = res.get('urlNotificationMetadata', {}).get('latestUpdate', {}).get('type', 'OK')
        print(f"[{idx}/{len(all_urls)}] Success ({update_type}): {url}")
        success += 1
    except Exception as e:
        print(f"[{idx}/{len(all_urls)}] Error {url}: {e}")

print(f"\nIndexed {success}/{len(all_urls)} News URLs successfully via Google Indexing API!")
