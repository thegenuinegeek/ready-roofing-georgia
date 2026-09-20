import re
import urllib.request
import os
from urllib.parse import urlparse

with open('Squarespace-Wordpress-Export-09-20-2026.xml', 'r', encoding='utf-8') as f:
    content = f.read()

urls = re.findall(r'https://images\.squarespace-cdn\.com/[^\"\'&<>\s]+', content)
urls = list(set(urls))

os.makedirs('public/images', exist_ok=True)

for i, url in enumerate(urls):
    parsed = urlparse(url)
    filename = os.path.basename(parsed.path)
    if not filename.endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif')):
        filename += '.jpg'
    
    filepath = os.path.join('public/images', filename)
    
    print(f'Downloading {url} to {filepath}')
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(filepath, 'wb') as out_file:
                out_file.write(response.read())
    except Exception as e:
        print(f'Failed to download {url}: {e}')
