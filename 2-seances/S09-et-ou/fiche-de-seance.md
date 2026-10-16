# Séance 9 — « Une seule question au lieu de trois »

> **La séance où le code rétrécit.** On n'ajoute rien au jeu : on enlève. Et le bug du zéro, qu'ils ont
> trouvé eux-mêmes il y a quinze jours, meurt aujourd'hui — **pour de bon** : depuis la séance 7 il
> était seulement *caché*, derrière un message faux.

---

## 0. Carte d'identité

| | |
|---|---|
| **Numéro** | 9 / 22 — Phase 2 « Le plateau vit » |
| **Date** | samedi 7 novembre 2026 · **12 h - 14 h** |
| **Notion** | **`and`** (il faut tout) et **`or`** (il suffit d'un) |
| **Brique projet** | Le `if` dans le `if` devient **une seule condition**, et le **bug du zéro est réparé** |
| **Point de départ** | [le code officiel de la séance 7](../S07-la-case-occupee/code/code_officiel_fin_de_seance.py) |
| **Livrable** | Le même jeu, dont **la décision passe de 7 lignes sur 2 niveaux à 4 lignes sur 1**, et qui refuse enfin le 0 pour la bonne raison |

### Les 3 objectifs

1. **Chacun sait dire la différence entre `and` et `or`** avec ses mots.
2. **Chacun a remplacé son `if` dans le `if`** par une condition unique.
3. **Le bug du zéro est mort**, et ils savent pourquoi.

> **Pourquoi cette séance arrive maintenant :** la boucle de samedi prochain serait **illisible** avec
> des `if` imbriqués. On nettoie avant de construire.

---

## 1. Le programme de la séance

| Horaire | Séquence | Durée |
|---|---|---|
| **12 h - 12 h 15** | Prière et accueil | 15 min |
| **12 h 15 - 12 h 22** | Quiz flash : retour du TP | 7 min |
| **12 h 22 - 12 h 40** | **Je montre** : `and`, puis `or` | 18 min |
| **12 h 40 - 12 h 55** | **Vous faites** : le videur du club | 15 min |
| **12 h 55 - 13 h 05** | Pause | 10 min |
| **13 h 05 - 13 h 20** | **Je montre** : on fusionne, et le zéro meurt | 15 min |
| **13 h 20 - 13 h 50** | **Vous faites** : LE PROJET | 30 min |
| **13 h 50 - 14 h** | Clôture | 10 min |

---

## 2. Préparation

| Quand | Quoi |
|---|---|
| **La veille** | [`code/live_coding_antiseche.py`](code/live_coding_antiseche.py) en entier |
| **La veille** | Lire le Journal du TP : **combien ont compris `case - 1`** ? S'ils sont moins de la moitié, commencez par 5 minutes de rappel |
| **30 min avant** | `GEEKS/mon_xo/jeu.py` = [`code/depart_eleves.py`](code/depart_eleves.py) |
| **Au tableau, en grand** | `and  →  il faut TOUT` · `or  →  il suffit d'UN` |

---

## 3. Le quiz flash — 12 h 15, 7 minutes

| | Question | Réponse |
|---|---|---|
| 1 | La case 1 est à quel indice ? | `0` |
| 2 | `plateau[9]` sur une liste de 9 cases | `IndexError` |
| 3 | Comment savoir qu'une case est libre ? | elle contient **encore son numéro** |
| 4 | `plateau[case - 1] = "X"` avec `case = 3` : où va le X ? | dans la **3ᵉ** case |
| 5 | Combien d'espaces devant le **deuxième** `if` — et devant son `print` ? | **4**, puis **8** |
| 6 | Si je tape 0, que dit le jeu de la séance 7 ? | *« la case 0 est déjà prise »* — **et c'est faux** : il refuse par accident |

---

## 4. Le déroulé

### 4.1 · 12 h 22 - 12 h 40 — Je montre : `and` et `or`

**Ouvrez par le bug.** Projetez le code de la séance 7 et tapez **0**.

> « Vous aviez trouvé ce bug. Aujourd'hui on le répare — **et le code va rétrécir.** »

**a) `and`, dans la vraie vie d'abord** (8 min) :

> « Pour entrer au camp, il faut **son cahier ET son stylo**. Tu n'as que le cahier ? Tu n'entres pas. »

```python
print(True and True)      # True
print(True and False)     # False
print(False and True)     # False
print(False and False)    # False
```

**Faites-leur dire les quatre résultats avant de lancer.**

> « Avec `and`, **il faut que tout soit vrai**. Un seul faux, et c'est faux. »

Puis l'exemple utile : `age >= 12 and age <= 18` → *« deux questions dans la même phrase. C'est
exactement ce qui nous manquait pour dire **entre 1 et 9**. »*

