---
projet: "Batailles de la Terre du Milieu"
type: "livret"
phase: "P14b"
statut: "en-cours"
date_maj: "2026-10-17"
tags: [BdTdM, type/livret]
version: "0.2"
---

# Batailles de la Terre du Milieu — Livret de référence

> Conventions d'écriture, frontières avec les autres livrets et glossaire : [[00_Conventions_et_glossaire]].

## Comment utiliser ce livret

Ce livret se garde sur la table. Il contient toutes les règles du jeu, classées par ordre alphabétique : quand une question se pose en cours de partie, c'est ici qu'on cherche la réponse.

- **Les entrées alphabétiques** couvrent tous les termes du jeu, les règles entre crochets comme [Armure] ou [Férocité], les terrains et les cas particuliers.
- **Le chapitre des cartes de commandement** donne le texte complet de chaque carte.
- **Le tableau du terrain**, en fin de livret, résume les effets de chaque terrain.

Le livret de règles apprend à jouer ; ce livret-ci répond aux questions. S'ils semblent se contredire, ce livret fait foi. Les règles propres à une bataille sont dans le livret de scénario, et celles d'une pièce unique dans le livret Factions : elles l'emportent sur celles de ce livret.

Les mots en *italique* renvoient à une autre entrée de ce livret.

---

## Entrées alphabétiques

### Activation

Activer une unité, c'est la mettre en action pour le tour : elle peut alors se déplacer puis attaquer. Une unité non activée ne bouge pas et ne combat pas, sauf pour reculer ou riposter.

- On active des unités en jouant une carte de commandement, puis, si on le souhaite, en dépensant des jetons de *Pouvoir*.
- Une unité n'est jamais activée deux fois dans le même tour, même si deux cartes, ou une carte et du Pouvoir, peuvent la désigner.
- Les unités activées sont désignées à l'étape d'ordre, avant tout mouvement.

*Voir aussi : Carte de section, Carte Tactique, Ignorer une carte, Pouvoir, Tour.*

### Archer en mêlée

**[Archer en mêlée]** : les faces {DÉ:Arc} Arc de l'unité touchent aussi quand elle attaque ou riposte en mêlée.

- Les Épées croisées et les Épées touchent normalement, comme pour toute unité de mêlée.
- Quand l'unité est *Faible*, ses Épées ne touchent plus, mais ses Arcs touchent toujours.

### Armure

**[Armure]** : pour chaque touche subie, l'unité lance 1 dé. Chaque {DÉ:Pouvoir} Pouvoir annule une touche. Si un *Leader* mène l'unité, chaque {DÉ:Couronne} Couronne en annule une aussi.

- L'[Armure] vaut contre toute attaque, mêlée comme tir, et contre toutes les faces qui touchent.
- Elle se lance après la *Protection*, sur les touches qui restent.
- Elle ne sauve pas les pertes d'une retraite bloquée (voir *Retraite*).
- Les dés d'[Armure] ne rapportent pas de jeton de Pouvoir.
- Toute unité rouge et toute *Créature* porte [Armure] d'office. D'autres unités la reçoivent par une règle, comme *Discipline de cohorte*.
- [Armure] n'est pas cumulable. Deux sources ne donnent pas deux dés par touche.

### Attaque

À l'étape d'attaque, chaque unité activée peut attaquer une unité ennemie, dans l'ordre choisi par son camp. Une unité peut renoncer à attaquer. Une unité n'attaque qu'une fois par tour, sauf si une règle ou une carte lui donne une attaque de plus.

Une attaque se résout toujours dans cet ordre :

1. **Choisir la cible.** En mêlée {MÊLÉE}, une unité ennemie adjacente. En tir {DISTANCE}, une unité ennemie à *Portée* et en *Ligne de vue*, adjacente comprise.
2. **Lancer les dés** (voir *Plafond de dés*), puis appliquer les relances (voir *Relance*). Chaque {DÉ:Pouvoir} Pouvoir obtenu rapporte 1 jeton de *Pouvoir*.
3. **Compter** les touches et les Drapeaux (voir *Faces de dé*).
4. **Encaisser** : *Protection*, puis *Armure*, puis pertes. La cible qui perd sa dernière figurine, ou son dernier PV, est en *Déroute*.
5. **Reculer** : la cible survivante recule de 1 hexagone par Drapeau (voir *Retraite*).
6. **Riposter** : la cible adjacente qui n'a pas bougé peut riposter (voir *Riposte*).
7. **Avancer ou poursuivre** : après une attaque de mêlée qui a fait reculer ou mis en déroute sa cible (voir *Avance*, *Poursuite*).

La mêlée n'a pas besoin de ligne de vue.

*Voir aussi : Faces de dé, Terrain.*

### Avance

Quand une attaque de **mêlée** met sa cible en déroute ou la fait reculer, l'attaquant peut entrer dans l'hexagone qu'elle a libéré. Rien ne l'y oblige.

- Un tir, même sur une unité adjacente, ne permet pas d'avancer, pas plus qu'une riposte.
- L'avance n'est arrêtée par aucun terrain : on entre dans l'hexagone libéré, quel qu'il soit.
- Une unité qui porte [Poursuite] peut poursuivre au lieu d'avancer (voir *Poursuite*).
- Une unité ne peut pas attaquer après avoir avancé, sauf par une poursuite.

### Badge

Un badge donne une règle de plus à une unité. Il est matérialisé par un jeton de badge d'unité, posé à côté d'elle. Il en existe deux :

- {LEADER} **Leader** : un Leader mène l'unité (voir *Leader*).
- {FACTION} **Faction** : l'unité a une règle propre, indiquée sur son profil (voir *Faction*).

La figurine avec bannière n'est pas un badge (voir *Bannière*).

### Bannière

Une unité peut compter une figurine avec bannière. Ce n'est pas un badge, mais l'unité y gagne [Inébranlable 1] : elle peut ignorer 1 Drapeau à chaque attaque qu'elle subit.

- La bannière s'additionne aux autres sources d'[Inébranlable] (voir *Inébranlable*).
- La figurine avec bannière est retirée en dernier quand l'unité subit des pertes. Si un Leader mène l'unité, elle est retirée en avant-dernier, juste avant lui.
- Une unité qui n'a plus de figurine avec bannière perd cet [Inébranlable 1].

### Bâtiment

Terrain. Une unité qui entre dans un bâtiment s'y arrête. Elle peut combattre depuis le bâtiment ce tour, et en sortir normalement au tour suivant.

- **Combat** : l'unité dans un bâtiment porte [Protection] : elle ignore 1 touche à chaque attaque qu'elle subit (voir *Protection*).
- **Vue** : un bâtiment bloque la ligne de vue. L'unité qui s'y trouve voit et tire normalement vers l'extérieur, et on peut tirer sur elle.
- **Retraite** : une unité qui recule traverse un bâtiment sans s'arrêter.

### Bois

