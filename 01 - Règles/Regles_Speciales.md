---
projet: "Batailles de la Terre du Milieu"
type: "regles"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-08-08"
tags: [BdTdM, "type/regles", "phase/1", "statut/brouillon"]
version: "0.19"
---

# Batailles de la Terre du Milieu — Règles spéciales

> **Objet de ce document (refonte P2, D062).** Depuis le pivot « taxonomie visuelle » (D059–D061), l'identité d'une unité — **classe** (couleur = dés), **type** (socle), **mode** (token mêlée/distance) — se lit sur le plateau, et l'essentiel des règles en **découle** au lieu d'être mémorisé profil par profil. Ce glossaire n'est donc plus un catalogue : c'est la **référence des signatures**, la courte liste des capacités marquantes qu'un adversaire doit pouvoir identifier **d'un coup d'œil**. Il conserve en tête le **socle générique** (vocabulaire défensif/offensif universel), renvoie à [[Regles_Base]] pour tout ce qui est intrinsèque à la taxonomie, et liste en fin de document ce qui a été retiré.
>
> Aligné sur **[[Regles_Base]] v0.6** et **[[Terrain]]**. Les règles universelles (Faible, contre-attaque, avance, retraite, faces de dé) sont définies dans [[Regles_Base]], pas ici.

> 🔄 **Tri du glossaire — 2026-08-04 (P2, D062)**
> Le glossaire a fondu. En synthèse :
> - **Intrinsèque à la taxonomie** (sort du profil, se lit au plateau) : [Mobilité], [Poursuite] et [Armure 1] dérivées de la case classe × type × mode. *Grille complète désormais écrite dans [[Regles_Base]] §2.4 (revue classe × type, D063) — source de vérité unique.*
> - **Fusions** : [Perforant X] → **[Relance X]** (une seule règle de relance, mêlée ou tir) · [Inamovible] → **[Inébranlable ∞]** (une valeur, pas un mot-clé de plus).
> - **Coupées** : [Réception de charge], [Mur de bouclier] (→ [Armure 1]), [Martyre], [Meute X], [Souffle de feu], [Immunisé au feu], [Immunisé au poison], [Terrain favori : X], [Rechargement], [Déploiement avancé]. Détail et renvois au §6. *([Arme de jet X], coupée à P2, a été restaurée au socle générique à P4/D068 — voir §2.)*
> - **Chaque peuple garde une signature identitaire** ; avec le badge **Élite**, la classe et le type, cela suffit à différencier les unités. Le plafond reste **1–2 règles spéciales par unité**.
> - Répercussions sur les profils, les coûts et les scénarios **renvoyées à P3 (coûts) / P4 (re-expression des rosters)** — voir §6. Les comptes-rendus de playtest ne sont pas modifiés (historique).

---

## Table des matières

