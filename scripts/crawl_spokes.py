# scripts\crawl_spokes.py
import json, time, hashlib, sys
from pathlib import Path
cfg = json.load(open("data/crawl_config.json","r",encoding="utf-8"))
out = []
ts = int(time.time())
def norm_id(url): return hashlib.sha1(url.encode()).hexdigest()[:20]
# TODO: 각 소스별 수집 함수 구현 (HTTP GET, RSS, JSON 등)
def collect(spoke):
    # placeholder 예시
    url = f"https://example.org/{spoke}/{ts}"
    return {
      "id": norm_id(url), "spoke": spoke, "lang":"en","region":"global",
      "url":url, "source":"example", "ts_fetch":ts,
      "title_raw":"Example Title", "summary_raw":"...", "body_raw":"...",
      "entities":[], "metrics":{}, "license":"permitted", "risk_flags":""
    }
for spoke in cfg["spokes"].keys():
    out.append(collect(spoke))
Path("static/ai_generated").mkdir(parents=True, exist_ok=True)
json.dump(out, open("static/ai_generated/crawl_raw.json","w",encoding="utf-8"), ensure_ascii=False)
print("[OK] crawl_raw.json")
