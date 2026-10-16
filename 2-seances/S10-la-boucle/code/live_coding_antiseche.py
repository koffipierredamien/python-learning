# -*- coding: utf-8 -*-
"""
=============================================================================
  SEANCE 10  -  LE LIVE CODING DE L'ENSEIGNANT
  "Le jeu tourne tout seul"   <<<  LA SEANCE LA PLUS IMPORTANTE  >>>
=============================================================================
  LE PROBLEME A POSER EN PREMIER :

     Ouvrez leur fichier de la seance 9 et faites defiler lentement.
     "Deux tours. Pour en faire neuf, il faudrait recopier ce bloc
      sept fois de plus. Qui a envie ?"
     Laissez-les repondre. Puis :
     "Il y a un mot pour dire 'recommence'. On l'apprend maintenant."

     12 h 22 - 12 h 32   etape A  -> while, sans le jeu
     12 h 32 - 12 h 40   etape B  -> la boucle infinie (volontaire)
     12 h 40 - 12 h 52   etape C  -> l'alternance des joueurs
     12 h 52 - 13 h      atelier 1 : le compte a rebours
     13 h 10 - 13 h 50   atelier 2 : le projet
=============================================================================
"""

# =============================================================================
#  ETAPE A  (10 min)  -  while  :  TANT QUE
# =============================================================================
#  AU TABLEAU D'ABORD, en francais :
#       TANT QUE le nombre de tours est plus petit que 9 :
#           on joue un tour
#           on ajoute 1 au nombre de tours
#
#  "Le  while  pose sa question AVANT chaque tour. Si la reponse est
#   True, il fait le bloc. Puis il repose la MEME question. Et ainsi
#   de suite, jusqu'a ce que la reponse soit False."

tour = 0
while tour < 3:
    print("Tour numero " + str(tour))
    tour = tour + 1
print("Fini ! tour vaut " + str(tour))

#  >>> AVANT DE LANCER : "combien de lignes vont s'afficher ?"
#      Beaucoup diront 3 et se tromperont sur les numeros (0,1,2).
#      Faites-leur suivre la valeur de tour au tableau, a la craie.


# =============================================================================
#  ETAPE B  (8 min)  -  L'ERREUR VOLONTAIRE : LA BOUCLE SANS FIN
# =============================================================================
#  Vous effacez la ligne  tour = tour + 1  et vous relancez.
#  L'ecran se remplit sans fin.
#
#    "Regardez : il ne s'arretera JAMAIS. tour vaut toujours 0, donc
#     la question 'tour < 3' repond toujours oui."
#
#  >>> MONTREZ LE GESTE QUI SAUVE :  Ctrl + C  dans la zone du bas.
#      Faites-le faire a tout le monde, maintenant, sur leur poste.
#      Ils en auront besoin aujourd'hui, c'est certain.
#
#    "La ligne qui fait avancer le compteur n'est pas un detail :
#     c'est elle qui fait que la boucle se termine un jour."


# =============================================================================
#  ETAPE C  (12 min)  -  L'ALTERNANCE DES JOUEURS
# =============================================================================
#  LE PROBLEME : dans la boucle, c'est toujours le meme symbole.
#  LA SOLUTION : a la fin de chaque tour, on echange.

symbole = "X"
tour = 0
while tour < 4:
    print("C'est au tour de " + symbole)
    if symbole == "X":
        symbole = "O"
    else:
        symbole = "X"
    tour = tour + 1

#  >>> AVANT DE LANCER : "X, O, X, O ou X, X, X, X ?"
#
#    "C'est la meme idee que le compteur : on regarde ce qu'il y a
#     dans la boite, et on y remet autre chose."
#
#  DANS LE JEU, on echange DEUX choses en meme temps : le symbole ET
#  le nom du joueur. Les deux lignes vont ensemble, dans le meme if.
#
#  LES ERREURS QUI VONT ARRIVER  (elles arriveront toutes, preparez-vous)
#   La boucle ne s'arrete pas ... tour = tour + 1 oublie -> Ctrl + C
#   IndentationError ........... le bloc de la boucle mal decale
#   Le jeu ne demande qu'une case  tout le bloc n'est pas DANS la boucle
#   Toujours des X ............. l'alternance est hors du if, ou oubliee
#   Le tour avance sur un coup refuse  tour = tour + 1 mal place
#   Le plateau ne s'affiche qu'une fois  l'affichage est hors de la boucle
# =============================================================================
