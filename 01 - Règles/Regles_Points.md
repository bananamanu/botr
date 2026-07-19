---
projet: "Batailles de la Terre du Milieu"
type: "regles"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-07-19"
tags: [BdTdM, "type/regles", "phase/1", "statut/brouillon", "construction-armee"]
version: "0.3"
---

# Batailles de la Terre du Milieu — Système de points

> **Objet de ce document :** Première proposition de formule de coût en points pour la construction d'armée (feuille de route Phase 3, [[Document de cadrage]] §6). Répond directement à D025 : les dominances strictes assumées en V1 (Chevaliers de Dol Amroth sur Chevaliers de Minas Tirith ; Archers de la Racine Noire sur Rangers d'Ithilien) doivent se refléter dans un écart de coût plutôt que dans une retouche de profil.
>
> Calibrée et testée sur les 14 profils déjà rédigés de [[Gondor_et_Fiefs]] — c'est la seule donnée réelle disponible à ce stade. À revalider dès que Rohan (et les autres peuples) seront rédigés, et impérativement au Playtest #3 (scénario Pelennor complet, premier test en conditions réelles de construction d'armée).

---

## 1. Pourquoi cette forme de formule

Trois remarques structurantes avant la formule elle-même :

**Le Mouvement et les PV ne varient quasiment pas entre profils d'un même Type.** Le [[Document de cadrage]] fixe PV et Mouvement par Type (Infanterie : 6 PV / Mvt 2 ; Cavalerie : 3 PV / Mvt 3), sans exception dans le roster Gondor hormis Mouvement 1 pour les Chevaliers à pied de Dol Amroth. Concrètement, ces deux stats ne différencient presque jamais deux profils entre eux — ce qui varie vraiment, c'est l'**Attaque** (2 à 4 dés) et les **règles spéciales**. La formule ci-dessous en tient compte : Mouvement et PV forment un "socle" quasi fixe par Type, l'Attaque et les règles font tout le travail de différenciation.

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

---

## 2bis. Compression de l'échelle (D027)

**Constat (2026-07-19) :** en comparant au vrai système de coûts de BattleLore Seconde Édition (jeu FFG dont BdVM/BdTdM hérite le socle), les unités standards y tiennent sur une échelle très resserrée — 4 à 6 points pour l'essentiel du roster, 8 points pour les unités "Légende" à PV doublés. Sur le roster Gondor et fiefs, `Points_bruts` s'étale au contraire sur 12 valeurs quasiment uniques pour 14 profils (14 à 26) — pas un problème de pondération (voir §1, le socle Infanterie/Cavalerie est déjà cohérent), mais un problème de granularité, contraire au principe "règles mémorisables" ([[Document de cadrage]] §3.1).

**Correctif : une étape de compression finale**, sans toucher aux poids de la formule brute :

```
Points_finaux(unité) = round(Points_bruts ÷ 3) − 1
```

Cette compression ramène le roster Gondor sur une échelle **4 à 8**, quasiment identique à celle de BattleLore V2, et regroupe les profils en une poignée de paliers mémorisables au lieu d'une valeur par unité (voir table complète au §4). Les deux dominances strictes actées en D025 restent lisibles après compression (vérifié au §4).

> 🎲 **Note de design** Le calcul de compression reste un calcul fait une fois par profil, à la rédaction du roster — pas à la volée en pleine partie (même logique de fluidité que pour le coût des règles, D026). C'est la valeur `Points_finaux` qui figure sur la fiche d'unité imprimée ; `Points_bruts` reste un calcul intermédiaire, pas une valeur de jeu.

---

## 3. Coût des règles spéciales — deux options

### Option A — Coût forfaitaire unique (la plus simple)

Chaque règle spéciale, quelle qu'elle soit, coûte **2 points** ; une règle avec valeur X coûte **2 × X**.

Avantages : aucune table à consulter, cohérent avec le principe 1 du [[Document de cadrage]] (mémorisable). Inconvénient : ne distingue pas une règle à fort impact ([Poursuite X], quasi une attaque supplémentaire) d'une règle très situationnelle ([Férocité], qui ne s'active qu'en contre-attaque et seulement si l'adversaire n'est pas déjà éliminé) — au prix identique, [Poursuite X] devient systématiquement le meilleur choix, ce qui pousse toutes les armées vers les mêmes règles.

### Option B — Coût par catégorie ✅ retenue (validée par Emmanuel, 2026-07-19)

Reprend les 4 catégories déjà utilisées dans [[Regles_Speciales]], avec un coût qui reflète l'impact typique de la catégorie :

