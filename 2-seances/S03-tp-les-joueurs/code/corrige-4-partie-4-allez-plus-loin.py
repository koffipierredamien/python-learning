# =====================================================================
#  TP n°1  -  CORRIGE DE L'ENSEIGNANT
#  ETOILE 4  -  les quatre defis du projet, reunis dans un seul
#               programme (l'eleve peut les faire dans l'ordre
#               qu'il veut, et n'en faire qu'un ou deux)
#
#  AUCUN DE CES DEFIS N'INTRODUIT DE NOTION NOUVELLE :
#  tout se fait avec  print, les variables, input  et  le + .
# =====================================================================


print("===================================")
print("       BIENVENUE DANS LE JEU XO")
print("===================================")
print("Cree par : Mehdi")
print("")

joueur1 = input("Joueur 1, quel est ton nom ? ")
joueur2 = input("Joueur 2, quel est ton nom ? ")

# --- DEFI 1 : la carte des joueurs -----------------------------------
#  Deux questions de plus, pour les villes.
ville1 = input(joueur1 + ", quelle est ta ville ? ")
ville2 = input(joueur2 + ", quelle est ta ville ? ")

# --- DEFI 2 : qui commence ? -----------------------------------------
#  Une troisieme question, et une ligne de plus a la fin.
premier = input("Qui commence la partie ? ")
print("")

symbole1 = "X"
symbole2 = "O"

print(joueur1 + " joue les " + symbole1)
print(joueur2 + " joue les " + symbole2)
print("")

# --- DEFI 1 (suite) : on affiche la carte, avant la grille -----------
print("+----------------------------------+")
print("| " + joueur1 + " (" + symbole1 + ") - " + ville1)
print("| " + joueur2 + " (" + symbole2 + ") - " + ville2)
print("+----------------------------------+")
print("")

# --- DEFI 4 : le compte a rebours ------------------------------------
print("3...")
print("2...")
print("1...")
print("PARTEZ !")
print("")

# --- DEFI 3 : le plateau numerote ------------------------------------
#  Les points deviennent les numeros 1 a 9. Les espaces ne bougent pas.
print(" 1 | 2 | 3")
print("---+---+---")
print(" 4 | 5 | 6")
print("---+---+---")
print(" 7 | 8 | 9")
print("")

print("Que la partie commence, " + joueur1 + " et " + joueur2 + " !")

# --- DEFI 2 (suite) --------------------------------------------------
print("C'est " + premier + " qui commence !")


# =====================================================================
#  SI UN ELEVE A TOUT FINI ET EN REDEMANDE :
#  donnez-lui le defi b) de l'etoile 2 - l'echange des deux boites.
#  C'est le plus difficile de la feuille.
#
#  LE PLATEAU NUMEROTE DU DEFI 3 EST LA BRIQUE DE LA SEANCE 4 :
#  celui qui l'a fait aura une longueur d'avance samedi prochain.
#  Dites-le-lui.
# =====================================================================
