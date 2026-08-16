# -*- coding: utf-8 -*-
"""사이트맵·robots 생성 —  python _tools/gen_sitemap.py"""
import os, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
DIST = os.path.join(ROOT, "dist")
SITE = "https://bitwave.kr"

PRIORITY = {"": "1.0", "solution": "0.9", "use-cases": "0.8",
            "industries": "0.8", "pricing": "0.7", "contact": "0.7"}


def urls():
    out = []
    for dp, _, fns in os.walk(DIST):
        if "index.html" not in fns:
            continue
        rel = os.path.relpath(dp, DIST).replace(os.sep, "/")
        path = "" if rel == "." else rel + "/"
        out.append(path)
    return sorted(out, key=lambda p: (p.count("/"), p))


def main():
    today = datetime.date.today().isoformat()
    rows = []
    for p in urls():
        top = p.split("/")[0] if p else ""
        rows.append(
            f"  <url><loc>{SITE}/{p}</loc><lastmod>{today}</lastmod>"
            f"<priority>{PRIORITY.get(top, '0.6')}</priority></url>")

    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    with open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)

    robots = (f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    with open(os.path.join(DIST, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)

    print(f"sitemap.xml  {len(rows)}개 URL")
    print("robots.txt   생성")


if __name__ == "__main__":
    main()
