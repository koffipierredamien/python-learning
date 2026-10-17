# 🔧 Les générateurs

**Vous n'avez normalement pas besoin d'ouvrir ce dossier.** Tout ce qu'il fabrique est déjà fabriqué,
rangé dans les dossiers des séances. Il est ici pour une seule raison : **le jour où vous voudrez
corriger une faute de frappe dans un quiz, rallonger un aide-mémoire ou décaler une date**, il vaut
mieux changer une ligne et relancer que refaire la mise en page à la main.

## Ce que chaque script fabrique

| Script | Ce qu'il écrit | Où |
|---|---|---|
| `aide_memoires.py` | les 5 aide-mémoires 1 page | `S06/S07/S09/S10/S11 · a-imprimer/` |
| `decks.js` + `donnees_decks.js` | les 5 diaporamas de séance | `S06/S07/S09/S10/S11 · a-projeter/` |
| `decks_tp.js` | les 2 diaporamas de TP | `S08/S12 · a-projeter/` |
| `quiz_hebdo.py` + `quiz_5_6.py`, `quiz_7_8.py`, `quiz_9_10.py` | les 6 quiz de la semaine (`.gs`) | `S06/S07/S09/S10/S11/S12 · a-envoyer/` |
| `exos_maison.py` + `donnees_exos.py` + `build_exos.py` | les 3 exercices de maison : feuille élève et corrigé, en **HTML → PDF → images** | `S06/S09/S10 · a-envoyer/` |
| `notices.py` | les 6 `quiz-semaine.md` (réglages, message aux parents) | `*/a-envoyer/` |
| `quantites.py` | les 5 `quantites-et-formats.md` des séances de cours | `*/a-imprimer/` |
| `deroules.py` + `deroules_donnees.py` | les 7 **déroulés pour le responsable** (Word) | `S06…S12 · a-envoyer/` |
| `programme_responsable.py` | le **programme des deux mois** (Word) | `3-suivi/points-au-responsable/` |
| `affiche.py` | **l'affiche du trimestre** : HTML → PDF → image | `2-seances/a-afficher/` |

> `S08` et `S12` (les deux TP) ont des documents écrits à la main, pas générés :
> leurs `.html` sont dans `a-imprimer/sources/`.

## Comment les relancer

```bash
cd 2-seances/generateurs

python3.13 -I quiz_5_6.py          # les quiz : chacun est revérifié en sortant
python3.13 -I quiz_7_8.py
python3.13 -I quiz_9_10.py
python3.13 -I aide_memoires.py     # affiche le taux de remplissage de chaque page
python3.13 -I build_exos.py        # exercices de maison : PDF + images
python3.13 -I notices.py
python3.13 -I quantites.py

NODE_PATH=/chemin/vers/node_modules node donnees_decks.js   # les 5 diaporamas
NODE_PATH=/chemin/vers/node_modules node decks_tp.js        # les 2 diaporamas de TP

python3.13 -I deroules.py              # les 7 déroulés (Word)
python3.13 -I programme_responsable.py # le programme des deux mois (Word)
python3.13 -I affiche.py               # l'affiche du trimestre

# les .docx se convertissent en PDF avec :
libreoffice --headless --convert-to pdf --outdir <dossier> <fichier>.docx
```

> Le **dictionnaire des erreurs** a son propre générateur, rangé avec lui :
> [`1-methode/annexes/sources/dictionnaire.py`](../../1-methode/annexes/sources/dictionnaire.py).
> Il reconstruit le tableau imprimable **à partir de l'annexe A6**, pour que les deux ne divergent
> jamais : on corrige le `.md`, on relance, et le PDF suit.

**Il faut :** `python3.13` avec **PyMuPDF** (`pip install pymupdf`) et **python-docx**
(`pip install python-docx`), **Chromium** (le chemin est en haut de `exos_maison.py` et
`aide_memoires.py`), **LibreOffice** pour les PDF des déroulés, et **Node** avec
**[pptxgenjs](https://gitbrent.github.io/PptxGenJS/)** (`npm install pptxgenjs`).

## La règle qu'on ne contourne pas

**Chaque quiz est rejoué contre un faux `FormApp`** avant d'être écrit
([`verifier-formulaire.js`](../S05-la-decision/a-envoyer/sources/verifier-formulaire.js)) : il compte
les questions, vérifie qu'il y a **exactement une bonne réponse par question**, qu'aucune explication
n'est vide, et que **la bonne réponse ne tombe jamais deux fois de suite au même endroit**.
Si une anomalie apparaît dans la sortie, **le quiz ne part pas**.

**Et chaque corrigé en `.py` est exécuté**, sur tous ses chemins, avant d'être publié.