| Règle | Coût | Catégorie |
|---|---|---|
| [Armure X] | 2 × X | Défensif |
| [Inébranlable X] | 2 × X | Défensif |
| [Protection X] | 1 × X | Défensif *(déjà porté par le terrain la plupart du temps)* |
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
| [Terrain favori : X] | 1 | Manœuvre |
| [Rechargement] | −2 | Manœuvre *(malus — restreint l'unité)* |
| [Bête incontrôlable] | −1 | Manœuvre *(malus — risque propre au Mûmakil)* |
| [Meute X] | +1 par PV supplémentaire accordé | Manœuvre |

> 🎲 **Note de design** L'écart entre [Férocité] (1 point) et [Poursuite X] (3×X points) n'est pas arbitraire : les deux appartiennent à la même catégorie "Offensif — Mêlée / Manœuvre" mais [Férocité] ne s'active que dans une fenêtre étroite (contre-attaque, adversaire pas encore éliminé), alors que [Poursuite X] offre une action quasi-garantie chaque fois que l'unité charge. Un coût forfaitaire unique gommerait cet écart et pousserait toutes les listes vers les mêmes règles — c'est l'argument principal en faveur de l'Option B.

**Décision (D026) :** Option B retenue. Le calcul reste simple à faire une fois par profil (pas à la volée en pleine partie, donc moins contraint par le principe de fluidité que les règles de jeu elles-mêmes) et évite qu'une poignée de règles dominent systématiquement les choix de liste.

---

## 4. Test sur le roster Gondor et fiefs (coûts calculés avec l'Option B, compression D027)

| # | Unité | Mvt | PV | Atk×D | Règles | Brut | **Final** |
|---|---|---|---|---|---|---|---|
| 1 | Guerriers de Minas Tirith | 2 | 6 | 3×3=9 | Armure1 (2) | 19 | **5** |
| 2 | Archers de Minas Tirith | 2 | 6 | 2×2=4 | Armure1 (2) | 14 | **4** |
| 3 | Chevaliers de Minas Tirith | 3 | 3 | 3×3=9 | Armure1 (2) + Poursuite1 (3) | 20 | **6** |
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

---

## 5. Cas particulier — unités composites à figurines nommées (La Compagnie Grise)

La Compagnie Grise ne porte pas des règles fixes : Gimli, Legolas, Elrohir+Elladan et Halbarad n'apportent leur règle que tant qu'ils sont en vie, et l'unité s'affaiblit au fil de la partie. Deux façons de la chiffrer :

**Décision (D026) : pleine puissance, 26 points bruts → 8 points finaux.** On compte toutes les règles comme actives, comme si les 6 figurines étaient en vie — Mvt2 + PV6 + Atk3×3=9 + ArmeLourde1(2) + ArcherEnMêlée(2) + Férocité(1) + Inébranlable2(4) = **26 points bruts**, soit `round(26÷3)−1 = 9−1 = 8` points finaux (D027) — exactement l'échelon "Légende" repéré dans BattleLore V2 (voir §2bis), cohérent avec le statut d'unité sur-mesure de la Compagnie Grise. Cohérent avec le fait qu'aucune unité du jeu ne voit son coût recalculé en cours de partie à mesure qu'elle prend des pertes — une unité à 1 PV restant vaut déjà objectivement moins qu'à pleine forme sans qu'on retouche son prix. L'alternative (valeur moyenne pondérée selon l'ordre de retrait probable) a été écartée : trop de calcul pour un cas unique, contraire au principe de simplicité du [[Document de cadrage]] §3.1.

> ⚠️ **Point ouvert pour vous, Emmanuel** — la Compagnie Grise sera-t-elle la seule unité de ce type dans le roster complet (6 peuples), ou d'autres composites nommés sont-ils prévus (par exemple côté Rohan ou Mordor) ? Si c'est un cas unique, "pleine puissance" reste la bonne règle par défaut. Si le mécanisme doit se généraliser, on formalisera une règle de calcul standard plutôt que de la retrancher au cas par cas.

---

## 6. Décisions actées (2026-07-19) et points encore ouverts

**Actés avec Emmanuel — voir D026 du [[Document de cadrage]] :**
- Coût des règles spéciales par catégorie (Option B), pas de coût forfaitaire unique.
- Pas de prime de sécurité pour le Tir en V1 — le ratio 3 pts/dé (Mêlée) contre 2 pts/dé (Tir) suffit pour l'instant. À revoir si le Playtest #3 montre que le Tir domine trop facilement.
- La Compagnie Grise (et tout futur composite à figurines nommées) se chiffre en pleine puissance, pas en valeur moyenne pondérée.

**Actés avec Emmanuel — voir D027 du [[Document de cadrage]] (2026-07-19) :**
- Le socle Mouvement/PV de la formule brute est validé tel quel — comparaison à la durabilité effective en Mêlée : ratio Infanterie/Cavalerie 8:6 (socle) = 12:9 (durabilité), les deux à 1,33:1 (voir §1). Pas de retouche des poids.
- Comparaison aux coûts réels de BattleLore V2 (échelle 4-8 pour l'essentiel du roster) → ajout d'une étape de compression finale `round(Points_bruts ÷ 3) − 1` (§2bis), qui ramène le roster Gondor sur la même échelle (4 à 8) tout en conservant les deux dominances D025. Ceci répond et clôt le point "Arrondi" laissé ouvert en v0.2.

**Encore ouvert :**
1. **Généralisation des unités composites** — la Compagnie Grise sera-t-elle un cas unique dans le roster complet, ou d'autres peuples (Rohan, Mordor...) auront-ils des unités du même type ? Pas bloquant maintenant, à surveiller à la rédaction des prochains peuples.

---

## 7. Prochaine étape

Une fois ces points tranchés, ce système peut être appliqué au roster Rohan dès sa rédaction — ce qui permettra un second point de calibrage (peuple différent, profils différents) avant de le considérer comme stable pour les 6 peuples V1.

---

*Version : 0.3 — Phase 1 (contenu Phase 3 anticipé) — 2026-07-19. Système de points validé par Emmanuel (D026) : coût par catégorie, pas de prime Tir, composites en pleine puissance. Compression finale de l'échelle validée (D027) après comparaison aux coûts réels de BattleLore V2 : `Points_finaux = round(Points_bruts ÷ 3) − 1`, échelle 4-8. Calibré et testé sur les 14 profils de [[Gondor_et_Fiefs]]. Non testé en partie réelle — à valider au Playtest #3.*
