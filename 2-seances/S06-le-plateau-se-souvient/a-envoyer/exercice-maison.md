# 🔐🚢 Exercice de maison — deux niveaux au choix

**Pour les enfants qui ont un ordinateur à la maison.** À envoyer **le mercredi 21 octobre**,
à rendre **samedi 24**. Comptez **45 min à 1 h** pour l'un comme pour l'autre.

**Les deux révisent exactement les mêmes notions, avec exactement la même boîte à outils.**
On envoie **l'un ou l'autre, jamais les deux** : un seul exercice par élève.

| | 🔐 **LE COFFRE-FORT** *(pour tous)* | 🚢 **LA BATAILLE NAVALE** *(renforcé)* |
|---|---|---|
| **Pour qui** | **tout le monde** | ceux qui finissent vite, ou qui ont déjà fait le premier |
| **Ce que c'est** | 5 tiroirs, **1** trésor, **2** essais | 8 cases, **3** bateaux, **4** tirs |
| **Ce qu'il y a en plus** | — | **la boîte témoin**, trois `if` indépendants, **deux** compteurs, **deux** verdicts |
| **L'exercice, en images** | [page 1](exercice-maison-le-coffre-fort-1.png) · [page 2](exercice-maison-le-coffre-fort-2.png) | [page 1](exercice-maison-la-bataille-navale-1.png) · [page 2](exercice-maison-la-bataille-navale-2.png) |
| **…et en PDF** | [`…le-coffre-fort.pdf`](exercice-maison-le-coffre-fort.pdf) | [`…la-bataille-navale.pdf`](exercice-maison-la-bataille-navale.pdf) |
| **La correction** | [p. 1](correction-le-coffre-fort-1.png) · [p. 2](correction-le-coffre-fort-2.png) · [PDF](correction-le-coffre-fort.pdf) · [`.py`](correction-coffre-fort.py) | [p. 1](correction-la-bataille-navale-1.png) · [p. 2](correction-la-bataille-navale-2.png) · [PDF](correction-la-bataille-navale.pdf) · [`.py`](correction-bataille-navale.py) |
| **Pour ceux sans ordinateur** | le **[quiz de la semaine n°5](quiz-semaine.md)**, à la place | — |

> **La correction ne part qu'après** le retour des copies.

---

## 🚢 La version renforcée, en deux mots

**Aucune notion nouvelle** — c'est tout l'intérêt. Ce qui change, c'est **l'assemblage** :

| Ce qui est plus dur | Pourquoi ça fait progresser |
|---|---|
| **Trois** valeurs cachées au lieu d'une | il faut **trois `if` indépendants**, collés à gauche l'un sous l'autre — et comprendre que Python les lit **tous les trois** |
| **La boîte témoin** `touche = 0` / `touche = 1` | une variable qui **retient ce qui vient de se passer**, pour décider après. C'est exactement l'idée de la boîte `gagnant` de la séance 11 |
| **Deux** compteurs en parallèle | `score` mesure l'adresse, `touches` dit si la mission est remplie : deux chiffres qui ne disent pas la même chose |
| **Deux** verdicts séparés à la fin | deux `if` / `else` l'un **sous** l'autre, pas l'un **dans** l'autre |
| 8 cases au lieu de 5, 4 tirs au lieu de 2 | plus de recopie — et c'est voulu : c'est ce qui rendra la boucle désirable en séance 10 |

> **Le piège qu'on vient chercher :** si l'élève écrit `touche = 0` **une seule fois tout en haut**
> au lieu de le remettre à zéro dans chaque bloc, il devient amiral **sans rien avoir coulé**.
> C'est le plus bel exemple de bug silencieux qu'on puisse leur offrir à ce stade.
> **Ne le lui dites pas : faites-lui jouer une partie, et laissez-le constater.**
> La feuille le prévient — mais en l'invitant à l'essayer exprès.

---

## 🔐 Le Coffre-Fort — ce que c'est

