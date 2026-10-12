# =====================================================================
#  LE NOMBRE SECRET  -  LA CORRECTION
#  Exercice de maison du 12 octobre 2026  -  Jeremiah Geeks
#
#  Un vrai jeu, a deux joueurs, qu'on rejoue autant de fois qu'on veut.
#  Tout ce qu'on a appris est dedans, et RIEN d'autre :
#     print · les variables · input · le +  ·  int() et str()
#     le compteur (en sens inverse)  ·  <  >  ==  ·  if
# =====================================================================


# --- ETAPE 1 : le decor ----------------------------------------------
print("=" * 33)
print("        LE NOMBRE SECRET")
print("=" * 33)
print("")
print("Joueur 1, ferme les yeux !")
print("")


# --- ETAPE 2 : le joueur 2 cache son nombre --------------------------
secret = input("Joueur 2, choisis un nombre entre 1 et 50 : ")
secret = int(secret)

print("")
print("=" * 33)
print("   Joueur 1, tu peux regarder !")
print("   Tu as 3 essais.  Score de depart : 100")
print("=" * 33)
print("")


# --- ETAPE 3 : le compteur de points ---------------------------------
points = 100


# --- ETAPE 4 : essai numero 1 ----------------------------------------
essai = input("Essai 1 - ton nombre : ")
essai = int(essai)

if essai < secret:
    print("   C'est PLUS GRAND !")
    points = points - 20

if essai > secret:
    print("   C'est PLUS PETIT !")
    points = points - 20

if essai == secret:
    print("   GAGNE ! Et du premier coup !")
print("")


# --- ETAPE 5 : essai numero 2  (on recopie, on change le numero) -----
essai = input("Essai 2 - ton nombre : ")
essai = int(essai)

if essai < secret:
    print("   C'est PLUS GRAND !")
    points = points - 20

if essai > secret:
    print("   C'est PLUS PETIT !")
    points = points - 20

if essai == secret:
    print("   GAGNE !")
print("")


# --- ETAPE 6 : essai numero 3 ----------------------------------------
essai = input("Essai 3 - ton nombre : ")
essai = int(essai)

if essai < secret:
    print("   Rate ! C'etait PLUS GRAND.")
    points = points - 20

if essai > secret:
    print("   Rate ! C'etait PLUS PETIT.")
    points = points - 20

if essai == secret:
    print("   GAGNE !")
print("")


# --- ETAPE 7 : le verdict --------------------------------------------
print("=" * 33)
print("Le nombre secret etait : " + str(secret))
print("Ton score : " + str(points) + " / 100")

if points > 50:
    print("CHAMPION DU NOMBRE SECRET !")
else:
    print("Perdu... mais la revanche est permise !")
print("=" * 33)


# =====================================================================
#  LES BONUS
# =====================================================================

# --- BONUS 1 : le 4e essai -------------------------------------------
#  Recopier le bloc de l'etape 5 et ecrire "Essai 4". Rien de plus.

# --- BONUS 2 : l'ecart ------------------------------------------------
print("")
print("Au dernier essai, tu etais a " + str(essai - secret) + " du nombre secret.")
print("(un nombre negatif veut dire que tu etais en dessous)")

# --- BONUS 3 : LE MODE SOLO  -  deux lignes magiques ------------------
#  C'est la SEULE notion nouvelle de la feuille, et elle est donnee
#  toute faite. Elle remplace l'etape 2 : l'ordinateur choisit tout
#  seul, et on peut jouer sans deuxieme joueur.
#
#       import random
#       secret = random.randint(1, 50)
#
#  On l'expliquera samedi. Celui qui l'essaie aura une longueur d'avance.


# =====================================================================
#  CE QU'ON REGARDE EN CORRIGEANT
#    - points = 100  est-il AVANT les essais, et une seule fois ?
#    - les deux lignes  essai = input(...)  et  essai = int(essai)
#      sont-elles bien la a chaque essai ?
#    - les TROIS if  (<, >, ==) sont-ils presents a chaque essai ?
#    - la ligne  points = points - 20  est-elle DANS le if (decalee) ?
#      Si elle est collee a gauche, le joueur perd des points meme
#      quand il gagne : c'est le bug le plus interessant de la feuille.
#    - str(secret) et str(points) sont-ils la dans le verdict ?
# =====================================================================
