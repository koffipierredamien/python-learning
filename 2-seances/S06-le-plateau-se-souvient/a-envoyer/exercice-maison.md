# 🔐 Exercice de maison — LE COFFRE-FORT

**Pour les enfants qui ont un ordinateur à la maison.** À envoyer **le mercredi 21 octobre**,
à rendre **samedi 24**. Comptez **45 min à 1 h**.

| | |
|---|---|
| **L'exercice, en images** | [page 1](exercice-maison-le-coffre-fort-1.png) · [page 2](exercice-maison-le-coffre-fort-2.png) |
| **…et en PDF, pour imprimer** | [`exercice-maison-le-coffre-fort.pdf`](exercice-maison-le-coffre-fort.pdf) |
| **La correction** | [page 1](correction-le-coffre-fort-1.png) · [page 2](correction-le-coffre-fort-2.png) · [PDF](correction-le-coffre-fort.pdf) · [`.py`](correction-coffre-fort.py) |
| **Pour ceux qui n'ont pas d'ordinateur** | le **[quiz de la semaine n°5](quiz-semaine.md)**, à la place |

> **La correction ne part qu'après** le retour des copies.

---

## Ce que c'est

Un coffre à **cinq tiroirs**. Joueur 2 cache un trésor, joueur 1 a **deux essais**, et le programme
**garde la trace** des tiroirs ouverts : `X` pour un tiroir vide, `T` pour le trésor.
Score de départ 50, **−20 par tiroir vide**.

**Pourquoi ce jeu et pas un autre :** c'est **le plateau du XO en plus petit**. Une liste, un indice
`−1`, une écriture dans la liste, un affichage qui change. Quand ils reviendront au jeu samedi, ils
auront déjà écrit tout ça — avec des tiroirs au lieu de cases.

## Ce que l'exercice fait réviser

**Aucune notion nouvelle.** Tout vient des séances 1 à 6.

| Notion | Où elle sert |
|---|---|
| `print`, le cadre `"=" * 34`, le `+` qui colle | étapes 1 et 4 |
| `input` et la variable | étape 2 |
| **`int()`** pour comparer des nombres | étapes 2 et 4 |
| **`str()`** pour écrire un nombre dans une phrase | étape 6 |
| **le compteur à l'envers** `points = points - 20` | étapes 3 à 5 |
| **`if` / `else`** | étapes 4, 5 et 6 |
| 🆕 **la liste** `tiroirs = [...]` | étape 1 — **la notion de samedi** |
| 🆕 **l'indice** `tiroirs[essai - 1]` | étapes 4 et 5 — **le cœur de l'exercice** |

## Les six choses à regarder dans une copie

1. **La liste a-t-elle cinq cases**, entre **crochets**, séparées par des virgules ?
2. L'affichage utilise-t-il `tiroirs[0]` à `tiroirs[4]` — et pas `[1]` à `[5]` ?
3. **Le `- 1` est-il présent** dans `tiroirs[essai - 1]` ? *(c'est la faute n° 1, et elle est normale)*
4. `points = 50` est-il **avant** les essais, et **une seule fois** ?
5. `points = points - 20` est-il **dans le `else`**, donc décalé ?
6. Les `str()` sont-ils là dans le verdict ?

> **Le bug le plus instructif :** `tiroirs[essai]` au lieu de `tiroirs[essai - 1]`. **Python ne dit rien**
> — la marque se pose simplement à côté. C'est exactement le bug qu'ils auront dans le jeu XO.
> **Faites-le-leur découvrir en jouant**, pas en relisant.

## Le bonus ⭐⭐ : le tiroir déjà ouvert

Le second bonus demande de refuser un tiroir déjà ouvert, en vérifiant qu'il **contient encore son
numéro** : `if tiroirs[essai - 1] == str(essai):`.

**C'est mot pour mot la leçon de la séance 7.** L'élève qui le réussit arrive samedi avec une séance
d'avance : **dites-le devant la classe**, et demandez-lui de l'expliquer lui-même au tableau. C'est
le meilleur démarrage possible pour la séance 7.

## Le message aux parents

```
Bonjour, et que la paix soit avec vous.

Voici un exercice pour les enfants qui ont un ordinateur à la maison.
Votre enfant va programmer un jeu : « Le Coffre-Fort ». L'un cache un
trésor dans un des cinq tiroirs, l'autre a deux essais pour le
trouver, et le programme marque les tiroirs déjà ouverts.

Toutes les instructions sont sur les deux images, étape par étape.
Comptez environ une heure. Ce n'est pas noté : c'est pour s'entraîner.

Et quand ça marchera, jouez une partie avec lui. C'est le meilleur
moment de l'exercice.

Qu'il nous envoie ensuite une photo de son écran — nous en
reparlerons samedi. S'il n'y arrive pas entièrement, qu'il envoie
quand même ce qu'il a fait : c'est là-dessus que nous travaillerons.

👉 LES DEUX IMAGES DE L'EXERCICE

Merci pour votre aide, et à samedi 12 h.
AcProKids Coding Camp — Vision Plénitudes Vie
```

> **Pour les enfants sans ordinateur :** ils font le [quiz de la semaine](quiz-semaine.md), et
> l'exercice sera refait **en classe** sur les postes. Rien de tout cela n'entre dans une note.

---

## Vérification faite

Le corrigé [`correction-coffre-fort.py`](correction-coffre-fort.py) **a été exécuté**, sur les deux
chemins : trésor trouvé au 1ᵉʳ essai (**30 / 50**, « PILLEUR DE COFFRE-FORT ! ») et jamais trouvé
(**10 / 50**, « Le coffre a resiste... »). Les marques tombent dans les bons tiroirs.
