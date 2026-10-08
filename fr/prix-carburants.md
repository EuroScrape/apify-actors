---
lang: fr
description: >-
  Les stations-service autour d'une ville, de la moins chère à la plus chère, avec les prix officiels du jour
  (prix-carburants.gouv.fr) et la date de chaque relevé. Un robot Apify, payé au résultat, utilisable comme API.
---
# Prix des carburants : la station la moins chère autour d'une ville, et depuis quand son prix date

Les stations-service déclarent leurs prix à l'État, qui les publie en continu. Ce robot lit ce flux pour un rayon autour d'une ville, d'un code postal ou d'un point GPS, classe les stations de la moins chère à la plus chère, et dit pour chaque prix quand il a été relevé, ce qui compte : une station qui n'a pas mis son prix à jour depuis des semaines est souvent « la moins chère » à tort.

**On lui donne** : une ville, un code postal ou des coordonnées, un rayon en kilomètres, les carburants voulus.

**Il rend** : une station par ligne (adresse, commune, distance, prix de chaque carburant avec sa date de relevé, ouverte 24 h/24 ou non, sur autoroute ou non, services), et un résumé par lieu et par carburant : la moins chère, le prix médian, l'écart entre stations.

**Pour qui** : gestionnaires de flottes, comparateurs, applications de trajet.

## Exemple : Grenoble, 10 km, le 8 octobre 2026

Lancé sur un ordinateur portable, 2 secondes, 31 stations.

| Carburant | Stations | Le moins cher | Prix médian | Écart entre stations |
|---|---|---|---|---|
| Gazole | 31 | 2,250 € | 2,357 € | 27,9 ct |
| SP95-E10 | 28 | 1,990 € | 2,182 € | 30,9 ct |

Le E10 le moins cher est à La Tronche, à 3 km, relevé le matin même à 9 h 19. Le gazole le moins cher, lui, affiche un prix relevé le 14 septembre : c'est le champ `updatedAt` qui le dit, et c'est pour ça qu'il est dans chaque ligne.

Une ligne de résultat ressemble à ceci :

```json
{
  "address": "Avenue de Verdun",
  "city": "La Tronche",
  "distanceKm": 3,
  "open24h": true,
  "motorway": false,
  "e10": 1.99,
  "e10UpdatedAt": "2026-10-08T09:19:34",
  "gazole": 2.29
}
```

## Ce que ça coûte

0,001 $ par station livrée, plus 0,003 $ par lancement. Les 30 stations ci-dessus : 0,03 $. Pas d'abonnement.

## Lancer le robot

- Sur Apify, avec la documentation complète en anglais : [apify.com/euroscrape/france-fuel-prices](https://apify.com/euroscrape/france-fuel-prices)
- Un lancement prêt à l'emploi, en français : [prix des carburants autour d'une ville](https://apify.com/euroscrape/france-fuel-prices/examples/prix-carburants-autour-d-une-ville)
- Sans rien lancer : [le carburant le moins cher aujourd'hui dans 20 villes](../data/prix-carburants-villes.md), page refaite chaque jour par ce robot.

Depuis votre code :

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~france-fuel-prices/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"locations": ["Grenoble"], "radiusKm": 10, "fuels": ["Gazole", "E10"]}'
```

## D'où viennent les données

Du flux instantané de prix-carburants.gouv.fr (Licence Ouverte). Ce sont des commerces, pas des particuliers.

Pour aller plus loin : [la station la moins chère est souvent un fantôme](../articles/11-energy-two-assumptions.md), mesuré sur le même flux.

---

*Un robot de la collection [EuroScrape](https://apify.com/euroscrape) · [les autres pages en français](README.md) · [English](../examples/france-fuel-prices/README.md)*
