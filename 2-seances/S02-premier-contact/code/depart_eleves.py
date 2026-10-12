# =====================================================
#  JEU XO  -  Seance 2  -  PISTE BLEUE
#  1) Mon ecran d'accueil      2) Le jeu demande ton nom
# =====================================================
#
#  COMMENT FAIRE :
#  1. Appuie tout de suite sur le bouton vert  ou sur F5.
#     Le programme marche deja ! Regarde en bas.
#  2. Ensuite, remplace chaque  ____  par ce qu'on te demande.
#  3. Relance apres CHAQUE changement. Toujours.
#
#  Les lignes qui commencent par  #  sont des messages pour toi.
#  L'ordinateur, lui, ne les lit pas.
#
#  >>> ON FAIT LA PARTIE 1 MAINTENANT.
#  >>> LA PARTIE 2, SEULEMENT QUAND LE PROFESSEUR LE DIRA.
# =====================================================


# =====================================================
#  PARTIE 1  -  MON ECRAN D'ACCUEIL      (avec print)
# =====================================================

# ETAPE 1 : cette ligne marche deja. N'y touche pas.
print("===================================")


# ETAPE 2 : remplace  ____  par :   BIENVENUE DANS LE JEU XO
print("        ____")


# ETAPE 3 : cette ligne marche deja. N'y touche pas.
print("===================================")


# ETAPE 4 : remplace  ____  par TON PRENOM
print("Cree par : ____")


# ETAPE 5 : ces lignes dessinent le plateau du morpion.
#           N'y touche pas... sauf si tu veux essayer autre chose !
print("")
print(" . | . | .")
print("---+---+---")
print(" . | . | .")
print("---+---+---")
print(" . | . | .")
print("")


#  >>> ARRETE-TOI ICI. Leve la carte VERTE si ca marche.
#  >>> On attend le professeur pour la partie 2.


# =====================================================
#  PARTIE 2  -  LE JEU TE POSE UNE QUESTION   (avec input)
# =====================================================

# ETAPE 6 : remplace  ____  par la question que le jeu doit poser.
#           Par exemple :   Comment t'appelles-tu ?
#           ATTENTION : garde l'espace avant le dernier guillemet,
#           c'est plus joli quand le joueur tape sa reponse.
nom = input("____ ")


# ETAPE 7 : cette ligne marche deja. N'y touche pas.
#           Elle affiche le nom que le joueur vient de taper.
print("Bonjour " + nom + " !")


# ETAPE 8 : ecris ce que tu veux dire au joueur.
#           Par exemple :   Prepare-toi a perdre
print("____ " + nom + " !")


# =====================================================
#  TU AS FINI ? LEVE LA CARTE BLEUE.
#  Le defi en plus : demande AUSSI son age au joueur,
#  et affiche-le.   age = input("Quel age as-tu ? ")
# =====================================================
