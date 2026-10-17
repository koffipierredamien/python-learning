# -*- coding: utf-8 -*-
"""L'affiche du trimestre : les sept cases du Mur de Mission, a cocher
   une par samedi. A4 portrait, a imprimer une fois et a coller au mur."""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import exos_maison as E

CASES = [
 ("6", "sam. 17 oct", "LE PLATEAU SE SOUVIENT",
  "Ton X reste sur le plateau. Pour la première fois, le programme se souvient."),
 ("7", "sam. 24 oct", "ON NE JOUE PAS DEUX FOIS<br>AU MÊME ENDROIT",
  "Le jeu refuse une case déjà prise. Plus moyen d'effacer le pion de l'autre."),
 ("8", "sam. 31 oct", "QUATRE COUPS D'AFFILÉE,<br>SANS BUG",
  "TP n°2. Deux heures, et un plateau qui tient le choc."),
 ("9", "sam. 7 nov", "LE JEU POSE<br>UNE SEULE QUESTION",
  "Le code rétrécit. Et le bug du zéro, trouvé le 24 octobre, meurt aujourd'hui."),
 ("10", "sam. 14 nov", "LE JEU TOURNE TOUT SEUL",
  "Neuf tours, chacun son tour. Et le fichier est plus court qu'avant."),
 ("11", "sam. 21 nov", "LE JEU SAIT QUI GAGNE",
  "Une vraie partie : il s'arrête, il annonce le vainqueur, il voit le match nul."),
 ("12", "sam. 28 nov", "ON A FAIT UN TOURNOI",
  "TP n°3. On teste, on fignole — et on joue les uns contre les autres."),
]

STYLE = """
 html,*{-webkit-print-color-adjust:exact;print-color-adjust:exact;box-sizing:border-box}
 @page{size:A4 portrait;margin:0}
 body{margin:0;font-family:"Trebuchet MS",Verdana,sans-serif;color:#14142b;background:#fff;
      padding:7mm 8mm 5mm}
 .band{background:#12122a;color:#fff;border-radius:3mm;padding:3.4mm 5mm;margin-bottom:3.2mm;
       text-align:center}
 .band .k{font-size:9.5pt;letter-spacing:2pt;color:#ffb74d;font-weight:bold}
 .band h1{font-size:24pt;margin:1.4mm 0 1.4mm;letter-spacing:.5pt}
 .band .s{font-size:11pt;color:#a8a8c0}
 .grille{display:flex;flex-wrap:wrap;gap:2.8mm}
 .c{width:calc(50% - 1.4mm);border:.7mm solid #14142b;border-radius:2.6mm;overflow:hidden;
    display:flex;flex-direction:column}
 .c.large{width:100%}
 .c .h{background:#14142b;color:#fff;padding:1.4mm 3mm;display:flex;align-items:center;gap:2.6mm}
 .c .n{background:#ffb74d;color:#14142b;border-radius:50%;width:7.6mm;height:7.6mm;line-height:7.6mm;
       text-align:center;font-size:12.5pt;font-weight:bold;flex:none}
 .c .d{font-size:9.6pt;color:#ffb74d;font-weight:bold;letter-spacing:.6pt}
 .c .b{padding:2.4mm 3mm 2.6mm;flex:1;display:flex;flex-direction:column}
 .c .t{font-size:12.6pt;font-weight:bold;line-height:1.2;color:#12122a;margin-bottom:1.6mm}
 .c .p{font-size:9.1pt;line-height:1.36;color:#3a3a52;flex:1}
 .c .pied{display:flex;align-items:center;gap:2.6mm;margin-top:2.2mm}
 .c .coche{width:7mm;height:7mm;border:.6mm solid #14142b;border-radius:1.2mm;flex:none}
 .c .photo{flex:1;height:7mm;border:.4mm dashed #9a9ab0;border-radius:1.2mm;font-size:7.4pt;
           color:#9a9ab0;text-align:center;line-height:7mm;letter-spacing:.8pt}
 .c.tp{border-color:#6b2d8f}
 .c.tp .h{background:#6b2d8f}
 .c.tp .n{background:#fff;color:#6b2d8f}
 .fin{margin-top:3mm;background:#2fb765;color:#fff;border-radius:2.6mm;padding:3mm 5mm;
      text-align:center;font-size:11.4pt;line-height:1.45}
 .fin b{font-size:13pt}
"""

corps = ['<div class="band"><div class="k">ACPROKIDS CODING CAMP · VISION PLÉNITUDES VIE</div>'
         '<h1>LE JEU XO — OCTOBRE ET NOVEMBRE</h1>'
         '<div class="s">Sept samedis. Une case cochée par samedi. '
         'À la fin, le jeu est à vous.</div></div>',
         '<div class="grille">']
for i, (num, date, titre, texte) in enumerate(CASES):
    tp = " tp" if num in ("8", "12") else ""
    large = " large" if i == len(CASES) - 1 else ""
    corps.append(
      '<div class="c%s%s"><div class="h"><span class="n">%s</span>'
      '<span class="d">%s</span></div>'
      '<div class="b"><div class="t">%s</div><div class="p">%s</div>'
      '<div class="pied"><div class="coche"></div>'
      '<div class="photo">LA PHOTO DU JOUR</div></div></div></div>'
      % (tp, large, num, date.upper(), titre, texte))
corps.append('</div>')
corps.append('<div class="fin"><b>Le 28 novembre, chacun repart avec son jeu.</b><br>'
             'Un vrai morpion à deux joueurs, qui sait qui a gagné — et que vous aurez écrit '
             'vous-mêmes, ligne par ligne.</div>')

ICI = os.path.join(E.RACINE, "a-afficher")
src = os.path.join(ICI, "sources", "affiche-du-trimestre.html")
E.ecrire(src, "Le jeu XO — octobre et novembre", STYLE, "\n".join(corps))
pdf = os.path.join(ICI, "affiche-du-trimestre.pdf")
E.pdf(src, pdf)
noms, doc = E.png(pdf, os.path.join(ICI, "affiche-du-trimestre"))
print("affiche : %d page(s), remplissage %s" % (doc.page_count, E.mesure(pdf)))
