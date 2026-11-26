# Séance 12 — « Le jeu dit enfin pourquoi »

> **Le cours est un quiz.** On projette une question, ils lèvent une carte, puis ils tapent.
> La notion arrive au moment où ils ont constaté eux-mêmes qu'elle leur manque.

> 🔴 **LA SEULE CHOSE À NE PAS OUBLIER : une feuille de papier et un stylo sur chaque poste.**
> C'est ce qui a interrompu la séance précédente. Vérifiez poste par poste, avant qu'ils entrent.

---

## 0. Carte d'identité

| | |
|---|---|
| **Numéro** | 12 / 22 |
| **Date** | samedi 28 novembre 2026 · **12 h - 14 h** |
| **Notion** | **Aucune nouvelle.** On pratique `elif` et **l'ordre des conditions**, vus la fois d'avant |
| **Brique projet** | Le jeu ne dit plus « la case n'existe pas **ou** elle est déjà prise » : **il dit laquelle des deux** |
| **Point de départ** | [`code/depart_eleves.py`](code/depart_eleves.py) — leur jeu, inchangé depuis la séance 9 |
| **Livrable** | Un jeu qui donne **trois réponses distinctes** à un coup |

### Les 3 objectifs

1. **Chacun a écrit un algorithme en français sur le papier avant de taper** — au moins deux fois.
2. **Chacun a tapé lui-même une cascade** et l'a vue répondre juste sur six essais.
3. **Chacun sait qu'un mauvais ordre ne provoque aucune erreur rouge** — et sait quels cas essayer
   pour le débusquer.

> **Pourquoi cette séance :** la séance 11 a donné la notion, pas la pratique. Elle s'est arrêtée
> à la diapo de l'algorithme, faute de papier. **Rien de neuf aujourd'hui** : on finit ce qui a été
> commencé, et on le met dans le jeu. Une notion qu'on n'a pas tapée de ses mains n'est pas acquise.

---

## 1. Le programme de la séance

| Horaire | Séquence | Durée |
|---|---|---|
| **12 h - 12 h 15** | Prière et accueil | 15 min |
| **12 h 15 - 12 h 27** | **Manche 1** — quiz de reprise, 7 cartes | 12 min |
| **12 h 27 - 12 h 45** | **Manche 2** — La Médaille : le papier, puis le clavier | 18 min |
| **12 h 45 - 12 h 50** | **Manche 3** — l'erreur qui ne fait pas d'erreur | 5 min |
| **12 h 50 - 13 h 10** | **Manche 4** — et maintenant, VOTRE JEU | 20 min |
| **13 h 10 - 13 h 20** | Pause | 10 min |
| **13 h 20 - 13 h 42** | **L'exercice** : Le Bulletin | 22 min |
| **13 h 42 - 13 h 50** | ⭐ **L'exercice étoile** : Le Prix du Ticket | 8 min |
| **13 h 50 - 14 h** | Clôture | 10 min |

**Tout tient dans un seul fichier à projeter :**
[`a-projeter/cours-en-quiz.pptx`](a-projeter/cours-en-quiz.pptx) — **38 diapos**, de la prière à la clôture.

---

## 2. Préparation

| Quand | Quoi |
|---|---|
| 🔴 **30 min avant** | **Une feuille et un stylo sur chaque poste.** Rien d'autre ne compte autant |
| **30 min avant** | `GEEKS/mon_xo/jeu.py` = [`code/depart_eleves.py`](code/depart_eleves.py), **ouvert dans Thonny** — on y revient à la manche 4 |
| **La veille** | Faire tourner [`code/corrige-la-medaille.py`](code/corrige-la-medaille.py) et les deux corrigés d'exercice. Dix minutes, et plus aucune surprise |
| **La veille** | Lire les **notes du diaporama** : elles portent ce que la fiche ne dit pas |
| **La veille** | **Imprimer** : 8 × [`a-imprimer/1-aide-memoire.pdf`](a-imprimer/1-aide-memoire.pdf) *(le même que la fois d'avant — s'il est déjà imprimé, il ressert)* et 8 × [`a-envoyer/exercice-le-bulletin.pdf`](a-envoyer/exercice-le-bulletin.pdf) — le détail dans [`a-imprimer/quantites-et-formats.md`](a-imprimer/quantites-et-formats.md) |
| **Au tableau, et on n'efface pas** | `Python ne vous dira JAMAIS que votre ordre est faux.` et, en dessous : **l'IMPOSSIBLE d'abord · le PLUS PRÉCIS · le plus large · le `else` attrape le reste** |
| **Les cartes** | Les quatre cartes de couleur sur chaque table |

---

## 3. Manche 1 — le quiz de reprise, 12 h 15

Sept cartes, douze minutes. **On ne s'attarde sur aucune.** Si une passe mal, on la note et on y
revient à la fin.

