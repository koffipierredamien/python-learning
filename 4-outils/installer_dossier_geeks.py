# -*- coding: utf-8 -*-
"""
=============================================================================
  INSTALLER LE DOSSIER "GEEKS" SUR CE POSTE
=============================================================================
  A LANCER UNE FOIS SUR CHAQUE ORDINATEUR DE LA SALLE, avant la seance.
  (Et sur votre machine a vous : vous travaillerez dans les memes conditions
  que vos eleves, et vous verrez les memes problemes qu'eux.)

  Ce programme cree sur le Bureau :

      GEEKS/
        |-- mon_xo/            <- le dossier de travail de l'eleve
        |     `-- jeu.py           le fichier de depart, deja pret
        |-- xo_officiel/       <- LE FILET : le code de reference
        `-- LISEZ-MOI.txt

  COMMENT FAIRE
  -------------
  1. Ouvrez ce fichier dans Thonny (ou double-cliquez dessus).
  2. F5. Lisez le rapport. C'est tout.

  IL NE DETRUIT JAMAIS LE TRAVAIL D'UN ELEVE.
  Si un dossier GEEKS existe deja, seuls les fichiers manquants sont ajoutes.
  Pour remettre un poste a neuf :
        python installer_dossier_geeks.py --neuf
=============================================================================
"""

import os
import shutil
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
NOMS_DE_BUREAU = ("Desktop", "Bureau", "Escritorio", "Schreibtisch")

LISEZ_MOI = """\
=====================================================
   DOSSIER GEEKS
   Jerusalem Geeks  -  Jeremiah Geeks
=====================================================

   mon_xo/        <-  TON dossier de travail.
                      C'est ici que tu codes.
                      Ton fichier s'appelle  jeu.py

   xo_officiel/   <-  LE FILET.
                      Le code de reference, donne par
                      le prof au debut de chaque seance.
                      N'y touche pas : c'est ta copie
                      de secours.

-----------------------------------------------------
   TU AS TOUT CASSE ?  CE N'EST PAS GRAVE.
   Recopie le fichier de  xo_officiel  dans  mon_xo
   et tu repars propre. Personne ne te grondera :
   c'est fait pour ca.
=====================================================
"""


def trouver_le_bureau():
    """Renvoie le chemin du Bureau, en essayant plusieurs pistes."""
    maison = os.path.expanduser("~")

    for nom in NOMS_DE_BUREAU:                       # 1. le cas normal
        chemin = os.path.join(maison, nom)
        if os.path.isdir(chemin):
            return chemin

    if os.path.isdir(maison):                        # 2. Windows avec OneDrive
        for dossier in os.listdir(maison):
            if dossier.lower().startswith("onedrive"):
                for nom in NOMS_DE_BUREAU:
                    chemin = os.path.join(maison, dossier, nom)
                    if os.path.isdir(chemin):
                        return chemin

    try:                                             # 3. Linux dans une autre langue
        import subprocess
        chemin = subprocess.check_output(
            ["xdg-user-dir", "DESKTOP"], stderr=subprocess.DEVNULL).decode().strip()
        if chemin and os.path.isdir(chemin):
            return chemin
    except Exception:
        pass

    return maison                                    # 4. on abandonne


def trouver_le_fichier_de_depart():
    """
    Cherche le fichier que l'eleve trouvera dans mon_xo/jeu.py, dans l'ordre :
      1. l'option --depart <chemin>
      2. un fichier depart-*.py pose a cote de ce script (cas de la cle USB)
      3. l'arborescence du projet (cas ou on lance depuis le depot)
    """
    if "--depart" in sys.argv:
        return sys.argv[sys.argv.index("--depart") + 1]

    for nom in sorted(os.listdir(ICI)):
        if nom.startswith("depart") and nom.endswith(".py"):
            return os.path.join(ICI, nom)

    racine = os.path.dirname(ICI)
    seances = os.path.join(racine, "2-seances")
    if os.path.isdir(seances):
        for seance in sorted(os.listdir(seances)):
            dossier = os.path.join(seances, seance, "code")
            if os.path.isdir(dossier):
                for nom in sorted(os.listdir(dossier)):
                    if nom.startswith("depart") and nom.endswith(".py"):
                        return os.path.join(dossier, nom)
    return None


