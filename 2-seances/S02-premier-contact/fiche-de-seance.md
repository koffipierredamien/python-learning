# Séance 2 — « Premier contact machine »

> **Cette séance reprend ce qui n'a pas pu être fait le 12 septembre.**
> La séance 1 s'est arrêtée après les missions de décollage : le premier contact machine, le Kahoot et
> la clôture n'ont pas eu lieu, et la méthode de travail n'a pas été expliquée. Tout cela est ici.
> Le reste du parcours décale d'une séance — c'est normal, et c'est sans conséquence : le projet
> n'a pas encore commencé à s'écrire.

---

## 0. Carte d'identité de la séance

| | |
|---|---|
| **Numéro** | 2 / 22 — Phase 0 « Décollage », deuxième moitié |
| **Date** | samedi 19 septembre 2026 · **12 h - 14 h** |
| **Organisation** | **Un enseignant par classe**, les deux classes en parallèle |
| **Notions** | `print()` · les guillemets · l'erreur et le message rouge · lire son programme de haut en bas |
| **Brique ajoutée au projet** | **L'écran d'accueil du jeu XO** — la brique prévue pour la séance 1 |
| **Livrable élève** | Un fichier `mon_xo/jeu.py` qui s'exécute et affiche l'écran d'accueil du jeu |
| **Nouveauté d'organisation** | Les **binômes officiels**, les **3 pistes** et **le Filet** commencent aujourd'hui |

### Les 4 objectifs, par ordre de priorité

1. **Chaque élève a lancé un programme qu'il a écrit lui-même**, et l'a vu s'afficher. C'est le seul objectif qui ne se négocie pas.
2. **Chaque élève a vu une erreur rouge, et a compris que ce n'est pas grave.** On la provoque exprès.
3. **La méthode de travail est posée** : binôme, pistes, cartes, le Filet. Elle servira les 20 séances suivantes.
4. **Personne ne repart sans un badge et sans avoir vu son nom au Mur de Mission.**

---

## 1. Le programme de la séance

| Horaire | Séquence | Durée |
|---|---|---|
| **12 h - 12 h 15** | Prière et accueil | 15 min |
| **12 h 15 - 12 h 25** | Récupération des exercices de décollage | 10 min |
| **12 h 25 - 12 h 45** | Le Kahoot : ce qui est resté de samedi dernier | 20 min |
| **12 h 45 - 13 h** | La méthode de travail | 15 min |
| **13 h - 13 h 10** | Pause | 10 min |
| **13 h 10 - 13 h 45** | **Premier contact machine : mon premier programme** | 35 min |
| **13 h 45 - 14 h** | Clôture : badges, Mur de Mission, post-it | 15 min |

**Le cœur de la séance est le bloc de 13 h 10.** Tout ce qui précède peut être raccourci ; lui, non.

### Le détail du bloc machine (13 h 10 - 13 h 45)

| Horaire | Quoi | Durée |
|---|---|---|
| 13 h 10 - 13 h 15 | Allumer, ouvrir Thonny, les 3 repères de la fenêtre | 5 min |
| 13 h 15 - 13 h 25 | Le live coding de l'enseignant, avec l'erreur volontaire | 10 min |
| 13 h 25 - 13 h 42 | **À vous** : l'écran d'accueil du jeu XO, en binôme | 17 min |
| 13 h 42 - 13 h 45 | On sauvegarde, et on distribue le Filet | 3 min |

### Les trois règles de temps de cette séance

1. **13 h 10, les machines sont allumées.** Si le Kahoot ou la méthode débordent, on les coupe — pas le bloc machine.
2. **On ne reprend aucune théorie de la séance 1.** Le Kahoot la révise à lui seul. Si une notion n'est pas passée, on la redit **en une phrase** au moment du Kahoot, pas plus.
3. **13 h 45, on arrête de coder**, même au milieu d'une ligne. La clôture fait autant pour la motivation que le code.

---

## 2. Préparation

### Avant la séance

| Quand | Quoi |
|---|---|
| **La veille** | Composer les **binômes** (voir § 3.4). C'est le seul vrai travail de préparation |
| **La veille** | Refaire soi-même le live coding avec [`code/live_coding_antiseche.py`](code/live_coding_antiseche.py). À voix haute, en entier |
| **La veille** | Préparer la clé : `python 4-outils/preparer_cle_usb.py --seance 2` |
| **30 min avant** | Sur chaque poste : lancer `installer_dossier_geeks.py` depuis la clé, puis `1-DEMO/verifier_un_poste.py`. Tout doit afficher `[OK]` |
| **30 min avant** | Dans Thonny : **police en taille 18 minimum** (Outils → Options → Éditeur). Sinon le fond de la salle ne lit rien |
| **30 min avant** | Ouvrir le Kahoot et le diaporama, projeter la première diapo, couper l'écran de veille |

