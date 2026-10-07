---
title: Privacy policy
description: What the EuroScrape MCP server and the EuroScrape Actors do with your data.
---
# Privacy policy

Last updated: 7 October 2026. This page covers the [EuroScrape MCP server](https://github.com/EuroScrape/euroscrape-mcp) and the [EuroScrape Actors](https://apify.com/euroscrape) on Apify.

## Data collection

The MCP server runs on your own computer. EuroScrape collects nothing through it: no analytics, no telemetry, no account, no cookies. This website is a static site hosted on GitHub Pages and sets no cookies of its own.

## Usage and storage

When your AI assistant calls a tool, the server sends the tool's arguments to the Apify API (`https://api.apify.com`) with your Apify API token, so that the Actor runs on your own Apify account, and it returns the results to your MCP client. The token is read from your configuration and sent only to Apify. The server writes nothing to disk.

The inputs and results of a run are stored in your Apify account, under your control.

## Third-party sharing

Your requests go to Apify, which runs the Actors and bills you: see [Apify's privacy policy](https://apify.com/privacy-policy). The Actors read the public sources named on each Actor page (official registers, open data portals, public web pages). Nothing is sent to anyone else.

As the publisher of the Actors, EuroScrape sees only aggregate statistics provided by Apify (number of runs and users, success rate). It does not see your inputs, your results or your logs, unless you choose to share a run with the developer in Apify Console.

## Data retention

EuroScrape retains none of your data. Runs and datasets in your Apify account are kept for the retention period of your Apify plan, and you can delete them at any time in Apify Console.

## Contact

Questions about this policy: open an issue at [github.com/EuroScrape/euroscrape-mcp/issues](https://github.com/EuroScrape/euroscrape-mcp/issues).
