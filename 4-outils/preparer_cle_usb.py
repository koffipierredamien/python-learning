# -*- coding: utf-8 -*-
"""
=============================================================================
  PREPARER LA CLE USB D'UNE SEANCE
=============================================================================
  A lancer depuis le dossier du projet :

        python 4-outils/preparer_cle_usb.py

  Il fabrique (ou remet a jour) un dossier  cle-usb/  contenant tout ce qu'il
  faut emporter le samedi. Vous copiez ensuite TOUT son contenu a la racine
  de la vraie cle.

  Ce dossier n'est PAS conserve dans le depot : c'est un assemblage de
  fichiers qui existent deja ailleurs. On le refabrique en 2 secondes.

  Options :
      --seance 2       preparer la cle d'une autre seance
      --vers E:/       ecrire directement sur la cle branchee
=============================================================================
"""

import os
import shutil
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LISEZ_MOI = """\
=====================================================================
  CLE USB  -  SEANCE {numero}
=====================================================================

  LES 3 GESTES A FAIRE AVEC CETTE CLE

  1. AVANT LA SEANCE, sur CHAQUE poste de la salle :
     ouvrez  installer_dossier_geeks.py  dans Thonny, puis F5.
     Le dossier GEEKS apparait sur le Bureau.
     Verifiez ensuite avec  1-DEMO/verifier_un_poste.py  (F5).

  2. PENDANT LA SEANCE, a 110 minutes :
     devant les eleves, vous copiez le fichier de
     5-CODE-OFFICIEL/ dans GEEKS/xo_officiel/ de votre machine.
     C'est le moment du FILET.

  3. EN FIN DE SEANCE :
     le Mecanicien passe avec la cle et copie le travail de chaque
     binome dans  4-SAUVEGARDES-ELEVES/

=====================================================================
  1-DEMO/               le jeu fini (le WOW), l'anti-seche du live
                        coding, et le verificateur de poste
  2-A-IMPRIMER/         les PDF, deja au bon format
  3-MES-FICHES/         la fiche de seance, le Kahoot, le deroule Word
  4-SAUVEGARDES-ELEVES/ ou l'on depose le travail des binomes
  5-CODE-OFFICIEL/      le code de reference publie en fin de seance
=====================================================================
"""


def option(nom, defaut=None):
    return sys.argv[sys.argv.index(nom) + 1] if nom in sys.argv else defaut


def dossier_de_seance(numero):
    seances = os.path.join(RACINE, "2-seances")
    for nom in sorted(os.listdir(seances)):
        if nom.startswith("S%s" % numero):
            return os.path.join(seances, nom)
    return None


def copier(source, cible, journal):
    if not os.path.isfile(source):
        journal.append(("absent", source))
        return
    if os.path.abspath(source) == os.path.abspath(cible):
        journal.append(("ok", cible))
        return
    dossier = os.path.dirname(cible)
    if not os.path.isdir(dossier):
        os.makedirs(dossier)
    shutil.copy2(source, cible)
    journal.append(("ok", cible))


def principal():
    numero = "%02d" % int(option("--seance", "1"))
    cle = option("--vers", os.path.join(RACINE, "cle-usb"))
    seance = dossier_de_seance(numero)
    journal = []

    print("=" * 66)
    print("  PREPARATION DE LA CLE  -  SEANCE %s" % numero)
    print("  Destination : %s" % cle)
    print("=" * 66)

    if seance is None:
        print("[ERREUR] Aucun dossier 2-seances/S%s... trouve." % numero)
        return 1

    # 1 - a la racine : ce que l'on lance sur chaque poste
    copier(os.path.join(RACINE, "4-outils", "installer_dossier_geeks.py"),
           os.path.join(cle, "installer_dossier_geeks.py"), journal)
    for nom in sorted(os.listdir(os.path.join(seance, "code"))):
        if nom.startswith("depart"):
            copier(os.path.join(seance, "code", nom), os.path.join(cle, nom), journal)

    # 2 - la demo et les outils de l'enseignant
    copier(os.path.join(RACINE, "4-outils", "jeu_xo_complet.py"),
           os.path.join(cle, "1-DEMO", "jeu_xo_complet.py"), journal)
    copier(os.path.join(RACINE, "4-outils", "verifier_un_poste.py"),
           os.path.join(cle, "1-DEMO", "verifier_un_poste.py"), journal)
    copier(os.path.join(seance, "code", "live_coding_antiseche.py"),
           os.path.join(cle, "1-DEMO", "live_coding_antiseche.py"), journal)

    # 3 - les documents
    a_imprimer = os.path.join(seance, "a-imprimer")
    if os.path.isdir(a_imprimer):
        for nom in sorted(os.listdir(a_imprimer)):
            copier(os.path.join(a_imprimer, nom),
                   os.path.join(cle, "2-A-IMPRIMER", nom), journal)
    copier(os.path.join(seance, "fiche-de-seance.md"),
           os.path.join(cle, "3-MES-FICHES", "fiche-de-seance.md"), journal)
    for sous, cible_sous in (("kahoot", "3-MES-FICHES"), ("a-envoyer", "3-MES-FICHES")):
        dossier_src = os.path.join(seance, sous)
        if os.path.isdir(dossier_src):
            for nom in sorted(os.listdir(dossier_src)):
                copier(os.path.join(dossier_src, nom),
                       os.path.join(cle, cible_sous, nom), journal)

    # 4 - l'emplacement des sauvegardes eleves
    dossier = os.path.join(cle, "4-SAUVEGARDES-ELEVES", "S%s" % numero)
    if not os.path.isdir(dossier):
        os.makedirs(dossier)
    journal.append(("ok", dossier))

    # 5 - le code officiel : celui de CETTE seance (publie a 110 min) et,
    #     des la seance 2, celui de la precedente, que l'installateur
    #     deposera directement dans xo_officiel/
    copier(os.path.join(seance, "code", "code_officiel_fin_de_seance.py"),
           os.path.join(cle, "5-CODE-OFFICIEL", "S%s-jeu.py" % numero), journal)
    if numero != "01":
        precedent = dossier_de_seance("%02d" % (int(numero) - 1))
        if precedent:
            copier(os.path.join(precedent, "code", "code_officiel_fin_de_seance.py"),
                   os.path.join(cle, "code-officiel", "jeu.py"), journal)

    with open(os.path.join(cle, "LISEZ-MOI.txt"), "w", encoding="utf-8") as f:
        f.write(LISEZ_MOI.format(numero=numero))
    journal.append(("ok", os.path.join(cle, "LISEZ-MOI.txt")))

    manquants = [c for etat, c in journal if etat == "absent"]
    print("  %d element(s) ecrits." % sum(1 for e, _ in journal if e == "ok"))
    if manquants:
        print()
        print("  ATTENTION, %d fichier(s) introuvable(s) :" % len(manquants))
        for chemin in manquants:
            print("    - %s" % os.path.relpath(chemin, RACINE))
    print("=" * 66)
    print("  Copiez maintenant TOUT le contenu de  %s" % cle)
    print("  a la racine de la vraie cle USB.")
    print("=" * 66)
    return 0


if __name__ == "__main__":
    sys.exit(principal())
