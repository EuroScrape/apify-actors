# France Real Estate Sold Prices (DVF): €/m², Sales & Trends

Real estate France: sold house prices from the State's record of property sales in France (DVF, valeurs foncières, prix immobilier) — price, €/m², address, 2021-2025, with the energy rating (DPE) of the home sold and indicative rental yield (rendement locatif). Medians per city, alerts on new sales.

**Run it on Apify:** [apify.com/euroscrape/france-property-prices](https://apify.com/euroscrape/france-property-prices) (full documentation, pay per result, no subscription).

## Use it as an API

Get your token in [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~france-property-prices/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Use it from an AI agent (MCP)

Add this server to Claude, Cursor, VS Code or any MCP client: the Actor becomes a tool your agent can call.

```
https://mcp.apify.com?tools=euroscrape/france-property-prices
```

It is a pay-per-event Actor, so agents can also pay per run without an Apify account ([agentic payments](https://github.com/apify/apify-mcp-server#-agentic-payments)).

## Input

[`input.json`](input.json), ready to paste in Apify Console or to send to the API:

```json
{
  "locations": [
    "Grenoble"
  ],
  "years": [
    2024,
    2025
  ],
  "propertyTypes": [
    "apartment"
  ],
  "includeEnergyRating": true,
  "includeRentalYield": true
}
```

## Output

One real result, shortened ([`output-sample.json`](output-sample.json) has the full sample; personal data removed):

```json
{
  "type": "sale",
  "location": "Grenoble",
  "saleId": "2025-5070••",
  "date": "2025-12-23",
  "year": 2025,
  "price": 465000,
  "propertyType": "apartment",
  "isNewBuild": false,
  "surface": 144,
  "rooms": 6,
  "pricePerM2": 3229,
  "dwellings": 1,
  "outbuildings": 2,
  "landSurface": null,
  "address": "•• CRS BERRIAT",
  "postalCode": "38000",
  "city": "Grenoble",
  "inseeCode": "38185",
  "department": "38",
  "latitude": 45.187,
  "longitude": 5.723,
  "rentIndicatorPerM2": 12.21,
  "grossRentalYieldPct": 4.5,
  "rentIndicatorReliable": true,
  "energyRating": "D",
  "ghgRating": "D",
  "energyKwhM2Year": 202,
  "energyRatingIssuedAt": "2025-10-23"
}
```

## Price

| Event | Price |
|---|---|
| Run start | $0.003 |
| Property sale | $0.0005 |

Apify subscribers get 10–30% off depending on their plan.

## More

- Ready-made example: [apartments sold in grenoble real prices](https://apify.com/euroscrape/france-property-prices/examples/apartments-sold-in-grenoble-real-prices)
- Ready-made example: [apartments sold in bordeaux real prices](https://apify.com/euroscrape/france-property-prices/examples/apartments-sold-in-bordeaux-real-prices)
- Ready-made example: [sold prices by energy class in lyon](https://apify.com/euroscrape/france-property-prices/examples/sold-prices-by-energy-class-in-lyon)
- Ready-made example: [rental yield by arrondissement in paris](https://apify.com/euroscrape/france-property-prices/examples/rental-yield-by-arrondissement-in-paris)
- Article: [France publishes every property sale as open data - most people compute the price per m² wrong](../../articles/10-dvf-prix-immobilier.md)
- Article: [I matched 2,518 apartment sales to their energy certificates - F and G homes sold 16% cheaper per m²](../../articles/12-dvf-dpe-energy-discount.md)
- [All EuroScrape Actors](../../README.md)
