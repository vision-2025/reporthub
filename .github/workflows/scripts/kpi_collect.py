import json, datetime, os

CTR_LOG = "logs/ctr_history.txt"
INDEXNOW_LOG = "logs/indexnow_history.txt"
REPORT = "logs/kpi_report.json"

def parse_ctr():
    if not os.path.exists(CTR_LOG): return 0
    with open(CTR_LOG) as f: lines=f.readlines()
    return float(lines[-1].split()[-1]) if lines else 0

def parse_indexnow():
    if not os.path.exists(INDEXNOW_LOG): return 0
    with open(INDEXNOW_LOG) as f: return len(f.readlines())

data = {
    "timestamp": datetime.datetime.now().isoformat(),
    "ctr": parse_ctr(),
    "indexnow_submissions": parse_indexnow(),
}

with open(REPORT, "w") as f: json.dump(data,f,indent=2)
print("[OK] KPI 보고서 생성 완료")
