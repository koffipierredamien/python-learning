# -*- coding: utf-8 -*-
"""La feuille « La Medaille » : trois questions de reflexion, puis un
   programme a ecrire SANS AUCUNE CONSIGNE DE CODE.

   REGLES DE CETTE FEUILLE :
   - elle n'est pas imprimee : elle part en image, on la lit sur un
     telephone. On ne demande donc JAMAIS d'ecrire dessus, et il n'y a
     aucun cadre a remplir ;
   - aucune date, aucune heure, aucun numero de seance, aucune duree ;
   - l'enonce du programme ne dit pas comment coder : il donne le
     bareme, l'ecran attendu et les essais a reussir. Trouver l'ordre
     des questions EST l'exercice.

   HTML autonome -> PDF (chromium) -> PNG (poppler).
"""
import os, subprocess

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME = "/opt/pw-browsers/chromium"
DOSSIER = os.path.join(BASE, "S11-les-trois-chemins", "a-envoyer")
NOM = "exercice-la-medaille"

PAGE = u"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>La Médaille</title>
<style>
 html,*{-webkit-print-color-adjust:exact;print-color-adjust:exact;box-sizing:border-box}
 @page{size:A4 portrait;margin:0}
 body{margin:0;padding:7mm 8mm;font-family:"Trebuchet MS",Verdana,sans-serif;
      font-size:10.4pt;color:#14142b;background:#fff;line-height:1.4}
 .saut{page-break-before:always}
 .mono{font-family:"Courier New",monospace;font-weight:bold;background:#f0f0f6;
       padding:.3mm 1mm;border-radius:1mm}

 .band{background:#12122a;color:#fff;border-radius:3mm;padding:3.4mm 5mm;margin-bottom:3.2mm}
 .band h1{font-size:21pt;margin:0 0 1.4mm}
 .band .s{font-size:10.4pt;color:#b8b8d0;line-height:1.42}

 h2{font-size:11.6pt;background:#6b2d8f;color:#fff;padding:1.4mm 4mm;margin:0 0 2.6mm;
    border-radius:2mm}
 h2.v{background:#2e9e52}

 .q{border:.5mm solid #14142b;border-radius:2.6mm;margin-bottom:2.8mm;overflow:hidden;
    page-break-inside:avoid}
 .q .h{background:#14142b;color:#fff;padding:1.2mm 3.4mm;font-size:10.6pt;font-weight:bold;
       display:flex;gap:2.8mm;align-items:center}
 .q .h .n{background:#ffb74d;color:#14142b;border-radius:50%;width:6.2mm;height:6.2mm;
          line-height:6.2mm;text-align:center;font-size:10.4pt;display:inline-block}
 .q .c{padding:2.2mm 3.4mm}
 .q .c p{margin:0 0 1.4mm}
 .q .c p:last-child{margin-bottom:0}

 .code{font-family:"Courier New",monospace;font-size:9.4pt;background:#12122a;color:#4fc3f7;
       padding:2mm 3mm;border-radius:1.8mm;white-space:pre;line-height:1.34;margin:1.4mm 0}
 .code i{color:#ffb74d;font-style:normal}
 .duo{display:flex;gap:3mm}
 .duo > div{flex:1}
 .duo .t{font-weight:bold;font-size:9.8pt;margin-bottom:.6mm}

 .demande{color:#6b2d8f;font-weight:bold}

 .ctx{background:#f3f3f8;border-left:3mm solid #6b2d8f;border-radius:2mm;
      padding:2.4mm 3.4mm;margin-bottom:2.8mm}
 .row{display:flex;gap:3mm;margin-bottom:2.8mm}
 .bareme{flex:1.05;border:.6mm solid #d79a00;border-radius:2.6mm;overflow:hidden;background:#fffaf0}
 .bareme .t{background:#d79a00;color:#fff;font-weight:bold;padding:1.2mm 3mm;font-size:10pt}
 .bareme table{width:100%;border-collapse:collapse;font-size:9.6pt}
 .bareme td{padding:1.1mm 3mm;border-bottom:.2mm solid #e8d6a8}
 .bareme tr:last-child td{border-bottom:0}
 .bareme td.n{font-family:"Courier New",monospace;font-weight:bold;white-space:nowrap;width:33%}
 .ecran{flex:1;border:.6mm solid #2fb765;border-radius:2.6mm;overflow:hidden}
 .ecran .t{background:#2fb765;color:#fff;font-weight:bold;padding:1.2mm 3mm;font-size:10pt}
 .ecran pre{margin:0;padding:2.2mm 3mm;font-family:"Courier New",monospace;font-size:8.4pt;
            line-height:1.34;background:#f2faf5;white-space:pre}
 .ecran b{color:#0c5c29}

 .essais{border:.5mm solid #14142b;border-radius:2.6mm;overflow:hidden;margin-bottom:2.8mm}
 .essais .t{background:#14142b;color:#fff;font-weight:bold;padding:1.2mm 3.4mm;font-size:10.4pt}
 .essais table{width:100%;border-collapse:collapse;font-size:9.8pt}
 .essais td{padding:1.1mm 3.4mm;border-bottom:.2mm solid #ddd}
 .essais tr:last-child td{border-bottom:0}
 .essais td.n{font-family:"Courier New",monospace;font-weight:bold;width:17%;text-align:right}
 .essais td.f{width:6%;text-align:center}

 .fin{background:#fffaf0;border:.6mm solid #d79a00;border-radius:2.6mm;padding:2.4mm 3.4mm;
      font-size:10pt}
 .fin b{color:#a65d00}
</style></head><body>

<div class="band">
  <h1>&#127941; LA MÉDAILLE</h1>
  <div class="s">Trois questions qui se répondent dans ta tête, puis un programme à écrire
    tout seul. <b>Personne ne va te dire quoi taper</b> : on te dit seulement ce que le
    programme doit faire.</div>
</div>

<h2>D'abord, trois questions. Réponds dans ta tête.</h2>

<div class="q"><div class="h"><span class="n">1</span> Il a tout juste, et il reçoit du bronze</div>
<div class="c">
<div class="code">note = 95

if note &gt;= 60:
    print("Bronze")
elif note &gt;= 90:
    print("Or")</div>
<p><span class="demande">Qu'est-ce qui s'affiche ?</span> Et surtout : <b>pourquoi ?</b></p>
<p><span class="demande">Répare-le</span> — sans ajouter, sans enlever et sans changer une seule
ligne. Tu n'as le droit que de les <b>déplacer</b>.</p>
</div></div>

<div class="q"><div class="h"><span class="n">2</span> Le programme qui ne répond rien</div>
<div class="c">
<div class="code">note = 30

if note &gt;= 90:
    print("Or")
elif note &gt;= 60:
    print("Recu")</div>
<p>Cette fois l'ordre est bon. Pourtant, avec 30, <b>l'écran reste vide</b>.</p>
<p><span class="demande">Pourquoi ?</span> Et <span class="demande">qu'est-ce qui manque</span>
pour qu'il y ait <b>toujours</b> une réponse, quel que soit le nombre ?</p>
</div></div>

<div class="q"><div class="h"><span class="n">3</span> Un if dans un if</div>
<div class="c">
<div class="code">if reponse == "oui":
    print("D'accord")
else:
    if reponse == "non":
        print("Tant pis")
    else:
        print("Je n'ai pas compris")</div>
<p><span class="demande">Récris-le avec <span class="mono">elif</span>.</span> Il doit répondre
exactement la même chose aux trois réponses possibles — mais tenir sur <b>un seul niveau de
décalage</b> au lieu de deux.</p>
<p>Recopie les deux versions dans Thonny et essaie <span class="mono">"oui"</span>,
<span class="mono">"non"</span>, puis <span class="mono">"peut-etre"</span>. Les deux doivent
donner le même résultat les trois fois.</p>
</div></div>

<div class="saut"></div>

<h2 class="v">Maintenant, le programme : LA MÉDAILLE</h2>

<div class="ctx">À la fin du <b>concours de calcul mental du quartier</b>, l'arbitre annonce à
chaque enfant ce qu'il a gagné, selon ses points sur 100. Il le fait de tête, et il se trompe.
<b>Écris le programme qui le fera à sa place.</b><br>
Il demande les points, puis il annonce <b>une seule</b> récompense.</div>

<div class="row">
  <div class="bareme"><div class="t">&#127942; CE QUE L'ARBITRE ANNONCE</div>
    <table>
      <tr><td class="n">exactement 100</td><td>SANS FAUTE ! Tu es en finale.</td></tr>
      <tr><td class="n">90 à 99</td><td>Medaille d'OR</td></tr>
      <tr><td class="n">75 à 89</td><td>Medaille d'ARGENT</td></tr>
      <tr><td class="n">60 à 74</td><td>Medaille de BRONZE</td></tr>
      <tr><td class="n">moins de 60</td><td>Participant. Reviens l'annee prochaine !</td></tr>
      <tr><td class="n">impossible</td><td>Ce nombre n'existe pas.</td></tr>
    </table></div>
  <div class="ecran"><div class="t">&#9989; CE QUE ÇA DONNE À L'ÉCRAN</div>
<pre>========================================
        LE CONCOURS DU QUARTIER
========================================

Combien de points sur 100 ? <b>100</b>

SANS FAUTE ! Tu es en finale.

========================================</pre></div>
</div>

<div class="essais"><div class="t">&#127919; LES SIX ESSAIS QUI DOIVENT TOMBER JUSTE</div>
<table>
  <tr><td class="n">100</td><td class="f">&rarr;</td><td>SANS FAUTE ! Tu es en finale.</td></tr>
  <tr><td class="n">90</td><td class="f">&rarr;</td><td>Medaille d'OR</td></tr>
  <tr><td class="n">74</td><td class="f">&rarr;</td><td>Medaille de BRONZE</td></tr>
  <tr><td class="n">59</td><td class="f">&rarr;</td><td>Participant. Reviens l'annee prochaine !</td></tr>
  <tr><td class="n">0</td><td class="f">&rarr;</td><td>Participant. Reviens l'annee prochaine !</td></tr>
  <tr><td class="n">120</td><td class="f">&rarr;</td><td>Ce nombre n'existe pas.</td></tr>
</table></div>

<div class="fin">
<b>Aucune consigne de code ne te sera donnée.</b> Tout l'exercice tient dans une seule
question : <b>dans quel ordre poser les questions ?</b> Deux des six essais ci-dessus piègent
presque tout le monde — à toi de voir lesquels.<br><br>
<b>L'algorithme d'abord.</b> Écris en français, une ligne par cas, ce que le programme doit
faire — dans ton cahier, ou directement dans Thonny en commençant chaque ligne par un
<span class="mono">#</span>. Le code vient après, sous chaque ligne de français.<br><br>
Dans Thonny : <b>Fichier &rarr; Nouveau &rarr; Enregistrer sous</b>
<span class="mono">medaille_tonprenom.py</span>. Quand les six essais tombent juste,
<b>envoie une photo de ton écran</b>.
</div>

</body></html>
"""

CORRIGE = u"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>Correction — La Médaille</title>
<style>
 html,*{-webkit-print-color-adjust:exact;print-color-adjust:exact;box-sizing:border-box}
 @page{size:A4 portrait;margin:0}
 body{margin:0;padding:7mm 8mm;font-family:"Trebuchet MS",Verdana,sans-serif;
      font-size:9.2pt;color:#14142b;background:#fff;line-height:1.33}
 .m{font-family:"Courier New",monospace;font-weight:bold;background:#f0f0f6;
    padding:.3mm 1mm;border-radius:1mm}
 .band{background:#0c5c29;color:#fff;border-radius:3mm;padding:3.2mm 5mm;margin-bottom:3mm}
 .band .k{font-size:8.6pt;letter-spacing:1.2pt;color:#a8e6bd;font-weight:bold}
 .band h1{font-size:19pt;margin:.8mm 0 1mm}
 .band .s{font-size:9.8pt;color:#d8f0e2;line-height:1.4}
 pre{margin:0 0 2.6mm;background:#12122a;color:#e8e8f2;border-radius:2.6mm;padding:2.8mm 3.6mm;
     font-family:"Courier New",monospace;font-size:7.7pt;line-height:1.28;white-space:pre}
 pre .c{color:#7f7f9c} pre .s{color:#ffb74d} pre .k{color:#4fc3f7;font-weight:bold}
 .note{background:#fffaf0;border:.6mm solid #d79a00;border-radius:2.6mm;padding:2.2mm 3mm;
       margin-bottom:2.4mm;line-height:1.38}
 .note h3{margin:0 0 1.1mm;font-size:10.2pt;color:#a65d00}
 .note b{color:#a65d00}
 .note ul{margin:1mm 0 0;padding-left:5mm}.note li{margin-bottom:.9mm}
 table{width:100%;border-collapse:collapse;margin:1mm 0 0;font-size:8.8pt}
 td,th{border:.2mm solid #999;padding:.9mm 2mm;text-align:left}
 th{background:#eee;font-size:8.8pt}
 td.n{font-family:"Courier New",monospace;font-weight:bold;width:14%;text-align:right}
 .vert{background:#f2faf5;border:.6mm solid #2fb765;border-radius:2.6mm;padding:2.2mm 3mm}
 .serre{font-size:8.6pt;line-height:1.3}
 .vert h3{margin:0 0 1.1mm;font-size:10.2pt;color:#0c5c29}
</style></head><body>

<div class="band">
  <div class="k">CORRECTION · POUR L'ENSEIGNANT ET LES PARENTS — NE PAS DONNER AUX ÉLÈVES</div>
  <h1>&#9989; LA MÉDAILLE</h1>
  <div class="s">L'énoncé ne donne <b>aucune consigne de code</b> : il donne un barème et six essais.
    <b>Tout l'exercice est de trouver dans quel ordre poser les questions.</b> Les messages peuvent
    varier : ce qui compte, c'est que les six essais tombent juste.</div>
</div>

<pre><span class="k">print</span>(<span class="s">"="</span> * 40)
<span class="k">print</span>(<span class="s">"        LE CONCOURS DU QUARTIER"</span>)
<span class="k">print</span>(<span class="s">"="</span> * 40)
<span class="k">print</span>(<span class="s">""</span>)

points = <span class="k">input</span>(<span class="s">"Combien de points sur 100 ? "</span>)
points = <span class="k">int</span>(points)

<span class="k">print</span>(<span class="s">""</span>)
<span class="k">if</span> points &lt; 0 <span class="k">or</span> points &gt; 100:
    <span class="k">print</span>(<span class="s">"Ce nombre n'existe pas."</span>)
<span class="c"># le cas le PLUS PRECIS d'abord : un seul nombre le satisfait</span>
<span class="k">elif</span> points == 100:
    <span class="k">print</span>(<span class="s">"SANS FAUTE ! Tu es en finale."</span>)
<span class="k">elif</span> points &gt;= 90:
    <span class="k">print</span>(<span class="s">"Medaille d'OR"</span>)
<span class="k">elif</span> points &gt;= 75:
    <span class="k">print</span>(<span class="s">"Medaille d'ARGENT"</span>)
<span class="k">elif</span> points &gt;= 60:
    <span class="k">print</span>(<span class="s">"Medaille de BRONZE"</span>)
<span class="k">else</span>:
    <span class="k">print</span>(<span class="s">"Participant. Reviens l'annee prochaine !"</span>)

<span class="k">print</span>(<span class="s">""</span>)
<span class="k">print</span>(<span class="s">"="</span> * 40)</pre>

<div class="note"><h3>&#9888; Les deux pièges — à faire vivre, surtout pas à expliquer</h3>
<b>1. Le 100.</b> Écrit <b>après</b> le <span class="m">&gt;= 90</span>, le cas
<span class="m">== 100</span> n'est <b>jamais atteint</b> : 100 est déjà plus grand que 90, et Python
s'arrête au premier chemin qui passe. L'enfant reçoit une médaille d'or au lieu d'aller en finale,
<b>et aucune erreur rouge ne s'affiche</b>.<br>
<b>2. Le 0.</b> Qui écrit <span class="m">points &lt;= 0</span> pour l'impossible refuse le zéro.
Or <b>on peut avoir zéro point sans tricher</b> : il fallait <span class="m">points &lt; 0</span>.<br>
<b>Ne corrigez pas la ligne fautive</b> : faites taper <b>100</b>, puis <b>0</b>, et faites lire
l'écran à voix haute. Ils trouvent seuls, et ils ne l'oublient plus.</div>

<table>
  <tr><th colspan="2">&#127919; Les six essais</th><th>Ce qui doit s'afficher</th></tr>
  <tr><td class="n">100</td><td>&rarr;</td><td>SANS FAUTE ! Tu es en finale. &nbsp; <b>— le piège</b></td></tr>
  <tr><td class="n">90</td><td>&rarr;</td><td>Medaille d'OR</td></tr>
  <tr><td class="n">74</td><td>&rarr;</td><td>Medaille de BRONZE</td></tr>
  <tr><td class="n">59</td><td>&rarr;</td><td>Participant. Reviens l'annee prochaine !</td></tr>
  <tr><td class="n">0</td><td>&rarr;</td><td>Participant. Reviens l'annee prochaine ! &nbsp; <b>— le second piège</b></td></tr>
  <tr><td class="n">120</td><td>&rarr;</td><td>Ce nombre n'existe pas.</td></tr>
</table>

<div style="height:1.8mm"></div>

<div class="vert"><h3>&#9989; Les trois réponses des questions de réflexion</h3>
<b>1.</b> Il s'affiche <b>Bronze</b>. 95 est déjà plus grand que 60 : le premier chemin passe, et
celui du 90 n'est jamais regardé. On répare en <b>échangeant les deux blocs</b> — rien d'autre.<br>
<b>2.</b> Avec 30, <b>aucune</b> des deux conditions n'est vraie, et il n'y a <b>pas de
<span class="m">else</span></b> : l'écran reste vide. Il manque le <span class="m">else</span>, qui
n'a pas de condition et attrape tout le reste.<br>
<b>3.</b> <span class="m">if reponse == "oui": … elif reponse == "non": … else: …</span> — même
comportement aux trois réponses, et surtout <b>un seul niveau de décalage</b> au lieu de deux.</div>

<div style="height:1.8mm"></div>

<div class="note serre" style="border-color:#2fb765;background:#f2faf5">
<h3 style="color:#0c5c29">Ce qu'on regarde en corrigeant</h3>
<b>L'algorithme en français existe-t-il, avant le code ?</b> C'est le premier livrable. &nbsp;·&nbsp;
Le <span class="m">int()</span> est-il là ? &nbsp;·&nbsp; Y a-t-il <b>un seul</b>
<span class="m">if</span>, puis des <span class="m">elif</span>, puis un
<span class="m">else</span> ? &nbsp;·&nbsp; Le test de l'impossible est-il <b>en premier</b> ?
&nbsp;·&nbsp; <b>On note la preuve, pas la perfection.</b></div>

</body></html>
"""


def construire(nom, page):
    os.makedirs(os.path.join(DOSSIER, "sources"), exist_ok=True)
    src = os.path.join(DOSSIER, "sources", nom + ".html")
    open(src, "w", encoding="utf-8").write(page)

    pdf = os.path.join(DOSSIER, nom + ".pdf")
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", "--print-to-pdf=" + pdf, "file://" + src],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    info = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    pages = int([l for l in info.splitlines() if l.startswith("Pages:")][0].split()[1])
    subprocess.run(["pdftoppm", "-png", "-r", "150", pdf, os.path.join(DOSSIER, nom)], check=True)
    for i in range(1, pages + 1):
        brut = os.path.join(DOSSIER, "%s-%0*d.png" % (nom, len(str(pages)), i))
        voulu = os.path.join(DOSSIER, "%s-%d.png" % (nom, i))
        if brut != voulu and os.path.exists(brut):
            os.replace(brut, voulu)

    bbox = subprocess.run(["pdftotext", "-bbox", pdf, "-"], capture_output=True, text=True).stdout
    taux = []
    for bloc in bbox.split("<page ")[1:]:
        h = float(bloc.split('height="')[1].split('"')[0])
        ys = [float(x.split('"')[0]) for x in bloc.split('yMax="')[1:]]
        taux.append(round(100 * max(ys) / h) if ys else 0)
    print("%-24s %d page(s)  remplissage %s" % (nom, pages, taux))


construire(NOM, PAGE)
construire("correction-la-medaille", CORRIGE)
