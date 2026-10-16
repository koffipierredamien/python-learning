# Séance 7 — « On ne joue pas deux fois au même endroit »

> Le plateau se souvient depuis samedi dernier. Mais il laisse écraser un X par un O.
> Aujourd'hui, le jeu apprend à **dire non** — et pour ça, il faut poser **une question dans une question**.

---

## 0. Carte d'identité

| | |
|---|---|
| **Numéro** | 7 / 22 — Phase 2 « Le plateau vit » |
| **Date** | samedi 24 octobre 2026 · **12 h - 14 h** |
| **Notion** | **le `if` dans le `if`** · une case libre contient **encore son numéro** |
| **Brique projet** | Le jeu **refuse** une case déjà prise, et les deux joueurs posent |
| **Point de départ** | [le code officiel de la séance 6](../S06-le-plateau-se-souvient/code/code_officiel_fin_de_seance.py) |
| **Livrable** | Un `jeu.py` où rejouer la case 5 affiche « déjà prise » et ne change rien |

### Les 3 objectifs

1. **Chacun sait reconnaître qu'une case est libre** : `plateau[case - 1] == str(case)`.
2. **Chacun sait écrire un `if` dans un `if`**, avec 4 puis 8 espaces.
3. **Le projet avance** : les deux joueurs posent, et le jeu refuse proprement.

> **L'idée à faire trouver, pas à donner :** comment savoir qu'une case est libre ? Elle n'est jamais
> vide — **elle contient son propre numéro**. C'est pour ça qu'on a mis les numéros dans la liste.

---

## 1. Le programme de la séance

| Horaire | Séquence | Durée |
|---|---|---|
| **12 h - 12 h 15** | Prière et accueil | 15 min |
| **12 h 15 - 12 h 22** | Quiz flash : les listes | 7 min |
| **12 h 22 - 12 h 45** | **Je montre** : la case libre, puis le `if` dans le `if` | 23 min |
| **12 h 45 - 13 h** | **Vous faites** : le videur de la case | 15 min |
| **13 h - 13 h 10** | Pause | 10 min |
| **13 h 10 - 13 h 20** | **Je montre** : l'erreur volontaire, et **le bug du zéro** | 10 min |
| **13 h 20 - 13 h 50** | **Vous faites** : LE PROJET | 30 min |
| **13 h 50 - 14 h** | Clôture | 10 min |

---

## 2. Préparation

| Quand | Quoi |
|---|---|
| **La veille** | [`code/live_coding_antiseche.py`](code/live_coding_antiseche.py) à voix haute, en entier |
| **La veille** | Imprimer 8 × [`a-imprimer/1-aide-memoire.pdf`](a-imprimer/1-aide-memoire.pdf) |
| **30 min avant** | `GEEKS/mon_xo/jeu.py` = [`code/depart_eleves.py`](code/depart_eleves.py) |
| **Au tableau** | `case libre  →  plateau[case - 1] == str(case)` |

---

## 3. Le quiz flash — 12 h 15, 7 minutes

| | Question | Réponse |
|---|---|---|
| 1 | `equipe = ["A","B","C"]` → `print(equipe[1])` | `B` |
| 2 | `print(equipe[3])` | `IndexError` |
| 3 | La case 7 est à quel indice ? | `6` |
| 4 | `plateau[case]` au lieu de `plateau[case - 1]`, que se passe-t-il ? | le symbole se pose **à côté** |
| 5 | `equipe[0] = "Z"` puis `print(equipe)` | `['Z','B','C']` |
| 6 | Pourquoi écrit-on `"1"` et pas `1` dans la liste ? | pour pouvoir **l'afficher** collé avec `+` |

---

## 4. Le déroulé

### 4.1 · 12 h 22 - 12 h 45 — Je montre

**Ouvrez par le problème.** Lancez le jeu de la séance 6, faites jouer la case 5 au joueur 1, puis
**la case 5 au joueur 2**.

> « Le O a mangé le X. **Est-ce qu'on a le droit, au morpion ?** »

**a) Comment savoir qu'une case est libre ?** (10 min) — **laissez-les chercher deux minutes, vraiment.**
Ils proposeront « si elle est vide ». Montrez que non : elle contient son numéro.

```python
plateau = ["1", "2", "3", "4", "X", "6", "7", "8", "9"]
case = 3
print(plateau[case - 1] == str(case))   # True  -> libre
case = 5
print(plateau[case - 1] == str(case))   # False -> prise
```

> « `str(case)` transforme le nombre 3 en texte `"3"`, pour le comparer avec ce qu'il y a dans la case,
> qui est du texte. »

**b) Le `if` dans le `if`** (8 min) — **au tableau d'abord, en français**, avec les décalages :

```
si la case n'existe pas :
    je refuse
sinon :
    si la case est libre :
        je pose
    sinon :
        je refuse aussi, mais pas pour la même raison
```

> « Deux questions, **l'une dans l'autre**. La deuxième ne se pose **que si** la réponse à la première
> est non. »

