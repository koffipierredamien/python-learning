# Python Learning — Jerusalem Geeks & Jeremiah Geeks

Programme de formation à la programmation Python pour enfants et adolescents,
construit autour d'un projet fil rouge unique : **le jeu XO (Tic-Tac-Toe)**,
de la première ligne de code jusqu'à l'application graphique jouable.

| | |
|---|---|
| **Jerusalem Geeks** | 9 – 12 ans |
| **Jeremiah Geeks** | 12 – 18 ans |
| **Format** | 1 séance de 2 h, chaque samedi (≈ 22 séances) |
| **Encadrement** | 2 enseignants |
| **Langage & outils** | Python 3 · Thonny · Tkinter |

---

## 📚 Documentation

### [→ Méthode pédagogique complète](docs/methode-pedagogique.md)

Le document de référence : la stratégie retenue pour faire progresser ensemble
des élèves de niveaux très différents — du grand débutant qui n'a jamais utilisé
un ordinateur à l'élève qui code déjà — avec seulement deux enseignants.

**Les huit principes :**

1. Une seule classe, un seul projet, **pas de groupes de niveau**
2. Différencier par la profondeur : **3 pistes** (🔵 Bleue guidée · 🔴 Rouge standard · ⚫ Noire défi), choisies par l'élève à chaque atelier
3. **Le Filet** : un code de départ officiel redistribué à chaque séance → aucun décrochage cumulatif possible
4. **Le binôme est le 3ᵉ enseignant** : pilote / copilote, rotation toutes les 10 minutes
5. **Deux rôles enseignants distincts et tournants** : le Capitaine (devant) et le Mécanicien (dans les rangs)
6. **Le Sas « Permis Machine »** pour les grands débutants, sans les séparer du groupe
7. **Motivation** : grades, badges, Mur de Mission, tournoi final devant les familles
8. **Évaluation par la preuve, jamais par la note** : ça marche / je sais l'expliquer / je sais le refaire

### Annexes opérationnelles

| Annexe | Contenu |
|---|---|
| [A1 — Diagnostic & Passeport Machine](docs/annexes/A1-diagnostic-et-passeport.md) | Le « Test de Décollage » en 3 stations, la grille d'observation, les 12 gestes du Passeport |
| [A2 — Conduite de séance](docs/annexes/A2-conduite-de-seance.md) | Le déroulé des 2 h minute par minute, les checklists avant/pendant/après, les scripts d'animation |
| [A3 — Matrice des cas particuliers](docs/annexes/A3-matrice-des-cas.md) | 35 cas (niveau, rythme, assiduité, matériel, émotionnel, cognitif, organisation, projet) avec détection et réponse |
| [A4 — Grades, badges & Mur de Mission](docs/annexes/A4-grades-et-badges.md) | Le système de motivation complet, et ce qu'il ne faut surtout pas faire |
| [A5 — Outils imprimables](docs/annexes/A5-outils-imprimables.md) | Cartes de signalisation, contrat de binôme, dictionnaire des erreurs, journal de bord, grille de test, tableau de suivi |

---

## 🗺️ Ossature du parcours

| Phase | Séances | Brique ajoutée au jeu | Notions Python |
|---|---|---|---|
| 0. Décollage | 1 | Premier programme, premier message affiché | environnement, exécution |
| 1. Parler au joueur | 2–5 | Le jeu dit bonjour, demande les noms, affiche un plateau vide | variables, `input()`, `print()`, types |
| 2. Le plateau vit | 6–9 | On place un X ou un O, les joueurs alternent | listes, indices, conditions, boucles |
| 3. Les règles du jeu | 10–13 | Coups invalides refusés, gagnant détecté, match nul | fonctions, `while`, opérateurs logiques |
| 4. L'interface graphique | 14–18 | Fenêtre, grille cliquable, personnalisation | Tkinter, événements, callbacks |
| 5. Finition & intelligence | 19–22 | Score, sons, **IA de l'ordinateur**, distribution | organisation du code, algorithmes |

> Le découpage détaillé séance par séance fera l'objet du document suivant, une fois la méthode validée.

---

## 📌 État du projet

- [x] Méthode pédagogique complète
- [x] Outils de diagnostic et de suivi
- [x] Annexes opérationnelles imprimables
- [ ] Découpage détaillé des 22 séances
- [ ] Supports élèves (fiches mémo, fichiers à trous par piste)
- [ ] Code de référence du jeu XO, version par version
