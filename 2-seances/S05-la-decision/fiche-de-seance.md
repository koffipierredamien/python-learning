# Séance 5 — « Le jeu compte et décide »

> **C'est la suite directe de la séance 4.** Samedi dernier, seule la première notion a été traitée :
> *texte ou nombre*. Les deux autres — **le compteur** et **la décision** — sont pour aujourd'hui.
> Tout le matériel existe déjà : il est dans le dossier de la séance 4, on ne refait rien.

---

## 0. Carte d'identité

| | |
|---|---|
| **Numéro** | 5 / 22 — Phase 1 « Parler au joueur » |
| **Date** | samedi 10 octobre 2026 · **12 h - 14 h** |
| **Déjà acquis** | `print`, les variables, `input`, le `+`, **`int()` et `str()`** et le tableau des types |
| **Au programme** | **le compteur** `tour = tour + 1` · **les opérateurs** de comparaison · **`if` / `else`** |
| **Brique projet** | Le plateau numéroté, le compteur de tours, et **la case qui n'existe pas est refusée** |
| **Point de départ** | Le code de la séance 3 (celui du TP) |

### Ce qui a changé par rapport au plan

Rien dans le contenu : **le découpage seulement**. La séance 4 prévoyait trois notions en deux heures,
elle en a fait une. On garde les deux autres, avec **plus d'air** : le projet passe de 22 à 27 minutes.

---

## 1. Le programme de la séance

| Horaire | Séquence | Durée |
|---|---|---|
| **12 h - 12 h 15** | Prière et accueil | 15 min |
| **12 h 15 - 12 h 50** | 🧭 **LE GRAND PARCOURS** — les 8 paliers, en autonomie | **35 min** |
| **12 h 50 - 13 h** | **Je montre** : le compteur — *on part du palier 7* | 10 min |
| **13 h - 13 h 10** | Pause | 10 min |
| **13 h 10 - 13 h 20** | **Je montre** : les opérateurs, les deux familles | 10 min |
| **13 h 20 - 13 h 35** | **Je montre** : `if` / `else` — *on part du palier 8* — et l'`IndentationError` | 15 min |
| **13 h 35 - 13 h 52** | **Vous faites** : LE PROJET — numéroter, compter, vérifier | 17 min |
| **13 h 52 - 14 h** | Clôture | 8 min |

### Ce que le parcours remplace

Il prend la place du **quiz flash** (il révise la même chose, en mieux : les doigts sur le clavier) et de
l'atelier **« compteur de points »** (les paliers 7 et 8 font le même travail, en découverte).
**Gardez le quiz** [`a-projeter/quiz-rappel.pptx`](a-projeter/quiz-rappel.pptx) : sa **dernière diapo**
est le tableau `texte / nombre`, à projeter pendant les paliers 5 et 6.

### Les deux règles de temps

1. **12 h 50, on s'arrête**, fini ou pas. Le parcours n'est pas une course : ce qui n'est pas fait n'est
   pas grave, c'est de la révision.
2. **Si le parcours déborde jusqu'à 13 h**, on coupe dans la leçon des opérateurs (quatre signes au lieu
   de six) — **jamais dans le `if` / `else`**. Et si le projet ne tient pas, **il passe à samedi
   prochain** : on distribue quand même le code officiel à 13 h 50, le Filet joue son rôle.

---

## 2. Ce qu'on ouvre, et quand

Tout est dans **[`../S04-le-jeu-compte/`](../S04-le-jeu-compte/fiche-de-seance.md)** : rien à refaire.

