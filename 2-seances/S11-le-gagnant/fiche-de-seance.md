# Séance 11 — « Le jeu sait qui gagne »

> **Aujourd'hui, le jeu est fini.** À 13 h 50, deux élèves joueront une vraie partie devant la classe,
> sur un programme qu'ils ont écrit eux-mêmes. Prévoyez les applaudissements : ils comptent autant que
> la leçon.

---

## 0. Carte d'identité

| | |
|---|---|
| **Numéro** | 11 / 22 — Phase 2 « Le plateau vit » |
| **Date** | samedi 21 novembre 2026 · **12 h - 14 h** |
| **Notion** | les **8 lignes gagnantes** · la boucle qui s'arrête : `while tour < 9 and gagnant == ""` |
| **Brique projet** | **Le jeu XO complet et jouable** : victoire, match nul, arrêt immédiat |
| **Point de départ** | [le code officiel de la séance 10](../S10-la-boucle/code/code_officiel_fin_de_seance.py) |
| **Livrable** | Une **vraie partie**, jouée et gagnée |

### Les 3 objectifs

1. **Chacun sait écrire une condition de victoire** : trois cases égales entre elles.
2. **Chacun comprend pourquoi la boîte `gagnant` se crée avant la boucle**, pas dedans.
3. **Chacun a joué une partie complète** sur son propre jeu.

> **La question qu'un élève posera, et qui mérite une vraie réponse :** *« et les cases vides ? »*
> Une case libre contient **son numéro** : `"1"`, `"2"`, `"3"` ne seront jamais égaux. Le choix fait à
> la séance 6 **sert encore aujourd'hui**. Dites-le-leur : c'est ça, bien concevoir.

---

## 1. Le programme de la séance

| Horaire | Séquence | Durée |
|---|---|---|
| **12 h - 12 h 15** | Prière et accueil | 15 min |
| **12 h 15 - 12 h 22** | Quiz flash : la boucle | 7 min |
| **12 h 22 - 12 h 35** | **Je montre** : qu'est-ce que gagner ? | 13 min |
| **12 h 35 - 12 h 50** | **Je montre** : les 8 lignes, et la boîte `gagnant` | 15 min |
| **12 h 50 - 13 h** | **Je montre** : la boucle qui s'arrête | 10 min |
| **13 h - 13 h 10** | Pause | 10 min |
| **13 h 10 - 13 h 45** | **Vous faites** : LE PROJET | 35 min |
| **13 h 45 - 14 h** | **La première partie**, et clôture | 15 min |

**Aujourd'hui il n'y a pas d'atelier d'échauffement** : la leçon est longue, et le projet est dense.

---

## 2. Préparation

| Quand | Quoi |
|---|---|
| **La veille** | [`code/live_coding_antiseche.py`](code/live_coding_antiseche.py) en entier |
| **La veille** | **Imprimer 8 × l'aide-mémoire** : il contient **le bloc des 8 `if`, écrit en entier**. Ils le recopieront de là |
| **30 min avant** | `GEEKS/mon_xo/jeu.py` = [`code/depart_eleves.py`](code/depart_eleves.py) |
| **30 min avant** | **[`a-projeter/quiz-rappel.pptx`](a-projeter/quiz-rappel.pptx)** ouvert en premier, le diaporama de la séance derrière |
| **Au tableau** | la grille **avec les indices** `0..8`, pas les numéros de case |

---

## 3. Le quiz flash — 12 h 15, 7 minutes

**Projetez [`a-projeter/quiz-rappel.pptx`](a-projeter/quiz-rappel.pptx)** — 14 diapos : une question par diapo, sa réponse juste après. **On avance d'une diapo seulement quand toutes les cartes sont levées.** Les six mêmes questions figurent aussi, en résumé, sur deux diapos du diaporama de la séance : c'est le plan de secours si vous ne pouvez ouvrir qu'un seul fichier.

| | Question | Réponse |
|---|---|---|
| 1 | `tour = 0` · `while tour < 3:` · `print("A")` · `tour = tour + 1` : combien de A ? | `3` |
| 2 | On oublie `tour = tour + 1` | **boucle sans fin** → `Ctrl + C` |
| 3 | Que fait `Ctrl + C` ? | arrête le programme |
| 4 | Comment alterner X et O ? | un `if` qui **remet** l'autre symbole dans la boîte |
| 5 | Où doit être `tour = tour + 1` ? | **dans** le `if` du coup valide |
| 6 | Un `print` collé à gauche après la boucle, quand s'affiche-t-il ? | **une seule fois, à la fin** |

---

## 4. Le déroulé

### 4.1 · 12 h 22 - 12 h 35 — Je montre : qu'est-ce que gagner ?

**Ouvrez par le problème.** Faites une partie devant eux avec le jeu de la séance 10 : alignez trois X,
et **continuez à jouer**. Le jeu continue bêtement.

> « Il ne voit rien. Aujourd'hui, on lui apprend à **regarder**. »

**Au tableau, la grille avec les indices** (pas les numéros !) :

```
 0 | 1 | 2
---+---+---
 3 | 4 | 5
---+---+---
 6 | 7 | 8
```

> « Donnez-moi **toutes** les façons de gagner. »

Laissez-les chercher. Ils en trouveront six ou sept. **Comptez ensemble : 3 lignes + 3 colonnes +
2 diagonales = 8.** Écrivez les huit triplets au tableau, ils y resteront toute la séance.

Puis la question, à la machine :

