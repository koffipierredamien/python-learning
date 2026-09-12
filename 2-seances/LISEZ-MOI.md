# 📅 Les séances

Une séance = un dossier. Tout ce qui la concerne est dedans, et rien d'autre.

| Séance | Brique ajoutée au jeu | Notion |
|---|---|---|
| **[S01 — Le Décollage](S01-decollage/fiche-de-seance.md)** · samedi 12 septembre 2026, 12 h - 14 h | L'écran d'accueil du jeu XO | Pourquoi et comment on code · l'algorithme · `print()` |
| S02 à S22 | *à venir* | |

---

## Comment est rangée une séance

Quatre dossiers, nommés par ce qu'on en fait.

```
S01-decollage/
│
├── fiche-de-seance.md     LA RÉFÉRENCE : déroulé minute par minute, scripts,
│                          erreurs anticipées, plans de secours
│
├── a-projeter/            ce qui passe au vidéoprojecteur
│     seance-1-projection.pptx      le diaporama de la séance (46 diapos)
│     quiz-seance-1.pptx            le quiz final (32 diapos)
│     quiz-questions-et-reponses.md les 15 questions, réponses et explications
│     prompt-pour-gemini.md         pour refaire le diaporama avec Gemini
│     kahoot-en-ligne/              si vous préférez le vrai Kahoot
│
├── a-imprimer/            ce qui part à l'imprimante
│     les 14 PDF + quantites-et-formats.md
│     sources/                      les .html, à ne rouvrir que pour corriger un texte
│
├── a-envoyer/             ce qui part par mail
│     deroule-seance-1.docx         le déroulé pour les responsables
│
└── code/                  ce qui tourne sur les machines
      depart_eleves_piste_bleue.py   le fichier de l'élève
      code_officiel_fin_de_seance.py le Filet
      live_coding_antiseche.py       pour répéter avant
```

## L'ordre dans lequel s'en servir

1. **La semaine d'avant** — lire `fiche-de-seance.md` en entier, à deux.
2. **J-7** — préparer les machines : voir [`4-outils/LISEZ-MOI.md`](../4-outils/LISEZ-MOI.md).
3. **J-1** — imprimer `a-imprimer/`, en suivant `quantites-et-formats.md`.
4. **J-7 aussi** — ouvrir les deux diaporamas de `a-projeter/` et les faire défiler une fois.
5. **Le jour J** — animer avec `00-MON-SCRIPT-animation.pdf` à la main.
6. **Le soir** — remplir le [classeur de suivi](../3-suivi/LISEZ-MOI.md) et répondre aux 3 questions de la revue.

## Pour modifier un document imprimé

On corrige le `.html` dans `a-imprimer/sources/`, puis on refabrique le PDF :

```
python 4-outils/faire_les_pdf.py --seance 1
```

La règle : les `.html` de `a-imprimer/sources/` produisent un PDF dans `a-imprimer/` ; tous les autres
produisent leur PDF **à côté d'eux**.

Sans Chrome sur la machine : ouvrir le `.html` dans le navigateur, `Ctrl+P`, « Enregistrer au format PDF »,
et le ranger au bon endroit sous le même nom.
