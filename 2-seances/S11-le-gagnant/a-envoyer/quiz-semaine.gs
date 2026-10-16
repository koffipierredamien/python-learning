/**
 * =====================================================================
 *  AcProKids Coding Camp — Quiz de la semaine n°9
 *  les lignes gagnantes et la fin de partie
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

  var form = FormApp.create('Quiz n°9 — Le jeu sait qui gagne');

  form.setDescription(
      'AcProKids Coding Camp — Jeremiah Geeks\n\n' +
      'Ce quiz porte sur la seance ou votre jeu a ete termine : les huit lignes gagnantes, et la partie qui s\'arrete.\n\n' +
      'RAPPELS A GARDER SOUS LES YEUX :\n' +
      '    gagner = trois cases qui contiennent LA MEME CHOSE\n    8 lignes : 3 lignes + 3 colonnes + 2 diagonales\n    while tour < 9 and gagnant == ""  : deux raisons de s\'arreter\n\n' +
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
    ['Combien y a-t-il de facons de gagner au morpion ?',
     ['3', '8', '6', '9'], '8',
     '3 lignes + 3 colonnes + 2 diagonales = 8.'],

    ['Les indices de la PREMIERE LIGNE du plateau sont :',
     ['1, 2, 3', '0, 3, 6', '1, 4, 7', '0, 1, 2'], '0, 1, 2',
     'On compte a partir de zero : la premiere ligne, c\'est 0, 1 et 2.'],

    ['Les indices de la PREMIERE COLONNE sont :',
     ['0, 1, 2', '1, 4, 7', '0, 3, 6', '0, 4, 8'], '0, 3, 6',
     'On descend de trois en trois : 0, puis 3, puis 6.'],

    ['Les indices d\'une DIAGONALE sont :',
     ['0, 4, 8', '0, 1, 2', '2, 4, 8', '1, 4, 7'], '0, 4, 8',
     'Les deux diagonales sont 0-4-8 et 2-4-6. Elles passent toutes les deux par le centre, l\'indice 4.'],

    ['plateau = ["X", "X", "X", "4", "O", "6", "O", "8", "9"]\nprint(plateau[0] == plateau[1] and plateau[1] == plateau[2])',
     ['False', 'True', 'X', 'une erreur rouge'], 'True',
     'Les trois premieres cases contiennent toutes X : c\'est gagne.'],

    ['Un plateau tout neuf : ["1","2","3","4","5","6","7","8","9"].\nEst-ce que la premiere ligne declenche une victoire ?',
     ['Oui, car les cases sont vides', 'Oui, c\'est un bug', 'Non, car "1", "2" et "3" sont differents', 'On ne peut pas savoir'], 'Non, car "1", "2" et "3" sont differents',
     'C\'est pour ca qu\'on a mis les NUMEROS dans les cases a la seance 6 : ils ne seront jamais egaux entre eux.'],

    ['Ou faut-il ecrire  gagnant = ""  ?',
     ['Avant la boucle, une seule fois', 'Au debut de chaque tour', 'Apres la boucle', 'Dans le if du coup valide'], 'Avant la boucle, une seule fois',
     'Si on la remet a chaque tour, le gagnant est efface et la partie ne s\'arrete jamais.'],

    ['while tour < 9 and gagnant == "":\n\nCombien de raisons d\'arreter la partie ?',
     ['1', '3', '9', '2'], '2',
     'Le plateau est plein, OU quelqu\'un a gagne. Tant que les deux conditions sont vraies, on continue.'],

    ['Ou faut-il placer le bloc des 8  if  ?',
     ['Avant la boucle', 'Dans la boucle, juste apres la pose', 'Apres la boucle', 'Au tout debut du programme'], 'Dans la boucle, juste apres la pose',
     'Il faut verifier apres CHAQUE coup. Avant la pose, on testerait le plateau d\'avant.'],

    ['Si le bloc des 8 if est place AVANT la pose du symbole, que se passe-t-il ?',
     ['Le jeu peut annoncer un gagnant qui s\'appelle « 5 »', 'Rien de special', 'Une erreur rouge', 'La partie ne demarre pas'], 'Le jeu peut annoncer un gagnant qui s\'appelle « 5 »',
     'Il teste le plateau avant le coup — et il peut aussi rater la victoire qui vient d\'etre jouee.'],

    ['Si le bloc des 8 if est place APRES la boucle, que se passe-t-il ?',
     ['Il annonce toujours X gagnant', 'Une erreur rouge', 'Le jeu joue toujours les 9 coups', 'Rien ne change'], 'Le jeu joue toujours les 9 coups',
     'On ne teste qu\'une seule fois, a la fin : la partie ne s\'arrete jamais sur une victoire.'],

    ['gagnant = plateau[0]\n\nQue contient gagnant apres cette ligne, si la premiere ligne est pleine de X ?',
     ['"0"', '"gagnant"', 'le nombre 0', '"X"'], '"X"',
     'On range dans gagnant le CONTENU de la case 0, c\'est-a-dire le symbole du vainqueur.'],

    ['Comment le jeu sait-il qu\'il y a match nul ?',
     ['Il compte les X et les O', 'La boucle est finie et gagnant est reste vide', 'Il regarde si le plateau est plein', 'Il ne le sait pas'], 'La boucle est finie et gagnant est reste vide',
     'Si on sort de la boucle sans gagnant, c\'est que les 9 cases ont ete jouees sans alignement.'],

    ['En combien de coups, au minimum, peut-on gagner ?',
     ['5', '3', '4', '9'], '5',
     'Celui qui commence joue les coups 1, 3, 5 : il lui faut donc au moins cinq coups joues au total pour en avoir trois.'],

    ['Ton jeu annonce « BRAVO Joyce ! » alors que c\'est Gedeon qui a aligne trois O.\nOu est le probleme ?',
     ['Les 8 if sont faux', 'La boucle est mal ecrite', 'Le verdict teste mal le contenu de gagnant', 'C\'est normal'], 'Le verdict teste mal le contenu de gagnant',
     'Le bloc final doit comparer gagnant avec "X" puis avec "O", et afficher le bon nom.']
  ];

  var sections = {0: ['PARTIE A — Gagner', 'Trois cases pareilles, et rien d\'autre.'], 6: ['PARTIE B — La boite gagnant', 'Une boite qui se cree une seule fois.'], 11: ['PARTIE C — Ton jeu', 'Ce qu\'il fait maintenant, du debut a la fin.']};

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
