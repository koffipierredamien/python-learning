# Séance 4 — « Le jeu compte les tours »

> Première séance de format normal après le TP. Les élèves reviennent avec un programme qui **parle** :
> il connaît les deux joueurs. Aujourd'hui, il apprend à **compter**.

---

## 0. Carte d'identité de la séance

| | |
|---|---|
| **Numéro** | 4 / 22 — Phase 1 « Parler au joueur » |
| **Date** | samedi 3 octobre 2026 · **12 h - 14 h** |
| **Organisation** | **Un enseignant par classe**, les deux classes en parallèle |
| **Notions** | **`int()`** : du texte au nombre · **le compteur** `tour = tour + 1` · `str()` pour réafficher |
| **Brique ajoutée au projet** | Le **plateau numéroté 1 à 9**, la case demandée à chaque joueur, et le **compteur de tours** |
| **Livrable élève** | Un `jeu.py` qui demande une case aux deux joueurs, compte les tours et annonce les cases restantes |
| **Point de départ** | Le code officiel de la séance 3, celui du TP |

### Les 3 objectifs, par ordre de priorité

1. **Chacun a compris que `input()` rend toujours du texte**, et sait le transformer avec `int()`.
2. **Chacun sait lire `tour = tour + 1`** : le `=` n'est pas « égal », c'est « range dans ».
3. **Le projet avance** : le plateau est numéroté et le jeu compte ses tours.

> **La vraie difficulté du jour n'est pas `int()`** — c'est la ligne `tour = tour + 1`. Beaucoup la lisent
> comme une équation impossible (« tour égale tour plus un ? »). Prévoyez-y du temps : c'est le socle des
> boucles, dans trois séances.

---

## 1. Le programme de la séance

| Horaire | Séquence | Durée |
|---|---|---|
| **12 h - 12 h 15** | Prière et accueil | 15 min |
| **12 h 15 - 12 h 25** | Le quiz flash : retour sur le TP et le test | 10 min |
| **12 h 25 - 12 h 40** | **Je montre** : texte ou nombre ? `int()`, et l'erreur du jour | 15 min |
| **12 h 40 - 13 h** | **Vous faites** : la calculatrice d'âge | 20 min |
| **13 h - 13 h 10** | Pause | 10 min |
| **13 h 10 - 13 h 25** | **Je montre** : le compteur `tour = tour + 1` | 15 min |
| **13 h 25 - 13 h 50** | **Vous faites** : LE PROJET — le plateau numéroté et les tours | 25 min |
| **13 h 50 - 14 h** | Clôture | 10 min |

**Même structure que la séance 2 : je montre, vous faites. Deux fois.**

### Les trois règles de temps

1. **13 h 25, le projet commence**, quoi qu'il arrive. S'il faut couper, on coupe la calculatrice d'âge : c'est un échauffement, pas la brique.
2. **On ne corrige pas le test n°2 question par question.** Le quiz flash reprend les trois notions les plus ratées, point.
3. **13 h 50, on arrête de coder.** On sauvegarde et on distribue le code officiel.

---

## 2. Préparation

| Quand | Quoi |
|---|---|
| **La veille** | Lire les résultats du test n°2 et **choisir les 3 notions les plus ratées** — elles ouvrent la séance |
| **La veille** | Refaire soi-même le live coding : [`code/live_coding_antiseche.py`](code/live_coding_antiseche.py), à voix haute, en entier |
| **La veille** | Copier le dossier `GEEKS` à jour sur la clé (voir ci-dessous) |
| **30 min avant** | Sur chaque poste : coller `GEEKS` sur le Bureau, vérifier que `mon_xo/jeu.py` s'ouvre et se lance |
| **30 min avant** | Thonny en **taille 18 minimum**, diaporama ouvert, première diapo projetée |

### Le dossier `GEEKS` de cette semaine

```
GEEKS/
├── mon_xo/
│     jeu.py        ← une copie de code/depart_eleves_piste_bleue.py
└── xo_officiel/
      jeu.py        ← une copie de code/code_officiel_fin_de_seance.py
```

