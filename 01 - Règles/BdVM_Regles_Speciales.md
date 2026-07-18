---
projet: "Batailles du Vieux Monde"
type: "règles"
phase: 1.6
statut: "à-tester"
date_maj: "2026-05-30"
tags: [BdVM, "type/règles", "phase/1.6", "statut/à-tester"]
---

# Batailles du Vieux Monde — Règles spéciales

> **Objet de ce document :** Glossaire de référence de toutes les règles spéciales actives en Phase 1.6. Chaque règle est définie une seule fois ici ; les profils d'unités y renvoient.
> Aligné sur **BdVM_Regles_Base v4.1** et **BdVM_Terrain v3.0**.
> Ce document ne couvre pas les règles universelles (Faible, contre-attaque, avance, Poursuite générique) ni les règles intrinsèques des types d'unités (Infanterie, Cavalerie, Créature, Machine de guerre, Artillerie), qui sont définies dans [[BdVM_Regles_Base]].

> 🔄 **Mise à jour — 2026-05-30 | Phase 1.6 Étape 3**
> - Nouvelle règle **[Terrain favori : Boisé]** (D079) — annule toutes les restrictions de mouvement et de combat du terrain boisé. Attribuée aux Skinks (D080).
> - Mise à jour de l'index Hommes-Lézards (Skinks).
> - Mise à jour du récapitulatif alphabétique.

