#!/usr/bin/env python3
"""
CaneUp IndexNow Submitter
Pings IndexNow API (Bing, Yandex, Seznam, Naver) for instantaneous indexing.
"""

import sys
import json
import urllib.request
import urllib.error

HOST = "caneup.xyz"
KEY = "9f8b4e72c1d34a5892e6f1a0b3c4d5e6"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"
ENDPOINT = "https://api.indexnow.org/indexnow"

def submit_urls(urls):
    if not urls:
        print("No URLs provided.")
        return False

    clean_urls = []
    for u in urls:
        u = u.strip()
        if not u:
            continue
        if not u.startswith("http"):
            u = f"https://{HOST}/{u.lstrip('/')}"
        clean_urls.append(u)

    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": clean_urls
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"}
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            status = response.status
            print(f"[+] Successfully submitted {len(clean_urls)} URLs to IndexNow! HTTP Status: {status}")
            return True
    except urllib.error.HTTPError as e:
        print(f"[!] HTTP Error during IndexNow submission: {e.code} - {e.reason}")
        print(e.read().decode('utf-8', errors='ignore'))
        return False
    except Exception as e:
        print(f"[!] Error submitting to IndexNow: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_urls = sys.argv[1:]
    else:
        # Default submission of core pages
        target_urls = [
            f"https://{HOST}/",
            f"https://{HOST}/news/",
            f"https://{HOST}/tools/",
            f"https://{HOST}/search/",
            f"https://{HOST}/ganna-parchi-calendar-caneup/",
            f"https://{HOST}/eganna/",
            f"https://{HOST}/ganna-bhugtan-status/"
        ]
    submit_urls(target_urls)
