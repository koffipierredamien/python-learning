# Séance 1 — « Le Décollage »

> **Fiche de conduite détaillée.** Tout ce qui doit être dit, tout ce qui doit être fait.
> Les passages en **🗣️ guillemets** sont des scripts : ils peuvent être lus tels quels.
> **Vous êtes seul avec votre classe.** Les réflexes du prof seul sont rappelés au § 2 bis.
> Voir [la méthode pédagogique](../../1-methode/methode-pedagogique.md) pour les principes.

---

## 0. Carte d'identité de la séance

| | |
|---|---|
| **Numéro** | 1 / 22 — Phase 0 « Décollage » |
| **Date** | samedi 12 septembre 2026 · **12 h - 14 h** |
| **Organisation** | **Un enseignant par classe**, les deux classes en parallèle : Jeremiah Geeks (12–18) et Jerusalem Geeks (9–12) |
| **Classes** | Même déroulé des deux côtés, variantes signalées par 🧒 (9–12) et 🧑 (12–18) |
| **Notions** | Pourquoi et comment on code · du binaire à Python · l'algorithme · `print()` |
| **Brique ajoutée au projet** | **L'écran d'accueil du jeu XO** : le jeu s'annonce et affiche le nom de son créateur |
| **Livrable élève** | Un fichier `mon_xo/jeu.py` qui s'exécute et affiche un écran d'accueil |
| **Particularité** | Séance de lancement : prière, théorie fondatrice, test de positionnement et quiz Kahoot. **Le temps de code est volontairement court (12 min).** La séance 2 est la première séance de format normal. |

### Les 5 objectifs, par ordre de priorité

1. **Que chaque élève reparte en ayant fait tourner un programme qu'il a écrit lui-même.** *Non négociable — y compris pour l'élève qui n'a jamais touché un ordinateur.*
2. Que chaque élève comprenne **pourquoi** il est là, et ait envie de revenir samedi.
3. Que les enseignants connaissent le niveau réel de chaque élève.
4. Que chaque élève sache dire ce qu'est **un algorithme**, et comment l'ordinateur comprend ce qu'on lui écrit.
5. Que le vocabulaire du jour soit **vérifié**, pas seulement énoncé — c'est le rôle du Kahoot final.

> **L'objectif n° 1 prime sur tous les autres.** Si le temps manque, on raccourcit le Kahoot, puis la théorie, puis le test de positionnement. **Jamais le temps machine.**

---

## 1. Le programme de la séance

| Horaire | Séquence | Durée |
|---|---|---|
| **12 h - 12 h 15** | Prière et accueil | 15 min |
| **12 h 15 - 12 h 25** | L'effet WOW et les trois promesses | 10 min |
| **12 h 25 - 12 h 55** | La théorie : pourquoi et comment on code | 30 min |
| **12 h 55 - 13 h 05** | Pause | 10 min |
| **13 h 05 - 13 h 30** | Les missions de décollage (test de positionnement) | 25 min |
| **13 h 30 - 13 h 45** | Premier contact machine : mon premier programme | 15 min |
| **13 h 45 - 13 h 55** | Le Kahoot | 10 min |
| **13 h 55 - 14 h** | Clôture : badges, Mur de Mission, post-it | 5 min |

### Détail de la théorie (12 h 25 - 12 h 55)

| Horaire | Sujet |
|---|---|
| 12 h 25 - 12 h 29 | Pourquoi coder ? |
| 12 h 29 - 12 h 34 | Où se cache le code ? Les domaines d'application |
| 12 h 34 - 12 h 42 | Ceux qui ont fait des choses magnifiques avec du code |
| 12 h 42 - 12 h 49 | Comment l'ordinateur comprend : du binaire à l'éditeur |
| 12 h 49 - 12 h 55 | La notion d'algorithme |

### Ce qui a été retiré du programme initial, et où c'est parti

| Retiré de la séance 1 | Pourquoi | Devient quoi |
|---|---|---|
| Le bloc des 4 rituels (10 min) | Trop tôt et trop long : on installe un rituel **au moment où il sert** | Le signal de silence est posé en 1 min à 12 h 15 ; les cartes de signalisation et la règle des 3 avant moi à 13 h 30, juste avant la machine |
| La constitution des binômes pendant la pause (5 min) | Faire des binômes en 5 minutes chrono était le point le plus fragile de la séance | **Reporté à la séance 2**, composés à froid le soir même à partir du diagnostic. C'est mieux fait. En séance 1, chacun travaille avec son voisin de poste |
| Le contrat de binôme (2 min) | Sans binômes officiels, il n'a pas d'objet | Séance 2, avec l'engagement collectif à voix haute |
| La visite guidée de Thonny (8 min) | On peut découvrir l'outil en s'en servant | Fondue dans le premier contact machine, réduite à 3 repères |
| Le live coding en 4 étapes (12 min) | Trop long après 30 min de théorie | Condensé à 5 min. **L'erreur volontaire est conservée** : c'est le moment le plus important de la séance |
| Les 3 pistes Bleue / Rouge / Noire | Tout le monde fait la même chose aujourd'hui : compléter un fichier déjà prêt | **Démarrent à la séance 2** |
| La mise en commun et les 2 démonstrations (6 min) | Le Kahoot joue ce rôle, et mieux : il fait participer tout le monde | Le Kahoot |

---

## 2. Préparation

### J-7 — À faire impérativement

- [ ] **Coder le jeu XO terminé** ([`4-outils/jeu_xo_complet.py`](../../4-outils/jeu_xo_complet.py) est prêt : il suffit de le tester). C'est la démo du « WOW » : sans elle, la séance perd son moteur.
- [ ] Installer **Python + Thonny** sur toutes les machines, **version identique**, et lancer [`4-outils/verifier_un_poste.py`](../../4-outils/verifier_un_poste.py) sur **chaque** poste.
- [ ] Lancer [`4-outils/installer_dossier_geeks.py`](../../4-outils/installer_dossier_geeks.py) sur chaque poste : le dossier `GEEKS` doit apparaître sur le Bureau.
- [ ] Régler la **taille de police de Thonny à 18** minimum sur tous les postes et sur la machine de projection.
- [ ] **Ouvrir le quiz** [`kahoot/quiz-seance-1.pptx`](kahoot/quiz-seance-1.pptx) une fois et le faire défiler. Rien d'autre à préparer : il se joue avec les cartes de couleur. *(Si vous préférez la version en ligne, les fichiers d'import Kahoot sont dans le même dossier.)*
- [ ] **Aucune partie de la séance ne dépend d'internet.** Vérifiez quand même que le vidéoprojecteur affiche bien les deux diaporamas.
- [ ] Préparer la **clé USB** : `python 4-outils/preparer_cle_usb.py`.
- [ ] Vérifier le **vidéoprojecteur** avec le câble et la machine du jour.
- [ ] **Ouvrir le diaporama** [`presentation/seance-1-projection.pptx`](presentation/seance-1-projection.pptx) une fois sur la machine de projection, en **mode Présentateur** : les notes de l'animateur s'affichent sur votre écran, les élèves ne voient que la diapositive.