`xo_officiel` **reste fermé** jusqu'à 13 h 50 : c'est le Filet.

### À imprimer

| Quantité | Document | Fichier |
|---|---|---|
| 1 par poste | **Aide-mémoire** — texte ou nombre, le compteur, les deux erreurs | [`a-imprimer/1-aide-memoire.pdf`](a-imprimer/1-aide-memoire.pdf) |

Les cartes de signalisation, l'affiche « 3 avant moi » et le Mur de Mission sont déjà en place.

---

## 3. Le déroulé, bloc par bloc

### 3.1 · 12 h - 12 h 15 — Prière et accueil

Comme chaque samedi. **Sur les deux dernières minutes** :

> « Samedi dernier, vous avez travaillé seuls pendant deux heures, et votre jeu connaît maintenant ses deux
> joueurs. Aujourd'hui, il va apprendre à **compter** — et à la fin de la séance, il saura dire combien de
> cases il reste. »

---

### 3.2 · 12 h 15 - 12 h 25 — Le quiz flash

Le support : [`a-projeter/quiz-rappel.pptx`](a-projeter/quiz-rappel.pptx) — 8 questions, les cartes de
couleur, une phrase d'explication par question.

Il reprend **ce que le test n°2 a montré de fragile** : la boîte qui ne garde qu'une valeur, la copie
`b = a`, `print(nom)` contre `print("nom")`, et `"3" + "4"` qui donne `34`. Cette dernière question est le
pont vers la leçon du jour : **gardez-la pour la fin.**

> **On ne commente pas les résultats individuels du test, jamais, et surtout pas à voix haute.**
> Le score est pour vous.

---

### 3.3 · 12 h 25 - 12 h 40 — Je montre : texte ou nombre ?

L'anti-sèche complète : [`code/live_coding_antiseche.py`](code/live_coding_antiseche.py), étapes A, B, C.
**On tape devant eux, dans un fichier vide.**

**a) `input()` rend toujours du texte** (4 min)

```python
age = input("Quel age as-tu ? ")
print(age + 10)
```

> **Avant de lancer : « ça va marcher ? »** Beaucoup diront oui. On lance : **`TypeError`.**
> « Il dit : *can only concatenate str to str*. `str`, c'est *string* : du **texte**. Pourtant j'ai tapé 15 !
> Oui — mais **`input` rend toujours du texte**, même quand vous tapez un nombre. C'est LA chose à retenir
> aujourd'hui. »

**b) `int()`, le traducteur** (4 min)

```python
age = int(age)
print(age + 10)
```

> « `int`, c'est *integer* : nombre entier. La boîte contenait du texte, elle contient maintenant un nombre.
> Et avec un nombre, on peut calculer. »

On lit la ligne à voix haute : *« range dans `age` la version **nombre** de ce qu'il y a dans `age` »*.

**c) L'erreur volontaire du jour** (3 min) — on relance et **on tape `douze` au lieu de `12`** :

> **`ValueError`.** « Il dit : *invalid literal for int*. Je lui ai demandé de transformer ça en nombre, et
> je lui ai donné *douze*. Il ne sait pas faire. `int()` ne marche que si ce qui est tapé est **bien un
> nombre**. »

**On ne répare pas** : se protéger d'une mauvaise saisie demande une condition, et on ne les a pas encore.
Aujourd'hui, on constate et on sait lire le message.

**d) Et pour réafficher : `str()`** (4 min)

```python
print("Dans 10 ans tu auras " + str(age + 10) + " ans")
```

> « Pour recoller un nombre à du texte, on refait le chemin dans l'autre sens. **`str()` : traite ça comme
> du texte.** » Montrez l'oubli une fois — même `TypeError`, ils le reconnaîtront.

---

### 3.4 · 12 h 40 - 13 h — Vous faites : la calculatrice d'âge

