<<<<<<< HEAD
import os, requests

SITE_URL = 'https://newspreadnow.com/sitemap.xml'
SITE_ID = 'https://newspreadnow.com/'   # GSC 등록 도메인
TOKEN = os.getenv('GSC_API_TOKEN', 'test-token')

url = f'https://www.googleapis.com/webmasters/v3/sites/{SITE_ID}/sitemaps/{SITE_URL}'
headers = {'Authorization': f'Bearer {TOKEN}'}

r = requests.put(url, headers=headers, timeout=10)
print('[OK] GSC Submit Response:', r.status_code, r.text)
=======
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SITE_URL = "https://newspreadnow.com/"
SITEMAP = "sitemap.xml"

creds = Credentials.from_authorized_user_file("scripts/token.json", ["https://www.googleapis.com/auth/webmasters"])
service = build("searchconsole", "v1", credentials=creds)

response = service.sitemaps().submit(
    siteUrl=SITE_URL,
    feedpath=f"{SITE_URL}{SITEMAP}"
).execute()

print("[OK] Sitemap submitted successfully")
>>>>>>> 135b02f (chore(security): rebuild clean branch without secrets)
