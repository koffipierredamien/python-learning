# Annexe A6 — Le dictionnaire des erreurs

**La règle, répétée à chaque séance :** le rouge n'est pas une punition. **Le rouge est une information** —
l'ordinateur explique ce qu'il n'a pas compris, et il montre la ligne.

Cette fiche est **complète pour tout le parcours** : elle ne s'affiche plus en classe et **ne se réimprime
pas à chaque séance**. L'enseignant la garde, et **coche la case quand l'erreur a été traitée** avec la
classe. Ce qui n'est pas coché est ce qui reste à voir.

La version à imprimer, avec la colonne à cocher : **[`dictionnaire-des-erreurs.pdf`](dictionnaire-des-erreurs.pdf)**.

---

## 1. Les erreurs d'écriture — dès le premier contact machine

| ✓ | Ce que l'ordinateur écrit | Ce qu'il veut dire | Ce que je fais | Vers |
|---|---|---|---|---|
| ☐ | `SyntaxError: invalid syntax` | « Je ne comprends pas ta phrase » | Je relis la ligne indiquée **et celle juste avant** : parenthèse, guillemet ou deux-points manquants | S2 |
| ☐ | `SyntaxError: unterminated string literal` | « Ton texte n'est jamais refermé » | Il manque un guillemet `"` — ils vont par deux | S2 |
| ☐ | `SyntaxError: '(' was never closed` | « Tu as ouvert une parenthèse et tu ne l'as pas fermée » | Je ferme la parenthèse | S2 |
| ☐ | `NameError: name '…' is not defined` | « Je ne connais pas ce mot » | Faute de frappe, majuscule en trop, ou du texte écrit **sans guillemets** | S2 |
| ☐ | Rien ne se passe quand j'appuie sur F5 | J'ai écrit dans la zone du bas, celle où l'ordinateur répond | Je remonte dans la zone blanche, en haut | S2 |
| ☐ | `SyntaxError` sur une ligne qui semble juste | L'erreur est presque toujours **sur la ligne d'avant** | Je regarde la ligne précédente | S3 |

## 2. Les variables et ce que tape le joueur

| ✓ | Ce que l'ordinateur écrit | Ce qu'il veut dire | Ce que je fais | Vers |
|---|---|---|---|---|
| ☐ | `TypeError: can only concatenate str (not "int") to str` | « Tu mélanges du texte et un nombre » | J'utilise une virgule dans le `print`, ou `str(mon_nombre)` | S3 |
| ☐ | `ValueError: invalid literal for int() with base 10` | « Tu m'as demandé un nombre, et j'ai reçu du texte » | Le joueur a tapé autre chose qu'un chiffre : je vérifie avant de convertir | S4 |
| ☐ | `TypeError: unsupported operand type(s) for +: 'int' and 'str'` | « Je ne peux pas additionner un nombre et du texte » | `input()` rend **toujours** du texte : je convertis avec `int()` | S4 |
| ☐ | Le programme attend et ne répond plus | Il attend une réponse du joueur (`input`) | Je clique dans la zone du bas et je tape ma réponse, puis Entrée | S3 |

## 3. L'indentation — le décalage du début de ligne

| ✓ | Ce que l'ordinateur écrit | Ce qu'il veut dire | Ce que je fais | Vers |
|---|---|---|---|---|
| ☐ | `IndentationError: expected an indented block` | « Après les deux-points, il faut décaler » | Je décale la ligne de **4 espaces** | S7 |
| ☐ | `IndentationError: unexpected indent` | « Cette ligne est décalée sans raison » | Je la remets au bord | S7 |
| ☐ | `TabError` | « Tu mélanges tabulations et espaces » | J'efface le début de la ligne et je remets **4 espaces** | S7 |

## 4. Les listes et le plateau

| ✓ | Ce que l'ordinateur écrit | Ce qu'il veut dire | Ce que je fais | Vers |
|---|---|---|---|---|
| ☐ | `IndexError: list index out of range` | « Cette case n'existe pas » | Une liste de 9 cases va de **0 à 8**, pas de 1 à 9 | S8 |
| ☐ | `TypeError: 'int' object is not subscriptable` | « Ça, ce n'est pas une liste » | Je vérifie que la variable contient bien une liste | S8 |
| ☐ | Le plateau ne change pas | J'ai modifié une copie, pas la liste elle-même | Je modifie directement `plateau[i]` | S9 |

## 5. Les conditions, les boucles et les fonctions

| ✓ | Ce que l'ordinateur écrit | Ce qu'il veut dire | Ce que je fais | Vers |
|---|---|---|---|---|
| ☐ | `SyntaxError` sur un `if` | J'ai écrit `=` au lieu de `==` | `=` donne une valeur, `==` compare deux valeurs | S10 |
| ☐ | Le programme ne s'arrête plus | Boucle sans fin : la condition reste vraie | `Ctrl + C` dans la zone du bas, puis je corrige ce qui doit changer dans la boucle | S11 |
| ☐ | `TypeError: … missing 1 required positional argument` | « Il manque quelque chose entre les parenthèses » | Je regarde ce que la fonction attend | S12 |
| ☐ | `UnboundLocalError` | « Tu utilises une variable avant de lui donner une valeur » | Je crée la variable avant de m'en servir | S13 |
| ☐ | `TypeError: 'str' object is not callable` | J'ai donné à une variable le nom d'une commande | Je renomme ma variable (jamais `print`, `list`, `str`…) | S13 |

## 6. La fenêtre graphique

| ✓ | Ce que l'ordinateur écrit | Ce qu'il veut dire | Ce que je fais | Vers |
|---|---|---|---|---|
| ☐ | `ModuleNotFoundError: No module named 'tkinter'` | « Je n'ai pas la boîte à outils des fenêtres » | Python mal installé sur ce poste : je change de machine et je le signale | S15 |
| ☐ | La fenêtre s'ouvre et se referme aussitôt | Il manque la dernière ligne | `fenetre.mainloop()` en fin de programme | S15 |
| ☐ | `_tkinter.TclError: unknown color name` | « Cette couleur n'existe pas » | J'écris la couleur en anglais, ou en code `#RRGGBB` | S17 |
| ☐ | Le bouton se déclenche tout seul au démarrage | J'ai mis les parenthèses à la fonction | `command=jouer` et non `command=jouer()` | S16 |

---

## Comment s'en servir en classe

1. **On ne l'affiche pas au mur.** L'enseignant l'a sous la main, c'est tout.
2. Quand une erreur tombe en classe, **on la traite devant tout le monde** : on lit le message à voix haute,
   on dit ce qu'il veut dire, on corrige. Puis **on coche la case**.
3. Les séances indiquées dans la colonne « Vers » sont une **prévision**, pas un programme : une erreur se
   traite le jour où elle arrive, même bien avant.
4. Une erreur qui n'est pas dans la liste s'ajoute à la main, en bas de la fiche imprimée.