Terrain. Une unité qui entre dans un bois s'y arrête, même s'il lui reste du mouvement. Elle en sort normalement au tour suivant.

- **Combat** : quand l'attaquant **ou** sa cible se trouve dans un bois, l'attaquant lance 2 dés au plus, en mêlée comme au tir, riposte comprise. Cette limite s'applique aux dés de l'unité, avant les dés en plus d'une carte ou d'une règle (voir *Plafond de dés*). Une unité qui lance déjà 2 dés n'est pas affectée.
- **Vue** : un bois bloque la ligne de vue. Une unité dans un bois voit et tire normalement vers l'extérieur, et on peut tirer sur une unité qui s'y trouve.
- **Retraite** : une unité qui recule traverse un bois sans s'arrêter.

### Bord

Chaque camp a son bord : le bord du champ de bataille de son côté. Le scénario y déploie son armée, ses Sections se nomment depuis lui, et ses unités reculent toujours vers lui.

### Camp

Le Bien ou le Mal. Chaque camp est mené par un à trois joueurs et réunit un ou plusieurs *Peuples*.

### Carte de section

Carte de commandement qui active des unités dans une ou plusieurs Sections. Le nombre d'unités est indiqué sur la carte : vous choisissez lesquelles, parmi celles qui se trouvent dans la Section visée au moment où vous jouez la carte.

- Une unité sur un *Hexagone de frontière* peut être activée par une carte de l'une ou l'autre de ses Sections.
- S'il y a moins d'unités dans la Section que la carte n'en permet, les activations en trop sont perdues.

Texte de chaque carte : chapitre *Cartes de commandement*.

### Carte Tactique

Carte de commandement qui active selon un autre critère que la Section : le type, la classe, le mode… le plus souvent n'importe où sur le champ de bataille. Beaucoup donnent en plus un avantage. La carte dit tout ce qu'elle fait, et son texte l'emporte sur les règles générales.

Texte de chaque carte : chapitre *Cartes de commandement*.

### Champ de bataille

Le tapis d'hexagones sur lequel se joue la partie. Sa taille dépend du *Format*. Il se découpe en trois *Sections* et peut porter du *Terrain*.

### Char

Pièce sur socle unique, avec un compteur de PV. Un Char compte comme une unité de *Cavalerie* pour tout le reste : cartes, activations, mouvement, et règles qu'il porte d'office.

- Il se déplace comme la Cavalerie de sa classe, sauf si son profil indique un autre mouvement.
- Il lit la ligne de la Cavalerie de son mode dans la grille des règles d'office (voir *Type*).
- Il n'est jamais *Faible*.
- Chaque touche lui retire 1 PV.

### Classe

La classe donne le nombre de dés que l'unité lance quand elle attaque. Elle se lit à la couleur de son jeton classe/mode.

| Classe | Couleur | Dés |
|---|---|---|
| Légère | {VERT} Vert | 2 |
| Standard | {BLEU} Bleu | 3 |
| Lourde | {ROUGE} Rouge | 4 |

La classe fixe aussi le *Mouvement* de l'unité et son coût en jetons de *Pouvoir* : autant de jetons que de dés.

### Colline

Terrain. Une colline ne freine pas le mouvement.

- **Combat** : une unité sur une colline lance 1 dé de plus quand elle attaque une cible en contrebas, en mêlée comme au tir, riposte comprise. Le bonus disparaît si la cible est elle aussi sur une colline. Une unité qui attaque une cible sur une colline depuis le contrebas lance ses dés normalement.
- **Vue** : une colline bloque la ligne de vue des unités en contrebas.
- **Vue depuis une colline** : une unité sur une colline ignore, pour tracer sa ligne de vue, les unités **adjacentes à elle et en contrebas**. Toute autre unité interposée bloque sa vue normalement, de même que tout terrain qui bloque la vue.
- **Retraite** : une unité qui recule traverse une colline sans s'arrêter.

> **Exemple** — Des Archers de Minas Tirith tiennent une colline, des Guerriers de Minas Tirith amis juste devant eux, en contrebas. Les archers tirent par-dessus leurs Guerriers sur une Bande d'orques à 3 hexagones, avec 1 dé de plus. Mais si des Gardes serpents se tiennent entre les Guerriers et les orques, la ligne de vue est bloquée.

### Commandement

Première étape du tour. Le camp joue sa ou ses cartes de commandement, puis peut dépenser des jetons de *Pouvoir* pour activer des unités supplémentaires.

- En format Escarmouche ou Normal, le camp joue **1 carte** de sa main.
- En format *Épique*, le camp joue **jusqu'à 2 cartes de section**, dont une au plus de sa main et une au plus du *Râtelier*, **ou une seule carte Tactique**, de sa main ou du râtelier. Il ne joue jamais une carte de section et une carte Tactique dans le même tour, ni deux cartes Tactiques.
- Vous pouvez toujours ignorer le texte d'une carte (voir *Ignorer une carte*).

*Voir aussi : Main, Valeur de commandement.*

### Contrôle d'une unité

Quand un camp compte plusieurs joueurs, chacun commande les unités de son camp qui se trouvent dans sa Section **au début du tour**.

- Une unité qui franchit une ligne de Section pendant le tour reste au joueur qui l'a activée jusqu'à la fin du tour, puis passe au joueur de sa nouvelle Section.
- Une unité qui change de Section en reculant passe de même au joueur de sa nouvelle Section au tour suivant.
- Pendant le tour adverse, c'est le joueur de la Section où se trouve l'unité qui la fait reculer, riposter et qui lance son Destin.
- Une unité sur un *Hexagone de frontière* peut être activée par l'un ou l'autre des deux joueurs voisins, jamais par les deux.

### Couronne

Face de dé {DÉ:Couronne}. Elle ne fait rien, sauf pour une unité menée par un *Leader* :

- en attaque comme en riposte, chaque Couronne inflige 1 touche ;
- sur un jet d'[Armure], chaque Couronne annule 1 touche ;
- c'est aussi la face qui sauve un Leader lors d'un jet de *Destin*.

La carte Cri de guerre donne aussi un effet à la Couronne (chapitre *Cartes de commandement*).

### Cours d'eau

Terrain infranchissable. Aucune unité n'y entre ni ne le traverse, en se déplaçant comme en reculant. On ne le franchit que par un *Gué* ou un *Pont*.

- **Vue** : un cours d'eau ne bloque pas la ligne de vue.
- **Retraite** : un cours d'eau bloque la retraite (voir *Retraite*).

### Créature

Pièce sur socle unique, avec un compteur de PV.

- Toute Créature porte d'office [Armure] et [Peur 1], quelle que soit sa classe.
- Elle se déplace comme l'Infanterie de sa classe, sauf si son profil indique un autre mouvement.
- Elle n'est jamais *Faible*.
- Chaque touche lui retire 1 PV.

### Déroute

Une unité qui perd sa dernière figurine, ou son dernier PV, est en déroute : retirez-la du champ de bataille. L'adversaire marque aussitôt 1 point de victoire et prend une médaille.

