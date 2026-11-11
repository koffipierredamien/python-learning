# -*- coding: utf-8 -*-
"""Mission autonome n 1 : la feuille de l'eleve et celle de l'enseignant.
   Format different des exercices de maison : ici on ne donne PAS les etapes."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import exos_maison as E

ICI = os.path.join(E.RACINE, "missions-autonomes")
PY = os.path.join(ICI, "mission-1-ascenseur-corrige.py")

COMMUN = """
 html,*{-webkit-print-color-adjust:exact;print-color-adjust:exact;box-sizing:border-box}
 @page{size:A4 portrait;margin:0}
 body{margin:0;font-family:"Trebuchet MS",Verdana,sans-serif;color:#14142b;background:#fff;
      font-size:9.4pt;padding:6mm 8mm 4mm}
 .saut{page-break-before:always}
 .mono{font-family:"Courier New",monospace;font-weight:bold;background:#f0f0f6;
       padding:.3mm 1mm;border-radius:1mm}
 .band{background:#12122a;color:#fff;border-radius:3mm;padding:3.2mm 5mm;margin-bottom:2.8mm}
 .band .k{font-size:8.8pt;letter-spacing:1.6pt;color:#ffb74d;font-weight:bold}
 .band h1{font-size:20pt;margin:1mm 0 1.2mm}
 .band .s{font-size:9.8pt;color:#a8a8c0;line-height:1.42}
 .band .f{font-family:"Courier New",monospace;background:#20204a;color:#4fc3f7;
          padding:.8mm 2.2mm;border-radius:1.4mm;display:inline-block;margin-top:1.6mm;font-size:9.6pt}
 .suite{background:#12122a;color:#fff;border-radius:2.4mm;padding:2mm 4mm;margin-bottom:2.6mm;
        font-size:10.2pt;font-weight:bold;display:flex;justify-content:space-between}
 .suite span{color:#ffb74d;font-weight:normal;font-size:9pt}
 .bt{border:.5mm solid #14142b;border-radius:2.6mm;margin-bottom:2.4mm;overflow:hidden;
     page-break-inside:avoid}
 .bt .h{background:#14142b;color:#fff;padding:1.1mm 3mm;font-size:10.4pt;font-weight:bold}
 .bt .c{padding:2mm 2.8mm;line-height:1.36}
 .bt ul{margin:0;padding-left:5mm}.bt li{margin-bottom:1mm}
 .bloc{font-family:"Courier New",monospace;font-size:8.2pt;background:#12122a;color:#4fc3f7;
       padding:1.7mm 2.6mm;border-radius:1.6mm;white-space:pre;line-height:1.32;margin:1.2mm 0}
 .bloc i{color:#ffb74d;font-style:normal}
 .tip{color:#6b2d8f;font-weight:bold}
"""

# =====================================================================
#  LA FEUILLE DE L'ELEVE
# =====================================================================
STYLE_ELEVE = COMMUN + """
 .avert{background:#6b2d8f;color:#fff;border-radius:2.6mm;padding:2.3mm 4mm;margin-bottom:2.5mm;
        font-size:9.5pt;line-height:1.38}
 .bt .c{line-height:1.32}
 .deux{display:flex;gap:3mm;margin-bottom:2.4mm}
 .col{flex:1;border:.6mm solid #13678f;border-radius:2.6mm;overflow:hidden}
 .col .t{background:#13678f;color:#fff;font-weight:bold;padding:1.1mm 3mm;font-size:9.6pt}
 .col .b{padding:2mm 2.6mm;font-size:8.8pt;line-height:1.4}
 .col ol{margin:0;padding-left:5mm}.col li{margin-bottom:1.3mm}
 .col pre{margin:0;font-family:"Courier New",monospace;font-size:7.6pt;line-height:1.32;
          white-space:pre;color:#12122a}
 .meth{display:flex;gap:2.4mm;margin-bottom:2.4mm}
 .meth .m{flex:1;border:.5mm solid #d79a00;border-radius:2.4mm;background:#fffaf0;
          padding:1.8mm 2.2mm;font-size:8.3pt;line-height:1.3}
 .meth .n{background:#d79a00;color:#fff;border-radius:50%;width:5.4mm;height:5.4mm;
          line-height:5.4mm;text-align:center;font-weight:bold;font-size:9.4pt;display:block;
          margin-bottom:1.2mm}
 .meth b{color:#a65d00}
 .regles{border:.7mm solid #2fb765;border-radius:2.6mm;overflow:hidden;margin-bottom:2.6mm}
 .regles .t{background:#2fb765;color:#fff;font-weight:bold;padding:1.3mm 3mm;font-size:11pt}
 .regles .b{padding:2.2mm 3mm;font-size:9.6pt;line-height:1.44;background:#f2faf5}
 .regles ol{margin:0;padding-left:5.5mm}.regles li{margin-bottom:1.5mm}
 .ecran{border:.4mm dashed #5a5a72;border-radius:2mm;padding:1.8mm 2.6mm;margin:1.6mm 0 0;
        font-family:"Courier New",monospace;font-size:8pt;line-height:1.34;white-space:pre;
        background:#fafafd;color:#2a2a44}
 .lignes{border:.5mm solid #6b2d8f;border-radius:2.6mm;overflow:hidden;margin-bottom:2.4mm}
 .lignes .t{background:#6b2d8f;color:#fff;font-weight:bold;padding:1.3mm 3mm;font-size:11pt}
 .lignes .b{padding:2.4mm 3mm 1.4mm}
 .lignes .l{display:flex;align-items:flex-end;gap:2mm;margin-bottom:2.9mm}
 .lignes .n{font-size:8.6pt;color:#6b2d8f;font-weight:bold;width:5mm;flex:none}
 .lignes .tr{flex:1;border-bottom:.3mm dotted #8a8aa0;height:4mm}
 .fin{background:#f3f3f8;border-left:3mm solid #6b2d8f;border-radius:2mm;
      padding:2.2mm 3mm;font-size:8.8pt;line-height:1.36}
 .lignes .l{margin-bottom:2.7mm}
"""

ALGO_EXEMPLE = """1. Je demande sa case au joueur, et je
   range sa reponse dans une boite.
2. Je transforme cette reponse en nombre.
3. SI la case est plus grande que 9 :
       je dis qu'elle n'existe pas.
   SINON :
       SI la case contient son numero :
           je range le symbole dedans.
       SINON :
           je dis qu'elle est deja prise.
4. J'affiche le plateau."""

CODE_EXEMPLE = """case = input("Quelle case ? ")

case = int(case)
if case &gt; 9:
    print("Elle n'existe pas !")
else:
    if plateau[case - 1] == str(case):
        plateau[case - 1] = "X"
    else:
        print("Deja prise !")
... les 5 print du plateau ..."""

eleve = ['''<div class="band">
  <div class="k">MISSION AUTONOME N&deg; 1 &middot; JEREMIAH GEEKS &middot; APR&Egrave;S LA S&Eacute;ANCE 7</div>
  <h1>&#127970; L'ASCENSEUR DE LA TOUR</h1>
  <div class="s">Mission confi&eacute;e &agrave; : <b style="color:#fff">_______________________________</b>
    &nbsp;&nbsp;&middot;&nbsp;&nbsp; &Agrave; rendre : <b style="color:#fff">______________</b></div>
  <div class="f">Thonny &rarr; Fichier &rarr; Nouveau &rarr; Enregistrer sous :  ascenseur_tonprenom.py</div>
</div>

<div class="avert">
  &#9888;&#65039; <b>Cette feuille n'est pas comme les autres.</b> On ne te donne <b>aucune &eacute;tape</b>, et
  <b>aucune ligne de code</b> &mdash; seulement <b>ce que le programme doit faire</b>. &Agrave; toi de trouver
  <b>comment</b>. C'est exactement le travail d'un vrai programmeur, et c'est pour &ccedil;a qu'on te la donne.
</div>

<div class="bt"><div class="h">&#129504; UN ALGORITHME, C'EST QUOI ?</div><div class="c">
  <b>C'est ton programme &eacute;crit en fran&ccedil;ais, avant de toucher au clavier.</b> Une suite de
  phrases courtes, dans l'ordre, qui disent ce que la machine doit faire &mdash; sans aucun mot de Python.
  <div style="margin-top:1.2mm">On l'&eacute;crit <b>d'abord</b>, parce qu'il est bien plus facile de se tromper
  sur une feuille que dans un fichier. <b>Un programmeur qui tape tout de suite est un programmeur qui
  recommence trois fois.</b></div>
</div></div>

<div class="deux">
  <div class="col"><div class="t">L'EXEMPLE &mdash; EN FRAN&Ccedil;AIS</div><div class="b">
    <div style="font-size:8.4pt;color:#5a5a72;margin-bottom:1.4mm">L'algorithme du coup jou&eacute;,
      celui que tu as &eacute;crit samedi dernier :</div>
<pre>''' + ALGO_EXEMPLE + '''</pre></div></div>
  <div class="col"><div class="t">&hellip;ET EN PYTHON</div><div class="b">
    <div style="font-size:8.4pt;color:#5a5a72;margin-bottom:1.4mm"><b>Ligne pour ligne</b>, en face.
      Une phrase &rarr; une ligne :</div>
<pre>''' + CODE_EXEMPLE + '''</pre></div></div>
</div>

<div class="bt"><div class="h">&#128221; LES QUATRE MOTS QUI SUFFISENT POUR &Eacute;CRIRE UN ALGORITHME</div><div class="c">
  <b>JE DEMANDE</b> &middot; <b>JE RANGE</b> dans une bo&icirc;te &middot; <b>SI &hellip; SINON &hellip;</b>
  &middot; <b>J'AFFICHE</b>.
  <div style="margin-top:1.2mm">Avec ces quatre-l&agrave;, tu peux d&eacute;crire tout ce que tu sais faire.
  <span class="tip">Et une r&egrave;gle d'or :</span> quand un <b>SI</b> est &agrave; l'int&eacute;rieur
  d'un autre, tu le <b>d&eacute;cales vers la droite</b> sur ta feuille, comme en Python.</div>
</div></div>

<div class="meth">
  <div class="m"><span class="n">1</span><b>&Eacute;cris.</b> Ton algorithme en fran&ccedil;ais,
    phrase par phrase, sur cette feuille. <b>Pas de clavier.</b></div>
  <div class="m"><span class="n">2</span><b>Joue-le &agrave; la main.</b> Prends un cas, suis tes
    phrases <b>une par une</b> comme si tu &eacute;tais l'ordinateur. &Ccedil;a marche ?</div>
  <div class="m"><span class="n">3</span><b>Traduis.</b> Une phrase &rarr; une ou deux lignes de
    Python. L&agrave; seulement, tu ouvres Thonny.</div>
  <div class="m"><span class="n">4</span><b>Casse-le.</b> Tape des choses bizarres expr&egrave;s,
    et regarde si ton programme tient debout.</div>
</div>

<div class="bt" style="border-color:#d79a00"><div class="h" style="background:#d79a00">&#128161; SI TU BLOQUES &mdash; trois questions &agrave; te poser (et aucune r&eacute;ponse)</div><div class="c">
  <ul><li><b>&laquo; Qu'est-ce que l'ordinateur doit savoir, et qui change pendant le programme ? &raquo;</b>
          Chaque chose qui change, c'est une bo&icirc;te &agrave; cr&eacute;er <b>avant</b> le premier voyage.</li>
      <li><b>&laquo; Combien de r&eacute;ponses diff&eacute;rentes mon programme peut-il donner, ici ? &raquo;</b>
          S'il y en a plus de deux, c'est qu'il te faut un <span class="mono">if</span>
          <b>dans</b> un <span class="mono">if</span>.</li>
      <li><b>&laquo; Je le fais comment, moi, avec un crayon ? &raquo;</b> Prends deux exemples
          pr&eacute;cis, avec de vrais chiffres, et fais-les &agrave; la main. Ce que ta main a fait
          <b>deux fois pareil</b>, c'est &ccedil;a, ton algorithme.</li></ul>
  <div style="margin-top:1.2mm"><span class="tip">Et si &ccedil;a bloque vraiment :</span> montre ton
  <b>algorithme</b> &agrave; ton enseignant, pas ton code. C'est presque toujours l&agrave; qu'est le probl&egrave;me.</div>
</div></div>

<div class="fin" style="border-color:#ffb74d;background:#fffaf0">
  &#128073; <b>La mission est sur la page 2.</b> Lis-la en entier <b>avant</b> d'&eacute;crire quoi que
  ce soit &mdash; puis reviens &eacute;crire ton algorithme dans le cadre violet.
</div>

<div class="saut"></div>
<div class="suite">&#127970; L'ASCENSEUR DE LA TOUR &mdash; la mission <span>page 2 sur 2 &middot; ascenseur_tonprenom.py</span></div>

<div class="regles"><div class="t">&#127919; LE CAHIER DES CHARGES &mdash; les sept r&egrave;gles</div><div class="b">
  <ol>
    <li>La tour a <b>cinq &eacute;tages</b> (<b>1 &agrave; 5</b>), et <b>chacun porte un nom</b>
        &mdash; les noms sont &agrave; toi. Le programme affiche la tour au d&eacute;marrage.</li>
    <li>L'ascenseur commence <b>&agrave; l'&eacute;tage 1</b>, et le dit.</li>
    <li>Il fait <b>trois voyages</b>. &Agrave; chaque voyage, il demande &agrave; quel &eacute;tage on va.</li>
    <li>Si l'&eacute;tage <b>n'existe pas</b>, l'ascenseur <b>refuse</b> et ne bouge pas &mdash;
        et ce voyage-l&agrave; ne compte pas.</li>
    <li>Sinon il annonce s'il <b>MONTE</b>, s'il <b>DESCEND</b> ou qu'on <b>y est d&eacute;j&agrave;</b>,
        <b>et de combien d'&eacute;tages</b> &mdash; puis <b>le nom</b> de l'&eacute;tage d'arriv&eacute;e.</li>
    <li>Il <b>retient o&ugrave; il est</b> : le voyage suivant part de l&agrave;.</li>
    <li>&Agrave; la fin, un <b>journal de bord</b> : o&ugrave; il se trouve, <b>combien d'&eacute;tages
        parcourus en tout</b>, <b>combien de voyages r&eacute;ussis sur trois</b>, et une phrase
        diff&eacute;rente selon qu'il a beaucoup travaill&eacute; ou non.</li>
  </ol>
  <div class="ecran">  Voyage 1 - a quel etage vas-tu ? 4
     L'ascenseur MONTE de 3 etage(s).
     Etage 4 : Cantine</div>
  <div style="font-size:8.6pt;color:#0c5c29;margin-top:1.4mm"><b>Trois lignes, pour te donner le ton
    &mdash; et c'est tout ce que tu auras.</b> Tes messages, ta mise en page et tes noms d'&eacute;tages
    sont les tiens.</div>
</div></div>

<div class="lignes"><div class="t">&#9999;&#65039; TON ALGORITHME &mdash; en fran&ccedil;ais, avant le clavier</div><div class="b">''' +
"".join('<div class="l"><div class="n">%d</div><div class="tr"></div></div>' % i for i in range(1, 11)) +
'''</div></div>

<div class="bt" style="border-color:#13678f"><div class="h" style="background:#13678f">&#129302; AVANT DE DIRE QUE C'EST FINI &mdash; les cinq essais obligatoires</div><div class="c">
  <ul><li>Monter, puis <b>redescendre</b> : le deuxi&egrave;me voyage part-il bien du nouvel &eacute;tage ?</li>
      <li>Demander <b>l'&eacute;tage o&ugrave; on est d&eacute;j&agrave;</b>.</li>
      <li>Demander <b>l'&eacute;tage 9</b> : refus&eacute;, et l'ascenseur ne bouge pas.</li>
      <li>Aller de <b>1 &agrave; 5</b> : le journal doit annoncer <b>4 &eacute;tages</b> parcourus, pas 5.</li>
      <li>Rater un voyage : le journal doit dire <b>2 / 3</b>.</li></ul>
</div></div>


<div class="bt" style="border-color:#6b2d8f"><div class="h" style="background:#6b2d8f">&#11088;&#11088; SI TU AS FINI</div><div class="c">
  <ul><li><b>Le compteur de refus.</b> Affiche aussi combien de voyages ont &eacute;t&eacute; refus&eacute;s.</li>
      <li><b>Le record.</b> Garde en m&eacute;moire <b>l'&eacute;tage le plus haut</b> atteint dans la
          journ&eacute;e, et annonce-le dans le journal.</li>
      <li><b>L'ascenseur bavard.</b> Pendant un trajet de plusieurs &eacute;tages, affiche une ligne
          par &eacute;tage travers&eacute;. <span class="tip">Attention :</span> tu vas avoir envie de
          r&eacute;p&eacute;ter quelque chose un nombre de fois que tu ne connais pas d'avance. Tu n'as
          pas encore l'outil. <b>&Eacute;cris l'algorithme quand m&ecirc;me</b>, et garde-le : c'est la
          s&eacute;ance du 14 novembre.</li></ul>
</div></div>

<div class="fin">
  <b>Ce qu'on regardera, et dans cet ordre :</b> d'abord <b>ton algorithme &eacute;crit</b>, ensuite si
  ton programme tourne, ensuite les cinq essais. <b>Un algorithme clair avec un programme &agrave;
  moiti&eacute; fini vaut mieux qu'un programme qui marche sans algorithme</b> &mdash; parce que le
  premier, tu sauras le refaire.<br>
  <b>Il n'y a pas une seule bonne r&eacute;ponse.</b> Si ton programme respecte les sept r&egrave;gles,
  il est juste, m&ecirc;me s'il ne ressemble &agrave; celui de personne d'autre.
</div>''']

E.ecrire(os.path.join(ICI, "sources", "mission-1-ascenseur-eleve.html"),
         "Mission autonome n°1 — L'ascenseur de la tour", STYLE_ELEVE, "\n".join(eleve))

# =====================================================================
#  LA FEUILLE DE L'ENSEIGNANT
# =====================================================================
STYLE_PROF = COMMUN + """
 .band{background:#0c5c29}
 .band .k{color:#a8e6bd}
 .band .s{color:#d8f0e2}
 .suite{background:#0c5c29}
 .suite span{color:#a8e6bd}
 pre.code{margin:0 0 2.2mm;background:#12122a;color:#e8e8f2;border-radius:2.6mm;padding:2.2mm 3mm;
     font-family:"Courier New",monospace;font-size:7.3pt;line-height:1.22;white-space:pre-wrap}
 pre.code .c{color:#7f7f9c} pre.code .s{color:#ffb74d} pre.code .k{color:#4fc3f7;font-weight:bold}
 .algo{border:.6mm solid #13678f;border-radius:2.6mm;overflow:hidden;margin-bottom:2.4mm}
 .algo .t{background:#13678f;color:#fff;font-weight:bold;padding:1.2mm 3mm;font-size:10.4pt}
 .algo pre{margin:0;padding:2mm 3mm;font-family:"Courier New",monospace;font-size:8.1pt;
           line-height:1.34;white-space:pre;background:#f2f8fc;color:#12122a}
 .note{background:#fffaf0;border:.6mm solid #d79a00;border-radius:2.6mm;padding:2.2mm 3mm;
       margin-bottom:2.4mm;line-height:1.4;font-size:9pt}
 .note h3{margin:0 0 1.2mm;font-size:10.4pt;color:#a65d00}
 .note ul{margin:1mm 0 0;padding-left:5mm}.note li{margin-bottom:1mm}
 .note .m{font-family:"Courier New",monospace;font-weight:bold;background:#fff;
          border:.3mm solid #e8d6a8;border-radius:1mm;padding:.3mm 1mm}
 .coupe{background:#6b2d8f;color:#fff;border-radius:2.2mm;padding:1.8mm 3.2mm;margin-bottom:2.4mm;
        font-size:9pt;line-height:1.4}
 table.g{width:100%;border-collapse:collapse;font-size:8.2pt;margin-top:1mm}
 table.g th{background:#14142b;color:#fff;padding:1mm 1.8mm;text-align:left;font-size:8pt}
 table.g td{border:.25mm solid #c8c8d8;padding:1mm 1.8mm;vertical-align:top;line-height:1.28}
"""

ALGO_MODELE = """1. Je cree la liste des cinq noms d'etages.
2. J'affiche la tour.
3. Je range 1 dans la boite "etage actuel".
4. Je range 0 dans la boite "etages parcourus".
5. Je range 0 dans la boite "arrets".

   -- POUR CHAQUE VOYAGE (je recopie le bloc 3 fois) --

6. Je demande l'etage, je le transforme en nombre.
7. SI cet etage est plus grand que 5 :
       je dis qu'il n'existe pas.          <-- et rien d'autre ne change
   SINON :
       SI l'etage demande est plus haut que l'etage actuel :
           je range (demande - actuel) dans "distance" ;
           je dis que ca MONTE de "distance".
       SINON :
           SI l'etage demande est plus bas :
               je range (actuel - demande) dans "distance" ;
               je dis que ca DESCEND de "distance".
           SINON :
               je range 0 dans "distance" ;
               je dis qu'on y est deja.

       j'affiche le nom de l'etage demande ;
       j'ajoute "distance" aux etages parcourus ;
       j'ajoute 1 aux arrets ;
       je range l'etage demande dans "etage actuel".

   -- FIN DU BLOC --

8. J'affiche le journal : etage actuel et son nom, etages
   parcourus, arrets sur 3.
9. SI les etages parcourus sont plus de 6 : une phrase.
   SINON : l'autre phrase."""

prof = ['''<div class="band">
  <div class="k">CORRIG&Eacute; &middot; POUR L'ENSEIGNANT &middot; &Agrave; NE PAS DONNER</div>
  <h1>&#9989; MISSION N&deg; 1 &mdash; L'ASCENSEUR DE LA TOUR</h1>
  <div class="s"><b style="color:#fff">Ceci est UNE solution, pas LA solution.</b> L'&eacute;l&egrave;ve
    a re&ccedil;u un cahier des charges, pas des instructions. Tout programme qui respecte les sept
    r&egrave;gles est juste, m&ecirc;me s'il ne ressemble en rien &agrave; celui-ci.</div>
</div>

<div class="note" style="border-color:#13678f;background:#f2f8fc">
  <h3 style="color:#13678f">&#127919; Pourquoi cette mission, et pour qui</h3>
  Elle s'adresse &agrave; un &eacute;l&egrave;ve <b>qui a fini avant les autres</b> et qui a besoin
  d'autre chose qu'un exercice de plus. <b>Elle est r&eacute;utilisable</b> : la feuille porte un champ
  &laquo;&nbsp;mission confi&eacute;e &agrave;&nbsp;&raquo; et ne nomme personne. <b>Aucune notion nouvelle</b> : tout tient dans la bo&icirc;te
  &agrave; outils de la s&eacute;ance 7. Ce qui est neuf, c'est qu'on lui demande
  <b>de concevoir, pas d'ex&eacute;cuter</b>.
  <ul>
    <li><b>Elle introduit l'algorithme pour de vrai.</b> La page 1 donne l'exemple qui manquait, et il
      porte sur un code d&eacute;j&agrave; &eacute;crit en classe : le coup jou&eacute; de
      la s&eacute;ance 7, en fran&ccedil;ais &agrave; gauche, en Python &agrave; droite.</li>
    <li><b>Elle force le <span class="m">if</span> dans le <span class="m">if</span></b> : trois
      r&eacute;ponses possibles (monte / descend / d&eacute;j&agrave; l&agrave;) ne peuvent pas s'&eacute;crire
      avec un seul <span class="m">if</span>. C'est la notion de samedi, port&eacute;e un cran plus loin.</li>
    <li><b>Elle pr&eacute;pare la s&eacute;ance 10</b> : le dernier bonus bute volontairement sur
      &laquo; r&eacute;p&eacute;ter un nombre de fois qu'on ne conna&icirc;t pas d'avance &raquo;.
      On lui demande d'&eacute;crire l'algorithme et de le garder.</li>
  </ul>
</div>

<div class="algo"><div class="t">&#129504; L'ALGORITHME MOD&Egrave;LE &mdash; c'est &ccedil;a qu'on lit en premier</div>
<pre>''' + ALGO_MODELE + '''</pre></div>

<div class="note">
  <h3>&#128172; Comment l'accompagner sans lui donner la r&eacute;ponse</h3>
  <b>La r&egrave;gle :</b> on ne r&eacute;pond jamais par une ligne de code. On r&eacute;pond
  <b>par une question</b>, et on s'en va.
  <ul>
    <li>&laquo; Montre-moi ton algorithme. &raquo; <i>(Pas d'algorithme &eacute;crit, pas de code&nbsp;: on s'arr&ecirc;te
      l&agrave;, retour &agrave; la feuille. C'est la seule consigne ferme de la mission.)</i></li>
    <li>&laquo; Lis-moi la phrase 7 &agrave; voix haute. &raquo; <i>Entendre son propre algorithme
      r&eacute;v&egrave;le les trous mieux que n'importe quelle relecture.</i></li>
    <li>&laquo; Fais-le &agrave; la main&nbsp;: tu es &agrave; l'&eacute;tage 2, tu demandes le 5.
      Qu'est-ce qui change&nbsp;? &raquo; <i>Pour la bo&icirc;te oubli&eacute;e.</i></li>
    <li>&laquo; Combien de r&eacute;ponses diff&eacute;rentes ton programme peut-il donner ici&nbsp;?
      &raquo; <i>Pour l'amener au <span class="m">if</span> dans le <span class="m">if</span>,
      sans le nommer.</i></li>
    <li>&laquo; Essaie le 9. &raquo; <i>Plut&ocirc;t que de signaler l'oubli du refus.</i></li>
  </ul>
</div>

<div class="saut"></div>
<div class="suite">&#9989; MISSION N&deg; 1 &mdash; la suite <span>page 2 sur 2 &middot; mission-1-ascenseur-corrige.py</span></div>
''']

code2 = E.colorie(E.extrait(PY, 40, 70))
prof.append('<div class="coupe">&#9986;&#65039; <b>Le d&eacute;but</b> (la liste des cinq noms, '
            'l\'affichage de la tour, les trois bo&icirc;tes de d&eacute;part) <b>est sans surprise</b> : '
            'il est dans le fichier <span style="font-family:\'Courier New\',monospace">'
            'mission-1-ascenseur-corrige.py</span>. Voici <b>le bloc du voyage</b>, le seul qui compte '
            '&mdash; il est <b>recopi&eacute; trois fois</b>, et le journal de bord vient apr&egrave;s.</div>\n')
prof.append('<pre class="code">%s</pre>\n' % code2)

prof.append('''<div class="note" style="border-color:#c0392b;background:#fdf3f2">
  <h3 style="color:#c0392b">&#10060; Ce qui est vraiment faux &mdash; et ce qui ne l'est pas</h3>
  <table class="g">
    <tr><th style="width:46%">Vraiment faux</th><th>Juste autrement &mdash; on ne corrige pas</th></tr>
    <tr><td><b><span class="m">actuel = demande</span> oubli&eacute;</b> &mdash; l'ascenseur ne bouge
        jamais. <b>&Agrave; chercher en premier.</b></td>
        <td>D'autres noms d'&eacute;tages, d'autres messages, une tour affich&eacute;e dans l'autre sens.</td></tr>
    <tr><td>Les quatre lignes de mise &agrave; jour <b>plac&eacute;es dans une seule branche</b> au lieu
        d'&ecirc;tre dessous : l'ascenseur ne se met &agrave; jour qu'un cas sur trois.</td>
        <td>Recalculer la distance dans chaque branche au lieu de garder une bo&icirc;te
        <span class="m">distance</span> : plus long, pas plus faux.</td></tr>
    <tr><td><span class="m">etages[demande]</span> sans le <span class="m">- 1</span> : le nom
        affich&eacute; est celui de l'&eacute;tage du dessus, <b>et Python ne dit rien</b>.</td>
        <td><span class="m">demande &gt; 5</span> ou <span class="m">demande &gt;= 6</span>.</td></tr>
    <tr><td>Un &eacute;tage inexistant accept&eacute; (<span class="m">IndexError</span> ou un nom
        faux), ou <span class="m">parcourus = parcourus + distance</span> &eacute;crit <b>avant</b> le
        calcul de la distance.</td>
        <td>Compter aussi les voyages rat&eacute;s, ou tenir un journal plus riche que demand&eacute; :
        c'est un bonus, pas une faute.</td></tr>
  </table>
  <div style="margin-top:1.4mm"><b>Le z&eacute;ro et les nombres n&eacute;gatifs ne sont pas au programme
  de cette mission</b> &mdash; les refuser demanderait le <span class="m">and</span> de la s&eacute;ance 9.
  Si l'&eacute;l&egrave;ve le remarque, c'est un excellent signe : dites-lui que c'est exactement la
  question du 7 novembre.</div>
</div>

<div class="note" style="border-color:#2fb765;background:#f2faf5">
  <h3 style="color:#0c5c29">&#9989; Comment l'&eacute;valuer &mdash; par la preuve, pas par une note</h3>
  <table class="g">
    <tr><th style="width:30%">Ce qu'on regarde</th><th>La preuve</th></tr>
    <tr><td><b>1. L'algorithme existe</b></td><td>Le cadre violet est rempli, en fran&ccedil;ais, avec
        des <b>SI</b> d&eacute;cal&eacute;s. <b>C'est le vrai livrable de la mission.</b></td></tr>
    <tr><td><b>2. Jou&eacute; &agrave; la main</b></td><td>L'&eacute;l&egrave;ve sait dire, sans la
        machine, ce que devient chaque bo&icirc;te quand on va de l'&eacute;tage 2 au 5.</td></tr>
    <tr><td><b>3. Le programme tourne</b></td><td>Les trois voyages s'encha&icirc;nent sans message rouge.</td></tr>
    <tr><td><b>4. Il tient debout</b></td><td>Les <b>cinq essais</b> de la feuille passent, le 9 refus&eacute;
        compris.</td></tr>
    <tr><td><b>5. Expliqu&eacute;</b></td><td>L'&eacute;l&egrave;ve sait dire <b>pourquoi</b> les quatre
        lignes de mise &agrave; jour sont &agrave; ce niveau de d&eacute;calage, et pas plus &agrave;
        droite.</td></tr>
  </table>
  <div style="margin-top:1.4mm"><b>Les points 1 et 5 comptent plus que le 3</b> &mdash; c'est
  &eacute;crit sur sa feuille, dites-le avant le d&eacute;but. <b>Et apr&egrave;s :</b>
  faites-lui pr&eacute;senter <b>son algorithme</b> &agrave; la classe en trois minutes, au tableau,
  <b>sans montrer le code</b>. Pour les autres, c'est le premier algorithme qu'ils verront
  &eacute;crit par quelqu'un de leur &acirc;ge.</div>
</div>''')

E.ecrire(os.path.join(ICI, "sources", "mission-1-ascenseur-corrige.html"),
         "Corrigé — Mission autonome n°1", STYLE_PROF, "\n".join(prof))

# =====================================================================
for base in ("mission-1-ascenseur-eleve", "mission-1-ascenseur-corrige"):
    src = os.path.join(ICI, "sources", base + ".html")
    pdf = os.path.join(ICI, base + ".pdf")
    E.pdf(src, pdf)
    noms, doc = E.png(pdf, os.path.join(ICI, base))
    print("%-34s %d pages  remplissage %s" % (base, doc.page_count, E.mesure(pdf)))
