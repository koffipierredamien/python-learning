// Le tableau de bord du Grand Parcours : 3 diapos a laisser projetees.
const P = require('/tmp/node_modules/pptxgenjs');
const p = new P();
p.layout = 'LAYOUT_WIDE';
const W = 13.3, H = 7.5, M = 0.7;
const NUIT = '12122A', CLAIR = 'F7F7FB', BLANC = 'FFFFFF', ENCRE = '14142B';
const GRIS = '5A5A72', GRIS_C = 'A8A8C0', CYAN = '4FC3F7', ORANGE = 'FFB74D';
const ORANGE_F = 'A65D00', VIOLET_F = '6B2D8F', VERT_F = '0C5C29', VERT = '2FB765';
const SANS = 'Calibri', MONO = 'Courier New';
p.author = 'Jerusalem Geeks & Jeremiah Geeks';
p.title = 'Le Grand Parcours - tableau de bord';

function txt(s, t, o) { s.addText(t, Object.assign({ isTextBox: true, margin: 0, fontFace: SANS, valign: 'top' }, o)); }
function neuf(s, x, y, t, c, o) {
  for (let i = 0; i < 9; i++) s.addShape(p.ShapeType.roundRect, {
    x: x + (i % 3) * t * 1.35, y: y + Math.floor(i / 3) * t * 1.35, w: t, h: t,
    fill: { color: c, transparency: o === undefined ? 60 : o }, line: { type: 'none' }, rectRadius: 0.02 });
}

// ------------------------------------------------- 1. l'annonce
{
  const s = p.addSlide(); s.background = { color: NUIT };
  neuf(s, 9.6, 1.5, 0.78, CYAN, 82);
  txt(s, 'JEREMIAH GEEKS  ·  10 OCTOBRE 2026', { x: M, y: 1.5, w: 8.4, h: 0.4, fontSize: 14, bold: true, color: VIOLET_F, charSpacing: 4 });
  txt(s, '🧭  LE GRAND PARCOURS', { x: M, y: 2.1, w: 9.0, h: 1.1, fontSize: 52, bold: true, color: BLANC });
  txt(s, 'Tout ce qu\'on sait faire, du premier samedi à aujourd\'hui.', { x: M, y: 3.35, w: 9.2, h: 0.6, fontSize: 23, color: CYAN, italic: true });
  const regles = ['8 paliers, dans l\'ordre. Tu écris le code toi-même.',
                  'F5 à la fin de chaque palier, puis tu coches ta feuille.',
                  'Bloqué plus de 2 minutes ? Carte orange, et tu passes au suivant.',
                  'Les 3 défis ⭐ sont au dos, pour ceux qui arrivent au bout.'];
  regles.forEach((r, i) => {
    txt(s, '▸', { x: M, y: 4.3 + i * 0.52, w: 0.4, h: 0.4, fontSize: 18, color: ORANGE, bold: true });
    txt(s, r, { x: M + 0.45, y: 4.3 + i * 0.52, w: 10.5, h: 0.45, fontSize: 18, color: GRIS_C });
  });
  s.addNotes('On distribue la feuille, on lit les quatre règles à voix haute, et on lance. 35 minutes. Je circule, je ne touche aucun clavier : je fais lire les messages rouges.');
}

