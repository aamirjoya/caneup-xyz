#!/usr/bin/env python3
"""
CaneUp Google Indexing API Script
----------------------------------
Submits URLs to Google for instant indexing.

Usage:
  python scripts/google-index.py                    # Index all recent pages
  python scripts/google-index.py --all              # Index ALL pages (uses quota!)
  python scripts/google-index.py --url URL          # Index a specific URL
  python scripts/google-index.py --news             # Index only /news/ pages
  python scripts/google-index.py --dry-run          # Show what would be submitted

Quota: 200 requests/day (Google default)
Credential: ~/.config/caneup-google-service-account.json
"""

import json
import sys
import os

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
import time
import argparse
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

# Google API imports
from google.oauth2 import service_account
from googleapiclient.discovery import build

# ── Config ──────────────────────────────────────────────────────────────
SITE_URL = "https://caneup.xyz"
CREDENTIAL_PATH = os.path.expanduser(r"~\.config\caneup-google-service-account.json")
SITEMAP_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "sitemap.xml")
NEWS_SITEMAP_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "news-sitemap.xml")
SCOPES = ["https://www.googleapis.com/auth/indexing"]
DAILY_QUOTA = 200
LOG_FILE = os.path.join(os.path.dirname(__file__), "indexing-log.json")

# ── Auth ────────────────────────────────────────────────────────────────
def get_service():
    """Authenticate and return Indexing API service."""
    if not os.path.exists(CREDENTIAL_PATH):
        print(f"❌ Credential file not found: {CREDENTIAL_PATH}")
        print("   Save your service account JSON there first.")
        sys.exit(1)

    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIAL_PATH, scopes=SCOPES
    )
    service = build("indexing", "v3", credentials=credentials)
    return service

# ── URL Collection ──────────────────────────────────────────────────────
def get_urls_from_sitemap(sitemap_path, filter_section=None, max_age_days=None):
    """Parse sitemap.xml and return list of URLs."""
    if not os.path.exists(sitemap_path):
        print(f"⚠️  Sitemap not found: {sitemap_path}")
        print("   Run 'hugo' first to generate public/ folder.")
        return []

    tree = ET.parse(sitemap_path)
    root = tree.getroot()

    # Handle XML namespace
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = []

    for url_elem in root.findall(".//sm:url", ns):
        loc = url_elem.find("sm:loc", ns)
        lastmod = url_elem.find("sm:lastmod", ns)

        if loc is None:
            continue

        url = loc.text.strip()

        # Filter by section
        if filter_section and f"/{filter_section}/" not in url:
            continue

        # Filter by age
        if max_age_days and lastmod is not None:
            try:
                mod_date = datetime.fromisoformat(lastmod.text.strip().replace("Z", "+00:00"))
                if (datetime.now(mod_date.tzinfo) - mod_date).days > max_age_days:
                    continue
            except (ValueError, TypeError):
                pass

        urls.append(url)

    return urls

# ── Load/Save Log ──────────────────────────────────────────────────────
def load_log():
    """Load indexing log to track what's been submitted."""
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"submitted": {}, "daily_count": 0, "last_date": ""}

def save_log(log):
    """Save indexing log."""
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(log, f, indent=2, ensure_ascii=False)

# ── Submit URL ──────────────────────────────────────────────────────────
def submit_url(service, url, action="URL_UPDATED"):
    """Submit a single URL for indexing."""
    body = {
        "url": url,
        "type": action  # URL_UPDATED or URL_DELETED
    }
    try:
        response = service.urlNotifications().publish(body=body).execute()
        return {
            "success": True,
            "url": url,
            "notifyTime": response.get("urlNotificationMetadata", {}).get("latestUpdate", {}).get("notifyTime", ""),
        }
    except Exception as e:
        error_msg = str(e)
        return {"success": False, "url": url, "error": error_msg}

