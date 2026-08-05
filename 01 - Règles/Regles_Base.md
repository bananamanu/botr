---
projet: "Batailles de la Terre du Milieu"
type: "regles"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-08-05"
tags: [BdTdM, "type/regles", "phase/1", "statut/brouillon"]
version: "0.7"
---

# Batailles de la Terre du Milieu — Règles de base

> Ce document couvre les règles fondamentales de la Phase 1 : structure du tour, types d'unités, mouvement, combat, avance, poursuite et retraite. Les héros, la Peur/Terreur et les monstres avancés sont traités en Phase 2 (voir Document de cadrage §5.2 et §6). **Refonte « taxonomie visuelle » (post-Playtest #2, D059/D060)** : l'identité d'une unité — classe, type, mode — se lit désormais sur son plateau, et les règles en découlent plutôt que d'être mémorisées profil par profil. Les règles spéciales intrinsèques par combinaison sont désormais définies au **§2.4** (revue classe × type, D063) ; le recalcul des coûts suit en P3.

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
- **Dés spéciaux** : 6 faces — Épées croisées / Épée / Cible / Drapeau / Couronne / Arcane (dé BattleLore V2, conservé tel quel)
- **Figurines** : unités des peuples joués (MESBG)
- **Plateaux de mouvement** (movement trays) **colorés par classe** : 🟢 vert (2 dés), 🔵 bleu (3 dés), 🔴 rouge (4 dés) — 4 emplacements pour l'Infanterie, 3 pour la Cavalerie
- **Tokens de mode** collés sur les socles : **mêlée** ou **distance**
- **Marqueurs** : compteurs de PV (Chars et Créatures uniquement), médailles objectif, jetons d'activation/cible (aide-mémoire de contre-attaque, §7.6)

### 2.2 Le langage du socle : classe, type et mode

Toute unité se lit **d'un coup d'œil sur son plateau**, sans consulter de profil. Trois informations y sont portées visuellement.

**La classe = la couleur du plateau = le nombre de dés d'attaque.**

| Couleur | Classe | Dés |
|---|---|---|
| 🟢 **Vert** | Légère | **2** |
| 🔵 **Bleu** | Standard | **3** |
| 🔴 **Rouge** | Lourde / élite | **4** |

**Le type**, donné par la forme du socle et le nombre de figurines :

| Type | Représentation | Pertes suivies par |
|---|---|---|
| **Infanterie** | plateau de **4 figurines** | figurines retirées |
| **Cavalerie** | plateau de **3 figurines** | figurines retirées |
| **Créature / Monstre** | socle unique (65 mm) | **compteur de PV** |
| **Char** | socle unique (65 mm) | **compteur de PV** |

> **Seuls les Chars et les Créatures portent un compteur de PV.** L'Infanterie et la Cavalerie n'ont pas de PV chiffré : on retire simplement leurs figurines du plateau (1 figurine = 1 « point de vie » implicite).

**Le mode = un token collé sur le socle : mêlée ou distance.** Il indique quelles faces de dé l'unité lit lorsqu'elle attaque (voir §2.3 et §7) : **mêlée → Épées croisées + Épée** · **distance → Cible**.

Une unité occupe toujours **un seul hexagone**. Les touches s'accumulent au sein d'une même attaque ; les pertes ne se récupèrent pas.

#### Déroute

Lorsqu'une unité perd sa **dernière figurine** (ou son dernier PV, pour un Char ou une Créature), elle est **en déroute** : retirez-la du champ de bataille. L'adversaire marque **1 point de victoire**, sauf indication contraire du scénario.

#### Unité Faible

Une unité d'**Infanterie** ou de **Cavalerie** est **Faible** lorsqu'il ne lui reste qu'**une seule figurine**. Elle subit alors l'effet suivant :

- Ses faces **Épée** ne causent aucune touche en mêlée (seules les **Épées croisées** comptent).

> Les Chars et Créatures, suivis en PV, **ne passent pas par l'état Faible** ; leur profil définit d'éventuels seuils (ex. Furie du Mûmakil).

> 💡 **Exemple de jeu**
> Des Piquiers réduits à 1 figurine (Faibles) attaquent en mêlée : les faces Épée n'infligent rien, seules les Épées croisées touchent.

### 2.3 Attaque et dégâts

Une unité attaque en lançant un nombre de dés égal à sa **classe** (couleur) : 2 (🟢), 3 (🔵) ou 4 (🔴), modifié le cas échéant par le terrain (§7.5) ou une capacité.

**Quelles faces touchent dépend du mode de l'unité** (son token) :