```python
plateau = ["X", "X", "X", "4", "O", "6", "O", "8", "9"]
print(plateau[0] == plateau[1] and plateau[1] == plateau[2])   # True
```

> « Si les trois cases contiennent **la même chose**, c'est gagné. Et on n'a pas besoin de savoir si
> c'est X ou O : **on regarde juste si c'est pareil.** »

**Et la question des cases vides** (voir l'encadré de la carte d'identité) : montrez que
`"1" == "2"` est `False`, donc un plateau vide ne déclenche rien.

### 4.2 · 12 h 35 - 12 h 50 — Je montre : les 8 `if` et la boîte `gagnant`

```python
gagnant = ""

if plateau[0] == plateau[1] and plateau[1] == plateau[2]:
    gagnant = plateau[0]
```

**Tapez les deux premiers devant eux, lentement, en nommant les indices à voix haute.** Les six autres,
**ils les recopient de l'aide-mémoire**. C'est long, et c'est normal — dites-le :

> « Oui, huit fois presque la même chose. Il existe une façon d'écrire ça en trois lignes, on
> l'apprendra. **Aujourd'hui, on veut surtout que le jeu marche.** »

### 4.3 · 12 h 50 - 13 h — Je montre : la boucle qui s'arrête

```python
while tour < 9 and gagnant == "":
```

> « **Deux** raisons d'arrêter : le plateau est plein, **ou** quelqu'un a gagné. Tant que les deux
> conditions sont vraies, on continue. »

**Le piège à montrer :** mettez `gagnant = ""` **dans** la boucle. Le gagnant est effacé à chaque tour
et la partie ne s'arrête jamais.

> « La boîte se crée **une seule fois, avant** le `while`. »

### 4.4 · 13 h 10 - 13 h 45 — Vous faites : LE PROJET

[`code/depart_eleves.py`](code/depart_eleves.py), cinq étapes. **Le gros morceau est l'étape 3** : le
bloc des 8 `if`, recopié depuis l'aide-mémoire, **dans la boucle et après la pose**.

**Les erreurs qui vont arriver :**

| Ce qui s'affiche | Ce qui s'est passé | Ce qu'on dit |
|---|---|---|
| La partie **ne s'arrête pas** | `gagnant = ""` remis à zéro dans la boucle | « Combien de fois ta boîte est-elle créée ? » |
| Le gagnant s'appelle **« 5 »** | le bloc des 8 `if` est **avant** la pose | « Tu testes avant de jouer. Dans quel ordre ça doit se passer ? » |
| **Toujours match nul** | le bloc est **après** la boucle | « Il faut vérifier **à chaque coup**, pas une fois à la fin » |
| `IndentationError` | les 8 `if` mal décalés | « Ils sont **dans** le `if` du coup valide. Compte les espaces » |
| `SyntaxError` | un `and` oublié entre deux comparaisons | « Relis ta ligne à voix haute » |

**Carte bleue :** le nombre de coups de la victoire · « VICTOIRE PARFAITE » en 5 coups ·
*« pourquoi ne peut-on pas garder le score entre deux parties ? »*

### 4.5 · 13 h 45 - 14 h — La première partie, et clôture

**Ne sautez pas ce moment, c'est le plus important de la séance.**

1. **Deux élèves jouent une partie devant la classe** (6 min), sur le jeu de l'un d'eux, projeté.
   Commentez à voix haute. **Faites applaudir le gagnant.**
2. **Mur de Mission** (3 min) — la case de la phase 2 est atteinte.
3. **La dernière phrase** (2 min) :

> « Vous avez écrit un jeu. Un **vrai**, avec des règles, un vainqueur et un match nul. Samedi
> prochain, on le teste à fond, on le fignole — **et on fait un tournoi.** À samedi, les Geeks ! »

---

## 5. Les plans de secours

| Ce qui arrive | Ce qu'on fait |
|---|---|
| **Les 8 `if` prennent trop de temps** | On n'en met que **quatre** (les 3 lignes + 1 diagonale) et on le dit : « le jeu sait déjà gagner, on complétera au TP » |
| **La classe est perdue dans les indices** | On revient au tableau, on numérote la grille à la craie, et on fait dicter les 8 triplets par les élèves |
| **Retard : on démarre le projet à 13 h 25** | On garde **la partie jouée devant la classe** et on raccourcit la clôture. Ce moment vaut plus que trois `if` de plus |
| **Un élève n'a pas de boucle qui marche** | Code officiel de la S10, et il repart de là |

---

## 6. Après la séance

1. **Classeur** : présence `S11`, production dans `Suivi` — notez **qui a un jeu complet**.
2. **Journal** : **combien de jeux annoncent correctement le gagnant.** C'est le bilan de la phase 2.
3. **Mercredi** : [quiz n°9](a-envoyer/quiz-semaine.md). *(Pas d'exercice : le TP du tournoi arrive.)*
4. **Préparez le tableau du tournoi** pour samedi prochain, et affichez-le vide dans la salle.

---

## 7. Ce que la séance 11 laisse pour la séance 12

| | |
|---|---|
| **Séance suivante** | **TP n°3 — le tournoi** : tester, fignoler, et jouer |
| **Point de départ** | [`code/code_officiel_fin_de_seance.py`](code/code_officiel_fin_de_seance.py) — **le jeu complet** |
| **Ce qui est acquis** | **tout le jeu XO** : listes, indices, conditions, boucle, victoire |
