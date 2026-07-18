---
projet: "Batailles du Vieux Monde"
type: "faction"
phase: 1.6
statut: "à-tester"
date_maj: "2026-05-23"
tags: [BdVM, "type/faction", "phase/1.6", "statut/à-tester"]
---

# Batailles du Vieux Monde — Profils d'unités : Hommes-Lézards

> Ce document recense les profils d'unités de la faction Hommes-Lézards pour la Phase 1.6. La magie des Slanns, le Slann Mage-Prêtre et le Stégadon + Machine des Dieux sont réservés à la Phase 2.
> Aligné sur **BdVM_Regles_Base v4.1** et **BdVM_Regles_Speciales v2.1**.
> **Toutes les unités de la faction sont [Immunisées au poison].**

> 🔄 **Réécriture complète — 2026-05-23 | Phase 1.6 Étape 2**
> - Nouvelle présentation des profils : type · mode d'attaque · tableau Mouvement / Attaque / PV
> - Suppression de [Ligne] — absorbé par la règle intrinsèque du type Infanterie
> - Suppression de [Tenace] sur toutes les unités — remplacé par [Massif] sur l'infanterie Saurus
> - Suppression de [Cavalerie] — absorbé par le type Cavalerie
> - Kroxigors : passage au type Créature avec [Meute 2], mouvement porté à 2
> - Saurus sur Sang-froid : suppression de [Tenace], attaque ramenée à 3 dés
> - Salamandres : passage au type Artillerie avec [Bête incontrôlable], attaque portée à 3 dés
> - Ajout du Stégadon et du Saurus sur Carnosaure

> 🔗 **Voir aussi** [[BdVM_Regles_Base]] — [[BdVM_Regles_Speciales]] — [[BdVM_Empire_Unites]]

---

## Table des matières

