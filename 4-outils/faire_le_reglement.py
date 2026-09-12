# -*- coding: utf-8 -*-
"""
=============================================================================
  FABRIQUER LE RÈGLEMENT INTÉRIEUR
=============================================================================
  Le texte du règlement est écrit UNE SEULE FOIS ci-dessous. Le programme en
  produit deux versions, qui ne peuvent donc pas diverger :

      0-administratif/reglement-interieur.docx   modifiable (Word)
      0-administratif/sources/reglement-interieur.html   -> PDF via faire_les_pdf.py

  L'EN-TÊTE. Déposez votre bandeau dans  0-administratif/en-tete.png  (ou .jpg)
  et relancez : il est alors placé en haut du Word et du PDF. Tant que le
  fichier n'est pas là, un bandeau de texte reprend le vôtre à l'identique.

  Utilisation :  python 4-outils/faire_le_reglement.py
  Nécessite   :  pip install python-docx
=============================================================================
"""
import os, sys, html

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOSSIER = os.path.join(RACINE, "0-administratif")

# ---------------------------------------------------------------- l'en-tête
ENTETE = {
    "org": "VISION PLÉNITUDES VIE",
    "devise": "« La Vie de Christ dans toutes Ses plénitudes »",
    "refs": "Jn 1.16-18 · Col 1.27 · 2.2-3, 9-10 · Ep 1.3 · Ps 119.96-105",
    "badge": "Vision soumise au CIE-MIA",
}

NOMS_D_ENTETE = ("en-tete.png", "en-tete.jpg", "en-tete.jpeg")


def image_d_entete():
    """Le bandeau fourni par la vision, s'il a été déposé dans 0-administratif/."""
    for nom in NOMS_D_ENTETE:
        chemin = os.path.join(DOSSIER, nom)
        if os.path.isfile(chemin):
            return chemin
    return None


TITRE = "RÈGLEMENT INTÉRIEUR"
SOUS_TITRE = "AcProKids Coding Camp — Initiation à la programmation"
LIGNE_INFO = ("Jerusalem Geeks (9 – 12 ans)  ·  Jeremiah Geeks (12 – 18 ans)   |   "
              "Chaque samedi, de 12 h à 14 h   |   Tabernacle Sagesse Divine")

PREAMBULE = (
    "Les apprenants du AcProKids Coding Camp ont été choisis parmi de nombreuses candidatures. "
    "Cette place est à la fois un privilège et un engagement : la formation est gratuite dans son "
    "esprit, exigeante dans sa conduite, et elle demande à chacun du sérieux.\n"
    "Le présent règlement dit clairement ce que la formation attend de l'apprenant et de sa famille, "
    "et ce que l'équipe pédagogique s'engage à leur donner en retour. Il est remis à chaque famille "
    "et signé par l'apprenant et son responsable légal."
)

