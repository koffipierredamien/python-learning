# =====================================================
#  JEU XO  -  Seance 4  -  PISTE BLEUE
#  Le jeu compte les tours
# =====================================================
#
#  COMMENT FAIRE :
#  1. Appuie tout de suite sur F5. Le programme marche deja :
#     c'est celui de samedi dernier.
#  2. Ensuite, remplace chaque  ____  par ce qu'on te demande.
#  3. Relance apres CHAQUE changement. Toujours.
#
#  >>> ON NE FAIT LA PARTIE 2 QU'APRES L'EXPLICATION DU PROFESSEUR.
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


#  >>> ARRETE-TOI ICI. Carte VERTE si ca marche, et attends.


# -----------------------------------------------------
#  PARTIE 2 : le jeu demande une case, et compte
# -----------------------------------------------------

# ETAPE 3 : le compteur part de zero.
tour = ____

# --- tour du joueur 1 --------------------------------
case = input(joueur1 + ", quelle case veux-tu jouer ? ")

# ETAPE 4 : le joueur a tape du TEXTE. Transforme-le en NOMBRE.
case = ____(case)

# ETAPE 5 : ajoute 1 au compteur.
tour = ____ + 1

print(joueur1 + " joue la case " + str(case) + "   (tour numero " + str(tour) + ")")
print("")

# --- tour du joueur 2 --------------------------------
# ETAPE 6 : recopie les quatre lignes du joueur 1, en remplacant
#           joueur1 par joueur2. Le compteur, lui, continue : il ne
#           repart PAS de zero.


# ETAPE 7 : affiche combien de cases restent libres.
#           Il y en a 9 au depart, et on en a joue "tour".
print("Il reste " + str(9 - ____) + " cases libres.")


# =====================================================
#  TU AS FINI ? LEVE LA CARTE BLEUE.
#  Le defi en plus : demande leur age aux deux joueurs,
#  et affiche lequel est le plus age.
# =====================================================
