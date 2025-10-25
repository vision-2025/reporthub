# scripts\analyze_spokes.py
import json, re, time, math, sys
from pathlib import Path
data = json.load(open("static/ai_generated/crawl_raw.json","r",encoding="utf-8"))
def score(d):
    fresh = 1.0; authority = 0.8; ed = 0.5; sm = 0.7
    return 0.35*fresh+0.25*authority+0.20*ed+0.20*sm
def normalize(txt): return re.sub(r"\s+"," ",txt).strip()
out=[]
for d in data:
    if d.get("license")=="unknown" or d.get("risk_flags"): continue
    d["title"]=normalize(d["title_raw"])[:64]
    d["description"]=normalize(d.get("summary_raw") or d["body_raw"][:160])
    d["qscore"]=round(score(d),3)
    out.append(d)
Path("static/ai_generated").mkdir(parents=True, exist_ok=True)
json.dump(out, open("static/ai_generated/analyzed.json","w",encoding="utf-8"), ensure_ascii=False)
print("[OK] analyzed.json")
