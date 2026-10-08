---
lang: fr
description: >-
  Les permis de construire accordés dans une commune, un arrondissement ou un département (Sitadel) : projet, logements,
  surface, avancement, et la société qui l'a déposé avec son SIREN. Un robot Apify, payé au résultat.
---
# Permis de construire : les chantiers autorisés avant qu'ils ouvrent, avec qui les construit

La base Sitadel du ministère chargé du logement enregistre chaque permis de construire et chaque déclaration préalable, avec le demandeur. Ce robot la lit pour une commune, un arrondissement ou un département, sur les douze derniers mois par défaut.

**On lui donne** : une commune, un arrondissement ou un département.

**Il rend** : un permis par ligne (numéro, type, statut : autorisé, commencé, achevé ; dates de dépôt et d'autorisation ; adresse et parcelles ; nombre de logements et surface de plancher ; usage principal pour le non-résidentiel), et pour chaque demandeur qui est une société : son nom, son SIREN et son SIRET, sa forme juridique et son activité. Plus un résumé par lieu : permis et logements par catégorie, par statut, principaux demandeurs.

**Pour qui** : entreprises du bâtiment, fournisseurs de matériaux, promoteurs, tous ceux qui veulent connaître les chantiers avant qu'ils ouvrent.

## Exemple : Grenoble, douze mois, le 8 octobre 2026

Lancé sur un ordinateur portable, 9 secondes, 48 permis depuis le 8 octobre 2025.

| | Permis | Logements | Surface de plancher |
|---|---|---|---|
| Logement | 11 | 34 | 1 483 m² |
| Non résidentiel | 37 | | 13 065 m² |

Le non-résidentiel, par usage : commerces et services 15, équipements publics 6, bureaux 6, entrepôts 5, industrie 3, hôtel 1. Statuts : 43 autorisés, 5 commencés.

Une ligne de résultat ressemble à ceci :

```json
{
  "permitNumber": "03818526U9196",
  "permitType": "prior declaration",
  "status": "authorized",
  "filedAt": "2026-04-27",
  "authorizedAt": "2026-08-27",
  "category": "nonResidential",
  "applicantType": "company",
  "applicant": { "name": "…", "siren": "…", "legalForm": "association", "activityCode": "94.99Z" },
  "postalCode": "38100",
  "city": "Grenoble"
}
```

## Ce que ça coûte

0,003 $ par permis livré, plus 0,003 $ par lancement. Les 48 permis ci-dessus : 0,15 $. Pas d'abonnement.

## Lancer le robot

- Sur Apify, avec la documentation complète en anglais : [apify.com/euroscrape/france-building-permits](https://apify.com/euroscrape/france-building-permits)
- Un lancement prêt à l'emploi, en français : [permis de construire par commune](https://apify.com/euroscrape/france-building-permits/examples/permis-de-construire-par-commune)

Depuis votre code :

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~france-building-permits/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"locations": ["Grenoble"], "maxPermitsPerLocation": 50}'
```

Avec un `monitorName` et une programmation hebdomadaire, chaque lancement ne rend que les nouveaux permis, avec une alerte Telegram, Discord ou Slack.

## D'où viennent les données

De la base Sitadel (ministère de la Transition écologique, Licence Ouverte), croisée avec le registre SIRENE pour identifier les sociétés. Les demandeurs particuliers ne sont pas nommés.

Pour aller plus loin : [la fenêtre entre le permis et le chantier](../articles/13-building-permits-window.md).

---

*Un robot de la collection [EuroScrape](https://apify.com/euroscrape) · [les autres pages en français](README.md) · [English](../examples/france-building-permits/README.md)*
