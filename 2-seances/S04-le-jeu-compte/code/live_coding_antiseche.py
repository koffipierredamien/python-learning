# -*- coding: utf-8 -*-
"""
=============================================================================
  SEANCE 4  -  LE LIVE CODING DE L'ENSEIGNANT
=============================================================================
  TROIS NOTIONS, TROIS DEMONSTRATIONS COURTES :

     12 h 22 - 12 h 35   etapes A, B, C   ->  int() et str()
     12 h 35 - 12 h 50   atelier 1 : la calculatrice d'age
     12 h 50 - 13 h      etape D          ->  le compteur
     13 h 10 - 13 h 30   etapes E, F, G   ->  les operateurs, puis decider
     13 h 30 - 13 h 52   atelier 2 : le projet

  REGLE D'OR : "JE CODE, VOUS PREDISEZ."
  AVANT LA SEANCE : police de Thonny en taille 18 minimum.
=============================================================================
"""

# =============================================================================
#  ETAPE A  (4 min)  -  input() REND TOUJOURS DU TEXTE
# =============================================================================
age = input("Quel age as-tu ? ")
print(age)

#  Puis vous ajoutez UNE ligne, et vous demandez avant de lancer :
#  print(age + 10)        <-- ERREUR ROUGE : TypeError
#
#    "str, c'est string : du TEXTE. input rend TOUJOURS du texte,
#     meme quand vous tapez un nombre."


# =============================================================================
#  ETAPE B  (4 min)  -  int() ET str()
# =============================================================================
age = input("Quel age as-tu ? ")
age = int(age)
print(age + 10)
print("Dans 10 ans tu auras " + str(age + 10) + " ans")

#    "int : traite ca comme un NOMBRE, pour calculer.
#     str : traite ca comme du TEXTE, pour coller avec le +."


# =============================================================================
#  ETAPE C  (3 min)  -  L'ERREUR VOLONTAIRE : on tape  douze
# =============================================================================
#    "ValueError : invalid literal for int. Je t'ai demande un nombre,
#     tu m'as donne un mot. Je ne sais pas faire."
#  >>> ON NE REPARE PAS : se proteger demande une condition... qu'on voit
#      justement dans une heure. Dites-le-leur, ca cree l'attente.


# =============================================================================
#  ETAPE D  (8 min)  -  LE COMPTEUR  (apres l'atelier 1)
# =============================================================================
#  D'abord SANS machine, avec une vraie boite et des papiers :
#     "Je prends ce qu'il y a dedans, j'ajoute 1, je REMETS dans la meme boite."

tour = 0
tour = tour + 1
tour = tour + 1
print(tour)

#  >>> AVANT DE LANCER : "0, 1, ou 2 ?"
#    "La ligne est TOUJOURS la meme et le resultat change. Le signe =
#     n'est pas 'egal'. C'est 'RANGE DANS'."


# =============================================================================
#  ETAPE E  (5 min)  -  LES OPERATEURS
# =============================================================================
#  LE MOT DU JOUR, a dire avant de taper quoi que ce soit :
#    "Un OPERATEUR, c'est un petit signe qui TRAVAILLE sur ce qu'il y a de
#     chaque cote de lui. Vous en utilisez depuis la seance 2 : le + .
#     Il en existe DEUX FAMILLES."
#
#  AU TABLEAU, DEUX COLONNES  (ils remplissent la premiere de memoire) :
#
#     OPERATEURS DE CALCUL          OPERATEURS DE COMPARAISON
#     --------------------          -------------------------
#       +   additionner / coller      >    plus grand que
#       -   soustraire                <    plus petit que
#       *   multiplier                >=   plus grand OU EGAL
#       /   diviser                   <=   plus petit OU EGAL
#                                     ==   EST EGAL A
#                                     !=   EST DIFFERENT DE
#
#     -> donnent un RESULTAT         -> donnent une REPONSE : True / False
#
#  LA PHRASE A FAIRE RETENIR :
#    "Les operateurs de calcul donnent un RESULTAT.
#     Les operateurs de comparaison donnent une REPONSE."

print(5 > 3)
print(5 < 3)
print(5 >= 5)
print(5 != 5)

#  >>> AVANT DE LANCER : "qu'est-ce que ca peut bien afficher ?"
#      Reponse : True False True False
#
#    ">= se lit 'plus grand ou egal'. Les deux signes dans cet ordre,
#     sans espace au milieu."
#
#  LE PIEGE A MONTRER TOUT DE SUITE :
#     =   c'est RANGE DANS                  (age = 15)
#     ==  c'est l'operateur EST EGAL A      (age == 15)
#  Ecrivez les deux au tableau, l'un sous l'autre. Laissez-les affiches.


# =============================================================================
#  ETAPE F  (8 min)  -  DECIDER : if / else
# =============================================================================
age = int(input("Quel age as-tu ? "))

if age > 17:
    print("Tu es un Jeremiah Geek !")
else:
    print("Tu es un Jerusalem Geek !")

#  Vous tapez TRES lentement, en nommant chaque geste :
#     "if, deux-points. Je passe a la ligne. Et maintenant, REGARDEZ :
#      Thonny m'a decale de quatre espaces tout seul. Ce decalage n'est pas
#      de la decoration : c'est lui qui dit CE QUI EST DANS le if.
#      else, deux-points, et on redecale."
#
#  >>> On lance DEUX fois, avec deux ages differents. C'est la demonstration :
#      le MEME programme ne fait pas la meme chose.


# =============================================================================
#  ETAPE G  (4 min)  -  L'ERREUR VOLONTAIRE DU BLOC
# =============================================================================
#  Vous effacez le decalage de la ligne qui suit le if :
#
#       if age > 17:
#       print("Tu es un Jeremiah Geek !")        <-- collee a gauche
#
#    "IndentationError : expected an indented block.
#     Il me dit : apres les deux-points, il faut DECALER.
#     Sans le decalage, il ne sait pas ce qui appartient au if."
#
#  Remettez les 4 espaces devant eux, relancez, ca marche.
#  >>> C'est l'erreur qu'ils verront le plus aujourd'hui. Qu'ils la voient
#      d'abord sur VOTRE ecran, calmement.


# =============================================================================
#  LES ERREURS QUI VONT ARRIVER PENDANT LES ATELIERS
# =============================================================================
#   TypeError .............. texte et nombre melanges : int() ou str().
#   ValueError ............. int() sur un mot.
#   IndentationError ....... il manque les 4 espaces apres les deux-points.
#   SyntaxError sur le if .. les deux-points oublies, ou = au lieu de ==.
#   = au lieu de == ....... un seul = est un ORDRE, == est l'operateur qui COMPARE.
#   Le compteur reste a 1 .. tour = 1 au lieu de tour = tour + 1.
#   Les deux messages s'affichent ... l'eleve a mis deux print dans le if,
#                            au lieu d'un dans le if et un dans le else.
#
#  Le dictionnaire complet : 1-methode/annexes/dictionnaire-des-erreurs.pdf
# =============================================================================
