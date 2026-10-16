# =====================================================
#  JEU XO  -  Seance 10
#  LE JEU TOURNE TOUT SEUL
# =====================================================
#
#  Aujourd'hui, on arrete de recopier.
#  Une seule fois le bloc du tour, et le jeu le rejoue
#  neuf fois tout seul.
#
#  1. F5 tout de suite.
#  2. Remplace les  ____  .
#  3. ATTENTION AUX DECALAGES : tout ce qui est DANS la
#     boucle est decale de 4 espaces.
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

# ETAPE 1 : les trois boites de depart.
tour = ____            # on commence a zero
symbole = "____"       # X commence toujours
joueur = ____          # et X, c'est le joueur 1


# -----------------------------------------------------
#  PARTIE 1 : la boucle
# -----------------------------------------------------

# ETAPE 2 : complete la condition de la boucle.
#           On recommence TANT QUE le nombre de tours est
#           plus petit que 9.
while tour < ____:

    print("")
    print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
    print("---+---+---")
    print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
    print("---+---+---")
    print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])
    print("")

    case = input(joueur + " (" + symbole + "), quelle case ? ")
    case = int(case)

    if case >= 1 and case <= 9 and plateau[case - 1] == str(case):

        # ETAPE 3 : pose le symbole du joueur qui joue.
        #           Attention : PAS "X" en dur ! La boite symbole.
        plateau[case - 1] = ____

        # ETAPE 4 : un tour de plus. Sinon la boucle ne
        #           s'arretera JAMAIS.
        tour = ____ + 1

        # ETAPE 5 : on passe la main a l'autre joueur.
        if symbole == "X":
            symbole = "____"
            joueur = ____
        else:
            symbole = "____"
            joueur = ____

    else:
        print("Coup impossible : la case n'existe pas, ou elle est deja prise.")


# -----------------------------------------------------
#  PARTIE 2 : apres la boucle
# -----------------------------------------------------
#  ETAPE 6 : ces lignes sont COLLEES A GAUCHE, donc elles
#            ne sont pas dans la boucle : elles ne se font
#            qu'une seule fois, a la fin.
print("")
print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])
print("")
print("Le plateau est plein ! Neuf coups joues.")


# =====================================================
#  TU AS FINI ? LEVE LA CARTE BLEUE.
#
#  DEFI 1 : affiche le numero du tour a chaque fois :
#           "Tour 4 sur 9".
#
#  DEFI 2 : compte les coups refuses, et affiche le total
#           a la fin.
#
#  DEFI 3 : fais commencer les O au lieu des X. Combien de
#           lignes as-tu du changer ?
#
#  DEFI 4 : essaie  while tour < 5 .  Que se passe-t-il ?
#           Et  while tour < 20  ?  Explique.
# =====================================================
