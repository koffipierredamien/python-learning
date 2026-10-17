# 📅 Les séances

Une séance = un dossier. Tout ce qui la concerne est dedans, et rien d'autre.

| Séance | Brique ajoutée au jeu | Notion |
|---|---|---|
| **[S01 — Le Décollage](S01-decollage/compte-rendu.md)** · samedi 12 septembre 2026 | *(faite)* La théorie et les missions de décollage | Pourquoi et comment on code · l'algorithme |
| **[S02 — Premier contact machine](S02-premier-contact/fiche-de-seance.md)** · samedi 19 septembre 2026 | L'écran d'accueil, **et le jeu demande ton nom** | `print()` · la variable · `input()` · lire une erreur |
| **[S03 — TP n°1 : les deux joueurs](S03-tp-les-joueurs/a-imprimer/quantites-et-formats.md)** · samedi 26 septembre 2026 | Le jeu demande le nom des **deux** joueurs et attribue X et O | TP de 2 h, en autonomie · quiz flash de rappel · `print`, variables, `input` — [corrigé en Python](S03-tp-les-joueurs/code/LISEZ-MOI.md) |
| **[S04 — Le jeu vérifie et compte](S04-le-jeu-compte/fiche-de-seance.md)** · samedi 3 octobre 2026 | Le plateau **numéroté**, la case demandée, le **compteur**, et la case qui n'existe pas **refusée** | `int()` · `str()` · `tour = tour + 1` · **les opérateurs** `+ - * /` et `> < >= <= == !=` · **`if` / `else`** |
| **[S05 — Le jeu compte et décide](S05-la-decision/fiche-de-seance.md)** · samedi 10 octobre 2026 | **Le Grand Parcours** (révision des 4 séances, 8 paliers), le compteur de tours, et la case qui n'existe pas **refusée** | `tour = tour + 1` · **les opérateurs** `> < >= <= == !=` · **`if` / `else`** |
| **[S06 — Le plateau se souvient](S06-le-plateau-se-souvient/fiche-de-seance.md)** · samedi 17 octobre 2026 | Le symbole **reste** sur le plateau | **la liste** · l'indice · `plateau[case - 1]` |
| **[S07 — On ne joue pas deux fois au même endroit](S07-la-case-occupee/fiche-de-seance.md)** · samedi 24 octobre 2026 | Le jeu **refuse** une case déjà prise | **le `if` dans le `if`** · `== str(case)` |
| **[S08 — TP n°2 : le plateau vivant](S08-tp-le-plateau/fiche-de-seance.md)** · samedi 31 octobre 2026 | Quatre coups d'affilée, sans bug | TP de 2 h, en autonomie — [corrigé](S08-tp-le-plateau/code/corrige-tp2.py) |
| **[S09 — Une seule question au lieu de trois](S09-et-ou/fiche-de-seance.md)** · samedi 7 novembre 2026 | Le même jeu, avec une décision **deux fois plus courte**, et le bug du zéro vraiment réparé | **`and`** et **`or`** |
| **[S10 — Le jeu tourne tout seul](S10-la-boucle/fiche-de-seance.md)** · samedi 14 novembre 2026 | **Neuf tours**, et les joueurs alternent | **la boucle `while`** |
| **[S11 — Le jeu sait qui gagne](S11-le-gagnant/fiche-de-seance.md)** · samedi 21 novembre 2026 | **Une vraie partie, avec un vainqueur** | les 8 lignes gagnantes · `while tour < 9 and gagnant == ""` |
| **[S12 — TP n°3 : le tournoi](S12-tp-le-tournoi/fiche-de-seance.md)** · samedi 28 novembre 2026 | **Le jeu XO, fini et jouable** | finitions, tests, et **tournoi de classe** |
| S13 à S22 | *à venir* | |

