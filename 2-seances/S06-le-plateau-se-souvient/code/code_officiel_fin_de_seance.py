# =====================================================
#  JEU XO  -  CODE OFFICIEL
#  Fin de la seance 6 : "Le plateau se souvient"
#
#  Point de depart de la seance 7.
#  Chaque eleve en recoit une copie en arrivant.
#
#  Notion de la seance :
#     la LISTE     plateau = ["1", "2", ... , "9"]
#     l'INDICE     plateau[0] est la premiere case
#     la POSE      plateau[case - 1] = "X"
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

# --- LE PLATEAU EST UNE LISTE DE 9 CASES -------------
#  Au depart, chaque case contient son propre numero.
#  C'est pratique : le joueur voit les numeros libres.
plateau = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])
print("")

# --- LE JOUEUR 1 POSE SON SYMBOLE --------------------
case = input(joueur1 + ", quelle case veux-tu jouer ? ")
case = int(case)

plateau[case - 1] = "X"        # <-- LA LIGNE DE LA SEANCE
                               #     case 1 -> plateau[0]

print("")
print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])
print("")

print("Le X de " + joueur1 + " est reste sur le plateau !")

# =====================================================
#  SEANCE 7 : le jeu refusera une case deja prise.
# =====================================================
