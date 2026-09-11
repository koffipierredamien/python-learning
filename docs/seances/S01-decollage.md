# Séance 1 — « Le Décollage »

> **Fiche de conduite détaillée.** Tout ce qui doit être dit, tout ce qui doit être fait.
> Les passages en **🗣️ guillemets** sont des scripts : ils peuvent être lus tels quels.
> `CAP` = le Capitaine (anime devant) · `MEC` = le Mécanicien (circule, observe, dépanne).
> Voir [la méthode pédagogique](../methode-pedagogique.md) pour les principes, et [l'annexe A2](../annexes/A2-conduite-de-seance.md) pour le rituel des séances ordinaires.

---

## 0. Carte d'identité de la séance

| | |
|---|---|
| **Numéro** | 1 / 22 — Phase 0 « Décollage » |
| **Durée** | 2 h (120 min) |
| **Classes** | Jerusalem Geeks (9–12) et Jeremiah Geeks (12–18) — même déroulé, variantes signalées par 🧒 et 🧑 |
| **Notion Python** | `print()` — faire parler l'ordinateur |
| **Brique ajoutée au projet** | **L'écran d'accueil du jeu XO** : le jeu s'annonce et affiche le nom de son créateur |
| **Livrable élève** | Un fichier `mon_xo/jeu.py` qui s'exécute et affiche un écran d'accueil |
| **Particularité** | Séance atypique : elle installe les rituels et contient le Test de Décollage. **Le temps de code est volontairement court (16 min).** La séance 2 est la première séance de format normal. |

### Les 6 objectifs, par ordre de priorité

1. **Que chaque élève reparte en ayant fait tourner un programme qu'il a écrit lui-même.** *Non négociable — y compris pour l'élève qui n'a jamais touché un ordinateur.*
2. Que chaque élève reparte avec l'envie de revenir samedi.
3. Que les 4 rituels soient installés (signal de silence, cartes de signalisation, règle des 3 avant moi, contrat de binôme).
4. Que les enseignants connaissent le profil de chaque élève.
5. Que chaque élève sache où est son fichier et comment le retrouver.
6. Que chaque élève ait vu un message d'erreur — et compris que ce n'est pas grave.

> **L'objectif n° 1 prime sur tous les autres.** Si le temps manque, on sacrifie le Test de Décollage (reportable à la séance 2), jamais l'atelier de code.

---

## 1. Préparation

### J-7 — À faire impérativement

- [ ] **Coder le jeu XO terminé** (version graphique jouable). C'est la démo du « WOW » d'ouverture : sans elle, la séance perd son moteur. Le tester sur la machine de démonstration.
- [ ] Installer **Python + Thonny** sur toutes les machines, **version identique**, et **lancer un programme sur chaque poste** pour vérifier.
- [ ] Créer sur chaque poste, sur le Bureau : le dossier **`GEEKS`**, contenant `xo_officiel/` (vide pour l'instant) et `mon_xo/`.
- [ ] Régler la **taille de police de Thonny à 18** minimum sur tous les postes, et sur la machine de projection.
- [ ] Préparer la **clé USB maîtresse** : le code officiel, les fichiers des 3 pistes, les fiches.
- [ ] Vérifier le vidéoprojecteur **avec le câble et la machine du jour**.

### J-1 — Impressions et matériel

| Quantité | Document | Source |
|---|---|---|
| 1 par binôme | Jeu de 4 **cartes de signalisation** (vert / orange / rouge / bleu), plastifiées | [A5 §1](../annexes/A5-outils-imprimables.md) |
| 1 affiche A3 | **Règle des 3 avant moi** | [A5 §2](../annexes/A5-outils-imprimables.md) |
| 1 affiche A3 | **Contrat de binôme** | [A5 §3](../annexes/A5-outils-imprimables.md) |
| 1 par élève | **Contrat de binôme** format A5, à signer | [A5 §3](../annexes/A5-outils-imprimables.md) |
| 1 affiche A3 | **Dictionnaire des erreurs**, avec seulement 3 lignes remplies | [A5 §4](../annexes/A5-outils-imprimables.md) |
| 1 affiche A1 | **Mur de Mission** : 22 cases, case 1 = « Le jeu dit bonjour » | [A4 §3](../annexes/A4-grades-et-badges.md) |
| 1 par élève | **Passeport Machine** (livret 12 gestes) | [A1 §6](../annexes/A1-diagnostic-et-passeport.md) |
| 1 par élève | **Journal de bord** (carnet A5) | [A5 §5](../annexes/A5-outils-imprimables.md) |
| 1 par élève | Questionnaire **station 3** | [A1 §4](../annexes/A1-diagnostic-et-passeport.md) |
| 6 exemplaires | Cartes-missions **station 1** | [A1 §2](../annexes/A1-diagnostic-et-passeport.md) |
| 6 exemplaires | Feuilles d'énigmes **station 2** | [A1 §3](../annexes/A1-diagnostic-et-passeport.md) |
| 2 exemplaires | **Grille d'observation** | [A1 §5](../annexes/A1-diagnostic-et-passeport.md) |
| 1 par binôme | **Fiche mémo S1** | [supports/S01/fiche-memo.md](../../supports/S01/fiche-memo.md) |
| — | Étiquettes prénom (grosses lettres), badges/autocollants, tampon, minuteur visible, boîte à post-it | |

### Le jour même — 30 minutes avant

- [ ] Machines allumées, Thonny ouvert sur chaque poste, dossier `GEEKS` visible
- [ ] **Une machine de réserve allumée** en fond de salle
- [ ] Fichier `piste_bleue_jeu.py` déjà copié dans `mon_xo/` de **chaque** poste
- [ ] Affiches au mur, Mur de Mission bien visible
- [ ] Le jeu XO fini est **ouvert et prêt à lancer** sur la machine de projection (ne pas le lancer devant les élèves en cherchant le fichier : l'effet est cassé)
- [ ] Rôles décidés à voix haute : « aujourd'hui, je suis Capitaine, tu es Mécanicien »
- [ ] **Salle ouverte 30 min avant** (Sas Permis Machine) : accueillir ceux qui arrivent tôt, les laisser explorer la machine

### Disposition de la salle

```
                        ┌──────────────────┐
                        │   ÉCRAN PROJETÉ  │
                        └──────────────────┘
                              [ CAP ]
      ╔═══════╗   ╔═══════╗          ╔═══════╗   ╔═══════╗
      ║ poste ║   ║ poste ║          ║ poste ║   ║ poste ║
      ╚═══════╝   ╚═══════╝          ╚═══════╝   ╚═══════╝
      ╔═══════╗   ╔═══════╗          ╔═══════╗   ╔═══════╗
      ║ poste ║   ║ poste ║          ║ poste ║   ║ poste ║
      ╚═══════╝   ╚═══════╝          ╚═══════╝   ╚═══════╝
           ↑ circuit du MEC ↑ ─────────────────→ ↓
      ┌─────────────────────────────────────────────────┐
      │  MURS : 3 avant moi · Contrat · Erreurs · MUR   │
      │  Table du fond : machine de réserve + matériel  │
      └─────────────────────────────────────────────────┘
```

**Règle de disposition :** tous les écrans doivent être visibles depuis le fond de la salle. En U ou en rangées face au tableau, **jamais** en épi dos au mur.

---

## 2. Le déroulé minute par minute

---

### ⏱️ 00 – 08 · Accueil et installation *(8 min)*

**MEC** — à la porte, accueille chaque élève individuellement, serre la main ou tope, donne une étiquette prénom, coche la présence.

> 🗣️ **MEC :** « Salut ! Comment tu t'appelles ? … Bienvenue chez les **Jerusalem Geeks** [ou Jeremiah Geeks]. Écris ton prénom en gros sur l'étiquette et colle-la sur toi. Ensuite, assieds-toi où tu veux — c'est la seule fois de l'année où tu choisis ta place ! »

**CAP** — debout devant, salue, distribue le **journal de bord** et le **Passeport Machine** sur chaque table.

> ⚠️ **Ne pas laisser les élèves toucher les machines pendant cette phase.** Écrans allumés mais non utilisés — sinon on ne récupère plus leur attention. Le dire simplement : *« Les ordinateurs, on n'y touche pas tout de suite. Promis, ça vient dans un instant. »*

**Ce que MEC observe déjà et note :** qui arrive avec un parent · qui n'ose pas entrer · qui se connaît déjà · qui se précipite sur la machine.

---

### ⏱️ 08 – 20 · L'ouverture : le WOW, la guilde, la promesse *(12 min)*

#### a) Le WOW (4 min) — `CAP`

On ne dit pas bonjour. **On lance le jeu terminé, en silence, plein écran.**

> 🗣️ **CAP :** *(après 5 secondes de silence)* « Il me faut un volontaire. … Viens. Assieds-toi ici. Tu joues contre moi. »

On joue une partie complète, en direct, au vidéoprojecteur. On la perd, de préférence. Applaudissements.

> 🗣️ **CAP :** « Ce jeu, ce n'est pas moi qui vais le faire. **C'est vous.** Vous allez le construire, morceau par morceau, un samedi après l'autre. Et à la fin, vous repartirez avec — sur une clé, pour le montrer à vos parents, à vos amis, et pour les battre. »

#### b) La guilde (4 min) — `CAP`

> 🗣️ **CAP :** « Bienvenue chez les **Jerusalem Geeks**. Un geek, ce n'est pas un mot moqueur ici : c'est quelqu'un qui comprend comment marchent les machines, et qui sait leur donner des ordres. À partir d'aujourd'hui, vous êtes des **Novices**. Dans quelques semaines vous serez **Apprentis Codeurs**, puis **Codeurs**, puis **Ingénieurs**, puis **Architectes** — et les meilleurs finiront **Maîtres Geeks**. »

Montrer le **Mur de Mission** — 22 cases.

> 🗣️ **CAP :** « Voilà notre carte. 22 cases, 22 samedis. Chaque samedi, la classe avance d'**une** case. Attention : la classe, pas un élève. On avance **ensemble**. Aujourd'hui, on va franchir la case 1 : *le jeu dit bonjour*. »

🧒 **Jerusalem :** insister sur la carte au trésor, le côté aventure, les bracelets de grade.
🧑 **Jeremiah :** ton plus sobre. « Ce que vous allez faire ici, c'est exactement ce que font les développeurs professionnels : un projet, découpé en versions, livré morceau par morceau. »

#### c) La promesse et les 3 règles (4 min) — `CAP`

> 🗣️ **CAP :** « Je vous fais trois promesses.
> **Un :** chaque samedi, en repartant, votre jeu marchera mieux qu'en arrivant. **Chaque samedi. Tous.**
> **Deux :** ici, il n'y a **pas de notes**. Jamais. Personne ne sera comparé à personne.
> **Trois :** si vous êtes absents un samedi, vous ne serez **pas** en retard. J'ai un système pour ça, je vous le montrerai tout à l'heure.
>
> En échange, je vous demande trois choses.
> **Un :** on ne se moque **jamais** de quelqu'un qui n'a pas compris ou qui va moins vite. Jamais. C'est la seule règle pour laquelle je me fâcherai.
> **Deux :** quand quelque chose ne marche pas, on ne dit pas *"je suis nul"*. On dit *"je n'ai pas encore trouvé"*.
> **Trois :** on essaie. Même quand on n'est pas sûr. Surtout quand on n'est pas sûr. »

---

### ⏱️ 20 – 30 · Les quatre rituels *(10 min)*

#### Rituel 1 — Le signal de silence (2 min)

> 🗣️ **CAP :** « Dans cette salle, il y aura du bruit, et c'est normal : quand on code à deux, on parle. Mais quand j'ai besoin de vous, j'ai un signal. »

Choisir **un** signal et ne jamais en changer : trois frappes dans les mains · une clochette · les bras levés.

> 🗣️ **CAP :** « Quand vous entendez ça : mains sur la table, yeux sur moi, plus un mot. En 3 secondes. On s'entraîne. Faites du bruit… allez, du vrai bruit ! … *[signal]* … Trois, deux, un. **Parfait.** On recommence, plus fort. »

> **Faire l'exercice 2 ou 3 fois, en jeu.** Dix minutes investies là économisent deux heures sur le trimestre.

#### Rituel 2 — Les cartes de signalisation (3 min)

`MEC` distribue un jeu de 4 cartes par poste pendant que `CAP` explique.

> 🗣️ **CAP :** « Ici, on ne lève **pas** la main. On lève une carte.
> 🟢 **Vert** : ça avance, tout va bien.
> 🟠 **Orange** : on est bloqués. On continue à chercher, mais on a besoin d'aide.
> 🔴 **Rouge** : rien ne marche du tout, au secours.
> 🔵 **Bleu** : on a fini — et on est prêts à aider les autres.
>
> Vous posez la carte sur l'écran, bien visible, et vous continuez à travailler. Nous, on voit toute la salle d'un coup d'œil.
> Je vous fais une promesse : **une carte orange est servie en moins de 5 minutes. Une carte rouge, tout de suite.** »

#### Rituel 3 — La règle des 3 avant moi (3 min)

Montrer l'affiche.

> 🗣️ **CAP :** « Avant de lever la carte orange, trois choses.
> **Un : je relis.** La consigne, puis le message rouge de l'ordinateur — **à voix haute**. Vous verrez, ça marche tout seul une fois sur trois.
> **Deux : je demande à mon binôme**, et on regarde la fiche mémo posée sur la table.
> **Trois : on demande au binôme d'à côté.** 30 secondes, pas plus.
> Toujours bloqués ? Carte orange, et on arrive. »

🧒 **Jerusalem :** faire répéter en chœur « je relis, mon binôme, le voisin ! ».
🧑 **Jeremiah :** « C'est exactement ce qu'on attend d'un développeur : ne pas rester bloqué en silence, mais ne pas non plus appeler à l'aide avant d'avoir lu l'erreur. »

#### Rituel 4 — Le contrat de binôme (2 min, la signature vient plus tard)

> 🗣️ **CAP :** « Ici, on code **à deux sur un ordinateur**. Ce n'est pas parce qu'on manque de machines : c'est comme ça que travaillent les vrais développeurs, ça s'appelle le *pair programming*.
> Un **Pilote** : il tient le clavier, il est le seul à taper, et il dit à voix haute ce qu'il fait.
> Un **Copilote** : il lit la consigne, il surveille les erreurs, il propose — et il **n'a pas le droit de toucher le clavier**. C'est le rôle le plus difficile, et c'est souvent lui qui trouve les bugs.
> Toutes les 10 minutes, au signal, **vous échangez**. »

---

### ⏱️ 30 – 55 · Le Test de Décollage *(25 min — 3 stations × 8 min)*

> ⚠️ **Le mot « test » n'est jamais prononcé devant les élèves.** On dit **« les missions de décollage »**.

> 🗣️ **CAP :** « Avant de décoller, tous les astronautes passent des missions de préparation. Trois missions, huit minutes chacune. Ce n'est pas noté, il n'y a pas de bonne ou de mauvaise équipe — ça sert **à nous**, pour bien vous accompagner. Vous êtes trois groupes. Quand j'appelle, vous tournez. »

Compter les élèves, faire trois groupes, désigner les zones : **Mission Pilotage** (postes) · **Mission Logique** (tables sans machine) · **Mission Identité** (table du fond).

| Station | Contenu | Tenue par |
|---|---|---|
| **1. Pilotage** — 8 min | Les 6 missions machine ([A1 §2](../annexes/A1-diagnostic-et-passeport.md)) | `CAP` observe et cote |
| **2. Logique** — 8 min | Les 4 énigmes papier ([A1 §3](../annexes/A1-diagnostic-et-passeport.md)) | En autonomie ; `MEC` circule |
| **3. Identité** — 5 min puis libre | Le questionnaire ([A1 §4](../annexes/A1-diagnostic-et-passeport.md)) | En autonomie ; ceux qui finissent commencent leur **Passeport Machine** |

**Pendant tout le test, `MEC` remplit la grille d'observation** et surtout la colonne décisive : *abandonne / demande / persévère / aide les autres*.

**À la fin du test, `MEC` trie immédiatement les fiches en 3 piles : P0 · P1 · P2-P3.** Ce tri sert au binômage pendant la pause. **C'est la tâche la plus urgente de la séance : elle doit être finie avant la fin de la pause.**

> 🗣️ **CAP** *(à la fin)* : « Missions terminées. Personne n'a raté quoi que ce soit : tout le monde décolle. Pause ! Dix minutes. Levez-vous, sortez, bougez — et revenez à l'heure. »

---

### ⏱️ 55 – 65 · Pause *(10 min)*

Pause **réelle** : les élèves sortent, se lèvent, boivent.

**Pendant ce temps, les deux enseignants forment les binômes, en 5 minutes chrono :**

1. Écrire chaque prénom sur un petit papier, avec son profil (P0 / P1 / P2 / P3).
2. **Trier tous les papiers du plus faible au plus fort.** Couper le paquet en deux moitiés : pile A (la moitié la moins à l'aise) et pile B.
3. **Associer le 1ᵉʳ de A avec le 1ᵉʳ de B, le 2ᵉ de A avec le 2ᵉ de B**, etc.
   → cela donne mécaniquement un **écart d'environ un niveau** : jamais un P0 avec un P3.
4. Ajuster à la main pour 2 ou 3 cas : élèves qui ne doivent pas être ensemble, élève très timide à placer avec un élève patient.
5. Nombre impair ? Former **un trinôme** : Pilote / Copilote / **Testeur** (le testeur lit la consigne à voix haute et vérifie le résultat). Jamais un élève seul.
6. Écrire la liste au tableau **avec le numéro du poste**, pour que l'installation soit instantanée.

---

### ⏱️ 65 – 72 · Les binômes s'installent et signent *(7 min)*

> 🗣️ **CAP :** « Les équipes sont au tableau, avec le numéro de votre poste. Vous ne choisissez pas votre binôme — comme au travail. Vous en changerez dans trois semaines. Installez-vous. »

`MEC` distribue le contrat A5, un par élève.

> 🗣️ **CAP :** « Lisez les six règles avec votre binôme, à voix haute. Puis vous signez tous les deux, sur votre feuille et sur celle de l'autre. »

*(Laisser 3 minutes, puis reprendre la parole.)*

> 🗣️ **CAP :** « Celui des deux dont le **prénom commence par la lettre la plus proche de A** est **Pilote** en premier. L'autre est **Copilote**. Copilotes, levez la main… vous êtes les gardiens : **vos doigts ne touchent pas le clavier**. »

---

### ⏱️ 72 – 80 · Visite guidée de Thonny *(8 min)*

Au vidéoprojecteur, très lentement, avec la police en taille 18+. Les élèves **regardent seulement** : on ne touche pas encore.

> 🗣️ **CAP :** « Voici l'outil des Geeks. Il s'appelle **Thonny**. Il n'y a que trois choses à retenir aujourd'hui. »

1. **La zone du haut, blanche : c'est là qu'on écrit le programme.**
   > 🗣️ « C'est votre feuille. Ce que vous écrivez ici, l'ordinateur ne le fait pas tout de suite : il attend. »
2. **La zone du bas : c'est là que l'ordinateur répond.**
   > 🗣️ « C'est sa bouche. Tout ce qu'il a à vous dire sort ici. Y compris quand il n'est pas content — en rouge. »
3. **Le gros bouton vert ▶, ou la touche `F5` : c'est le bouton "vas-y".**
   > 🗣️ « Quand vous appuyez là, l'ordinateur lit votre programme du début à la fin et fait **exactement** ce que vous avez écrit. Ni plus, ni moins. Retenez bien : **l'ordinateur n'est pas intelligent. Il est obéissant.** Si votre programme fait une bêtise, ce n'est pas lui qui s'est trompé. »

Montrer aussi, en 30 secondes : `Fichier > Enregistrer`, et où se trouve `Bureau / GEEKS / mon_xo`.

---

### ⏱️ 80 – 92 · Live coding : « je code, vous prédisez » *(12 min)*

#### a) Le premier `print` (3 min)

`CAP` tape, très lentement, en verbalisant chaque caractère :

```python
print("Bonjour")
```

> 🗣️ **CAP :** « `p-r-i-n-t`, ça veut dire *affiche*. Ensuite une parenthèse — on l'ouvrira et on la fermera **toujours**. Puis un guillemet, mon texte, un guillemet. Et on referme la parenthèse.
> **Avant que j'appuie : qu'est-ce qui va se passer ? … À trois. Un, deux, trois !** »

*(Appuyer sur F5. Le mot apparaît en bas.)*

> 🗣️ **CAP :** « Voilà. Vous venez de voir un ordinateur **obéir**. C'est tout le métier. »

#### b) Prédiction n° 2 (2 min)

```python
print("Bonjour")
print("Je suis ton ordinateur")
```

> 🗣️ **CAP :** « Deux lignes maintenant. Qu'est-ce que ça va afficher ? Dans quel ordre ? … Levez la main ceux qui pensent que "Bonjour" sortira en premier. … On vérifie. »

> 🗣️ **CAP :** « Règle numéro un de la programmation : **l'ordinateur lit de haut en bas, ligne par ligne, dans l'ordre.** Toujours. »

#### c) 🔥 L'erreur volontaire (4 min) — **le moment le plus important de la séance**

`CAP` oublie volontairement le guillemet de fin :

```python
print("Bonjour)
```

Appuyer sur F5. Du rouge apparaît.

> 🗣️ **CAP :** *(avec un grand sourire)* « **Ah ! Du rouge !** … Alors, qui a peur ? »

*(Laisser réagir. Puis, très calmement :)*

> 🗣️ **CAP :** « Moi je code depuis des années, et j'ai du rouge **tous les jours**. Le rouge, ce n'est pas une punition. Ce n'est pas une mauvaise note. **C'est l'ordinateur qui vous explique ce qu'il n'a pas compris.** Il essaie de vous aider. Le problème, c'est qu'il le dit en anglais. Alors on va apprendre à le lire. Ensemble. Il a écrit : `SyntaxError`. Quelqu'un devine ? … *Syntax*, c'est la grammaire. *Error*, l'erreur. Il nous dit : **"je ne comprends pas ta phrase"**. Et regardez : il montre même l'endroit avec une petite flèche. »

Réparer devant tout le monde, relancer, ça marche.

> 🗣️ **CAP :** « Réparé en quatre secondes. Retenez ça : **dans cette salle, le rouge n'est pas grave. Le rouge est une information.** »

Aller écrire `SyntaxError` au tableau du **Dictionnaire des erreurs**, et nommer un **Gardien des erreurs** pour la séance.

#### d) La consigne de l'atelier (3 min)

Projeter le résultat à obtenir :

```
===================================
       BIENVENUE DANS LE JEU XO
===================================
Créé par : Damien
```

> 🗣️ **CAP :** « Votre mission : faire dire ça à votre ordinateur. Avec **votre** prénom. Trois pistes, vous choisissez :
> 🔵 **Bleue** — le début est déjà écrit dans votre fichier, vous complétez les trous. Aucune honte, c'est la piste la plus maligne quand on débute.
> 🔴 **Rouge** — vous écrivez tout vous-mêmes, à partir de la consigne.
> ⚫ **Noire** — vous faites tout ça, **et en plus** vous dessinez la grille vide du morpion en dessous. Avec des `print`, uniquement.
>
> Personne ne vous jugera sur votre piste. **Le jeu qui sort est le même.** Cartes de signalisation sorties. Pilotes, à vous. Copilotes : vos mains restent sur vos genoux ! C'est parti. »

---

### ⏱️ 92 – 108 · Atelier 1 : mon premier programme *(16 min)*

**Déroulé mécanique :**
- 92 : lancement. Les binômes ouvrent `GEEKS / mon_xo / jeu.py` dans Thonny.
- **100 : signal sonore → rotation Pilote / Copilote.** Sans exception, même au milieu d'une ligne.
- 108 : signal de silence, on s'arrête.

**Positions :**
- `CAP` **reste debout, devant**, balaye la salle du regard, gère le temps. Il ne se déplace que pour une carte rouge.
- `MEC` fait son circuit en U, **en commençant par les postes des profils P0**.

**Les 4 phrases autorisées pour aider** *(ne jamais prendre le clavier)* :
1. « Lis-moi ton message d'erreur à voix haute. »
2. « Montre-moi la ligne. Qu'est-ce que tu voulais qu'elle fasse ? »
3. « Qu'est-ce qui se passerait si on mettait ça ici ? Essaie. »
4. « Explique-moi cette ligne comme si j'étais ton petit frère. »

**Les 3 gestes du Passeport Machine à valider pendant l'atelier** (tampon donné sur place par `MEC`) :
`#10` j'ouvre Thonny et je lance un programme · `#8` j'enregistre au bon endroit · `#9` je retrouve mon fichier.

**Les erreurs attendues aujourd'hui — et la réponse, en une phrase :**

| Erreur | Ce qu'on voit | Ce qu'on dit |
|---|---|---|
| Guillemet oublié | `SyntaxError` | « Compte tes guillemets. Il en faut deux, comme une paire de chaussures. » |
| Parenthèse oubliée | `SyntaxError` | « Tout ce qui s'ouvre doit se fermer. » |
| `Print` avec majuscule | `NameError: name 'Print' is not defined` | « L'ordinateur est très à cheval sur les majuscules. `print`, tout en minuscules. » |
| Texte sans guillemets | `SyntaxError` / `NameError` | « Du texte, ça se met toujours entre guillemets — sinon il croit que c'est un ordre. » |
| Clavier : ne trouve pas `"` ou `(` | — | Montrer la touche physiquement. **Geste 4 du Passeport.** Ne pas taper à sa place. |
| A tapé dans la zone du bas (console) | Ça s'exécute mais rien n'est enregistré | « Ça, c'est sa bouche. Ta feuille, c'est en haut. » |
| Le fichier n'est pas enregistré | Thonny propose d'enregistrer au lancement | « Tu enregistres d'abord, tu lances ensuite. Toujours. » |

**Gestion des rythmes pendant ces 16 minutes :**

| Situation | Réponse immédiate |
|---|---|
| Binôme carte 🔵 en 5 min | 1) Passer piste Noire (la grille du morpion) 2) puis devenir **Geek Mentor** : « va aider le binôme du poste 4, mais **interdiction de toucher leur clavier** » |
| Binôme qui n'a pas fini à 108 | On s'arrête quand même. `MEC` enregistre leur fichier, et **CAP annonce publiquement** : « personne ne finit tout aujourd'hui, c'est normal, et ça ne vous mettra jamais en retard. » |
| Un élève ne trouve aucune touche | Lui donner **une seule** ligne à compléter, et célébrer bruyamment quand elle s'affiche |

> **Objectif absolu de ces 16 minutes : que 100 % des écrans aient affiché quelque chose écrit par l'élève.** `MEC` tient mentalement le compte. À 104, s'il reste un poste où rien n'est jamais sorti, **c'est la priorité n° 1 des deux enseignants.**

---

### ⏱️ 108 – 114 · Mise en commun, le Filet, sauvegarde *(6 min)*

#### a) Deux démonstrations (2 min)

Choisir **un binôme piste Bleue** et **un binôme piste Noire** — dans cet ordre, jamais l'inverse.

> 🗣️ **CAP :** « Poste 3, montrez-nous votre écran. … Vous avez fait quoi ? … Applaudissez-les. »

> 🗣️ **CAP :** *(après la Noire)* « Vous voyez : le leur a une grille en plus. Mais les deux jeux disent bonjour, et les deux marchent. Piste Bleue ou piste Noire : **vous avez tous franchi la case 1.** »

#### b) Le Filet (2 min) — **à faire solennellement**

> 🗣️ **CAP :** « Vous vous souvenez de ma troisième promesse ? Regardez bien. »

Brancher la clé USB, copier `jeu.py` dans `xo_officiel/`, devant tout le monde, au vidéoprojecteur.

> 🗣️ **CAP :** « Ce fichier, c'est le **code officiel**. Il contient exactement ce qu'on a fait aujourd'hui, sans erreur. Et samedi prochain, **je le redonne à tout le monde**.
> Ça veut dire quoi ? Que si vous êtes malade samedi prochain… vous ne serez **pas** en retard. Que si vous effacez tout par accident… ce n'est **pas** grave. Que si vous cassez votre code en essayant un truc… **ce n'est pas grave du tout.**
> Donc à partir d'aujourd'hui : **essayez des choses. Cassez. Expérimentez.** On a toujours une copie de secours. »

#### c) Sauvegarde (2 min)

> 🗣️ **CAP :** « Tout le monde : `Fichier`, `Enregistrer`. Vérifiez en haut que c'est bien dans `GEEKS / mon_xo`. Copilotes, c'est **vous** qui vérifiez. Levez le pouce quand c'est fait. »

`MEC` passe avec la clé et copie le travail de chaque binôme (filet de sécurité côté enseignants).

---

### ⏱️ 114 – 120 · Clôture rituelle *(6 min)*

#### a) Badges et grade (2 min)

> 🗣️ **CAP :** « Premiers badges des Jerusalem Geeks ! »

- 🧱 **`Bâtisseur`** → **à tous ceux dont le programme a affiché quelque chose.** Viser 100 %.
- 🤝 `Bon copilote` → à 3 ou 4 élèves qui ont vraiment tenu le rôle sans toucher le clavier
- 🐞 `Chasseur de bug` → à ceux qui ont trouvé une erreur seuls
- 💪 `Persévérant` → **en priorité à ceux qui ont galéré et qui sont restés dessus** — le dire fort
- 🔤 `Traducteur d'erreur` → au Gardien des erreurs du jour
- 🤍 **Grade Novice** → à toute la classe, avec la carte de membre de la guilde

#### b) Le Mur de Mission (1 min)

Désigner un élève — de préférence **le plus discret de la séance**.

> 🗣️ **CAP :** « Viens colorier la case 1. … *Le jeu dit bonjour.* Une case sur 22. Applaudissez-vous. »

#### c) Le journal de bord (2 min)

> 🗣️ **CAP :** « Ouvrez votre journal, page de la séance 1. Deux phrases à compléter :
> *Aujourd'hui j'ai compris ___* et *Je ne suis pas encore sûr de ___*.
> La deuxième est **plus importante** que la première : c'est elle qui nous dit, à nous, par quoi commencer samedi. Écrivez la vérité. Puis vous détachez le post-it et vous le mettez dans la boîte en sortant. »

#### d) Sortie (1 min)

> 🗣️ **CAP :** « Défi maison, **totalement facultatif** : expliquez à quelqu'un chez vous ce que fait `print`. Et si vous n'avez pas d'ordinateur à la maison — **aucun problème, vous ne serez jamais en retard**. Rien ici ne dépend de ce que vous faites chez vous.
> Samedi prochain : le jeu va vous **demander votre nom**. À samedi, les Geeks ! »

Éteindre les machines (**geste 1 du Passeport**), ranger les chaises, `MEC` à la porte pour saluer chacun et récupérer les post-it.

---

## 3. Après la séance — 15 minutes à deux

- [ ] **Finaliser le code officiel** `code-officiel/S01/jeu.py` et le copier sur la clé maîtresse
- [ ] **Remplir le tableau de suivi** : une ligne par élève — `✔` / `~` / `✖` + piste (B/R/N) + profil P0–P3
- [ ] **Lire tous les post-it** et compter ce qui revient. Si une même difficulté apparaît chez plus de 30 % du groupe, **elle ouvre la séance 2**
- [ ] **Établir la liste des 10 minutes** pour la séance 2 : qui n'a rien produit, qui a décroché, qui n'a pas parlé de la séance
- [ ] **Envoyer le message aux familles** (modèle ci-dessous)
- [ ] **Répondre aux 3 questions de la revue**, dans le carnet partagé :
  1. Qui a décroché aujourd'hui, et qu'est-ce qu'on fait samedi prochain ?
  2. Quelle explication n'a pas fonctionné, et comment on la reformule ?
  3. La brique de la semaine prochaine est-elle trop grosse ?
- [ ] **Décider les rôles de la séance 2** : les rôles s'échangent (`CAP` ↔ `MEC`)

### Message aux familles

```
Bonjour à tous 👋

Première séance des Jerusalem Geeks aujourd'hui — et tout le
monde a décollé !

✅ Ce qu'ils ont appris : donner un ordre à un ordinateur
   (la commande « print »), et surtout que les messages
   d'erreur ne sont PAS des fautes : ce sont des indices.

🎮 Leur jeu sait déjà faire quelque chose : il affiche son
   écran d'accueil, avec le nom de son créateur.

🏅 Tous sont repartis avec le badge « Bâtisseur » et le
   grade de Novice.

🎯 Défi facultatif : demandez-leur ce que fait « print ».
   Aucune obligation, et aucun retard si ce n'est pas fait —
   tout se fait en classe.

📅 Samedi prochain : le jeu leur demandera leur nom.
```

---

## 4. Plans de secours

| Problème | Quoi faire |
|---|---|
| **Panne de courant / machines HS** | Basculer sur la **version débranchée** (§ 5). Le WOW se raconte, le Test de Décollage se fait entièrement sur papier (stations 2 et 3), et l'atelier devient « le programme sur papier » : chaque binôme **écrit** son écran d'accueil au feutre sur une feuille A3, et un camarade joue le rôle de l'ordinateur en le lisant **littéralement, ligne par ligne**. Très efficace, et les élèves en reparlent des semaines après. |
| **Le vidéoprojecteur ne marche pas** | Le WOW se fait en petits groupes autour de la machine de démonstration (3 minutes par groupe, pendant que `MEC` distribue le matériel). Le live coding se fait aussi par groupes tournants. |
| **Un enseignant absent** | Supprimer le Test de Décollage (reporté à la séance 2). Garder : accueil, WOW, guilde, rituels, Thonny, live coding, atelier, clôture. Binômes formés par proximité géographique. |
| **Beaucoup plus d'élèves que prévu** | Trinômes (Pilote / Copilote / Testeur). Test de Décollage réduit aux stations 2 et 3, station 1 reportée à la séance 2. |
| **Moins de machines que de binômes** | Alterner : pendant que la moitié code, l'autre moitié fait les énigmes de la station 2 ou avance son Passeport. Échange à mi-atelier. |
| **On a 20 minutes de retard** | Supprimer, dans cet ordre : 1) la station 3 du test (questionnaire à remplir à la maison ou en séance 2) 2) la 2ᵉ démonstration de la mise en commun 3) la station 1. **Ne jamais supprimer l'atelier, ni la clôture avec les badges.** |
| **Un élève arrive 45 min en retard** | `MEC` le prend 2 min à part : étiquette prénom, résumé en 3 phrases, placement dans un binôme existant en **trinôme**, et il code. Pas de test de décollage : on le fera la semaine prochaine. |

