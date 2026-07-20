---
projet: "Batailles de la Terre du Milieu"
type: "regles"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-07-20"
tags: [BdTdM, "type/regles", "phase/1", "statut/brouillon", "construction-armee"]
version: "0.7"
---

# Batailles de la Terre du Milieu — Système de points

> **Objet de ce document :** Première proposition de formule de coût en points pour la construction d'armée (feuille de route Phase 3, [[Document de cadrage]] §6). Répond directement à D025 : les dominances strictes assumées en V1 (Chevaliers de Dol Amroth sur Chevaliers de Minas Tirith ; Archers de la Racine Noire sur Rangers d'Ithilien) doivent se refléter dans un écart de coût plutôt que dans une retouche de profil.
>
> Calibrée et testée sur les 14 profils de [[Gondor_et_Fiefs]], puis sur les rosters **Rohan** (9 profils), **Khand** (5 profils) et **Mordor** (6 profils, D036) comme points de calibrage successifs. Le roster **Easterling** (`02 - Factions/Easterling.md`, validé et clos, D038) sert de cinquième point de calibrage — première application réelle de la nouvelle règle [Mur de bouclier] (D037) et première assignation de [Double Tir].

---

## 1. Pourquoi cette forme de formule

Trois remarques structurantes avant la formule elle-même :

**Le Mouvement et les PV ne varient quasiment pas entre profils d'un même Type.** Le [[Document de cadrage]] fixe PV et Mouvement par Type (Infanterie : 6 PV / Mvt 2 ; Cavalerie : 3 PV / Mvt 3), avec de rares exceptions (Chevaliers à pied de Dol Amroth, Mouvement 1 ; Éored d'éclaireur du Rohan, Mouvement 4 ; Aurige de Khand, PV ramené à 3 pour sa 3e règle signature). Concrètement, ces deux stats ne différencient presque jamais deux profils entre eux — ce qui varie vraiment, c'est l'**Attaque** (2 à 4 dés) et les **règles spéciales**. La formule ci-dessous en tient compte : Mouvement et PV forment un "socle" quasi fixe par Type, l'Attaque et les règles font tout le travail de différenciation.

**L'Attaque vaut plus cher en Mêlée qu'au Tir, à dé égal.** Sur les 6 faces de dé, la Mêlée touche sur *deux* faces (Épées croisées, Épée) alors que le Tir n'en a qu'*une* (Cible) — voir [[Regles_Base]] §7.2-7.3. Un dé de Mêlée produit donc, en moyenne, environ 1,5× plus de dégâts attendus qu'un dé de Tir contre une cible d'Infanterie. La formule reflète ce ratio (3 points/dé en Mêlée contre 2 points/dé au Tir) plutôt que de traiter tous les dés pareil.

**Les PV n'ont pas le même "poids" chez tous les Types — mais une fois le Mouvement ajouté, le socle se recale tout seul.** Un dé Épées croisées/Cible retire 2 PV à une cible Infanterie mais seulement 1 à une cible Cavalerie ([[Regles_Base]] §2.3) — la Cavalerie encaisse donc moins de PV bruts (3 contre 6) mais les perd moins vite par touche. **Vérification (2026-07-19) :** en calculant la durabilité effective en Mêlée (PV ÷ perte moyenne de PV par dé encaissé, faces Épée + Épées croisées), Infanterie = 6 ÷ 0,5 = 12 dés nécessaires pour l'éliminer, Cavalerie = 3 ÷ 0,333 ≈ 9 dés — soit un ratio de **12:9 = 1,33:1**. Comparé au socle Mouvement + PV de la formule (Infanterie 2+6=8, Cavalerie 3+3=6, ratio **8:6 = 1,33:1**), les deux ratios sont identiques. Le Mouvement plus coûteux de la Cavalerie compense exactement le fait que ses PV bruts semblent sous-évalués pris isolément — la pondération Mouvement=1/PV=1 n'était pas démontrée à l'origine, mais elle produit malgré tout un socle Infanterie/Cavalerie cohérent avec la durabilité réelle en jeu. Pas de correctif nécessaire sur ce point (confirmé suite à une comparaison avec les coûts réels de BattleLore Seconde Édition, voir §2bis).

> 🔗 **Voir aussi** [[Document de cadrage]] D027 — le point encore ouvert n'est donc pas le poids des termes de la formule (validés ci-dessus), mais l'échelle finale des totaux, traitée au §2bis.

