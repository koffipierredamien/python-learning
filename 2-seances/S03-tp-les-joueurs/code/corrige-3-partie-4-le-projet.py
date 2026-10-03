# =====================================================================
#  TP n°1  -  CORRIGE DE L'ENSEIGNANT
#  Partie 4  :  LE PROJET  -  le jeu XO rencontre ses joueurs
#
#  Fichier de l'eleve : tp1_xo.py
#
#  C'EST LE CODE OFFICIEL DE LA SEANCE 3. A 13 h 50 on le projette
#  (ou on le dicte) a ceux qui n'ont pas fini : c'est le Filet,
#  personne ne commence la seance 4 en retard.
#
#  Le seul objectif non negociable du TP : que chaque eleve arrive
#  jusqu'ici et fasse tourner ce programme.
# =====================================================================


# --- 4.1  l'ecran d'accueil ------------------------------------------
print("===================================")
print("       BIENVENUE DANS LE JEU XO")
print("===================================")
print("Cree par : Mehdi")
print("")


# --- 4.2 et 4.3  les deux joueurs ------------------------------------
#  DEUX boites differentes. Avec une seule, le premier nom est ecrase.
joueur1 = input("Joueur 1, quel est ton nom ? ")
joueur2 = input("Joueur 2, quel est ton nom ? ")
print("")


# --- 4.4  les symboles -----------------------------------------------
#  On affiche en utilisant LES VARIABLES, jamais les noms ecrits en dur.
symbole1 = "X"
symbole2 = "O"

print(joueur1 + " joue les " + symbole1)
print(joueur2 + " joue les " + symbole2)
print("")


# --- 4.5  le plateau vide --------------------------------------------
#  Un espace de travers et la grille penche : on recopie soigneusement.
print(" . | . | .")
print("---+---+---")
print(" . | . | .")
print("---+---+---")
print(" . | . | .")
print("")


# --- 4.6  le lancement -----------------------------------------------
print("Que la partie commence, " + joueur1 + " et " + joueur2 + " !")


# =====================================================================
#  LES TROIS ERREURS LES PLUS PROBABLES
#
#   1. Une seule variable pour les deux joueurs
#      -> "Regarde : ou est passe le premier nom ? Une boite ne garde
#          qu'une chose. Il t'en faut deux."
#
#   2. Les noms ecrits en dur :  print("Joyce joue les X")
#      -> "Relance avec un autre prenom. Ca marche toujours ?
#          Alors ce n'est pas le programme qui parle, c'est toi."
#
#   3. La grille de travers
#      -> "Compte les espaces. L'ordinateur affiche exactement ce que
#          tu ecris, ni plus ni moins."
# =====================================================================