| Mode | Faces qui touchent | Spéciale | Retraite |
|---|---|---|---|
| **Mêlée** | Épées croisées · Épée¹ | Couronne² | Drapeau |
| **Distance** | Cible | Couronne² | Drapeau |

*¹ Épée inactive si l'unité est Faible. — ² La Couronne déclenche la règle signature de l'unité, si elle en a une. La face **Arcane** est un échec (réservée à [Peur] et à la couche Leadership, Phase 2).*

**Règle de dégâts — unique et universelle :**

> **Chaque touche retire exactement 1 figurine — ou 1 PV pour un Char / une Créature — quelle que soit la cible.** Une touche ne retire jamais plus qu'il ne reste.

Il n'y a **plus** de dégâts variables selon le type de cible (la double-touche contre l'infanterie est supprimée, D059/D060). La durabilité d'une unité découle directement de son nombre de figurines/PV — **Infanterie 4, Cavalerie 3** (ratio 1,33, socle sur lequel repose le chiffrage des points, voir [[Regles_Points]]). Cette règle unique vaut aussi pour les touches « hors face » (Couronne convertie en touche, [Poison], recul bloqué, piétinement du Mûmakil…) : **1 touche = 1 figurine/PV**, sans exception.

> 💡 **Exemple de jeu**
> Des Chevaliers (Cavalerie, 🔴 4 dés, mêlée) chargent des Épéistes (Infanterie, mêlée) : 4 dés → Épées croisées, Épée, Épée, Drapeau = **3 touches** (3 figurines retirées) **+ 1 Drapeau** (1 hexagone de recul).

#### Types particuliers

Les **Chars** (ex. Aurige de Khand) et les **Créatures** (Mûmakil, Troll) occupent 1 hexagone sur socle 65 mm et se comptent en **PV**. Leur mouvement et leurs règles sont propres à leur profil (pièces signatures), hors de la grille standard (§6.1).

> **Artillerie / Machine de guerre : hors périmètre de la v1.** Non utilisée au Pelennor ; ses règles sont mises de côté et pourront être réactivées ultérieurement si un scénario l'exige.

### 2.4 Règles intrinsèques par combinaison (classe × type × mode)

Certaines règles spéciales ne se notent **pas** sur le profil : elles découlent directement de la **classe** (couleur), du **type** (socle) et du **mode** (token), et se lisent d'un coup d'œil au plateau. Une unité applique **toutes** les intrinsèques de sa case. Un profil ne mentionne une valeur que s'il **dépasse** le plancher intrinsèque (ex. [Armure 2]) ou porte en plus une **signature** (voir [[Regles_Speciales]]).

