# -*- coding: utf-8 -*-
"""
=============================================================================
  FABRIQUER LES DEUX ENVOIS DE RÉVISION DE LA SEMAINE
=============================================================================
  Chaque semaine, deux envois partent aux parents par message :

      envoi 1, en semaine  : le quiz de la semaine (sans ordinateur)
      envoi 2, avant le samedi : le défi de la semaine

  Le programme écrit, dans  2-seances/S01-decollage/a-envoyer/revisions-maison/ :

      envoi-1.html · envoi-2.html   -> les PDF à joindre au message
      messages-a-copier.md          -> le texte du message, et les réponses

  Utilisation :  python 4-outils/faire_les_revisions.py
                 python 4-outils/faire_les_revisions.py --seance 2

  Les PDF se fabriquent ensuite avec :
                 python 4-outils/faire_les_pdf.py --seance 1
=============================================================================
"""
import os, sys, html

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# =========================================================== LE CONTENU
# Une entrée par séance. Tout ce qui est demandé à la maison ne porte que sur
# ce qui a déjà été fait en classe.

SEMAINES = {
 1: {
  "seance": "Séance 1 — Le décollage",
  "envoi1": {
    "jour": "mardi 15 septembre 2026",
    "titre": "Le quiz de la semaine",
    "intro": "Six questions sur ce qu'on a vu samedi. Aucun ordinateur n'est nécessaire : "
             "on répond sur une feuille, puis on renvoie les réponses par message.",
    "questions": [
      ("Que fait la commande print en Python ?",
       ["elle affiche du texte à l'écran", "elle imprime sur du papier", "elle calcule"], "A"),
      ("Au fond, l'ordinateur ne comprend que…",
       ["le français", "des 0 et des 1", "des images"], "B"),
      ("Un algorithme, c'est…",
       ["un ordinateur très rapide", "une suite d'ordres précis, dans le bon ordre",
        "un langage de programmation"], "B"),
      ("Comment s'appelle le logiciel dans lequel on écrit notre code ?",
       ["Python", "Thonny", "Windows"], "B"),
      ("L'ordinateur lit ton programme…",
       ["de haut en bas, ligne par ligne", "dans le désordre", "de bas en haut"], "A"),
      ("Combien de guillemets faut-il autour d'un texte ?",
       ["un seul", "deux : un avant, un après", "aucun"], "B"),
    ],
    "ouverte": "Cite un métier, un objet ou un domaine de ta vie où il y a du code. "
               "Écris une phrase pour dire à quoi le code y sert.",
    "renvoyer": "Renvoie tes réponses par message, comme ceci :  1A  2B  3B  4B  5A  6B, "
                "puis ta phrase.",
  },
  "envoi2": {
    "jour": "vendredi 18 septembre 2026",
    "titre": "Le défi de la semaine",
    "intro": "Un défi sans ordinateur, que tout le monde peut faire. Et un second défi, "
             "seulement pour ceux qui ont un ordinateur à la maison.",
    "defi1": ("Défi de tout le monde — sans ordinateur",
      ["Prends une feuille. Choisis une chose que tu fais tous les jours : préparer un thé, "
       "te brosser les dents, aller à l'école.",
       "Écris les étapes dans l'ordre, une par ligne, de 5 à 8 étapes. Sois très précis : "
       "l'ordinateur, lui, ne devine rien.",
       "Relis-les à voix haute à quelqu'un de ta famille, et demande-lui de faire exactement "
       "ce qui est écrit. S'il se trompe, c'est qu'une étape manque : corrige-la.",
       "Tu viens d'écrire un algorithme. C'est exactement ce que nous avons fait en classe "
       "avec le robot humain."]),
    "defi2": ("Défi en plus — seulement si tu as un ordinateur",
      ["Ouvre Thonny.",
       "Écris trois lignes, en changeant le texte par le tien :",
       "print(\"Je m'appelle …\")",
       "print(\"J'ai … ans\")",
       "print(\"Je construis le jeu XO\")",
       "Appuie sur F5 pour lancer. Si l'écran devient rouge, lis le message : "
       "il te dit ce qu'il n'a pas compris. Vérifie tes guillemets et tes parenthèses."]),
    "renvoyer": "Renvoie une photo de ta feuille par message. Et, si tu as fait le défi en plus, "
                "une photo de ton écran.",
  },
 },
}

RAPPEL = ("Ces révisions sont facultatives : personne n'est puni s'il ne les fait pas. "
          "Elles prennent dix minutes, et elles suffisent pour ne rien oublier d'une semaine à l'autre.")
