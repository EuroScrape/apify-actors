# Website Technology Stack Detector: Tech Stack API, CMS & Leads

Website technology detector & tech stack API: technology detection and CMS detection for any website (280+ technologies: e-commerce, analytics, consent, booking…), plus company identity (legal name, VAT, directors, emails, phones) and sales signals for technology leads (old WordPress, no HTTPS).

**Run it on Apify:** [apify.com/euroscrape/website-intelligence](https://apify.com/euroscrape/website-intelligence) (full documentation, pay per result, no subscription).

## Use it as an API

Get your token in [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~website-intelligence/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Use it from an AI agent (MCP)

Add this server to Claude, Cursor, VS Code or any MCP client: the Actor becomes a tool your agent can call.

```
https://mcp.apify.com?tools=euroscrape/website-intelligence
```

It is a pay-per-event Actor, so agents can also pay per run without an Apify account ([agentic payments](https://github.com/apify/apify-mcp-server#-agentic-payments)).

## Input

[`input.json`](input.json), ready to paste in Apify Console or to send to the API:

```json
{
  "searchQueries": [
    "plombier Lyon"
  ],
  "searchCountry": "fr",
  "resultsPerQuery": 20
}
```

## Output

One real result, shortened ([`output-sample.json`](output-sample.json) has the full sample; personal data removed):

```json
{
  "url": "https://ubiagarage.de/",
  "domain": "ubiagarage.de",
  "source": "input",
  "query": null,
  "finalUrl": "https://ubiagarage.de/",
  "redirectedToDomain": null,
  "reachable": true,
  "technologies": [
    {
      "name": "WordPress",
      "category": "cms",
      "categoryLabel": "CMS",
      "version": null,
      "evidence": [
        "html"
      ]
    },
    {
      "name": "WooCommerce",
      "category": "ecommerce",
      "categoryLabel": "E-commerce",
      "version": null,
      "evidence": [
        "html"
      ]
    },
    {
      "name": "Divi",
      "category": "page-builder",
      "categoryLabel": "Page builder",
      "version": null,
      "evidence": [
        "html"
      ]
    }
  ],
  "technologyNames": [
    "WordPress",
    "WooCommerce",
    "Divi"
  ],
  "technologiesByCategory": {
    "cms": [
      "WordPress"
    ],
    "ecommerce": [
      "WooCommerce"
    ],
    "page-builder": [
      "Divi",
      "Gutenberg blocks"
    ],
    "consent": [
      "Usercentrics"
    ],
    "server": [
      "Nginx"
    ],
    "js-library": [
      "jQuery 3.7.1"
    ]
  },
  "cms": "WordPress",
  "ecommercePlatform": "WooCommerce",
  "platformSummary": "WordPress + WooCommerce + Divi",
  "opportunityScore": 7,
  "salesSignals": [
    {
      "code": "no_analytics",
      "severity": 1,
      "label": "No analytics detected: they cannot measure their marketing."
    }
  ],
  "audit": {
    "https": true,
    "statusCode": 200,
    "responseTimeMs": 686,
    "totalLoadMs": 1111,
    "htmlSizeKb": 142,
    "mobileViewport": true,
    "title": "Ubiagarage Köln - Ihre Autowerkstatt in Köln › Ubiagarage Köln",
    "metaDescription": "Die freie Autowerkstatt in Köln. Unfallreparatur, Reifenwechsel, Scheibentausch, Fehlerdiagnose, kommen Sie zu uns. Vereinbaren Sie einen…",
    "language": "de",
    "sslIssuer": "Let's Encrypt",
    "sslValidTo": "2026-12-24T21:42:23.000Z",
    "sslDaysLeft": 86
  },
  "socials": {},
  "country": "DE",
  "companyName": "UBIA–Garage",
  "tradeName": null,
  "legalForm": null,
  "registrations": [],
  "vatIds": [
    "DE180343005"
  ],
  "address": {
    "street": "Rondorfer Str. 30",
    "postalCode": "50354",
    "city": "Hürth"
  },
  "emails": [
    "info@ubia-garage.de"
  ],
  "primaryEmail": "info@ubia-garage.de",
  "phones": [
    "+49941104929"
  ],
  "legalNoticeUrl": "https://ubiagarage.de/impressum/"
}
```

## Price

| Event | Price |
|---|---|
| Run start | $0.003 |
| Website analyzed | $0.02 |
| Google search page | $0.004 |

Apify subscribers get 10–30% off depending on their plan.

## More

- Ready-made example: [tech stack and sales signals of a website](https://apify.com/euroscrape/website-intelligence/examples/tech-stack-and-sales-signals-of-a-website)
- Article: [Find websites running WordPress, WooCommerce or Shopify - and the ones that need your help](../../articles/04-tech-stack-leads.md)
- [All EuroScrape Actors](../../README.md)
