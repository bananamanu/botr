---
projet: "Batailles de la Terre du Milieu"
type: "regles"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-07-18"
tags: [BdTdM, "type/regles", "phase/1", "statut/brouillon"]
version: "0.2"
---

# Batailles de la Terre du Milieu — Règles de base

> Ce document couvre les règles fondamentales de la Phase 1 : structure du tour, types d'unités, mouvement, combat, avance, poursuite et retraite. Les héros, la Peur/Terreur et les monstres avancés sont traités en Phase 2 (voir Document de cadrage §5.2 et §6). Premier brouillon à valider au Playtest #1.

---

## Table des matières

1. [Présentation générale](#1-présentation-générale)
2. [Composants](#2-composants)
3. [Mise en place](#3-mise-en-place)
4. [Déroulement d'un tour](#4-déroulement-dun-tour)
5. [Commandement](#5-commandement)
6. [Mouvement](#6-mouvement)
7. [Combat](#7-combat)
8. [Avance et poursuite](#8-avance-et-poursuite)
9. [Retraite](#9-retraite)
10. [Fin de partie](#10-fin-de-partie)

---

## 1. Présentation générale

**Batailles de la Terre du Milieu (BdTdM)** est un wargame tactique pour 2 camps (jusqu'à 6 joueurs en format Épique, 3 par camp) se déroulant dans l'univers du Seigneur des Anneaux. Il s'appuie sur le système **Commands & Colors / BattleLore Seconde Édition** comme référence mécanique : les joueurs manœuvrent leurs unités sur un champ de bataille hexagonal en jouant des **cartes de commandement**, résolvent les combats sur des **dés spéciaux** et cherchent à atteindre leur objectif de victoire avant l'adversaire.

Les règles de base couvrent les affrontements sans pouvoirs ni héros — le socle sur lequel s'appuieront les couches ajoutées en Phase 2 (héros, Peur/Terreur, monstres avancés).

---

## 2. Composants

### 2.1 Matériel de jeu

- **Tapis de jeu hexagonal** : taille selon le format choisi — Escarmouche (10 × 7), Normal (13 × 9) ou Épique (16 × 13). Voir Document de cadrage §4.
- **Tuiles de terrain** : bois, collines, cours d'eau, gués, ponts, bâtiments (règles détaillées à développer dans un document dédié — hors scope de cette première version)
- **Deck de commandement** : cartes de section et cartes Tactiques
- **Dés spéciaux** : 6 faces — Épées croisées / Épée / Cible / Drapeau / Couronne / Arcane
- **Figurines** : unités des peuples joués (MESBG)
- **Marqueurs** : jetons PV, médailles objectif

### 2.2 Unités et PV

Chaque unité est représentée par un groupe de figurines occupant un seul hexagone. Chaque figurine possède **1 PV**. Lorsqu'une figurine perd son dernier PV, elle est retirée du jeu.

Les touches s'accumulent au sein d'une même attaque. Les PV perdus ne se récupèrent pas.

#### Déroute

Lorsqu'une unité atteint **0 figurine**, elle est **en déroute** : retirez-la du champ de bataille. L'adversaire marque **1 point de victoire**, sauf indication contraire du scénario.

#### Unité Faible

Une unité est **Faible** lorsqu'il ne lui reste qu'**une seule figurine**, quelle que soit la façon dont elle a perdu les précédentes.

Une unité Faible subit l'effet suivant :

- Elle **ne peut pas causer de touche** sur une face **Épée** lors de ses attaques de mêlée.

> 💡 **Exemple de jeu**
> Des Piquiers de Gondor sont réduits à 1 figurine (Faibles). Lors de leur prochaine attaque en mêlée, les faces Épée n'infligent aucune touche — seules les Épées croisées comptent.

### 2.3 Types d'unités et règle générale de dégâts

Chaque unité est définie par **deux caractéristiques** indiquées dans son profil :

| Caractéristique | Valeurs possibles |
|---|---|
| **Type** | Infanterie · Cavalerie · Chars · Artillerie · Créature · Machine de guerre |
| **Combat** | Mêlée · À distance |

#### Règle générale — Dégâts par type de cible

Le nombre de figurines retirées par touche dépend du **type de l'unité ciblée** et de la **face de dé** obtenue :

| Face de dé | Cible Infanterie | Cible Cavalerie / Chars / Artillerie / Machine de guerre / Créature |
|---|---|---|
| **Épées croisées** | **2 figurines** | 1 figurine |
| **Épée** | 1 figurine | 1 figurine |
| **Cible** | **2 figurines** | 1 figurine |

> Cette règle s'applique automatiquement à toutes les attaques. Elle n'est pas répétée dans les profils individuels.

> 💡 **Exemple de jeu**
> Des Chevaliers de Dol Amroth (Cavalerie — Mêlée) attaquent des Épéistes de la Garde (Infanterie — Mêlée) adjacents : 4 dés. Résultat : Épées croisées, Épée, Épée, Drapeau. Les Épées croisées retirent **2 figurines**, chaque Épée retire **1 figurine** → 4 figurines retirées et 1 Drapeau.
>
> À l'inverse, si les Épéistes contre-attaquent les Chevaliers : Épées croisées → **1 figurine** retirée seulement (les Chevaliers sont Cavalerie, pas Infanterie).

#### Type Chars

Les **Chars** (ex. Char de Khand) occupent 1 hexagone et suivent les règles de dégâts standard des cibles non-Infanterie (1 figurine/véhicule par touche). Base 65 mm, identique aux Créatures/Trolls.

#### Type Artillerie

Les unités de type Artillerie fonctionnent différemment des autres unités :

- **PV = nombre de servants** : chaque servant est une figurine avec 1 PV.
- **1 dégât par touche** quelle que soit la face obtenue et quelle que soit la cible.
- Lorsque le **dernier servant est retiré**, l'unité est **détruite** — elle ne passe pas par l'état Faible.
- La pièce d'artillerie elle-même n'est pas une figurine : elle est retirée avec les servants.

> 💡 **Exemple de jeu**
> Une Baliste de Minas Tirith (Artillerie — 2 servants) reçoit 3 touches : les 2 servants sont retirés → la Baliste est détruite immédiatement. Il n'y a pas d'état Faible.

---

## 3. Mise en place

### 3.1 Préparation

1. Dépliez le tapis de jeu selon le format choisi (Escarmouche, Normal ou Épique).
2. Placez les éléments de terrain définis par le scénario.
3. Constituez le deck de commandement selon le format.
4. Chaque joueur (ou chaque commandement, en format Épique) prend en main le nombre de cartes défini par son format.
5. Déterminez qui déploie en premier (défini par le scénario, ou tirage au sort).

### 3.2 Déploiement alterné

Les joueurs déploient leurs unités en **alternant**, une unité à la fois, en commençant par le joueur désigné par le scénario.

- Chaque unité est placée dans la **zone de déploiement** définie par le scénario.
- Un joueur ne peut pas placer deux unités dans le même hexagone.
- Le déploiement est terminé quand toutes les unités des deux camps sont sur le champ de bataille.

> 🎲 **Note de design**
> Le déploiement alterné permet à chaque joueur de réagir au placement adverse et crée des décisions tactiques dès la mise en place.

---

## 4. Déroulement d'un tour

Un tour se déroule en **deux phases** successives.

### Phase principale

#### a. Étape de commandement

Le joueur actif choisit **une carte** dans sa main et la joue face visible. Cette carte définit quelles unités peuvent être activées ce tour.

> 💡 **Règle d'urgence** : si aucune carte ne couvre les unités que vous souhaitez activer, vous pouvez **ignorer le texte** de n'importe quelle carte et activer **1 unité de votre choix** sur l'ensemble du champ de bataille.

#### b. Étape d'ordre

Le joueur actif désigne les unités éligibles conformément à la carte jouée. Il les **déclare activées** une à une. Une unité non activée ne peut ni bouger ni combattre ce tour.

#### c. Étape de mouvement

Les unités activées effectuent leur mouvement dans l'ordre choisi par le joueur actif. Une unité peut choisir de ne pas bouger. Toute unité doit terminer son mouvement avant qu'une autre commence.

#### d. Étape d'attaque

Les unités activées qui sont en mesure de combattre effectuent leurs attaques dans l'ordre choisi par le joueur actif. Une unité peut choisir de ne pas attaquer.

### Phase de bilan

#### e. Étape des points de victoire

Le joueur actif marque les points de victoire éventuellement gagnés par des **médailles objectif** définies dans le scénario.

#### f. Étape de pioche

Le joueur actif pioche une nouvelle carte pour ramener sa main au nombre de cartes de son format. Si le deck est épuisé, mélangez la défausse pour en former un nouveau.

---

## 5. Commandement

> 🔄 **Résolu — 2026-07-18**
> Pas de sous-force nominative par joueur (abandon de la logique « Rohan / Minas Tirith-Dol Amroth / Compagnie Grise » du cadrage 5). « Commandement » ne désigne plus qu'une seule chose : le système de cartes/activation ci-dessous. En format Épique (3v3), **chaque joueur contrôle une Section** (Gauche, Centre ou Droite) plutôt qu'une armée nommée — la répartition des peuples entre les sections reste une décision de scénario (Phase 3), pas une règle de commandement.

### 5.1 Cartes de section

Une **carte de section** (Gauche, Centre ou Droite) permet d'activer **toutes les unités** situées dans la section correspondante au moment où la carte est jouée.

> 💡 **Exemple de jeu**
> Le joueur Gondor joue « Ordre Centre ». Il active toutes ses unités en section centrale — deux unités de Piquiers et une unité d'Archers. Il déplace les Piquiers et fait tirer les Archers.

### 5.2 Cartes Tactiques

Les **cartes Tactiques** permettent d'activer un nombre limité d'unités selon des critères définis sur la carte (ex. : « 3 unités de Cavalerie », « 2 unités dans n'importe quelle section »). Ce nombre est souvent égal à la valeur de commandement du joueur.

### 5.3 Valeur de commandement

La valeur de commandement est égale au **nombre de cartes dans la main du joueur actif** au moment où il joue sa carte (cette carte comprise).

- **En Phase 1** (sans héros) : la valeur de commandement est déterminée uniquement par la taille de la main.
- **En Phase 2+** (avec héros) : elle sera recalculée en tenant compte des héros vivants (règle à développer).

### 5.4 Règle d'urgence

Si aucune unité éligible ne peut être activée avec la carte jouée (ex. aucune unité dans la section visée), le joueur peut **ignorer le texte** de la carte et activer **1 unité de son choix** n'importe où sur le champ de bataille.

### 5.5 Jeu à plusieurs joueurs (format Épique)

En Épique, chaque camp compte 3 joueurs, un par section. Répartition des cartes, ordre de jeu entre les 3 joueurs d'un même camp et gestion de la main partagée (ou non) restent **à définir** — ce n'est pas nécessaire pour le Playtest #1 (prévu en format Normal, 1 joueur par camp), mais devra être réglé avant le premier test en Épique (Phase 2 de la feuille de route).

---

## 6. Mouvement

### 6.1 Valeur de mouvement

Chaque unité possède une **valeur de mouvement** définie dans son profil. Elle indique le nombre maximal d'hexagones qu'elle peut traverser lors de son activation. Une unité peut toujours choisir de se déplacer de moins que sa valeur maximale, ou de ne pas se déplacer.

### 6.2 Règles de mouvement

- Une unité ne peut pas **traverser** un hexagone occupé par une autre unité (amie ou ennemie).
- Une unité ne peut pas **entrer** dans un hexagone occupé par une unité ennemie (sauf lors d'une avance — voir §8).
- Une unité ne peut pas **sortir** du champ de bataille.
- Les **sections** (Gauche, Centre, Droite) n'ont aucun effet sur le mouvement — elles ne s'appliquent qu'à l'activation.

### 6.3 Effets de terrain sur le mouvement

Règles génériques de départ (à affiner dans un document de terrain dédié, hors scope de cette version) :

- **Terrain boisé** : une unité qui entre dans un hexagone boisé **s'y arrête immédiatement**.
- **Gué** : une unité qui entre dans un hexagone de gué **s'y arrête immédiatement**.
- **Bâtiment** : une unité qui entre dans un hexagone de bâtiment **s'y arrête immédiatement**.
- **Cours d'eau** : **impassable** — aucune unité ne peut y entrer (sauf gué ou pont).
- **Terrain surélevé** : aucune restriction — mouvement libre.

> 🔄 **Résolu — 2026-07-18**
> Pas de terrain spécifique à développer pour le Pelennor : le champ de bataille est majoritairement plat (des champs qui s'étendent à perte de vue). Les règles génériques ci-dessus suffiront pour d'éventuels éléments ponctuels que le scénario voudrait introduire (bosquet, talus).

---

## 7. Combat

### 7.1 Séquence de résolution d'un combat

Quelle que soit la nature de l'attaque (mêlée ou tir), la résolution suit toujours la séquence suivante :

1. **Déclarer la cible** : choisir une unité ennemie éligible (adjacente pour la mêlée, à portée et en ligne de vue pour le tir).
2. **Lancer les dés** : lancer un nombre de dés égal à la valeur d'attaque de l'unité, modifiée par les effets de terrain si applicable.
3. **Relancer et modifier** : utiliser les capacités ou effets disponibles.
4. **Appliquer [Armure X]** si applicable : retirer X faces Épée des résultats.
5. **Compter les touches et les Drapeaux** : identifier les faces actives selon le type d'attaque.
6. **Appliquer [Protection X]** si applicable : ignorer X touches.
7. **Retirer les figurines** selon la règle générale de dégâts (voir §2.3).
8. **Résoudre la retraite** : 1 Drapeau = 1 hexagone. Appliquer [Inébranlable X] si applicable.
9. **Contre-attaque** si les conditions sont réunies (adjacente, pas de retraite, non éliminée).
10. **Avance** si la cible est éliminée ou en retraite.

### 7.2 Attaque de mêlée

Une unité de mêlée peut attaquer une **unité ennemie adjacente** (dans l'un des 6 hexagones voisins).

Les faces actives en mêlée sont :
- **Épées croisées** : touche inconditionnelle
- **Épée** : touche — **inactive si l'unité est Faible**
- **Drapeau** : retraite
- **Couronne** : capacité spéciale (si profil)
- **Cible** et **Arcane** : échec en mêlée

### 7.3 Attaque de tir

Une unité à distance peut attaquer une unité ennemie **à portée et en ligne de vue**. Elle peut également attaquer une unité **adjacente** (en utilisant la face Cible comme si c'était du tir).

Les faces actives au tir sont :
- **Cible** : touche inconditionnelle
- **Drapeau** : retraite
- **Couronne** : capacité spéciale (si profil)
- **Épées croisées**, **Épée** et **Arcane** : échec au tir

### 7.4 Ligne de vue

La ligne de vue est tracée du **centre de l'hexagone attaquant** au **centre de l'hexagone cible**. Elle est bloquée par :
- Les hexagones de **terrain boisé** traversés
- Les hexagones de **bâtiment** traversés
- Les hexagones de **terrain surélevé** traversés (sauf si l'attaquant est aussi en hauteur)
- Les **unités** (amies ou ennemies) occupant les hexagones traversés

### 7.5 Modificateurs de dés liés au terrain

Certains terrains modifient le nombre de dés lancés. Ces modificateurs s'appliquent **avant** tout bonus ou malus du profil.

| Situation | Effet sur les dés |
|---|---|
| Attaquant ou cible en **terrain boisé** | Maximum **2 dés** |
| Attaquant ou cible en **gué** | Maximum **2 dés** |
| Attaquant en **terrain surélevé**, cible en contrebas | **+1 dé** (mêlée et tir) |

> ⚠️ **Rappel — Règle générale de dégâts :** le nombre de figurines retirées par touche dépend du **type de la cible**. Épées croisées et Cible retirent **2 figurines** sur une cible Infanterie, et **1 figurine** sur toutes les autres cibles. Voir §2.3.

### 7.6 Contre-attaque

Après avoir subi une attaque et résolu toutes les retraites, l'unité ciblée peut **contre-attaquer** si les trois conditions suivantes sont réunies :

- Elle est **adjacente** à l'attaquant.
- Elle est **restée dans le même hexagone** (aucune retraite effectuée).
- Elle **n'a pas été éliminée**.

La contre-attaque est **universelle** — toute unité peut contre-attaquer sans règle spéciale. Elle s'effectue à la valeur d'attaque complète selon la séquence normale (étapes 1 à 8 uniquement — pas d'avance ni de nouvelle contre-attaque).

---

## 8. Avance et poursuite

### 8.1 Avance

Après avoir **éliminé** ou **forcé la retraite** d'une cible adjacente lors d'un combat de mêlée, l'unité attaquante peut **avancer** dans l'hexagone que la cible occupait.

- L'avance est **universelle** et **optionnelle**.
- Une unité qui avance **ne peut pas être contre-attaquée** au titre de cette avance.

### 8.2 Poursuite ([Poursuite X])

Certaines unités possèdent **[Poursuite X]**. Lorsqu'elles peuvent avancer, elles peuvent choisir à la place d'effectuer une **poursuite** :

1. Se déplacer d'**au moins 1 hexagone** et jusqu'à **X hexagones**, en passant par l'hexagone libéré.
2. Effectuer **une attaque supplémentaire** contre une unité adjacente à la nouvelle position.
3. Utilisation limitée à **une seule fois par tour**.

---

## 9. Retraite

### 9.1 Résolution de la retraite

La retraite est résolue immédiatement après le retrait des figurines (étape 8 de la séquence de combat).

Chaque face **Drapeau** obtenue par l'attaquant force la cible à reculer d'**1 hexagone**. Il n'y a pas de valeur de moral : **1 Drapeau = 1 hexagone**, sans exception.

> **[Inébranlable X]** est le seul modificateur : l'unité ignore X Drapeaux par attaque reçue, quelle qu'en soit la source.

### 9.2 Direction de la retraite

- **Mêlée :** la cible recule dans la direction **à l'opposé de l'unité attaquante**.
- **Tir :** la cible recule dans la direction **à l'opposé du bord d'hexagone par lequel la ligne de vue a été tracée**.

### 9.3 Obstacles sur le chemin

Le terrain **n'a aucun effet** sur la retraite — une unité la traverse librement, y compris la forêt, le gué et le bâtiment.

Seules deux situations **bloquent** la retraite et infligent **1 touche par hexagone non résolu** :

| Obstacle rencontré | Effet |
|---|---|
| Forêt, gué, bâtiment, terrain surélevé, pont | Aucun — retraite continue normalement. |
| Cours d'eau / bord du plateau | Bloqué — 1 touche par hexagone non résolu. |
| Unité ennemie | Bloqué — 1 touche par hexagone non résolu. |
| Unité amie | **Soutien** — tous les hex restants ignorés, 0 touche supplémentaire. |

### 9.4 Après la retraite

Une unité ayant effectué une retraite **ne peut pas contre-attaquer** ce tour.

---

## 10. Fin de partie

### 10.1 Points de victoire

Chaque **unité ennemie mise en déroute** rapporte **1 point de victoire**. Des points supplémentaires peuvent être accordés par les **médailles objectif** définies dans le scénario.

### 10.2 Condition de victoire

La partie se termine dès qu'un camp atteint le **seuil de victoire** défini par le scénario :

| Format | Seuil indicatif |
|---|---|
| Escarmouche | 4 points |
| Normal | 6 points |
| Épique | 8 points |

> ⚠️ **Point ouvert** — ces seuils sont repris tels quels d'un système voisin, à valider (ou recalibrer) au Playtest #1.

---

## Récapitulatif rapide

### Séquence de tour

| Phase | Étape | Action |
|---|---|---|
| Principale | Commandement | Jouer une carte de commandement |
| | Ordre | Déclarer les unités activées |
| | Mouvement | Effectuer les mouvements |
| | Attaque | Résoudre les combats |
| Bilan | Points de victoire | Marquer les médailles objectif |
| | Pioche | Piocher 1 carte |

### Séquence de résolution d'un combat

1. Déclarer la cible
2. Lancer les dés (valeur d'attaque, modifiée par le terrain si applicable)
3. Relancer / modifier (effets et capacités)
4. Appliquer [Armure X] si applicable
5. Compter les touches et les Drapeaux
6. Appliquer [Protection X] si applicable
7. Retirer les figurines (voir tableau de dégâts ci-dessous)
8. Résoudre la retraite (1 Drapeau = 1 hex · [Inébranlable X] si applicable)
9. Contre-attaque si conditions réunies
10. Avance si cible éliminée ou en retraite

### Tableau de dégâts par type de cible

| Face de dé | Cible Infanterie | Cible Cavalerie / Chars / Artillerie / Machine de guerre / Créature |
|---|---|---|
| **Épées croisées** | **2 figurines** | 1 figurine |
| **Épée** | 1 figurine | 1 figurine |
| **Cible** | **2 figurines** | 1 figurine |

### Résumé des faces de dés

| Face | Mêlée | Tir |
|---|---|---|
| Épées croisées | 1 ou 2 touches* | Échec |
| Épée | 1 touche (sauf si Faible) | Échec |
| Cible | Échec | 1 ou 2 touches* |
| Drapeau | 1 hex de retraite | 1 hex de retraite |
| Couronne | Capacité spéciale | Capacité spéciale |
| Arcane | Échec (miss universel — V1, voir cadrage §5.2) | Échec (miss universel — V1) |

*\* 1 touche sur Cavalerie/Chars/Artillerie/Créature/Machine de guerre — 2 touches sur Infanterie (sans [Massif]). Voir §2.3.*

### Mémo règles spéciales de base

| Règle | Résumé |
|---|---|
| **Faible** | Dernière figurine : Épée inactive en attaque |
| **[Armure X]** | Retire X faces Épée des attaques de mêlée reçues |
| **[Protection X]** | Ignore X touches par attaque (terrain, fortifications) |
| **[Inébranlable X]** | Ignore X résultats de retraite par attaque reçue |
| **[Poursuite X]** | Alternative à l'avance : déplacement + attaque supplémentaire |
| **[Mobilité X]** | Déplacement supplémentaire après l'étape d'attaque |
| **[Férocité]** | Contre-attaque avant résolution des retraites |

---

## Points ouverts de ce document

| # | Sujet | Renvoi |
|---|---|---|
| 1 | Seuils de victoire par format, à valider au Playtest #1 | §10.2 |
| 2 | Répartition des cartes et ordre de jeu à 3 joueurs par camp (format Épique) | §5.5 |

---

*Version : 0.2 — Phase 1 — 2026-07-18. [Massif] retirée, commandement/terrain Pelennor clarifiés. Non testé.*
