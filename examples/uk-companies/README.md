# UK Companies House API & Scraper: UK Company Data & B2B Leads

Unofficial Companies House API & scraper: UK company data by SIC code, location, incorporation date and status. Company profiles, directors and officers, and optionally the website, emails and phones (UK B2B leads). No 10,000-result cap. Monitor new incorporations and changes.

**Run it on Apify:** [apify.com/euroscrape/uk-companies](https://apify.com/euroscrape/uk-companies) (full documentation, pay per result, no subscription).

## Use it as an API

Get your token in [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~uk-companies/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Use it from an AI agent (MCP)

Add this server to Claude, Cursor, VS Code or any MCP client: the Actor becomes a tool your agent can call.

```
https://mcp.apify.com?tools=euroscrape/uk-companies
```

It is a pay-per-event Actor, so agents can also pay per run without an Apify account ([agentic payments](https://github.com/apify/apify-mcp-server#-agentic-payments)).

## Input

[`input.json`](input.json), ready to paste in Apify Console or to send to the API:

```json
{
  "sicCodes": [
    "43220"
  ],
  "location": "Manchester",
  "maxItems": 100,
  "findContacts": true
}
```

## Output

One real result, shortened ([`output-sample.json`](output-sample.json) has the full sample; personal data removed):

```json
{
  "companyNumber": "12499918",
  "name": "PINK PONY LTD",
  "status": "dissolved",
  "companyType": "Private limited Company",
  "incorporatedOn": "2020-03-05",
  "dissolvedOn": "2021-09-07",
  "registeredOffice": "115 Henbury Road, Bristol, City Of Bristol, England, BS10 7AA",
  "postcode": "BS10 7AA",
  "sicCodes": [
    {
      "code": "56101",
      "description": "Licensed restaurants"
    }
  ],
  "accounts": {
    "nextMadeUpTo": null,
    "nextDueBy": null,
    "lastMadeUpTo": null,
    "overdue": false
  },
  "confirmationStatement": {
    "nextDueBy": null,
    "lastDated": null
  },
  "previousNames": [],
  "hasCharges": false,
  "hasInsolvencyHistory": false,
  "ageYears": 6,
  "links": {
    "companiesHouse": "https://find-and-update.company-information.service.gov.uk/company/12499918",
    "filingHistory": "https://find-and-update.company-information.service.gov.uk/company/12499918/filing-history"
  },
  "changeType": null,
  "scrapedAt": "2026-09-29T13:25:47.118Z"
}
```

## Price

| Event | Price |
|---|---|
| Run start | $0.003 |
| Company | $0.004 |
| Website & contacts found | $0.025 |

Apify subscribers get 10–30% off depending on their plan.

## More

- Ready-made example: [new london software companies with officers](https://apify.com/euroscrape/uk-companies/examples/new-london-software-companies-with-officers)
- Ready-made example: [newly incorporated uk companies this week](https://apify.com/euroscrape/uk-companies/examples/newly-incorporated-uk-companies-this-week)
- Ready-made example: [uk restaurants by town with directors](https://apify.com/euroscrape/uk-companies/examples/uk-restaurants-by-town-with-directors)
- Article: [Build B2B lead lists from official company registers (France SIRENE and UK Companies House)](../../articles/05-company-registers-leads.md)
- [All EuroScrape Actors](../../README.md)
