# 🎮 Exercice de maison — deux versions au choix

**Pour les enfants qui ont un ordinateur à la maison.** Comptez **45 min à 1 h**.
Les deux exercices révisent **exactement les mêmes notions** — on envoie **l'un ou l'autre**, pas les deux.

| | 🔢 **LE NOMBRE SECRET** *(recommandé)* | 🎯 **LE QUIZ DES GEEKS** |
|---|---|---|
| **Ce que c'est** | Un **vrai jeu à deux joueurs**, qu'on rejoue | Un quiz de 3 questions, qu'on joue une fois |
| **On y joue en famille ?** | **Oui** — c'est tout l'intérêt | Non |
| **L'exercice, en images** | [page 1](exercice-maison-le-nombre-secret-1.png) · [page 2](exercice-maison-le-nombre-secret-2.png) | [page 1](exercice-maison-le-quiz-des-geeks-1.png) · [page 2](exercice-maison-le-quiz-des-geeks-2.png) |
| **…et en PDF, pour imprimer** | [`exercice-maison-le-nombre-secret.pdf`](exercice-maison-le-nombre-secret.pdf) | [`exercice-maison-le-quiz-des-geeks.pdf`](exercice-maison-le-quiz-des-geeks.pdf) |
| **La correction** | [page 1](correction-le-nombre-secret-1.png) · [page 2](correction-le-nombre-secret-2.png) · [PDF](correction-le-nombre-secret.pdf) · [`.py`](correction-nombre-secret.py) | [page 1](correction-le-quiz-des-geeks-1.png) · [page 2](correction-le-quiz-des-geeks-2.png) · [PDF](correction-le-quiz-des-geeks.pdf) · [`.py`](correction-quiz-des-geeks.py) |

> **Pourquoi *Le Nombre Secret* est meilleur :** l'enfant ne répond pas à des questions, **il fait jouer
> quelqu'un**. Le programme réagit (« plus grand ! », « plus petit ! »), il y a un score, et on a envie de
> refaire une partie. C'est la différence entre un exercice et un jeu.

> **La correction ne part qu'après** le retour des copies.

### 📱 Et pour ceux qui n'ont pas d'ordinateur

Ils font le **[quiz de la semaine](quiz-semaine.md)** à la place : 15 questions à choix multiples sur
**le même jeu**, depuis un téléphone, **corrigé à 100 % automatiquement**. Personne n'est laissé de côté,
et samedi tout le monde parlera de la même chose.

### 🖨️ Deux images, ou un PDF

Chaque exercice tient maintenant sur **deux pages A4** : envoyez **les deux images** par message, ou
**le PDF** à ceux qui veulent l'imprimer. Les deux contiennent exactement la même chose.

---

## Ce que l'exercice fait réviser

Tout, et rien d'autre. **Aucune notion nouvelle** — sauf le bonus ⭐⭐ final, signalé comme tel.

| Notion | Où elle sert dans *Le Nombre Secret* |
|---|---|
| `print`, le cadre `"=" * 33` | étape 1 |
| la variable, `input`, le `+` | étapes 1 et 2 |
| **`int()`** pour comparer des nombres | étapes 2 et 4 |
| **`str()`** pour écrire un nombre dans une phrase | étape 6 |
| **le compteur, à l'envers** : `points = points - 20` | étapes 3 à 5 |
| **`<`, `>`, `==`** et le `if` | étape 4 — **le cœur du jeu** |
| `if` / `else` | étape 6, le verdict |

**Le `if` sans `else`** apparaît ici pour la première fois dans un exercice. Ce n'est pas une notion
nouvelle (ils l'ont vu au quiz flash) : c'est un `if` tout seul, en plus simple.

## Les cinq choses à regarder dans une copie

1. **`points = 100` est-il avant les essais, et une seule fois ?**
2. **Les deux lignes `essai = input(…)` puis `essai = int(essai)`** sont-elles là **à chaque essai** ?
3. **Les trois `if`** (`<`, `>`, `==`) sont-ils présents à chaque essai ?
4. **Le bug le plus intéressant :** `points = points - 20` **collée à gauche**, donc hors du `if` —
   le joueur perd alors des points **même quand il gagne**. À lui faire découvrir **en jouant**.
5. **`str(secret)` et `str(points)`** sont-ils là dans le verdict ?

> **Ce que ce jeu prépare, sans le dire :** l'élève recopie **trois fois** le même bloc. C'est exactement
> l'agacement dont naîtra la boucle `while`. Si un enfant demande *« on est obligés de tout recopier ? »*,
> la réponse est : **« non — et c'est ce qu'on apprendra bientôt. »**

## Le bonus ⭐⭐ : les deux lignes magiques

Le dernier bonus donne `import random` / `random.randint(1, 50)` **tout fait**, pour jouer en solo.
C'est **la seule chose nouvelle** de la feuille, et elle est écrite noir sur blanc comme telle.
**Si vous préférez ne rien introduire du tout, dites-le-moi : je retire ce bonus en deux minutes.**

## Le message aux parents

```
Bonjour, et que la paix soit avec vous.

Voici un exercice pour les enfants qui ont un ordinateur à la maison.
Votre enfant va programmer un vrai jeu : « Le Nombre Secret ». L'un
cache un nombre, l'autre a trois essais pour le trouver, et le
programme répond « plus grand » ou « plus petit » à chaque fois.

Toutes les instructions sont sur l'image, étape par étape. Comptez
environ une heure. Ce n'est pas noté : c'est pour s'entraîner.

Et quand ça marchera, jouez une partie avec lui. C'est le meilleur
moment de l'exercice.

Qu'il nous envoie ensuite une photo de son écran — nous en reparlerons
samedi. S'il n'y arrive pas entièrement, qu'il envoie quand même ce
qu'il a fait : c'est là-dessus que nous travaillerons.

👉 L'IMAGE DE L'EXERCICE

Merci pour votre aide, et à samedi 12 h.
AcProKids Coding Camp — Vision Plénitudes Vie
```

> **Pour les enfants sans ordinateur :** ils font le [quiz de la semaine](quiz-semaine.md), et l'exercice
> sera refait **en classe** sur les postes. Rien de tout cela n'entre dans une note.
