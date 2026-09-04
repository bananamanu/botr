---
projet: "Batailles de la Terre du Milieu"
type: "faction"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-08-30"
tags: [BdTdM, "type/faction", "peuple/mordor", "statut/brouillon"]
version: "1.9"
---

# Mordor — Profils d'unités

> **Objet de ce document (P8 — simplification radicale D101/D102, [Horde] troisième version D105, refonte défense créature D103).** Même principe que les autres peuples : plus aucun badge d'office. [Horde] devient une **option**, disponible sur tous les orques (bandes, Uruk-hai, wargs, et la nouvelle **Piétaille orque du Mordor** — troupe légère supplémentaire, voir §2). Nouvelle version de [Horde] : +1 dé et [Inébranlable 1] à pleine santé seulement, **sans effet négatif** ensuite (contrairement aux versions précédentes). Le Roi-Sorcier et le Troll adoptent la nouvelle règle **[Armure]** (défense unifiée des Créatures, D103).
>
> Aligné sur [[Regles_Base]] v0.17, [[Regles_Speciales]] v0.31, [[Regles_Points]] v0.30.

---

## 1. Faction de Mordor — [Horde] *(troisième version, D105)*

> Tant que l'unité est à **pleine santé**, elle porte **+1 dé de combat** et **[Inébranlable 1]**. Dès la première perte, ces effets disparaissent — sans aucune pénalité en contrepartie.

**Outil optionnel**, +3 brut, disponible sur tous les orques (voir tableau §2).

**Bannière** : [Inébranlable 1], +2 brut, disponible sur les formations organisées (pas les pisteurs, tireurs isolés).

---

## 2. Liste des troupes (coûts de base — sans option)

| # | Unité | Type | Combat | Classe | Options disponibles | **Points** |
|---|---|---|---|---|---|---|
| 1 | Bande d'orques du Mordor | Infanterie | Mêlée | 🔵 | Horde, Bannière | **4** |
| 2 | Bande d'orques du Morannon | Infanterie | Mêlée | 🔵 | Horde, Bannière | **4** |

> 🎲 **Cases comblées (D124).** Bande d'orques 🔵 (Mordor ou Morannon, brut 15) : **+ [Horde]** = 16 → **4** *(absorbé, gratuit)* · **+ Bannière** = 17 → **5** · **+ [Horde] + Bannière** = 18 → **5**. La combinaison des deux badges ne coûte donc rien de plus que la Bannière seule.
| 3 | **Piétaille orque du Mordor** — *nouveau* | Infanterie | Mêlée | 🟢 | Horde, Bannière | **3** |
| 4 | Bande de pisteurs orques | Infanterie | Distance | 🟢 | *(aucune)* | **3** |
| 5 | Meute de cavaliers wargs | Cavalerie | Mêlée | 🔵 | Horde, Bannière | **6** |
| 6 | Bande d'uruk-hai du Mordor | Infanterie | Mêlée | 🔴 | Horde, Bannière | **5** |
| 7 | Troll du Mordor — *signature* | Créature | Mêlée | 🔴 | *(hors matrice, voir §3)* | **7** |
| 8 | Roi-Sorcier sur l'ombre ailée — *signature* | Créature | Mêlée | 🔴 *(nominal)* | *(hors matrice, voir §4)* | **10** *(17 avec Général/Destin)* |

**Coûts avec option Horde (+3 brut) :**

| # | Unité | Base | +Horde |
|---|---|---|---|
| 1 | Bande d'orques du Mordor | 4 | **5** |
| 2 | Bande d'orques du Morannon | 4 | **5** |
| 3 | Piétaille orque du Mordor | 3 | **4** |
| 5 | Meute de cavaliers wargs | 6 | **7** |
| 6 | Bande d'uruk-hai | 5 | **6** |

> 🎲 **Nouvelle unité : « Piétaille orque du Mordor » (D106).** Orques légers, classe 🟢, moins bien équipés que les bandes existantes (🔵), pour donner du volume bon marché au roster. **Nom validé (D113)** — les alternatives envisagées (« Racaille orque », « Traînards du Mordor ») sont écartées.
>
> 🔄 **Baisses par rapport à l'ancien roster.** Bande d'orques du Morannon perd son [Relance 1] par défaut (5→**4**, identique à la Bande du Mordor — coïncidence de coût acceptée, cf. précédents du projet). Uruk-hai perd [Inébranlable 1]+JF par défaut (6→**5**).

---

## 3. Troll du Mordor — pièce signature *(inchangé sauf défense, D103)*

