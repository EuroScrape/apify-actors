# Trusted Shops Scraper: Shop Leads, Ratings, Reviews & Alerts

E-commerce leads and e-commerce reviews (shop reviews) from Trusted Shops: online shops (Germany, Austria, Switzerland, France, Spain, Italy, Netherlands, Poland, UK) by keyword with company, email, phone, Handelsregister, rating. Customer reviews (Bewertungen, avis clients), negative-review alerts.

**Run it on Apify:** [apify.com/euroscrape/trusted-shops-scraper](https://apify.com/euroscrape/trusted-shops-scraper) (full documentation, pay per result, no subscription).

## Use it as an API

Get your token in [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~trusted-shops-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Use it from an AI agent (MCP)

Add this server to Claude, Cursor, VS Code or any MCP client: the Actor becomes a tool your agent can call.

```
https://mcp.apify.com?tools=euroscrape/trusted-shops-scraper
```

It is a pay-per-event Actor, so agents can also pay per run without an Apify account ([agentic payments](https://github.com/apify/apify-mcp-server#-agentic-payments)).

## Input

[`input.json`](input.json), ready to paste in Apify Console or to send to the API:

```json
{
  "searchTerms": [
    "fahrrad"
  ],
  "countries": [
    "DE"
  ],
  "maxShopsPerSearch": 4,
  "shops": [
    "bergfreunde.de"
  ],
  "maxReviewsPerShop": 5
}
```

## Output

One real result, shortened ([`output-sample.json`](output-sample.json) has the full sample; personal data removed):

```json
{
  "type": "shop",
  "name": "RennerXXL - Outdoor- und Sportbekleidung in Übergrößen",
  "domain": "outdoor-renner.de",
  "url": "https://www.outdoor-renner.de",
  "tsId": "X8B4BF6371C245F95B3BD70755FE286F2",
  "profileUrl": "https://www.trustedshops.de/bewertung/info_X8B4BF6371C245F95B3BD70755FE286F2.html",
  "market": "DE",
  "language": "de",
  "description": "RennerXXL steht für Outdoor-, Ski-, Fahrrad-, Wander-, Funktions-, und Sportbekleidung in Übergrößen, Langgrößen und Kurzgrößen für Damen…",
  "categories": [
    "Sportartikel"
  ],
  "rating": 4.8,
  "reviewsLast12Months": 1906,
  "reviewsAllTime": 28662,
  "stars": {
    "1": 19,
    "2": 10,
    "3": 34,
    "4": 214,
    "5": 1629
  },
  "negativeSharePct": 1.5,
  "certified": true,
  "profileType": "member",
  "memberSince": "2010-04-12",
  "buyerProtectionMax": "100 EUR",
  "companyName": "RennerXXL GmbH & Co. KG",
  "isCompany": true,
  "street": "Flurstr. 1",
  "postalCode": "84172",
  "city": "Buch",
  "countryCode": "DE",
  "phone": "+4987099430146",
  "email": "service@outdoor-renner.de",
  "contactFormUrl": null
}
```

## Price

| Event | Price |
|---|---|
| Run start | $0.003 |
| Shop | $0.002 |
| Company profile | $0.004 |
| Review | $0.0006 |

Apify subscribers get 10–30% off depending on their plan.

## More

- Ready-made example: [german bike shops with 5000 reviews](https://apify.com/euroscrape/trusted-shops-scraper/examples/german-bike-shops-with-5000-reviews)
- Ready-made example: [latest customer reviews of an online shop](https://apify.com/euroscrape/trusted-shops-scraper/examples/latest-customer-reviews-of-an-online-shop)
- Article: [A 4.8-star shop tells you nothing - across 444 German online shops the rating fits in a third of a point, while the share of 1 and 2 star reviews varies 11x](../../articles/14-trusted-shops-ratings.md)
- Example project: [`complaints.py`](../shop-complaint-rate/complaints.py), a single Python file to rank the shops of a niche by their share of 1 and 2 star reviews
- [All EuroScrape Actors](../../README.md)
