# Séance 4 — « Le jeu vérifie et compte »

> Première séance de format normal après le TP. Les élèves reviennent avec un programme qui **parle** :
> il connaît les deux joueurs. Aujourd'hui, il apprend à **compter** — et surtout à **décider**.

---

## 0. Carte d'identité de la séance

| | |
|---|---|
| **Numéro** | 4 / 22 — Phase 1 « Parler au joueur » |
| **Date** | samedi 3 octobre 2026 · **12 h - 14 h** |
| **Organisation** | **Un enseignant par classe**, les deux classes en parallèle |
| **Notions** | **`int()` / `str()`** : texte ou nombre · **le compteur** `tour = tour + 1` · **les opérateurs** : ceux de calcul `+ - * /` et ceux de comparaison `>` `<` `>=` `<=` `==` `!=` · **`if` / `else`** |
| **Brique ajoutée au projet** | Le **plateau numéroté 1 à 9**, la case demandée à chaque joueur, le **compteur de tours**, et le **refus d'une case qui n'existe pas** |
| **Livrable élève** | Un `jeu.py` qui demande une case aux deux joueurs, **vérifie** qu'elle existe, ne compte que les coups valides et annonce les cases restantes |
| **Point de départ** | Le code officiel de la séance 3, celui du TP |

### Trois notions en deux heures : pourquoi

`int()` et `str()` seuls ne remplissent pas deux heures, et à une notion par samedi les 22 séances ne
suffisent pas à finir le jeu. On ajoute donc **la décision**, qui est le vrai déblocage : c'est elle qui
transforme un programme qui récite en programme qui **réfléchit**. Les trois notions s'enchaînent
naturellement : `int()` donne des **nombres**, les nombres se **comparent**, et comparer permet de
**décider**.

> **On nomme les choses : les opérateurs.** Plutôt que de parler vaguement de « comparaison », on leur
> donne le mot et la **famille**. Ils connaissent déjà les **opérateurs de calcul** (`+ - * /`) : ils s'en
> servent depuis la séance 2. On ajoute aujourd'hui les **opérateurs de comparaison**
> (`>` `<` `>=` `<=` `==` `!=`). La différence tient en une phrase : **les premiers donnent un résultat,
> les seconds donnent une réponse — `True` ou `False`.** Ce vocabulaire leur resservira à chaque séance,
> et il évite qu'ils voient `>` comme un signe isolé tombé du ciel.

### Les 4 objectifs, par ordre de priorité

1. **Chacun sait écrire un `if` / `else`** correctement indenté, et sait lire `IndentationError`.
2. **Chacun sait qu'un opérateur de comparaison répond `True` ou `False`**, et ne confond pas `=` et `==`.
3. **Chacun a compris que `input()` rend toujours du texte**, et sait le transformer avec `int()`.
4. **Chacun sait lire `tour = tour + 1`** : le `=` n'est pas « égal », c'est « range dans ».

> **Les deux pièges du jour, à écrire au tableau et à y laisser :**
> `=` c'est **range dans** · `==` c'est **l'opérateur « est égal à »**
> et : après les deux-points, **on décale de 4 espaces**.

---

## 1. Le programme de la séance

| Horaire | Séquence | Durée |
|---|---|---|
| **12 h - 12 h 15** | Prière et accueil | 15 min |
| **12 h 15 - 12 h 22** | Le quiz flash : retour sur le TP et le test | 7 min |
| **12 h 22 - 12 h 35** | **Je montre** : texte ou nombre ? `int()` et `str()` | 13 min |
| **12 h 35 - 12 h 50** | **Vous faites** : la calculatrice d'âge | 15 min |
| **12 h 50 - 13 h** | **Je montre** : le compteur `tour = tour + 1` | 10 min |
| **13 h - 13 h 10** | Pause | 10 min |
| **13 h 10 - 13 h 30** | **Je montre** : les opérateurs, puis la décision `if` / `else` | 20 min |
| **13 h 30 - 13 h 52** | **Vous faites** : LE PROJET — numéroter, compter, vérifier | 22 min |
| **13 h 52 - 14 h** | Clôture | 8 min |

