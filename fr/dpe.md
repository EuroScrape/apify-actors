---
lang: fr
description: >-
  Les diagnostics de performance énergétique (DPE) officiels d'une ville : classe énergie, classe CO2, surface,
  consommation, facture estimée. Trouver les passoires thermiques avec un robot Apify, payé au résultat.
---
# DPE : les diagnostics énergie officiels d'une ville, et ses passoires thermiques

Chaque diagnostic de performance énergétique est enregistré par l'ADEME et publié en données ouvertes. Ce robot les lit pour une ville ou un code postal, et peut ne garder que les classes qui vous intéressent, par exemple F et G, les logements que la loi interdit progressivement à la location.

**On lui donne** : une ville ou un code postal, et si on veut les classes recherchées.

**Il rend** : un diagnostic par ligne (classe énergie, classe CO2, date du diagnostic et de fin de validité, année d'interdiction de louer quand elle s'applique, type de logement, surface, période de construction, étage, énergie principale, consommation en kWh/m²/an, émissions, facture annuelle estimée, état de l'isolation), et un résumé par ville : nombre de diagnostics par classe et part des passoires.

**Pour qui** : artisans de la rénovation, diagnostiqueurs, investisseurs qui cherchent les logements à rénover d'une ville.

## Exemple : Grenoble, classes F et G, le 8 octobre 2026

Lancé sur un ordinateur portable, 2 secondes. Grenoble compte 56 932 diagnostics ; voici leur répartition :

| Classe | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| Part | 0,8 % | 7 % | 33,7 % | 33,5 % | 17,2 % | 5,4 % | 2,4 % |

Les passoires (F et G) : 4 448 logements, soit 7,8 %. Sur les 50 diagnostics livrés, la facture énergétique annuelle estimée médiane est de 1 882 €.

Une ligne de résultat ressemble à ceci :

```json
{
  "energyRating": "F",
  "ghgRating": "F",
  "issuedAt": "2026-10-05",
  "rentalBanFrom": 2028,
  "propertyType": "apartment",
  "surfaceM2": 73.2,
  "constructionPeriod": "1948-1974",
  "mainEnergy": "Gaz naturel",
  "primaryEnergyKwhM2Year": 329,
  "estimatedAnnualEnergyCostEur": 2526,
  "postalCode": "38100",
  "city": "Grenoble"
}
```

## Ce que ça coûte

0,001 $ par diagnostic livré, plus 0,003 $ par lancement. Mille diagnostics : 1 $. Pas d'abonnement.

## Lancer le robot

- Sur Apify, avec la documentation complète en anglais : [apify.com/euroscrape/france-energy-ratings](https://apify.com/euroscrape/france-energy-ratings)
- Un lancement prêt à l'emploi, en français : [DPE par commune et classes énergie](https://apify.com/euroscrape/france-energy-ratings/examples/dpe-par-commune-classes-energie)

Depuis votre code :

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~france-energy-ratings/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"locations": ["Grenoble"], "ratings": ["F", "G"], "maxRatingsPerLocation": 50}'
```

## D'où viennent les données

De la base des DPE de l'ADEME (logements existants, depuis juillet 2021, Licence Ouverte). Le diagnostic décrit un logement, jamais son occupant : le robot ne livre aucun nom.

Pour aller plus loin : [les logements classés F ou G se vendent 16 % moins cher au m²](../articles/12-dvf-dpe-energy-discount.md).

---

*Un robot de la collection [EuroScrape](https://apify.com/euroscrape) · [les autres pages en français](README.md) · [English](../examples/france-energy-ratings/README.md)*
