/**
 * =====================================================================
 *  AcProKids Coding Camp — QUIZ DE RAPPEL
 *  texte et nombres, if / else, listes, and / or, et l'ordre des conditions
 *
 *  POUR TOUT LE MONDE. Un telephone suffit, et rien d'autre.
 *
 *  LE FORMULAIRE SE SUFFIT A LUI-MEME : aucune question ne renvoie a
 *  une seance, a un atelier ni a un projet. On peut donc le renvoyer
 *  tel quel plus tard, ou le donner a un enfant qui etait absent.
 *
 *  IL S'ARRETE A L'ORDRE DES CONDITIONS. La repetition (while) n'y
 *  figure pas : elle n'a pas encore ete vue en classe.
 *
 *  20 questions a choix multiples = 20 points.
 *  TOUT EST CORRIGE AUTOMATIQUEMENT : aucun corrige a coller a la main.
 * =====================================================================
 *
 *  MODE D'EMPLOI :
 *   1. script.google.com  →  Nouveau projet
 *   2. Effacez le code present, collez TOUT ce fichier
 *   3. Bouton ▶ Executer  →  autorisez a la premiere utilisation
 *   4. Le journal affiche le lien a envoyer
 *
 *  ⚠⚠ ETAPE 5, SANS LAQUELLE L'ELEVE NE VERRA AUCUNE CORRECTION :
 *     formulaire → ⚙ Parametres → Questionnaires :
 *        « Publier les notes »  →  IMMEDIATEMENT APRES CHAQUE ENVOI
 *        « Le participant peut voir » → cochez les TROIS cases
 *     Apps Script n'expose pas ces reglages : quatre clics, une fois.
 *
 *  RECETTE : repondez vous-meme. Le bouton « Afficher le score » doit
 *  apparaitre, avec la note et les corriges.
 * =====================================================================
 */

