# Séance 6 — « Le plateau se souvient »

> **La notion la plus importante des deux mois.** Sans mémoire, pas de partie. Tout ce qui vient après
> — refuser une case, boucler, détecter le gagnant — repose sur ce qu'ils comprennent aujourd'hui.

---

## 0. Carte d'identité

| | |
|---|---|
| **Numéro** | 6 / 22 — Phase 2 « Le plateau vit » |
| **Date** | samedi 17 octobre 2026 · **12 h - 14 h** |
| **Notion** | **la liste** · l'indice qui commence à **0** · `plateau[case - 1] = "X"` |
| **Brique projet** | Le plateau est une **liste**, il se dessine à partir d'elle, et **le symbole reste** |
| **Point de départ** | [le code officiel de la séance 5](../S04-le-jeu-compte/code/code_officiel_fin_de_seance.py) |
| **Livrable** | Un `jeu.py` où le X du joueur 1 **reste affiché** sur le plateau |

### Les 3 objectifs, par ordre de priorité

1. **Chacun sait que le premier élément porte le numéro 0**, et sait lire une `IndexError`.
2. **Chacun sait écrire `plateau[case - 1] = "X"`** et dire pourquoi il y a un `- 1`.
3. **Le projet avance** : le plateau se dessine à partir de la liste, et garde le symbole posé.

> **Le piège de la séance, et il est unique :** `plateau[case]` au lieu de `plateau[case - 1]`.
> Le symbole se pose **à côté**. Ça ne lève aucune erreur — c'est pour ça que c'est traître.

---

## 1. Le programme de la séance

| Horaire | Séquence | Durée |
|---|---|---|
| **12 h - 12 h 15** | Prière et accueil | 15 min |
| **12 h 15 - 12 h 22** | Quiz flash : ce qu'on sait déjà | 7 min |
| **12 h 22 - 12 h 40** | **Je montre** : la liste, l'indice, l'`IndexError` | 18 min |
| **12 h 40 - 13 h** | **Vous faites** : la liste de la classe | 20 min |
| **13 h - 13 h 10** | Pause | 10 min |
| **13 h 10 - 13 h 20** | **Je montre** : `plateau[case - 1]`, la ligne du jour | 10 min |
| **13 h 20 - 13 h 50** | **Vous faites** : LE PROJET | 30 min |
| **13 h 50 - 14 h** | Clôture | 10 min |

**La règle du jour : 13 h 20, le projet commence.** S'il faut couper, on coupe l'atelier de 12 h 40.

---

## 2. Préparation

| Quand | Quoi |
|---|---|
| **La veille** | Refaire soi-même [`code/live_coding_antiseche.py`](code/live_coding_antiseche.py) à voix haute, en entier |
| **La veille** | Imprimer : 8 × [`a-imprimer/1-aide-memoire.pdf`](a-imprimer/1-aide-memoire.pdf) |
| **30 min avant** | Sur chaque poste : `GEEKS/mon_xo/jeu.py` = [`code/depart_eleves.py`](code/depart_eleves.py) · `GEEKS/xo_officiel/` fermé |
| **30 min avant** | Thonny en taille 18 minimum, diaporama ouvert |
| **Au tableau, et on n'efface pas** | les deux rangées : `1 2 3 4 5 6 7 8 9` et en dessous `0 1 2 3 4 5 6 7 8` |

---

## 3. Le quiz flash — 12 h 15, 7 minutes

Les cartes de couleur, comme d'habitude. **6 questions**, elles sont dans le diaporama.

| | Question | Réponse |
|---|---|---|
| 1 | `print("3" + "4")` | `34` |
| 2 | `age = input(...)` puis `print(age + 1)`, le joueur tape 12 | `TypeError` |
| 3 | `tour = 0` puis deux fois `tour = tour + 1` | `2` |
| 4 | `print(7 >= 7)` | `True` |
| 5 | `if case > 9:` … `else:` … avec `case = 3` | le `else` |
| 6 | Il manque les 4 espaces après `if x > 3:` | `IndentationError` |

---

