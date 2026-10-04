# EU Public Tenders Scraper: TED, BOAMP, Awards & Tender Alerts

Public tenders in Europe and contract awards (appels d'offres, marchés publics, Ausschreibungen): EU tenders and procurement notices from TED, plus French tenders (BOAMP) and awarded contracts (DECP). Deadlines, values in €, buyer contacts, winners per lot with bids received, daily tender alerts.

**Run it on Apify:** [apify.com/euroscrape/eu-public-tenders](https://apify.com/euroscrape/eu-public-tenders) (full documentation, pay per result, no subscription).

## Use it as an API

Get your token in [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~eu-public-tenders/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Use it from an AI agent (MCP)

Add this server to Claude, Cursor, VS Code or any MCP client: the Actor becomes a tool your agent can call.

```
https://mcp.apify.com?tools=euroscrape/eu-public-tenders
```

It is a pay-per-event Actor, so agents can also pay per run without an Apify account ([agentic payments](https://github.com/apify/apify-mcp-server#-agentic-payments)).

## Input

[`input.json`](input.json), ready to paste in Apify Console or to send to the API:

```json
{
  "mode": "tenders",
  "keywords": [
    "software"
  ],
  "countries": [
    "DE",
    "FR",
    "PL"
  ],
  "publishedWithinDays": 7,
  "maxItems": 50
}
```

## Output

One real result, shortened ([`output-sample.json`](output-sample.json) has the full sample; personal data removed):

```json
{
  "type": "tender",
  "source": "TED",
  "noticeId": "674214-2026",
  "procedureId": "663171e3-c5be-4930-9462-f4c455f12cb6",
  "url": "https://ted.europa.eu/en/notice/-/detail/674214-2026",
  "pdfUrl": "https://ted.europa.eu/en/notice/674214-2026/pdf",
  "publishedAt": "2026-09-30",
  "country": "DE",
  "countryName": "Germany",
  "buyerName": "Humboldt-Universität zu Berlin",
  "buyerCity": "Berlin",
  "buyerPostCode": "10099",
  "buyerEmail": null,
  "buyerWebsite": "https://zuv.hu-berlin.de/de/ta/bst/",
  "title": "HCM Ausschreibung für Service und Support sowie Projektbegleitung und Change Requests",
  "description": "Service und Support sowie Projektbegleitung und Change Requests für HCM",
  "language": "de",
  "contractType": "services",
  "procedureType": "Open",
  "mainCpv": "72261000",
  "mainCpvLabel": "Software support services",
  "cpvCodes": [
    "72261000",
    "72253000",
    "72253200"
  ],
  "regions": [
    "DE300"
  ],
  "lotsCount": 1,
  "lotTitles": [
    "HCM Ausschreibung für Service und Support sowie Projektbegleitung und Change Requests"
  ],
  "estimatedValue": null,
  "currency": null,
  "deadline": "2026-11-02T08:15:00.000Z"
}
```

## Price

| Event | Price |
|---|---|
| Run start | $0.003 |
| Open tender delivered | $0.003 |
| Contract award delivered | $0.005 |

Apify subscribers get 10–30% off depending on their plan.

## More

- Ready-made example: [daily alerts eu software tenders](https://apify.com/euroscrape/eu-public-tenders/examples/daily-alerts-eu-software-tenders)
- Article: [57% of the contract lots I sampled got a single bid - mining EU tenders and award winners from TED](../../articles/03-eu-tenders.md)
- Example project: [`tenders.py`](../eu-tenders-slack-alerts/tenders.py), a single Python file to post new tenders matching your keywords to Slack, daily
- [All EuroScrape Actors](../../README.md)
