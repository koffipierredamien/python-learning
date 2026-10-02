/**
 * =====================================================================
 *  AcProKids Coding Camp — Test de révision n°3  (après la séance 4)
 *  Formulaire Google NOTÉ, en deux parties :
 *     A. « Que va afficher ce programme ? »  — corrigé automatiquement
 *     B. « Écris le code »                   — l'élève tape du code
 *
 *  Ce qu'il révise : int() et str(), le compteur tour = tour + 1,
 *  les comparaisons, et la décision if / else (avec le décalage).
 * =====================================================================
 *
 *  MODE D'EMPLOI :
 *   1. script.google.com  →  Nouveau projet
 *   2. Effacez le code présent, collez TOUT ce fichier
 *   3. Bouton ▶ Exécuter  →  autorisez à la première utilisation
 *   4. Le journal affiche le lien à envoyer et le lien pour modifier
 *
 *  ⚠ UNE SEULE CHOSE À FAIRE À LA MAIN, dans le formulaire (4 minutes) :
 *     les 8 questions « Écris le code » sont des réponses libres. Google
 *     ne permet pas de fixer leur corrigé depuis un script — il faut
 *     l'ajouter dans le formulaire : sur chaque question, « Corrigé » →
 *     « Ajouter une réponse correcte ». Les réponses à coller sont dans
 *     le fichier  formulaire-exercices.md,  déjà écrites, variantes
 *     comprises. Sans cela, ces 8 questions se corrigent à la main.
 * =====================================================================
 */

