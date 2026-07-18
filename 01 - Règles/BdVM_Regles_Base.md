---
projet: "Batailles du Vieux Monde"
type: "regles"
phase: 1.6
statut: "à-tester"
date_maj: "2026-06-01"
tags: [BdVM, "type/regles", "phase/1.6", "statut/à-tester"]
---

# Batailles du Vieux Monde — Règles de base

> Ce document couvre les règles fondamentales de la Phase 1.6 : structure du tour (alignée BattleLore V2), types d'unités, mouvement, combat, avance, poursuite et retraite. La magie, les monstres et les personnages héroïques sont traités dans les documents de Phase 2. La règle de **Peur** est introduite dès cette phase ; la **Terreur** est réservée à la Phase 2.

> 🔄 **Mise à jour — 2026-06-01 | Phase 1.6 Étape 6**
> - **§9** : réécriture complète — suppression de la valeur de Moral (D063). §9.3 : alignement C&C standard (D091) — seul le terrain impassable bloque la retraite, forêt/gué/bâtiment sans effet. [Inébranlable X] est le seul modificateur.
> - **§7.1 étape 8** : reformulation sans référence au Moral.
> - **Récapitulatif** : mémo Faible et séquence de combat mis à jour.
> - Titre du §9 renommé : "Moral et retraite" → "Retraite".

> 🔄 **Mise à jour — 2026-05-30 | Phase 1.6 Étape 4**
> - **§7.5** : ajout du bonus de terrain surélevé (+1 dé depuis la hauteur — D086). Mise à jour des renvois vers [[BdVM_Terrain]].
> - **Récapitulatif** : mémo règles spéciales de base mis à jour — suppression de [Cavalerie] (absorbé par le type, jamais une règle spéciale) et de [Tenace] (retiré de la majorité des unités en D072, réservé à un usage exceptionnel).

> 🔄 **Modifié — 2026-05-23 | Phase 1.6 Étape 2**
> - Introduction des **types d'unités** (§2.3) : Infanterie, Cavalerie, Artillerie, Créature, Machine de guerre
> - Introduction de la **règle générale "2 dégâts sur Infanterie"** (§2.3)
> - Introduction de **[Massif]** comme protection contre le bonus Infanterie (§2.3)
> - Introduction du **type Artillerie** et de ses règles (§2.3)
> - Formalisation du **déploiement alterné** (§3.2)
> - Mise à jour du récapitulatif des dés avec renvoi vers §2.3 (§7.5)
> - Mise à jour du mémo règles spéciales de base (récapitulatif)

---

## Table des matières

