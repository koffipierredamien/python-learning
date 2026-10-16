# =====================================================
#  JEU XO  -  CODE OFFICIEL
#  Fin de la seance 9 : "Une seule question
#                        au lieu de trois"
#
#  Point de depart de la seance 10.
#
#  Notion de la seance :
#     and   les DEUX conditions doivent etre vraies
#     or    il suffit d'UNE des deux
#
#  Le if dans le if de la seance 7 a disparu :
#  une seule condition, et le bug du zero est repare.
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

#  UNE SEULE condition, trois questions reliees par  and  :
#     la case existe par en bas  ET  par en haut  ET  elle est libre
if case >= 1 and case <= 9 and plateau[case - 1] == str(case):
    plateau[case - 1] = "X"
    print(joueur1 + " pose un X sur la case " + str(case) + ".")
else:
    print("Coup impossible : la case n'existe pas, ou elle est deja prise.")

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

if case >= 1 and case <= 9 and plateau[case - 1] == str(case):
    plateau[case - 1] = "O"
    print(joueur2 + " pose un O sur la case " + str(case) + ".")
else:
    print("Coup impossible : la case n'existe pas, ou elle est deja prise.")

print("")
print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])

# =====================================================
#  SEANCE 10 : le jeu jouera les 9 tours TOUT SEUL.
#  On arretera enfin de recopier.
# =====================================================
