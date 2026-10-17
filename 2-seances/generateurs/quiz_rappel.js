// Le diaporama du quiz flash d'ouverture : une question par diapo,
// sa reponse juste apres. C'est le rituel des cartes de couleur.
const P = require('pptxgenjs');
const BASE = require('path').resolve(__dirname, '..') + '/';
const W = 13.3, H = 7.5, M = 0.7;
const NUIT='12122A', CLAIR='F7F7FB', BLANC='FFFFFF', ENCRE='14142B';
const GRIS='5A5A72', GRIS_C='A8A8C0', CYAN='4FC3F7', ORANGE='FFB74D', ORANGE_F='A65D00';
const VIOLET='B06FD8', VIOLET_F='6B2D8F', VERT='2FB765', VERT_F='0C5C29', ROUGE='FF6B6B';
const SANS='Calibri', MONO='Courier New';

// les quatre cartes, dans l'ordre ou elles sont proposees
const CARTES = [
  {s:'▲', nom:'ROUGE',  c:ROUGE},
  {s:'◆', nom:'BLEUE',  c:CYAN},
  {s:'●', nom:'ORANGE', c:ORANGE},
  {s:'■', nom:'VERTE',  c:VERT},
];

function creer(s) {
  const p = new P();
  p.layout = 'LAYOUT_WIDE';
  p.author = 'Jerusalem Geeks & Jeremiah Geeks';
  p.title = 'Quiz flash — séance ' + s.num;

  const txt=(sl,t,o)=>sl.addText(t,Object.assign({isTextBox:true,margin:0,fontFace:SANS,valign:'top'},o));
  const neuf=(sl,x,y,t,c,o)=>{for(let i=0;i<9;i++)sl.addShape(p.ShapeType.roundRect,{
    x:x+(i%3)*t*1.35,y:y+Math.floor(i/3)*t*1.35,w:t,h:t,
    fill:{color:c,transparency:o===undefined?60:o},line:{type:'none'},rectRadius:0.02});};
  const pied=(sl,h,sombre)=>{if(h)txt(sl,h,{x:W-3.1,y:H-0.74,w:2.4,h:0.34,fontFace:MONO,fontSize:11,
    color:sombre?GRIS_C:GRIS,align:'right'});neuf(sl,W-0.66,H-0.70,0.075,sombre?CYAN:VIOLET_F,sombre?55:70);};
  const sombre=(h)=>{const sl=p.addSlide();sl.background={color:NUIT};pied(sl,h,true);return sl;};
  const claire=(h)=>{const sl=p.addSlide();sl.background={color:CLAIR};pied(sl,h,false);return sl;};
  const carte=(sl,x,y,w,h,o)=>{o=o||{};sl.addShape(p.ShapeType.roundRect,{x,y,w,h,rectRadius:0.08,
    fill:{color:o.fond||BLANC},line:o.trait?{color:o.trait,width:1.5}:{type:'none'},
    shadow:o.ombre===false?undefined:{type:'outer',color:'20204A',blur:10,offset:2,angle:90,opacity:0.12}});};

  // ------------------------------------------------------------ 1. ouverture
  {const sl=sombre(null); neuf(sl,9.6,1.6,0.8,CYAN,82);
   txt(sl,'SÉANCE '+s.num+'  ·  '+s.surtitre.toUpperCase(),
       {x:M,y:1.55,w:8.6,h:0.4,fontSize:14,bold:true,color:VIOLET,charSpacing:4});
   txt(sl,'QUIZ FLASH',{x:M,y:2.15,w:8.6,h:1.2,fontSize:60,bold:true,color:BLANC});
   txt(sl,'6 questions, 7 minutes.  '+s.sousTitre,
       {x:M,y:3.5,w:8.8,h:0.9,fontSize:20,color:GRIS_C,lineSpacing:26});
   CARTES.forEach((k,i)=>{const y=4.5+i*0.52;
     txt(sl,String(i+1),{x:M,y:y,w:0.3,h:0.42,fontSize:16,bold:true,color:GRIS_C});
     txt(sl,k.s,{x:M+0.35,y:y-0.02,w:0.4,h:0.44,fontSize:18,bold:true,color:k.c});
     txt(sl,'lève ta carte '+k.nom,{x:M+0.85,y:y,w:5,h:0.42,fontSize:16,bold:true,color:k.c});});
   sl.addNotes("Affichée pendant que les élèves s'installent. On rappelle la règle : "
     +"tout le monde lève sa carte EN MÊME TEMPS, au signal. Personne ne parle. "
     +"C'est ce qui permet de voir d'un coup d'œil qui a compris, sans interroger personne.");}

  // ------------------------------------------------------------ les 6 questions
  s.questions.forEach((q,i)=>{
    const n=i+1, bonne=CARTES[q.bonne];

    // ---- la question
    {const sl=sombre(null);
     txt(sl,'QUESTION '+n+' / 6',{x:M,y:0.5,w:6,h:0.4,fontSize:14,bold:true,color:ORANGE,charSpacing:3});
     carte(sl,W-M-1.25,0.38,1.25,0.62,{fond:'20204A',ombre:false});
     txt(sl,'20 s',{x:W-M-1.25,y:0.38,w:1.25,h:0.62,fontSize:18,bold:true,color:ORANGE,
       align:'center',valign:'middle'});
     let y=1.15;
     if(q.code){const h=0.42*q.code.split('\n').length+0.5;
       carte(sl,M,y,W-2*M,h,{fond:'20204A',ombre:false});
       txt(sl,q.code,{x:M+0.35,y:y+0.25,w:W-2*M-0.7,h:h-0.5,fontSize:q.taille||22,fontFace:MONO,
         color:CYAN,lineSpacing:(q.taille||22)*1.3});
       y+=h+0.3;}
     txt(sl,q.consigne,{x:M,y:y,w:W-2*M,h:0.6,fontSize:q.code?22:30,bold:true,color:BLANC,lineSpacing:34});
     y+=(q.code?0.75:1.0);
     const gap=0.18, hc=(H-0.95-y-3*gap)/4;
     q.options.forEach((o,j)=>{const k=CARTES[j], yy=y+j*(hc+gap);
       carte(sl,M,yy,W-2*M,hc,{fond:'1B1B38',ombre:false});
       txt(sl,k.s,{x:M+0.3,y:yy,w:0.5,h:hc,fontSize:20,bold:true,color:k.c,valign:'middle'});
       txt(sl,o,{x:M+1.0,y:yy,w:W-2*M-1.3,h:hc,fontSize:18,color:BLANC,valign:'middle'});});
     sl.addNotes(q.note||'On lit la question à voix haute, on laisse 20 secondes, puis « cartes en l\'air ! ».');}

    // ---- la reponse
    {const sl=claire('réponse '+n);
     txt(sl,'RÉPONSE '+n,{x:M,y:0.5,w:6,h:0.4,fontSize:14,bold:true,color:VIOLET_F,charSpacing:3});
     let y=1.05;
     if(q.code){const h=0.25*q.code.split('\n').length+0.35;
       carte(sl,M,y,W-2*M,h,{fond:'EFEFF6',ombre:false});
       txt(sl,q.code,{x:M+0.35,y:y+0.17,w:W-2*M-0.7,h:h-0.34,fontSize:14,fontFace:MONO,
         color:ENCRE,lineSpacing:18});
       y+=h+0.12;}
     txt(sl,q.consigne,{x:M,y:y,w:W-2*M,h:0.4,fontSize:16,color:GRIS});
     y+=0.6;
     // la bonne reponse
     carte(sl,M,y,W-2*M,1.3,{fond:BLANC,trait:bonne.c});
     txt(sl,bonne.s+'   '+bonne.nom,{x:M+0.4,y:y+0.14,w:3.2,h:0.42,fontSize:18,bold:true,color:bonne.c});
     txt(sl,q.options[q.bonne],{x:M+0.4,y:y+0.6,w:W-2*M-3.6,h:0.6,fontSize:25,bold:true,color:ENCRE});
     sl.addShape(p.ShapeType.roundRect,{x:W-M-2.65,y:y+0.17,w:2.25,h:0.46,rectRadius:0.08,
       fill:{color:VERT},line:{type:'none'}});
     txt(sl,'LA BONNE RÉPONSE',{x:W-M-2.65,y:y+0.17,w:2.25,h:0.46,fontSize:11,bold:true,
       color:BLANC,align:'center',valign:'middle',charSpacing:1});
     y+=1.52;
     const hp=H-0.88-y;
     carte(sl,M,y,W-2*M,hp,{fond:'FFFAF0',trait:ORANGE_F});
     txt(sl,'POURQUOI',{x:M+0.4,y:y+0.2,w:4,h:0.34,fontSize:12,bold:true,color:ORANGE_F,charSpacing:2});
     txt(sl,q.pourquoi,{x:M+0.4,y:y+0.62,w:W-2*M-0.8,h:hp-0.8,fontSize:17,color:ENCRE,lineSpacing:23});
     sl.addNotes(q.noteReponse||'Une phrase d\'explication, pas plus. On ne commente jamais qui s\'est trompé.');}
  });

  // ------------------------------------------------------------ la bascule
  {const sl=sombre('12 h 22'); neuf(sl,W-3.4,1.2,0.62,ORANGE,85);
   txt(sl,'ET MAINTENANT',{x:M,y:1.6,w:8.4,h:0.5,fontSize:16,bold:true,color:ORANGE,charSpacing:3});
   txt(sl,s.bascule.titre,{x:M,y:2.0,w:10.6,h:1.9,fontSize:36,bold:true,color:BLANC,lineSpacing:46});
   txt(sl,s.bascule.texte,{x:M,y:4.1,w:10.6,h:1.0,fontSize:20,color:GRIS_C,lineSpacing:27});
   if(s.bascule.tableau){
     const nl=s.bascule.tableau.split('\n').length, h=0.34*nl+0.4, y=6.6-h;
     carte(sl,M,y,W-2*M,h,{fond:'20204A',ombre:false});
     txt(sl,s.bascule.tableau,{x:M+0.35,y:y+0.2,w:W-2*M-0.7,h:h-0.4,fontSize:17,fontFace:MONO,
       color:CYAN,lineSpacing:24});}
   sl.addNotes(s.bascule.note||'On enchaîne tout de suite sur la leçon. Le quiz ne se commente pas.');}

  const sortie = BASE + s.dossier + '/a-projeter/quiz-rappel.pptx';
  return p.writeFile({fileName: sortie})
          .then(()=>console.log('  S'+s.num+' -> '+s.dossier+'/a-projeter/quiz-rappel.pptx'));
}
module.exports = {creer};
