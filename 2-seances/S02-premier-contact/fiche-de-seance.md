# Séance 2 — « Premier contact machine »

> **Cette séance reprend ce qui n'a pas pu être fait le 12 septembre** — le premier contact machine, le
> quiz, la clôture et la méthode de travail — **et ajoute la brique du jour : le jeu demande ton nom.**
> Le parcours décale d'une séance. Voir le [compte rendu de la séance 1](../S01-decollage/compte-rendu.md).

---

## 0. Carte d'identité de la séance

| | |
|---|---|
| **Numéro** | 2 / 22 — Phase 0 « Décollage », deuxième moitié |
| **Date** | samedi 19 septembre 2026 · **12 h - 14 h** |
| **Organisation** | **Un enseignant par classe**, les deux classes en parallèle |
| **Notions** | **`print()`** · **la variable** · **`input()`** · lire un message d'erreur |
| **Brique ajoutée au projet** | L'écran d'accueil, **et le jeu qui demande son nom au joueur** |
| **Livrable élève** | Un fichier `mon_xo/jeu.py` qui s'exécute, pose une question et répond avec le nom du joueur |

> **Deux notions, deux démonstrations, deux ateliers.** On fait ce qui n'a pas été fait la semaine passée
> — `print()` et l'écran d'accueil — **et** ce qui était prévu pour aujourd'hui — la variable et `input()`.
> Le bloc machine fait 50 minutes et il est découpé en deux moitiés symétriques : je montre, vous faites.

### Les 4 objectifs, par ordre de priorité

1. **Chaque élève a lancé un programme et l'a vu s'exécuter.** Le seul objectif qui ne se négocie pas.
2. **Chaque élève a vu une erreur rouge, et a compris que ce n'est pas grave.** On la provoque exprès.
3. **Chaque élève a écrit son écran d'accueil**, puis **son jeu pose une question et affiche la réponse.**
4. **La méthode de travail est posée** : les pistes, les cartes, le Filet. Elle servira les 20 séances suivantes.

---

## 1. Le programme de la séance

| Horaire | Séquence | Durée |
|---|---|---|
| **12 h - 12 h 15** | Prière et accueil | 15 min |
| **12 h 15 - 12 h 22** | Récupération des exercices de décollage | 7 min |
| **12 h 22 - 12 h 40** | Le quiz : ce qui est resté de samedi dernier | 18 min |
| **12 h 40 - 12 h 50** | La méthode de travail | 10 min |
| **12 h 50 - 13 h** | Pause | 10 min |
| **13 h - 13 h 50** | **Premier contact machine : `print()`, puis `input()`** | 50 min |
| **13 h 50 - 14 h** | Clôture | 10 min |

### Le détail du bloc machine (13 h - 13 h 50)

**Deux moitiés symétriques : je montre 8 minutes, vous faites 12 minutes.**

| Horaire | Quoi | Durée |
|---|---|---|
| 13 h - 13 h 07 | Allumer, ouvrir Thonny, les 3 repères, les cartes de couleur | 7 min |
| 13 h 07 - 13 h 15 | **Je montre `print()`** : la commande, l'ordre des lignes, **et l'erreur volontaire** | 8 min |
| 13 h 15 - 13 h 27 | **Vous faites** : l'écran d'accueil du jeu XO — partie 1 du fichier | 12 min |
| 13 h 27 - 13 h 35 | **Je montre la variable, puis `input()`** | 8 min |
| 13 h 35 - 13 h 47 | **Vous faites** : le jeu demande le nom du joueur — partie 2 du fichier | 12 min |
| 13 h 47 - 13 h 50 | On sauvegarde, et on distribue le Filet | 3 min |

> **Le fichier de l'élève est coupé en deux parties**, avec un panneau d'arrêt au milieu :
> *« arrête-toi ici, lève la carte verte, on attend le professeur pour la partie 2 ».*
> C'est ce qui empêche les plus rapides de partir dans `input()` avant l'explication.

### Les trois règles de temps

1. **13 h, les machines sont allumées.** Si le quiz ou la méthode débordent, on les coupe — pas le bloc machine.
2. **On ne reprend aucune théorie de la séance 1.** Le quiz la révise à lui seul : une phrase d'explication par question, pas plus.
3. **13 h 47, on arrête de coder**, même au milieu d'une ligne. On sauvegarde et on distribue le code officiel.
4. **Si la première moitié déborde**, on écourte l'atelier 1 à 10 minutes — on ne sacrifie ni l'erreur volontaire, ni `input()` : ce sont les deux raisons d'être de la séance.

---

## 2. Préparation

