---
lang: fr
description: >-
  Les ventes immobilières réellement enregistrées par l'État (DVF) pour une ville ou un code postal : prix, surface,
  prix au m², date, classe énergie. Un robot Apify, payé au résultat, utilisable comme API.
---
# Prix immobilier : les ventes réelles d'une ville (DVF), prix au m² et tendances

Les annonces disent ce que les vendeurs demandent. Le fichier des *Demandes de valeurs foncières* (DVF), publié par l'État, dit ce qui a été payé : chaque vente enregistrée chez le notaire, avec son prix, sa surface et son adresse. Ce robot le lit pour vous, ville par ville.

**On lui donne** : une ville ou un code postal, et si on veut des années et un type de bien (appartement, maison).

**Il rend** : une ligne par vente (date, prix, surface, prix au m², nombre de pièces, adresse, type de bien, neuf ou ancien, classe énergie quand le diagnostic est connu : 264 des 500 ventes de l'exemple, loyer indicatif au m² et rendement brut), et un résumé par ville : prix médian, prix médian au m², surface médiane, par type de bien et par année, part du neuf, rues les plus actives.

**Pour qui** : agents immobiliers, investisseurs, acheteurs qui veulent le vrai prix d'un quartier et pas celui des annonces.

## Exemple : Grenoble, le 8 octobre 2026

Lancé sur un ordinateur portable, 6 secondes, 500 ventes livrées sur 4 916 trouvées.

| | Ventes | Prix médian | Prix médian au m² | Surface médiane |
|---|---|---|---|---|
| Appartements | 4 791 | 131 350 € | 2 500 € | 60 m² |
| Maisons | 125 | 330 000 € | 3 437 € | 92 m² |

Par année : 2 479 ventes en 2024 (appartements à 2 522 €/m², maisons à 365 000 € en médiane), 2 437 en 2025 (2 500 €/m², 313 500 €). Part du neuf : 1,2 %.

Une ligne de résultat ressemble à ceci :

```json
{
  "date": "2025-12-31",
  "price": 160000,
  "propertyType": "apartment",
  "surface": 109,
  "rooms": 3,
  "pricePerM2": 1468,
  "postalCode": "38000",
  "city": "Grenoble"
}
```

## Ce que ça coûte

0,0005 $ par vente livrée, plus 0,003 $ par lancement. Les 500 ventes ci-dessus : 0,25 $. Pas d'abonnement ; le plan gratuit d'Apify suffit pour essayer.

## Lancer le robot

- Sur Apify, avec la documentation complète en anglais : [apify.com/euroscrape/france-property-prices](https://apify.com/euroscrape/france-property-prices)
- Un lancement prêt à l'emploi, en français : [prix immobilier, ventes réelles par commune](https://apify.com/euroscrape/france-property-prices/examples/prix-immobilier-ventes-reelles-par-commune)

Depuis votre code, avec votre jeton Apify (Console → Settings → Integrations) :

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~france-property-prices/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"locations": ["Grenoble"], "years": [2024, 2025], "propertyTypes": ["apartment"]}'
```

## D'où viennent les données

Du fichier DVF de la Direction générale des finances publiques (Licence Ouverte), croisé avec les diagnostics de performance énergétique de l'ADEME quand l'adresse correspond. Les ventes sont publiques, mais les acheteurs et vendeurs n'y figurent pas : le robot ne livre aucun nom de particulier.

Pour aller plus loin : [les logements classés F ou G se vendent 16 % moins cher au m²](../articles/12-dvf-dpe-energy-discount.md), mesuré sur 2 518 ventes d'appartements.

---

*Un robot de la collection [EuroScrape](https://apify.com/euroscrape) · [les autres pages en français](README.md) · [English](../examples/france-property-prices/README.md)*
