# -*- coding: utf-8 -*-
"""Meme contenu, en Word, pour que le responsable puisse annoter ou transferer."""
import importlib.util, sys
spec = importlib.util.spec_from_file_location("rap", "/home/user/python-learning/3-suivi/points-au-responsable/sources/rapport.py")
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
riche([("2 octobre 2026", True), ("  ·  séances 1 à 3  ·  3 devoirs", False)], 9.5, after=10)

chiffres = [("17", "élèves inscrits (9 Jerusalem · 8 Jeremiah)", MARINE),
            (str(rap.RET), "retards à signaler", ORANGE),
            (str(rap.RETX), "retards excusés (école le samedi)", GRIS),
            (str(rap.ABS), "absences non excusées (%d autres, excusées)" % rap.EXC, ROUGE),
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

def tableau(titre, groupe, intitules):
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
        if not ret:
            ecrire(ligne[2], "—")
        elif nom in rap.RETARD_EXCUSE:
            ecrire(ligne[2], "%d exc." % ret, False, GRIS)
        else:
            ecrire(ligne[2], str(ret), True, ORANGE)
        ecrire(ligne[3], str(absc) if absc else "—", bool(absc), ROUGE if absc else None)
        for j, cell in enumerate((d1, d2, d3)):
            etat, note = cell
            if etat == "ok":
                ecrire(ligne[4+j], "rendu", True, VERT, 7.5)
                ombrer(ligne[4+j], "F2FAF5")
            elif j == 2:
                ecrire(ligne[4+j], "en attente", False, GRIS, 7.5); ombrer(ligne[4+j], "F7F7FB")
            else:
                ecrire(ligne[4+j], "NON RENDU", True, ROUGE, 7.5); ombrer(ligne[4+j], "FDF4F4")
        ecrire(ligne[7], "%d / 2" % rendus, True)
        if absc >= 2 or rendus == 0: ombrer(ligne[0], "FDF0F0")
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

tableau("JERUSALEM GEEKS — 9 à 12 ans · 9 élèves", rap.JERUSALEM,
        ["Devoir 1 quiz d'introduction", "Devoir 2 quiz de révision", "Devoir 3 (échéance demain)"])
tableau("JEREMIAH GEEKS — 12 à 18 ans · 8 élèves", rap.JEREMIAH,
        ["Devoir 1 quiz d'introduction", "Devoir 2 révision séance 2", "Devoir 3 (échéance demain)"])

riche([("Présence : ", True), ("P présent · R en retard · E absence excusée · A absence non excusée.  ", False),
       ("exc.", True), (" = retards excusés : ces élèves ont cours à leur école le samedi matin.  ", False),
       ("« Devoirs exigibles »", True), (" compte les devoirs 1 et 2 : ", False),
       ("le devoir 3 n'est pas encore dû", True), (", son échéance est la séance de demain.", False)], 8, after=10)

riche([("Ce que ces chiffres disent en une phrase. ", True),
       ("L'assiduité n'est pas le problème ; les devoirs le sont, et pour quelques familles seulement. ", True),
       ("Sur 17 élèves, 11 ont rendu le devoir 2 et 9 le devoir 1. Les %d retards excusés viennent tous "
        "de l'école du samedi matin et ne dépendent pas des enfants. Les absences non excusées sont "
        "concentrées sur deux familles." % rap.RETX, False)], 10, after=12)

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

para("2 · Des retards qui ne dépendent pas des enfants", 11, True, VIOLET, after=4)
riche([("Acquilas, Bénicia et Viesainte MBIERE et Isaac YEDOH LOHOUESS", True),
       (" — %d des %d retards relevés sont les leurs, et ils s'expliquent par une seule raison : " % (rap.RETX, rap.RET + rap.RETX), False),
       ("ces élèves ont cours à leur école le samedi matin", True),
       (" et ne peuvent pas être là à 12 h. ", False),
       ("Ces retards sont excusés", True), (", et inscrits comme tels dans le classeur de suivi.", False)], 10, puce=True)
riche([("Et ils travaillent : ", False), ("tous les quatre ont rendu le devoir 2 et le devoir 3", True),
       (". Ce n'est donc ni un problème de motivation, ni un problème de famille — il n'y a rien à leur demander.", False)], 10, puce=True)
riche([("Ce qu'on peut faire de notre côté : la séance ", False), ("commence par la prière", True),
       (", et la leçon ne démarre qu'à 12 h 20. ", False), ("L'essentiel leur est préservé", True),
       (" — c'est la raison de cet ordre.", False)], 10, puce=True, after=10)

para("3 · Ce qui fonctionne, et qu'il faut dire aux familles", 11, True, VIOLET, after=4)
riche([("Lohiss LOUA, Yanis AMESSAN et Joyce Bouam LALLE", True), (" — assidus, et ", False),
       ("les trois devoirs rendus", True), (", avec les meilleures notes des deux classes. ", False),
       ("Sarah LOUA", True), (" et ", False), ("Gédéon OKITONGA", True), (" suivent de près.", False)], 10, puce=True)
riche([("Aucune absence non excusée chez 13 élèves sur 17", True),
       (", et la participation aux devoirs ", False), ("monte", True),
       (" : 9 au premier, 11 au deuxième.", False)], 10, puce=True, after=10)

para("4 · Discipline en classe", 11, True, VIOLET, after=4)
riche([("Un seul fait inscrit au registre depuis le début", True),
       (" : séance 3 du 26 septembre, ", False), ("Ephraïm AMON", True),
       (", déconcentration répétée pendant l'atelier, ", False), ("observation verbale", True),
       (". La famille n'a pas encore été informée. Aucun avertissement écrit n'a été prononcé.", False)], 10, puce=True, after=10)

para("5 · Ce que nous proposons de faire d'ici la séance 5", 11, True, VIOLET, after=4)
for m in ([("Appeler quatre familles", True),
           (" : SORO (deux absences), DOGBRE (absence + devoirs), NGAPELA et AMON (devoirs jamais rendus).", False)],
          [("Ne pas relancer les quatre élèves en retard excusé", True),
           (", et le dire au reste de la classe : arriver à 12 h 20 après l'école n'est pas un manque de sérieux.", False)],
          [("Rappeler le lien du devoir par message la veille de l'échéance", True),
           (" : les deux tiers des non-rendus sont des familles qui n'ont pas réagi au premier envoi.", False)],
          [("Féliciter nommément", True), (" les élèves à jour, en début de séance 4.", False)]):
    riche(m, 10, puce=True)

doc.add_paragraph().paragraph_format.space_after = Pt(6)
sortie = "/home/user/python-learning/3-suivi/points-au-responsable/point-assiduite-et-devoirs.docx"
doc.save(sortie)
print("word ecrit :", sortie)
