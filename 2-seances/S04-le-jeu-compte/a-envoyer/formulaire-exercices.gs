/**
 * =====================================================================
 *  AcProKids Coding Camp — Test de révision n°3
 *  TEXTE OU NOMBRE  (int et str)  —  Jeremiah Geeks
 *
 *  Formulaire Google NOTÉ, en deux parties :
 *     A. « Que va afficher ce programme ? »  — corrigé automatiquement
 *     B. « Écris le code »                   — l'élève tape du code
 *
 *  Il ne porte QUE sur la première notion de la séance 4 : le texte et
 *  les nombres. Le compteur et le if / else n'y sont pas : ils n'ont
 *  pas encore été vus.
 *
 *  Il s'appuie sur le tableau donné en classe :
 *      str + str  ->  concatenation
 *      str + int  ->  TypeError
 *      int + str  ->  TypeError
 *      int + int  ->  addition
 * =====================================================================
 *
 *  MODE D'EMPLOI :
 *   1. script.google.com  →  Nouveau projet
 *   2. Effacez le code présent, collez TOUT ce fichier
 *   3. Bouton ▶ Exécuter  →  autorisez à la première utilisation
 *   4. Le journal affiche le lien à envoyer et le lien pour modifier
 *
 *  ⚠⚠ ETAPE 5, SANS LAQUELLE L'ELEVE NE VERRA AUCUNE CORRECTION :
 *     ouvrez le formulaire → roue dentée ⚙ Paramètres → Questionnaires,
 *     et réglez à la main :
 *        « Publier les notes »  →  IMMEDIATEMENT APRES CHAQUE ENVOI
 *        « Le participant peut voir »  →  cochez les TROIS cases :
 *               Questions manquées · Bonnes réponses · Valeurs des points
 *     Tant que c'est sur « Plus tard, après examen manuel », l'élève ne
 *     voit que « Votre réponse a été enregistrée », sans note ni corrigé.
 *     Apps Script n'expose pas ce réglage : il ne peut pas être fait par
 *     le script, c'est quatre clics et c'est définitif pour ce formulaire.
 *
 *  ⚠ ET LA DEUXIEME CHOSE À FAIRE À LA MAIN (4 minutes) :
 *     les 8 questions « Écris le code » sont des réponses libres. Google
 *     ne permet pas de fixer leur corrigé depuis un script — il faut
 *     l'ajouter dans le formulaire : sur chaque question, « Corrigé » →
 *     « Ajouter une réponse correcte ». Les réponses à coller sont dans
 *     le fichier  formulaire-exercices.md,  déjà écrites, variantes
 *     comprises. Sans cela, ces 8 questions se corrigent à la main.
 * =====================================================================
 */

