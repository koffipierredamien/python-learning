# =====================================================================
#  LA BATAILLE NAVALE  -  LA CORRECTION
#  Exercice de maison RENFORCE de la semaine du 21 octobre 2026
#  (version plus difficile du Coffre-Fort : meme boite a outils)
#
#  Tout ce qu'on sait, et rien d'autre :
#     print · les variables · input · le +  ·  int() et str()
#     le compteur  ·  if / else  ·  LA LISTE et l'indice case - 1
#
#  CE QUI EST NOUVEAU DANS LA FACON DE S'EN SERVIR :
#     - une liste de HUIT cases
#     - TROIS valeurs cachees au lieu d'une
#     - trois  if  independants au lieu d'un seul
#     - une boite TEMOIN (touche = 0 / 1) qui retient ce qui s'est passe
#     - DEUX compteurs qui avancent en meme temps
#     - deux verdicts independants a la fin
# =====================================================================

print("=" * 40)
print("           LA BATAILLE NAVALE")
print("=" * 40)
print("")

# --- ETAPE 1 : la mer, huit cases ------------------------------------
mer = ["1", "2", "3", "4", "5", "6", "7", "8"]

print(" " + mer[0] + " | " + mer[1] + " | " + mer[2] + " | " + mer[3] + " | " + mer[4] + " | " + mer[5] + " | " + mer[6] + " | " + mer[7])
print("")


# --- ETAPE 2 : le joueur 2 place ses trois bateaux -------------------
print("Joueur 1, ferme les yeux !")
print("")

b1 = input("Joueur 2, premier bateau  (1 a 8) ? ")
b1 = int(b1)
b2 = input("Joueur 2, deuxieme bateau (1 a 8) ? ")
b2 = int(b2)
b3 = input("Joueur 2, troisieme bateau (1 a 8) ? ")
b3 = int(b3)

print("")
print("=" * 40)
print("   Joueur 1, tu peux regarder !")
print("   3 bateaux caches. Tu as 4 tirs.")
print("=" * 40)
print("")


# --- ETAPE 3 : les deux compteurs ------------------------------------
score = 0
touches = 0


# --- ETAPE 4 : LE TIR N 1  (le bloc a recopier) ----------------------
tir = input("Tir 1 - quelle case ? ")
tir = int(tir)

#  La boite temoin : on la remet a 0 AVANT les trois questions.
touche = 0

if tir == b1:
    touche = 1
if tir == b2:
    touche = 1
if tir == b3:
    touche = 1

if touche == 1:
    print("   TOUCHE ! Un bateau coule.")
    mer[tir - 1] = "X"
    score = score + 30
    touches = touches + 1
else:
    print("   PLOUF ! Rien que de l'eau.")
    mer[tir - 1] = "o"
    score = score - 10

print("")
print(" " + mer[0] + " | " + mer[1] + " | " + mer[2] + " | " + mer[3] + " | " + mer[4] + " | " + mer[5] + " | " + mer[6] + " | " + mer[7])
print(" Score : " + str(score) + "   Bateaux coules : " + str(touches) + " / 3")
print("")


# --- ETAPE 5 : LE TIR N 2  (on recopie l'etape 4) --------------------
tir = input("Tir 2 - quelle case ? ")
tir = int(tir)

touche = 0

if tir == b1:
    touche = 1
if tir == b2:
    touche = 1
if tir == b3:
    touche = 1

if touche == 1:
    print("   TOUCHE ! Un bateau coule.")
    mer[tir - 1] = "X"
    score = score + 30
    touches = touches + 1
else:
    print("   PLOUF ! Rien que de l'eau.")
    mer[tir - 1] = "o"
    score = score - 10

print("")
print(" " + mer[0] + " | " + mer[1] + " | " + mer[2] + " | " + mer[3] + " | " + mer[4] + " | " + mer[5] + " | " + mer[6] + " | " + mer[7])
print(" Score : " + str(score) + "   Bateaux coules : " + str(touches) + " / 3")
print("")


# --- ETAPE 6 : LE TIR N 3 --------------------------------------------
tir = input("Tir 3 - quelle case ? ")
tir = int(tir)

touche = 0

if tir == b1:
    touche = 1
