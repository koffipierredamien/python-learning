# 🗺️ Le parcours d'octobre et novembre 2026 — 7 séances

> **Ce document est la carte.** Il dit où on va, pourquoi dans cet ordre, et ce qui est prêt.
> Les sept séances sont **entièrement préparées** : fiche, code, aide-mémoire, diaporama, quiz de la
> semaine, exercices de maison et corrigés. **Vous pouvez tenir deux mois sans rien avoir à écrire.**

---

## 1. Ce que les élèves savent déjà, au 17 octobre

`print` · les variables · `input` · le `+` qui colle · **`int()` et `str()`** · le compteur
`tour = tour + 1` · les opérateurs de comparaison `>` `<` `>=` `<=` `==` `!=` · **`if` / `else`** ·
lire un message rouge.

**Leur jeu, aujourd'hui :** il accueille les deux joueurs, affiche un plateau dessiné en dur, demande
une case à chacun, refuse un numéro au-dessus de 9, et compte les coups valides.
**Ce qu'il ne sait pas faire :** se souvenir. Si Joyce joue la case 5, le plateau ne change pas.

---

## 2. Le fil des sept séances

**Une règle a guidé tout le parcours : à chaque séance, le jeu doit faire quelque chose de
visiblement nouveau.** Pas une notion pour la notion — une notion parce que le jeu en a besoin,
maintenant.

| # | Date | Titre | La notion | Ce que le jeu sait faire en partant |
|---|---|---|---|---|
| **6** | sam. 17 oct | **Le plateau se souvient** | **la liste**, l'indice, `plateau[case - 1]` | Le symbole **reste** sur le plateau |
| **7** | sam. 24 oct | **On ne joue pas deux fois au même endroit** | **le `if` dans le `if`** | Le jeu **refuse** une case déjà prise |
| **8** | sam. 31 oct | 🛠️ **TP n°2 — le plateau vivant** | *(consolidation, 2 h en autonomie)* | Quatre coups d'affilée, sans bug |
| **9** | sam. 7 nov | **Une seule question au lieu de trois** | **`and` et `or`** | Le même jeu, **avec deux fois moins de lignes** |
| **10** | sam. 14 nov | **Le jeu tourne tout seul** | **la boucle `while`** | **Neuf tours**, les joueurs alternent |
| **11** | sam. 21 nov | **Le jeu sait qui gagne** | les 8 lignes gagnantes, la boucle qui s'arrête | **Une vraie partie, avec un vainqueur** |
| **12** | sam. 28 nov | 🏆 **TP n°3 — le tournoi** | *(finitions, tests, et on joue)* | **Le jeu XO, fini et jouable** |

### Pourquoi cet ordre, et pas un autre

- **La liste d'abord (S6).** C'est la seule notion qui débloque tout le reste : sans mémoire, pas de
  partie. Et c'est la plus dure — elle arrive donc quand il reste sept semaines pour la digérer.
- **`and` / `or` avant la boucle (S9).** À la séance 7, le code a **un `if` dans un `if`** : ça
  marche, mais c'est lourd. `and` permet de le réécrire en **une seule ligne**. On introduit donc la
  notion au moment où elle *simplifie* quelque chose qu'ils ont écrit eux-mêmes — pas avant.
  Et surtout : la boucle de la séance 10 serait illisible avec des `if` imbriqués.
- **La boucle en dixième position (S10).** Depuis la séance 5, les élèves **recopient** des blocs
  entiers — au devoir du Nombre Secret, trois fois le même. L'agacement est installé. Quand `while`
  arrive, ce n'est pas une nouveauté scolaire : c'est **une délivrance**.
- **Deux TP, aux bons endroits (S8, S12).** Le premier juste après la notion la plus dure, pour
  laisser le temps de la digérer. Le second à la fin, pour finir et **jouer**.

### Les trois rendez-vous où ils sentiront qu'ils progressent

| Quand | Ce qui se passe | Pourquoi ça marque |
|---|---|---|
| **S6, 17 oct** | Le premier X **reste** sur le plateau | Pour la première fois, le programme *se souvient* |
| **S10, 14 nov** | Le jeu enchaîne **9 tours tout seul** | Ils ont supprimé 40 lignes et le jeu fait plus |
| **S12, 28 nov** | **Tournoi de classe** sur leurs propres jeux | Ils jouent à ce qu'ils ont fabriqué |

---

## 3. Le calendrier complet, semaine par semaine

| Samedi | En séance | Le mercredi suivant |
|---|---|---|
| **17 oct** | S6 — Le plateau se souvient | Quiz n°5 · **Exercice de maison : Le Coffre-Fort** |
| **24 oct** | S7 — La case déjà prise | Quiz n°6 |
| **31 oct** | S8 — **TP n°2** (2 h) | *rien* — le TP est le travail de la semaine |
| **7 nov** | S9 — `and` / `or` | Quiz n°7 · **Exercice de maison : Le Videur du Club** |
| **14 nov** | S10 — La boucle `while` | Quiz n°8 · **Exercice de maison : Le Distributeur** |
| **21 nov** | S11 — Le gagnant | Quiz n°9 |
| **28 nov** | S12 — **TP n°3 + tournoi** | Quiz n°10 (bilan des deux mois) |

**Six quiz** (15 questions, corrigés à 100 % automatiquement) et **trois exercices de maison** (un vrai
petit jeu à écrire, avec corrigé). Comme d'habitude : **ceux qui ont un ordinateur font l'exercice,
les autres font le quiz.**

---

## 4. Ce qui est prêt pour chaque séance

Chaque dossier `S0x-…/` contient exactement la même chose, au même endroit :

```
fiche-de-seance.md      LA RÉFÉRENCE : le déroulé minute par minute, les phrases à dire,
                        les erreurs qui vont arriver, et les plans de secours
a-projeter/             le diaporama de la séance (quiz flash de début compris)
a-imprimer/             l'aide-mémoire 1 page + la liste de ce qu'il faut imprimer
a-envoyer/              le déroulé pour le responsable · le quiz de la semaine ·
                        l'exercice de maison et son corrigé
code/                   depart_eleves.py · code_officiel_fin_de_seance.py ·
                        live_coding_antiseche.py
```

**Le Filet n'a pas changé :** à la fin de chaque séance, `code_officiel_fin_de_seance.py` est
distribué à tout le monde, fini ou pas. Personne ne commence la séance suivante en retard.

---

## 5. Les trois règles qui tiennent le parcours

1. **Un seul exercice pour tous.** Des défis ⭐ pour ceux qui finissent avant ; de l'aide — pas un
   exercice plus facile — pour ceux qui bloquent.
2. **On ne devance jamais le besoin.** Chaque notion arrive quand le jeu la réclame. Si une séance
   déborde, ce qu'on coupe est toujours l'atelier d'échauffement, jamais la leçon.
3. **Le jeu doit marcher à la fin de chaque samedi.** Un jeu qui marche moins bien mais qui marche
   vaut mieux qu'un jeu à moitié écrit : c'est ce qui fait revenir les enfants.

---

## 6. Si vous prenez du retard

C'est prévu, et ce n'est pas grave. **L'ordre des séances est une file, pas un calendrier.** Si la
séance 7 n'est pas finie le 24, elle se termine le 31 et le TP n°2 glisse d'une semaine — le parcours
reste cohérent, seul le tournoi recule.

**Les deux choses à ne jamais sacrifier :** la liste (S6) et la boucle (S10). Tout le reste peut
attendre une semaine de plus.
