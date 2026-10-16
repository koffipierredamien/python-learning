# =====================================================
#  JEU XO  -  CODE OFFICIEL
#  Fin de la seance 7 : "On ne joue pas deux fois
#                        au meme endroit"
#
#  Point de depart de la seance 8 (le TP n°2).
#
#  Notion de la seance :
#     le IF DANS LE IF
#     une case est LIBRE si elle contient encore son numero :
#         plateau[case - 1] == str(case)
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


# --- TOUR DU JOUEUR 1 --------------------------------
case = input(joueur1 + ", quelle case veux-tu jouer ? ")
case = int(case)

if case > 9:
    print("La case " + str(case) + " n'existe pas ! Choisis entre 1 et 9.")
else:
    if plateau[case - 1] == str(case):
        plateau[case - 1] = "X"
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


# --- TOUR DU JOUEUR 2 --------------------------------
case = input(joueur2 + ", quelle case veux-tu jouer ? ")
case = int(case)

if case > 9:
    print("La case " + str(case) + " n'existe pas ! Choisis entre 1 et 9.")
else:
    if plateau[case - 1] == str(case):
        plateau[case - 1] = "O"
        print(joueur2 + " pose un O sur la case " + str(case) + ".")
    else:
        print("La case " + str(case) + " est deja prise ! Tu perds ton tour.")

print("")
print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])

# =====================================================
#  CE QUI NE MARCHE PAS ENCORE, ET C'EST VOULU :
#  si le joueur tape 0, le programme accepte.
#  On le reparera a la seance 9, avec le mot  or .
#
#  SEANCE 8 : TP n°2, on consolide tout ca.
# =====================================================