function creerLeTest() {

  var form = FormApp.create('Test n°3 — texte ou nombre');

  form.setDescription(
      'AcProKids Coding Camp — Jeremiah Geeks\n\n' +
      'Ce test porte sur UNE SEULE chose, celle de samedi : savoir si on a du TEXTE ' +
      'ou un NOMBRE entre les mains, et passer de l\'un à l\'autre avec int() et str().\n\n' +
      'GARDE CE TABLEAU SOUS LES YEUX — c\'est celui de la classe :\n' +
      '    texte  +  texte   →  les deux sont collés  ("3" + "4" donne 34)\n' +
      '    texte  +  nombre  →  TypeError\n' +
      '    nombre +  texte   →  TypeError\n' +
      '    nombre +  nombre  →  une addition      (3 + 4 donne 7)\n\n' +
      'Et la règle à ne jamais oublier : input() rend TOUJOURS du texte.\n\n' +
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
      .setHelpText('Pour chaque programme, demande-toi d\'abord : de chaque côté du + , '
                 + 'est-ce que c\'est du TEXTE (avec des guillemets) ou un NOMBRE (sans guillemets) ? '
                 + 'Ensuite, regarde ton tableau.');

  var reflexion = [

    ['print("3" + "4")\n\nQu\'est-ce qui s\'affiche ?',
     ['34', '7', '"34"', 'une erreur rouge'], '34',
     'Texte + texte : les deux sont collés l\'un à l\'autre. "3" et "4" sont entre guillemets, donc ce sont des textes.'],

    ['print(3 + 4)\n\nQu\'est-ce qui s\'affiche ?',
     ['34', '7', '3 + 4', 'une erreur rouge'], '7',
     'Nombre + nombre : c\'est une addition. Pas de guillemets, donc ce sont bien des nombres.'],

    ['print("3" + 4)\n\nQue se passe-t-il ?',
     ['Ça affiche 34', 'Ça affiche 7', 'Une erreur rouge : TypeError', 'Ça affiche "34"'],
     'Une erreur rouge : TypeError',
     'Texte + nombre : TypeError. Python ne sait pas s\'il doit coller ou additionner, alors il refuse.'],

    ['print(3 + "4")\n\nQue se passe-t-il ?',
     ['Ça affiche 7', 'Ça affiche 34', 'Ça n\'affiche rien', 'Une erreur rouge : TypeError'],
     'Une erreur rouge : TypeError',
     'Nombre + texte : TypeError aussi. L\'ordre ne change rien, c\'est le mélange qui ne passe pas.'],

    ['print(int("3") + 4)\n\nQu\'est-ce qui s\'affiche ?',
     ['7', '34', 'une erreur rouge', '"7"'], '7',
     'int("3") transforme le texte 3 en nombre 3. On a donc nombre + nombre : une addition.'],

    ['print("3" + str(4))\n\nQu\'est-ce qui s\'affiche ?',
     ['une erreur rouge', '34', '7', '3 4'], '34',
     'str(4) transforme le nombre 4 en texte. On a donc texte + texte : les deux sont collés.'],

    ['age = input("Ton age ? ")\nprint(age + 1)\n\nLe joueur tape  12.  Que se passe-t-il ?',
     ['Ça affiche 13', 'Ça affiche 121', 'Ça affiche 12', 'Une erreur rouge : TypeError'],
     'Une erreur rouge : TypeError',
     'input rend TOUJOURS du texte, même quand le joueur tape un nombre. On a donc texte + nombre : TypeError.'],

    ['age = input("Ton age ? ")\nage = int(age)\nprint(age + 1)\n\nLe joueur tape  12.  Qu\'est-ce qui s\'affiche ?',
     ['13', '121', 'une erreur rouge', '12'], '13',
     'La ligne int() a transformé le texte en nombre. Maintenant, nombre + nombre : 12 + 1 = 13.'],

    ['tour = 3\nprint("Tour " + tour)\n\nQue se passe-t-il ?',
     ['Ça affiche Tour 3', 'Ça affiche Tour tour', 'Une erreur rouge : TypeError', 'Ça affiche 3'],
     'Une erreur rouge : TypeError',
     'tour contient un NOMBRE, et "Tour " est du texte. Texte + nombre : TypeError. Il fallait écrire str(tour).'],

    ['print("Total : " + str(5 + 3))\n\nQu\'est-ce qui s\'affiche ?',
     ['Total : 53', 'Total : 8', 'une erreur rouge', 'Total : 5 + 3'], 'Total : 8',
     'D\'abord 5 + 3 fait 8, parce que ce sont deux nombres. Puis str(8) en fait du texte, qu\'on peut coller.'],

    ['age = int("douze")\n\nQue se passe-t-il ?',
     ['age contient 12', 'age contient douze', 'Il ne se passe rien', 'Une erreur rouge : ValueError'],
     'Une erreur rouge : ValueError',
     'int() ne marche que si le texte est VRAIMENT un nombre. Avec le mot douze, Python ne sait pas faire.'],

    ['nombre = "10"\nnombre = int(nombre)\nprint(nombre + nombre)\n\nQu\'est-ce qui s\'affiche ?',
     ['1010', 'une erreur rouge', '20', '"20"'], '20',
     'Sans la ligne int(), on aurait eu 1010 (deux textes collés). Avec elle, ce sont deux nombres : 10 + 10 = 20.']
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

    ['Complète pour transformer la réponse du joueur en NOMBRE :\n\nage = ______(age)\n\nÉcris seulement le mot qui manque.',
     'Un seul mot, en minuscules.',
     'int'],

    ['Complète pour pouvoir coller le nombre au texte :\n\nprint("J\'ai " + ______(age) + " ans")\n\nÉcris seulement le mot qui manque.',
     'Un seul mot, en minuscules.',
     'str'],

    ['Cette ligne est cassée :\n\nprint("Tour " + 3)\n\nRécris-la correctement, pour qu\'elle affiche  Tour 3',
     'Une seule ligne.',
     'print("Tour " + str(3))'],

    ['Cette ligne est cassée :\n\nprint("J\'ai " + 15 + " ans")\n\nRécris-la correctement.',
     'Une seule ligne. Attention : il y a UN SEUL nombre à transformer.',
     'print("J\'ai " + str(15) + " ans")'],

    ['Écris la ligne qui range le nombre  7  dans une boîte appelée  tour\n\n(le NOMBRE 7, pas le texte)',
     'Une seule ligne. Pas de guillemets.',
     'tour = 7'],

    ['Ce programme plante. Récris-le EN ENTIER pour qu\'il marche :\n\nage = input("Ton age ? ")\nprint(age + 10)',
     'Trois lignes. Il manque une ligne au milieu.',
     'age = input("Ton age ? ")\nage = int(age)\nprint(age + 10)'],

    ['Deux boîtes contiennent des NOMBRES :\n\na = 4\nb = 5\n\nÉcris la ligne qui affiche leur somme (donc 9).',
     'Une seule ligne, sans guillemets.',
     'print(a + b)'],

    ['Écris le programme qui demande son âge au joueur, puis affiche :\n\nDans 10 ans tu auras 25 ans\n\n(si le joueur a tapé 15)',
     'Trois lignes : la question, la transformation en nombre, et l\'affichage.',
     'age = input("Ton age ? ")\nage = int(age)\nprint("Dans 10 ans tu auras " + str(age + 10) + " ans")']
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

  Logger.log('#######################################################');
  Logger.log('##  A FAIRE MAINTENANT, SINON L\'ELEVE NE VERRA RIEN  ##');
  Logger.log('#######################################################');
  Logger.log('1. Ouvrez le formulaire (lien de modification ci-dessous)');
  Logger.log('2. Roue dentee ⚙ Parametres  >  Questionnaires');
  Logger.log('3. « Publier les notes »  ->  Immediatement apres chaque envoi');
  Logger.log('4. « Le participant peut voir »  ->  cochez les TROIS cases :');
  Logger.log('      Questions manquees · Bonnes reponses · Valeurs des points');
  Logger.log('5. Collez les corriges des 8 exercices (formulaire-exercices.md)');
  Logger.log('6. RECETTE : repondez vous-meme au formulaire. Vous devez voir');
  Logger.log('      le bouton « Afficher le score », la note, et les corriges.');
  Logger.log('');
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
