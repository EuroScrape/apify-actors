# No-Website Leads: New Businesses Without a Website (US, UK, FR)

No-website leads API: newly registered companies without website, from registers of UK, France and 5 US states (Oregon, Texas, New York, Colorado, Connecticut). New business leads, new company leads, web design leads, web agency leads: newly incorporated companies, businesses without website.

**Run it on Apify:** [apify.com/euroscrape/no-website-leads](https://apify.com/euroscrape/no-website-leads) (full documentation, pay per result, no subscription).

## Use it as an API

Get your token in [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~no-website-leads/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Use it from an AI agent (MCP)

Add this server to Claude, Cursor, VS Code or any MCP client: the Actor becomes a tool your agent can call.

```
https://mcp.apify.com?tools=euroscrape/no-website-leads
```

It is a pay-per-event Actor, so agents can also pay per run without an Apify account ([agentic payments](https://github.com/apify/apify-mcp-server#-agentic-payments)).

## Input

[`input.json`](input.json), ready to paste in Apify Console or to send to the API:

```json
{
  "countries": [
    "UK",
    "FR"
  ],
  "registeredInLastDays": 7,
  "activityKeywords": [
    "restaurant",
    "cafe",
    "restauration"
  ],
  "ukLocations": [
    "Manchester",
    "Leeds"
  ],
  "frDepartments": [
    "69",
    "13"
  ],
  "output": "noWebsite",
  "maxItems": 100
}
```

## Output

One real result, shortened ([`output-sample.json`](output-sample.json) has the full sample; personal data removed):

```json
{
  "type": "lead",
  "country": "UK",
  "companyNumber": "17495516",
  "name": "TAP WAGON LTD",
  "tradeName": null,
  "legalForm": "Private limited company",
  "registeredOn": "2026-10-02",
  "publishedOn": null,
  "activity": "Event catering activities; Public houses and bars; Other amusement and recreation activities n.e.c.",
  "noActivityYet": null,
  "activityStartsOn": null,
  "sicCodes": [
    {
      "code": "56210",
      "description": "Event catering activities"
    },
    {
      "code": "56302",
      "description": "Public houses and bars"
    },
    {
      "code": "93290",
      "description": "Other amusement and recreation activities n.e.c."
    }
  ],
  "capital": null,
  "address": "•• Market Place, Cawood, Selby, England YO8 3SR",
  "postcode": "YO8 3SR",
  "city": "Selby",
  "area": null,
  "areaCode": "YO",
  "region": null,
  "sourceUrl": "https://find-and-update.company-information.service.gov.uk/company/17495516",
  "websiteStatus": "domain_registered",
  "website": null,
  "websiteConfidence": null,
  "emails": [],
  "primaryEmail": null,
  "phones": [],
  "socials": {},
  "domainsChecked": 10,
  "registeredDomains": [
    "tap-wagon.com",
    "tapwagon.co.uk",
    "tapwagon.com"
  ],
  "domain": "tapwagon.co.uk",
  "domainCreatedOn": "2026-09-28",
  "domainRecent": true,
  "domainPage": "no_response",
  "domainPageTitle": null,
  "ageDays": 2,
  "scrapedAt": "2026-10-04T04:31:59.945Z"
}
```

## Price

| Event | Price |
|---|---|
| Run start | $0.003 |
| No-website lead | $0.005 |
| New company with a website, or undecided | $0.002 |

Apify subscribers get 10–30% off depending on their plan.

## More

- Ready-made example: [Find new restaurants in Manchester that have no website yet](https://apify.com/euroscrape/no-website-leads/examples/new-manchester-restaurants-without-a-website)
- Ready-made example: [New companies that just bought a domain and have no website yet](https://apify.com/euroscrape/no-website-leads/examples/new-companies-that-just-bought-their-domain)
- Ready-made example: [Find new companies around Denver that have no website yet](https://apify.com/euroscrape/no-website-leads/examples/new-denver-companies-without-a-website)
- Ready-made example: [Find new companies around Houston that have no website yet](https://apify.com/euroscrape/no-website-leads/examples/new-houston-companies-without-a-website)
- Ready-made example: [List the new Texas LLCs and corporations of the last 30 days](https://apify.com/euroscrape/no-website-leads/examples/new-texas-llc-and-corporation-filings)
- Ready-made example: [Find new businesses in New York City with no website yet](https://apify.com/euroscrape/no-website-leads/examples/new-nyc-businesses-without-a-website)
- Ready-made example: [Build a mailing list of new Colorado businesses](https://apify.com/euroscrape/no-website-leads/examples/new-colorado-businesses-mailing-list)
- Ready-made example: [Find UK companies registered this week with no website](https://apify.com/euroscrape/no-website-leads/examples/new-uk-companies-without-a-website-this-week)
- Ready-made example: [Trouver les nouvelles entreprises sans site internet](https://apify.com/euroscrape/no-website-leads/examples/nouvelles-entreprises-sans-site-internet)
- Example project: [`leads.py`](../new-company-leads/leads.py), a single Python file to list this week's new companies in your town that have no website, the ones that just bought a domain first
- [All EuroScrape Actors](../../README.md)
