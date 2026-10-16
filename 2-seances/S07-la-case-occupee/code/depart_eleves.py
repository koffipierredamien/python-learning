# =====================================================
#  JEU XO  -  Seance 7
#  ON NE JOUE PAS DEUX FOIS AU MEME ENDROIT
# =====================================================
#
#  1. F5 tout de suite : le jeu de samedi dernier marche.
#  2. Remplace les  ____  .
#  3. Relance apres CHAQUE changement.
#
#  >>> DEUX PARTIES. On attend l'explication entre les deux.
# =====================================================

print("===================================")
print("       BIENVENUE DANS LE JEU XO")
print("===================================")
print("Cree par : les Jeremiah Geeks")
print("")

joueur1 = input("Joueur 1, quel est ton nom ? ")
joueur2 = input("Joueur 2, quel est ton nom ? ")
print("")
print(joueur1 + " joue les X")
print(joueur2 + " joue les O")
print("")

plateau = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])
print("")


# -----------------------------------------------------
#  PARTIE 1 : le jeu verifie que la case est LIBRE
# -----------------------------------------------------

case = input(joueur1 + ", quelle case veux-tu jouer ? ")
case = int(case)

# ETAPE 1 : complete le IF DANS LE IF.
#           Une case est LIBRE si elle contient encore son
#           numero. Le numero, en texte, c'est  str(case) .
#
#           Compte bien les espaces :
#              4 espaces pour le premier niveau
#              8 espaces pour le deuxieme
if case > 9:
    print("La case " + str(case) + " n'existe pas ! Choisis entre 1 et 9.")
else:
    if plateau[case - 1] == ____(case):
        plateau[case - 1] = "____"
        print(joueur1 + " pose un X sur la case " + str(case) + ".")
    else:
        print("La case " + str(case) + " est deja prise ! Tu perds ton tour.")

print("")
print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])
print("")

#  >>> TESTE LES TROIS CHEMINS avant d'appeler :
#      une case libre (5), la meme case (5), une case folle (12).
#  >>> CARTE VERTE, et on attend.


# -----------------------------------------------------
#  PARTIE 2 : le tour du joueur 2
# -----------------------------------------------------

# ETAPE 2 : recopie TOUT le bloc de la partie 1 ici, et change
#           trois choses : joueur1 -> joueur2, le "X" -> "O",
#           et le mot "pose un X" -> "pose un O".



# ETAPE 3 : recopie encore les cinq lignes d'affichage, a la fin.



# =====================================================
#  TU AS FINI ? LEVE LA CARTE BLEUE.
#
#  DEFI 1 : ajoute un troisieme tour, pour le joueur 1.
#
#  DEFI 2 : compte les coups REELLEMENT poses (un compteur
#           tour, qui n'augmente que dans le bon if) et
#           affiche-le a la fin.
#
#  DEFI 3 : le bug du zero. Lance le jeu et tape 0.
#           Que se passe-t-il ? Ecris ce que tu observes
#           sur un papier : on le reparera samedi prochain.
# =====================================================
