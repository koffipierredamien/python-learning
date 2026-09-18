# -*- coding: utf-8 -*-
"""
=============================================================================
  REFABRIQUER LES PDF D'UNE SEANCE
=============================================================================
  Convertit en PDF tous les fichiers .html d'une seance, au bon format de
  papier et avec les couleurs. La regle est simple :

    a-imprimer/sources/*.html   ->  le PDF monte dans  a-imprimer/
    tout autre  *.html          ->  le PDF est ecrit a cote de sa source

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


def travaux_d_un_dossier(racine_du_lot, dossier_de_sortie):
    """Liste les (source .html, PDF a ecrire) d'un dossier.

    Regle unique : ce qui est dans un sous-dossier "sources" monte dans
    dossier_de_sortie ; tout le reste reste a cote de sa source.
    """
    travaux = []
    for dossier, _, fichiers in os.walk(racine_du_lot):
        for nom in sorted(fichiers):
            if not nom.endswith(".html"):
                continue
            source = os.path.join(dossier, nom)
            if os.path.basename(dossier) == "sources":
                cible = os.path.join(dossier_de_sortie, nom[:-5] + ".pdf")
            else:
                cible = os.path.join(dossier, nom[:-5] + ".pdf")
            travaux.append((source, cible))
    travaux.sort(key=lambda t: t[1])
    return travaux


def le_lot_demande():
    """Renvoie (titre, dossier de reference, liste des travaux) ou None."""
    numero = "%02d" % int(sys.argv[sys.argv.index("--seance") + 1]) if "--seance" in sys.argv else "01"
    seances = os.path.join(RACINE, "2-seances")
    seance = next((os.path.join(seances, n) for n in sorted(os.listdir(seances))
                   if n.startswith("S" + numero)), None)
    if seance is None:
        print("[ERREUR] Aucun dossier 2-seances/S%s... trouve." % numero)
        return None
    return ("SEANCE %s" % numero, seance,
            travaux_d_un_dossier(seance, os.path.join(seance, "a-imprimer")))


def principal():
    lot = le_lot_demande()
    if lot is None:
        return 1
    titre, dossier_de_reference, travaux = lot
    if not travaux:
        print("[ERREUR] Aucun fichier .html trouve dans %s"
              % os.path.relpath(dossier_de_reference, RACINE))
        return 1

    navigateur = trouver_le_navigateur()
    if navigateur is None:
        print("[ERREUR] Chrome ou Chromium est introuvable sur cette machine.")
        print("         Faites-le a la main : ouvrez chaque .html du dossier dans")
        print("         votre navigateur, Ctrl+P, 'Enregistrer au format PDF', et rangez")
        print("         le resultat sous le meme nom (ceux d'un dossier sources/ montent")
        print("         d'un cran, les autres restent a cote de leur source).")
        return 1

    print("=" * 66)
    print("  PDF - %s" % titre)
    print("  Navigateur : %s" % navigateur)
    print("=" * 66)

    faits = 0
    for source, sortie in travaux:
        dossier = os.path.dirname(sortie)
        if not os.path.isdir(dossier):
            os.makedirs(dossier)
        subprocess.run([navigateur, "--headless", "--disable-gpu", "--no-sandbox",
                        "--no-pdf-header-footer", "--print-to-pdf=" + sortie,
                        "file://" + source],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if os.path.isfile(sortie):
            print("  + %s" % os.path.relpath(sortie, dossier_de_reference))
            faits += 1
        else:
            print("  ! echec : %s" % os.path.relpath(source, dossier_de_reference))

    print("=" * 66)
    print("  %d PDF ecrits" % faits)
    print("=" * 66)
    return 0


if __name__ == "__main__":
    sys.exit(principal())
