# Impressum & Legal Notice Scraper: VAT, Registry, Contacts

Impressum scraper and legal notice scraper (imprint, mentions légales): find the website owner of any company website in Europe — legal entity name, registry numbers (HRB, SIREN, KvK, BCE, UK no.), VAT IDs, directors, address, emails, phones. From URLs or Google searches. Checked for France & UK.

**Run it on Apify:** [apify.com/euroscrape/company-identity](https://apify.com/euroscrape/company-identity) (full documentation, pay per result, no subscription).

## Use it as an API

Get your token in [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~company-identity/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Use it from an AI agent (MCP)

Add this server to Claude, Cursor, VS Code or any MCP client: the Actor becomes a tool your agent can call.

```
https://mcp.apify.com?tools=euroscrape/company-identity
```

It is a pay-per-event Actor, so agents can also pay per run without an Apify account ([agentic payments](https://github.com/apify/apify-mcp-server#-agentic-payments)).

## Input

[`input.json`](input.json), ready to paste in Apify Console or to send to the API:

```json
{
  "searchQueries": [
    "Tischlerei München"
  ],
  "searchCountry": "de",
  "resultsPerQuery": 20,
  "skipWithoutIdentity": true
}
```

## Output

One real result, shortened ([`output-sample.json`](output-sample.json) has the full sample; personal data removed):

```json
{
  "url": "https://www.grenoble-emplois.com/",
  "domain": "grenoble-emplois.com",
  "source": "google",
  "query": "menuisier Grenoble",
  "finalUrl": "https://www.grenoble-emplois.com/",
  "reachable": true,
  "legalNoticeUrl": "https://www.grenoble-emplois.com/infos-legales.html",
  "country": "FR",
  "companyName": "HelloWork SASU",
  "tradeName": null,
  "legalForm": "SASU",
  "registrations": [
    {
      "type": "FR_SIREN",
      "value": "428843130",
      "registry": "RCS RENNES"
    }
  ],
  "vatIds": [
    "FR69428843130"
  ],
  "shareCapital": 168672,
  "address": {
    "street": "2, rue de la Mabilais",
    "postalCode": "35000",
    "city": "RENNES"
  },
  "emails": [
    "contact@hellowork.com"
  ],
  "phones": [
    "+33223448044",
    "+33223448045",
    "+33299125757"
  ],
  "socials": {
    "facebook": "https://www.facebook.com/helloworkcom/",
    "linkedin": "https://www.linkedin.com/company/helloworkcom/",
    "x": "https://twitter.com/hellowork"
  },
  "primaryEmail": "contact@hellowork.com",
  "primaryRegistration": {
    "type": "FR_SIREN",
    "value": "428843130",
    "registry": "RCS RENNES"
  },
  "pagesScanned": [
    "https://www.grenoble-emplois.com/infos-legales.html",
    "https://www.grenoble-emplois.com/"
  ],
  "registryCheck": {
    "country": "FR",
    "source": "INSEE/INPI (recherche-entreprises.api.gouv.fr)",
    "id": "428843130",
    "found": true,
    "officialName": "HELLOWORK",
    "status": "active",
    "nameMatches": true,
    "createdAt": "2000-01-01",
    "nafCode": "63.12Z",
    "nafLabel": "Portails Internet",
    "employees": "500 à 999 salariés",
    "headquarters": "2 RUE DE LA MABILAIS 35000 RENNES"
  },
  "scrapedAt": "2026-09-29T13:26:47.639Z"
}
```

## Price

| Event | Price |
|---|---|
| Run start | $0.003 |
| Website identified | $0.004 |
| Google search page | $0.004 |

Apify subscribers get 10–30% off depending on their plan.

## More

- Ready-made example: [Extract the legal identity behind any European website](https://apify.com/euroscrape/company-identity/examples/legal-identity-behind-any-eu-website)
- Ready-made example: [Find the company behind any German online shop](https://apify.com/euroscrape/company-identity/examples/find-the-company-behind-any-german-shop)
- Ready-made example: [Trouver la société derrière un site web (mentions légales)](https://apify.com/euroscrape/company-identity/examples/trouver-la-societe-derriere-un-site-web)
- [All EuroScrape Actors](../../README.md)
