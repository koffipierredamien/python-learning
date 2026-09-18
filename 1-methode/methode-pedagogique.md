# Méthode pédagogique — Apprendre Python en construisant le jeu XO

**Classes concernées :** Jerusalem Geeks (9–12 ans) · Jeremiah Geeks (12–18 ans)
**Format :** 1 séance de 2 h, chaque samedi, de 12 h à 14 h — ouverte par un temps de prière de 15 minutes
**Encadrement :** 2 enseignants — **un par classe**, les deux classes en parallèle
**Projet fil rouge :** le jeu XO (Tic-Tac-Toe), de la première ligne de code jusqu'à l'application graphique jouable

---

## 0. Résumé exécutif — la stratégie en une page

Le problème n'est pas « comment enseigner Python ». Le problème est : **comment faire progresser ensemble, dans une même salle, un enfant qui n'a jamais tenu une souris et un adolescent qui code déjà — pendant 5 mois, sur un projet où chaque séance dépend de la précédente, avec seulement 2 enseignants.**

Notre réponse tient en sept principes. Ils sont conçus pour fonctionner ensemble ; en retirer un fait tomber les autres.

| # | Principe | Ce qu'il résout |
|---|---|---|
| 1 | **Un seul projet, une seule classe, jamais de groupes de niveau figés** | Évite la stigmatisation et la classe à deux vitesses |
| 2 | **Différencier par la profondeur, jamais par le contenu** — chaque atelier existe en 3 pistes (Bleue / Rouge / Noire) que l'élève choisit lui-même | Chacun travaille à sa hauteur, tout le monde traite la même notion |
| 3 | **Le Filet : un « code de départ officiel » distribué au début de CHAQUE séance** | Supprime le décrochage cumulatif : rater une séance ne condamne jamais la suite |
| 4 | **Un enseignant par classe, et cinq réflexes pour tenir seul** : j'alterne parler / circuler, les cartes sont mes yeux, les élèves s'entraident d'abord, 2 Geek Mentors par séance, je ne m'assois jamais | Personne ne reste bloqué plus de 5 minutes, même sans deuxième adulte |
| 5 | **Le Sas « Permis Machine »** pour les grands débutants, en parallèle et sans les sortir du groupe | Traite le cas « ne sait pas utiliser un ordinateur » sans créer une sous-classe |
| 6 | **Motivation par le grade, le Mur de Mission et la démo** — tournoi final, présentation aux parents | Tient l'engagement sur 20+ semaines |
| 7 | **Évaluation par la preuve, jamais par la note** : ça marche / je sais l'expliquer / je sais le refaire | Enlève la peur de l'erreur, indispensable pour apprendre à coder |

**La promesse faite aux élèves :** *« À la fin de chaque samedi, ton jeu marche mieux qu'en arrivant. À la fin du parcours, tu auras un jeu que tu pourras montrer, faire jouer et installer chez toi. »*

---

## 1. Le problème posé, formulé précisément

Nous devons concevoir un dispositif qui tienne face à **quatre contraintes simultanées** :

1. **Hétérogénéité inconnue et extrême.** Le spectre va de « ne sait pas ouvrir une fenêtre / ne sait pas taper au clavier » à « a déjà fait du Scratch ou du Python ». Nous ne connaîtrons le vrai profil qu'à la première séance.
2. **Encadrement rare.** 2 enseignants. Si 15 élèves lèvent la main en même temps, le dispositif s'effondre.
3. **Projet cumulatif.** « Chaque séance ajoute une brique » est pédagogiquement excellent (sens, motivation, fierté) mais crée un risque mortel : *l'élève qui n'a pas fini la brique n° 4 ne peut pas poser la brique n° 5.* Un absent est mécaniquement éliminé. C'est le point de rupture le plus probable de tout le programme.
4. **Public jeune.** L'attention d'un enfant de 9 ans ne tient pas 2 h ; la motivation d'un adolescent ne tient pas sans défi ni reconnaissance.

Toute la méthode ci-dessous découle de ces quatre contraintes.

---

## 2. Les sept principes directeurs (détaillés)

### Principe 1 — Une seule classe, un seul projet, pas de groupes de niveau

