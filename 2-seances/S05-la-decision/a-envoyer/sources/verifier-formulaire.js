// Rejoue un script .gs de formulaire contre un faux FormApp, sans rien envoyer
// a Google. Usage :  node sources/verifier-formulaire.js quiz-semaine.gs creerLeQuiz
const fs = require('fs');
let items = [], titre = null, quiz = false;

function item(type) {
  const it = { type, choix: [], points: 0, requis: false, titre: '', retours: {} };
  items.push(it);
  const self = {
    setTitle(t) { it.titre = t; return self; }, setHelpText(t) { it.aide = t; return self; },
    setPoints(p) { it.points = p; return self; }, setRequired(r) { it.requis = r; return self; },
    setChoiceValues(v) { it.choix = v.map(x => ({ v: x, ok: false })); return self; },
    setChoices(c) { it.choix = c; return self; },
    createChoice(v, ok) { return { v, ok: !!ok }; },
    setFeedbackForCorrect(f) { it.retours.ok = f; return self; },
    setFeedbackForIncorrect(f) { it.retours.ko = f; return self; },
    setGeneralFeedback(f) { it.retours.gen = f; return self; },
  };
  return self;
}
global.FormApp = {
  create(t) { titre = t;
    const f = { setDescription: () => f, setIsQuiz: (v) => { quiz = v; return f; },
      setShowLinkToRespondAgain: () => f, setConfirmationMessage: () => f, setPublished: () => f,
      addTextItem: () => item('texte'), addParagraphTextItem: () => item('paragraphe'),
      addMultipleChoiceItem: () => item('qcm'), addSectionHeaderItem: () => item('section'),
      getPublishedUrl: () => 'https://…/viewform', getEditUrl: () => 'https://…/edit' };
    return f; },
  createFeedback() { const b = { t: '', setText(x) { b.t = x; return b; }, build() { return b.t; } }; return b; },
};
global.Logger = { log: () => {} };

const fichier = process.argv[2], fonction = process.argv[3] || 'creerLeTest';
eval(fs.readFileSync(fichier, 'utf8'));
eval(fonction + '();');

const qcm = items.filter(i => i.type === 'qcm' && i.points > 0);
const txt = items.filter(i => (i.type === 'texte' || i.type === 'paragraphe') && i.points > 0);
console.log('Titre :', titre, '| quiz :', quiz);
console.log('QCM notés :', qcm.length, '| questions à réponse libre notées :', txt.length);
console.log('Total des points :', items.reduce((s, i) => s + i.points, 0));
let souci = 0;
const pos = qcm.map(it => {
  const b = it.choix.filter(c => c.ok);
  if (b.length !== 1) { souci++; console.log('  !! pas une seule bonne réponse :', it.titre.slice(0, 40)); }
  if (new Set(it.choix.map(c => c.v)).size !== it.choix.length) { souci++; console.log('  !! doublon :', it.titre.slice(0, 40)); }
  if (!it.retours.ko || it.retours.ko.length < 25) { souci++; console.log('  !! explication trop courte :', it.titre.slice(0, 40)); }
  return it.choix.findIndex(c => c.ok) + 1;
});
console.log('Position de la bonne réponse :', pos.join(' '));
const c = {}; pos.forEach(p => c[p] = (c[p] || 0) + 1);
console.log('Répartition :', JSON.stringify(c), '| deux fois de suite :',
            pos.some((p, i) => i && p === pos[i - 1]));
txt.forEach(it => { if (!it.retours.gen) { souci++; console.log('  !! pas de corrigé sur :', it.titre.slice(0, 40)); } });
console.log('Anomalies :', souci);
