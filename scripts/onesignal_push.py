#!/usr/bin/env python3
"""Send a OneSignal web-push notification for a newly published caneup.xyz article.

Usage:
  onesignal_push.py --title "..." --url "https://caneup.xyz/news/<slug>/"
                     [--image "https://caneup.xyz/images/<slug>.webp"]
                     [--excerpt "..."] [--dry-run]

- Reads the REST API key from ~/workspace/user/onesignal-rest-key-caneup (0600).
- Skips (exit 0) if this article slug was already pushed in the last 7 days
  (dedupe log: scripts/.onesignal_push_sent.json, untracked).
- Non-fatal by design: any failure prints to stderr and exits 0, so a
  publishing cron never fails because of push.
"""
import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from os import path
from os.path import abspath, dirname, expanduser, join

APP_ID = 'b86aeb76-438e-49d0-863a-7fb1bfb4e7da'
KEY_FILE = expanduser('~/workspace/user/onesignal-rest-key-caneup')
SENT_LOG = join(dirname(abspath(path.realpath(__file__))), '.onesignal_push_sent.json')

API_URL = 'https://api.onesignal.com/notifications'
PUSH_SLOTS = {1, 4, 7}


def load_sent():
    try:
        with open(SENT_LOG, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def save_sent(data):
    try:
        with open(SENT_LOG, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
    except OSError as e:
        print('warn: could not write sent log: ' + str(e), file=sys.stderr)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--title', required=True)
    ap.add_argument('--url', required=True)
    ap.add_argument('--image', default='')
    ap.add_argument('--excerpt', default='')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--force', action='store_true',
                    help="bypass the daily slot gate (manual send; does not consume the day's auto counter)")
    args = ap.parse_args()

    slug = args.url.rstrip('/').rsplit('/', 1)[-1]
    body_text = args.excerpt.strip() or args.title.strip()

    payload = {
        'app_id': APP_ID,
        'included_segments': ['Active Subscriptions'],
        'headings': {'hi': args.title, 'en': args.title},
        'contents': {'hi': body_text, 'en': body_text},
        'web_url': args.url,
    }
    if args.image:
        payload['big_picture'] = args.image
        payload['chrome_web_image'] = args.image

    if args.dry_run:
        print(json.dumps(payload, ensure_ascii=False, indent=2)[:1500])
        print('dry-run: not sent (no state changed)')
        return 0

    try:
        with open(KEY_FILE, 'r', encoding='utf-8') as f:
            api_key = f.read().strip()
    except OSError as e:
        print('push skipped (no api key): ' + str(e), file=sys.stderr)
        return 0
    if not api_key:
        print('push skipped (empty api key)', file=sys.stderr)
        return 0

    sent = load_sent()
    last = sent.get(slug, 0)
    if time.time() - last < 604800:
        print('skip: already pushed ' + slug)
        return 0

    if args.force:
        n = None
    else:
        try:
            from zoneinfo import ZoneInfo
            today = time.strftime('%Y-%m-%d', time.localtime(time.time(), ZoneInfo('Asia/Kolkata')))
        except Exception:
            today = time.strftime('%Y-%m-%d')
        counts = sent.setdefault('_counts', {})
        n = counts.get(today, 0) + 1
        counts[today] = n
        for d in [d for d in counts if d < today]:
            del counts[d]
        if n not in PUSH_SLOTS:
            save_sent(sent)
            print('skip: article #%d today not in push slots %s' % (n, sorted(PUSH_SLOTS)))
            return 0

    if n is not None:
        save_sent(sent)

    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
        headers={
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': 'Bearer ' + api_key,
        },
        method='POST')

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('push FAILED: HTTP %d %s' % (e.code, e.read().decode('utf-8')[:300]), file=sys.stderr)
        return 0
    except Exception as e:
        print('push FAILED: ' + str(e), file=sys.stderr)
        return 0

    errs = result.get('errors') if isinstance(result, dict) else None
    if errs:
        print('push FAILED: OneSignal errors: ' + str(errs), file=sys.stderr)
        return 0

    nid = result.get('id') if isinstance(result, dict) else None
    if not nid:
        print('push FAILED: no notification id in response: ' + json.dumps(result)[:200], file=sys.stderr)
        return 0

    recipients = result.get('recipients', '?')
    print('push sent: id=%s recipients=%s url=%s' % (nid, recipients, args.url))
    sent[slug] = time.time()
    save_sent(sent)
    return 0


if __name__ == '__main__':
    sys.exit(main())
