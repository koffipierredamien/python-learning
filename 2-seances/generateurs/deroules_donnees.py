# -*- coding: utf-8 -*-
"""Contenu des deroules destines au responsable, seances 6 a 12."""
import os
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ACCUEIL = ("Temps de prière conduit par l'enseignant, comme à l'ouverture de chaque séance.",
           "Appel et feuille de présence.",
           "Annonce de l'objectif de la séance en deux phrases.")

SEANCES = [

# =====================================================================
{"num": 6, "dossier": "S06-le-plateau-se-souvient",
 "titre": "Le plateau se souvient",
 "date": "samedi 17 octobre 2026",
 "objet":
 "Les apprenants disposent d'un programme qui dialogue avec deux joueurs, affiche un plateau "
 "numéroté et refuse une case qui n'existe pas. Il lui manque l'essentiel : la mémoire. Lorsqu'un "
 "joueur annonce la case qu'il veut jouer, le programme en prend acte, mais n'en garde aucune trace. "
 "La séance introduit la notion de liste — une seule variable capable de contenir plusieurs valeurs, "
 "ici les neuf cases du plateau — et celle de rang, qui permet d'en désigner une en particulier. "
 "C'est la notion la plus abstraite du parcours et celle dont tout le reste dépend : sans elle, "
 "aucune partie n'est possible. En fin de séance, le symbole déposé par un joueur demeure affiché "
 "sur le plateau.",
 "horaires": [("12 h - 12 h 15", "Prière et accueil", "15 min"),
              ("12 h 15 - 12 h 22", "Quiz de révision du travail de la semaine précédente", "7 min"),
              ("12 h 22 - 12 h 40", "Première séquence : la liste et le rang", "18 min"),
              ("12 h 40 - 13 h", "Premier atelier : la liste de la classe", "20 min"),
              ("13 h - 13 h 10", "Pause", "10 min"),
              ("13 h 10 - 13 h 20", "Deuxième séquence : désigner la case jouée", "10 min"),
              ("13 h 20 - 13 h 50", "Second atelier : le projet", "30 min"),
              ("13 h 50 - 14 h", "Clôture", "10 min")],
 "deroule": [
  ("12 h - 12 h 15   Prière et accueil", ACCUEIL),
  ("12 h 15 - 12 h 22   Quiz de révision",
   ("Six questions projetées, auxquelles les élèves répondent simultanément au moyen de cartes de "
    "couleur. Aucun appareil n'est nécessaire.",
    "Les questions reprennent les notions des séances précédentes que le travail de la semaine a "
    "montrées fragiles. Les résultats individuels ne sont jamais commentés devant le groupe.")),
  ("12 h 22 - 12 h 40   Première séquence : la liste et le rang",
   ("La notion est d'abord présentée sans machine. Neuf cartons numérotés sont alignés devant la "
    "classe, puis une seconde étiquette est collée sous chacun : son rang. Les élèves constatent que "
    "les deux numérotations ne coïncident pas, la seconde commençant à zéro.",
    "Démonstration ensuite commentée au vidéoprojecteur. L'enseignant écrit le programme devant la "
    "classe et demande systématiquement aux élèves de prédire le résultat avant de l'exécuter.",
    "Une erreur est provoquée volontairement : demander à l'ordinateur un rang qui n'existe pas. "
    "Le message correspondant est lu avec la classe et ajouté au dictionnaire des erreurs tenu par "
    "les élèves. Cette erreur est la plus fréquente de toute la phase qui s'ouvre ; il est préférable "
    "qu'elle soit rencontrée en démonstration avant de l'être en atelier.")),
  ("12 h 40 - 13 h   Premier atelier : la liste de la classe",
   ("Chaque élève crée une liste contenant les prénoms de trois camarades, en affiche un, puis en "
    "remplace un autre. L'exercice est volontairement court et sans rapport avec le jeu : il s'agit "
    "que chacun ait manipulé la notion de ses mains avant de l'appliquer au projet.",
    "Un prolongement est prévu pour les élèves les plus rapides. Conformément au principe retenu "
    "pour l'ensemble du parcours, il n'existe qu'un seul exercice pour toute la classe : ceux qui "
    "avancent vite reçoivent un défi supplémentaire, ceux qui butent reçoivent de l'aide, et non un "
    "exercice allégé.",
    "L'enseignant circule et n'intervient jamais sur le clavier de l'élève : il lui fait lire le "
    "message d'erreur et le laisse corriger.")),
  ("13 h - 13 h 10   Pause",
   ("Pause réelle. L'enseignant ouvre le fichier du projet sur chaque poste.",)),
  ("13 h 10 - 13 h 20   Deuxième séquence : désigner la case jouée",
   ("Séquence principale de la séance, et la plus courte. Elle établit le lien entre le numéro de "
    "case annoncé par le joueur et le rang que l'ordinateur attend, lequel vaut toujours une unité "
    "de moins.",
    "Les deux rangées de chiffres sont écrites au tableau, l'une sous l'autre, et y demeurent "
    "jusqu'à la fin de la séance. Elles y resteront, sous une forme ou une autre, pendant les six "
    "semaines suivantes.")),
  ("13 h 20 - 13 h 50   Second atelier : le projet",
   ("Le plateau du jeu cesse d'être un dessin figé pour devenir une liste de neuf valeurs, que le "
    "programme affiche à partir de son contenu réel.",
    "Chaque élève fait en sorte que le symbole du premier joueur s'inscrive dans la case demandée, "
    "puis réaffiche le plateau pour vérifier que la marque est au bon endroit.",
    "À la fin de l'atelier, le programme de référence est remis à tous, qu'ils aient terminé ou non : "
    "aucun élève ne prend de retard sur le projet.")),
  ("13 h 50 - 14 h   Clôture",
   ("Avancement du Mur de Mission.",
    "Question posée à la classe sur ce qui a été compris et sur ce dont les élèves ne sont pas sûrs. "
    "Les réponses déterminent l'ouverture de la séance suivante.",
    "Annonce de la séance 7 : le jeu refusera de jouer deux fois au même endroit.")),
 ],
 "travail":
 "Deux travaux équivalents sont proposés, au choix selon l'équipement de la famille. Les élèves qui "
 "disposent d'un ordinateur écrivent un petit jeu complet, « Le Coffre-Fort », qui réemploie "
 "exactement les notions de la séance ; comptez une heure. Les autres répondent, depuis un téléphone, "
 "à un questionnaire de quinze questions corrigé automatiquement ; comptez vingt minutes. Les deux "
 "portent sur le même contenu, afin que la séance suivante puisse s'ouvrir pour tout le monde de la "
 "même manière. Aucun des deux n'entre dans une note.",
 "acquis":
 "À l'issue de cette séance, chaque élève sait ce qu'est une liste, sait que le rang d'un élément "
 "commence à zéro, et sait désigner une case du plateau à partir du numéro annoncé par le joueur. "
 "Le jeu conserve désormais la trace du coup joué et le réaffiche."},

# =====================================================================
{"num": 7, "dossier": "S07-la-case-occupee",
 "titre": "On ne joue pas deux fois au même endroit",
 "date": "samedi 24 octobre 2026",
 "objet":
 "Le plateau conserve maintenant les coups joués, mais le programme accepte encore qu'un joueur "
 "dépose son symbole sur une case déjà occupée, effaçant celui de son adversaire. La séance apprend "
 "au programme à vérifier l'état d'une case avant d'y écrire, et introduit pour cela une structure "
 "de décision placée à l'intérieur d'une autre : le programme pose une première question, et ne pose "
 "la seconde que si la réponse à la première l'y autorise. En fin de séance, un coup déposé sur une "
 "case occupée est refusé et le joueur perd son tour.",
 "horaires": [("12 h - 12 h 15", "Prière et accueil", "15 min"),
              ("12 h 15 - 12 h 22", "Quiz de révision du travail de la semaine précédente", "7 min"),
              ("12 h 22 - 12 h 45", "Première séquence : reconnaître une case libre, puis la décision imbriquée", "23 min"),
              ("12 h 45 - 13 h", "Premier atelier : le contrôle d'une case", "15 min"),
              ("13 h - 13 h 10", "Pause", "10 min"),
              ("13 h 10 - 13 h 20", "Deuxième séquence : l'erreur provoquée et l'anomalie annoncée", "10 min"),
              ("13 h 20 - 13 h 50", "Second atelier : le projet", "30 min"),
              ("13 h 50 - 14 h", "Clôture", "10 min")],
 "deroule": [
  ("12 h - 12 h 15   Prière et accueil", ACCUEIL),
  ("12 h 15 - 12 h 22   Quiz de révision",
   ("Six questions sur la notion de liste et de rang, introduite la semaine précédente. Les réponses "
    "sont données simultanément par cartes de couleur.",
    "Cette révision n'est pas facultative : la notion de rang conditionne la totalité de la séance "
    "du jour. Si la moitié de la classe hésite encore, l'enseignant y consacre cinq minutes "
    "supplémentaires avant de poursuivre, en retranchant ce temps au premier atelier.")),
  ("12 h 22 - 12 h 45   Première séquence : reconnaître une case libre, puis la décision imbriquée",
   ("Le programme ne voit pas le plateau : il ne peut donc pas constater qu'une case est occupée, il "
    "doit le déduire. La classe cherche d'abord elle-même à quoi se reconnaît une case libre, avant "
    "que la réponse ne soit écrite : une case libre contient encore son propre numéro.",
    "Introduction ensuite de la décision placée à l'intérieur d'une autre. La notion est présentée "
    "au tableau, en français et sans machine, avant d'être écrite à l'écran : le programme demande "
    "d'abord si la case existe, et seulement dans le cas où elle existe, si elle est libre.",
    "Le décalage des lignes, qui exprime cette imbrication, est nommé à voix haute pendant la frappe. "
    "Il constitue la difficulté réelle de la séance, bien davantage que la notion elle-même.")),
  ("12 h 45 - 13 h   Premier atelier : le contrôle d'une case",
   ("Dans un fichier distinct du projet, chaque élève écrit un programme court qui demande un numéro "
    "de case et répond par l'une des trois réponses possibles : la case n'existe pas, la case est "
    "libre, la case est déjà prise.",
    "Les trois réponses doivent être essayées par l'élève lui-même avant qu'il ne signale avoir "
    "terminé. Cette vérification systématique, demandée à chaque atelier du parcours, est la "
    "première forme de ce qu'on appellera plus tard le test.")),
  ("13 h - 13 h 10   Pause",
   ("Pause réelle. L'enseignant ouvre le fichier du projet sur chaque poste.",)),
  ("13 h 10 - 13 h 20   Deuxième séquence : l'erreur provoquée et l'anomalie annoncée",
   ("L'enseignant supprime volontairement le décalage d'une ligne devant la classe, lit le message "
    "obtenu avec les élèves, puis le rétablit. C'est l'erreur qu'ils rencontreront le plus pendant "
    "l'atelier qui suit.",
    "Il saisit ensuite une valeur que le programme ne prévoit pas — le chiffre zéro — et montre que "
    "le symbole se dépose alors à l'autre extrémité du plateau. L'anomalie n'est pas corrigée "
    "aujourd'hui : sa correction suppose une notion qui sera abordée deux semaines plus tard. Elle "
    "est nommée, notée par les élèves, et datée.",
    "Cet engagement est tenu à la séance 9. Une anomalie que l'on nomme et que l'on date cesse "
    "d'être un échec et devient une étape du travail : c'est l'une des idées que la formation "
    "cherche à transmettre.")),
  ("13 h 20 - 13 h 50   Second atelier : le projet",
   ("Le contrôle écrit pendant le premier atelier est reporté dans le jeu, pour le premier joueur "
    "puis pour le second.",
    "Le bloc correspondant doit être recopié une seconde fois, à l'identique, pour le joueur adverse. "
    "Cette répétition est délibérée : elle prépare la séance 10, où une seule instruction remplacera "
    "l'ensemble de ces recopies.",
    "À la fin de l'atelier, le programme de référence est remis à tous, qu'ils aient terminé ou non.")),
  ("13 h 50 - 14 h   Clôture",
   ("Avancement du Mur de Mission.",
    "Question posée à la classe sur ce qui a été compris et sur ce dont les élèves ne sont pas sûrs.",
    "Annonce de la séance 8 : deux heures de travaux pratiques, en autonomie.")),
 ],
 "travail":
 "Cette semaine, un questionnaire unique de quinze questions, corrigé automatiquement, est adressé à "
 "toutes les familles ; il se fait depuis un téléphone et demande vingt minutes. Aucun exercice de "
 "programmation n'est donné : la séance suivante est une séance de travaux pratiques de deux heures, "
 "et il est préférable que les élèves s'y présentent disponibles.",
 "acquis":
 "À l'issue de cette séance, chaque élève sait reconnaître une case occupée, sait écrire une décision "
 "à l'intérieur d'une autre et sait lire le message d'erreur que produit un décalage incorrect. "
 "Le jeu refuse un coup déjà joué, et une anomalie connue reste ouverte, inscrite au programme de la "
 "séance 9."},

# =====================================================================
{"num": 8, "dossier": "S08-tp-le-plateau",
 "titre": "Travaux pratiques n°2 — le plateau vivant",
 "date": "samedi 31 octobre 2026",
 "objet":
 "Deuxième séance de travaux pratiques du parcours. Elle ne comporte aucune notion nouvelle. Les "
 "élèves travaillent seuls, sur un document écrit qui leur est remis, pendant que l'enseignant "
 "circule, débloque et valide. L'objectif est de consolider la notion de liste et celle de rang, "
 "introduites les deux samedis précédents et de loin les plus difficiles de ces deux mois : un élève "
 "qui ne les possède pas ne pourra suivre aucune des séances suivantes. Le travail est organisé en "
 "quatre parties de difficulté croissante, et se termine par un programme qui enchaîne quatre coups "
 "sans anomalie.",
 "horaires": [("12 h - 12 h 15", "Prière et accueil", "15 min"),
              ("12 h 15 - 12 h 40", "Partie 1 : lire et modifier une liste", "25 min"),
              ("12 h 40 - 13 h", "Partie 2 : le rang d'une case", "20 min"),
              ("13 h - 13 h 10", "Pause", "10 min"),
              ("13 h 10 - 13 h 15", "Reprise et consignes de la seconde moitié", "5 min"),
              ("13 h 15 - 13 h 50", "Parties 3 et 4 : le plateau qui vit, puis quatre coups", "35 min"),
              ("13 h 50 - 14 h", "Bilan écrit et clôture", "10 min")],
 "deroule": [
  ("12 h - 12 h 15   Prière et accueil", ACCUEIL + (
   "Remise du document de travaux pratiques, quatre pages, un exemplaire par élève. Les consignes "
   "y figurent en entier : l'enseignant ne fait pas cours.",)),
  ("12 h 15 - 12 h 40   Partie 1 : lire et modifier une liste",
   ("Exercices courts, à difficulté croissante, portant sur la lecture d'un élément dans une liste "
    "et sur son remplacement.",
    "L'enseignant circule en permanence. Il ne touche aucun clavier : il fait lire le message "
    "d'erreur à l'élève et lui demande ce que le message lui dit.")),
  ("12 h 40 - 13 h   Partie 2 : le rang d'une case",
   ("Partie décisive de la séance, et la seule qui ne puisse en aucun cas être abrégée.",
    "Un contrôle individuel de dix secondes est effectué auprès de chaque élève : l'enseignant "
    "désigne une case au hasard sur le plateau dessiné au tableau et demande son rang. En cas "
    "d'hésitation, l'élève écrit les deux rangées de chiffres sur son cahier, l'une sous l'autre, "
    "et reprend. Deux minutes suffisent, et elles décident de la suite du parcours pour cet élève.")),
  ("13 h - 13 h 10   Pause",
   ("Pause réelle.",)),
  ("13 h 10 - 13 h 15   Reprise",
   ("Si trois élèves ou plus butent sur la même difficulté, une reprise collective de trois minutes "
    "est faite au tableau, pour tout le monde. Au-delà, on repart au travail : la séance n'est pas "
    "un cours.",)),
  ("13 h 15 - 13 h 50   Parties 3 et 4 : le plateau qui vit, puis quatre coups",
   ("Les élèves construisent un programme qui affiche le plateau à partir du contenu réel de la "
    "liste, puis qui enchaîne quatre coups successifs en refusant les cases déjà prises.",
    "Des prolongements signalés comme tels sont prévus pour ceux qui terminent avant l'heure. Aucun "
    "ne va au-delà de ce qui a été enseigné.",
    "À 13 h 50, tout le monde s'arrête, terminé ou non, et le programme de référence est distribué "
    "à l'ensemble de la classe.")),
  ("13 h 50 - 14 h   Bilan écrit et clôture",
   ("La dernière page du document comporte un bilan que chaque élève remplit lui-même, et dont la "
    "rubrique la plus utile est celle intitulée « ce que je n'ai pas bien compris ».",
    "Les documents sont ramassés, ou photographiés. Ils constituent, avec le journal de l'enseignant, "
    "la principale source d'information pour la préparation de la séance 9.",
    "Avancement du Mur de Mission et annonce de la séance suivante.")),
 ],
 "travail":
 "Aucun travail n'est donné cette semaine : la séance de travaux pratiques constitue le travail de "
 "la semaine. Les élèves qui n'ont pas terminé peuvent poursuivre chez eux s'ils disposent d'un "
 "ordinateur, sans obligation et sans conséquence sur la suite, le programme de référence leur ayant "
 "été remis.",
 "acquis":
 "À l'issue de cette séance, l'enseignant sait, élève par élève, lesquels possèdent la notion de rang "
 "et lesquels doivent être soutenus. Les élèves disposent d'un programme qui enchaîne quatre coups "
 "sans anomalie, et d'un document écrit qui garde la trace de ce qu'ils ont su faire seuls."},

# =====================================================================
{"num": 9, "dossier": "S09-et-ou",
 "titre": "Une seule question au lieu de trois",
 "date": "samedi 7 novembre 2026",
 "objet":
 "La séance n'ajoute rien au jeu : elle en retranche. Le contrôle écrit à la séance 7 fonctionne, "
 "mais il est long et difficile à relire, et il laisse subsister l'anomalie annoncée ce jour-là. "
 "La séance introduit les deux opérateurs qui permettent de réunir plusieurs questions en une seule — "
 "l'un exige que toutes les conditions soient remplies, l'autre se contente d'une seule — puis les "
 "emploie pour réécrire ce contrôle en une ligne unique. L'anomalie du chiffre zéro est corrigée à "
 "cette occasion, comme annoncé aux élèves quinze jours plus tôt. Cette simplification n'est pas une "
 "élégance : la séance suivante serait illisible sans elle.",
 "horaires": [("12 h - 12 h 15", "Prière et accueil", "15 min"),
              ("12 h 15 - 12 h 22", "Quiz de révision et retour sur les travaux pratiques", "7 min"),
              ("12 h 22 - 12 h 40", "Première séquence : les deux opérateurs logiques", "18 min"),
              ("12 h 40 - 12 h 55", "Premier atelier : le contrôle d'entrée", "15 min"),
              ("12 h 55 - 13 h 05", "Pause", "10 min"),
              ("13 h 05 - 13 h 20", "Deuxième séquence : la réécriture, et la correction annoncée", "15 min"),
              ("13 h 20 - 13 h 50", "Second atelier : le projet", "30 min"),
              ("13 h 50 - 14 h", "Clôture", "10 min")],
 "deroule": [
  ("12 h - 12 h 15   Prière et accueil", ACCUEIL),
  ("12 h 15 - 12 h 22   Quiz de révision et retour sur les travaux pratiques",
   ("Six questions projetées, portant sur la notion de rang et sur ce que les travaux pratiques ont "
    "montré de plus fragile.",
    "L'enseignant a relu, la veille, les bilans écrits remplis par les élèves à la fin de la séance "
    "8. Si moins de la moitié de la classe possède la notion de rang, la séance s'ouvre par cinq "
    "minutes de reprise et le premier atelier est supprimé.")),
  ("12 h 22 - 12 h 40   Première séquence : les deux opérateurs logiques",
   ("Les apprenants connaissent depuis la séance 4 les opérateurs de comparaison, qui produisent une "
    "réponse vraie ou fausse. Ils découvrent ici les opérateurs qui combinent plusieurs de ces "
    "réponses entre elles.",
    "Les deux sont présentés par des exemples de la vie courante avant d'être écrits : l'un "
    "correspond à une exigence cumulative — il faut à la fois son cahier et son stylo — l'autre à une "
    "alternative — avoir terminé son exercice ou avoir aidé un camarade.",
    "Les quatre combinaisons possibles de chacun sont essayées à l'écran, les élèves annonçant le "
    "résultat avant l'exécution. Les deux règles, énoncées en une ligne chacune, sont écrites au "
    "tableau et y demeurent jusqu'à la fin de la séance.")),
  ("12 h 40 - 12 h 55   Premier atelier : le contrôle d'entrée",
   ("Dans un fichier distinct, chaque élève écrit un programme qui décide si une personne peut "
    "entrer dans un club, selon deux conditions cumulatives. Le sujet est choisi pour être parlant "
    "et sans rapport avec le jeu.",
    "Le prolongement prévu pour ceux qui avancent vite consiste à ajouter une troisième condition "
    "alternative. Il est repris et développé dans l'exercice donné pour la semaine.")),
  ("12 h 55 - 13 h 05   Pause",
   ("Pause réelle. L'enseignant ouvre le fichier du projet sur chaque poste.",)),
  ("13 h 05 - 13 h 20   Deuxième séquence : la réécriture, et la correction annoncée",
   ("Séquence principale de la séance. L'ancien contrôle est écrit sur la moitié gauche du tableau "
    "et le nouveau sur la moitié droite : sept lignes et deux niveaux de décalage deviennent quatre "
    "lignes et un seul niveau.",
    "Quatre cas sont essayés devant la classe, dans un ordre déterminé, le dernier étant le chiffre "
    "zéro. Le programme le refuse désormais, et pour la bonne raison. L'engagement pris à la séance "
    "7 est ainsi tenu devant les élèves, et il est utile de le souligner.",
    "La formule retenue pour conclure la séquence est reprise chaque fois que l'occasion se présente "
    "dans la suite du parcours : on vient d'écrire moins de lignes, et le programme fait davantage.")),
  ("13 h 20 - 13 h 50   Second atelier : le projet",
   ("Chaque élève remplace, dans son propre jeu, le contrôle de la séance 7 par la ligne unique, "
    "pour les deux joueurs.",
    "Il vérifie ensuite les quatre cas essayés en démonstration. Cette vérification est la condition "
    "pour que le travail soit considéré comme terminé.",
    "À la fin de l'atelier, le programme de référence est remis à tous, qu'ils aient terminé ou non.")),
  ("13 h 50 - 14 h   Clôture",
   ("Avancement du Mur de Mission.",
    "Il est demandé aux élèves de compter le nombre de lignes qu'ils ont supprimées, et de le noter. "
    "Le chiffre sera réclamé à l'ouverture de la séance suivante.",
    "Annonce de la séance 10 : le jeu jouera ses neuf tours sans qu'on ait à les écrire.")),
 ],
 "travail":
 "Deux travaux équivalents, au choix selon l'équipement de la famille. Les élèves qui disposent d'un "
 "ordinateur écrivent « La Soirée du Club Geek », prolongement direct de l'atelier de la séance, qui "
 "demande environ une heure. Les autres répondent à un questionnaire de quinze questions, corrigé "
 "automatiquement, depuis un téléphone, en vingt minutes. Aucun des deux n'entre dans une note.",
 "acquis":
 "À l'issue de cette séance, chaque élève sait énoncer avec ses propres mots la différence entre une "
 "exigence cumulative et une alternative, et sait réunir plusieurs conditions en une seule ligne. "
 "Le jeu rend la même décision qu'auparavant, en deux fois moins de lignes, et l'anomalie ouverte "
 "depuis la séance 7 est close."},

# =====================================================================
{"num": 10, "dossier": "S10-revision-generale",
 "titre": "Révision générale",
 "date": "samedi 14 novembre 2026",
 "objet":
 "Séance de consolidation, sans notion nouvelle. Après neuf séances, il devenait nécessaire de "
 "vérifier ce qui était réellement acquis, et non ce qui avait été enseigné. La séance a pris la "
 "forme d'un questionnaire projeté en cinq manches, chacune suivie d'un atelier où les apprenants "
 "éprouvent sur leur poste un programme qui ne fait pas ce qu'ils attendent. La séance n'a pas pu "
 "aller à son terme : les deux dernières manches n'ont pas été traitées, et la notion qui devait "
 "être introduite en fin de séance a été reportée.",
 "horaires": [("12 h - 12 h 15", "Prière et accueil", "15 min"),
              ("12 h 15 - 12 h 18", "Règle du jeu : la carte, puis le clavier", "3 min"),
              ("12 h 18 - 12 h 26", "Manche 1 : distinguer un texte d'un nombre", "8 min"),
              ("12 h 26 - 12 h 35", "Manche 2 : les listes et le rang", "9 min"),
              ("12 h 35 - 12 h 45", "Manche 3 : le décalage des lignes", "10 min"),
              ("12 h 45 - 13 h 56", "Manches 4 et 5 : non traitées, reportées", "—"),
              ("13 h 56 - 14 h", "Clôture", "4 min")],
 "deroule": [
  ("12 h - 12 h 15   Prière et accueil", ACCUEIL),
  ("12 h 15 - 12 h 18   La règle de la séance",
   ("Deux sortes de questions sont annoncées : celles auxquelles on répond en levant une carte de "
    "couleur, tout le monde en même temps, et celles où l'on tape soi-même le programme projeté.",
    "Une consigne est posée pour toute la séance : avant de lancer un programme, chacun annonce ce "
    "qu'il pense qu'il va faire. Cette prédiction est l'exercice ; celui qui lance sans prédire ne "
    "se trompe jamais devant lui-même, et n'apprend donc rien.")),
  ("12 h 18 - 12 h 45   Les trois premières manches",
   ("Chaque manche associe deux questions à la carte et un atelier sur machine. Les ateliers sont "
    "construits autour d'un programme qui échoue : les apprenants doivent trouver pourquoi, puis "
    "réparer.",
    "Les trois manches traitées ont porté sur la distinction entre un texte et un nombre, sur la "
    "manière de désigner un élément dans une liste, et sur le décalage des lignes, qui détermine "
    "quelles instructions dépendent d'une condition.",
    "Le temps consacré à chaque atelier a dépassé ce qui était prévu, les apprenants ayant cherché "
    "les causes par eux-mêmes plutôt que de recevoir la correction. Ce dépassement est considéré "
    "comme utile.")),
  ("12 h 45 - 14 h   Ce qui n'a pas pu être traité",
   ("Les deux dernières manches, ainsi que la notion de répétition qui devait être introduite en fin "
    "de séance, n'ont pas été abordées.",
    "Le programme des séances suivantes a été réorganisé en conséquence. La séance du 21 novembre "
    "reprend les points que la révision a montrés fragiles, et la répétition est reportée à une "
    "séance ultérieure, lorsque le besoin en sera clairement établi.")),
  ("13 h 56 - 14 h   Clôture",
   ("Avancement du Mur de Mission.",
    "Annonce de la séance suivante.")),
 ],
 "travail":
 "Un questionnaire de vingt questions, corrigé automatiquement, a été adressé à toutes les familles. "
 "Il reprend l'intégralité de la séance et se fait depuis un téléphone en une demi-heure. Il a été "
 "rédigé de manière à être compréhensible sans avoir assisté à la séance, afin que les apprenants "
 "absents puissent en bénéficier également. Il n'entre dans aucune note.",
 "acquis":
 "Cette séance n'a pas ajouté de compétence nouvelle. Elle a donné à l'équipe enseignante une "
 "photographie précise de ce qui est acquis et de ce qui ne l'est pas, laquelle a servi à "
 "réorganiser le programme des séances suivantes."},

# =====================================================================
{"num": 11, "dossier": "S11-les-trois-chemins",
 "titre": "Trois chemins au lieu de deux",
 "date": "samedi 21 novembre 2026",
 "objet":
 "Le programme des apprenants sait aujourd'hui refuser un coup illégal, mais il ne sait en donner "
 "qu'une seule explication, et elle est ambiguë : il annonce que la case n'existe pas ou qu'elle est "
 "déjà occupée, sans jamais dire laquelle des deux. La raison en est technique : une structure de "
 "décision ordinaire n'offre que deux issues, et il en faudrait trois. La séance introduit donc le "
 "moyen d'enchaîner plusieurs conditions, et surtout la règle qui le gouverne : l'ordinateur "
 "s'arrête à la première condition vraie et ne regarde pas les suivantes — d'où l'importance de "
 "l'ordre dans lequel on les écrit. La séance se tient entièrement au format questionnaire, et "
 "chaque notion est suivie d'un atelier sur machine.",
 "horaires": [("12 h - 12 h 15", "Prière et accueil", "15 min"),
              ("12 h 15 - 12 h 28", "Questionnaire de révision : sept questions", "13 min"),
              ("12 h 28 - 13 h 05", "Le cours : quatre séquences, trois ateliers sur machine", "37 min"),
              ("13 h 05 - 13 h 15", "Pause", "10 min"),
              ("13 h 15 - 13 h 40", "Exercice : le bulletin scolaire", "25 min"),
              ("13 h 40 - 13 h 50", "Exercice de prolongement, pour les plus rapides", "10 min"),
              ("13 h 50 - 14 h", "Clôture", "10 min")],
 "deroule": [
  ("12 h - 12 h 15   Prière et accueil", ACCUEIL),
  ("12 h 15 - 12 h 28   Questionnaire de révision",
   ("Sept questions projetées, auxquelles les apprenants répondent simultanément au moyen de cartes "
    "de couleur. Aucun appareil n'est nécessaire, et les résultats individuels ne sont jamais "
    "commentés devant le groupe.",
    "Les questions portent sur les points que la séance de révision du 14 novembre a montrés "
    "fragiles, en premier lieu le décalage des lignes.")),
  ("12 h 28 - 12 h 32   Première séquence : constater le défaut",
   ("L'enseignant exécute devant la classe le programme que les apprenants ont eux-mêmes écrit, et "
    "lui soumet deux coups illégaux de natures différentes. Le programme répond la même chose dans "
    "les deux cas.",
    "Ce constat précède la leçon : la notion du jour est introduite parce que les apprenants "
    "viennent de voir qu'elle leur manque, et non parce qu'elle figure au programme.")),
  ("12 h 32 - 12 h 44   Deuxième séquence : enchaîner les conditions",
   ("Présentation de la structure qui permet de poser une deuxième question seulement si la première "
    "a reçu une réponse négative, puis une troisième, et ainsi de suite.",
    "La règle qui la gouverne est écrite au tableau et y demeure toute la séance : l'ordinateur "
    "s'arrête à la première condition vraie et ne regarde pas les suivantes.",
    "Atelier sur machine. Un prolongement est prévu pour les apprenants les plus rapides ; il les "
    "conduit à découvrir d'eux-mêmes la nécessité d'un cas par défaut, qui sera la séquence "
    "suivante.")),
  ("12 h 44 - 12 h 59   Troisième séquence : l'ordre des conditions",
   ("Séquence principale de la séance. Une suite de conditions parfaitement exactes, mais écrite "
    "dans le mauvais ordre, produit un résultat faux pour tout le monde. La démonstration est faite "
    "avant toute explication.",
    "Atelier sur machine, le plus long de la séance. Il est soumis à une condition : "
    "**l'algorithme doit être rédigé sur le cahier, en français, avant toute saisie au clavier**, "
    "et l'enseignant le vérifie en circulant. Les apprenants n'ayant jamais travaillé cette "
    "démarche de manière formelle, elle fait ici l'objet d'une exigence explicite.")),
  ("12 h 59 - 13 h 05   Quatrième séquence : application au projet",
   ("La structure étudiée est reportée dans le jeu de chacun. Le programme énonce désormais trois "
    "réponses distinctes à un coup, là où il n'en donnait qu'une, ambiguë.",
    "À la fin de la séquence, le programme de référence est remis à tous, qu'ils aient terminé ou "
    "non : aucun apprenant ne prend de retard sur le projet commun.")),
  ("13 h 05 - 13 h 15   Pause",
   ("Pause réelle. L'enseignant prépare les postes pour l'exercice.",)),
  ("13 h 15 - 13 h 40   Exercice : le bulletin scolaire",
   ("Chaque apprenant écrit un programme qui demande le nom d'un élève et trois notes, calcule la "
    "moyenne et annonce la mention correspondante.",
    "Comme à la troisième séquence, l'algorithme est rédigé sur le cahier avant toute saisie.")),
  ("13 h 40 - 13 h 50   Exercice de prolongement",
   ("Destiné aux apprenants qui ont terminé avant les autres. Il s'agit d'une tarification par "
    "tranches d'âge, assortie d'une réduction un jour de la semaine.",
    "Deux difficultés y sont dissimulées volontairement, et ne sont pas signalées : un ordre de "
    "conditions qui paraît correct attribue le mauvais tarif aux personnes âgées, et l'absence "
    "d'une précaution conduit le programme à annoncer un prix négatif. L'enseignant se borne à "
    "demander quatre essais précis ; les apprenants trouvent eux-mêmes.",
    "Conformément au principe retenu pour l'ensemble du parcours, il n'existe qu'un seul exercice "
    "pour toute la classe : ceux qui avancent vite reçoivent un travail supplémentaire, et non un "
    "exercice allégé pour les autres.")),
  ("13 h 50 - 14 h   Clôture",
   ("Avancement du Mur de Mission.",
    "Question posée à la classe sur ce qui n'est pas sûr d'avoir été compris. Les réponses "
    "déterminent l'ouverture de la séance suivante.",
    "Annonce de la séance 12.")),
 ],
 "travail":
 "Deux travaux équivalents sont proposés, au choix selon l'équipement de la famille, et aucun "
 "n'entre dans une note. Les apprenants disposant d'un ordinateur reprennent chez eux l'exercice du "
 "bulletin et son prolongement ; les autres répondent, depuis un téléphone, au questionnaire de "
 "révision adressé la semaine précédente, qui reste accessible et peut être refait autant de fois "
 "que souhaité.",
 "acquis":
 "À l'issue de cette séance, chaque apprenant sait enchaîner plusieurs conditions, sait que "
 "l'ordinateur s'arrête à la première qui est vraie, et sait en déduire dans quel ordre les écrire. "
 "Il a en outre rédigé au moins un algorithme en français avant de programmer. Le jeu indique "
 "désormais au joueur la raison précise pour laquelle un coup est refusé."},
]
