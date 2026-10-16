/**
 * =====================================================================
 *  AcProKids Coding Camp — Quiz de la semaine n°7
 *  les operateurs logiques
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

  var form = FormApp.create('Quiz n°7 — and, or, et une seule question');

  form.setDescription(
      'AcProKids Coding Camp — Jeremiah Geeks\n\n' +
      'Ce quiz porte sur la seance de samedi : and (il faut TOUT) et or (il suffit d\'UN), et la condition unique du jeu.\n\n' +
      'RAPPELS A GARDER SOUS LES YEUX :\n' +
      '    and  ->  il faut que TOUT soit vrai\n    or   ->  il suffit qu\'UNE SEULE chose soit vraie\n    la condition du coup valide : case >= 1 and case <= 9 and plateau[case-1] == str(case)\n\n' +
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
    ['print(True and True)',
     ['True', 'False', '1', 'une erreur rouge'], 'True',
     'Avec and, il faut que les DEUX soient vrais. Ici, les deux le sont.'],

    ['print(True and False)',
     ['True', '0', 'False', 'une erreur rouge'], 'False',
     'Un seul faux suffit a tout rendre faux, avec and.'],

    ['print(False or True)',
     ['False', 'True', 'None', 'une erreur rouge'], 'True',
     'Avec or, il suffit qu\'UNE des deux soit vraie.'],

    ['print(False or False)',
     ['True', '0', 'une erreur rouge', 'False'], 'False',
     'Les deux sont fausses : il n\'y en a aucune de vraie, donc False.'],

    ['age = 14\nprint(age >= 12 and age <= 18)',
     ['True', 'False', '14', 'une erreur rouge'], 'True',
     '14 est bien plus grand que 12 ET plus petit que 18 : les deux sont vraies.'],

    ['age = 20\nprint(age >= 12 and age <= 18)',
     ['True', 'False', '20', 'une erreur rouge'], 'False',
     '20 est bien plus grand que 12, mais PAS plus petit que 18. Avec and, il faut les deux.'],

    ['Pour dire « le nombre est entre 1 et 9 », j\'ecris :',
     ['nombre >= 1 or nombre <= 9', 'nombre >= 1 and nombre >= 9', '1 < nombre < 9 and', 'nombre >= 1 and nombre <= 9'], 'nombre >= 1 and nombre <= 9',
     'Les deux bornes doivent etre vraies en meme temps : c\'est and.'],

    ['Pour dire « la case n\'existe pas », j\'ecris :',
     ['case < 1 and case > 9', 'case == 0 or case == 10', 'case < 1 or case > 9', 'case != 1 and case != 9'], 'case < 1 or case > 9',
     'Un nombre ne peut pas etre a la fois plus petit que 1 ET plus grand que 9 : avec and, ce serait toujours faux.'],

    ['print(5 > 3 and 2 > 7)',
     ['False', 'True', '5', 'une erreur rouge'], 'False',
     'La premiere est vraie, la deuxieme est fausse. Avec and : faux.'],

    ['print(5 > 3 or 2 > 7)',
     ['False', '2', 'une erreur rouge', 'True'], 'True',
     'La premiere suffit : avec or, une seule vraie suffit.'],

    ['if case >= 1 and case <= 9:\n    print("OK")\n\ncase = 0 : qu\'est-ce qui s\'affiche ?',
     ['OK', 'rien', 'une erreur rouge', 'False'], 'rien',
     '0 n\'est pas plus grand ou egal a 1 : la condition est fausse, et il n\'y a pas de else.'],

    ['Combien de  if  y a-t-il maintenant dans le tour d\'un joueur ?',
     ['Deux, l\'un dans l\'autre', 'Trois', 'Un seul', 'Aucun'], 'Un seul',
     'C\'est tout l\'interet de la seance : le if dans le if est devenu UN SEUL if.'],

    ['Que se passe-t-il maintenant si le joueur tape 0 ?',
     ['Le jeu refuse', 'Le symbole se pose dans la case 9', 'Le jeu plante', 'Le jeu accepte'], 'Le jeu refuse',
     'Le bug est repare : c\'est le morceau case >= 1 qui s\'en charge.'],

    ['Dans  case >= 1 and case <= 9 and plateau[case-1] == str(case),\ncombien de questions sont posees ?',
     ['1', '2', '9', '3'], '3',
     'Trois questions reliees par deux and. Il faut que les trois soient vraies.'],

    ['if case >= 1 and case <= 9 or plateau[case-1] == str(case):\n\nQuel est le probleme ?',
     ['Il n\'y a aucun probleme', 'Avec or, une case deja prise serait acceptee', 'Ca provoque une erreur rouge', 'Le jeu refuserait tout'], 'Avec or, une case deja prise serait acceptee',
     'Il faut les TROIS conditions : c\'est and partout, pas or.']
  ];

  var sections = {0: ['PARTIE A — and et or', 'Vrai ou faux : la table a connaitre.'], 6: ['PARTIE B — Des conditions utiles', 'Les conditions qu\'on ecrit pour de vrai.'], 11: ['PARTIE C — Le jeu', 'Ce que la condition unique a change.']};

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