- La déroute peut venir d'une attaque, d'une riposte ou d'une retraite bloquée.
- Si un Leader menait l'unité, il tente aussitôt de survivre (voir *Destin*). Le point de victoire est marqué dans tous les cas.

### Destin

Valeur d'un *Leader*, de 1 à 4, indiquée sur son profil. Quand une unité menée par un Leader est mise en déroute, l'adversaire marque son point de victoire comme d'habitude, puis le Leader tente de rejoindre une autre unité :

1. **Choisissez une unité de repli** : une unité amie de son peuple, sans Leader, à 3 hexagones ou moins de l'hexagone qu'occupait son unité. S'il n'y en a aucune, le Leader est éliminé, sans jet.
2. **Lancez autant de dés que sa valeur de Destin.** Ces dés ne rapportent pas de Pouvoir.
3. **Au moins une {DÉ:Couronne} Couronne : il est sauvé.** Il rejoint l'unité de repli de votre choix, et sa valeur de Destin baisse de 1 pour le reste de la partie. Sans Couronne, il est éliminé.

- Le Leader sauvé prend la place d'une figurine ordinaire de l'unité qui l'accueille : retirez-en une et posez la sienne. L'unité ne gagne aucun PV. Posez le jeton {LEADER} à côté d'elle. Sur un Char ou une Créature, seul le jeton change de place.
- Un Leader dont le Destin tombe à 0 n'a plus de jet : il est éliminé avec sa prochaine unité.
- Un Leader **universel**, comme son profil le précise, peut rejoindre une unité de n'importe quel peuple de son camp.
- Un Leader éliminé ne rapporte pas de point de victoire, sauf si le scénario en fait un objectif.
- Un Général sauvé reste en jeu : la main de son camp ne change pas.

### Discipline de cohorte

**[Discipline de cohorte]** (badge Faction) : aussitôt après son attaque, l'unité peut se mettre en position défensive. Posez le jeton de position défensive {POSITION} à côté d'elle. Une unité activée qui renonce à attaquer peut prendre la position à l'étape d'attaque.

Tant que le jeton est en place :

- l'unité porte [Armure] et [Inébranlable 1] ;
- elle ne riposte pas.

Retirez le jeton au début de sa prochaine activation, avant qu'elle ne bouge. Il reste en place si l'unité recule.

- Ce [Inébranlable 1] s'additionne aux autres sources (voir *Inébranlable*).
- Une unité qui porte déjà [Armure] n'y gagne que [Inébranlable 1] : deux sources ne donnent pas deux dés par touche.

### Drapeau

Face de dé {DÉ:Drapeau}. Chaque Drapeau fait reculer la cible de 1 hexagone, en mêlée comme au tir (voir *Retraite*). D'autres règles produisent aussi des Drapeaux, comme [Peur].

### Épique

Format des grandes batailles : champ de bataille de 17 × 13 hexagones. Il se joue à deux joueurs, ou à six en *Mode multi-joueurs*. Quel que soit le nombre de joueurs, les règles suivantes s'y appliquent :

- **Le râtelier** : 3 cartes face visible, communes aux deux camps (voir *Râtelier*).
- **Jouer ses cartes** : jusqu'à 2 cartes de section, ou une seule carte Tactique (voir *Commandement*).
- **La valeur de commandement** ne compte que la main, jamais le râtelier (voir *Valeur de commandement*).
- **Ordre direct et Contre-attaque** ont une version Épique (chapitre *Cartes de commandement*).
- **Les Généraux** ne sont pas limités en nombre.

### Faces de dé

Chaque dé a six faces. Le *Mode* de l'unité, rappelé par son jeton, dit quelles faces touchent.

| Face | {MÊLÉE} Mêlée | {DISTANCE} Distance |
|---|---|---|
| {DÉ:ÉpéesCroisées} Épées croisées | 1 touche | — |
| {DÉ:Épée} Épée | 1 touche, sauf si l'unité est Faible | — |
| {DÉ:Arc} Arc | — | 1 touche |
| {DÉ:Drapeau} Drapeau | 1 hexagone de retraite | 1 hexagone de retraite |
| {DÉ:Couronne} Couronne | 1 touche si un Leader mène l'unité | 1 touche si un Leader mène l'unité |
| {DÉ:Pouvoir} Pouvoir | Déclenche la règle de l'unité, s'il y en a une ; 1 touche contre une cible empoisonnée | Déclenche la règle de l'unité, s'il y en a une ; 1 touche contre une cible empoisonnée |

Un tiret signifie que la face ne fait rien. Chaque camp lance ses propres dés : la face Pouvoir porte la Rune de Gandalf sur ceux du Bien, l'Œil de Sauron sur ceux du Mal. C'est la même face, avec le même effet.

*Voir aussi : Archer en mêlée, Couronne, Drapeau, Faible, Pouvoir.*

### Faction

Badge {FACTION} qui donne à une unité une règle propre. Le profil de l'unité, dans le livret Factions, dit laquelle. Les règles de badge Faction sont définies dans ce livret : *Discipline de cohorte*, *Férocité*, *Horde*, *Mercenaire*, *Poison*, *Relance*.

Le badge Faction n'est jamais automatique : le scénario ou la composition d'armée dit quelles unités le portent.

### Faible

Une unité d'Infanterie ou de Cavalerie réduite à une seule figurine est Faible : ses {DÉ:Épée} Épées ne touchent plus en mêlée. Seules ses Épées croisées touchent encore, ainsi que ses Couronnes si un Leader la mène.

- Un Char ou une Créature n'est jamais Faible.
- Une unité de tir n'est pas gênée : elle touche sur Arc.
- Une unité menée par un Leader réduite à la figurine du Leader est Faible elle aussi.

### Férocité

**[Férocité]** (badge Faction) : l'unité peut riposter même si l'attaque qu'elle subit la fait reculer. Elle résout d'abord sa riposte, **puis** recule.

- Elle doit remplir les autres conditions de la riposte : être adjacente à l'attaquant et ne pas être en déroute.
- Elle ne riposte pas contre un attaquant qui porte [Vigilant].

> **Exemple** — Un Éored de cavalier portant [Férocité] subit 2 touches et 1 Drapeau. Il riposte avec ses figurines restantes, puis recule de 1 hexagone.

### Format

Chaque scénario se joue dans l'un des trois formats du jeu.

| Format | Champ de bataille | Généraux par camp | Deck | Score indicatif |
|---|---|---|---|---|
| Escarmouche | 10 × 7 hexagones | 2 au plus | sans Attaque ni En avant | 4 points |
| Normal | 13 × 9 hexagones | 3 au plus | complet | 6 points |
| Épique | 17 × 13 hexagones | sans limite | complet, avec le râtelier | 8 points |

Le score de victoire est toujours fixé par le scénario.

### Général

Statut d'un *Leader*, indiqué sur son profil. Tant qu'un Général est en jeu, la main de son camp compte 1 carte de plus.

