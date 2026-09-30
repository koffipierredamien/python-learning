/**
 * =====================================================================
 *  AcProKids Coding Camp — Test de révision n°2  (après le TP)
 *  Formulaire Google NOTÉ, en deux parties :
 *     A. « Que va afficher ce programme ? »  — corrigé automatiquement
 *     B. « Écris le code »                   — l'élève tape du code
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

  var form = FormApp.create('Test n°2 — variables, input et affichage');

  form.setDescription(
      'AcProKids Coding Camp — Jerusalem Geeks & Jeremiah Geeks\n\n' +
      'Ce test reprend tout ce qu\'on a fait depuis le début : afficher, les boîtes ' +
      '(les variables), les questions au joueur, et les erreurs.\n\n' +
      'Il y a deux parties :\n' +
      '  A. Que va afficher ce programme ? — tu lis le code dans ta tête\n' +
      '  B. Écris le code — tu tapes toi-même la bonne ligne\n\n' +
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
                 + 'Souviens-toi : une boîte ne garde qu\'une seule chose à la fois.');

  var reflexion = [

    ['a = 3\na = 5\nprint(a)\n\nQu\'est-ce qui s\'affiche ?',
     ['3', '5', '3 puis 5', 'a'], '5',
     'La deuxième ligne remplace le contenu de la boîte. Quand on arrive au print, il n\'y a plus que 5 dedans.'],

    ['a = 4\nb = 5\nb = a\nprint(b)\n\nQu\'est-ce qui s\'affiche ?',
     ['4', '5', '9', 'b'], '4',
     'b = a met DANS b ce qu\'il y a dans a. Donc b contient 4. Le 5 est perdu.'],

    ['a = 4\nb = 5\nb = a\nprint(a)\n\nQu\'est-ce qui s\'affiche ?',
     ['5', '9', '4', 'rien'], '4',
     'a n\'a jamais changé : il contient toujours 4. Copier une boîte dans une autre ne vide pas la première.'],

    ['a = "X"\nb = "O"\na = b\nb = a\nprint(a)\nprint(b)\n\nQu\'est-ce qui s\'affiche ?',
     ['O puis X', 'X puis O', 'X puis X', 'O puis O'], 'O puis O',
     'Le piège ! Dès la ligne a = b, le X est perdu pour toujours. Pour échanger deux boîtes, il en faut une troisième.'],

    ['nom = "Joyce"\nprint("nom")\n\nQu\'est-ce qui s\'affiche ?',
     ['nom', 'Joyce', '"Joyce"', 'une erreur rouge'], 'nom',
     'Avec des guillemets, il affiche le MOT. Sans guillemets, il affiche ce qu\'il y a dans la boîte.'],

    ['x = "3"\ny = "4"\nprint(x + y)\n\nQu\'est-ce qui s\'affiche ?',
     ['7', '34', '3 + 4', '"34"'], '34',
     'Entre guillemets, 3 et 4 sont du TEXTE. Le + colle deux textes : ça donne 34, pas 7.'],

    ['nom = "Joyce"\nprint("Bonjour" + nom)\n\nQu\'est-ce qui s\'affiche ?',
     ['Bonjour Joyce', 'Bonjour + Joyce', 'Bonjour nom', 'BonjourJoyce'], 'BonjourJoyce',
     'Il colle EXACTEMENT ce qu\'on lui donne. Il manque l\'espace : il fallait écrire "Bonjour ".'],

    ['print("Un")\nprint("Deux")\nprint("Trois")\n\nDans quel ordre les mots s\'affichent-ils ?',
     ['Trois, Deux, Un', 'Dans le désordre', 'Un, Deux, Trois', 'Tout sur la même ligne'],
     'Un, Deux, Trois',
     'De haut en bas, ligne par ligne, toujours. Il ne saute jamais et ne revient jamais en arrière.'],

    ['prenom = input("Ton prenom ? ")\nprint("Salut " + prenom)\n\nLe joueur tape  Gedeon.  Qu\'est-ce qui s\'affiche ?',
     ['Salut prenom', 'Salut Gedeon', 'Gedeon', 'Salut input'], 'Salut Gedeon',
     'Ce que le joueur tape est rangé dans la boîte prenom, et le + le colle après Salut.'],

    ['age = "15"\nage = "16"\nage = "17"\nprint(age)\n\nQu\'est-ce qui s\'affiche ?',
     ['15', '151617', '15 16 17', '17'], '17',
     'Chaque ligne écrase la précédente. Il ne reste que la dernière valeur rangée.'],

    ['nom = input("Ton nom ? ")\nprint("Bonjour " + Nom)\n\nQue se passe-t-il ?',
     ['Ça affiche Bonjour', 'Ça affiche le nom', 'Une erreur rouge : NameError', 'Ça n\'affiche rien'],
     'Une erreur rouge : NameError',
     'La boîte s\'appelle nom, on l\'appelle Nom. Pour Python, ce ne sont pas les mêmes : il ne connaît pas Nom.'],

    ['print("Bonjour)\n\nQue se passe-t-il ?',
     ['Une erreur rouge : SyntaxError', 'Ça affiche Bonjour', 'Ça affiche "Bonjour', 'Ça n\'affiche rien'],
     'Une erreur rouge : SyntaxError',
     'Il manque le guillemet fermant. Les guillemets vont par deux, comme une paire de chaussures.']
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
                 + 'Ton code ne sera pas exécuté : c\'est ta façon de l\'écrire qui compte.');

  var exercices = [

    ['Écris la ligne qui affiche exactement :  Bonjour',
     'Une seule ligne. Réponse attendue de la forme : print("...")',
     'print("Bonjour")'],

    ['Complète cette ligne pour qu\'elle pose une question au joueur :\n\nprenom = ______("Ton prenom ? ")\n\nÉcris seulement le mot qui manque.',
     'Un seul mot, en minuscules.',
     'input'],

    ['Complète pour coller les deux morceaux :\n\nprint("Bonjour " __ prenom)\n\nÉcris seulement le signe qui manque.',
     'Un seul caractère.',
     '+'],

    ['Écris la ligne qui range le mot  Joyce  dans une boîte appelée  nom',
     'Une seule ligne, de la forme :  boite = "valeur"',
     'nom = "Joyce"'],

    ['Écris la ligne qui range  15  dans une boîte appelée  age,  en tant que TEXTE',
     'Une seule ligne. Attention aux guillemets.',
     'age = "15"'],

    ['Cette ligne est cassée :\n\nprint("Bonjour)\n\nRécris-la correctement.',
     'Une seule ligne.',
     'print("Bonjour")'],

    ['Cette ligne est cassée :\n\nPrint("Salut")\n\nRécris-la correctement.',
     'Une seule ligne. Regarde bien le premier mot.',
     'print("Salut")'],

    ['Écris les DEUX lignes qui demandent son nom au joueur, puis le saluent :\n\n1) ranger la réponse dans une boîte appelée  joueur\n2) afficher  Bonjour  suivi du nom du joueur',
     'Deux lignes, l\'une sous l\'autre. Appuie sur Entrée entre les deux.',
     'joueur = input("Ton nom ? ")\nprint("Bonjour " + joueur)']
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
