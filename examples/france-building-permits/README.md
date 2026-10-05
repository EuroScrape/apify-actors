# France Building Permits (Sitadel): Projects, Builders & Alerts

Official French building permits (permis de construire, planning permission, Sitadel): construction projects and construction leads — new housing programmes, commercial building projects. Real estate developers (name, SIREN), address of the works, dwellings, floor area, status. New-permit alerts.

**Run it on Apify:** [apify.com/euroscrape/france-building-permits](https://apify.com/euroscrape/france-building-permits) (full documentation, pay per result, no subscription).

## Use it as an API

Get your token in [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~france-building-permits/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Use it from an AI agent (MCP)

Add this server to Claude, Cursor, VS Code or any MCP client: the Actor becomes a tool your agent can call.

```
https://mcp.apify.com?tools=euroscrape/france-building-permits
```

It is a pay-per-event Actor, so agents can also pay per run without an Apify account ([agentic payments](https://github.com/apify/apify-mcp-server#-agentic-payments)).

## Input

[`input.json`](input.json), ready to paste in Apify Console or to send to the API:

```json
{
  "locations": [
    "38"
  ],
  "permitTypes": [
    "housing"
  ],
  "minDwellings": 10
}
```

## Output

One real result, shortened ([`output-sample.json`](output-sample.json) has the full sample; personal data removed):

```json
{
  "type": "locationSummary",
  "location": "38",
  "since": "2025-10-03",
  "permitsMatching": 85,
  "permitsDelivered": 40,
  "byCategory": {
    "housing": {
      "permits": 85,
      "dwellings": 2480,
      "floorAreaM2": 159110
    }
  },
  "byStatus": {
    "authorized": 82,
    "started": 3
  },
  "topApplicants": [
    {
      "name": "GILLES TRIGNAT RESIDENCES",
      "siren": "397947433",
      "permits": 8,
      "dwellings": 245,
      "floorAreaM2": 15065
    },
    {
      "name": "ISERE HABITAT",
      "siren": "998318711",
      "permits": 6,
      "dwellings": 132,
      "floorAreaM2": 10459
    },
    {
      "name": "EDIFIM DAUPHINE",
      "siren": "485015242",
      "permits": 3,
      "dwellings": 97,
      "floorAreaM2": 5412
    }
  ],
  "source": "SDES — Sitadel, liste des permis de construire et autres autorisations d'urbanisme (Licence Ouverte / Open Licence)",
  "generatedAt": "2026-10-03T13:47:47.316Z"
}
```

## Price

| Event | Price |
|---|---|
| Run start | $0.003 |
| Building permit | $0.003 |

Apify subscribers get 10–30% off depending on their plan.

## More

- Ready-made example: [Find new housing programmes authorized around Lyon](https://apify.com/euroscrape/france-building-permits/examples/new-housing-programmes-around-lyon)
- Ready-made example: [Permis de construire accordés par commune (Sitadel)](https://apify.com/euroscrape/france-building-permits/examples/permis-de-construire-par-commune)
- Ready-made example: [Find new commercial building projects in France](https://apify.com/euroscrape/france-building-permits/examples/new-commercial-building-projects-in-france)
- Article: [Companies file 1 French building permit in 5 and build 3 homes in 4 - and the register names them 8 months before the site opens](../../articles/13-building-permits-window.md)
- [All EuroScrape Actors](../../README.md)
