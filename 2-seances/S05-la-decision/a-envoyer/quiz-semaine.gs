/**
 * =====================================================================
 *  AcProKids Coding Camp — Quiz de la semaine n°4
 *  POUR LES ENFANTS QUI N'ONT PAS D'ORDINATEUR
 *  Ils font ce quiz À LA PLACE de l'exercice « Le Nombre Secret ».
 *
 *  15 questions, 15 points, TOUT EST CORRIGÉ AUTOMATIQUEMENT :
 *  aucune réponse libre, donc AUCUN corrigé à coller à la main.
 *
 *  Il porte sur exactement les mêmes notions que l'exercice de maison :
 *     int() et str()  ·  le compteur  ·  <  >  ==  ·  if / else
 *  et il raconte la même histoire : le jeu du Nombre Secret.
 * =====================================================================
 *
 *  MODE D'EMPLOI :
 *   1. script.google.com  →  Nouveau projet
 *   2. Effacez le code présent, collez TOUT ce fichier
 *   3. Bouton ▶ Exécuter  →  autorisez à la première utilisation
 *   4. Le journal affiche le lien à envoyer et le lien pour modifier
 *
 *  ⚠⚠ ETAPE 5, SANS LAQUELLE L'ELEVE NE VERRA AUCUNE CORRECTION :
 *     ouvrez le formulaire → roue dentée ⚙ Paramètres → Questionnaires :
 *        « Publier les notes »  →  IMMEDIATEMENT APRES CHAQUE ENVOI
 *        « Le participant peut voir »  →  cochez les TROIS cases :
 *               Questions manquées · Bonnes réponses · Valeurs des points
 *     Apps Script n'expose pas ces réglages : c'est quatre clics, une
 *     seule fois, et sans eux l'enfant ne voit ni note ni corrigé.
 *
 *  RECETTE : répondez vous-même au formulaire. Le bouton « Afficher le
 *  score » doit apparaître, avec votre note et les explications.
 * =====================================================================
 */

