# =====================================================
#  JEU XO  -  Seance 9
#  UNE SEULE QUESTION AU LIEU DE TROIS
# =====================================================
#
#  Aujourd'hui, on n'ajoute rien au jeu : ON ENLEVE.
#  Le meme jeu, avec deux fois moins de lignes, et le
#  bug du zero repare.
#
#  1. F5 tout de suite.
#  2. Remplace les  ____  .
#  3. Teste les QUATRE chemins : 5, puis 5, puis 12, puis 0.
# =====================================================

print("===================================")
print("       BIENVENUE DANS LE JEU XO")
print("===================================")
print("Cree par : les Jeremiah Geeks")
print("")

joueur1 = input("Joueur 1, quel est ton nom ? ")
joueur2 = input("Joueur 2, quel est ton nom ? ")
print("")
print(joueur1 + " joue les X")
print(joueur2 + " joue les O")
print("")

plateau = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])
print("")


# -----------------------------------------------------
#  PARTIE 1 : les trois questions deviennent UNE SEULE
# -----------------------------------------------------

case = input(joueur1 + ", quelle case veux-tu jouer ? ")
case = int(case)

# ETAPE 1 : complete la condition. Il faut les TROIS choses
#           en meme temps, reliees par  and  :
#              la case est au moins 1
#              ET la case est au plus 9
#              ET la case contient encore son numero
#
#           Regarde : il n'y a plus de if dans le if.
#           Un seul if, un seul else, et 4 espaces. C'est tout.
if case >= 1 and case <= ____ and plateau[case - 1] == ____(case):
    plateau[case - 1] = "X"
    print(joueur1 + " pose un X sur la case " + str(case) + ".")
else:
    print("Coup impossible : la case n'existe pas, ou elle est deja prise.")

print("")
print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])
print("")

#  >>> TESTE LE ZERO. Le bug de samedi dernier doit avoir disparu.
#  >>> CARTE VERTE, et on attend.


# -----------------------------------------------------
#  PARTIE 2 : le joueur 2
# -----------------------------------------------------

# ETAPE 2 : recopie le bloc de la partie 1 (il est court,
#           maintenant !) et change joueur1 -> joueur2 et X -> O.



# ETAPE 3 : recopie les cinq lignes d'affichage, a la fin.



# =====================================================
#  TU AS FINI ? LEVE LA CARTE BLEUE.
#
#  DEFI 1 : avec  or , affiche un message DIFFERENT selon
#           la raison du refus :
#               if case < 1 or case > 9:
#                   print("Cette case n'existe pas !")
#               else:
#                   ...
#
#  DEFI 2 : ajoute un compteur de coups REFUSES, et affiche
#           a la fin : "Vous avez fait 3 coups impossibles."
#
#  DEFI 3 : compte les lignes de ton fichier d'aujourd'hui,
#           et celles de celui de samedi dernier. Tu as
#           enleve combien de lignes ?
# =====================================================
