# -*- coding: utf-8 -*-
"""
=============================================================================
  SEANCE 9  -  LE LIVE CODING DE L'ENSEIGNANT
  "Une seule question au lieu de trois"
=============================================================================
  LE PROBLEME A POSER EN PREMIER :

     Projetez le code de la seance 7, et tapez 0 devant eux.
     Le symbole se pose dans la case 9. "Vous aviez trouve ce bug.
     Aujourd'hui, on le repare -- et le code va RETRECIR."

     12 h 22 - 12 h 32   etape A  -> and, la table a deux colonnes
     12 h 32 - 12 h 40   etape B  -> or
     12 h 40 - 12 h 52   etape C  -> on fusionne le if dans le if
     12 h 52 - 13 h      atelier 1 : le videur du club
     13 h 10 - 13 h 50   atelier 2 : le projet
=============================================================================
"""

# =============================================================================
#  ETAPE A  (10 min)  -  and  :  LES DEUX, EN MEME TEMPS
# =============================================================================
#  AU TABLEAU, SANS MACHINE. Prenez un exemple de la vraie vie :
#    "Pour entrer au camp, il faut avoir son cahier ET son stylo.
#     Si tu n'as que le cahier ? Tu n'entres pas."

print(True and True)      # True
print(True and False)     # False
print(False and True)     # False
print(False and False)    # False

#  >>> AVANT DE LANCER : faites-leur dire les quatre resultats.
#    "Avec and, il faut que TOUT soit vrai. Un seul faux, et c'est faux."

age = 14
print(age >= 12 and age <= 18)      # True  : il est bien entre 12 et 18

#    "Deux questions dans la meme phrase. C'est exactement ce qu'il
#     nous manquait pour dire 'entre 1 et 9'."


# =============================================================================
#  ETAPE B  (8 min)  -  or  :  IL SUFFIT D'UN SEUL
# =============================================================================
print(True or False)      # True
print(False or False)     # False

#    "Pour avoir un gouter, il faut avoir fini son exercice OU avoir
#     aide un voisin. Un des deux suffit."
#
#  LE TABLEAU A LAISSER AU TABLEAU TOUTE LA SEANCE :
#       and  ->  il faut TOUT
#       or   ->  il suffit d'UN


# =============================================================================
#  ETAPE C  (12 min)  -  ON FUSIONNE  (le moment de la seance)
# =============================================================================
#  Ecrivez l'ANCIEN code a gauche du tableau, le NOUVEAU a droite.
#
#     AVANT (seance 7)                  APRES (aujourd'hui)
#     if case > 9:                      if case >= 1 and case <= 9 and ...:
#         refus                             pose
#     else:                             else:
#         if libre:                         refus
#             pose
#         else:
#             refus
#     7 lignes, 2 niveaux               4 lignes, 1 niveau

plateau = ["1", "2", "3", "4", "X", "6", "7", "8", "9"]
case = 3

if case >= 1 and case <= 9 and plateau[case - 1] == str(case):
    plateau[case - 1] = "O"
    print("Pose !")
else:
    print("Coup impossible.")

#  >>> TESTEZ LES QUATRE CAS DEVANT EUX, dans cet ordre :
#        case = 3   -> pose
#        case = 5   -> refus (deja prise)
#        case = 12  -> refus (trop grand)
#        case = 0   -> refus  <-- LE BUG EST MORT. Marquez le coup.
#
#    "Vous venez d'ecrire moins de code, et votre jeu fait PLUS de
#     choses. C'est ca, programmer : quand ca rallonge tout le temps,
#     c'est souvent qu'il manque une idee."
#
#  LES ERREURS QUI VONT ARRIVER
#   SyntaxError ............. "and" oublie entre deux conditions
#   La condition est toujours fausse  >= et <= inverses
#   NameError ............... "AND" en majuscules, ou "et"
#   Le bug du zero revient .. le  case >= 1  a ete oublie
# =============================================================================
