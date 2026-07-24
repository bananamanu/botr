---
projet: "Batailles de la Terre du Milieu"
type: "scenario"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-07-21"
tags: [BdTdM, "type/scenario", "phase/1", "statut/brouillon", "playtest/1"]
version: "1.0"
---

# Playtest #1 — « Avant-garde sur le Pelennor »

> **Objet de ce document :** Scénario du premier test du cœur de règles, en réponse à la tâche Todoist « Rédiger le scénario de Playtest #1 » (due 24/07). Cadre de test **générique** en format Normal — *pas* le scénario canonique de la Bataille des Champs du Pelennor (celui-ci est le Playtest #3, `[[Document de cadrage]]` §6). But recherché : roder le moteur (commandement, dés, mêlée/tir, recul, contre-attaque, avance/poursuite) et **faire tomber un maximum de règles à la table**, avec 5 des 6 peuples du Pelennor (seul Harad manque — repoussé au Playtest #2 avec le Mûmakil).
>
> Aligné sur `[[Regles_Base]]`, `[[Regles_Speciales]]`, `[[Cartes_Commandement]]` et `[[Regles_Points]]`. Rosters : `[[Gondor_et_Fiefs]]`, `[[Rohan]]`, `[[Khand]]`, `[[Mordor]]`, `[[Easterling]]`.

---

## 1. Cadre

