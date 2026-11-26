# 🔧 Les générateurs

**Vous n'avez normalement pas besoin d'ouvrir ce dossier.** Tout ce qu'il fabrique est déjà fabriqué,
rangé dans les dossiers des séances. Il est ici pour une seule raison : **le jour où vous voudrez
corriger une faute de frappe dans un quiz, rallonger un aide-mémoire ou décaler une date**, il vaut
mieux changer une ligne et relancer que refaire la mise en page à la main.

## Ce que chaque script fabrique

| Script | Ce qu'il écrit | Où |
|---|---|---|
| `aide_memoires.py` | les aide-mémoires 1 page | `S06/S07/S09/S11 · a-imprimer/` |
| `quiz_rappel.js` + `donnees_quiz_rappel.js` | les **quiz flash d'ouverture** (14 diapos : 1 question par diapo) | `S06/S07/S09 · a-projeter/` |
| `decks.js` + `donnees_decks.js` | les diaporamas de séance *(ancien format : « je montre / vous faites »)* | `S06/S07/S09 · a-projeter/` |
| `decks_tp.js` | les diaporamas de TP | `S08 · a-projeter/` |
| `quiz_hebdo.py` + `quiz_5_6.py`, `quiz_7_8.py`, `quiz_9_10.py` | les quiz de la semaine (`.gs`), 15 QCM chacun | `S06/S07/S09 · a-envoyer/` |
| `quiz_revision.py` | la **révision générale en formulaire** (20 questions) | `S10-revision-generale · a-envoyer/` |
| `exos_maison.py` + `donnees_exos.py` + `build_exos.py` | les exercices : feuille élève et corrigé, en **HTML → PDF → images** | `S06/S09/S11 · a-envoyer/` |
| `notices.py` | les `quiz-semaine.md` (réglages, message aux parents) | `*/a-envoyer/` |
| `quantites.py` | les `quantites-et-formats.md` des séances de cours | `*/a-imprimer/` |
| `deroules.py` + `deroules_donnees.py` | les **déroulés pour le responsable** (Word) | `S06…S11 · a-envoyer/` |
| `programme_responsable.py` | le **programme des deux mois** (Word) — écrit avant le réordonnancement du 20 novembre | `3-suivi/points-au-responsable/` |
| `affiche.py` | **l'affiche du trimestre** : HTML → PDF → image | `2-seances/a-afficher/` |
| `mission_ascenseur.py` | la **mission autonome n°1** : feuille élève et feuille enseignant | `2-seances/missions-autonomes/` |
| `revision_generale.js` + `donnees_revision_generale.js` | la **révision générale** du 14 novembre : cartes **et** ateliers au clavier | `S10-revision-generale/a-projeter/` |
| `quiz_rappel_general.py` | le **quiz de rappel** (20 questions) : tout le parcours jusqu'à l'ordre des conditions, **sans la boucle** | `S11-les-trois-chemins · a-envoyer/` |
| `exercice_la_medaille.py` | l'exercice **La Médaille** : HTML → PDF → images, sans date ni cadre à remplir — il se lit sur un téléphone | `S11-les-trois-chemins · a-envoyer/` |
| `cours_en_quiz.js` + `donnees_cours_s11.js` | **le cours en quiz** de la séance 11 : 46 diapos, de la prière à la clôture — révision, leçons, ateliers au clavier, ⭐ et exercices | `S11-les-trois-chemins/a-projeter/` |
| `cours_en_quiz.js` + `donnees_cours_s12.js` | **le cours en quiz** de la séance 12 : 38 diapos — la reprise, bâtie sur le travail fait à la maison | `S12-le-jeu-dit-pourquoi/a-projeter/` |

> `S08` (le TP) a des documents écrits à la main, pas générés :
> ses `.html` sont dans `a-imprimer/sources/`.

### ⚠️ Les séances retirées du parcours

Le 20 novembre, les séances préparées pour **la boucle, le gagnant et le tournoi** ont été retirées
du parcours actif : elles annonçaient des dates fausses et un ordre qui ne tient plus
(voir [le plan](../PLAN.md), § 2).

