---
projet: "Batailles de la Terre du Milieu"
type: "regles"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-08-18"
tags: [BdTdM, "type/regles", "phase/1", "statut/brouillon"]
version: "0.29"
---

# Batailles de la Terre du Milieu — Règles spéciales

> **Objet de ce document (refonte P2, D062).** Depuis le pivot « taxonomie visuelle » (D059–D061), l'identité d'une unité — **classe** (couleur du jeton = dés), **type** (plateau/socle), **mode** (symbole du jeton, mêlée/distance — jeton unique depuis D089) — se lit d'un coup d'œil, et l'essentiel des règles en **découle** au lieu d'être mémorisé profil par profil. Ce glossaire n'est donc plus un catalogue : c'est la **référence des signatures**, la courte liste des capacités marquantes qu'un adversaire doit pouvoir identifier **d'un coup d'œil**. Il conserve en tête le **socle générique** (vocabulaire défensif/offensif universel), renvoie à [[Regles_Base]] pour tout ce qui est intrinsèque à la taxonomie, et liste en fin de document ce qui a été retiré.
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
4. [[#4a. Anciennes règles de Faction — retirées (D090)]]
5. [[#4b. Signature — pièces bespoke]]
6. [[#Récapitulatif alphabétique]]
7. [[#Retiré au tri P2]]
8. [[#Différées — Phase 2+]]

---

## Conventions

### Notation

- **[Règle]** : nom entre crochets — standard dans tous les profils.
- **[Règle X]** : règle avec une valeur numérique (ex. [Armure 1], [Relance 2]).

### Trois familles *(D089/D090 — retrait de la famille Faction)*

| Famille | Rôle | Où c'est défini |
|---|---|---|
| **Socle générique** | Vocabulaire universel disponible à tout profil (défense, relance, poursuite…) | §2 de ce document |
| **Intrinsèque** | Découle de la combinaison classe × type × mode — **ne se note pas sur le profil**, se lit au jeton/plateau | [[Regles_Base]] (§2, §6) |
| **Signature** | Capacité(s) marquante(s), réservée aux **pièces bespoke uniquement** (Compagnie Grise, Mûmakil), hors matrice de badges | §4b de ce document |

> **Faction retirée (D090).** L'ancienne famille « Faction — trait de peuple imprimé sur tout le roster » n'existe plus ; l'asymétrie de chaque peuple sera portée par des cartes de commandement dédiées (chantier P8). Ses anciennes règles ([Horde], [Poison], [Défense X], [Férocité], [Mercenaire]) restent au glossaire, sans porteur actif — voir §4a.
>
> **Badges secondaires : jusqu'à 2 maximum par unité standard** — un badge parmi Spéciale/Élite/Légende (1 max) **+** le badge Leader (1 max, D089). Défini dans [[Regles_Base]] §2.2 ; coûts dans [[Regles_Points]] §3.1.

### Où se résolvent les signatures

L'ordre de résolution d'un combat est celui de [[Regles_Base]] §7.1. Les signatures s'y insèrent ainsi :

1. **Avant le décompte** — relances : [Relance X], [Horde] *(sans porteur actif, D090)*.
2. **Au décompte des touches** — effets de **Couronne** (badge Leader uniquement, D089) et effets d'**Arcane** ([Charge écrasante]… — migrées depuis Couronne, D089).
3. **Réductions défensives** — [Armure X] puis [Protection X].
4. **Retraites** — les **Drapeaux**, plus les Drapeaux issus de la face **Arcane** via [Peur X] ; [Inébranlable X] (jusqu'à ∞) absorbe le tout, quelle qu'en soit la source.

> 🎲 **Note (D089).** Toutes les règles spéciales/signature à déclenchement par face se résolvent désormais sur **Arcane** (y compris [Peur X], déjà le cas depuis D033, et [Charge écrasante], migrée depuis Couronne). La **Couronne** est réservée au badge **Leader** — sur une unité qui ne le porte pas, elle est sans effet. Une unité pourrait en théorie cumuler Peur (Arcane, intrinsèque Créature) et une autre règle à Arcane sur le même jet : dans ce cas les deux effets s'appliquent, chacun sur sa propre attaque (aucun cas actif ne collisionne à ce jour — voir Mûmakil, `02 - Factions/Harad.md`, où Peur ne porte que sur l'attaque de charge et [Howdah] sur un jet de tir séparé).

> 🔗 **Voir aussi** [[Regles_Base]] §2 (types et faces de dé), §7 (combat), §9 (retraite). Les anciennes tables « règles intrinsèques des types » et « priorité de résolution » de ce document sont **supprimées** : périmées par [[Regles_Base]] v0.6 (jamais-Faible au socle, double-touche retirée, 1 touche = 1 figurine/PV).

---

## Socle générique

Vocabulaire universel. Ne compte **pas** dans le plafond de signatures d'une unité, mais reste soumis au bon sens de lisibilité.

### [Armure X]

Lorsque cette unité reçoit une attaque de **mêlée**, elle retire **X faces Épée** des résultats avant de compter les touches. Les faces **Épées croisées** ne sont jamais affectées. Sans effet contre le **tir**.

> 🔄 **Nom d'usage [Défense X] pour la Faction Gondor/Orientaux — D080/D081.** Quand [Armure X] sert de trait de Faction (imprimé pour tout un peuple, plutôt que dérivé de la classe), elle est désignée **[Défense X]** dans les rosters Gondor et Orientaux — mécanique strictement identique, nom distinct pour ne jamais la confondre avec le plancher [Armure 1] intrinsèque au 🔴 ([[Regles_Base]] §2.4). *(Historique : [Mur de bouclier], identité propre des Orientaux depuis D077, redevient sans porteur actif à P7c — les Orientaux reviennent au miroir mécanique de Gondor, [Défense 1] partout.)*

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

> 🔄 **Fusion — P2 (D062)** : absorbe l'ancienne [Perforant X] (même mécanique de relance, jadis réservée au tir). Le **jeton de mode** indique quels dés sont relancés — un seul mot-clé à retenir. Nom historique conservé (le plus assigné). Porteurs : armes de hache lourde (Khand), gourdin du Troll, et l'archerie d'élite qui le portait sous [Perforant] (Racine Noire, Gondor).

### [Arme de jet X]

Le tour où cette unité **s'est déplacée puis attaque en mêlée**, chaque face **Cible** obtenue compte comme **une touche supplémentaire** (au lieu d'un échec) — les projectiles lancés avant le choc.

> 🔄 **Restaurée — P4 (D068)**, après avoir été coupée au tri P2 (D062) faute de porteur en attente de re-expression, puis réintégrée à l'occasion de la re-expression du Rohan (porteur d'origine : Milice lige, D044). **Sans porteur actif depuis D074** : le Rohan migre son badge Faction vers [Férocité] (pivot « badges universels »). Conservée au socle générique, réutilisable si un futur profil de mêlée veut l'identité « projectile lancé avant le choc ».

### [Mercenaire]  *(coût négatif)*

Chaque **retrait forcé** (recul de combat) de cette unité compte **double** (déplacement de recul et éventuels dégâts de collision doublés, selon la règle qui déclenche le retrait).

> 🔄 **Créée — P4 (D070)**, premier badge/règle à **coût négatif** du projet : **−2 brut**, symétrique au coût des badges positifs existants. Traduit un moral fragile et une motivation strictement pécuniaire — l'unité cède plus volontiers le terrain qu'une troupe régulière ou fidèle. Porteuse d'origine : Khand (badge Faction, D070) — généralisable à toute future troupe mercenaire d'un autre peuple.

---

## Règles intrinsèques (dérivées de la taxonomie)

Ces effets **ne se notent pas sur le profil** : ils découlent de la classe (couleur du jeton), du type (plateau/socle) et du mode (symbole du jeton), et se lisent d'un coup d'œil. Leur **définition de référence** — la grille complète classe × type × mode — vit dans **[[Regles_Base]] §2.4** (revue D063). Ce document n'en rappelle que le cas fondateur, à titre d'illustration :

### 🟢 Léger + mode distance → [Mobilité 1]

Toute unité **légère (🟢, 2 dés) en mode distance** décroche après avoir tiré : **après son attaque**, elle peut se déplacer de **1 hexagone supplémentaire**. Sans attaque ce tour, pas de bonus (elle bouge de son Mouvement normal).

> 🎲 Identité **harceleur** (tir-puis-décroche), lisible d'un coup d'œil (jeton vert + symbole distance) — plus besoin d'écrire [Mobilité 1] sur ces profils. Formule pour l'aide de jeu : *« Tu frappes, puis tu décroches. Pas d'attaque, pas de bonus. »*

> 🔄 **P2 (D062) → revue classe × type (D063)** : absorbe les anciennes assignations éparses de [Mobilité 1] (Rangers du Gondor et famille, Pillards de Khand, pisteurs orques). La grille complète est désormais écrite dans **[[Regles_Base]] §2.4** — [Mobilité] est étendue à la cavalerie légère (**2**) et standard (**1**), et [Armure 1] / [Poursuite] ajoutées aux cases lourdes et de cavalerie de mêlée. Contraste voulu avec [Double Tir] (§4), signature de l'archer **immobile** qui, lui, troque la mobilité contre le volume.

---

## 4a. Anciennes règles de Faction — retirées (D090)

*(Retrait D089/D090, pivot jeton/badges.)* Ces règles étaient jusqu'ici imprimées une fois par peuple et appliquées automatiquement à toutes ses unités standard. **Ce mécanisme n'existe plus** : l'asymétrie de chaque peuple sera portée par des cartes de commandement dédiées (chantier P8). Les règles elles-mêmes restent définies ci-dessous, **sans porteur actif**, conservées au glossaire pour une éventuelle réassignation en P8 (carte de commandement ou signature bespoke).

#### [Horde]  — *sans porteur actif (ex-Faction Mordor)*

Tant que cette unité **n'a subi aucune touche**, elle bénéficie de **+1 dé d'attaque**. Dès qu'elle subit sa **première touche**, elle perd ce bonus **et** passe immédiatement en **état Faible** ([[Regles_Base]] §2.2 : ses faces Épée cessent de toucher) — **quel que soit le nombre de figurines qu'il lui reste**, pas seulement à la dernière.

> 🎲 « Très fort au premier choc, s'effondre au premier sang » : la horde d'orques nombreuse, redoutable en masse et vite débandée dès qu'elle encaisse. Condition lisible au nombre de figurines, sans jeton. Inspirée des *Warriors* de C&C Ancients.
>
> 🔄 **Refondue — P4 (D075)** : ajoute l'entrée en état Faible **immédiate** (dès la première touche, plus seulement à la dernière figurine) à l'ancien effet (+1 dé à pleine santé, D032 ; perte de [Inébranlable 1], D071). Coût ramené de 2 à **1** (forfait) — le nouveau malus (Faible prématuré) est une contrepartie réelle, pas seulement la perte d'un bonus. Toujours provisoire, non testé sous cette forme.
>
> 🔄 **Restriction de portée levée (D075)** : jusqu'ici réservée à l'infanterie orque de mêlée (D032, jamais la cavalerie ni les bêtes), la règle est désormais aussi assignée à la Meute de cavaliers wargs de Mordor — la restriction D032 est supersédée pour ce cas précis, à l'appréciation de chaque peuple.
>
> 🔄 **Étendue à toute l'infanterie de mêlée du roster, Uruk-hai compris — P7c (D081).** Auparavant l'Uruk-hai en était explicitement exclu (« exception steadfast », D035) : il porte désormais [Horde] comme trait de Faction, badge Élite en plus (Jamais Faible neutralise le volet Faible-immédiate de la règle — l'Uruk-hai profite du +1 dé à pleine santé sans jamais en subir la contrepartie, cohérent avec son statut d'élite qui ne rompt pas). **Reste hors périmètre : la Bande de pisteurs orques** (tir) — sur une unité qui ne porte pas de faces Épée actives, le volet Faible de [Horde] ne mord pas, ce qui en ferait un bonus sans contrepartie ; exclue par choix, pas par oubli.

#### [Poison]  — *sans porteur actif (ex-Faction Harad)*

Lorsque cette unité attaque, chaque face **Arcane** inflige **1 touche supplémentaire** *(migré depuis Couronne, D089 — Couronne est réservée au badge Leader)*.

> 🎲 Ancien fil conducteur du Harad (flèches et lames empoisonnées). Porté par tout le roster d'escorte et la volée du Mûmakil ([Howdah]) jusqu'à D090 — retiré des deux, y compris du Mûmakil (`02 - Factions/Harad.md`).

#### [Défense X]  — *sans porteur actif (ex-Faction Gondor et Orientaux)*

Nom d'usage d'[Armure X] (§2, socle générique) quand la règle sert de trait de Faction plutôt que d'être dérivée de la classe : lorsque cette unité reçoit une attaque de **mêlée**, elle retire **X faces Épée** des résultats avant de compter les touches. Sans effet contre le tir.

> 🎲 Miroir mécanique exact entre les deux peuples : troupes régulières et bien équipées, quel que soit le camp. Nom distinct d'[Armure X] pour ne jamais le confondre avec le plancher [Armure 1] intrinsèque au 🔴 ([[Regles_Base]] §2.4) — sur un profil 🔴, [Défense 1] est donc **gratuit** (déjà inclus), seul l'excédent ([Défense 2]) se facture.
>
> 🔄 **Étendue à tout le roster — P7c (D081).** Jusqu'ici cantonnée aux profils lourds chez Gondor et absente chez les Orientaux (badge [Mur de bouclier], D077), la Faction couvre désormais **toutes** les unités standard des deux peuples, sans exception. **[Mur de bouclier] redevient sans porteur actif** (voir ci-dessous) : les Orientaux reviennent au miroir mécanique de Gondor.

#### [Férocité]  — *sans porteur actif (ex-Faction Rohan)*

Cette unité peut effectuer sa contre-attaque même si l'attaque subie la force à reculer (voir §2, socle générique) — l'exception à la condition « restée sur son hexagone ».

> 🎲 Porté par les 9 profils du roster sans exception depuis D074 (premier peuple à universaliser sa Faction). Traduit la vaillance désespérée du Rohan mieux qu'une arme ou une armure — « personne au Rohan ne cède un pouce de terrain sans rendre un coup ».

#### [Mercenaire]  — *sans porteur actif (ex-Faction Khand)*  *(coût négatif)*

Chaque retrait forcé (recul de combat) de cette unité compte double (voir §2, socle générique).

> 🎲 Porté par toutes les troupes mercenaires et pillards de Khand. **L'Aurige de Khand ne le porte pas** : seul corps régulier du peuple, pas un mercenaire — exclusion par identité, pas un oubli (D070).

*(Historique : la Bande de pisteurs orques (Mordor, tir) et l'Aurige de Khand (seul corps régulier) étaient les seules unités **sans** Faction avant son retrait généralisé (D090) — la distinction n'a plus d'effet mécanique aujourd'hui.)*

#### [Mur de bouclier]  — *sans porteur actif*

Tant que cette unité n'a subi aucune touche, elle bénéficie de [Protection 1] (ignore 1 touche par attaque reçue, mêlée ou tir). Dès qu'elle subit sa première touche, la formation est rompue : la protection disparaît définitivement.

> 🎲 Le mur tient tant que la ligne n'est pas percée, puis s'effondre d'un coup — même patron que [Horde]. **Sans porteur depuis P7c (D081)** : identité propre des Orientaux depuis D077, elle cède la place au miroir mécanique de Gondor ([Défense 1], universel sur les deux rosters). Conservée au glossaire — réutilisable si un futur profil ou peuple veut l'identité « formation qui tient tant qu'elle n'est pas percée ».

#### [Double Tir]  — *sans porteur actif*

Si cette unité **ne s'est pas déplacée** ce tour, elle effectue une **seconde attaque à distance** (même cible ou une autre, à portée et en ligne de vue).

> 🎲 La discipline de la ligne qui tient sa position et double la salve — miroir de l'archer **mobile** (intrinsèque [Mobilité 1], §3). Sans porteur depuis P4/D072 (les Orientaux redeviennent un profil standard, sans règle bespoke). Conservée au glossaire — réutilisable si un futur profil veut l'identité « archer immobile qui double la salve ».

## 4b. Signature — pièces bespoke

Règles propres, **hors matrice de badges**, réservées aux pièces qui ne se ramènent pas à une combinaison classe × type × mode + badges standard. Deux porteuses actives à ce stade : **La Compagnie Grise** (Gondor) et **le Mûmakil** (Harad). *(Troll du Mordor et Aurige de Khand : candidats évoqués au Playtest #3, confirmés en matrice standard — D081/P7c, pas de statut bespoke.)*

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

Règles **propres au Mûmakil**, non transférables (l'unité est chiffrée par équivalence d'impact, pas à la formule). Le Mûmakil porte aussi **[Inébranlable ∞]** (socle, ex-[Inamovible]) et, depuis P5 (D079), **[Protection 1] contre le tir uniquement** (formalise le houserule appliqué au Playtest #2, où la bête avait été traitée comme cible molle).

#### [Charge écrasante]  *(bespoke)*

À son activation, le Mûmakil **DOIT** effectuer un déplacement complet de **2 hexagones** (1 + 1) vers l'hexagone de tête visé, **sans tenir compte** des figurines présentes. Chaque unité dont un hexagone est traversé subit une **attaque de 4 dés** où l'**Arcane inflige aussi une touche** *(migré depuis Couronne, D089 — Couronne est réservée au badge Leader)* ; cela se passe **en phase de mouvement — pas de combat, aucune contre-attaque**. Toute **cavalerie** repoussée recule du **double**. S'il reste des unités gênantes non détruites/repoussées, il s'arrête au dernier hexagone libre. **Aucune attaque de mêlée en phase d'attaque.**

> 🎲 Choc de masse réservé à la grande créature, en phase de mouvement (l'usage annoncé lors du retrait de l'ancienne [Charge écrasante] générique, D043→D054). Le gabarit 1-2-1 ne pivote pas (translation pure).

#### [Bête incontrôlable]  *(bespoke, refondue P5/D079)*

Le Mûmakil entre en **Furie** dès qu'il tombe à **son dernier point de vie (1 PV)** — pas de test de déclenchement, l'état est automatique. Tant qu'il est à 1 PV : **chaque tour, un tirage à pile ou face détermine qui contrôle la bête** ce tour-là (Mal ou Bien). Quel que soit le résultat, **le Mûmakil s'active obligatoirement au tour du Mal, sans consommer de carte de commandement** (activation gratuite) ; si le tirage désigne le Bien, c'est lui qui dirige le mouvement et l'attaque ce tour-là, comme une de ses propres figurines. Pas de test de reprise : la Furie dure jusqu'à la mort de la bête.

> 🎲 **Refonte D079.** L'ancienne version (test de déclenchement ET de reprise indexés aux PV restants) créait une spirale jugée trop punitive à la lecture (jamais déclenchée au Playtest #2) : plus la bête était blessée, moins elle avait de dés pour se reprendre. La refonte remplace la probabilité graduelle par un état binaire au seuil critique — plus simple, plus mémorisable, et cohérent avec l'image d'une bête à l'agonie qui ne se calme plus.

#### [Howdah]  *(bespoke)*

**[Howdah] = [Plateforme de tir 2]** : une attaque de tir de **2 dés**, portée **1–3**, en plus de la mêlée. *([Poison] retiré, D090 — c'était le trait de Faction du Harad, désormais sans porteur ; aucune collision avec [Peur 1] du Mûmakil, puisque Peur ne s'applique qu'à son attaque de charge, un jet distinct du tir de Howdah.)*

---

## Récapitulatif alphabétique

| Règle | Famille | Résumé |
|---|---|---|
| **[Archer en mêlée]** | Sans porteur actif | Les faces Cible touchent aussi en mêlée |
| **[Arme de jet X]** | Socle *(sans porteur actif)* | Le tour où l'unité s'est déplacée puis attaque en mêlée, chaque Cible compte aussi comme touche |
| **[Relance X]** | Socle | Relance X dés (mêlée ou tir) — absorbe l'ex-[Perforant X] |
| **[Armure X]** | Socle | Retire X faces Épée des attaques de mêlée reçues |
| **[Bête incontrôlable]** | Signature bespoke (Mûmakil) | À 1 PV (dernier point) : Furie automatique, contrôle à pile ou face chaque tour, activation gratuite garantie au tour du Mal (refondue D079) |
| **[Charge écrasante]** | Signature bespoke (Mûmakil) | Charge de 2 hex en mouvement : 4 dés (Arcane = touche, migré depuis Couronne D089) sur le trajet, sans contre-attaque |
| **[Double Tir]** | Sans porteur actif | Seconde attaque à distance si non déplacé |
| **[Défense X]** | Sans porteur actif *(ex-Faction Gondor/Orientaux, retiré D090)* | = [Armure X], nom d'usage quand la règle était trait de peuple |
| **[Férocité]** | Sans porteur actif *(ex-Faction Rohan, retiré D090 — aussi disponible au socle)* | Contre-attaque même en cas de recul forcé, puis recule |
| **[Horde]** | Sans porteur actif *(ex-Faction Mordor, retiré D090)* | +1 dé à pleine santé, Faible dès la 1ʳᵉ touche — refondue P4/D075 |
| **[Howdah]** | Signature bespoke (Mûmakil) | = [Plateforme de tir 2] *([Poison] retiré, D090)* |
| **[Inébranlable X]** | Socle | Ignore X retraites (∞ = ne recule jamais, ex-[Inamovible]) |
| **[Leader]** | Badge *(D089, slot réservé — Phase 2)* | Touche aussi sur Couronne, en plus des faces normales du mode |
| **[Mercenaire]** | Sans porteur actif *(ex-Faction Khand, retiré D090)* *(coût négatif)* | Chaque retrait forcé compte double |
| **[Mobilité X]** | Intrinsèque (tir léger/monté) | Déplacement +X hex après avoir attaqué — grille [[Regles_Base]] §2.4 |
| **[Mur de bouclier]** | Sans porteur actif *(depuis P7c/D081)* | [Protection 1] tant qu'aucune touche subie, perdue définitivement à la 1ʳᵉ |
| **[Poursuite X]** *(intrinsèque)* | Intrinsèque (cavalerie de mêlée) | 2 en 🟢/🔵, 1 en 🔴 — grille [[Regles_Base]] §2.4 |
| **[Armure 1]** *(intrinsèque)* | Intrinsèque (lourd 🔴 + type Créature) | Plancher d'armure de tout lourd — grille [[Regles_Base]] §2.4 ; toute créature en porte aussi (D071) |
| **[Peur X]** | Intrinsèque (type Créature) | Chaque Arcane = X Drapeaux (n'inflige pas de touche) — devenue intrinsèque P4/D071, plus une signature à assigner |
| **[Plateforme de tir X]** | Sans porteur actif | Tir de X dés (portée 1–3) en plus de l'attaque, 1×/activation |
| **[Poison]** | Sans porteur actif *(ex-Faction Harad, retiré D090)* | Arcane → 1 touche supplémentaire (migré depuis Couronne, D089) |
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

> 🔗 **Voir aussi** [[Regles_Base]] — [[Terrain]] — [[Regles_Points]] — [[Document_de_cadrage]]

---

*Version 0.29 — Phase 1 — 2026-08-18. **Pivot jeton/badges (D089) et retrait de la famille Faction (D090).** §4a renommé « Anciennes règles de Faction — retirées » : [Horde], [Poison], [Défense X], [Férocité], [Mercenaire] passent sans porteur actif, conservées pour réassignation en P8 (cartes de commandement par faction). Table « Quatre familles » → « Trois familles ». Migration Couronne→Arcane pour toutes les règles spéciales/signature à déclenchement par face ([Charge écrasante], [Poison]) — la Couronne est réservée au nouveau badge **Leader** (D089, slot réservé Phase 2). [Howdah] (Mûmakil) perd son volet Poison. Récapitulatif alphabétique et ordre de résolution des signatures mis à jour.*

*Version 0.27 — Phase 1 — 2026-08-13. **Collapse du système de badges (D080/D081, tâche P7c).** Nouvelle famille **Faction** (§4a) séparée de **Signature** (§4b) : la Faction devient un trait de peuple imprimé une fois, plus un badge ; la Signature se réserve désormais aux seules pièces bespoke (Compagnie Grise, Mûmakil). [Horde] étendue à l'Uruk-hai (Mordor), exclut toujours la Bande de pisteurs orques. Nouvelle entrée **[Défense X]**, nom d'usage d'[Armure X] en Faction Gondor/Orientaux, universel sur les deux rosters. **[Mur de bouclier] redevient sans porteur actif** (les Orientaux reviennent au miroir mécanique de Gondor). Table des matières, conventions et récapitulatif alphabétique alignés.*

*Version 0.26 — Phase 1 — 2026-08-09. **Refonte P5 du Mûmakil (D079).** [Bête incontrôlable] réécrite : la Furie devient un état déterministe déclenché à 1 PV (dernier point de vie), fini le test de probabilité indexé aux PV restants jugé trop punitif (spirale, jamais déclenchée en PT2). Contrôle tiré à pile ou face chaque tour ; activation garantie et gratuite au tour du Mal (sans carte de commandement). Le Mûmakil porte désormais aussi [Protection 1] contre le tir uniquement (formalise le houserule PT2).*

*Version 0.15 — Phase 1 — 2026-08-04. **Tri du glossaire (P2, D062).** Le document devient la référence des signatures. Créé un socle générique ([Armure X], [Protection X], [Inébranlable X] + convention ∞, [Poursuite X], [Férocité], [Relance X]) et une section « intrinsèques » (🟢 distance → [Mobilité 1], à écrire dans [[Regles_Base]] à la revue classe × type). Fusions : [Perforant X] → [Relance X] ; [Inamovible] → [Inébranlable ∞]. Coupées : [Réception de charge], [Mur de bouclier] (→ [Armure 1]), [Arme de jet X], [Martyre], [Meute X], [Souffle de feu], [Immunisé au feu], [Immunisé au poison], [Terrain favori : X], [Rechargement], [Déploiement avancé]. Signatures conservées, groupées par peuple / pièce unique / bespoke Mûmakil. Supprimé les tables « intrinsèques des types » et « priorité de résolution » (périmées par [[Regles_Base]] v0.6). Répercussions profils/coûts/scénarios renvoyées à P3–P4.*

*Version 0.16 — Phase 1 — 2026-08-05. **Mise à jour de renvois seulement (pas de re-tri).** La revue classe × type est faite (D063) : les mentions « revue à venir » pointent désormais vers [[Regles_Base]] §2.4 (source de vérité unique des intrinsèques) ; §3 recadré en illustration ([Mobilité 1] cas fondateur) ; récapitulatif alphabétique complété ([Mobilité X], [Poursuite] et [Armure 1] intrinsèques). Aucune décision de tri modifiée.*

*Version 0.25 — Phase 1 — 2026-08-08. **[Mur de bouclier] restaurée et refondue (D077).** Nouvelle mécanique conditionnelle : [Protection 1] tant qu'aucune touche subie, perdue définitivement à la première — même patron que [Horde]. Redevient le badge Faction des Orientaux, à la place d'[Armure 1] (D072 caduque).*

*Version 0.24 — Phase 1 — 2026-08-08. **[Horde] refondue (D075).** Ajoute l'entrée en état Faible immédiate dès la première touche (plus seulement à la dernière figurine), coût 2→1. Restriction D032 (jamais la cavalerie) levée pour la Meute de cavaliers wargs (Mordor). Migration Mordor du badge Spéciale vers [Relance 1] — dernière répercussion de D073.*

*Version 0.23 — Phase 1 — 2026-08-08. **Migration Rohan (D074).** [Arme de jet X] devient sans porteur actif — le Rohan migre son badge Faction vers [Férocité] (pivot badges universels, D073). Conservée au socle générique.*

*Version 0.22 — Phase 1 — 2026-08-08. **Pivot transverse « badges universels » (D073).** [Archer en mêlée] devient sans porteur actif — la Compagnie Grise (Gondor) passe au badge Légende plutôt qu'à une règle bespoke par figurine. Badges Élite (+Jamais Faible) et Légende (nouveau) définis dans [[Regles_Base]] §2.2 ; badge Spéciale universel ([Relance 1] pour tous) défini dans [[Regles_Points]] §3.2.*

*Version 0.21 — Phase 1 — 2026-08-08. **P4 — Orientaux (ex-Easterling) re-exprimés** (`02 - Factions/Orientaux.md` v2.0) : miroir mécanique pur de Gondor, Faction=[Armure 1] / Spéciale=[Relance 1]. **[Double Tir] devient sans porteur actif** — ancienne signature de peuple, conservée au glossaire, réutilisable.*

*Version 0.20 — Phase 1 — 2026-08-08. **[Horde] nerfée** (P4, D071) : perd le volet [Inébranlable 1] à pleine santé, coût ramené de 3 à 2. **[Peur X] et [Armure 1] deviennent intrinsèques au type Créature** (toute créature en porte sans supplément, plus une signature à assigner unité par unité) — première application Troll du Mordor, s'étendra au Mûmakil à sa re-expression.*

*Version 0.19 — Phase 1 — 2026-08-08. **[Mercenaire] créée** (P4, D070) : premier badge/règle à coût négatif du projet (−2 brut), badge Faction de Khand. **[Plateforme de tir X] sans porteur actif** : l'Aurige de Khand, seule pièce à l'avoir portée, abandonne le type Chars pour devenir cavalerie standard — règle conservée au glossaire, réutilisable pour un futur char. Identité de Khand reformulée §Signatures (mercenaire + hache lourde, non plus « le char »).*

*Version 0.28 — Phase 1 — 2026-08-16. **Corrections de relecture — revue de finalisation « Verrouillage v1.0 ».** Liens `[[Document de cadrage]]` corrigés en `[[Document_de_cadrage]]` (nom réel du fichier, 2 occurrences). Aucune décision mécanique — pas de numéro D.*

*Version 0.18 — Phase 1 — 2026-08-08. **[Arme de jet X] restaurée au socle générique** (P4, D068) — coupée à P2 faute de porteur en attente, réintégrée à l'occasion de la re-expression du Rohan (Milice lige, porteur d'origine D044). Ajoutée §2 et au récapitulatif alphabétique ; retirée de la liste des coupures §6.*

*Version 0.17 — Phase 1 — 2026-08-08. **Renommage global [Arme Lourde X] → [Relance X]** (P4, D066) : nom plus direct pour la table à 6 joueurs — la relance est l'unique effet de la règle, plus besoin de retenir un nom hérité. Répercuté dans ce document, [[Regles_Points]] et [[Regles_Base]] ; les profils de peuples migreront à leur propre passage P4 (Gondor fait, D067).*

*Historique antérieur (0.7 → 0.14) : reprise du glossaire générique BdVM ; assignations Gondor/Rohan/Khand/Mordor/Easterling/Harad ; règles [Archer en mêlée] (D024), [Déploiement avancé] (D028), [Horde] (D032), [Peur X] (D033), [Mur de bouclier] (D037), [Arme de jet X] (D044), [Plateforme de tir X]/[Howdah] (D045), [Prise de flanc]/[Vigilant] (D047–D050) ; refontes Mûmakil (D054), [Férocité] (D057), [Réception de charge] (D058). Détail dans le [[Document_de_cadrage]] §8.*