---

## 2. La formule

```
Points_bruts(unité) = Mouvement + PV + (Attaque × D) + Σ Coût(règles spéciales)

D = 3 si Combat = Mêlée
D = 2 si Combat = Tir
```

Rien d'autre n'entre dans le calcul de base — la Portée (fixée à 4 pour tout le monde en V1, D020) ne varie pas encore assez d'un profil à l'autre pour justifier un terme dédié ; à réintroduire si un futur peuple a des portées différentes.

> 🎲 **Note sur [Horde] et l'Attaque de base** : pour une unité [Horde], le terme `Attaque × D` de la formule utilise l'**Attaque de base** (après effondrement), pas la valeur "à pleine force". Le bonus +1 dé est déjà facturé dans le coût forfaitaire de la règle elle-même (§3) — le compter aussi dans le terme Attaque reviendrait à le payer deux fois.

---

## 2bis. Compression de l'échelle (D027)

**Constat (2026-07-19) :** en comparant au vrai système de coûts de BattleLore Seconde Édition (jeu FFG dont BdVM/BdTdM hérite le socle), les unités standards y tiennent sur une échelle très resserrée — 4 à 6 points pour l'essentiel du roster, 8 points pour les unités "Légende" à PV doublés. Sur le roster Gondor et fiefs, `Points_bruts` s'étale au contraire sur 12 valeurs quasiment uniques pour 14 profils (14 à 26) — pas un problème de pondération (voir §1, le socle Infanterie/Cavalerie est déjà cohérent), mais un problème de granularité, contraire au principe "règles mémorisables" ([[Document de cadrage]] §3.1).

**Correctif : une étape de compression finale**, sans toucher aux poids de la formule brute :

```
Points_finaux(unité) = round(Points_bruts ÷ 3) − 1
```

Cette compression ramène le roster Gondor sur une échelle **4 à 8**, quasiment identique à celle de BattleLore V2, et regroupe les profils en une poignée de paliers mémorisables au lieu d'une valeur par unité (voir table complète au §4). Les deux dominances strictes actées en D025 restent lisibles après compression (vérifié au §4).

> 🎲 **Note de design** Le calcul de compression reste un calcul fait une fois par profil, à la rédaction du roster — pas à la volée en pleine partie (même logique de fluidité que pour le coût des règles, D026). C'est la valeur `Points_finaux` qui figure sur la fiche d'unité imprimée ; `Points_bruts` reste un calcul intermédiaire, pas une valeur de jeu.
>
> ⚠️ **Effet de bord observé sur le roster Rohan (2026-07-19)** : la largeur des paliers de compression (chaque palier couvre 3 points de `Points_bruts`) fait qu'une petite règle ajoutée à une unité peu chère (coût brut ≤ 2-3) ne change parfois pas du tout `Points_finaux` — ex. [Mobilité 2] sur l'Éored d'éclaireur ou [Mobilité 1] sur les Archers liges, ajoutées « gratuitement » en points. Pas anormal en soi, mais à garder en tête : le système de points est peu sensible aux petits ajustements de règles sur les profils bon marché.
>
> ⚠️ **Même effet observé sur l'Aurige de Khand (2026-07-19)** : réduire les PV de 4 à 3 (bruts −1) et ajouter [Poursuite 1] (bruts +3) donne un solde net de +2 bruts (23 → 25), mais `Points_finaux` reste à **7** dans les deux cas (`round(23÷3)−1 = round(25÷3)−1 = 7`) — l'arrondi absorbe l'ajustement. Voir `02 - Factions/Khand.md` §2, profil 5, pour le détail.

---

## 3. Coût des règles spéciales — deux options

### Option A — Coût forfaitaire unique (la plus simple)

Chaque règle spéciale, quelle qu'elle soit, coûte **2 points** ; une règle avec valeur X coûte **2 × X**.

Avantages : aucune table à consulter, cohérent avec le principe 1 du [[Document de cadrage]] (mémorisable). Inconvénient : ne distingue pas une règle à fort impact ([Poursuite X], quasi une attaque supplémentaire) d'une règle très situationnelle ([Férocité], qui ne s'active qu'en contre-attaque et seulement si l'adversaire n'est pas déjà éliminé) — au prix identique, [Poursuite X] devient systématiquement le meilleur choix, ce qui pousse toutes les armées vers les mêmes règles.

### Option B — Coût par catégorie ✅ retenue (validée par Emmanuel, 2026-07-19)

