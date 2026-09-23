# 📲 Le formulaire de révision de la semaine — séance 2

**12 questions notées sur 12.** L'élève a **son score et la correction dès qu'il envoie** ses réponses.
Aucun ordinateur n'est nécessaire : on peut répondre depuis le téléphone du parent, en dix minutes.

---

## 1. Fabriquer le formulaire — une fois, 5 minutes

Le fichier **[`formulaire-de-revision.gs`](formulaire-de-revision.gs)** construit tout le formulaire
automatiquement : les questions, les points, les bonnes réponses et les explications.

1. Ouvrez **[script.google.com](https://script.google.com)** → **Nouveau projet**.
2. Effacez le petit bout de code présent, et **collez tout le contenu du fichier `.gs`**.
3. Cliquez sur **Exécuter** (le bouton ▶). Google demande une autorisation la première fois : acceptez
   *(c'est votre propre compte qui crée un formulaire sur votre propre Drive)*.
4. En bas, le journal d'exécution affiche **deux liens** :
   - **le lien à envoyer aux parents** ;
   - le lien pour ouvrir et modifier le formulaire.

> **Si un bouton « Publier » apparaît** quand vous ouvrez le formulaire, cliquez dessus : depuis 2025,
> Google demande cette confirmation avant qu'un formulaire accepte des réponses.

### Deux réglages à vérifier dans le formulaire, avant d'envoyer

| Où | Quoi |
|---|---|
| ⚙️ **Paramètres → Questionnaire** | « Publier les notes » doit être sur **immédiatement après chaque envoi** |
| **Réponses → lier à Sheets** | Crée la feuille où toutes les réponses arrivent, avec le score de chacun |

---

## 2. Le message aux parents

```
Bonjour, et que la paix soit avec vous.

Voici le petit questionnaire de révision de la semaine pour votre enfant.
Il porte sur ce que nous avons fait samedi : afficher un message,
et faire en sorte que le programme demande son nom au joueur.

12 questions, environ 10 minutes, aucun ordinateur n'est nécessaire.
Il peut répondre depuis votre téléphone.

Il aura sa note tout de suite à la fin, avec l'explication de ce qu'il
n'a pas trouvé. Se tromper n'est pas grave : c'est comme ça qu'on apprend.

👉 LIEN DU FORMULAIRE

Merci pour votre aide, et à samedi 12 h.
AcProKids Coding Camp — Vision Plénitudes Vie
```

---

## 3. Les questions et les réponses — pour vous

| # | Question | Bonne réponse |
|---|---|---|
| 1 | Que fait la commande `print` ? | Elle affiche du texte à l'écran |
| 2 | Combien de guillemets autour d'un texte ? | Deux : un avant, un après |
| 3 | Dans Thonny, où écrit-on son programme ? | Dans la zone blanche, en haut |
| 4 | Comment lance-t-on son programme ? | F5, ou le bouton vert |
| 5 | L'ordinateur lit ton programme… | De haut en bas, ligne par ligne |
| 6 | `print("Bonjour)` devient rouge. Pourquoi ? | Il manque un guillemet |
| 7 | Quand l'écran devient rouge, cela veut dire… | Il t'explique ce qu'il n'a pas compris |
| 8 | `nom = "Damien"` puis `print(nom)` | **Damien** |
| 9 | `nom = "Damien"` puis `print("nom")` | **nom** |
| 10 | À quoi sert `input()` ? | Le programme pose une question et attend la réponse |
| 11 | `print("Bonjour " + nom + " !")` avec Joyce | Bonjour Joyce ! |
| 12 | À quoi sert le `+` ? | Il colle les morceaux bout à bout |

**Les questions 8 et 9 sont le cœur du test.** Elles séparent *la boîte* et *le mot* : c'est la confusion
numéro un de toute l'année. Si beaucoup se trompent, on rouvre la séance 3 là-dessus, deux minutes.

Une **dernière question, libre et non notée**, demande à l'élève ce qu'il n'a pas compris. C'est ce qui
prépare le mieux la séance suivante. Si vous n'en voulez pas, effacez le dernier bloc du fichier `.gs`.

---

## 4. Ce qu'on en fait après

- Les réponses arrivent dans la feuille liée au formulaire, **avec le score de chacun**.
- Dans le classeur de suivi, onglet **`Révisions maison`**, on note `O` pour ceux qui ont répondu,
  `N` pour les autres — colonne `S02-1`.
- **Le score ne sert qu'à vous.** Il ne se lit pas à voix haute, il ne se compare pas devant le groupe :
  c'est un thermomètre pour savoir quoi reprendre samedi, pas une note de bulletin.
