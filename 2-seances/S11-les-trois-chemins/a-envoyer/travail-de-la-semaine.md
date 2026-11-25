# 📱 Le travail de la semaine — le quiz et l'exercice

Deux documents partent ensemble. Ils ne font pas la même chose :

| | Pour quoi faire | Pour qui |
|---|---|---|
| 🧠 **Le quiz de rappel** | Revoir **tout** ce qui a été vu, du premier jour jusqu'à l'ordre des conditions | **Tout le monde.** Un téléphone suffit |
| 🏅 **L'exercice — La Médaille** | Réfléchir sur `if` / `else`, puis **écrire un programme sans aucune consigne de code** | Ceux qui ont un ordinateur |

---

## 🧠 Le quiz de rappel

| | |
|---|---|
| **Le script** | [`quiz-rappel-general.gs`](quiz-rappel-general.gs) — à coller dans [script.google.com](https://script.google.com) |
| **Format** | **20 questions à choix multiples, 20 points** |
| **Correction** | **100 % automatique** — *il n'y a aucun corrigé à coller à la main* |
| **Durée** | 20 à 25 minutes depuis un téléphone |

### Ce qu'il contient

| Partie | Ce qu'elle vérifie |
|---|---|
| **A — Parler, demander, compter** | le `+` qui colle, `input` qui rend du texte, le compteur, `str()` |
| **B — Décider : `if` et `else`** | le décalage, `>` contre `>=`, `==` contre `=`, un `else` à deux lignes |
| **C — La liste et le décalage** | l'indice qui commence à zéro, `case - 1`, `IndexError`, la case libre |
| **D — `and` et `or`** | il faut tout / il suffit d'un, et comment refuser un numéro impossible |
| **E — Plusieurs chemins : `elif`** | deux `if` contre une cascade, et **l'ordre : du plus précis au plus large** |

> **Ce qui n'y est pas : la répétition (`while`).** Elle n'a pas été introduite en classe, elle
> n'est donc pas demandée. Le quiz s'arrête exactement où la classe s'est arrêtée.

> **Le formulaire se suffit à lui-même.** Aucune question ne renvoie à une séance, à un atelier
> ni au projet : les listes sont redonnées à chaque fois, les programmes recopiés en entier, et
> aucune question ne dépend de la précédente. On peut le renvoyer tel quel plus tard, ou le
> donner à un enfant qui était absent.

### Les trois réglages à faire

1. **[script.google.com](https://script.google.com)** → Nouveau projet → effacer le code présent →
   coller **tout** le `.gs` → **▶ Exécuter** (autoriser à la première utilisation).
   Le journal affiche **le lien à envoyer**.
2. 🔴 **L'ÉTAPE QU'ON OUBLIE.** Ouvrez le formulaire → **⚙ Paramètres → Questionnaires** :
   « Publier les notes » sur **Immédiatement après chaque envoi**, et cochez **les trois cases**
   de « Le participant peut voir ». *Apps Script ne sait pas régler ça : quatre clics, une fois.*
   **Sans ces quatre clics, l'élève n'a ni note ni correction.**
3. **Recette :** répondez vous-même au formulaire. Le bouton **« Afficher le score »**
   doit apparaître, avec la note et les explications.

---

## 🏅 L'exercice — La Médaille

| | |
|---|---|
| **À envoyer** | [`exercice-la-medaille-1.png`](exercice-la-medaille-1.png) et [`exercice-la-medaille-2.png`](exercice-la-medaille-2.png) — les deux images, dans l'ordre |
| **En PDF** | [`exercice-la-medaille.pdf`](exercice-la-medaille.pdf) |
| **Le corrigé** | [`correction-la-medaille.py`](correction-la-medaille.py) — **il ne part pas** : il est pour vous et pour les parents |

**La feuille ne demande d'écrire nulle part dessus** : elle se lit sur un téléphone, et tout se
fait dans la tête puis dans Thonny.

**Ce qu'elle contient :** trois questions de réflexion sur `if` / `else` — l'ordre qui donne du
bronze à un 95, la cascade sans `else` qui ne répond rien, et un `if` dans un `if` à récrire avec
`elif` — puis **un programme à écrire sans aucune consigne de code** : seulement un barème, un
écran attendu et six essais qui doivent tomber juste.

### Les deux pièges, à ne pas annoncer

| L'essai | Ce qui se passe |
|---|---|
| **100** | Si le cas « exactement 100 » est écrit **après** `>= 90`, il n'est jamais atteint : l'enfant reçoit une médaille d'or au lieu d'aller en finale. **C'est l'ordre du plus précis au plus large, en situation.** |
| **0** | Qui écrit `points <= 0` pour l'impossible refuse le zéro. Or **on peut avoir zéro point sans tricher**. |

**Ne corrigez pas la ligne fautive.** Faites taper `100`, puis `0`, et faites lire l'écran à voix
haute. Ils trouvent seuls, et ils ne l'oublient plus.

---

## Le message à envoyer aux familles

```
Bonjour à tous, et que la paix soit avec vous.

Voici le travail de la semaine pour vos enfants. Il y a deux
choses, et aucune des deux n'est notée.

1. UN QUIZ, pour tout le monde. Vingt questions depuis un
   téléphone, environ vingt minutes. Il reprend tout ce qui a
   été vu depuis le début. L'enfant voit sa note et les
   explications tout de suite, et il peut le refaire autant de
   fois qu'il veut.
   Le lien : <COLLER LE LIEN ICI>

2. UN EXERCICE, pour ceux qui ont un ordinateur. Deux images
   jointes à ce message. Cette fois, on ne dit pas à l'enfant
   quoi écrire : on lui dit seulement ce que son programme doit
   faire, et c'est à lui de trouver comment. C'est exactement ce
   que nous travaillons en ce moment.
   Qu'il réfléchisse d'abord, et qu'il écrive en français ce que
   le programme doit faire, avant de toucher au clavier.

Quand son programme marche, il peut nous envoyer une photo de
son écran.

Merci de votre accompagnement.
```
