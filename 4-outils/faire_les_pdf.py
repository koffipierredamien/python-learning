# -*- coding: utf-8 -*-
"""
=============================================================================
  REFABRIQUER LES PDF D'UNE SEANCE
=============================================================================
  Convertit chaque document de  2-seances/Sxx.../sources/*.html
  en PDF dans  2-seances/Sxx.../a-imprimer/ , au bon format de papier et
  avec les couleurs.

        python 4-outils/faire_les_pdf.py            (seance 1)
        python 4-outils/faire_les_pdf.py --seance 2

  Il a besoin de Chrome ou Chromium installe sur la machine.
  Si vous ne l'avez pas : ouvrez le fichier .html dans votre navigateur,
  Ctrl+P, destination "Enregistrer au format PDF", et rangez le resultat
  dans a-imprimer/ sous le meme nom. C'est exactement equivalent.
=============================================================================
"""

import os
import shutil
import subprocess
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NOMS_DE_NAVIGATEUR = (
    "google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome",
)
CHEMINS_CONNUS = (
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
)


def trouver_le_navigateur():
    for nom in NOMS_DE_NAVIGATEUR:
        chemin = shutil.which(nom)
        if chemin:
            return chemin
    for chemin in CHEMINS_CONNUS:
        if os.path.isfile(chemin):
            return chemin
    return None


def principal():
    numero = "%02d" % int(sys.argv[sys.argv.index("--seance") + 1]) if "--seance" in sys.argv else "01"

    seances = os.path.join(RACINE, "2-seances")
    seance = next((os.path.join(seances, n) for n in sorted(os.listdir(seances))
                   if n.startswith("S" + numero)), None)
    if seance is None:
        print("[ERREUR] Aucun dossier 2-seances/S%s... trouve." % numero)
        return 1

    # (dossier des sources, dossier de sortie)
    paires = [(os.path.join(seance, "sources"), os.path.join(seance, "a-imprimer")),
              (os.path.join(seance, "kahoot"), os.path.join(seance, "kahoot"))]
    paires = [(s, c) for s, c in paires if os.path.isdir(s)]
    sources = paires[0][0]
    for _, c in paires:
        if not os.path.isdir(c):
            os.makedirs(c)

    navigateur = trouver_le_navigateur()
    if navigateur is None:
        print("[ERREUR] Chrome ou Chromium est introuvable sur cette machine.")
        print("         Faites-le a la main : ouvrez chaque fichier de")
        print("         %s" % os.path.relpath(sources, RACINE))
        print("         dans votre navigateur, Ctrl+P, 'Enregistrer au format PDF',")
        print("         et rangez le resultat dans a-imprimer/ sous le meme nom.")
        return 1

    print("=" * 66)
    print("  PDF DE LA SEANCE %s" % numero)
    print("  Navigateur : %s" % navigateur)
    print("=" * 66)

    faits = 0
    for dossier_src, cible in paires:
        for nom in sorted(os.listdir(dossier_src)):
            if not nom.endswith(".html"):
                continue
            source = os.path.join(dossier_src, nom)
            sortie = os.path.join(cible, nom[:-5] + ".pdf")
            subprocess.run([navigateur, "--headless", "--disable-gpu", "--no-sandbox",
                            "--no-pdf-header-footer", "--print-to-pdf=" + sortie,
                            "file://" + source],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if os.path.isfile(sortie):
                print("  + %s" % os.path.relpath(sortie, seance))
                faits += 1
            else:
                print("  ! echec : %s" % nom)

    print("=" * 66)
    print("  %d PDF ecrits" % faits)
    print("=" * 66)
    return 0


if __name__ == "__main__":
    sys.exit(principal())
