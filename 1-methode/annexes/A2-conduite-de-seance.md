# Annexe A2 — Fiche de conduite de séance

Document à imprimer et à avoir sous les yeux chaque samedi.

---

## 1. Checklist — la veille (30 min de préparation)

- [ ] Le **code officiel** de la séance précédente est finalisé, testé, et copié sur la clé / le dossier partagé
- [ ] La brique du jour est codée **en entier par l'enseignant**, sur une machine identique à celles des élèves
- [ ] Les **trois pistes** sont prêtes : fichier à trous (Bleue), consigne écrite (Rouge), défi ouvert (Noire)
- [ ] La **fiche mémo** de la séance est imprimée (1 par binôme) : les 5 lignes de syntaxe utiles du jour
- [ ] La **grille de test** pour la chasse aux bugs est imprimée
- [ ] La **version débranchée** de la séance est prête (plan B panne de courant / machines HS)
- [ ] Les post-it, badges, tampons, cartes de signalisation sont dans la boîte
- [ ] Les binômes du jour sont écrits sur une feuille (rotation tous les 3 samedis)
- [ ] La **liste des 10 minutes** est relue : qui a besoin d'un tête-à-tête aujourd'hui ?
- [ ] Les post-it « je ne suis pas sûr de ___ » de la semaine dernière sont relus → la notion la plus citée ouvre la séance

## 2. Checklist — 20 minutes avant

- [ ] Machines allumées, Thonny ouvert, dossier `xo_officiel` en place sur chaque poste
- [ ] Machine de réserve allumée en fond de salle
- [ ] Vidéoprojecteur testé, **police de l'éditeur agrandie** (taille 18 minimum)
- [ ] Le Mur de Mission et les affiches (Règle des 3 avant moi, Contrat de binôme) sont visibles
- [ ] Un message à mon collègue de l'autre classe : tout est prêt des deux côtés ?

---

## 3. Le déroulé, avec les scripts d'animation

### 12 h - 12 h 15 · Prière et accueil
> *« Bienvenue les Geeks ! Vous connaissez la routine : on allume, on ouvre le dossier officiel, et 5 minutes de clavier. Qui bat son record aujourd'hui ? »*

J'accueille à la porte, je repère les visages fermés, je note les absents.
**Dès la séance 3, cette phase est 100 % autonome** — la procédure est affichée au mur en 4 images.

### 12 h 15 - 12 h 25 · Le WOW puis le rappel
On lance **le jeu terminé de la séance** sur le vidéoprojecteur et on y joue 30 secondes avec un élève.
> *« Voilà ce que votre jeu saura faire dans deux heures. Vous êtes prêts ? »*

Puis 3 questions de rappel, réponse à main levée, **jamais interrogation individuelle** (un élève interrogé au hasard et qui ne sait pas répond une fois, et ne lève plus jamais la main).

### 12 h 25 - 12 h 40 · La notion
**Toujours dans cet ordre :**
1. **Débranché** (5 min) — avec le corps ou des objets. *Exemple pour les listes : sept élèves debout, chacun tient un carton numéroté de 0 à 6. « Le plateau, c'est vous. Élève numéro 4, lève ton carton : voilà `plateau[4]`. »*
2. **Live coding lent** (8 min) — l'enseignant tape en direct, très lentement, en verbalisant tout. **Règle : « je code, vous prédisez »** — s'arrêter avant chaque exécution : *« qu'est-ce qui va s'afficher ? À trois : un, deux, trois ! »*
3. **L'erreur volontaire** (2 min) — l'enseignant fait une faute réaliste (oubli des deux-points, indentation, `=` au lieu de `==`), montre le message d'erreur, **le lit à voix haute, le traduit en français**, et le répare.
   > *« Vous voyez ? Moi aussi je fais des erreurs, tout le temps. La différence, c'est que je sais lire ce que l'ordinateur me dit. »*

### 12 h 40 - 13 h · Atelier 1 · 13 h 10 - 13 h 35 · Atelier 2
Annonce systématique avant de lâcher la classe :
> *« Atelier 1 : mission = ___ . Piste Bleue si vous voulez être guidés, Rouge pour le niveau normal, Noire si vous voulez du défi. Cartes de signalisation sorties. Pilote et copilote : vous savez qui vous êtes. Rotation dans 10 minutes. C'est parti ! »*