**b) `or`** (6 min) : *« pour avoir un goûter, il faut avoir fini son exercice **OU** avoir aidé un
voisin. Un des deux suffit. »*

**c) Le tableau qui reste affiché** (2 min) : `and → il faut TOUT` / `or → il suffit d'UN`.

### 4.2 · 12 h 40 - 12 h 55 — Vous faites : le videur du club

Nouveau fichier, `videur_club.py`. Le programme demande **l'âge** et **le nombre de séances suivies**,
puis décide :

1. **entrée acceptée** si l'âge est entre 12 et 18 **et** qu'il a suivi au moins 3 séances ;
2. sinon, **refus**.

**Carte bleue :** *« avec `or`, accepte aussi quelqu'un qui a plus de 18 ans s'il est enseignant
(une troisième question). »*

### 4.3 · 13 h 05 - 13 h 20 — Je montre : on fusionne

**Le moment de la séance.** Écrivez **l'ancien code à gauche du tableau, le nouveau à droite** :

```
AVANT (séance 7)                   APRÈS (aujourd'hui)
if case > 9:                       if case >= 1 and case <= 9 and plateau[case-1] == str(case):
    refus                              pose
else:                              else:
    if libre:                          refus
        pose
    else:
        refus
7 lignes, 2 niveaux                4 lignes, 1 niveau
```

**Testez les quatre cas devant eux, dans cet ordre : 3 → pose · 5 → refus · 12 → refus · 0 → refus.**

> « **Le bug est mort.** Vous venez d'écrire **moins** de code, et votre jeu fait **plus** de choses.
> C'est ça, programmer : quand ça rallonge tout le temps, c'est souvent qu'il manque une idée. »

### 4.4 · 13 h 20 - 13 h 50 — Vous faites : LE PROJET

[`code/depart_eleves.py`](code/depart_eleves.py).

| | |
|---|---|
| **1** | Compléter la condition unique avec les deux `and` |
| **2** | **Recopier** le bloc (il est court maintenant) pour le joueur 2 |
| **3** | Les cinq lignes d'affichage à la fin |

**Les erreurs qui vont arriver :**

| Ce qui s'affiche | Ce qui s'est passé | Ce qu'on dit |
|---|---|---|
| `SyntaxError` | `and` oublié entre deux conditions | « Lis ta ligne à voix haute : ça se dit ? » |
| Tout est toujours refusé | `>=` et `<=` inversés | « Tu demandes une case **plus petite que 1** ? » |
| `NameError: AND` | `AND` ou `ET` au lieu de `and` | « En minuscules, et en anglais » |
| Le zéro redit « déjà prise » | `case >= 1` oublié | « Il manque une des trois questions. Laquelle ? » |

**Carte bleue :** message différent selon la raison du refus (avec `or`) · compteur de coups refusés ·
**compter les lignes gagnées** par rapport à la semaine dernière.

### 4.5 · 13 h 50 - 14 h — Clôture

> « Votre décision tient en deux fois moins de lignes. Mais pour jouer neuf tours, il faudrait **recopier
> neuf fois** ce bloc. Samedi prochain, on apprend le mot qui dit **recommence**. C'est le plus grand
> jour des deux mois. À samedi ! »

---

## 5. Les plans de secours

| Ce qui arrive | Ce qu'on fait |
|---|---|
| **`and` / `or` ne rentre pas** | On le joue **debout** : « levez la main si vous avez un stylo **ET** un cahier » puis « **OU** ». Ils voient la différence physiquement |
| **Le TP a montré que `case - 1` n'est pas acquis** | 5 minutes de rappel en ouverture, **et on supprime `videur_club.py`** |
| **Retard : 12 h 40 au démarrage** | On supprime l'atelier. La fusion (13 h 05) est **intouchable** |
| **Un élève finit tout** | Qu'il réécrive aussi le **videur du club** avec une seule condition |

---

## 6. Après la séance

1. **Classeur** : présence `S09`, production dans `Suivi`.
2. **Journal** : **combien ont une condition unique qui marche**, zéro compris.
3. **Dictionnaire des erreurs** : cocher le `SyntaxError` sur les conditions.
4. **Mercredi** : [quiz n°7](a-envoyer/quiz-semaine.md) et [exercice de maison](a-envoyer/exercice-maison.md).

---

## 7. Ce que la séance 9 laisse pour la séance 10

| | |
|---|---|
| **Brique suivante** | **La boucle `while`** : neuf tours, tout seuls |
| **Point de départ** | [`code/code_officiel_fin_de_seance.py`](code/code_officiel_fin_de_seance.py) |
| **Ce qui est acquis** | la liste, l'indice, la pose, **`and` et `or`**, une condition propre |
