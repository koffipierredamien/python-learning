# 📊 Le classeur de suivi

**[`classeur-de-suivi.xlsx`](classeur-de-suivi.xlsx)** — 14 onglets, tout ce que les deux enseignants
doivent savoir et noter sur le groupe.

## L'importer dans Google Sheets

1. **Google Drive** → `Nouveau` → `Importation de fichier` → choisir `classeur-de-suivi.xlsx`
2. Puis, dans le fichier ouvert : `Fichier` → `Enregistrer au format Google Sheets`
3. `Partager` → **accès restreint**, et ajouter uniquement les deux enseignants

> ⚠️ Ce classeur contient les coordonnées de mineurs. Il ne doit **jamais** être publié,
> ni partagé par lien public. Aucune donnée personnelle n'est publiée en ligne.

Les menus déroulants, les calculs, les couleurs et les alertes sont conservés à l'import.

## La règle d'or

**On saisit les noms une seule fois, dans l'onglet `01_Apprenants`.** Tous les autres onglets les
recopient automatiquement. Si un nom manque ailleurs, c'est qu'il manque dans `01`.

## Les 14 onglets

| Onglet | À quoi il sert |
|---|---|
| `00_Mode-emploi` | Comment se servir du classeur, et le code couleur |
| `01_Apprenants` | La fiche complète de chaque élève + les contacts des responsables. **Le point de départ** |
| `02_Diagnostic` | Résultats du Test de Décollage, profil P0→P3. **Interne : jamais communiqué** |
| `03_Presence` | Feuille de présence des 22 séances, taux calculé, alerte sous 85 % |
| `04_Suivi-seances` | Ce que chaque élève a produit, sur quelle piste. **Colonne ALERTE automatique** |
| `05_Observations` | Le journal : un fait marquant, l'action décidée, et si elle a été faite |
| `06_Binomes` | Qui travaille avec qui, à quel poste, séance par séance |
| `07_Badges-Grades` | Les badges distribués et le grade atteint |
| `08_Passeport` | Les 12 gestes machine — remplace le livret papier |
| `09_Checklist-S01` | Les 43 tâches de préparation de la séance 1, avec responsable et date |
| `10_Journal-enseignants` | La revue de 15 min après chaque séance : 3 questions, et les décisions |
| `11_Materiel` | L'inventaire : imprimé, acheté, installé |
| `12_Tableau-de-bord` | 25 indicateurs calculés automatiquement |
| `13_Listes` | Les valeurs des menus déroulants — modifiables |

## Le déclencheur à surveiller

Dans `04_Suivi-seances`, la colonne **ALERTE** passe à `OUI` dès qu'un élève cumule **deux séances de
suite sans production**. Cet élève entre sur la **liste des 10 minutes** : le Mécanicien lui consacre
10 minutes en tête-à-tête à la séance suivante.

C'est un rendez-vous, pas une punition — et c'est ce qui empêche un décrochage silencieux de devenir
un abandon. Le tableau de bord affiche en permanence le nombre d'élèves concernés.

## Modifier la structure du classeur

Le classeur est généré par [`../4-outils/construire_classeur.py`](../4-outils/construire_classeur.py).
Ne le relancez que pour changer la structure (ajouter une colonne, un onglet, une valeur de liste) :
**il écrase le fichier, donc les données déjà saisies.** Pour l'usage courant, travaillez dans Google Sheets.