Puis à la machine, lentement. **Le geste à faire :** passez le doigt le long des décalages sur l'écran.
*4 espaces, puis 8. Le décalage dit qui est dans qui.*

**c) L'erreur volontaire** (5 min) : effacez les 4 espaces du deuxième `if` → `IndentationError`.

### 4.2 · 12 h 45 - 13 h — Vous faites : le videur de la case

Nouveau fichier, `videur.py`. Au tableau :

```python
plateau = ["1", "2", "3", "4", "X", "6", "7", "8", "9"]
```

1. Demande un numéro de case au joueur, transforme-le en nombre.
2. **Si** la case n'existe pas (plus de 9) → « Cette case n'existe pas ! »
3. **Sinon**, **si** elle est libre → « Case libre, tu peux jouer ! » **sinon** → « Déjà prise ! »

**Testez les trois chemins : 3, puis 5, puis 12.** Carte verte quand les trois marchent.

**Carte bleue :** *« ajoute un compteur : combien de cases sont encore libres ? »*
(Il faudra tester les neuf à la main — et ils trouveront ça long. **C'est voulu** : c'est la boucle qui
s'annonce.)

### 4.3 · 13 h 10 - 13 h 20 — Je montre : le bug qu'on ne répare pas

Tapez **0** devant eux. Le symbole se pose dans la **case 9**.

> « Vous venez de trouver un vrai bug. Pour le réparer proprement, il faudrait poser **deux questions en
> même temps** : *plus grand que 0* **ET** *plus petit que 10*. Ce mot-là, **ET**, on l'apprend dans deux
> semaines. **Notez le bug** : on y revient. »

**Tenez cette promesse** — c'est l'ouverture de la séance 9.

### 4.4 · 13 h 20 - 13 h 50 — Vous faites : LE PROJET

[`code/depart_eleves.py`](code/depart_eleves.py), deux parties.

| | |
|---|---|
| **1** | Le `if` dans le `if` pour le joueur 1 : refus / pose / déjà prise |
| **2** | **Recopier** le bloc pour le joueur 2 (X → O) |
| **3** | **Recopier** les cinq lignes d'affichage à la fin |

**Les erreurs qui vont arriver :**

| Ce qui s'affiche | Ce qui s'est passé | Ce qu'on dit |
|---|---|---|
| `IndentationError` | le deuxième `if` n'est pas décalé | « Le deuxième `if` est **dans** le premier. Décale-le » |
| La case se pose **quand même** | la pose est **hors** du `if` | « Relis le décalage : qu'est-ce qui est dans quoi ? » |
| `TypeError` dans la comparaison | `str(case)` oublié | « Tu compares du texte avec un nombre » |
| Les **deux** messages s'affichent | un `print` en trop, hors du `else` | « Combien de messages veux-tu voir ? » |
| La case 5 reste prenable | la comparaison porte sur `case` au lieu de `plateau[case - 1]` | « Tu compares quoi, avec quoi ? » |

**Carte bleue :** troisième tour · compteur de coups valides · **le bug du zéro** (observer et écrire).

**13 h 48 — `Ctrl + S`**, puis `xo_officiel/`.

### 4.5 · 13 h 50 - 14 h — Clôture

> « Votre jeu dit non. Mais il faut **recopier tout le bloc** pour chaque tour — et pour neuf tours, ce
> serait neuf fois. Samedi prochain, c'est **TP** : on consolide tout ça. Et après, on apprendra à ne
> plus jamais recopier. À samedi ! »

---

## 5. Les plans de secours

| Ce qui arrive | Ce qu'on fait |
|---|---|
| **La classe bloque sur le `if` dans le `if`** | On revient **au français**, au tableau, sans machine. Ils dictent, vous écrivez les décalages |
| **Retard : on démarre à 12 h 40** | On supprime `videur.py` : le projet fait le même travail |
| **Un élève a un plateau cassé depuis S6** | On lui donne le code officiel de la S6 et il repart de là. Pas de rattrapage |
| **Un élève finit tout** | Geek Mentor. Et s'il insiste : qu'il écrive le jeu **à trois joueurs** |

---

## 6. Après la séance

1. **Classeur** : présence `S07`, production dans `Suivi`.
2. **Journal** : **qui a écrit le `if` dans le `if` sans aide**, et qui a trouvé le bug du zéro.
3. **Mercredi** : envoyer le [quiz n°6](a-envoyer/quiz-semaine.md). *(Pas d'exercice de maison : le TP arrive.)*

---

## 7. Ce que la séance 7 laisse pour la séance 8

| | |
|---|---|
| **Séance suivante** | **TP n°2 — le plateau vivant**, 2 h en autonomie |
| **Point de départ** | [`code/code_officiel_fin_de_seance.py`](code/code_officiel_fin_de_seance.py) |
| **Ce qui est acquis** | la liste, l'indice, la pose, **le `if` dans le `if`** |
| **Ce qui reste cassé, exprès** | **le bug du zéro** — réparé à la séance 9 |
