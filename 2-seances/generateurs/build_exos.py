# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import exos_maison as E
from donnees_exos import TOUS

def etape(num, titre, corps):
    return ('<div class="st"><div class="h"><span class="n">%s</span> %s</div>'
            '<div class="c">%s</div></div>\n' % (num, titre, corps))

def feuille_exo(d, dossier):
    p = []
    p.append('<div class="band">\n'
             '  <div class="k">%s</div>\n  <h1>%s %s</h1>\n  <div class="s">%s</div>\n'
             '  <div class="f">Thonny → Fichier → Nouveau → Enregistrer sous :  %s</div>\n</div>\n'
             % (d["kicker"], d["emoji"], d["nom"], d["chapo"], d["fichier"]))
    p.append('<div class="regle">%s</div>\n' % d["regle"])
    p.append('<div class="row">\n'
             '  <div class="goal"><div class="t">✅ CE QUE TON PROGRAMME DOIT FAIRE</div>\n'
             '<pre>%s</pre></div>\n'
             '  <div class="kit"><div class="t">🧰 LA BOÎTE À OUTILS</div>\n'
             '    <div class="b">%s</div>\n  </div>\n</div>\n' % (d["ecran"], d["kit"]))
    for n, t, c in d["etapes1"]:
        p.append(etape(n, t, c))
    p.append('<div class="fin" style="border-color:#ffb74d;background:#fffaf0">\n'
             '  👉 <b>La suite est sur la page 2</b> : le cœur du programme, la fin, et les bonus.\n</div>\n')
    p.append('<div class="saut"></div>\n')
    p.append('<div class="suite">%s %s — la suite <span>page 2 sur 2 · %s</span></div>\n'
             % (d["emoji"], d["nom"], d["fichier"]))
    for n, t, c in d["etapes2"]:
        p.append(etape(n, t, c))
    p.append('<div class="st" style="border-color:#d79a00"><div class="h" style="background:#d79a00">'
             '<span class="n" style="background:#fff">⭐</span> SI TU AS FINI — LES BONUS</div>'
             '<div class="c">%s</div></div>\n' % d["bonus"])
    p.append('<div class="fin">%s</div>\n' % d["fin"])
    html = "".join(p)
    src = os.path.join(dossier, "sources", d["base"] + ".html")
    E.ecrire(src, "Exercice de maison — " + d["titre"], E.STYLE_EXO + d.get("css1", ""), html)
    return src

def feuille_cor(d, dossier):
    chemin_py = os.path.join(dossier, d["py"])
    style = E.STYLE_COR % {"taille": d["taille"]}
    p = []
    p.append('<div class="band">\n  <div class="k">CORRECTION · POUR L\'ENSEIGNANT ET LES PARENTS</div>\n'
             '  <h1>✅ %s</h1>\n  <div class="s">%s</div>\n</div>\n' % (d["nom"], d["cor_chapo"]))
    a, b = d["blocs"][0]
    p.append('<pre>%s</pre>\n' % E.colorie(E.extrait(chemin_py, a, b)))
    p.append('<div class="saut"></div>\n')
    p.append('<div class="suite">✅ %s — la suite <span>page 2 sur 2 · %s</span></div>\n'
             % (d["nom"], d["py"]))
    if d["coupe_texte"]:
        p.append('<div class="coupe">%s</div>\n' % d["coupe_texte"])
    a, b = d["blocs"][1]
    p.append('<pre>%s</pre>\n' % E.colorie(E.extrait(chemin_py, a, b)))
    p.append(d["cor_notes"])
    src = os.path.join(dossier, "sources", d["base_cor"] + ".html")
    E.ecrire(src, "Correction — " + d["titre"], style, "".join(p))
    return src

for d in TOUS:
    dossier = os.path.join(E.RACINE, d["dossier"], "a-envoyer")
    for src, base in ((feuille_exo(d, dossier), d["base"]),
                      (feuille_cor(d, dossier), d["base_cor"])):
        out_pdf = os.path.join(dossier, base + ".pdf")
        E.pdf(src, out_pdf)
        noms, doc = E.png(out_pdf, os.path.join(dossier, base))
        print("%-42s %d pages  remplissage %s" % (base, len(doc), E.mesure(out_pdf)))
