# -*- coding: utf-8 -*-
"""Le formulaire de revision a la maison, bati sur le diaporama du 14 novembre.
   Vingt questions : les huit cartes du diaporama, et les cinq ateliers au clavier
   transformes en questions a choix multiples (Apps Script ne sait pas corriger
   une reponse libre)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quiz_hebdo import ecrire

ecrire(11, "S10-la-boucle",
 titre="Revision generale — a refaire a la maison",
 sujet="tout ce qu'on sait depuis septembre, et la boucle pour finir",
 intro="Ce sont les questions de la revision de samedi, plus celles des ateliers qu'on a faits au clavier. Si tu as suivi samedi, tu les connais deja : c'est fait pour.",
 rappels=["input rend TOUJOURS du texte",
          "indice = numero - 1",
          "le decalage dit QUI DEPEND DE QUI",
          "and : il faut TOUT   ·   or : il suffit d'UN",
          "une boucle s'arrete parce que quelque chose AVANCE"],
 fichier="quiz-revision-generale.gs",
 remplacements=[
   (" *  AcProKids Coding Camp — Quiz de la semaine n°11",
    " *  AcProKids Coding Camp — REVISION GENERALE, a refaire a la maison"),
   (""" *  POUR LES ENFANTS QUI N'ONT PAS D'ORDINATEUR : ils le font A LA PLACE
 *  de l'exercice de maison. Un telephone suffit.""",
    """ *  POUR TOUT LE MONDE, cette fois : c'est la revision du samedi
 *  14 novembre, refaite a la maison. Un telephone suffit.
 *  Les cinq ateliers qu'on a tapes au clavier y sont devenus des
 *  questions : on ne demande plus d'ecrire le code, on demande
 *  de dire ce qu'il fait."""),
 ],
 sections={0:  ("PARTIE A — Texte ou nombre",
                "La question qui provoque la moitie des ecrans rouges depuis septembre."),
           4:  ("PARTIE B — La liste et l'indice",
                "Le numero du sac est celui de l'humain. L'indice est celui de la machine."),
           8:  ("PARTIE C — Le decalage decide de tout",
                "Quatre espaces, et le programme ne fait plus la meme chose."),
           12: ("PARTIE D — and, or, et le piege",
                "Celle-la, c'est ton propre jeu qui est en cause."),
           16: ("PARTIE E — Le defi, et la boucle",
                "Pourquoi on avait besoin d'un outil de plus.")},
 qs=[
 # ---------------------------------------------------------- A
 ('print("7" + "7")\n\nQu\'est-ce qui s\'affiche ?',
  "77", ["14", "7 7", "une erreur rouge"],
  "Des guillemets autour : c'est du TEXTE. Le + colle, il n'additionne pas."),
 ('age = input("Ton age ? ")\nprint(age * 2)\n\nLe joueur tape 12. Qu\'est-ce qui s\'affiche ?',
  "1212", ["24", "12", "une erreur rouge"],
  "input rend TOUJOURS du texte. Et texte x 2, c'est le texte ecrit deux fois de suite, exactement comme \"=\" * 33 qui dessine nos cadres."),
 ('print(int("7") + int("7"))\n\nEt maintenant ?',
  "14", ["77", "7 7", "une erreur rouge"],
  "int() transforme le dessin du chiffre en vrai nombre. Et deux nombres, le + les additionne."),
 ('a = input("Un nombre : ")\nb = input("Un autre : ")\n\nQue faut-il ecrire pour afficher leur SOMME ?',
  "print(int(a) + int(b))", ["print(a + b)", "print(str(a) + str(b))", "print(a) + print(b)"],
  "Tant qu'on ne les a pas convertis, a et b sont deux dessins de chiffres, que le + met bout a bout. C'etait l'atelier n°1 de samedi."),

 # ---------------------------------------------------------- B
 ('equipe = ["A", "B", "C", "D"]\nprint(equipe[3])',
  "D", ["C", "A", "une erreur rouge"],
  "Les rangs partent de zero : A est au rang 0, donc D est au rang 3. Le dernier rang, c'est toujours un de moins que le nombre d'elements."),
 ('equipe[1] = equipe[2]\nprint(equipe)\n\nQu\'est-ce qui s\'affiche ?',
  "['A', 'C', 'C', 'D']", ["['A', 'B', 'C', 'D']", "['A', 'B', 'B', 'D']", "une erreur rouge"],
  "On LIT equipe[2], qui vaut C, et on le RANGE dans equipe[1]. Le B est ecrase, le C reste a sa place : la fleche va de droite a gauche."),
 ('sacs = ["riz", "sucre", "sel", "farine", "huile"]\n\nQuel est l\'indice du sac numero 5 ?',
  "4", ["5", "3", "Il n'y en a pas"],
  "indice = numero - 1. Cinq sacs, ce sont les rangs 0, 1, 2, 3 et 4."),
 ('print(sacs[5])\n\nQue se passe-t-il ?',
  "Une erreur rouge : IndexError", ["Ca affiche huile", "Ca n'affiche rien", "Ca affiche 5"],
  "Le rang 5 n'existe pas : la liste s'arrete au rang 4. C'est le message rouge qu'on a fait apparaitre expres samedi."),

 # ---------------------------------------------------------- C
 ('x = 10\nif x > 5:\n    print("A")\nprint("B")\n\nQu\'est-ce qui s\'affiche ?',
  "A puis B", ["A seulement", "B seulement", "rien du tout"],
  "print(\"B\") est colle a gauche : il est DEHORS du if. Il s'affiche quoi qu'il arrive."),
 ('points = 50\nif points > 50:\n    points = points + 10\nprint(points)',
  "50", ["60", "0", "une erreur rouge"],
  "50 n'est pas PLUS GRAND que 50. La condition est fausse, la ligne decalee est sautee, et points n'a pas bouge."),
 ('if reponse == 56:\n    print("Juste !")\nelse:\n    points = points - 40\n    print("Il te reste " + str(points))\n\nPourquoi le score ne s\'affiche-t-il QUE quand on se trompe ?',
  "Parce que la ligne du score est DANS le else",
  ["Parce que str() ne marche pas dans un if", "Parce qu'il manque un deuxieme else", "C'est un bug de Python"],
  "Decalee sous le else, la ligne appartient au else : elle ne s'execute que si la condition est fausse."),
 ('Toujours le meme programme.\n\nSANS AJOUTER AUCUNE LIGNE, comment faire pour que le score s\'affiche dans les DEUX cas ?',
  "On recule la ligne de 4 espaces, pour la coller a gauche",
  ["On l'ecrit une deuxieme fois dans le if", "On enleve le else", "On met le if et le else a la meme hauteur"],
  "Collee a gauche, la ligne n'appartient plus au else : elle appartient au programme, et s'affiche dans tous les cas. C'etait l'atelier n°3."),

 # ---------------------------------------------------------- D
 ('age = 11\nprint(age >= 12 and age <= 18)',
  "False", ["True", "11", "une erreur rouge"],
  "La premiere question est fausse : 11 n'est pas plus grand ou egal a 12. Avec and, une seule fausse suffit pour que tout soit faux."),
 ('Pour REFUSER une case qui n\'existe pas, j\'ecris :',
  "case < 1 or case > 9", ["case < 1 and case > 9", "case >= 1 or case <= 9", "case > 1 or case < 9"],
  "Une seule des deux raisons suffit pour refuser : c'est or. Avec and, il faudrait un nombre a la fois plus petit que 1 ET plus grand que 9. Ca n'existe pas."),
 ('La case 3 contient deja un X.\n\nif case >= 1 or case <= 9 and plateau[case - 1] == str(case):\n\nAvec case = 3, que fait le programme ?',
  "Il pose quand meme, par-dessus le X", ["Il refuse, c'est correct", "Il plante", "Il ne fait rien du tout"],
  "case >= 1 est vrai. Avec or, il suffit d'une reponse vraie : le reste de la ligne n'est meme plus regarde. C'est le programme qui mentait, samedi."),
 ('Quel mot faut-il changer pour reparer cette ligne ?',
  "le or, qu'il faut remplacer par and",
  ["le str(), qu'il faut enlever", "le - 1, qu'il faut enlever", "le >= qu'il faut mettre en >"],
  "Avec and, les TROIS questions comptent : la case existe par en bas, par en haut, et elle est libre."),

 # ---------------------------------------------------------- E
 ('Afficher le plateau une fois coute 5 lignes de print.\n\nPour l\'afficher TROIS fois en recopiant, combien de lignes d\'affichage faut-il ecrire ?',
  "15", ["5", "8", "3"],
  "Cinq lignes, trois fois : quinze. Plus les lignes qui posent les symboles : c'est le chiffre qu'on a compte au tableau samedi."),
 ('tour = 0\nwhile tour < 3:\n    print("A")\n    tour = tour + 1\n\nCombien de A s\'affichent ?',
  "3", ["2", "4", "sans fin"],
  "tour vaut 0, puis 1, puis 2 : trois passages. A 3, la condition devient fausse et la boucle s'arrete."),
 ('On oublie la ligne  tour = tour + 1.\n\nQue se passe-t-il ?',
  "Ca affiche A sans fin", ["Ca affiche A une seule fois", "Une erreur rouge", "Rien ne s'affiche"],
  "Rien ne fait avancer tour : la condition reste vraie pour toujours. Une boucle s'arrete parce que quelque chose AVANCE."),
 ('Quelle touche arrete un programme parti en boucle sans fin ?',
  "Ctrl + C", ["Ctrl + S", "Entree", "Echap"],
  "Dans la zone du bas de Thonny, Ctrl + C est le bouton d'arret d'urgence. Ailleurs, oui, Ctrl + C copie."),
])
