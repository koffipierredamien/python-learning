# =====================================================================
#  TP n°2  -  CORRIGE DE L'ENSEIGNANT
#  "Le plateau vivant"  -  samedi 31 octobre 2026
#
#  Les cinq parties, puis les defis. Ce fichier tourne tel quel.
# =====================================================================


# =====================================================================
#  PARTIE 1  -  ECHAUFFEMENT : LES LISTES
# =====================================================================

# 1.1 - creer une liste et l'afficher en entier
equipe = ["Joyce", "Gedeon", "Sarah", "Ethan"]
print(equipe)

# 1.2 - afficher UN SEUL element (le premier est le numero 0)
print(equipe[0])
print(equipe[3])

# 1.3 - changer un element
equipe[1] = "Isaac"
print(equipe)

# 1.4 - l'erreur volontaire :  print(equipe[4])
#       -> IndexError: list index out of range
#       Une liste de 4 elements a les indices 0, 1, 2, 3.
print("")


# =====================================================================
#  PARTIE 2  -  L'INDICE : CASE - 1
# =====================================================================

cases = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# 2.1 - la case 1 est a l'indice 0
case = 1
print("La case " + str(case) + " est a l'indice " + str(case - 1))

# 2.2 - poser un symbole a la main, trois fois
cases[0] = "X"      # case 1
cases[4] = "O"      # case 5
cases[8] = "X"      # case 9
print(cases)

# 2.3 - poser avec la formule
case = 3
cases[case - 1] = "O"
print(cases[2])
print("")


# =====================================================================
#  PARTIE 3  -  LE PLATEAU QUI VIT
# =====================================================================

plateau = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])
print("")

plateau[4] = "X"

print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])
print("")


# =====================================================================
#  PARTIE 4  -  LE PROJET : QUATRE COUPS, SANS TRICHE
# =====================================================================

print("===================================")
print("       LE JEU XO  -  4 COUPS")
print("===================================")

joueur1 = input("Joueur 1, ton nom ? ")
joueur2 = input("Joueur 2, ton nom ? ")

plateau = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
tour = 0

# --- coup 1 : joueur 1 ----------------------------------------------
print("")
print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])

case = int(input(joueur1 + " (X), quelle case ? "))
if case > 9:
    print("Cette case n'existe pas !")
else:
    if plateau[case - 1] == str(case):
        plateau[case - 1] = "X"
        tour = tour + 1
    else:
        print("Case deja prise !")

# --- coup 2 : joueur 2 ----------------------------------------------
print("")
print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])

case = int(input(joueur2 + " (O), quelle case ? "))
if case > 9:
    print("Cette case n'existe pas !")
else:
    if plateau[case - 1] == str(case):
        plateau[case - 1] = "O"
        tour = tour + 1
    else:
        print("Case deja prise !")

# --- coup 3 : joueur 1 ----------------------------------------------
print("")
print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])

case = int(input(joueur1 + " (X), quelle case ? "))
if case > 9:
    print("Cette case n'existe pas !")
else:
    if plateau[case - 1] == str(case):
        plateau[case - 1] = "X"
        tour = tour + 1
    else:
        print("Case deja prise !")

# --- coup 4 : joueur 2 ----------------------------------------------
print("")
print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])

case = int(input(joueur2 + " (O), quelle case ? "))
if case > 9:
    print("Cette case n'existe pas !")
else:
    if plateau[case - 1] == str(case):
        plateau[case - 1] = "O"
        tour = tour + 1
    else:
        print("Case deja prise !")

# --- le bilan -------------------------------------------------------
print("")
print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])
print("")
print("Coups reellement joues : " + str(tour) + " sur 4.")
print("Cases encore libres : " + str(9 - tour))


# =====================================================================
#  PARTIE 5  -  LA CHASSE AUX BUGS   (les cinq corrections)
# =====================================================================
#
#  BUG 1   plateau[9] = "X"
#          -> IndexError. Les indices vont de 0 a 8.
#          CORRECTION :  plateau[8] = "X"
#
#  BUG 2   plateau[case] = "X"   avec case = 3
#          -> le X se pose sur la case 4, pas la 3.
#          CORRECTION :  plateau[case - 1] = "X"
#
#  BUG 3   plateau = "1", "2", "3"
#          -> ce n'est pas une liste : il manque les crochets.
#          CORRECTION :  plateau = ["1", "2", "3"]
#
#  BUG 4   case = input("Case ? ")   puis   plateau[case - 1] = "X"
#          -> TypeError : case est du texte.
#          CORRECTION : ajouter  case = int(case)
#
#  BUG 5   if plateau[case - 1] = str(case):
#          -> SyntaxError : un seul = . Il en faut deux pour comparer.
#          CORRECTION :  if plateau[case - 1] == str(case):
# =====================================================================
