
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import datetime, json

# ✅ 토큰 파일 (이미 인증 완료된 GSC token.json 사용)
creds = Credentials.from_authorized_user_file(
    "scripts/token.json", ["https://www.googleapis.com/auth/webmasters.readonly"]
)
service = build("searchconsole", "v1", credentials=creds)

# ✅ 사이트 설정
SITE_URL = "https://newspreadnow.com/"
today = datetime.date.today()
start_date = (today - datetime.timedelta(days=7)).isoformat()
end_date = today.isoformat()

# ✅ Discover 데이터 요청
request = {
    "startDate": start_date,
    "endDate": end_date,
    "dimensions": ["page"],
    "rowLimit": 50
}

response = service.searchanalytics().query(siteUrl=SITE_URL, body=request).execute()

# ✅ 결과 요약
rows = response.get("rows", [])
total_clicks = sum([r["clicks"] for r in rows])
total_impressions = sum([r["impressions"] for r in rows])
ctr = (total_clicks / total_impressions * 100) if total_impressions > 0 else 0

summary = {
    "date": str(today),
    "clicks": total_clicks,
    "impressions": total_impressions,
    "ctr_percent": round(ctr, 2),
}

print(json.dumps(summary, indent=2))
with open("scripts/ctr_report.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

print("[OK] Discover CTR 리포트 생성 완료 → scripts/ctr_report.json")
