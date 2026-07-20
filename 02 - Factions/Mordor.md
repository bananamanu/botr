---
projet: "Batailles de la Terre du Milieu"
type: "faction"
phase: "1"
statut: "valide"
date_maj: "2026-07-20"
tags: [BdTdM, "type/faction", "peuple/mordor", "statut/valide"]
version: "0.3"
---

# Mordor — Profils d'unités

> **Objet de ce document :** Profils de troupes pour le peuple Mordor (6 unités, liste fournie par Emmanuel), en réponse à la tâche Todoist « Rédiger les profils d'unités — Mordor » (due 20/07, P1). **Roster validé et clos (D036 du [[Document de cadrage]]).** Prêt pour le Playtest #1.
>
> Historique de la revue :
> - **Passe 0 (ébauche)** : identité cadrée — [Horde] (D032) comme fil conducteur de la piétaille orque ; chiffrage initial proposé par Claude.
> - **Passe 1 partielle (2026-07-20)** : Uruk-hai validé (Attaque 4 constante, sans Horde — l'élite qui ne rompt pas) ; [Peur] rebasculée sur la face Arcane au lieu de la Couronne (résout le conflit de Couronne du Troll, réutilise une face morte, ouvre la couche Leadership — voir D033/D034 du cadrage).
> - **Clôture (2026-07-20, D036)** : les 4 derniers points ouverts tranchés avec Emmanuel — Uruk-hai garde [Férocité] (7 pts) ; Troll à [Peur 1] et 5 PV (7 pts) ; Pisteurs orques restent sans [Horde] (3 pts, profil simple). **Les 6 profils sont validés tels que chiffrés dans l'ébauche initiale — aucun recalcul nécessaire.** Restent uniquement des points « à surveiller au playtest, non bloquants » (§6), même statut que [Déploiement avancé] pour Rohan ou le compromis PV de l'Aurige pour Khand à leur clôture.
>
> **Choix d'identité actés (2026-07-20) :**
> - **[Horde] comme fil conducteur du peuple** (D032, réservée aux Orcs) : la piétaille de Mordor est terrible au premier choc (+1 dé + [Inébranlable 1] à pleine force) puis s'effondre dès la première perte — nombreuse et féroce dans la charge, prompte à rompre une fois entamée. Aussi lisible que « armure » pour Gondor, « hache lourde » pour Khand ou « mobilité » pour Rohan.
> - **L'armure comme signal d'échelon**, pas comme trait de peuple : seuls les gros orques mailés (Morannon, Uruk-hai) portent [Armure 1]. Contraste net avec Gondor ([Armure] partout) et Khand (aucune armure).
> - **L'Uruk-hai est la seule infanterie orque SANS [Horde]** (validé) : l'élite noire de Barad-dûr est l'orque qui *ne rompt pas*. Attaque 4 constante là où le reste de la horde surgit puis s'effondre.
> - **[Peur X] déclenchée par la face Arcane** (D033) : chaque Arcane obtenue en attaque compte comme X Drapeaux contre la cible. Débute sur le Troll ; premier jalon de la future couche Leadership (Œil de Sauron / Rune de Gandalf, D034), candidate pour les Nazgûl / le Roi-Sorcier en Phase 2 (versions « Terreur »).
> - **Troll traité comme pièce signature** : seul profil autorisé à dépasser 2 règles spéciales (D023).
>
> Aligné sur [[Regles_Base]] et [[Regles_Speciales]]. **Coût en points** : `Points_finaux = round((Mouvement + PV + Attaque×D + Σ coût des règles) ÷ 3) − 1`.

---

## Conventions de ce roster

- **Mouvement** : 2 pour l'Infanterie et la Créature (le Troll lambine), 3 pour la Cavalerie (D022).
- **Portée de tir** : 4 hexagones pour l'unité de tir (D020).
- **Attaque des unités [Horde]** : la valeur inscrite au profil est la valeur **de base** (après effondrement) ; le « +1 dé à pleine force » vient de [Horde]. On note « 2 dés (3 à pleine force) » et « 3 dés (4 à pleine force) ».
- **Chiffrage de [Horde]** : la formule utilise l'**Attaque de base** (2 orques, 3 Morannon), et [Horde] est facturé **3 pts forfaitaires** — le +1 dé *est* la règle, jamais compté deux fois. Première assignation de [Horde] : convention à valider.
- **Règles spéciales** : 1 par profil standard, jusqu'à 2 pour le Troll (pièce signature).
- **Roster de 6 profils** correspondant à la liste fournie pour le Playtest #1.

---

## 1. Liste des troupes

| # | Unité | Type | Combat | **Points** |
|---|---|---|---|---|
| 1 | Bande d'orques du Mordor | Infanterie | Mêlée | **5** |
| 2 | Bande d'orques du Morannon | Infanterie | Mêlée | **6** |
| 3 | Bande de pisteurs orques | Infanterie | Tir | **3** |
| 4 | Meute de cavaliers wargs | Cavalerie | Mêlée | **4** |
| 5 | Bande d'uruk-hai du Mordor | Infanterie | Mêlée | **7** |
| 6 | Troll du Mordor | Créature | Mêlée | **7** |

> 🎲 **Note de design — lecture rapide du roster**
> Le cœur de l'armée, ce sont les deux bandes d'orques (1, 2), toutes deux [Horde] : elles frappent au-dessus de leur poids au premier contact puis retombent. Les pisteurs (3) et les wargs (4) sont les pièces mobiles/bon marché. L'Uruk-hai (5) est le pilier d'élite qui *ne rompt pas*. Le Troll (6) est la pièce signature, la seule à porter [Peur].
>
> **Comparaison utile :** l'orque du Mordor (5 pts, [Horde]) coûte comme le Guerrier de Minas Tirith (5 pts, [Armure 1]) et le Mercenaire de Khand (5 pts, [Arme Lourde 1]) — trois routes opposées vers le même total : durer (Gondor), taper fort en continu (Khand), submerger au premier choc puis s'effondrer (Mordor). Illustration du principe 6 (asymétrie assumée).

---

## 2. Profils détaillés

### 1. Bande d'orques du Mordor

| Type | Combat | Mouvement | Attaque | Portée | PV | **Points** |
|---|---|---|---|---|---|---|
| Infanterie | Mêlée | 2 | 2 dés *(3 à pleine force)* | — | 6 figurines | **5** |

**Règles spéciales :** [Horde]

**Note narrative :** la piétaille de Sauron, jetée en masse contre les lignes. Féroce tant que le nombre la porte ([Horde] : 3 dés + [Inébranlable 1] à pleine force), elle rompt et s'égaille dès qu'elle est entamée (retour à 2 dés, plus d'Inébranlable, pour le reste de la partie). L'orque ne se lit pas au dé près : il se lit à la vague.

> 🔗 **Voir aussi** [[Regles_Speciales]] — [Horde] (D032)

---

### 2. Bande d'orques du Morannon

| Type | Combat | Mouvement | Attaque | Portée | PV | **Points** |
|---|---|---|---|---|---|---|
| Infanterie | Mêlée | 2 | 3 dés *(4 à pleine force)* | — | 6 figurines | **6** |

**Règles spéciales :** [Armure 1] + [Horde]

**Note narrative :** les orques-soldats de la Porte Noire, plus grands que la piétaille et bardés de fer noir. Même dynamique de horde que la Bande du Mordor (1), mais une crête plus haute (4 dés à pleine force) et une armure qui les fait durer un peu au-delà du premier choc. C'est le « vrai » soldat orque : la ligne sur laquelle Mordor s'appuie.

> 🔗 **Voir aussi** [[Regles_Speciales]] — [Armure X] · [Horde]

---

### 3. Bande de pisteurs orques

| Type | Combat | Mouvement | Attaque | Portée | PV | **Points** |
|---|---|---|---|---|---|---|
| Infanterie | Tir | 2 | 2 dés | 4 | 6 figurines | **3** |

**Règles spéciales :** [Mobilité 1]

**Note narrative :** les traqueurs à l'arc de la Terre de l'Ombre — des orques d'un genre plus fureteur, envoyés en avant pour flécher et harceler. [Mobilité 1] leur permet de se replacer après avoir tiré.

> ✅ **Validé (2026-07-20)** : [Horde] volontairement retirée — règle réservée à la mêlée de masse à 6 PV (D032), pas au tir. Profil confirmé tel quel.

> 🔗 **Voir aussi** [[Regles_Speciales]] — [Mobilité X]

---

### 4. Meute de cavaliers wargs

| Type | Combat | Mouvement | Attaque | Portée | PV | **Points** |
|---|---|---|---|---|---|---|
| Cavalerie | Mêlée | 3 | 3 dés | — | 3 figurines | **4** |

**Règles spéciales :** [Férocité]

**Note narrative :** des loups sauvages montés par des orques, qui déchirent et mordent sans lâcher prise. [Férocité] (la contre-attaque se résout avant les retraites adverses) traduit la bête qui claque des mâchoires même sous les coups. Volontairement en retrait de l'Éored du Rohan : la mobilité reste le domaine réservé du Rohan — les wargs sont *sauvages*, pas manœuvriers.

> 🎲 **Note de design** Pas de [Horde] : D032 la réserve aux Orcs (le warg est une bête), et la Cavalerie à 3 PV perdrait sa première figurine trop vite pour qu'un bonus « à pleine force » existe. [Horde] est structurellement une règle d'infanterie à 6 PV.

> 🔗 **Voir aussi** [[Regles_Speciales]] — [Férocité]

---

### 5. Bande d'uruk-hai du Mordor — *validée*

| Type | Combat | Mouvement | Attaque | Portée | PV | **Points** |
|---|---|---|---|---|---|---|
| Infanterie | Mêlée | 2 | 4 dés *(constante)* | — | 6 figurines | **7** |

**Règles spéciales :** [Armure 1] + [Férocité]

**Note narrative :** les grands Uruks noirs de Barad-dûr, la haute stature bréée par Sauron pour tenir là où la piétaille rompt. C'est **l'exception du roster** : pas de [Horde], mais une Attaque 4 **constante** — l'élite qui ne s'effondre pas au premier sang. [Armure 1] (mailles noires) et [Férocité] (la cruauté d'élite qui riposte avant de reculer) en font le pilier autour duquel la horde se rassemble.

> ✅ **Validé (2026-07-20)** : Attaque 4 constante, sans Horde. [Férocité] confirmée (7 pts) — l'élite qui riposte férocement même sous les coups.

> 🔗 **Voir aussi** [[Regles_Speciales]] — [Armure X] · [Férocité]

---

### 6. Troll du Mordor — *pièce signature*

| Type | Combat | Mouvement | Attaque | Portée | PV | **Points** |
|---|---|---|---|---|---|---|
| Créature | Mêlée | 2 | 4 dés | — | 5 | **7** |

**Règles spéciales :** [Charge écrasante] + [Peur 1]

**Règle intrinsèque du type :** Jamais Faible (Créature) — 5 PV encaissés sans jamais subir la pénalité de dernière figurine.

**Note narrative :** un Olog-hai tiré des fosses de Gorgoroth, une masse de muscle et de fer qui balaie les rangs d'un revers de gourdin ([Charge écrasante] : la Couronne inflige une touche à une unité adjacente à la cible) et dont la seule approche fait plier le courage des hommes ([Peur 1] : chaque **Arcane** obtenue compte comme 1 Drapeau contre la cible). Un Troll si terrible que même ses coups perdus sèment la terreur — l'Arcane, ailleurs un échec, devient chez lui une source d'effroi.

> 🎲 **Note de design — plus de conflit de Couronne** : depuis que [Peur] passe par la face **Arcane** (D033), le Troll exploite deux faces distinctes — la Couronne pour [Charge écrasante], l'Arcane pour [Peur]. Les deux ne se marchent plus dessus.
>
> ✅ **Validé (2026-07-20)** : [Peur 1] (modéré — Peur 2/« Terreur » reste réservée aux Nazgûl et au Roi-Sorcier en Phase 2, pour garder une gradation) ; 5 PV (cohérent avec le reste du roster, pas une éponge hors-norme).
> ⚠️ **Seul point encore provisoire (non bloquant)** : coût de [Peur X] fixé à 2×X — non testé en partie réelle, à surveiller au Playtest #1 (même statut que le coût de [Horde]). Note : les Drapeaux ne tuent pas (ils font reculer) — peut-être 1×X après un premier test.

> 🔗 **Voir aussi** [[Regles_Speciales]] — [Charge écrasante] · [Peur X] · règle intrinsèque Créature

---

## 3. Trio du Playtest #1 (choix d'Emmanuel)

**Bande d'orques du Mordor (5) + Bande d'uruk-hai (7) + Troll du Mordor (7) = 19 points.**

> 🎲 **Note de design** Trio volontairement **haut de gamme** (19 pts, contre 15 Gondor / 13 Rohan) : il teste en priorité les deux mécaniques neuves — [Horde] (orques de base) et [Peur] (Troll, face Arcane) — plus la pièce signature. Il ne met pas en avant l'identité « nombre » du peuple, mais c'est le bon choix pour un rodage de règles.
>
> ⚠️ **À noter** : la description de la tâche Todoist visait « infanterie orque, tir » — ce trio n'a pas d'unité de tir (pisteurs absents). Si tu veux valider le tir au Playtest #1, ajoute les pisteurs en 4ᵉ slot.

---

## 4. Récapitulatif des règles spéciales utilisées

| Règle | Unités qui la portent |
|---|---|
| [Horde] | Bande d'orques du Mordor (1) · Bande d'orques du Morannon (2) |
| [Armure 1] | Bande d'orques du Morannon (2) · Bande d'uruk-hai (5) |
| [Férocité] | Meute de cavaliers wargs (4) · Bande d'uruk-hai (5) |
| [Mobilité 1] | Bande de pisteurs orques (3) |
| [Charge écrasante] | Troll du Mordor (6) |
| [Peur 1] *(face Arcane)* | Troll du Mordor (6) |

---

## 5. Règle à répercuter dans le socle — [Peur X]

Voir le doc de mise à jour du socle (blocs à insérer dans [[Regles_Speciales]], [[Regles_Points]] et [[Document de cadrage]]). Résumé :

**[Peur X]** *(Offensif — Mêlée/Distance)* : lorsque cette unité attaque, chaque face **Arcane** obtenue compte comme **X Drapeaux (retraites)** contre la cible, au lieu d'être un échec. N'inflige pas de touche : la Peur fait rompre, elle ne tue pas. Peut être annulée par l'[Inébranlable X] de la cible (un ennemi inébranlable résiste à l'effroi).

- **Première assignation** : Troll du Mordor.
- **Déclencheur** : la face **Arcane** (D033) — premier usage concret de la future couche Leadership (Œil de Sauron / Rune de Gandalf, D034).
- **Coût provisoire** : 2 × X. Non testé — à caler après un premier usage (comme [Déploiement avancé] et [Horde]).

---

## 6. Points restants — non bloquants pour le Playtest #1

Tout est validé pour lancer le Playtest #1. Rien ne bloque, mais deux choses à garder en tête (même statut que [Déploiement avancé] pour Rohan ou le compromis PV de l'Aurige pour Khand à leur clôture) :

1. **Coût de [Horde]** (3 pts forfaitaires, D032) — première assignation réelle (Bande d'orques du Mordor, Bande d'orques du Morannon) mais jamais testée en partie. À surveiller en priorité au Playtest #1.
2. **Coût de [Peur X]** (2×X, D033) — première assignation (Troll, [Peur 1]) également non testée. Piste de correction si trop cher : 1×X, puisque l'effet ne fait que reculer (pas de touche).

**Aucune unité composite** nommée dans ce roster (type Compagnie Grise) — le point ouvert de [[Regles_Points]] §5 reste sans objet pour Mordor.

**Couche Leadership (Phase 2)** — dé-randomiser l'accès des héros à la face Arcane ; arbitrer la propriété de l'Arcane quand une unité [Peur] et un héros coïncident (D034). Hors scope de ce roster, mais à garder en tête pour la suite.

---

*Version : 0.3 — Phase 1 — 2026-07-20. **Roster validé et clos (D036)** : Uruk-hai confirmé avec [Férocité] (7 pts) ; Troll confirmé à [Peur 1] et 5 PV (7 pts) ; Pisteurs orques confirmés sans [Horde] (3 pts). Les 6 profils sont validés tels que chiffrés en Passe 0 — aucun recalcul nécessaire. Prêt pour le Playtest #1 (trio : Bande d'orques + Uruk-hai + Troll, 19 pts). Restent uniquement les coûts de [Horde] et [Peur X] à confirmer au playtest (§6, non bloquant).*