- Quand un Général est éliminé, son camp défausse aussitôt une carte de sa main, à son choix, même pendant le tour adverse. La main compte désormais une carte de moins.
- Un Général sauvé par son Destin reste en jeu : la main ne change pas.
- Nombre de Généraux par camp : 2 au plus en Escarmouche, 3 au plus en Normal, sans limite en Épique.

### Gué

Terrain qui permet de franchir un *Cours d'eau*. Une unité qui entre dans un gué s'y arrête. Elle en sort normalement au tour suivant.

- **Combat** : une unité dans un gué lance 2 dés au plus quand elle attaque ou riposte. Celle qui l'attaque depuis la berge lance ses dés normalement. Cette limite s'applique aux dés de l'unité, avant les dés en plus d'une carte ou d'une règle (voir *Plafond de dés*).
- **Vue** : un gué ne bloque pas la ligne de vue.
- **Retraite** : une unité qui recule traverse un gué sans s'arrêter.

### Hexagone

Le champ de bataille est découpé en hexagones. Une unité occupe toujours un hexagone entier, et un hexagone n'accueille jamais qu'une seule unité. Les rares pièces qui en couvrent plusieurs le précisent sur leur profil.

Deux hexagones qui partagent un côté sont adjacents. Toutes les distances se comptent en hexagones.

### Hexagone de frontière

Une ligne de Section peut couper des hexagones en deux au lieu de suivre leurs côtés. Un hexagone ainsi coupé appartient aux deux Sections voisines : une carte de l'une comme de l'autre peut activer l'unité qui s'y trouve.

- Quand un camp compte plusieurs joueurs, chacun des deux joueurs voisins peut l'activer, ou l'acheter avec du Pouvoir.
- Comme toute unité, elle n'est activée qu'une seule fois par tour.

### Horde

**[Horde]** (badge Faction) : tant que l'unité est à pleine santé, sans avoir perdu une seule figurine ni un seul PV, elle lance 1 dé de plus en combat et porte [Inébranlable 1]. Dès sa première perte, ces deux effets disparaissent pour le reste de la partie, sans autre conséquence.

- Le dé en plus vaut en attaque comme en riposte, et compte dans le *Plafond de dés*.
- Ce [Inébranlable 1] s'additionne aux autres sources (voir *Inébranlable*).
- Une touche annulée par l'[Armure] n'est pas une perte.

### Ignorer une carte

Vous pouvez toujours ignorer le texte de la carte que vous jouez, et activer à la place 1 unité de votre choix, n'importe où sur le champ de bataille. La carte est défaussée et remplacée comme d'habitude.

Son texte étant ignoré, la carte ne produit aucun autre effet : un Éclaireur ainsi joué ne fait pas piocher 2 cartes.

### Inébranlable

**[Inébranlable X]** : l'unité peut ignorer jusqu'à X Drapeaux à chaque attaque qu'elle subit, quelle qu'en soit la source : dés, [Peur], effets.

- **C'est un choix.** Son camp décide, Drapeau par Drapeau, d'en ignorer ou non. Il peut préférer laisser l'unité reculer, par exemple pour la dégager.
- **Les sources s'additionnent.** Une figurine avec bannière donne [Inébranlable 1] à son unité, un Leader à son unité et à chaque unité amie adjacente ; [Horde] et [Discipline de cohorte] en donnent aussi. Une unité avec bannière, adjacente à un Leader ami, porte [Inébranlable 2].
- **[Inébranlable ∞]** : l'unité ne recule jamais. Elle ignore tous les Drapeaux.
- Un Drapeau ignoré ne fait rien : il ne cause pas de perte.

### Jeton classe/mode

Jeton posé à côté de chaque unité. Sa couleur rappelle sa *Classe*, son symbole son *Mode* : des épées croisées pour la mêlée, un arc pour le tir. Il suffit à savoir combien de dés lance l'unité et sur quelles faces elle touche.

### Leader

Badge {LEADER}. Un Leader est un personnage nommé qui mène une unité. Sa figurine fait partie de l'unité, et le jeton de badge d'unité posé à côté d'elle le signale.

Un Leader donne à son unité :

- une touche sur chaque {DÉ:Couronne} Couronne, en attaque comme en riposte ;
- si l'unité porte [Armure], l'annulation d'une touche sur chaque Couronne, comme sur un Pouvoir ;
- [Inébranlable 1], pour son unité et pour chaque unité amie adjacente.

Règles du Leader :

- La figurine du Leader est toujours retirée en dernier.
- Une unité n'est jamais menée par plus d'un Leader.
- Un Leader peut mener n'importe quelle unité de son peuple. Quelques unités incluent leur Leader dans leur profil.
- Certains Leaders sont aussi des *Généraux*. Chacun a une valeur de *Destin*.

### Ligne de vue

Pour tirer, une unité doit voir sa cible. Tendez une ligne droite du centre de l'hexagone du tireur au centre de l'hexagone de la cible. Elle est bloquée si elle traverse un hexagone qui contient :

- une autre unité, amie ou ennemie ;
- un terrain qui bloque la vue : bois, colline ou bâtiment.

Précisions :

- L'hexagone du tireur et celui de la cible ne comptent pas : on peut tirer depuis un bois, et sur une unité dans un bois.
- Quand la ligne longe exactement le côté commun à deux hexagones, elle n'est bloquée que si ces deux hexagones la bloquent l'un et l'autre.
- Une unité sur une colline voit par-dessus les unités adjacentes en contrebas (voir *Colline*).
- Cours d'eau, gué, pont et plaine ne bloquent pas la vue.
- Certaines pièces ont leurs propres règles de vue, indiquées sur leur profil.
- La mêlée n'a pas besoin de ligne de vue.

### Main

Les cartes de commandement d'un camp, tenues secrètes : **4 cartes, plus 1 par Général en jeu**, dans tous les formats. Les deux camps piochent dans le même deck.

- À l'étape de pioche, le camp complète sa main pour chaque carte jouée de sa main.
- Quand un Général est éliminé, le camp défausse aussitôt une carte : la main en compte une de moins.
- En *Mode multi-joueurs*, le joueur Centre tient la main et la montre à ses coéquipiers, jamais à l'adversaire.

### Manche

Un tour de chaque camp. Le scénario indique le camp qui ouvre chaque manche.

### Mercenaire

**[Mercenaire]** (badge Faction) : chaque Drapeau qui fait reculer l'unité la fait reculer de **2 hexagones** au lieu d'un.

- Si sa retraite est bloquée, elle perd 1 figurine par hexagone qu'elle n'a pas pu parcourir, donc jusqu'à 2 par Drapeau.
- Les Drapeaux ignorés grâce à [Inébranlable] ne la font pas reculer du tout.

> **Exemple** — Des Pillards de Khand portant [Mercenaire] subissent 1 Drapeau. Ils doivent reculer de 2 hexagones. Le premier est libre, le second est occupé par une unité amie : ils perdent 1 figurine.

