import os, json, datetime

OUTPUT_DIR = "public/ai_generated"
os.makedirs(OUTPUT_DIR, exist_ok=True)

data = {
    "timestamp": datetime.datetime.now().isoformat(),
    "status": "AI merge executed",
    "message": "auto-generated content placeholder"
}

with open(os.path.join(OUTPUT_DIR, "ai_result.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("[OK] ai_merge.py executed successfully")
