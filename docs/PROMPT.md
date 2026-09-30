# Phase-wise Build Prompt: 579999.com "Lucky Number Exchange"

Use these prompts in order with an AI coding assistant (or hand them to a developer). Each phase is self-contained, and each ends with acceptance criteria. Replace `[OWNER_INBOX]` with the private inbox address. **Never print that address on any page:** assemble it at runtime from an encoded array and use it only inside form-submission code and click handlers.

---

## PHASE 0: Context (paste first, keep in every session)

> You are building **579999.com**, a static, free-hostable (GitHub Pages) website called **"579999 — Lucky Number Exchange"**. The site decodes, values and helps people trade Chinese lucky numbers (phone numbers, license plates, numeric domains, addresses, prices, dates).
> Brand story: 5·7·9999 in Mandarin reads as 我妻久久久久 ("my wife, forever and ever") or 吾起久久久久 ("I rise, lasting forever"). 9999 = 久久久久 (forever) and also marks 99.99% gold. Be honest that it is a homophone reading, not a fixed idiom.
> Tech constraints: plain HTML/CSS/vanilla JS, with no server and no build step required for hosting. A small Python generator (`build.py`) renders shared header and footer into flat `.html` files. All links are relative so the site works both at `username.github.io/579999-com/` and at the custom domain.
> Global rules:
> 1. On top of **every** page, show a bar reading: "Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership", linked to `https://web.works/contact`.
> 2. All forms submit to `[OWNER_INBOX]` via FormSubmit AJAX (`https://formsubmit.co/ajax/<inbox>`). The inbox is decoded in JS at submit time and is never visible in HTML, text or links. Provide a mailto fallback that is also assembled at runtime.
> 3. Avoid any trademark claim on "579999". Include a trademark and copyright disclosure in the footer and on `disclaimer.html`.
> 4. Design: red `#b3121f`, gold `#c9a227`, ink `#1a1512`, rice-paper `#fbf7ef`; Noto Serif SC headings and Inter body; dark mode; mobile-first; WCAG AA contrast.

## PHASE 1: Foundation and design system
> Create `/assets/css/style.css` with CSS variables (light and dark), the layout grid (g2/g3/g4), cards, buttons, tags (good/bad/mix), the tool UI (gauge, digit tiles, meter), tables, FAQ `<details>`, CTA band, multi-step form, lite-YouTube, donation tiers, progress bar, sticky mobile CTA, newsletter toast and cookie notice.
> Create `src/layout.py` with `render(path,title,desc,body,ld)`. It outputs the doctype, SEO meta (title, description, canonical, Open Graph, Twitter), JSON-LD, Google Fonts, the top interest bar, a sticky header with dropdown nav (Tools / Learn / Buy·Sell·Appraise / Community), a dark-mode toggle, a burger menu, the footer (newsletter, 4 link columns, legal note), the sticky mobile CTA, the toast and the cookie bar.
> **Accept when:** no horizontal scroll at 390px, the nav works on touch, and dark mode persists.

## PHASE 2: Number intelligence engine (`assets/js/numlogic.js`)
> Build a dependency-free engine exposing `NUM.analyze(number,type)`, `NUM.generate(opts)`, `NUM.zodiac(date,beforeCNY)`, `DIGITS`, `COMBOS`, `ANIMALS`, `CNY`.
> - Digit table 0–9: characters, pinyin, Mandarin and Cantonese values, tone, meaning.
> - 45+ codes (520, 1314, 5201314, 3344, 3399, 168, 518, 888, 9999, 666, 88, 250, 748, 514, 7456…) with characters, reading, meaning, polarity and category.
> - Score = digit average (last 4 digits weighted 40%) + code bonus or penalty + pattern points. Output Mandarin and Cantonese scores, overall = 65/35, and a verdict.
> - Pattern tiers: Standard, Notable, Premium, Elite, Legendary (AAAA+, AABB, ABAB, palindrome, ascending runs, no-4, 6N no-0/4, strong ending, repeated-4 penalty).
> - Type notes for phone, plate, domain, address, price and date, with sourced reference figures.
> - Generator: never uses 4; supports prefix, length, favourite digits and pattern styles.
> - Zodiac: CNY dates 1960–2030 plus a user override outside that range; element by last digit; yin/yang.
> **Accept when:** 579999 → Elite, 88888888 → Legendary, 4444 → Standard with a very low score, and 5201314 → Lucky.

