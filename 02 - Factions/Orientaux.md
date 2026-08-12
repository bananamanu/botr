---
projet: "Batailles de la Terre du Milieu"
type: "faction"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-08-08"
tags: [BdTdM, "type/faction", "peuple/orientaux", "statut/brouillon"]
version: "2.1"
---

# Orientaux — Profils d'unités

> **Objet de ce document (refonte P4, D072 ; repositionnement D077).** Re-expression complète du roster sur la taxonomie visuelle (classe × type × mode, [[Regles_Base]] §2.4) et la matrice de points ([[Regles_Points]] §2). Renommage du peuple : **Easterling → Orientaux** (le nom des unités utilisait déjà « orientaux » depuis la Passe 0 ; seul le nom de peuple/fichier a suivi, D072).
>
> **Repositionnement d'identité (D077) : le miroir mécanique pur de Gondor (D072) est abandonné.** Emmanuel demande une identité propre, distincte d'[Armure 1]. Nouveau badge Faction : **[Mur de bouclier]**, restaurée et refondue depuis l'ancienne version coupée en P2 — une protection qui tient tant que la ligne n'est pas percée, puis s'effondre d'un coup au premier sang. Fidèle à l'image Tolkien d'une infanterie disciplinée en formation plutôt qu'en armure individuelle.
>
> Aligné sur [[Regles_Base]] v0.12 et [[Regles_Speciales]] v0.25, [[Regles_Points]] v0.22.

---

## 1. Les deux badges des Orientaux

| Badge | Effet | Coût brut | Porté par |
|---|---|---|---|
| **Faction** (Orientaux) | **[Mur de bouclier]** *(restaurée et refondue, D077)* | +1 *(forfait, provisoire)* | Cohorte d'orientaux · Cohorte de piquiers |
| **Spéciale** (unité) | **[Relance 1]** | +2 | Cohorte de piquiers · Cohorte d'archers |

**[Mur de bouclier], nouvelle mouture : tient tant que la ligne n'est pas percée.** Tant que l'unité n'a subi aucune touche, elle bénéficie de [Protection 1] (ignore 1 touche, mêlée ou tir). Dès la première touche encaissée, la formation est rompue : la protection disparaît définitivement. Distinct d'[Armure 1] (qui retire des faces Épée, mêlée seulement) — ici, le bouclier arrête aussi bien la lame que la flèche, mais seulement tant que le mur tient.

**Distribution volontairement partielle.** Contrairement à Rohan (Faction universelle) ou Gondor (Faction sur presque tout le roster), seules les deux unités de ligne massée (Cohorte, Piquiers) portent [Mur de bouclier] — les Cataphractaires (cavalerie, pas de formation de mêlée serrée) et les Archers (tirailleurs, pas de mur) en sont exclus par construction : la règle ne dit quelque chose que si elle reste réservée à l'infanterie de ligne.

Le badge **Élite** ([Inébranlable 1] + Jamais Faible) reste disponible au système mais n'est porté par **aucune** unité de ce roster resserré à 4 profils — même situation que Khand.

---

## 2. Liste des troupes

| #   | Unité                         | Type       | Combat   | Classe | Badges             | **Points** |
| --- | ----------------------------- | ---------- | -------- | ------ | ------------------ | ---------- |
| 1   | Cohorte d'orientaux           | Infanterie | Mêlée    | 🔵     | Faction            | **4**      |
| 2   | Cohorte de piquiers orientaux | Infanterie | Mêlée    | 🔵     | Faction + Spéciale | **5**      |
| 3   | Cohorte d'archers orientaux   | Infanterie | Distance | 🟢     | Spéciale           | **3**      |
| 4   | Cataphractaires orientaux     | Cavalerie  | Mêlée    | 🔴     | *(aucun)*          | **7**      |

