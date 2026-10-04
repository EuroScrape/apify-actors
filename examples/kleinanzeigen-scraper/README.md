# Kleinanzeigen Scraper & Kleinanzeigen API: Deals & Alerts

Unofficial Kleinanzeigen API & scraper for German classifieds: Kleinanzeigen.de ads (ex eBay Kleinanzeigen), Kleinanzeigen prices with a 0–100 deal score vs. market price, monitor mode for new ads & price drops (Suchauftrag, Preisalarm), Kleinanzeigen alerts on Telegram/Discord, seller details.

**Run it on Apify:** [apify.com/euroscrape/kleinanzeigen-scraper](https://apify.com/euroscrape/kleinanzeigen-scraper) (full documentation, pay per result, no subscription).

## Use it as an API

Get your token in [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~kleinanzeigen-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Use it from an AI agent (MCP)

Add this server to Claude, Cursor, VS Code or any MCP client: the Actor becomes a tool your agent can call.

```
https://mcp.apify.com?tools=euroscrape/kleinanzeigen-scraper
```

It is a pay-per-event Actor, so agents can also pay per run without an Apify account ([agentic payments](https://github.com/apify/apify-mcp-server#-agentic-payments)).

## Input

[`input.json`](input.json), ready to paste in Apify Console or to send to the API:

```json
{
  "keywords": [
    "iphone 15"
  ],
  "locations": [
    "Berlin"
  ],
  "radiusKm": 20,
  "maxItems": 50,
  "minDealScore": 60
}
```

## Output

One real result, shortened ([`output-sample.json`](output-sample.json) has the full sample; personal data removed):

```json
{
  "id": "3526538200",
  "url": "https://www.kleinanzeigen.de/s-anzeige/fahrradtraeger/3526538200-217-20258",
  "title": "Fahrradträger",
  "price": null,
  "priceType": "NEGOTIABLE",
  "priceText": "VB",
  "currency": "EUR",
  "location": "25856 Hattstedt",
  "postalCode": "25856",
  "city": "Hattstedt",
  "postedAt": "2026-09-29T12:56:00.000Z",
  "postedAtText": "Heute, 14:56",
  "shippingAvailable": true,
  "buyNowAvailable": false,
  "adType": "OFFERED",
  "isTopAd": false,
  "descriptionSnippet": "Ich biete diesen stabilen Fahrradträger für die Anhängerkupplung an, der sich ideal für den Transport von 3 Rädern eignet.\n\n- Robuste sch…",
  "imageUrl": "https://img.kleinanzeigen.de/api/v1/prod-ads/images/fa/fa8114df-6aff-4542-ad89-8997dcc4b68e?rule=$_59.JPG",
  "imageCount": 3,
  "comparableAds": [],
  "search": {
    "keyword": "fahrrad",
    "location": "Atlantisstadt",
    "resolvedLocation": "hattstedt"
  },
  "changeType": null,
  "riskFlags": [],
  "scrapedAt": "2026-09-29T13:24:54.016Z"
}
```

## Price

| Event | Price |
|---|---|
| Run start | $0.003 |
| Ad | $0.002 |
| Ad with full details | $0.004 |

Apify subscribers get 10–30% off depending on their plan.

## More

- Ready-made example: [instant alerts new kleinanzeigen ads](https://apify.com/euroscrape/kleinanzeigen-scraper/examples/instant-alerts-new-kleinanzeigen-ads)
- [All EuroScrape Actors](../../README.md)
