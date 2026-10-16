# =====================================================================
#  LA SOIREE DU CLUB GEEK  -  LA CORRECTION
#  Exercice de maison de la semaine du 11 novembre 2026
#
#  Tout ce qu'on sait, et rien d'autre :
#     print · les variables · input · le +  ·  int() et str()
#     le compteur  ·  if / else  ·  le if dans le if
#     la liste et l'indice  ·  ET AUJOURD'HUI :  and  /  or
#
#  En classe, le videur posait UNE question.
#  Ici, il tient toute la soiree : trois fauteuils, quatre visiteurs.
# =====================================================================

print("=" * 38)
print("        LE CLUB GEEK  -  CE SOIR")
print("=" * 38)
print("Trois fauteuils. Pas un de plus.")
print("")

# --- ETAPE 1 : les trois fauteuils, et le compteur -------------------
fauteuils = ["(libre)", "(libre)", "(libre)"]
entres = 0


# =====================================================================
#  VISITEUR 1
# =====================================================================
print("-" * 38)
nom = input("Qui se presente ? ")
age = input("Ton age ? ")
age = int(age)
seances = input("Combien de seances as-tu suivies ? ")
seances = int(seances)
code = input("Ton code VIP (sinon tape juste Entree) ? ")

if entres < 3:
    #  La regle du club, en une seule question :
    #     ( le bon age  ET  assez de seances )   OU   le code VIP
    #  Les parentheses, comme en maths : on fait d'abord ce qui est dedans.
    if (age >= 12 and age <= 18 and seances >= 3) or code == "GEEK2026":
        print("   ENTREZ, " + nom + " !")
        fauteuils[entres] = nom
        entres = entres + 1
    else:
        print("   Desole " + nom + ", pas ce soir.")
else:
    print("   Le club est COMPLET. Reviens samedi prochain.")

print("   Fauteuils occupes : " + str(entres) + " / 3")
print("")


# =====================================================================
#  VISITEUR 2   (on recopie le bloc du visiteur 1)
# =====================================================================
print("-" * 38)
nom = input("Qui se presente ? ")
age = input("Ton age ? ")
age = int(age)
seances = input("Combien de seances as-tu suivies ? ")
seances = int(seances)
code = input("Ton code VIP (sinon tape juste Entree) ? ")

if entres < 3:
    if (age >= 12 and age <= 18 and seances >= 3) or code == "GEEK2026":
        print("   ENTREZ, " + nom + " !")
        fauteuils[entres] = nom
        entres = entres + 1
    else:
        print("   Desole " + nom + ", pas ce soir.")
else:
    print("   Le club est COMPLET. Reviens samedi prochain.")

print("   Fauteuils occupes : " + str(entres) + " / 3")
print("")


# =====================================================================
#  VISITEUR 3
# =====================================================================
print("-" * 38)
nom = input("Qui se presente ? ")
age = input("Ton age ? ")
age = int(age)
seances = input("Combien de seances as-tu suivies ? ")
seances = int(seances)
code = input("Ton code VIP (sinon tape juste Entree) ? ")

if entres < 3:
    if (age >= 12 and age <= 18 and seances >= 3) or code == "GEEK2026":
        print("   ENTREZ, " + nom + " !")
        fauteuils[entres] = nom
        entres = entres + 1
    else:
        print("   Desole " + nom + ", pas ce soir.")
else:
    print("   Le club est COMPLET. Reviens samedi prochain.")

print("   Fauteuils occupes : " + str(entres) + " / 3")
print("")


# =====================================================================
#  VISITEUR 4
# =====================================================================
print("-" * 38)
nom = input("Qui se presente ? ")
age = input("Ton age ? ")
age = int(age)
seances = input("Combien de seances as-tu suivies ? ")
seances = int(seances)
code = input("Ton code VIP (sinon tape juste Entree) ? ")

if entres < 3:
    if (age >= 12 and age <= 18 and seances >= 3) or code == "GEEK2026":
        print("   ENTREZ, " + nom + " !")
        fauteuils[entres] = nom
        entres = entres + 1
    else:
        print("   Desole " + nom + ", pas ce soir.")
else:
    print("   Le club est COMPLET. Reviens samedi prochain.")

print("   Fauteuils occupes : " + str(entres) + " / 3")
print("")


# --- LE RAPPORT DE FIN DE SOIREE -------------------------------------
print("=" * 38)
print("        RAPPORT DU VIDEUR")
print("=" * 38)
print(" Fauteuil 1 : " + fauteuils[0])
print(" Fauteuil 2 : " + fauteuils[1])
print(" Fauteuil 3 : " + fauteuils[2])
print("")
print(" Entrees de la soiree : " + str(entres) + " / 3")

if entres == 3:
    print(" SOIREE COMPLETE ! Le club a fait salle pleine.")
else:
    print(" Il restait de la place. Le videur a ete severe.")
print("=" * 38)


# --- BONUS 1 : le visiteur 5 -----------------------------------------
#  Recopier encore tout le bloc. Encore. Oui, c'est enervant.
#  RETENIR CET AGACEMENT : samedi prochain, une seule ligne
#  remplacera les quatre blocs. Ca s'appelle une boucle.

# --- BONUS 2 : le code en minuscules ---------------------------------
#  Le VIP qui tape "geek2026" doit entrer aussi. Un  or  de plus :
#      ... or code == "GEEK2026" or code == "geek2026":

# --- BONUS 3 : deja entre ! ------------------------------------------
#  Avant de faire entrer, verifier que le nom n'est pas deja assis :
#      if nom == fauteuils[0] or nom == fauteuils[1] or nom == fauteuils[2]:
#          print("Tu es deja a l'interieur !")
#      else:
#          ... la regle du club ...
#  C'est EXACTEMENT le test de la case occupee du jeu XO,
#  avec des fauteuils a la place des cases.

# =====================================================================
#  CE QU'ON REGARDE EN CORRIGEANT
#    - y a-t-il un  and  entre CHAQUE question ? (pas de virgule)
#    - les parentheses encadrent-elles bien le groupe  age/seances ?
#    - le  or  est-il DEHORS des parentheses ?
#    - entres = 0 est-il AVANT le premier visiteur, et une seule fois ?
#    - entres = entres + 1 est-il DANS le if qui accepte ?
#    - fauteuils[entres] -- et pas fauteuils[entres - 1] :
#      ici le compteur part de 0, il tombe deja sur le bon fauteuil.
#    - str(entres) dans les print ?
# =====================================================================
