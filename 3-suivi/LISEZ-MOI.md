# 📊 Le suivi

## Le classeur principal : votre fichier d'inscriptions

**[`InscriptionsAcProKidsCodingCampSept2026.xlsx`](InscriptionsAcProKidsCodingCampSept2026.xlsx)**

Vos deux feuilles d'origine — **Enfants** et **Parents** — sont **intactes**, formules et mises en forme comprises.
Cinq onglets de suivi ont été ajoutés à la suite :

| Onglet | À quoi il sert |
|---|---|
| **Présence** | Les 22 séances. `P` présent · `R` retard · `E` excusé · `A` absent. Le taux se calcule seul et passe en rouge sous 85 % |
| **Diagnostic** | Le Test de Décollage : pilotage /6, logique /4, profil P0→P3. **Interne : jamais communiqué aux élèves ni aux familles** |
| **Suivi** | Ce que chaque élève a produit à chaque séance, et sur quelle piste. **Colonne ALERTE automatique** |
| **Observations** | Le journal : un fait marquant, l'action décidée, et si elle a été faite |
| **Journal** | La revue d'après-séance. **Une ligne par séance ET par classe** : chaque enseignant remplit la sienne |

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

### La règle d'or

**On saisit les noms une seule fois, dans la feuille `Enfants`.** Les cinq onglets les recopient automatiquement,
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

## L'autre fichier : `classeur-de-suivi.xlsx`

[`classeur-de-suivi.xlsx`](classeur-de-suivi.xlsx) était le classeur complet construit avant que vous
fournissiez votre fichier d'inscriptions. **Il n'est plus le classeur de référence.**

Il garde cependant six onglets qui n'existent pas ailleurs et qui restent utiles :

`06_Binomes` · `07_Badges-Grades` · `08_Passeport` · `09_Checklist-S01` · `11_Materiel` · `12_Tableau-de-bord`

> ⚠️ **Ses onglets `01_Apprenants`, `02_Diagnostic`, `03_Presence`, `04_Suivi-seances`, `05_Observations` et
> `10_Journal-enseignants` font maintenant double emploi : ne les utilisez pas.** Le suivi réel se fait dans le
> fichier d'inscriptions.
>
> Dites-moi quand vous voulez, et je fusionne les six onglets utiles dans votre fichier d'inscriptions pour
> n'avoir plus qu'un seul classeur.
