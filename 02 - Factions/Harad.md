---
projet: "Batailles de la Terre du Milieu"
type: "faction"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-08-23"
tags: [BdTdM, "type/faction", "peuple/harad", "statut/brouillon"]
version: "1.7"
---

# Harad — Profils d'unités *(escorte + Pillards + Mûmakil)*

> **Objet de ce document (P8 — simplification radicale, D101, généralisée).** Même principe qu'à Gondor : plus aucun badge d'office. [Poison] — trait matériel — devient lui aussi une **option**, pas un défaut. Le Mûmakil reste hors matrice, inchangé.
>
> Aligné sur [[Regles_Base]] v0.17, [[Regles_Speciales]] v0.30, [[Regles_Points]] v0.29.

---

## 1. Faction du Harad — [Poison]

Arcane inflige 1 touche. **Outil optionnel**, +1 brut, disponible sur tout le roster d'escorte (1-6).

---

## 2. Liste des troupes (coûts de base — sans option)

| # | Unité | Type | Combat | Classe | Options disponibles | **Points** |
|---|---|---|---|---|---|---|
| 1 | Archers du Harad | Infanterie | Distance | 🟢 | Faction | **3** |
| 2 | Lanciers du Harad | Infanterie | Mêlée | 🟢 | Faction, Bannière | **3** |
| 3 | Gardes serpents | Infanterie | Mêlée | 🔵 | Faction *(pas de Bannière, D109)* | **4** |
| 4 | Gardes serpent à cheval | Cavalerie | Mêlée | 🔵 | Faction, Bannière | **6** |
| 5 | Pillards haradrim (mêlée) | Cavalerie | Mêlée | 🟢 | Faction, **Bannière** *(D109)* | **5** |
| 6 | Pillards haradrim (archers) | Cavalerie | Distance | 🟢 | Faction | **3** |
| 7 | Mûmakil — *signature* | Créature | Mêlée *(charge)* | 🔴 *(nominal)* | *(hors matrice)* | **15** |

**Coûts avec option Faction [Poison] (+1 brut) :**

| # | Unité | Base | +Faction |
|---|---|---|---|
| 2 | Lanciers du Harad | 3 | 3 *(absorbé)* |
| 3 | Gardes serpents | 4 | **5** |
| 4 | Gardes serpent à cheval | 6 | 6 *(absorbé)* |
| 5 | Pillards haradrim (mêlée) | 5 | 5 *(absorbé)* |

**Coûts avec option Bannière (+2 brut) :**

| # | Unité | Base | +Bannière |
|---|---|---|---|
| 2 | Lanciers du Harad | 3 | **4** |
| 4 | Gardes serpent à cheval | 6 | 6 *(absorbé)* |
| 5 | Pillards haradrim (mêlée) | 5 | **6** |

