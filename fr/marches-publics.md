---
lang: fr
description: >-
  Les appels d'offres ouverts (TED, BOAMP) et les marchés attribués (DECP) par mot-clé, pays, département et catégorie
  d'achat : acheteur, montant, date limite, attributaire. Un robot Apify avec alertes, payé au résultat.
---
# Marchés publics : les appels d'offres de la semaine, et qui a gagné les précédents

Trois sources publiques : le journal officiel européen (TED), le bulletin français (BOAMP) et les données essentielles des marchés attribués (DECP). Ce robot les interroge ensemble, par mot-clé, pays, département français, catégorie d'achat (code CPV) et montant, en deux modes : les appels d'offres encore ouverts, ou les marchés déjà attribués avec leur gagnant.

**On lui donne** : des mots-clés, des pays ou des départements, une catégorie, une fourchette de montant, une période.

**Il rend** : un avis par ligne (source, numéro, lien vers l'avis et son PDF, date de publication, acheteur avec sa ville et son site, titre, description, type de contrat, procédure, code CPV, montant, date limite, lots), et un résumé : nombre d'avis, montant cumulé, répartition par pays et par catégorie. En mode « attribués » : l'attributaire, le montant, le nombre d'offres reçues.

**Pour qui** : entreprises qui répondent aux marchés publics, et celles qui veulent savoir ce que gagnent leurs concurrents.

## Exemple : « logiciel », France, sept jours, le 8 octobre 2026

Lancé sur un ordinateur portable, 2 secondes, 30 avis publiés depuis le 1er octobre, pour 83,9 millions d'euros sur les 14 avis qui indiquent un montant.

| Catégorie d'achat (CPV) | Avis | Montant indiqué |
|---|---|---|
| Services de programmation et de conseil en logiciels | 10 | 12,58 M€ |
| Logiciels et systèmes d'information | 5 | non indiqué |
| Services de technologies de l'information | 2 | 1,15 M€ |

Parmi eux, publié le jour même : une infogérance scientifique certifiée ISO 27001 et HDS pour le CEA Paris-Saclay, en procédure négociée.

Une ligne de résultat ressemble à ceci :

```json
{
  "source": "TED",
  "noticeId": "696424-2026",
  "url": "https://ted.europa.eu/fr/notice/-/detail/696424-2026",
  "publishedAt": "2026-10-08",
  "country": "FR",
  "buyerName": "CEA Paris-Saclay - Service Marchés Achats",
  "buyerCity": "Gif-sur-Yvette",
  "title": "DRF INFOGERANCE SCIENTIFIQUE ISO 27001 et HDS",
  "contractType": "services",
  "procedureType": "Negotiated with call for competition"
}
```

## Ce que ça coûte

0,003 $ par appel d'offres livré, 0,005 $ par marché attribué (mode « attribués »), plus 0,003 $ par lancement. Les 30 avis ci-dessus : 0,09 $. Pas d'abonnement.

## Lancer le robot

- Sur Apify, avec la documentation complète en anglais : [apify.com/euroscrape/eu-public-tenders](https://apify.com/euroscrape/eu-public-tenders)
- Un lancement prêt à l'emploi, en français : [appels d'offres par mot-clé et département](https://apify.com/euroscrape/eu-public-tenders/examples/appels-d-offres-par-mot-cle-et-departement)

Depuis votre code :

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~eu-public-tenders/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["logiciel"], "countries": ["FR"], "sources": ["boamp", "ted"], "language": "fr", "publishedWithinDays": 7}'
```

Avec un `monitorName` et une programmation quotidienne, chaque lancement ne rend que les avis nouveaux, avec une alerte Telegram, Discord ou Slack.

## D'où viennent les données

De TED (Office des publications de l'Union européenne), du BOAMP (DILA) et des DECP (data.gouv.fr), toutes en licence ouverte. Ce sont des acheteurs publics et des entreprises ; aucun particulier.

Pour aller plus loin : [ce que disent les attributions de marchés](../articles/03-eu-tenders.md).

---

*Un robot de la collection [EuroScrape](https://apify.com/euroscrape) · [les autres pages en français](README.md) · [English](../examples/eu-public-tenders/README.md)*