1. [[#1. Présentation générale]]
2. [[#2. Composants]]
3. [[#3. Mise en place]]
4. [[#4. Déroulement d'un tour]]
5. [[#5. Commandement]]
6. [[#6. Mouvement]]
7. [[#7. Combat]]
8. [[#8. Avance et poursuite]]
9. [[#9. Retraite]]
10. [[#10. Peur]]
11. [[#11. Fin de partie]]

---

## 1. Présentation générale

**Batailles du Vieux Monde** est un wargame tactique pour **2 joueurs** se déroulant dans l'univers de Warhammer Fantasy Battle. Il s'appuie sur le système **BattleLore Seconde Édition** (FFG) comme référence mécanique principale : les joueurs manœuvrent leurs unités sur un champ de bataille hexagonal en jouant des **cartes de commandement**, résolvent les combats sur des **dés spéciaux** et cherchent à atteindre leur objectif de victoire avant l'adversaire.

Chaque partie représente une bataille rangée entre deux armées du Vieux Monde. Les règles de base couvrent les affrontements sans magie ni créatures fantastiques — l'épine dorsale du jeu sur laquelle toutes les extensions de règles s'appuient.

> 🔄 **Modifié après playtest** — 2026-04-24 | Playtest #01
> Pivot vers BattleLore V2 comme référence mécanique principale (décision D022). Structure du document refondée en conséquence.

---

## 2. Composants

### 2.1 Matériel de jeu

- **Tapis de jeu hexagonal** : 13 × 9 hexagones (format Bataille standard)
- **Tuiles de terrain** : bois, collines, cours d'eau, guésl, ponts, bâtiments
- **Deck de commandement** : cartes de section et cartes Tactiques (voir [[BdVM_Cartes_Commandement]])
- **Dés spéciaux** : 6 faces — Épées croisées / Épée / Cible / Drapeau / Couronne / Arcane
- **Figurines** : unités des factions jouées (voir profils d'unités)
- **Marqueurs** : jetons PV, jetons de rechargement, médailles objectif

### 2.2 Unités et PV

Chaque unité est représentée par un groupe de figurines occupant un seul hexagone. Chaque figurine possède **1 PV**. Lorsqu'une figurine perd son dernier PV, elle est retirée du jeu.

Les touches s'accumulent au sein d'une même attaque. Les PV perdus ne se récupèrent pas.

#### Déroute

Lorsqu'une unité atteint **0 figurine**, elle est **en déroute** : retirez-la du champ de bataille. L'adversaire marque **1 point de victoire**, sauf indication contraire dans le profil ou dans les règles du scénario.

#### Unité Faible

Une unité est **Faible** lorsqu'il ne lui reste qu'**une seule figurine**, quelle que soit la façon dont elle a perdu les précédentes.

Une unité Faible subit l'effet suivant :

- Elle **ne peut pas causer de touche** sur une face **Épée** lors de ses attaques de mêlée.

> 💡 **Exemple de jeu**
> Des Hallebardiers sont réduits à 1 figurine (Faibles). Lors de leur prochaine attaque en mêlée, les faces Épée n'infligent aucune touche — seules les Épées croisées comptent.

### 2.3 Types d'unités et règle générale de dégâts

Chaque unité est définie par **deux caractéristiques** indiquées dans son profil :

| Caractéristique | Valeurs possibles |
|---|---|
| **Type** | Infanterie · Cavalerie · Artillerie · Créature · Machine de guerre |
| **Combat** | Mêlée · À distance |

Ces deux caractéristiques déterminent comment l'unité attaque et comment elle encaisse les dégâts.

#### Règle générale — Dégâts par type de cible

Le nombre de figurines retirées par touche dépend du **type de l'unité ciblée** et de la **face de dé** obtenue :

| Face de dé | Cible Infanterie | Cible Cavalerie | Cible Artillerie | Cible Créature |
|---|---|---|---|---|
| **Épées croisées** | **2 figurines** | 1 figurine | 1 figurine | 1 figurine |
| **Épée** | 1 figurine | 1 figurine | 1 figurine | 1 figurine |
| **Cible** | **2 figurines** | 1 figurine | 1 figurine | 1 figurine |

> Cette règle s'applique automatiquement à toutes les attaques. Elle n'est pas répétée dans les profils individuels.
> La Machine de guerre suit les mêmes règles de dégâts que la Cavalerie — 1 figurine par touche.

> 💡 **Exemple de jeu**
> Des Chevaliers (Cavalerie — Mêlée) attaquent des Épéistes (Infanterie — Mêlée) adjacents : 4 dés. Résultat : Épées croisées, Épée, Épée, Drapeau. Les Épées croisées retirent **2 figurines**, chaque Épée retire **1 figurine** → 4 figurines retirées et 1 Drapeau. Les Épéistes passent à 2 figurines.
>
> À l'inverse, si les Épéistes contre-attaquent les Chevaliers : Épées croisées → **1 figurine** retirée seulement (les Chevaliers sont Cavalerie, pas Infanterie).

#### [Massif]

Certaines unités d'Infanterie sur socle 25 mm et tous les Créatures possèdent la propriété **[Massif]** :

> **[Massif] :** cette unité ignore le bonus de dégâts sur les cibles Infanterie. Toutes les touches lui retirent **1 figurine**, quelle que soit la face obtenue (Épées croisées ou Cible).

[Massif] est indiqué dans le profil pour les unités Infanterie 25 mm (ex. Saurus à l'Épée, Gardes du Temple). Pour les Créatures, [Massif] est une **propriété native du type** — il n'est pas répété dans le profil.

> 💡 **Exemple de jeu**
> Des Hallebardiers attaquent des Saurus à l'Épée [Massif] : Épées croisées → **1 figurine** retirée seulement (et non 2). [Massif] annule le bonus Infanterie.

#### Type Artillerie

Les unités de type Artillerie fonctionnent différemment des autres unités :

- **PV = nombre de servants** : chaque servant est une figurine avec 1 PV.
- **1 dégât par touche** quelle que soit la face obtenue et quelle que soit la cible.
- Lorsque le **dernier servant est retiré**, l'unité est **détruite** — elle ne passe pas par l'état Faible.
- La pièce d'artillerie elle-même (canon, trébuchet, catapulte) n'est pas une figurine : elle est retirée avec les servants.

> 💡 **Exemple de jeu**
> Un Canon de l'Empire (Artillerie — 2 servants) reçoit 3 touches : les 2 servants sont retirés → le Canon est détruit immédiatement. Il n'y a pas d'état Faible.

> ⚠️ **Règles spéciales d'Artillerie** : certaines unités Artillerie possèdent des règles qui modifient ce comportement standard. Exemple : [Bête incontrôlable] des Salamandres — voir [[BdVM_Regles_Speciales]].

---

## 3. Mise en place

### 3.1 Préparation

1. Dépliez le tapis de jeu selon le format choisi (Escarmouche, Bataille ou Épique).
2. Placez les éléments de terrain définis par le scénario.
3. Constituez le deck de commandement selon le format (voir [[BdVM_Cartes_Commandement]]).
4. Chaque joueur prend en main le nombre de cartes défini par son format.
5. Déterminez qui déploie en premier (défini par le scénario, ou tirage au sort).

### 3.2 Déploiement alterné

Les joueurs déploient leurs unités en **alternant**, une unité à la fois, en commençant par le joueur désigné par le scénario.

- Chaque unité est placée dans la **zone de déploiement** définie par le scénario.
- Un joueur ne peut pas placer deux unités dans le même hexagone.
- Le déploiement est terminé quand toutes les unités des deux armées sont sur le champ de bataille.

> 🎲 **Note de design** Le déploiement alterné a été validé au Playtest #2 (D065). Il permet à chaque joueur de réagir au placement adverse et crée des décisions tactiques dès la mise en place.

> 🔄 **Modifié — 2026-05-23 | Phase 1.6**
> Formalisation du déploiement alterné (décision D065 — validé Playtest #2).

---

## 4. Déroulement d'un tour

Un tour se déroule en **deux phases** successives.

### Phase principale (*Main Phase*)

#### a. Étape de commandement (*Command Step*)

Le joueur actif choisit **une carte** dans sa main et la joue face visible. Cette carte définit quelles unités peuvent être activées ce tour.

> 💡 **Règle d'urgence** : si aucune carte ne couvre les unités que vous souhaitez activer, vous pouvez **ignorer le texte** de n'importe quelle carte et activer **1 unité de votre choix** sur l'ensemble du champ de bataille.

#### b. Étape d'ordre (*Order Step*)

Le joueur actif désigne les unités éligibles conformément à la carte jouée. Il les **déclare activées** une à une. Une unité non activée ne peut ni bouger ni combattre ce tour.

#### c. Étape de mouvement (*Move Step*)

Les unités activées effectuent leur mouvement dans l'ordre choisi par le joueur actif. Une unité peut choisir de ne pas bouger. Toute unité doit terminer son mouvement avant qu'une autre commence.

#### d. Étape d'attaque (*Attack Step*)

Les unités activées qui sont en mesure de combattre effectuent leurs attaques dans l'ordre choisi par le joueur actif. Une unité peut choisir de ne pas attaquer.

### Phase de bilan (*Upkeep Phase*)

#### e. Étape des points de victoire (*VP Step*)

Le joueur actif marque les points de victoire éventuellement gagnés par des **médailles objectif** définies dans le scénario.

#### f. Étape de pioche (*Draw Step*)

Le joueur actif pioche une nouvelle carte pour ramener sa main au nombre de cartes de son format. Si le deck est épuisé, mélangez la défausse pour en former un nouveau.

#### g. Étape de lore (*Lore Step*) — *Phase 2*

Cette étape est **inactive en Phase 1.6**. Elle sera introduite en Phase 2 avec le système de magie.

> 🔄 **Modifié après playtest** — 2026-04-27 | Post-Playtest #01
> Adoption de la nomenclature BLv2 : Main Phase + Upkeep Phase (décision D043).

---

## 5. Commandement

### 5.1 Cartes de section

Une **carte de section** (Gauche, Centre ou Droite) permet d'activer **toutes les unités** situées dans la section correspondante au moment où la carte est jouée.

> 💡 **Exemple de jeu**
> Le joueur Empire joue "Ordre Centre". Il active toutes ses unités en section centrale — deux unités d'Hallebardiers et une unité d'Archers. Il déplace les Hallebardiers et fait tirer les Archers.

### 5.2 Cartes Tactiques

Les **cartes Tactiques** permettent d'activer un nombre limité d'unités selon des critères définis sur la carte (ex. : "3 unités de Cavalerie", "2 unités dans n'importe quelle section"). Ce nombre est souvent égal à la **valeur de commandement** du joueur.

### 5.3 Valeur de commandement

La valeur de commandement est égale au **nombre de cartes dans la main du joueur actif** au moment où il joue sa carte (cette carte comprise).

- **En Phase 1.6** (sans héros) : la valeur de commandement est déterminée uniquement par la taille de la main.
- **En Phase 2+** (avec héros) : elle sera calculée sur la base 3 + valeur du meilleur héros vivant.

### 5.4 Règle d'urgence

Si aucune unité éligible ne peut être activée avec la carte jouée (ex. aucune unité dans la section visée), le joueur peut **ignorer le texte** de la carte et activer **1 unité de son choix** n'importe où sur le champ de bataille.

> 🔗 **Voir aussi** [[BdVM_Cartes_Commandement]]

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

Certains terrains imposent des restrictions au mouvement :

- **Terrain boisé** : une unité qui entre dans un hexagone boisé **s'y arrête immédiatement**.
- **Gué** : une unité qui entre dans un hexagone de gué **s'y arrête immédiatement**.
- **Bâtiment** : une unité qui entre dans un hexagone de bâtiment **s'y arrête immédiatement**.
- **Cours d'eau** : **impassable** — aucune unité ne peut y entrer (sauf gué ou pont).
- **Terrain surélevé** : aucune restriction — mouvement libre.

> 🔗 **Voir aussi** [[BdVM_Terrain]] — règles détaillées par type de terrain.

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

> 🔗 **Voir aussi** [[BdVM_Terrain]] §2 — règles détaillées de ligne de vue.

### 7.5 Modificateurs de dés liés au terrain

Certains terrains modifient le nombre de dés lancés. Ces modificateurs s'appliquent **avant** tout bonus ou malus du profil.

| Situation | Effet sur les dés |
|---|---|
| Attaquant ou cible en **terrain boisé** | Maximum **2 dés** |
| Attaquant ou cible en **gué** | Maximum **2 dés** |
| Attaquant en **terrain surélevé**, cible en contrebas | **+1 dé** (mêlée et tir) |

> **Note sur [Terrain favori : Boisé] :** les unités possédant cette règle (ex. Skinks) ignorent le plafond de 2 dés en terrain boisé.

> 🔗 **Voir aussi** [[BdVM_Terrain]] §4 (terrain boisé), §5 (terrain surélevé), §7 (gué) — tableau complet des effets de terrain sur le combat.

> ⚠️ **Rappel — Règle générale de dégâts :** le nombre de figurines retirées par touche dépend du **type de la cible**. Épées croisées et Cible retirent **2 figurines** sur une cible Infanterie (sans [Massif]), et **1 figurine** sur toutes les autres cibles. Voir §2.3.

### 7.6 Contre-attaque

Après avoir subi une attaque et résolu toutes les retraites, l'unité ciblée peut **contre-attaquer** si les trois conditions suivantes sont réunies :

- Elle est **adjacente** à l'attaquant.
- Elle est **restée dans le même hexagone** (aucune retraite effectuée).
- Elle **n'a pas été éliminée**.

La contre-attaque est **universelle** — toute unité peut contre-attaquer sans règle spéciale. Elle s'effectue à la valeur d'attaque complète selon la séquence normale (étapes 1 à 8 uniquement — pas d'avance ni de nouvelle contre-attaque).

> 🔄 **Modifié après playtest** — 2026-04-24 | Playtest #01
> Contre-attaque universelle (décision D026 — alignement BLv2).

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
4. Une unité avec [Férocité] qui a forcé une retraite **ne peut pas** utiliser [Poursuite] ce tour.

> 💡 **Exemple de jeu**
> Des Saurus sur Sang-froid [Poursuite 2] éliminent des Épéistes adjacents. Ils poursuivent sur 2 hexagones et attaquent une seconde unité adjacente à leur nouvelle position.

---

## 9. Retraite

### 9.1 Résolution de la retraite

La retraite est résolue immédiatement après le retrait des figurines (étape 8 de la séquence de combat).

Chaque face **Drapeau** obtenue par l'attaquant force la cible à reculer d'**1 hexagone**. Il n'y a pas de valeur de Moral : **1 Drapeau = 1 hexagone**, sans exception.

> **[Inébranlable X]** est le seul modificateur : l'unité ignore X Drapeaux par attaque reçue, quelle qu'en soit la source (dés, cartes, sorts).

### 9.2 Direction de la retraite

- **Mêlée :** la cible recule dans la direction **à l'opposé de l'unité attaquante**.
- **Tir :** la cible recule dans la direction **à l'opposé du bord d'hexagone par lequel la ligne de vue a été tracée**.

### 9.3 Obstacles sur le chemin

Le terrain **n'a aucun effet** sur la retraite — une unité la traverse librement, y compris la forêt, le gué et le bâtiment.

Seules deux situations **bloquent** la retraite et infligent **1 touche par hexagone non résolu** :

| Obstacle rencontré | Effet |
|---|---|
| **Forêt, gué, bâtiment, terrain surélevé, pont** | Aucun — retraite continue normalement. |
| **Cours d'eau / bord du plateau** | Bloqué — 1 touche par hexagone non résolu. |
| **Unité ennemie** | Bloqué — 1 touche par hexagone non résolu. |
| **Unité amie** | **Soutien** — tous les hex restants ignorés, 0 touche supplémentaire. |

> 🎲 **Note de design** Alignement sur la règle standard C&C (Memoir '44, C&C Ancients, BattleCry — D091). BLv2 arrêtait la retraite en terrain bloquant, mais c'est une exception dans la famille C&C. BdVM suit la règle majoritaire : seul le terrain impassable bloque.

### 9.4 Après la retraite

Une unité ayant effectué une retraite **ne peut pas contre-attaquer** ce tour.

> 🔗 **Voir aussi** [[BdVM_Terrain]] §10 — Retraites et terrain (tableau complet).

---

## 10. Peur

Certaines unités du Vieux Monde sont si redoutables que leur simple présence fragilise le moral adverse. Ces unités possèdent la règle spéciale **[Peur]**.

Lorsqu'une unité avec **[Peur]** attaque, chaque face **Couronne** obtenue génère **1 Drapeau supplémentaire** (en plus de l'effet normal de la Couronne si applicable). Ces Drapeaux supplémentaires sont ajoutés au total avant la résolution de la retraite.

> 🔗 **Voir aussi** [[BdVM_Regles_Speciales]] — [Peur] et interactions.

---

## 11. Fin de partie

### 11.1 Points de victoire

Chaque **unité ennemie mise en déroute** rapporte **1 point de victoire**. Des points supplémentaires peuvent être accordés par les **médailles objectif** définies dans le scénario (tenir un hexagone clé, franchir une ligne, éliminer une unité spécifique).

### 11.2 Condition de victoire

La partie se termine dès qu'un joueur atteint le **seuil de victoire** défini par le scénario :

| Format | Seuil indicatif |
|---|---|
| **Escarmouche** | 4 points |
| **Bataille** | 6 points |
| **Épique** | 8 points |

---

## Récapitulatif rapide

### Séquence de tour

| Phase | Étape | Action |
|---|---|---|
| **Main Phase** | Command Step | Jouer une carte de commandement |
| | Order Step | Déclarer les unités activées |
| | Move Step | Effectuer les mouvements |
| | Attack Step | Résoudre les combats |
| **Upkeep Phase** | VP Step | Marquer les médailles objectif |
| | Draw Step | Piocher 1 carte |
| | Lore Step | *(inactive en Phase 1.6)* |

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

| Face de dé | Cible Infanterie | Cible Cavalerie | Cible Artillerie / MdG | Cible Créature |
|---|---|---|---|---|
| **Épées croisées** | **2 figurines** | 1 figurine | 1 figurine | 1 figurine |
| **Épée** | 1 figurine | 1 figurine | 1 figurine | 1 figurine |
| **Cible** | **2 figurines** | 1 figurine | 1 figurine | 1 figurine |

> **Exception [Massif] :** les unités Infanterie 25 mm portant cette règle, ainsi que toutes les Créatures, ne subissent que 1 figurine retirée quelle que soit la face.

### Résumé des faces de dés

| Face | Mêlée | Tir |
|---|---|---|
| Épées croisées | 1 ou 2 touches* | Échec |
| Épée | 1 touche (sauf si Faible) | Échec |
| Cible | Échec | 1 ou 2 touches* |
| Drapeau | 1 hex de retraite | 1 hex de retraite |
| Couronne | Capacité spéciale | Capacité spéciale |
| Arcane | Échec *(Phase 2)* | Échec *(Phase 2)* |

*\* 1 touche sur Cavalerie, Artillerie, Créature, Machine de guerre — 2 touches sur Infanterie (sans [Massif]). Voir §2.3.*

### Mémo règles spéciales de base

| Règle | Résumé |
|---|---|
| **Faible** | Dernière figurine : Épée inactive en attaque |
| **[Massif]** | Ignore le bonus 2 dégâts Infanterie — toujours 1 figurine par touche |
| **[Armure X]** | Retire X faces Épée des attaques de mêlée reçues |
| **[Protection X]** | Ignore X touches par attaque (terrain, fortifications) |
| **[Inébranlable X]** | Ignore X résultats de retraite par attaque reçue |
| **[Peur]** | Couronne → Drapeau supplémentaire |
| **[Poursuite X]** | Alternative à l'avance : déplacement + attaque supplémentaire |
| **[Mobilité X]** | Déplacement supplémentaire après l'Attack Step |
| **[Férocité]** | Contre-attaque avant résolution des retraites |
| **[Terrain favori : X]** | Ignore toutes les restrictions de mouvement et de combat du terrain X |

---

> 🔗 **Voir aussi**
> [[BdVM_Regles_Speciales]] — [[BdVM_Terrain]] — [[BdVM_Cartes_Commandement]] — [[BdVM_AideDeJeu]]

---

*Version : 4.3 — Phase 1.6 — 2026-06-01.*
*🔄 Mise à jour Phase 1.6 Étape 6. §9 réécrit (suppression valeur de Moral — D063) ; §7.1 étape 8 reformulée ; récapitulatif Faible et séquence combat mis à jour ; renvoi vers [[BdVM_AideDeJeu]] ajouté.*
*Remplace : BdVM_Regles_Base v4.2 (2026-05-30).*
