---
projet: "Batailles de la Terre du Milieu"
type: "faction"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-08-13"
tags: [BdTdM, "type/faction", "peuple/orientaux", "statut/brouillon"]
version: "2.2"
---

# Orientaux — Profils d'unités

> **Objet de ce document (refonte P4, D072 ; miroir Gondor rétabli P7c, D081).** Re-expression complète du roster sur la taxonomie visuelle (classe × type × mode, [[Regles_Base]] §2.4) et la matrice de points ([[Regles_Points]] §2). Renommage du peuple : **Easterling → Orientaux** (le nom des unités utilisait déjà « orientaux » depuis la Passe 0 ; seul le nom de peuple/fichier a suivi, D072).
>
> **Le collapse de badges (D081) revient sur le repositionnement D077.** Au Playtest #3, le constat de terrain a été que la Faction de Gondor comme des Orientaux ne couvrait pas tout le roster ; l'houserule l'a étendue partout sous un nom commun, **[Défense 1]** (= [Armure 1]), distinct de l'intrinsèque du 🔴. **[Mur de bouclier]** (identité propre des Orientaux depuis D077) redevient sans porteur actif — les Orientaux reviennent au **miroir mécanique exact de Gondor**.
>
> Aligné sur [[Regles_Base]] v0.13 et [[Regles_Speciales]] v0.27, [[Regles_Points]] v0.24.

---

## 1. Faction des Orientaux et badge secondaire

*(Collapse de badges — D080/D081, tâche P7c.)* Comme Gondor, les Orientaux ont un trait de Faction universel, plus un éventuel badge secondaire.

