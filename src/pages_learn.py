"""Learn pages: meaning, numbers, slang, records, guides."""
from layout import render, page_hero, ad, LEAD_BAND, BASE

SRC = {
    "wiki": ("Wikipedia — Chinese numerology", "https://en.wikipedia.org/wiki/Chinese_numerology"),
    "bloomberg": ("Bloomberg — Hong Kong auctions 'lucky' plate for $2.3 million (2016)", "https://www.bloomberg.com/news/articles/2016-02-22/hong-kong-just-auctioned-off-a-lucky-license-plate-number-for-2-3-million"),
    "scmp": ("SCMP — 'Lucky' phone number sells for US$50,000 in China, but it's not a record", "https://www.scmp.com/news/china/article/3005561/lucky-phone-number-sells-us50000-china-its-not-record"),
    "namepros": ("NamePros — Should You Buy 6N .COMs? (2016)", "https://www.namepros.com/blog/should-you-buy-6n-coms-a-guide-to-this-rapidly-expanding-market.916489/"),
    "dnw": ("Domain Name Wire — Making a fortune with 88.com (2020)", "https://domainnamewire.com/2020/07/28/making-a-fortune-with-88-com/"),
    "nbc": ("NBC News — Man pays $215,000 for lucky phone number", "https://www.nbcnews.com/news/amp/wbna6421318"),
    "vice": ("VICE — 'Lucky' phone number sold for over $300,000 at a Chinese online auction", "https://www.vice.com/en/article/lucky-phone-number-sold-300000-dollars-china-auction-numerology/"),
    "fineness": ("Wikipedia — Fineness (gold purity)", "https://en.wikipedia.org/wiki/Fineness"),
    "hktd": ("Hong Kong Transport Department — Vehicle registration marks", "https://www.td.gov.hk/en/public_services/vehicle_registration_mark/index.html"),
    "cambridge": ("Cambridge Network — The meaning of numbers in Chinese culture", "https://www.cambridgenetwork.co.uk/news/whats-your-number-meaning-numbers-chinese-culture"),
    "yisheng": ("Wikipedia — Yisheng Yishi (1314)", "https://en.wikipedia.org/wiki/Yisheng_Yishi"),
    "ltl": ("LTL Mandarin School — Lucky numbers in Chinese", "https://ltl-school.com/lucky-numbers-chinese/"),
}


def sources(*keys):
    return '<div class="sources"><h3>Sources</h3><ul>' + "".join(
        f'<li><a href="{SRC[k][1]}" target="_blank" rel="noopener nofollow">{SRC[k][0]}</a></li>' for k in keys) + "</ul></div>"


