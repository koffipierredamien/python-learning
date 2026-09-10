# Annexe A5 — Outils imprimables

Tout ce qui doit être affiché au mur, plastifié ou photocopié avant la séance 1.

---

## 1. Les cartes de signalisation (1 jeu par binôme)

Quatre cartonnettes A6, à poser bien visibles sur l'écran ou l'unité centrale. Elles remplacent la main levée.

```
┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│                  │   │                  │   │                  │   │                  │
│       🟢         │   │       🟠         │   │       🔴         │   │       🔵         │
│                  │   │                  │   │                  │   │                  │
│   ÇA AVANCE      │   │  ON EST BLOQUÉS  │   │  RIEN NE MARCHE  │   │  ON A FINI !     │
│                  │   │  (on cherche     │   │  (au secours)    │   │  On peut aider   │
│                  │   │   quand même)    │   │                  │   │                  │
└──────────────────┘   └──────────────────┘   └──────────────────┘   └──────────────────┘
```

**Engagement des enseignants, annoncé aux élèves :** *« Une carte orange est servie en moins de 5 minutes. Une carte rouge, tout de suite. »*

---

## 2. Affiche — La règle des 3 avant moi

```
╔════════════════════════════════════════════════════════╗
║        BLOQUÉ ? 3 CHOSES AVANT DE LEVER LA CARTE       ║
╠════════════════════════════════════════════════════════╣
║                                                        ║
║   1️⃣  JE RELIS                                         ║
║       la consigne, puis le message d'erreur            ║
║       À VOIX HAUTE.                                    ║
║                                                        ║
║   2️⃣  JE DEMANDE À MON BINÔME                          ║
║       et on regarde la fiche mémo du jour.             ║
║                                                        ║
║   3️⃣  ON DEMANDE AU BINÔME D'À CÔTÉ                    ║
║       30 secondes, pas plus.                           ║
║                                                        ║
║   ➡️  Toujours bloqués ? CARTE ORANGE. 🟠              ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
```

---

## 3. Le contrat de binôme (signé à la séance 1, affiché toute l'année)

```
              ⚔️  CONTRAT DES GEEKS EN BINÔME  ⚔️

   1. Quand je suis COPILOTE, je ne touche pas le clavier.
      Je lis, je surveille, je propose.

   2. Quand je suis PILOTE, je dis à voix haute ce que je tape.

   3. Je ne dis jamais « t'es nul ».  Je dis « essaie ça ».

   4. Si mon binôme n'a pas compris,
      on ne passe pas à la suite.

   5. Une erreur, ce n'est pas une honte.
      C'est une information.

   6. On lève la carte ensemble, pas chacun de son côté.

   Signature :  ____________      ____________
```

---

## 4. Affiche — Le Dictionnaire des erreurs

À afficher **vide** à la séance 1 et à **remplir par les élèves** au fil des semaines (badge `Traducteur d'erreur`). Amorce recommandée :

| Le message de l'ordinateur | Ce que ça veut dire | Ce que je fais |
|---|---|---|
| `SyntaxError` | « Je ne comprends pas ta phrase » | Je vérifie les `:` , les `(` `)` , les guillemets |
| `IndentationError` | « Ton décalage est bizarre » | Je vérifie les 4 espaces au début de la ligne |
| `NameError: name 'x' is not defined` | « Tu me parles d'un mot que je ne connais pas » | Faute de frappe dans un nom, ou variable jamais créée |
| `TypeError` | « Tu mélanges du texte et des nombres » | J'utilise `int()` ou `str()` |
| `IndexError: list index out of range` | « Cette case n'existe pas dans ta liste » | Attention : la première case est la case **0** |
| `ValueError: invalid literal for int()` | « Tu m'as donné du texte, je voulais un nombre » | Je vérifie ce que le joueur a tapé |
| `KeyboardInterrupt` | « Tu as arrêté le programme toi-même » | Ce n'est pas un bug |
| `FileNotFoundError` | « Je ne trouve pas ce fichier » | Je vérifie le nom et le dossier |

---

## 5. Le journal de bord de l'élève (carnet A5, 1 page par séance)