Nous **n'ouvrons pas** de « groupe débutant » et de « groupe avancé ». Trois raisons :

- Séparer une classe en deux groupes de niveau la rendrait ingérable : **un enseignant seul ne peut pas animer deux groupes différents en même temps.**
- Les groupes de niveau enferment : un enfant étiqueté « faible » à la séance 2 le reste jusqu'à la fin.
- L'écart de niveau est une **ressource** : celui qui explique consolide deux fois plus que celui qui écoute.

**En revanche, les deux tranches d'âge restent deux classes séparées** (Jerusalem 9–12, Jeremiah 12–18) : le vocabulaire, le rythme, la durée d'attention et les métaphores ne sont pas transposables (voir § 12).

### Principe 2 — Différencier par la profondeur : le système des 3 pistes

C'est le cœur du dispositif. **Tous les élèves travaillent la même notion, à la même heure, sur la même brique du jeu.** Seule la *forme* de la tâche change. Chaque atelier est publié en trois versions, présentées comme des pistes de ski :

| Piste | Pour qui | Forme de la consigne | Exemple (séance « demander le coup du joueur ») |
|---|---|---|---|
| 🔵 **Bleue** — *guidée* | Débutant total, ou notion pas encore digérée | Code à trous + copie d'écran du résultat attendu + étapes numérotées | On donne le `input()` complet, l'élève complète le message affiché et teste |
| 🔴 **Rouge** — *standard* | La cible du groupe | Consigne écrite en français + rappel des outils disponibles | « Demande au joueur le numéro de la case et range la réponse dans une variable » |
| ⚫ **Noire** — *défi* | Ceux qui vont vite ou qui savent déjà | Consigne ouverte + contrainte supplémentaire | « Et si le joueur tape `stop` ? Et s'il tape `abc` ? Que doit-il se passer ? » |

**Règles d'or des pistes :**

1. **C'est l'élève qui choisit sa piste, à chaque atelier.** Ce n'est pas une étiquette permanente. On peut être Bleue le matin sur les boucles et Noire l'après-midi sur l'affichage.
2. **Aucune piste n'est « le vrai travail ».** La piste Bleue produit exactement le même jeu fonctionnel que la Noire. Le jeu de l'élève Bleue marche.
3. **La piste Noire n'est jamais « la suite du programme ».** Elle approfondit, elle n'avance pas. Sinon les rapides prennent une avance impossible à rattraper et le groupe explose.
4. **L'enseignant oriente, il n'assigne pas.** « Tu as fini en 4 minutes la dernière fois, essaie la Rouge aujourd'hui. » / « Prends la Bleue, tu passeras en Rouge sur la deuxième partie. »

> **Pourquoi ça marche :** le groupe reste synchronisé sur le projet (indispensable pour un projet cumulatif), tout en laissant chacun travailler à son niveau de difficulté réel. Personne ne s'ennuie, personne ne se noie.

### Principe 3 — Le Filet : le code de départ officiel

**C'est la mesure la plus importante du document.**

À chaque début de séance, les enseignants distribuent (clé USB, dossier partagé, dépôt Git, ou impression + fichier prêt sur les machines) le **« code de départ officiel » : le fichier du projet tel qu'il devrait être à la fin de la séance précédente.**

Chaque élève commence la séance en ouvrant ce fichier, **quel que soit ce qu'il a réussi ou raté la semaine d'avant.**

Conséquences :

