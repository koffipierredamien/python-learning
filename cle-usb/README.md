# 💾 La clé USB de la séance

**Copiez tout le contenu de ce dossier à la racine de votre clé USB.**
Vous aurez alors, en une seule clé, tout ce qu'il faut pour animer la séance et équiper la salle.

```
CLE USB/
│
├── installer_sur_ce_poste.py      ← À LANCER SUR CHAQUE ORDINATEUR DE LA SALLE
│
├── 1-DEMO/
│     xo_complet.py                Le jeu fini — la démo du « WOW » (08→12 min)
│     live_coding_S01.py           Mon anti-sèche pour le live coding (78→90 min)
│     verifier_le_jeu.py           Vérifie qu'un poste est bien configuré
│
├── 2-A-COPIER-SUR-LES-POSTES/
│     GEEKS/                       Le dossier qui doit apparaître sur chaque Bureau
│       ├── mon_xo/jeu.py            le fichier de travail (piste Bleue, déjà prêt)
│       ├── xo_officiel/             LE FILET — vide avant la séance 1
│       └── LISEZ-MOI.txt
│
├── 3-SUPPORTS-A-IMPRIMER/        Les 13 documents + le guide d'impression
│
├── 4-SAUVEGARDES-ELEVES/
│     S01/                          ← on y copie le travail des binômes en fin de séance
│
├── 5-MES-FICHES/
│     MON-SCRIPT.html               Le script d'animation (à imprimer)
│     fiche-de-seance.md            La fiche détaillée complète
│     fiche-de-validation.html      Le document pour les responsables
│
└── 6-CODE-OFFICIEL/
      S01/jeu.py                    Le code officiel, publié devant les élèves à 110 min
```

---

## Les 3 gestes à faire avec cette clé

### 1️⃣ Avant la séance — équiper chaque poste de la salle

Sur **chaque** ordinateur : branchez la clé, ouvrez `installer_sur_ce_poste.py` dans Thonny, `F5`.
Le dossier `GEEKS` apparaît sur le Bureau, avec le fichier de travail déjà dedans.

> Le script **ne détruit jamais le travail d'un élève** : si un dossier `GEEKS` existe déjà, il ajoute
> seulement ce qui manque. Pour remettre un poste à neuf : `python installer_sur_ce_poste.py --neuf`

Puis, sur ce poste, vérifiez : `1-DEMO/verifier_le_jeu.py` → `F5`. Tout doit être `[OK]`.

### 2️⃣ Pendant la séance — à 110 minutes

Devant les élèves, solennellement : vous branchez la clé et vous copiez `jeu.py` dans `xo_officiel/`.
**C'est le moment du Filet**, et c'est ce qui vous permet de promettre qu'une absence ne mettra
jamais personne en retard.

### 3️⃣ En fin de séance — sauvegarder

Le Mécanicien passe avec la clé et copie le fichier de chaque binôme dans `4-SAUVEGARDES-ELEVES/S01/`.
Filet de sécurité côté enseignants : si un poste est réinitialisé pendant la semaine, rien n'est perdu.

---

## Le dossier GEEKS, sur votre machine à vous

Chez vous, gardez la **même arborescence** que sur les postes de la salle — vous travaillerez
dans les mêmes conditions que vos élèves, et vous verrez les mêmes problèmes qu'eux :

```
Bureau/
└── GEEKS/
     ├── mon_xo/          ← vous codez ici, comme un élève
     │     jeu.py
     └── xo_officiel/     ← le code de référence
           jeu.py
```

Le plus simple : lancez `installer_sur_ce_poste.py` sur votre propre machine aussi.

---

## Après avoir modifié un support

Relancez, depuis le dossier du projet :

```
python outils/preparer_la_cle.py
```

Il reconstruit ce dossier à partir des sources (fiches, impressions, démo, code officiel),
puis vous le recopiez sur la clé. Pour préparer la clé d'une autre séance :
`python outils/preparer_la_cle.py --seance 2`
