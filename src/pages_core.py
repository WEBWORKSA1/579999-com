"""Core pages: home, tools, lead generation."""
from layout import render, page_hero, ad, LEAD_BAND, BASE, NEWSLETTER_FORM

VIDEOS = [
    ("wf13M4MoHS4", "Chinese Lucky and Unlucky Numbers Explained", "Learn Chinese Now"),
    ("sr673iAqLZY", "MEANINGS behind Chinese NUMBERS | What numbers are lucky in Chinese?", "Chinese with Christine"),
    ("QwvlAbisiRc", "Most Lucky and Unlucky Numbers for Chinese People", "Off the Great Wall"),
    ("42OAA04eft4", "Crack China's Number Code: 520 = Love, 666 = Awesome, 555 = Cry!", "Chinese Teacher - Red"),
    ("gXoC6oubwDM", "Slow Chinese - 88, 520, 5201314 in Chinese Meanings", "Everyday Chinese"),
    ("KjrUhgVFINI", "How to Count in Chinese from 0 to 1,000,000,000", "Chinese with LTL"),
    ("efoyHJ1j9jg", "The Order of Zodiac Animals", "HuiChinese会中文"),
    ("bJag2BvLnBY", "The Great Race | Story of the Chinese Zodiac", "Mythology Unleashed"),
]


def video_cards(items):
    return "".join(
        f'<div><div class="vid" data-id="{i}" role="button" aria-label="Play: {t}"></div><div class="vid-title">{t}</div><div class="vid-by">{a} · YouTube</div></div>'
        for i, t, a in items
    )


ORG_LD = {
    "@context": "https://schema.org", "@type": "Organization", "name": "579999.com",
    "url": BASE, "logo": f"{BASE}/assets/img/favicon.svg",
}
SITE_LD = {
    "@context": "https://schema.org", "@type": "WebSite", "name": "579999.com — Lucky Number Exchange",
    "url": BASE,
}

APPRAISER_FORM = """
<form id="appraiser" class="tool" autocomplete="off">
 <label for="num">Enter any number: phone, plate, domain, address, price or date</label>
 <input id="num" name="num" class="num-input" inputmode="numeric" placeholder="e.g. 579999" required>
 <div class="row" style="margin-top:12px">
  <select name="type" aria-label="Number type">
   <option value="any">Any number</option><option value="phone">Phone number</option><option value="plate">License plate</option>
   <option value="domain">Numeric domain</option><option value="address">House / unit number</option><option value="price">Price / gift amount</option><option value="date">Date (e.g. 20260808)</option>
  </select>
  <button class="btn btn-red btn-lg" type="submit">Reveal my luck score</button>
 </div>
 <div class="chip-list" style="margin-top:12px"><span class="muted" style="font-size:.85rem">Try:</span>
  <button type="button" class="chip" data-try="579999">579999</button><button type="button" class="chip" data-try="88888888">88888888</button>
  <button type="button" class="chip" data-try="5201314">5201314</button><button type="button" class="chip" data-try="168168">168168</button><button type="button" class="chip" data-try="4444">4444</button></div>
</form>
"""