Pendant l'atelier :
- **C'est le moment où je circule** : je ne m'adresse plus au groupe. Circuit en U, en commençant par la zone des profils P0.
- Je sers les cartes orange en moins de 5 minutes, les rouges tout de suite. Je nomme **2 Geek Mentors** dès les premières cartes bleues.
- **Signal sonore de rotation** pilote/copilote toutes les 10 à 12 minutes (minuteur visible au mur ou projeté).

**Comment aider sans faire à la place — les 4 phrases autorisées :**
1. *« Lis-moi ton message d'erreur à voix haute. »*
2. *« Montre-moi la ligne où ça se passe. Qu'est-ce que tu voulais qu'elle fasse ? »*
3. *« Qu'est-ce qui se passerait si on mettait 5 ici ? Essaie. »*
4. *« Explique-moi cette ligne comme si j'étais ton petit frère. »*

**Interdit :** prendre le clavier de l'élève. Si vraiment nécessaire : demander la permission, taper au maximum une ligne, la commenter à voix haute, puis rendre le clavier immédiatement.

### 13 h 35 - 13 h 47 · Chasse aux bugs croisée
> *« Vous changez de place : binôme 1 va tester le jeu du binôme 2. Votre mission : le faire planter. Vous avez la grille de test. Tout bug trouvé = un badge Chasseur de bug pour vous, et un badge Testeur impitoyable si vous expliquez gentiment comment le réparer. »*

C'est la phase qui **absorbe naturellement les écarts de rythme** : les binômes rapides deviennent testeurs et Geek Mentors, les binômes lents finissent leur brique pendant qu'on teste leur jeu.

### 13 h 47 - 13 h 55 · Mise en commun
- 2 binômes montrent (2 min chacun) — **tenir la liste de passage** pour que tout le monde passe au moins une fois par mois. Un binôme timide passe en duo avec l'enseignant à côté de lui.
- Récapitulatif en 3 phrases maximum, écrites au tableau.
- **Publication du nouveau code officiel** (clé USB / dossier partagé), devant les élèves : c'est un moment rituel, on le fait solennellement.
- Distribution du défi maison **facultatif**, en insistant : *« Ceux qui n'ont pas d'ordinateur à la maison : ce n'est pas grave du tout, vous ne serez jamais en retard à cause de ça. »*

### 13 h 55 - 14 h · Clôture rituelle
1. Remise des badges et des grades, avec applaudissements.
2. Avancée du **Mur de Mission** par un élève désigné.
3. Post-it : *« aujourd'hui j'ai compris ___ , je ne suis pas encore sûr de ___ »*, déposé dans la boîte en sortant.
4. Rangement, extinction des machines (c'est aussi un geste du Passeport).

---

## 4. Checklist — après la séance (15 min seul, puis 10 min avec mon collègue)

- [ ] Tableau de suivi complété (`✔` / `~` / `✖` + piste)
- [ ] Post-it lus et triés : quelle notion revient le plus ?
- [ ] **Liste des 10 minutes** mise à jour (deux `~`/`✖` consécutifs = rendez-vous individuel la semaine prochaine)
- [ ] Message aux familles envoyé (2 lignes)
- [ ] Code officiel de la séance archivé et daté
- [ ] Les 3 questions de la revue notées dans l'onglet `Journal` du classeur — **une ligne par classe** :
  1. Qui a décroché aujourd'hui, et qu'est-ce qu'on fait samedi prochain ?
  2. Quelle explication n'a pas fonctionné, et comment on la reformule ?
  3. La brique de la semaine prochaine est-elle trop grosse ?

---

## 5. Les signaux d'alerte pendant la séance

| Signal | Interprétation | Action immédiate |
|---|---|---|
| Plus de 3 cartes orange sur la même difficulté | L'explication a échoué, pas les élèves | **J'arrête tout** et je reprends la notion devant, autrement |
| Un binôme reste vert mais n'avance pas | Décrochage silencieux ou copie sans comprendre | Je demande : *« explique-moi cette ligne »* |
| Un élève regarde son binôme taper sans rien dire | Rôle de copilote non tenu | Rotation immédiate des rôles |
| Un élève range ses affaires 20 min avant la fin | Perte de sens ou frustration | Tête-à-tête de 2 min, hors du groupe, sans reproche |
| Le brouhaha monte d'un coup | Consigne pas comprise ou atelier trop long | Reformuler la consigne en une seule phrase au tableau |
| Un élève finit systématiquement en 5 min | Sous-alimenté | Passage en piste Noire + attribution d'une mission spéciale |