Nouveau fichier, `calculatrice.py`. Au tableau, les quatre étapes :

1. demander son âge au joueur et le **transformer en nombre** ;
2. afficher **l'âge dans 10 ans** ;
3. afficher **l'année de naissance** (2026 moins l'âge) ;
4. demander l'âge d'un **deuxième** joueur et afficher **la somme des deux âges**.

**Ce que l'enseignant fait :** il circule, il ne s'assoit pas, **il ne touche jamais un clavier**. Devant un
message rouge, **on le lit avec l'élève** et on demande *« qu'est-ce qu'il te dit ? »*.

**Carte bleue (fini avant) :** *« demande aussi l'âge d'un troisième joueur, et affiche la moyenne des trois. »*

---

### 3.5 · 13 h - 13 h 10 — Pause

Dix minutes. On en profite pour ouvrir `GEEKS/mon_xo/jeu.py` sur chaque poste.

---

### 3.6 · 13 h 10 - 13 h 25 — Je montre : le compteur

**Tout le monde lâche le clavier. Écrans face à nous, mains sur la table.**

**D'abord sans machine, avec les mains :**

> « J'ai une boîte `tour`. Dedans, il y a 0. Je prends ce qu'il y a dedans, j'ajoute 1, et **je remets le
> tout dans la même boîte**. Elle contient maintenant 1. »

```python
tour = 0
tour = tour + 1
print(tour)
```

> **Avant de lancer : « 0 ou 1 ? »**

Puis on ajoute **deux fois exactement la même ligne**, et on redemande :

```python
tour = tour + 1
tour = tour + 1
print(tour)
```

> « La ligne est **toujours la même**, et pourtant le résultat change à chaque fois. C'est normal : elle ne
> dit pas *tour égale 1*. Elle dit **range dans `tour` ce qu'il y a dans `tour`, plus un**.
> **Le signe `=` n'est pas « égal ». C'est « range dans ».** »

> **C'est le point le plus important de la séance.** Allez lentement, faites-le redire par deux ou trois
> élèves avec leurs mots. Dans trois séances, les boucles reposeront entièrement là-dessus.

---

### 3.7 · 13 h 25 - 13 h 50 — Vous faites : LE PROJET

