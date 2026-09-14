# 🔧 Outils

Sept programmes Python. Vous les lancez depuis Thonny (`F5`) ou en ligne de commande.
Aucun n'est destiné aux élèves.

| Programme | Quand s'en servir |
|---|---|
| [`jeu_xo_complet.py`](jeu_xo_complet.py) | **Le jeu XO terminé.** C'est la démonstration d'ouverture de la séance 1 (le « WOW »), et le point d'arrivée du parcours. 2 joueurs, ou contre un ordinateur imbattable. |
| [`verifier_un_poste.py`](verifier_un_poste.py) | **À lancer sur chaque machine avant la séance.** Vérifie Python, la logique du jeu, et que la fenêtre graphique pourra s'ouvrir. Tout doit afficher `[OK]`. |
| [`installer_dossier_geeks.py`](installer_dossier_geeks.py) | **À lancer sur chaque poste de la salle** (et sur votre machine). Crée le dossier `GEEKS` sur le Bureau, avec le fichier de départ de l'élève. |
| [`preparer_cle_usb.py`](preparer_cle_usb.py) | Fabrique le dossier `cle-usb/` à emporter le samedi. |
| [`faire_les_pdf.py`](faire_les_pdf.py) | Refabrique les PDF d'une séance — ou du règlement — à partir des sources `.html`. |
| [`faire_le_reglement.py`](faire_le_reglement.py) | Réécrit le **règlement intérieur** dans ses deux versions, Word et source du PDF, à partir d'un texte unique. |
| [`faire_les_revisions.py`](faire_les_revisions.py) | Écrit les **deux envois de révision de la semaine** — le quiz, le défi, et le texte des messages aux parents. |

---

## Préparer la salle, dans l'ordre

```
1.  python 4-outils/verifier_un_poste.py          sur votre machine
2.  python 4-outils/jeu_xo_complet.py             la démo s'ouvre-t-elle ?
3.  python 4-outils/preparer_cle_usb.py           fabrique cle-usb/
4.  copier tout le contenu de cle-usb/ sur la vraie clé
5.  sur CHAQUE poste : lancer installer_dossier_geeks.py depuis la clé
6.  sur CHAQUE poste : lancer 1-DEMO/verifier_un_poste.py depuis la clé
```

---

## Le dossier `GEEKS`, sur les postes et sur votre machine

`installer_dossier_geeks.py` crée exactement ceci sur le Bureau :

```
Bureau/
└── GEEKS/
     ├── mon_xo/          ← l'élève code ici
     │     jeu.py             son fichier de travail, déjà prêt
     ├── xo_officiel/     ← LE FILET : le code de référence
     └── LISEZ-MOI.txt
```

> **Il ne détruit jamais le travail d'un élève.** Relancé sur un poste déjà équipé, il n'ajoute
> que ce qui manque. Pour remettre un poste à neuf : `python installer_dossier_geeks.py --neuf`

Installez-le **aussi sur votre machine** : vous travaillerez dans les mêmes conditions que vos
élèves, et vous rencontrerez les mêmes problèmes qu'eux avant eux.

---

## La clé USB

`preparer_cle_usb.py` assemble un dossier `cle-usb/` à partir des fichiers du projet :

```
cle-usb/
├── LISEZ-MOI.txt                   les 3 gestes à faire avec la clé
├── installer_dossier_geeks.py      à lancer sur chaque poste
├── depart_eleves_piste_bleue.py    le fichier que l'installateur copie
├── 1-DEMO/                         le jeu fini, l'anti-sèche, le vérificateur
├── 2-A-IMPRIMER/                   les PDF de la séance + le règlement intérieur
├── 3-MES-FICHES/                   la fiche de séance, le classeur de suivi, le règlement en Word
├── 4-SAUVEGARDES-ELEVES/           où déposer le travail des binômes en fin de séance
└── 5-CODE-OFFICIEL/                le code publié devant les élèves à 110 min
```

Ce dossier **n'est pas conservé dans le dépôt** : ce ne sont que des copies de fichiers qui
existent déjà ailleurs. On le refabrique en deux secondes, et on évite ainsi 2 Mo de doublons.

Pour une autre séance : `python 4-outils/preparer_cle_usb.py --seance 2`
Pour écrire directement sur la clé : `python 4-outils/preparer_cle_usb.py --vers E:/`

---

## Refabriquer les PDF

`faire_les_pdf.py` convertit tous les `.html` d'une séance. La règle tient en deux lignes :

```
a-imprimer/sources/*.html   →  le PDF monte dans  a-imprimer/
tout autre  *.html          →  le PDF est écrit à côté de sa source
```

Pour le règlement intérieur : `python 4-outils/faire_les_pdf.py --reglement`
(il convertit alors `0-administratif/sources/*.html` dans `0-administratif/`).

Il a besoin de Chrome ou Chromium. Sans navigateur installé, il vous dit quoi faire à la main.

---

## Le règlement intérieur

Son texte n'est écrit qu'**une seule fois**, dans `faire_le_reglement.py`, article par article et en clair.
Le programme en sort le Word **et** la source du PDF : les deux versions ne peuvent donc pas se contredire.

```
python 4-outils/faire_le_reglement.py          → 0-administratif/reglement-interieur.docx
                                                 + 0-administratif/sources/…html
python 4-outils/faire_les_pdf.py --reglement   → 0-administratif/reglement-interieur.pdf
```

Déposez votre bandeau d'en-tête dans `0-administratif/en-tete.png` (ou `.jpg`) avant de relancer :
il remplace alors le bandeau de texte, dans le Word comme dans le PDF.
Détails : [0-administratif/LISEZ-MOI.md](../0-administratif/LISEZ-MOI.md)

---

## Les révisions à la maison

Deux envois par semaine aux parents. `faire_les_revisions.py` écrit les deux pages et le texte des
messages, dans `2-seances/S01-decollage/a-envoyer/revisions-maison/` :

```
python 4-outils/faire_les_revisions.py             → envoi-1.html · envoi-2.html
                                                     + messages-a-copier.md
python 4-outils/faire_les_pdf.py --seance 1        → envoi-1.pdf · envoi-2.pdf
```

Le contenu de chaque semaine est écrit en clair en haut du programme, dans `SEMAINES` : questions,
réponses, défis. **Il ne porte que sur ce qui a déjà été fait en classe**, et s'ajoute séance par séance.