> 🔄 **Réécriture complète — 2026-05-23 | Phase 1.6 Étape 2**
> - Suppression de [Ligne], [Cavalerie], [Salve], [Frénésie] — absorbés par les types d'unités ou remplacés
> - Suppression de [Tenace] sur la majorité des unités — remplacé par [Massif] et les types d'unités
> - Nouvelle règle [Arme à feu] — remplace [Salve]
> - Nouvelle règle [Inébranlable X] (ex [Inamovible X] — traduction officielle BLv2 VF)
> - Nouvelle règle [Massif] — annule la règle intrinsèque Infanterie
> - Nouvelle règle [Meute X] — Kroxigors
> - Nouvelle règle [Rechargement] — remplace [Mise en batterie]
> - Nouvelle règle [Bête incontrôlable] — Salamandres
> - Nouvelle règle [Charge écrasante] — Stégadon, Saurus sur Carnosaure
> - Nouvelle règle [Howdah] — Stégadon
> - [Perforant X] reformulé : relance de dés (abandon de la réduction d'[Armure])
> - [Armure X] conservé tel quel (BLv2 standard — mêlée uniquement)

> 🔗 **Voir aussi** [[BdVM_Regles_Base]] — [[BdVM_Terrain]] — [[BdVM_Empire_Unites]] — [[BdVM_Hommes_Lezards_Unites]]

---

## Table des matières

1. [[#Conventions]]
2. [[#Règles défensives]]
   - [[#[Armure X]]]
   - [[#[Inébranlable X]]]
   - [[#[Immunisé au poison]]]
   - [[#[Immunisé au feu]]]
   - [[#[Massif]]]
   - [[#[Protection X]]]
3. [[#Règles offensives — Mêlée]]
   - [[#[Arme Lourde X]]]
   - [[#[Charge écrasante]]]
   - [[#[Férocité]]]
   - [[#[Martyre]]]
   - [[#[Réception de charge]]]
4. [[#Règles offensives — Distance]]
   - [[#[Arme à feu]]]
   - [[#[Bête incontrôlable]]]
   - [[#[Double Tir]]]
   - [[#[Howdah]]]
   - [[#[Perforant X]]]
   - [[#[Poison]]]
   - [[#[Souffle de feu]]]
5. [[#Règles de mouvement et de manœuvre]]
   - [[#[Meute X]]]
   - [[#[Mobilité X]]]
   - [[#[Poursuite X]]]
   - [[#[Rechargement]]]
   - [[#[Terrain favori : Boisé]]]
6. [[#Récapitulatif alphabétique]]
7. [[#Index par faction]]
8. [[#Règles différées — Phase 2+]]

---

## Conventions

### Notation

- **[Règle]** : nom entre crochets — standard dans tous les profils.
- **[Règle X]** : règle avec une valeur numérique (ex. [Armure 1], [Arme Lourde 2]).
- Les règles marquées ⏳ sont définies ici pour mémoire mais non actives en Phase 1.6.

### Règles intrinsèques des types d'unités

Les règles suivantes ne sont **pas** des règles spéciales — elles sont portées directement par le type d'unité et s'appliquent à toutes les unités de ce type sans mention dans le profil :

| Type | Règle intrinsèque |
|---|---|
| **Infanterie** | Les faces Épées croisées et Cible infligent **2 PV** à la cible au lieu de 1 |
| **Cavalerie** | Aucune règle intrinsèque — 1 touche = 1 PV |
| **Créature** | Jamais Faible (sauf exception explicite dans le profil) |
| **Machine de guerre** | Jamais Faible |
| **Artillerie** | Jamais Faible · Perd ses servants en premier (ordre de pertes défini dans le profil) |

> 🔗 **Voir aussi** [[BdVM_Regles_Base]] §2 — Types d'unités

### Priorité de résolution

Lors d'une attaque, les modificateurs s'appliquent dans l'ordre suivant :

1. Relances et bonus de dés (avant résolution) — [Arme Lourde X], [Perforant X], [Réception de charge]
2. Décompte des touches
3. Règle intrinsèque Infanterie (Épées croisées et Cible → 2 PV)
4. Annulation de la règle intrinsèque — [Massif]
5. Réductions défensives — [Armure X]
6. Effets de Couronne — [Poison], [Souffle de feu], [Charge écrasante]
7. Résistances spéciales — [Inébranlable X]
8. Drapeaux et retraites (après résolution des touches)

---

## Règles défensives

---

### [Armure X]

**Factions :** Empire (Chevaliers [Armure 1], Tank à vapeur [Armure 2])

Lorsque cette unité reçoit une attaque de **mêlée**, elle retire **X faces Épée** des résultats avant de compter les touches. Les faces **Épées croisées** ne sont jamais affectées par [Armure].

[Armure X] ne s'applique **pas** aux attaques à distance.

> 💡 **Exemple de jeu**
> Des Lanciers attaquent des Chevaliers [Armure 1] adjacents : 3 dés. Résultat : Épées croisées, Épée, Drapeau. [Armure 1] retire 1 Épée → 1 touche restante (Épées croisées). La règle intrinsèque Infanterie s'applique : 1 Épées croisées = 2 PV perdus chez les Chevaliers.

---

### [Inébranlable X]

**Factions :** Empire (Flagellants [Inébranlable 2], Tank à vapeur [Inébranlable 1]) · Hommes-Lézards (Stégadon [Inébranlable 1])

Cette unité ignore **X résultats de retraite** par attaque reçue, quelle qu'en soit la source — dés, cartes tactiques ou sorts.

> 💡 **Exemple de jeu**
> Des Flagellants [Inébranlable 2] reçoivent une attaque dont le résultat produit 3 Drapeaux. Ils ignorent 2 Drapeaux → ne reculent que d'1 hexagone.
> Avec seulement 1 ou 2 Drapeaux obtenus, les Flagellants ne reculent pas du tout.

---

### [Immunisé au poison]

**Factions :** Hommes-Lézards (toutes les unités)

Cette unité ignore les touches supplémentaires générées par la règle **[Poison]**, quelle qu'en soit la source. Les touches normales s'appliquent normalement.

> 💡 **Exemple de jeu**
> Des Skinks tirent sur des Saurus à l'Épée (scénario allié) : 2 dés. Résultat : Cible, Couronne. La Couronne ([Poison]) n'a aucun effet — 1 touche seulement, soit 1 PV perdu ([Massif]).

---

### [Immunisé au feu]

**Factions :** — *(aucune unité en Phase 1.6)*

Cette unité ignore les touches supplémentaires générées par la règle **[Souffle de feu]**. Réservé aux unités de Phase 2+ (ex. créatures ignifuges).

> ⚠️ **Point ouvert** — Phase 2 : définir quelles unités disposent de cette immunité.

---

### [Massif]

**Factions :** Hommes-Lézards (Saurus à l'Épée, Saurus à la Lance, Gardes du Temple)

Les attaques reçues par cette unité n'infligent qu'**1 PV par touche**, quelle que soit la source. La règle intrinsèque du type Infanterie (Épées croisées et Cible → 2 PV) ne s'applique pas contre cette unité.

> 💡 **Exemple de jeu**
> Des Épéistes attaquent des Saurus à l'Épée [Massif] adjacents : 3 dés. Résultat : Épées croisées, Épée, Drapeau → 2 touches. [Massif] : chaque touche n'inflige qu'1 PV → 2 PV perdus seulement (au lieu de 3 sans [Massif]).

---

### [Protection X]

**Factions :** — *(règle de terrain, non portée par une unité en Phase 1.6)*

Lorsqu'une unité occupant une position protégée (bâtiment, fortification) reçoit une attaque, elle ignore **X touches** après décompte des dégâts.

| Type de position | Valeur |
|---|---|
| Ruine | 1 |
| Bâtiment solide | 2 |
| Fortification | 3 |

> 🔗 **Voir aussi** [[BdVM_Terrain]] §9 — Bâtiment.

---

## Règles offensives — Mêlée

---

### [Arme Lourde X]

**Factions :** Empire (Hallebardiers [Arme Lourde 1], Grandes Épées [Arme Lourde 1]) · Hommes-Lézards (Gardes du Temple [Arme Lourde 1])

Après le lancer de dés, le joueur peut **relancer X dés** de son choix. Chaque dé ne peut être relancé qu'une seule fois.

> 💡 **Exemple de jeu**
> Des Hallebardiers [Arme Lourde 1] attaquent des Chevaliers adjacents : 3 dés. Résultat : Épée, Drapeau, Arcane. Le joueur relance l'Arcane → obtient Épées croisées. Résultat final : Épée + Épées croisées = 2 touches.

---

### [Charge écrasante]

**Factions :** Hommes-Lézards (Stégadon, Saurus sur Carnosaure)

Lorsque cette unité a **effectué un déplacement ce tour** avant d'attaquer, chaque face **Couronne** obtenue inflige **1 touche supplémentaire** à une unité adjacente à la cible (au choix du joueur actif).

> 💡 **Exemple de jeu**
> Un Stégadon se déplace d'1 hexagone et attaque des Hallebardiers adjacents : 3 dés. Résultat : Épées croisées, Couronne, Drapeau. [Charge écrasante] : la Couronne inflige 1 touche sur des Lanciers adjacents aux Hallebardiers — 2 PV perdus chez les Lanciers (règle intrinsèque Infanterie).

---

### [Férocité]

**Factions :** Empire (Flagellants)

Lorsque cette unité effectue une **contre-attaque**, celle-ci est résolue **avant** que l'adversaire ne résout ses retraites. Si l'adversaire est éliminé par la contre-attaque, ses retraites ne sont pas résolues.

> 💡 **Exemple de jeu**
> Des Grandes Épées attaquent les Flagellants : 4 Drapeaux. Les Flagellants contre-attaquent immédiatement ([Férocité]) avant de résoudre leur retraite. S'ils éliminent les Grandes Épées, les Drapeaux ne sont plus appliqués.

---

### [Martyre]

**Factions :** Empire (Flagellants)

Lorsque les Flagellants attaquent, le joueur peut **sacrifier 1 figurine** de l'unité pour convertir **1 face Couronne** en **1 touche supplémentaire**. La figurine sacrifiée est retirée immédiatement.

> 💡 **Exemple de jeu**
> Des Flagellants attaquent des Saurus : 2 dés. Résultat : Couronne, Drapeau. Le joueur sacrifie 1 Flagellant → la Couronne devient 1 touche. La règle intrinsèque Infanterie s'applique : 1 touche = 2 PV perdus chez les Saurus.

---

### [Réception de charge]

**Factions :** Empire (Lanciers) · Hommes-Lézards (Saurus à la Lance)

Lorsque cette unité effectue une **contre-attaque** contre une unité qui s'est **déplacée ce tour**, elle lance **1 dé supplémentaire**.

> 💡 **Exemple de jeu**
> Des Chevaliers avancent de 2 hexagones et chargent les Lanciers. Les Lanciers contre-attaquent : 3 + 1 = **4 dés** grâce à [Réception de charge]. Si les Chevaliers n'avaient pas bougé ce tour, les Lanciers n'auraient que 3 dés.

---

## Règles offensives — Distance

---

### [Arme à feu]

**Factions :** Empire (Arquebusiers, Pistoliers, Canon de l'Empire, Tank à vapeur)

Le nombre de dés d'attaque **diminue de 1 par hexagone de distance** au-delà du premier hexagone.

| Distance | Dés lancés |
|---|---|
| 1 hexagone | Valeur d'attaque complète |
| 2 hexagones | Valeur d'attaque − 1 |
| 3 hexagones | Valeur d'attaque − 2 |
| … | … |

> 💡 **Exemple de jeu**
> Des Arquebusiers (Attaque 3, portée 1–3) tirent sur une cible à 2 hexagones : 3 − 1 = **2 dés**. À 3 hexagones : **1 dé**. À 1 hexagone : **3 dés**.
> Un Canon (Attaque 5, portée 1–5) tire à 3 hexagones : 5 − 2 = **3 dés**.

---

### [Bête incontrôlable]

**Factions :** Hommes-Lézards (Salamandres)

Lorsque **tous les servants** de cette unité sont éliminés, elle **ne peut plus se déplacer** mais peut encore attaquer normalement. Une **touche supplémentaire** l'élimine définitivement.

> 💡 **Exemple de jeu**
> Une Salamandre perd ses 3 servants sur deux attaques successives. Elle ne peut plus bouger mais tire encore à 3 dés sur les unités à portée. L'adversaire lui inflige 1 touche → la Salamandre est éliminée.

---

### [Double Tir]

**Factions :** Empire (Archers)

Si les Archers **ne se sont pas déplacés** ce tour, ils peuvent effectuer une **seconde attaque à distance** après leur première, en ciblant la même unité ou une unité différente à portée et en ligne de vue.

> 💡 **Exemple de jeu**
> Des Archers immobiles tirent sur des Skinks à 3 hexagones : 2 dés, 1 touche. Grâce à [Double Tir], ils tirent une seconde fois sur les mêmes Skinks : 2 dés, 1 touche supplémentaire.

---

### [Howdah]

**Factions :** Hommes-Lézards (Stégadon)

Le Stégadon peut effectuer une **attaque à distance en plus de son attaque de mêlée**. Cette attaque utilise **2 dés**, une portée de **1 à 3 hexagones**, et bénéficie de la règle **[Poison]**.

> 💡 **Exemple de jeu**
> Un Stégadon attaque des Saurus ennemis adjacents (mêlée, 3 dés), puis tire sur des Skinks adverses à 2 hexagones grâce à [Howdah] : 2 dés avec [Poison]. Un résultat Couronne sur ce tir inflige 1 touche supplémentaire (sauf [Immunisé au poison]).

---

### [Perforant X]

**Factions :** Empire (Arbalétriers [Perforant 1])

Après le lancer de dés d'une attaque à distance, le joueur peut **relancer X dés** de son choix. Chaque dé ne peut être relancé qu'une seule fois.

> 💡 **Exemple de jeu**
> Des Arbalétriers tirent sur des Chevaliers adjacents : 2 dés. Résultat : Drapeau, Arcane. Le joueur relance l'Arcane ([Perforant 1]) → obtient Cible. Résultat final : 1 touche (Cible = 2 PV perdus via règle intrinsèque Infanterie).

> 🎲 **Note de design** [Perforant X] et [Arme Lourde X] partagent la même mécanique de relance. La distinction de nom reflète leur contexte d'usage : [Arme Lourde X] pour la mêlée, [Perforant X] pour le tir à distance.

---

### [Poison]

**Factions :** Hommes-Lézards (Skinks) · via [Howdah] (Stégadon)

Lorsque cette unité effectue une attaque, chaque face **Couronne** obtenue inflige **1 touche supplémentaire**, sauf contre les unités **[Immunisées au poison]**.

> 💡 **Exemple de jeu**
> Les Skinks tirent sur des Hallebardiers : 2 dés. Résultat : Cible, Couronne → 2 touches (Cible + 1 via [Poison]). Règle intrinsèque Infanterie : 2 touches = 4 PV perdus chez les Hallebardiers.

---

### [Souffle de feu]

**Factions :** Hommes-Lézards (Salamandres)

Lorsque les Salamandres effectuent une attaque, chaque face **Couronne** obtenue inflige **1 touche supplémentaire**, sauf contre les unités **[Immunisées au feu]**.

> 💡 **Exemple de jeu**
> Les Salamandres tirent sur des Grandes Épées : 3 dés. Résultat : Cible, Couronne, Drapeau → 2 touches (Cible + 1 via [Souffle de feu]). Règle intrinsèque Infanterie : 2 touches = 4 PV perdus.

> 🎲 **Note de design** [Souffle de feu] et [Poison] ont la même structure mécanique (Couronne → touche supplémentaire) mais des immunités distinctes. Les Hommes-Lézards sont immunisés au poison mais pas au feu.

---

## Règles de mouvement et de manœuvre

---

### [Meute X]

**Factions :** Hommes-Lézards (Kroxigors [Meute 2])

Cette unité est composée de **plusieurs figurines de X PV chacune**. Retirer une figurine dès qu'elle atteint 0 PV. L'unité est **Faible** quand il ne reste qu'une seule figurine.

> 💡 **Exemple de jeu**
> Les Kroxigors [Meute 2] ont 2 figurines de 2 PV chacune (4 PV total). Ils reçoivent 3 touches : les 2 premiers PV éliminent la première figurine, le 3e PV est appliqué à la seconde. Il reste 1 figurine à 1 PV → l'unité est Faible.

---

### [Mobilité X]

**Factions :** Empire (Pistoliers [Mobilité 2])

Après avoir effectué une attaque, cette unité peut se déplacer de **X hexagones supplémentaires**.

> 💡 **Exemple de jeu**
> Des Pistoliers tirent sur une unité ennemie puis se déplacent de 2 hexagones pour se mettre hors de portée de contre-attaque.

---

### [Poursuite X]

**Factions :** Empire (Chevaliers [Poursuite 1]) · Hommes-Lézards (Saurus sur Sang-froid [Poursuite 2], Saurus sur Carnosaure [Poursuite 2])

Après avoir **éliminé une unité ennemie adjacente** ou l'avoir **forcée à retraiter**, cette unité peut, **à la place de l'avance normale**, se déplacer de **jusqu'à X hexagones** et effectuer **une attaque supplémentaire** contre une unité adjacente à sa nouvelle position.

> 💡 **Exemple de jeu**
> Un Saurus sur Carnosaure [Poursuite 2] élimine des Épéistes adjacents. Il se déplace de 2 hexagones et attaque des Archers voisins : 4 dés supplémentaires.

---

### [Rechargement]

**Factions :** Empire (Canon de l'Empire)

Cette unité **ne peut pas attaquer** si elle s'est **déplacée ce tour**.

> 💡 **Exemple de jeu**
> Le Canon se déplace d'1 hexagone pour améliorer sa position — il ne peut pas tirer ce tour. Au tour suivant, immobile, il peut tirer normalement.

> 🎲 **Note de design** Le Tank à vapeur ne possède pas [Rechargement] — c'est le différenciateur tactique majeur entre les deux machines. Le Canon est plus puissant (5 dés) mais statique ; le Tank est mobile (peut avancer et tirer) mais moins offensif (4 dés).

---

### [Terrain favori : Boisé]

**Factions :** Hommes-Lézards (Skinks)

Cette unité ignore **toutes les restrictions** de mouvement et de combat liées au terrain boisé (forêt). Elle est traitée comme si elle se trouvait en terrain de campagne pour ces effets.

Les restrictions annulées incluent :
- le plafond de 2 dés en terrain boisé (§4.2)
- l'arrêt immédiat à l'entrée d'un hexagone boisé (§4.1)
- l'arrêt de retraite en forêt (§4.4)

Les effets de **ligne de vue** du terrain boisé s'appliquent normalement à toutes les unités, y compris celles avec [Terrain favori : Boisé].

> 💡 **Exemple de jeu**
> Des Skinks [Terrain favori : Boisé] se déplacent de 2 hexagones en forêt : ils n'y sont pas arrêtés et poursuivent leur mouvement normalement.
>
> Des Skinks tirent depuis un bois sur des Hallebardiers à 2 hexagones : **2 dés** (valeur normale — plafond de 2 dés ignoré).
>
> Des Skinks en retraite entrent dans un hexagone de forêt : ils **ne s'arrêtent pas** et continuent leur retraite normalement.
>
> Des Hallebardiers attaquent des Skinks dans un bois : les Hallebardiers sont toujours soumis au plafond de 2 dés. [Terrain favori : Boisé] s'applique uniquement à l'unité qui le possède, pas à ses attaquants.

> 🎲 **Note de design**
> [Terrain favori : Boisé] annule une pénalité — il ne confère pas de bonus. Des Skinks en forêt ne sont pas meilleurs qu'en campagne, ils y sont aussi efficaces. C'est suffisant pour créer une asymétrie tactique lisible : l'ennemi est gêné dans les bois, les Skinks ne le sont pas. La LdV reste bloquante pour tout le monde afin de conserver la valeur de couvert du terrain.

---

## Récapitulatif alphabétique

| Règle                        | Catégorie           | Effet résumé                                                              | Factions                                                                 |
| ---------------------------- | ------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **[Arme à feu]**             | Offensif — Distance | −1 dé par hexagone au-delà du premier                                     | Empire (Arquebusiers, Pistoliers, Canon, Tank à vapeur)                  |
| **[Arme Lourde X]**          | Offensif — Mêlée    | Relancer X dés après le lancer                                            | Empire (Hallebardiers, Grandes Épées) · HL (Gardes du Temple)            |
| **[Armure X]**               | Défensif            | Retire X faces Épée des attaques de mêlée reçues                          | Empire (Chevaliers [1], Tank à vapeur [2])                               |
| **[Bête incontrôlable]**     | Offensif — Distance | Sans servants : ne bouge plus, 1 touche pour éliminer                     | HL (Salamandres)                                                         |
| **[Charge écrasante]**       | Offensif — Mêlée    | Si déplacé ce tour : Couronne → touche sup. sur unité adjacente           | HL (Stégadon, Saurus sur Carnosaure)                                     |
| **[Double Tir]**             | Offensif — Distance | Seconde attaque si non déplacé ce tour                                    | Empire (Archers)                                                         |
| **[Férocité]**               | Offensif — Mêlée    | Contre-attaque résolue avant les retraites adverses                       | Empire (Flagellants)                                                     |
| **[Howdah]**                 | Offensif — Distance | Attaque à distance en plus de la mêlée — 2 dés (1–3) + [Poison]           | HL (Stégadon)                                                            |
| **[Immunisé au feu]**        | Défensif            | Ignore les touches de [Souffle de feu]                                    | — (Phase 2+)                                                             |
| **[Immunisé au poison]**     | Défensif            | Ignore les touches de [Poison]                                            | HL (toutes les unités)                                                   |
| **[Inébranlable X]**         | Défensif            | Ignore X résultats de retraite par attaque reçue                          | Empire (Flagellants [2], Tank à vapeur [1]) · HL (Stégadon [1])          |
| **[Martyre]**                | Offensif — Mêlée    | Sacrifier 1 fig. pour convertir 1 Couronne en touche                      | Empire (Flagellants)                                                     |
| **[Massif]**                 | Défensif            | 1 PV perdu par touche — annule la règle intrinsèque Infanterie            | HL (Saurus à l'Épée, Saurus à la Lance, Gardes du Temple)                |
| **[Meute X]**                | Manœuvre            | X PV par figurine — Faible à 1 figurine restante                          | HL (Kroxigors [2])                                                       |
| **[Mobilité X]**             | Manœuvre            | Déplacement supplémentaire de X hex après l'attaque                       | Empire (Pistoliers [2])                                                  |
| **[Perforant X]**            | Offensif — Distance | Relancer X dés après le lancer (attaque à distance)                       | Empire (Arbalétriers [1])                                                |
| **[Poison]**                 | Offensif — Distance | Couronne → 1 touche sup. (sauf [Immunisé au poison])                      | HL (Skinks) · via [Howdah] (Stégadon)                                    |
| **[Poursuite X]**            | Manœuvre            | Alternative à l'avance : jusqu'à X hex + attaque sup.                     | Empire (Chevaliers [1]) · HL (Saurus sur Sang-froid [2], Carnosaure [2]) |
| **[Protection X]**           | Défensif            | Ignore X touches (terrain : bâtiments, fortifications)                    | Terrain                                                                  |
| **[Rechargement]**           | Manœuvre            | Ne peut pas attaquer si déplacé ce tour                                   | Empire (Canon)                                                           |
| **[Réception de charge]**    | Offensif — Mêlée    | +1 dés en contre-attaque si l'adversaire s'est déplacé ce tour            | Empire (Lanciers) · HL (Saurus à la Lance)                               |
| **[Souffle de feu]**         | Offensif — Distance | Couronne → 1 touche sup. (sauf [Immunisé au feu])                         | HL (Salamandres)                                                         |
| **[Terrain favori : Boisé]** | Manœuvre            | Ignore toutes les restrictions de mouvement et de combat en terrain boisé | HL (Skinks)                                                              |

---

## Index par faction

### Empire

| Unité | Règles spéciales |
|---|---|
| Épéistes | — |
| Lanciers | [Réception de charge] |
| Hallebardiers | [Arme Lourde 1] |
| Archers | [Double Tir] |
| Arbalétriers | [Perforant 1] |
| Arquebusiers | [Arme à feu] |
| Grandes Épées | [Arme Lourde 1] |
| Flagellants | [Inébranlable 2], [Férocité], [Martyre] |
| Pistoliers | [Mobilité 2], [Arme à feu] |
| Chevaliers | [Armure 1], [Poursuite 1] |
| Canon de l'Empire | [Arme à feu], [Rechargement] |
| Tank à vapeur | [Inébranlable 1], [Arme à feu], [Armure 2] |

### Hommes-Lézards

> **Rappel :** toutes les unités Hommes-Lézards sont **[Immunisées au poison]**.

| Unité | Règles spéciales |
|---|---|
| Saurus à l'Épée | [Massif], [Immunisé au poison] |
| Saurus à la Lance | [Massif], [Réception de charge], [Immunisé au poison] |
| Gardes du Temple | [Massif], [Arme Lourde 1], [Immunisé au poison] |
| Kroxigors | [Meute 2], [Immunisé au poison] |
| Skinks | [Poison], [Terrain favori : Boisé], [Immunisé au poison] |
| Salamandres | [Souffle de feu], [Bête incontrôlable], [Immunisé au poison] |
| Saurus sur Sang-froid | [Poursuite 2], [Immunisé au poison] |
| Stégadon | [Inébranlable 1], [Charge écrasante], [Howdah], [Immunisé au poison] |
| Saurus sur Carnosaure | [Charge écrasante], [Poursuite 2], [Immunisé au poison] |

---

## Règles différées — Phase 2+

| Règle | Description préliminaire | Statut |
|---|---|---|
| **[Immunisé au feu]** | Ignore les touches supplémentaires de [Souffle de feu] | ⏳ Phase 2 |
| **[Peur]** | Convertit les Couronnes en Drapeaux supplémentaires contre les unités affectées | ⏳ Phase 2 |
| **[Terreur]** | Version renforcée de [Peur] | ⏳ Phase 2 |
| **[Vol]** | L'unité peut traverser des hexagones occupés et ignorer certains terrains | ⏳ Phase 2 |
| **[Souffle de feu en zone]** | Tir en cône affectant plusieurs hexagones | ⏳ Phase 2 (Salamandres) |
| **Système Lore / Arcanes** | Face Arcane activée — canalisation de sorts | ⏳ Phase 2 |
| **[Stégadon + Machine des Dieux]** | Profil étendu du Stégadon avec capacités magiques Slann | ⏳ Phase 2 |
| **[Terrain favori : X]** *(autres terrains)* | Jungle, marais, montagne — à définir selon les factions Phase 2+ | ⏳ Phase 2 |

---

*Version : 2.2 — Phase 1.6 — 2026-05-30.*
*🔄 Ajout de [Terrain favori : Boisé] (D079). Mise à jour de l'index Hommes-Lézards (Skinks) et du récapitulatif alphabétique.*
*Remplace : BdVM_Regles_Speciales v2.1 (2026-05-23).*
