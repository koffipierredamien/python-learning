# 🤖 Script pour Gemini — refaire ou retravailler le diaporama

Le diaporama est déjà prêt : **[`seance-1-projection.pptx`](seance-1-projection.pptx)**, 46 diapositives,
avec les notes de l'animateur sur chacune.

Ce fichier-ci sert si vous voulez que **Gemini** le refasse, le restyle, l'illustre avec de vraies photos,
ou le reconstruise directement dans **Google Slides**. Copiez-collez les blocs ci-dessous.

---

## Comment s'en servir

| Où | Quoi faire |
|---|---|
| **Gemini dans Google Slides** *(le plus simple)* | Ouvrez une présentation vide → panneau Gemini → collez le **BLOC 1**, puis le 2, puis le 3. Les diapos se créent directement. |
| **L'application Gemini** | Collez le **BLOC 0** (le cadrage), puis les blocs 1 à 3. Demandez un export en `.pptx`. |
| **Retravailler le fichier existant** | Ouvrez le `.pptx` dans Google Slides, puis demandez à Gemini : *« garde le texte et la structure, remplace les emoji par de vraies photos libres de droits, et harmonise »*. |

> ⚠️ **Ne collez pas les quatre blocs d'un coup.** Au-delà d'une quinzaine de diapositives par demande,
> Gemini raccourcit, fusionne ou oublie des diapos. Allez-y bloc par bloc, et vérifiez entre chaque.
>
> ⚠️ **Les emoji sont des marqueurs visuels de dépannage.** Si vous pouvez, demandez à Gemini de les
> remplacer par de vraies images. Pour les portraits, demandez explicitement **des photos libres de droits
> ou des illustrations** : Gemini n'a pas le droit de générer le visage d'une personne réelle.

---

## BLOC 0 — le cadrage (à coller en premier)

```
Tu es directeur artistique et concepteur pédagogique. Tu dois produire un diaporama de
présentation destiné à être PROJETÉ pendant un cours de programmation Python pour des
enfants de 9 à 12 ans et des adolescents de 12 à 18 ans, en français.

CONTEXTE
- Cours du samedi 12 septembre 2026, de 12 h à 14 h. C'est la toute première séance.
- Le projet de l'année : les élèves construisent le jeu XO (morpion) en 22 samedis.
- Le diaporama couvre TOUT ce qui est projeté pendant la séance.
- L'animateur parle : les diapos ne doivent JAMAIS contenir son discours, seulement
  l'idée forte, en très gros. Le discours va dans les NOTES de l'orateur.

RÈGLES DE CONCEPTION, à respecter sans exception
1. Format 16:9.
2. Palette (n'en utilise aucune autre) :
   - bleu nuit   #12122A  (fond des diapos sombres)
   - nuit clair  #20204A  (cartes sur fond sombre)
   - blanc cassé #F7F7FB  (fond des diapos claires)
   - encre       #14142B  (texte sur fond clair)
   - cyan        #4FC3F7  (accent lumineux ; version foncée #13678F sur fond clair)
   - orange      #FFB74D  (accent chaud ; version foncée #A65D00 sur fond clair)
   - violet      #B06FD8  (accent ; version foncée #6B2D8F sur fond clair)
   - vert        #2FB765  (validation ; version foncée #0C5C29 sur fond clair)
   Le cyan et l'orange viennent des symboles X et O du jeu que les élèves vont construire.
3. Alternance imposée : les diapositives de TITRE, de SÉPARATION et de CITATION sont
   sur fond bleu nuit ; les diapositives de CONTENU sont sur fond blanc cassé.
4. Typographie : une seule famille sans serif (Calibri ou Arial). Titres 36 à 44 pt en gras,
   sous-titres 20 à 24 pt, corps 14 à 18 pt, chiffres de mise en avant 60 à 90 pt.
5. Motif récurrent : une petite grille de morpion 3x3 en carrés arrondis, discrète,
   dans un coin. Elle revient sur chaque diapositive. C'est la signature visuelle.
6. Chaque diapositive porte son HORAIRE en petit, en bas à droite (ex. « 12 h 34 »).
7. INTERDITS : aucune barre de couleur décorative, aucun trait sous les titres, aucun
   texte centré pour les paragraphes (seuls les titres peuvent être centrés), aucune
   diapositive composée uniquement d'un titre et de puces, jamais plus de 25 mots
   sur une diapositive de contenu.
8. Contenus obligatoires : cartes arrondies à ombre douce, pastilles rondes colorées
   pour les numéros, gros chiffres en évidence, et des blocs reliés par des flèches
   pour les enchaînements.
9. Pour chaque diapositive, écris les NOTES DE L'ORATEUR : ce que l'enseignant dit,
   au style direct, entre guillemets.

Réponds seulement « prêt », et j'envoie le contenu diapositive par diapositive.
```

