"""Shared layout for 579999.com static build."""
import json, html

BASE = "https://579999.com"
SITE = "579999.com"
INTEREST_URL = "https://web.works/contact"
VERSION = "1.0.0"

NAV = [
    ("Tools", [
        ("appraise.html", "🧮 Lucky Number Appraiser"),
        ("decoder.html", "🔎 Number Code Decoder"),
        ("generator.html", "✨ Lucky Number Generator"),
        ("zodiac.html", "🐉 Zodiac & Lucky Numbers"),
    ]),
    ("Learn", [
        ("meaning-579999.html", "🧧 What 579999 Means"),
        ("numbers.html", "🔢 Digits 0–9 & Combinations"),
        ("slang.html", "💬 Number Slang Dictionary"),
        ("records.html", "🏆 Record Sales Hall of Fame"),
        ("guides.html", "📚 Guides & Articles"),
        ("videos.html", "▶️ Videos"),
    ]),
    ("get-matched.html", "Buy · Sell · Appraise"),
    ("Community", [
        ("contests.html", "🎁 Contests & Prizes"),
        ("careers.html", "🤝 Join the Team"),
        ("support.html", "❤️ Support / Donate"),
        ("advertise.html", "📣 Advertise & Sponsor"),
        ("about.html", "ℹ️ About"),
        ("contact.html", "✉️ Contact"),
    ]),
]


def nav_html(active):
    out = []
    for item in NAV:
        if isinstance(item[1], list):
            cur = ' aria-current="page"'
            subs = "".join(
                f'<li><a href="{h}"{cur if h == active else ""}>{t}</a></li>' for h, t in item[1]
            )
            out.append(f'<li><button class="dd" type="button">{item[0]} ▾</button><ul class="sub">{subs}</ul></li>')
        else:
            out.append(f'<li><a href="{item[0]}">{item[1]}</a></li>')
    return "".join(out)


def ad(slot="inContent"):
    return f'<div class="ad-slot wrap" data-slot="{slot}" aria-label="Advertisement">Advertisement</div>'


def crumbs(items):
    parts = ['<a href="index.html">Home</a>'] + [
        (f'<a href="{h}">{t}</a>' if h else html.escape(t)) for h, t in items
    ]
    ld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": t, "item": f"{BASE}/{h or ''}"}
            for i, (h, t) in enumerate([("index.html", "Home")] + items)
        ],
    }
    return (
        f'<nav class="crumbs wrap" aria-label="Breadcrumb">{" › ".join(parts)}</nav>'
        f'<script type="application/ld+json">{json.dumps(ld)}</script>'
    )


def page_hero(title, sub, eyebrow=None, crumb=None):
    return (
        f'<section class="page-hero">{crumbs(crumb) if crumb else ""}<div class="wrap" style="padding-top:18px">'
        + (f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else "")
        + f'<h1>{title}</h1><p class="lead" style="max-width:780px">{sub}</p></div></section>'
    )


LEAD_BAND = """
<section class="section"><div class="wrap"><div class="cta-band">
 <div><span class="eyebrow" style="background:#ffffff22;color:#ffe9a8">Lucky Number Exchange</span>
 <h2>Own a lucky number? Want one?</h2>
 <p>Phone numbers, license plates, numeric domains, addresses. Tell us what you have or what you want, and we will appraise it, find buyers or source your perfect number. Free first review.</p></div>
 <div class="grid" style="gap:10px">
  <a class="btn btn-gold btn-lg btn-block" href="get-matched.html?goal=buy">I want to BUY a lucky number</a>
  <a class="btn btn-lg btn-block" style="background:#fff;color:#8e0c17" href="get-matched.html?goal=sell">I want to SELL / list my number</a>
  <a class="btn btn-lg btn-block" style="border-color:#ffffff66;color:#fff" href="get-matched.html?goal=appraise">Get a free expert appraisal</a>
 </div></div></div></section>
"""

NEWSLETTER_FORM = """<form class="newsletter" data-form="Newsletter signup" data-ok="You're in! Watch your inbox for this week's lucky numbers.">
 <input type="email" name="email" required placeholder="Your email for weekly lucky numbers" aria-label="Email">
 <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off">
 <input type="hidden" name="list" value="Weekly Lucky Numbers">
 <button class="btn btn-gold" type="submit">Subscribe free</button><div class="form-msg"></div></form>"""


