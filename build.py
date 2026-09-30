#!/usr/bin/env python3
"""Build 579999.com static site: python3 build.py  (outputs HTML into repo root)."""
import os, sys, datetime
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "src"))
from layout import BASE  # noqa: E402
import pages_core, pages_learn, pages_community  # noqa: E402

pages = {}
pages.update(pages_core.PAGES)
pages.update(pages_learn.PAGES())
pages.update(pages_community.PAGES)

for name, fn in pages.items():
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(fn())

today = datetime.date.today().isoformat()
prio = {"index.html": "1.0", "appraise.html": "0.9", "get-matched.html": "0.9", "meaning-579999.html": "0.9"}
urls = "".join(
    f"<url><loc>{BASE}/{'' if n == 'index.html' else n}</loc><lastmod>{today}</lastmod><priority>{prio.get(n, '0.7')}</priority></url>"
    for n in sorted(pages) if n != "404.html")
open(os.path.join(ROOT, "sitemap.xml"), "w").write(
    f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
print(f"Built {len(pages)} pages")
