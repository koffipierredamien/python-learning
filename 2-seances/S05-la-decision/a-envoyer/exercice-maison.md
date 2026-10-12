# 🎮 Exercice de maison — « Le Quiz des Geeks »

**Pour les enfants qui ont un ordinateur à la maison.** Ils écrivent un vrai jeu : trois questions, un
score qui monte, et un verdict à la fin. Comptez **45 minutes à 1 heure**.

| | |
|---|---|
| **À envoyer** | [`exercice-maison-le-quiz-des-geeks.png`](exercice-maison-le-quiz-des-geeks.png) — **une seule image**, lisible sur un téléphone |
| **La correction** | [`correction-le-quiz-des-geeks.png`](correction-le-quiz-des-geeks.png) · le code seul : [`correction-quiz-des-geeks.py`](correction-quiz-des-geeks.py) |
| **À ne pas envoyer avec l'exercice** | la correction, évidemment — elle part **après** le retour des copies |

## Ce que l'exercice fait réviser

Tout, et rien d'autre. **Aucune notion nouvelle.**

| Notion | Où elle sert |
|---|---|
| `print`, le cadre `"=" * 35` | étape 1 |
| la variable, `input`, le `+` | étape 1 |
| **le compteur** `score = score + 1` | étapes 2 à 5 |
| **`int()`** pour comparer un nombre | étapes 3 et 5 |
| **`str()`** pour coller un nombre dans une phrase | étape 6 |
| **`==`** et **`>`**, et le `if` / `else` | étapes 3 à 6 |

Les **deux bonus** (le reste à faire pour le sans-faute, la question d'âge) n'ajoutent rien de neuf non
plus : ils recombinent.

## Les cinq choses à regarder dans une copie

1. **`score = 0` est-il avant les questions, et une seule fois ?**
2. **`int()` est-il là aux questions 1 et 3** (des nombres) **et absent à la question 2** (du texte) ?
3. **Le `==` est-il doublé** dans les `if` ? Un seul `=` donne un `SyntaxError`.
4. **Les 4 espaces de décalage** sont-ils là sous chaque `if` et chaque `else` ? *C'est l'erreur n°1.*
5. **`str(score)`** est-il présent dans la phrase du bilan ? Sans lui : `TypeError`.

> **La vraie question à poser à l'enfant :** *« lance-le en te trompant exprès — est-ce que le `else` se
> déclenche ? »* Un `if` qu'on n'a pas testé dans ses deux cas n'est pas testé.

## Le message aux parents

```
Bonjour, et que la paix soit avec vous.

Voici un exercice pour les enfants qui ont un ordinateur à la maison.
Il reprend tout ce que nous avons appris depuis le premier samedi, et
cette fois votre enfant écrit un vrai petit jeu : un quiz de trois
questions, avec un score et un verdict à la fin.

Toutes les instructions sont sur l'image, étape par étape. Comptez
environ une heure. Ce n'est pas noté : c'est pour s'entraîner.

Quand ça marche, qu'il nous envoie une photo de son écran — nous en
reparlerons samedi.

Et s'il n'y arrive pas entièrement, ce n'est pas grave : qu'il envoie
quand même ce qu'il a fait. C'est là-dessus que nous travaillerons.

👉 L'IMAGE DE L'EXERCICE

Merci pour votre aide, et à samedi 12 h.
AcProKids Coding Camp — Vision Plénitudes Vie
```

> **Pour les enfants sans ordinateur :** ils ne sont pas pénalisés. L'exercice sera refait **en classe**
> sur les postes, et il n'entre dans aucune note.
