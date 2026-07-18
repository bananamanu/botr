---
projet: "Batailles du Vieux Monde"
type: "composant"
phase: "1.5"
statut: "en-cours"
date_maj: "2026-05-09"
tags: [BdVM, "type/composant", "phase/1.5", "statut/en-cours"]
---

# Batailles du Vieux Monde — Cartes de commandement

> Ce document définit le système de cartes de commandement, la composition des decks par format de bataille, et le protocole de constitution du deck en début de partie. Les cartes spécifiques aux factions sont traitées en Phase 3.
>
> Le deck de base est adapté de **BattleLore V1** (Days of Wonder, 2006), dont les cartes de commandement constituent le socle mécanique. Les cartes à système de Bannières (Blue/Green/Red Banners, BattleLore V1) sont écartées — leur équivalent BdVM est différé en Phase 3. Les cartes inventées spécifiquement pour une première version de BdVM (Tir d'artillerie, Repli tactique, Terrain connu, Ralliement, Double ordre) sont retirées.

> 🔄 **Modifié — 2026-05-09 | Phase 1.5 Étape 6**
> Harmonisation avec la base mécanique BLv2 (voir `BdVM_Analyse_BLv2.md`).
> - Suppression des textes alternatifs "si vous n'avez aucune unité de [type]" sur Charge de cavalerie, Assaut d'infanterie et Pluie de flèches : ces cas limites sont gérés par les règles générales.
> - Suppression de la référence aux bannières de couleur dans Charge de cavalerie (point ouvert #4 tranché — système de bannières écarté en Phase 1.5).
> - Arcanes de guerre : effet complet rédigé et validé. Faces Épée et Épées croisées → unités de mêlée ; face Cible → unités à distance ; face Couronne → unité libre (point ouvert #3 tranché).
> - Bonus offensifs doublés sur Charge de cavalerie, Ordre direct et Arcanes de guerre : +1 dé → **+2 dés** (décision D038).
> - Clarification terminologique : la carte "Contre-attaque" est distincte de la règle universelle de contre-attaque BLv2.

---

## Table des matières

1. [[#1. Principes généraux]]
2. [[#2. Anatomie d'une carte]]
3. [[#3. Les formats de bataille et leurs decks]]
4. [[#4. Composition détaillée du deck]]
5. [[#5. Protocole de constitution du deck]]
6. [[#6. Évolution en Phase 3 — cartes de faction]]

---

## 1. Principes généraux

Le deck de commandement est le **moteur de tension** du jeu. Il conditionne quelles unités peuvent agir à chaque tour, forçant les joueurs à des choix permanents entre opportunité et priorité.

### 1.1 Un deck calibré par format

Le nombre et la nature des cartes sont directement liés à la taille du plateau. La règle de calibrage est la suivante :

> **Le deck doit permettre d'activer en moyenne entre 1/3 et 1/2 des unités d'une armée par tour, quel que soit le format.**

Un deck trop généreux rend chaque tour prévisible. Un deck trop restrictif paralyse les joueurs. Le calibrage par format maintient cet équilibre sur des plateaux de tailles différentes.

### 1.2 La valeur de commandement

Plusieurs cartes activent un nombre d'unités **égal à la valeur de commandement** du joueur, c'est-à-dire le nombre de cartes qu'il a en main au moment où il joue la carte (cette carte comprise).

En Phase 1.5, la valeur de commandement est fixée par le format (voir §3). En Phase 2+, elle sera déterminée par la formule suivante : **3 + valeur du meilleur héros vivant** (valeur de héros : 1 à 3). Elle est réévaluée immédiatement à chaque mort de héros. Ce double rôle — cartes en main et unités activables — crée une tension tactique autour des héros sans les rendre indispensables (une valeur de base de 3 reste fonctionnelle).

> 💡 **Exemple de jeu**
> Un joueur joue "Percée Gauche" avec 4 cartes en main (dont "Percée Gauche" elle-même). Sa valeur de commandement est 4 : il peut activer jusqu'à 4 unités dans la section gauche.

### 1.3 Deck partagé en Phase 1.5

En Phase 1.5, les deux joueurs puisent dans un **deck commun unique**, sans cartes de faction. Chacun constitue sa main en début de partie (voir §5).

> 🔗 **Voir aussi** [[BdVM_Cartes_Commandement#6. Évolution en Phase 3 — cartes de faction]]

---

## 2. Anatomie d'une carte

Chaque carte de commandement comporte les informations suivantes, du haut vers le bas :

```
┌─────────────────────────────┐  ← 63 × 88 mm (standard poker)
│  zone de sécurité : 3 mm   │  ← zone utile : 57 × 82 mm
│ ┌─────────────────────────┐ │
│ │   NOM DE LA CARTE       │ │  ← ① Bandeau nom
│ │   type de carte         │ │     Police médiévale (UnifrakturMaguntia)
│ └─────────────────────────┘ │     Taille adaptée à la longueur du titre
│                             │
│  [ G ]  [ C ]  [ D ]        │  ← ② Pictogramme
│   (section active grisée)   │     Cartes de section : plateau schématique 3 bandes
│                             │     Cartes Tactiques : icône propre au type d'effet
│ ┌─────────────────────────┐ │
│ │  Texte de règle         │ │  ← ③ Zone de règle
│ │  (9.5 px, adapté si     │ │     Fond gris léger
│ │   texte long → 8.5 px)  │ │     Note secondaire sous trait de séparation
│ └─────────────────────────┘ │
│                       [E·B] │  ← ④ Pastille format (bas droite)
└─────────────────────────────┘     E = Escarmouche / B = Bataille / E·B = les deux
```

- **① Bandeau nom** : titre de la carte en police UnifrakturMaguntia. Taille variable selon longueur : 18 px (court), 14 px (moyen), 11 px (long). Étiquette de type en dessous (8.5 px, capitales, discret).
- **② Pictogramme** : pour les cartes de section, trois bandes verticales représentant G / C / D — la section active en gris soutenu, les sections inactives en gris très léger. Pour les cartes Tactiques, icône propre à l'effet (silhouettes, flèches, etc.). Zone Phase 4 : remplacée par une illustration.
- **③ Zone de règle** : texte de la règle en 9.5 px (8.5 px si volume important). Fond gris léger. Une note secondaire optionnelle est séparée par un trait fin (cas limite, interaction avec une règle spéciale, etc.).
- **④ Pastille format** : coin bas droit, hors zone de règle. Indique le(s) deck(s) dans lesquels la carte est incluse.

> 🔄 **Modifié — 2026-04-08**
> Gabarit Playtest défini. Suppression du récapitulatif en pied de carte (section / nb unités / deck). La pastille format migre en bas à droite. Ajout du pictogramme plateau schématique pour les cartes de section. Police médiévale (UnifrakturMaguntia) retenue pour le bandeau nom. Direction artistique finale réservée à la Phase 4.

> ⚠️ **Point ouvert**
> Le format physique des cartes est fixé à 63 × 88 mm (standard poker). La direction artistique finale (illustrations, couleurs par type de carte, ornements) est réservée à la Phase 4.

---

## 3. Les formats de bataille et leurs decks

### 3.1 Vue d'ensemble

| Format | Plateau | Sections | Main de départ | Taille du deck |
|---|---|---|---|---|
| **Bataille** | 13 × 9 | 3 (G / C / D) | 5 cartes | 60 cartes |
| **Escarmouche** | 10 × 7 | 3 (G / C / D) | 4 cartes | 43 cartes |
| **Épique** | 26 × 9 | _Point ouvert_ | _À définir_ | _À définir_ |

> ⚠️ **Point ouvert**
> Le format Épique est réservé à une décision ultérieure, après les Playtests #1 et #2.

### 3.2 Logique de différenciation des decks

Le deck Escarmouche est un **sous-ensemble strict** du deck Bataille. On retire les cartes qui activeraient proportionnellement trop d'unités sur un plateau 10×7 et réduiraient la tension tactique :

- Les **Attaque** (G / C / D) : 3 unités par section — trop fort sur un front réduit. **−15 cartes.**
- Les **En avant** : 2 unités dans chaque section, soit 6 activations — disproportionné. **−2 cartes.**

**Total retiré : 17 cartes. Deck Escarmouche : 43 cartes.**

Toutes les autres cartes, y compris les Percées (activation variable selon la main), sont conservées. Sur un plateau réduit avec une main de 4 cartes, la valeur de commandement est naturellement plus basse qu'en Bataille, ce qui calibre automatiquement leur puissance.

### 3.3 La valeur de commandement par format

La main de départ détermine la valeur de commandement de base pour les cartes à activation variable :

- **Bataille** : main de 5 cartes → valeur de commandement de départ = 5
- **Escarmouche** : main de 4 cartes → valeur de commandement de départ = 4

La valeur de commandement fluctue en cours de partie selon les cartes jouées et piochées, ce qui crée une tension dynamique : jouer une carte réduit temporairement la valeur de commandement avant que la pioche ne la rétablisse.

---

## 4. Composition détaillée du deck

### 4.1 Catégories de cartes

Les cartes se répartissent en deux catégories :

**A — Cartes de section** : activent un nombre défini d'unités dans une ou plusieurs sections du champ de bataille.

**B — Cartes tactiques** : activent des unités selon leur **type** (cavalerie, infanterie, unités à distance) plutôt que leur position, ou produisent des effets spéciaux.

---

### 4.2 Deck Bataille — 60 cartes

#### Cartes de section (48 cartes)

Ces cartes activent des unités selon leur position sur le plateau.

**Éclaireur** — Section unique, 1 unité + avantage de pioche _(6 cartes — présentes en Escarmouche)_

| Carte | Nb | Effet |
|---|---|---|
| Éclaireur Gauche | 2 | Activez 1 unité dans la section gauche. Au lieu de piocher normalement en fin de tour, piochez 2 cartes et défaussez-en 1. |
| Éclaireur Centre | 2 | Activez 1 unité dans la section centrale. Au lieu de piocher normalement en fin de tour, piochez 2 cartes et défaussez-en 1. |
| Éclaireur Droite | 2 | Activez 1 unité dans la section droite. Au lieu de piocher normalement en fin de tour, piochez 2 cartes et défaussez-en 1. |

**Patrouille** — Section unique, 2 unités _(15 cartes — présentes en Escarmouche)_

| Carte | Nb | Effet |
|---|---|---|
| Patrouille Gauche | 5 | Activez 2 unités dans la section gauche. |
| Patrouille Centre | 5 | Activez 2 unités dans la section centrale. |
| Patrouille Droite | 5 | Activez 2 unités dans la section droite. |

**Attaque** — Section unique, 3 unités _(15 cartes — **absentes du deck Escarmouche**)_

| Carte | Nb | Effet |
|---|---|---|
| Attaque Gauche | 5 | Activez 3 unités dans la section gauche. |
| Attaque Centre | 5 | Activez 3 unités dans la section centrale. |
| Attaque Droite | 5 | Activez 3 unités dans la section droite. |

**Percée** — Section unique, activation variable _(6 cartes — présentes en Escarmouche)_

| Carte | Nb | Effet |
|---|---|---|
| Percée Gauche | 2 | Activez dans la section gauche autant d'unités que votre valeur de commandement. |
| Percée Centre | 2 | Activez dans la section centrale autant d'unités que votre valeur de commandement. |
| Percée Droite | 2 | Activez dans la section droite autant d'unités que votre valeur de commandement. |

**Cartes multi-sections** _(6 cartes)_

| Carte | Nb | Escarmouche | Effet |
|---|---|---|---|
| En marche | 2 | ✅ | Activez 1 unité dans chaque section. |
| En avant | 2 | ❌ | Activez 2 unités dans chaque section. |
| Encerclement | 2 | ✅ | Activez 2 unités dans la section gauche et 2 unités dans la section droite. |

---

#### Cartes tactiques (12 cartes — toutes présentes en Escarmouche)

Ces cartes activent des unités selon leur type ou produisent des effets spéciaux.

> ⚠️ **Note terminologique**
> La carte "Contre-attaque" décrite ci-dessous est une **carte de commandement** jouée volontairement depuis la main. Elle est distincte de la **règle universelle de contre-attaque** (réaction automatique disponible pour toute unité survivante après avoir subi une attaque au corps-à-corps). Voir [[BdVM_Regles_Base §7]].

| Carte | Nb | Effet |
|---|---|---|
| Charge de cavalerie | 3 | Activez autant d'unités de Cavalerie que votre valeur de commandement, dans n'importe quelle section. Toutes les unités activées combattent à **+2 dés** en mêlée. Elles ne peuvent pas tirer à distance. |
| Assaut d'infanterie | 2 | Activez autant d'unités d'Infanterie que votre valeur de commandement, dans n'importe quelle section. Ces unités doivent être adjacentes entre elles, formant un groupe continu. Elles peuvent se déplacer de 2 hexagones et combattre en mêlée. Elles ne peuvent pas tirer à distance. |
| Pluie de flèches | 2 | Activez toutes vos unités capables de tirer à distance, dans n'importe quelle section. Ces unités tirent deux fois ce tour, mais ne peuvent pas se déplacer ni tirer à bout portant. |
| Ordre direct | 2 | Activez 1 unité de votre choix, dans n'importe quelle section. Cette unité combat à **+2 dés** pour toute la durée du tour. |
| Contre-attaque | 2 | Jouez cette carte en réponse à la carte que vient de jouer votre adversaire. Vous exécutez le même ordre que lui : si c'est une carte de section, la section gauche devient la droite et vice-versa. Si c'est une carte tactique, appliquez l'effet identique. |
| Arcanes de guerre | 1 | Lancez autant de dés de bataille que votre valeur de commandement. Pour chaque face **Épée** ou **Épées croisées** obtenue, activez 1 unité de mêlée de votre choix. Pour chaque face **Cible** obtenue, activez 1 unité à distance de votre choix. Pour chaque face **Couronne** obtenue, activez 1 unité de votre choix. Toutes les unités ainsi activées combattent à **+2 dés** pour ce tour. Puis mélangez la défausse avec la pioche. |

> 🎲 **Note de design — Arcanes de guerre**
> La carte utilise les faces des dés BdVM comme mécanisme de sélection d'unités : Épée et Épées croisées → mêlée, Cible → distance, Couronne → libre. Les faces Drapeau et Arcane n'activent aucune unité. La pioche est mélangée immédiatement, quel que soit le résultat des dés.

> 🔄 **Modifié — 2026-04-24 | Playtest #01**
> Bonus offensifs doublés : +1 dé → +2 dés sur Charge de cavalerie, Ordre direct et Arcanes de guerre (décision D038). Le +1 dé s'avérait trop faible avec le système de dés BdVM (probabilité de touche trop basse pour être significative).

---

### 4.3 Récapitulatif comparatif

| Catégorie | Bataille (60) | Escarmouche (43) |
|---|---|---|
| Éclaireur (G / C / D) | 6 | 6 |
| Patrouille (G / C / D) | 15 | 15 |
| **Attaque (G / C / D)** | **15** | **—** |
| Percée (G / C / D) | 6 | 6 |
| En marche | 2 | 2 |
| **En avant** | **2** | **—** |
| Encerclement | 2 | 2 |
| Charge de cavalerie | 3 | 3 |
| Assaut d'infanterie | 2 | 2 |
| Pluie de flèches | 2 | 2 |
| Ordre direct | 2 | 2 |
| Contre-attaque | 2 | 2 |
| Arcanes de guerre | 1 | 1 |
| **Total** | **60** | **43** |

---

## 5. Protocole de constitution du deck

### 5.1 Avant chaque partie

1. **Choisir le format** de la bataille.
2. **Prendre le deck correspondant**, déjà constitué et maintenu séparé de l'autre deck.
3. **Mélanger le deck** à la vue des deux joueurs.
4. **Chaque joueur pioche** le nombre de cartes de départ indiqué par le format (5 en Bataille, 4 en Escarmouche) pour constituer sa main secrète.
5. Le reste du deck forme la **pioche centrale**, placée face cachée entre les joueurs.

### 5.2 Gestion de la pioche en cours de partie

- Après avoir joué une carte, le joueur actif la défausse face visible à côté de la pioche, puis **pioche 1 carte** pour ramener sa main au nombre initial — sauf s'il a joué un Éclaireur (voir §4.2).
- Si la pioche est épuisée, **mélanger la défausse** pour former une nouvelle pioche. Exception : la carte "Arcanes de guerre" déclenche ce mélange immédiatement après résolution.

### 5.3 Main minimale

Si un joueur se retrouve sans carte en main en début de son tour (situation rare mais possible en fin de pioche), il pioche immédiatement **2 cartes** avant de jouer.

> 💡 **Exemple de jeu**
> Début de partie en format Bataille. Le joueur Empire pioche 5 cartes : Patrouille Centre, Charge de cavalerie, Attaque Droite, Éclaireur Gauche, En marche. Sa valeur de commandement est 5. Il joue "Charge de cavalerie" et peut activer jusqu'à 5 unités de cavalerie sur tout le plateau, chacune avec +2 dés en mêlée. Il défausse la carte, pioche 1 carte, et sa main revient à 5.

---

## 6. Évolution en Phase 3 — cartes de faction

En Phase 3, chaque faction dispose d'un **supplément de cartes** qui s'intègre au deck de base selon la règle suivante :

> Pour chaque carte de faction ajoutée au deck, **une carte générique de même catégorie** est retirée.

Le deck garde ainsi une taille constante par format. L'identité tactique de la faction est renforcée sans déséquilibrer le volume d'activations disponibles.

_Exemple (non définitif) :_

- L'Empire ajoute 3 cartes "Artillerie de l'Empire" → retire 3 "Patrouille" génériques.
- Les Hommes-Lézards ajoutent 3 cartes "Rites anciens des Slanns" → retire 3 "En marche".

En Phase 2+, la **valeur de commandement** évoluera avec le système de héros : elle sera de **3 + valeur du meilleur héros vivant**, ce qui augmentera naturellement la puissance des cartes à activation variable au fur et à mesure que les héros plus puissants sont engagés.

> ⚠️ **Point ouvert**
> Le nombre exact de cartes de faction par armée et le mécanisme d'échange (libre ou imposé par catégorie ?) sont à définir lors de la Phase 3.

---

## Annexe A — Points ouverts

| # | Sujet | Décision requise |
|---|---|---|
| 1 | Composition du deck Escarmouche | ✅ Défini : retrait des Attaque et En avant (−17 cartes, 43 cartes au total) |
| 2 | Découpage des sections et deck Épique | Après Playtest #2 |
| 3 | Arcanes de guerre — effet complet (faces de dés) | ✅ Tranché : Épée + Épées croisées → mêlée, Cible → distance, Couronne → libre, Drapeau + Arcane → aucune activation |
| 4 | Bannières de couleur BLv2 (Charge de cavalerie) | ✅ Écarté en Phase 1.5 : toutes les unités de cavalerie sont traitées identiquement. À reconsidérer en Phase 3 si nécessaire. |
| 5 | Cartes de faction et Conseil de Guerre | Phase 3 |
| 6 | Équivalent des cartes Bannières V1 (Blue/Green/Red) | ⏳ Différé Phase 3 — réflexion sur un équivalent BdVM |
| 7 | Format physique et mise en page graphique | Phase 4 |

---

## Annexe B — Correspondance BattleLore V1 / BdVM

| BattleLore V1 (EN) | BattleLore V1 (FR officiel) | BdVM | Statut |
|---|---|---|---|
| Scout | Éclaireur | Éclaireur | ✅ Repris |
| Patrol | Patrouille | Patrouille | ✅ Repris |
| Attack | Attaque | Attaque | ✅ Repris |
| Advance | Percée | Percée | ✅ Repris |
| On the March All | En marche | En marche | ✅ Repris |
| Forward All | En avant | En avant | ✅ Repris |
| Surround Left/Right | Encerclement | Encerclement | ✅ Repris |
| Mounted Charge | Charge de cavalerie | Charge de cavalerie | ✅ Repris (adapté — bannières supprimées) |
| Foot Onslaught | Assaut d'infanterie | Assaut d'infanterie | ✅ Repris |
| Darken the Skies | Pluie de flèches | Pluie de flèches | ✅ Repris |
| Leadership | Ordre direct | Ordre direct | ✅ Repris |
| Counter Attack | Contre-attaque | Contre-attaque | ✅ Repris |
| Battlelore | Arcanes de guerre | Arcanes de guerre | ⏳ Différé Phase 2 (effet simplifié en Phase 1.5) |
| Blue/Green/Red Banners | — | — | ⏸ Écarté — équivalent BdVM à réfléchir en Phase 3 |

---

> 🔗 **Voir aussi**
> [[BdVM_Regles_Base]] — [[BdVM_Regles_Speciales]] — [[BdVM_Analyse_BLv2]] — [[BdVM_Des]]

---

_Version : 3.0 — Phase 1.5 — 2026-05-09._
_🔄 Mise à jour complète (Phase 1.5 Étape 6) : harmonisation BLv2, traitement des points ouverts #3 et #4, clarification terminologique Contre-attaque, note sur Arcanes de guerre._