def meaning():
    body = page_hero("The Meaning of 579999 (我妻久久久久)", "What 5·7·9999 sounds like in Mandarin and Cantonese, why 9999 is one of the most prized endings in Chinese culture, and where the number shows up in money, love and business.", "Number profile", [(None, "Meaning of 579999")]) + f"""
<section class="section"><div class="wrap article">
 <div class="toc"><b>On this page</b><ol><li><a href="#read">How to read 579999</a></li><li><a href="#digits">Digit by digit</a></li><li><a href="#canto">The Cantonese caveat</a></li><li><a href="#economy">579999 in the economy</a></li><li><a href="#people">579999 in people's lives</a></li><li><a href="#score">Score</a></li></ol></div>
 <h2 id="read">How to read 579999</h2>
 <p>Chinese numerology works by <b>homophones</b>: a digit "means" whatever word it sounds like. Read aloud in Mandarin, 5-7-9-9-9-9 is <b>wǔ qī jiǔ jiǔ jiǔ jiǔ</b>. Swap each digit for its sound-alike and you get two natural readings:</p>
 <div class="grid g2">
  <div class="card"><h3>我妻久久久久</h3><p><b>wǒ qī jiǔjiǔ jiǔjiǔ</b>: "My wife, forever and ever". A love and devotion reading, in the family of 520 (我爱你) and 1314 (一生一世).</p></div>
  <div class="card"><h3>吾起久久久久</h3><p><b>wú qǐ jiǔjiǔ jiǔjiǔ</b>: "I rise, and it lasts forever". An ambition and enduring-success reading, suited to brands and businesses.</p></div>
 </div>
 <blockquote>Honest note: 579999 is not a fixed idiom like 1314. Its meaning is built from widely recognised digit homophones, which is exactly how most lucky numbers get their meaning.</blockquote>
 <h2 id="digits">Digit by digit</h2>
 <div class="table-wrap"><table><tr><th>Digit</th><th>Mandarin</th><th>Sounds like</th><th>Reading</th></tr>
 <tr><td class="num">5</td><td>五 wǔ</td><td>我 / 吾 (I, me) · 无 (without)</td><td>Self. It is also the number of the Five Elements, balance and completeness.</td></tr>
 <tr><td class="num">7</td><td>七 qī</td><td>妻 (wife) · 起 (rise) · 气 (vital energy)</td><td>Partnership or ascent. The reading depends on context.</td></tr>
 <tr><td class="num">9999</td><td>九九九九 jiǔ×4</td><td>久久久久 (long, long-lasting)</td><td>Eternity. Nine is the highest single digit and was historically tied to the Emperor.</td></tr></table></div>
 <h2 id="canto">The Cantonese caveat</h2>
 <p>In Cantonese (Hong Kong, Guangdong, much of the diaspora), 5 (ng5) can sound like 唔 ("not"), and both 7 and 9 have vulgar slang senses. Cantonese buyers therefore read 579999 less romantically, and our appraiser scores it lower in Cantonese. It is still a strong number there: 9 is also heard as 久 ("lasting") and 够 ("enough"), and a four-digit repeat is valued as a <i>pattern</i> in every dialect.</p>
 <h2 id="economy">579999 in the Chinese economy</h2>
 <ul>
  <li><b>Gold:</b> "9999" is stamped on 99.99%-pure ("four nines") gold, the purity grade favoured for bullion and Chinese 足金/千足金 jewellery. To a Chinese buyer, 9999 already suggests <i>pure and valuable</i>.</li>
  <li><b>Phone numbers:</b> numbers ending in AAAA are the top tier on carrier and court-auction platforms. A number ending in five 5s went for more than 30× its opening bid in 2019.</li>
  <li><b>Numeric domains:</b> 579999 contains <b>no 0 and no 4</b>, so it belongs to the 262,144-combination "premium 6N .com" class that Chinese domain investors bought up in 2015–16.</li>
  <li><b>Plates and prices:</b> repeating-9 endings are sought after for car plates and used in shop prices meant to suggest durability.</li>
 </ul>
 <h2 id="people">579999 in people's lives</h2>
 <ul>
  <li><b>Weddings:</b> 9 = 久 is a wedding favourite (99 or 999 roses; red envelopes of 999 or 3399 长长久久). 57 + 9999 reads as a vow.</li>
  <li><b>Anniversaries and gifts:</b> numbers as coded messages (520, 1314, 5201314) are everyday romantic shorthand online.</li>
  <li><b>Business:</b> "I rise, lasting forever" is a founder's motto. Numeric brands like 58.com and 360 show how Chinese consumers embrace number names.</li>
 </ul>
 <h2 id="score">Score</h2>
 <p>Run it yourself: <a class="btn btn-red" href="appraise.html?n=579999">Appraise 579999 →</a></p>
 {sources("wiki", "scmp", "namepros", "fineness", "yisheng")}
</div></section>
{ad()}
{LEAD_BAND}
"""
    ld = [{"@context": "https://schema.org", "@type": "Article", "headline": "The Meaning of 579999 (我妻久久久久)", "author": {"@type": "Organization", "name": "579999.com"}, "publisher": {"@type": "Organization", "name": "579999.com"}, "datePublished": "2026-09-30", "mainEntityOfPage": f"{BASE}/meaning-579999.html"}]
    return render("meaning-579999.html", "579999 Meaning in Chinese — 我妻久久久久 'My Wife, Forever' & 9999 Explained",
                  "What does 579999 mean in Chinese? Digit-by-digit homophones (我妻久久久久 / 吾起久久久久), the Cantonese caveat, and 9999 in gold, phone numbers and numeric domains.", body, ld=ld, og_type="article")


