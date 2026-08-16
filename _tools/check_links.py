# -*- coding: utf-8 -*-
"""내부 링크 검사 —  python _tools/check_links.py"""
import os, re, sys
from urllib.parse import urljoin

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dist")
ROOT = os.path.abspath(ROOT)
SEP = os.sep

bad, total, pages = [], 0, 0
for dp, _, fns in os.walk(ROOT):
    for fn in fns:
        if not fn.endswith(".html"):
            continue
        pages += 1
        p = os.path.join(dp, fn)
        rel = os.path.relpath(p, ROOT).replace(SEP, "/")
        base = "/" + os.path.dirname(rel)
        if not base.endswith("/"):
            base += "/"
        html = open(p, encoding="utf-8").read()
        for m in re.findall(r'(?:href|src)="([^"]+)"', html):
            if m.startswith(("http", "tel:", "mailto:", "#", "data:")):
                continue
            total += 1
            tgt = urljoin(base, m.split("#")[0])
            if not tgt or tgt == "/":
                tgt = "/index.html"
            elif tgt.endswith("/"):
                tgt += "index.html"
            fs = os.path.join(ROOT, tgt.lstrip("/").replace("/", SEP))
            if not os.path.exists(fs):
                bad.append((rel, m, tgt))

print(f"페이지 {pages}개 / 내부링크 {total}개 / 깨진 링크 {len(bad)}개")
for r, m, t in bad[:30]:
    print(f"  X  {r}  ->  {m}   ({t})")
sys.exit(1 if bad else 0)