### J-1 — Impressions et matériel

| Quantité | Document | Fichier |
|---|---|---|
| 1 par binôme | Jeu de 4 **cartes de signalisation**, plastifiées — **elles serviront aussi de cartes de réponse au Kahoot** | `a-imprimer/01-cartes-signalisation.pdf` |
| 1 affiche A3 | **Règle des 3 avant moi** | `a-imprimer/02-affiche-3-avant-moi.pdf` |
| 1 affiche A3 | **Contrat de binôme** *(affiché aujourd'hui, expliqué en séance 2)* | `a-imprimer/03-affiche-contrat-binome.pdf` |
| 1 affiche A3 | **Dictionnaire des erreurs** | `a-imprimer/04-affiche-dictionnaire-erreurs.pdf` |
| 1 affiche A3 | **Mur de Mission** | `a-imprimer/05-mur-de-mission.pdf` |
| 1 par binôme | **Fiche mémo S1** | `a-imprimer/06-fiche-memo-eleve.pdf` |
| 6 exemplaires | Cartes-missions **station 1** | `a-imprimer/07-station1-cartes-missions.pdf` |
| 6 exemplaires | Feuilles d'énigmes **station 2** | `a-imprimer/08-station2-enigmes.pdf` |
| 1 par élève | Questionnaire **station 3** | `a-imprimer/09-station3-questionnaire.pdf` |
| 2 exemplaires | **Grille d'observation** *(pages 2-3 = corrigés)* | `a-imprimer/10-grille-observation.pdf` |
| 3 pages | **Étiquettes prénom** | `a-imprimer/11-etiquettes-prenoms.pdf` |
| 2 exemplaires | **Affiche « aider sans faire à la place »** *(côté enseignants)* | `a-imprimer/12-affiche-4-phrases-enseignant.pdf` |
| 1, agrafé | **MON SCRIPT d'animation** | `a-imprimer/00-MON-SCRIPT-animation.pdf` |
| — | Badges / autocollants, minuteur visible, **2 post-it par élève**, boîte à post-it | |

> Les quantités et les formats sont détaillés dans [`a-imprimer/quantites-et-formats.md`](a-imprimer/quantites-et-formats.md).
> Le document **13-cartes-pistes** n'est pas utile aujourd'hui : les 3 pistes démarrent en séance 2.

### Le jour même — 30 minutes avant

- [ ] Machines allumées, Thonny ouvert, `GEEKS/mon_xo/jeu.py` **déjà ouvert** sur chaque poste
- [ ] **Une machine de réserve allumée** en fond de salle
- [ ] Le jeu XO fini est **lancé et réduit** dans la barre des tâches (ne jamais chercher le fichier devant la classe)
- [ ] Le **diaporama est ouvert** en mode Présentateur, sur la diapositive 1
- [ ] Le **quiz** est ouvert dans une deuxième fenêtre, prêt à projeter
- [ ] Affiches au mur, Mur de Mission bien visible
- [ ] Un coup de fil à votre collègue de l'autre classe : tout est prêt des deux côtés ?

---

## 2 bis. Seul avec votre classe : les cinq réflexes

L'organisation a changé : **un enseignant par classe**, les deux classes en parallèle. Personne ne circule
pendant que vous parlez. Toute la méthode tient encore, mais elle repose désormais sur cinq réflexes.

| # | Le réflexe | Pourquoi |
|---|---|---|
| **1** | **J'alterne explicitement : « je parle » ou « je circule ».** Jamais les deux. Quand je parle, personne ne code — écrans éteints ou mains sur la table. Quand je circule, je ne m'adresse plus au groupe. | C'était le partage Capitaine / Mécanicien. Seul, on ne peut plus le faire en même temps : on le fait l'un après l'autre. |
| **2** | **Les cartes de signalisation sont mes yeux.** Je balaye la salle du regard toutes les 2 minutes, sans bouger. | Seul, je ne peux pas aller voir chaque poste. La carte vient à moi, pas l'inverse. |
| **3** | **Les élèves s'entraident d'abord.** Je relis la consigne → je demande à mon voisin → on regarde la fiche. Ensuite seulement, la carte orange. | Ce n'est plus un confort, c'est **la condition** pour qu'une classe seule tienne. |
| **4** | **Je nomme 2 Geek Mentors par séance.** Les premiers qui lèvent la carte bleue deviennent aide-enseignants pendant 10 minutes — sans jamais toucher le clavier des autres. | C'est ce qui remplace le deuxième adulte. |
| **5** | **Je ne m'assois jamais, et je fais un tour complet avant de répondre deux fois au même élève.** 60 secondes debout par poste, puis je repars. | Sinon un élève bavard capte tout le temps, et trois autres décrochent en silence. |

> **Le binôme fait le travail du deuxième enseignant.** C'est pour ça que le pair programming n'est pas
> optionnel dans ce dispositif : à partir de la séance 2, un élève sur deux est en train d'aider l'autre.

> ⚠️ **Conséquence directe :** la règle des **3 avant moi** devient structurelle. Elle reste affichée au mur
> (document 02) et projetée à 13 h 32, même si elle a été retirée de la fiche mémo de l'élève.

---

## 3. Le déroulé

---

### ⏱️ 12 h - 12 h 15 · Prière et accueil *(15 min)*

**Vous accueillez à la porte**, un élève à la fois : étiquette prénom, présence cochée.

> 🗣️ **Vous :** « Salut ! Comment tu t'appelles ? … Bienvenue chez les **Jerusalem Geeks** [ou Jeremiah Geeks]. Écris ton prénom en gros sur l'étiquette et colle-la sur toi. Ensuite, assieds-toi où tu veux — c'est la seule fois de l'année où tu choisis ta place ! »

Puis vous rassemblez la salle et vous conduisez le temps de prière.

> 🗣️ **Vous :** « Bienvenue à tous. On va commencer comme on commencera chaque samedi : par un temps de prière. »

*(Temps de prière — 10 à 12 minutes.)*

> 🗣️ *(pour faire le lien avec la séance, en une phrase)* : « On va apprendre à donner des ordres à des machines. Que ce qu'on construira ici serve, et serve bien. »

**Puis, immédiatement, le signal de silence** (1 min) — c'est le seul rituel dont on a besoin tout de suite :

> 🗣️ **Vous :** « Une seule règle d'organisation pour l'instant. Quand j'ai besoin de vous, j'ai un signal. *[signal]* Quand vous l'entendez : mains sur la table, yeux sur moi, plus un mot, en 3 secondes. On s'entraîne. Faites du bruit… allez, du **vrai** bruit ! … *[signal]* … Trois, deux, un. **Parfait.** »

> ⚠️ **Ne pas laisser les élèves toucher les machines** pendant toute la première heure. Écrans allumés mais non utilisés. Le dire simplement : *« Les ordinateurs, on n'y touche pas tout de suite. Promis, ça vient. »*

**Ce que vous observez et notez :** qui arrive avec un parent · qui n'ose pas entrer · qui se connaît déjà · qui se précipite sur la machine.

---

### ⏱️ 12 h 15 - 12 h 25 · L'effet WOW et les trois promesses *(10 min)*

#### a) Le WOW (4 min)

**On lance le jeu terminé, en silence, plein écran.** On laisse 5 secondes.

> 🗣️ **Vous :** « Il me faut un volontaire… Viens. Assieds-toi ici. Tu joues contre moi. »

On joue une partie complète, en direct, au vidéoprojecteur. **On la perd**, de préférence. Applaudissements.

> 🗣️ **Vous :** « Ce jeu, ce n'est pas moi qui vais le faire. **C'est vous.** Vous allez le construire, morceau par morceau, un samedi après l'autre. Et à la fin, vous repartirez avec — sur une clé, pour le montrer à vos parents, à vos amis, et pour les battre. »

#### b) La guilde et le Mur de Mission (3 min)

> 🗣️ **Vous :** « Bienvenue chez les **……………… Geeks**. Un geek, ce n'est pas un mot moqueur ici : c'est quelqu'un qui comprend comment marchent les machines, et qui sait leur donner des ordres. À partir d'aujourd'hui, vous êtes des **Novices**. Puis Apprentis Codeurs, Codeurs, Ingénieurs, Architectes — et les meilleurs finiront **Maîtres Geeks**. »

*(Montrer le Mur de Mission.)*

> 🗣️ **Vous :** « Voilà notre carte. 22 cases, 22 samedis. Chaque samedi, la classe avance d'**une** case. Attention : **la classe**, pas un élève. On avance **ensemble**. Aujourd'hui, on franchit la case 1 : *le jeu dit bonjour*. »

#### c) Les trois promesses et les trois règles (3 min)

> 🗣️ **Vous :** « Je vous fais trois promesses.
> **Un :** chaque samedi, en repartant, votre jeu marchera mieux qu'en arrivant. **Chaque samedi. Tous.**
> **Deux :** ici, il n'y a **pas de notes**. Jamais. Personne ne sera comparé à personne.
> **Trois :** si vous êtes absents un samedi, vous ne serez **pas** en retard. J'ai un système pour ça, je vous le montrerai.
>
> En échange, je vous demande trois choses.
> **Un :** on ne se moque **jamais** de quelqu'un qui n'a pas compris ou qui va moins vite. Jamais. C'est la seule règle pour laquelle je me fâcherai.
> **Deux :** quand quelque chose ne marche pas, on ne dit pas *"je suis nul"*. On dit *"je n'ai pas encore trouvé"*.
> **Trois :** on essaie. Même quand on n'est pas sûr. Surtout quand on n'est pas sûr. »

---

### ⏱️ 12 h 25 - 12 h 55 · La théorie : pourquoi et comment on code *(30 min)*

> ⚠️ **Trente minutes sans machine, c'est long.** Cette partie ne doit pas être un cours magistral :
> chaque sujet contient une question posée à la classe ou une activité debout. **On ne parle jamais plus
> de 3 minutes d'affilée sans faire réagir la salle.** Tout s'écrit au tableau en même temps.
>
> 🧒 **Jerusalem (9–12) :** beaucoup de questions à main levée, les portraits racontés comme des histoires.
> 🧑 **Jeremiah (12–18) :** on peut aller plus vite sur les domaines et plus loin sur le binaire.

#### a) 12 h 25 - 12 h 29 · Pourquoi coder ? *(4 min)*

> 🗣️ **Vous :** « Première question. **Ce matin, avant d'arriver ici, combien d'ordres avez-vous donnés à une machine ?** … Réfléchissez. Vous avez allumé un téléphone ? Envoyé un message ? Mis de la musique ? Retiré de l'argent ? Regardé l'heure ? … Chacun de ces gestes, une machine l'a exécuté parce que **quelqu'un, un jour, lui a écrit quoi faire.** »

> 🗣️ **Vous :** « Aujourd'hui, vous **utilisez** ce que d'autres ont écrit. Vous êtes des consommateurs.
> Coder, c'est passer de l'autre côté : **devenir celui qui écrit.** Celui qui décide ce que la machine fait.
> Et ça sert à trois choses : **fabriquer** des outils qui n'existent pas encore, **résoudre** des problèmes autour de vous, et **comprendre** le monde dans lequel vous vivez — parce qu'aujourd'hui, tout ce qui vous entoure obéit à du code. »

**Question à la classe :** *« Qu'est-ce que vous aimeriez que la machine fasse, et qu'elle ne fait pas encore ? »*
→ On note 2 ou 3 réponses au tableau. **On y reviendra à la dernière séance.**

#### b) 12 h 29 - 12 h 34 · Où se cache le code ? *(5 min)*

**Jeu : « il y a du code là-dedans ? »** — Vous nommez un métier ou un objet, les élèves répondent **oui / non** à main levée, puis vous expliquez en une phrase.

| Ce qu'on nomme | La phrase d'explication |
|---|---|
| 🎮 **Les jeux vidéo** | « Chaque déplacement, chaque point, chaque adversaire : du code. » |
| 🏥 **La santé** | « Les machines qui regardent à l'intérieur du corps, les dossiers des patients, les alarmes qui sauvent une vie la nuit. » |
| 🌾 **L'agriculture** | « Savoir quand il va pleuvoir, combien d'engrais mettre, repérer une maladie sur une feuille avec une photo. » |
| 🎵 **La musique** | « Presque toute la musique que vous écoutez est enregistrée, mélangée et parfois créée avec du code. » |
| 🚗 **Les transports** | « Le GPS qui choisit ta route, les feux de circulation, les avions. » |
| 💸 **L'argent** | « Le mobile money, les distributeurs, les paiements par téléphone. » |
| 🎬 **Le cinéma et le dessin animé** | « Les images de synthèse, les décors, les personnages. » |
| 🚀 **L'espace** | « Il n'y a personne pour tourner le volant d'une fusée. C'est du code. » |
| ⚽ **Le sport** | « Les statistiques, la vidéo, les capteurs sur les joueurs. » |

> 🗣️ *(conclusion)* : « Alors, dans quel domaine n'y a-t-il **pas** de code ? … **Il n'y en a aucun.**
> Ce que vous allez apprendre ici ne sert pas à "faire de l'informatique". Ça sert **dans le métier que vous choisirez**, quel qu'il soit. »

#### c) 12 h 34 - 12 h 42 · Ceux qui ont fait des choses magnifiques *(8 min)*

> **C'est le cœur émotionnel de la séance.** Le but n'est pas de réciter des biographies : c'est que
> chaque élève se dise *« si lui l'a fait à mon âge, moi aussi je peux »*. Racontez, ne lisez pas.

**1. Deux noms qu'ils connaissent déjà — et ce qu'ils ne savent pas *(2 min)***

| Qui | L'histoire à raconter |
|---|---|
| **Mark Zuckerberg** | « Vous connaissez Facebook, Instagram, WhatsApp ? Un seul homme a lancé tout ça. Il a écrit la première version de Facebook **dans sa chambre d'étudiant**, à 19 ans. Mais voilà ce que personne ne vous dit : **il a commencé à coder vers 12 ans.** Son premier programme servait à envoyer des messages entre les ordinateurs de la maison de ses parents. C'était minuscule. Il l'a fait quand même. » |
| **Elon Musk** | « Les fusées qui reviennent se poser toutes seules, les voitures électriques : c'est son entreprise. Et savez-vous ce qu'il faisait **à 12 ans** ? Il a codé un petit jeu vidéo, il s'appelait *Blastar*, et **il l'a vendu à un magazine d'informatique.** Douze ans. Vous avez presque son âge. » |

**2. Trois jeunes qui n'ont pas attendu d'être grands *(4 min — le bloc le plus important)***

| Qui | L'histoire à raconter |
|---|---|
| **Thomas Suarez**<br>🇺🇸 · avait **12 ans** | « À 12 ans, il fabriquait déjà des applications pour téléphone dans sa chambre. Il en a fait un petit jeu, puis un autre. Et un jour, on l'a invité à monter sur une grande scène pour expliquer à des adultes comment il faisait. **Sa vidéo a été vue des millions de fois.** À 12 ans. » |
| **Nick D'Aloisio**<br>🇬🇧 · avait **15 ans** | « Il en avait assez de lire de longs articles. Alors, à 15 ans, il a codé une application qui **résume automatiquement** les articles d'actualité en quelques lignes. Deux ans plus tard, à 17 ans, **une très grande entreprise a racheté son application** pour une somme énorme. Il était encore au lycée. » |
| **Gitanjali Rao**<br>🇺🇸 · avait **11 puis 15 ans** | « Elle a entendu parler d'une ville où l'eau du robinet était empoisonnée au plomb. À 11 ans, elle a fabriqué un appareil qui **détecte le plomb dans l'eau**. Ensuite elle a créé une application qui repère les messages méchants sur internet avant qu'ils fassent mal. À 15 ans, un grand magazine l'a nommée **« enfant de l'année »**. Elle a utilisé le code pour **régler de vrais problèmes**. » |

**3. Deux histoires proches de nous *(2 min)***

| Qui | L'histoire à raconter |
|---|---|
| **Charlette N'Guessan**<br>🇨🇮 Côte d'Ivoire | « Elle est ivoirienne. Avec son équipe, elle a créé un logiciel qui **reconnaît le visage d'une personne** pour vérifier son identité à distance — pour que les banques africaines ne se fassent plus voler des identités. En 2020, elle a gagné un grand prix africain d'ingénierie : **la première femme à le remporter.** » |
| **Kelvin Doe**<br>🇸🇱 Sierra Leone · avait **13 ans** | « Chez lui, il n'y avait pas d'électricité tous les jours. À 13 ans, avec des morceaux ramassés dans les poubelles, il a fabriqué une batterie pour éclairer sa maison, puis **son propre émetteur radio**, pour faire une station de radio dans son quartier. Une grande université américaine l'a fait venir chez elle pour qu'il montre comment il faisait. » |

> 🗣️ *(la conclusion — c'est LE message du bloc, à dire lentement)* :
> « Regardez-les bien. **Thomas avait 12 ans. Nick avait 15 ans. Gitanjali avait 11 ans. Kelvin avait 13 ans.**
> Aucun d'eux n'était un génie. Aucun n'avait de matériel extraordinaire — Kelvin travaillait avec des déchets.
> **Aucun d'eux n'a commencé en sachant coder.** Ils ont tous commencé exactement là où vous êtes assis
> aujourd'hui. La seule différence, c'est qu'ils ont commencé. »

> 🗣️ **Et la transition vers Python :** « Et tout ça, ça s'écrit dans un langage. Le nôtre s'appelle **Python**.
> Il a été créé par **Guido van Rossum**, qui voulait un langage simple, lisible, qu'un débutant puisse comprendre.
> C'est exactement pour ça qu'on l'a choisi pour vous. »

> 💡 **Ajoutez un portrait que vous connaissez personnellement** — quelqu'un de votre ville, de votre église,
> de votre famille, qui vit du code. Un exemple qu'on peut croiser dans la rue vaut mieux que tous les milliardaires.

> ⚠️ **Avant de citer un chiffre précis** (un âge, un montant, une date), vérifiez-le : les enfants retiennent
> les chiffres, et un élève curieux ira lire. Si vous n'êtes pas sûr, dites « il était encore adolescent » plutôt
> qu'un âge exact.

#### d) 12 h 42 - 12 h 49 · Comment l'ordinateur comprend : du binaire à l'éditeur *(7 min)*

**Activité debout (3 min).** Vous faites lever **8 élèves** en ligne face à la classe.

> 🗣️ **Vous :** « Vous êtes l'intérieur d'un ordinateur. Chacun de vous n'a le droit d'être que dans deux états : **debout = 1**, **assis = 0**. C'est tout. Pas de "peut-être", pas de "un peu". L'ordinateur ne sait faire que ça : du courant qui passe, ou qui ne passe pas.
> Maintenant, on va écrire une lettre. La lettre **A**, pour une machine, c'est : `01000001`. Allez : assis, debout, assis, assis, assis, assis, assis, debout. … **Voilà. Vous êtes la lettre A.** »

> 🗣️ **Vous :** « Vous imaginez écrire tout un jeu comme ça ? Avec des milliers de 0 et de 1 ? … Personne ne veut faire ça. **Alors on a inventé des langages** pour parler à la machine avec des mots. Python est l'un d'eux — et c'est l'un des plus proches de l'anglais courant. »

**Le tableau (4 min).** Vous dessinez la chaîne, de gauche à droite, en parlant :

```
   MOI              PYTHON            L'INTERPRÈTE          0 et 1         LA MACHINE
   j'écris   →   print("Bonjour")  →   il traduit    →   01110000...  →   elle obéit
  dans THONNY      (des mots !)        (le traducteur)                    (elle affiche)
```

> 🗣️ **Vous :** « Trois mots à retenir.
> **Python**, c'est la **langue** dans laquelle j'écris mes ordres — avec des mots, pas des chiffres.
> **L'interprète**, c'est le **traducteur** : il transforme mes mots en 0 et en 1. Il est déjà installé, vous ne le verrez jamais, mais il travaille à chaque fois.
> **Thonny**, c'est l'**éditeur** : c'est ma feuille, avec un bouton "vas-y". C'est le seul des trois que vous allez toucher.
>
> Et **retenez surtout ceci** : l'ordinateur, dans tout ça, **ne réfléchit jamais**. Il ne devine pas ce que vous voulez dire. **Il n'est pas intelligent : il est obéissant.** S'il fait une bêtise, ce n'est pas lui qui s'est trompé. »

#### e) 12 h 49 - 12 h 55 · La notion d'algorithme *(6 min)*

**Activité : le robot humain (4 min).** Un élève volontaire se place au fond de la salle.

> 🗣️ **Vous :** « Lui, c'est un robot. Il ne comprend que trois ordres : **AVANCE**, **TOURNE À GAUCHE**, **TOURNE À DROITE**. Il n'a pas d'imagination : il fait **exactement** ce qu'on lui dit, ni plus, ni moins. Votre mission, tous ensemble : l'amener au tableau, et lui faire écrire un X. »

La classe dicte les ordres. **Le robot obéit à la lettre — donc il se cogne, il s'arrête trop tôt, il tourne dans le vide.** C'est exactement l'effet recherché : on rit, et on comprend.

> 🗣️ **Vous :** « Vous venez de vivre ce que vit un programmeur toute la journée. Ce que vous avez écrit — cette suite d'ordres précis, dans le bon ordre — **ça s'appelle un algorithme.** »

**La définition, écrite au tableau et recopiée par les élèves :**

> **Un algorithme, c'est une suite d'ordres précis, donnés dans le bon ordre, pour arriver à un résultat.**

> 🗣️ **Vous :** « Une recette de cuisine est un algorithme. Un itinéraire est un algorithme. Les règles du morpion sont un algorithme — et c'est précisément celui-là que vous allez apprendre à écrire pendant 22 samedis.
> **Attention :** l'algorithme, ce n'est pas encore du code. C'est la **réflexion** avant le code. On peut l'écrire en français, sur du papier, sans ordinateur. **C'est la partie la plus difficile du métier — et c'est celle que vous allez travailler dans un instant.** »

> 🗣️ **Vous :** « Pause de dix minutes. Levez-vous, sortez, bougez — et revenez à l'heure. »

---

### ⏱️ 12 h 55 - 13 h 05 · Pause *(10 min)*

Pause **réelle** : les élèves sortent, se lèvent, boivent. Non négociable, surtout après 30 minutes de théorie.

Vous en profitez pour installer les 3 stations du test et vérifier que le quiz est prêt.

---

### ⏱️ 13 h 05 - 13 h 30 · Les missions de décollage *(25 min — 3 stations)*

> ⚠️ **Le mot « test » n'est jamais prononcé devant les élèves.** On dit **« les missions de décollage »**.

> 🗣️ **Vous :** « Avant de décoller, tous les astronautes passent des missions de préparation. Trois missions. **Ce n'est pas noté**, il n'y a pas de bonne ou de mauvaise équipe — ça sert **à nous**, pour bien vous accompagner. Vous êtes trois groupes. Quand j'appelle, vous tournez. »

| Station | Durée | Contenu | Tenue par |
|---|---|---|---|
| **1 · Pilotage** (postes) | 8 min | Les 6 manœuvres machine ([A1 §2](../../1-methode/annexes/A1-diagnostic-et-passeport.md)) | **Vous**, vous cotez /6 |
| **2 · Logique** (tables) | 8 min | Les 4 énigmes papier — **dont le robot et le morpion, qu'on vient de voir** | En autonomie |
| **3 · Identité** (fond) | 8 min | « Ma fiche de Geek » | En autonomie |

> 💡 **Le lien avec la théorie est explicite, dites-le :** *« L'énigme du robot, c'est exactement ce qu'on a fait tout à l'heure. Et la dernière — expliquer le morpion à un extraterrestre — c'est votre premier algorithme. Gardez bien cette feuille : on la relira à la séance 10, quand votre programme saura reconnaître le gagnant. »*

**Vous remplissez la grille d'observation depuis la station 1**, et surtout la colonne décisive : *abandonne / demande / persévère / aide les autres*. Les feuilles des stations 2 et 3 se corrigent le soir, pas pendant la séance.

> 🗣️ *(à la fin)* : « Missions terminées. **Personne n'a raté quoi que ce soit : tout le monde décolle.** Et maintenant… on allume les machines. »

---

### ⏱️ 13 h 30 - 13 h 45 · Premier contact machine *(15 min)*

#### a) Les cartes de signalisation et la règle des 3 avant moi (3 min)

Un jeu de 4 cartes est déjà posé sur chaque poste.

> 🗣️ **Vous :** « À partir de maintenant, dans cette salle, on ne lève **pas** la main. On lève une carte.
> 🟢 **Vert** : ça avance. 🟠 **Orange** : on est bloqués, on cherche quand même. 🔴 **Rouge** : rien ne marche, au secours. 🔵 **Bleu** : on a fini, on peut aider.
> Vous la posez sur l'écran, bien visible, et vous continuez à travailler. Nous, on voit toute la salle d'un coup d'œil. **Une carte orange est servie en moins de 5 minutes. Une carte rouge, tout de suite.**
>
> Et avant de lever l'orange, trois choses *(montrer l'affiche)* : **je relis** la consigne et le message rouge **à voix haute** · **je demande à mon voisin** · **on regarde la fiche mémo**. Ensuite seulement, la carte. »

#### b) Le live coding condensé, avec l'erreur volontaire (5 min)

Vous tapez au vidéoprojecteur, très lentement, en verbalisant. **Trois repères Thonny suffisent :** la zone du haut (ma feuille), la zone du bas (sa bouche), le bouton vert ▶ / `F5` (vas-y).

```python
print("Bonjour")
```

> 🗣️ **Vous :** « `p-r-i-n-t`, ça veut dire **affiche**. Une parenthèse : on l'ouvre, on la fermera **toujours**. Un guillemet, mon texte, un guillemet. On referme.
> **Avant que j'appuie : qu'est-ce qui va se passer ? À trois. Un, deux, trois !** »

*(Exécuter.)* « Voilà. Vous venez de voir un ordinateur **obéir**. C'est tout le métier. »

**🔥 Puis l'erreur volontaire — le moment le plus important de la séance.** Vous effacez le guillemet de fin :

```python
print("Bonjour)
```

*(Exécuter. Du rouge apparaît.)*

> 🗣️ *(avec un grand sourire)* : « **Ah ! Du rouge !** … Alors, qui a peur ? »
>
> *(Laisser réagir, puis très calmement)* « Moi je code depuis des années, et j'ai du rouge **tous les jours**. Le rouge, ce n'est pas une punition. Ce n'est pas une mauvaise note. **C'est l'ordinateur qui vous explique ce qu'il n'a pas compris.** Il essaie de vous aider — mais il le dit en anglais. Alors on va apprendre à le lire. Ensemble.
> Il a écrit `SyntaxError`. Quelqu'un devine ? … *Syntax*, c'est la grammaire. *Error*, l'erreur. Il nous dit : **"je ne comprends pas ta phrase"**. Et regardez : il montre même l'endroit avec une petite flèche. »
>
> *(Réparer, relancer, ça marche.)* « Réparé en quatre secondes. Retenez ça : **dans cette salle, le rouge n'est pas grave. Le rouge est une information.** »

Vous écrivez `SyntaxError` sur l'affiche du **Dictionnaire des erreurs** et nomme le **Gardien des erreurs** de la séance.

#### c) Chacun à son poste (7 min)

Le fichier `GEEKS/mon_xo/jeu.py` est **déjà ouvert** sur chaque écran : c'est un texte à trous, il fonctionne dès la première exécution.

> 🗣️ **Vous :** « À vos postes, avec votre voisin. Le fichier est déjà ouvert. **Premier geste : appuyez sur F5, tout de suite, avant d'avoir rien écrit.** … Vous voyez ? Ça marche déjà.
> Maintenant, vous remplacez chaque `____` par ce qu'on vous demande : le titre du jeu, **votre prénom**, votre âge, et une phrase à vous. Vous relancez après **chaque** changement. Cartes sorties. C'est parti ! »

**Votre position :** vous ne restez plus devant — **vous circulez**, en commençant par les élèves repérés en difficulté à la station 1. Le vidéoprojecteur affiche la consigne, il parle à votre place.

**Les 4 phrases autorisées pour aider** *(ne jamais prendre le clavier)* :
1. « Lis-moi ton message d'erreur à voix haute. »
2. « Montre-moi la ligne. Qu'est-ce que tu voulais qu'elle fasse ? »
3. « Qu'est-ce qui se passerait si on mettait ça ici ? Essaie. »
4. « Explique-moi cette ligne comme si j'étais ton petit frère. »

**Les erreurs attendues — et la réponse, en une phrase :**

| Erreur | Ce qu'on voit | Ce qu'on dit |
|---|---|---|
| Guillemet oublié | `SyntaxError` | « Compte tes guillemets. Il en faut deux, comme une paire de chaussures. » |
| Parenthèse oubliée | `SyntaxError` | « Tout ce qui s'ouvre doit se fermer. » |
| `Print` avec majuscule | `NameError` | « L'ordinateur est très à cheval sur les majuscules. `print`, tout en minuscules. » |
| Ne trouve pas `"` ou `(` | — | Montrer la touche du doigt. **Ne pas taper à sa place.** |
| A tapé dans la zone du bas | Rien n'est enregistré | « Ça, c'est sa bouche. Ta feuille, c'est en haut. » |
| Fichier non enregistré | Thonny le propose au lancement | « Tu enregistres d'abord, tu lances ensuite. Toujours. » |

> **Objectif absolu de ces 7 minutes : que 100 % des écrans aient affiché quelque chose écrit par l'élève.**
> Vous comptez les écrans à **13 h 42**. S'il reste un poste où rien n'est jamais sorti, **c'est la priorité n° 1 des deux enseignants.**

> 🗣️ *(à 13 h 44)* : « Tout le monde : `Fichier`, `Enregistrer`. Pouce levé quand c'est fait. »

Vous passez avec la clé et vous sauvegardez le travail de chaque poste.

---

### ⏱️ 13 h 45 - 13 h 55 · Le Kahoot *(10 min)*

> 🗣️ **Vous :** « Dernière épreuve du décollage : on va voir ce qui est resté. **Ce n'est pas une note**, c'est un jeu. Et il y a des questions sur tout ce qu'on a fait aujourd'hui — la théorie **et** la machine. »

- **Le quiz est un diaporama** : [`kahoot/quiz-seance-1.pptx`](kahoot/quiz-seance-1.pptx). Une diapositive par question, puis une diapositive de réponse avec l'explication. 15 questions, 20 secondes chacune.
- Les 4 réponses portent **les couleurs des cartes de signalisation** : 🔴 = 1 · 🔵 = 2 · 🟠 = 3 · 🟢 = 4. Les élèves répondent **en levant leur carte**, tous en même temps, au signal « 3, 2, 1 ».
- Le détail, les bonnes réponses et l'explication à dire sont aussi dans **[`kahoot/questions-et-reponses.md`](kahoot/questions-et-reponses.md)**.
- **En retard ?** Gardez les **10 premières** : elles couvrent l'essentiel.
- Après chaque question, **vous expliquez la réponse en une phrase**. C'est là que le Kahoot devient de l'enseignement et plus seulement un jeu.
- On célèbre le podium, **mais on insiste** :

> 🗣️ **Vous :** « Et ceux qui n'ont pas gagné : vous avez appris exactement les mêmes choses. Le podium, c'est pour rire. »

> ✅ **Le quiz ne dépend plus d'internet du tout** : c'est un diaporama et des cartes en carton. Si vous préférez la version en ligne, les fichiers d'import Kahoot restent dans le dossier `kahoot/`.

---

### ⏱️ 13 h 55 - 14 h · Clôture *(5 min)*

#### a) Badges et grade (2 min)

> 🗣️ **Vous :** « Premiers badges des ……………… Geeks ! »

- 🧱 **`Bâtisseur`** → **à tous ceux dont le programme a affiché quelque chose. Viser 100 %.**
- 🐞 `Chasseur de bug` → ceux qui ont trouvé une erreur seuls
- 💪 `Persévérant` → **en priorité ceux qui ont galéré et sont restés dessus. Le dire fort.**
- ❓ `Question en or` → celui qui a posé la question que toute la classe se posait
- 🔤 `Traducteur d'erreur` → le Gardien des erreurs du jour
- 🤍 **Grade Novice** → toute la classe

#### b) Le Mur de Mission et le Filet (1 min 30)

Désignez un élève — de préférence **le plus discret de la séance** — pour colorier la case 1.

> 🗣️ **Vous :** « *Le jeu dit bonjour.* Une case sur 22. Applaudissez-vous. »

*(Brancher la clé et copier `jeu.py` dans `xo_officiel/`, devant tout le monde.)*

> 🗣️ **Vous :** « Vous vous souvenez de ma troisième promesse ? Ce fichier, c'est le **code officiel**. Samedi prochain, **je le redonne à tout le monde**. Donc si vous êtes malade, vous ne serez **pas** en retard. Et si vous cassez votre code en essayant un truc, **ce n'est pas grave du tout**. Alors à partir d'aujourd'hui : **essayez des choses.** »

#### c) Les deux post-it et la sortie (1 min 30)

> 🗣️ **Vous :** « Prenez vos deux post-it. Sur le premier : votre prénom et *aujourd'hui j'ai compris ___*. Sur le deuxième : votre prénom et *je ne suis pas encore sûr de ___*. Le deuxième est **plus important** que le premier : c'est lui qui nous dit par quoi commencer samedi. Écrivez la vérité — personne d'autre que nous deux ne les lira. Déposez-les dans la boîte en sortant.
>
> Défi maison, **totalement facultatif** : expliquez à quelqu'un chez vous ce qu'est un algorithme. Et si vous n'avez pas d'ordinateur à la maison, **aucun problème : vous ne serez jamais en retard.**
>
> Samedi prochain : le jeu va vous **demander votre nom**. À samedi, les Geeks ! »

Éteindre les machines, ranger les chaises. **Vous à la porte** pour saluer chacun et récupérer les post-it.

---

## 4. Après la séance — 15 minutes, puis 10 minutes à deux

- [ ] **Saisir le diagnostic** dans le classeur de suivi, onglet `02_Diagnostic`
- [ ] **Composer les binômes de la séance 2**, à froid : prénoms sur papiers, tri par profil, paquet coupé en deux, 1ᵉʳ de A avec 1ᵉʳ de B → écart d'un niveau, **jamais un P0 avec un P3**
- [ ] Remplir `03_Presence` et `04_Suivi-seances`
- [ ] **Lire tous les post-it** : si une même difficulté revient chez plus de 30 % du groupe, **elle ouvre la séance 2**
- [ ] **Noter les 2 ou 3 questions du quiz les plus ratées** : elles se reprennent en 2 minutes au début de la séance 2
- [ ] Établir la **liste des 10 minutes** pour la séance 2
- [ ] Envoyer le message aux familles
- [ ] Répondre aux **3 questions de la revue** (onglet `10_Journal-enseignants`)
- [ ] **Appeler votre collègue de l'autre classe** : 10 minutes. Ce qui a marché, ce qui a raté, ce qu'on change samedi. C'est le seul moment où les deux classes se parlent — ne le sautez pas.

---

## 5. Plans de secours

| Problème | Quoi faire |
|---|---|
| **Pas d'internet** | **Aucun impact** : rien dans la séance n'en dépend, quiz compris. |

| **Le vidéoprojecteur ne marche pas** | Le WOW se fait en petits groupes autour de la machine de démonstration (3 min par groupe). La théorie se fait au tableau — elle est de toute façon conçue pour le tableau. |
| **Panne de courant / machines HS** | Toute la première heure (prière, WOW raconté, théorie) fonctionne telle quelle. Le premier contact machine devient **« le programme sur papier »** : chaque binôme écrit son écran d'accueil au feutre sur une A3, et un camarade joue l'ordinateur en le lisant **littéralement**. |
| **Un enseignant absent** | Les deux classes **fusionnent** dans une seule salle, avec l'enseignant présent. On garde prière, WOW, théorie et clôture ; on supprime les missions de décollage (reportées) et on réduit le temps machine à une démonstration collective. Prévenir les familles de l'autre classe. |
| **On a 15 minutes de retard** | Supprimer, dans cet ordre : 1) le Kahoot passe à 8 questions 2) les portraits passent de 5 à 3 3) la station 3 du test (questionnaire à remplir en séance 2). **Ne jamais supprimer le temps machine, ni la clôture avec les badges.** |
| **Un élève arrive pendant la théorie** | Vous vous interrompez 30 secondes : étiquette prénom, une phrase d'accueil, une place. Le résumé et les missions de décollage attendront la pause — ne coupez pas la théorie pour lui. |

