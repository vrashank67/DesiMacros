# DesiMacros 🥗

**Indian fast food & restaurant nutrition data — all from official sources.**

Browse, search, filter, and compare calories, protein, carbs, and fat across 12 major Indian restaurant chains. No sign-ups, no PDF hunting — just clean, sortable data in one place.

👉 **[desimacros.netlify.app](https://desimacros.netlify.app)** (or open `index.html` directly)

---

## Features

- **258 items** across 12 chains — McDonald's India, Burger King India, Subway India, Pizza Hut India, KFC India, Taco Bell India, Domino's India, Starbucks India, Wow! Momo, Faasos, California Burrito India, Haldiram's
- **Sortable columns** — click any header to sort by calories, protein, carbs, or fat
- **Filter by chain, category, or veg/non-veg**
- **Search** across all items
- **Calorie visual bars** — quick glance at calorie density (green < 200, amber < 450, red ≥ 450)
- **Serving notes** on every item so you know exactly what you're comparing
- **Responsive** — works on desktop and mobile
- **Zero dependencies** — one HTML file, open and go

## Data Sources

All nutrition values are sourced from:

| Chain | Source |
|-------|--------|
| McDonald's India | Official McDonald's India nutrition PDF |
| Burger King India | Official Burger King India menu |
| Subway India | Official Subway India nutrition PDF |
| Pizza Hut India | Official Pizza Hut India menu |
| KFC India | FSSAI-compliant KFC India nutrition booklet |
| Taco Bell India | Official tacobell.co.in/nutritional-info page |
| Domino's India | FatSecret India branded entries (official manufacturer data) |
| Starbucks India | FatSecret India branded entries |
| Wow! Momo | Official Wow! Momo dashboard |
| Faasos | Official Rebel Foods nutrition PDF |
| California Burrito India | FatSecret India branded entries |
| Haldiram's | Official Haldiram's calorific value page |

> **Note:** Values are approximate and may vary by location, recipe changes, and preparation. Always check the restaurant's current menu for the most up-to-date information.

## Usage

Clone the repo and open `index.html` in any modern browser:

```bash
git clone https://github.com/vrashank67/DesiMacros.git
cd DesiMacros
open index.html
```

No build step, no server required — it's a single static HTML file with embedded CSS and JS.

## Tech Stack

- **Zero frameworks** — vanilla HTML / CSS / JS
- Google Fonts (DM Sans + DM Serif Display)
- The entire app (data + UI) lives in one file — easy to fork and extend

## Contributing

Know a chain we're missing? Found an error? Want to add more items?

1. Fork the repo
2. Edit `index.html` — add your chain to the `DATA` array (see existing structure)
3. Submit a pull request

All data **must** come from official sources (brand website, FSSAI-compliant PDF, or manufacturer-provided data). No crowdsourced or user-submitted values.

## Why This Exists

Indian fast-food nutrition info is spread across dozens of PDFs, web pages, and confusing calorie charts. DesiMacros brings it all together in one clean, comparable format — **no account, no app download, no PDF downloads needed.**

## License

MIT — use it, fork it, share it.
