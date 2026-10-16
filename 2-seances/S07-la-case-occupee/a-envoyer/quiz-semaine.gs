/**
 * =====================================================================
 *  AcProKids Coding Camp — Quiz de la semaine n°6
 *  la case libre, et le if dans le if
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

  var form = FormApp.create('Quiz n°6 — On ne joue pas deux fois au meme endroit');

  form.setDescription(
      'AcProKids Coding Camp — Jeremiah Geeks\n\n' +
      'Ce quiz porte sur la seance de samedi : reconnaitre une case libre, et ecrire un if DANS un if.\n\n' +
      'RAPPELS A GARDER SOUS LES YEUX :\n' +
      '    une case libre contient ENCORE SON NUMERO\n    plateau[case - 1] == str(case)  ->  True si la case est libre\n    4 espaces pour le premier if, 8 pour le deuxieme\n\n' +
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
    ['plateau = ["1", "2", "3", "4", "X", "6", "7", "8", "9"]\ncase = 3\nprint(plateau[case - 1] == str(case))',
     ['False', 'True', '3', 'une erreur rouge'], 'True',
     'plateau[2] contient encore "3", donc la case 3 est LIBRE : True.'],

    ['Avec le meme plateau, case = 5 :\nprint(plateau[case - 1] == str(case))',
     ['True', 'X', 'une erreur rouge', 'False'], 'False',
     'plateau[4] contient "X", pas "5". La case est PRISE : False.'],

    ['A quoi sert  str(case)  dans cette comparaison ?',
     ['A transformer le nombre en texte, pour le comparer', 'A transformer le texte en nombre', 'A afficher la case', 'A rien du tout'], 'A transformer le nombre en texte, pour le comparer',
     'La case contient du TEXTE. Pour comparer, il faut comparer du texte avec du texte.'],

    ['Une case libre, qu\'est-ce qu\'elle contient ?',
     ['Rien du tout', 'Un espace', 'Son propre numero', 'Le mot libre'], 'Son propre numero',
     'C\'est toute l\'astuce : une case libre contient encore son numero, et c\'est comme ca qu\'on la reconnait.'],

    ['plateau[case - 1] = str(case)\n\nQu\'est-ce que cette ligne fait ?',
     ['Elle verifie si la case est libre', 'Elle REMET le numero dans la case', 'Elle affiche la case', 'Elle provoque une erreur'], 'Elle REMET le numero dans la case',
     'Attention : un seul = range dans la case. Pour comparer, il en faut DEUX.'],

    ['if case > 9:\n    print("A")\nelse:\n    if plateau[case - 1] == str(case):\n        print("B")\n    else:\n        print("C")\n\ncase = 12 : qu\'est-ce qui s\'affiche ?',
     ['A', 'B', 'C', 'rien'], 'A',
     '12 est plus grand que 9 : on prend le premier chemin, et on ne pose meme pas la deuxieme question.'],

    ['Meme programme, case = 3 et la case 3 est libre :',
     ['A', 'C', 'B', 'A puis B'], 'B',
     'La case existe, donc on passe au else. Elle est libre, donc on prend le premier chemin du deuxieme if.'],

    ['Meme programme, case = 5 et la case 5 est prise :',
     ['A', 'B', 'B puis C', 'C'], 'C',
     'La case existe mais elle est prise : c\'est le else du deuxieme if.'],

    ['Combien d\'espaces faut-il devant le deuxieme  if  ?',
     ['0', '4', '8', '2'], '4',
     'Le deuxieme if est DANS le else du premier : il est decale de 4 espaces. Ce qui est dedans sera a 8.'],

    ['else:\nif plateau[case - 1] == str(case):\n\nQue se passe-t-il ?',
     ['Ca marche quand meme', 'Une SyntaxError', 'Une erreur rouge : IndentationError', 'Rien'], 'Une erreur rouge : IndentationError',
     'Apres les deux-points, il faut decaler. Le deuxieme if doit etre DANS le else.'],

    ['Dans ton jeu, que se passe-t-il si le joueur 2 rejoue la case du joueur 1 ?',
     ['Le jeu refuse et il perd son tour', 'Le O remplace le X', 'Le jeu plante', 'Le jeu demande une autre case'], 'Le jeu refuse et il perd son tour',
     'C\'est exactement ce qu\'on a programme samedi : le jeu refuse, et le plateau ne bouge pas.'],

    ['Et si le joueur tape 0 dans le jeu de samedi soir ?',
     ['Il accepte et pose dans la case 9', 'Il plante', 'Il redemande une autre case', 'Il refuse, en disant que la case est DEJA PRISE'], 'Il refuse, en disant que la case est DEJA PRISE',
     'Piege ! 0 - 1 vaut -1, et plateau[-1] est la DERNIERE case : elle contient "9", pas "0". Le test de la case libre refuse donc -- par accident, et avec un message faux. Le bug n\'est pas repare, il est CACHE. On le tue vraiment a la seance 9.'],

    ['Pourquoi le jeu refuse-t-il la case 12 ?',
     ['Parce que la case 12 est prise', 'Parce que  case > 9  est vrai', 'Parce que 12 n\'est pas un nombre', 'Parce que le plateau est plein'], 'Parce que  case > 9  est vrai',
     'La premiere question du if teste si la case existe.'],

    ['plateau[case - 1] = "X"  est ecrite COLLEE A GAUCHE, hors du if.\nQue se passe-t-il ?',
     ['Une erreur rouge', 'Le X ne se pose jamais', 'Le X se pose meme quand le coup est refuse', 'Rien ne change'], 'Le X se pose meme quand le coup est refuse',
     'Ce qui n\'est pas decale ne depend d\'aucun if : ca se fait toujours.'],

    ['Combien de fois faut-il recopier le bloc du tour, pour que DEUX joueurs jouent ?',
     ['2 fois', '1 fois', '9 fois', '18 fois'], '2 fois',
     'Une fois par joueur. Et pour neuf tours, il faudrait le recopier neuf fois : c\'est pour ca qu\'on apprendra la boucle.']
  ];

  var sections = {0: ['PARTIE A — La case libre', 'Comment le programme sait qu\'une case est prise.'], 5: ['PARTIE B — Le if dans le if', 'Une question dans une question.'], 10: ['PARTIE C — Le jeu complet', 'Ce que fait ton jeu, maintenant.']};

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
