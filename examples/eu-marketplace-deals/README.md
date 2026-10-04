# EU Second-Hand Marketplaces Scraper: Vinted, OLX & More

Second-hand price comparison for used items across the top European marketplaces (18 countries): Kleinanzeigen, Vinted, OLX, Marktplaats, Subito, Wallapop, willhaben, Blocket, DBA, FINN… Second-hand prices in €, deal score vs. the European market, cheapest country, resale margin (arbitrage), alerts.

**Run it on Apify:** [apify.com/euroscrape/eu-marketplace-deals](https://apify.com/euroscrape/eu-marketplace-deals) (full documentation, pay per result, no subscription).

## Use it as an API

Get your token in [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~eu-marketplace-deals/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Use it from an AI agent (MCP)

Add this server to Claude, Cursor, VS Code or any MCP client: the Actor becomes a tool your agent can call.

```
https://mcp.apify.com?tools=euroscrape/eu-marketplace-deals
```

It is a pay-per-event Actor, so agents can also pay per run without an Apify account ([agentic payments](https://github.com/apify/apify-mcp-server#-agentic-payments)).

## Input

[`input.json`](input.json), ready to paste in Apify Console or to send to the API:

```json
{
  "searchQueries": [
    "nintendo switch oled"
  ],
  "countries": [
    "DE",
    "FR",
    "IT",
    "ES",
    "NL",
    "PL"
  ],
  "maxItemsPerMarketplace": 20
}
```

## Output

One real result, shortened ([`output-sample.json`](output-sample.json) has the full sample; personal data removed):

```json
{
  "type": "listing",
  "query": "nintendo switch oled",
  "marketplace": "willhaben",
  "country": "AT",
  "countryName": "Austria",
  "listingId": "1572600251",
  "url": "https://www.willhaben.at/iad/kaufen-und-verkaufen/d/nintendo-switch-lite-oled-konsole-spiele-zubehoer-1572600251/",
  "title": "NINTENDO SWITCH| LITE & OLED | KONSOLE | SPIELE | ZUBEHÖR",
  "price": 99.99,
  "currency": "EUR",
  "priceEur": 99.99,
  "priceType": "fixed",
  "previousPrice": null,
  "priceWithBuyerFee": null,
  "condition": null,
  "conditionNormalized": null,
  "brand": null,
  "location": "Wien, 10. Bezirk, Favoriten 1100",
  "postedAt": "2026-09-29T20:00:59Z",
  "imageUrl": "https://cache.willhaben.at/mmo/1/157/260/0251_-1524531789_hoved.jpg",
  "sellerType": "business",
  "shippingAvailable": null,
  "reserved": null,
  "views": null,
  "favourites": null,
  "descriptionSnippet": "AN- VERKAUF & TAUSCH Neilreichgasse 26 | 1100 WIEN DIE ÖFFNUNGSZEITEN: MO. - DO.: 10:30 - 19:00 FR.: 10:30 - 12:30 | 14:00 - 19:00 SA.: 1…",
  "isAccessoryOnly": false,
  "isPossiblyDefective": false
}
```

## Price

| Event | Price |
|---|---|
| Run start | $0.003 |
| Listing delivered | $0.002 |

Apify subscribers get 10–30% off depending on their plan.

## More

- Ready-made example: [compare iphone prices across 18 countries](https://apify.com/euroscrape/eu-marketplace-deals/examples/compare-iphone-prices-across-18-countries)
- Article: [Same used iPhone, 62% price gap - comparing second-hand prices across 18 European countries](../../articles/02-second-hand-europe.md)
- [All EuroScrape Actors](../../README.md)
