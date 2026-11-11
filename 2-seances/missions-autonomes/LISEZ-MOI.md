# 🧠 Les missions autonomes

**Pour l'élève qui a fini avant les autres** — et qui a besoin d'autre chose qu'un exercice de plus.

Une mission autonome n'est **pas** un exercice de maison. La différence tient en une phrase :

> **Dans un exercice, on donne les étapes et l'élève écrit le code.
> Dans une mission, on donne le résultat attendu, et l'élève invente les étapes.**

C'est le premier pas vers le vrai métier : on y apprend à **écrire un algorithme avant de taper**.
Aucune notion nouvelle n'y est jamais introduite — **la difficulté est entièrement dans la conception.**

---

## Mission n°1 — 🏢 L'ascenseur de la tour · *après la séance 7*

| | |
|---|---|
| **La feuille de l'élève** | [page 1](mission-1-ascenseur-eleve-1.png) · [page 2](mission-1-ascenseur-eleve-2.png) · [**PDF, 2 pages recto-verso**](mission-1-ascenseur-eleve.pdf) |
| **Pour vous — à ne pas donner** | [page 1](mission-1-ascenseur-corrige-1.png) · [page 2](mission-1-ascenseur-corrige-2.png) · [PDF](mission-1-ascenseur-corrige.pdf) · [`.py`](mission-1-ascenseur-corrige.py) |
| **Boîte à outils** | tout ce qui a été vu **jusqu'à la séance 7**, et rien de plus |
| **Durée** | 1 h à 1 h 30, dont **au moins 15 minutes sans clavier** |

### Ce que l'élève reçoit

**Page 1 — la méthode.** C'est l'exemple d'algorithme qui a manqué en classe, et il porte sur un code
déjà écrit par toute la classe : **le coup joué de la séance 7**, en français à gauche, en Python à
droite, **ligne pour ligne**. Puis les quatre mots qui suffisent pour écrire un algorithme
(*je demande · je range · si… sinon… · j'affiche*), la méthode en quatre temps, et trois questions à
se poser en cas de blocage — **des questions, pas des réponses**.

**Page 2 — la mission.** Un cahier des charges de **sept règles**, trois lignes d'écran pour le ton,
**un cadre vierge pour écrire l'algorithme à la main**, cinq essais obligatoires avant de dire que
c'est fini, et trois défis ⭐⭐.

> **Il n'y a aucune ligne de code sur la feuille de l'élève**, et aucune étape. C'est écrit en haut
> de la page 1, en violet, pour que ce ne soit pas pris pour un oubli.

### Les trois règles de l'accompagnement

1. **Pas d'algorithme écrit, pas de clavier.** C'est la seule consigne ferme de la mission. Si l'élève
   ouvre Thonny avant d'avoir rempli le cadre violet, on l'y renvoie — gentiment, mais on l'y renvoie.
2. **On ne répond jamais par une ligne de code.** On répond **par une question**, et on s'éloigne.
   Les cinq questions à poser sont sur la feuille enseignant.
3. **Il n'y a pas une bonne réponse.** Tout programme qui respecte les sept règles est juste, même
   s'il ne ressemble en rien au corrigé. Le `.py` fourni est **une** solution ; la feuille enseignant
   liste ce qui est **vraiment faux** et ce qui est seulement **fait autrement**.

### Et après : faites-la présenter

Demandez-lui de présenter **son algorithme** à la classe, en trois minutes, au tableau,
**sans montrer le code**. Pour les autres, ce sera le premier algorithme qu'ils verront écrit par
quelqu'un de leur âge — et c'est la meilleure introduction possible à la notion.

---

## Si vous voulez en fabriquer d'autres

Le générateur est [`../generateurs/mission_ascenseur.py`](../generateurs/mission_ascenseur.py) :
il écrit les deux feuilles en HTML, puis le PDF et les images. La structure se réutilise telle quelle
pour une mission n°2 — seuls changent le cahier des charges, l'algorithme modèle et le corrigé.

**Trois sujets possibles pour la suite**, à mesure que la boîte à outils grandit :

| Quand | Sujet possible | Ce qu'il forcerait |
|---|---|---|
| après la **séance 9** | un distributeur de tickets qui refuse selon trois critères | combiner les conditions avec `and` et `or` |
| après la **séance 10** | une caisse de supermarché qui encaisse jusqu'au paiement | trouver seule la bonne condition d'arrêt |
| après la **séance 11** | un jeu de son choix, cahier des charges écrit **par l'élève** | tout, y compris définir le problème |

---

## Vérification faite

Le corrigé [`mission-1-ascenseur-corrige.py`](mission-1-ascenseur-corrige.py) **a été exécuté sur
quatre chemins** : montée puis descente puis même étage (5 étages parcourus, 3 arrêts), un étage
inexistant refusé au milieu (8 étages, **2 arrêts sur 3**), et l'aller-retour complet 1 → 5 → 1 → 5
(**12 étages parcourus**). Les noms d'étages affichés sont les bons dans tous les cas.
