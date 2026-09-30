"""Community, monetization and legal pages."""
from layout import render, page_hero, ad, LEAD_BAND, INTEREST_URL, BASE

HONEY = '<input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off">'


def support():
    tiers = [("9", "Supporter", "Keeps the tools online for a week. Name in our thank-you list."),
             ("57", "Patron · 我妻", "Funds a new guide or tool feature. Name on the Supporters page and a patron badge.", True),
             ("99", "Forever Friend · 久久", "Sponsors a monthly contest prize. Shout-out in the newsletter."),
             ("999", "Founding Partner", "Funds a hire or a marketing campaign. Logo on the Supporters page and a strategy call.")]
    tcards = "".join(f'<div class="card tier{" featured" if len(t) > 3 else ""}"><div class="amt">${t[0]}</div><h3>{t[1]}</h3><p class="muted">{t[2]}</p><a class="btn btn-red btn-block" href="#donate" data-amount="{t[0]}">Choose ${t[0]}</a></div>' for t in tiers)
    body = page_hero("Support 579999.com ❤️", "The tools are free for everyone. Your support pays for hosting and operations, promotion and marketing, new team members and contest prizes.", "Donate · Sponsor", [(None, "Support")]) + f"""
<section class="section"><div class="wrap">
 <div class="card"><div class="row" style="align-items:center"><div><h3 style="margin:0">Community fund</h3><p class="muted" style="margin:0">Raised <b class="fr-raised">USD 0</b> of <b class="fr-goal">USD 5,000</b> goal</p></div><div style="flex:2 1 300px"><div class="progress"><i class="fr-bar" style="width:0%"></i></div></div></div></div>
 <h2 class="mt">Choose a level</h2>
 <div class="grid g4">{tcards}</div>
</div></section>
<section class="section alt" id="donate"><div class="wrap">
 <h2>Give in one click</h2><p class="muted">Pick your favourite platform. Payments are processed by the provider; we never see your card details.</p>
 <div class="grid g3">
  <a class="card center" data-donate="paypal"><div class="ico">💳</div><h3>PayPal</h3><p>One-off or monthly</p></a>
  <a class="card center" data-donate="stripe"><div class="ico">💠</div><h3>Card / Apple Pay</h3><p>Secure Stripe checkout</p></a>
  <a class="card center" data-donate="buymeacoffee"><div class="ico">☕</div><h3>Buy Me a Coffee</h3><p>Small thank-yous</p></a>
  <a class="card center" data-donate="kofi"><div class="ico">🍵</div><h3>Ko-fi</h3><p>No platform fee on donations</p></a>
  <a class="card center" data-donate="patreon"><div class="ico">🎗️</div><h3>Patreon</h3><p>Monthly membership perks</p></a>
  <a class="card center" data-donate="githubSponsors"><div class="ico">🐙</div><h3>GitHub Sponsors</h3><p>For developers</p></a>
 </div>
</div></section>
<section class="section"><div class="wrap grid g2">
 <div><h2>Where your money goes</h2>
  <p><b>Operations &amp; tools: 35%</b></p><div class="meter"><i style="width:35%"></i></div>
  <p class="mt"><b>Promotion &amp; marketing: 25%</b></p><div class="meter"><i style="width:25%"></i></div>
  <p class="mt"><b>Hiring writers, editors &amp; developers: 25%</b></p><div class="meter"><i style="width:25%"></i></div>
  <p class="mt"><b>Contests &amp; prizes: 15%</b></p><div class="meter"><i style="width:15%"></i></div>
  <p class="muted mt">We publish a short funding update each quarter in the newsletter.</p>
 </div>
 <form id="pledge" class="tool" data-form="Donation pledge / sponsorship" data-ok="Thank you! We'll email you a secure payment link and your supporter perks within 1–2 business days.">
  <h3>Pledge, sponsor or ask about bank transfer</h3>
  <div class="form-grid">
   <div><label>Name</label><input name="name" required></div><div><label>Email</label><input type="email" name="email" required></div>
   <div><label>Amount (USD)</label><input name="amount" type="number" min="1" placeholder="57"></div>
   <div><label>Purpose</label><select name="purpose"><option>General support / operations</option><option>Promotion &amp; marketing</option><option>Hiring talent</option><option>Contest prize pool</option><option>Corporate sponsorship</option></select></div>
   <div class="full"><label>Message (optional)</label><textarea name="message" rows="3"></textarea></div>
   <div class="full"><label class="check"><input type="checkbox" name="public_credit" value="yes"> Credit my name publicly on the Supporters list</label></div>
  </div>{HONEY}
  <button class="btn btn-red btn-lg btn-block mt" type="submit">Send pledge</button><div class="form-msg"></div>
 </form>
</div></section>
<section class="section alt"><div class="wrap"><h2>Supporters wall</h2><p class="muted">Be the first name here, or your company logo. Founding Partners appear at the top.</p></div></section>
<section class="section"><div class="wrap article"><p class="muted"><small>Donations support an independent website and are not tax-deductible unless a receipt from a registered charity says otherwise. Donations are voluntary and non-refundable except where required by law. Contest prizes are funded from the prize pool as announced in each contest's rules.</small></p></div></section>
"""
    return render("support.html", "Support & Donate — Keep the Lucky Number Tools Free",
                  "Donate to 579999.com to fund operations, promotion, hiring and contest prizes. Choose PayPal, card, Buy Me a Coffee, Ko-fi, Patreon or GitHub Sponsors.", body)