### À imprimer

| Quantité | Document | Fichier |
|---|---|---|
| 1 par binôme | **Aide-mémoire machine** — les 5 gestes et les 3 erreurs fréquentes | `a-imprimer/01-aide-memoire-machine.pdf` |
| — | Les affiches de la séance 1 sont déjà au mur : cartes de signalisation, 3 avant moi, contrat de binôme, dictionnaire des erreurs, Mur de Mission | |
| — | **Badges / autocollants**, **2 post-it par élève**, minuteur visible | |

> **Si vous ne pouvez pas imprimer :** l'aide-mémoire se projette. Les 5 gestes tiennent au tableau.

### Le matériel du Filet

Le **code officiel de fin de séance** ([`code/code_officiel_fin_de_seance.py`](code/code_officiel_fin_de_seance.py))
est copié sur chaque poste par la clé, dans `GEEKS/xo_officiel/`. **On le distribue à tout le monde à 13 h 42**,
qu'on ait fini ou non. C'est la promesse du Filet : une absence, un poste en panne, un binôme qui s'est
perdu — personne ne commence la séance 3 en retard.

---

## 3. Le déroulé, bloc par bloc

### 3.1 · 12 h - 12 h 15 — Prière et accueil

Comme chaque samedi. Rien à changer.

**Sur les deux dernières minutes**, on annonce la séance en trois phrases :

> « Samedi dernier, on a beaucoup parlé, beaucoup réfléchi — et on n'a pas eu le temps d'allumer les machines.
> Aujourd'hui, on répare ça : **à 13 h 10, tout le monde est devant un clavier.**
> Avant, trois choses : vos exercices, un jeu, et la façon dont on va travailler ensemble pendant 20 samedis. »

---

### 3.2 · 12 h 15 - 12 h 25 — Récupération des exercices de décollage

**Ce qu'on fait :**

1. On ramasse les feuilles, rang par rang. On **note qui a rendu** dans l'onglet `Suivi` du classeur.
2. On feuillette **sans corriger** : ce n'est pas noté, et on n'a pas le temps.
3. On dit une phrase sur ce qu'on a vu : *« J'en ai lu trois en arrivant. Il y a des choses très justes, et une erreur qui revient souvent — on la reverra tout à l'heure. »*

**Ce qu'on ne fait pas :** nommer ceux qui n'ont rien rendu. On le note dans le classeur, on en parle en privé.

> **Ceux qui n'ont pas rendu** ne sont pas en retard : les exercices étaient facultatifs, et la séance
> d'aujourd'hui ne les suppose pas faits. C'est à dire à voix haute, une fois, pour tout le monde.

---

### 3.3 · 12 h 25 - 12 h 45 — Le Kahoot

**C'est le quiz préparé pour la séance 1 et qui n'a pas eu lieu.** Il révise toute la théorie du 12 septembre.

**Le support :** [`a-projeter/quiz-seance-1.pptx`](a-projeter/quiz-seance-1.pptx) — 15 questions,
une diapo par question, puis la réponse. Les questions et les corrigés sont dans
[`a-projeter/quiz-questions-et-reponses.md`](a-projeter/quiz-questions-et-reponses.md).
*(Ce quiz avait été préparé pour la séance 1 ; il a été déplacé ici, dans la séance où il est joué.)*

**Comment on joue — sans internet, avec les cartes de couleur :**

| Réponse | Carte à lever |
|---|---|
| 1 | 🔴 Rouge |
| 2 | 🔵 Bleu |
| 3 | 🟠 Orange |
| 4 | 🟢 Vert |

On projette la question, on lit les 4 réponses à voix haute, on compte « 3, 2, 1 » — **et tout le monde
lève sa carte en même temps**. On regarde la salle d'un coup d'œil, on affiche la réponse, on donne
l'explication **en une seule phrase**, on enchaîne.

**Le minutage, à tenir :** 2 min pour la règle du jeu · **15 questions à une minute** · 3 min de conclusion.
**En retard, on garde les 10 premières questions** et on saute les autres : elles ne se rattrapent pas,
elles ne manqueront à personne.

**Ce qu'on dit en conclusion :**

