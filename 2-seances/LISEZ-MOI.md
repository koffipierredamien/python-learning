# 📅 Les séances

Une séance = un dossier. Tout ce qui la concerne est dedans, et rien d'autre.

| Séance | Brique ajoutée au jeu | Notion |
|---|---|---|
| **[S01 — Le Décollage](S01-decollage/compte-rendu.md)** · samedi 12 septembre 2026 | *(faite)* La théorie et les missions de décollage | Pourquoi et comment on code · l'algorithme |
| **[S02 — Premier contact machine](S02-premier-contact/fiche-de-seance.md)** · samedi 19 septembre 2026 | L'écran d'accueil, **et le jeu demande ton nom** | `print()` · la variable · `input()` · lire une erreur |
| **[S03 — TP n°1 : les deux joueurs](S03-tp-les-joueurs/a-imprimer/quantites-et-formats.md)** · samedi 26 septembre 2026 | Le jeu demande le nom des **deux** joueurs et attribue X et O | TP de 2 h, en autonomie · quiz flash de rappel · `print`, variables, `input` |
| S04 à S22 | *à venir* | |

> **La séance 1 s'est arrêtée après les missions de décollage.** Le premier contact machine, le Kahoot,
> la clôture et la méthode de travail n'ont pas eu lieu : ils sont repris dans la séance 2, et le reste
> du parcours décale d'une séance.

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
│
└── code/                  ce qui tourne sur les machines
      depart_eleves_piste_bleue.py   le fichier de l'élève
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