- Un élève absent revient et repart au même point que les autres. **Il ne rate qu'une notion, jamais le projet.**
- Un élève qui n'a pas fini son atelier n'est pas puni la semaine suivante.
- Un élève dont le code est cassé, effacé, ou irrécupérable repart proprement en 30 secondes.
- Un nouvel inscrit à la séance 7 peut intégrer le groupe (voir protocole d'intégration, Annexe A3).

Chaque élève conserve **deux dossiers** :
- `mon_xo/` — sa version personnelle, avec ses expériences, ses couleurs, ses bêtises assumées ;
- `xo_officiel/` — la version de référence, remise à jour au début de chaque séance.

L'élève travaille dans `mon_xo/`. S'il se perd, il recopie depuis `xo_officiel/`. **On dit aux élèves, dès la séance 1 : « Casser ton code n'est jamais grave. On a toujours une copie de secours. »** C'est aussi ce qui autorise l'expérimentation, donc l'apprentissage.

En fin de parcours, pour les Jeremiah Geeks, ce mécanisme devient l'introduction naturelle à Git et GitHub (« les grands en font leur métier »).

### Principe 4 — Un enseignant par classe : les cinq réflexes du prof seul

**L'organisation retenue : un enseignant par classe, les deux classes en parallèle.** Jeremiah Geeks (12–18)
d'un côté, Jerusalem Geeks (9–12) de l'autre. Personne ne circule pendant que vous parlez.

Toute la méthode tient encore — mais elle repose désormais sur cinq réflexes, et sur l'entraide entre voisins.

| # | Le réflexe | Pourquoi |
|---|---|---|
| **1** | **J'alterne explicitement : « je parle » ou « je circule ».** Jamais les deux. Quand je parle, personne ne code. Quand je circule, je ne m'adresse plus au groupe. | Ce que deux enseignants faisaient en même temps, un seul le fait l'un après l'autre. |
| **2** | **Les cartes de signalisation sont mes yeux.** Je balaye la salle toutes les 2 minutes, sans bouger. | Seul, je ne peux pas passer à chaque poste. C'est la carte qui vient à moi. |
| **3** | **Les élèves s'entraident d'abord** : je relis · je demande à mon voisin · on regarde la fiche. Ensuite seulement, la carte orange. | Ce n'est plus un confort, c'est **la condition** pour qu'une classe seule tienne. |
| **4** | **Je nomme 2 Geek Mentors par séance** — les premières cartes bleues. Ils aident 10 minutes, **sans jamais toucher le clavier des autres**. | C'est ce qui remplace le deuxième adulte. |
| **5** | **Je ne m'assois jamais**, et je fais un tour complet avant de répondre deux fois au même élève. | Sinon un élève bavard capte tout le temps, et trois autres décrochent en silence. |

**Le système des cartes de signalisation** (un jeu de cartes cartonnées par poste, posé bien visible sur l'écran) :

- 🟢 **Vert** — « Tout va bien, on avance. »
- 🟠 **Orange** — « On est bloqués, on a besoin d'aide, mais on continue à chercher. »
- 🔴 **Rouge** — « On est totalement arrêtés, rien ne marche. » (Priorité absolue.)
- 🔵 **Bleu** *(bonus)* — « On a fini, on est disponible pour aider. » → l'élève devient **Geek Mentor** pour 10 minutes.

Ce système supprime les mains levées, le bruit, l'attente passive, et donne une **carte thermique instantanée**
de la classe — ce qui, seul, est la seule façon de savoir où on en est.

**La règle des 3 avant moi** (affichée au mur) : avant de lever la carte orange, on essaie dans l'ordre :
1. **Je relis** la consigne et le message d'erreur à voix haute.
2. **Je demande à mon voisin**, puis je cherche dans la **fiche mémo** de la séance.
3. **On demande à la table d'à côté** (30 secondes maximum).
Ensuite seulement : carte orange.

> **Garde-fou :** une carte orange doit être servie en moins de 5 minutes. Si la salle est saturée d'orange,
> c'est un signal : **on arrête tout le monde** et on reprend la notion devant. Trois cartes orange sur la même
> difficulté = la faute est à l'enseignement, pas aux élèves.

**Les deux enseignants se parlent après la séance, pas pendant.** 15 minutes seul pour le suivi, puis
**10 minutes ensemble** : ce qui a marché, ce qui a raté, ce qu'on change samedi. C'est le seul moment où les
deux classes se parlent — il n'est pas facultatif. Chacun remplit sa propre ligne dans l'onglet `Journal`
du classeur : **une ligne par séance et par classe**.

### Principe 5 — Le Sas « Permis Machine »

Certains élèves ne savent pas utiliser un ordinateur. **Ils ne doivent ni bloquer le groupe, ni être mis à part.** Dispositif en trois volets :

**a) Les 30 minutes d'avance (facultatif mais fortement recommandé).** Une demi-heure avant la séance officielle, un enseignant ouvre la salle pour un atelier libre « Permis Machine » : allumer/éteindre, souris, clic droit, fenêtres, clavier, enregistrer un fichier, retrouver un fichier. Ouvert à tous, jamais nominatif — on l'annonce comme un bonus, pas comme du rattrapage.

**b) Le Passeport Machine.** Un petit livret de 12 gestes à valider, un tampon par geste (voir Annexe A1). Chaque geste validé est coché devant l'élève. C'est valorisant, mesurable, et ça donne au grand débutant des victoires immédiates dès la séance 1, avant même de coder.

