# 📅 Les séances

Une séance = un dossier. Tout ce qui la concerne est dedans, et rien d'autre.

| Séance | Brique ajoutée au jeu | Notion |
|---|---|---|
| **[S01 — Le Décollage](S01-decollage/fiche-de-seance.md)** · samedi 12 septembre 2026, 12 h - 14 h | L'écran d'accueil du jeu XO | Pourquoi et comment on code · l'algorithme · `print()` |
| S02 à S22 | *à venir* | |

---

## Comment est rangée une séance

```
S01-decollage/
├── fiche-de-seance.md     LA RÉFÉRENCE : déroulé minute par minute, scripts,
│                          erreurs anticipées, plans de secours
├── a-imprimer/            les PDF prêts à imprimer + les quantités
│                          (dont MON-SCRIPT d'animation, à agrafer)
├── code/                  depart_eleves_piste_bleue.py   le fichier de l'élève
│                          code_officiel_fin_de_seance.py le Filet
│                          live_coding_antiseche.py       pour répéter avant
└── sources/               les .html modifiables des documents imprimés
```

## L'ordre dans lequel s'en servir

1. **La semaine d'avant** — lire `fiche-de-seance.md` en entier, à deux.
2. **J-7** — préparer les machines : voir [`4-outils/LISEZ-MOI.md`](../4-outils/LISEZ-MOI.md).
3. **J-1** — imprimer `a-imprimer/`, en suivant `quantites-et-formats.md`.
4. **J-7 aussi** — créer le Kahoot depuis `kahoot/import-kahoot.xlsx`, et le tester une fois en solo.
5. **Le jour J** — animer avec `00-MON-SCRIPT-animation.pdf` à la main.
6. **Le soir** — remplir le [classeur de suivi](../3-suivi/LISEZ-MOI.md) et répondre aux 3 questions de la revue.

## Pour modifier un document imprimé

On corrige le `.html` dans `sources/`, puis on refabrique le PDF :

```
python 4-outils/faire_les_pdf.py --seance 1
```

Sans Chrome sur la machine : ouvrir le `.html` dans le navigateur, `Ctrl+P`,
« Enregistrer au format PDF », et le ranger dans `a-imprimer/` sous le même nom.
