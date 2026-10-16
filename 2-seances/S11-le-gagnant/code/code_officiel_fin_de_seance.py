# =====================================================
#  JEU XO  -  CODE OFFICIEL
#  Fin de la seance 11 : "Le jeu sait qui gagne"
#
#  >>> LE JEU EST TERMINE. Il est jouable, pour de vrai.
#
#  Notion de la seance :
#     les 8 lignes gagnantes, testees avec  and
#     la boucle qui s'arrete :  while tour < 9 and gagnant == ""
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
gagnant = ""

# --- tant qu'il reste des cases ET que personne n'a gagne
while tour < 9 and gagnant == "":

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

        # --- LES HUIT LIGNES QUI FONT GAGNER -----------------
        #  les 3 lignes
        if plateau[0] == plateau[1] and plateau[1] == plateau[2]:
            gagnant = plateau[0]
        if plateau[3] == plateau[4] and plateau[4] == plateau[5]:
            gagnant = plateau[3]
        if plateau[6] == plateau[7] and plateau[7] == plateau[8]:
            gagnant = plateau[6]
        #  les 3 colonnes
        if plateau[0] == plateau[3] and plateau[3] == plateau[6]:
            gagnant = plateau[0]
        if plateau[1] == plateau[4] and plateau[4] == plateau[7]:
            gagnant = plateau[1]
        if plateau[2] == plateau[5] and plateau[5] == plateau[8]:
            gagnant = plateau[2]
        #  les 2 diagonales
        if plateau[0] == plateau[4] and plateau[4] == plateau[8]:
            gagnant = plateau[0]
        if plateau[2] == plateau[4] and plateau[4] == plateau[6]:
            gagnant = plateau[2]

        # --- on passe la main -------------------------------
        if symbole == "X":
            symbole = "O"
            joueur = joueur2
        else:
            symbole = "X"
            joueur = joueur1
    else:
        print("Coup impossible : la case n'existe pas, ou elle est deja prise.")

# --- la partie est finie -----------------------------
print("")
print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])
print("")
print("===================================")

if gagnant == "X":
    print("   BRAVO " + joueur1 + " ! LES X ONT GAGNE !")
else:
    if gagnant == "O":
        print("   BRAVO " + joueur2 + " ! LES O ONT GAGNE !")
    else:
        print("   MATCH NUL ! Personne n'a gagne.")

print("===================================")

# =====================================================
#  SEANCE 12 : TP n°3. On teste, on fignole, ET ON JOUE.
# =====================================================
