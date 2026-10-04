"""This week's new companies in your town that have no website, the ones that just bought a domain first.

Lists built from maps show businesses that have been open for years, and every agency has the same ones. A company
registered this week is on no map yet. In a sample of 160 companies registered in the UK and France between
28 September and 2 October 2026, 90 had no domain name at their name, and 28 had a domain with no site on it:
half of those domains had been created around the registration of the company.

Runs the "No-Website Leads: New Companies Without Website, UK, France, US" Actor on Apify, prints the leads and
writes leads.csv (company, activity, address, registered on, domain, domain created on, what answers there).

    pip install apify-client
    export APIFY_TOKEN=your_token
    python leads.py --uk Manchester Leeds --keywords restaurant cafe --days 14
    python leads.py --fr 69 13 --keywords coiffure --days 30
    python leads.py --us-states CO CT --us Denver Boulder Hartford --days 14
"""
import argparse
import csv
import os

ORDER = {"just bought a domain": 0, "no domain": 1, "old domain, no site": 2}


def kind(lead):
    """Why this company is a lead, from the warmest to the coldest."""
    if lead.get("websiteStatus") == "no_website_found":
        return "no domain"
    if lead.get("domainRecent"):
        return "just bought a domain"  # someone paid for the name and has not built the site
    return "old domain, no site"       # the name is taken or dormant: the company itself has no site


def ranking(items):
    """Leads only (companies with a site, or undecided, are left out), warmest first, then the most recent."""
    leads = [x for x in items if x.get("websiteStatus") in ("no_website_found", "domain_registered")]
    for x in leads:
        x["kind"] = kind(x)
    return sorted(leads, key=lambda x: (ORDER[x["kind"]], x.get("ageDays") if x.get("ageDays") is not None else 999))


def show(leads):
    print(f"{'company':34} {'town':16} {'registered':10} {'why':22} domain")
    for x in leads:
        day = x.get("registeredOn") or x.get("publishedOn") or ""
        domain = f"{x['domain']} (created {x.get('domainCreatedOn') or '?'}, {x.get('domainPage')})" if x.get("domain") else ""
        print(f"{(x.get('name') or '')[:34]:34} {(x.get('city') or '')[:16]:16} {day:10} {x['kind']:22} {domain}")
    counts = {k: sum(1 for x in leads if x["kind"] == k) for k in ORDER}
    print(f"\n{len(leads)} leads - " + ", ".join(f"{n} {k}" for k, n in counts.items()))


def save(leads, path="leads.csv"):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["company", "country", "activity", "address", "registered_on", "why", "domain", "domain_created_on", "domain_page", "official_record"])
        for x in leads:
            w.writerow([x.get("name"), x.get("country"), x.get("activity"), x.get("address"), x.get("registeredOn") or x.get("publishedOn"),
                        x["kind"], x.get("domain"), x.get("domainCreatedOn"), x.get("domainPage"), x.get("sourceUrl")])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--uk", nargs="*", default=[], help='UK towns, counties or postcodes: "Manchester", "SW1"')
    parser.add_argument("--fr", nargs="*", default=[], help='French department numbers: "69", "13", "2A"')
    parser.add_argument("--us", nargs="*", default=[], help='US cities or counties: "Denver", "Hartford", "Kings"')
    parser.add_argument("--us-states", nargs="*", default=[], help="US states among NY, CO and CT (default: the three of them)")
    parser.add_argument("--keywords", nargs="*", default=[], help='activity keywords (English for the UK, French for France): "restaurant", "coiffure"')
    parser.add_argument("--days", type=int, default=7, help="registered in the last N days")
    parser.add_argument("--max", type=int, default=100, help="maximum number of leads")
    args = parser.parse_args()

    from apify_client import ApifyClient

    countries = [c for c, places in (("UK", args.uk), ("FR", args.fr), ("US", args.us or args.us_states)) if places] or ["UK", "FR", "US"]
    client = ApifyClient(os.environ["APIFY_TOKEN"])
    run = client.actor("euroscrape/no-website-leads").call(run_input={
        "countries": countries,
        "registeredInLastDays": args.days,
        "ukLocations": args.uk,
        "frDepartments": args.fr,
        "usStates": args.us_states,
        "usLocations": args.us,
        "activityKeywords": args.keywords,
        "maxItems": args.max,
    })
    leads = ranking(list(client.dataset(run["defaultDatasetId"]).iterate_items()))
    show(leads)
    save(leads)
    print("written: leads.csv")
