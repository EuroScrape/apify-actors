"""Online shops of a niche, ranked by the share of unhappy customers instead of by their stars.

Star ratings of online shops are nearly all the same: in a sample of 444 German shops, eight out of ten sit between
4.58 and 4.92. The share of 1 and 2 star reviews over the last twelve months separates them: it varies elevenfold
between the best and the worst tenth.

Runs the "Trusted Shops Scraper: Shop Leads, Ratings, Reviews & Alerts" Actor on Apify, prints the ranking
and writes shops.csv (shop, company, rating, reviews over 12 months, share of negative reviews, email, phone).

    pip install apify-client
    export APIFY_TOKEN=your_token
    python complaints.py fahrrad --country DE --shops 50 --min-reviews 100
"""
import argparse
import csv
import os


def ranking(items, min_reviews=100):
    """Shops with enough reviews to be compared, from the lowest share of 1-2 star reviews to the highest."""
    shops = [s for s in items if s.get("type") == "shop" and (s.get("reviewsLast12Months") or 0) >= min_reviews and s.get("stars")]
    for s in shops:
        s["negativeShare"] = 100 * (s["stars"]["1"] + s["stars"]["2"]) / s["reviewsLast12Months"]
    return sorted(shops, key=lambda s: s["negativeShare"])


def show(shops):
    print(f"{'shop':32} {'rating':>6} {'reviews/yr':>10} {'1-2 stars':>10}")
    for s in shops:
        print(f"{(s.get('domain') or s.get('name') or '')[:32]:32} {s.get('rating') or 0:>6.2f} {s['reviewsLast12Months']:>10} {s['negativeShare']:>9.1f}%")
    if shops:
        middle = shops[len(shops) // 2]["negativeShare"]
        print(f"\n{len(shops)} shops compared - median share of 1-2 star reviews: {middle:.1f}% - from {shops[0]['negativeShare']:.1f}% to {shops[-1]['negativeShare']:.1f}%")


def save(shops, path="shops.csv"):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["shop", "website", "company", "city", "country", "rating", "reviews_12_months", "negative_share_pct", "email", "phone"])
        for s in shops:
            w.writerow([s.get("name"), s.get("url"), s.get("companyName"), s.get("city"), s.get("countryCode"), s.get("rating"),
                        s["reviewsLast12Months"], round(s["negativeShare"], 2), s.get("email"), s.get("phone")])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("keywords", nargs="+", help='what the shops sell, in the language of the market: "fahrrad", "chaussures"…')
    parser.add_argument("--country", default="DE", help="DE, AT, CH, FR, ES, IT, NL, BE, PL, PT or GB")
    parser.add_argument("--shops", type=int, default=50, help="shops per keyword")
    parser.add_argument("--min-reviews", type=int, default=100, help="reviews over 12 months needed to be compared")
    args = parser.parse_args()

    from apify_client import ApifyClient

    client = ApifyClient(os.environ["APIFY_TOKEN"])
    run = client.actor("euroscrape/trusted-shops-scraper").call(run_input={
        "searchTerms": args.keywords,
        "countries": [args.country],
        "maxShopsPerSearch": args.shops,
        "membersOnly": True,
        "includeProfile": True,
    })
    shops = ranking(list(client.dataset(run["defaultDatasetId"]).iterate_items()), args.min_reviews)
    show(shops)
    save(shops)
    print("written: shops.csv")
