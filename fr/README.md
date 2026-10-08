---
lang: fr
description: >-
  Les robots EuroScrape sur données publiques françaises, expliqués en français : prix immobilier (DVF), DPE,
  permis de construire, prix des carburants, entreprises (SIRENE), marchés publics. Payés au résultat sur Apify.
---
# Les robots EuroScrape en français

EuroScrape publie vingt robots de collecte de données sur [Apify](https://apify.com/euroscrape), une plateforme où chacun se lance en un clic, s'appelle comme une API et se paie au résultat, sans abonnement. Six d'entre eux lisent des données publiques françaises. Leur documentation complète est en anglais ; ces pages expliquent en français ce qu'ils donnent, avec un exemple du jour et ce que ça coûte.

| Robot | Ce qu'il rend | Prix |
|---|---|---|
| [Prix immobilier (DVF)](prix-immobilier.md) | Les ventes réellement enregistrées d'une ville : prix, surface, prix au m², classe énergie, résumé par ville | 0,0005 $ par vente |
| [DPE](dpe.md) | Les diagnostics énergie officiels d'une ville, et ses passoires thermiques | 0,001 $ par diagnostic |
| [Permis de construire](permis-de-construire.md) | Les chantiers autorisés dans une commune ou un département, avec la société qui les dépose | 0,003 $ par permis |
| [Prix des carburants](prix-carburants.md) | Les stations autour d'une ville, de la moins chère à la plus chère, avec la date de chaque prix | 0,001 $ par station |
| [Entreprises (SIRENE)](entreprises.md) | Un fichier d'entreprises par activité, département et taille, avec contacts en option | 0,004 $ par entreprise |
| [Marchés publics](marches-publics.md) | Les appels d'offres ouverts (TED, BOAMP) et les marchés attribués, avec alertes | 0,003 $ par avis |

Chaque robot a aussi un lancement prêt à l'emploi en français sur Apify : [prix immobilier par commune](https://apify.com/euroscrape/france-property-prices/examples/prix-immobilier-ventes-reelles-par-commune), [DPE par commune](https://apify.com/euroscrape/france-energy-ratings/examples/dpe-par-commune-classes-energie), [permis de construire par commune](https://apify.com/euroscrape/france-building-permits/examples/permis-de-construire-par-commune), [carburants autour d'une ville](https://apify.com/euroscrape/france-fuel-prices/examples/prix-carburants-autour-d-une-ville), [entreprises par code NAF et département](https://apify.com/euroscrape/france-companies/examples/liste-entreprises-par-code-naf-et-departement), [appels d'offres par mot-clé et département](https://apify.com/euroscrape/eu-public-tenders/examples/appels-d-offres-par-mot-cle-et-departement).

## Sans rien lancer

[Le carburant le moins cher aujourd'hui dans 20 villes de France](../data/prix-carburants-villes.md), une page refaite chaque jour par le robot des carburants.

## Un septième, pour les sites web

[Impressum & Legal Notice Scraper](https://apify.com/euroscrape/company-identity) lit les mentions légales d'un site et rend la société qui est derrière (raison sociale, SIREN, TVA, dirigeants, contacts), vérifiée au registre pour la France et le Royaume-Uni : [trouver la société derrière un site web](https://apify.com/euroscrape/company-identity/examples/trouver-la-societe-derriere-un-site-web).

## Les autres robots

Vols (Google Flights, Ryanair), hôtels, électricité en Europe, occasion (Vinted, Kleinanzeigen, 18 pays), entreprises britanniques, numéros de TVA, technologies des sites web, avis d'applications : [la liste complète, en anglais](../README.md).

---

*[EuroScrape](https://apify.com/euroscrape) · [English](../README.md)*
