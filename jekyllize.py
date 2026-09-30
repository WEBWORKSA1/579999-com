#!/usr/bin/env python3
"""Emit Jekyll sources (GitHub Pages builds them natively): _layouts/default.html + one small page file per route.
Usage: python3 jekyllize.py [outdir]   (default: repo root)"""
import os, sys, json, html
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "src"))
import layout
captured = {}
_orig = layout.render
def capture(path, title, desc, body, active=None, ld=None, og_type="website", extra_head=""):
    full = title if "579999" in title else f"{title} | 579999.com"
    ldb = "".join(f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>' for b in (ld or []))
    captured[path] = dict(title=full, description=desc, canonical=f"{layout.BASE}/{'' if path == 'index.html' else path}", og_type=og_type, content=ldb + body)
    return ""
import pages_core, pages_learn, pages_community
for m in (pages_core, pages_learn, pages_community):
    m.render = capture
pages = {}; pages.update(pages_core.PAGES); pages.update(pages_learn.PAGES()); pages.update(pages_community.PAGES)
for fn in pages.values(): fn()
out = sys.argv[1] if len(sys.argv) > 1 else ROOT
os.makedirs(os.path.join(out, "_layouts"), exist_ok=True)
lay = _orig("@@PATH@@", "@@TITLE@@", "@@DESC@@", "@@BODY@@", og_type="@@OG@@")
lay = (lay.replace("@@TITLE@@ | 579999.com", "{{ page.title | escape }}").replace("@@DESC@@", "{{ page.description | escape }}")
          .replace(f"{layout.BASE}/@@PATH@@", "{{ page.canonical }}").replace("@@OG@@", "{{ page.og_type }}").replace("@@BODY@@", "{{ content }}"))
assert "@@" not in lay
open(os.path.join(out, "_layouts", "default.html"), "w").write(lay)
for path, d in captured.items():
    fm = "---\nlayout: default\n" + "".join(f"{k}: {json.dumps(d[k], ensure_ascii=False)}\n" for k in ("title", "description", "canonical", "og_type")) + "---\n"
    open(os.path.join(out, path), "w").write(fm + d["content"].strip() + "\n")
import datetime
today = datetime.date.today().isoformat()
prio = {"index.html": "1.0", "appraise.html": "0.9", "get-matched.html": "0.9", "meaning-579999.html": "0.9"}
urls = "".join(f"<url><loc>{d['canonical']}</loc><lastmod>{today}</lastmod><priority>{prio.get(p, '0.7')}</priority></url>" for p, d in sorted(captured.items()) if p != "404.html")
open(os.path.join(out, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
open(os.path.join(out, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {layout.BASE}/sitemap.xml\n")
print(len(captured), "pages")