**La séance est dense. Elle tient si et seulement si les trois « je montre » sont courts.**
Chronométrez-les : 13, 10, 20 minutes. Pas une de plus.

### Les quatre règles de temps

1. **13 h 30, le projet commence**, quoi qu'il arrive. S'il faut couper, on coupe la calculatrice d'âge :
   c'est un échauffement, pas la brique.
2. **Le bloc de 13 h 10 est intouchable.** Si quelque chose doit déborder, ce n'est pas celui-là.
3. **On ne corrige pas le test n°2 question par question.** Le quiz flash reprend les trois notions les
   plus ratées, point.
4. **13 h 52, on arrête de coder.** On sauvegarde et on distribue le code officiel.

---

## 2. Préparation

| Quand | Quoi |
|---|---|
| **La veille** | Lire les résultats du test n°2 et **choisir les 3 notions les plus ratées** — elles ouvrent la séance |
| **La veille** | Refaire soi-même le live coding : [`code/live_coding_antiseche.py`](code/live_coding_antiseche.py), à voix haute, en entier. **Sept étapes, A à G** |
| **La veille** | Copier le dossier `GEEKS` à jour sur la clé (voir ci-dessous) |
| **30 min avant** | Sur chaque poste : coller `GEEKS` sur le Bureau, vérifier que `mon_xo/jeu.py` s'ouvre et se lance |
| **30 min avant** | Thonny en **taille 18 minimum**, diaporama ouvert, première diapo projetée |
| **30 min avant** | Au tableau, en haut, et on n'efface pas : `=` **range dans** · `==` **est-ce égal à ?** |

### Le dossier `GEEKS` de cette semaine

```
GEEKS/
├── mon_xo/
│     jeu.py        ← une copie de code/depart_eleves_piste_bleue.py
└── xo_officiel/
      jeu.py        ← une copie de code/code_officiel_fin_de_seance.py
```

`xo_officiel` **reste fermé** jusqu'à 13 h 52 : c'est le Filet.

### À imprimer

| Quantité | Document | Fichier |
|---|---|---|
| 1 par poste | **Aide-mémoire** — texte ou nombre, le compteur, `if` / `else`, les erreurs du jour | [`a-imprimer/1-aide-memoire.pdf`](a-imprimer/1-aide-memoire.pdf) |

Les cartes de signalisation, l'affiche « 3 avant moi » et le Mur de Mission sont déjà en place.

---

## 3. Le déroulé, bloc par bloc

### 3.1 · 12 h - 12 h 15 — Prière et accueil

Comme chaque samedi. **Sur les deux dernières minutes** :

> « Samedi dernier, vous avez travaillé seuls pendant deux heures, et votre jeu connaît maintenant ses deux
> joueurs. Aujourd'hui, il va apprendre à **compter**, et surtout à **réfléchir** : à la fin de la séance,
> si vous demandez la case 12, il vous répondra qu'elle n'existe pas. »

---

### 3.2 · 12 h 15 - 12 h 22 — Le quiz flash

Le support : [`a-projeter/quiz-rappel.pptx`](a-projeter/quiz-rappel.pptx) — **6 questions**, les cartes de
couleur, une phrase d'explication par question. **Sept minutes, pas dix** : la séance est chargée.

Il reprend **ce que le test n°2 a montré de fragile** : la boîte qui ne garde qu'une valeur, la copie
`b = a`, `print(nom)` contre `print("nom")`, et `"3" + "4"` qui donne `34`. Cette dernière question est le
pont vers la leçon du jour : **gardez-la pour la fin.**

> **On ne commente pas les résultats individuels du test, jamais, et surtout pas à voix haute.**
> Le score est pour vous.

---

### 3.3 · 12 h 22 - 12 h 35 — Je montre : texte ou nombre ?

