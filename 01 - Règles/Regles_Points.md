---
projet: "Batailles de la Terre du Milieu"
type: "regles"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-08-23"
tags: [BdTdM, "type/regles", "phase/1", "statut/brouillon", "construction-armee"]
version: "0.30"
---

# Batailles de la Terre du Milieu — Système de points

> **Objet de ce document (refonte P3, D064).** Depuis le pivot « taxonomie visuelle » (D059–D063), une unité standard n'est plus un profil libre mais une **combinaison (type × classe × mode)**, complétée d'un éventuel **badge Élite** et de **0–2 signatures**. Le coût n'est donc plus un calcul profil par profil : c'est la **lecture d'une case de matrice** + les suppléments Élite/signature. Ce document donne la matrice, sa dérivation (auditée), et le barème des suppléments.
>
> Aligné sur **[[Regles_Base]] v0.8** (taxonomie, grille de mouvement §6.1, intrinsèques §2.4, badge Élite §2.2) et **[[Regles_Speciales]] v0.16** (socle générique + signatures survivantes de P2).

---

## 1. Du calcul par profil à la matrice

Trois faits, hérités du pivot, rendent la matrice possible :

1. **La classe fixe l'attaque.** Le nombre de dés n'est plus libre (2–4) : il **est** la couleur — 🟢 2, 🔵 3, 🔴 4. Une variable de moins.
2. **Le type fixe la durabilité et les PV.** Infanterie 4 figurines, Cavalerie 3. La double-touche ayant disparu (**1 touche = 1 figurine**, [[Regles_Base]] §2.3), la durabilité **est** le nombre de figurines : ratio Inf:Cav = **4:3 = 1,33** — identique à l'ancien ratio de durabilité (12:9), mais désormais lisible sans aucun calcul. *(L'ancien §1 « durabilité effective ÷ perte moyenne » est caduc : sans double-touche, il n'y a plus rien à corriger.)*
3. **Le mode fixe le rendement du dé.** La mêlée touche sur deux faces (Épées croisées, Épée), le tir sur une (Cible) : un dé de mêlée vaut ~1,5× un dé de tir. On garde **D = 3 en mêlée, D = 2 au tir**.

**Conséquence directe du rebase de durabilité (Inf 6→4 PV).** Le terme PV de l'infanterie chute de 2 : l'infanterie à règles glisse d'environ **un palier vers le bas** (plus fragile, moins chère). C'est l'effet recherché. La cavalerie (PV inchangés à 3) bouge peu ; la cavalerie **lourde** perd un point de socle car la grille de mouvement lui donne Mvt 2 (elle troque désormais vitesse contre frappe, [[Regles_Base]] §6.1).

---

## 2. La matrice de base (unités standard)

Le coût **de base** d'une unité standard se lit dans cette table, selon sa case (type × mode × classe). Les **intrinsèques de la case (§2.4) sont déjà incluses** — on ne les refacture **jamais**.

| Type + mode | 🟢 (2 dés) | 🔵 (3 dés) | 🔴 (4 dés) |
|---|---|---|---|
| **Infanterie — mêlée** | **3** | **4** | **5** |
| **Infanterie — distance** | **3** | **3** | — |
| **Cavalerie — mêlée** | **5** | **6** | **7** |
| **Cavalerie — distance** | **3** | **3** | — |