# (titre, [paragraphes ou (liste, [items])])
ARTICLES = [
("Article 1 — Objet du règlement", [
 "Le présent règlement fixe les règles de fonctionnement, de discipline et d'assiduité du AcProKids "
 "Coding Camp, organisé par Vision Plénitudes Vie. Il s'applique à tous les apprenants inscrits, à "
 "leurs responsables légaux et à l'équipe pédagogique, pendant toute la durée de la formation.",
]),
("Article 2 — Organisation de la formation", [
 ("liste", [
  "**Deux classes** : **Jerusalem Geeks** (9 à 12 ans) — Découvrir · Apprendre · Créer ; "
  "**Jeremiah Geeks** (12 à 18 ans) — Coder · Développer · Progresser.",
  "**Un enseignant par classe**, les deux classes se déroulant en parallèle.",
  "**Séances** : chaque samedi, de **12 h à 14 h**, soit deux heures.",
  "**Lieu** : Tabernacle Sagesse Divine.",
  "**Début des cours** : samedi 12 septembre 2026.",
  "**Contenu** : initiation à la programmation en Python, autour d'un projet unique construit "
  "brique par brique sur l'ensemble du parcours.",
 ]),
 "Toute modification durable des horaires ou du lieu est communiquée aux familles à l'avance.",
]),
("Article 3 — Participation financière", [
 ("liste", [
  "La participation est de **50 DH par mois et par apprenant**. Elle est symbolique : elle couvre "
  "une partie du matériel, des impressions et des consommables.",
  "Elle est versée **au début de chaque mois**, auprès de l'enseignant de la classe ou de la "
  "personne désignée par la coordination.",
  "Un suivi des versements est tenu par la coordination et peut être consulté par la famille à tout moment.",
 ]),
 "**Une difficulté de paiement ne prive jamais un enfant de la formation.** Elle se signale à la "
 "coordination, se traite en privé, et **ne donne lieu à aucun avertissement**.",
]),
("Article 4 — Assiduité et ponctualité", [
 "La présence est attendue à **toutes** les séances. L'apprenant se présente au plus tard à 12 h, "
 "prêt à commencer.",
 ("liste", [
  "Toute **absence** et tout **retard de plus de 10 minutes** doivent être **signalés avant la séance** "
  "au **+212 680 706 164**, avec un motif.",
  "Une absence ou un retard de plus de 10 minutes **non signalé et non justifié par un motif valable "
  "entraîne un avertissement**.",
  "Sont considérés comme motifs valables : la maladie, une obligation familiale majeure, un empêchement "
  "de transport imprévu, et toute situation appréciée comme telle par la coordination.",
 ]),
 "Après **trois séances manquées consécutives**, même justifiées, un entretien est proposé à la famille "
 "pour faire le point. Cet entretien n'est pas une sanction.",
]),
("Article 5 — Comportement, respect et discipline", [
 "La règle première de la salle est le respect : de l'enseignant, des camarades, du lieu et du matériel. "
 "Personne ne se moque de celui qui n'a pas compris ou qui va moins vite.",
 "**Entraîne un avertissement** tout comportement d'indiscipline, notamment :",
 ("liste", [
  "parler mal ou manquer de respect à un enseignant ou à un camarade ;",
  "se moquer d'un camarade, l'humilier ou l'exclure ;",
  "être turbulent au point de gêner le travail des autres ;",
  "perturber le déroulement du cours de façon répétée ;",
  "refuser d'obéir à une consigne de l'enseignant.",
 ]),
]),
("Article 6 — Diligence et travail", [
 "La diligence est l'application sérieuse au travail demandé **pendant la séance**. Elle se manifeste "
 "concrètement par le fait de :",
 ("liste", [
  "suivre les consignes données et faire le travail demandé pendant les deux heures ;",
  "apporter ses affaires et venir prêt à travailler ;",
  "signaler qu'on est bloqué plutôt que de rester silencieux et inactif ;",
  "tenir son rôle lorsqu'on travaille à deux, et laisser sa place à son binôme au moment prévu ;",
  "ranger son poste et éteindre sa machine en fin de séance.",
 ]),
 "**Un manque de diligence répété, après rappel de l'enseignant, entraîne un avertissement.**",
 "**Les défis à faire à la maison restent facultatifs** : tous les apprenants n'ont pas d'ordinateur chez "
 "eux, et **aucun avertissement ne peut être donné pour un travail non fait à la maison**.",
]),
("Article 7 — Matériel et locaux", [
 ("liste", [
  "Les ordinateurs sont confiés aux apprenants : ils s'en servent uniquement pour ce qui est demandé "
  "en cours. Les jeux et la navigation hors consigne sont interdits.",
  "Les téléphones restent éteints et rangés, sauf consigne contraire de l'enseignant.",
  "Il est interdit de boire et de manger à proximité des machines.",
  "Toute dégradation volontaire du matériel ou des locaux entraîne un avertissement, et sa réparation "
  "reste à la charge de la famille.",
 ]),
]),
("Article 8 — Avertissements et exclusion", [
 "Le régime disciplinaire est simple, et il est connu de tous dès le premier jour.",
 ("liste", [
  "**Une observation verbale** est faite d'abord pour un premier écart léger. Elle **n'est pas** un "
  "avertissement : elle sert à corriger avant de sanctionner.",
  "**L'avertissement** est prononcé pour les manquements prévus aux articles 4, 5, 6 et 7. Il est "
  "**notifié par écrit à la famille** et consigné dans le dossier de suivi de l'apprenant.",
  "**Au deuxième avertissement, l'apprenant est renvoyé de la formation.** L'exclusion est définitive.",
 ]),
 "L'exclusion est prononcée par la coordination de la formation, après information de la famille. "
 "Elle ne donne lieu à aucun remboursement des participations déjà versées.",
 "**Un fait grave** — violence, vol, propos injurieux répétés, mise en danger d'autrui — peut entraîner "
 "l'exclusion immédiate, sans passer par les avertissements.",
]),
("Article 9 — Sécurité et responsabilité", [
 ("liste", [
  "Les apprenants sont sous la responsabilité de l'équipe pédagogique **pendant les deux heures de "
  "cours uniquement**, dans l'enceinte du lieu de formation.",
  "L'accompagnement à l'arrivée et au départ relève des responsables légaux. La ponctualité à 14 h est "
  "demandée à chacun.",
  "Aucun apprenant ne quitte la salle pendant la séance sans l'accord de l'enseignant.",
  "Tout problème de santé, allergie ou traitement doit être signalé à l'inscription et mis à jour en "
  "cas de changement.",
  "En cas d'urgence, la famille est prévenue immédiatement et les secours sont appelés si nécessaire.",
 ]),
]),
("Article 10 — Droit à l'image", [
 "Des photographies ou de courtes vidéos peuvent être réalisées pendant les séances, pour la mémoire "
 "de la formation et la communication de Vision Plénitudes Vie.",
 "Elles ne sont utilisées qu'avec **l'accord écrit du responsable légal**, donné sur le coupon "
 "d'engagement ci-après. **Un refus n'a aucune conséquence** sur la participation de l'apprenant.",
]),
("Article 11 — Ce que l'équipe pédagogique s'engage à donner en retour", [
 "Les exigences ci-dessus ont une contrepartie. L'équipe s'engage à :",
 ("liste", [
  "**ne donner aucune note et n'établir aucun classement** : la progression se mesure sur ce que "
  "l'apprenant sait faire, pas sur une comparaison avec les autres ;",
  "faire en sorte que **chaque apprenant reparte de chaque séance avec un projet qui a avancé** ;",
  "garantir qu'**une absence ne met jamais un apprenant en retard** : le code de référence est "
  "redistribué à tous au début de chaque séance ;",
  "**ne tolérer aucune moquerie** dans la salle, d'où qu'elle vienne ;",
  "traiter les difficultés d'un apprenant **avec sa famille, en privé, jamais devant le groupe** ;",
  "informer les familles de la marche de la formation et répondre à leurs questions.",
 ]),
]),
("Article 12 — Communication avec les familles", [
 ("liste", [
  "Un message est adressé aux familles après chaque séance : ce qui a été appris, et où en est le projet.",
  "Le numéro **+212 680 706 164** est le point de contact pour toute absence, tout retard et toute question.",
  "Les familles signalent sans délai tout changement de numéro, d'adresse ou de situation de l'apprenant.",
 ]),
]),
("Article 13 — Entrée en vigueur", [
 "Le présent règlement entre en vigueur dès sa signature et vaut pour toute la durée de la formation. "
 "Un exemplaire est remis à chaque famille. Toute modification est portée à la connaissance des familles "
 "par écrit avant son application.",
 "**La signature du coupon ci-après vaut acceptation pleine et entière du présent règlement.**",
]),
]

