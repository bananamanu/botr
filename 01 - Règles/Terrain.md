---
projet: "Batailles de la Terre du Milieu"
type: "regles"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-07-19"
tags: [BdTdM, "type/regles", "phase/1", "statut/brouillon"]
version: "0.1"
---

# Batailles de la Terre du Milieu — Règles de terrain

> Ce document définit les règles de terrain de la Phase 1. Il couvre six types de terrain : campagne, terrain boisé, terrain surélevé (colline), cours d'eau, gué, pont et bâtiment. Les terrains fantastiques ou spéciaux propres à certains lieux de la Terre du Milieu sont réservés à une phase ultérieure, si besoin s'en fait sentir.
>
> Ce document est un complément détaillé à [[Regles_Base]] §6 (Mouvement) et §7.5 (Modificateurs de dés liés au terrain), qui donnent déjà la version condensée nécessaire au Playtest #1. Pas de terrain spécifique développé pour le scénario du Pelennor (D017 du [[Document de cadrage]]) : le champ de bataille y est majoritairement plat. Ces règles génériques couvrent les éléments ponctuels qu'un scénario pourrait vouloir introduire (bosquet, talus, cours d'eau, ruines).

---

## Table des matières

1. [[#1. Terrain bloquant et terrain impassable]]
2. [[#2. Ligne de vue]]
3. [[#3. Campagne]]
4. [[#4. Terrain boisé]]
5. [[#5. Terrain surélevé]]
6. [[#6. Cours d'eau]]
7. [[#7. Gué]]
8. [[#8. Pont]]
9. [[#9. Bâtiment]]
10. [[#10. Retraites et terrain]]
11. [[#11. Tableau récapitulatif]]

---

## 1. Terrain bloquant et terrain impassable

Deux grandes catégories de terrain ont des effets systémiques sur la ligne de vue et le mouvement.

**Terrain bloquant** : bloque la ligne de vue pour toute unité dont la ligne traverse l'hexagone (sauf exceptions précisées). Les types suivants sont des terrains bloquants : terrain boisé, terrain surélevé, bâtiment.

**Terrain impassable** : aucune unité ne peut entrer dans cet hexagone ni le traverser, que ce soit en mouvement volontaire ou en retraite. Le cours d'eau est impassable, sauf si l'hexagone contient un gué ou un pont.

> 🔗 **Voir aussi** [[Regles_Base]] §6 — Mouvement · §9 — Retraite

---

## 2. Ligne de vue

La **ligne de vue** (LdV) est nécessaire pour toute attaque à distance. Elle est tracée du centre de l'hexagone de l'unité attaquante au centre de l'hexagone de la cible.

La ligne de vue est **bloquée** si elle traverse au moins un hexagone occupé par :

- un **terrain bloquant** (bois, colline, bâtiment), ou
- une **autre unité**, amie ou ennemie.

La ligne de vue **n'est pas bloquée** par :

- l'hexagone de l'unité attaquante elle-même,
- l'hexagone de la cible elle-même,
- la campagne, un cours d'eau, un gué ou un pont.

**Cas d'arête :** lorsque la ligne de vue longe le bord d'un ou plusieurs hexagones, elle est décalée d'un côté. Elle n'est bloquée que s'il y a du terrain bloquant ou une unité des **deux côtés** de la ligne.

**Unités en hauteur :** une unité positionnée sur un hexagone de terrain surélevé ignore toutes les autres unités lorsqu'elle trace sa ligne de vue. Le terrain bloquant continue de bloquer sa LdV normalement.

> ⚠️ **Point ouvert**
> Les unités volantes (ex. Nazgûl montés sur créature ailée) et leurs interactions avec la ligne de vue seront précisées en Phase 2, avec le reste des règles de monstres avancés.

> 🔗 **Voir aussi** [[Regles_Base]] §7.4 — Ligne de vue

---

## 3. Campagne

La **campagne** désigne tout hexagone de terrain ouvert, sans obstacle ni élévation. C'est le terrain de référence du jeu.

| Aspect | Règle |
|---|---|
| **Mouvement** | Aucune restriction. |
| **Combat** | Aucune restriction. |
| **Ligne de vue** | Dégagée. |
| **Retraite** | Aucune restriction. |

_Tout ce qui n'est pas qualifié autrement est de la campagne._

---

## 4. Terrain boisé

Le **terrain boisé** représente les bois, bosquets et sous-bois de la Terre du Milieu. Ces zones offrent un couvert naturel mais gênent les manœuvres et les tirs.

> 🎲 **Note de design** Certaines unités pourront à l'avenir porter la règle [Terrain favori : Boisé] (voir [[Regles_Speciales]]), qui annule toutes les restrictions de mouvement et de combat du terrain boisé pour elles — la LdV du bois reste bloquante même pour ces unités. Aucun peuple de la V1 ne porte cette règle pour l'instant.

### 4.1 Mouvement

Une unité qui **entre** dans un hexagone de terrain boisé **s'y arrête immédiatement**, quelle que soit sa valeur de mouvement restante.

- Une unité déjà en forêt en début de tour peut la quitter normalement en dépensant 1 point de mouvement, puis continuer son déplacement.

### 4.2 Combat

- Toute attaque dont **l'attaquant ou la cible** se trouve en terrain boisé est limitée à **2 dés maximum** (avant modificateurs).
- Cette limite s'applique aussi bien au **tir** qu'à la **mêlée**.
- Si la valeur d'attaque de l'unité est inférieure ou égale à 2, elle lance ses dés normalement.

> 💡 **Exemple de jeu**
> Une unité d'Infanterie (4 dés) attaque une unité positionnée dans un bois : 2 dés au lieu de 4.

### 4.3 Ligne de vue

Un hexagone de terrain boisé est du **terrain bloquant** : il bloque la LdV pour toute unité extérieure dont la ligne le traverse. Une unité dans le bois trace sa LdV normalement vers l'extérieur.

---

## 5. Terrain surélevé

Le **terrain surélevé** représente les collines et promontoires qui offrent un avantage tactique décisif.

### 5.1 Mouvement

Le terrain surélevé **n'impose aucune restriction de mouvement**.

### 5.2 Combat

Une unité qui attaque **depuis** un hexagone de terrain surélevé vers un hexagone en **contrebas** gagne **+1 dé** (mêlée et tir).

Ce bonus ne s'applique **pas** si :
- l'attaquant et la cible sont tous les deux en hauteur (même altitude),
- l'attaquant est en contrebas et la cible est en hauteur.

> 💡 **Exemple de jeu**
> Des archers (2 dés) en hauteur tirent sur une unité en contrebas : 3 dés. Une unité en contrebas attaque une unité en hauteur : 0 bonus.

### 5.3 Ligne de vue

- Un hexagone de terrain surélevé est du **terrain bloquant** pour les unités en contrebas.
- Une unité en hauteur ignore toutes les autres unités pour tracer sa LdV (mais pas le terrain bloquant).

---

## 6. Cours d'eau

Le **cours d'eau** représente rivières, lacs et étendues d'eau infranchissables.

### 6.1 Mouvement

Un hexagone de cours d'eau est **impassable** : aucune unité ne peut y entrer ni le traverser, sauf si l'hexagone contient un gué ou un pont.

### 6.2 Combat

Non applicable — aucune unité ne peut occuper un hexagone de cours d'eau.

### 6.3 Ligne de vue

Un hexagone de cours d'eau **ne bloque pas la ligne de vue**.

> ⚠️ **Point ouvert**
> Les règles de traversée pour les unités dotées de capacités spéciales (vol, etc.) seront définies en Phase 2.

---

## 7. Gué

Un **gué** est un point de passage praticable à travers un cours d'eau.

### 7.1 Mouvement

Une unité qui **entre** dans un hexagone de gué **s'y arrête immédiatement**, quelle que soit sa valeur de mouvement restante. Elle peut quitter le gué normalement au tour suivant.

### 7.2 Combat

- Toute unité **positionnée dans un gué** attaque avec un maximum de **2 dés** (avant modificateurs), en mêlée comme au tir.
- Cette limite s'applique à l'**attaquant uniquement**. Une unité sur la berge attaquant une unité dans le gué utilise sa valeur d'attaque normale.

> 💡 **Exemple de jeu**
> Une unité dans un gué contre-attaque avec 3 dés en profil : 2 dés au lieu de 3. Une unité sur la berge l'attaque normalement.

### 7.3 Ligne de vue

Un hexagone de gué **ne bloque pas la ligne de vue**.

---

## 8. Pont

Le **pont** est un ouvrage franchissant un cours d'eau.

### 8.1 Mouvement

Un pont **n'impose aucune restriction de mouvement**. Les règles d'occupation standard s'appliquent : une seule unité peut occuper l'hexagone de pont à la fois.

### 8.2 Combat

Aucune règle spéciale. Les unités sur un pont combattent normalement.

### 8.3 Ligne de vue

Un hexagone de pont **ne bloque pas la ligne de vue**.

---

## 9. Bâtiment

Le **bâtiment** représente les constructions de la Terre du Milieu : ruines, fermes, bastions, fortifications.

### 9.1 Mouvement

Une unité qui **entre** dans un hexagone de bâtiment **s'y arrête immédiatement**. Elle peut combattre normalement depuis le bâtiment ce tour, et le quitter normalement au tour suivant.

### 9.2 Combat — [Protection X]

Une unité occupant un bâtiment bénéficie de **[Protection X]**, où X est défini par le type de bâtiment indiqué dans le scénario :

| Type de bâtiment | [Protection X] |
|---|---|
| **Ruine** | [Protection 1] |
| **Bâtiment solide** | [Protection 2] |
| **Fortification** | [Protection 3] |

**Effet :** l'unité ignore X touches par attaque reçue, avant d'appliquer les pertes. S'applique à toutes les attaques (mêlée et tir).

> 💡 **Exemple de jeu**
> Une unité dans un bâtiment solide [Protection 2] reçoit 5 touches et 1 Drapeau : elle ignore 2 touches → 3 touches effectives. Le Drapeau force 1 hexagone de retraite.

### 9.3 Ligne de vue

Un hexagone de bâtiment est du **terrain bloquant** : il bloque la LdV pour toute unité extérieure. Une unité à l'intérieur trace sa LdV normalement vers l'extérieur.

---

## 10. Retraites et terrain

**Règle générale :**

Le terrain **n'a aucun effet** sur la retraite. Une unité en retraite traverse librement la forêt, le gué, le bâtiment et le terrain surélevé sans s'arrêter.

Seules deux situations **bloquent** la retraite et infligent **1 touche par hexagone non résolu** :

- **Terrain impassable** (cours d'eau, bord du plateau)
- **Unité ennemie** sur le chemin de retraite

**Exception — soutien :** si l'unité entre dans un hexagone occupé par une unité **amie**, elle est soutenue : tous les hexagones de retraite restants sont ignorés sans touche supplémentaire.

| Obstacle rencontré en retraite | Effet |
|---|---|
| **Campagne, forêt, gué, bâtiment, terrain surélevé, pont** | Aucun — retraite continue normalement. |
| **Cours d'eau / bord du plateau** | Bloqué — 1 touche par hexagone non résolu. |
| **Unité ennemie** | Bloqué — 1 touche par hexagone non résolu. |
| **Unité amie** | Soutien — tous les hexagones restants ignorés, 0 touche. |

> 🔗 **Voir aussi** [[Regles_Base]] §9 — Retraite

---

## 11. Tableau récapitulatif

| Terrain | Mouvement | Combat (attaquant) | Combat (cible) | Ligne de vue | Retraite |
|---|---|---|---|---|---|
| **Campagne** | Libre | Normal | Normal | Dégagée | Libre |
| **Terrain boisé** | Arrêt à l'entrée | Max 2 dés | Max 2 dés | Bloquante si traversée | Libre |
| **Terrain surélevé** | Libre | +1 dé si cible en contrebas | Normal | Bloquante (unités en hauteur ignorent les unités) | Libre |
| **Cours d'eau** | Impassable | — | — | Dégagée | **Impassable** |
| **Gué** | Arrêt à l'entrée | Max 2 dés si dans le gué | Normal | Dégagée | Libre |
| **Pont** | Libre (1 unité max) | Normal | Normal | Dégagée | Libre |
| **Bâtiment** | Arrêt à l'entrée | Normal | Normal + [Protection X] | Bloquante si traversée | Libre |

> **Note sur [Terrain favori : X] :** une unité portant cette règle pour un type de terrain donné ignore le plafond de dés et l'arrêt à l'entrée pour ce terrain. La ligne de vue du terrain s'applique normalement à toutes les unités, y compris celles-ci. Aucun peuple de la V1 ne porte cette règle pour l'instant (voir [[Regles_Speciales]]).

> **Note sur [Protection X] :** valeur définie par le scénario (ruine = 1, bâtiment solide = 2, fortification = 3). S'applique aux touches en combat uniquement.

---

> 🔗 **Voir aussi**
> [[Regles_Base]] — [[Regles_Speciales]] — [[Document de cadrage]]

---

*Version : 0.1 — Phase 1 — 2026-07-19.*
*Première adaptation de Batailles de la Terre du Milieu (BdTdM) : reprise du corps de règles générique (campagne, bois, colline, cours d'eau, gué, pont, bâtiment), sans reprise du contenu spécifique à l'autre projet dont il est issu. Retrait des exemples et références liés à cet autre univers, des notes de changelog propres à son historique de phases, et de toute mention de faction. Renommé depuis `BdVM_Terrain.md`.*
