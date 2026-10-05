# Examples: one page per Actor, and five small projects

Each Actor has a page with what it returns, the API call, the MCP server URL for AI agents, its price, a ready-to-paste input and a real result.

## Actors

**Travel prices**

- [Google Flights Scraper: Cheapest Dates, Prices & Price History](google-flights-prices/README.md)
- [Google Hotels Scraper (Google Travel): Prices on Booking Sites](google-hotels-prices/README.md)
- [Ryanair Low Fare Finder: Cheapest Days, Anywhere & Alerts](ryanair-low-fares/README.md)

**Company data and B2B leads**

- [French Companies Scraper: SIRENE Leads, Directors & Emails](france-companies/README.md)
- [UK Companies House API & Scraper: UK Company Data & B2B Leads](uk-companies/README.md)
- [Impressum & Legal Notice Scraper: VAT, Registry, Contacts](company-identity/README.md)
- [EU VAT Number Validator (VIES): Bulk Check, Proof & Alerts](vat-validator/README.md)
- [Website Technology Stack Detector: Tech Stack API, CMS & Leads](website-intelligence/README.md)
- [Trusted Shops Scraper: Shop Leads, Ratings, Reviews & Alerts](trusted-shops-scraper/README.md)
- [No-Website Leads: New Businesses Without a Website (US, UK, FR)](no-website-leads/README.md)

**Real estate and energy (France, EU)**

- [France Real Estate Sold Prices (DVF): €/m², Sales & Trends](france-property-prices/README.md)
- [France Energy Ratings (DPE): Homes, Energy Certificates, Sieves](france-energy-ratings/README.md)
- [France Building Permits (Sitadel): Projects, Builders & Alerts](france-building-permits/README.md)
- [EU Electricity Prices API: Day-Ahead Power Prices & Cheap Hours](eu-electricity-prices/README.md)
- [France Fuel Prices: Gas Station Prices, Diesel Prices & Alerts](france-fuel-prices/README.md)

**Second-hand marketplaces**

- [Vinted Scraper & Vinted API: 26 Countries, Deals & Alerts](vinted-scraper/README.md)
- [Kleinanzeigen Scraper & Kleinanzeigen API: Deals & Alerts](kleinanzeigen-scraper/README.md)
- [EU Second-Hand Marketplaces Scraper: Vinted, OLX & More](eu-marketplace-deals/README.md)

**Public tenders and app reviews**

- [EU Public Tenders Scraper: TED, BOAMP, Awards & Tender Alerts](eu-public-tenders/README.md)
- [App Store Reviews Scraper + Google Play Reviews (All Countries)](app-reviews/README.md)

## Example projects

Single-file Python scripts that call an Actor and do something useful with the result:

- [`flight-fare-calendar/fare_calendar.py`](https://github.com/EuroScrape/apify-actors/blob/main/examples/flight-fare-calendar/fare_calendar.py): print the cheapest day to fly on your routes as a fare calendar
- [`hotel-rate-parity-monitor/parity.py`](https://github.com/EuroScrape/apify-actors/blob/main/examples/hotel-rate-parity-monitor/parity.py): check whether a hotel's official site is the cheapest place to book it
- [`shop-complaint-rate/complaints.py`](https://github.com/EuroScrape/apify-actors/blob/main/examples/shop-complaint-rate/complaints.py): rank the shops of a niche by their share of 1 and 2 star reviews
- [`eu-tenders-slack-alerts/tenders.py`](https://github.com/EuroScrape/apify-actors/blob/main/examples/eu-tenders-slack-alerts/tenders.py): post new tenders matching your keywords to Slack, daily
- [`new-company-leads/leads.py`](https://github.com/EuroScrape/apify-actors/blob/main/examples/new-company-leads/leads.py): list this week's new companies in your town that have no website, the ones that just bought a domain first

[All EuroScrape Actors](../README.md)
