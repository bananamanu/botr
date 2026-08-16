---
projet: "Batailles de la Terre du Milieu"
type: "playtest"
phase: "1"
statut: "clos"
date_maj: "2026-07-25"
tags: [BdTdM, "type/playtest", "phase/1", "statut/analyse"]
version: "1.1"
---

# Playtest #1 — Compte rendu

> **Objet de ce document :** débrief de la première partie de test de *Batailles de la Terre du Milieu*, jouée le 2026-07-25 sur le scénario `[[Playtest1_Avant-garde_sur_le_Pelennor]]` (format Normal, 1 joueur par camp, D039). Analyse des enseignements, décisions de design prises en conséquence (D040-D046) et points reportés. Les modifications de profils et de règles décrites ici sont **déjà appliquées** dans les fichiers concernés (Rohan v1.1, Gondor v1.2, Khand v1.1, Mordor v0.4, Easterling v1.1, [[Regles_Speciales]] v0.9, [[Document_de_cadrage]] v1.14).

---

## 1. Résultat & déroulé

| | |
|---|---|
| **Format** | Normal, 1v1 (D039) — plateau hérité, seuil de victoire à **6 unités détruites** |
| **Ordre de bataille** | Bien (Rohan + Gondor/fiefs, 12 u./60 pts) vs Mal (Khand + Easterling + Mordor, 10 u./62 pts) |
| **Résultat** | **Victoire du Mal, 6–2, en 7 tours** |

Le déséquilibre était assumé et documenté (quantité côté Bien vs qualité côté Mal, seuil fixe). Le score n'est pas un blowout mais reste net.

---

## 2. Le constat qui prime : la partie s'est étranglée au centre (D040)

**C'est l'enseignement le plus important, avant tout ajustement de profil.** Toute l'action s'est concentrée au centre ; les ailes sont restées largement inactives et une grande partie des unités n'a jamais été activée, faute des bonnes cartes de section. Conséquence directe : **les 5 règles neuves que ce test devait éprouver ([Horde], [Peur X], [Mur de bouclier], [Déploiement avancé], compromis Aurige) sont restées en grande partie non testées.** L'objectif premier du Playtest #1 n'est donc atteint qu'à moitié.

Deux lectures :

1. **Texture normale de Commands & Colors** — la famine de cartes sur une aile *est* un ressort voulu du système. Un peu de centre-lourd est sain.
2. **Mais ici, c'est un défaut** — pour un test dont le but était de faire tomber les règles, et surtout **pour la cible convention en 3v3 : un centre qui aspire tout, c'est 2 joueurs sur 6 qui regardent la partie.** Rédhibitoire.

**Leviers à explorer (non tranchés) :**
- **Audit du deck de commandement** (`[[Cartes_Commandement]]`) : compter les cartes Gauche / Centre / Droite / Toutes-sections. Si le centre et le « toutes-sections » dominent, tout converge mécaniquement. Premier chantier.
- **Main plus large / valeur de commandement plus haute** en Normal : plus de cartes en main = moins de famine d'aile.
- **Déploiement plus imbriqué ou objectifs de flanc** pour donner une raison d'aller sur les ailes.
- **Enjeu Épique (Phase 2)** : le commandement multi-joueurs doit **garantir à chaque section une activation régulière**. Ce point doit être résolu **avant** le passage à l'Épique.

→ **Décision : un `Playtest #1b` est ajouté à la feuille de route** (Phase 1), dédié à rejouer les règles non éprouvées dans un dispositif forçant l'engagement des ailes.

---

## 3. Changements actés à la table

### 3.1 Recul façon Memoir '44 (D041) — à reporter dans [[Regles_Base]]

Le recul a été joué **toujours vers le bord ami** du joueur qui recule, au lieu de la résolution directionnelle C&C jugée « compliquée ou absurde à appliquer ». Retenu : plus simple, plus mémorisable (principe 1).

- **Direction** : vers le bord du joueur qui recule. Il choisit l'hexagone parmi ceux **strictement plus proches de son bord**.
- **Conservé** : « 1 perte par hexagone de recul non effectué » (identique dans les deux systèmes).
- **À trancher** : le terrain infranchissable bloque-t-il le recul (→ pertes) ? *(à confirmer à la rédaction de [[Regles_Base]])*

