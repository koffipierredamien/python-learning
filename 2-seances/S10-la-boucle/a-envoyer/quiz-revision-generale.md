# 📱 La révision générale, à refaire à la maison

**Le formulaire reprend le diaporama du samedi 14 novembre**, question par question : les **huit
cartes** de la révision, et les **cinq ateliers au clavier** transformés en questions.

> **Pourquoi transformer les ateliers ?** À la maison, personne ne regarde par-dessus l'épaule, et
> Google Forms ne sait pas corriger du code tapé. On ne leur demande donc plus **d'écrire** le
> programme — on leur demande **de dire ce qu'il fait**, ce qui est exactement la compétence que les
> ateliers travaillaient : prédire avant de lancer.

> 🔒 **Le formulaire se suffit à lui-même.** Aucune question ne renvoie à une séance, à un atelier
> ni au projet XO. Les listes sont redonnées à chaque question, les programmes recopiés en entier,
> et **aucune question ne dépend de la précédente**. Conséquences pratiques : on peut le donner
> **à un enfant qui était absent**, le **renvoyer tel quel dans un mois**, et un parent peut le lire
> par-dessus l'épaule sans rien connaître au cours.

| | |
|---|---|
| **Le script** | [`quiz-revision-generale.gs`](quiz-revision-generale.gs) — à coller dans [script.google.com](https://script.google.com) |
| **Format** | **20 questions à choix multiples, 20 points** |
| **Correction** | **100 % automatique** — *il n'y a aucun corrigé à coller à la main* |
| **Durée** | 25 à 30 minutes depuis un téléphone |
| **Pour qui** | **tout le monde, cette fois** — avec ou sans ordinateur |

## Lequel envoyer cette semaine ?

Il y en a deux dans ce dossier, et **on n'envoie qu'un seul**.

| | [Quiz n°8](quiz-semaine.md) | **Cette révision générale** |
|---|---|---|
| **Porte sur** | la boucle `while`, seulement | **tout depuis septembre**, la boucle comprise |
| **Longueur** | 15 questions, 20 min | 20 questions, 30 min |
| **Quand le choisir** | un samedi ordinaire | **après une séance de révision** — donc cette semaine |

👉 **Cette semaine, envoyez la révision générale.** Gardez le quiz n°8 pour un rappel plus tard, ou
pour les élèves qui auraient manqué le 14 novembre.

## Ce qu'il vérifie

| Partie | Questions | Ce qu'elle vérifie |
|---|---|---|
| **A** — Texte ou nombre | 4 | `"7" + "7"`, le piège de `age * 2`, `int("7") + int("7")`, et **comment additionner deux réponses d'`input`** |
| **B** — Les listes | 4 | `equipe[3]`, la copie d'une case dans une autre, le numéro de `huile`, l'`IndexError` |
| **C** — Le décalage | 4 | ce qui est dans le `if` et ce qui n'y est pas, et **comment sortir une ligne du `else` sans en ajouter une** |
| **D** — `and`, `or` | 4 | `age >= 12 and age <= 18`, le refus d'un numéro qui n'existe pas, **et le `or` qui laisse passer un coup interdit** |
| **E** — Répéter | 4 | les 15 lignes recopiées, les trois tours du `while`, la répétition sans fin, `Ctrl + C` |

**Les quatre questions à regarder dans les résultats**, dans cet ordre :

1. **Celle du `or`** (partie D) — c'est la condition du coup valide de leur jeu, posée sans le dire.
   Qui ne l'a pas ne saura pas débugger le sien.
2. **Celle de la ligne à reculer de 4 espaces** (partie C) — la faute n° 1 de leurs copies depuis
   la séance 5.
3. **Celle de `age * 2`** (partie A) — elle sépare ceux qui récitent « input rend du texte » de ceux
   qui l'ont compris.
4. **Celle de la répétition sans fin** (partie E) — c'est la panne qui les attend cette semaine.

## Les trois réglages à faire

1. **[script.google.com](https://script.google.com)** → Nouveau projet → effacer le code présent →
   coller **tout** le `.gs` → **▶ Exécuter** (autoriser à la première utilisation).
   Le journal affiche **le lien à envoyer**.
2. 🔴 **L'ÉTAPE QU'ON OUBLIE.** Formulaire → **⚙ Paramètres → Questionnaires** :
   « Publier les notes » sur **Immédiatement après chaque envoi**, et cochez **les trois cases**
   de « Le participant peut voir ». *Apps Script ne sait pas régler ça : quatre clics, une fois.*
   **Sans ces quatre clics, l'élève n'a ni note ni correction.**
3. **Recette :** répondez vous-même. Le bouton **« Afficher le score »** doit apparaître.

## Le message à envoyer

```
Bonjour, et que la paix soit avec vous.

Voici une révision générale pour votre enfant : 20 questions à faire
depuis un téléphone, comptez une demi-heure. Elle reprend tout ce qui
a été appris depuis le début.

Tout ce qu'il faut pour répondre est écrit dans les questions : il n'a
besoin ni de son cahier, ni d'un ordinateur.

Ce n'est pas une note. Votre enfant aura son score et les explications
dès qu'il aura envoyé ses réponses, et il peut la refaire autant de
fois qu'il veut.

👉 LIEN DU QUIZ

Merci pour votre aide, et à samedi 12 h.
AcProKids Coding Camp — Vision Plénitudes Vie
```

---

## Vérification faite

Le script a été **rejoué contre un faux `FormApp`**
([`verifier-formulaire.js`](../../S05-la-decision/a-envoyer/sources/verifier-formulaire.js)) :
**20 questions, 20 points, aucune anomalie.** La bonne réponse n'est **jamais deux fois de suite au
même endroit**, et les quatre positions servent 4 à 6 fois chacune.

**Aucune question ne renvoie à l'extérieur** : les listes sont redonnées à chaque fois, les deux
programmes des parties C et D sont recopiés en entier dans les deux questions qui les utilisent, et
le message de fin ne cite plus de date.

**Les quatorze réponses calculatoires ont été exécutées en Python** : `"7" + "7"` → `77`,
`"12" * 2` → `1212`, `int("7") + int("7")` → `14`, `equipe[3]` → `D`, la copie → `['A', 'C', 'C', 'D']`,
`sacs[5]` → `IndexError`, le `A puis B`, le `50` inchangé, `11 >= 12 and 11 <= 18` → `False`,
la condition avec `or` → `True` (il pose), avec `and` → `False` (il refuse), et les trois `A` de la boucle.
