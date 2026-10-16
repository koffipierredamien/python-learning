# 📱 Quiz de la semaine n°9 — Le jeu sait qui gagne

**Cette semaine, le quiz est pour TOUT LE MONDE.** Pas d'exercice de maison : samedi
28 novembre c'est le **TP n°3 et le tournoi**, et chacun doit venir avec **son jeu qui marche**.
Le vrai travail de la semaine, c'est ça.

| | |
|---|---|
| **Quand l'envoyer** | **le mercredi 25 novembre**, après la séance du samedi 21 novembre |
| **Le script** | [`quiz-semaine.gs`](quiz-semaine.gs) — à coller dans [script.google.com](https://script.google.com) |
| **Format** | **15 questions à choix multiples, 15 points** |
| **Correction** | **100 % automatique** — *il n'y a aucun corrigé à coller à la main* |
| **Durée** | 20 minutes depuis un téléphone |

## Ce qu'il vérifie

| Partie | Questions | Ce qu'elle vérifie |
|---|---|---|
| **A** — Gagner | 6 | les **8 lignes gagnantes**, et pourquoi trois cases pareilles ne suffisent pas toujours |
| **B** — La boîte `gagnant` | 5 | pourquoi on la crée **vide**, **avant** la boucle, et une seule fois |
| **C** — Ton jeu | 4 | `while tour < 9 and gagnant == ""` : **deux raisons de s'arrêter** |

**La question sur `gagnant = ""` est le cœur du quiz.** Une boîte vide qui attend, créée avant
la boucle : c'est l'idée la plus abstraite des deux mois. Celui qui sait dire *pourquoi avant* a tout compris.

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

Les questions portent sur la séance de samedi : notre jeu sait
maintenant dire QUI A GAGNÉ, et il s'arrête tout seul.

Samedi 28 novembre, c'est le tournoi de classe : les enfants joueront
aux jeux qu'ils ont eux-mêmes programmés. Qu'il vienne avec le sien.

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
