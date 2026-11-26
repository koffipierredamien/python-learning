# 🗺️ Où nous en sommes, et ce qui vient

> **Ce document dit la vérité du terrain, pas le programme rêvé.** Il est refait à chaque fois que
> la réalité s'écarte du plan — c'est-à-dire souvent, et c'est normal.
>
> **Dernière mise à jour : jeudi 26 novembre 2026.**

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
| **[S12](S12-le-jeu-dit-pourquoi/fiche-de-seance.md)** | **28 nov** | **La cascade pratiquée**, et la brique : le jeu dit **laquelle** des deux raisons | 🔜 **prête** |

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

## 3. La prochaine séance — [S12, « Le jeu dit enfin pourquoi »](S12-le-jeu-dit-pourquoi/fiche-de-seance.md)

### ⚠️ D'où elle part

La séance 11 s'est arrêtée **à la diapo qui demande d'écrire l'algorithme** : les apprenants
n'avaient **ni papier ni stylo**.

| Ce qui a été fait le 21 | Ce que la séance 12 reprend |
|---|---|
| Le quiz de révision — 7 cartes | **Écrire une cascade soi-même**, algorithme d'abord |
| Le constat : le jeu dit quelque chose de faux | **La mettre dans le jeu** — la brique, jamais posée |
| `elif`, et l'atelier « deux `if`, ou un `elif` ? » | L'exercice **Le Bulletin** |
| Le piège de `note = 18`, et l'ordre des conditions | ⭐ **Le Prix du Ticket** |

**La notion est passée ; la pratique au clavier, non.** La séance 12 **n'apporte rien de neuf** :
elle finit ce qui a été commencé, en partant du travail fait à la maison.

### Son programme

| Horaire | Séquence |
|---|---|
| 12 h 00 | Prière et accueil |
| 12 h 15 | **Manche 1** — quiz de reprise, 7 cartes |
| 12 h 27 | **Manche 2** — La Médaille : le papier, puis le clavier |
| 12 h 45 | **Manche 3** — l'erreur qui ne fait pas d'erreur |
| 12 h 50 | **Manche 4** — et maintenant, VOTRE JEU |
| 13 h 10 | Pause |
| 13 h 20 | **L'exercice** : Le Bulletin |
| 13 h 42 | ⭐ **L'exercice étoile** : Le Prix du Ticket |
| 13 h 50 | Clôture |

| J'ai besoin de… | C'est ici |
|---|---|
| **Tout projeter** | [`a-projeter/cours-en-quiz.pptx`](S12-le-jeu-dit-pourquoi/a-projeter/cours-en-quiz.pptx) — **38 diapos**, de la prière à la clôture |
| Animer | [📖 la fiche de séance](S12-le-jeu-dit-pourquoi/fiche-de-seance.md) |
| Les corrigés | [La Médaille](S12-le-jeu-dit-pourquoi/code/corrige-la-medaille.py) · [Le Bulletin](S12-le-jeu-dit-pourquoi/code/corrige-exercice.py) · [⭐ Le Prix du Ticket](S12-le-jeu-dit-pourquoi/code/corrige-exercice-etoile.py) |
| Imprimer | 🖨️ [la liste du jour](S12-le-jeu-dit-pourquoi/a-imprimer/quantites-et-formats.md) · [l'aide-mémoire](S12-le-jeu-dit-pourquoi/a-imprimer/1-aide-memoire.pdf) · [la feuille d'exercice](S12-le-jeu-dit-pourquoi/a-envoyer/exercice-le-bulletin.pdf) |
| Préparer les postes | [`code/depart_eleves.py`](S12-le-jeu-dit-pourquoi/code/depart_eleves.py) · le Filet : [`code_officiel_fin_de_seance.py`](S12-le-jeu-dit-pourquoi/code/code_officiel_fin_de_seance.py) |
| Transmettre à Pasteur Eli | [📋 le déroulé](S12-le-jeu-dit-pourquoi/a-envoyer/deroule-seance-12.pdf) · [version Word](S12-le-jeu-dit-pourquoi/a-envoyer/deroule-seance-12.docx) |

### 🔴 La seule chose à ne pas oublier

**Une feuille de papier et un stylo sur chaque poste, vérifiés avant qu'ils entrent.**
C'est ce qui a coûté la séance précédente, et c'est la chose la moins chère à prévoir.
À défaut : l'algorithme s'écrit **dans Thonny, en commentaires** — ce n'est pas un pis-aller,
c'est une vraie méthode de programmeur.

### Les deux autres choses à ne pas lâcher

1. **Le clavier se refuse à qui n'a pas écrit son algorithme.** Trois minutes, et pour tout le
   monde — sans exception, sinon la règle ne vaut rien.
2. **La manche 4.** C'est la brique, et c'est celle que la séance 11 n'a pas atteinte. Si le temps
   manque, on sacrifie Le Bulletin, jamais la manche 4.

### Pour les rapides, comme Sara

Trois niveaux, dans cet ordre : les ⭐ **à l'intérieur de chaque atelier** · l'**exercice étoile**
(Le Prix du Ticket, deux pièges cachés) · et, si elle a tout fini, la
[**mission autonome n°1**](missions-autonomes/LISEZ-MOI.md), qui s'écrit entièrement avec ce qu'elle sait.

---

## 4. Le travail envoyé entre les deux séances

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

## 5. Le format des séances a changé

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
[le déroulé transmis à Pasteur Eli](S12-le-jeu-dit-pourquoi/a-envoyer/deroule-seance-12.pdf),
rédigé sans code ni jargon.

---

## 6. Ce qui reste prêt et attend son tour

| Ce qui existe déjà | Où |
|---|---|
| **La révision générale** (46 diapos) et son formulaire de 20 questions | [`S10-revision-generale/`](S10-revision-generale/revision-generale.md) |
| **L'affiche du trimestre**, les sept cases du Mur de Mission | [`a-afficher/`](a-afficher/LISEZ-MOI.md) |
| **La mission autonome n°1** — l'ascenseur, pour les élèves en avance | [`missions-autonomes/`](missions-autonomes/LISEZ-MOI.md) |
| **Les exercices de maison** du Coffre-Fort, de la Bataille Navale et du Club Geek | `S06/`, `S09/` · `a-envoyer/` |
| **Tous les générateurs** — diaporamas, quiz, fiches, déroulés, aide-mémoires | [`generateurs/`](generateurs/LISEZ-MOI.md) |

---

## 7. Les règles qui ne changent pas

1. **Le Filet** — à la fin de chaque séance, le code officiel est distribué à tout le monde, fini ou
   pas. Personne ne commence la séance suivante en retard.
2. **Un seul exercice pour tous** — des défis ⭐ pour ceux qui finissent avant, de l'aide (pas un
   exercice plus facile) pour ceux qui bloquent.
3. **Le jeu doit marcher à la fin de chaque samedi.** Un jeu qui fait moins mais qui marche vaut
   mieux qu'un jeu à moitié écrit.
4. **On ne devance jamais le besoin.** Chaque notion arrive quand le projet la réclame — et on
   accepte que le calendrier en souffre.
