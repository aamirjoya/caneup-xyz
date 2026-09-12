#!/usr/bin/env python3
"""
CaneUp Auto Push Script (auto-push-latest.py)
--------------------------------------------
Automatically detects the latest news article in `content/news/`
or blog post in `content/posts/`, extracts its title, description,
banner image, and canonical URL, and triggers a push notification.

Usage:
  python scripts/auto-push-latest.py
  python scripts/auto-push-latest.py --dry-run
"""

import os
import sys
import glob
import re
import argparse
import subprocess

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEWS_DIR = os.path.join(BASE_DIR, "content", "news")
POSTS_DIR = os.path.join(BASE_DIR, "content", "posts")
BASE_URL = "https://caneup.xyz"


def get_latest_article():
    files = glob.glob(os.path.join(NEWS_DIR, "*.md")) + glob.glob(os.path.join(POSTS_DIR, "*.md"))
    articles = []

    for f in files:
        if os.path.basename(f).startswith("_"):
            continue
        try:
            content = open(f, "r", encoding="utf-8").read()
            # Extract date
            dm = re.search(r"date:\s*([^\n\r]+)", content)
            tm = re.search(r"title:\s*[\"']?([^\"'\n\r]+)", content)
            desc_m = re.search(r"description:\s*[\"']?([^\"'\n\r]+)", content)
            slug_m = re.search(r"slug:\s*[\"']?([^\"'\n\r]+)", content)
            img_m = re.search(r"featured_image:\s*[\"']?([^\"'\n\r]+)", content)

            if dm and tm:
                date_str = dm.group(1).strip().strip('"\'')
                title_str = tm.group(1).strip().strip('"\'')
                desc_str = desc_m.group(1).strip().strip('"\'') if desc_m else ""
                slug_str = slug_m.group(1).strip().strip('"\'') if slug_m else os.path.splitext(os.path.basename(f))[0]
                img_str = img_m.group(1).strip().strip('"\'') if img_m else ""

                section = "news" if "content\\news" in f or "content/news" in f else "posts"
                url = f"{BASE_URL}/{section}/{slug_str}/"

                articles.append({
                    "date": date_str,
                    "title": title_str,
                    "description": desc_str,
                    "url": url,
                    "image": img_str,
                    "file": f
                })
        except Exception:
            pass

    articles.sort(key=lambda x: x["date"], reverse=True)
    return articles[0] if articles else None


def main():
    parser = argparse.ArgumentParser(description="Auto push latest article")
    parser.add_argument("--dry-run", action="store_true", help="Preview only, do not send")
    args = parser.parse_args()

    latest = get_latest_article()
    if not latest:
        print("❌ No articles found in content/news or content/posts.")
        return

    print("=" * 60)
    print(" 📰 LATEST ARTICLE DETECTED FOR AUTO-PUSH")
    print("=" * 60)
    print(f" Date:  {latest['date']}")
    print(f" Title: {latest['title']}")
    print(f" Desc:  {latest['description'][:100]}...")
    print(f" URL:   {latest['url']}")
    print(f" Image: {latest['image']}")
    print("=" * 60)

    # Call send-push.py
    send_script = os.path.join(os.path.dirname(__file__), "send-push.py")
    cmd = [
        sys.executable,
        send_script,
        "--title", latest["title"],
        "--body", latest["description"][:140],
        "--url", latest["url"]
    ]
    if latest["image"]:
        cmd.extend(["--image", latest["image"]])
    if args.dry_run:
        cmd.append("--dry-run")

    subprocess.run(cmd)


if __name__ == "__main__":
    main()
