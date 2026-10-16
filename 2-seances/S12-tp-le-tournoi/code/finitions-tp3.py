# =====================================================================
#  TP n°3  -  LES FINITIONS  (corrige de l'enseignant)
#  Chaque finition est un petit bout de code a GLISSER dans le jeu.
#  Ce fichier tourne tel quel : il montre chaque morceau isole.
# =====================================================================

plateau = ["X", "O", "X", "4", "O", "6", "X", "8", "9"]
tour = 5
refus = 2
joueur1 = "Joyce"
joueur2 = "Gedeon"
gagnant = "X"


# --- FINITION A : le numero du tour ----------------------------------
#  A placer au debut de la boucle, juste avant de demander la case.
print("--- Tour " + str(tour + 1) + " sur 9 ---")
print("")


# --- FINITION B : l'ecran de victoire --------------------------------
#  A placer a la toute fin, a la place du simple print du gagnant.
if gagnant == "X":
    nom = joueur1
else:
    nom = joueur2

print("*" * 35)
print("*" + " " * 33 + "*")
print("*        BRAVO " + nom + " !")
print("*     Tu as gagne en " + str(tour) + " coups.")
print("*" + " " * 33 + "*")
print("*" * 35)
print("")


# --- FINITION C : le compteur de coups impossibles -------------------
#  refus = 0  avant la boucle, puis  refus = refus + 1  dans le else.
print("Coups impossibles tentes : " + str(refus))
print("")


# --- FINITION D : les symboles au choix ------------------------------
#  A placer apres avoir demande les noms.
#  symbole1 = input(joueur1 + ", quel symbole veux-tu ? (1 seul caractere) ")
#  symbole2 = input(joueur2 + ", et toi ? ")
symbole1 = "A"
symbole2 = "Z"
print(joueur1 + " joue les " + symbole1 + "   /   " + joueur2 + " joue les " + symbole2)
print("")
#  ATTENTION : si on change les symboles, la detection du gagnant
#  continue de marcher -- elle compare des cases entre elles, pas
#  avec "X". C'est une bonne question a leur poser.


# --- FINITION E : qui commence, au hasard ---------------------------
#  Deux lignes nouvelles, donnees toutes faites (comme au devoir).
import random

if random.randint(1, 2) == 1:
    print("Le sort a parle : " + joueur1 + " commence.")
else:
    print("Le sort a parle : " + joueur2 + " commence.")


# =====================================================================
#  CE QU'ON REGARDE EN CIRCULANT
#    A : le  + 1  est-il la ?  (le tour 0 n'existe pas pour un joueur)
#    B : str(tour) present ? sinon TypeError
#    C : refus = 0 est-il AVANT la boucle, et refus = refus + 1 DANS le else ?
#    D : le symbole est-il repris partout, ou "X" est-il reste en dur ?
#    E : import random est-il tout en haut du fichier ?
# =====================================================================