def contests():
    body = page_hero("Contests &amp; Prizes 🎁", "Share your story, show your creativity and test your number knowledge. Winners get prizes, features and bragging rights.", "Community", [(None, "Contests")]) + f"""
<section class="section"><div class="wrap grid g3">
 <div class="card"><span class="tag good">Open</span><h3>📖 My Lucky Number Story</h3><p>Tell us, in up to 500 words, about a number that changed your luck: a wedding date, phone number, plate or address.</p><p><b>Prizes:</b> a featured article, a winner badge and a share of the contest prize pool.</p></div>
 <div class="card"><span class="tag good">Open</span><h3>🎨 Design the 579999 Card</h3><p>Design a greeting card, poster or phone wallpaper around a Chinese number code (520, 1314, 9999…).</p><p><b>Prizes:</b> your design featured site-wide and in the newsletter, plus a prize-pool share.</p></div>
 <div class="card"><span class="tag mix">Monthly</span><h3>🧠 Decode Challenge</h3><p>Each month we post 10 number riddles in the newsletter. First all-correct entry wins.</p><p><b>Prizes:</b> a free expert appraisal and a winner shout-out.</p></div>
</div></section>
<section class="section alt"><div class="wrap grid g2">
 <form class="tool" data-form="Contest entry" data-ok="🎉 Entry received! We'll confirm by email. Good luck!">
  <h3>Submit your entry</h3>
  <div class="form-grid">
   <div><label>Name</label><input name="name" required></div><div><label>Email</label><input type="email" name="email" required></div>
   <div class="full"><label>Contest</label><select name="contest" required><option>My Lucky Number Story</option><option>Design the 579999 Card</option><option>Decode Challenge</option></select></div>
   <div class="full"><label>Your entry (text, or a link to your design: Google Drive, Dropbox, Behance…)</label><textarea name="entry" rows="6" required></textarea></div>
   <div><label>Country</label><input name="country" required></div>
   <div><label>Social handle (optional)</label><input name="social"></div>
   <div class="full"><label class="check"><input type="checkbox" name="rules" value="accepted" required> I am 18+ (or have a parent's permission), the entry is my original work, and I accept the contest rules.</label></div>
  </div>{HONEY}
  <button class="btn btn-red btn-lg btn-block mt" type="submit">Submit entry</button><div class="form-msg"></div>
 </form>
 <div class="article"><h3>Official rules (summary)</h3><ul>
  <li>No purchase or donation is necessary to enter or win. Void where prohibited.</li>
  <li>One entry per person per contest. Entries must be original and must not infringe anyone's rights.</li>
  <li>Prize amounts are announced at the start of each contest round and funded from the <a href="support.html">community prize pool</a> and sponsors.</li>
  <li>A panel judges entries on creativity, cultural insight and presentation. Judges' decisions are final.</li>
  <li>Winners are notified by email and must reply within 14 days. Prizes are non-transferable. Winners are responsible for any taxes.</li>
  <li>By entering, you grant 579999.com a non-exclusive licence to publish your entry with credit. You keep your copyright.</li>
 </ul>
 <h3>Sponsor a contest</h3><p>Put your brand in front of an engaged audience. <a href="advertise.html">See sponsorship options →</a></p></div>
</div></section>
{ad()}
"""
    return render("contests.html", "Contests & Prizes — Lucky Number Stories, Design & Decode Challenges",
                  "Enter 579999.com contests: share your lucky number story, design a Chinese number card or solve the monthly decode challenge to win prizes.", body)


