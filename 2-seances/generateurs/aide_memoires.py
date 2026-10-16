# -*- coding: utf-8 -*-
"""Un seul gabarit, cinq aide-memoires. Un par seance a notion."""
import io, os, subprocess, html

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME = "/opt/pw-browsers/chromium"

GABARIT = u"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>Aide-mémoire — {titre}</title>
<style>
  html,*{{-webkit-print-color-adjust:exact;print-color-adjust:exact;box-sizing:border-box}}
  @page{{size:A4 portrait;margin:7mm 9mm}}
  body{{margin:0;font-family:"Trebuchet MS",Verdana,sans-serif;font-size:9.3pt;color:#14142b}}
  .consigne{{font-size:8.3pt;color:#333;border:1px dashed #999;padding:1.8mm;margin-bottom:2.4mm}}
  h1{{font-size:15.5pt;margin:0 0 .8mm;text-align:center}}
  .sur{{text-align:center;font-size:9pt;color:#555;margin-bottom:2mm}}
  h2{{font-size:10.4pt;background:#1a1a2e;color:#fff;padding:1mm 3mm;margin:2.6mm 0 1.2mm;border-radius:1.5mm}}
  h2.o{{background:#e07b1a}} h2.v{{background:#2e9e52}} h2.p{{background:#6b2d8f}}
  .cle{{background:#fff6d8;border:.7mm solid #d79a00;border-radius:2mm;padding:1.8mm;font-size:9.6pt;
       text-align:center;margin:1.4mm 0}}
  .code{{font-family:"Courier New",monospace;font-size:9.6pt;background:#12122a;color:#4fc3f7;
        padding:1.8mm 2.6mm;border-radius:1.5mm;white-space:pre;line-height:1.32;margin:1.2mm 0}}
  .code i{{color:#ffb74d;font-style:normal}}
  .code b{{color:#ff8a80;font-weight:normal}}
  .duo{{display:flex;gap:3mm;margin-top:1.2mm}}
  .duo > div{{flex:1;border:.5mm solid #1a1a2e;border-radius:2mm;padding:1.8mm;font-size:8.8pt;line-height:1.34}}
  .duo b.t{{display:block;font-size:10pt;margin-bottom:.8mm}}
  table{{width:100%;border-collapse:collapse;margin-top:1.1mm}}
  td,th{{border:1px solid #666;padding:.9mm 1.5mm;font-size:8.3pt;vertical-align:top;text-align:left}}
  th{{background:#eee}}
  .mono{{font-family:"Courier New",monospace;font-weight:bold}}
  .fait{{background:#eaf7ef;border:.5mm solid #2fb765;border-radius:2mm;padding:1.8mm 2.4mm;font-size:8.8pt;line-height:1.45}}
  .fait b{{color:#0c5c29}}
  .fait .ok{{color:#2e9e52;font-weight:bold}}
  @media print{{.consigne{{display:none}}}}
</style></head><body>
<div class="consigne"><b>À imprimer :</b> 1 par poste, A4 recto. Posé à côté du clavier.</div>
<h1>{emoji} {titre}</h1>
<div class="sur">Séance {num} — {date}</div>
{corps}
<h2 class="o">Si l'écran devient rouge</h2>
<table>
  <tr><th style="width:23%">Ce qui s'affiche</th><th style="width:35%">Ce que ça veut dire</th><th>Ce que je fais</th></tr>
  {erreurs}
</table>
<h2 class="v">Ce que ton jeu sait faire</h2>
<div class="fait">{acquis}</div>
</body></html>"""


def ligne_err(a, b, c):
    return u'<tr><td class="mono">%s</td><td>%s</td><td>%s</td></tr>' % (a, b, c)


ACQUIS_BASE = [
    u'afficher du texte et des phrases fabriquées avec le <span class="mono">+</span>',
    u'poser des questions au joueur et garder ses réponses',
    u'passer du texte au nombre et retour (<span class="mono">int()</span>, <span class="mono">str()</span>)',
    u'compter (<span class="mono">tour = tour + 1</span>)',
    u'décider avec <span class="mono">if</span> / <span class="mono">else</span>',
]

SEANCES = [
 dict(dossier="S06-le-plateau-se-souvient", num=6, date="samedi 17 octobre 2026",
      titre="LE PLATEAU SE SOUVIENT", emoji="🧠",
      nouveau=[u'garder neuf cases dans une <b>liste</b>, et <b>poser un symbole</b> qui reste'],
      corps=u"""
<h2>1 · La liste : une boîte à neuf compartiments</h2>
<div class="code">plateau = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            <i>0    1    2    3    4    5    6    7    8</i></div>
<div class="cle">Le <b>premier</b> compartiment porte le numéro <b>0</b>. Pas 1. <b>Jamais 1.</b></div>
<div class="duo">
  <div><b class="t">Lire une case</b>
    <div class="code" style="font-size:9pt">print(plateau[0])   <i>la 1re</i>
print(plateau[8])   <i>la 9e</i></div></div>
  <div><b class="t">Changer une case</b>
    <div class="code" style="font-size:9pt">plateau[4] = "X"
<i>la 5e case contient X</i></div></div>
</div>

<h2 class="p">2 · La ligne du jour</h2>
<div class="code">plateau[case - 1] = "X"</div>
<table>
  <tr><th style="width:30%">La case du joueur</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr>
  <tr><th>L'indice Python</th><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr>
</table>
<div class="cle" style="margin-top:1.4mm"><b>indice = case − 1</b> &nbsp;·&nbsp; si tu oublies le <b>− 1</b>,
le symbole se pose <b>à côté</b>, sans aucune erreur rouge.</div>

<h2>3 · Dessiner le plateau à partir de la liste</h2>
<div class="code">print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
print("---+---+---")
print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
print("---+---+---")
print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])</div>
<div class="cle">Pour voir le plateau <b>changer</b>, il faut <b>recopier ces cinq lignes après la pose</b>.</div>""",
      erreurs=[("IndexError", u"« Cette case n'existe pas dans la liste »", u"Une liste de 9 va de <b>0 à 8</b>. Vérifie ton <span class='mono'>− 1</span>"),
               ("TypeError", u"Je mélange du texte et un nombre", u"<span class='mono'>int()</span> pour calculer, <span class='mono'>str()</span> pour coller"),
               (u"<i>le X se pose à côté</i>", u"Tu as écrit <span class='mono'>plateau[case]</span>", u"<span class='mono'>plateau[case − 1]</span>, toujours"),
               (u"<i>le plateau ne change pas</i>", u"Tu l'affiches <b>avant</b> de poser", u"Recopie l'affichage <b>après</b> la pose")]),

 dict(dossier="S07-la-case-occupee", num=7, date="samedi 24 octobre 2026",
      titre="ON NE JOUE PAS DEUX FOIS AU MÊME ENDROIT", emoji="🚫",
      nouveau=[u'garder neuf cases dans une <b>liste</b>, et poser un symbole qui reste',
               u'<b>refuser</b> une case déjà prise ou impossible'],
      corps=u"""
<h2>1 · Comment savoir qu'une case est libre</h2>
<div class="cle">Une case libre n'est pas vide : <b>elle contient encore son numéro</b>.</div>
<div class="code">plateau[case - 1] == str(case)    <i>→ True : la case est LIBRE</i>
                                  <i>→ False : elle est PRISE</i></div>
<div style="font-size:8.6pt;margin-top:1mm"><span class="mono">str(case)</span> transforme le nombre
<span class="mono">3</span> en texte <span class="mono">"3"</span>, pour le comparer avec ce qu'il y a
dans la case — qui est du texte.</div>

<h2 class="p">2 · Le <span style="font-family:'Courier New'">if</span> dans le <span style="font-family:'Courier New'">if</span></h2>
<div class="code">if case &gt; 9:
<b>····</b>print("Cette case n'existe pas !")
else:
<b>····</b>if plateau[case - 1] == str(case):
<b>········</b>plateau[case - 1] = "X"
<b>····</b>else:
<b>········</b>print("Case deja prise !")</div>
<div class="duo">
  <div><b class="t">Les décalages</b><b>4 espaces</b> pour le premier niveau,
    <b>8 espaces</b> pour le deuxième. C'est le décalage qui dit <b>qui est dans qui</b>.</div>
  <div><b class="t">L'ordre des questions</b>La deuxième question ne se pose <b>que si</b> la réponse
    à la première est non. On ne demande pas si la case est libre si elle n'existe pas.</div>
</div>

<h2>3 · Teste les trois chemins</h2>
<table>
  <tr><th style="width:25%">Je tape</th><th>Ce qui doit se passer</th></tr>
  <tr><td class="mono">5</td><td>le symbole se pose</td></tr>
  <tr><td class="mono">5</td><td>« Case deja prise ! » — et le plateau ne bouge pas</td></tr>
  <tr><td class="mono">12</td><td>« Cette case n'existe pas ! »</td></tr>
</table>
<div class="cle" style="margin-top:1.4mm">⚠️ <b>Le bug connu :</b> si tu tapes <b>0</b>, le jeu accepte.
C'est normal pour l'instant — on le répare à la séance 9.</div>""",
      erreurs=[("IndentationError", u"Il manque le décalage après les deux-points", u"4 espaces, puis 8 pour le <span class='mono'>if</span> dans le <span class='mono'>if</span>"),
               (u"<i>ça se pose quand même</i>", u"La pose est <b>hors</b> du <span class='mono'>if</span>", u"Relis les décalages de haut en bas"),
               ("TypeError", u"<span class='mono'>str(case)</span> oublié", u"On compare du texte avec du texte"),
               (u"<i>deux messages</i>", u"Un <span class='mono'>print</span> en trop, hors du <span class='mono'>else</span>", u"Un seul message par chemin")]),

 dict(dossier="S09-et-ou", num=9, date="samedi 7 novembre 2026",
      titre="UNE SEULE QUESTION AU LIEU DE TROIS", emoji="🔗",
      nouveau=[u'garder neuf cases dans une <b>liste</b>, et poser un symbole qui reste',
               u'refuser une case déjà prise ou impossible — <b>en une seule ligne</b>'],
      corps=u"""
<h2>1 · Les deux mots du jour</h2>
<div class="duo">
  <div><b class="t">and &nbsp;— il faut TOUT</b>
    <div class="code" style="font-size:9pt">True  and True   → True
True  and False  → False
False and True   → False
False and False  → False</div>
    « Mon cahier <b>ET</b> mon stylo. »</div>
  <div><b class="t">or &nbsp;— il suffit d'UN</b>
    <div class="code" style="font-size:9pt">True  or False  → True
False or True   → True
True  or True    → True
False or False  → False</div>
    « Fini l'exercice <b>OU</b> aidé un voisin. »</div>
</div>

<h2 class="p">2 · Le coup valide, en une seule ligne</h2>
<div class="code">if case &gt;= 1 and case &lt;= 9 and plateau[case - 1] == str(case):
<b>····</b>plateau[case - 1] = "X"
else:
<b>····</b>print("Coup impossible.")</div>
<div class="cle">Trois questions, <b>un seul</b> <span class="mono">if</span>, <b>un seul</b> niveau de
décalage. Le <span class="mono">if</span> dans le <span class="mono">if</span> a disparu.</div>

<h2>3 · Ce que chaque morceau vérifie</h2>
<table>
  <tr><th style="width:38%">Le morceau</th><th>La question qu'il pose</th></tr>
  <tr><td class="mono">case &gt;= 1</td><td>la case n'est pas 0 ou négative — <b>c'est le bug réparé</b></td></tr>
  <tr><td class="mono">case &lt;= 9</td><td>la case n'est pas 12, ni 50</td></tr>
  <tr><td class="mono">plateau[case-1] == str(case)</td><td>la case est encore libre</td></tr>
</table>
<div class="cle" style="margin-top:1.4mm">Les trois sont reliées par <b>and</b> : il faut que
<b>les trois</b> soient vraies pour que le coup passe.</div>""",
      erreurs=[("SyntaxError", u"<span class='mono'>and</span> oublié entre deux conditions", u"Relis ta ligne à voix haute : est-ce que ça se dit ?"),
               ("NameError", u"<span class='mono'>AND</span> ou <span class='mono'>ET</span>", u"En minuscules, et en anglais : <span class='mono'>and</span>, <span class='mono'>or</span>"),
               (u"<i>tout est refusé</i>", u"<span class='mono'>&gt;=</span> et <span class='mono'>&lt;=</span> inversés", u"Tu demandes une case plus petite que 1 ?"),
               (u"<i>le 0 repasse</i>", u"Le <span class='mono'>case &gt;= 1</span> manque", u"Trois questions, pas deux")]),

 dict(dossier="S10-la-boucle", num=10, date="samedi 14 novembre 2026",
      titre="LE JEU TOURNE TOUT SEUL", emoji="🔄",
      nouveau=[u'garder neuf cases dans une liste, poser, et refuser un coup impossible',
               u'<b>jouer neuf tours tout seul</b>, les joueurs à tour de rôle'],
      corps=u"""
<h2>1 · La boucle : TANT QUE</h2>
<div class="code">tour = 0                       <i>← la boîte existe AVANT la boucle</i>
while tour &lt; 9:
<b>····</b>print("Un tour de plus")
<b>····</b>tour = tour + 1            <i>← SANS CETTE LIGNE, ça ne s'arrête jamais</i></div>
<div class="cle">Le <span class="mono">while</span> pose sa question <b>avant chaque tour</b>.
Tant que la réponse est <b>True</b>, il refait le bloc décalé.</div>

<h2 class="o">2 · Le geste qui sauve</h2>
<div class="cle" style="background:#fdeaea;border-color:#c0392b"><b>Ctrl + C</b> dans la zone du bas
= <b>arrêter un programme devenu fou</b>. Essaie-le une fois pour de vrai, maintenant.</div>

<h2 class="p">3 · Les joueurs alternent</h2>
<div class="code">if symbole == "X":
<b>····</b>symbole = "O"
<b>····</b>joueur = joueur2
else:
<b>····</b>symbole = "X"
<b>····</b>joueur = joueur1</div>
<div style="font-size:8.6pt">C'est l'idée du compteur : on <b>regarde</b> ce qu'il y a dans la boîte,
et on y <b>remet autre chose</b>. Les deux lignes vont <b>ensemble</b>, dans le même <span class="mono">if</span>.</div>

<h2>4 · Dedans ou dehors ?</h2>
<table>
  <tr><th style="width:46%">Ce qui est DANS la boucle (décalé)</th><th>Ce qui est DEHORS (collé à gauche)</th></tr>
  <tr><td>l'affichage du plateau, la question au joueur, la pose, le compteur, l'alternance</td>
      <td>les trois boîtes de départ, et l'affichage final</td></tr>
</table>
<div class="cle" style="margin-top:1.4mm">Un coup <b>refusé</b> ne doit <b>pas</b> faire avancer
<span class="mono">tour</span> : cette ligne est <b>dans</b> le <span class="mono">if</span> du coup valide.</div>""",
      erreurs=[(u"<i>ça ne s'arrête plus</i>", u"<span class='mono'>tour = tour + 1</span> oublié", u"<b>Ctrl + C</b>, puis ajoute la ligne qui fait avancer"),
               ("IndentationError", u"Le bloc de la boucle est mal décalé", u"Tout ce qui se répète est décalé de 4 espaces"),
               (u"<i>une seule question</i>", u"Le bloc n'est pas <b>dans</b> la boucle", u"Regarde où s'arrête le décalage"),
               (u"<i>toujours des X</i>", u"L'alternance est oubliée, ou hors du <span class='mono'>if</span>", u"Qui joue le 2ᵉ tour, dans ton code ?")]),

 dict(dossier="S11-le-gagnant", num=11, date="samedi 21 novembre 2026",
      titre="LE JEU SAIT QUI GAGNE", emoji="🏆",
      nouveau=[u'garder neuf cases dans une liste, poser, refuser, et jouer neuf tours',
               u'<b>reconnaître une victoire, annoncer le gagnant et s\'arrêter</b>'],
      corps=u"""
<h2>1 · La grille, en indices</h2>
<div class="duo">
  <div><b class="t">Les numéros de la grille</b>
    <div class="code" style="font-size:9.4pt"> 0 | 1 | 2
---+---+---
 3 | 4 | 5
---+---+---
 6 | 7 | 8</div></div>
  <div><b class="t">Les 8 façons de gagner</b>
    <div style="font-size:8.8pt;line-height:1.5">
    <b>3 lignes :</b> 0-1-2 · 3-4-5 · 6-7-8<br>
    <b>3 colonnes :</b> 0-3-6 · 1-4-7 · 2-5-8<br>
    <b>2 diagonales :</b> 0-4-8 · 2-4-6</div></div>
</div>

<h2 class="p">2 · LE BLOC À RECOPIER — les huit lignes gagnantes</h2>
<div class="code" style="font-size:8.6pt">if plateau[0] == plateau[1] and plateau[1] == plateau[2]:
<b>····</b>gagnant = plateau[0]
if plateau[3] == plateau[4] and plateau[4] == plateau[5]:
<b>····</b>gagnant = plateau[3]
if plateau[6] == plateau[7] and plateau[7] == plateau[8]:
<b>····</b>gagnant = plateau[6]
if plateau[0] == plateau[3] and plateau[3] == plateau[6]:
<b>····</b>gagnant = plateau[0]
if plateau[1] == plateau[4] and plateau[4] == plateau[7]:
<b>····</b>gagnant = plateau[1]
if plateau[2] == plateau[5] and plateau[5] == plateau[8]:
<b>····</b>gagnant = plateau[2]
if plateau[0] == plateau[4] and plateau[4] == plateau[8]:
<b>····</b>gagnant = plateau[0]
if plateau[2] == plateau[4] and plateau[4] == plateau[6]:
<b>····</b>gagnant = plateau[2]</div>
<div class="cle">Ce bloc se place <b>dans</b> la boucle, <b>juste après la pose</b> du symbole.</div>

<h2>3 · La boucle qui s'arrête</h2>
<div class="code">gagnant = ""                              <i>← AVANT la boucle, une seule fois</i>
while tour &lt; 9 and gagnant == "":</div>
<div style="font-size:8.6pt"><b>Deux</b> raisons d'arrêter : le plateau est plein, <b>ou</b> quelqu'un a
gagné. Et <b>pourquoi une case libre ne déclenche rien :</b> elle contient son numéro, et
<span class="mono">"1"</span>, <span class="mono">"2"</span>, <span class="mono">"3"</span> ne seront
jamais égaux.</div>""",
      erreurs=[(u"<i>ça ne s'arrête pas</i>", u"<span class='mono'>gagnant = \"\"</span> est <b>dans</b> la boucle", u"La boîte se crée une seule fois, avant"),
               (u"<i>le gagnant s'appelle « 5 »</i>", u"Le bloc des 8 <span class='mono'>if</span> est <b>avant</b> la pose", u"On teste <b>après</b> avoir joué"),
               (u"<i>toujours match nul</i>", u"Le bloc est <b>après</b> la boucle", u"Il doit être dedans, à chaque coup"),
               ("IndentationError", u"Les 8 <span class='mono'>if</span> mal décalés", u"Ils sont dans le <span class='mono'>if</span> du coup valide")]),
]

for s in SEANCES:
    acquis = ACQUIS_BASE + s["nouveau"]
    liste = u" &nbsp;·&nbsp; ".join(u'<span class="ok">✔</span> ' + a for a in acquis)
    page = GABARIT.format(titre=s["titre"], emoji=s["emoji"], num=s["num"], date=s["date"],
                          corps=s["corps"],
                          erreurs=u"\n  ".join(ligne_err(*e) for e in s["erreurs"]),
                          acquis=u"<b>Depuis le premier samedi, tu sais :</b><br>" + liste)
    dossier = os.path.join(BASE, s["dossier"], "a-imprimer")
    src = os.path.join(dossier, "sources", "1-aide-memoire.html")
    io.open(src, "w", encoding="utf-8").write(page)
    pdf = os.path.join(dossier, "1-aide-memoire.pdf")
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", "--print-to-pdf=" + pdf, src],
                   capture_output=True)
    import pymupdf
    d = pymupdf.open(pdf)
    taux = 100 * max(x[3] for x in d[0].get_text("blocks")) / d[0].rect.height
    print("S%02d  %-12s  %d page(s)  %3.0f%%" % (s["num"], s["dossier"][:12], len(d), taux))
