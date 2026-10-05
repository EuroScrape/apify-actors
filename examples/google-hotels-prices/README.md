# Google Hotels Scraper (Google Travel): Prices on Booking Sites

Unofficial Google Hotels API and hotel price tracker: hotel prices from Google Hotels for any destination and dates — per night and total, rating, stars, plus the price on every booking site (Booking.com, Expedia, Agoda…). Hotel price comparison, price calendars, rate parity, price-drop alerts.

**Run it on Apify:** [apify.com/euroscrape/google-hotels-prices](https://apify.com/euroscrape/google-hotels-prices) (full documentation, pay per result, no subscription).

## Use it as an API

Get your token in [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~google-hotels-prices/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Use it from an AI agent (MCP)

Add this server to Claude, Cursor, VS Code or any MCP client: the Actor becomes a tool your agent can call.

```
https://mcp.apify.com?tools=euroscrape/google-hotels-prices
```

It is a pay-per-event Actor, so agents can also pay per run without an Apify account ([agentic payments](https://github.com/apify/apify-mcp-server#-agentic-payments)).

## Input

[`input.json`](input.json), ready to paste in Apify Console or to send to the API:

```json
{
  "locations": [
    "Lisbon"
  ],
  "nights": 2,
  "maxHotelsPerLocation": 20
}
```

## Output

One real result, shortened ([`output-sample.json`](output-sample.json) has the full sample; personal data removed):

```json
{
  "type": "hotel",
  "searchType": "tracked",
  "query": "https://www.google.com/travel/hotels/entity/ChkI1N6v0cC4pfmpARoML2cvMTJxNHhyNHh0EAE",
  "position": null,
  "name": "Novotel Suites Paris Stade de France",
  "hotelId": "ChkI1N6v0cC4pfmpARoML2cvMTJxNHhyNHh0EAE",
  "checkIn": "2026-10-21",
  "checkOut": "2026-10-23",
  "nights": 2,
  "adults": 2,
  "childrenAges": [],
  "currency": "EUR",
  "pricePerNight": 149.23,
  "priceTotal": 298.47,
  "priceBeforeTaxes": 244.23,
  "taxesAndFees": 54.24,
  "dealLabel": null,
  "bookingSitesCount": 23,
  "cheapestSite": "Kiwi.com",
  "cheapestSitePricePerNight": 149.23,
  "officialSitePricePerNight": 181.8,
  "officialVsCheapestPct": 21.8,
  "bookingSites": [
    {
      "site": "Kiwi.com",
      "isOfficialSite": false,
      "pricePerNight": 149.23,
      "priceTotal": 298.47,
      "url": "https://hotels-tracker.kiwi.com/?sig=863672d43279b952b5170ed2c3497011c1cf2b4bb2c02e0599107fa8b3d0ad44333737&turl=https%3A%2F%2Fhotels.kiw…"
    },
    {
      "site": "Super.com",
      "isOfficialSite": false,
      "pricePerNight": 160.93,
      "priceTotal": 321.86,
      "url": "https://www.super.com/travel/transition/?data=price=263.87%26total_price=290.26%26retail_price=374.73%26retail_total_price=412.2%26surcha…"
    },
    {
      "site": "Agoda",
      "isOfficialSite": false,
      "pricePerNight": 161.33,
      "priceTotal": 322.66,
      "url": "https://www.agoda.com/partners/partnersearch.aspx?site_id=1917614&CkInDay=21&CkInMonth=10&CkInYear=2026&CkOutDay=23&campaignid=&CkOutMont…"
    }
  ],
  "rating": 4.3,
  "reviewsCount": 1431,
  "hotelClass": 4,
  "propertyType": "4-star tourist hotel",
  "ratingDistribution": {
    "1": 4,
    "2": 3,
    "3": 9,
    "4": 25,
    "5": 59
  }
}
```

## Price

| Event | Price |
|---|---|
| Run start | $0.003 |
| Hotel price | $0.002 |
| Booking-site prices | $0.003 |

Apify subscribers get 10–30% off depending on their plan.

## More

- Ready-made example: [Compare a hotel's price on every booking site](https://apify.com/euroscrape/google-hotels-prices/examples/hotel-price-on-every-booking-site)
- Ready-made example: [Check a hotel's rate parity: official site vs booking sites](https://apify.com/euroscrape/google-hotels-prices/examples/hotel-rate-parity-official-site-vs-booking-sites)
- Ready-made example: [Find the cheapest well-rated hotels in Paris for your dates](https://apify.com/euroscrape/google-hotels-prices/examples/cheapest-well-rated-hotels-in-paris)
- Article: [Check a hotel's price on every booking site (and spot rate-parity gaps) without writing a scraper](../../articles/01-google-hotels.md)
- Example project: [`parity.py`](../hotel-rate-parity-monitor/parity.py), a single Python file to check whether a hotel's official site is the cheapest place to book it
- [All EuroScrape Actors](../../README.md)