1. [[#Conventions]]
2. [[#Socle générique]]
3. [[#Règles intrinsèques (dérivées de la taxonomie)]]
4. [[#Signatures]]
5. [[#Récapitulatif alphabétique]]
6. [[#Retiré au tri P2]]
7. [[#Différées — Phase 2+]]

---

## Conventions

### Notation

- **[Règle]** : nom entre crochets — standard dans tous les profils.
- **[Règle X]** : règle avec une valeur numérique (ex. [Armure 1], [Relance 2]).

### Trois familles

| Famille | Rôle | Où c'est défini |
|---|---|---|
| **Socle générique** | Vocabulaire universel disponible à tout profil (défense, relance, poursuite…) | §2 de ce document |
| **Intrinsèque** | Découle de la combinaison classe × type × mode — **ne se note pas sur le profil**, se lit au plateau | [[Regles_Base]] (§2, §6) |
| **Signature** | Capacité marquante, **1–2 max par unité**, réservée aux pièces d'identité de peuple et aux pièces uniques | §4 de ce document |

### Où se résolvent les signatures

L'ordre de résolution d'un combat est celui de [[Regles_Base]] §7.1. Les signatures s'y insèrent ainsi :

1. **Avant le décompte** — relances : [Relance X], [Horde] (+1 dé).
2. **Au décompte des touches** — effets de **Couronne** : [Poison], [Charge écrasante], [Howdah]… (chaque Couronne devient une touche ou un effet, selon la règle).
3. **Réductions défensives** — [Armure X] puis [Protection X].
4. **Retraites** — les **Drapeaux**, plus les Drapeaux issus de la face **Arcane** via [Peur X] ; [Inébranlable X] (jusqu'à ∞) absorbe le tout, quelle qu'en soit la source.

> 🎲 **Note** [Peur X] (Arcane) et les règles à **Couronne** vivent sur des faces différentes : elles ne se disputent jamais le même dé.

> 🔗 **Voir aussi** [[Regles_Base]] §2 (types et faces de dé), §7 (combat), §9 (retraite). Les anciennes tables « règles intrinsèques des types » et « priorité de résolution » de ce document sont **supprimées** : périmées par [[Regles_Base]] v0.6 (jamais-Faible au socle, double-touche retirée, 1 touche = 1 figurine/PV).

---

## Socle générique

Vocabulaire universel. Ne compte **pas** dans le plafond de signatures d'une unité, mais reste soumis au bon sens de lisibilité.

### [Armure X]

Lorsque cette unité reçoit une attaque de **mêlée**, elle retire **X faces Épée** des résultats avant de compter les touches. Les faces **Épées croisées** ne sont jamais affectées. Sans effet contre le **tir**.

> Remplace désormais l'ancienne [Mur de bouclier] sur les profils Easterling (coupée en P2, → [Armure 1], voir §6).

### [Protection X]

Une unité en position protégée (terrain) ignore **X touches** après décompte des dégâts.

| Position | Valeur |
|---|---|
| Ruine | 1 |
| Bâtiment solide | 2 |
| Fortification | 3 |

> 🔗 **Voir aussi** [[Terrain]] §9.

### [Inébranlable X]

Cette unité ignore **X résultats de retraite** par attaque reçue, quelle qu'en soit la source (dés, [Peur X], cartes, effets).

- **Convention [Inébranlable ∞]** : une unité qui ne recule **jamais** (elle ignore tout Drapeau). Remplace l'ancienne règle [Inamovible] (fusionnée en P2). Réservée aux grandes créatures ancrées — premier porteur : le Mûmakil.

> 💡 [Inébranlable 2] face à 3 Drapeaux → recule d'1 seul hexagone. [Inébranlable ∞] → ne recule pas.

### [Poursuite X]

Alternative à l'avance (voir [[Regles_Base]] §8.2) : après avoir éliminé ou fait reculer une cible adjacente, se déplacer de 1 à X hexagones puis effectuer **une attaque supplémentaire** contre une unité adjacente à la nouvelle position. Une fois par tour.

> Gradée selon la pièce (ex. 1 pour la cavalerie de ligne, 2 pour un éored). Reste un mot-clé de profil, **pas** un trait automatique de la Cavalerie (arbitrage D062, point 6).

### [Férocité]

Cette unité peut effectuer sa **contre-attaque même si l'attaque subie la force à reculer** : elle résout d'abord la contre-attaque, **puis** recule normalement. C'est l'exception à la condition « restée sur son hexagone » de [[Regles_Base]] §7.6.

> 💡 Attaquée avec 3 Épées + 1 Drapeau, une unité [Férocité] contre-attaque quand même, immédiatement, avant de reculer d'1 hexagone.

### [Relance X]

Après le lancer, le joueur peut **relancer X dés** de son choix (mêlée **ou** tir, selon le mode de l'unité). Chaque dé n'est relancé qu'une fois.

> 🔄 **Fusion — P2 (D062)** : absorbe l'ancienne [Perforant X] (même mécanique de relance, jadis réservée au tir). Le **token de mode** indique quels dés sont relancés — un seul mot-clé à retenir. Nom historique conservé (le plus assigné). Porteurs : armes de hache lourde (Khand), gourdin du Troll, et l'archerie d'élite qui le portait sous [Perforant] (Racine Noire, Gondor).

### [Arme de jet X]

Le tour où cette unité **s'est déplacée puis attaque en mêlée**, chaque face **Cible** obtenue compte comme **une touche supplémentaire** (au lieu d'un échec) — les projectiles lancés avant le choc.

> 🔄 **Restaurée — P4 (D068)**, après avoir été coupée au tri P2 (D062) faute de porteur en attente de re-expression. Réintégrée au socle générique à l'occasion de la re-expression du Rohan : porteur d'origine (Milice lige, D044), désormais généralisable à toute unité de mêlée dont l'équipement le justifie.

### [Mercenaire]  *(coût négatif)*

Chaque **retrait forcé** (recul de combat) de cette unité compte **double** (déplacement de recul et éventuels dégâts de collision doublés, selon la règle qui déclenche le retrait).

> 🔄 **Créée — P4 (D070)**, premier badge/règle à **coût négatif** du projet : **−2 brut**, symétrique au coût des badges positifs existants. Traduit un moral fragile et une motivation strictement pécuniaire — l'unité cède plus volontiers le terrain qu'une troupe régulière ou fidèle. Porteuse d'origine : Khand (badge Faction, D070) — généralisable à toute future troupe mercenaire d'un autre peuple.

---

## Règles intrinsèques (dérivées de la taxonomie)

Ces effets **ne se notent pas sur le profil** : ils découlent de la classe (couleur), du type (socle) et du mode (token), et se lisent au plateau. Leur **définition de référence** — la grille complète classe × type × mode — vit dans **[[Regles_Base]] §2.4** (revue D063). Ce document n'en rappelle que le cas fondateur, à titre d'illustration :

### 🟢 Léger + mode distance → [Mobilité 1]

Toute unité **légère (🟢, 2 dés) en mode distance** décroche après avoir tiré : **après son attaque**, elle peut se déplacer de **1 hexagone supplémentaire**. Sans attaque ce tour, pas de bonus (elle bouge de son Mouvement normal).

> 🎲 Identité **harceleur** (tir-puis-décroche), lisible d'un coup d'œil (vert + token distance) — plus besoin d'écrire [Mobilité 1] sur ces profils. Formule pour l'aide de jeu : *« Tu frappes, puis tu décroches. Pas d'attaque, pas de bonus. »*

> 🔄 **P2 (D062) → revue classe × type (D063)** : absorbe les anciennes assignations éparses de [Mobilité 1] (Rangers du Gondor et famille, Pillards de Khand, pisteurs orques). La grille complète est désormais écrite dans **[[Regles_Base]] §2.4** — [Mobilité] est étendue à la cavalerie légère (**2**) et standard (**1**), et [Armure 1] / [Poursuite] ajoutées aux cases lourdes et de cavalerie de mêlée. Contraste voulu avec [Double Tir] (§4), signature de l'archer **immobile** qui, lui, troque la mobilité contre le volume.

---

## Signatures

Capacités marquantes. **1–2 maximum par unité.** Chaque peuple porte **une** signature identitaire ; les pièces uniques et les créations bespoke complètent la liste. L'objectif « **une seule** signature bien nette par peuple » se finalise à la re-expression des rosters (P4) ; certaines signatures ci-dessous coiffent encore plusieurs unités d'un même peuple.

### Signatures de peuple

#### [Horde]  — *Mordor*

Tant que cette unité **n'a perdu aucun PV** : **+1 dé d'attaque** et **[Inébranlable 1]**. Les deux bonus disparaissent **définitivement** dès la première perte.

> 🎲 « Très fort au premier choc, fragile ensuite » : la horde d'orques nombreuse et prompte à rompre. Condition lisible au nombre de figurines, sans jeton. Inspirée des *Warriors* de C&C Ancients. Assignée aux bandes d'orques (pas à l'Uruk-hai, élite qui tient).

#### [Poison]  — *Harad*

Lorsque cette unité attaque, chaque face **Couronne** inflige **1 touche supplémentaire**.

> 🎲 Fil conducteur du Harad (flèches et lames empoisonnées). Porté par les Lanciers, les Gardes serpents et la volée du Mûmakil ([Howdah]).

#### [Double Tir]  — *Easterling*

Si cette unité **ne s'est pas déplacée** ce tour, elle effectue une **seconde attaque à distance** (même cible ou une autre, à portée et en ligne de vue).

> 🎲 La discipline de la ligne qui tient sa position et double la salve — signature glanceable de l'archer d'Easterling, miroir de l'archer **mobile** (intrinsèque [Mobilité 1], §3). Depuis la coupe de [Mur de bouclier] (P2), c'est [Double Tir] qui porte l'identité de tir discipliné du peuple ; sa protection passe par [Armure 1] (socle).

*(Khand : identité portée par le badge Faction [Mercenaire] (moral fragile, coût réduit) et le badge Spéciale [Relance 1] (hache lourde) — voir §2. Gondor : identité portée par l'armure lourde ([Armure X], socle) et ses pièces uniques.)*

### Signatures de pièce unique

#### [Peur X]  — *Troll du Mordor*

Chaque face **Arcane** obtenue en attaque compte comme **X Drapeaux** contre la cible (au lieu d'un échec). N'inflige **aucune touche** : la Peur fait rompre, elle ne tue pas. Annulable par l'[Inébranlable X] de la cible.

> 🎲 Réutilise la face Arcane (morte par défaut) et pose le premier jalon de la couche Leadership (Phase 2). Versions « Terreur » (X élevé, Nazgûl/Roi-Sorcier) différées (§7).

#### [Archer en mêlée]  — *Compagnie Grise (Legolas)*

Les faces **Cible** infligent aussi une touche lors d'une attaque de **mêlée** (normalement inertes en mêlée).

> 🎲 Précision hors norme, dangereuse jusqu'au corps à corps.

#### [Vigilant]  — *Éored d'éclaireur (Rohan)*

La cible d'une attaque de cette unité **ne peut pas la contre-attaquer**, quelle que soit l'issue. Mêlée ou tir à bout portant.

> 🎲 Cavalerie légère de harcèlement : elle frappe et se replace sans jamais laisser l'adversaire répliquer. Adaptée des *Riverwatch Riders* (BattleLore V2).

#### [Prise de flanc]  — *Éored de cavalier (Rohan)*

Tant qu'une **unité ennemie** est **adjacente** à cette unité, chaque **autre unité amie** attaquant cette ennemie ajoute **1 dé**. Cette unité n'en profite pas pour ses propres attaques. Les sources multiples se cumulent (1 dé chacune).

> 🎲 Rôle de **soutien** (pas de dégât propre) : le cavalier tient la faille ouverte, les lances plus lourdes l'exploitent. Second mot-clé des *Riverwatch Riders*, séparé de [Vigilant].

#### [Plateforme de tir X]  — *sans porteur actif*

En plus de son attaque normale, cette unité effectue **une attaque de tir de X dés**, portée **1–3**, en ligne de vue, **qu'elle se soit déplacée ou non**. Une seule par activation.

> 🎲 Le tir depuis un véhicule en mouvement (char, howdah). Distincte de [Double Tir] (qui exige l'immobilité). [Howdah] en est la déclinaison Mûmakil. **Sans porteur depuis P4/D070** : l'Aurige de Khand, seul profil à l'avoir jamais portée, devient cavalerie standard (abandon du type Chars pour cette pièce). Conservée au glossaire — réutilisable si un futur char apparaît au roster d'un autre peuple.

### Signatures bespoke — Mûmakil

Règles **propres au Mûmakil**, non transférables (l'unité est chiffrée par équivalence d'impact, pas à la formule). Le Mûmakil porte aussi **[Inébranlable ∞]** (socle, ex-[Inamovible]).

#### [Charge écrasante]  *(bespoke)*

À son activation, le Mûmakil **DOIT** effectuer un déplacement complet de **2 hexagones** (1 + 1) vers l'hexagone de tête visé, **sans tenir compte** des figurines présentes. Chaque unité dont un hexagone est traversé subit une **attaque de 4 dés** où la **Couronne inflige aussi une touche** ; cela se passe **en phase de mouvement — pas de combat, aucune contre-attaque**. Toute **cavalerie** repoussée recule du **double**. S'il reste des unités gênantes non détruites/repoussées, il s'arrête au dernier hexagone libre. **Aucune attaque de mêlée en phase d'attaque.**

> 🎲 Choc de masse réservé à la grande créature, en phase de mouvement (l'usage annoncé lors du retrait de l'ancienne [Charge écrasante] générique, D043→D054). Le gabarit 1-2-1 ne pivote pas (translation pure).

#### [Bête incontrôlable]  *(bespoke)*

À son activation, **s'il est blessé** : lancez autant de dés que ses **PV restants** ; **sans aucune Couronne**, posez un marqueur **Furie** — l'adversaire dirige immédiatement son déplacement et peut l'activer comme une de ses figurines tant que la Furie tient. À la **fin de chaque tour**, le camp du Mal relance **(PV restants + 1)** dés : une **Couronne** retire la Furie.

> 🎲 Auto-équilibrage par les PV (plus blessé = plus affolé, moins récupérable). Le Mûmakil **doit** être activé chaque tour ; le contrôle se vérifie **avant** l'activation ; le test de reprise est **toujours** lancé par le camp du Mal. *(Refonte de la Furie prévue en P5.)*

#### [Howdah]  *(bespoke)*

**[Howdah] = [Plateforme de tir 2] + [Poison]** : une attaque de tir de **2 dés**, portée **1–3**, en plus de la mêlée, bénéficiant de [Poison] (tour d'archers Haradrim, flèches empoisonnées).

---

## Récapitulatif alphabétique

| Règle | Famille | Résumé |
|---|---|---|
| **[Archer en mêlée]** | Signature (Compagnie Grise) | Les faces Cible touchent aussi en mêlée |
| **[Arme de jet X]** | Socle | Le tour où l'unité s'est déplacée puis attaque en mêlée, chaque Cible compte aussi comme touche |
| **[Relance X]** | Socle | Relance X dés (mêlée ou tir) — absorbe l'ex-[Perforant X] |
| **[Armure X]** | Socle | Retire X faces Épée des attaques de mêlée reçues |
| **[Bête incontrôlable]** | Signature bespoke (Mûmakil) | Blessé : test de contrôle par PV ; échec → Furie dirigée par l'adversaire |
| **[Charge écrasante]** | Signature bespoke (Mûmakil) | Charge de 2 hex en mouvement : 4 dés (Couronne = touche) sur le trajet, sans contre-attaque |
| **[Double Tir]** | Signature (Easterling) | Seconde attaque à distance si non déplacé |
| **[Férocité]** | Socle | Contre-attaque même en cas de recul forcé, puis recule |
| **[Horde]** | Signature (Mordor) | +1 dé et [Inébranlable 1] à pleine santé ; perdus à la 1ʳᵉ perte |
| **[Howdah]** | Signature bespoke (Mûmakil) | = [Plateforme de tir 2] + [Poison] |
| **[Inébranlable X]** | Socle | Ignore X retraites (∞ = ne recule jamais, ex-[Inamovible]) |
| **[Mercenaire]** | Socle *(coût négatif)* | Chaque retrait forcé compte double — badge Faction Khand |
| **[Mobilité X]** | Intrinsèque (tir léger/monté) | Déplacement +X hex après avoir attaqué — grille [[Regles_Base]] §2.4 |
| **[Poursuite X]** *(intrinsèque)* | Intrinsèque (cavalerie de mêlée) | 2 en 🟢/🔵, 1 en 🔴 — grille [[Regles_Base]] §2.4 |
| **[Armure 1]** *(intrinsèque)* | Intrinsèque (lourd 🔴) | Plancher d'armure de tout lourd — grille [[Regles_Base]] §2.4 |
| **[Peur X]** | Signature (Troll) | Chaque Arcane = X Drapeaux (n'inflige pas de touche) |
| **[Plateforme de tir X]** | Signature (char de Khand) | Tir de X dés (portée 1–3) en plus de l'attaque, 1×/activation |
| **[Poison]** | Signature (Harad) | Couronne → 1 touche supplémentaire |
| **[Poursuite X]** | Socle | Alternative à l'avance : déplacement + attaque supplémentaire |
| **[Prise de flanc]** | Signature (Éored de cavalier) | +1 dé aux attaques amies contre une ennemie adjacente à cette unité |
| **[Protection X]** | Socle | Ignore X touches (terrain, fortifications) |
| **[Vigilant]** | Signature (Éored d'éclaireur) | La cible de cette unité ne peut pas la contre-attaquer |

---

## Retiré au tri P2

Traçabilité des règles sorties du glossaire actif le 2026-08-04 (D062).

| Règle | Sort | Renvoi / remplacement |
|---|---|---|
| **[Perforant X]** | Fusionnée | → **[Relance X]** (relance X, mêlée ou tir) |
| **[Inamovible]** | Fusionnée | → **[Inébranlable ∞]** |
| **[Mobilité X]** | Devenue intrinsèque | → 🟢 distance (§3) — plus un mot-clé de profil |
| **[Mur de bouclier]** | Coupée | → **[Armure 1]** sur les profils Easterling (répercussion P4) |
| **[Réception de charge]** | Coupée | — (bonus de contre-attaque accroché à l'action la plus oubliée à la table) |
| **[Arme de jet X]** | Coupée puis **restaurée** | → socle générique (P4, D068), voir §2 — coupure P2 caduque |
| **[Martyre]** | Coupée | Jamais assignée |
| **[Meute X]** | Coupée | Candidate créature en Phase 2 |
| **[Souffle de feu]** | Coupée | Ré-skinnable sur [Poison] si une unité de feu apparaît |
| **[Immunisé au feu]** | Coupée | Sans objet ([Souffle de feu] coupée) |
| **[Immunisé au poison]** | Coupée | Géré au cas par cas si nécessaire |
| **[Terrain favori : X]** | Coupée | → document [[Terrain]] |
| **[Rechargement]** | Coupée | Artillerie hors périmètre v1 ([[Regles_Base]]) |
| **[Déploiement avancé]** | Coupée | Retrait déjà acté (D047), ici formalisé |

> ⚠️ **Répercussions différées (conscientes, non omises).** Le retrait des règles coupées des **profils** (`02 - Factions/*`), le passage d'Easterling à [Armure 1], la mise à jour de **[[Regles_Points]]** (coûts des règles fusionnées/coupées) et l'ajustement des **scénarios** (`03 - Scénarios/*`) relèvent de **P3 (coûts)** et **P4 (re-expression des 6 rosters)**, conformément à D060 — pas de retouche piecemeal de fichiers voués à être réécrits. Les **comptes-rendus de playtest** (`05 - Playtest/*`) ne sont jamais modifiés (historique).

---

## Différées — Phase 2+

| Règle | Description préliminaire | Statut |
|---|---|---|
| **[Terreur]** | Version renforcée de [Peur X] (X élevé) — Nazgûl, Roi-Sorcier, Mûmakil | ⏳ Phase 2 |
| **[Vol]** | Traverser des hexagones occupés, ignorer certains terrains — créatures ailées (Nazgûl) | ⏳ Phase 2 |
| **[Piétinement en zone]** | Attaque touchant plusieurs hexagones adjacents — grandes créatures | ⏳ Phase 2 |
| **Manœuvres de héros (face Arcane)** | Couche Leadership : héros activant des manœuvres via les Arcanes (Espoir/Désespoir). Voir D034. | ⏳ Phase 2 |

---

> 🔗 **Voir aussi** [[Regles_Base]] — [[Terrain]] — [[Regles_Points]] — [[Document de cadrage]]

---

*Version 0.15 — Phase 1 — 2026-08-04. **Tri du glossaire (P2, D062).** Le document devient la référence des signatures. Créé un socle générique ([Armure X], [Protection X], [Inébranlable X] + convention ∞, [Poursuite X], [Férocité], [Relance X]) et une section « intrinsèques » (🟢 distance → [Mobilité 1], à écrire dans [[Regles_Base]] à la revue classe × type). Fusions : [Perforant X] → [Relance X] ; [Inamovible] → [Inébranlable ∞]. Coupées : [Réception de charge], [Mur de bouclier] (→ [Armure 1]), [Arme de jet X], [Martyre], [Meute X], [Souffle de feu], [Immunisé au feu], [Immunisé au poison], [Terrain favori : X], [Rechargement], [Déploiement avancé]. Signatures conservées, groupées par peuple / pièce unique / bespoke Mûmakil. Supprimé les tables « intrinsèques des types » et « priorité de résolution » (périmées par [[Regles_Base]] v0.6). Répercussions profils/coûts/scénarios renvoyées à P3–P4.*

*Version 0.16 — Phase 1 — 2026-08-05. **Mise à jour de renvois seulement (pas de re-tri).** La revue classe × type est faite (D063) : les mentions « revue à venir » pointent désormais vers [[Regles_Base]] §2.4 (source de vérité unique des intrinsèques) ; §3 recadré en illustration ([Mobilité 1] cas fondateur) ; récapitulatif alphabétique complété ([Mobilité X], [Poursuite] et [Armure 1] intrinsèques). Aucune décision de tri modifiée.*

*Version 0.19 — Phase 1 — 2026-08-08. **[Mercenaire] créée** (P4, D070) : premier badge/règle à coût négatif du projet (−2 brut), badge Faction de Khand. **[Plateforme de tir X] sans porteur actif** : l'Aurige de Khand, seule pièce à l'avoir portée, abandonne le type Chars pour devenir cavalerie standard — règle conservée au glossaire, réutilisable pour un futur char. Identité de Khand reformulée §Signatures (mercenaire + hache lourde, non plus « le char »).*

*Version 0.18 — Phase 1 — 2026-08-08. **[Arme de jet X] restaurée au socle générique** (P4, D068) — coupée à P2 faute de porteur en attente, réintégrée à l'occasion de la re-expression du Rohan (Milice lige, porteur d'origine D044). Ajoutée §2 et au récapitulatif alphabétique ; retirée de la liste des coupures §6.*

*Version 0.17 — Phase 1 — 2026-08-08. **Renommage global [Arme Lourde X] → [Relance X]** (P4, D066) : nom plus direct pour la table à 6 joueurs — la relance est l'unique effet de la règle, plus besoin de retenir un nom hérité. Répercuté dans ce document, [[Regles_Points]] et [[Regles_Base]] ; les profils de peuples migreront à leur propre passage P4 (Gondor fait, D067).*

*Historique antérieur (0.7 → 0.14) : reprise du glossaire générique BdVM ; assignations Gondor/Rohan/Khand/Mordor/Easterling/Harad ; règles [Archer en mêlée] (D024), [Déploiement avancé] (D028), [Horde] (D032), [Peur X] (D033), [Mur de bouclier] (D037), [Arme de jet X] (D044), [Plateforme de tir X]/[Howdah] (D045), [Prise de flanc]/[Vigilant] (D047–D050) ; refontes Mûmakil (D054), [Férocité] (D057), [Réception de charge] (D058). Détail dans le [[Document de cadrage]] §8.*
