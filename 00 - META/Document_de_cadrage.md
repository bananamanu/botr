---
projet: "Batailles de la Terre du Milieu"
type: "meta"
phase: "1"
statut: "en-cours"
date_maj: "2026-07-18"
tags: [BdTdM, type/meta, statut/en-cours]
version: "1.1"
---

# Document de cadrage du projet

> **Nature du document :** Ce fichier est le point d'entrée du projet. Il définit la vision, les contraintes de design, la feuille de route et les conventions à respecter dans tous les documents du projet. Il doit être fourni à Claude en début de session pour recadrer le contexte.

---

## Table des matières

1. [Vision du projet](#1-vision-du-projet)
2. [Références et inspirations](#2-références-et-inspirations)
3. [Principes de design](#3-principes-de-design)
4. [Composants du jeu](#4-composants-du-jeu)
5. [Axes d'adaptation — BLv2 vers la Terre du Milieu](#5-axes-dadaptation--blv2-vers-la-terre-du-milieu)
6. [Feuille de route](#6-feuille-de-route)
7. [Conventions de travail](#7-conventions-de-travail)
8. [Journal de décisions](#8-journal-de-décisions)

---

## 1. Vision du projet

**Batailles de la Terre du Milieu (BdTdM)** est une adaptation du système **Commands & Colors** / **BattleLore Seconde Édition** à l'univers du **Seigneur des Anneaux**.

### Ambition

Offrir un système générique pour rejouer les grands affrontements de la Terre du Milieu, décliné en plusieurs formats — **Escarmouche**, **Normal**, **Épique** — plutôt qu'un système taillé pour un seul scénario. La **Bataille des Champs du Pelennor**, objectif de la convention de fin septembre 2026, sert de cas d'usage pour le format **Épique** (6 joueurs, 3v3, 1 table).

### Philosophie de design

> _"Les règles doivent servir le thème, pas l'inverse."_

Le système hérite de l'architecture Commands & Colors / BLv2 (deck de cartes de commandement, dés à faces spéciales, profils d'unités portant les règles spéciales, PV par figurine). Abandon complet de la mécanique précédente à sac de tokens (Destin / Test of Honour).

Figurines MESBG, collection très complète.

---

## 2. Références et inspirations

### Références principales

| Jeu | Ce qu'on en retient |
|---|---|
| **BattleLore Seconde Édition** (FFG) | Référence mécanique principale : dés, règles spéciales, profils d'unités, avance, poursuite, contre-attaque universelle, système Lore (pouvoirs — hors scope V1, voir §5.2). |
| **Commands & Colors : Medievals** | Structure de commandement (cartes de section + Tactiques), proximité thématique médiévale, profils d'infanterie lourde. |

### Références secondaires

| Jeu | Ce qu'on en retient |
|---|---|
| **C&C Ancients** | Gestion des unités légères, règles d'évasion. |
| **Memoir '44** | Clarté de présentation des scénarios, format des cartes de terrain, médailles objectif. Règle [Arme à distance] (dés dégressifs avec la distance) — utile pour Archers de Mirkwood/Arcs Longs de Rohan. Face de dé « miss universel » (voir §5.2, D001). |
| **C&C Napoleonics** | Système de moral et de cohésion d'unité. |
| **BattleLore V1** | Règles de Peur/Terreur — pertinentes pour les Nazgûl, les Trolls, les Mûmakil. |
| **Battle of Westeros** | Bonus offensif +1 dé depuis le terrain surélevé. |
| **MESBG (sourcebook officiel)** | Référence de fidélité au texte de Tolkien pour les scénarios et objectifs narratifs — pas de reprise mécanique (échelle et système trop différents). |

---

## 3. Principes de design

1. **Priorité à la fluidité et à l'accessibilité** : les règles ne doivent jamais ralentir le jeu ni demander de consulter un livre en pleine partie. Contrainte forte : les joueurs sont expérimentés mais de moins en moins à l'aise avec les systèmes complexes — toute règle qui génère une question à chaque résolution est à réviser.
2. **Émotion et narration avant la profondeur tactique** : privilégier les moments marquants (charge des Rohirrim, duel Éowyn/Roi-Sorcier) plutôt que l'optimisation. Conditions de victoire narratives, propres à chaque scénario, fidèles au texte de Tolkien (pas aux films).
3. **Profils comme vecteurs de règles** : les règles spéciales vivent dans les profils d'unités, pas dans un livre de règles à consulter. Un joueur connaît son armée, pas le manuel.
4. **Lisibilité sur la table** : l'état du jeu doit être lisible d'un coup d'œil. Jetons acceptés pour PV et effets temporaires, jamais pour les règles permanentes.
5. **Scalabilité par le format, pas par la complexité** : un même socle de règles doit fonctionner en Escarmouche, Normal et Épique — on ajuste le nombre d'unités et la taille de table, jamais la complexité des règles de base.
6. **Asymétrie assumée** : chaque peuple (Gondor, Rohan, Mordor, Harad...) doit se jouer différemment. L'équilibre se fait par la diversité tactique, pas par la similitude des profils.
7. **Minimalisme des règles de terrain** : le terrain crée de la tension, pas de la complexité. Chaque type de terrain a un effet simple et mémorable.

---

## 4. Composants du jeu

### Champ de bataille

Tapis hexagonal, taille selon le format :

| Format | Taille | Usage |
|---|---|---|
| Escarmouche | 10 × 7 hexagones | Petits engagements, 1v1/2v2 |
| Normal | 13 × 9 hexagones | Format standard, 2v2/3v3 léger |
| Épique | 16 × 13 hexagones | Grands affrontements type Pelennor (3v3, 6 joueurs) |

Divisé verticalement en 3 sections (Gauche / Centre / Droite), quel que soit le format.

### Dés

6 faces : Épées croisées (1-2 touches mêlée), Épée (1 touche mêlée), Cible (1-2 touches tir), Drapeau (retraite), Couronne (capacité spéciale), **Arcane (miss universel en V1** — inspiration Memoir '44, voir D001).

### Unités

| Type | Figurines/hex | PV | Base |
|---|---|---|---|
| Infanterie | 6 | 1/fig. | 25 mm |
| Cavalerie | 3 | 1/fig. | 40 mm |
| Chars | 1 | Variable | 65 mm |
| Créature / Machine de guerre | 1 | Variable | 65 mm (ex. Troll du Mordor) |
| Artillerie | 1 pièce + servants | 1/servant | — |

Pas de distinction Infanterie standard/élite par le nombre de figurines ou la base (cohérent avec le principe 3 : la différenciation élite/standard passe par le profil, pas par l'effectif).

> ⚠️ **Point ouvert critique — Mûmakil**
> La figurine ne tient pas sur un hex standard (10 cm). Sujet sensible à traiter en profondeur, hors de ce document de cadrage. Pistes possibles : hex agrandi dédié, occupation de plusieurs hexes, ou gabarit hors-grille avec règles de zone d'effet. À planifier comme tâche de conception à part entière.

---

## 5. Axes d'adaptation — BLv2 vers la Terre du Milieu

### 5.1 Priorité haute — Cœur de règles

- [ ] Système de commandement : deck de cartes C&C (cartes de section + Tactiques). En Épique (3v3), chaque joueur contrôle une Section (Gauche/Centre/Droite) plutôt qu'une armée nommée — pas de sous-force nominative par joueur (D016)
- [ ] Dés : reprise des faces BLv2 (mêlée/tir/retraite/capacité/miss)
- [ ] Types d'unités : Infanterie, Cavalerie, Chars, Créature, Machine de guerre, Artillerie
- [ ] Règle Faible (dernière figurine), Contre-attaque universelle, Avance et Poursuite
- [ ] Règles spéciales de base : [Armure X], [Protection X], [Férocité], [Mobilité X]
- [ ] Formats Escarmouche / Normal / Épique — tables et volumes d'unités par format
- [ ] **Cas Mûmakil** : règle et gabarit dédiés (point ouvert critique, §4)

### 5.2 Priorité moyenne — Héros et monstres avancés

- [ ] Règles des héros à développer : une ébauche de structure a déjà été explorée ailleurs, à formaliser et adapter ici — valeur de commandement modulable, distinction Standard/Majeur (posée en cadrage 5)
- [ ] [Peur] / [Terreur] — Nazgûl, Trolls, Mûmakil, Roi-Sorcier
- [ ] Monstres avancés : vol (Fell Beasts), piétinement en zone (Mûmakil/Trolls)

> 🎲 **Note de design — Pas de couche pouvoirs/magie en V1**
> Hors scope pour l'instant (D001). Piste future : magie légère fondée sur les thèmes **Espoir** (Bien) / **Peur** (Mal), avec des dés personnalisés par camp portant sur la face concernée la **Rune de Gandalf** (Bien) et l'**Œil de Sauron** (Mal) au lieu du symbole Arcane générique.

### 5.3 Priorité basse — Contenu et scénarios

- [ ] Peuples à couvrir en V1 : **Gondor et ses fiefs, Rohan, Mordor, Harad, Khand, Easterling**
- [ ] Scénarios : Pelennor comme référence Épique, autres affrontements en Normal/Escarmouche
- [ ] Construction d'armée : valeurs en points par unité et héros

---

## 6. Feuille de route

Convention fin septembre 2026 — cadrage lancé le 18 juillet, soit environ 10 semaines.

### Phase 1 — Fondations (cœur de règles) ← EN COURS

- [ ] Formaliser le corps de règles de base (commandement, dés, types d'unités, Faible, contre-attaque, avance/poursuite, règles spéciales de base)
- [ ] Choisir le format de travail initial : Normal (plus rapide à tester qu'Épique)
- [ ] **Playtest #1**

### Phase 2 — Héros, cas Mûmakil, montée en Épique

- [ ] Développer les règles de héros (profils Standard/Majeur)
- [ ] Résoudre le cas Mûmakil (gabarit/règle dédiée)
- [ ] Passer au format Épique (16×13), premier test à cette échelle
- [ ] **Playtest #2**

### Phase 3 — Contenu Pelennor

- [ ] Profils d'unités pour les 6 peuples V1 (Gondor et fiefs, Rohan, Mordor, Harad, Khand, Easterling)
- [ ] Reprise et adaptation du travail déjà fait en cadrage 5 (forces, héros, objectifs narratifs) au nouveau système — répartition des peuples par Section plutôt que par sous-force nominative (D016)
- [ ] Valeurs en points, équilibrage Bien/Mal
- [ ] **Playtest #3** (scénario Pelennor complet)

### Phase 4 — Finalisation convention

- [ ] Livret de règles complet + aide de jeu imprimable
- [ ] Fiches unités/héros imprimables
- [ ] Répétition générale avant fin septembre

> ⚠️ **Point ouvert**
> Calendrier resserré (10 semaines) — le découpage tient si chaque phase reste ~2-3 semaines max. À surveiller après le Playtest #1.

---

## 7. Conventions de travail

### Blocs de note standardisés

```
> ⚠️ **Point ouvert**
> Question de design non résolue.

> 🔄 **Modifié après playtest**
> Date : YYYY-MM-DD | Playtest #N
> Description de la modification.

> 🔗 **Voir aussi**
> [[Lien vers règle connexe]]

> 🎲 **Note de design**
> Justification d'un choix de design.
```

### Terminologie fixée

| Terme retenu | Signification | Éviter |
|---|---|---|
| **Champ de bataille** | Surface de jeu (tapis hexagonal) | "Plateau", "Table" |
| **Unité** | Groupe de figurines occupant un hexagone | "Régiment", "Bande" |
| **Section** | Gauche / Centre / Droite du champ de bataille | "Flanc", "Aile" |
| **Ordre** | Activation d'une unité via une carte | "Activation", "Tour" |
| **Carte Tactique** | Carte spéciale (hors carte de section) | "Carte spéciale" |
| **Commandement** | Système de cartes/activation (sens C&C d'origine) — plus de sous-force nominative par joueur | "Commande" |
| **Peuple** | Camp jouable (Gondor, Rohan, Mordor...) | "Faction", "Race" |
| **Camp** | Bien / Mal | "Alliance", "Légion" |
| **Drapeau** | Face de dé forçant une retraite | "Bannière", "Étendard" |
| **Faible** | Unité à 1 PV restant (dernière figurine) | "Blessé", "En déroute" |
| **PV** | Points de Vie — une figurine = 1 PV | "Figurine" (dans un contexte de règle) |
| **Infanterie** | 6 fig., base 25 mm | "Fantassin", "Piéton" |
| **Cavalerie** | 3 fig., base 40 mm | "Cavalier", "Monture" |
| **Chars** | 1/hex, base 65 mm | "Chariot" |
| **Créature** | PV variables, jamais Faible | "Monstre", "Bête" |
| **Machine de guerre** | PV variables, jamais Faible | "Engin" |
| **Artillerie** | Servants éliminés en premier, jamais Faible | "Canon", "Pièce" |

---

## 8. Journal de décisions

| # | Date | Décision | Justification |
|---|---|---|---|
| 001 | 2026-07-18 | Face Arcane = miss universel en V1 | Simplicité, pas de couche magie prévue pour l'instant. Piste future : dés custom par camp (Rune de Gandalf / Œil de Sauron) pour une magie légère Espoir/Peur. |
| 002 | 2026-07-18 | Nom du projet : **Batailles de la Terre du Milieu (BdTdM)** | Basé directement sur Commands & Colors / BattleLore Seconde Édition — pas de dépendance affichée à un autre projet. |
| 003 | 2026-07-18 | Ambition multi-format : Escarmouche / Normal / Épique | Le Pelennor n'est qu'un cas d'usage (format Épique) d'un système générique pour la Terre du Milieu, pas l'unique objectif du système. |
| 004 | 2026-07-18 | Abandon complet de la mécanique à sac de tokens (Destin/Test of Honour) | Jugée trop fragile pour 6 joueurs peu à l'aise avec les règles complexes. Remplacée par le deck de commandement C&C/BLv2. |
| 005 | 2026-07-18 | Format Épique fixé à 16 × 13 hexagones | Dimensionné pour le scénario Pelennor (6 joueurs, 3v3, 1 table). |
| 006 | 2026-07-18 | Bases figurines MESBG : Infanterie 25 mm, Cavalerie 40 mm, Chars/Créatures 65 mm | Alignement sur les bases réelles de la collection MESBG plutôt que sur des valeurs génériques. |
| 007 | 2026-07-18 | Pas de distinction Infanterie standard/élite par base ou effectif | Cohérent avec le principe "profils comme vecteurs de règles" (§3.3) — la différenciation élite/standard passe par le profil, pas par le socle. |
| 008 | 2026-07-18 | Chars = type à 1 figurine/hex, base identique aux Trolls du Mordor (65 mm) | Simplifie la classification, réutilise un gabarit déjà existant. |
| 009 | 2026-07-18 | Cas Mûmakil identifié comme point ouvert critique, hors cadrage | La figurine ne tient pas sur un hex standard (10 cm) — nécessite une tâche de conception dédiée (gabarit ou occupation multi-hex). |
| 010 | 2026-07-18 | Pas de couche pouvoirs/magie pour la V1 | Hors scope pour la convention de septembre — priorité au socle de règles et au contenu Pelennor. |
| 011 | 2026-07-18 | Peuples à couvrir en V1 : Gondor et fiefs, Rohan, Mordor, Harad, Khand, Easterling | Correspond aux 6 commandements du scénario Pelennor (cadrage 5) — Elfes/Nains/Isengard réservés à une version future. |
| 012 | 2026-07-18 | Règles des héros à développer en Phase 2 | Une ébauche de structure existe ailleurs et doit être formalisée et adaptée au contexte BdTdM. |
| 013 | 2026-07-18 | Feuille de route en 4 phases sur ~10 semaines | Fondations → Héros/Mûmakil/Épique → Contenu Pelennor → Finalisation, calé sur l'échéance de fin septembre. |
| 014 | 2026-07-18 | Terminologie fixée : "Commandement" (sous-force), "Peuple" (camp jouable), "Camp" (Bien/Mal) | Clarté et cohérence terminologique pour tous les documents du projet. *(Révisé par D016.)* |
| 015 | 2026-07-18 | [Massif] retirée du socle de règles, sans remplacement en V1 | Règle héritée d'un système voisin pour différencier l'infanterie d'élite sur socle 25 mm (type Hommes-Lézards de Warhammer). Toutes les Infanteries de BdTdM partagent déjà la même base (25 mm) — le cas ne se présente plus. Si un besoin de différenciation apparaît en Phase 3, une nouvelle règle sera introduite à ce moment-là. |
| 016 | 2026-07-18 | Abandon de la sous-force nominative par joueur ("Commandement" ne désigne plus que le système de cartes/activation) | La logique "Rohan / Minas Tirith-Dol Amroth / Compagnie Grise" du cadrage 5 n'a plus de sens dans l'architecture C&C pure. En Épique (3v3), chaque joueur contrôle une Section (Gauche/Centre/Droite) ; la répartition des peuples entre sections devient une décision de scénario (Phase 3), pas une règle de commandement. Annule la définition "sous-force" de D014. |
| 017 | 2026-07-18 | Pas de terrain spécifique développé pour le Pelennor | Le champ de bataille est majoritairement plat (des champs qui s'étendent à perte de vue) — les règles de terrain génériques (bois, gué, terrain surélevé) suffiront pour d'éventuels éléments ponctuels introduits par le scénario. |

---

*Version : 1.1 — Phase 1 — 2026-07-18. [Massif] retirée (D015), sous-force nominative abandonnée au profit des Sections (D016), pas de terrain spécifique Pelennor (D017).*
*Document de cadrage initial de Batailles de la Terre du Milieu (BdTdM), établi par adaptation de la structure de cadrage d'un projet jumeau, sans reprise de son contenu mécanique spécifique.*
