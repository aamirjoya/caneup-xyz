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
    'https://caneup.xyz/news/allahabad-high-court-strict-order-1936-crore-cane-dues-recovery-2026/',
    'https://caneup.xyz/news/simbhaoli-brijnathpur-sugar-mills-100-crore-clearance-order-2026/',
    'https://caneup.xyz/news/sp-chief-akhilesh-yadav-promises-24-hour-cane-payment-2026/',
    'https://caneup.xyz/news/up-ganna-satta-campaign-day-4-68000-objections-resolved-2026/',
    'https://caneup.xyz/news/dfpd-sugar-mills-7-day-quota-liquidation-mandate-2026/',
    'https://caneup.xyz/news/tehsil-24-hour-token-fast-tomorrow-5-september-kisan-morcha-2026/',
    'https://caneup.xyz/news/autumn-sugarcane-mustard-potato-intercropping-guidelines-upcsr-2026/',
    'https://caneup.xyz/news/soil-health-card-camps-cover-45000-farmers-sugar-belt-up-2026/',
    'https://caneup.xyz/news/pre-crushing-digital-weighbridge-stamping-completed-800-centers-2026/',
    'https://caneup.xyz/news/kolkata-transit-sugar-stock-limit-4000-quintals-exemption-2026/'
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

print(f"\nIndexed {success}/{len(morning_urls)} September 4 Morning News URLs successfully via Google Indexing API!")
