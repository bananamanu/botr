---
projet: "Batailles de la Terre du Milieu"
type: "playtest"
phase: "1"
statut: "clos"
date_maj: "2026-07-27"
tags: [BdTdM, "type/playtest", "phase/1", "statut/analyse", "playtest/1b"]
version: "1.0"
---

# Playtest #1b — Addendum au compte-rendu

> **Objet de ce document :** débrief du re-run du scénario `[[Playtest1_Avant-garde_sur_le_Pelennor]]` (« Playtest #1b »), joué le 2026-07-27, avec les profils corrigés du Playtest #1 (D040-D050). Objectif : éprouver les cinq règles restées non testées ([Horde], [Peur X], [Mur de bouclier], l'Aurige reconçu, les règles neuves) dans un dispositif forçant l'engagement des ailes. Décisions D051-D058.

---

## 1. Résultat & déroulé

| | |
|---|---|
| **Format** | Normal, 1v1 — re-run du même scénario, mêmes ordres de bataille corrigés |
| **Résultat** | **Victoire du Bien, 6–4**, quasi 6–6 : le Mal pouvait scorer 2 médailles de plus au tour suivant (deux unités affaiblies à portée) |

**Verdict d'équilibre (D051) :** le retrait de [Charge écrasante] (D043) et les sept ajustements de profils (D046-D050) tiennent leur promesse. La partie est serrée, sans camp qui blowout l'autre, et aucun combo n'a semblé overkill. L'intention quantité (Bien) / qualité (Mal) fonctionne comme prévu : le Bien l'emporte grâce au nombre, le Mal reste dangereux jusqu'au dernier tour. **Playtest #1b clôt la phase de correction ouverte au Playtest #1** — plus de re-run prévu sur ce point avant le Playtest #3 (Pelennor complet).

---

## 2. Jetons d'activation / de cible — dispositif validé (D052)

Le jeton unique de contre-attaque (D042) est remplacé à la table par **deux jetons distincts** : un jeton d'activation sur les unités du camp actif, un jeton cible sur les unités adverses touchées. **Très efficace** — plus aucun oubli de contre-attaque signalé. Retenu comme convention officielle de jeu, à intégrer à l'aide de jeu convention (6 joueurs, enjeu de lisibilité maximal).

---

## 3. Règles neuves — enfin éprouvées (D053)

| Règle | Constat |
|---|---|
| **[Horde]** (3 pts) | Peu d'activations mais potentiel bien lu : les orques du Morannon frappent à 4 dés à pleine force, subissent une contre-attaque, perdent le bonus. Le surge-puis-effondrement se *sent* à la table. **Coût 3 pts confirmé.** |
| **[Armure 2]** | A sauvé les Cataphractaires orientaux sur une attaque. **Validé.** |
| **[Mur de bouclier]** (1 pt) | A absorbé 2 touches sur la partie. Crainte initiale de surpuissance, mais **la règle s'autolimite** : un recul rompt l'adjacence et fait perdre la protection. La décision « tenir ou rompre » existe bel et bien. **Coût 1 pt confirmé.** ⚠️ Point de vigilance conservé (pas de correctif) : le risque de sur-cumul reste ouvert si une liste empile plusieurs porteurs en formation permanente — à surveiller, pas à corriger maintenant. |
| **[Arme de jet X]** / **[Plateforme de tir X]** | Chacune déclenchée une fois. Minimum vital atteint pour valider les coûts provisoires (1×X et 2×X). Rien d'anormal observé. |

---

## 4. Ajustements de profils actés (D054-D057)

### 4.1 Troll du Mordor (D054)

A fini la partie à 3/5 PV — a tenu son rôle de pièce signature sans jamais tomber. Décision d'Emmanuel : **PV 5 → 4, coût maintenu à 7 pts.**

- Recalcul brut : `Mvt 2 + PV 4 + (4×3) + [Arme Lourde 1](2) + [Peur 1](2) = 22 → round(22÷3)−1 = 6`.
- Le maintien à **7 pts** est une **prime de pièce signature assumée** (+1 au-dessus du calcul brut), cohérente avec son statut déjà dérogatoire (seul profil de la V1 à dépasser 2 règles spéciales, D023). Décision manuelle documentée, pas une correction de calcul.

### 4.2 Rangers du Gondor (D055)

Profil jugé en retrait par rapport à sa famille (Rangers d'Ithilien, Archers de la Racine Noire). Décision : **ajout de [Mobilité 1]**, sans changement de rôle ni empiètement sur les autres membres de la famille.

- Recalcul brut : `Mvt 2 + PV 6 + (2×2) + [Double Tir](3) + [Mobilité 1](1) = 16 → round(16÷3)−1 = 4`.
- **Coût inchangé : 4 pts** — même effet de palier « gratuit » déjà observé sur l'Éored d'éclaireur et les Archers liges (Regles_Points §2bis).
- Hiérarchie de famille préservée : Rangers du Gondor (2 dés + Double Tir + Mobilité 1, **4 pts**) reste strictement sous Rangers d'Ithilien (3 dés + mêmes règles, **5 pts**). Dominance stricte lisible au prix, pas au profil (principe D025).

### 4.3 [Mobilité X] — clarification de fonctionnement (D056)

Question posée à la table : faut-il attaquer pour bénéficier de [Mobilité X] ? **Réponse par le texte du glossaire, confirmée et formalisée** : oui — *« Après avoir effectué une attaque, cette unité peut se déplacer de X hexagones supplémentaires. »* Sans attaque, l'unité se déplace simplement de son Mouvement normal, sans bonus. C'est voulu : [Mobilité X] modélise le **tir-puis-décroche** (identité harcèlement Rohan/Mordor/Fiefs), pas une mobilité brute. Formulation à reporter telle quelle dans l'aide de jeu convention pour éviter que la question ne revienne à la table à 6 joueurs : *« Mobilité = tu frappes, puis tu décroches. Pas d'attaque, pas de bonus. »*

---

## 5. Suivi documentaire

**Reste à répercuter dans le dépôt** (hors périmètre de cette tâche Todoist, à planifier) :
- `02 - Factions/Mordor.md` : Troll — PV 5 → 4, note D054 (prime signature).
- `02 - Factions/Gondor_et_Fiefs.md` : Rangers du Gondor — ajout [Mobilité 1], note D055.
- `01 - Règles/Regles_Speciales.md` : clarifier explicitement la dépendance à l'attaque de [Mobilité X] (D056), et lever la réserve « non testé » sur [Horde] (D032), [Peur X] reste provisoire (Arcane peu vue, à confirmer au Playtest #3), [Mur de bouclier] (D037).
- `01 - Règles/Regles_Base.md` : documenter le dispositif à deux jetons (activation/cible) comme convention de jeu recommandée (D052).
- `00 - META/Document_de_cadrage.md` : journal D051-D056.

---

*Version : 1.0 — Phase 1 — 2026-07-27. Addendum au compte-rendu du Playtest #1, couvrant le re-run #1b. Résultat 6–4 Bien (quasi 6–6) ; équilibre validé ; [Horde], [Mur de bouclier], [Arme de jet X], [Plateforme de tir X] éprouvés sans dérive ; jetons activation/cible adoptés ; Troll (PV 4, 7 pts) et Rangers du Gondor (+[Mobilité 1], 4 pts) ajustés ; [Mobilité X] clarifiée comme dépendante de l'attaque.*
