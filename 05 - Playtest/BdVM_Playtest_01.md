---
projet: "Batailles du Vieux Monde"
type: "playtest"
numero: "01"
phase: 1
scenario: "La Passe des Collines Grises"
factions_testees: ["Empire", "Hommes-Lézards"]
date: "2026-04-24"
statut: "clôturé"
tags: [BdVM, type/playtest, phase/1, statut/clôturé]
---

# Playtest #01 — 24/04/2026

> 🔗 **Voir aussi** [[Document de cadrage]] — [[BdVM_cloture_phase1]] — [[BdVM_Playtest1_scenario]]

---

## Contexte

| Paramètre | Valeur |
|---|---|
| Scénario joué | La Passe des Collines Grises |
| Factions en présence | Empire (Nord) vs Hommes-Lézards (Sud) |
| Format | Escarmouche — 10 × 7 hexagones |
| Seuil de victoire | 4 points |
| Durée de la partie | Non mesurée |
| Participants | Solo (les deux factions jouées par le même joueur) |
| Résultat | Victoire des Hommes-Lézards — 4 à 1 |

**Objectif du playtest :** Valider la fluidité du système de base (mouvement, combat, commandement, terrain) avec les deux factions de Phase 1. Observer l'équilibre tir Empire / mêlée Hommes-Lézards, et tester les règles [Massif], [Intrépide], [Rechargement] et le terrain surélevé.

---

## Déroulement

La partie s'est terminée normalement — les Hommes-Lézards ont atteint le seuil de 4 points en premier. La victoire était nette et acquise avant la fin : l'Empire n'avait plus d'issue réaliste pour renverser la situation. Les Hommes-Lézards ont dominé la partie de bout en bout, leur ligne de mêlée [Massif] s'avérant structurellement trop résistante face au tir Empire.

---

## Problèmes identifiés

| # | Règle concernée | Description du problème | Gravité |
|---|---|---|---|
| 1 | Effectifs — socles 20 mm | 8 figurines par unité sur socles 20 mm : trop encombré sur un plateau 10×7. Lisibilité et placement difficiles. | Bloquant |
| 2 | Effectifs — socles 25 mm | 6 figurines par unité sur socles 25 mm : même problème d'encombrement. | Bloquant |
| 3 | [Massif] | Ignorer la première touche de chaque attaque reçue s'avère trop puissant sur 4 unités HL sur 6. Chaque échange commence avec un dé "perdu" pour l'Empire. | Bloquant |
| 4 | [Intrépide] | La règle n'a pas fonctionné — ni la contre-attaque conditionnelle ni l'immunité partielle aux Drapeaux n'ont créé de moments de jeu intéressants. La condition d'adjacence (2 unités amies) était difficile à atteindre en Escarmouche. | Bloquant |
| 5 | [Rechargement] | Le marqueur physique à gérer tour par tour sur 3 unités Empire est fastidieux. Génère une charge mentale disproportionnée sans créer de décisions intéressantes. | Gênant |
| 6 | Faces de dés — Poing | Les conditions d'application du Poing par profil (vs infanterie, vs cavalerie, vs tous) créent de la complexité sans apporter de richesse tactique suffisante. | Gênant |
| 7 | Assaut d'infanterie | La carte ne mentionne pas explicitement que les unités peuvent se déplacer de 2 hexagones et combattre en mêlée. Ambiguïté à table. | Mineur |
| 8 | Bonus offensifs (+1 dé) | Avec le système de dés actuel, +1 dé représente une probabilité de touche trop faible pour être significatif. | Mineur |

---

## Points positifs

- La structure en 5 étapes du tour (carte → activation → mouvement → combat → fin de tour) s'est enchaînée naturellement, sans friction.
- Le système de sections et de cartes de commandement crée bien la tension tactique attendue — les choix d'activation sont significatifs.
- Le terrain surélevé a été disputé et le différentiel 6 dés / 4 dés a créé des moments de décision intéressants.
- Le seuil de victoire à 4 points est adapté au roster de 6 unités par camp en format Escarmouche.
- Le déploiement alterné a bien fonctionné et sera à formaliser dans les règles de base.

