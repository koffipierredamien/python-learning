# 📱 Quiz de la semaine n°6 — On ne joue pas deux fois au même endroit

**Cette semaine, le quiz est pour TOUT LE MONDE.** Il n'y a pas d'exercice de maison :
samedi 31 octobre, c'est le **TP n°2**, et il vaut mieux qu'ils arrivent frais. Vingt minutes de quiz,
et on se retrouve.

| | |
|---|---|
| **Quand l'envoyer** | **le mercredi 28 octobre**, après la séance du samedi 24 octobre |
| **Le script** | [`quiz-semaine.gs`](quiz-semaine.gs) — à coller dans [script.google.com](https://script.google.com) |
| **Format** | **15 questions à choix multiples, 15 points** |
| **Correction** | **100 % automatique** — *il n'y a aucun corrigé à coller à la main* |
| **Durée** | 20 minutes depuis un téléphone |

## Ce qu'il vérifie

| Partie | Questions | Ce qu'elle vérifie |
|---|---|---|
| **A** — La case libre | 5 | comment le programme sait qu'une case est prise : **elle ne contient plus son numéro** |
| **B** — Le `if` dans le `if` | 5 | **4 espaces puis 8**, quel `else` répond à quel `if`, et ce qui se passe quand on en oublie un |
| **C** — Le jeu complet | 5 | les quatre cas d'un coup joué, et **le bug du zéro** qu'ils ont trouvé eux-mêmes |

**La question du zéro est la plus retorse du quiz — et la bonne réponse surprendra même les adultes.**
Dans le jeu **de la séance 6**, taper `0` posait le symbole dans la **case 9** (`0 - 1` vaut `-1`, et
`-1` désigne le **dernier** élément). Mais dans le jeu **de samedi dernier**, le test de la case libre
le **refuse** — en annonçant *« la case 0 est déjà prise »*, ce qui est **faux** : personne n'a jamais
joué la case 0, elle n'existe même pas.

**Le bug n'est donc pas réparé : il est caché, derrière un message qui ment.** C'est exactement ce
qu'on répare à la séance 9 avec `and`. Les élèves qui répondent juste à celle-là arrivent le
7 novembre avec la question déjà posée.

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

Voici le travail de la semaine : un quiz de 15 questions, depuis un
téléphone. Comptez 20 minutes. Cette semaine il est pour tous les
enfants, avec ou sans ordinateur.

Les questions portent sur la séance de samedi : comment notre jeu
refuse une case déjà jouée.

Samedi 31 octobre, ce sera un TP : deux heures pour construire,
en équipe et en autonomie. Qu'il vienne reposé.

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
