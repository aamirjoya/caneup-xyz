import urllib.request
import json
import os
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

out_dir = r'C:\Users\caneu\.gemini\antigravity\brain\f0566670-25ee-4739-bb10-e53286d68160\real_photos'
os.makedirs(out_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def download_file(url, out_path):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as resp:
        with open(out_path, 'wb') as f:
            f.write(resp.read())
    print(f"Downloaded: {os.path.basename(out_path)} ({os.path.getsize(out_path)/1024:.1f} KB)")

# Direct authentic verified Wikimedia images
photos = {
    'yogi_adityanath.jpg': 'https://upload.wikimedia.org/wikipedia/commons/1/1a/Yogi_Adityanath_in_2023.jpg',
    'akhilesh_yadav.jpg': 'https://upload.wikimedia.org/wikipedia/commons/7/7e/Akhilesh_Yadav.JPG',
    'rakesh_tikait.jpg': 'https://upload.wikimedia.org/wikipedia/commons/f/f1/BKD%27s_national_spokesperson_Rakesh_Tikait_addressing_rally.jpg',
    'high_court_lucknow.jpg': 'https://upload.wikimedia.org/wikipedia/commons/4/47/High_Court_Lucknow.jpg',
    'sugar_mill_moradabad.jpg': 'https://upload.wikimedia.org/wikipedia/commons/c/c9/Sugar_Mill%2C_Raja_ka_Sahaspur.jpg',
    'mustard_crop_field.jpg': 'https://upload.wikimedia.org/wikipedia/commons/b/b2/Agriculture_Rajasthan_India_-_2009_Mustard_crop.jpg',
    'tractor_agriculture_india.jpg': 'https://upload.wikimedia.org/wikipedia/commons/5/53/Tractor_in_Paddy_field_at_vill._Aanji%2C_Dist._Hardoi%2C_Uttar_Pradesh.jpg',
    'sugarcane_harvest_india.jpg': 'https://upload.wikimedia.org/wikipedia/commons/4/4b/Harvesting_sugarcane_near_Dharwad%2C_Karnataka%2C_India.jpg'
}

for name, url in photos.items():
    dest = os.path.join(out_dir, name)
    try:
        download_file(url, dest)
    except Exception as e:
        print(f"Error downloading {name}: {e}")

print("Real photo downloads complete!")