| # | Ce qu'on demande | La réponse | Ce qu'elle vérifie |
|---|---|---|---|
| 1 | `note = 30`, cascade 90 / 60 **sans `else`** | **rien du tout** | le trou silencieux |
| 2 | Deux `if` séparés, `note = 95` | **Recu, puis Felicitations** | deux `if` ≠ une cascade |
| 3 | `age = input(...)` puis `if age > 12` | **une erreur rouge** | `input` rend du texte |
| 4 | Dans quel ordre range-t-on une cascade ? | **de la plus précise à la plus large** | la règle du jour |
| 5 | Le joueur annonce la case 3 → ? | **`plateau[2]`** | le `case - 1` |
| 6 | Refuser un numéro impossible | **`if case < 1 or case > 9:`** | le `or` |
| 7 | 3 réponses à donner : combien de chemins, combien de conditions ? | **3 chemins, 2 conditions** | **le comptage qu'on fait sur le papier** |

> **La carte 7 prépare toute la séance.** Le `else` n'a pas de condition : il attrape le reste.
> C'est ce comptage qu'ils vont refaire sur leur feuille dix minutes plus tard.

---

## 4. Manche 2 — La Médaille, 12 h 27

**Commencez par demander, à main levée, qui l'a faite à la maison.** On ne commente jamais ceux qui
ne l'ont pas faite : ils la font maintenant, avec les autres.

**La carte :** `points = 100`, avec `if points >= 90` **avant** `elif points == 100`.
La réponse est **« Medaille d'or »**. Demandez qui est tombé dedans chez lui — les mains qui se
lèvent valent tous les discours.

**L'atelier (15 min), en trois temps que l'on tient :**

1. ✍ **La feuille, et rien d'autre.** Une ligne de français par cas, puis on compte : combien de
   chemins, combien de conditions ?
2. **Main levée quand la feuille est écrite.** *Refusez le clavier à qui ne l'a pas.* Trois minutes,
   et tenez-le pour tout le monde, sans exception.
3. **Le clavier**, puis les six essais : 100, 90, 74, 59, 0, 120.

| Le piège | Ce qui se passe |
|---|---|
| **100** | Placé après `>= 90`, le cas `== 100` n'est **jamais atteint** |
| **0** | Qui écrit `points <= 0` pour l'impossible refuse le zéro — **on peut avoir zéro point sans tricher** |

**Faites taper 0 avant de passer à la suite.** Le corrigé complet :
[`code/corrige-la-medaille.py`](code/corrige-la-medaille.py).

⭐ **Pour ceux qui finissent avant :** afficher en plus combien de points il manquait pour la
médaille du dessus — un bloc **séparé**, après la cascade.

---

## 5. Manche 3 — l'erreur qui ne fait pas d'erreur, 12 h 45

Cinq minutes, une seule idée, et c'est la plus importante de la journée :

> **Une erreur rouge est un cadeau : elle vous dit où regarder.
> Un ordre faux ne fait aucun bruit.**

Écrivez-la au tableau et ne l'effacez pas. Les deux réflexes qui en découlent :
**essayer le plus grand, le plus petit, et celui qui est pile sur la limite** ; et **si un chemin
ne s'affiche jamais, c'est qu'un chemin au-dessus l'attrape déjà**.

**La carte :** une cascade `>= 1000` puis `>= 5000`. **« Tres cher » ne s'affichera jamais** —
c'est du code mort, et rien ne le signale.

---

## 6. Manche 4 — et maintenant, VOTRE JEU, 12 h 50

**C'est le moment que la séance précédente n'a pas atteint. Ne le sacrifiez pour rien.**

Projetez leur jeu, tapez `12`, puis une case déjà prise : **le même message les deux fois.**

**La carte — et c'est la meilleure question de la séance :** dans quel ordre poser les trois
questions ? La réponse est **« existe-t-elle ? » d'abord**, et la raison n'est pas seulement
logique : pour savoir si la case 12 est prise, il faudrait aller regarder dans `plateau[11]`,
qui n'existe pas. **Python s'arrêterait sur un `IndexError`.** Laissez le silence, puis faites
expliquer cette raison par un élève.

**L'atelier (14 min) — la brique du jour :**

```python
if case < 1 or case > 9:
    print("   Cette case n'existe pas !")
elif plateau[case - 1] != str(case):
    print("   Cette case est deja prise !")
else:
    plateau[case - 1] = "X"
    print("   Pose !")
```

Trois essais : `12`, une case prise, une case libre. **Trois messages différents.**
⭐ Pour les rapides : la même chose pour le joueur 2, avec un `O`.

**À la fin, le code officiel est distribué à tout le monde, fini ou pas : c'est Le Filet.**
[`code/code_officiel_fin_de_seance.py`](code/code_officiel_fin_de_seance.py)

