/**
 * =====================================================================
 *  AcProKids Coding Camp — Quiz de la semaine n°5
 *  les listes, l'indice, et la pose d'un symbole
 *
 *  POUR LES ENFANTS QUI N'ONT PAS D'ORDINATEUR : ils le font A LA PLACE
 *  de l'exercice de maison. Un telephone suffit.
 *
 *  15 questions a choix multiples = 15 points.
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

  var form = FormApp.create('Quiz n°5 — Le plateau se souvient');

  form.setDescription(
      'AcProKids Coding Camp — Jeremiah Geeks\n\n' +
      'Ce quiz porte sur la seance de samedi : la LISTE, l\'INDICE qui commence a zero, et la ligne plateau[case - 1].\n\n' +
      'RAPPELS A GARDER SOUS LES YEUX :\n' +
      '    le premier compartiment porte le numero 0\n    indice = case - 1\n    une liste de 9 cases va de l\'indice 0 a l\'indice 8\n\n' +
      '15 questions, 15 points. Tu as ta note et les explications a la fin. ' +
      'Se tromper n\'est pas grave : c\'est comme ca qu\'on apprend.');

  form.setIsQuiz(true);
  form.setShowLinkToRespondAgain(false);
  form.setConfirmationMessage(
      'C\'est envoye ! Clique sur « Afficher le score » pour voir ta note et les explications. ' +
      'A samedi, 12 h !');

  form.addTextItem().setTitle('Ton prenom et ton nom').setRequired(true);
  form.addMultipleChoiceItem()
      .setTitle('Ta classe')
      .setChoiceValues(['Jerusalem Geeks (9 – 12 ans)', 'Jeremiah Geeks (12 – 18 ans)'])
      .setRequired(true);

  var questions = [
    ['equipe = ["Joyce", "Gedeon", "Sarah"]\nprint(equipe[0])\n\nQu\'est-ce qui s\'affiche ?',
     ['Joyce', 'Gedeon', 'Sarah', 'equipe'], 'Joyce',
     'Le PREMIER element porte le numero 0. equipe[0], c\'est Joyce.'],

    ['print(equipe[2])',
     ['Gedeon', 'Joyce', 'Sarah', 'une erreur rouge'], 'Sarah',
     'Les numeros sont 0, 1, 2. Le numero 2 est donc le troisieme : Sarah.'],

    ['print(equipe[3])\n\nQue se passe-t-il ?',
     ['Ca affiche Sarah', 'Une erreur rouge : IndexError', 'Ca n\'affiche rien', 'Ca affiche equipe'], 'Une erreur rouge : IndexError',
     'Une liste de trois elements a les numeros 0, 1 et 2. Le 3 n\'existe pas.'],

    ['equipe[1] = "Ethan"\nprint(equipe)\n\nQu\'est-ce qui s\'affiche ?',
     ['[\'Ethan\', \'Gedeon\', \'Sarah\']', '[\'Joyce\', \'Gedeon\', \'Ethan\']', 'une erreur rouge', '[\'Joyce\', \'Ethan\', \'Sarah\']'], '[\'Joyce\', \'Ethan\', \'Sarah\']',
     'equipe[1] est le DEUXIEME element. On remplace Gedeon par Ethan.'],

    ['Combien d\'elements a cette liste ?\n\nscores = [10, 25, 7, 3]',
     ['4', '3', '5', 'On ne peut pas savoir'], '4',
     'Quatre elements, donc des indices qui vont de 0 a 3.'],

    ['La case 1 du plateau est a quel indice ?',
     ['1', '0', '2', '9'], '0',
     'indice = case - 1. La case 1 est donc a l\'indice 0.'],

    ['La case 7 est a quel indice ?',
     ['7', '8', '5', '6'], '6',
     '7 - 1 = 6. Toujours un de moins.'],

    ['plateau = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]\ncase = 3\nplateau[case - 1] = "X"\n\nOu se pose le X ?',
     ['Sur la case 2', 'Sur la case 4', 'Sur la case 3', 'Nulle part : erreur'], 'Sur la case 3',
     'case - 1 vaut 2, et plateau[2] est bien la TROISIEME case.'],

    ['Et si on ecrit  plateau[case] = "X"  avec case = 3 ?',
     ['Le X se pose sur la case 4', 'Le X se pose sur la case 3', 'Une erreur rouge', 'Rien ne se passe'], 'Le X se pose sur la case 4',
     'Sans le - 1, on decale tout d\'une case. Et il n\'y a AUCUNE erreur rouge : c\'est le piege.'],

    ['plateau[9] = "X"\n\nQue se passe-t-il ?',
     ['Le X se pose sur la case 9', 'Le X se pose sur la case 10', 'Rien', 'Une erreur rouge : IndexError'], 'Une erreur rouge : IndexError',
     'Une liste de 9 cases va de 0 a 8. L\'indice 9 n\'existe pas : la case 9 est a l\'indice 8.'],

    ['Pourquoi ecrit-on  ["1", "2", "3", ...]  avec des guillemets, et pas [1, 2, 3] ?',
     ['Parce que Python l\'exige', 'Pour pouvoir les coller a du texte avec le +', 'Pour qu\'ils soient plus jolis', 'Il n\'y a aucune raison'], 'Pour pouvoir les coller a du texte avec le +',
     'Les cases sont affichees avec le + , qui ne sait coller que du texte.'],

    ['plateau = ["1", "2", "3", "4", "X", "6", "7", "8", "9"]\nprint(plateau[4])',
     ['5', '4', 'X', 'une erreur rouge'], 'X',
     'L\'indice 4, c\'est la cinquieme case : elle contient X.'],

    ['Dans quel ordre faut-il ecrire ces deux lignes pour voir le plateau changer ?\n\n   A : les 5 lignes d\'affichage\n   B : plateau[case - 1] = "X"',
     ['B puis A', 'A puis B', 'L\'ordre n\'a aucune importance', 'Il faut les ecrire en meme temps'], 'B puis A',
     'On pose D\'ABORD, on affiche ENSUITE. Sinon on affiche l\'ancien plateau.'],

    ['case = input("Quelle case ? ")\nplateau[case - 1] = "X"\n\nQue se passe-t-il ?',
     ['Le X se pose', 'Une IndexError', 'Rien ne se passe', 'Une erreur rouge : TypeError'], 'Une erreur rouge : TypeError',
     'input rend du TEXTE. On ne peut pas faire texte - 1. Il manque la ligne case = int(case).'],

    ['Que contient la case 5 au DEBUT de la partie ?',
     ['Rien, elle est vide', 'Le texte "5"', 'Le nombre 5', 'Un espace " "'], 'Le texte "5"',
     'Au depart, chaque case contient son propre numero, en texte. C\'est ce qui permet au joueur de voir les cases libres.']
  ];

  var sections = {0: ['PARTIE A — Lire une liste', 'Souviens-toi : on compte a partir de ZERO.'], 5: ['PARTIE B — L\'indice et la pose', 'La case du joueur, et l\'indice de Python.'], 10: ['PARTIE C — Le plateau du jeu', 'Le plateau est une liste de neuf cases.']};

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
  Logger.log('15 questions a choix multiples = 15 points, 100 % automatique.');
}
