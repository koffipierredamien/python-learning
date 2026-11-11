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
#  LA FEUILLE DE L'ELEVE  -  une page, le contexte et le rendu
# =====================================================================
STYLE_ELEVE = COMMUN + """
 .deux{display:flex;gap:3mm;margin-bottom:2.6mm}
 .col{flex:1;border:.6mm solid #13678f;border-radius:2.6mm;overflow:hidden}
 .col .t{background:#13678f;color:#fff;font-weight:bold;padding:1.1mm 3mm;font-size:9.6pt}
 .col .b{padding:2mm 2.6mm;font-size:8.8pt;line-height:1.4}
 .col pre{margin:0;font-family:"Courier New",monospace;font-size:7.6pt;line-height:1.32;
          white-space:pre;color:#12122a}
 .mission{display:flex;gap:3mm;margin-bottom:2.6mm;align-items:stretch}
 .regles{flex:1.15;border:.7mm solid #2fb765;border-radius:2.6mm;overflow:hidden;
         display:flex;flex-direction:column}
 .regles .t{background:#2fb765;color:#fff;font-weight:bold;padding:1.3mm 3mm;font-size:10.6pt}
 .regles .b{padding:2.2mm 3mm;font-size:9.3pt;line-height:1.42;background:#f2faf5;flex:1}
 .regles .ctx{margin-bottom:1.8mm;color:#0c5c29}
 .regles ol{margin:0;padding-left:5mm}.regles li{margin-bottom:1.4mm}
 .ecran{flex:1;border:.7mm solid #12122a;border-radius:2.6mm;overflow:hidden;
        display:flex;flex-direction:column}
 .ecran .t{background:#12122a;color:#fff;font-weight:bold;padding:1.3mm 3mm;font-size:10.2pt}
 .ecran .t span{color:#4fc3f7;font-weight:normal;font-size:8pt}
 .ecran pre{margin:0;padding:2.4mm 3mm;background:#12122a;color:#d8d8e8;flex:1;
            font-family:"Courier New",monospace;font-size:7.1pt;line-height:1.3;white-space:pre}
 .ecran pre b{color:#4fc3f7}
 .pas{display:flex;gap:3mm}
 .pas .p{flex:1;border:.6mm solid #6b2d8f;border-radius:2.6mm;background:#faf5fd;
         padding:2.4mm 3mm;font-size:9.6pt;line-height:1.4}
 .pas .n{background:#6b2d8f;color:#fff;border-radius:50%;width:6mm;height:6mm;line-height:6mm;
         text-align:center;font-weight:bold;font-size:10.4pt;display:inline-block;
         margin-right:2mm;vertical-align:-1mm}
 .pas b{color:#4b1f66}
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

ECRAN = """========================================
        LA TOUR ACPROKIDS
========================================

 5 - Terrasse
 4 - Cantine
 3 - Bureaux
 2 - Accueil
 1 - Parking

L'ascenseur est a l'etage 1 : Parking
Tu as droit a 3 voyages.

Voyage 1 - a quel etage vas-tu ? <b>4</b>
   L'ascenseur MONTE de 3 etage(s).
   Etage 4 : Cantine

Voyage 2 - a quel etage vas-tu ? <b>9</b>
   Cet etage n'existe pas.
   La tour va de 1 a 5.

Voyage 3 - a quel etage vas-tu ? <b>2</b>
   L'ascenseur DESCEND de 2 etage(s).
   Etage 2 : Accueil

========================================
       JOURNAL DE L'ASCENSEUR
========================================
 Position finale : etage 2 (Accueil)
 Etages parcourus : 5
 Arrets effectues : 2 / 3

 Journee tranquille dans la tour.
