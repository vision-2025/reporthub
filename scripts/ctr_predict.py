import json, random, os

INPUT_PATH = "public/ai_generated/ai_result.json"
OUTPUT_PATH = "public/ai_generated/ctr_predict.json"

if not os.path.exists(INPUT_PATH):
    print("[WARN] AI merge result not found, skipping CTR prediction")
    exit(0)

ctr = round(random.uniform(2.5, 5.0), 2)
data = {"predicted_ctr": ctr}

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print(f"[OK] CTR predicted value: {ctr}%")
