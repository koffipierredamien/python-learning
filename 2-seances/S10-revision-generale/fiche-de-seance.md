# Séance 10 — « Révision générale » · samedi 14 novembre 2026

> **Séance faite, et non terminée.** On en garde ici le compte rendu honnête : ce qui a été traité,
> ce qui ne l'a pas été, et ce que ça a changé pour la suite.

---

## Ce qui était prévu, et ce qui s'est passé

| | |
|---|---|
| **Format** | Le cours en quiz : cinq manches, chacune = deux questions à la carte + **un atelier au clavier** |
| **Prévu** | Les cinq manches, puis l'introduction de la **boucle `while`** en fin de séance |
| **Fait** | **Les trois premières manches** — texte ou nombre · les listes et l'indice · le décalage |
| **Non fait** | Les manches 4 et 5, et **la boucle n'a pas été commencée du tout** |

**Pourquoi :** les ateliers ont duré plus longtemps que prévu, parce que les élèves ont cherché les
causes eux-mêmes au lieu de recevoir la correction. **Ce dépassement est un bon dépassement** — mais
il a coûté la fin de la séance.

---

## Ce que la séance a appris à l'enseignant

C'était son premier but, et il est atteint : on sait maintenant, poste par poste, où ça coince.

| Ce qui tient | Ce qui est fragile |
|---|---|
| `int()` / `str()` et le piège de `input` | **le décalage des lignes** — ce qui est dans le `if` et ce qui n'y est pas |
| la liste, l'indice, l'`IndexError` | le `if` / `else` manque encore d'exercices |
| `and` / `or`, posés en séance 9 | `elif` n'a jamais été introduit |

**C'est ce constat qui a servi à réordonner le parcours le 20 novembre** — voir [le plan](../PLAN.md).

---

## Ce qui reste de cette séance, et qui sert encore

| | |
|---|---|
| **Le diaporama complet** | [`a-projeter/revision-generale.pptx`](a-projeter/revision-generale.pptx) — **38 diapos**. Les manches 4 et 5 n'ont pas été jouées : **elles sont toujours dedans, prêtes** |
| **La conduite de séance** | [`revision-generale.md`](revision-generale.md) — minutage, réponses, et l'ordre dans lequel couper |
| **Les cinq corrigés d'atelier** | [`code/revision_ateliers_corrige.py`](code/revision_ateliers_corrige.py) — exécuté, sans aucun `for` ni `while` |
| **Le formulaire à la maison** | [`a-envoyer/quiz-revision-generale.md`](a-envoyer/quiz-revision-generale.md) — 20 questions, corrigées automatiquement, **et qui ne dépendent d'aucune séance** : on peut le renvoyer n'importe quand |
| **Le déroulé pour le responsable** | [`a-envoyer/deroule-seance-10.pdf`](a-envoyer/deroule-seance-10.pdf) — il dit, sans détour, ce qui n'a pas pu être traité |

> **Les manches 4 et 5 ne sont pas perdues.** Elles portent sur `and` / `or` et sur le coût de la
> recopie — le jour où la répétition sera au programme, elles ouvriront la séance toutes seules.

---

## Ce que cette séance a retiré du parcours

Le matériel qui avait été préparé pour la boucle, le gagnant et le tournoi annonçait des dates
fausses. Il a été **retiré du parcours actif le 20 novembre**, et il est conservé dans l'historique
Git. Le détail est dans [le plan](../PLAN.md), § 2.