**c) La dictée de code interdite.** Pour un élève qui tape à 5 mots/minute, recopier 15 lignes prend 20 minutes et il rate la notion. Solution : **sur piste Bleue, le squelette de code est déjà dans le fichier** ; l'élève ne tape que ce qui porte du sens (une valeur, une condition, un mot). On enseigne la logique, pas la dactylographie. La vitesse de frappe viendra toute seule.

**d) L'apprentissage du clavier par le jeu**, 5 minutes en rituel d'accueil (voir § 8), sur un logiciel de frappe — présenté comme un mini-jeu chronométré avec record personnel.

### Principe 6 — Motivation : grades, Mur de Mission, démos

Un parcours de 20+ samedis a besoin d'un moteur. Le nôtre a trois étages :

**1. Les grades (progression individuelle, liée aux compétences).** L'élève monte en grade dans la guilde :

`Novice` → `Apprenti Codeur` → `Codeur` → `Ingénieur` → `Architecte` → `Maître Geek`

Chaque grade s'obtient en validant un **bloc de compétences** (voir § 11), pas en assistant à des séances. Remise du grade en début de séance, devant le groupe, avec un bracelet, un autocollant ou une carte de grade.

**2. Le Mur de Mission (progression collective).** Une grande affiche : la carte du projet XO en 22 étapes, sous forme de parcours (fusée, montagne ou carte au trésor). À chaque fin de séance, **la classe entière** avance d'une case. C'est collectif : la classe réussit ou échoue ensemble, ce qui pousse les rapides à aider au lieu de fuir en avant.

**3. Les grands rendez-vous.** Ils donnent une raison d'aller jusqu'au bout :
- **Séance 9 — La première démo** : le jeu tourne en console, on y joue à deux.
- **Séance 15 — Le concours de design** : chacun personnalise son plateau.
- **Séance 19 — La Nuit du bug** : les élèves s'échangent des jeux volontairement cassés à réparer, en équipes.
- **Séance finale — Le Tournoi XO + démo aux familles** : les élèves font jouer leurs parents à leur propre programme, et repartent avec leur jeu installé.

> **À proscrire absolument :** le classement individuel public par points. Il démotive durablement 70 % du groupe. Les points, s'il y en a, sont **collectifs**.

### Principe 7 — Évaluation par la preuve, jamais par la note

**Aucune note, jamais.** Une compétence est validée quand l'élève apporte **trois preuves** :

1. **Ça marche** — il lance son programme, ça fonctionne devant l'enseignant (15 secondes).
2. **Je sais l'expliquer** — il explique à son voisin, en français, ce que fait la ligne (30 secondes). *C'est le filtre anti-copie.*
3. **Je sais le refaire** — il réussit un micro-défi de la même famille sur une variante (2 minutes), lors d'une séance ultérieure.

L'auto-évaluation de fin de séance tient en une question posée à la classe, à voix haute : **« Qu'est-ce que vous avez compris aujourd'hui, et de quoi n'êtes-vous pas encore sûrs ? »** Ce qui en ressort se note le soir dans l'onglet `Journal` du classeur : c'est le meilleur outil de préparation de la séance suivante qui existe.

---

## 3. Diagnostic initial : connaître le groupe sans le classer

### Séance 0 / première demi-heure de la séance 1 : le « Test de Décollage »

Il est **présenté comme un jeu, jamais comme un test**. Il dure 25 minutes, se fait en rotation sur 3 stations, et sert **uniquement aux enseignants** (les résultats ne sont jamais communiqués aux élèves ni aux parents).

