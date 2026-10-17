# -*- coding: utf-8 -*-
"""Contenu des trois exercices de maison du package octobre-novembre."""

# =====================================================================
#  1  -  LE COFFRE-FORT   (apres la seance 6 : la liste)
# =====================================================================
COFFRE = dict(
    dossier="S06-le-plateau-se-souvient",
    css1="",
    base="exercice-maison-le-coffre-fort",
    base_cor="correction-le-coffre-fort",
    py="correction-coffre-fort.py",
    titre="Le Coffre-Fort",
    emoji="🔐",
    nom="LE COFFRE-FORT",
    kicker="EXERCICE DE MAISON · JEREMIAH GEEKS · SEMAINE DU 17 OCTOBRE",
    fichier="coffre_tonprenom.py",
    chapo="""Un coffre à <b style="color:#fff">cinq tiroirs</b>, un trésor caché, et deux essais pour
      le trouver. Ta nouvelle arme : <b style="color:#fff">la liste</b> — une seule boîte qui range
      cinq choses, et qui se souvient de ce que tu as déjà ouvert.""",
    regle="""🎯 <b>La règle du jeu :</b> joueur 2 cache un trésor dans un des cinq tiroirs.
      Joueur 1 a <b>deux essais</b>. On part de <b>50 points</b> et chaque tiroir vide en coûte <b>20</b>.
      Les tiroirs déjà ouverts <b>restent marqués</b> : <b>X</b> s'ils étaient vides, <b>T</b> pour le trésor.""",
    ecran="""==================================
        LE COFFRE-FORT
==================================

 1 | 2 | 3 | 4 | 5

Joueur 1, ferme les yeux !
Joueur 2, dans quel tiroir
caches-tu le tresor ? (1 a 5) <b>3</b>

==================================
   Joueur 1, tu as 2 essais.
==================================

Essai 1 - quel tiroir ouvres-tu ? <b>1</b>
   Vide ! Ce tiroir ne contenait rien.

 X | 2 | 3 | 4 | 5

Essai 2 - quel tiroir ouvres-tu ? <b>3</b>
   BRAVO ! Le tresor etait bien la !

 X | 2 | T | 4 | 5

==================================
Le tresor etait dans le tiroir 3.
Ton score : 30 / 50
PILLEUR DE COFFRE-FORT !
==================================""",
    kit="""<b>La liste :</b> une boîte qui en contient cinq.<br>
      <span class="m">tiroirs = ["1", "2", "3", "4", "5"]</span>
      <hr>
      <b>L'indice commence à ZÉRO.</b><br>
      tiroir n° 1 → <span class="m">tiroirs[0]</span><br>
      tiroir n° 3 → <span class="m">tiroirs[2]</span><br>
      tiroir n° <b>N</b> → <span class="m">tiroirs[N - 1]</span>
      <hr>
      <b>Écrire dans un tiroir :</b><br>
      <span class="m">tiroirs[essai - 1] = "X"</span>
      <hr>
      <b>input rend TOUJOURS du texte.</b><br>
      Pour comparer : <span class="m">essai = int(essai)</span><br>
      Pour l'écrire dans une phrase : <span class="m">str(points)</span>
      <hr>
      <b>Le compteur, à l'envers :</b><br>
      <span class="m">points = 50</span> une seule fois, au début<br>
      <span class="m">points = points - 20</span> à chaque raté""",
    etapes1=[
        ("1", "LES CINQ TIROIRS", """
         <ul><li>Affiche le cadre de <b>34 signes</b> <span class="mono">=</span> et le titre.</li>
             <li>Crée <b>la liste</b> <span class="mono">tiroirs</span> avec les cinq numéros
                 <b>entre guillemets</b> : ce sont des textes, pas des nombres.</li>
             <li>Affiche la ligne des tiroirs :
               <div class="bloc">print(" " + tiroirs[0] + " | " + tiroirs[1] + " | " + tiroirs[2] + " | " + tiroirs[3] + " | " + tiroirs[4])</div>
               <span class="tip">Oui, c'est long.</span> Recopie-le une fois, puis fais
               <b>copier-coller</b> : tu en auras besoin trois fois.</li></ul>"""),
        ("2", "LE JOUEUR 2 CACHE LE TRÉSOR", """
         <ul><li>Affiche <span class="mono">Joueur 1, ferme les yeux !</span></li>
             <li>Demande <span class="mono">Joueur 2, dans quel tiroir caches-tu le tresor ? (1 a 5)</span>
                 et range la réponse dans <span class="mono">tresor</span>.</li>
             <li><b>Transforme-la en nombre.</b> Sans ça, la comparaison de l'étape 4 ne marchera jamais.</li>
             <li>Affiche le cadre <span class="mono">Joueur 1, tu as 2 essais.</span></li></ul>"""),
        ("3", "LES POINTS", """
         Crée une boîte <span class="mono">points</span> qui contient <b>50</b>.
         <b>Une seule fois</b>, avant les essais — si tu la remets avant chaque essai, le score
         restera bloqué à 50."""),
    ],
    etapes2=[
        ("4", "L'ESSAI N° 1 — le cœur du jeu", """
         Demande le tiroir, transforme-le en nombre, puis :
         <div class="bloc">if essai == tresor:
    print("   BRAVO ! Le tresor etait bien la !")
    tiroirs[essai - 1] = "T"      <i>← le trésor</i>
else:
    print("   Vide ! Ce tiroir ne contenait rien.")
    tiroirs[essai - 1] = "X"      <i>← la croix</i>
    points = points - 20          <i>← DANS le else</i></div>
         Puis <b>réaffiche la ligne des tiroirs</b> (copier-coller de l'étape 1) :
         la marque doit apparaître au bon endroit."""),
        ("5", "L'ESSAI N° 2", """
         <b>Recopie tout le bloc de l'étape 4.</b> Tu changes seulement
         <span class="mono">Essai 1</span> en <span class="mono">Essai 2</span>.
         <div style="margin-top:1.2mm"><span class="tip">Oui, on recopie encore :</span> garde cet agacement
         en tête. Dans trois séances, une seule ligne remplacera tous ces blocs.</div>"""),
        ("6", "LE VERDICT", """
         <ul><li><span class="mono">Le tresor etait dans le tiroir &lt;tresor&gt;.</span> — il faudra <span class="mono">str()</span>.</li>
             <li><span class="mono">Ton score : &lt;points&gt; / 50</span></li>
             <li><b>Si</b> les points sont <b>plus grands que 20</b> : <span class="mono">PILLEUR DE COFFRE-FORT !</span></li>
             <li><b>Sinon</b> : <span class="mono">Le coffre a resiste... pour cette fois.</span></li></ul>"""),
    ],
    bonus="""<ul>
      <li><b>Un troisième essai.</b> Recopie encore un bloc. Le score peut alors tomber à 0 — c'est permis.</li>
      <li><b>⭐⭐ Le tiroir déjà ouvert.</b> Si le joueur retape un tiroir qu'il a déjà ouvert, il ne
        devrait pas perdre 20 points une deuxième fois. Comment savoir qu'un tiroir est <b>encore fermé</b> ?
        <b>Il contient encore son numéro.</b>
        <div class="bloc">if tiroirs[essai - 1] == str(essai):
    <i>... on ouvre, comme à l'étape 4 ...</i>
else:
    print("Tu as deja ouvert ce tiroir !")</div>
        <b>Celui qui réussit ce bonus a déjà compris la séance de samedi prochain.</b></li></ul>""",
    fin="""<b>Quand ça marche :</b> fais une <b>vraie partie</b> avec quelqu'un de ta maison.
      Puis relance-le en te trompant aux deux essais : le score doit tomber à <b>10</b> et afficher
      <span class="mono">Le coffre a resiste...</span>. Ensuite <b>Ctrl + S</b>, et
      <b>envoie une photo de ton écran</b> à ton enseignant.<br>
      <b>Le bug le plus courant :</b> <span class="mono">tiroirs[essai]</span> au lieu de
      <span class="mono">tiroirs[essai - 1]</span> — la marque se met <b>à côté</b>.
      Et si tu tapes 5, Python crie <span class="mono">IndexError</span> : il n'y a pas de tiroir n° 5
      dans une liste qui s'arrête à l'indice 4.""",
    # --- corrige -----------------------------------------------------
    cor_chapo="""Le programme complet. Il tourne tel quel dans Thonny.
      Les messages peuvent varier d'un élève à l'autre : <b>ce qui compte, c'est que les marques
      tombent dans le bon tiroir et que le score soit juste.</b>""",
    blocs=[(14, 65), (66, 76)],
    coupe_texte=None,
    taille="8.1pt",
    cor_notes="""
      <div class="note"><h3>⭐ Les deux bonus</h3>
        <b>1. Le troisième essai :</b> recopier le bloc de l'étape 5. Rien de plus.<br>
        <b>2. Le tiroir déjà ouvert :</b> avant d'ouvrir, vérifier que le tiroir
        <b>contient encore son numéro</b> —
        <span class="m">if tiroirs[essai - 1] == str(essai):</span> … <span class="m">else:</span>
        <span class="m">print("Tu as deja ouvert ce tiroir !")</span>.
        C'est exactement le test de la case libre de la <b>séance 7</b> : l'élève qui le réussit
        arrive samedi avec une séance d'avance — dites-le-lui devant la classe.</div>
      <div class="note" style="border-color:#2fb765;background:#f2faf5">
        <h3 style="color:#0c5c29">✅ Les six choses à regarder dans une copie</h3>
        <ul>
          <li>la liste a-t-elle bien <b>cinq</b> cases, entre <b>crochets</b>, séparées par des virgules ?</li>
          <li>l'affichage utilise-t-il <span class="m">tiroirs[0]</span> à <span class="m">tiroirs[4]</span>
              — et pas <span class="m">[1]</span> à <span class="m">[5]</span> ?</li>
          <li>le <span class="m">- 1</span> est-il présent dans <span class="m">tiroirs[essai - 1]</span> ?</li>
          <li><span class="m">points = 50</span> est-il <b>avant</b> les essais, et <b>une seule fois</b> ?</li>
          <li><span class="m">points = points - 20</span> est-il <b>dans le else</b>, donc décalé ?</li>
          <li>les <span class="m">str()</span> sont-ils là dans le verdict ?</li>
        </ul>
        <div style="margin-top:1.6mm"><b>Barème conseillé :</b> les étapes 1 à 3 = « il a compris la liste ».
        Les étapes 4 à 6 = « il a compris l'indice ». <b>On note la preuve, pas la perfection :</b>
        un jeu qui marche avec deux fautes d'orthographe dans les messages vaut mieux qu'un code
        parfait qui ne tourne pas.</div></div>""",
)