## 4. Le déroulé

### 4.1 · 12 h 22 - 12 h 40 — Je montre : une boîte à neuf compartiments

**Ouvrez par le problème, pas par la notion.** Lancez leur jeu de samedi dernier, faites jouer la case 5,
et montrez le plateau inchangé :

> « Joyce a joué la case 5. Regardez le plateau… il n'a pas bougé. Votre jeu **ne se souvient de rien**.
> Aujourd'hui, on lui donne une mémoire. »

**a) Au tableau, sans machine** (4 min). Dessinez neuf compartiments côte à côte, et **numérotez-les
dessous, en commençant à 0** :

```
      +-----+-----+-----+-----+-----+-----+-----+-----+-----+
      | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" |
      +-----+-----+-----+-----+-----+-----+-----+-----+-----+
         0     1     2     3     4     5     6     7     8
```

> « Jusqu'ici : une boîte, une chose. Aujourd'hui : **une boîte à neuf compartiments**. Ça s'appelle une
> **liste**. Et attention — **l'ordinateur compte à partir de zéro.** »

**b) À la machine** (6 min) — anti-sèche étapes A et B :

```python
equipe = ["Joyce", "Gedeon", "Sarah"]
print(equipe[0])
print(equipe[2])
```

> **Avant de lancer : « qu'est-ce que `equipe[0]` va afficher ? »** Beaucoup diront *Gedeon*.
> **C'est LA confusion de la séance**, et il faut qu'elle sorte maintenant, à voix haute.

Puis **l'erreur volontaire** : `print(equipe[3])` → **`IndexError: list index out of range`**.

> « Ma liste a trois noms, donc les numéros vont de **0 à 2**. Le 3 n'existe pas. »
> **Faites-leur compter sur leurs doigts : 0, 1, 2.**

**c) On change une case** (4 min) : `equipe[1] = "Ethan"` puis `print(equipe)`.

> « Un compartiment, ça se vide et ça se remplit — comme une boîte. La différence, c'est qu'il y en a
> neuf dans la même. »

**d) Le plateau est une liste** (4 min) — anti-sèche étape D. On affiche la grille **à partir de la
liste**, puis on change `plateau[4]` et on réaffiche.

> « Le dessin n'est plus écrit en dur : il est **fabriqué** à partir de la liste. La liste change,
> le dessin change. »

### 4.2 · 12 h 40 - 13 h — Vous faites : la liste de la classe

Nouveau fichier, `listes.py`. Au tableau, les quatre étapes :

1. une liste `equipe` avec **quatre prénoms** de la classe, affichée en entier ;
2. afficher **le premier**, puis **le dernier** — en nommant leur numéro à voix haute ;
3. remplacer le deuxième prénom, et réafficher ;
4. provoquer l'`IndexError` **exprès**, et lire le message.

**Carte bleue :** *« une liste peut contenir des nombres : `scores = [10, 25, 7]`. Affiche leur total. »*

### 4.3 · 13 h 10 - 13 h 20 — Je montre : la ligne du jour

**Claviers lâchés.** Au tableau, les deux rangées, l'une sous l'autre :

```
la case du joueur :  1  2  3  4  5  6  7  8  9
l'indice Python   :  0  1  2  3  4  5  6  7  8
```

> « Toujours **un de moins**. Donc : **indice = case − 1**. »

```python
case = 5
plateau[case - 1] = "X"
```

**Montrez le piège exprès** : tapez `plateau[case]`, relancez, et laissez-les voir le X se poser à côté.

> « Aucune erreur rouge. Le programme marche… et il est faux. **C'est le genre de bug qu'on ne trouve
> qu'en regardant l'écran.** »

### 4.4 · 13 h 20 - 13 h 50 — Vous faites : LE PROJET

Fichier `GEEKS/mon_xo/jeu.py` = [`code/depart_eleves.py`](code/depart_eleves.py), **trois parties avec
un arrêt après chacune**.