ENGAGEMENT = [
 ("Nom et prénoms de l'apprenant", 1),
 ("Classe", 0),
 ("Nom et prénoms du responsable légal", 1),
 ("Téléphone du responsable légal", 0),
]

# =============================================================== version HTML
def faire_html():
    def gras(t):
        out, morceaux = "", t.split("**")
        for i, m in enumerate(morceaux):
            out += ("<b>%s</b>" % html.escape(m)) if i % 2 else html.escape(m)
        return out

    corps = []
    for titre, blocs in ARTICLES:
        corps.append('<h2>%s</h2>' % html.escape(titre))
        for b in blocs:
            if isinstance(b, tuple):
                corps.append("<ul>" + "".join("<li>%s</li>" % gras(i) for i in b[1]) + "</ul>")
            else:
                corps.append("<p>%s</p>" % gras(b).replace("\n", "<br>"))
    image = image_d_entete()
    if image is not None:
        import base64, mimetypes
        donnees = base64.b64encode(open(image, "rb").read()).decode("ascii")
        type_mime = mimetypes.guess_type(image)[0] or "image/png"
        bandeau = ('<img class="bandeau" src="data:%s;base64,%s" alt="%s">'
                   % (type_mime, donnees, html.escape(ENTETE["org"])))
    else:
        bandeau = ("""<div class="remplacer"><b>Bandeau provisoire.</b> Déposez votre image d'en-tête dans """
                   """<b>0-administratif/en-tete.png</b> puis relancez """
                   """<b>python 4-outils/faire_le_reglement.py</b> : elle prendra la place du texte ci-dessous. """
                   """(Cette note ne s'imprime pas.)</div>\n"""
                   """<div class="entete">\n"""
                   """  <div class="g">\n"""
                   """    <div class="org">\u271d {org}</div>\n"""
                   """    <div class="devise">{devise}</div>\n"""
                   """    <div class="refs">{refs}</div>\n"""
                   """  </div>\n"""
                   """  <div class="badge">{badge}</div>\n"""
                   """</div>""").format(
                       org=html.escape(ENTETE["org"]), devise=html.escape(ENTETE["devise"]),
                       refs=html.escape(ENTETE["refs"]), badge=html.escape(ENTETE["badge"]))

    champs = "".join(
        '<div class="champ"><span>%s</span><span class="ligne"></span></div>' % html.escape(n)
        for n, _ in ENGAGEMENT)

    return """<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>Règlement intérieur — AcProKids Coding Camp</title>
<style>
  html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  * {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; box-sizing:border-box; }}
  @page {{ size: A4 portrait; margin: 14mm 15mm 13mm; }}
  body {{ margin:0; font-family: Candara, Calibri, Arial, sans-serif; font-size:10.5pt; color:#111; line-height:1.42; }}
  .remplacer {{ font-size:8.5pt; color:#7a7a7a; border:1px dashed #b0b0b0; padding:2mm; margin-bottom:3mm; }}
  @media print {{ .remplacer {{ display:none; }} }}
  .bandeau {{ display:block; width:100%; height:auto; margin-bottom:5mm;
              border-bottom:1mm solid #356854; padding-bottom:2.5mm; }}
  .entete {{ display:flex; align-items:flex-start; gap:6mm; border-bottom:1mm solid #356854;
             padding-bottom:2.5mm; margin-bottom:5mm; }}
  .entete .g {{ flex:1; }}
  .entete .org {{ font-size:14pt; font-weight:bold; color:#1d3f5e; letter-spacing:.5px; }}
  .entete .devise {{ font-size:9.5pt; font-style:italic; color:#356854; }}
  .entete .refs {{ font-size:7.5pt; color:#666; }}
  .badge {{ background:#1d3f5e; color:#fff; font-size:8.5pt; padding:1.6mm 4mm; border-radius:1mm; white-space:nowrap; }}
  h1 {{ font-size:19pt; text-align:center; margin:0 0 1mm; color:#1d3f5e; letter-spacing:1px; }}
  .st {{ text-align:center; font-size:12pt; font-weight:bold; margin-bottom:1.5mm; }}
  .info {{ text-align:center; font-size:9pt; color:#555; border-top:.3mm solid #ccc;
           border-bottom:.3mm solid #ccc; padding:1.6mm 0; margin-bottom:4mm; }}
  .preambule {{ background:#EDF4F1; border-left:2mm solid #356854; padding:3mm 4mm; margin-bottom:4mm; font-size:10pt; }}
  h2 {{ font-size:11pt; color:#356854; margin:4mm 0 1.5mm; padding-bottom:.8mm; border-bottom:.3mm solid #cfe0d8; }}
  p {{ margin:0 0 1.8mm; text-align:justify; }}
  ul {{ margin:0 0 1.8mm; padding-left:6mm; }}
  li {{ margin-bottom:1mm; text-align:justify; }}
  .coupon {{ border:.8mm solid #1d3f5e; padding:4mm; margin-top:5mm; page-break-inside:avoid; }}
  .coupon h3 {{ margin:0 0 2mm; font-size:12pt; color:#1d3f5e; text-align:center; }}
  .champ {{ display:flex; gap:3mm; align-items:baseline; margin-bottom:3mm; font-size:10pt; }}
  .champ > span:first-child {{ flex:0 0 62mm; }}
  .ligne {{ flex:1; border-bottom:.3mm solid #333; height:4mm; }}
  .cases {{ margin:2mm 0 3mm; font-size:10pt; }}
  .case {{ display:inline-block; width:4mm; height:4mm; border:.4mm solid #333; margin:0 1.5mm 0 4mm;
           vertical-align:-.4mm; }}
  .sign {{ display:flex; gap:6mm; margin-top:3mm; }}
  .sign > div {{ flex:1; border:.3mm solid #999; padding:2.5mm; height:26mm; font-size:9pt; }}
  .fin {{ text-align:center; font-size:9pt; color:#356854; font-style:italic; margin-top:4mm; }}
</style></head><body>
{bandeau}

<h1>{titre}</h1>
<div class="st">{soustitre}</div>
<div class="info">{info}</div>
<div class="preambule">{preambule}</div>
{corps}

<div class="coupon">
  <h3>ENGAGEMENT — à retourner signé</h3>
  {champs}
  <div class="cases"><b>Droit à l'image :</b>
    <span class="case"></span>j'autorise <span class="case"></span>je n'autorise pas
    l'utilisation de photographies de mon enfant par Vision Plénitudes Vie.</div>
  <p style="font-size:10pt">Nous déclarons avoir lu le présent règlement intérieur, en avoir compris chaque
  article, et nous engageons à le respecter pendant toute la durée de la formation.</p>
  <div class="sign">
    <div><b>L'apprenant</b><br>Fait à ................. le ......../......../........<br><br>Signature :</div>
    <div><b>Le responsable légal</b><br>Fait à ................. le ......../......../........<br><br>Signature :</div>
    <div><b>Pour la formation</b><br>Nom : ...................................<br><br>Signature et cachet :</div>
  </div>
</div>
<div class="fin">Ensemble pour leur avenir !</div>
</body></html>""".format(
        bandeau=bandeau, titre=html.escape(TITRE), soustitre=html.escape(SOUS_TITRE), info=html.escape(LIGNE_INFO),
        preambule=gras(PREAMBULE).replace("\n", "<br>"), corps="\n".join(corps), champs=champs)


