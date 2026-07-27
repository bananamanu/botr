---
projet: "Batailles de la Terre du Milieu"
type: "faction"
phase: "1"
statut: "brouillon"
date_maj: "2026-07-27"
tags: [BdTdM, "type/faction", "peuple/harad", "statut/brouillon"]
version: "0.2"
---

# Harad — Profils d'unités *(escorte minimale + Mûmakil)*

> **Objet de ce document :** Profils Harad **en version minimale** pour accompagner le Mûmakil au **Playtest #2** (1er août ; test du gabarit et des règles de la bête, cadrage §4). En réponse aux tâches Todoist « Rédiger le profil d'unité Harad (minimal) » et « Résoudre le cas Mûmakil » (dues 29/07). **Pas** le roster complet du peuple — reporté.
>
> Statut : **brouillon à valider** — non testé. Le Mûmakil (§3) est spécifié par Emmanuel le 2026-07-27 ; forfaits de coût et rulings marqués provisoires.
>
> Aligné sur [[Regles_Base]] et [[Regles_Speciales]]. **Coût en points** : `Points_finaux = round((Mvt + PV + Attaque×D + Σ règles) ÷ 3) − 1` ([[Regles_Points]]).

---

## Choix d'identité (à acter)

- **Fil conducteur mécanique = [Poison].** Le [Howdah] du Mûmakil est déjà défini comme *[Plateforme de tir 2] + [Poison]* (D045). Les archers d'escorte portent aussi [Poison] — **première assignation réelle de [Poison] en V1** — reliant l'escorte à sa bête par un même thème (flèches empoisonnées haradrim). Fil analogue aux autres peuples (Mordor = [Horde], Easterling = [Mur de bouclier], Khand = [Arme Lourde], Rohan = mobilité).
- **Peu ou pas d'armure** : guerriers du désert légers.
- **Roster squelettique** : escorte (2 profils) + le Mûmakil comme unique pièce hors-norme.

---

## 1. Liste des troupes (brouillon)

| # | Unité | Type | Combat | **Points** |
|---|---|---|---|---|
| 1 | Archers du Harad | Infanterie | Tir | **3** |
| 2 | Lanciers du Harad *(optionnel)* | Infanterie | Mêlée | **5** |
| 3 | **Mûmakil** | Créature | *(charge — voir §3)* | **21** |

---

## 2. Escorte

### 1. Archers du Harad

| Type | Combat | Mvt | Attaque | Portée | PV | **Points** |
|---|---|---|---|---|---|---|
| Infanterie | Tir | 2 | 2 dés | 4 | 6 fig | **3** |

**Règles spéciales :** [Poison]
**Calcul :** `2 + 6 + 2×2 + [Poison](1) = 13 → round(13÷3)−1 =` **3**

