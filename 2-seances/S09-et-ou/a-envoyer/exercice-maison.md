# 🕶️ Exercice de maison — LA SOIRÉE DU CLUB GEEK

**Pour les enfants qui ont un ordinateur à la maison.** À envoyer **le mercredi 11 novembre**,
à rendre **samedi 14**. Comptez **45 min à 1 h**.

| | |
|---|---|
| **L'exercice, en images** | [page 1](exercice-maison-la-soiree-du-club-1.png) · [page 2](exercice-maison-la-soiree-du-club-2.png) |
| **…et en PDF, pour imprimer** | [`exercice-maison-la-soiree-du-club.pdf`](exercice-maison-la-soiree-du-club.pdf) |
| **La correction** | [page 1](correction-la-soiree-du-club-1.png) · [page 2](correction-la-soiree-du-club-2.png) · [PDF](correction-la-soiree-du-club.pdf) · [`.py`](correction-videur-club.py) |
| **Pour ceux qui n'ont pas d'ordinateur** | le **[quiz de la semaine n°7](quiz-semaine.md)**, à la place |

> **La correction ne part qu'après** le retour des copies.

---

## Ce que c'est

**La suite directe de l'atelier de 12 h 40.** En classe, le videur posait **une question** à **une
personne**. À la maison, il tient **toute la soirée** : **trois fauteuils**, **quatre visiteurs**,
une règle de club qui combine `and` et `or`, et un rapport de fin de soirée.

**Pourquoi ce prolongement et pas un nouveau sujet :** ils partent d'un code qu'ils ont déjà écrit et
qui marche. Toute l'heure passe sur la **vraie** difficulté — combiner les conditions, tenir un
compteur, ranger quelqu'un dans une liste — et pas à relire un énoncé.

> **Les trois fauteuils, c'est le plateau.** Une liste, un compteur qui avance, une condition qui
> décide : samedi prochain, la boucle `while` s'enroulera autour d'exactement ces trois choses.

## Ce que l'exercice fait réviser

**Aucune notion nouvelle.**

| Notion | Où elle sert |
|---|---|
| `print`, `input`, le `+`, `int()`, `str()` | étapes 1, 2 et 6 |
| **la liste** et l'écriture dedans | étapes 1 et 4 |
| **le `if` dans le `if`** *(séance 7)* | étapes 3 et 4 |
| **le compteur qui monte** `entres = entres + 1` | étape 4 |
| 🆕 **`and`** — il faut tout | étape 4 — **la notion de samedi** |
| 🆕 **`or`** — il suffit d'un | étape 4, pour le VIP |
| 🆕 **les parenthèses** `(A and B) or C` | étape 4 |

## Les sept choses à regarder dans une copie

1. Y a-t-il un `and` entre **chaque** question ? *(une virgule à la place → `SyntaxError`)*
2. Les parenthèses encadrent-elles bien le groupe **âge + séances** ?
3. Le `or` est-il **dehors** des parenthèses ?
4. `entres = 0` est-il avant le premier visiteur, et **une seule fois** ?
5. `entres = entres + 1` est-il **dans** le `if` qui accepte ?
6. **`fauteuils[entres]` — sans le `- 1`.** 👉 **C'est la faute n° 1, et elle est normale :** depuis
   trois séances ils écrivent `case - 1`. Ici le compteur part de **0**, il tombe déjà sur le bon
   fauteuil. **Expliquez la différence au tableau, pour toute la classe.**
7. Le rapport final est-il **dehors** des blocs, collé à gauche ?

## Le chiffre à leur demander samedi

L'étape 5 leur demande de **compter les lignes qu'ils ont recopiées** et de noter le nombre.
**Réclamez ce chiffre en ouverture de la séance 10**, écrivez-le au tableau, et écrivez la boucle
juste en dessous. C'est le meilleur argument que vous aurez pour `while` — et il vient d'eux.

## Le bonus ⭐⭐ : « déjà entré ! »

`if nom == fauteuils[0] or nom == fauteuils[1] or nom == fauteuils[2]:` — c'est **le test de la case
occupée du jeu XO**, avec des fauteuils à la place des cases. Faites le rapprochement à voix haute :
*« tu viens de réécrire le cœur de notre jeu. »*

## Le message aux parents

```
Bonjour, et que la paix soit avec vous.

Voici un exercice pour les enfants qui ont un ordinateur à la maison.
Votre enfant va programmer « La Soirée du Club Geek » : il tient la
porte d'un club de trois places, et décide qui entre et qui n'entre
pas, selon l'âge, l'assiduité, et un code VIP.

Toutes les instructions sont sur les deux images, étape par étape.
Comptez environ une heure. Ce n'est pas noté : c'est pour s'entraîner.

Faites-vous refuser à l'entrée, puis entrez avec le code VIP : c'est
le meilleur moment de l'exercice.

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

Le corrigé [`correction-videur-club.py`](correction-videur-club.py) **a été exécuté**, sur les deux
chemins : une soirée mélangée (un accepté, un refusé, un VIP de 25 ans accepté, un quatrième accepté
→ **3 / 3**) et une soirée de quatre visiteurs valables (le quatrième lit bien **« Le club est
COMPLET »**). Les noms tombent dans les bons fauteuils.
