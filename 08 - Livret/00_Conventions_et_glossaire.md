---
projet: "Batailles de la Terre du Milieu"
type: "livret"
phase: "P14"
statut: "en-cours"
date_maj: "2026-09-27"
tags: [BdTdM, type/livret]
version: "0.8"
---

# Corpus joueur — conventions et glossaire

> Document de travail commun aux quatre livrets. Il n'est pas destiné à l'impression : il fixe la façon d'écrire, pour que les quatre livrets parlent la même langue. Décisions de référence : D144 à D146, D151 ([[Document_de_cadrage]] §8).

---

## 1. Les quatre livrets

| Livret | Tâche | Rôle | Lecture |
|---|---|---|---|
| **Livret de règles** — `Livret_de_regles.md` | P14a | Apprendre à jouer, sur le modèle FFG *Learn to Play*. ~12 pages. | Linéaire, une fois, jamais rouvert en jeu |
| **Livret de référence** | P14b | Tout le vocabulaire générique : mots-clés, intrinsèques, règles de badge Faction, cas limites, texte des cartes. Indépendant de tout roster et de tout scénario. | Consultation à la table, entrées alphabétiques |
| **Livret Factions** | P14d | Un chapitre par peuple : identité, profils d'unités avec leur coût, badges Faction disponibles, Leaders nommés (Général, Destin), signatures écrites en entier. | Préparation d'une bataille, consultation |
| **Livret de scénario** — Pelennor | P14c | Contexte fidèle au texte de Tolkien, carte, hexagones de frontière, ordre de bataille (unités nommées, sans profil), déploiement, règles propres, conditions de victoire. | Mise en place |

## 2. Frontières — qui dit quoi

- **Une règle n'a qu'une seule définition**, dans le livret où elle est définie. Les autres livrets y renvoient.
- **Livret de règles** : tout ce qu'il faut pour jouer des unités standard — taxonomie (classe, type, mode), intrinsèques, badge **Leader** (Général, Destin), figurine avec bannière, réserve de Pouvoir, format Épique, terrain en version courte, **hexagones de frontière**, y compris à plusieurs joueurs par camp (chapitre 2, D151). Le badge Faction y est seulement annoncé : « il donne une règle propre à l'unité, indiquée sur son profil ».
- **Livret de référence** : définitions de toutes les règles entre crochets hors signatures — socle générique **et** règles de badge Faction ([Férocité], [Horde], [Poison], [Mercenaire], [Discipline de cohorte]…) ; cas limites (obstacles de retraite, transfert de contrôle) ; texte des cartes de commandement ; terrain complet.
- **Livret Factions** : indique **qui porte** une règle de badge Faction, sans la redéfinir. Seules les **signatures** (Mûmakil, Roi-Sorcier, Compagnie Grise…) y sont écrites en entier.
- **Livret de scénario** : ce qui n'existe que dans cette bataille. Les unités y sont nommées, leurs profils sont dans le livret Factions.

## 3. Règles d'écriture

- **Vouvoiement**, phrases courtes, présent de l'indicatif.
- **Aucun numéro D, aucune note de design, aucun historique** (« modifié après playtest », « anciennement »…). Le livret décrit le jeu tel qu'il est ; les justifications restent dans le corpus de conception.
- **Une règle est expliquée là où elle se déclenche en jeu**, avec au besoin un renvoi d'une ligne ailleurs :
  - Réserve de Pouvoir : règle complète au chapitre 5 (commandement) ; rappel au chapitre 7 au moment du lancer ; spécificités à trois joueurs au chapitre 10.
  - [Armure] et plafond de 6 dés : chapitre 7 (combat). Le chapitre 3 annonce seulement « rouge = armuré ».
  - Grille des intrinsèques : une seule fois, au chapitre 3 ; [Mobilité] expliquée au chapitre 6, [Poursuite] au chapitre 7.
- **Renvois** vers un autre livret par **nom d'entrée**, jamais par numéro de paragraphe : « voir *Armure* dans le livret de référence ».
- **Faces de dé** : toujours par leur nom mécanique (Épées croisées, Épée, Arc, Drapeau, Couronne, Pouvoir). La Rune de Gandalf et l'Œil de Sauron sont présentés une seule fois, au chapitre 1.
- **Nombres** : en chiffres pour les valeurs de jeu (2 dés, 3 hexagones, 1 touche), en lettres dans le récit.
- **Aucune quantité de matériel** dans le livret de règles, qui reste valable pour toute bataille : ce qu'il faut sortir de la boîte est indiqué par le livret de scénario.

### Encadrés

Deux encadrés seulement, en blockquote Markdown (conversion ODT propre) :

```
> **Exemple** — Des Chevaliers de Dol Amroth chargent…

> **À retenir** — Une unité coûte autant de points qu'elle lance de dés.
```

Chaque chapitre du livret de règles se termine par **un seul** encadré « À retenir », d'une phrase.

### Marqueurs de pictos

