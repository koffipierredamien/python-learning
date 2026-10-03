# =====================================================================
#  TP n°1  -  CORRIGE DE L'ENSEIGNANT
#  Partie 5  :  la chasse aux bugs
#
#  Les cinq programmes casses sont en commentaire, la correction
#  juste en dessous. Ce fichier TOURNE : il affiche cinq fois Bonjour.
#
#  CE QU'ON CHERCHE ICI, ce n'est pas la correction - ils la trouvent
#  vite - c'est qu'ils sachent DIRE CE QUE LE MESSAGE RACONTE.
#  Demandez-leur a voix haute : "il dit quoi, exactement ?"
# =====================================================================


# ---------------------------------------------------------------------
#  BUG 1   SyntaxError
#     print("Bonjour)
#
#  Il manque le guillemet fermant. Les guillemets vont par deux,
#  comme une paire de chaussures.
# ---------------------------------------------------------------------
print("Bonjour")


# ---------------------------------------------------------------------
#  BUG 2   NameError: name 'Bonjour' is not defined
#     print(Bonjour)
#
#  Du texte ecrit SANS guillemets : Python croit que c'est une boite,
#  il la cherche, et il n'en trouve aucune de ce nom.
# ---------------------------------------------------------------------
print("Bonjour")


# ---------------------------------------------------------------------
#  BUG 3   NameError: name 'Print' is not defined
#     Print("Bonjour")
#
#  La majuscule. La commande s'ecrit  print , tout en minuscules.
#  Pour Python, Print et print sont deux mots differents.
# ---------------------------------------------------------------------
print("Bonjour")


# ---------------------------------------------------------------------
#  BUG 4   SyntaxError
#     print("Bonjour"
#
#  Il manque la parenthese fermante. A noter : Python signale souvent
#  l'erreur sur la ligne SUIVANTE - on regarde toujours la ligne
#  d'au-dessus.
# ---------------------------------------------------------------------
print("Bonjour")


# ---------------------------------------------------------------------
#  BUG 5   NameError: name 'Nom' is not defined
#     nom = input("Ton nom ? ")
#     print("Bonjour " + Nom)
#
#  La boite s'appelle  nom , on l'appelle  Nom . Ce n'est pas la meme :
#  une majuscule suffit a en faire une autre boite.
# ---------------------------------------------------------------------
nom = input("Ton nom ? ")
print("Bonjour " + nom)
