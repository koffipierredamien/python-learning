# =====================================================================
#  LE GRAND PARCOURS  -  CORRIGE DE L'ENSEIGNANT
#  Les huit paliers, puis les trois defis.
#  Ce fichier tourne tel quel : F5 et repondez aux questions.
# =====================================================================


# --- PALIER 1 : afficher --------------------------------------------
print("-" * 30)
print("Mehdi")
print("Jeremiah Geeks")
print("Jeremiah Geek")
print("-" * 30)
print("")


# --- PALIER 2 : la boite --------------------------------------------
joueur = "Mehdi"
print(joueur)        # le CONTENU de la boite
print("joueur")      # le MOT, a cause des guillemets

joueur = "Joyce"     # la boite ne garde qu'une seule chose a la fois
print(joueur)
print("")

#  Ce qu'on attend sur la feuille : "sans guillemets il affiche ce qu'il
#  y a dans la boite, avec guillemets il affiche le mot".


# --- PALIER 3 : coller ----------------------------------------------
print("Bienvenue " + joueur + " !")
print("")

#  L'erreur frequente :  "Bienvenue" + joueur  ->  BienvenueJoyce
#  On fait remarquer l'espace manquant, on ne le corrige pas a leur place.


# --- PALIER 4 : demander --------------------------------------------
couleur = input("Ta couleur preferee ? ")
print("Tres bien, " + joueur + ", ta couleur est le " + couleur + ".")
print("")


# --- PALIER 5 : texte ou nombre -------------------------------------
print("3" + "4")     # 34   -> texte + texte : les deux sont colles
print(3 + 4)         # 7    -> nombre + nombre : une addition

#  print("3" + 4)    <-- TypeError : texte + nombre
#  Les deux reparations possibles :
print(int("3") + 4)  # 7    -> on transforme le texte en nombre
print("3" + str(4))  # 34   -> on transforme le nombre en texte
print("")


# --- PALIER 6 : l'age -----------------------------------------------
age = input("Quel age as-tu ? ")
age = int(age)
print("Dans 10 ans tu auras " + str(age + 10) + " ans")
print("")


# --- PALIER 7 : le compteur (decouverte) ----------------------------
tour = 0
tour = tour + 1
tour = tour + 1
print(tour)          # 2   -> la meme ligne, et pourtant le resultat change
print("")

#  C'est le pont vers la lecon qui suit : "= ne veut pas dire egal,
#  mais RANGE DANS".


# --- PALIER 8 : la decision (decouverte) ----------------------------
age = int(input("Quel age as-tu ? "))

if age > 11:
    print("Tu es un Jeremiah Geek !")
else:
    print("Tu es un Jerusalem Geek !")
print("")

#  On le lance DEUX fois en classe, avec deux ages : le meme programme
#  ne fait pas la meme chose. Il a choisi.


# =====================================================================
#  LES TROIS DEFIS  (carte bleue)
# =====================================================================

# --- DEFI A : la fiche du joueur, encadree --------------------------
nom = input("Ton prenom ? ")
age_texte = input("Ton age ? ")
couleur2 = input("Ta couleur ? ")

print("=" * 30)
print("       FICHE DU JOUEUR")
print("=" * 30)
print("Prenom  : " + nom)
print("Age     : " + age_texte)
print("Couleur : " + couleur2)
print("=" * 30)
print("")


# --- DEFI B : le compteur de scores ---------------------------------
points = 0

score = int(input("Combien de points au 1er tour ? "))
points = points + score

score = int(input("Combien de points au 2e tour ? "))
points = points + score

score = int(input("Combien de points au 3e tour ? "))
points = points + score

print("Total : " + str(points) + " points")
print("Il te manque " + str(20 - points) + " points pour atteindre 20.")
print("")


# --- DEFI C : le controle d'age -------------------------------------
age3 = int(input("Quel age as-tu ? "))

if age3 > 11:
    print(nom + ", tu es dans la classe des Jeremiah Geeks.")
else:
    print(nom + ", tu es dans la classe des Jerusalem Geeks.")


# =====================================================================
#  CE QU'ON REGARDE EN CIRCULANT
#   palier 2  -> sait-il dire la difference print(x) / print("x") ?
#   palier 5  -> sait-il NOMMER l'erreur (TypeError) avant de reparer ?
#   palier 6  -> met-il int() a l'entree ET str() a la sortie ?
#   palier 7  -> a-t-il predit 2, ou a-t-il dit 1 ?  (note le nom)
#   palier 8  -> le decalage de 4 espaces est-il la, sans aide ?
# =====================================================================
