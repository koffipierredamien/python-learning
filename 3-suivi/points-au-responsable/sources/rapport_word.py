# -*- coding: utf-8 -*-
"""Meme contenu, en Word, pour que le responsable puisse annoter ou transferer."""
import importlib.util, sys
spec = importlib.util.spec_from_file_location("rap", "/tmp/claude-0/-home-user-python-learning/731be2d5-98da-5705-b521-79ab616d2443/scratchpad/rapport.py")
rap = importlib.util.module_from_spec(spec); spec.loader.exec_module(rap)

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

MARINE = RGBColor(0x1A,0x1A,0x2E); VIOLET = RGBColor(0x6B,0x2D,0x8F)
VERT = RGBColor(0x1D,0x7A,0x3E); ROUGE = RGBColor(0xC0,0x39,0x2B)
ORANGE = RGBColor(0xC9,0x7A,0x00); GRIS = RGBColor(0x66,0x66,0x70)

doc = Document()
st = doc.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(10)
for s in doc.sections:
    s.top_margin = s.bottom_margin = Cm(1.6); s.left_margin = s.right_margin = Cm(1.6)

def para(txt="", size=10, bold=False, color=None, after=4, italic=False, align=None):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    if align is not None: p.alignment = align
    r = p.add_run(txt); r.bold = bold; r.italic = italic; r.font.size = Pt(size)
    if color is not None: r.font.color.rgb = color
    return p

def riche(morceaux, size=10, after=4, puce=False):
    p = doc.add_paragraph(style="List Bullet" if puce else None)
    p.paragraph_format.space_after = Pt(after)
    for txt, gras in morceaux:
        r = p.add_run(txt); r.bold = gras; r.font.size = Pt(size)
    return p

def ombrer(cell, hexa):
    sh = OxmlElement("w:shd"); sh.set(qn("w:val"), "clear"); sh.set(qn("w:fill"), hexa)
    cell._tc.get_or_add_tcPr().append(sh)

para("ACPROKIDS CODING CAMP · VISION PLÉNITUDES VIE", 8.5, True, VIOLET, after=2)
para("Point d'assiduité et de devoirs", 20, True, MARINE, after=2)
riche([("À l'attention du Pasteur Eli", True),
       ("  ·  situation arrêtée le ", False), ("vendredi 2 octobre 2026", True),
       (", veille de la séance 4  ·  période couverte : ", False),
       ("séances 1 à 3", True), (" (12, 19 et 26 septembre) et les ", False),
       ("3 devoirs", True), (" envoyés les mercredis", False)], 9.5, after=10)

chiffres = [("17", "élèves inscrits (9 Jerusalem · 8 Jeremiah)", MARINE),
            (str(rap.RET), "retards sur 3 séances", ORANGE),
            (str(rap.ABS), "absences non excusées", ROUGE),
            (str(rap.EXC), "absences excusées", GRIS),
            ("%d / 17" % rap.DEV[0], "devoir 1 rendu", MARINE),
            ("%d / 17" % rap.DEV[1], "devoir 2 rendu", MARINE),
            ("%d / 17" % rap.DEV[2], "devoir 3 rendu — échéance demain", ORANGE)]
t = doc.add_table(rows=2, cols=len(chiffres)); t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
for i, (k, l, c) in enumerate(chiffres):
    cel = t.cell(0, i); cel.text = ""
    r = cel.paragraphs[0].add_run(k); r.bold = True; r.font.size = Pt(15); r.font.color.rgb = c
    cel.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    cel2 = t.cell(1, i); cel2.text = ""
    r2 = cel2.paragraphs[0].add_run(l); r2.font.size = Pt(7.5); r2.font.color.rgb = GRIS
    cel2.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    ombrer(cel, "FAFAFF"); ombrer(cel2, "FAFAFF")
doc.add_paragraph().paragraph_format.space_after = Pt(6)

ETAT = {"P": "P", "R": "R", "E": "E", "A": "A"}