L'anti-sèche : [`code/live_coding_antiseche.py`](code/live_coding_antiseche.py), **étapes A, B, C**.
**On tape devant eux, dans un fichier vide.**

**a) `input()` rend toujours du texte** (4 min)

```python
age = input("Quel age as-tu ? ")
print(age + 10)
```

> **Avant de lancer : « ça va marcher ? »** Beaucoup diront oui. On lance : **`TypeError`.**
> « Il dit : *can only concatenate str to str*. `str`, c'est *string* : du **texte**. Pourtant j'ai tapé 15 !
> Oui — mais **`input` rend toujours du texte**, même quand vous tapez un nombre. »

**b) `int()` et `str()`, les deux traducteurs** (5 min)

```python
age = int(age)
print(age + 10)
print("Dans 10 ans tu auras " + str(age + 10) + " ans")
```

> « `int`, c'est *integer* : **traite ça comme un nombre**, pour calculer. `str` : **traite ça comme du
> texte**, pour coller avec le `+`. Deux sens, deux mots. »

On lit la ligne à voix haute : *« range dans `age` la version **nombre** de ce qu'il y a dans `age` »*.
Montrez l'oubli du `str()` une fois — même `TypeError`, ils le reconnaîtront.

**c) L'erreur volontaire du jour** (3 min) — on relance et **on tape `douze` au lieu de `12`** :

> **`ValueError`.** « Il dit : *invalid literal for int*. Je lui ai demandé de transformer ça en nombre, et
> je lui ai donné *douze*. Il ne sait pas faire. »

**On ne répare pas tout de suite** — et on le dit : *« se protéger d'une mauvaise réponse, ça demande une
**condition**… et justement, on voit ça dans une heure. »* L'attente est créée.

---

### 3.4 · 12 h 35 - 12 h 50 — Vous faites : la calculatrice d'âge

Nouveau fichier, `calculatrice.py`. Au tableau, les trois étapes :

1. demander son âge au joueur et le **transformer en nombre** ;
2. afficher **l'âge dans 10 ans** ;
3. demander l'âge d'un **deuxième** joueur et afficher **la somme des deux âges**.

**Quinze minutes, c'est court : c'est voulu.** L'objectif est que chacun ait tapé `int()` et `str()` une
fois de ses doigts, pas que la calculatrice soit complète.

**Ce que l'enseignant fait :** il circule, il ne s'assoit pas, **il ne touche jamais un clavier**. Devant un
message rouge, **on le lit avec l'élève** et on demande *« qu'est-ce qu'il te dit ? »*.

**Carte bleue (fini avant) :** *« affiche aussi l'année de naissance de chacun : 2026 moins l'âge. »*

---

### 3.5 · 12 h 50 - 13 h — Je montre : le compteur

**Tout le monde lâche le clavier. Écrans face à nous, mains sur la table.**

**D'abord sans machine, avec une vraie boîte et un papier :**

> « J'ai une boîte `tour`. Dedans, un papier avec 0. Je prends ce qu'il y a dedans, j'ajoute 1, et **je
> remets le tout dans la même boîte**. Elle contient maintenant 1. »

```python
tour = 0
tour = tour + 1
tour = tour + 1
print(tour)
```

> **Avant de lancer : « 0, 1, ou 2 ? »**

> « La ligne est **toujours la même**, et pourtant le résultat change à chaque fois. C'est normal : elle ne
> dit pas *tour égale 1*. Elle dit **range dans `tour` ce qu'il y a dans `tour`, plus un**.
> **Le signe `=` n'est pas « égal ». C'est « range dans ».** »

Faites-le redire par deux élèves avec leurs mots, puis on enchaîne. Dix minutes, c'est assez : ils le
retravailleront dans le projet, et dans trois séances les boucles reposeront entièrement là-dessus.

---

### 3.6 · 13 h - 13 h 10 — Pause

Dix minutes. On en profite pour ouvrir `GEEKS/mon_xo/jeu.py` sur chaque poste.

---

