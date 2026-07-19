---
projet: "Batailles de la Terre du Milieu"
type: "regles"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-07-19"
tags: [BdTdM, "type/regles", "phase/1", "statut/brouillon"]
version: "0.6"
---

# Batailles de la Terre du Milieu — Règles spéciales

> **Objet de ce document :** Glossaire de référence de toutes les règles spéciales disponibles pour la Phase 1. Chaque règle est définie une seule fois ici ; les profils d'unités y renverront une fois rédigés.
> Aligné sur **Regles_Base** et **Terrain**.
> Ce document ne couvre pas les règles universelles (Faible, contre-attaque, avance, Poursuite générique) ni les règles intrinsèques des types d'unités, qui sont définies dans [[Regles_Base]].
>
> **Statut des assignations :** Gondor et ses fiefs (14 unités, voir `02 - Factions/Gondor_et_Fiefs.md`), **Rohan** (9 unités, voir `02 - Factions/Rohan.md`) et **Khand** (5 unités, voir `02 - Factions/Khand.md`) sont rédigés et validés — prêts pour le Playtest #1. Mordor, Harad, Easterling restent à faire. [Massif] a été retirée du socle (D015 du [[Document de cadrage]]) : toute l'infanterie BdTdM partage la même base, le cas qu'elle traitait ne se présente plus.
>
> **Nouvelle règle issue de Gondor :** [Archer en mêlée] a été créée pour le profil de la Compagnie Grise (Legolas) et généralisée volontairement pour pouvoir resservir sur d'autres profils/peuples (D024 du [[Document de cadrage]]).
>
> **Nouvelle règle issue de Rohan :** [Déploiement avancé] a été créée pour l'Éored d'éclaireur (`02 - Factions/Rohan.md`) — un repositionnement unique avant le tour 1, plutôt qu'une capacité de combat classique (D028 du [[Document de cadrage]]).
>
> **Nouvelle règle en réserve pour Mordor :** [Horde] a été créée sur proposition d'Emmanuel (D032 du [[Document de cadrage]]) — bonus offensif et défensif à pleine santé (+1 dé d'attaque + [Inébranlable 1]), perdu définitivement à la première perte. Réservée aux Orcs ; non assignée à un profil existant, Mordor n'a pas encore de roster.
>
> **Note pour le Mûmakil (tâche à venir) :** [Howdah], [Bête incontrôlable] et [Meute X] sont des candidates naturelles pour cette unité — une tour d'archers sur son dos, un risque d'affolement une fois les guides tués, ou une résistance répartie sur plusieurs points de vie. Emmanuel a déjà une idée de règle dédiée pour l'impact au contact du Mûmakil, distincte de [Charge écrasante] (désormais assignée à la Garde du roi à cheval du Rohan et à l'Aurige de Khand, D029/D031) — à formaliser au moment de rédiger son profil.

---

## Table des matières

