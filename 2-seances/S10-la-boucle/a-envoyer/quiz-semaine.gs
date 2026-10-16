/**
 * =====================================================================
 *  AcProKids Coding Camp — Quiz de la semaine n°8
 *  la boucle while, et l'alternance des joueurs
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

  var form = FormApp.create('Quiz n°8 — Le jeu tourne tout seul');

  form.setDescription(
      'AcProKids Coding Camp — Jeremiah Geeks\n\n' +
      'Ce quiz porte sur la plus grande seance des deux mois : la boucle while, et les joueurs qui se passent la main.\n\n' +
      'RAPPELS A GARDER SOUS LES YEUX :\n' +
      '    while  =  TANT QUE la reponse est vraie, on refait le bloc\n    sans la ligne qui fait avancer le compteur, la boucle ne s\'arrete JAMAIS\n    Ctrl + C arrete un programme devenu fou\n\n' +
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
    ['tour = 0\nwhile tour < 3:\n    print("A")\n    tour = tour + 1\n\nCombien de A s\'affichent ?',
     ['3', '2', '4', 'une infinite'], '3',
     'tour vaut 0, puis 1, puis 2 : trois tours. A 3, la question repond False.'],

    ['Apres cette boucle, que vaut tour ?',
     ['0', '2', '3', '4'], '3',
     'La boucle s\'arrete quand tour vaut 3 — mais tour vaut bien 3 a ce moment-la.'],

    ['tour = 0\nwhile tour < 3:\n    print("A")\n\nQue se passe-t-il ?',
     ['Ca affiche 3 A', 'Ca affiche A sans fin', 'Ca n\'affiche rien', 'Une erreur rouge'], 'Ca affiche A sans fin',
     'Il manque tour = tour + 1. tour vaut toujours 0, donc la question repond toujours True.'],

    ['Quelle touche arrete un programme parti en boucle sans fin ?',
     ['Ctrl + S', 'F5', 'Entree', 'Ctrl + C'], 'Ctrl + C',
     'Ctrl + C dans la zone du bas. C\'est le geste a connaitre par coeur.'],

    ['tour = 5\nwhile tour > 0:\n    print(tour)\n    tour = tour - 1\n\nQuel est le PREMIER nombre affiche ?',
     ['5', '4', '0', '1'], '5',
     'On affiche AVANT d\'enlever 1 : le premier affiche est donc 5.'],

    ['Et quel est le DERNIER nombre affiche ?',
     ['0', '1', '-1', '5'], '1',
     'Quand tour vaut 1, la question 1 > 0 est vraie : on affiche 1, puis tour passe a 0 et ca s\'arrete.'],

    ['Qu\'est-ce qui doit etre DANS la boucle du jeu ?',
     ['Seulement la question au joueur', 'Seulement la pose', 'Rien, tout est dehors', 'L\'affichage, la question, la pose et le compteur'], 'L\'affichage, la question, la pose et le compteur',
     'Tout ce qui doit se repeter a chaque tour est decale dans la boucle.'],

    ['Et qu\'est-ce qui doit rester DEHORS, colle a gauche ?',
     ['La pose du symbole', 'La question au joueur', 'Les boites de depart, et l\'affichage final', 'L\'alternance des joueurs'], 'Les boites de depart, et l\'affichage final',
     'Ce qui ne se fait qu\'une seule fois reste hors de la boucle.'],

    ['tour = 0\nwhile tour < 9:\n    ...\nprint("Fini")\n\nCombien de fois « Fini » s\'affiche-t-il ?',
     ['1 fois', '9 fois', '0 fois', 'une infinite'], '1 fois',
     'print("Fini") est colle a gauche : il n\'est pas dans la boucle, il se fait une seule fois, a la fin.'],

    ['Ou doit etre place  tour = tour + 1  dans le jeu ?',
     ['Au tout debut de la boucle', 'Apres la boucle', 'N\'importe ou dans la boucle', 'Dans le if du coup valide'], 'Dans le if du coup valide',
     'Un coup REFUSE ne doit pas faire avancer le tour, sinon le plateau n\'est jamais plein.'],

    ['Que se passe-t-il si  tour = tour + 1  est au debut de la boucle, avant la question ?',
     ['La boucle ne s\'arrete jamais', 'Un coup refuse fait quand meme avancer le tour', 'Une erreur rouge', 'Rien ne change'], 'Un coup refuse fait quand meme avancer le tour',
     'Le joueur peut alors perdre son tour en tapant n\'importe quoi neuf fois.'],

    ['symbole = "X"\nif symbole == "X":\n    symbole = "O"\nelse:\n    symbole = "X"\n\nQue vaut symbole a la fin ?',
     ['"X"', 'rien', '"O"', 'une erreur rouge'], '"O"',
     'On regarde ce qu\'il y a dans la boite, et on y remet autre chose. C\'est l\'idee du compteur.'],

    ['Dans le jeu, combien de choses echange-t-on quand on passe la main ?',
     ['Deux : le symbole et le nom du joueur', 'Une seule : le symbole', 'Trois', 'Aucune, c\'est automatique'], 'Deux : le symbole et le nom du joueur',
     'Les deux lignes vont ensemble, dans le meme if.'],

    ['Le fichier de la seance 10 est-il plus long ou plus court que celui de la seance 9 ?',
     ['Plus long, forcement', 'Exactement pareil', 'Deux fois plus long', 'Plus court, et il fait beaucoup plus'], 'Plus court, et il fait beaucoup plus',
     'C\'est ca, programmer : une bonne idee fait souvent RETRECIR le code.'],

    ['while tour < 20:\n\nQue se passerait-il dans le jeu XO ?',
     ['Le jeu jouerait 20 tours normalement', 'Le jeu planterait quand le plateau serait plein', 'Rien ne changerait', 'La boucle ne demarrerait pas'], 'Le jeu planterait quand le plateau serait plein',
     'Apres 9 coups, plus aucune case n\'est libre : le joueur ne pourrait plus jamais jouer un coup valide, et la boucle tournerait sans fin.']
  ];

  var sections = {0: ['PARTIE A — La boucle', 'Tant que la reponse est vraie, on recommence.'], 6: ['PARTIE B — Dedans ou dehors ?', 'Le decalage decide de tout.'], 11: ['PARTIE C — Le jeu', 'Neuf tours, et deux joueurs.']};

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
