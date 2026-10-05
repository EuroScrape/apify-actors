# The same flight cost $362 or $162 depending on the day - building a fare calendar from Google Flights

![cover](../assets/cover-google-flights.png)

Nonstop Lisbon → Amsterdam, two adults, one way. Same route, same airlines, same week:

| Departure | Cheapest fare |
|---|---|
| Mon 2 Nov | $362 |
| Tue 3 Nov | $234 |
| Wed 4 Nov | $183 |
| Thu 5 Nov | $183 |
| Fri 6 Nov | $205 |
| Sat 7 Nov | $263 |
| Sun 8 Nov | $326 |
| Mon 9 Nov | $293 |
| Tue 10 Nov | $183 |
| Wed 11 Nov | $162 |

Flying on the Wednesday instead of the Monday saves **$200 (55%)**. Google Flights shows this in its date grid, but only for one route at a time and only on screen. I wanted it as data, for many routes, refreshed every day, so I built [Google Flights Scraper: Cheapest Dates, Prices & Price History](https://apify.com/euroscrape/google-flights-prices) on Apify.

## A fare calendar in one input

```json
{
  "routes": ["LIS-AMS", "MAD-ROM", "PAR-BCN"],
  "departureDate": "2026-11-02",
  "numberOfDates": 30,
  "maxStops": "nonstop",
  "cheapestOnly": true
}
```

`cheapestOnly` keeps one flight per route and date, the cheapest, so a 30-day calendar for one route is 30 results (about $0.06). Each route also gets a free summary with the cheapest departure date, the most expensive one, the cheapest fare per airline and the full calendar.

City codes cover every airport of a city: `PAR` includes CDG, Orly and Beauvais, `LON` all London airports, `NYC` JFK, Newark and LaGuardia.

## Round trips and weekends

```json
{ "routes": ["PAR-BCN"], "departureDate": "2026-11-06", "numberOfDates": 8, "daysBetweenDates": 7, "tripLengthDays": 2, "adults": 2 }
```

That's every Friday-to-Sunday weekend for two months. Prices are totals for all passengers (round-trip totals for round trips), with `pricePerPassenger` alongside.

## More than the price

Each flight comes with flight numbers, times, duration, stops and layover durations, aircraft, legroom, and **CO2 emissions** compared with the typical flight on the route. A real one:

```json
{
  "route": "PAR-BCN",
  "price": 106,
  "airline": "Vueling",
  "flightNumbers": ["VY 8061"],
  "departure": "2026-11-12T09:50",
  "arrival": "2026-11-12T11:45",
  "stops": 0,
  "aircraft": ["Airbus A320"],
  "co2Kg": 88,
  "co2TypicalKg": 84,
  "priceLevel": "typical",
  "typicalPriceLow": 50,
  "typicalPriceHigh": 130
}
```

`priceLevel` says whether the fare is low, typical or high compared with Google's typical range for that trip. When Google shows them, the summary also includes about 60 days of price history and the train alternative (Paris → Barcelona: 6 h 50 by train, departing Gare de Lyon).

## Alerts

Add a `monitorName`, schedule the Actor every morning, add a Telegram, Slack, Discord or webhook target, and you get an alert when a fare drops by more than `alertOnPriceDropPct` (10% by default).

Input templates and sample outputs: [github.com/EuroScrape/apify-actors](https://github.com/EuroScrape/apify-actors).

---

*Part of the [EuroScrape](https://apify.com/euroscrape) actor collection — [all articles](README.md).*
