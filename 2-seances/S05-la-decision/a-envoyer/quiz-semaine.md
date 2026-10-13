# 📱 Quiz de la semaine — pour ceux qui n'ont pas d'ordinateur

**Ils le font À LA PLACE de l'exercice « Le Nombre Secret ».** Un téléphone suffit, comptez **20 minutes**.

| | |
|---|---|
| **Le script** | [`quiz-semaine.gs`](quiz-semaine.gs) — à coller dans script.google.com |
| **Format** | **15 questions à choix multiples, 15 points** |
| **Correction** | **100 % automatique** — *il n'y a aucun corrigé à coller à la main* |

> **C'est la nouveauté par rapport aux tests précédents :** aucune question à réponse libre, donc
> **la corvée des 4 minutes disparaît**. Vous collez, vous exécutez, vous réglez la publication des
> notes, et c'est fini.

## Il raconte le même jeu

Les questions mettent en scène **Le Nombre Secret** : le joueur cache un nombre, l'autre a trois essais,
le programme répond « plus grand » ou « plus petit ». Les enfants sans ordinateur **pensent donc le même
jeu** que les autres — ils ne le tapent simplement pas. Samedi, tout le monde parlera de la même chose.

| Partie | Questions | Ce qu'elle vérifie |
|---|---|---|
| **A** — Texte ou nombre | 4 | `"3" + "4"`, `input` qui rend du texte, la ligne `int()`, le `str()` oublié |
| **B** — Le compteur | 3 | `points = points - 20`, la ligne qui ajoute 1, **où placer `points = 100`** |
| **C** — Comparer et décider | 4 | `7 > 10`, les **trois `if`** du jeu, le piège `=` / `==` |
| **D** — Le décalage | 4 | `IndentationError`, le `print` hors du `if`, le `else` qui se déclenche |

**La question 13 est la plus importante de tout le quiz.** C'est le bug du jeu : `points = points - 20`
collée à gauche, hors du `if`. Le joueur **perd des points même quand il gagne**. Celui qui répond juste
à celle-là a compris l'indentation.

## Les trois réglages à faire (les mêmes que d'habitude)

1. **[script.google.com](https://script.google.com)** → Nouveau projet → coller le `.gs` → **▶ Exécuter**.
2. 🔴 **⚙ Paramètres → Questionnaires** : « Publier les notes » sur **Immédiatement après chaque envoi**,
   et cochez **les trois cases** de « Le participant peut voir ».
3. **Recette :** répondez vous-même — le bouton **« Afficher le score »** doit apparaître.

## Le message aux parents

```
Bonjour, et que la paix soit avec vous.

Si votre enfant n'a pas d'ordinateur à la maison, voici son travail de
la semaine : un quiz de 15 questions, à faire depuis un téléphone.
Comptez 20 minutes.

Les questions racontent le jeu que les autres enfants programment cette
semaine, « Le Nombre Secret » : il ne tape pas le code, mais il le lit
et il le comprend — c'est tout aussi utile.

Il aura sa note et les explications dès qu'il aura envoyé ses réponses.

👉 LIEN DU QUIZ

Merci pour votre aide, et à samedi 12 h.
AcProKids Coding Camp — Vision Plénitudes Vie
```

---

## Vérification faite

Le script a été **rejoué contre un faux `FormApp`** ([`sources/verifier-formulaire.js`](sources/verifier-formulaire.js)) :
15 questions, 15 points, aucune anomalie, et la bonne réponse tombe **4 fois en position 1, 4 fois en 2,
3 fois en 3 et 4 fois en 4**, jamais deux fois de suite au même endroit.

**Les 15 réponses ont été exécutées en Python** : les affichages (`60`, `grand puis fini`, `80`,
`Perdu...`) et les types d'erreur (`TypeError` ×2, `SyntaxError`, `IndentationError`) sont conformes.
