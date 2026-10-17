# Séance 10 — « Le jeu tourne tout seul »

> **La séance la plus importante du parcours.** Depuis cinq semaines, ils recopient des blocs entiers.
> Aujourd'hui, ils apprennent le mot qui dit *recommence* — et leur jeu devient, d'un coup, un vrai jeu.

---

## 0. Carte d'identité

| | |
|---|---|
| **Numéro** | 10 / 22 — Phase 2 « Le plateau vit » |
| **Date** | samedi 14 novembre 2026 · **12 h - 14 h** |
| **Notion** | **la boucle `while`** · l'alternance des joueurs |
| **Brique projet** | **Neuf tours**, joués l'un après l'autre, X et O à tour de rôle |
| **Point de départ** | [le code officiel de la séance 9](../S09-et-ou/code/code_officiel_fin_de_seance.py) |
| **Livrable** | Un `jeu.py` **plus court** que celui de samedi dernier, qui joue une partie entière |

### Les 3 objectifs

1. **Chacun sait écrire une boucle qui s'arrête** — et sait que `tour = tour + 1` en est la clé.
2. **Chacun connaît `Ctrl + C`** pour sortir d'une boucle sans fin. *(Ils en auront besoin aujourd'hui.)*
3. **Le projet avance** : neuf tours, les joueurs alternent.

> **Le geste à enseigner avant tout le reste : `Ctrl + C`.** Faites-le faire à toute la classe, sur
> leur poste, **avant** de commencer. Une boucle infinie sans ce réflexe, c'est un élève qui éteint son
> ordinateur et perd son travail.

---

## 1. Le programme de la séance

| Horaire | Séquence | Durée |
|---|---|---|
| **12 h - 12 h 15** | Prière et accueil | 15 min |
| **12 h 15 - 12 h 22** | Quiz flash : `and` / `or` | 7 min |
| **12 h 22 - 12 h 40** | **Je montre** : `while`, et la boucle sans fin | 18 min |
| **12 h 40 - 12 h 55** | **Vous faites** : le compte à rebours | 15 min |
| **12 h 55 - 13 h 05** | Pause | 10 min |
| **13 h 05 - 13 h 20** | **Je montre** : l'alternance des joueurs | 15 min |
| **13 h 20 - 13 h 50** | **Vous faites** : LE PROJET | 30 min |
| **13 h 50 - 14 h** | Clôture | 10 min |

---

## 2. Préparation

| Quand | Quoi |
|---|---|
| **La veille** | [`code/live_coding_antiseche.py`](code/live_coding_antiseche.py), **deux fois** : c'est la séance à ne pas rater |
| **La veille** | Imprimer 8 × [`a-imprimer/1-aide-memoire.pdf`](a-imprimer/1-aide-memoire.pdf) |
| **30 min avant** | `GEEKS/mon_xo/jeu.py` = [`code/depart_eleves.py`](code/depart_eleves.py) |
| **30 min avant** | **[`a-projeter/quiz-rappel.pptx`](a-projeter/quiz-rappel.pptx)** ouvert en premier, le diaporama de la séance derrière |
| **Au tableau, en grand** | `Ctrl + C` = **arrêter un programme fou** |

---

## 3. Le quiz flash — 12 h 15, 7 minutes

**Projetez [`a-projeter/quiz-rappel.pptx`](a-projeter/quiz-rappel.pptx)** — 14 diapos : une question par diapo, sa réponse juste après. **On avance d'une diapo seulement quand toutes les cartes sont levées.** Les six mêmes questions figurent aussi, en résumé, sur deux diapos du diaporama de la séance : c'est le plan de secours si vous ne pouvez ouvrir qu'un seul fichier.

| | Question | Réponse |
|---|---|---|
| 1 | `print(True and False)` | `False` |
| 2 | `print(False or True)` | `True` |
| 3 | `age = 14` → `print(age >= 12 and age <= 18)` | `True` |
| 4 | `and` ou `or` pour « entre 1 et 9 » ? | `and` |
| 5 | Qu'est-ce qui a disparu du code, samedi dernier ? | le **`if` dans le `if`** |
| 6 | Que fait le jeu si je tape 0, maintenant ? | il **refuse** |

---

## 4. Le déroulé

### 4.1 · 12 h 22 - 12 h 40 — Je montre : `while`

**Ouvrez par la douleur.** Ouvrez leur fichier de la séance 9 et faites défiler lentement.

> « Deux tours. Pour en faire neuf, il faudrait recopier ce bloc **sept fois de plus**. Qui a envie ? »

Laissez-les répondre. Puis : *« il y a un mot pour dire **recommence**. On l'apprend maintenant. »*

**a) Au tableau, en français** (4 min) :

```
TANT QUE le nombre de tours est plus petit que 9 :
    on joue un tour
    on ajoute 1 au nombre de tours
```

> « Le `while` pose sa question **avant chaque tour**. Si la réponse est `True`, il fait le bloc. Puis il
> repose **la même question**. Et ainsi de suite, jusqu'à ce que la réponse soit `False`. »

**b) À la machine** (6 min) :

```python
tour = 0
while tour < 3:
    print("Tour numero " + str(tour))
    tour = tour + 1
print("Fini ! tour vaut " + str(tour))
```

**Avant de lancer : « combien de lignes vont s'afficher ? »** Puis **suivez la valeur de `tour` au
tableau, à la craie**, tour par tour. C'est ce tableau qui fait comprendre, pas le code.

**c) L'erreur volontaire : la boucle sans fin** (8 min). Effacez `tour = tour + 1`, relancez. L'écran
se remplit sans fin.

> « Il ne s'arrêtera **jamais**. `tour` vaut toujours 0, donc la question répond toujours oui. »