| Quand | Quoi |
|---|---|
| **La veille** | Refaire soi-même le live coding avec [`code/live_coding_antiseche.py`](code/live_coding_antiseche.py), à voix haute, en entier |
| **La veille** | Copier sur une clé le dossier `GEEKS` (voir ci-dessous) |
| **30 min avant** | Sur chaque poste : coller le dossier `GEEKS` sur le Bureau, et vérifier que `mon_xo/jeu.py` s'ouvre et se lance |
| **30 min avant** | Dans Thonny : **police en taille 18 minimum** (Outils → Options → Éditeur) |
| **30 min avant** | Ouvrir le quiz et le diaporama, projeter la première diapo |

### Le dossier `GEEKS`, à préparer sur la clé

```
GEEKS/
├── mon_xo/
│     jeu.py          ← une copie de code/depart_eleves_piste_bleue.py
└── xo_officiel/
      jeu.py          ← une copie de code/code_officiel_fin_de_seance.py
```

On copie ce dossier sur le Bureau de chaque poste. **`xo_officiel` reste fermé** jusqu'à 13 h 47 : c'est le Filet.

### À imprimer

| Quantité | Document | Fichier |
|---|---|---|
| 1 par poste | **Aide-mémoire machine** — les 5 gestes, `print()`, `input()`, les 4 erreurs | [`a-imprimer/1-aide-memoire-machine.pdf`](a-imprimer/1-aide-memoire-machine.pdf) |
| 1 pour vous | **Le dictionnaire des erreurs** — si ce n'est pas déjà fait | [`1-methode/annexes/dictionnaire-des-erreurs.pdf`](../../1-methode/annexes/dictionnaire-des-erreurs.pdf) |

Les cartes de signalisation, l'affiche « 3 avant moi » et le Mur de Mission sont déjà en place.

---

## 3. Le déroulé, bloc par bloc

### 3.1 · 12 h - 12 h 15 — Prière et accueil

Comme chaque samedi. **Sur les deux dernières minutes**, on annonce la séance :

> « Samedi dernier, on a beaucoup parlé, beaucoup réfléchi — et on n'a pas eu le temps d'allumer les machines.
> Aujourd'hui, on répare ça : **à 13 h, tout le monde est devant un clavier.** Et à 14 h, votre jeu vous
> demandera votre nom. »

---

### 3.2 · 12 h 15 - 12 h 22 — Récupération des exercices de décollage

1. On ramasse les feuilles. On **note qui a rendu** dans l'onglet `Suivi` du classeur.
2. On feuillette **sans corriger** : ce n'est pas noté, et on n'a pas le temps.
3. Une phrase sur ce qu'on a vu : *« J'en ai lu trois en arrivant. Il y a des choses très justes. »*

**On ne nomme pas ceux qui n'ont rien rendu.** Les exercices étaient facultatifs, et la séance ne les
suppose pas faits. C'est à dire à voix haute, une fois, pour tout le monde.

---

### 3.3 · 12 h 22 - 12 h 40 — Le quiz

Le quiz préparé pour la séance 1 et qui n'a pas eu lieu. Il révise toute la théorie du 12 septembre.

**Le support :** [`a-projeter/quiz-seance-1.pptx`](a-projeter/quiz-seance-1.pptx) — 15 questions, une diapo
par question puis la réponse. Les corrigés : [`a-projeter/quiz-questions-et-reponses.md`](a-projeter/quiz-questions-et-reponses.md).

| Réponse | Carte à lever |
|---|---|
| 1 | 🔴 Rouge |
| 2 | 🔵 Bleu |
| 3 | 🟠 Orange |
| 4 | 🟢 Vert |

On projette la question, on lit les 4 réponses à voix haute, on compte « 3, 2, 1 » — **et tout le monde lève
sa carte en même temps**. On regarde la salle d'un coup d'œil, on affiche la réponse, **une seule phrase
d'explication**, on enchaîne.

**Le minutage :** 1 min de règle du jeu · **15 questions à une minute** · 2 min de conclusion.
**En retard, on garde les 10 premières questions** — et on s'arrête à 12 h 40, quoi qu'il arrive.

> **Le piège :** commenter chaque question pendant deux minutes. Quinze questions à deux minutes, c'est une
> demi-heure — et le bloc machine est mort. **Une phrase par question. Chronomètre visible.**

**En conclusion :**

> « Personne n'a tout juste, et c'est normal : on a vu ça une seule fois. Ce qui compte, c'est que **tout est
> encore là dans votre tête**. Maintenant, on arrête de parler des ordinateurs. On va s'en servir. »

---

### 3.4 · 12 h 40 - 12 h 50 — La méthode de travail

