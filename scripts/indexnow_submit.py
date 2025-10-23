import os, json, requests
INDEXNOW_KEY = os.getenv("INDEXNOW_KEY", "test-key")
SITE_URL = "https://newspreadnow.com"
SITEMAP_URL = f"{SITE_URL}/sitemap.xml"
KEY_LOCATION = f"{SITE_URL}/indexnow.txt"
INDEXNOW_API = "https://api.indexnow.org/indexnow"
BING_API     = "https://www.bing.com/indexnow"
payload = {"host": "newspreadnow.com","key": INDEXNOW_KEY,"keyLocation": KEY_LOCATION,"urlList": [SITEMAP_URL]}
headers = {"Content-Type": "application/json"}
def submit(api: str, name: str):
    try:
        r = requests.post(api, data=json.dumps(payload), headers=headers, timeout=10)
        if r.status_code in (200, 202):
            print(f"[OK] {name} accepted ({r.status_code})")
        else:
            print(f"[ERROR] {name} failed ({r.status_code}): {r.text[:200]}")
    except Exception as e:
        print(f"[ERROR] {name} exception: {e}")
submit(INDEXNOW_API, "IndexNow")
submit(BING_API, "Bing")
print("[OK] IndexNow submission complete")
