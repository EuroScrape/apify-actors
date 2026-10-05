# Check a hotel's price on every booking site (and spot rate-parity gaps) without writing a scraper

Google Hotels quietly does something very useful: for any hotel and any dates, it lists the price on the hotel's own website **and** on Booking.com, Expedia, Agoda, Hotels.com, Trip.com and often 20+ other sites.

That's exactly what two kinds of people need:

- **Hotels and revenue managers**, who want to know if an online travel agency undercuts their official rate (a "rate parity" gap), on which dates, and by how much.
- **Travellers and deal hunters**, who want the cheapest night and the cheapest site for a stay.

The data is public, but collecting it at scale is painful: dates and guests are encoded in a binary URL parameter, prices sit in nested JavaScript arrays, pagination uses opaque tokens. So I packaged it as a cloud scraper you can just run: [Google Hotels Scraper: Prices from Every Booking Site](https://apify.com/euroscrape/google-hotels-prices) on Apify.

## What you get

One item per hotel and stay date, with every booking site in it. A real example (Amsterdam, 1 night, 2 adults):

```json
{
  "name": "DoubleTree by Hilton Amsterdam - NDSM Wharf",
  "checkIn": "2026-10-14",
  "checkOut": "2026-10-15",
  "currency": "EUR",
  "pricePerNight": 130.93,
  "dealLabel": "23% less than usual",
  "bookingSitesCount": 16,
  "cheapestSite": "DoubleTree by Hilton Amsterdam - NDSM Wharf",
  "officialSitePricePerNight": 130.93,
  "officialVsCheapestPct": 0,
  "bookingSites": [
    { "site": "DoubleTree by Hilton Amsterdam - NDSM Wharf", "isOfficialSite": true, "pricePerNight": 130.93 },
    { "site": "Qantas Hotels", "isOfficialSite": false, "pricePerNight": 134.45 },
    { "site": "KAYAK.fr", "isOfficialSite": false, "pricePerNight": 135.11 }
  ],
  "rating": 4.4,
  "reviewsCount": 1702,
  "hotelClass": 3,
  "address": "NDSM-Plein 28, 1033 WB Amsterdam, Netherlands"
}
```

Here the official website is the cheapest (`officialVsCheapestPct: 0`). That's not always the case: in my tests, a Paris hotel's official site was about 15–22% more expensive than the cheapest agency on the same nights.

## 1. Rate shopping: a few hotels, every night of next month

```json
{
  "hotels": ["Hotel Adlon Kempinski Berlin", "Regent Berlin", "Hotel de Rome Berlin"],
  "checkInDate": "2026-11-01",
  "numberOfDates": 30,
  "currency": "EUR"
}
```

You get 90 items (3 hotels × 30 nights) with every site's price, plus a free price-calendar summary per hotel: cheapest night, most expensive night, which site is most often the cheapest, and how often the official website is the cheapest.

Real calendar data for one hotel over 7 nights showed something you'd never see by checking manually: two nights at about €2,350 instead of €290 on *every* site, the kind of event-driven spike a revenue manager wants to know about early.

## 2. A destination: the cheapest good hotels for your dates

```json
{
  "locations": ["Lisbon"],
  "checkInDate": "2026-11-06",
  "nights": 2,
  "minRating": 4.2,
  "hotelClasses": ["4", "5"],
  "amenities": ["pool"],
  "sortBy": "lowest_price"
}
```

Each destination also gets a free summary: median price per night, price per star class, and a "best value" list (cheapest hotels rated 4.2+ with at least 50 reviews).

## 3. From Python

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")
run = client.actor("euroscrape/google-hotels-prices").call(run_input={
    "hotels": ["Hotel Adlon Kempinski Berlin"],
    "checkInDate": "2026-11-01",
    "numberOfDates": 14,
})
for x in client.dataset(run["defaultDatasetId"]).iterate_items():
    if x.get("type") == "hotel":
        print(x["checkIn"], x["pricePerNight"], x["cheapestSite"], x["officialVsCheapestPct"])
```

## 4. Price-drop alerts

Add a `monitorName`, schedule the Actor daily, and add a Telegram, Slack, Discord or webhook target. Each item then shows the price change since the previous run, and drops above your threshold (`alertOnPriceDropPct`, default 10%) send an alert.

## Cost

You pay per result: $0.002 per hotel and date, +$0.003 when you want every booking site's price, and $0.003 per run. Tracking 5 hotels over 30 dates is about $0.75.

## Limits, honestly

- Prices are what Google shows for the market you choose (`countryCode`), so a few sites may differ from what you see logged in on their own website.
- Hotels given by URL or exact name don't get the amenity list (Google opens their page directly and the list isn't always there).
- When nothing is bookable for your dates, you get `available: false` instead of a made-up price.

If you try it, I'd love feedback on the fields you'd want next.

Input templates and real sample outputs for this and other EuroScrape Actors are on GitHub: [EuroScrape/apify-actors](https://github.com/EuroScrape/apify-actors).

---

*Part of the [EuroScrape](https://apify.com/euroscrape) actor collection — [all articles](README.md).*
