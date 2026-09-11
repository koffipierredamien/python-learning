# 🖨️ Dossier d'impression — Séance 1

## En bref : que faire de ces fichiers ?

**Prenez les PDF, ignorez le reste.** Tout est déjà converti, au bon format de papier, prêt pour l'imprimeur.

```
impressions/
├── pdf/            ←  C'EST ICI. Ouvrez, imprimez. Rien d'autre à faire.
└── *.html             les fichiers sources, seulement si vous voulez modifier un document
```

- **Pour imprimer :** ouvrez le PDF, `Ctrl+P`, vérifiez le format de papier indiqué dans le tableau ci-dessous, et lancez. Les couleurs et les cadres sont déjà inclus dans le PDF — vous n'avez **aucune** option à cocher.
- **Pour faire imprimer en boutique :** donnez-leur le dossier `pdf/` sur une clé, avec le tableau ci-dessous.
- **Pour vos responsables :** le PDF `00-FICHE-DE-VALIDATION-responsables.pdf` est fait pour un **envoi numérique** — il s'envoie par mail tel quel, et n'a pas besoin d'être imprimé. Renseignez la date prévue dans l'en-tête avant de l'envoyer.

> Les fichiers `.html` sont les **sources**. Un fichier HTML est une page web : si vous double-cliquez dessus, il s'ouvre dans votre navigateur et vous pouvez aussi l'imprimer avec `Ctrl+P` — mais il faut alors penser à cocher **« Graphiques d'arrière-plan »**. Les PDF vous évitent ça. Ne gardez les HTML que si vous voulez corriger un texte : voir « Modifier un document » en bas de page.

---

## La liste de courses de la séance 1

| # | Document (dans `pdf/`) | Papier | Pages | Combien | Pour qui |
|---|---|---|---|---|---|
| — | `00-MON-SCRIPT-animation.pdf` | A4 | **14** | 1, agrafé | **L'animateur** (la dernière page se détache pour le Mécanicien) |
| — | `00-FICHE-DE-VALIDATION-responsables.pdf` | A4 | 2 | **à envoyer par mail**, pas à imprimer | Les responsables |
| 01 | `01-cartes-signalisation.pdf` | A4 **couleur** | 1 | **1 par binôme** | Élèves — à découper et plastifier |
| 02 | `02-affiche-3-avant-moi.pdf` | **A3** couleur | 1 | 1 | Mur |
| 03 | `03-affiche-contrat-binome.pdf` | **A3** couleur | 1 | 1 | Mur |
| 04 | `04-affiche-dictionnaire-erreurs.pdf` | **A3** couleur | 1 | 1 | Mur |
| 05 | `05-mur-de-mission.pdf` | **A3 paysage** | 1 | 1 | Mur |
| 06 | `06-fiche-memo-eleve.pdf` | A4 | 1 | **1 par binôme** | Élèves — sur la table |
| 07 | `07-station1-cartes-missions.pdf` | A4 | 1 | 6 | Test — à découper |
| 08 | `08-station2-enigmes.pdf` | A4 **recto-verso** | 2 | 6 | Test |
| 09 | `09-station3-questionnaire.pdf` | A4 | 1 | **1 par élève** | Test |
| 10 | `10-grille-observation.pdf` | A4 **paysage** | 3 | 2 | **Enseignants** |
| 11 | `11-etiquettes-prenoms.pdf` | A4 | 1 | 3 (= 24 étiquettes) | Élèves — à découper |
| 12 | `12-affiche-4-phrases-enseignant.pdf` | A4 | 1 | 2 | **Enseignants** |
| 13 | `13-cartes-pistes.pdf` | A4 **couleur** | 1 | **1 par binôme** | Élèves — à découper |

### Total pour une classe de 20 élèves (10 binômes)

| | Pages |
|---|---|
| A4 noir et blanc | ≈ 75 |
| A4 couleur | ≈ 20 (documents 01 et 13) |
| A3 couleur | 4 |

> ⚠️ **Les pages 2 et 3 du document 10 contiennent les corrigés des énigmes.** Ne les laissez pas traîner sur une table pendant le test.

---

## Ce qui n'est PAS imprimé (décision assumée)

| Support écarté | Ce qui le remplace |
|---|---|
| Contrat de binôme individuel à signer | **L'affiche 03** + un engagement collectif à voix haute (rituel 4, à 65 min) |
| Passeport Machine (livret 12 gestes) | Validation **orale** + badge, suivi dans le classeur, onglet `08_Passeport` |
| Journal de bord (carnet A5) | **2 post-it par élève**, déposés dans la boîte en sortant |
| Tableau de suivi papier | Le **classeur de suivi** Google Sheets |

---

## Matériel à acheter (non imprimable)

- Post-it : **2 par élève et par séance** — prévoir large
- Feutres noirs à pointe large (étiquettes prénoms et affiches à compléter)
- Autocollants / gommettes de couleur → servent de **badges** (une couleur par badge)
- Papier épais 160 g pour les cartes de signalisation, ou pochettes de plastification
- Ruban adhésif ou porte-badges pour les étiquettes
- Un minuteur visible de toute la salle (ou un chronomètre projeté)
- Une boîte / un bocal pour les post-it de sortie
- Une clé USB (voir [`../cle-usb/`](../cle-usb/README.md))

---

## Modifier un document

Les `.html` sont les sources. Ouvrez-en un avec un éditeur de texte (le Bloc-notes suffit), corrigez le texte
entre les balises, enregistrez. Puis, pour refabriquer le PDF : ouvrez le fichier dans Chrome → `Ctrl+P` →
destination **« Enregistrer au format PDF »** → enregistrez dans `pdf/` sous le même nom.

Pas d'imprimante A3 ? Imprimez en A4 avec l'option **« Ajuster à la page »** : les affiches restent lisibles.
Pour le Mur de Mission, imprimez-le en A3 et collez-le sur une grande feuille de papier kraft.
