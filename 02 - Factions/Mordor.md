---
projet: "Batailles de la Terre du Milieu"
type: "faction"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-08-08"
tags: [BdTdM, "type/faction", "peuple/mordor", "statut/brouillon"]
version: "1.1"
---

# Mordor — Profils d'unités

> **Objet de ce document (refonte P4, D071).** Re-expression complète du roster sur la taxonomie visuelle (classe × type × mode, [[Regles_Base]] §2.4) et la matrice de points ([[Regles_Points]] §2). Système à deux badges fixes, miroir des autres peuples : **[Horde]** devient le badge Faction (nerfé au passage — perd son volet [Inébranlable 1]), **[Férocité]** devient le badge Spéciale.
>
> **[Peur X] et [Armure 1] deviennent intrinsèques au type Créature** (D071) — plus des règles à assigner, un trait du type lui-même, comme le compteur de PV. Le Troll en bénéficie sans supplément de coût ; la même règle s'appliquera au Mûmakil (Harad) à sa propre re-expression.
>
> Aligné sur [[Regles_Base]] v0.10 et [[Regles_Speciales]] v0.20.

---

## 1. Les deux badges de Mordor

| Badge | Effet | Coût brut | Porté par |
|---|---|---|---|
| **Faction** (Mordor) | **[Horde]** *(nerfée D071 — +1 dé à pleine santé seulement, plus d'Inébranlable)* | +2 *(forfait)* | Infanterie orque de mêlée uniquement — jamais le tir, jamais la cavalerie/les bêtes (D032) |
| **Élite** | **[Inébranlable 1]** | +2 | Réservé à l'Uruk-hai — l'élite qui ne rompt pas |
| **Spéciale** (unité) | **[Férocité]** | +1 | Troupes qui rendent coup pour coup, même en reculant |

**[Horde] reste réservée aux Orcs de mêlée**, exactement comme avant la refonte : l'Uruk-hai (l'élite qui ne rompt pas) n'en porte jamais, ni les pisteurs (le tir), ni les wargs (des bêtes, pas des orques).

---

## 2. Liste des troupes

| # | Unité | Type | Combat | Classe | Badges | **Points** |
|---|---|---|---|---|---|---|
| 1 | Bande d'orques du Mordor | Infanterie | Mêlée | 🟢 | Faction | **4** |
| 2 | Bande d'orques du Morannon | Infanterie | Mêlée | 🔵 | Faction + Spéciale | **5** |
| 3 | Bande de pisteurs orques | Infanterie | Distance | 🟢 | *(aucun)* | **3** |
| 4 | Meute de cavaliers wargs | Cavalerie | Mêlée | 🔵 | Spéciale | **6** |
| 5 | Bande d'uruk-hai du Mordor | Infanterie | Mêlée | 🔴 | Spéciale + Élite | **6** |
| 6 | Troll du Mordor | Créature | Mêlée | 🔴 | Spéciale *(+ Peur 1/Armure 1 intrinsèques)* | **6** |

> ⚠️ **Meute de cavaliers wargs : hausse de coût réelle, non compensée.** Toute cavalerie 🟢/🔵 de mêlée porte désormais [Poursuite 2] intrinsèque, gratuit, quel que soit le peuple — les wargs en héritent sans qu'aucun badge Mordor ne vienne compenser (contrairement à Khand, où [Mercenaire] absorbe l'effet). Coût réel : **4 → 6 pts**, assumé comme conséquence de la taxonomie plutôt que corrigé par une règle ad hoc.

---

## 3. Profils détaillés

### 1. Bande d'orques du Mordor

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Infanterie | Mêlée | 🟢 | 2 | 2 dés *(3 à pleine force)* | — | 4 | **4** |

**Badges :** Faction ([Horde])

**Note narrative :** la piétaille de Sauron, jetée en masse contre les lignes. Féroce tant que le nombre la porte (3 dés à pleine force), elle rompt et retombe à 2 dés dès la première perte — pour le reste de la partie. L'orque ne se lit pas au dé près : il se lit à la vague.

