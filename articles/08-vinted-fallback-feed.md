# When a Vinted search finds nothing, it quietly shows you popular junk - here is how to detect it

![cover](../assets/cover-vinted.png)

While building a [Vinted scraper](https://apify.com/euroscrape/vinted-scraper), my cloud test suite flagged something odd: a search for `zqxwcevrbtynumz introuvable` - deliberate nonsense - returned **50 items**. Dresses, sneakers, a phone case. All real listings, none related to the query.

Vinted does this on purpose: when a search has no real matches, the page is filled with popular listings so the user never sees an empty screen. Fine for shoppers. Terrible for a scraper that charges per item: users would pay for junk.

## The obvious signals don't work

Each listing in the server-rendered payload carries tracking data, so my first idea was to read it:

```json
{ "contentSource": "search", "searchScore": 1 }
```

`contentSource` stays `"search"` even for the fallback junk, and `searchScore` has the same decreasing values (1, 0.9999989…, 0.9999979…) on every page I compared - nonsense query or real one. No `isFallback` flag, no `emptyState` marker anywhere in the payload. I diffed the full set of JSON keys between a real search page and a nonsense one: **identical**.

## Title matching backfires

Second idea: keep only items whose title contains the searched words. It kills the junk, but it also killed legitimate results. Searching `gameboy` on vinted.de returns actual Game Boy games - titled "Super Mario Advance 4", "Tetris DX", "L'âge de glace"… Sellers title listings by the game's name, not the console's. My filter dropped all of them. Title relevance is a trap for marketplace search.

## The signature was in the pagination

The real tell is one number. Every search result page carries:

```json
"pagination": { "current_page": 1, "per_page": 96, "total_entries": 960 }
```

For real searches, `total_entries` is the (capped) result count: 960, 234, whatever. For every no-result search I could produce - on vinted.fr, vinted.de and vinted.co.uk, with nonsense text or with a real but impossible query like `gameboy advance sp ags 101 rouge` - it is **exactly 150**. The fallback feed is a fixed-size block of popular items, and its size is the signature.

One subtlety: the flight data contains several `total_entries` keys (favourites lists, other blocks), so you must read the one **immediately after** the items array, not the first match in the page.

## What the scraper does with it

```
total_entries == 150  → the market found nothing real:
                        keep only items that actually match the text (usually zero), bill nothing for junk
anything else         → trust Vinted's own ranking, deliver everything
```

The check runs per country, because a search can be empty in Germany and full in France. And a `strictMatching` option lets price researchers force title matching everywhere.

After the fix, the nonsense search returns 0 items and the gameboy search returns its 40 real games. The test suite is green, and nobody pays for a fallback feed.

The result, if you want to see it live: [Vinted Scraper on Apify](https://apify.com/euroscrape/vinted-scraper) - 26 countries, prices converted with ECB rates, alerts on new listings. Input templates: [github.com/EuroScrape/apify-actors](https://github.com/EuroScrape/apify-actors).

---

*Part of the [EuroScrape](https://apify.com/euroscrape) actor collection — [all articles](README.md).*
