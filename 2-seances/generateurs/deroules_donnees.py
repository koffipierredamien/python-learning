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
{"num": 10, "dossier": "S10-la-boucle",
 "titre": "Le jeu tourne tout seul",
 "date": "samedi 14 novembre 2026",
 "objet":
 "Depuis cinq semaines, les élèves recopient à l'identique le bloc d'instructions correspondant au "
 "tour d'un joueur, autant de fois qu'il y a de tours à jouer. L'agacement est installé, et il a été "
 "entretenu volontairement. La séance introduit la répétition : une instruction qui demande à "
 "l'ordinateur de refaire un travail tant qu'une condition reste vraie. C'est la notion la plus "
 "rentable du parcours. En fin de séance, le jeu enchaîne ses neuf tours en alternant les deux "
 "joueurs, et le programme est plus court que celui de la semaine précédente.",
 "horaires": [("12 h - 12 h 15", "Prière et accueil", "15 min"),
              ("12 h 15 - 12 h 22", "Quiz de révision du travail de la semaine précédente", "7 min"),
              ("12 h 22 - 12 h 40", "Première séquence : la répétition, et la répétition sans fin", "18 min"),
              ("12 h 40 - 12 h 55", "Premier atelier : le compte à rebours", "15 min"),
              ("12 h 55 - 13 h 05", "Pause", "10 min"),
              ("13 h 05 - 13 h 20", "Deuxième séquence : l'alternance des deux joueurs", "15 min"),
              ("13 h 20 - 13 h 50", "Second atelier : le projet", "30 min"),
              ("13 h 50 - 14 h", "Clôture", "10 min")],
 "deroule": [
  ("12 h - 12 h 15   Prière et accueil", ACCUEIL),
  ("12 h 15 - 12 h 22   Quiz de révision",
   ("Six questions sur les opérateurs introduits la semaine précédente.",
    "L'enseignant réclame ensuite le chiffre noté à la fin de la séance 9 — le nombre de lignes que "
    "chacun recopie — et l'inscrit au tableau. La leçon du jour s'écrit dessous. L'argument en faveur "
    "de la notion vient ainsi des élèves eux-mêmes, et non de l'enseignant.")),
  ("12 h 22 - 12 h 40   Première séquence : la répétition, et la répétition sans fin",
   ("La notion est d'abord énoncée en français, puis mimée avec un objet que l'on fait tourner, avant "
    "d'être écrite. Une répétition comporte toujours trois éléments : un point de départ, une "
    "condition d'arrêt, et quelque chose qui progresse à chaque passage.",
    "Démonstration à l'écran, les élèves annonçant le nombre de passages avant exécution.",
    "L'enseignant supprime ensuite l'élément qui progresse, et le programme ne s'arrête plus. Il "
    "laisse défiler quelques secondes, puis montre comment interrompre un programme devenu "
    "incontrôlable. Cette manipulation est faite devant la classe à dessein : elle se produira chez "
    "plusieurs élèves dans l'heure qui suit, et il importe qu'ils sachent déjà quoi faire, et qu'ils "
    "sachent que cela n'a rien de grave.")),
  ("12 h 40 - 12 h 55   Premier atelier : le compte à rebours",
   ("Chaque élève écrit, dans un fichier distinct, un compte à rebours qui part d'un nombre et "
    "descend jusqu'à un. L'exercice est court et son résultat est immédiatement visible.",
    "L'enseignant circule et vérifie une seule chose auprès de chacun : la présence de l'élément qui "
    "progresse, et son décalage correct.")),
  ("12 h 55 - 13 h 05   Pause",
   ("Pause réelle. L'enseignant ouvre le fichier du projet sur chaque poste.",)),
  ("13 h 05 - 13 h 20   Deuxième séquence : l'alternance des deux joueurs",
   ("Le jeu ne doit pas seulement répéter le tour : il doit changer de joueur à chaque passage. Deux "
    "informations changent ensemble — le symbole déposé et le nom affiché — et elles sont traitées "
    "au même endroit.",
    "L'enseignant montre ce qui se produit lorsqu'on ne change que l'une des deux, puis corrige. "
    "C'est l'erreur la plus fréquente de l'atelier qui suit.")),
  ("13 h 20 - 13 h 50   Second atelier : le projet",
   ("Les blocs recopiés depuis cinq semaines sont supprimés et remplacés par une répétition unique.",
    "C'est la première fois du parcours que l'atelier consiste principalement à effacer. Le résultat "
    "est spectaculaire et doit être montré : le fichier est plus court que celui de la semaine "
    "précédente, et il joue neuf tours au lieu de deux.",
    "À la fin de l'atelier, le programme de référence est remis à tous, qu'ils aient terminé ou non.")),
  ("13 h 50 - 14 h   Clôture",
   ("Avancement du Mur de Mission.",
    "Une partie complète est jouée devant la classe, du premier au neuvième coup.",
    "Annonce de la séance 11 : le jeu dira qui a gagné.")),
 ],
 "travail":
 "Deux travaux équivalents, au choix selon l'équipement de la famille. Les élèves qui disposent d'un "
 "ordinateur écrivent « Le Distributeur de la récré », une machine qui propose ses produits tant que "
 "le client a de quoi payer ; comptez une heure. Les autres répondent à un questionnaire de quinze "
 "questions corrigé automatiquement, en vingt minutes. Les familles sont prévenues qu'un programme "
 "peut se mettre à défiler sans s'arrêter, que cela est normal à ce stade, et comment l'interrompre.",
 "acquis":
 "À l'issue de cette séance, chaque élève sait écrire une répétition comportant ses trois éléments, "
 "sait reconnaître et interrompre une répétition sans fin, et sait faire alterner deux joueurs. "
 "Le jeu enchaîne ses neuf tours sans intervention."},

