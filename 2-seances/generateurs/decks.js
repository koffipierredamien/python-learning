// Un seul gabarit, sept diaporamas. Node + pptxgenjs.
const P = require('pptxgenjs');
const BASE = '/home/user/python-learning/2-seances/';
const W = 13.3, H = 7.5, M = 0.7;
const NUIT='12122A', NUIT2='20204A', CLAIR='F7F7FB', BLANC='FFFFFF', ENCRE='14142B';
const GRIS='5A5A72', GRIS_C='A8A8C0', CYAN='4FC3F7', ORANGE='FFB74D', ORANGE_F='A65D00';
const VIOLET='B06FD8', VIOLET_F='6B2D8F', VERT='2FB765', VERT_F='0C5C29', ROUGE='FF6B6B', ROUGE_F='B01B20';
const SANS='Calibri', MONO='Courier New';

function creer(s) {
  const p = new P();
  p.layout = 'LAYOUT_WIDE';
  p.author = 'Jerusalem Geeks & Jeremiah Geeks';
  p.title = 'Seance ' + s.num + ' - ' + s.titre;

  const txt = (sl,t,o)=>sl.addText(t,Object.assign({isTextBox:true,margin:0,fontFace:SANS,valign:'top'},o));
  const neuf = (sl,x,y,t,c,o)=>{for(let i=0;i<9;i++)sl.addShape(p.ShapeType.roundRect,{
    x:x+(i%3)*t*1.35,y:y+Math.floor(i/3)*t*1.35,w:t,h:t,
    fill:{color:c,transparency:o===undefined?60:o},line:{type:'none'},rectRadius:0.02});};
  const pied=(sl,h,sombre)=>{if(h)txt(sl,h,{x:W-2.9,y:H-0.74,w:2.2,h:0.34,fontFace:MONO,fontSize:11,
    color:sombre?GRIS_C:GRIS,align:'right'});neuf(sl,W-0.66,H-0.70,0.075,sombre?CYAN:VIOLET_F,sombre?55:70);};
  const sombre=(h)=>{const sl=p.addSlide();sl.background={color:NUIT};pied(sl,h,true);return sl;};
  const claire=(h)=>{const sl=p.addSlide();sl.background={color:CLAIR};pied(sl,h,false);return sl;};
  const surtitre=(sl,t,c)=>txt(sl,t.toUpperCase(),{x:M,y:0.5,w:W-2*M,h:0.34,fontSize:13,bold:true,
    color:c||VIOLET_F,charSpacing:3});
  const titre=(sl,t,o)=>{o=o||{};txt(sl,t,{x:M,y:o.y===undefined?0.95:o.y,w:o.w||W-2*M,h:o.h||1.0,
    fontSize:o.size||36,bold:true,color:o.color||ENCRE,lineSpacing:o.size?o.size*1.1:40});};
  const carte=(sl,x,y,w,h,o)=>{o=o||{};sl.addShape(p.ShapeType.roundRect,{x,y,w,h,rectRadius:0.08,
    fill:{color:o.fond||BLANC},line:o.trait?{color:o.trait,width:1.5}:{type:'none'},
    shadow:o.ombre===false?undefined:{type:'outer',color:'20204A',blur:10,offset:2,angle:90,opacity:0.12}});};
  const pastille=(sl,x,y,d,t,f,c,ta)=>{sl.addShape(p.ShapeType.ellipse,{x,y,w:d,h:d,fill:{color:f},line:{type:'none'}});
    txt(sl,t,{x,y,w:d,h:d,fontSize:ta||20,bold:true,color:c||BLANC,align:'center',valign:'middle'});};
  const bloc=(sl,code,o)=>{o=o||{};const y=o.y===undefined?2.4:o.y,h=o.h||1.2,w=o.w||(W-2*M),x=o.x===undefined?M:o.x;
    carte(sl,x,y,w,h,{fond:'12122A',ombre:false});
    txt(sl,code,{x:x+0.35,y:y+0.25,w:w-0.7,h:h-0.5,fontSize:o.taille||20,fontFace:MONO,
      color:o.couleur||CYAN,lineSpacing:o.inter||28});};
  const bandeau=(sl,t,c)=>txt(sl,t,{x:M,y:H-1.5,w:W-2*M,h:0.7,fontSize:19,bold:true,color:c||VIOLET_F});

  // ---------------------------------------------------------------- 1. ouverture
  {const sl=sombre(null); neuf(sl,9.3,1.55,0.78,CYAN,82);
   txt(sl,'JERUSALEM GEEKS  ·  JEREMIAH GEEKS',{x:M,y:1.5,w:8.4,h:0.4,fontSize:14,bold:true,color:VIOLET,charSpacing:4});
   txt(sl,[{text:'LE JEU ',options:{color:BLANC}},{text:'X',options:{color:CYAN}},{text:'O',options:{color:ORANGE}}],
       {x:M,y:2.1,w:8.4,h:1.3,fontSize:64,bold:true});
   txt(sl,'Séance ' + s.num + '  —  « ' + s.titre + ' »',{x:M,y:3.45,w:9.6,h:0.9,fontSize:27,bold:true,color:BLANC});
   txt(sl,s.date + '   ·   12 h - 14 h',{x:M,y:4.4,w:8.4,h:0.5,fontSize:18,color:GRIS_C});
   txt(sl,s.phrase,{x:M,y:5.2,w:10.0,h:0.9,fontSize:21,italic:true,color:CYAN,lineSpacing:26});
   sl.addNotes(s.notesOuverture||'Diapo affichée pendant que les élèves entrent.');}

  // ---------------------------------------------------------------- 2. le programme
  {const sl=claire('12 h 15'); surtitre(sl,"Le programme d'aujourd'hui");
   titre(sl,s.programmeTitre);
   const n=s.programme.length, gap=0.3, w=(W-2*M-gap*(n-1))/n;
   s.programme.forEach((it,i)=>{const x=M+i*(w+gap);
     carte(sl,x,2.5,w,2.9,{fond:it.fond||BLANC,trait:it.trait});
     pastille(sl,x+0.25,2.75,0.62,String(i+1),it.couleur||VIOLET_F,BLANC,22);
     txt(sl,it.titre,{x:x+0.25,y:3.55,w:w-0.5,h:0.5,fontSize:18,bold:true,color:it.couleur||ENCRE});
     txt(sl,it.texte,{x:x+0.25,y:4.1,w:w-0.5,h:1.2,fontSize:14,color:GRIS,lineSpacing:19});});
   bandeau(sl,s.programmeBandeau);
   sl.addNotes('Trois phrases, on ne détaille rien ici.');}

  // ---------------------------------------------------------------- 3-4. quiz flash
  {const sl=sombre('12 h 15 - 12 h 22'); neuf(sl,W-3.4,1.1,0.6,ORANGE,85);
   txt(sl,'🎯',{x:M,y:1.8,w:2.0,h:1.2,fontSize:56});
   txt(sl,'QUIZ FLASH',{x:M,y:2.9,w:9.6,h:1.0,fontSize:50,bold:true,color:BLANC});
   txt(sl,'6 questions, 7 minutes. Les cartes de couleur, comme d\'habitude.',
       {x:M,y:4.0,w:9.6,h:0.7,fontSize:20,color:ORANGE,italic:true});
   sl.addNotes('Je lis une question, « 3, 2, 1 — cartes en l\'air », je compte à vue, j\'explique en une phrase. Aucun résultat individuel n\'est commenté.');}
  {const sl=claire('12 h 16'); surtitre(sl,'Les six questions',ORANGE_F); titre(sl,'À lire une par une.');
   s.quiz.forEach((q,i)=>{const y=2.15+i*0.78;
     carte(sl,M,y,W-2*M,0.66,{fond:BLANC,trait:'E4E4EE'});
     pastille(sl,M+0.18,y+0.12,0.42,String(i+1),ORANGE_F,BLANC,14);
     txt(sl,q[0],{x:M+0.78,y:y+0.17,w:11.0,h:0.4,fontSize:15,color:ENCRE,fontFace:q[2]?MONO:SANS});});
   bandeau(sl,'Les réponses sur la diapo suivante — ne la montrez qu\'après.',ORANGE_F);
   sl.addNotes('Une question à la fois. On laisse 15 secondes, puis cartes en l\'air.');}
  {const sl=claire('12 h 20'); surtitre(sl,'Les réponses',VERT_F); titre(sl,'Une phrase d\'explication, pas plus.');
   s.quiz.forEach((q,i)=>{const y=2.15+i*0.78;
     carte(sl,M,y,W-2*M,0.66,{fond:'F2FAF5',trait:'B8E6CA'});
     pastille(sl,M+0.18,y+0.12,0.42,String(i+1),VERT_F,BLANC,14);
     txt(sl,q[1],{x:M+0.78,y:y+0.17,w:11.0,h:0.4,fontSize:15,bold:true,color:VERT_F});});
   sl.addNotes('On ne s\'attarde pas : 7 minutes au total pour le quiz.');}

  // ---------------------------------------------------------------- 5. le probleme du jour
  {const sl=sombre(s.heureLecon); neuf(sl,W-3.6,1.2,0.62,ROUGE,85);
   txt(sl,'LE PROBLÈME DU JOUR',{x:M,y:1.5,w:8.4,h:0.5,fontSize:17,bold:true,color:ROUGE,charSpacing:3});
   txt(sl,s.probleme,{x:M,y:2.2,w:10.4,h:2.4,fontSize:32,bold:true,color:BLANC,lineSpacing:40});
   txt(sl,s.problemeSous,{x:M,y:4.9,w:10.4,h:1.2,fontSize:19,color:CYAN,italic:true,lineSpacing:25});
   sl.addNotes(s.notesProbleme||'On montre le problème en vrai, sur l\'écran, avant toute explication.');}

  // ---------------------------------------------------------------- 6..n. la lecon
  s.lecon.forEach(d=>{
    const sl = d.sombre ? sombre(d.h) : claire(d.h);
    if (d.sur) surtitre(sl,d.sur,d.sombre?CYAN:(d.surCouleur||VIOLET_F));
    if (d.titre) titre(sl,d.titre,{color:d.sombre?BLANC:ENCRE,size:d.taille||32});
    if (d.code) bloc(sl,d.code,{y:d.codeY||2.3,h:d.codeH||2.0,taille:d.codeTaille||19,inter:d.codeInter||26});
    if (d.points) d.points.forEach((pt,i)=>{const y=(d.pointsY||4.6)+i*0.62;
      txt(sl,'▸',{x:M,y:y,w:0.35,h:0.4,fontSize:17,bold:true,color:ORANGE});
      txt(sl,pt,{x:M+0.42,y:y,w:11.4,h:0.5,fontSize:17,color:d.sombre?GRIS_C:ENCRE});});
    if (d.cle) {carte(sl,M,d.cleY||5.5,W-2*M,0.9,{fond:d.sombre?'20204A':'FFF6D8',trait:d.sombre?undefined:'D79A00',ombre:false});
      txt(sl,d.cle,{x:M+0.35,y:(d.cleY||5.5)+0.25,w:W-2*M-0.7,h:0.5,fontSize:18,bold:true,
        color:d.sombre?ORANGE:ORANGE_F,align:'center'});}
    if (d.notes) sl.addNotes(d.notes);});

  // ---------------------------------------------------------------- atelier
  if (s.atelier) {const sl=claire(s.atelier.h); surtitre(sl,'À vous',VERT_F); titre(sl,s.atelier.titre);
   s.atelier.etapes.forEach((e,i)=>{pastille(sl,M,2.5+i*0.82,0.52,String(i+1),VERT_F,BLANC,17);
     txt(sl,e,{x:M+0.8,y:2.58+i*0.82,w:11.2,h:0.5,fontSize:18,color:ENCRE});});
   bandeau(sl,s.atelier.bandeau,VERT_F);
   sl.addNotes(s.atelier.notes||'Je circule, je ne m\'assois pas, je ne touche aucun clavier.');}

  // ---------------------------------------------------------------- pause
  if (s.pause) {const sl=sombre(s.pause);
   txt(sl,'☕',{x:M,y:2.0,w:W-2*M,h:1.2,fontSize:54,align:'center'});
   txt(sl,'PAUSE',{x:M,y:3.25,w:W-2*M,h:0.9,fontSize:48,bold:true,color:BLANC,align:'center'});
   txt(sl,'10 minutes. Levez-vous, sortez, bougez.',{x:M,y:4.25,w:W-2*M,h:0.6,fontSize:20,color:CYAN,align:'center',italic:true});
   sl.addNotes('Pendant la pause : vérifier que GEEKS/mon_xo/jeu.py est ouvert sur chaque poste.');}

  // ---------------------------------------------------------------- le projet
  {const sl=claire(s.projet.h); surtitre(sl,'À vous — LE PROJET',VERT_F); titre(sl,s.projet.titre);
   bloc(sl,s.projet.rendu,{y:2.2,h:s.projet.renduH||2.6,taille:s.projet.renduTaille||13,inter:19});
   s.projet.etapes.forEach((e,i)=>txt(sl,e,{x:M,y:(2.2+(s.projet.renduH||2.6)+0.25)+i*0.44,w:W-2*M,h:0.4,
     fontSize:14,color:ENCRE}));
   bandeau(sl,s.projet.bandeau,VERT_F);
   sl.addNotes(s.projet.notes||'');}

  // ---------------------------------------------------------------- les erreurs
  {const sl=claire(s.projet.h); surtitre(sl,'Si l\'écran devient rouge',ORANGE_F); titre(sl,'Les erreurs du jour.');
   txt(sl,'Le rouge est une information. Lis-le, il te dit où chercher.',
       {x:M,y:1.95,w:W-2*M,h:0.4,fontSize:16,bold:true,color:ORANGE_F});
   s.erreurs.forEach((e,i)=>{const y=2.45+i*0.72;
     carte(sl,M,y,W-2*M,0.6,{fond:BLANC,trait:'E4E4EE'});
     txt(sl,e[0],{x:M+0.3,y:y+0.14,w:3.5,h:0.4,fontSize:14,bold:true,color:ROUGE_F,fontFace:MONO});
     txt(sl,e[1],{x:M+3.95,y:y+0.15,w:4.3,h:0.4,fontSize:13,color:GRIS});
     txt(sl,'→  '+e[2],{x:M+8.35,y:y+0.14,w:3.6,h:0.4,fontSize:13,bold:true,color:VERT_F});});
   sl.addNotes('Diapo à laisser affichée pendant tout l\'atelier.');}

  // ---------------------------------------------------------------- cloture
  {const sl=sombre('14 h'); neuf(sl,W-3.4,1.2,0.62,ORANGE,85);
   txt(sl,'📅  ' + s.cloture.sur,{x:M,y:1.7,w:8.4,h:0.5,fontSize:17,bold:true,color:ORANGE,charSpacing:3});
   txt(sl,s.cloture.titre,{x:M,y:2.4,w:10.4,h:1.8,fontSize:36,bold:true,color:BLANC,lineSpacing:46});
   txt(sl,s.cloture.texte,{x:M,y:4.5,w:10.4,h:1.2,fontSize:19,color:GRIS_C,lineSpacing:26});
   txt(sl,'🚀  À samedi, les Geeks !',{x:M,y:5.8,w:9.0,h:0.7,fontSize:23,color:CYAN,italic:true});
   sl.addNotes('On laisse la diapo affichée pendant la sortie.');}

  const sortie = BASE + s.dossier + '/a-projeter/seance-' + s.num + '-projection.pptx';
  return p.writeFile({fileName: sortie}).then(()=>console.log('  S' + s.num + ' -> ' + sortie.split('/').slice(-1)[0]));
}
module.exports = {creer};
