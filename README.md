# EuroScrape: ready-to-use data scrapers (Apify Actors)

Cloud scrapers for hotel prices, public tenders, second-hand marketplaces, company data and website technologies. No code and no servers needed: run them on [Apify](https://apify.com/euroscrape), schedule them, get alerts, and pay only per result.

This repository holds **input templates and real sample outputs** for each Actor, plus code snippets to run them from your own scripts. (The Actors' source code is not public.)

## 📦 Actors

| Actor | What you get | Price |
|---|---|---|
| [Google Hotels Scraper: Prices from Every Booking Site](https://apify.com/euroscrape/google-hotels-prices) | Hotel prices for any destination and dates, the price on every booking site (official website, Booking.com, Expedia…), rate parity, price calendars, price-drop alerts | $0.002 per hotel and date, +$0.003 with all booking sites |
| [EU Public Tenders Scraper: TED, BOAMP, Procurement & Awards](https://apify.com/euroscrape/eu-public-tenders) | Open tenders and contract awards from all of Europe (TED) and France (BOAMP, DECP): deadlines, values in €, buyers, winners per lot, bids received | $0.003 per tender, $0.005 per award |
| [EU Second-Hand Marketplaces Scraper: Vinted, OLX & More](https://apify.com/euroscrape/eu-marketplace-deals) | One search on the top second-hand marketplace of 18 European countries: prices in €, deal score, cheapest country, resale margin | $0.002 per listing |
| [Website Tech Stack Detector: 280+ Technologies, Leads & Signals](https://apify.com/euroscrape/website-intelligence) | Technologies of any website (CMS, e-commerce, analytics…), company identity from the legal notice, contacts and sales signals | $0.02 per website |
| [Impressum & Legal Notice Scraper: VAT, Registry, Contacts](https://apify.com/euroscrape/company-identity) | Legal name, registry numbers and VAT IDs from any European website, checked against official registries | $0.004 per website |
| [French Companies Scraper: SIRENE Leads, Directors & Emails](https://apify.com/euroscrape/france-companies) | Every French company by activity, area and size, with finances and optionally a verified website, emails and phones | $0.004 per company |
| [UK Companies House Scraper: Directors, Leads & Emails](https://apify.com/euroscrape/uk-companies) | UK companies by SIC code and location, with officers and optionally website, emails and phones | $0.004 per company |
| [Kleinanzeigen Scraper: Deal Finder & Price-Drop Alerts](https://apify.com/euroscrape/kleinanzeigen-scraper) | German classifieds with a deal score vs. market price, view counts and instant alerts | $0.002 per ad |

Each run also costs $0.003 to start. Apify subscribers get 10–30% off.

## 🚀 Run an Actor from your code

Get your API token in [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations).

**curl**
```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~google-hotels-prices/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @examples/google-hotels-prices/input.json
```

**Python** (`pip install apify-client`)
```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")
run = client.actor("euroscrape/eu-public-tenders").call(run_input={
    "keywords": ["software"],
    "countries": ["DE", "FR", "PL"],
    "publishedWithinDays": 7,
})
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("deadline"), item.get("url"))
```

**JavaScript** (`npm install apify-client`)
```js
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('euroscrape/eu-marketplace-deals').call({ searchQueries: ['nintendo switch oled'] });
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items.filter((x) => x.type === 'listing').slice(0, 5));
```

## 📁 Examples

Each folder in [`examples/`](examples) has:
- `input.json`: a working input you can paste in Apify Console or send to the API,
- `output-sample.json`: one real result (personal data removed).

## 🔔 Monitoring

Hotels, tenders, second-hand marketplaces, Kleinanzeigen and company registries have a monitoring mode: set a `monitorName`, schedule the Actor (Apify Console → Schedules), and each run returns only what's new (new tenders, new listings, new companies, price drops…). Hotels, tenders and marketplaces can also push alerts to Slack, Telegram, Discord or any webhook.

## 💬 Feedback

Missing a field, a country or a source? Say it in a review on the Actor's page in Apify Store.
