# -*- coding: utf-8 -*-
"""
=============================================================================
  SEANCE 7  -  LE LIVE CODING DE L'ENSEIGNANT
  "On ne joue pas deux fois au meme endroit"
=============================================================================
  LE PROBLEME A POSER EN PREMIER :

     Lancez le jeu de la seance 6 devant eux. Faites jouer la case 5
     au joueur 1... puis la case 5 au joueur 2.
     "Le O a mange le X. Est-ce qu'on a le droit, au morpion ?"

     12 h 22 - 12 h 32   etape A    -> comment savoir si une case est libre
     12 h 32 - 12 h 45   etapes B,C -> le if dans le if
     12 h 45 - 13 h      atelier 1 : le videur de la case
     13 h 10 - 13 h 50   atelier 2 : le projet
=============================================================================
"""

# =============================================================================
#  ETAPE A  (10 min)  -  COMMENT SAVOIR QU'UNE CASE EST LIBRE ?
# =============================================================================
#  LAISSEZ-LES CHERCHER DEUX MINUTES, VRAIMENT. Ils proposeront
#  "si la case est vide" -- mais elle n'est jamais vide : elle contient
#  son numero. C'est la toute l'astuce :
#
#      case libre   ->  plateau[case - 1] contient ENCORE son numero
#      case prise   ->  plateau[case - 1] contient "X" ou "O"

plateau = ["1", "2", "3", "4", "X", "6", "7", "8", "9"]

case = 3
print(plateau[case - 1] == str(case))      # True  : la case 3 est libre

case = 5
print(plateau[case - 1] == str(case))      # False : la case 5 est prise

#    "str(case) transforme le nombre 3 en texte "3", pour pouvoir le
#     comparer avec ce qu'il y a dans la case, qui est du texte."


# =============================================================================
#  ETAPE B  (8 min)  -  LE IF DANS LE IF
# =============================================================================
#  AU TABLEAU D'ABORD, EN FRANCAIS, avec les decalages :
#
#      si la case n'existe pas :
#          je refuse
#      sinon :
#          si la case est libre :
#              je pose
#          sinon :
#              je refuse aussi, mais pas pour la meme raison
#
#  "Deux questions, l'une DANS l'autre. La deuxieme ne se pose que si
#   la reponse a la premiere est non."

case = 3
if case > 9:
    print("La case n'existe pas !")
else:
    if plateau[case - 1] == str(case):
        plateau[case - 1] = "X"
        print("Pose !")
    else:
        print("Deja prise !")

#  >>> LE GESTE A MONTRER : passez le doigt le long des decalages
#      sur l'ecran. 4 espaces, puis 8. Le decalage dit QUI est dans QUI.


# =============================================================================
#  ETAPE C  (5 min)  -  L'ERREUR VOLONTAIRE
# =============================================================================
#  Effacez les 4 espaces du deuxieme if :
#
#       else:
#       if plateau[case - 1] == str(case):     <-- IndentationError
#
#    "Il attend un bloc decale apres le else. Le deuxieme if DOIT etre
#     dans le premier, sinon il ne veut rien dire."


# =============================================================================
#  CE QU'ON NE REPARE PAS AUJOURD'HUI, ET ON LE DIT
# =============================================================================
#  Tapez 0 devant eux. Le programme accepte, et le symbole se pose
#  dans la derniere case (plateau[-1], la case 9).
#
#    "Vous avez trouve un vrai bug. Pour le reparer proprement, il
#     faudrait poser DEUX questions en meme temps : 'plus grand que 0
#     ET plus petit que 10'. Ce mot-la, ET, on l'apprend dans deux
#     semaines. Notez le bug, on y revient."
#
#  >>> C'est la promesse de la seance 9. Tenez-la.
#
#  LES ERREURS QUI VONT ARRIVER
#   IndentationError ........ le deuxieme if non decale
#   La case se pose quand meme  le eleve a mis la pose HORS du if
#   TypeError ............... str(case) oublie dans la comparaison
#   Le message s'affiche deux fois  un print en trop, hors du else
# =============================================================================