# =============================================================== version DOCX
def faire_docx(chemin):
    import docx
    from docx.shared import Pt, Cm, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement

    VERT = RGBColor(0x35, 0x68, 0x54); BLEU = RGBColor(0x1D, 0x3F, 0x5E); GRIS = RGBColor(0x66, 0x66, 0x66)
    d = docx.Document()
    st = d.styles["Normal"]; st.font.name = "Candara"; st.font.size = Pt(10.5)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Candara")
    pf = st.paragraph_format; pf.space_after = Pt(4); pf.line_spacing = 1.08

    for s in d.sections:
        s.top_margin = s.bottom_margin = Cm(1.4); s.left_margin = s.right_margin = Cm(1.6)

    def run(p, texte, taille=10.5, gras=False, ital=False, couleur=None):
        r = p.add_run(texte); r.font.name = "Candara"; r.font.size = Pt(taille)
        r.bold = gras; r.italic = ital
        if couleur is not None: r.font.color.rgb = couleur
        return r

    def bord_bas(p, couleur="356854", taille=12):
        pPr = p._p.get_or_add_pPr(); bdr = OxmlElement("w:pBdr"); b = OxmlElement("w:bottom")
        b.set(qn("w:val"), "single"); b.set(qn("w:sz"), str(taille))
        b.set(qn("w:space"), "2"); b.set(qn("w:color"), couleur)
        bdr.append(b); pPr.append(bdr)

    # --- l'en-tête, répété sur chaque page ---
    h = d.sections[0].header
    image = image_d_entete()
    if image is not None:
        p = h.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        largeur = d.sections[0].page_width - d.sections[0].left_margin - d.sections[0].right_margin
        p.add_run().add_picture(image, width=largeur)
        bord_bas(p)
    else:
        p = h.paragraphs[0]; run(p, "✝ " + ENTETE["org"], 14, True, couleur=BLEU)
        p2 = h.add_paragraph(); run(p2, ENTETE["devise"], 9.5, ital=True, couleur=VERT)
        p3 = h.add_paragraph(); run(p3, ENTETE["refs"], 7.5, couleur=GRIS)
        run(p3, "          " + ENTETE["badge"], 8.5, True, couleur=BLEU)
        bord_bas(p3)

    def para(texte, taille=10.5, gras=False, ital=False, couleur=None, align=None,
             avant=0, apres=4, puce=False, justif=True):
        p = d.add_paragraph(style="List Bullet" if puce else None)
        p.paragraph_format.space_before = Pt(avant); p.paragraph_format.space_after = Pt(apres)
        if align is not None: p.alignment = align
        elif justif and not puce: p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        for i, m in enumerate(texte.split("**")):
            if m: run(p, m, taille, gras or bool(i % 2), ital, couleur)
        return p

    para(TITRE, 19, True, couleur=BLEU, align=WD_ALIGN_PARAGRAPH.CENTER, avant=6, apres=1)
    para(SOUS_TITRE, 12, True, align=WD_ALIGN_PARAGRAPH.CENTER, apres=1)
    p = para(LIGNE_INFO, 9, couleur=GRIS, align=WD_ALIGN_PARAGRAPH.CENTER, apres=8); bord_bas(p, "CCCCCC", 6)
    for bloc in PREAMBULE.split("\n"):
        para(bloc, 10, ital=True, apres=3)

    for titre, blocs in ARTICLES:
        p = para(titre, 11, True, couleur=VERT, avant=10, apres=3, justif=False)
        bord_bas(p, "CFE0D8", 4)
        for b in blocs:
            if isinstance(b, tuple):
                for item in b[1]: para(item, puce=True, apres=2)
            else:
                para(b)

    # --- le coupon ---
    p = para("ENGAGEMENT — à retourner signé", 12, True, couleur=BLEU,
             align=WD_ALIGN_PARAGRAPH.CENTER, avant=14, apres=6)
    for nom, _ in ENGAGEMENT:
        para(nom + " :  " + "." * 60, apres=6)
    para("Droit à l'image :  ☐ j'autorise    ☐ je n'autorise pas   l'utilisation de photographies de mon "
         "enfant par Vision Plénitudes Vie.", apres=6)
    para("Nous déclarons avoir lu le présent règlement intérieur, en avoir compris chaque article, et nous "
         "engageons à le respecter pendant toute la durée de la formation.", apres=8)
    t = d.add_table(rows=1, cols=3); t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for cell, titre_c in zip(t.rows[0].cells, ("L'apprenant", "Le responsable légal", "Pour la formation")):
        cp = cell.paragraphs[0]; run(cp, titre_c, 10, True)
        cq = cell.add_paragraph(); run(cq, "Fait à ............... le ......../......../........", 9)
        cell.add_paragraph(); cr = cell.add_paragraph(); run(cr, "Signature :", 9)
        cell.add_paragraph()
    para("Ensemble pour leur avenir !", 10, ital=True, couleur=VERT,
         align=WD_ALIGN_PARAGRAPH.CENTER, avant=10)
    d.save(chemin)


def principal():
    if not os.path.isdir(os.path.join(DOSSIER, "sources")):
        os.makedirs(os.path.join(DOSSIER, "sources"))
    chemin_html = os.path.join(DOSSIER, "sources", "reglement-interieur.html")
    with open(chemin_html, "w", encoding="utf-8") as f:
        f.write(faire_html())
    print("  + %s" % os.path.relpath(chemin_html, RACINE))
    chemin_docx = os.path.join(DOSSIER, "reglement-interieur.docx")
    try:
        faire_docx(chemin_docx)
        print("  + %s" % os.path.relpath(chemin_docx, RACINE))
    except ImportError:
        print("  ! python-docx manquant : pip install python-docx")
        return 1
    print()
    print("  Le PDF se fabrique ensuite avec :  python 4-outils/faire_les_pdf.py --reglement")
    return 0


if __name__ == "__main__":
    sys.exit(principal())
