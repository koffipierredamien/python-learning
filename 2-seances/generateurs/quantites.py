# -*- coding: utf-8 -*-
import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GAB = u"""# 🖨️ Ce qu'il faut imprimer pour la séance {num} ({date})

| Quantité | Document | Format | Papier |
|---|---|---|---|
| **8** (1 par poste) | [`1-aide-memoire.pdf`](1-aide-memoire.pdf) | A4 portrait, **recto** | ordinaire |
{extra}
**L'aide-mémoire est à eux** : ils écrivent dessus, ils le gardent dans leur chemise.
{note_aide}

> **Si vous ne pouvez pas imprimer :** l'aide-mémoire **se projette** (il est repris sur les
> dernières diapos de `a-projeter/seance-{num}-projection.pptx`). On perd le papier, pas le fond.

## Sur chaque poste, avant leur arrivée

- le dossier `GEEKS` à jour ;
- `GEEKS/mon_xo/jeu.py` = [`code/depart_eleves.py`](../code/depart_eleves.py) ;
- `GEEKS/xo_officiel/` **fermé** jusqu'à la fin de la séance : c'est **Le Filet**.

## Au tableau, avant leur arrivée — et on n'efface pas

```
{tableau}
```

## Le matériel non imprimé

| Quantité | Quoi |
|---|---|
{materiel}
"""

S = [
 dict(num=6, date="17 octobre",
   extra="",
   note_aide="**Le bandeau du bas — « ce que ton jeu sait faire » — se coche en fin de séance, tous ensemble.**",
   tableau="""la case du joueur :  1  2  3  4  5  6  7  8  9
l'indice Python   :  0  1  2  3  4  5  6  7  8

            indice = case - 1""",
   materiel=[("1 jeu", "**Neuf cartons numérotés 1 à 9** et neuf étiquettes `0` à `8` à coller dessous — la liste se montre **avec les mains** avant de se taper"),
             ("1", "Minuteur visible"),
             ("1", "Une **clé USB** avec le dossier `GEEKS` à jour, au cas où un poste refuserait de démarrer")]),

 dict(num=7, date="24 octobre",
   extra="",
   note_aide="",
   tableau="""une case est LIBRE  =  elle contient encore son numéro

      plateau[case - 1] == str(case)""",
   materiel=[("1 jeu", "Les **neuf cartons** de la séance 6 — on y repose un X dessus, et on relit ce que contient la case"),
             ("1", "Minuteur visible"),
             ("8", "Les aide-mémoires de la **séance 6** : ils restent sur les postes, on y revient tout le temps")]),

 dict(num=9, date="7 novembre",
   extra="",
   note_aide="",
   tableau="""and   ->  il faut TOUT
or    ->  il suffit d'UN

if case >= 1 and case <= 9 and plateau[case - 1] == str(case):""",
   materiel=[("1", "Minuteur visible"),
             ("1", "**Le tableau coupé en deux** : l'ancien code (séance 7) à gauche, le nouveau à droite. On ne l'efface pas avant la fin"),
             ("—", "**Lisez le Journal du TP n°2 la veille** : si moins de la moitié a compris `case - 1`, la séance commence par 5 minutes de rappel")]),

 dict(num=10, date="14 novembre",
   extra="",
   note_aide="**C'est la séance la plus importante des deux mois.** L'aide-mémoire porte le squelette de la boucle : ils le recopient de là.",
   tableau="""while  ...  :        tant que c'est vrai, on recommence
                     et tout ce qui se répète est DÉCALÉ

Ctrl + C   =   arrêter un programme devenu fou""",
   materiel=[("1", "Minuteur visible"),
             ("1", "**Un objet à faire tourner** (un dé, une balle) : la boucle se mime avant de s'écrire"),
             ("—", "Prévoyez d'écrire **Ctrl + C** en très grand : au moins un poste partira en boucle infinie, et c'est une bonne nouvelle")]),

 dict(num=11, date="21 novembre",
   extra="",
   note_aide="🔴 **Celui-ci est différent : il contient le bloc des 8 `if`, écrit en entier.** Ils le recopient depuis la feuille — c'est prévu, et c'est le seul moyen de tenir dans l'heure.",
   tableau="""les indices, pas les numéros de case :

        0 | 1 | 2
       ---+---+---
        3 | 4 | 5
       ---+---+---
        6 | 7 | 8

while tour < 9 and gagnant == "" :  deux raisons de s'arrêter""",
   materiel=[("1", "Minuteur visible"),
             ("1 jeu", "Les **neuf cartons**, pour montrer les 8 lignes gagnantes à la main avant de les écrire"),
             ("8", "Une **feuille blanche par élève** : ils écrivent les 8 lignes gagnantes avant de taper quoi que ce soit")]),
]

for s in S:
    mat = "\n".join("| **%s** | %s |" % (a, b) for a, b in s["materiel"])
    txt = GAB.format(num=s["num"], date=s["date"], extra=s["extra"],
                     note_aide=s["note_aide"], tableau=s["tableau"], materiel=mat)
    dossier = {6: "S06-le-plateau-se-souvient", 7: "S07-la-case-occupee", 9: "S09-et-ou",
               10: "S10-la-boucle", 11: "S11-le-gagnant"}[s["num"]]
    chemin = os.path.join(BASE, dossier, "a-imprimer", "quantites-et-formats.md")
    open(chemin, "w", encoding="utf-8").write(txt)
    print("écrit :", chemin)