---

## BLOC 1 — ouverture et théorie, 1/2 *(diapositives 1 à 25)*

```
Crée les diapositives 1 à 25, en appliquant les règles envoyées.

1. [SOMBRE] Surtitre « JERUSALEM GEEKS · JEREMIAH GEEKS ». Titre géant « LE JEU XO »
   avec le X en cyan et le O en orange. Sous-titre « Séance 1 — Le Décollage ».
   Ligne de date « samedi 12 septembre 2026 · 12 h - 14 h ». Phrase en cyan :
   « Aujourd'hui, vous devenez ceux qui écrivent. »
2. [SOMBRE] Une seule idée, centrée : « Prière ». Sous-titre : « Comme chaque samedi,
   on commence par là. » Horaire 12 h - 12 h 15.
3. [SOMBRE] En très gros, centré : « REGARDEZ L'ÉCRAN. » Puis, en cyan :
   « Il me faut un volontaire. » Notes : l'enseignant lance le jeu terminé et perd
   une partie contre un élève.
4. [CLAIRE] Titre « 22 samedis. Une brique à la fois. » Une frise de 12 petites cartes
   numérotées : 1 Le jeu dit bonjour (mise en avant en vert) · 2 Il demande ton nom ·
   3 Les 2 joueurs · 4 Le plateau s'affiche · 5 Les cases numérotées · 6 On place un X ·
   7 X et O à tour de rôle · 8 PREMIÈRE DÉMO (mise en avant) · 9 Coups interdits ·
   10 Le compte des tours · 11 Le code se range · 12 Le gagnant détecté.
   Bas de diapo : « On avance ENSEMBLE : une case par samedi, pour toute la classe. »
5. [CLAIRE] Titre « De Novice à Maître Geek ». Six pastilles en ligne reliées par des
   chevrons : Novice · Apprenti Codeur · Codeur · Ingénieur · Architecte · Maître Geek,
   en dégradé du gris clair au bleu nuit. Puis : « Un grade ne s'obtient pas en venant.
   Il s'obtient quand ton programme marche, que tu sais l'expliquer, et que tu sais
   le refaire. »
6. [SOMBRE] Titre « Ce que je vous promets ». Trois cartes numérotées 1, 2, 3 :
   « Chaque samedi, ton jeu marchera mieux qu'en arrivant » / « Il n'y a AUCUNE note.
   Jamais. » / « Si tu es absent, tu ne seras PAS en retard. »
7. [SOMBRE] Titre « Ce que je vous demande ». Trois lignes avec une icône :
   « On ne se moque JAMAIS de quelqu'un qui n'a pas compris » / « On ne dit pas je suis
   nul, on dit je n'ai pas encore trouvé » / « On essaie, même quand on n'est pas sûr ».
8. [SOMBRE — SÉPARATION] Grande pastille « 1 ». Titre « POURQUOI CODER ? ».
   Sous-titre en cyan « De celui qui utilise… à celui qui écrit. »
9. [CLAIRE] Titre « Ce matin, combien d'ordres avez-vous donnés à une machine ? »
   Six cartes avec icône : allumer un téléphone · envoyer un message · mettre de la
   musique · retirer de l'argent · regarder l'heure · lancer une vidéo. Conclusion en
   gras : « Chacun de ces gestes, une machine l'a exécuté parce que quelqu'un, un jour,
   lui a écrit quoi faire. »
10. [CLAIRE] Deux blocs face à face, reliés par une grosse flèche : à gauche, en gris,
    « AUJOURD'HUI — vous utilisez ce que d'autres ont écrit » ; à droite, sur fond violet,
    « À PARTIR DE MAINTENANT — vous devenez ceux qui écrivent ». En bas, trois items :
    FABRIQUER des outils qui n'existent pas encore · RÉSOUDRE de vrais problèmes autour
    de vous · COMPRENDRE le monde où vous vivez.
11. [SOMBRE — SÉPARATION] Pastille « 2 ». Titre « OÙ SE CACHE LE CODE ? ».
    Sous-titre « Dans absolument tous les métiers. On vérifie. »
12. [CLAIRE] Titre « Il y a du code là-dedans ? » Grille de 9 cartes avec icône et
    libellé : les jeux vidéo · la santé · l'agriculture · la musique · les transports ·
    l'argent · le cinéma · l'espace · le sport. Dans la dernière case libre :
    « On lève la main : oui ou non ? »
13. [SOMBRE — CITATION] « Dans quel domaine n'y a-t-il PAS de code ? Il n'y en a aucun. »
    Sous-titre : « Ce que vous apprenez ici servira dans le métier que vous choisirez —
    quel qu'il soit. »
14. [SOMBRE — SÉPARATION] Pastille « 3 ». Titre « CEUX QUI L'ONT FAIT ».
    Sous-titre en cyan : « Certains avaient votre âge. »
15 à 23. NEUF DIAPOSITIVES DE PORTRAIT, toutes bâties sur le même gabarit :
    une carte verticale sombre à gauche (un tiers de la largeur) avec une illustration,
    le nom sur deux lignes, le pays avec son drapeau, et — quand il y en a un — un
    bandeau coloré avec l'âge en gros ; à droite, un titre fort, un paragraphe de
    trois lignes, et une phrase de chute en couleur.
    15. Mark Zuckerberg, États-Unis. Titre : « Il a écrit Facebook dans sa chambre
        d'étudiant. » Texte : Facebook, Instagram, WhatsApp, un seul homme a lancé tout ça ;
        la première version codée à 19 ans dans sa chambre. Chute : « Mais voilà ce qu'on
        ne vous dit pas : il a commencé à coder vers 12 ans. »
    16. Elon Musk, Afrique du Sud / États-Unis, bandeau « à 12 ans ». Titre : « À 12 ans,
        il a vendu son premier jeu vidéo. » Chute : « Il a codé un jeu, Blastar, et un
        magazine d'informatique le lui a acheté. Douze ans. »
    17. [SOMBRE] Transition en très gros : « ET MAINTENANT, TROIS JEUNES QUI N'ONT PAS
        ATTENDU D'ÊTRE GRANDS. »
    18. Thomas Suarez, États-Unis, bandeau « à 12 ans ». Titre : « À 12 ans, il fabriquait
        des applications dans sa chambre. » Chute : « Sa vidéo a été vue des millions
        de fois. Il avait 12 ans. »
    19. Nick D'Aloisio, Royaume-Uni, bandeau « à 15 ans ». Titre : « À 15 ans, il a codé
        une application qui résume les articles. » Chute : « Deux ans plus tard, à 17 ans,
        une très grande entreprise a racheté son application. Il était encore au lycée. »
    20. Gitanjali Rao, États-Unis, bandeau « à 11 ans ». Titre : « À 11 ans, elle a inventé
        un appareil qui détecte le poison dans l'eau. » Texte : elle avait entendu parler
        d'une ville où l'eau du robinet était empoisonnée au plomb ; puis elle a créé une
        application qui repère les messages méchants. Chute : « À 15 ans, un grand magazine
        l'a nommée enfant de l'année. Le code sert à régler de vrais problèmes. »
    21. [SOMBRE] Transition : « ET PRÈS DE CHEZ NOUS ? DEUX HISTOIRES DE CHEZ NOUS. »
    22. Charlette N'Guessan, Côte d'Ivoire. Titre : « Elle a créé un logiciel qui reconnaît
        les visages. » Texte : avec son équipe, un programme qui vérifie l'identité d'une
        personne à distance, pour que les banques africaines ne se fassent plus voler des
        identités. Chute : « En 2020, elle a gagné un grand prix africain d'ingénierie.
        La première femme à le remporter. »
    23. Kelvin Doe, Sierra Leone, bandeau « à 13 ans ». Titre : « À 13 ans, il a construit
        sa radio avec des déchets. » Texte : pas d'électricité tous les jours chez lui ;
        avec des morceaux ramassés dans les poubelles, une batterie, puis son propre
        émetteur radio. Chute : « Une grande université américaine l'a fait venir chez elle. »
24. [SOMBRE] La diapositive la plus importante. Surtitre « REGARDEZ BIEN LEURS ÂGES. »
    Quatre chiffres géants côte à côte, chacun d'une couleur différente, avec le prénom
    en dessous : 12 Thomas · 15 Nick · 11 Gitanjali · 13 Kelvin. Puis :
    « Aucun d'eux n'était un génie. Aucun n'avait de matériel extraordinaire. Aucun d'eux
    n'a commencé en sachant coder. » Et en orange, plus gros : « Ils ont tous commencé
    exactement là où vous êtes assis aujourd'hui. La seule différence : ils ont commencé. »
25. [CLAIRE] Titre « Et tout ça s'écrit dans un langage. » À gauche, une carte avec
    « PYTHON » en très gros et « le langage que vous allez apprendre aujourd'hui même ».
    À droite : « Guido van Rossum — c'est lui qui a créé Python. Il voulait un langage
    simple, lisible, qu'un débutant puisse comprendre sans être ingénieur. »
    Chute : « C'est exactement pour ça qu'on l'a choisi pour vous. »
```

