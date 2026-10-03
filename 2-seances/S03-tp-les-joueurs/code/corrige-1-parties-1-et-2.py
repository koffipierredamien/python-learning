# =====================================================================
#  TP n°1  -  CORRIGE DE L'ENSEIGNANT
#  Parties 0, 1 et 2  :  afficher, puis les variables
#  (etoiles 1 et 2 comprises)
#
#  Fichier de l'eleve : tp1_tonprenom.py
#  Ici, le prenom d'exemple est Mehdi : remplacez-le par le votre
#  si vous projetez ce corrige.
# =====================================================================


# ---------------------------------------------------------------------
#  EXERCICE 0  -  la mise en route
# ---------------------------------------------------------------------
print("TP1 - Mehdi")
print("")


# ---------------------------------------------------------------------
#  EXERCICES 1.1, 1.2 et 1.3  -  trois lignes, un cadre, une ligne vide
#
#  L'ordre compte : le cadre (1.2) entoure les trois lignes (1.1),
#  et la ligne vide (1.3) se glisse juste apres le cadre du haut.
# ---------------------------------------------------------------------
print("------------------------------")   # 1.2  le cadre du haut
print("")                                 # 1.3  LA reponse : deux guillemets, rien dedans
print("Mehdi")                            # 1.1  les trois lignes
print("15 ans")
print("Casablanca")
print("------------------------------")   # 1.2  le cadre du bas
print("")


# ---------------------------------------------------------------------
#  ETOILE 1  -  multiplier du texte, et la virgule
# ---------------------------------------------------------------------
print("-" * 30)                 # repete le tiret 30 fois
print("=" * 30)
print("ABC" * 3)                # ABCABCABC
print("")

#  Le cadre de l'exercice 1.2, refait avec la multiplication :
print("-" * 30)
print("")
print("Mehdi")
print("15 ans")
print("Casablanca")
print("-" * 30)
print("")

#  La decouverte a faire remarquer : la virgule met un espace toute seule.
print("J'ai" , "15" , "ans")    # ->  J'ai 15 ans
print("J'ai" + "15" + "ans")    # ->  J'ai15ans
print("")


# ---------------------------------------------------------------------
#  EXERCICE 2.1  -  trois boites, trois phrases
#
#  age est entre guillemets : c'est du TEXTE. Sans guillemets, Python
#  refuse de le coller a du texte avec le + (il le dira en rouge).
# ---------------------------------------------------------------------
prenom = "Mehdi"
age = "15"
ville = "Casablanca"

print("Je m'appelle " + prenom)
print("J'ai " + age + " ans")
print("J'habite a " + ville)
print("")


# ---------------------------------------------------------------------
#  EXERCICE 2.2  -  la boite change
#
#  Reponse attendue : la boite ne garde qu'une seule chose a la fois.
#  A partir de cette ligne, c'est la nouvelle valeur qui s'affiche.
# ---------------------------------------------------------------------
ville = "Rabat"
print("J'habite a " + ville)        # affiche Rabat, plus Casablanca
print("")


# ---------------------------------------------------------------------
#  EXERCICE 2.3  -  une boite dans une boite
# ---------------------------------------------------------------------
message = "Bonjour " + prenom + " !"
print(message)

presentation = prenom + " de " + ville
print(presentation)
print("")


# ---------------------------------------------------------------------
#  ETOILE 2 a)  -  la grille rangee dans des boites
#
#  Le dessin n'est ecrit qu'UNE SEULE FOIS, et sert cinq fois.
#  C'est du temps gagne pour la partie 4.
# ---------------------------------------------------------------------
ligne = " . | . | ."
separateur = "---+---+---"

print(ligne)
print(separateur)
print(ligne)
print(separateur)
print(ligne)
print("")


# ---------------------------------------------------------------------
#  ETOILE 2 b)  -  echanger le contenu de deux boites
#
#  LE morceau difficile de la feuille. Presque tous ecrivent
#      boite1 = boite2
#      boite2 = boite1
#  et obtiennent deux fois O : des la premiere ligne, le X est perdu.
#  Il faut poser le X quelque part AVANT de lacher la boite.
# ---------------------------------------------------------------------
boite1 = "X"
boite2 = "O"

cache = boite1          # <-- LA ligne a trouver : on met le X de cote
boite1 = boite2
boite2 = cache

print(boite1)           # affiche O
print(boite2)           # affiche X
