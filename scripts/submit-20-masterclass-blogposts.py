#!/usr/bin/env python3
import os
import sys
import time
from google.oauth2 import service_account
from googleapiclient.discovery import build

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

SITE_URL = 'https://caneup.xyz'
CREDENTIAL_PATH = os.path.expanduser(r'~\.config\caneup-google-service-account.json')
SCOPES = ['https://www.googleapis.com/auth/indexing']

slugs = [
    'ganna-parchi-calendar-12-pakhwada-basic-quota-samjhe-2026',
    'eganna-app-v6-2-complete-login-password-reset-guide-2026',
    'ganna-satta-naam-bank-khata-transfer-warasat-guide-2026',
    'ganna-toul-ghattoli-roktham-kisan-kanuni-adhikar-2026',
    'sharadkalin-ganna-buwai-trench-vidhi-600-quintal-formula-2026',
    'ganna-sarso-aalu-matar-sah-fasli-kheti-double-income-2026',
    'ganna-beej-shodhan-bavistin-trichoderma-treatment-guide-2026',
    'soil-health-card-ganna-kheti-dap-urea-potash-dose-calculator-2026',
    'co-0238-replacement-top-5-sugarcane-varieties-comparison-2026',
    'ganne-mein-lal-sadan-red-rot-rog-lakshan-ilaj-fungicide-spray-2026',
    'top-borer-kansua-keet-coragen-drenching-spray-dose-2026',
    'kisan-drone-spray-nano-dap-potash-booking-subsidy-2026',
    'ganna-kisan-kcc-loan-4-percent-byaj-apply-guide-2026',
    'pm-kusum-solar-pump-70-percent-subsidy-up-tubewell-booking-2026',
    'up-krishi-yantra-anudan-rotavator-trench-opener-80-subsidy-2026',
    'pmfby-ganna-fasal-bima-claim-barish-jalbhav-compensation-2026',
    'ganna-bhugtan-14-din-niyam-15-percent-byaj-claim-guide-2026',
    'ganna-toul-parchi-kho-jaye-duplicate-parchi-download-2026',
    'ganna-pressmud-maili-se-jaivik-khad-making-formula-2026',
    'ganna-basic-quota-kaise-badhaye-parchi-calculation-rules-2026'
]

urls = [f'{SITE_URL}/posts/{slug}/' for slug in slugs]

def get_service():
    if not os.path.exists(CREDENTIAL_PATH):
        print(f'Credential file not found: {CREDENTIAL_PATH}')
        sys.exit(1)
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIAL_PATH, scopes=SCOPES
    )
    return build('indexing', 'v3', credentials=credentials)

def main():
    service = get_service()
    print('=' * 65)
    print('Submitting 20 Masterclass Blog Posts to Google Indexing API')
    print('=' * 65)
    success = 0
    errors = 0
    for idx, url in enumerate(urls, 1):
        body = {'url': url, 'type': 'URL_UPDATED'}
        try:
            res = service.urlNotifications().publish(body=body).execute()
            print(f'[{idx:02d}/20] OK: {url}')
            success += 1
        except Exception as e:
            print(f'[{idx:02d}/20] ERR: {url} -> {e}')
            errors += 1
        time.sleep(0.5)

    print('=' * 65)
    print(f'Indexing Complete! Success: {success}/20 | Errors: {errors}/20')
    print('=' * 65)

if __name__ == '__main__':
    main()
