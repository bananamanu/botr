---
projet: "Batailles de la Terre du Milieu"
type: "regles"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-08-08"
tags: [BdTdM, "type/regles", "phase/1", "statut/brouillon"]
version: "0.25"
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

> 🔄 **Restaurée au socle générique — D077** : brièvement remplacée par [Armure 1] sur les profils Orientaux (P2→D072), [Mur de bouclier] est réintroduite sous une forme conditionnelle et refondue — voir §Signatures de peuple ci-dessous. [Armure 1] reste disponible comme badge Faction pour tout autre peuple (Gondor).

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

> 🔄 **Restaurée — P4 (D068)**, après avoir été coupée au tri P2 (D062) faute de porteur en attente de re-expression, puis réintégrée à l'occasion de la re-expression du Rohan (porteur d'origine : Milice lige, D044). **Sans porteur actif depuis D074** : le Rohan migre son badge Faction vers [Férocité] (pivot « badges universels »). Conservée au socle générique, réutilisable si un futur profil de mêlée veut l'identité « projectile lancé avant le choc ».

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

Tant que cette unité **n'a subi aucune touche**, elle bénéficie de **+1 dé d'attaque**. Dès qu'elle subit sa **première touche**, elle perd ce bonus **et** passe immédiatement en **état Faible** ([[Regles_Base]] §2.2 : ses faces Épée cessent de toucher) — **quel que soit le nombre de figurines qu'il lui reste**, pas seulement à la dernière.

> 🎲 « Très fort au premier choc, s'effondre au premier sang » : la horde d'orques nombreuse, redoutable en masse et vite débandée dès qu'elle encaisse. Condition lisible au nombre de figurines, sans jeton. Inspirée des *Warriors* de C&C Ancients.
>
> 🔄 **Refondue — P4 (D075)** : ajoute l'entrée en état Faible **immédiate** (dès la première touche, plus seulement à la dernière figurine) à l'ancien effet (+1 dé à pleine santé, D032 ; perte de [Inébranlable 1], D071). Coût ramené de 2 à **1** (forfait) — le nouveau malus (Faible prématuré) est une contrepartie réelle, pas seulement la perte d'un bonus. Toujours provisoire, non testé sous cette forme.
>
> 🔄 **Restriction de portée levée (D075)** : jusqu'ici réservée à l'infanterie orque de mêlée (D032, jamais la cavalerie ni les bêtes), la règle est désormais aussi assignée à la Meute de cavaliers wargs de Mordor — la restriction D032 est supersédée pour ce cas précis, à l'appréciation de chaque peuple.

#### [Poison]  — *Harad*

Lorsque cette unité attaque, chaque face **Couronne** inflige **1 touche supplémentaire**.

> 🎲 Fil conducteur du Harad (flèches et lames empoisonnées). Porté par les Lanciers, les Gardes serpents et la volée du Mûmakil ([Howdah]).

#### [Mur de bouclier]  — *Orientaux*

Tant que cette unité **n'a subi aucune touche**, elle bénéficie de **[Protection 1]** (ignore 1 touche par attaque reçue, mêlée ou tir). Dès qu'elle subit sa **première touche**, la formation est rompue : la protection disparaît **définitivement**.

> 🎲 Le mur tient tant que la ligne n'est pas percée, puis s'effondre d'un coup — même patron que [Horde] (condition liée à l'état de l'unité, pas à son voisinage), appliqué à une protection plutôt qu'à un bonus offensif.
>
> 🔄 **Restaurée et refondue — P4 (D077)**, après avoir été coupée au tri P2 (D062) faute d'une version assez simple pour la table (l'ancienne mouture exigeait de vérifier l'adjacence à une autre unité d'Infanterie amie à chaque combat). Cette version ne dépend plus que du nombre de touches subies, lisible au même coup d'œil que [Horde]. **[Protection 1] à plat jugé trop fort** (retour d'Emmanuel) : la version conditionnelle s'auto-limite au premier choc, ce qui justifie de garder le même coût que la version à plat malgré la puissance ponctuelle.

#### [Double Tir]  — *sans porteur actif*

Si cette unité **ne s'est pas déplacée** ce tour, elle effectue une **seconde attaque à distance** (même cible ou une autre, à portée et en ligne de vue).

> 🎲 La discipline de la ligne qui tient sa position et double la salve — miroir de l'archer **mobile** (intrinsèque [Mobilité 1], §3). **Sans porteur depuis P4/D072** : à la re-expression des Orientaux (ex-Easterling), Emmanuel choisit un **miroir mécanique pur de Gondor** (badge Faction [Armure 1] + badge Spéciale [Relance 1]) plutôt que de reconduire cette signature — l'archer orientaux redevient un profil standard (classe 🟢, [Mobilité 1] intrinsèque gratuite), sans règle bespoke. Conservée au glossaire — réutilisable si un futur profil veut l'identité « archer immobile qui double la salve ».

