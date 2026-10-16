# 📱 Quiz de la semaine n°5 — Le plateau se souvient

**Pour ceux qui n'ont pas d'ordinateur : ils le font À LA PLACE de l'exercice
« Le Coffre-Fort ».** Les questions racontent **le même plateau** que l'exercice — samedi, tout le
monde parlera de la même chose.

| | |
|---|---|
| **Quand l'envoyer** | **le mercredi 21 octobre**, après la séance du samedi 17 octobre |
| **Le script** | [`quiz-semaine.gs`](quiz-semaine.gs) — à coller dans [script.google.com](https://script.google.com) |
| **Format** | **15 questions à choix multiples, 15 points** |
| **Correction** | **100 % automatique** — *il n'y a aucun corrigé à coller à la main* |
| **Durée** | 20 minutes depuis un téléphone |

## Ce qu'il vérifie

| Partie | Questions | Ce qu'elle vérifie |
|---|---|---|
| **A** — Lire une liste | 5 | `equipe[0]`, `equipe[2]`, l'`IndexError`, remplacer un élément, compter les éléments |
| **B** — L'indice et la pose | 5 | `case - 1`, où tombe le X, et le piège du `plateau[case]` **sans erreur rouge** |
| **C** — Le plateau du jeu | 5 | pourquoi les guillemets, l'ordre poser → afficher, et la case libre |

**La question 9 est la plus importante.** `plateau[case] = "X"` sans le `- 1` **ne déclenche
aucune erreur** : le X se pose simplement à côté. C'est le bug qu'ils rencontreront tous, et le seul
moyen de le voir, c'est de le savoir.

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

Voici le travail de la semaine pour votre enfant s'il n'a pas
d'ordinateur à la maison : un quiz de 15 questions, depuis un
téléphone. Comptez 20 minutes.

Les questions portent sur ce que nous avons appris samedi : la LISTE,
qui permet enfin à notre jeu de se souvenir des coups joués.

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