function creerLeTest() {

  var form = FormApp.create('Test n°3 — les nombres, le compteur et les décisions');

  form.setDescription(
      'AcProKids Coding Camp — Jerusalem Geeks & Jeremiah Geeks\n\n' +
      'Ce test reprend la séance de samedi : le texte et les nombres (int et str), ' +
      'le compteur tour = tour + 1, les opérateurs de comparaison, et la décision if / else.\n\n' +
      'Il y a deux parties :\n' +
      '  A. Que va afficher ce programme ? — tu lis le code dans ta tête\n' +
      '  B. Écris le code — tu tapes toi-même les bonnes lignes\n\n' +
      'Aucun ordinateur n\'est nécessaire : on peut répondre depuis un téléphone. ' +
      'Tu as ta note à la fin, avec les explications. Se tromper n\'est pas grave : ' +
      'c\'est comme ça qu\'on apprend.');

  form.setIsQuiz(true);
  form.setShowLinkToRespondAgain(false);
  form.setConfirmationMessage(
      'C\'est envoyé ! Clique sur « Afficher le score » pour voir ta note et les explications. ' +
      'À samedi, 12 h !');

  // ------------------------------------------------------------ identité
  form.addTextItem().setTitle('Ton prénom et ton nom').setRequired(true);
  form.addMultipleChoiceItem()
      .setTitle('Ta classe')
      .setChoiceValues(['Jerusalem Geeks (9 – 12 ans)', 'Jeremiah Geeks (12 – 18 ans)'])
      .setRequired(true);

  // ============================================================ PARTIE A
  form.addSectionHeaderItem()
      .setTitle('PARTIE A — Que va afficher ce programme ?')
      .setHelpText('Lis chaque programme dans ta tête, ligne par ligne, de haut en bas. '
                 + 'Souviens-toi : le signe = veut dire « range dans », un opérateur de comparaison '
                 + 'répond True ou False, et le décalage de 4 espaces dit ce qui appartient au if.');

  var reflexion = [

    ['a = "5"\nb = a + a\nprint(b)\n\nQu\'est-ce qui s\'affiche ?',
     ['55', '10', '5 5', 'une erreur rouge'], '55',
     'Entre guillemets, 5 est du TEXTE. Le + colle deux textes : 55. Pour obtenir 10, il aurait fallu des nombres.'],

    ['age = input("Ton age ? ")\nprint(age + 1)\n\nLe joueur tape  12.  Que se passe-t-il ?',
     ['Ça affiche 13', 'Ça affiche 121', 'Une erreur rouge : TypeError', 'Ça affiche 12'],
     'Une erreur rouge : TypeError',
     'input rend TOUJOURS du texte, même quand on tape un nombre. On ne peut pas ajouter 1 à du texte : il fallait int(age) d\'abord.'],

    ['age = int("12")\nprint(age + 1)\n\nQu\'est-ce qui s\'affiche ?',
     ['121', '13', 'une erreur rouge', '"13"'], '13',
     'int() a transformé le texte 12 en nombre 12. Avec un nombre, on peut calculer : 12 + 1 = 13.'],

    ['tour = 0\ntour = tour + 1\ntour = tour + 1\ntour = tour + 1\nprint(tour)\n\nQu\'est-ce qui s\'affiche ?',
     ['0', '1', '111', '3'], '3',
     'La même ligne, trois fois : chaque fois elle prend ce qu\'il y a dans tour et y remet un de plus. 0, puis 1, puis 2, puis 3.'],

    ['print(10 >= 10)\n\nQu\'est-ce qui s\'affiche ?',
     ['True', 'False', '10', 'une erreur rouge'], 'True',
     'L\'opérateur >= veut dire « plus grand OU ÉGAL ». 10 n\'est pas plus grand que 10, mais il est égal : la réponse est True.'],

    ['x = 4\nprint(x == 4)\n\nQu\'est-ce qui s\'affiche ?',
     ['4', 'True', 'False', 'x == 4'], 'True',
     'L\'opérateur == pose une QUESTION : est-ce que x vaut 4 ? Oui : True. Un seul = aurait été un ordre.'],

    ['age = 20\n\nif age > 17:\n    print("Jeremiah")\nelse:\n    print("Jerusalem")\n\nQu\'est-ce qui s\'affiche ?',
     ['Jerusalem', 'Jeremiah puis Jerusalem', 'rien', 'Jeremiah'], 'Jeremiah',
     '20 est plus grand que 17 : il prend le premier chemin, et il ne fait PAS le else. Un seul des deux chemins est pris, jamais les deux.'],

    ['age = 20\n\nif age = 17:\n    print("Bravo")\n\nQue se passe-t-il ?',
     ['Une erreur rouge : SyntaxError', 'Ça affiche Bravo', 'Ça n\'affiche rien', 'Ça affiche 17'],
     'Une erreur rouge : SyntaxError',
     'Un seul = , c\'est « range dans » : un ORDRE. Pour poser une question dans un if, il faut l\'opérateur == .'],

    ['age = 20\n\nif age > 17:\nprint("Bravo")\n\nQue se passe-t-il ?',
     ['Ça affiche Bravo', 'Ça n\'affiche rien', 'Une erreur rouge : IndentationError', 'Une erreur rouge : NameError'],
     'Une erreur rouge : IndentationError',
     'Après les deux-points, il faut DÉCALER de 4 espaces. Sans le décalage, Python ne sait pas ce qui appartient au if.'],

    ['nombre = 5\n\nif nombre > 3:\n    print("grand")\nprint("fini")\n\nQu\'est-ce qui s\'affiche ?',
     ['grand', 'grand puis fini', 'fini', 'rien'], 'grand puis fini',
     'print("fini") n\'est PAS décalé : il n\'appartient pas au if. Il s\'affiche donc dans tous les cas.'],

    ['tour = 0\ncase = 12\n\nif case > 9:\n    print("La case n\'existe pas !")\nelse:\n    tour = tour + 1\n\nprint(tour)\n\nQu\'est-ce qui s\'affiche à la fin ?',
     ['1', '12', '9', '0'], '0',
     'La case 12 est refusée : c\'est le premier chemin qui est pris. La ligne tour = tour + 1 est dans le else, elle n\'a pas été exécutée.'],

    ['tour = 3\nprint("Tour " + tour)\n\nQue se passe-t-il ?',
     ['Ça affiche Tour 3', 'Ça affiche Tour tour', 'Une erreur rouge : TypeError', 'Ça affiche 3'],
     'Une erreur rouge : TypeError',
     'tour contient un NOMBRE, et on essaie de le coller à du texte avec le +. Il fallait écrire str(tour).']
  ];

  reflexion.forEach(function (q) {
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

  // ============================================================ PARTIE B
  form.addSectionHeaderItem()
      .setTitle('PARTIE B — Écris le code')
      .setHelpText('Tape ta réponse comme tu l\'écrirais dans Thonny. '
                 + 'Utilise des guillemets doubles " et respecte les majuscules et les minuscules. '
                 + 'Quand il faut décaler une ligne, décale-la de 4 espaces. '
                 + 'Ton code ne sera pas exécuté : c\'est ta façon de l\'écrire qui compte.');

  var exercices = [

    ['Complète pour transformer la réponse du joueur en NOMBRE :\n\ncase = ______(case)\n\nÉcris seulement le mot qui manque.',
     'Un seul mot, en minuscules.',
     'int'],

    ['Complète pour pouvoir coller le nombre au texte :\n\nprint("Tour " + ______(tour))\n\nÉcris seulement le mot qui manque.',
     'Un seul mot, en minuscules.',
     'str'],

    ['Écris la ligne qui ajoute 1 au compteur appelé  tour',
     'Une seule ligne. Souviens-toi : le = veut dire « range dans ».',
     'tour = tour + 1'],

    ['Écris la comparaison qui demande :  est-ce que  case  est plus grand que 9 ?',
     'Seulement la comparaison, avec le bon opérateur. Sans print et sans if.',
     'case > 9'],

    ['Cette ligne est cassée :\n\nif age = 17:\n\nRécris-la correctement.',
     'Une seule ligne, les deux-points compris.',
     'if age == 17:'],

    ['Cette ligne est cassée :\n\nif case > 9\n    print("Trop grand !")\n\nRécris la PREMIÈRE ligne correctement.',
     'Une seule ligne. Regarde bien la fin.',
     'if case > 9:'],

    ['Ce programme est cassé :\n\nif age > 17:\nprint("Jeremiah")\n\nRécris les DEUX lignes correctement.',
     'Deux lignes, l\'une sous l\'autre. Pense au décalage de 4 espaces.',
     'if age > 17:\n    print("Jeremiah")'],

    ['Écris le if / else complet :\n\n1) si  case  est plus grand que 9, afficher  Impossible\n2) sinon, afficher  Case acceptee',
     'Quatre lignes. Pense aux deux-points et au décalage de 4 espaces.',
     'if case > 9:\n    print("Impossible")\nelse:\n    print("Case acceptee")']
  ];

  exercices.forEach(function (e) {
    var item = (e[2].indexOf('\n') >= 0) ? form.addParagraphTextItem() : form.addTextItem();
    item.setTitle(e[0]);
    item.setHelpText(e[1]);
    item.setPoints(1);
    item.setRequired(true);
    try {
      item.setGeneralFeedback(
          FormApp.createFeedback().setText('La réponse attendue :\n' + e[2]).build());
    } catch (err) {
      Logger.log('Retour général impossible sur : ' + e[0].substring(0, 40));
    }
  });

  try { form.setPublished(true); } catch (e) {
    Logger.log('À faire à la main : ouvrez le formulaire et cliquez sur « Publier ».');
  }

  Logger.log('=======================================================');
  Logger.log('LIEN À ENVOYER AUX PARENTS :');
  Logger.log(form.getPublishedUrl());
  Logger.log('');
  Logger.log('LIEN POUR MODIFIER LE FORMULAIRE :');
  Logger.log(form.getEditUrl());
  Logger.log('=======================================================');
  Logger.log('12 questions de réflexion + 8 exercices de code = 20 points.');
  Logger.log('Pensez à coller les corrigés des 8 exercices : voir formulaire-exercices.md');
}