**Total roster : 19 points** *(21 dans la version miroir pur D072, 22 dans l'originale)*.

> 🎲 **Cohorte et Piquiers enfin distingués.** Le miroir pur (D072) faisait tomber les deux profils au même prix (5 pts) — [Mur de bouclier] (1 pt) coûte moins qu'[Armure 1] (2 pts), ce qui libère un palier de compression : la Cohorte de base descend à 4 pts, les Piquiers (qui ajoutent Spéciale) restent à 5. Collision résolue sans badge supplémentaire.

---

## 3. Profils détaillés

### 1. Cohorte d'orientaux

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Infanterie | Mêlée | 🔵 | 2 | 3 dés | — | 4 | **4** |

**Badges :** Faction ([Mur de bouclier])

**Note narrative :** l'infanterie de ligne régulière des peuples de l'Est, alliés de longue date de Sauron — rangs serrés, boucliers refermés au contact. Tant que la ligne tient, elle encaisse ce qu'aucune armure individuelle n'arrêterait ; dès la première percée, la protection tombe pour de bon. Une discipline de formation plutôt qu'un métal individuel — l'identité originelle du peuple (D037), retrouvée sous une forme plus simple à la table.

> 🎲 **Note de calcul.** Brut = 15 (Inf 🔵 mêlée) + [Mur de bouclier] Faction (1) = 16 → round(16÷3)−1 = **4**.

---

### 2. Cohorte de piquiers orientaux

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Infanterie | Mêlée | 🔵 | 2 | 3 dés | — | 4 | **5** |

**Badges :** Faction ([Mur de bouclier]) + Spéciale ([Relance 1])

**Note narrative :** une compagnie de piquiers longs, la même discipline de formation que la Cohorte de base ([Mur de bouclier]), avec une arme qui ne rate pas deux fois une fois la ligne engagée ([Relance 1]). Le badge Spéciale les distingue enfin clairement de la Cohorte : plus cher, plus mordant.

> 🎲 **Note de calcul.** Brut = 15 (Inf 🔵 mêlée) + [Mur de bouclier] Faction (1) + [Relance 1] Spéciale (2) = 18 → round(18÷3)−1 = **5**.

---

### 3. Cohorte d'archers orientaux

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Infanterie | Distance | 🟢 | 2 | 2 dés | 4 | 4 | **3** |

**Badges :** Spéciale ([Relance 1])

**Note narrative :** des archers de l'Est, tirailleurs mobiles — ils décrochent après avoir tiré ([Mobilité 1] intrinsèque, gratuite, classe 🟢), sans jamais tenir de ligne au sens du [Mur de bouclier]. Pas de badge Faction : pas de formation à rompre pour des tireurs qui ne restent jamais en place. [Relance 1] (Spéciale) traduit une discipline de tir, pas de position — une flèche qui ne rate pas deux fois.

> 🎲 **Note de calcul.** Brut = 11 (Inf 🟢 distance, [Mobilité 1] incluse) + [Relance 1] Spéciale (2) = 13 → round(13÷3)−1 = **3**.

---

### 4. Cataphractaires orientaux

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Cavalerie | Mêlée | 🔴 | 2 | 4 dés | — | 3 | **7** |

**Badges :** *(aucun)*

**Note narrative :** la cavalerie lourde de l'Est. Ni [Mur de bouclier] (une charge montée ne tient pas de mur), ni Spéciale — [Armure 1] et [Poursuite 1] intrinsèques à la classe 🔴 suffisent à en faire une pièce lourde crédible, sans badge à afficher. S'aligne mécaniquement sur les Chevaliers de Minas Tirith de Gondor (même classe, même absence de supplément, même coût) — la distinction reste narrative.

> 🎲 **Note de calcul.** Brut = 23 (Cav 🔴 mêlée, [Armure 1] + [Poursuite 1] + prime de choc déjà inclus) → round(23÷3)−1 = **7**. Coût inchangé par rapport à la version miroir pur (le badge Faction y était déjà gratuit au plancher) — le retirer n'a aucun effet sur le prix.

---

## 4. Récapitulatif des badges portés

| Badge | Unités qui le portent |
|---|---|
| **Faction** ([Mur de bouclier]) | Cohorte d'orientaux (1) · Cohorte de piquiers (2) |
| **Spéciale** ([Relance 1]) | Cohorte de piquiers (2) · Cohorte d'archers (3) |
| **Élite** | *(aucune unité)* |
| **Aucun badge** | Cataphractaires orientaux (4) — seule unité définie par sa classe seule |

---

## 5. Points ouverts transverses

- **Coût de [Mur de bouclier] (1, refondue D077)** — jamais testé sous cette forme, ni sous l'ancienne (coupée avant tout playtest réel avec la version conditionnelle par adjacence). À surveiller en priorité au prochain playtest, comme [Horde] chez Mordor (même patron de règle).
- **[Double Tir] toujours sans porteur** — abandonnée depuis D072 (miroir pur), reste sans porteur après D077 (le retour de [Mur de bouclier] ne la ressuscite pas). Conservée au glossaire.
- **Réception de charge** reste coupée du système entier (inchangé depuis P2, D062) — aucun porteur nulle part dans le projet à ce stade.

---

*Version : 2.1 — Phase 1 — 2026-08-08. **Repositionnement D077 : abandon du miroir pur de Gondor.** Badge Faction remplacé par **[Mur de bouclier]**, restaurée et refondue ([Protection 1] tant qu'aucune touche subie, perdue à la 1ʳᵉ) — porté par Cohorte et Piquiers uniquement (plus par Archers ni Cataphractaires). Archers perdent Faction, gardent Spéciale seule (4→3 pts). Cataphractaires perdent Faction, aucun badge (coût inchangé, 7 pts — le badge y était déjà gratuit). Cohorte de base et Piquiers enfin distingués en coût (4 vs 5, résolvant la collision D072). Total roster 21→**19 pts**. Non testé — validation P7a.*

*Version : 2.0 — Phase 1 — 2026-08-08. **Refonte P4 (D072) : renommage Easterling → Orientaux + miroir mécanique pur de Gondor.** Système à deux badges : **Faction** = [Armure 1] (tout le roster) · **Spéciale** = [Relance 1] (piquiers, archers). Abandon de l'ancienne identité « discipline de formation » et de la signature [Double Tir] (sans porteur depuis ce passage). Cataphractaires perdent [Armure 2] (alignés sur les Chevaliers de Minas Tirith de Gondor) ; Mouvement 2 n'est plus une exception mais la valeur standard de la grille cavalerie 🔴. Piquiers perdent [Réception de charge] (coupée P2, sans remplacement) et tombent au même prix que la Cohorte de base (5 pts, compression). Roster inchangé à 4 profils, total 21 pts (vs 22 dans l'ancienne version). Non testé — validation P7a.*

*Version : 1.2 — Phase 1 — 2026-07-29. **[Réception de charge] refondue en inconditionnelle** (D058, voir [[Regles_Speciales]]) : la Cohorte de piquiers orientaux bénéficie désormais de +1 dé sur **toute** contre-attaque, plus seulement contre un adversaire qui vient de se déplacer. Note narrative corrigée en conséquence. Coût du profil inchangé (6 pts) ; le coût de la règle elle-même est signalé provisoire dans [[Regles_Points]].*

*Version : 1.1 — Phase 1 — 2026-07-25. **Mise à jour post-Playtest #1** (`[[Playtest1_Compte-rendu]]`). Cataphractaires orientaux : retrait de [Charge écrasante] sans remplacement (D043 — règle retirée de toute la V1) ; coût 7 → 6 pts (D046). Le trio suggéré passe de 16 à 15 pts (parité avec Gondor). Le coût de [Mur de bouclier] (1 pt) reste non éprouvé (partie étranglée au centre).*

*Version : 1.0 — Phase 1 — 2026-07-20. Roster (alors « Easterling ») validé et clos dès la première session (D038) : identité « miroir discipliné de Gondor » actée, nouvelle règle [Mur de bouclier] créée (D037), 4 profils chiffrés et validés sans repasse ultérieure. Prêt pour le Playtest #1 (trio suggéré : Cohorte + Archers + Cataphractaires, 16 pts).*
