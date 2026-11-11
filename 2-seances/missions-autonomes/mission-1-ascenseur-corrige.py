# =====================================================================
#  MISSION AUTONOME n 1  -  L'ASCENSEUR DE LA TOUR
#  CORRIGE  -  POUR L'ENSEIGNANT, A NE PAS DONNER
#
#  ATTENTION : ce fichier est UNE solution, pas LA solution.
#  L'eleve a recu un cahier des charges, pas des instructions.
#  Tout programme qui respecte les sept regles est juste, meme s'il
#  ne ressemble pas du tout a celui-ci. On note le RESULTAT et
#  L'ALGORITHME, jamais la ressemblance avec ce fichier.
#
#  Boite a outils : rien au-dela de la seance 7.
#     print · variables · input · le +  ·  int() et str()
#     le compteur  ·  les operateurs  ·  if / else
#     la liste et l'indice  ·  LE IF DANS LE IF
# =====================================================================

print("=" * 42)
print("        LA TOUR ACPROKIDS")
print("=" * 42)
print("")

# --- ce que la tour contient -----------------------------------------
etages = ["Parking", "Accueil", "Bureaux", "Cantine", "Terrasse"]

print(" 5 - " + etages[4])
print(" 4 - " + etages[3])
print(" 3 - " + etages[2])
print(" 2 - " + etages[1])
print(" 1 - " + etages[0])
print("")

# --- l'etat de l'ascenseur au depart ---------------------------------
actuel = 1
parcourus = 0
arrets = 0

print("L'ascenseur est a l'etage 1 : " + etages[actuel - 1])
print("Tu as droit a 3 voyages.")
print("")


# =====================================================================
#  VOYAGE 1   (c'est ce bloc que l'eleve recopiera trois fois)
# =====================================================================
demande = input("Voyage 1 - a quel etage vas-tu ? ")
demande = int(demande)

if demande > 5:
    print("   Cet etage n'existe pas. La tour va de 1 a 5.")
else:
    if demande > actuel:
        distance = demande - actuel
        print("   L'ascenseur MONTE de " + str(distance) + " etage(s).")
    else:
        if demande < actuel:
            distance = actuel - demande
            print("   L'ascenseur DESCEND de " + str(distance) + " etage(s).")
        else:
            distance = 0
            print("   Tu y es deja ! Les portes se rouvrent.")

    #  Ces quatre lignes sont DANS le else du premier if, mais
    #  DEHORS des trois branches : elles servent dans les trois cas.
    print("   Etage " + str(demande) + " : " + etages[demande - 1])
    parcourus = parcourus + distance
    arrets = arrets + 1
    actuel = demande

print("")


# =====================================================================
#  VOYAGE 2
# =====================================================================
demande = input("Voyage 2 - a quel etage vas-tu ? ")
demande = int(demande)

if demande > 5:
    print("   Cet etage n'existe pas. La tour va de 1 a 5.")
else:
    if demande > actuel:
        distance = demande - actuel
        print("   L'ascenseur MONTE de " + str(distance) + " etage(s).")
    else:
        if demande < actuel:
            distance = actuel - demande
            print("   L'ascenseur DESCEND de " + str(distance) + " etage(s).")
        else:
            distance = 0
            print("   Tu y es deja ! Les portes se rouvrent.")

    print("   Etage " + str(demande) + " : " + etages[demande - 1])
    parcourus = parcourus + distance
    arrets = arrets + 1
    actuel = demande

print("")


# =====================================================================
#  VOYAGE 3
# =====================================================================
demande = input("Voyage 3 - a quel etage vas-tu ? ")
demande = int(demande)

if demande > 5:
    print("   Cet etage n'existe pas. La tour va de 1 a 5.")
else:
    if demande > actuel:
        distance = demande - actuel
        print("   L'ascenseur MONTE de " + str(distance) + " etage(s).")
    else:
        if demande < actuel:
            distance = actuel - demande
            print("   L'ascenseur DESCEND de " + str(distance) + " etage(s).")
        else:
            distance = 0
            print("   Tu y es deja ! Les portes se rouvrent.")

    print("   Etage " + str(demande) + " : " + etages[demande - 1])
    parcourus = parcourus + distance
    arrets = arrets + 1
    actuel = demande

print("")


# =====================================================================
#  LE JOURNAL DE BORD
# =====================================================================
print("=" * 42)
print("          JOURNAL DE L'ASCENSEUR")
print("=" * 42)
print(" Position finale : etage " + str(actuel) + " (" + etages[actuel - 1] + ")")
print(" Etages parcourus : " + str(parcourus))
print(" Arrets effectues : " + str(arrets) + " / 3")
print("")

if parcourus > 6:
    print(" Cet ascenseur a bien travaille aujourd'hui !")
else:
    print(" Journee tranquille dans la tour.")
print("=" * 42)


# =====================================================================
#  CE QUE L'ELEVE A LE DROIT DE FAIRE AUTREMENT
#    - d'autres noms d'etages, d'autres messages : aucune importance
#    - afficher la tour a l'endroit (1 en haut) : c'est son choix
#    - garder "distance" ou recalculer a chaque branche : les deux
#      marchent ; recalculer est plus long, pas plus faux
#    - compter les voyages RATES en plus : c'est un bonus, pas une faute
#    - tester  demande > 5  ou  demande >= 6  : identique
#
#  CE QUI EST VRAIMENT FAUX
#    - la ligne  actuel = demande  oubliee : l'ascenseur ne bouge
#      jamais. C'est LA faute a chercher en premier.
#    - les quatre lignes de mise a jour placees DANS une des branches
#      au lieu d'etre dessous : l'ascenseur ne se met a jour que dans
#      un cas sur trois.
#    - parcourus = parcourus + distance place avant le calcul de
#      distance.
#    - etages[demande] sans le - 1 : le nom affiche est celui de
#      l'etage du dessus. Python ne dit rien.
#    - un etage inexistant accepte : le programme plante en
#      IndexError, ou affiche un nom faux.
# =====================================================================