def numbers():
    body = page_hero("Chinese Number Meanings: 0–9 &amp; Lucky Combinations", "Every digit's Mandarin and Cantonese sound-alike, whether it is lucky or not, and the combinations that matter most.", "Reference", [(None, "Digits 0–9")]) + f"""
<section class="section"><div class="wrap">
 <div class="table-wrap"><table id="digit-table"><thead><tr><th>Digit</th><th>Chinese</th><th>Verdict</th><th>Meaning</th></tr></thead><tbody></tbody></table></div>
</div></section>
{ad()}
<section class="section alt"><div class="wrap article">
 <h2>The big picture</h2>
 <ul>
  <li><b>Most loved:</b> 8 (发, prosper), 6 (流/禄, smooth, fortune), 9 (久, lasting), 2 (pairs).</li>
  <li><b>Most avoided:</b> 4 (死, death). Buildings in parts of Asia skip floors 4, 14 and 24.</li>
  <li><b>Depends on context:</b> 3, 5 and 7, whose meaning changes with the dialect and the digits around them.</li>
  <li><b>Endings matter most:</b> buyers read the last 2–4 digits first. That is why 579999 or xxx8888 carry a premium.</li>
 </ul>
 <h2>Famous combinations</h2>
 <p>168 一路发 (prosper all the way) · 518 我要发 (I will prosper) · 520 我爱你 (I love you) · 1314 一生一世 (a lifetime) · 3344 生生世世 (forever) · 3399 长长久久 (long-lasting) · 666 溜 (awesome) · 88 发发 / bye-bye · 250 二百五 (idiot) · 748 去死吧 (go die).</p>
 <p><a class="btn btn-ghost" href="slang.html">Browse the full slang dictionary →</a></p>
 {sources("wiki", "cambridge", "ltl")}
</div></section>
"""
    return render("numbers.html", "Chinese Number Meanings 0–9 — Lucky & Unlucky Numbers Explained",
                  "Meaning of every Chinese number 0–9 in Mandarin and Cantonese: why 8 is lucky, 4 is unlucky, 9 means forever, plus famous combinations like 168, 520 and 1314.", body)


def slang():
    cats = "".join(f'<button type="button" class="chip" data-cat="{c}" data-target="#slang-table">{t}</button>' for c, t in [("all", "All"), ("love", "❤️ Love"), ("wealth", "💰 Wealth"), ("luck", "🍀 Luck"), ("slang", "💬 Chat & insults")])
    body = page_hero("Chinese Number Slang Dictionary", "47+ number codes used in Chinese chat, love notes, shop prices and red envelopes, with Chinese characters, pinyin and meaning. Filter, search or decode your own.", "Reference", [(None, "Number Slang")]) + f"""
<section class="section"><div class="wrap">
 <div class="row" style="margin-bottom:14px"><input data-filter="#slang-table" placeholder="Search a code or meaning, e.g. love, 520, bye" aria-label="Search slang"></div>
 <div class="chip-list" style="margin-bottom:14px">{cats}</div>
 <div class="table-wrap"><table id="slang-table"><thead><tr><th>Code</th><th>Chinese</th><th>Reading</th><th>Meaning</th><th>Use?</th></tr></thead><tbody></tbody></table></div>
 <p class="muted mt">Missing a code? <a href="contact.html">Suggest it</a>. Contributors are credited, and the best submissions enter our monthly <a href="contests.html">contest</a>.</p>
</div></section>
{ad()}
<section class="section alt"><div class="wrap article">
 <h2>Etiquette tips</h2>
 <ul><li>Love codes (520, 1314, 5201314) are sweet and safe to use.</li><li>Avoid 250, 38, 748 and 514 in anything serious. They are insults or morbid.</li><li>88 in chat means "bye-bye", but in prices it means "double prosperity".</li><li>Before giving money in red envelopes, avoid amounts containing 4.</li></ul>
 <p><a class="btn btn-red" href="decoder.html">Decode a number →</a></p>
</div></section>
"""
    return render("slang.html", "Chinese Number Slang Dictionary — 520, 1314, 666, 88, 250 & More",
                  "Complete Chinese number slang list with characters, pinyin and meanings: 520 I love you, 1314 forever, 666 awesome, 88 bye, 250 idiot, 748 go die. Searchable and filterable.", body)


