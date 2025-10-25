import json, sys, datetime, pathlib
root = pathlib.Path(__file__).resolve().parents[1]
model_p = root / "static/ai_generated/ctr_model.json"
fb_p    = root / "static/ai_generated/feedback.json"

m = json.loads(model_p.read_text(encoding="utf-8"))
fb = json.loads(fb_p.read_text(encoding="utf-8"))

ctr = sum(s.get("clicks",0) for s in fb.get("samples",[])) / max(1,sum(s.get("impressions",0) for s in fb.get("samples",[])))
m["version"] = int(m.get("version",0)) + 1
m["last_trained"] = datetime.datetime.utcnow().replace(microsecond=0).isoformat()+"Z"
m["baseline_ctr"] = round(ctr,5)

model_p.write_text(json.dumps(m, ensure_ascii=False, indent=2), encoding="utf-8")
print("[OK] ctr_model.json updated:", m)
