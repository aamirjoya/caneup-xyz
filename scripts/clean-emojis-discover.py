import os
import glob
import re

news_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore\content\news'
posts_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore\content\posts'

# List of 30 files created for Aug 25
created_files = [
    os.path.join(news_dir, "digital-agri-review-25-august-2026.md"),
    os.path.join(news_dir, "chini-stock-checking-up-districts-2026.md"),
    os.path.join(posts_dir, "caneup-survey-data-sudhar-last-date-2026.md"),
    os.path.join(news_dir, "maharashtra-ganna-andolan-impact-up-2026.md"),
    os.path.join(posts_dir, "eganna-app-login-session-expired-solution.md"),
    os.path.join(news_dir, "up-weather-monsoon-rain-sugarcane-relief-2026.md"),
    os.path.join(posts_dir, "ganna-basic-quota-calculation-formula-2026.md"),
    os.path.join(news_dir, "harvester-machine-subsidy-lottery-list-2026.md"),
    os.path.join(posts_dir, "streptocycline-spray-dosage-red-rot-2026.md"),
    os.path.join(news_dir, "balrampur-biopolymer-plant-update-2026.md"),
    os.path.join(posts_dir, "cos-17231-ganna-beej-nursery-booking-2026.md"),
    os.path.join(news_dir, "pm-kisan-24th-installment-beneficiary-status-2026.md"),
    os.path.join(posts_dir, "ganna-parchi-fortnight-calendar-explained-2026.md"),
    os.path.join(news_dir, "andhra-drought-relief-package-farmer-demand-2026.md"),
    os.path.join(posts_dir, "ganna-ghosna-patra-khasra-khatauni-error-solution.md"),
    os.path.join(news_dir, "early-crushing-october-15-mills-preparation-2026.md"),
    os.path.join(posts_dir, "ganna-trench-method-4-feet-spacing-secrets.md"),
    os.path.join(news_dir, "10000-fpo-scheme-ganna-kisan-benefits-2026.md"),
    os.path.join(posts_dir, "ganna-bakaya-15-percent-byaj-claim-process.md"),
    os.path.join(news_dir, "nhb-subsidy-politicians-banned-farmers-benefit-2026.md"),
    os.path.join(posts_dir, "ganna-sarson-intercropping-step-by-step-guide.md"),
    os.path.join(news_dir, "e20-ethanol-target-ahead-of-time-2026.md"),
    os.path.join(posts_dir, "eganna-app-se-grower-code-search-kaise-kare.md"),
    os.path.join(news_dir, "red-rot-september-high-alert-up-cane-dept-2026.md"),
    os.path.join(posts_dir, "ganna-kisan-kcc-loan-3-lakh-apply-online.md"),
    os.path.join(news_dir, "ganna-kisan-kalyan-dbt-scheme-update-2026.md"),
    os.path.join(posts_dir, "caneup-grievance-token-track-status-mobile.md"),
    os.path.join(news_dir, "ganna-rakba-decline-maize-paddy-shift-2026.md"),
    os.path.join(posts_dir, "drip-irrigation-ganna-90-percent-subsidy-guide.md"),
    os.path.join(news_dir, "frp-365-kisan-narazgi-up-sap-600-update-2026.md")
]

# Regex pattern for emojis
emoji_pattern = re.compile(
    "[\U00010000-\U0010ffff"  # Supplemental symbols
    "\u2600-\u27BF"            # Miscellaneous symbols
    "\u2300-\u23FF"            # Technical symbols
    "\u2B50\u2B55\u2934\u2935"
    "\u203C\u2049"
    "\u25AA-\u25FE"
    "\u00A9\u00AE\u2122]+", flags=re.UNICODE
)

updated_count = 0

for file_path in created_files:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        
    cleaned_text = emoji_pattern.sub('', text)
    # Clean up double spaces created by emoji removal
    cleaned_text = re.sub(r' +', ' ', cleaned_text)
    cleaned_text = cleaned_text.replace('title: " ', 'title: "').replace('title: "', 'title: "')
    
    if text != cleaned_text:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_text)
        updated_count += 1
        print(f"Cleaned Emojis: {os.path.basename(file_path)}")

print(f"\nTotal files cleaned from emojis/symbols: {updated_count}")
