# Annexe A1 — Test de Décollage & Passeport Machine

> **À dire aux élèves :** « On va faire trois jeux pour préparer le décollage. Il n'y a pas de note, il n'y a pas de bonne équipe. Ça sert juste à nous, les profs, à bien vous accompagner. »
> **À ne jamais faire :** annoncer un « test de niveau », communiquer un résultat, comparer deux élèves à voix haute.

---

## 1. Organisation pratique

- **Durée :** 25 minutes, en 3 stations tournantes.
- **Où :** pendant la séance 1, juste après l'accueil.
- **Qui :** l'enseignant lance la station 1 (machines), puis circule entre les stations 2 et 3 et note ce qu'il observe directement dans l'onglet `Diagnostic` du classeur.
- **Groupes :** la classe est divisée en 3 sous-groupes qui tournent toutes les 8 minutes.

---

## 2. Station 1 — Le pilotage (8 min, sur machine)

L'élève reçoit une carte-mission illustrée. On observe, on n'aide qu'après 60 secondes de blocage.

| # | Mission | Ce qu'on observe |
|---|---|---|
| 1 | Allume l'ordinateur et ouvre une session | Sait démarrer seul ? |
| 2 | Ouvre le dossier `GEEKS` sur le Bureau | Double-clic, navigation |
| 3 | Crée un fichier texte nommé avec ton prénom | Clic droit, nommage |
| 4 | Écris dedans : ton prénom, ton âge, ton jeu préféré | Vitesse et posture de frappe |
| 5 | Enregistre le fichier | Comprend la notion d'enregistrement ? |
| 6 | Ferme la fenêtre, puis retrouve ton fichier | Comprend qu'un fichier « existe quelque part » ? |

**Cotation rapide (pour l'enseignant uniquement) :**
- 0–2 missions réussies seules → **P0 Découvreur**
- 3–4 → **P0/P1 limite** (à confirmer séance 2)
- 5–6 rapidement → **P1 ou plus**

---

## 3. Station 2 — La logique (8 min, sur papier, sans ordinateur)

Quatre énigmes, ordre libre. **On ne cherche pas les bonnes réponses, on cherche la manière de raisonner.**

**Énigme 1 — Remets dans l'ordre (algorithme séquentiel)**
Six vignettes mélangées : « préparer un sandwich », « se brosser les dents » ou « faire une partie de morpion ». L'élève les numérote.

**Énigme 2 — Le robot aveugle (instructions et exécution)**
Un quadrillage 5×5, un robot, un trésor, des obstacles. L'élève écrit la suite d'instructions (`avance`, `tourne à gauche`, `tourne à droite`) pour atteindre le trésor.
→ *Observation clé : sait-il se mettre à la place du robot ?*

**Énigme 3 — Trouve la règle (abstraction)**
`2, 4, 6, 8, ...` puis `1, 2, 4, 8, ...` puis une suite de formes. L'élève complète **et** écrit la règle en une phrase.
→ *Observation clé : arrive-t-il à formuler la règle, pas seulement à deviner la suite ?*

**Énigme 4 — Explique le morpion à un extraterrestre (décomposition)**
« Un extraterrestre ne connaît pas le morpion. Écris toutes les règles pour qu'il puisse y jouer sans se tromper. »
→ *C'est l'énigme la plus riche du test : elle prépare directement le projet, et révèle la capacité à décomposer un problème. On la garde et on la relit à la séance 10.*

---

## 4. Station 3 — L'expérience (5 min, questionnaire à cocher)

```
Prénom : ______________________  Âge : ______  Classe : ☐ Jerusalem  ☐ Jeremiah

1. As-tu un ordinateur à la maison ?        ☐ Oui, à moi  ☐ Oui, partagé  ☐ Non
2. As-tu internet à la maison ?             ☐ Oui  ☐ Parfois  ☐ Non
3. Combien de fois utilises-tu un ordinateur par semaine ?
                                            ☐ Jamais  ☐ 1-2 fois  ☐ Presque tous les jours
4. As-tu déjà programmé ?
   ☐ Jamais   ☐ Scratch   ☐ Python   ☐ Autre : __________
5. Sais-tu lire un peu l'anglais ?          ☐ Non  ☐ Un peu  ☐ Oui
6. Pourquoi veux-tu apprendre à coder ?  (une phrase, libre)
   ______________________________________________________________
7. Ton jeu préféré ?  ____________________
```

> Les questions 6 et 7 ne servent pas au diagnostic : elles servent à **personnaliser les exemples en classe**. Un enfant qui aime le football retiendra mieux une variable nommée `score_equipe`.

---

## 5. Ce qu'on note pour chaque élève

Directement dans l'onglet `Diagnostic` du [classeur de suivi](../../3-suivi/LISEZ-MOI.md) :

| Élève | Pilotage /6 | Logique /4 | A déjà codé | Face à la difficulté | Profil retenu |
|---|---|---|---|---|---|
| | | | | ☐ abandonne ☐ demande ☐ persévère ☐ aide les autres | P0 / P1 / P2 / P3 |

**La colonne « face à la difficulté » est la plus importante du tableau.** Un P0 persévérant progressera plus vite qu'un P2 qui abandonne au premier message d'erreur, et c'est celui-là qu'il faudra soutenir en priorité — pas sur la technique, mais sur la confiance.

---

## 6. Le Passeport Machine — 12 gestes à valider

Petit livret A5 (ou carte plastifiée) remis à **tous** les élèves — pas seulement aux débutants, pour éviter toute stigmatisation. Une case cochée par geste validé. Les P2/P3 le remplissent en une séance et deviennent **Examinateurs** (ils peuvent valider un geste chez un camarade, ce qui décharge les enseignants).

| # | Geste | Validé par |
|---|---|---|
| 1 | J'allume et j'éteins proprement l'ordinateur | |
| 2 | Je sais utiliser la souris : clic, double-clic, clic droit, glisser | |
| 3 | Je sais faire une majuscule, un accent, un point, une virgule | |
| 4 | Je trouve les touches spéciales : `Entrée`, `Effacer`, `Échap`, `#`, `(`, `)`, `:`, `_` | |
| 5 | J'ouvre, je réduis, j'agrandis et je ferme une fenêtre | |
| 6 | Je passe d'une fenêtre à l'autre | |
| 7 | Je crée un dossier et je le nomme | |
| 8 | J'enregistre un fichier au bon endroit | |
| 9 | Je retrouve un fichier que j'ai enregistré | |
| 10 | J'ouvre Thonny et je lance un programme | |
| 11 | Je copie mon projet depuis le dossier officiel | |
| 12 | Je tape 20 mots sans regarder mes doigts *(objectif du parcours, pas de la séance 1)* | |

**Le geste 12 est un objectif de fin de parcours**, travaillé 5 minutes chaque samedi pendant le rituel d'accueil, sous forme de record personnel à battre. On ne compare jamais les vitesses entre élèves.