def home():
    body = f"""
<section class="hero"><div class="wrap hero-grid">
 <div>
  <span class="eyebrow">Lucky Number Exchange · 吉祥号码</span>
  <div class="bignum" aria-label="579999">579999</div>
  <h1 style="margin-top:10px">Decode, value &amp; trade lucky numbers</h1>
  <p class="lead">In Chinese culture, numbers carry meaning and command market prices. A single plate sold for HK$18.1 million; one phone number went for CN¥2.33 million. Score any number in seconds, learn what it really says, and connect with buyers, sellers and experts.</p>
  <div class="row" style="max-width:520px"><a class="btn btn-red btn-lg" href="#check">Check a number free</a><a class="btn btn-ghost btn-lg" href="get-matched.html">Buy / Sell a number</a></div>
  <div class="hero-stats"><div><b>47+</b><span>number codes decoded</span></div><div><b>0–9</b><span>Mandarin + Cantonese</span></div><div><b>4</b><span>free pro tools</span></div><div><b>US$2.3M</b><span>record plate ('28')</span></div></div>
 </div>
 <div id="check">{APPRAISER_FORM}</div>
</div>
<div class="wrap"><div id="appraiser-out" class="result tool" aria-live="polite"></div></div>
</section>

<section class="section alt"><div class="wrap">
 <div class="section-head"><span class="eyebrow">The number</span><h2>What does 5·7·9999 say?</h2>
 <p class="lead">579999 is built from well-known Mandarin homophones. It is not a fixed idiom, but every Chinese speaker can "hear" it.</p></div>
 <div class="grid g3">
  <div class="card"><div class="ico">5 · 我</div><h3>wǔ → wǒ / wú</h3><p>Five sounds like 我/吾, "I, me". That is why 520 means "I love you". It is also the number of the Five Elements (五行).</p></div>
  <div class="card"><div class="ico">7 · 妻 / 起</div><h3>qī → wife · rise</h3><p>Seven sounds like 妻 ("wife"), 起 ("to rise") and 气 ("vital energy"). With 5 in front, "57" reads as 我妻, "my wife", or 吾起, "I rise".</p></div>
  <div class="card"><div class="ico">9999 · 久久久久</div><h3>jiǔ → forever</h3><p>Nine sounds like 久, "long-lasting". Four in a row is the strongest "forever" pattern, and 9999 is also the stamp on 99.99%-pure gold.</p></div>
 </div>
 <p class="mt"><a class="btn btn-ghost" href="meaning-579999.html">Read the full meaning of 579999 →</a></p>
</div></section>

{ad()}

<section class="section"><div class="wrap">
 <div class="section-head"><span class="eyebrow">Free tools</span><h2>Everything you need to read a number</h2></div>
 <div class="grid g4">
  <a class="card" href="appraise.html"><div class="ico">🧮</div><h3>Lucky Number Appraiser</h3><p>Mandarin and Cantonese luck score, pattern tier and market notes for phones, plates and domains.</p></a>
  <a class="card" href="decoder.html"><div class="ico">🔎</div><h3>Number Code Decoder</h3><p>Translate 520, 1314, 748, 666 and other Chinese number slang instantly.</p></a>
  <a class="card" href="generator.html"><div class="ico">✨</div><h3>Lucky Number Generator</h3><p>Generate 4-free numbers with AAAA, AABB, ABAB and 168-style patterns, then source them.</p></a>
  <a class="card" href="zodiac.html"><div class="ico">🐉</div><h3>Zodiac &amp; Lucky Numbers</h3><p>Find your animal (with the Chinese New Year cut-off) and its traditional lucky numbers.</p></a>
 </div>
</div></section>

{LEAD_BAND}

<section class="section alt"><div class="wrap">
 <div class="section-head"><span class="eyebrow">Why numbers are worth money</span><h2>The lucky-number economy in 4 facts</h2></div>
 <div class="grid g4">
  <div class="card"><div class="kpi">HK$18.1M</div><p>Paid for Hong Kong license plate <b>28</b> (sounds like "easy to prosper" in Cantonese), 2016.</p></div>
  <div class="card"><div class="kpi">CN¥2.33M</div><p>Paid by Sichuan Airlines for the phone number <b>+86 28 8888 8888</b> in 2003.</p></div>
  <div class="card"><div class="kpi">30×</div><p>A phone number ending in five 5s sold for over 350,000 yuan, more than 30× its opening bid (2019).</p></div>
  <div class="card"><div class="kpi">262,144</div><p>Six-digit .com names with no 0 and no 4: the "premium 6N" set that Chinese investors cleared out in 2015–16.</p></div>
 </div>
 <p class="mt"><a href="records.html">See the Record Sales Hall of Fame and sources →</a></p>
</div></section>

<section class="section"><div class="wrap">
 <div class="section-head"><span class="eyebrow">Guides</span><h2>Learn from the experts</h2></div>
 <div class="grid g3">
  <a class="card" href="guide-why-9999-means-forever.html"><div class="ico">♾️</div><h3>Why 9999 means "forever"</h3><p>Nine, longevity, the Emperor, and the gold connection.</p></a>
  <a class="card" href="guide-numeric-domains-china.html"><div class="ico">🌐</div><h3>Why China loves numeric domains</h3><p>58.com, 163.com, 360, and the 6N .com market explained.</p></a>
  <a class="card" href="guide-sell-a-lucky-number.html"><div class="ico">💰</div><h3>How to sell a lucky number</h3><p>Pricing, platforms and pitfalls for phones, plates and domains.</p></a>
 </div>
 <p class="mt"><a class="btn btn-ghost" href="guides.html">All guides →</a></p>
</div></section>

<section class="section alt"><div class="wrap">
 <div class="section-head"><span class="eyebrow">Watch</span><h2>Lucky numbers, explained on video</h2></div>
 <div class="grid g3">{video_cards(VIDEOS[:3])}</div>
 <p class="mt"><a class="btn btn-ghost" href="videos.html">More videos →</a></p>
</div></section>

{ad()}

<section class="section"><div class="wrap grid g3">
 <a class="card" href="contests.html"><div class="ico">🎁</div><h3>Contests &amp; prizes</h3><p>Share your lucky-number story or design, win prizes and get featured.</p></a>
 <a class="card" href="support.html"><div class="ico">❤️</div><h3>Support the project</h3><p>Keep the tools free. Donations fund operations, marketing, new hires and contest prizes.</p></a>
 <a class="card" href="careers.html"><div class="ico">🤝</div><h3>Join the team</h3><p>Bilingual writers, video creators, numerology consultants and deal-makers wanted.</p></a>
</div></section>

<section class="section alt"><div class="wrap center" style="max-width:720px">
 <h2>Get your weekly lucky numbers 🧧</h2><p class="muted">Lucky dates, auction news and rare numbers for sale. One email a week, unsubscribe anytime.</p>
 {NEWSLETTER_FORM}
</div></section>
"""
    return render("index.html", "579999.com — Lucky Number Exchange: Decode, Value & Trade Chinese Lucky Numbers",
                  "Free Chinese lucky number appraiser, number slang decoder, generator and zodiac tools, plus a buy/sell/appraise desk for lucky phone numbers, license plates and numeric domains.",
                  body, ld=[ORG_LD, SITE_LD])


