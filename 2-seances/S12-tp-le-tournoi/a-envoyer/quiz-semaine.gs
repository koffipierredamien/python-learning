/**
 * =====================================================================
 *  AcProKids Coding Camp — Quiz de la semaine n°10
 *  tout ce qu'on a appris depuis octobre
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

  var form = FormApp.create('Quiz n°10 — Le bilan des deux mois');

  form.setDescription(
      'AcProKids Coding Camp — Jeremiah Geeks\n\n' +
      'Dernier quiz de l\'annee 2026 ! Il reprend TOUT : les listes, l\'indice, and et or, la boucle, et la victoire. Prends ton temps.\n\n' +
      'RAPPELS A GARDER SOUS LES YEUX :\n' +
      '    indice = case - 1\n    and -> il faut tout  ·  or -> il suffit d\'un\n    une boucle qui n\'avance pas ne s\'arrete jamais\n\n' +
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
    ['print("3" + "4")',
     ['34', '7', '3 4', 'une erreur rouge'], '34',
     'Texte + texte : les deux sont colles.'],

    ['age = input("Ton age ? ")\nprint(age + 1)\n\nLe joueur tape 12.',
     ['13', '121', 'Une erreur rouge : TypeError', '12'], 'Une erreur rouge : TypeError',
     'input rend TOUJOURS du texte. Il manque la ligne age = int(age).'],

    ['tour = 0\ntour = tour + 1\ntour = tour + 1\nprint(tour)',
     ['0', '2', '1', '3'], '2',
     'Deux fois « reprends ce qu\'il y a dedans et ajoute 1 ».'],

    ['print("Score : " + str(60))',
     ['Score : str(60)', 'une erreur rouge', 'Score : 6 0', 'Score : 60'], 'Score : 60',
     'str() transforme le nombre en texte, et le + peut alors le coller.'],

    ['if age > 11:\n    print("Jeremiah")\nelse:\n    print("Jerusalem")\n\nage = 11 :',
     ['Jerusalem', 'Jeremiah', 'les deux', 'rien'], 'Jerusalem',
     '11 n\'est pas PLUS GRAND que 11. C\'est le else qui est pris.'],

    ['plateau = ["1","2","3","4","5","6","7","8","9"]\nplateau[6] = "O"\n\nQuelle case du joueur porte le O ?',
     ['La case 6', 'La case 7', 'La case 8', 'Aucune'], 'La case 7',
     'indice 6 = septieme case. indice = case - 1, donc case = indice + 1.'],

    ['print(True and False)',
     ['True', '0', 'une erreur rouge', 'False'], 'False',
     'Avec and, il faut que tout soit vrai.'],

    ['print(False or True)',
     ['False', '1', 'True', 'une erreur rouge'], 'True',
     'Avec or, il suffit d\'une seule.'],

    ['tour = 0\nwhile tour < 4:\n    print("A")\n    tour = tour + 1\n\nCombien de A ?',
     ['4', '3', '5', 'une infinite'], '4',
     'tour vaut 0, 1, 2, 3 : quatre tours.'],

    ['Qu\'est-ce qui fait qu\'une boucle s\'arrete un jour ?',
     ['Le mot while', 'Les deux-points', 'Rien, elle s\'arrete toute seule', 'La ligne qui fait avancer le compteur'], 'La ligne qui fait avancer le compteur',
     'Sans elle, la question repond toujours la meme chose : Ctrl + C.'],

    ['Dans ton jeu, qu\'est-ce qui empeche de jouer deux fois la meme case ?',
     ['case <= 9', 'plateau[case - 1] == str(case)', 'le compteur tour', 'l\'alternance des symboles'], 'plateau[case - 1] == str(case)',
     'Une case libre contient encore son numero : c\'est ce test qui refuse une case prise.'],

    ['Qu\'est-ce qui empeche de jouer la case 0 ?',
     ['case <= 9', 'le while', 'case >= 1', 'rien, c\'est un bug'], 'case >= 1',
     'C\'est le morceau ajoute a la seance 9, qui a tue le bug du zero.'],

    ['Combien de lignes gagnantes ton jeu verifie-t-il, a chaque coup ?',
     ['8', '3', '4', '9'], '8',
     '3 lignes, 3 colonnes, 2 diagonales.'],

    ['Ton jeu dit « MATCH NUL » alors que tu viens d\'aligner trois X.\nOu regardes-tu en premier ?',
     ['Le nom des joueurs', 'Le plateau de depart', 'La ligne input', 'Le bloc des 8 if : est-il DANS la boucle ?'], 'Le bloc des 8 if : est-il DANS la boucle ?',
     'S\'il est apres la boucle, il ne teste qu\'une fois, a la fin : le gagnant n\'est jamais detecte en cours de partie.'],

    ['Qu\'est-ce que tu sais faire aujourd\'hui, que tu ne savais pas le 17 octobre ?',
     ['Afficher du texte', 'Garder des choses dans une liste et faire tourner une boucle', 'Poser une question au joueur', 'Utiliser int() et str()'], 'Garder des choses dans une liste et faire tourner une boucle',
     'Les trois autres, tu les savais deja avant octobre. Les listes et la boucle, c\'est le travail de ces deux mois -- et c\'est ce qui a rendu ton jeu jouable.']
  ];

  var sections = {0: ['PARTIE A — Les bases', 'Ce qu\'on savait deja avant octobre.'], 5: ['PARTIE B — Les listes et la boucle', 'Le coeur des deux mois.'], 10: ['PARTIE C — Ton jeu, en entier', 'Du premier print au tournoi.']};

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
