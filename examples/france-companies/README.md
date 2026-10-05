# French Companies Scraper: SIRENE Leads, Directors & Emails

French companies API & SIRENE scraper: company data France, 26M+ companies (entreprises françaises) from the INSEE SIRENE register (SIREN, SIRET) by activity (NAF), area, size, revenue. Directors, finances, VAT, optional verified website, emails, phones: France B2B leads, no 10,000-result cap.

**Run it on Apify:** [apify.com/euroscrape/france-companies](https://apify.com/euroscrape/france-companies) (full documentation, pay per result, no subscription).

## Use it as an API

Get your token in [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~france-companies/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Use it from an AI agent (MCP)

Add this server to Claude, Cursor, VS Code or any MCP client: the Actor becomes a tool your agent can call.

```
https://mcp.apify.com?tools=euroscrape/france-companies
```

It is a pay-per-event Actor, so agents can also pay per run without an Apify account ([agentic payments](https://github.com/apify/apify-mcp-server#-agentic-payments)).

## Input

[`input.json`](input.json), ready to paste in Apify Console or to send to the API:

```json
{
  "nafCodes": [
    "43.22A"
  ],
  "departments": [
    "38"
  ],
  "employeeRanges": [
    "11",
    "12"
  ],
  "maxItems": 100,
  "findContacts": true
}
```

## Output

One real result, shortened ([`output-sample.json`](output-sample.json) has the full sample; personal data removed):

```json
{
  "siren": "501542021",
  "name": "SYSTEMES SOLAIRES",
  "legalName": "SYSTEMES SOLAIRES",
  "acronym": null,
  "status": "active",
  "createdAt": "2007-12-07",
  "ageYears": 18,
  "closedAt": null,
  "legalForm": {
    "code": "5599",
    "label": "SA à conseil d'administration (s.a.i.)"
  },
  "companyCategory": "PME",
  "nafCode": "43.22B",
  "nafLabel": "Travaux d’installation d’équipements thermiques et de climatisation",
  "sector": "F",
  "sectorLabel": "Construction",
  "employees": {
    "code": "12",
    "label": "20 à 49 salariés",
    "min": 20,
    "max": 49,
    "year": 2023
  },
  "isEmployer": null,
  "establishmentsCount": 273,
  "openEstablishmentsCount": 251,
  "headquarters": {
    "siret": "50154202100057",
    "isHeadquarters": true,
    "status": "active",
    "tradeName": null,
    "address": "20 RUE LE CORBUSIER 63800 COURNON-D'AUVERGNE",
    "postalCode": "63800",
    "city": "COURNON-D'AUVERGNE",
    "cityCode": "63124",
    "department": "63",
    "departmentName": "Puy-de-Dôme",
    "region": "84",
    "regionName": "Auvergne-Rhône-Alpes"
  },
  "matchingEstablishments": [],
  "latestFinances": {
    "year": 2024,
    "revenue": 36754436,
    "netIncome": 9196836,
    "revenueDisclosed": true
  },
  "financesHistory": [
    {
      "year": 2024,
      "revenue": 36754436,
      "netIncome": 9196836,
      "revenueDisclosed": true
    }
  ],
  "vatNumber": "FR02501542021",
  "labels": [
    "RGE"
  ],
  "collectiveAgreements": [
    "2420",
    "1597",
    "2609"
  ],
  "links": {
    "annuaireEntreprises": "https://annuaire-entreprises.data.gouv.fr/entreprise/501542021",
    "pappers": "https://www.pappers.fr/entreprise/501542021",
    "societeCom": "https://www.societe.com/cgi-bin/search?champs=501542021"
  },
  "changeType": null,
  "scrapedAt": "2026-09-29T13:25:01.228Z"
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

- Ready-made example: [Build a list of French plumbing companies by area](https://apify.com/euroscrape/france-companies/examples/french-plumbing-companies-with-contacts)
- Ready-made example: [Liste d'entreprises par code NAF et par département](https://apify.com/euroscrape/france-companies/examples/liste-entreprises-par-code-naf-et-departement)
- Article: [Build B2B lead lists from official company registers (France SIRENE and UK Companies House)](../../articles/05-company-registers-leads.md)
- [All EuroScrape Actors](../../README.md)
