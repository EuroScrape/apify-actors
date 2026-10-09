# Ryanair Low Fare Finder: Cheapest Days, Anywhere & Alerts

Unofficial Ryanair API: Ryanair prices and Ryanair flights — the fare calendar of any route (cheapest price per day, months ahead), every destination under your price cap from any airport (cheap flights Europe, low cost flights, low cost airline), round trips, alerts on price drops and new deals.

**Run it on Apify:** [apify.com/euroscrape/ryanair-low-fares](https://apify.com/euroscrape/ryanair-low-fares) (full documentation, pay per result, no subscription).

## Use it as an API

Get your token in [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~ryanair-low-fares/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Use it from an AI agent (MCP)

Add this server to Claude, Cursor, VS Code or any MCP client: the Actor becomes a tool your agent can call.

```
https://mcp.apify.com?tools=euroscrape/ryanair-low-fares
```

It is a pay-per-event Actor, so agents can also pay per run without an Apify account ([agentic payments](https://github.com/apify/apify-mcp-server#-agentic-payments)).

## Input

[`input.json`](input.json), ready to paste in Apify Console or to send to the API:

```json
{
  "routes": [
    "BER-ALC"
  ],
  "months": 2,
  "airports": [
    "Paris Beauvais"
  ],
  "maxPrice": 30
}
```

## Output

One real result, shortened ([`output-sample.json`](output-sample.json) has the full sample; personal data removed):

```json
{
  "type": "destination",
  "origin": "BVA",
  "originName": "Paris Beauvais",
  "destination": "BGY",
  "destinationName": "Milan Bergamo",
  "city": "Bergamo",
  "country": "Italy",
  "departure": "2026-11-02T06:00:00",
  "arrival": "2026-11-02T07:30:00",
  "flightNumber": "FR3433",
  "price": 14.99,
  "currency": "EUR",
  "ryanairPreviousPrice": 0,
  "priceUpdatedAt": "2026-10-02T19:17:49.000Z",
  "scrapedAt": "2026-10-02T19:27:32.579Z"
}
```

## Price

| Event | Price |
|---|---|
| Run start | $0.003 |
| Calendar fare | $0.0005 |
| Destination deal | $0.001 |

Apify subscribers get 10–30% off depending on their plan.

## More

- Ready-made example: [See everywhere you can fly under 30 € from Paris Beauvais](https://apify.com/euroscrape/ryanair-low-fares/examples/fly-under-30-euros-from-paris-beauvais)
- Ready-made example: [See everywhere you can fly under 20 € from Brussels Charleroi](https://apify.com/euroscrape/ryanair-low-fares/examples/fly-under-20-euros-from-brussels-charleroi)
- Ready-made example: [See everywhere you can fly under £20 from London Stansted](https://apify.com/euroscrape/ryanair-low-fares/examples/fly-under-20-pounds-from-london-stansted)
- Ready-made example: [Get the Ryanair fare calendar of a route, day by day](https://apify.com/euroscrape/ryanair-low-fares/examples/ryanair-fare-calendar-cheapest-day-for-a-route)
- Article: [Fridays cost 25% more than Mondays on Ryanair - what the November fare calendars of three routes look like as data](../../articles/17-ryanair-fridays.md)
- [All EuroScrape Actors](../../README.md)