def appraise():
    body = page_hero("Lucky Number Appraiser", "Score any phone number, license plate, numeric domain, address or price on Chinese numerology. You get Mandarin and Cantonese readings, hidden codes, pattern tier and market context.", "Tool · Free", [(None, "Lucky Number Appraiser")]) + f"""
<section class="section"><div class="wrap" style="max-width:900px">
 {APPRAISER_FORM}
 <div id="appraiser-out" class="result tool" aria-live="polite"></div>
</div></section>
{ad()}
<section class="section alt"><div class="wrap article">
 <h2>How the score works</h2>
 <ol>
  <li><b>Digit values:</b> each digit gets a Mandarin and a Cantonese value (8 = 发 prosper; 4 = 死 death). The last four digits count for 40% of the score, because that is how buyers read numbers.</li>
  <li><b>Hidden codes:</b> we scan for 47+ known sequences (168 一路发, 518 我要发, 1314 一生一世, 748 去死吧…). Good codes add points; negative codes subtract.</li>
  <li><b>Pattern tier:</b> repeats (AAA, AAAA), AABB, ABAB, palindromes, ascending runs and "no 4" determine collector appeal: Standard → Notable → Premium → Elite → Legendary.</li>
  <li><b>Overall:</b> Mandarin 65% + Cantonese 35%, reflecting the size of each speaker market.</li>
 </ol>
 <blockquote>The score measures cultural perception, not a guaranteed price. Real value depends on the asset (carrier, plate authority, domain extension), its length, its market and whether a buyer is ready. <a href="get-matched.html?goal=appraise">Request a human appraisal</a>.</blockquote>
 <h2>FAQ</h2>
 <details><summary>Is a number with 4 always bad?</summary><p>Not always. 4 is avoided because it sounds like 死, but some readings (such as 54, which in Cantonese sounds like "won't die") flip it. Most Chinese buyers still pay less for numbers with 4.</p></details>
 <details><summary>Why do Mandarin and Cantonese scores differ?</summary><p>Homophones differ by dialect. 3 sounds like 生 ("life") in Cantonese but 散 ("scatter") in Mandarin, and 7 and 9 have slang meanings in Cantonese. See our <a href="guide-mandarin-vs-cantonese-numbers.html">dialect guide</a>.</p></details>
 <details><summary>Can you tell me what my number is worth in dollars?</summary><p>Yes, through a human appraisal. We look at comparable sales for your asset type and market. <a href="get-matched.html?goal=appraise">Start here</a>.</p></details>
</div></section>
{LEAD_BAND}
"""
    ld = [{"@context": "https://schema.org", "@type": "WebApplication", "name": "Lucky Number Appraiser", "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "url": f"{BASE}/appraise.html"}]
    return render("appraise.html", "Lucky Number Appraiser — Chinese Numerology Score for Phone, Plate & Domain",
                  "Free Chinese lucky number checker: Mandarin & Cantonese luck score, hidden codes like 168 and 1314, pattern tier (AAAA, AABB) and market notes.", body, ld=ld)


def decoder():
    chips = "".join(f'<button type="button" class="chip" data-code="{c}">{c}</button>' for c in ["520", "1314", "5201314", "88", "666", "748", "250", "3344", "7758", "9494", "168", "579999"])
    body = page_hero("Chinese Number Code Decoder", "Type any digits and see the hidden message in Chinese internet slang and homophones: love codes, insults, wealth wishes and chat shorthand.", "Tool · Free", [(None, "Number Code Decoder")]) + f"""
<section class="section"><div class="wrap" style="max-width:900px">
<form id="decoder" class="tool" autocomplete="off">
 <label for="code">Digits to decode</label>
 <input id="code" name="code" class="num-input" inputmode="numeric" placeholder="e.g. 5201314" required>
 <button class="btn btn-red btn-lg btn-block" style="margin-top:12px" type="submit">Decode</button>
 <div class="chip-list" style="margin-top:12px">{chips}</div>
</form>
<div id="decoder-out" class="result tool" aria-live="polite"></div>
</div></section>
{ad()}
<section class="section alt"><div class="wrap article">
 <h2>Why Chinese speakers talk in numbers</h2>
 <p>Mandarin has relatively few syllables, so digits naturally sound like words. Pager users in the 1990s and QQ chat users in the 2000s turned that into a shorthand. 520 (wǔ èr líng) echoes 我爱你 (wǒ ài nǐ, "I love you"), and 88 (bā bā) echoes "bye-bye". Today these codes appear in wedding red envelopes (1314, 3399), shop prices (168, 888) and even official dates: 20 May (5/20) has become an unofficial Valentine's Day.</p>
 <p>Browse the full list in the <a href="slang.html">Number Slang Dictionary</a>, or learn each <a href="numbers.html">digit's meaning</a>.</p>
</div></section>
"""
    return render("decoder.html", "Chinese Number Code Decoder — What Do 520, 1314, 88, 748 Mean?",
                  "Decode Chinese number slang instantly: 520 I love you, 1314 forever, 88 bye-bye, 666 awesome, 748 go away. Free decoder with pinyin and meanings.", body)


def generator():
    fav = "".join(f'<label class="check" style="display:inline-flex;margin-right:12px"><input type="checkbox" name="fav" value="{d}" {"checked" if d in "689" else ""}> {d}</label>' for d in "12356789")
    body = page_hero("Lucky Number Generator", "Generate lucky numbers with no 4, strong endings and famous codes (168, 518, 1314). Pick one, and we can try to source it for you.", "Tool · Free", [(None, "Lucky Number Generator")]) + f"""
<section class="section"><div class="wrap" style="max-width:960px">
<form id="generator" class="tool">
 <div class="form-grid">
  <div><label>Use for</label><select name="type"><option value="phone">Phone number</option><option value="plate">License plate</option><option value="domain">Numeric domain</option><option value="any">PIN / other</option></select></div>
  <div><label>Length</label><select name="length"><option>4</option><option>5</option><option selected>6</option><option>7</option><option>8</option><option>10</option><option>11</option></select></div>
  <div><label>Fixed prefix (optional)</label><input name="prefix" inputmode="numeric" placeholder="e.g. area code 139"></div>
  <div><label>Pattern style</label><select name="style"><option value="mixed">Mixed best</option><option value="tail">Repeating ending (AAAA)</option><option value="aabb">AABB</option><option value="abab">ABAB</option><option value="combo">Famous code (168, 1314…)</option><option value="asc">Rising run (步步高)</option><option value="lucky">Only lucky digits</option></select></div>
  <div class="full"><label>Favourite digits</label>{fav}</div>
 </div>
 <button class="btn btn-red btn-lg btn-block" style="margin-top:14px" type="submit">Generate 12 lucky numbers</button>
</form>
<div id="generator-out" class="result" aria-live="polite" style="margin-top:20px"></div>
</div></section>
{ad()}
{LEAD_BAND}
"""
    return render("generator.html", "Lucky Number Generator — Chinese Lucky Phone, Plate & Domain Numbers",
                  "Generate lucky numbers with no 4, AAAA/AABB/ABAB patterns and codes like 168 and 1314, each with a luck score. Free Chinese lucky number generator.", body)


def zodiac():
    body = page_hero("Chinese Zodiac &amp; Lucky Numbers", "Find your zodiac animal and element, correctly adjusted for the Chinese New Year cut-off, and see its traditional lucky numbers and colours.", "Tool · Free", [(None, "Zodiac & Lucky Numbers")]) + f"""
<section class="section"><div class="wrap" style="max-width:820px">
<form id="zodiac" class="tool">
 <label for="dob">Date of birth</label><input id="dob" type="date" name="dob" required min="1900-01-01" max="2099-12-31">
 <label class="check" style="margin-top:10px"><input type="checkbox" name="before"> I was born in Jan/Feb <i>before</i> that year's Chinese New Year (only needed for years outside 1960–2030)</label>
 <button class="btn btn-red btn-lg btn-block" style="margin-top:12px" type="submit">Find my animal</button>
</form>
<div id="zodiac-out" class="result" aria-live="polite" style="margin-top:20px"></div>
</div></section>
{ad()}
<section class="section alt"><div class="wrap">
 <h2>Lucky numbers for all 12 animals</h2>
 <p class="muted">Lucky numbers and colours as traditionally listed in popular Chinese astrology references. Years shown are Chinese zodiac years (each begins at Chinese New Year, not 1 January).</p>
 <div class="table-wrap"><table id="zodiac-table"><thead><tr><th></th><th>Animal</th><th>Lucky numbers</th><th>Lucky colours</th><th>Years</th></tr></thead><tbody></tbody></table></div>
 <h3 class="mt">Elements by year</h3>
 <p>The element comes from the last digit of the zodiac year: 0–1 Metal, 2–3 Water, 4–5 Wood, 6–7 Fire, 8–9 Earth. Even years are Yang, odd years are Yin.</p>
 <h3>Watch: the Great Race legend</h3>
 <div class="grid g2">{video_cards(VIDEOS[6:8])}</div>
</div></section>
"""
    return render("zodiac.html", "Chinese Zodiac Calculator & Lucky Numbers for All 12 Animals",
                  "Find your Chinese zodiac animal and element with the Chinese New Year cut-off, plus lucky numbers and colours for Rat, Ox, Tiger, Rabbit, Dragon, Snake, Horse, Goat, Monkey, Rooster, Dog and Pig.", body)


def get_matched():
    goals = [
        ("buy", "🛒 Buy a lucky number", "Phone, plate, domain, vanity number"),
        ("sell", "💰 Sell / list my number", "Reach Chinese-culture buyers"),
        ("appraise", "📊 Expert appraisal", "Comparable sales & price range"),
        ("consult", "🧭 Numerology consult", "Business names, dates, addresses"),
        ("domain", "🌐 Numeric domain deal", "Acquire or broker 3N–6N names"),
        ("partner", "🤝 Partnership / bulk", "Dealers, carriers, agencies"),
    ]
    goal_html = "".join(f'<label class="choice"><input type="radio" name="goal" value="{v}" required><span>{t}<small>{s}</small></span></label>' for v, t, s in goals)
    body = page_hero("Buy · Sell · Appraise a Lucky Number", "Tell us in 60 seconds what you want. A specialist reviews every request and replies with next steps. The first review is free, with no obligation.", "Lucky Number Exchange", [(None, "Get Matched")]) + f"""
<section class="section"><div class="wrap grid" style="grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:28px" id="lead">
<form class="tool multistep" data-form="Lead — Get Matched" data-ok="✅ Request received! A specialist will review it and reply within 1–2 business days. Check your inbox (and spam folder)." novalidate>
 <div class="steps"><i></i><i></i><i></i><i></i></div>
 <div class="step"><h3>1. What would you like to do?</h3><div class="choice-grid">{goal_html}</div>
  <button class="btn btn-red btn-lg btn-block mt" type="button" data-next>Continue →</button></div>
 <div class="step"><h3>2. About the number</h3><div class="form-grid">
  <div><label>Asset type</label><select name="asset_type" required><option value="phone">Phone number</option><option value="plate">License plate</option><option value="domain">Numeric domain</option><option value="address">Address / unit</option><option value="any">Other / not sure</option></select></div>
  <div><label>Country / region</label><input name="region" placeholder="e.g. Hong Kong, Canada, Malaysia" required></div>
  <div class="full"><label>The number (or the pattern you want)</label><input name="number" placeholder="e.g. 579999, or 'ending in 8888'" required></div>
  <div class="full"><label>Details (optional)</label><textarea name="details" rows="3" placeholder="Carrier, plate format, domain extension, your story, deadline…"></textarea></div>
 </div><div class="row mt"><button class="btn btn-ghost" type="button" data-prev>← Back</button><button class="btn btn-red" type="button" data-next>Continue →</button></div></div>
 <div class="step"><h3>3. Budget &amp; timing</h3><div class="form-grid">
  <div><label>Budget / asking price (USD)</label><select name="budget" required><option value="">Choose…</option><option>Under $500</option><option>$500 – $2,500</option><option>$2,500 – $10,000</option><option>$10,000 – $50,000</option><option>$50,000+</option><option>Not sure — need appraisal</option></select></div>
  <div><label>Timeline</label><select name="timeline" required><option value="">Choose…</option><option>ASAP (this week)</option><option>Within 30 days</option><option>1–3 months</option><option>Just exploring</option></select></div>
  <div class="full"><label>How did you hear about us?</label><select name="source"><option>Google search</option><option>YouTube</option><option>Social media</option><option>Friend / referral</option><option>Other</option></select></div>
 </div><div class="row mt"><button class="btn btn-ghost" type="button" data-prev>← Back</button><button class="btn btn-red" type="button" data-next>Continue →</button></div></div>
 <div class="step"><h3>4. Where should we send your results?</h3><div class="form-grid">
  <div><label>Full name</label><input name="name" required autocomplete="name"></div>
  <div><label>Email</label><input type="email" name="email" required autocomplete="email"></div>
  <div><label>Phone / WhatsApp (optional)</label><input name="phone" autocomplete="tel"></div>
  <div><label>WeChat / LINE ID (optional)</label><input name="wechat"></div>
  <div class="full"><label>Preferred contact</label><select name="contact_pref"><option>Email</option><option>WhatsApp</option><option>WeChat</option><option>Phone call</option></select></div>
  <div class="full"><label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about my request and accept the <a href="privacy.html">Privacy Policy</a>.</label></div>
  <div class="full"><label class="check"><input type="checkbox" name="newsletter" value="yes" checked> Also send me the free weekly lucky-numbers email.</label></div>
 </div>
 <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off">
 <div class="row mt"><button class="btn btn-ghost" type="button" data-prev>← Back</button><button class="btn btn-red btn-lg" type="submit">Send my request →</button></div>
 <div class="form-msg"></div></div>
 <div class="trust"><span>🔒 Private. Never sold.</span><span>⚡ Reply in 1–2 business days</span><span>💬 English · 中文</span></div>
</form>
<aside>
 <div class="card"><h3>How it works</h3><ol><li><b>Tell us</b> what you want to buy, sell or value.</li><li><b>We research</b> comparable sales, availability and demand.</li><li><b>You decide.</b> You get a clear proposal, price guide or buyer shortlist.</li></ol></div>
 <div class="card mt"><h3>What we handle</h3><p><span class="tag">Vanity phone numbers</span><span class="tag">Personalised plates</span><span class="tag">3N–6N .com domains</span><span class="tag">Business numbers (168, 888)</span><span class="tag">Wedding &amp; launch dates</span><span class="tag">Address feng shui</span></p></div>
 <div class="card mt"><h3>Fair &amp; transparent</h3><p class="muted">The first review is always free. If we broker a sale, commission is agreed in writing before anything happens. Transfers follow your carrier's, plate authority's or registrar's official rules.</p></div>
 <div class="card mt"><h3>Prefer a quick check first?</h3><p><a class="btn btn-ghost btn-block" href="appraise.html">Use the free appraiser</a></p></div>
</aside>
</div></section>
<style>@media (max-width:900px){{#lead{{grid-template-columns:1fr!important}}}}</style>
"""
    return render("get-matched.html", "Buy, Sell or Appraise a Lucky Number — Phone, Plate & Numeric Domain",
                  "Buy or sell lucky phone numbers, personalised plates and numeric domains, or get an expert appraisal. Free first review from the 579999.com Lucky Number Exchange.", body)


def videos():
    body = page_hero("Videos: Chinese Numbers Explained", "Hand-picked videos on lucky and unlucky numbers, number slang and the zodiac legend. Click to play; nothing loads from YouTube until you do.", "Watch", [(None, "Videos")]) + f"""
<section class="section"><div class="wrap"><div class="grid g3">{video_cards(VIDEOS)}</div>
<p class="muted mt">Videos are embedded from YouTube and remain the property of their creators. Creators: want your video featured, or removed? <a href="contact.html">Contact us</a>.</p></div></section>
{ad()}
<section class="section alt"><div class="wrap center" style="max-width:760px"><h2>Make videos about Chinese culture?</h2><p>We feature creators, sponsor episodes and hire editors. <a href="careers.html">Join the team</a> or <a href="advertise.html">partner with us</a>.</p></div></section>
"""
    return render("videos.html", "Videos — Chinese Lucky Numbers, Number Slang & Zodiac Explained",
                  "Watch the best videos on Chinese lucky and unlucky numbers, number slang like 520 and 88, and the zodiac Great Race legend.", body)


PAGES = {"index.html": home, "appraise.html": appraise, "decoder.html": decoder, "generator.html": generator,
         "zodiac.html": zodiac, "get-matched.html": get_matched, "videos.html": videos}
