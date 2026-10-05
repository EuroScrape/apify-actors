# EU Electricity Prices API: Day-Ahead Power Prices & Cheap Hours

Electricity prices scraper & API: hourly (or 15-minute) day-ahead spot prices of the European electricity market (Strompreise, prix de l'électricité), 40+ bidding zones, official data — energy prices, cheapest hours, negative-price and spike alerts, history. For Home Assistant, Slack, webhooks.

**Run it on Apify:** [apify.com/euroscrape/eu-electricity-prices](https://apify.com/euroscrape/eu-electricity-prices) (full documentation, pay per result, no subscription).

## Use it as an API

Get your token in [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~eu-electricity-prices/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Use it from an AI agent (MCP)

Add this server to Claude, Cursor, VS Code or any MCP client: the Actor becomes a tool your agent can call.

```
https://mcp.apify.com?tools=euroscrape/eu-electricity-prices
```

It is a pay-per-event Actor, so agents can also pay per run without an Apify account ([agentic payments](https://github.com/apify/apify-mcp-server#-agentic-payments)).

## Input

[`input.json`](input.json), ready to paste in Apify Console or to send to the API:

```json
{
  "zones": [
    "FR",
    "DE-LU"
  ],
  "resolution": "hour"
}
```

## Output

One real result, shortened ([`output-sample.json`](output-sample.json) has the full sample; personal data removed):

```json
{
  "type": "daySummary",
  "zone": "FR",
  "zoneName": "France",
  "country": "France",
  "date": "2026-10-03",
  "marketResolution": "15min",
  "averageEurMwh": 172.52,
  "minEurMwh": 63.94,
  "minTimeCet": "2026-10-03T13:30",
  "maxEurMwh": 243.06,
  "maxTimeCet": "2026-10-03T18:45",
  "negativeQuarterHours": 0,
  "negativeHours": 0,
  "cheapestWindow": {
    "hours": 4,
    "startCet": "2026-10-03T11:45",
    "averageEurMwh": 89.88,
    "endCet": "2026-10-03T15:45"
  },
  "priciestWindow": {
    "hours": 4,
    "startCet": "2026-10-03T17:45",
    "averageEurMwh": 226.32,
    "endCet": "2026-10-03T21:45"
  },
  "cheapest3hWindow": {
    "startCet": "2026-10-03T12:15",
    "averageEurMwh": 81.95
  },
  "priciest3hWindow": {
    "startCet": "2026-10-03T18:15",
    "averageEurMwh": 229.93
  },
  "spreadEurMwh": 179.12,
  "source": "Bundesnetzagentur | SMARD.de via api.energy-charts.info (CC BY 4.0)"
}
```

## Price

| Event | Price |
|---|---|
| Run start | $0.003 |
| Price row | $0.0002 |

Apify subscribers get 10–30% off depending on their plan.

## More

- Ready-made example: [cheapest electricity hours france](https://apify.com/euroscrape/eu-electricity-prices/examples/cheapest-electricity-hours-france)
- Ready-made example: [alerts when german power prices go negative](https://apify.com/euroscrape/eu-electricity-prices/examples/alerts-when-german-power-prices-go-negative)
- Ready-made example: [germany day ahead electricity prices hourly](https://apify.com/euroscrape/eu-electricity-prices/examples/germany-day-ahead-electricity-prices-hourly)
- Ready-made example: [strompreise morgen stuendlich day ahead](https://apify.com/euroscrape/eu-electricity-prices/examples/strompreise-morgen-stuendlich-day-ahead)
- Ready-made example: [netherlands dynamic electricity prices hourly](https://apify.com/euroscrape/eu-electricity-prices/examples/netherlands-dynamic-electricity-prices-hourly)
- Ready-made example: [precio luz manana por horas](https://apify.com/euroscrape/eu-electricity-prices/examples/precio-luz-manana-por-horas)
- Ready-made example: [nordic electricity spot prices by zone](https://apify.com/euroscrape/eu-electricity-prices/examples/nordic-electricity-spot-prices-by-zone)
- Ready-made example: [prix electricite demain heure par heure](https://apify.com/euroscrape/eu-electricity-prices/examples/prix-electricite-demain-heure-par-heure)
- Article: [Night power is not the cheapest, and the cheapest fuel station is often a ghost - two things official energy data taught me](../../articles/11-energy-two-assumptions.md)
- [All EuroScrape Actors](../../README.md)
