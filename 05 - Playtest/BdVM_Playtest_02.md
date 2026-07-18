---
projet: "Batailles du Vieux Monde"
type: "playtest"
numero: "02"
phase: 1.5
scenario: "Scénario Playtest #2"
factions_testees: ["Empire", "Hommes-Lézards"]
date: "2026-05-15"
statut: "clôturé"
tags: [BdVM, type/playtest, phase/1.5, statut/clôturé]
---

# Playtest #02 — 15/05/2026

> 🔗 **Voir aussi** [[Document de cadrage]] — [[BdVM_Playtest_01]]

---

## Contexte

| Paramètre | Valeur |
|---|---|
| Scénario joué | Scénario Playtest #2 |
| Factions en présence | Empire vs Hommes-Lézards |
| Format | Escarmouche |
| Seuil de victoire | 4 points |
| Durée de la partie | Non mesurée |
| Participants | Solo |
| Résultat | Victoire de l'Empire — 4 à 1 |

**Objectif du playtest :** Valider les règles refondues de la Phase 1.5 (alignement BLv2) — en particulier [Tenace], [Réception de charge], [Poursuite], [Perforant], [Venin de Skink], [Salve] et la mécanique Salamandres. Observer l'équilibre global Empire / Hommes-Lézards après la refonte des profils.

---

## Déroulement

Malgré un score sans appel (4-1 Empire), la partie a été ressentie comme plus équilibrée que le Playtest #1. La cavalerie Empire a dominé les échanges de façon décisive et balayé ses opposants sans rencontrer de résistance significative. Les Hommes-Lézards sont restés en retrait — les Kroxigors n'ont pas bougé de la partie. Les retraites ont été fréquentes et massives (jusqu'à 3-4 Drapeaux sur un seul lancer), provoquant des déroutes rapides difficiles à anticiper. Les règles de retraite ont été régulièrement oubliées en cours de jeu. Les unités Faibles ont été rares, et [Tenace] n'a créé aucun moment de jeu notable. [Réception de charge] n'a fonctionné qu'une seule fois.

---

## Problèmes identifiés

| # | Règle concernée | Description du problème | Gravité |
|---|---|---|---|
| 1 | Nombre de dés — doublement généralisé (D012) | Trop de dés génèrent en cascade : Drapeaux en excès, déroutes trop rapides, règles annexes inopérantes, lecture de table confuse. Le doublement, pensé pour compenser le ratio 1 touche = 1 figurine, crée plus de problèmes qu'il n'en résout. | Bloquant |
| 2 | Drapeaux — volume | 3 à 4 Drapeaux sur un seul lancer = retraites de 3-4 hexagones en une activation. Trop brutal, peu narratif, empêche [Réception de charge] de se déclencher. | Bloquant |
| 3 | Cavalerie Empire — Chevaliers | Trop dominante. A balayé ses opposants sans véritable résistance. Profil à réévaluer après retour aux dés originaux. | Bloquant |
| 4 | [Salve] — Arquebusiers | +2 dés à bout portant = 8 dés sur une unité d'infanterie standard. Trop puissant, et le risque est encore plus fort si les dés de base sont réduits sans recalibrer la règle. | Gênant |
| 5 | [Tenace] | Quasiment pas déclenché : peu d'unités Faibles atteintes, et quand c'était le cas, la règle n'a pas suffi à créer un moment de jeu. La condition (2 touches simultanées sur la dernière figurine) est trop restrictive. | Gênant |
| 6 | Kroxigors | N'ont pas bougé de la partie. Mouvement 1 trop contraignant sur un plateau Escarmouche. | Gênant |
| 7 | [Réception de charge] | N'a fonctionné qu'une seule fois. Diagnostic révisé : la règle n'est probablement pas défaillante en elle-même — l'excès de Drapeaux faisait reculer les unités avant qu'elles puissent contre-attaquer. Symptôme du problème #2. | Mineur |
| 8 | Règles de retraite | Oublis fréquents. Problème de présentation et de mémorisation, pas de règle. | Mineur |

---

## Points positifs

- La partie a été ressentie comme plus équilibrée que le Playtest #1 malgré le score — le système de base est lisible.
- La structure du tour ne génère plus de friction majeure.
- Le seuil de victoire à 4 points reste adapté au format Escarmouche.

---

## Décisions prises suite au playtest

| # | Règle modifiée | Ancienne version | Nouvelle version | Justification |
|---|---|---|---|---|
| D060 | Dés d'attaque — valeurs générales | Doublement généralisé par rapport aux valeurs C&C/BLv2 de référence (D012) | Retour aux valeurs de dés originaux BLv2. Tous les profils sont à recalibrer en conséquence. | Le doublement génère des Drapeaux excessifs, des déroutes injouables et neutralise les règles spéciales. |
| D061 | Forêt — plafond de dés (D053) | Max 4 dés (cohérent avec le doublement) | À réviser après D060 — probablement retour à max 2 dés comme BLv2. | Conséquence directe de D060. |
| D062 | [Salve] | +2 dés si cible à portée minimale (8 dés total) | À revoir — soit réduire le bonus à +1 dé, soit conditionner davantage le déclencheur. | Trop puissant à 8 dés, risque amplifié après recalibration générale. |

> 🔄 **Rappel** : Reporter chaque modification dans les documents concernés avec le bloc `🔄 Modifié après playtest — 2026-05-15 | Playtest #02`.

---

## Questions ouvertes pour le Playtest #3

- **Valeurs de dés** : une fois les profils recalibrés sur base BLv2, vérifier que le ratio touches/Drapeaux est jouable sur les deux factions.
- **[Tenace]** : reformuler (activation plus tôt dans la vie de l'unité ?) ou réserver aux élites uniquement (Gardes du Temple, Kroxigors) ?
- **Cavalerie** : le retour aux dés originaux suffira-t-il à rééquilibrer les Chevaliers, ou faut-il aussi ajuster leur profil ?
- **Kroxigors** : mouvement à 2 ou mécanique d'ancrage volontaire ?
- **[Réception de charge]** : à surveiller avec moins de Drapeaux — si toujours inerte, élargir la condition (ex. +2 dés en contre-attaque inconditionnelle).
- **Règles de retraite** : créer une aide de jeu récapitulative.

---

*Version : 1.0 — 2026-05-15. Compte-rendu rédigé à l'issue du débrief Playtest #2.*
