---
## projet: "Batailles de la Terre du Milieu" 
type: "faction" 
phase: "1" 
statut: "brouillon-a-tester" 
date_maj: "2026-07-26" 
tags: [BdTdM, "type/faction", "peuple/rohan", "statut/valide-playtest1"] 
version: "1.3"
---
# Rohan — Profils d'unités

> **Objet de ce document :** Profils de troupes pour le peuple Rohan (9 unités, liste fournie par Emmanuel), en réponse à la tâche Todoist du 20/07/2026 (« Rédiger les profils d'unités — Rohan »). **Roster complet revu profil par profil et validé par Emmanuel le 2026-07-19 — prêt pour le Playtest #1.** Non testé en partie réelle : les ajustements de cette revue (notamment le coût provisoire de [Déploiement avancé]) restent à confirmer une fois passés à la table.
> 
> Historique de la revue :
> 
> - **Passe 1** : Éored de cavalier ([Poursuite 2]), Éored d'éclaireur ([Mobilité 2]), Archers liges (+[Mobilité 1]) ; Milice lige confirmée.
> - **Passe 2** : nouvelle règle [Déploiement avancé] créée pour l'Éored d'éclaireur (+ Mouvement à 4) ; Gardes royaux à cheval et Garde du roi à cheval alignés sur [Poursuite 2] ; Garde du Roi à 4 dés ; Helmingas de Grimbolg + [Arme Lourde 1] ; Gardes Royaux du Rohan confirmés.
> - **Passe 3 (clôture)** : [Charge écrasante] confirmée pour la Garde du roi à cheval. Le Mûmakil aura sa propre règle dédiée (idée déjà en tête d'Emmanuel) plutôt que de réutiliser [Charge écrasante] — voir [[Regles_Speciales]].
> 
> **Choix d'identité actés :**
> 
> - Le Rohan se distingue de Gondor par l'**armure rare** : seules les troupes royales/légendaires portent [Armure X].
> - **« Le Rohan doit avoir la meilleure cavalerie »** : toute la cavalerie de mêlée du roster (standard, élite, légendaire) partage [Poursuite 2] — la différenciation de palier se fait par l'armure, les dés d'attaque et les règles supplémentaires.
> - **Milice lige / Archers liges** : un cran en dessous des standards de Gondor.
> - **Helmingas de Grimbolg** : glossaire existant ([Inébranlable X] + [Férocité]) + [Arme Lourde 1] (haches à deux mains).
> - **Éored d'éclaireur** : « l'Éored, mais au tir ». Depuis le 2026-07-26 : 2 dés, Mouvement 3, et [Vigilant] (D050, hit-and-run, adaptée des Riverwatch Riders de BattleLore V2) remplace [Déploiement avancé], retirée de la V1.
> - **Éored de cavalier du Rohan** : porte désormais [Prise de flanc] (D049, ex-« Flanking », même origine BattleLore V2) en plus de [Poursuite 2] — 7 pts (au lieu de 6).
> 
> Aligné sur [[Regles_Base]] et [[Regles_Speciales]]. **[Déploiement avancé]**, créée pour l'Éored d'éclaireur (D028), a été **retirée de la V1 le 2026-07-26 (D047)**. Les deux mots-clés « Vigilant Flanking » de BattleLore V2 sont désormais répartis entre deux unités du Rohan : **[Prise de flanc]** (D049) sur l'Éored de cavalier, **[Vigilant]** (D050) sur l'Éored d'éclaireur. **[Charge écrasante]** a été retirée de la Garde du roi à cheval — et de toute la V1 — après le Playtest #1 (D043) ; le Mûmakil recevra une règle d'impact dédiée distincte (Phase 2).
> 
> **Coût en points** calculé avec la formule validée dans [[Regles_Points]] : `Points_finaux = round((Mouvement + PV + Attaque×D + Σ coût des règles) ÷ 3) − 1`.

---

## Conventions de ce roster

- **Mouvement** : 2 pour toute Infanterie, 3 pour toute Cavalerie (D022) — **aucune exception** dans ce roster : l'Éored d'éclaireur, autrefois à Mouvement 4 pour [Déploiement avancé], est resté à Mouvement 3 standard depuis que cette règle a été retirée (D047).
- **Portée de tir** : 4 hexagones pour toutes les unités de tir (D020).
- **Règles spéciales** : 0 à 2 par défaut pour les troupes standard/élite ; les unités légendaires peuvent en cumuler davantage (D023).
- **Pas de piquiers dans cette liste** — [Réception de charge] reste ouverte pour un futur profil du Rohan (D021) mais n'est assignée à aucune des 9 unités ci-dessous.
- **Logique d'escalade cavalerie standard → élite → légendaire (Rohan)** : [Poursuite 2] est partagé par les trois paliers de cavalerie de mêlée (profils 1, 5, 8). Ce qui distingue les paliers : l'armure (absente en standard, présente dès l'élite) et les dés d'attaque (3 → 4). *(Depuis le Playtest #1, [Charge écrasante] ne distingue plus le légendaire — elle a été retirée de la V1, D043.)*

---

## 1. Liste des troupes

|#|Unité|Type|Combat|Statut|**Points**|
|---|---|---|---|---|---|
|1|Éored de cavalier du Rohan|Cavalerie|Mêlée|Ligne standard|**6**|
|2|Milice lige|Infanterie|Mêlée|Ligne standard|**4**|
|3|Archers liges|Infanterie|Tir|Ligne standard|**3**|
|4|Éored d'éclaireur|Cavalerie|Tir|Ligne standard|**4**|
|5|Gardes royaux à cheval|Cavalerie|Mêlée|Élite|**8**|
|6|Gardes Royaux du Rohan|Infanterie|Mêlée|Élite|**6**|
|7|Garde du Roi|Infanterie|Mêlée|**Légendaire**|**8**|
|8|Garde du roi à cheval|Cavalerie|Mêlée|**Légendaire**|**8**|
|9|Helmingas de Grimbolg|Infanterie|Mêlée|**Légendaire**|**7**|

> 🎲 **Note de design — hiérarchie du roster validé**
> 
> - **Ligne standard** (1-4) : jamais d'armure. La cavalerie porte la signature Rohan ([Poursuite 2]/[Mobilité]/[Déploiement avancé]), l'infanterie de levée (milice, archers) n'a pas ou peu de règles.
> - **Élite** (5-6) : première apparition de l'armure — marqueur des troupes royales.
> - **Légendaire** (7-9) : 3 règles spéciales chacune, choisies pour raconter un moment précis du texte — la mort de Théoden entouré des siens (7, 8) et la résistance de Grimbold aux Gués de l'Isen (9).
> 
> Trois unités à égalité à 8 points (5, 7, 8) : conséquence assumée de la compression d'échelle, précédent déjà vu chez Gondor (Gardes de la Citadelle = Vétérans d'Osgiliath) — validé tel quel par Emmanuel.

---

## 2. Profils détaillés

### 1. Éored de cavalier du Rohan
![[cavalier_rohan-page001.png]]

|Type|Combat|Mouvement|Attaque|Portée|PV|**Points**|
|---|---|---|---|---|---|---|
|Cavalerie|Mêlée|3|3 dés|—|3 figurines|**7**|

**Règles spéciales :** [Poursuite 2] + [Prise de flanc]

**Note narrative :** le cœur de la cavalerie du Rohan — les cavaliers de la Marche, dont la charge a brisé le siège de Minas Tirith. « Le Rohan doit avoir la meilleure cavalerie du jeu » : [Poursuite 2] permet d'enchaîner deux fois mouvement + attaque en alternative à l'avance. Pas d'armure : l'identité du Rohan reste dans le mouvement, pas la protection. [Prise de flanc] complète le tableau : un éored qui tient une ligne ennemie au contact ouvre la voie aux autres unités du camp, qui frappent avec 1 dé de plus contre cette cible — la cavalerie de ligne ne se contente pas de charger, elle crée la brèche pour le reste de l'armée.

> 🔄 **Nouvelle règle assignée — 2026-07-26 (D049)**
> [Prise de flanc] (ex-« Flanking »), d'abord créée pour l'Éored d'éclaireur (D047), est réassignée ici sur arbitrage d'Emmanuel — l'éclaireur reçoit [Vigilant] à la place (profil 4). Recalcul : `Mvt 3 + PV 3 + 3×3 + [Poursuite 2](6) + [Prise de flanc](3) = 24 → round(24÷3)−1 = 7`. Coût **6 → 7 pts** — contrairement aux ajustements précédents, l'arrondi n'absorbe pas cette fois l'ajout : c'est une vraie hausse de coût, pas un effet de compression gratuit.

> 🔗 **Voir aussi** [[Regles_Speciales]] — [Poursuite X] · [Prise de flanc]

---

### 2. Milice lige
![[guerrier_rohan-page001.png]]

|Type|Combat|Mouvement|Attaque|Portée|PV|**Points**|
|---|---|---|---|---|---|---|
|Infanterie|Mêlée|2|2 dés|—|6 figurines|**4**|

**Règles spéciales :** [Arme de jet 1]

**Note narrative :** la levée du Rohan — paysans et hommes de ferme convoqués par devoir de « lige », armés de ce qu'ils ont sous la main : lances, épieux, et surtout javelots et haches de jet lancés en approche. Un cran en dessous des Guerriers de Minas Tirith (3 dés, [Armure 1]) au corps à corps, mais [Arme de jet 1] lui rend une bouffée d'agressivité quand elle charge : le tour où elle s'est déplacée puis attaque, une face **Cible** obtenue compte comme une touche (les projectiles lancés avant le choc).

> 🔄 **Modifié après playtest — 2026-07-25 (Playtest #1, D044)**
> Ajout de [Arme de jet 1]. À la table, la Milice lige (2 dés, aucune règle) s'était révélée « trop nulle », sans rôle propre. La règle lui rend une identité de levée qui escarmouche à la lance et à la hache de jet, sans en faire une ligne de front à la Gondor : c'est [Archer en mêlée] (Compagnie Grise) en version conditionnelle (seulement en chargeant) et plafonnée à X. Coût 1×X ; la compression laisse le total à **4 pts** (inchangé).

> 🔗 **Voir aussi** [[Regles_Speciales]] — [Arme de jet X] · [Archer en mêlée] · [[Document de cadrage]] principe 6

---

### 3. Archers liges
![[archer_rohan-page001.png]]

|Type|Combat|Mouvement|Attaque|Portée|PV|**Points**|
|---|---|---|---|---|---|---|
|Infanterie|Tir|2|2 dés|4|6 figurines|**3**|

**Règles spéciales :** [Mobilité 1]

**Note narrative :** chasseurs et archers de village mobilisés aux côtés de la milice — même compétence de tir que les Archers de Minas Tirith (2 dés), sans la cotte de mailles de leurs homologues de Gondor. [Mobilité 1] leur permet de tirer puis de se replacer.

> 🔗 **Voir aussi** [[Regles_Speciales]] — [Mobilité X] · [Armure X] _(non portée ici)_

---

### 4. Éored d'éclaireur
![[eclaireur_rohan-page001.png]]

|Type|Combat|Mouvement|Attaque|Portée|PV|**Points**|
|---|---|---|---|---|---|---|
|Cavalerie|Tir|3|2 dés|4|3 figurines|**4**|

**Règles spéciales :** [Mobilité 2] + [Vigilant]

**Note narrative :** les éclaireurs qui patrouillent les frontières de la Marche — le même éored que l'unité 1, tourné vers le harcèlement à distance et la reconnaissance. [Mobilité 2] permet de tirer puis se replacer loin de toute riposte ; [Vigilant] scelle le profil hit-and-run : quelle que soit l'issue de son tir, la cible ne peut jamais le contre-attaquer — l'éclaireur frappe et s'efface avant que l'ennemi n'ait pu réagir.

> 🔄 **Révisé — 2026-07-26 (retour sur D046, D047)**
> Après un nouvel examen, Emmanuel revient sur deux points du Playtest #1 : l'attaque repasse de 3 à **2 dés**, et [Déploiement avancé] est **retirée** (retirée de toute la V1 — aucune autre unité ne la portait). En remplacement, nouvelle règle **[Flanking]**, adaptée des Riverwatch Riders de *BattleLore : Seconde Édition*. Recalcul : `Mvt 3 + PV 3 + 2×2 + [Mobilité 2](2) + [Flanking](3) = 15 → round(15÷3)−1 = 4`. Coût **4 pts inchangé**.

> 🔄 **Révisé une seconde fois — 2026-07-26 (D049, D050)**
> [Flanking], renommée **[Prise de flanc]**, est réassignée à l'Éored de cavalier (profil 1) — la cavalerie de ligne au contact, pas l'éclaireur. En remplacement, nouvelle règle **[Vigilant]** : la cible de cette unité ne peut jamais la contre-attaquer. Les deux mots-clés d'origine des Riverwatch Riders (« Vigilant Flanking ») sont ainsi répartis sur deux unités distinctes du Rohan, chacune avec sa propre identité — le soutien de groupe pour la cavalerie de ligne, l'immunité hit-and-run pour l'éclaireur. Recalcul : `Mvt 3 + PV 3 + 2×2 + [Mobilité 2](2) + [Vigilant](2) = 14 → round(14÷3)−1 = 4`. Coût **4 pts inchangé**.

> 🔗 **Voir aussi** [[Regles_Speciales]] — [Mobilité X] · [Vigilant]

---

### 5. Gardes royaux à cheval

|Type|Combat|Mouvement|Attaque|Portée|PV|**Points**|
|---|---|---|---|---|---|---|
|Cavalerie|Mêlée|3|4 dés|—|3 figurines|**8**|

**Règles spéciales :** [Armure 1] + [Poursuite 2]

**Note narrative :** l'escorte montée de la maison du roi — mieux protégée et mieux montée que les éoreds ordinaires. Garde le même [Poursuite 2] que la troupe standard (1) : la différence de palier tient à l'armure et au dé d'attaque supplémentaire.

> 🔗 **Voir aussi** [[Regles_Speciales]] — [Armure X] · [Poursuite X]

---

### 6. Gardes Royaux du Rohan

|Type|Combat|Mouvement|Attaque|Portée|PV|**Points**|
|---|---|---|---|---|---|---|
|Infanterie|Mêlée|2|3 dés|—|6 figurines|**6**|

**Règles spéciales :** [Armure 1] + [Inébranlable 1]

**Note narrative :** les gardiens de Meduseld, la salle dorée d'Edoras — la garde d'honneur du roi, bien équipée et disciplinée. Même formule que les Gardes de la Citadelle de Gondor (5).

> 🔗 **Voir aussi** [[Regles_Speciales]] — [Armure X] · [Inébranlable X]

---

### 7. Garde du Roi — _unité légendaire_

|Type|Combat|Mouvement|Attaque|Portée|PV|**Points**|
|---|---|---|---|---|---|---|
|Infanterie|Mêlée|2|**4 dés**|—|6 figurines|**8**|

**Règles spéciales :** [Armure 1] + [Inébranlable 2] + [Férocité]

**Note narrative :** les hommes de la maison du roi qui se battent à pied autour de Théoden lorsque Grisenel tombe sur les Champs du Pelennor — un cercle qui ne cède pas et qui frappe aussi fort qu'il encaisse.

> 🔗 **Voir aussi** [[Regles_Speciales]] — [Armure X] · [Inébranlable X] · [Férocité]

---

### 8. Garde du roi à cheval — _unité légendaire_

|Type|Combat|Mouvement|Attaque|Portée|PV|**Points**|
|---|---|---|---|---|---|---|
|Cavalerie|Mêlée|3|4 dés|—|3 figurines|**8**|

**Règles spéciales :** [Armure 1] + [Poursuite 2]

**Note narrative :** les chevaliers de la maison du roi qui chevauchent à ses côtés depuis Edoras jusqu'au Pelennor — la meilleure cavalerie du Rohan. L'armure des troupes royales ([Armure 1]) et la meilleure cavalerie du jeu ([Poursuite 2], deux enchaînements mouvement + attaque) suffisent à en faire une pièce d'élite redoutable, sans surcouche de dégâts en éclaboussure.

> 🔄 **Modifié après playtest — 2026-07-25 (Playtest #1, D043)**
> Retrait de [Charge écrasante]. Au test, le couple [Charge écrasante] + [Poursuite]/charge de cavalerie s'est révélé être une boucherie (deux enchaînements de charge, deux salves d'éclaboussures). [Charge écrasante] est retirée de **tous** les profils de la V1 ; l'effet de choc de masse est réservé aux grandes créatures (règle dédiée du Mûmakil, Phase 2). La compression laisse le coût à **8 pts** (inchangé). L'unité conserve [Armure 1] + [Poursuite 2].

> 🔗 **Voir aussi** [[Regles_Speciales]] — [Armure X] · [Poursuite X]

---

### 9. Helmingas de Grimbolg — _unité légendaire_

|Type|Combat|Mouvement|Attaque|Portée|PV|**Points**|
|---|---|---|---|---|---|---|
|Infanterie|Mêlée|2|3 dés|—|6 figurines|**7**|

**Règles spéciales :** [Inébranlable 2] + [Férocité] + [Arme Lourde 1]

**Note narrative :** les hommes du Pays de Norfolde restés fidèles à Grimbold, qui a tenu les Gués de l'Isen face aux forces de Saroumane avant de mourir plus tard sur le Pelennor — une résistance acharnée, armée de haches à deux mains, sans l'équipement des troupes royales.

> 🔗 **Voir aussi** [[Regles_Speciales]] — [Inébranlable X] · [Férocité] · [Arme Lourde X]

---

## 3. Récapitulatif des règles spéciales utilisées

|Règle|Unités qui la portent|
|---|---|
|[Poursuite 2]|Éored de cavalier du Rohan (1) · Gardes royaux à cheval (5) · Garde du roi à cheval (8)|
|[Mobilité 2]|Éored d'éclaireur (4)|
|[Mobilité 1]|Archers liges (3)|
|[Prise de flanc]|Éored de cavalier du Rohan (1) *(D049, ex-« Flanking »)*|
|[Vigilant]|Éored d'éclaireur (4) *(nouvelle règle, D050, remplace [Prise de flanc])*|
|[Armure 1]|Gardes royaux à cheval (5) · Gardes Royaux du Rohan (6) · Garde du Roi (7) · Garde du roi à cheval (8)|
|[Inébranlable 1]|Gardes Royaux du Rohan (6)|
|[Inébranlable 2]|Garde du Roi (7) · Helmingas de Grimbolg (9)|
|[Férocité]|Garde du Roi (7) · Helmingas de Grimbolg (9)|
|[Arme de jet 1]|Milice lige (2)|
|[Arme Lourde 1]|Helmingas de Grimbolg (9)|

Aucune règle liée aux piques ([Réception de charge]) n'est utilisée. [Charge écrasante] a été retirée de la Garde du roi à cheval au Playtest #1 (D043) — plus aucune unité du Rohan ne la porte.

---

## 4. Note de clôture — sous-ensemble pour le Playtest #1

- **Éored de cavalier du Rohan** (1) — cavalerie, [Poursuite 2] + [Prise de flanc]. **7 points.**
- **Milice lige** (2) — infanterie de mêlée, [Arme de jet 1]. **4 points.**
- **Archers liges** (3) — infanterie de tir, [Mobilité 1]. **3 points.**

Soit **13 points** pour le trio Rohan. Le roster complet (9 unités) est disponible pour des tests ultérieurs une fois ce socle validé.

---

## 5. Points restants — non bloquants pour le Playtest #1

Tout est validé pour lancer le Playtest #1. Deux points à garder en tête pour la suite, sans être des blocages :

- **[Déploiement avancé] retirée de la V1** (D047, 2026-07-26) — jamais éprouvée en partie réelle (le centre-funnel du Playtest #1 n'a pas donné de verdict). Plus aucune unité ne la porte.
- **Coût de [Prise de flanc]** (3 pts forfaitaires, Éored de cavalier) et **[Vigilant]** (2 pts forfaitaires, Éored d'éclaireur) : deux nouvelles règles, non testées — à surveiller au prochain playtest. Le trio suggéré pour le Playtest #1 (§4 ci-dessus) grimpe de 13 à **14 points** avec l'Éored de cavalier à 7 pts.
- **Aucun profil de piquiers pour le Rohan** : [Réception de charge] reste ouverte si une future unité de piquiers du Rohan est ajoutée (D021).

---

_Version : 1.0 — Phase 1 — 2026-07-19. Roster complet Rohan (9 unités), revu profil par profil et validé par Emmanuel. [Charge écrasante] confirmée pour la Garde du roi à cheval (D029) ; le Mûmakil aura sa propre règle. Prêt pour le Playtest #1 — non testé en partie réelle._

_Version : 1.1 — Phase 1 — 2026-07-25. **Mise à jour post-Playtest #1** (`[[Playtest1_Compte-rendu]]`). Trois profils modifiés : Milice lige +[Arme de jet 1] (D044, 4 pts inchangé) ; Éored d'éclaireur 2→3 dés et Mouvement 4→3, suppression de l'exception de Mouvement du roster (D046, 4 pts inchangé) ; Garde du roi à cheval — retrait de [Charge écrasante], retirée de toute la V1 (D043, 8 pts inchangé). Conventions, entête et récapitulatif mis à jour en conséquence._

_Version : 1.2 — Phase 1 — 2026-07-26. **Retour sur l'Éored d'éclaireur** (D047) : attaque 3→2 dés, [Déploiement avancé] retirée de la V1, nouvelle règle [Flanking] ajoutée (adaptée des Riverwatch Riders, BattleLore V2) — 4 pts inchangé. Conventions, entête et récapitulatif mis à jour._

_Version : 1.3 — Phase 1 — 2026-07-26. « Flanking » renommée **[Prise de flanc]** et réassignée à l'**Éored de cavalier du Rohan** (profil 1, D049) — passe de 6 à **7 pts**. Nouvelle règle **[Vigilant]** créée (D050) et assignée à l'Éored d'éclaireur en remplacement — 4 pts inchangé. Les deux mots-clés d'origine « Vigilant Flanking » (BattleLore V2) sont ainsi répartis sur deux unités distinctes. Trio du Playtest #1 : 13 → **14 points**. Conventions, entête et récapitulatif mis à jour._