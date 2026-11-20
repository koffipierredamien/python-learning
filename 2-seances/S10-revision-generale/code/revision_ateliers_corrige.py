# =====================================================================
#  REVISION GENERALE DU 14 NOVEMBRE  -  LES CINQ ATELIERS
#  CORRIGE  -  POUR L'ENSEIGNANT
#
#  Chaque atelier se joue en trois temps :
#     1. on PROJETTE le code de depart, ils le tapent
#     2. ils PREDISENT ce qui va s'afficher, cartes en l'air
#     3. ils LANCENT, et on repare ensemble
#
#  Rien au-dela de la seance 9. La boucle arrive APRES.
# =====================================================================

print("=" * 60)
print("  Ce fichier contient les CINQ corriges, l'un apres l'autre.")
print("  Les input() ont ete remplaces par des valeurs fixes,")
print("  pour pouvoir le lancer d'un coup avant la seance.")
print("=" * 60)
print("")


# =====================================================================
#  ATELIER 1  -  TEXTE OU NOMBRE          (facile, 5 min)
#  Depart projete :
#       a = input("Un nombre : ")
#       b = input("Un autre : ")
#       print(a + b)
#  Ils tapent 2 puis 3.  Ils predisent 5.  Ca affiche 23.
#  LA QUESTION : fais-lui afficher 5.
# =====================================================================
print("--- ATELIER 1 ---")

a = "2"          # a = input("Un nombre : ")
b = "3"          # b = input("Un autre : ")

print(a + b)                    # 23   <- le depart

a = int(a)
b = int(b)
print(a + b)                    # 5    <- la reparation

#  AUTRE REPARATION, tout aussi juste :
#       print(int(a) + int(b))
#  Les deux marchent. On montre les deux.
print("")


# =====================================================================
#  ATELIER 2  -  LA LISTE ET L'INDICE      (facile, 6 min)
#  Depart projete :
#       sacs = ["riz", "sucre", "sel", "farine", "huile"]
#  TROIS COMMANDES, dans l'ordre :
#    a) affiche  Le sac 3 contient : sel
#    b) remplace le contenu du sac 4 par mais
#    c) affiche la liste entiere, avec UN SEUL print
# =====================================================================
print("--- ATELIER 2 ---")

sacs = ["riz", "sucre", "sel", "farine", "huile"]

print("Le sac 3 contient : " + sacs[2])        # a)
sacs[3] = "mais"                                # b)
print(sacs)                                     # c)

#  LA QUESTION PIEGE A POSER AVANT DE LANCER :
#    "Quel indice pour le sac 5 ?"  -> 4
#    "Et sacs[5] ?"                 -> IndexError
print("")


# =====================================================================
#  ATELIER 3  -  LE DECALAGE DECIDE DE TOUT   (moyen, 8 min)
#  Depart projete : le code ci-dessous.
#  LA QUESTION : le score ne s'affiche que quand on se trompe.
#  Fais en sorte qu'il s'affiche DANS LES DEUX CAS,
#  en DEPLACANT une seule ligne. On n'en ajoute aucune.
# =====================================================================
print("--- ATELIER 3 ---")

points = 100
reponse = "56"        # reponse = input("Combien font 7 x 8 ? ")
reponse = int(reponse)

if reponse == 56:
    print("Juste !")
else:
    points = points - 40
    print("Faux.")

#  LA REPARATION : cette ligne etait DANS le else. On la colle a gauche.
print("Il te reste " + str(points) + " points.")
print("")


# =====================================================================
#  ATELIER 4  -  LE BUG DU OU               (complexe, 10 min)
#  Depart projete : le code ci-dessous, avec  or  a la place de  and.
#  La case 3 est DEJA PRISE, et pourtant le programme pose dessus.
#  LA QUESTION : pourquoi ? Repare, puis teste 5, 0 et 12.
# =====================================================================
print("--- ATELIER 4 ---")

plateau = ["1", "2", "X", "4", "5", "6", "7", "8", "9"]
case = 3

#  LE DEPART (faux) :
#       if case >= 1 or case <= 9 and plateau[case - 1] == str(case):
#  case >= 1 est VRAI, donc avec  or  tout est vrai : il pose sur le X.

#  LA REPARATION :
if case >= 1 and case <= 9 and plateau[case - 1] == str(case):
    plateau[case - 1] = "O"
    print("Pose !")
else:
    print("Coup impossible.")

print(plateau)

#  LES TROIS TESTS A FAIRE ENSUITE, en changeant la valeur de case
#  et en relancant a chaque fois :
#        case = 5   -> Pose !
#        case = 0   -> Coup impossible.
#        case = 12  -> Coup impossible.
#
#  Le 0 est le plus interessant : sans le  case >= 1,  il passerait,
#  et le symbole irait se poser dans la case 9.
print("")


# =====================================================================
#  ATELIER 5  -  LE DEFI, ET LE PIEGE       (complexe, 12 min)
#  LA CONSIGNE, sans code de depart :
#    "Affiche le plateau TROIS fois de suite. Entre deux affichages,
#     pose un symbole de plus : X en case 1, puis O en case 5,
#     puis X en case 9."
#  Ils vont recopier les cinq lignes d'affichage trois fois.
#  C'EST VOULU. A la fin : "combien de lignes as-tu ecrites ?"
# =====================================================================
print("--- ATELIER 5 ---")

plateau = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

plateau[0] = "X"
print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])
print("")

plateau[4] = "O"
print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])
print("")

plateau[8] = "X"
print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])

# =====================================================================
#  18 lignes recopiees pour TROIS affichages.
#  Pour les neuf tours d'une vraie partie : 54.
#  C'est exactement la question qui ouvre la lecon du jour.
# =====================================================================