### Mobilité

**[Mobilité X]** : juste après avoir attaqué, l'unité peut se déplacer de X hexagones de plus.

- Ce déplacement se fait aussitôt, avant qu'une autre unité attaque.
- Il suit les règles normales du *Mouvement* : il est arrêté par un bois, un gué ou un bâtiment.
- Il vaut aussi après un tir sur une unité adjacente.
- Une unité qui renonce à attaquer n'en profite pas, pas plus qu'une unité qui riposte.
- Une carte qui interdit de se déplacer, comme Pluie de flèches, interdit aussi ce déplacement.
- Portent [Mobilité] d'office : l'Infanterie légère de tir [Mobilité 1], la Cavalerie légère de tir [Mobilité 2], la Cavalerie standard de tir [Mobilité 1].

### Mode

La façon de combattre de l'unité, lue au symbole de son jeton classe/mode.

- {MÊLÉE} **Mêlée** : l'unité attaque une unité ennemie adjacente et touche sur Épées croisées et Épée.
- {DISTANCE} **Distance** : l'unité tire sur une unité ennemie à portée et en ligne de vue, et touche sur Arc. Elle peut aussi tirer sur une unité adjacente, et riposte ainsi.

### Mode multi-joueurs

Le format *Épique* peut se jouer à six, trois joueurs par camp. Chaque joueur commande une Section de son camp : Gauche, Centre ou Droite.

- **Cartes** : le camp ne tient qu'une main, tenue par le joueur Centre, qui la montre à ses deux coéquipiers. Les trois joueurs discutent des cartes à jouer ; le joueur Centre a le dernier mot. Chaque joueur active, déplace et fait combattre ensuite les unités de sa propre Section.
- **Cartes qui activent un nombre limité d'unités n'importe où** (Charge de cavalerie, Assaut d'infanterie, Bannières, Ordre direct, Cri de guerre, Ignorer une carte) : les joueurs se répartissent les activations à la discussion. S'ils ne s'entendent pas, le joueur Centre tranche.
- **Pouvoir** : la réserve est commune au camp. Chaque joueur peut acheter jusqu'à 2 unités de sa propre Section ; si les joueurs ne s'entendent pas sur l'usage de la réserve, le joueur Centre tranche.
- **Contrôle** : voir *Contrôle d'une unité* et *Hexagone de frontière*.

### Mouvement

Une unité ne bouge que si elle est activée. À l'étape de mouvement, son camp déplace ses unités activées une à une, chacune terminant son déplacement avant que la suivante commence. Toutes les unités se déplacent avant la première attaque.

| | {VERT} Légère | {BLEU} Standard | {ROUGE} Lourde |
|---|---|---|---|
| Infanterie | 2, puis attaque | 2, puis attaque | 1 puis attaque, ou 2 sans attaquer |
| Cavalerie | 4, puis attaque | 3, puis attaque | 2 puis attaque, ou 3 sans attaquer |

- Un Char se déplace comme la Cavalerie de sa classe, une Créature comme l'Infanterie de sa classe, sauf mouvement propre indiqué sur le profil.
- Une unité peut toujours se déplacer de moins, ou rester sur place.
- **Bouger ou frapper** : une unité rouge qui va au bout de sa plus longue distance ne peut plus attaquer ce tour. Rien à annoncer : c'est la distance parcourue qui décide.
- **Ce qui arrête** : une unité n'entre jamais dans un hexagone occupé et ne le traverse pas, que l'unité qui s'y trouve soit amie ou ennemie. Elle ne quitte jamais le champ de bataille. Un bois, un gué ou un bâtiment l'arrête ; un cours d'eau lui barre le passage.
- **Rien d'autre ne gêne** : une unité peut passer à côté d'une unité ennemie, et s'arrêter contre elle pour l'attaquer.
- Les Sections n'ont aucun effet sur le mouvement : une unité peut franchir une ligne de Section (voir *Contrôle d'une unité*).
- Une carte peut changer le mouvement des unités qu'elle active : son texte l'emporte.
- Une unité qui a attaqué ne se déplace plus, sauf par une *Avance*, une *Poursuite* ou [Mobilité].

### Objectif

Hexagone ou but fixé par le scénario, qui rapporte des points de victoire.

- **Objectif acquis** : rapporte ses points une fois pour toutes, comme éliminer une unité précise.
- **Objectif d'occupation** : temporaire. À chaque étape des points de victoire, quel que soit le camp qui joue, sa médaille va au camp dont une unité occupe l'hexagone. S'il est vide, elle ne va à personne.

### Peuple

Rohan, Gondor, Mordor, Harad, Khand, Orientaux… Chaque peuple a son chapitre dans le livret Factions. Un camp en réunit souvent plusieurs.

### Peur

**[Peur X]** : chaque {DÉ:Pouvoir} Pouvoir obtenu par l'unité quand elle attaque ou riposte compte comme X Drapeaux de plus contre la cible. La Peur fait reculer, elle ne touche pas.

- Toute *Créature* porte [Peur 1] d'office. Si son profil indique une valeur plus haute, comme [Peur 2], celle-ci la remplace.
- La cible peut ignorer ces Drapeaux grâce à [Inébranlable], comme ceux des dés.
- Chaque Pouvoir rapporte aussi son jeton de Pouvoir, sauf en riposte.

### Plafond de dés

Pour savoir combien de dés lance une unité, comptez dans cet ordre :

1. **Les dés de l'unité** : 2, 3 ou 4 selon sa classe ;
2. **les limites du terrain** : 2 dés au plus si l'attaquant ou sa cible est dans un bois, ou si l'attaquant est dans un gué ;
3. **les dés en plus** d'une carte, d'une colline ou d'une règle comme [Horde] ;
4. **jamais plus de 6 dés au total.**

> **Exemple** — Une Bande d'orques {BLEU} portant [Horde], à pleine santé, activée par Ordre direct, attaque depuis un bois : 3 dés, ramenés à 2 par le bois, puis 1 pour [Horde] et 1 pour la carte, soit 4 dés.

### Plaine

Hexagone sans terrain. Il n'a aucun effet.

### Poison

**[Poison]** (badge Faction) : quand l'unité attaque ou riposte, chaque {DÉ:Pouvoir} Pouvoir qu'elle obtient empoisonne sa cible. Posez le jeton Empoisonnée {POISON} à côté de la cible. Ce Pouvoir ne touche pas.

**Cible empoisonnée.** Toute attaque contre une unité empoisonnée touche aussi sur {DÉ:Pouvoir} Pouvoir, que l'attaquant porte [Poison] ou non.

- Le jeton reste en place jusqu'à la déroute de l'unité. Une unité n'est empoisonnée qu'une fois : un second jeton ne change rien.
- Une riposte contre une unité empoisonnée touche aussi sur Pouvoir.
- Les touches sur Pouvoir s'ajoutent aux autres : [Protection] et [Armure] s'appliquent.
- Sur une cible empoisonnée, le Pouvoir touche **et** déclenche la règle de l'attaquant, comme [Peur].
- Chaque Pouvoir rapporte aussi son jeton de Pouvoir, sauf en riposte.

