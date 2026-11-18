/**
 * =====================================================================
 *  AcProKids Coding Camp — REVISION GENERALE, a refaire a la maison
 *  tout ce qu'on sait depuis septembre, et la boucle pour finir
 *
 *  POUR TOUT LE MONDE, cette fois : c'est la revision du samedi
 *  14 novembre, refaite a la maison. Un telephone suffit.
 *  Les cinq ateliers qu'on a tapes au clavier y sont devenus des
 *  questions : on ne demande plus d'ecrire le code, on demande
 *  de dire ce qu'il fait.
 *
 *  20 questions a choix multiples = 20 points.
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

  var form = FormApp.create('Revision generale — a refaire a la maison');

  form.setDescription(
      'AcProKids Coding Camp — Jeremiah Geeks\n\n' +
      'Ce sont les questions de la revision de samedi, plus celles des ateliers qu\'on a faits au clavier. Si tu as suivi samedi, tu les connais deja : c\'est fait pour.\n\n' +
      'RAPPELS A GARDER SOUS LES YEUX :\n' +
      '    input rend TOUJOURS du texte\n    indice = numero - 1\n    le decalage dit QUI DEPEND DE QUI\n    and : il faut TOUT   ·   or : il suffit d\'UN\n    une boucle s\'arrete parce que quelque chose AVANCE\n\n' +
      '20 questions, 20 points. Tu as ta note et les explications a la fin. ' +
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
    ['print("7" + "7")\n\nQu\'est-ce qui s\'affiche ?',
     ['14', '7 7', '77', 'une erreur rouge'], '77',
     'Des guillemets autour : c\'est du TEXTE. Le + colle, il n\'additionne pas.'],

    ['age = input("Ton age ? ")\nprint(age * 2)\n\nLe joueur tape 12. Qu\'est-ce qui s\'affiche ?',
     ['24', '12', 'une erreur rouge', '1212'], '1212',
     'input rend TOUJOURS du texte. Et texte x 2, c\'est le texte ecrit deux fois de suite, exactement comme "=" * 33 qui dessine nos cadres.'],

    ['print(int("7") + int("7"))\n\nEt maintenant ?',
     ['14', '77', '7 7', 'une erreur rouge'], '14',
     'int() transforme le dessin du chiffre en vrai nombre. Et deux nombres, le + les additionne.'],

    ['a = input("Un nombre : ")\nb = input("Un autre : ")\n\nQue faut-il ecrire pour afficher leur SOMME ?',
     ['print(a + b)', 'print(int(a) + int(b))', 'print(str(a) + str(b))', 'print(a) + print(b)'], 'print(int(a) + int(b))',
     'Tant qu\'on ne les a pas convertis, a et b sont deux dessins de chiffres, que le + met bout a bout. C\'etait l\'atelier n°1 de samedi.'],

    ['equipe = ["A", "B", "C", "D"]\nprint(equipe[3])',
     ['C', 'A', 'D', 'une erreur rouge'], 'D',
     'Les rangs partent de zero : A est au rang 0, donc D est au rang 3. Le dernier rang, c\'est toujours un de moins que le nombre d\'elements.'],

    ['equipe[1] = equipe[2]\nprint(equipe)\n\nQu\'est-ce qui s\'affiche ?',
     ['[\'A\', \'C\', \'C\', \'D\']', '[\'A\', \'B\', \'C\', \'D\']', '[\'A\', \'B\', \'B\', \'D\']', 'une erreur rouge'], '[\'A\', \'C\', \'C\', \'D\']',
     'On LIT equipe[2], qui vaut C, et on le RANGE dans equipe[1]. Le B est ecrase, le C reste a sa place : la fleche va de droite a gauche.'],

    ['sacs = ["riz", "sucre", "sel", "farine", "huile"]\n\nQuel est l\'indice du sac numero 5 ?',
     ['5', '4', '3', 'Il n\'y en a pas'], '4',
     'indice = numero - 1. Cinq sacs, ce sont les rangs 0, 1, 2, 3 et 4.'],

    ['print(sacs[5])\n\nQue se passe-t-il ?',
     ['Ca affiche huile', 'Ca n\'affiche rien', 'Ca affiche 5', 'Une erreur rouge : IndexError'], 'Une erreur rouge : IndexError',
     'Le rang 5 n\'existe pas : la liste s\'arrete au rang 4. C\'est le message rouge qu\'on a fait apparaitre expres samedi.'],

    ['x = 10\nif x > 5:\n    print("A")\nprint("B")\n\nQu\'est-ce qui s\'affiche ?',
     ['A seulement', 'B seulement', 'A puis B', 'rien du tout'], 'A puis B',
     'print("B") est colle a gauche : il est DEHORS du if. Il s\'affiche quoi qu\'il arrive.'],

    ['points = 50\nif points > 50:\n    points = points + 10\nprint(points)',
     ['60', '50', '0', 'une erreur rouge'], '50',
     '50 n\'est pas PLUS GRAND que 50. La condition est fausse, la ligne decalee est sautee, et points n\'a pas bouge.'],

    ['if reponse == 56:\n    print("Juste !")\nelse:\n    points = points - 40\n    print("Il te reste " + str(points))\n\nPourquoi le score ne s\'affiche-t-il QUE quand on se trompe ?',
     ['Parce que la ligne du score est DANS le else', 'Parce que str() ne marche pas dans un if', 'Parce qu\'il manque un deuxieme else', 'C\'est un bug de Python'], 'Parce que la ligne du score est DANS le else',
     'Decalee sous le else, la ligne appartient au else : elle ne s\'execute que si la condition est fausse.'],

    ['Toujours le meme programme.\n\nSANS AJOUTER AUCUNE LIGNE, comment faire pour que le score s\'affiche dans les DEUX cas ?',
     ['On l\'ecrit une deuxieme fois dans le if', 'On enleve le else', 'On met le if et le else a la meme hauteur', 'On recule la ligne de 4 espaces, pour la coller a gauche'], 'On recule la ligne de 4 espaces, pour la coller a gauche',
     'Collee a gauche, la ligne n\'appartient plus au else : elle appartient au programme, et s\'affiche dans tous les cas. C\'etait l\'atelier n°3.'],

    ['age = 11\nprint(age >= 12 and age <= 18)',
     ['True', '11', 'False', 'une erreur rouge'], 'False',
     'La premiere question est fausse : 11 n\'est pas plus grand ou egal a 12. Avec and, une seule fausse suffit pour que tout soit faux.'],

    ['Pour REFUSER une case qui n\'existe pas, j\'ecris :',
     ['case < 1 and case > 9', 'case < 1 or case > 9', 'case >= 1 or case <= 9', 'case > 1 or case < 9'], 'case < 1 or case > 9',
     'Une seule des deux raisons suffit pour refuser : c\'est or. Avec and, il faudrait un nombre a la fois plus petit que 1 ET plus grand que 9. Ca n\'existe pas.'],

    ['La case 3 contient deja un X.\n\nif case >= 1 or case <= 9 and plateau[case - 1] == str(case):\n\nAvec case = 3, que fait le programme ?',
     ['Il pose quand meme, par-dessus le X', 'Il refuse, c\'est correct', 'Il plante', 'Il ne fait rien du tout'], 'Il pose quand meme, par-dessus le X',
     'case >= 1 est vrai. Avec or, il suffit d\'une reponse vraie : le reste de la ligne n\'est meme plus regarde. C\'est le programme qui mentait, samedi.'],

    ['Quel mot faut-il changer pour reparer cette ligne ?',
     ['le str(), qu\'il faut enlever', 'le - 1, qu\'il faut enlever', 'le or, qu\'il faut remplacer par and', 'le >= qu\'il faut mettre en >'], 'le or, qu\'il faut remplacer par and',
     'Avec and, les TROIS questions comptent : la case existe par en bas, par en haut, et elle est libre.'],

    ['Afficher le plateau une fois coute 5 lignes de print.\n\nPour l\'afficher TROIS fois en recopiant, combien de lignes d\'affichage faut-il ecrire ?',
     ['5', '8', '3', '15'], '15',
     'Cinq lignes, trois fois : quinze. Plus les lignes qui posent les symboles : c\'est le chiffre qu\'on a compte au tableau samedi.'],

    ['tour = 0\nwhile tour < 3:\n    print("A")\n    tour = tour + 1\n\nCombien de A s\'affichent ?',
     ['3', '2', '4', 'sans fin'], '3',
     'tour vaut 0, puis 1, puis 2 : trois passages. A 3, la condition devient fausse et la boucle s\'arrete.'],

    ['On oublie la ligne  tour = tour + 1.\n\nQue se passe-t-il ?',
     ['Ca affiche A une seule fois', 'Ca affiche A sans fin', 'Une erreur rouge', 'Rien ne s\'affiche'], 'Ca affiche A sans fin',
     'Rien ne fait avancer tour : la condition reste vraie pour toujours. Une boucle s\'arrete parce que quelque chose AVANCE.'],

    ['Quelle touche arrete un programme parti en boucle sans fin ?',
     ['Ctrl + S', 'Entree', 'Ctrl + C', 'Echap'], 'Ctrl + C',
     'Dans la zone du bas de Thonny, Ctrl + C est le bouton d\'arret d\'urgence. Ailleurs, oui, Ctrl + C copie.']
  ];

  var sections = {0: ['PARTIE A — Texte ou nombre', 'La question qui provoque la moitie des ecrans rouges depuis septembre.'], 4: ['PARTIE B — La liste et l\'indice', 'Le numero du sac est celui de l\'humain. L\'indice est celui de la machine.'], 8: ['PARTIE C — Le decalage decide de tout', 'Quatre espaces, et le programme ne fait plus la meme chose.'], 12: ['PARTIE D — and, or, et le piege', 'Celle-la, c\'est ton propre jeu qui est en cause.'], 16: ['PARTIE E — Le defi, et la boucle', 'Pourquoi on avait besoin d\'un outil de plus.']};

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
  Logger.log('20 questions a choix multiples = 20 points, 100 % automatique.');
}