CONTACT = "+212 680 706 164"
FIN = "Ensemble pour leur avenir !"


# ============================================================== une page HTML
GABARIT = """<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>{titre} — {seance}</title>
<style>
  html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  * {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; box-sizing:border-box; }}
  @page {{ size: A5 portrait; margin: 9mm 10mm; }}
  body {{ margin:0; font-family: Candara, Calibri, Arial, sans-serif; font-size:10.5pt;
          color:#111; line-height:1.32; }}
  .haut {{ border-bottom:.8mm solid #356854; padding-bottom:1.5mm; margin-bottom:3mm; }}
  .org {{ font-size:9pt; color:#1d3f5e; font-weight:bold; }}
  .classe {{ font-size:8.5pt; color:#666; }}
  h1 {{ font-size:15pt; color:#1d3f5e; margin:0 0 .8mm; }}
  .jour {{ font-size:9.5pt; color:#356854; font-weight:bold; margin-bottom:2mm; }}
  .intro {{ font-size:9.5pt; margin:0 0 3mm; }}
  .q {{ margin-bottom:2.6mm; }}
  .q .n {{ font-weight:bold; color:#1d3f5e; }}
  .rep {{ margin:.4mm 0 0 6mm; font-size:9.5pt; }}
  h2 {{ font-size:11pt; color:#356854; margin:3mm 0 1.5mm; border-bottom:.3mm solid #cfe0d8;
        padding-bottom:1mm; }}
  ol, ul {{ margin:0 0 0 5mm; padding:0; }}
  li {{ margin-bottom:1.2mm; }}
  code {{ font-family: Consolas, monospace; font-size:10pt; background:#f2f2f2; padding:.3mm 1mm; }}
  .cadre {{ border:.5mm solid #1d3f5e; padding:2.5mm; margin-top:3mm; font-size:9.5pt; }}
  .rappel {{ font-size:8.5pt; color:#555; font-style:italic; margin-top:2.5mm; }}
  .fin {{ text-align:center; font-size:9pt; color:#356854; font-style:italic; margin-top:2mm; }}
</style></head><body>
<div class="haut">
  <div class="org">✝ VISION PLÉNITUDES VIE — AcProKids Coding Camp</div>
  <div class="classe">{seance} · Jerusalem Geeks &amp; Jeremiah Geeks</div>
</div>
<h1>{titre}</h1>
<div class="jour">À faire pour le {jour}</div>
<p class="intro">{intro}</p>
{corps}
<div class="cadre"><b>Comment renvoyer.</b> {renvoyer}<br>
Par message au <b>{contact}</b>.</div>
<p class="rappel">{rappel}</p>
<div class="fin">{fin}</div>
</body></html>
"""


def echapper(t):
    return html.escape(t)


def page_envoi1(seance, e):
    corps = []
    for i, (q, reps, _) in enumerate(e["questions"], start=1):
        lettres = "ABC"
        lignes = '<div class="rep">%s</div>' % " &nbsp;·&nbsp; ".join(
            "<b>%s.</b> %s" % (lettres[j], echapper(r)) for j, r in enumerate(reps))
        corps.append('<div class="q"><span class="n">%d.</span> %s%s</div>'
                     % (i, echapper(q), lignes))
    corps.append('<h2>Et une question pour réfléchir</h2><p>%s</p>' % echapper(e["ouverte"]))
    return GABARIT.format(titre=echapper(e["titre"]), seance=echapper(seance),
                          jour=echapper(e["jour"]), intro=echapper(e["intro"]),
                          corps="\n".join(corps), renvoyer=echapper(e["renvoyer"]),
                          contact=CONTACT, rappel=echapper(RAPPEL), fin=FIN)


def page_envoi2(seance, e):
    corps = []
    for titre, etapes in (e["defi1"], e["defi2"]):
        corps.append("<h2>%s</h2>" % echapper(titre))
        corps.append("<ol>" + "".join("<li>%s</li>" % echapper(x) for x in etapes) + "</ol>")
    return GABARIT.format(titre=echapper(e["titre"]), seance=echapper(seance),
                          jour=echapper(e["jour"]), intro=echapper(e["intro"]),
                          corps="\n".join(corps), renvoyer=echapper(e["renvoyer"]),
                          contact=CONTACT, rappel=echapper(RAPPEL), fin=FIN)