1. [[#Conventions de lecture]]
2. [[#1. Saurus à l'Épée]]
3. [[#2. Saurus à la Lance]]
4. [[#3. Gardes du Temple]]
5. [[#4. Kroxigors]]
6. [[#5. Skinks]]
7. [[#6. Salamandres]]
8. [[#7. Saurus sur Sang-froid]]
9. [[#8. Stégadon]]
10. [[#9. Saurus sur Carnosaure]]
11. [[#Récapitulatif]]
12. [[#Règles spéciales utilisées]]
13. [[#Notes de design]]

---

## Conventions de lecture

### Présentation des profils

Chaque profil indique :

- **Le type** et **le mode d'attaque** (Mêlée ou Distance) — sur la ligne sous le nom.
- **Trois caractéristiques** dans un tableau : Mouvement, Attaque, PV.
- **Les règles spéciales** propres à l'unité.

Pour les unités à Distance, la valeur d'Attaque est suivie de la portée entre parenthèses. Exemple : `2 (1–3)` signifie 2 dés à portée 1, et la règle [Arme à feu] s'applique si l'unité la possède.

### Types d'unités et règles intrinsèques

| Type | Règle intrinsèque |
|---|---|
| **Infanterie** | Épées croisées et Cible → **2 PV** perdus chez la cible |
| **Cavalerie** | Aucune — 1 touche = 1 PV |
| **Créature** | Jamais Faible (sauf exception explicite dans le profil) |
| **Artillerie** | Jamais Faible · Servants éliminés en premier |

> 🔗 **Voir aussi** [[BdVM_Regles_Base]] §2 — Types d'unités

### Unité Faible

Une unité est **Faible** lorsqu'il ne lui reste **qu'1 PV** (dernière figurine). À l'état Faible, la face Épée n'inflige plus de touche lors de ses attaques.

Les Créatures et l'Artillerie ne sont **jamais** Faibles (sauf exception explicite).

> 🔗 **Voir aussi** [[BdVM_Regles_Base]] §2.2

### Immunité au poison

Toutes les unités Hommes-Lézards sont **[Immunisées au poison]** : elles ignorent les touches supplémentaires générées par la règle **[Poison]**, quelle qu'en soit la source.

---

## 1. Saurus à l'Épée

*Guerriers reptiliens nés pour le combat, les Saurus à l'Épée sont des soldats de ligne d'une résistance hors du commun. Leur constitution surnaturelle leur permet d'encaisser les blessures qui abattraient plusieurs hommes sans fléchir.*

**Infanterie · Mêlée**

| Mouvement | Attaque | PV |
|---|---|---|
| 2 | 3 | 4 |

Règles spéciales : [Massif], [Immunisé au poison]

**[Massif] :** les attaques reçues par cette unité n'infligent qu'**1 PV par touche**, quelle que soit la source. La règle intrinsèque du type Infanterie ne s'applique pas contre cette unité.

> 💡 **Exemple de jeu**
> Des Hallebardiers [Arme Lourde 1] attaquent des Saurus à l'Épée : 3 dés, 1 relance possible. Résultat final : Épées croisées, Épée → 2 touches. [Massif] : 2 touches = **2 PV perdus** (au lieu de 4 sans [Massif]).

---

## 2. Saurus à la Lance

*Formés à recevoir les charges de cavalerie, les Saurus à la Lance combinent la résistance naturelle des reptiles guerriers à une technique anti-charge éprouvée. Leurs longues lances transforment chaque charge ennemie en piège mortel.*

**Infanterie · Mêlée**

| Mouvement | Attaque | PV |
|---|---|---|
| 2 | 3 | 4 |

Règles spéciales : [Massif], [Réception de charge], [Immunisé au poison]

**[Massif] :** voir Saurus à l'Épée.

**[Réception de charge] :** lorsque les Saurus à la Lance effectuent une **contre-attaque** contre une unité qui s'est **déplacée ce tour**, ils lancent **1 dé supplémentaire** (4 dés au total).

> 💡 **Exemple de jeu**
> Des Chevaliers de l'Empire avancent de 3 hexagones et chargent les Saurus à la Lance. Les Saurus contre-attaquent : 3 + 1 = **4 dés** grâce à [Réception de charge]. Si les Chevaliers n'avaient pas bougé, les Saurus n'auraient que 3 dés.

---

## 3. Gardes du Temple

*Guerriers d'élite voués à la protection des Slanns, les Gardes du Temple sont les combattants les plus redoutables que les cités-temples puissent aligner. Leur dévotion totale et leur entraînement sans relâche en font des adversaires terrifiants au corps à corps.*

**Infanterie · Mêlée**

| Mouvement | Attaque | PV |
|---|---|---|
| 1 | 4 | 4 |

Règles spéciales : [Massif], [Arme Lourde 1], [Immunisé au poison]

**[Massif] :** voir Saurus à l'Épée.

**[Arme Lourde 1] :** après le lancer de dés, le joueur peut **relancer 1 dé** de son choix.

> 💡 **Exemple de jeu**
> Des Gardes du Temple attaquent des Chevaliers [Armure 1] adjacents : 4 dés. Résultat : Épées croisées, Épée, Drapeau, Arcane. [Armure 1] retire l'Épée → 1 touche (Épées croisées). Le joueur relance l'Arcane ([Arme Lourde 1]) → obtient Épées croisées : 2 touches au final. Règle intrinsèque Infanterie : 2 touches = 4 PV perdus chez les Chevaliers.

---

## 4. Kroxigors

*Cousins géants des Saurus, les Kroxigors sont des machines de destruction naturelles. Ils se battent en binômes implacables — chaque individu encaisse des blessures qui abattraient plusieurs hommes, et le dernier d'entre eux continue de se battre jusqu'au bout.*

**Créature · Mêlée**

| Mouvement | Attaque | PV |
|---|---|---|
| 2 | 4 | 4 |

Faible à : 1 figurine restante (2 PV)

Règles spéciales : [Meute 2], [Immunisé au poison]

**[Meute 2] :** cette unité est composée de **2 figurines de 2 PV chacune**. Retirer une figurine dès qu'elle atteint 0 PV. L'unité est **Faible** quand il ne reste qu'une seule figurine. *(Exception à la règle "jamais Faible" des Créatures.)*

> 💡 **Exemple de jeu**
> Les Kroxigors reçoivent 3 touches : les 2 premiers PV éliminent la première figurine, le 3e PV est appliqué à la seconde. Il reste 1 Kroxigor à 1 PV → l'unité est Faible. La face Épée n'inflige plus de touche lors de ses attaques.

---

## 5. Skinks

*Agiles et rusés, les Skinks harcèlent l'ennemi depuis les franges du champ de bataille. Armés de sarbacanes empoisonnées, ils sont trop fragiles pour tenir une ligne de front — mais leurs projectiles venimeux peuvent faire chanceler les unités les plus solides.*

**Infanterie · Distance**

| Mouvement | Attaque | PV |
|---|---|---|
| 2 | 2 (1–3) | 6 |

Règles spéciales : [Poison], [Immunisé au poison], [Terrain favori : Boisé]

**[Poison] :** lorsque les Skinks effectuent une attaque, chaque face **Couronne** obtenue inflige **1 touche supplémentaire**, sauf contre les unités **[Immunisées au poison]**.

> 💡 **Exemple de jeu**
> Les Skinks tirent sur des Hallebardiers à 2 hexagones : 2 dés. Résultat : Cible, Couronne → 2 touches (Cible + 1 via [Poison]). Règle intrinsèque Infanterie : 2 touches = **4 PV perdus** chez les Hallebardiers.
> Contre des Saurus à l'Épée alliés (scénario) : la Couronne n'a aucun effet ([Immunisé au poison]) — 1 touche seulement, soit 1 PV perdu ([Massif]).

---

## 6. Salamandres

*La Salamandre est une créature de guerre crachant une substance enflammée dévastatrice. Elle est guidée et alimentée par trois coureurs Skinks qui dirigent l'animal vers ses cibles. Sans ses servants, la bête devient incontrôlable — dangereuse mais incapable de se repositionner.*

**Artillerie · Distance**

| Mouvement | Attaque | PV |
|---|---|---|
| 2 | 3 (1–3) | 3 |

Règles spéciales : [Souffle de feu], [Bête incontrôlable], [Immunisé au poison]

*Représentée par 1 Salamandre + 3 servants Skinks. Les servants sont éliminés en premier (1 servant par touche reçue). Une fois tous les servants éliminés, [Bête incontrôlable] s'active.*

**[Souffle de feu] :** lorsque les Salamandres effectuent une attaque, chaque face **Couronne** obtenue inflige **1 touche supplémentaire**, sauf contre les unités **[Immunisées au feu]**.

**[Bête incontrôlable] :** lorsque tous les servants sont éliminés, la Salamandre **ne peut plus se déplacer** mais peut encore attaquer normalement. Une **touche supplémentaire** l'élimine définitivement.

> 💡 **Exemple de jeu**
> Les Salamandres tirent sur des Grandes Épées à 2 hexagones : 3 dés. Résultat : Cible, Couronne, Drapeau → 2 touches (Cible + 1 via [Souffle de feu]). Règle intrinsèque Infanterie : 2 touches = **4 PV perdus** chez les Grandes Épées.
> Les Salamandres reçoivent ensuite 3 touches : les 3 servants sont éliminés. [Bête incontrôlable] s'active — la Salamandre ne peut plus bouger mais tire encore à 3 dés. L'adversaire lui inflige 1 touche → elle est éliminée.

> 🎲 **Note de design** L'ordre de pertes (servants en premier) crée une décision tactique pour l'adversaire : faut-il concentrer les attaques pour neutraliser les servants rapidement, ou disperser les tirs ? La Salamandre seule ([Bête incontrôlable]) reste dangereuse grâce à [Souffle de feu] mais devient une cible fixe vulnérable.

---

## 7. Saurus sur Sang-froid

*Montés sur de puissants reptiles Sang-froid, les Guerriers Saurus constituent la cavalerie lourde des Hommes-Lézards. Combinant la résistance des Saurus à la mobilité de leur monture, ils frappent fort et s'acharnent sur leur proie avec une implacable ténacité.*

**Cavalerie · Mêlée**

| Mouvement | Attaque | PV |
|---|---|---|
| 3 | 3 | 3 |

Règles spéciales : [Poursuite 2], [Immunisé au poison]

**[Poursuite 2] :** après avoir éliminé une unité ennemie adjacente ou l'avoir forcée à retraiter, les Saurus sur Sang-froid peuvent, à la place de l'avance normale, se déplacer de **jusqu'à 2 hexagones** et effectuer **une attaque supplémentaire** contre une unité adjacente à leur nouvelle position.

> 💡 **Exemple de jeu**
> Des Saurus sur Sang-froid éliminent des Épéistes adjacents. Ils se déplacent de 2 hexagones ([Poursuite 2]) et attaquent des Archers voisins : 3 dés supplémentaires.

---

## 8. Stégadon

*Dinosaure de guerre colossal, le Stégadon est une force de la nature impossible à arrêter. Sa masse écrase tout sur son passage lors d'une charge, et les Skinks perchés dans son howdah harcèlent l'ennemi par-dessus les rangs adverses.*

**Créature · Mêlée**

| Mouvement | Attaque | PV |
|---|---|---|
| 2 | 3 | 4 |

Règles spéciales : [Inébranlable 1], [Charge écrasante], [Howdah], [Immunisé au poison]

**[Inébranlable 1] :** le Stégadon ignore **1 résultat de retraite** par attaque reçue, quelle qu'en soit la source.

**[Charge écrasante] :** si le Stégadon s'est **déplacé ce tour** avant d'attaquer, chaque résultat **Couronne** inflige **1 touche supplémentaire**. Cette touche peut être appliquée à n'importe quelle unité **adjacente au Stégadon**, pas nécessairement la cible de l'attaque.

**[Howdah] :** le Stégadon peut effectuer une **attaque à distance en plus de son attaque de mêlée** — **2 dés**, portée **1 à 3 hexagones**, avec la règle **[Poison]**.

> 💡 **Exemple de jeu**
> Le Stégadon se déplace de 2 hexagones et charge des Épéistes adjacents : 3 dés. Résultat : Épées croisées, Couronne, Drapeau. [Charge écrasante] : la Couronne inflige 1 touche supplémentaire — le joueur choisit de l'appliquer à des Lanciers adjacents au Stégadon. [Inébranlable 1] ignore le Drapeau. Résultat final : 1 touche sur les Épéistes (2 PV, règle intrinsèque Infanterie) + 1 touche sur les Lanciers (2 PV).
> Le Stégadon tire ensuite avec son [Howdah] sur des Archers à 2 hexagones : 2 dés avec [Poison].

> ⚠️ **Note de design — à évaluer au Playtest** : 4 PV + [Inébranlable 1] + [Charge écrasante] + [Howdah] constituent un profil très complet. Ajuster le coût en points si l'unité s'avère dominante.

---

## 9. Saurus sur Carnosaure

*Prédateur de guerre ultime des Hommes-Lézards, le Saurus sur Carnosaure est plus rapide et plus agressif que le Stégadon. Sa charge dévaste les lignes ennemies, et sa vitesse lui permet d'enchaîner les attaques sur des cibles affaiblies.*

**Créature · Mêlée**

| Mouvement | Attaque | PV |
|---|---|---|
| 3 | 4 | 4 |

Règles spéciales : [Charge écrasante], [Poursuite 2], [Immunisé au poison]

**[Charge écrasante] :** si le Saurus sur Carnosaure s'est **déplacé ce tour** avant d'attaquer, chaque résultat **Couronne** inflige **1 touche supplémentaire**. Cette touche peut être appliquée à n'importe quelle unité **adjacente au Carnosaure**, pas nécessairement la cible de l'attaque.

**[Poursuite 2] :** après avoir éliminé une unité ennemie adjacente ou l'avoir forcée à retraiter, le Saurus sur Carnosaure peut, à la place de l'avance normale, se déplacer de **jusqu'à 2 hexagones** et effectuer **une attaque supplémentaire** contre une unité adjacente à sa nouvelle position.

> 💡 **Exemple de jeu**
> Le Saurus sur Carnosaure se déplace de 2 hexagones et charge des Hallebardiers adjacents : 4 dés. Résultat : Épées croisées, Épées croisées, Couronne, Drapeau. [Charge écrasante] : la Couronne inflige 1 touche sur des Lanciers adjacents (2 PV, règle intrinsèque Infanterie). Les Hallebardiers perdent 4 PV (2 × Épées croisées × 2 PV) → ils sont éliminés. [Poursuite 2] : le Carnosaure se déplace de 2 hexagones et attaque une nouvelle unité : 4 dés supplémentaires.

> ⚠️ **Note de design — à évaluer au Playtest** : 4 PV + Mouvement 3 + 4 dés + [Charge écrasante] + [Poursuite 2] en font l'unité offensive la plus puissante des Hommes-Lézards. Coût en points élevé à prévoir.

---

## Récapitulatif

| Unité | Type | Mvt | Attaque | PV | Règles spéciales |
|---|---|---|---|---|---|
| Saurus à l'Épée | Infanterie · Mêlée | 2 | 3 | 4 | [Massif], [Immunisé au poison] |
| Saurus à la Lance | Infanterie · Mêlée | 2 | 3 | 4 | [Massif], [Réception de charge], [Immunisé au poison] |
| Gardes du Temple | Infanterie · Mêlée | 1 | 4 | 4 | [Massif], [Arme Lourde 1], [Immunisé au poison] |
| Kroxigors | Créature · Mêlée | 2 | 4 | 4 | [Meute 2], [Immunisé au poison] |
| Skinks | Infanterie · Distance | 2 | 2 (1–3) | 6 | [Poison], [Immunisé au poison] |
| Salamandres | Artillerie · Distance | 2 | 3 (1–3) | 3 | [Souffle de feu], [Bête incontrôlable], [Immunisé au poison] |
| Saurus sur Sang-froid | Cavalerie · Mêlée | 3 | 3 | 3 | [Poursuite 2], [Immunisé au poison] |
| Stégadon | Créature · Mêlée | 2 | 3 | 4 | [Inébranlable 1], [Charge écrasante], [Howdah], [Immunisé au poison] |
| Saurus sur Carnosaure | Créature · Mêlée | 3 | 4 | 4 | [Charge écrasante], [Poursuite 2], [Immunisé au poison] |

---

## Règles spéciales utilisées

| Règle                     | Unités concernées                                    | Résumé                                                          |
| ------------------------- | ---------------------------------------------------- | --------------------------------------------------------------- |
| **[Arme Lourde 1]**       | Gardes du Temple                                     | Relancer 1 dé après le lancer                                   |
| **[Bête incontrôlable]**  | Salamandres                                          | Sans servants : ne bouge plus, 1 touche pour éliminer           |
| **[Charge écrasante]**    | Stégadon, Saurus sur Carnosaure                      | Si déplacé ce tour : Couronne → touche sur unité adjacente      |
| **[Howdah]**              | Stégadon                                             | Attaque à distance en plus de la mêlée — 2 dés (1–3) + [Poison] |
| **[Immunisé au poison]**  | Toutes                                               | Ignore les touches générées par [Poison]                        |
| **[Inébranlable 1]**      | Stégadon                                             | Ignore 1 résultat de retraite par attaque reçue                 |
| **[Massif]**              | Saurus à l'Épée, Saurus à la Lance, Gardes du Temple | 1 PV perdu par touche — annule la règle intrinsèque Infanterie  |
| **[Meute 2]**             | Kroxigors                                            | 2 figurines de 2 PV chacune — Faible à 1 figurine restante      |
| **[Poison]**              | Skinks, via [Howdah] (Stégadon)                      | Couronne → 1 touche sup. (sauf [Immunisé au poison])            |
| **[Poursuite 2]**         | Saurus sur Sang-froid, Saurus sur Carnosaure         | Alternative à l'avance : jusqu'à 2 hex + attaque supplémentaire |
| **[Réception de charge]** | Saurus à la Lance                                    | +1 dés en contre-attaque si l'adversaire s'est déplacé ce tour  |
| **[Souffle de feu]**      | Salamandres                                          | Couronne → 1 touche sup. (sauf [Immunisé au feu])               |

---

## Notes de design

### Identité de faction — Les Hommes-Lézards

Les Hommes-Lézards sont une armée lente et massive qui frappe fort quand elle est engagée. À l'inverse de l'Empire, leur force réside dans la résistance et la puissance brute plutôt que dans la diversité.

- **Infanterie Saurus** : plus résistante que l'infanterie Empire grâce à [Massif] (4 PV, 1 touche = 1 PV), mais plus lente sur les élites (Gardes du Temple à Mouvement 1)
- **Créatures** : trois profils très différents — les Kroxigors sont tenaces ([Meute 2]), le Stégadon est polyvalent ([Charge écrasante] + [Howdah]), le Carnosaure est offensif ([Charge écrasante] + [Poursuite 2])
- **Tir** : limité aux Skinks ([Poison]) et aux Salamandres ([Souffle de feu]) — moins diversifié que l'Empire mais thématiquement distinctif
- **Cavalerie** : un seul profil (Saurus sur Sang-froid), plus modeste que les Chevaliers Empire (3 dés vs 4) mais avec [Poursuite 2]

### Immunité au poison — impact sur les affrontements miroir

Dans un scénario HL vs HL, [Poison] des Skinks est totalement neutralisé par [Immunisé au poison] universel. Les Skinks deviennent de simples unités de tir à 2 dés — leur intérêt tactique disparaît. À noter pour la conception des scénarios.

### Points ouverts pour le Playtest #3

- **Saurus à l'Épée / Saurus à la Lance / Gardes du Temple** : [Massif] remplace [Tenace] — observer si la résistance est suffisante (4 PV, 1 PV par touche) sans être excessive face à l'infanterie Empire (6 PV, 2 PV par touche Épées croisées/Cible).
- **Kroxigors** : Mouvement 2 + 4 dés + [Meute 2] — vérifier qu'ils s'engagent enfin sur le champ de bataille (problème observé au Playtest #2 avec Mouvement 1).
- **Stégadon** : première apparition en jeu — observer si [Charge écrasante] + [Howdah] crée des moments de jeu intéressants sans être surpuissant.
- **Saurus sur Carnosaure** : première apparition en jeu — surveiller l'enchaînement [Charge écrasante] + [Poursuite 2] qui peut potentiellement dévaster deux unités en un seul ordre.
- **Salamandres** : passage à 3 dés (vs 2 en v2.0) — observer si le [Souffle de feu] reste équilibré avec cette hausse offensive.

---

*Version : 4.0 — Phase 1.6 — 2026-05-23.*
*🔄 Réécriture complète. Nouvelle présentation des profils (type · mode · tableau). Suppression de [Ligne], [Tenace], [Cavalerie]. Remplacement par [Massif] sur l'infanterie Saurus. Kroxigors → Créature [Meute 2], Mouvement 2. Salamandres → Artillerie 3 dés + [Bête incontrôlable]. Saurus sur Sang-froid : attaque 3 dés, suppression [Tenace]. Ajout Stégadon et Saurus sur Carnosaure.*
*Remplace : BdVM_Hommes_Lezards_Unites v2.0 (2026-05-17).*
