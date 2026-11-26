# =====================================================================
#  L'EXERCICE DE LA SEANCE 11  -  LE BULLETIN
#  CORRIGE  -  POUR L'ENSEIGNANT
#
#  Rien au-dela de la seance 11 : print, input, int(), str(), le +,
#  les operateurs, if / elif / else.
#
#  RAPPEL DE LA CONSIGNE : l'algorithme sur le cahier D'ABORD.
#  Pas de clavier avant d'avoir montre son algorithme.
# =====================================================================

print("=" * 38)
print("          LE BULLETIN")
print("=" * 38)
print("")

# --- ETAPE 1 : qui est-ce ? ------------------------------------------
nom = input("Nom de l'eleve : ")

# --- ETAPE 2 : les trois notes ---------------------------------------
note1 = input("Note de Mathematiques /20 : ")
note1 = int(note1)
note2 = input("Note de Francais /20      : ")
note2 = int(note2)
note3 = input("Note d'Informatique /20   : ")
note3 = int(note3)

# --- ETAPE 3 : la moyenne --------------------------------------------
#  On garde la partie entiere : int() coupe ce qu'il y a apres la virgule.
moyenne = int((note1 + note2 + note3) / 3)

# --- ETAPE 4 : LA CASCADE  (le coeur de l'exercice) ------------------
#  Du PLUS EXIGEANT au MOINS EXIGEANT. Dans l'autre sens, tout le
#  monde serait "Passable".
if moyenne >= 16:
    mention = "TRES BIEN"
elif moyenne >= 14:
    mention = "BIEN"
elif moyenne >= 12:
    mention = "ASSEZ BIEN"
elif moyenne >= 10:
    mention = "PASSABLE"
else:
    mention = "A REVOIR"

# --- ETAPE 5 : le bulletin -------------------------------------------
print("")
print("=" * 38)
print(" Eleve   : " + nom)
print(" Maths   : " + str(note1) + " / 20")
print(" Francais: " + str(note2) + " / 20")
print(" Info    : " + str(note3) + " / 20")
print("-" * 38)
print(" Moyenne : " + str(moyenne) + " / 20")
print(" Mention : " + mention)
print("=" * 38)


# --- POUR CEUX QUI FINISSENT (sans aller jusqu'a l'exo etoile) -------
#  Ajouter une ligne d'appreciation, avec une DEUXIEME cascade :
#      if moyenne >= 14:
#          print(" Continue comme ca !")
#      elif moyenne >= 10:
#          print(" Tu peux faire mieux.")
#      else:
#          print(" On se voit apres le cours.")

# =====================================================================
#  CE QU'ON REGARDE EN CORRIGEANT
#    - L'ALGORITHME EST-IL SUR LE CAHIER ? C'est le premier livrable.
#    - les TROIS int() sont-ils la, un par note ?
#    - la cascade va-t-elle du plus grand au plus petit ?
#      (dans l'autre sens, tout le monde est PASSABLE : faites-le
#       essayer a celui qui s'est trompe, il verra tout de suite)
#    - y a-t-il UN SEUL if au debut, et des elif ensuite ?
#      (quatre if separes marchent aussi ici, mais Python pose alors
#       quatre questions au lieu d'une : on le dit, on ne le sanctionne pas)
#    - le else final est-il la ? Sans lui, une note de 5 n'affiche rien.
#    - les str() sont-ils la dans le bulletin ?
# =====================================================================