| | |
|---|---|
| **Format** | Normal — 13 × 9 hexagones, 3 Sections (Gauche / Centre / Droite) |
| **Joueurs** | **1 par camp** (voir `[[Cartes_Commandement]]` §7 et `[[Regles_Base]]` §5.5 — l'Épique à 6 joueurs reste Phase 2) |
| **Commandement** | Deck Normal commun (60 cartes), main de départ **5**, valeur de commandement 5 |
| **Victoire** | **6 médailles = 6 unités ennemies détruites.** Pas de médaille d'objectif. |
| **Durée estimée** | 60–90 min |

---

## 2. Prémisse (fidèle au texte)

Avant que les deux ost ne s'ébranlent pour la grande bataille, leurs avant-gardes se heurtent sur les champs cultivés qui s'étendent à perte de vue devant Minas Tirith. Les Rohirrim lancent leurs éclaireurs sur une aile ; la ligne de Gondor tient le centre ; les levées des fiefs affrontent la piétaille de l'Ombre. Rien n'est encore joué.

---

## 3. Champ de bataille

```
           SECTION GAUCHE      SECTION CENTRE       SECTION DROITE
             (col. 1–4)          (col. 5–9)           (col. 10–13)
  Rgée I ┌──────────────────┬────────────────────┬──────────────────┐ ← bord MAL
 (dépl.  │   KHAND (3)      │   EASTERLING (4)   │   MORDOR (4)      │
   Mal)  │                  │                    │                  │
  Rgée G ├──────────────────┼────────────────────┼──────────────────┤
  Rgée F │                  │      🌲 bois        │                  │
 (no     │    🏚 ruine       │     ⛰ colline       │                  │
 man's)  │                  │                    │                  │
  Rgée D │                  │                    │                  │
  Rgée C ├──────────────────┼────────────────────┼──────────────────┤
 (dépl.  │   ROHAN (4)      │   GONDOR (4)       │   FIEFS (4)       │
  Bien)  │                  │                    │                  │
  Rgée A └──────────────────┴────────────────────┴──────────────────┘ ← bord BIEN
```

**Terrain (simple — 3 éléments, en no man's land).**

| Élément | Position | Effet |
|---|---|---|
| ⛰ **Colline** | col. 7, rgée E | Terrain surélevé → **+1 dé en attaque** pour l'unité au sommet. Enjeu de contrôle du centre. |
| 🏚 **Ruine** | col. 3, rgée D | L'unité qui l'occupe gagne **[Protection 1]** (ignore 1 touche). → teste [Protection X]. |
| 🌲 **Bois** | col. 11–12, rgée F | **Bloque la ligne de vue** ; l'Infanterie s'y arrête en entrant ; la Cavalerie n'y pénètre pas. |

> ⚠️ **Point ouvert** — effets exacts du terrain à caler sur `[[Terrain]]` (doc non encore ouvert lors de la rédaction). Les trois effets ci-dessus sont ceux attendus d'après `[[Document de cadrage]]` §2 (terrain surélevé = +1 dé, réf. *Battle of Westeros*) et la table [Protection X] de `[[Regles_Speciales]]`.

---

## 4. Ordres de bataille

### Camp Bien — 12 unités, 60 points

| Section | Unité | Type | Pts | Règles |
|---|---|---|---|---|
| **Gauche** | Éored de cavalier | Cav. Mêlée | 6 | [Poursuite 2] |
| (Rohan) | Éored d'éclaireur | Cav. Tir | 4 | [Mobilité 2] + [Déploiement avancé] · Mvt 4 |
| | Archers liges | Inf. Tir | 3 | [Mobilité 1] |
| | Milice lige | Inf. Mêlée | 4 | — |
| **Centre** | Guerriers de Minas Tirith | Inf. Mêlée | 5 | [Armure 1] |
| (Gondor) | Archers de Minas Tirith | Inf. Tir | 4 | [Armure 1] |
| | Hommes d'armes de Dol Amroth *(piques)* | Inf. Mêlée | 6 | [Armure 1] + [Réception de charge] |
| | Gardes de la Citadelle | Inf. Mêlée | 6 | [Armure 1] + [Inébranlable 1] |
| **Droite** | Guerriers de Lossarnach | Inf. Mêlée | 6 | [Armure 1] + [Arme Lourde 1] |
| (Fiefs) | Guerriers des clans de Lamedon | Inf. Mêlée | 5 | [Arme Lourde 1] |
| | Rangers du Gondor | Inf. Tir | 4 | [Double Tir] |
| | Chevaliers de Dol Amroth | Cav. Mêlée | 7 | [Armure 1] + [Poursuite 1] |

### Camp Mal — 10 unités, 62 points

| Section | Unité | Type | Pts | Règles |
|---|---|---|---|---|
| **Gauche** | Pillards de Khand (hache) | Cav. Mêlée | 5 | [Arme Lourde 1] |
| (Khand) | Pillards de Khand (archer) | Cav. Tir | 3 | [Mobilité 1] |
| | Aurige de Khand *(char)* | Chars Mêlée | 7 | [Charge écrasante] + [Arme Lourde 1] + [Poursuite 1] · Jamais Faible · PV 3 |
| **Centre** | Cohorte d'orientaux | Inf. Mêlée | 5 | [Mur de bouclier] |
| (Easterling) | Cohorte de piquiers orientaux *(piques)* | Inf. Mêlée | 6 | [Réception de charge] + [Mur de bouclier] |
| | Cohorte d'archers orientaux | Inf. Tir | 4 | [Double Tir] |
| | Cataphractaires orientaux | Cav. Mêlée | 7 | [Armure 2] + [Charge écrasante] · Mvt 2 |
| **Droite** | Bande d'orques du Mordor | Inf. Mêlée | 5 | [Horde] (2→3 dés) |
| (Mordor) | Bande d'orques du Morannon | Inf. Mêlée | 6 | [Armure 1] + [Horde] (3→4 dés) |
| | Bande d'uruk-hai du Mordor | Inf. Mêlée | 7 | [Armure 1] + [Férocité] · Attaque 4 constante |
| | Troll du Mordor *(créature)* | Créat. Mêlée | 7 | [Charge écrasante] + [Peur 1] · Jamais Faible · PV 5 |

**Confrontations par Section :** Gauche = duel de mobilité (Rohan ↔ Khand) · Centre = miroir des empires disciplinés (Gondor ↔ Easterling) · Droite = ligne lourde contre la horde (Fiefs ↔ Mordor).

---

## 5. Déploiement

1. Chaque camp place ses unités dans sa **zone de déploiement** (Bien : rgées A–C ; Mal : rgées G–I), **chaque peuple dans sa Section** (colonnes du §4). Placement libre à l'intérieur de la zone + section.
2. **Le Mal déploie en premier**, le Bien répond (le Bien voit le dispositif adverse — cohérent avec une force qui arrive en renfort).
3. **[Déploiement avancé]** : une fois les deux camps déployés, avant le tour 1, l'Éored d'éclaireur se repositionne d'un plein mouvement (4 hex), sans finir au contact d'une unité ennemie.
4. **Premier tour : au Mal** (l'Ombre presse l'assaut).

---

## 6. Déroulement (rappel — tout est dans le socle)

Deck Normal commun. À son tour, le joueur actif : **joue 1 carte → active → déplace → attaque → pioche** pour ramener sa main à 5 (`[[Cartes_Commandement]]` §5, `[[Regles_Base]]` §4).

- **Contre-attaque universelle** : réaction automatique de toute unité survivante après une mêlée subie (`[[Regles_Base]]` §7).
- **Recul (Drapeaux)** : une unité qui ne peut pas reculer (bord de table, unités, terrain infranchissable) subit **1 perte par hexagone de recul non effectué** (règle de base C&C).
- **Faible** : unité réduite à sa dernière figurine (sauf types « Jamais Faible » : Chars, Créature).

---

## 7. Ce qu'on surveille (pour le compte-rendu — `Tpl playtest`)

Les cinq coûts jamais éprouvés en partie réelle, tous présents dans ce scénario :

| Règle | Porteur(s) | Question |
|---|---|---|
| **[Horde]** (3 pts) | Orques + Morannon | L'effondrement à la 1ʳᵉ perte se sent-il ? (deux paliers : 2→3 et 3→4 dés) |
| **[Peur 1]** via Arcane (2×X) | Troll | Fréquence des Arcanes ; le Troll fait-il vraiment plier ? Interaction : Gardes de la Citadelle [Inébranlable 1] absorbent la Peur. |
| **[Mur de bouclier]** (1 pt) | Cohorte + Piquiers | Risque de sous-évaluation (quasi-[Armure 1] permanent en ligne). La décision « rompre ou tenir » existe-t-elle vraiment ? |
| **[Déploiement avancé]** (2 pts) | Éored d'éclaireur | Avantage réel du repositionnement pré-bataille ? |
| **Aurige de Khand** (PV 3 + [Poursuite 1], 7 pts) | Aurige | Trop rentable pour son coût ? |

**Aussi à l'œil :** `[Armure 2]` (première armure doublée, Cataphractaires) · `[Charge écrasante]` sur 3 porteurs distincts (tours trop punitifs ?) · lisibilité des types « Jamais Faible » (Aurige, Troll) · piques et [Réception de charge] des deux côtés (Dol Amroth ↔ piquiers orientaux).

---

## 8. Points ouverts (à trancher après le test)

> ⚠️ **Équilibre** — Bien **60** / Mal **62** (Mal +2), et surtout **12 unités contre 10** sous un seuil de médailles *fixe* (6) : le Bien a un léger avantage de nombre pour atteindre 6 éliminations, le Mal des unités individuellement plus fortes (quantité vs qualité). Écart assumé pour ce premier test ; à égaliser pour les runs suivants (unités à effectif égal, ou seuils asymétriques) si le déséquilibre se confirme à la table.

> ⚠️ **Cadrage joueurs** — rédigé pour du **1v1 Normal** (design documenté). Une table à 6 joueurs supposerait d'improviser le commandement Épique multi-joueurs, explicitement réservé à la Phase 2 (`[[Cartes_Commandement]]` §7).

> ⚠️ **Terrain** — effets exacts à confirmer sur `[[Terrain]]` (voir §3).

---

> 🔗 **Voir aussi**
> `[[Document de cadrage]]` · `[[Regles_Base]]` · `[[Regles_Speciales]]` · `[[Cartes_Commandement]]` · `[[Regles_Points]]` · rosters des 5 peuples

---

*Version : 1.0 — Phase 1 — 2026-07-21. Premier scénario de test du cœur de règles (Normal, 1v1). OOB calé avec Emmanuel : Camp Bien = Rohan + Gondor + fiefs (12 u., 60 pts) ; Camp Mal = Khand + Easterling + Mordor (10 u., 62 pts). Victoire à 6 unités détruites. Couvre les 5 règles neuves jamais testées ([Horde], [Peur X], [Mur de bouclier], [Déploiement avancé], compromis Aurige) plus les premières [Armure 2] / types « Jamais Faible ». Non joué — premier passage à la table prévu au Playtest #1.*