# =====================================================================
{"num": 11, "dossier": "S11-le-gagnant",
 "titre": "Le jeu sait qui gagne",
 "date": "samedi 21 novembre 2026",
 "objet":
 "Le jeu joue ses neuf tours, mais il ne sait pas ce qu'il joue : il s'arrête quand le plateau est "
 "plein, sans jamais constater qu'un joueur a aligné trois symboles. La séance lui apprend à le "
 "voir. Les huit alignements possibles sont d'abord établis par la classe elle-même, puis vérifiés "
 "par le programme après chaque coup ; une information nouvelle, qui retient le nom du vainqueur, est "
 "introduite à cette occasion, ainsi qu'une seconde condition d'arrêt. En fin de séance, le jeu est "
 "une partie de morpion complète : il s'arrête dès qu'un joueur gagne, l'annonce, et reconnaît le "
 "match nul.",
 "horaires": [("12 h - 12 h 15", "Prière et accueil", "15 min"),
              ("12 h 15 - 12 h 22", "Quiz de révision du travail de la semaine précédente", "7 min"),
              ("12 h 22 - 12 h 35", "Première séquence : qu'est-ce que gagner ?", "13 min"),
              ("12 h 35 - 12 h 50", "Deuxième séquence : les huit alignements et le nom du vainqueur", "15 min"),
              ("12 h 50 - 13 h", "Troisième séquence : la seconde condition d'arrêt", "10 min"),
              ("13 h - 13 h 10", "Pause", "10 min"),
              ("13 h 10 - 13 h 45", "Atelier : le projet", "35 min"),
              ("13 h 45 - 14 h", "La première partie complète, et clôture", "15 min")],
 "deroule": [
  ("12 h - 12 h 15   Prière et accueil", ACCUEIL),
  ("12 h 15 - 12 h 22   Quiz de révision",
   ("Six questions sur la répétition introduite la semaine précédente, et sur la manière "
    "d'interrompre un programme qui ne s'arrête plus.",)),
  ("12 h 22 - 12 h 35   Première séquence : qu'est-ce que gagner ?",
   ("Séquence sans machine. Les élèves énumèrent eux-mêmes, sur une feuille blanche puis au tableau, "
    "toutes les façons de gagner au morpion. Ils en trouvent huit, et l'enseignant ne donne le "
    "chiffre qu'une fois la recherche terminée.",
    "La formulation exacte de la règle est ensuite discutée. Trois cases identiques ne suffisent "
    "pas : trois cases encore vides portent des numéros différents, mais trois cases contenant le "
    "même symbole constituent un alignement. Cette précision est le point difficile de la séance.")),
  ("12 h 35 - 12 h 50   Deuxième séquence : les huit alignements et le nom du vainqueur",
   ("Les huit vérifications sont écrites à l'écran. Elles sont répétitives et sans difficulté "
    "individuelle ; elles figurent en entier sur l'aide-mémoire distribué, et les élèves les "
    "recopient de là. Ce choix est assumé : le temps de la séance doit aller à la compréhension, "
    "non à la saisie.",
    "Une information nouvelle est créée avant la partie, vide, et destinée à recevoir le nom du "
    "vainqueur lorsqu'il y en aura un. Le fait qu'elle soit créée avant, et une seule fois, est la "
    "notion la plus abstraite de la séance ; elle est expliquée lentement et vérifiée par questions.")),
  ("12 h 50 - 13 h   Troisième séquence : la seconde condition d'arrêt",
   ("La partie s'arrêtait jusqu'ici pour une seule raison : le plateau plein. Elle doit désormais "
    "s'arrêter aussi dès qu'un vainqueur est désigné. Les deux raisons sont réunies au moyen de "
    "l'opérateur cumulatif appris à la séance 9.",
    "L'emplacement des huit vérifications est souligné : elles doivent être faites après chaque coup "
    "et à l'intérieur de la répétition. Placées ailleurs, elles produisent deux anomalies "
    "caractéristiques que l'enseignant montre volontairement.")),
  ("13 h - 13 h 10   Pause", ("Pause réelle.",)),
  ("13 h 10 - 13 h 45   Atelier : le projet",
   ("Atelier le plus long du parcours à ce jour. Chaque élève ajoute à son propre jeu les huit "
    "vérifications, l'information retenant le vainqueur, la seconde condition d'arrêt et l'annonce "
    "finale.",
    "Trois situations doivent être essayées par l'élève avant qu'il ne signale avoir terminé : une "
    "victoire en ligne, une victoire en diagonale, et une partie nulle.",
    "À la fin de l'atelier, le programme de référence est remis à tous, qu'ils aient terminé ou non.")),
  ("13 h 45 - 14 h   La première partie complète, et clôture",
   ("Une partie entière est jouée devant la classe sur le programme d'un élève, choisi parmi ceux "
    "qui parlent le moins souvent.",
    "C'est le terme de deux mois de travail : le programme écrit par des enfants de neuf à dix-huit "
    "ans est devenu un jeu complet, avec ses règles, son vainqueur et son match nul. Le moment est "
    "nommé comme tel devant le groupe.",
    "Annonce de la séance 12 : travaux pratiques, finitions, et tournoi de classe.")),
 ],
 "travail":
 "Un questionnaire unique de quinze questions, corrigé automatiquement, est adressé à toutes les "
 "familles ; il demande vingt minutes depuis un téléphone. Aucun exercice de programmation n'est "
 "donné : le travail réel de la semaine est que chaque élève se présente le samedi suivant avec un "
 "jeu qui fonctionne, le tournoi se jouant sur leurs propres programmes.",
 "acquis":
 "À l'issue de cette séance, chaque élève sait énumérer les huit alignements gagnants, sait conserver "
 "une information d'une étape à l'autre d'une répétition, et sait arrêter une répétition pour deux "
 "raisons distinctes. Le jeu est une partie de morpion complète et jouable."},