| | |
|---|---|
| **1** | Ton prénom dans l'écran d'accueil |
| **2** | Compléter la **liste** des neuf cases |
| **3** | Compléter les **indices** dans les cinq lignes d'affichage |
| **4** | `case = int(case)` |
| **5** | **`plateau[case - 1] = "X"`** — la ligne de la séance |
| **6** | **Recopier** les cinq lignes d'affichage, après la pose |

**Le rendu attendu**, à projeter :

```
 1 | 2 | 3            Joyce, quelle case veux-tu jouer ? 5
---+---+---
 4 | 5 | 6             1 | 2 | 3
---+---+---            ---+---+---
 7 | 8 | 9              4 | X | 6
                       ---+---+---
                        7 | 8 | 9

                       Le X de Joyce est reste sur le plateau !
```

**Les erreurs qui vont arriver :**

| Ce qui s'affiche | Ce qui s'est passé | Ce qu'on dit |
|---|---|---|
| `IndexError` | indice 9 au lieu de 8, ou `- 1` oublié avec la case 9 | « Compte : de 0 à combien ? » |
| Le X se pose **à côté** | `plateau[case]` au lieu de `plateau[case - 1]` | « Tu as demandé quelle case ? Et le X, il est où ? » |
| `TypeError` | `int(case)` oublié | « Texte ou nombre ? » |
| Le plateau **ne change pas** | l'affichage a été recopié **avant** la pose | « Lis ton programme de haut en bas, avec le doigt » |
| `SyntaxError` sur la liste | une virgule ou un guillemet manquant | « Neuf cases, neuf virgules — compte-les » |

**Carte bleue :** *« fais poser aussi le O du joueur 2 »*, puis *« mets le prénom du joueur dans la case :
que devient le dessin ? »*

**13 h 48 — `Ctrl + S`**, puis on ouvre `xo_officiel/` : le Filet.

### 4.5 · 13 h 50 - 14 h — Clôture

1. **Mur de Mission** (4 min) — la classe avance d'une case.
2. **La question** (4 min) — *« qu'avez-vous compris, de quoi n'êtes-vous pas sûrs ? »*
3. **La dernière phrase** (2 min) :

> « Votre plateau se souvient. Mais essayez de jouer deux fois la même case… il laisse faire. Samedi
> prochain, **le jeu va refuser**. À samedi, les Geeks ! »

---

## 5. Les plans de secours

| Ce qui arrive | Ce qu'on fait |
|---|---|
| **La classe bloque sur l'indice 0** | On arrête tout et on le joue **debout** : neuf élèves alignés, on leur donne un numéro à partir de 0, et on appelle « numéro 4, lève la main ». Cinq minutes qui sauvent le mois |
| **On démarre à 12 h 35** | On supprime l'atelier `listes.py`. On garde : la liste, l'`IndexError`, `case - 1`, le projet |
| **Un élève finit en 10 minutes** | Carte bleue, puis **Geek Mentor** : il aide deux voisins sans toucher leur clavier |
| **Un élève était absent samedi dernier** | Il part du même fichier que les autres. Le Filet a tout rattrapé |
| **Le vidéoprojecteur ne marche pas** | Le live coding se fait sur un poste, les élèves debout autour |

---

## 6. Après la séance, le soir même

1. **Classeur** : présence `S06`, production dans `Suivi`.
2. **Journal** : **combien ont écrit `plateau[case - 1]` sans aide.** C'est la mesure de la séance.
3. **[Dictionnaire des erreurs](../../1-methode/annexes/A6-dictionnaire-des-erreurs.md)** : cocher `IndexError`.
4. **Mercredi** : envoyer le [quiz n°5](a-envoyer/quiz-semaine.md) et l'[exercice de maison](a-envoyer/exercice-maison.md).

---

## 7. Ce que la séance 6 laisse pour la séance 7

| | |
|---|---|
| **Brique suivante** | Le jeu **refuse** une case déjà prise |
| **Point de départ** | [`code/code_officiel_fin_de_seance.py`](code/code_officiel_fin_de_seance.py) |
| **Ce qui est acquis** | tout le reste, **+ la liste, l'indice, et la pose d'un symbole** |