# =====================================================================
#  2  -  LA SOIREE DU CLUB GEEK   (apres la seance 9 : and / or)
# =====================================================================
CLUB = dict(
    dossier="S09-et-ou",
    css1=".goal pre{font-size:6.9pt;line-height:1.26}",
    base="exercice-maison-la-soiree-du-club",
    base_cor="correction-la-soiree-du-club",
    py="correction-videur-club.py",
    titre="La Soirée du Club Geek",
    emoji="🕶️",
    nom="LA SOIRÉE DU CLUB GEEK",
    kicker="EXERCICE DE MAISON · JEREMIAH GEEKS · SEMAINE DU 7 NOVEMBRE",
    fichier="videur_tonprenom.py",
    chapo="""En classe, ton videur posait <b style="color:#fff">une seule question</b>.
      Ce soir, il tient la porte tout seul : <b style="color:#fff">trois fauteuils, quatre visiteurs</b>,
      et une règle de club qui tient en <b style="color:#fff">une ligne</b> grâce à
      <b style="color:#fff">and</b> et <b style="color:#fff">or</b>.""",
    regle="""🎯 <b>La règle du club :</b> on entre si on a <b>entre 12 et 18 ans</b>
      <b>ET</b> qu'on a suivi <b>au moins 3 séances</b> — <b>OU</b> si on a le code VIP
      <span style="font-family:'Courier New',monospace">GEEK2026</span>.
      Mais il n'y a que <b>trois fauteuils</b> : quand ils sont pris, c'est complet.
      <b>Même pour un VIP.</b>""",
    ecran="""======================================
        LE CLUB GEEK  -  CE SOIR
======================================
Trois fauteuils. Pas un de plus.

--------------------------------------
Qui se presente ? <b>Kofi</b>
Ton age ? <b>14</b>
Combien de seances as-tu suivies ? <b>5</b>
Ton code VIP ?
   ENTREZ, Kofi !
   Fauteuils occupes : 1 / 3

--------------------------------------
Qui se presente ? <b>Awa</b>
Ton age ? <b>11</b>
Combien de seances as-tu suivies ? <b>9</b>
Ton code VIP ?
   Desole Awa, pas ce soir.
   Fauteuils occupes : 1 / 3

     ( ... visiteurs 3 et 4 ... )

======================================
        RAPPORT DU VIDEUR
======================================
 Fauteuil 1 : Kofi
 Fauteuil 2 : Jeremie
 Fauteuil 3 : Sarah

 Entrees de la soiree : 3 / 3
 SOIREE COMPLETE !
 Le club a fait salle pleine.
======================================""",
    kit="""<b>Les deux mots de la semaine :</b><br>
      <span class="m">and</span> → il faut <b>TOUT</b><br>
      <span class="m">or</span> &nbsp;→ il suffit d'<b>UN</b>
      <hr>
      <b>Les parenthèses, comme en maths :</b><br>
      <span class="m">(A and B) or C</span><br>
      on règle d'abord ce qui est <b>dedans</b>.
      <hr>
      <b>Le compteur qui MONTE :</b><br>
      <span class="m">entres = 0</span> au début<br>
      <span class="m">entres = entres + 1</span> à chaque entrée
      <hr>
      <b>La liste des fauteuils :</b><br>
      <span class="m">fauteuils = ["(libre)", "(libre)", "(libre)"]</span><br>
      <b>Attention, piège :</b> ici on écrit
      <span class="m">fauteuils[entres]</span> <b>sans le −1</b> !
      Le compteur part de 0, il tombe déjà sur le bon fauteuil.
      <hr>
      <span class="m">int()</span> pour l'âge et les séances,
      <span class="m">str()</span> pour les afficher.""",
    etapes1=[
        ("1", "LE CLUB OUVRE", """
         <ul><li>Affiche le cadre de <b>38</b> signes <span class="mono">=</span>, le titre, et
             <span class="mono">Trois fauteuils. Pas un de plus.</span></li>
             <li>Crée la liste <span class="mono">fauteuils</span> avec trois fois
                 <span class="mono">"(libre)"</span>.</li>
             <li>Crée le compteur <span class="mono">entres</span> à <b>0</b>.
                 <b>Une seule fois</b>, tout en haut.</li></ul>"""),
        ("2", "LE VISITEUR SE PRÉSENTE", """
         Quatre questions, dans cet ordre : <span class="mono">nom</span>,
         <span class="mono">age</span>, <span class="mono">seances</span>, <span class="mono">code</span>.
         <div style="margin-top:1.2mm"><b>L'âge et les séances doivent devenir des nombres</b> —
         on va les comparer. Le nom et le code restent du texte.</div>"""),
        ("3", "Y A-T-IL ENCORE DE LA PLACE ?", """
         <b>Avant même de regarder le visiteur</b>, le videur regarde la salle :
         <div class="bloc">if entres &lt; 3:
    <i>... ici viendra la règle du club (étape 4) ...</i>
else:
    print("   Le club est COMPLET. Reviens samedi prochain.")</div>
         Puis, à la fin du visiteur :
         <span class="mono">print("   Fauteuils occupes : " + str(entres) + " / 3")</span>"""),
    ],
    etapes2=[
        ("4", "LA RÈGLE DU CLUB — le cœur de l'exercice", """
         <b>Dedans</b>, décalé de 4 espaces de plus, le <span class="mono">if</span> qui décide :
         <div class="bloc">    if (age &gt;= 12 and age &lt;= 18 and seances &gt;= 3) or code == "GEEK2026":
        print("   ENTREZ, " + nom + " !")
        fauteuils[entres] = nom        <i>← on l'assoit</i>
        entres = entres + 1            <i>← un fauteuil de moins</i>
    else:
        print("   Desole " + nom + ", pas ce soir.")</div>
         <span class="tip">Lis la condition à voix haute :</span> « (le bon âge <b>et</b> le bon âge
         <b>et</b> assez de séances) <b>ou</b> le code VIP ». Si tu sais la dire, tu sais l'écrire."""),
        ("5", "LES VISITEURS 2, 3 ET 4", """
         <b>Recopie tout le bloc</b> (étapes 2, 3 et 4) <b>trois fois de plus</b>.
         Tu ne changes <b>rien</b> : les questions sont les mêmes, c'est le visiteur qui change.
         <div style="margin-top:1.2mm"><span class="tip">Compte les lignes que tu recopies.</span>
         Note le nombre sur ta feuille et apporte-le samedi : on va le faire tomber à <b>zéro</b>.</div>"""),
        ("6", "LE RAPPORT DU VIDEUR", """
         <ul><li>Affiche les trois fauteuils, un par ligne :
             <span class="mono">Fauteuil 1 : &lt;fauteuils[0]&gt;</span>…</li>
             <li><span class="mono">Entrees de la soiree : &lt;entres&gt; / 3</span></li>
             <li><b>Si</b> <span class="mono">entres == 3</span> :
                 <span class="mono">SOIREE COMPLETE !</span> <b>Sinon</b> :
                 <span class="mono">Il restait de la place. Le videur a ete severe.</span></li></ul>"""),
    ],
    bonus="""<ul>
      <li><b>Le code en minuscules.</b> Le VIP qui tape <span class="mono">geek2026</span> doit entrer aussi.
        Un <span class="mono">or</span> de plus suffit.</li>
      <li><b>Dis-lui pourquoi.</b> Dans le refus, ajoute un <span class="mono">if</span> :
        si <span class="mono">age &lt; 12</span>, affiche <span class="mono">Trop jeune !</span> ;
        si <span class="mono">seances &lt; 3</span>, affiche <span class="mono">Viens plus souvent !</span></li>
      <li><b>⭐⭐ Déjà entré !</b> Un malin se représente une deuxième fois. Avant de l'asseoir :
        <div class="bloc">if nom == fauteuils[0] or nom == fauteuils[1] or nom == fauteuils[2]:
    print("Tu es deja a l'interieur !")</div>
        <b>C'est exactement le test de la case occupée du jeu XO</b>, avec des fauteuils
        à la place des cases.</li></ul>""",
    fin="""<b>Quand ça marche :</b> teste les <b>trois situations</b> — quelqu'un qui entre normalement,
      quelqu'un qu'on refuse, et un <b>VIP de 30 ans</b> qui entre quand même avec le code.
      Puis fais entrer quatre personnes valables : la quatrième doit lire
      <span class="mono">Le club est COMPLET</span>. <b>Ctrl + S</b>, et
      <b>envoie une photo de ton écran</b> à ton enseignant.<br>
      <b>Les deux bugs les plus courants :</b> un <span class="mono">and</span> oublié entre deux
      questions (Python répond <span class="mono">SyntaxError</span>), et
      <span class="mono">entres = entres + 1</span> <b>oublié</b> — alors tout le monde s'assoit sur
      le fauteuil 1 et le club n'est jamais complet.""",
    cor_chapo="""Le programme complet. <b>Les visiteurs 2, 3 et 4 sont le bloc du visiteur 1,
      recopié tel quel</b> — il n'est imprimé qu'une fois ici, mais il doit bien apparaître
      quatre fois dans le fichier de l'élève.""",
    blocs=[(19, 52), (128, 143)],
    coupe_texte="""✂️ <b>Ici, dans le fichier de l'élève :</b> le bloc du visiteur 1 (de
      <span style="font-family:'Courier New',monospace">nom = input(...)</span> jusqu'au
      <span style="font-family:'Courier New',monospace">print</span> des fauteuils occupés)
      <b>recopié trois fois de plus</b>, pour les visiteurs 2, 3 et 4. Rien n'y change.
      Le fichier <span style="font-family:'Courier New',monospace">.py</span> du dossier
      <span style="font-family:'Courier New',monospace">a-envoyer/</span> contient les quatre blocs en entier.""",
    taille="8.1pt",
    cor_notes="""
      <div class="note"><h3>⭐ Les trois bonus</h3>
        <b>1. Le code en minuscules :</b>
        <span class="m">... or code == "GEEK2026" or code == "geek2026":</span><br>
        <b>2. Dis-lui pourquoi :</b> deux <span class="m">if</span> sans <span class="m">else</span>
        dans le refus — on peut être trop jeune <i>et</i> pas assez assidu.<br>
        <b>3. Déjà entré :</b>
        <span class="m">if nom == fauteuils[0] or nom == fauteuils[1] or nom == fauteuils[2]:</span>
        — c'est <b>mot pour mot</b> le test de la case occupée du jeu XO. Montrez le rapprochement :
        « tu viens de réécrire le cœur de notre jeu avec des fauteuils ».</div>
      <div class="note" style="border-color:#2fb765;background:#f2faf5">
        <h3 style="color:#0c5c29">✅ Les sept choses à regarder dans une copie</h3>
        <ul>
          <li>y a-t-il un <span class="m">and</span> entre <b>chaque</b> question ? (pas une virgule)</li>
          <li>les parenthèses encadrent-elles bien le groupe <b>âge + séances</b> ?</li>
          <li>le <span class="m">or</span> est-il <b>dehors</b> des parenthèses ?</li>
          <li><span class="m">entres = 0</span> est-il avant le premier visiteur, <b>une seule fois</b> ?</li>
          <li><span class="m">entres = entres + 1</span> est-il <b>dans</b> le <span class="m">if</span> qui accepte ?</li>
          <li><span class="m">fauteuils[entres]</span> — <b>sans</b> le −1 : ici le compteur part de 0.
              <b>C'est la faute n° 1</b>, et elle est normale : depuis trois séances on écrit
              <span class="m">case - 1</span>. Expliquez la différence au tableau.</li>
          <li>le rapport est-il <b>dehors</b> des blocs, collé à gauche ?</li>
        </ul>
        <div style="margin-top:1.6mm"><b>Le vrai signal de réussite :</b> l'élève a noté
        <b>combien de lignes il a recopiées</b> (étape 5). Demandez-le en classe avant d'écrire
        la première boucle : c'est le meilleur argument que vous aurez.</div></div>""",
)

