# 📱 Quiz de la semaine n°10 — Le bilan des deux mois

**Le quiz-bilan, pour tout le monde.** Il reprend **les sept séances d'octobre et novembre**,
des bases jusqu'au tournoi. C'est aussi **votre instrument de mesure** : les résultats question par
question vous disent exactement ce qu'il faudra reprendre en décembre.

| | |
|---|---|
| **Quand l'envoyer** | **le mercredi 2 décembre**, après la séance du samedi 28 novembre |
| **Le script** | [`quiz-semaine.gs`](quiz-semaine.gs) — à coller dans [script.google.com](https://script.google.com) |
| **Format** | **15 questions à choix multiples, 15 points** |
| **Correction** | **100 % automatique** — *il n'y a aucun corrigé à coller à la main* |
| **Durée** | 20 minutes depuis un téléphone |

## Ce qu'il vérifie

| Partie | Questions | Ce qu'elle vérifie |
|---|---|---|
| **A** — Les bases | 5 | `int()` / `str()`, le compteur, `if` / `else` — ce qu'ils savaient **avant** octobre |
| **B** — Les listes et la boucle | 5 | `case - 1`, `and` / `or`, `while` — **le cœur des deux mois** |
| **C** — Ton jeu, en entier | 5 | du premier `print` au vainqueur : ce que leur programme fait, et pourquoi |

**Lisez les résultats partie par partie, pas élève par élève.** Si la partie B s'effondre, c'est
l'indice `case - 1` qu'il faut reprendre en décembre — pas la motivation des enfants.

## Les trois réglages à faire

1. **[script.google.com](https://script.google.com)** → Nouveau projet → effacer le code présent →
   coller **tout** le `.gs` → **▶ Exécuter** (autoriser à la première utilisation).
   Le journal affiche **le lien à envoyer**.
2. 🔴 **L'ÉTAPE QU'ON OUBLIE.** Ouvrez le formulaire → **⚙ Paramètres → Questionnaires** :
   « Publier les notes » sur **Immédiatement après chaque envoi**, et cochez **les trois cases**
   de « Le participant peut voir ». *Apps Script ne sait pas régler ça : quatre clics, une fois.*
   **Sans ces quatre clics, l'élève n'a ni note ni correction.**
3. **Recette :** répondez vous-même au formulaire. Le bouton **« Afficher le score »**
   doit apparaître, avec la note et les explications.

## Le message à envoyer

```
Bonjour, et que la paix soit avec vous.

Voici le dernier quiz de l'année civile : 15 questions qui reprennent
tout ce que les enfants ont appris en octobre et novembre. Comptez
20 minutes, depuis un téléphone.

En deux mois, ils sont passés d'un programme qui affichait du texte
à un vrai jeu de morpion à deux joueurs, qui sait qui a gagné.
Nous en sommes fiers.

Ce quiz n'est pas une note : c'est pour savoir ce que nous devons
revoir ensemble à la reprise.

Il aura sa note et les explications dès qu'il aura envoyé ses réponses.

👉 LIEN DU QUIZ

Merci pour votre aide, et à samedi 12 h.
AcProKids Coding Camp — Vision Plénitudes Vie
```

---

## Vérification faite

Le script a été **rejoué contre un faux `FormApp`**
([`verifier-formulaire.js`](../../S05-la-decision/a-envoyer/sources/verifier-formulaire.js)) :
**15 questions, 15 points, aucune anomalie.** La bonne réponse n'est **jamais deux fois de suite au
même endroit**, et les quatre positions servent **3 ou 4 fois chacune** : un élève qui répondrait
« toujours B » n'aurait que 3 ou 4 sur 15. **La suite des positions change d'un quiz à l'autre** —
celui qui comparerait le quiz de cette semaine à celui de la semaine dernière n'y gagnerait rien.
