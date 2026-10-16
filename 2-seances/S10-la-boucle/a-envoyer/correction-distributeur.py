# =====================================================================
#  LE DISTRIBUTEUR DE LA RECRE  -  LA CORRECTION
#  Exercice de maison de la semaine du 18 novembre 2026
#
#  Tout ce qu'on sait, et rien d'autre :
#     print · les variables · input · le +  ·  int() et str()
#     le compteur  ·  if / else  ·  la liste et l'indice
#     and / or  ·  ET AUJOURD'HUI :  while
#
#  Zero bloc recopie. Le programme tourne tout seul
#  jusqu'a ce que le client n'ait plus assez d'argent.
# =====================================================================

print("=" * 40)
print("      LE DISTRIBUTEUR DE LA RECRE")
print("=" * 40)
print("")

# --- ETAPE 1 : la machine -------------------------------------------
#  Deux listes qui vont ensemble :
#  le produit numero 1 est produits[0], et il coute prix[0].
produits = ["Chips", "Jus", "Chocolat", "Gateau"]
prix = [100, 150, 200, 250]

# --- ETAPE 2 : le client --------------------------------------------
argent = input("Combien as-tu d'argent ? ")
argent = int(argent)

achats = 0

# --- ETAPE 3 : LA BOUCLE --------------------------------------------
#  Tant qu'il reste de quoi acheter le moins cher (100)
#  ET qu'il reste au moins un produit dans la machine.
while argent >= 100 and achats < 4:

    print("")
    print("-" * 40)
    print(" 1. " + produits[0] + " - " + str(prix[0]) + " F")
    print(" 2. " + produits[1] + " - " + str(prix[1]) + " F")
    print(" 3. " + produits[2] + " - " + str(prix[2]) + " F")
    print(" 4. " + produits[3] + " - " + str(prix[3]) + " F")
    print("-" * 40)
    print(" Tu as " + str(argent) + " F.")

    choix = input(" Ton choix (1 a 4) ? ")
    choix = int(choix)

    #  Une seule question, quatre conditions :
    #  le numero existe, le produit est encore la, et tu as de quoi payer.
    if choix >= 1 and choix <= 4 and produits[choix - 1] != "EPUISE" and prix[choix - 1] <= argent:
        print("")
        print("   CLONK !  " + produits[choix - 1] + " tombe dans le bac.")
        argent = argent - prix[choix - 1]
        produits[choix - 1] = "EPUISE"
        achats = achats + 1
    else:
        print("")
        print("   BZZZT !  Impossible : mauvais numero, produit epuise,")
        print("            ou pas assez d'argent.")

# --- ETAPE 4 : la boucle est finie, le ticket ------------------------
print("")
print("=" * 40)
print("              TON TICKET")
print("=" * 40)
print(" Produits pris : " + str(achats) + " / 4")
print(" Monnaie       : " + str(argent) + " F")
print("")

if achats == 4:
    print(" TU AS VIDE LA MACHINE. Respect.")
else:
    print(" Plus assez d'argent. La recre est finie !")
print("=" * 40)


# --- BONUS 1 : dis-lui ce qui manque ---------------------------------
#  Dans le else, avant le BZZZT :
#      if choix >= 1 and choix <= 4 and prix[choix - 1] > argent:
#          print("   Il te manque " + str(prix[choix - 1] - argent) + " F.")

# --- BONUS 2 : le bouton SORTIE --------------------------------------
#  Le client peut partir quand il veut en tapant 0.
#  Avant la boucle :        choix = 1
#  Et dans le while :       while argent >= 100 and achats < 4 and choix != 0:
#  ATTENTION : il faut initialiser choix AVANT, sinon NameError.

# --- BONUS 3 : un cinquieme produit ----------------------------------
#  Ajoute "Biscuit" a la fin de produits, 50 a la fin de prix,
#  une ligne de menu, et remplace les 4 par des 5.
#  Compte combien de lignes tu as change : c'est tout ce qu'il faut
#  pour agrandir une machine. Sans boucle, il en aurait fallu dix fois plus.

# =====================================================================
#  CE QU'ON REGARDE EN CORRIGEANT
#    - les deux points  :  a la fin de la ligne  while  ?
#    - tout ce qui doit se repeter est-il DECALE sous le while ?
#    - argent = argent - prix[choix - 1]  est-il DANS le if qui vend ?
#      (sinon la machine fait payer meme quand elle ne donne rien)
#    - achats = achats + 1 est-il la ? Sans lui : BOUCLE INFINIE.
#      ---> Ctrl + C pour arreter un programme qui ne s'arrete plus.
#    - produits[choix - 1] = "EPUISE" : le  - 1  est-il present ?
#    - le ticket est-il DEHORS de la boucle (colle a gauche) ?
# =====================================================================