---

## Décisions prises suite au playtest

### Composants

| Règle modifiée | Ancienne version | Nouvelle version | Justification |
|---|---|---|---|
| Effectifs infanterie 20 mm | 8 figurines | 6 figurines | Encombrement trop important sur plateau 10×7 |
| Effectifs infanterie 25 mm | 6 figurines | 4 figurines | Même raison |
| Effectifs cavalerie | 3 figurines, 1 PV | 3 figurines, 2 PV cumulés dans le tour | Alignement BattleLore V2 — lisibilité plateau |

### Dés — refonte complète

| Face | Ancienne version | Nouvelle version |
|---|---|---|
| Épée | 1 touche (mêlée) | 1 touche mêlée — sauf si l'unité est **Faible** (dernière figurine) |
| Arc | 1 touche (tir) | Supprimée — remplacée par **Cible** |
| **Cible** (nouvelle) | — | 1 touche, toute unité à distance |
| Poing | 1 touche conditionnelle | **Supprimée** |
| **Épées croisées** (nouvelle) | — | 1 touche inconditionnelle, toute unité de mêlée |
| Drapeau | 1 retraite | Inchangé — sauf unité Faible : 1 Drapeau = 1 retraite |
| Couronne | Capacité spéciale | Inchangé |
| Arcane | Échec (Phase 2) | Inchangé |

### Règles de combat

| Règle modifiée | Ancienne version | Nouvelle version | Justification |
|---|---|---|---|
| Contre-attaque | Conditionnelle ([Intrépide]) | **Universelle** — toute unité survivante non en retraite peut contre-attaquer | Alignement BattleLore V2 |
| Avance | Non définie | **Universelle** — après élimination ou retraite forcée d'une cible adjacente, l'attaquant peut avancer dans l'hex libéré | Alignement BattleLore V2 |
| Avance et contre-attaque | — | Une unité qui avance **ne peut pas être contre-attaquée** | Cohérence avec BattleLore V2 |
| Unité Faible | Non définie | Dernière figurine restante : ne touche plus sur Épée/Cible ; 1 Drapeau = 1 hexagone de retraite | Crée une dynamique de fin de vie lisible |

### Règles spéciales — suppressions

| Règle | Décision |
|---|---|
| [Massif] | **Supprimé** — remplacé par [Tenace] |
| [Intrépide] | **Supprimé** — la contre-attaque devient universelle |
| [Rechargement] | **Supprimé** — remplacé par des règles positives par unité |
| [Colosse] | **Supprimé** — remplacé par un système de PV par figurine |

### Règles spéciales — ajouts et modifications

| Règle | Définition |
|---|---|
| **[Tenace]** | La dernière figurine de l'unité nécessite 2 touches pour être retirée. Les touches se cumulent dans le tour ; une touche isolée en fin de tour est ignorée. |
| **[Venin de Skink]** | Couronne → pose un jeton **Empoisonné** sur la cible au lieu d'une touche immédiate. Tant qu'une unité est Empoisonnée, chaque Couronne obtenue lors d'une attaque contre elle inflige 1 touche supplémentaire. Jeton permanent jusqu'à élimination. |
| **[Double Tir]** (Archers) | Si l'unité n'a pas bougé ce tour, elle peut effectuer une seconde attaque. |
| **[Salve]** (Arquebusiers) | +2 dés si la cible est adjacente (à bout portant). |
| **[Pénétration]** (Arbalétriers) | Chaque dé ayant obtenu Cible est relancé. Chaque nouvelle Cible inflige une touche supplémentaire. Relance ad vitam — la probabilité (1/6) fait office de limite naturelle. |
| **[Harcèlement]** (Pistoliers) | Les Pistoliers peuvent se déplacer **après** avoir tiré (mouvement complet de 4 hexagones). |

### Profils modifiés