function creerLeQuiz() {

  var form = FormApp.create('Quiz de rappel — tout ce que tu sais deja');

  form.setDescription(
      'AcProKids Coding Camp — Jeremiah Geeks\n\n' +
      'Vingt questions pour faire le tour de tout ce que tu sais deja. Chacune se repond avec ce qui est ecrit dedans : tu n\'as besoin de rien d\'autre, ni d\'un cahier, ni d\'un ordinateur. Tu peux le refaire autant de fois que tu veux.\n\n' +
      'RAPPELS A GARDER SOUS LES YEUX :\n' +
      '    input rend TOUJOURS du texte\n    dans une liste, les numeros commencent a ZERO\n    le decalage dit QUI DEPEND DE QUI\n    and : il faut TOUT   ·   or : il suffit d\'UN\n    une cascade s\'arrete au PREMIER chemin qui passe\n\n' +
      '20 questions, 20 points. Tu as ta note et les explications a la fin. ' +
      'Se tromper n\'est pas grave : c\'est comme ca qu\'on apprend.');

  form.setIsQuiz(true);
  form.setShowLinkToRespondAgain(false);
  form.setConfirmationMessage(
      'C\'est envoye ! Clique sur « Afficher le score » pour voir ta note et les explications. ' +
      'Tu peux refaire ce quiz autant de fois que tu veux.');

  form.addTextItem().setTitle('Ton prenom et ton nom').setRequired(true);
  form.addMultipleChoiceItem()
      .setTitle('Ta classe')
      .setChoiceValues(['Jerusalem Geeks (9 – 12 ans)', 'Jeremiah Geeks (12 – 18 ans)'])
      .setRequired(true);

  var questions = [
    ['print("3" + "4")\n\nQu\'est-ce qui s\'affiche ?',
     ['34', '7', '3 + 4', 'une erreur rouge'], '34',
     'Entre guillemets, 3 et 4 sont du TEXTE. Le + ne les additionne pas : il les colle l\'un derriere l\'autre.'],

    ['age = input("Ton age ? ")\nprint(age + 1)\n\nL\'enfant tape 10. Qu\'est-ce qui s\'affiche ?',
     ['11', '101', 'une erreur rouge', '10'], 'une erreur rouge',
     'input rend TOUJOURS du texte. On ne peut pas ajouter 1 a du texte. Il fallait ecrire age = int(age) avant.'],

    ['points = 10\npoints = points + 5\npoints = points + 5\nprint(points)\n\nQu\'est-ce qui s\'affiche ?',
     ['10', '15', 'points + 5', '20'], '20',
     'A chaque ligne, on regarde ce qu\'il y a dans la boite et on y remet la nouvelle valeur : 10, puis 15, puis 20.'],

    ['points est un NOMBRE qui vaut 20.\n\nQuelle ligne affiche  Il te reste 20 points  sans erreur rouge ?',
     ['print("Il te reste " + points + " points")', 'print("Il te reste " + str(points) + " points")', 'print("Il te reste " + int(points) + " points")', 'print("Il te reste points points")'], 'print("Il te reste " + str(points) + " points")',
     'Pour coller un nombre a du texte, il faut d\'abord le transformer en texte : c\'est str().'],

    ['x = 2\n\nif x > 5:\n    print("A")\nprint("B")\n\nQu\'est-ce qui s\'affiche ?',
     ['B seulement', 'A puis B', 'A seulement', 'rien du tout'], 'B seulement',
     '2 n\'est pas plus grand que 5 : la ligne decalee est sautee. Mais print("B") est colle a gauche : il ne depend du if de personne, et s\'affiche toujours.'],

    ['points = 50\n\nif points > 50:\n    points = points + 10\nprint(points)\n\nQu\'est-ce qui s\'affiche ?',
     ['60', '0', 'une erreur rouge', '50'], '50',
     '50 n\'est pas PLUS GRAND que 50 : la condition est fausse. Pour l\'inclure, il fallait ecrire >= au lieu de >.'],

    ['Je veux verifier si la boite  note  contient le nombre 10.\n\nJ\'ecris :',
     ['if note = 10:', 'if note == 10:', 'if note := 10:', 'if note egal 10:'], 'if note == 10:',
     'Un seul = sert a RANGER quelque chose dans une boite. Pour COMPARER, il en faut deux : ==.'],

    ['reponse = "non"\n\nif reponse == "oui":\n    print("D\'accord")\nelse:\n    print("Tant pis")\n    print("On se revoit")\n\nQu\'est-ce qui s\'affiche ?',
     ['Tant pis seulement', 'D\'accord, puis On se revoit', 'Tant pis, puis On se revoit', 'une erreur rouge'], 'Tant pis, puis On se revoit',
     'Les DEUX lignes sont decalees sous le else : elles appartiennent toutes les deux au else, et partent ensemble.'],

    ['equipe = ["Ama", "Kofi", "Sara", "Yao"]\nprint(equipe[0])\n\nQu\'est-ce qui s\'affiche ?',
     ['Ama', 'Kofi', 'Yao', 'une erreur rouge'], 'Ama',
     'Dans une liste, les numeros commencent a ZERO. Le premier element porte le numero 0, pas 1.'],

    ['Les cases d\'un jeu portent les numeros 1 a 9, mais la liste qui les contient commence a zero.\n\nLe joueur annonce la case 7. Quel numero faut-il demander a la liste ?',
     ['7', '6', '8', '1'], '6',
     'Le numero de la liste vaut toujours une unite de moins que le numero annonce : c\'est le fameux  case - 1.'],

    ['plateau = ["1", "2", "X", "4", "5", "6", "7", "8", "9"]\nprint(plateau[9])\n\nQu\'est-ce qui s\'affiche ?',
     ['le chiffre 9', 'la lettre X', 'rien du tout', 'une erreur rouge : IndexError'], 'une erreur rouge : IndexError',
     'Une liste de neuf elements va de 0 a 8. Le numero 9 n\'existe pas : Python dit IndexError.'],

    ['plateau = ["1", "2", "X", "4", "5", "6", "7", "8", "9"]\n\nDans ce jeu, une case LIBRE contient encore son numero.\nCombien de cases sont encore libres ?',
     ['9', '1', '8', '0'], '8',
     'Une seule case a change : la troisieme contient "X" au lieu de "3". Les huit autres contiennent encore leur numero, donc elles sont libres.'],

    ['age = 11\nprint(age >= 12 and age <= 18)\n\nQu\'est-ce qui s\'affiche ?',
     ['False', 'True', '11', 'une erreur rouge'], 'False',
     '11 n\'est pas plus grand ou egal a 12. Avec and, une seule reponse fausse suffit pour que tout soit faux.'],

    ['Les cases d\'un jeu portent les numeros 1 a 9.\n\nPour REFUSER un numero qui n\'existe pas, j\'ecris :',
     ['if case < 1 and case > 9:', 'if case < 1 or case > 9:', 'if case >= 1 or case <= 9:', 'if case > 1 or case < 9:'], 'if case < 1 or case > 9:',
     'Une seule des deux raisons suffit pour refuser : c\'est or. Avec and, il faudrait un nombre a la fois plus petit que 1 ET plus grand que 9 : ca n\'existe pas, donc rien ne serait jamais refuse.'],

    ['fini = True\naide = False\nprint(fini or aide)\n\nQu\'est-ce qui s\'affiche ?',
     ['False', 'fini', 'une erreur rouge', 'True'], 'True',
     'Avec or, il suffit d\'UNE seule reponse vraie. La premiere l\'est : c\'est fini, le reste n\'est meme plus regarde.'],

    ['Que veut dire le mot  elif  ?',
     ['sinon, est-ce que...', 'sinon, dans tous les cas', 'si et seulement si', 'la fin du programme'], 'sinon, est-ce que...',
     'elif, c\'est else + if colles ensemble : "sinon, est-ce que...". Il ne pose sa question QUE SI la precedente etait fausse.'],

    ['note = 95\n\nif note >= 60:\n    print("Recu")\nif note >= 90:\n    print("Felicitations")\n\nAttention, ce sont DEUX if separes. Qu\'est-ce qui s\'affiche ?',
     ['Recu seulement', 'Felicitations seulement', 'Recu, puis Felicitations', 'rien du tout'], 'Recu, puis Felicitations',
     'Deux if separes, ce sont DEUX questions independantes : Python pose les deux, et les deux sont vraies. Avec elif, la deuxieme n\'aurait meme pas ete regardee.'],

    ['note = 18\n\nif note >= 10:\n    print("Passable")\nelif note >= 16:\n    print("Tres bien")\n\nQu\'est-ce qui s\'affiche ?',
     ['Tres bien', 'Passable, puis Tres bien', 'rien du tout', 'Passable'], 'Passable',
     '18 >= 10 est DEJA vrai : Python s\'arrete la et n\'ira jamais voir la ligne du 16. Un 20 sur 20 serait annonce "Passable".'],

    ['note = 100\n\nif note >= 90:\n    print("Medaille d\'or")\nelif note == 100:\n    print("Sans faute !")\n\nQu\'est-ce qui s\'affiche ?',
     ['Sans faute !', 'Medaille d\'or', 'Medaille d\'or, puis Sans faute !', 'rien du tout'], 'Medaille d\'or',
     '100 est deja plus grand ou egal a 90 : le premier chemin passe, et le second n\'est jamais regarde. Le cas le PLUS PRECIS — exactement 100 — devait etre ecrit EN PREMIER.'],

    ['Dans une cascade de  if / elif / else , dans quel ordre faut-il ranger les questions ?',
     ['De la plus PRECISE a la plus LARGE', 'De la plus LARGE a la plus PRECISE', 'Dans n\'importe quel ordre', 'Par ordre alphabetique'], 'De la plus PRECISE a la plus LARGE',
     'Python s\'arrete au premier chemin qui passe. La question la plus difficile a satisfaire doit donc venir en premier, et celle qui attrape tout le monde en dernier — souvent, c\'est le else.']
  ];

  var sections = {0: ['PARTIE A — Parler, demander, compter', 'Le texte, les nombres, et la difference entre les deux.'], 4: ['PARTIE B — Decider : if et else', 'Une question, deux chemins. Et le decalage qui dit qui depend de qui.'], 8: ['PARTIE C — La liste et le decalage', 'Une boite a neuf compartiments, et le numero de chacun.'], 12: ['PARTIE D — and et or', 'Reunir plusieurs questions en une seule.'], 15: ['PARTIE E — Plusieurs chemins : elif', 'Trois chemins ou plus, et l\'ordre dans lequel on les ecrit.']};

  questions.forEach(function (q, i) {
    if (sections[i]) {
      form.addSectionHeaderItem().setTitle(sections[i][0]).setHelpText(sections[i][1]);
    }
    var item = form.addMultipleChoiceItem();
    item.setTitle(q[0]);
    item.setPoints(1);
    item.setRequired(true);
    item.setChoices(q[1].map(function (texte) {
      return item.createChoice(texte, texte === q[2]);
    }));
    item.setFeedbackForCorrect(FormApp.createFeedback().setText('Bravo !').build());
    item.setFeedbackForIncorrect(FormApp.createFeedback().setText(q[3]).build());
  });

  try { form.setPublished(true); } catch (e) {
    Logger.log('A faire a la main : ouvrez le formulaire et cliquez sur « Publier ».');
  }

  Logger.log('#######################################################');
  Logger.log('##  A FAIRE MAINTENANT, SINON L\'ELEVE NE VERRA RIEN  ##');
  Logger.log('#######################################################');
  Logger.log('⚙ Parametres > Questionnaires :');
  Logger.log('   « Publier les notes » -> Immediatement apres chaque envoi');
  Logger.log('   « Le participant peut voir » -> les TROIS cases');
  Logger.log('Puis repondez vous-meme pour verifier.');
  Logger.log('');
  Logger.log('LIEN A ENVOYER AUX PARENTS :');
  Logger.log(form.getPublishedUrl());
  Logger.log('LIEN POUR MODIFIER :');
  Logger.log(form.getEditUrl());
  Logger.log('20 questions a choix multiples = 20 points, 100 % automatique.');
}
