---
projet: "Batailles du Vieux Monde"
type: "regles"
phase: "1.6"
statut: "à-tester"
date_maj: "2026-06-01"
tags: [BdVM, "type/regles", "phase/1.6", "statut/à-tester"]
---

# Batailles du Vieux Monde — Règles de terrain

> Ce document définit les règles de terrain pour la Phase 1.6. Il couvre six types de terrain : campagne, terrain boisé, terrain surélevé (colline), cours d'eau, gué, pont et bâtiment. Les terrains fantastiques (Tour de sorcier, Portail du Chaos, Pierre de Sang, etc.) sont réservés à la Phase 2.
>
> **Base de référence :** BattleLore Seconde Édition (FFG, 2013) — Rulebook p. 13 + Reference Book p. 2–5. Toutes les adaptations par rapport à BLv2 sont tracées dans `BdVM_Analyse_BLv2.md` §9.

> 🔄 **Mise à jour — 2026-06-01 | Phase 1.6 Étape 6**
> - **§10 — Retraites et terrain** : réécriture complète (D091). Alignement C&C standard (Memoir '44, C&C Ancients, BattleCry) : seul le terrain **impassable** bloque la retraite. La forêt, le gué et le bâtiment n'ont aucun effet sur la retraite.
> - **§4, §7, §9** : suppression des sous-sections "Retraite" par terrain (devenues inutiles).
> - **§9.2** : suppression de la référence au Moral dans l'exemple de jeu.

> 🔄 **Mise à jour — 2026-05-30 | Phase 1.6 Étape 3**
> - **Terrain boisé §4.2** : plafond de dés ramené à **2 dés** (retour BLv2 standard, conséquence de D061).
> - **Terrain surélevé §5.2** : introduction du **bonus offensif +1 dé** pour l'attaquant en hauteur (D076).
> - **[Terrain favori : Boisé]** : nouvelle règle spéciale (D079).
> - **Tableau récapitulatif §11** : mis à jour.

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

> 🔗 **Voir aussi** [[BdVM_Regles_Base]] §6 — Mouvement · §9 — Retraite

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
> Les unités volantes et leurs interactions avec la ligne de vue seront précisées en Phase 2.

> 🔗 **Voir aussi** [[BdVM_Regles_Base]] §7.4 — Ligne de vue

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

Le **terrain boisé** représente les forêts, bosquets et sous-bois du Vieux Monde. Ces zones offrent un couvert naturel mais gênent les manœuvres et les tirs.

> 🎲 **Note de design** Le plafond est ramené à 2 dés (BLv2 standard) suite à la recalibration générale des dés (D061). Les unités avec [Terrain favori : Boisé] (ex. Skinks) ignorent toutes les restrictions du terrain boisé sauf la LdV.

### 4.1 Mouvement

Une unité qui **entre** dans un hexagone de terrain boisé **s'y arrête immédiatement**, quelle que soit sa valeur de mouvement restante.

- Une unité déjà en forêt en début de tour peut la quitter normalement en dépensant 1 point de mouvement, puis continuer son déplacement.

### 4.2 Combat

- Toute attaque dont **l'attaquant ou la cible** se trouve en terrain boisé est limitée à **2 dés maximum** (avant modificateurs).
- Cette limite s'applique aussi bien au **tir** qu'à la **mêlée**.
- Si la valeur d'attaque de l'unité est inférieure ou égale à 2, elle lance ses dés normalement.

> 💡 **Exemple de jeu**
> Des Grandes Épées (4 dés) attaquent des Saurus positionnés dans un bois : 2 dés au lieu de 4. Des Skinks [Terrain favori : Boisé] tirent depuis un bois : ils ignorent le plafond.

### 4.3 Ligne de vue

Un hexagone de terrain boisé est du **terrain bloquant** : il bloque la LdV pour toute unité extérieure dont la ligne le traverse. Une unité dans le bois trace sa LdV normalement vers l'extérieur.

---

## 5. Terrain surélevé

Le **terrain surélevé** représente les collines et promontoires qui offrent un avantage tactique décisif.

> 🎲 **Note de design** En Phase 1.5, les collines n'avaient d'effet que sur la LdV. Le Playtest #2 a confirmé qu'elles n'étaient jamais disputées. La Phase 1.6 introduit un bonus offensif +1 dé (D086) inspiré de Battle of Westeros. Le mouvement reste libre (D087 écarté).

### 5.1 Mouvement

Le terrain surélevé **n'impose aucune restriction de mouvement**.

### 5.2 Combat

Une unité qui attaque **depuis** un hexagone de terrain surélevé vers un hexagone en **contrebas** gagne **+1 dé** (mêlée et tir).

Ce bonus ne s'applique **pas** si :
- l'attaquant et la cible sont tous les deux en hauteur (même altitude),
- l'attaquant est en contrebas et la cible est en hauteur.

> 💡 **Exemple de jeu**
> Des Arbalétriers (2 dés) en hauteur tirent sur des Saurus en contrebas : 3 dés. Des Hallebardiers en contrebas attaquent des Gardes du Temple en hauteur : 0 bonus.

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
> Les règles de traversée pour les unités dotées de capacités spéciales (vol, déplacement magique) seront définies en Phase 2.

---

## 7. Gué

Un **gué** est un point de passage praticable à travers un cours d'eau.

### 7.1 Mouvement

Une unité qui **entre** dans un hexagone de gué **s'y arrête immédiatement**, quelle que soit sa valeur de mouvement restante. Elle peut quitter le gué normalement au tour suivant.

### 7.2 Combat

- Toute unité **positionnée dans un gué** attaque avec un maximum de **2 dés** (avant modificateurs), en mêlée comme au tir.
- Cette limite s'applique à l'**attaquant uniquement**. Une unité sur la berge attaquant une unité dans le gué utilise sa valeur d'attaque normale.

> 💡 **Exemple de jeu**
> Des Saurus à la Lance (3 dés) dans un gué contre-attaquent : 2 dés au lieu de 3. Des Grandes Épées sur la berge les attaquent : 4 dés normalement.

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

Le **bâtiment** représente les constructions du Vieux Monde : ruines, maisons, bastions, fortifications.

> 🎲 **Note de design** BLv2 accorde une protection fixe de 1 dégât ignoré. BdVM adapte ce système avec **[Protection X]** modulable (D050).

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
> Des Hallebardiers dans un bâtiment solide [Protection 2] reçoivent 5 touches et 1 Drapeau : ils ignorent 2 touches → 3 touches effectives. Le Drapeau force 1 hexagone de retraite.

### 9.3 Ligne de vue

Un hexagone de bâtiment est du **terrain bloquant** : il bloque la LdV pour toute unité extérieure. Une unité à l'intérieur trace sa LdV normalement vers l'extérieur.

---

## 10. Retraites et terrain

> 🔄 **Réécriture — 2026-06-01 | Phase 1.6 Étape 6 — D091**
> Alignement sur la règle standard C&C (Memoir '44, C&C Ancients, BattleCry), en écart par rapport à BLv2 : seul le terrain impassable bloque la retraite.

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

> **Note sur [Terrain favori : Boisé] :** cette règle reste utile pour le mouvement volontaire et le combat en forêt — la retraite en forêt étant désormais libre pour toutes les unités, cet aspect de [Terrain favori : Boisé] est sans objet.

> 🔗 **Voir aussi** [[BdVM_Regles_Base]] §9 — Retraite

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

> **Note sur [Terrain favori : Boisé] :** les unités avec cette règle (ex. Skinks) ignorent le plafond de 2 dés et l'arrêt à l'entrée en terrain boisé. La LdV du bois s'applique normalement à toutes les unités.

> **Note sur [Protection X] :** valeur définie par le scénario (ruine = 1, bâtiment solide = 2, fortification = 3). S'applique aux touches en combat uniquement.

---

> 🔗 **Voir aussi**
> [[BdVM_Regles_Base]] — [[BdVM_Regles_Speciales]] — [[BdVM_Analyse_BLv2]] §9

---

*Version : 3.1 — Phase 1.6 — 2026-06-01.*
*🔄 Mise à jour Phase 1.6 Étape 6. §10 réécrit (D091) : seul le terrain impassable bloque la retraite, alignement C&C standard. Suppression des sous-sections retraite dans §4, §7, §9. Suppression référence au Moral dans §9.2. Colonne Retraite ajoutée au tableau récapitulatif §11.*
*Remplace : BdVM_Terrain.md v3.0 (2026-05-30).*
