# -*- coding: utf-8 -*-
"""Le formulaire de revision, bati sur le diaporama de la revision generale.

   REGLE DE CE FICHIER : le formulaire se suffit a lui-meme.
   Aucune question ne renvoie a une seance, a un atelier, a un projet ou
   a un document exterieur. Tout ce qu'il faut pour repondre est ECRIT
   DANS LA QUESTION : la liste est redonnee a chaque fois, le programme
   est recopie en entier, et rien ne depend de la question precedente.
   Un enfant qui ouvrirait ce formulaire sans avoir rien suivi doit
   pouvoir le lire et le comprendre."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quiz_hebdo import ecrire

#  Le programme du decalage : donne en entier, deux fois, pour que les
#  questions 11 et 12 ne dependent pas l'une de l'autre.
PROG_POINTS = ('points = 100\n'
               'reponse = int(input("Combien font 7 x 8 ? "))\n'
               '\n'
               'if reponse == 56:\n'
               '    print("Juste !")\n'
               'else:\n'
               '    points = points - 40\n'
               '    print("Il te reste " + str(points))')

#  Le programme du coup valide : meme principe pour les questions 15 et 16.
PROG_CASE = ('plateau = ["1", "2", "X", "4", "5", "6", "7", "8", "9"]\n'
             'case = 3\n'
             '\n'
             'if case >= 1 or case <= 9 and plateau[case - 1] == str(case):\n'
             '    plateau[case - 1] = "O"\n'
             '    print("Pose !")\n'
             'else:\n'
             '    print("Coup impossible.")')

NOTE_CASE = ('Dans cette liste, la case 3 est deja prise : elle contient "X" '
             'au lieu de "3".\nLe test  plateau[case - 1] == str(case)  veut dire : '
             '« la case contient encore son numero, donc elle est libre ».\n\n')

ecrire(11, "S10-revision-generale",
 titre="Revision generale — vingt questions",
 sujet="texte et nombres, listes, decalage, and / or, et la repetition",
 intro="Vingt questions pour verifier ce que tu sais faire. Chacune se repond avec ce qui est ecrit dedans : tu n'as besoin de rien d'autre, ni d'un cahier, ni d'un ordinateur. Tu peux la refaire autant de fois que tu veux.",
 rappels=["input rend TOUJOURS du texte",
          "dans une liste, les numeros commencent a ZERO",
          "le decalage dit QUI DEPEND DE QUI",
          "and : il faut TOUT   ·   or : il suffit d'UN",
          "une repetition s'arrete parce que quelque chose AVANCE"],
 fichier="quiz-revision-generale.gs",
 remplacements=[
   (" *  AcProKids Coding Camp — Quiz de la semaine n°11",
    " *  AcProKids Coding Camp — REVISION GENERALE"),
   (""" *  POUR LES ENFANTS QUI N'ONT PAS D'ORDINATEUR : ils le font A LA PLACE
 *  de l'exercice de maison. Un telephone suffit.""",
    """ *  POUR TOUT LE MONDE. Un telephone suffit, et rien d'autre.
 *
 *  LE FORMULAIRE SE SUFFIT A LUI-MEME : aucune question ne renvoie a
 *  une seance, a un atelier ni a un projet. Les listes sont redonnees
 *  a chaque question, les programmes recopies en entier, et aucune
 *  question ne depend de la precedente. On peut donc le renvoyer tel
 *  quel dans un mois, ou le donner a un enfant qui etait absent."""),
   ("""'C\\'est envoye ! Clique sur « Afficher le score » pour voir ta note et les explications. ' +
      'A samedi, 12 h !');""",
    """'C\\'est envoye ! Clique sur « Afficher le score » pour voir ta note et les explications. ' +
      'Tu peux refaire ce quiz autant de fois que tu veux.');"""),
 ],
 sections={0:  ("PARTIE A — Texte ou nombre",
                "Ce que fait l'ordinateur quand on melange du texte et des nombres."),
           4:  ("PARTIE B — Les listes",
                "Une liste, et le numero de chaque chose a l'interieur."),
           8:  ("PARTIE C — Le decalage",
                "Quatre espaces de plus, et le programme ne fait plus la meme chose."),
           12: ("PARTIE D — and, or",
                "Deux petits mots qui decident de tout dans une condition."),
           16: ("PARTIE E — Repeter",
                "Repeter quelque chose, et savoir s'arreter.")},
 qs=[
 # ---------------------------------------------------------- A
 ('print("7" + "7")\n\nQu\'est-ce qui s\'affiche ?',
  "77", ["14", "7 7", "une erreur rouge"],
  "Il y a des guillemets autour : ce sont deux TEXTES. Le + colle les textes bout a bout, il ne les additionne pas."),
 ('age = input("Ton age ? ")\nprint(age * 2)\n\nLe joueur tape 12. Qu\'est-ce qui s\'affiche ?',
  "1212", ["24", "12", "une erreur rouge"],
  "input rend TOUJOURS du texte, meme quand on tape des chiffres. Et un texte multiplie par 2, c'est le texte ecrit deux fois de suite."),
 ('print(int("7") + int("7"))\n\nQu\'est-ce qui s\'affiche ?',
  "14", ["77", "7 7", "une erreur rouge"],
  "int() transforme le texte \"7\" en vrai nombre 7. Et deux nombres, le + les additionne."),
 ('a = input("Un nombre : ")\nb = input("Un autre : ")\n\nQue faut-il ecrire pour afficher leur SOMME ?',
  "print(int(a) + int(b))", ["print(a + b)", "print(str(a) + str(b))", "print(a) + print(b)"],
  "Tant qu'on ne les a pas transformes en nombres, a et b sont deux textes, que le + met bout a bout."),

 # ---------------------------------------------------------- B
 ('equipe = ["A", "B", "C", "D"]\nprint(equipe[3])\n\nQu\'est-ce qui s\'affiche ?',
  "D", ["C", "A", "une erreur rouge"],
  "Les numeros commencent a ZERO : A est le 0, B le 1, C le 2, D le 3."),
 ('equipe = ["A", "B", "C", "D"]\nequipe[1] = equipe[2]\nprint(equipe)\n\nQu\'est-ce qui s\'affiche ?',
  "['A', 'C', 'C', 'D']", ["['A', 'B', 'C', 'D']", "['A', 'B', 'B', 'D']", "une erreur rouge"],
  "On LIT equipe[2], qui vaut C, et on le RANGE dans equipe[1]. Le B est ecrase, le C reste a sa place : ca va de droite a gauche."),
 ('sacs = ["riz", "sucre", "sel", "farine", "huile"]\n\nQuel numero faut-il ecrire entre les crochets pour obtenir "huile" ?',
  "4", ["5", "3", "Aucun : il faut ecrire son nom"],
  "Les numeros commencent a ZERO : riz est 0, sucre 1, sel 2, farine 3, huile 4."),
 ('sacs = ["riz", "sucre", "sel", "farine", "huile"]\nprint(sacs[5])\n\nQue se passe-t-il ?',
  "Une erreur rouge : IndexError", ["Ca affiche huile", "Ca n'affiche rien", "Ca affiche 5"],
  "Cinq elements, ce sont les numeros 0, 1, 2, 3 et 4. Le numero 5 n'existe pas : Python s'arrete et le dit."),

 # ---------------------------------------------------------- C
 ('x = 10\nif x > 5:\n    print("A")\nprint("B")\n\nQu\'est-ce qui s\'affiche ?',
  "A puis B", ["A seulement", "B seulement", "rien du tout"],
  "print(\"B\") est colle a gauche : il est DEHORS du if, donc il s'affiche quoi qu'il arrive."),
 ('points = 50\nif points > 50:\n    points = points + 10\nprint(points)\n\nQu\'est-ce qui s\'affiche ?',
  "50", ["60", "0", "une erreur rouge"],
  "50 n'est pas PLUS GRAND que 50. La condition est fausse, la ligne decalee est sautee, et points n'a pas bouge."),
 (PROG_POINTS + '\n\nPourquoi le nombre de points ne s\'affiche-t-il QUE lorsque la reponse est fausse ?',
  "Parce que la ligne qui l'affiche est DANS le else",
  ["Parce que str() ne marche pas dans un if", "Parce qu'il manque un deuxieme else",
   "Parce que points vaut 100 au depart"],
  "Decalee sous le else, cette ligne appartient au else : elle ne s'execute que si la condition est fausse."),
 (PROG_POINTS + '\n\nSANS AJOUTER AUCUNE LIGNE, comment faire pour que le nombre de points s\'affiche dans les DEUX cas ?',
  "On recule la derniere ligne de 4 espaces, pour la coller a gauche",
  ["On l'ecrit une deuxieme fois dans le if", "On enleve le else",
   "On met le if et le else a la meme hauteur"],
  "Collee a gauche, la ligne n'appartient plus au else : elle appartient au programme, et s'affiche dans tous les cas."),

 # ---------------------------------------------------------- D
 ('age = 11\nprint(age >= 12 and age <= 18)\n\nQu\'est-ce qui s\'affiche ?',
  "False", ["True", "11", "une erreur rouge"],
  "La premiere question est fausse : 11 n'est pas plus grand ou egal a 12. Avec and, une seule fausse suffit pour que tout soit faux."),
 ('Les cases d\'un jeu portent les numeros 1 a 9.\n\nPour REFUSER un numero de case qui n\'existe pas, j\'ecris :',
  "case < 1 or case > 9", ["case < 1 and case > 9", "case >= 1 or case <= 9", "case > 1 or case < 9"],
  "Une seule des deux raisons suffit pour refuser : c'est or. Avec and, il faudrait un nombre a la fois plus petit que 1 ET plus grand que 9 : ca n'existe pas, donc rien ne serait jamais refuse."),
 (NOTE_CASE + PROG_CASE + '\n\nQu\'est-ce qui s\'affiche ?',
  "Pose !   (le O s'ecrit par-dessus le X)",
  ["Coup impossible.", "une erreur rouge", "rien du tout"],
  "case >= 1 est vrai. Avec or, il suffit d'une seule reponse vraie : le reste de la ligne n'est meme plus regarde, et le coup passe."),
 (PROG_CASE + '\n\nLa case 3 est deja prise. Quel mot faut-il changer pour que le coup soit REFUSE ?',
  "le premier or, qu'il faut remplacer par and",
  ["le str(), qu'il faut enlever", "le - 1, qu'il faut enlever", "le >= qu'il faut mettre en >"],
  "Avec and, les TROIS questions comptent : le numero est assez grand, il est assez petit, ET la case est libre."),

 # ---------------------------------------------------------- E
 ('Un dessin s\'affiche avec 5 lignes de print.\n\nPour l\'afficher TROIS fois de suite, en recopiant les lignes a chaque fois, combien de lignes de print faut-il ecrire en tout ?',
  "15", ["5", "8", "3"],
  "Cinq lignes, trois fois : quinze. C'est pour eviter ce genre de recopiage qu'existe la repetition."),
 ('tour = 0\nwhile tour < 3:\n    print("A")\n    tour = tour + 1\n\nCombien de A s\'affichent ?',
  "3", ["2", "4", "sans fin"],
  "tour vaut 0, puis 1, puis 2 : trois passages. A 3, la condition devient fausse et la repetition s'arrete."),
 ('tour = 0\nwhile tour < 3:\n    print("A")\n\nQu\'est-ce qui se passe ?',
  "Ca affiche A sans fin", ["Ca affiche A une seule fois", "Une erreur rouge", "Rien ne s'affiche"],
  "Rien ne fait avancer tour : il vaut 0 pour toujours, donc la condition reste vraie pour toujours. Une repetition s'arrete parce que quelque chose AVANCE."),
 ('Quelle touche arrete un programme qui s\'est mis a repeter sans fin ?',
  "Ctrl + C", ["Ctrl + S", "Entree", "Echap"],
  "Dans la zone du bas de Thonny, Ctrl + C est le bouton d'arret d'urgence. Ailleurs, oui, Ctrl + C sert a copier."),
])