// ------------------------------------------------- 2. le tableau de bord
{
  const s = p.addSlide(); s.background = { color: CLAIR };
  txt(s, 'OÙ DEVRAIS-TU EN ÊTRE ?', { x: M, y: 0.5, w: 8, h: 0.4, fontSize: 13, bold: true, color: VIOLET_F, charSpacing: 3 });
  txt(s, 'Le tableau de bord', { x: M, y: 0.95, w: 8, h: 0.8, fontSize: 36, bold: true, color: ENCRE });
  const paliers = [
    ['1', 'AFFICHER', '3 min', '12 h 18', VIOLET_F],
    ['2', 'LA BOÎTE', '4 min', '12 h 22', VIOLET_F],
    ['3', 'COLLER', '4 min', '12 h 26', VIOLET_F],
    ['4', 'DEMANDER', '5 min', '12 h 31', VIOLET_F],
    ['5', 'TEXTE OU NOMBRE', '6 min', '12 h 37', ORANGE_F],
    ['6', 'L\'ÂGE', '6 min', '12 h 43', ORANGE_F],
    ['7', 'LE COMPTEUR', '4 min', '12 h 47', VERT_F],
    ['8', 'LA DÉCISION', '3 min', '12 h 50', VERT_F],
  ];
  paliers.forEach((pa, i) => {
    const col = i % 2, lig = Math.floor(i / 2);
    const x = M + col * 6.15, y = 2.0 + lig * 1.18;
    s.addShape(p.ShapeType.roundRect, { x, y, w: 5.75, h: 1.0, rectRadius: 0.07,
      fill: { color: BLANC }, line: { color: 'E0E0EA', width: 1 } });
    s.addShape(p.ShapeType.ellipse, { x: x + 0.22, y: y + 0.24, w: 0.52, h: 0.52, fill: { color: pa[4] }, line: { type: 'none' } });
    txt(s, pa[0], { x: x + 0.22, y: y + 0.24, w: 0.52, h: 0.52, fontSize: 18, bold: true, color: BLANC, align: 'center', valign: 'middle' });
    txt(s, pa[1], { x: x + 0.92, y: y + 0.19, w: 3.2, h: 0.4, fontSize: 16, bold: true, color: ENCRE });
    txt(s, pa[2], { x: x + 0.92, y: y + 0.58, w: 3.2, h: 0.32, fontSize: 12, color: GRIS });
    txt(s, pa[3], { x: x + 4.0, y: y + 0.33, w: 1.55, h: 0.4, fontSize: 17, bold: true, color: pa[4], align: 'right', fontFace: MONO });
  });
  txt(s, 'Tu es en retard sur l\'horloge ? Ce n\'est pas grave : avance, et saute ce qui bloque.', {
    x: M, y: H - 1.35, w: W - 2 * M, h: 0.5, fontSize: 18, bold: true, color: VIOLET_F });
  s.addNotes('Diapo à laisser affichée pendant tout le parcours. Les heures sont indicatives : elles servent à l\'élève pour se situer, pas à le presser. Les paliers 7 et 8 sont de la DÉCOUVERTE : on ne corrige pas, on les laisse constater.');
}

// ------------------------------------------------- 3. la bascule
{
  const s = p.addSlide(); s.background = { color: NUIT };
  neuf(s, W - 3.4, 1.2, 0.62, ORANGE, 85);
  txt(s, '✋  ON S\'ARRÊTE', { x: M, y: 1.6, w: 8.4, h: 0.5, fontSize: 18, bold: true, color: ORANGE, charSpacing: 3 });
  txt(s, 'Les deux derniers paliers,\nvous venez de les découvrir seuls.', {
    x: M, y: 2.3, w: 10.6, h: 1.8, fontSize: 36, bold: true, color: BLANC, lineSpacing: 46 });
  txt(s, 'Le palier 7, c\'est le COMPTEUR.   ·   Le palier 8, c\'est la DÉCISION.', {
    x: M, y: 4.3, w: 10.6, h: 0.6, fontSize: 21, color: CYAN });
  txt(s, 'Maintenant, on va comprendre POURQUOI ça marche.\nClaviers lâchés, écrans face à moi.', {
    x: M, y: 5.1, w: 10.6, h: 1.1, fontSize: 20, color: GRIS_C, lineSpacing: 28, italic: true });
  s.addNotes('La bascule du parcours vers la leçon. On demande d\'abord : « au palier 7, qui avait prédit 2 ? » et « au palier 8, qui a vu le programme changer d\'avis ? » Puis on enchaîne sur la boîte en carton.');
}

p.writeFile({ fileName: '/home/user/python-learning/2-seances/S05-la-decision/a-projeter/parcours-tableau-de-bord.pptx' })
  .then((f) => console.log('deck ecrit :', f));