| Type + mode | 🟢 Légère (2 dés) | 🔵 Standard (3 dés) | 🔴 Lourde (4 dés) |
|---|---|---|---|
| **Infanterie — mêlée** | — | — | **[Armure 1]** |
| **Infanterie — distance** | **[Mobilité 1]** | — | *(n'existe pas)* |
| **Cavalerie — mêlée** | **[Poursuite 2]** | **[Poursuite 2]** | **[Poursuite 1]** + **[Armure 1]** |
| **Cavalerie — distance** | **[Mobilité 2]** | **[Mobilité 1]** | *(n'existe pas)* |

Trois lignes de force, toutes lisibles à la couleur ou au socle :

- **Rouge = fortement armuré.** Toute unité lourde (🔴), à pied ou montée, porte **[Armure 1]** d'office : elle retire 1 face Épée des attaques de mêlée subies. C'est le **plancher** — un profil peut monter à [Armure 2] (Cataphractaires orientaux, lourds du Gondor), et la valeur du profil prime alors.
- **Cavalerie de mêlée = elle enfonce et poursuit.** Après avoir éliminé ou fait reculer une cible adjacente, elle peut **poursuivre** (§8.2) au lieu d'avancer : **[Poursuite 2]** pour la légère et la standard (plus mobiles), **[Poursuite 1]** pour la lourde (qui traîne son armure). C'est la mécanique de percée du choc de cavalerie.
- **Tir léger ou monté = harceleur mobile.** En mode distance, l'unité décroche après avoir tiré ([Mobilité X] : déplacement de X hexagones **après l'étape d'attaque**, §6) : **[Mobilité 2]** pour la cavalerie légère (la plus insaisissable), **[Mobilité 1]** pour la cavalerie standard et l'infanterie légère. L'**archer à pied standard (🔵) ne décroche pas** — c'est l'archer de ligne « planté » (la base), miroir de la signature [Double Tir] de l'Easterling (l'archer immobile qui double la salve).

> **Cases vides et cases absentes.** Un tiret « — » signifie *aucune intrinsèque* : l'unité est définie par ses seuls dés et son éventuelle signature. L'**infanterie de tir lourde** et la **cavalerie de tir lourde** *n'existent pas* dans le jeu (aucune combinaison 🔴 + distance) — un archer d'élite est une unité 🔵 portant une signature ou [Arme Lourde X] au profil, jamais une unité rouge.

> 💡 **Exemple de jeu**
> Des Chevaliers (Cavalerie 🔴, mêlée) enfoncent des Orques : lourds, ils portent **[Armure 1]** en défense et **[Poursuite 1]** — après avoir fait reculer les Orques, ils avancent d'1 hexagone et frappent une seconde cible adjacente. Un Éored du Rohan (Cavalerie 🔵) à leur place disposerait de **[Poursuite 2]** (jusqu'à 2 hexagones).

> 🔗 Définitions complètes des mots-clés : [[Regles_Speciales]] (socle générique). Ces règles se lisent au plateau et **ne sont jamais réécrites sur le profil** tant que celui-ci ne dépasse pas le plancher.

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

### 6.1 Mouvement par classe et type

Le mouvement se lit **directement sur le plateau** (couleur + type), sans profil — inspiré de *C&C Medieval*. Principe : plus une unité frappe fort (rouge), moins elle est mobile ; les unités lourdes doivent choisir entre **bouger** et **frapper**.

| | 🟢 Verte (2 dés) | 🔵 Bleue (3 dés) | 🔴 Rouge (4 dés) |
|---|---|---|---|
| **Infanterie** | 2 cases + combat | 2 cases + combat | 1 case + combat, **ou** 2 cases |
| **Cavalerie** | 4 cases + combat | 3 cases + combat | 2 cases + combat, **ou** 3 cases |

- « **X cases + combat** » : l'unité peut se déplacer jusqu'à X hexagones **puis** attaquer.
- « **ou Y cases** » (unités rouges) : alternativement, elle **renonce à attaquer** pour se déplacer de Y hexagones.

> **Règles intrinsèques liées au mouvement.** Plusieurs cases de la grille classe × type × mode portent des règles qui se lisent au plateau (voir §2.4) : **[Mobilité X]** — le tir léger ou monté décroche de X hexagones après avoir tiré — et **[Poursuite X]** — la cavalerie de mêlée enfonce puis frappe une seconde cible (§8.2). Elles ne se notent pas sur le profil.

**Créatures et Chars** conservent une valeur de mouvement **propre à leur profil** (pièces signatures) et ne suivent pas cette grille — le Mûmakil, par exemple, a son déplacement dédié (translation 1-2-1).

> Une unité peut toujours se déplacer de moins que son maximum, ou ne pas bouger.

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

Une unité en **mode mêlée** (token mêlée) peut attaquer une **unité ennemie adjacente** (dans l'un des 6 hexagones voisins).

Les faces actives en mêlée sont :
- **Épées croisées** : touche inconditionnelle
- **Épée** : touche — **inactive si l'unité est Faible**
- **Drapeau** : retraite
- **Couronne** : capacité spéciale (si profil)
- **Cible** et **Arcane** : échec en mêlée

### 7.3 Attaque de tir

Une unité en **mode distance** (token distance) peut attaquer une unité ennemie **à portée et en ligne de vue**. Elle peut également attaquer une unité **adjacente** (en utilisant la face Cible comme si c'était du tir).

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

> ⚠️ **Rappel — Dégâts :** chaque touche retire **1 figurine/PV**, quelle que soit la cible (§2.3).

### 7.6 Contre-attaque

Après avoir subi une attaque et résolu toutes les retraites, l'unité ciblée peut **contre-attaquer** si les trois conditions suivantes sont réunies :

- Elle est **adjacente** à l'attaquant.
- Elle est **restée dans le même hexagone** (aucune retraite effectuée).
- Elle **n'a pas été éliminée**.

La contre-attaque est **universelle** — toute unité peut contre-attaquer sans règle spéciale. Elle s'effectue à la valeur d'attaque complète selon la séquence normale (étapes 1 à 8 uniquement — pas d'avance ni de nouvelle contre-attaque).

> 🔄 **Convention de jeu recommandée — Playtest #1b (2026-07-27, D052)** : la contre-attaque universelle est la règle la plus oubliée à la table (constat du Playtest #1, D042). Dispositif validé pour y remédier, en particulier pour la table à 6 joueurs : poser un **jeton d'activation** sur chaque unité du camp actif au moment où elle joue, et un **jeton de cible** sur toute unité adverse qui subit une attaque et survit. Le jeton de cible rappelle qu'une contre-attaque est due ; il est retiré une fois celle-ci résolue. Testé avec succès au Playtest #1b — plus aucun oubli signalé. À intégrer à l'aide de jeu convention.

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

### 9.2 Direction de la retraite (recul façon Memoir '44)

Quelle que soit la source de l'attaque (mêlée ou tir), la cible recule **toujours vers le bord de plateau de son propre camp** (celui depuis lequel elle a été déployée) — la direction ne dépend ni de la position de l'attaquant, ni de l'angle de tir.

- Pour chaque hexagone de recul, **le joueur qui recule choisit** un hexagone voisin **strictement plus proche de son bord** que l'hexagone actuel (mesuré en nombre d'hexagones jusqu'au bord). S'il existe plusieurs hexagones valables à égale distance, il choisit librement parmi eux.
- S'il n'existe **aucun** hexagone valable (l'unité est déjà sur son propre bord, ou tous les hexagones plus proches sont bloqués), ce hexagone de recul est **bloqué** — voir §9.3.

> 💡 **Exemple de jeu**
> Une unité du Rohan (déployée au sud) subit 2 Drapeaux, peu importe que l'attaque vienne de face, de flanc ou par une volée de tir en biais : elle recule de 2 hexagones vers le bord sud, en choisissant à chaque étape l'hexagone libre le plus proche de ce bord.

> 🔄 **Modifié après playtest — 2026-07-25 (Playtest #1, D041)**
> Adoption du recul façon *Memoir '44* (toujours vers le bord ami), en remplacement de la retraite directionnelle C&C classique (opposée à l'attaquant en mêlée, opposée à la ligne de vue au tir). Joué ainsi à la table et retenu : bien plus simple et mémorisable (principe 1 du [[Document de cadrage]]) — l'ancienne résolution était jugée « compliquée ou absurde à appliquer », en particulier pour arbitrer la direction exacte d'un tir en angle. Le nombre d'hexagones de recul (1 Drapeau = 1 hex) et les règles de blocage (§9.3) restent inchangés.

### 9.3 Obstacles sur le chemin

Le terrain **n'a aucun effet** sur la retraite — une unité la traverse librement, y compris la forêt, le gué et le bâtiment.

Seules deux situations **bloquent** la retraite et infligent **1 touche par hexagone non résolu** :

| Obstacle rencontré | Effet |
|---|---|
| Forêt, gué, bâtiment, terrain surélevé, pont | Aucun — retraite continue normalement. |
| Sortie du plateau (l'unité est déjà sur son propre bord et devrait en sortir) | Bloqué — 1 touche par hexagone non résolu. |
| Cours d'eau infranchissable, ou aucun hexagone valable disponible (encerclement) | Bloqué — 1 touche par hexagone non résolu. |
| Unité ennemie occupant le seul hexagone valable | Bloqué — 1 touche par hexagone non résolu. |
| Unité amie occupant le seul hexagone valable | **Soutien** — tous les hex restants ignorés, 0 touche supplémentaire. |

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
7. Retirer **1 figurine/PV par touche** (§2.3)
8. Résoudre la retraite (1 Drapeau = 1 hex · [Inébranlable X] si applicable)
9. Contre-attaque si conditions réunies
10. Avance si cible éliminée ou en retraite

### Dégâts

**1 touche = 1 figurine retirée** (ou 1 PV pour un Char / une Créature), **quelle que soit la cible**. Jamais plus qu'il ne reste.

### Résumé des faces de dés

| Face | Mode mêlée | Mode distance |
|---|---|---|
| Épées croisées | 1 touche | Échec |
| Épée | 1 touche (sauf si Faible) | Échec |
| Cible | Échec | 1 touche |
| Drapeau | 1 hex de retraite | 1 hex de retraite |
| Couronne | Règle signature (si profil) | Règle signature (si profil) |
| Arcane | Échec (réservée [Peur]/Leadership, Phase 2) | Échec (réservée [Peur]/Leadership, Phase 2) |

*Le **mode** (token mêlée/distance) détermine quelles faces l'unité lit. Chaque touche retire **1 figurine/PV** (§2.3).*

### Mémo règles spéciales de base

| Règle | Résumé |
|---|---|
| **Faible** | Dernière figurine : Épée inactive en attaque |
| **[Armure X]** | Retire X faces Épée des attaques de mêlée reçues |
| **[Protection X]** | Ignore X touches par attaque (terrain, fortifications) |
| **[Inébranlable X]** | Ignore X résultats de retraite par attaque reçue |
| **[Poursuite X]** | Alternative à l'avance : déplacement + attaque supplémentaire |
| **[Mobilité X]** | Déplacement supplémentaire après l'étape d'attaque |
| **[Férocité]** | Contre-attaque même en cas de recul forcé, puis recule normalement |

> Les règles **[Armure X]**, **[Mobilité X]** et **[Poursuite X]** sont pour partie **intrinsèques** : elles sont attachées à une case de la grille §2.4 et se lisent au plateau. Un profil ne les réécrit que s'il **dépasse** le plancher intrinsèque.

---

## Points ouverts de ce document

| # | Sujet | Renvoi |
|---|---|---|
| 1 | Seuils de victoire par format, à revalider au playtest de la taxonomie | §10.2 / P7a |
| 2 | Répartition des cartes et ordre de jeu à 3 joueurs par camp (format Épique) | §5.5 |
| 3 | Recalcul des coûts sur la nouvelle base (durabilité 4:3, archerie affaiblie, **intrinsèques par case §2.4**, passage en matrice) | P3 |
| 4 | Mouvement et PV des **Créatures / Chars** (hors grille) à confirmer profil par profil | P4 / P5 |

> ✅ **Résolus par la revue classe × type (2026-08-05, D063)** : les règles spéciales **intrinsèques par combinaison** (ex-#3) et les **bonus intrinsèques par classe/type** (ex-#5, jadis écartés) sont désormais définis au **§2.4**.

---

*Version : 0.2 — Phase 1 — 2026-07-18. [Massif] retirée, commandement/terrain Pelennor clarifiés. Non testé.*

*Version : 0.3 — Phase 1 — 2026-07-25. **Mise à jour post-Playtest #1** (D041, `[[Playtest1_Compte-rendu]]`) : §9.2 réécrite — recul façon Memoir '44 (toujours vers le bord ami, le joueur qui recule choisit l'hexagone) en remplacement de la retraite directionnelle C&C. §9.3 (obstacles) reformulée en conséquence.*

*Version : 0.5 — Phase 1 — 2026-07-28. Correction du récapitulatif : [Férocité] permet à l'unité de contre-attaquer même forcée de reculer (elle recule ensuite normalement), et non « avant les retraites adverses » comme écrit précédemment (D057, voir [[Regles_Speciales]]).*

*Version : 0.6 — Phase 1 — 2026-08-03. **Refonte P1 « taxonomie visuelle » (D059/D060).** §2.1 (plateaux colorés, tokens de mode, compteurs de PV). §2.2 réécrite — classe (couleur = dés 2/3/4), type (Inf 4 fig / Cav 3 fig ; Chars et Créatures = PV), mode (token mêlée/distance) ; Faible limitée à Inf/Cav. §2.3 réécrite — **suppression de la double-touche** : règle unique « 1 touche = 1 figurine/PV, quelle que soit la cible » ; Artillerie mise hors périmètre v1. §6.1 réécrite — **grille de mouvement par classe × type** (inspirée C&C Medieval) ; aucune règle spéciale attachée d'office à une classe/type (les bonus intrinsèques éventuels — mobilité légère, double tir léger — sont écartés pour l'instant, décision reportée à P2) ; Créatures/Chars hors grille. §7.2/7.3 rattachées au token de mode ; récapitulatifs et rappels alignés. Reste à peupler en P2 (règles intrinsèques par combo) et à recalculer en P3 (coûts). Non testé — validation en P7a.*

*Version : 0.7 — Phase 1 — 2026-08-05. **Revue classe × type (D063).** Ajout du §2.4 « Règles intrinsèques par combinaison » : grille classe × type × mode peuplée. **[Armure 1]** intrinsèque à tout lourd 🔴 (plancher, un profil peut monter à [Armure 2]) ; **[Poursuite]** intrinsèque à la cavalerie de mêlée (2 pour 🟢/🔵, 1 pour 🔴) ; **[Mobilité]** intrinsèque au tir léger/monté (🟢 cavalerie 2 ; 🟢 infanterie et 🔵 cavalerie 1 ; 🔵 infanterie = rien, archer de ligne planté). Infanterie et cavalerie de tir lourdes actées inexistantes. Supersession de D062-6 (la [Poursuite] cavalerie était renvoyée au profil). §6.1 et le mémo renvoient au §2.4 ; points ouverts #3 et #5 fermés. Répercussions profils/coûts renvoyées à P3 (chiffrage par case) / P4 (nettoyage des redondances). Non testé — validation en P7a.*
