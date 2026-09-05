import urllib.request
import json
import os
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def search_wikimedia_image(query):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrnamespace=6&gsrsearch={urllib.parse.quote(query)}&gsrlimit=5&prop=imageinfo&iiprop=url|dimensions|mime&format=json"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for pid, pdata in pages.items():
                ii = pdata.get('imageinfo', [{}])[0]
                img_url = ii.get('url')
                mime = ii.get('mime', '')
                if img_url and ('image/jpeg' in mime or 'image/png' in mime or 'image/webp' in mime):
                    return img_url
    except Exception as e:
        print(f"Error searching {query}: {e}")
    return None

queries = {
    'akhilesh_yadav': 'Akhilesh Yadav',
    'high_court_lucknow': 'Allahabad High Court Lucknow',
    'rakesh_tikait': 'Rakesh Tikait',
    'farmer_protest_tractors': 'Farmers protest India tractor',
    'sugarcane_field_india': 'Sugarcane field India farming',
    'fertilizer_bags': 'Fertilizer bags agriculture India',
    'sugar_mill_factory': 'Sugar factory India mill',
    'mustard_field_india': 'Mustard field India agriculture',
    'tractor_trolley_sugarcane': 'Sugarcane tractor India',
    'indian_farmer_smartphone': 'Indian farmer smartphone mobile'
}

for key, q in queries.items():
    found_url = search_wikimedia_image(q)
    print(f"{key}: {found_url}")