### 3.7 · 13 h 10 - 13 h 30 — Je montre : les opérateurs, puis la décision

**Le bloc le plus important de la séance.** Anti-sèche, **étapes E, F, G**. Claviers lâchés.

**a) Le mot du jour : un opérateur** (2 min)

> « Vous en utilisez depuis la séance 2 sans le savoir. Un **opérateur**, c'est un petit signe qui
> **travaille** sur ce qu'il y a de chaque côté de lui. Le `+` en est un. Et il en existe **deux
> familles.** »

Au tableau, les deux colonnes — ils complètent la première de mémoire :

| Les opérateurs de **calcul** | Les opérateurs de **comparaison** |
|---|---|
| `+` additionner (ou coller du texte) | `>` plus grand que |
| `-` soustraire | `<` plus petit que |
| `*` multiplier | `>=` plus grand **ou égal** |
| `/` diviser | `<=` plus petit **ou égal** |
| | `==` **est égal à** |
| | `!=` **est différent de** |
| → donnent un **résultat** : `7`, `12`, `2.5` | → donnent une **réponse** : `True` ou `False` |

> **La phrase à faire retenir :** « les opérateurs de calcul donnent un **résultat**, les opérateurs de
> comparaison donnent une **réponse**. »

**b) On les essaie** (3 min)

```python
print(5 > 3)
print(5 < 3)
print(5 >= 5)
print(5 != 5)
```

> **Avant de lancer : « qu'est-ce que ça peut bien afficher ? »** Ils proposeront `8`, `oui`, `vrai`…
> On lance : **`True False True False`.**
> « Vrai, faux. Un opérateur de comparaison ne donne jamais un nombre : il donne une **réponse** à une
> question fermée. »

> **`>=` se lit « plus grand ou égal », et s'écrit dans cet ordre, sans espace au milieu.** C'est lui
> qu'ils voudront pour le défi en carte bleue (`case >= 1`).

**Le piège, tout de suite**, au tableau, l'un sous l'autre, et on ne l'efface pas :

| | |
|---|---|
| `age = 15` | **range dans** la boîte `age` le nombre 15 |
| `age == 15` | l'**opérateur de comparaison** : est-ce que `age` vaut 15 ? → `True` ou `False` |

> « Un seul `=`, c'est un ordre. Deux `=`, c'est une question. »

**c) Décider : `if` / `else`** (8 min)

```python
age = int(input("Quel age as-tu ? "))

if age > 17:
    print("Tu es un Jeremiah Geek !")
else:
    print("Tu es un Jerusalem Geek !")
```

On tape **très lentement**, en nommant chaque geste :

> « `if`, deux-points. Je passe à la ligne. Et maintenant, **regardez** : Thonny m'a décalé de quatre
> espaces tout seul. Ce décalage n'est pas de la décoration : **c'est lui qui dit ce qui est dans le `if`.**
> `else`, deux-points, et on redécale. »

**On lance deux fois, avec deux âges différents.** C'est toute la démonstration : *« le même programme ne
fait pas la même chose. Il a choisi. »*

**d) L'erreur volontaire du bloc** (4 min) — on efface le décalage de la ligne qui suit le `if` :

> **`IndentationError: expected an indented block`.** « Il me dit : après les deux-points, **il faut
> décaler**. Sans le décalage, il ne sait pas ce qui appartient au `if`. »

On remet les 4 espaces devant eux, on relance, ça marche. **C'est l'erreur qu'ils verront le plus
aujourd'hui : qu'ils la voient d'abord sur votre écran, calmement.**

**e) Le pont vers le projet** (3 min)

> « Tout à l'heure, quand j'ai tapé *douze*, le programme a planté. Et si quelqu'un demande la case **12**
> alors qu'il n'y en a que 9 ? Votre jeu va maintenant **vérifier**. »

---

### 3.8 · 13 h 30 - 13 h 52 — Vous faites : LE PROJET

