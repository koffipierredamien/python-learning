# 📝 Test n°2 — le formulaire d'exercices noté

**20 points : 12 questions « que va afficher ce programme ? » + 8 exercices où l'élève tape du code.**
Aucun ordinateur n'est nécessaire, on peut répondre depuis un téléphone. Comptez 20 à 25 minutes.

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
| 1 · affiche Bonjour | `print("Bonjour")` · `print('Bonjour')` |
| 2 · le mot qui manque | `input` · `input()` |
| 3 · le signe qui manque | `+` |
| 4 · ranger Joyce dans nom | `nom = "Joyce"` · `nom="Joyce"` · `nom = 'Joyce'` · `nom='Joyce'` |
| 5 · ranger 15 dans age | `age = "15"` · `age="15"` · `age = '15'` · `age='15'` |
| 6 · réparer print("Bonjour) | `print("Bonjour")` · `print('Bonjour')` |
| 7 · réparer Print("Salut") | `print("Salut")` · `print('Salut')` |
| 8 · les deux lignes | **à corriger à la main** — les variantes sont trop nombreuses |

> **L'exercice 8 reste manuel**, c'est normal : c'est une réponse longue. Google affichera la copie,
> vous mettez 1 ou 0. L'élève voit de toute façon la réponse attendue dans le retour.

Puis, dans **⚙️ Paramètres → Questionnaire** : « publier les notes » **immédiatement après chaque envoi**.

> 🔴 **Le réglage qui décide de tout.** Tant que « Publier les notes » est sur *Plus tard, après examen
> manuel*, l'élève ne voit que « Votre réponse a été enregistrée » : **ni note, ni corrigé**. Il faut
> aussi cocher les trois cases de **« Le participant peut voir »** : *Questions manquées · Bonnes
> réponses · Valeurs des points*. Apps Script n'expose pas ces réglages — c'est à faire à la main, une
> fois par formulaire. **Vérifiez en répondant vous-même : le bouton « Afficher le score » doit apparaître.**

Et dans **Réponses → lier à Sheets** pour recevoir tous les scores dans une feuille.

---

## 2. Le message aux parents

```
Bonjour, et que la paix soit avec vous.

Voici le test de révision de la semaine pour votre enfant. Il reprend
tout ce que nous avons vu depuis le début, et surtout le TP de samedi.

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

## 3. Partie A — les réponses

| # | Le programme | Réponse | Ce qui est testé |
|---|---|---|---|
| 1 | `a = 3` / `a = 5` / `print(a)` | **5** | La boîte ne garde que la dernière valeur |
| 2 | `a = 4` / `b = 5` / `b = a` / `print(b)` | **4** | La copie écrase le contenu de b |
| 3 | idem, mais `print(a)` | **4** | Copier ne vide pas la boîte source |
| 4 | `a="X"` / `b="O"` / `a=b` / `b=a` | **O puis O** | **Le piège de l'échange** — le X est perdu dès la 3ᵉ ligne |
| 5 | `nom = "Joyce"` / `print("nom")` | **nom** | Les guillemets : le mot, pas le contenu |
| 6 | `x="3"` / `y="4"` / `print(x + y)` | **34** | Le `+` sur du texte colle, il n'additionne pas |
| 7 | `print("Bonjour" + nom)` | **BonjourJoyce** | L'espace manquant |
| 8 | trois `print` à la suite | **Un, Deux, Trois** | De haut en bas, ligne par ligne |
| 9 | `input` puis `print("Salut " + prenom)` | **Salut Gedeon** | Ce que tape le joueur est rangé dans la boîte |
| 10 | `age` réécrit trois fois | **17** | Chaque ligne écrase la précédente |
| 11 | `nom` rangé, `Nom` affiché | **NameError** | Majuscule : ce n'est pas la même boîte |
| 12 | `print("Bonjour)` | **SyntaxError** | Le guillemet fermant |

**Les questions 4 et 6 sont les plus instructives.** La 4, c'est exactement le défi ⭐ du TP : si beaucoup
se trompent, c'est normal — mais c'est le signe qu'il faut y revenir cinq minutes samedi, au tableau, avec
trois boîtes dessinées. La 6 annonce la conversion des nombres, qu'on verra plus tard.

## 4. Partie B — les réponses

```python
1)  print("Bonjour")
2)  input
3)  +
4)  nom = "Joyce"
5)  age = "15"
6)  print("Bonjour")
7)  print("Salut")
8)  joueur = input("Ton nom ? ")
    print("Bonjour " + joueur)
```

> **Tous ces programmes ont été exécutés pour vérifier les réponses**, y compris les deux erreurs :
> `NameError: name 'Nom' is not defined` et `SyntaxError: unterminated string literal`.

---

## 5. Après

Les scores arrivent dans la feuille liée au formulaire. Dans le classeur, onglet **`Révisions maison`**,
on note `O` ou `N` dans la colonne `S03-1`.

**Le score ne sert qu'à vous.** Il ne se lit pas à voix haute et ne se compare pas devant le groupe :
c'est un thermomètre pour savoir quoi reprendre, pas une note de bulletin.