# =====================================================================
{"num": 12, "dossier": "S12-tp-le-tournoi",
 "titre": "Travaux pratiques n°3 — tests, finitions et tournoi",
 "date": "samedi 28 novembre 2026",
 "objet":
 "Dernière séance des deux mois. Elle comporte trois temps : les élèves éprouvent leur propre "
 "programme au moyen d'une liste de huit situations à essayer, réparent ce qui doit l'être, puis "
 "jouent les uns contre les autres sur les jeux qu'ils ont écrits. La séance introduit, sans en "
 "faire une leçon, une idée professionnelle : un programme que l'on n'a pas éprouvé ne fonctionne "
 "pas, il n'a simplement pas encore échoué. Elle se termine par un bilan écrit rempli par chaque "
 "élève, dont les réponses détermineront le programme de décembre.",
 "horaires": [("12 h - 12 h 15", "Prière, accueil et annonce du tournoi", "15 min"),
              ("12 h 15 - 12 h 45", "Partie 1 : le contrôle technique, huit situations", "30 min"),
              ("12 h 45 - 13 h 10", "Partie 2 : les réparations", "25 min"),
              ("13 h 10 - 13 h 20", "Pause et tirage au sort des rencontres", "10 min"),
              ("13 h 20 - 13 h 25", "Partie 3 : une finition au choix", "5 min"),
              ("13 h 25 - 13 h 55", "Partie 4 : le tournoi de classe", "30 min"),
              ("13 h 55 - 14 h", "Bilan écrit, photographie et clôture", "5 min")],
 "deroule": [
  ("12 h - 12 h 15   Prière, accueil et annonce du tournoi",
   ACCUEIL + (
   "Le tableau du tournoi est affiché vide dès l'ouverture. Il est annoncé que tout le monde y "
   "participera, y compris les élèves dont le programme ne fonctionne pas : ceux-là joueront sur le "
   "programme de leur adversaire. Aucun enfant ne repart sans avoir joué.",)),
  ("12 h 15 - 12 h 45   Partie 1 : le contrôle technique",
   ("Chaque élève essaie sur son propre jeu huit situations précisées sur le document remis, et "
    "coche uniquement celles dont le résultat est exactement celui annoncé. Les situations qui "
    "échouent sont notées et seront traitées dans le temps suivant.",
    "Les élèves se prêtent les postes deux par deux : éprouver le programme d'un camarade est plus "
    "efficace, et moins douloureux, qu'éprouver le sien.")),
  ("12 h 45 - 13 h 10   Partie 2 : les réparations",
   ("Les situations ayant échoué sont reprises dans l'ordre. Le document remis associe à chaque "
    "symptôme l'endroit du programme où se trouve presque toujours la cause.",
    "L'enseignant ne corrige pas à la place de l'élève. Lorsque les huit situations passent, l'élève "
    "lève la main : c'est la validation des travaux pratiques, et la qualification pour le tournoi.",
    "Les élèves dont le programme ne peut être réparé dans le temps imparti reçoivent le programme "
    "de référence, sans commentaire et sans que cela soit présenté comme un échec.")),
  ("13 h 10 - 13 h 20   Pause et tirage au sort",
   ("Pause réelle. Le tirage au sort des rencontres est effectué pendant la pause et les noms sont "
    "inscrits au tableau du tournoi.",)),
  ("13 h 20 - 13 h 25   Partie 3 : une finition au choix",
   ("Chaque élève ajoute à son jeu une amélioration de son choix parmi celles proposées. Elles ne "
    "changent pas les règles du jeu : elles le rendent agréable, et elles sont le seul espace de la "
    "séance où l'élève décide seul de ce qu'il fait.",)),
  ("13 h 25 - 13 h 55   Partie 4 : le tournoi de classe",
   ("Rencontres à élimination directe. Chaque match se joue sur le programme de l'un des deux "
    "joueurs, désigné par tirage au sort.",
    "Si un programme s'interrompt ou annonce un résultat faux pendant un match, la rencontre est "
    "rejouée sur l'autre programme : la solidité d'un programme compte, et les élèves le constatent "
    "d'eux-mêmes.",
    "Le perdant de chaque rencontre devient arbitre de la suivante. Tout le monde a donc une fonction "
    "jusqu'à la fin.")),
  ("13 h 55 - 14 h   Bilan écrit, photographie et clôture",
   ("Chaque élève remplit la dernière page de son document : sept compétences à cocher, et deux "
    "questions ouvertes. La seconde — ce qu'il aimerait que son jeu sache faire et qu'il ne sait pas "
    "encore — sert à établir le programme de décembre.",
    "Photographie du groupe devant le tableau du tournoi rempli. Elle servira longtemps.",
    "Les documents sont ramassés. Ils constituent le bilan des deux mois.")),
 ],
 "travail":
 "Un questionnaire-bilan de quinze questions, corrigé automatiquement, reprend l'ensemble des sept "
 "séances d'octobre et novembre. Il est adressé à toutes les familles et demande vingt minutes. "
 "Il n'est pas une évaluation : lu partie par partie plutôt qu'élève par élève, il indique à "
 "l'équipe enseignante ce qui devra être repris à la reprise.",
 "acquis":
 "À l'issue de ces deux mois, chaque élève dispose d'un jeu de morpion complet, qu'il a écrit "
 "lui-même, auquel il a fait jouer ses camarades, et qu'il sait éprouver. Il sait employer une "
 "liste, le rang d'un élément, une décision, des conditions combinées et une répétition — c'est-à-dire "
 "l'essentiel de ce dont il aura besoin pour la suite du parcours."},
]