Le fichier est sur chaque poste : `GEEKS/mon_xo/jeu.py`
(c'est [`code/depart_eleves_piste_bleue.py`](code/depart_eleves_piste_bleue.py)).

> « Ouvrez `jeu.py`. **F5 tout de suite : c'est votre programme de samedi dernier, il marche.** Ensuite,
> partie 1 : le plateau porte des numéros. Carte verte, et vous m'attendez. »

**Le fichier est coupé en trois parties, avec un arrêt après chacune** — comme au TP, pour que les plus
rapides ne partent pas seuls dans la partie suivante. **Le bloc `if` / `else` de l'étape 6 leur est donné
écrit, en commentaire** : à ce stade, on ne leur demande pas de l'inventer, mais de le **recopier
correctement** et de comprendre ce qu'il fait.

Les étapes, telles qu'elles sont dans leur fichier :

| | |
|---|---|
| | **Partie 1 — le plateau porte des numéros** |
| **1** | Ton prénom dans l'écran d'accueil |
| **2** | Les points deviennent les numéros **1 à 9**, en gardant les espaces |
| | **Partie 2 — le jeu demande une case, et compte** |
| **3** | Le compteur part de **zéro** |
| **4** | La case tapée devient un **nombre** |
| **5** | **Ajouter 1** au compteur |
| | **Partie 3 — le jeu réfléchit avant d'accepter** |
| **6** | Transformer la partie 2 en `if` / `else` : la case **au-dessus de 9 est refusée** |
| **7** | **Recopier le bloc** pour le joueur 2 — le compteur **ne repart pas** de zéro |
| **8** | Afficher le **bilan** : coups valides, et cases restantes |

**Le rendu attendu**, à projeter pendant l'atelier :

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Joyce, quelle case veux-tu jouer ? 5
Joyce joue la case 5   (tour numero 1)

Gedeon, quelle case veux-tu jouer ? 12
La case 12 n'existe pas ! Choisis entre 1 et 9.

Coups valides joues : 1
Il reste 8 cases libres.
```

**Dites-leur de tester les deux chemins : une fois la case 5, une fois la case 12.** Un `if` qu'on n'a pas
testé dans ses deux cas n'est pas testé.

**Les erreurs qui vont arriver :**

| Ce qui s'affiche | Ce qui s'est passé | Ce qu'on dit |
|---|---|---|
| `IndentationError` | il manque les 4 espaces après les deux-points | « Après deux-points, on décale. Qu'est-ce qui appartient au `if` ? » |
| `SyntaxError` sur la ligne du `if` | deux-points oubliés, ou `=` au lieu de `==` | « Un ordre ou une question ? Regarde le tableau » |
| **Les deux messages** s'affichent | deux `print` dans le `if`, aucun dans le `else` | « Relis le décalage : qu'est-ce qui est dans quoi ? » |
| `TypeError` | un nombre collé à du texte sans `str()`, ou du texte calculé sans `int()` | « Texte ou nombre ? Regarde ce qu'il y a vraiment dans ta boîte » |
| `ValueError` | `int()` sur autre chose qu'un nombre | « Qu'est-ce que tu as tapé ? Relance et tape un chiffre » |
| Le compteur reste à **1** | `tour = 1` au lieu de `tour = tour + 1` | « Relis ta ligne à voix haute : range dans tour… quoi ? » |
| Le compteur **compte le coup refusé** | `tour = tour + 1` est au-dessus du `if`, ou dans les deux branches | « Un coup refusé, ça compte ? Alors où doit être cette ligne ? » |

**Carte bleue :** *« et si le joueur tape 0, ou -3 ? Ajoute un troisième cas avec `elif case < 1:` »* — ou,
pour ceux qui ont retenu le tableau des opérateurs, `elif case <= 0:`, qui dit exactement la même chose.
Le défi est écrit en bas de leur fichier.

**13 h 50 — `Ctrl + S` tous ensemble**, puis on ouvre `xo_officiel/` devant eux : *« voilà le code officiel.
Celui qui n'a pas fini l'a aussi. »*

---

### 3.9 · 13 h 52 - 14 h — Clôture

1. **Le Mur de Mission** (3 min) — la classe avance d'une case. Tout le monde vient.
2. **La question à la classe** (3 min) — *« qu'avez-vous compris aujourd'hui, de quoi n'êtes-vous pas
   encore sûrs ? »* On écoute, on ne corrige pas. **On note le soir dans l'onglet `Journal`.**
3. **La dernière phrase** (2 min) :

> « Votre jeu sait compter, et il sait refuser. Mais il oublie tout : si Joyce joue la case 5, il ne s'en
> souvient pas. Samedi prochain, **le plateau va se souvenir des coups joués.** À samedi, les Geeks ! »

---

## 4. Les plans de secours

| Ce qui arrive | Ce qu'on fait |
|---|---|
| **Le vidéoprojecteur ne marche pas** | Le live coding se fait sur l'écran d'un poste, les élèves debout autour. Le quiz se lit à voix haute |
| **Une machine ne démarre pas** | L'élève rejoint le poste d'un voisin : à deux sur une machine, on travaille très bien |
| **On démarre à 12 h 35** (retard) | On supprime le quiz flash **et** la calculatrice d'âge. On garde : `int()`/`str()` (8 min), le compteur (7 min), `if`/`else` (20 min), le projet |
| **Le `if` / `else` prend du retard** | On raccourcit le tableau des opérateurs à quatre (`>` `<` `==` `!=`) et on coupe l'étape 7 du projet (le joueur 2) : le joueur 1 qui vérifie suffit. Le code officiel apportera le reste |
| **La classe bloque sur `tour = tour + 1`** | On le joue **avec un objet** : une boîte, un papier avec un nombre écrit dessus, qu'on remplace. Cinq minutes investies ici en valent trente plus tard |
| **La classe bloque sur l'indentation** | Tout le monde ferme le fichier et **recopie les 5 lignes du `if`** depuis le tableau, en comptant les espaces à voix haute. On ne continue pas avant |
| **Un élève finit en 10 minutes** | Carte bleue → le `elif case < 1:`. Puis **Geek Mentor** : il aide deux voisins, sans toucher à leur clavier |
| **Un élève n'a pas fait le TP** (absent) | Il part du même fichier que les autres : le Filet a tout rattrapé. Aucun rattrapage à faire |
| **Un enseignant est absent** | Les deux classes fusionnent, même déroulé, deux élèves par poste |

---

## 5. Après la séance, le soir même

1. **Le classeur** ([`3-suivi/`](../../3-suivi/LISEZ-MOI.md)) : présence `S04`, la production de chacun dans `Suivi`.
2. **L'onglet `Journal`** : ce qui est ressorti de la clôture — en particulier, **combien ont écrit un `if` / `else` qui marche sans aide**.
3. **L'onglet `Indiscipline`**, s'il s'est passé quelque chose.
4. **Le [dictionnaire des erreurs](../../1-methode/annexes/A6-dictionnaire-des-erreurs.md)** : cocher `TypeError`, `ValueError`, `IndentationError` et le `=`/`==`, traités aujourd'hui.
5. **Dans la semaine, le mercredi** : envoyer aux parents le **test n°3**
   ([`a-envoyer/formulaire-exercices.md`](a-envoyer/formulaire-exercices.md)) — 20 points, 12 questions de
   lecture de code et 8 exercices à taper. Les résultats ouvriront la séance 5.

---

## 6. Ce que la séance 4 laisse pour la séance 5

| | |
|---|---|
| **Brique suivante** | Le plateau **se souvient** : la liste des 9 cases, et le symbole qui s'y pose |
| **Point de départ** | [`code/code_officiel_fin_de_seance.py`](code/code_officiel_fin_de_seance.py), distribué aujourd'hui |
| **Ce qui est acquis** | `print`, les variables, `input`, **`int()` et `str()`**, **le compteur**, **les opérateurs de calcul et de comparaison**, **`if` / `else`** |