---

## BLOC 2 — théorie 2/2 et test *(diapositives 26 à 38)*

```
Continue avec les diapositives 26 à 38, mêmes règles.

26. [SOMBRE — SÉPARATION] Pastille « 4 ». Titre « COMMENT LA MACHINE COMPREND ».
    Sous-titre « Du courant électrique… jusqu'à vos mots. »
27. [CLAIRE] Titre « La machine ne connaît que deux états. » Deux grandes cartes
    côte à côte : « 0 — ASSIS — le courant ne passe pas » (gris) et « 1 — DEBOUT —
    le courant passe » (cyan). En dessous : « Alors on va écrire une lettre. La lettre A,
    pour une machine, c'est : » suivi de huit cases carrées 0 1 0 0 0 0 0 1, les « 1 »
    en cyan plein, puis « = A » en orange.
28. [SOMBRE — CITATION] « Vous imaginez écrire un jeu entier comme ça ? Personne ne veut
    faire ça. » Sous-titre : « Alors on a inventé des langages pour parler à la machine
    avec des mots. »
29. [CLAIRE] Titre « Ce qui se passe quand j'appuie sur F5 ». Cinq blocs reliés par des
    flèches : MOI (j'écris dans Thonny) → PYTHON (print("Bonjour") — des mots !) →
    L'INTERPRÈTE (il traduit) → 0 et 1 (01110000…) → LA MACHINE (elle obéit, elle affiche).
    En dessous, « Trois mots à retenir » : PYTHON = la LANGUE dans laquelle j'écris mes
    ordres · L'INTERPRÈTE = le TRADUCTEUR qui transforme mes mots en 0 et 1 ·
    THONNY = l'ÉDITEUR, ma feuille avec un bouton « vas-y ».
30. [SOMBRE — CITATION] « L'ordinateur n'est pas intelligent. Il est OBÉISSANT. »
    Sous-titre : « Il fait exactement ce qui est écrit. Ni plus, ni moins. S'il fait une
    bêtise, ce n'est pas lui qui s'est trompé. »
31. [SOMBRE — SÉPARATION] Pastille « 5 ». Titre « L'ALGORITHME ». Sous-titre :
    « La partie la plus difficile du métier. Et vous savez déjà le faire. »
32. [CLAIRE] Titre « Voici un robot. Il ne comprend que 3 ordres. » Trois cartes avec
    flèche : AVANCE · TOURNE À GAUCHE · TOURNE À DROITE. Puis : « Il n'a pas d'imagination.
    Il fait EXACTEMENT ce qu'on lui dit, ni plus, ni moins. » Et un bandeau violet :
    « VOTRE MISSION, TOUS ENSEMBLE — l'amener jusqu'au tableau, et lui faire écrire un X. »
33. [SOMBRE — CITATION] « Ce que vous venez d'écrire, ça s'appelle un ALGORITHME. »
    Sous-titre : « Une suite d'ordres précis, donnés dans le bon ordre, pour arriver
    à un résultat. »
34. [CLAIRE] Titre « Vous en connaissez déjà plein ». Trois cartes : une recette de
    cuisine (les étapes, dans l'ordre) · un itinéraire (tourne ici, puis tout droit) ·
    les règles du morpion (et c'est celui-là qu'on va écrire) — cette dernière mise en
    avant. Bandeau sombre en bas : « ATTENTION : un algorithme, ce n'est pas encore du
    code. C'est la réflexion AVANT le code. On peut l'écrire en français, sur du papier,
    sans ordinateur. »
35. [SOMBRE] « PAUSE » en très gros, centré. « 10 minutes. Levez-vous, sortez, bougez. »
    Et un bandeau orange : « Retour à 13 h 05 ».
36. [SOMBRE — SÉPARATION] Pastille « 6 ». Titre « LES MISSIONS DE DÉCOLLAGE ».
    Sous-titre : « Trois missions. Ce n'est pas noté. Personne ne peut échouer. »
37. [CLAIRE] Titre « Trois missions, huit minutes chacune ». Trois cartes :
    MISSION 1 PILOTAGE (aux ordinateurs, 6 manœuvres à réussir) · MISSION 2 LOGIQUE
    (sur papier, sans machine, 4 énigmes) · MISSION 3 IDENTITÉ (ta fiche de Geek, pour
    qu'on te connaisse). Bandeau vert : « Ce n'est pas noté. Il n'y a pas de bonne ou de
    mauvaise équipe. Tout le monde décolle. »
38. [SOMBRE] « ET MAINTENANT… ON ALLUME LES MACHINES. » en très gros.
```

