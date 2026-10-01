"""Flight fare calendar: the cheapest day to fly on one or more routes.

Runs the "Google Flights Scraper: Cheapest Dates, Prices & Price History" Actor on Apify
(one cheapest flight per route and date), prints a calendar and writes fares.csv.

    pip install apify-client
    export APIFY_TOKEN=your_token
    python fare_calendar.py LIS-AMS MAD-ROM --days 30 --nonstop
"""
import argparse
import csv
import datetime as dt
import os

from apify_client import ApifyClient

parser = argparse.ArgumentParser()
parser.add_argument("routes", nargs="+", help='routes like "LIS-AMS" or "PAR-BCN"')
parser.add_argument("--days", type=int, default=14, help="number of departure dates")
parser.add_argument("--from-date", default=(dt.date.today() + dt.timedelta(days=21)).isoformat())
parser.add_argument("--trip-length", type=int, default=0, help="0 = one way, N = return after N days")
parser.add_argument("--nonstop", action="store_true")
parser.add_argument("--currency", default="EUR")
args = parser.parse_args()

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("euroscrape/google-flights-prices").call(run_input={
    "routes": args.routes,
    "departureDate": args.from_date,
    "numberOfDates": args.days,
    "tripLengthDays": args.trip_length,
    "maxStops": "nonstop" if args.nonstop else "any",
    "cheapestOnly": True,
    "currency": args.currency,
})

flights, summaries = [], []
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    (flights if item.get("type") == "flight" else summaries).append(item)

for s in summaries:
    print(f"\n{s['route']}: cheapest on {s['cheapestDepartureDate']} at {s['cheapestPrice']} {s['currency']}"
          f" (most expensive: {s['mostExpensiveDate']})")
    low = min((c["cheapestPrice"] for c in s["calendar"] if c["cheapestPrice"]), default=0)
    for c in s["calendar"]:
        if c["cheapestPrice"] is None:
            continue
        bar = "█" * max(1, round(c["cheapestPrice"] / low * 10)) if low else ""
        day = dt.date.fromisoformat(c["departureDate"]).strftime("%a %d %b")
        print(f"  {day}  {c['cheapestPrice']:>6}  {bar}")

with open("fares.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["route", "departure_date", "return_date", "price", "currency", "airline", "flight_numbers", "departure", "arrival", "stops"])
    for x in sorted(flights, key=lambda x: (x["route"], x["departureDate"])):
        writer.writerow([x["route"], x["departureDate"], x.get("returnDate"), x["price"], x["currency"], x.get("airline"),
                         " ".join(x.get("flightNumbers") or []), x.get("departure"), x.get("arrival"), x.get("stops")])
print(f"\n{len(flights)} fares written to fares.csv")