========================================"""

eleve = ['''<div class="band">
  <h1>&#127970; L\'ASCENSEUR DE LA TOUR</h1>
  <div class="s">La tour AcProKids a <b style="color:#fff">cinq &eacute;tages</b>, et chacun porte un
    nom. Il y a un ascenseur, et <b style="color:#fff">c\'est toi qui vas l\'&eacute;crire</b>.</div>
</div>

<div class="bt"><div class="h">&#129504; UN ALGORITHME, C\'EST QUOI ?</div><div class="c">
  <b>C\'est ton programme &eacute;crit en fran&ccedil;ais, avant de toucher au clavier.</b> Une suite de
  phrases courtes, dans l\'ordre, qui disent ce que la machine doit faire &mdash; sans aucun mot de Python.
  <div style="margin-top:1.2mm">Quand un <b>SI</b> est &agrave; l\'int&eacute;rieur d\'un autre, tu le
  <b>d&eacute;cales vers la droite</b> sur ta feuille, exactement comme en Python.</div>
</div></div>

<div class="deux">
  <div class="col"><div class="t">L\'EXEMPLE &mdash; EN FRAN&Ccedil;AIS</div><div class="b">
    <div style="font-size:8.4pt;color:#5a5a72;margin-bottom:1.4mm">L\'algorithme du coup jou&eacute;,
      celui que tu as &eacute;crit samedi dernier :</div>
<pre>''' + ALGO_EXEMPLE + '''</pre></div></div>
  <div class="col"><div class="t">&hellip;ET EN PYTHON</div><div class="b">
    <div style="font-size:8.4pt;color:#5a5a72;margin-bottom:1.4mm"><b>Ligne pour ligne</b>, en face.
      Une phrase &rarr; une ligne :</div>
<pre>''' + CODE_EXEMPLE + '''</pre></div></div>
</div>

<div class="mission">
  <div class="regles"><div class="t">&#127919; LE PROGRAMME &Agrave; &Eacute;CRIRE</div><div class="b">
    <div class="ctx">L\'ascenseur part de l\'<b>&eacute;tage 1</b> et fait <b>trois voyages</b>.
      &Agrave; chaque voyage, il demande o&ugrave; on veut aller.</div>
    <ol>
      <li>Au d&eacute;marrage, il <b>affiche la tour</b> : les cinq &eacute;tages et leurs noms.</li>
      <li>Si l\'&eacute;tage demand&eacute; <b>n\'existe pas</b>, il <b>refuse</b> et ne bouge pas &mdash;
          et ce voyage ne compte pas.</li>
      <li>Sinon il annonce s\'il <b>MONTE</b>, s\'il <b>DESCEND</b> ou qu\'on <b>y est d&eacute;j&agrave;</b>,
          <b>et de combien d\'&eacute;tages</b>.</li>
      <li>Puis il annonce <b>le nom</b> de l\'&eacute;tage o&ugrave; il s\'arr&ecirc;te.</li>
      <li>Il <b>retient o&ugrave; il est</b> : le voyage suivant part de l&agrave;.</li>
      <li>&Agrave; la fin, un <b>journal de bord</b> : o&ugrave; il se trouve, combien d\'&eacute;tages
          parcourus <b>en tout</b>, combien de voyages r&eacute;ussis <b>sur trois</b>, et une phrase
          diff&eacute;rente selon qu\'il a beaucoup travaill&eacute; ou non.</li>
    </ol>
  </div></div>
  <div class="ecran"><div class="t">&#128187; CE QUE &Ccedil;A DOIT DONNER <span>&middot; en bleu : ce qu'on tape</span></div>
<pre>''' + ECRAN + '''</pre></div>
</div>

<div class="pas">
  <div class="p"><span class="n">1</span><b>Ton algorithme, dans ton cahier.</b><br>
    En fran&ccedil;ais, phrase par phrase, <b>avant</b> d\'ouvrir Thonny.</div>
  <div class="p"><span class="n">2</span><b>Ton code, dans Thonny.</b><br>
    Une phrase de ton algorithme = une ou deux lignes de Python.
    <span style="font-family:\'Courier New\',monospace;font-size:8.4pt">ascenseur_tonprenom.py</span></div>
</div>''']

E.ecrire(os.path.join(ICI, "sources", "mission-1-ascenseur-eleve.html"),
         "L'ascenseur de la tour", STYLE_ELEVE, "\n".join(eleve))

# =====================================================================
#  LA FEUILLE DE L'ENSEIGNANT
# =====================================================================
STYLE_PROF = COMMUN + """
 .band{background:#0c5c29;padding:2.6mm 5mm;margin-bottom:2.4mm}
 .band h1{font-size:18pt;margin:.8mm 0 1mm}
 .band .k{color:#a8e6bd}
 .band .s{color:#d8f0e2}
 .suite{background:#0c5c29}
 .suite span{color:#a8e6bd}
 pre.code{margin:0 0 2.2mm;background:#12122a;color:#e8e8f2;border-radius:2.6mm;padding:2.2mm 3mm;
     font-family:"Courier New",monospace;font-size:7.3pt;line-height:1.22;white-space:pre-wrap}
 pre.code .c{color:#7f7f9c} pre.code .s{color:#ffb74d} pre.code .k{color:#4fc3f7;font-weight:bold}
 .algo{border:.6mm solid #13678f;border-radius:2.6mm;overflow:hidden;margin-bottom:1.8mm}
 .algo .t{background:#13678f;color:#fff;font-weight:bold;padding:1.2mm 3mm;font-size:10.4pt}
 .algo pre{margin:0;padding:1.6mm 2.4mm;font-family:"Courier New",monospace;font-size:7pt;
           line-height:1.22;white-space:pre;background:#f2f8fc;color:#12122a}
 .algo .t{padding:1mm 3mm;font-size:10pt}
 .note{background:#fffaf0;border:.6mm solid #d79a00;border-radius:2.6mm;padding:2mm 2.8mm;
       margin-bottom:1.7mm;line-height:1.32;font-size:8.4pt}
 .note h3{margin:0 0 1mm;font-size:10pt;color:#a65d00}
 .note ul{margin:.8mm 0 0;padding-left:4.6mm}.note li{margin-bottom:.8mm}
 .note .m{font-family:"Courier New",monospace;font-weight:bold;background:#fff;
          border:.3mm solid #e8d6a8;border-radius:1mm;padding:.3mm 1mm}
 .coupe{background:#6b2d8f;color:#fff;border-radius:2.2mm;padding:1.8mm 3.2mm;margin-bottom:2.4mm;
        font-size:9pt;line-height:1.4}
 table.g{width:100%;border-collapse:collapse;font-size:8pt;margin-top:1mm}
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
  Pour un &eacute;l&egrave;ve <b>qui a fini avant les autres</b>. <b>Aucune notion nouvelle</b> : tout
  tient dans la bo&icirc;te &agrave; outils de la s&eacute;ance 7. Ce qui est neuf, c'est qu'on demande
  <b>de concevoir, pas d'ex&eacute;cuter</b>. La feuille ne nomme personne : elle resservira.
  <ul>
    <li><b>Elle introduit l'algorithme pour de vrai.</b> Sa feuille donne l'exemple qui manquait, et il
      porte sur un code d&eacute;j&agrave; &eacute;crit en classe : le coup jou&eacute; de la
      s&eacute;ance 7, en fran&ccedil;ais &agrave; gauche, en Python &agrave; droite, ligne pour ligne.</li>
    <li><b>Elle force le <span class="m">if</span> dans le <span class="m">if</span></b> : trois
      r&eacute;ponses possibles (monte / descend / d&eacute;j&agrave; l&agrave;) ne peuvent pas s'&eacute;crire
      avec un seul <span class="m">if</span>. C'est la notion de samedi, port&eacute;e un cran plus loin.</li>
    <li><b>Sa feuille tient sur une page</b> et ne porte que trois choses : ce qu'est un algorithme,
      le cahier des charges du programme, et l'&eacute;cran attendu. <b>Aucune &eacute;tape, aucune ligne
      de code.</b> L'algorithme s'&eacute;crit <b>dans son cahier</b>, le code ensuite dans Thonny.</li>
  </ul>
</div>

<div class="algo"><div class="t">&#129504; L'ALGORITHME MOD&Egrave;LE &mdash; c'est &ccedil;a qu'on lit en premier</div>
<pre>''' + ALGO_MODELE + '''</pre></div>

<div class="note" style="border-color:#13678f;background:#f2f8fc">
  <h3 style="color:#13678f">&#129302; Les cinq essais &agrave; lui faire faire avant de valider</h3>
  Ils ne sont pas sur sa feuille, <b>expr&egrave;s</b> : trouver comment on &eacute;prouve un programme
  fait partie du travail. Demandez-les un par un, <b>&agrave; la fin</b>.
  <ul style="margin-top:1mm">
    <li>Monter, puis <b>redescendre</b> : le deuxi&egrave;me voyage part-il bien du nouvel &eacute;tage ?</li>
    <li>Demander <b>l'&eacute;tage o&ugrave; on est d&eacute;j&agrave;</b>.</li>
    <li>Demander <b>l'&eacute;tage 9</b> : refus&eacute;, et l'ascenseur ne bouge pas.</li>
    <li>Aller de <b>1 &agrave; 5</b> : le journal annonce <b>4 &eacute;tages</b> parcourus, pas 5.</li>
    <li>Rater un voyage : le journal dit <b>2 / 3</b>.</li>
  </ul>
  <div style="margin-top:1.2mm"><b>Et si tout est fini</b>, trois prolongements &agrave; donner
  oralement : compter les voyages <b>refus&eacute;s</b> ; retenir <b>l'&eacute;tage le plus haut</b>
  atteint ; afficher <b>une ligne par &eacute;tage travers&eacute;</b> pendant un trajet.
  <b>Le troisi&egrave;me est un pi&egrave;ge volontaire</b> : il demande de r&eacute;p&eacute;ter un
  nombre de fois qu'on ne conna&icirc;t pas d'avance, et l'outil n'arrive que le 14 novembre.
  Demandez l'algorithme quand m&ecirc;me, et gardez-le pour ce jour-l&agrave;.</div>
</div>

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
      &raquo; <i>Pour amener au <span class="m">if</span> dans le <span class="m">if</span> sans le
      nommer.</i> &mdash; et &laquo; Essaie le 9. &raquo; <i>plut&ocirc;t que de signaler l'oubli
      du refus.</i></li>
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
    <tr><td><b>1. L'algorithme existe</b></td><td>Il est dans le cahier, en fran&ccedil;ais, avec des
        <b>SI</b> d&eacute;cal&eacute;s. <b>C'est le vrai livrable de la mission.</b></td></tr>
    <tr><td><b>2. Jou&eacute; &agrave; la main</b></td><td>L'&eacute;l&egrave;ve sait dire, sans la
        machine, ce que devient chaque bo&icirc;te quand on va de l'&eacute;tage 2 au 5.</td></tr>
    <tr><td><b>3. Le programme tourne</b></td><td>Les trois voyages s'encha&icirc;nent sans message rouge.</td></tr>
    <tr><td><b>4. Il tient debout</b></td><td>Les <b>cinq essais</b> list&eacute;s plus haut passent, le 9
        refus&eacute; compris.</td></tr>
    <tr><td><b>5. Expliqu&eacute;</b></td><td>L'&eacute;l&egrave;ve sait dire <b>pourquoi</b> les quatre
        lignes de mise &agrave; jour sont &agrave; ce niveau de d&eacute;calage, et pas plus &agrave;
        droite.</td></tr>
  </table>
  <div style="margin-top:1.4mm"><b>Les points 1 et 5 comptent plus que le 3</b> &mdash; ce n'est
  pas &eacute;crit sur sa feuille : <b>dites-le vous-m&ecirc;me, avant le d&eacute;but.</b> <b>Et apr&egrave;s :</b>
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
