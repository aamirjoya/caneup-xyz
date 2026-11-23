#!/usr/bin/env python3
"""Regenerate static/webstory-sitemap.xml from content/webstories/*.md.

Portable: repo-relative paths (works on Linux and Windows), base URL from
BASE_URL env (default https://upcaneup.info). Run from anywhere:
    python3 scripts/generate-webstory-sitemap.py
"""
import glob
import os
import re
import sys
from xml.sax.saxutils import escape

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = os.environ.get("BASE_URL", "https://upcaneup.info").rstrip("/")
WS_DIR = os.path.join(REPO_ROOT, "content", "webstories")
OUT_FILE = os.path.join(REPO_ROOT, "static", "webstory-sitemap.xml")

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL | re.MULTILINE)


def field(txt, name):
    m = re.search(r"^" + name + r":\s*(.+)$", txt, re.MULTILINE)
    if not m:
        return ""
    return m.group(1).strip().strip('"').strip("'").strip()


def clean_w3c_date(dt_str):
    dt_str = (dt_str or "2026-08-28T16:00:00+05:30").strip()
    if " " in dt_str and "T" not in dt_str:
        dt_str = dt_str.replace(" ", "T", 1)
    if not re.search(r"[\+\-]\d{2}:\d{2}$", dt_str) and not dt_str.endswith("Z"):
        if len(dt_str) == 10:
            dt_str += "T00:00:00+05:30"
        elif len(dt_str) == 19:
            dt_str += "+05:30"
    return dt_str


def main():
    webstories = []
    for f in sorted(glob.glob(os.path.join(WS_DIR, "*.md"))):
        if os.path.basename(f) == "_index.md":
            continue
        with open(f, "r", encoding="utf-8") as fp:
            txt = fp.read()
        fm = FRONTMATTER_RE.search(txt)
        head = fm.group(1) if fm else txt
        title = field(head, "title") or "Web Story"
        slug = os.path.splitext(os.path.basename(f))[0]
        raw_date = field(head, "lastmod") or field(head, "date")
        feat_img = field(head, "featured_image")
        if feat_img and not feat_img.startswith("http"):
            feat_img = BASE_URL + (feat_img if feat_img.startswith("/") else "/" + feat_img)
        webstories.append({
            "url": f"{BASE_URL}/webstories/{slug}/",
            "title": title,
            "date": clean_w3c_date(raw_date),
            "img": feat_img,
        })

    webstories.sort(key=lambda w: w["date"], reverse=True)

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">',
        '  <!-- Dedicated Web Stories XML Sitemap for upcaneup.info -->',
    ]
    for ws in webstories:
        lines.append("  <url>")
        lines.append(f"    <loc>{escape(ws['url'])}</loc>")
        lines.append(f"    <lastmod>{escape(ws['date'])}</lastmod>")
        lines.append("    <changefreq>daily</changefreq>")
        lines.append("    <priority>0.9</priority>")
        if ws["img"]:
            lines.append("    <image:image>")
            lines.append(f"      <image:loc>{escape(ws['img'])}</image:loc>")
            lines.append(f"      <image:title>{escape(ws['title'])}</image:title>")
            lines.append("    </image:image>")
        lines.append("  </url>")
    lines.append("</urlset>")

    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Found {len(webstories)} web stories.")
    print(f"Wrote {OUT_FILE}")
    if webstories:
        print(f"Newest: {webstories[0]['date']} — {webstories[0]['url']}")
        print(f"Oldest: {webstories[-1]['date']} — {webstories[-1]['url']}")


if __name__ == "__main__":
    sys.exit(main())
