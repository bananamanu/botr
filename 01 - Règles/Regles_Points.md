---
projet: "Batailles de la Terre du Milieu"
type: "regles"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-08-16"
tags: [BdTdM, "type/regles", "phase/1", "statut/brouillon", "construction-armee"]
version: "0.25"
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

## 3. Suppléments : Faction, badge secondaire et signatures

*(Collapse de badges — D080/D081, tâche P7c.)* Le coût final d'un profil **standard** (hors pièces Signature, §6) se construit ainsi :

```
Brut = Brut_de_base (case, §5) + Coût(Faction du peuple) + Coût(badge secondaire, si porté) 
Final = round(Brut ÷ 3) − 1
```

**Faction n'est plus optionnelle : c'est un trait de peuple**, présent (ou non, cas rares documentés par peuple) sur **toute** unité standard sans que ce soit un choix de construction d'armée — son coût s'ajoute donc systématiquement pour les unités qui la portent, exactement comme avant, seule la présentation change (plus de case à cocher). **Le badge secondaire est plafonné à 1 par unité**, choisi parmi Spéciale/Élite/Légende — fini le cumul jusqu'à 3 badges secondaires (D073).

La compression (§4) se fait **une fois**, à la rédaction du profil, après avoir additionné tous les suppléments au brut de la case — jamais à la volée en partie.

### 3.1 Le badge secondaire — un seul par unité

- **Spéciale** confère **[Relance 1]**, universel depuis D073. **Coût : +2 brut** (tarif socle [Relance X] = 2×X).
- **Élite** confère **[Inébranlable 1] + Jamais Faible** (D073 : l'unité ignore l'état Faible, ses faces Épée touchent toujours). **Coût : +2 brut**, inchangé malgré l'enrichissement (Jamais Faible n'ajoute rien au forfait — provisoire, à surveiller au playtest).
- **Légende** (réservé aux unités uniques) ajoute **+1 dé** à l'attaque, dans son mode. **Coût : +3 brut en mêlée (D=3), +2 brut au tir (D=2)** — dérivé de la même méthode que le reste de la matrice (§5).

Une unité porte l'un des trois, ou aucun — jamais deux à la fois. Les collisions de coût que ce resserrement recrée localement (deux profils qui retombent au même palier) sont **acceptées par construction du système**, au même titre que les égalités déjà existantes ailleurs dans les rosters (ex. Hommes d'armes de Dol Amroth / Guerriers de Lossarnach, Gondor).

### 3.2 Le trait de Faction — coût par peuple

Chaque peuple a sa propre règle de Faction, définie une fois pour tout le roster ([[Regles_Speciales]] §4a) et son coût s'ajoute au brut de **toute** unité qui la porte :

