# 📊 Les points transmis au responsable

Un dossier, un document par point demandé. Chaque point est **daté et arrêté** : on ne le modifie pas
après l'avoir envoyé, on en fait un nouveau.

| Date | Document | Demandé par | Couvre |
|---|---|---|---|
| 2 octobre 2026 | [`point-assiduite-et-devoirs.pdf`](point-assiduite-et-devoirs.pdf) · [version Word](point-assiduite-et-devoirs.docx) | Pasteur Eli | Retards, absences et devoirs — séances 1 à 3, devoirs 1 à 3 |

## Comment il est fabriqué

Les chiffres ne sont pas saisis à la main : ils sont **lus dans les fichiers**.

| Ce qui est repris | D'où ça vient |
|---|---|
| Présence, retards, absences | classeur de suivi, onglet `Présence` |
| Fait de discipline | classeur de suivi, onglet `Indiscipline` |
| Devoirs rendus et notes | les réponses des formulaires Google (un fichier par devoir) |

Le générateur : [`sources/point-assiduite-et-devoirs.html`](sources/point-assiduite-et-devoirs.html) —
c'est la source à corriger si un nom ou une case est faux. Le PDF et le Word en sont tirés.

## Les trois règles qu'on s'est données

1. **Un devoir dont l'échéance n'est pas passée n'est jamais compté comme non rendu.** Il est marqué
   *en attente*, et la colonne « devoirs exigibles » ne le compte pas.
2. **Toute incertitude est écrite dans le document**, pas corrigée en silence — une réponse signée d'un
   nom non inscrit, un double envoi, une note encore partielle.
3. **Aucun jugement sur un enfant.** On distingue ce qui relève de la famille (un horaire, un téléphone)
   de ce qui relève de l'élève. Les trois retardataires permanents rendent tous leurs devoirs : ce n'est
   pas un problème de motivation, et le document le dit.
