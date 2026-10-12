# =====================================================================
#  LE QUIZ DES GEEKS  -  LA CORRECTION
#  Exercice de maison du 12 octobre 2026  -  Jeremiah Geeks
#
#  Tout ce qu'on a appris depuis le debut est dedans :
#     print · les variables · input · le +  ·  int() et str()
#     le compteur  score = score + 1  ·  ==  et  >  ·  if / else
#
#  Ce fichier tourne tel quel : F5 dans Thonny.
# =====================================================================


# --- ETAPE 1 : l'accueil ---------------------------------------------
print("=" * 35)
print("      LE QUIZ DES GEEKS")
print("=" * 35)
print("")

joueur = input("Quel est ton nom ? ")
print("Bonjour " + joueur + " ! Trois questions t'attendent.")
print("")


# --- ETAPE 2 : le compteur part de zero ------------------------------
score = 0


# --- ETAPE 3 : question 1  (un NOMBRE) -------------------------------
print("QUESTION 1")
reponse = input("Combien font 3 + 4 ? ")
reponse = int(reponse)          # la reponse du joueur est du TEXTE : on la transforme

if reponse == 7:
    print("Bravo, c'est juste !")
    score = score + 1
else:
    print("Non, la bonne reponse etait 7.")
print("")


# --- ETAPE 4 : question 2  (du TEXTE) --------------------------------
print("QUESTION 2")
reponse = input("Que donne  \"3\" + \"4\"  en Python ? ")

if reponse == "34":
    print("Bravo, c'est juste !")
    score = score + 1
else:
    print("Non, la bonne reponse etait 34 : deux textes sont colles.")
print("")


# --- ETAPE 5 : question 3  (un NOMBRE) -------------------------------
print("QUESTION 3")
reponse = input("Combien de cases a le plateau XO ? ")
reponse = int(reponse)

if reponse == 9:
    print("Bravo, c'est juste !")
    score = score + 1
else:
    print("Non, la bonne reponse etait 9.")
print("")


# --- ETAPE 6 : le bilan ----------------------------------------------
print("=" * 35)
print(joueur + ", ton score est de " + str(score) + " sur 3.")

if score > 1:
    print("Tu es un vrai Geek !")
else:
    print("Il faut reviser, mais tu vas y arriver !")
print("=" * 35)


# =====================================================================
#  LES DEUX BONUS
# =====================================================================

# --- BONUS 1 : le nombre de points qui manquent ----------------------
print("")
print("Il te manquait " + str(3 - score) + " point(s) pour le sans-faute.")

# --- BONUS 2 : la quatrieme question ---------------------------------
print("")
print("QUESTION BONUS")
age = input("Quel age as-tu ? ")
age = int(age)

if age > 11:
    print(joueur + ", tu es un Jeremiah Geek.")
else:
    print(joueur + ", tu es un Jerusalem Geek.")


# =====================================================================
#  CE QU'ON REGARDE EN CORRIGEANT
#    - la ligne  score = 0  est-elle AVANT les questions ?
#    - la ligne  reponse = int(reponse)  est-elle la pour les questions
#      1 et 3 (des nombres), et ABSENTE pour la question 2 (du texte) ?
#    - le  ==  est-il bien double dans les  if  ?
#    - les 4 espaces de decalage sont-ils la sous chaque if et chaque else ?
#    - le  str(score)  est-il present dans la phrase du bilan ?
# =====================================================================