def careers():
    roles = [
        ("Bilingual Content Writer (EN / 中文)", "Remote · Freelance", "Write sourced guides on Chinese culture, numerology and the lucky-number market."),
        ("SEO & Growth Specialist", "Remote · Part-time", "Own keyword strategy, internal linking and programmatic pages for 1000+ numbers."),
        ("YouTube / Shorts Video Editor", "Remote · Per project", "Turn our guides into short videos and Shorts for the channel."),
        ("Numerology &amp; Feng Shui Consultant", "Remote · Partner", "Handle consult and appraisal leads on a revenue-share basis."),
        ("Partnerships &amp; Sales (Commission)", "Remote · Commission", "Sign up plate dealers, number resellers, domain brokers and advertisers."),
        ("Front-end Developer", "Remote · Contract", "Build new tools (lunar calendar, BaZi-lite, embeddable widgets)."),
    ]
    rc = "".join(f'<div class="card"><h3>{t}</h3><p class="muted">{w}</p><p>{d}</p><a class="btn btn-ghost" href="#apply">Apply</a></div>' for t, w, d in roles)
    opts = "".join(f"<option>{t}</option>" for t, _, _ in roles)
    body = page_hero("Join the Team 🤝", "We are building the internet's go-to home for lucky numbers. Help us grow it and get paid, credited or share in the revenue.", "Careers", [(None, "Careers")]) + f"""
<section class="section"><div class="wrap"><div class="grid g3">{rc}</div></div></section>
<section class="section alt" id="apply"><div class="wrap" style="max-width:820px">
 <form class="tool" data-form="Job application" data-ok="Thanks for applying! If there's a fit, we'll reach out within 2 weeks.">
  <h3>Apply or introduce yourself</h3>
  <div class="form-grid">
   <div><label>Full name</label><input name="name" required></div><div><label>Email</label><input type="email" name="email" required></div>
   <div><label>Role</label><select name="role" required>{opts}<option>Other / open application</option></select></div>
   <div><label>Location / time zone</label><input name="location" required></div>
   <div class="full"><label>Portfolio / LinkedIn / CV link</label><input name="portfolio" type="url" placeholder="https://" required></div>
   <div class="full"><label>Why you? (languages, experience, rate)</label><textarea name="pitch" rows="5" required></textarea></div>
  </div>{HONEY}
  <button class="btn btn-red btn-lg btn-block mt" type="submit">Send application</button><div class="form-msg"></div>
 </form>
</div></section>
"""
    return render("careers.html", "Careers — Writers, SEO, Video Editors & Numerology Consultants",
                  "Join 579999.com: remote roles for bilingual content writers, SEO specialists, video editors, numerology consultants, partnerships and developers.", body)


def advertise():
    pk = [("📰 Display Sponsorship", "Premium banner placement across tool and guide pages, alongside Google AdSense."),
          ("🧮 Sponsored Tool", "'Lucky Number Appraiser, presented by YOUR BRAND' on every result."),
          ("✉️ Newsletter Sponsor", "A sponsored slot in the weekly lucky-numbers email."),
          ("🎁 Contest Sponsor", "Fund a prize and get brand exposure across the contest campaign."),
          ("🎯 Lead Partnership", "Receive qualified buy/sell/consult leads in your category and region."),
          ("🔗 Affiliate &amp; Content", "Sponsored guides, reviews and affiliate placements, clearly labelled.")]
    pc = "".join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t, d in pk)
    body = page_hero("Advertise, Sponsor &amp; Partner 📣", "Reach people actively deciding what to pay for a meaningful number: buyers of phones, plates, domains, wedding services, jewellery, feng shui and Chinese-language learning.", "Media kit", [(None, "Advertise")]) + f"""
<section class="section"><div class="wrap"><div class="grid g3">{pc}</div>
<p class="mt">Interested in acquiring or partnering on the whole website or the domain name? Use the <a href="{INTEREST_URL}" target="_blank" rel="noopener">domain &amp; partnership inquiry page</a>.</p></div></section>
<section class="section alt"><div class="wrap" style="max-width:820px">
 <form class="tool" data-form="Advertising / sponsorship inquiry" data-ok="Thanks! We'll send the media kit and availability within 1–2 business days.">
  <h3>Request the media kit</h3>
  <div class="form-grid">
   <div><label>Name</label><input name="name" required></div><div><label>Work email</label><input type="email" name="email" required></div>
   <div><label>Company</label><input name="company" required></div><div><label>Website</label><input name="website" type="url" placeholder="https://"></div>
   <div><label>Interested in</label><select name="package">{"".join(f"<option>{t.split(' ',1)[1]}</option>" for t,_ in pk)}<option>Acquire / partner on the site</option></select></div>
   <div><label>Monthly budget</label><select name="budget"><option>Under $500</option><option>$500–$2,000</option><option>$2,000–$10,000</option><option>$10,000+</option></select></div>
   <div class="full"><label>Goals / target markets</label><textarea name="goals" rows="4"></textarea></div>
  </div>{HONEY}
  <button class="btn btn-red btn-lg btn-block mt" type="submit">Get the media kit</button><div class="form-msg"></div>
 </form>
</div></section>
"""
    return render("advertise.html", "Advertise & Sponsor — Reach Lucky Number Buyers and Chinese-Culture Audiences",
                  "Advertising, sponsorship, lead partnerships and newsletter placements on 579999.com, the Lucky Number Exchange.", body)