| Unité | Modification |
|---|---|
| Saurus à l'Épée, à la Lance, Gardes du Temple | [Massif] → [Tenace] |
| Gardes du Temple | [Intrépide] supprimé |
| Grandes Épées | [Intrépide] supprimé |
| Skinks | Effectif 6 fig. · 2 dés · portée 3 hex · sans portée minimale · [Venin de Skink] remplace [Poison] |
| Kroxigors | [Colosse] supprimé → 3 PV par figurine · Faible à la perte de la 1re figurine |
| Salamandres | [Massif] supprimé · Composition : 1 Salamandre + 3 Skinks coureurs (4 fig. total) · Les Skinks sont retirés en premier · La Salamandre seule ne peut plus se déplacer mais peut toujours attaquer |
| Saurus sur Sang-froid | Cavalerie lourde → **Cavalerie moyenne** (3 hex et combat) · Ajout [Poursuite 2] |
| Chevaliers de l'Empire | Ajout [Poursuite 1] |
| Hallebardiers | Règle Hallebarde (bonus contre-attaque) à réviser — [Intrépide] supprimé |

### Cartes de commandement

| Carte | Modification |
|---|---|
| Assaut d'infanterie | Ajout explicite : les unités activées peuvent se déplacer de 2 hexagones et combattre en mêlée |
| Charge de cavalerie | Bonus offensif : +1 dé → **+2 dés** |
| Ordre direct | Bonus offensif : +1 dé → **+2 dés** |

### Nouvelles règles générales

| Règle | Définition |
|---|---|
| **Avance** | Après avoir éliminé ou forcé la retraite d'une cible adjacente, l'attaquant peut avancer dans l'hex libéré. Une unité qui avance ne peut pas être contre-attaquée. |
| **[Poursuite X]** | Quand une unité avec [Poursuite X] peut avancer, elle peut choisir d'avancer de X hexagones et effectuer une attaque supplémentaire. Elle doit passer par l'hex libéré. |
| **PV par figurine** | Certaines unités nécessitent plusieurs touches pour perdre une figurine. Les touches se cumulent dans le tour ; les touches non converties en fin de tour sont ignorées. L'unité est Faible dès qu'il ne lui reste qu'une figurine. |
| **Déploiement alterné** | À formaliser dans `BdVM_Regles_Base` §3 — les deux joueurs déploient en alternance, à commencer par le joueur désigné dans le scénario. |

> 🔄 **Rappel** : Reporter chaque modification dans le document de règle concerné avec le bloc `🔄 Modifié après playtest — 2026-04-24 | Playtest #01`.

---

## Questions ouvertes pour le Playtest #2

- **[Tenace] sur les unités à PV multiples** : confirmer que la règle Faible s'applique bien à la dernière figurine des Kroxigors (après perte de leur 1re figurine à 3 PV).
- **Cavalerie moyenne** : valider que 3 hexagones et combat est bien calibré pour les Saurus sur Sang-froid.
- **[Poursuite]** : vérifier que Poursuite 2 (Saurus sur Sang-froid) n'est pas trop dominant sur un plateau Escarmouche.
- **[Pénétration]** : vérifier que la relance ad vitam sur Cible ne crée pas de pics de dégâts trop importants sur les Arbalétriers.
- **[Venin de Skink]** : vérifier que le jeton Empoisonné permanent ne déséquilibre pas la faction HL sur la durée.
- **[Salve] à bout portant** : vérifier que les Arquebusiers ne sont pas trop puissants quand ils sont collés à une unité ennemie.
- **Salamandres — composition mixte** : valider que la mécanique 1 Salamandre + 3 Skinks est lisible à table et crée bien la dynamique de dégradation attendue.
- **Unité mixte Skinks + Kroxigor** : piste à explorer en Phase 2.
- **[Frénésie] + [Martyre]** : non testés dans ce scénario — à inclure dans le Playtest #2.
- **Terrain boisé et infanterie légère** : point ouvert `BdVM_Terrain` §3.1 — non tranché.
- **Coût de mouvement terrain surélevé** : point ouvert `BdVM_Terrain` §4.1 — non tranché.
- **Valeur de commandement** : point ouvert `BdVM_Regles_Base` §3 — non tranché.

---

*Version : 1.0 — 2026-04-24. Compte-rendu rédigé à l'issue du débrief Playtest #1.*
