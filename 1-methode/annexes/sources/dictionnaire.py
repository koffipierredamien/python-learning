# -*- coding: utf-8 -*-
"""Reconstruit le tableau du dictionnaire des erreurs (HTML puis PDF)
   a partir de l'annexe A6, pour que les deux ne divergent jamais."""
import html, io, os, re, subprocess

ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD = os.path.join(ICI, "A6-dictionnaire-des-erreurs.md")
HTML = os.path.join(ICI, "dictionnaire-des-erreurs.html")
PDF = os.path.join(ICI, "dictionnaire-des-erreurs.pdf")
CHROME = "/opt/pw-browsers/chromium"
LIGNES_VIDES = 6


def enrichir(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", lambda m: '<span class="c">%s</span>' % m.group(1), t)
    t = re.sub(r"\*\*([^*]+)\*\*", lambda m: "<b>%s</b>" % m.group(1), t)
    return t


def lire():
    sections = []
    for ligne in io.open(MD, encoding="utf-8"):
        ligne = ligne.rstrip("\n")
        m = re.match(r"^## \d+\. (.+)$", ligne)
        if m:
            sections.append((m.group(1), []))
            continue
        if ligne.startswith("| ☐ |") and sections:
            cases = [c.strip() for c in ligne.strip("|").split("|")]
            sections[-1][1].append(cases[1:])      # on jette la colonne a cocher
    return sections


def construire():
    out = ['<table>',
           "<tr><th>Traitée</th><th>Ce que l'ordinateur écrit</th><th>Ce qu'il veut dire</th>"
           "<th>Ce qu'on fait</th><th>Vers</th></tr>"]
    for titre, lignes in lire():
        out.append('<tr class="sec"><td colspan="5">%s</td></tr>' % enrichir(titre))
        for msg, sens, quoi, vers in lignes:
            out.append('<tr><td class="case"></td><td class="msg">%s</td><td>%s</td><td>%s</td>'
                       '<td class="s">%s</td></tr>'
                       % (enrichir(msg), enrichir(sens), enrichir(quoi), enrichir(vers)))
    out.append('<tr class="sec"><td colspan="5">Les erreurs rencontrées en classe, à ajouter</td></tr>')
    for _ in range(LIGNES_VIDES):
        out.append('<tr><td class="case"></td><td>&nbsp;</td><td></td><td></td><td></td></tr>')
    out.append('</table>')
    return "\n".join(out)


s = io.open(HTML, encoding="utf-8").read()
neuf = re.sub(r"<table>.*?</table>", lambda m: construire(), s, count=1, flags=re.S)
io.open(HTML, "w", encoding="utf-8").write(neuf)

subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                "--no-pdf-header-footer", "--print-to-pdf=" + PDF, "file://" + HTML],
               check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

import pymupdf
d = pymupdf.open(PDF)
print("%d lignes · %d page(s) · remplissage %s"
      % (sum(len(l) for _, l in lire()), d.page_count,
         [round(100 * max(b[3] for b in p.get_text("blocks")) / p.rect.height) for p in d]))
