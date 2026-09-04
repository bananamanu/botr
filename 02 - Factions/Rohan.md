---
projet: "Batailles de la Terre du Milieu"
type: "faction"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-08-30"
tags: [BdTdM, "type/faction", "peuple/rohan", "statut/brouillon"]
version: "2.8"
---

# Rohan — Profils d'unités

> **Objet de ce document (P8 — simplification radicale, D101/D102, retouches D107).** Même principe qu'à Gondor : une unité de base ne porte **plus aucun badge d'office**. Profil = Type + Combat + Classe. Seules options possibles : **Faction** ([Férocité], toujours disponible en tant qu'outil, jamais un supplément systématique) et **Bannière**, marquées ligne par ligne. Pas de fusion de familles nécessaire ici (arbitrage Emmanuel) — les 9 lignes historiques restent distinctes, différenciées par leur classe.
>
> **La Garde du Roi (8, 9) devient une pièce entièrement signature (D107)** : elle abandonne Faction et se définit désormais par **Légende** (+1 dé) + **[Inébranlable ∞]** — elle ne recule jamais, donc [Férocité] (contre-attaquer malgré un recul) n'a plus de sens et disparaît.
>
> Aligné sur [[Regles_Base]] v0.17, [[Regles_Speciales]] v0.31, [[Regles_Points]] v0.30.

---

## 1. Faction du Rohan — [Férocité]

Contre-attaque même repoussé. **Outil optionnel**, +1 brut, disponible sur les unités marquées éligibles ci-dessous — jamais automatique.

**Bannière** : [Inébranlable 1], +2 brut, figurine porte-étendard — disponible sur les formations réglées, **y compris désormais la Milice lige** (D107 : une milice peut très bien se rallier à un étendard local).

---

## 2. Liste des troupes (coûts de base — sans option)

| # | Unité | Type | Combat | Classe | Options disponibles | **Points** |
|---|---|---|---|---|---|---|
| 1 | Éored de cavalier du Rohan | Cavalerie | Mêlée | 🔵 | Faction, Bannière | **6** |
| 2 | Milice lige | Infanterie | Mêlée | 🟢 | Faction, **Bannière** | **3** |
| 3 | Archers liges | Infanterie | Distance | 🟢 | Faction | **3** |
| 4 | Éored d'éclaireur | Cavalerie | Distance | 🔵 | Faction | **3** |

> 🎲 **Case comblée (D124).** Éored d'éclaireur **+ Faction [Férocité]** : brut 13 + 1 = 14 → `round(14÷3)−1` = **4**. C'est la seule unité du Rohan où la Faction n'est **pas** absorbée par la compression — sur l'Éored de cavalier (22 → 6) et les Gardes royaux à cheval (24 → 7), elle reste gratuite.
| 5 | Gardes royaux à cheval | Cavalerie | Mêlée | 🔴 | Faction, Bannière | **7** |
| 6 | Gardes Royaux du Rohan | Infanterie | Mêlée | 🔴 | Faction, Bannière | **5** |
| 7 | Helmingas de Grimbolg | Infanterie | Mêlée | 🔵 | Faction, Bannière | **4** |
| 8 | Garde du Roi *(à pied)* — *signature* | Infanterie | Mêlée | 🔴 | *(hors matrice, voir §3)* | **8** |
| 9 | Garde du Roi *(à cheval)* — *signature* | Cavalerie | Mêlée | 🔴 | *(hors matrice, voir §3)* | **10** |

**Coûts avec options :**

| # | Unité | Base | +Faction | +Bannière |
|---|---|---|---|---|
| 1 | Éored de cavalier | 6 | 6 *(absorbé)* | **7** |
| 2 | Milice lige | 3 | 3 *(absorbé)* | 3 *(absorbé)* |
| 5 | Gardes royaux à cheval | 7 | 7 *(absorbé)* | 7 *(absorbé)* |
| 6 | Gardes Royaux du Rohan | 5 | **6** | **6** |
| 7 | Helmingas de Grimbolg | 4 | **5** | **5** |

> 🔄 **Baisses par rapport à l'ancien roster (P7c) :** 5, 6, 7 perdent leur badge Élite/Spéciale par défaut — Gardes royaux du Rohan 6→**5**, Helmingas 5→**4** ; Gardes royaux à cheval reste **7** (absorbé par la compression). Ces règles (Inébranlable, Relance) ne sont plus disponibles comme options génériques du roster — le menu se réduit à Faction/Bannière, cohérent avec la simplification radicale.

---

## 3. Garde du Roi — pièce entièrement signature (D107)

Infanterie ou Cavalerie (au choix, jamais les deux simultanément), Mêlée, 🔴.

**Règles :** **Légende** (+1 dé) + **[Inébranlable ∞]** (ne recule jamais, quel que soit le nombre de Drapeaux subis).

> 🎲 **Pourquoi plus de Férocité ?** [Férocité] permet de contre-attaquer *malgré* un recul forcé. Une unité qui ne recule **jamais** n'a strictement rien à gagner de cette règle — elle contre-attaque de toute façon, dans tous les cas. La retirer est une simplification pure, pas une perte de puissance.

**Chiffrage (D107, [Inébranlable ∞] au tarif bespoke établi par le Mûmakil — voir [[Regles_Points]] §3.4) :**

- À pied : brut = 19 (Inf🔴 mêlée) + 3 (Légende mêlée) + 6 (Inébranlable ∞) = 28 → round(28÷3)−1 = **8**.
- À cheval : brut = 23 (Cav🔴 mêlée) + 3 (Légende) + 6 (Inébranlable ∞) = 32 → round(32÷3)−1 = **10**.

*(Hausse par rapport à l'ancienne version avec Férocité en dur — 7→**8** et 8→**10** — cohérente avec la puissance réelle d'une unité totalement increvable au recul.)*

---

## 4. Variantes avec Leader — Playtest #4 (Pelennor)

| Unité porteuse | Leader | Général | Destin | Options prises | **Points** |
|---|---|---|---|---|---|
| Éored de cavalier | **Éomer** | Oui | 3 | Faction | **13** *(brut 21+1+4+9+6=41)* |
| Gardes royaux à cheval | **Théoden** | Oui | 1 | Faction | **12** *(brut 23+1+4+9+2=39)* |

Bannière portée au Playtest #4 par 2 éoreds (+1 → **7** chacun) et 1 garde royal à cheval (base 7, absorbé, reste **7**).

---

## 5. Récapitulatif

| Option | Disponible sur |
|---|---|
| **Faction [Férocité]** | 1-7 (optionnelle) |
| **Bannière** | 1, 2, 5, 6, 7 |
| **Hors matrice, signature** | Garde du Roi (8, 9) — Légende + [Inébranlable ∞] |
| **Leader/Général/Destin** | Éomer (Éored), Théoden (Gardes royaux à cheval) au Pelennor |

---

## 6. Points ouverts transverses

- **Menu réduit à Faction/Bannière seulement** — les anciennes règles socle (Relance 1, Inébranlable+JF) disparaissent des options standard, ne survivent que dans les pièces signature (Garde du Roi, Compagnie Grise, futures pièces bespoke).
- **Garde du Roi à 8/10 pts** — hausse sensible par rapport à l'ancienne version (7/8), à surveiller au prochain playtest : une pièce increvable au recul, avec 5 dés (Légende), à ce tarif, doit rester utilisable dans un format 3v3 sans écraser la ligne.

---

*Version : 2.8 — Phase 1 — 2026-08-30. **D124 — case de coût comblée.** Éored d'éclaireur + Faction [Férocité] chiffré à **4** (brut 14) : seule unité du roster où la Faction n'est pas absorbée par la compression. La case manquait à la table des options et faussait le chiffrage du scénario du Pelennor. Aucun autre coût touché.*

*Version : 2.7 — Phase 1 — 2026-08-23. **Retouches Emmanuel (D107).** Bannière ajoutée en option sur la Milice lige (2). Garde du Roi (8, 9) devient une pièce **entièrement signature**, hors matrice : Légende + [Inébranlable ∞], Férocité retirée (une unité qui ne recule jamais n'a rien à gagner de la contre-attaque-malgré-recul). Nouveaux coûts : à pied 7→**8**, à cheval 8→**10** (tarif [Inébranlable ∞] repris du Mûmakil, +6 brut bespoke).*

*Version : 2.6 — Phase 1 — 2026-08-23. **Simplification radicale généralisée (D101).** Plus aucun badge par défaut : Faction et Bannière deviennent les deux seules options, marquées ligne par ligne, jamais automatiques — y compris sur les unités auparavant Élite/Spéciale (5, 6, 7), dont le coût de base baisse en conséquence (6→5, 5→4). Garde du Roi (8, 9) conservée en exception (Légende + Férocité en dur, signature). Variantes Leader recalculées sur les nouvelles bases : Éored+Éomer **13**, Gardes royaux+Théoden **12**.*

*Version : 2.5 — Phase 1 — 2026-08-23. **P8 — recalcul complet (D097/D098).** Faction ciblée : retirée par défaut (1-4), conservée en dur sur la Garde du Roi (8, 9), réapparaît sur toute unité avec Leader. Anciens badges Spéciale/Élite renommés « règles socle », coûts inchangés. Éored d'éclaireur 4→**3** pts (seul changement de coût de base). Nouvelles variantes chiffrées : Éored avec Éomer (Général, Destin 3) = **13** pts ; Gardes royaux à cheval avec Théoden (Général, Destin 1) = **12** pts ; variantes Bannière ajoutées. §4 (nouveau) récapitule les variantes Leader du Playtest #4.*

*Version : 2.4 — Phase 1 — 2026-08-18. **Retrait du trait de Faction (D089/D090).** [Férocité] n'est plus imprimé pour tout le roster ; asymétrie reportée sur les cartes de commandement (P8). Lignes « Badges » nettoyées. §1 et §4 réécrits. Ajout du badge **Leader** (slot réservé, Phase 2). Coûts inchangés en attendant P8.*

*Version : 2.3 — Phase 1 — 2026-08-16. **Corrections de relecture — revue de finalisation « Verrouillage v1.0 ».** En-tête « Aligné sur » rafraîchi (v0.12/v0.22/v0.19 → v0.13/v0.27/v0.24, versions réelles depuis P7c). Aucune décision mécanique — pas de numéro D.*

*Version : 2.2 — Phase 1 — 2026-08-13. **Collapse du système de badges (D080/D081, tâche P7c).** Faction déjà universelle depuis D074 : rien à changer à ce niveau. Plafond à 1 badge secondaire : Garde du Roi (8, 9), seul profil du roster à cumuler Élite+Légende, ne garde que **Légende**. À pied : coût inchangé (7, absorbé par la compression). À cheval : 9→**8 pts**. Récapitulatif (§4) et points ouverts (§5) mis à jour.*

*Version : 2.1 — Phase 1 — 2026-08-08. **Migration « badges universels » (D074).** Badge Faction remplacé par **[Férocité]**, désormais porté par **tout le roster sans exception** (Archers liges inclus, coût inchangé) — abandon de [Arme de jet 1]. Badge Spéciale migré vers **[Relance 1]** (universel D073), ne reste porté que par Helmingas de Grimbolg (qui échange son Élite contre ce badge, coût inchangé à 5 pts). Gardes royaux (à cheval et à pied) **reclassés en 🔴** et perdent leur badge Spéciale — l'armure vient désormais de la classe (8 et 6 pts). Garde du Roi (les deux versions) perd Spéciale et l'ancienne signature bespoke [Férocité], gagne le badge **Légende** (+1 dé de combat, +2 pts chaque version : 6→7 à pied, 8→9 à cheval) — devient la pièce la plus chère du projet. Non testé — validation P7a.*

*Version : 2.0 — Phase 1 — 2026-08-08. **Refonte P4 (D069) : re-expression complète sur la taxonomie visuelle et le système de badges, miroir de Gondor.** Roster resserré à 9 profils (Garde du Roi formalisée en pièce unique à deux incarnations plutôt que deux unités séparées). Deux badges fixes (Faction=[Arme de jet 1], Spéciale=[Armure 1]) + Élite, inversés par rapport à Gondor pour refléter l'armure rare du Rohan. [Arme de jet X] restaurée au socle générique (coupée à P2, faute de porteur en attente). [Prise de flanc]/[Vigilant] abandonnées. [Férocité] ajoutée comme signature de la Garde du Roi (les deux versions), résout la collision de coût avec Gardes royaux à cheval et restaure l'ancien coût (8 pts). Non testé — validation P7a.*
