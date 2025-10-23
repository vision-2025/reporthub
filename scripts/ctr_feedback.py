
import json, os

path = "D:\\limhansin\\vision2025\\reporthub\\scripts\\ctr_report.json"
if not os.path.exists(path):
    print("[ERROR] CTR 리포트 없음")
    exit()

with open(path, encoding="utf-8") as f:
    data = json.load(f)

ctr = data.get("ctr_percent", 0)
print(f"[INFO] 현재 CTR: {ctr}%")

if ctr < 3:
    print("[WARN] CTR 3% 미만 → 콘텐츠 보강 트리거 실행")
    # 여기서 Colab/AI 호출 가능 (예: 콘텐츠 품질 강화)
else:
    print("[OK] CTR 양호, Discover 성능 안정권")
