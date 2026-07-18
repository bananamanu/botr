---
projet: "Batailles du Vieux Monde"
type: "meta"
phase: "1.5"
statut: "validé"
date_maj: "2026-04-27"
tags: [BdVM, type/meta, phase/1.5, statut/validé]
---

# BdVM — Analyse comparative BattleLore V2 / BdVM
## Phase 1.5 — Étape 1

> **Objet de ce document :** Passer en revue l'ensemble des mécaniques de *BattleLore Seconde Édition* (Fantasy Flight Games, 2013) et déterminer pour chacune son statut dans BdVM : reprise à l'identique, reprise avec adaptation, ou écartée avec justification. Ce document sert de base de référence pour les étapes 3 à 7 de la Phase 1.5.
>
> **Sources utilisées :** Rulebook BLv2 (20 pages) + Reference Book BLv2 (12 pages) + `BdVM_Playtest_01.md` + `Document_de_cadrage.md` v2.0.
>
> **Statut :** Revue complète effectuée le 2026-04-27. Tous les points ouverts sont tranchés.

> 🔗 **Voir aussi** [[Document de cadrage]] — [[BdVM_Regles_Base]] — [[BdVM_Playtest_01]]

---

## Table des matières

1. [Structure de la partie](#1-structure-de-la-partie)
2. [Commandement et activation](#2-commandement-et-activation)
3. [Mouvement](#3-mouvement)
4. [Combat — Séquence de résolution](#4-combat--séquence-de-résolution)
5. [Dés et résultats](#5-dés-et-résultats)
6. [Moral et retraites](#6-moral-et-retraites)
7. [Contre-attaque et avance](#7-contre-attaque-et-avance)
8. [Unités — Statuts et règles universelles](#8-unités--statuts-et-règles-universelles)
9. [Terrain](#9-terrain)
10. [Ligne de vue](#10-ligne-de-vue)
11. [Règles spéciales d'unités (BLv2)](#11-règles-spéciales-dunités-blv2)
12. [Cartes de commandement spécifiques (BLv2)](#12-cartes-de-commandement-spécifiques-blv2)
13. [Système Lore (BLv2)](#13-système-lore-blv2)
14. [Mustering / Construction d'armée (BLv2)](#14-mustering--construction-darmée-blv2)
15. [Scénarios et mise en place (BLv2)](#15-scénarios-et-mise-en-place-blv2)
16. [Règles optionnelles (BLv2)](#16-règles-optionnelles-blv2)
17. [Synthèse et décisions](#17-synthèse-et-décisions)

---

## Légende des statuts

| Statut | Signification |
|---|---|
| ✅ **Repris** | Mécanique intégrée à l'identique dans BdVM |
| 🔧 **Adapté** | Mécanique reprise avec modifications pour coller à BdVM/Warhammer |
| ❌ **Écarté** | Mécanique non retenue, avec justification |
| ⏳ **Différé** | Mécanique non traitée en Phase 1.5, réservée à une phase ultérieure |

---

## 1. Structure de la partie

### BLv2

La partie se déroule en tours alternés. Chaque tour comprend deux phases : la **Main Phase** (Command Step → Order Step → Move Step → Attack Step) et l'**Upkeep Phase** (VP Step → Draw Step → Lore Step). Le joueur qui a le token premier joueur garde ce statut toute la partie. La victoire est vérifiée à chaque début de tour du premier joueur (16 PV ou élimination totale).

### Décisions

| Élément BLv2 | Statut | Note |
|---|---|---|
| Structure Main Phase / Upkeep Phase | ✅ **Repris** | Reprise à l'identique. Nomenclature harmonisée dans BdVM_Regles_Base v4.0. |
| VP Step + Draw Step | ✅ **Repris** | |
| Lore Step | ⏳ **Différé** | Phase 2 |
| Token premier joueur fixe | ✅ **Repris** | Défini dans le scénario |
| Condition de victoire — seuil de PV | 🔧 **Adapté** | Seuil adapté par format. 4 pts Escarmouche validé Playtest #1. Bataille/Épique à définir post-Playtest #2. |
| Condition de victoire — élimination totale | ✅ **Repris** | Universelle, immédiate |
| Vérification victoire au début du tour | ✅ **Repris** | À inscrire explicitement dans BdVM_Regles_Base |
| Gains de PV | 🔧 **Adapté** | Règle générale : 1 unité éliminée = 1 PV. Les scénarios peuvent ajouter des médailles objectif (tenir un hex, franchir une ligne, éliminer une unité spécifique) inspirées de Memoir'44. |

> 🎲 **Note de design** La structure BLv2 est plus atomisée que l'ancienne structure BdVM. La séparation Move Step / Attack Step permet de gérer proprement les règles comme [Double Tir] (pas de mouvement ce tour) ou [Mobilité X] (mouvement après combat). La terminologie BLv2 sera reprise intégralement dans BdVM_Regles_Base v4.0.

---

## 2. Commandement et activation

### Décisions

| Élément BLv2 | Statut | Note |
|---|---|---|
| Jouer une carte obligatoire par tour | ✅ **Repris** | |
| Ignorer le texte → activer 1 unité partout | ✅ **Repris** | À mettre en valeur dans les règles de base — réflexe crucial pour les nouveaux joueurs |
| Unité ordonnée libre de bouger et/ou attaquer | ✅ **Repris** | |
| Défausser la carte jouée | ✅ **Repris** | |
| Piocher 1 carte en fin de tour | ✅ **Repris** | |
| Deck commun aux 2 joueurs | ✅ **Repris** | Phase 1.5. Cartes de faction éventuelles en Phase 3. |
| Reformation du deck (mélange défausse) | ✅ **Repris** | |
| Valeur de commandement | 🔧 **Adapté** | Fixée à 4 en Phase 1.5 (sans héros). En Phase 2+ : valeur de base 3 + valeur du meilleur héros vivant. Voir D042–D043. |

---

## 3. Mouvement

### Décisions

| Élément BLv2 | Statut | Note |
|---|---|---|
| Valeur de mouvement définie dans le profil | ✅ **Repris** | 1 valeur unique — l'unité peut toujours se déplacer et attaquer. Les exceptions sont dans le profil (ex. artillerie). |
| Hex occupé = infranchissable | ✅ **Repris** | |
| Terrain bloquant = arrêt immédiat | ✅ **Repris** | |
| Mouvement forcé impossible = pas de mouvement | ✅ **Repris** | |
| Unité ne peut pas sortir du champ de bataille | ✅ **Repris** | |
| Sections = activation uniquement, pas d'effet sur le mouvement | ✅ **Repris** | Format BdVM conservé (3-4-3 / 5-5-5), différent de BLv2 (4-4-4) |

> 🎲 **Note de design** Simplification importante par rapport à la Phase 1 : suppression de la distinction "X hex sans combat / Y hex avec combat". Une seule valeur de mouvement, toujours combinable avec le combat. Les exceptions (artillerie, unités spéciales) sont portées par le profil.

---

## 4. Combat — Séquence de résolution

### BLv2 (Reference Book p.2) — 11 étapes

1. Déclarer la cible
2. Jet de combat
3. Relances et modifications
4. Engager les dés (Commit)
5. Ignorer les dégâts
6. Subir les dégâts
7. Ignorer les retraites
8. Résoudre les retraites
9. Gagner du Lore
10. Contre-attaque
11. Avance

### Décisions

| Élément BLv2 | Statut | Note |
|---|---|---|
| Déclarer la cible avant de lancer | ✅ **Repris** | |
| Jet de combat = valeur de combat du profil | ✅ **Repris** | |
| Relances et modifications | 🔧 **Adapté** | Uniquement via règles spéciales du profil. Pas de mécanique générale de relance. |
| Engager les dés (Commit) pour capacités | 🔧 **Adapté** | Conservé pour les Couronnes. Terminologie "engager" retenue. |
| Ignorer les dégâts (step 5) | ❌ **Écarté** | Remplacé par [Tenace], [Armure X] et [Protection X] — plus lisible. Pas de défense passive générique. |
| Ignorer les retraites (step 7) | 🔧 **Adapté** | Conservé via la règle de soutien (unité amie dans la direction de retraite). |
| Ordre dégâts → retraites | ✅ **Repris** | Les dégâts sont résolus avant les retraites, jamais simultanément. |
| Gagner du Lore (step 9) | ⏳ **Différé** | Phase 2 |
| Contre-attaque (step 10) | ✅ **Repris** | Universelle. Conditions : adjacente, survivante, non en retraite. |
| Avance (step 11) | ✅ **Repris** | Universelle. |
| Une seule attaque par unité par tour | ✅ **Repris** | Sauf [Double Tir] |

---

## 5. Dés et résultats

### Tableau de correspondance BLv2 → BdVM

| Face BLv2 | Face BdVM | Statut | Note |
|---|---|---|---|
| Strike (§) — mêlée inconditionnelle | **Épées croisées** | ✅ **Repris** | Renommé |
| Cleave (£) — mêlée si non Faible | **Épée** | ✅ **Repris** | Logique identique |
| Pierce (¥) — distance | **Cible** | ✅ **Repris** | Renommé |
| Morale (¢) — retraite | **Drapeau** | ✅ **Repris** | |
| Heroic (¦) — déclencheur de capacité | **Couronne** | ✅ **Repris** | Couronne = capacité spéciale du profil uniquement |
| Lore (¤) — ressource magique | **Arcane** | ⏳ **Différé** | Arcane inactive en Phase 1.5. Activée en Phase 2 comme ressource de canalisation. |

> 🎲 **Note de design** Les rôles sont clairement séparés : Couronne = déclencheur de capacité active (≈ Heroic BLv2), Arcane = ressource lore/magie (≈ Lore BLv2). Pas de fusion entre les deux faces.

---

## 6. Moral et retraites

### Décisions

| Élément BLv2 | Statut | Note |
|---|---|---|
| 1 Drapeau = 1 hex de retraite | 🔧 **Adapté** | BdVM introduit une **valeur de Moral** : nombre de Drapeaux ignorés par attaque. Valeur par défaut : 1. |
| Direction opposée à l'attaquant | ✅ **Repris** | |
| Direction retraite tir (opposée à l'arête de LdV) | ✅ **Repris** | Description textuelle dans BdVM_Regles_Base |
| Soutien (unité amie dans direction) = retraite ignorée sans dégât | ✅ **Repris** | |
| Terrain infranchissable / bord plateau → 1 dégât par retraite non résolue | ✅ **Repris** | |
| Unité ennemie dans direction → 1 dégât | ✅ **Repris** | |
| Règle Faible — moral | 🔧 **Adapté** | Quand Faible : Moral baisse de 1. Une unité à Moral 1 tombe à 0 — chaque Drapeau force une retraite. |

> 🎲 **Note de design** La valeur de Moral remplace l'ancien seuil "2 Drapeaux = 1 retraite". Elle est modulable par le profil (unités d'élite à Moral 2+) et par les héros (un héros ajoute sa valeur de commandement au Moral de l'unité qu'il accompagne). Exemple : Hallebardiers (Moral 1) + Général Empire (commandement 3) = Moral 4 — très difficile à faire reculer.

---

## 7. Contre-attaque et avance

### Décisions

| Élément BLv2 | Statut | Note |
|---|---|---|
| Contre-attaque universelle | ✅ **Repris** | |
| Contre-attaque optionnelle | ✅ **Repris** | |
| Contre-attaque ne déclenche pas de nouvelle contre-attaque | ✅ **Repris** | |
| Unité qui contre-attaque ne peut pas avancer | ✅ **Repris** | |
| Avance après élimination OU retraite forcée de la cible adjacente | ✅ **Repris** | |
| Une unité qui avance ne peut pas être contre-attaquée | ✅ **Repris** | |
| [Poursuite X] = avancer + attaque supplémentaire | ✅ **Repris** | Une seule utilisation par tour. L'unité doit passer par l'hex libéré. |
| [Férocité] = contre-attaque avant résolution des retraites | ✅ **Repris** | Repris tel quel de BLv2. Une unité avec [Férocité] qui force une retraite ne peut pas avancer ni utiliser [Poursuite]. |

---

## 8. Unités — Statuts et règles universelles

### Décisions

| Élément BLv2 | Statut | Note |
|---|---|---|
| Règle Faible — inactive sur Cleave/Épée | ✅ **Repris** | |
| Règle Faible — malus moral | 🔧 **Adapté** | BdVM : Moral baisse de 1 quand Faible (absent de BLv2) |
| Jetons de dégâts (Damage Tokens) | 🔧 **Adapté** | BdVM : PV par figurine avec jetons conservés entre les attaques. Plus flexible. Applicable à cavalerie, monstres, grandes créatures. |
| [Tenace] | 🔧 **Adapté** | Dernière figurine nécessite 2 touches dans la même attaque pour être retirée. Pas de conservation de touches entre attaques. |
| Unité = toutes les figurines d'un hex | ✅ **Repris** | |
| Impossible de scinder une unité | ✅ **Repris** | |

---

## 9. Terrain

### Décisions

| Terrain BLv2 | Statut | Note |
|---|---|---|
| Forêt — bloquant + arrêt immédiat | ✅ **Repris** | |
| Forêt — max de dés | 🔧 **Adapté** | BLv2 : max 2 dés. BdVM : max **4 dés** (before modifiers), cohérent avec le doublement des dés. S'applique à l'attaquant ET si la cible est en forêt. |
| Colline — bloquant LdV | ✅ **Repris** | |
| Colline — ignorent les unités pour LdV | ✅ **Repris** | |
| Colline — pas de coût de mouvement | ✅ **Repris** | Alignement BLv2 — pas de coût supplémentaire |
| Bâtiment — bloquant + arrêt | ✅ **Repris** | |
| Bâtiment — protection | 🔧 **Adapté** | BLv2 : ignore 1 dégât. BdVM : **[Protection X]** — valeur modulable selon le type de bâtiment (ruine = 1, bâtiment solide = 2, fortification = 3). |
| Tente de commandement | ❌ **Écarté** | Spécifique au mustering BLv2. Non applicable. |
| Eau infranchissable | ✅ **Repris** | |
| Gué — passable + arrêt immédiat | ✅ **Repris** | Emplacement défini par le scénario, pas de liberté de placement. |
| Pont — passable sans restriction | ✅ **Repris** | |
| Exception Vol | ⏳ **Différé** | Phase 2 |
| Exception infanterie légère en forêt | ❌ **Écarté** | Alignement BLv2 — pas d'exception |

> 🎲 **Note de design** [Protection X] est une règle générique extensible — elle pourra s'appliquer à des effets magiques défensifs en Phase 2.

---

## 10. Ligne de vue

### Décisions

| Élément BLv2 | Statut | Note |
|---|---|---|
| Centre-à-centre | ✅ **Repris** | |
| Hex attaquant et cible ne bloquent pas | ✅ **Repris** | |
| Terrain bloquant et unités bloquent la LdV | ✅ **Repris** | |
| Cas d'arête — décalage d'un côté, bloquée seulement si des deux côtés | ✅ **Repris** | Description textuelle dans BdVM_Regles_Base (pas de schéma) |
| Unités sur colline ignorent les autres unités (pas le terrain) | ✅ **Repris** | |

---

## 11. Règles spéciales d'unités (BLv2)

| Règle BLv2 | Statut | Équivalent BdVM / Note |
|---|---|---|
| **Double Shot** | ✅ **Repris** | [Double Tir] — Archers Empire |
| **Pursue X** | ✅ **Repris** | [Poursuite X] — 1 utilisation par tour |
| **Ferocity** | ✅ **Repris** | [Férocité] — repris tel quel |
| **Frenzy** | 🔧 **Adapté** | [Martyre] — même inspiration, déclencheur Couronne au lieu de Heroic |
| **Poison** | 🔧 **Adapté** | [Venin de Skink] — jeton Empoisonné permanent, plus simple et thématique |
| **Flying** | ⏳ **Différé** | Phase 2 |
| **Stun** | ⏳ **Différé** | Phase 2 — sorts et effets magiques |
| **Mobility X** | 🔧 **Adapté** | [Mobilité X] — attribué aux tirailleurs en remplacement de leur règle actuelle |
| **Flanking** | ⏳ **Différé** | Mis en réserve — Phase 3 selon les besoins des factions |
| **Rage** | ⏳ **Différé** | Mis en réserve — Phase 3 (Berserkers Chaos) |
| **Immovable X** | ❌ **Écarté** | Remplacé par soutien (universel) et valeur de Moral |
| **Massive** (sens BLv2) | ❌ **Écarté** | Non applicable — restrictions de terrain dans le profil si besoin |
| — | 🔧 **Nouveau** | [Armure X] — ignore X résultats Épée en mêlée uniquement |
| — | 🔧 **Nouveau** | [Protection X] — ignore X dégâts (terrain, fortifications) |
| — | 🔧 **Nouveau** | [Tenace] — 2 touches dans la même attaque pour éliminer la dernière figurine |
| — | 🔧 **Nouveau** | [Salve] — +2 dés à bout portant (Arquebusiers) |
| — | 🔧 **Nouveau** | [Pénétration] — relance des Cible, chaque nouvelle Cible = 1 touche supplémentaire (Arbalétriers) |
| — | 🔧 **Nouveau** | [Harcèlement] — mouvement complet après tir (Pistoliers) |

---

## 12. Cartes de commandement spécifiques (BLv2)

| Carte BLv2 | Statut | Note |
|---|---|---|
| Onslaught → Assaut d'infanterie | 🔧 **Adapté** | Déplacement 2 hex + combat. Validé Playtest #1. |
| Battle Cry | ⏳ **Différé** | Phase 3 — cartes de faction éventuelles |
| Overrun | ⏳ **Différé** | Phase 3 |
| Unstoppable | ⏳ **Différé** | Phase 3 |
| BattleLore → Arcanes de guerre | ⏳ **Différé** | Phase 2 — à revoir avec le système de magie |
| Rune Blade | ❌ **Écarté** | Trop complexe, lié à l'univers BLv2 |
| Runic Barrier | ⏳ **Différé** | Phase 2 — contre-magie |
| Portal | ❌ **Écarté** | Trop spécifique à BLv2 |

> 🎲 **Note de design** La question d'un deck de faction reste ouverte pour la Phase 3. Un deck commun bien calibré avec des règles spéciales portées par les profils donne déjà une identité forte à chaque faction sans créer d'asymétrie d'apprentissage défavorable aux nouveaux joueurs.

---

## 13. Système Lore (BLv2)

Tout différé Phase 2 sans exception :

| Élément | Statut |
|---|---|
| Accumulation de tokens via face Arcane | ⏳ **Différé** |
| Lore Step (3 options) | ⏳ **Différé** |
| Decks Lore par faction | ⏳ **Différé** |
| Dépense de tokens pour jouer des cartes | ⏳ **Différé** |

> 🎲 **Note de design** La correspondance est établie : face Arcane BdVM = face Lore ¤ BLv2 / face Couronne BdVM = face Heroic ¦ BLv2. La structure est prête pour la Phase 2.

---

## 14. Mustering / Construction d'armée (BLv2)

| Élément BLv2 | Statut | Note |
|---|---|---|
| Budget de points, deployment cards, leurres | ❌ **Écarté** | |
| Tente de commandement | ❌ **Écarté** | |
| Déploiement secret simultané | ❌ **Écarté** | Remplacé par déploiement alterné |
| Army Cards | 🔧 **Adapté** | Équivalent : listes d'armées par scénario. En Phase 3 : listes standardisées par faction avec valeurs en points pour parties libres. Chaque unité et chaque héros aura une valeur en points. |

---

## 15. Scénarios et mise en place (BLv2)

| Élément BLv2 | Statut | Note |
|---|---|---|
| Terrain défini par le scénario | ✅ **Repris** | |
| Indicateur d'initiative (premier joueur) | ✅ **Repris** | |
| Conditions de victoire asymétriques | 🔧 **Adapté** | BdVM vise des scénarios narratifs avec objectifs asymétriques + médailles objectif |
| Déploiement simultané secret | ❌ **Écarté** | |
| Choix du scénario parmi 3 | ❌ **Écarté** | Scénario défini à l'avance |
| Déploiement alterné | 🔧 **Adapté** | 1 unité par tour, ordre défini dans le scénario |
| Placement des gués | 🔧 **Adapté** | Emplacements définis par le scénario — pas de liberté de placement |

---

## 16. Règles optionnelles (BLv2)

| Élément | Statut |
|---|---|
| Mains de départ fixes | ❌ **Écarté** |
| Campagne | ⏳ **Différé** Phase 3/4 |
| Multiples copies du jeu | ❌ **Écarté** |

---

## 17. Synthèse et décisions

### Ce qui est entièrement repris de BLv2

Structure de la partie, séquence de combat, contre-attaque et avance universelles, [Poursuite X], [Férocité], [Double Tir], règle Faible, dés (Épées croisées / Épée / Cible / Drapeau / Couronne), moral et retraites, terrain (forêt / colline / eau / gué / pont), ligne de vue.

### Ce qui est adapté

- **Valeur de Moral** : remplace le seuil de Drapeaux. Modulable par profil et par héros.
- **PV par figurine** : jetons conservés entre attaques (cavalerie, monstres).
- **[Tenace]** : 2 touches dans la même attaque, sans conservation.
- **Forêt** : max 4 dés (before modifiers) au lieu de 2 — cohérent avec doublement des dés BdVM.
- **[Protection X]** : générique et modulable, remplace "ignore 1 dégât" fixe de BLv2.
- **[Armure X]** : ignore X résultats Épée en mêlée uniquement.
- **[Mobilité X]** : attribué aux tirailleurs, remplace leur règle actuelle.
- **Couronne / Arcane** : rôles clairement séparés (capacité / lore).
- **Valeur de commandement** : fixe à 4 en Phase 1.5, modulée par les héros en Phase 2+.

### Ce qui est écarté

Mustering, deployment cards, leurres, tente de commandement, déploiement secret, [Immovable], [Massive] (sens BLv2), Rune Blade, Portal, règles optionnelles.

### Ce qui est différé (Phase 2+)

Système Lore complet, face Arcane active, [Flying], [Stun], cartes Lore spécifiques, campagne, [Flanking], [Rage].

### Nouvelles règles introduites par BdVM

[Armure X], [Protection X], [Tenace], [Salve], [Pénétration], [Harcèlement], [Venin de Skink], [Martyre], [Mobilité X], Valeur de Moral, système de héros et valeur de commandement.

---

*Version : 1.1 — Phase 1.5 — 2026-04-27.*
*Revue complète effectuée le 2026-04-27. Tous les points ouverts tranchés.*
*Document prêt à archiver dans `00 - META/`.*