| Niveau | Effet | Coût brut | Porté par |
|---|---|---|---|
| **Faction** (tout le roster, sans exception) | **[Défense 1]** *(= [Armure 1], nom d'usage — [[Regles_Speciales]] §4a)* | +2 *(gratuit sur 🔴, déjà au plancher intrinsèque)* | **Les 4 unités du roster** |
| **Badge secondaire** (1 max) — **Spéciale** | **[Relance 1]** | +2 | Cohorte de piquiers |

Le badge **Élite** reste disponible au système mais n'est porté par **aucune** unité de ce roster resserré à 4 profils — même situation que Khand.

> 🔄 **P7c (D081) — retour au miroir de Gondor.** [Mur de bouclier] (D077) couvrait Cohorte + Piquiers seulement, en excluait Archers et Cataphractaires par construction. [Défense 1] s'applique désormais **partout**, sans exception de type ou de mode — Archers (3) et Cataphractaires (4) gagnent la Faction qu'ils n'avaient jamais eue.

---

## 2. Liste des troupes

| #   | Unité                         | Type       | Combat   | Classe | Faction | Badge secondaire | **Points** |
| --- | ----------------------------- | ---------- | -------- | ------ | --- | --- | ---------- |
| 1   | Cohorte d'orientaux           | Infanterie | Mêlée    | 🔵     | Défense 1 | *(aucun)* | **5**      |
| 2   | Cohorte de piquiers orientaux | Infanterie | Mêlée    | 🔵     | Défense 1 | Spéciale | **5**      |
| 3   | Cohorte d'archers orientaux   | Infanterie | Distance | 🟢     | Défense 1 | Spéciale | **4**      |
| 4   | Cataphractaires orientaux     | Cavalerie  | Mêlée    | 🔴     | Défense 1 *(gratuite)* | *(aucun)* | **7**      |

**Total roster : 21 points** *(19 avec [Mur de bouclier] partiel D077, 21 dans la version miroir pur D072, 22 dans l'originale)*.

> 🔄 **P7c (D081) — Faction étendue à tout le roster.** Cohorte (1) : 4→**5 pts** ([Défense 1] coûte plus que l'ancien [Mur de bouclier]). Archers (3) : 3→**4 pts** (gagnent Faction, n'en avaient jamais eu). Piquiers (2) et Cataphractaires (4) : coût inchangé (la compression absorbe l'écart, et Défense 1 est gratuite sur les Cataphractaires 🔴).

---

## 3. Profils détaillés

### 1. Cohorte d'orientaux

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Infanterie | Mêlée | 🔵 | 2 | 3 dés | — | 4 | **4** |

**Badges :** Faction ([Défense 1])

**Note narrative :** l'infanterie de ligne régulière des peuples de l'Est, alliés de longue date de Sauron — rangs serrés, cottes de mailles renforcées, aussi bien équipée que son miroir de Gondor.

> 🎲 **Note de calcul (P7c, D081).** Brut = 15 (Inf 🔵 mêlée) + [Défense 1] Faction (2) = 17 → round(17÷3)−1 = **5**. *(Ancien coût : 4, avec [Mur de bouclier] à 1 pt — [Défense 1] coûte plus cher.)*

---

### 2. Cohorte de piquiers orientaux

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Infanterie | Mêlée | 🔵 | 2 | 3 dés | — | 4 | **5** |

**Badges :** Faction ([Défense 1]) + Spéciale ([Relance 1])

**Note narrative :** une compagnie de piquiers longs, aussi bien protégée que la Cohorte de base ([Défense 1]), avec une arme qui ne rate pas deux fois une fois la ligne engagée ([Relance 1]).

> 🎲 **Note de calcul.** Brut = 15 (Inf 🔵 mêlée) + [Défense 1] Faction (2) + [Relance 1] Spéciale (2) = 19 → round(19÷3)−1 = **5**. *(Inchangé.)*

---

### 3. Cohorte d'archers orientaux

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Infanterie | Distance | 🟢 | 2 | 2 dés | 4 | 4 | **3** |

**Badges :** Faction ([Défense 1]) + Spéciale ([Relance 1])

**Note narrative :** des archers de l'Est, tirailleurs mobiles — ils décrochent après avoir tiré ([Mobilité 1] intrinsèque, gratuite, classe 🟢), une flèche qui ne rate pas deux fois ([Relance 1]), et portent désormais la même protection que le reste du roster.

> 🔄 **P7c (D081).** Gagne [Défense 1] — n'avait jamais porté de Faction sous [Mur de bouclier] (D077, réservé à l'infanterie de ligne massée). Brut = 11 (Inf 🟢 distance, [Mobilité 1] incluse) + [Relance 1] Spéciale (2) + [Défense 1] Faction (2) = 15 → round(15÷3)−1 = **4**. *(Ancien coût : 3.)*

---

### 4. Cataphractaires orientaux

| Type | Combat | Classe | Mouvement | Attaque | Portée | Figurines | **Points** |
|---|---|---|---|---|---|---|---|
| Cavalerie | Mêlée | 🔴 | 2 | 4 dés | — | 3 | **7** |

**Badges :** Faction ([Défense 1] — gratuite)

**Note narrative :** la cavalerie lourde de l'Est. [Armure 1] et [Poursuite 1] intrinsèques à la classe 🔴 couvrent déjà le plancher de [Défense 1] — la Faction ne coûte donc rien de plus ici. S'aligne mécaniquement sur les Chevaliers de Minas Tirith de Gondor (même classe, même Faction gratuite, même coût) — la distinction reste narrative.

> 🔄 **P7c (D081).** Gagne [Défense 1], gratuite (déjà au plancher 🔴). Brut = 23 (Cav 🔴 mêlée, [Armure 1] + [Poursuite 1] + prime de choc déjà inclus) → round(23÷3)−1 = **7**. *(Coût inchangé.)*

---

## 4. Récapitulatif des badges portés

| Badge | Unités qui le portent |
|---|---|
| **Faction** ([Défense 1]) | **Les 4 unités du roster, sans exception** — gratuite sur les Cataphractaires (4, 🔴) |
| **Spéciale** ([Relance 1]) | Cohorte de piquiers (2) · Cohorte d'archers (3) |
| **Élite** | *(aucune unité)* |
| **Aucun badge secondaire** | Cohorte d'orientaux (1) · Cataphractaires orientaux (4) |

---

## 5. Points ouverts transverses

- **[Mur de bouclier] redevient sans porteur actif** (P7c, D081) — conservée au glossaire, réutilisable pour un futur profil ou peuple voulant l'identité « formation qui tient tant qu'elle n'est pas percée ».
- **[Double Tir] toujours sans porteur** — abandonnée depuis D072, jamais ressuscitée.
- **Réception de charge** reste coupée du système entier (inchangé depuis P2, D062) — aucun porteur nulle part dans le projet à ce stade.
- **Hausse de coût du roster (19→21 pts, P7c)** — non testée sous cette forme : le Playtest #3 a joué les Orientaux à l'ancien barème [Mur de bouclier]. À surveiller au prochain test, en particulier l'équilibre général Bien/Mal (D084) qui s'appuyait sur les anciens totaux.

---

*Version : 2.2 — Phase 1 — 2026-08-13. **Collapse du système de badges (D080/D081, tâche P7c) — retour au miroir de Gondor.** [Mur de bouclier] (D077) redevient sans porteur actif ; la Faction devient **[Défense 1]** (= [Armure 1]), universelle sur les 4 unités. Cohorte (1) : 4→**5 pts**. Cohorte d'archers (3) : 3→**4 pts** (gagne Faction). Piquiers (2) et Cataphractaires (4) : coût inchangé. Total roster 19→**21 pts**.*

*Version : 2.1 — Phase 1 — 2026-08-08. **Repositionnement D077 : abandon du miroir pur de Gondor.** Badge Faction remplacé par **[Mur de bouclier]**, restaurée et refondue ([Protection 1] tant qu'aucune touche subie, perdue à la 1ʳᵉ) — porté par Cohorte et Piquiers uniquement (plus par Archers ni Cataphractaires). Archers perdent Faction, gardent Spéciale seule (4→3 pts). Cataphractaires perdent Faction, aucun badge (coût inchangé, 7 pts — le badge y était déjà gratuit). Cohorte de base et Piquiers enfin distingués en coût (4 vs 5, résolvant la collision D072). Total roster 21→**19 pts**. Non testé — validation P7a.*

*Version : 2.0 — Phase 1 — 2026-08-08. **Refonte P4 (D072) : renommage Easterling → Orientaux + miroir mécanique pur de Gondor.** Système à deux badges : **Faction** = [Armure 1] (tout le roster) · **Spéciale** = [Relance 1] (piquiers, archers). Abandon de l'ancienne identité « discipline de formation » et de la signature [Double Tir] (sans porteur depuis ce passage). Cataphractaires perdent [Armure 2] (alignés sur les Chevaliers de Minas Tirith de Gondor) ; Mouvement 2 n'est plus une exception mais la valeur standard de la grille cavalerie 🔴. Piquiers perdent [Réception de charge] (coupée P2, sans remplacement) et tombent au même prix que la Cohorte de base (5 pts, compression). Roster inchangé à 4 profils, total 21 pts (vs 22 dans l'ancienne version). Non testé — validation P7a.*

*Version : 1.2 — Phase 1 — 2026-07-29. **[Réception de charge] refondue en inconditionnelle** (D058, voir [[Regles_Speciales]]) : la Cohorte de piquiers orientaux bénéficie désormais de +1 dé sur **toute** contre-attaque, plus seulement contre un adversaire qui vient de se déplacer. Note narrative corrigée en conséquence. Coût du profil inchangé (6 pts) ; le coût de la règle elle-même est signalé provisoire dans [[Regles_Points]].*

*Version : 1.1 — Phase 1 — 2026-07-25. **Mise à jour post-Playtest #1** (`[[Playtest1_Compte-rendu]]`). Cataphractaires orientaux : retrait de [Charge écrasante] sans remplacement (D043 — règle retirée de toute la V1) ; coût 7 → 6 pts (D046). Le trio suggéré passe de 16 à 15 pts (parité avec Gondor). Le coût de [Mur de bouclier] (1 pt) reste non éprouvé (partie étranglée au centre).*

*Version : 1.0 — Phase 1 — 2026-07-20. Roster (alors « Easterling ») validé et clos dès la première session (D038) : identité « miroir discipliné de Gondor » actée, nouvelle règle [Mur de bouclier] créée (D037), 4 profils chiffrés et validés sans repasse ultérieure. Prêt pour le Playtest #1 (trio suggéré : Cohorte + Archers + Cataphractaires, 16 pts).*