def ecrire(chemin, contenu, ecraser, journal):
    if os.path.exists(chemin) and not ecraser:
        journal.append(("conserve", chemin))
        return
    etat = "remplace" if os.path.exists(chemin) else "copie"
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(contenu)
    journal.append((etat, chemin))


def principal():
    ecraser = "--neuf" in sys.argv

    print("=" * 64)
    print("  INSTALLATION DU DOSSIER GEEKS")
    print("=" * 64)

    depart = trouver_le_fichier_de_depart()
    if depart is None or not os.path.isfile(depart):
        print("[ERREUR] Je ne trouve pas le fichier de depart des eleves.")
        print("         Lancez ce programme depuis la cle USB preparee, ou")
        print("         depuis le dossier 4-outils/ du projet, ou indiquez-le :")
        print("         python installer_dossier_geeks.py --depart chemin/du/fichier.py")
        return 1

    bureau = trouver_le_bureau()
    cible = os.path.join(bureau, "GEEKS")
    print("  Bureau detecte  : %s" % bureau)
    print("  Dossier a creer : %s" % cible)
    print("  Fichier eleve   : %s" % os.path.basename(depart))
    if ecraser:
        print("  Mode --neuf : les fichiers existants seront REMPLACES.")
    print("-" * 64)

    journal = []
    try:
        for sous_dossier in ("", "mon_xo", "xo_officiel"):
            chemin = os.path.join(cible, sous_dossier) if sous_dossier else cible
            if not os.path.isdir(chemin):
                os.makedirs(chemin)
                journal.append(("cree", chemin))

        ecrire(os.path.join(cible, "LISEZ-MOI.txt"), LISEZ_MOI, ecraser, journal)

        jeu = os.path.join(cible, "mon_xo", "jeu.py")
        if os.path.exists(jeu) and not ecraser:
            journal.append(("conserve", jeu))
        else:
            etat = "remplace" if os.path.exists(jeu) else "copie"
            shutil.copy2(depart, jeu)
            journal.append((etat, jeu))

        # le code officiel des seances precedentes, s'il est pose a cote
        officiel = os.path.join(ICI, "code-officiel")
        if os.path.isdir(officiel):
            for nom in sorted(os.listdir(officiel)):
                if nom.endswith(".py"):
                    cible_off = os.path.join(cible, "xo_officiel", "jeu.py")
                    shutil.copy2(os.path.join(officiel, nom), cible_off)
                    journal.append(("copie", cible_off))
    except PermissionError:
        print("[ERREUR] Ecriture refusee sur ce poste (droits insuffisants).")
        print("         Demandez a l'administrateur, ou installez le dossier")
        print("         GEEKS dans le dossier personnel de l'eleve.")
        return 1

    marques = {"cree": "+ dossier ", "copie": "+ fichier ",
               "remplace": "~ remplace", "conserve": "= conserve"}
    for action, chemin in journal:
        print("  %s  %s" % (marques[action], os.path.relpath(chemin, bureau)))

    conserves = sum(1 for action, _ in journal if action == "conserve")
    print("-" * 64)
    print("  TERMINE.")
    if conserves and not ecraser:
        print("  %d fichier(s) deja presents ont ete conserves (travail des eleves)." % conserves)
        print("  Pour tout remettre a neuf : python installer_dossier_geeks.py --neuf")
    print()
    print("  A VERIFIER MAINTENANT SUR CE POSTE :")
    print("    1. Le dossier GEEKS est visible sur le Bureau")
    print("    2. Thonny s'ouvre")
    print("    3. GEEKS/mon_xo/jeu.py s'ouvre dans Thonny et s'execute avec F5")
    print("    4. La police de Thonny est en taille 18 (Outils > Options > Editeur)")
    print("=" * 64)
    return 0


if __name__ == "__main__":
    sys.exit(principal())
