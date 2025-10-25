# scripts\build_markdown.py
import json, os, re, time
from pathlib import Path

BASE = Path("content/reports")
DATA = Path("static/ai_generated/analyzed.json")

if not DATA.exists():
    print("[ERROR] analyzed.json 없음 — 먼저 analyze_spokes.py 실행 필요")
    exit(1)

with open(DATA, "r", encoding="utf-8") as f:
    docs = json.load(f)

def sanitize(name:str):
    return re.sub(r"[^a-z0-9\-]", "-", name.lower())

for doc in docs:
    spoke = doc.get("spoke","misc")
    title = doc.get("title","Untitled")
    desc = doc.get("description","")
    body = doc.get("body_raw","")
    qscore = doc.get("qscore",0)
    folder = BASE / spoke
    folder.mkdir(parents=True, exist_ok=True)

    slug = sanitize(title)[:60]
    out = folder / f"{slug}.md"

    fm = f"""---
title: "{title}"
description: "{desc}"
date: {time.strftime('%Y-%m-%dT%H:%M:%S')}
spoke: "{spoke}"
qscore: {qscore}
draft: false
---

{body}

{{{{< cta label="엔슨 리포트 더 보기" url="/reports/" >}}}}
"""

    with open(out, "w", encoding="utf-8") as w:
        w.write(fm)

print(f"[OK] {len(docs)}개 콘텐츠 변환 완료 → {BASE}")
