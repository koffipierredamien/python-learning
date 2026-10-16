# -*- coding: utf-8 -*-
"""Notices d'accompagnement : quiz-semaine.md (x6) et exercice-maison.md (x3)."""
import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENTETE_QUIZ = u"""# 📱 Quiz de la semaine n°{num} — {titre}

{accroche}

| | |
|---|---|
| **Quand l'envoyer** | **le mercredi {mercredi}**, après la séance du samedi {samedi} |
| **Le script** | [`quiz-semaine.gs`](quiz-semaine.gs) — à coller dans [script.google.com](https://script.google.com) |
| **Format** | **15 questions à choix multiples, 15 points** |
| **Correction** | **100 % automatique** — *il n'y a aucun corrigé à coller à la main* |
| **Durée** | 20 minutes depuis un téléphone |

## Ce qu'il vérifie

| Partie | Questions | Ce qu'elle vérifie |
|---|---|---|
{parties}

{clef}

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

{message}

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
"""

QUIZ = [
 dict(num=5, dossier="S06-le-plateau-se-souvient", mercredi="21 octobre", samedi="17 octobre",
   titre="Le plateau se souvient",
   accroche="**Pour ceux qui n'ont pas d'ordinateur : ils le font À LA PLACE de l'exercice\n« Le Coffre-Fort ».** Les questions racontent **le même plateau** que l'exercice — samedi, tout le\nmonde parlera de la même chose.",
   parties=[("**A** — Lire une liste", 5, "`equipe[0]`, `equipe[2]`, l'`IndexError`, remplacer un élément, compter les éléments"),
            ("**B** — L'indice et la pose", 5, "`case - 1`, où tombe le X, et le piège du `plateau[case]` **sans erreur rouge**"),
            ("**C** — Le plateau du jeu", 5, "pourquoi les guillemets, l'ordre poser → afficher, et la case libre")],
   clef="**La question 9 est la plus importante.** `plateau[case] = \"X\"` sans le `- 1` **ne déclenche\naucune erreur** : le X se pose simplement à côté. C'est le bug qu'ils rencontreront tous, et le seul\nmoyen de le voir, c'est de le savoir.",
   message="""Voici le travail de la semaine pour votre enfant s'il n'a pas
d'ordinateur à la maison : un quiz de 15 questions, depuis un
téléphone. Comptez 20 minutes.

Les questions portent sur ce que nous avons appris samedi : la LISTE,
qui permet enfin à notre jeu de se souvenir des coups joués."""),

 dict(num=6, dossier="S07-la-case-occupee", mercredi="28 octobre", samedi="24 octobre",
   titre="On ne joue pas deux fois au même endroit",
   accroche="**Cette semaine, le quiz est pour TOUT LE MONDE.** Il n'y a pas d'exercice de maison :\nsamedi 31 octobre, c'est le **TP n°2**, et il vaut mieux qu'ils arrivent frais. Vingt minutes de quiz,\net on se retrouve.",
   parties=[("**A** — La case libre", 5, "comment le programme sait qu'une case est prise : **elle ne contient plus son numéro**"),
            ("**B** — Le `if` dans le `if`", 5, "**4 espaces puis 8**, quel `else` répond à quel `if`, et ce qui se passe quand on en oublie un"),
            ("**C** — Le jeu complet", 5, "les quatre cas d'un coup joué, et **le bug du zéro** qu'ils ont trouvé eux-mêmes")],
   clef="""**La question du zéro est la plus retorse du quiz — et la bonne réponse surprendra même les adultes.**
Dans le jeu **de la séance 6**, taper `0` posait le symbole dans la **case 9** (`0 - 1` vaut `-1`, et
`-1` désigne le **dernier** élément). Mais dans le jeu **de samedi dernier**, le test de la case libre
le **refuse** — en annonçant *« la case 0 est déjà prise »*, ce qui est **faux** : personne n'a jamais
joué la case 0, elle n'existe même pas.

**Le bug n'est donc pas réparé : il est caché, derrière un message qui ment.** C'est exactement ce
qu'on répare à la séance 9 avec `and`. Les élèves qui répondent juste à celle-là arrivent le
7 novembre avec la question déjà posée.""",
   message="""Voici le travail de la semaine : un quiz de 15 questions, depuis un
téléphone. Comptez 20 minutes. Cette semaine il est pour tous les
enfants, avec ou sans ordinateur.

Les questions portent sur la séance de samedi : comment notre jeu
refuse une case déjà jouée.

Samedi 31 octobre, ce sera un TP : deux heures pour construire,
en équipe et en autonomie. Qu'il vienne reposé."""),

 dict(num=7, dossier="S09-et-ou", mercredi="11 novembre", samedi="7 novembre",
   titre="`and`, `or`, et une seule question",
   accroche="**Pour ceux qui n'ont pas d'ordinateur : ils le font À LA PLACE de l'exercice\n« La Soirée du Club Geek ».** Mêmes notions, même semaine.",
   parties=[("**A** — `and` et `or`", 6, "la table à connaître : `True and False`, `False or True`… et la règle en français"),
            ("**B** — Des conditions utiles", 5, "`age >= 12 and age <= 18`, les parenthèses, et les conditions qu'on écrit pour de vrai"),
            ("**C** — Le jeu", 4, "la condition unique du coup valide, et **le bug du zéro enfin mort**")],
   clef="**La question clé est celle du zéro réparé.** Ils ont vécu le bug pendant trois semaines ;\ncette semaine ils doivent pouvoir dire **quelle partie de la condition le tue** : le `case >= 1`.",
   message="""Voici le travail de la semaine pour votre enfant s'il n'a pas
d'ordinateur à la maison : un quiz de 15 questions, depuis un
téléphone. Comptez 20 minutes.

Les questions portent sur les deux mots appris samedi : « and »
(il faut tout) et « or » (il suffit d'un). Grâce à eux, notre jeu
prend deux fois moins de place à l'endroit qui décide."""),

 dict(num=8, dossier="S10-la-boucle", mercredi="18 novembre", samedi="14 novembre",
   titre="Le jeu tourne tout seul",
   accroche="**Pour ceux qui n'ont pas d'ordinateur : ils le font À LA PLACE de l'exercice\n« Le Distributeur de la récré ».** Mêmes notions, même semaine.",
   parties=[("**A** — La boucle", 6, "combien de tours, quand elle s'arrête, et **la boucle infinie**"),
            ("**B** — Dedans ou dehors ?", 5, "le décalage décide de tout : ce qui se répète et ce qui ne se répète pas"),
            ("**C** — Le jeu", 4, "les neuf tours, l'alternance des joueurs, et pourquoi `tour = tour + 1` est **dans le `if`**")],
   clef="**La question sur la boucle infinie est la plus utile de l'année.** Un `while` dont le compteur\nn'avance jamais ne s'arrête jamais — et la seule porte de sortie est **Ctrl + C**. Qu'ils le sachent\navant que ça leur arrive à la maison, un dimanche soir.",
   message="""Voici le travail de la semaine pour votre enfant s'il n'a pas
d'ordinateur à la maison : un quiz de 15 questions, depuis un
téléphone. Comptez 20 minutes.

Les questions portent sur la grande nouveauté de samedi : la boucle.
Notre jeu joue maintenant ses neuf tours tout seul — et le programme
est plus COURT qu'avant."""),

 dict(num=9, dossier="S11-le-gagnant", mercredi="25 novembre", samedi="21 novembre",
   titre="Le jeu sait qui gagne",
   accroche="**Cette semaine, le quiz est pour TOUT LE MONDE.** Pas d'exercice de maison : samedi\n28 novembre c'est le **TP n°3 et le tournoi**, et chacun doit venir avec **son jeu qui marche**.\nLe vrai travail de la semaine, c'est ça.",
   parties=[("**A** — Gagner", 6, "les **8 lignes gagnantes**, et pourquoi trois cases pareilles ne suffisent pas toujours"),
            ("**B** — La boîte `gagnant`", 5, "pourquoi on la crée **vide**, **avant** la boucle, et une seule fois"),
            ("**C** — Ton jeu", 4, "`while tour < 9 and gagnant == \"\"` : **deux raisons de s'arrêter**")],
   clef="**La question sur `gagnant = \"\"` est le cœur du quiz.** Une boîte vide qui attend, créée avant\nla boucle : c'est l'idée la plus abstraite des deux mois. Celui qui sait dire *pourquoi avant* a tout compris.",
   message="""Voici le travail de la semaine : un quiz de 15 questions, depuis un
téléphone. Comptez 20 minutes. Cette semaine il est pour tous les
enfants, avec ou sans ordinateur.

Les questions portent sur la séance de samedi : notre jeu sait
maintenant dire QUI A GAGNÉ, et il s'arrête tout seul.

Samedi 28 novembre, c'est le tournoi de classe : les enfants joueront
aux jeux qu'ils ont eux-mêmes programmés. Qu'il vienne avec le sien."""),

 dict(num=10, dossier="S12-tp-le-tournoi", mercredi="2 décembre", samedi="28 novembre",
   titre="Le bilan des deux mois",
   accroche="**Le quiz-bilan, pour tout le monde.** Il reprend **les sept séances d'octobre et novembre**,\ndes bases jusqu'au tournoi. C'est aussi **votre instrument de mesure** : les résultats question par\nquestion vous disent exactement ce qu'il faudra reprendre en décembre.",
   parties=[("**A** — Les bases", 5, "`int()` / `str()`, le compteur, `if` / `else` — ce qu'ils savaient **avant** octobre"),
            ("**B** — Les listes et la boucle", 5, "`case - 1`, `and` / `or`, `while` — **le cœur des deux mois**"),
            ("**C** — Ton jeu, en entier", 5, "du premier `print` au vainqueur : ce que leur programme fait, et pourquoi")],
   clef="**Lisez les résultats partie par partie, pas élève par élève.** Si la partie B s'effondre, c'est\nl'indice `case - 1` qu'il faut reprendre en décembre — pas la motivation des enfants.",
   message="""Voici le dernier quiz de l'année civile : 15 questions qui reprennent
tout ce que les enfants ont appris en octobre et novembre. Comptez
20 minutes, depuis un téléphone.

En deux mois, ils sont passés d'un programme qui affichait du texte
à un vrai jeu de morpion à deux joueurs, qui sait qui a gagné.
Nous en sommes fiers.

Ce quiz n'est pas une note : c'est pour savoir ce que nous devons
revoir ensemble à la reprise."""),
]

for q in QUIZ:
    parties = "\n".join("| %s | %d | %s |" % (p[0], p[1], p[2]) for p in q["parties"])
    txt = ENTETE_QUIZ.format(num=q["num"], titre=q["titre"], accroche=q["accroche"],
                             mercredi=q["mercredi"], samedi=q["samedi"],
                             parties=parties, clef=q["clef"], message=q["message"])
    chemin = os.path.join(BASE, q["dossier"], "a-envoyer", "quiz-semaine.md")
    open(chemin, "w", encoding="utf-8").write(txt)
    print("écrit :", chemin)
