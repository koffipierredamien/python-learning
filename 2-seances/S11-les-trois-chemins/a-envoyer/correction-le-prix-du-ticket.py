# =====================================================================
#  L'EXERCICE ETOILE DE LA SEANCE 11  -  LE PRIX DU TICKET
#  CORRIGE  -  POUR L'ENSEIGNANT  (a ne pas donner)
#
#  Pour ceux qui ont fini Le Bulletin avant les autres.
#  Rien de nouveau : une cascade, plus un if ordinaire apres.
#  Ce qui est dur, c'est de TROUVER L'ORDRE et de voir le piege du
#  dernier tarif.
#
#  CONSIGNE : l'algorithme sur le cahier, MONTRE, avant tout clavier.
# =====================================================================

print("=" * 44)
print("        LE CINEMA DU QUARTIER")
print("=" * 44)
print("")

age = input("Quel age as-tu ? ")
age = int(age)
jour = input("Quel jour viens-tu ? ")

# --- LA CASCADE DES TARIFS -------------------------------------------
#  LE PIEGE : si on ecrit  elif age >= 18  pour les adultes AVANT la
#  ligne des 65 ans, alors une personne de 70 ans paie 2000, parce que
#  70 >= 18 est deja vrai et que Python s'arrete au premier vrai.
#  En allant du plus jeune au plus age, le probleme disparait tout seul.
if age < 5:
    prix = 0
elif age <= 12:
    prix = 500
elif age <= 17:
    prix = 1000
elif age <= 64:
    prix = 2000
else:
    prix = 1000

print("")
print("Tarif de base : " + str(prix) + " F")

# --- LA REDUCTION DU SAMEDI ------------------------------------------
#  Ce n'est PAS un elif : la reduction s'applique APRES, quel que soit
#  le tarif trouve. C'est un if tout seul, qui vient apres la cascade.
if jour == "samedi":
    prix = prix - 500
    #  Le garde-fou : on ne rembourse personne.
    if prix < 0:
        prix = 0
    print("Reduction du samedi : -500 F")

print("")
print("=" * 44)
print(" A PAYER : " + str(prix) + " F")
if prix == 0:
    print(" C'est gratuit, bonne seance !")
print("=" * 44)


# =====================================================================
#  LES QUATRE ESSAIS A LUI FAIRE FAIRE AVANT DE VALIDER
#    age 3,  un lundi  -> 0 F      (et "c'est gratuit")
#    age 70, un lundi  -> 1000 F   (LE PIEGE : pas 2000)
#    age 30, un samedi -> 1500 F
#    age 3,  un samedi -> 0 F      (LE GARDE-FOU : pas -500)
#
#  CE QU'ON REGARDE EN CORRIGEANT
#    - L'ALGORITHME EST-IL SUR LE CAHIER ? C'est le premier livrable.
#    - la cascade est-elle dans un ordre qui tient ? (du plus jeune au
#      plus age, ou du plus age au plus jeune : les deux marchent)
#    - la reduction est-elle un  if  SEPARE, et non un  elif  de la
#      cascade ? Colle en elif, elle ne s'appliquerait qu'a ceux qui
#      ne sont tombes dans aucune tranche : personne.
#    - le garde-fou  if prix < 0  est-il la ?
# =====================================================================