function creerLeQuiz() {

  var form = FormApp.create('Quiz de la semaine — Le Nombre Secret');

  form.setDescription(
      'AcProKids Coding Camp — Jeremiah Geeks\n\n' +
      'Ce quiz est pour toi si tu n\'as pas d\'ordinateur à la maison : tu le fais À LA PLACE ' +
      'de l\'exercice « Le Nombre Secret ». Tu peux répondre depuis un téléphone.\n\n' +
      'Les questions racontent le même jeu : un joueur cache un nombre, l\'autre a trois essais ' +
      'pour le trouver, et le programme répond « plus grand » ou « plus petit ».\n\n' +
      'GARDE CES TROIS RAPPELS SOUS LES YEUX :\n' +
      '    input() rend TOUJOURS du texte  →  int() pour comparer, str() pour écrire\n' +
      '    le compteur : points = points - 20  (on reprend ce qu\'il y a dedans, et on remet)\n' +
      '    le décalage de 4 espaces dit CE QUI EST DANS le if\n\n' +
      '15 questions, 15 points. Tu as ta note et les explications à la fin. ' +
      'Se tromper n\'est pas grave : c\'est comme ça qu\'on apprend.');

  form.setIsQuiz(true);
  form.setShowLinkToRespondAgain(false);
  form.setConfirmationMessage(
      'C\'est envoyé ! Clique sur « Afficher le score » pour voir ta note et les explications. ' +
      'À samedi, 12 h !');

  form.addTextItem().setTitle('Ton prénom et ton nom').setRequired(true);
  form.addMultipleChoiceItem()
      .setTitle('Ta classe')
      .setChoiceValues(['Jerusalem Geeks (9 – 12 ans)', 'Jeremiah Geeks (12 – 18 ans)'])
      .setRequired(true);

  // ========================================================= PARTIE A
  form.addSectionHeaderItem()
      .setTitle('PARTIE A — Texte ou nombre ?')
      .setHelpText('De chaque côté du + , demande-toi : du TEXTE (avec guillemets) ou un NOMBRE ?');

  var questions = [

    ['print("3" + "4")\n\nQu\'est-ce qui s\'affiche ?',
     ['34', '7', '"34"', 'une erreur rouge'], '34',
     'Texte + texte : les deux sont collés l\'un à l\'autre.'],

    ['essai = input("Ton nombre : ")\nprint(essai + 1)\n\nLe joueur tape 10. Que se passe-t-il ?',
     ['Ça affiche 11', 'Ça affiche 101', 'Une erreur rouge : TypeError', 'Ça affiche 10'],
     'Une erreur rouge : TypeError',
     'input rend TOUJOURS du texte. Texte + nombre : TypeError. Il manquait la ligne int().'],

    ['essai = input("Ton nombre : ")\nessai = int(essai)\nprint(essai + 1)\n\nLe joueur tape 10. Qu\'est-ce qui s\'affiche ?',
     ['101', '11', '10', 'une erreur rouge'], '11',
     'La ligne int() a transformé le texte en nombre. 10 + 1 = 11.'],

    ['points = 60\nprint("Ton score : " + points)\n\nQue se passe-t-il ?',
     ['Ça affiche Ton score : 60', 'Ça affiche Ton score : points', 'Ça affiche 60', 'Une erreur rouge : TypeError'],
     'Une erreur rouge : TypeError',
     'points contient un NOMBRE, et on le colle à du texte. Il fallait écrire str(points).'],

    // ======================================================= PARTIE B
    ['points = 100\npoints = points - 20\npoints = points - 20\nprint(points)\n\nQu\'est-ce qui s\'affiche ?',
     ['60', '100', '80', '20'], '60',
     'Chaque ligne reprend ce qu\'il y a dans points et enlève 20 : 100, puis 80, puis 60.'],

    ['Quelle ligne ajoute 1 au compteur  tour  ?',
     ['tour + 1', 'tour = tour + 1', 'tour = 1', 'tour == tour + 1'], 'tour = tour + 1',
     'On reprend ce qu\'il y a dans la boîte, on ajoute 1, et on remet le tout dans la même boîte.'],

    ['Où faut-il écrire la ligne  points = 100  ?',
     ['À chaque essai', 'À la fin, dans le verdict', 'Juste après chaque if', 'Au début, une seule fois, avant les essais'], 'Au début, une seule fois, avant les essais',
     'Si on la répète, le score repart à 100 à chaque essai : le joueur ne perd jamais rien.'],

    // ======================================================= PARTIE C
    ['print(7 > 10)\n\nQu\'est-ce qui s\'affiche ?',
     ['True', '7', 'False', 'une erreur rouge'], 'False',
     '7 n\'est pas plus grand que 10. Une comparaison donne toujours True ou False, jamais un nombre.'],

    ['secret = 23\nessai = 40\n\nif essai < secret:\n    print("C\'est PLUS GRAND !")\nif essai > secret:\n    print("C\'est PLUS PETIT !")\nif essai == secret:\n    print("GAGNE !")\n\nQu\'est-ce qui s\'affiche ?',
     ['C\'est PLUS PETIT !', 'C\'est PLUS GRAND !', 'GAGNE !', 'Rien du tout'], 'C\'est PLUS PETIT !',
     '40 est plus grand que 23 : c\'est le deuxième if qui est vrai. Les deux autres sont faux.'],

    ['Dans le même programme, le joueur tape 23. Qu\'est-ce qui s\'affiche ?',
     ['C\'est PLUS GRAND !', 'Les trois messages', 'C\'est PLUS PETIT !', 'GAGNE !'], 'GAGNE !',
     'Un seul des trois if peut être vrai à la fois. Ici, c\'est celui du == .'],

    ['secret = 23\n\nif essai = secret:\n    print("GAGNE !")\n\nQue se passe-t-il ?',
     ['Ça affiche GAGNE !', 'Une erreur rouge : SyntaxError', 'Ça n\'affiche rien', 'Ça affiche 23'],
     'Une erreur rouge : SyntaxError',
     'Un seul = , c\'est « range dans » : un ORDRE. Pour poser une question, il faut == .'],

    // ======================================================= PARTIE D
    ['if essai > secret:\nprint("C\'est PLUS PETIT !")\n\nQue se passe-t-il ?',
     ['Ça marche', 'Une erreur rouge : NameError', 'Une erreur rouge : IndentationError', 'Ça n\'affiche jamais rien'], 'Une erreur rouge : IndentationError',
     'Après les deux-points, il faut décaler de 4 espaces. Sans le décalage, Python ne sait pas ce qui appartient au if.'],

    ['points = 100\n\nif essai == secret:\n    print("GAGNE !")\npoints = points - 20\n\nLe joueur GAGNE. Que vaut points à la fin ?',
     ['80', '100', '0', 'On ne peut pas savoir'], '80',
     'LE BUG DU JEU : la ligne points = points - 20 n\'est PAS décalée, donc elle n\'est pas dans le if. Elle s\'exécute toujours — même quand on gagne.'],

    ['nombre = 5\n\nif nombre > 3:\n    print("grand")\nprint("fini")\n\nQu\'est-ce qui s\'affiche ?',
     ['grand', 'fini', 'rien', 'grand puis fini'], 'grand puis fini',
     'print("fini") n\'est pas décalé : il n\'appartient pas au if, donc il s\'affiche dans tous les cas.'],

    ['points = 40\n\nif points > 50:\n    print("CHAMPION !")\nelse:\n    print("Perdu...")\n\nQu\'est-ce qui s\'affiche ?',
     ['CHAMPION !', 'Perdu...', 'Les deux', 'rien'], 'Perdu...',
     '40 n\'est pas plus grand que 50 : c\'est le chemin du else qui est pris. Un seul des deux, jamais les deux.']
  ];

  questions.forEach(function (q, i) {
    if (i === 4) {
      form.addSectionHeaderItem().setTitle('PARTIE B — Le compteur')
          .setHelpText('Le compteur reprend ce qu\'il y a dans la boîte, le change, et le remet dedans.');
    }
    if (i === 7) {
      form.addSectionHeaderItem().setTitle('PARTIE C — Comparer, et décider')
          .setHelpText('Une comparaison répond True ou False. Le if choisit quoi faire ensuite.');
    }
    if (i === 11) {
      form.addSectionHeaderItem().setTitle('PARTIE D — Le décalage de 4 espaces')
          .setHelpText('C\'est lui qui dit CE QUI EST DANS le if. C\'est l\'erreur n°1 de toute la classe.');
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
    Logger.log('À faire à la main : ouvrez le formulaire et cliquez sur « Publier ».');
  }

  Logger.log('#######################################################');
  Logger.log('##  A FAIRE MAINTENANT, SINON L\'ELEVE NE VERRA RIEN  ##');
  Logger.log('#######################################################');
  Logger.log('1. Ouvrez le formulaire (lien de modification ci-dessous)');
  Logger.log('2. Roue dentee ⚙ Parametres  >  Questionnaires');
  Logger.log('3. « Publier les notes »  ->  Immediatement apres chaque envoi');
  Logger.log('4. « Le participant peut voir »  ->  cochez les TROIS cases');
  Logger.log('5. RECETTE : repondez vous-meme. Le bouton « Afficher le score »');
  Logger.log('      doit apparaitre, avec la note et les corriges.');
  Logger.log('');
  Logger.log('BONNE NOUVELLE : il n\'y a AUCUN corrige a coller a la main,');
  Logger.log('les 15 questions sont a choix multiples.');
  Logger.log('');
  Logger.log('=======================================================');
  Logger.log('LIEN À ENVOYER AUX PARENTS :');
  Logger.log(form.getPublishedUrl());
  Logger.log('');
  Logger.log('LIEN POUR MODIFIER LE FORMULAIRE :');
  Logger.log(form.getEditUrl());
  Logger.log('=======================================================');
  Logger.log('15 questions a choix multiples = 15 points, 100 % automatique.');
}
