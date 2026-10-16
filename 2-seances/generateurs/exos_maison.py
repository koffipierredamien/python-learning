# -*- coding: utf-8 -*-
"""Generateur des exercices de maison (feuille eleve 2 pages + corrige)
   HTML autonome -> PDF (chromium) -> PNG (pymupdf)."""
import html, re, os, subprocess, sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME = "/opt/pw-browsers/chromium"

# ---------------------------------------------------------------- coloration
MOTS = ("print", "input", "int", "str", "if", "else", "while", "and", "or", "not")
MOTIF = re.compile(
    r'(?P<com>#[^\n]*)'
    r'|(?P<txt>"[^"\n]*")'
    r"|(?P<mot>\b(?:" + "|".join(MOTS) + r")\b)"
)

def colorie(code):
    out, pos = [], 0
    for m in MOTIF.finditer(code):
        out.append(html.escape(code[pos:m.start()], quote=False))
        if m.lastgroup == "com":
            cls = "c"
        elif m.lastgroup == "txt":
            cls = "s"
        else:
            cls = "k"
        out.append('<span class="%s">%s</span>' % (cls, html.escape(m.group(), quote=False)))
        pos = m.end()
    out.append(html.escape(code[pos:], quote=False))
    return "".join(out)

def extrait(chemin, debut, fin):
    """lignes debut..fin incluses, 1-indexees"""
    lignes = open(chemin, encoding="utf-8").read().split("\n")
    return "\n".join(lignes[debut - 1:fin]).strip("\n")

# ---------------------------------------------------------------- styles
STYLE_COMMUN = """
 html,*{-webkit-print-color-adjust:exact;print-color-adjust:exact;box-sizing:border-box}
 @page{size:A4 portrait;margin:0}
 body{margin:0;font-family:"Trebuchet MS",Verdana,sans-serif;color:#14142b;background:#fff}
 .saut{page-break-before:always}
 .mono{font-family:"Courier New",monospace;font-weight:bold;background:#f0f0f6;
       padding:.3mm 1mm;border-radius:1mm}
"""

STYLE_EXO = STYLE_COMMUN + """
  body{font-size:9.3pt;padding:6mm 8mm 4mm}
  .band{background:#12122a;color:#fff;border-radius:3mm;padding:3.2mm 5mm;margin-bottom:2.8mm}
  .band .k{font-size:9pt;letter-spacing:1.2pt;color:#ffb74d;font-weight:bold}
  .band h1{font-size:19pt;margin:1mm 0 1.2mm}
  .band .s{font-size:9.9pt;color:#a8a8c0;line-height:1.4}
  .band .f{font-family:"Courier New",monospace;background:#20204a;color:#4fc3f7;
           padding:.8mm 2.2mm;border-radius:1.4mm;display:inline-block;margin-top:1.8mm;font-size:9.8pt}
  .regle{background:#6b2d8f;color:#fff;border-radius:2.6mm;padding:2.6mm 4mm;
         margin-bottom:2.8mm;font-size:9.7pt;line-height:1.4}
  .row{display:flex;gap:3mm;margin-bottom:2.8mm}
  .goal{flex:1.1;border:.6mm solid #2fb765;border-radius:2.6mm;overflow:hidden}
  .goal .t{background:#2fb765;color:#fff;font-weight:bold;padding:1.1mm 3mm;font-size:9.8pt}
  .goal pre{margin:0;padding:2.2mm 2.6mm;font-family:"Courier New",monospace;font-size:7.2pt;
            line-height:1.3;background:#f2faf5;white-space:pre}
  .goal b{color:#0c5c29}
  .kit{flex:1;border:.6mm solid #d79a00;border-radius:2.6mm;overflow:hidden;background:#fffaf0}
  .kit .t{background:#d79a00;color:#fff;font-weight:bold;padding:1.1mm 3mm;font-size:9.8pt}
  .kit .b{padding:2mm 2.6mm;font-size:8.1pt;line-height:1.34}
  .kit .m{font-family:"Courier New",monospace;font-weight:bold;background:#fff;
          border:.3mm solid #e8d6a8;border-radius:1mm;padding:.4mm 1mm}
  .kit hr{border:0;border-top:.3mm dashed #d79a00;margin:1.5mm 0}
  .st{border:.5mm solid #14142b;border-radius:2.6mm;margin-bottom:2.2mm;overflow:hidden;page-break-inside:avoid}
  .st .h{background:#14142b;color:#fff;padding:1.1mm 3mm;font-size:10.4pt;font-weight:bold;
         display:flex;gap:2.6mm;align-items:center}
  .st .h .n{background:#ffb74d;color:#14142b;border-radius:50%;width:6mm;height:6mm;line-height:6mm;
            text-align:center;font-size:10pt;display:inline-block}
  .st .c{padding:1.9mm 2.6mm;line-height:1.34}
  .st .c ul{margin:0;padding-left:5mm}.st .c li{margin-bottom:.9mm}
  .bloc{font-family:"Courier New",monospace;font-size:8.2pt;background:#12122a;color:#4fc3f7;
        padding:1.7mm 2.6mm;border-radius:1.6mm;white-space:pre;line-height:1.32;margin:1.2mm 0}
  .bloc i{color:#ffb74d;font-style:normal}
  .tip{color:#6b2d8f;font-weight:bold}
  .fin{background:#f3f3f8;border-left:3mm solid #6b2d8f;border-radius:2mm;
       padding:2.3mm 3mm;font-size:9pt;line-height:1.36}
  .suite{background:#12122a;color:#fff;border-radius:2.4mm;padding:2.2mm 4mm;margin-bottom:3mm;
         font-size:10.4pt;font-weight:bold;display:flex;justify-content:space-between}
  .suite span{color:#ffb74d;font-weight:normal;font-size:9.4pt}
"""

