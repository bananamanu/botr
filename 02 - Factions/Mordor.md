---
projet: "Batailles de la Terre du Milieu"
type: "faction"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-08-08"
tags: [BdTdM, "type/faction", "peuple/mordor", "statut/brouillon"]
version: "1.2"
---

# Mordor — Profils d'unités

> **Objet de ce document (refonte P4, D071 ; refonte de [Horde] et migration badges universels, D075).** Re-expression complète du roster sur la taxonomie visuelle (classe × type × mode, [[Regles_Base]] §2.4) et la matrice de points ([[Regles_Points]] §2). Système à deux badges fixes : **[Horde]** reste le badge Faction, **refondue une seconde fois** (D075) pour une identité plus tranchée — frappe fort au premier contact, s'effondre au premier sang. Le badge Spéciale migre vers **[Relance 1]** (universel, D073) ; [Férocité] disparaît entièrement du roster.
>
> **[Peur X] et [Armure 1] restent intrinsèques au type Créature** (D071) — inchangé.
>
> Aligné sur [[Regles_Base]] v0.12 et [[Regles_Speciales]] v0.24, [[Regles_Points]] v0.21.

---

## 1. Les deux badges de Mordor

| Badge | Effet | Coût brut | Porté par |
|---|---|---|---|
| **Faction** (Mordor) | **[Horde]** *(refondue D075 — +1 dé à pleine santé, Faible dès la 1ʳᵉ touche)* | +1 *(forfait, provisoire)* | Bande d'orques du Mordor · Bande d'orques du Morannon · **Meute de cavaliers wargs** |
| **Spéciale** (unité) | **[Relance 1]** *(badge universel depuis D073)* | +2 | Bande d'orques du Morannon · Bande d'uruk-hai · Troll du Mordor |
| **Élite** | **[Inébranlable 1] + Jamais Faible** *(enrichi D073)* | +2 | Bande d'uruk-hai uniquement |

**[Horde], nouvelle mouture (D075) : frappe fort, s'effondre vite.** Tant que l'unité n'a subi aucune touche, elle lance **+1 dé**. Dès la première touche encaissée, elle perd ce bonus **et** passe immédiatement en état **Faible** — ses faces Épée cessent de toucher, quel que soit le nombre de figurines restantes, pas seulement à la dernière. Une armée du Mordor qui domine les premiers échanges puis s'effrite d'un coup, sans palier intermédiaire.

