---
projet: "Batailles de la Terre du Milieu"
type: "composant"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-08-30"
tags: [BdTdM, "type/composant", "phase/1", "statut/brouillon"]
version: "0.9"
---

# Batailles de la Terre du Milieu — Cartes de commandement

> Ce document définit le système de cartes de commandement, la composition des decks par format de bataille, et le protocole de constitution du deck en début de partie. Les cartes spécifiques aux peuples sont traitées en Phase 3.
>
> Le deck de base est adapté de **BattleLore V1** (Days of Wonder, 2006), dont les cartes de commandement constituent le socle mécanique.

---

## Table des matières

1. [[#1. Principes généraux]]
2. [[#2. Anatomie d'une carte]]
3. [[#3. Les formats de bataille et leurs decks]]
4. [[#4. Composition détaillée du deck]]
5. [[#5. Protocole de constitution du deck]]
6. [[#6. Évolution en Phase 3 — cartes de peuple]]
7. [[#7. Commandement à plusieurs joueurs — format Épique]]

---

## 1. Principes généraux

Le deck de commandement est le **moteur de tension** du jeu. Il conditionne quelles unités peuvent agir à chaque tour, forçant les joueurs à des choix permanents entre opportunité et priorité.

### 1.1 Un deck calibré par format

Le nombre et la nature des cartes sont directement liés à la taille du plateau. La règle de calibrage est la suivante :

> **Le deck doit permettre d'activer en moyenne entre 1/3 et 1/2 des unités d'une armée par tour, quel que soit le format.**

Un deck trop généreux rend chaque tour prévisible. Un deck trop restrictif paralyse les joueurs. Le calibrage par format maintient cet équilibre sur des plateaux de tailles différentes.

### 1.2 La valeur de commandement

Plusieurs cartes activent un nombre d'unités **égal à la valeur de commandement** du joueur, c'est-à-dire le nombre de cartes qu'il a en main au moment où il joue la carte (cette carte comprise).

En Phase 1, la valeur de commandement est fixée par le format (voir §3). En Phase 2+, elle sera déterminée par une formule tenant compte des héros vivants — voir [[Regles_Base]] §5.3.

> 💡 **Exemple de jeu**
> Un joueur joue "Percée Gauche" avec 4 cartes en main (dont "Percée Gauche" elle-même). Sa valeur de commandement est 4 : il peut activer jusqu'à 4 unités dans la section gauche.

### 1.3 Deck partagé

Pour la Phase 1, les deux camps puisent dans un **deck commun unique**, sans cartes de peuple. Chacun constitue sa main en début de partie (voir §5).

> 🔗 **Voir aussi** [[#6. Évolution en Phase 3 — cartes de peuple]]

---

## 2. Anatomie d'une carte

Chaque carte de commandement comporte les informations suivantes, du haut vers le bas :

```
┌─────────────────────────────┐  ← 63 × 88 mm (standard poker)
│  zone de sécurité : 3 mm   │  ← zone utile : 57 × 82 mm
│ ┌─────────────────────────┐ │
│ │   NOM DE LA CARTE       │ │  ← ① Bandeau nom
│ │   type de carte         │ │
│ └─────────────────────────┘ │
│                             │
│  [ G ]  [ C ]  [ D ]        │  ← ② Pictogramme
│   (section active grisée)   │
│                             │
│ ┌─────────────────────────┐ │
│ │  Texte de règle         │ │  ← ③ Zone de règle
│ │  (9.5 px, adapté si     │ │     Fond gris léger
│ │   texte long → 8.5 px)  │ │     Note secondaire sous trait de séparation
│ └─────────────────────────┘ │
│                       [E·N] │  ← ④ Pastille format (bas droite)
└─────────────────────────────┘     E = Escarmouche / N = Normal / É = Épique
```

- **① Bandeau nom** : titre de la carte. Taille variable selon longueur : 18 px (court), 14 px (moyen), 11 px (long). Étiquette de type en dessous (8.5 px, capitales, discret).
- **② Pictogramme** : pour les cartes de section, trois bandes verticales représentant G / C / D — la section active en gris soutenu, les sections inactives en gris très léger. Pour les cartes Tactiques, icône propre à l'effet (silhouettes, flèches, etc.).
- **③ Zone de règle** : texte de la règle en 9.5 px (8.5 px si volume important). Fond gris léger. Une note secondaire optionnelle est séparée par un trait fin (cas limite, interaction avec une règle spéciale, etc.).
- **④ Pastille format** : coin bas droit, hors zone de règle. Indique le(s) deck(s) dans lesquels la carte est incluse.

> ⚠️ **Point ouvert**
> Le format physique des cartes est fixé à 63 × 88 mm (standard poker). La direction artistique finale (typographie, illustrations, couleurs par type de carte, ornements) est réservée à la Phase 4.

---

## 3. Les formats de bataille et leurs decks

### 3.1 Vue d'ensemble

| Format | Plateau | Sections | Main de départ | Taille du deck |
|---|---|---|---|---|
| **Escarmouche** | 10 × 7 | 3 (G / C / D) | 4 cartes | 45 cartes |
| **Normal** | 13 × 9 | 3 (G / C / D) | 5 cartes | 60 cartes |
| **Épique** | 13 × 17 | 3 (G / C / D) | 5 cartes (main de camp, tenue par le joueur Centre) | 60 cartes (deck Normal réutilisé tel quel) |

> 🔄 **Résolu (D087)**
> Le format Épique réutilise le deck Normal sans modification — même 60 cartes, même main de départ. La montée en puissance à 6 joueurs vient du **râtelier de Commandement** partagé (§7), pas d'un deck dédié. Adapté d'*Epic BattleLore* (Days of Wonder, V1, 2007).

### 3.2 Logique de différenciation des decks

Le deck Escarmouche est un **sous-ensemble strict** du deck Normal. On retire les cartes qui activeraient proportionnellement trop d'unités sur un plateau 10×7 et réduiraient la tension tactique :

- Les **Attaque** (G / C / D) : 3 unités par section — trop fort sur un front réduit. **−13 cartes.**
- Les **En avant** : 2 unités dans chaque section, soit 6 activations — disproportionné. **−2 cartes.**

**Total retiré : 15 cartes. Deck Escarmouche : 45 cartes.**

Toutes les autres cartes, y compris les Percées (activation variable selon la main) et les cartes Classe (activation variable par couleur), sont conservées. Sur un plateau réduit avec une main de 4 cartes, la valeur de commandement est naturellement plus basse qu'en Normal, ce qui calibre automatiquement leur puissance.

### 3.3 La valeur de commandement par format

La main de départ détermine la valeur de commandement de base pour les cartes à activation variable :

- **Normal** : main de 5 cartes → valeur de commandement de départ = 5
- **Escarmouche** : main de 4 cartes → valeur de commandement de départ = 4

La valeur de commandement fluctue en cours de partie selon les cartes jouées et piochées, ce qui crée une tension dynamique : jouer une carte réduit temporairement la valeur de commandement avant que la pioche ne la rétablisse.

---

## 4. Composition détaillée du deck

### 4.1 Catégories de cartes

Les cartes se répartissent en deux catégories :

**A — Cartes de section** : activent un nombre défini d'unités dans une ou plusieurs sections du champ de bataille.

**B — Cartes tactiques** : activent des unités selon leur **type** (cavalerie, infanterie, unités à distance) ou leur **classe** (couleur) plutôt que leur position, ou produisent des effets spéciaux.

---

### 4.2 Deck Normal — 60 cartes

> 🔄 **Résolu (D088)**
> Le deck Normal reprend désormais le deck de *BattleLore* (Days of Wonder, V1, 2006) à la lettre — composition et quantités identiques, carte pour carte. Les cartes bannière (Vert/Bleu/Rouge) redeviennent jouables telles quelles depuis la réintroduction de la classe = couleur du plateau (D059-D061) : leur mécanisme d'activation « par couleur » colle exactement à notre taxonomie. Seule « Battlelore » a nécessité une adaptation (nos dés n'ont pas de faces bannière) — elle est notre « Cri de guerre » depuis D019.

#### Cartes de section (42 cartes)

Ces cartes activent des unités selon leur position sur le plateau. Le Centre reçoit systématiquement plus de cartes Attaque et Patrouille que les ailes (5 contre 4 et 5 contre 3) — répartition héritée telle quelle de *BattleLore* V1, pas une invention locale.

**Éclaireur** — Section unique, 1 unité + avantage de pioche _(6 cartes — présentes en Escarmouche)_

| Carte | Nb | Effet |
|---|---|---|
| Éclaireur Gauche | 2 | Activez 1 unité dans la section gauche. Au lieu de piocher normalement en fin de tour, piochez 2 cartes et défaussez-en 1. |
| Éclaireur Centre | 2 | Activez 1 unité dans la section centrale. Au lieu de piocher normalement en fin de tour, piochez 2 cartes et défaussez-en 1. |
| Éclaireur Droite | 2 | Activez 1 unité dans la section droite. Au lieu de piocher normalement en fin de tour, piochez 2 cartes et défaussez-en 1. |

**Patrouille** — Section unique, 2 unités _(11 cartes — présentes en Escarmouche)_

| Carte | Nb | Effet |
|---|---|---|
| Patrouille Gauche | 3 | Activez 2 unités dans la section gauche. |
| Patrouille Centre | 5 | Activez 2 unités dans la section centrale. |
| Patrouille Droite | 3 | Activez 2 unités dans la section droite. |

**Attaque** — Section unique, 3 unités _(13 cartes — **absentes du deck Escarmouche**)_

| Carte | Nb | Effet |
|---|---|---|
| Attaque Gauche | 4 | Activez 3 unités dans la section gauche. |
| Attaque Centre | 5 | Activez 3 unités dans la section centrale. |
| Attaque Droite | 4 | Activez 3 unités dans la section droite. |

**Percée** — Section unique, activation variable _(6 cartes — présentes en Escarmouche)_

| Carte | Nb | Effet |
|---|---|---|
| Percée Gauche | 2 | Activez dans la section gauche autant d'unités que votre valeur de commandement. |
| Percée Centre | 2 | Activez dans la section centrale autant d'unités que votre valeur de commandement. |
| Percée Droite | 2 | Activez dans la section droite autant d'unités que votre valeur de commandement. |

**Cartes multi-sections** _(6 cartes)_

| Carte | Nb | Escarmouche | Effet |
|---|---|---|---|
| En marche | 2 | ✅ | Activez 1 unité dans chaque section. |
| En avant | 2 | ❌ | Activez 2 unités dans chaque section. |
| Encerclement | 2 | ✅ | Activez 2 unités dans la section gauche et 2 unités dans la section droite. |

---

#### Cartes tactiques (18 cartes — toutes présentes en Escarmouche)

Ces cartes activent des unités selon leur classe ou leur type, ou produisent des effets spéciaux.

> ⚠️ **Note terminologique**
> La carte "Contre-attaque" décrite ci-dessous est une **carte de commandement** jouée volontairement depuis la main. Elle est distincte de la **règle universelle de contre-attaque** (réaction automatique disponible pour toute unité survivante après avoir subi une attaque au corps-à-corps). Voir [[Regles_Base]] §7.

**Classe** — activation par couleur de classe _(6 cartes, 3 nouvelles — anciennement les cartes bannière de BattleLore V1)_

| Carte | Nb | Effet |
|---|---|---|
| Classe Verte | 2 | Pour chaque carte de Commandement en main (celle-ci comprise), activez 1 unité 🟢 de votre choix, dans n'importe quelle section. Si vous ne contrôlez aucune unité 🟢, activez 1 unité de votre choix. |
| Classe Bleue | 2 | Pour chaque carte de Commandement en main (celle-ci comprise), activez 1 unité 🔵 de votre choix, dans n'importe quelle section. Si vous ne contrôlez aucune unité 🔵, activez 1 unité de votre choix. |
| Classe Rouge | 2 | Pour chaque carte de Commandement en main (celle-ci comprise), activez 1 unité 🔴 de votre choix, dans n'importe quelle section. Si vous ne contrôlez aucune unité 🔴, activez 1 unité de votre choix. |

**Autres cartes Tactiques** _(12 cartes)_

| Carte | Nb | Effet |
|---|---|---|
| Charge de cavalerie | 3 | Activez autant d'unités de Cavalerie que votre valeur de commandement, dans n'importe quelle section. Les unités 🔴 ainsi activées peuvent se déplacer de 3 cases et batailler quand même (exception à la règle « bouger ou frapper » du 🔴, §6.1). Toutes les unités activées combattent à **+1 dé** en mêlée pour toute la durée du tour. Elles ne peuvent pas tirer à distance. Si vous ne contrôlez aucune unité de Cavalerie, activez 1 unité de votre choix. |
| Assaut d'infanterie | 2 | Activez autant d'unités d'Infanterie que votre valeur de commandement, dans n'importe quelle section. Ces unités doivent être adjacentes entre elles, formant un groupe continu. Elles peuvent se déplacer de 2 hexagones et combattre en mêlée. Elles ne peuvent pas tirer à distance. Si vous ne contrôlez aucune unité d'Infanterie, activez 1 unité de votre choix. |
| Pluie de flèches | 2 | Activez toutes vos unités capables de tirer à distance, dans n'importe quelle section. Ces unités tirent deux fois ce tour, mais ne peuvent pas se déplacer ni tirer à bout portant. Si vous ne contrôlez aucune unité à distance, activez 1 unité de votre choix. |
| Ordre direct | 2 | Activez 1 unité de votre choix, dans n'importe quelle section. Cette unité combat à **+1 dé** pour toute la durée du tour. |
| Contre-attaque | 2 | Jouez cette carte en réponse à la carte que vient de jouer votre adversaire. Vous exécutez le même ordre que lui : si c'est une carte de section, la section gauche devient la droite et vice-versa. Si c'est une carte tactique, appliquez l'effet identique. |
| Cri de guerre | 1 | Lancez autant de dés de bataille que votre valeur de commandement. Pour chaque face **Épée** ou **Épées croisées** obtenue, activez 1 unité de mêlée de votre choix. Pour chaque face **Cible** obtenue, activez 1 unité à distance de votre choix. Pour chaque face **Couronne** obtenue, activez 1 unité de votre choix. Toutes les unités ainsi activées combattent à **+1 dé** pour ce tour. Puis mélangez la défausse avec la pioche. |

> 🎲 **Note de design — Cri de guerre**
> La carte utilise les faces des dés comme mécanisme de sélection d'unités : Épée et Épées croisées → mêlée, Cible → distance, Couronne → libre. Les faces Drapeau et Arcane n'activent aucune unité. La pioche est mélangée immédiatement, quel que soit le résultat des dés. Adaptée de la carte éponyme « Battlelore » (BattleLore V1) — celle-ci active par **couleur de dé obtenue** (nos dés BattleLore V2 n'ont pas de faces bannière), remplacée ici par une activation par **symbole de dé**, seule modification nécessaire à la reprise du deck V1 (D088). Le nom "Cri de guerre" date de D019 (étape intermédiaire "Ruée générale", depuis "Arcanes de guerre" jugé trop connoté magie).

---

### 4.3 Récapitulatif comparatif

| Catégorie | Normal (60) | Escarmouche (45) |
|---|---|---|
| Éclaireur (G / C / D) | 6 | 6 |
| **Patrouille (G / C / D)** | **11** | **11** |
| **Attaque (G / C / D)** | **13** | **—** |
| Percée (G / C / D) | 6 | 6 |
| En marche | 2 | 2 |
| **En avant** | **2** | **—** |
| Encerclement | 2 | 2 |
| **Classe (Verte/Bleue/Rouge)** | **6** | **6** |
| Charge de cavalerie | 3 | 3 |
| Assaut d'infanterie | 2 | 2 |
| Pluie de flèches | 2 | 2 |
| Ordre direct | 2 | 2 |
| Contre-attaque | 2 | 2 |
| Cri de guerre | 1 | 1 |
| **Total** | **60** | **45** |

---

## 5. Protocole de constitution du deck

### 5.1 Avant chaque partie

1. **Choisir le format** de la bataille.
2. **Prendre le deck correspondant**, déjà constitué et maintenu séparé des autres decks.
3. **Mélanger le deck** à la vue des deux camps.
4. **Chaque camp pioche** le nombre de cartes de départ indiqué par le format (5 en Normal, 4 en Escarmouche) pour constituer sa main secrète.
5. Le reste du deck forme la **pioche centrale**, placée face cachée entre les joueurs.

### 5.2 Gestion de la pioche en cours de partie

- Après avoir joué une carte, le joueur actif la défausse face visible à côté de la pioche, puis **pioche 1 carte** pour ramener sa main au nombre initial — sauf s'il a joué un Éclaireur (voir §4.2).
- Si la pioche est épuisée, **mélanger la défausse** pour former une nouvelle pioche. Exception : la carte "Cri de guerre" déclenche ce mélange immédiatement après résolution.

### 5.3 Main minimale

Si un joueur se retrouve sans carte en main en début de son tour (situation rare mais possible en fin de pioche), il pioche immédiatement **2 cartes** avant de jouer.

> 💡 **Exemple de jeu**
> Début de partie en format Normal. Le camp du Bien pioche 5 cartes : Patrouille Centre, Charge de cavalerie, Attaque Droite, Éclaireur Gauche, En marche. Sa valeur de commandement est 5. Il joue "Charge de cavalerie" et peut activer jusqu'à 5 unités de cavalerie sur tout le plateau, chacune avec +1 dé en mêlée. Il défausse la carte, pioche 1 carte, et sa main revient à 5.

---

## 6. Évolution en Phase 3 — cartes de peuple

En Phase 3, chaque peuple dispose d'un **supplément de cartes** qui s'intègre au deck de base selon la règle suivante :

> Pour chaque carte de peuple ajoutée au deck, **une carte générique de même catégorie** est retirée.

Le deck garde ainsi une taille constante par format. L'identité tactique du peuple est renforcée sans déséquilibrer le volume d'activations disponibles.

_Exemple (non définitif, à des fins d'illustration uniquement) :_

- Gondor pourrait ajouter des cartes "Feux d'alerte" (activation d'urgence des garnisons) → retirer autant de "Patrouille" génériques.
- Le Mordor pourrait ajouter des cartes "Cris de guerre" (bonus offensif orque) → retirer autant de "En marche".

> ⚠️ **Point ouvert**
> Le nombre exact de cartes de peuple par armée et le mécanisme d'échange (libre ou imposé par catégorie ?) sont à définir lors de la Phase 3.

---

## 7. Commandement à plusieurs joueurs — format Épique

> 🔄 **Résolu (D087, note mise à jour D088)**
> Adapté d'*Epic BattleLore* (Days of Wonder, extension V1, 2007), avec une seule simplification restante : pas de cartes Lore (pas de couche magie en V1, D001/D010). Les cartes Classe (ex-bannières, D088) sont incluses comme le reste du deck Normal réutilisé tel quel — aucune règle Épique spécifique ne les concerne. Déjà tranché en amont (D016) : chaque joueur contrôle une **Section** (Gauche/Centre/Droite), pas de sous-force nominative.

### 7.1 Rôles

Chaque camp compte 3 joueurs, un par Section. Le camp ne tient qu'**une seule main**, comme en format Normal (§5.1-§5.4 de [[Regles_Base]]) — c'est le **joueur Centre** qui la tient et qui décide, à chaque tour de son camp, quelle(s) carte(s) jouer, en concertation avec ses deux coéquipiers Gauche et Droite.

Une fois la carte choisie, chaque joueur déplace et fait combattre les unités de **sa propre** Section : le joueur Centre ne joue pas à la place de ses coéquipiers, il choisit seulement quel ordre est donné. Sur une carte multi-sections (En marche, En avant, Encerclement) ou une carte Tactique touchant plusieurs sections (Charge de cavalerie, Cri de guerre, etc.), chaque joueur résout l'activation de ses propres unités concernées.

> 💡 **Exemple de jeu**
> Le camp Bien joue « En avant » (2 unités par section). Le joueur Centre annonce la carte ; chacun des 3 joueurs déplace et fait combattre 2 de ses propres unités, dans sa propre Section.

**Hexagones de frontière.** Une limite de Section peut couper des hexagones en deux plutôt que suivre leurs arêtes — c'est le cas de quatorze cases au Pelennor (colonnes F et L des lignes impaires, voir `[[Pelennor_Epique]]` §2.1). Un hexagone ainsi coupé **appartient aux deux Sections voisines** : l'unité qui s'y trouve peut être activée par l'un **ou** l'autre des deux joueurs concernés, mais **jamais par les deux dans le même tour**. Elle compte pour une seule unité ordonnée, à porter au décompte de la Section du joueur qui l'active.

**Transfert de contrôle en cours de tour.** Si une unité franchit la ligne séparant deux Sections au cours d'un même tour, le joueur qui a initié son mouvement la contrôle jusqu'à la fin du tour. Au tour suivant, elle passe sous le contrôle du joueur de la Section où elle se trouve désormais.

### 7.2 Le râtelier de Commandement

En plus de sa main, chaque camp peut piocher dans un **râtelier commun** de 3 cartes, visibles des deux camps, posé à côté de la pioche. Avant le premier tour, remplir le râtelier avec les 3 cartes du dessus du deck Normal (§3, 60 cartes — deck unique, partagé entre les deux camps comme en Normal, §1.3).

À la fin de son tour, si une carte a été prélevée dans le râtelier, un camp pioche une carte de remplacement depuis la pioche et la place dans le râtelier (visible des deux camps) — le râtelier doit toujours compter 3 cartes en début de tour. Si les 3 cartes du râtelier sont un jour toutes des cartes Tactiques, défaussez-les et repiochez 3 nouvelles cartes : le râtelier doit toujours contenir au moins une carte de section une fois reconstitué. Si la pioche s'épuise, mélangez la défausse pour former une nouvelle pioche.

### 7.3 Déroulement du tour

À son tour, un camp joue **soit** :

- **jusqu'à 2 cartes de section** — si 2 cartes sont jouées, l'une doit venir de sa main, l'autre du râtelier (si une seule est jouée, elle peut venir indifféremment de la main ou du râtelier) ;
- **soit une seule carte Tactique**, venant de sa main ou du râtelier.

Un camp ne peut jamais combiner une carte de section et une carte Tactique dans le même tour, ni jouer deux cartes Tactiques dans le même tour.

Si un camp joue une carte Tactique **prise dans le râtelier**, il ne pioche **pas** de carte de remplacement pour sa main en fin de tour — seul le râtelier est reconstitué (§7.2). S'il joue une carte Tactique **de sa main**, il pioche normalement en fin de tour, comme en Normal.

> 💡 **Exemple de jeu** *(adapté d'Epic BattleLore)*
> Le camp Mal joue « Attaque Gauche » (sa main) et « Patrouille Droite » (le râtelier) : 3 unités activées à gauche, 2 à droite, dans le même tour.

### 7.4 Valeur de commandement

La valeur de commandement reste égale au nombre de cartes dans la **main du camp** (celle du joueur Centre) — les cartes présentes dans le râtelier ne comptent jamais dans ce calcul, même si le camp vient d'en jouer une.

### 7.5 Erratum Épique — Contre-attaque

Si l'adversaire vient de jouer 2 cartes de section (§7.3), « Contre-attaque » n'en contre qu'**une seule**, au choix du camp qui contre.

### 7.6 Ordre de jeu

L'alternance des tours entre les deux camps reste celle du format Normal — un camp joue, puis l'autre, sans changement lié au nombre de joueurs. Le premier camp à jouer est déterminé par le scénario (voir le document de scénario concerné), pas par une règle de commandement.

---

> 🔗 **Voir aussi**
> [[Regles_Base]] — [[Regles_Speciales]] — [[Document_de_cadrage]]

---

*Version : 0.9 — Phase 1 — 2026-08-30. **D119 — règle des hexagones de frontière ajoutée au §7.1.** Lacune réelle du document : le transfert de contrôle traitait le cas d'une unité qui *franchit* une limite de Section en cours de tour, mais rien ne disait ce qu'il advenait d'une unité *posée à cheval* sur une limite qui coupe l'hexagone. Un tel hexagone appartient désormais explicitement aux deux Sections voisines, activable par l'un ou l'autre joueur mais jamais par les deux dans le même tour. Aucune autre modification.*

*Version : 0.8 — Phase 1 — 2026-08-16. **Correction de cohérence — note d'intro §7.** La note D087 mentionnait encore « pas de bannières de couleur » comme simplification Épique, périmée depuis D088 (cartes Classe réintégrées au deck Normal, donc au râtelier Épique sans traitement spécial). Repérée en répondant à une question directe sur l'emplacement des règles Épique — aucune décision mécanique, pas de nouveau numéro D.*

*Version : 0.7 — Phase 1 — 2026-08-16. **D088 — reprise littérale du deck de commandement de BattleLore V1**, en réponse à la réintroduction de la classe = couleur du plateau (D059-D061). **Supersède la note de D087** qui donnait les cartes bannière pour non intégrées : elles reviennent bel et bien, sous le nom **Classe Verte/Bleue/Rouge**, avec un texte identique à l'original (activation par couleur de classe, jamais de carte morte). §3.1, §3.2, §4.1, §4.2 et §4.3 réécrits : **Attaque** et **Patrouille** perdent leur symétrie (Centre renforcé : Attaque 5/4/4 au lieu de 5/5/5, Patrouille 5/3/3 au lieu de 5/5/5 — total cartes de section 48→**42**) ; 3 nouvelles cartes Classe ajoutées (6 cartes, total cartes Tactiques 12→**18**) ; deck Normal toujours à **60** cartes, calibrage exact retrouvé carte pour carte. Deck Escarmouche recalculé en conséquence (43→**45**, retrait Attaque 15→13). « Charge de cavalerie » gagne la clause Bannière Rouge d'origine (les 🔴 activés peuvent se déplacer 3 cases et batailler quand même) ; « Assaut d'infanterie » et « Pluie de flèches » gagnent leur clause de repli (« si vous ne contrôlez aucune unité éligible, activez 1 unité de votre choix »), comme dans le texte d'origine. « Cri de guerre » reste la seule carte modifiée par rapport à V1 (nos dés n'ont pas de faces bannière) — confirmé, aucun autre changement nécessaire.*

*Version : 0.6 — Phase 1 — 2026-08-16. **D086 (format Épique corrigé, 13×17) et D087 (commandement à plusieurs joueurs en Épique).** §3.1 : plateau corrigé, deck/main Épique fixés (deck Normal réutilisé tel quel, 60 cartes/main de 5), point ouvert levé. **§7 entièrement réécrit**, adapté d'*Epic BattleLore* (Days of Wonder, V1, 2007) : rôle décisionnel du joueur Centre (main unique par camp, exécution distribuée par Section), râtelier de Commandement partagé (3 cartes, alimenté par le deck Normal), déroulement du tour (jusqu'à 2 cartes de section ou 1 carte Tactique, sources main/râtelier), règle de transfert de contrôle d'unité en cours de tour, valeur de commandement (râtelier hors calcul), erratum Contre-attaque (ne contre qu'une des deux cartes de section adverses), ordre de jeu (inchangé par rapport au Normal). Cartes bannière (D064) confirmées non intégrées, hors périmètre de cette passe.*

*Version : 0.5 — Phase 1 — 2026-08-16. **Corrections de relecture — revue de finalisation « Verrouillage v1.0 ».** Liens `[[Document de cadrage]]` corrigés en `[[Document_de_cadrage]]` (nom réel du fichier, 2 occurrences). Aucune décision mécanique — pas de numéro D.*

*Version : 0.4 — Phase 1 — 2026-07-19.*
*Première adaptation de Batailles de la Terre du Milieu (BdTdM) : reprise du système de deck générique, sans reprise du contenu spécifique à l'autre projet dont il est issu. Renommage "Bataille" → "Normal" (même plateau 13×9, mêmes decks). Dimensions du format Épique alignées sur le document de cadrage (16×13, D005). Annexe de correspondance BattleLore V1 retirée (plus nécessaire — terminologie déjà fixée). Carte "Arcanes de guerre" renommée en "Cri de guerre" (D019, via l'étape intermédiaire "Ruée générale") — connotation magique incompatible avec l'absence de couche pouvoirs en V1 (D001, D010) ; nom final choisi pour son ancrage Terre du Milieu, neutre entre les deux camps ; mécanisme de dés inchangé. Ajout d'une section dédiée au commandement multi-joueurs, explicitement différée à la Phase 2. Renommé depuis `BdVM_Cartes_Commandement.md`. **Correction** : "Charge de cavalerie", "Ordre direct" et "Cri de guerre" indiquaient un bonus **+2 dés**, reliquat d'une ancienne calibration de BdVM (abandonnée dans ce projet jumeau) — corrigé en **+1 dé**, cohérent avec le reste du système.*