def tableau(titre, groupe, intitules, unites):
    para(titre, 11.5, True, MARINE, after=4)
    entetes = ["Élève", "S01 S02 S03", "Retards", "Absences",
               intitules[0], intitules[1], intitules[2], "Devoirs exigibles"]
    t = doc.add_table(rows=1, cols=len(entetes)); t.style = "Table Grid"
    for i, e in enumerate(entetes):
        c = t.rows[0].cells[i]; c.text = ""
        r = c.paragraphs[0].add_run(e); r.bold = True; r.font.size = Pt(7.5)
        r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        ombrer(c, "1A1A2E")
    for nom, pres, d1, d2, d3 in groupe:
        ret, absc, exc = rap.compte(pres)
        rendus = sum(1 for x in (d1, d2) if x[0] == "ok")
        ligne = t.add_row().cells
        def ecrire(cel, txt, gras=False, coul=None, taille=8, centre=True):
            cel.text = ""
            r = cel.paragraphs[0].add_run(txt); r.bold = gras; r.font.size = Pt(taille)
            if coul is not None: r.font.color.rgb = coul
            if centre: cel.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        ecrire(ligne[0], nom, True, None, 8.5, False)
        ecrire(ligne[1], "  ".join(ETAT[x] for x in pres))
        ecrire(ligne[2], str(ret) if ret else "—", bool(ret), ORANGE if ret else None)
        ecrire(ligne[3], str(absc) if absc else "—", bool(absc), ROUGE if absc else None)
        for j, (cell, unite) in enumerate(zip((d1, d2, d3), unites)):
            etat, note = cell
            if etat == "ok":
                ecrire(ligne[4+j], "rendu" + (("  " + note + unite) if note else ""), True, VERT, 7.5)
                ombrer(ligne[4+j], "F2FAF5")
            elif etat == "?":
                ecrire(ligne[4+j], "? à confirmer", False, ORANGE, 7.5); ombrer(ligne[4+j], "FFFAF0")
            elif j == 2:
                ecrire(ligne[4+j], "en attente", False, GRIS, 7.5); ombrer(ligne[4+j], "F7F7FB")
            else:
                ecrire(ligne[4+j], "NON RENDU", True, ROUGE, 7.5); ombrer(ligne[4+j], "FDF4F4")
        ecrire(ligne[7], "%d / 2" % rendus, True)
        if absc >= 2 or rendus == 0: ombrer(ligne[0], "FDF0F0")
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

tableau("JERUSALEM GEEKS — 9 à 12 ans · 9 élèves", rap.JERUSALEM,
        ["Devoir 1 quiz d'introduction", "Devoir 2 quiz de révision", "Devoir 3 (échéance demain)"],
        ["", "", ""])
tableau("JEREMIAH GEEKS — 12 à 18 ans · 8 élèves", rap.JEREMIAH,
        ["Devoir 1 quiz d'introduction", "Devoir 2 révision séance 2", "Devoir 3 (échéance demain)"],
        ["", "/12", "/12*"])

riche([("Présence : ", True), ("P présent · R en retard · E absence excusée · A absence non excusée.  ", False),
       ("« Devoirs exigibles »", True), (" compte les devoirs 1 et 2 : ", False),
       ("le devoir 3 n'est pas encore dû", True), (", son échéance est la séance de demain.", False)], 8, after=10)

riche([("Ce que ces chiffres disent en une phrase. ", True),
       ("L'assiduité n'est pas le problème : la ponctualité et les devoirs le sont. ", True),
       ("Sur 17 élèves, 11 ont rendu le devoir 2 et 8 le devoir 1. Les retards sont presque tous "
        "concentrés sur deux familles, et les absences non excusées sur une seule.", False)], 10, after=12)

doc.add_page_break()
para("LES SITUATIONS À REGARDER — par ordre d'urgence", 13, True, MARINE, after=8)

para("1 · Ce qui demande une action cette semaine", 11, True, VIOLET, after=4)
riche([("PRIORITÉ — Ethan SORO et Eunice SORO", True),
       (" — présents à la séance 1, puis ", False), ("absents aux séances 2 et 3", True),
       (", et aucun des devoirs rendu. Le règlement intérieur prévoit d'appeler la famille ", False),
       ("dès la deuxième absence", True),
       (" : l'appel reste à faire. C'est le seul cas de décrochage réel à ce jour.", False)], 10, puce=True)
riche([("À suivre — Joseph Daniel NGAPELA et Ephraïm AMON", True),
       (" — assidus (une absence excusée chacun), mais ", False),
       ("aucun devoir rendu sur les deux", True),
       (" exigibles. Ce n'est pas un problème de présence : les formulaires n'arrivent probablement pas "
        "jusqu'aux parents, ou le téléphone n'est pas disponible. Un appel suffira à le savoir.", False)], 10, puce=True)
riche([("À suivre — Caleb DOGBRE et Joshua DOGBRE", True),
       (" (même famille) — une absence excusée, un retard, puis ", False),
       ("une absence non excusée à la séance 3", True),
       (", et le devoir 2 non rendu pour les deux. À relier à l'appel ci-dessus.", False)], 10, puce=True, after=10)

