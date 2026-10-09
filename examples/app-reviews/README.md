# App Store Reviews Scraper + Google Play Reviews (All Countries)

Mobile app reviews: App Store reviews API and Google Play reviews API in 58 countries — iOS reviews and Android reviews (Play Store reviews) with rating, text, version, date, developer reply, app details and a free summary (rating by version and country). Alerts on new negative app reviews.

**Run it on Apify:** [apify.com/euroscrape/app-reviews](https://apify.com/euroscrape/app-reviews) (full documentation, pay per result, no subscription).

## Use it as an API

Get your token in [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~app-reviews/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Use it from an AI agent (MCP)

Add this server to Claude, Cursor, VS Code or any MCP client: the Actor becomes a tool your agent can call.

```
https://mcp.apify.com?tools=euroscrape/app-reviews
```

It is a pay-per-event Actor, so agents can also pay per run without an Apify account ([agentic payments](https://github.com/apify/apify-mcp-server#-agentic-payments)).

## Input

[`input.json`](input.json), ready to paste in Apify Console or to send to the API:

```json
{
  "appNames": [
    "Duolingo"
  ],
  "countries": [
    "us",
    "gb",
    "fr",
    "de"
  ],
  "maxReviewsPerCountry": 50
}
```

## Output

One real result, shortened ([`output-sample.json`](output-sample.json) has the full sample; personal data removed):

```json
{
  "type": "review",
  "store": "Google Play",
  "appId": "com.spotify.music",
  "appName": "Spotify: Music and Podcasts",
  "country": "us",
  "countryName": "United States",
  "language": "en",
  "reviewId": "de82d3cb-4b4a-43e9-9814-906e71b4ffb9",
  "rating": 5,
  "title": null,
  "text": "I just updated the app today and its now unusable. It wouldnt connect to the internet, or show my profile or playlists. I tried to uninst…",
  "version": "9.1.86.2432",
  "date": "2026-09-29T19:17:03.870Z",
  "helpfulCount": 0,
  "developerReply": "Hi! This should be fixed now. If you're still having issues, we'd recommend reinstalling the app. If that doesn't help, reach out to our …",
  "developerReplyDate": "2026-09-30T14:45:32.400Z",
  "url": "https://play.google.com/store/apps/details?id=com.spotify.music&reviewId=de82d3cb-4b4a-43e9-9814-906e71b4ffb9",
  "changeType": null,
  "scrapedAt": "2026-09-30T19:23:08.022Z"
}
```

## Price

| Event | Price |
|---|---|
| Run start | $0.003 |
| Review delivered | $0.0002 |

Apify subscribers get 10–30% off depending on their plan.

## More

- Ready-made example: [Track negative App Store and Google Play reviews](https://apify.com/euroscrape/app-reviews/examples/track-negative-app-reviews-spotify)
- Ready-made example: [Export the Google Play reviews of any app](https://apify.com/euroscrape/app-reviews/examples/export-google-play-reviews-of-any-app)
- Article: [Get every new 1-star review of your app in Slack (App Store and Google Play, 58 countries)](../../articles/07-app-reviews-alerts.md)
- Article: [Duolingo is rated 4.7 in both app stores, and its newest reviews in Germany average 3.1 - what a store rating hides, country by country](../../articles/18-duolingo-reviews-by-country.md)
- [All EuroScrape Actors](../../README.md)