---

## 6. Le quiz : comment on le joue

**Il ne coûte rien à préparer et il ne dépend de rien.** Les élèves ont déjà les 4 cartes de couleur sur leur poste : elles deviennent les cartes de réponse, et les couleurs du diaporama sont les mêmes.

| Réponse | Couleur Kahoot | Carte à lever |
|---|---|---|
| 1 | 🔴 rouge | 🔴 **Rouge** |
| 2 | 🔵 bleu | 🔵 **Bleu** |
| 3 | 🟡 jaune | 🟠 **Orange** |
| 4 | 🟢 vert | 🟢 **Vert** |

**Déroulé :** vous projetez la diapositive de la question, vous lisez les 4 réponses à voix haute, vous comptez « 3, 2, 1 », **et tout le monde lève sa carte en même temps**. Vous comptez à vue les bonnes réponses — inutile de tenir un score exact — puis vous affichez la diapositive de réponse et vous donnez l'explication.

> **C'est meilleur que le Kahoot en ligne pour une classe seule :** pas de comptes à créer, pas d'appareils à distribuer, tout le monde répond en même temps, personne ne recopie son voisin — et vous voyez d'un seul regard quelle notion n'est pas passée.

---

## 7. Les six pièges de cette séance

| Piège | Conséquence | Parade |
|---|---|---|
| **Faire de la théorie un cours magistral** | Trente minutes assis = classe perdue avant la machine | Chaque sous-partie a **une question ou une activité debout**. On ne parle jamais 3 minutes d'affilée |
| **Laisser toucher les machines avant 13 h 30** | Plus personne n'écoute pendant la théorie | Règle annoncée d'emblée, avec humour, et rappelée |
| **Déborder sur la théorie** | On mange le temps machine, et l'objectif n° 1 tombe | **Minuteur visible.** À 12 h 55 on s'arrête, même au milieu d'un portrait |
| **Présenter le test comme un test** | Angoisse, résultats faussés, mauvais départ | On dit « missions de décollage », toujours |
| **Prendre le clavier d'un élève** | Il apprend qu'il n'y arrive pas seul. Le geste le plus destructeur du métier | Les 4 phrases autorisées, et rien d'autre |
| **Laisser le Kahoot manger la clôture** | On finit sans badges : le moteur de motivation est cassé dès le premier samedi | Le Kahoot **s'arrête à 13 h 55**, question en cours ou pas |

