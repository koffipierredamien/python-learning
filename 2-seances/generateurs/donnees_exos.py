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
