---

projet: "Batailles du Vieux Monde"
type: "playtest"
phase: 1
statut: "en-cours"
date_maj: "2026-04-06"
tags: [BdVM, "type/playtest", "phase/1", "statut/en-cours"]
---
# Batailles du Vieux Monde — Checklist de clôture Phase 1

> Ce document liste les points à trancher **avant** et **après** le Playtest #1 pour valider la clôture de la Phase 1. Il ne contient pas de règles — uniquement des décisions à prendre et des éléments à produire.

---

## Avant le Playtest #1

### Règles — précisions à ajouter

- [ ] **Portée de tir** : ajouter une phrase dans `BdVM_Regles_Base` §7.1 précisant que la portée est définie dans le profil d'unité et qu'en l'absence de mention, il n'y a pas de limite.
- [ ] **Contre-attaque [Intrépide]** : préciser dans `BdVM_Regles_Base` §7.4 et `BdVM_Regles_Speciales` que la contre-attaque s'effectue uniquement contre une cible adjacente.
- [ ] **Ordre de résolution [Massif] + [Colosse]** : trancher le cas (théorique en Phase 1, réel en Phase 2) où une unité possède les deux règles simultanément. Proposition : [Massif] s'applique en premier, puis [Colosse] sur les touches restantes.
- [ ] **Non-cumul d'[Intrépide]** : inscrire le principe général dans `BdVM_Regles_Speciales` — [Intrépide] ne se cumule jamais, quelle qu'en soit la source (profil, terrain, adjacence).
- [ ] **Tir sur une unité sur un pont** : confirmer explicitement qu'il n'y a pas de couvert ni de malus pour l'attaquant — le pont ne protège que moralement (via [Intrépide]).
- [ ] **Lien cassé** : corriger dans `BdVM_Regles_Speciales` le renvoi vers §7.5 et §8.4 → doit pointer vers §7.4 (Intrépide) dans `BdVM_Regles_Base`.

### Composants — décisions à prendre

- [ ] **Marqueur de rechargement** : choisir la solution physique pour [Rechargement] (jeton dédié, dé posé sur le socle, figurine couchée).
- [ ] **Dés** : finaliser les faces et lancer la production.

### Contenu — à produire

- [ ] **Profils d'unités Empire** : document `BdVM_Empire_Unites.md` complet pour le Playtest #1.
- [ ] **Profils d'unités Hommes-Lézards** : document `BdVM_Hommes_Lezards_Unites.md` complet pour le Playtest #1.
- [ ] **Scénario de test** : 1 scénario simple (infanterie + cavalerie, terrain mixte incluant au moins un bois et une position surélevée pour valider les règles de terrain).

---

## Pendant le Playtest #1 — points à surveiller

- [ ] **[Frénésie] + [Martyre]** : observer si les Flagellants sont trop difficiles à déloger ou trop dominants offensivement. Levier principal : leur valeur d'attaque.
- [ ] **[Intrépide] par adjacence** : vérifier si la condition (2 unités amies adjacentes) est trop facilement atteinte en Escarmouche, rendant la règle quasi-permanente.
- [ ] **Asymétrie de tir Empire / Hommes-Lézards** : s'assurer que le terrain offre suffisamment d'options aux Hommes-Lézards pour contourner la supériorité de tir Empire (couverts, approche par les flancs).
- [ ] **Fluidité du tour** : noter les étapes qui ralentissent le jeu ou génèrent des questions non prévues par les règles.
- [ ] **Seuils de victoire** : noter la durée effective de la partie pour ajuster les seuils (5 / 6 / 8 pts selon format).

---

## Après le Playtest #1 — à traiter en clôture de Phase 1

- [ ] **Valider ou ajuster** les seuils de victoire par format.
- [ ] **Valider ou ajuster** la valeur d'attaque des Flagellants selon les observations sur [Frénésie] + [Martyre].
- [ ] **Valider ou réviser** la condition d'[Intrépide] par adjacence si elle s'avère trop systématique.
- [ ] **Valider ou réviser** les profils d'unités des deux factions selon les déséquilibres observés.
- [ ] **Décider** de l'exception d'infanterie légère en terrain boisé (point ouvert `BdVM_Terrain` §3.1).
- [ ] **Décider** d'un éventuel coût de mouvement pour monter/descendre un terrain surélevé (point ouvert `BdVM_Terrain` §4.1).
- [ ] **Décider** de la règle de Valeur de commandement (point ouvert `BdVM_Regles_Base` §3).
- [ ] Mettre à jour le **journal de décisions** dans `Document_de_cadrage.md` avec toutes les décisions prises.
- [ ] Passer le statut des documents validés à `validé` dans leur frontmatter YAML.
- [ ] **Démarrer la Phase 2** : magie, monstres, personnages héroïques.

---

_Version : 1.0 — 2026-04-06. Document créé à l'issue de la revue de cohérence pré-playtest._