---

## 7. L'exercice — 13 h 20

**[LE BULLETIN](code/corrige-exercice.py)** (22 min) : trois notes, une moyenne, une cascade de
mentions. La feuille existe :
[`a-envoyer/exercice-le-bulletin.pdf`](a-envoyer/exercice-le-bulletin.pdf) — 2 pages, **étape 0 =
l'algorithme**. Ceux qui n'auront pas fini terminent à la maison.

**⭐ [LE PRIX DU TICKET](code/corrige-exercice-etoile.py)** (8 min, pour ceux qui ont fini) :
une tarification par tranches d'âge, plus une réduction le samedi.

| Le piège | Ce qui se passe |
|---|---|
| **70 ans** | Si la tranche adulte est écrite `elif age >= 18`, un homme de 70 ans paie **2000 F** |
| **3 ans, un samedi** | Sans garde-fou, le prix tombe à **−500 F** : le cinéma rembourse l'enfant |

**Ne les annoncez pas.** Donnez les quatre essais de la diapo, et laissez-les trouver.
Huit minutes ne suffiront pas — c'est voulu : il se finit à la maison.
Le corrigé des deux : [`a-envoyer/correction-le-bulletin.pdf`](a-envoyer/correction-le-bulletin.pdf).

---

## 8. Les erreurs qui vont arriver

| Ce qu'on verra | Ce qu'on fait |
|---|---|
| `elseif`, `else if`, `elsif` | En Python c'est **`elif`**, en un seul mot. Au tableau, en grand |
| La cascade dans le mauvais ordre | **On ne corrige pas la ligne.** On fait taper le cas extrême et lire l'écran à voix haute |
| Pas de `else` final | On fait taper un cas qui ne rentre nulle part. L'écran reste vide : la démonstration est faite |
| `IndentationError` | Il manque les 4 espaces après les deux-points |
| Un élève tape avant d'avoir écrit sa feuille | On ferme Thonny. Trois minutes de papier, puis il reprend. **Sans exception, sinon la règle ne vaut rien** |
| « J'ai pas fait le travail de la maison » | Aucun commentaire. Il le fait maintenant, avec les autres. C'est exactement pour ça que la manche 2 existe |

---

## 9. Plans de secours

| Si… | Alors |
|---|---|
| **Le quiz de reprise déborde** | On coupe les cartes 5 et 6. On ne coupe **jamais** la 1, la 4 ni la 7 |
| **La manche 2 prend tout le temps** | On supprime la manche 3 — sa phrase se dit en trente secondes à la manche 4 |
| **La moitié bloque sur l'algorithme** | On en écrit **un ensemble au tableau**, à voix haute, dicté par la classe. Puis chacun recopie le sien. On ne saute pas l'étape |
| **Il n'y a vraiment pas de papier** | L'algorithme s'écrit **dans Thonny, en commentaires** : une ligne par cas, chacune commençant par `#`, et le code se glisse dessous. **Ce n'est pas un pis-aller : c'est une vraie méthode de programmeur** |
| **Plus que 10 minutes à 13 h 20** | On saute Le Bulletin en classe et on le donne à la maison. On ne saute **jamais** la manche 4 : c'est la brique |
| **Un élève finit tout, exercice étoile compris** | La [mission autonome n°1](../missions-autonomes/LISEZ-MOI.md) — l'ascenseur — s'écrit entièrement avec ce qu'il sait |

---

## 10. Après la séance

1. **Classeur** : présence `S12`, production dans `Suivi`.
2. **Journal** : **combien ont écrit leur algorithme sans qu'on le leur redemande ?**
   C'est l'indicateur de la séance, plus que la cascade elle-même.
3. **À envoyer le soir** : les deux images de
   [`exercice-le-bulletin`](a-envoyer/exercice-le-bulletin-1.png), pour ceux qui finissent à la
   maison. **Le corrigé ne part pas** : il reste pour l'enseignant et les parents.
4. **Le déroulé à transmettre** : [`a-envoyer/deroule-seance-12.pdf`](a-envoyer/deroule-seance-12.pdf) —
   pour Pasteur Eli, une page, sans code ni jargon.

---

## 11. Ce que la séance 12 laisse pour la suite

| | |
|---|---|
| **Ce qui est acquis** | la liste et l'indice · `if` / `elif` / `else` · `and` / `or` · **l'ordre des conditions, pratiqué** · **l'algorithme avant le code** |
| **Ce qui manque encore** | **la répétition.** Leur jeu ne joue toujours qu'**un seul coup** |
| **La suite naturelle** | la boucle `while`, le jour où recopier le bloc du tour neuf fois sera devenu insupportable. **La clôture plante cette graine : laissez la dernière diapo à l'écran pendant qu'ils rangent.** |