if tir == b2:
    touche = 1
if tir == b3:
    touche = 1

if touche == 1:
    print("   TOUCHE ! Un bateau coule.")
    mer[tir - 1] = "X"
    score = score + 30
    touches = touches + 1
else:
    print("   PLOUF ! Rien que de l'eau.")
    mer[tir - 1] = "o"
    score = score - 10

print("")
print(" " + mer[0] + " | " + mer[1] + " | " + mer[2] + " | " + mer[3] + " | " + mer[4] + " | " + mer[5] + " | " + mer[6] + " | " + mer[7])
print(" Score : " + str(score) + "   Bateaux coules : " + str(touches) + " / 3")
print("")


# --- ETAPE 7 : LE TIR N 4 --------------------------------------------
tir = input("Tir 4 - quelle case ? ")
tir = int(tir)

touche = 0

if tir == b1:
    touche = 1
if tir == b2:
    touche = 1
if tir == b3:
    touche = 1

if touche == 1:
    print("   TOUCHE ! Un bateau coule.")
    mer[tir - 1] = "X"
    score = score + 30
    touches = touches + 1
else:
    print("   PLOUF ! Rien que de l'eau.")
    mer[tir - 1] = "o"
    score = score - 10

print("")
print(" " + mer[0] + " | " + mer[1] + " | " + mer[2] + " | " + mer[3] + " | " + mer[4] + " | " + mer[5] + " | " + mer[6] + " | " + mer[7])
print(" Score : " + str(score) + "   Bateaux coules : " + str(touches) + " / 3")
print("")


# --- ETAPE 8 : LES DEUX VERDICTS -------------------------------------
print("=" * 40)
print("Les bateaux etaient en " + str(b1) + ", " + str(b2) + " et " + str(b3) + ".")
print("Score final : " + str(score))
print("")

#  Premier verdict : la mission.
if touches == 3:
    print("FLOTTE COULEE. Tu es AMIRAL !")
else:
    print("Il reste des bateaux a flot...")

#  Deuxieme verdict : le tir. Les deux sont INDEPENDANTS :
#  on peut avoir un bon score sans avoir tout coule.
if score >= 60:
    print("Et quel tir ! Score de professionnel.")
else:
    print("Le tir, en revanche, demande de l'entrainement.")
print("=" * 40)


# --- BONUS 1 : un cinquieme tir --------------------------------------
#  Recopier le bloc de l'etape 7. Compte les lignes que tu recopies :
#  tu auras besoin de ce chiffre dans quelques semaines.

# --- BONUS 2 : la precision ------------------------------------------
#  Avant le score final, affiche combien de tirs ont rate :
#      rates = 4 - touches
#      print("Tirs dans l'eau : " + str(rates))

# --- BONUS 3 : le tir deja joue  (niveau seance 7) -------------------
#  Si le joueur retire au meme endroit, il ne devrait pas gagner
#  30 points une deuxieme fois. Une case ou personne n'a encore tire
#  contient ENCORE SON NUMERO :
#      if mer[tir - 1] == str(tir):
#          ... tout le bloc du tir ...
#      else:
#          print("Tu as deja tire la !")
#  C'est exactement la lecon de la seance 7.

# =====================================================================
#  CE QU'ON REGARDE EN CORRIGEANT
#    - la liste a-t-elle bien HUIT cases, et l'affichage va-t-il
#      de mer[0] a mer[7] ?
#    - le  - 1  est-il present dans  mer[tir - 1]  ?
#    - LA FAUTE N 1 :  touche = 0  doit etre remis a zero DANS chaque
#      bloc de tir, AVANT les trois questions. S'il est ecrit une seule
#      fois tout en haut, alors des le premier TOUCHE tous les tirs
#      suivants seront comptes comme touches.
#    - les trois  if  sont-ils INDEPENDANTS (colles a gauche, l'un
#      sous l'autre) et non imbriques ?
#    - score et touches sont-ils crees UNE SEULE FOIS, avant le tir 1 ?
#    - touches = touches + 1 est-il bien DANS le if, et pas dans le else ?
#    - les deux verdicts de la fin sont-ils SEPARES (deux if / else
#      independants), et pas emboites ?
# =====================================================================