def records():
    rows = [
        ("Plate", "28", "HK$18.1M (≈US$2.3M)", "Hong Kong, 2016", "Cantonese 'easy to prosper'", "bloomberg"),
        ("Plate", "18", "≈US$2.1M (earlier record)", "Hong Kong", "'will prosper'", "bloomberg"),
        ("Plate", "9", "≈US$1.7M", "Hong Kong", "'lasting'; the Emperor's number", "bloomberg"),
        ("Phone", "+86 28 8888 8888", "CN¥2.33M (≈US$280k)", "Chengdu, 2003", "Bought by Sichuan Airlines", "wiki"),
        ("Phone", "Lucky number (reported)", "US$300,000+", "China, online auction", "Reported by VICE", "vice"),
        ("Phone", "Lucky number (reported)", "US$215,000", "China, 2004", "Reported by NBC News", "nbc"),
        ("Phone", "…55555 ending", "CN¥350,000+ (≈US$52k)", "China, 2019 (Alibaba court auction)", "Over 30× its opening bid", "scmp"),
        ("Email / domain", "88888@88.com", "US$24,000", "88.com, 2020", "Numeric vanity email address", "dnw"),
        ("Domain", "888733.com", "£2,808", "6N .com market, 2016", "Double-8 start, no 4", "namepros"),
    ]
    trs = "".join(f'<tr><td>{a}</td><td class="num">{b}</td><td><b>{c}</b></td><td>{d}</td><td>{e}</td><td><a href="{SRC[s][1]}" target="_blank" rel="noopener nofollow">source</a></td></tr>' for a, b, c, d, e, s in rows)
    body = page_hero("Lucky Number Record Sales — Hall of Fame", "The most expensive lucky license plates, phone numbers and numeric names on record, each linked to its source.", "Market data", [(None, "Record Sales")]) + f"""
<section class="section"><div class="wrap">
 <div class="row" style="margin-bottom:14px"><input data-filter="#rec-table" placeholder="Filter: plate, phone, domain, Hong Kong…" aria-label="Filter records"></div>
 <div class="table-wrap"><table id="rec-table"><thead><tr><th>Type</th><th>Number</th><th>Price</th><th>Where / when</th><th>Why</th><th></th></tr></thead><tbody>{trs}</tbody></table></div>
 <p class="muted mt">Currency conversions are approximate, as reported at the time. Know of a verified sale we are missing? <a href="contact.html">Send it in</a> with a source link.</p>
</div></section>
{ad()}
<section class="section alt"><div class="wrap article">
 <h2>What the records teach sellers</h2>
 <ol><li><b>Short beats long:</b> single and double-digit plates set the records.</li><li><b>Meaning plus pattern:</b> 28 wins on meaning, 8888 8888 on pattern. The best numbers have both.</li><li><b>Auctions create spikes:</b> competitive bidding can multiply the opening price 30× in minutes.</li><li><b>No 4:</b> the 4-free premium is consistent across plates, phones and domains.</li></ol>
 <p><a class="btn btn-red" href="get-matched.html?goal=sell">Sell your number →</a> <a class="btn btn-ghost" href="guide-sell-a-lucky-number.html">Read the seller's guide</a></p>
</div></section>
"""
    return render("records.html", "Most Expensive Lucky Numbers Ever Sold — Plates, Phone Numbers & Domains",
                  "Record prices for lucky numbers: Hong Kong plate 28 for HK$18.1M, phone number 8888 8888 for CN¥2.33M, numeric domains and more, with sources.", body)


