import os
import sys
import glob
import re

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
ws_dir = os.path.join(base_dir, 'content', 'webstories')
static_dir = os.path.join(base_dir, 'static')
os.makedirs(static_dir, exist_ok=True)

md_files = glob.glob(os.path.join(ws_dir, '*.md'))
webstories = []

def clean_w3c_date(dt_str):
    if not dt_str:
        return "2026-08-28T16:00:00+05:30"
    dt_str = dt_str.strip('"').strip("'").strip()
    # Replace space with T for strict ISO-8601 W3C date format
    if " " in dt_str and "T" not in dt_str:
        dt_str = dt_str.replace(" ", "T", 1)
    # If no timezone offset, add +05:30
    if not re.search(r'[\+\-]\d{2}:\d{2}$', dt_str) and not dt_str.endswith('Z'):
        if len(dt_str) == 10:
            dt_str += "T00:00:00+05:30"
        elif len(dt_str) == 19:
            dt_str += "+05:30"
    return dt_str

for f in md_files:
    if os.path.basename(f) == '_index.md':
        continue
        
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
        
    # Extract title
    m_title = re.search(r'title:\s*["\']?(.*?)["\']?\n', txt)
    title = m_title.group(1).strip() if m_title else "Web Story"
    
    # Extract slug
    m_slug = re.search(r'slug:\s*([^\s\n]+)', txt)
    slug = m_slug.group(1).strip() if m_slug else os.path.basename(f).replace('.md', '')
    
    # Extract date/lastmod
    m_lastmod = re.search(r'lastmod:\s*([^\n]+)', txt)
    m_date = re.search(r'date:\s*([^\n]+)', txt)
    
    raw_date = m_lastmod.group(1).strip() if m_lastmod else (m_date.group(1).strip() if m_date else "2026-08-28T16:00:00+05:30")
    formatted_date = clean_w3c_date(raw_date)
    
    # Extract featured_image
    m_img = re.search(r'featured_image:\s*["\']?(.*?)["\']?\n', txt)
    feat_img = m_img.group(1).strip() if m_img else ""
    if feat_img and not feat_img.startswith('http'):
        feat_img = f"https://caneup.xyz{feat_img if feat_img.startswith('/') else '/' + feat_img}"
        
    url = f"https://caneup.xyz/webstories/{slug}/"
    webstories.append({
        "url": url,
        "title": title,
        "date": formatted_date,
        "img": feat_img
    })

print(f"Found {len(webstories)} Web Stories. Generating SINGLE WebStory XML Sitemap...")

# Build XML Sitemap
xml_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
    '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">',
    '  <!-- Dedicated Web Stories XML Sitemap for CaneUp.xyz -->'
]

for ws in webstories:
    xml_lines.append('  <url>')
    xml_lines.append(f'    <loc>{ws["url"]}</loc>')
    xml_lines.append(f'    <lastmod>{ws["date"]}</lastmod>')
    xml_lines.append('    <changefreq>daily</changefreq>')
    xml_lines.append('    <priority>0.9</priority>')
    if ws["img"]:
        xml_lines.append('    <image:image>')
        xml_lines.append(f'      <image:loc>{ws["img"]}</image:loc>')
        xml_lines.append(f'      <image:title>{ws["title"]}</image:title>')
        xml_lines.append('    </image:image>')
    xml_lines.append('  </url>')

xml_lines.append('</urlset>')

xml_content = '\n'.join(xml_lines)

# Write ONLY ONE file: static/webstory-sitemap.xml
out_file1 = os.path.join(static_dir, 'webstory-sitemap.xml')
out_file2 = os.path.join(static_dir, 'sitemap-webstories.xml')

with open(out_file1, 'w', encoding='utf-8') as f:
    f.write(xml_content)

# Remove duplicate sitemap-webstories.xml if present
if os.path.exists(out_file2):
    os.remove(out_file2)
    print("Removed duplicate sitemap file: sitemap-webstories.xml")

print(f"Successfully generated single WebStory Sitemap with {len(webstories)} URLs:")
print(f" - {out_file1}")