---

## 5. Version débranchée de la séance 1 (plan B complet)

**Matériel :** feuilles A3, gros feutres, la grille XO dessinée au tableau.

1. **Le WOW** : jouer une vraie partie de morpion au tableau, contre un élève.
2. **La guilde, la promesse, les rituels** : identiques, mot pour mot.
3. **« L'ordinateur humain »** (20 min) : un enseignant joue le rôle de l'ordinateur. Il **n'obéit qu'aux ordres écrits, et à la lettre**. Les élèves lui écrivent `print("Bonjour")` sur une feuille. Il lit, il dit « Bonjour ». Si on écrit `Print`, il répond : *« je ne connais pas ce mot »*. Si on oublie un guillemet, il dit : *« erreur de grammaire, je ne comprends pas ta phrase »*.
   > Cette activité enseigne **mieux que la machine** ce qu'est l'obéissance littérale d'un ordinateur. À garder même quand tout fonctionne, si le temps le permet.
4. **Atelier papier** (20 min) : chaque binôme écrit son écran d'accueil du jeu XO en lignes de `print`, sur A3. Un autre binôme vient « l'exécuter » à voix haute, littéralement. Les bugs se voient immédiatement, et c'est très drôle.
5. **Clôture** : identique — badges, Mur de Mission, journal de bord. Les A3 sont affichés au mur.