Un coffre à **cinq tiroirs**. Joueur 2 cache un trésor, joueur 1 a **deux essais**, et le programme
**garde la trace** des tiroirs ouverts : `X` pour un tiroir vide, `T` pour le trésor.
Score de départ 50, **−20 par tiroir vide**.

**Pourquoi ce jeu et pas un autre :** c'est **le plateau du XO en plus petit**. Une liste, un indice
`−1`, une écriture dans la liste, un affichage qui change. Quand ils reviendront au jeu samedi, ils
auront déjà écrit tout ça — avec des tiroirs au lieu de cases.

## Ce que l'exercice fait réviser

**Aucune notion nouvelle.** Tout vient des séances 1 à 6.

| Notion | Où elle sert |
|---|---|
| `print`, le cadre `"=" * 34`, le `+` qui colle | étapes 1 et 4 |
| `input` et la variable | étape 2 |
| **`int()`** pour comparer des nombres | étapes 2 et 4 |
| **`str()`** pour écrire un nombre dans une phrase | étape 6 |
| **le compteur à l'envers** `points = points - 20` | étapes 3 à 5 |
| **`if` / `else`** | étapes 4, 5 et 6 |
| 🆕 **la liste** `tiroirs = [...]` | étape 1 — **la notion de samedi** |
| 🆕 **l'indice** `tiroirs[essai - 1]` | étapes 4 et 5 — **le cœur de l'exercice** |

## Les six choses à regarder dans une copie

1. **La liste a-t-elle cinq cases**, entre **crochets**, séparées par des virgules ?
2. L'affichage utilise-t-il `tiroirs[0]` à `tiroirs[4]` — et pas `[1]` à `[5]` ?
3. **Le `- 1` est-il présent** dans `tiroirs[essai - 1]` ? *(c'est la faute n° 1, et elle est normale)*
4. `points = 50` est-il **avant** les essais, et **une seule fois** ?
5. `points = points - 20` est-il **dans le `else`**, donc décalé ?
6. Les `str()` sont-ils là dans le verdict ?

> **Le bug le plus instructif :** `tiroirs[essai]` au lieu de `tiroirs[essai - 1]`. **Python ne dit rien**
> — la marque se pose simplement à côté. C'est exactement le bug qu'ils auront dans le jeu XO.
> **Faites-le-leur découvrir en jouant**, pas en relisant.

## Le bonus ⭐⭐ : le tiroir déjà ouvert

Le second bonus demande de refuser un tiroir déjà ouvert, en vérifiant qu'il **contient encore son
numéro** : `if tiroirs[essai - 1] == str(essai):`.

**C'est mot pour mot la leçon de la séance 7.** L'élève qui le réussit arrive samedi avec une séance
d'avance : **dites-le devant la classe**, et demandez-lui de l'expliquer lui-même au tableau. C'est
le meilleur démarrage possible pour la séance 7.

## Le message aux parents

```
Bonjour, et que la paix soit avec vous.

Voici un exercice pour les enfants qui ont un ordinateur à la maison.
Votre enfant va programmer un jeu : « Le Coffre-Fort ». L'un cache un
trésor dans un des cinq tiroirs, l'autre a deux essais pour le
trouver, et le programme marque les tiroirs déjà ouverts.

Toutes les instructions sont sur les deux images, étape par étape.
Comptez environ une heure. Ce n'est pas noté : c'est pour s'entraîner.

Et quand ça marchera, jouez une partie avec lui. C'est le meilleur
moment de l'exercice.

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

[`correction-coffre-fort.py`](correction-coffre-fort.py) **a été exécuté** sur ses deux chemins :
trésor trouvé au 1ᵉʳ essai (**30 / 50**, « PILLEUR DE COFFRE-FORT ! ») et jamais trouvé
(**10 / 50**, « Le coffre a resiste... »). Les marques tombent dans les bons tiroirs.

[`correction-bataille-navale.py`](correction-bataille-navale.py) **a été exécuté sur quatre
chemins** : flotte coulée (**80**, « AMIRAL »), deux bateaux (**40**), un seul (**0**) et aucun
(**−40**). Les X et les o tombent dans les bonnes cases, et les deux verdicts se déclenchent
indépendamment.