---

### 2. Bande d'orques du Morannon

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Infanterie | Mêlée | 🔵 | 2 | 3 dés *(4 à pleine force)* | — | 4 | **5** |

**Badges :** Faction ([Horde]) + Spéciale ([Férocité])

**Note narrative :** les orques-soldats de la Porte Noire, plus grands et mieux armés que la piétaille — pas blindés (l'armure n'est plus leur trait, contrairement aux versions précédentes de ce roster), mais rendent coup pour coup même en cédant du terrain. C'est le « vrai » soldat orque : la ligne sur laquelle Mordor s'appuie.

---

### 3. Bande de pisteurs orques

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Infanterie | Distance | 🟢 | 2 | 2 dés | 4 | 4 | **3** |

**Badges :** *(aucun)*

**Note narrative :** les traqueurs à l'arc de la Terre de l'Ombre — des orques d'un genre plus fureteur, envoyés en avant pour flécher et harceler. Décroche après avoir tiré ([Mobilité 1] intrinsèque, gratuite, classe 🟢). Pas de [Horde] : la règle reste réservée à la mêlée de masse (D032, confirmé depuis la Passe 0).

---

### 4. Meute de cavaliers wargs

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Cavalerie | Mêlée | 🔵 | 3 | 3 dés | — | 3 | **6** |

**Badges :** Spéciale ([Férocité])

**Note narrative :** des loups sauvages montés par des orques, qui déchirent et mordent sans lâcher prise ([Férocité] : contre-attaque même forcée de reculer). Porte [Poursuite 2] intrinsèque comme toute cavalerie 🔵 — Mordor n'a jamais prétendu avoir la meilleure cavalerie du jeu (identité réservée au Rohan), mais en hérite mécaniquement comme tout le monde depuis la refonte de la taxonomie. Pas de badge Faction : ce sont des bêtes, pas des orques (D032).

---

### 5. Bande d'uruk-hai du Mordor

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Infanterie | Mêlée | 🔴 | 1 ou 2 | 4 dés *(constante)* | — | 4 | **6** |

**Badges :** Spéciale ([Férocité]) + Élite ([Inébranlable 1])

**Note narrative :** les grands Uruks noirs de Barad-dûr, la haute stature bréée par Sauron pour tenir là où la piétaille rompt. C'est **l'exception du roster** : pas de [Horde], une Attaque 4 **constante**. [Armure 1] (mailles noires) vient gratuitement de la classe 🔴, plus besoin de la mentionner explicitement ; [Férocité] (badge Spéciale) traduit la cruauté d'élite qui riposte avant de reculer ; [Inébranlable 1] (badge Élite) confirme mécaniquement ce que dit le texte depuis l'origine — « l'orque qui ne rompt pas ».

> 🎲 **Note de calcul.** Brut = 19 (Inf 🔴 mêlée, Armure 1 incluse) + Férocité (1) + Élite (2) = 22 → round(22÷3)−1 = 6. La compression absorbe le badge Élite au même palier — coût inchangé malgré la règle en plus.

---

### 6. Troll du Mordor

| Type | Combat | Classe | Mouvement | Attaque | Portée | PV | **Points** |
|---|---|---|---|---|---|---|---|
| Créature | Mêlée | 🔴 | 2 | 4 dés | — | 4 | **6** |

**Badges :** Spéciale ([Férocité])

**Intrinsèques du type Créature (D071) :** **[Armure 1]** + **[Peur 1]** *(chaque Arcane obtenue en attaque compte comme 1 Drapeau contre la cible)*, sans supplément de coût — plus besoin de les chiffrer, ce sont des traits du type lui-même.

