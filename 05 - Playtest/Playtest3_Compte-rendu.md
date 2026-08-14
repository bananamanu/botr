---
projet: "Batailles de la Terre du Milieu"
type: "playtest"
phase: "1"
statut: "clos"
date_maj: "2026-08-13"
tags: [BdTdM, "type/playtest", "phase/1", "statut/analyse", "playtest/3"]
version: "1.0"
---

# Playtest #3 — Validation du « big bang » (P7a)

> **Objet de ce document :** débrief du grand playtest solo (Emmanuel MJ des deux camps, tirage aléatoire de la carte de commandement à chaque tour pour ne favoriser aucun camp), joué le 2026-08-13, déployant **les six peuples simultanément**, Harad avec le Mûmakil compris. Objectif du test : valider en conditions réelles tout ce qui portait la mention *« non testé — validation en P7a »* depuis le sprint de refonte P1-P6 — lisibilité de la taxonomie visuelle, système de badges, refonte Mûmakil/Furie (P5), équilibre de la matrice de points (P3). Décisions D080-D084.
>
> ⚠️ Ce compte-rendu **acte et journalise** ; la répercussion mécanique du collapse de badges (§2) dans `[[Regles_Base]]`, `[[Regles_Speciales]]`, `[[Regles_Points]]` et les 6 rosters est le travail de la tâche **P7c**, distincte et à boucler avant le jalon « Verrouillage v1.0 » du 18/08. La réécriture du §3 (principes) et de la feuille de route du cadrage suit en fin de P7b.

---

## 1. Résultat & déroulé

