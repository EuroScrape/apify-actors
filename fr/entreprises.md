---
lang: fr
description: >-
  La liste des entreprises du registre SIRENE par activité, département et taille : siège, forme juridique, effectif,
  dirigeants, et en option leur site web, e-mails et téléphones. Un robot Apify pour la prospection, payé au résultat.
---
# Entreprises françaises : un fichier de prospection tiré du registre SIRENE

Le registre SIRENE connaît chaque entreprise de France : activité, adresse du siège, effectif, date de création, dirigeants. Ce robot le filtre pour vous et, si vous le demandez, cherche le site web de chaque entreprise et y lit ses e-mails et téléphones.

**On lui donne** : une activité (un mot-clé comme « plomberie », ou des codes NAF), des départements, des codes postaux ou des régions, une tranche d'effectif, une date de création, une forme juridique.

**Il rend** : une entreprise par ligne (SIREN, nom, statut, date de création, forme juridique, catégorie, code et libellé NAF, effectif, nombre d'établissements, siège avec SIRET et adresse, dirigeants), et avec l'option contacts : site web vérifié, e-mails, téléphones.

**Pour qui** : commerciaux et agences qui construisent des fichiers de prospection entre entreprises.

## Exemple : plombiers de l'Isère, le 8 octobre 2026

Lancé sur un ordinateur portable, 2 secondes, 30 entreprises demandées et livrées. La première ligne : une SAS de plomberie créée en 2018, catégorie PME, 6 à 9 salariés, deux établissements, activité 43.22A (installation d'eau et de gaz).

Une ligne de résultat ressemble à ceci :

```json
{
  "siren": "…",
  "legalName": "…",
  "status": "active",
  "createdAt": "2018-01-23",
  "legalForm": { "code": "5710", "label": "SAS, société par actions simplifiée" },
  "nafCode": "43.22A",
  "nafLabel": "Travaux d'installation d'eau et de gaz en tous locaux",
  "employees": { "label": "6 à 9 salariés", "min": 6, "max": 9, "year": 2024 },
  "headquarters": { "siret": "…", "postalCode": "38…", "city": "…" }
}
```

## Ce que ça coûte

0,004 $ par entreprise livrée, plus 0,003 $ par lancement. Mille entreprises : 4 $. Avec l'option contacts, une entreprise dont le site a été trouvé et lu (site, e-mails, téléphones) coûte 0,025 $ au lieu de 0,004 $. Pas d'abonnement.

## Lancer le robot

- Sur Apify, avec la documentation complète en anglais : [apify.com/euroscrape/france-companies](https://apify.com/euroscrape/france-companies)
- Un lancement prêt à l'emploi, en français : [liste d'entreprises par code NAF et département](https://apify.com/euroscrape/france-companies/examples/liste-entreprises-par-code-naf-et-departement)

Depuis votre code :

```bash
curl -X POST "https://api.apify.com/v2/acts/euroscrape~france-companies/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query": "plomberie", "departments": ["38"], "employeeRanges": ["03", "11"], "findContacts": true, "maxItems": 100}'
```

Les tranches d'effectif sont les codes de l'INSEE : `03` pour 6 à 9 salariés, `11` pour 10 à 19, `12` pour 20 à 49, `21` pour 50 à 99.

```bash
# même chose, sans les contacts, pour un fichier moins cher
curl -X POST "https://api.apify.com/v2/acts/euroscrape~france-companies/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"nafCodes": ["43.22A"], "departments": ["38", "73", "74"], "maxItems": 500}'
```

Avec un `monitorName`, chaque lancement ne rend que les entreprises nouvelles ou modifiées depuis le précédent.

## D'où viennent les données

Du registre SIRENE (INSEE) par l'API officielle de recherche d'entreprises, et des sites web des entreprises elles-mêmes pour les contacts. Les adresses livrées sont celles des sièges, telles que le registre public les publie ; les 30 lignes de l'exemple sont toutes des sociétés.

---

*Un robot de la collection [EuroScrape](https://apify.com/euroscrape) · [les autres pages en français](README.md) · [English](../examples/france-companies/README.md)*
