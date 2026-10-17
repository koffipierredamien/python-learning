# -*- coding: utf-8 -*-
"""Le programme des deux mois, pour le responsable : un seul document."""
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SORTIE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "3-suivi", "points-au-responsable")

MARINE = RGBColor(0x1A, 0x1A, 0x2E); VIOLET = RGBColor(0x6B, 0x2D, 0x8F)
GRIS = RGBColor(0x66, 0x66, 0x70); VERT = RGBColor(0x1D, 0x7A, 0x3E)

doc = Document()
st = doc.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(10.5)
for s in doc.sections:
    s.top_margin = s.bottom_margin = Cm(1.7); s.left_margin = s.right_margin = Cm(1.9)

def ombrer(cell, hexa):
    sh = OxmlElement("w:shd"); sh.set(qn("w:val"), "clear"); sh.set(qn("w:fill"), hexa)
    cell._tc.get_or_add_tcPr().append(sh)

def para(txt="", size=10.5, bold=False, color=None, after=6, italic=False, align=None):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    if align is not None: p.alignment = align
    r = p.add_run(txt); r.bold = bold; r.italic = italic; r.font.size = Pt(size)
    if color is not None: r.font.color.rgb = color
    return p

def riche(morceaux, size=10.5, after=6, puce=False):
    p = doc.add_paragraph(style="List Bullet" if puce else None)
    p.paragraph_format.space_after = Pt(after)
    for txt, gras in morceaux:
        r = p.add_run(txt); r.bold = gras; r.font.size = Pt(size)
    return p

def tableau(entetes, lignes, largeurs, taille=9):
    t = doc.add_table(rows=1 + len(lignes), cols=len(entetes))
    t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, e in enumerate(entetes):
        c = t.cell(0, i); c.text = ""
        r = c.paragraphs[0].add_run(e); r.bold = True; r.font.size = Pt(taille)
        ombrer(c, "EFEFF6")
    for li, ligne in enumerate(lignes, start=1):
        for ci, v in enumerate(ligne):
            c = t.cell(li, ci); c.text = ""
            r = c.paragraphs[0].add_run(v); r.font.size = Pt(taille)
            if ci == 0: r.bold = True
    for i, w in enumerate(largeurs):
        t.columns[i].width = Cm(w)
    return t

# --------------------------------------------------------------- en-tete
para("ACPROKIDS CODING CAMP · VISION PLÉNITUDES VIE", 8.5, True, VIOLET, after=2)
para("PROGRAMME DE FORMATION — CODAGE PYTHON POUR LES JEUNES", 9, True, GRIS, after=8)
para("Programme des mois d'octobre et de novembre 2026", 17, True, MARINE, after=4)
riche([("Sept séances, du samedi 17 octobre au samedi 28 novembre 2026", True),
       ("  ·  de 12 h à 14 h  ·  un enseignant par classe", False)], 9.5, after=2)
riche([("Classes : ", True),
       ("Jerusalem Geeks (9 – 12 ans) et Jeremiah Geeks (12 – 18 ans)", False)], 9.5, after=12)

para("Objet du présent document.", 10.5, True, MARINE, after=3)
para("Ce document présente, pour information et pour archive, l'intégralité du programme des deux "
     "mois à venir. Les sept séances sont préparées : chacune dispose de son déroulé détaillé, de "
     "ses documents à imprimer, de son support de projection et du travail donné aux familles. "
     "Aucune décision n'est attendue de la direction ; le document est transmis afin que le "
     "programme soit connu, et qu'il puisse être communiqué aux parents qui en feraient la demande.",
     after=12)

# --------------------------------------------------------------- 1
para("1. OÙ EN SONT LES APPRENANTS AU 17 OCTOBRE", 11.5, True, MARINE, after=5)
para("Cinq séances ont eu lieu depuis le 12 septembre. Les apprenants savent faire afficher un "
     "message par l'ordinateur, conserver une information dans une variable, poser une question au "
     "joueur, distinguer un texte d'un nombre, tenir un compteur, comparer deux valeurs et faire "
     "choisir le programme entre deux comportements. Ils savent également lire un message d'erreur, "
     "ce qui n'est pas la moindre des compétences.", after=4)
para("Leur projet commun — le jeu de morpion, appelé jeu XO — accueille les deux joueurs, affiche un "
     "plateau numéroté, demande à chacun la case qu'il veut jouer, refuse une case qui n'existe pas "
     "et compte les coups valides. Il lui manque une chose : la mémoire. C'est par là que commencent "
     "les deux mois qui viennent.", after=12)

# --------------------------------------------------------------- 2
para("2. LES SEPT SÉANCES", 11.5, True, MARINE, after=5)
tableau(["Date", "Séance", "Ce qui est enseigné", "Ce que le jeu sait faire à la fin"],
 [["17 oct", "Le plateau se souvient", "La liste, et le rang d'un élément",
   "Le symbole joué reste affiché"],
  ["24 oct", "On ne joue pas deux fois au même endroit", "La décision imbriquée",
   "Un coup sur une case prise est refusé"],
  ["31 oct", "Travaux pratiques n° 2", "Consolidation, deux heures en autonomie",
   "Quatre coups enchaînés sans anomalie"],
  ["7 nov", "Une seule question au lieu de trois", "Les opérateurs logiques",
   "La même décision, en deux fois moins de lignes"],
  ["14 nov", "Le jeu tourne tout seul", "La répétition",
   "Les neuf tours s'enchaînent, les joueurs alternent"],
  ["21 nov", "Le jeu sait qui gagne", "Les alignements gagnants, la fin de partie",
   "Une partie complète, avec un vainqueur"],
  ["28 nov", "Travaux pratiques n° 3 et tournoi", "Tests, finitions, tournoi de classe",
   "Le jeu est terminé et jouable"]],
 [1.9, 5.0, 4.6, 5.8])
