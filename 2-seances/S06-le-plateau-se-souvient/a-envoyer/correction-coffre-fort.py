# =====================================================================
#  LE COFFRE-FORT  -  LA CORRECTION
#  Exercice de maison de la semaine du 21 octobre 2026
#
#  Tout ce qu'on sait, et rien d'autre :
#     print · les variables · input · le +  ·  int() et str()
#     le compteur  ·  if / else  ·  LA LISTE et l'indice case - 1
# =====================================================================

print("=" * 34)
print("        LE COFFRE-FORT")
print("=" * 34)
print("")

# --- ETAPE 1 : les cinq tiroirs, dans une liste ----------------------
tiroirs = ["1", "2", "3", "4", "5"]

print(" " + tiroirs[0] + " | " + tiroirs[1] + " | " + tiroirs[2] + " | " + tiroirs[3] + " | " + tiroirs[4])
print("")

# --- ETAPE 2 : le joueur 2 cache le tresor ---------------------------
print("Joueur 1, ferme les yeux !")
tresor = input("Joueur 2, dans quel tiroir caches-tu le tresor ? (1 a 5) ")
tresor = int(tresor)

print("")
print("=" * 34)
print("   Joueur 1, tu as 2 essais.")
print("=" * 34)
print("")

# --- ETAPE 3 : le compteur de points ---------------------------------
points = 50

# --- ETAPE 4 : premier essai -----------------------------------------
essai = input("Essai 1 - quel tiroir ouvres-tu ? ")
essai = int(essai)

if essai == tresor:
    print("   BRAVO ! Le tresor etait bien la !")
    tiroirs[essai - 1] = "T"
else:
    print("   Vide ! Ce tiroir ne contenait rien.")
    tiroirs[essai - 1] = "X"
    points = points - 20

print("")
print(" " + tiroirs[0] + " | " + tiroirs[1] + " | " + tiroirs[2] + " | " + tiroirs[3] + " | " + tiroirs[4])
print("")

# --- ETAPE 5 : deuxieme essai  (on recopie l'etape 4) ----------------
essai = input("Essai 2 - quel tiroir ouvres-tu ? ")
essai = int(essai)

if essai == tresor:
    print("   BRAVO ! Le tresor etait bien la !")
    tiroirs[essai - 1] = "T"
else:
    print("   Vide ! Ce tiroir ne contenait rien.")
    tiroirs[essai - 1] = "X"
    points = points - 20

print("")
print(" " + tiroirs[0] + " | " + tiroirs[1] + " | " + tiroirs[2] + " | " + tiroirs[3] + " | " + tiroirs[4])
print("")

# --- ETAPE 6 : le verdict --------------------------------------------
print("=" * 34)
print("Le tresor etait dans le tiroir " + str(tresor) + ".")
print("Ton score : " + str(points) + " / 50")

if points > 20:
    print("PILLEUR DE COFFRE-FORT !")
else:
    print("Le coffre a resiste... pour cette fois.")
print("=" * 34)

# --- BONUS 1 : le troisieme essai ------------------------------------
#  Recopier le bloc de l'etape 5. Rien de plus.

# --- BONUS 2 : le tiroir deja ouvert ---------------------------------
#  Avant d'ouvrir, verifier que le tiroir contient encore son numero :
#      if tiroirs[essai - 1] == str(essai):
#          ... on ouvre ...
#      else:
#          print("Tu as deja ouvert ce tiroir !")
#  C'est exactement l'idee de la seance 7 : une case libre contient
#  encore son numero.

# =====================================================================
#  CE QU'ON REGARDE EN CORRIGEANT
#    - la liste a-t-elle bien CINQ cases, entre crochets ?
#    - l'affichage utilise-t-il tiroirs[0] a tiroirs[4] -- et pas [1] a [5] ?
#    - le  - 1  est-il present dans  tiroirs[essai - 1]  ?
#    - points = 50 est-il AVANT les essais, et une seule fois ?
#    - points = points - 20 est-il DANS le else (decale) ?
#    - str(tresor) et str(points) sont-ils la dans le verdict ?
# =====================================================================
