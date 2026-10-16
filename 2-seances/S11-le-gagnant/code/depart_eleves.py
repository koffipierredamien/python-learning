# =====================================================
#  JEU XO  -  Seance 11
#  LE JEU SAIT QUI GAGNE
#
#  >>> A LA FIN DE CETTE SEANCE, TON JEU EST FINI.
# =====================================================
#
#  1. F5 tout de suite.
#  2. Remplace les  ____  et recopie le grand bloc.
#  3. Teste une VRAIE partie : fais gagner les X.
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

# ETAPE 1 : une boite pour le gagnant. Au depart, elle est
#           VIDE : deux guillemets, rien dedans.
gagnant = ____


# ETAPE 2 : la boucle s'arrete maintenant pour DEUX raisons :
#           le plateau est plein, OU quelqu'un a gagne.
#           Complete avec  and  :
#              tant que tour < 9  ET  que gagnant est encore vide
while tour < 9 and gagnant == ____:

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

        # ETAPE 3 : LE GRAND BLOC. Recopie-le EXACTEMENT, ici.
        #           Huit  if , huit lignes gagnantes.
        #           Il est ecrit en entier sur ta feuille.
        #
        #           les 3 lignes    :  0-1-2   3-4-5   6-7-8
        #           les 3 colonnes  :  0-3-6   1-4-7   2-5-8
        #           les 2 diagonales:  0-4-8   2-4-6


        # ETAPE 4 : on passe la main (c'est deja ecrit)
        if symbole == "X":
            symbole = "O"
            joueur = joueur2
        else:
            symbole = "X"
            joueur = joueur1
    else:
        print("Coup impossible : la case n'existe pas, ou elle est deja prise.")


# -----------------------------------------------------
#  APRES LA BOUCLE : le verdict
# -----------------------------------------------------
print("")
print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])
print("")
print("===================================")

# ETAPE 5 : le verdict. Trois cas : X a gagne, O a gagne,
#           ou personne.
if gagnant == "X":
    print("   BRAVO " + ____ + " ! LES X ONT GAGNE !")
else:
    if gagnant == "____":
        print("   BRAVO " + joueur2 + " ! LES O ONT GAGNE !")
    else:
        print("   MATCH NUL ! Personne n'a gagne.")

print("===================================")


# =====================================================
#  TU AS FINI ? LEVE LA CARTE BLEUE.
#
#  DEFI 1 : affiche en combien de coups la partie a ete
#           gagnee.
#
#  DEFI 2 : au lieu de "LES X ONT GAGNE", affiche une
#           phrase differente si la victoire arrive en
#           5 coups (le minimum) : "VICTOIRE PARFAITE !"
#
#  DEFI 3 : garde le score entre deux parties... impossible
#           pour l'instant ! Ecris sur un papier POURQUOI,
#           et ce qu'il faudrait. On en reparlera.
# =====================================================
