# -*- coding: utf-8 -*-
"""
=============================================================================
  PREPARER LA CLE USB DE LA SEANCE
=============================================================================
  A lancer depuis le dossier du projet :   python outils/preparer_la_cle.py

  Ce programme remplit (ou remet a jour) le dossier  cle-usb/  a partir des
  sources du projet : les fiches, les supports a imprimer, la demo, le code
  officiel. Relancez-le apres CHAQUE modification d'un support, puis copiez
  le dossier  cle-usb/  entier sur la vraie cle.

  Option :  --seance 2   pour preparer la cle d'une autre seance
            --vers E:/   pour ecrire directement sur la cle branchee
=============================================================================
"""

import os
import shutil
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def numero_de_seance():
    if "--seance" in sys.argv:
        return "%02d" % int(sys.argv[sys.argv.index("--seance") + 1])
    return "01"


def destination():
    if "--vers" in sys.argv:
        return sys.argv[sys.argv.index("--vers") + 1]
    return os.path.join(RACINE, "cle-usb")


def copier_fichier(source, cible, journal):
    if not os.path.isfile(source):
        journal.append(("absent", source))
        return
    if os.path.abspath(source) == os.path.abspath(cible):
        journal.append(("ok", cible))       # deja au bon endroit
        return
    dossier = os.path.dirname(cible)
    if not os.path.isdir(dossier):
        os.makedirs(dossier)
    shutil.copy2(source, cible)
    journal.append(("ok", cible))


def principal():
    seance = numero_de_seance()
    cle = destination()
    journal = []

    print("=" * 66)
    print("  PREPARATION DE LA CLE  -  SEANCE %s" % seance)
    print("  Destination : %s" % cle)
    print("=" * 66)

    # 1 - la demo et les outils de l'enseignant
    for nom in ("xo_complet.py", "verifier_le_jeu.py", "live_coding_S%s.py" % seance):
        copier_fichier(os.path.join(RACINE, "demo", nom),
                       os.path.join(cle, "1-DEMO", nom), journal)

    # 2 - le dossier GEEKS a installer sur les postes
    geeks = os.path.join(cle, "2-A-COPIER-SUR-LES-POSTES", "GEEKS")
    copier_fichier(os.path.join(RACINE, "supports", "S%s" % seance, "piste_bleue_jeu.py"),
                   os.path.join(geeks, "mon_xo", "jeu.py"), journal)
    if seance != "01":       # des la seance 2, le filet part du code precedent
        precedente = "%02d" % (int(seance) - 1)
        copier_fichier(os.path.join(RACINE, "code-officiel", "S%s" % precedente, "jeu.py"),
                       os.path.join(geeks, "xo_officiel", "jeu.py"), journal)
    else:
        dossier = os.path.join(geeks, "xo_officiel")
        if not os.path.isdir(dossier):
            os.makedirs(dossier)
        journal.append(("ok", dossier + "  (vide : normal a la seance 1)"))

    # 3 - les supports a imprimer
    source_impressions = os.path.join(RACINE, "impressions")
    for nom in sorted(os.listdir(source_impressions)):
        if nom.endswith((".html", ".md")):
            copier_fichier(os.path.join(source_impressions, nom),
                           os.path.join(cle, "3-SUPPORTS-A-IMPRIMER", nom), journal)

    # 4 - l'emplacement des sauvegardes eleves
    dossier = os.path.join(cle, "4-SAUVEGARDES-ELEVES", "S%s" % seance)
    if not os.path.isdir(dossier):
        os.makedirs(dossier)
    journal.append(("ok", dossier))

    # 5 - mes fiches d'animation
    for chemin, nom in (
        (os.path.join("docs", "seances", "S%s-decollage.md" % seance), "fiche-de-seance.md"),
        (os.path.join("docs", "seances", "S%s-script-animateur.html" % seance), "MON-SCRIPT.html"),
        (os.path.join("docs", "S%s-fiche-de-validation.html" % seance), "fiche-de-validation.html"),
    ):
        copier_fichier(os.path.join(RACINE, chemin),
                       os.path.join(cle, "5-MES-FICHES", nom), journal)

    # 6 - le code officiel des seances deja faites
    dossier_officiel = os.path.join(RACINE, "code-officiel")
    if os.path.isdir(dossier_officiel):
        for nom in sorted(os.listdir(dossier_officiel)):
            fichier = os.path.join(dossier_officiel, nom, "jeu.py")
            if os.path.isfile(fichier):
                copier_fichier(fichier, os.path.join(cle, "6-CODE-OFFICIEL", nom, "jeu.py"), journal)

    copier_fichier(os.path.join(RACINE, "cle-usb", "installer_sur_ce_poste.py"),
                   os.path.join(cle, "installer_sur_ce_poste.py"), journal)

    manquants = [c for etat, c in journal if etat == "absent"]
    print("  %d element(s) ecrits." % sum(1 for e, _ in journal if e == "ok"))
    if manquants:
        print()
        print("  ATTENTION, %d fichier(s) introuvable(s) (normal s'ils n'existent" % len(manquants))
        print("  pas encore pour cette seance) :")
        for chemin in manquants:
            print("    - %s" % os.path.relpath(chemin, RACINE))
    print("=" * 66)
    print("  Copiez maintenant TOUT le contenu de  %s" % cle)
    print("  a la racine de la vraie cle USB.")
    print("=" * 66)
    return 0


if __name__ == "__main__":
    sys.exit(principal())
