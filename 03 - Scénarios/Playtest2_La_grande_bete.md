---
projet: "Batailles de la Terre du Milieu"
type: "scenario"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-07-29"
tags: [BdTdM, "type/scenario", "phase/1", "statut/brouillon", "playtest/2"]
version: "0.1"
---

# Playtest #2 — « La grande bête sur le Pelennor »

> **Objet de ce document :** Scénario du deuxième test, **recentré sur le Mûmakil** (gabarit + règles de la bête), en réponse à la tâche Todoist « Ajuster le scénario pour intégrer Harad + Mûmakil » (due 31/07). Session prévue le **1er août**, 1 joueur par camp (Emmanuel + un testeur neuf). Ni héros ni format Épique — réservés à la Phase 2.
>
> **Intention de design.** On reprend le cadre validé au Playtest #1b (Normal 13×9, 3 Sections, deck commun) et on y greffe la pièce neuve. L'enseignement n°1 de PT1 (le centre aspire tout, les règles neuves ne tombent pas) est retourné en **atout** : le Mûmakil est placé au **centre** et rendu **objectif à 2 médailles**, ce qui oblige les deux camps à converger vers lui. La bête ne peut pas être ignorée — donc elle *sera* testée. Le renfort du Mal est composé pour rejouer au passage les règles insuffisamment éprouvées ([Peur], [Horde], [Mur de bouclier], Aurige reconçu).
>
> Aligné sur `[[Regles_Base]]`, `[[Regles_Speciales]]`, `[[Cartes_Commandement]]`, `[[Regles_Points]]`. Rosters : `[[Harad]]`, `[[Rohan]]`, `[[Gondor_et_Fiefs]]`, `[[Khand]]`, `[[Easterling]]`, `[[Mordor]]`.

---

## 1. Cadre

