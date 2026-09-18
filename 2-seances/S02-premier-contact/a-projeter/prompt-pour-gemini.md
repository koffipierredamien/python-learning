# 🤖 Script pour Gemini — le diaporama de la séance 2

Le diaporama est déjà prêt : **[`seance-2-projection.pptx`](seance-2-projection.pptx)**, 24 diapositives,
avec les notes de l'animateur sur chacune.

Ce fichier-ci sert **si vous voulez le refaire en plus beau**, comme vous l'avez fait pour la séance 1 :
mêmes couleurs, mêmes règles, vraies images à la place des emoji.

> **Le plus rapide :** ouvrez `seance-2-projection.pptx` dans Google Slides et demandez à Gemini
> *« garde exactement le texte, la structure et les notes ; applique la même charte que ma présentation
> de la séance 1 ; remplace les emoji par de vraies images libres de droits »*.
> Vous gardez ainsi le minutage et les notes, qui sont le vrai travail.

Si vous préférez repartir de zéro, collez le BLOC 0, puis le BLOC 1, puis le BLOC 2.
**Jamais les deux blocs de contenu d'un coup** : au-delà d'une quinzaine de diapos par demande,
Gemini fusionne ou oublie des diapositives.

---

## BLOC 0 — le cadrage

```
Tu es directeur artistique et concepteur pédagogique. Tu produis un diaporama PROJETÉ
pendant un cours de programmation Python pour des enfants de 9 à 12 ans et des
adolescents de 12 à 18 ans, en français.

CONTEXTE
- Séance 2 du samedi 19 septembre 2026, de 12 h à 14 h.
- Le projet de l'année : construire le jeu XO (morpion) en 22 samedis.
- C'est la séance du PREMIER CONTACT AVEC LA MACHINE : les élèves écrivent et lancent
  leur premier programme. La séance 1 était entièrement théorique.
- L'animateur parle : les diapos ne contiennent JAMAIS son discours, seulement l'idée
  forte, en très gros. Le discours va dans les NOTES de l'orateur.

RÈGLES DE CONCEPTION, à respecter sans exception
1. Format 16:9.
2. Palette (aucune autre) :
   bleu nuit #12122A (fonds sombres) · nuit clair #20204A (cartes sur fond sombre) ·
   blanc cassé #F7F7FB (fonds clairs) · encre #14142B (texte sur fond clair) ·
   cyan #4FC3F7 / #13678F · orange #FFB74D / #A65D00 · violet #B06FD8 / #6B2D8F ·
   vert #2FB765 / #0C5C29 · rouge #FF6B6B / #B01B20 (uniquement pour les erreurs).
   Le cyan et l'orange sont les couleurs du X et du O du jeu.
3. Diapositives de TITRE, de SÉPARATION, de PROMESSE et de PAUSE sur fond bleu nuit ;
   diapositives de CONTENU sur fond blanc cassé.
4. Une seule famille sans serif. Titres 36 à 44 pt gras, sous-titres 20 à 24 pt,
   corps 14 à 18 pt. Le CODE toujours en police à chasse fixe (Consolas ou Courier New).
5. Motif récurrent : une petite grille de morpion 3x3 en carrés arrondis, discrète,
   dans un coin de chaque diapositive. C'est la signature visuelle de la formation.
6. Chaque diapositive porte son HORAIRE en petit, en bas à droite (ex. « 13 h 21 »).
7. Aucune diapositive ne dépasse 25 mots, titre compris. Si je te donne plus de texte,
   c'est qu'il va dans les notes de l'orateur.

Réponds simplement "prêt" et attends le contenu.
```

---

## BLOC 1 — les 13 premières diapositives

```
Crée les 13 premières diapositives, dans cet ordre exact.

1. TITRE (sombre) — « LE JEU XO » (le X en cyan, le O en orange),
   sous-titre « Séance 2 — Premier contact machine », « samedi 19 septembre 2026 · 12 h - 14 h »,
   phrase d'accroche « Aujourd'hui, on allume les machines. »
2. PRIÈRE (sombre) — horaire « 12 h - 12 h 15 ». Un seul mot : « Prière ».
   Sous-titre : « Comme chaque samedi, on commence par là. »
3. LE PROGRAMME (clair, 12 h 15) — titre « Trois choses, puis les machines. »
   Quatre cartes numérotées : 1 Vos exercices · 2 Un jeu (le quiz de samedi dernier) ·
   3 Comment on travaille · 4 LES MACHINES (carte mise en avant, en vert).
   Bandeau bas : « À 13 h 10, tout le monde est devant un clavier. »
4. LES EXERCICES (clair, 12 h 15) — titre « On ramasse. On ne corrige pas. »
   Trois cartes : Ce qui compte (que vous ayez essayé, ce n'est pas noté) ·
   Ceux qui n'ont rien fait (ce n'était pas obligatoire, vous n'êtes pas en retard) ·
   Ce qu'on en fait (je les lis ce soir).
5. KAHOOT (sombre, 12 h 25 - 12 h 45) — « KAHOOT ! » en très gros.
   « 15 questions sur samedi dernier. Ce n'est pas une note : c'est un jeu. »
6. LA RÈGLE DU JEU (clair, 12 h 25) — titre « Une carte, pas une main levée. »
   Quatre pavés de couleur : réponse 1 ROUGE, 2 BLEU, 3 ORANGE, 4 VERT.
   Bandeau bas : « Je compte 3, 2, 1 — et tout le monde lève sa carte EN MÊME TEMPS. »
7. SÉPARATION (sombre, 12 h 45) — grand numéro 3, « LA MÉTHODE DE TRAVAIL »,
   « Comment on va travailler pendant 20 samedis. »
8. LE BINÔME (clair, 12 h 45) — titre « Un pilote, un copilote. » Deux grandes cartes :
   LE PILOTE (il a le clavier, lui seul touche la machine) et LE COPILOTE (il lit la
   consigne et surveille les fautes, il ne prend jamais le clavier).
   Bandeau bas : « On échange toutes les 10 minutes. »
9. L'ENGAGEMENT (sombre, 12 h 47) — en très gros, entre guillemets :
   « Je ne prends pas le clavier de mon binôme. Je ne me moque pas. Je demande de l'aide
   à deux avant de la demander au professeur. »
10. LES TROIS PISTES (clair, 12 h 51) — trois cartes : PISTE BLEUE (le fichier est déjà
    écrit, avec des trous à remplir) · PISTE ROUGE (tu écris toi-même, avec le modèle) ·
    PISTE NOIRE (la même chose, plus un défi).
    Bandeau bas : « Les trois pistes arrivent au MÊME résultat. »
11. LA PROMESSE (sombre, 12 h 55) — « À la fin de chaque séance, je vous donne le code
    officiel. » Sous-titre : « Même si tu n'as pas fini. Même si tu étais absent. »
    Phrase finale en vert : « Dans cette formation, on ne peut pas prendre du retard. »
12. L'ÉVALUATION (clair, 12 h 58) — titre « Il n'y en a pas. Ni classement. »
    Trois cartes numérotées : Ça marche · Je sais l'expliquer · Je sais le refaire.
13. PAUSE (sombre, 13 h - 13 h 10) — « PAUSE », « 10 minutes. Retour à 13 h 10 ».
```

