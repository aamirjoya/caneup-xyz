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
    # check in project root or current dir
    print("Service account file not found at", creds_path)
    sys.exit(0)

SCOPES = ["https://www.googleapis.com/auth/indexing"]
credentials = service_account.Credentials.from_service_account_file(
    creds_path, scopes=SCOPES
)
service = build("indexing", "v3", credentials=credentials)

urls = [
    'https://caneup.xyz/posts/ganna-parchi-calendar-2026-27-online-check-step-by-step/',
    'https://caneup.xyz/posts/ganna-bhugtan-status-check-online-14-din-niyam-2026/',
    'https://caneup.xyz/posts/up-ganna-sap-rate-2026-27-bhav-suchi-tulna/',
    'https://caneup.xyz/posts/eganna-app-download-latest-version-login-problem-solution-2026/',
    'https://caneup.xyz/posts/ganne-mein-lal-sadan-red-rot-rog-ka-pakka-ilaj-2026/',
    'https://caneup.xyz/posts/co-0238-replacement-top-5-ganna-kismen-2026/',
    'https://caneup.xyz/posts/sharadkalin-ganna-trench-buwai-sarso-aalu-intercropping-guide-2026/',
    'https://caneup.xyz/posts/pm-kusum-yojana-up-solar-pump-70-percent-subsidy-online-apply-2026/',
    'https://caneup.xyz/posts/kisan-credit-card-kcc-ganna-kisan-3-lakh-loan-4-percent-2026/',
    'https://caneup.xyz/posts/krishi-yantra-anudan-fpo-farm-machinery-bank-80-percent-subsidy-2026/'
]

success = 0
for url in urls:
    try:
        body = {"url": url, "type": "URL_UPDATED"}
        res = service.urlNotifications().publish(body=body).execute()
        print(f"Success ({res.get('urlNotificationMetadata', {}).get('latestUpdate', {}).get('type', 'OK')}): {url}")
        success += 1
    except Exception as e:
        print(f"Error {url}: {e}")

print(f"\nIndexed {success}/{len(urls)} URLs successfully via Google Indexing API!")