> « Personne n'a tout juste, et c'est normal : on a vu ça une seule fois. Ce qui compte, c'est que **tout
> est encore là dans votre tête**. Maintenant, on arrête de parler des ordinateurs. On va s'en servir. »

> **Le piège de ce bloc :** commenter chaque question pendant deux minutes. Quinze questions à deux
> minutes, c'est une demi-heure — et le bloc machine est mort. **Une phrase par question. Chronomètre visible.**

---

### 3.4 · 12 h 45 - 13 h — La méthode de travail

C'est le bloc qui n'a pas été fait samedi dernier. Il sert les 20 séances suivantes. **Quinze minutes, pas plus.**

#### a) Les binômes (6 min)

On annonce les binômes **déjà composés** — on ne les fait pas devant la classe, on perdrait dix minutes.

> **Comment les composer, la veille.** À partir de ce qu'on a vu aux missions de décollage :
> on associe un élève à l'aise **avec** un élève moins à l'aise — jamais deux débutants ensemble,
> jamais les deux plus rapides ensemble. Si le diagnostic n'est pas rempli, on compose à l'œil :
> ça marche presque aussi bien, et on corrigera la semaine suivante.

Puis la règle, au tableau, en deux lignes :

| | |
|---|---|
| **Le pilote** | il a le clavier et la souris. **Lui seul touche la machine.** |
| **Le copilote** | il lit la consigne à voix haute, il surveille les fautes, il ne prend jamais le clavier |
| **On échange** | **toutes les 10 minutes**, au signal. Celui qui pilotait devient copilote |

**L'engagement, à voix haute, tous ensemble** (c'est le contrat de binôme, déjà affiché au mur) :

> « Je ne prends pas le clavier de mon binôme. Je ne me moque pas. Je demande de l'aide à deux avant de la demander au professeur. »

#### b) Les trois pistes (4 min)

> « À partir d'aujourd'hui, à chaque atelier, **vous choisissez votre piste**. »

| Piste | Pour qui | Ce que c'est |
|---|---|---|
| 🔵 **Bleue** | on découvre | Le fichier est déjà écrit. Il y a des trous à remplir. **Il marche déjà quand on le lance.** |
| 🔴 **Rouge** | on suit | On écrit soi-même, avec le modèle à l'écran |
| ⚫ **Noire** | on veut plus | La même chose, plus un défi en plus |

**Les trois pistes arrivent au même résultat.** C'est la profondeur qui change, pas le programme.
**On change de piste quand on veut, d'une séance à l'autre.** Personne n'est « de la piste bleue ».

> **Aujourd'hui, tout le monde est en piste bleue** : c'est le premier contact machine, on ne complique rien.
> Les élèves qui finissent en avance passent au défi de la piste noire, écrit sur leur feuille.

#### c) Le Filet (3 min)

> « Voici ma promesse. **À la fin de chaque séance, je vous donne le code officiel**, celui qui marche,
> même si vous n'avez pas fini, même si vous étiez absent. Chaque samedi, tout le monde repart du même
> point. **Dans cette formation, on ne peut pas prendre du retard.** »

C'est la phrase la plus importante de la séance pour les élèves les plus fragiles. On la dit lentement.

#### d) Comment on est évalué (2 min)

> « Il n'y a **aucune note** ici, et aucun classement. Une chose est acquise quand vous savez faire trois
> choses : **ça marche · je sais l'expliquer · je sais le refaire tout seul.** C'est tout. »

---

### 3.5 · 13 h - 13 h 10 — Pause

Dix minutes. On en profite pour **allumer les machines** et vérifier que Thonny s'ouvre partout.
**À 13 h 10, on commence — les retardataires s'assoient sans qu'on les attende.**

---

### 3.6 · 13 h 10 - 13 h 45 — Premier contact machine

#### a) 13 h 10 - 13 h 15 · Les trois repères de Thonny

On projette la fenêtre de Thonny. **Trois choses seulement** — on ne fait pas la visite du logiciel :

| | |
|---|---|
| **En haut** | la zone blanche : **c'est là qu'on écrit.** |
| **En bas** | la zone grise : **c'est là que l'ordinateur répond.** On ne peut pas y écrire son programme |
| **Le bouton vert, ou F5** | **c'est « vas-y ».** Rien ne se passe tant qu'on n'appuie pas dessus |

Puis les cartes de signalisation, posées sur chaque poste, en 1 minute :

| Carte | Ce qu'elle dit |
|---|---|
| 🟢 **Vert** | ça avance, tout va bien |
| 🟠 **Orange** | je suis bloqué, j'ai besoin d'aide — **je continue à chercher en attendant** |
| 🔴 **Rouge** | j'ai un problème de machine : elle ne démarre pas, l'écran est figé |
| 🔵 **Bleu** | j'ai fini, je veux le défi en plus |