**Note narrative :** un Olog-hai tiré des fosses de Gorgoroth, une masse de muscle et de fer dont la seule approche fait plier le courage des hommes ([Peur], désormais un trait de toute créature, pas une exclusivité du Troll) et dont la peau épaisse encaisse ce que l'acier ne saurait percer ([Armure], idem). [Férocité] (badge Spéciale) ajoute la cruauté brute : même blessé, il rend coup pour coup avant de reculer.

**Simplification par rapport aux versions précédentes** : perd [Relance 1] *(ex-[Arme Lourde 1])*, qui n'a plus de rôle distinctif une fois [Peur]/[Armure] rendues gratuites — le profil se resserre sur une seule règle explicite (Férocité) plus les deux intrinsèques.

> 🎲 **Note de calcul.** Brut = Mvt 2 + PV 4 + Atk 4×3(12) + Férocité(1) = 19 → round(19÷3)−1 = 5. **Prime de pièce signature assumée (+1)**, cohérente avec le traitement déjà appliqué à ce profil (D054) : coût final **6**, en baisse par rapport à l'ancien 7 — la simplification (Peur/Armure gratuites, Relance abandonnée) fait plus que compenser le badge Férocité ajouté.

---

## 4. Récapitulatif des badges portés

| Badge | Unités qui le portent |
|---|---|
| **Faction** ([Horde]) | Bande d'orques du Mordor (1) · Bande d'orques du Morannon (2) |
| **Spéciale** ([Férocité]) | Bande d'orques du Morannon (2) · Meute de cavaliers wargs (4) · Bande d'uruk-hai (5) · Troll du Mordor (6) |
| **Élite** ([Inébranlable 1]) | Bande d'uruk-hai (5) |
| **Aucun badge** | Bande de pisteurs orques (3) — tir, exclu de Horde par principe (D032) |

**Intrinsèques hors badges** : [Armure 1] (classe 🔴, sur Uruk-hai et Troll) · [Peur 1] (type Créature, sur Troll uniquement pour l'instant).

---

## 5. Points ouverts transverses

- **Coût de [Horde] (2, nerfée)** — jamais testé sous cette forme allégée (l'ancien forfait à 3, avec Inébranlable inclus, n'avait lui-même jamais été validé en partie). À surveiller en priorité au prochain playtest.
- **Meute de cavaliers wargs (6 pts, hausse non compensée)** — voir l'avertissement §2. Pas de solution retenue pour l'instant ; à observer à la table avant d'envisager un correctif dédié.
- **Intrinsèque Créature (Peur 1 + Armure 1)** — nouvelle règle transverse, first appliquée au Troll seul dans ce projet. À vérifier à la re-expression du Mûmakil (Harad, P4/P5) qu'elle ne fait pas doublon avec ses règles bespoke existantes ([Howdah], [Inébranlable ∞]).
- **[Réception de charge]** reste sans porteur à Mordor (inchangé depuis la Passe 0).
- **Couche Leadership (Phase 2)** — dé-randomiser l'accès des héros à la face Arcane, hors scope de cette repasse.

---

*Version : 1.1 — Phase 1 — 2026-08-08. **Élite ajouté à l'Uruk-hai** (oubli de la repasse initiale) : badge Élite ([Inébranlable 1]) en plus de Spéciale ([Férocité]). Coût inchangé (6 pts) — la compression absorbe le badge au même palier.*

*Version : 1.0 — Phase 1 — 2026-08-08. **Refonte P4 (D071) : re-expression complète sur la taxonomie visuelle et le système de badges.** [Horde] devient le badge Faction, nerfée (perd [Inébranlable 1], coût 3→2) ; [Férocité] devient le badge Spéciale. **[Peur X] et [Armure 1] rendues intrinsèques au type Créature** — transverse, s'appliquera au Mûmakil. Troll simplifié : perd [Relance 1], conserve la prime de pièce signature (+1). Meute de cavaliers wargs : hausse de coût non compensée (4→6 pts), assumée. Roster inchangé à 6 profils. Non testé — validation P7a.*