---

## 6. Les six pièges de la séance 1

| Piège | Conséquence | Parade |
|---|---|---|
| **Trop parler au début** | On perd la classe avant même d'avoir codé | Le bloc 08–30 est **chronométré**. Si à 30 min on n'a pas fini, on coupe et on avance |
| **Laisser les élèves toucher les machines pendant les explications** | Plus personne n'écoute | Règle annoncée d'emblée, et rappelée avec humour |
| **Présenter le Test comme un test** | Angoisse, résultats faussés, mauvais départ | On dit « missions de décollage », toujours |
| **Prendre le clavier d'un élève pour aller plus vite** | L'élève apprend qu'il n'y arrive pas seul. Le geste le plus destructeur du métier | Les 4 phrases autorisées, et rien d'autre |
| **Laisser un élève repartir sans avoir rien affiché** | Il ne reviendra probablement pas samedi | `MEC` surveille les écrans à 104 min ; c'est la priorité absolue |
| **Oublier les badges faute de temps** | On casse le moteur de motivation dès la première séance | Les 6 dernières minutes sont **intouchables** |

---

## 7. Supports de la séance

| Support | Fichier |
|---|---|
| Fiche mémo élève (1 par binôme) | [`supports/S01/fiche-memo.md`](../../supports/S01/fiche-memo.md) |
| 🔵 Piste Bleue — fichier à trous | [`supports/S01/piste_bleue_jeu.py`](../../supports/S01/piste_bleue_jeu.py) |
| 🔴 Piste Rouge — consigne | [`supports/S01/piste_rouge.md`](../../supports/S01/piste_rouge.md) |
| ⚫ Piste Noire — défi | [`supports/S01/piste_noire.md`](../../supports/S01/piste_noire.md) |
| **Code officiel de fin de séance 1** | [`code-officiel/S01/jeu.py`](../../code-officiel/S01/jeu.py) |

---

## 8. Vers la séance 2

**Brique suivante :** *le jeu demande son nom au joueur et le salue.*
**Notion :** les variables et `input()`.
**Accroche à annoncer dès aujourd'hui :** *« Samedi prochain, votre jeu ne va plus seulement parler. Il va vous écouter. »*

**À préparer avec ce qui est sorti d'aujourd'hui :**
- Les profils P0 → le fichier piste Bleue de la séance 2 devra être encore plus guidé
- Les post-it → la difficulté la plus citée ouvre la séance
- La liste des 10 minutes → qui `MEC` prend en tête-à-tête pendant l'atelier 2
- Les binômes → inchangés jusqu'à la séance 4
