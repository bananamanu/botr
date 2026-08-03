---
projet: "Batailles de la Terre du Milieu"
type: "playtest"
phase: "1"
statut: "clos"
date_maj: "2026-08-02"
tags: [BdTdM, "type/playtest", "phase/1", "statut/analyse", "playtest/2"]
version: "1.0"
---

# Playtest #2 — Compte rendu

> **Scénario :** « La grande bête sur le Pelennor » (`[[Playtest2_La_grande_bete]]`), Normal 13×9. **Emmanuel en MJ**, deux joueurs qui s'affrontaient — un ami et son fils, **non versés dans l'univers de Tolkien**. Ce dispositif (joueurs neufs, arbitre qui n'intervient pas sur leurs choix) est le meilleur révélateur de lisibilité qu'on ait eu.
>
> **Verdict :** le gabarit du Mûmakil tient, mais le test révèle un **point noir structurant** — le *easy-to-play* n'est pas atteint. C'est ce constat, pas l'équilibre, qui déclenche une refonte de fond (le « big bang »). Les décisions correctives sont **actées** (D059/D060) ; leur mise en œuvre est le sprint P1→P7.

---

## 1. Résultat & déroulé

| | |
|---|---|
| **Format** | Normal, 13×9, 1 joueur par camp, **Emmanuel MJ** |
| **Ordre de bataille** | Bien 75 pts (13 u.) / Mal 76 pts (12 u., dont Mûmakil 21) — cf. scénario |
| **Résultat** | **Victoire du Bien, 7–6** |
| **Réserve majeure** | Score obtenu **après avoir nerfé la bête à la volée** (voir §3) — l'équilibre affiché n'a donc pas tenu tel quel |

La partie a « pas trop mal tourné » sur le plan du déroulé. Mais deux enseignements dominent tout le reste : la lisibilité (§2) et le Mûmakil (§3).

---

## 2. Le verdict qui prime : *easy-to-play* raté

C'est **le point noir**, et il touche la **priorité n°1 du projet** (principe §1 : fluidité/accessibilité pour des joueurs peu à l'aise avec la complexité).

- Les deux joueurs avaient **énormément de mal à distinguer les unités** les unes des autres — normal, ils ne connaissent pas l'univers, et rien sur la table ne dit d'un coup d'œil « qui est quoi et qui frappe fort ».
- Ils **ne retenaient pas les règles spéciales** attachées à chaque profil.
- Même la **double-touche en mêlée**, pourtant comprise, **ne se rappelait pas** en cours de partie.
- Suggestion de l'ami testeur, retenue : **des tokens pour visualiser** forces et règles spéciales de chaque unité.

Diagnostic : le modèle « chaque profil porte ses propres règles » (principe §3) suppose qu'un joueur **connaît son armée** — hypothèse **fausse** pour le public visé (convention, joueurs neufs). La mémorisation par profil est le goulot.

---

## 3. Le Mûmakil : un boulet plus qu'un atout

- Il a été **nerfé en cours de partie** : traité comme **cible molle**, et doté d'une **[Protection 1] contre les tirs** en houserule pour qu'il tienne un peu.
- La **Furie ([Bête incontrôlable]) n'a pas été déclenchée** (la bête n'a pas été suffisamment blessée au bon moment), mais **paraît trop punitive** à la lecture. **Bonne idée narrative et fun** — une bête acculée qui piétine les siens — mais **dans les faits la bête est plus un désavantage qu'autre chose**.
- **Verdict : à repenser en profondeur** (spirale de Furie, impact, et en conséquence la mécanique d'objectif/médailles du scénario). → tâche **P5**.

---

## 4. La décision : le « big bang » — retour au C&C pur, à taxonomie visuelle

Réponse actée au §2 : on **arrête de faire porter les règles par le profil** et on les fait **dériver d'une catégorie lisible d'un coup d'œil**. Décisions (détail en **D059/D060** du cadrage) :

- **Couleur = classe = nombre de dés** : 🟢 vert **2** / 🔵 bleu **3** / 🔴 rouge **4**.
- **Effectifs/PV** : **Infanterie 4** figurines · **Cavalerie 3** · Créature à part.
- **Type d'attaque au token** : mêlée / distance.
- **Mouvement et règles intrinsèques dérivés** de la combinaison **classe × type × moyen d'attaque** — plus de règles à mémoriser profil par profil.
- **Badge Élite** : un cran de granularité en plus.
- **Unités signature** : une ou deux règles spéciales **maximum**, réservées aux pièces marquantes (**Mûmakil, Compagnie grise**…).
- **Tokens de table** pour rendre tout ça visible (la suggestion du testeur, opérationnalisée en P6).

Ce pivot **amende le principe §3** (« profils comme vecteurs de règles ») : le vecteur devient la **taxonomie**, l'asymétrie de peuple étant réinjectée par le badge Élite et les rares signatures.

---

## 5. Ce que ça déclenche

Un **sprint de refonte** court jusqu'au **18/08** (système jouable verrouillé avant l'ajout des héros) : **P1** la grille → **P2** tri du glossaire → **P3** points en matrice → **P4** re-expression des 6 rosters → **P5** refonte Mûmakil/Furie → **P6** composants visuels → **P7** playtest de validation + refonte du cadrage. Détail et dates dans Todoist (section *Refonte système C&C*).

> ⚠️ **Ce compte-rendu ne retouche aucune règle ni aucun profil.** La refonte proprement dite (règles de base, glossaire, points, rosters) est le travail des phases P1-P4 ; la réécriture des principes §3 et de la feuille de route est P7b. Ici, on **acte et on journalise**.

---

## 6. Suivi documentaire

| Document | État |
|---|---|
| `[[Playtest2_Compte-rendu]]` (ce fichier) | **créé** |
| `00 - META/Document_de_cadrage.md` | **amendé** — D059 (pivot) + D060 (paramètres de la taxonomie) |
| `Regles_Base.md` / `Regles_Speciales.md` / `Regles_Points.md` | à refondre — **P1 / P2 / P3** |
| 6 rosters `02 - Factions/*.md` | à re-exprimer — **P4** |
| `Harad.md` (Mûmakil) + scénario PT2 | à refondre — **P5** |
| Composants visuels (tokens + fiche A4) | à spécifier — **P6** |

---

> 🔗 **Voir aussi**
> `[[Playtest2_La_grande_bete]]` · `[[Playtest1_Compte-rendu]]` · `[[Playtest1b_Addendum]]` · `[[Document_de_cadrage]]` (D059/D060)

---

*Version : 1.0 — Phase 1 — 2026-08-02. Compte-rendu du Playtest #2 (« La grande bête », Normal 13×9, Emmanuel MJ + 2 joueurs neufs). Résultat 7–6 Bien, bête nerfée à la volée. Verdict structurant : easy-to-play non atteint (joueurs incapables de distinguer les unités / retenir les règles) → pivot « big bang » vers une taxonomie visuelle C&C pure (D059/D060). Mûmakil/Furie à refondre (P5). Aucune règle ni profil retouché dans ce document.*