> **Exemple** — Des Archers du Harad portant [Poison] tirent sur des Guerriers de Minas Tirith : Arc, Pouvoir. Une touche, et les Guerriers sont empoisonnés. Au tour suivant, des Lanciers du Harad sans [Poison] les attaquent : Épée, Pouvoir, Drapeau. Deux touches, car la cible est empoisonnée.

### Pont

Terrain qui permet de franchir un *Cours d'eau*. Un pont ne freine pas le mouvement, ne change rien au combat et ne bloque pas la vue. Comme tout hexagone, il n'accueille qu'une unité.

### Portée

Distance de tir en hexagones, sans compter celui du tireur : une unité adjacente est à 1 hexagone.

- **Infanterie** : 1 à 4 hexagones.
- **Cavalerie** : 1 à 3 hexagones.

### Poursuite

**[Poursuite X]** : quand l'unité, en mêlée, met sa cible en déroute ou la fait reculer, elle peut poursuivre au lieu d'avancer.

1. Elle se déplace de 1 à X hexagones, en entrant d'abord dans l'hexagone libéré. Ce déplacement suit les règles normales du *Mouvement* : un bois, un gué ou un bâtiment l'arrête.
2. Elle attaque une unité ennemie adjacente, la même ou une autre.

- L'attaque de poursuite est une attaque complète : elle rapporte du Pouvoir, sa cible peut riposter, et l'attaquant peut ensuite avancer.
- Une unité ne poursuit qu'une fois par tour.
- La poursuite est un choix : l'unité peut aussi avancer, ou rester sur place.
- Une riposte ne permet jamais de poursuivre.
- Portent [Poursuite] d'office : la Cavalerie de mêlée légère et standard [Poursuite 2], la Cavalerie de mêlée lourde [Poursuite 1]. Les Chars aussi, selon leur classe.

### Pouvoir

Le mot désigne trois choses liées.

**La face {DÉ:Pouvoir} Pouvoir.** Elle déclenche la règle de l'unité qui se déclenche sur Pouvoir, comme [Peur] ou [Poison]. Contre une cible empoisonnée, elle touche aussi (voir *Poison*). Sinon, elle ne fait rien. Sur un jet d'[Armure], elle annule une touche.

**Le jeton de Pouvoir** {POUVOIR:Bien} {POUVOIR:Mal}. Chaque face Pouvoir obtenue quand vous attaquez rapporte 1 jeton à la réserve de votre camp, que la face déclenche une règle ou non.

- On compte les faces Pouvoir **après les relances** : un Pouvoir relancé ne rapporte rien, un dé relancé qui donne Pouvoir rapporte son jeton.
- L'attaque de poursuite et chacune des attaques données par une carte rapportent du Pouvoir.
- Ne rapportent rien : les ripostes, les jets d'[Armure], les jets de Destin, et le lancer de la carte Cri de guerre.
- Vous ne gagnez donc du Pouvoir que pendant votre propre tour.

**La réserve de Pouvoir.** Chaque camp tient une réserve commune de jetons, sans plafond : les jetons non dépensés se gardent.

- **Gain** : les jetons des attaques, plus 2 jetons à l'étape de Pouvoir, à la fin de chaque tour du camp.
- **Dépense** : à l'étape de commandement, après avoir joué la ou les cartes, le camp peut activer des unités supplémentaires. Chacune coûte autant de jetons qu'elle lance de dés : {VERT} 2, {BLEU} 3, {ROUGE} 4.
- Un camp achète ainsi 2 unités au plus par tour ; en *Mode multi-joueurs*, 2 au plus par joueur, chacun dans sa propre Section.
- Une unité achetée ne peut pas être une unité déjà activée par la carte.

### Profil

Fiche d'une unité, dans le livret Factions. Il donne son *Type*, sa *Classe* et son *Mode*, son coût, ses badges et, pour quelques pièces uniques, ses règles propres. En jeu, le jeton classe/mode suffit : on ne rouvre le profil que pour une règle particulière.

### Protection

**[Protection]** : l'unité ignore 1 touche à chaque attaque qu'elle subit.

- Elle s'applique avant l'[Armure], qui ne se lance que sur les touches qui restent.
- Elle vaut contre la mêlée comme contre le tir.
- Elle ne s'applique pas aux pertes d'une retraite bloquée.
- Elle n'est pas cumulable : deux sources n'en font ignorer qu'une.
- Une unité dans un *Bâtiment* porte [Protection].

### PV

Points de vie. Chaque figurine d'Infanterie ou de Cavalerie vaut 1 PV. Un Char ou une Créature a un compteur de PV. Chaque *Touche* retire 1 figurine ou 1 PV.

### Râtelier

En format *Épique*, rangée de 3 cartes de commandement posées face visible à côté de la pioche, communes aux deux camps. Avant le premier tour, retournez-y les 3 premières cartes de la pioche.

- **Jouer** : un camp peut y prendre 1 carte de section, en plus de 1 carte de section de sa main, ou y prendre sa seule carte Tactique du tour.
- **Repiocher** : à l'étape de pioche, chaque carte jouée est remplacée là d'où elle vient. Une carte prise au râtelier est remplacée par la première carte de la pioche ; la main du camp ne change pas.
- **Valeur de commandement** : les cartes du râtelier n'y comptent jamais, même celle que vous jouez.
- **Éclaireur pris au râtelier** : au lieu de retourner 1 carte, retournez-en 2 ; placez-en une dans le râtelier et défaussez l'autre.
- **Râtelier entièrement Tactique** : si, une fois reconstitué, le râtelier ne compte que des cartes Tactiques, défaussez ses 3 cartes et retournez-en 3 nouvelles. Recommencez jusqu'à ce qu'il compte au moins une carte de section.
- **Pioche vide** : mélangez la défausse pour former une nouvelle pioche.

### Relance

**[Relance X]** : après le lancer, l'unité peut relancer jusqu'à X dés de son choix, en attaque comme en riposte. Chaque dé n'est relancé qu'une fois, et on garde le nouveau résultat.

- Les relances se font avant de compter touches et Drapeaux.
- Les jetons de Pouvoir se comptent sur le résultat final (voir *Pouvoir*).
- [Relance] ne s'applique pas aux jets d'[Armure] ni de Destin.

### Retraite

Chaque {DÉ:Drapeau} Drapeau fait reculer la cible survivante de 1 hexagone. La retraite se résout après les pertes.

**Direction.** C'est le camp de l'unité qui la déplace. À chaque hexagone, il choisit un hexagone adjacent libre, **strictement plus proche de son bord** que celui qu'elle quitte. D'où que vienne l'attaque, une unité recule toujours vers son bord. S'il a le choix entre plusieurs hexagones, il choisit librement.

