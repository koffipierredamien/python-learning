# =====================================================
#  JEU XO  -  CODE OFFICIEL
#  Fin de la seance 11 : "Trois chemins au lieu de deux"
#
#  Notion de la seance :
#     elif   =   "sinon, si ..."
#
#  Le jeu ne dit plus "la case n'existe pas OU elle est
#  deja prise". Il dit LAQUELLE des deux. Le joueur sait
#  enfin ce qu'il a fait de travers.
#
#  LA REGLE D'OR :  Python s'arrete au PREMIER VRAI.
#  Les questions d'apres ne sont meme plus regardees.
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

#  TROIS CHEMINS, et un seul sera pris.
#  L'ORDRE COMPTE : on elimine d'abord le cas impossible,
#  ensuite le cas occupe, et ce qui reste est jouable.
if case < 1 or case > 9:
    print("   Cette case n'existe pas ! Choisis un numero entre 1 et 9.")
elif plateau[case - 1] != str(case):
    print("   Cette case est deja prise ! Choisis-en une autre.")
else:
    plateau[case - 1] = "X"
    print("   " + joueur1 + " pose un X sur la case " + str(case) + ".")

print("")
print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])
print("")


# --- TOUR DU JOUEUR 2  (le meme bloc, avec un O) -----
case = input(joueur2 + ", quelle case veux-tu jouer ? ")
case = int(case)

if case < 1 or case > 9:
    print("   Cette case n'existe pas ! Choisis un numero entre 1 et 9.")
elif plateau[case - 1] != str(case):
    print("   Cette case est deja prise ! Choisis-en une autre.")
else:
    plateau[case - 1] = "O"
    print("   " + joueur2 + " pose un O sur la case " + str(case) + ".")

print("")
print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])

# =====================================================
#  CE QUE LE JEU SAIT FAIRE MAINTENANT
#    - il accueille les deux joueurs
#    - il affiche le plateau, et il s'en souvient
#    - il refuse une case qui n'existe pas, EN LE DISANT
#    - il refuse une case deja prise, EN LE DISANT
#    - il pose le symbole quand le coup est bon
# =====================================================
