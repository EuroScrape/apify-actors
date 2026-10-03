# Companies file 1 French building permit in 5 and build 3 homes in 4 - and the register names them 8 months before the site opens

![cover](../assets/cover-building-permits.png)


Every building permit granted in France ends up in a national register called Sitadel, and the Ministry's statistics office publishes it as open data every month: 1.9 million permits creating dwellings since 2013, 800,000 for non-residential buildings. It is one of the most commercially useful public datasets in the country, and it is little known outside the construction trade.

I spent a day with it. Three things stood out.

## 1. One permit in five, three homes in four

Most housing permits are a private individual building one house. Over the last twelve months, in eight large departments (Isère, Rhône, Gironde, Loire-Atlantique, Nord, Haute-Garonne, Bouches-du-Rhône, Ille-et-Vilaine):

- companies and public bodies filed **19% of the housing permits**;
- those permits carry **74% of the dwellings**.

So if you want to know where housing is going to be built, four permits out of five are noise - and the one that matters comes with a company name.

## 2. The register names the builder, by design

The State removes the names of private individuals before publishing. But when the applicant is a legal entity found in the official company register, its name and SIREN number stay: developers, social landlords, build-to-sell companies, municipalities. In the Isère department, the last twelve months look like this: 407 housing permits by companies for 3,117 dwellings, and the ten biggest applicants are a readable list of who is actually building there: the first obtained nine permits for 245 dwellings, the next two 132 and 103.

Each permit also carries the address of the works, the cadastral parcels, the number of dwellings, the floor area, and a status that moves over time: authorized, works started, completed.

## 3. Eight months of notice

That status is what makes the register more than an archive. For company housing permits granted in 2022 and 2023 in those eight departments, I compared the permit date with the date the site was declared open:

- median delay: **258 days**, about eight and a half months;
- a quarter of the sites opened within 133 days, a quarter took more than 500;
- for programmes of ten dwellings or more: **426 days**, about fourteen months.

Two caveats. This only counts projects whose site has opened: depending on the department, 44% to 65% of the 2022-2023 permits have a declared opening so far, and 6% to 10% were cancelled - so the true delays are, if anything, longer. And the register is published monthly, so the freshest permits are a few weeks old.

For anyone selling to construction - trades, materials, equipment, services - that is the window: the project exists, the company behind it is named, and the site is still months away.

## Getting it without the plumbing

The raw files are large and coded (status 2, 5, 6; legal category 6541; surfaces split by use), and a share of the accented letters in addresses arrive mangled. I packaged the cleaning into [France Building Permits (Sitadel)](https://apify.com/euroscrape/france-building-permits):

```json
{ "locations": ["38"], "permitTypes": ["housing"], "minDwellings": 10 }
```

A city, a postal code or a department number; filters on type, status, date and size; SIREN numbers to follow specific companies nationwide; and a monitoring mode that returns only new permits and status changes, with alerts when works start.

One design choice worth stating: the open data still contains the address of the works for every permit, including those of private individuals. The Actor returns companies and public bodies by default, and when you ask for individuals' projects it gives them at commune level only - no street address, no parcel, no permit number. Statistics, yes; knocking on doors, no.

Input templates and sample outputs: [github.com/EuroScrape/apify-actors](https://github.com/EuroScrape/apify-actors).

---

*Part of the [EuroScrape](https://apify.com/euroscrape) actor collection — [all articles](../README.md#-articles--guides).*
