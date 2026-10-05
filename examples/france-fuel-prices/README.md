# France Fuel Prices: Gas Station Prices, Diesel Prices & Alerts

Live fuel prices in France (prix des carburants, gas prices France, petrol prices, gasoline prices): diesel prices, SP95/98, E10, E85 and LPG of all ~10,000 French fuel stations (official government feed) — cheapest around any city or point, with distances, median, local spread, price-drop alerts.

**Run it on Apify:** [apify.com/euroscrape/france-fuel-prices](https://apify.com/euroscrape/france-fuel-prices) (full documentation, pay per result, no subscription).

## Use it as an API

Get your token in [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~france-fuel-prices/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Use it from an AI agent (MCP)

Add this server to Claude, Cursor, VS Code or any MCP client: the Actor becomes a tool your agent can call.

```
https://mcp.apify.com?tools=euroscrape/france-fuel-prices
```

It is a pay-per-event Actor, so agents can also pay per run without an Apify account ([agentic payments](https://github.com/apify/apify-mcp-server#-agentic-payments)).

## Input

[`input.json`](input.json), ready to paste in Apify Console or to send to the API:

```json
{
  "locations": [
    "Grenoble"
  ],
  "radiusKm": 10,
  "fuels": [
    "Gazole",
    "E10"
  ]
}
```

## Output

One real result, shortened ([`output-sample.json`](output-sample.json) has the full sample; personal data removed):

```json
{
  "type": "locationSummary",
  "location": "Grenoble",
  "radiusKm": 8,
  "stationsFound": 27,
  "stationsDelivered": 12,
  "stalePricesIgnored": 0,
  "byFuel": {
    "Gazole": {
      "stations": 26,
      "cheapest": {
        "price": 2.25,
        "address": "14 Avenue Esclangon",
        "city": "Gières",
        "distanceKm": 5.5,
        "updatedAt": "2026-09-14T08:12:08"
      },
      "median": 2.381,
      "spreadCts": 29.9
    },
    "E10": {
      "stations": 25,
      "cheapest": {
        "price": 1.99,
        "address": "Avenue de Verdun",
        "city": "LA TRONCHE",
        "distanceKm": 3,
        "updatedAt": "2026-10-02T15:49:30"
      },
      "median": 2.199,
      "spreadCts": 31.9
    },
    "SP98": {
      "stations": 20,
      "cheapest": {
        "price": 1.99,
        "address": "115 AVENUE DE LA REPUBLIQUE",
        "city": "SEYSSINET",
        "distanceKm": 1.7,
        "updatedAt": "2026-10-03T08:25:19"
      },
      "median": 2.305,
      "spreadCts": 49.9
    }
  },
  "source": "prix-carburants.gouv.fr (Licence Ouverte / Open Licence)",
  "generatedAt": "2026-10-03T13:04:41.023Z"
}
```

## Price

| Event | Price |
|---|---|
| Run start | $0.003 |
| Station | $0.001 |

Apify subscribers get 10–30% off depending on their plan.

## More

- Ready-made example: [Find the cheapest Diesel around Lyon right now](https://apify.com/euroscrape/france-fuel-prices/examples/cheapest-diesel-around-lyon)
- Ready-made example: [Find the cheapest Diesel around Marseille right now](https://apify.com/euroscrape/france-fuel-prices/examples/cheapest-diesel-around-marseille)
- Ready-made example: [Find E85 ethanol stations around Toulouse with live prices](https://apify.com/euroscrape/france-fuel-prices/examples/e85-stations-around-toulouse)
- Ready-made example: [Prix des carburants autour d'une ville, station par station](https://apify.com/euroscrape/france-fuel-prices/examples/prix-carburants-autour-d-une-ville)
- Article: [Night power is not the cheapest, and the cheapest fuel station is often a ghost - two things official energy data taught me](../../articles/11-energy-two-assumptions.md)
- [All EuroScrape Actors](../../README.md)
