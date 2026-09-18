# =====================================================
#  JEU XO  -  Seance 2  -  PISTE BLEUE
#  Mon ecran d'accueil, et le jeu qui demande ton nom
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
# =====================================================


# -----------------------------------------------------
#  PARTIE 1 : l'ecran d'accueil. Il est deja ecrit.
#             Tu changes seulement la ligne du createur.
# -----------------------------------------------------

print("===================================")
print("       BIENVENUE DANS LE JEU XO")
print("===================================")

# ETAPE 1 : remplace  ____  par TON PRENOM
print("Cree par : ____")

print("")
print(" . | . | .")
print("---+---+---")
print(" . | . | .")
print("---+---+---")
print(" . | . | .")
print("")


# -----------------------------------------------------
#  PARTIE 2 : le jeu va te poser une question.
#             C'est la nouveaute d'aujourd'hui.
# -----------------------------------------------------

# ETAPE 2 : remplace  ____  par la question que le jeu doit poser.
#           Par exemple :   Comment t'appelles-tu ?
#           ATTENTION : garde bien l'espace avant le dernier guillemet,
#           c'est plus joli quand le joueur tape sa reponse.
nom = input("____ ")

# ETAPE 3 : cette ligne marche deja. N'y touche pas.
#           Elle affiche le nom que le joueur vient de taper.
print("Bonjour " + nom + " !")

# ETAPE 4 : ecris ce que tu veux dire au joueur.
#           Par exemple :   Prepare-toi a perdre
print("____ " + nom + " !")


# =====================================================
#  TU AS FINI ? LEVE LA CARTE BLEUE.
#  Le defi en plus : demande AUSSI son age au joueur,
#  et affiche-le.   age = input("Quel age as-tu ? ")
# =====================================================