Pas d'emoji dans les livrets : ils passent mal dans l'ODT puis dans Scribus. On écrit un marqueur entre accolades, remplacé par l'icône en rechercher-remplacer à la mise en page.

| Marqueur | Icône |
|---|---|
| `{VERT}` `{BLEU}` `{ROUGE}` | Pastille de classe |
| `{MÊLÉE}` `{DISTANCE}` | Symbole du jeton classe/mode |
| `{DÉ:ÉpéesCroisées}` `{DÉ:Épée}` `{DÉ:Arc}` `{DÉ:Drapeau}` `{DÉ:Couronne}` `{DÉ:Pouvoir}` | Face de dé |
| `{LEADER}` | Jeton de badge d'unité Leader (couronne) |
| `{FACTION}` | Jeton de badge d'unité Faction |
| `{POUVOIR:Bien}` `{POUVOIR:Mal}` | Jeton de Pouvoir (Rune de Gandalf / Œil de Sauron) |

### Marqueurs d'illustration

Une illustration à produire s'écrit sur sa propre ligne, à l'endroit où elle doit apparaître : `{ILLUS:nom-court — description de ce qu'elle montre}`. Le nom court sert de nom de fichier dans `06 - Images/` ; la description est le cahier des charges de l'image et disparaît à la mise en page.

---

## 4. Glossaire figé

Termes employés dans les quatre livrets. La colonne « Éviter » liste les synonymes à ne jamais utiliser, même par souci de style.