---

## BLOC 3 — la machine, le quiz, la clôture *(diapositives 39 à 46)*

```
Termine avec les diapositives 39 à 46, mêmes règles.

39. [CLAIRE] Titre « Ici, on ne lève pas la main. On lève une carte. » Quatre cartes
    avec une grosse pastille de couleur : VERT (ça avance, tout va bien) · ORANGE
    (on est bloqués, on cherche quand même) · ROUGE (rien ne marche, au secours) ·
    BLEU (on a fini, on peut aider). Bandeau sombre : « Ma promesse : une carte orange
    est servie en moins de 5 minutes. Une carte rouge, tout de suite. »
40. [CLAIRE] Titre « Bloqué ? Trois choses avant de lever l'orange. » Trois lignes
    numérotées : 1 JE RELIS la consigne, puis le message rouge — À VOIX HAUTE ·
    2 JE DEMANDE À MON VOISIN, et on regarde la fiche mémo · 3 ON DEMANDE AU BINÔME
    D'À CÔTÉ, 30 secondes pas plus. Bandeau orange : « Toujours bloqués ? CARTE ORANGE. »
41. [CLAIRE] Titre « Votre première commande ». Un grand bloc de code sur fond sombre,
    en police à espacement fixe, texte vert : print("Bonjour"). Puis trois lignes
    d'explication : print = AFFICHE, toujours tout en minuscules · ( … ) = ce qu'on ouvre,
    on le ferme, toujours · " … " = du texte se met toujours entre DEUX guillemets.
    Bas de diapo : « Avant que j'appuie : qu'est-ce qui va se passer ? À trois.
    Un, deux, trois ! »
42. [CLAIRE] Titre « Et maintenant, je casse tout. » À gauche, un bloc de code sombre
    avec print("Bonjour) en rouge ; à droite, un bloc rouge pâle avec « SyntaxError ».
    Puis : « Syntax = la grammaire. Error = l'erreur. Il nous dit : je ne comprends pas
    ta phrase. » Et un grand bandeau sombre, texte orange en très gros :
    « LE ROUGE N'EST PAS GRAVE. LE ROUGE EST UNE INFORMATION. »
43. [CLAIRE] Titre « À vous. Votre mission : ». À gauche, un bloc de code sombre montrant
    le résultat attendu (un encadré de signes égal, BIENVENUE DANS LE JEU XO, « Cree par :
    (ton prenom) », « Age du createur : (ton age) ans », « Prepare-toi a perdre ! »).
    À droite, quatre étapes numérotées : appuyez sur F5 tout de suite, avant d'avoir rien
    écrit · remplacez chaque ____ · relancez après CHAQUE changement · enregistrez.
    Bandeau vert : « Le fichier est déjà ouvert sur votre écran. Cartes de signalisation
    sorties. C'est parti ! »
44. [SOMBRE] « KAHOOT ! » en très gros. « On va voir ce qui est resté. 15 questions.
    Ce n'est pas une note : c'est un jeu. » Et en petit : « Pas d'internet ? On lève les
    cartes de couleur : 1 = rouge, 2 = bleu, 3 = orange, 4 = vert. »
45. [CLAIRE] Titre « Vous avez franchi la case 1. » Quatre cartes de badges : Bâtisseur
    (ton programme a affiché quelque chose) · Chasseur de bug (tu as trouvé une erreur
    tout seul) · Persévérant (tu as galéré, et tu es resté dessus) · Grade Novice
    (toute la classe). Puis deux lignes : « Deux post-it avant de sortir : j'ai compris ___
    et je ne suis pas encore sûr de ___ » et « Le code officiel : je le publie maintenant,
    samedi je le redonne à tout le monde. »
46. [SOMBRE] Surtitre « SAMEDI PROCHAIN ». En très gros : « Votre jeu ne va plus seulement
    parler. Il va vous ÉCOUTER. » Et en orange : « À samedi, les Geeks ! »
```

---

## BLOC 4 — pour aller plus loin *(facultatif)*

```
Maintenant, améliore le diaporama sans changer un mot des textes :
1. Remplace chaque emoji par une illustration ou une photo libre de droits cohérente
   avec la palette. Pour les neuf portraits, n'invente aucun visage : utilise une
   silhouette, une illustration abstraite ou un symbole lié à ce que la personne a fait
   (un téléphone, une fusée, une goutte d'eau, un poste de radio…).
2. Ajoute une transition « morphose » douce entre les diapositives d'un même bloc.
3. Vérifie qu'aucun texte ne dépasse de son cadre et qu'aucune diapositive de contenu
   ne dépasse 25 mots.
4. Vérifie que chaque diapositive porte bien son horaire en bas à droite.
5. Laisse les notes de l'orateur intactes.
```

---

## Si vous préférez ne rien refaire

Le `.pptx` fourni est complet et testé. Dans ce cas, la seule chose à faire est de
**l'ouvrir une fois avant la séance** pour vérifier l'affichage des emoji et des couleurs
sur la machine de projection, en mode Présentateur — les notes de l'animateur s'affichent
alors sur votre écran, et les élèves ne voient que la diapositive.