| | |
|---|---|
| **Format** | Solo, MJ des deux camps — main de 6 cartes, carte de commandement tirée au hasard chaque tour (neutralité délibérée, pas de main jouée stratégiquement d'un côté) |
| **Déploiement** | Les six peuples sur table simultanément, Harad avec Mûmakil |
| **Résultat** | **Victoire du Mal, 11–9** |

**Ordre de bataille — Mal :** Cataphractaires orientaux, Cohorte d'orientaux, Cohorte de piquiers orientaux, Cohorte d'archers orientaux, Bande d'orques du Mordor, Bande d'orques du Morannon, Bande de pisteurs orques, Bande d'uruk-hai du Mordor, Troll du Mordor, Archers du Harad, Lanciers du Harad (×3), Mûmakil, Pillards de Khand (hache), Pillards de Khand (archer), Aurige de Khand.

**Ordre de bataille — Bien :** Éored de cavalier du Rohan (×3), Éored d'éclaireur, Milice lige, Archers liges, Gardes royaux à cheval (×2), Gardes Royaux du Rohan, Guerriers de Minas Tirith (×2), Archers de Minas Tirith, Chevaliers de Dol Amroth, Garde de la Citadelle, Hommes d'armes de Dol Amroth, Guerriers de Lossarnach, Guerriers des clans de Lamedon, Rangers du Gondor.

**Verdict d'ensemble :** score serré, pas de déséquilibre structurel identifié — le ratio quantité (Bien) / qualité (Mal) reproduit une texture déjà connue de BattleLore V1/C&C (D084). Le test valide surtout la **mécanique**, moins l'équilibre fin (à l'échelle 6 peuples simultanés en solo, la lecture d'équilibre reste indicative).

---

## 2. Le constat qui prime : accumulation de badges → collapse du système (D080-D081)

**C'est le retour le plus structurant du test, avant tout ajustement de profil.** En jouant les six peuples soi-même, l'empilement de badges (Faction + Spéciale + Élite/Légende, jusqu'à 3-4 lignes de règles par figurine sur certains profils) s'est révélé lourd à porter à la table — y compris pour le concepteur du système. Emmanuel a corrigé en cours de partie par une houserule, désormais actée comme décision de design :

- **Le badge Faction cesse d'être un badge/token.** Il devient un **trait de peuple**, imprimé une fois et appliqué automatiquement à toutes les unités du roster — plus rien à poser sur le plateau pour le signaler.
- **Chaque unité porte au maximum un badge**, choisi parmi **Spéciale / Élite / Légende** (fin du cumul introduit par D073).
- **Les pièces signature** (Compagnie Grise, Mûmakil, et candidats à confirmer — Troll, Aurige de Khand…) sortent de la matrice de badges et conservent leurs règles bespoke propres, comme c'était déjà le cas pour le Mûmakil.

Constat de terrain sur l'application : pour Harad, Khand et Rohan, la règle de Faction couvrait déjà tout le roster (rien à changer). Pour Gondor et les Orientaux, la règle de Faction ([Armure 1]) n'était portée que par les profils lourds 🔴 (l'armure basse étant déjà intrinsèque à cette classe) — l'houserule l'a étendue à tout le roster sous un nom **distinct de l'intrinsèque**, **[Défense 1]**, pour ne pas se confondre avec le plancher [Armure 1] du 🔴. Pour Mordor, [Horde] a été étendue à toute l'infanterie du roster, y compris l'Uruk-hai (auparavant hors périmètre de la règle).

**Ce constat revient sur D073** (pivot « badges universels », cumul jusqu'à 4 badges) : le mandat qu'il visait — asymétrie de peuple sans prolifération de règles bespoke — reste juste, mais le curseur du cumul était mal placé. D080-D081 resserrent au lieu d'annuler.

> 🔗 **Répercussion technique** — répartie en tâche **P7c** (`Regles_Base`, `Regles_Speciales`, `Regles_Points`, 6 rosters, cadrage). Non exécutée dans ce document.

---

## 3. Mûmakil / Furie (validation de la refonte P5)

Le Mûmakil a traversé toute la carte et causé à lui seul au moins 3 destructions et autant d'affaiblissements — **verdict : redevenu un atout majeur**, à l'inverse du bilan du Playtest #2 (« la bête est un boulet »). La refonte P5 (PV 8, Protection 1 contre le tir, [Charge écrasante]/[Inébranlable ∞] tarifées à 15/15 pts) tient à l'usage.

**Point notable : la Furie ne s'est jamais déclenchée.** Le Mûmakil a perdu ses deux derniers points de vie en un seul coup, sans jamais passer par le palier « 1 PV » qui déclenche l'état (D082). **Décision : pas de correctif.** La Furie reste un bonus conditionnel de fin de vie, pas une garantie — le comportement observé (mourir avant de l'atteindre) est un résultat de jeu acceptable, pas un trou de règle à combler.

**Point de vigilance conservé, sans correctif immédiat (D083) :** un doute soulevé en cours de partie sur la force de la contre-attaque du Mûmakil. Pas assez d'évidence pour trancher un chiffre — à surveiller au prochain test, sur le modèle du traitement réservé à [Mur de bouclier] au Playtest #1b.

---

## 4. Équilibre de la matrice de points (P3)

**Aucun déséquilibre spécifique identifié** sur cette partie. Le ratio quantité (Bien, 14 unités) / qualité (Mal, 15 unités dont Mûmakil) reproduit une texture déjà connue de BattleLore V1 et des autres C&C — pas un signal propre à la refonte P1-P6 (D084). Le socle Infanterie 4 PV / Cavalerie 3 PV n'a rien montré d'anormal.

---

## 5. Composants visuels et lisibilité (P6)

**Le rendu couleur = classe = nombre de dés a « super bien marché »** — validation nette de l'axiome fondateur du pivot D059/D060, celui-là même que le Playtest #2 avait fait échouer. C'est le résultat le plus important du test : l'objectif *easy-to-play* qui avait motivé tout le sprint de refonte est atteint sur son critère le plus dur (distinction visuelle des unités sans consulter de fiche).

Un seul token par unité (mode mêlée/distance) a suffi en configuration solo. Verdict d'Emmanuel : si l'on veut pousser la simplicité encore plus loin, le prochain candidat à la coupe serait la règle de Faction elle-même — non retenu à ce stade (voir §6).

---

## 6. Identité de peuple

Constat en tension avec le collapse de badges (§2) : en réduisant l'écart mécanique entre profils d'un même peuple, **les unités se ressemblent davantage entre elles** — mais **la règle de Faction, désormais universelle par peuple, porte l'essentiel de l'identité restante**. C'est jugé suffisant pour l'instant (pas de perte d'identité perçue comme problématique), mais noté comme point à surveiller si un futur passage veut aller plus loin vers la simplicité — toute nouvelle coupe rognerait directement sur l'identité de peuple, plus sur du superflu.

---

## 7. Suivi documentaire

| Document | État |
|---|---|
| `[[Playtest3_Compte-rendu]]` (ce fichier) | **créé** |
| `00 - META/Document_de_cadrage.md` | à amender — D080 à D084 + réécriture §3/feuille de route (fin P7b) |
| `Regles_Base.md` / `Regles_Speciales.md` / `Regles_Points.md` | à répercuter — **P7c** (collapse badges) |
| 6 rosters `02 - Factions/*.md` | à re-exprimer sur 1 badge max — **P7c** |
| Scénario Pelennor (Phase 3) | note de scope : condition de victoire propre au scénario, hors décompte de médailles générique — à formaliser à la rédaction du scénario |

---

> 🔗 **Voir aussi**
> `[[Playtest2_Compte-rendu]]` · `[[Document_de_cadrage]]` (D059/D060, D073, D079)

---

*Version : 1.0 — Phase 1 — 2026-08-13. Compte-rendu du Playtest #3 (validation P7a, solo Emmanuel MJ des deux camps, six peuples déployés simultanément dont Harad/Mûmakil). Résultat 11–9 Mal. Verdict structurant : taxonomie couleur/classe/dés validée sans réserve ; accumulation de badges constatée en jeu → collapse à 1 badge max par unité + Faction en trait de peuple (D080-D081, répercussion en P7c) ; refonte Mûmakil/Furie (P5) validée, Furie jamais déclenchée mais jugée conforme (D082) ; contre-attaque Mûmakil en vigilance (D083) ; ratio de points Bien/Mal conforme aux références C&C, aucun déséquilibre à corriger (D084). Aucune règle ni profil retouché dans ce document.*