1. [[#Conventions]]
2. [[#Règles défensives]]
3. [[#Règles offensives — Mêlée]]
4. [[#Règles offensives — Distance]]
5. [[#Règles de mouvement et de manœuvre]]
6. [[#Règles hybrides — offensif + défensif]]
7. [[#Récapitulatif alphabétique]]
8. [[#Règles différées — Phase 2+]]

---

## Conventions

### Notation

- **[Règle]** : nom entre crochets — standard dans tous les profils.
- **[Règle X]** : règle avec une valeur numérique (ex. [Armure 1], [Arme Lourde 2]).

### Règles intrinsèques des types d'unités

Les règles suivantes ne sont **pas** des règles spéciales — elles sont portées directement par le type d'unité et s'appliquent à toutes les unités de ce type sans mention dans le profil :

| Type | Règle intrinsèque |
|---|---|
| **Infanterie** | Les faces Épées croisées et Cible infligent **2 PV** à la cible au lieu de 1 |
| **Cavalerie** | Aucune règle intrinsèque — 1 touche = 1 PV |
| **Chars** | Jamais Faible (véhicule unique, pas de groupe de figurines qui s'amenuise) |
| **Créature** | Jamais Faible (sauf exception explicite dans le profil) |
| **Machine de guerre** | Jamais Faible |
| **Artillerie** | Jamais Faible · Perd ses servants en premier (ordre de pertes défini dans le profil) |

> 🔄 **Tranché — 2026-07-19 (D030)** : le type **Chars** suit la même règle intrinsèque que Créature/Machine de guerre — **Jamais Faible**. Décision prise à l'ouverture du roster Khand (Aurige de Khand, `02 - Factions/Khand.md`) : cohérent avec le fait qu'il s'agit d'un seul véhicule et non d'un groupe de figurines, et évite un palier de dégradation supplémentaire à suivre en partie (principe 1 du [[Document de cadrage]], fluidité et mémorisation). Alternative envisagée et écartée : dégradation des dés d'attaque par palier de PV perdus — plus thématique mais contraire au principe de fluidité.

> 🔗 **Voir aussi** [[Regles_Base]] §2 — Types d'unités

### Priorité de résolution

Lors d'une attaque, les modificateurs s'appliquent dans l'ordre suivant :

1. Relances et bonus de dés (avant résolution) — [Arme Lourde X], [Perforant X], [Réception de charge], [Horde]
2. Décompte des touches
3. Règle intrinsèque Infanterie (Épées croisées et Cible → 2 PV)
4. Réductions défensives — [Armure X]
5. Effets de Couronne — [Poison], [Souffle de feu], [Charge écrasante]
6. Résistances spéciales — [Inébranlable X], [Horde]
7. Drapeaux et retraites (après résolution des touches)

---

## Règles défensives

---

### [Armure X]

Lorsque cette unité reçoit une attaque de **mêlée**, elle retire **X faces Épée** des résultats avant de compter les touches. Les faces **Épées croisées** ne sont jamais affectées par [Armure].

[Armure X] ne s'applique **pas** aux attaques à distance.

> 💡 **Exemple de jeu**
> Une unité d'Infanterie attaque une Cavalerie [Armure 1] adjacente : 3 dés. Résultat : Épées croisées, Épée, Drapeau. [Armure 1] retire 1 Épée → 1 touche restante (Épées croisées), soit 1 PV perdu (Cavalerie : pas de règle intrinsèque).

---

### [Inébranlable X]

Cette unité ignore **X résultats de retraite** par attaque reçue, quelle qu'en soit la source — dés, cartes tactiques ou sorts.

> 💡 **Exemple de jeu**
> Une unité [Inébranlable 2] reçoit une attaque dont le résultat produit 3 Drapeaux. Elle ignore 2 Drapeaux → ne recule que d'1 hexagone. Avec seulement 1 ou 2 Drapeaux obtenus, elle ne recule pas du tout.

---

### [Immunisé au poison]

Cette unité ignore les touches supplémentaires générées par la règle **[Poison]**, quelle qu'en soit la source. Les touches normales s'appliquent normalement.

> *Non assignée en V1 — disponible si un peuple ultérieur porte [Poison].*

---

### [Immunisé au feu]

Cette unité ignore les touches supplémentaires générées par la règle **[Souffle de feu]**.

> *Non assignée en V1.*

---

### [Protection X]

Lorsqu'une unité occupant une position protégée (bâtiment, fortification) reçoit une attaque, elle ignore **X touches** après décompte des dégâts.

| Type de position | Valeur |
|---|---|
| Ruine | 1 |
| Bâtiment solide | 2 |
| Fortification | 3 |

> 🔗 **Voir aussi** [[Terrain]] §9 — Bâtiment.

---

## Règles offensives — Mêlée

---

### [Archer en mêlée]

Cette unité inflige aussi une touche sur chaque face **Cible** obtenue lors d'une attaque de **mêlée** (normalement inerte en mêlée, voir [[Regles_Base]] §7.2).

> 💡 **Exemple de jeu**
> Une unité [Archer en mêlée] attaque en mêlée : 3 dés. Résultat : Cible, Épée, Drapeau. Sans cette règle, seule l'Épée toucherait. Avec [Archer en mêlée], la Cible touche aussi → 2 touches au lieu d'une.

> 🎲 **Note de design** Créée pour représenter une précision hors norme qui reste dangereuse même au corps à corps (Legolas, dans le profil de la Compagnie Grise — Gondor). Nommée de façon générique pour pouvoir être réattribuée à d'autres profils.

---

### [Arme Lourde X]

Après le lancer de dés, le joueur peut **relancer X dés** de son choix. Chaque dé ne peut être relancé qu'une seule fois.

> 💡 **Exemple de jeu**
> Une unité [Arme Lourde 1] attaque une Cavalerie adjacente : 3 dés. Résultat : Épée, Drapeau, Arcane. Le joueur relance l'Arcane → obtient Épées croisées. Résultat final : Épée + Épées croisées = 2 touches.

> 🔄 **Assignée — 2026-07-19** : Guerriers de Lossarnach (Gondor et fiefs), Compagnie Grise tant que Gimli est présent (Gondor et fiefs), Helmingas de Grimbolg (Rohan — haches à deux mains). **Khand** (`02 - Factions/Khand.md`) : fil conducteur du peuple, porté par Mercenaires de Khand (hache), Pillards de Khand (hache) et l'Aurige de Khand — en écho aux cleavers de Khand du matériel MESBG.

---

### [Charge écrasante]

Lorsque cette unité a **effectué un déplacement ce tour** avant d'attaquer, chaque face **Couronne** obtenue inflige **1 touche supplémentaire** à une unité adjacente à la cible (au choix du joueur actif).

> 💡 **Exemple de jeu**
> Une Créature se déplace d'1 hexagone et attaque une unité d'Infanterie adjacente : 3 dés. Résultat : Épées croisées, Couronne, Drapeau. [Charge écrasante] : la Couronne inflige 1 touche sur une autre unité adjacente à la cible.

> 🔄 **Assignée et confirmée — 2026-07-19 (D029)** : Garde du roi à cheval (Rohan) — la charge de la maison du roi qui déborde sur les rangs adverses. **Seconde assignation confirmée — 2026-07-19 (D031)** : Aurige de Khand (`02 - Factions/Khand.md`), pour l'impact d'un char lancé dans une ligne d'infanterie — cohérent avec le choix initial d'Emmanuel de réserver une règle d'impact distincte au Mûmakil (voir note en tête de document) : [Charge écrasante] reste une règle générique de choc au contact, réutilisable par toute unité rapide et lourde (cavalerie d'élite, chars), pas seulement le Rohan.

---

### [Férocité]

Lorsque cette unité effectue une **contre-attaque**, celle-ci est résolue **avant** que l'adversaire ne résout ses retraites. Si l'adversaire est éliminé par la contre-attaque, ses retraites ne sont pas résolues.

> 💡 **Exemple de jeu**
> Une unité attaque une unité [Férocité] : 4 Drapeaux. La cible contre-attaque immédiatement ([Férocité]) avant de résoudre sa retraite. Si elle élimine l'attaquant, les Drapeaux ne sont plus appliqués.

---

### [Martyre]

Lorsque cette unité attaque, le joueur peut **sacrifier 1 figurine** de l'unité pour convertir **1 face Couronne** en **1 touche supplémentaire**. La figurine sacrifiée est retirée immédiatement.

> 💡 **Exemple de jeu**
> Une unité [Martyre] attaque : 2 dés. Résultat : Couronne, Drapeau. Le joueur sacrifie 1 figurine → la Couronne devient 1 touche.

> *Non assignée en V1.*

---

### [Réception de charge]

Lorsque cette unité effectue une **contre-attaque** contre une unité qui s'est **déplacée ce tour**, elle lance **1 dé supplémentaire**.

> 💡 **Exemple de jeu**
> Une Cavalerie avance de 2 hexagones et charge une unité [Réception de charge] : 3 + 1 = **4 dés** en contre-attaque. Si la Cavalerie n'avait pas bougé ce tour, la cible n'aurait que 3 dés.

> 🔄 **Assignée — 2026-07-19** : Hommes d'armes de Dol Amroth (Gondor et fiefs), seule troupe de piquiers du peuple (D021 du [[Document de cadrage]] — assignée par équipement constaté sur la figurine, pas par peuple entier). Aucune unité du Rohan ni de Khand n'en est équipée ; reste ouverte pour un futur profil de piquiers.

---

## Règles offensives — Distance

---

### [Bête incontrôlable]

Lorsque **tous les servants/guides** de cette unité sont éliminés, elle **ne peut plus se déplacer** mais peut encore attaquer normalement. Une **touche supplémentaire** l'élimine définitivement.

> *Candidate pour le Mûmakil (risque d'affolement une fois les cornacs tués) — voir note en tête de document.*

---

### [Double Tir]

Si cette unité **ne s'est pas déplacée** ce tour, elle peut effectuer une **seconde attaque à distance** après la première, en ciblant la même unité ou une unité différente à portée et en ligne de vue.

> 💡 **Exemple de jeu**
> Une unité de tir immobile tire sur une cible à 3 hexagones : 2 dés, 1 touche. Grâce à [Double Tir], elle tire une seconde fois sur la même cible : 2 dés, 1 touche supplémentaire.

---

### [Howdah]

Cette unité peut effectuer une **attaque à distance en plus de son attaque de mêlée**. Cette attaque utilise **2 dés**, une portée de **1 à 3 hexagones**, et bénéficie de la règle **[Poison]**.

> *Candidate forte pour le Mûmakil (tour d'archers Haradrim sur son dos) — voir note en tête de document. La règle [Poison] associée est optionnelle et à retrancher si non pertinente pour cette unité.*

---

### [Perforant X]

Après le lancer de dés d'une attaque à distance, le joueur peut **relancer X dés** de son choix. Chaque dé ne peut être relancé qu'une seule fois.

> 🎲 **Note de design** [Perforant X] et [Arme Lourde X] partagent la même mécanique de relance. La distinction de nom reflète leur contexte d'usage : [Arme Lourde X] pour la mêlée, [Perforant X] pour le tir à distance.

---

### [Poison]

Lorsque cette unité effectue une attaque, chaque face **Couronne** obtenue inflige **1 touche supplémentaire**, sauf contre les unités **[Immunisées au poison]**.

> *Non assignée en V1.*

---

### [Souffle de feu]

Lorsque cette unité effectue une attaque, chaque face **Couronne** obtenue inflige **1 touche supplémentaire**, sauf contre les unités **[Immunisées au feu]**.

> *Non assignée en V1.*

---

## Règles de mouvement et de manœuvre

---

### [Déploiement avancé]

Une fois que toutes les unités (amies et ennemies) sont déployées, avant le premier Ordre du tour 1, le joueur propriétaire de cette unité peut la **repositionner** : elle effectue un déplacement égal à sa valeur de Mouvement. Elle ne peut pas terminer ce déplacement au contact d'une unité ennemie.

> 💡 **Exemple de jeu**
> Une unité [Déploiement avancé] (Mouvement 4) est déployée en retrait derrière la ligne de bataille. Une fois le déploiement terminé des deux côtés, son joueur la repositionne de 4 hexagones vers un flanc dégagé, sans finir au contact d'une unité ennemie — avant même que le premier Ordre du tour 1 ne soit joué.

> 🎲 **Note de design** Créée pour l'Éored d'éclaireur (Rohan) — représente des éclaireurs qui repèrent le déploiement adverse et se replacent en conséquence avant que la bataille ne commence. Contrairement à [Mobilité X], ce redéploiement est unique (avant le tour 1), pas répété après chaque attaque.

> 🔄 **Nouvelle règle — 2026-07-19** : créée et assignée pour l'Éored d'éclaireur (Rohan). Voir D028 du [[Document de cadrage]] et [[Regles_Points]] pour son coût provisoire.

---

### [Meute X]

Cette unité est composée de **plusieurs figurines de X PV chacune**. Retirer une figurine dès qu'elle atteint 0 PV. L'unité est **Faible** quand il ne reste qu'une seule figurine. *(Exception à la règle "jamais Faible" des Créatures.)*

> *Candidate possible pour une unité à plusieurs figurines résistantes (Trolls du Mordor en groupe, par exemple) — à confirmer à la rédaction des profils.*

---

### [Mobilité X]

Après avoir effectué une attaque, cette unité peut se déplacer de **X hexagones supplémentaires**.

---

### [Poursuite X]

Alternative à l'avance (voir [[Regles_Base]] §8.2) : se déplacer d'au moins 1 et jusqu'à X hexagones, puis effectuer une attaque supplémentaire contre une unité adjacente à la nouvelle position. Une seule fois par tour.

> 🔄 **Assignée — 2026-07-19** : Éored de cavalier, Gardes royaux à cheval et Garde du roi à cheval (Rohan, [Poursuite 2]). **Khand** (`02 - Factions/Khand.md`) : Aurige de Khand ([Poursuite 1]) — l'attelage enchaîne sur sa lancée après le premier choc ; le profil sacrifie 1 PV pour ce troisième atout signature.

---

### [Rechargement]

Cette unité **ne peut pas attaquer** lors d'un tour où elle s'est déplacée.

> *Candidate pour une pièce d'artillerie de siège (trébuchet de Gondor, catapulte de Mordor) — à confirmer à la rédaction des profils.*

---

### [Terrain favori : X]

Voir [[Terrain]] §11. Annule toutes les restrictions de mouvement et de combat du terrain X pour cette unité — la ligne de vue du terrain reste bloquante. Aucun peuple de la V1 ne porte cette règle pour l'instant.

---

## Règles hybrides — offensif + défensif

---

### [Horde]

Tant que cette unité **n'a perdu aucun PV**, elle bénéficie de **+1 dé d'attaque** et de **[Inébranlable 1]**. Ces deux bonus disparaissent **définitivement** dès que l'unité perd son premier PV — même si elle en regagnait par la suite (aucun mécanisme de regain de PV n'existe actuellement dans le système).

> 💡 **Exemple de jeu**
> Une unité de 3 dés [Horde], encore indemne, attaque à **4 dés** et ignore 1 Drapeau par attaque reçue. Dès qu'elle perd sa première figurine, elle retombe à son profil de base (3 dés, sans Inébranlable) pour le reste de la partie — même si l'ennemi ne la touche plus jamais après ça.

> 🎲 **Note de design** Inspirée de la règle *Warriors* de Commands & Colors: Ancients (bonus offensif à pleine force, perdu à la première perte). La condition (« n'a perdu aucun PV ») se lit directement sur le nombre de figurines encore présentes sur le socle — aucun jeton supplémentaire n'est nécessaire (principe 4 du [[Document de cadrage]]). Réservée aux Orcs (Mordor) plutôt qu'à Khand : le fil conducteur de Khand est déjà [Arme Lourde 1] (une relance permanente, D031), tout juste validé pour le Playtest #1 — superposer un second mécanisme offensif aurait dilué cette identité fraîchement close. Le pattern « très fort au premier contact, fragile ensuite » colle en revanche précisément à la horde d'Orcs du texte — nombreuse, féroce dans la charge, prompte à rompre une fois entamée.

> 🔄 **Nouvelle règle — 2026-07-19 (D032)** : créée sur proposition d'Emmanuel, réservée aux Orcs (Mordor). Non assignée à un profil existant — Mordor n'a pas encore de roster (voir D011 du [[Document de cadrage]]). Coût de 3 points forfaitaires — voir [[Regles_Points]].

---

## Récapitulatif alphabétique

| Règle | Catégorie | Résumé |
|---|---|---|
| **[Archer en mêlée]** | Offensif — Mêlée | Les faces Cible touchent aussi en mêlée |
| **[Arme Lourde X]** | Offensif — Mêlée | Relancer X dés après le lancer |
| **[Armure X]** | Défensif | Retire X faces Épée des attaques de mêlée reçues |
| **[Bête incontrôlable]** | Offensif — Distance | Sans guides : ne bouge plus, 1 touche pour éliminer |
| **[Charge écrasante]** | Offensif — Mêlée | Si déplacé ce tour : Couronne → touche sur unité adjacente |
| **[Déploiement avancé]** | Manœuvre | Repositionnement unique avant le tour 1, jusqu'à sa valeur de Mouvement, sans finir au contact ennemi |
| **[Double Tir]** | Offensif — Distance | Seconde attaque si non déplacé ce tour |
| **[Férocité]** | Offensif — Mêlée | Contre-attaque résolue avant les retraites adverses |
| **[Horde]** | Mixte — Offensif + Défensif | +1 dé d'attaque et [Inébranlable 1] tant qu'aucun PV n'a été perdu ; perdus définitivement à la 1ère perte |
| **[Howdah]** | Offensif — Distance | Attaque à distance en plus de la mêlée — 2 dés (1–3) + [Poison] |
| **[Immunisé au feu]** | Défensif | Ignore les touches de [Souffle de feu] |
| **[Immunisé au poison]** | Défensif | Ignore les touches de [Poison] |
| **[Inébranlable X]** | Défensif | Ignore X résultats de retraite par attaque reçue |
| **[Martyre]** | Offensif — Mêlée | Sacrifier 1 fig. pour convertir 1 Couronne en touche |
| **[Meute X]** | Manœuvre | X PV par figurine — Faible à 1 figurine restante |
| **[Mobilité X]** | Manœuvre | Déplacement supplémentaire de X hex après l'attaque |
| **[Perforant X]** | Offensif — Distance | Relancer X dés après le lancer (attaque à distance) |
| **[Poison]** | Offensif — Distance | Couronne → 1 touche sup. (sauf [Immunisé au poison]) |
| **[Poursuite X]** | Manœuvre | Alternative à l'avance : jusqu'à X hex + attaque sup. |
| **[Protection X]** | Défensif | Ignore X touches (terrain : bâtiments, fortifications) |
| **[Rechargement]** | Manœuvre | Ne peut pas attaquer si déplacé ce tour |
| **[Réception de charge]** | Offensif — Mêlée | +1 dé en contre-attaque si l'adversaire s'est déplacé ce tour |
| **[Souffle de feu]** | Offensif — Distance | Couronne → 1 touche sup. (sauf [Immunisé au feu]) |
| **[Terrain favori : X]** | Manœuvre | Ignore toutes les restrictions de mouvement et de combat du terrain X |

---

## Règles différées — Phase 2+

| Règle | Description préliminaire | Statut |
|---|---|---|
| **[Peur]** | Convertit les Couronnes en Drapeaux supplémentaires contre les unités affectées | ⏳ Phase 2 |
| **[Terreur]** | Version renforcée de [Peur] | ⏳ Phase 2 |
| **[Vol]** | L'unité peut traverser des hexagones occupés et ignorer certains terrains — candidate pour les créatures ailées (Nazgûl) | ⏳ Phase 2 |
| **[Piétinement en zone]** | Attaque touchant plusieurs hexagones adjacents — candidate pour les grandes créatures (Mûmakil, Trolls) | ⏳ Phase 2 |
| **Système Lore / Arcanes** | Face Arcane activée — magie légère Espoir/Peur (voir [[Document de cadrage]] §5.2) | ⏳ Hors scope V1 |

---

> 🔗 **Voir aussi**
> [[Regles_Base]] — [[Terrain]] — [[Document de cadrage]]

---

*Version : 0.6 — Phase 1 — 2026-07-19.*
*Première adaptation de Batailles de la Terre du Milieu (BdTdM) : reprise du glossaire mécanique générique, sans reprise du contenu spécifique à l'autre projet dont il est issu. [Massif] retirée (D015). [Arme à feu] supprimée (spécifique aux armes à poudre, sans objet en Terre du Milieu). Index par faction retiré (aucune assignation encore faite). Renommé depuis `BdVM_Regles_Speciales.md`.*
*0.2 — Rédaction des profils Gondor et fiefs (voir `02 - Factions/Gondor_et_Fiefs.md`) : nouvelle règle [Archer en mêlée] ajoutée (D024). [Réception de charge] assignée aux Hommes d'armes de Dol Amroth (D021).*
*0.3 — Rédaction en cours des profils Rohan (voir `02 - Factions/Rohan.md`) : nouvelle règle [Déploiement avancé] ajoutée (D028), créée pour l'Éored d'éclaireur. [Charge écrasante] assignée pour la première fois (Garde du roi à cheval). [Arme Lourde 1] assignée aux Helmingas de Grimbolg.*
*0.4 — Roster Rohan validé et clos (D029) : [Charge écrasante] confirmée pour la Garde du roi à cheval — le Mûmakil aura sa propre règle dédiée, retirée de la liste des candidates pour cette règle.*
*0.5 — Ouverture du roster Khand (`02 - Factions/Khand.md`) : type **Chars** tranché — Jamais Faible (D030). [Charge écrasante] et [Arme Lourde X] proposées comme règles transversales du peuple Khand (chariot et armes de hache), en cours de revue profil par profil.*
*0.6 — Roster Khand validé et clos (D031) : [Arme Lourde 1] et [Charge écrasante] confirmées, [Poursuite 1] assignée à l'Aurige de Khand (3e règle signature, PV ramené à 3). Nouvelle règle hybride [Horde] ajoutée (D032), inspirée des Warriors de C&C Ancients — réservée aux Orcs (Mordor), non assignée à un profil, roster à venir. Nouvelle section « Règles hybrides — offensif + défensif » créée pour l'accueillir.*