## PHASE 3: Tool pages
> `appraise.html` (form, gauge result, hidden codes, pattern list, market notes, CTA band to Get Matched with number and type prefilled, share link with `?n=`), `decoder.html` (slang decoder with example chips), `generator.html` (12 results table with a "Source it →" link per row), `zodiac.html` (calculator plus a table for all 12 animals and 2 videos). Put the appraiser in the home hero.
> **Accept when:** each tool works offline and has no console errors.

## PHASE 4: Lead generation desk (`get-matched.html`)
> A 4-step form with a progress bar: (1) goal radio cards (buy, sell, appraise, consult, numeric domain, partnership), (2) asset type, region, number or pattern, details, (3) budget and timeline and how they found us, (4) name, email, WhatsApp/phone, WeChat/LINE, preferred contact, consent, and newsletter opt-in. Add a honeypot, prefill from URL (`goal`, `number`, `type`), trust row, and a "how it works" aside. Put lead CTAs on every tool result, a lead band on most pages, and a sticky mobile CTA.
> **Accept when:** the submission arrives at the inbox as a table and GA4 fires `generate_lead` if GA4 is configured.

## PHASE 5: Content and SEO
> Pages: `meaning-579999.html`, `numbers.html`, `slang.html` (filterable), `records.html` (sourced hall of fame), `guides.html` plus 8 guides (9999 forever, numeric domains in China, license plates, phone numbers, 9999 gold, Mandarin vs Cantonese, how to sell a lucky number, red envelope amounts), `videos.html`, and `faq.html` with FAQPage schema.
> Include Article, BreadcrumbList, WebApplication, Organization and WebSite JSON-LD, `sitemap.xml`, `robots.txt` and the OG image.
> Rule: every market figure links to its source. Never invent records.

## PHASE 6: Monetization
> - **AdSense:** `config.js → adsenseClient`. Slots load only when it is configured; placeholders stay hidden (preview with `?showads=1`). Update `ads.txt`.
> - **YouTube:** click-to-load embeds from youtube-nocookie with verified video IDs, and an optional channel link.
> - **Donations** (`support.html`): tiers $9 / $57 / $99 / $999, provider buttons (PayPal, Stripe, BMAC, Ko-fi, Patreon, GitHub Sponsors) from config, a fundraising progress bar, a use-of-funds breakdown (operations, marketing, hiring, prizes) and a pledge form.
> - **Sponsorship** (`advertise.html`): packages plus a media-kit form, with a link to web.works/contact for site or domain acquisition.
> - **Contests** (`contests.html`): 3 contests, an entry form and an official-rules summary (no purchase necessary).
> - **Hiring** (`careers.html`): 6 roles and an application form.

## PHASE 7: Trust and legal
> `about`, `contact` (form plus a runtime mailto button), `privacy` (FormSubmit, AdSense cookies, opt-out links, GDPR/CCPA/PIPEDA), `terms`, `disclaimer` (trademark disclosure: no claim to "579999", no affiliation; copyright; takedown procedure), and `404`.

## PHASE 8: QA and deploy
> - Automated checks: internal links, no inbox string anywhere in the repo (`grep`), no console errors (Playwright across all pages), 390px scroll width, and a Lighthouse score of at least 90.
> - Deploy: push to `main` of `webworksa1/579999-com` → Settings → Pages → Deploy from branch `main` / root. Optional custom domain: add `CNAME` with `579999.com` and set DNS A records to 185.199.108.153, .109.153, .110.153 and .111.153 (plus `www` CNAME → `webworksa1.github.io`).
> - Post-launch: submit the sitemap in Search Console, apply for AdSense, and confirm the one-time FormSubmit activation email.

## PHASE 9: Growth roadmap
> 1. Programmatic pages for 00–99 and 100–999 (`/n/168.html`) generated from the engine, which creates a large long-tail SEO footprint.
> 2. Embeddable "Lucky Number Checker" widget for backlinks.
> 3. Chinese (简体/繁體) versions with hreflang.
> 4. A paid PDF "Number Destiny Report" ($19–$49) through Stripe Payment Links.
> 5. A live listings board (Google Sheet → JSON) for numbers for sale.
> 6. A lunar almanac lucky-date picker, BaZi-lite and Kua number tools.
> 7. A YouTube Shorts series turning each guide into a 45-second video.
