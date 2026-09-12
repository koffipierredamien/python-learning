# 📜 Administratif

Les documents officiels de la formation : ceux qu'on remet aux familles et qui engagent les deux parties.

## Le règlement intérieur

| Fichier | À quoi il sert |
|---|---|
| **[`reglement-interieur.pdf`](reglement-interieur.pdf)** | La version à **imprimer et à remettre** — 4 pages, le coupon d'engagement sur la dernière |
| **[`reglement-interieur.docx`](reglement-interieur.docx)** | La version **Word, modifiable** — pour le responsable, s'il veut retoucher un mot ou l'en-tête |
| `sources/reglement-interieur.html` | La source du PDF. On n'y touche pas à la main (voir plus bas) |

**À imprimer :** 1 exemplaire par famille — **15 exemplaires**, recto verso, agrafés.
Chaque famille garde le règlement et **rend le coupon signé** (dernière page, détachable).

### Le régime disciplinaire, en trois lignes

1. Un premier écart léger → **observation verbale**. Ce n'est **pas** un avertissement : elle sert à corriger avant de sanctionner.
2. **Avertissement**, notifié par écrit à la famille, pour : absence ou retard de plus de 10 minutes non signalé et non justifié · indiscipline (manque de respect, moqueries, agitation, refus de consigne) · manque de diligence répété après rappel · dégradation volontaire du matériel.
3. **Au 2ᵉ avertissement, l'apprenant est renvoyé.** Un fait grave (violence, vol, mise en danger) entraîne l'exclusion immédiate.

### Trois garde-fous volontairement inscrits dans le texte

Ils ne figuraient pas dans la consigne : ils sont là pour que le règlement reste tenable et cohérent
avec la méthode. **Dites-le et je les retire.**

- **Une difficulté de paiement ne donne lieu à aucun avertissement** (article 3). Elle se traite en privé.
- **Les défis à la maison restent facultatifs**, et aucun avertissement ne peut être donné pour un travail
  non fait à la maison (article 6) — tous les apprenants n'ont pas d'ordinateur chez eux.
- **L'article 11 dit ce que l'équipe s'engage à donner en retour** : aucune note, aucun classement, un projet
  qui avance à chaque séance, une absence qui ne met jamais personne en retard, aucune moquerie tolérée.
  Un règlement qui n'exige que d'un seul côté se retourne toujours contre celui qui l'a écrit.

### L'en-tête de la vision

Le bandeau que vous m'avez montré est arrivé **comme image dans la conversation, pas comme fichier**.
En attendant, le texte a été reproduit à l'identique (nom, devise, références, mention CIE-MIA).

**Pour mettre votre vraie image :** déposez-la ici sous le nom **`en-tete.png`** (ou `.jpg`), puis relancez
la fabrication ci-dessous. Elle prend automatiquement la place du bandeau de texte, dans le Word **et** dans
le PDF, et se répète en haut de chaque page.

## Refabriquer les deux versions

Le texte du règlement est écrit **une seule fois**, dans `4-outils/faire_le_reglement.py`.
Le Word et le PDF en sortent tous les deux : ils ne peuvent donc pas se contredire.

```
python 4-outils/faire_le_reglement.py      # écrit le .docx et la source .html
python 4-outils/faire_les_pdf.py --reglement   # écrit le .pdf
```

> Si vous corrigez directement le `.docx`, la correction sera **perdue** au prochain lancement.
> Pour qu'elle tienne, corrigez le texte dans `4-outils/faire_le_reglement.py` (il est en clair,
> article par article), ou dites-le-moi.