GUIDES = [
    ("guide-why-9999-means-forever.html", "Why 9999 Means 'Forever' in Chinese Culture", "Nine, longevity, the Emperor and gold: why four nines are one of the most prized endings.", "♾️"),
    ("guide-numeric-domains-china.html", "Why Chinese Businesses Love Numeric Domains", "58.com, 163.com, 360 and the 6N .com market: what numeric names are worth and why.", "🌐"),
    ("guide-lucky-license-plates.html", "Lucky License Plates: How the Auctions Work", "From Hong Kong's HK$18.1M '28' to personalised marks: what drives plate prices.", "🚗"),
    ("guide-lucky-phone-numbers.html", "Lucky Phone Numbers: How Buyers Price 8888 and 9999", "Why the last four digits matter most, and how to buy or sell a vanity number safely.", "📱"),
    ("guide-9999-gold.html", "9999 Gold: What 'Four Nines' Purity Means", "999.9 fine gold, 足金 and 千足金 marks, and why buyers look for 9999.", "🥇"),
    ("guide-mandarin-vs-cantonese-numbers.html", "Mandarin vs Cantonese: Same Number, Different Luck", "Why 3, 5, 7 and 9 change meaning between dialects, and what that does to prices.", "🗣️"),
    ("guide-sell-a-lucky-number.html", "How to Sell a Lucky Number for Top Dollar", "Pricing, platforms, transfer rules and pitfalls for phones, plates and domains.", "💰"),
    ("guide-red-envelope-amounts.html", "Lucky Red Envelope (Hongbao) Amounts", "How much to give for weddings, New Year and birthdays, and which numbers to avoid.", "🧧"),
]


def guides_index():
    cards = "".join(f'<a class="card" href="{h}"><div class="ico">{i}</div><h3>{t}</h3><p>{d}</p></a>' for h, t, d, i in GUIDES)
    body = page_hero("Guides &amp; Articles", "In-depth, sourced guides to the culture and the economics of lucky numbers.", "Learn", [(None, "Guides")]) + f"""
<section class="section"><div class="wrap"><div class="grid g3">{cards}</div></div></section>{ad()}{LEAD_BAND}"""
    return render("guides.html", "Guides — Chinese Lucky Numbers, Plates, Phone Numbers & Numeric Domains",
                  "Sourced guides on Chinese lucky numbers: 9999 meaning, numeric domains, lucky plates and phone numbers, gold purity, dialect differences and how to sell a lucky number.", body)