---

## BLOC 2 — les 11 dernières diapositives

```
Continue avec les 11 diapositives suivantes, même charte.

14. SÉPARATION (sombre, 13 h 10) — « ET MAINTENANT… » puis, énorme :
    « ON ALLUME LES MACHINES. »
15. THONNY (clair, 13 h 10) — titre « Thonny : trois repères, pas plus. »
    Trois cartes numérotées : la zone blanche en haut (on y écrit) · la zone grise en bas
    (l'ordinateur y répond) · le bouton vert ou F5 (c'est « vas-y »).
16. LES CARTES (clair, 13 h 13) — titre « On lève une carte. » Quatre pavés de couleur :
    VERT ça avance · ORANGE je suis bloqué, je continue à chercher · ROUGE problème de
    machine · BLEU j'ai fini, je veux le défi.
17. LA PREMIÈRE COMMANDE (clair, 13 h 15) — au centre, en très gros et en chasse fixe :
    print("Bonjour")
    Trois cartes en dessous : print = AFFICHE (jamais de papier) · les parenthèses se
    referment toujours · les guillemets vont par deux, comme des chaussures.
18. L'ORDRE DES LIGNES (clair, 13 h 18) — titre « De haut en bas. Ligne par ligne.
    Toujours. » À gauche trois lignes de code numérotées 1, 2, 3 ; à droite : « Il ne
    devine pas. Il ne saute pas de ligne. Il ne revient pas en arrière. »
19. L'ERREUR (sombre, 13 h 21) — « ET MAINTENANT, JE CASSE TOUT. » Puis, en chasse fixe :
    print("Bonjour)   ← il manque un guillemet.
    Un encadré rouge : SyntaxError. Et en très gros, en orange :
    « Le rouge n'est pas une punition. LE ROUGE EST UNE INFORMATION. »
20. LA MISSION (clair, 13 h 25) — titre « Votre mission : l'écran d'accueil du jeu. »
    À gauche, un faux écran de terminal sombre montrant :
    « BIENVENUE DANS LE JEU XO / Cree par : TON PRENOM / Prepare-toi a perdre ! »
    À droite, 5 étapes numérotées : ouvrir GEEKS puis mon_xo puis jeu.py · appuyer sur F5
    tout de suite, il marche déjà · remplacer chaque ____ · relancer après chaque
    changement · Ctrl + S pour sauver.
    Bandeau bas : « Pilote au clavier. Copilote sur la consigne. Échange à 13 h 35. »
21. LES ERREURS (clair, 13 h 27) — titre « Les trois erreurs de la journée. »
    Trois bandes : SyntaxError → compte tes guillemets · NameError → mets ton texte entre
    guillemets · Rien ne se passe → tu as écrit dans la zone grise du bas.
22. SAUVEGARDE (sombre, 13 h 42) — « ON SAUVEGARDE. » puis « Ctrl + S » en chasse fixe.
    Encadré vert : « Et voici le code officiel de la séance : il est déjà sur votre poste.
    Celui qui n'a pas fini l'a aussi. C'était ma promesse. »
23. CLÔTURE (clair, 13 h 45) — titre « Vous avez écrit votre premier programme. »
    Quatre badges : Bâtisseur (ton programme a affiché quelque chose) · Chasseur de bug
    (tu as réparé une erreur rouge) · Copilote (tu as aidé sans prendre le clavier) ·
    Curieux (tu as essayé quelque chose que personne n'avait demandé).
    Bandeau bas : « Tout le monde repart avec au moins un badge. »
24. SAMEDI PROCHAIN (sombre, 14 h) — « Votre jeu ne va plus seulement parler.
    Il va vous ÉCOUTER. » Puis « À samedi, les Geeks ! »
```

---

## Après la génération — les trois vérifications

1. **Le minutage en bas à droite** est-il sur toutes les diapositives, et juste ?
2. **Les notes de l'orateur** ont-elles survécu ? Ce sont elles qui portent le déroulé —
   si Gemini les a perdues, recopiez-les depuis `seance-2-projection.pptx`.
3. **La diapositive 19 (l'erreur)** est-elle restée choquante visuellement ? C'est le moment
   le plus important de la séance : il faut que le rouge se voie du fond de la salle.
