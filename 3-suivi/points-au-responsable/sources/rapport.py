# -*- coding: utf-8 -*-
"""Point d'assiduite et de devoirs pour le responsable — HTML (puis PDF) + Word."""
import io, os

BASE = "/home/user/python-learning/3-suivi/points-au-responsable"

# ---------------------------------------------------------------- les donnees
# presence : P present · R retard · E absence excusee · A absence non excusee
# devoirs  : 'ok' rendu · 'non' pas rendu · '?' a confirmer
JERUSALEM = [
 ("Gédéon OKITONGA",               "PPP", ("ok","10"), ("ok","12"), ("non","")),
 ("Lohiss LOUA",                   "PPP", ("ok","15"), ("ok","15"), ("ok","")),
 ("Yanis AMESSAN",                 "PPR", ("ok","9"),  ("ok","15"), ("ok","")),
 ("Ephraïm Christ-Emmanuel AMON",  "PER", ("non",""),  ("non",""),  ("non","")),
 ("Joyce Bouam LALLE",             "PPP", ("ok","15"), ("ok","12"), ("ok","")),
 ("Grâce-Elsa DREESEN",            "PRP", ("ok","10"), ("ok","11"), ("non","")),
 ("Caleb DOGBRE",                  "ERA", ("ok","9"),  ("non",""),  ("non","")),
 ("Joseph Daniel NGAPELA",         "EPR", ("non",""),  ("non",""),  ("non","")),
 ("Els MOADJIDIBAYE",              "PPR", ("ok","7"),  ("ok","13"), ("non","")),
]
JEREMIAH = [
 ("Acquilas MBIERE",               "RRR", ("non",""),  ("ok","9"),  ("ok","4")),
 ("Bénicia Chryti Léa MBIERE",     "RRR", ("non",""),  ("ok","9"),  ("ok","7")),
 ("Viesainte MBIERE",              "RRR", ("non",""),  ("ok","10"), ("ok","8")),
 ("Isaac YEDOH LOHOUESS",          "PRR", ("non",""),  ("ok","8"),  ("ok","4")),
 ("Sarah LOUA",                    "PPP", ("ok","11"), ("ok","12"), ("non","")),
 ("Joshua DOGBRE",                 "ERA", ("?",""),    ("non",""),  ("non","")),
 ("Ethan SORO",                    "PAA", ("non",""),  ("non",""),  ("non","")),
 ("Eunice SORO",                   "PAA", ("non",""),  ("non",""),  ("non","")),
]

def compte(p):
    return p.count("R"), p.count("A"), p.count("E")

def totaux(groupes):
    r = a = e = 0; d = [0, 0, 0]
    n = 0
    for g in groupes:
        for el in g:
            n += 1
            rr, aa, ee = compte(el[1]); r += rr; a += aa; e += ee
            for i in range(3):
                if el[2+i][0] == "ok": d[i] += 1
    return n, r, a, e, d

N, RET, ABS, EXC, DEV = totaux([JERUSALEM, JEREMIAH])

# ---------------------------------------------------------------- HTML
PAST = {"P": ("P", "#2e9e52", "#e9f7ee"), "R": ("R", "#c97a00", "#fff4de"),
        "E": ("E", "#5a5a72", "#eeeef4"), "A": ("A", "#c0392b", "#fdeaea")}

def pastilles(p):
    return "".join('<span class="pz" style="color:%s;background:%s">%s</span>' % (c, f, t)
                   for t, c, f in (PAST[x] for x in p))

def dev(cell, note_unite="", non_echu=False):
    etat, note = cell
    if etat == "ok":
        n = ('<i>%s%s</i>' % (note, note_unite)) if note else ""
        return '<td class="ok">✔ <b>rendu</b> %s</td>' % n
    if etat == "?":
        return '<td class="dt">? à confirmer</td>'
    if non_echu:
        return '<td class="att">— en attente</td>'
    return '<td class="ko">✘ non rendu</td>'

def lignes(groupe, unites):
    out = []
    for nom, pres, d1, d2, d3 in groupe:
        r, a, e = compte(pres)
        rendus = sum(1 for x in (d1, d2) if x[0] == "ok")
        cls = ' class="alerte"' if (a >= 2 or rendus == 0) else ""
        out.append(
            "<tr%s><td class='nom'>%s</td><td class='pres'>%s</td>"
            "<td class='n %s'>%s</td><td class='n %s'>%s</td>"
            "%s%s%s<td class='n b'>%d / 2</td></tr>" % (
             cls, nom, pastilles(pres),
             "warn" if r else "", r or "—",
             "bad" if a else "", a or "—",
             dev(d1, unites[0]), dev(d2, unites[1]), dev(d3, unites[2], True), rendus))
    return "\n".join(out)

