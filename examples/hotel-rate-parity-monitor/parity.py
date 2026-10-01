"""Hotel rate-parity monitor: is a hotel's official website the cheapest place to book it?

Runs the "Google Hotels Scraper: Prices from Every Booking Site" Actor on Apify for a few hotels
and the next N nights, then prints a parity table and writes parity.csv.

    pip install apify-client
    export APIFY_TOKEN=your_token
    python parity.py "Hotel Adlon Kempinski Berlin" "Regent Berlin" --nights 14
"""
import argparse
import csv
import datetime as dt
import os

from apify_client import ApifyClient

parser = argparse.ArgumentParser()
parser.add_argument("hotels", nargs="+", help="hotel names or Google Hotels URLs")
parser.add_argument("--nights", type=int, default=7, help="number of check-in dates to check")
parser.add_argument("--from-date", default=(dt.date.today() + dt.timedelta(days=14)).isoformat())
parser.add_argument("--currency", default="EUR")
args = parser.parse_args()

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("euroscrape/google-hotels-prices").call(run_input={
    "hotels": args.hotels,
    "checkInDate": args.from_date,
    "numberOfDates": args.nights,
    "currency": args.currency,
})

rows = []
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    if item.get("type") != "hotel":
        continue
    rows.append({
        "hotel": item["name"],
        "check_in": item["checkIn"],
        "cheapest_site": item.get("cheapestSite"),
        "cheapest_price": item.get("cheapestSitePricePerNight"),
        "official_price": item.get("officialSitePricePerNight"),
        "official_vs_cheapest_pct": item.get("officialVsCheapestPct"),
        "booking_sites": item.get("bookingSitesCount"),
        "available": item.get("available"),
    })

rows.sort(key=lambda r: (r["hotel"], r["check_in"]))
print(f"{'Hotel':38} {'Check-in':10} {'Cheapest site':22} {'Cheapest':>9} {'Official':>9} {'Gap':>6}")
for r in rows:
    gap = "" if r["official_vs_cheapest_pct"] is None else f"{r['official_vs_cheapest_pct']:+.0f}%"
    print(f"{r['hotel'][:38]:38} {r['check_in']:10} {str(r['cheapest_site'])[:22]:22} "
          f"{r['cheapest_price'] or '-':>9} {r['official_price'] or '-':>9} {gap:>6}")

with open("parity.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]) if rows else ["hotel"])
    writer.writeheader()
    writer.writerows(rows)
print(f"\n{len(rows)} rows written to parity.csv")
