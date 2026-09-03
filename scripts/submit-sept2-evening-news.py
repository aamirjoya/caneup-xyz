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

evening_urls = [
    'https://caneup.xyz/news/up-ganna-satta-campaign-day-2-36000-objections-resolved-2026/',
    'https://caneup.xyz/news/mandi-samiti-inspections-sugar-stock-limit-2000-quintals-2026/',
    'https://caneup.xyz/news/shamli-sugar-mills-final-clearance-order-september-10-2026/',
    'https://caneup.xyz/news/western-up-rain-impact-red-rot-prevention-advisory-2026/',
    'https://caneup.xyz/news/autumn-sugarcane-seed-booking-opens-co15023-cos17231-2026/',
    'https://caneup.xyz/news/uperc-reviews-sugar-mill-green-cogeneration-tariff-2026/',
    'https://caneup.xyz/news/bku-village-panchayats-8-september-muzaffarnagar-mahapanchayat-2026/',
    'https://caneup.xyz/news/haryana-ministerial-panel-clears-405-ganna-sap-2026/',
    'https://caneup.xyz/news/drone-spraying-booking-surge-12000-acres-meerut-moradabad-2026/',
    'https://caneup.xyz/news/up-cooperative-banks-disburse-140-crore-kcc-loans-day-2-2026/'
]

success = 0
for url in evening_urls:
    try:
        body = {"url": url, "type": "URL_UPDATED"}
        res = service.urlNotifications().publish(body=body).execute()
        print(f"Success ({res.get('urlNotificationMetadata', {}).get('latestUpdate', {}).get('type', 'OK')}): {url}")
        success += 1
    except Exception as e:
        print(f"Error {url}: {e}")

print(f"\nIndexed {success}/{len(evening_urls)} September 2 Evening News URLs successfully via Google Indexing API!")
