import os, json, datetime

SRC = "static/ai_generated/"
OUT = "content/posts/"
LOG = "logs/ai_merge.log"

def merge_latest():
    files = sorted([f for f in os.listdir(SRC) if f.endswith(".json")])
    if not files: 
        print("[ERROR] No AI JSON found"); return
    latest = os.path.join(SRC, files[-1])
    with open(latest, encoding="utf-8") as f:
        data = json.load(f)
    slug = data.get("slug", datetime.datetime.now().strftime("%Y%m%d%H%M"))
    post_path = os.path.join(OUT, f"{slug}.md")
    with open(post_path, "w", encoding="utf-8") as w:
        w.write(f"---\ntitle: \"{data.get('title','AI Generated Post')}\"\ndate: {datetime.datetime.now().isoformat()}\ndescription: {data.get('summary','')}\n---\n\n")
        w.write(data.get("content",""))
    with open(LOG,"a",encoding="utf-8") as log:
        log.write(f"{datetime.datetime.now()} merged {latest} -> {post_path}\n")
    print(f"[OK] {post_path} generated")

if __name__ == "__main__":
    merge_latest()