Dix minutes, pas plus. Trois choses.

#### a) Les trois pistes (4 min)

> « À partir d'aujourd'hui, à chaque atelier, **vous choisissez votre piste**. »

| Piste | Pour qui | Ce que c'est |
|---|---|---|
| 🔵 **Bleue** | on découvre | Le fichier est déjà écrit, avec des trous à remplir. **Il marche déjà quand on le lance.** |
| 🔴 **Rouge** | on suit | On écrit soi-même, avec le modèle à l'écran |
| ⚫ **Noire** | on veut plus | La même chose, plus un défi en plus |

**Les trois pistes arrivent au même résultat.** C'est la profondeur qui change, pas le programme.
**On change de piste quand on veut, d'une séance à l'autre.** Personne n'est « de la piste bleue ».

> **Aujourd'hui, tout le monde part en piste bleue** : c'est le premier contact machine, on ne complique rien.
> Qui finit en avance prend le défi écrit en bas de son fichier.

#### b) Le Filet (4 min)

> « Voici ma promesse. **À la fin de chaque séance, je vous donne le code officiel**, celui qui marche, même
> si vous n'avez pas fini, même si vous étiez absent. Chaque samedi, tout le monde repart du même point.
> **Dans cette formation, on ne peut pas prendre du retard.** »

C'est la phrase la plus importante de la séance pour les élèves les plus fragiles. On la dit lentement.

#### c) Comment on est évalué (2 min)

> « Il n'y a **aucune note** ici, et aucun classement. Une chose est acquise quand vous savez faire trois
> choses : **ça marche · je sais l'expliquer · je sais le refaire tout seul.** C'est tout. »

---

### 3.5 · 12 h 50 - 13 h — Pause

Dix minutes. On en profite pour **allumer les machines** et vérifier que Thonny s'ouvre partout.
**À 13 h, on commence — les retardataires s'assoient sans qu'on les attende.**

---

### 3.6 · 13 h - 13 h 50 — Premier contact machine : `print()`, puis `input()`

**Deux moitiés, construites pareil : je montre 8 minutes, vous faites 12 minutes.**
L'anti-sèche complète, avec ce qu'on dit à chaque étape :
[`code/live_coding_antiseche.py`](code/live_coding_antiseche.py).

#### a) 13 h - 13 h 07 · Les trois repères de Thonny, et les cartes

On projette la fenêtre de Thonny. **Trois choses seulement** — pas de visite du logiciel :

| | |
|---|---|
| **En haut** | la zone blanche : **c'est là qu'on écrit.** |
| **En bas** | la zone grise : **c'est là que l'ordinateur répond**, et c'est là que le joueur tapera sa réponse |
| **Le bouton vert, ou F5** | **c'est « vas-y ».** Rien ne se passe tant qu'on n'appuie pas dessus |

Puis les cartes de signalisation, déjà sur les postes, en une minute :

| Carte | Ce qu'elle dit |
|---|---|
| 🟢 **Vert** | ça avance, tout va bien |
| 🟠 **Orange** | je suis bloqué — **je continue à chercher en attendant** |
| 🔴 **Rouge** | problème de machine : elle ne démarre pas, l'écran est figé |
| 🔵 **Bleu** | j'ai fini, je veux le défi en plus |

> « **Ici, on ne lève pas la main : on lève une carte.** Comme ça je vois toute la salle d'un coup d'œil, et
> vous continuez à travailler pendant que j'arrive. »

Et la règle des **3 avant moi**, affichée au mur : je relis la consigne · je demande à mon voisin · je
regarde la fiche mémo. **Ensuite** je lève l'orange.

#### b) 13 h 07 - 13 h 15 · Je montre `print()` — « je code, vous prédisez »

**On tape devant eux, lentement, dans un fichier vide.** On ne lance pas un fichier tout fait.
**Avant chaque exécution : « qu'est-ce qui va s'afficher ? À trois. »** F5 seulement après leur réponse.

1. **`print("Bonjour")`** — on épelle en verbalisant : *« p-r-i-n-t, ça veut dire **AFFICHE**. Une parenthèse
   qu'on ouvre et qu'on fermera toujours. Un guillemet, mon texte, un guillemet. »* Puis F5.
   → *« Vous venez de voir un ordinateur obéir. C'est tout le métier. **Attention au piège : ça n'imprime
   rien sur du papier.** »* Et les guillemets ne s'affichent pas : ils disent seulement *« ceci est du texte »*.
