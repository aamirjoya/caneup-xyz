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
    'https://caneup.xyz/news/sugar-dealers-stock-limit-halved-2000-quintals-2026/',
    'https://caneup.xyz/news/up-ganna-satta-disposal-day-1-18400-objections-resolved-2026/',
    'https://caneup.xyz/news/shamli-bijnor-sugar-mills-release-280-crore-cane-arrears-2026/',
    'https://caneup.xyz/news/imd-western-up-heavy-rainfall-drainage-advisory-september-2026/',
    'https://caneup.xyz/news/free-soil-health-card-camps-120-sugar-mill-zones-2026/',
    'https://caneup.xyz/news/balrampur-chini-lakhimpur-bioplastic-fmcg-orders-2026/',
    'https://caneup.xyz/news/sugar-industry-demands-ethanol-price-hike-62-50-litre-2026/',
    'https://caneup.xyz/news/punjab-announces-early-crushing-transport-subsidy-2026/',
    'https://caneup.xyz/news/bku-7-day-ultimatum-smart-meters-tubewells-meerut-2026/',
    'https://caneup.xyz/news/ccea-reviews-fertilizer-subsidy-dap-uninterrupted-supply-2026/'
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

print(f"\nIndexed {success}/{len(evening_urls)} September 1 Evening News URLs successfully via Google Indexing API!")
