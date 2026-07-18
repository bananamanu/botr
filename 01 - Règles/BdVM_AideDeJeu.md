---
projet: "Batailles du Vieux Monde"
type: "aide-de-jeu"
phase: 1.6
statut: "à-tester"
date_maj: "2026-06-01"
tags: [BdVM, "type/aide-de-jeu", "phase/1.6", "statut/à-tester"]
---

# Batailles du Vieux Monde — Aide de jeu

> **Objet de ce document :** Référence rapide à conserver sur la table pendant la partie.
> Aligné sur **BdVM_Regles_Base v4.2** et **BdVM_Regles_Speciales v2.2**.

> 🔗 **Voir aussi** [[BdVM_Regles_Base]] — [[BdVM_Regles_Speciales]] — [[BdVM_Terrain]]

---

## 1. Séquence de retraite

La retraite est résolue à l'**étape 8** de chaque combat (après retrait des figurines).

### Étapes

1. **Compter les Drapeaux** obtenus par l'attaquant.
2. **Chaque Drapeau** force la cible à reculer d'**1 hexagone**.
   - Si l'unité possède **[Inébranlable X]**, elle ignore X Drapeaux par attaque reçue.
3. **Déterminer la direction** :
   - **Mêlée :** à l'opposé de l'unité attaquante.
   - **Tir :** à l'opposé du bord d'hexagone par lequel la ligne de vue a été tracée.
4. **Résoudre les obstacles sur le chemin :**
   - **Terrain boisé ou gué :** arrêt immédiat — chaque hexagone de retraite non résolu inflige **1 touche**.
   - **Terrain impassable (cours d'eau) ou bord du plateau :** bloqué — chaque hexagone non résolu inflige **1 touche**.
   - **Unité ennemie :** bloqué — chaque hexagone non résolu inflige **1 touche**.
   - **Unité amie :** **soutien** — tous les hexagones restants ignorés, aucune touche supplémentaire.

> **Rappels :**
> - Les restrictions de mouvement liées au terrain sont **ignorées** pendant la retraite.
> - Une unité en retraite **ne peut pas contre-attaquer** ce tour.
> - Le terrain surélevé ne bloque pas la retraite — l'unité continue normalement.

### Tableau récapitulatif

| Drapeaux reçus | [Inébranlable X] ? | Retraite effective |
|---|---|---|
| 1 | Non | 1 hex |
| 2 | Non | 2 hex |
| 3 | Non | 3 hex |
| 1 | [Inébranlable 1] | 0 hex |
| 3 | [Inébranlable 2] | 1 hex |
| 2 | [Inébranlable 2] | 0 hex |

---

## 2. Règle [Armure X]

### Résumé

Lorsqu'une unité avec **[Armure X]** reçoit une attaque de **mêlée**, elle retire **X faces Épée** des résultats avant de compter les touches.

### Ce que [Armure X] fait — et ne fait pas

| Situation | [Armure X] s'applique ? |
|---|---|
| Attaque de **mêlée** reçue | ✅ Oui |
| Attaque à **distance** reçue | ❌ Non |
| Face **Épée** dans les résultats | ✅ Retirée (jusqu'à X par attaque) |
| Face **Épées croisées** dans les résultats | ❌ Jamais annulée |
| Face **Drapeau** dans les résultats | ❌ Non affectée |

[Armure X] s'applique à l'**étape 4** de la séquence — après les relances, avant le décompte des touches.

> 💡 **Exemple**
> Des Lanciers attaquent des Chevaliers [Armure 1] : 3 dés → Épées croisées, Épée, Drapeau.
> [Armure 1] retire l'Épée → 1 Épées croisées + 1 Drapeau subsistent.
> Résultat : 1 PV perdu (Épées croisées sur Cavalerie = 1 PV) + 1 hexagone de retraite.

---

## 3. Types d'unités

### Tableau récapitulatif

| Type | Socle | Effectif | Jamais Faible ? | Règle intrinsèque |
|---|---|---|---|---|
| **Infanterie** | 20 mm ou 25 mm | 6 fig. (20 mm) · 4 fig. (25 mm) | Non | Épées croisées + Cible → **2 PV** chez la cible |
| **Cavalerie** | 25–40 mm | 3 figurines | Non | Aucune — 1 touche = 1 PV |
| **Créature** | 40–60 mm | Variable | ✅ Oui | Aucune — 1 touche = 1 PV · [Massif] natif |
| **Machine de guerre** | Variable | Variable | ✅ Oui | Aucune |
| **Artillerie** | — | 1 pièce + servants | ✅ Oui | Servants éliminés en premier |

### Règle intrinsèque Infanterie — Rappel

Contre une cible **Infanterie**, les faces **Épées croisées** et **Cible** infligent **2 PV** au lieu de 1.

> **Exception [Massif] :** les unités Infanterie portant cette règle (en pratique les socles 25 mm), ainsi que toutes les Créatures, ne subissent que **1 PV par touche**, quelle que soit la face.

### Tableau de dégâts complet

| Face de dé | Infanterie (sans [Massif]) | Infanterie [Massif] | Cavalerie | Machine de guerre | Créature |
|---|---|---|---|---|---|
| **Épées croisées** | **2 PV** | 1 PV | 1 PV | 1 PV | 1 PV |
| **Épée** | 1 PV | 1 PV | 1 PV | 1 PV | 1 PV |
| **Cible** | **2 PV** | 1 PV | 1 PV | 1 PV | 1 PV |

> L'Artillerie suit les mêmes règles de dégâts que la Cavalerie — 1 PV par touche.

---

## 4. Séquence de combat — Rappel express

| # | Étape | Notes |
|---|---|---|
| 1 | Déclarer la cible | |
| 2 | Lancer les dés | Modificateurs de terrain appliqués ici |
| 3 | Relancer / modifier | [Arme Lourde X], [Perforant X], [Réception de charge] |
| 4 | Appliquer **[Armure X]** | Retire les faces Épée (mêlée uniquement) |
| 5 | Compter les touches et les Drapeaux | Selon type d'attaque (mêlée / tir) |
| 6 | Appliquer **[Protection X]** | Ignore X touches (bâtiments) |
| 7 | Retirer les figurines | Voir tableau de dégâts §3 |
| 8 | Résoudre la retraite | 1 Drapeau = 1 hex · [Inébranlable X] s'applique ici |
| 9 | Contre-attaque | Si adjacent, vivant, pas en retraite |
| 10 | Avance | Si cible éliminée ou en retraite |

---

*Version : 1.1 — Phase 1.6 Étape 6 — 2026-06-01.*
*Aligné sur BdVM_Regles_Base v4.2 · BdVM_Regles_Speciales v2.2.*
*Corrections v1.1 : suppression de la valeur de Moral (D063), fusion Infanterie standard/élite,
suppression de [Tenace] de la séquence (D072), précision des effets de terrain en retraite.*
