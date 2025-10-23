import os, requests, json

API_KEY = os.getenv('BING_API_KEY', '').strip()
if not API_KEY:
    raise SystemExit('[ERROR] Bing API Key missing')

SITE_URL = 'https://newspreadnow.com/sitemap.xml'
endpoint = f'https://ssl.bing.com/webmaster/api.svc/json/SubmitUrlbatch?apikey={API_KEY}'
payload = {'siteUrl': 'https://newspreadnow.com', 'urlList': [SITE_URL]}

r = requests.post(endpoint, json=payload, timeout=10)
print('[OK] Bing Submit Response:', r.status_code, r.text)