def about():
    body = page_hero("About 579999.com", "An independent project that makes the culture and the economics of lucky numbers easy to understand, and easy to trade.", "About", [(None, "About")]) + f"""
<section class="section"><div class="wrap article">
 <h2>Our mission</h2><p>Hundreds of millions of people choose phone numbers, wedding dates, prices and addresses by what the digits say. Yet most information online is scattered, repetitive or unsourced. 579999.com brings it together: free tools, sourced guides and a trusted desk for buying, selling and valuing meaningful numbers.</p>
 <h2>Why "579999"?</h2><p>Because it is a lucky number in its own right: 我妻久久久久, "my wife, forever and ever", or 吾起久久久久, "I rise, lasting forever". Six digits, no 0, no 4, and a quad-9 ending. <a href="meaning-579999.html">Full meaning →</a></p>
 <h2>Editorial standards</h2><ul><li>Market facts are linked to their sources, and records only appear with a citation.</li><li>Cultural readings are labelled as traditional or popular beliefs, not scientific claims.</li><li>Sponsored content is always labelled.</li></ul>
 <h2>What we are not</h2><p>We are not a phone carrier, plate authority, domain registrar, bank or licensed financial adviser. We connect people and provide information; official transfers happen through the proper authorities.</p>
 <p><a class="btn btn-red" href="contact.html">Contact us</a> <a class="btn btn-ghost" href="careers.html">Join the team</a></p>
</div></section>
"""
    return render("about.html", "About 579999.com — The Lucky Number Exchange", "About 579999.com: mission, editorial standards and what the Lucky Number Exchange does.", body)


def contact():
    body = page_hero("Contact Us", "Questions, corrections, partnerships or press. Send us a message and we reply within 1–2 business days.", "Contact", [(None, "Contact")]) + f"""
<section class="section"><div class="wrap grid g2">
 <form class="tool" data-form="Contact" data-ok="Message sent! We'll reply within 1–2 business days.">
  <div class="form-grid">
   <div><label>Name</label><input name="name" required autocomplete="name"></div><div><label>Email</label><input type="email" name="email" required autocomplete="email"></div>
   <div class="full"><label>Topic</label><select name="topic"><option>General question</option><option>Buy / sell / appraise a number</option><option>Advertising / sponsorship</option><option>Partnership</option><option>Website or domain acquisition</option><option>Correction / suggest a number code</option><option>Press</option><option>Video creator</option></select></div>
   <div class="full"><label>Message</label><textarea name="message" rows="6" required></textarea></div>
   <div class="full"><label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to the <a href="privacy.html">Privacy Policy</a>.</label></div>
  </div>{HONEY}
  <button class="btn btn-red btn-lg btn-block mt" type="submit">Send message</button><div class="form-msg"></div>
 </form>
 <div>
  <div class="card"><h3>Faster routes</h3><ul><li>Buying or selling a number? <a href="get-matched.html">Use Get Matched</a></li><li>Advertising? <a href="advertise.html">Media kit</a></li><li>Donations? <a href="support.html">Support page</a></li><li>Jobs? <a href="careers.html">Careers</a></li></ul></div>
  <div class="card mt"><h3>Website, domain, sponsorship or partnership</h3><p>Interested in this website or the 579999.com domain name?</p><a class="btn btn-gold btn-block" href="{INTEREST_URL}" target="_blank" rel="noopener">Contact via web.works →</a></div>
  <div class="card mt"><h3>Prefer email?</h3><p>Open a pre-addressed message in your email app.</p><a class="btn btn-ghost btn-block" href="#contact" data-mail="579999.com inquiry">Email us</a></div>
 </div>
</div></section>
"""
    return render("contact.html", "Contact 579999.com", "Contact the 579999.com team about lucky numbers, advertising, partnerships or the domain.", body)