| Terme | Sens | Éviter |
|---|---|---|
| **Activation**, **activer** | Mettre une unité en action, par une carte ou en dépensant du Pouvoir. Une unité non activée ne bouge ni ne combat. | « ordonner », « ordre » (sauf nom de l'étape d'ordre, et de la carte Ordre direct) |
| **Arc** | Face de dé : 1 touche en mode distance. Même symbole que le jeton des unités de tir, qui ne lisent que cette face. | « Cible » (le mot *cible* désigne l'unité visée) |
| **Badge** | Jeton de badge d'unité posé sur le socle, qui donne une règle à l'unité : Leader ou Faction. | « marqueur », « option » |
| **Bannière** | Figurine avec bannière dans une unité : l'unité gagne [Inébranlable 1]. Ce n'est pas un badge. | « badge Bannière », « étendard » comme nom de règle ; jamais « Drapeau » |
| **Bord** | Le bord du champ de bataille du côté d'un camp. Les Sections se nomment depuis lui ; les retraites se font vers lui. | « ligne de base », « côté » |
| **Camp** | Bien ou Mal. | « alliance », « armée » |
| **Carte de section** | Carte qui active des unités d'une ou plusieurs Sections. | « ordre » |
| **Carte Tactique** | Carte qui active selon un autre critère (type, classe…). | « carte spéciale » |
| **Champ de bataille** | Le tapis hexagonal. | « plateau », « table », « carte » (sauf carte à jouer) |
| **Char** | Pièce sur socle unique avec compteur de PV, qui compte comme Cavalerie pour tout le reste. | « chariot » |
| **Classe** | Légère / Standard / Lourde, lue à la couleur du jeton : 2 / 3 / 4 dés. | « rang », « niveau » |
| **Contre-attaque** | **Uniquement** la carte Tactique qui rejoue la carte que l'adversaire vient de jouer. | pour la réaction d'une unité attaquée (dire « riposte ») |
| **Créature** | Pièce sur socle unique avec compteur de PV, [Armure] et [Peur 1] intrinsèques ; jamais Faible. | « monstre », « bête » |
| **Déroute** | Élimination d'une unité ; rapporte 1 point de victoire à l'adversaire. | « destruction » |
| **Destin** | Valeur d'un Leader : nombre de dés lancés pour le sauver quand son unité est éliminée (une Couronne suffit). | « chance » |
| **Drapeau** | Face de dé : 1 hexagone de retraite. | « bannière », « étendard » |
| **Faction** | **Uniquement** le badge (jeton de badge d'unité) qui donne une règle propre à une unité, indiquée sur son profil. | pour désigner un peuple |
| **Faible** | Infanterie ou Cavalerie réduite à une figurine : ses Épées ne touchent plus en mêlée. | « blessé » |
| **Général** | Statut d'un Leader : +1 carte dans la main du camp tant qu'il vit. Au plus 2 par camp en Escarmouche, 3 en Normal, sans limite en Épique. | « chef », « commandant » |
| **Jeton classe/mode** | Jeton de 20 mm : couleur = classe, symbole = mode. | « token » |
| **Hexagone de frontière** | Hexagone coupé par une limite de Section : il appartient aux deux Sections voisines. | « hexagone partagé » |
| **Leader** | Badge (jeton de badge d'unité à couronne) : touche aussi sur Couronne, [Inébranlable 1] pour son unité et les unités amies adjacentes. | « héros » |
| **Main** | Cartes du camp : 4 + 1 par Général vivant, dans tous les formats. Tenue par le joueur Centre en Épique. | — |
| **Manche** | Un tour de chaque camp. | « tour de jeu » |
| **Mode** | Mêlée ou distance, lu au symbole du jeton. | « type d'attaque » |
| **Objectif** | Hexagone ou but fixé par le scénario, qui rapporte des points de victoire. Un objectif **d'occupation** est temporaire : sa médaille va, à chaque étape des points de victoire, au camp qui occupe l'hexagone. | « point de contrôle » |
| **Peuple** | Rohan, Gondor, Mordor, Harad, Khand, Orientaux. | « faction », « race » |
| **Plateau** | Plateau de mouvement : élément pratique de table, sans valeur de règle. Les livrets n'en parlent pas. | pour désigner le champ de bataille ; comme source d'une règle |
| **Pouvoir** | Face de dé portant la Rune de Gandalf (Bien) ou l'Œil de Sauron (Mal) — même face, même mécanique. Déclenche la règle spéciale de l'unité ; sur un jet d'attaque, rapporte 1 jeton de Pouvoir. Désigne aussi la **réserve** commune du camp, en jetons de Pouvoir, dépensée pour activer des unités supplémentaires. | « Arcane », « Espoir », « Désespoir », « magie », « mana » |
| **PV** | Points de vie : une figurine en Infanterie et Cavalerie, un compteur pour Chars et Créatures. | — |
| **Râtelier** | Les 3 cartes visibles communes aux deux camps, en format Épique. | « rivière » |
| **Retraite**, **reculer** | Déplacement forcé par les Drapeaux, toujours vers son propre bord. | « fuite », « déroute » |
| **Riposte**, **riposter** | Réaction d'une unité attaquée, adjacente, qui n'a ni reculé ni été éliminée : elle attaque à son tour son assaillant. | « contre-attaque », « contre-attaquer » |
| **Section** | Gauche, Centre ou Droite du champ de bataille, nommée depuis le bord de son camp : la Gauche d'un camp fait face à la Droite de l'autre. | « flanc », « aile » |
| **Signature** | Règle propre à une pièce unique, écrite en entier dans le livret Factions. | — |
| **Tour** | Tour d'un seul camp, de l'étape de commandement à celle de Pouvoir. | « round » |
| **Touche** | Retire 1 figurine ou 1 PV, quelle que soit la cible. | « blessure », « dégât » |
| **Type** | Infanterie, Cavalerie, Char, Créature, donné par le profil de l'unité. | « catégorie » |
| **Unité** | Figurines occupant un même hexagone et agissant ensemble. | « régiment », « bande » |
| **Valeur de commandement** | Nombre de cartes en main au moment de jouer, carte jouée comprise. | — |

---

*Version : 0.8 — 2026-09-27. P14a.3. D155 : entrée Objectif (objectif d'occupation temporaire). D158 : la réaction de combat s'appelle désormais **riposte** (entrée Riposte ajoutée) ; « Contre-attaque » ne désigne plus que la carte (entrée réécrite). Entrée Activation : l'étape b est désignée par son nom, étape d'ordre.*
*Version : 0.7 — 2026-09-24. D152 : le plateau de mouvement n'a pas de valeur de règle (entrées Plateau et Type) ; la classe, le type et le mode viennent du profil.*

*Version : 0.6 — 2026-09-24. Revue d'Emmanuel du livret, chapitres 1 et 2. La figurine avec bannière n'est plus un badge (entrées Badge et Bannière, §2). « Jeton de badge d'unité » remplace « jeton rond ». La réserve de Pouvoir est faite de jetons, sans piste (entrée Pouvoir). L'activation d'un hexagone de frontière à plusieurs joueurs est décrite au chapitre 2 et non plus au chapitre 10 (D151 amendée).*

*Version : 0.5 — 2026-09-24. P14a.2. D150 : Sections nommées depuis le bord de chaque camp (entrée Section). D151 : principe des hexagones de frontière déplacé au livret de règles (§2, entrée ajoutée). Badges Leader et Faction décrits comme jetons ronds, marqueur `{FACTION}` ; entrée Légende retirée sur indication d'Emmanuel (le badge n'existe plus ; son retrait des documents de conception reste à enregistrer) ; entrées Badge et Bord ajoutées. Règle d'écriture : aucune quantité de matériel dans le livret de règles. Marqueur d'illustration `{ILLUS:…}`.*

*Version : 0.4 — 2026-09-23. D149 : face Cible renommée Arc ; entrée Arc ajoutée ; marqueur `{DÉ:Arc}`.*

*Version : 0.3 — 2026-09-23. D148 : Arcane et Espoir/Désespoir remplacés par **Pouvoir** (face, jeton et réserve) ; marqueurs de pictos `{DÉ:Pouvoir}`, `{POUVOIR:Bien}`, `{POUVOIR:Mal}`.*

*Version : 0.2 — 2026-09-23. D147 : entrées Main et Général alignées (Général dans tous les formats).*

*Version : 0.1 — P14a.1 — 2026-09-23. Création (D144-D146) : rôle et frontières des quatre livrets, règles d'écriture, encadrés, marqueurs de pictos, glossaire figé.*
