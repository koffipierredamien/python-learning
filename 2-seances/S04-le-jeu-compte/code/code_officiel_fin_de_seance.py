# =====================================================
#  JEU XO  -  CODE OFFICIEL
#  Fin de la seance 4 : "Le jeu verifie et compte"
#
#  Ce fichier est le point de depart de la seance 5.
#  Chaque eleve en recoit une copie en arrivant,
#  quoi qu'il ait reussi ou rate la semaine precedente.
#
#  Notions de la seance :
#     int() et str()      le texte et les nombres
#     tour = tour + 1     le compteur
#     if / else           la decision
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

print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 ")
print("")

tour = 0

# --- tour du joueur 1 -------------------------------
case = input(joueur1 + ", quelle case veux-tu jouer ? ")
case = int(case)

if case > 9:
    print("La case " + str(case) + " n'existe pas ! Choisis entre 1 et 9.")
else:
    tour = tour + 1
    print(joueur1 + " joue la case " + str(case) + "   (tour numero " + str(tour) + ")")
print("")

# --- tour du joueur 2 -------------------------------
case = input(joueur2 + ", quelle case veux-tu jouer ? ")
case = int(case)

if case > 9:
    print("La case " + str(case) + " n'existe pas ! Choisis entre 1 et 9.")
else:
    tour = tour + 1
    print(joueur2 + " joue la case " + str(case) + "   (tour numero " + str(tour) + ")")
print("")

print("Coups valides joues : " + str(tour))
print("Il reste " + str(9 - tour) + " cases libres.")

# =====================================================
#  SEANCE 5 : le plateau va se souvenir des coups joues.
# =====================================================