HTML = u"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>Point d'assiduité et de devoirs</title>
<style>
  html,*{-webkit-print-color-adjust:exact;print-color-adjust:exact;box-sizing:border-box}
  @page{size:A4 portrait;margin:11mm 11mm 10mm}
  body{margin:0;font-family:"Trebuchet MS",Verdana,sans-serif;font-size:9.1pt;color:#14142b}
  .ent{border-bottom:1.1mm solid #1a1a2e;padding-bottom:2mm;margin-bottom:3.4mm}
  .sur{font-size:8.2pt;letter-spacing:.9pt;color:#6b2d8f;font-weight:bold}
  h1{font-size:19pt;margin:1.2mm 0 1mm}
  .dest{font-size:9.2pt;color:#444}
  .dest b{color:#14142b}
  .tiles{display:flex;gap:2.4mm;margin-bottom:3.6mm}
  .ti{flex:1;border:.4mm solid #d8d8e4;border-radius:2mm;padding:2.2mm 2.4mm;background:#fafaff}
  .ti .k{font-size:21pt;font-weight:bold;line-height:1}
  .ti .l{font-size:7.6pt;color:#555;margin-top:.8mm;line-height:1.25}
  h2{font-size:11pt;margin:4mm 0 1.6mm;padding:1.2mm 3mm;background:#1a1a2e;color:#fff;border-radius:1.5mm}
  h2 span{font-weight:normal;opacity:.75;font-size:9pt}
  h3{font-size:10pt;margin:3.4mm 0 1.4mm;color:#6b2d8f}
  table{width:100%;border-collapse:collapse}
  th,td{border:.25mm solid #b9b9c9;padding:1.1mm 1.4mm;font-size:8.2pt;vertical-align:middle}
  th{background:#ecebf3;font-size:7.6pt;text-align:center;line-height:1.2}
  th.l,td.nom{text-align:left}
  td.nom{font-weight:bold;font-size:8.4pt}
  td.n{text-align:center}
  td.b{font-weight:bold;background:#f6f6fb}
  .pres{text-align:center;white-space:nowrap}
  .pz{display:inline-block;width:4.6mm;height:4.6mm;line-height:4.6mm;text-align:center;
      border-radius:1mm;font-weight:bold;font-size:8pt;margin:0 .3mm}
  td.ok{color:#1d7a3e;font-size:7.8pt;text-align:center}
  td.ok i{color:#555;font-style:normal;font-size:7pt;white-space:nowrap}
  td.ko{color:#c0392b;font-size:7.8pt;text-align:center;background:#fdf4f4}
  td.att{color:#8a8aa0;font-size:7.8pt;text-align:center;background:#f7f7fb}
  td.dt{color:#c97a00;font-size:7.8pt;text-align:center;background:#fffaf0}
  td.warn{color:#c97a00;font-weight:bold}
  td.bad{color:#c0392b;font-weight:bold}
  tr.alerte td.nom{background:#fdf0f0}
  .leg{font-size:7.6pt;color:#555;margin-top:1.4mm}
  .leg b{color:#14142b}
  .enc{border:.5mm solid #d79a00;background:#fffaf0;border-radius:2mm;padding:2.4mm 3mm;margin:3mm 0}
  .enc .t{font-weight:bold;font-size:9.6pt;margin-bottom:1.2mm}
  ol,ul{margin:1mm 0 0;padding-left:5mm}
  li{margin-bottom:1.4mm;line-height:1.35}
  .pri{display:inline-block;background:#c0392b;color:#fff;border-radius:1mm;padding:0 1.4mm;
       font-size:7.4pt;font-weight:bold;margin-right:1mm}
  .pri.b{background:#c97a00}.pri.c{background:#5a5a72}
  .note{font-size:7.8pt;color:#555;border-top:.25mm solid #c9c9d6;padding-top:1.6mm;margin-top:3mm;line-height:1.4}
  .sig{margin-top:5mm;font-size:8.6pt;color:#333}
  .pb{page-break-before:always}
</style></head><body>

<div class="ent">
  <div class="sur">ACPROKIDS CODING CAMP · VISION PLÉNITUDES VIE</div>
  <h1>Point d'assiduité et de devoirs</h1>
  <div class="dest"><b>À l'attention du Pasteur Eli</b> &nbsp;·&nbsp; situation arrêtée le
    <b>vendredi 2 octobre 2026</b>, veille de la séance 4 &nbsp;·&nbsp;
    période couverte : <b>séances 1 à 3</b> (12, 19 et 26 septembre) et les <b>3 devoirs</b> envoyés les mercredis</div>
</div>

<div class="tiles">
  <div class="ti"><div class="k">{{N}}</div><div class="l">élèves inscrits<br>9 Jerusalem · 8 Jeremiah</div></div>
  <div class="ti"><div class="k" style="color:#c97a00">{{RET}}</div><div class="l">retards<br>sur 3 séances</div></div>
  <div class="ti"><div class="k" style="color:#c0392b">{{ABS}}</div><div class="l">absences<br>non excusées</div></div>
  <div class="ti"><div class="k" style="color:#5a5a72">{{EXC}}</div><div class="l">absences<br>excusées</div></div>
  <div class="ti"><div class="k">{{D1}}<span style="font-size:11pt">/17</span></div><div class="l">devoir 1 rendu<br>quiz d'introduction</div></div>
  <div class="ti"><div class="k">{{D2}}<span style="font-size:11pt">/17</span></div><div class="l">devoir 2 rendu<br>quiz de révision</div></div>
  <div class="ti" style="background:#fffaf0;border-color:#d79a00"><div class="k" style="color:#c97a00">{{D3}}<span style="font-size:11pt">/17</span></div><div class="l"><b>devoir 3 — en cours</b><br>échéance demain</div></div>
</div>

<h2>JERUSALEM GEEKS <span>— 9 à 12 ans · 9 élèves</span></h2>
<table>
  <tr><th class="l" style="width:24%">Élève</th><th style="width:16%">S01 · S02 · S03</th>
      <th style="width:7%">Retards</th><th style="width:7%">Absences</th>
      <th>Devoir 1<br>quiz d'introduction</th><th>Devoir 2<br>quiz de révision</th>
      <th>Devoir 3<br><i>échéance demain</i></th><th style="width:8%">Devoirs<br>exigibles</th></tr>
  {{TJ}}
</table>

<h2>JEREMIAH GEEKS <span>— 12 à 18 ans · 8 élèves</span></h2>
<table>
  <tr><th class="l" style="width:24%">Élève</th><th style="width:16%">S01 · S02 · S03</th>
      <th style="width:7%">Retards</th><th style="width:7%">Absences</th>
      <th>Devoir 1<br>quiz d'introduction</th><th>Devoir 2<br>révision séance 2</th>
      <th>Devoir 3<br><i>échéance demain</i></th><th style="width:8%">Devoirs<br>exigibles</th></tr>
  {{TM}}
</table>
<div class="leg"><b>Présence :</b>
  <span class="pz" style="color:#2e9e52;background:#e9f7ee">P</span> présent &nbsp;
  <span class="pz" style="color:#c97a00;background:#fff4de">R</span> en retard &nbsp;
  <span class="pz" style="color:#5a5a72;background:#eeeef4">E</span> absence excusée &nbsp;
  <span class="pz" style="color:#c0392b;background:#fdeaea">A</span> absence non excusée. &nbsp;
  <b>« Devoirs exigibles »</b> compte les devoirs 1 et 2 : <b>le devoir 3 n'est pas encore dû</b>, son échéance est la séance de demain.
  Les notes entre parenthèses sont celles calculées par le formulaire.</div>

<div class="enc">
  <div class="t">Ce que ces chiffres disent en une phrase</div>
  <b>L'assiduité n'est pas le problème : la ponctualité et les devoirs le sont.</b>
  Sur 17 élèves, 11 ont rendu le devoir 2 et 8 le devoir 1. Les retards sont presque tous concentrés
  sur deux familles, et les absences non excusées sur une seule.
</div>

<h2 class="pb">LES SITUATIONS À REGARDER <span>— par ordre d'urgence</span></h2>

<h3>1 · Ce qui demande une action cette semaine</h3>
<ol>
  <li><span class="pri">PRIORITÉ</span><b>Ethan SORO et Eunice SORO</b> — présents à la séance 1, puis
    <b>absents aux séances 2 et 3</b>, et aucun des devoirs rendu. Le règlement intérieur prévoit
    d'appeler la famille <b>dès la deuxième absence</b> : l'appel reste à faire. C'est le seul cas de
    décrochage réel à ce jour.</li>
  <li><span class="pri b">À SUIVRE</span><b>Joseph Daniel NGAPELA</b> et <b>Ephraïm AMON</b> — assidus
    (une absence excusée chacun), mais <b>aucun devoir rendu sur les deux</b> exigibles. Ce n'est pas un
    problème de présence : les formulaires n'arrivent probablement pas jusqu'aux parents, ou le téléphone
    n'est pas disponible. Un appel suffira à le savoir.</li>
  <li><span class="pri b">À SUIVRE</span><b>Caleb DOGBRE</b> et <b>Joshua DOGBRE</b> (même famille) —
    une absence excusée, un retard, puis <b>une absence non excusée à la séance 3</b>, et le devoir 2
    non rendu pour les deux. À relier à l'appel ci-dessus.</li>
</ol>

<h3>2 · Un problème d'horaire, pas de motivation</h3>
<ul>
  <li><b>Acquilas, Bénicia et Viesainte MBIERE</b> — <b>en retard aux trois séances</b>, soit 9 des
    {{RET}} retards à eux seuls. Mais <b>ils ont rendu le devoir 2 et le devoir 3</b>, tous les trois.
    Ces enfants travaillent : c'est l'arrivée à 12 h qui coince. Une question à poser à la famille
    (transport, trajet, horaire de départ) plutôt qu'un rappel à l'ordre.</li>
  <li><b>Isaac YEDOH LOHOUESS</b> — deux retards, mais devoirs 2 et 3 rendus. Même lecture.</li>
</ul>

<h3>3 · Ce qui fonctionne, et qu'il faut dire aux familles</h3>
<ul>
  <li><b>Lohiss LOUA, Yanis AMESSAN et Joyce Bouam LALLE</b> — assidus, et <b>les trois devoirs rendus</b>,
    avec les meilleures notes des deux classes. <b>Sarah LOUA</b> et <b>Gédéon OKITONGA</b> suivent de près.</li>
  <li><b>Aucune absence non excusée chez 13 élèves sur 17</b>, et la participation aux devoirs <b>monte</b> :
    8 au premier, 11 au deuxième.</li>
</ul>

<h3>4 · Discipline en classe</h3>
<ul>
  <li><b>Un seul fait inscrit au registre depuis le début</b> : séance 3 du 26 septembre,
    <b>Ephraïm AMON</b>, déconcentration répétée pendant l'atelier → <b>observation verbale</b>.
    La famille n'a pas encore été informée. Aucun avertissement écrit n'a été prononcé.</li>
</ul>

<h3>5 · Ce que nous proposons de faire d'ici la séance 5</h3>
<ol>
  <li><b>Appeler quatre familles</b> : SORO (deux absences), DOGBRE (absence + devoirs),
    NGAPELA et AMON (devoirs jamais rendus).</li>
  <li><b>Appeler la famille MBIERE</b> sur la seule question de l'heure d'arrivée.</li>
  <li><b>Rappeler le lien du devoir par message la veille de l'échéance</b> : les deux tiers des
    non-rendus sont des familles qui n'ont pas réagi au premier envoi.</li>
  <li><b>Féliciter nommément</b> les cinq élèves à jour, en début de séance 4.</li>
</ol>

<div class="note">
  <b>Sources et précisions de lecture.</b>
  Présence, retards et discipline : classeur de suivi <i>AcProKidsCodingCampSept2026</i>, onglets
  <i>Présence</i> et <i>Indiscipline</i>. Devoirs : les réponses des quatre formulaires Google, plus le
  relevé du devoir 3 des Jerusalem Geeks transmis par l'enseignant.
  <br>• <b>Devoir 3 non échu.</b> Son échéance est la séance du 3 octobre : les « non rendu » de cette
  colonne ne sont pas des manquements, ils indiquent seulement où nous en sommes ce soir.
  <br>• <b>Une réponse non identifiée.</b> Le devoir 1 comporte une réponse signée « David Dogbre », qui
  ne correspond à aucun nom inscrit. S'il s'agit de Joshua DOGBRE, son devoir 1 est rendu, et le total
  passe de 8 à 9. <b>À confirmer auprès de la famille</b> — c'est la seule incertitude de ce document.
  <br>• <b>Barèmes différents d'un devoir à l'autre</b> : le devoir 2 des Jeremiah Geeks est noté sur 12,
  les autres suivent le barème propre à leur formulaire. Les notes du devoir 3 sont <b>partielles</b> :
  seules les 12 questions à choix sont corrigées automatiquement, les 8 exercices où l'élève écrit du code
  restent à corriger à la main. <b>Aucune note n'est donc définitive.</b>
  <br>• <b>Double envoi</b> : Grâce-Elsa DREESEN a répondu deux fois au devoir 1 ; la meilleure note est retenue.
</div>

<div class="sig">Fait par les deux enseignants du Coding Camp, le 2 octobre 2026.</div>
</body></html>
"""

jetons = {"N": N, "RET": RET, "ABS": ABS, "EXC": EXC,
          "D1": DEV[0], "D2": DEV[1], "D3": DEV[2],
          "TJ": lignes(JERUSALEM, ["", "", ""]),
          "TM": lignes(JEREMIAH, ["", "/12", "/12*"])}
html = HTML
for cle, val in jetons.items():
    html = html.replace("{{%s}}" % cle, str(val))
assert "{{" not in html, "jeton non remplace"
io.open(os.path.join(BASE, "sources", "point-assiduite-et-devoirs.html"), "w", encoding="utf-8").write(html)
print("totaux :", N, "eleves ·", RET, "retards ·", ABS, "absences ·", EXC, "excusees · devoirs", DEV)
