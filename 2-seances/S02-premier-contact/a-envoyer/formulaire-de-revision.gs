/**
 * =====================================================================
 *  AcProKids Coding Camp — Révision de la séance 2
 *  Crée un formulaire Google NOTÉ, prêt à envoyer aux parents.
 * =====================================================================
 *
 *  MODE D'EMPLOI (5 minutes, une seule fois) :
 *
 *   1. Allez sur  script.google.com  et cliquez sur « Nouveau projet ».
 *   2. Effacez le petit bout de code qui s'y trouve.
 *   3. Collez TOUT ce fichier à la place.
 *   4. Cliquez sur « Exécuter » (le bouton ▶).
 *      Google demande une autorisation la première fois : acceptez.
 *   5. En bas, dans le journal d'exécution, vous verrez DEUX liens :
 *         - le lien À ENVOYER aux parents
 *         - le lien pour modifier le formulaire vous-même
 *
 *  Chaque question vaut 1 point. Le score s'affiche à l'élève dès qu'il
 *  a envoyé ses réponses, avec l'explication de ce qu'il a raté.
 * =====================================================================
 */

function creerLeFormulaire() {

  var form = FormApp.create('Révision — séance 2 : mon premier programme');

  form.setDescription(
      'AcProKids Coding Camp — Jerusalem Geeks & Jeremiah Geeks\n\n' +
      'Douze questions sur ce qu\'on a fait samedi : afficher un message, ' +
      'la boîte à étiquette, et le jeu qui demande ton nom.\n\n' +
      'Aucun ordinateur n\'est nécessaire, cela prend dix minutes. ' +
      'Tu as ta note tout de suite à la fin — et l\'explication de ce que tu n\'as pas trouvé. ' +
      'Ce n\'est pas grave de se tromper : c\'est comme ça qu\'on apprend.');

  form.setIsQuiz(true);
  form.setShowLinkToRespondAgain(false);
  form.setConfirmationMessage(
      'Merci, c\'est envoyé ! Clique sur « Afficher le score » pour voir ta note ' +
      'et les explications. À samedi, 12 h !');

  // ------------------------------------------------ qui répond ?
  form.addTextItem()
      .setTitle('Ton prénom et ton nom')
      .setRequired(true);

  form.addMultipleChoiceItem()
      .setTitle('Ta classe')
      .setChoiceValues(['Jerusalem Geeks (9 – 12 ans)', 'Jeremiah Geeks (12 – 18 ans)'])
      .setRequired(true);

  // ------------------------------------------------ les 12 questions notées
  var questions = [

    ['Que fait la commande  print  ?',
     ['Elle affiche du texte à l\'écran',
      'Elle imprime sur du papier',
      'Elle efface le programme',
      'Elle calcule'],
     'Elle affiche du texte à l\'écran',
     'print veut dire AFFICHE. Attention au piège : ça n\'imprime rien sur du papier !'],

    ['Combien faut-il de guillemets autour d\'un texte ?',
     ['Un seul', 'Deux : un avant, un après', 'Trois', 'Aucun'],
     'Deux : un avant, un après',
     'Les guillemets vont par deux, comme une paire de chaussures. Jamais un tout seul.'],

    ['Dans Thonny, où écrit-on son programme ?',
     ['Dans la zone blanche, en haut',
      'Dans la zone grise, en bas',
      'N\'importe où',
      'Sur le bureau'],
     'Dans la zone blanche, en haut',
     'On écrit en haut, dans la zone blanche. La zone grise du bas, c\'est là que l\'ordinateur RÉPOND.'],

    ['Comment lance-t-on son programme ?',
     ['En appuyant sur F5, ou sur le bouton vert',
      'En fermant la fenêtre',
      'En appuyant sur Entrée',
      'Il se lance tout seul'],
     'En appuyant sur F5, ou sur le bouton vert',
     'F5, ou le bouton vert : c\'est le « vas-y ». Rien ne se passe tant qu\'on n\'appuie pas dessus.'],

    ['L\'ordinateur lit ton programme…',
     ['De haut en bas, ligne par ligne',
      'De bas en haut',
      'Dans le désordre',
      'En commençant par le milieu'],
     'De haut en bas, ligne par ligne',
     'De haut en bas, ligne par ligne, toujours. Si ça s\'affiche dans le désordre, c\'est l\'ordre de tes lignes.'],

    ['Tu écris  print("Bonjour)  et l\'écran devient rouge. Pourquoi ?',
     ['Il manque un guillemet',
      'L\'ordinateur est cassé',
      'Il manque un point',
      'print s\'écrit avec une majuscule'],
     'Il manque un guillemet',
     'Il en faut deux : un avant le texte, un après. L\'ordinateur affiche SyntaxError : il n\'a pas compris ta phrase.'],

    ['Quand l\'écran devient rouge, cela veut dire…',
     ['Il t\'explique ce qu\'il n\'a pas compris',
      'Tu es puni',
      'L\'ordinateur est en colère',
      'Il faut tout effacer'],
     'Il t\'explique ce qu\'il n\'a pas compris',
     'Le rouge n\'est pas une punition : LE ROUGE EST UNE INFORMATION. Il te dit même sur quelle ligne chercher.'],

    ['Tu écris ces deux lignes :\n\nnom = "Damien"\nprint(nom)\n\nQu\'est-ce qui s\'affiche ?',
     ['Damien', 'nom', '"Damien"', 'Rien'],
     'Damien',
     'Sans guillemets, l\'ordinateur affiche CE QU\'IL Y A DANS LA BOÎTE. La boîte s\'appelle nom, et dedans il y a Damien.'],

    ['Et maintenant :\n\nnom = "Damien"\nprint("nom")\n\nQu\'est-ce qui s\'affiche ?',
     ['nom', 'Damien', 'Rien', 'Une erreur rouge'],
     'nom',
     'Avec des guillemets, il affiche le MOT écrit entre les guillemets. C\'est toute la différence — et c\'est l\'erreur numéro un de l\'année !'],

    ['À quoi sert  input()  ?',
     ['Le programme pose une question et attend la réponse du joueur',
      'Il affiche un texte',
      'Il efface l\'écran',
      'Il compte jusqu\'à dix'],
     'Le programme pose une question et attend la réponse du joueur',
     'input veut dire DEMANDE : le programme s\'arrête, il attend, et il range la réponse dans la boîte.'],

    ['Ton programme est :\n\nnom = input("Ton prénom ? ")\nprint("Bonjour " + nom + " !")\n\nLe joueur tape  Joyce.  Qu\'est-ce qui s\'affiche ?',
     ['Bonjour Joyce !', 'Bonjour nom !', 'Joyce', 'Bonjour + Joyce !'],
     'Bonjour Joyce !',
     'Ce que le joueur tape est rangé dans la boîte nom, et le + colle les morceaux bout à bout.'],

    ['Dans  print("Bonjour " + nom),  à quoi sert le  +  ?',
     ['Il colle les morceaux bout à bout',
      'Il fait une addition',
      'Il sépare deux lignes',
      'Il ne sert à rien'],
     'Il colle les morceaux bout à bout',
     'Il colle. Et attention à l\'espace après Bonjour : sans lui, ça donne BonjourJoyce !']
  ];

  questions.forEach(function (q) {
    var item = form.addMultipleChoiceItem();
    item.setTitle(q[0]);
    item.setPoints(1);
    item.setRequired(true);
    item.setChoices(q[1].map(function (texte) {
      return item.createChoice(texte, texte === q[2]);
    }));
    item.setFeedbackForCorrect(
        FormApp.createFeedback().setText('Bravo, c\'est exactement ça !').build());
    item.setFeedbackForIncorrect(
        FormApp.createFeedback().setText(q[3]).build());
  });

  // ------------------------------------------------ une question libre, non notée
  form.addParagraphTextItem()
      .setTitle('Y a-t-il quelque chose que tu n\'as pas bien compris samedi ?')
      .setHelpText('Facultatif. Ta réponse n\'est pas notée — elle sert au professeur '
                 + 'à savoir par quoi commencer samedi prochain.')
      .setRequired(false);

  // ------------------------------------------------ publication (Google l'exige depuis 2025)
  try {
    form.setPublished(true);
  } catch (e) {
    Logger.log('À faire à la main : ouvrez le formulaire et cliquez sur « Publier ».');
  }

  Logger.log('=======================================================');
  Logger.log('LIEN À ENVOYER AUX PARENTS :');
  Logger.log(form.getPublishedUrl());
  Logger.log('');
  Logger.log('LIEN POUR MODIFIER LE FORMULAIRE :');
  Logger.log(form.getEditUrl());
  Logger.log('=======================================================');
  Logger.log('12 questions notées sur 12 points. Le score s\'affiche à l\'élève');
  Logger.log('dès qu\'il envoie ses réponses.');
}
