# Google Flights Scraper: Cheapest Dates, Prices & Price History

Unofficial Google Flights API and flight price tracker to find cheap flight tickets: airfare from Google Flights for any route and dates — airlines, times, stops, CO2, typical price range and flight price history, cheapest day to fly (flight price calendar), round trips and price-drop alerts.

**Run it on Apify:** [apify.com/euroscrape/google-flights-prices](https://apify.com/euroscrape/google-flights-prices) (full documentation, pay per result, no subscription).

## Use it as an API

Get your token in [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~google-flights-prices/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Use it from an AI agent (MCP)

Add this server to Claude, Cursor, VS Code or any MCP client: the Actor becomes a tool your agent can call.

```
https://mcp.apify.com?tools=euroscrape/google-flights-prices
```

It is a pay-per-event Actor, so agents can also pay per run without an Apify account ([agentic payments](https://github.com/apify/apify-mcp-server#-agentic-payments)).

## Input

[`input.json`](input.json), ready to paste in Apify Console or to send to the API:

```json
{
  "routes": [
    "PAR-BCN"
  ],
  "departureDate": "2026-11-06",
  "numberOfDates": 8,
  "daysBetweenDates": 7,
  "tripLengthDays": 2,
  "adults": 2
}
```

## Output

One real result, shortened ([`output-sample.json`](output-sample.json) has the full sample; personal data removed):

```json
{
  "type": "flight",
  "route": "PAR-BCN",
  "origin": "PAR",
  "destination": "BCN",
  "departureDate": "2026-11-12",
  "returnDate": "2026-11-16",
  "tripType": "round_trip",
  "adults": 1,
  "children": 0,
  "cabinClass": "economy",
  "currency": "EUR",
  "price": 80,
  "pricePerPassenger": 80,
  "priceLevel": "high",
  "typicalPriceLow": 50,
  "typicalPriceHigh": 130,
  "isBestFlight": true,
  "airline": "Ryanair",
  "airlines": [
    "Ryanair"
  ],
  "airlineCode": "FR",
  "flightNumbers": [
    "FR 3122"
  ],
  "departureAirport": "BVA",
  "arrivalAirport": "BCN",
  "departure": "2026-11-12T14:05",
  "arrival": "2026-11-12T15:50",
  "durationMinutes": 105,
  "stops": 0,
  "layovers": []
}
```

## Price

| Event | Price |
|---|---|
| Run start | $0.003 |
| Flight delivered | $0.002 |

Apify subscribers get 10–30% off depending on their plan.

## More

- Ready-made example: [Find the cheapest day to fly Berlin to Alicante](https://apify.com/euroscrape/google-flights-prices/examples/cheapest-day-to-fly-berlin-alicante)
- Ready-made example: [Find the cheapest day to fly Paris to New York](https://apify.com/euroscrape/google-flights-prices/examples/cheapest-day-to-fly-paris-new-york)
- Ready-made example: [Find the cheapest day to fly New York to London](https://apify.com/euroscrape/google-flights-prices/examples/cheapest-day-to-fly-new-york-london)
- Ready-made example: [Find the cheapest day to fly Los Angeles to Honolulu](https://apify.com/euroscrape/google-flights-prices/examples/cheapest-day-to-fly-los-angeles-honolulu)
- Ready-made example: [Track a flight's price and get alerts when it drops](https://apify.com/euroscrape/google-flights-prices/examples/flight-price-tracker-with-price-drop-alerts)
- Article: [The same flight cost $362 or $162 depending on the day - building a fare calendar from Google Flights](../../articles/06-google-flights-calendar.md)
- Example project: [`fare_calendar.py`](../flight-fare-calendar/fare_calendar.py), a single Python file to print the cheapest day to fly on your routes as a fare calendar
- [All EuroScrape Actors](../../README.md)