> 📌 **[L'affiche du trimestre](a-afficher/LISEZ-MOI.md)** — une page A4 à imprimer **avant le
> 17 octobre** et à laisser au mur jusqu'au 28 novembre : les sept samedis, une case à cocher
> chaque semaine. Avec le message d'annonce aux familles.

> 🗺️ **[Le parcours d'octobre et novembre](PLAN-OCTOBRE-NOVEMBRE.md)** — la carte des sept séances
> ci-dessus : pourquoi cet ordre, le calendrier semaine par semaine, le tableau de bord de tous les
> fichiers, et la routine des quatre gestes. **C'est par là qu'il faut commencer.**

> **La séance 4 n'a traité que sa première notion** (texte ou nombre). Le compteur et la décision
> passent à la séance 5, qui réutilise **tout** le matériel de la séance 4 : diaporama, aide-mémoire,
> anti-sèche et fichiers de code. Seul le quiz flash est neuf.

> **La séance 1 s'est arrêtée après les missions de décollage.** Le premier contact machine, le Kahoot,
> la clôture et la méthode de travail ont été repris dans la séance 2. Le samedi ainsi perdu est
> **récupéré à partir de la séance 4**, qui porte trois notions au lieu de deux : la phase 1 du parcours
> passe de quatre séances à trois.

---

## Comment est rangée une séance

Quatre dossiers, nommés par ce qu'on en fait.

```
S02-premier-contact/
│
├── fiche-de-seance.md     LA RÉFÉRENCE : déroulé minute par minute, scripts,
│                          erreurs anticipées, plans de secours
│
├── a-projeter/            ce qui passe au vidéoprojecteur
│     seance-2-projection.pptx      le diaporama de la séance (28 diapos)
│     quiz-seance-1.pptx            le quiz (32 diapos), joué en séance 2
│     quiz-questions-et-reponses.md les 15 questions, réponses et explications
│     kahoot-en-ligne/              si vous préférez le vrai Kahoot
│
├── a-imprimer/            ce qui part à l'imprimante
│     les PDF + quantites-et-formats.md
│     sources/                      les .html, à ne rouvrir que pour corriger un texte
│
├── a-envoyer/             ce qui part par mail ou par message
│     deroule-seance-2.docx         le déroulé pour les responsables
│     formulaire-de-revision.gs     fabrique le formulaire Google noté, en un clic
│     formulaire-de-revision.md     le mode d'emploi, le message aux parents, les réponses
│     (séances 3 et 4 : formulaire-exercices.gs — le test noté avec du code à écrire)
│     (à partir de la séance 5 : quiz-semaine.gs + quiz-semaine.md — 15 QCM
│      corrigés à 100 % automatiquement, pour ceux qui n'ont pas d'ordinateur ;
│      et exercice-maison.md + les images, le PDF et le corrigé, pour les autres)
│     deroule-seance-N.docx / .pdf      le déroulé pour le responsable :
│                                       pas de code, pas de jargon, il se
│                                       transfère tel quel
│
└── code/                  ce qui tourne sur les machines
      depart_eleves.py   le fichier de l'élève
      code_officiel_fin_de_seance.py le Filet
      live_coding_antiseche.py       pour répéter avant
```

## L'ordre dans lequel s'en servir

1. **La semaine d'avant** — lire `fiche-de-seance.md` en entier, à deux.
2. **J-7** — préparer la clé et les postes : voir la fiche de séance, § Préparation.
3. **J-1** — imprimer `a-imprimer/`, en suivant `quantites-et-formats.md`.
4. **J-7 aussi** — ouvrir les diaporamas de `a-projeter/` et les faire défiler une fois.
5. **Le jour J** — animer avec la fiche de séance à la main.
6. **Le soir** — remplir le [classeur de suivi](../3-suivi/LISEZ-MOI.md) et répondre aux 3 questions de la revue.
7. **Dans la semaine qui suit** — envoyer le formulaire Google aux parents, et noter ce qui revient
   dans l'onglet `Révisions maison` du classeur.

## Pour modifier un document imprimé

On ouvre le `.html` correspondant dans `a-imprimer/sources/`, on corrige le texte, puis
**`Ctrl + P` → « Enregistrer au format PDF »**, en remplaçant le PDF du même nom dans `a-imprimer/`.
