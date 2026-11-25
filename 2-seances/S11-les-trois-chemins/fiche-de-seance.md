# Séance 11 — « Trois chemins au lieu de deux »

> **Le cours est devenu un quiz.** On ne fait plus « je montre / vous faites » : on projette une
> question, ils lèvent une carte, puis ils tapent. La notion du jour arrive au moment où ils ont
> constaté eux-mêmes qu'elle leur manque.

> ⚠️ **CETTE SÉANCE A ÉTÉ INTERROMPUE, ET ELLE REPREND.**
> Elle s'est arrêtée **à la diapo qui demande d'écrire l'algorithme** (l'atelier de la manche 3) :
> les apprenants n'avaient **ni papier ni stylo**. Ont été faits : le quiz de révision, les manches
> 1 et 2 en entier (le constat, `elif`, l'atelier 1), et **les deux questions de la manche 3** —
> le piège de `note = 18` et l'ordre des conditions. Reste : **l'atelier 2**, la manche 4, et les
> deux exercices.
>
> **On reprend cette même fiche à cet endroit**, avec deux précautions : **du papier et un stylo
> sur chaque poste avant leur arrivée**, et **cinq minutes de reprise** sur les manches 2 et 3,
> parce qu'une semaine a passé. Rien d'autre ne change.
>
> Entre les deux, un quiz de rappel et un exercice sont partis aux familles :
> [`a-envoyer/travail-de-la-semaine.md`](a-envoyer/travail-de-la-semaine.md).

---

## 0. Carte d'identité

| | |
|---|---|
| **Numéro** | 11 / 22 |
| **Date** | samedi 21 novembre 2026 · **12 h - 14 h** |
| **Notion** | **`elif`** — « sinon, si… » · et **l'ordre des conditions** |
| **Brique projet** | Le jeu ne dit plus « la case n'existe pas **ou** elle est déjà prise » : **il dit laquelle des deux** |
| **Point de départ** | [le code officiel de la séance 9](../S09-et-ou/code/code_officiel_fin_de_seance.py) |
| **Livrable** | Un jeu qui donne **trois réponses distinctes** à un coup |

### Les 3 objectifs

1. **Chacun sait dire ce que fait `elif`** avec ses mots : *« sinon, si… »*.
2. **Chacun sait que Python s'arrête au premier vrai** — et sait ce que ça coûte quand l'ordre est faux.
3. **Chacun a écrit un algorithme sur son cahier avant de taper**, au moins une fois.

> **Pourquoi cette séance maintenant :** la révision du 14 novembre n'a pas pu aller à son terme, la
> boucle n'a pas été commencée, et le `if` / `else` n'a pas eu assez d'exercices. `elif` consolide
> exactement ce qui est fragile, **sans rien ouvrir de neuf** — et le jeu y gagne une brique visible
> le jour même.

---

## 1. Le programme de la séance

| Horaire | Séquence | Durée |
|---|---|---|
| **12 h - 12 h 15** | Prière et accueil | 15 min |
| **12 h 15 - 12 h 28** | **Quiz de révision** — 7 cartes | 13 min |
| **12 h 28 - 13 h 05** | **Le cours en quiz** — 4 manches, 3 ateliers au clavier | 37 min |
| **13 h 05 - 13 h 15** | Pause | 10 min |
| **13 h 15 - 13 h 40** | **L'exercice** : Le Bulletin | 25 min |
| **13 h 40 - 13 h 50** | ⭐ **L'exercice étoile** : Le Prix du Ticket *(pour ceux qui ont fini)* | 10 min |
| **13 h 50 - 14 h** | Clôture | 10 min |

**Tout tient dans un seul fichier à projeter :**
[`a-projeter/cours-en-quiz.pptx`](a-projeter/cours-en-quiz.pptx) — **46 diapos**, de la prière à la clôture.

---

## 2. Préparation

| Quand | Quoi |
|---|---|
| **La veille** | Faire tourner [`code/ateliers-corriges.py`](code/ateliers-corriges.py) et les deux corrigés d'exercice. Dix minutes, et plus aucune surprise |
| **La veille** | Lire les **notes du diaporama** : elles portent ce que la fiche ne dit pas |
| **La veille** | **Imprimer** : 8 × [`a-imprimer/1-aide-memoire.pdf`](a-imprimer/1-aide-memoire.pdf) (A4 recto) et 8 × [`a-envoyer/exercice-le-bulletin.pdf`](a-envoyer/exercice-le-bulletin.pdf) (A4 recto-verso) — le détail dans [`a-imprimer/quantites-et-formats.md`](a-imprimer/quantites-et-formats.md) |
| **30 min avant** | `GEEKS/mon_xo/jeu.py` = [`code/depart_eleves.py`](code/depart_eleves.py) · un fichier neuf `mentions.py` pour les ateliers |
| **Au tableau, et on n'efface pas** | `elif  =  « sinon, si ... »` et, en dessous, **`Python s'arrete au PREMIER VRAI`** |
| **Les cartes** | Les quatre cartes de couleur sur chaque table, comme d'habitude |
| 🔴 **Sur chaque poste** | **Une feuille de papier et un stylo.** C'est ce qui a interrompu la séance la première fois : l'algorithme ne s'écrit pas sans. À défaut, on écrit l'algorithme **dans Thonny, en commentaires**, chaque ligne commençant par `#` |

---

## 3. Le quiz de révision — 12 h 15, 7 cartes

| | Question | Réponse |
|---|---|---|
| 1 | `x = 2` · `if x > 5: print("A")` · `print("B")` | **B seulement** |
| 2 | `points = 50` · `if points > 50: points = points + 10` | **50** |
| 3 | `age = 11` · `print(age >= 12 and age <= 18)` | **False** |
| 4 | Refuser une case hors de 1 à 9 | `case < 1 or case > 9` |
| 5 | `equipe = ["A","B","C","D"]` · `print(equipe[3])` | **D** |
| 6 | `plateau[case]` sans le `- 1`, avec `case = 3` | le X se pose **case 4**, et **Python ne dit rien** |
| 7 | `print` collé à gauche après les deux-points | `IndentationError` |

**Treize minutes, sept cartes : on ne s'attarde sur aucune.** Si une carte passe mal, notez-la et
revenez-y à la clôture — pas maintenant.

---

## 4. Le cours en quiz — 12 h 28, quatre manches

### Manche 1 · 12 h 28 — « Votre jeu dit quelque chose de faux » (4 min)

**Projetez leur vrai jeu** et tapez `12`. Puis tapez une case déjà prise. **Le même message les deux
fois.** C'est tout le problème du jour, et ce sont eux qui le constatent.

Puis la carte : *« avec un `if` et un `else`, combien de réponses différentes ? »* → **deux**.
Or il en faut **trois**. Enchaînez.

### Manche 2 · 12 h 32 — `elif` (12 min)

La leçon tient en une diapo et une règle, **à écrire au tableau et à ne pas effacer** :

> **Python s'arrête au PREMIER VRAI. Les questions d'après ne sont même plus regardées.**

Puis la carte des **deux `if` séparés** — beaucoup répondront « Admis » seulement, et l'écran en
affichera deux. **N'expliquez pas : enchaînez sur l'atelier.**

**Atelier 1 (8 min)** — remplacer le deuxième `if` par `elif`.
⭐ *pour ceux qui finissent :* mettre `note = 8` et relancer les deux versions. Aucune n'affiche rien :
il manque un `else`. **La notion suivante arrive par eux.**

### Manche 3 · 12 h 44 — « L'ordre décide de tout » (15 min)

**La question la plus importante de la séance :**

```
note = 18
if note >= 10:
    print("Passable")
elif note >= 16:
    print("Tres bien")
```

Un 18/20 annoncé « Passable ». **Laissez le silence s'installer** avant de montrer la réponse.

**Atelier 2 (12 min) — la cascade des mentions.** C'est ici que l'algorithme devient obligatoire :

> ✍️ **L'algorithme sur le cahier d'abord. Pas de clavier tant qu'il n'est pas écrit.**
> Circulez et **refusez le clavier** à qui ne l'a pas. Ça prend trois minutes et ça change la séance.

⭐ *pour ceux qui finissent :* une deuxième cascade d'appréciations.

### Manche 4 · 12 h 59 — « Et maintenant, votre jeu » (6 min)

La carte sur `plateau[case - 1] != str(case)`, puis **l'atelier 3** : la cascade entre dans leur jeu,
pour le joueur 1. ⭐ *pour ceux qui finissent :* le joueur 2, avec un O.

**À la fin, [le code officiel](code/code_officiel_fin_de_seance.py) est distribué à tous, fini ou pas.**
C'est Le Filet.

---

## 5. L'exercice — 13 h 15

**[LE BULLETIN](code/corrige-exercice.py)** (25 min) : trois notes, une moyenne, une cascade de mentions,
un bulletin affiché. **L'algorithme sur le cahier d'abord**, comme à l'atelier 2.

> **La feuille existe :** [`a-envoyer/exercice-le-bulletin.pdf`](a-envoyer/exercice-le-bulletin.pdf)
> (2 pages, étape 0 = l'algorithme) et son corrigé
> [`a-envoyer/correction-le-bulletin.pdf`](a-envoyer/correction-le-bulletin.pdf), qui porte **les deux
> programmes**. Les `.png` à côté sont là pour WhatsApp. Ceux qui n'auront pas fini terminent à la maison.

**⭐ [LE PRIX DU TICKET](code/corrige-exercice-etoile.py)** (10 min, pour ceux qui ont fini) : une
tarification par tranches d'âge, plus une réduction le samedi. **Deux pièges sont cachés dedans :**

| Le piège | Ce qui se passe |
|---|---|
| **70 ans** | Si la tranche adulte est écrite `elif age >= 18`, un homme de 70 ans paie **2000 F** : `70 >= 18` est déjà vrai, et Python s'arrête là |
| **3 ans, un samedi** | Sans garde-fou, le prix tombe à **−500 F** : le cinéma rembourse l'enfant |

**Ne les annoncez pas.** Demandez simplement **les quatre essais** de la diapo, et laissez-les trouver.

---

## 6. Les erreurs qui vont arriver

| Ce qu'on voit | La cause | Ce qu'on dit |
|---|---|---|
| `SyntaxError` sur le `elif` | `elseif`, ou `else if`, ou un `elif` sans `if` avant | « En Python, c'est **un seul mot** : `elif` » |
| Tout le monde est « Passable » | La cascade commence par la condition la plus large | « Essaie avec 20. Qu'est-ce qu'il te dit ? » |
| Les deux messages s'affichent | Deux `if` séparés au lieu d'une cascade | « Compte les questions que Python pose » |
| Une note de 5 n'affiche rien | Le `else` final manque | « Et celui qui n'est dans aucun cas, qui lui répond ? » |
| `IndentationError` | Pas de décalage après les deux-points | *(connu depuis la séance 4 — on pointe le tableau)* |

---

## 7. Plans de secours

| Si… | Alors |
|---|---|
| **Le quiz de révision déborde** | On coupe les cartes 5, 6 et 7. On ne coupe jamais la 1 ni la 2 : le décalage est la fragilité du moment |
| **Retard : 12 h 45 à la manche 2** | On supprime l'atelier 1 et on va directement à la manche 3. **La manche 3 est intouchable** |
| **La manche 3 se passe mal pour la moitié** | On supprime la manche 4, et on passe les 6 minutes gagnées sur l'exercice. Le jeu attendra samedi prochain |
| **Un élève finit tout, exercice étoile compris** | La [mission autonome n°1](../missions-autonomes/LISEZ-MOI.md) — l'ascenseur — s'écrit entièrement avec ce qu'il sait |

---

## 8. Après la séance

1. **Classeur** : présence `S11`, production dans `Suivi`.
2. **Journal** : **combien ont écrit un algorithme sur leur cahier sans qu'on le leur redemande ?**
   C'est l'indicateur de la séance, plus que la cascade elle-même.
3. **À envoyer le soir** : les deux images
   [`a-envoyer/exercice-le-bulletin-1.png`](a-envoyer/exercice-le-bulletin-1.png) et
   [`-2.png`](a-envoyer/exercice-le-bulletin-2.png), pour ceux qui finissent à la maison.
   **Le corrigé ne part pas** : il reste pour l'enseignant et les parents.
4. **Le déroulé à transmettre** : [`a-envoyer/deroule-seance-11.pdf`](a-envoyer/deroule-seance-11.pdf) —
   pour Pasteur Eli, sans code ni jargon.

---

## 9. Ce que la séance 11 laisse pour la suite

| | |
|---|---|
| **Ce qui est acquis** | la liste et l'indice · `if` / `elif` / `else` · `and` / `or` · l'ordre des conditions · l'algorithme avant le code |
| **Ce qui manque encore** | **la répétition** — recopier le bloc du tour reste la seule manière de jouer plusieurs coups |
| **La suite naturelle** | la boucle `while`, le jour où la recopie sera devenue insupportable. **Elle le sera.** |
