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

sept1_urls = [
    'https://caneup.xyz/news/sugar-stock-limit-order-effective-1-september-2026/',
    'https://caneup.xyz/news/september-first-fortnight-13-lakh-tonne-sugar-sales-quota-2026/',
    'https://caneup.xyz/news/up-ganna-satta-objection-disposal-campaign-1-15-september-2026/',
    'https://caneup.xyz/news/western-up-sugar-mills-boiler-trial-maintenance-start-2026/',
    'https://caneup.xyz/news/upcsr-september-ganna-potash-zinc-foliar-spray-advisory-2026/',
    'https://caneup.xyz/news/meerut-saharanpur-drone-spraying-50-percent-subsidy-booking-2026/',
    'https://caneup.xyz/news/nbcc-sugarcane-syrup-ethanol-allocation-2026-27-boost/',
    'https://caneup.xyz/news/up-cooperative-banks-10-day-kcc-renewal-camps-september-2026/',
    'https://caneup.xyz/news/bku-muzaffarnagar-kisan-mahapanchayat-450-sap-demand-2026/',
    'https://caneup.xyz/news/haryana-cabinet-ganna-sap-405-quintal-proposal-review-2026/'
]

success = 0
for url in sept1_urls:
    try:
        body = {"url": url, "type": "URL_UPDATED"}
        res = service.urlNotifications().publish(body=body).execute()
        print(f"Success ({res.get('urlNotificationMetadata', {}).get('latestUpdate', {}).get('type', 'OK')}): {url}")
        success += 1
    except Exception as e:
        print(f"Error {url}: {e}")

print(f"\nIndexed {success}/{len(sept1_urls)} September 1 News URLs successfully via Google Indexing API!")
