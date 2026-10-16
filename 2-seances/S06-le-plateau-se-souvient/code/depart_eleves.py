# =====================================================
#  JEU XO  -  Seance 6
#  LE PLATEAU SE SOUVIENT
# =====================================================
#
#  COMMENT FAIRE :
#  1. Appuie tout de suite sur F5 : le programme de
#     samedi dernier marche deja.
#  2. Remplace chaque  ____  par ce qu'on te demande.
#  3. Relance apres CHAQUE changement. Toujours.
#
#  >>> TROIS PARTIES. On attend l'explication avant
#      de passer a la suivante.
# =====================================================

print("===================================")
print("       BIENVENUE DANS LE JEU XO")
print("===================================")
print("Cree par : ____")                  # ETAPE 1 : ton prenom
print("")

joueur1 = input("Joueur 1, quel est ton nom ? ")
joueur2 = input("Joueur 2, quel est ton nom ? ")
print("")
print(joueur1 + " joue les X")
print(joueur2 + " joue les O")
print("")


# -----------------------------------------------------
#  PARTIE 1 : le plateau devient une LISTE
# -----------------------------------------------------

# ETAPE 2 : complete la liste. Neuf cases, de "1" a "9".
#           Attention : chaque numero est entre guillemets.
plateau = ["1", "2", "3", "4", "____", "____", "____", "____", "____"]

# ETAPE 3 : complete l'affichage. La premiere case de la
#           liste est plateau[0], pas plateau[1] !
print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[____] + " | " + plateau[____])
print("---+---+---")
print(" " + plateau[____] + " | " + plateau[____] + " | " + plateau[____])
print("")

#  >>> CARTE VERTE, et on attend.


# -----------------------------------------------------
#  PARTIE 2 : le joueur pose son symbole
# -----------------------------------------------------

case = input(joueur1 + ", quelle case veux-tu jouer ? ")

# ETAPE 4 : transforme la reponse en nombre (comme d'habitude).
case = ____(case)

# ETAPE 5 : LA LIGNE DE LA SEANCE.
#           Range "X" dans la case choisie.
#           Souviens-toi : la case 1 est a l'indice 0,
#           donc l'indice, c'est  case - 1 .
plateau[____] = "X"

#  >>> CARTE VERTE, et on attend.


# -----------------------------------------------------
#  PARTIE 3 : on regarde si le plateau a change
# -----------------------------------------------------

# ETAPE 6 : recopie ici les CINQ lignes d'affichage de
#           l'etape 3. Oui, on recopie. On apprendra
#           bientot a ne plus le faire.
print("")



print("")
print("Le X de " + joueur1 + " est reste sur le plateau !")


# =====================================================
#  TU AS FINI ? LEVE LA CARTE BLEUE.
#
#  DEFI 1 : fais poser aussi le O du joueur 2,
#           puis reaffiche le plateau une troisieme fois.
#
#  DEFI 2 : au lieu de "X", mets le prenom du joueur 1
#           dans la case. Que se passe-t-il avec le
#           dessin du plateau ? Explique pourquoi.
# =====================================================
