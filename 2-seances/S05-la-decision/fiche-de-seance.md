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
| **12 h 15 - 12 h 22** | **Quiz flash** : texte ou nombre | 7 min |
| **12 h 22 - 12 h 35** | **Je montre** : le compteur `tour = tour + 1` | 13 min |
| **12 h 35 - 12 h 50** | **Vous faites** : le compteur de points | 15 min |
| **12 h 50 - 13 h** | **Je montre** : les opérateurs, les deux familles | 10 min |
| **13 h - 13 h 10** | Pause | 10 min |
| **13 h 10 - 13 h 25** | **Je montre** : `if` / `else`, et l'`IndentationError` | 15 min |
| **13 h 25 - 13 h 52** | **Vous faites** : LE PROJET — numéroter, compter, vérifier | 27 min |
| **13 h 52 - 14 h** | Clôture | 8 min |

**La règle du jour : 13 h 25, le projet commence.** S'il faut couper, on coupe le compteur de points —
c'est un échauffement, le projet le refait travailler de toute façon.

---

## 2. Ce qu'on ouvre, et quand

Tout est dans **[`../S04-le-jeu-compte/`](../S04-le-jeu-compte/fiche-de-seance.md)** : rien à refaire.

| Moment | Le fichier |
|---|---|
| 12 h 15 | [`a-projeter/quiz-rappel.pptx`](a-projeter/quiz-rappel.pptx) — **le seul fichier neuf d'aujourd'hui** |
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

### 3.1 · 12 h 15 - 12 h 22 — Le quiz flash

6 questions, les cartes de couleur. Elles reprennent **exactement** le tableau de samedi dernier :
`"3" + "4"`, `3 + 4`, `"3" + 4`, l'`input` qui rend du texte, la ligne `int()` qui répare, et `str()`
dans une phrase.

**La dernière diapo est le tableau complet**, à laisser affiché pendant le début de séance.

> **On ne commente aucun résultat individuel du test envoyé mercredi.** Le score est pour vous.

### 3.2 · 12 h 35 - 12 h 50 — Vous faites : le compteur de points

Nouveau fichier, `compteur.py`. Au tableau, les quatre étapes :

1. crée un compteur `points` qui part de **zéro**, et affiche-le ;
2. ajoute 1 **trois fois**, en affichant après chaque ajout — tu dois voir `1`, `2`, `3` ;
3. demande au joueur **combien de points il marque**, transforme sa réponse en **nombre**, et
   ajoute-les au compteur ;
4. affiche `Total : …` — attention, il faudra `str()`.

**Carte bleue :** *« demande un deuxième score, ajoute-le aussi, et affiche combien il manque pour
atteindre 20. »*

**Aucune notion nouvelle** : c'est le compteur de tout à l'heure, plus `int()` et `str()` de samedi
dernier. L'élève qui bute sur l'étape 3 n'a pas compris le compteur — c'est exactement ce qu'on veut
repérer avant le projet.

---

## 4. Le reste du déroulé

Il est **inchangé**, dans la fiche de la séance 4 :

- **le compteur** → [§ 3.5](../S04-le-jeu-compte/fiche-de-seance.md) (la boîte, les papiers, « range dans »)
- **les opérateurs et `if` / `else`** → [§ 3.7](../S04-le-jeu-compte/fiche-de-seance.md), les cinq temps a) à e)
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
4. **Le [dictionnaire des erreurs](../../1-methode/annexes/A6-dictionnaire-des-erreurs.md)** : cocher
   `IndentationError` et le `=` / `==`.