> ⚠️ **Compression à trancher** : sans [Poison], brut 12 → 3 pts aussi (poison « gratuit », artefact documenté §2bis). **(a)** accepter *(recommandé, c'est une escorte)* ; **(b)** 3 dés de tir → 4 pts (poison réellement facturé).

### 2. Lanciers du Harad *(optionnel)*

| Type | Combat | Mvt | Attaque | Portée | PV | **Points** |
|---|---|---|---|---|---|---|
| Infanterie | Mêlée | 2 | 3 dés | — | 6 fig | **5** |

**Règles spéciales :** *(aucune — à trancher)*
**Calcul :** `2 + 6 + 3×3 = 17 → round(17÷3)−1 =` **5**

> ⚠️ **Règle à trancher** : proposé nu (minimal). [Réception de charge] rentre gratuitement sous compression (brut 19 → 5 pts inchangé) si tu veux la saveur « mur de lances » face aux Rohirrim.

---

## 3. Mûmakil — *pièce centrale, spécifiée par Emmanuel (2026-07-27)*

| Type | Combat | Mvt | Attaque | Portée | PV | **Points** |
|---|---|---|---|---|---|---|
| Créature | Mêlée *(par charge)* | 2 | 4 dés *(charge)* / 2 dés *(tir)* | 1–3 *(tir)* | 6 | **21** |

**Règles spéciales :** [Charge écrasante] *(refonte dédiée)* · [Howdah] *(= Plateforme de tir 2 + Poison)* · [Inamovible] · [Bête incontrôlable] *(refonte dédiée)*
**Règle intrinsèque du type :** Jamais Faible (Créature).
**Occupation :** 4 hexagones en colonne **1–2–1** (le modèle y tient parfaitement). **Pas de pivot (D10)** : le gabarit reste toujours orienté pointe vers le haut ; son déplacement est une **translation pure** (aucun changement d'orientation). *Direction de translation : par défaut libre (non contrainte vers le camp adverse) — à confirmer par Emmanuel au moment des pistes de mouvement.*

### Coût : 21 points *(par équivalence d'impact, D054)*

Le système additif de [[Regles_Points]] atteint sa limite sur une pièce unique : arbitrage d'Emmanuel de **chiffrer le Mûmakil par équivalence d'impact** plutôt que par la formule.

**Analyse d'équivalence (dé uniforme 1/6, B4 adopté) :**
- *Charge vs infanterie* : faces touchantes = Épées croisées (2) + Épée (1) + Couronne (2) → `(2+1+2)/6 = 0,83 fig/dé` × 4 = **~3,3 figurines** par unité traversée, sur *chaque* unité du trajet, **sans contre-attaque**.
- *Charge vs cavalerie* : `3/6 = 0,5 fig/dé` × 4 = **~2 figurines sur 3**, + recul **doublé**.
- *Durabilité* : PV 6, sans armure, ne contre-attaque jamais → un Éored (3 dés) inflige ~1 PV/attaque ; ~6 attaques pour le tuer, mais il en détruit ~1 par tour d'ici là.

→ **≈ 3-4 Éored** pour un affrontement équilibré, 5-6 pour le tuer proprement. Chiffrage retenu : **3 × Éored de cavalier (7 pts) = 21 pts**. Le vrai levier d'équilibre reste le **ratio de forces du scénario**, pas cette étiquette.

**Rappel forfaits** : [Inamovible] = **3 pts** (seule règle transférable, ajoutée au barème). [Charge écrasante] refonte et [Bête incontrôlable] refonte = **bespoke**, non transférables, absorbées dans les 21 pts.

### [Charge écrasante] — refonte dédiée Mûmakil *(format carte B)*

> À son activation, le Mûmakil **DOIT** effectuer un déplacement complet de **2 hexagones** (1 + 1). Le joueur désigne l'hexagone de tête visé, **sans tenir compte** des figurines amies ou ennemies présentes là où le Mûmakil finirait. Chaque unité dont un hexagone est traversé par son corps subit une **attaque de 4 dés** où la **Couronne inflige aussi une touche** ; cela a lieu **en phase de mouvement — ce n'est pas un combat** : aucune contre-attaque ni règle de combat ne s'applique. Toute **cavalerie** repoussée par cette charge **recule du double**. Si toutes les unités qui gênaient le passage sont détruites ou repoussées, il termine ses 2 hexagones ; sinon il s'arrête au dernier hexagone libre. **Le Mûmakil ne fait aucune attaque de mêlée en phase d'attaque.**

### [Inamovible] — *nouvelle règle (format carte B)*

> Le Mûmakil ne recule jamais : il ignore tout Drapeau ou résultat de retraite qui le viserait.

### [Bête incontrôlable] — refonte dédiée Mûmakil *(format carte B)*

> À son activation, **s'il est blessé**, lancez autant de dés que ses **PV restants** : sans aucune Couronne, posez un **marqueur Furie** et l'adversaire dirige immédiatement son déplacement. Tant qu'il porte une Furie, le camp adverse peut l'activer comme une de ses propres figurines. À la **fin de chaque tour**, le propriétaire relance **(PV restants + 1)** dés : une Couronne retire la Furie.

> 🎲 **Note de design** Auto-équilibrage par les PV : plus la bête est blessée, plus elle s'affole (1 PV → 1 dé, ~17 % de tenir) et moins elle se calme (1 PV → 2 dés de récupération, ~31 %). Spirale « géant blessé et incontrôlable ».

### [Howdah]

> En phase d'attaque, le Mûmakil tire **2 dés** sur une cible à **portée 1–3** en ligne de vue ; chaque **Couronne** inflige 1 touche supplémentaire (poison).

---

## 4. Rulings — tranchés (D054)

1. **Couronne dans la charge = touche** régie par la règle générale B4 (`Regles_Base` §2.3, D053) : **2 figurines contre l'infanterie**, 1 contre les autres cibles.
2. **Le Mûmakil ne contre-attaque jamais** — même quand il est lui-même ciblé en phase d'attaque. Toute son offense passe par la charge ; contre-jeu = le noyer sous le nombre.
3. **Mouvement impossible** : survivant non repoussable → arrêt au dernier hex libre ; aucun mouvement possible (bord/impassable) → activation perdue.
4. **Furie pendant l'activation du propriétaire** : l'adversaire dirige la charge **immédiatement**, règles [Charge écrasante] complètes, **y compris percuter les unités Harad**. ✅ confirmé.
5. **Activer un Mûmakil en Furie coûte une activation** de Section/carte au camp qui l'active. ✅ confirmé. Le test de reprise reste **toujours** lancé par le camp du Mal (fin de tour) — pari à double tranchant.
6. **Unités « affectées » par le trajet** = celles dont un hexagone est **nouvellement pénétré** par l'un des 4 hexagones du gabarit pendant la translation (D10, pas de pivot). *Seule zone d'ombre restante : la direction de translation autorisée — défaut « libre » en attendant les pistes de mouvement d'Emmanuel.*

---

## 5. Récapitulatif des règles spéciales (brouillon)

| Règle | Unités |
|---|---|
| [Poison] | Archers du Harad (1) — **première assignation V1** ; Mûmakil (via [Howdah]) |
| [Charge écrasante] *(refonte dédiée)* | Mûmakil (3) |
| [Howdah] = [Plateforme de tir 2] + [Poison] | Mûmakil (3) |
| [Inamovible] *(nouvelle)* | Mûmakil (3) |
| [Bête incontrôlable] *(refonte dédiée)* | Mûmakil (3) |
| *(aucune / [Réception de charge] ?)* | Lanciers du Harad (2) |

> 🔗 **Édits glossaire à répercuter dans [[Regles_Speciales]]** (après validation) : refonte de [Charge écrasante] (jusqu'ici « retirée de la V1 », redevient assignée sous forme dédiée Mûmakil) ; refonte de [Bête incontrôlable] (l'ancienne version « ne peut plus se déplacer » devient « affolement/Furie ») ; création de [Inamovible]. Coûts : [Charge écrasante] passe de 2 forfaitaire à la valeur arbitrée ; [Inamovible] et le nouveau malus [Bête incontrôlable] à ajouter à la table.

---

## 6. Points restants — à valider

- **Direction de translation du gabarit 1-2-1** (libre vs contrainte vers l'adversaire) — dernière inconnue de mouvement, à caler par Emmanuel (défaut « libre » en attendant).
- **Profils d'escorte** — Emmanuel fournira lui-même la liste d'unités Harad qu'il veut (archers/lanciers ci-dessus = brouillon en attente ; micro-choix poison a/b et règle des Lanciers parkés).
- **Vérification au Playtest #2** : les deux points de vigilance de B4 (recul bloqué ×2 et [Poison] ×2 contre l'infanterie), et l'étiquette 21 pts par équivalence.
- **Unité composite nommée ?** — point ouvert n°1 de [[Regles_Points]] §5 (aucune ici).

---

*Version : 0.3 — Phase 1 — 2026-07-27. Mûmakil chiffré à **21 pts par équivalence d'impact** (≈ 3 Éored, D054) ; rulings tranchés ; D10 (pas de pivot, translation pure) intégré ; B4 adopté comme règle générale de dégâts (`Regles_Base` §2.3, D053). Édits glossaire répercutés ([Charge écrasante]/[Bête incontrôlable] refondues, [Inamovible] créée à 3 pts). Escorte en attente des profils d'Emmanuel.*

*Version : 0.2 — Phase 1 — 2026-07-27. Ajout du profil complet du Mûmakil (spécifié par Emmanuel) : occupation 1-2-1, Créature Mvt 2 / 4 dés / PV 6, refonte de [Charge écrasante] (impact dédié en phase de mouvement) et de [Bête incontrôlable] (Furie), nouvelle règle [Inamovible], [Howdah] confirmé. Coût provisoire 8 pts, forfaits et rulings à arbitrer. Escorte inchangée. À valider — non testé.*
