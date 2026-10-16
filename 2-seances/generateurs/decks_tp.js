const P = require('pptxgenjs');
const W=13.3,H=7.5,M=0.7;
const NUIT='12122A',CLAIR='F7F7FB',BLANC='FFFFFF',ENCRE='14142B',GRIS='5A5A72',GRIS_C='A8A8C0';
const CYAN='4FC3F7',ORANGE='FFB74D',ORANGE_F='A65D00',VIOLET='B06FD8',VIOLET_F='6B2D8F',VERT_F='0C5C29';
const SANS='Calibri',MONO='Courier New';

function deck(d) {
  const p=new P(); p.layout='LAYOUT_WIDE'; p.title='TP - seance '+d.num;
  const txt=(s,t,o)=>s.addText(t,Object.assign({isTextBox:true,margin:0,fontFace:SANS,valign:'top'},o));
  const neuf=(s,x,y,t,c,o)=>{for(let i=0;i<9;i++)s.addShape(p.ShapeType.roundRect,{x:x+(i%3)*t*1.35,
    y:y+Math.floor(i/3)*t*1.35,w:t,h:t,fill:{color:c,transparency:o===undefined?60:o},line:{type:'none'},rectRadius:0.02});};
  const carte=(s,x,y,w,h,o)=>{o=o||{};s.addShape(p.ShapeType.roundRect,{x,y,w,h,rectRadius:0.08,
    fill:{color:o.fond||BLANC},line:o.trait?{color:o.trait,width:1.5}:{type:'none'}});};
  const pastille=(s,x,y,dd,t,f,c,ta)=>{s.addShape(p.ShapeType.ellipse,{x,y,w:dd,h:dd,fill:{color:f},line:{type:'none'}});
    txt(s,t,{x,y,w:dd,h:dd,fontSize:ta||18,bold:true,color:c||BLANC,align:'center',valign:'middle'});};

  {const s=p.addSlide(); s.background={color:NUIT}; neuf(s,9.3,1.55,0.78,CYAN,82);
   txt(s,'JEREMIAH GEEKS',{x:M,y:1.5,w:8.4,h:0.4,fontSize:14,bold:true,color:VIOLET,charSpacing:4});
   txt(s,d.emoji+'  '+d.titre,{x:M,y:2.1,w:9.4,h:1.4,fontSize:48,bold:true,color:BLANC});
   txt(s,d.date+'   ·   12 h - 14 h',{x:M,y:3.7,w:8.4,h:0.5,fontSize:19,color:GRIS_C});
   txt(s,d.phrase,{x:M,y:4.6,w:10.2,h:1.4,fontSize:22,italic:true,color:CYAN,lineSpacing:28});
   s.addNotes(d.notes1||'');}

  {const s=p.addSlide(); s.background={color:CLAIR};
   txt(s,'COMMENT ON TRAVAILLE AUJOURD\'HUI',{x:M,y:0.5,w:W-2*M,h:0.4,fontSize:13,bold:true,color:VIOLET_F,charSpacing:3});
   txt(s,d.reglesTitre,{x:M,y:0.95,w:W-2*M,h:0.9,fontSize:34,bold:true,color:ENCRE});
   d.regles.forEach((r,i)=>{const y=2.2+i*0.95;
     carte(s,M,y,W-2*M,0.82,{fond:BLANC,trait:'E4E4EE'});
     pastille(s,M+0.22,y+0.17,0.48,String(i+1),ORANGE_F,BLANC,15);
     txt(s,r,{x:M+0.9,y:y+0.24,w:11.2,h:0.45,fontSize:17,color:ENCRE});});
   s.addNotes('On lit les règles à voix haute, et on lance. Deux minutes maximum.');}

  {const s=p.addSlide(); s.background={color:CLAIR};
   txt(s,'OÙ DEVRAIS-TU EN ÊTRE ?',{x:M,y:0.5,w:W-2*M,h:0.4,fontSize:13,bold:true,color:VIOLET_F,charSpacing:3});
   txt(s,'Le tableau de bord',{x:M,y:0.95,w:W-2*M,h:0.9,fontSize:34,bold:true,color:ENCRE});
   d.bord.forEach((b,i)=>{const col=i%2,lig=Math.floor(i/2),x=M+col*6.15,y=2.1+lig*1.15;
     carte(s,x,y,5.75,0.98,{fond:BLANC,trait:'E0E0EA'});
     txt(s,b[0],{x:x+0.25,y:y+0.3,w:1.6,h:0.4,fontSize:17,bold:true,color:ORANGE_F,fontFace:MONO});
     txt(s,b[1],{x:x+1.95,y:y+0.3,w:3.6,h:0.45,fontSize:15,color:ENCRE});});
   txt(s,d.bordBas,{x:M,y:H-1.5,w:W-2*M,h:0.7,fontSize:18,bold:true,color:VIOLET_F});
   s.addNotes('Diapo à laisser affichée pendant tout le TP.');}

  {const s=p.addSlide(); s.background={color:NUIT}; neuf(s,W-3.4,1.2,0.62,ORANGE,85);
   txt(s,'POUR FINIR',{x:M,y:1.6,w:8.4,h:0.5,fontSize:17,bold:true,color:ORANGE,charSpacing:3});
   txt(s,d.finTitre,{x:M,y:2.3,w:10.4,h:1.8,fontSize:36,bold:true,color:BLANC,lineSpacing:44});
   txt(s,d.finTexte,{x:M,y:4.4,w:10.4,h:1.4,fontSize:19,color:GRIS_C,lineSpacing:26});
   s.addNotes(d.notesFin||'');}

  return p.writeFile({fileName:'/home/user/python-learning/2-seances/'+d.dossier+'/a-projeter/seance-'+d.num+'-projection.pptx'})
          .then(f=>console.log('  TP S'+d.num+' écrit'));
}