**Terrain.** Le terrain ne gêne pas une unité qui recule : elle traverse bois, gués, collines, ponts et bâtiments sans s'arrêter. Seul le cours d'eau l'arrête.

**Retraite bloquée.** Quand aucun hexagone libre ne rapproche l'unité de son bord, parce que le bord, un cours d'eau ou d'autres unités, amies comme ennemies, lui barrent la route, sa retraite est bloquée. Elle perd 1 figurine, ou 1 PV, par hexagone qu'elle n'a pas pu parcourir.

- Ni l'[Armure] ni la [Protection] ne sauvent ces pertes.
- Une unité déjà sur son propre bord a sa retraite bloquée dès le premier Drapeau.
- Une unité peut parcourir une partie de sa retraite, puis être bloquée : elle ne perd que pour les hexagones restants.
- Ces pertes peuvent mettre l'unité en déroute. L'attaquant marque alors son point de victoire, et un Leader tente son Destin comme d'habitude.
- Une unité dont la retraite a été bloquée n'a pas bougé : si elle survit, elle peut riposter.

**Cas particuliers.**

- **Encerclée** : une unité entourée au point qu'aucun hexagone ne la rapproche de son bord subit toute sa retraite en pertes.
- **Sources multiples** : les Drapeaux des dés et ceux d'une règle comme [Peur] s'additionnent. [Inébranlable] s'applique au total.
- **[Mercenaire]** : chaque Drapeau fait reculer de 2 hexagones (voir *Mercenaire*).
- **Changer de Section en reculant** : l'unité passe au joueur de sa nouvelle Section au tour suivant (voir *Contrôle d'une unité*).
- **Après la retraite** : l'unité qui a reculé ne riposte pas, sauf [Férocité]. L'attaquant de mêlée peut avancer ou poursuivre.

### Riposte

Une fois les pertes et la retraite réglées, la cible d'une attaque peut riposter si elle remplit trois conditions :

- elle est adjacente à l'attaquant ;
- elle n'a pas bougé ;
- elle n'est pas en déroute.

Elle attaque alors son assaillant avec tous ses dés, comme pour une attaque normale : terrain, faces, règles sur Pouvoir, [Armure] et retraite s'appliquent.

- Une unité de tir riposte aussi, puisqu'elle peut tirer sur une unité adjacente.
- Une unité dont la retraite a été bloquée n'a pas bougé : si elle survit, elle peut riposter.
- Une riposte ne rapporte pas de Pouvoir.
- L'unité qui riposte ne peut ni avancer, ni poursuivre, ni décrocher avec [Mobilité].
- On ne riposte jamais à une riposte.
- La riposte est un choix : la cible peut y renoncer.
- **Exceptions** : [Férocité] permet de riposter avant de reculer ; on ne riposte pas contre une unité qui porte [Vigilant] ; une unité en position défensive ([Discipline de cohorte]) ne riposte pas.

### Section

Deux lignes découpent le champ de bataille en trois Sections : Gauche, Centre et Droite. Les cartes de section s'y réfèrent.

- Chaque camp nomme ses Sections depuis son propre bord : votre Gauche est à votre gauche quand vous regardez le champ de bataille depuis votre bord. Elle fait face à la Droite de l'adversaire.
- Une unité appartient à la Section où elle se trouve. Les Sections n'ont aucun effet sur le mouvement.
- Voir aussi *Hexagone de frontière*, *Contrôle d'une unité*.

### Terrain

Un hexagone peut porter du terrain : *Bois*, *Colline*, *Cours d'eau*, *Gué*, *Pont* ou *Bâtiment*. Un hexagone sans terrain est une *Plaine*. Le scénario indique où le placer. Tableau récapitulatif en fin de livret.

### Touche

Chaque touche retire 1 figurine d'une unité, ou 1 PV du compteur d'un Char ou d'une Créature, quelle que soit la cible. Une unité ne perd jamais plus que ce qu'il lui reste.

### Tour

Le tour d'un seul camp. Il suit toujours sept étapes, en deux phases.

**Phase principale**

1. **Commandement** : jouer sa ou ses cartes, puis dépenser éventuellement du Pouvoir (voir *Commandement*).
2. **Ordre** : désigner les unités activées.
3. **Mouvement** : déplacer les unités activées, une à une (voir *Mouvement*).
4. **Attaque** : les unités activées attaquent, une à une (voir *Attaque*).

**Phase de bilan**

5. **Points de victoire** : compter les objectifs d'occupation (voir *Objectif*).
6. **Pioche** : défausser les cartes jouées et les remplacer (voir *Main*, *Râtelier*).
7. **Pouvoir** : ajouter 2 jetons à la réserve du camp.

### Type

Le type d'une unité vient de son profil.

| Type | Composition | Points de vie |
|---|---|---|
| Infanterie | 4 figurines à pied | 1 par figurine |
| Cavalerie | 3 figurines montées | 1 par figurine |
| Char | 1 pièce | sur un compteur |
| Créature | 1 pièce | sur un compteur |

Un profil peut déroger à la composition. Le type, la classe et le mode donnent à l'unité des règles d'office, qui ne sont pas écrites sur son profil :

| Type et mode | {VERT} Légère | {BLEU} Standard | {ROUGE} Lourde |
|---|---|---|---|
| Infanterie {MÊLÉE} | — | — | [Armure] |
| Infanterie {DISTANCE} | [Mobilité 1] | — | n'existe pas |
| Cavalerie {MÊLÉE} | [Poursuite 2] | [Poursuite 2] | [Poursuite 1], [Armure] |
| Cavalerie {DISTANCE} | [Mobilité 2] | [Mobilité 1] | n'existe pas |
| Créature | [Armure] et [Peur 1], quelle que soit sa classe | | |

Un Char lit la ligne de la Cavalerie de son mode. Un profil ne rappelle l'une de ces règles que s'il va au-delà.

### Unité

Groupe de figurines qui occupent le même hexagone et agissent ensemble : c'est elle qu'on active, qu'on déplace, qui attaque et qui subit des touches. Un Char ou une Créature forme une unité à lui seul.

### Valeur de commandement

Nombre de cartes que votre camp a en main quand vous jouez, carte jouée comprise. Beaucoup de cartes activent « autant d'unités que votre valeur de commandement ».

- En Épique, les cartes du râtelier n'y comptent jamais, même celle que vous jouez. Une carte prise au râtelier se calcule donc sur le nombre de cartes en main.
- Quand vous jouez 2 cartes de section, dont une de votre main, celle-ci compte dans la valeur.

### Victoire

Chaque scénario fixe ses conditions de victoire. Sauf indication contraire :

- **chaque unité ennemie mise en déroute** rapporte 1 point de victoire, dès qu'elle est retirée ;
- **les objectifs** du scénario rapportent aussi des points (voir *Objectif*) ;
- **dès qu'un camp atteint le score** fixé par le scénario, il gagne la partie, même au milieu d'un tour.

