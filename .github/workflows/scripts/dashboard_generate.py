import json, datetime, os, glob

SRC = "logs/"
OUT = "public/dashboard.html"

def load_jsonlines(path):
    result=[]
    with open(path, encoding="utf-8") as f:
        for line in f:
            try: result.append(json.loads(line))
            except: pass
    return result

ctr = load_jsonlines(os.path.join(SRC,"discover_metrics.json"))
kpi = json.load(open(os.path.join(SRC,"kpi_report.json"))) if os.path.exists(os.path.join(SRC,"kpi_report.json")) else {}

html = f"""
<html><head><meta charset='utf-8'><title>Narak Dashboard</title>
<style>body{{font-family:sans-serif;background:#101010;color:#eee;padding:30px;}}
.card{{margin:20px;padding:20px;border:1px solid #333;border-radius:8px;}}</style></head><body>
<h1>나라크 통합 대시보드</h1>
<div class='card'><h2>📊 Discover 실측 (최근)</h2>
<p>CTR: {ctr[-1]['ctr']}% / 진입률: {ctr[-1]['entry_rate']}% / 클릭수: {ctr[-1]['clicks']} / 노출수: {ctr[-1]['impressions']}</p></div>
<div class='card'><h2>🧠 KPI 리포트</h2>
<pre>{json.dumps(kpi, indent=2, ensure_ascii=False)}</pre></div>
<p>최종 업데이트: {datetime.datetime.now().isoformat()}</p>
</body></html>
"""
with open(OUT,"w",encoding="utf-8") as f:f.write(html)
print("[OK] Dashboard 생성 완료:", OUT)
