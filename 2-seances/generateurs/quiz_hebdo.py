# -*- coding: utf-8 -*-
"""Six quiz hebdomadaires, 15 questions a choix multiples chacun, 100 % auto-corriges.
   Les bonnes reponses sont placees automatiquement selon une sequence de positions
   qui evite deux fois de suite le meme emplacement."""
import io, os, subprocess

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_CIBLE = [1, 3, 2, 4, 1, 2, 4, 3, 1, 4, 2, 3, 1, 4, 2]   # jamais deux fois de suite
# Une permutation differente par quiz : d'une semaine a l'autre, la suite des
# positions change, pour qu'aucun eleve ne puisse la repérer d'un quiz au suivant.
PERMUTATIONS = {5: [1, 2, 3, 4], 6: [2, 1, 4, 3], 7: [3, 4, 1, 2],
                8: [4, 3, 2, 1], 9: [2, 3, 4, 1], 10: [4, 1, 2, 3]}

def cible(num):
    p = PERMUTATIONS.get(num, [1, 2, 3, 4])
    return [p[v - 1] for v in BASE_CIBLE]

GABARIT = u'''/**
 * =====================================================================
 *  AcProKids Coding Camp — Quiz de la semaine n°{num}
 *  {sujet}
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

function creerLeQuiz() {{

  var form = FormApp.create('{titre}');

  form.setDescription(
      'AcProKids Coding Camp — Jeremiah Geeks\\n\\n' +
      '{intro}\\n\\n' +
      'RAPPELS A GARDER SOUS LES YEUX :\\n' +
      '{rappels}\\n\\n' +
      '15 questions, 15 points. Tu as ta note et les explications a la fin. ' +
      'Se tromper n\\'est pas grave : c\\'est comme ca qu\\'on apprend.');

  form.setIsQuiz(true);
  form.setShowLinkToRespondAgain(false);
  form.setConfirmationMessage(
      'C\\'est envoye ! Clique sur « Afficher le score » pour voir ta note et les explications. ' +
      'A samedi, 12 h !');

  form.addTextItem().setTitle('Ton prenom et ton nom').setRequired(true);
  form.addMultipleChoiceItem()
      .setTitle('Ta classe')
      .setChoiceValues(['Jerusalem Geeks (9 – 12 ans)', 'Jeremiah Geeks (12 – 18 ans)'])
      .setRequired(true);

  var questions = [
{questions}
  ];

  var sections = {sections};

  questions.forEach(function (q, i) {{
    if (sections[i]) {{
      form.addSectionHeaderItem().setTitle(sections[i][0]).setHelpText(sections[i][1]);
    }}
    var item = form.addMultipleChoiceItem();
    item.setTitle(q[0]);
    item.setPoints(1);
    item.setRequired(true);
    item.setChoices(q[1].map(function (texte) {{
      return item.createChoice(texte, texte === q[2]);
    }}));
    item.setFeedbackForCorrect(FormApp.createFeedback().setText('Bravo !').build());
    item.setFeedbackForIncorrect(FormApp.createFeedback().setText(q[3]).build());
  }});

  try {{ form.setPublished(true); }} catch (e) {{
    Logger.log('A faire a la main : ouvrez le formulaire et cliquez sur « Publier ».');
  }}

  Logger.log('#######################################################');
  Logger.log('##  A FAIRE MAINTENANT, SINON L\\'ELEVE NE VERRA RIEN  ##');
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
}}
'''


def js(t):
    return t.replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n")


def bloc_questions(qs, num):
    out = []
    for i, (enonce, bonne, distracteurs, expl) in enumerate(qs):
        k = cible(num)[i] - 1
        choix = distracteurs[:k] + [bonne] + distracteurs[k:]
        assert len(choix) == 4, (i, choix)
        assert len(set(choix)) == 4, (i, choix)
        out.append(u"    ['%s',\n     [%s], '%s',\n     '%s']" % (
            js(enonce), ", ".join("'" + js(c) + "'" for c in choix), js(bonne), js(expl)))
    return u",\n\n".join(out)


def ecrire(num, dossier, titre, sujet, intro, rappels, sections, qs):
    assert len(qs) == 15, (num, len(qs))
    src = GABARIT.format(
        num=num, sujet=sujet, titre=js(titre), intro=js(intro),
        rappels=js("\n".join("    " + r for r in rappels)),
        questions=bloc_questions(qs, num),
        sections=u"{" + u", ".join("%d: ['%s', '%s']" % (k, js(v[0]), js(v[1]))
                                   for k, v in sections.items()) + u"}")
    chemin = os.path.join(BASE, dossier, "a-envoyer", "quiz-semaine.gs")
    io.open(chemin, "w", encoding="utf-8").write(src)
    # on rejoue contre le faux FormApp
    tmp = "/tmp/quiz_check.js"
    io.open(tmp, "w", encoding="utf-8").write(src)
    r = subprocess.run(["node", os.path.join(BASE, "S05-la-decision/a-envoyer/sources/verifier-formulaire.js"),
                        tmp, "creerLeQuiz"], capture_output=True, text=True)
    print("QUIZ %d  %s" % (num, dossier))
    for l in r.stdout.strip().split("\n"):
        print("        " + l)
    if r.returncode != 0:
        print(r.stderr[:500])