# =====================================================================
#  3  -  LE DISTRIBUTEUR DE LA RECRE   (apres la seance 10 : while)
# =====================================================================
DISTRIB = dict(
    dossier="S10-la-boucle",
    css1="",
    base="exercice-maison-le-distributeur",
    base_cor="correction-le-distributeur",
    py="correction-distributeur.py",
    titre="Le Distributeur de la Récré",
    emoji="🥤",
    nom="LE DISTRIBUTEUR",
    kicker="EXERCICE DE MAISON · JEREMIAH GEEKS · SEMAINE DU 14 NOVEMBRE",
    fichier="distributeur_tonprenom.py",
    chapo="""Quatre produits, un porte-monnaie, et <b style="color:#fff">zéro bloc recopié</b>.
      La machine repropose son menu toute seule, encore et encore, tant qu'il te reste de l'argent.
      <b style="color:#fff">Ton programme va être plus court que celui de la semaine dernière</b> —
      et il fera dix fois plus de choses.""",
    regle="""🎯 <b>La règle :</b> la machine contient <b>quatre produits</b>, <b>un seul exemplaire</b>
      de chacun. Tu dis combien tu as d'argent. <b>Tant qu'il te reste au moins 100 F</b> et
      <b>qu'il reste quelque chose à acheter</b>, la machine réaffiche son menu. À la fin,
      elle imprime ton ticket.""",
    ecran="""========================================
      LE DISTRIBUTEUR DE LA RECRE
========================================

Combien as-tu d'argent ? <b>400</b>

----------------------------------------
 1. Chips - 100 F
 2. Jus - 150 F
 3. Chocolat - 200 F
 4. Gateau - 250 F
----------------------------------------
 Tu as 400 F.
 Ton choix (1 a 4) ? <b>3</b>

   CLONK !  Chocolat tombe dans le bac.

  ( ... le menu revient tout seul : la
    case 3 affiche EPUISE, il te reste
    200 F ... )

 Ton choix (1 a 4) ? <b>4</b>

   BZZZT !  Impossible : mauvais numero,
            produit epuise, ou pas assez
            d'argent.

  ( ... elle redemande. Tu prends le Jus,
    et la boucle s'arrete toute seule ... )

========================================
              TON TICKET
========================================
 Produits pris : 2 / 4
 Monnaie       : 50 F

 Plus assez d'argent. La recre est finie !
========================================""",
    kit="""<b>La boucle :</b><br>
      <span class="m">while argent &gt;= 100 and achats &lt; 4:</span><br>
      les <b>deux points</b> à la fin, et <b>tout ce qui se répète est décalé</b> dessous.
      <hr>
      <b>Deux listes qui vont ensemble :</b><br>
      <span class="m">produits = ["Chips", "Jus", ...]</span><br>
      <span class="m">prix = [100, 150, 200, 250]</span><br>
      Le produit n° 3, c'est <span class="m">produits[2]</span>,
      et il coûte <span class="m">prix[2]</span>. <b>Même indice.</b>
      <hr>
      <b>Donc :</b> <span class="m">prix[choix - 1]</span>
      <hr>
      <span class="m">!=</span> veut dire <b>est différent de</b>.
      <hr>
      ⚠️ <b>Si tu oublies <span class="m">achats = achats + 1</span></b>, la boucle
      <b>ne s'arrête jamais</b>. Pour arrêter un programme fou :
      <b>Ctrl + C</b> dans la fenêtre du bas.""",
    etapes1=[
        ("1", "LA MACHINE", """
         <ul><li>Affiche le cadre de <b>40</b> signes <span class="mono">=</span> et le titre.</li>
             <li>Crée <b>deux listes</b>, dans le même ordre :
               <div class="bloc">produits = ["Chips", "Jus", "Chocolat", "Gateau"]
prix     = [100, 150, 200, 250]</div>
               Les prix sont des <b>nombres</b> : pas de guillemets autour.</li></ul>"""),
        ("2", "LE CLIENT", """
         <ul><li>Demande <span class="mono">Combien as-tu d'argent ?</span>, range dans
             <span class="mono">argent</span>, et <b>transforme en nombre</b>.</li>
             <li>Crée le compteur <span class="mono">achats</span> à <b>0</b>.</li></ul>"""),
    ],
    etapes2=[
        ("3", "LA BOUCLE — et le menu dedans", """
         <div class="bloc">while argent &gt;= 100 and achats &lt; 4:

    <i>... à partir d'ici, TOUT est décalé de 4 espaces ...</i>
    print(" 1. " + produits[0] + " - " + str(prix[0]) + " F")
    <i>... les trois autres lignes du menu ...</i>
    print(" Tu as " + str(argent) + " F.")
    choix = input(" Ton choix (1 a 4) ? ")
    choix = int(choix)</div>
         <span class="tip">Lis la condition :</span> « tant qu'il me reste de quoi payer le
         <b>moins cher</b> (100) <b>et</b> qu'il reste un produit à prendre ». Les deux doivent
         être vraies pour continuer."""),
        ("4", "LA VENTE — toujours dans la boucle", """
         Quatre conditions pour une vente. Lis-les une par une :
         <div class="bloc">    if choix &gt;= 1 and choix &lt;= 4 and produits[choix - 1] != "EPUISE" and prix[choix - 1] &lt;= argent:
        print("   CLONK !  " + produits[choix - 1] + " tombe dans le bac.")
        argent = argent - prix[choix - 1]    <i>← on paie</i>
        produits[choix - 1] = "EPUISE"       <i>← le produit part</i>
        achats = achats + 1                  <i>← le compteur AVANCE</i></div>
         <b>Ces trois lignes vont ensemble.</b> Si tu enlèves la dernière, la boucle tourne pour
         toujours : c'est <b>la</b> panne de la semaine."""),
        ("5", "LE REFUS", """
         <div class="bloc">    else:
        print("   BZZZT !  Impossible : mauvais numero, produit epuise,")
        print("            ou pas assez d'argent.")</div>
         <b>Remarque :</b> en cas de refus, <b>rien ne change</b> — ni l'argent, ni le compteur.
         La boucle repart donc <b>exactement comme avant</b>, et redemande. C'est exactement ce
         qu'on veut (et exactement ce que fait notre jeu XO quand la case est prise)."""),
        ("6", "LE TICKET — DEHORS de la boucle", """
         <b>Recolle ces lignes tout à gauche</b> : elles ne doivent s'afficher
         <b>qu'une fois la boucle terminée</b>.
         <ul><li><span class="mono">Produits pris : &lt;achats&gt; / 4</span></li>
             <li><span class="mono">Monnaie       : &lt;argent&gt; F</span></li>
             <li><b>Si</b> <span class="mono">achats == 4</span> :
                 <span class="mono">TU AS VIDE LA MACHINE. Respect.</span> <b>Sinon</b> :
                 <span class="mono">Plus assez d'argent. La recre est finie !</span></li></ul>
         <span class="tip">Le test qui ne trompe pas :</span> si ton ticket s'affiche
         <b>après chaque achat</b>, c'est qu'il est resté décalé dans la boucle."""),
    ],
    bonus="""<ul>
      <li><b>Dis-lui ce qui manque.</b> Dans le refus :
        <span class="mono">print("   Il te manque " + str(prix[choix - 1] - argent) + " F.")</span></li>
      <li><b>Le bouton SORTIE.</b> Le client peut partir en tapant <b>0</b>. Il faut
        <span class="mono">choix = 1</span> <b>avant</b> la boucle, puis
        <div class="bloc">while argent &gt;= 100 and achats &lt; 4 and choix != 0:</div>
        <span class="tip">Pourquoi avant ?</span> Parce que Python lit la condition
        <b>avant</b> le premier tour : si <span class="mono">choix</span> n'existe pas encore,
        c'est <span class="mono">NameError</span>.</li>
      <li><b>⭐⭐ Un cinquième produit.</b> Ajoute <span class="mono">"Biscuit"</span> et
        <span class="mono">50</span> à la fin des deux listes, une ligne de menu, et remplace les 4
        par des 5. <b>Compte les lignes que tu as changées.</b> Sans boucle, il t'en aurait fallu
        dix fois plus : voilà ce que la boucle t'a donné.</li></ul>""",
    fin="""<b>Quand ça marche :</b> fais <b>trois parties</b> — une où tu vides la machine
      (il faut 700 F), une où tu tombes en panne d'argent, et une où tu demandes un produit
      <b>déjà épuisé</b>. Les trois doivent se terminer proprement sur un ticket.
      <b>Ctrl + S</b>, et <b>envoie une photo de ton écran</b> à ton enseignant.<br>
      <b>La panne de la semaine :</b> la boucle ne s'arrête plus. Dans 9 cas sur 10,
      <span class="mono">achats = achats + 1</span> manque, ou il est <b>collé à gauche</b> au lieu
      d'être dans le <span class="mono">if</span>. <b>Ctrl + C</b> arrête le programme,
      et on recompte les espaces.""",
    cor_chapo="""Le programme complet. Il tourne tel quel dans Thonny. <b>Le point à vérifier en
      premier dans une copie, c'est le décalage</b> : ce qui est dans la boucle, et ce qui n'y est pas.""",
    blocs=[(18, 59), (60, 75)],
    coupe_texte=None,
    taille="8.3pt",
    cor_notes="""
      <div class="note"><h3>⭐ Les trois bonus</h3>
        <b>1. Ce qui manque :</b> <span class="m">str(prix[choix - 1] - argent)</span> dans le refus.<br>
        <b>2. Le bouton SORTIE :</b> <span class="m">choix = 1</span> <b>avant</b> la boucle, puis
        <span class="m">and choix != 0</span> dans la condition. L'élève qui oublie l'initialisation
        récolte un <span class="m">NameError</span> : c'est une excellente leçon, laissez-la arriver.<br>
        <b>3. Le cinquième produit :</b> 4 lignes à changer. <b>Faites-les compter</b> — puis demandez
        combien il en aurait fallu dans la version « recopiée » de la semaine dernière.</div>
      <div class="note" style="border-color:#2fb765;background:#f2faf5">
        <h3 style="color:#0c5c29">✅ Les six choses à regarder dans une copie</h3>
        <ul>
          <li>les <b>deux points</b> à la fin de la ligne <span class="m">while</span> ?</li>
          <li>tout ce qui doit se répéter est-il <b>décalé</b> sous le <span class="m">while</span> ?</li>
          <li><span class="m">argent = argent - prix[choix - 1]</span> est-il <b>dans</b> le
              <span class="m">if</span> qui vend ? (sinon la machine fait payer sans rien donner)</li>
          <li><span class="m">achats = achats + 1</span> est-il là ? <b>Sans lui : boucle infinie.</b></li>
          <li>le <span class="m">- 1</span> est-il présent dans les deux listes ?</li>
          <li>le ticket est-il <b>dehors</b> de la boucle, collé à gauche ?</li>
        </ul>
        <div style="margin-top:1.6mm"><b>Si un élève arrive avec une boucle infinie :</b> ne corrigez pas
        tout de suite. Lancez-la, laissez défiler, puis <b>Ctrl + C</b> devant tout le monde, et
        demandez à la classe <i>« qu'est-ce qui ne change jamais ? »</i>. C'est la leçon la plus
        rentable de la séance 11.</div></div>""",
)

