---
projet: "Batailles de la Terre du Milieu"
type: "faction"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-08-23"
tags: [BdTdM, "type/faction", "peuple/khand", "statut/brouillon"]
version: "2.7"
---

# Khand — Profils d'unités

> **Objet de ce document (P8 — simplification radicale, D101/D102, retouches D108).** Même principe qu'à Gondor : plus aucun badge d'office. [Mercenaire] devient une option (D102). **Retouche Emmanuel (D108) : Khand ne porte jamais de Bannière** — troupes disparates, sans étendard commun. En contrepartie, l'Aurige de Khand (le char) gagne une signature bespoke : **[Peur 1 contre les bannières vertes]**.
>
> Aligné sur [[Regles_Base]] v0.17, [[Regles_Speciales]] v0.31, [[Regles_Points]] v0.30.

---

## 1. Faction de Khand — [Mercenaire]

Retrait forcé compte double. **Outil optionnel, coût négatif** : **−2 brut**. Disponible sur tout le roster sauf l'Aurige.

**Bannière : jamais disponible chez Khand** (D108).

---

## 2. Liste des troupes (coûts de base — sans option)

| # | Unité | Type | Combat | Classe | Options disponibles | **Points** |
|---|---|---|---|---|---|---|
| 1 | Mercenaire de Khand | Infanterie | Mêlée | 🟢 | Faction | **3** |
| 2 | Mercenaire archer de Khand | Infanterie | Distance | 🟢 | Faction | **3** |
| 3 | Pillards de Khand (hache) | Cavalerie | Mêlée | 🟢 | Faction | **5** |
| 4 | Pillards de Khand (archer) | Cavalerie | Distance | 🟢 | Faction | **3** |
| 5 | Aurige de Khand | Cavalerie | Mêlée | 🔵 | *(signature, voir §3)* | **7** |

**Coûts avec option Mercenaire (−2 brut) :**

| # | Unité | Base | +Faction [Mercenaire] |
|---|---|---|---|
| 1 | Mercenaire de Khand | 3 | **2** |
| 2 | Mercenaire archer | 3 | **2** |
| 3 | Pillards (hache) | 5 | **4** |
| 4 | Pillards (archer) | 3 | **2** |

---

## 3. Aurige de Khand — signature *(D108)*

Cavalerie, Mêlée, 🔵. **[Peur 1 contre les bannières vertes]** (voir [[Regles_Speciales]]) — le fracas du char devant des troupes légères peu aguerries.

**Chiffrage :** brut = 21 (base) + 2 ([Peur 1 vs 🟢], bespoke) = 23 → round(23÷3)−1 = **7**.

---

## 4. Variante avec Leader — Playtest #4

**Aurige de Khand avec le Roi de Khand** (Leader, Destin 2) : brut = 23 (base+signature) + 4 (Leader) + 4 (Destin 2) = 31 → round(31÷3)−1 = **9**.

---

## 5. Récapitulatif

| Option | Disponible sur |
|---|---|
| **Faction [Mercenaire]** *(coût négatif)* | 1, 2, 3, 4 — jamais l'Aurige (5) |
| **Bannière** | Jamais (D108) |
| **Signature bespoke** | Aurige : [Peur 1 contre les bannières vertes] |
| **Leader/Destin** | Aurige avec le Roi de Khand au Pelennor |

---

## 6. Points ouverts transverses

- **[Peur 1 contre les bannières vertes], tarif +2 non testé** — à confirmer au playtest : est-ce trop fort face à un roster où les classes 🟢 dominent (Harad, Khand lui-même en miroir), ou trop anecdotique face à des rosters à dominante 🔵/🔴 ?

---

*Version : 2.7 — Phase 1 — 2026-08-23. **Retouches Emmanuel (D108).** Bannière retirée définitivement du roster (jamais disponible chez Khand). Aurige de Khand devient une pièce signature avec la nouvelle règle bespoke [Peur 1 contre les bannières vertes] (+2 brut) — coût de base 6→**7**. Variante avec le Roi de Khand recalculée : **9** pts (inchangé par coïncidence).*

*Version : 2.6 — Phase 1 — 2026-08-23. **Simplification radicale généralisée (D101).** [Mercenaire] devient une option (coût négatif, −2 brut) plutôt qu'un trait automatique — même logique que Gondor, étendue aux traits matériels sur validation d'Emmanuel. Coûts de base recalculés en pure matrice. Nouvelle variante : Aurige avec le Roi de Khand = **9** pts.*

*Version : 2.5 — Phase 1 — 2026-08-23. **P8 — recalcul complet (D097/D098).** [Mercenaire] confirmé trait matériel, aucun changement de coût de base — seul roster du projet totalement inchangé par le ciblage. Nouvelle variante chiffrée : Aurige avec le Roi de Khand (Leader, Destin 2) = **9** pts. Ancien badge Spéciale renommé « règle socle ».*

*Version : 2.3 — Phase 1 — 2026-08-16. **Corrections de relecture — revue de finalisation « Verrouillage v1.0 ».** En-tête « Aligné sur » rafraîchi (v0.12/v0.24/v0.21 → v0.13/v0.27/v0.24, versions réelles depuis P7c). Aucune décision mécanique — pas de numéro D.*

*Version : 2.2 — Phase 1 — 2026-08-13. **Collapse du système de badges (D080/D081, tâche P7c) — sans effet sur les coûts.** Khand était déjà conforme (D076) : [Mercenaire] devient un trait de peuple plutôt qu'un badge, présentation seule mise à jour (§1, §2). Aucun changement de points.*

*Version : 2.1 — Phase 1 — 2026-08-08. **Revue de conformité au pivot « badges universels » (D073-D075) — D076.** Aucun changement de badge ni de coût : [Mercenaire] reste le badge Faction (identité propre, l'exclusion de l'Aurige est le point de la règle, pas un oubli à corriger) ; [Relance 1] est déjà le badge Spéciale depuis D070. Roster confirmé conforme sans modification.*

*Version : 2.0 — Phase 1 — 2026-08-08. **Refonte P4 (D070) : repositionnement complet d'identité — Khand devient une faction mercenaire à moral fragile.** Système à deux badges : **Faction** = [Mercenaire] (premier badge à coût négatif du projet, −2 brut, chaque retrait forcé compte double) · **Spéciale** = [Relance 1] (hache lourde, inchangée). **Abandon du type Chars** : l'Aurige de Khand devient cavalerie 🔵 standard (badge Spéciale seul, pas de Faction — seul corps régulier du peuple), perd son statut Jamais Faible et ses règles bespoke ([Poursuite 1]/[Plateforme de tir 2], D045/D046). Roster inchangé à 5 profils, tous en classe 🟢 sauf l'Aurige. Non testé — validation P7a.*