# ── Batch Submit ────────────────────────────────────────────────────────
def batch_submit(urls, dry_run=False):
    """Submit multiple URLs with quota management."""
    log = load_log()
    today = datetime.now().strftime("%Y-%m-%d")

    # Reset daily counter if new day
    if log["last_date"] != today:
        log["daily_count"] = 0
        log["last_date"] = today

    remaining_quota = DAILY_QUOTA - log["daily_count"]

    if remaining_quota <= 0:
        print(f"❌ Daily quota exhausted ({DAILY_QUOTA}/day). Try again tomorrow.")
        return

    # Filter already submitted today
    new_urls = []
    for url in urls:
        last_submit = log["submitted"].get(url, "")
        if last_submit == today:
            continue  # Already submitted today
        new_urls.append(url)

    if not new_urls:
        print("✅ All URLs already submitted today!")
        return

    # Limit to remaining quota
    submit_list = new_urls[:remaining_quota]

    print(f"\n{'='*60}")
    print(f"  CaneUp Google Indexing API")
    print(f"{'='*60}")
    print(f"  Total URLs found:     {len(urls)}")
    print(f"  Already submitted:    {len(urls) - len(new_urls)}")
    print(f"  To submit now:        {len(submit_list)}")
    print(f"  Remaining quota:      {remaining_quota}/{DAILY_QUOTA}")
    print(f"{'='*60}\n")

    if dry_run:
        print("🔍 DRY RUN — No actual submissions:\n")
        for i, url in enumerate(submit_list, 1):
            print(f"  {i:3d}. {url}")
        print(f"\n  Would submit {len(submit_list)} URLs.")
        return

    service = get_service()
    success_count = 0
    error_count = 0

    for i, url in enumerate(submit_list, 1):
        result = submit_url(service, url)

        if result["success"]:
            success_count += 1
            log["submitted"][url] = today
            log["daily_count"] += 1
            print(f"  ✅ {i:3d}/{len(submit_list)} | {url}")
        else:
            error_count += 1
            error_short = result["error"][:100]
            print(f"  ❌ {i:3d}/{len(submit_list)} | {url}")
            print(f"       Error: {error_short}")
            if "429" in error_short or "Quota" in error_short:
                print("\n⚠️  Google Indexing API Rate Limit / Daily Quota (429) hit. Stopping batch.")
                break

        # Rate limiting: 1 request per 0.5 second
        if i < len(submit_list):
            time.sleep(0.5)

    save_log(log)

    print(f"\n{'='*60}")
    print(f"  ✅ Success: {success_count}")
    print(f"  ❌ Errors:  {error_count}")
    print(f"  📊 Quota used today: {log['daily_count']}/{DAILY_QUOTA}")
    print(f"{'='*60}\n")

# ── Main ────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="CaneUp Google Indexing API")
    parser.add_argument("--all", action="store_true", help="Submit ALL pages from sitemap")
    parser.add_argument("--news", action="store_true", help="Submit only /news/ pages")
    parser.add_argument("--posts", action="store_true", help="Submit only /posts/ pages")
    parser.add_argument("--recent", type=int, default=7, help="Submit pages modified in last N days (default: 7)")
    parser.add_argument("--url", type=str, help="Submit a specific URL")
    parser.add_argument("--dry-run", action="store_true", help="Show URLs without submitting")
    parser.add_argument("--status", action="store_true", help="Show today's submission status")

    args = parser.parse_args()

    # Status check
    if args.status:
        log = load_log()
        today = datetime.now().strftime("%Y-%m-%d")
        count = log["daily_count"] if log["last_date"] == today else 0
        print(f"\n📊 Today's Status ({today}):")
        print(f"   Submitted: {count}/{DAILY_QUOTA}")
        print(f"   Remaining: {DAILY_QUOTA - count}")
        print(f"   Total URLs ever: {len(log['submitted'])}\n")
        return

    # Single URL
    if args.url:
        url = args.url if args.url.startswith("http") else f"{SITE_URL}{args.url}"
        batch_submit([url], dry_run=args.dry_run)
        return

    # Collect URLs
    urls = []
    if args.news:
        urls = get_urls_from_sitemap(SITEMAP_PATH, filter_section="news")
        # Also add from news sitemap
        news_urls = get_urls_from_sitemap(NEWS_SITEMAP_PATH)
        urls = list(set(urls + news_urls))
    elif args.posts:
        urls = get_urls_from_sitemap(SITEMAP_PATH, filter_section="posts")
    elif args.all:
        urls = get_urls_from_sitemap(SITEMAP_PATH)
    else:
        # Default: recent pages only
        urls = get_urls_from_sitemap(SITEMAP_PATH, max_age_days=args.recent)

    if not urls:
        print("⚠️  No URLs found. Run 'hugo' first to generate sitemap.")
        return

    batch_submit(urls, dry_run=args.dry_run)

if __name__ == "__main__":
    main()