```
  ┌────────────────────────────────────────────────────────┐
  │  SÉANCE N° ____        DATE : ____/____/____           │
  │  Mon binôme du jour : ______________________           │
  │                                                        │
  │  Aujourd'hui, mon jeu sait faire :                     │
  │  _____________________________________________         │
  │                                                        │
  │  Piste choisie :   🔵 Bleue    🔴 Rouge    ⚫ Noire     │
  │                                                        │
  │  Le mot Python que j'ai appris : ______________        │
  │                                                        │
  │  J'AI COMPRIS : ______________________________         │
  │                                                        │
  │  JE NE SUIS PAS ENCORE SÛR DE : ______________         │
  │                                                        │
  │  Mon bug le plus pénible :  ___________________        │
  │  Comment on l'a réparé :    ___________________        │
  │                                                        │
  │  Badges du jour : 🏅 ____________________________      │
  │                                                        │
  │  Mon humeur :   😀    🙂    😐    😕    😣            │
  └────────────────────────────────────────────────────────┘
```

> La ligne « je ne suis pas encore sûr de » est **l'outil de préparation le plus utile pour les enseignants**. Elle se recopie sur un post-it déposé dans la boîte en sortant, pour être lue le soir même.

---

## 6. Grille de test — la chasse aux bugs croisée

À remettre au binôme testeur. *« Votre mission : faire planter leur jeu. »*

```
  JEU TESTÉ — binôme : ______________     Testeurs : ______________

  ☐ Le jeu démarre sans erreur
  ☐ Les messages s'affichent sans faute d'orthographe
  ☐ Le plateau s'affiche correctement
  ☐ Je peux jouer un coup normal
  ☐ Je joue sur une case DÉJÀ PRISE → que se passe-t-il ?  __________
  ☐ Je tape une case qui n'existe pas (ex : 99) →           __________
  ☐ Je tape des LETTRES au lieu d'un chiffre →              __________
  ☐ Je n'écris RIEN et j'appuie sur Entrée →                __________
  ☐ Le jeu détecte bien le gagnant
  ☐ Le jeu détecte bien le match nul

  🏆 Notre bug préféré :  ___________________________________

  💬 Un compliment obligatoire sur leur jeu :  ______________
```

> **La ligne « compliment obligatoire » n'est pas décorative.** Elle transforme la critique du code en pratique bienveillante — exactement ce qu'est une revue de code entre professionnels.

---

## 7. Le tableau de suivi des enseignants

| Élève | Profil | S1 | S2 | S3 | S4 | S5 | … | Grade | Vigilance |
|---|---|---|---|---|---|---|---|---|---|
| | P0/P1/P2/P3 | ✔R | ~B | ✖ | ✔B | ✔R | | | ☐ liste des 10 min |

**Codes :** `✔` brique produite · `~` partielle · `✖` absent ou non produite · lettre = piste (B/R/N)
**Déclencheur :** deux `~` ou `✖` consécutifs → **liste des 10 minutes** (tête-à-tête de 10 min à la séance suivante, pendant l'atelier 2).

---

## 8. Modèle de message hebdomadaire aux familles

```
Bonjour à tous 👋

Séance 7 des Jerusalem Geeks aujourd'hui !

✅ Ce qu'on a appris : les boucles — comment demander à
   l'ordinateur de répéter quelque chose sans le réécrire.

🎮 Ce que leur jeu sait faire maintenant : les deux joueurs
   jouent chacun leur tour, et le plateau se met à jour.

🏅 Bravo à tous : chacun est reparti avec sa brique.

🎯 Défi facultatif (aucune obligation, et aucun retard si
   ce n'est pas fait) : demandez à votre enfant de vous
   expliquer ce qu'est une boucle. S'il y arrive, c'est
   qu'il a compris !

📅 Rendez-vous samedi prochain, 9h.
```

---

## 9. Affiche — Les 4 phrases de l'enseignant qui aide

À garder en tête, et à afficher côté enseignants.

```
   AIDER SANS FAIRE À LA PLACE

   1. « Lis-moi ton message d'erreur à voix haute. »

   2. « Montre-moi la ligne. Qu'est-ce que tu voulais
       qu'elle fasse ? »

   3. « Qu'est-ce qui se passerait si on mettait 5 ici ?
       Essaie. »

   4. « Explique-moi cette ligne comme si j'étais
       ton petit frère. »

   ⛔ NE JAMAIS PRENDRE LE CLAVIER DE L'ÉLÈVE.
```