para("2 · Un problème d'horaire, pas de motivation", 11, True, VIOLET, after=4)
riche([("Acquilas, Bénicia et Viesainte MBIERE", True), (" — ", False),
       ("en retard aux trois séances", True),
       (", soit 9 des %d retards à eux seuls. Mais " % rap.RET, False),
       ("ils ont rendu le devoir 2 et le devoir 3", True),
       (", tous les trois. Ces enfants travaillent : c'est l'arrivée à 12 h qui coince. Une question à "
        "poser à la famille (transport, trajet, horaire de départ) plutôt qu'un rappel à l'ordre.", False)], 10, puce=True)
riche([("Isaac YEDOH LOHOUESS", True),
       (" — deux retards, mais devoirs 2 et 3 rendus. Même lecture.", False)], 10, puce=True, after=10)

para("3 · Ce qui fonctionne, et qu'il faut dire aux familles", 11, True, VIOLET, after=4)
riche([("Lohiss LOUA, Yanis AMESSAN et Joyce Bouam LALLE", True), (" — assidus, et ", False),
       ("les trois devoirs rendus", True), (", avec les meilleures notes des deux classes. ", False),
       ("Sarah LOUA", True), (" et ", False), ("Gédéon OKITONGA", True), (" suivent de près.", False)], 10, puce=True)
riche([("Aucune absence non excusée chez 13 élèves sur 17", True),
       (", et la participation aux devoirs ", False), ("monte", True),
       (" : 8 au premier, 11 au deuxième.", False)], 10, puce=True, after=10)

para("4 · Discipline en classe", 11, True, VIOLET, after=4)
riche([("Un seul fait inscrit au registre depuis le début", True),
       (" : séance 3 du 26 septembre, ", False), ("Ephraïm AMON", True),
       (", déconcentration répétée pendant l'atelier, ", False), ("observation verbale", True),
       (". La famille n'a pas encore été informée. Aucun avertissement écrit n'a été prononcé.", False)], 10, puce=True, after=10)

para("5 · Ce que nous proposons de faire d'ici la séance 5", 11, True, VIOLET, after=4)
for m in ([("Appeler quatre familles", True),
           (" : SORO (deux absences), DOGBRE (absence + devoirs), NGAPELA et AMON (devoirs jamais rendus).", False)],
          [("Appeler la famille MBIERE", True), (" sur la seule question de l'heure d'arrivée.", False)],
          [("Rappeler le lien du devoir par message la veille de l'échéance", True),
           (" : les deux tiers des non-rendus sont des familles qui n'ont pas réagi au premier envoi.", False)],
          [("Féliciter nommément", True), (" les cinq élèves à jour, en début de séance 4.", False)]):
    riche(m, 10, puce=True)

doc.add_paragraph().paragraph_format.space_after = Pt(6)
para("Sources et précisions de lecture", 9.5, True, MARINE, after=3)
for m in ([("Présence, retards et discipline : classeur de suivi AcProKidsCodingCampSept2026, onglets "
            "Présence et Indiscipline. Devoirs : les réponses des quatre formulaires Google, plus le "
            "relevé du devoir 3 des Jerusalem Geeks transmis par l'enseignant.", False)],
          [("Devoir 3 non échu. ", True),
           ("Son échéance est la séance du 3 octobre : les « en attente » de cette colonne ne sont pas "
            "des manquements, ils indiquent seulement où nous en sommes ce soir.", False)],
          [("Une réponse non identifiée. ", True),
           ("Le devoir 1 comporte une réponse signée « David Dogbre », qui ne correspond à aucun nom "
            "inscrit. S'il s'agit de Joshua DOGBRE, son devoir 1 est rendu et le total passe de 8 à 9. "
            "À confirmer auprès de la famille : c'est la seule incertitude de ce document.", False)],
          [("Barèmes différents d'un devoir à l'autre. ", True),
           ("Le devoir 2 des Jeremiah Geeks est noté sur 12, les autres suivent le barème propre à leur "
            "formulaire. Les notes du devoir 3 sont partielles : seules les 12 questions à choix sont "
            "corrigées automatiquement, les 8 exercices où l'élève écrit du code restent à corriger à la "
            "main. Aucune note n'est donc définitive.", False)],
          [("Double envoi. ", True),
           ("Grâce-Elsa DREESEN a répondu deux fois au devoir 1 ; la meilleure note est retenue.", False)]):
    riche(m, 8.5, after=3)

para("Fait par les deux enseignants du Coding Camp, le 2 octobre 2026.", 9, False, GRIS, after=0)

sortie = "/home/user/python-learning/3-suivi/points-au-responsable/point-assiduite-et-devoirs.docx"
doc.save(sortie)
print("word ecrit :", sortie)
