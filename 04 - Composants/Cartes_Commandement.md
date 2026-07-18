---
projet: "Batailles de la Terre du Milieu"
type: "composant"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-07-19"
tags: [BdTdM, "type/composant", "phase/1", "statut/brouillon"]
version: "0.4"
---

# Batailles de la Terre du Milieu — Cartes de commandement

> Ce document définit le système de cartes de commandement, la composition des decks par format de bataille, et le protocole de constitution du deck en début de partie. Les cartes spécifiques aux peuples sont traitées en Phase 3.
>
> Le deck de base est adapté de **BattleLore V1** (Days of Wonder, 2006), dont les cartes de commandement constituent le socle mécanique.

---

## Table des matières

1. [[#1. Principes généraux]]
2. [[#2. Anatomie d'une carte]]
3. [[#3. Les formats de bataille et leurs decks]]
4. [[#4. Composition détaillée du deck]]
5. [[#5. Protocole de constitution du deck]]
6. [[#6. Évolution en Phase 3 — cartes de peuple]]
7. [[#7. Commandement à plusieurs joueurs — format Épique]]

---

## 1. Principes généraux

Le deck de commandement est le **moteur de tension** du jeu. Il conditionne quelles unités peuvent agir à chaque tour, forçant les joueurs à des choix permanents entre opportunité et priorité.

### 1.1 Un deck calibré par format

Le nombre et la nature des cartes sont directement liés à la taille du plateau. La règle de calibrage est la suivante :

> **Le deck doit permettre d'activer en moyenne entre 1/3 et 1/2 des unités d'une armée par tour, quel que soit le format.**

Un deck trop généreux rend chaque tour prévisible. Un deck trop restrictif paralyse les joueurs. Le calibrage par format maintient cet équilibre sur des plateaux de tailles différentes.

### 1.2 La valeur de commandement

Plusieurs cartes activent un nombre d'unités **égal à la valeur de commandement** du joueur, c'est-à-dire le nombre de cartes qu'il a en main au moment où il joue la carte (cette carte comprise).

En Phase 1, la valeur de commandement est fixée par le format (voir §3). En Phase 2+, elle sera déterminée par une formule tenant compte des héros vivants — voir [[Regles_Base]] §5.3.

> 💡 **Exemple de jeu**
> Un joueur joue "Percée Gauche" avec 4 cartes en main (dont "Percée Gauche" elle-même). Sa valeur de commandement est 4 : il peut activer jusqu'à 4 unités dans la section gauche.

### 1.3 Deck partagé

Pour la Phase 1, les deux camps puisent dans un **deck commun unique**, sans cartes de peuple. Chacun constitue sa main en début de partie (voir §5).

> 🔗 **Voir aussi** [[#6. Évolution en Phase 3 — cartes de peuple]]

---

## 2. Anatomie d'une carte

Chaque carte de commandement comporte les informations suivantes, du haut vers le bas :

```
┌─────────────────────────────┐  ← 63 × 88 mm (standard poker)
│  zone de sécurité : 3 mm   │  ← zone utile : 57 × 82 mm
│ ┌─────────────────────────┐ │
│ │   NOM DE LA CARTE       │ │  ← ① Bandeau nom
│ │   type de carte         │ │
│ └─────────────────────────┘ │
│                             │
│  [ G ]  [ C ]  [ D ]        │  ← ② Pictogramme
│   (section active grisée)   │
│                             │
│ ┌─────────────────────────┐ │
│ │  Texte de règle         │ │  ← ③ Zone de règle
│ │  (9.5 px, adapté si     │ │     Fond gris léger
│ │   texte long → 8.5 px)  │ │     Note secondaire sous trait de séparation
│ └─────────────────────────┘ │
│                       [E·N] │  ← ④ Pastille format (bas droite)
└─────────────────────────────┘     E = Escarmouche / N = Normal / É = Épique
```

- **① Bandeau nom** : titre de la carte. Taille variable selon longueur : 18 px (court), 14 px (moyen), 11 px (long). Étiquette de type en dessous (8.5 px, capitales, discret).
- **② Pictogramme** : pour les cartes de section, trois bandes verticales représentant G / C / D — la section active en gris soutenu, les sections inactives en gris très léger. Pour les cartes Tactiques, icône propre à l'effet (silhouettes, flèches, etc.).
- **③ Zone de règle** : texte de la règle en 9.5 px (8.5 px si volume important). Fond gris léger. Une note secondaire optionnelle est séparée par un trait fin (cas limite, interaction avec une règle spéciale, etc.).
- **④ Pastille format** : coin bas droit, hors zone de règle. Indique le(s) deck(s) dans lesquels la carte est incluse.

> ⚠️ **Point ouvert**
> Le format physique des cartes est fixé à 63 × 88 mm (standard poker). La direction artistique finale (typographie, illustrations, couleurs par type de carte, ornements) est réservée à la Phase 4.

---

## 3. Les formats de bataille et leurs decks

### 3.1 Vue d'ensemble

| Format | Plateau | Sections | Main de départ | Taille du deck |
|---|---|---|---|---|
| **Escarmouche** | 10 × 7 | 3 (G / C / D) | 4 cartes | 43 cartes |
| **Normal** | 13 × 9 | 3 (G / C / D) | 5 cartes | 60 cartes |
| **Épique** | 16 × 13 | 3 (G / C / D) | _À définir_ | _À définir_ |

> ⚠️ **Point ouvert**
> La composition du deck Épique (taille, éventuel découpage supplémentaire des sections pour 6 joueurs) est réservée à la Phase 2, après le Playtest #1 en format Normal. Voir aussi §7.

### 3.2 Logique de différenciation des decks

Le deck Escarmouche est un **sous-ensemble strict** du deck Normal. On retire les cartes qui activeraient proportionnellement trop d'unités sur un plateau 10×7 et réduiraient la tension tactique :

- Les **Attaque** (G / C / D) : 3 unités par section — trop fort sur un front réduit. **−15 cartes.**
- Les **En avant** : 2 unités dans chaque section, soit 6 activations — disproportionné. **−2 cartes.**

**Total retiré : 17 cartes. Deck Escarmouche : 43 cartes.**

Toutes les autres cartes, y compris les Percées (activation variable selon la main), sont conservées. Sur un plateau réduit avec une main de 4 cartes, la valeur de commandement est naturellement plus basse qu'en Normal, ce qui calibre automatiquement leur puissance.

### 3.3 La valeur de commandement par format

La main de départ détermine la valeur de commandement de base pour les cartes à activation variable :

- **Normal** : main de 5 cartes → valeur de commandement de départ = 5
- **Escarmouche** : main de 4 cartes → valeur de commandement de départ = 4

La valeur de commandement fluctue en cours de partie selon les cartes jouées et piochées, ce qui crée une tension dynamique : jouer une carte réduit temporairement la valeur de commandement avant que la pioche ne la rétablisse.

---

## 4. Composition détaillée du deck

### 4.1 Catégories de cartes

Les cartes se répartissent en deux catégories :

**A — Cartes de section** : activent un nombre défini d'unités dans une ou plusieurs sections du champ de bataille.

**B — Cartes tactiques** : activent des unités selon leur **type** (cavalerie, infanterie, unités à distance) plutôt que leur position, ou produisent des effets spéciaux.

---

### 4.2 Deck Normal — 60 cartes

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
> La carte "Contre-attaque" décrite ci-dessous est une **carte de commandement** jouée volontairement depuis la main. Elle est distincte de la **règle universelle de contre-attaque** (réaction automatique disponible pour toute unité survivante après avoir subi une attaque au corps-à-corps). Voir [[Regles_Base]] §7.

| Carte | Nb | Effet |
|---|---|---|
| Charge de cavalerie | 3 | Activez autant d'unités de Cavalerie que votre valeur de commandement, dans n'importe quelle section. Toutes les unités activées combattent à **+1 dé** en mêlée. Elles ne peuvent pas tirer à distance. |
| Assaut d'infanterie | 2 | Activez autant d'unités d'Infanterie que votre valeur de commandement, dans n'importe quelle section. Ces unités doivent être adjacentes entre elles, formant un groupe continu. Elles peuvent se déplacer de 2 hexagones et combattre en mêlée. Elles ne peuvent pas tirer à distance. |
| Pluie de flèches | 2 | Activez toutes vos unités capables de tirer à distance, dans n'importe quelle section. Ces unités tirent deux fois ce tour, mais ne peuvent pas se déplacer ni tirer à bout portant. |
| Ordre direct | 2 | Activez 1 unité de votre choix, dans n'importe quelle section. Cette unité combat à **+1 dé** pour toute la durée du tour. |
| Contre-attaque | 2 | Jouez cette carte en réponse à la carte que vient de jouer votre adversaire. Vous exécutez le même ordre que lui : si c'est une carte de section, la section gauche devient la droite et vice-versa. Si c'est une carte tactique, appliquez l'effet identique. |
| Cri de guerre | 1 | Lancez autant de dés de bataille que votre valeur de commandement. Pour chaque face **Épée** ou **Épées croisées** obtenue, activez 1 unité de mêlée de votre choix. Pour chaque face **Cible** obtenue, activez 1 unité à distance de votre choix. Pour chaque face **Couronne** obtenue, activez 1 unité de votre choix. Toutes les unités ainsi activées combattent à **+1 dé** pour ce tour. Puis mélangez la défausse avec la pioche. |

> 🎲 **Note de design — Cri de guerre**
> La carte utilise les faces des dés comme mécanisme de sélection d'unités : Épée et Épées croisées → mêlée, Cible → distance, Couronne → libre. Les faces Drapeau et Arcane n'activent aucune unité. La pioche est mélangée immédiatement, quel que soit le résultat des dés. Renommée depuis "Arcanes de guerre" (hérité de BattleLore V1) : le nom d'origine évoquait une magie de bataille incompatible avec l'absence de couche pouvoirs/magie en V1 (D001, D010) — le mécanisme lui-même n'a jamais invoqué de sort, c'est une simple activation aléatoire par dés.

---

### 4.3 Récapitulatif comparatif

| Catégorie | Normal (60) | Escarmouche (43) |
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
| Cri de guerre | 1 | 1 |
| **Total** | **60** | **43** |

---

## 5. Protocole de constitution du deck

### 5.1 Avant chaque partie

1. **Choisir le format** de la bataille.
2. **Prendre le deck correspondant**, déjà constitué et maintenu séparé des autres decks.
3. **Mélanger le deck** à la vue des deux camps.
4. **Chaque camp pioche** le nombre de cartes de départ indiqué par le format (5 en Normal, 4 en Escarmouche) pour constituer sa main secrète.
5. Le reste du deck forme la **pioche centrale**, placée face cachée entre les joueurs.

### 5.2 Gestion de la pioche en cours de partie

- Après avoir joué une carte, le joueur actif la défausse face visible à côté de la pioche, puis **pioche 1 carte** pour ramener sa main au nombre initial — sauf s'il a joué un Éclaireur (voir §4.2).
- Si la pioche est épuisée, **mélanger la défausse** pour former une nouvelle pioche. Exception : la carte "Cri de guerre" déclenche ce mélange immédiatement après résolution.

### 5.3 Main minimale

Si un joueur se retrouve sans carte en main en début de son tour (situation rare mais possible en fin de pioche), il pioche immédiatement **2 cartes** avant de jouer.

> 💡 **Exemple de jeu**
> Début de partie en format Normal. Le camp du Bien pioche 5 cartes : Patrouille Centre, Charge de cavalerie, Attaque Droite, Éclaireur Gauche, En marche. Sa valeur de commandement est 5. Il joue "Charge de cavalerie" et peut activer jusqu'à 5 unités de cavalerie sur tout le plateau, chacune avec +1 dé en mêlée. Il défausse la carte, pioche 1 carte, et sa main revient à 5.

---

## 6. Évolution en Phase 3 — cartes de peuple

En Phase 3, chaque peuple dispose d'un **supplément de cartes** qui s'intègre au deck de base selon la règle suivante :

> Pour chaque carte de peuple ajoutée au deck, **une carte générique de même catégorie** est retirée.

Le deck garde ainsi une taille constante par format. L'identité tactique du peuple est renforcée sans déséquilibrer le volume d'activations disponibles.

_Exemple (non définitif, à des fins d'illustration uniquement) :_

- Gondor pourrait ajouter des cartes "Feux d'alerte" (activation d'urgence des garnisons) → retirer autant de "Patrouille" génériques.
- Le Mordor pourrait ajouter des cartes "Cris de guerre" (bonus offensif orque) → retirer autant de "En marche".

> ⚠️ **Point ouvert**
> Le nombre exact de cartes de peuple par armée et le mécanisme d'échange (libre ou imposé par catégorie ?) sont à définir lors de la Phase 3.

---

## 7. Commandement à plusieurs joueurs — format Épique

> ⚠️ **Point ouvert — non requis avant la Phase 2**
> Le Playtest #1 et le Playtest #2 se jouent tous les deux en format Normal, à 1 joueur par camp (voir [[Regles_Base]] §5.5). Cette section reste à concevoir avant le premier test en format Épique (6 joueurs, 3v3), prévu en Phase 2 — tâche "Passer au format Épique" du plan de projet.
>
> Ce qui est déjà tranché (D016 du [[Document de cadrage]]) : en Épique, chaque joueur contrôle une **Section** (Gauche/Centre/Droite) plutôt qu'une armée nommée — pas de sous-force nominative par joueur. La répartition des peuples entre sections est une décision de scénario (Phase 3), pas une règle de commandement.
>
> Reste à trancher le jour venu : les 3 joueurs d'un même camp jouent-ils une main commune (décidée ensemble) ou une sous-main individuelle par section ? Comment se répartissent les cartes multi-sections (En marche, En avant, Encerclement) ou les cartes tactiques qui ne visent pas une section précise (Charge de cavalerie, Cri de guerre) entre les 3 joueurs d'un camp ? Ces questions seront rouvertes avant ce test, pas avant.

---

> 🔗 **Voir aussi**
> [[Regles_Base]] — [[Regles_Speciales]] — [[Document de cadrage]]

---

*Version : 0.4 — Phase 1 — 2026-07-19.*
*Première adaptation de Batailles de la Terre du Milieu (BdTdM) : reprise du système de deck générique, sans reprise du contenu spécifique à l'autre projet dont il est issu. Renommage "Bataille" → "Normal" (même plateau 13×9, mêmes decks). Dimensions du format Épique alignées sur le document de cadrage (16×13, D005). Annexe de correspondance BattleLore V1 retirée (plus nécessaire — terminologie déjà fixée). Carte "Arcanes de guerre" renommée en "Cri de guerre" (D019, via l'étape intermédiaire "Ruée générale") — connotation magique incompatible avec l'absence de couche pouvoirs en V1 (D001, D010) ; nom final choisi pour son ancrage Terre du Milieu, neutre entre les deux camps ; mécanisme de dés inchangé. Ajout d'une section dédiée au commandement multi-joueurs, explicitement différée à la Phase 2. Renommé depuis `BdVM_Cartes_Commandement.md`. **Correction** : "Charge de cavalerie", "Ordre direct" et "Cri de guerre" indiquaient un bonus **+2 dés**, reliquat d'une ancienne calibration de BdVM (abandonnée dans ce projet jumeau) — corrigé en **+1 dé**, cohérent avec le reste du système.*
