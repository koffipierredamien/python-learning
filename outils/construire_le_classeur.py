# -*- coding: utf-8 -*-
"""
Construit suivi/classeur-de-suivi.xlsx a partir de zero.
A relancer seulement si vous voulez changer la structure du classeur
(ajouter une colonne, un onglet, une valeur de menu deroulant).
ATTENTION : cela ECRASE le fichier et donc les donnees deja saisies.
Pour un usage normal, travaillez directement dans Google Sheets.
   Utilisation :  python outils/construire_le_classeur.py
   Necessite :    pip install openpyxl
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.utils import get_column_letter

N = 30                      # nombre de lignes eleves
L0, L1 = 2, 2 + N - 1       # premiere / derniere ligne eleve
SEANCES = ["S%02d" % i for i in range(1, 23)]

MARINE = "1A1A2E"; VIOLET = "6B2D8F"; GRIS = "EFEFF4"; JAUNE = "FFF6D8"
VERT = "EAF7EE"; ROUGE = "FDECEC"; ORANGE = "FFF0DF"; BLEU = "E8F1FC"

F = "Arial"
h1   = Font(name=F, size=14, bold=True, color="FFFFFF")
hcol = Font(name=F, size=9,  bold=True, color="FFFFFF")
base = Font(name=F, size=10)
gras = Font(name=F, size=10, bold=True)
petit= Font(name=F, size=8.5, color="555555")
calc = Font(name=F, size=10, color="0B6B2E")      # vert = calcule automatiquement
ex   = Font(name=F, size=10, italic=True, color="888888")

fond_titre = PatternFill("solid", fgColor=MARINE)
fond_col   = PatternFill("solid", fgColor=VIOLET)
fond_gris  = PatternFill("solid", fgColor=GRIS)
fond_jaune = PatternFill("solid", fgColor=JAUNE)
fond_vert  = PatternFill("solid", fgColor=VERT)
fond_bleu  = PatternFill("solid", fgColor=BLEU)
bord = Border(*[Side(style="thin", color="BFBFBF")] * 4)
centre = Alignment(horizontal="center", vertical="center")
retour = Alignment(wrap_text=True, vertical="top")

wb = openpyxl.Workbook()
wb.remove(wb.active)


def feuille(nom, titre, sous_titre, colonnes, largeurs, gel="A4"):
    ws = wb.create_sheet(nom)
    ws.sheet_view.showGridLines = False
    ws["A1"] = titre; ws["A1"].font = h1; ws["A1"].fill = fond_titre
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=max(len(colonnes), 4))
    ws.row_dimensions[1].height = 24
    ws["A2"] = sous_titre; ws["A2"].font = petit
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=max(len(colonnes), 4))
    for i, (col, larg) in enumerate(zip(colonnes, largeurs), start=1):
        c = ws.cell(row=3, column=i, value=col)
        c.font = hcol; c.fill = fond_col; c.alignment = Alignment(wrap_text=True, horizontal="center", vertical="center")
        c.border = bord
        ws.column_dimensions[get_column_letter(i)].width = larg
    ws.row_dimensions[3].height = 30
    ws.freeze_panes = gel
    return ws


def quadriller(ws, l1, l2, c1, c2, police=None):
    for r in range(l1, l2 + 1):
        for c in range(c1, c2 + 1):
            cell = ws.cell(row=r, column=c)
            cell.border = bord
            if cell.font is None or cell.font.name != F:
                cell.font = police or base


def liste(ws, formule, plage):
    dv = DataValidation(type="list", formula1=formule, allow_blank=True)
    dv.error = "Choisissez une valeur dans la liste."
    dv.errorTitle = "Valeur non prevue"
    ws.add_data_validation(dv); dv.add(plage)


def nom_eleve(col_source, ligne):
    return "=IF('01_Apprenants'!%s%d=\"\",\"\",'01_Apprenants'!%s%d)" % (col_source, ligne, col_source, ligne)


# =====================================================================  13_Listes
listes = {
    "A": ("Classe", ["Jerusalem Geeks", "Jeremiah Geeks"]),
    "B": ("Profil", ["P0 Decouvreur", "P1 Initie", "P2 Autonome", "P3 Avance"]),
    "C": ("Presence", ["P present", "R retard", "E excuse", "A absent"]),
    "D": ("Production", ["V-Bleue", "V-Rouge", "V-Noire", "Partielle", "Rien"]),
    "E": ("Oui/Non", ["Oui", "Non"]),
    "F": ("Attitude", ["abandonne", "demande", "persevere", "aide les autres"]),
    "G": ("Grade", ["Novice", "Apprenti Codeur", "Codeur", "Ingenieur", "Architecte", "Maitre Geek"]),
    "H": ("Type d'observation", ["Reussite", "Difficulte", "Comportement", "Famille", "Sante", "Materiel", "Autre"]),
    "I": ("Statut eleve", ["Actif", "En pause", "Parti"]),
    "J": ("Quand", ["J-7", "J-1", "Jour J", "Pendant", "Apres"]),
    "K": ("Fait ?", ["A faire", "En cours", "Fait"]),
    "L": ("Lien de parente", ["Mere", "Pere", "Tuteur/Tutrice", "Grand-parent", "Frere/Soeur", "Autre"]),
    "M": ("Ordi maison", ["Oui a moi", "Oui partage", "Non"]),
    "N": ("Internet maison", ["Oui", "Parfois", "Non"]),
    "O": ("Deja code", ["Jamais", "Scratch", "Python", "Autre"]),
    "P": ("Niveau anglais", ["Non", "Un peu", "Oui"]),
    "Q": ("Coche", ["V", ""]),
}
ws = feuille("13_Listes", "LISTES DE CHOIX",
             "Ces colonnes alimentent les menus deroulants des autres onglets. Vous pouvez ajouter des valeurs a la suite : elles apparaitront automatiquement.",
             [v[0] for v in listes.values()], [18] * len(listes), gel="A4")
for col, (_, valeurs) in listes.items():
    for i, v in enumerate(valeurs, start=4):
        c = ws[col + str(i)]; c.value = v; c.font = base; c.border = bord
quadriller(ws, 4, 20, 1, len(listes))

def plage_liste(col, n):
    return "'13_Listes'!$%s$4:$%s$%d" % (col, col, 3 + n)

P_CLASSE   = plage_liste("A", 2)
P_PROFIL   = plage_liste("B", 4)
P_PRESENCE = plage_liste("C", 4)
P_PROD     = plage_liste("D", 5)
P_OUINON   = plage_liste("E", 2)
P_ATTITUDE = plage_liste("F", 4)
P_GRADE    = plage_liste("G", 6)
P_TYPEOBS  = plage_liste("H", 7)
P_STATUT   = plage_liste("I", 3)
P_QUAND    = plage_liste("J", 5)
P_FAIT     = plage_liste("K", 3)
P_LIEN     = plage_liste("L", 6)
P_ORDI     = plage_liste("M", 3)
P_NET      = plage_liste("N", 3)
P_CODE     = plage_liste("O", 4)
P_ANGLAIS  = plage_liste("P", 3)

# =====================================================================  00_Mode d'emploi
ws = wb.create_sheet("00_Mode-emploi", 0)
ws.sheet_view.showGridLines = False
ws.column_dimensions["A"].width = 26; ws.column_dimensions["B"].width = 96
ws["A1"] = "CLASSEUR DE SUIVI  -  JERUSALEM GEEKS & JEREMIAH GEEKS"
ws["A1"].font = h1; ws["A1"].fill = fond_titre; ws.merge_cells("A1:B1"); ws.row_dimensions[1].height = 26
lignes = [
    ("", ""),
    ("A QUOI SERT CE CLASSEUR", "Il rassemble tout ce que les deux enseignants doivent savoir et noter : qui sont les eleves, "
     "comment les joindre, qui etait la, qui progresse, qui decroche, et ce qui reste a preparer."),
    ("COMMENT L'OUVRIR DANS GOOGLE SHEETS", "Google Drive > Nouveau > Importation de fichier > choisir ce fichier .xlsx. "
     "Puis Fichier > Enregistrer au format Google Sheets. Les menus deroulants et les calculs sont conserves."),
    ("QUI PEUT LE VOIR", "Partagez-le uniquement avec les deux enseignants (Partager > acces restreint). "
     "Il contient les coordonnees de mineurs : il ne doit jamais etre publie ni partage par lien public."),
    ("", ""),
    ("LES COULEURS", ""),
    ("   Fond jaune", "Cellules a remplir a la main."),
    ("   Texte vert", "Cellules calculees automatiquement : n'ecrivez pas dedans, vous casseriez le calcul."),
    ("   Texte gris italique", "Ligne d'exemple. Ecrivez par-dessus avec votre premier eleve."),
    ("", ""),
    ("LA REGLE D'OR", "On ne saisit les noms QU'UNE SEULE FOIS, dans l'onglet 01_Apprenants. "
     "Tous les autres onglets les recopient tout seuls. Si un nom est vide ailleurs, c'est qu'il manque dans 01."),
    ("", ""),
    ("LES ONGLETS", ""),
    ("   01_Apprenants", "La fiche complete de chaque eleve et les contacts des responsables. LE POINT DE DEPART."),
    ("   02_Diagnostic", "Les resultats du Test de Decollage et le profil P0 a P3. Interne aux enseignants : jamais communique."),
    ("   03_Presence", "La feuille de presence des 22 seances, avec le taux calcule."),
    ("   04_Suivi-seances", "Ce que chaque eleve a produit a chaque seance, et sur quelle piste. La colonne ALERTE se declenche toute seule."),
    ("   05_Observations", "Le journal : une ligne par fait marquant, avec l'action decidee et si elle a ete faite."),
    ("   06_Binomes", "Qui travaille avec qui, a quel poste, seance par seance."),
    ("   07_Badges-Grades", "Les badges distribues et le grade atteint."),
    ("   08_Passeport", "Les 12 gestes machine, valides oralement. Remplace le livret papier."),
    ("   09_Checklist-S01", "Tout ce qu'il reste a preparer avant la seance 1, avec un responsable et une date."),
    ("   10_Journal-enseignants", "La revue de 15 minutes apres chaque seance : 3 questions, et ce qu'on decide."),
    ("   11_Materiel", "L'inventaire : ce qui est imprime, achete, installe."),
    ("   12_Tableau-de-bord", "Les indicateurs calcules automatiquement. A regarder une fois par mois."),
    ("   13_Listes", "Les valeurs des menus deroulants. Modifiable si besoin."),
    ("", ""),
    ("LE DECLENCHEUR A SURVEILLER", "Dans 04_Suivi-seances, la colonne ALERTE passe a OUI des qu'un eleve cumule deux seances de suite "
     "sans production. Cet eleve entre sur la LISTE DES 10 MINUTES : le Mecanicien lui consacre 10 minutes en tete-a-tete "
     "a la seance suivante. C'est un rendez-vous, pas une punition -- et c'est ce qui empeche un decrochage silencieux "
     "de devenir un abandon."),
]
r = 2
for a, b in lignes:
    ws.cell(row=r, column=1, value=a).font = gras if a and not a.startswith("   ") else base
    c = ws.cell(row=r, column=2, value=b); c.font = base; c.alignment = retour
    if a.startswith("   "):
        ws.cell(row=r, column=1).font = Font(name=F, size=10, bold=True, color=VIOLET)
    ws.row_dimensions[r].height = 28 if len(b) > 95 else (42 if len(b) > 190 else 15)
    r += 1

# =====================================================================  01_Apprenants
cols = ["N°", "NOM", "Prenom", "Classe", "Date de naissance", "Age", "Ecole", "Niveau scolaire",
        "Tel. eleve", "Email eleve", "RESPONSABLE 1 - Nom", "Lien", "Telephone 1", "WhatsApp ?", "Email 1",
        "RESPONSABLE 2 - Nom", "Lien", "Telephone 2", "Quartier / Adresse", "Contact d'urgence (nom + tel)",
        "Sante / allergies a connaitre", "Autorisation photo", "Ordinateur a la maison", "Internet a la maison",
        "Comment vient-il ?", "Date d'inscription", "Statut", "Remarques"]
larg = [5, 16, 14, 16, 15, 7, 16, 13, 14, 20, 20, 12, 14, 10, 20, 20, 12, 14, 22, 24, 22, 12, 16, 14, 16, 14, 11, 30]
ws = feuille("01_Apprenants", "FICHE DES APPRENANTS",
             "On saisit les noms ICI et nulle part ailleurs : les autres onglets les recopient automatiquement. Ecrivez par-dessus la ligne d'exemple.",
             cols, larg, gel="D4")
for r in range(L0 + 2, L1 + 3):
    i = r - 3
    ws.cell(row=r, column=1, value=i).font = base
    ws.cell(row=r, column=6, value='=IF(E%d="","",DATEDIF(E%d,TODAY(),"Y"))' % (r, r)).font = calc
    for c in (5, 26):
        ws.cell(row=r, column=c).number_format = "DD/MM/YYYY"
quadriller(ws, 4, L1 + 2, 1, len(cols))
for c in (2, 3, 4, 5, 11, 13, 16, 18, 20, 22, 23, 24):
    for r in range(4, L1 + 3):
        ws.cell(row=r, column=c).fill = fond_jaune
exemple = [1, "KOUASSI", "Awa", "Jerusalem Geeks", "12/03/2015", None, "EPP Riviera", "CM2",
           "", "", "KOUASSI Marie", "Mere", "07 00 00 00 00", "Oui", "marie.k@exemple.com",
           "KOUASSI Jean", "Pere", "05 00 00 00 00", "Riviera 2, rue des Jardins", "KOUASSI Marie - 07 00 00 00 00",
           "Asthme leger - inhalateur dans le sac", "Oui", "Oui partage", "Parfois", "A pied avec sa soeur",
           "05/09/2026", "Actif", "Tres timide, ne demande jamais d'aide"]
for i, v in enumerate(exemple, start=1):
    c = ws.cell(row=4, column=i); c.value = v; c.font = ex
ws["F4"] = '=IF(E4="","",DATEDIF(E4,TODAY(),"Y"))'; ws["F4"].font = calc
liste(ws, P_CLASSE, "D4:D%d" % (L1 + 2)); liste(ws, P_LIEN, "L4:L%d" % (L1 + 2))
liste(ws, P_LIEN, "Q4:Q%d" % (L1 + 2)); liste(ws, P_OUINON, "N4:N%d" % (L1 + 2))
liste(ws, P_OUINON, "V4:V%d" % (L1 + 2)); liste(ws, P_ORDI, "W4:W%d" % (L1 + 2))
liste(ws, P_NET, "X4:X%d" % (L1 + 2)); liste(ws, P_STATUT, "AA4:AA%d" % (L1 + 2))

DERNIERE = L1 + 2   # derniere ligne eleve dans tous les onglets (ligne 4 = premier eleve)

def colonnes_identite(ws):
    for r in range(4, DERNIERE + 1):
        ws.cell(row=r, column=1, value=r - 3).font = base
        ws.cell(row=r, column=2, value=nom_eleve("B", r)).font = calc
        ws.cell(row=r, column=3, value=nom_eleve("C", r)).font = calc
        ws.cell(row=r, column=4, value=nom_eleve("D", r)).font = calc

# =====================================================================  02_Diagnostic
cols = ["N°", "NOM", "Prenom", "Classe", "Pilotage /6", "Logique /4", "Deja code ?", "Anglais",
        "Frappe clavier", "Face a la difficulte", "PROFIL", "Piste conseillee", "Remarques (ecrire tout de suite)",
        "Reevaluation S5", "Reevaluation S12"]
larg = [5, 16, 14, 16, 11, 10, 13, 10, 12, 18, 16, 14, 40, 14, 14]
ws = feuille("02_Diagnostic", "TEST DE DECOLLAGE  -  DIAGNOSTIC (SEANCE 1)",
             "INTERNE AUX ENSEIGNANTS. Ces resultats ne sont communiques ni aux eleves ni aux familles. La colonne la plus importante est 'Face a la difficulte'.",
             cols, larg, gel="E4")
colonnes_identite(ws)
quadriller(ws, 4, DERNIERE, 1, len(cols))
for r in range(4, DERNIERE + 1):
    for c in range(5, 16):
        ws.cell(row=r, column=c).fill = fond_jaune
    ws.cell(row=r, column=12,
            value='=IF(K%d="","",IF(LEFT(K%d,2)="P0","Bleue",IF(LEFT(K%d,2)="P3","Noire","Rouge")))' % (r, r, r)).font = calc
    ws.cell(row=r, column=12).fill = PatternFill("solid", fgColor="FFFFFF")
liste(ws, P_PROFIL, "K4:K%d" % DERNIERE); liste(ws, P_ATTITUDE, "J4:J%d" % DERNIERE)
liste(ws, P_CODE, "G4:G%d" % DERNIERE); liste(ws, P_ANGLAIS, "H4:H%d" % DERNIERE)
liste(ws, P_ANGLAIS, "I4:I%d" % DERNIERE); liste(ws, P_PROFIL, "N4:N%d" % DERNIERE)
liste(ws, P_PROFIL, "O4:O%d" % DERNIERE)
ws.conditional_formatting.add("K4:K%d" % DERNIERE,
    FormulaRule(formula=['LEFT($K4,2)="P0"'], fill=PatternFill("solid", fgColor=ROUGE)))
ws.conditional_formatting.add("K4:K%d" % DERNIERE,
    FormulaRule(formula=['LEFT($K4,2)="P3"'], fill=PatternFill("solid", fgColor=BLEU)))

# =====================================================================  03_Presence
cols = ["N°", "NOM", "Prenom", "Classe"] + SEANCES + ["Presences", "Absences", "Taux"]
larg = [5, 16, 14, 16] + [6] * 22 + [11, 11, 9]
ws = feuille("03_Presence", "FEUILLE DE PRESENCE",
             "P = present   R = retard   E = excuse   A = absent.  Le total et le taux se calculent tout seuls. Une absence est le premier facteur d'abandon : appelez la famille des la 2e.",
             cols, larg, gel="E4")
colonnes_identite(ws)
quadriller(ws, 4, DERNIERE, 1, len(cols))
deb, fin = get_column_letter(5), get_column_letter(4 + 22)
for r in range(4, DERNIERE + 1):
    for c in range(5, 27):
        ws.cell(row=r, column=c).fill = fond_jaune
        ws.cell(row=r, column=c).alignment = centre
    vide = '\'01_Apprenants\'!B%d=""' % r
    ws.cell(row=r, column=27, value='=IF(%s,"",COUNTIF(%s%d:%s%d,"P*")+COUNTIF(%s%d:%s%d,"R*"))' % (vide, deb, r, fin, r, deb, r, fin, r)).font = calc
    ws.cell(row=r, column=28, value='=IF(%s,"",COUNTIF(%s%d:%s%d,"A*"))' % (vide, deb, r, fin, r)).font = calc
    ws.cell(row=r, column=29, value='=IF(COUNTA(%s%d:%s%d)=0,"",AA%d/COUNTA(%s%d:%s%d))' % (deb, r, fin, r, r, deb, r, fin, r)).font = calc
    ws.cell(row=r, column=29).number_format = "0%"
liste(ws, P_PRESENCE, "E4:%s%d" % (fin, DERNIERE))
ws.conditional_formatting.add("AC4:AC%d" % DERNIERE,
    CellIsRule(operator="lessThan", formula=["0.85"], fill=PatternFill("solid", fgColor=ROUGE), font=Font(name=F, bold=True, color="A11111")))

# =====================================================================  04_Suivi-seances
cols = ["N°", "NOM", "Prenom", "Classe"] + SEANCES + ["Briques", "Partielles", "Manquees", "ALERTE 10 min"]
larg = [5, 16, 14, 16] + [8] * 22 + [10, 10, 10, 14]
ws = feuille("04_Suivi-seances", "SUIVI DES SEANCES  -  QUI A PRODUIT SA BRIQUE ?",
             "V-Bleue / V-Rouge / V-Noire = brique produite, et sur quelle piste.  Partielle = commencee mais pas finie.  Rien = rien produit. La colonne ALERTE passe a OUI apres deux seances de suite sans production.",
             cols, larg, gel="E4")
colonnes_identite(ws)
quadriller(ws, 4, DERNIERE, 1, len(cols))
for r in range(4, DERNIERE + 1):
    for c in range(5, 27):
        ws.cell(row=r, column=c).fill = fond_jaune
        ws.cell(row=r, column=c).alignment = centre
    vide = '\'01_Apprenants\'!B%d=""' % r
    ws.cell(row=r, column=27, value='=IF(%s,"",COUNTIF(%s%d:%s%d,"V*"))' % (vide, deb, r, fin, r)).font = calc
    ws.cell(row=r, column=28, value='=IF(%s,"",COUNTIF(%s%d:%s%d,"Partielle"))' % (vide, deb, r, fin, r)).font = calc
    ws.cell(row=r, column=29, value='=IF(%s,"",COUNTIF(%s%d:%s%d,"Rien"))' % (vide, deb, r, fin, r)).font = calc
    ws.cell(row=r, column=30, value=(
        '=IF(SUMPRODUCT(((E%d:Y%d="Partielle")+(E%d:Y%d="Rien"))*'
        '((F%d:Z%d="Partielle")+(F%d:Z%d="Rien")))>0,"OUI","")' % (r, r, r, r, r, r, r, r))).font = calc
liste(ws, P_PROD, "E4:%s%d" % (fin, DERNIERE))
ws.conditional_formatting.add("AD4:AD%d" % DERNIERE,
    CellIsRule(operator="equal", formula=['"OUI"'], fill=PatternFill("solid", fgColor="FFC7C7"),
               font=Font(name=F, bold=True, color="A11111")))

# =====================================================================  05_Observations
cols = ["Date", "Seance", "Eleve", "Type", "Ce que j'ai observe", "Action decidee", "Qui s'en occupe", "Pour quand", "Fait ?"]
larg = [12, 9, 20, 15, 46, 40, 15, 12, 11]
ws = feuille("05_Observations", "JOURNAL DES OBSERVATIONS",
             "Une ligne par fait marquant. Ecrivez le soir meme : on oublie tres vite. Une observation sans action decidee ne sert a rien.",
             cols, larg, gel="A4")
quadriller(ws, 4, 120, 1, len(cols))
for r in range(4, 121):
    ws.cell(row=r, column=1).number_format = "DD/MM/YYYY"
    for c in range(1, 10):
        ws.cell(row=r, column=c).fill = fond_jaune
        ws.cell(row=r, column=c).alignment = retour
for i, v in enumerate(["05/09/2026", "S01", "KOUASSI Awa", "Difficulte",
                       "N'a pas ose lever la carte orange de toute la seance. Bloquee 10 min sur un guillemet.",
                       "Rappeler a toute la classe que la carte sert justement a ne pas avoir a parler. La placer avec un binome patient.",
                       "Mecanicien", "12/09/2026", "A faire"], start=1):
    ws.cell(row=4, column=i).value = v; ws.cell(row=4, column=i).font = ex
liste(ws, P_TYPEOBS, "D4:D120"); liste(ws, P_FAIT, "I4:I120")
ws.conditional_formatting.add("I4:I120",
    CellIsRule(operator="equal", formula=['"Fait"'], fill=PatternFill("solid", fgColor=VERT)))

# =====================================================================  06_Binomes
cols = ["Seance", "Poste n°", "Eleve A (pilote en 1er)", "Profil A", "Eleve B (copilote)", "Profil B",
        "3e eleve (trinome)", "Ca s'est bien passe ?", "Remarques"]
larg = [9, 10, 24, 14, 24, 14, 22, 18, 36]
ws = feuille("06_Binomes", "COMPOSITION DES BINOMES",
             "Regle : un ecart d'UN niveau maximum. Jamais un P0 avec un P3 -- sinon le P3 fait tout et le P0 regarde. Rotation des binomes toutes les 3 seances.",
             cols, larg, gel="A4")
quadriller(ws, 4, 80, 1, len(cols))
for r in range(4, 81):
    for c in range(1, 10):
        ws.cell(row=r, column=c).fill = fond_jaune
        ws.cell(row=r, column=c).alignment = retour
for i in range(12):
    ws.cell(row=4 + i, column=1, value="S01").font = base
    ws.cell(row=4 + i, column=2, value=i + 1).font = base
for i, v in enumerate(["S01", 1, "KOUASSI Awa", "P0 Decouvreur", "DIALLO Ibrahim", "P1 Initie", "", "", "Awa n'ose pas taper : rappeler la rotation"], start=1):
    ws.cell(row=4, column=i).value = v; ws.cell(row=4, column=i).font = ex
liste(ws, P_PROFIL, "D4:D80"); liste(ws, P_PROFIL, "F4:F80"); liste(ws, P_OUINON, "H4:H80")

# =====================================================================  07_Badges-Grades
badges = ["Batisseur", "Bon copilote", "Chasseur de bug", "Sauveteur", "Traducteur d'erreur", "Perseverant",
          "Question en or", "Zero indentation", "Testeur impitoyable", "Beau design", "Explorateur",
          "Piste Noire", "Presentateur"]
cols = ["N°", "NOM", "Prenom", "Classe"] + badges + ["TOTAL", "GRADE ACTUEL", "Date du grade"]
larg = [5, 16, 14, 16] + [11] * len(badges) + [9, 18, 13]
ws = feuille("07_Badges-Grades", "BADGES ET GRADES",
             "On note le NOMBRE de fois ou le badge a ete donne. Objectif : chaque eleve repart avec au moins un badge par seance. Le badge 'Perseverant' est le plus important du dispositif.",
             cols, larg, gel="E4")
colonnes_identite(ws)
quadriller(ws, 4, DERNIERE, 1, len(cols))
c_deb, c_fin = 5, 4 + len(badges)
for r in range(4, DERNIERE + 1):
    for c in range(c_deb, c_fin + 1):
        ws.cell(row=r, column=c).fill = fond_jaune
        ws.cell(row=r, column=c).alignment = centre
    ws.cell(row=r, column=c_fin + 1,
            value='=IF(\'01_Apprenants\'!B%d="","",SUM(%s%d:%s%d))'
                  % (r, get_column_letter(c_deb), r, get_column_letter(c_fin), r)).font = calc
    ws.cell(row=r, column=c_fin + 2).fill = fond_jaune
    ws.cell(row=r, column=c_fin + 3).fill = fond_jaune
    ws.cell(row=r, column=c_fin + 3).number_format = "DD/MM/YYYY"
liste(ws, P_GRADE, "%s4:%s%d" % (get_column_letter(c_fin + 2), get_column_letter(c_fin + 2), DERNIERE))

# =====================================================================  08_Passeport
gestes = ["1 Allumer / eteindre", "2 Souris : clic, double-clic, clic droit, glisser", "3 Majuscule, accent, point, virgule",
          "4 Touches speciales ( ) : _ #", "5 Ouvrir / reduire / fermer une fenetre", "6 Passer d'une fenetre a l'autre",
          "7 Creer un dossier et le nommer", "8 Enregistrer au bon endroit", "9 Retrouver un fichier enregistre",
          "10 Ouvrir Thonny et lancer un programme", "11 Copier le projet depuis le dossier officiel",
          "12 Taper 20 mots sans regarder ses doigts"]
cols = ["N°", "NOM", "Prenom", "Classe"] + ["G%d" % i for i in range(1, 13)] + ["Acquis", "%"]
larg = [5, 16, 14, 16] + [6] * 12 + [9, 8]
ws = feuille("08_Passeport", "PASSEPORT MACHINE  -  LES 12 GESTES",
             "Remplace le livret papier. Validation ORALE pendant l'atelier ('montre-moi'), cochee le soir. Le geste 12 est un objectif de FIN de parcours, travaille 5 min chaque samedi.",
             cols, larg, gel="E4")
colonnes_identite(ws)
quadriller(ws, 4, DERNIERE, 1, len(cols))
for r in range(4, DERNIERE + 1):
    for c in range(5, 17):
        ws.cell(row=r, column=c).fill = fond_jaune
        ws.cell(row=r, column=c).alignment = centre
    ws.cell(row=r, column=17, value='=IF(\'01_Apprenants\'!B%d="","",COUNTIF(E%d:P%d,"V"))' % (r, r, r)).font = calc
    ws.cell(row=r, column=18, value='=IF(Q%d="","",Q%d/12)' % (r, r)).font = calc
    ws.cell(row=r, column=18).number_format = "0%"
liste(ws, "\"V\"", "E4:P%d" % DERNIERE)
ws_legende = ws
ws.cell(row=DERNIERE + 2, column=1, value="Legende des 12 gestes :").font = gras
for i, g in enumerate(gestes):
    ws.cell(row=DERNIERE + 3 + i, column=1, value=g).font = base
    ws.merge_cells(start_row=DERNIERE + 3 + i, start_column=1, end_row=DERNIERE + 3 + i, end_column=5)

# =====================================================================  09_Checklist-S01
taches = [
    ("J-7", "Coder le jeu XO termine et le tester sur la machine de demo (c'est le WOW : sans lui, la seance perd son moteur)", "Capitaine"),
    ("J-7", "Installer Python + Thonny sur TOUTES les machines, meme version", "Les deux"),
    ("J-7", "Lancer un programme sur CHAQUE poste pour verifier (lancer demo/verifier_le_jeu.py)", "Les deux"),
    ("J-7", "Creer le dossier GEEKS sur le Bureau de chaque poste (cle-usb/installer_sur_ce_poste.py)", "Mecanicien"),
    ("J-7", "Regler la police de Thonny en taille 18 sur tous les postes et sur la machine de projection", "Mecanicien"),
    ("J-7", "Preparer la cle USB maitresse (outils/preparer_la_cle.py)", "Capitaine"),
    ("J-7", "Verifier le videoprojecteur AVEC le cable et la machine du jour", "Capitaine"),
    ("J-7", "Reserver la salle 30 min avant (Sas Permis Machine)", "Les deux"),
    ("J-1", "Imprimer 01 - Cartes de signalisation (1 page par binome, papier epais)", "Mecanicien"),
    ("J-1", "Imprimer 02 - Affiche 3 avant moi (A3)", "Mecanicien"),
    ("J-1", "Imprimer 03 - Affiche Contrat des Geeks (A3)", "Mecanicien"),
    ("J-1", "Imprimer 04 - Affiche Dictionnaire des erreurs (A3)", "Mecanicien"),
    ("J-1", "Imprimer 05 - Mur de Mission (A3 paysage)", "Mecanicien"),
    ("J-1", "Imprimer 06 - Fiche memo eleve (1 par binome)", "Mecanicien"),
    ("J-1", "Imprimer 07 - Cartes-missions station 1 (6 ex.)", "Capitaine"),
    ("J-1", "Imprimer 08 - Enigmes station 2 (6 ex., recto-verso)", "Capitaine"),
    ("J-1", "Imprimer 09 - Ma fiche de Geek (1 par eleve)", "Capitaine"),
    ("J-1", "Imprimer 10 - Grille d'observation + corriges (2 ex.)", "Capitaine"),
    ("J-1", "Imprimer 11 - Etiquettes prenoms (3 pages) et les decouper", "Mecanicien"),
    ("J-1", "Imprimer 12 - Affiche Aider sans faire a la place (2 ex.)", "Capitaine"),
    ("J-1", "Imprimer 13 - Cartes des pistes Rouge et Noire (1 par binome)", "Mecanicien"),
    ("J-1", "Imprimer MON-SCRIPT d'animation (7 pages, agrafe)", "Capitaine"),
    ("J-1", "Acheter / preparer : post-it (2 par eleve), feutres, gommettes-badges, ruban adhesif", "Mecanicien"),
    ("J-1", "Preparer la boite a post-it et le minuteur visible", "Mecanicien"),
    ("J-1", "Relire la fiche de seance en entier, a deux", "Les deux"),
    ("Jour J", "Arriver 30 min avant. Machines allumees, Thonny ouvert, dossier GEEKS visible", "Les deux"),
    ("Jour J", "Lancer le jeu fini et le REDUIRE (ne jamais chercher le fichier devant la classe)", "Capitaine"),
    ("Jour J", "Machine de reserve allumee au fond de la salle", "Mecanicien"),
    ("Jour J", "Afficher les 4 affiches + le Mur de Mission", "Mecanicien"),
    ("Jour J", "Poser sur chaque poste : fiche memo, 4 cartes, carte des pistes, 2 post-it par eleve", "Les deux"),
    ("Jour J", "Verifier que mon_xo/jeu.py est bien present et s'ouvre sur chaque poste", "Mecanicien"),
    ("Jour J", "Decider et dire a voix haute : qui est Capitaine, qui est Mecanicien", "Les deux"),
    ("Jour J", "Choisir le signal de silence et s'accorder dessus", "Les deux"),
    ("Pendant", "A 104 min : verifier qu'AUCUN ecran n'est reste vide. Priorite absolue.", "Les deux"),
    ("Pendant", "Sauvegarder le travail de chaque binome sur la cle (4-SAUVEGARDES-ELEVES/S01)", "Mecanicien"),
    ("Apres", "Finaliser le code officiel S01 et le copier sur la cle", "Capitaine"),
    ("Apres", "Remplir 03_Presence et 04_Suivi-seances", "Mecanicien"),
    ("Apres", "Saisir le diagnostic dans 02_Diagnostic", "Mecanicien"),
    ("Apres", "Trier les post-it en 2 tas et noter la difficulte la plus citee", "Les deux"),
    ("Apres", "Etablir la liste des 10 minutes pour la seance 2", "Les deux"),
    ("Apres", "Envoyer le message aux familles", "Capitaine"),
    ("Apres", "Repondre aux 3 questions de la revue (onglet 10)", "Les deux"),
    ("Apres", "Echanger les roles pour la seance 2", "Les deux"),
]
cols = ["Quand", "Tache", "Responsable", "Fait ?", "Date", "Remarques"]
ws = feuille("09_Checklist-S01", "CHECKLIST DE PREPARATION  -  SEANCE 1",
             "Tout ce qui doit etre fait avant, pendant et apres la seance 1. Cochez au fur et a mesure. Le tableau de bord compte ce qui reste.",
             cols, [10, 82, 14, 12, 12, 30], gel="A4")
for i, (quand, tache, qui) in enumerate(taches):
    r = 4 + i
    ws.cell(row=r, column=1, value=quand).font = gras
    ws.cell(row=r, column=2, value=tache).font = base
    ws.cell(row=r, column=2).alignment = retour
    ws.cell(row=r, column=3, value=qui).font = base
    ws.cell(row=r, column=4, value="A faire").font = base
    ws.cell(row=r, column=4).fill = fond_jaune
    ws.cell(row=r, column=5).fill = fond_jaune
    ws.cell(row=r, column=5).number_format = "DD/MM/YYYY"
    ws.cell(row=r, column=6).fill = fond_jaune
    if quand == "J-7":   ws.cell(row=r, column=1).fill = PatternFill("solid", fgColor=ROUGE)
    elif quand == "J-1": ws.cell(row=r, column=1).fill = PatternFill("solid", fgColor=ORANGE)
    elif quand == "Jour J": ws.cell(row=r, column=1).fill = fond_jaune
    else: ws.cell(row=r, column=1).fill = fond_vert
FIN_CHK = 3 + len(taches)
quadriller(ws, 4, FIN_CHK, 1, 6)
liste(ws, P_FAIT, "D4:D%d" % FIN_CHK)
ws.conditional_formatting.add("D4:D%d" % FIN_CHK,
    CellIsRule(operator="equal", formula=['"Fait"'], fill=PatternFill("solid", fgColor=VERT)))

# =====================================================================  10_Journal-enseignants
cols = ["Seance", "Date", "Capitaine", "Mecanicien", "Presents", "Q1 - Qui a decroche, et qu'est-ce qu'on fait samedi ?",
        "Q2 - Quelle explication n'a pas marche, et comment on la reformule ?",
        "Q3 - La brique de la semaine prochaine est-elle trop grosse ?",
        "Notion la plus citee sur les post-it", "Decisions prises"]
ws = feuille("10_Journal-enseignants", "REVUE D'APRES-SEANCE  -  15 MINUTES, A DEUX",
             "A remplir juste apres chaque seance, avant de rentrer. C'est le meilleur outil de preparation de la seance suivante qui existe.",
             cols, [9, 12, 15, 15, 10, 44, 44, 34, 28, 40], gel="A4")
for i in range(22):
    r = 4 + i
    ws.cell(row=r, column=1, value=SEANCES[i]).font = gras
    ws.cell(row=r, column=2).number_format = "DD/MM/YYYY"
    for c in range(2, 11):
        ws.cell(row=r, column=c).fill = fond_jaune
        ws.cell(row=r, column=c).alignment = retour
    ws.row_dimensions[r].height = 46
quadriller(ws, 4, 25, 1, 10)

# =====================================================================  11_Materiel
materiel = [
    ("Impression", "Cartes de signalisation (1 page / binome)", 10, "Papier epais 160g + plastification"),
    ("Impression", "Affiches A3 (3 avant moi, Contrat, Erreurs)", 3, "Couleur"),
    ("Impression", "Mur de Mission A3 paysage", 1, "A coller sur papier kraft si possible"),
    ("Impression", "Fiche memo eleve", 10, "1 par binome"),
    ("Impression", "Cartes des pistes Rouge/Noire", 10, "1 par binome"),
    ("Impression", "Station 1 - cartes-missions", 6, "A decouper"),
    ("Impression", "Station 2 - enigmes (recto-verso)", 6, ""),
    ("Impression", "Station 3 - Ma fiche de Geek", 20, "1 par eleve"),
    ("Impression", "Grille d'observation + corriges", 2, "PAGE 2 = CORRIGES, ne pas laisser trainer"),
    ("Impression", "Etiquettes prenoms", 3, "24 etiquettes, a decouper"),
    ("Impression", "Affiche Aider sans faire a la place", 2, "Cote enseignants"),
    ("Impression", "MON-SCRIPT d'animation", 1, "7 pages, agrafe"),
    ("Achat", "Post-it", 2, "PAR ELEVE ET PAR SEANCE - prevoir large"),
    ("Achat", "Feutres noirs pointe large", 4, "Etiquettes et affiches"),
    ("Achat", "Gommettes de couleur (= badges)", 1, "Une couleur par badge"),
    ("Achat", "Ruban adhesif / porte-badges", 1, ""),
    ("Achat", "Boite ou bocal pour les post-it de sortie", 1, ""),
    ("Achat", "Minuteur visible de toute la salle", 1, "Ou un chronometre projete"),
    ("Achat", "Cle USB", 1, "Contenu : voir le dossier cle-usb/"),
    ("Salle", "Videoprojecteur teste avec le cable du jour", 1, ""),
    ("Salle", "Machine de reserve allumee au fond", 1, ""),
    ("Salle", "Mur libre pour les affiches", 1, ""),
    ("Salle", "Disposition : tous les ecrans visibles depuis le fond", 1, "Jamais en epi dos au mur"),
    ("Logiciel", "Python 3 installe (meme version partout)", 0, "Version utilisee : ..............."),
    ("Logiciel", "Thonny installe", 0, "Police reglee sur 18"),
    ("Logiciel", "Dossier GEEKS cree sur chaque Bureau", 0, "Via installer_sur_ce_poste.py"),
]
cols = ["Categorie", "Article", "Quantite prevue", "Quantite reelle", "Ou / qui", "Statut", "Cout", "Remarques"]
ws = feuille("11_Materiel", "MATERIEL ET INVENTAIRE",
             "Ce qu'il faut imprimer, acheter, installer. Mettez le statut a jour : le tableau de bord compte ce qui reste.",
             cols, [12, 48, 14, 14, 16, 12, 10, 44], gel="A4")
for i, (cat, art, qte, rem) in enumerate(materiel):
    r = 4 + i
    ws.cell(row=r, column=1, value=cat).font = gras
    ws.cell(row=r, column=2, value=art).font = base
    ws.cell(row=r, column=2).alignment = retour
    if qte: ws.cell(row=r, column=3, value=qte).font = base
    ws.cell(row=r, column=4).fill = fond_jaune
    ws.cell(row=r, column=5).fill = fond_jaune
    ws.cell(row=r, column=6, value="A faire").font = base
    ws.cell(row=r, column=6).fill = fond_jaune
    ws.cell(row=r, column=7).fill = fond_jaune
    ws.cell(row=r, column=8, value=rem).font = base
    ws.cell(row=r, column=8).alignment = retour
FIN_MAT = 3 + len(materiel)
quadriller(ws, 4, FIN_MAT, 1, 8)
liste(ws, P_FAIT, "F4:F%d" % FIN_MAT)
ws.cell(row=FIN_MAT + 2, column=2, value="TOTAL des couts saisis").font = gras
ws.cell(row=FIN_MAT + 2, column=7, value="=SUM(G4:G%d)" % FIN_MAT).font = calc

# =====================================================================  12_Tableau-de-bord
ws = wb.create_sheet("12_Tableau-de-bord")
ws.sheet_view.showGridLines = False
ws.column_dimensions["A"].width = 52; ws.column_dimensions["B"].width = 14
ws.column_dimensions["C"].width = 16; ws.column_dimensions["D"].width = 62
ws["A1"] = "TABLEAU DE BORD"; ws["A1"].font = h1; ws["A1"].fill = fond_titre
ws.merge_cells("A1:D1"); ws.row_dimensions[1].height = 26
ws["A2"] = "Tout se calcule automatiquement a partir des autres onglets. A regarder une fois par mois, et avant chaque reunion."
ws["A2"].font = petit; ws.merge_cells("A2:D2")

def section(r, titre):
    ws.cell(row=r, column=1, value=titre).font = Font(name=F, size=11, bold=True, color="FFFFFF")
    ws.cell(row=r, column=1).fill = fond_col
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)

def indicateur(r, libelle, formule, cible, commentaire, fmt=None):
    ws.cell(row=r, column=1, value=libelle).font = base
    c = ws.cell(row=r, column=2, value=formule); c.font = calc; c.alignment = centre
    if fmt: c.number_format = fmt
    ws.cell(row=r, column=3, value=cible).font = gras
    ws.cell(row=r, column=3).alignment = centre
    d = ws.cell(row=r, column=4, value=commentaire); d.font = petit; d.alignment = retour
    for col in range(1, 5):
        ws.cell(row=r, column=col).border = bord

r = 4
section(r, "L'EFFECTIF"); r += 1
ws.cell(row=r, column=2, value="Valeur").font = hcol; ws.cell(row=r, column=2).fill = fond_col
ws.cell(row=r, column=3, value="Cible").font = hcol; ws.cell(row=r, column=3).fill = fond_col
ws.cell(row=r, column=4, value="Que faire si on est hors cible").font = hcol; ws.cell(row=r, column=4).fill = fond_col
ws.cell(row=r, column=1, value="Indicateur").font = hcol; ws.cell(row=r, column=1).fill = fond_col
r += 1
indicateur(r, "Eleves inscrits", "=COUNTA('01_Apprenants'!B4:B%d)" % DERNIERE, "", "Total des lignes remplies dans 01_Apprenants."); r += 1
indicateur(r, "dont Jerusalem Geeks (9-12)", "=COUNTIF('01_Apprenants'!D4:D%d,\"Jerusalem*\")" % DERNIERE, "", ""); r += 1
indicateur(r, "dont Jeremiah Geeks (12-18)", "=COUNTIF('01_Apprenants'!D4:D%d,\"Jeremiah*\")" % DERNIERE, "", ""); r += 1
indicateur(r, "Binomes a prevoir (arrondi au superieur)", "=ROUNDUP(B6/2,0)", "max 12", "Au-dela de 24 eleves par classe avec 2 enseignants, il faut un 3e encadrant : le dire aux responsables AVANT la rupture."); r += 1
indicateur(r, "Eleves actifs", "=COUNTIF('01_Apprenants'!AA4:AA%d,\"Actif\")" % DERNIERE, "", ""); r += 2

section(r, "LES PROFILS (apres le Test de Decollage)"); r += 1
for code, libelle, aide in (("P0", "P0 Decouvreur - ne maitrise pas la machine", "Piste Bleue, squelette de code fourni, binome P1, vue de pres 3x par seance."),
                            ("P1", "P1 Initie - sait s'en servir, n'a jamais code", "C'est la cible standard du cours. Piste Rouge."),
                            ("P2", "P2 Autonome", "Piste Rouge puis Noire. Geek Mentor a partir de la seance 4."),
                            ("P3", "P3 Avance - sait deja coder", "Piste Noire systematique + mission speciale sur un module bonus.")):
    indicateur(r, libelle, "=COUNTIF('02_Diagnostic'!K4:K%d,\"%s*\")" % (DERNIERE, code), "", aide); r += 1
indicateur(r, "Eleves diagnostiques", "=COUNTA('02_Diagnostic'!K4:K%d)" % DERNIERE, "= effectif", "Si l'ecart persiste apres la seance 2, completer le diagnostic des absents."); r += 2

section(r, "LA SANTE DU DISPOSITIF"); r += 1
indicateur(r, "Taux de presence moyen", "=IFERROR(AVERAGE('03_Presence'!AC4:AC%d),\"\")" % DERNIERE, "> 85 %",
           "Sous 85 % : enqueter aupres des familles. L'absence est le premier facteur d'abandon.", "0%"); r += 1
indicateur(r, "Eleves sur la LISTE DES 10 MINUTES", "=COUNTIF('04_Suivi-seances'!AD4:AD%d,\"OUI\")" % DERNIERE, "0",
           "Deux seances de suite sans production. Chacun doit avoir un tete-a-tete de 10 min a la prochaine seance."); r += 1
indicateur(r, "Briques produites (toutes seances, tous eleves)", "=SUM('04_Suivi-seances'!AA4:AA%d)" % DERNIERE, "", ""); r += 1
indicateur(r, "Seances manquees sans production", "=SUM('04_Suivi-seances'!AC4:AC%d)" % DERNIERE, "le plus bas possible", ""); r += 1
indicateur(r, "Observations sans action realisee", "=COUNTIF('05_Observations'!I4:I120,\"A faire\")+COUNTIF('05_Observations'!I4:I120,\"En cours\")", "0",
           "Une observation sans action decidee et faite ne sert a rien."); r += 1
indicateur(r, "Badges distribues", "=SUM('07_Badges-Grades'!R4:R%d)" % DERNIERE, "",
           "Objectif : au moins 1 badge par eleve et par seance."); r += 2

section(r, "L'EQUITE (a surveiller de pres)"); r += 1
indicateur(r, "Eleves SANS ordinateur a la maison", "=COUNTIF('01_Apprenants'!W4:W%d,\"Non\")" % DERNIERE, "",
           "AUCUN devoir ne doit jamais etre obligatoire. Le redire a voix haute a chaque distribution de defi."); r += 1
indicateur(r, "Eleves sans internet a la maison", "=COUNTIF('01_Apprenants'!X4:X%d,\"Non\")" % DERNIERE, "",
           "Rien dans le cours ne doit dependre d'internet."); r += 1
indicateur(r, "Eleves n'ayant jamais code", "=COUNTIF('02_Diagnostic'!G4:G%d,\"Jamais\")" % DERNIERE, "", ""); r += 1
indicateur(r, "Passeport Machine : moyenne des gestes acquis", "=IFERROR(AVERAGE('08_Passeport'!Q4:Q%d),\"\")" % DERNIERE, "12 en fin de parcours",
           "Le geste 12 (frappe au clavier) est un objectif de fin d'annee, pas de debut.", "0.0"); r += 1
indicateur(r, "Autorisations photo obtenues", "=COUNTIF('01_Apprenants'!V4:V%d,\"Oui\")" % DERNIERE, "",
           "Aucune photo d'eleve utilisee sans accord ecrit."); r += 2

section(r, "LA PREPARATION DE LA SEANCE 1"); r += 1
indicateur(r, "Taches de preparation restantes", "=COUNTIF('09_Checklist-S01'!D4:D%d,\"A faire\")+COUNTIF('09_Checklist-S01'!D4:D%d,\"En cours\")" % (FIN_CHK, FIN_CHK), "0",
           "Detail dans l'onglet 09."); r += 1
indicateur(r, "Taches faites", "=COUNTIF('09_Checklist-S01'!D4:D%d,\"Fait\")" % FIN_CHK, "", ""); r += 1
indicateur(r, "Avancement de la preparation", "=IFERROR(B%d/(B%d+B%d),\"\")" % (r - 1, r - 1, r - 2), "100 %", "", "0%"); r += 1
indicateur(r, "Materiel non encore pret", "=COUNTIF('11_Materiel'!F4:F%d,\"A faire\")+COUNTIF('11_Materiel'!F4:F%d,\"En cours\")" % (FIN_MAT, FIN_MAT), "0",
           "Detail dans l'onglet 11."); r += 2

ws.cell(row=r, column=1, value="RAPPEL : l'indicateur le plus important du programme n'est pas dans ce tableau.").font = gras
ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4); r += 1
ws.cell(row=r, column=1, value="C'est celui-ci : 100 % des eleves repartent-ils de chaque seance avec un jeu qui fonctionne ? "
                               "Si la reponse est non, on allege la brique ou on renforce la piste Bleue -- on ne demande pas aux eleves d'aller plus vite.").font = base
ws.cell(row=r, column=1).alignment = retour
ws.merge_cells(start_row=r, start_column=1, end_row=r + 1, end_column=4)

import os
ordre = ["00_Mode-emploi","01_Apprenants","02_Diagnostic","03_Presence","04_Suivi-seances",
         "05_Observations","06_Binomes","07_Badges-Grades","08_Passeport","09_Checklist-S01",
         "10_Journal-enseignants","11_Materiel","12_Tableau-de-bord","13_Listes"]
wb._sheets = [wb[n] for n in ordre]
racine = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
wb.save(os.path.join(racine, "suivi", "classeur-de-suivi.xlsx"))
print("ecrit : suivi/classeur-de-suivi.xlsx")
print("onglets :", ", ".join(wb.sheetnames))
