# =====================================================================
#  LA MEDAILLE  -  CORRIGE, POUR L'ENSEIGNANT ET LES PARENTS
#
#  L'enonce ne donne AUCUNE consigne de code : il donne un bareme et
#  un ecran attendu. Tout l'exercice est de trouver DANS QUEL ORDRE
#  poser les questions.
#
#  Les messages peuvent varier d'un enfant a l'autre. Ce qui compte,
#  c'est que les six essais de l'enonce tombent juste.
# =====================================================================

print("=" * 40)
print("        LE CONCOURS DU QUARTIER")
print("=" * 40)
print("")

points = input("Combien de points sur 100 ? ")
points = int(points)

print("")

#  L'ORDRE EST TOUT L'EXERCICE.
#
#  1. On elimine d'abord l'IMPOSSIBLE. Tant qu'on n'a pas ecarte les
#     nombres qui n'existent pas, on ne peut rien juger du tout.
#  2. Puis le cas le PLUS PRECIS : exactement 100. Il n'y a qu'un seul
#     nombre qui le satisfait. Place apres le  >= 90 , il ne serait
#     JAMAIS atteint, parce que 100 est deja plus grand que 90.
#  3. Puis les tranches, de la plus haute a la plus basse.
#  4. Le else final attrape tout le reste : sans lui, un enfant qui
#     tape 30 ne verrait rien s'afficher.
if points < 0 or points > 100:
    print("Ce nombre n'existe pas.")
elif points == 100:
    print("SANS FAUTE ! Tu es en finale.")
elif points >= 90:
    print("Medaille d'OR")
elif points >= 75:
    print("Medaille d'ARGENT")
elif points >= 60:
    print("Medaille de BRONZE")
else:
    print("Participant. Reviens l'annee prochaine !")

print("")
print("=" * 40)


# =====================================================================
#  LES SIX ESSAIS DE L'ENONCE
#    100  ->  SANS FAUTE        (LE PIEGE : surtout pas "Medaille d'OR")
#     90  ->  Medaille d'OR
#     74  ->  Medaille de BRONZE
#     59  ->  Participant
#      0  ->  Participant       (LE SECOND PIEGE : 0 EXISTE)
#    120  ->  Ce nombre n'existe pas.
#
#  LES TROIS ERREURS QU'ON VERRA
#    - le  == 100  ecrit APRES le  >= 90  : il ne sert alors a rien.
#      Ne corrigez pas la ligne : faites taper 100 et lire l'ecran.
#    - le test de l'impossible ecrit EN DERNIER, ou pas ecrit du tout.
#    - "points <= 0" au lieu de "points < 0", qui refuse le zero.
#      Faites taper 0 : un enfant peut avoir zero point sans tricher.
#
#  CE QU'ON REGARDE EN CORRIGEANT
#    - l'algorithme en francais existe-t-il, avant le code ?
#    - y a-t-il UN SEUL if, puis des elif, puis un else ?
#    - le int() est-il la ? Sans lui, les comparaisons sont fausses.
# =====================================================================
