# EU VAT Number Validator (VIES): Bulk Check, Proof & Alerts

VAT validation API & VAT number scraper: validate EU VAT numbers (numéro de TVA intracommunautaire, USt-IdNr) in bulk against VIES, the European Commission's official registry — company name and address, official consultation proof for tax audits, alerts when a customer's number becomes invalid.

**Run it on Apify:** [apify.com/euroscrape/vat-validator](https://apify.com/euroscrape/vat-validator) (full documentation, pay per result, no subscription).

## Use it as an API

Get your token in [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~vat-validator/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Use it from an AI agent (MCP)

Add this server to Claude, Cursor, VS Code or any MCP client: the Actor becomes a tool your agent can call.

```
https://mcp.apify.com?tools=euroscrape/vat-validator
```

It is a pay-per-event Actor, so agents can also pay per run without an Apify account ([agentic payments](https://github.com/apify/apify-mcp-server#-agentic-payments)).

## Input

[`input.json`](input.json), ready to paste in Apify Console or to send to the API:

```json
{
  "vatNumbers": [
    "FR40303265045",
    "IE6388047V",
    "PL5260250995",
    "FR00000000000"
  ],
  "requesterVatNumber": "FR40303265045"
}
```

## Output

One real result, shortened ([`output-sample.json`](output-sample.json) has the full sample; personal data removed):

```json
{
  "type": "vat",
  "input": "IE 6388047V",
  "countryCode": "IE",
  "vatNumber": "6388047V",
  "vatNumberFormatted": "IE6388047V",
  "syntaxValid": true,
  "valid": true,
  "companyName": "GOOGLE IRELAND LIMITED",
  "companyAddress": "3RD FLOOR, GORDON HOUSE, BARROW STREET, DUBLIN 4",
  "consultationNumber": "WAPIAAAAaD5Jk8-i",
  "memberStateUnavailable": false,
  "checkedAt": "2026-10-01T20:27:12.735Z"
}
```

## Price

| Event | Price |
|---|---|
| Run start | $0.003 |
| VAT number checked | $0.002 |

Apify subscribers get 10–30% off depending on their plan.

## More

- Ready-made example: [Check EU VAT numbers in bulk against VIES](https://apify.com/euroscrape/vat-validator/examples/check-eu-vat-numbers-in-bulk)
- Ready-made example: [Monitor your partners' VAT numbers and catch invalid ones](https://apify.com/euroscrape/vat-validator/examples/monitor-vat-numbers-alert-when-invalid)
- Ready-made example: [Vérifier des numéros de TVA intracommunautaire en masse](https://apify.com/euroscrape/vat-validator/examples/verifier-numeros-tva-intracommunautaire-en-masse)
- Ready-made example: [USt-IdNr. prüfen: Massenabfrage über VIES mit Nachweis](https://apify.com/euroscrape/vat-validator/examples/ust-idnr-pruefen-massenabfrage)
- Article: [Zero-rating an intra-EU invoice? Without a VIES consultation number, you may owe the VAT yourself](../../articles/09-vat-vies-proof.md)
- [All EuroScrape Actors](../../README.md)