| | |
|---|---|
| **Format** | Normal — 13 × 9 hexagones, 3 Sections (Gauche / Centre / Droite) |
| **Joueurs** | **1 par camp** (l'Épique à 6 joueurs reste Phase 2) |
| **Commandement** | Deck Normal commun (60 cartes), main de départ **5**, valeur de commandement 5 |
| **Points** | Bien **75** (13 unités) / Mal **76** (12 unités, dont le Mûmakil à 21) — écart +1 Mal assumé (cf. PT1) |
| **Victoire** | **8 médailles** — avec la règle spéciale du Mûmakil (§ Victoire ci-dessous) |
| **Durée estimée** | 90–120 min |

### Victoire — 8 médailles, la bête au centre du jeu

Chaque unité ennemie détruite = **1 médaille**. Deux exceptions liées au Mûmakil :

- **Prime de la bête (Mal).** Tant que le Mûmakil est **en vie et sur la table**, le Mal dispose d'une **médaille permanente supplémentaire** — il joue donc *effectivement à 7*. Cette médaille **s'évapore à l'instant où le Mûmakil est détruit**.
- **Abattre le Mûmakil (Bien).** Sa destruction rapporte **2 médailles** au Bien (au lieu de 1).
- **Le pivot.** La chute de la bête est donc une **bascule de 3 médailles** (+2 au Bien, −1 au Mal). C'est le cœur battant du scénario — et ça recoupe l'étiquette « 21 pts ≈ 3 Éored » du profil (`[[Harad]]`, D054).
- **Bête affolée.** Tant que le Mûmakil porte un **marqueur Furie**, la prime de la bête du Mal est **suspendue** — une bête devenue folle n'est plus un atout. Elle est rétablie si la Furie est retirée, et disparaît définitivement à la mort de la bête. **Affoler le Mûmakil devient donc une fin en soi pour le Bien**, pas seulement un préalable à l'abattre.

> **Exemple.** Au tour 5, le Mal a détruit 5 unités du Bien : sa jauge affiche **6** (5 + la prime de la bête). Il lui manque 2 pour gagner. Le Bien jette ses deux lances de cavalerie sur le Mûmakil et l'abat : il encaisse **2 médailles d'un coup** et la jauge du Mal **retombe de 6 à 5** — la prime disparaît. Un seul événement vient de renverser la course.

---

## 2. Prémisse (fidèle au texte)

Les grandes bêtes du Harad se sont avancées sur les champs du Pelennor, tours de guerre vivantes tanguant au-dessus de la mêlée, leurs cornacos les poussant droit dans les rangs de Gondor. Les chevaux de la Marche refusent d'en approcher : leur seule masse suffit à briser une charge avant même le contact. Autour de leurs pattes se pressent les Suderons et, plus loin, la piétaille de l'Ombre et les cohortes disciplinées de l'Est. Une bête acculée devient plus terrible encore pour les siens que pour l'ennemi : blessée, affolée, elle piétine sans distinguer ami de foe. Aux Rohirrim et aux hommes de Gondor de la faire tomber — ou de la rendre folle — avant qu'elle n'ouvre la brèche.

---

## 3. Champ de bataille

```
              GAUCHE (col 1–4)      CENTRE (col 5–9)       DROITE (col 10–13)
  Rgée I ┌───────────────────┬─────────────────────┬───────────────────┐ ← bord MAL
 (dépl.  │   MORDOR          │   HARAD             │   EASTERLING      │
   Mal)  │  Troll + Horde    │  🐘 MÛMAKIL + esc.   │  Mur de bouclier  │
  Rgée G │  + pisteurs orques│                     │  + AURIGE (Khand) │
  Rgée F ├───────────────────┼─────────────────────┼───────────────────┤
 (no     │    🏚 ruine        │      ⛰ colline       │     🌲 bois        │
  man's  │   (col 3, rgD)    │    (col 7, rgE)     │   (col 11–12,rgF) │
  land)  │                   │                     │                   │
  Rgée D │                   │                     │                   │
  Rgée C ├───────────────────┼─────────────────────┼───────────────────┤
 (dépl.  │  GONDOR           │  ROHAN (lances)     │  FIEFS + Rohan    │
  Bien)  │ Citadelle + Rohan │  + enclume Gondor   │  léger            │
  Rgée A └───────────────────┴─────────────────────┴───────────────────┘ ← bord BIEN
```

**Terrain — repris tel quel de PT1b (validé), 3 éléments en no man's land.**

| Élément | Position | Effet |
|---|---|---|
| ⛰ **Colline** | col. 7, rgée E | Terrain surélevé → **+1 dé en attaque** pour l'unité au sommet. |
| 🏚 **Ruine** | col. 3, rgée D | L'unité qui l'occupe gagne **[Protection 1]**. |
| 🌲 **Bois** | col. 11–12, rgée F | **Bloque la ligne de vue** ; l'Infanterie s'y arrête en entrant ; la Cavalerie n'y pénètre pas. |

> ⚠️ **Nouveau point ouvert — gabarit ↔ terrain.** Le comportement du gabarit 1-2-1 du Mûmakil face à la colline (col 7) sur son axe de progression n'est **pas** écrit. À trancher **à la table et à journaliser** : la bête traverse-t-elle la colline (la piétine), s'y arrête-t-elle, ou la contourne-t-elle ? La colline est volontairement laissée sur l'axe central pour que la question se pose au moins une fois. Bois et ruine sont sur les ailes, hors de sa route directe.

---

## 4. Ordres de bataille

### Camp Bien — 13 unités, 75 points *(Rohan + Gondor et fiefs)*

| Section | Unité | Type | Pts | Règles |
|---|---|---|---|---|
| **Centre** | Gardes royaux à cheval | Cav. Mêlée | 8 | [Armure 1] + [Poursuite 2] |
| (lances Rohan | Éored de cavalier du Rohan | Cav. Mêlée | 7 | [Poursuite 2] + [Prise de flanc] |
| + enclume | Guerriers de Minas Tirith | Inf. Mêlée | 5 | [Armure 1] |
| Gondor) | Hommes d'armes de Dol Amroth *(piques)* | Inf. Mêlée | 6 | [Armure 1] + [Réception de charge] |
| **Gauche** | Gardes de la Citadelle | Inf. Mêlée | 6 | [Armure 1] + [Inébranlable 1] |
| (Gondor, | Gardes royaux à cheval | Cav. Mêlée | 8 | [Armure 1] + [Poursuite 2] |
| face Mordor) | Archers de Minas Tirith | Inf. Tir | 4 | [Armure 1] |
| | Milice lige | Inf. Mêlée | 4 | [Arme de jet 1] |
| **Droite** | Chevaliers de Dol Amroth | Cav. Mêlée | 7 | [Armure 2] + [Poursuite 1] · Mvt 2 |
| (fiefs + | Guerriers de Lossarnach | Inf. Mêlée | 6 | [Armure 1] + [Arme Lourde 1] |
| Rohan léger, | Gardes Royaux du Rohan | Inf. Mêlée | 6 | [Armure 1] + [Inébranlable 1] |
| face Easterling)| Rangers du Gondor | Inf. Tir | 4 | [Double Tir] + [Mobilité 1] |
| | Éored d'éclaireur | Cav. Tir | 4 | [Mobilité 2] + [Vigilant] |

**Total : 8+7+5+6 (C) + 6+8+4+4 (G) + 7+6+6+4+4 (D) = 26 + 22 + 27 = 75.**

### Camp Mal — 12 unités, 76 points *(Harad + Mordor + Easterling + Khand)*

| Section | Unité | Type | Pts | Règles |
|---|---|---|---|---|
| **Centre** | **Mûmakil** | Créature | 21 | [Charge écrasante]* + [Howdah] + [Inamovible] + [Bête incontrôlable]* · Jamais Faible · PV 6 |
| (Harad) | Archers du Harad | Inf. Tir | 3 | [Poison] |
| | Lanciers du Harad | Inf. Mêlée | 5 | — |
| | Lanciers du Harad | Inf. Mêlée | 5 | — |
| **Gauche** | Troll du Mordor *(créature)* | Créat. Mêlée | 7 | [Arme Lourde 1] + [Peur 1] · Jamais Faible · PV 4 |
| (Mordor) | Bande d'orques du Mordor | Inf. Mêlée | 5 | [Horde] (2→3 dés) |
| | Bande d'orques du Morannon | Inf. Mêlée | 6 | [Armure 1] + [Horde] (3→4 dés) |
| | Bande de pisteurs orques | Inf. Tir | 3 | [Mobilité 1] |
| **Droite** | Cohorte d'orientaux | Inf. Mêlée | 5 | [Mur de bouclier] |
| (Easterling | Cohorte de piquiers orientaux *(piques)* | Inf. Mêlée | 6 | [Réception de charge] + [Mur de bouclier] |
| + Khand) | Cohorte d'archers orientaux | Inf. Tir | 4 | [Double Tir] |
| | Aurige de Khand *(char)* | Chars Mêlée | 6 | [Poursuite 1] + [Plateforme de tir 2] · Jamais Faible · PV 3 |

**Total : 21+3+5+5 (C) + 7+5+6+3 (G) + 5+6+4+6 (D) = 34 + 21 + 21 = 76.**

\* *[Charge écrasante] et [Bête incontrôlable] du Mûmakil sont les **refontes dédiées** de `[[Harad]]` (D054), distinctes des versions retirées de la V1 — voir §6.*

**Confrontations par Section :**
- **Centre — la bête.** Mûmakil + double haie de lanciers Harad face aux cavaleries du Rohan (test du **recul cavalerie ×2**) et à l'enclume d'infanterie de Gondor (test de l'**impact anti-infanterie B4** et du contre-jeu « le noyer sous le nombre »). Les piques de Dol Amroth y sont un cas d'école (voir §6, interaction piques).
- **Gauche — la horde.** Mordor ([Horde] + Troll [Peur 1] + pisteurs à l'arc) contre une ligne de Gondor bâtie autour des **Gardes de la Citadelle [Inébranlable 1]** — l'interaction [Peur]↔[Inébranlable] flaggée depuis PT1 se joue enfin ici.
- **Droite — la discipline.** Easterling ([Mur de bouclier]) + Aurige de Khand (char-plateforme reconçu) contre la cavalerie lourde de Dol Amroth et les fiefs.

---

## 5. Déploiement

1. Chaque camp place ses unités dans sa **zone de déploiement** (Bien : rgées A–C ; Mal : rgées G–I), **chaque peuple dans sa Section** (colonnes du §4). Placement libre à l'intérieur de la zone + section.
2. **Le Mûmakil occupe 4 hexagones en colonne 1-2-1**, pointe vers le haut (vers son bord), au centre de la zone Mal (autour des col. 6–8). Vérifier qu'il tient physiquement dès le déploiement.
3. **Le Mal déploie en premier**, le Bien répond (il voit le dispositif adverse, cohérent avec une force qui arrive en renfort — et lui laisse une chance de calibrer sa réponse à la bête).
4. **Premier tour : au Mal** (l'Ombre presse l'assaut, la bête s'ébranle).

---

## 6. Déroulement (rappels + spécificités du Mûmakil)

Deck Normal commun. À son tour, le joueur actif : **joue 1 carte → active → déplace → attaque → pioche** pour ramener sa main à 5.

**Conventions de table (validées PT1b, à rappeler au joueur neuf) :**
- **Deux jetons** (D052) : un jeton *activation* sur les unités du camp actif ; un jeton *cible* sur toute unité adverse touchée mais survivante, retiré une fois la **contre-attaque** résolue. Fin des oublis de riposte.
- **Recul façon Memoir '44** (D041) : toujours vers le bord du joueur qui recule ; 1 perte par hexagone de recul non effectué.
- **[Mobilité X]** (D056) : *« tu frappes, puis tu décroches. Pas d'attaque, pas de bonus. »*
- **Faible** : dernière figurine (sauf types **Jamais Faible** — Créature, Chars).

**Le Mûmakil — mémo de la bête** *(détail complet dans `[[Harad]]` §3)* :

- **Gabarit 1-2-1, translation pure.** Pas de pivot : la pointe reste toujours vers le haut ; le déplacement est une translation (aucun changement d'orientation). **Direction libre** (tranché) : le joueur choisit librement l'axe de translation, y compris latéral.
- **[Charge écrasante] (refonte).** À son activation, le Mûmakil **DOIT** avancer de **2 hexagones** (1+1) vers l'hexagone de tête désigné, **sans tenir compte** des figurines présentes. Chaque unité dont un hexagone est traversé subit une **attaque de 4 dés où la Couronne compte aussi comme touche** — **en phase de mouvement, ce n'est pas un combat** : **aucune contre-attaque, aucune règle de combat**. Toute **cavalerie** repoussée **recule du double**. Si un survivant bloque le passage, il s'arrête au **dernier hexagone libre**. **Aucune attaque de mêlée en phase d'attaque.**
- **Interaction piques (à confirmer).** Comme l'impact n'est **pas** un combat, **[Réception de charge] ne se déclenche pas** contre lui : les piques de Dol Amroth (Bien) ne « reçoivent » pas la bête — elle les piétine. Cas d'école volontairement placé sur son axe. À confirmer et journaliser.
- **[Howdah] = [Plateforme de tir 2] + [Poison].** En phase d'attaque, tir de **2 dés**, portée **1–3**, ligne de vue, **en plus** de tout le reste, une fois par activation ; chaque **Couronne** = 1 touche (poison).
- **[Inamovible].** Ne recule jamais : ignore tout Drapeau ou résultat de retraite.
- **[Bête incontrôlable] (refonte) — Furie.** À son activation, **s'il est blessé**, lancer autant de dés que ses **PV restants** : **aucune Couronne** → poser un **marqueur Furie**, l'adversaire dirige immédiatement la charge (règles [Charge écrasante] complètes, **y compris percuter les Harad**). Tant que la Furie est posée, le camp adverse peut l'activer comme une de ses figurines. À la **fin de chaque tour**, le propriétaire relance **(PV restants + 1)** dés : une Couronne retire la Furie. **Tant que la Furie est posée, la prime de médaille du Mal est suspendue** (voir Victoire). *(Auto-équilibrage : plus la bête est basse en PV, plus elle s'affole et moins elle se calme.)*
- **Jamais Faible** (Créature) ; **ne contre-attaque jamais** — tout son contre-jeu est de la noyer sous le nombre.

---

## 7. Ce qu'on surveille (grille du compte-rendu — `Tpl playtest`)

**Priorité — la bête.** La session **rate** si l'un de ces points ne se produit pas au moins une fois :

| Règle | Porteur | Question |
|---|---|---|
| **Gabarit 1-2-1 / translation** | Mûmakil | Tient-il à la table ? Translation **libre** (y compris latérale) sans ambiguïté ? Devient-elle gamey (la bête esquive) ? |
| **[Charge écrasante] refonte** | Mûmakil | Impact en phase de mouvement lisible ? Couronne = touche clair ? Trop punitif par tour ? |
| **Recul cavalerie ×2** | Mûmakil ↔ lances Rohan | Le double-recul se sent-il ? (d'où deux cavaleries royales au centre) |
| **[Howdah]** | Mûmakil | Volée 2 dés + poison déclenchée, en plus du reste. |
| **[Bête incontrôlable] / Furie** | Mûmakil | **Se déclenche (donc la bête doit être blessée)** ? Spirale lisible ? A-t-elle piétiné les siens ? La **prime du Mal** a-t-elle bien été suspendue le temps de la Furie ? |
| **[Inamovible]** | Mûmakil | Confronté à un Drapeau au moins une fois. |
| **Interaction piques** | Mûmakil ↔ Dol Amroth | [Réception de charge] bien **inerte** contre l'impact ? |
| **Étiquette 21 pts** | Mûmakil | ≈ 3 Éored : l'équivalence tient-elle à la table ? |
| **Lisibilité (joueur neuf)** | Mûmakil (4 règles) | Se joue-t-il **sans arbitrage constant** ? Point convention n°1. |

**Au passage — les règles sous-testées du renfort :**

| Règle | Porteur(s) | Question |
|---|---|---|
| **[Peur 1]** (face Arcane) | Troll | Fréquence des Arcanes ; les **Gardes de la Citadelle [Inébranlable 1]** absorbent-ils bien la Peur ? Coût 2×X toujours provisoire. |
| **[Horde]** (3 pts) | Orques + Morannon | Surge puis effondrement (2→3 et 3→4 dés) — davantage d'activations qu'en #1b ? |
| **[Mur de bouclier]** (1 pt) | Cohorte + Piquiers | Risque de **sur-cumul** en ligne permanente (vigilance conservée de #1b). |
| **Aurige de Khand** (6 pts) | Aurige | Densité d'actions **volée + mêlée + Poursuite** sur une activation — à l'œil. |
| **[Poison]** | Archers du Harad | **Première assignation réelle sur infanterie** ; Couronne = touche supplémentaire. |

---

## 8. Points ouverts (restants)

> ✅ **Tranché (v0.2)** : direction de translation **libre** · la **Furie suspend la prime** du Mal · escorte Harad = **2 Lanciers + Archers** (wargs retirés) · côté Bien, seconde **Gardes royaux à cheval** au lieu de la Garde du roi.

> ⚠️ **1. Gabarit ↔ terrain** (colline centrale) — aucune règle écrite : trancher **à la table et journaliser** (§3). Seule inconnue de mouvement restante, la direction étant désormais libre.

> ⚠️ **2. Équilibre 75 / 76** — Bien 13 unités / Mal 12 unités + prime de la bête, seuil 8. Léger **+1 au Mal** (dans la lignée du +2 de PT1), écart quantité (Bien) / qualité (Mal) assumé. Si tu veux 75 pile, retirer un pisteur orque (−3) côté Mal suffit — sinon on laisse tel quel.

---

> 🔗 **Voir aussi**
> `[[Harad]]` (profil complet du Mûmakil) · `[[Playtest1_Avant-garde_sur_le_Pelennor]]` · `[[Playtest1_Compte-rendu]]` · `[[Playtest1b_Addendum]]` · `[[Regles_Base]]` · `[[Regles_Speciales]]` · `[[Cartes_Commandement]]` · `[[Regles_Points]]`

---

*Version : 0.2 — Phase 1 — 2026-07-29. Arbitrages d'Emmanuel intégrés : direction de translation du gabarit **libre** ; **la Furie suspend la prime de la bête** du Mal (règle actée, plus une option — affoler devient une fin en soi pour le Bien) ; escorte Harad = **2 Lanciers + Archers**, **Meute de cavaliers wargs retirée** ; côté Bien, **Garde du roi à cheval remplacée par une seconde Gardes royaux à cheval** (même coût, 8). Nouveaux totaux : Bien 75 (13 u.) / Mal 76 (12 u.). Restent ouverts : gabarit ↔ terrain, et l'écart +1 Mal.*

*Version : 0.1 — Phase 1 — 2026-07-29. Premier jet du scénario de Playtest #2, recentré sur le Mûmakil (gabarit + règles de la bête). Cadre PT1b réutilisé (Normal 13×9, deck commun). Mûmakil placé au centre et rendu objectif à 2 médailles (prime de la bête pour le Mal, bascule de 3 médailles à sa chute) pour forcer la convergence des deux camps. Renfort du Mal composé pour rejouer [Peur]/[Horde]/[Mur de bouclier]/Aurige. Non joué.*