| Peuple | Faction | Coût brut |
|---|---|---|
| Gondor, Orientaux | [Défense 1] *(= [Armure 1], nom d'usage)* | +2, **gratuit sur 🔴** (déjà au plancher intrinsèque) |
| Rohan | [Férocité] | +1 |
| Khand | [Mercenaire] | **−2** *(coût négatif)* |
| Mordor | [Horde] | +1 |
| Harad | [Poison] | +1 |

Cas particuliers sans Faction (documentés par peuple, [[Regles_Speciales]] §4a) : la Bande de pisteurs orques (Mordor, tir — le volet Faible de [Horde] ne mordrait pas sur une unité sans faces Épée actives) et l'Aurige de Khand (seul corps régulier du peuple, pas un mercenaire).

### 3.3 Barème des règles (Faction, badges, socle explicite)

Repris de l'Option B (D026), **élagué au tri P2** (D062), **réorganisé au collapse de badges P7c** (D081) : la colonne Note précise désormais si la règle est une **Faction** (peuple entier, §3.2), un **badge secondaire** (§3.1) ou du **socle libre**. Les règles devenues **intrinsèques** ne se facturent qu'en **excédent au-dessus du plancher de la case**.

| Règle | Coût | Note |
|---|---|---|
| **[Armure X] / [Défense X]** | 2 × X | Socle libre / **Faction Gondor-Orientaux** (nom [Défense X] en Faction). Sur 🔴, plancher [Armure 1] **inclus** → ne facturer que l'excédent. |
| **[Inébranlable X]** | 2 × X | Socle libre. Si l'unité est **Élite** (badge), le premier point est déjà dans le badge → ne facturer que l'excédent. |
| **[Protection X]** | 1 × X | Le plus souvent porté par le terrain. |
| **[Relance X]** | 2 × X | Socle libre / **badge Spéciale** (universel depuis D073, plafonné à 1 badge secondaire depuis D081). |
| **Légende** *(badge secondaire)* | 3 (mêlée) / 2 (tir) *(forfait, +1 dé)* | Réservé aux unités uniques, D073 — voir §3.1. |
| **[Arme de jet X]** | 1 × X | Sans porteur actif depuis D074 (Rohan migré vers [Férocité]). Conservée au barème, réutilisable. |
| **[Mercenaire]** | **−2** *(forfait, coût négatif)* | **Faction Khand**, P4/D070 — premier badge/trait à coût négatif du barème. |
| **[Poursuite X]** | 3 × X | Cavalerie de mêlée : plancher (2 ou 1) **inclus** → ne facturer que l'excédent. |
| **[Mobilité X]** | 1 × X | Tir léger/monté : plancher **inclus** → excédent seul. |
| **[Férocité]** | 1 | **Faction Rohan** — universelle sur tout le roster depuis D074. |
| **[Horde]** | **1** *(forfait)* | **Faction Mordor** (+1 dé à pleine santé, Faible dès la 1ʳᵉ touche). Refondue P4/D075 ; étendue à l'Uruk-hai P7c/D081, exclut la Bande de pisteurs orques (tir). Provisoire. |
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

**Guerriers de Minas Tirith** — 🔵 Infanterie, mêlée, Faction [Défense 1]. Base 🔵 Inf mêlée (brut 15) + [Défense 1] Faction (+2) = **17** → `round(17/3)−1` = **5**. *(Inchangé.)*

**Gardes de la Citadelle** — 🔵 Infanterie, mêlée, Faction [Défense 1] + badge **Élite**. Brut 15 + [Défense 1] (+2) + Élite (+2) = **19** → **5**. *(Inchangé.)*

**Chevaliers de Dol Amroth** — 🔴 Cavalerie, mêlée (base **23**, inclut [Armure 1] + [Poursuite 1] + prime de choc D065 — Faction [Défense 1] **gratuite**, déjà au plancher 🔴). **Depuis P7c (D081) : un seul badge secondaire.** Élite retenu (+2 → 25) → `round(25/3)−1` = **7**. *(Ancien coût : 8, avec Spéciale+Élite cumulés — perd 1 pt avec le plafond à 1 badge. Retombe à égalité avec Chevaliers de Minas Tirith, 7 pts — collision acceptée par Emmanuel, cf. Hommes d'armes/Lossarnach.)*

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

**Ouverts :**
1. **Bornes de l'échelle** — le plancher tombe à **3** (infanterie légère/tir léger) et le plafond monte à **~9** pour une cavalerie lourde maxée (Élite + [Armure 2] + signature, au-dessus de l'ancien 8 de BattleLore V2). À confirmer au playtest de la taxonomie (P7a) : bornes acceptables, ou faut-il resserrer la compression ?
2. **Re-expression des 6 rosters (P4)** : appliquer la matrice, retirer les [Poursuite]/[Armure] écrits en dur (redondants), trancher les armures de faction (ex. [Armure 2] Dol Amroth / Cataphractaires), reconfirmer chaque case type × mode × classe.
3. **Cartes bannière (vert/bleu/rouge)** — leur retour probable dans le deck de commandement active les unités **par couleur = classe**. Sans impact sur le coût unitaire (l'activation n'est pas tarifée au profil en C&C), mais **point de veille** : un roster trop concentré sur une couleur devient dur à activer — à intégrer à la conception du deck, pas au chiffrage.

---

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

*Version : 0.25 — Phase 1 — 2026-08-16. **Corrections de relecture — revue de finalisation « Verrouillage v1.0 ».** Lien `[[Document de cadrage]]` corrigé en `[[Document_de_cadrage]]` (nom réel du fichier). Aucune décision mécanique — pas de numéro D.*

*Version : 0.15 — Phase 1 — 2026-08-08. **[Arme de jet X] restaurée au barème** (P4, D068), 1×X — coupure P2 caduque.*

*Version : 0.14 — Phase 1 — 2026-08-08. **Renommage [Arme Lourde X] → [Relance X]** (P4, D066), répercuté dans le barème §3.2. Aucun changement de coût.*

*Historique antérieur (0.7 → 0.11) : formule brute par profil `Mvt + PV + Attaque×D + Σrègles` (D025) ; compression `round(÷3)−1` (D027) ; Option B du coût des règles (D026) ; cinq points de calibrage (Gondor, Rohan, Khand, Mordor, Easterling) ; coûts provisoires [Horde] (D032), [Peur X] (D033), [Mur de bouclier] (D037, coupée en P2), [Prise de flanc]/[Vigilant] (D049/D050), [Réception de charge] refondue puis coupée (D058/D062). Détail dans le [[Document_de_cadrage]] §8.*