(async()=>{
await deck({num:8,dossier:'S08-tp-le-plateau',emoji:'🛠️',titre:'TP n°2',date:'samedi 31 octobre 2026',
 phrase:"Le plateau vivant. Deux heures, seul, pour que tout devienne solide.",
 reglesTitre:'Cinq règles, et on part.',
 regles:['Tu travailles SEUL, à ton rythme. Le professeur passe : il ne fera pas à ta place.',
         'Tu coches chaque exercice réussi sur ta feuille. Elle est à toi, tu l\'emportes.',
         'F5 après chaque changement. Ctrl + S après chaque partie.',
         'Bloqué plus de 5 minutes ? Tu passes à la suite, et tu y reviendras.',
         'Les encadrés jaunes ⭐ sont facultatifs : personne n\'est en retard sans eux.'],
 bord:[['12 h 15','Partie 0 — le fichier est créé'],['12 h 40','Partie 1 — les listes'],
       ['13 h 00','Partie 2 — l\'indice  case - 1'],['13 h 15','Partie 3 — le plateau qui vit'],
       ['13 h 50','Partie 4 — LE PROJET, validé'],['13 h 55','Partie 5 — la chasse aux bugs']],
 bordBas:'En retard sur l\'horloge ? Avance quand même : la partie 4 est la seule obligatoire.',
 finTitre:'À 13 h 50, tout le monde\ns\'arrête et sauvegarde.',
 finTexte:"On remplit le bilan de la dernière page, et on repart avec le code officiel.\nSamedi prochain : and et or — le code va rétrécir.",
 notes1:"Le seul objectif non négociable : que chacun ait terminé la partie 4."});

await deck({num:12,dossier:'S12-tp-le-tournoi',emoji:'🏆',titre:'LE TOURNOI',date:'samedi 28 novembre 2026',
 phrase:"Votre jeu est fini. On le teste, on le fignole — et on joue.",
 reglesTitre:'Les règles du tournoi.',
 regles:['On joue sur le programme de l\'un des deux joueurs, tiré au sort.',
         'Si le programme plante pendant le match, on rejoue sur l\'autre. Un jeu solide, ça compte.',
         'Un match nul se rejoue, et c\'est l\'autre qui commence.',
         'Celui qui perd devient ARBITRE du match suivant.',
         'Tout le monde joue. Même si ton jeu ne marche pas encore.'],
 bord:[['12 h 45','Les 8 scénarios de test'],['13 h 10','Les réparations'],
       ['13 h 10','Pause + TIRAGE AU SORT'],['13 h 20','Une finition, vite'],
       ['13 h 25','LE TOURNOI'],['13 h 55','Bilan des deux mois, et photo']],
 bordBas:'Les 8 scénarios d\'abord. Un jeu non testé n\'est pas un jeu fini.',
 finTitre:'Deux questions,\net c\'est fini.',
 finTexte:"De quoi es-tu le plus fier dans ton jeu ?\nQu'est-ce que tu aimerais qu'il sache faire, et qu'il ne sait pas encore ?\n\nLa deuxième réponse décidera du programme de décembre.",
 notesFin:"Ramassez vraiment ces réponses : c'est le programme de décembre, écrit par eux."});
})();