| Station | Durée | Ce qu'on observe | Comment |
|---|---|---|---|
| **1. Le pilotage** | 8 min | Souris, double-clic, clavier, fenêtres, enregistrer/retrouver un fichier | Mini-parcours : « ouvre ce dossier, crée un fichier, écris ton nom, enregistre-le sur le Bureau, retrouve-le » |
| **2. La logique** | 8 min | Raisonnement algorithmique **sans ordinateur** | 4 énigmes papier : ranger des étapes dans l'ordre, suivre un labyrinthe avec des instructions, trouver la règle d'une suite, expliquer la règle du morpion à un extraterrestre |
| **3. L'expérience** | 5 min | Vécu numérique et code | Questionnaire de 6 questions à cocher : as-tu un ordinateur à la maison ? as-tu déjà fait Scratch / Python / autre ? sais-tu ce qu'est un fichier ? lis-tu un peu l'anglais ? |
| **Observation continue** | — | Attitude face à la difficulté | L'autre enseignant note discrètement : abandonne vite / demande / persévère / aide les autres |

### Les 4 profils enseignants (jamais communiqués aux élèves)

| Profil | Description | Réponse pédagogique prioritaire |
|---|---|---|
| **P0 — Découvreur** | Ne maîtrise pas la machine | Passeport Machine, piste Bleue, squelette de code fourni, voisin P1, vérification visuelle 3×/séance |
| **P1 — Initié** | Sait utiliser un ordinateur, n'a jamais codé | **C'est la cible standard du cours.** Piste Rouge |
| **P2 — Autonome** | À l'aise, logique solide, éventuellement un peu de Scratch | Piste Rouge → Noire, rôle de Geek Mentor à partir de la séance 4 |
| **P3 — Avancé** | Sait déjà coder | Piste Noire systématique + **mission spéciale** : responsable d'un module bonus du jeu (score, sons, thèmes, IA). Voir § 13, cas B1 |

Les profils sont **réévalués à la séance 5 et à la séance 12**. Un P0 devient très souvent P1 en six semaines : le dispositif doit acter cette progression, sinon il enferme.

---

## 4. Le rituel de séance : les 2 heures, minute par minute

Le rituel est **identique chaque samedi**, de **12 h à 14 h**, et il ouvre toujours par le temps de prière. La répétition rassure les jeunes élèves, réduit le temps perdu, et permet à un élève absent de reprendre sans effort.

| Temps | Bloc | Contenu | Qui |
|---|---|---|---|
| **12 h - 12 h 15** | 🙏 **Prière et accueil** | La séance ouvre par le temps de prière. J'accueille à la porte, je coche la présence, puis je rassemble. | L'enseignant conduit |
| **12 h 15 - 12 h 25** | 🎬 **Le WOW et le rappel** | On montre **le résultat de la séance** avant de commencer : « Voilà ce que votre jeu saura faire dans deux heures. » Puis rappel express de la séance précédente en 3 questions à main levée. Les élèves ouvrent le projet et récupèrent le **code de départ officiel**. | L'enseignant, debout devant |
| **12 h 25 - 12 h 40** | 🧠 **La notion** | Une seule notion nouvelle par séance. Introduite en **débranché** (avec le corps, des cartes, des objets) puis en **live coding lent** avec la règle « je code, vous prédisez ». **L'enseignant fait volontairement une erreur et la répare devant tout le monde.** | L'enseignant, debout devant |
| **12 h 40 - 13 h** | 🔨 **Atelier 1** | Chacun code sur son poste, piste Bleue / Rouge / Noire au choix. S'il manque des machines, deux élèves partagent un poste et alternent à 12 h 50. | **Je circule** — je ne parle plus au groupe |
| **13 h - 13 h 10** | 🥤 **Pause** | Pause réelle : on se lève, on sort de la salle, on bouge. Non négociable, surtout pour les 9–12 ans. | — |
| **13 h 10 - 13 h 35** | 🔨 **Atelier 2** | Deuxième moitié de la brique + intégration dans le jeu complet. | **Je circule** — je ne parle plus au groupe |
| **13 h 35 - 13 h 47** | 🐞 **Chasse aux bugs croisée** | Chacun teste **le jeu de son voisin** (« essaie de le faire planter »). Les élèves rapides deviennent testeurs officiels et Geek Mentors. | J'organise les échanges |
| **13 h 47 - 13 h 55** | 🎤 **Mise en commun** | 2 élèves montrent leur écran (2 min chacun, tournant). Je récapitule la notion en 3 phrases. Distribution du **défi maison facultatif**. Sauvegarde et publication du **nouveau code officiel**. | L'enseignant, debout devant |
| **13 h 55 - 14 h** | 🏅 **Clôture rituelle** | Remise des grades du jour, s'il y en a. Avancée du Mur de Mission. La question « qu'avez-vous compris, de quoi n'êtes-vous pas sûrs ? ». Rangement. | L'enseignant |

