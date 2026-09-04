---
projet: "Batailles de la Terre du Milieu"
type: "faction"
phase: "1"
statut: "brouillon-a-tester"
date_maj: "2026-08-30"
tags: [BdTdM, "type/faction", "peuple/gondor", "statut/brouillon"]
version: "3.2"
---

# Gondor et ses fiefs — Profils d'unités

> **Objet de ce document (P8 — simplification radicale, arbitrage Emmanuel).** Retour au principe 8 (simplification radicale) poussé à son terme : une unité de base ne porte **plus aucun badge d'office**. Le profil se résume à **Type + Combat + Classe**. Deux options existent, jamais imposées : **Bannière** (là où une figurine porte-étendard a un sens narratif) et **Faction** (« Défenseur de la Terre du Milieu », désormais **[Relance 1]** plutôt que [Défense X] — un outil à disposition du concepteur de scénario pour marquer ponctuellement une troupe comme vétérante, pas un supplément systématique). Le roster se resserre en conséquence : les anciennes familles distinguées uniquement par un badge (Rangers du Gondor/Ithilien/Nord, Guerriers de Minas Tirith/Garde de la Citadelle…) fusionnent en profils uniques.
>
> La Compagnie Grise redevient une pièce **entièrement bespoke** : six figurines nommées (Aragorn, Gimli, Legolas, Elrohir, Elladan, Halbarad), chacune apportant sa propre règle tant qu'elle est présente — retour à l'esprit d'origine plutôt qu'un empilement de badges génériques.
>
> Aligné sur [[Regles_Base]] v0.17, [[Regles_Speciales]] v0.30, [[Regles_Points]] v0.29.

---

## 1. Faction de Gondor — « Défenseur de la Terre du Milieu »

> Les troupes du Gondor combattent les forces de Sauron depuis des siècles et sont aguerries. **Effet : [Relance 1].**

**Ce n'est plus un trait de peuple, ni même un trait lié à un Leader — c'est un outil disponible**, à poser sur une unité éligible (voir tableau §2) quand un scénario veut en faire une troupe vétérante. Coût : **+2 brut**, jamais gratuit (contrairement à l'ancien [Défense X], la nouvelle règle [Relance 1] n'a pas de plancher intrinsèque à absorber).

**Bannière** reste un badge optionnel indépendant : **[Inébranlable 1]**, +2 brut, incarné par une figurine porte-étendard — disponible seulement là où c'est narrativement cohérent (pas sur les troupes légères qui ne portent pas d'étendard en formation).

---

## 2. Liste des troupes

