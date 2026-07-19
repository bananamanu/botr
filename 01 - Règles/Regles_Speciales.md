---
projet: Batailles de la Terre du Milieu
type: regles
phase: "1"
statut: brouillon-a-tester
date_maj: 2026-07-19
tags:
  - BdTdM
  - type/regles
  - phase/1
  - statut/brouillon
version: "0.4"
---

# Batailles de la Terre du Milieu — Règles spéciales

> **Objet de ce document :** Glossaire de référence de toutes les règles spéciales disponibles pour la Phase 1. Chaque règle est définie une seule fois ici ; les profils d'unités y renverront une fois rédigés. Aligné sur **Regles_Base** et **Terrain**. Ce document ne couvre pas les règles universelles (Faible, contre-attaque, avance, Poursuite générique) ni les règles intrinsèques des types d'unités, qui sont définies dans [[Regles_Base]].
> 
> **Statut des assignations :** Gondor et ses fiefs (14 unités, voir `02 - Factions/Gondor_et_Fiefs.md`) et **Rohan** (9 unités, voir `02 - Factions/Rohan.md`) sont rédigés et validés — prêts pour le Playtest #1. Mordor, Harad, Khand, Easterling restent à faire. [Massif] a été retirée du socle (D015 du [[Document de cadrage]]) : toute l'infanterie BdTdM partage la même base, le cas qu'elle traitait ne se présente plus.
> 
> **Nouvelle règle issue de Gondor :** [Archer en mêlée] a été créée pour le profil de la Compagnie Grise (Legolas) et généralisée volontairement pour pouvoir resservir sur d'autres profils/peuples (D024 du [[Document de cadrage]]).
> 
> **Nouvelle règle issue de Rohan :** [Déploiement avancé] a été créée pour l'Éored d'éclaireur (`02 - Factions/Rohan.md`) — un repositionnement unique avant le tour 1, plutôt qu'une capacité de combat classique (D028 du [[Document de cadrage]]).
> 
> **Note pour le Mûmakil (tâche à venir) :** [Howdah], [Bête incontrôlable] et [Meute X] sont des candidates naturelles pour cette unité — une tour d'archers sur son dos, un risque d'affolement une fois les guides tués, ou une résistance répartie sur plusieurs points de vie. Emmanuel a déjà une idée de règle dédiée pour l'impact au contact du Mûmakil, distincte de [Charge écrasante] (désormais assignée exclusivement à la Garde du roi à cheval du Rohan, D029) — à formaliser au moment de rédiger son profil.

---

## Table des matières