**Règle des blocs d'attention :** aucun bloc où l'élève est passif ne dépasse **15 minutes** (Jerusalem) ou **20 minutes** (Jeremiah). Au-delà, la classe décroche, quel que soit le talent de l'orateur.

---

## 5. Adaptation aux deux classes

| | **Jerusalem Geeks (9–12)** | **Jeremiah Geeks (12–18)** |
|---|---|---|
| Bloc d'attention max | 12–15 min | 20–25 min |
| Métaphores | Concrètes et corporelles : la variable est une **boîte** étiquetée, la boucle est une **ronde**, la fonction est une **recette de cuisine** | Fonctionnelles : mémoire, structure de données, réutilisation, factorisation |
| Activités débranchées | Systématiques, avec le corps et des objets (cartes, gobelets, déplacements dans la salle) | Ponctuelles, au tableau, sous forme de défis logiques |
| Vitesse de frappe | Squelettes de code généreusement fournis | Frappe complète attendue à partir de la séance 5 |
| Nommage | Français (`plateau`, `joueur`, `case_choisie`) | Français d'abord, anglais introduit à mi-parcours |
| Autonomie | Consignes très découpées, une étape visible à la fois | Consignes globales, découpage à faire par l'élève (c'est l'exercice) |
| Ambition finale | Jeu graphique jouable à 2 + personnalisation | Jeu graphique + **IA de l'ordinateur** + score persistant + initiation Git/GitHub |
| Gestion de l'écart d'âge interne | — | Les 16–18 ans prennent le rôle de **Chef d'équipe** sur des modules ; ne pas les faire travailler exclusivement avec des 12 ans |
| Ton | Enthousiaste, ludique, beaucoup de célébration | Respectueux, exigeant, « on fait du vrai développement » — les ados détestent être infantilisés |

**Les deux classes suivent la même méthode et la même colonne vertébrale de projet.** Seuls le rythme, le vocabulaire et la profondeur changent. Cela divise par deux la charge de préparation des enseignants.

---

## 6. Environnement technique et plans de secours

Le premier tueur de séance n'est pas la pédagogie, c'est l'installation logicielle. Règles :