# ================================================== les messages à copier-coller
def messages(numero, s):
    e1, e2 = s["envoi1"], s["envoi2"]
    reponses = "  ".join("%d%s" % (i, bonne) for i, (_, _, bonne)
                         in enumerate(e1["questions"], start=1))
    lignes = []
    a = lignes.append
    a("# 📲 Les deux messages de la semaine — %s" % s["seance"])
    a("")
    a("Deux envois par semaine, aux parents. On joint le PDF, et on copie le texte ci-dessous.")
    a("Ce qui revient se note dans l'onglet **Révisions maison** du classeur : `O` si l'apprenant "
      "a répondu, `N` si rien n'est revenu.")
    a("")
    a("---")
    a("")
    a("## Envoi 1 — %s" % e1["jour"])
    a("")
    a("**À joindre :** `envoi-1.pdf`")
    a("")
    a("```")
    a("Bonjour, et que la paix soit avec vous.")
    a("Voici le quiz de révision de la semaine pour votre enfant.")
    a("Six questions sur ce que nous avons vu samedi. Aucun ordinateur n'est nécessaire,")
    a("cela prend dix minutes.")
    a("Les réponses se renvoient par message, sous la forme : 1A 2B 3B ...")
    a("C'est facultatif, et personne n'est puni s'il ne le fait pas.")
    a("Merci pour votre aide.")
    a("AcProKids Coding Camp — Vision Plénitudes Vie")
    a("```")
    a("")
    a("**Les réponses, pour vous :** `%s`" % reponses)
    a("")
    for i, (q, reps, bonne) in enumerate(e1["questions"], start=1):
        a("%d. %s → **%s. %s**" % (i, q, bonne, reps["ABC".index(bonne)]))
    a("")
    a("> La question ouverte n'a pas de réponse unique : toute réponse qui cite un domaine et "
      "dit à quoi le code y sert est juste.")
    a("")
    a("---")
    a("")
    a("## Envoi 2 — %s" % e2["jour"])
    a("")
    a("**À joindre :** `envoi-2.pdf`")
    a("")
    a("```")
    a("Bonjour. Voici le défi de la semaine avant notre séance de samedi.")
    a("Le premier défi se fait sur une feuille, sans ordinateur : tout le monde peut le faire.")
    a("Le second est en plus, seulement pour ceux qui ont un ordinateur à la maison.")
    a("Une photo de la feuille se renvoie par message.")
    a("C'est facultatif. Rendez-vous samedi à 12 h.")
    a("AcProKids Coding Camp — Vision Plénitudes Vie")
    a("```")
    a("")
    a("**Ce qu'on regarde dans les réponses :** les étapes sont-elles dans le bon ordre, et "
      "assez précises pour être exécutées telles quelles ? C'est tout. On ne note pas.")
    a("")
    a("---")
    a("")
    a("## En classe, samedi")
    a("")
    a("Deux minutes au début de la séance : on demande qui a fait le quiz, on donne les bonnes "
      "réponses à voix haute, et on lit un algorithme reçu. Ceux qui n'ont rien envoyé ne sont "
      "pas nommés.")
    return "\n".join(lignes) + "\n"


def principal():
    numero = int(sys.argv[sys.argv.index("--seance") + 1]) if "--seance" in sys.argv else 1
    if numero not in SEMAINES:
        print("[ERREUR] Le contenu de la semaine %d n'est pas encore écrit." % numero)
        print("         Il s'ajoute dans SEMAINES, dans ce fichier : les révisions ne portent")
        print("         que sur ce qui a déjà été fait en classe.")
        return 1
    s = SEMAINES[numero]

    seances = os.path.join(RACINE, "2-seances")
    dossier_seance = next((os.path.join(seances, n) for n in sorted(os.listdir(seances))
                           if n.startswith("S%02d" % numero)), None)
    if dossier_seance is None:
        print("[ERREUR] Aucun dossier 2-seances/S%02d... trouve." % numero)
        return 1
    dossier = os.path.join(dossier_seance, "a-envoyer", "revisions-maison")
    if not os.path.isdir(dossier):
        os.makedirs(dossier)

    ecrits = [
        ("envoi-1.html", page_envoi1(s["seance"], s["envoi1"])),
        ("envoi-2.html", page_envoi2(s["seance"], s["envoi2"])),
        ("messages-a-copier.md", messages(numero, s)),
    ]
    for nom, contenu in ecrits:
        chemin = os.path.join(dossier, nom)
        with open(chemin, "w", encoding="utf-8") as f:
            f.write(contenu)
        print("  + %s" % os.path.relpath(chemin, RACINE))
    print()
    print("  Les PDF se fabriquent ensuite avec :  python 4-outils/faire_les_pdf.py --seance %d" % numero)
    return 0


if __name__ == "__main__":
    sys.exit(principal())