STYLE_COR = STYLE_COMMUN + """
 body{font-size:9.6pt;padding:7mm 8mm 5mm}
 .band{background:#0c5c29;color:#fff;border-radius:3mm;padding:3.6mm 5mm;margin-bottom:3.4mm}
 .band .k{font-size:9pt;letter-spacing:1.2pt;color:#a8e6bd;font-weight:bold}
 .band h1{font-size:20pt;margin:1mm 0 1.2mm}
 .band .s{font-size:10pt;color:#d8f0e2;line-height:1.45}
 pre{margin:0 0 2.6mm;background:#12122a;color:#e8e8f2;border-radius:2.6mm;padding:3mm 4mm;
     font-family:"Courier New",monospace;font-size:%(taille)s;line-height:1.3;white-space:pre-wrap}
 pre .c{color:#7f7f9c} pre .s{color:#ffb74d} pre .k{color:#4fc3f7;font-weight:bold}
 .coupe{background:#6b2d8f;color:#fff;border-radius:2.2mm;padding:2mm 3.4mm;margin-bottom:2.6mm;
        font-size:9.4pt;line-height:1.4}
 .note{background:#fffaf0;border:.6mm solid #d79a00;border-radius:2.6mm;padding:2.6mm 3.4mm;
       margin-bottom:2.6mm;line-height:1.42;font-size:9.2pt}
 .note b{color:#a65d00}
 .note h3{margin:0 0 1.4mm;font-size:10.6pt;color:#a65d00}
 .note ul{margin:1.2mm 0 0;padding-left:5mm}.note li{margin-bottom:1.1mm}
 .note .m{font-family:"Courier New",monospace;font-weight:bold;background:#fff;
          border:.3mm solid #e8d6a8;border-radius:1mm;padding:.3mm 1mm}
 .suite{background:#0c5c29;color:#fff;border-radius:2.4mm;padding:2.2mm 4mm;margin-bottom:3mm;
        font-size:10.4pt;font-weight:bold;display:flex;justify-content:space-between}
 .suite span{color:#a8e6bd;font-weight:normal;font-size:9.4pt}
"""

# ---------------------------------------------------------------- rendu
def ecrire(chemin, titre, style, corps):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    open(chemin, "w", encoding="utf-8").write(
        '<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>'
        + titre + '</title>\n<style>' + style + '</style></head><body>\n'
        + corps + '\n</body></html>\n')

def pdf(src_html, out_pdf):
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", "--print-to-pdf=" + out_pdf,
                    "file://" + src_html], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def png(src_pdf, prefixe):
    import pymupdf
    doc = pymupdf.open(src_pdf)
    noms = []
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=150)
        nom = "%s-%d.png" % (prefixe, i + 1)
        pix.save(nom)
        noms.append(nom)
    return noms, doc

def mesure(src_pdf):
    import pymupdf
    doc = pymupdf.open(src_pdf)
    return [round(100 * max(b[3] for b in p.get_text("blocks")) / p.rect.height)
            for p in doc]
