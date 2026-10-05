# Vinted Scraper & Vinted API: 26 Countries, Deals & Alerts

Unofficial Vinted API & scraper: Vinted search in 26 countries at once — prices with buyer fees, brand, size, condition, seller rating. Price comparison across countries for Vinted arbitrage, cheapest-country summary, and a Vinted monitor with instant Vinted alerts on new listings and price drops.

**Run it on Apify:** [apify.com/euroscrape/vinted-scraper](https://apify.com/euroscrape/vinted-scraper) (full documentation, pay per result, no subscription).

## Use it as an API

Get your token in [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~vinted-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Use it from an AI agent (MCP)

Add this server to Claude, Cursor, VS Code or any MCP client: the Actor becomes a tool your agent can call.

```
https://mcp.apify.com?tools=euroscrape/vinted-scraper
```

It is a pay-per-event Actor, so agents can also pay per run without an Apify account ([agentic payments](https://github.com/apify/apify-mcp-server#-agentic-payments)).

## Input

[`input.json`](input.json), ready to paste in Apify Console or to send to the API:

```json
{
  "searches": [
    "nike air max 90"
  ],
  "countries": [
    "FR",
    "DE"
  ],
  "conditions": [
    "new_with_tags",
    "very_good"
  ],
  "priceMax": 80,
  "order": "newest",
  "maxItemsPerSearch": 30
}
```

## Output

One real result, shortened ([`output-sample.json`](output-sample.json) has the full sample; personal data removed):

```json
{
  "type": "item",
  "search": "air max 90",
  "id": "10206388821",
  "url": "https://www.vinted.fr/items/10206388821-nike-air-max-90-blanche-taille-42",
  "title": "Nike Air max 90 blanche taille 42",
  "price": 15,
  "currency": "EUR",
  "totalPrice": 16.45,
  "serviceFee": 1.45,
  "brand": "Nike",
  "size": "42",
  "condition": "Très bon état",
  "conditionCode": "very_good",
  "favourites": 5,
  "isPromoted": false,
  "sellerType": "private",
  "photo": "https://images1.vinted.net/t/04_003eb_ukTqiqU2eFLwKebttceHDdzR/f800/2b75ef3e.webp?s=fdb6d9877cb757be69e9e48671d0390c7adc49ed",
  "country": "FR",
  "site": "Vinted FR",
  "priceConverted": 15,
  "totalPriceConverted": 16.45,
  "convertedCurrency": "EUR",
  "scrapedAt": "2026-10-01T17:47:18.812Z"
}
```

## Price

| Event | Price |
|---|---|
| Run start | $0.003 |
| Item | $0.001 |
| Item with full details | $0.002 |
| Sold listing detected | $0.002 |

Apify subscribers get 10–30% off depending on their plan.

## More

- Ready-made example: [vinted new listing alerts nike fr](https://apify.com/euroscrape/vinted-scraper/examples/vinted-new-listing-alerts-nike-fr)
- Ready-made example: [ps5 deal alerts on vinted](https://apify.com/euroscrape/vinted-scraper/examples/ps5-deal-alerts-on-vinted)
- Ready-made example: [vinted price comparison across countries](https://apify.com/euroscrape/vinted-scraper/examples/vinted-price-comparison-across-countries)
- Ready-made example: [track sold items on vinted](https://apify.com/euroscrape/vinted-scraper/examples/track-sold-items-on-vinted)
- Ready-made example: [alerte vinted nouvelles annonces](https://apify.com/euroscrape/vinted-scraper/examples/alerte-vinted-nouvelles-annonces)
- Ready-made example: [vinted alarm neue artikel](https://apify.com/euroscrape/vinted-scraper/examples/vinted-alarm-neue-artikel)
- Article: [When a Vinted search finds nothing, it quietly shows you popular junk - here is how to detect it](../../articles/08-vinted-fallback-feed.md)
- [All EuroScrape Actors](../../README.md)
