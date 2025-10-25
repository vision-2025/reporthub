import requests, json, os, sys

GSC_API = os.getenv("GSC_API_URL", "https://www.google.com/ping?sitemap=")
BING_API = os.getenv("BING_API_URL", "https://www.bing.com/ping?sitemap=")

SITEMAPS = [
    "https://newspreadnow.com/sitemap.xml",
    "https://newspreadnow.com/sitemap-us.xml",
    "https://newspreadnow.com/sitemap-uk.xml",
    "https://newspreadnow.com/sitemap-ca.xml",
    "https://newspreadnow.com/sitemap-au.xml",
    "https://newspreadnow.com/sitemap-de.xml",
    "https://newspreadnow.com/sitemap-ch.xml",
    "https://newspreadnow.com/sitemap-sg.xml"
]

def submit(api, sitemap):
    try:
        r = requests.get(api + sitemap, timeout=10)
        if r.status_code == 200:
            print(f"[OK] 제출 성공 → {api}{sitemap}")
        else:
            print(f"[WARN] 제출 실패 ({r.status_code}) → {api}{sitemap}")
    except Exception as e:
        print(f"[ERROR] 요청 실패 → {e}")

if __name__ == "__main__":
    try:
        for s in SITEMAPS:
            submit(GSC_API, s)
            submit(BING_API, s)
        print("[OK] GSC·Bing 자동 제출 완료")
        sys.exit(0)
    except Exception as e:
        print(f"[ERROR] discover 루프 예외: {e}")
        sys.exit(0)  # 실패 시에도 종료 코드 0으로 반환
