# =====================================================
#  JEU XO  -  Seance 4  -  PISTE BLEUE
#  Le jeu verifie et compte
# =====================================================
#
#  COMMENT FAIRE :
#  1. Appuie tout de suite sur F5. Le programme marche deja :
#     c'est celui de samedi dernier.
#  2. Remplace chaque  ____  par ce qu'on te demande.
#  3. Relance apres CHAQUE changement. Toujours.
#
#  >>> TROIS PARTIES. On n'attaque la suivante qu'apres l'explication.
# =====================================================

print("===================================")
print("       BIENVENUE DANS LE JEU XO")
print("===================================")
print("Cree par : ____")                       # ETAPE 1 : ton prenom
print("")

joueur1 = input("Joueur 1, quel est ton nom ? ")
joueur2 = input("Joueur 2, quel est ton nom ? ")
print("")
print(joueur1 + " joue les X")
print(joueur2 + " joue les O")
print("")


# -----------------------------------------------------
#  PARTIE 1 : le plateau porte des NUMEROS
# -----------------------------------------------------

# ETAPE 2 : remplace les points par les numeros 1 a 9,
#           en gardant les espaces exactement comme ils sont.
print(" . | . | . ")
print("---+---+---")
print(" . | . | . ")
print("---+---+---")
print(" . | . | . ")
print("")

#  >>> CARTE VERTE, et on attend.


# -----------------------------------------------------
#  PARTIE 2 : le jeu demande une case, et compte
# -----------------------------------------------------

# ETAPE 3 : le compteur part de zero.
tour = ____

case = input(joueur1 + ", quelle case veux-tu jouer ? ")

# ETAPE 4 : le joueur a tape du TEXTE. Transforme-le en NOMBRE.
case = ____(case)

# ETAPE 5 : ajoute 1 au compteur.
tour = ____ + 1

print(joueur1 + " joue la case " + str(case) + "   (tour numero " + str(tour) + ")")
print("")

#  >>> CARTE VERTE, et on attend.


# -----------------------------------------------------
#  PARTIE 3 : le jeu REFLECHIT avant d'accepter
# -----------------------------------------------------

# ETAPE 6 : remonte dans la PARTIE 2 et transforme-la comme ceci.
#           Attention aux deux-points et au decalage de 4 espaces !
#
#       if case > 9:
#           print("La case " + str(case) + " n'existe pas ! Choisis entre 1 et 9.")
#       else:
#           tour = tour + 1
#           print(joueur1 + " joue la case " + str(case) + "   (tour numero " + str(tour) + ")")
#
#  Teste les DEUX chemins : tape 5, puis relance et tape 12.


# ETAPE 7 : recopie tout le bloc pour le joueur 2.
#           Le compteur, lui, continue : il ne repart PAS de zero.


# ETAPE 8 : a la toute fin, affiche le bilan.
print("Coups valides joues : " + str(____))
print("Il reste " + str(9 - ____) + " cases libres.")


# =====================================================
#  TU AS FINI ? LEVE LA CARTE BLEUE.
#  Le defi en plus : et si le joueur tape 0, ou -3 ?
#  Ajoute un troisieme cas avec  elif case < 1:
# =====================================================
