
import json, datetime, os

# ✅ KPI 데이터 로드
kpi_path = "D:\\limhansin\\vision2025\\reporthub\\scripts\\kpi_report.json"
output_path = "D:\\limhansin\\vision2025\\reporthub\\static\\ai_generated\\ai_kpi_report.json"

if not os.path.exists(kpi_path):
    print("[ERROR] KPI 데이터 없음 — kpi_report.json 먼저 생성 필요")
    exit()

with open(kpi_path, encoding="utf-8") as f:
    kpi = json.load(f)

# ✅ 분석 및 요약 생성
today = datetime.date.today().isoformat()
ctr = kpi["discover"]["ctr"]
score = kpi["score"]

summary = {
    "date": today,
    "report": {
        "ctr": ctr,
        "score": score,
        "discover_clicks": kpi["discover"]["clicks"],
        "discover_impressions": kpi["discover"]["impressions"],
        "indexnow_status": kpi["indexnow"]["status"],
        "gsc_status": kpi["gsc"]["status"],
        "comment": (
            "🚀 Discover 성능 양호 (CTR ≥ 3%)" if ctr >= 3
            else "⚠️ Discover CTR 저조 — 콘텐츠 보강 필요"
        )
    }
}

# ✅ 결과 저장
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

print(json.dumps(summary, indent=2, ensure_ascii=False))
print(f"[OK] AI KPI 리포트 생성 완료 → {output_path}")
