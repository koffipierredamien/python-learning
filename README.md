# Jerusalem Geeks & Jeremiah Geeks

Apprendre Python en construisant le jeu **XO** (morpion), une brique par samedi,
de la première ligne de code jusqu'à l'application graphique jouable.

| | |
|---|---|
| **Jerusalem Geeks** | 9 – 12 ans |
| **Jeremiah Geeks** | 12 – 18 ans |
| **Format** | 2 h, chaque samedi de **12 h à 14 h** · 22 séances, ouvertes par un temps de prière |
| **Encadrement** | 2 enseignants — **un par classe**, les deux classes en parallèle |
| **Outils** | Python 3 · Thonny · Tkinter — gratuits, sans internet |
| **Séance en préparation** | **Séance 4**, samedi 3 octobre 2026, 12 h - 14 h |

---

## Où est quoi

| Dossier | Contenu | Quand on l'ouvre |
|---|---|---|
| **[0-administratif/](0-administratif/LISEZ-MOI.md)** | Le règlement intérieur, à remettre signé par chaque famille | Une fois, à la séance 1 |
| **[1-methode/](1-methode/methode-pedagogique.md)** | La pédagogie : comment faire progresser ensemble des niveaux très différents, à 2 enseignants | Une fois, au début. On y revient en cas de problème |
| **[2-seances/](2-seances/LISEZ-MOI.md)** | Une séance = un dossier. Fiche détaillée, PDF à imprimer, code, sources | **Chaque semaine** |
| **[3-suivi/](3-suivi/LISEZ-MOI.md)** | Le classeur : inscriptions, présence, diagnostic, suivi, observations, journal, cotisations et caisse, **indiscipline et révisions maison** | Après chaque séance |
| **[4-le-jeu-termine/](4-le-jeu-termine/LISEZ-MOI.md)** | Le jeu XO fini : la démonstration d'ouverture, et le point d'arrivée du parcours | Pour montrer, et pour se repérer |

---

## Samedi prochain : la séance 4

👉 **[2-seances/S04-le-jeu-compte/](2-seances/S04-le-jeu-compte/fiche-de-seance.md)**

> **« Le jeu compte les tours. »** Deux notions : `int()` — pourquoi `"3" + "4"` donne `34` — et le
> compteur `tour = tour + 1`, qui est le socle des boucles. Même structure qu'à la séance 2 :
> je montre, vous faites. Deux fois.

| J'ai besoin de… | C'est ici |
|---|---|
| Animer la séance | [📖 La fiche de séance](2-seances/S04-le-jeu-compte/fiche-de-seance.md) — minute par minute |
| Projeter | [📺 Le diaporama](2-seances/S04-le-jeu-compte/a-projeter/seance-4-projection.pptx) — 19 diapos, notes incluses |
| Ouvrir la séance | [🎯 Le quiz flash](2-seances/S04-le-jeu-compte/a-projeter/quiz-rappel.pptx) — 8 questions, 10 min |
| Répéter le live coding | [⌨️ L'anti-sèche](2-seances/S04-le-jeu-compte/code/live_coding_antiseche.py) — à faire la veille, à voix haute |
| Imprimer | [🖨️ Un seul document](2-seances/S04-le-jeu-compte/a-imprimer/quantites-et-formats.md) |
| Envoyer le programme au responsable | [📋 Le déroulé en Word](2-seances/S04-le-jeu-compte/a-envoyer/deroule-seance-4.docx) |
| Revoir le TP de samedi dernier | [📄 La séance 3](2-seances/S03-tp-les-joueurs/a-imprimer/quantites-et-formats.md) |

---

## La méthode en sept principes

1. Une seule classe, un seul projet, **pas de groupes de niveau**
2. Différencier par la profondeur : **3 pistes** (🔵 guidée · 🔴 standard · ⚫ défi), choisies par l'élève à chaque atelier
3. **Le Filet** : le code de référence redistribué à chaque séance → une absence ne met jamais personne en retard
4. **Un enseignant par classe**, et cinq réflexes pour tenir seul : j'alterne parler / circuler, les cartes de couleur sont mes yeux, les élèves s'entraident d'abord, 2 Geek Mentors par séance, je ne m'assois jamais
5. **Le Sas « Permis Machine »** pour les grands débutants, sans les séparer du groupe
6. **Motivation** : grades, Mur de Mission, tournoi final devant les familles
7. **Évaluation par la preuve, jamais par la note** : ça marche / je sais l'expliquer / je sais le refaire

→ [La méthode complète](1-methode/methode-pedagogique.md) ·
[Diagnostic](1-methode/annexes/A1-diagnostic-et-passeport.md) ·
[Conduite de séance](1-methode/annexes/A2-conduite-de-seance.md) ·
[Les 35 cas particuliers](1-methode/annexes/A3-matrice-des-cas.md) ·
[Grades et Mur de Mission](1-methode/annexes/A4-grades-et-mur-de-mission.md) ·
[Outils et modèles](1-methode/annexes/A5-outils-et-modeles.md) ·
[Dictionnaire des erreurs](1-methode/annexes/A6-dictionnaire-des-erreurs.md)

---

## Le parcours

| Phase | Séances | Brique ajoutée au jeu | Notions |
|---|---|---|---|
| 0. Décollage | 1–2 | L'écran d'accueil, et le jeu demande ton nom | théorie de base · l'algorithme · `print()` · la variable · `input()` |
| 1. Parler au joueur | 3–6 | Le jeu parle aux deux joueurs, et compte | variables, `input()`, `int()`, le compteur |
| 2. Le plateau vit | 7–10 | On place X et O à tour de rôle | listes, indices, conditions, boucles |
| 3. Les règles du jeu | 11–14 | Coups refusés, gagnant, match nul | fonctions, `while`, opérateurs logiques |
| 4. L'interface graphique | 15–19 | Fenêtre, grille cliquable, design | Tkinter, événements |
| 5. Finition & intelligence | 20–22 | Score, sons, **IA**, distribution | organisation du code, algorithmes |

Les rendez-vous : **S9** première démo jouable · **S15** concours de design ·
**S19** la Nuit du bug · **S22** tournoi XO et démo aux familles.
*(Le parcours a décalé d'une séance : la séance 1 n'a pas pu aller jusqu'au bout.)*

---

## Où on en est

- [x] La méthode pédagogique et ses annexes
- [x] Le règlement intérieur, version du responsable
- [x] Séance 1 : faite — compte rendu, diaporama de 46 diapos, les 4 documents qui servent encore
- [x] Séance 2 : fiche, diaporama de 28 diapos, quiz, aide-mémoire machine, code, déroulé Word
- [x] Le dictionnaire des erreurs, complet pour tout le parcours
- [x] Séance 3 : le TP de 2 h en autonomie (feuille élève + corrigé enseignant)
- [x] Séance 4 : fiche, diaporama de 19 diapos, quiz flash, aide-mémoire, code, déroulé Word
- [x] Le classeur de suivi, le registre des indisciplines et le suivi des révisions à la maison
- [x] Le jeu XO terminé (démonstration d'ouverture)
- [ ] Séances 5 à 22