Certains scénarios s'écartent de ce modèle, par exemple en s'arrêtant sur une limite de temps.

### Vigilant

**[Vigilant]** : la cible d'une attaque de cette unité ne peut pas riposter, quelle que soit l'issue de l'attaque, en mêlée comme au tir.

### Vol

**[Vol X]** : à son activation, l'unité peut se déplacer jusqu'à X hexagones en survolant tout ce qui se trouve sur son trajet : unités, amies ou ennemies, et terrain, cours d'eau compris.

- Elle termine son déplacement sur un hexagone libre, jamais dans un cours d'eau.
- Le terrain où elle s'arrête s'applique normalement au combat.
- Elle peut attaquer après son vol, quelle que soit sa classe.
- [Vol] ne change rien à la retraite : l'unité recule comme toute autre.

---

## Cartes de commandement

Le deck compte 60 cartes : 42 cartes de section et 18 cartes Tactiques. En Escarmouche, il ne contient ni les cartes Attaque ni En avant, soit 45 cartes. Le nombre d'exemplaires de chaque carte figure entre parenthèses.

Règles qui valent pour toutes les cartes :

- « N'importe où » signifie dans n'importe quelle Section.
- Vous pouvez toujours ignorer le texte d'une carte (voir *Ignorer une carte*).
- « Jusqu'à la fin du tour » : le dé en plus vaut pour toutes les attaques des unités activées pendant ce tour, poursuite comprise.
- En *Mode multi-joueurs*, chaque joueur résout l'activation de ses propres unités ; les cartes qui activent un nombre limité d'unités n'importe où se répartissent à la discussion, le joueur Centre tranche.

### Cartes de section

**Éclaireur Gauche (2), Éclaireur Centre (2), Éclaireur Droite (2)**
Activez 1 unité dans la Section indiquée. À l'étape de pioche, piochez 2 cartes au lieu d'une et défaussez-en 1.
*En Épique, pris au râtelier : retournez 2 cartes, placez-en une dans le râtelier et défaussez l'autre.*

**Patrouille Gauche (3), Patrouille Centre (5), Patrouille Droite (3)**
Activez 2 unités dans la Section indiquée.

**Attaque Gauche (4), Attaque Centre (5), Attaque Droite (4)**
Activez 3 unités dans la Section indiquée.
*Absente en Escarmouche.*

**Percée Gauche (2), Percée Centre (2), Percée Droite (2)**
Activez dans la Section indiquée autant d'unités que votre valeur de commandement.

**En marche (2)**
Activez 1 unité dans chacune de vos trois Sections.

**En avant (2)**
Activez 2 unités dans chacune de vos trois Sections.
*Absente en Escarmouche.*

**Encerclement (2)**
Activez 2 unités dans votre Section Gauche et 2 unités dans votre Section Droite.

### Cartes Tactiques

**Bannières vertes (2), Bannières bleues (2), Bannières rouges (2)**
Activez autant d'unités de la classe indiquée que votre valeur de commandement, n'importe où. Si vous n'avez aucune unité de cette classe, activez 1 unité de votre choix.

**Charge de cavalerie (3)**
Activez autant d'unités de Cavalerie que votre valeur de commandement, n'importe où. Elles combattent en mêlée avec 1 dé de plus jusqu'à la fin du tour. Les unités rouges ainsi activées peuvent se déplacer de 3 hexagones et attaquer quand même. Elles ne peuvent pas tirer. Si vous n'avez aucune unité de Cavalerie, activez 1 unité de votre choix.
*Les Chars comptent comme de la Cavalerie.*

**Assaut d'infanterie (2)**
Activez autant d'unités d'Infanterie que votre valeur de commandement, n'importe où, à condition qu'elles forment un groupe d'unités adjacentes les unes aux autres. Elles peuvent se déplacer de 2 hexagones puis attaquer en mêlée, même rouges. Elles ne peuvent pas tirer. Si vous n'avez aucune unité d'Infanterie, activez 1 unité de votre choix.

**Pluie de flèches (2)**
Activez toutes vos unités de tir, n'importe où. Elles ne se déplacent pas, mais tirent deux fois ce tour, sur la même cible ou sur une autre, jamais sur une unité adjacente. Si vous n'avez aucune unité de tir, activez 1 unité de votre choix.
*Ne se déplaçant pas, elles ne décrochent pas avec [Mobilité]. Chaque tir rapporte son Pouvoir.*

**Ordre direct (2)**
Activez 1 unité de votre choix, n'importe où. Elle combat avec 1 dé de plus jusqu'à la fin du tour.
*En Épique : activez 1 unité par tranche de 2 cartes dans votre main, arrondi au supérieur — 3 unités avec une main de 5 ou 6 cartes, 4 avec une main de 7 ou 8. Chacune combat avec 1 dé de plus.*

**Contre-attaque (2)**
Jouez le même ordre que la carte que l'adversaire vient de jouer. Si c'est une carte de section, la Gauche devient la Droite et inversement ; le Centre reste le Centre. Vous activez ainsi vos unités qui font face à celles qu'il a activées. Si c'est une carte Tactique, appliquez le même effet.
*En Épique, si l'adversaire vient de jouer 2 cartes de section, Contre-attaque n'en reprend qu'une, à votre choix.*

**Cri de guerre (1)**
Lancez autant de dés que votre valeur de commandement. Pour chaque Épées croisées ou Épée, activez 1 unité de mêlée ; pour chaque Arc, 1 unité de tir ; pour chaque Couronne, 1 unité de votre choix. Drapeau et Pouvoir n'activent rien. Les unités activées combattent avec 1 dé de plus jusqu'à la fin du tour. Puis mélangez la défausse avec la pioche.
*Ce lancer n'est pas une attaque : ses Pouvoirs ne rapportent pas de jeton.*

---

## Tableau du terrain

| Terrain | Mouvement | Combat | Vue | Retraite |
|---|---|---|---|---|
| Plaine | Libre | Normal | Ne bloque pas | Libre |
| Bois | L'unité qui entre s'arrête | 2 dés au plus si l'attaquant **ou** la cible s'y trouve | Bloque | Libre |
| Colline | Libre | +1 dé contre une cible en contrebas | Bloque ; depuis la colline, on voit par-dessus les unités adjacentes en contrebas | Libre |
| Cours d'eau | Infranchissable | — | Ne bloque pas | Bloquée |
| Gué | L'unité qui entre s'arrête | 2 dés au plus pour l'unité qui s'y trouve | Ne bloque pas | Libre |
| Pont | Libre | Normal | Ne bloque pas | Libre |
| Bâtiment | L'unité qui entre s'arrête | [Protection] pour l'unité qui s'y trouve : ignore 1 touche par attaque | Bloque | Libre |

Les limites de dés du bois et du gué s'appliquent aux dés de l'unité, avant les dés en plus d'une carte ou d'une règle. Jamais plus de 6 dés.
