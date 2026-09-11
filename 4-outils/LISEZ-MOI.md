# 🔧 Outils

Cinq programmes Python. Vous les lancez depuis Thonny (`F5`) ou en ligne de commande.
Aucun n'est destiné aux élèves.

| Programme | Quand s'en servir |
|---|---|
| [`jeu_xo_complet.py`](jeu_xo_complet.py) | **Le jeu XO terminé.** C'est la démonstration d'ouverture de la séance 1 (le « WOW »), et le point d'arrivée du parcours. 2 joueurs, ou contre un ordinateur imbattable. |
| [`verifier_un_poste.py`](verifier_un_poste.py) | **À lancer sur chaque machine avant la séance.** Vérifie Python, la logique du jeu, et que la fenêtre graphique pourra s'ouvrir. Tout doit afficher `[OK]`. |
| [`installer_dossier_geeks.py`](installer_dossier_geeks.py) | **À lancer sur chaque poste de la salle** (et sur votre machine). Crée le dossier `GEEKS` sur le Bureau, avec le fichier de départ de l'élève. |
| [`preparer_cle_usb.py`](preparer_cle_usb.py) | Fabrique le dossier `cle-usb/` à emporter le samedi. |
| [`construire_classeur.py`](construire_classeur.py) | Refabrique le classeur de suivi **à vide**. À n'utiliser que pour changer sa structure. |

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
├── 2-A-IMPRIMER/                   les PDF de la séance
├── 3-MES-FICHES/                   la fiche de séance détaillée
├── 4-SAUVEGARDES-ELEVES/           où déposer le travail des binômes en fin de séance
└── 5-CODE-OFFICIEL/                le code publié devant les élèves à 110 min
```

Ce dossier **n'est pas conservé dans le dépôt** : ce ne sont que des copies de fichiers qui
existent déjà ailleurs. On le refabrique en deux secondes, et on évite ainsi 2 Mo de doublons.

Pour une autre séance : `python 4-outils/preparer_cle_usb.py --seance 2`
Pour écrire directement sur la clé : `python 4-outils/preparer_cle_usb.py --vers E:/`

---

## Le classeur de suivi

⚠️ `construire_classeur.py` **écrase** `3-suivi/classeur-de-suivi.xlsx` et donc les données
déjà saisies. Ne le lancez que pour modifier la structure du classeur (ajouter une colonne, un
onglet, une valeur de menu déroulant). Pour l'usage courant, travaillez dans Google Sheets.

Il a besoin d'`openpyxl` : `pip install openpyxl`
