---
projet: "Batailles de la Terre du Milieu"
type: "faction"
phase: "1"
statut: "brouillon"
date_maj: "2026-07-29"
tags: [BdTdM, "type/faction", "peuple/harad", "statut/brouillon"]
version: "0.4"
---

# Harad — Profils d'unités *(escorte + Mûmakil)*

> **Objet de ce document :** Profils Harad pour accompagner le Mûmakil au **Playtest #2** (1er août ; test du gabarit et des règles de la bête, cadrage §4). En réponse aux tâches Todoist « Rédiger le profil d'unité Harad » et « Résoudre le cas Mûmakil ». **Pas** le roster complet du peuple (unités de tir supplémentaires, héros — reportés).
>
> Statut : **brouillon à valider** — non testé. Le Mûmakil (§3) est spécifié par Emmanuel le 2026-07-27 ; forfaits de coût et rulings marqués provisoires.
>
> Aligné sur [[Regles_Base]] et [[Regles_Speciales]]. **Coût en points** : `Points_finaux = round((Mvt + PV + Attaque×D + Σ règles) ÷ 3) − 1` ([[Regles_Points]]).

---

## Choix d'identité (à acter)

- **Fil conducteur mécanique = [Poison].** Le [Howdah] du Mûmakil est déjà défini comme *[Plateforme de tir 2] + [Poison]* (D045). Toute l'escorte porte [Poison] — archers **et**, depuis D058, les trois profils de mêlée (Lanciers, Gardes serpents, Gardes serpent à cheval) — reliant l'escorte à sa bête par un même thème (venin haradrim), y compris sur des lames et non plus seulement des flèches. Fil analogue aux autres peuples (Mordor = [Horde], Easterling = [Mur de bouclier], Khand = [Arme Lourde], Rohan = mobilité).
- **Second fil = [Réception de charge].** Trois des quatre profils d'escorte (Lanciers, Gardes serpents, et [Arme Lourde 1] en variante montée) tiennent la ligne au contact plutôt que de harceler — cohérent avec un rôle d'escorte rapprochée du Mûmakil, pas de cavalerie légère.
- **Peu ou pas d'armure** : guerriers du désert légers.
- **Roster complet** : escorte (4 profils) + le Mûmakil comme unique pièce hors-norme.

---

## 1. Liste des troupes (brouillon)

| # | Unité | Type | Combat | **Points** |
|---|---|---|---|---|
| 1 | Archers du Harad | Infanterie | Tir | **3** |
| 2 | Lanciers du Harad | Infanterie | Mêlée | **5** |
| 3 | Gardes serpents | Infanterie | Mêlée | **6** |
| 4 | Gardes serpent à cheval | Cavalerie | Mêlée | **5** |
| 5 | **Mûmakil** | Créature | *(charge — voir §3)* | **21** |

---

## 2. Escorte

### 1. Archers du Harad

| Type | Combat | Mvt | Attaque | Portée | PV | **Points** |
|---|---|---|---|---|---|---|
| Infanterie | Tir | 2 | 2 dés | 4 | 6 fig | **3** |

**Règles spéciales :** [Poison]
**Calcul :** `2 + 6 + 2×2 + [Poison](1) = 13 → round(13÷3)−1 =` **3**