Le fichier est sur chaque poste : `GEEKS/mon_xo/jeu.py`
(c'est [`code/depart_eleves_piste_bleue.py`](code/depart_eleves_piste_bleue.py)).

> « Ouvrez `jeu.py`. **F5 tout de suite : c'est votre programme de samedi dernier, il marche.** Ensuite,
> partie 1 : le plateau porte des numéros. Carte verte, et vous m'attendez. »

**Le fichier est coupé en deux parties, avec un arrêt au milieu** — comme au TP, pour que les plus rapides
ne partent pas seuls dans la partie 2.

Les étapes, telles qu'elles sont dans leur fichier :

| | |
|---|---|
| **1** | Ton prénom dans l'écran d'accueil |
| **2** | Le plateau : les points deviennent les numéros **1 à 9**, en gardant les espaces |
| **3** | Le compteur part de **zéro** |
| **4** | La case tapée devient un **nombre** |
| **5** | **Ajouter 1** au compteur |
| **6** | **Recopier les quatre lignes** pour le joueur 2 — le compteur **ne repart pas** de zéro |
| **7** | Afficher **combien de cases restent libres** (9 moins le nombre de tours) |

**Le rendu attendu**, à projeter pendant l'atelier :

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Joyce, quelle case veux-tu jouer ? 5
Joyce joue la case 5   (tour numero 1)

Gedeon, quelle case veux-tu jouer ? 1
Gedeon joue la case 1   (tour numero 2)

Il reste 7 cases libres.
```

**Les erreurs qui vont arriver :**

| Ce qui s'affiche | Ce qui s'est passé | Ce qu'on dit |
|---|---|---|
| `TypeError` | un nombre collé à du texte sans `str()`, ou du texte calculé sans `int()` | « Texte ou nombre ? Regarde ce qu'il y a vraiment dans ta boîte » |
| `ValueError` | `int()` sur autre chose qu'un nombre | « Qu'est-ce que tu as tapé ? Relance et tape un chiffre » |
| Le compteur reste à **1** | l'élève a écrit `tour = 1` au lieu de `tour = tour + 1` | « Relis ta ligne à voix haute : range dans tour… quoi ? » |
| Le compteur repart à **1** au tour 2 | l'élève a recopié `tour = 0` | « Ton compteur recommence à zéro. Où est-ce qu'il se remet à zéro ? » |

**Carte bleue :** *« demande leur âge aux deux joueurs, et affiche lequel est le plus âgé »* — le défi est
écrit en bas de leur fichier.

**13 h 47 — `Ctrl + S` tous ensemble**, puis on ouvre `xo_officiel/` devant eux : *« voilà le code officiel.
Celui qui n'a pas fini l'a aussi. »*

---

### 3.8 · 13 h 50 - 14 h — Clôture

1. **Le Mur de Mission** (4 min) — la classe avance d'une case. Tout le monde vient.
2. **La question à la classe** (4 min) — *« qu'avez-vous compris aujourd'hui, de quoi n'êtes-vous pas
   encore sûrs ? »* On écoute, on ne corrige pas. **On note le soir dans l'onglet `Journal`.**
3. **La dernière phrase** (2 min) :

> « Votre jeu sait compter. Mais il oublie tout : si Joyce joue la case 5, il ne s'en souvient pas.
> Samedi prochain, **le plateau va se souvenir des coups joués.** À samedi, les Geeks ! »

---

## 4. Les plans de secours

| Ce qui arrive | Ce qu'on fait |
|---|---|
| **Le vidéoprojecteur ne marche pas** | Le live coding se fait sur l'écran d'un poste, les élèves debout autour. Le quiz se lit à voix haute |
| **Une machine ne démarre pas** | L'élève rejoint le poste d'un voisin : à deux sur une machine, on travaille très bien |
| **On démarre à 12 h 35** (retard) | On supprime la calculatrice d'âge. On garde : `int()`, l'erreur volontaire, le compteur, le projet |
| **La classe bloque sur `tour = tour + 1`** | On arrête tout et on le joue **avec un objet** : une boîte, un papier avec un nombre écrit dessus, qu'on remplace. Cinq minutes investies ici en valent trente plus tard |
| **Un élève finit en 10 minutes** | Carte bleue → le défi des âges. Puis **Geek Mentor** : il aide deux voisins, sans toucher à leur clavier |
| **Un élève n'a pas fait le TP** (absent) | Il part du même fichier que les autres : le Filet a tout rattrapé. Aucun rattrapage à faire |
| **Un enseignant est absent** | Les deux classes fusionnent, même déroulé, deux élèves par poste |

---

## 5. Après la séance, le soir même

1. **Le classeur** ([`3-suivi/`](../../3-suivi/LISEZ-MOI.md)) : présence `S04`, la production de chacun dans `Suivi`.
2. **L'onglet `Journal`** : ce qui est ressorti de la clôture — en particulier, combien ont vraiment compris le compteur.
3. **L'onglet `Indiscipline`**, s'il s'est passé quelque chose.
4. **Le [dictionnaire des erreurs](../../1-methode/annexes/A6-dictionnaire-des-erreurs.md)** : cocher `TypeError` et `ValueError`, traités aujourd'hui.

---

## 6. Ce que la séance 4 laisse pour la séance 5

| | |
|---|---|
| **Brique suivante** | Le plateau **se souvient** : la liste des 9 cases, et le symbole qui s'y pose |
| **Point de départ** | [`code/code_officiel_fin_de_seance.py`](code/code_officiel_fin_de_seance.py), distribué aujourd'hui |
| **Ce qui est acquis** | `print`, les variables, `input`, le `+`, **`int()` et `str()`**, **le compteur** |