para("", 6, after=8)
para("L'ordre n'est pas arbitraire. Chaque notion est introduite au moment où le projet en a besoin, "
     "et jamais avant : les apprenants rencontrent d'abord la difficulté, puis reçoivent l'outil qui "
     "la résout. Deux séances de travaux pratiques sont placées à dessein, la première après la "
     "notion la plus difficile des deux mois, la seconde à la fin, pour terminer et pour jouer.",
     after=12)

# --------------------------------------------------------------- 3
para("3. CE QUE LES APPRENANTS SAURONT FAIRE LE 28 NOVEMBRE", 11.5, True, MARINE, after=5)
for t in ("Employer une liste, c'est-à-dire conserver plusieurs valeurs dans une seule variable, et "
          "en désigner une par son rang.",
          "Écrire une décision, y compris une décision placée à l'intérieur d'une autre, et combiner "
          "plusieurs conditions en une seule.",
          "Écrire une répétition, reconnaître une répétition qui ne s'arrête pas, et l'interrompre.",
          "Éprouver leur propre programme au moyen d'une liste de situations à essayer, et réparer "
          "ce qui ne fonctionne pas.",
          "Lire un message d'erreur et en déduire où regarder."):
    riche([(t, False)], after=3, puce=True)
para("Chacun repartira avec un jeu de morpion complet, qu'il aura écrit lui-même et auquel ses "
     "camarades auront joué.", after=12)

# --------------------------------------------------------------- 4
para("4. LE TRAVAIL DONNÉ AUX FAMILLES", 11.5, True, MARINE, after=5)
para("Un travail est envoyé chaque mercredi, à l'exception de la semaine des travaux pratiques. "
     "Il est proposé sous deux formes équivalentes, afin qu'aucun enfant ne soit écarté faute "
     "d'équipement :", after=4)
riche([("pour les familles disposant d'un ordinateur", True),
       (" — un petit programme complet à écrire, environ une heure, avec une fiche d'instructions "
        "illustrée et son corrigé ; trois sont prévus sur les deux mois ;", False)], after=3, puce=True)
riche([("pour les autres", True),
       (" — un questionnaire de quinze questions, à faire depuis un téléphone en vingt minutes, "
        "corrigé automatiquement, qui porte sur le même contenu ; six sont prévus.", False)],
      after=3, puce=True)
para("Aucun de ces travaux n'entre dans une note. Ils servent à ce que la séance du samedi suivant "
     "puisse s'ouvrir, pour toute la classe, sur le même contenu. Les familles reçoivent avec chaque "
     "envoi un message les informant de ce qui est demandé et du temps à y consacrer.", after=12)

# --------------------------------------------------------------- 5
para("5. CE QUI EST DEMANDÉ À L'ÉCOLE", 11.5, True, MARINE, after=5)
tableau(["Quoi", "Quand", "Quantité"],
 [["Photocopies : une fiche d'aide-mémoire d'une page", "Chaque séance de cours (5 fois)",
   "8 par classe"],
  ["Photocopies : le document de travaux pratiques", "31 octobre (4 pages) et 28 novembre (2 pages)",
   "8 par classe"],
  ["Une grande feuille pour le tableau du tournoi", "28 novembre", "1"],
  ["Un appareil photographique", "28 novembre", "1"],
  ["Postes de travail en état, avec Thonny installé", "Chaque séance", "1 par élève"]],
 [8.4, 5.6, 3.3])
para("", 6, after=8)
para("Aucune dépense nouvelle n'est engagée. Le logiciel utilisé est gratuit et fonctionne sans "
     "connexion internet.", after=12)

# --------------------------------------------------------------- 6
para("6. SUIVI ET COMPTE RENDU", 11.5, True, MARINE, after=5)
para("La présence, la production de chaque élève et les travaux rendus continuent d'être consignés "
     "après chaque séance dans le classeur de suivi. Les enseignants remplissent en outre, le soir "
     "même, un journal de trois questions qui détermine l'ouverture de la séance suivante.", after=4)
para("Deux points d'étape écrits sont prévus pour la direction : le premier après la séance de "
     "travaux pratiques du 31 octobre, le second après le tournoi du 28 novembre. Ce dernier "
     "comportera le bilan des deux mois rempli par les élèves eux-mêmes, et les éléments qui "
     "détermineront le programme de décembre.", after=14)

para("Document établi le 17 octobre 2026 — AcProKids Coding Camp, Vision Plénitudes Vie.",
     9, False, GRIS, italic=True)

chemin = os.path.join(SORTIE, "programme-octobre-novembre.docx")
doc.save(chemin)
print("écrit :", chemin)
