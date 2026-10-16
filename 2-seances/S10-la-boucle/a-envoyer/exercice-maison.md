# 🥤 Exercice de maison — LE DISTRIBUTEUR DE LA RÉCRÉ

**Pour les enfants qui ont un ordinateur à la maison.** À envoyer **le mercredi 18 novembre**,
à rendre **samedi 21**. Comptez **45 min à 1 h**.

| | |
|---|---|
| **L'exercice, en images** | [page 1](exercice-maison-le-distributeur-1.png) · [page 2](exercice-maison-le-distributeur-2.png) |
| **…et en PDF, pour imprimer** | [`exercice-maison-le-distributeur.pdf`](exercice-maison-le-distributeur.pdf) |
| **La correction** | [page 1](correction-le-distributeur-1.png) · [page 2](correction-le-distributeur-2.png) · [PDF](correction-le-distributeur.pdf) · [`.py`](correction-distributeur.py) |
| **Pour ceux qui n'ont pas d'ordinateur** | le **[quiz de la semaine n°8](quiz-semaine.md)**, à la place |

> **La correction ne part qu'après** le retour des copies.

---

## Ce que c'est

Une machine à **quatre produits**, un porte-monnaie, et **zéro bloc recopié**. Tant qu'il reste de
quoi payer le moins cher **et** qu'il reste un produit, la machine réaffiche son menu toute seule.
À la fin, elle imprime un ticket.

**C'est le premier exercice de l'année plus court que le précédent.** Dites-le-leur : *« la semaine
dernière, quatre visiteurs = quatre blocs. Cette semaine, quatre achats = un seul bloc. »*
**C'est là qu'ils sentent qu'ils progressent** — pas quand on le leur dit, quand ils le comptent.

> **La machine, c'est le jeu XO.** Une liste qu'on modifie, un compteur de tours, une condition de
> coup valide, un refus qui ne consomme pas de tour, et une boucle autour. **Exactement** le code
> officiel de samedi, avec des chips à la place des X.

## Ce que l'exercice fait réviser

**Aucune notion nouvelle.**

| Notion | Où elle sert |
|---|---|
| `print`, `input`, le `+`, `int()`, `str()` | étapes 1, 2 et 6 |
| **la liste** et l'indice `- 1` | étapes 1, 4 et 5 |
| **deux listes qui vont ensemble** (même indice) | étape 1 — *nouvel usage, notion connue* |
| **`and`** (quatre conditions d'un coup) | étape 4 |
| **`!=`** | étape 4 |
| **`if` / `else`**, le compteur | étapes 4 à 6 |
| 🆕 **`while`** | étape 3 — **la notion de samedi** |
| 🆕 **dedans / dehors** : le décalage | étapes 3 à 6 — **le vrai enjeu** |

## Les six choses à regarder dans une copie

1. Les **deux points** à la fin de la ligne `while` ?
2. **Tout ce qui doit se répéter est-il décalé** sous le `while` ?
3. `argent = argent - prix[choix - 1]` est-il **dans** le `if` qui vend ?
   *(sinon la machine fait payer sans rien donner)*
4. **`achats = achats + 1` est-il là ?** Sans lui : **boucle infinie**.
5. Le `- 1` est-il présent sur **les deux** listes ?
6. **Le ticket est-il dehors de la boucle**, collé à gauche ? *(s'il s'affiche après chaque achat,
   c'est qu'il est resté dedans — et c'est le test le plus rapide à faire en regardant l'écran)*

## La boucle infinie : qu'elle arrive, et traitez-la en public

Un ou deux élèves arriveront samedi avec une boucle qui ne s'arrête pas. **Ne corrigez pas tout de
suite.** Lancez-la, laissez défiler dix secondes, faites **Ctrl + C** devant tout le monde, puis
demandez à la classe : *« qu'est-ce qui ne change jamais ? »*

C'est la leçon la plus rentable des deux mois, et elle les vaccine pour toute l'année :
**une boucle s'arrête parce que quelque chose avance.**

## Le bonus ⭐⭐ : un cinquième produit

Ajouter `"Biscuit"` et `50` à la fin des deux listes, une ligne de menu, remplacer les 4 par des 5.
**Faites-leur compter les lignes changées** (quatre), puis demandez combien il en aurait fallu dans
la version « recopiée » de la semaine dernière. **Voilà ce que la boucle leur a donné**, en chiffres.

## Le message aux parents

```
Bonjour, et que la paix soit avec vous.

Voici un exercice pour les enfants qui ont un ordinateur à la maison.
Votre enfant va programmer « Le Distributeur de la récré » : une
machine à quatre produits, qui redemande ce qu'on veut acheter tant
qu'il reste de l'argent, et qui imprime un ticket à la fin.

Toutes les instructions sont sur les deux images, étape par étape.
Comptez environ une heure. Ce n'est pas noté : c'est pour s'entraîner.

Une précision utile : si le programme se met à défiler sans s'arrêter,
ce n'est pas grave. Il faut appuyer sur Ctrl et C en même temps pour
l'arrêter. Cela arrive à tout le monde, et cela s'explique samedi.

Qu'il nous envoie ensuite une photo de son écran — nous en
reparlerons samedi. S'il n'y arrive pas entièrement, qu'il envoie
quand même ce qu'il a fait : c'est là-dessus que nous travaillerons.

👉 LES DEUX IMAGES DE L'EXERCICE

Merci pour votre aide, et à samedi 12 h.
AcProKids Coding Camp — Vision Plénitudes Vie
```

> **Pour les enfants sans ordinateur :** ils font le [quiz de la semaine](quiz-semaine.md), et
> l'exercice sera refait **en classe** sur les postes. Rien de tout cela n'entre dans une note.

---

## Vérification faite

Le corrigé [`correction-distributeur.py`](correction-distributeur.py) **a été exécuté**, sur les trois
chemins : machine vidée (700 F dépensés → **4 / 4**, « TU AS VIDE LA MACHINE »), panne d'argent
(**2 / 4**, 0 F restant) et refus d'un achat trop cher (la machine **redemande sans rien prélever**).