| # | Unité(s) | Type | Combat | Classe | Options disponibles | **Points (base)** |
|---|---|---|---|---|---|---|
| 1 | Rangers *(du Gondor, d'Ithilien, du Nord — même profil)* | Infanterie | Distance | 🟢 | Faction | **3** |
| 2 | Archers de Minas Tirith | Infanterie | Distance | 🟢 | Faction, Bannière | **3** |
| 3 | Troupes régulières de Minas Tirith *(Garde de la Citadelle, Guerriers de Minas Tirith)* | Infanterie | Mêlée | 🔵 | Faction, Bannière | **4** |
| 4 | Troupes des Fiefs *(Guerriers de Lossarnach, Guerriers des clans de Lamedon, **Hommes d'armes de Dol Amroth**)* | Infanterie | Mêlée | 🔵 | Faction | **4** |
| 5 | Troupes lourdes des Fiefs *(Chevaliers à pied de Dol Amroth)* | Infanterie | Mêlée | 🔴 | Bannière | **5** |
| 6 | Cavalerie du Gondor *(Chevaliers de Dol Amroth, Chevaliers de Minas Tirith)* | Cavalerie | Mêlée | 🔴 | Faction, Bannière | **7** |
| 7 | La Compagnie Grise — *signature* | Infanterie | Mêlée | 🔵 | *(hors matrice, voir §3)* | **15** |

**Coûts avec options :**

| # | Unité | Base | +Faction | +Bannière | +les deux |
|---|---|---|---|---|---|
| 1 | Rangers | 3 | 3 *(absorbé)* | — | — |
| 2 | Archers de Minas Tirith | 3 | 3 *(absorbé)* | 3 *(absorbé)* | **4** |
| 3 | Troupes régulières MT | 4 | **5** | **5** | **5** *(absorbé)* |
| 4 | Troupes des Fiefs | 4 | **5** | — | — |
| 5 | Troupes lourdes des Fiefs | 5 | — | **6** | — |
| 6 | Cavalerie du Gondor | 7 | 7 *(absorbé)* | 7 *(absorbé)* | **8** |

> 🎲 **Note sur les paliers absorbés.** Sur plusieurs cases (Rangers, Archers, Cavalerie), une seule option ne change pas le coût final — la compression `round(brut÷3)−1` l'absorbe. C'est un effet de palier assumé (déjà rencontré ailleurs dans le projet, ex. Rangers du Gondor/Mobilité) : l'option reste un vrai outil narratif et tactique (donne une vraie règle en jeu) même quand elle ne coûte rien sur cette case précise.

> ✅ **Correction (D110) : les Chevaliers à pied de Dol Amroth restent en 🔴**, pas 🔵 — erreur de Claude dans la v3.0. Conservent [Armure 1]/[Poursuite 1] intrinsèques de la classe lourde. Coût de base **5** (au lieu de 4), avec Bannière **6** (au lieu de 5).

**Roster resserré de 13 lignes à 7** (Rangers 10-12 fusionnés en 1 ; Guerriers de Minas Tirith/Garde de la Citadelle fusionnés en 1 ; Lossarnach/Lamedon fusionnés en 1 ; Chevaliers de Minas Tirith/Dol Amroth fusionnés en 1).

---

## 3. La Compagnie Grise — pièce bespoke

| Type | Combat | Classe | Mouvement | Attaque | PV | **Points** |
|---|---|---|---|---|---|---|
| Infanterie | Mêlée | 🔵 | 2 | 3 dés *(+1 avec Gimli présent)* | **6** | **15** |

**Composition :** 6 figurines nommées — Aragorn, Gimli, Legolas, Elrohir, Elladan, Halbarad. Le joueur qui contrôle l'unité choisit quelle figurine retirer à chaque perte (règle héritée, inchangée).

**Règles — chacune active tant que la figurine correspondante est présente :**

| Figurine | Règle |
|---|---|
| **Gimli** | +1 dé de combat |
| **Legolas** | [Archer en mêlée] (les faces Cible touchent aussi en mêlée) |
| **Elrohir** | [Férocité] |
| **Elladan** | [Défense 1] *(= [Armure 1], règle socle générique — pas la Faction du peuple)* |
| **Halbarad** | [Inébranlable 1] |
| **Aragorn** | Badge **Leader** — Général universel, Destin 4 (voir [[Regles_Points]] §3.3). Son Leader confère aussi [Inébranlable 1] à l'unité, qui **s'additionne** à celui de Halbarad quand les deux sont présents → **[Inébranlable 2]**. |

**Chiffrage (méthode bespoke, comme le Mûmakil D079) :**

| Élément | Brut |
|---|---|
| Socle (Mvt 2 + PV 6) | 8 |
| Attaque (3 dés mêlée, D=3) | 9 |
| Gimli (+1 dé, forfait mêlée) | 3 |
| Legolas ([Archer en mêlée]) | 2 |
| Elrohir ([Férocité]) | 1 |
| Elladan ([Défense 1]) | 2 |
| Halbarad ([Inébranlable 1]) | 2 |
| Aragorn — Leader | 4 |
| Aragorn — Général | 9 |
| Aragorn — Destin 4 | 8 |
| **Brut total** | **48** |
| **Final = round(48÷3)−1** | **15** |

*(Pour référence, sans le statut Général/Destin d'Aragorn — Leader seul : brut 31 → **9** pts. La quasi-totalité de l'écart avec la version complète vient du forfait Général, cohérent avec D097.)*

**Note narrative :** six figures exceptionnelles réunies pour l'assaut final — chacune reconnaissable par sa règle propre plutôt que par un empilement de badges génériques, cohérent avec ce que la pièce a toujours représenté dans le projet.

---

## 4. Récapitulatif

| Option | Disponible sur |
|---|---|
| **Faction (Relance 1)** | Rangers (1) · Archers de Minas Tirith (2) · Troupes régulières MT (3) · Troupes des Fiefs (4) · Cavalerie du Gondor (6) |
| **Bannière** | Archers de Minas Tirith (2) · Troupes régulières MT (3) · Troupes lourdes des Fiefs (5) · Cavalerie du Gondor (6) |
| **Hors matrice** | La Compagnie Grise (7) |

---

## 5. Points ouverts transverses

- **Rangers, un seul profil pour trois anciennes identités** (Gondor/Ithilien/Nord) — si Emmanuel veut préserver une distinction narrative à la table (ex. « ces Rangers sont d'Ithilien »), c'est désormais purement cosmétique (même profil, même coût), l'option Faction pouvant marquer ponctuellement les plus aguerris pour un scénario donné.
- **Compagnie Grise, seule pièce à conserver des règles nommées par figurine** — cohérent avec le statut Signature, mais à re-vérifier si Emmanuel veut appliquer ce même traitement (règles par figure plutôt que badges génériques) à d'autres pièces uniques du projet (Mûmakil, futur Roi-Sorcier).
- **Options « absorbées » par la compression** (Rangers+Faction, Archers+Faction seule, Cavalerie+Faction seule) — à surveiller : est-ce acceptable qu'un outil narratif ne change parfois rien au prix, ou faut-il revoir le tarif de Faction à la hausse pour que l'option pèse toujours ?

---

*Version : 3.2 — Phase 1 — 2026-08-30. **D116 — les Hommes d'armes de Dol Amroth rejoignent la ligne 4 (Troupes des Fiefs).** L'unité figurait dans l'ordre de bataille du Pelennor sous le nom trompeur de « Piquiers de Dol Amroth » sans exister au roster. Dol Amroth étant un fief au même titre que Lossarnach et le Lamedon, elle prend place sur la ligne des Troupes des Fiefs : 🔵 mêlée, 4 pts, Faction disponible (5 pts), pas de Bannière. Aucun coût modifié, aucune ligne créée.*

*Version : 3.1 — Phase 1 — 2026-08-23. **Correction (D110) — Chevaliers à pied de Dol Amroth restent 🔴, pas 🔵.** Erreur de classe introduite en v3.0 : ils gardent leur classe lourde d'origine (Armure 1 + Poursuite 1 intrinsèques). Coût de base corrigé 4→**5**, avec Bannière 5→**6**. Note de reclassement erronée retirée.*

*Version : 3.0 — Phase 1 — 2026-08-23. **Simplification radicale (arbitrage Emmanuel) — refonte complète.** Roster resserré de 13 à 7 lignes : plus aucun badge par défaut, profil de base = Type+Combat+Classe seul. Faction devient un outil optionnel (« Défenseur de la Terre du Milieu » = [Relance 1], remplace [Défense X]), disponible sur les unités marquées éligibles, jamais un supplément systématique. Bannière reste optionnelle, disponible sélectivement. Familles fusionnées : Rangers (ex-10/11/12), Troupes régulières de Minas Tirith (ex-1/5), Troupes des Fiefs (ex-8/9), Cavalerie du Gondor (ex-3/4). Compagnie Grise entièrement bespoke : six figurines nommées, chacune sa propre règle tant qu'elle est présente (retour à l'esprit pré-D073) ; chiffrée à **15** pts (méthode barème+bespoke, cohérente avec le Mûmakil).*

*Version : 2.5 — Phase 1 — 2026-08-23. **P8 — recalcul complet (D097/D098).** Faction ciblée : retirée par défaut de tout le roster, réapparaît sur toute unité avec Leader. Anciens badges Spéciale/Élite renommés « règles socle », coûts inchangés. Guerriers de Minas Tirith 5→**4** (seul changement de coût de base). Nouvelles variantes chiffrées : Chevaliers de Dol Amroth avec Imrahil = **14** ; Compagnie Grise avec Aragorn = **14** ; Lossarnach avec Forlong = **8** ; Lamedon avec Angbor = **8**. §4 (nouveau) récapitule les variantes Leader du Playtest #4.*

*Version : 2.3 — Phase 1 — 2026-08-16. **Corrections de relecture — revue de finalisation « Verrouillage v1.0 ».** Liens `[[Document de cadrage]]` corrigés en `[[Document_de_cadrage]]` (nom réel du fichier, 2 occurrences). En-tête « Aligné sur » rafraîchi (v0.12/v0.21/v0.19 → v0.13/v0.27/v0.24, versions réelles depuis P7c). Aucune décision mécanique — pas de numéro D.*

*Version : 2.2 — Phase 1 — 2026-08-13. **Collapse du système de badges (D080/D081, tâche P7c).** Faction ([Armure 1] renommée [Défense 1]) devient un trait de peuple universel — étendue à Lamedon (9) et toute la famille Rangers (10-12), auparavant sans Faction. Plafond à 1 badge secondaire (Spéciale/Élite/Légende) : Chevaliers de Dol Amroth (4) perd Spéciale, garde Élite, 8→**7 pts** (collision assumée avec Chevaliers de Minas Tirith) ; Rangers du Nord (12) perd Spéciale, garde Élite, coût inchangé (4). La Compagnie Grise (13), confirmée pièce Signature, est exemptée du plafond — inchangée. Récapitulatif des badges (§4) et points ouverts (§5) mis à jour.*

*Version : 2.1 — Phase 1 — 2026-08-08. **Pivot « badges universels » (D073).** Badge Élite enrichi (+ Jamais Faible, coût inchangé). Nouveau badge **Légende** (+1 dé de combat) : La Compagnie Grise (13) perd tout son empilement de règles bespoke ([Archer en mêlée], [Férocité]) au profit des quatre badges standard (Faction + Spéciale + Élite + Légende) — sort du régime « hors matrice », chiffrée à la matrice comme le reste du roster. Coût 6 → **7 pts**, devient l'une des unités d'infanterie les plus chères du roster. Profils 1-12 inchangés (Faction/Spéciale déjà conformes au nouveau standard). Non testé — validation P7a.*

*Version : 2.0 — Phase 1 — 2026-08-08. **Refonte P4 (D067) : re-expression complète sur la taxonomie visuelle et le système de badges.** Roster resserré de 14 à 13 unités (Vétérans d'Osgiliath retirés, Archers de la Racine Noire fusionnés dans la famille Rangers, Rangers du Nord ajoutés). Trois badges fixes (Faction/Spéciale/Élite) remplacent le barème à valeur variable. Compagnie Grise refondue : 6→4 figurines, règles actives en permanence (fin du suivi conditionnel par figurine), badge Élite ajouté. Renommage [Arme Lourde X]→[Relance X] (D066) répercuté. Non testé — validation P7a.*