| Type | Combat | Classe | Mouvement | Attaque | PV | **Points** |
|---|---|---|---|---|---|---|
| Créature | Mêlée | 🔴 | 2 | 4 dés | 4 | **7** |

**Règles :** **[Relance 1]** (fixe, signature — le coup de massue qui ne rate pas deux fois).

**Défense (D103) :** **[Armure]** (sans X) — jet de sauvetage 1d6 contre chaque touche reçue, annulée sur Arcane. Remplace l'ancien [Armure 1] intrinsèque (mécanique différente, valeur équivalente). Intrinsèque, gratuit — comme avant.

**Chiffrage (inchangé) :** brut = 2 (Mvt) + 4 (PV) + 12 (Atk 4×3) + 2 (Relance 1) = 20 → round(20÷3)−1 = 6, **+1 prime de pièce signature** = **7**.

---

## 4. Roi-Sorcier sur l'ombre ailée — pièce signature *(D095/D099, défense mise à jour D103)*

| Type | Combat | Classe | Mouvement | Attaque | PV | **Points** |
|---|---|---|---|---|---|---|
| Créature | Mêlée | 🔴 *(nominal)* | [Vol] 4 cases *(ignore les figurines)* | 4 dés | 6 | **10** *(base)* / **17** *(avec Général+Destin 4, forme jouée au Pelennor)* |

**Règles :** [Terreur] (Arcane = 2 Drapeaux) · [Vigilant] (jamais contre-attaqué) · [Vol] (bespoke, 4 cases, ignore les figurines).

**Défense (D103) :** **[Armure]** — même refonte que le Troll et le Mûmakil, remplace l'ancien [Armure 1] intrinsèque. Aucun changement de coût (déjà gratuit).

**Chiffrage (inchangé) :**

| Élément | Brut |
|---|---|
| Socle (Mvt 4 + PV 6) | 10 |
| Attaque (4 dés mêlée, D=3) | 12 |
| [Terreur] *(excédent sur [Peur 1] gratuit)* | 2 |
| [Vigilant] | 2 |
| [Vol] *(bespoke)* | 8 |
| **Sous-total** | **34** |
| **Final = round(34÷3)−1** | **10** |

**Avec Général (universel) + Destin 4** : brut = 34 + 4 + 9 + 8 = 55 → round(55÷3)−1 = **17**.

> 🎲 **17 pts — sommet du projet, au-dessus du Mûmakil (15), confirmé (D112).** Le prix est assumé : pas de plafonnement des pièces bespoke. Le chef des Nazgûl est la pièce la plus dangereuse du Pelennor.

---

## 5. Variante avec Leader — Uruk-hai

**Bande d'uruk-hai avec Gothmog** (Général non-universel, Destin 2, sans Horde — Gothmog mène une élite, pas une masse) : brut = 19 (base) + 4 (Leader) + 9 (Général) + 4 (Destin 2) = 36 → round(36÷3)−1 = **11**.

---

## 6. Récapitulatif

| Option | Disponible sur |
|---|---|
| **Faction [Horde]** *(troisième version)* | 1, 2, 3, 5, 6 |
| **Bannière** | 1, 2, 3, 5, 6 |
| **Signature, hors matrice** | Troll (7) · Roi-Sorcier (8) |
| **Leader/Général/Destin** | Gothmog (Uruk-hai) · Roi-Sorcier au Pelennor |

---

## 7. Points ouverts transverses

- ~~**Nom de la Piétaille orque du Mordor**~~ — **validé (D113)**, nom définitif.
- ~~**Roi-Sorcier à 17 pts avec Général**~~ — **confirmé (D112)**, sommet assumé sans plafonnement.
- **[Horde] v3 jamais testée** — la disparition de l'effet négatif change nettement le ressenti par rapport aux deux versions précédentes, à surveiller au prochain playtest.

---

*Version : 1.9 — Phase 1 — 2026-08-30. **D124 — cases de coût comblées.** Les combinaisons de badges sur les bandes d'orques 🔵 sont explicitées : [Horde] seul est absorbé (4), Bannière seule coûte +1 (5), et [Horde] + Bannière ne coûte pas plus que la Bannière seule (5). Ces cases manquaient et faussaient le chiffrage du Pelennor, où le Morannon avait été surévalué d'un point par unité.*

