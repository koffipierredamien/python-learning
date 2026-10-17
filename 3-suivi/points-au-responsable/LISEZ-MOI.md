# 📊 Les points transmis au responsable

Un dossier, un document par point demandé. Chaque point est **daté et arrêté** : on ne le modifie pas
après l'avoir envoyé, on en fait un nouveau.

| Date | Document | Demandé par | Couvre |
|---|---|---|---|
| 2 octobre 2026 | [`point-assiduite-et-devoirs.pdf`](point-assiduite-et-devoirs.pdf) · [version Word](point-assiduite-et-devoirs.docx) | le responsable | Retards, absences et devoirs — séances 1 à 3, devoirs 1 à 3 |
| 17 octobre 2026 | [`programme-octobre-novembre.pdf`](programme-octobre-novembre.pdf) · [version Word](programme-octobre-novembre.docx) | *transmis d'initiative* | Le programme des **sept séances** du 17 octobre au 28 novembre : contenu, travail donné aux familles, ce qui est demandé à l'école |

> Le second document n'est pas un compte rendu mais une **annonce de programme** : il se transmet
> avant les séances, et il peut être communiqué aux parents qui en font la demande. Il est fabriqué
> par [`2-seances/generateurs/programme_responsable.py`](../../2-seances/generateurs/programme_responsable.py).
>
> **Deux points d'étape sont prévus** sur ces deux mois : après le TP du 31 octobre, et après le
> tournoi du 28 novembre — celui-là reprendra le bilan rempli par les élèves eux-mêmes.

## Comment il est fabriqué

Les chiffres ne sont pas saisis à la main : ils sont **lus dans les fichiers**.

| Ce qui est repris | D'où ça vient |
|---|---|
| Présence, retards, absences | classeur de suivi, onglet `Présence` |
| Fait de discipline | classeur de suivi, onglet `Indiscipline` |
| Devoirs rendus | les réponses des formulaires Google (un fichier par devoir) |
| Retards excusés | onglet `Observations` du classeur |

Le générateur : [`sources/rapport.py`](sources/rapport.py) — **c'est le seul fichier à corriger** si un
nom ou une case est faux. Il écrit le HTML, dont on tire le PDF ; [`sources/rapport_word.py`](sources/rapport_word.py)
relit les mêmes données et écrit la version Word. Les deux documents ne peuvent donc pas se contredire.

## Les trois règles qu'on s'est données

1. **Un devoir dont l'échéance n'est pas passée n'est jamais compté comme non rendu.** Il est marqué
   *en attente*, et la colonne « devoirs exigibles » ne le compte pas.
2. **Un retard excusé n'est pas un retard.** Quatre élèves ont cours à leur école le samedi matin : leurs
   retards sont comptés à part, en gris, et le document explique pourquoi. On ne mélange jamais ce qui
   dépend de l'enfant et ce qui ne dépend pas de lui.
3. **Aucun jugement sur un enfant.** On distingue ce qui relève de la famille (un téléphone qui ne suit
   pas, une école le samedi) de ce qui relève de l'élève. Les quatre retardataires rendent tous leurs
   devoirs : le document le dit, pour qu'on n'en tire pas la mauvaise conclusion.