> « **Ici, on ne lève pas la main : on lève une carte.** Comme ça je vois toute la salle d'un coup d'œil,
> et vous continuez à travailler pendant que j'arrive. »

#### b) 13 h 15 - 13 h 25 · Le live coding — « je code, vous prédisez »

L'anti-sèche complète, avec ce qu'on dit à chaque étape :
[`code/live_coding_antiseche.py`](code/live_coding_antiseche.py). **On tape devant eux, lentement.**
On ne lance pas le fichier tout fait.

**Avant chaque exécution, on s'arrête et on demande : « Qu'est-ce qui va s'afficher ? À trois. »**
On n'appuie sur F5 qu'après leur réponse.

1. **`print("Bonjour")`** — on épelle en verbalisant : *« p-r-i-n-t, ça veut dire AFFICHE. Une parenthèse qu'on ouvre et qu'on fermera toujours. Un guillemet, mon texte, un guillemet. »* Puis F5.
   → *« Vous venez de voir un ordinateur obéir. C'est tout le métier. »*
2. **Trois lignes à la suite** — on montre qu'il lit **de haut en bas, ligne par ligne, toujours**.
3. **L'erreur volontaire** — `print("Bonjour)` : il manque un guillemet. **C'est le moment le plus important de la séance.**

> **Ce qu'on dit devant le message rouge** — lentement, sans dramatiser :
> « Regardez. **Rouge.** Est-ce que l'ordinateur est cassé ? Non. Est-ce que je suis puni ? Non.
> **Il m'explique ce qu'il n'a pas compris.** Il dit `SyntaxError` : j'ai mal écrit quelque chose.
> Il me montre même la ligne. Le rouge n'est pas une punition, **le rouge est une information.**
> Aujourd'hui, celui qui voit du rouge lève le pouce : il a trouvé quelque chose. »

Puis on corrige devant eux, on relance, ça marche. **On laisse ça affiché.**

#### c) 13 h 25 - 13 h 42 · À vous : l'écran d'accueil du jeu XO