---

## 8. Supports de la séance

### Pour les enseignants

| Support | Fichier |
|---|---|
| 🎤 **Mon script d'animation** (à imprimer, agrafé) | [`a-imprimer/00-MON-SCRIPT-animation.pdf`](a-imprimer/00-MON-SCRIPT-animation.pdf) |
| 📺 **Le diaporama à projeter** — 46 diapos, notes de l'animateur incluses | [`presentation/seance-1-projection.pptx`](presentation/seance-1-projection.pptx) |
| 🤖 Refaire le diaporama avec Gemini | [`presentation/prompt-pour-gemini.md`](presentation/prompt-pour-gemini.md) |
| 🎯 **Le quiz à projeter** : 32 diapos, une par question puis la réponse | [`kahoot/quiz-seance-1.pptx`](kahoot/quiz-seance-1.pptx) |
| 📝 Les 15 questions, réponses et explications | [`kahoot/questions-et-reponses.md`](kahoot/questions-et-reponses.md) |
| 📥 Import Kahoot (si version en ligne) : le modèle officiel déjà rempli | [`kahoot/import-kahoot.xlsx`](kahoot/import-kahoot.xlsx) · [`kahoot/import-kahoot.pdf`](kahoot/import-kahoot.pdf) |
| 📨 **Le déroulé à envoyer au responsable** (Word, modifiable) | [`a-envoyer/deroule-seance-1.docx`](a-envoyer/deroule-seance-1.docx) |
| 🖨️ Tous les documents à imprimer | [`a-imprimer/`](a-imprimer/) — quantités : [`quantites-et-formats.md`](a-imprimer/quantites-et-formats.md) |
| 📊 Classeur de suivi | [`3-suivi/classeur-de-suivi.xlsx`](../../3-suivi/classeur-de-suivi.xlsx) |
| 🎮 Le jeu fini, pour le WOW | [`4-outils/jeu_xo_complet.py`](../../4-outils/jeu_xo_complet.py) |
| ⌨️ L'anti-sèche du live coding | [`code/live_coding_antiseche.py`](code/live_coding_antiseche.py) |
| ✅ Vérifier un poste avant la séance | [`4-outils/verifier_un_poste.py`](../../4-outils/verifier_un_poste.py) |
| 💾 Préparer la clé USB | [`4-outils/LISEZ-MOI.md`](../../4-outils/LISEZ-MOI.md) |