FAQS = [
    ("What does 579999 mean?", "Read in Mandarin, it sounds like 我妻久久久久 ('my wife, forever and ever') or 吾起久久久久 ('I rise, lasting forever'). 9999 alone means 'forever' because 9 (jiǔ) sounds like 久 (lasting)."),
    ("Why is 8 lucky and 4 unlucky in Chinese?", "8 (bā) sounds like 发 (fā, to prosper), and 4 (sì) sounds like 死 (sǐ, death)."),
    ("Is the luck score scientific?", "No. It measures how Chinese speakers traditionally perceive a number, based on homophones and patterns. It is cultural, not predictive."),
    ("Can you tell me what my number is worth?", "The free appraiser gives a cultural score and pattern tier. For a price range based on comparable sales, request a free human review on Get Matched."),
    ("Do you sell phone numbers or plates directly?", "We connect buyers and sellers and help with research. Official transfers always go through the carrier, plate authority or registrar."),
    ("How is my data used?", "Form submissions are emailed to our team so we can reply. We never sell your data. See the Privacy Policy."),
    ("How can I support the site?", "Donate or sponsor on the Support page, share our tools, or enter a contest."),
]


def faq():
    items = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQS)
    ld = [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}]
    body = page_hero("Frequently Asked Questions", "Quick answers about lucky numbers, our tools and the exchange.", "FAQ", [(None, "FAQ")]) + f'<section class="section"><div class="wrap article">{items}</div></section>{LEAD_BAND}'
    return render("faq.html", "FAQ — Chinese Lucky Numbers & 579999.com", "Answers about the meaning of 579999, lucky and unlucky Chinese numbers, our luck score and the lucky number exchange.", body, ld=ld)


def legal(path, title, html_body):
    body = page_hero(title, "Last updated: 30 September 2026", "Legal", [(None, title)]) + f'<section class="section"><div class="wrap article">{html_body}</div></section>'
    return render(path, title, f"{title} for 579999.com.", body)


def privacy():
    return legal("privacy.html", "Privacy Policy", """
<p>This policy explains what 579999.com ("we") collects and why.</p>
<h2>What we collect</h2><ul><li><b>Information you submit</b> in forms (name, email, optional phone/WeChat, message, number details). It is sent to our private inbox through FormSubmit (formsubmit.co), a form-to-email service, so we can reply.</li><li><b>Tool inputs</b> (numbers you check) are processed in your browser. They are not sent to us unless you submit a form.</li><li><b>Cookies and analytics:</b> if enabled, Google Analytics and Google AdSense may use cookies to measure traffic and show ads, including personalised ads where permitted.</li><li><b>Local storage:</b> we store small preferences (theme, dismissed pop-ups) in your browser.</li></ul>
<h2>Google advertising</h2><p>Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits. You can opt out of personalised advertising at <a href="https://adssettings.google.com" target="_blank" rel="noopener">Google Ads Settings</a> or <a href="https://www.aboutads.info" target="_blank" rel="noopener">aboutads.info</a>.</p>
<h2>Embedded content</h2><p>YouTube videos load only when you click play, from youtube-nocookie.com. Donation links take you to the provider (PayPal, Stripe and others) under their own privacy policies.</p>
<h2>How we use data</h2><p>To answer requests, provide matching and appraisal services, send newsletters you asked for, and improve the site. <b>We do not sell personal data.</b> With your consent, we may introduce you to a vetted buyer, seller or consultant for your request.</p>
<h2>Retention and your rights</h2><p>We keep inquiry emails as long as needed to handle your request and for legitimate records. You may ask for access, correction or deletion at any time through the <a href="contact.html">contact form</a>. Residents of the EU/UK (GDPR), California (CCPA/CPRA), Canada (PIPEDA) and other regions have the rights their laws provide.</p>
<h2>Children</h2><p>The site is not directed to children under 13, and we do not knowingly collect their data.</p>
<h2>Hosting</h2><p>The site is hosted on GitHub Pages, which may log IP addresses for security.</p>""")


