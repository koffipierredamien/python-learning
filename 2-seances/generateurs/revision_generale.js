// La revision generale : le quiz, mais avec des ateliers au clavier entre
// les manches. Se termine pile sur le besoin de la boucle.
const P = require('pptxgenjs');
const BASE = require('path').resolve(__dirname, '..') + '/';
const W = 13.3, H = 7.5, M = 0.7;
const NUIT='12122A', NUIT2='20204A', CLAIR='F7F7FB', BLANC='FFFFFF', ENCRE='14142B';
const GRIS='5A5A72', GRIS_C='A8A8C0', CYAN='4FC3F7', ORANGE='FFB74D', ORANGE_F='A65D00';
const VIOLET='B06FD8', VIOLET_F='6B2D8F', VERT='2FB765', VERT_F='0C5C29', ROUGE='FF6B6B';
const SANS='Calibri', MONO='Courier New';

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
  p.title = s.titre;

  const txt=(sl,t,o)=>sl.addText(t,Object.assign({isTextBox:true,margin:0,fontFace:SANS,valign:'top'},o));
  const neuf=(sl,x,y,t,c,o)=>{for(let i=0;i<9;i++)sl.addShape(p.ShapeType.roundRect,{
    x:x+(i%3)*t*1.35,y:y+Math.floor(i/3)*t*1.35,w:t,h:t,
    fill:{color:c,transparency:o===undefined?60:o},line:{type:'none'},rectRadius:0.02});};
  const pied=(sl,h,sombre)=>{if(h)txt(sl,h,{x:W-3.4,y:H-0.74,w:2.7,h:0.34,fontFace:MONO,fontSize:11,
    color:sombre?GRIS_C:GRIS,align:'right'});neuf(sl,W-0.66,H-0.70,0.075,sombre?CYAN:VIOLET_F,sombre?55:70);};
  const sombre=(h)=>{const sl=p.addSlide();sl.background={color:NUIT};pied(sl,h,true);return sl;};
  const claire=(h)=>{const sl=p.addSlide();sl.background={color:CLAIR};pied(sl,h,false);return sl;};
  const carte=(sl,x,y,w,h,o)=>{o=o||{};sl.addShape(p.ShapeType.roundRect,{x,y,w,h,rectRadius:0.08,
    fill:{color:o.fond||BLANC},line:o.trait?{color:o.trait,width:1.5}:{type:'none'},
    shadow:o.ombre===false?undefined:{type:'outer',color:'20204A',blur:10,offset:2,angle:90,opacity:0.12}});};
  const pastille=(sl,x,y,d,t,f,c,ta)=>{sl.addShape(p.ShapeType.ellipse,{x,y,w:d,h:d,fill:{color:f},line:{type:'none'}});
    txt(sl,t,{x,y,w:d,h:d,fontSize:ta||20,bold:true,color:c||BLANC,align:'center',valign:'middle'});};
  const bloc=(sl,code,o)=>{o=o||{};const y=o.y,h=o.h,w=o.w||(W-2*M),x=o.x===undefined?M:o.x;
    carte(sl,x,y,w,h,{fond:o.fond||NUIT2,ombre:false});
    txt(sl,code,{x:x+0.35,y:y+0.22,w:w-0.7,h:h-0.44,fontSize:o.taille||18,fontFace:MONO,
      color:o.couleur||CYAN,lineSpacing:o.inter||(o.taille||18)*1.35});};

  // ================================================================ ouverture
  {const sl=sombre(null); neuf(sl,9.6,1.6,0.8,CYAN,82);
   txt(sl,'SÉANCE 10  ·  SAMEDI 14 NOVEMBRE',{x:M,y:1.5,w:8.6,h:0.4,fontSize:14,bold:true,color:VIOLET,charSpacing:4});
   txt(sl,'RÉVISION GÉNÉRALE',{x:M,y:2.05,w:9.2,h:1.3,fontSize:54,bold:true,color:BLANC});
   txt(sl,'Cinq manches. Des cartes en l\'air, et les mains sur le clavier.',
       {x:M,y:3.5,w:9.0,h:0.8,fontSize:21,color:GRIS_C,lineSpacing:27});
   txt(sl,'Tout ce qu\'on sait depuis septembre — et à la fin,\nce qui nous manque encore.',
       {x:M,y:4.5,w:9.4,h:1.2,fontSize:20,italic:true,color:CYAN,lineSpacing:27});
   sl.addNotes('Affichée pendant qu\'ils s\'installent. Thonny ouvert sur chaque poste, '
     + 'un fichier neuf : revision.py. On ne touche pas au jeu aujourd\'hui.');}

  // ================================================================ la regle
  {const sl=claire('12 h 17');
   txt(sl,'COMMENT ON JOUE',{x:M,y:0.5,w:8,h:0.4,fontSize:14,bold:true,color:VIOLET_F,charSpacing:3});
   txt(sl,'Deux sortes de questions.',{x:M,y:1.0,w:11,h:0.8,fontSize:34,bold:true,color:ENCRE});
   const w=(W-2*M-0.4)/2;
   carte(sl,M,2.1,w,4.0,{fond:BLANC,trait:VIOLET_F});
   pastille(sl,M+0.35,2.4,0.7,'1',VIOLET_F,BLANC,24);
   txt(sl,'LA CARTE',{x:M+1.25,y:2.52,w:w-1.6,h:0.45,fontSize:21,bold:true,color:VIOLET_F});
   txt(sl,'Je projette, tu réfléchis, et tout le monde lève sa carte EN MÊME TEMPS, au signal.\n\nPersonne ne parle. Personne ne se retourne.',
       {x:M+0.35,y:3.3,w:w-0.7,h:1.6,fontSize:16,color:GRIS,lineSpacing:22});
   CARTES.forEach((k,i)=>{txt(sl,k.s+'  '+k.nom,{x:M+0.35+(i%2)*(w/2-0.2),y:5.0+Math.floor(i/2)*0.45,
     w:w/2-0.3,h:0.4,fontSize:15,bold:true,color:k.c});});
   carte(sl,M+w+0.4,2.1,w,4.0,{fond:BLANC,trait:VERT_F});
   pastille(sl,M+w+0.75,2.4,0.7,'2',VERT_F,BLANC,24);
   txt(sl,'LE CLAVIER',{x:M+w+1.65,y:2.52,w:w-1.6,h:0.45,fontSize:21,bold:true,color:VERT_F});
   txt(sl,'Tu tapes le code projeté. Tu PRÉDIS ce qu\'il va faire — carte en l\'air. Et seulement après, tu lances.',
       {x:M+w+0.75,y:3.3,w:w-0.7,h:1.3,fontSize:16,color:GRIS,lineSpacing:22});
   txt(sl,'⚠  Prédire AVANT de lancer, c\'est tout l\'exercice.\nCelui qui lance d\'abord n\'apprend rien.',
       {x:M+w+0.75,y:4.75,w:w-0.9,h:1.1,fontSize:16,bold:true,color:ORANGE_F,lineSpacing:22});
   sl.addNotes('Insistez sur la prédiction : c\'est elle qui révèle ce qui est compris. '
     + 'Un élève qui lance avant de prédire se prive de l\'information.');}

  // ================================================================ les manches
  s.manches.forEach((m,mi)=>{

    // ---- separateur
    {const sl=sombre(m.heure); neuf(sl,W-3.4,1.2,0.62,ORANGE,85);
     txt(sl,'MANCHE '+(mi+1)+'  ·  '+m.duree,{x:M,y:1.7,w:8.4,h:0.5,fontSize:16,bold:true,color:ORANGE,charSpacing:3});
     txt(sl,m.titre,{x:M,y:2.4,w:10.4,h:1.6,fontSize:44,bold:true,color:BLANC,lineSpacing:52});
     txt(sl,m.sous,{x:M,y:4.3,w:10.4,h:1.4,fontSize:21,color:GRIS_C,lineSpacing:28});
     sl.addNotes(m.note||'');}

    // ---- les questions a la carte
    (m.qcm||[]).forEach((q,i)=>{
      const n=i+1, bonne=CARTES[q.bonne];
      {const sl=sombre(null);
       txt(sl,'MANCHE '+(mi+1)+'  ·  CARTE '+n,{x:M,y:0.5,w:6,h:0.4,fontSize:14,bold:true,color:ORANGE,charSpacing:3});
       carte(sl,W-M-1.25,0.38,1.25,0.62,{fond:NUIT2,ombre:false});
       txt(sl,'20 s',{x:W-M-1.25,y:0.38,w:1.25,h:0.62,fontSize:18,bold:true,color:ORANGE,align:'center',valign:'middle'});
       let y=1.15;
       if(q.code){const h=0.42*q.code.split('\n').length+0.5;
         bloc(sl,q.code,{y:y,h:h,taille:q.taille||22});
         y+=h+0.3;}
       txt(sl,q.consigne,{x:M,y:y,w:W-2*M,h:0.6,fontSize:q.code?22:30,bold:true,color:BLANC,lineSpacing:34});
       y+=(q.code?0.75:1.0);
       const gap=0.18, hc=(H-0.95-y-3*gap)/4;
       q.options.forEach((o,j)=>{const k=CARTES[j], yy=y+j*(hc+gap);
         carte(sl,M,yy,W-2*M,hc,{fond:'1B1B38',ombre:false});
         txt(sl,k.s,{x:M+0.3,y:yy,w:0.5,h:hc,fontSize:20,bold:true,color:k.c,valign:'middle'});
         txt(sl,o,{x:M+1.0,y:yy,w:W-2*M-1.3,h:hc,fontSize:18,color:BLANC,valign:'middle'});});
       sl.addNotes(q.note||'20 secondes, puis « cartes en l\'air ! ».');}

      {const sl=claire(null);
       txt(sl,'LA RÉPONSE',{x:M,y:0.5,w:6,h:0.4,fontSize:14,bold:true,color:VIOLET_F,charSpacing:3});
       let y=1.05;
       if(q.code){const h=0.25*q.code.split('\n').length+0.35;
         carte(sl,M,y,W-2*M,h,{fond:'EFEFF6',ombre:false});
         txt(sl,q.code,{x:M+0.35,y:y+0.17,w:W-2*M-0.7,h:h-0.34,fontSize:14,fontFace:MONO,color:ENCRE,lineSpacing:18});
         y+=h+0.12;}
       txt(sl,q.consigne,{x:M,y:y,w:W-2*M,h:0.4,fontSize:16,color:GRIS});
       y+=0.6;
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
       sl.addNotes(q.noteReponse||'Une phrase, pas plus. On ne commente jamais qui s\'est trompé.');}
    });

    // ---- l'atelier : le code a taper, puis les temps, puis la correction
    if(m.atelier){const a=m.atelier;
     const entete=(sl)=>{
       txt(sl,'MANCHE '+(mi+1)+'  ·  AU CLAVIER',{x:M,y:0.5,w:7,h:0.4,fontSize:14,bold:true,color:VERT,charSpacing:3});
       carte(sl,W-M-1.6,0.38,1.6,0.62,{fond:VERT,ombre:false});
       txt(sl,a.duree,{x:W-M-1.6,y:0.38,w:1.6,h:0.62,fontSize:17,bold:true,color:BLANC,align:'center',valign:'middle'});
       txt(sl,a.titre,{x:M,y:1.02,w:W-2*M-1.8,h:0.75,fontSize:32,bold:true,color:BLANC});};

     // (a) le code a taper -- seulement s'il y en a un
     if(a.code){const sl=sombre(null); entete(sl);
      const ta=a.taille||20, nl=a.code.split('\n').length;
      const h=Math.min(4.3, nl*ta*1.38/72 + 0.5);
      bloc(sl,a.code,{y:2.05,h:h,taille:ta,inter:ta*1.38});
      carte(sl,M,6.25,W-2*M,0.72,{fond:'1B1B38',ombre:false});
      txt(sl,'⌨  Tape-le tel quel, dans un fichier neuf.  ET NE LANCE PAS ENCORE.',
          {x:M+0.4,y:6.25,w:W-2*M-0.8,h:0.72,fontSize:18,bold:true,color:ORANGE,valign:'middle'});
      sl.addNotes(a.noteCode||'Laissez la diapo affichée pendant toute la frappe. Circulez, ne corrigez pas : la frappe fait partie de l\'exercice.');}

     // (b) les trois temps
     {const sl=sombre(null); entete(sl);
      const n=a.temps.length, gap=0.25, y0=2.05;
      const hc=Math.min(1.25,(H-1.1-y0-(n-1)*gap)/n);
      a.temps.forEach((t,j)=>{const yy=y0+j*(hc+gap);
        carte(sl,M,yy,W-2*M,hc,{fond:j===n-1?'2A1F3D':'1B1B38',ombre:false,
          trait:j===n-1?VIOLET:undefined});
        pastille(sl,M+0.32,yy+(hc-0.58)/2,0.58,String(j+1),j===n-1?ORANGE:VERT,j===n-1?ENCRE:BLANC,19);
        txt(sl,t,{x:M+1.15,y:yy,w:W-2*M-1.5,h:hc,fontSize:a.tailleTemps||18,color:BLANC,
          valign:'middle',lineSpacing:(a.tailleTemps||18)*1.3});});
      sl.addNotes(a.note||'');}

     // (c) la correction
     {const sl=claire(null);
      txt(sl,'LA CORRECTION  ·  '+a.titre.toUpperCase(),{x:M,y:0.5,w:10,h:0.4,fontSize:14,bold:true,color:VERT_F,charSpacing:3});
      let y=1.0;
      const nl=a.corrige.split('\n').length, hmax=a.variante?2.95:3.9;
      let tc=a.tailleCor||16, h=nl*tc*1.35/72 + 0.45;
      if(h>hmax){tc=Math.floor((hmax-0.45)*72/(nl*1.35)); h=nl*tc*1.35/72 + 0.45;}
      carte(sl,M,y,W-2*M,h,{fond:NUIT,ombre:false});
      txt(sl,a.corrige,{x:M+0.35,y:y+0.22,w:W-2*M-0.7,h:h-0.44,fontSize:tc,fontFace:MONO,
        color:CYAN,lineSpacing:tc*1.35});
      y+=h+0.28;
      if(a.variante){carte(sl,M,y,W-2*M,0.72,{fond:'EFEFF6',ombre:false});
        txt(sl,a.variante,{x:M+0.35,y:y,w:W-2*M-0.7,h:0.72,fontSize:15,color:GRIS,valign:'middle'});
        y+=0.9;}
      const hl=Math.max(1.4,H-0.9-y);
      carte(sl,M,y,W-2*M,hl,{fond:'F2FAF5',trait:VERT});
      txt(sl,'LA LEÇON',{x:M+0.4,y:y+0.18,w:4,h:0.32,fontSize:12,bold:true,color:VERT_F,charSpacing:2});
      txt(sl,a.lecon,{x:M+0.4,y:y+0.58,w:W-2*M-0.8,h:hl-0.72,fontSize:17,color:ENCRE,lineSpacing:23});
      sl.addNotes(a.noteCorrige||'');}
    }
  });

  // ================================================================ bascule
  {const sl=sombre(s.bascule.heure); neuf(sl,W-3.4,1.2,0.62,ORANGE,85);
   txt(sl,'ET MAINTENANT',{x:M,y:1.5,w:8.4,h:0.5,fontSize:16,bold:true,color:ORANGE,charSpacing:3});
   txt(sl,s.bascule.titre,{x:M,y:2.1,w:10.8,h:2.0,fontSize:40,bold:true,color:BLANC,lineSpacing:50});
   txt(sl,s.bascule.texte,{x:M,y:4.3,w:10.8,h:1.1,fontSize:21,color:GRIS_C,lineSpacing:28});
   const nl=s.bascule.tableau.split('\n').length, h=0.36*nl+0.45, yy=6.65-h;
   carte(sl,M,yy,W-2*M,h,{fond:NUIT2,ombre:false});
   txt(sl,s.bascule.tableau,{x:M+0.35,y:yy+0.22,w:W-2*M-0.7,h:h-0.44,fontSize:19,fontFace:MONO,
     color:ORANGE,lineSpacing:26});
   sl.addNotes(s.bascule.note||'');}

  const sortie = BASE + s.dossier + '/a-projeter/revision-generale.pptx';
  return p.writeFile({fileName: sortie}).then(()=>console.log('  -> ' + sortie.split('/').slice(-2).join('/')));
}
module.exports = {creer};
