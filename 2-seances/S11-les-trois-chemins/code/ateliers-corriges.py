# =====================================================================
#  SEANCE 11  -  LES QUATRE ATELIERS DU COURS EN QUIZ
#  CORRIGE  -  POUR L'ENSEIGNANT
#
#  Les input() sont remplaces par des valeurs fixes, pour pouvoir
#  lancer ce fichier d'un bloc avant la seance.
#  Rien au-dela de la seance 9, plus le elif du jour.
# =====================================================================

print("=" * 62)


# =====================================================================
#  ATELIER 1  -  DEUX  if,  OU UN  elif ?        (facile, 6 min)
#
#  Depart projete :
#       note = 12
#       if note >= 10:
#           print("Admis")
#       if note >= 10:
#           print("Felicitations")
#
#  Ils predisent "Admis". Ca affiche LES DEUX.
#  LA QUESTION : remplace le deuxieme if par elif. Que se passe-t-il ?
# =====================================================================
print("--- ATELIER 1 ---")

note = 12

#  LE DEPART : deux if separes. Python pose les DEUX questions.
if note >= 10:
    print("Admis")
if note >= 10:
    print("Felicitations")

print("  ... et maintenant avec elif :")

#  LA REPARATION : elif ne se pose la question que si la precedente
#  etait FAUSSE. Ici elle etait vraie : la deuxieme n'est pas regardee.
if note >= 10:
    print("Admis")
elif note >= 10:
    print("Felicitations")

print("")


# =====================================================================
#  ATELIER 2  -  LA CASCADE DES MENTIONS         (moyen, 12 min)
#
#  ALGORITHME D'ABORD, SUR LE CAHIER. Pas de clavier avant.
#  Puis : une note sur 20, et le programme annonce
#     16 et plus .. Tres bien
#     14 a 15 .... Bien
#     12 a 13 .... Assez bien
#     10 a 11 .... Passable
#     moins de 10  A revoir
#
#  LE PIEGE : celui qui commence par  note >= 10  met TOUT le monde
#  en "Passable". L'ordre des questions EST l'exercice.
# =====================================================================
print("--- ATELIER 2 ---")

note = 15        # note = int(input("Ta note sur 20 ? "))

if note >= 16:
    print("Tres bien")
elif note >= 14:
    print("Bien")
elif note >= 12:
    print("Assez bien")
elif note >= 10:
    print("Passable")
else:
    print("A revoir")

#  POURQUOI CA MARCHE : quand on arrive a  note >= 14,  on SAIT DEJA
#  que la note est plus petite que 16. On n'a donc pas besoin d'ecrire
#  "entre 14 et 15" : le elif l'a deja fait pour nous.
print("")


# =====================================================================
#  ATELIER 3  -  LE COUP, EN UNE CASCADE          (moyen, 10 min)
#
#  Leur propre jeu. Le message "la case n'existe pas OU elle est deja
#  prise" devient DEUX messages distincts.
# =====================================================================
print("--- ATELIER 3 ---")

plateau = ["1", "2", "X", "4", "5", "6", "7", "8", "9"]

case = 12
if case < 1 or case > 9:
    print("Cette case n'existe pas !")
elif plateau[case - 1] != str(case):
    print("Cette case est deja prise !")
else:
    plateau[case - 1] = "O"
    print("Pose !")

case = 3
if case < 1 or case > 9:
    print("Cette case n'existe pas !")
elif plateau[case - 1] != str(case):
    print("Cette case est deja prise !")
else:
    plateau[case - 1] = "O"
    print("Pose !")

case = 7
if case < 1 or case > 9:
    print("Cette case n'existe pas !")
elif plateau[case - 1] != str(case):
    print("Cette case est deja prise !")
else:
    plateau[case - 1] = "O"
    print("Pose !")

print(plateau)
print("")


# =====================================================================
#  ATELIER 4  -  LE PIEGE DE L'ORDRE              (complexe, 10 min)
#
#  Depart projete : la cascade CI-DESSOUS, dans le mauvais ordre.
#  Quelle que soit la note, elle affiche toujours la meme chose.
#  LA QUESTION : pourquoi, et comment reparer SANS rien ajouter.
# =====================================================================
print("--- ATELIER 4 ---")

#  LE DEPART (faux) :
#       if note >= 10:
#           print("Passable")
#       elif note >= 12:
#           print("Assez bien")
#       elif note >= 16:
#           print("Tres bien")
#
#  Avec note = 18 : la PREMIERE question est deja vraie (18 >= 10),
#  Python s'arrete la et affiche "Passable". Les deux autres ne sont
#  jamais regardees.
note = 18
if note >= 10:
    print("  le depart affiche : Passable      <- faux")

#  LA REPARATION : on ne change rien, on REMET LES LIGNES DANS L'ORDRE,
#  du plus exigeant au moins exigeant.
if note >= 16:
    print("  l'ordre repare affiche : Tres bien")
elif note >= 12:
    print("  Assez bien")
elif note >= 10:
    print("  Passable")

#  LA REGLE A RETENIR, ecrite au tableau :
#     dans une cascade, on va du PLUS PRECIS au PLUS GENERAL.
print("")
print("=" * 62)
