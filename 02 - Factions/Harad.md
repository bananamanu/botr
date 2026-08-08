---
projet: "Batailles de la Terre du Milieu"
type: "faction"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-08-08"
tags: [BdTdM, "type/faction", "peuple/harad", "statut/brouillon"]
version: "1.0"
---

# Harad — Profils d'unités *(escorte + Pillards + Mûmakil)*

> **Objet de ce document (refonte P4, D078) — dernier des 6 rosters.** Re-expression complète du roster sur la taxonomie visuelle (classe × type × mode, [[Regles_Base]] §2.4) et la matrice de points ([[Regles_Points]] §2). Le fil conducteur déjà acté à la Passe 0 — **[Poison]** — devient le badge Faction, cohérent avec le pivot D073-D077 (chaque peuple garde une identité propre plutôt qu'un miroir mécanique). Roster élargi : deux nouveaux profils de **Pillards haradrim**, cavalerie légère de raid, mêlée et tir.
>
> **Terminologie mise à jour** (héritée d'un roster jamais retouché depuis le Playtest #2) : [Arme Lourde 1] → [Relance 1] (D066, badge Spéciale universel) ; [Inamovible] → [Inébranlable ∞] (D062).
>
> **Mûmakil inchangé dans ses règles bespoke** (charge, Furie, Howdah — spécifiées par Emmanuel le 2026-07-27, D054), mais bénéficie désormais des **intrinsèques du type Créature** ([Armure 1] + [Peur 1], D071) sans supplément de coût — vérifié sans redondance avec [Howdah]/[Inébranlable ∞] (aucun chevauchement : l'un est une plateforme de tir, l'autre une immunité au recul).
>
> Aligné sur [[Regles_Base]] v0.12 et [[Regles_Speciales]] v0.25, [[Regles_Points]] v0.22.

---

## 1. Les deux badges du Harad

| Badge | Effet | Coût brut | Porté par |
|---|---|---|---|
| **Faction** (Harad) | **[Poison]** | +1 | **Toutes les unités du roster, escorte et Pillards** |
| **Spéciale** (unité) | **[Relance 1]** | +2 | Gardes serpent à cheval · Pillards haradrim (mêlée) |
| **Élite** | **[Inébranlable 1] + Jamais Faible** | +2 | Gardes serpents uniquement |

**[Poison] reste le fil conducteur du peuple**, inchangé depuis la Passe 0 : chaque Couronne obtenue en attaque inflige une touche supplémentaire — flèches et lames haradrim également enduites du même venin. Devenu badge Faction plutôt que règle assignée profil par profil, il couvre désormais **tout le roster sans exception**, escorte comme Mûmakil (via [Howdah]).

---

## 2. Liste des troupes

| # | Unité | Type | Combat | Classe | Badges | **Points** |
|---|---|---|---|---|---|---|
| 1 | Archers du Harad | Infanterie | Distance | 🟢 | Faction | **3** |
| 2 | Lanciers du Harad | Infanterie | Mêlée | 🟢 | Faction | **3** |
| 3 | Gardes serpents | Infanterie | Mêlée | 🔵 | Faction + Élite | **5** |
| 4 | Gardes serpent à cheval | Cavalerie | Mêlée | 🔵 | Faction + Spéciale | **7** |
| 5 | **Pillards haradrim (mêlée)** — *nouveau* | Cavalerie | Mêlée | 🟢 | Faction + Spéciale | **6** |
| 6 | **Pillards haradrim (archers)** — *nouveau* | Cavalerie | Distance | 🟢 | Faction | **4** |
| 7 | Mûmakil | Créature | Mêlée *(charge)* | 🔴 *(nominal)* | *(hors matrice — voir §4)* | **21** |

**Total escorte + Pillards : 28 points** (hors Mûmakil, hors matrice par équivalence).

> 🎲 **Note de design — deux paires, deux rôles.** L'escorte au sol (Lanciers → Gardes serpents) et la cavalerie légère (Pillards) se répondent : les Lanciers/Gardes serpents tiennent la formation autour de la bête (infanterie, classes 🟢→🔵) ; les Pillards raident en périphérie (cavalerie légère 🟢, mobilité intrinsèque gratuite en tir). Les Gardes serpent à cheval (🔵) restent la seule cavalerie « lourde » du peuple — Spéciale ([Relance 1]) marque une arme de meilleure qualité que celle des Pillards, malgré la même classe de dés que ces derniers en mêlée.

---

## 3. Profils détaillés

### 1. Archers du Harad

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Infanterie | Distance | 🟢 | 2 | 2 dés | 4 | 4 | **3** |

**Badges :** Faction ([Poison])

**Note narrative :** les archers du désert, flèches traitées au venin — le fil conducteur du peuple porté par sa forme la plus ancienne. Décroche après avoir tiré ([Mobilité 1] intrinsèque, gratuite, classe 🟢).

> 🎲 **Note de calcul.** Brut = 11 (Inf 🟢 distance) + [Poison] Faction (1) = 12 → round(12÷3)−1 = **3**.

---

### 2. Lanciers du Harad

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Infanterie | Mêlée | 🟢 | 2 | 2 dés | — | 4 | **3** |

**Badges :** Faction ([Poison])

**Note narrative :** l'escorte au sol du Mûmakil, lances enduites du même poison que les archers — la piétaille légère qui referme la marche autour de la bête. Perd son ancienne [Réception de charge] (coupée du système entier depuis P2, sans remplacement) : reste une ligne légère, pas un mur anti-charge au sens mécanique.

> 🎲 **Note de calcul.** Brut = 12 (Inf 🟢 mêlée) + [Poison] Faction (1) = 13 → round(13÷3)−1 = **3**.

---

### 3. Gardes serpents

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Infanterie | Mêlée | 🔵 | 2 | 3 dés | — | 4 | **5** |

**Badges :** Faction ([Poison]) + Élite ([Inébranlable 1] + Jamais Faible)

**Note narrative :** la garde d'élite du Harad, lames traitées au venin, formée pour tenir le contact plutôt que le harceler — l'échelon au-dessus des Lanciers (classe 🔵 contre 🟢), et la seule unité du roster à porter le badge Élite : ce sont eux qui referment le dernier cercle autour de la bête quand la ligne plie.

> 🎲 **Note de calcul.** Brut = 15 (Inf 🔵 mêlée) + [Poison] Faction (1) + Élite (2) = 18 → round(18÷3)−1 = **5**.

---

### 4. Gardes serpent à cheval

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Cavalerie | Mêlée | 🔵 | 3 | 3 dés | — | 3 | **7** |

**Badges :** Faction ([Poison]) + Spéciale ([Relance 1])

**Note narrative :** la version montée des Gardes serpents — une arme qui ne rate pas deux fois ([Relance 1], ex-[Arme Lourde 1]) plutôt que le statut Élite de leurs homologues à pied, cohérent avec une cavalerie qui frappe et poursuit plutôt qu'elle n'encaisse en formation. Porte [Poursuite 2] intrinsèque comme toute cavalerie 🔵 de mêlée. Poison conservé : même venin, porté à cheval.

> 🎲 **Note de calcul.** Brut = 21 (Cav 🔵 mêlée) + [Poison] Faction (1) + [Relance 1] Spéciale (2) = 24 → round(24÷3)−1 = **7**.

---

### 5. Pillards haradrim (mêlée) — *nouveau profil*

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Cavalerie | Mêlée | 🟢 | 4 | 2 dés | — | 3 | **6** |

**Badges :** Faction ([Poison]) + Spéciale ([Relance 1])

**Note narrative :** des raiders montés du désert, lames empoisonnées et armes de jet légères — la mobilité avant tout (classe légère, la plus rapide du roster : 4 cases + combat). [Relance 1] marque une arme qui frappe deux fois plutôt qu'une, malgré le faible gabarit de la monture. Porte [Poursuite 2] intrinsèque comme toute cavalerie légère de mêlée.

> 🎲 **Note de calcul.** Brut = 19 (Cav 🟢 mêlée) + [Poison] Faction (1) + [Relance 1] Spéciale (2) = 22 → round(22÷3)−1 = **6**.

---

### 6. Pillards haradrim (archers) — *nouveau profil*

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Cavalerie | Distance | 🟢 | 4 | 2 dés | 4 | 3 | **4** |

**Badges :** Faction ([Poison])

**Note narrative :** la version tir des Pillards — harcèlement à cheval, flèches empoisonnées tirées puis décrochage immédiat ([Mobilité 2] intrinsèque, cavalerie légère de tir, gratuite). Pas de badge Spéciale : le venin suffit à porter l'identité, l'arc reste standard.

> 🎲 **Note de calcul.** Brut = 13 (Cav 🟢 distance, [Mobilité 2] incluse) + [Poison] Faction (1) = 14 → round(14÷3)−1 = **4**.

---

### 7. Mûmakil — *pièce unique, spécifiée par Emmanuel (2026-07-27, D054)*

| Type | Combat | Classe | Mouvement | Attaque | Portée | PV | **Points** |
|---|---|---|---|---|---|---|---|
| Créature | Mêlée *(par charge)* | 🔴 *(nominal)* | 2 *(translation 1-2-1)* | 4 dés *(charge)* / 2 dés *(tir)* | 1–3 *(tir)* | 6 | **21** |

**Règles spéciales :** [Charge écrasante] *(bespoke)* · [Howdah] *(= [Plateforme de tir 2] + [Poison])* · [Inébranlable ∞] *(ex-[Inamovible])* · [Bête incontrôlable] *(bespoke, Furie)*

**Intrinsèques du type Créature (D071) :** **[Armure 1]** + **[Peur 1]**, sans supplément de coût — vérifié sans redondance avec les règles bespoke ci-dessus : [Howdah] est une plateforme de tir (aucun chevauchement avec l'armure), [Inébranlable ∞] porte sur le recul (aucun chevauchement avec la peur, qui inflige des Drapeaux via l'Arcane plutôt que d'agir sur la résistance au recul elle-même).

**Occupation :** 4 hexagones en colonne **1–2–1**. **Pas de pivot** : le gabarit reste toujours orienté pointe vers le haut, son déplacement est une **translation pure**. **Direction de translation : libre** (Emmanuel, D058).

**Coût : 21 points, par équivalence d'impact (D054)** — le système additif atteint sa limite sur une pièce hors norme. Analyse d'équivalence (dé uniforme B4) : ≈3,3 figurines par unité d'infanterie traversée lors d'une charge, sans contre-attaque possible ; ≈2 figurines sur 3 contre la cavalerie, avec recul doublé. Équivalence retenue : **3 × Éored de cavalier du Rohan (7 pts) = 21 pts**. Inchangé malgré le gain gratuit d'[Armure 1]/[Peur 1] (D071) — **point de veille**, voir §5.

#### [Charge écrasante] *(bespoke)*

> À son activation, le Mûmakil **DOIT** effectuer un déplacement complet de **2 hexagones** (1 + 1) vers l'hexagone de tête visé, **sans tenir compte** des figurines présentes. Chaque unité dont un hexagone est traversé subit une **attaque de 4 dés** où la **Couronne inflige aussi une touche** ; cela se passe **en phase de mouvement — pas de combat, aucune contre-attaque**. Toute **cavalerie** repoussée recule du **double**. S'il reste des unités gênantes non détruites/repoussées, il s'arrête au dernier hexagone libre. **Aucune attaque de mêlée en phase d'attaque.**

#### [Bête incontrôlable] *(bespoke)*

> À son activation, **s'il est blessé** : lancez autant de dés que ses **PV restants** ; **sans aucune Couronne**, posez un marqueur **Furie** — l'adversaire dirige immédiatement son déplacement et peut l'activer comme une de ses figurines tant que la Furie tient. À la **fin de chaque tour**, le camp du Mal relance **(PV restants + 1)** dés : une **Couronne** retire la Furie.

#### [Howdah]

> **[Howdah] = [Plateforme de tir 2] + [Poison]** : une attaque de tir de **2 dés**, portée **1–3**, en plus de la mêlée, bénéficiant de [Poison].

---

## 4. Récapitulatif des badges portés

| Badge | Unités qui le portent |
|---|---|
| **Faction** ([Poison]) | **Toutes les unités (1 à 6), sans exception** — plus le Mûmakil via [Howdah] |
| **Spéciale** ([Relance 1]) | Gardes serpent à cheval (4) · Pillards haradrim mêlée (5) |
| **Élite** ([Inébranlable 1] + Jamais Faible) | Gardes serpents (3) uniquement |

**Hors badges (Mûmakil)** : [Charge écrasante], [Bête incontrôlable] — bespoke, non transférables.

---

## 5. Points ouverts transverses

- **Coût de [Poison] en badge Faction (1, forfait)** — jamais testé sous cette forme généralisée à tout le roster (auparavant assignée profil par profil). À surveiller comme tout badge Faction nouvellement créé.
- **Gain gratuit d'[Armure 1]/[Peur 1] sur le Mûmakil (D071)** sans repricing — la pièce est mécaniquement plus dure à tuer et plus effrayante qu'au moment où les 21 pts ont été fixés (D054, avant l'intrinsèque Créature). Le chiffrage par équivalence absorbe mal ce genre d'ajout transverse ; à réévaluer explicitement au playtest de validation (P7a) plutôt que par calcul.
- **Gardes serpent à cheval (7 pts) vs Pillards mêlée (6 pts)** — écart d'1 pt pour Élite-vs-Spéciale sur classe différente (🔵 vs 🟢) : à confirmer que l'écart de puissance perçu à la table correspond à l'écart de prix.
- **[Réception de charge]** reste coupée du système entier (inchangé depuis P2, D062) — plus aucun porteur nulle part dans le projet.
- **Furie du Mûmakil** — refonte complète prévue en P5 (jugée trop punitive au Playtest #2, point noir identifié). Ce document ne la retouche pas.

---

*Version : 1.0 — Phase 1 — 2026-08-08. **Refonte P4 (D078) : première re-expression complète du roster Harad, sixième et dernier peuple.** Badge Faction = [Poison] (fil conducteur déjà acté, désormais universel sur tout le roster) ; Badge Spéciale = [Relance 1] (ex-[Arme Lourde 1], Gardes serpent à cheval) ; Badge Élite = [Inébranlable 1] + Jamais Faible (Gardes serpents). **Deux nouveaux profils : Pillards haradrim**, cavalerie légère 🟢 de raid, en version mêlée (Faction+Spéciale, 6 pts) et tir (Faction seule, 4 pts). Escorte reclassée sur la taxonomie (Archers/Lanciers 🟢, Gardes serpents/à cheval 🔵) ; [Réception de charge] et l'ancienne valeur X d'[Arme Lourde 1] abandonnées avec le reste du système pré-taxonomie. Mûmakil : règles bespoke inchangées, terminologie mise à jour ([Inamovible]→[Inébranlable ∞]), gagne [Armure 1]/[Peur 1] intrinsèques (D071) sans repricing — point de veille signalé. Roster porté à 6 profils + Mûmakil. Non testé — validation P7a. **Sixième et dernier roster du sprint P4 : le mandat de re-expression est complet.***

*Version : 0.4 — Phase 1 — 2026-07-29. **Roster d'escorte complété (D058)** : Lanciers du Harad passés à 2 dés + [Poison] + [Réception de charge] (5 pts, inchangé) ; deux nouveaux profils, **Gardes serpents** (Infanterie, 3 dés + [Poison] + [Réception de charge], 6 pts) et **Gardes serpent à cheval** (Cavalerie, 3 dés + [Poison] + [Arme Lourde 1], 5 pts). [Réception de charge] refondue en bonus de contre-attaque inconditionnel dans [[Regles_Speciales]] (répercuté depuis Gondor/Easterling). Direction de translation du gabarit tranchée en « libre » (voir `[[Playtest2_La_grande_bete]]`). Roster d'escorte à 4 profils, non testé.*

*Version : 0.3 — Phase 1 — 2026-07-27. Mûmakil chiffré à **21 pts par équivalence d'impact** (≈ 3 Éored, D054) ; rulings tranchés ; D10 (pas de pivot, translation pure) intégré ; B4 adopté comme règle générale de dégâts (`Regles_Base` §2.3, D053). Édits glossaire répercutés ([Charge écrasante]/[Bête incontrôlable] refondues, [Inamovible] créée à 3 pts). Escorte en attente des profils d'Emmanuel.*

*Version : 0.2 — Phase 1 — 2026-07-27. Ajout du profil complet du Mûmakil (spécifié par Emmanuel) : occupation 1-2-1, Créature Mvt 2 / 4 dés / PV 6, refonte de [Charge écrasante] (impact dédié en phase de mouvement) et de [Bête incontrôlable] (Furie), nouvelle règle [Inamovible], [Howdah] confirmé. Coût provisoire 8 pts, forfaits et rulings à arbitrer. Escorte inchangée. À valider — non testé.*
