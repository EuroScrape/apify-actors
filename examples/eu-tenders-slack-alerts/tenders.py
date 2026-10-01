"""EU public tenders to Slack: post new tenders matching your keywords and categories.

Runs the "EU Public Tenders Scraper: TED, BOAMP, Procurement & Awards" Actor on Apify with a monitor,
so each run only returns tenders it hasn't seen before, and posts them to a Slack channel.
Schedule it once a day (cron, GitHub Actions or an Apify schedule).

    pip install apify-client requests
    export APIFY_TOKEN=your_token
    export SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...
    python tenders.py --keywords "software" "cloud" --cpv 72 48 --countries DE AT FR
"""
import argparse
import os

import requests
from apify_client import ApifyClient

parser = argparse.ArgumentParser()
parser.add_argument("--keywords", nargs="*", default=[])
parser.add_argument("--cpv", nargs="*", default=[], help='CPV prefixes, e.g. 72 (IT services), 45 (construction)')
parser.add_argument("--countries", nargs="*", default=[], help="2-letter codes, empty = all of Europe")
parser.add_argument("--monitor", default="my-tenders", help="monitor name: keeps track of tenders already seen")
parser.add_argument("--dry-run", action="store_true", help="print instead of posting to Slack")
args = parser.parse_args()

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("euroscrape/eu-public-tenders").call(run_input={
    "mode": "tenders",
    "keywords": args.keywords,
    "cpvCodes": args.cpv,
    "countries": args.countries,
    "publishedWithinDays": 3,
    "monitorName": args.monitor,
    "includeSummary": False,
})
tenders = [x for x in client.dataset(run["defaultDatasetId"]).iterate_items() if x.get("type") == "tender"]
# the first run of a monitor saves the current tenders as the baseline (changeType is empty);
# from the next run on, only tenders published since then come back, with changeType "new"
new = [t for t in tenders if t.get("changeType") == "new"]
if tenders and not new:
    print(f"First run: {len(tenders)} matching tender(s) saved as the baseline. New ones are posted from the next run.")

for t in (tenders if args.dry_run else new):
    value = f"{t['estimatedValueEur']:,.0f} €" if t.get("estimatedValueEur") else "value not published"
    deadline = (t.get("deadline") or "")[:10] or "no deadline"
    text = (f"*<{t['url']}|{t['title'][:150]}>*\n"
            f"{t.get('buyerName')} · {t.get('countryName')} · {t.get('mainCpvLabel')}\n"
            f"{value} · deadline {deadline}")
    if args.dry_run:
        print(text.replace("*", ""), "\n")
    else:
        requests.post(os.environ["SLACK_WEBHOOK_URL"], json={"text": text}, timeout=30)

print(f"{len(new)} new tender(s)" + ("" if args.dry_run else " posted to Slack"))
