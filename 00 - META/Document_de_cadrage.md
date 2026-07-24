---
projet: "Batailles de la Terre du Milieu"
type: "meta"
phase: "1"
statut: "en-cours"
date_maj: "2026-07-20"
tags: [BdTdM, type/meta, statut/en-cours]
version: "1.13"
---

# Document de cadrage du projet

> **Nature du document :** Ce fichier est le point d'entrée du projet. Il définit la vision, les contraintes de design, la feuille de route et les conventions à respecter dans tous les documents du projet. Il doit être fourni à Claude en début de session pour recadrer le contexte.

---

## Table des matières

1. [Vision du projet](#1-vision-du-projet)
2. [Références et inspirations](#2-références-et-inspirations)
3. [Principes de design](#3-principes-de-design)
4. [Composants du jeu](#4-composants-du-jeu)
5. [Axes d'adaptation — BLv2 vers la Terre du Milieu](#5-axes-dadaptation--blv2-vers-la-terre-du-milieu)
6. [Feuille de route](#6-feuille-de-route)
7. [Conventions de travail](#7-conventions-de-travail)
8. [Journal de décisions](#8-journal-de-décisions)

---

## 1. Vision du projet

**Batailles de la Terre du Milieu (BdTdM)** est une adaptation du système **Commands & Colors** / **BattleLore Seconde Édition** à l'univers du **Seigneur des Anneaux**.

### Ambition

Offrir un système générique pour rejouer les grands affrontements de la Terre du Milieu, décliné en plusieurs formats — **Escarmouche**, **Normal**, **Épique** — plutôt qu'un système taillé pour un seul scénario. La **Bataille des Champs du Pelennor**, objectif de la convention de fin septembre 2026, sert de cas d'usage pour le format **Épique** (6 joueurs, 3v3, 1 table).

### Philosophie de design

> _"Les règles doivent servir le thème, pas l'inverse."_

Le système hérite de l'architecture Commands & Colors / BLv2 (deck de cartes de commandement, dés à faces spéciales, profils d'unités portant les règles spéciales, PV par figurine). Abandon complet de la mécanique précédente à sac de tokens (Destin / Test of Honour).

Figurines MESBG, collection très complète.

---

## 2. Références et inspirations

### Références principales

| Jeu | Ce qu'on en retient |
|---|---|
| **BattleLore Seconde Édition** (FFG) | Référence mécanique principale : dés, règles spéciales, profils d'unités, avance, poursuite, contre-attaque universelle, système Lore (pouvoirs — voir §5.2, réorienté vers une couche Leadership en V1). |
| **Commands & Colors : Medievals** | Structure de commandement (cartes de section + Tactiques), proximité thématique médiévale, profils d'infanterie lourde. |

### Références secondaires

| Jeu | Ce qu'on en retient |
|---|---|
| **C&C Ancients** | Gestion des unités légères, règles d'évasion. Règle *Warriors* (bonus à pleine force, perdu à la première perte) — inspiration directe de [Horde], voir D032. |
| **Memoir '44** | Clarté de présentation des scénarios, format des cartes de terrain, médailles objectif. Face de dé « miss universel » (voir §5.2, D001). |
| **C&C Napoleonics** | Système de moral et de cohésion d'unité. |
| **BattleLore V1** | Règles de Peur/Terreur — pertinentes pour les Nazgûl, les Trolls, les Mûmakil. Premier jalon passé en V1 avec [Peur X] (D033). |
| **Battle of Westeros** | Bonus offensif +1 dé depuis le terrain surélevé. |
| **MESBG (sourcebook officiel)** | Référence de fidélité au texte de Tolkien pour les scénarios et objectifs narratifs — pas de reprise mécanique (échelle et système trop différents). Sert aussi de référence d'identité de peuple quand le texte de Tolkien est trop avare en détails (ex. Khand, voir D031). |

---

## 3. Principes de design

1. **Priorité à la fluidité et à l'accessibilité** : les règles ne doivent jamais ralentir le jeu ni demander de consulter un livre en pleine partie. Contrainte forte : les joueurs sont expérimentés mais de moins en moins à l'aise avec les systèmes complexes — toute règle qui génère une question à chaque résolution est à réviser.
2. **Émotion et narration avant la profondeur tactique** : privilégier les moments marquants (charge des Rohirrim, duel Éowyn/Roi-Sorcier) plutôt que l'optimisation. Conditions de victoire narratives, propres à chaque scénario, fidèles au texte de Tolkien (pas aux films).
3. **Profils comme vecteurs de règles** : les règles spéciales vivent dans les profils d'unités, pas dans un livre de règles à consulter. Un joueur connaît son armée, pas le manuel.
4. **Lisibilité sur la table** : l'état du jeu doit être lisible d'un coup d'œil. Jetons acceptés pour PV et effets temporaires, jamais pour les règles permanentes.
5. **Scalabilité par le format, pas par la complexité** : un même socle de règles doit fonctionner en Escarmouche, Normal et Épique — on ajuste le nombre d'unités et la taille de table, jamais la complexité des règles de base.
6. **Asymétrie assumée** : chaque peuple (Gondor, Rohan, Mordor, Harad...) doit se jouer différemment. L'équilibre se fait par la diversité tactique, pas par la similitude des profils.
7. **Minimalisme des règles de terrain** : le terrain crée de la tension, pas de la complexité. Chaque type de terrain a un effet simple et mémorable.

---

## 4. Composants du jeu

### Champ de bataille

Tapis hexagonal, taille selon le format :

| Format | Taille | Usage |
|---|---|---|
| Escarmouche | 10 × 7 hexagones | Petits engagements, 1v1/2v2 |
| Normal | 13 × 9 hexagones | Format standard, 2v2/3v3 léger |
| Épique | 16 × 13 hexagones | Grands affrontements type Pelennor (3v3, 6 joueurs) |

Divisé verticalement en 3 sections (Gauche / Centre / Droite), quel que soit le format.

### Dés

6 faces : Épées croisées (1-2 touches mêlée), Épée (1 touche mêlée), Cible (1-2 touches tir), Drapeau (retraite), Couronne (capacité spéciale), **Arcane** (échec universel par défaut, D001 — deux exceptions croissantes en V1/Phase 2, voir §5.2).

### Unités

| Type | Figurines/hex | PV | Base |
|---|---|---|---|
| Infanterie | 6 | 1/fig. | 25 mm |
| Cavalerie | 3 | 1/fig. | 40 mm |
| Chars | 1 | Variable | 65 mm |
| Créature / Machine de guerre | 1 | Variable | 65 mm (ex. Troll du Mordor) |
| Artillerie | 1 pièce + servants | 1/servant | — |

Pas de distinction Infanterie standard/élite par le nombre de figurines ou la base (cohérent avec le principe 3 : la différenciation élite/standard passe par le profil, pas par l'effectif).

> ⚠️ **Point ouvert critique — Mûmakil**
> La figurine ne tient pas sur un hex standard (10 cm). Sujet sensible à traiter en profondeur, hors de ce document de cadrage. Pistes possibles : hex agrandi dédié, occupation de plusieurs hexes, ou gabarit hors-grille avec règles de zone d'effet. À planifier comme tâche de conception à part entière. Emmanuel a déjà une idée de règle dédiée pour l'impact au contact (distincte de [Charge écrasante] — D029) ; à formaliser au moment de rédiger ce profil.

---

## 5. Axes d'adaptation — BLv2 vers la Terre du Milieu

### 5.1 Priorité haute — Cœur de règles

- [ ] Système de commandement : deck de cartes C&C (cartes de section + Tactiques). En Épique (3v3), chaque joueur contrôle une Section (Gauche/Centre/Droite) plutôt qu'une armée nommée — pas de sous-force nominative par joueur (D016)
- [ ] Dés : reprise des faces BLv2 (mêlée/tir/retraite/capacité/miss)
- [ ] Types d'unités : Infanterie, Cavalerie, Chars, Créature, Machine de guerre, Artillerie
- [ ] Règle Faible (dernière figurine), Contre-attaque universelle, Avance et Poursuite
- [ ] Règles spéciales de base : [Armure X], [Protection X], [Férocité], [Mobilité X]
- [ ] Formats Escarmouche / Normal / Épique — tables et volumes d'unités par format
- [ ] **Cas Mûmakil** : règle et gabarit dédiés (point ouvert critique, §4)

### 5.2 Priorité moyenne — Héros et monstres avancés

- [ ] Règles des héros à développer : une ébauche de structure a déjà été explorée ailleurs, à formaliser et adapter ici — valeur de commandement modulable, distinction Standard/Majeur (posée en cadrage 5)
- [x] [Peur] de base — **passée en V1** avec [Peur X] (D033, déclenchée par la face Arcane). [Terreur] (version renforcée, X élevé) reste en Phase 2 pour Nazgûl, Trolls majeurs, Roi-Sorcier.
- [ ] Monstres avancés : vol (Fell Beasts), piétinement en zone (Mûmakil/Trolls)

> 🎲 **Note de design — De la « magie » à la couche Leadership**
> Pas de système de sorts en V1 (D001). La piste n'est plus une magie légère mais une **couche Leadership** fondée sur la face **Arcane** (D034) : les héros (Phase 2) exploiteront les Arcanes pour activer des **manœuvres spéciales**, dans l'esprit **Espoir** (Bien — Rune de Gandalf) / **Désespoir** (Mal — Œil de Sauron) déjà pressenti dès la v1.0 de ce document. Premier jalon déjà en V1 : la règle **[Peur X]** (D033, Troll du Mordor), où les Arcanes d'une unité comptent comme des Drapeaux au lieu d'un échec. Points à résoudre en Phase 2 : dé-randomiser l'accès des héros à l'Arcane (un commandement qui « rate » sur un mauvais jet sonne faux — piste : bonus par-dessus le rôle normal du héros, ou génération fiable d'Arcane), et arbitrer la propriété de l'Arcane quand une unité [Peur] et un héros l'exploitent tous deux.

### 5.3 Priorité basse — Contenu et scénarios

- [ ] Peuples à couvrir en V1 : **Gondor et ses fiefs**, **Rohan**, **Khand**, **Mordor** (`02 - Factions/Mordor.md`, D036) et **Easterling** (`02 - Factions/Easterling.md`, D038) rédigés et validés — prêts pour le Playtest #1. Reste : **Harad**.
- [ ] Scénarios : Pelennor comme référence Épique, autres affrontements en Normal/Escarmouche
- [ ] Construction d'armée : valeurs en points par unité et héros

---

## 6. Feuille de route

Convention fin septembre 2026 — cadrage lancé le 18 juillet, soit environ 10 semaines.

### Phase 1 — Fondations (cœur de règles) ← EN COURS

- [ ] Formaliser le corps de règles de base (commandement, dés, types d'unités, Faible, contre-attaque, avance/poursuite, règles spéciales de base)
- [ ] Choisir le format de travail initial : Normal (plus rapide à tester qu'Épique)
- [ ] **Playtest #1** — Gondor (trio 15 pts), Rohan (trio 13 pts), Khand (5 profils), Mordor (trio 19 pts) et Easterling (trio 16 pts) tous rédigés et validés, prêts à être testés. Seul Harad reste à rédiger.

### Phase 2 — Héros, cas Mûmakil, montée en Épique

- [ ] Développer les règles de héros (profils Standard/Majeur)
- [ ] Développer la couche Leadership (manœuvres de héros sur la face Arcane, D034) et [Terreur] (X élevé)
- [ ] Résoudre le cas Mûmakil (gabarit/règle dédiée)
- [ ] Passer au format Épique (16×13), premier test à cette échelle
- [ ] **Playtest #2**

### Phase 3 — Contenu Pelennor

- [ ] Profils d'unités pour les 6 peuples V1 (Gondor et fiefs, Rohan, Mordor, Harad, Khand, Easterling)
- [ ] Reprise et adaptation du travail déjà fait en cadrage 5 (forces, héros, objectifs narratifs) au nouveau système — répartition des peuples par Section plutôt que par sous-force nominative (D016)
- [ ] Valeurs en points, équilibrage Bien/Mal, et limite d'enrôlement des unités légendaires par format (Escarmouche/Normal/Épique) — nécessaire pour arbitrer les quelques dominances strictes assumées en V1 entre profils d'un même peuple (D025)
- [ ] **Playtest #3** (scénario Pelennor complet)

### Phase 4 — Finalisation convention

- [ ] Livret de règles complet + aide de jeu imprimable
- [ ] Fiches unités/héros imprimables
- [ ] Répétition générale avant fin septembre

> ⚠️ **Point ouvert**
> Calendrier resserré (10 semaines) — le découpage tient si chaque phase reste ~2-3 semaines max. À surveiller après le Playtest #1.

---

## 7. Conventions de travail

### Blocs de note standardisés

```
> ⚠️ **Point ouvert**
> Question de design non résolue.

> 🔄 **Modifié après playtest**
> Date : YYYY-MM-DD | Playtest #N
> Description de la modification.

> 🔗 **Voir aussi**
> [[Lien vers règle connexe]]

> 🎲 **Note de design**
> Justification d'un choix de design.
```

### Terminologie fixée

| Terme retenu | Signification | Éviter |
|---|---|---|
| **Champ de bataille** | Surface de jeu (tapis hexagonal) | "Plateau", "Table" |
| **Unité** | Groupe de figurines occupant un hexagone | "Régiment", "Bande" |
| **Section** | Gauche / Centre / Droite du champ de bataille | "Flanc", "Aile" |
| **Ordre** | Activation d'une unité via une carte | "Activation", "Tour" |
| **Carte Tactique** | Carte spéciale (hors carte de section) | "Carte spéciale" |
| **Commandement** | Système de cartes/activation (sens C&C d'origine) — plus de sous-force nominative par joueur | "Commande" |
| **Peuple** | Camp jouable (Gondor, Rohan, Mordor...) | "Faction", "Race" |
| **Camp** | Bien / Mal | "Alliance", "Légion" |
| **Drapeau** | Face de dé forçant une retraite | "Bannière", "Étendard" |
| **Faible** | Unité à 1 PV restant (dernière figurine) | "Blessé", "En déroute" |
| **PV** | Points de Vie — une figurine = 1 PV | "Figurine" (dans un contexte de règle) |
| **Infanterie** | 6 fig., base 25 mm | "Fantassin", "Piéton" |
| **Cavalerie** | 3 fig., base 40 mm | "Cavalier", "Monture" |
| **Chars** | 1/hex, base 65 mm | "Chariot" |
| **Créature** | PV variables, jamais Faible | "Monstre", "Bête" |
| **Machine de guerre** | PV variables, jamais Faible | "Engin" |
| **Artillerie** | Servants éliminés en premier, jamais Faible | "Canon", "Pièce" |
| **Unité légendaire** | Troupe d'élite narrativement marquante, profil enrichi (peut dépasser le plafond de 2 règles spéciales) — **pas** un héros, aucune valeur de commandement individuelle | "Héros" (réservé à la Phase 2, voir §5.2) |

---

## 8. Journal de décisions

| # | Date | Décision | Justification |
|---|---|---|---|
| 001 | 2026-07-18 | Face Arcane = miss universel en V1 | Simplicité, pas de couche magie prévue pour l'instant. Piste future : dés custom par camp (Rune de Gandalf / Œil de Sauron) pour une magie légère Espoir/Peur. *(Révisé par D033/D034 : la face Arcane accueille désormais [Peur X] et, en Phase 2, la couche Leadership — toujours pas de système de sorts.)* |
| 002 | 2026-07-18 | Nom du projet : **Batailles de la Terre du Milieu (BdTdM)** | Basé directement sur Commands & Colors / BattleLore Seconde Édition — pas de dépendance affichée à un autre projet. |
| 003 | 2026-07-18 | Ambition multi-format : Escarmouche / Normal / Épique | Le Pelennor n'est qu'un cas d'usage (format Épique) d'un système générique pour la Terre du Milieu, pas l'unique objectif du système. |
| 004 | 2026-07-18 | Abandon complet de la mécanique à sac de tokens (Destin/Test of Honour) | Jugée trop fragile pour 6 joueurs peu à l'aise avec les règles complexes. Remplacée par le deck de commandement C&C/BLv2. |
| 005 | 2026-07-18 | Format Épique fixé à 16 × 13 hexagones | Dimensionné pour le scénario Pelennor (6 joueurs, 3v3, 1 table). |
| 006 | 2026-07-18 | Bases figurines MESBG : Infanterie 25 mm, Cavalerie 40 mm, Chars/Créatures 65 mm | Alignement sur les bases réelles de la collection MESBG plutôt que sur des valeurs génériques. |
| 007 | 2026-07-18 | Pas de distinction Infanterie standard/élite par base ou effectif | Cohérent avec le principe "profils comme vecteurs de règles" (§3.3) — la différenciation élite/standard passe par le profil, pas par le socle. |
| 008 | 2026-07-18 | Chars = type à 1 figurine/hex, base identique aux Trolls du Mordor (65 mm) | Simplifie la classification, réutilise un gabarit déjà existant. |
| 009 | 2026-07-18 | Cas Mûmakil identifié comme point ouvert critique, hors cadrage | La figurine ne tient pas sur un hex standard (10 cm) — nécessite une tâche de conception dédiée (gabarit ou occupation multi-hex). |
| 010 | 2026-07-18 | Pas de couche pouvoirs/magie pour la V1 | Hors scope pour la convention de septembre — priorité au socle de règles et au contenu Pelennor. *(Nuancé par D033/D034 : la couche Leadership n'est pas un système de sorts, premier jalon [Peur X] passé en V1.)* |
| 011 | 2026-07-18 | Peuples à couvrir en V1 : Gondor et fiefs, Rohan, Mordor, Harad, Khand, Easterling | Correspond aux 6 commandements du scénario Pelennor (cadrage 5) — Elfes/Nains/Isengard réservés à une version future. |
| 012 | 2026-07-18 | Règles des héros à développer en Phase 2 | Une ébauche de structure existe ailleurs et doit être formalisée et adaptée au contexte BdTdM. |
| 013 | 2026-07-18 | Feuille de route en 4 phases sur ~10 semaines | Fondations → Héros/Mûmakil/Épique → Contenu Pelennor → Finalisation, calé sur l'échéance de fin septembre. |
| 014 | 2026-07-18 | Terminologie fixée : "Commandement" (sous-force), "Peuple" (camp jouable), "Camp" (Bien/Mal) | Clarté et cohérence terminologique pour tous les documents du projet. *(Révisé par D016.)* |
| 015 | 2026-07-18 | [Massif] retirée du socle de règles, sans remplacement en V1 | Règle héritée d'un système voisin pour différencier l'infanterie d'élite sur socle 25 mm (type Hommes-Lézards de Warhammer). Toutes les Infanteries de BdTdM partagent déjà la même base (25 mm) — le cas ne se présente plus. Si un besoin de différenciation apparaît en Phase 3, une nouvelle règle sera introduite à ce moment-là. |
| 016 | 2026-07-18 | Abandon de la sous-force nominative par joueur ("Commandement" ne désigne plus que le système de cartes/activation) | La logique "Rohan / Minas Tirith-Dol Amroth / Compagnie Grise" du cadrage 5 n'a plus de sens dans l'architecture C&C pure. En Épique (3v3), chaque joueur contrôle une Section (Gauche/Centre/Droite) ; la répartition des peuples entre sections devient une décision de scénario (Phase 3), pas une règle de commandement. Annule la définition "sous-force" de D014. |
| 017 | 2026-07-18 | Pas de terrain spécifique développé pour le Pelennor | Le champ de bataille est majoritairement plat (des champs qui s'étendent à perte de vue) — les règles de terrain génériques (bois, gué, terrain surélevé) suffiront pour d'éventuels éléments ponctuels introduits par le scénario. |
| 018 | 2026-07-19 | [Arme à distance] (ex-[Arme à feu]) retirée du socle de règles, sans remplacement en V1 | Règle spécifique aux armes à poudre (dés dégressifs avec la distance), héritée par erreur de la référence Memoir '44 — sans objet dans un univers sans armes à feu. Le §2 est corrigé en conséquence : la référence Memoir '44 ne mentionne plus cette règle. Voir [[Regles_Speciales]]. |
| 019 | 2026-07-19 | Carte de commandement "Arcanes de guerre" renommée en "Ruée générale" | Le nom évoquait une magie de bataille, incompatible avec l'absence de couche pouvoirs/magie en V1 (D001, D010). Le mécanisme (activation par dés) reste inchangé. Voir [[Cartes_Commandement]] §4.2. |
| 020 | 2026-07-19 | Portée de tir fixée à 4 hexagones pour les unités d'arc en V1 | Aucune valeur n'était définie dans [[Regles_Base]]. Choisie à la rédaction des profils Gondor et fiefs — assez généreuse pour laisser le tir dominer une partie du champ de bataille sans être illimitée. S'applique à tous les peuples à venir sauf mention contraire dans un profil. |
| 021 | 2026-07-19 | [Réception de charge] assignée par équipement constaté (troupes effectivement armées de piques), pas par peuple entier | Évite d'attribuer une règle anti-cavalerie à un peuple entier par défaut. Pour Gondor et fiefs, seuls les Hommes d'armes de Dol Amroth en sont équipés. Aucune unité du Rohan ou de Khand n'en est équipée dans les rosters validés — reste ouverte pour un futur profil de piquiers. |
| 022 | 2026-07-19 | Convention de profil : Mouvement 2 (Infanterie) / 3 (Cavalerie) par défaut, exception possible si justifiée dans le profil | Garde les profils mémorisables (règle par défaut simple) tout en autorisant des cas spéciaux clairement signalés — Gondor : Chevaliers à pied de Dol Amroth (Mouvement 1, armure très lourde) ; Rohan : Éored d'éclaireur (Mouvement 4, pour donner du rayon d'action à [Déploiement avancé], voir D028). |
| 023 | 2026-07-19 | Convention de profil : maximum 2 règles spéciales pour les troupes standard/élite ; les unités légendaires peuvent en cumuler davantage | Garde la majorité des profils simples à mémoriser à la table tout en laissant les unités légendaires (voir Terminologie §7) se distinguer nettement. Premiers cas côté Gondor : Vétérans d'Osgiliath et Archers de la Racine Noire (3 règles), La Compagnie Grise (mécanique sur mesure, voir D024). Côté Rohan : Garde du Roi, Garde du roi à cheval et Helmingas de Grimbolg (3 règles chacun). Côté Khand : Aurige de Khand (3 règles, pièce signature, voir D031). |
| 024 | 2026-07-19 | Nouvelle règle spéciale [Archer en mêlée] ajoutée au socle : les faces Cible infligent aussi une touche en mêlée | Créée pour le profil de la Compagnie Grise (Gondor et fiefs) — représente la précision hors norme de Legolas, dangereuse même au corps à corps. Nommée génériquement pour pouvoir être réattribuée à d'autres profils/peuples. Voir [[Regles_Speciales]]. |
| 025 | 2026-07-19 | Des dominances strictes entre profils d'un même peuple sont temporairement assumées en V1 | Ex. Chevaliers de Dol Amroth vs Chevaliers de Minas Tirith ; Archers de la Racine Noire vs Rangers d'Ithilien (Gondor et fiefs). Pas un défaut de conception à corriger profil par profil — seront équilibrées en Phase 3 par un coût en points et/ou une limite d'enrôlement des unités légendaires par format (voir §6 Phase 3). |
| 026 | 2026-07-19 | Système de points validé : `Points = Mouvement + PV + (Attaque × D) + Σ coût des règles` (D=3 Mêlée, D=2 Tir), règles spéciales chiffrées par catégorie (pas de coût forfaitaire unique), pas de prime de sécurité pour le Tir en V1, unités composites à figurines nommées chiffrées en pleine puissance | Calibré et testé sur les 14 profils de Gondor et fiefs — valide directement D025 (Chevaliers de Dol Amroth : 23 pts contre 20 pour Minas Tirith ; Racine Noire : 20 pts contre 18 pour Ithilien) sans retoucher aucun profil. Détail complet et table de coût par règle dans [[Regles_Points]]. Arrondi des coûts et généralisation des unités composites restent des points ouverts. |
| 027 | 2026-07-19 | Compression finale ajoutée à la formule de points : `Points_finaux = round(Points_bruts ÷ 3) − 1`, sans changer les poids de la formule brute (D026) | Comparaison aux coûts réels de BattleLore Seconde Édition (échelle 4-8 pour l'essentiel du roster, PV uniforme à 3 par Type standard) : la formule brute de D026 étalait le roster Gondor sur 12 valeurs quasi uniques (14 à 26) pour 14 profils — pas mémorisable. La compression ramène le roster sur 4-8, quasi identique à BattleLore V2, tout en conservant les deux dominances D025 (Chevaliers de Dol Amroth 7 vs Minas Tirith 6 ; Racine Noire 6 vs Ithilien 5). Vérification annexe : le socle Mouvement+PV Infanterie/Cavalerie (8:6) correspond exactement au ratio de durabilité effective en Mêlée (12:9 dés pour tuer) — les poids de D026 n'avaient pas besoin d'être retouchés, seule l'échelle finale posait problème. Clôt le point "Arrondi" laissé ouvert en D026. Détail complet dans [[Regles_Points]] §2bis. |
| 028 | 2026-07-19 | Nouvelle règle spéciale [Déploiement avancé] ajoutée au socle : une fois le déploiement des deux camps terminé, avant le premier Ordre du tour 1, l'unité se repositionne d'un déplacement égal à sa valeur de Mouvement, sans pouvoir finir au contact d'une unité ennemie | Créée pour l'Éored d'éclaireur (Rohan, `02 - Factions/Rohan.md`) — représente un rôle de reconnaissance qui permet de se replacer une fois le dispositif adverse connu, plutôt qu'une capacité de combat. Accompagnée d'une exception de Mouvement (3 → 4, voir D022) pour lui donner un vrai rayon d'action. Coût provisoire de 2 points forfaitaires dans [[Regles_Points]], non testé — à revoir après un premier usage à la table. |
| 029 | 2026-07-19 | [Charge écrasante] confirmée pour la Garde du roi à cheval (Rohan) ; le Mûmakil recevra sa propre règle dédiée à l'impact au contact, distincte de [Charge écrasante] | Emmanuel a déjà une idée de règle spécifique pour le Mûmakil — [Charge écrasante] n'est donc plus listée comme candidate pour cette unité dans [[Regles_Speciales]] et reste assignée à la Garde du roi à cheval (Rohan) et, depuis, à l'Aurige de Khand (D031). Clôture la revue du roster Rohan : les 9 profils sont validés et prêts pour le Playtest #1 (tâche Todoist du 20/07 close). |
| 030 | 2026-07-19 | Type **Chars** : règle intrinsèque tranchée — Jamais Faible, comme Créature/Machine de guerre | Point ouvert depuis la rédaction de [[Regles_Speciales]]. Tranché à l'ouverture du roster Khand (Aurige de Khand) : cohérent avec le fait qu'un char est un véhicule unique, pas un groupe de figurines qui s'amenuise — évite un palier de dégradation supplémentaire à suivre en partie (principe 1). Alternative « dégradation des dés par palier de PV perdus » envisagée et écartée pour la même raison de fluidité. |
| 031 | 2026-07-19 | Identité mécanique de Khand calée sur le matériel MESBG (Variags de Khand) plutôt que sur le texte de Tolkien, très avare sur ce peuple (seule mention : les « Variags of Khand » alliés de Sauron au Pelennor) | Décision d'Emmanuel : pour Khand spécifiquement, le texte ne donne aucun détail de culture, d'équipement ou de tactique — la référence MESBG (guerriers aux haches lourdes, pas d'armure notable, chars rapides) sert de base d'identité mécanique. Ne remet pas en cause le principe de fidélité au texte pour les conditions de victoire narratives des scénarios (§3.2), qui reste la règle pour le contenu propre à chaque bataille. **Roster clos le 2026-07-19** : Mercenaires de Khand (archer) confirmés sans règle ; Aurige de Khand porte 3 règles signature ([Charge écrasante] + [Arme Lourde 1] + [Poursuite 1], PV ramené à 3) ; format resserré à 5 profils confirmé, sans palier standard/élite/légendaire. |
| 032 | 2026-07-19 | Nouvelle règle spéciale [Horde] créée : tant qu'une unité n'a perdu aucun PV, elle bénéficie de +1 dé d'attaque et de [Inébranlable 1] ; ces deux bonus disparaissent définitivement dès la première perte. Coût forfaitaire de 3 points. Réservée aux Orcs (Mordor) — non assignée à un profil existant à sa création, Mordor n'avait pas encore de roster (voir D011) | Proposée par Emmanuel, inspirée de la règle *Warriors* de Commands & Colors: Ancients (bonus à pleine force, perdu à la première perte). Volontairement réservée aux Orcs plutôt qu'à Khand : le fil conducteur de Khand est déjà [Arme Lourde 1] (relance permanente, D031), tout juste validé pour le Playtest #1 — superposer un second mécanisme offensif aurait dilué cette identité fraîchement close. Le pattern « très fort au premier contact, fragile ensuite » colle en revanche précisément au texte pour les Orcs — nombreux, féroces dans la charge, prompts à rompre une fois entamés. Condition lisible directement sur le nombre de figurines restantes, sans jeton supplémentaire (principe 4). Détail complet et coût dans [[Regles_Speciales]] et [[Regles_Points]]. |
| 033 | 2026-07-20 | **[Peur X] déclenchée par la face Arcane** (et non la Couronne), et **sortie du différé Phase 2** — passe en V1 | Proposition d'Emmanuel. Réutilise la face Arcane (échec universel, D001) en résolvant un conflit d'usage de la Couronne avec [Charge écrasante] sur le Troll du Mordor (première assignation). Mécanique triviale et sans jeton (principe 4) : chaque Arcane obtenue en attaque compte comme X Drapeaux, sans infliger de touche. Coût provisoire 2×X ([[Regles_Points]]). Les versions « Terreur » (X élevé, Nazgûl/Roi-Sorcier) restent en Phase 2. Voir `02 - Factions/Mordor.md` et [[Regles_Speciales]]. |
| 034 | 2026-07-20 | **Réorientation de la couche « Magie » vers une couche Leadership fondée sur la face Arcane** (Œil de Sauron / Rune de Gandalf), plutôt qu'un système de sorts | Décision d'Emmanuel, avis de Claude versé au dossier (pour/contre : fidélité à Tolkien — pouvoir de volonté/moral plutôt que pyrotechnie ; complexité concentrée sur les héros, piétaille inchangée, principe 1 ; ressuscite une face morte sans jeton, principe 4 ; asymétrie de camp gratuite, principe 6 — contre : dépendre du dé pour un commandement sonne faux, moment de déclenchement à définir, collision possible avec [Peur]). Reste en **Phase 2**. Deux points ouverts à traiter alors : (a) dé-randomiser l'accès des héros à l'Arcane ; (b) arbitrer la propriété de l'Arcane quand une unité [Peur] et un héros l'exploitent tous deux. Amende D001 et §5.2. |
| 035 | 2026-07-20 | **Identité mécanique de Mordor actée** : [Horde] (D032) comme fil conducteur de la piétaille orque ; [Armure] en **signal d'échelon** (seulement Morannon/Uruk-hai, pas un trait de peuple comme chez Gondor) ; **Uruk-hai en exception steadfast** (Attaque 4 constante, sans Horde — validé) | Parallèle à D031 (identité de Khand). Donne à Mordor une signature distincte des trois peuples déjà cadrés : « nombreux et front-loaded, seule l'élite tient ». Roster : `02 - Factions/Mordor.md` (v0.2, Passe 1 partielle — Uruk-hai et [Peur]/Arcane validés, reste ouvert au §6 du document). |
| 036 | 2026-07-20 | **Roster Mordor clos** : Uruk-hai confirmé avec [Férocité] (7 pts) ; Troll confirmé à [Peur 1] et 5 PV (7 pts) ; Pisteurs orques confirmés sans [Horde] (3 pts, profil de tir simple) | Les 4 derniers points ouverts tranchés avec Emmanuel — les 6 profils sont validés **tels que chiffrés dans l'ébauche initiale**, aucun recalcul nécessaire. Parallèle direct à D029 (clôture Rohan) et D031 (clôture Khand) : restent seulement les coûts de [Horde] et [Peur X] à confirmer au Playtest #1, non bloquants. Roster prêt pour le Playtest #1 (trio Bande d'orques + Uruk-hai + Troll, 19 pts) — voir `02 - Factions/Mordor.md` §3 et §6. Tâche Todoist « Rédiger les profils d'unités — Mordor » close. |
| 037 | 2026-07-20 | **Nouvelle règle spéciale [Mur de bouclier] créée** : tant qu'une unité est adjacente à au moins une autre unité d'Infanterie amie, elle bénéficie de [Protection 1]. Version « conditionnelle à la formation » de [Protection X] (habituellement liée au terrain). Coût provisoire de 1 point forfaitaire | Créée pour la Cohorte d'orientaux et la Cohorte de piquiers orientaux (Easterling, `02 - Factions/Easterling.md`). Proposée par Emmanuel pour incarner « la discipline de la tortue » — une armure qui dépend de la formation tenue, pas un chiffre inconditionnel sur le profil comme [Armure X] chez Gondor. Distingue mécaniquement l'identité "empire discipliné" de l'Easterling de celle de Gondor, tout en gardant les deux peuples thématiquement proches (miroir Bien/Mal). Détail complet dans [[Regles_Speciales]] et [[Regles_Points]]. |
| 038 | 2026-07-20 | **Roster Easterling rédigé et clos dès sa première session** : Cohorte d'orientaux (5 pts, [Mur de bouclier]) ; Cohorte de piquiers orientaux (6 pts, [Réception de charge] + [Mur de bouclier], Attaque relevée à 3 dés) ; Cohorte d'archers orientaux (4 pts, [Double Tir], première assignation de cette règle) ; Cataphractaires orientaux (7 pts, Mouvement réduit à 2 + [Armure 2], première armure doublée du jeu, + [Charge écrasante]) | Identité actée : l'Easterling est le miroir maléfique de Gondor — l'armée régulière et disciplinée du camp du Mal, face à la horde de Mordor (D032/D035) et au verre-canon de Khand (D031). Roster délibérément haut de gamme, assumé par Emmanuel : trio de base à 16 pts, plus cher que le trio Gondor (15) — la faction la plus chère du roster à ce stade. Aucune passe de repasse nécessaire : les 4 profils ont été tranchés en une seule session, contrairement à Mordor (D035→D036). Roster prêt pour le Playtest #1 (trio suggéré : Cohorte + Archers + Cataphractaires, 16 pts) — voir `02 - Factions/Easterling.md`. Tâche Todoist « Rédiger les profils d'unités — Easterling » (due 22/07) traitée en avance et close. |
| 039 | 2026-07-21 | **Playtest #1 cadré en format Normal à 1 joueur par camp** (et non en Épique 3v3/6 joueurs) — scénario rédigé (`[[Playtest1_Avant-garde_sur_le_Pelennor]]`) | Confirmé à la rédaction du scénario : le commandement multi-joueurs Épique est explicitement réservé à la Phase 2 (`[[Cartes_Commandement]]` §7, `[[Regles_Base]]` §5.5), non conçu à ce stade. Le Playtest #1 reste un rodage du moteur en 1v1 ; la montée à 6 joueurs (Épique) est un jalon distinct de Phase 2. L'hypothèse « une Section = un joueur » ne vaut qu'en Épique (D016), pas pour ce test. OOB : Camp Bien (Rohan + Gondor + fiefs, 12 u./60 pts) vs Camp Mal (Khand + Easterling + Mordor, 10 u./62 pts), victoire à 6 unités détruites ; couvre les 5 règles neuves jamais testées ([Horde], [Peur X], [Mur de bouclier], [Déploiement avancé], compromis Aurige de Khand). |

---

*Version : 1.13 — Phase 1 — 2026-07-21. Ajout D039 (Playtest #1 cadré en 1v1 Normal ; scénario `[[Playtest1_Avant-garde_sur_le_Pelennor]]` rédigé). Voir aussi D032-D038 (rosters Mordor et Easterling, règles [Horde]/[Peur X]/[Mur de bouclier]).*
*Document de cadrage initial de Batailles de la Terre du Milieu (BdTdM), établi par adaptation de la structure de cadrage d'un projet jumeau, sans reprise de son contenu mécanique spécifique.*