def article(path, title, desc, eyebrow, content, src_keys, related=None):
    rel = related or [g for g in GUIDES if g[0] != path][:3]
    relc = "".join(f'<a class="card" href="{h}"><div class="ico">{i}</div><h3>{t}</h3></a>' for h, t, d, i in rel)
    body = page_hero(title, desc, eyebrow, [("guides.html", "Guides"), (None, title)]) + f"""
<section class="section"><div class="wrap article">
 <p class="meta">By the 579999.com editorial team · Updated September 2026 · <button class="chip" data-share="{title}">Share</button></p>
 {content}
 {sources(*src_keys) if src_keys else ""}
 <div class="cta-band mt"><div><h3>Have a lucky number to buy, sell or value?</h3><p>Free first review from our Lucky Number Exchange desk.</p></div><div><a class="btn btn-gold btn-lg btn-block" href="get-matched.html">Get matched →</a></div></div>
</div></section>
{ad()}
<section class="section alt"><div class="wrap"><h2>Keep reading</h2><div class="grid g3">{relc}</div></div></section>
"""
    ld = [{"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc, "author": {"@type": "Organization", "name": "579999.com"}, "publisher": {"@type": "Organization", "name": "579999.com"}, "datePublished": "2026-09-30", "mainEntityOfPage": f"{BASE}/{path}"}]
    return render(path, title, desc, body, active="guides.html", ld=ld, og_type="article")


def guide_pages():
    out = {}
    out["guide-why-9999-means-forever.html"] = lambda: article(
        "guide-why-9999-means-forever.html", "Why 9999 Means 'Forever' in Chinese Culture",
        "Nine sounds like 久 (lasting). Here is how that single homophone turned 9999 into one of the most prized number endings in the Chinese-speaking world.", "Guide",
        """
<h2>The sound: 九 = 久</h2><p>In Mandarin, nine (九, jiǔ) is a near-perfect homophone of 久 (jiǔ), "long-lasting". Repeating it intensifies the meaning: 99 久久 is "long, long", and 9999 久久久久 is "forever and ever". That is why nines appear everywhere couples want permanence: 99 or 999 roses, wedding dates with 9s, red-envelope amounts like 999 or 3399 (长长久久).</p>
<h2>The Emperor's number</h2><p>Nine is the highest single digit, and in imperial China it was associated with the Emperor, who wore robes with nine dragons. Palace architecture is full of nines, such as the rows of door studs on Forbidden City gates. That history gives 9 a sense of supreme and enduring power.</p>
<h2>The gold connection</h2><p>"9999" is also the fineness mark for 99.99% pure gold ("four nines"). In Chinese jewellery shops, high-purity gold is marked 足金 or 千足金, and bullion is traded at the 99.99 grade. So the digits 9999 carry two positive signals at once: <i>forever</i> and <i>pure value</i>.</p>
<h2>What it means for prices</h2><ul><li>Phone numbers and plates ending in 9999 fall into the top AAAA pattern tier.</li><li>Businesses that sell durability (insurance, jewellery, wedding services) favour 9-heavy numbers.</li><li>Dialect matters: in Cantonese, 9 can also carry slang meanings, so Hong Kong buyers weigh 8 more heavily than 9.</li></ul>
<p><a class="btn btn-red" href="appraise.html?n=9999">Score a 9999 number →</a></p>""", ["wiki", "fineness", "cambridge"])
    out["guide-numeric-domains-china.html"] = lambda: article(
        "guide-numeric-domains-china.html", "Why Chinese Businesses Love Numeric Domains",
        "Some of China's biggest internet brands use numbers. Here is why, and what the 3N–6N .com market tells domain owners.", "Guide",
        """
<h2>Numbers beat letters for many Chinese users</h2><p>Latin-letter brand names can be hard to remember for users who think in characters, and pinyin spellings are ambiguous. Digits are universal. Many of China's best-known web brands therefore picked number domains: <b>58.com</b> (classifieds; 五八 echoes 我发 "I prosper"), <b>163.com</b> (NetEase mail) and <b>360</b> (Qihoo 360 security). Reporting from Domain Name Wire notes that several of China's top internet companies use numeric domains.</p>
<h2>The 6N .com gold rush</h2><p>In 2015–16, Chinese investors bought up six-digit .com names (6N). NamePros counted <b>262,144 "premium" 6N combinations</b> (those without 0 or 4) and reported prices rising from about $160 for random combos to $1,000–$2,800+ for strong patterns, like the reported £2,808 sale of 888733.com.</p>
<h2>What makes a numeric domain valuable</h2><ol><li><b>Length:</b> 2N and 3N are ultra-premium; 4N and 5N are liquid; 6N is a volume market.</li><li><b>No 4</b>, and ideally no 0 (Chinese investors call these "CHIP" or premium-digit names).</li><li><b>Patterns:</b> repeats (AAAA), AABB, ABAB and the famous codes 168, 518, 520.</li><li><b>Extension:</b> .com leads, followed by .cn and .net.</li></ol>
<h2>Case study: 579999.com</h2><p>Six digits, no 0, no 4, a quad-9 ending and a readable phrase (我妻久久久久). Our appraiser places it in the Elite tier.</p>
<p><a class="btn btn-red" href="get-matched.html?goal=domain">Buy or sell a numeric domain →</a></p>""", ["dnw", "namepros"])
    out["guide-lucky-license-plates.html"] = lambda: article(
        "guide-lucky-license-plates.html", "Lucky License Plates: How the Auctions Work",
        "Hong Kong's government auctions have produced some of the highest prices ever paid for a number. Here is what drives them.", "Guide",
        """
<h2>The records</h2><p>In 2016 Hong Kong's plate <b>28</b> sold for <b>HK$18.1 million (≈US$2.3M)</b>. In Cantonese, 28 sounds like "easy to prosper". Bloomberg noted earlier records of about US$2.1M for <b>18</b> and US$1.7M for <b>9</b>.</p>
<h2>How Hong Kong's system works</h2><p>The Transport Department runs auctions for "special" registration marks, both in person (paddle auctions) and online. It also sells personalised marks of up to 8 characters. Proceeds go to charity, which is part of the appeal for bidders.</p>
<h2>What drives value</h2><ul><li><b>Brevity:</b> 1–2 characters is the pinnacle.</li><li><b>Meaning:</b> 8, 28, 168 and 88 (prosperity); 9 (lasting).</li><li><b>Pattern:</b> 8888, 9999, AABB.</li><li><b>No 4.</b></li><li><b>Transferability:</b> rules differ by jurisdiction. Always check the official authority.</li></ul>
<h2>Outside Hong Kong</h2><p>Mainland cities, Singapore, Malaysia, the UK and many US states sell or auction special plates, and dealers such as UK plate brokers actively market "lucky Chinese numbers" to diaspora buyers.</p>
<p><a class="btn btn-red" href="get-matched.html?goal=buy&type=plate">Find a lucky plate →</a></p>""", ["bloomberg", "hktd"])
    out["guide-lucky-phone-numbers.html"] = lambda: article(
        "guide-lucky-phone-numbers.html", "Lucky Phone Numbers: How Buyers Price 8888 and 9999",
        "Why a phone number can be worth more than a car, and what to check before you buy or sell one.", "Guide",
        """
<h2>Record sales</h2><p>In 2003 Sichuan Airlines paid <b>CN¥2.33 million</b> for +86 28 8888 8888. In 2019 a number ending in five 5s sold at an Alibaba court auction for more than CN¥350,000, over 30× its opening bid, after 107 bids in 24 hours (SCMP).</p>
<h2>How buyers read a number</h2><ol><li><b>Last 4 digits first.</b> AAAA endings (8888, 9999, 6666) are the top tier.</li><li><b>Then the last 8:</b> AABB, ABAB and codes like 168 or 518 add value.</li><li><b>Count the 4s.</b> Each one lowers demand.</li><li><b>Carrier and region:</b> a premium carrier in a major city is worth more.</li></ol>
<h2>Buying or selling safely</h2><ul><li>Transfer ownership through the carrier's official process, never by just handing over a SIM.</li><li>Use escrow for high-value deals.</li><li>Check local rules: some carriers and countries forbid resale of numbers.</li></ul>
<p><a class="btn btn-red" href="generator.html">Generate lucky numbers →</a> <a class="btn btn-ghost" href="get-matched.html?goal=sell&type=phone">Sell a number</a></p>""", ["wiki", "scmp", "nbc"])
    out["guide-9999-gold.html"] = lambda: article(
        "guide-9999-gold.html", "9999 Gold: What 'Four Nines' Purity Means",
        "Why the digits 9999 appear on gold bars and jewellery, and how Chinese gold marks relate to them.", "Guide",
        """
<h2>Fineness in plain English</h2><p>Gold purity is measured in parts per thousand ("fineness"). 999.9 fine, often written <b>9999</b> or "four nines", means 99.99% gold. It is the highest common commercial grade, used for many investment bars and coins.</p>
<h2>Chinese gold marks</h2><ul><li><b>足金 (zújīn, "full gold"):</b> commonly used for gold of at least 99.0% purity.</li><li><b>千足金 (qiān zújīn):</b> commonly used for at least 99.9%.</li><li>Jewellery may also be stamped with the numeric fineness (990, 999, 9999).</li></ul>
<p>Retailers and buyers in China are very familiar with these marks, which reinforces 9999 as a symbol of purity and value.</p>
<h2>Why it matters here</h2><p>When 9999 appears in a phone number, domain or brand, Chinese speakers hear 久久久久 ("forever") and also think of <i>pure gold</i>. Few four-digit sequences carry that double meaning.</p>
<blockquote>This guide is educational. It is not investment advice. Check purity and hallmarking rules with an accredited assayer or dealer in your country.</blockquote>""", ["fineness"])
    out["guide-mandarin-vs-cantonese-numbers.html"] = lambda: article(
        "guide-mandarin-vs-cantonese-numbers.html", "Mandarin vs Cantonese: Same Number, Different Luck",
        "Numerology runs on sound, and Mandarin and Cantonese sound different. Here is how that changes what a number is worth.", "Guide",
        """
<h2>The digits that flip</h2><div class="table-wrap"><table><tr><th>Digit</th><th>Mandarin</th><th>Cantonese</th></tr>
<tr><td class="num">3</td><td>三 sān, like 散 "scatter" (mixed)</td><td>saam1, like 生 "life" (good)</td></tr>
<tr><td class="num">5</td><td>五 wǔ, like 我 "me" (neutral)</td><td>ng5, like 唔 "not" (reverses what follows)</td></tr>
<tr><td class="num">7</td><td>七 qī, like 起/妻 "rise / wife"</td><td>cat1, a vulgar slang sense</td></tr>
<tr><td class="num">9</td><td>九 jiǔ, like 久 "lasting" (good)</td><td>gau2, like 久/够 "lasting / enough", with some slang use</td></tr>
<tr><td class="num">2</td><td>二 èr, pairs</td><td>yi6, like 易 "easy" (good)</td></tr></table></div>
<h2>Famous flips</h2><ul><li><b>28</b>: nothing special in Mandarin, but "easy to prosper" in Cantonese. That is why it set a Hong Kong plate record.</li><li><b>54</b>: Mandarin "I die", Cantonese 唔死 "won't die".</li><li><b>13</b>: fine in Cantonese, "silly" in Shanghainese slang.</li></ul>
<h2>Pricing tip</h2><p>Know your buyer's dialect. A number marketed in Hong Kong or Guangzhou should be pitched on Cantonese readings; one sold in Beijing, Shanghai or Taipei on Mandarin. Our appraiser shows both scores.</p>""", ["wiki", "bloomberg"])
    out["guide-sell-a-lucky-number.html"] = lambda: article(
        "guide-sell-a-lucky-number.html", "How to Sell a Lucky Number for Top Dollar",
        "A practical playbook for selling a lucky phone number, plate or numeric domain: price it, present it, find buyers and transfer it safely.", "Seller's guide",
        """
<h2>1. Know what you own</h2><p>Run your number through the <a href="appraise.html">appraiser</a>. Note its pattern tier, hidden codes, count of 4s and dialect scores. Those become your selling points.</p>
<h2>2. Check it is legally transferable</h2><ul><li><b>Phones:</b> carrier transfer-of-ownership rules. Some jurisdictions prohibit resale.</li><li><b>Plates:</b> the plate authority's assignment or transfer process.</li><li><b>Domains:</b> registrar transfer; use an escrow service.</li></ul>
<h2>3. Price with comparables</h2><p>Look at recent sales of the same asset type, market and pattern, not headline records. A human appraisal can find comparables for you.</p>
<h2>4. Tell the story</h2><p>Chinese buyers pay for meaning. Lead with the reading ("我妻久久久久: my wife, forever"), the pattern ("quad-9 ending, no 4") and the use case (wedding gift, business hotline, brand).</p>
<h2>5. Reach the right buyers</h2><p>Diaspora communities, businesses in auspicious-sounding sectors (finance, jewellery, weddings, real estate) and numeric-domain investors. List with our exchange desk and we will match you with buyers.</p>
<h2>6. Close safely</h2><p>Put terms in writing, use escrow, and complete the official transfer before releasing funds.</p>
<p><a class="btn btn-red btn-lg" href="get-matched.html?goal=sell">List my number →</a></p>""", ["scmp", "namepros"])
    out["guide-red-envelope-amounts.html"] = lambda: article(
        "guide-red-envelope-amounts.html", "Lucky Red Envelope (Hongbao) Amounts",
        "How much to put in a red envelope, and which numbers send the right message, for weddings, Chinese New Year and birthdays.", "Guide",
        """
<h2>General rules</h2><ul><li>Use even amounts for happy occasions (好事成双, good things come in pairs).</li><li>Avoid anything with 4.</li><li>Favour 6, 8 and 9 and famous codes.</li><li>Use new, crisp notes.</li></ul>
<h2>Popular amounts by occasion</h2><div class="table-wrap"><table><tr><th>Occasion</th><th>Amounts people like</th><th>Why</th></tr>
<tr><td>Wedding</td><td class="num">520 · 1314 · 3399 · 999</td><td>Love, lifetime, long-lasting</td></tr>
<tr><td>Chinese New Year</td><td class="num">88 · 168 · 888</td><td>Prosperity</td></tr>
<tr><td>Business opening</td><td class="num">168 · 518 · 1688 · 6688</td><td>Prosper all the way</td></tr>
<tr><td>Birthday (elders)</td><td class="num">99 · 999</td><td>Longevity</td></tr></table></div>
<p class="muted">Amounts vary widely by region, relationship and income. The digits matter more than the size.</p>
<p><a class="btn btn-red" href="decoder.html">Decode any amount →</a></p>""", ["wiki", "yisheng"])
    return out


def PAGES():
    p = {"meaning-579999.html": meaning, "numbers.html": numbers, "slang.html": slang, "records.html": records, "guides.html": guides_index}
    p.update(guide_pages())
    return p
