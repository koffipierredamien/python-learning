/**
 * =====================================================================
 *  AcProKids Coding Camp — REVISION GENERALE
 *  texte et nombres, listes, decalage, and / or, et la repetition
 *
 *  POUR TOUT LE MONDE. Un telephone suffit, et rien d'autre.
 *
 *  LE FORMULAIRE SE SUFFIT A LUI-MEME : aucune question ne renvoie a
 *  une seance, a un atelier ni a un projet. Les listes sont redonnees
 *  a chaque question, les programmes recopies en entier, et aucune
 *  question ne depend de la precedente. On peut donc le renvoyer tel
 *  quel dans un mois, ou le donner a un enfant qui etait absent.
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

  var form = FormApp.create('Revision generale — vingt questions');

  form.setDescription(
      'AcProKids Coding Camp — Jeremiah Geeks\n\n' +
      'Vingt questions pour verifier ce que tu sais faire. Chacune se repond avec ce qui est ecrit dedans : tu n\'as besoin de rien d\'autre, ni d\'un cahier, ni d\'un ordinateur. Tu peux la refaire autant de fois que tu veux.\n\n' +
      'RAPPELS A GARDER SOUS LES YEUX :\n' +
      '    input rend TOUJOURS du texte\n    dans une liste, les numeros commencent a ZERO\n    le decalage dit QUI DEPEND DE QUI\n    and : il faut TOUT   ·   or : il suffit d\'UN\n    une repetition s\'arrete parce que quelque chose AVANCE\n\n' +
      '20 questions, 20 points. Tu as ta note et les explications a la fin. ' +
      'Se tromper n\'est pas grave : c\'est comme ca qu\'on apprend.');

  form.setIsQuiz(true);
  form.setShowLinkToRespondAgain(false);
  form.setConfirmationMessage(
      'C\'est envoye ! Clique sur « Afficher le score » pour voir ta note et les explications. ' +
      'Tu peux refaire ce quiz autant de fois que tu veux.');

  form.addTextItem().setTitle('Ton prenom et ton nom').setRequired(true);
  form.addMultipleChoiceItem()
      .setTitle('Ta classe')
      .setChoiceValues(['Jerusalem Geeks (9 – 12 ans)', 'Jeremiah Geeks (12 – 18 ans)'])
      .setRequired(true);

  var questions = [
    ['print("7" + "7")\n\nQu\'est-ce qui s\'affiche ?',
     ['14', '7 7', '77', 'une erreur rouge'], '77',
     'Il y a des guillemets autour : ce sont deux TEXTES. Le + colle les textes bout a bout, il ne les additionne pas.'],

    ['age = input("Ton age ? ")\nprint(age * 2)\n\nLe joueur tape 12. Qu\'est-ce qui s\'affiche ?',
     ['24', '12', 'une erreur rouge', '1212'], '1212',
     'input rend TOUJOURS du texte, meme quand on tape des chiffres. Et un texte multiplie par 2, c\'est le texte ecrit deux fois de suite.'],

    ['print(int("7") + int("7"))\n\nQu\'est-ce qui s\'affiche ?',
     ['14', '77', '7 7', 'une erreur rouge'], '14',
     'int() transforme le texte "7" en vrai nombre 7. Et deux nombres, le + les additionne.'],

    ['a = input("Un nombre : ")\nb = input("Un autre : ")\n\nQue faut-il ecrire pour afficher leur SOMME ?',
     ['print(a + b)', 'print(int(a) + int(b))', 'print(str(a) + str(b))', 'print(a) + print(b)'], 'print(int(a) + int(b))',
     'Tant qu\'on ne les a pas transformes en nombres, a et b sont deux textes, que le + met bout a bout.'],

    ['equipe = ["A", "B", "C", "D"]\nprint(equipe[3])\n\nQu\'est-ce qui s\'affiche ?',
     ['C', 'A', 'D', 'une erreur rouge'], 'D',
     'Les numeros commencent a ZERO : A est le 0, B le 1, C le 2, D le 3.'],

    ['equipe = ["A", "B", "C", "D"]\nequipe[1] = equipe[2]\nprint(equipe)\n\nQu\'est-ce qui s\'affiche ?',
     ['[\'A\', \'C\', \'C\', \'D\']', '[\'A\', \'B\', \'C\', \'D\']', '[\'A\', \'B\', \'B\', \'D\']', 'une erreur rouge'], '[\'A\', \'C\', \'C\', \'D\']',
     'On LIT equipe[2], qui vaut C, et on le RANGE dans equipe[1]. Le B est ecrase, le C reste a sa place : ca va de droite a gauche.'],

    ['sacs = ["riz", "sucre", "sel", "farine", "huile"]\n\nQuel numero faut-il ecrire entre les crochets pour obtenir "huile" ?',
     ['5', '4', '3', 'Aucun : il faut ecrire son nom'], '4',
     'Les numeros commencent a ZERO : riz est 0, sucre 1, sel 2, farine 3, huile 4.'],

    ['sacs = ["riz", "sucre", "sel", "farine", "huile"]\nprint(sacs[5])\n\nQue se passe-t-il ?',
     ['Ca affiche huile', 'Ca n\'affiche rien', 'Ca affiche 5', 'Une erreur rouge : IndexError'], 'Une erreur rouge : IndexError',
     'Cinq elements, ce sont les numeros 0, 1, 2, 3 et 4. Le numero 5 n\'existe pas : Python s\'arrete et le dit.'],

    ['x = 10\nif x > 5:\n    print("A")\nprint("B")\n\nQu\'est-ce qui s\'affiche ?',
     ['A seulement', 'B seulement', 'A puis B', 'rien du tout'], 'A puis B',
     'print("B") est colle a gauche : il est DEHORS du if, donc il s\'affiche quoi qu\'il arrive.'],

    ['points = 50\nif points > 50:\n    points = points + 10\nprint(points)\n\nQu\'est-ce qui s\'affiche ?',
     ['60', '50', '0', 'une erreur rouge'], '50',
     '50 n\'est pas PLUS GRAND que 50. La condition est fausse, la ligne decalee est sautee, et points n\'a pas bouge.'],

    ['points = 100\nreponse = int(input("Combien font 7 x 8 ? "))\n\nif reponse == 56:\n    print("Juste !")\nelse:\n    points = points - 40\n    print("Il te reste " + str(points))\n\nPourquoi le nombre de points ne s\'affiche-t-il QUE lorsque la reponse est fausse ?',
     ['Parce que la ligne qui l\'affiche est DANS le else', 'Parce que str() ne marche pas dans un if', 'Parce qu\'il manque un deuxieme else', 'Parce que points vaut 100 au depart'], 'Parce que la ligne qui l\'affiche est DANS le else',
     'Decalee sous le else, cette ligne appartient au else : elle ne s\'execute que si la condition est fausse.'],

    ['points = 100\nreponse = int(input("Combien font 7 x 8 ? "))\n\nif reponse == 56:\n    print("Juste !")\nelse:\n    points = points - 40\n    print("Il te reste " + str(points))\n\nSANS AJOUTER AUCUNE LIGNE, comment faire pour que le nombre de points s\'affiche dans les DEUX cas ?',
     ['On l\'ecrit une deuxieme fois dans le if', 'On enleve le else', 'On met le if et le else a la meme hauteur', 'On recule la derniere ligne de 4 espaces, pour la coller a gauche'], 'On recule la derniere ligne de 4 espaces, pour la coller a gauche',
     'Collee a gauche, la ligne n\'appartient plus au else : elle appartient au programme, et s\'affiche dans tous les cas.'],

    ['age = 11\nprint(age >= 12 and age <= 18)\n\nQu\'est-ce qui s\'affiche ?',
     ['True', '11', 'False', 'une erreur rouge'], 'False',
     'La premiere question est fausse : 11 n\'est pas plus grand ou egal a 12. Avec and, une seule fausse suffit pour que tout soit faux.'],

    ['Les cases d\'un jeu portent les numeros 1 a 9.\n\nPour REFUSER un numero de case qui n\'existe pas, j\'ecris :',
     ['case < 1 and case > 9', 'case < 1 or case > 9', 'case >= 1 or case <= 9', 'case > 1 or case < 9'], 'case < 1 or case > 9',
     'Une seule des deux raisons suffit pour refuser : c\'est or. Avec and, il faudrait un nombre a la fois plus petit que 1 ET plus grand que 9 : ca n\'existe pas, donc rien ne serait jamais refuse.'],

    ['Dans cette liste, la case 3 est deja prise : elle contient "X" au lieu de "3".\nLe test  plateau[case - 1] == str(case)  veut dire : « la case contient encore son numero, donc elle est libre ».\n\nplateau = ["1", "2", "X", "4", "5", "6", "7", "8", "9"]\ncase = 3\n\nif case >= 1 or case <= 9 and plateau[case - 1] == str(case):\n    plateau[case - 1] = "O"\n    print("Pose !")\nelse:\n    print("Coup impossible.")\n\nQu\'est-ce qui s\'affiche ?',
     ['Pose !   (le O s\'ecrit par-dessus le X)', 'Coup impossible.', 'une erreur rouge', 'rien du tout'], 'Pose !   (le O s\'ecrit par-dessus le X)',
     'case >= 1 est vrai. Avec or, il suffit d\'une seule reponse vraie : le reste de la ligne n\'est meme plus regarde, et le coup passe.'],

    ['plateau = ["1", "2", "X", "4", "5", "6", "7", "8", "9"]\ncase = 3\n\nif case >= 1 or case <= 9 and plateau[case - 1] == str(case):\n    plateau[case - 1] = "O"\n    print("Pose !")\nelse:\n    print("Coup impossible.")\n\nLa case 3 est deja prise. Quel mot faut-il changer pour que le coup soit REFUSE ?',
     ['le str(), qu\'il faut enlever', 'le - 1, qu\'il faut enlever', 'le premier or, qu\'il faut remplacer par and', 'le >= qu\'il faut mettre en >'], 'le premier or, qu\'il faut remplacer par and',
     'Avec and, les TROIS questions comptent : le numero est assez grand, il est assez petit, ET la case est libre.'],

    ['Un dessin s\'affiche avec 5 lignes de print.\n\nPour l\'afficher TROIS fois de suite, en recopiant les lignes a chaque fois, combien de lignes de print faut-il ecrire en tout ?',
     ['5', '8', '3', '15'], '15',
     'Cinq lignes, trois fois : quinze. C\'est pour eviter ce genre de recopiage qu\'existe la repetition.'],

    ['tour = 0\nwhile tour < 3:\n    print("A")\n    tour = tour + 1\n\nCombien de A s\'affichent ?',
     ['3', '2', '4', 'sans fin'], '3',
     'tour vaut 0, puis 1, puis 2 : trois passages. A 3, la condition devient fausse et la repetition s\'arrete.'],

    ['tour = 0\nwhile tour < 3:\n    print("A")\n\nQu\'est-ce qui se passe ?',
     ['Ca affiche A une seule fois', 'Ca affiche A sans fin', 'Une erreur rouge', 'Rien ne s\'affiche'], 'Ca affiche A sans fin',
     'Rien ne fait avancer tour : il vaut 0 pour toujours, donc la condition reste vraie pour toujours. Une repetition s\'arrete parce que quelque chose AVANCE.'],

    ['Quelle touche arrete un programme qui s\'est mis a repeter sans fin ?',
     ['Ctrl + S', 'Entree', 'Ctrl + C', 'Echap'], 'Ctrl + C',
     'Dans la zone du bas de Thonny, Ctrl + C est le bouton d\'arret d\'urgence. Ailleurs, oui, Ctrl + C sert a copier.']
  ];

  var sections = {0: ['PARTIE A — Texte ou nombre', 'Ce que fait l\'ordinateur quand on melange du texte et des nombres.'], 4: ['PARTIE B — Les listes', 'Une liste, et le numero de chaque chose a l\'interieur.'], 8: ['PARTIE C — Le decalage', 'Quatre espaces de plus, et le programme ne fait plus la meme chose.'], 12: ['PARTIE D — and, or', 'Deux petits mots qui decident de tout dans une condition.'], 16: ['PARTIE E — Repeter', 'Repeter quelque chose, et savoir s\'arreter.']};

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