TOUS = [COFFRE, CLUB, DISTRIB]

# =====================================================================
#  4  -  LA BATAILLE NAVALE   (version renforcee du Coffre-Fort, seance 6)
# =====================================================================
NAVALE = dict(
    dossier="S06-le-plateau-se-souvient",
    css1=".goal pre{font-size:6.8pt;line-height:1.25}.kit .b{font-size:7.7pt;line-height:1.3}.kit hr{margin:1.2mm 0}.regle{font-size:9.3pt}",
    base="exercice-maison-la-bataille-navale",
    base_cor="correction-la-bataille-navale",
    py="correction-bataille-navale.py",
    titre="La Bataille Navale",
    emoji="\U0001F6A2",
    nom="LA BATAILLE NAVALE",
    kicker="EXERCICE RENFORC\u00c9 \u00b7 JEREMIAH GEEKS \u00b7 SEMAINE DU 17 OCTOBRE",
    fichier="navale_tonprenom.py",
    chapo="""La version <b style="color:#fff">difficile</b> de la semaine, avec
      <b style="color:#fff">exactement les m\u00eames outils</b> que Le Coffre-Fort \u2014 pas une notion de plus.
      Huit cases, <b style="color:#fff">trois bateaux cach\u00e9s</b>, quatre tirs, et une id\u00e9e neuve&nbsp;:
      <b style="color:#fff">une bo\u00eete t\u00e9moin</b> qui retient ce qui vient de se passer.""",
    regle="""\U0001F3AF <b>La r\u00e8gle du jeu :</b> joueur 2 cache <b>trois bateaux</b> dans trois cases
      diff\u00e9rentes, de 1 \u00e0 8. Joueur 1 a <b>quatre tirs</b>. Un bateau touch\u00e9 vaut <b>+30</b>,
      un tir dans l'eau co\u00fbte <b>\u221210</b>. La mer garde la trace&nbsp;: <b>X</b> pour un bateau coul\u00e9,
      <b>o</b> pour un trou dans l'eau.""",
    ecran="""========================================
           LA BATAILLE NAVALE
========================================
 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8

Joueur 1, ferme les yeux !
Joueur 2, premier bateau  (1 a 8) ? <b>2</b>
Joueur 2, deuxieme bateau (1 a 8) ? <b>5</b>
Joueur 2, troisieme bateau (1 a 8) ? <b>7</b>

========================================
   Joueur 1, tu peux regarder !
   3 bateaux caches. Tu as 4 tirs.
========================================
Tir 1 - quelle case ? <b>2</b>
   TOUCHE ! Un bateau coule.

 1 | X | 3 | 4 | 5 | 6 | 7 | 8
 Score : 30   Bateaux coules : 1 / 3

Tir 2 - quelle case ? <b>1</b>
   PLOUF ! Rien que de l'eau.

 o | X | 3 | 4 | 5 | 6 | 7 | 8
 Score : 20   Bateaux coules : 1 / 3

   ( ... les tirs 3 et 4 : 5 puis 7 ... )

========================================
Les bateaux etaient en 2, 5 et 7.
Score final : 80

FLOTTE COULEE. Tu es AMIRAL !
Et quel tir ! Score de professionnel.
========================================""",
    kit="""<b>La mer, c'est une liste de HUIT :</b><br>
      <span class="m">mer = ["1", "2", ..., "8"]</span><br>
      donc les indices vont de <b>0 \u00e0 7</b>.
      <hr>
      <b>Marquer une case :</b><br>
      <span class="m">mer[tir - 1] = "X"</span>
      <hr>
      \U0001F195 <b>LA BO\u00ceTE T\u00c9MOIN.</b> Elle retient si quelque chose
      s'est pass\u00e9&nbsp;:<br>
      <span class="m">touche = 0</span> &nbsp;avant de poser les questions<br>
      <span class="m">touche = 1</span> &nbsp;si on a trouv\u00e9 un bateau<br>
      puis <span class="m">if touche == 1:</span> pour d\u00e9cider.
      <hr>
      <b>Trois <span class="m">if</span> \u00e0 la suite</b>, coll\u00e9s \u00e0 gauche l'un sous l'autre.
      Ils ne s'emp\u00eachent pas&nbsp;: Python les lit tous les trois.
      <hr>
      <b>DEUX compteurs qui avancent ensemble :</b><br>
      <span class="m">score = score + 30</span> ou <span class="m">score = score - 10</span><br>
      <span class="m">touches = touches + 1</span>
      <hr>
      <span class="m">int()</span> pour les cases, <span class="m">str()</span> pour les afficher.""",
    etapes1=[
        ("1", "LA MER", """
         <ul><li>Affiche un cadre de <b>40</b> signes <span class="mono">=</span> et le titre.</li>
             <li>Cr\u00e9e la liste <span class="mono">mer</span> avec les <b>huit</b> num\u00e9ros,
                 entre guillemets.</li>
             <li>Affiche la ligne de mer. Elle est longue&nbsp;: \u00e9cris-la <b>une fois</b>, puis
                 <b>copier-coller</b> \u2014 tu en auras besoin <b>cinq</b> fois.
               <div class="bloc">print(" " + mer[0] + " | " + mer[1] + " | " + <i>... jusqu'\u00e0 ...</i> + mer[7])</div></li></ul>"""),
        ("2", "LES TROIS BATEAUX", """
         <ul><li>Affiche <span class="mono">Joueur 1, ferme les yeux !</span></li>
             <li><b>Trois questions</b> au joueur 2, rang\u00e9es dans <span class="mono">b1</span>,
                 <span class="mono">b2</span> et <span class="mono">b3</span> \u2014 et <b>trois</b>
                 <span class="mono">int()</span>, un par bateau.</li>
             <li>Affiche le cadre <span class="mono">3 bateaux caches. Tu as 4 tirs.</span></li></ul>
         <div style="margin-top:1.2mm"><span class="tip">On fait confiance au joueur 2 :</span>
         il doit choisir <b>trois cases diff\u00e9rentes</b>. V\u00e9rifier \u00e7a, on saura le faire
         dans trois semaines.</div>"""),
        ("3", "LES DEUX COMPTEURS", """
         <span class="mono">score</span> \u00e0 <b>0</b>, et <span class="mono">touches</span> \u00e0 <b>0</b>.
         <b>Une seule fois chacun</b>, avant le premier tir.
         <div style="margin-top:1.2mm"><span class="tip">Pourquoi deux ?</span> Parce qu'ils ne disent pas
         la m\u00eame chose&nbsp;: l'un mesure <b>l'adresse</b>, l'autre dit si <b>la mission</b> est remplie.</div>"""),
    ],
    etapes2=[
        ("4", "LE TIR N\u00b0 1 \u2014 tout l'exercice est l\u00e0", """
         Demande la case, transforme-la en nombre, puis&nbsp;:
         <div class="bloc">touche = 0                  <i>\u2190 la bo\u00eete t\u00e9moin, remise \u00e0 z\u00e9ro</i>

if tir == b1:
    touche = 1
if tir == b2:
    touche = 1
if tir == b3:
    touche = 1               <i>\u2190 trois if, coll\u00e9s \u00e0 gauche</i>

if touche == 1:
    print("   TOUCHE ! Un bateau coule.")
    mer[tir - 1] = "X"
    score = score + 30
    touches = touches + 1
else:
    print("   PLOUF ! Rien que de l'eau.")
    mer[tir - 1] = "o"
    score = score - 10</div>
         Puis <b>r\u00e9affiche la mer</b>, le score et le nombre de bateaux coul\u00e9s.
         <div style="margin-top:1.2mm"><span class="tip">Lis le bloc \u00e0 voix haute :</span>
         \u00ab je ne sais rien (0) \u2192 je pose mes trois questions \u2192 je regarde ce que la bo\u00eete
         retient \u2192 je d\u00e9cide. \u00bb Si tu sais le dire, tu sais l'\u00e9crire."""),
        ("5", "LES TIRS N\u00b0 2, 3 ET 4", """
         <b>Recopie tout le bloc de l'\u00e9tape 4, trois fois de plus.</b> Tu ne changes que le num\u00e9ro
         dans la question (<span class="mono">Tir 2</span>, <span class="mono">Tir 3</span>,
         <span class="mono">Tir 4</span>).
         <div style="margin-top:1.2mm">\u26a0\ufe0f <b>Le pi\u00e8ge de l'exercice :</b> la ligne
         <span class="mono">touche = 0</span> doit \u00eatre <b>dans chaque bloc</b>. Si tu ne l'\u00e9cris
         qu'une seule fois tout en haut, alors d\u00e8s que tu touches un bateau, <b>tous les tirs
         suivants seront compt\u00e9s comme touch\u00e9s</b> \u2014 et tu finiras amiral sans rien avoir coul\u00e9.
         <b>Teste-le expr\u00e8s</b>, pour voir.</div>"""),
        ("6", "LES DEUX VERDICTS", """
         <ul><li>Affiche o\u00f9 \u00e9taient les trois bateaux, et le score final \u2014 il faudra
             <span class="mono">str()</span>.</li>
             <li><b>Premier verdict \u2014 la mission :</b> <b>si</b> <span class="mono">touches == 3</span>,
             <span class="mono">FLOTTE COULEE. Tu es AMIRAL !</span> <b>sinon</b>
             <span class="mono">Il reste des bateaux a flot...</span></li>
             <li><b>Deuxi\u00e8me verdict \u2014 le tir :</b> <b>si</b> <span class="mono">score &gt;= 60</span>,
             <span class="mono">Score de professionnel.</span> <b>sinon</b>
             <span class="mono">Le tir demande de l'entrainement.</span></li></ul>
         <div style="margin-top:1.2mm"><span class="tip">Les deux sont ind\u00e9pendants :</span>
         deux <span class="mono">if</span> / <span class="mono">else</span> l'un <b>sous</b> l'autre,
         coll\u00e9s \u00e0 gauche. Pas l'un dans l'autre.</div>"""),
    ],
    bonus="""<ul>
      <li><b>Un cinqui\u00e8me tir.</b> Recopie encore le bloc. <b>Compte les lignes que tu recopies</b>
        et note le nombre sur ta feuille&nbsp;: on te le demandera.</li>
      <li><b>La pr\u00e9cision.</b> Avant le verdict, affiche le nombre de tirs rat\u00e9s&nbsp;:
        <span class="mono">rates = 4 - touches</span></li>
      <li><b>\u2b50\u2b50 Le tir d\u00e9j\u00e0 jou\u00e9.</b> Retirer au m\u00eame endroit ne devrait pas rapporter
        30 points une deuxi\u00e8me fois. Une case o\u00f9 personne n'a encore tir\u00e9
        <b>contient encore son num\u00e9ro</b>&nbsp;:
        <div class="bloc">if mer[tir - 1] == str(tir):
    <i>... tout le bloc du tir ...</i>
else:
    print("Tu as deja tire la !")</div>
        <b>Celui qui r\u00e9ussit ce bonus a d\u00e9j\u00e0 compris la s\u00e9ance de samedi prochain.</b></li></ul>""",
    fin="""<b>Quand \u00e7a marche :</b> joue <b>trois parties</b> \u2014 une o\u00f9 tu coules tout,
      une o\u00f9 tu raterais tout (le score doit tomber \u00e0 <b>\u221240</b>), et une o\u00f9 tu tires
      <b>deux fois au m\u00eame endroit</b> pour voir ce que fait ton programme. Puis <b>Ctrl + S</b>,
      et <b>envoie une photo de ton \u00e9cran</b>.<br>
      <b>Les deux bugs les plus courants :</b> <span class="mono">touche = 0</span> \u00e9crit une seule
      fois tout en haut au lieu d'\u00eatre dans chaque bloc \u2014 et <span class="mono">mer[tir]</span>
      sans le <span class="mono">- 1</span>, qui marque <b>la case d'\u00e0 c\u00f4t\u00e9</b> sans que Python
      ne dise rien.""",
    cor_chapo="""Le programme complet. <b>Les tirs 2, 3 et 4 sont le bloc du tir 1, recopi\u00e9 tel
      quel</b>&nbsp;: il n'est imprim\u00e9 qu'une fois ici, mais il doit appara\u00eetre <b>quatre fois</b>
      dans le fichier de l'\u00e9l\u00e8ve.""",
    blocs=[(19, 83), (172, 190)],
    coupe_texte="""\u2702\ufe0f <b>Ici, dans le fichier de l'\u00e9l\u00e8ve :</b> le bloc du tir 1 (depuis
      <span style="font-family:'Courier New',monospace">tir = input(...)</span> jusqu'\u00e0 l'affichage
      du score) <b>recopi\u00e9 trois fois de plus</b>, pour les tirs 2, 3 et 4. Seul le num\u00e9ro dans la
      question change. Le fichier
      <span style="font-family:'Courier New',monospace">.py</span> du dossier
      <span style="font-family:'Courier New',monospace">a-envoyer/</span> contient les quatre blocs en entier.""",
    taille="8.1pt",
    cor_notes="""
      <div class="note"><h3>\u2b50 Les trois bonus</h3>
        <b>1. Un cinqui\u00e8me tir :</b> recopier le bloc. Le chiffre de lignes recopi\u00e9es est \u00e0
        r\u00e9clamer&nbsp;: il resservira \u00e0 la s\u00e9ance 10.<br>
        <b>2. La pr\u00e9cision :</b> <span class="m">rates = 4 - touches</span>, puis un
        <span class="m">str()</span> pour l'afficher.<br>
        <b>3. Le tir d\u00e9j\u00e0 jou\u00e9 :</b> <span class="m">if mer[tir - 1] == str(tir):</span> \u2014
        c'est <b>mot pour mot</b> le test de la case libre de la <b>s\u00e9ance 7</b>. L'\u00e9l\u00e8ve qui
        le r\u00e9ussit arrive samedi avec une s\u00e9ance d'avance&nbsp;: faites-le expliquer au tableau
        par lui.</div>
      <div class="note" style="border-color:#2fb765;background:#f2faf5">
        <h3 style="color:#0c5c29">\u2705 Les sept choses \u00e0 regarder dans une copie</h3>
        <ul>
          <li>la liste a-t-elle <b>huit</b> cases, et l'affichage va-t-il de
              <span class="m">mer[0]</span> \u00e0 <span class="m">mer[7]</span>&nbsp;?</li>
          <li>le <span class="m">- 1</span> est-il pr\u00e9sent dans <span class="m">mer[tir - 1]</span>&nbsp;?</li>
          <li><b>LA FAUTE N\u00b0 1 \u2014 et c'est elle qu'on vient chercher&nbsp;:</b>
              <span class="m">touche = 0</span> doit \u00eatre remis \u00e0 z\u00e9ro <b>dans chaque bloc de tir</b>.
              \u00c9crit une seule fois tout en haut, l'\u00e9l\u00e8ve devient amiral sans rien couler.
              <b>Ne le dites pas&nbsp;: faites-lui jouer une partie et constater.</b></li>
          <li>les trois <span class="m">if</span> sont-ils <b>ind\u00e9pendants</b>, coll\u00e9s \u00e0 gauche
              l'un sous l'autre \u2014 et non imbriqu\u00e9s&nbsp;?</li>
          <li><span class="m">score</span> et <span class="m">touches</span> sont-ils cr\u00e9\u00e9s
              <b>une seule fois</b>, avant le tir 1&nbsp;?</li>
          <li><span class="m">touches = touches + 1</span> est-il <b>dans le if</b>, et pas dans le else&nbsp;?</li>
          <li>les deux verdicts de la fin sont-ils <b>s\u00e9par\u00e9s</b>&nbsp;?</li>
        </ul>
        <div style="margin-top:1.6mm"><b>\u00c0 qui le donner.</b> C'est l'exercice de ceux qui ont fini
        Le Coffre-Fort en vingt minutes, ou qui l'avaient d\u00e9j\u00e0 fait. <b>On ne donne pas les deux</b>&nbsp;:
        un seul exercice par \u00e9l\u00e8ve, et les autres gardent Le Coffre-Fort. La bo\u00eete \u00e0 outils est
        <b>exactement la m\u00eame</b>&nbsp;: aucune notion nouvelle, seulement un assemblage plus exigeant.</div></div>""",
)

TOUS.append(NAVALE)
