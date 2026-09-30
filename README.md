# 579999.com — Lucky Number Exchange

Static website that decodes, values and trades Chinese lucky numbers. It runs on the free **GitHub Pages** plan, with no server or database.

**Live:** https://webworksa1.github.io/579999-com/ (custom domain: 579999.com)

## What's inside
- **Tools:** Lucky Number Appraiser, Number Code Decoder, Lucky Number Generator, Zodiac & Lucky Numbers. They run entirely in the browser (`assets/js/numlogic.js`).
- **Lead generation:** `get-matched.html`, a 4-step buy/sell/appraise form. Lead calls to action appear on every tool result and most pages, plus a sticky mobile CTA.
- **Content:** meaning of 579999, digits 0–9, slang dictionary, record sales, 8 guides, videos, FAQ.
- **Monetization:** AdSense slots, YouTube embeds, donations (`support.html`), sponsorship (`advertise.html`), contests, careers.
- **Legal:** privacy, terms, disclaimer with trademark/copyright disclosure.
- **Docs:** `docs/PROMPT.md` (phase-wise build prompt), `docs/RESEARCH.md` (research and competitor audit).

## Go-live checklist
1. **AdSense:** put your `ca-pub-…` ID in `assets/js/config.js` and uncomment the line in `ads.txt`.
2. **Donations:** paste PayPal, Stripe, BMAC, Ko-fi, Patreon or GitHub Sponsors links into `config.js`.
3. **Forms:** submit any form once, then click **Activate** in the one-time FormSubmit email sent to the owner inbox.
4. **Social image (optional):** run `python3 src/make_og.py`, commit `assets/img/og.png`, and add an `og:image` meta tag in `src/layout.py`.
5. **Custom domain (optional):** create a `CNAME` file containing `579999.com` and point DNS A records to 185.199.108.153 / 109.153 / 110.153 / 111.153.

## Edit and rebuild
GitHub Pages builds the site natively with Jekyll: `_layouts/default.html` wraps each page file (front matter + content). Page content lives in `src/*.py`. After editing, run `python3 jekyllize.py` to regenerate the layout, page files, `sitemap.xml` and `robots.txt`, then commit. For a full static preview, `python3 build.py` writes to `dist/`.

**Enable hosting (one time):** repo Settings → Pages → Build and deployment → Source: *Deploy from a branch* → `main` / `/ (root)` → Save.

Contact: all inquiries go through the site forms or https://web.works/contact.