### Pour les élèves

| Support | Fichier |
|---|---|
| Fiche mémo (1 par binôme) | [`a-imprimer/06-fiche-memo-eleve.pdf`](a-imprimer/06-fiche-memo-eleve.pdf) |
| Le fichier de départ, déjà sur leur poste | [`code/depart_eleves_piste_bleue.py`](code/depart_eleves_piste_bleue.py) |
| **Code officiel de fin de séance** — le Filet | [`code/code_officiel_fin_de_seance.py`](code/code_officiel_fin_de_seance.py) |

---

## 9. Vers la séance 2

**Brique suivante :** *le jeu demande son nom au joueur et le salue.*
**Notion :** les variables et `input()`.
**Accroche à annoncer dès aujourd'hui :** *« Samedi prochain, votre jeu ne va plus seulement parler. Il va vous écouter. »*

**Ce qui démarre en séance 2 et pas aujourd'hui :**
- les **binômes officiels** (composés à froid ce soir, à partir du diagnostic) et le **contrat de binôme** lu à voix haute ;
- les **3 pistes** Bleue / Rouge / Noire ;
- le format de séance normal, avec deux ateliers et la chasse aux bugs.

**À préparer avec ce qui est sorti d'aujourd'hui :** les profils P0→P3 · les post-it · les résultats du Kahoot · la liste des 10 minutes.
