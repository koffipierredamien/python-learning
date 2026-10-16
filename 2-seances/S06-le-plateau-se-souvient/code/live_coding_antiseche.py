# -*- coding: utf-8 -*-
"""
=============================================================================
  SEANCE 6  -  LE LIVE CODING DE L'ENSEIGNANT
  "Le plateau se souvient"
=============================================================================
  LE PROBLEME A POSER EN PREMIER, AVANT TOUTE EXPLICATION :

     "Samedi dernier, Joyce a joue la case 5. Regardez le plateau...
      il n'a pas bouge. Votre jeu ne se SOUVIENT de rien.
      Aujourd'hui, on lui donne une memoire."

     12 h 22 - 12 h 40   etapes A, B, C   ->  la liste et l'indice
     12 h 40 - 12 h 55   atelier 1 : la liste de la classe
     13 h 05 - 13 h 20   etapes D, E      ->  poser un symbole
     13 h 20 - 13 h 50   atelier 2 : le projet

  REGLE D'OR : "JE CODE, VOUS PREDISEZ."
=============================================================================
"""

# =============================================================================
#  ETAPE A  (5 min)  -  UNE BOITE QUI CONTIENT PLUSIEURS CHOSES
# =============================================================================
#  AU TABLEAU D'ABORD, SANS MACHINE :
#    "Jusqu'ici, une boite = une chose. Aujourd'hui, une boite avec
#     NEUF COMPARTIMENTS. Ca s'appelle une LISTE."
#
#    Dessinez les neuf compartiments cote a cote, numerotes DESSOUS :
#         +---+---+---+---+---+---+---+---+---+
#         |"1"|"2"|"3"|"4"|"5"|"6"|"7"|"8"|"9"|
#         +---+---+---+---+---+---+---+---+---+
#           0   1   2   3   4   5   6   7   8     <- les INDICES

equipe = ["Joyce", "Gedeon", "Sarah"]
print(equipe[0])
print(equipe[2])

#  >>> AVANT DE LANCER : "qu'est-ce que print(equipe[0]) va afficher ?"
#      Beaucoup diront Gedeon. C'est LA confusion de la seance.
#    "L'ordinateur compte a partir de ZERO. Le premier est le numero 0."


# =============================================================================
#  ETAPE B  (5 min)  -  L'ERREUR VOLONTAIRE DU JOUR
# =============================================================================
#  Vous tapez devant eux :
#       print(equipe[3])        <-- IndexError: list index out of range
#
#    "Il dit : l'indice est HORS DE LA LISTE. Ma liste a trois noms,
#     donc les indices vont de 0 a 2. Le numero 3 n'existe pas."
#
#  >>> Faites-leur compter sur leurs doigts, a voix haute : 0, 1, 2.


# =============================================================================
#  ETAPE C  (6 min)  -  ON PEUT CHANGER UNE CASE
# =============================================================================
equipe[1] = "Ethan"
print(equipe)

#  >>> AVANT DE LANCER : "qui va disparaitre ?"
#    "Un compartiment, ca se vide et ca se remplit, comme une boite.
#     La difference, c'est qu'il y en a neuf dans la meme boite."


# =============================================================================
#  ETAPE D  (8 min)  -  LE PLATEAU DU JEU EST UNE LISTE
# =============================================================================
plateau = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])

#    "Le dessin n'est plus ecrit en dur : il est FABRIQUE a partir
#     de la liste. Si la liste change, le dessin change."
#
#  >>> Montrez-le : changez plateau[4] = "X" puis relancez l'affichage.


# =============================================================================
#  ETAPE E  (7 min)  -  LA LIGNE DE LA SEANCE  :  case - 1
# =============================================================================
#  AU TABLEAU, LES DEUX RANGEES, L'UNE SOUS L'AUTRE :
#       la case du joueur :   1  2  3  4  5  6  7  8  9
#       l'indice Python   :   0  1  2  3  4  5  6  7  8
#    "Toujours un de moins. Donc : indice = case - 1."

case = 5
plateau[case - 1] = "X"
print(plateau[4])

#  >>> LE PIEGE A MONTRER : plateau[case] au lieu de plateau[case - 1].
#      Le X se pose a cote. Faites-le exprès, laissez-les trouver.
#
#  LES ERREURS QUI VONT ARRIVER PENDANT L'ATELIER
#   IndexError .............. l'indice depasse : case 9 -> plateau[9] n'existe pas
#   Le X se pose a cote ..... case oubliee -1
#   TypeError ............... case est restee du texte : il manque int()
#   Le plateau ne change pas  l'eleve a recopie l'affichage AVANT la pose
# =============================================================================
