# 📊 Le suivi

## Le classeur principal : votre fichier d'inscriptions

**[`AcProKidsCodingCampSept2026.xlsx`](AcProKidsCodingCampSept2026.xlsx)**

Vos deux feuilles d'origine — **Enfants** et **Parents** — sont **intactes**, formules et mises en forme comprises.
Les onglets de suivi ont été ajoutés à la suite :

| Onglet | À quoi il sert |
|---|---|
| **Présence** | Les 22 séances. `P` présent · `R` retard · `E` excusé · `A` absent. Le taux se calcule seul et passe en rouge sous 85 % |
| **Diagnostic** | Le Test de Décollage : pilotage /6, logique /4, profil P0→P3. **Interne : jamais communiqué aux élèves ni aux familles** |
| **Suivi** | Ce que chaque élève a produit à chaque séance, et sur quelle piste. **Colonne ALERTE automatique** |
| **Observations** | Le journal : un fait marquant, l'action décidée, et si elle a été faite |
| **Journal** | La revue d'après-séance. **Une ligne par séance ET par classe** : chaque enseignant remplit la sienne |
| **Indiscipline** | Le registre demandé par le responsable : un fait par ligne, la sanction, et le **compteur d'avertissements par apprenant** |
| **Révisions maison** | Ce qui revient des deux envois de la semaine. `O` = a répondu · `N` = rien reçu |

### Les deux onglets financiers

| Onglet | À quoi il sert |
|---|---|
| **Cotisations** | Qui est à jour. Une colonne par mois, de septembre à juin. On écrit le **montant reçu** dans la case du mois ; le total, le solde et le statut se calculent seuls |
| **Caisse** | Le journal de l'argent : **entrées et sorties**, avec catégorie, moyen de paiement et numéro de pièce. Le solde se calcule seul |

**Cotisations — deux réglages seulement**, dans les cases crème en haut :

- **Montant mensuel** : 50 DH.
- **Mois dus à ce jour** : mettez `1` en septembre, `2` en octobre, et ainsi de suite. **C'est le seul geste à ne pas oublier au début de chaque mois** — c'est lui qui fait basculer les élèves en retard.

Le statut se met à jour tout seul : **À jour** sur fond vert clair, ou **« Doit 50 DH »** sur fond rose.
La dernière ligne donne le total encaissé par mois, le total dû et le reste à recouvrer.

**Caisse — le contrôle automatique.** Les cotisations encaissées se notent **aussi** dans la Caisse, en
*Entrée* / catégorie *Cotisation*. La case **« Contrôle cotisations »** compare les deux onglets :

> **Elle doit toujours afficher 0 DH.** Si elle affiche autre chose, c'est qu'un encaissement a été noté dans un
> onglet et pas dans l'autre. C'est le seul moyen simple de ne pas perdre d'argent en route.

> ⚠️ **Attention au doublon :** votre feuille `Enfants` a déjà des colonnes *Participation*, *Montant* et
> *Date de Paiement*. Elles conviennent bien pour le **paiement d'inscription**. Pour les **cotisations
> mensuelles**, utilisez l'onglet `Cotisations` — sinon vous aurez deux vérités et aucune ne sera fiable.

### L'onglet Indiscipline

Une ligne par fait : la date, la séance, la classe, l'apprenant, ce qui s'est passé, la sanction, et si la
famille a été informée. **La ligne passe en rose dès que la sanction est un avertissement.**

Deux valeurs seulement dans la colonne *Sanction*, celles du règlement :

- **Observation verbale** — pour un premier écart léger. Ce **n'est pas** un avertissement.
- **Avertissement** — notifié par écrit à la famille.

À droite du registre, le **compteur par apprenant** se calcule tout seul : observations verbales,
avertissements, et statut. À **1 avertissement**, la case passe en crème. À **2**, elle affiche
**« RENVOYÉ — 2 avertissements »** en rouge : c'est l'article 8 du règlement.

> Le nom de l'apprenant se choisit dans une liste déroulante alimentée par la feuille `Enfants` —
> c'est ce qui fait marcher le compteur. **Un nom tapé à la main ne sera pas compté.**

### L'onglet Révisions maison

Deux colonnes par séance : `S01-1` pour le premier envoi de la semaine, `S01-2` pour le second.
On écrit `O` si l'apprenant a renvoyé ses réponses, `N` si rien n'est revenu, et **on laisse vide
si l'envoi n'a pas été fait** — c'est ce qui rend le taux juste : il compare ce qui est revenu à ce
qui a réellement été envoyé.

Les envois eux-mêmes sont dans le dossier de la séance :
[`2-seances/S01-decollage/a-envoyer/revisions-maison/`](../2-seances/S01-decollage/a-envoyer/revisions-maison/messages-a-copier.md)

### La règle d'or

**On saisit les noms une seule fois, dans la feuille `Enfants`.** Les autres onglets les recopient automatiquement,
avec la classe. Si un nom manque ailleurs, c'est qu'il manque dans `Enfants`.

**Le code couleur, identique partout :** les cellules **crème** se remplissent à la main · le **texte vert** est
calculé, n'écrivez pas dedans · le **rose** signale ce qui demande une action (retard de paiement, décrochage).
Tout le classeur est en **Candara**, avec les bandeaux verts de votre charte.
Les onglets ont de la place pour **40 élèves** — il y en a 15 aujourd'hui (7 Jerusalem, 8 Jeremiah).

### Le déclencheur à surveiller

Dans l'onglet **Suivi**, la colonne **ALERTE** passe à `OUI` dès qu'un élève cumule **deux séances de suite
sans production**. Cet élève entre sur la **liste des 10 minutes** : l'enseignant lui consacre 10 minutes en
tête-à-tête à la séance suivante, pendant que le reste de la classe travaille en binôme.

C'est un rendez-vous, pas une punition — et c'est ce qui empêche un décrochage silencieux de devenir un abandon.

### L'importer dans Google Sheets

Drive → `Nouveau` → `Importation de fichier` → puis `Fichier` → `Enregistrer au format Google Sheets`.
`Partager` → **accès restreint**, uniquement les deux enseignants.

> ⚠️ Ce classeur contient les coordonnées de mineurs. Il ne doit **jamais** être publié ni partagé par lien public.

---

## Un seul classeur

Il n'y a **qu'un seul fichier de suivi**, celui-ci. L'ancien `classeur-de-suivi.xlsx`, construit avant que
vous fournissiez votre fichier d'inscriptions, a été retiré : ses onglets faisaient double emploi avec les
vôtres et créaient deux vérités.

Trois suivis qu'il contenait n'ont pas été repris, faute d'être utilisés pour l'instant :
**les binômes**, **les badges et grades**, et **le Passeport Machine**. Dites-le-moi et je les ajoute
comme onglets de ce classeur-ci, dans la même charte.
