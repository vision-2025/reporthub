
import json, os, datetime

# ✅ 파일 경로 정의
ctr_path = "D:\\limhansin\\vision2025\\reporthub\\scripts\\ctr_report.json"
indexnow_log = "D:\\limhansin\\vision2025\\reporthub\\scripts\\indexnow_submit.log"
gsc_status = "D:\\limhansin\\vision2025\\reporthub\\scripts\\gsc_submit.log"
kpi_out = "D:\\limhansin\\vision2025\\reporthub\\scripts\\kpi_report.json"

# ✅ KPI 초기 구조
kpi = {
    "date": str(datetime.date.today()),
    "discover": {"clicks": 0, "impressions": 0, "ctr": 0.0},
    "indexnow": {"status": "unknown"},
    "gsc": {"status": "unknown"},
    "score": 0
}

# ✅ Discover CTR 리포트 불러오기
if os.path.exists(ctr_path):
    with open(ctr_path, encoding="utf-8") as f:
        c = json.load(f)
        kpi["discover"]["clicks"] = c.get("clicks", 0)
        kpi["discover"]["impressions"] = c.get("impressions", 0)
        kpi["discover"]["ctr"] = c.get("ctr_percent", 0.0)

# ✅ IndexNow 상태 로그 반영
if os.path.exists(indexnow_log):
    with open(indexnow_log, encoding="utf-8", errors="ignore") as f:
        lines = f.read()
        if "OK" in lines or "202" in lines:
            kpi["indexnow"]["status"] = "ok"
        else:
            kpi["indexnow"]["status"] = "error"

# ✅ GSC 제출 로그 반영
if os.path.exists(gsc_status):
    with open(gsc_status, encoding="utf-8", errors="ignore") as f:
        lines = f.read()
        if "OK" in lines or "successfully" in lines:
            kpi["gsc"]["status"] = "ok"
        else:
            kpi["gsc"]["status"] = "error"

# ✅ KPI 점수 계산 (Discover CTR·제출 성공률 기준)
score = 0
if kpi["discover"]["ctr"] >= 3:
    score += 40
if kpi["indexnow"]["status"] == "ok":
    score += 30
if kpi["gsc"]["status"] == "ok":
    score += 30
kpi["score"] = score

# ✅ 저장
with open(kpi_out, "w", encoding="utf-8") as f:
    json.dump(kpi, f, ensure_ascii=False, indent=2)

print(json.dumps(kpi, indent=2, ensure_ascii=False))
print(f"[OK] KPI 통합 리포트 생성 완료 → {kpi_out}")
