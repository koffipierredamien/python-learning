# 📱 Quiz de la semaine n°8 — Le jeu tourne tout seul

**Pour ceux qui n'ont pas d'ordinateur : ils le font À LA PLACE de l'exercice
« Le Distributeur de la récré ».** Mêmes notions, même semaine.

| | |
|---|---|
| **Quand l'envoyer** | **le mercredi 18 novembre**, après la séance du samedi 14 novembre |
| **Le script** | [`quiz-semaine.gs`](quiz-semaine.gs) — à coller dans [script.google.com](https://script.google.com) |
| **Format** | **15 questions à choix multiples, 15 points** |
| **Correction** | **100 % automatique** — *il n'y a aucun corrigé à coller à la main* |
| **Durée** | 20 minutes depuis un téléphone |

## Ce qu'il vérifie

| Partie | Questions | Ce qu'elle vérifie |
|---|---|---|
| **A** — La boucle | 6 | combien de tours, quand elle s'arrête, et **la boucle infinie** |
| **B** — Dedans ou dehors ? | 5 | le décalage décide de tout : ce qui se répète et ce qui ne se répète pas |
| **C** — Le jeu | 4 | les neuf tours, l'alternance des joueurs, et pourquoi `tour = tour + 1` est **dans le `if`** |

**La question sur la boucle infinie est la plus utile de l'année.** Un `while` dont le compteur
n'avance jamais ne s'arrête jamais — et la seule porte de sortie est **Ctrl + C**. Qu'ils le sachent
avant que ça leur arrive à la maison, un dimanche soir.

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

Les questions portent sur la grande nouveauté de samedi : la boucle.
Notre jeu joue maintenant ses neuf tours tout seul — et le programme
est plus COURT qu'avant.

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
