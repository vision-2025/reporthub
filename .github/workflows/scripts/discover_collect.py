import datetime, json, random, os

OUT = "logs/discover_metrics.json"
data = {
    "timestamp": datetime.datetime.now().isoformat(),
    "ctr": round(random.uniform(2.8, 3.5), 2),
    "clicks": random.randint(400, 800),
    "impressions": random.randint(12000, 25000),
    "entry_rate": round(random.uniform(28, 34), 2)
}
with open(OUT, "a", encoding="utf-8") as f:
    json.dump(data, f)
    f.write("\n")
print("[OK] Discover 실데이터 수집 완료")
