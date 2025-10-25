import requests, json, os

API_KEY = os.getenv("INDEXNOW_KEY", "your-indexnow-key")
SITE_URL = "https://newspreadnow.com"
ENDPOINT = "https://api.indexnow.org/indexnow"

urls = [
    f"{SITE_URL}/sitemap.xml",
    f"{SITE_URL}/ai_generated/",
]

payload = {
    "host": SITE_URL.replace("https://", ""),
    "key": API_KEY,
    "urlList": urls
}

try:
    r = requests.post(ENDPOINT, json=payload)
    if r.status_code == 200:
        print("[OK] IndexNow 제출 성공")
    else:
        print(f"[ERROR] IndexNow 실패: {r.status_code} - {r.text}")
except Exception as e:
    print(f"[ERROR] 요청 실패: {e}")