### 3.2 Jeton « à contre-attaquer » (D042) — à reporter dans [[Regles_Base]] + aide de jeu

La contre-attaque universelle a été **oubliée en boucle**, y compris par l'arbitre. C'est une réaction *toujours active* — la catégorie de règle la plus oubliée. Correctif à moindre risque, sans changement de règle : **poser un jeton sur toute unité touchée mais survivante**, retiré une fois la riposte résolue. La question de fond (contre-attaque universelle vs limitée, façon BattleLore V2) reste ouverte.

---

## 4. Ajustements de profils (D046) — appliqués

Sept profils modifiés. Tous les coûts recalculés à la formule `round((Mvt + PV + Attaque×D + Σ règles) ÷ 3) − 1`.

| Peuple | Unité | Changement | Coût |
|---|---|---|---|
| Rohan | Milice lige | +[Arme de jet 1] (rôle d'escarmouche) | 4 → **4** |
| Rohan | Éored d'éclaireur | 2 → **3 dés**, Mouvement 4 → **3** | 4 → **4** |
| Rohan | Garde du roi à cheval | −[Charge écrasante] (garde [Armure 1]+[Poursuite 2]) | 8 → **8** |
| Gondor | Chevaliers de Dol Amroth | Mvt 3 → **2**, [Armure 1] → **[Armure 2]** | 7 → **7** |
| Khand | Aurige de Khand | 4 → **3 dés**, −[Charge écrasante] −[Arme Lourde 1], +[Plateforme de tir 2] | 7 → **6** |
| Mordor | Troll du Mordor | [Charge écrasante] → **[Arme Lourde 2]** | 7 → **7** |
| Easterling | Cataphractaires orientaux | −[Charge écrasante] (ne gardent que [Armure 2]) | 7 → **6** |

**Deux effets de bord positifs, notés au dossier :**
- **Exceptions de Mouvement rationalisées (amende D022)** : l'ancienne exception Mvt 4 du Rohan (Éored) disparaît ; les nouvelles exceptions sont « cavalerie lourde Mvt 2 » (Chevaliers de Dol Amroth, en écho aux Cataphractaires déjà à Mvt 2). Les exceptions deviennent **thématiques** — l'armure ralentit.
- **Dissolution de la 1re dominance stricte D025** : Dol Amroth (7) ne domine plus les Chevaliers de Minas Tirith (6) ; il échange la vitesse (Mvt 2 vs 3) contre l'armure et un dé. Vrai arbitrage, plus une supériorité réglée au prix. Miroir maléfique côté Mal : les Cataphractaires (aussi Mvt 2 / [Armure 2]).

**À surveiller au prochain test :** la densité d'actions de l'Aurige reconçu (volée + mêlée + Poursuite sur une activation), même sans pic de dégâts.

---

## 5. Deux règles neuves & retrait de [Charge écrasante]

### 5.1 [Charge écrasante] retirée de toute la V1 (D043)

Cause racine du 6–2 : le couple **[Charge écrasante] + charge de cavalerie/[Poursuite]** a été une boucherie — l'Aurige de Khand et les Cataphractaires ont fait **4 pertes sur 6** à eux deux. La règle n'est pas cassée en soi, mais l'est sur une unité rapide à 4 dés qui charge chaque tour (et double la mise sous [Poursuite]). Elle est **retirée de tous les profils de la V1**, conservée au glossaire mais non assignée. L'effet de choc de masse est réservé aux grandes créatures via la règle d'impact **dédiée** du Mûmakil (Phase 2, distincte de [Charge écrasante]).

### 5.2 [Arme de jet X] (D044)

Le tour où l'unité s'est déplacée puis attaque en mêlée, jusqu'à **X faces Cible** comptent comme touches. Coût **1×X**. Version conditionnelle et plafonnée de [Archer en mêlée] (D024). Première porteuse : Milice lige.

### 5.3 [Plateforme de tir X] (D045)

Attaque de tir de **X dés** (portée 1–3, ligne de vue) **en plus** de l'attaque normale, déplacée ou non, une fois par activation. Coût **2×X**. Première porteuse : Aurige de Khand ([Plateforme de tir 2]).
**Unification bienvenue** : le [Howdah] déjà au glossaire en devient le cas particulier du Mûmakil → **[Howdah] = [Plateforme de tir 2] + [Poison]**.

---

## 6. Ce qui reste non testé → Playtest #1b

Faute d'engagement des ailes, restent **non éprouvés** : [Horde] (D032), [Peur X] (D033, coût 2×X provisoire), [Mur de bouclier] (D037, coût 1 pt provisoire), [Déploiement avancé] (D028), et les règles neuves de ce débrief ([Arme de jet X], [Plateforme de tir X], [Arme Lourde 2] sur le Troll). Ils constituent la raison d'être du **Playtest #1b**, à jouer dans un dispositif qui force l'action sur les flancs.

---

## 7. Suivi documentaire

**Fichiers déjà mis à jour** (2026-07-25) : `02 - Factions/Rohan.md` (v1.1), `Gondor_et_Fiefs.md` (v1.2), `Khand.md` (v1.1), `Mordor.md` (v0.4), `Easterling.md` (v1.1), `[[Regles_Speciales]]` (v0.9), `[[Document_de_cadrage]]` (v1.14, D040-D046).

**Restent à mettre à jour (non traités dans cette passe) :**
- **[[Regles_Base]]** : formaliser le recul Memoir '44 (D041) et le jeton contre-attaque (D042).
- **[[Regles_Points]]** : ajouter au barème le coût des deux règles neuves — **[Arme de jet X] = 1×X**, **[Plateforme de tir X] = 2×X** ; répercuter les nouveaux coûts (Aurige 6, Cataphractaires 6) et acter la dissolution de la 1re dominance D025 dans la table de calibrage Gondor.
- **[[Cartes_Commandement]]** : audit de la répartition des cartes de section (chantier « centre-funnel », D040).

---

## 8. Addendum — révisions du 2026-07-26 (D047, D048)

Après relecture, Emmanuel est revenu sur deux points de ce débrief :

- **Éored d'éclaireur (D047)** : l'attaque redescend de 3 à **2 dés** et **[Déploiement avancé] est retirée de la V1** (jamais éprouvée, faute d'engagement des ailes). Remplacée par une nouvelle règle, **[Flanking]** (adaptée des Riverwatch Riders de *BattleLore : Seconde Édition*) : tant qu'une unité ennemie est adjacente à l'éored, les autres unités amies qui l'attaquent gagnent +1 dé. Coût 3 pts forfaitaires, inchangé au total (4 pts). L'éored devient un rôle de soutien/harcèlement plutôt qu'un tireur en propre.
- **Troll du Mordor (D048)** : [Arme Lourde 2] ramenée à **[Arme Lourde 1]** — une seule relance suffit, coût inchangé (7 pts).
- **Riverwatch Riders scindés en deux (D049, D050)** : le mot-clé d'origine « Vigilant Flanking » (BattleLore V2) combinait deux effets sur une seule unité. Emmanuel les répartit sur deux unités distinctes du Rohan : « Flanking » est renommée **[Prise de flanc]** et réassignée à l'**Éored de cavalier du Rohan** (profil 1, qui passe de 6 à **7 pts** — premier cas où la compression n'absorbe pas l'ajout) ; une nouvelle règle **[Vigilant]** (la cible ne peut jamais contre-attaquer, 2 pts) est créée et assignée à l'**Éored d'éclaireur** à la place. Coût de l'éclaireur inchangé (4 pts).

Les fichiers `02 - Factions/Rohan.md` (v1.3), `02 - Factions/Mordor.md` (v0.5), `02 - Factions/Khand.md` (v1.3), `[[Regles_Speciales]]` (v0.11), `[[Regles_Points]]` (v0.9) et `[[Document_de_cadrage]]` (v1.16) reflètent l'ensemble de ces révisions (D041, D043-D050). Le recul façon Memoir '44 (D041, §3.1 ci-dessus) a par ailleurs été formalisé dans **`[[Regles_Base]]` (v0.3)**.

---

*Version : 1.0 — Phase 1 — 2026-07-25. Compte rendu du Playtest #1 (`[[Playtest1_Avant-garde_sur_le_Pelennor]]`). Résultat 6–2 Mal ; constat structurant du centre-funnel ; décisions D040-D046 (recul Memoir '44, jeton contre-attaque, retrait de [Charge écrasante], [Arme de jet X], [Plateforme de tir X], 7 profils ajustés). Règles non éprouvées reportées au Playtest #1b.*