*(Valeurs **finales**, prêtes pour la fiche. 🔴 + distance n'existe pas, D063.)*

Rappel des intrinsèques incluses (pour mémoire, **pas** à ajouter) : 🔴 → [Armure 1] ; cavalerie de mêlée → [Poursuite 2] (🟢/🔵) ou [Poursuite 1] (🔴) ; tir léger/monté → [Mobilité] (🟢 cav 2 ; 🟢 inf et 🔵 cav 1).

> **Prime de choc de la cavalerie lourde (D065).** La case **Cav 🔴 mêlée** porte **+1 brut** au-delà de sa dérivation mécanique : la charge blindée compounde plus que ne le dit le compte de dés linéaire, mais un dé entier de plus (dé lourd = 4) déborderait à 8 et toucherait aussi l'infanterie lourde. La prime est donc **réservée à la cavalerie** et dosée à **+1**, ce qui pose la case à **7** — et lui rend son ancien coût (Chevaliers de Dol Amroth). C'est le seul écart assumé entre la matrice et la formule brute.

---

## 3. Suppléments : Faction, Bannière, Leader/Général/Destin, règles socle

*(Troisième refonte des badges — D092/D093, Playtest #4 — architecture actée P8/D097.)* Le coût final d'un profil **standard** (hors pièces Signature, §6) se construit ainsi :

```
Brut = Brut_de_base (case, §5) + Σ Coût(chaque badge/règle porté)
Final = round(Brut ÷ 3) − 1
```

**Plus de plafond.** Une unité additionne librement : une éventuelle règle **socle générique** ([Relance X], [Inébranlable X]… — voir §3.1), le badge **Faction** de son peuple si elle est assignée à en porter une (§3.2, désormais ciblé plutôt qu'universel), le badge **Bannière** si une figurine porte-étendard l'incarne, le badge **Légende** si c'est une pièce unique, et le badge **Leader** (avec ses composantes Général/Destin optionnelles, §3.3) si un personnage nommé y est attaché. La compression (§4) se fait **une fois**, après avoir additionné tous les suppléments — jamais à la volée en partie.

### 3.1 Règles socle portées directement au profil *(ex-badges Spéciale/Élite, D073 — noms de badge abandonnés D092, effets et coûts inchangés)*

Ces deux effets restent au vocabulaire socle générique ([[Regles_Speciales]] §2) et se notent directement sur le profil qui les mérite, sans être rattachés à une catégorie de badge nommée :

- **[Relance 1]** *(ex-badge « Spéciale »)* : arme ou tir remarquable. **Coût : +2 brut.**
- **[Inébranlable 1] + Jamais Faible** *(ex-badge « Élite »)* : troupe aguerrie qui ne rompt jamais. **Coût : +2 brut.**

Rien ne change dans la façon dont les profils existants les portent (Gardes de la Citadelle, Chevaliers de Dol Amroth, Uruk-hai…) — seule la présentation (« badge » → « règle de profil ») est mise à jour.

### 3.2 Le badge Faction — outil optionnel à disposition, jamais un défaut (D101)

> ⚠️ **Correction D101 (sur D098) — simplification radicale poussée plus loin.** D098 liait encore l'apparition de Faction à la présence d'un badge Leader. Emmanuel a tranché plus loin : **aucune unité de base ne porte de badge d'office.** Faction est un **outil à disposition du concepteur de scénario/liste**, à poser sur une unité **éligible** (marquée au roster) pour créer ponctuellement un effet « troupe vétérante/élite » — indépendamment de la présence d'un Leader, et jamais un supplément automatique. Chaque roster indique désormais, ligne par ligne, si Faction et/ou Bannière sont des options disponibles pour cette unité. **Chantier en cours (P8)** : seul Gondor (`Gondor_et_Fiefs.md` v3.0) applique ce principe à ce stade — Rohan, Khand, Mordor, Orientaux, Harad restent au régime D097/D098 (Faction ciblée sur Leader) en attendant l'arbitrage du périmètre exact par peuple.

Chaque peuple garde sa règle de Faction propre, son tarif, et son **nom d'usage narratif** :

| Peuple | Faction | Coût brut |
|---|---|---|
| **Gondor** *(à jour, D101)* | « Défenseur de la Terre du Milieu » = [Relance 1] | **+2**, jamais gratuit *(remplace [Défense 1] — plus de plancher 🔴 à absorber)* |
| Orientaux | [Défense 1] *(= [Armure 1])* | +2, gratuit sur 🔴 — **à reconfirmer si le peuple suit Gondor vers [Relance 1]** |
| Rohan | [Férocité] | +1 |
| Khand | [Mercenaire] | **−2** *(coût négatif)* |
| Mordor | [Horde] | +1 |
| Harad | [Poison] | +1 |

**Où Faction reste utilisable, par roster :**
- **Gondor, Rohan, Khand, Harad** *(à jour, D101/D102)* : marquée disponible unité par unité au roster, jamais automatique — y compris pour les traits matériels (Poison, Mercenaire), sur arbitrage d'Emmanuel : même logique partout.
- **Orientaux, Mordor** : en attente de la nouvelle définition de la règle de Faction/[Horde] (Emmanuel doit préciser le texte) avant recalcul.

Cas particuliers sans Faction, inchangés : la Bande de pisteurs orques (Mordor, tir) et l'Aurige de Khand (seul corps régulier, pas un mercenaire).

### 3.3 Le badge Leader — Général et Destin (D093/D097)

Rattaché à une unité (jamais une figurine libre), le badge **Leader** ([[Regles_Base]] §2.2bis) se chiffre en trois composantes indépendantes, cumulables :

| Composante | Effet | Coût brut |
|---|---|---|
| **Leader** (toujours présente) | [Inébranlable 1] à soi **+ unités amies adjacentes**, touche supplémentaire sur Couronne | **+4** |
| **Général** *(optionnel)* | Main de commandement du camp +1 par Général vivant | **+9** *(forfait)* |
| **Destin** *(optionnel, 1 à 4)* | Jet de sauvetage à l'élimination de l'unité porteuse | **+2 par point** |

**Dérivation (palier « Marqué », validé Emmanuel, P8) :**
- Leader seul (+4) : la zone d'effet (soi + adjacentes) vaut environ le double de Bannière (+2, soi seul) ; la touche sur Couronne, comparable à la conversion d'une face jusque-là inerte, est incluse dans ce forfait plutôt que facturée à part (à la différence de [Poison], qui reste un cas socle indépendant).
- Général (+9) : le seul supplément du barème qui n'agit pas sur l'unité porteuse mais sur **tout le camp**, chaque tour, toute la partie — un point de main en plus vaut largement plus qu'un dé de combat en plus sur une seule unité. Prix délibérément lourd : à ce tarif, un Général bien équipé (Leader + Général + Destin moyen) coûte environ le **double** du coût de base de l'unité qui le porte.
- Destin (+2/point) : assurance-vie graduée, dans la même logique tarifaire que [Protection X] (+1×X) mais un cran au-dessus car elle porte sur l'élimination complète, pas une simple touche.

Un Leader qui ne prend pas le statut Général (les « Leaders mineurs » du Pelennor — Suladan, le Roi de Khand, Angbor le Brave, Forlong le Gros) ne paie que Leader + Destin, sensiblement moins cher qu'un Général en pleine tenue.

> ⚠️ **Roi-Sorcier sur l'ombre ailée — cas extrême signalé.** Général universel + Destin 4 sur un profil bespoke déjà coûteux (§6, `02 - Factions/Mordor.md`) fait grimper la pièce à **17 pts**, au-dessus du Mûmakil (15). Défendable narrativement (le chef des Nazgûl est la pièce la plus dangereuse du Pelennor) mais c'est le prix le plus élevé du projet à ce jour — à confirmer avec Emmanuel, sans quoi il faudra soit plafonner les pièces bespoke les plus chargées, soit accepter ce nouveau sommet d'échelle.

### 3.4 Barème des règles (Faction, socle, signatures)

Repris de l'Option B (D026), **élagué au tri P2** (D062), **réaligné P8** (D097/D098) : la colonne Note précise désormais si la règle est une **Faction** (ciblée par unité, §3.2), une **règle socle libre** (§3.1) ou un badge de la famille **Leader** (§3.3). Les règles devenues **intrinsèques** ne se facturent qu'en **excédent au-dessus du plancher de la case**.

| Règle | Coût | Note |
|---|---|---|
| **[Armure X] / [Défense X]** | 2 × X | Socle libre / **Faction Orientaux** *(Gondor a migré vers [Relance 1], voir `Gondor_et_Fiefs.md`)*. Sur 🔴, plancher [Armure 1] **inclus** → ne facturer que l'excédent. |
| **[Armure]** *(sans X, Créatures)* | **0** *(intrinsèque)* | D103, P8 — remplace [Armure 1]+[Protection 1] pour le type Créature. Jet de sauvetage 1d6 (Arcane annule, +Couronne si Leader), toujours gratuit comme l'ancien [Armure 1]. |
| **[Inébranlable X]** | 2 × X | Socle libre. Si l'unité porte déjà [Inébranlable 1] via Bannière ou Leader, le premier point est inclus → ne facturer que l'excédent. |
| **[Inébranlable ∞]** | 6 *(forfait, bespoke)* | ≈3× le forfait standard [Inébranlable 1] — jugement par analogie (D079). Porteurs : Mûmakil, Garde du Roi (Rohan, P8). |
| **[Protection X]** | 1 × X | Le plus souvent porté par le terrain. *(Sur les Créatures, supersedée par [Armure] — D103.)* |
| **[Relance X]** | 2 × X | Socle libre — ex-badge « Spéciale » (D073), nom de badge abandonné D092, coût inchangé. |
| **Légende** *(badge, pièces uniques)* | 3 (mêlée) / 2 (tir) *(forfait, +1 dé)* | D073 — voir [[Regles_Speciales]] §Conventions. |
| **[Inébranlable 1] + Jamais Faible** | 2 *(forfait)* | Socle libre — ex-badge « Élite » (D073), nom de badge abandonné D092, coût inchangé. **Ne fait plus partie du menu d'options standard depuis P8 (D101/D102)** — ne survit que dans les pièces signature. |
| **[Bannière]** | 2 *(forfait, [Inébranlable 1])* | Badge, D092 — figurine porte-étendard, cumulable avec tout le reste. **Jamais disponible chez Khand** (D102bis, arbitrage Emmanuel — troupes trop disparates pour porter un étendard commun). |
| **[Leader]** | 4 *(forfait)* | Badge, D093/D097 — Inébranlable 1 (soi + adjacentes) + touche sur Couronne. |
| **[Général]** *(add-on de Leader)* | 9 *(forfait)* | D093/D097 — main de camp +1 par Général vivant. Prix délibérément lourd, effet de camp. |
| **[Destin X]** *(add-on de Leader)* | 2 × X | D093/D097 — X de 1 à 4, jet de sauvetage à l'élimination. |
| **[Arme de jet X]** | 1 × X | Sans porteur actif depuis D074 (Rohan migré vers [Férocité]). Conservée au barème, réutilisable. |
| **[Mercenaire]** | **−2** *(forfait, coût négatif)* | **Faction Khand**, P4/D070 — devenu option (D102), jamais un défaut. |
| **[Poursuite X]** | 3 × X | Cavalerie de mêlée : plancher (2 ou 1) **inclus** → ne facturer que l'excédent. |
| **[Mobilité X]** | 1 × X | Tir léger/monté : plancher **inclus** → excédent seul. |
| **[Férocité]** | 1 | **Faction Rohan** — devenue option (D101), disponible sur 1-7 ; en dur sur la Garde du Roi jusqu'à P8 (retirée, voir D107). |
| **[Discipline de cohorte]** | **2** *(forfait)* | **Faction Orientaux**, D104, P8 — remplace [Défense X]. Posture activée : renonce à la riposte, gagne [Défense 1]+[Inébranlable 1]. Disponible sur les Cohortes (guerriers, piquiers) uniquement. |
| **[Horde]** *(troisième version)* | **3** *(forfait)* | **Faction Mordor**, D105, P8 — +1 dé et Inébranlable 1 à pleine santé, aucun effet négatif ensuite. Disponible sur tous les orques (bandes, Uruk-hai, Piétaille orque, wargs). |
| **[Peur 1 contre les bannières vertes]** | **2** *(forfait, bespoke)* | D106, P8 — signature Aurige de Khand. Cible uniquement la classe 🟢. |
| **[Mur de bouclier]** | **1** *(forfait)* | Sans porteur actif depuis P7c/D081 — [Protection 1] tant qu'aucune touche subie, perdue à la 1ʳᵉ. Conservée au barème, réutilisable. |
| **[Poison]** | 1 | **Faction Harad** — universelle sur tout le roster d'escorte. |
| **[Double Tir]** | 3 | Sans porteur actif depuis P4/D072. Conservée au barème, réutilisable. |
| **[Prise de flanc]** | 3 *(forfait)* | Signature Éored de cavalier. Provisoire, D049. |
| **[Vigilant]** | 2 *(forfait)* | Signature Éored d'éclaireur. Provisoire, D050. |
| **[Archer en mêlée]** | 2 | Signature Compagnie Grise. |
| **[Peur X]** | *(intrinsèque Créature — voir note)* | Devenue intrinsèque au type Créature (P4/D071), plus une signature au barème. Toute créature en porte 1 sans supplément. |

> **Retirées au tri P2** (ne plus chiffrer) : [Réception de charge], [Martyre], [Meute X], [Souffle de feu], immunités, [Terrain favori], [Rechargement], [Déploiement avancé]. Traçabilité : [[Regles_Speciales]] §6. *([Arme de jet X] restaurée au barème ci-dessus, P4/D068.)*

> **Pièces bespoke** (Mûmakil : [Charge écrasante], [Bête incontrôlable], [Howdah]) : **hors barème**, absorbées dans le chiffrage par équivalence de la pièce (§6). *(Le type Chars et [Plateforme de tir X] n'ont plus de porteur depuis P4/D070 — l'Aurige de Khand devient cavalerie standard, chiffrée à la matrice comme toute autre unité.)*

---

## 4. Compression de l'échelle (D027, inchangée)

```
Points_finaux = round(Points_bruts ÷ 3) − 1
```

Ramène le roster sur une échelle resserrée et mémorisable, calée sur BattleLore V2. Avec le rebase de durabilité, la fourchette standard est désormais **3 à 8** (le plancher descend à 3 pour l'infanterie légère et le tir léger — sain : ce sont les unités les plus jetables). L'effet d'absorption reste vrai : sur une case bon marché, un petit supplément (Élite, [Poison]) ne change parfois pas le final — normal, le système est peu sensible aux petits ajustements sur les unités peu chères.

---

## 5. Dérivation de la matrice (audit)

Pour traçabilité — la matrice du §2 découle mécaniquement de la formule brute appliquée à chaque case.

**Socle = Mvt (grille §6.1) + PV (Inf 4 / Cav 3) :**

| | 🟢 | 🔵 | 🔴 |
|---|---|---|---|
| **Infanterie** (PV 4) | 2+4 = 6 | 2+4 = 6 | 1+4 = 5 |
| **Cavalerie** (PV 3) | 4+3 = 7 | 3+3 = 6 | 2+3 = 5 |

**Attaque × D** (D = 3 mêlée / 2 tir) : 🟢 6/4 · 🔵 9/6 · 🔴 12/— (mêlée/tir).

**Assemblage (Brut → Final) :**

| Case | Socle | Atk×D | Intrinsèques | **Brut** | **Final** |
|---|---|---|---|---|---|
| Inf 🟢 mêlée | 6 | 6 | — | 12 | **3** |
| Inf 🔵 mêlée | 6 | 9 | — | 15 | **4** |
| Inf 🔴 mêlée | 5 | 12 | Armure 1 (2) | 19 | **5** |
| Inf 🟢 distance | 6 | 4 | Mobilité 1 (1) | 11 | **3** |
| Inf 🔵 distance | 6 | 6 | — | 12 | **3** |
| Cav 🟢 mêlée | 7 | 6 | Poursuite 2 (6) | 19 | **5** |
| Cav 🔵 mêlée | 6 | 9 | Poursuite 2 (6) | 21 | **6** |
| Cav 🔴 mêlée | 5 | 12 | Pours. 1 + Arm. 1 (5) + choc (1) | 23 | **7** |
| Cav 🟢 distance | 7 | 4 | Mobilité 2 (2) | 13 | **3** |
| Cav 🔵 distance | 6 | 6 | Mobilité 1 (1) | 13 | **3** |

> 🎲 **Note.** Le terme Attaque utilise l'attaque **de base**. Pour une unité [Horde], le +1 dé est déjà payé dans le forfait de la règle — ne pas le compter deux fois. La ligne **Cav 🔴 mêlée** inclut la **prime de choc** (+1, D065) : seul écart assumé entre la dérivation et la formule brute.

---

## 6. Créatures, Chars et pièces uniques (hors matrice)

Les **Créatures** (Mûmakil, Troll) et **Chars** (Aurige de Khand) se comptent en PV, sortent de la grille type × classe. **Depuis P5 (D079)**, le Mûmakil applique la dérivation brute standard (socle Mvt+PV, Attaque×D, signatures tarifées) à tout ce qui est chiffrable au barème, et ne réserve le jugement par équivalence qu'aux règles réellement bespoke ([Charge écrasante], [Inébranlable ∞]) — voir le détail du calcul dans `02 - Factions/Harad.md` §3.7. Nouveau coût : **15 pts** (ancien : 21 pts, pure équivalence narrative). Le Troll et l'Aurige de Khand restent chiffrés par équivalence narrative pure, non revus à ce stade. Idem pour les **composites nommés** (La Compagnie Grise, chiffrée à pleine puissance — D026).

---

## 7. Exemples travaillés

**Guerriers de Minas Tirith** — 🔵 Infanterie, mêlée, aucune Faction assignée (ciblage D098 : pas de Leader dans cette unité, pas un trait matériel). Base 🔵 Inf mêlée (brut 15) = **15** → `round(15/3)−1` = **4**. *(Baisse de 5→4 : Faction n'étant plus universelle, l'unité de ligne « propre » redescend à son coût de matrice nu.)*

**Gardes de la Citadelle** — 🔵 Infanterie, mêlée, [Inébranlable 1] + Jamais Faible (règle socle, ex-badge Élite). Brut 15 + (+2) = **17** → `round(17/3)−1` = **5**. *(Inchangé — la règle socle est indépendante du ciblage de Faction.)*

**Chevaliers de Dol Amroth** — 🔴 Cavalerie, mêlée (base **23**, inclut [Armure 1] + [Poursuite 1] + prime de choc D065 — Faction [Défense 1] **gratuite** de toute façon sur 🔴). [Inébranlable 1] + Jamais Faible (+2 → 25) → `round(25/3)−1` = **7**. *(Coût de base inchangé par rapport à l'ère P7c — Faction n'y coûtait déjà rien.)*

**Chevaliers de Dol Amroth — variante avec Imrahil** (Général, Destin 3, Playtest #4) : brut 23 + Élite (2) + [Défense 1] Faction (0, gratuite 🔴) + Leader (4) + Général (9) + Destin 3 (6) = **44** → `round(44/3)−1` = **14**. *(La composante Général domine largement le calcul — cohérent avec le tarif délibérément lourd de §3.3.)*

---

## 8. Décisions actées et points ouverts

**Actés (D064, 2026-08-05) :**
- Passage à la **matrice** (type × mode × classe), intrinsèques incluses par case ; suppléments Élite + signatures ajoutés au brut avant compression.
- **Rebase durabilité** : Inf 6→4 PV, Cav 3 ; socle Mvt+PV recalculé sur la grille §6.1.
- **Élite = [Inébranlable 1]**, +2 brut.
- **[Armure X] = règle de faction** ouverte à toute classe (pas verrouillée au rouge) ; sur 🔴, seul l'excédent au-dessus du plancher [Armure 1] est facturé.

**Ajusté (D065, 2026-08-05) :**
- **Prime de choc de la cavalerie lourde** : +1 brut sur la seule case **Cav 🔴 mêlée** (22→23 → final **6→7**). Supersède la valeur Cav 🔴 mêlée de D064. Réservée à la cavalerie et dosée à +1 (un dé lourd = 4 déborderait à 8 et toucherait l'infanterie). Rend son ancien coût de 7 à la cavalerie lourde.

**Hérités, toujours provisoires (à caler en jeu) :** [Horde] (D032), [Peur X] (D033), [Prise de flanc] (D049), [Vigilant] (D050).

**Actés (D097/D098, P8, 2026-08-23) :**
- **Architecture badges troisième refonte répercutée** : plus de plafond, Faction ciblée par unité (§3.2), règles socle ex-Spéciale/Élite renommées sans changement de coût (§3.1), Leader/Général/Destin chiffrés (§3.3, palier « Marqué » validé Emmanuel).
- **Bornes de l'échelle** — dépassées volontairement par le haut : un Général en pleine tenue peut atteindre 12-14 pts, le Roi-Sorcier culmine à 17 (au-dessus du Mûmakil, 15) — nouveau sommet du projet, signalé §3.3. Les bornes 3-9 restent valables pour les unités **standard** (sans Leader).

**Ouverts :**
1. **Roi-Sorcier à 17 pts** — au-dessus du Mûmakil, à confirmer avec Emmanuel (voir avertissement §3.3) : accepter ce nouveau sommet, ou plafonner les pièces bespoke les plus chargées ?
2. **Équilibre du scénario Pelennor** — le recalcul complet des deux camps (`02 - Factions/*.md`, P8) donne un total très proche (219 Bien / 220 Mal, voir compte-rendu P8) : l'ancien gap de 9 pts semble largement résorbé par le nouveau chiffrage Leader/Général plutôt que par un ajustement volontaire d'effectifs. À confirmer si ce résultat est jugé suffisant ou s'il appelle un ajustement fin.
3. ~~**Cartes bannière (vert/bleu/rouge)**~~ — **résolu (D088)** : intégrées au deck sous le nom Classe Verte/Bleue/Rouge, activation par couleur = classe, sans impact sur le coût unitaire (l'activation n'est pas tarifée au profil en C&C). Le risque signalé (roster mono-couleur dur à activer) reste un point de vigilance pour la conception des rosters, mais n'est plus un point ouvert côté deck — voir [[Cartes_Commandement]] §4.2.

---

*Version : 0.30 — Phase 1 — 2026-08-23. **P8 — Retouches de barème (D103-D107).** Nouvelle règle [Armure] (Créatures, D103) intrinsèque, remplace [Armure 1]+[Protection 1]. [Discipline de cohorte] (D104, Faction Orientaux, +2) et [Horde] troisième version (D105, Faction Mordor, +3, plus d'effet négatif) ajoutées au barème. Nouvelle signature bespoke [Peur 1 contre les bannières vertes] (D106, Aurige de Khand, +2). Bannière retirée du barème disponible chez Khand (jamais). [Inébranlable ∞] entre au barème (6, bespoke) avec un second porteur (Garde du Roi, Rohan).*

*Version : 0.29 — Phase 1 — 2026-08-23. **Correction D101 (simplification radicale, sur D098).** §3.2 réécrite : Faction n'est plus liée à la présence d'un Leader — c'est un **outil optionnel** à disposition, marqué disponible unité par unité au roster, jamais un supplément automatique. Gondor appliqué à ce principe (`Gondor_et_Fiefs.md` v3.0, Faction devient « Défenseur de la Terre du Milieu » = [Relance 1], +2 brut toujours). Rohan/Khand/Mordor/Orientaux/Harad restent au régime transitoire D097/D098 en attendant l'arbitrage du périmètre par peuple — signalé explicitement dans le texte.*

*Version : 0.28 — Phase 1 — 2026-08-23. **P8 — Chantier de recalcul complet (D097/D098).** §3 entièrement réécrite : plus de plafond de badge, Faction ciblée par unité (§3.2, principe D098 — traits matériels universels vs traits de prestige réservés aux porteurs de Leader), règles ex-Spéciale/Élite renommées « socle » sans changement de coût (§3.1), badge Leader chiffré en trois composantes Leader/Général/Destin (§3.3, palier « Marqué » validé Emmanuel : +4/+9/+2 par point). Barème §3.4 mis à jour. Exemples §7 recalculés (Guerriers de Minas Tirith 5→4 ; Chevaliers de Dol Amroth avec Imrahil, nouvel exemple à 14 pts). §8 : point ouvert sur le prix du Roi-Sorcier (17 pts, nouveau sommet) et sur l'équilibre Pelennor (recalcul donnant 219/220, quasi-parité). Détail du recalcul des 6 rosters dans `02 - Factions/*.md` et le nouveau profil Roi-Sorcier dans `Mordor.md`.*

*Version : 0.27 — Phase 1 — 2026-08-22. **Playtest #4 joué — pivot badges signalé, non répercuté (D092/D093).** Avertissement ajouté en tête de §3 : Spéciale/Élite abandonnés, Faction redevient un badge par unité (§3.1/§3.2 marquées historiques), nouveau badge Bannière au tarif [Inébranlable 1] (+2, provisoire), coût de Leader/Général non chiffré (Emmanuel : doit être significatif). Recalcul complet des 6 rosters et refonte de ce document renvoyés au chantier **P8**. Voir `[[Playtest4_Compte-rendu]]`.*

*Version : 0.26 — Phase 1 — 2026-08-16. **D088 — clôture du point de veille D064 sur les cartes bannière.** §8 : point ouvert #3 marqué résolu — les cartes bannière reviennent sous le nom Classe Verte/Bleue/Rouge dans `[[Cartes_Commandement]]` §4.2, activation par couleur = classe, sans impact sur le chiffrage. Aucun changement de coût dans ce document.*

*Version : 0.25 — Phase 1 — 2026-08-16. **Corrections de relecture — revue de finalisation « Verrouillage v1.0 ».** Lien `[[Document de cadrage]]` corrigé en `[[Document_de_cadrage]]` (nom réel du fichier). Aucune décision mécanique — pas de numéro D.*

*Version : 0.24 — Phase 1 — 2026-08-13. **Collapse du système de badges (D080/D081, tâche P7c).** §3 réécrite : Faction (§3.2) devient un trait de peuple systématique par unité (barème inchangé par peuple), badge secondaire (§3.1) plafonné à **1** parmi Spéciale/Élite/Légende (fin du cumul jusqu'à 3, D073). Barème §3.3 réorganisé avec la colonne Note distinguant Faction / badge secondaire / socle libre ; [Défense X] ajoutée (= [Armure X], nom Faction Gondor-Orientaux) ; [Mur de bouclier] repasse sans porteur actif. Exemple Dol Amroth (§7) recalculé : 8→**7 pts** (perd le cumul Spéciale+Élite, un seul badge retenu — Élite). Collisions de coût locales acceptées par construction.*

*Version : 0.12 — Phase 1 — 2026-08-05. **Refonte P3 (D064) : passage en matrice.** Réécriture complète autour de la matrice type × mode × classe (§2), intrinsèques incluses par case. Rebase durabilité (Inf 6→4, Cav 3) ; socle Mvt+PV recalculé sur la grille §6.1 ; ancien §1 (durabilité ÷ perte moyenne) caduc (double-touche supprimée). Badge Élite = [Inébranlable 1] (+2). [Armure X] rouverte à toute classe comme règle de faction (excédent seul sur rouge). Barème des règles élagué au tri P2 (retrait des règles coupées ; intrinsèques facturées en excédent). Dérivation auditée (§5), exemples (§7). Créatures/Chars/composites hors matrice (équivalence). Fourchette 3–8. Non testé — validation P7a puis Playtest Pelennor.*

*Version : 0.13 — Phase 1 — 2026-08-05. **Prime de choc de la cavalerie lourde (D065).** +1 brut sur la seule case Cav 🔴 mêlée (22→23), portant son coût final de 6 à **7** (matrice §2, dérivation §5, exemple Dol Amroth §7). Supersède la valeur Cav 🔴 mêlée de D064. Réservée à la cavalerie et dosée à +1 (un dé lourd = 4 aurait débordé à 8 et touché aussi l'infanterie lourde). Rend son ancien coût de 7 à la cavalerie lourde. Nouveau plafond ~9 pour une pièce de choc maxée. Non testé.*

*Version : 0.23 — Phase 1 — 2026-08-09. **Repricing du Mûmakil (D079, P5).** §6 : le Mûmakil applique désormais la dérivation brute standard partout où c'est calculable, et ne réserve le jugement d'équivalence qu'aux deux règles réellement bespoke (Charge écrasante, Inébranlable ∞). Coût 21→**15 pts**. Détail du calcul dans `02 - Factions/Harad.md`.*

*Version : 0.22 — Phase 1 — 2026-08-08. **[Mur de bouclier] ajoutée au barème (D077)**, 1 pt forfait — redevient le badge Faction des Orientaux, remplace [Armure 1] (D072 caduque).*

*Version : 0.21 — Phase 1 — 2026-08-08. **[Horde] refondue (D075)** : coût 2→1 (forfait). Migration Mordor du badge Spéciale vers [Relance 1] actée — tous les peuples déjà re-exprimés sont désormais conformes au badge Spéciale universel (D073).*

*Version : 0.20 — Phase 1 — 2026-08-08. **Migration Rohan actée** (D074) : Rohan retiré de la liste des peuples en attente de badge Spéciale universel. Seul Mordor reste à migrer.*

*Version : 0.19 — Phase 1 — 2026-08-08. **Pivot transverse « badges universels » (D073).** §3.1 : badge Élite enrichi (+ Jamais Faible), coût inchangé (+2). Nouveau **§3.1bis badge Légende** (+1 dé de combat, +3 brut mêlée / +2 tir), réservé aux unités uniques — remplace le régime « hors matrice, équivalence narrative » pour les pièces dont les règles se ramènent à un empilement de badges. Nouveau **§3.2 badge Spéciale universel** : [Relance 1] pour tous les peuples (ancien §3.2 renuméroté §3.3). Répercussions sur Rohan/Mordor (badge Spéciale à migrer) renvoyées à leur propre passage.*

*Version : 0.18 — Phase 1 — 2026-08-08. **[Double Tir] sans porteur actif** (P4/D072, Orientaux passés en miroir mécanique pur de Gondor — Faction [Armure 1] + Spéciale [Relance 1] plutôt que la signature de peuple). Barème inchangé, conservé pour réutilisation future.*

*Version : 0.17 — Phase 1 — 2026-08-08. **[Horde] nerfée** (P4, D071), forfait 3→2. **[Peur X] devenue intrinsèque au type Créature** (toute créature en porte 1 sans supplément), retirée du barème à cocher au profil.*

*Version : 0.16 — Phase 1 — 2026-08-08. **[Mercenaire] ajoutée au barème** (P4, D070), −2 forfait — premier coût négatif du système. Type Chars et [Plateforme de tir X] retirés des pièces bespoke (sans porteur, l'Aurige de Khand devient cavalerie standard).*

*Version : 0.15 — Phase 1 — 2026-08-08. **[Arme de jet X] restaurée au barème** (P4, D068), 1×X — coupure P2 caduque.*

*Version : 0.14 — Phase 1 — 2026-08-08. **Renommage [Arme Lourde X] → [Relance X]** (P4, D066), répercuté dans le barème §3.2. Aucun changement de coût.*

*Historique antérieur (0.7 → 0.11) : formule brute par profil `Mvt + PV + Attaque×D + Σrègles` (D025) ; compression `round(÷3)−1` (D027) ; Option B du coût des règles (D026) ; cinq points de calibrage (Gondor, Rohan, Khand, Mordor, Easterling) ; coûts provisoires [Horde] (D032), [Peur X] (D033), [Mur de bouclier] (D037, coupée en P2), [Prise de flanc]/[Vigilant] (D049/D050), [Réception de charge] refondue puis coupée (D058/D062). Détail dans le [[Document_de_cadrage]] §8.*
