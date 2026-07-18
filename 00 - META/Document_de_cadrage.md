---
projet: "Batailles du Vieux Monde"
type: "meta"
phase: "2"
statut: "en-cours"
date_maj: "2026-07-17"
tags: [BdVM, type/meta, statut/en-cours]
version: "7.0"
---

# Batailles du Vieux Monde — Document de cadrage du projet

> **Nature du document :** Ce fichier est le point d'entrée du projet. Il définit la vision, les contraintes de design, la feuille de route et les conventions à respecter dans tous les documents du projet. Il doit être fourni à Claude en début de session pour recadrer le contexte.

---

## Table des matières

1. [[#1. Vision du projet]]
2. [[#2. Références et inspirations]]
3. [[#3. Principes de design]]
4. [[#4. Composants du jeu]]
5. [[#5. Axes d'adaptation — BLv2 vers le Vieux Monde]]
6. [[#6. Feuille de route]]
7. [[#7. Conventions de travail]]
8. [[#8. Journal de décisions]]

---

## 1. Vision du projet

**Batailles du Vieux Monde** est une adaptation du système **Commands & Colors** (Richard Borg) dans l'univers de **Warhammer Fantasy Battle** (le Vieux Monde), en prenant **BattleLore Seconde Édition** (Fantasy Flight Games) comme référence mécanique principale.

### Ambition

Recréer les grandes batailles du Vieux Monde avec la fluidité et la tension tactique de C&C/BLv2, en y intégrant :

- La **diversité des races et factions** de Warhammer Fantasy Battle
- La **magie**, les monstres et les règles spéciales propres à l'univers
- Des **scénarios** couvrant à la fois les batailles canoniques du lore et des affrontements libres

### Philosophie de design

> _"Les règles doivent servir le thème, pas l'inverse."_

- **Accessibilité BLv2** : conserver la structure de jeu qui rend BLv2 immédiatement lisible — cartes de commandement, activation par section, résolution rapide sur dés, règles spéciales portées par les profils.
- **Saveur Warhammer** : chaque faction doit se jouer différemment. Un joueur Empire ne doit pas avoir la même expérience qu'un joueur Orques & Gobelins.
- **Scalabilité** : les règles de base doivent fonctionner en escarmouche comme en grande bataille.

---

## 2. Références et inspirations

### Références principales

| Jeu | Ce qu'on en retient |
|---|---|
| **BattleLore Seconde Édition** (FFG) | Référence mécanique principale depuis la Phase 1.5 : dés, règles spéciales, profils d'unités, avance, poursuite, contre-attaque universelle, système Lore (Phase 2). |
| **C&C Medievals** | Structure de commandement (cartes de section + Tactiques), proximité thématique médiévale, inspiration pour les profils d'infanterie lourde. |

### Références secondaires

| Jeu | Ce qu'on en retient |
|---|---|
| **C&C Ancients** | Gestion des unités légères, règles d'évasion. |
| **Memoir '44** | Clarté de présentation des scénarios, format des cartes de terrain, médailles objectif. Règle [Arme à feu] (dés dégressifs avec la distance). |
| **C&C Napoleonics** | Système de moral et de cohésion d'unité. |
| **BattleLore V1** | Règles de Peur/Terreur, inspiration pour les règles spéciales de faction. |
| **Battle of Westeros** | Bonus offensif +1 dé depuis le terrain surélevé (D086). |

---

## 3. Principes de design

1. **Priorité à la fluidité** : les règles ne doivent jamais ralentir le rythme de jeu. Toute règle qui génère des questions à chaque résolution est à réviser.
2. **Profils comme vecteurs de règles** : les règles spéciales vivent dans les profils d'unités, pas dans un livre de règles à consulter. Un joueur connaît son armée, pas le manuel.
3. **Lisibilité sur la table** : l'état du jeu doit être lisible d'un coup d'œil. L'utilisation de jetons est acceptée pour les PV et effets temporaires, jamais pour les règles permanentes.
4. **Asymétrie assumée** : les deux factions n'ont pas à être symétriques. L'équilibre se fait par la diversité des approches tactiques, pas par la similitude des profils.
5. **Minimalisme des règles de terrain** : le terrain crée de la tension, pas de la complexité. Chaque type de terrain a un effet simple et mémorable.

---

## 4. Composants du jeu

### Champ de bataille

- Tapis hexagonal. Format Escarmouche : **10 × 7 hexagones**. Format Bataille : **13 × 9 hexagones**.
- Divisé verticalement en 3 sections (Gauche / Centre / Droite).

### Dés

6 faces, version 4.0 — **validées** *(Playtest #02)* :

| Face | Effet mêlée | Effet tir |
|---|---|---|
| **Épées croisées** | 1 ou 2 touches* | Échec |
| **Épée** | 1 touche (inactive si Faible) | Échec |
| **Cible** | Échec | 1 ou 2 touches* |
| **Drapeau** | 1 hex de retraite | 1 hex de retraite |
| **Couronne** | Capacité spéciale | Capacité spéciale |
| **Arcane** | Échec (Phase 2) | Échec (Phase 2) |

*\* 2 touches sur Infanterie (sans [Massif]) — 1 touche sur tous les autres types. Voir §5.1 et [BdVM_Regles_Base] §2.3.*

### Unités

| Type | Figurines | PV | Base |
|---|---|---|---|
| Infanterie standard (20 mm) | 6 | 1 par fig. | 20 mm |
| Infanterie élite (25 mm) | 4 | 1 par fig. | 25 mm |
| Cavalerie | 3 | 1 par fig. | 25–40 mm |
| Créature / Machine de guerre | 1 | Variable | 40–60 mm |
| Artillerie | 1 pièce + servants | 1 par servant | — |

---

## 5. Axes d'adaptation — BLv2 vers le Vieux Monde

### 5.1 Priorité haute — Cœur de règles

- [x] **Système de commandement** : deck de cartes C&C conservé ✅
- [x] **Dés** : refonte complète alignée BLv2 ✅ *(Playtest #01)*
- [x] **Faces de dés v4.0** : validées ✅ *(Playtest #02)*
- [x] **Règle Faible** : dernière figurine — malus offensif ✅ *(Playtest #01)*
- [x] **Contre-attaque universelle** ✅ *(Playtest #01)*
- [x] **Avance universelle** ✅ *(Playtest #02)*
- [x] **Avance et Poursuite** ✅ *(Playtest #01)*
- [x] **Déploiement alterné** ✅ *(Playtest #02 — formalisé §3.2 — Phase 1.6 Étape 4)*
- [x] **Analyse comparative BLv2 complète** ✅ *(Phase 1.5 — voir BdVM_Analyse_BLv2.md)*
- [x] **[Armure X]**, **[Protection X]**, **[Férocité]**, **[Mobilité X]** ✅ *(Phase 1.5)*
- [x] **Recalibration des dés** : retour aux valeurs BLv2 originales ✅ *(Phase 1.6 — D060)*
- [x] **Système de types d'unités** : Infanterie, Cavalerie, Créature, Machine de guerre, Artillerie ✅ *(Phase 1.6 — D070)*
- [x] **Règle intrinsèque Infanterie** : Épées croisées et Cible → 2 PV ✅ *(Phase 1.6 — D071)*
- [x] **[Massif]** : annule la règle intrinsèque Infanterie ✅ *(Phase 1.6 — D072)*
- [x] **[Arme à feu]** : dés dégressifs avec la distance ✅ *(Phase 1.6 — D073)*
- [x] **[Inébranlable X]** : ignore X résultats de retraite ✅ *(Phase 1.6 — D074)*
- [x] **[Meute X]** : Créature multi-figurines avec PV par figurine ✅ *(Phase 1.6 — D075)*
- [x] **Profils d'unités Empire v4.0** ✅ *(Phase 1.6 Étape 2)*
- [x] **Profils d'unités Hommes-Lézards v4.0** ✅ *(Phase 1.6 Étape 2)*
- [x] **`BdVM_Regles_Speciales.md` v2.1** ✅ *(Phase 1.6 Étape 2)*
- [x] **Collines — bonus offensif +1 dé depuis la hauteur** ✅ *(Phase 1.6 — D086)*
- [x] **[Terrain favori : Boisé]** : annule les restrictions de mouvement et de combat en forêt ✅ *(Phase 1.6 — D089)*
- [x] **`BdVM_Terrain.md` v3.0** ✅ *(Phase 1.6 Étape 3)*
- [x] **`BdVM_Regles_Speciales.md` v2.2** ✅ *(Phase 1.6 Étape 3)*
- [x] **Recalibration [Réception de charge]** : +2 dés → +1 dé ✅ *(Phase 1.6 — D091)*
- [x] **Playtest #3 — validation finale du socle de règles** ✅ *(Phase 1.6 — 2026-07-17, victoire Hommes-Lézards 5-4)*

### 5.2 Priorité moyenne — Couche fantasy

- [ ] **Système de magie** : basé sur le système Lore de BLv2, adapté aux lores du Vieux Monde. Face Arcane activée. *(Phase 2)*
- [ ] **Héros** : valeur de commandement modulable, figurine indépendante. *(Phase 2)*
- [ ] **Monstres et créatures avancés** : vol, piétinement en zone, souffle en cône. *(Phase 2)*
- [ ] **Règles raciales** : au moins une mécanique distinctive par grande faction. *(Phase 3)*
- [ ] **[Peur] / [Terreur]** : Couronnes converties en Drapeaux. *(Phase 2)*
- [ ] **Stégadon + Machine des Dieux** : profil étendu avec capacités magiques Slann. *(Phase 2)*

### 5.3 Priorité basse — Contenu et scénarios

- [ ] **Liste des factions à couvrir en V1** (proposition : Empire, Bretonie, Orques & Gobelins, Nains, Elfes Sylvains, Morts-Vivants)
- [ ] **Scénarios historiques/canoniques**
- [ ] **Construction d'armée** : valeurs en points par unité et par héros, budget par scénario. *(Phase 3)*

---

## 6. Feuille de route

### Phase 1 — Fondations ✅ CLÔTURÉE

- [x] Rédiger les règles de base ✅
- [x] Concevoir le deck de commandement V1 ✅
- [x] Définir les profils d'unités Empire et Hommes-Lézards ✅
- [x] Écrire le scénario Playtest #1 ✅
- [x] **Playtest #1** — 2026-04-24 ✅

**Bilan :** Victoire Hommes-Lézards 4-1. Problèmes majeurs : encombrement plateau, [Massif] trop puissant, [Intrépide] inopérant, [Rechargement] fastidieux, dés déséquilibrés. Décision : pivot vers BLv2 → Phase 1.5.

---

### Phase 1.5 — Refondation mécanique BLv2 ✅ CLÔTURÉE

- [x] Étape 1 — Analyse comparative BLv2 / BdVM ✅
- [x] Étape 2 — Mise à jour Document de cadrage ✅
- [x] Étape 3 — Réécriture `BdVM_Regles_Base.md` v4.0 ✅
- [x] Étape 4 — Réécriture `BdVM_Regles_Speciales.md` v2.0 ✅
- [x] Étape 5 — Profils Empire v2.0 et Hommes-Lézards v1.0 ✅
- [x] Étape 6 — `BdVM_Cartes_Commandement.md` v3.0 ✅
- [x] Étape 7 — `BdVM_Terrain.md` v2.0 ✅
- [x] **Playtest #2** — 2026-05-15 ✅

**Bilan :** Victoire Empire 4-1. Partie plus équilibrée que le Playtest #1. Problèmes majeurs : doublement des dés génère trop de Drapeaux, déroutes trop rapides, cavalerie trop dominante, [Salve] trop puissant, collines sans intérêt stratégique. Décision : recalibration sur valeurs BLv2 originales → Phase 1.6.

> 🔗 Voir [[BdVM_cloture_phase1_5]] pour le bilan détaillé.

---

### Phase 1.6 — Recalibration et stabilisation ✅ CLÔTURÉE

**Objectif :** Corriger les déséquilibres identifiés au Playtest #2, stabiliser le corps de règles, valider au Playtest #3.

- [x] **Étape 1** — Recalibration des dés : retour aux valeurs BLv2 originales. Introduction de [Ligne]. Révision profils Empire v3.0 et HL v2.0 ✅
- [x] **Étape 2** — Refonte des types d'unités, révision complète des profils Empire v4.0 et HL v4.0, réécriture `BdVM_Regles_Speciales.md` v2.1 ✅
- [x] **Étape 3** — Terrain surélevé : bonus +1 dé depuis la hauteur (D086). Création [Terrain favori : Boisé] (D089). Skinks mis à jour (D090). → `BdVM_Terrain.md` v3.0 · `BdVM_Regles_Speciales.md` v2.2 ✅
- [x] **Étape 4** — Formalisation déploiement alterné (§3.2) + mise à jour §7.5 terrain surélevé → `BdVM_Regles_Base.md` v4.2 ✅
- [x] **Étape 5** — Suppression `Livre de règles.md` ✅
- [x] **Étape 6** — Recalibration [Réception de charge] : +2 dés → +1 dé (D091) ✅
- [x] **Étape 7** — Écriture scénario Playtest #3 → `BdVM_Playtest3_scenario.md` ✅
- [x] **Playtest #3** — 2026-07-17 ✅

**Bilan :** Victoire Hommes-Lézards 5-4. Partie la plus équilibrée du projet à ce jour — tension maintenue jusqu'au dernier tour, aucun sens unique. Toutes les mécaniques prioritaires validées (colline comme objectif, Kroxigors enfin engagés, Chevaliers et Flagellants bien calibrés, [Massif] approprié). Deux points non testés validés par défaut ([Terrain favori : Boisé], [Martyre]). Point mineur reporté : visibilité de [Réception de charge] à table (support visuel à envisager en Phase 2).

> 🔗 Voir [[BdVM_cloture_phase1_6]] pour le bilan détaillé.

---

### Phase 2 — Couche fantasy ← EN COURS

**Objectif :** Introduire la magie, les héros et les monstres avancés sur un socle de règles désormais validé.

- [ ] Concevoir le système de magie (face Arcane activée, basé sur Lore BLv2)
- [ ] Intégrer le système de héros (valeur de commandement modulable)
- [ ] Rédiger les règles [Peur] et [Terreur]
- [ ] Rédiger les règles pour les Monstres (vol, piétinement en zone, souffle en cône)
- [ ] Profils Phase 2 : Slann Mage-Prêtre (HL) ; Stégadon + Machine des Dieux (HL)
- [ ] Envisager un support visuel pour [Réception de charge] (point mineur reporté de la Phase 1.6)
- [ ] **Playtest #4** : tester l'équilibre magie vs. non-magie

---

### Phase 3 — Factions

- [ ] Rédiger les règles spéciales pour chaque faction
- [ ] Créer les profils d'unités par faction
- [ ] Définir les valeurs en points (unités + héros)
- [ ] Écrire 2 à 3 scénarios par affrontement de factions
- [ ] **Playtest #5** : équilibrage inter-factions

---

### Phase 4 — Finalisation

- [ ] Rédiger le livret de règles complet
- [ ] Rédiger le livret de scénarios V1
- [ ] Créer les fiches unités imprimables
- [ ] Relecture globale et cohérence terminologique

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
| **Drapeau** | Face de dé forçant une retraite | "Bannière", "Étendard" |
| **Faible** | Unité à 1 PV restant (dernière figurine) | "Blessé", "En déroute" |
| **PV** | Points de Vie — une figurine = 1 PV (sauf [Meute X]) | "Figurine" (dans un contexte de règle) |
| **Infanterie** | Type d'unité : règle intrinsèque 2 PV sur Épées croisées/Cible | "Fantassin", "Piéton" |
| **Cavalerie** | Type d'unité : 3 figurines, 1 PV par figurine | "Cavalier", "Monture" |
| **Créature** | Type d'unité : PV variables, jamais Faible (sauf [Meute X]) | "Monstre", "Bête" |
| **Machine de guerre** | Type d'unité : PV variables, jamais Faible | "Engin", "Véhicule" |
| **Artillerie** | Type d'unité : servants éliminés en premier, jamais Faible | "Canon", "Pièce" |
| **[Inébranlable X]** | Ignore X résultats de retraite par attaque reçue | "[Inamovible]", "[Immovable]" |
| **[Terrain favori : X]** | Annule les restrictions de mouvement et de combat du terrain X | "Affinité", "Expertise" |

---

## 8. Journal de décisions

| # | Date | Décision | Justification |
|---|---|---|---|
| 001–014 | 2026-03-xx | *(Décisions Phase 1 — voir BdVM_cloture_phase1.md)* | |
| 015 | 2026-03-31 | Terme "Drapeau" retenu pour la face de retraite | Élimine la confusion avec la signification Warhammer du terme "Bannière". |
| 016 | 2026-03-31 | Règle [Cavalerie] : 2 touches = 1 figurine perdue | Cohérent avec l'effectif réduit et le doublement des dés. **Annulé par D068.** |
| 017–021 | 2026-03-31 | *(Décisions Phase 1 — voir BdVM_cloture_phase1.md)* | |
| 022 | 2026-04-24 | **Pivot BLv2** : BattleLore V2 devient la référence mécanique principale | Playtest #1 révèle que la base C&C Medievals est insuffisamment adaptée au format Escarmouche fantasy. |
| 023 | 2026-04-24 | **Effectifs révisés** : 20 mm → 6 fig., 25 mm → 4 fig., cavalerie → 3 fig. | Encombrement trop important sur plateau 10×7. |
| 024 | 2026-04-24 | **Refonte des dés** : Épées croisées / Épée / Cible / Drapeau / Couronne / Arcane | Suppression du Poing. Alignement BLv2. |
| 025 | 2026-04-24 | **Règle Faible** : dernière figurine → ne touche plus sur Épée, malus moral | Crée une dynamique de fin de vie lisible et universelle. |
| 026 | 2026-04-24 | **Contre-attaque universelle** | Alignement BLv2. |
| 027 | 2026-04-24 | **Avance universelle** : après élimination ou retraite forcée d'une cible adjacente | Alignement BLv2. |
| 028 | 2026-04-24 | Suppression de [Massif v1], [Intrépide], [Rechargement v1], [Colosse] | Remplacés par des mécaniques BLv2 plus simples. |
| 029 | 2026-04-24 | **[Tenace]** : 2 touches simultanées pour éliminer la dernière figurine | Résistance structurelle. **Annulé par D072 sur la majorité des unités.** |
| 030–059 | 2026-04-24 à 2026-05-04 | *(Décisions Phase 1.5 — voir BdVM_Analyse_BLv2.md et BdVM_cloture_phase1_5.md)* | |
| 060 | 2026-05-15 | **Retour aux valeurs de dés BLv2 originales** | Le doublement génère des Drapeaux excessifs, des déroutes injouables et neutralise les règles spéciales. |
| 061 | 2026-05-15 | **Plafond forêt** : retour à 2 dés max (BLv2 standard) | Conséquence directe de D060. |
| 062 | 2026-05-15 | **[Salve] abandonné** — remplacé par [Arme à feu] (D073) | 8 dés à bout portant trop puissant. **Annulé et remplacé par D073.** |
| 063 | 2026-05-15 | **Valeur de Moral abandonnée** : retour à 1 Drapeau = 1 hex de retraite | Conséquence de D060. |
| 064 | 2026-05-15 | **`Livre de règles.md` supprimé** | Document obsolète, source de confusion. |
| 065 | 2026-05-15 | **Déploiement alterné validé** — à formaliser dans `BdVM_Regles_Base` §3 | Fonctionne bien, aucun problème observé sur deux playtests. |
| 066 | 2026-05-17 | **Règle [Ligne] introduite** — remplacée par la règle intrinsèque Infanterie (D071) | Préservait l'effet visuel "grande bataille". **Annulée et remplacée par D071.** |
| 067 | 2026-05-17 | **Effectifs 25 mm fixés à 4 figurines** | Différenciateur de durabilité et de coût en points. |
| 068 | 2026-05-17 | **Suppression de la règle "2 PV par figurine" pour la cavalerie** — retour à 1 PV par figurine | Alignement BLv2 standard. Annule D016. |
| 069 | 2026-05-17 | **Suppression des PV multiples des Kroxigors** | Simplification mécanique. Remplacé par [Meute 2] (D075). Annule le système Kroxigors v1.0. |
| 070 | 2026-05-23 | **Système de types d'unités** : Infanterie, Cavalerie, Créature, Machine de guerre, Artillerie | Architecture unifiée. Chaque type porte ses règles intrinsèques — supprime le besoin de règles spéciales redondantes ([Ligne], [Cavalerie]). |
| 071 | 2026-05-23 | **Règle intrinsèque Infanterie** : Épées croisées et Cible → 2 PV perdus chez la cible | Maintient la durabilité des unités à 6 figurines (6 touches pour éliminer) dans la dynamique BLv2. Remplace [Ligne]. |
| 072 | 2026-05-23 | **[Massif] redéfini** : annule la règle intrinsèque Infanterie — 1 PV par touche | Différenciateur fort pour l'infanterie Saurus. Remplace [Tenace] sur Saurus à l'Épée, Saurus à la Lance, Gardes du Temple. Annule D029 sur ces unités. |
| 073 | 2026-05-23 | **[Arme à feu]** : −1 dé par hexagone de distance au-delà du premier | Remplace [Salve]. Thématique (poudre noire), réutilisable (Arquebusiers, Pistoliers, Canon, Tank à vapeur). Inspiré de Memoir '44 / Battlecry. |
| 074 | 2026-05-23 | **[Inébranlable X]** : ignore X résultats de retraite par attaque reçue (dés, cartes, sorts) | Traduction officielle BLv2 VF de "Immovable X". Remplace [Frénésie] sur les Flagellants. Flagellants [2], Tank à vapeur [1], Stégadon [1]. |
| 075 | 2026-05-23 | **[Meute X]** : Créature multi-figurines de X PV chacune, Faible à 1 figurine | Résout le cas Kroxigors (Créature à 2 figurines). Exception explicite à la règle "jamais Faible" des Créatures. |
| 076 | 2026-05-23 | **Nouvelles unités Empire** : Canon de l'Empire (Artillerie) et Tank à vapeur (Machine de guerre) | Anticipé Phase 2 → avancé en Phase 1.6 pour enrichir les rosters du Playtest #3. |
| 077 | 2026-05-23 | **Nouvelles unités Hommes-Lézards** : Stégadon (Créature) et Saurus sur Carnosaure (Créature) | Idem D076. |
| 078 | 2026-05-23 | **[Bête incontrôlable]** : Salamandres sans servants — immobile, 1 touche pour éliminer | Formalise le comportement des Salamandres seules. Règle spécifique non réutilisable. |
| 079 | 2026-05-23 | **[Charge écrasante]** : si déplacé ce tour, Couronne → touche sur unité adjacente au choix | Règle thématique pour les grandes créatures en charge. Réutilisable (Stégadon, Saurus sur Carnosaure). |
| 080 | 2026-05-23 | **[Howdah]** : attaque à distance 2 dés (1–3) + [Poison] en plus de la mêlée | Identité distinctive du Stégadon. Reflète les Skinks archers embarqués. |
| 081 | 2026-05-23 | **[Perforant X] reformulé** : relance X dés (attaque à distance) — abandon de la réduction d'[Armure] | [Armure] ne protège que contre la mêlée (faces Épée). [Perforant] sur une unité de tir était sans effet. |
| 082 | 2026-05-23 | **Salamandres** : passage au type Artillerie, attaque portée à 3 dés | Cohérence avec le modèle Canon/Artillerie. La hausse offensive (+1 dé) compense la perte de mobilité relative du type Artillerie. |
| 083 | 2026-05-23 | **Saurus sur Sang-froid** : suppression de [Tenace], attaque ramenée à 3 dés | Simplification. [Tenace] redondant avec la durabilité native de la Cavalerie à 3 PV. |
| 084 | 2026-05-23 | **Grandes Épées** : [Arme Lourde 2] → [Arme Lourde 1] | 4 dés + 2 relances + règle intrinsèque Infanterie trop puissant. 4 dés + 1 relance reste une unité d'élite clairement différenciée. |
| 085 | 2026-05-23 | **Kroxigors** : Mouvement 1 → Mouvement 2, type Créature [Meute 2] | Kroxigors trop passifs au Playtest #2 (Mouvement 1, jamais engagés). Mouvement 2 permet l'engagement. [Meute 2] remplace le système 4 figurines + [Tenace]. |
| 086 | 2026-05-30 | **Bonus colline** : +1 dé en attaque (mêlée et tir) depuis le terrain surélevé vers un hexagone en contrebas | Collines sans intérêt stratégique au Playtest #2 — aucune raison d'y aller. Inspiré de Battle of Westeros (autre implémentation C&C). Simple, lisible, crée un enjeu de contrôle. |
| 087 | 2026-05-30 | **Coût de mouvement terrain surélevé** : **écarté** — mouvement libre conservé | Simplicité prioritaire. Le bonus offensif suffit à créer l'enjeu sans pénaliser le mouvement. |
| 088 | 2026-05-30 | **Retraite en terrain surélevé** : pas de restriction (inchangé) | Aucun problème identifié. La retraite sur colline est intuitive et sans friction. |
| 089 | 2026-05-30 | **[Terrain favori : Boisé]** : annule toutes les restrictions de mouvement et de combat du terrain boisé — la LdV reste bloquante | Symétrie tactique : l'ennemi est gêné en forêt, les Skinks non. Annule pénalité (plafond 2 dés, arrêt à l'entrée, arrêt de retraite) sans conférer de bonus. |
| 090 | 2026-05-30 | **Skinks** : ajout de [Terrain favori : Boisé] au profil | Application directe de D089. Reflète la nature de chasseurs-cueilleurs des Skinks dans la jungle/forêt. Mis à jour dans `BdVM_Hommes_Lezards_Unites.md` et `BdVM_Regles_Speciales.md`. |
| 091 | 2026-07-17 | **[Réception de charge]** : +2 dés → **+1 dé** | +2 dés était un reliquat du doublement des dés (D060), jamais recalibré. Incohérent avec le retour aux valeurs BLv2 standard. Recalibré pour cohérence avant Playtest #3. |
| 092 | 2026-07-17 | **Phase 1.6 clôturée, Phase 2 débloquée** | Playtest #3 valide l'ensemble du socle de règles BLv2 — victoire Hommes-Lézards 5-4, partie la plus équilibrée du projet à ce jour. Toutes les mécaniques prioritaires validées ; aucun point bloquant reporté. |

---

*Version : 7.0 — Phase 2 — 2026-07-17.*
*🔄 Phase 1.6 clôturée suite au Playtest #3 (victoire Hommes-Lézards 5-4). Phase 2 débloquée. Décisions D091 ([Réception de charge] +1 dé) et D092 (clôture de phase) ajoutées. En-tête YAML mise à jour (phase 2, version 7.0).*
*Remplace : Document_de_cadrage v6.1 (2026-05-30).*
