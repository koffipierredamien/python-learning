# 🎯 La révision générale du 14 novembre — conduite de séance

> **Le quiz, mais avec les mains sur le clavier.** Cinq manches : des questions à la carte, puis un
> atelier où ils tapent du code et où quelque chose ne marche pas. La dernière manche ne se corrige
> pas : elle **fabrique le besoin de la boucle**, et vous enchaînez sur votre leçon.

| | |
|---|---|
| **À projeter** | [`a-projeter/revision-generale.pptx`](a-projeter/revision-generale.pptx) — **38 diapos** |
| **Pour vous** | [`code/revision_ateliers_corrige.py`](code/revision_ateliers_corrige.py) — les cinq corrigés, **il tourne d'un bloc** |
| **Sur chaque poste** | Thonny ouvert, **un fichier neuf** : `revision.py`. **On ne touche pas au jeu aujourd'hui.** |
| **Durée** | **50 minutes** si tout passe — voir plus bas ce qu'on coupe |

> La version courte de 7 minutes reste disponible : [`a-projeter/quiz-rappel.pptx`](a-projeter/quiz-rappel.pptx).
> Elle sert les samedis ordinaires. Aujourd'hui, c'est la grande.

---

## 1. Le minutage

| Horaire | Manche | Ce qu'ils font | Durée |
|---|---|---|---|
| **12 h 15** | Ouverture et règle du jeu | — | 3 min |
| **12 h 18** | **1 · Texte ou nombre** | 2 cartes + *« Fais-lui dire 5 »* | 8 min |
| **12 h 26** | **2 · La liste et l'indice** | 2 cartes + *« Trois ordres, et un piège »* | 9 min |
| **12 h 35** | **3 · Le décalage décide de tout** | 2 cartes + *« Déplace une seule ligne »* | 10 min |
| **12 h 45** | **4 · `and`, `or` — et le piège** | 2 cartes + *« Le programme ment »* | 11 min |
| **12 h 56** | **5 · Le défi** | *« Affiche le plateau trois fois »* | 12 min |
| **13 h 08** | **La bascule** → votre leçon sur la boucle | — | 2 min |

**Si vous prenez du retard, voici l'ordre dans lequel on coupe :**
1. les **deux cartes** de la manche 3 (gardez l'atelier, c'est lui qui compte) ;
2. l'**atelier de la manche 2** (les deux cartes suffisent) ;
3. les **deux cartes** de la manche 1.

**Ce qu'on ne coupe jamais :** l'atelier de la manche 4 *(le bug du `or`)* et **toute la manche 5**.
La manche 5 n'est pas une révision — c'est l'ouverture de votre leçon.

---

## 2. La règle, à poser en ouverture

Deux sortes de questions, et la deuxième est nouvelle :

| | |
|---|---|
| 🃏 **La carte** | Je projette, tu réfléchis, **tout le monde lève sa carte en même temps**, au signal. |
| ⌨️ **Le clavier** | Tu tapes le code projeté, **tu prédis** ce qu'il va faire — carte en l'air — **et seulement après, tu lances.** |

> **Insistez sur la prédiction.** C'est elle qui vous dit ce qui est compris. Un élève qui lance avant
> de prédire ne se trompe jamais devant lui-même, et n'apprend donc rien. Dites-le une fois, en
> ouverture, et rappelez-le au premier qui lance trop vite.

---

## 3. Les cinq ateliers — ce qu'on cherche vraiment

| | Atelier | Le piège | Ce que ça vous dit |
|---|---|---|---|
| **1** | **Fais-lui dire 5** | Ils prédisent `5`, l'écran dit `23` | Qui a vraiment intégré que `input` rend du texte |
| **2** | **Trois ordres, et un piège** | *« Quel indice pour le sac 5 ? »* — et `sacs[5]` qui plante | Qui compte encore sur ses doigts |
| **3** | **Déplace une seule ligne** | Le score ne s'affiche que dans le `else` | **La faute n° 1 de leurs copies depuis la séance 5** |
| **4** | **Le programme ment** | `or` au lieu de `and` : il pose sur une case déjà prise | Qui sait lire une condition, et pas seulement l'écrire |
| **5** | **Trois fois le plateau** | Il n'y a pas d'astuce : il faut recopier | **Le chiffre qu'ils vont vous donner ouvre la leçon** |

### Les réponses, en une ligne chacune

1. `print(int(a) + int(b))` — ou bien deux lignes `a = int(a)` et `b = int(b)` avant. **Montrez les deux**,
   et dites que les deux sont justes : ils doivent sortir de l'idée qu'il n'y a qu'une bonne façon.
2. `sacs[2]` · `sacs[3] = "mais"` · `print(sacs)`. L'indice du sac 5 est **4**, et `sacs[5]` donne
   `IndexError` — **faites-le essayer en vrai**, et lisez le message rouge ensemble.
3. La ligne du score **recule de quatre espaces** : elle sort du `else` et se colle à gauche.
   **Rien d'autre ne change.** Faites venir quelqu'un faire le geste au tableau.
4. Le mot fautif est le **`or`**. Avec lui, `case >= 1` suffisait à tout rendre vrai, et le reste
   n'était même plus regardé. Après réparation : `5` → pose, `0` → refus, `12` → refus.
   **Le 0 est le plus parlant** : sans le `case >= 1`, le symbole irait dans la case 9.
5. Il n'y a pas de correction astucieuse. **18 lignes recopiées** pour trois affichages.

---

## 4. La manche 5, et la bascule — le seul moment à ne pas improviser

L'atelier 5 n'a **pas de code de départ** : seulement le résultat voulu. Ils vont recopier les cinq
lignes d'affichage trois fois, et c'est exactement ce qu'on veut.

**La dernière consigne est la plus importante :** *« compte les lignes que tu as écrites, et note le
nombre sur ton cahier. »*

À 13 h 08, **ramassez les chiffres à voix haute** — 18, 20, 22 selon les espaces — et **écrivez le plus
grand au tableau, en très grand**. Puis la diapo de bascule :

> **Dix-huit lignes pour trois plateaux. Cinquante-quatre pour une partie.**
> *Vous n'avez rien fait de mal : il vous manque une idée. On va la chercher maintenant.*

**Et vous enchaînez immédiatement sur la leçon.** Ne commentez pas la révision, ne donnez aucun score,
ne dites pas qui a eu juste : **le chiffre écrit au tableau est la seule conclusion dont vous avez
besoin**, et il vient d'eux.

---

## 5. Après la séance

- **Journal** : notez, pour chacun des cinq ateliers, **combien l'ont fait tourner seuls**. C'est une
  photographie de la classe plus honnête qu'un test écrit.
- **Les deux ateliers à retenir** : si la manche 3 (le décalage) ou la manche 4 (le `or`) se passent
  mal pour plus de la moitié, reprenez-les cinq minutes au début de la séance 11 — avant les lignes
  gagnantes, qui en dépendent entièrement.

---

## Vérification faite

[`code/revision_ateliers_corrige.py`](code/revision_ateliers_corrige.py) **a été exécuté** : atelier 1
(`23` puis `5`), atelier 2 (`sel`, puis la liste avec `mais`), atelier 3 (le score affiché dans les deux
cas), atelier 4 (le `or` rend bien la condition vraie sur une case prise, le `and` la rend fausse),
atelier 5 (les trois plateaux). **Il ne contient ni `for` ni `while`** : rien n'y dépasse la séance 9.