2. **Trois lignes à la suite** — `print("Un")`, `print("Deux")`, `print("Trois")`. On demande l'ordre **avant**
   de lancer. → *« De haut en bas. Ligne par ligne. Toujours. Il ne devine pas, il ne saute pas de ligne, il
   ne revient pas en arrière. Si ça s'affiche dans le désordre, ce n'est pas lui : c'est l'ordre de vos lignes. »*
3. **L'erreur volontaire** — `print("Bonjour)` : il manque un guillemet. **C'est le moment le plus important
   de la séance.**

> **Ce qu'on dit devant le message rouge** — lentement, sans dramatiser :
> « Regardez. **Rouge.** Est-ce que l'ordinateur est cassé ? Non. Est-ce que je suis puni ? Non.
> **Il m'explique ce qu'il n'a pas compris.** Il dit `SyntaxError` : j'ai mal écrit quelque chose.
> Il me montre même la ligne. Le rouge n'est pas une punition, **le rouge est une information.**
> Aujourd'hui, celui qui voit du rouge lève le pouce : il a trouvé quelque chose. »

On corrige devant eux, on relance, ça marche. **On laisse ça affiché.**

#### c) 13 h 15 - 13 h 27 · Vous faites : l'écran d'accueil du jeu XO

Le fichier est déjà sur chaque poste : `GEEKS/mon_xo/jeu.py`
(c'est [`code/depart_eleves_piste_bleue.py`](code/depart_eleves_piste_bleue.py)).

> « Ouvrez `GEEKS`, puis `mon_xo`, puis `jeu.py`. **Appuyez tout de suite sur F5 : il marche déjà.**
> Ensuite, **la partie 1 seulement** — étapes 1 à 5. Vous remplacez chaque `____`. Et vous relancez
> après chaque changement. Quand ça marche, **carte verte, et vous m'attendez.** »

**Le panneau d'arrêt est écrit dans leur fichier**, au milieu : *« arrête-toi ici, lève la carte verte, on
attend le professeur pour la partie 2 »*. Les rapides ne partent donc pas seuls dans `input()`.

**Ce que l'enseignant fait :** il circule, il ne s'assoit pas, **il ne touche jamais le clavier d'un élève**.
Devant une erreur, on ne corrige pas : **on lit le message rouge avec l'élève** et on demande
*« qu'est-ce qu'il te dit ? »*.

**À 13 h 27, tout le monde doit avoir vu son écran d'accueil s'afficher, avec son prénom dessus.**

#### d) 13 h 27 - 13 h 35 · Je montre la variable, puis `input()`

Tout le monde lâche le clavier. **Écrans face à nous, mains sur la table.**

**1. La variable, d'abord sans machine** — avec les mains :

> « J'ai une boîte. Je colle une étiquette dessus : `nom`. Je mets quelque chose dedans : *Damien*.
> Quand je dis `nom`, l'ordinateur va regarder **dans la boîte**. »

Puis à l'écran, deux lignes, avec la question qui fait tout comprendre :

```python
nom = "Damien"
print(nom)
```

> **Avant de lancer : « qu'est-ce qui va s'afficher ? `nom`, ou `Damien` ? »**
> Laissez-les se tromper : c'est comme ça qu'ils comprennent.

Puis `print("nom")` juste après, pour montrer la différence :
**avec guillemets, il affiche le mot ; sans guillemets, il affiche ce qu'il y a dans la boîte.**
C'est l'erreur numéro un de toute l'année — on le dit dès aujourd'hui.

**2. `input()` : c'est le joueur qui remplit la boîte**

```python
nom = input("Comment t'appelles-tu ? ")
print("Bonjour " + nom + " !")
```

On lance, et **on tape le prénom d'un élève de la classe**. Effet garanti.

> « Le programme s'est arrêté, et il m'attend. C'est ça, `input` : il pose la question, il attend, et il
> **range la réponse dans la boîte**. Le `+` colle les morceaux bout à bout — attention à l'espace après
> *Bonjour*, sinon ça colle tout. »

Montrez l'oubli de l'espace une fois : `BonjourDamien`. Ils rient, ils retiennent.

#### e) 13 h 35 - 13 h 47 · Vous faites : le jeu demande le nom du joueur

> « **Partie 2** de votre fichier, étapes 6, 7 et 8. Votre jeu doit poser une question, attendre, et répondre
> avec le nom du joueur. **Relancez après chaque changement.** »

**Les erreurs qui vont arriver :**

| Ce qui s'affiche | Ce qui s'est passé | Ce qu'on dit |
|---|---|---|
| `SyntaxError` | un guillemet ou une parenthèse manque | « Compte tes guillemets : ils vont par deux, comme des chaussures » |
| `NameError` | du texte sans guillemets, ou `Nom` écrit au lieu de `nom` | « L'ordinateur cherche une boîte qui n'existe pas. Regarde comment tu l'as appelée » |
| `BonjourDamien` collé | l'espace manque dans `"Bonjour "` | « Il colle exactement ce que tu lui donnes. Ajoute l'espace avant le guillemet » |
| Rien ne se passe | il a écrit dans la zone grise du bas | « Remonte dans la zone blanche : c'est là qu'on écrit » |

**Pour ceux qui finissent avant** (carte bleue) : *« demande aussi son âge au joueur, et affiche-le »* —
le défi est écrit en bas de leur fichier.

#### f) 13 h 47 - 13 h 50 · On sauvegarde, et le Filet

1. **`Ctrl + S`**, tous ensemble, au signal. On vérifie que l'étoile a disparu du titre.
2. On ouvre `GEEKS/xo_officiel/` devant eux : *« voilà le code officiel de la séance. Il est déjà sur votre poste. Celui qui n'a pas fini, celui qui n'était pas là : tout le monde repart avec. »*

---

### 3.7 · 13 h 50 - 14 h — Clôture

Dix minutes, trois temps :

1. **Le Mur de Mission** (4 min) — la classe avance d'une case. **Tout le monde vient**, l'affiche est au mur.
2. **La question à la classe** (4 min) — *« qu'est-ce que vous avez compris aujourd'hui, et de quoi n'êtes-vous
   pas encore sûrs ? »* On écoute, on ne corrige pas. **On note le soir même dans l'onglet `Journal`** : ce qui
   revient le plus ouvre la séance 3.
3. **La dernière phrase** (2 min) :

> « Aujourd'hui, votre jeu a appris à parler, **et à écouter**. Samedi prochain, **il parlera aux deux
> joueurs** — il demandera leurs deux noms, et il saura qui joue les X et qui joue les O.
> À samedi, les Geeks ! »

---

## 4. Les plans de secours

| Ce qui arrive | Ce qu'on fait |
|---|---|
| **Le vidéoprojecteur ne marche pas** | Le quiz se lit à voix haute, les cartes de couleur suffisent. Le live coding se fait sur l'écran d'un poste, les élèves debout autour |
| **Une machine ne démarre pas** | L'élève rejoint le poste d'un voisin : à deux sur une machine, on travaille très bien. On note le poste dans le classeur |
| **Il n'y a pas assez de machines** | Deux élèves par poste, **10 minutes chacun**, chronomètre visible. Celui qui ne tape pas lit la consigne à voix haute |
| **Le bloc machine commence à 13 h 15** (retard accumulé) | On écourte les deux ateliers à 10 minutes. **On ne coupe ni l'erreur volontaire, ni `input()`** : ce sont les deux raisons d'être de la séance |
| **Un élève finit en 5 minutes** | Carte bleue → le défi de l'âge. Puis il devient **Geek Mentor** : il aide deux voisins, sans toucher à leur clavier |
| **Un élève bloque et se décourage** | On s'assoit à côté, on lui fait relancer le fichier **tel quel** pour qu'il voie que ça marche, puis **une seule** modification : son prénom. C'est suffisant pour aujourd'hui |
| **Un nouvel élève arrive aujourd'hui** | Il prend le fichier de départ comme tout le monde : la séance 2 ne suppose rien de la séance 1. On lui donne la fiche mémo de la séance 1 en partant |
| **Un enseignant est absent** | Les deux classes fusionnent dans la même salle, même déroulé, deux élèves par poste |

---

## 5. Après la séance, le soir même

1. **Le classeur** ([`3-suivi/`](../../3-suivi/LISEZ-MOI.md)) : présence `S02`, la production de chacun dans `Suivi`, les exercices rendus.
2. **L'onglet `Journal`** : ce qui est ressorti de la clôture, ce qui a débordé, qui décroche.
3. **L'onglet `Indiscipline`**, s'il s'est passé quelque chose. À chaud, pas trois jours après.
4. **Le [dictionnaire des erreurs](../../1-methode/annexes/A6-dictionnaire-des-erreurs.md)** : on coche les erreurs traitées aujourd'hui.

---

## 6. Ce que la séance 2 laisse pour la séance 3

| | |
|---|---|
| **Brique suivante** | Le jeu demande le nom **des deux joueurs**, et attribue les X et les O |
| **Point de départ** | [`code/code_officiel_fin_de_seance.py`](code/code_officiel_fin_de_seance.py), distribué aujourd'hui à tout le monde |
| **Ce qui est déjà en place** | Les pistes, les cartes, le Filet — on ne les réexplique plus |