> 🔄 **Baisses par rapport à l'ancien roster (P7c).** Gardes serpents 5→**4** (perd Inébranlable+JF par défaut), Gardes serpent à cheval 7→**6** (perd Relance 1 par défaut). **Retouche Emmanuel (D109) :** Gardes serpents perdent l'option Bannière (troupe d'élite rapprochée, pas une formation à étendard) ; les Pillards haradrim à cheval (mêlée, 5) la gagnent à la place (cavalerie légère organisée, plus cohérent avec un porte-étendard monté).

---

## 3. Le Mûmakil — pièce unique *(D054 ; refondue P5/D079 ; défense refondue P8/D103)*

| Type | Combat | Classe | Mouvement | Attaque | Portée | PV | **Points** |
|---|---|---|---|---|---|---|---|
| Créature | Mêlée *(par charge)* | 🔴 *(nominal)* | 2 *(translation 1-2-1)* | 4 dés *(charge)* / 2 dés *(tir)* | 1–3 *(tir)* | **8** | **15** |

**Règles spéciales :** [Charge écrasante] *(bespoke)* · [Howdah] *(= [Plateforme de tir 2])* · [Inébranlable ∞] · [Bête incontrôlable] *(bespoke, Furie)*.

**Défense (D103, refonte P8) :** porte désormais **[Armure]** (sans X) au lieu de l'ancien duo [Armure 1] intrinsèque + [Protection 1] payant — jet de sauvetage 1d6 contre chaque touche reçue (mêlée ou tir), annulée sur Arcane. Reste intrinsèque, gratuit.

**Occupation :** 4 hexagones en colonne **1–2–1**. Pas de pivot, translation pure, direction libre (D058).

**Coût : 15 points.** Détail du calcul (recalculé D103, [Protection 1] superseded par [Armure] intrinsèque) :

| Élément | Valeur brute |
|---|---|
| Socle (Mvt 2 + PV 8) | 10 |
| Charge principale (4 dés mêlée, D=3) | 12 |
| Howdah (tir 2 dés, D=2) | 4 |
| [Bête incontrôlable] (malus résiduel) | −1 |
| **Sous-total tarifable au barème standard** | **25** |
| [Charge écrasante] *(bespoke, jugement)* | 15 |
| [Inébranlable ∞] *(bespoke, jugement, tarif barème 6 — voir [[Regles_Points]] §3.4)* | 6 |
| **Brut total** | **47** |
| **Final = round(47÷3)−1** | **15** |

*(Inchangé — la suppression de la ligne [Protection 1] (−1 brut) est absorbée par la compression : 47→15, comme 48→15 avant.)*

#### [Charge écrasante] *(bespoke)*

> À son activation, le Mûmakil **DOIT** effectuer un déplacement complet de **2 hexagones** (1 + 1) vers l'hexagone de tête visé, **sans tenir compte** des figurines présentes. Chaque unité dont un hexagone est traversé subit une **attaque de 4 dés** où l'**Arcane inflige aussi une touche** ; cela se passe **en phase de mouvement — pas de combat, aucune contre-attaque**. Toute **cavalerie** repoussée recule du **double**. S'il reste des unités gênantes non détruites/repoussées, il s'arrête au dernier hexagone libre. **Aucune attaque de mêlée en phase d'attaque.**

#### [Bête incontrôlable] *(bespoke, refondue P5/D079)*

> Le Mûmakil entre en **Furie** dès qu'il tombe à **son dernier point de vie (1 PV)**. Tant qu'il est à 1 PV : **chaque tour, un tirage à pile ou face détermine qui contrôle la bête** ce tour-là. Le Mûmakil s'active obligatoirement au tour du Mal, sans consommer de carte de commandement ; si le tirage désigne le Bien, c'est lui qui dirige le mouvement et l'attaque ce tour-là. Dure jusqu'à la mort du Mûmakil.

#### [Howdah]

> **= [Plateforme de tir 2]** : une attaque de tir de **2 dés**, portée **1–3**, en plus de la mêlée.

---

## 4. Variante avec Leader — Playtest #4

**Gardes serpent à cheval avec Suladan** (Leader, Destin 2) : brut = 21 (base) + 1 (Faction, prise) + 4 (Leader) + 4 (Destin 2) = 30 → round(30÷3)−1 = **9**.

---

## 5. Récapitulatif

| Option | Disponible sur |
|---|---|
| **Faction [Poison]** | 1, 2, 3, 4, 5, 6 |
| **Bannière** | 2, 4, 5 |
| **Leader/Destin** | Suladan (Gardes serpent à cheval) au Pelennor |
| **Hors matrice, signature** | Mûmakil (§3) — [Armure] intrinsèque, D103 |

---

## 6. Points ouverts transverses

Inchangés — le Mûmakil reste au prix fixé en P5 (D079), non retouché par ce chantier.

---

*Version : 1.7 — Phase 1 — 2026-08-23. **Retouches Emmanuel (D109) + refonte défense créature (D103) + correction.** Bannière retirée des Gardes serpents (3), ajoutée aux Pillards haradrim à cheval mêlée (5). **Correction : restauration du détail complet du Mûmakil (§3)**, perdu par erreur lors de la réécriture v1.6 — Charge écrasante, Bête incontrôlable, Howdah réintégrés, défense mise à jour vers la nouvelle règle [Armure] (D103, remplace [Armure 1]+[Protection 1]) : coût final inchangé (**15** pts, absorbé par la compression).*

*Version : 1.6 — Phase 1 — 2026-08-23. **Simplification radicale généralisée (D101).** [Poison] devient une option plutôt qu'un trait automatique. Coûts de base recalculés en pure matrice : Gardes serpents 5→**4**, Gardes serpent à cheval 7→**6**. Nouvelle variante : Gardes serpent à cheval avec Suladan = **9** pts.*

*Version : 1.5 — Phase 1 — 2026-08-23. **P8 — recalcul complet (D097/D098).** [Poison] confirmé trait matériel, aucun changement de coût de base sur l'escorte. Nouvelle variante chiffrée : Gardes serpent à cheval avec Suladan (Leader, Destin 2) = **10** pts. Anciens badges Spéciale/Élite renommés « règles socle ». Mûmakil inchangé.*

*Version : 1.3 — Phase 1 — 2026-08-16. **Corrections de relecture — revue de finalisation « Verrouillage v1.0 ».** En-tête « Aligné sur » rafraîchi (v0.12/v0.26/v0.22 → v0.13/v0.27/v0.24, versions réelles depuis P7c). Aucune décision mécanique — pas de numéro D.*

*Version : 1.2 — Phase 1 — 2026-08-13. **Collapse du système de badges (D080/D081, tâche P7c) — sans effet sur les coûts.** Harad était déjà conforme : [Poison] devient un trait de peuple plutôt qu'un badge (§1, §2 réécrits) ; le Mûmakil est confirmé pièce **Signature**, exemptée du plafond à 1 badge secondaire. Aucun changement de points.*

*Version : 1.1 — Phase 1 — 2026-08-09. **Refonte P5 du Mûmakil (D079).** [Bête incontrôlable] refondue : la Furie devient un état déterministe à 1 PV (fini le test PV-scaling jugé trop punitif), contrôle tiré à pile ou face chaque tour, activation garantie et gratuite au tour du Mal. PV 6→8. Nouveau [Protection 1] contre le tir (formalise le houserule PT2). Coût recalculé au barème normal : 21→**15 pts** (détail du calcul dans le profil, bespoke Charge écrasante/Inébranlable ∞ chiffrées par jugement analogique, jamais tarifées avant P5).

*Version : 1.0 — Phase 1 — 2026-08-08. **Refonte P4 (D078) : première re-expression complète du roster Harad, sixième et dernier peuple.** Badge Faction = [Poison] (fil conducteur déjà acté, désormais universel sur tout le roster) ; Badge Spéciale = [Relance 1] (ex-[Arme Lourde 1], Gardes serpent à cheval) ; Badge Élite = [Inébranlable 1] + Jamais Faible (Gardes serpents). **Deux nouveaux profils : Pillards haradrim**, cavalerie légère 🟢 de raid, en version mêlée (Faction+Spéciale, 6 pts) et tir (Faction seule, 4 pts). Escorte reclassée sur la taxonomie (Archers/Lanciers 🟢, Gardes serpents/à cheval 🔵) ; [Réception de charge] et l'ancienne valeur X d'[Arme Lourde 1] abandonnées avec le reste du système pré-taxonomie. Mûmakil : règles bespoke inchangées, terminologie mise à jour ([Inamovible]→[Inébranlable ∞]), gagne [Armure 1]/[Peur 1] intrinsèques (D071) sans repricing — point de veille signalé. Roster porté à 6 profils + Mûmakil. Non testé — validation P7a. **Sixième et dernier roster du sprint P4 : le mandat de re-expression est complet.***

*Version : 0.4 — Phase 1 — 2026-07-29. **Roster d'escorte complété (D058)** : Lanciers du Harad passés à 2 dés + [Poison] + [Réception de charge] (5 pts, inchangé) ; deux nouveaux profils, **Gardes serpents** (Infanterie, 3 dés + [Poison] + [Réception de charge], 6 pts) et **Gardes serpent à cheval** (Cavalerie, 3 dés + [Poison] + [Arme Lourde 1], 5 pts). [Réception de charge] refondue en bonus de contre-attaque inconditionnel dans [[Regles_Speciales]] (répercuté depuis Gondor/Easterling). Direction de translation du gabarit tranchée en « libre » (voir `[[Playtest2_La_grande_bete]]`). Roster d'escorte à 4 profils, non testé.*

*Version : 0.3 — Phase 1 — 2026-07-27. Mûmakil chiffré à **21 pts par équivalence d'impact** (≈ 3 Éored, D054) ; rulings tranchés ; D10 (pas de pivot, translation pure) intégré ; B4 adopté comme règle générale de dégâts (`Regles_Base` §2.3, D053). Édits glossaire répercutés ([Charge écrasante]/[Bête incontrôlable] refondues, [Inamovible] créée à 3 pts). Escorte en attente des profils d'Emmanuel.*

*Version : 0.2 — Phase 1 — 2026-07-27. Ajout du profil complet du Mûmakil (spécifié par Emmanuel) : occupation 1-2-1, Créature Mvt 2 / 4 dés / PV 6, refonte de [Charge écrasante] (impact dédié en phase de mouvement) et de [Bête incontrôlable] (Furie), nouvelle règle [Inamovible], [Howdah] confirmé. Coût provisoire 8 pts, forfaits et rulings à arbitrer. Escorte inchangée. À valider — non testé.*
