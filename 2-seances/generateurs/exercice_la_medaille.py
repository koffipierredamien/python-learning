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

os.makedirs(os.path.join(DOSSIER, "sources"), exist_ok=True)
src = os.path.join(DOSSIER, "sources", NOM + ".html")
open(src, "w", encoding="utf-8").write(PAGE)

pdf = os.path.join(DOSSIER, NOM + ".pdf")
subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                "--no-pdf-header-footer", "--print-to-pdf=" + pdf, "file://" + src],
               check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

info = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
pages = int([l for l in info.splitlines() if l.startswith("Pages:")][0].split()[1])
subprocess.run(["pdftoppm", "-png", "-r", "150", pdf, os.path.join(DOSSIER, NOM)], check=True)
for i in range(1, pages + 1):
    brut = os.path.join(DOSSIER, "%s-%0*d.png" % (NOM, len(str(pages)), i))
    voulu = os.path.join(DOSSIER, "%s-%d.png" % (NOM, i))
    if brut != voulu and os.path.exists(brut):
        os.replace(brut, voulu)

bbox = subprocess.run(["pdftotext", "-bbox", pdf, "-"], capture_output=True, text=True).stdout
taux = []
for bloc in bbox.split("<page ")[1:]:
    h = float(bloc.split('height="')[1].split('"')[0])
    ys = [float(x.split('"')[0]) for x in bloc.split('yMax="')[1:]]
    taux.append(round(100 * max(ys) / h) if ys else 0)
print("%s  %d page(s)  remplissage %s" % (NOM, pages, taux))
