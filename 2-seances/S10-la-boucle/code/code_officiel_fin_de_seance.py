# =====================================================
#  JEU XO  -  CODE OFFICIEL
#  Fin de la seance 10 : "Le jeu tourne tout seul"
#
#  Point de depart de la seance 11.
#
#  Notion de la seance :
#     while   tant que la condition est vraie, on recommence
#
#  Le jeu joue les NEUF tours, et les joueurs alternent.
#  Ce fichier est plus COURT que celui de la semaine
#  derniere, et il fait quatre fois plus de choses.
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

tour = 0
symbole = "X"
joueur = joueur1

# --- LA BOUCLE : tant qu'il reste des cases ----------
while tour < 9:

    print("")
    print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
    print("---+---+---")
    print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
    print("---+---+---")
    print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])
    print("")

    case = input(joueur + " (" + symbole + "), quelle case ? ")
    case = int(case)

    if case >= 1 and case <= 9 and plateau[case - 1] == str(case):
        plateau[case - 1] = symbole
        tour = tour + 1

        # --- on passe la main a l'autre joueur -------
        if symbole == "X":
            symbole = "O"
            joueur = joueur2
        else:
            symbole = "X"
            joueur = joueur1
    else:
        print("Coup impossible : la case n'existe pas, ou elle est deja prise.")

# --- la boucle est finie : le plateau est plein ------
print("")
print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])
print("")
print("Le plateau est plein ! Neuf coups joues.")

# =====================================================
#  SEANCE 11 : le jeu dira QUI A GAGNE, et la partie
#  s'arretera des qu'il y a un vainqueur.
# =====================================================
