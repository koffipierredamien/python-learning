# =====================================================================
#  TP n°1  -  CORRIGE DE L'ENSEIGNANT
#  Partie 3  :  le programme te parle  (input)
#  (etoile 3 comprise)
#
#  Fichier de l'eleve : tp1_partie3.py
#
#  LE DETAIL QUI COMPTE : on garde UN ESPACE avant le dernier
#  guillemet de la question -  "Ton nom ? "  -  sinon la reponse du
#  joueur se colle au point d'interrogation.
# =====================================================================


# ---------------------------------------------------------------------
#  EXERCICE 3.1  -  bonjour a toi
# ---------------------------------------------------------------------
prenom = input("Comment t'appelles-tu ? ")
print("Bonjour " + prenom + " !")
print("")


# ---------------------------------------------------------------------
#  EXERCICE 3.2  -  deux questions, UNE SEULE phrase
# ---------------------------------------------------------------------
ville = input("Dans quelle ville habites-tu ? ")
couleur = input("Ta couleur preferee ? ")
print("A " + ville + ", il y a surement du " + couleur + " quelque part !")
print("")


# ---------------------------------------------------------------------
#  EXERCICE 3.3  -  la fiche d'identite
#
#  Les deux-points sont alignes a la main, avec des espaces :
#  "Prenom      : "   "Age         : "   "Plat prefere: "
# ---------------------------------------------------------------------
prenom = input("Ton prenom ? ")
age = input("Ton age ? ")
plat = input("Ton plat prefere ? ")

print("==============================")
print("       FICHE DU JOUEUR")
print("==============================")
print("Prenom      : " + prenom)
print("Age         : " + age)
print("Plat prefere: " + plat)
print("==============================")
print("")


# ---------------------------------------------------------------------
#  ETOILE 3 a)  -  l'histoire folle
#
#  Quatre questions, puis trois lignes au moins qui utilisent
#  LES QUATRE reponses. L'histoire peut etre tout autre : ce qui
#  compte, c'est que les quatre boites soient reutilisees.
# ---------------------------------------------------------------------
prenom = input("Un prenom ? ")
animal = input("Un animal ? ")
lieu = input("Un lieu ? ")
objet = input("Un objet ? ")

print("")
print("Ce matin, " + prenom + " est parti a " + lieu + ".")
print("Sur le chemin, il a rencontre un " + animal)
print("qui lui a vole " + objet + " !")
print("")


# ---------------------------------------------------------------------
#  ETOILE 3 b)  -  le badge
#
#  ATTENTION, c'est un defi SANS solution parfaite aujourd'hui :
#  le cadre se deregle des que le prenom change de longueur, et
#  c'est VOULU. L'objectif est qu'ils constatent le probleme.
#
#  Les deux reponses acceptees :
#     1) ajouter des espaces a la main (ci-dessous) ;
#     2) mettre le prenom sur sa propre ligne, sans etoile a droite.
#
#  Celui qui demande "est-ce qu'on peut compter les lettres ?" a pose
#  la question de la seance suivante. Notez son nom.
# ---------------------------------------------------------------------
prenom = input("Ton prenom ? ")

print("****************************")
print("*                          *")
print("*        " + prenom)
print("*                          *")
print("****************************")

#  La variante acceptee, sans etoile a droite : le cadre reste droit
#  quelle que soit la longueur du prenom.
print("")
print("* * * * * * * * * * * * * *")
print("")
print("     " + prenom)
print("")
print("* * * * * * * * * * * * * *")
