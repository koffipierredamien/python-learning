# -*- coding: utf-8 -*-
"""
=============================================================================
  SEANCE 4  -  LE LIVE CODING DE L'ENSEIGNANT
=============================================================================
  DEUX DEMONSTRATIONS, DEUX ATELIERS :

     12 h 25 - 12 h 40   etapes A, B, C   ->  texte ou nombre ? int()
     12 h 40 - 13 h      les eleves font la calculatrice d'age
     13 h 10 - 13 h 25   etapes D, E      ->  le compteur de tours
     13 h 25 - 13 h 50   les eleves font le projet

  REGLE D'OR : "JE CODE, VOUS PREDISEZ."
  Avant CHAQUE execution, on demande a la classe ce qui va s'afficher.

  AVANT LA SEANCE : police de Thonny en taille 18 minimum.
=============================================================================
"""

# =============================================================================
#  ETAPE A  (4 min)  -  input() REND TOUJOURS DU TEXTE
# =============================================================================
#  Vous tapez devant eux :

age = input("Quel age as-tu ? ")
print(age)

#  Ca marche. Tout le monde est content. Puis vous ajoutez UNE ligne :
#
#  >>> AVANT DE LANCER : "qu'est-ce qui va s'afficher ? 25 ? ou autre chose ?"

#  print(age + 10)        <-- a taper devant eux : ERREUR ROUGE
#
#    "TypeError. Il dit : can only concatenate str to str.
#     str, c'est string : du TEXTE. Il me dit qu'il ne sait pas ajouter
#     un nombre a du texte.
#     Pourtant j'ai tape 15 ! Oui... mais input rend TOUJOURS du texte.
#     Meme quand vous tapez un nombre. C'est LA chose a retenir aujourd'hui."


# =============================================================================
#  ETAPE B  (4 min)  -  int() : LE TRADUCTEUR
# =============================================================================
#     "Il existe un mot pour dire : traite ca comme un NOMBRE. C'est int."

age = input("Quel age as-tu ? ")
age = int(age)
print(age + 10)

#  >>> AVANT DE LANCER : "et maintenant, ca va marcher ?"
#
#    "int, c'est integer : nombre entier. La boite contenait du texte,
#     maintenant elle contient un nombre. Et avec un nombre, on peut calculer."
#
#  Montrez la ligne 'age = int(age)' et dites-la a voix haute :
#     "range dans age, la version NOMBRE de ce qu'il y a dans age."


# =============================================================================
#  ETAPE C  (3 min)  -  L'ERREUR VOLONTAIRE DU JOUR
# =============================================================================
#  Vous relancez le meme programme, et vous tapez  douze  au lieu de  12.
#
#    "ValueError. Il dit : invalid literal for int.
#     Traduction : je t'ai demande de transformer ca en nombre,
#     et tu m'as donne 'douze'. Je ne sais pas faire.
#     Retenez : int() ne marche que si ce qui est tape est bien un nombre."
#
#  >>> Ne cherchez pas a reparer : on verra comment se proteger plus tard.
#      Aujourd'hui, on constate, et on sait lire le message.


# =============================================================================
#  ETAPE D  (5 min)  -  LE COMPTEUR : tour = tour + 1
# =============================================================================
#  D'abord SANS machine, avec les mains :
#     "J'ai une boite 'tour'. Dedans, il y a 0.
#      Je prends ce qu'il y a dedans, j'ajoute 1, et je remets le tout
#      dans la MEME boite. Elle contient maintenant 1."

tour = 0
tour = tour + 1
print(tour)

#  >>> AVANT DE LANCER : "qu'est-ce qui s'affiche ? 0 ou 1 ?"
#
#  Puis vous ajoutez deux fois la meme ligne, et vous redemandez :

tour = tour + 1
tour = tour + 1
print(tour)

#    "La ligne est TOUJOURS la meme, et pourtant le resultat change a chaque
#     fois. C'est normal : elle ne dit pas 'tour egale 1'. Elle dit
#     'range dans tour, ce qu'il y a dans tour, PLUS un'.
#     Le signe = n'est pas 'egal'. C'est 'range dans'."
#
#  C'EST LE POINT LE PLUS IMPORTANT DE LA SEANCE. Allez lentement.


# =============================================================================
#  ETAPE E  (3 min)  -  AFFICHER UN NOMBRE DANS UNE PHRASE
# =============================================================================
#     "Attention : pour coller un nombre a du texte, il faut refaire
#      le chemin dans l'autre sens. str() : traite ca comme du texte."

tour = 3
print("Tour numero " + str(tour))

#  Montrez l'oubli une fois : print("Tour numero " + tour) -> TypeError.
#     "Le meme message rouge que tout a l'heure. Vous le connaissez
#      maintenant : il parle de texte et de nombre melanges."
#
#  >>> ET C'EST TOUT. On les envoie faire le projet.


# =============================================================================
#  LES ERREURS QUI VONT ARRIVER PENDANT LES ATELIERS
# =============================================================================
#   TypeError .......... un nombre colle a du texte sans str(),
#                        ou du texte utilise dans un calcul sans int().
#   ValueError ......... int() sur quelque chose qui n'est pas un nombre.
#                        "Qu'est-ce que tu as tape ? Relance et tape un chiffre."
#   Le compteur reste a 1 ... l'eleve a ecrit tour = 1 au lieu de tour = tour + 1.
#                        "Relis ta ligne a voix haute : range dans tour... quoi ?"
#
#  Le dictionnaire complet : 1-methode/annexes/dictionnaire-des-erreurs.pdf
# =============================================================================