Reprend les catégories déjà utilisées dans [[Regles_Speciales]], avec un coût qui reflète l'impact typique de la catégorie :

| Règle | Coût | Catégorie |
|---|---|---|
| [Armure X] | 2 × X | Défensif |
| [Inébranlable X] | 2 × X | Défensif |
| [Protection X] | 1 × X | Défensif *(déjà porté par le terrain la plupart du temps)* |
| [Mur de bouclier] | 1 *(forfaitaire)* | Défensif *(version conditionnelle-à-la-formation de [Protection 1] — provisoire, non testée)* |
| [Immunisé au poison/feu] | 1 | Défensif *(rare, situationnel)* |
| [Arme Lourde X] | 2 × X | Offensif — Mêlée |
| [Perforant X] | 2 × X | Offensif — Distance |
| [Réception de charge] | 2 | Offensif — Mêlée |
| [Férocité] | 1 | Offensif — Mêlée *(situationnel : seulement en contre-attaque)* |
| [Charge écrasante] | 2 | Offensif — Mêlée |
| [Archer en mêlée] | 2 | Offensif — Mêlée |
| [Martyre] | 1 | Offensif — Mêlée |
| [Double Tir] | 3 | Offensif — Distance *(quasi une attaque complète en plus)* |
| [Howdah] | 3 | Offensif — Distance |
| [Poison] / [Souffle de feu] | 1 | Offensif — Distance |
| [Mobilité X] | 1 × X | Manœuvre |
| [Poursuite X] | 3 × X | Manœuvre *(mouvement + attaque supplémentaire)* |
| [Déploiement avancé] | 2 *(forfaitaire)* | Manœuvre *(repositionnement unique avant le tour 1, indépendant de la valeur de Mouvement — provisoire, non testé)* |
| [Terrain favori : X] | 1 | Manœuvre |
| [Rechargement] | −2 | Manœuvre *(malus — restreint l'unité)* |
| [Bête incontrôlable] | −1 | Manœuvre *(malus — risque propre au Mûmakil)* |
| [Meute X] | +1 par PV supplémentaire accordé | Manœuvre |
| [Horde] | 3 *(forfaitaire)* | Mixte — Offensif + Défensif *(+1 dé d'attaque et [Inébranlable 1] tant qu'aucun PV n'a été perdu ; provisoire, non testé)* |
| [Peur X] | 2 × X | Moral *(provisoire, non testé — voir note ci-dessous)* |

> 🎲 **Note de design** L'écart entre [Férocité] (1 point) et [Poursuite X] (3×X points) n'est pas arbitraire : les deux appartiennent à la même catégorie "Offensif — Mêlée / Manœuvre" mais [Férocité] ne s'active que dans une fenêtre étroite (contre-attaque, adversaire pas encore éliminé), alors que [Poursuite X] offre une action quasi-garantie chaque fois que l'unité charge. Un coût forfaitaire unique gommerait cet écart et pousserait toutes les listes vers les mêmes règles — c'est l'argument principal en faveur de l'Option B.
>
> ⚠️ **[Déploiement avancé] — coût provisoire (2026-07-19)** : première règle entièrement nouvelle depuis la validation du barème (créée pour l'Éored d'éclaireur, Rohan). Fixée à 2 points forfaitaires par analogie avec les autres règles de manœuvre à effet ponctuel ([Terrain favori] = 1, [Réception de charge] = 2), sans référence testée puisqu'aucune règle de « repositionnement pré-bataille » n'existait avant. À revoir après un premier usage à la table (voir `02 - Factions/Rohan.md` §5.5).
>
> ⚠️ **[Horde] — coût provisoire (2026-07-19, D032)** : première règle à cumuler un effet offensif et un effet défensif sous une seule condition (« indemne »), en dehors des catégories existantes. Par décomposition : le +1 dé s'apparente à [Réception de charge] (2 pts, bonus de dé conditionnel) et [Inébranlable 1] vaut 2 pts en continu dans la table Défensif — la somme brute des deux donnerait 4, mais ici les deux bonus s'éteignent **définitivement** à la toute première perte, une fenêtre plus courte que toute autre règle situationnelle du glossaire. Fixé à **3 points forfaitaires** (arbitrage d'Emmanuel entre 2/3/4 proposés) plutôt que la somme brute des composants. **Première assignation — 2026-07-20** : Bande d'orques du Mordor et Bande d'orques du Morannon (`02 - Factions/Mordor.md`). Toujours non testé en partie réelle — à revoir après le Playtest #1.
>
> ⚠️ **[Peur X] — coût provisoire (2026-07-20, D033)** : fixé à 2×X par analogie avec les autres règles offensives à valeur ([Armure X], [Arme Lourde X], [Perforant X]) — la face Arcane a la même probabilité qu'une autre face (1/6). Attention toutefois : [Peur X] génère des **Drapeaux, pas des touches** — l'effet fait reculer mais ne tue pas, et peut être annulé par [Inébranlable X] de la cible. Il se peut que **1×X** soit plus juste après un premier test. Première (et seule) assignation à ce jour : Troll du Mordor ([Peur 1], `02 - Factions/Mordor.md`). À caler au Playtest #1.
>
> ⚠️ **[Mur de bouclier] — coût provisoire (2026-07-20, D037)** : fixé à 1 point forfaitaire, aligné sur le tarif de [Protection 1] dans la table. Point de vigilance : en formation de ligne classique (le cas d'usage normal pour une Infanterie disciplinée), la condition d'adjacence sera presque toujours vraie — ce qui pourrait sous-évaluer la règle par rapport à un [Armure 1] permanent (2 pts, toujours actif). Première assignation : Cohorte d'orientaux et Cohorte de piquiers orientaux (`02 - Factions/Easterling.md`). À surveiller au Playtest #1.

**Décision (D026) :** Option B retenue. Le calcul reste simple à faire une fois par profil (pas à la volée en pleine partie, donc moins contraint par le principe de fluidité que les règles de jeu elles-mêmes) et évite qu'une poignée de règles dominent systématiquement les choix de liste.

---

## 4. Test sur le roster Gondor et fiefs (coûts calculés avec l'Option B, compression D027)

| # | Unité | Mvt | PV | Atk×D | Règles | Brut | **Final** |
|---|---|---|---|---|---|---|---|
| 1 | Guerriers de Minas Tirith | 2 | 6 | 3×3=9 | Armure1 (2) | 19 | **5** |
| 2 | Archers de Minas Tirith | 2 | 6 | 2×2=4 | Armure1 (2) | 14 | **4** |
| 3 | Chevaliers de Minas Tirith | 3 | 3 | 3×3=9 | Armure1 (2) | 20 | **6** |
| 4 | Rangers du Gondor | 2 | 6 | 2×2=4 | Double Tir (3) | 15 | **4** |
| 5 | Gardes de la Citadelle | 2 | 6 | 3×3=9 | Armure1 (2) + Inébranlable1 (2) | 21 | **6** |
| 6 | Hommes d'armes de Dol Amroth | 2 | 6 | 3×3=9 | Armure1 (2) + Réception de charge (2) | 21 | **6** |
| 7 | Chevaliers à pied de Dol Amroth | **1** | 6 | 4×3=12 | Armure1 (2) | 21 | **6** |
| 8 | Chevaliers de Dol Amroth | 3 | 3 | 4×3=12 | Armure1 (2) + Poursuite1 (3) | 23 | **7** |
| 9 | Guerriers de Lossarnach | 2 | 6 | 3×3=9 | Armure1 (2) + Arme Lourde1 (2) | 21 | **6** |
| 10 | Guerriers des clans de Lamedon | 2 | 6 | 3×3=9 | Arme Lourde1 (2) | 19 | **5** |
| 11 | Rangers d'Ithilien 🌟 | 2 | 6 | 3×2=6 | Mobilité1 (1) + Double Tir (3) | 18 | **5** |
| 12 | Vétérans d'Osgiliath 🌟 | 2 | 6 | 3×3=9 | Armure1 (2) + Inébranlable1 (2) + Férocité (1) | 22 | **6** |
| 13 | La Compagnie Grise 🌟 | 2 | 6 | 3×3=9 | *(voir §5 — cas particulier)* | 26* | **8*** |
| 14 | Archers de la Racine Noire 🌟 | 2 | 6 | 3×2=6 | Perforant1 (2) + Mobilité1 (1) + Double Tir (3) | 20 | **6** |

*(Colonne « Brut » = `Points_bruts` du §2 ; colonne « Final » = `round(Brut ÷ 3) − 1` du §2bis, D027. C'est la valeur « Final » qui figure sur la fiche imprimée.)*

**Validation directe de D025 (sur la valeur finale, après compression) :**
- Chevaliers de Dol Amroth (**7**) coûtent **1 point de plus** que Chevaliers de Minas Tirith (**6**) — écart conservé après compression.
- Archers de la Racine Noire (**6**) coûtent **1 point de plus** que Rangers d'Ithilien (**5**) — écart conservé également.

Les deux dominances strictes actées "à assumer" en D025 restent donc lisibles après compression, sans avoir eu besoin de retoucher un seul profil.

**Fourchette obtenue :** 4 à 7 points pour les profils "normaux", 8 pour la Compagnie Grise — échelle quasiment identique à celle de BattleLore V2 (4 à 8, voir §2bis). Une armée Normal tournerait autour de 25-40 points par camp selon ce calibrage (à l'aune d'un roster de 6-8 unités) — chiffre à confirmer par le Playtest #3, pas encore validé par le jeu réel.

**Second point de calibrage — roster Rohan (validé) :** le trio équivalent au Playtest #1 de Gondor (Guerriers/Archers/Chevaliers de Minas Tirith, 15 points) donne, côté Rohan, Éored de cavalier + Milice lige + Archers liges = **13 points** — cohérent avec l'identité « moins armuré, plus mobile » actée pour ce peuple (voir `02 - Factions/Rohan.md` §4). Détail complet des 9 profils Rohan dans ce document.

**Troisième point de calibrage — roster Khand (validé et clos) :** 5 profils, de 3 à 7 points — Mercenaires de Khand (hache/archer) : 5/3 ; Pillards de Khand (hache/archer) : 5/3 ; Aurige de Khand (pièce signature, 3 règles, PV ramené à 3) : 7. Échelle cohérente avec Gondor (4-8) et Rohan (3-8), sans avoir eu besoin d'ajuster la formule. Détail complet dans `02 - Factions/Khand.md`.

**Quatrième point de calibrage — roster Mordor (validé et clos) :** 6 profils, de 3 à 7 points — Bande d'orques (5, [Horde]) et Bande d'orques du Morannon (6, Armure1 + [Horde]) donnent le premier test en conditions réelles du coût forfaitaire de [Horde] (D032) ; le Troll (7, Charge écrasante + [Peur 1]) fait de même pour [Peur X] (D033). Détail complet dans `02 - Factions/Mordor.md`.

**Cinquième point de calibrage — roster Easterling (validé et clos) :** 4 profils, de 4 à 7 points — Cohorte d'orientaux (5, [Mur de bouclier]) et Cohorte de piquiers (6, Réception de charge + [Mur de bouclier]) donnent le premier test en conditions réelles du coût forfaitaire de [Mur de bouclier] (D037) ; Cataphractaires (7, [Armure 2] + Charge écrasante) est la première unité du jeu à porter une armure doublée. Roster délibérément haut de gamme (trio de base à 16 pts, contre 15 pour Gondor) — cohérent avec l'identité « armée de métier » actée pour ce peuple. Détail complet dans `02 - Factions/Easterling.md`.

---

## 5. Cas particulier — unités composites à figurines nommées (La Compagnie Grise)

La Compagnie Grise ne porte pas des règles fixes : Gimli, Legolas, Elrohir+Elladan et Halbarad n'apportent leur règle que tant qu'ils sont en vie, et l'unité s'affaiblit au fil de la partie. Deux façons de la chiffrer :

**Décision (D026) : pleine puissance, 26 points bruts → 8 points finaux.** On compte toutes les règles comme actives, comme si les 6 figurines étaient en vie — Mvt2 + PV6 + Atk3×3=9 + ArmeLourde1(2) + ArcherEnMêlée(2) + Férocité(1) + Inébranlable2(4) = **26 points bruts**, soit `round(26÷3)−1 = 9−1 = 8` points finaux (D027) — exactement l'échelon "Légende" repéré dans BattleLore V2 (voir §2bis), cohérent avec le statut d'unité sur-mesure de la Compagnie Grise. Cohérent avec le fait qu'aucune unité du jeu ne voit son coût recalculé en cours de partie à mesure qu'elle prend des pertes — une unité à 1 PV restant vaut déjà objectivement moins qu'à pleine forme sans qu'on retouche son prix. L'alternative (valeur moyenne pondérée selon l'ordre de retrait probable) a été écartée : trop de calcul pour un cas unique, contraire au principe de simplicité du [[Document de cadrage]] §3.1.

> ⚠️ **Point ouvert pour vous, Emmanuel** — la Compagnie Grise sera-t-elle la seule unité de ce type dans le roster complet (6 peuples), ou d'autres composites nommés sont-ils prévus ? Ni le roster Rohan, ni le roster Khand, ni l'ébauche actuelle du roster Mordor n'en comportent — la question reste ouverte pour Harad et Easterling.

---

## 6. Décisions actées et points encore ouverts

**Actés avec Emmanuel — voir D026 du [[Document de cadrage]] :**
- Coût des règles spéciales par catégorie (Option B), pas de coût forfaitaire unique.
- Pas de prime de sécurité pour le Tir en V1 — le ratio 3 pts/dé (Mêlée) contre 2 pts/dé (Tir) suffit pour l'instant. À revoir si le Playtest #3 montre que le Tir domine trop facilement.
- La Compagnie Grise (et tout futur composite à figurines nommées) se chiffre en pleine puissance, pas en valeur moyenne pondérée.

**Actés avec Emmanuel — voir D027 du [[Document de cadrage]] :**
- Le socle Mouvement/PV de la formule brute est validé tel quel — comparaison à la durabilité effective en Mêlée : ratio Infanterie/Cavalerie 8:6 (socle) = 12:9 (durabilité), les deux à 1,33:1 (voir §1). Pas de retouche des poids.
- Comparaison aux coûts réels de BattleLore V2 (échelle 4-8 pour l'essentiel du roster) → ajout d'une étape de compression finale `round(Points_bruts ÷ 3) − 1` (§2bis), qui ramène le roster Gondor sur la même échelle (4 à 8) tout en conservant les deux dominances D025.

**Actés — voir D032 du [[Document de cadrage]] :**
- [Horde] chiffrée à 3 points forfaitaires (arbitrage entre 2/3/4). Première assignation réelle : roster Mordor (2026-07-20).

**Nouveau — voir D033 du [[Document de cadrage]] (2026-07-20) :**
- Nouvelle règle [Peur X] créée pour le Troll du Mordor, coût provisoire 2×X (catégorie Moral) — non testé, à revoir après un premier usage à la table. Possible correction vers 1×X si le Playtest #1 montre le coût trop élevé pour un effet qui ne fait que reculer (pas de touche).

**Nouveau — voir D037 du [[Document de cadrage]] (2026-07-20) :**
- Nouvelle règle [Mur de bouclier] créée pour la Cohorte d'orientaux et la Cohorte de piquiers orientaux (Easterling), coût provisoire 1 pt forfaitaire (catégorie Défensif) — non testé. Risque identifié : sous-évaluation possible si la condition d'adjacence est quasi toujours vraie en formation de ligne (voir note ci-dessus).

**Encore ouvert :**
1. **Généralisation des unités composites** — aucune unité composite de type Compagnie Grise dans les rosters Rohan, Khand, Mordor ou Easterling. Reste à surveiller pour Harad, le dernier peuple non rédigé.
2. **Coût de [Déploiement avancé]** — provisoire, jamais testé en partie réelle (D028).
3. **Coût de [Horde]** — provisoire, première assignation réelle mais pas encore jouée (D032).
4. **Coût de [Peur X]** — provisoire, non testé (D033).
5. **Coût de [Mur de bouclier]** — provisoire, non testé, risque de sous-évaluation identifié (D037).
6. **Compromis PV/règle de l'Aurige de Khand** (PV 3 + [Poursuite 1]) — chiffré mais jamais testé en partie réelle, à surveiller en priorité au Playtest #1.

---

## 7. Prochaine étape

Les rosters Gondor, Rohan, Khand, Mordor et Easterling étant tous rédigés et validés, ce système a servi de cinq points de calibrage cohérents — voir §4. Reste à l'appliquer à Harad, dernier peuple de la V1, et à valider l'ensemble (notamment [Horde], [Peur X] et [Mur de bouclier], jamais testés en partie réelle) au Playtest #1 puis au Playtest #3 (scénario Pelennor complet).

---

*Version : 0.7 — Phase 1 (contenu Phase 3 anticipé) — 2026-07-20. Ajout de la ligne de coût [Mur de bouclier] (1 pt forfaitaire, provisoire, D037) et de sa note associée. Cinquième point de calibrage du système de points effectué sur le roster Easterling, validé et clos dès sa première session (`02 - Factions/Easterling.md`, D038).*