1. [[#Conventions]]
2. [[#Règles défensives]]
3. [[#Règles offensives — Mêlée]]
4. [[#Règles offensives — Distance]]
5. [[#Règles de mouvement et de manœuvre]]
6. [[#Récapitulatif alphabétique]]
7. [[#Règles différées — Phase 2+]]

---

## Conventions

### Notation

- **[Règle]** : nom entre crochets — standard dans tous les profils.
- **[Règle X]** : règle avec une valeur numérique (ex. [Armure 1], [Arme Lourde 2]).

### Règles intrinsèques des types d'unités

Les règles suivantes ne sont **pas** des règles spéciales — elles sont portées directement par le type d'unité et s'appliquent à toutes les unités de ce type sans mention dans le profil :

|Type|Règle intrinsèque|
|---|---|
|**Infanterie**|Les faces Épées croisées et Cible infligent **2 PV** à la cible au lieu de 1|
|**Cavalerie**|Aucune règle intrinsèque — 1 touche = 1 PV|
|**Créature**|Jamais Faible (sauf exception explicite dans le profil)|
|**Machine de guerre**|Jamais Faible|
|**Artillerie**|Jamais Faible · Perd ses servants en premier (ordre de pertes défini dans le profil)|

> ⚠️ **Point ouvert** — Le type **Chars**, introduit au [[Document de cadrage]] §4 (base identique aux Créatures/Machines de guerre, 65 mm), n'a pas encore de règle intrinsèque confirmée dans [[Regles_Base]]. À trancher avant de rédiger un profil de ce type.

> 🔗 **Voir aussi** [[Regles_Base]] §2 — Types d'unités

### Priorité de résolution

Lors d'une attaque, les modificateurs s'appliquent dans l'ordre suivant :

1. Relances et bonus de dés (avant résolution) — [Arme Lourde X], [Perforant X], [Réception de charge]
2. Décompte des touches
3. Règle intrinsèque Infanterie (Épées croisées et Cible → 2 PV)
4. Réductions défensives — [Armure X]
5. Effets de Couronne — [Poison], [Souffle de feu], [Charge écrasante]
6. Résistances spéciales — [Inébranlable X]
7. Drapeaux et retraites (après résolution des touches)

---

## Règles défensives

---

### [Armure X]

Lorsque cette unité reçoit une attaque de **mêlée**, elle retire **X faces Épée** des résultats avant de compter les touches. Les faces **Épées croisées** ne sont jamais affectées par [Armure].

[Armure X] ne s'applique **pas** aux attaques à distance.

> 💡 **Exemple de jeu** Une unité d'Infanterie attaque une Cavalerie [Armure 1] adjacente : 3 dés. Résultat : Épées croisées, Épée, Drapeau. [Armure 1] retire 1 Épée → 1 touche restante (Épées croisées), soit 1 PV perdu (Cavalerie : pas de règle intrinsèque).

---

### [Inébranlable X]

Cette unité ignore **X résultats de retraite** par attaque reçue, quelle qu'en soit la source — dés, cartes tactiques ou sorts.

> 💡 **Exemple de jeu** Une unité [Inébranlable 2] reçoit une attaque dont le résultat produit 3 Drapeaux. Elle ignore 2 Drapeaux → ne recule que d'1 hexagone. Avec seulement 1 ou 2 Drapeaux obtenus, elle ne recule pas du tout.

---

### [Immunisé au poison]

Cette unité ignore les touches supplémentaires générées par la règle **[Poison]**, quelle qu'en soit la source. Les touches normales s'appliquent normalement.

> _Non assignée en V1 — disponible si un peuple ultérieur porte [Poison]._

---

### [Immunisé au feu]

Cette unité ignore les touches supplémentaires générées par la règle **[Souffle de feu]**.

> _Non assignée en V1._

---

### [Protection X]

Lorsqu'une unité occupant une position protégée (bâtiment, fortification) reçoit une attaque, elle ignore **X touches** après décompte des dégâts.

|Type de position|Valeur|
|---|---|
|Ruine|1|
|Bâtiment solide|2|
|Fortification|3|

> 🔗 **Voir aussi** [[Terrain]] §9 — Bâtiment.

---

## Règles offensives — Mêlée

---

### [Archer en mêlée]

Cette unité inflige aussi une touche sur chaque face **Cible** obtenue lors d'une attaque de **mêlée** (normalement inerte en mêlée, voir [[Regles_Base]] §7.2).

> 💡 **Exemple de jeu** Une unité [Archer en mêlée] attaque en mêlée : 3 dés. Résultat : Cible, Épée, Drapeau. Sans cette règle, seule l'Épée toucherait. Avec [Archer en mêlée], la Cible touche aussi → 2 touches au lieu d'une.

> 🎲 **Note de design** Créée pour représenter une précision hors norme qui reste dangereuse même au corps à corps (Legolas, dans le profil de la Compagnie Grise — Gondor). Nommée de façon générique pour pouvoir être réattribuée à d'autres profils.

---

### [Arme Lourde X]

Après le lancer de dés, le joueur peut **relancer X dés** de son choix. Chaque dé ne peut être relancé qu'une seule fois.

> 💡 **Exemple de jeu** Une unité [Arme Lourde 1] attaque une Cavalerie adjacente : 3 dés. Résultat : Épée, Drapeau, Arcane. Le joueur relance l'Arcane → obtient Épées croisées. Résultat final : Épée + Épées croisées = 2 touches.

> 🔄 **Assignée — 2026-07-19** : Guerriers de Lossarnach (Gondor et fiefs), Compagnie Grise tant que Gimli est présent (Gondor et fiefs), Helmingas de Grimbolg (Rohan — haches à deux mains).

---

### [Charge écrasante]

Lorsque cette unité a **effectué un déplacement ce tour** avant d'attaquer, chaque face **Couronne** obtenue inflige **1 touche supplémentaire** à une unité adjacente à la cible (au choix du joueur actif).

> 💡 **Exemple de jeu** Une Créature se déplace d'1 hexagone et attaque une unité d'Infanterie adjacente : 3 dés. Résultat : Épées croisées, Couronne, Drapeau. [Charge écrasante] : la Couronne inflige 1 touche sur une autre unité adjacente à la cible.

> 🔄 **Assignée et confirmée — 2026-07-19 (D029)** : Garde du roi à cheval (Rohan) — la charge de la maison du roi qui déborde sur les rangs adverses. Le Mûmakil recevra sa propre règle dédiée à l'impact au contact plutôt que de réutiliser celle-ci (voir note en tête de document).

---

### [Férocité]

Lorsque cette unité effectue une **contre-attaque**, celle-ci est résolue **avant** que l'adversaire ne résout ses retraites. Si l'adversaire est éliminé par la contre-attaque, ses retraites ne sont pas résolues.

> 💡 **Exemple de jeu** Une unité attaque une unité [Férocité] : 4 Drapeaux. La cible contre-attaque immédiatement ([Férocité]) avant de résoudre sa retraite. Si elle élimine l'attaquant, les Drapeaux ne sont plus appliqués.

---

### [Martyre]

Lorsque cette unité attaque, le joueur peut **sacrifier 1 figurine** de l'unité pour convertir **1 face Couronne** en **1 touche supplémentaire**. La figurine sacrifiée est retirée immédiatement.

> 💡 **Exemple de jeu** Une unité [Martyre] attaque : 2 dés. Résultat : Couronne, Drapeau. Le joueur sacrifie 1 figurine → la Couronne devient 1 touche.

> _Non assignée en V1._

---

### [Réception de charge]

Lorsque cette unité effectue une **contre-attaque** contre une unité qui s'est **déplacée ce tour**, elle lance **1 dé supplémentaire**.

> 💡 **Exemple de jeu** Une Cavalerie avance de 2 hexagones et charge une unité [Réception de charge] : 3 + 1 = **4 dés** en contre-attaque. Si la Cavalerie n'avait pas bougé ce tour, la cible n'aurait que 3 dés.

> 🔄 **Assignée — 2026-07-19** : Hommes d'armes de Dol Amroth (Gondor et fiefs), seule troupe de piquiers du peuple (D021 du [[Document de cadrage]] — assignée par équipement constaté sur la figurine, pas par peuple entier). Aucune unité du Rohan n'en est équipée (voir `02 - Factions/Rohan.md` §5) ; reste ouverte pour un futur profil de piquiers du Rohan.

---

## Règles offensives — Distance

---

### [Bête incontrôlable]

Lorsque **tous les servants/guides** de cette unité sont éliminés, elle **ne peut plus se déplacer** mais peut encore attaquer normalement. Une **touche supplémentaire** l'élimine définitivement.

> _Candidate pour le Mûmakil (risque d'affolement une fois les cornacs tués) — voir note en tête de document._

---

### [Double Tir]

Si cette unité **ne s'est pas déplacée** ce tour, elle peut effectuer une **seconde attaque à distance** après la première, en ciblant la même unité ou une unité différente à portée et en ligne de vue.

> 💡 **Exemple de jeu** Une unité de tir immobile tire sur une cible à 3 hexagones : 2 dés, 1 touche. Grâce à [Double Tir], elle tire une seconde fois sur la même cible : 2 dés, 1 touche supplémentaire.

---

### [Howdah]

Cette unité peut effectuer une **attaque à distance en plus de son attaque de mêlée**. Cette attaque utilise **2 dés**, une portée de **1 à 3 hexagones**, et bénéficie de la règle **[Poison]**.

> _Candidate forte pour le Mûmakil (tour d'archers Haradrim sur son dos) — voir note en tête de document. La règle [Poison] associée est optionnelle et à retrancher si non pertinente pour cette unité._

---

### [Perforant X]

Après le lancer de dés d'une attaque à distance, le joueur peut **relancer X dés** de son choix. Chaque dé ne peut être relancé qu'une seule fois.

> 🎲 **Note de design** [Perforant X] et [Arme Lourde X] partagent la même mécanique de relance. La distinction de nom reflète leur contexte d'usage : [Arme Lourde X] pour la mêlée, [Perforant X] pour le tir à distance.

---

### [Poison]

Lorsque cette unité effectue une attaque, chaque face **Couronne** obtenue inflige **1 touche supplémentaire**, sauf contre les unités **[Immunisées au poison]**.

> _Non assignée en V1._

---

### [Souffle de feu]

Lorsque cette unité effectue une attaque, chaque face **Couronne** obtenue inflige **1 touche supplémentaire**, sauf contre les unités **[Immunisées au feu]**.

> _Non assignée en V1._

---

## Règles de mouvement et de manœuvre

---

### [Déploiement avancé]

Une fois que toutes les unités (amies et ennemies) sont déployées, avant le premier Ordre du tour 1, le joueur propriétaire de cette unité peut la **repositionner** : elle effectue un déplacement égal à sa valeur de Mouvement. Elle ne peut pas terminer ce déplacement au contact d'une unité ennemie.

> 💡 **Exemple de jeu** Une unité [Déploiement avancé] (Mouvement 4) est déployée en retrait derrière la ligne de bataille. Une fois le déploiement terminé des deux côtés, son joueur la repositionne de 4 hexagones vers un flanc dégagé, sans finir au contact d'une unité ennemie — avant même que le premier Ordre du tour 1 ne soit joué.

> 🎲 **Note de design** Créée pour l'Éored d'éclaireur (Rohan) — représente des éclaireurs qui repèrent le déploiement adverse et se replacent en conséquence avant que la bataille ne commence. Contrairement à [Mobilité X], ce redéploiement est unique (avant le tour 1), pas répété après chaque attaque.

> 🔄 **Nouvelle règle — 2026-07-19** : créée et assignée pour l'Éored d'éclaireur (Rohan). Voir D028 du [[Document de cadrage]] et [[Regles_Points]] pour son coût provisoire.

---

### [Meute X]

Cette unité est composée de **plusieurs figurines de X PV chacune**. Retirer une figurine dès qu'elle atteint 0 PV. L'unité est **Faible** quand il ne reste qu'une seule figurine. _(Exception à la règle "jamais Faible" des Créatures.)_

> _Candidate possible pour une unité à plusieurs figurines résistantes (Trolls du Mordor en groupe, par exemple) — à confirmer à la rédaction des profils._

---

### [Mobilité X]

Après avoir effectué une attaque, cette unité peut se déplacer de **X hexagones supplémentaires**.

---

### [Poursuite X]

Alternative à l'avance (voir [[Regles_Base]] §8.2) : se déplacer d'au moins 1 et jusqu'à X hexagones, puis effectuer une attaque supplémentaire contre une unité adjacente à la nouvelle position. Une seule fois par tour.

---

### [Rechargement]

Cette unité **ne peut pas attaquer** lors d'un tour où elle s'est déplacée.

> _Candidate pour une pièce d'artillerie de siège (trébuchet de Gondor, catapulte de Mordor) — à confirmer à la rédaction des profils._

---

### [Terrain favori : X]

Voir [[Terrain]] §11. Annule toutes les restrictions de mouvement et de combat du terrain X pour cette unité — la ligne de vue du terrain reste bloquante. Aucun peuple de la V1 ne porte cette règle pour l'instant.

---

## Récapitulatif alphabétique

|Règle|Catégorie|Résumé|
|---|---|---|
|**[Archer en mêlée]**|Offensif — Mêlée|Les faces Cible touchent aussi en mêlée|
|**[Arme Lourde X]**|Offensif — Mêlée|Relancer X dés après le lancer|
|**[Armure X]**|Défensif|Retire X faces Épée des attaques de mêlée reçues|
|**[Bête incontrôlable]**|Offensif — Distance|Sans guides : ne bouge plus, 1 touche pour éliminer|
|**[Charge écrasante]**|Offensif — Mêlée|Si déplacé ce tour : Couronne → touche sur unité adjacente|
|**[Déploiement avancé]**|Manœuvre|Repositionnement unique avant le tour 1, jusqu'à sa valeur de Mouvement, sans finir au contact ennemi|
|**[Double Tir]**|Offensif — Distance|Seconde attaque si non déplacé ce tour|
|**[Férocité]**|Offensif — Mêlée|Contre-attaque résolue avant les retraites adverses|
|**[Howdah]**|Offensif — Distance|Attaque à distance en plus de la mêlée — 2 dés (1–3) + [Poison]|
|**[Immunisé au feu]**|Défensif|Ignore les touches de [Souffle de feu]|
|**[Immunisé au poison]**|Défensif|Ignore les touches de [Poison]|
|**[Inébranlable X]**|Défensif|Ignore X résultats de retraite par attaque reçue|
|**[Martyre]**|Offensif — Mêlée|Sacrifier 1 fig. pour convertir 1 Couronne en touche|
|**[Meute X]**|Manœuvre|X PV par figurine — Faible à 1 figurine restante|
|**[Mobilité X]**|Manœuvre|Déplacement supplémentaire de X hex après l'attaque|
|**[Perforant X]**|Offensif — Distance|Relancer X dés après le lancer (attaque à distance)|
|**[Poison]**|Offensif — Distance|Couronne → 1 touche sup. (sauf [Immunisé au poison])|
|**[Poursuite X]**|Manœuvre|Alternative à l'avance : jusqu'à X hex + attaque sup.|
|**[Protection X]**|Défensif|Ignore X touches (terrain : bâtiments, fortifications)|
|**[Rechargement]**|Manœuvre|Ne peut pas attaquer si déplacé ce tour|
|**[Réception de charge]**|Offensif — Mêlée|+1 dé en contre-attaque si l'adversaire s'est déplacé ce tour|
|**[Souffle de feu]**|Offensif — Distance|Couronne → 1 touche sup. (sauf [Immunisé au feu])|
|**[Terrain favori : X]**|Manœuvre|Ignore toutes les restrictions de mouvement et de combat du terrain X|

---

## Règles différées — Phase 2+

|Règle|Description préliminaire|Statut|
|---|---|---|
|**[Peur]**|Convertit les Couronnes en Drapeaux supplémentaires contre les unités affectées|⏳ Phase 2|
|**[Terreur]**|Version renforcée de [Peur]|⏳ Phase 2|
|**[Vol]**|L'unité peut traverser des hexagones occupés et ignorer certains terrains — candidate pour les créatures ailées (Nazgûl)|⏳ Phase 2|
|**[Piétinement en zone]**|Attaque touchant plusieurs hexagones adjacents — candidate pour les grandes créatures (Mûmakil, Trolls)|⏳ Phase 2|
|**Système Lore / Arcanes**|Face Arcane activée — magie légère Espoir/Peur (voir [[Document de cadrage]] §5.2)|⏳ Hors scope V1|

---

> 🔗 **Voir aussi** [[Regles_Base]] — [[Terrain]] — [[Document de cadrage]]

---

_Version : 0.4 — Phase 1 — 2026-07-19._ _Première adaptation de Batailles de la Terre du Milieu (BdTdM) : reprise du glossaire mécanique générique, sans reprise du contenu spécifique à l'autre projet dont il est issu. [Massif] retirée (D015). [Arme à feu] supprimée (spécifique aux armes à poudre, sans objet en Terre du Milieu). Index par faction retiré (aucune assignation encore faite). Renommé depuis `BdVM_Regles_Speciales.md`._ _0.2 — Rédaction des profils Gondor et fiefs (voir `02 - Factions/Gondor_et_Fiefs.md`) : nouvelle règle [Archer en mêlée] ajoutée (D024). [Réception de charge] assignée aux Hommes d'armes de Dol Amroth (D021)._ _0.3 — Rédaction en cours des profils Rohan (voir `02 - Factions/Rohan.md`) : nouvelle règle [Déploiement avancé] ajoutée (D028), créée pour l'Éored d'éclaireur. [Charge écrasante] assignée pour la première fois (Garde du roi à cheval). [Arme Lourde 1] assignée aux Helmingas de Grimbolg._ _0.4 — Roster Rohan validé et clos (D029) : [Charge écrasante] confirmée pour la Garde du roi à cheval — le Mûmakil aura sa propre règle dédiée, retirée de la liste des candidates pour cette règle._