> ⚠️ **Compression à trancher** : sans [Poison], brut 12 → 3 pts aussi (poison « gratuit », artefact documenté §2bis). **(a)** accepter *(recommandé, c'est une escorte)* ; **(b)** 3 dés de tir → 4 pts (poison réellement facturé).

### 2. Lanciers du Harad

| Type | Combat | Mvt | Attaque | Portée | PV | **Points** |
|---|---|---|---|---|---|---|
| Infanterie | Mêlée | 2 | 2 dés | — | 6 fig | **5** |

**Règles spéciales :** [Poison] + [Réception de charge]
**Calcul :** `2 + 6 + 2×3 + [Poison](1) + [Réception de charge](2) = 17 → round(17÷3)−1 =` **5**

**Note narrative :** l'escorte au sol du Mûmakil, lances enduites du même poison que les archers — la piétaille qui referme la marche autour de la bête. [Réception de charge] leur donne un vrai rôle défensif de mur de lances, y compris face à la cavalerie du Rohan.

> 🔄 **2026-07-29 (D058)** : attaque ramenée de 3 à **2 dés**, ajout de [Poison] et [Réception de charge] (décision d'Emmanuel — l'ancienne version nue « à trancher » est close). Coût final inchangé à 5 pts (la baisse d'attaque brute compense exactement l'ajout des deux règles, `Points_bruts` reste à 17). Première assignation de [Réception de charge] hors piquiers de Gondor/Easterling, et première assignation de [Poison] à une unité de mêlée (jusqu'ici réservé au tir) — voir refonte de la règle dans [[Regles_Speciales]].

### 3. Gardes serpents

| Type | Combat | Mvt | Attaque | Portée | PV | **Points** |
|---|---|---|---|---|---|---|
| Infanterie | Mêlée | 2 | 3 dés | — | 6 fig | **6** |

**Règles spéciales :** [Poison] + [Réception de charge]
**Calcul :** `2 + 6 + 3×3 + [Poison](1) + [Réception de charge](2) = 20 → round(20÷3)−1 =` **6**

**Note narrative :** la garde d'élite du Harad, aux lames traitées au venin, formée pour tenir le contact plutôt que le harceler — l'échelon au-dessus des Lanciers (3 dés contre 2), même thème du poison et de la lance reçue en pointe.

> 🎲 **Note de design** Premier profil du peuple à cumuler [Poison] et [Réception de charge] sur la même unité — les deux thèmes du roster (venin haradrim, discipline de contact) convergent enfin sur une seule troupe plutôt que d'être séparés entre archers et lanciers.

### 4. Gardes serpent à cheval

| Type | Combat | Mvt | Attaque | Portée | PV | **Points** |
|---|---|---|---|---|---|---|
| Cavalerie | Mêlée | 3 | 3 dés | — | 3 fig | **5** |

**Règles spéciales :** [Poison] + [Arme Lourde 1]
**Calcul :** `3 + 3 + 3×3 + [Poison](1) + [Arme Lourde 1](2) = 18 → round(18÷3)−1 =` **5**

**Note narrative :** la version montée des Gardes serpents — arme lourde plutôt que réception de charge, cohérent avec une cavalerie qui frappe et poursuit plutôt qu'elle n'encaisse en formation. Poison conservé : même venin, porté à cheval.

> ⚠️ **Hypothèse posée** : [Arme Lourde 1] (X=1), non précisé par Emmanuel — alignée sur le seul autre usage à valeur unique du glossaire (Guerriers de Lossarnach, Helmingas de Grimbolg). À confirmer.

---

## 3. Mûmakil — *pièce centrale, spécifiée par Emmanuel (2026-07-27)*

| Type | Combat | Mvt | Attaque | Portée | PV | **Points** |
|---|---|---|---|---|---|---|
| Créature | Mêlée *(par charge)* | 2 | 4 dés *(charge)* / 2 dés *(tir)* | 1–3 *(tir)* | 6 | **21** |

**Règles spéciales :** [Charge écrasante] *(refonte dédiée)* · [Howdah] *(= Plateforme de tir 2 + Poison)* · [Inamovible] · [Bête incontrôlable] *(refonte dédiée)*
**Règle intrinsèque du type :** Jamais Faible (Créature).
**Occupation :** 4 hexagones en colonne **1–2–1** (le modèle y tient parfaitement). **Pas de pivot (D10)** : le gabarit reste toujours orienté pointe vers le haut ; son déplacement est une **translation pure** (aucun changement d'orientation). **Direction de translation : libre** — tranché par Emmanuel (2026-07-29, voir `[[Playtest2_La_grande_bete]]`).

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
6. **Unités « affectées » par le trajet** = celles dont un hexagone est **nouvellement pénétré** par l'un des 4 hexagones du gabarit pendant la translation (D10, pas de pivot). Direction de translation **libre**, tranchée le 2026-07-29.

---

## 5. Récapitulatif des règles spéciales

| Règle | Unités |
|---|---|
| [Poison] | Archers du Harad (1) · Lanciers du Harad (2) · Gardes serpents (3) · Gardes serpent à cheval (4) · Mûmakil (via [Howdah]) |
| [Réception de charge] *(refondue D058, inconditionnelle)* | Lanciers du Harad (2) · Gardes serpents (3) |
| [Arme Lourde 1] | Gardes serpent à cheval (4) |
| [Charge écrasante] *(refonte dédiée)* | Mûmakil |
| [Howdah] = [Plateforme de tir 2] + [Poison] | Mûmakil |
| [Inamovible] *(nouvelle)* | Mûmakil |
| [Bête incontrôlable] *(refonte dédiée)* | Mûmakil |

> 🔗 **Édits glossaire à répercuter dans [[Regles_Speciales]]** (après validation) : refonte de [Charge écrasante] (jusqu'ici « retirée de la V1 », redevient assignée sous forme dédiée Mûmakil) ; refonte de [Bête incontrôlable] (l'ancienne version « ne peut plus se déplacer » devient « affolement/Furie ») ; création de [Inamovible]. Coûts : [Charge écrasante] passe de 2 forfaitaire à la valeur arbitrée ; [Inamovible] et le nouveau malus [Bête incontrôlable] à ajouter à la table.

---

## 6. Points restants — à valider

- **Direction de translation du gabarit 1-2-1** (libre vs contrainte vers l'adversaire) — **tranchée : libre** (Emmanuel, 2026-07-29, voir `[[Playtest2_La_grande_bete]]`).
- **Profils d'escorte** — ✅ tranchés (D058) : Lanciers du Harad, Gardes serpents, Gardes serpent à cheval. Reste ouvert : la valeur X de [Arme Lourde X] sur les Gardes serpent à cheval, posée à 1 par hypothèse (§2 profil 4).
- **[Réception de charge] refondue en inconditionnelle** (D058) — coût de la règle laissé provisoire à 2 pts dans [[Regles_Points]], à réévaluer après un premier usage à la table sous cette forme plus généreuse.
- **Vérification au Playtest #2** : les deux points de vigilance de B4 (recul bloqué ×2 et [Poison] ×2 contre l'infanterie), et l'étiquette 21 pts par équivalence.
- **Unité composite nommée ?** — point ouvert n°1 de [[Regles_Points]] §5 (aucune ici).

---

*Version : 0.4 — Phase 1 — 2026-07-29. **Roster d'escorte complété (D058)** : Lanciers du Harad passés à 2 dés + [Poison] + [Réception de charge] (5 pts, inchangé) ; deux nouveaux profils, **Gardes serpents** (Infanterie, 3 dés + [Poison] + [Réception de charge], 6 pts) et **Gardes serpent à cheval** (Cavalerie, 3 dés + [Poison] + [Arme Lourde 1], 5 pts). [Réception de charge] refondue en bonus de contre-attaque inconditionnel dans [[Regles_Speciales]] (répercuté depuis Gondor/Easterling). Direction de translation du gabarit tranchée en « libre » (voir `[[Playtest2_La_grande_bete]]`). Roster d'escorte à 4 profils, non testé.*

*Version : 0.3 — Phase 1 — 2026-07-27. Mûmakil chiffré à **21 pts par équivalence d'impact** (≈ 3 Éored, D054) ; rulings tranchés ; D10 (pas de pivot, translation pure) intégré ; B4 adopté comme règle générale de dégâts (`Regles_Base` §2.3, D053). Édits glossaire répercutés ([Charge écrasante]/[Bête incontrôlable] refondues, [Inamovible] créée à 3 pts). Escorte en attente des profils d'Emmanuel.*

*Version : 0.2 — Phase 1 — 2026-07-27. Ajout du profil complet du Mûmakil (spécifié par Emmanuel) : occupation 1-2-1, Créature Mvt 2 / 4 dés / PV 6, refonte de [Charge écrasante] (impact dédié en phase de mouvement) et de [Bête incontrôlable] (Furie), nouvelle règle [Inamovible], [Howdah] confirmé. Coût provisoire 8 pts, forfaits et rulings à arbitrer. Escorte inchangée. À valider — non testé.*