**La règle s'étend désormais à la cavalerie.** La Meute de cavaliers wargs porte [Horde] à la place de son ancien badge Spéciale — la restriction historique « jamais la cavalerie » (D032) est levée pour ce cas (voir [[Regles_Speciales]] §Signatures). L'Uruk-hai (l'élite qui ne rompt pas) et les pisteurs (le tir) restent exclus, comme depuis l'origine.

---

## 2. Liste des troupes

| #   | Unité                      | Type       | Combat   | Classe           | Badges                                      | **Points** |
| --- | -------------------------- | ---------- | -------- | ---------------- | ------------------------------------------- | ---------- |
| 1   | Bande d'orques du Mordor   | Infanterie | Mêlée    | 🔵 *(reclassée)* | Faction                                     | **4**      |
| 2   | Bande d'orques du Morannon | Infanterie | Mêlée    | 🔵               | Faction + Spéciale                          | **5**      |
| 3   | Bande de pisteurs orques   | Infanterie | Distance | 🟢               | *(aucun)*                                   | **3**      |
| 4   | Meute de cavaliers wargs   | Cavalerie  | Mêlée    | 🔵               | **Faction** *(remplace Spéciale)*           | **6**      |
| 5   | Bande d'uruk-hai du Mordor | Infanterie | Mêlée    | 🔴               | Spéciale + Élite                            | **7**      |
| 6   | Troll du Mordor            | Créature   | Mêlée    | 🔴               | Spéciale *(+ Peur 1/Armure 1 intrinsèques)* | **7**      |

> 🎲 **Les deux bandes d'orques passent en classe 🔵 (3 dés).** Auparavant seule la bande du Morannon portait 3 dés ; la bande de base rejoint désormais la même classe. La différence entre les deux profils n'est plus dans les dés, mais dans le badge Spéciale (Morannon seul) — plus simple à lire, l'écart de qualité se voit au picto, pas au nombre de dés lancés.
>
> ⚠️ **Uruk-hai et Troll : +1 pt chacun** (6→7), effet de bord de la migration du badge Spéciale ([Férocité], 1 pt → [Relance 1], 2 pts). Aucun changement de contenu demandé pour ces deux profils ; la hausse est mécanique, pas un choix de design du jour.

---

## 3. Profils détaillés

### 1. Bande d'orques du Mordor

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Infanterie | Mêlée | 🔵 | 2 | 3 dés *(4 tant qu'aucune touche subie)* | — | 4 | **4** |

**Badges :** Faction ([Horde])

**Note narrative :** la piétaille de Sauron, jetée en masse contre les lignes. Terrifiante au premier contact (4 dés), elle rompt psychologiquement dès la première touche encaissée — non seulement elle retombe à 3 dés, mais ses figurines cessent de porter des coups francs (état Faible immédiat, [Horde] refondue D075). L'orque ne se lit pas au dé près : il se lit à la première estafilade.

> 🎲 **Note de calcul.** Brut = 15 (Inf 🔵 mêlée, reclassée) + [Horde] Faction (1) = 16 → round(16÷3)−1 = **4**.

---

### 2. Bande d'orques du Morannon

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Infanterie | Mêlée | 🔵 | 2 | 3 dés *(4 tant qu'aucune touche subie)* | — | 4 | **5** |

**Badges :** Faction ([Horde]) + Spéciale ([Relance 1])

**Note narrative :** les orques-soldats de la Porte Noire, plus disciplinés que la piétaille de base — même chair à canon au premier contact ([Horde]), mais une arme qui ne rate pas deux fois une fois la ligne rompue ([Relance 1]). Le seul profil du roster à distinguer la qualité de l'équipement par un badge plutôt que par la classe.

> 🎲 **Note de calcul.** Brut = 15 (Inf 🔵 mêlée) + [Horde] Faction (1) + [Relance 1] Spéciale (2) = 18 → round(18÷3)−1 = **5**.

---

### 3. Bande de pisteurs orques

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Infanterie | Distance | 🟢 | 2 | 2 dés | 4 | 4 | **3** |

**Badges :** *(aucun)*

**Note narrative :** les traqueurs à l'arc de la Terre de l'Ombre — des orques d'un genre plus fureteur, envoyés en avant pour flécher et harceler. Décroche après avoir tiré ([Mobilité 1] intrinsèque, gratuite, classe 🟢). Pas de [Horde] : la règle reste réservée à la mêlée et à la cavalerie de choc (D032, désormais étendue aux wargs par D075, mais toujours pas au tir).

---

### 4. Meute de cavaliers wargs

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Cavalerie | Mêlée | 🔵 | 3 | 3 dés *(4 tant qu'aucune touche subie)* | — | 3 | **6** |

**Badges :** Faction ([Horde])

**Note narrative :** des loups sauvages montés par des orques, qui déferlent en surnombre au premier contact puis s'égaillent dès qu'ils encaissent — [Horde] leur va aussi bien qu'à l'infanterie orque : la meute charge en masse, mord fort, puis se disperse à la première blessure sérieuse. Porte [Poursuite 2] intrinsèque comme toute cavalerie 🔵 de mêlée. Premier profil du roster à porter [Horde] hors infanterie — la restriction D032 (« jamais la cavalerie ») est levée pour ce cas (D075).

> 🎲 **Note de calcul.** Brut = 21 (Cav 🔵 mêlée) + [Horde] Faction (1) = 22 → round(22÷3)−1 = **6**.

---

### 5. Bande d'uruk-hai du Mordor

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Infanterie | Mêlée | 🔴 | 1 ou 2 | 4 dés *(constante)* | — | 4 | **7** |

**Badges :** Spéciale ([Relance 1]) + Élite ([Inébranlable 1] + Jamais Faible)

**Note narrative :** les grands Uruks noirs de Barad-dûr, la haute stature bréée par Sauron pour tenir là où la piétaille rompt. C'est **l'exception du roster** : pas de [Horde], une Attaque 4 **constante**, aucun effondrement au premier sang. [Armure 1] (mailles noires) vient gratuitement de la classe 🔴 ; [Relance 1] (badge Spéciale, ex-[Férocité]) traduit une arme qui ne rate pas deux fois ; [Inébranlable 1] + Jamais Faible (badge Élite) confirment mécaniquement ce que dit le texte depuis l'origine — « l'orque qui ne rompt pas », jusqu'à sa dernière figurine.

> 🎲 **Note de calcul.** Brut = 19 (Inf 🔴 mêlée, Armure 1 incluse) + [Relance 1] Spéciale (2) + Élite (2) = 23 → round(23÷3)−1 = **7**. Effet de bord de la migration du badge Spéciale ([Férocité], 1 pt → [Relance 1], 2 pts) — +1 pt sans changement de design demandé.

---

### 6. Troll du Mordor

| Type | Combat | Classe | Mouvement | Attaque | Portée | PV | **Points** |
|---|---|---|---|---|---|---|---|
| Créature | Mêlée | 🔴 | 2 | 4 dés | — | 4 | **7** |

**Badges :** Spéciale ([Relance 1])

**Intrinsèques du type Créature (D071) :** **[Armure 1]** + **[Peur 1]** *(chaque Arcane obtenue en attaque compte comme 1 Drapeau contre la cible)*, sans supplément de coût — plus besoin de les chiffrer, ce sont des traits du type lui-même.

**Note narrative :** un Olog-hai tiré des fosses de Gorgoroth, une masse de muscle et de fer dont la seule approche fait plier le courage des hommes ([Peur], trait de toute créature) et dont la peau épaisse encaisse ce que l'acier ne saurait percer ([Armure], idem). [Relance 1] (badge Spéciale, ex-[Férocité]) traduit un coup de massue qui ne rate pas deux fois — la même règle qu'il portait déjà avant la refonte P4 (D071), qui l'avait retirée puis la voit revenir sous un autre nom via la migration du badge Spéciale.

> 🎲 **Note de calcul.** Brut = Mvt 2 + PV 4 + Atk 4×3(12) + Relance 1 Spéciale(2) = 20 → round(20÷3)−1 = 6. **Prime de pièce signature assumée (+1)**, cohérente avec le traitement déjà appliqué à ce profil (D054) : coût final **7**. Effet de bord de la migration du badge Spéciale — +1 pt sans changement de design demandé aujourd'hui.

---

## 4. Récapitulatif des badges portés

| Badge | Unités qui le portent |
|---|---|
| **Faction** ([Horde]) | Bande d'orques du Mordor (1) · Bande d'orques du Morannon (2) · **Meute de cavaliers wargs (4)** |
| **Spéciale** ([Relance 1]) | Bande d'orques du Morannon (2) · Bande d'uruk-hai (5) · Troll du Mordor (6) |
| **Élite** ([Inébranlable 1] + Jamais Faible) | Bande d'uruk-hai (5) |
| **Aucun badge** | Bande de pisteurs orques (3) — tir, toujours exclu de Horde |

**Intrinsèques hors badges** : [Armure 1] (classe 🔴, sur Uruk-hai et Troll) · [Peur 1] (type Créature, sur Troll uniquement pour l'instant).

---

## 5. Points ouverts transverses

- **Coût de [Horde] (1, refondue D075)** — jamais testé sous cette forme (ni la précédente, ni celle-ci). L'entrée en état Faible immédiate est un vrai changement de comportement à la table : à surveiller en priorité au prochain playtest, en particulier si elle rend les bandes d'orques trop fragiles dès le premier échange.
- **Uruk-hai et Troll : hausse de +1 pt chacun**, effet de bord de la migration du badge Spéciale ([Férocité] 1 pt → [Relance 1] 2 pts) plutôt qu'un choix de design — voir avertissement §2. À surveiller si ça déséquilibre leur rapport qualité/prix face au reste du roster.
- **Meute de cavaliers wargs** : coût inchangé (6 pts) par le remplacement Spéciale→Faction (même coût brut, 1 pt dans les deux cas) — mais premier profil de cavalerie du projet à porter [Horde], comportement jamais testé à la table.
- **Intrinsèque Créature (Peur 1 + Armure 1)** — nouvelle règle transverse, appliquée au Troll seul dans ce projet. À vérifier à la re-expression du Mûmakil (Harad, P4/P5) qu'elle ne fait pas doublon avec ses règles bespoke existantes ([Howdah], [Inébranlable ∞]).
- **[Réception de charge]** reste sans porteur à Mordor (inchangé depuis la Passe 0).
- **Couche Leadership (Phase 2)** — dé-randomiser l'accès des héros à la face Arcane, hors scope de cette repasse.

---

*Version : 1.2 — Phase 1 — 2026-08-08. **Refonte de [Horde] (D075) et migration badges universels.** [Horde] gagne l'entrée en état Faible immédiate dès la première touche (plus seulement à la dernière figurine), coût 2→1 ; sa portée s'étend à la cavalerie — la Meute de cavaliers wargs l'adopte en badge Faction et perd son ancien badge Spéciale (coût inchangé, 6 pts). Les deux bandes d'orques passent en classe 🔵 (3 dés) ; seule la bande du Morannon garde le badge Spéciale, migré vers [Relance 1] (universel, D073) — [Férocité] disparaît entièrement du roster. Uruk-hai et Troll suivent la même migration Spéciale, +1 pt chacun (6→7) en effet de bord non demandé. Roster inchangé à 6 profils. Non testé — validation P7a.*

*Version : 1.1 — Phase 1 — 2026-08-08. **Élite ajouté à l'Uruk-hai** (oubli de la repasse initiale) : badge Élite ([Inébranlable 1]) en plus de Spéciale ([Férocité]). Coût inchangé (6 pts) — la compression absorbe le badge au même palier.*

*Version : 1.0 — Phase 1 — 2026-08-08. **Refonte P4 (D071) : re-expression complète sur la taxonomie visuelle et le système de badges.** [Horde] devient le badge Faction, nerfée (perd [Inébranlable 1], coût 3→2) ; [Férocité] devient le badge Spéciale. **[Peur X] et [Armure 1] rendues intrinsèques au type Créature** — transverse, s'appliquera au Mûmakil. Troll simplifié : perd [Relance 1], conserve la prime de pièce signature (+1). Meute de cavaliers wargs : hausse de coût non compensée (4→6 pts), assumée. Roster inchangé à 6 profils. Non testé — validation P7a.*
