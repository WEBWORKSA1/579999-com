/* ============================================================
   579999.com — SITE CONFIG (edit this one file to go live)
   ============================================================ */
window.SITE_CONFIG = {
  siteName: "579999.com",
  // Google AdSense: paste your publisher ID (e.g. "ca-pub-1234567890123456").
  // Leave empty to show neutral ad placeholders. Also update /ads.txt.
  adsenseClient: "",
  // Optional per-slot IDs from AdSense > Ads > By ad unit
  adSlots: { top: "", inContent: "", sidebar: "", footer: "" },

  // Google Analytics 4 measurement ID (e.g. "G-XXXXXXX"). Optional.
  ga4: "",

  // Donation / support links. Leave "" to route the button to the pledge form.
  donate: {
    paypal: "",        // e.g. "https://www.paypal.com/donate/?hosted_button_id=XXXX"
    stripe: "",        // e.g. Stripe Payment Link "https://buy.stripe.com/xxxx"
    buymeacoffee: "",  // e.g. "https://buymeacoffee.com/yourname"
    kofi: "",          // e.g. "https://ko-fi.com/yourname"
    patreon: "",       // e.g. "https://patreon.com/yourname"
    githubSponsors: "" // e.g. "https://github.com/sponsors/yourname"
  },

  // Fundraising goal shown on /support.html (update manually)
  fundraising: { goal: 5000, raised: 0, currency: "USD" },

  // External inquiry link shown in the top bar of every page
  interestUrl: "https://web.works/contact",

  // YouTube channel (optional) for the subscribe button
  youtubeChannel: ""
};
