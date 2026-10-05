# France Energy Ratings (DPE): Homes, Energy Certificates, Sieves

DPE scraper & DPE API: official energy performance certificates (EPC, diagnostic de performance énergétique) of French homes (ADEME data) — energy efficiency class & CO2 class, address, surface, consumption, yearly bill, insulation. Find F/G energy sieves (passoires thermiques); alerts on new ones.

**Run it on Apify:** [apify.com/euroscrape/france-energy-ratings](https://apify.com/euroscrape/france-energy-ratings) (full documentation, pay per result, no subscription).

## Use it as an API

Get your token in [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~france-energy-ratings/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Use it from an AI agent (MCP)

Add this server to Claude, Cursor, VS Code or any MCP client: the Actor becomes a tool your agent can call.

```
https://mcp.apify.com?tools=euroscrape/france-energy-ratings
```

It is a pay-per-event Actor, so agents can also pay per run without an Apify account ([agentic payments](https://github.com/apify/apify-mcp-server#-agentic-payments)).

## Input

[`input.json`](input.json), ready to paste in Apify Console or to send to the API:

```json
{
  "locations": [
    "Grenoble"
  ],
  "ratings": [
    "F",
    "G"
  ],
  "maxRatingsPerLocation": 50
}
```

## Output

One real result, shortened ([`output-sample.json`](output-sample.json) has the full sample; personal data removed):

```json
{
  "type": "locationSummary",
  "location": "Grenoble",
  "totalRatings": 56771,
  "byRating": {
    "A": {
      "count": 480,
      "sharePct": 0.8
    },
    "B": {
      "count": 3974,
      "sharePct": 7
    },
    "C": {
      "count": 19117,
      "sharePct": 33.7
    },
    "D": {
      "count": 19011,
      "sharePct": 33.5
    },
    "E": {
      "count": 9758,
      "sharePct": 17.2
    },
    "F": {
      "count": 3061,
      "sharePct": 5.4
    },
    "G": {
      "count": 1370,
      "sharePct": 2.4
    }
  },
  "energySieves": {
    "count": 4431,
    "sharePct": 7.8
  },
  "deliveredRatings": 40,
  "medianAnnualEnergyCostEurDelivered": 1766,
  "source": "ADEME — DPE Logements existants (depuis juillet 2021), Licence Ouverte / Open Licence",
  "generatedAt": "2026-10-03T12:54:51.034Z"
}
```

## Price

| Event | Price |
|---|---|
| Run start | $0.003 |
| Energy rating | $0.001 |

Apify subscribers get 10–30% off depending on their plan.

## More

- Ready-made example: [Find the F and G rated homes of Paris, address by address](https://apify.com/euroscrape/france-energy-ratings/examples/energy-sieves-f-g-homes-in-paris)
- Ready-made example: [DPE par commune : classes énergie et passoires thermiques](https://apify.com/euroscrape/france-energy-ratings/examples/dpe-par-commune-classes-energie)
- Article: [I matched 2,518 apartment sales to their energy certificates - F and G homes sold 16% cheaper per m²](../../articles/12-dvf-dpe-energy-discount.md)
- [All EuroScrape Actors](../../README.md)