| Moment | Le fichier |
|---|---|
| 12 h 15 | 🧭 [`a-imprimer/1-parcours-revision.pdf`](a-imprimer/1-parcours-revision.pdf) — **1 par élève, recto-verso** |
| 12 h 15 → 12 h 50 | [`a-projeter/parcours-tableau-de-bord.pptx`](a-projeter/parcours-tableau-de-bord.pptx) — 3 diapos, **la 2ᵉ reste affichée** |
| sur chaque poste | [`code/parcours_depart.py`](code/parcours_depart.py) → enregistré sous `parcours_tonprenom.py` |
| pour vous, la veille | [`code/parcours_corrige.py`](code/parcours_corrige.py) — les 8 paliers et les 3 défis, **il tourne** |
| pendant les paliers 5-6 | la **dernière diapo** de [`a-projeter/quiz-rappel.pptx`](a-projeter/quiz-rappel.pptx) : le tableau texte / nombre |
| 12 h 22 → 13 h 25 | [le diaporama de la séance 4](../S04-le-jeu-compte/a-projeter/seance-4-projection.pptx) — **on démarre au séparateur « 2 · Le compteur »**, on saute les diapos de `int()` / `str()` |
| la veille, à voix haute | [l'anti-sèche](../S04-le-jeu-compte/code/live_coding_antiseche.py) — **étapes D à G seulement** |
| 1 par poste | [l'aide-mémoire](../S04-le-jeu-compte/a-imprimer/1-aide-memoire.pdf) — il porte déjà les trois notions |
| sur chaque poste | [`depart_eleves_piste_bleue.py`](../S04-le-jeu-compte/code/depart_eleves_piste_bleue.py) → `GEEKS/mon_xo/jeu.py` |
| à 13 h 50 | [`code_officiel_fin_de_seance.py`](../S04-le-jeu-compte/code/code_officiel_fin_de_seance.py) → `GEEKS/xo_officiel/` |

**Au tableau avant leur arrivée, et on n'efface pas :**

```
=    range dans          age = 15
==   est egal a ?        age == 15
```

---

## 3. Les deux blocs neufs

### 3.1 · 12 h 15 - 12 h 50 — 🧭 Le Grand Parcours

**C'est le bloc neuf de la séance.** Les élèves travaillent **seuls**, à leur rythme, sur un seul
fichier. Vous circulez, vous ne vous asseyez pas, **vous ne touchez aucun clavier**.

**Le lancement, en deux minutes :** on distribue la feuille, on lit les quatre règles à voix haute, on
projette la diapo 2 (le tableau de bord), et on part.

| Palier | Ce qu'il révise | Durée |
|---|---|---|
| **1** · Afficher | `print`, plusieurs lignes, `"-" * 30` | 3 min |
| **2** · La boîte | la variable, et `print(x)` contre `print("x")` | 4 min |
| **3** · Coller | le `+`, et l'espace qui ne se met pas tout seul | 4 min |
| **4** · Demander | `input`, et l'espace avant le guillemet | 5 min |
| **5** · Texte ou nombre | le tableau des types, **et l'erreur provoquée exprès** | 6 min |
| **6** · L'âge | `int()` à l'entrée **et** `str()` à la sortie | 6 min |
| **7** · Le compteur | ⚡ **découverte** : ils tapent, ils prédisent, on n'explique pas | 4 min |
| **8** · La décision | ⚡ **découverte** : `if` / `else` recopié, lancé deux fois | 3 min |

**Les paliers 7 et 8 sont le cœur du dispositif.** Les élèves y découvrent **seuls**, sans explication,
les deux notions du jour. On ne corrige pas, on ne commente pas : **on les laisse constater**, et la
leçon de 12 h 50 vient répondre à une question qu'ils se posent déjà.

**Ce que vous regardez en circulant** (c'est aussi écrit en bas du corrigé) :

| Palier | La question |
|---|---|
| 2 | sait-il **dire** la différence `print(x)` / `print("x")` ? |
| 5 | sait-il **nommer** l'erreur (`TypeError`) avant de la réparer ? |
| 6 | met-il `int()` à l'entrée **et** `str()` à la sortie ? |
| 7 | a-t-il prédit **2**, ou a-t-il dit 1 ? — **notez les noms** |
| 8 | le décalage de 4 espaces est-il là **sans aide** ? |

**Les trois défis ⭐** (au dos de la feuille) occupent les plus rapides : la fiche du joueur encadrée, le
compteur de scores, le contrôle d'âge. **Personne n'est en retard s'il ne les fait pas.**

> **On ne commente aucun résultat individuel du test envoyé mercredi.** Le score est pour vous.

---

## 4. Le reste du déroulé

Il est **inchangé**, dans la fiche de la séance 4 :

- **le compteur** → [§ 3.5](../S04-le-jeu-compte/fiche-de-seance.md) (la boîte, les papiers, « range dans ») —
  **ouvrez en demandant : « au palier 7, qui avait prédit 2 ? »**
- **les opérateurs et `if` / `else`** → [§ 3.7](../S04-le-jeu-compte/fiche-de-seance.md), les cinq temps a) à e) —
  **ouvrez en demandant : « au palier 8, qui a vu le programme changer d'avis ? »**
- **le projet, ses 8 étapes et ses 7 erreurs** → [§ 3.8](../S04-le-jeu-compte/fiche-de-seance.md)
- **la clôture et les plans de secours** → [§ 3.9 et § 4](../S04-le-jeu-compte/fiche-de-seance.md)

**La dernière phrase**, à la place de celle de la séance 4 :

> « Votre jeu sait compter, et il sait refuser. Mais il oublie tout : si Joyce joue la case 5, il ne s'en
> souvient pas. Samedi prochain, **le plateau va se souvenir des coups joués.** À samedi, les Geeks ! »

---

## 5. Après la séance, le soir même

1. **Le classeur** : présence `S05`, la production de chacun dans `Suivi`.
2. **L'onglet `Journal`** : **combien ont écrit un `if` / `else` qui marche sans aide.** C'est la mesure
   de la séance.
3. **L'onglet `Révisions maison`** : colonne `S05`, qui a rendu le devoir de mercredi.
4. **Les feuilles de parcours restent aux élèves** — mais **lisez le bas de leur page 2 avant qu'ils
   partent** : « ce que je n'ai pas bien compris depuis le premier samedi ». C'est ce qui ouvrira la séance 6.
5. **Le [dictionnaire des erreurs](../../1-methode/annexes/A6-dictionnaire-des-erreurs.md)** : cocher
   `IndentationError` et le `=` / `==`.