*(Khand : identité portée par le badge Faction [Mercenaire] (moral fragile, coût réduit) et le badge Spéciale [Relance 1] (hache lourde) — voir §2. Gondor et Orientaux : identité portée par l'armure lourde ([Armure X], socle) et le badge Spéciale [Relance 1], en miroir mécanique exact l'un de l'autre.)*

### Signatures de pièce unique

#### [Peur X]  — *intrinsèque du type Créature*

Chaque face **Arcane** obtenue en attaque compte comme **X Drapeaux** contre la cible (au lieu d'un échec). N'inflige **aucune touche** : la Peur fait rompre, elle ne tue pas. Annulable par l'[Inébranlable X] de la cible.

> 🎲 Réutilise la face Arcane (morte par défaut) et pose le premier jalon de la couche Leadership (Phase 2). Versions « Terreur » (X élevé, Nazgûl/Roi-Sorcier) différées (§7).
>
> 🔄 **Devenue intrinsèque au type Créature — P4 (D071)** : **toute créature porte [Peur 1] et [Armure 1] sans supplément de coût** — ce n'est plus une signature à assigner unité par unité (voir [[Regles_Base]] §2.3, à ajouter). Première application : Troll du Mordor. S'appliquera au Mûmakil (Harad) à sa propre re-expression P4/P5, sans redondance avec ses règles bespoke déjà en place ([Howdah], [Charge écrasante], [Inébranlable ∞]).

#### [Archer en mêlée]  — *sans porteur actif*

Les faces **Cible** infligent aussi une touche lors d'une attaque de **mêlée** (normalement inertes en mêlée).

> 🎲 Précision hors norme, dangereuse jusqu'au corps à corps. **Sans porteur depuis P4/D073** : la Compagnie Grise (Legolas), seule pièce à l'avoir jamais portée, passe au badge **Légende** (+1 dé de combat) plutôt qu'à une règle bespoke par figurine. Conservée au glossaire — réutilisable si un futur profil veut l'identité « tireur d'élite qui touche aussi au contact ».

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
| **[Archer en mêlée]** | Sans porteur actif | Les faces Cible touchent aussi en mêlée |
| **[Arme de jet X]** | Socle *(sans porteur actif)* | Le tour où l'unité s'est déplacée puis attaque en mêlée, chaque Cible compte aussi comme touche |
| **[Relance X]** | Socle | Relance X dés (mêlée ou tir) — absorbe l'ex-[Perforant X] |
| **[Armure X]** | Socle | Retire X faces Épée des attaques de mêlée reçues |
| **[Bête incontrôlable]** | Signature bespoke (Mûmakil) | Blessé : test de contrôle par PV ; échec → Furie dirigée par l'adversaire |
| **[Charge écrasante]** | Signature bespoke (Mûmakil) | Charge de 2 hex en mouvement : 4 dés (Couronne = touche) sur le trajet, sans contre-attaque |
| **[Double Tir]** | Sans porteur actif | Seconde attaque à distance si non déplacé |
| **[Férocité]** | Socle | Contre-attaque même en cas de recul forcé, puis recule |
| **[Horde]** | Signature (Mordor) | +1 dé à pleine santé, Faible dès la 1ʳᵉ touche — refondue P4/D075 |
| **[Howdah]** | Signature bespoke (Mûmakil) | = [Plateforme de tir 2] + [Poison] |
| **[Inébranlable X]** | Socle | Ignore X retraites (∞ = ne recule jamais, ex-[Inamovible]) |
| **[Mercenaire]** | Socle *(coût négatif)* | Chaque retrait forcé compte double — badge Faction Khand |
| **[Mobilité X]** | Intrinsèque (tir léger/monté) | Déplacement +X hex après avoir attaqué — grille [[Regles_Base]] §2.4 |
| **[Mur de bouclier]** | Signature (Orientaux) | [Protection 1] tant qu'aucune touche subie, perdue définitivement à la 1ʳᵉ |
| **[Poursuite X]** *(intrinsèque)* | Intrinsèque (cavalerie de mêlée) | 2 en 🟢/🔵, 1 en 🔴 — grille [[Regles_Base]] §2.4 |
| **[Armure 1]** *(intrinsèque)* | Intrinsèque (lourd 🔴 + type Créature) | Plancher d'armure de tout lourd — grille [[Regles_Base]] §2.4 ; toute créature en porte aussi (D071) |
| **[Peur X]** | Intrinsèque (type Créature) | Chaque Arcane = X Drapeaux (n'inflige pas de touche) — devenue intrinsèque P4/D071, plus une signature à assigner |
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
| **[Mur de bouclier]** | **Restaurée (D077)** | → refondue en signature conditionnelle Orientaux, voir §Signatures de peuple |
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

*Version 0.25 — Phase 1 — 2026-08-08. **[Mur de bouclier] restaurée et refondue (D077).** Nouvelle mécanique conditionnelle : [Protection 1] tant qu'aucune touche subie, perdue définitivement à la première — même patron que [Horde]. Redevient le badge Faction des Orientaux, à la place d'[Armure 1] (D072 caduque).*

*Version 0.24 — Phase 1 — 2026-08-08. **[Horde] refondue (D075).** Ajoute l'entrée en état Faible immédiate dès la première touche (plus seulement à la dernière figurine), coût 2→1. Restriction D032 (jamais la cavalerie) levée pour la Meute de cavaliers wargs (Mordor). Migration Mordor du badge Spéciale vers [Relance 1] — dernière répercussion de D073.*

*Version 0.23 — Phase 1 — 2026-08-08. **Migration Rohan (D074).** [Arme de jet X] devient sans porteur actif — le Rohan migre son badge Faction vers [Férocité] (pivot badges universels, D073). Conservée au socle générique.*

*Version 0.22 — Phase 1 — 2026-08-08. **Pivot transverse « badges universels » (D073).** [Archer en mêlée] devient sans porteur actif — la Compagnie Grise (Gondor) passe au badge Légende plutôt qu'à une règle bespoke par figurine. Badges Élite (+Jamais Faible) et Légende (nouveau) définis dans [[Regles_Base]] §2.2 ; badge Spéciale universel ([Relance 1] pour tous) défini dans [[Regles_Points]] §3.2.*

*Version 0.21 — Phase 1 — 2026-08-08. **P4 — Orientaux (ex-Easterling) re-exprimés** (`02 - Factions/Orientaux.md` v2.0) : miroir mécanique pur de Gondor, Faction=[Armure 1] / Spéciale=[Relance 1]. **[Double Tir] devient sans porteur actif** — ancienne signature de peuple, conservée au glossaire, réutilisable.*

*Version 0.20 — Phase 1 — 2026-08-08. **[Horde] nerfée** (P4, D071) : perd le volet [Inébranlable 1] à pleine santé, coût ramené de 3 à 2. **[Peur X] et [Armure 1] deviennent intrinsèques au type Créature** (toute créature en porte sans supplément, plus une signature à assigner unité par unité) — première application Troll du Mordor, s'étendra au Mûmakil à sa re-expression.*

*Version 0.19 — Phase 1 — 2026-08-08. **[Mercenaire] créée** (P4, D070) : premier badge/règle à coût négatif du projet (−2 brut), badge Faction de Khand. **[Plateforme de tir X] sans porteur actif** : l'Aurige de Khand, seule pièce à l'avoir portée, abandonne le type Chars pour devenir cavalerie standard — règle conservée au glossaire, réutilisable pour un futur char. Identité de Khand reformulée §Signatures (mercenaire + hache lourde, non plus « le char »).*

*Version 0.18 — Phase 1 — 2026-08-08. **[Arme de jet X] restaurée au socle générique** (P4, D068) — coupée à P2 faute de porteur en attente, réintégrée à l'occasion de la re-expression du Rohan (Milice lige, porteur d'origine D044). Ajoutée §2 et au récapitulatif alphabétique ; retirée de la liste des coupures §6.*

*Version 0.17 — Phase 1 — 2026-08-08. **Renommage global [Arme Lourde X] → [Relance X]** (P4, D066) : nom plus direct pour la table à 6 joueurs — la relance est l'unique effet de la règle, plus besoin de retenir un nom hérité. Répercuté dans ce document, [[Regles_Points]] et [[Regles_Base]] ; les profils de peuples migreront à leur propre passage P4 (Gondor fait, D067).*

*Historique antérieur (0.7 → 0.14) : reprise du glossaire générique BdVM ; assignations Gondor/Rohan/Khand/Mordor/Easterling/Harad ; règles [Archer en mêlée] (D024), [Déploiement avancé] (D028), [Horde] (D032), [Peur X] (D033), [Mur de bouclier] (D037), [Arme de jet X] (D044), [Plateforme de tir X]/[Howdah] (D045), [Prise de flanc]/[Vigilant] (D047–D050) ; refontes Mûmakil (D054), [Férocité] (D057), [Réception de charge] (D058). Détail dans le [[Document de cadrage]] §8.*