**Leurs données sont restées ici** — dans `donnees_decks.js`, `donnees_quiz_rappel.js`,
`quiz_7_8.py`, `quiz_9_10.py`, `donnees_exos.py`, `deroules_donnees.py`, `aide_memoires.py`,
`quantites.py`, `notices.py`. Rien n'est perdu : le jour où la boucle reprendra sa place, on recrée
le dossier de la séance et on relance le générateur.

**En attendant, chaque générateur vérifie que le dossier existe avant d'écrire** et affiche
`IGNORE (seance retiree du parcours)` sinon. C'est volontaire : **relancer un générateur ne peut
pas ressusciter une séance retirée.** Les fichiers eux-mêmes sont dans l'historique Git, au commit
`65667c2`.

## Comment les relancer

```bash
cd 2-seances/generateurs

python3.13 -I quiz_5_6.py          # les quiz : chacun est revérifié en sortant
python3.13 -I quiz_7_8.py
python3.13 -I quiz_9_10.py
python3.13 -I quiz_revision.py    # la révision générale en formulaire
python3.13 -I quiz_rappel_general.py   # le quiz de rappel (20 questions)
python3.13 -I exercice_la_medaille.py  # l'exercice La Médaille : PDF + images
python3.13 -I aide_memoires.py     # affiche le taux de remplissage de chaque page
python3.13 -I build_exos.py        # exercices de maison : PDF + images
python3.13 -I notices.py
python3.13 -I quantites.py

NODE_PATH=/chemin/vers/node_modules node donnees_quiz_rappel.js  # les 5 quiz flash
NODE_PATH=/chemin/vers/node_modules node donnees_revision_generale.js  # la révision générale
NODE_PATH=/chemin/vers/node_modules node donnees_cours_s11.js   # le cours en quiz de la séance 11
NODE_PATH=/chemin/vers/node_modules node donnees_cours_s12.js   # le cours en quiz de la séance 12
NODE_PATH=/chemin/vers/node_modules node donnees_decks.js   # les 5 diaporamas
NODE_PATH=/chemin/vers/node_modules node decks_tp.js        # les 2 diaporamas de TP

python3.13 -I deroules.py              # les 7 déroulés (Word)
python3.13 -I programme_responsable.py # le programme des deux mois (Word)
python3.13 -I affiche.py               # l'affiche du trimestre
python3.13 -I mission_ascenseur.py     # la mission autonome n°1

# les .docx se convertissent en PDF avec :
libreoffice --headless --convert-to pdf --outdir <dossier> <fichier>.docx
```

> Le **dictionnaire des erreurs** a son propre générateur, rangé avec lui :
> [`1-methode/annexes/sources/dictionnaire.py`](../../1-methode/annexes/sources/dictionnaire.py).
> Il reconstruit le tableau imprimable **à partir de l'annexe A6**, pour que les deux ne divergent
> jamais : on corrige le `.md`, on relance, et le PDF suit.

**Il faut :** `python3` avec **python-docx** (`pip install python-docx`), **Chromium** (le chemin est
en haut de `exos_maison.py` et `aide_memoires.py`), **poppler-utils** (`pdfinfo`, `pdftoppm`,
`pdftotext` — pour compter les pages, fabriquer les images et mesurer le remplissage),
**LibreOffice** pour les PDF des déroulés, et **Node** avec
**[pptxgenjs](https://gitbrent.github.io/PptxGenJS/)** (`npm install pptxgenjs`).

## La règle qu'on ne contourne pas

**Chaque quiz est rejoué contre un faux `FormApp`** avant d'être écrit
([`verifier-formulaire.js`](../S05-la-decision/a-envoyer/sources/verifier-formulaire.js)) : il compte
les questions, vérifie qu'il y a **exactement une bonne réponse par question**, qu'aucune explication
n'est vide, et que **la bonne réponse ne tombe jamais deux fois de suite au même endroit**.
Si une anomalie apparaît dans la sortie, **le quiz ne part pas**.

**Et chaque corrigé en `.py` est exécuté**, sur tous ses chemins, avant d'être publié.

**Les six questions du quiz flash n'existent qu'à un seul endroit** :
`donnees_quiz_rappel.js`. Le diaporama de la séance en reprend le résumé par
`QF(numéro)` — il ne les recopie pas. Corriger une question, c'est donc la corriger partout.
*(Il reste une troisième copie, à la main : le tableau du § 3 de la fiche de séance. Si vous
changez une question, changez-la là aussi.)*
