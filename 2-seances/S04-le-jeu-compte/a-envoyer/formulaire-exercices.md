# 📝 Test n°3 — « texte ou nombre »

**20 points : 12 questions « que va afficher ce programme ? » + 8 exercices où l'élève tape du code.**
Il ne porte que sur **la première notion de la séance 4** : `int()` et `str()`. Le compteur et le
`if` / `else` n'y sont pas — **ils n'ont pas encore été vus.**
Aucun ordinateur n'est nécessaire, on peut répondre depuis un téléphone. Comptez 20 minutes.

> **Le tableau de la classe est rappelé en haut du formulaire**, et chaque ligne est testée par au moins
> une question :
>
> | | |
> |---|---|
> | texte + texte | les deux sont collés — `"3" + "4"` → `34` |
> | texte + nombre | **TypeError** |
> | nombre + texte | **TypeError** |
> | nombre + nombre | une addition — `3 + 4` → `7` |
>
> Plus la règle qui déclenche tout : **`input()` rend toujours du texte.**

---

## 1. Fabriquer le formulaire

1. **[script.google.com](https://script.google.com)** → **Nouveau projet**.
2. Effacez le code présent, **collez tout [`formulaire-exercices.gs`](formulaire-exercices.gs)**.
3. Bouton **▶ Exécuter**, autorisez à la première utilisation.
4. Le journal affiche **le lien à envoyer** et le lien pour modifier.

### 🔴 ÉTAPE 5 — sans elle, l'élève ne voit AUCUNE correction

C'est le piège de Google Forms, et il est silencieux : le formulaire marche, les réponses arrivent,
mais **l'élève ne voit que « Votre réponse a été enregistrée »** — pas de note, pas de corrigé.

Ouvrez le formulaire → **roue dentée ⚙ Paramètres** → **Questionnaires** :

| Réglage | À mettre sur |
|---|---|
| **Publier les notes** | **Immédiatement après chaque envoi** *(et non « Plus tard, après examen manuel »)* |
| **Le participant peut voir** | cochez **les trois** : Questions manquées · Bonnes réponses · Valeurs des points |

> **Pourquoi le script ne le fait pas :** Apps Script n'expose pas ce réglage. Il n'existe aucune
> méthode pour le poser par programme — c'est quatre clics, une seule fois par formulaire.

**La recette, avant d'envoyer aux parents :** répondez vous-même au formulaire. Vous devez voir, après
l'envoi, **le bouton « Afficher le score »**, puis votre note et les corrigés. Si vous ne voyez pas ce
bouton, l'étape 5 n'a pas été faite.

### ⚠️ Et les 4 minutes à faire à la main

Les **12 questions de la partie A se corrigent toutes seules**. Les **8 exercices de la partie B** sont
des réponses libres : Google ne permet pas de fixer leur corrigé depuis un script. Sur chaque question :
**« Corrigé » → « Ajouter une réponse correcte »**, puis collez les réponses ci-dessous — **toutes les
variantes**, sinon un élève qui a juste sera compté faux.

| Exercice | Réponses à accepter |
|---|---|
| 1 · le mot qui transforme en nombre | `int` · `int()` |
| 2 · le mot qui transforme en texte | `str` · `str()` |
| 3 · réparer `print("Tour " + 3)` | `print("Tour " + str(3))` · `print("Tour " + str(3) )` · avec guillemets simples |
| 4 · réparer `print("J'ai " + 15 + " ans")` | `print("J'ai " + str(15) + " ans")` |
| 5 · ranger le nombre 7 | `tour = 7` · `tour=7` |
| 6 · les trois lignes de l'âge | **à corriger à la main** |
| 7 · afficher la somme | `print(a + b)` · `print(a+b)` |
| 8 · le programme complet | **à corriger à la main** |

> **Les exercices 6 et 8 restent manuels**, c'est normal : ce sont des réponses sur plusieurs lignes.
> Ce qu'on regarde dans le 6 : **la ligne `age = int(age)` est-elle là, et au bon endroit** (après la
> question, avant le calcul) ? Dans le 8 : `int()` à l'entrée **et** `str()` à la sortie.

Et dans **Réponses → lier à Sheets** pour recevoir tous les scores dans une feuille.

> **Les 8 exercices de la partie B restent « à corriger » tant que vous n'avez pas collé leur corrigé** —
> l'élève les voit alors à 0 point, en attente. C'est l'autre raison pour laquelle une copie peut sembler
> « sans réponse ».

---

## 2. Le message aux parents

```
Bonjour, et que la paix soit avec vous.

Voici le test de révision de la semaine pour votre enfant. Il porte sur
une seule chose, celle que nous avons travaillée samedi : savoir si on
a du texte ou un nombre entre les mains, et passer de l'un à l'autre.

Il y a deux parties : d'abord lire un programme et dire ce qu'il
affiche, ensuite écrire soi-même quelques lignes de code. Comptez
20 minutes. Aucun ordinateur n'est nécessaire, un téléphone suffit.

Le tableau que les enfants ont recopié en classe est rappelé en haut du
formulaire : ils peuvent l'avoir sous les yeux, ce n'est pas de la
triche, c'est l'outil.

Il aura sa note à la fin, avec les explications de ce qu'il n'a pas
trouvé. Se tromper n'est pas grave : c'est comme ça qu'on apprend.

👉 LIEN DU FORMULAIRE

Merci pour votre aide, et à samedi 12 h.
AcProKids Coding Camp — Vision Plénitudes Vie
```

---

## 3. Les réponses de la partie A

Toutes ont été **vérifiées en exécutant le code**.

| # | Le programme | Réponse | La ligne du tableau |
|---|---|---|---|
| 1 | `print("3" + "4")` | `34` | texte + texte |
| 2 | `print(3 + 4)` | `7` | nombre + nombre |
| 3 | `print("3" + 4)` | `TypeError` | texte + nombre |
| 4 | `print(3 + "4")` | `TypeError` | nombre + texte |
| 5 | `print(int("3") + 4)` | `7` | `int()` rend l'addition possible |
| 6 | `print("3" + str(4))` | `34` | `str()` rend la colle possible |
| 7 | `input` puis `age + 1` | `TypeError` | **`input` rend du texte** |
| 8 | `input`, `int()`, puis `age + 1` | `13` | la ligne `int()` règle tout |
| 9 | `print("Tour " + tour)`, `tour = 3` | `TypeError` | texte + nombre |
| 10 | `print("Total : " + str(5 + 3))` | `Total : 8` | on additionne, **puis** on colle |
| 11 | `int("douze")` | `ValueError` | `int()` veut un vrai nombre |
| 12 | `"10"` converti, puis `nombre + nombre` | `20` | sans `int()`, ce serait `1010` |

**Les trois questions qui séparent vraiment** sont les n° **7**, **10** et **12** : elles demandent de
suivre ce qu'il y a *dans la boîte* au fil des lignes, pas seulement de lire un signe `+`. Si elles sont
ratées en masse, le quiz flash de samedi repart de là.