Le fichier est déjà sur chaque poste : `GEEKS/mon_xo/jeu.py`
(c'est [`code/depart_eleves_piste_bleue.py`](code/depart_eleves_piste_bleue.py)).

**La consigne, en trois phrases :**

> « Ouvrez `GEEKS`, puis `mon_xo`, puis `jeu.py`. **Appuyez tout de suite sur F5 : il marche déjà.**
> Ensuite, vous remplacez chaque `____` par ce qu'on vous demande — votre prénom, votre âge, votre
> phrase à vous. **Vous relancez après chaque changement.** Pilote au clavier, copilote sur la consigne. »

**Ce que l'enseignant fait pendant 17 minutes :** il circule, il ne s'assoit pas, il ne touche jamais le
clavier d'un élève. Devant une erreur, on ne corrige pas : **on lit le message rouge avec l'élève** et on
demande *« qu'est-ce qu'il te dit ? »*.

**Le signal des 10 minutes :** à 13 h 35, on annonce **l'échange pilote / copilote**. Tout le monde change.

**Les trois erreurs qui vont arriver** — les reconnaître d'un coup d'œil :

| Ce qui s'affiche | Ce qui s'est passé | Ce qu'on dit |
|---|---|---|
| `SyntaxError` | un guillemet ou une parenthèse manque | « Compte tes guillemets : ils vont par deux, comme des chaussures » |
| `NameError` | du texte écrit sans guillemets | « L'ordinateur a cru que c'était un ordre. Mets-le entre guillemets » |
| Rien ne se passe | il a écrit dans la zone grise du bas | « Remonte dans la zone blanche : c'est là qu'on écrit » |

**Pour ceux qui finissent avant 13 h 42** (carte bleue levée) : *« Ajoute deux lignes pour dessiner la grille
du morpion avec des points et des tirets. Regarde le modèle au tableau. »*

#### d) 13 h 42 - 13 h 45 · On sauvegarde, et le Filet

1. **`Ctrl + S`**, tous ensemble, au signal. On vérifie d'un coup d'œil que l'étoile a disparu du titre.
2. On ouvre `GEEKS/xo_officiel/` devant eux : *« Voilà le code officiel de la séance. Il est déjà sur votre poste. Celui qui n'a pas fini, celui qui n'était pas là : tout le monde repart avec. »*
3. Les binômes qui le souhaitent copient leur `jeu.py` dans `4-SAUVEGARDES-ELEVES/S02/` de la clé.

---

### 3.7 · 13 h 45 - 14 h — Clôture

C'est le bloc qui n'a pas eu lieu samedi dernier. **On ne le sacrifie pas une deuxième fois.**

#### a) Les badges (6 min)

On appelle les élèves par leur nom, on donne l'autocollant, on dit **pour quoi** en trois mots.

| Badge | Il s'obtient si… |
|---|---|
| 🧱 **Bâtisseur** | ton programme a affiché quelque chose |
| 🐞 **Chasseur de bug** | tu as eu une erreur rouge et tu l'as réparée |
| 🤝 **Copilote** | tu as aidé ton binôme sans prendre son clavier |
| 🎯 **Curieux** | tu as essayé quelque chose que personne n'avait demandé |

> **Tout le monde repart avec au moins un badge.** Celui qui a lancé le fichier de départ est Bâtisseur :
> c'est vrai, et c'est mérité.

#### b) Le Mur de Mission (5 min)

Chaque élève vient écrire son prénom sur la case de la séance 2. **Tout le monde passe.**
L'affiche est celle de la séance 1, déjà au mur.

#### c) Les post-it (4 min)

Deux post-it par élève, anonymes, déposés dans la boîte en sortant :

- l'un pour **une chose que j'ai comprise aujourd'hui** ;
- l'autre pour **une chose que je n'ai pas comprise**.

**On les lit le soir même**, et on commence la séance 3 par les deux questions qui reviennent le plus.

**Et la dernière phrase :**

> « Samedi prochain, votre jeu ne va plus seulement parler : **il va vous écouter.** Il va vous demander
> votre nom. À samedi, les Geeks ! »

---

## 4. Les plans de secours

| Ce qui arrive | Ce qu'on fait |
|---|---|
| **Le vidéoprojecteur ne marche pas** | Le Kahoot se lit à voix haute : les questions sont dans `quiz-questions-et-reponses.md`, les cartes de couleur suffisent. Le live coding se fait sur l'écran d'un poste, les élèves debout autour |
| **Une machine ne démarre pas** | Le binôme rejoint un autre poste : **trois élèves sur une machine, ça marche.** On note le poste dans le classeur |
| **Il n'y a pas assez de machines** | On garde les binômes et on alterne : 8 minutes chacun, chronomètre visible |
| **Le bloc machine commence à 13 h 25** (retard accumulé) | On coupe le live coding à `print("Bonjour")` + l'erreur volontaire, et on passe à la mission. **Ces deux moments-là ne se coupent jamais** |
| **Un élève finit en 3 minutes** | Carte bleue → le défi de la grille. Puis il devient **Geek Mentor** : il aide deux binômes voisins, sans toucher aux claviers |
| **Un élève bloque et se décourage** | On s'assoit à côté, on lui fait relancer le fichier **tel quel** pour qu'il voie que ça marche, puis **une seule** modification : son prénom. C'est suffisant pour aujourd'hui |
| **Un nouvel élève arrive aujourd'hui** | Il prend le fichier de départ comme tout le monde : la séance 2 ne suppose rien de la séance 1. On lui donne la fiche mémo de la séance 1 en partant |
| **Un enseignant est absent** | Les deux classes fusionnent dans la même salle. On garde le même déroulé, le bloc machine passe à 45 min par rotation |

---

## 5. Après la séance, le soir même

1. **Le classeur** ([`3-suivi/`](../../3-suivi/LISEZ-MOI.md)) : présence `S02`, la production de chacun dans `Suivi`, et les exercices rendus.
2. **L'onglet `Indiscipline`**, s'il s'est passé quelque chose. À chaud, pas trois jours après.
3. **Les post-it** : on les lit, on garde les deux questions les plus fréquentes pour l'ouverture de la séance 3.
4. **L'onglet `Journal`** : trois lignes, une par classe. Ce qui a marché, ce qui a débordé, qui décroche.
5. **Les binômes qui ont fonctionné**, et ceux à défaire la semaine prochaine.

---

## 6. Ce que la séance 2 laisse pour la séance 3

| | |
|---|---|
| **Brique suivante** | Le jeu **demande son nom au joueur** : `input()` et les variables |
| **Point de départ** | [`code/code_officiel_fin_de_seance.py`](code/code_officiel_fin_de_seance.py), distribué aujourd'hui à tout le monde |
| **Ce qui est déjà en place** | Les binômes, les pistes, les cartes, le Filet — on ne les réexplique plus |