**Puis montrez `Ctrl + C`, et faites-le faire à toute la classe.**

> « La ligne qui fait avancer le compteur n'est pas un détail : **c'est elle qui fait que la boucle se
> termine un jour.** »

### 4.2 · 12 h 40 - 12 h 55 — Vous faites : le compte à rebours

Nouveau fichier, `rebours.py`.

1. Une boucle qui affiche `5, 4, 3, 2, 1` puis `PARTEZ !` *(indice : on part de 5 et on **enlève** 1)*.
2. Puis : demander un nombre au joueur et compter **de 1 jusqu'à ce nombre**.

**Carte bleue :** *« affiche la table de multiplication du 7, de 1 à 10, avec une boucle. »*

### 4.3 · 13 h 05 - 13 h 20 — Je montre : l'alternance

**Le problème :** dans la boucle, c'est toujours le même symbole.

```python
symbole = "X"
tour = 0
while tour < 4:
    print("C'est au tour de " + symbole)
    if symbole == "X":
        symbole = "O"
    else:
        symbole = "X"
    tour = tour + 1
```

**Avant de lancer : « X, O, X, O — ou X, X, X, X ? »**

> « C'est la même idée que le compteur : on regarde ce qu'il y a dans la boîte, **et on y remet autre
> chose**. »

Puis montrez que dans le jeu, on échange **deux choses en même temps** : le symbole **et** le nom du
joueur. Les deux lignes vont ensemble, dans le même `if`.

### 4.4 · 13 h 20 - 13 h 50 — Vous faites : LE PROJET

[`code/depart_eleves.py`](code/depart_eleves.py), six étapes.

| | |
|---|---|
| **1** | Les trois boîtes de départ : `tour`, `symbole`, `joueur` |
| **2** | La condition de la boucle : `while tour < 9:` |
| **3** | Poser **le symbole du joueur qui joue** — pas `"X"` en dur |
| **4** | `tour = tour + 1` — **sinon la boucle ne s'arrête jamais** |
| **5** | L'échange : symbole **et** joueur |
| **6** | L'affichage final, **collé à gauche** : hors de la boucle |

**Les erreurs qui vont arriver — elles arriveront toutes :**

| Ce qui s'affiche | Ce qui s'est passé | Ce qu'on dit |
|---|---|---|
| **Ça ne s'arrête plus** | `tour = tour + 1` oublié | « **Ctrl + C.** Maintenant, qu'est-ce qui fait avancer ta boucle ? » |
| `IndentationError` | le bloc de la boucle mal décalé | « Qu'est-ce qui doit se répéter ? Tout ça doit être décalé » |
| Le jeu ne demande **qu'une** case | tout le bloc n'est pas **dans** la boucle | « Regarde où s'arrête le décalage » |
| **Toujours des X** | l'alternance est hors du `if`, ou oubliée | « Qui joue le 2ᵉ tour, dans ton code ? » |
| Le tour avance sur un **coup refusé** | `tour = tour + 1` mal placé | « Un coup refusé, ça compte ? Alors où va cette ligne ? » |
| Le plateau ne s'affiche qu'**une fois** | l'affichage est hors de la boucle | « Tu veux le voir quand, le plateau ? » |

**Carte bleue :** numéro du tour affiché · compteur de coups refusés · faire commencer les O ·
**essayer `while tour < 5` puis `while tour < 20`, et expliquer**.

**13 h 48 — `Ctrl + S`**, puis `xo_officiel/`.

### 4.5 · 13 h 50 - 14 h — Clôture

**Prenez trente secondes pour marquer le coup :**

> « Ouvrez le fichier de samedi dernier, et celui d'aujourd'hui. **Celui d'aujourd'hui est plus court.
> Et il joue une partie entière.** Vous venez de faire ce que font les vrais programmeurs : moins de
> lignes, plus de choses. »

> « Il reste une chose : il ne sait pas **qui a gagné**. Samedi prochain, il le saura. À samedi ! »

---

## 5. Les plans de secours

| Ce qui arrive | Ce qu'on fait |
|---|---|
| **Toute la classe est en boucle infinie** | On arrête tout. `Ctrl + C` ensemble, puis **on écrit au tableau les trois lignes obligatoires** d'une boucle : la boîte avant, la question, et l'avancée dedans |
| **La boucle ne rentre pas** | On la joue **debout** : un élève fait le `while` et demande « tour est plus petit que 3 ? », un autre avance le compteur. Trois tours suffisent |
| **Retard : 12 h 45** | On supprime `rebours.py`. L'alternance (13 h 05) est **intouchable** |
| **Un élève bloque depuis la séance 9** | On lui donne le code officiel de la S9 et il part de là, sans rattrapage |
| **Un élève finit en 15 minutes** | Carte bleue, puis Geek Mentor — il y aura du travail aujourd'hui |

---

## 6. Après la séance

1. **Classeur** : présence `S10`, production dans `Suivi`.
2. **Journal** : **combien ont une boucle qui joue 9 tours sans planter.** C'est la mesure du mois.
3. **Dictionnaire des erreurs** : cocher la boucle sans fin et son `Ctrl + C`.
4. **Mercredi** : [quiz n°8](a-envoyer/quiz-semaine.md) et [exercice de maison](a-envoyer/exercice-maison.md).

---

## 7. Ce que la séance 10 laisse pour la séance 11

| | |
|---|---|
| **Brique suivante** | **Le gagnant**, et la partie qui s'arrête |
| **Point de départ** | [`code/code_officiel_fin_de_seance.py`](code/code_officiel_fin_de_seance.py) |
| **Ce qui est acquis** | la liste, l'indice, `and`/`or`, **la boucle et l'alternance** |
