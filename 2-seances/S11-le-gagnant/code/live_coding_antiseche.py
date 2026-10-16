# -*- coding: utf-8 -*-
"""
=============================================================================
  SEANCE 11  -  LE LIVE CODING DE L'ENSEIGNANT
  "Le jeu sait qui gagne"      >>>  LE JEU EST FINI AUJOURD'HUI  <<<
=============================================================================
  LE PROBLEME A POSER EN PREMIER :

     Faites une partie devant eux avec le jeu de la seance 10.
     Alignez trois X. Continuez a jouer. Le jeu continue betement.
     "Il ne voit rien. Aujourd'hui, on lui apprend a regarder."

     12 h 22 - 12 h 35   etapes A, B  -> comment voir une ligne
     12 h 35 - 12 h 50   etape C      -> les huit lignes, et la boite gagnant
     12 h 50 - 13 h      etape D      -> arreter la boucle
     13 h 10 - 13 h 50   atelier : le projet, et UNE VRAIE PARTIE
=============================================================================
"""

# =============================================================================
#  ETAPE A  (7 min)  -  QU'EST-CE QUE GAGNER ?
# =============================================================================
#  AU TABLEAU, dessinez la grille avec les INDICES, pas les numeros :
#
#         0 | 1 | 2
#        ---+---+---
#         3 | 4 | 5
#        ---+---+---
#         6 | 7 | 8
#
#  Puis demandez : "donnez-moi toutes les facons de gagner."
#  Laissez-les chercher. Ils en trouveront 6 ou 7. Comptez ensemble :
#       3 lignes  +  3 colonnes  +  2 diagonales  =  8

plateau = ["X", "X", "X", "4", "O", "6", "O", "8", "9"]

#  La question a se poser pour la premiere ligne :
print(plateau[0] == plateau[1] and plateau[1] == plateau[2])   # True

#    "Si les trois cases contiennent la meme chose, c'est gagne.
#     Et on n'a pas besoin de savoir si c'est X ou O : on regarde
#     juste si c'est PAREIL."


# =============================================================================
#  ETAPE B  (6 min)  -  POURQUOI CA NE SE DECLENCHE PAS TOUT SEUL
# =============================================================================
#  LA QUESTION QU'UN ELEVE VA POSER : "et les cases vides ?"
plateau2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
print(plateau2[0] == plateau2[1] and plateau2[1] == plateau2[2])   # False

#    "Une case libre contient son NUMERO. "1", "2", "3" ne seront
#     jamais pareils. C'est pour ca qu'on a choisi les numeros au
#     depart, a la seance 6 : ils nous servent encore aujourd'hui."


# =============================================================================
#  ETAPE C  (15 min)  -  LES HUIT LIGNES, ET LA BOITE  gagnant
# =============================================================================
gagnant = ""

if plateau[0] == plateau[1] and plateau[1] == plateau[2]:
    gagnant = plateau[0]
#  ... et les sept autres, sur le meme modele.

print("gagnant = " + gagnant)

#  >>> TAPEZ LES DEUX PREMIERS DEVANT EUX, lentement, en nommant les
#      indices a voix haute. Les six autres, ILS les recopient de la
#      feuille : c'est long, et c'est normal. Dites-le :
#
#    "Oui, huit fois presque la meme chose. Il y a une facon
#     d'ecrire ca en trois lignes -- on l'apprendra. Aujourd'hui,
#     on veut surtout que le jeu MARCHE."


# =============================================================================
#  ETAPE D  (10 min)  -  LA BOUCLE S'ARRETE
# =============================================================================
#     while tour < 9 and gagnant == "":
#
#    "Deux raisons d'arreter : le plateau est plein, OU quelqu'un a
#     gagne. Tant que les DEUX sont vraies, on continue."
#
#  >>> MONTREZ LE PIEGE : si on ecrit  gagnant = ""  DANS la boucle,
#      le gagnant est efface a chaque tour et la partie ne s'arrete
#      jamais. La boite se cree UNE SEULE FOIS, avant le while.
#
#  LES ERREURS QUI VONT ARRIVER
#   La partie ne s'arrete pas .... gagnant remis a "" dans la boucle
#   Le gagnant est "5" ........... le bloc des 8 if est AVANT la pose
#   IndentationError ............. les 8 if mal decales (ils sont DANS le if)
#   SyntaxError .................. un  and  oublie entre deux comparaisons
#   Toujours match nul ........... le bloc des 8 if est apres la boucle
#
#  >>> LE MOMENT DE LA SEANCE : faites jouer deux eleves devant la
#      classe, sur le jeu qu'ils viennent d'ecrire. Laissez-les
#      applaudir le gagnant. C'est aussi ca, le travail.
# =============================================================================