1. **Un seul environnement, identique pour tous, installé et testé par les enseignants avant la séance 1.** Aucun élève n'installe quoi que ce soit pendant les 10 premières séances.
2. **Recommandation : Thonny** (éditeur Python conçu pour les débutants : installation unique, mode pas-à-pas, visualisation des variables, messages d'erreur simplifiés). Alternative en ligne si les machines sont verrouillées.
3. **Version Python figée** et notée sur une fiche affichée. Un même code doit tourner à l'identique sur toutes les machines.
4. **Le jeu doit fonctionner sans internet.** Internet est un confort, jamais une dépendance.

**Plans de secours (à préparer avant la séance 1) :**

| Panne | Plan B |
|---|---|
| Pas d'internet | Tout le contenu sur clé USB + fiches papier. Le code officiel se distribue par clé. |
| Une machine tombe en panne | L'élève rejoint le poste d'un voisin : à deux sur une machine, on travaille très bien. Une machine de réserve allumée en fond de salle. |
| Plusieurs machines HS | Bascule sur la **séance débranchée équivalente** — chaque séance a une version papier prête (jeu de rôle, cartes-instructions, plateau XO en carton). |
| Coupure de courant | Séance débranchée + défi logique en équipes. |
| Un enseignant absent | **Mode dégradé** : pas de notion nouvelle. Séance « Atelier & Consolidation » : rattrapage, piste Bleue pour tous ceux qui en ont besoin, défis Noirs pour les autres, Geek Mentors activés. La brique est reportée d'une semaine. |

---

## 7. Traitement des cas particuliers

La matrice complète — **35 cas, avec signal de détection, réponse immédiate, réponse de fond et responsable** — est en **[Annexe A3](annexes/A3-matrice-des-cas.md)**. Elle couvre :

- **A. Entrée & niveau** : non-utilisateur d'ordinateur, frappe très lente, lecture difficile / dyslexie, non-anglophone face aux messages d'erreur, élève qui sait déjà coder.
- **B. Rythme** : finit en 3 minutes, ne finit jamais, abandonne en cours d'atelier, refuse de travailler.
- **C. Assiduité** : absence ponctuelle, absences répétées, arrivée en cours de parcours, retards chroniques.
- **D. Matériel** : pas d'ordinateur à la maison, panne, pas d'internet, versions différentes, ordinateur partagé.
- **E. Relationnel & émotionnel** : élève moqué, timide qui n'ose pas demander, leader qui monopolise, démotivation, peur de l'erreur, crise de frustration devant un bug.
- **F. Cognitif** : blocage sur une notion clé, erreurs d'indentation répétées, copie sans comprendre, confusion `=` / `==`.
- **G. Classe & organisation** : effectif qui grossit, écart d'âge interne, enseignant absent, salle indisponible.
- **H. Projet** : code irrécupérable, élève qui veut faire un autre jeu, élève qui a terminé tout le parcours.

Deux principes transversaux gouvernent toute la matrice :

> **Aucun cas ne doit ralentir le groupe. Aucun cas ne doit exclure un élève.**
> Chaque fois que ces deux exigences semblent s'opposer, la réponse est toujours la même : **le Filet** (§ 2.3) et **les pistes** (§ 2.2).

---

## 8. Pilotage de la qualité

### Le tableau de suivi (2 minutes après chaque séance)

Une ligne par élève, une colonne par séance. Trois symboles seulement :

- `✔` a produit la brique de la séance (piste indiquée : B / R / N)
- `~` a produit partiellement — **à revoir la semaine prochaine**
- `✖` absent ou n'a pas produit — **priorité de vigilance à la séance suivante**

**Règle de déclenchement :** deux `~` ou `✖` consécutifs = l'élève est mis sur la **liste des 10 minutes**. Je lui consacre 10 minutes en tête-à-tête à la séance suivante, pendant l'atelier 2 — c'est le moment où le reste de la classe travaille sans moi. C'est un rendez-vous, pas une punition — et c'est ce qui empêche un décrochage silencieux de devenir un abandon.

### Les indicateurs de santé du dispositif

| Indicateur | Cible | Que faire si hors cible |
|---|---|---|
| Élèves ayant un jeu fonctionnel en fin de séance | **100 %** | Alléger la brique ou renforcer la piste Bleue |
| Temps d'attente moyen après carte orange | < 5 min | Réduire la difficulté, renforcer les fiches mémo, activer plus de Geek Mentors |
| Même notion citée comme « pas sûr » à la clôture | < 30 % du groupe | La notion est reprise en ouverture de la séance suivante |
| Taux de présence | > 85 % | Enquête auprès des familles, revoir l'attractivité |
| Élèves déclarant s'ennuyer | 0 | Renforcer les pistes Noires et les missions spéciales |

### La revue des enseignants (15 minutes, après chaque séance)

Trois questions, écrites dans un carnet partagé :
1. Qui a décroché aujourd'hui, et qu'est-ce qu'on fait samedi prochain ?
2. Quelle explication n'a pas fonctionné, et comment on la reformule ?
3. La brique de la semaine prochaine est-elle trop grosse ?

---

## 9. Les familles

- **Réunion de lancement (30 min, avant la séance 1)** : montrer le jeu final, expliquer qu'il n'y a **pas de notes**, expliquer que **l'absence n'exclut pas** (le Filet), et demander une seule chose : la régularité.
- **Message court après chaque séance** (2 lignes, groupe de discussion) : « Aujourd'hui les Geeks ont appris à ___ . Leur jeu sait maintenant ___ . Défi facultatif : ___ . »
- **Aucun devoir obligatoire.** Tous les élèves n'ont pas d'ordinateur à la maison ; rendre le travail à la maison obligatoire créerait une inégalité immédiate et durable. Les défis maison sont des bonus, jamais requis pour suivre.
- **Deux rendez-vous ouverts** : la démo de mi-parcours et le tournoi final.

---

## 10. Ossature du parcours (vue macro, à détailler dans un second temps)

Cette progression n'est donnée ici que pour vérifier que la méthode tient sur la durée. Le découpage séance par séance fera l'objet du document suivant.

| Phase | Séances | Brique ajoutée au projet | Notions Python |
|---|---|---|---|
| **0. Décollage** | 1–2 | Test de Décollage, premier contact machine, le jeu s'annonce et demande le nom du joueur | environnement, exécuter un programme, `print()`, la variable, `input()` |
| **1. Parler au joueur** | 3–6 | Le jeu dit bonjour, demande les noms, affiche un plateau vide | variables, `input()`, `print()`, chaînes, types |
| **2. Le plateau vit** | 7–10 | On place un X ou un O, on rejoue, on alterne les joueurs | listes, indices, conditions, boucles — **1ʳᵉ démo jouable en S9** |
| **3. Les règles du jeu** | 11–14 | Coups invalides refusés, détection du gagnant, match nul, fin de partie | fonctions, `while`, opérateurs logiques, algorithme de victoire |
| **4. L'interface graphique** | 15–19 | Fenêtre, grille cliquable, symboles dessinés, personnalisation, rejouer | Tkinter, événements, callbacks — **concours de design en S15, Nuit du bug en S19** |
| **5. Finition & intelligence** | 20–22 | Score, sons, écran de victoire, **IA de l'ordinateur** (Jeremiah), distribution du jeu | organisation du code, algorithme de choix, packaging — **Tournoi final** |

---

## 11. Ce qu'il reste à décider avec vous

Ces cinq points conditionnent le calibrage fin du parcours et ne peuvent pas être tranchés sans vous :

1. **Effectifs par classe** — 15 élèves inscrits à ce jour (7 Jerusalem, 8 Jeremiah), soit 7 à 8 élèves par classe : parfaitement tenable seul. **Au-delà de 12 élèves dans une classe seule, il faudra un deuxième adulte ou un Geek Mentor permanent.**
2. **Le matériel** — un ordinateur par élève, ou un pour deux ? S'il en manque, deux élèves partagent un poste et alternent.
3. **La possibilité d'ouvrir la salle 30 minutes avant** pour le Sas Permis Machine.
4. **Le nombre de séances disponibles** dans le calendrier (vacances, jours fériés) — l'ossature ci-dessus suppose 22 samedis.
5. **Le devenir des machines** : les élèves peuvent-ils repartir avec leur jeu (clé USB, envoi par mail) ? C'est un levier de motivation majeur.

---

## Annexes

- **[A1 — Test de Décollage & Passeport Machine](annexes/A1-diagnostic-et-passeport.md)** — les 3 stations et les 12 gestes du passeport
- **[A2 — Fiche de conduite de séance](annexes/A2-conduite-de-seance.md)** — le déroulé imprimable, la checklist avant/pendant/après, les scripts d'animation
- **[A3 — Matrice des cas particuliers](annexes/A3-matrice-des-cas.md)** — les 35 cas, détection, réponse immédiate, réponse de fond
- **[A4 — Grades et Mur de Mission](annexes/A4-grades-et-mur-de-mission.md)** — le système de motivation
- **[A6 — Dictionnaire des erreurs](annexes/A6-dictionnaire-des-erreurs.md)** — toutes les erreurs du parcours, avec la case à cocher quand elle a été traitée
- **[A5 — Outils et modèles](annexes/A5-outils-et-modeles.md)** — journal de bord, grille de test, message aux familles, et le renvoi vers les documents prêts à imprimer