*Version : 1.8 — Phase 1 — 2026-08-30. **P9 — clôture des points ouverts du roster (D112/D113).** Nom « Piétaille orque du Mordor » validé sans modification (D113) ; la note de proposition devient une note d'entérinement et corrige au passage un renvoi erroné à D105 (la nouvelle unité est D106, D105 étant [Horde] v3). Roi-Sorcier confirmé à 17 pts (D112) : l'avertissement ⚠️ devient une note 🎲, le sommet tarifaire est assumé sans plafonnement des pièces bespoke. §7 : les deux points ouverts correspondants passent en résolus ; seul reste **[Horde] v3 jamais testée**, à surveiller au Playtest #5 du 12 septembre. Aucun coût modifié, aucun profil touché.*

*Version : 1.7 — Phase 1 — 2026-08-23. **Simplification radicale généralisée (D101/D102) + [Horde] troisième version (D105) + nouvelle unité + refonte défense créature (D103).** Plus aucun badge par défaut : Horde et Bannière deviennent des options, disponibles sur tous les orques. [Horde] réécrite : +1 dé et Inébranlable 1 à pleine santé, plus d'effet négatif (+3 brut). Nouvelle unité **Piétaille orque du Mordor** (Inf 🟢 mêlée, **3** pts base, nom à valider). Troll et Roi-Sorcier passent à la nouvelle règle [Armure] (D103) — coûts inchangés (7 et 10/17). Variante Gothmog recalculée : **11** pts (perd Inébranlable+JF par défaut).*

*Version : 1.6 — Phase 1 — 2026-08-23. **P8 — recalcul complet (D097/D098) + intégration du Roi-Sorcier (D099).** [Horde] confirmée trait matériel sur les bandes d'orques et la Meute de wargs (coûts inchangés), retirée de l'Uruk-hai (identité plus nette élite vs masse). Roi-Sorcier intégré au roster (§3, nouveau) : **10** pts en profil nu, **17** pts en version Général/Destin 4 jouée au Pelennor — nouveau sommet du projet, signalé comme point ouvert. Variante Gothmog chiffrée (Uruk-hai, **12** pts).*

*Version : 1.4 — Phase 1 — 2026-08-16. **Corrections de relecture — revue de finalisation « Verrouillage v1.0 ».** En-tête « Aligné sur » rafraîchi (v0.12/v0.24/v0.21 → v0.13/v0.27/v0.24, versions réelles depuis P7c). Aucune décision mécanique — pas de numéro D.*

*Version : 1.3 — Phase 1 — 2026-08-13. **Collapse du système de badges (D080/D081, tâche P7c).** [Horde] devient un trait de Faction porté par toute l'infanterie de mêlée, **Uruk-hai compris** (auparavant exception explicite, D035) ; reste exclu : pisteurs orques (tir) et Troll (Créature). Plafond à 1 badge secondaire : Uruk-hai perd Spéciale, garde Élite (neutralise la pénalité Faible de Horde) — coût 7→**6 pts**. Récapitulatif (§4) et points ouverts (§5) mis à jour.*

*Version : 1.2 — Phase 1 — 2026-08-08. **Refonte de [Horde] (D075) et migration badges universels.** [Horde] gagne l'entrée en état Faible immédiate dès la première touche (plus seulement à la dernière figurine), coût 2→1 ; sa portée s'étend à la cavalerie — la Meute de cavaliers wargs l'adopte en badge Faction et perd son ancien badge Spéciale (coût inchangé, 6 pts). Les deux bandes d'orques passent en classe 🔵 (3 dés) ; seule la bande du Morannon garde le badge Spéciale, migré vers [Relance 1] (universel, D073) — [Férocité] disparaît entièrement du roster. Uruk-hai et Troll suivent la même migration Spéciale, +1 pt chacun (6→7) en effet de bord non demandé. Roster inchangé à 6 profils. Non testé — validation P7a.*

*Version : 1.1 — Phase 1 — 2026-08-08. **Élite ajouté à l'Uruk-hai** (oubli de la repasse initiale) : badge Élite ([Inébranlable 1]) en plus de Spéciale ([Férocité]). Coût inchangé (6 pts) — la compression absorbe le badge au même palier.*

*Version : 1.0 — Phase 1 — 2026-08-08. **Refonte P4 (D071) : re-expression complète sur la taxonomie visuelle et le système de badges.** [Horde] devient le badge Faction, nerfée (perd [Inébranlable 1], coût 3→2) ; [Férocité] devient le badge Spéciale. **[Peur X] et [Armure 1] rendues intrinsèques au type Créature** — transverse, s'appliquera au Mûmakil. Troll simplifié : perd [Relance 1], conserve la prime de pièce signature (+1). Meute de cavaliers wargs : hausse de coût non compensée (4→6 pts), assumée. Roster inchangé à 6 profils. Non testé — validation P7a.*
