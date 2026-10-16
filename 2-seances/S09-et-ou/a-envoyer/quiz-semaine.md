# 📱 Quiz de la semaine n°7 — `and`, `or`, et une seule question

**Pour ceux qui n'ont pas d'ordinateur : ils le font À LA PLACE de l'exercice
« La Soirée du Club Geek ».** Mêmes notions, même semaine.

| | |
|---|---|
| **Quand l'envoyer** | **le mercredi 11 novembre**, après la séance du samedi 7 novembre |
| **Le script** | [`quiz-semaine.gs`](quiz-semaine.gs) — à coller dans [script.google.com](https://script.google.com) |
| **Format** | **15 questions à choix multiples, 15 points** |
| **Correction** | **100 % automatique** — *il n'y a aucun corrigé à coller à la main* |
| **Durée** | 20 minutes depuis un téléphone |

## Ce qu'il vérifie

| Partie | Questions | Ce qu'elle vérifie |
|---|---|---|
| **A** — `and` et `or` | 6 | la table à connaître : `True and False`, `False or True`… et la règle en français |
| **B** — Des conditions utiles | 5 | `age >= 12 and age <= 18`, les parenthèses, et les conditions qu'on écrit pour de vrai |
| **C** — Le jeu | 4 | la condition unique du coup valide, et **le bug du zéro enfin mort** |

**La question clé est celle du zéro réparé.** Ils ont vécu le bug pendant trois semaines ;
cette semaine ils doivent pouvoir dire **quelle partie de la condition le tue** : le `case >= 1`.

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

Les questions portent sur les deux mots appris samedi : « and »
(il faut tout) et « or » (il suffit d'un). Grâce à eux, notre jeu
est devenu deux fois plus court.

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
