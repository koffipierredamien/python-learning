# 🗺️ Où nous en sommes, et ce qui vient

> **Ce document dit la vérité du terrain, pas le programme rêvé.** Il est refait à chaque fois que
> la réalité s'écarte du plan — c'est-à-dire souvent, et c'est normal.
>
> **Dernière mise à jour : mercredi 25 novembre 2026.**

---

## 1. Ce qui a réellement eu lieu

| Séance | Date | Ce qui s'est passé | Acquis |
|---|---|---|---|
| **[S01](S01-decollage/compte-rendu.md)** | 12 sept | Décollage — la théorie, les missions | ✅ |
| **[S02](S02-premier-contact/fiche-de-seance.md)** | 19 sept | `print`, la variable, `input` | ✅ |
| **[S03](S03-tp-les-joueurs/a-imprimer/quantites-et-formats.md)** | 26 sept | **TP n°1** — les deux joueurs | ✅ |
| **[S04](S04-le-jeu-compte/fiche-de-seance.md)** | 3 oct | `int()` / `str()` · *(le compteur et la décision n'ont pas été finis)* | ⚠️ partiel |
| **[S05](S05-la-decision/fiche-de-seance.md)** | 10 oct | Le compteur, les opérateurs, `if` / `else` | ✅ |
| **[S06](S06-le-plateau-se-souvient/fiche-de-seance.md)** | 17 oct | **La liste**, l'indice, `plateau[case - 1]` | ✅ |
| **[S07](S07-la-case-occupee/fiche-de-seance.md)** | 24 oct | Le `if` dans le `if`, la case déjà prise | ✅ |
| **[S08](S08-tp-le-plateau/fiche-de-seance.md)** | 31 oct | **TP n°2 — le plateau vivant** | ✅ |
| **[S09](S09-et-ou/fiche-de-seance.md)** | 7 nov | `and` / `or`, la condition unique | ✅ |
| **[S10](S10-revision-generale/revision-generale.md)** | 14 nov | **Révision générale** — *non terminée : deux manches sur cinq n'ont pas été faites* | ⚠️ partiel |
| **[S11](S11-les-trois-chemins/fiche-de-seance.md)** | 21 nov | **`elif`** — *arrêtée à la page de l'algorithme : les apprenants n'avaient ni papier ni stylo* | ⚠️ partiel |

### Ce que la classe sait faire, au 25 novembre

`print` · les variables · `input` · le `+` qui colle · **`int()` et `str()`** · le compteur ·
les opérateurs `>` `<` `>=` `<=` `==` `!=` · **`if` / `else`** · **le `if` dans le `if`** ·
**`and` et `or`** · **la liste et l'indice `case - 1`** · lire un message rouge ·
**`elif` et la règle du premier vrai** — *vus, mais pas encore pratiqués au clavier*.

**Leur jeu :** il accueille les deux joueurs, affiche un plateau qui se souvient des coups, refuse
une case qui n'existe pas et une case déjà prise — mais sans dire laquelle des deux.

### Ce que la classe ne sait PAS encore faire

| | |
|---|---|
| **Écrire une cascade au clavier** | la notion est vue, l'atelier n'a pas eu lieu |
| **La répétition (`while`)** | **pas commencée.** Elle n'arrivera que le jour où recopier sera devenu insupportable |
| **Détecter le gagnant** | elle suppose la répétition |
| **Les fonctions, le graphique** | plus tard |

---

## 2. Pourquoi ce dépôt a été réordonné le 20 novembre

Un parcours de sept séances avait été préparé d'avance, d'octobre à fin novembre. **La réalité en a
décidé autrement** : la révision du 14 novembre n'a pas pu aller à son terme, la répétition n'a pas
été commencée, et le `if` / `else` manquait encore d'exercices.

Les séances préparées pour la boucle, le gagnant et le tournoi **ont donc été retirées du parcours
actif** : elles annonçaient des dates fausses et un ordre qui ne tient plus.

> **Rien n'est perdu.** Tout ce qui a été retiré est dans l'historique Git, au commit
> `65667c2`, et **les générateurs sont restés en place** : une séance se reconstruit en quelques
> secondes le jour où elle reprendra sa place. Voir
> [`generateurs/LISEZ-MOI.md`](generateurs/LISEZ-MOI.md).

**La règle qu'on se donne désormais : on prépare la séance suivante, pas le trimestre.**
Le parcours d'ensemble reste celui du [README](../README.md) ; le calendrier, lui, se décide
chaque semaine, sur ce qui a été réellement compris.

---

## 3. Où la séance 11 s'est arrêtée, et par où elle reprend

### ⚠️ Ce qui s'est passé

La séance s'est arrêtée **à la diapo qui demande d'écrire l'algorithme** : les apprenants
n'avaient **ni papier ni stylo**. Tout ce qui précède a été fait.

| Ce qui a été fait | Ce qui reste |
|---|---|
| Le quiz de révision — les 7 cartes | **L'atelier 2** : la cascade des mentions, algorithme d'abord |
| Manche 1 : le constat (le jeu dit quelque chose de faux) | Manche 4 : la cascade reportée **dans leur jeu** |
| Manche 2 : `elif`, et l'atelier « deux `if`, ou un `elif` ? » | L'exercice **Le Bulletin** |
| Manche 3 : les deux questions — le piège de `note = 18`, et l'ordre | ⭐ **Le Prix du Ticket** |

**La notion est passée ; la pratique au clavier, non.** C'est exactement ce qui manque.

### Ce qu'on fait la prochaine fois

**On reprend la même séance, à la diapo où l'on s'est arrêté.** Rien à repréparer : le
[diaporama](S11-les-trois-chemins/a-projeter/cours-en-quiz.pptx) et la
[fiche](S11-les-trois-chemins/fiche-de-seance.md) sont les mêmes. Deux précautions :

1. **Du papier et un stylo sur chaque poste, avant leur arrivée.** C'est ce qui a bloqué la
   séance, et c'est la chose la moins chère à prévoir.
2. **Cinq minutes de reprise** sur les manches 2 et 3 avant de repartir : une semaine a passé.

| J'ai besoin de… | C'est ici |
|---|---|
| **Tout projeter** | [`a-projeter/cours-en-quiz.pptx`](S11-les-trois-chemins/a-projeter/cours-en-quiz.pptx) — on reprend à l'atelier de la manche 3 |
| Animer | [📖 la fiche de séance](S11-les-trois-chemins/fiche-de-seance.md) |
| Les corrigés | [les 4 ateliers](S11-les-trois-chemins/code/ateliers-corriges.py) · [Le Bulletin](S11-les-trois-chemins/code/corrige-exercice.py) · [⭐ Le Prix du Ticket](S11-les-trois-chemins/code/corrige-exercice-etoile.py) |
| Imprimer | 🖨️ [la liste du jour](S11-les-trois-chemins/a-imprimer/quantites-et-formats.md) — 8 × [l'aide-mémoire](S11-les-trois-chemins/a-imprimer/1-aide-memoire.pdf) et 8 × [la feuille d'exercice](S11-les-trois-chemins/a-envoyer/exercice-le-bulletin.pdf) |
| Préparer les postes | [`code/depart_eleves.py`](S11-les-trois-chemins/code/depart_eleves.py) · le Filet : [`code_officiel_fin_de_seance.py`](S11-les-trois-chemins/code/code_officiel_fin_de_seance.py) |
| Transmettre à Pasteur Eli | [📋 le déroulé](S11-les-trois-chemins/a-envoyer/deroule-seance-11.pdf) · [version Word](S11-les-trois-chemins/a-envoyer/deroule-seance-11.docx) |

### Les deux choses à ne pas lâcher

1. **L'algorithme sur le papier avant le clavier.** C'est exigé deux fois : à l'atelier 2 et à
   l'exercice. **Refusez le clavier à qui ne l'a pas écrit** — ça prend trois minutes, et c'est la
   compétence qui manque le plus.
2. **L'atelier 2** (la cascade des mentions). C'est celui qu'on n'a pas pu faire : il passe avant
   tout le reste.

### Pour les rapides, comme Sara

Trois niveaux, dans cet ordre : les ⭐ **à l'intérieur de chaque atelier** · l'**exercice étoile**
(Le Prix du Ticket, deux pièges cachés) · et, si elle a tout fini, la
[**mission autonome n°1**](missions-autonomes/LISEZ-MOI.md), qui s'écrit entièrement avec ce qu'elle sait.

---

## 3 bis. Le travail envoyé entre les deux séances

Deux documents, pour que la semaine ne soit pas perdue — le mode d'emploi et le message aux
familles sont dans
[**`travail-de-la-semaine.md`**](S11-les-trois-chemins/a-envoyer/travail-de-la-semaine.md).

| | Quoi | Pour qui |
|---|---|---|
| 🧠 | [**Le quiz de rappel**](S11-les-trois-chemins/a-envoyer/quiz-rappel-general.gs) — 20 questions, corrigées automatiquement, de la première séance jusqu'à l'ordre des conditions | tout le monde, depuis un téléphone |
| 🏅 | [**L'exercice — La Médaille**](S11-les-trois-chemins/a-envoyer/exercice-la-medaille.pdf) — trois questions de réflexion, puis un programme **sans aucune consigne de code** | ceux qui ont un ordinateur |

**Pourquoi La Médaille :** la question du quiz qui dit *« du plus précis au plus large »* ne vaut
que si on l'a pratiquée. Ici, le cas « exactement 100 » placé après `>= 90` n'est jamais atteint —
l'enfant le découvre en tapant 100, et personne ne le lui aura dit.
Le corrigé est dans
[`correction-la-medaille.py`](S11-les-trois-chemins/a-envoyer/correction-la-medaille.py) : **il ne
part pas aux élèves.**

---

## 4. Le format des séances a changé

Depuis le 14 novembre, **le cours lui-même est un quiz**. On ne fait plus « je montre / vous
faites » :

| | |
|---|---|
| 🃏 **La carte** | On projette une question, tout le monde lève sa carte **en même temps**, au signal |
| ⌨️ **Le clavier** | On tape le code projeté, **on prédit** ce qu'il va faire, **et seulement après on lance** |
| ⭐ **Plus loin** | Chaque atelier porte une ligne ⭐ pour ceux qui finissent avant les autres |
| ✍️ **L'algorithme** | Au moins une fois par séance : en français, sur le cahier, **avant** le clavier |

**La notion du jour arrive toujours après le constat de son absence**, jamais avant.

Et **la fiche de séance continue d'exister** : c'est elle qui produit
[le déroulé transmis à Pasteur Eli](S11-les-trois-chemins/a-envoyer/deroule-seance-11.pdf),
rédigé sans code ni jargon.

---

## 5. Ce qui reste prêt et attend son tour

| Ce qui existe déjà | Où |
|---|---|
| **La révision générale** (46 diapos) et son formulaire de 20 questions | [`S10-revision-generale/`](S10-revision-generale/revision-generale.md) |
| **L'affiche du trimestre**, les sept cases du Mur de Mission | [`a-afficher/`](a-afficher/LISEZ-MOI.md) |
| **La mission autonome n°1** — l'ascenseur, pour les élèves en avance | [`missions-autonomes/`](missions-autonomes/LISEZ-MOI.md) |
| **Les exercices de maison** du Coffre-Fort, de la Bataille Navale et du Club Geek | `S06/`, `S09/` · `a-envoyer/` |
| **Tous les générateurs** — diaporamas, quiz, fiches, déroulés, aide-mémoires | [`generateurs/`](generateurs/LISEZ-MOI.md) |

---

## 6. Les règles qui ne changent pas

1. **Le Filet** — à la fin de chaque séance, le code officiel est distribué à tout le monde, fini ou
   pas. Personne ne commence la séance suivante en retard.
2. **Un seul exercice pour tous** — des défis ⭐ pour ceux qui finissent avant, de l'aide (pas un
   exercice plus facile) pour ceux qui bloquent.
3. **Le jeu doit marcher à la fin de chaque samedi.** Un jeu qui fait moins mais qui marche vaut
   mieux qu'un jeu à moitié écrit.
4. **On ne devance jamais le besoin.** Chaque notion arrive quand le projet la réclame — et on
   accepte que le calendrier en souffre.
