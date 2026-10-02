# 📝 Test n°3 — le formulaire d'exercices noté

**20 points : 12 questions « que va afficher ce programme ? » + 8 exercices où l'élève tape du code.**
Il porte sur la séance 4 : `int()` / `str()`, le compteur, **les opérateurs de comparaison** et `if` / `else`.
Aucun ordinateur n'est nécessaire, on peut répondre depuis un téléphone. Comptez 20 à 25 minutes.

> **À envoyer dans la semaine qui suit la séance 4** — le mercredi, comme les deux précédents.

---

## 1. Fabriquer le formulaire

1. **[script.google.com](https://script.google.com)** → **Nouveau projet**.
2. Effacez le code présent, **collez tout [`formulaire-exercices.gs`](formulaire-exercices.gs)**.
3. Bouton **▶ Exécuter**, autorisez à la première utilisation.
4. Le journal affiche **le lien à envoyer** et le lien pour modifier.

### ⚠️ Les 4 minutes à faire à la main

Les **12 questions de la partie A se corrigent toutes seules**. Les **8 exercices de la partie B** sont
des réponses libres : Google ne permet pas de fixer leur corrigé depuis un script, il faut l'ajouter
dans le formulaire. Sur chaque question : **« Corrigé » → « Ajouter une réponse correcte »**, puis collez
les réponses ci-dessous — **toutes les variantes**, sinon un élève qui a juste sera compté faux.

| Exercice | Réponses à accepter |
|---|---|
| 1 · le mot qui transforme en nombre | `int` · `int()` |
| 2 · le mot qui transforme en texte | `str` · `str()` |
| 3 · ajouter 1 au compteur | `tour = tour + 1` · `tour=tour+1` · `tour = tour+1` · `tour = 1 + tour` |
| 4 · la comparaison | `case > 9` · `case>9` |
| 5 · réparer `if age = 17:` | `if age == 17:` · `if age==17:` |
| 6 · réparer `if case > 9` | `if case > 9:` · `if case>9:` |
| 7 · les deux lignes du `if` | **à corriger à la main** — le décalage compte, les variantes sont trop nombreuses |
| 8 · le `if` / `else` complet | **à corriger à la main** — même raison |

> **Les exercices 7 et 8 restent manuels**, c'est normal : ce sont des réponses sur plusieurs lignes, et
> c'est justement **le décalage** qu'on veut voir. Google affichera la copie, vous mettez 1 ou 0.
> L'élève voit de toute façon la réponse attendue dans le retour.

**Ce qu'on regarde dans les exercices 7 et 8 :** les deux-points en fin de ligne, et **4 espaces** devant
la ligne qui suit. Un élève qui a mis 2 ou 3 espaces a compris l'idée : comptez juste, et notez-le dans
l'onglet `Révisions maison`.

Puis, dans **⚙️ Paramètres → Questionnaire** : « publier les notes » **immédiatement après chaque envoi**.
Et dans **Réponses → lier à Sheets** pour recevoir tous les scores dans une feuille.

---

## 2. Le message aux parents

```
Bonjour, et que la paix soit avec vous.

Voici le test de révision de la semaine pour votre enfant. Il reprend la
séance de samedi : les nombres et le texte, le compteur, et surtout les
décisions — le moment où le programme choisit tout seul ce qu'il fait.

Il y a deux parties : d'abord lire un programme et dire ce qu'il affiche,
ensuite écrire soi-même quelques lignes de code. Comptez 20 minutes.
Aucun ordinateur n'est nécessaire, un téléphone suffit.

Il aura sa note à la fin, avec les explications de ce qu'il n'a pas
trouvé. Se tromper n'est pas grave : c'est comme ça qu'on apprend.

👉 LIEN DU FORMULAIRE

Merci pour votre aide, et à samedi 12 h.
AcProKids Coding Camp — Vision Plénitudes Vie
```

---

## 3. Les réponses de la partie A

Pour corriger à la main en cas de besoin, et pour préparer le quiz flash de la séance 5.

| # | Le programme | Réponse | Ce qu'on vérifie |
|---|---|---|---|
| 1 | `a = "5"` puis `b = a + a` | `55` | texte collé, pas additionné |
| 2 | `print(age + 1)` après `input` | `TypeError` | `input` rend du texte |
| 3 | `int("12") + 1` | `13` | `int()` permet de calculer |
| 4 | trois fois `tour = tour + 1` | `3` | le compteur |
| 5 | `print(10 >= 10)` | `True` | `>=` = plus grand **ou égal** |
| 6 | `print(x == 4)` | `True` | l'opérateur `==` pose une question |
| 7 | `if age > 17 … else …` avec 20 | `Jeremiah` | **un seul** des deux chemins |
| 8 | `if age = 17:` | `SyntaxError` | le piège `=` / `==` |
| 9 | `if` sans décalage | `IndentationError` | les 4 espaces |
| 10 | un `print` décalé, un autre non | `grand puis fini` | ce qui appartient au `if` |
| 11 | `case = 12`, compteur dans le `else` | `0` | le coup refusé n'est pas compté |
| 12 | `"Tour " + tour` | `TypeError` | il manquait `str()` |

**Les trois questions les plus discriminantes sont les n° 9, 10 et 11.** Si elles sont massivement
ratées, le quiz flash de la séance 5 repart de là : **le décalage dit ce qui appartient au `if`.**