def terms():
    return legal("terms.html", "Terms of Use", """
<h2>1. Acceptance</h2><p>By using 579999.com you agree to these terms. If you do not agree, please do not use the site.</p>
<h2>2. Information only</h2><p>Numerology, zodiac and "luck" content reflects cultural traditions and popular beliefs for entertainment and education. Luck scores and pattern tiers are not appraisals, guarantees of value or financial advice.</p>
<h2>3. Exchange and matching services</h2><p>We may introduce buyers, sellers and consultants. We are not a party to any transaction unless agreed in writing. You are responsible for confirming that transfers are lawful and for completing them through the proper carrier, plate authority or registrar. Commissions or fees, if any, are agreed in writing in advance.</p>
<h2>4. User submissions</h2><p>You confirm that anything you submit is accurate and yours to share, and you grant us a licence to use it to respond to you (and, for contest entries, to publish it with credit).</p>
<h2>5. Donations</h2><p>Donations are voluntary gifts to support an independent website, are processed by third-party providers, and are non-refundable except where required by law.</p>
<h2>6. Intellectual property</h2><p>Original text, design and code on this site are © 579999.com. Third-party trademarks and embedded videos belong to their owners. See the <a href="disclaimer.html">Disclaimer &amp; Trademark notice</a>.</p>
<h2>7. Liability</h2><p>The site is provided "as is". To the fullest extent permitted by law, we are not liable for losses arising from its use or from any transaction between users.</p>
<h2>8. Changes</h2><p>We may update these terms. Continued use after an update means you accept the new terms.</p>""")


def disclaimer():
    return legal("disclaimer.html", "Disclaimer & Trademark / Copyright Disclosure", f"""
<h2>Trademark disclosure</h2>
<p>"579999" appears on this website solely as (a) the domain name 579999.com and (b) a descriptive numeric sequence discussed for its cultural meaning. <b>We do not claim trademark rights in the number "579999"</b>, and we make no claim to any mark consisting of or containing these digits. This website is <b>not affiliated with, sponsored by or endorsed by</b> any company, product, brand, telecom carrier, plate authority, registrar, financial institution or government that uses the same or similar numbers or names.</p>
<p>All other trademarks, service marks, company names and logos mentioned (for example, 58.com, NetEase/163.com, Qihoo 360, YouTube, Google, PayPal, Stripe) belong to their respective owners and are referenced only for identification, commentary and news reporting. No endorsement is implied.</p>
<h2>Copyright disclosure</h2>
<p>Original articles, tools, code and design are © 579999.com and may not be republished without permission. Short quotations with a link back are welcome. Market facts are cited to their original publishers. Numbers and facts themselves are not subject to copyright, but the publishers' articles are, and we link to them rather than reproduce them.</p>
<p>Embedded YouTube videos are displayed with YouTube's embed player under YouTube's Terms of Service and remain the property of their creators. Creators may request removal at any time.</p>
<h2>Copyright complaints (DMCA-style notice)</h2>
<p>If you believe content here infringes your rights, send a notice through our <a href="contact.html">contact form</a> including: the work, the URL on our site, your contact details, a good-faith statement, and a statement that the notice is accurate and that you are the owner or authorised to act. We will respond promptly.</p>
<h2>General disclaimer</h2>
<p>Content is provided for entertainment and education. It is not financial, investment, legal, tax or religious advice. Cultural meanings vary by region, dialect and family tradition. Prices and records are historical and do not predict future values.</p>
<p>Inquiries about this website or the domain: <a href="{INTEREST_URL}" target="_blank" rel="noopener">web.works/contact</a>.</p>""")


def notfound():
    body = """<section class="section"><div class="wrap center" style="max-width:720px"><div class="bignum">404</div>
<h1>This number isn't lucky… it doesn't exist.</h1><p class="lead">(Also, 4 sounds like 死. We'll let that one go.)</p>
<p><a class="btn btn-red btn-lg" href="index.html">Go home</a> <a class="btn btn-ghost btn-lg" href="appraise.html">Check a number</a></p></div></section>"""
    return render("404.html", "Page not found", "Page not found.", body)


PAGES = {"support.html": support, "contests.html": contests, "careers.html": careers, "advertise.html": advertise,
         "about.html": about, "contact.html": contact, "faq.html": faq, "privacy.html": privacy, "terms.html": terms,
         "disclaimer.html": disclaimer, "404.html": notfound}
