---
projet: "Batailles de la Terre du Milieu"
type: "faction"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-08-13"
tags: [BdTdM, "type/faction", "peuple/khand", "statut/brouillon"]
version: "2.2"
---

# Khand — Profils d'unités

> **Objet de ce document (refonte P4, D070 ; confirmé conforme au système « badges universels », D076).** Re-expression complète du roster sur la taxonomie visuelle (classe × type × mode, [[Regles_Base]] §2.4) et la matrice de points ([[Regles_Points]] §2). Repositionnement d'identité complet par rapport aux versions précédentes : Khand n'est plus « le peuple sans armure qui frappe à la hache » avec une pièce signature (l'Aurige, char de choc puis char-plateforme) — c'est désormais **une faction mercenaire à moral fragile et prix cassé**, dont le seul atout structurel est sa cavalerie de raid.
>
> **Le type Chars est abandonné.** L'Aurige de Khand, seule pièce à l'avoir jamais utilisé (D030), devient cavalerie standard — plus de compteur de PV dédié, plus de statut « Jamais Faible » de char, plus de règle bespoke ([Poursuite 1] + [Plateforme de tir 2], retirées). Le type reste défini dans [[Regles_Base]] pour un usage futur éventuel, mais n'a plus de porteur actif dans ce projet.
>
> **Revue D076 (pivot badges universels, D073-D075) : aucun changement nécessaire.** [Mercenaire] reste le badge Faction — identité propre du peuple, pas un candidat à l'universalisation façon Rohan/Mordor, puisque l'exclusion de l'Aurige (le seul corps régulier) *est* le point de la règle. [Relance 1] est déjà le badge Spéciale depuis D070 : Khand anticipait sans le savoir le badge Spéciale universel. Aucune unité Élite ni Légende dans ce roster resserré — cohérent avec « bon marché et peu fiable », pas de tronc d'élite à afficher.
>
> Aligné sur [[Regles_Base]] v0.12 et [[Regles_Speciales]] v0.24, [[Regles_Points]] v0.21.

---

## 1. Faction de Khand et badge secondaire

*(Collapse de badges — D080/D081, tâche P7c.)* Khand était déjà conforme au nouveau système avant même qu'il n'existe (D076) : [Mercenaire] couvrait déjà tout le roster mercenaire (sauf l'Aurige, par identité), et aucun profil ne portait plus d'un badge secondaire. Le collapse P7c ne change donc **aucun coût** ici — seule la présentation passe de « badge Faction » à « trait de peuple ».

| Niveau | Effet | Coût brut | Porté par |
|---|---|---|---|
| **Faction** (troupes mercenaires) | **[Mercenaire]** *(chaque retrait forcé compte double)* | **−2** *(coût négatif)* | Mercenaire de Khand (1) · Mercenaire archer (2) · Pillards hache (3) · Pillards archer (4) |
| **Badge secondaire** (1 max) — **Spéciale** | **[Relance 1]** *(hache lourde)* | +2 | Troupes équipées de hache |

**[Mercenaire] est le premier badge/trait à coût négatif du projet** ([[Regles_Speciales]] §4a, D070) : une troupe motivée par la solde plutôt que par la loyauté cède plus facilement le terrain — mécaniquement, ses reculs de combat comptent double. Ça traduit un moral fragile sans complexifier la règle de recul elle-même, et ça fait de Khand la faction la moins chère à l'unité du projet, cohérent avec le principe de départ.

**L'Aurige de Khand ne porte pas la Faction.** C'est le seul corps qui échappe au statut mercenaire — l'unique force que Khand entraîne et possède en propre plutôt que loue au plus offrant. Son moral est celui d'une troupe régulière, pas d'un ramassis de reîtres.

---

## 2. Liste des troupes

| #   | Unité                      | Type       | Combat   | Classe | Faction | Badge secondaire | **Points** |
| --- | -------------------------- | ---------- | -------- | ------ | ------------------ | ---- | ---------- |
| 1   | Mercenaire de Khand        | Infanterie | Mêlée    | 🟢     | Mercenaire | Spéciale | **3**      |
| 2   | Mercenaire archer de Khand | Infanterie | Distance | 🟢     | Mercenaire | *(aucun)* | **2**      |
| 3   | Pillards de Khand (hache)  | Cavalerie  | Mêlée    | 🟢     | Mercenaire | Spéciale | **5**      |
| 4   | Pillards de Khand (archer) | Cavalerie  | Distance | 🟢     | Mercenaire | *(aucun)* | **3**      |
| 5   | Aurige de Khand            | Cavalerie  | Mêlée    | 🔵     | *(aucune — seul corps régulier)* | Spéciale | **7**      |

**Total roster : 20 points, inchangé — P7c (D081) sans effet sur Khand.**

> 🎲 **Note de design — un roster entièrement 🟢, sauf l'Aurige**
> Toute l'infanterie et la cavalerie de ligne de Khand est en classe légère (🟢, 2 dés) — un peuple de mercenaires n'a ni l'équipement ni l'entraînement pour porter des dés lourds. L'Aurige (🔵, 3 dés) est la seule pièce à sortir de ce plancher : c'est son avantage de classe, pas une règle spéciale de plus.

---

## 3. Profils détaillés

### 1. Mercenaire de Khand

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Infanterie | Mêlée | 🟢 | 2 | 2 dés | — | 4 | **3** |

**Badges :** Faction ([Mercenaire]) + Spéciale ([Relance 1])

**Note narrative :** des hommes venus vendre leur hache au service de Sauron — pas de cité pour les équiper d'armure ni de solde pour les fidéliser, seulement des cleavers de Khand qui frappent fort tant que le contrat tient. [Mercenaire] traduit crûment cette fidélité de façade : au premier coup dur, ils reculent deux fois plus vite qu'une troupe régulière.

---

### 2. Mercenaire archer de Khand

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Infanterie | Distance | 🟢 | 2 | 2 dés | 4 | 4 | **2** |

**Badges :** Faction ([Mercenaire])

**Note narrative :** des archers mercenaires, moins réputés que ceux de Gondor ou du Rohan — recrutés pour le nombre, pas pour la finesse. Décroche après avoir tiré ([Mobilité 1] intrinsèque, gratuite, classe 🟢) sans aucun badge à porter en plus du statut mercenaire. Le profil le moins cher du projet à ce stade.

---

### 3. Pillards de Khand (hache)

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Cavalerie | Mêlée | 🟢 | 4 | 2 dés | — | 3 | **5** |

**Badges :** Faction ([Mercenaire]) + Spéciale ([Relance 1])

**Note narrative :** des raiders montés qui frappent aux avant-postes puis se replient avec leur butin — la même hache que les Mercenaires (1), mais à cheval. Porte [Poursuite 2] intrinsèque comme toute cavalerie légère ou standard, tous peuples confondus — Khand n'a pas *la meilleure* cavalerie du jeu (identité toujours réservée au Rohan), mais bénéficie du même mécanisme que tout le monde. Le badge [Mercenaire] compense mécaniquement ce qu'un peuple raider paie normalement pour sa mobilité : coûteux à l'attaque, bon marché à la tenue.

---

### 4. Pillards de Khand (archer)

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Cavalerie | Distance | 🟢 | 4 | 2 dés | 4 | 3 | **3** |

**Badges :** Faction ([Mercenaire])

**Note narrative :** des cavaliers harceleurs qui tirent puis s'éloignent avant la riposte. Porte [Mobilité 2] intrinsèque (classe légère, cavalerie distance) — un cran au-dessus de l'ancien [Mobilité 1], gratuit par construction de la taxonomie. Moins cher et plus fragile que l'Éored d'éclaireur du Rohan (4 pts, badge Faction en plus).

---

### 5. Aurige de Khand

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Cavalerie | Mêlée | 🔵 | 3 | 3 dés | — | 3 | **7** |

**Badges :** Spéciale ([Relance 1])

**Note narrative :** l'attelage de guerre de Khand, l'unique force que ce peuple possède et entraîne en propre — pas une hache louée, un corps constitué. Ancienne pièce hors-norme (char de choc, puis char-plateforme après le Playtest #1), désormais **cavalerie de classe standard à part entière** : ni statut de mercenaire (pas de badge Faction — c'est le seul corps régulier du peuple), ni règle bespoke. Son avantage tient à la classe seule (🔵, seule unité du roster à sortir du plancher léger) et à [Poursuite 2] intrinsèque, comme toute cavalerie de mêlée standard.

**Abandon du type Chars et de ses règles bespoke** ([Poursuite 1] + [Plateforme de tir 2], D045/D046) : la pièce perd son statut « Jamais Faible » et son profil char-plateforme au profit d'un traitement identique à n'importe quelle cavalerie 🔵 du projet — plus simple à mémoriser à la table, au prix de l'identité distinctive qu'elle avait acquise post-Playtest #1.

---

## 4. Récapitulatif des badges portés

| Badge | Unités qui le portent |
|---|---|
| **Faction** ([Mercenaire]) | Mercenaire de Khand (1) · Mercenaire archer (2) · Pillards hache (3) · Pillards archer (4) |
| **Spéciale** ([Relance 1]) | Mercenaire de Khand (1) · Pillards hache (3) · Aurige de Khand (5) |
| **Aucun badge Faction** | Aurige de Khand (5) — seul corps régulier du peuple |

---

## 5. Points ouverts transverses

- **[Mercenaire] est une règle neuve, jamais testée** : son effet (retrait forcé doublé) n'a d'impact que si l'unité subit effectivement des reculs de combat répétés — son poids réel à la table reste à observer au prochain playtest, comme toute règle P4 non éprouvée.
- **Abandon du type Chars** : structure encore présente dans [[Regles_Base]] (§2.1, §2.3, §6.1) mais sans porteur actif dans tout le projet. À surveiller si un futur peuple (Orientaux, Harad ?) veut réintroduire une pièce à char — le type reste disponible, [Plateforme de tir X] aussi.
- **Pas de piquiers dans ce roster** — [Réception de charge] reste ouverte pour un futur profil de Khand si le matériel s'y prête (inchangé depuis la Passe 0).
- **Aucune unité légendaire au sens strict** (D023) — roster confirmé plat, 5 profils, sans palier standard/élite/légendaire. Choix assumé pour une faction mercenaire : pas de hiérarchie de prestige à représenter.

---

*Version : 2.2 — Phase 1 — 2026-08-13. **Collapse du système de badges (D080/D081, tâche P7c) — sans effet sur les coûts.** Khand était déjà conforme (D076) : [Mercenaire] devient un trait de peuple plutôt qu'un badge, présentation seule mise à jour (§1, §2). Aucun changement de points.*

*Version : 2.1 — Phase 1 — 2026-08-08. **Revue de conformité au pivot « badges universels » (D073-D075) — D076.** Aucun changement de badge ni de coût : [Mercenaire] reste le badge Faction (identité propre, l'exclusion de l'Aurige est le point de la règle, pas un oubli à corriger) ; [Relance 1] est déjà le badge Spéciale depuis D070. Roster confirmé conforme sans modification.*

*Version : 2.0 — Phase 1 — 2026-08-08. **Refonte P4 (D070) : repositionnement complet d'identité — Khand devient une faction mercenaire à moral fragile.** Système à deux badges : **Faction** = [Mercenaire] (premier badge à coût négatif du projet, −2 brut, chaque retrait forcé compte double) · **Spéciale** = [Relance 1] (hache lourde, inchangée). **Abandon du type Chars** : l'Aurige de Khand devient cavalerie 🔵 standard (badge Spéciale seul, pas de Faction — seul corps régulier du peuple), perd son statut Jamais Faible et ses règles bespoke ([Poursuite 1]/[Plateforme de tir 2], D045/D046). Roster inchangé à 5 profils, tous en classe 🟢 sauf l'Aurige. Non testé — validation P7a.*
