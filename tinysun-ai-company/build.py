#!/usr/bin/env python3
"""Ghép ngữ cảnh dùng chung vào từng template skill → dist/<skill>/SKILL.md.

Cách dùng:  python3 build.py
Sau đó upload từng thư mục trong dist/ lên claude.ai (Settings → Skills) thay cho bản cũ.
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent
CTX = (ROOT / "context" / "tinysun-context.md").read_text(encoding="utf-8").strip()
FILE_RULES = (ROOT / "context" / "file-rules.md").read_text(encoding="utf-8").strip()
FACTS = (ROOT / "context" / "product-fact-sheet.md").read_text(encoding="utf-8").strip()

PLACEHOLDERS = {
    "{{CONTEXT}}": CTX,
    "{{FILE_RULES}}": FILE_RULES,
    "{{PRODUCT_FACTS}}": FACTS,
}

def build():
    out_dirs = []
    for tpl in sorted((ROOT / "templates").glob("*.md")):
        name = tpl.stem
        text = tpl.read_text(encoding="utf-8")
        for key, val in PLACEHOLDERS.items():
            text = text.replace(key, val)
        left = re.findall(r"{{[A-Z_]+}}", text)
        if left:
            sys.exit(f"{name}: placeholder chưa thay: {left}")
        if not text.startswith("---\nname: " + name + "\n"):
            sys.exit(f"{name}: frontmatter 'name' phải trùng tên file template")
        dst = ROOT / "dist" / name / "SKILL.md"
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(text, encoding="utf-8")
        out_dirs.append((name, len(text.encode("utf-8"))))
    for name, size in out_dirs:
        print(f"dist/{name}/SKILL.md  {size:>6} bytes")

if __name__ == "__main__":
    build()