def footer():
    return f"""
<footer class="site-footer"><div class="wrap">
 <div class="foot-grid">
  <div><a class="brand" href="index.html" style="color:#fff"><span class="logo">久</span><span>579999<small style="color:#a89b8d">Lucky Number Exchange</small></span></a>
   <p style="margin-top:14px">An independent hub to decode, value and trade lucky numbers in Chinese culture. 5·7·9999 reads as 我妻久久久久, "my wife, forever and ever", or "I rise, lasting forever".</p>
   {NEWSLETTER_FORM}
  </div>
  <div><h4>Tools</h4><ul><li><a href="appraise.html">Number Appraiser</a></li><li><a href="decoder.html">Code Decoder</a></li><li><a href="generator.html">Number Generator</a></li><li><a href="zodiac.html">Zodiac Calculator</a></li><li><a href="get-matched.html">Buy / Sell / Appraise</a></li></ul></div>
  <div><h4>Learn</h4><ul><li><a href="meaning-579999.html">Meaning of 579999</a></li><li><a href="numbers.html">Digits 0–9</a></li><li><a href="slang.html">Number Slang</a></li><li><a href="records.html">Record Sales</a></li><li><a href="guides.html">Guides</a></li><li><a href="videos.html">Videos</a></li></ul></div>
  <div><h4>Community</h4><ul><li><a href="contests.html">Contests & Prizes</a></li><li><a href="careers.html">Careers</a></li><li><a href="support.html">Donate / Support</a></li><li><a href="advertise.html">Advertise</a></li></ul></div>
  <div><h4>Company</h4><ul><li><a href="about.html">About</a></li><li><a href="contact.html">Contact</a></li><li><a href="faq.html">FAQ</a></li><li><a href="privacy.html">Privacy</a></li><li><a href="terms.html">Terms</a></li><li><a href="disclaimer.html">Disclaimer & Trademark</a></li></ul></div>
 </div>
 <div class="legal-note">
  <p><b>Trademark & copyright disclosure:</b> "579999" is used on this site only as a domain name and as a descriptive numeric sequence. We claim no trademark rights in the number, and no affiliation with or endorsement by any company, brand, carrier, registry or government body that may use the same or similar digits. All third-party names, trademarks and videos belong to their owners and are used for identification, commentary or embedding under the platforms' terms. Cultural information is for entertainment and education only; it is not financial, legal or investment advice. <a href="disclaimer.html">Full disclosure →</a></p>
  <p>© <span class="year">2026</span> 579999.com · Site content and original tools © 579999.com. All rights reserved. · <a href="{INTEREST_URL}" target="_blank" rel="noopener">Domain / sponsorship / partnership inquiries</a></p>
 </div>
</div></footer>
<div class="sticky-cta"><a class="btn btn-red" href="appraise.html">Check my number</a><a class="btn btn-gold" href="get-matched.html">Buy / Sell</a></div>
<div class="toast" id="toast" role="dialog" aria-label="Newsletter"><button class="x" aria-label="Close">×</button>
 <h3 style="margin-top:0">🧧 Get your weekly lucky numbers</h3><p class="muted">Lucky dates, number-auction news and rare numbers for sale, once a week. Free.</p>{NEWSLETTER_FORM}</div>
<div class="cookie" id="cookie">We use cookies for analytics and ads (Google AdSense) to keep this site free. <a href="privacy.html" style="color:var(--gold)">Privacy</a><br><button class="btn btn-gold" type="button">OK, got it</button></div>
"""


def render(path, title, desc, body, active=None, ld=None, og_type="website", extra_head=""):
    canonical = f"{BASE}/{'' if path == 'index.html' else path}"
    ld_blocks = ""
    for block in (ld or []):
        ld_blocks += f'<script type="application/ld+json">{json.dumps(block, ensure_ascii=False)}</script>'
    full_title = title if "579999" in title else f"{title} | 579999.com"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#b3121f">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="579999.com">
<meta property="og:title" content="{html.escape(full_title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Noto+Serif+SC:wght@600;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css?v={VERSION}">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
{ld_blocks}{extra_head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar" role="note">Contact, if you are interested in this <a href="{INTEREST_URL}" target="_blank" rel="noopener">website / domain name / Sponsorship / Advertisement / Partnership</a></div>
<header class="site-header"><div class="wrap nav">
 <a class="brand" href="index.html" aria-label="579999.com home"><span class="logo">久</span><span>579999<small>Lucky Number Exchange</small></span></a>
 <ul class="menu" id="menu">{nav_html(active or path)}</ul>
 <div class="nav-cta"><button class="icon-btn theme-toggle" type="button" aria-label="Toggle dark mode">☾</button><a class="btn btn-red" href="get-matched.html">Get Matched</a><button class="icon-btn burger" type="button" aria-label="Menu" aria-controls="menu" aria-expanded="false">☰</button></div>
</div></header>
<main id="main">
{ad("top")}
{body}
</main>
{footer()}
<script src="assets/js/config.js?v={VERSION}"></script>
<script src="assets/js/numlogic.js?v={VERSION}"></script>
<script src="assets/js/app.js?v={VERSION}"></script>
</body>
</html>
"""
