#!/usr/bin/env python3
"""
CaneUp Custom Push Notification Dispatcher (send-push.py)
---------------------------------------------------------
LaraPush-style CLI tool to broadcast rich web push notifications
to all CaneUp subscribers with large banners, deep links, and action buttons.

Usage:
  # Interactive mode:
  python scripts/send-push.py

  # Direct command line:
  python scripts/send-push.py --title "सट्टा सुधार अंतिम 3 दिन" \
                             --body "15 सितंबर को बंद होगा पोर्टल, तुरंत जांचें।" \
                             --url "https://caneup.xyz/news/up-ganna-satta-objection-last-3-days-september-15-deadline-2026/" \
                             --image "/images/news/up-ganna-satta-objection-last-3-days-september-15-deadline-2026.webp"

  # Dry-run test preview:
  python scripts/send-push.py --dry-run
"""

import sys
import os
import json
import argparse
import urllib.request
import urllib.parse
from datetime import datetime

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Configuration
ONESIGNAL_APP_ID = "b86aeb76-438e-49d0-863a-7fb1bfb4e7da"
ONESIGNAL_REST_API_KEY = os.environ.get("ONESIGNAL_REST_API_KEY", "")
BASE_URL = "https://caneup.xyz"
LOG_FILE = os.path.join(os.path.dirname(__file__), "push-history.json")


def load_history():
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []


def save_history(record):
    history = load_history()
    history.insert(0, record)
    history = history[:100]  # Keep last 100
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)


def render_preview(title, body, url, image_url):
    print("\n" + "=" * 62)
    print(" 📱 MOBILE NOTIFICATION PREVIEW (LaraPush Style)")
    print("=" * 62)
    print(" [ 🌾 CaneUp • अभी-अभी ]")
    print(f" 🔔 {title}")
    print(f" 📄 {body}")
    if image_url:
        print(f" 🖼️ [बड़ा बैनर फोटो: {image_url}]")
    print(f" 🔗 लिंक: {url}")
    print(" [👉 अभी देखें]   [बंद करें]")
    print("=" * 62 + "\n")


def send_notification(title, body, url, image_url=None, dry_run=False):
    if not url.startswith("http"):
        url = urllib.parse.urljoin(BASE_URL, url)
    if image_url and not image_url.startswith("http"):
        image_url = urllib.parse.urljoin(BASE_URL, image_url)

    render_preview(title, body, url, image_url)

    payload = {
        "app_id": ONESIGNAL_APP_ID,
        "included_segments": ["All", "Subscribed Users"],
        "headings": {"en": title, "hi": title},
        "contents": {"en": body, "hi": body},
        "url": url,
        "chrome_web_icon": f"{BASE_URL}/images/logo-192.png",
        "chrome_web_badge": f"{BASE_URL}/images/favicon-32x32.png",
        "web_buttons": [
            {"id": "read-now", "text": "👉 अभी देखें", "icon": f"{BASE_URL}/images/favicon-32x32.png", "url": url},
            {"id": "dismiss", "text": "बंद करें"}
        ]
    }

    if image_url:
        payload["chrome_web_image"] = image_url
        payload["big_picture"] = image_url

    if dry_run:
        print("🔍 DRY-RUN MODE: Notification was NOT dispatched to subscribers.")
        print("Payload JSON:")
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return True

    record = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S IST"),
        "title": title,
        "body": body,
        "url": url,
        "image": image_url,
        "status": "ready"
    }

    # Save to local history log
    save_history(record)
    print(f"✅ Push Campaign recorded in push-history.json!")

    if ONESIGNAL_REST_API_KEY:
        try:
            req = urllib.request.Request(
                "https://onesignal.com/api/v1/notifications",
                data=json.dumps(payload).encode("utf-8"),
                headers={
                    "Content-Type": "application/json; charset=utf-8",
                    "Authorization": f"Basic {ONESIGNAL_REST_API_KEY}"
                },
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                result = json.loads(resp.read().decode("utf-8"))
                print(f"🚀 Sent successfully to subscribers! ID: {result.get('id', 'N/A')}, Recipients: {result.get('recipients', 'All')}")
                return True
        except Exception as e:
            print(f"❌ Error dispatching via REST API: {e}")
            return False
    else:
        print("\n💡 TIP: ONESIGNAL_REST_API_KEY environment variable is not set.")
        print("To auto-blast directly via API:")
        print("  1. OneSignal Dashboard -> Settings -> Keys & IDs -> REST API Key")
        print("  2. $env:ONESIGNAL_REST_API_KEY = 'your-key'")
        print("Meanwhile, your notification payload is ready and can be pasted into OneSignal or LaraPush dashboard!")
        return True


def interactive_mode():
    print("\n" + "=" * 60)
    print(" 🌾 CaneUp LaraPush-Style Notification Dispatcher")
    print("=" * 60)

    title = input("शीर्षक (Title): ").strip()
    if not title:
        title = "गन्ना पर्ची व सट्टा महत्वपूर्ण सूचना — CaneUp"

    body = input("संदेश (Message / Body): ").strip()
    if not body:
        body = "आज का नया अपडेट और जरूरी आदेश पोर्टल पर उपलब्ध है।"

    url = input("टारगेट लिंक (URL): ").strip()
    if not url:
        url = "https://caneup.xyz/news/"

    image = input("बैनर फोटो (Image URL, optional): ").strip()

    send_notification(title, body, url, image if image else None, dry_run=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send Web Push Notifications for CaneUp")
    parser.add_argument("--title", type=str, help="Notification title")
    parser.add_argument("--body", type=str, help="Notification body message")
    parser.add_argument("--url", type=str, help="Target link URL")
    parser.add_argument("--image", type=str, help="Large banner image URL")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without broadcasting")

    args = parser.parse_args()

    if args.title and args.body:
        send_notification(
            args.title,
            args.body,
            args.url or "https://caneup.xyz/",
            args.image,
            dry_run=args.dry_run
        )
    elif args.dry_run:
        send_notification(
            "सट्टा व सर्वे आपत्ति के अंतिम 3 दिन शेष",
            "15 सितंबर को लॉक होगा पोर्टल। काउंटर खुले हैं।",
            "https://caneup.xyz/news/up-ganna-satta-objection-last-3-days-september-15-deadline-2026/",
            "/images/news/up-ganna-satta-objection-last-3-days-september-15-deadline-2026.webp",
            dry_run=True
        )
    else:
        interactive_mode()
